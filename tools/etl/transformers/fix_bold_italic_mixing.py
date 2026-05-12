r"""Transformer: normaliseer chaotische bold/italic-marker-mixing (D4 in CBN).

CBN-website rendert soms inconsistente markdown-emphasis-markers door
HTML-render-bugs in italic/bold combinaties. Drie veilige sub-patronen:

1. **Mid-word bold-marker**: `*N**iet...*` → `*Niet...*`
   Voorbeeld uit CBN-0167-02: `*N**iet in de balans...*` — auteur wou
   één italic, geen interne bold. Detect: `\w\*\*\w` (word-char, dubbele
   asterisk, word-char).

2. **3+ aaneengesloten asterisks** → `*` of strip:
   - `***Boekingen***` is bold+italic combo, te kwetsbaar — laat staan
   - `\*{4,}` (4+ asterisks aaneengesloten) zonder content tussen → strip
     (typisch lege link `****` of pure ruis).

3. **Lone trailing `**` zonder matching open**: niet auto-fixbaar zonder
   context — skip.

Veilig: legitieme `**bold**` en `*italic*` blijven onaangetast.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Mid-word `\w**\w` — `**` geplaatst tussen twee word-chars.
# Verwijder de `**` (waarschijnlijk een rendering-glitch).
_MID_WORD_BOLD_RE = re.compile(r"(\w)\*\*(\w)")

# 4+ aaneengesloten asterisks zonder content tussen — pure ruis (vaak lege link).
_FOUR_PLUS_STARS_RE = re.compile(r"\*{4,}")


def fix_bold_italic_mixing(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Normaliseer chaotische bold/italic-marker-mixing."""
    new_body = _MID_WORD_BOLD_RE.sub(r"\1\2", body)
    new_body = _FOUR_PLUS_STARS_RE.sub("", new_body)
    return new_body, frontmatter
