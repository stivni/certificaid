r"""Transformer: strip inline footnote-blocks die in body gerendered zijn.

Sommige PDFs renderen voetnoten (typisch artikelen uit andere wetten waarnaar
verwezen wordt) als inline-blok midden in de body. Voorbeeld WBTW-KB39:

  (1) Art. 138: Deze wet is niet van toepassing:
  1° op het administratieve dwangbevel ...
  5° op fiscale en niet-fiscale schuldvorderingen ...
  ## Art. 139: De Koning kan ...

Het footnote-blok hoort er niet bij — het is de inhoud van Art. 138-139
van een ANDERE wet waarnaar de voetnoot (1) verwijst.

Conservatieve strip: alleen de regels die ZICHTBAAR onderdeel van het
footnote-blok zijn:
1. `^\(\d+\)\s+Art\.\s+\d+\w*:`  — footnote-start
2. `^\d+°\b` — direct opvolgend nummered item (eindigt op `;`)
3. `^#{1,6}\s+Art\.\s+\d+\w*:` — fake-promoted heading (met colon)

Stopt zodra een blanco regel verschijnt; daarna gewone body voortzetten.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_FOOTNOTE_START_RE = re.compile(
    r"^\(\d+\)\s+Art\.\s+\d+\w*\s*:",
)
_NUMBERED_ITEM_RE = re.compile(r"^\d+°\b")
_FAKE_ART_HEADING_WITH_COLON_RE = re.compile(
    r"^#{1,6}\s+Art\.\s+\d+\w*:\s+\S",
)


def strip_inline_footnote_block(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip inline footnote-block: voetnoot-start + nummered items + fake-heading."""
    lines = body.split("\n")
    out: list[str] = []
    in_footnote = False
    for line in lines:
        if _FOOTNOTE_START_RE.match(line):
            in_footnote = True
            continue  # strip
        if in_footnote:
            # Continue strippen zolang de regel deel uitmaakt van de footnote.
            if not line.strip():
                # Blanco regel → einde footnote-blok.
                in_footnote = False
                out.append(line)
                continue
            if _NUMBERED_ITEM_RE.match(line) or _FAKE_ART_HEADING_WITH_COLON_RE.match(line):
                continue  # strip
            # Andere niet-blanco regel → einde footnote (we hadden eerder
            # gestopt bij een blanco, dus dit is een continuation van item).
            # Wees conservatief: strip ALLEEN als dit eruit ziet als een
            # vervolg van een numbered-item (geen heading, niet-hoofdletter).
            if line.lstrip()[:1].islower() or line.lstrip()[:1] in "(":
                continue  # strip
            # Anders: stop hier, keep
            in_footnote = False
            out.append(line)
            continue
        # Strip ook geïsoleerde fake-promoted Art-heading (## Art. N: title)
        if _FAKE_ART_HEADING_WITH_COLON_RE.match(line):
            continue
        out.append(line)
    new_body = "\n".join(out)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
