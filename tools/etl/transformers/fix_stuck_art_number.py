"""Transformer: voeg ontbrekende spatie in tussen 'Art. N.' en eerste body-woord.

Sommige Fisconet/Justel-PDFs renderen artikel-headings zonder spatie tussen
het artikelnummer-punt en het eerste woord:

    `Art. 3.Deze wet is van toepassing op alle betalingen ...`
                ^ ontbrekende spatie

Gevolg: heading-injectie ziet de hele regel als heading-tekst en promoveert
hem onveranderd tot `## Art. 3.Deze wet is van toepassing ...` — dat is een
RAG-onvriendelijke chunk-titel.

Deze transformer normaliseert de spatiëring vóór de heading-injectie draait,
zodat `inject_headings_wettekst` een schone heading kan injecteren met de
body als aparte regel.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag
(niet extractor).
"""
from __future__ import annotations

import re

# `Art.` of `Artikel`, gevolgd door whitespace + artikel-nummer + punt +
# direct een non-whitespace karakter (hoofdletter, bracket, dollar, etc.).
# Het nummer ondersteunt:
#   - simpele cijfers (5, 23)
#   - roman-prefix WER-stijl (XV.125, XV.125/4/1)
#   - WVV NUM:NUM (1:5, 18:8)
#   - bis/ter/quater/... suffix
#
# We voegen ÉÉN spatie in tussen de punt en het volgende karakter.
_STUCK_ART_NUM_RE = re.compile(
    r"(\b(?:Art\.|Artikel)\s+"    # `Art.` (afkorting met punt) of `Artikel` (lang, geen punt)
    r"(?:[IVXLCDM]+\.)?"
    r"\d+(?:[\./:]\d+)*"
    r"(?:bis|ter|quater|quinquies|sexies|septies)?"
    r"\.)"
    r"(?=\S)"      # non-whitespace direct na de punt
    r"(?!\d)"      # ... maar GEEN cijfer (zou een vervolgnummer zijn,
                   #     zoals `Art. 3.1` — die punt is geen heading-eind)
    r"(?![/])"     # ... en GEEN forward slash (`Art. 3.5/2` voor sub-num)
    r"",
    re.IGNORECASE,
)


def fix_stuck_art_number(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Voeg spatie in tussen 'Art. N.' en het volgende karakter."""
    new_body = _STUCK_ART_NUM_RE.sub(r"\1 ", body)
    return new_body, frontmatter
