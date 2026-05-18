"""Splits een examenvraag-blok in individuele sub-vragen (j/f, MC, open).

PDF-extractie levert vaak één vraag met meerdere onderdelen (sub-vragen A/B/C/D,
soms met j/f-sets of MC-opties). Voor pedagogische rendering willen we elk
individueel item als één voorbeeldvraag tonen: één j/f-stelling = één
voorbeeldvraag, één MC-vraag = één voorbeeldvraag.

Heuristiek:
- Niveau-1-markers: paragraph begint met "A. ", "B. ", "C. ", "D. ", "E. "
- Per sub-blok type-detectie via keywords + body-structuur:
  - "Juist/fout"-keywords + body met letter-prefixed lijst → j_f_set
    (elke stelling wordt eigen sub-vraag)
  - Body met letter-prefixed lijst zonder j/f-keywords → MC (één sub-vraag
    met opties[])
  - Anders → open vraag (één sub-vraag)
- Onderdrukt het PDF-extract artefact "A. a." / "B. b." (dubbele prefix
  doordat PDF de MC-opties opnieuw met hoofdletter prefixt)

Bij minder dan 2 sub-blokken: returnt lege lijst (caller toont vraagtekst as-is).
"""
from __future__ import annotations

import re
from typing import Literal, TypedDict

NIVEAU1_MARKER = re.compile(r"^([A-Z])\.\s+(.+)", re.DOTALL)
"""Match niveau-1 sub-vraag-marker: paragraph begint met "A. ", "B. ", enz."""

DUBBEL_PREFIX = re.compile(r"^([A-Z])\.\s+([a-z])[.)]\s+(.+)", re.DOTALL)
"""Match PDF-artefact: "A. a. <tekst>" of "B. b) <tekst>" — dubbele letter
door PDF-extractor die MC-opties opnieuw met hoofdletter prefixed."""

MC_OPTIE = re.compile(r"^([a-z])[.)]\s+(.+)", re.DOTALL)
"""Match MC-optie of sub-stelling: "a. <tekst>" of "a) <tekst>"."""

JF_KEYWORDS = re.compile(r"juist\s*/?\s*fout|stellingen.*juist|kruis.*juist", re.IGNORECASE)


class SubVraag(TypedDict):
    sub_id: str
    type: Literal["j_f_set", "mc", "open"]
    stem: str
    context: str
    opties: list[str]        # MC-antwoord-opties
    stellingen: list[str]    # j/f-stellingen (één per regel, allemaal beantwoord met juist/fout)


def _is_dubbel_prefix(paragraph: str) -> bool:
    """True voor PDF-artefact 'A. a. ...' (MC-optie met dubbele prefix)."""
    return bool(DUBBEL_PREFIX.match(paragraph))


def _extract_optie_uit_dubbel(paragraph: str) -> str | None:
    """Pak de tekst-payload uit een 'A. a. <tekst>'-paragraph."""
    m = DUBBEL_PREFIX.match(paragraph)
    if not m:
        return None
    return m.group(3).strip()


def _extract_optie_uit_kleinletter(paragraph: str) -> str | None:
    """Pak de tekst-payload uit een 'a. <tekst>'- of 'a) <tekst>'-paragraph."""
    m = MC_OPTIE.match(paragraph)
    if not m:
        return None
    return m.group(2).strip()


def _verzamel_opties(body: list[str]) -> list[str]:
    """Detecteer MC-opties / sub-stellingen in een sub-blok-body.

    Een 'optie' is een paragraph die start met `a. ` of `a) ` of als
    PDF-artefact met `A. a. ` (dubbele prefix), of een al-gestripte
    optie-tekst (geabsorbeerd via _absorbeer_volgende_opties).
    """
    opties: list[str] = []
    for p in body:
        tekst = _extract_optie_uit_dubbel(p) or _extract_optie_uit_kleinletter(p) or p.strip()
        if tekst:
            opties.append(tekst)
    return opties


