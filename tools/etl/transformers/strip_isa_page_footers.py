"""Transformer: strip ISA page-footer blokken.

ISA-PDF's van IBR-IRE (NL-vertaling NBA-IBR) bevatten op elke pagina een
herhaald footer-blok dat in de pymupdf-conversie inline tussen de body-tekst
landt. Een typisch blok ziet eruit als:

    ALGEHELE DOELSTELLINGEN VAN DE ONAFHANKELIJKE AUDITOR, ALSMEDE HET
    UITVOEREN VAN EEN CONTROLE OVEREENKOMSTIG DE
    INTERNATIONAL STANDARDS ON AUDITING


    ISA 200
    NBA-IBR 2022
    3/28
    Originele bron: Handbook of International Quality Management, Auditing,
    Review, Other Assurance, and Related Services Pronouncements, 2022
    Edition Volume I
    Versie 2023

Karakteristieken:
- De ALL-CAPS running-title is variabel maar bevindt zich altijd vlak vóór
  het ISA-anker.
- `ISA <num>` of `ISA <num> (herzien)` is het stabiele anker.
- `NBA-IBR 20XX` of `NBA – IBR 20XX` (en-dash) volgt direct daarna.
- `N/M` paginanummer staat op een eigen regel.
- `Originele bron: Handbook ...` is een lange copyright-regel.
- `Versie 20XX` sluit het blok meestal af.

We strippen het blok als een geheel door de anker-regel (`ISA <num>`) op
te sporen en in een venster vóór + na de noise-regels te verwijderen. Pure
inline `ISA 200`-verwijzingen in zinnen blijven onaangetast omdat die niet
op een eigen regel staan met enkel het anker.

Conform ADR-005 §1: format-agnostische tekst-transformatie. Idempotent.
"""
from __future__ import annotations

import re

# ─── Anker-detectie ──────────────────────────────────────────────────────────

# `ISA 200`, `ISA 315 (herzien)`, `ISA 315 (herzien-2019)`, `ISA 700 (herzien)`
# op een eigen regel — dat is altijd het kop-anker van een page-footer-blok
# (nooit een inline verwijzing want die staat in een zin met punctuatie).
# Variant met optionele suffix ` - Bijlage` (ISA-810 Bijlage-secties).
_ISA_ANCHOR_RE = re.compile(
    r"^\s*ISA\s*\d{3,4}(?:\s*\([^)]+\))?"
    r"(?:\s*[-–]\s*Bijlage(?:\s+\d+)?)?\s*$",
    re.M | re.I,
)

# `NBA-IBR 2022` / `NBA – IBR 2023` / `NBA - IBR 2022` (en-dash + spaties)
_NBA_IBR_RE = re.compile(
    r"^\s*NBA\s*[-–]\s*IBR\s*\d{4}\s*$",
    re.M,
)

# Geglue-de anker-regel: `ISA 810 (herzien)<spaces>NBA-IBR 2025` op één regel,
# eventueel met page-nummer er achter geglue-d (`ISA 805 (herzien)<sp>NBA-IBR
# 2025<sp>5/27`). Komt voor bij ISA-805/810 + andere recentere updates.
_ISA_NBA_GLUED_RE = re.compile(
    r"^\s*ISA\s*\d{3,4}(?:\s*\([^)]+\))?\s+NBA\s*[-–]\s*IBR\s*\d{4}"
    r"(?:\s+\d{1,3}\s*/\s*\d{1,4})?\s*$",
    re.M | re.I,
)

# `2/28`, `3/114`, ` 4/50 ` — page-nummer-regel
_PAGE_NUMBER_RE = re.compile(r"^\s*\d{1,3}\s*/\s*\d{1,4}\s*$", re.M)

# `Originele bron : Handbook ...` (met of zonder spatie voor de dubbele punt)
_ORIGINELE_BRON_RE = re.compile(r"^\s*Originele\s+bron\s*:\s+.*$", re.M)

# Continuation-regels van een wrap-gesplitste `Originele bron`-regel.
# Voorbeelden uit ISA-810/200:
#   `Pronouncements, 2022 Edition Volume I`
#   `Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0.`
# We accepteren ze als "noise" wanneer ze direct na een geaccepteerde
# Originele-bron-regel volgen.
_HANDBOOK_CONT_RE = re.compile(
    r"^\s*(?:Pronouncements,\s*)?\d{4}\s+Edition\s+Volume\b.*$",
    re.M,
)

# `Versie 2023` / `Version 2025` standalone
_VERSIE_RE = re.compile(r"^\s*(?:Versie|Version)\s+\d{4}\s*$", re.M)

