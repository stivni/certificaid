"""Transformer: strip ITAA-norm-specifieke page-footer-artefacten.

ITAA-norm PDFs hebben verschillende herkenbare page-footer-patronen die door
pdftotext midden in de body terechtkomen:

1. **Copyright-footer met ©**: `© ITAA – Norm betreffende ...` (herhaalt per pagina).
2. **Variant-footer zonder ©**: `ITAA – Norm permanente vorming ...`
   (zelfde patroon, maar bij sommige PDFs valt het ©-symbool weg in pdftotext-uitvoer).
3. **Goedkeurings-footer**: `Goedgekeurd HREB (datum)- ter goedkeuring van
   de minister voorgelegd N/47` (per pagina). Wordt soms verkeerd als
   `## heading` gepromoveerd.
4. **Heading met paginamarker**: `## TITLE ... N/M`-regel waar `N/M` een
   paginanummer + total is — page-footer werd door upstream-extractie tot
   heading gepromoveerd.
5. **Standalone paginanummers**: een regel met enkel een 1-3-cijferig getal,
   omringd door witregels. We zijn conservatief: alleen bare digits omringd
   door witregels (geen `1.` / `1°` / `1)` — dat zijn opsommingen).
6. **Standalone `Inhoud`-header**: het residu van een TOC-pagina waarin alleen
   het woord `Inhoud` op een eigen regel staat (zonder volgende TOC-items).
   Bona-fide kopjes als `## Inhoud van de opdracht` blijven onaangetast.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Copyright-footer met © ITAA-prefix.
_ITAA_COPYRIGHT_RE = re.compile(
    r"^\s*©\s*ITAA[^\n]*$",
    re.M,
)

# Variant-footer zonder ©-symbool: regel die start (optioneel met whitespace)
# met `ITAA – Norm ...` of `ITAA – Reglement ...`. We zijn streng over het
# vervolg om false-positives in body-tekst te vermijden: een woord dat typisch
# in een norm-titel staat (`Norm`, `Reglement`, `Aanbeveling`, `Nota`, `Bijlage`).
_ITAA_DASH_FOOTER_RE = re.compile(
    r"^\s*ITAA\s+[–-]\s+(?:Norm|Reglement|Aanbeveling|Nota|Bijlage)\b[^\n]*$",
    re.M,
)

# Goedkeurings-footer; optionele ## heading-prefix (was foutief gepromoveerd).
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

# Standalone paginanummer: regel met enkel 1-3 cijfers (optioneel whitespace).
# We vereisen dat de regel volledig uit het getal bestaat — opsomming-vormen
# als `1.`, `1°`, `1)`, `1 De regel ...` worden bewust niet gematcht.
_STANDALONE_PAGENUM_RE = re.compile(
    r"^[ \t]*\d{1,3}[ \t]*$",
    re.M,
)

# Standalone 'Inhoud'-residu uit TOC-pagina. Alleen exact het woord 'Inhoud'
# (case-sensitive, geen kop-prefix, geen volgende tekst) wordt gestript.
# Een echte heading `## Inhoud van de opdracht` valt hier niet onder doordat
# we eisen dat de regel volledig uit het woord bestaat én geen `#`-prefix heeft.
_STANDALONE_INHOUD_RE = re.compile(
    r"^[ \t]*Inhoud[ \t]*$",
    re.M,
)


def strip_itaa_norm_footers(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip ITAA-norm page-footer-regels uit body."""
    new_body = _ITAA_COPYRIGHT_RE.sub("", body)
    new_body = _ITAA_DASH_FOOTER_RE.sub("", new_body)
    new_body = _HREB_FOOTER_RE.sub("", new_body)
    new_body = _HEADING_WITH_PAGE_MARKER_RE.sub("", new_body)
    new_body = _STANDALONE_PAGENUM_RE.sub("", new_body)
    new_body = _STANDALONE_INHOUD_RE.sub("", new_body)
    # Collapse opeenvolgende lege regels
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
