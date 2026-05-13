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


def strip_concord_table_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Demote concord-table 'headings' naar plain text."""
    # Verwijder heading-prefix; behoud heading-tekst als plain text
    new_body = _CONCORD_HEADING_RE.sub(r"\2", body)
    return new_body, frontmatter
