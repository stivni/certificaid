"""Transformer: strip 'running page-header' regels (paginanr + titel).

Sommige PDF-extractie laat running headers/footers staan met patronen zoals:

  `9 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen`
  `- KB nr. 13 / 1 -`
  `- KB nr. 13 / 2 -`

Dat zijn pagina-headers die per PDF-pagina herhaald worden. Markdown-renderer
ziet het als body-tekst en RAG-chunking pikt het meermaals op.

Twee patronen gestript:
1. **N | Title-string** — paginanr direct gevolgd door `|` en herhalende titel
2. **- KB nr. N / M -** of **- M.B. nr. N / M -** — gecentreerd KB/MB-marker
   (typisch in Fisconet compilatie-PDFs)

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# `9 | Minimum Algemeen Rekeningstelsel ...` patroon (page-num + pipe + title)
_PG_PIPE_TITLE_RE = re.compile(
    r"^\s*\d{1,3}\s*\|\s*[A-Z].{8,200}$",
    re.M,
)

# `- KB nr. 13 / 1 -` / `- M.B. nr. 7 / 12 -` (centred page-marker)
_KB_MB_PAGE_MARKER_RE = re.compile(
    r"^\s*-\s*(?:KB|MB|M\.B\.)\s*nr\.\s*\d+\s*/\s*\d+\s*-\s*$",
    re.M | re.I,
)

# `KB57 (2017) pg. 1 Plaats van de dienst` / `MB7 pg. Bijw/2 Iets`
# Bron-id (KB/MB + nummer, optioneel met jaartal) gevolgd door `pg. N` (of
# `pg. Bijw/N`) en een herhalende titel. Komt voor onderaan WBTW-KB-pagina's.
_KB_MB_PG_TITLE_RE = re.compile(
    r"^\s*(?:KB|MB|M\.B\.|K\.B\.)\s*\d+(?:\s*\(\d{4}\))?\s+pg\.\s+\S+\s+.+$",
    re.M | re.I,
)

# `Interne procedure –11/2019/ p. N` — ITAA-handleiding interne procedures AWW
# (sessie 2026-05-19). Running page-header op elke pagina met paginanr (1-3 cijfers).
# Pattern accepteert zowel U+2013 (en-dash) als gewone hyphen tussen 'procedure' en de datum.
_ITAA_INTERNE_PROCEDURE_RE = re.compile(
    r"^\s*Interne procedure\s*[–\-]\s*\d{1,2}/\d{4}/\s*p\.\s*\d{1,3}\s*$",
    re.M,
)


def strip_running_page_headers(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip running-page-header regels (paginanr + herhaalde titel)."""
    new_body = _PG_PIPE_TITLE_RE.sub("", body)
    new_body = _KB_MB_PAGE_MARKER_RE.sub("", new_body)
    new_body = _KB_MB_PG_TITLE_RE.sub("", new_body)
    new_body = _ITAA_INTERNE_PROCEDURE_RE.sub("", new_body)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
