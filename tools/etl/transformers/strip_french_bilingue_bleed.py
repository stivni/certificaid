r"""Transformer: strip Frans tekstfragment na NL in bilingue PDF-leak.

Sommige bilingue PDFs (Belgische Codex Fiscale Procedure, VCF,
Registratierechten-federaal) leveren een 2-koloms layout op die door
pdftotext geconcateneerd wordt op één regel:

  In titel 2, hoofdstuk 2, wordt verstaan onder :  Dans le titre 2, ...
  Deze wet is van toepassing op:  La présente loi s'applique à:

De FR-helft (rechts) is een vertaling van de NL-helft (links). Voor een
NL-RAG-index is alleen de NL-helft relevant; de FR-helft verstoort
embeddings.

Detectie-heuristiek:
- Regel bevat eerst NL-tekst, dan 2+ spaties als kolom-separator,
  dan een FR-marker (Dans le, Dans la, Le présent, La présente, ...).
- Strip van de FR-marker tot einde regel.

Conservatief: alleen wanneer een duidelijke FR-marker aanwezig is.
Vermijdt false-positives op generieke "  word" patronen.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Zekere FR-markers die in NL nooit zo voorkomen (op kolom-separator-positie).
# Match `  ` (2+ spaces) of einde van NL-zin met `:`, dan FR-marker.
_FR_MARKERS = (
    r"Dans\s+(?:le|la|les)\b",
    r"Le\s+présent\b",
    r"La\s+présente\b",
    r"Les\s+présents\b",
    r"Le\s+présent\s+article\b",
    r"Article\s+\d+",  # FR "Article" (NL gebruikt "Artikel")
    r"L['']article\b",
    r"Pour\s+l['']application\b",
    r"Pour\s+l['']exécution\b",
    r"Au\s+sens\s+du\b",
    r"L['']exécution\b",
    r"Sont\s+considérées\b",
    r"Toute\s+personne\b",
    r"En\s+vertu\s+de\b",
    r"Par\s+dérogation\b",
    r"Conformément\s+à\b",
    r"Aux?\s+fins\b",
    r"Le\s+Roi\b",  # "Le Roi" = "De Koning"
    r"Lorsque\s+\S+",  # FR conditional
    r"Sont\s+considérés\b",
    r"Il\s+(?:est|n'est)\b",
    r"Cette\s+(?:loi|disposition)\b",
    r"Ces\s+\S+",
    r"Par\s+\S+",  # Par décret, Par arrêté, ...
    r"Les\s+\S+\s+(?:de|du|des|à|au)\b",  # Les modalités de ...
)

# FR-tabel-continuation rij: regel begint met '/  ' gevolgd door FR-content.
_FR_TABLE_ROW_RE = re.compile(
    r"^\s*/\s+[A-Za-zéàèîôûïüç']",
)

# Regel met 2+ spaties gevolgd door FR-marker.
_BILINGUE_PATTERN = re.compile(
    r"(.+?)\s{2,}(?P<fr>(?:" + "|".join(_FR_MARKERS) + r")\b.*)$",
)


def strip_french_bilingue_bleed(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip FR-tekstfragmenten na NL+kolom-separator in bilingue PDF-leak.

    Per regel: als die eindigt met '  + FR-marker', knip vanaf de FR-marker.
    """
    out_lines: list[str] = []
    for line in body.split("\n"):
        # FR-tabel-rij (regel begint met '/  FR-tekst') — strip volledig.
        if _FR_TABLE_ROW_RE.match(line):
            continue
        m = _BILINGUE_PATTERN.match(line)
        if m:
            nl_part = m.group(1).rstrip()
            # Behoud NL-deel als die niet leeg is.
            if nl_part:
                out_lines.append(nl_part)
                continue
        out_lines.append(line)
    return "\n".join(out_lines), frontmatter
