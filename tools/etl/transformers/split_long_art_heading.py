r"""Transformer: split heading-regels waar artikel-body in heading staat.

Pymupdf-extractor zet soms de eerste regel van een artikel-body samen met
het Art.-label op één heading-regel (door PDF font-based detectie):

  #### Art. 1. Boekhoudplichtige ondernemingen die een onderneming

  zijn in de zin van artikel I.1, eerste lid, ...

De heading bevat de eerste 10+ woorden van de body. Resultaat:
- Heading is onnatuurlijk lang
- RAG-chunker breekt op de heading-regel, body op volgende regel
- "## Art. 1." wordt niet herkenbaar als chunk-titel

Detectie: heading-regel `^#{1,6}\s+Art\.\s+\d+\w*\.?\s+\S.{19,}$` (lange
tekst na Art.-nummer). Split in:
  - Pure heading: `#### Art. N`
  - Body: `<de rest>`

Conservatief: alleen wanneer
- Heading-tekst (post-Art.-N.) is ≥20 chars
- Eindigt niet met punt (anders is het een echte zin als heading)

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Match: `#### Art. 1. <lange tekst zonder eind-punt>`
_LONG_ART_HEADING_RE = re.compile(
    r"^(?P<prefix>#{1,6})\s+(?P<art>Art\.\s+\d+\w*(?:/\d+)?)\.\s+(?P<rest>\S.{19,})$"
)


def split_long_art_heading(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Split heading-regels met artikel-body in heading."""
    lines = body.split("\n")
    out: list[str] = []
    for line in lines:
        m = _LONG_ART_HEADING_RE.match(line)
        if m:
            rest = m.group("rest").rstrip()
            # Alleen splitten als rest niet met punt eindigt (echte body, geen kort titel)
            if not rest.endswith(("."  , "?", "!")):
                out.append(f"{m.group('prefix')} {m.group('art')}")
                out.append("")
                out.append(rest)
                continue
            # Rest eindigt met punt → mogelijk een titel ('Definities.'). Keep.
        out.append(line)
    return "\n".join(out), frontmatter
