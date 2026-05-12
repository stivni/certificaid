"""
Transformer: inject_headings_narratief (ADR-005 §4).

Injecteert markdown-headings in narratieve praktijkgidsen (Type 3 PDFs) waarvan
pdftotext_ejustice + simple_mode 0 headings produceert. De transformer herkent
vijf specifieke patronen die in de vijf doelbronnen voorkomen:

  A. `    Vak [Roman] - [titel]` — PB-toelichtingen (deel 1 + 2)
     Typisch: 1-4 spaties inspring, 'Vak' (mixed case), Romein-numeral, dash,
     ALLCAPS-titel. Eventuele vervolgregels (afgebroken ALLCAPS-titel) worden
     samengevoegd tot één heading. Stopt bij mixed-case tekst.

  B. ` HOOFDSTUK [N|Roman]` (alleen numeral op de regel) — Fiscaal Memento
     De titel staat op de VOLGENDE niet-lege regel. De transformer voegt deze
     samen tot `## HOOFDSTUK N — titel`.

  C. ` [Roman] [titel]` (1 spatie + Romein + titel, geen puntjes-leider)
     — Belastinggids ACLVB
     TOC-regels eindigen op puntjes + paginanummer; body-regels niet.

  D. Zelfstandige ALLCAPS-regel op kolom 0, omsloten door lege regels
     — VenB-toelichting (VOORAFGAANDE OPMERKINGEN, GEBRUIKTE AFKORTINGEN, …)
     Wordt NIET getriggerd voor regels die beginnen met `VAK ` (dat zijn
     TOC-regels in de PB-toelichting, niet te converteren).

  E. 1–4 spaties + ALLCAPS-regel, omsloten door lege regels
     — VenB `    VAK - RESERVES`, `    BANKINFORMATIE`, …

Conservatieve heuristiek: bij twijfel NIET annoteren. De transformer
produceert uitsluitend ##-level headings (H2) voor top-level secties.

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations

import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ─── Regex-helpers ────────────────────────────────────────────────────────────

# Romein-numerals (beperkt: I, V, X — geen M/D want die geven valse positieven)
_ROMAN = r"(?:[IVX]+)"

# TOC-leider-dots (4+ punten op een rij) → regel is TOC-entry, geen heading
_TOC_LEADER = re.compile(r"\.{4,}")

# Trailing page number: spatie(s) + 1-4 cijfers aan het einde van de regel
_TRAILING_PAGE = re.compile(r"\s+\d{1,4}\s*$")

# A1. Vak-patroon (PB-toelichtingen): 1-4 spaties + 'Vak' (mixed case) + Roman + ' - '
_VAK_ROMAN = re.compile(
    r"^( {1,4})(Vak) (" + _ROMAN + r") - (.*)$"
)

# A2. VAK-sectie (VenB-toelichting): kolom 0 + 'VAK - ' + ALLCAPS-titel (geen Roman-numeral)
# De VenB-aangifte gebruikt 'VAK - RESERVES', 'VAK - VERWORPEN UITGAVEN', …
# Dit patroon vangt de sectie-headers op kolom 0 zonder context-eis (blank lines),
# omdat de content soms direct na de header-regel volgt.
_VAK_MIN = re.compile(r"^(VAK - )(.+)$")

# B. HOOFDSTUK solo (fiscaal-memento body): 1 spatie + HOOFDSTUK + Roman/cijfer, EINDE REGEL
_HOOFDSTUK_SOLO = re.compile(
    r"^ (HOOFDSTUK) (" + _ROMAN + r"|\d+)$",
    re.IGNORECASE,
)

# C. Roman chapter (belastinggids): precies 1 spatie + Roman + spatie + titel-tekst
_ROMAN_CHAPTER = re.compile(
    r"^ (" + _ROMAN + r") (.+)$"
)

# D. ALL-CAPS standalone (VenB col 0): alleen hoofdletters + spaties + basisleestekens
# Minimum 10 chars en minstens 1 spatie (multi-woord). Kolom 0 (geen leading whitespace).
# De eis van minstens 1 spatie voorkomt dat enkelvoudige ALLCAPS-woorden die als
# titel-fragments verspreid over meerdere regels voorkomen (bv. VERLEEND, BELASTINGKREDIET)
# als heading worden gepromoveerd.
# Uitgesloten:
#   - regels die beginnen met 'VAK [Roman]' (PB-toelichting TOC-regels)
#   - regels die beginnen met Romein-numeral + punt (I., II., …)
_ALLCAPS_COL0 = re.compile(
    r"^([A-Z][A-Z ,/\(\)\-\.]{9,})$"
)
# Eis minstens 1 spatie in de ALL-CAPS regel (multi-woord) — enkelvoudige woorden worden
# niet gepromoveerd (te hoog risico op valse positieven bij gefragmenteerde PDFs).
_ALLCAPS_HAS_SPACE = re.compile(r" ")
# Patronen die patroon D uitsluiten:
#   - VAK [Roman]: PB-toelichting TOC-regels (VAK I -, VAK II -, …)
#     Note: 'VAK - ...' (met koppelteken i.p.v. Romein) is VenB-sectie → NIET uitsluiten
_STARTS_WITH_VAK_ROMAN = re.compile(r"^VAK [IVXLCDM]")
_STARTS_WITH_ROMAN_DOT = re.compile(r"^[IVXLCDM]+\. ")

# E. Ingesprongen ALLCAPS (VenB indented sections): 1-4 spaties + ALLCAPS
_ALLCAPS_INDENTED = re.compile(
    r"^( {1,4})([A-Z][A-Z ,/\(\)\-\.]{4,})$"
)

# Detecteert een ALLCAPS vervolgregel (titel-continuatie in Vak-headings).
# Toegestaan: hoofdletters, spaties, basisleestekens en cijfers (bv. AANSLAGJAAR 2025).
# Uitgesloten: regels die beginnen met een enkelvoudige letter + punt (A., B., …)
# — dit zijn sub-sectie-aanduidingen, geen titel-vervolgregels.
_ALLCAPS_CONTINUATION = re.compile(
    r"^[A-Z][A-Z0-9 ,\-\./\(\)]+$"
)
# Sub-sectie-prefix (A. B. C. … ook meerdere letters) uitsluiten van Vak-continuatie
_SUBSECTION_PREFIX = re.compile(r"^[A-Z]{1,2}\. [A-Z]")


def _is_blank(line: str) -> bool:
    return not line.strip()


def _strip_trailing_page(s: str) -> str:
    """Verwijder een trailing paginanummer (spatie + 1-4 cijfers)."""
    return _TRAILING_PAGE.sub("", s).rstrip()


def inject_headings_narratief(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Injecteer narratieve sectie-headings in de body.

    Verwijdert GEEN bestaande headings; is idempotent voor al-geconverteerde
    regels (regels die al starten met `## ` worden overgeslagen).

    De frontmatter wordt niet gewijzigd — alleen de body wordt verwerkt.
    """
    lines = body.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # Reeds een markdown-heading → pass-through
        if line.lstrip().startswith("#"):
            out.append(line)
            i += 1
            continue

        # ─── Patroon A: Vak [Roman] - [titel] (PB-toelichtingen) ──────────────
        m_vak = _VAK_ROMAN.match(line)
        if m_vak:
            vak_label = m_vak.group(3)  # bijv. "I", "XIV"
            rest = m_vak.group(4).strip()
            # Verwijder trailing paginanummer in de eerste regel
            rest = _strip_trailing_page(rest)

            # Verzamel aansluitende ALLCAPS-vervolgregels (afgebroken titel).
            # Stop bij de eerste niet-ALLCAPS of lege regel.
            title_parts = [rest] if rest else []
            j = i + 1
            while j < n and not _is_blank(lines[j]):
                next_stripped = lines[j].strip()
                # Stop bij sub-sectie-prefix (A. B. C. …) — geen titel-vervolg
                if _SUBSECTION_PREFIX.match(next_stripped):
                    break
                if not _ALLCAPS_CONTINUATION.match(next_stripped):
                    # Geen ALLCAPS-continuatie → dit is al body-tekst
                    break
                title_parts.append(next_stripped)
                j += 1

            full_title = " ".join(p for p in title_parts if p).strip()
            if full_title:
                out.append(f"## Vak {vak_label} - {full_title}")
            else:
                out.append(f"## Vak {vak_label}")

            # j wijst nu naar de eerste non-titel-regel (body-content of lege regel)
            # De geconsumeerde titel-vervolgregels worden overgeslagen.
            i = j
            continue

        # ─── Patroon A2: VAK - [titel] (VenB-toelichting, kolom 0) ───────────
        m_vak_min = _VAK_MIN.match(line)
        if m_vak_min:
            rest = m_vak_min.group(2).strip()
            # Verzamel aansluitende ALLCAPS-vervolgregels (afgebroken titel).
            title_parts = [rest] if rest else []
            j = i + 1
            while j < n and not _is_blank(lines[j]):
                next_stripped = lines[j].strip()
                if _SUBSECTION_PREFIX.match(next_stripped):
                    break
                if not _ALLCAPS_CONTINUATION.match(next_stripped):
                    break
                title_parts.append(next_stripped)
                j += 1
            full_title = " ".join(p for p in title_parts if p).strip()
            if full_title:
                out.append(f"## VAK - {full_title}")
            else:
                out.append("## VAK")
            i = j
            continue

        # ─── Patroon B: HOOFDSTUK N (solo op de regel, fiscaal-memento) ───────
        m_hfst = _HOOFDSTUK_SOLO.match(line)
        if m_hfst:
            numeral = m_hfst.group(2)  # bijv. "1", "II"
            # Zoek de volgende niet-lege regel als titel
            j = i + 1
            while j < n and _is_blank(lines[j]):
                j += 1
            if j < n:
                next_line = lines[j].strip()
                # Controleer dat het een echte titel is (niet datum, paginanummer, …)
                if (next_line
                        and not re.match(r"^\d{1,2}[-./]\d{1,2}[-./]\d{2,4}$", next_line)
                        and not re.match(r"^\d{1,4}$", next_line)
                        and not _TOC_LEADER.search(next_line)):
                    # Titel kan meerregelig zijn (fiscaal-memento wraps headings)
                    titel_parts = [next_line]
                    k = j + 1
                    while k < n and not _is_blank(lines[k]):
                        next_cont = lines[k].strip()
                        # Stop bij mixed-case (content) of datum-regel
                        if not next_cont or next_cont[0].islower():
                            break
                        if re.match(r"(?:Bijgewerkt|Updated|Mis\s+à\s+jour)", next_cont, re.I):
                            break
                        # Stop bij genummerd blok (1., 2., …) of opsomming
                        if re.match(r"^\d+[\.\)]", next_cont):
                            break
                        titel_parts.append(next_cont)
                        k += 1
                    titel = " ".join(p for p in titel_parts if p)
                    out.append(f"## HOOFDSTUK {numeral} — {titel}")
                    # Sla de HOOFDSTUK-regel én de titel-regels over
                    i = k
                    continue
            # Geen geldig titel-vervolg gevonden → pass-through
            out.append(line)
            i += 1
            continue

        # ─── Patroon C: Roman chapter (belastinggids) ─────────────────────────
        m_roman = _ROMAN_CHAPTER.match(line)
        if m_roman:
            roman = m_roman.group(1)
            title = m_roman.group(2).strip()
            # Negeer als dots-leider of trailing paginanummer aanwezig
            if not _TOC_LEADER.search(title) and not _TRAILING_PAGE.search(title):
                out.append(f"## {roman} {title}")
                i += 1
                continue

        # ─── Patroon D: ALL-CAPS col-0, omsloten door lege regels ─────────────
        m_col0 = _ALLCAPS_COL0.match(line)
        if (m_col0
                and _ALLCAPS_HAS_SPACE.search(line)
                and not _STARTS_WITH_VAK_ROMAN.match(line)
                and not _STARTS_WITH_ROMAN_DOT.match(line)):
            # Controleer of vorige regel leeg is
            prev_blank = (i == 0) or _is_blank(lines[i - 1])
            # Controleer of volgende regel leeg is (of einde bestand)
            next_blank = (i + 1 >= n) or _is_blank(lines[i + 1])
            if prev_blank and next_blank:
                title = m_col0.group(1).strip()
                out.append(f"## {title}")
                i += 1
                continue

        # ─── Patroon E: ingesprongen ALLCAPS, omsloten door lege regels ────────
        m_indent = _ALLCAPS_INDENTED.match(line)
        if m_indent:
            prev_blank = (i == 0) or _is_blank(lines[i - 1])
            next_blank = (i + 1 >= n) or _is_blank(lines[i + 1])
            if prev_blank and next_blank:
                title = m_indent.group(2).strip()
                # Strip trailing paginanummer (kan voorkomen bij TOC-resten)
                title = _strip_trailing_page(title)
                if not _TOC_LEADER.search(title):
                    out.append(f"## {title}")
                    i += 1
                    continue

        out.append(line)
        i += 1

    return "\n".join(out), frontmatter