# All-caps running title: regel met minstens 3 woorden, allemaal hoofdletters
# (eventueel met cijfers, leestekens, spaties). Voorbeeld:
#   `ALGEHELE DOELSTELLINGEN VAN DE ONAFHANKELIJKE AUDITOR`
#   `HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN`
#   `CONTROLE-INFORMATIE` (kortere variant — minstens 1 woord)
# We staan ook 1-woordige ALL-CAPS toe (CONTROLE-INFORMATIE) maar enkel
# als ze direct gevolgd worden door het ISA-anker (zie strip-logica).
_ALL_CAPS_LINE_RE = re.compile(
    r"^\s*[A-ZÀ-Ý][A-ZÀ-Ý0-9\-’'.,()\s]{2,}\s*$"
)


def _is_all_caps_running_title(line: str) -> bool:
    """True als regel een ALL-CAPS running title is (≥3 letters, geen lowercase)."""
    stripped = line.strip()
    if not stripped:
        return False
    if len(stripped) < 3:
        return False
    # Mag geen lowercase letters bevatten
    if any(c.islower() for c in stripped):
        return False
    # Moet minstens 3 letters bevatten (geen pure cijfer-regel)
    letters = sum(1 for c in stripped if c.isalpha())
    if letters < 3:
        return False
    return _ALL_CAPS_LINE_RE.match(stripped) is not None


def _strip_footer_block_around(lines: list[str], anchor_idx: int) -> tuple[int, int]:
    """Bepaal het range [start, end) (exclusief end) dat geschrapt moet worden
    rond een gevonden `ISA <num>`-anker op `anchor_idx`.

    We breiden naar voren uit zolang we ALL-CAPS running-title regels of lege
    regels zien (max 6 regels vóór het anker). Naar achteren breiden we uit
    zolang we de bekende noise-regels (NBA-IBR / page-num / Originele bron /
    Versie / lege regels) zien (max 8 regels na het anker).
    """
    start = anchor_idx
    # Backward expand: lege regels en ALL-CAPS running-title regels
    look_back = 0
    while start > 0 and look_back < 6:
        prev = lines[start - 1]
        if prev.strip() == "":
            start -= 1
            look_back += 1
            continue
        if _is_all_caps_running_title(prev):
            start -= 1
            look_back += 1
            continue
        break

    # Forward expand: NBA-IBR + page-num + Originele bron + Versie + lege regels
    end = anchor_idx + 1
    look_fwd = 0
    while end < len(lines) and look_fwd < 10:
        nxt = lines[end]
        if nxt.strip() == "":
            end += 1
            look_fwd += 1
            continue
        if _NBA_IBR_RE.match(nxt):
            end += 1
            look_fwd += 1
            continue
        if _PAGE_NUMBER_RE.match(nxt):
            end += 1
            look_fwd += 1
            continue
        if _ORIGINELE_BRON_RE.match(nxt):
            end += 1
            look_fwd += 1
            continue
        if _HANDBOOK_CONT_RE.match(nxt):
            end += 1
            look_fwd += 1
            continue
        if _VERSIE_RE.match(nxt):
            end += 1
            look_fwd += 1
            continue
        break
    return start, end


def strip_isa_page_footers(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip de repeterende NBA-IBR page-footer-blokken uit een ISA-body."""
    lines = body.split("\n")

    # Verzamel alle anker-indices waar `ISA <num>` op een eigen regel staat,
    # MAAR alleen als het anker NIET in een H1-context staat (regel begint
    # met `#`). De top-titel `# ISA 200 — ...` mag intact blijven.
    delete_ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Sla H1-regels over (de top-titel)
        if line.lstrip().startswith("#"):
            i += 1
            continue
        # Variant A: geglue-de anker `ISA 810 (herzien)   NBA-IBR 2025`
        if _ISA_NBA_GLUED_RE.match(line):
            start, end = _strip_footer_block_around(lines, i)
            delete_ranges.append((start, end))
            i = end
            continue
        # Variant B: gescheiden anker — `ISA 200` op een regel + `NBA-IBR
        # 2022` binnen 3 regels.
        if _ISA_ANCHOR_RE.match(line):
            has_nba = False
            for j in range(i + 1, min(i + 4, len(lines))):
                if _NBA_IBR_RE.match(lines[j]):
                    has_nba = True
                    break
                if lines[j].strip() == "":
                    continue
                # Andere niet-lege regel zonder NBA-IBR → geen footer
                break
            if has_nba:
                start, end = _strip_footer_block_around(lines, i)
                delete_ranges.append((start, end))
                i = end
                continue
        i += 1

    if not delete_ranges:
        # Idempotency-shortcut + behoud whitespace
        return body, frontmatter

    # Bouw de nieuwe regel-lijst op door delete-ranges over te slaan
    keep_mask = [True] * len(lines)
    for start, end in delete_ranges:
        for k in range(start, end):
            keep_mask[k] = False
    new_lines = [ln for ln, keep in zip(lines, keep_mask) if keep]
    new_body = "\n".join(new_lines)

    # Collapse 3+ opeenvolgende blank-regels naar maximaal 2.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
