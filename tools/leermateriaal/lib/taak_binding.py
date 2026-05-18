"""Taak-binding voor minicursus-render (ADR-010 §implicatie-5).

Resolve welke ITAA-taken een minicursus-hoofdstuk raakt, via de ketting:

    hoofdstuk (records via wikilinks) → record.linked_anchors[] →
        anchor_id → ofwel direct "X.Y.taak.N" ofwel kenniselement → taak

Voor PO's met één taak: fallback "alle inhoudelijke hoofdstukken → die ene taak"
als geen record een expliciet taak-anchor draagt. Voor PO's met meerdere taken
zonder expliciete bindings: curator-warning (taak-mapping is dan onvolledig).
"""
from __future__ import annotations

import re
from typing import TypedDict

TAAK_ANCHOR_RE = re.compile(r"^(\d+\.\d+)\.taak\.(\d+)$")
"""Match anchor-id van vorm 'X.Y.taak.N'."""


NIVEAU_TOELICHTINGEN: dict[str, str] = {
    "kennen": (
        "Je moet de definities, regels en termijnen van dit programmaonderdeel "
        "paraat hebben — woordelijk weten."
    ),
    "begrijpen": (
        "Je moet de samenhang tussen de begrippen kunnen uitleggen — "
        "niet alleen weten *wat*, ook *waarom*."
    ),
    "toepassen": (
        "Je moet deze regels en begrippen kunnen toepassen op een nieuwe casus — "
        "herkennen welk concept geldt en de stappen correct uitvoeren."
    ),
    "integratie": (
        "Je moet meerdere concepten samen kunnen inzetten in complexe casussen — "
        "onderdelen herkennen, prioriteren, en tot een coherent oordeel komen."
    ),
}
"""Studie-niveau → toelichtingszin voor de oriëntatie-callout
(docs/studiemateriaal-schrijfregels.md §9)."""


HOOFDSTUK_TYPES_GEEN_TAAK: frozenset[str] = frozenset({
    "orientatie",
    "oriëntatie",
    "voorbereiding",
})
"""Hoofdstuk-types die per definitie géén taak-marker krijgen.

- orientatie: introductie van het PO, geen taak-werk
- voorbereiding: fundament voor meerdere taken zonder 1:1-mapping
  (leerpad-schema 1.1, ADR-007)
"""


class TaakDekking(TypedDict):
    taak_code: str
    taak_tekst: str
    sectie_nummers: list[int]
    status: str
    cross_po: str | None


def niveau_toelichting(niveau: str) -> str:
    """Eén-zin toelichting voor de niveau-callout van de minicursus."""
    if not niveau:
        return ""
    return NIVEAU_TOELICHTINGEN.get(niveau.lower(), "")


def _records_in_hoofdstuk(hoofdstuk: dict, records_dict: dict[str, dict]) -> list[dict]:
    """Verzamel alle records die in dit hoofdstuk worden aangeraakt.

    Werkt voor leerpad-hoofdstuk-types:
    - thematisch: hoofdstuk['concepten'][] → lookup in records_dict
    - voorbereiding: zelfde
    - competentie: hoofdstuk['competentie'] is de record zelf
    - synthese: hoofdstuk['synthese'] is de record zelf
    - oriëntatie: geen records
    """
    htype = hoofdstuk.get("type", "")
    if htype in ("thematisch", "voorbereiding"):
        ids = hoofdstuk.get("concepten", []) or []
        return [records_dict[i] for i in ids if i in records_dict]
    if htype == "competentie":
        comp = hoofdstuk.get("competentie")
        return [comp] if comp else []
    if htype == "synthese":
        syn = hoofdstuk.get("synthese")
        return [syn] if syn else []
    return []


