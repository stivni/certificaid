"""Transformer: promote bekende ITAA-norm sectielabels naar ## headings.

Sommige ITAA-norm PDFs hebben standaard sectielabels (Overwegende, Definities,
Onderzoek, etc.) als plain-text in plaats van markdown-headings. Conservatieve
whitelist-approach: alleen exact-match standaard-labels worden gepromoveerd.

Whitelist gebaseerd op de 6 needs-rework normen (B4-patronen uit L2-pass):
- 'Definities'
- 'Overwegende:' (met optionele colon)
- 'Onderzoek'
- 'Wettelijke verplichting'
- 'Toepassingsgebied'
- 'Doelstelling'
- 'OPDRACHTBRIEF'
- 'Conclusie'
- N-eerste/tweede/derde principe (`Eerste principe` etc.)

Uitbreiding extensie 3 (ADR-005 Fase 1 fix):
- 'CABINET Doelstelling' — compound uppercase label uit intern-kwaliteitsmanagement
  (regel 142 in de norm: structuurlabel met kantoor-scope-aanduiding)
- 'KANTOORNIVEAU' — standalone uppercase sectie-indicator uit intern-kwaliteitsmanagement
  (regel 149 in de norm)

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Whitelist labels (exact match na strip, optional trailing `:` of newline).
# Title-case OR ALL-CAPS variants beide toegelaten.
_NORM_SECTION_LABELS = [
    "Overwegende",
    "Definities",
    "Onderzoek",
    "Wettelijke verplichting",
    "Toepassingsgebied",
    "Doelstelling",
    "Conclusie",
    "Inleiding",
    "OPDRACHTBRIEF",
    # Extensie 3: structuurlabels uit ITAA-norm-intern-kwaliteitsmanagement
    "CABINET Doelstelling",
    "KANTOORNIVEAU",
]

# Eerste/Tweede/.../Tiende + principe
_ORDINAL = r"(?:Eerste|Tweede|Derde|Vierde|Vijfde|Zesde|Zevende|Achtste|Negende|Tiende)"

_LABEL_PATTERN = re.compile(
    r"^(?P<label>(?:" + "|".join(re.escape(l) for l in _NORM_SECTION_LABELS) + r"|" + _ORDINAL + r"\s+principe))\s*:?\s*$",
)


def promote_norm_section_labels(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Promote whitelisted plain-text norm-sectie-labels naar `## heading`.

    Vereist: regel is exact-match (na strip + optional colon), tussen lege
    regels (paragraph-isolated).
    """
    lines = body.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        m = _LABEL_PATTERN.match(line.strip()) if line.strip() else None
        if m:
            prev_blank = (i == 0 or not lines[i - 1].strip())
            next_blank = (i >= len(lines) - 1 or not lines[i + 1].strip())
            if prev_blank and next_blank:
                label = m.group("label").rstrip(":")
                out.append(f"## {label}")
                continue
        out.append(line)
    return "\n".join(out), frontmatter
