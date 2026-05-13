r"""Transformer: strip de cover-pagina van WBTW-MB-compilatie uit MB1.

De pdftotext-output van de WBTW-MB-compilatie bevat een uitgebreide cover:

  BELASTING OVER DE TOEGEVOEGDE WAARDE
  MINISTERIËLE BESLUITEN
  BIJGEWERKT TOT EN MET HET MB VAN 29.04.2024
  Federale Overheidsdienst FINANCIEN
  contact : comments.kms@minfin.fed.be
  ...
  Lijst van de ministeriële besluiten
   * Ministerieel besluit nr. 1, van 2 september 1980, ...
   * Ministerieel besluit nr. 2, van 21 december 2010, ...
   ...
   * Ministerieel besluit nr. 32, ...

De splitter wijst dit aan MB-1 (eerste split) toe, met als gevolg dat 80+
regels cover voor de eigenlijke MB-1-tekst staan. Dit transformer detecteert
de cover-pattern en strip het.

Sentinel: aanwezigheid van zowel:
  - "Lijst van de ministeriële besluiten" (of "...koninklijke besluiten")
  - meerdere `* Ministerieel/Koninklijk besluit nr. N` bullet-items achter elkaar

Strip-range: van "BELASTING OVER DE TOEGEVOEGDE WAARDE" (of vanaf body-start)
tot na het laatste bullet-item. Idempotent.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_COVER_LIST_HEADER_RE = re.compile(
    r"^Lijst van de (?:ministeriële|koninklijke) besluiten\s*$",
    re.I | re.M,
)

_COVER_BULLET_RE = re.compile(
    r"^\s*\*\s+(?:Ministerieel|Koninklijk)\s+besluit\s+nr\.\s+\d+",
    re.I,
)

# Cover-start anchors — als één van deze in de eerste 100 regels staat én
# we vinden de Lijst+bullets, dan strippen we vanaf de eerste anchor.
_COVER_START_ANCHORS = (
    re.compile(r"^BELASTING OVER DE TOEGEVOEGDE WAARDE\s*$"),
    re.compile(r"^Federale\s*$|^Federale\s+Overheidsdienst", re.I),
    re.compile(r"^contact\s*:\s*comments\.kms@minfin", re.I),
    re.compile(r"^MINISTERIËLE BESLUITEN\s*$"),
    re.compile(r"^KONINKLIJKE BESLUITEN\s*$"),
)


def strip_mb_compilatie_cover(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip de WBTW-MB-compilatie cover-pagina (Lijst van MB's + intro)."""
    if not _COVER_LIST_HEADER_RE.search(body):
        return body, frontmatter

    lines = body.split("\n")

    # 1) Vind de regel-index van de Lijst-header.
    lijst_idx: int | None = None
    for i, line in enumerate(lines):
        if _COVER_LIST_HEADER_RE.match(line):
            lijst_idx = i
            break
    if lijst_idx is None:
        return body, frontmatter

    # 2) Verifieer dat er minstens 2 bullet-items zijn (anders is het mogelijk
    #    een legitieme verwijzing en strippen we niet).
    bullet_count = 0
    last_bullet_idx = lijst_idx
    j = lijst_idx + 1
    while j < len(lines):
        line = lines[j]
        if _COVER_BULLET_RE.match(line):
            bullet_count += 1
            last_bullet_idx = j
            j += 1
            continue
        stripped = line.strip()
        if not stripped:
            # Lege regel — mogelijk separator binnen lijst (vaak tussen bullets).
            j += 1
            continue
        # Non-bullet non-blank: alleen meebrengen als INGESPRONGEN continuation-line
        # (start met whitespace). Anders: einde van lijst.
        if line.startswith((" ", "\t")):
            last_bullet_idx = j
            j += 1
            continue
        # Niet-ingesprongen non-bullet regel → einde van cover-lijst.
        break

    if bullet_count < 2:
        return body, frontmatter

    # 3) Bepaal cover-start: eerste anchor-regel vóór lijst_idx, anders
    #    body-start (eerste non-blank regel).
    cover_start = 0
    for i in range(0, lijst_idx):
        line = lines[i]
        if any(p.match(line.strip()) for p in _COVER_START_ANCHORS):
            cover_start = i
            break
    else:
        # Geen anchor: begin bij eerste non-blank regel
        for i, line in enumerate(lines[:lijst_idx]):
            if line.strip():
                cover_start = i
                break

    # 4) Strip [cover_start .. last_bullet_idx] inclusief.
    new_lines = lines[:cover_start] + lines[last_bullet_idx + 1:]
    new_body = "\n".join(new_lines)
    # Collapse trailing blanks bij snij-punt.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
