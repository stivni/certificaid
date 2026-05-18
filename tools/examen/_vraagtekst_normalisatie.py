"""Normaliseer ruwe PDF-vraagtekst tot leesbare Markdown.

PDF-extractie via pdfplumber levert `\\n` op willekeurige plekken — vooral
kolom-/pagina-wrap-grenzen. Markdown vat single `\\n` op als zachte return
(= spatie), waardoor structuur-markers zoals "A. ", "B. ", "a) " hun
positie verliezen en de vraag-tekst renderd als één lange paragraph.

Deze module reflowt de tekst: structuur-markers krijgen een paragraph-break
ervoor; mid-zin breaks worden vervangen door een spatie.

Detecteerde structuur-markers (per regel-begin):
- `A.`, `B.`, ... — sub-vraag met hoofdletter + punt
- `a)`, `b)`, ... — sub-sub-vraag met kleine letter + haakje sluit
- `a.`, `b.`, ... — sub-sub-vraag met kleine letter + punt
- `1.`, `2.`, ... — genummerde sub-vraag
- `(1)`, `(a)`, ... — sub-vraag met haakjes
"""
from __future__ import annotations

import re

# Match: regel begint met een structuur-marker gevolgd door whitespace
# Voorbeelden: "A.", "B.", "a)", "a.", "1.", "(1)", "(a)"
STRUCTUUR_MARKER = re.compile(
    r"^("
    r"[A-Z]\.|"           # A. B. C.
    r"[a-z][.)]|"         # a. b. c. a) b) c)
    r"\d+[.)]|"           # 1. 2. 1) 2)
    r"\([A-Za-z0-9]+\)"   # (1) (a) (i)
    r")\s+"
)


def normaliseer(text: str) -> str:
    """Reflow PDF-vraagtekst naar Markdown met paragraph-breaks op structuur-markers.

    Args:
        text: ruwe vraagtekst uit PDF (met willekeurige single `\\n`)

    Returns:
        Genormaliseerde tekst met `\\n\\n` tussen paragraphs en zonder mid-zin
        `\\n`. Leeg → lege string.
    """
    if not text:
        return ""

    # Strip per-regel whitespace, drop fully-empty lines
    lines = [r.rstrip() for r in text.split("\n")]

    paragraphs: list[str] = []
    huidige: list[str] = []

    for regel in lines:
        if not regel.strip():
            # Lege regel: sluit huidige paragraph af
            if huidige:
                paragraphs.append(" ".join(huidige))
                huidige = []
            continue

        if STRUCTUUR_MARKER.match(regel) and huidige:
            # Marker start nieuwe paragraph
            paragraphs.append(" ".join(huidige))
            huidige = [regel.strip()]
        else:
            huidige.append(regel.strip())

    if huidige:
        paragraphs.append(" ".join(huidige))

    return "\n\n".join(paragraphs)