def _absorbeer_volgende_opties(blokken: list[dict]) -> list[dict]:
    """Detecteer alfabetische A→B→C→D-sequenties als opties van voorgaand blok.

    PDF-extract heeft vaak: een hoofdvraag (B.) gevolgd door 4 lange j/f-stellingen
    of MC-opties die elk OPNIEUW ge-prefixed zijn met A./B./C./D. door de extractor.
    De heuristiek: 3+ consecutieve blokken met letters A,B,C,D... in sequentie →
    opties van het vorige blok.
    """
    nieuwe: list[dict] = []
    i = 0
    while i < len(blokken):
        b = blokken[i]
        # Kijk vooruit voor een opties-sequentie
        opties: list[str] = []
        for j in range(i + 1, len(blokken)):
            kandidaat = blokken[j]
            verwachte_letter = chr(ord('A') + j - i - 1)
            if kandidaat["letter"] != verwachte_letter:
                break
            # Geen body → enkelvoudige optie. Body → mogelijk eigen sub-vraag, stop.
            if kandidaat["body"]:
                break
            opties.append(kandidaat["stem"])

        if len(opties) >= 3:
            # Absorbeer
            b = {**b, "body": b["body"] + opties}
            nieuwe.append(b)
            i += 1 + len(opties)
        else:
            nieuwe.append(b)
            i += 1

    return nieuwe


def splits_in_sub_vragen(vraagtekst: str) -> list[SubVraag]:
    """Splits een genormaliseerde vraagtekst in sub-vragen.

    Args:
        vraagtekst: genormaliseerde tekst (paragraphs gescheiden door `\\n\\n`)

    Returns:
        Lijst van sub-vragen, lege lijst als de heuristiek geen duidelijke
        sub-structuur detecteert.
    """
    if not vraagtekst:
        return []

    paragraphs = [p.strip() for p in vraagtekst.split("\n\n") if p.strip()]
    if not paragraphs:
        return []

    # Splits in niveau-1-blokken
    blokken: list[dict] = []
    huidig: dict | None = None
    voor_first: list[str] = []  # paragraphs vóór de eerste niveau-1-marker (= intro/context)

    for p in paragraphs:
        if _is_dubbel_prefix(p):
            # PDF-artefact: MC-optie, geen nieuwe sub-vraag. Voeg toe aan huidige body.
            if huidig is not None:
                huidig["body"].append(p)
            continue
        m = NIVEAU1_MARKER.match(p)
        if m:
            if huidig:
                blokken.append(huidig)
            huidig = {"letter": m.group(1), "stem": m.group(2).strip(), "body": []}
        elif huidig:
            huidig["body"].append(p)
        else:
            voor_first.append(p)
    if huidig:
        blokken.append(huidig)

    if len(blokken) < 2:
        return []

    # Post-process: absorbeer alfabetische optie-sequenties.
    # PDF-extract levert vaak "B. <hoofdvraag> / A.<optie1> B.<optie2> C.<optie3> D.<optie4>"
    # Detecteer: 3+ consecutive blokken met letters A→B→C→D... → opties van voorgaand blok.
    blokken = _absorbeer_volgende_opties(blokken)
    if len(blokken) < 2:
        return []

    # Per blok: type detecteren en sub_vraag-records bouwen
    sub_vragen: list[SubVraag] = []
    context_intro = " ".join(voor_first).strip()

    for blok in blokken:
        opties = _verzamel_opties(blok["body"])
        is_jf = bool(JF_KEYWORDS.search(blok["stem"]))

        if is_jf and opties:
            # j/f-blok: één sub-vraag met meerdere stellingen
            sub_vragen.append(SubVraag(
                sub_id=blok["letter"],
                type="j_f_set",
                stem=blok["stem"],
                context=context_intro,
                opties=[],
                stellingen=opties,
            ))
        elif opties:
            # MC-vraag: één sub-vraag met opties
            sub_vragen.append(SubVraag(
                sub_id=blok["letter"],
                type="mc",
                stem=blok["stem"],
                context=context_intro,
                opties=opties,
                stellingen=[],
            ))
        else:
            # Open vraag of onbekende structuur
            stem = blok["stem"]
            if blok["body"]:
                stem = stem + "\n\n" + "\n\n".join(blok["body"])
            sub_vragen.append(SubVraag(
                sub_id=blok["letter"],
                type="open",
                stem=stem,
                context=context_intro,
                opties=[],
                stellingen=[],
            ))

    return sub_vragen
