"""
Transformer: strip_compilatie_appendix (ADR-005 §4).

Verwijdert het Fisconet-editorieel appendix aan het einde van KB/MB-splits
uit de pdftotext_compilatie_btw-extractor. Dit appendix bestaat uit:

  * Bijlage A — "Lijst van de bijwerkingen" (paginavervangings-overzicht)
  * Bijlage B — "Recente wijzigingen" + changelog van wetswijzigingen

Beide secties zijn Fisconet-publishingresidu, geen wettekst-inhoud.

Detectie-strategie (in volgorde van prioriteit):
  1. "Bijlage [letter]" op een eigen regel, gevolgd (binnen 4 regels) door
     een editorieel-label: "Lijst van de bijwerkingen", "Bijwerking"
     (kolom-header), of "Recente wijzigingen".
  2. "Bijlage" op een eigen regel, gevolgd door "Recente wijzigingen".
  3. "Recente wijzigingen" op een eigen regel (alleen of gevolgd door
     " – KB" / " - KB" suffix).

Conservatief: "BIJLAGE" (alle hoofdletters) en genummerde `## Bijlage N`-
markdown-headings worden NIET gestript — die horen bij de rechtskracht.

Idempotent: een tweede run wijzigt niets meer.

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations

import re

# ─── Patronen ─────────────────────────────────────────────────────────────────

# "Bijlage A" / "Bijlage B" / "Bijlage X" op een eigen regel
# Matcht alleen enkelvoudige letter-suffix, geen markdown-headings (geen #-prefix),
# geen Roman-nummerals (zoals "Bijlage III" in echte bijlagen).
_BIJLAGE_LETTER_RE = re.compile(r"^Bijlage\s+[A-Z]\s*$")

# "Bijlage" op een eigen regel (zonder suffix)
_BIJLAGE_BARE_RE = re.compile(r"^Bijlage\s*$")

# Editorieel-label: "Lijst van de bijwerkingen" of "Bijwerking" als kolom-header
# De "Bijwerking"-kolom-header verschijnt in twee varianten:
#   "   Bijwerking    t.e.m. B.S. van..."  (met t.e.m.)
#   "   Bijwerking    Te vervangen pagina's"  (zonder t.e.m.)
# Let op: \b werkt niet na een punt; match termineert vóór spaties/t.e.m./Te.
_BIJWERKINGEN_LABEL_RE = re.compile(
    r"^(Lijst van de bijwerkingen"
    r"|KB\b.*Lijst van de bijwerkingen"
    r"|\s+Bijwerking\s+(?:t\.e\.m\.|Te vervangen)"
    r"|Bijwerking\s+(?:t\.e\.m\.|Te vervangen))",
    re.I,
)

# "Recente wijzigingen" al dan niet met " – KB..." of " - KB..." suffix
_RECENTE_WIJZIGINGEN_RE = re.compile(r"^Recente wijzigingen(\s*[–\-]|\s*$)", re.I)

# Decoratieve sterrenlijn: "   *   *   *   *   *" (Fisconet-sectie-scheider)
_STAR_SEPARATOR_RE = re.compile(r"^\s*\*(\s+\*){2,}\s*$")


def _is_editorial_label(line: str) -> bool:
    """Return True als de lijn een bekende editorieel-label is."""
    stripped = line.strip()
    return bool(
        _BIJWERKINGEN_LABEL_RE.match(line)
        or _BIJWERKINGEN_LABEL_RE.match(stripped)
        or _RECENTE_WIJZIGINGEN_RE.match(stripped)
    )


def _find_appendix_start(lines: list[str]) -> int | None:
    """Zoek de eerste regel van het Fisconet-appendix.

    Geeft de index van de trigger-regel terug, of None als niet gevonden.

    Detectie (in prioriteitsvolgorde):
      1. "Bijlage [letter]" gevolgd door editorieel-label (binnen 4 regels).
      2. "Bijlage" (bare) gevolgd door "Recente wijzigingen" (binnen 4 regels).
      3. "Recente wijzigingen" op een eigen regel.
    """
    n = len(lines)
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Variant 3: directe "Recente wijzigingen"-trigger
        if _RECENTE_WIJZIGINGEN_RE.match(stripped):
            return i

        # Variant 1: "Bijlage [letter]"
        if _BIJLAGE_LETTER_RE.match(stripped):
            # Kijk de volgende 4 niet-lege regels na op editorieel-label
            seen = 0
            for j in range(i + 1, min(i + 8, n)):
                ns = lines[j].strip()
                if not ns:
                    continue
                seen += 1
                if _is_editorial_label(lines[j]) or _is_editorial_label(ns):
                    return i
                if seen >= 4:
                    break

        # Variant 2: bare "Bijlage"
        if _BIJLAGE_BARE_RE.match(stripped):
            for j in range(i + 1, min(i + 5, n)):
                ns = lines[j].strip()
                if not ns:
                    continue
                if _RECENTE_WIJZIGINGEN_RE.match(ns):
                    return i
                break  # Eerste niet-lege lijn na "Bijlage" niet "Recente" → geen match

    return None


def strip_compilatie_appendix(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Verwijder het Fisconet-editorieel appendix (Bijlage A/B bijwerkingen +
    Recente wijzigingen) van het einde van een KB/MB-split.

    Conservatief:
    - Strips enkel als de trigger-regel duidelijk editorieel is.
    - BIJLAGE (all-caps) en markdown-headings (## Bijlage N) blijven ongemoeid.
    - Idempotent.

    Geeft de ongewijzigde body terug als geen appendix gedetecteerd.
    """
    if not body.strip():
        return body, frontmatter

    lines = body.split("\n")
    appendix_start = _find_appendix_start(lines)

    if appendix_start is None:
        return body, frontmatter

    # Kap het appendix af; strip overtollige lege regels aan het einde
    kept = lines[:appendix_start]
    while kept and not kept[-1].strip():
        kept.pop()

    result = "\n".join(kept) + "\n"
    return result, frontmatter
