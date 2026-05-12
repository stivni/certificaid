"""Transformer: strip Fisconet wijzigings-overzicht-artefacten.

Sommige Fisconet-PDFs renderen aan het begin van de body een overzicht van
wijzigings-data + artikelnummers als plain-text. Voorbeeld uit AVG-wet-2018:

    (Art.254)   (Art.255)    (Art.256)      (Art.257)     (Art.258)
    01-04-2019             (Art.20)

Dat is een wijzigings-traceer-overzicht — geen wettekst-inhoud. Het zou in
de PDF als aparte tabel/marge moeten worden gerenderd, maar pdftotext gooit
het in de body.

Twee patronen gestript:
1. Regel met ≥3 `(Art.N)`-occurrences (compacte opsomming)
2. Regel met `DD-MM-YYYY (Art.N)` als enige inhoud (datum + art-ref koppel)

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Regel met ≥3 `(Art.N)`-achtige patronen — typisch een overzicht-rij.
# Tolerant voor:
# - missing-close-paren (`(Art.260` zonder `)` — Fisconet-typo)
# - embedded datums en extra spaties tussen refs
# - eind-`.` of andere trailing punctuation
# We detecteren regels waar de meerderheid van de inhoud uit
# `(Art.NUM` of `(Art.NUM)`-tokens bestaat.
_ART_REF_TOKEN_RE = re.compile(r"\(Art\.\s*\d+\)?")
_MIN_REFS_FOR_OVERVIEW = 3

# Regel die louter een datum + artikel-referentie bevat (de "uit de marge"-regel
# die bij de overzicht-tabel hoort). Strikt: niet andere body-content.
_DATE_ART_REF_RE = re.compile(
    r"^\s*\d{1,2}-\d{1,2}-\d{4}\s+\(Art\.\s*\d+\)\s*$",
    re.M,
)


def _is_overview_line(line: str) -> bool:
    """Return True als de regel een overzicht-rij is (≥N art-refs en
    overgrote-deel-content is refs/whitespace/punctuation)."""
    refs = _ART_REF_TOKEN_RE.findall(line)
    if len(refs) < _MIN_REFS_FOR_OVERVIEW:
        return False
    # Verwijder refs en wat 'lawaai' (datums, leestekens, whitespace);
    # wat overblijft mag niet substantieel zijn.
    stripped = _ART_REF_TOKEN_RE.sub("", line)
    stripped = re.sub(r"\d{1,2}-\d{1,2}-\d{2,4}", "", stripped)  # embedded datums
    stripped = re.sub(r"[\s.,;:()-]+", "", stripped)
    # Een echte body-regel zou substantiële tekst bevatten naast de refs.
    return len(stripped) < 5


def strip_amendment_overview(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Verwijder Fisconet wijzigings-overzicht-regels uit body."""
    out_lines = []
    for line in body.split("\n"):
        # Date-only-line met (Art.N): strip
        if _DATE_ART_REF_RE.match(line):
            continue
        # Multi-art-ref overzicht: strip
        if _is_overview_line(line):
            continue
        out_lines.append(line)
    new_body = "\n".join(out_lines)
    # Collapse opeenvolgende lege regels.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
