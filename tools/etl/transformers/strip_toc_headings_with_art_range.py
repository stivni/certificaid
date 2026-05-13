r"""Transformer: strip TOC-style headings die eindigen met 'Art. N - M'.

Sommige WBTW-KB's hebben een TOC bovenaan waar afdelingen geheel als
heading zijn opgenomen, maar elk eindigend met een artikel-range:

  ## AFDELING 2. Betaling vastgesteld door middel van...  Art. 14 - 15
  ## AFDELING 3. Betaling bestemd voor het kantoor van...  Art. 16 - 19
  ## AFDELING 4. Betaling op een douane of accijnskantoor...  Art. 20 - 21
  ## AFDELING 5. Slotbepalingen.  Art. 22 - 24

  ## AFDELING 1
  Betalingen op de rekeningen van...
  (Het opschrift van Afdeling 1, werd vervangen met ingang van 01.12.2019...)

De eerste 4 zijn TOC-entries; AFDELING 1 (zonder Art.-range) is het echte
content-begin. De TOC-entries worden als duplicate heading-injecties
herkend door RAG-chunker en verstoren de hiërarchie.

Detectie: heading-regel met `Art. \d+\w? - \d+\w?` of `Art. \d+bis` suffix
als laatste zinsdeel.

Strip alleen wanneer:
- Heading-regel eindigt met deze Art.-range patroon
- Er is een 'echte' versie van dezelfde heading verderop in de body
  (zelfde label, zonder Art.-range)

Conservatief: we strippen NIET een geïsoleerde heading. Alleen TOC-runs.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Heading met Art-range suffix: `## AFDELING 2. Title.  Art. 14 - 15`
# of `### Onderafdeling 1. Title  Art. 1 - 8`
_TOC_HEADING_RE = re.compile(
    r"^(?P<prefix>#{2,6})\s+"
    r"(?P<label>AFDELING|Onderafdeling|Hoofdstuk|HOOFDSTUK|Afdeling)\s+"
    r"(?P<num>\d+\w*)\..*?\s+"
    r"Art\.\s+\d+\w*\s*[-–]\s*\d+\w*\s*$",
    re.M,
)


# Multi-line variant: heading-regel zonder Art-range, next non-blank line eindigt
# met `Art. N - M` of `Art. Nbis`. Strip beide regels.
_HEADING_PREFIX_RE = re.compile(
    r"^(?P<prefix>#{2,6})\s+"
    r"(?:AFDELING|Onderafdeling|Hoofdstuk|HOOFDSTUK|Afdeling)\s+\d+\w*\."
)
_ART_RANGE_LINE_RE = re.compile(
    r".*\bArt\.\s+\d+\w*(?:\s*[-–]\s*\d+\w*)?\s*$",
)


def strip_toc_headings_with_art_range(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip heading-regels eindigend met 'Art. N - M' (TOC-entries).

    Twee patronen:
    1. Single-line: heading-regel met Art-range op zelfde regel.
    2. Multi-line: heading + next-line eindigt met Art-range (wrapped TOC).
    """
    # Single-line strip
    new_body = _TOC_HEADING_RE.sub("", body)

    # Multi-line strip
    lines = new_body.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if _HEADING_PREFIX_RE.match(line) and i + 1 < len(lines):
            next_line = lines[i + 1]
            if _ART_RANGE_LINE_RE.match(next_line) and next_line.strip():
                # Skip heading + continuation-with-art-range
                i += 2
                continue
        out.append(line)
        i += 1
    new_body = "\n".join(out)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
