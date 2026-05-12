"""Transformer: merge_pdf_paragraph_breaks (ADR-005 §4).

Detecteert en repareert twee PDF-paginabreuk-patronen die leiden tot gefragmenteerde
alinea's in de geëxtraheerde markdown:

PATROON 1 — IESBA lettered items op eigen regel:
    (a)
    ↵
    Content van het item.
  →  (a) Content van het item.

  Trigger: een regel die uitsluitend `(a)` t/m `(z)`, of `(i)` t/m `(x)` (Romein),
  of een getal `(1)` t/m `(99)` bevat, gevolgd door een lege regel en niet-lege tekst.
  Merge: het haakjes-label wordt met een spatie aan de volgende niet-lege regel
  geplakt.

PATROON 2 — woord-per-woord splits (kort-regelbreuk):
  Wanneer pdftotext een enkele tekstkolom over meerdere visuele regels uitspreidt
  zonder trailing spatie, verschijnt elke visuele regel als een aparte alinea.
  Kenmerken:
    - De huidige regel is korter dan `MAX_SHORT_LINE` tekens (standaard 20).
    - De huidige regel eindigt NIET op een sentence-end marker (`.`, `?`, `!`, `:`)
      óf op een markdown-structuurmarker (heading `#`, lijst `-`/`*`/`1.`/`(a)`).
    - De volgende niet-lege regel bestaat ook.
  Dan worden de twee regels met een spatie samengevoegd.

Conservatief beleid — NIET mergen:
  - Headings (begint met `#`).
  - Lijstitems (begint met `-`, `*`, `>`, `|`).
  - YAML-frontmatter-blokken (tussen `---` markers).
  - Regels die eindigen op `.`, `?`, `!`, `:` (echte alinea-einde).
  - Pagina-headers/footers die door strip_pdf_page_noise zijn overgebleven
    (maar die zijn eerder in de chain al gestript).
  - Lege regels.
  - Paragraaf-nummers in bold (bv. `**100.3**`) worden niet gemerged.

Idempotent: een tweede doorloop verandert niets.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Lettered-item regex: `(a)`, `(b)`, ..., `(z)`, `(i)`, ..., ook Roomse `(iv)` etc.,
# ook genummerd `(1)` t/m `(99)`.
_LETTERED_ITEM_RE = re.compile(
    r"^\((?:[a-z]|[ivxlc]{1,6}|\d{1,2})\)$",
    re.IGNORECASE,
)

# Sentence-end markers die een "echte" alinea-afbreuk signaleren.
_SENTENCE_END_RE = re.compile(r"[.?!:;]\s*$")

# Structuur-regels die nooit gemerged worden (beginkarakter-check).
_STRUCTURE_START_RE = re.compile(r"^(?:#|-|\*|>|\||\d+\.|```|\*\*)")

# Maximale regellengte voor het "korte-regel"-heuristiek (exclusief newline).
MAX_SHORT_LINE = 20


def _is_frontmatter_line(line: str, in_fm: bool) -> bool:
    """Hulpfunctie: geef True als deze regel deel uitmaakt van een frontmatter-blok."""
    return in_fm


def merge_pdf_paragraph_breaks(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Merge PDF-regelbreuk-artefacten in `body` (zie module-docstring)."""
    lines = body.split("\n")
    result: list[str] = []
    i = 0
    in_frontmatter = False
    fm_delimiter_count = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── YAML-frontmatter detectie ──────────────────────────────────────
        if stripped == "---":
            fm_delimiter_count += 1
            in_frontmatter = (fm_delimiter_count % 2 == 1)
            result.append(line)
            i += 1
            continue

        if in_frontmatter:
            result.append(line)
            i += 1
            continue

        # ── PATROON 1: lettered item op eigen regel ────────────────────────
        if _LETTERED_ITEM_RE.match(stripped):
            # Zoek de volgende niet-lege regel.
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                next_line = lines[j].strip()
                # Merge: `(a) Content`
                result.append(f"{stripped} {next_line}")
                i = j + 1
                continue
            # Geen volgende niet-lege regel: behoud onveranderd.
            result.append(line)
            i += 1
            continue

        # ── PATROON 2: korte regel (woord-per-woord split) ─────────────────
        # Greedy: verzamel alle opeenvolgende korte-regel-fragmenten in één alinea.
        if (
            stripped  # niet leeg
            and len(stripped) < MAX_SHORT_LINE
            and not _STRUCTURE_START_RE.match(stripped)
            and not _SENTENCE_END_RE.search(stripped)
        ):
            # Zoek de volgende niet-lege regel.
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].strip():
                next_stripped = lines[j].strip()
                # Niet mergen als de volgende regel een structuur-marker is.
                if not _STRUCTURE_START_RE.match(next_stripped):
                    # Greedy merge: bouw de alinea op zolang we korte
                    # fragmenten tegenkomen (idempotentie vereist dit).
                    fragments = [stripped]
                    k = j
                    while True:
                        cur = lines[k].strip()
                        fragments.append(cur)
                        # Stop als huidige fragment een sentence-end heeft
                        # of als er geen volgende niet-lege regel is.
                        if _SENTENCE_END_RE.search(cur):
                            break
                        # Zoek volgende niet-lege regel
                        m = k + 1
                        while m < len(lines) and lines[m].strip() == "":
                            m += 1
                        if m >= len(lines) or not lines[m].strip():
                            break
                        next_candidate = lines[m].strip()
                        # Stop als volgende een structuur-marker is of
                        # als de huidige fragment al lang genoeg is.
                        if (
                            _STRUCTURE_START_RE.match(next_candidate)
                            or len(cur) >= MAX_SHORT_LINE
                        ):
                            break
                        k = m
                    result.append(" ".join(fragments))
                    i = k + 1
                    continue

        # ── Standaard: behoud onveranderd ──────────────────────────────────
        result.append(line)
        i += 1

    return "\n".join(result), frontmatter
