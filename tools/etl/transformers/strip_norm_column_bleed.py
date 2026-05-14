r"""Transformer: strip column-bleed-artefacten uit ITAA-norm-PDFs.

Sommige ITAA-normen zijn opgemaakt als tweekoloms PDF (linkerkolom
``VEREISTEN``, rechterkolom ``TOEPASSINGSMODALITEITEN``). pdftotext leest
deze kolommen niet correct uit: kolomtitels worden samengevoegd op één
heading-regel en NL+FR-headings (bilingue normen) blijven naast elkaar
staan.

Patronen die deze transformer aanpakt:

1. **Standalone gemergde kolomtitel** — ``## VEREISTEN TOEPASSINGSMODALITEITEN``
   is pure boilerplate uit de PDF-template, geen echte sectie. Volledig
   strippen (header-lijn + omliggende blanco-regel-redundantie).

2. **Compound heading met trailing kolomtitel** — bv.
   ``## II.2. Aard van de opdracht VEREISTEN TOEPASSINGSMODALITEITEN``.
   Trailing ``VEREISTEN TOEPASSINGSMODALITEITEN`` strippen, de echte
   NL-heading behouden.

3. **Bilingue NL+FR heading** — bv. ``## Aanvaarding van opdrachten
   Acceptation de missions``. Het FR-deel is een kolom-bleed uit de
   rechterkolom (tweetalige PDF). FR-deel strippen via taal-marker-woorden.

4. **Pure FR-heading** — bv. ``## Fin des relations clients``. Bestaat
   enkel uit FR-woorden, restant van rechterkolom-bleed. Volledig strippen.

5. **Standalone FR-lek als plain-tekst** (niet als heading) — een losse
   FR-woordrij die als standalone tekstregel verschijnt, bv. ``demande.``
   (residu van een FR-pagina-header in een tweetalig document). Alleen
   een beperkte whitelist van herkenbare kortste FR-lekken wordt gestript;
   de context moet een geïsoleerde standalone regel zijn.

WAT DEZE TRANSFORMER NIET DOET: de correcte kolom-volgorde van de
body-tekst reconstrueren. Daarvoor zou column-aware PDF-extractie
(bv. pymupdf met blocks) nodig zijn. Buiten scope.

Conform ADR-005 §1: format-agnostische tekst-transformatie, idempotent.
"""
from __future__ import annotations

import re

# Patroon 1 & 2: gemergde kolomtitels.
# ``VEREISTEN TOEPASSINGSMODALITEITEN`` (eventueel met extra whitespace).
_BLEED_MARKER = r"VEREISTEN\s+TOEPASSINGSMODALITEITEN"

# Standalone gemergde kolomtitel-heading (alleen de twee woorden).
# Optioneel met trailing parenthetical-referentie zoals ``(Zie Par. 22)`` of
# ``(Zie Par. 23, 25(e)(iii))`` (zoals voorkomt in ISA/ISRS-normen). De
# trailing-suffix is geen body-content maar deel van de kolom-marker. Match
# greedy tot einde regel zodat geneste parens (bv. ``25(e)(iii)``) meegaan.
_STANDALONE_BLEED_HEADING_RE = re.compile(
    rf"^#{{1,6}}\s+{_BLEED_MARKER}(?:\s+\(\s*(?:Zie|Ref\.?)\b.*)?\s*$",
    re.IGNORECASE,
)

# Compound heading: ## <iets> VEREISTEN TOEPASSINGSMODALITEITEN
# Strip trailing marker; behoud heading-prefix + NL-tekst.
_COMPOUND_BLEED_HEADING_RE = re.compile(
    rf"^(?P<prefix>#{{1,6}}\s+\S.+?)\s+{_BLEED_MARKER}\s*$"
)

# FR-markers voor bilingue heading-bleed.
# Zekere FR-woorden die in NL nooit zo voorkomen. Bewust beperkt tot de
# patronen die in de ITAA-normen daadwerkelijk voorkomen.
_FR_WORDS = (
    "Acceptation",
    "Documentation",
    "Fin",  # "Fin des ..."
    "Mission",  # ook "Missions", "missions"
    "missions",
    "des",
    "de",
    "du",
    "Continuité",
    "Continuite",
    "Engagement",
    "Acceptance",  # EN-leak komt ook voor in oudere PDF-templates
    "relations",
    "clients",
    "Relation",
    "Relations",
)

# Een woord is "FR" als het in de FR-marker-set staat.
_FR_WORD_SET = {w for w in _FR_WORDS}

# Heading-prefix-detectie (#, ##, ...).
_HEADING_PREFIX_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# Pure FR-marker-headings die zekere overblijfselen zijn van rechterkolom.
# Conservatief: alleen specifieke FR-zinnen die we in de PDFs zien.
_PURE_FR_HEADING_PATTERNS = (
    re.compile(r"^Fin\s+des?\s+\S+", re.IGNORECASE),
    re.compile(r"^Acceptation\s+de\s+\S+", re.IGNORECASE),
    re.compile(r"^Continuité?\s+de\s+\S+", re.IGNORECASE),
)

