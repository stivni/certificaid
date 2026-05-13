"""Transformer: strip de Fisconet 'Lijst van de bijwerkingen'-appendix.

Veel WBTW-KBs en -MBs uit de Fisconet-compilatie eindigen met een
metadata-blok dat per bijwerking (datum + welke pagina's vervangen werden)
een rij bevat. Voorbeeld:

  ---

  Lijst van de bijwerkingen

  Bijwerking Te vervangen pagina's

  Bijw. 01 / 01.01.2012 - Volledige uitgave
  Bijw. 02 / 20.02.2015 - pg. 1 - Bijw. 02 - pg. 1
  Bijw. 03 / 12.07.2019 - Volledige uitgave

Soms voorgegaan door `KB nr. N - Lijst van de bijwerkingen` (compilatie-vorm).

Dit blok is geen wetinhoud — het is publicatie-metadata van Fisconet over
welke pagina's in de papieren compilatie vernieuwd zijn. Voor RAG is het
ruis (datums + paginanummers raken vermengd met inhoud).

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Match 'Lijst van de bijwerkingen' header (optionally prefixed with KB/MB nr. N).
# Case-insensitive op de label-tekst; whitespace tollerant.
_BIJWERKINGEN_HEADER_RE = re.compile(
    r"^\s*(?:(?:KB|MB|M\.B\.|K\.B\.)\s*nr\.\s*\d+(?:\s*\(\d{4}\))?\s*-\s*)?"
    r"Lijst\s+van\s+de\s+bijwerkingen\s*$",
    re.I | re.M,
)

# 'Recent opgeheven of vervangen (koninklijke|ministeriële) besluiten.'
# Fisconet-appendix met lijst van recente repeals/replacements als bullet-list.
_RECENT_OPGEHEVEN_HEADER_RE = re.compile(
    r"^\s*Recent\s+opgeheven\s+of\s+vervangen\s+"
    r"(?:koninklijke|ministeriële)\s+besluiten\s*\.?\s*$",
    re.I | re.M,
)


def strip_kb_bijwerkingen(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip Fisconet-appendices tot einde body.

    Patronen:
    1. 'Lijst van de bijwerkingen' — bijwerk-metadata (datums + pagina's).
    2. 'Recent opgeheven of vervangen koninklijke/ministeriële besluiten' —
       lijst van recente repeals/replacements als bullet-list met kolom-bleed.

    Snijdt body af bij de eerste match (incl. zelf). Verwijdert ook
    voorafgaande `---`-separator en trailing blanks.
    """
    candidates: list[int] = []
    for pat in (_BIJWERKINGEN_HEADER_RE, _RECENT_OPGEHEVEN_HEADER_RE):
        m = pat.search(body)
        if m:
            candidates.append(m.start())
    if not candidates:
        return body, frontmatter
    cut = min(candidates)
    new_body = body[: cut]
    new_body = re.sub(r"(?:\n\s*-{2,}\s*)+\s*$", "", new_body)
    new_body = new_body.rstrip() + "\n"
    return new_body, frontmatter