def resolve_taken_voor_hoofdstuk(
    hoofdstuk: dict,
    records_dict: dict[str, dict],
    programmaonderdeel: dict,
) -> set[str]:
    """Resolve welke taak-codes (`X.Y.taak.N`) dit hoofdstuk raakt.

    Returnt lege set voor `orientatie`/`voorbereiding` (per ADR-007/010 design)
    en voor `oriëntatie` (alternatieve spelling).

    Voor andere types:
    1. Scan `linked_anchors` van alle records in dit hoofdstuk
    2. Match anchors op `X.Y.taak.N`-patroon
    3. Als geen matches én PO heeft één taak: fallback naar die ene taak
    4. Anders: lege set (curator-warning bij render-time)

    Args:
        hoofdstuk: leerpad-hoofdstuk-dict (verrijkt met competentie/synthese-records)
        records_dict: id → record-dict voor snelle lookup
        programmaonderdeel: PO-dict uit programma.json (voor 1-taak-fallback)

    Returns:
        set van taak-codes (bv. {"1.5.taak.1"})
    """
    if hoofdstuk.get("type", "") in HOOFDSTUK_TYPES_GEEN_TAAK:
        return set()

    records = _records_in_hoofdstuk(hoofdstuk, records_dict)
    po_code = str(programmaonderdeel.get("code", ""))

    taken: set[str] = set()
    for record in records:
        for anchor in record.get("linked_anchors", []) or []:
            match = TAAK_ANCHOR_RE.match(anchor)
            if match and match.group(1) == po_code:
                taken.add(anchor)

    if taken:
        return taken

    # Fallback: PO met één taak en hoofdstuk heeft inhoudelijke records
    if records and len(programmaonderdeel.get("taken", [])) == 1:
        enige_taak = programmaonderdeel["taken"][0].get("code")
        if enige_taak:
            return {enige_taak}

    return set()


def bouw_taak_dekking(
    leerpad: dict,
    records_dict: dict[str, dict],
    programmaonderdeel: dict,
    sectie_offset: int = 1,
) -> list[TaakDekking]:
    """Bouw eind-dashboard data: per taak welke secties dekken hem?

    `sectie_offset` is de H2-index van het eerste inhoudelijke hoofdstuk
    (na oriëntatie + Leesgids + Waarom-PO etc.). Default 1 — render-laag
    kan dit overschrijven na vaste leesgids-/waarom-secties.

    Args:
        leerpad: leerpad-YAML-dict
        records_dict: id → record voor lookup
        programmaonderdeel: PO-dict uit programma.json
        sectie_offset: H2-volgnummer van eerste inhoudelijke hoofdstuk

    Returns:
        Lijst van taak-dekking-dicts, één per taak van het PO
    """
    hoofdstukken = leerpad.get("hoofdstukken", [])
    # Map taak_code → list van sectie_nummers die deze taak raken
    taken_naar_secties: dict[str, list[int]] = {}

    for i, hoofdstuk in enumerate(hoofdstukken):
        sectie_nr = sectie_offset + i
        for taak in resolve_taken_voor_hoofdstuk(hoofdstuk, records_dict, programmaonderdeel):
            taken_naar_secties.setdefault(taak, []).append(sectie_nr)

    dekking: list[TaakDekking] = []
    for taak in programmaonderdeel.get("taken", []):
        taak_code = taak.get("code", "")
        secties = sorted(taken_naar_secties.get(taak_code, []))
        if secties:
            status = "gedekt"
        else:
            status = "niet_gedekt"
        dekking.append(TaakDekking(
            taak_code=taak_code,
            taak_tekst=taak.get("tekst", ""),
            sectie_nummers=secties,
            status=status,
            cross_po=None,  # cross-PO-detectie nog niet geïmplementeerd
        ))

    return dekking


def alle_po_taak_bindings(
    leerpad: dict,
    records_dict: dict[str, dict],
    programmaonderdeel: dict,
) -> list[set[str]]:
    """Per hoofdstuk in het leerpad: set van gekoppelde taak-codes.

    Volgorde matcht `leerpad['hoofdstukken']`. Returnt lege set voor
    oriëntatie/voorbereiding-hoofdstukken.
    """
    return [
        resolve_taken_voor_hoofdstuk(h, records_dict, programmaonderdeel)
        for h in leerpad.get("hoofdstukken", [])
    ]
