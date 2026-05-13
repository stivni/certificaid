r"""Transformer: strip fake Art-headings uit concordantietabel.

In BTW-richtlijn-2006-112 wordt de concordantietabel (Bijlage XII)
geconverteerd met elke tabelrij als markdown-heading, wat de heading-
boom vervuilt:

  ###### Art. 28. septdecies, eerste alinea,
  ###### Art. 33. bis, lid 1, inleidende zin
  ###### Art. 2. van Richtlijn 94/5/EG

Echte artikel-headings hebben simpele vorm `Art. N` of `Art. Nbis` —
geen punt na het nummer, geen komma's, geen 'lid X' suffix.

Detectie: heading-regel met patroon:
  `^#{1,6}\s+Art\.\s+\d+\.\s+(?:bis|onder|lid|alinea|septdecies|...|van Richtlijn|,)`

→ Demote naar plain text (verwijder de heading-prefix).

Conservatief: alleen wanneer de heading-tekst niet matcht het standaard
`Art. \d+\w?\s*$` patroon.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Concord-keyword-list: woorden die in een echte heading niet voorkomen
# (typisch concord-tabel suffixen).
_CONCORD_KEYWORDS = (
    r"(?:septdecies|undecies|duodecies|terdecies|quaterdecies|"
    r"quindecies|sexdecies|septdecies|octodecies|novodecies|vicies|"
    r"septies|octies|nonies|decies|"
    r"bis|ter|quater|quinquies|sexies|"
    r"lid\s+\d+|alinea|inleidende\s+zin|"
    r"onder\s+\w\)|streepje|"
    r"van\s+Richtlijn|van\s+richtlijn|"
    r"eerste|tweede|derde|vierde|vijfde|zesde|zevende|achtste|negende|tiende)"
)

# Heading met `Art. N. <concord-keyword>` of `Art. N, <concord-keyword>`.
_CONCORD_HEADING_RE = re.compile(
    r"^(#{1,6})\s+(Art\.\s+\d+\w*[\.,]\s+" + _CONCORD_KEYWORDS + r".*)$",
    re.M | re.I,
)


_CONCORDANTIETABEL_SECTION_RE = re.compile(
    r"^(?:#{1,6}\s+)?(?:BIJLAGE\s+(?:XI{1,2}|[IVX]+)|Bijlage\s+(?:XI{1,2}|[IVX]+))\s*\n+"
    r"(?:#{1,6}\s+)?CONCORDANTIETABEL\b",
    re.M | re.I,
)
_ANY_ART_HEADING_RE = re.compile(
    r"^(#{1,6})\s+(Art\.\s+\d+\w*.*)$",
    re.M,
)


def strip_concord_table_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Demote concord-table 'headings' naar plain text.

    Twee strategieën:
    1. Pattern-match: heading met expliciete concord-keywords (bis,
       lid N, alinea, van Richtlijn, eerste, ...).
    2. Region-match: alles binnen 'Bijlage XII / CONCORDANTIETABEL'
       sectie tot einde body — demote ALLE Art-headings naar plain text.
    """
    new_body = _CONCORD_HEADING_RE.sub(r"\2", body)
    # Region-based: vind start van CONCORDANTIETABEL sectie
    m = _CONCORDANTIETABEL_SECTION_RE.search(new_body)
    if m:
        head = new_body[:m.start()]
        tail = new_body[m.start():]
        # In de tail: demote alle ## Art. N headings naar plain text
        tail = _ANY_ART_HEADING_RE.sub(r"\2", tail)
        new_body = head + tail
    return new_body, frontmatter
