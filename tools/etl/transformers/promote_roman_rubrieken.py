r"""Transformer: promote `I.` / `II.` / `XL.` rubrieken naar `### heading`.

KB20-tarieven heeft een tabel-structuur met Romeinse-cijfer rubrieken:

  ## GOEDEREN

  I. Levende dieren.

  (De tekst van KB nr. 20, TABEL A, I, 1°, is van toepassing met ...)

  1° Runderen, varkens, schapen ...

De rubriek-regels `I. Levende dieren.` zijn plain text terwijl ze de
sub-secties van GOEDEREN/DIENSTEN aanduiden. Voor RAG-chunking is dit
problematisch — GOEDEREN wordt één enorme chunk (>50k chars).

Promote-criteria:
- Regel matcht `^[IVXLCDM]+\.\s+<title>$` (Romeins + punt + titel)
- Title is een zelfstandige beschrijving (eindigt op punt of geen einde-leesteken)
- Paragraph-isolated: prev_blank, next blanco OF amendment-annotatie `(...)` OF
  beginnen met `1°` (eerste enumeratie-item van rubriek)
- Titel is <100 chars (heading-grootte)

Resultaat: `### I. Levende dieren.`

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# `I. Levende dieren.` / `IV. Melk en zuivelprodukten; eieren; honig.`
# / `XI. (Opgeheven bij KB 11.08.1972)` / `XV. (opgeheven bij KB 29.12.1992)`
_ROMAN_RUBRIEK_RE = re.compile(
    r"^(?P<roman>[IVXLCDM]+)\.\s+(?P<title>\S.{0,98})\s*$",
)


def promote_roman_rubrieken(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Promote `I. <Title>` regels naar `### I. <Title>` headings."""
    lines = body.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        m = _ROMAN_RUBRIEK_RE.match(line.strip()) if line.strip() else None
        if m:
            prev_blank = (i == 0 or not lines[i - 1].strip())
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            # next is OK als blank, OF amendment-annotatie `(...)`, OF `1°` item
            next_ok = (
                not next_line
                or next_line.startswith("(")
                or re.match(r"^\d+°", next_line)
            )
            if prev_blank and next_ok:
                roman = m.group("roman")
                title = m.group("title").strip()
                out.append(f"### {roman}. {title}")
                continue
        out.append(line)
    return "\n".join(out), frontmatter
