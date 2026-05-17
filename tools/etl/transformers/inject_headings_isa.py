"""Transformer: promote ISA-sectielabels naar `## `-headings.

In de NBA-IBR NL-vertaling van een ISA worden de hoofdsecties als eenvoudige
tekst-regels in de PDF gerenderd (typisch in een groter lettertype, geen
markdown-structuur). Na pymupdf-extractie staan ze als kale regels in de
body:

    Inleiding
    Toepassingsgebied van deze ISA
    Doelstelling
    Definities
    Vereisten
    Toepassingsgerichte en overige verklarende teksten
    Ingangsdatum
    Bijlage

Deze transformer detecteert die labels op een eigen regel en promoot ze
naar `## `-headings zodat RAG-chunking + Quartz-rendering ze als secties
behandelen.

False-positive-bescherming:
- TOC-entries met dotted-leader + paginanummer (`Inleiding ........ 1-2`)
  worden NIET gepromoot — ze bevatten een punt-of-spatie-sequentie.
- Bestaande `## Label`-headings worden niet gedupliceerd.
- Labels die als woord in een lopende zin staan (regel bevat andere
  tekst) worden niet gepromoot — alleen kale-regel-matches tellen.

Conform ADR-005 §4-contract. Idempotent.
"""
from __future__ import annotations

import re

# ─── Sectielabels die als ## gepromoot worden ────────────────────────────────
#
# De labels zijn gekozen uit de standaard ISA-templating:
#   - Hoofdsecties (altijd aanwezig): Inleiding, Doelstelling(en), Definities,
#     Vereisten, Toepassingsgerichte en overige verklarende teksten,
#     Ingangsdatum, Bijlage(n).
#   - Subsecties onder Inleiding (consistent in ISA-templating):
#     Toepassingsgebied van deze ISA, Belangrijke uitgangspunten,
#     Schaalbaarheid.
#
# We matchen case-sensitive (eerste letter hoofdletter, rest lowercase
# behalve eigen namen). Ankers worden exact-match gedaan op een gestripte
# regel — dat voorkomt dat 'Inleiding tot ...' in een zin geraakt wordt.

_HEADING_LABELS = (
    # Hoofdsecties
    "Inleiding",
    "Doelstelling",
    "Doelstellingen",
    "Definities",
    "Vereisten",
    "Toepassingsgerichte en overige verklarende teksten",
    "Ingangsdatum",
    "Bijlage",
    "Bijlagen",
    # Subsecties die als eigen-regel-label voorkomen
    "Toepassingsgebied van deze ISA",
    "Belangrijke uitgangspunten",
    "Belangrijke uitgangspunten in deze ISA",
    "Schaalbaarheid",
    "Begripsbepalingen",
)

# Aanvullende numerieke `Bijlage 1:` / `Bijlage 2:` varianten worden ook
# herkend via een aparte regex.
_BIJLAGE_NUMMER_RE = re.compile(
    r"^Bijlage\s+\d+(?:\s*[:\.\-—–]\s*.+)?$"
)


def _is_toc_line(stripped: str) -> bool:
    """True als een regel een TOC-entry is (dotted-leader + nummer)."""
    # TOC-pattern: label gevolgd door spaties/punten en eindigend op een
    # cijfer / cijfer-range / `A1-A5`.
    if re.search(r"\.{3,}", stripped):
        return True
    # Trailing reeks van enkel cijfers/letters-met-streep (A1-A57)
    if re.search(r"\s{2,}[\dA]\S*$", stripped):
        return True
    return False


def _line_is_promoteable_label(line: str) -> str | None:
    """Return het exacte label als de regel een ISA-sectielabel is, anders None."""
    stripped = line.strip()
    if not stripped:
        return None
    # Skip TOC-regels
    if _is_toc_line(stripped):
        return None
    # Exact-match tegen de gekende labels
    if stripped in _HEADING_LABELS:
        return stripped
    # `Bijlage 1: ...` style
    if _BIJLAGE_NUMMER_RE.match(stripped):
        return stripped
    return None


def inject_headings_isa(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Promoot ISA-sectielabels op eigen regel naar `## `-headings."""
    if not body:
        return body, frontmatter

    lines = body.split("\n")
    out: list[str] = []

    for line in lines:
        # Bestaande `## Label` overslaan (idempotency)
        if line.lstrip().startswith("## "):
            out.append(line)
            continue
        # Andere heading-levels (`#`, `###`) niet aanraken
        if line.lstrip().startswith("#"):
            out.append(line)
            continue
        label = _line_is_promoteable_label(line)
        if label is not None:
            out.append(f"## {label}")
        else:
            out.append(line)

    return "\n".join(out), frontmatter
