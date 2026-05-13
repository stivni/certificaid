r"""Transformer: normaliseer 'Artikel N' (kolom 0) naar 'Art. N' headings.

Sommige pdftotext-outputs van wetteksten (vooral MB29apr2024-kassasysteem)
renderen artikel-headings als full word 'Artikel' op kolom 0 i.p.v. de
verkorte 'Art.' vorm. inject_headings_wettekst herkent 'Artikel' niet als
artikel-heading omdat het de 'Art.' afkorting verwacht.

Twee vormen worden genormaliseerd:

1. Alleen-op-de-regel: `Artikel 86` → `Art. 86`
2. Met body inline op één regel: `Artikel 46. Elk kassasysteem moet ...`
   → splits in `Art. 46\n\nElk kassasysteem moet ...`

Conservatief:
- Alleen op kolom 0 (geen leading whitespace) — anders gebrand als
  body-tekst die toevallig 'Artikel 46.' citeert.
- Vereist artikel-nummer in eerste 5 chars (Artikel + N).
- Title-text na de punt blijft als body op nieuwe regel.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_ART_BIS_SUFFIX = (
    r"(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|"
    r"undecies|duodecies|terdecies|quaterdecies)"
)

# Alleen-op-regel: "Artikel 86", "Artikel 86.", "Artikel 12bis"
_ARTIKEL_BARE_RE = re.compile(
    rf"^Artikel\s+(\d+(?:{_ART_BIS_SUFFIX})?(?:/\d+)?)\.?\s*$"
)

# Met body inline: "Artikel 46. Elk kassasysteem moet voorzien zijn van ..."
_ARTIKEL_WITH_BODY_RE = re.compile(
    rf"^Artikel\s+(\d+(?:{_ART_BIS_SUFFIX})?(?:/\d+)?)\.\s+(\S.+)$"
)


def normalize_artikel_to_art(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Normaliseer 'Artikel N'-lijnen op kolom 0 naar 'Art. N'-headings."""
    out: list[str] = []
    for ln in body.split("\n"):
        m_bare = _ARTIKEL_BARE_RE.match(ln)
        if m_bare:
            out.append(f"Art. {m_bare.group(1)}")
            continue
        m_body = _ARTIKEL_WITH_BODY_RE.match(ln)
        if m_body:
            num = m_body.group(1)
            inline_body = m_body.group(2).strip()
            out.append(f"Art. {num}")
            out.append("")
            out.append(inline_body)
            continue
        out.append(ln)
    return "\n".join(out), frontmatter
