r"""Transformer: strip leading TOC-block bestaande uit kale headings.

Sommige PDF-extracties (notable: AVG-wet-2018) plaatsen de inhoudstafel
als een blok kale markdown-headings vóór de eigenlijke wettekst:

  # Titel
  *Bijgewerkt tot ...*

  ###### Art. 24             ← TOC begint (geen body)
  ## TITEL 2. - ...
  #### HOOFDSTUK I. - ...
  ###### Art. 252
  #### HOOFDSTUK I. - ...
  ###### Art. 280

  Tekst                       ← sentinel: einde TOC

  VOORAFGAANDE TITEL. - ...   ← echte body begint

De TOC heeft 200+ heading-regels zonder body tussen — pure inhoudsopgave.
RAG-chunking pikt deze lege headings op als losse documenten en de
hiërarchie springt willekeurig (H6 → H2 → H4).

Detectie-heuristiek (conservatief):
1. Vind een aaneengesloten regio na intro-paragrafen waar ≥ 80% van de
   non-blank regels markdown-headings zijn.
2. Regio moet minimaal 15 headings bevatten (random heading-cluster
   van 1-2 stuks blijft staan).
3. Regio eindigt OF bij een 'Tekst' / 'VOORAFGAANDE'-sentinel OF bij
   de eerste non-heading body-regel die volgt op de heading-run.
4. Strip regio.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_HEADING_RE = re.compile(r"^#{1,6}\s+\S")
_SENTINEL_RE = re.compile(
    r"^(?:Tekst|VOORAFGAANDE\s+TITEL\b|HOOFDSTUK\s+[IVX]+\.\s+\w|Artikel\s+1\.\s+\S).*$",
    re.I,
)


def strip_leading_toc_heading_block(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip leading TOC-block met ≥15 kale headings."""
    lines = body.split("\n")
    n = len(lines)

    # Skip H1 + intro tot eerste blanco regel + eerste body-content na intro
    i = 0
    # Skip H1
    while i < n and not lines[i].strip():
        i += 1
    if i < n and lines[i].startswith("# ") and not lines[i].startswith("## "):
        i += 1
    # Skip intro-paragrafen tot eerste H2+ heading OF non-blank non-heading-2+
    intro_end = i
    while intro_end < n:
        line = lines[intro_end]
        stripped = line.strip()
        if not stripped:
            intro_end += 1
            continue
        # H2-6 → TOC region begins here
        if _HEADING_RE.match(line) and not line.startswith("# "):
            break
        # non-heading body-text → niet TOC, stop hier
        intro_end += 1
        continue

    if intro_end >= n:
        return body, frontmatter

    # Scan vooruit voor een region van headings + blanks. Stop bij Tekst-sentinel
    # of bij een non-heading non-blank line.
    toc_start = intro_end
    toc_end = intro_end  # exclusive
    heading_count = 0
    j = intro_end
    while j < n:
        line = lines[j]
        stripped = line.strip()
        if not stripped:
            j += 1
            continue
        # Sentinels: stop direct (en strip tot hier exclusive)
        if stripped == "Tekst":
            # Strip ook de sentinel
            toc_end = j + 1
            break
        if _HEADING_RE.match(line):
            heading_count += 1
            toc_end = j + 1
            j += 1
            continue
        # Non-heading non-blank → einde TOC-block
        break

    if heading_count < 15:
        return body, frontmatter

    # Strip [toc_start..toc_end). Behoud blanks rondom voor leesbaarheid.
    new_lines = lines[:toc_start] + [""] + lines[toc_end:]
    new_body = "\n".join(new_lines)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
