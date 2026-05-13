r"""Transformer: merge pdftotext-linewraps midden in artikel-verwijzingen.

`pdftotext -layout` breekt soms een artikelverwijzing op een ongelukkige plek.
Voorbeelden uit WBTW-KB48 / KB51 / KB53 / KB57 / KB24:

    ... bedoeld in artikel 53,
    § 1, eerste lid, 2°, van het Wetboek, moet ...

    ... overeenkomstig artikel
    6.

    ... van het Wetboek of in artikel 5, § 2,
    7° van dit besluit.

Drie surgical merges:
1. `artikel \d+,` of `Art. \d+,` + newline + `§ \d+` → ` § \d+`
2. `artikel` of `Art.` + newline + `\d+(\.|,)` → ` \d+(\.|,)`
3. `§ \d+,` + newline + `\d+°` → ` \d+°`

Conservatief: alleen mergen wanneer beide kanten een **artikel-/§-referentie**
zijn — geen generieke paragraaf-merge.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# `artikel 53,\n§ 1` → `artikel 53, § 1`
_ARTIKEL_NUM_BREAK_SECTION_RE = re.compile(
    r"((?:artikel|Art\.)\s+\d+(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?,)\n(\s*§\s*\d+)",
    re.I,
)

# `... artikel\n6.` → `... artikel 6.`
_ARTIKEL_BREAK_NUM_RE = re.compile(
    r"((?:artikel|Art\.))\n(\s*\d+(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?[\.,])",
    re.I,
)

# `§ 1,\n7°` → `§ 1, 7°`
_SECTION_BREAK_ORDINAL_RE = re.compile(
    r"(§\s*\d+,)\n(\s*\d+°)",
)


def merge_article_reference_wraps(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Merge pdftotext-linewraps in artikel-/§-verwijzingen."""
    new_body = _ARTIKEL_NUM_BREAK_SECTION_RE.sub(r"\1 \2", body)
    new_body = _ARTIKEL_BREAK_NUM_RE.sub(r"\1 \2", new_body)
    new_body = _SECTION_BREAK_ORDINAL_RE.sub(r"\1 \2", new_body)
    return new_body, frontmatter
