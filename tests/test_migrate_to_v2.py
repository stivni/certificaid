"""Tests voor tools.examen.migrate_to_v2 — antwoord-merge en diff-logica."""
from __future__ import annotations

from tools.examen.migrate_to_v2 import (
    _merge_subvragen,
    merge_v1_in_v2,
)


def _v1_doc():
    return {
        "examen_id": "X",
        "vragen": [
            {
                "id": "X-vr1",
                "vraagtekst": "Oud vraagtekst",
                "correct_antwoord": "antwoord A",
                "antwoord_motivering": "omdat A",
                "antwoord_provenance": {"datum": "2026-05-01"},
                "antwoord_type": "kort",
                "antwoord_confidence": "grounded",
                "antwoord_bron": ["ITAA-LEX"],
                "record_gap_report": None,
                "vraagtekst_normalized_at": "2026-05-01",
                "vak_code_in_pdf": "1.1",
                "vak_naam_in_pdf": "Vak naam",
                "themas": ["thema1"],
                "wets_verwijzingen": ["art. 1"],
                "punten": 5.0,
                "vraagtype": "open",
                "pdf_pagina": 3,
            },
            {
                "id": "X-vr2",
                "vraagtekst": "Tweede oud",
                "correct_antwoord": None,
                "themas": ["thema2"],
            },
        ],
    }


def _v2_doc():
    return {
        "examen_id": "X",
        "schema_versie": "2.0",
        "vragen": [
            {
                "id": "X-vr1",
                "vraagtekst": "Nieuw vraagtekst",
                "vraagtekst_blokken": [{"type": "tekst", "inhoud": "Nieuw vraagtekst"}],
                "correct_antwoord": None,
                "antwoord_motivering": None,
                "vak_code_in_pdf": "andere",
                "themas": [],
                "wets_verwijzingen": [],
                "punten": None,
                "vraagtype": "open",
                "pdf_pagina": 1,
            },
            {
                "id": "X-vr2",
                "vraagtekst": "Tweede nieuw",
                "vraagtekst_blokken": [{"type": "tekst", "inhoud": "Tweede nieuw"}],
                "correct_antwoord": None,
                "themas": [],
            },
        ],
    }


class TestMergeV1InV2:
    def test_antwoord_velden_worden_overgenomen(self):
        v1 = _v1_doc()
        v2 = _v2_doc()
        merged, diff = merge_v1_in_v2(v1, v2)
        vr1 = next(v for v in merged["vragen"] if v["id"] == "X-vr1")
        assert vr1["correct_antwoord"] == "antwoord A"
        assert vr1["antwoord_motivering"] == "omdat A"
        assert vr1["antwoord_provenance"]["datum"] == "2026-05-01"
        assert vr1["antwoord_bron"] == ["ITAA-LEX"]
        assert vr1["vraagtekst_normalized_at"] == "2026-05-01"

    def test_classificatie_overgenomen(self):
        v1 = _v1_doc()
        v2 = _v2_doc()
        merged, _ = merge_v1_in_v2(v1, v2)
        vr1 = next(v for v in merged["vragen"] if v["id"] == "X-vr1")
        assert vr1["vak_code_in_pdf"] == "1.1"
        assert vr1["themas"] == ["thema1"]
        assert vr1["wets_verwijzingen"] == ["art. 1"]
        assert vr1["punten"] == 5.0
        assert vr1["pdf_pagina"] == 3

    def test_vraagtekst_blokken_blijven_v2(self):
        # vraagtekst zelf komt uit v2 (re-extract), niet uit v1
        v1 = _v1_doc()
        v2 = _v2_doc()
        merged, _ = merge_v1_in_v2(v1, v2)
        vr1 = next(v for v in merged["vragen"] if v["id"] == "X-vr1")
        assert vr1["vraagtekst"] == "Nieuw vraagtekst"
        assert vr1["vraagtekst_blokken"] == [{"type": "tekst", "inhoud": "Nieuw vraagtekst"}]

    def test_diff_telt_antwoord_behoud(self):
        v1 = _v1_doc()
        v2 = _v2_doc()
        _, diff = merge_v1_in_v2(v1, v2)
        assert diff["v1_met_antwoord"] == 1
        assert diff["antwoorden_behouden"] == 1
        assert diff["behouden_ids"] == ["X-vr1", "X-vr2"]
        assert diff["verloren_ids_uit_v1"] == []

    def test_id_verlies_detected(self):
        v1 = _v1_doc()
        v2 = _v2_doc()
        # Verwijder vr2 uit v2
        v2["vragen"] = [v for v in v2["vragen"] if v["id"] != "X-vr2"]
        _, diff = merge_v1_in_v2(v1, v2)
        assert "X-vr2" in diff["verloren_ids_uit_v1"]


class TestMergeSubvragen:
    def test_label_match(self):
        v1_sub = [{"label": "a)", "tekst": "a oud", "correct_antwoord": "A"}]
        v2_sub = [{"label": "a)", "tekst": "a nieuw", "correct_antwoord": None}]
        out = _merge_subvragen(v1_sub, v2_sub)
        assert out[0]["correct_antwoord"] == "A"
        assert out[0]["tekst"] == "a nieuw"  # tekst blijft v2

    def test_geen_match_geen_overname(self):
        v1_sub = [{"label": "a)", "correct_antwoord": "A"}]
        v2_sub = [{"label": "b)", "correct_antwoord": None}]
        out = _merge_subvragen(v1_sub, v2_sub)
        assert out[0]["correct_antwoord"] is None
