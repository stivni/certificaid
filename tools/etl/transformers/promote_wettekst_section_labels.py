r"""Transformer: promote 'Enig artikel' en 'Bijlage N' naar ## headings.

Sommige wetteksten (MB23jun2005, MB28okt2009, ...) bevatten standaard
sectie-labels als plain-text in plaats van markdown-headings:
- `Enig artikel` — centrale bepaling van een MB dat maar één artikel heeft
- `Bijlage 1`, `Bijlage I`, `Bijlage`, `Bijlage N1`, ... — bijlage-secties

Promote-criteria (zoals promote_norm_section_labels):
- Regel is exact-match (na strip)
- Paragraph-isolated (lege regel ervoor + erna)
- Whitelist labels (geen vrije regex)

Resultaat: `## Enig artikel`, `## Bijlage 1`, etc.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Whitelist labels:
# - "Enig artikel" (case-insensitive)
# - "Bijlage" optioneel met nummer (1/2/3/N1/N2/I/II/...) — exact-match alleen.
_LABEL_PATTERN = re.compile(
    r"^(?P<label>"
    r"Enig\s+artikel"
    r"|Bijlage(?:\s+(?:\d+|[IVX]+|N\d+))?"
    r"|TABEL\s+[A-Z]"
    r"|GOEDEREN(?:\s+AAN\s+\S+)?"
    r"|DIENSTEN(?:\s+AAN\s+\S+)?"
    r"|Tijdelijke\s+bepalingen?"
    r"|Slotbepalingen?"
    r"|Overgangsbepalingen?"
    r"|Inwerkingtreding"
    r")\s*$",
    re.I,
)


def promote_wettekst_section_labels(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Promote whitelisted plain-text wettekst-labels naar `## heading`."""
    lines = body.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        m = _LABEL_PATTERN.match(line.strip()) if line.strip() else None
        if m:
            prev_blank = (i == 0 or not lines[i - 1].strip())
            # next-line: blank OF amendment-annotation `(...)` (Belgische wettekst-stijl)
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            next_ok = (not next_line) or next_line.startswith("(")
            if prev_blank and next_ok:
                label = m.group("label").strip()
                # Normaliseer "enig artikel" → "Enig artikel"
                if label.lower().startswith("enig"):
                    label = "Enig artikel"
                elif label.lower().startswith("bijlage"):
                    # Preserve volume-suffix maar capitalize 'Bijlage'
                    rest = label[len("Bijlage"):].strip()
                    label = "Bijlage" + (" " + rest if rest else "")
                elif label.lower().startswith("tabel"):
                    # 'TABEL A' / 'tabel a' → 'Tabel A'
                    suffix = label[len("tabel"):].strip().upper()
                    label = f"Tabel {suffix}"
                elif label.upper() in ("GOEDEREN", "DIENSTEN"):
                    # ALL-CAPS structuurlabel — behoud caps stijl
                    label = label.strip()
                out.append(f"## {label}")
                continue
        out.append(line)
    return "\n".join(out), frontmatter
