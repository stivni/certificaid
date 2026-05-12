"""Transformer: merge spurious paragraph-breaks midden in een zin.

CBN-website rendert soms paragrafen op verkeerde plek — een zin krijgt midden
in een lege regel door PDF-conversie of redactionele opmaak:

    worden geïdentificeerd Bij de als dekking

    bestemde verrichtingen moet een onderscheid

De zin loopt door maar staat in twee paragrafen. Conservatieve heuristiek:

  - Vorige regel eindigt op een KLEINE letter of komma
  - Volgende regel begint met een KLEINE letter (geen hoofdletter, geen heading)
  - Tussen beide één of meer lege regels
  - Geen list-marker, table-pipe of heading-marker bij next-line

Bij match: merge de twee non-empty regels op één regel met spatie ertussen.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
Gewired in adviezen-chain (cbn_advies).
"""
from __future__ import annotations

import re

# Vorige regel eindigt met lowercase letter, voetnoot-ref, of komma.
# Footnote-ref-suffix `[^N]` telt als "midden in zin" (de zin gaat door).
_PREV_ENDS_MIDSENTENCE_RE = re.compile(r"(?:[a-zéèêëàâîïôûüçñ]|,|\[\^\d+\])$")

# Volgende regel begint met lowercase letter — geen hoofdletter,
# geen heading, geen list-marker, geen pipe.
_NEXT_STARTS_LOWERCASE_RE = re.compile(r"^\s*[a-zéèêëàâîïôûüçñ]")


def merge_broken_sentences(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Merge zinnen die door spurious paragraph-break gesplitst zijn."""
    lines = body.split("\n")
    out_lines: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out_lines.append(line)
        # Check of we kunnen mergen met volgende non-empty regel
        if (line.strip()
            and _PREV_ENDS_MIDSENTENCE_RE.search(line.rstrip())
            and not line.lstrip().startswith(("#", "-", "*", "|", "1.", "2.", "3."))):
            # Verzamel lege regels
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j > i + 1 and j < len(lines):
                next_line = lines[j]
                if (_NEXT_STARTS_LOWERCASE_RE.match(next_line)
                    and not next_line.lstrip().startswith(("#", "-", "*", "|"))):
                    # Merge: vervang de laatste out_lines[-1] door
                    # `current + " " + next_line`, skip de lege regels en de next-line.
                    out_lines[-1] = line.rstrip() + " " + next_line.lstrip()
                    i = j + 1
                    continue
        i += 1
    return "\n".join(out_lines), frontmatter
