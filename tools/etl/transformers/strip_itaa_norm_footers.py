"""Transformer: strip ITAA-norm-specifieke page-footer-artefacten.

ITAA-norm PDFs hebben twee herkenbare page-footer-patronen die door pdftotext
midden in de body terechtkomen:

1. **Copyright-footer**: `© ITAA – Norm betreffende ...` (herhaalt per pagina)
2. **Goedkeurings-footer**: `Goedgekeurd HREB (datum)- ter goedkeuring van
   de minister voorgelegd N/47` (per pagina). Wordt soms verkeerd als
   `## heading` gepromoveerd.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Copyright-footer met © ITAA-prefix
_ITAA_COPYRIGHT_RE = re.compile(
    r"^\s*©\s*ITAA[^\n]*$",
    re.M,
)

# Goedkeurings-footer; optionele ## heading-prefix (was foutief gepromoveerd)
_HREB_FOOTER_RE = re.compile(
    r"^\s*(?:#+\s+)?Goedgekeurd\s+HREB[^\n]*\d+/\d+\s*$",
    re.M | re.I,
)

# Generieke heading-met-pagina-marker: een `## TITLE ... N/M`-regel waar N/M
# een paginanummer + total is. Page-footer wordt gepromoot tot heading.
# Voorbeeld: `## VERZOEK TOT GOEDKEURING OKTOBER 2025 64/64` (122× in
# ITAA-norm-omzetting-vennootschap).
_HEADING_WITH_PAGE_MARKER_RE = re.compile(
    r"^\s*#+\s+[A-Z][^\n]*?\s\d{1,3}/\d{1,3}\s*$",
    re.M,
)


def strip_itaa_norm_footers(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip ITAA-norm page-footer-regels uit body."""
    new_body = _ITAA_COPYRIGHT_RE.sub("", body)
    new_body = _HREB_FOOTER_RE.sub("", new_body)
    new_body = _HEADING_WITH_PAGE_MARKER_RE.sub("", new_body)
    # Collapse opeenvolgende lege regels
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
