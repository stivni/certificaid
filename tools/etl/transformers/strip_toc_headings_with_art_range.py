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


def strip_toc_headings_with_art_range(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip heading-regels eindigend met 'Art. N - M' (TOC-entries)."""
    new_body = _TOC_HEADING_RE.sub("", body)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