# Patroon 5: standalone FR-lekken als plain-tekst (geen heading).
# Whitelist van herkenbare korte FR-lekresten die als standalone regel voorkomen.
# Bewust heel beperkt om false-positives te vermijden. Een "standalone" regel is
# een regel die volledig uit de whitelisted string bestaat (optioneel met
# interpunctie aan het einde), dus GEEN langere zin.
#
# 'demande.' — FR-equivalent van 'verzoek', residu uit NL/FR tweetalig document
#   (ITAA-norm-intern-kwaliteitsmanagement, regel 237 in de MD).
# 'du', 'de', 'des' — FR-voorzetsels die soms als losstaand fragment overblijven.
_STANDALONE_FR_LEK_RE = re.compile(
    r"^\s*(?:demande|du|des?)\s*\.?\s*$",
    re.IGNORECASE,
)


def _strip_bilingue_fr_tail(heading_text: str) -> str:
    """Strip FR-tail van een bilingue NL+FR heading.

    Heuristiek: scan woord-voor-woord van rechts naar links. Zolang het
    rechter-woord een FR-marker is (of FR-bijwoord zoals 'de', 'des'),
    verwijder het. Stop zodra een woord NL-only is (geen FR-marker en
    geen lowercase verbindingswoord na een FR-marker).

    Belangrijke veiligheid: er moet minstens één duidelijk FR-anchor-woord
    (Acceptation, Documentation, Mission, etc.) gevonden worden vóór we
    iets strippen. Anders gevaar voor false-positives.
    """
    woorden = heading_text.split()
    if len(woorden) < 2:
        return heading_text

    # Vind het laatste anchor-FR-woord (typisch een naamwoord).
    # Anchor = woord dat zeker FR is (hoofdletter en in marker-set).
    anchor_words = {"Acceptation", "Documentation", "Mission", "Missions",
                    "Continuité", "Continuite", "Engagement", "Acceptance",
                    "Relation", "Relations"}

    # Zoek vanaf rechts naar een anchor.
    anchor_idx = -1
    for i in range(len(woorden) - 1, -1, -1):
        if woorden[i] in anchor_words:
            anchor_idx = i
            break

    if anchor_idx == -1:
        return heading_text

    # Vanaf het anchor naar links: zolang elk woord een FR-marker is,
    # blijft de "FR-staart" groeien. We strippen vanaf het eerste woord
    # van de FR-staart.
    fr_start = anchor_idx
    # Optioneel: woorden rechts van anchor (bv. "Acceptation de missions")
    # zijn ook FR.
    # Werkwijze: vanaf anchor_idx, ga naar links zolang het woord in FR-set zit.
    while fr_start > 0 and woorden[fr_start - 1] in _FR_WORD_SET:
        fr_start -= 1

    # Veiligheid: er moet minstens één NL-woord overblijven.
    if fr_start == 0:
        return heading_text  # alles FR — laat aan caller om te beslissen

    nl_deel = " ".join(woorden[:fr_start]).rstrip()
    return nl_deel


def _is_pure_fr_heading(heading_text: str) -> bool:
    """True als de heading enkel uit FR-woorden bestaat (kolom-bleed-restant)."""
    for pat in _PURE_FR_HEADING_PATTERNS:
        if pat.match(heading_text):
            return True
    return False


def strip_norm_column_bleed(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip column-bleed-artefacten uit ITAA-norm-bodies.

    Bewerkt regel-voor-regel. Conservatief: alleen wanneer een duidelijke
    kolom-bleed-marker aanwezig is.
    """
    out_lines: list[str] = []
    for line in body.split("\n"):
        # Patroon 1: standalone ## VEREISTEN TOEPASSINGSMODALITEITEN — strip volledig.
        if _STANDALONE_BLEED_HEADING_RE.match(line):
            continue

        # Patroon 2: compound heading met trailing VEREISTEN TOEPASSINGSMODALITEITEN.
        m = _COMPOUND_BLEED_HEADING_RE.match(line)
        if m:
            out_lines.append(m.group("prefix").rstrip())
            continue

        # Patroon 3 + 4: heading met FR-bleed.
        heading_match = _HEADING_PREFIX_RE.match(line)
        if heading_match:
            level = heading_match.group(1)
            text = heading_match.group(2)

            # Patroon 4: pure FR-heading → strip volledig.
            if _is_pure_fr_heading(text):
                continue

            # Patroon 3: bilingue NL+FR heading → strip FR-tail.
            stripped = _strip_bilingue_fr_tail(text)
            if stripped != text and stripped:
                out_lines.append(f"{level} {stripped}")
                continue

        # Patroon 5: standalone FR-lek als plain-tekst (niet als heading).
        if _STANDALONE_FR_LEK_RE.match(line):
            continue

        out_lines.append(line)

    return "\n".join(out_lines), frontmatter
