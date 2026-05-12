"""Transformer: strip whitespace adjacent to italic-markers (D4 in CBN-adviezen).

CBN-HTML rendert soms `<em>foo </em>` (met trailing whitespace BINNEN de em-tag).
Onze parser emit `*` open + content + `*` close, met de whitespace direct vóór
de closing `*`. Resultaat: `*foo *` — defecte markdown-italic-syntax die door
sommige renderers (en RAG-chunkers) niet als italic herkend wordt.

Drie varianten:
- `*foo *` (trailing whitespace voor closing `*`)
- `* foo*` (leading whitespace na opening `*`)
- `* foo *` (beide)

Fix: strip whitespace direct na opening `*` en direct voor closing `*` binnen
één italic-paar. Behoud whitespace ELDERS in de body (alleen tussen `*` en
content wordt aangeraakt).

Niet aanraken:
- Bold `**foo **` — andere transformer of bold-context (markdown bold is
  toleranter; bovendien is `**` opening niet `*` open).
- Lijstmarkers `* item` aan begin regel — die zijn geen italic.
- Multi-line italics (over `\n` heen) — risicovol, skip.

Conform ADR-005 §1: format-agnostische tekst-transformatie → transformer-laag.
"""
from __future__ import annotations

import re

# Match een complete italic-pair: opening `*` (niet bold), content zonder `*`
# of newline, closing `*` (niet bold). Niet-greedy zodat we de KORTSTE pair
# nemen — zo gegarandeerd dat we niet over een ander italic-paar heen springen.
#
# Voorbeeld: in "Een *foo* en *bar*" matcht non-greedy 2× los: `*foo*` en `*bar*`,
# niet `*foo* en *bar*` als één lange greedy match.
_ITALIC_PAIR_RE = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")


def fix_italic_spacing(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip whitespace adjacent to italic-markers binnen elk italic-pair."""

    def _normalize(match: "re.Match[str]") -> str:
        content = match.group(1)
        stripped = content.strip()
        if not stripped:
            # `*  *` leeg/whitespace-only — onveranderd laten (riskant te raken)
            return match.group(0)
        return f"*{stripped}*"

    new_body = _ITALIC_PAIR_RE.sub(_normalize, body)
    return new_body, frontmatter
