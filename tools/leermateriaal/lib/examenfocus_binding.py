"""Examenfocus-binding voor minicursus-render (ADR-009 §6 + §7).

Resolve welke `examenfocus--*.json` en `voorbeeldvraag--*.json` (synthetisch)
toegepast moeten worden in de eind-rubriek "Examenfocus" van een minicursus.

Eenrichtingsverkeer (ADR-009 §6): concept-records linken niet terug naar
examenfocus. Render-laag scant alle examenfocus-objecten en filtert op
`concept_ids ⊆ records van PO X`. Idem voor voorbeeldvraag-synthetisch via
`gebaseerd_op_concepten`.

Confidence-afleiding (ADR-009 §7 render-zijde): examenfocus → ⚖️ via tier
A/B/C in `voorbeeldvragen[]`. Synthetisch → altijd 🤖.

Folders kunnen ontbreken — module returnt lege lijsten als data niet bestaat.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).resolve().parent.parent.parent.parent
EXAM_FOCUS_DIR = ROOT / "data" / "exam_focus"
VOORBEELDVRAGEN_SYNTH_DIR = ROOT / "data" / "voorbeeldvragen-synthetisch"
EXAMEN_VRAGEN_DIR = ROOT / "data" / "programma" / "examen_vragen"

TIER_VOLGORDE = {"A": 0, "B": 1, "C": 2}


class ExamenfocusVraag(TypedDict):
    """Eén voorbeeldvraag binnen een examenfocus-groep."""
    examen_id: str
    vraag_id: str
    vraag_nr: str
    tier: str
    vraag_tekst: str
    antwoord_motivering: str | None


class ExamenfocusGroep(TypedDict):
    """Eén examenfocus-object — focus-intro + één-of-meer voorbeeldvragen."""
    id: str
    naam: str
    wat_getoetst_wordt: str
    is_bootstrap: bool
    vragen: list[ExamenfocusVraag]


class VoorbeeldvraagCallout(TypedDict):
    """Render-data voor één synthetische voorbeeldvraag (🤖)."""
    id: str
    vraag_tekst: str
    voorbeeld_oplossing: str
    redenering: str
    patroon_naam: str | None


def _laad_examenvraag(examen_id: str, vraag_id: str) -> dict | None:
    """Lookup van vraag-detail in data/programma/examen_vragen/<examen_id>.json.

    Schema: top-level dict met `vragen[]`; per vraag een `id` (= "2024-1-vr7"),
    `vraagtekst`, `antwoord_motivering`, etc.
    """
    pad = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
    if not pad.exists():
        return None
    try:
        examen = json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    vragen = examen.get("vragen") if isinstance(examen, dict) else examen
    for v in vragen or []:
        if v.get("id") == vraag_id:
            return v
    return None


def laad_examenfocus_groepen(records_van_po: set[str]) -> list[ExamenfocusGroep]:
    """Vind alle examenfocus-groepen voor records van een PO.

    Filter: `examenfocus.concept_ids ⊆ records_van_po`. Returnt één groep per
    examenfocus-object met alle voorbeeldvragen erin (tier-gesorteerd).
    Groepen zelf zijn gesorteerd: niet-bootstrap eerst (echte curatie), dan
    bootstrap-stubs; binnen elke set op laagste-tier-vraag.

    Returnt lege lijst als `data/exam_focus/` niet bestaat of leeg is.
    """
    if not EXAM_FOCUS_DIR.exists():
        return []

    groepen: list[ExamenfocusGroep] = []
    for pad in sorted(EXAM_FOCUS_DIR.glob("examenfocus--*.json")):
        try:
            ef = json.loads(pad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        concept_ids = set(ef.get("concept_ids", []) or [])
        if not concept_ids or not concept_ids.issubset(records_van_po):
            continue

        curator = (ef.get("_provenance") or {}).get("curator", "")
        is_bootstrap = curator == "bootstrap"

        vragen: list[ExamenfocusVraag] = []
        for vv in ef.get("voorbeeldvragen", []) or []:
            examen_id = vv.get("examen_id", "")
            vraag_id = vv.get("vraag_id", "")
            vraag_detail = _laad_examenvraag(examen_id, vraag_id)
            vragen.append(ExamenfocusVraag(
                examen_id=examen_id,
                vraag_id=vraag_id,
                vraag_nr=vv.get("vraag_nr", ""),
                tier=vv.get("tier", "C"),
                vraag_tekst=(vraag_detail or {}).get("vraagtekst", ""),
                antwoord_motivering=(vraag_detail or {}).get("antwoord_motivering"),
            ))
        vragen.sort(key=lambda v: (TIER_VOLGORDE.get(v["tier"], 9), v["examen_id"], v["vraag_id"]))

        groepen.append(ExamenfocusGroep(
            id=ef.get("id", ""),
            naam=ef.get("naam") or ef.get("id", ""),
            wat_getoetst_wordt=ef.get("wat_getoetst_wordt", "") if not is_bootstrap else "",
            is_bootstrap=is_bootstrap,
            vragen=vragen,
        ))

    # Niet-bootstrap eerst (echte curatie), dan bootstrap; binnen elke groep
    # op laagste tier-vraag (= best representative)
    def _sortsleutel(g: ExamenfocusGroep) -> tuple:
        beste_tier = min((TIER_VOLGORDE.get(v["tier"], 9) for v in g["vragen"]), default=9)
        return (g["is_bootstrap"], beste_tier, g["naam"])

    groepen.sort(key=_sortsleutel)
    return groepen


def laad_voorbeeldvragen_synthetisch(records_van_po: set[str]) -> list[VoorbeeldvraagCallout]:
    """Vind alle synthetische voorbeeldvragen voor records van een PO.

    Filter: `gebaseerd_op_concepten ⊆ records_van_po`. Sorteer alfabetisch op
    patroon-naam (= grouping per pedagogisch patroon).

    Returnt lege lijst als `data/voorbeeldvragen-synthetisch/` niet bestaat.
    """
    if not VOORBEELDVRAGEN_SYNTH_DIR.exists():
        return []

    callouts: list[VoorbeeldvraagCallout] = []
    for pad in sorted(VOORBEELDVRAGEN_SYNTH_DIR.glob("voorbeeldvraag--*.json")):
        try:
            vv = json.loads(pad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        concepten = set(vv.get("gebaseerd_op_concepten", []) or [])
        if not concepten or not concepten.issubset(records_van_po):
            continue

        callouts.append(VoorbeeldvraagCallout(
            id=vv.get("id", pad.stem),
            vraag_tekst=vv.get("vraag_tekst", ""),
            voorbeeld_oplossing=vv.get("voorbeeld_oplossing", ""),
            redenering=vv.get("redenering", ""),
            patroon_naam=vv.get("gebaseerd_op_patroon"),
        ))

    callouts.sort(key=lambda c: (c["patroon_naam"] or "", c["id"]))
    return callouts
