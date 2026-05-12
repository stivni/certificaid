"""Transformer: normaliseer `•` bullet-glyphs naar markdown `-` lijst-syntax.

Sommige CBN-adviezen renderen opsommingen met het bullet-glyph `•` (U+2022)
in plaats van een markdown `-` lijst-marker:

    • Eerste punt
    • Tweede punt

Markdown-renderers herkennen `•` niet als lijst-syntax → opsommingen worden
als gewone alinea's gerenderd, en RAG-chunking verliest de lijst-context.

Fix: regels die met `•` beginnen (met optionele leading whitespace) krijgen
`-` als marker. Behoud de leading-whitespace (geneste lijsten).

Niet aanraken:
- `•` middenin een zin (`zie • dit • en dat`)
- `•` zonder trailing whitespace (`•woord` → mogelijk geen lijst)

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Lijst-regel met `•` als marker — vervangen door `-`.
# Vereist whitespace na de `•` (anders is het inline-symbool, geen lijst).
_BULLET_RE = re.compile(r"^([ \t]*)•(\s+)", re.M)


def normalize_bullet_glyphs(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Vervang `•` lijst-markers door markdown `-`."""
    return _BULLET_RE.sub(r"\1-\2", body), frontmatter
