r"""Transformer: strip lege of contentless heading-regels onderaan de body.

Soms eindigt een document met een 'lege' heading-regel die door de
extractor of heading-injectie is achtergelaten zonder body — bv.
`## Art.` zonder nummer of inhoud aan het einde van het bestand.

Twee gevallen die gestript worden:
1. Heading-line ALS LAATSTE non-blank regel zonder inhoud erna:
   `^#{1,6}\s+.{0,15}$` met het body-deel "leeg-genoeg" (alleen Art./§/punten).
2. Een heading direct gevolgd door een andere heading (geen body ertussen):
   conservatief NIET stripping — kan legitieme nested structure zijn.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Match `## Art.`, `## Art.   `, `### Art.`, `## §`, etc. — heading met alleen
# een label en geen substantiele content erna. We zijn streng: max 8 tekens
# in het body-deel van de heading (na het #-prefix) en het is een van enkele
# bekende "lege labels".
_EMPTY_HEADING_TAIL_RE = re.compile(
    r"\n#{1,6}\s+(?:Art\.|Artikel|§|HOOFDSTUK|TITEL|Afdeling|Bijlage)\.?\s*\n*\s*\Z",
    re.I,
)


def strip_empty_trailing_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip één of meerdere lege heading-regels onderaan de body.

    Conservatief: alleen heading-regels met een 'label' (Art./§/HOOFDSTUK)
    en niets erna, helemaal aan het einde van het bestand. Loops om
    meerdere achterelkaar te strippen.
    """
    prev = None
    new_body = body
    # Loop totdat geen veranderingen meer — strips meerdere achter elkaar.
    while prev != new_body:
        prev = new_body
        new_body = _EMPTY_HEADING_TAIL_RE.sub("\n", new_body)
    if new_body != body:
        new_body = new_body.rstrip() + "\n"
    return new_body, frontmatter
