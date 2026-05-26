"""Tests voor examenfocus_v4_binding.py — TDD-suite.

Dekt:
- laad_vragen_voor_po: filter op programmaonderdeel_ids, sortering, meerdere PO's
- render_vraag_callout: nested collapsible callout-structuur
- Idempotentie van render
- Skip-paden voor PO's zonder vragen (1.8, 2.1, 2.7)
- Parametrized smoke-test over alle 16 vertegenwoordigde PO's
"""
from __future__ import annotations

import re

import pytest

from tools.leermateriaal.lib.examenfocus_v4_binding import (
    laad_vragen_voor_po,
    render_vraag_callout,
)

# ---------------------------------------------------------------------------
# laad_vragen_voor_po — filter + sortering
# ---------------------------------------------------------------------------


def test_po_17_levert_minstens_15_vragen():
    vragen = laad_vragen_voor_po("1.7")
    assert len(vragen) >= 15, f"Verwacht ≥15 vragen voor PO 1.7, kreeg {len(vragen)}"


def test_po_30_bevat_vraag_2003_bibf_vrI2():
    """Dubbel-PO-vraag (2.6 + 3.0) moet in PO 3.0-filter zitten."""
    vragen = laad_vragen_voor_po("3.0")
    vraag_ids = [v["vraag_id"] for v in vragen]
    assert "2003-bibf-vrI2" in vraag_ids, (
        f"Verwacht 2003-bibf-vrI2 in PO 3.0, gevonden ids: {vraag_ids[:5]}..."
    )


def test_vraag_met_2_pos_komt_in_beide_filters():
    """2013-2-vr19 heeft PO's [1.6, 3.0] — moet in beide filters zitten."""
    vragen_16 = laad_vragen_voor_po("1.6")
    vragen_30 = laad_vragen_voor_po("3.0")
    ids_16 = {v["vraag_id"] for v in vragen_16}
    ids_30 = {v["vraag_id"] for v in vragen_30}
    assert "2013-2-vr19" in ids_16, "2013-2-vr19 niet gevonden in PO 1.6"
    assert "2013-2-vr19" in ids_30, "2013-2-vr19 niet gevonden in PO 3.0"


def test_sortering_is_deterministisch():
    """Twee calls geven byte-identieke lijst (gesorteerd op examen_id, vraag_id)."""
    vragen_a = laad_vragen_voor_po("1.1")
    vragen_b = laad_vragen_voor_po("1.1")
    ids_a = [v["vraag_id"] for v in vragen_a]
    ids_b = [v["vraag_id"] for v in vragen_b]
    assert ids_a == ids_b


def test_sortering_op_examen_id_dan_vraag_id():
    """Vragen zijn gesorteerd op (examen_id, vraag_id)."""
    vragen = laad_vragen_voor_po("1.1")
    sleutels = [(v["examen_id"], v["vraag_id"]) for v in vragen]
    assert sleutels == sorted(sleutels), "Vragen zijn niet gesorteerd op (examen_id, vraag_id)"


def test_vraag_dict_heeft_vereiste_velden():
    """Return-dicts bevatten de velden die de template nodig heeft."""
    vragen = laad_vragen_voor_po("1.7")
    assert len(vragen) > 0
    v = vragen[0]
    for veld in ("vraag_id", "examen_id", "onderwerp", "herkomst_label", "context_blokken", "deelvragen", "antwoord"):
        assert veld in v, f"Veld '{veld}' ontbreekt in vraag-dict"


# ---------------------------------------------------------------------------
# Skip-paden: PO's zonder vragen
# ---------------------------------------------------------------------------


def test_po_18_levert_lege_lijst():
    """PO 1.8 heeft geen geclassificeerde vragen — lege lijst verwacht."""
    assert laad_vragen_voor_po("1.8") == []


def test_po_21_levert_lege_lijst():
    assert laad_vragen_voor_po("2.1") == []


def test_po_27_levert_lege_lijst():
    assert laad_vragen_voor_po("2.7") == []


def test_onbestaande_po_levert_lege_lijst():
    assert laad_vragen_voor_po("9.9") == []


# ---------------------------------------------------------------------------
# Parametrized smoke-test over alle 16 vertegenwoordigde PO's
# ---------------------------------------------------------------------------

# PO's met minstens 1 vraag per bovenstaande telling
_PO_MET_VRAGEN = [
    "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.9",
    "2.2", "2.3", "2.4", "2.5", "2.6", "2.8", "3.0", "4.0",
]

# PO's met 0 vragen → lege lijst
_PO_ZONDER_VRAGEN = ["1.8", "2.1", "2.7"]


@pytest.mark.parametrize("po_code", _PO_MET_VRAGEN)
def test_po_heeft_minstens_een_vraag(po_code: str):
    vragen = laad_vragen_voor_po(po_code)
    assert len(vragen) >= 1, f"PO {po_code}: verwacht ≥1 vraag, kreeg 0"


@pytest.mark.parametrize("po_code", _PO_ZONDER_VRAGEN)
def test_po_zonder_vragen(po_code: str):
    assert laad_vragen_voor_po(po_code) == [], f"PO {po_code}: verwacht lege lijst"


