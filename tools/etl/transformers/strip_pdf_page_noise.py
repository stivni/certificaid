"""Transformer: strip PDF-paginanummer + dotted-leader artefacten uit body.

Praktijkgidsen-PDFs (fiscaal-memento, belastinggids, toelichting-PB) renderen
typisch paginanummers en TOC-leaders die als plain-text in de body terechtkomen:

Patronen die worden gestript:
1. Dotted-leader TOC-regels: `VOORWOORD..........................9`
   (regel eindigt met ≥4 dots gevolgd door paginanummer)
2. Standalone paginanummers: `\n  3\n`, `\n8\n`
   (uitsluitend 1-3 cijfers op een eigen regel — 4-cijfer is meestal een jaar
   en wordt NIET gestript)
3. Dash-wrapped pagina-aanduidingen: `\n -3- \n`, `\n - 12 - \n`
4. MM/YYYY pagina-stamps: `\n  12/2024  \n`

Conservatief:
- Geen 4-cijferige getallen (`2025` blijft, is meestal jaar).
- Vereist regel-isolatie (omringd door whitespace of newlines), niet inline.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Patroon 1: dotted-leader TOC-rest
_DOTTED_LEADER_RE = re.compile(
    r"^.{0,80}\.{4,}\s*\d{1,4}\s*$",
    re.M,
)

# Patroon 2: standalone paginanummer (1-3 cijfers, optioneel met dashes/punten/bullets)
_STANDALONE_PG_RE = re.compile(
    r"^\s*[-•·]?\s*\d{1,3}\s*[-•·]?\s*$",
    re.M,
)

# Patroon 3: MM/YYYY pagina-stamp (typisch in voet-marges)
_MMYYYY_STAMP_RE = re.compile(
    r"^\s*\d{1,2}/\d{4}\s*$",
    re.M,
)


def strip_pdf_page_noise(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip paginanummer- + dotted-leader-artefacten uit body-regels."""
    new_body = _DOTTED_LEADER_RE.sub("", body)
    new_body = _STANDALONE_PG_RE.sub("", new_body)
    new_body = _MMYYYY_STAMP_RE.sub("", new_body)
    # Collapse runs van lege regels die door de strip ontstaan.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
