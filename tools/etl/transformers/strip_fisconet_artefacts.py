"""
Transformer: strip_fisconet_artefacts (ADR-005 §4).

Verwijdert twee Fisconet-specifieke artefacten die de QA-laag flaggt op
bronnen met extract.method=custom_wetboek:

1. **TOC-fragment bovenaan body**: heading-blok zonder bijhorende tekst,
   vóór de eerste echte sectie met substantiële body-tekst.
   Opzij geschoven door 2-kolom PDF-extractie.
   Conservatief: alleen strippen als ER minstens 3 heading-blokken in de
   TOC-zone zijn (aaneengesloten blokken zonder ≥ 100 chars body-tekst).

2. **`Titel` als losse regel**: `^Titel$` op een eigen regel → verwijderen.

3. **`Bron : FINANCIEN`** (met of zonder spaties, variaties in
   hoofdletters/kleine letters) → verwijderen.

Idempotent: een tweede run wijzigt niets meer.
Conservatief: bij twijfel niet strippen.

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations

import re

# ─── Regexes ─────────────────────────────────────────────────────────────────

# Losse "Titel" als eigen regel (geen #-prefix, geen spaties na "Titel")
_RE_TITEL_LABEL = re.compile(r"^Titel\s*$", re.MULTILINE)

# "Bron : FINANCIEN" met variaties in spatiëring en hoofdletters
_RE_BRON_FINANCIEN = re.compile(
    r"^Bron\s*:\s*FINANCIEN\s*$",
    re.MULTILINE | re.IGNORECASE,
)

# Drempel voor "substantiële tekst": een niet-heading-regel met ≥ N chars
# markeert het begin van de echte inhoud (buiten het TOC-fragment).
_SUBSTANTIAL_LINE_CHARS = 100


def _strip_toc_fragment(body: str) -> str:
    """Verwijder het TOC-fragment bovenaan de body als dat detecteerbaar is.

    Strategie:
    - Bepaal de intro-zone: alles vóór de eerste ##-heading.
    - Scan daarna lineair. De TOC-zone loopt zolang:
      - elke niet-heading, niet-lege regel < _SUBSTANTIAL_LINE_CHARS chars heeft.
    - Zodra een niet-heading regel ≥ _SUBSTANTIAL_LINE_CHARS chars gevonden
      wordt, stop de scan: DEZE REGEL markeert het begin van de echte inhoud.
    - Conservatief: strip alleen als er minstens 3 ##-headings in de
      TOC-zone liggen (vóór de eerste substantiële regel).
    - Geeft de ongewijzigde body terug bij twijfel.
    """
    lines = body.split("\n")
    n = len(lines)

    # ── Stap 1: bepaal intro_end (eerste ##-heading) ──────────────────────
    intro_end = n
    for i, line in enumerate(lines):
        if re.match(r"^#{2,}\s", line):
            intro_end = i
            break

    if intro_end == n:
        return body  # geen sub-heading → niets te strippen

    # ── Stap 2: zoek de eerste substantiële niet-heading regel ────────────
    # Scan vanaf intro_end. Tel het aantal ##-headings in de TOC-zone.
    toc_heading_count = 0
    first_substantial_line: int | None = None

    for i in range(intro_end, n):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            continue  # lege regel: overslaan

        if re.match(r"^#{2,}\s", line):
            toc_heading_count += 1
        else:
            # Niet-lege, niet-heading regel
            if len(stripped) >= _SUBSTANTIAL_LINE_CHARS:
                # Eerste substantiële inhoudslijn gevonden
                first_substantial_line = i
                break
            # Korte niet-heading regel (bv. "Bijlagen.", TOC-label):
            # onderdeel van de TOC-zone, gewoon doorgaan

    if first_substantial_line is None:
        # Geen substantiële inhoudslijn gevonden → conservatief: niet strippen
        return body

    if toc_heading_count < 3:
        # Conservatief: < 3 ##-headings in TOC-zone → niet strippen
        return body

    # ── Stap 3: bepaal het werkelijke toc_end ─────────────────────────────
    # De TOC-zone eindigt op de regel VÓÓR de eerste substantiële inhoudslijn.
    # We willen echter ook de heading (als die er is) die net vóór de
    # substantiële lijn staat BEHOUDEN — die is de "opener" van de sectie.
    # Ga terug tot de dichtstbijzijnde ##-heading vóór first_substantial_line.
    toc_end = first_substantial_line
    for i in range(first_substantial_line - 1, intro_end - 1, -1):
        line = lines[i]
        if line.strip() and re.match(r"^#{2,}\s", line):
            # Dichtstbijzijnde heading vóór de substantiële lijn
            toc_end = i
            break
        if line.strip():
            # Niet-lege, niet-heading lijn (korte label) → ook TOC; ga verder
            continue

    # ── Stap 4: bouw de gestripte body ────────────────────────────────────
    intro_lines = lines[:intro_end]
    rest_lines = lines[toc_end:]

    # Verwijder overtollige lege regels aan het begin van rest_lines
    while rest_lines and not rest_lines[0].strip():
        rest_lines = rest_lines[1:]

    # Plak samen: intro + lege scheidslijn + rest
    result_lines = intro_lines
    if intro_lines and intro_lines[-1].strip():
        result_lines = result_lines + [""]
    result_lines = result_lines + rest_lines

    return "\n".join(result_lines)


def _strip_label_lines(body: str) -> str:
    """Verwijder 'Titel' en 'Bron : FINANCIEN' als losse regels.

    Na verwijdering worden meer dan 2 opeenvolgende lege regels gecollapsed
    zodat er maximaal één lege regel overblijft tussen twee blokken.
    """
    result = _RE_TITEL_LABEL.sub("", body)
    result = _RE_BRON_FINANCIEN.sub("", result)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result


def strip_fisconet_artefacts(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Verwijder Fisconet-artefacten: TOC-fragment + plain-text labels.

    Stap 1: verwijder 'Titel'- en 'Bron : FINANCIEN'-regels.
    Stap 2: verwijder het TOC-fragment bovenaan als ≥ 3 TOC-blokken detecteerbaar.

    Idempotent: een tweede run wijzigt niets meer.
    Conservatief: bij twijfel wordt er niets gestript.

    De frontmatter wordt niet gewijzigd.
    """
    if not body.strip():
        return body, frontmatter

    # Stap 1: verwijder label-regels (idempotent)
    result = _strip_label_lines(body)

    # Stap 2: verwijder TOC-fragment (idempotent)
    result = _strip_toc_fragment(result)

    return result, frontmatter
