r"""Transformer: merge headings die over twee regels gebroken zijn.

Pdftotext breekt soms een lange heading-titel op twee regels:

  ## TITEL II. - TECHNISCHE EISEN TEN AANZIEN VAN DE ONDERDELEN VAN EEN
  GEREGISTREERD KASSASYSTEEM

  ###### Art. 3
  Body...

De heading-injectie ziet dit als ÉÉN heading + 1 plain-text-regel, en
de body-tekst raakt de heading-hiërarchie kwijt.

Detectie-heuristiek (conservatief):
1. Heading-regel (^#{1,6}\s+\S) eindigt NIET op punt/colon/punctuatie,
   en eindigt met een hoofdletter-woord (typisch ALL-CAPS heading).
2. Volgende non-blank regel begint met hoofdletter (geen heading, geen
   list-marker) en bestaat uit ALL-CAPS of Title-case woorden.
3. Eerstvolgende regel daarna is blanco of een sub-heading.

Bij match: join de twee regels met spatie. Resultaat:
  ## TITEL II. - TECHNISCHE EISEN ... ONDERDELEN VAN EEN GEREGISTREERD KASSASYSTEEM

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_HEADING_RE = re.compile(r"^(#{1,6})\s+(\S.*)$")
# ALL-CAPS continuation: alleen hoofdletters, cijfers, spaties, leestekens.
_ALLCAPS_CONT_RE = re.compile(r"^[A-Z][A-Z0-9 .,\-'°§]{2,}$")
# Eindigt met een 'incomplete' woord (hoofdletter, geen sluit-punt/colon)
_HEADING_INCOMPLETE_RE = re.compile(r"[A-Z]{2,}$")


def merge_wrapped_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Merge gebroken heading-regels (pdftotext line-wrap in heading)."""
    lines = body.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _HEADING_RE.match(line)
        if m and i + 1 < len(lines):
            heading_text = m.group(2)
            # Eindigt heading op een 'incomplete' ALL-CAPS woord (zonder . of :)?
            stripped_text = heading_text.rstrip()
            if (not stripped_text.endswith((".", ":", "?", "!", ")", "—"))
                and _HEADING_INCOMPLETE_RE.search(stripped_text)):
                next_line = lines[i + 1]
                if _ALLCAPS_CONT_RE.match(next_line.strip()):
                    # Check dat na de continuation een blank/heading volgt
                    if i + 2 >= len(lines) or not lines[i + 2].strip() or lines[i + 2].lstrip().startswith("#"):
                        merged = f"{m.group(1)} {stripped_text} {next_line.strip()}"
                        out.append(merged)
                        i += 2
                        continue
        out.append(line)
        i += 1
    return "\n".join(out), frontmatter