# ---------------------------------------------------------------------------
# render_vraag_callout — nested collapsible callout structuur
# ---------------------------------------------------------------------------


def _vraag_17() -> dict:
    """Haal eerste PO 1.7-vraag op voor render-tests."""
    vragen = laad_vragen_voor_po("1.7")
    assert vragen, "Geen PO 1.7-vragen beschikbaar"
    return vragen[0]


def test_render_produceert_question_callout():
    vraag = _vraag_17()
    md = render_vraag_callout(vraag)
    assert "> [!question]-" in md, "Outer [!question]- callout ontbreekt"


def test_render_produceert_success_callout():
    """Elk antwoord-blok moet een inner [!success]- callout bevatten."""
    vraag = _vraag_17()
    md = render_vraag_callout(vraag)
    assert "[!success]-" in md, "Inner [!success]- antwoord-callout ontbreekt"


def test_render_nested_prefix():
    """Inner antwoord-callout moet correct genest zijn (>> prefix)."""
    vraag = _vraag_17()
    md = render_vraag_callout(vraag)
    # Nested callout vereist minstens één lijn met "> > [!success]"
    assert re.search(r"^> >", md, re.MULTILINE), (
        "Geneste callout-prefix '> >' ontbreekt in output"
    )


def test_render_herkomst_aanwezig():
    """Herkomst-regel (examen_id) moet in de callout-body staan."""
    vragen = laad_vragen_voor_po("1.7")
    assert vragen
    vraag = vragen[0]
    md = render_vraag_callout(vraag)
    examen_id = vraag["examen_id"]
    assert examen_id in md, f"examen_id '{examen_id}' niet gevonden in render-output"


def test_render_fraude_casus_vr13():
    """vr13 (fraude-casus, 7 alineas) moet volledig gerenderd zijn zonder afkap."""
    vragen = laad_vragen_voor_po("1.7")
    vr13 = next((v for v in vragen if v["vraag_id"] == "2013-1-vr13"), None)
    assert vr13 is not None, "2013-1-vr13 niet gevonden in PO 1.7-vragen"
    md = render_vraag_callout(vr13)
    # Controleer dat de casus-tekst aanwezig is (begin van eerste alinea)
    assert "NV SLA-BAK" in md, "Casus-tekst 'NV SLA-BAK' niet aanwezig in render"
    # Controleer dat de laatste alinea ook aanwezig is
    assert "dubbel had betaald" in md, "Laatste alinea van casus-tekst ontbreekt"


def test_render_collapsed_by_default():
    """Outer callout moet collapsed zijn (eindigt op '-')."""
    vraag = _vraag_17()
    md = render_vraag_callout(vraag)
    # Eerste lijn moet zijn: > [!question]- ...
    eerste_lijn = md.splitlines()[0]
    assert "[!question]-" in eerste_lijn, f"Outer callout niet collapsed: {eerste_lijn}"


def test_render_idempotent():
    """Tweede call met zelfde input geeft byte-identieke output."""
    vraag = _vraag_17()
    md_a = render_vraag_callout(vraag)
    md_b = render_vraag_callout(vraag)
    assert md_a == md_b, "render_vraag_callout is niet idempotent"


def test_render_onderwerp_in_titel():
    """Vraag-onderwerp moet in de callout-titel staan."""
    vragen = laad_vragen_voor_po("1.7")
    assert vragen
    vraag = vragen[0]
    md = render_vraag_callout(vraag)
    eerste_lijn = md.splitlines()[0]
    # Onderwerp staat achter > [!question]- in de eerste lijn
    assert vraag["onderwerp"] in eerste_lijn, (
        f"Onderwerp '{vraag['onderwerp']}' niet in callout-titel: {eerste_lijn}"
    )


def test_render_mc_opties_aanwezig():
    """MC-vraag moet opties tonen in het callout-body."""
    # Zoek een mc_keuze-vraag
    for po in _PO_MET_VRAGEN:
        vragen = laad_vragen_voor_po(po)
        for vraag in vragen:
            for dv in vraag.get("deelvragen", []):
                if dv.get("vraagtype") == "mc_keuze" and dv.get("opties"):
                    md = render_vraag_callout(vraag)
                    # MC-optie-id zoals "a)" of "A)" moet in de output staan
                    eerste_optie_id = dv["opties"][0]["id"]
                    # Markdown-rendering: `**{id}**` (zonder `)`-haakje na ADR-032
                    # styling; haakje weggehaald omdat letter als badge wordt
                    # gerendered).
                    assert (
                        f"**{eerste_optie_id}**" in md
                        or f"**{eerste_optie_id})**" in md
                    ), f"MC-optie '{eerste_optie_id}' niet in output"
                    return
    pytest.skip("Geen mc_keuze-vraag met opties gevonden in testdata")


def test_render_alle_po_vragen_valid_markdown():
    """Smoke-test: render elke vraag voor PO 1.7 en controleer minimale structuur."""
    vragen = laad_vragen_voor_po("1.7")
    for vraag in vragen:
        md = render_vraag_callout(vraag)
        assert "> [!question]-" in md, f"[!question]- ontbreekt voor {vraag['vraag_id']}"
        assert md.strip(), f"Lege output voor {vraag['vraag_id']}"
