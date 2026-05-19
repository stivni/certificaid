"""Tests voor migratie v2 → v3 (ADR-021 v3.0)."""
from __future__ import annotations

from tools.examen import migrate_to_v3 as M


def _v2_doc(vragen):
    return {
        "examen_id": "test",
        "schema_versie": "2.0",
        "vragen": vragen,
    }


def _v3_doc(vragen):
    return {
        "examen_id": "test",
        "schema_versie": "3.0",
        "vragen": vragen,
    }


class TestMergeV2InV3:
    def test_antwoord_velden_behouden(self):
        v2 = _v2_doc([
            {
                "id": "test-vr1",
                "vraagtekst": "Bereken.",
                "correct_antwoord": "42",
                "antwoord_motivering": "Omdat",
                "antwoord_bron": [{"record": "x.md"}],
                "vraagtekst_blokken": [{"type": "tekst", "inhoud": "Bereken."}],
            }
        ])
        v3 = _v3_doc([
            {
                "id": "test-vr1",
                "vraagtekst": "Bereken.",
                "vraagtekst_blokken": [
                    {"type": "vraag_instructie", "inhoud": "Bereken."}
                ],
            }
        ])
        merged, diff = M.merge_v2_in_v3(v2, v3)
        v3_vr = merged["vragen"][0]
        assert v3_vr["correct_antwoord"] == "42"
        assert v3_vr["antwoord_motivering"] == "Omdat"
        assert v3_vr["antwoord_bron"] == [{"record": "x.md"}]
        assert diff["antwoorden_behouden"] == 1

    def test_classificatie_velden_behouden(self):
        v2 = _v2_doc([
            {
                "id": "vr1",
                "vraagtekst": "x",
                "vak_code_in_pdf": "A",
                "vak_naam_in_pdf": "Algemene boekhouding",
                "themas": ["voorraden"],
                "wets_verwijzingen": ["KB WVV art. 3:42"],
                "vraagtekst_blokken": [],
            }
        ])
        v3 = _v3_doc([{"id": "vr1", "vraagtekst": "x", "vraagtekst_blokken": []}])
        merged, _ = M.merge_v2_in_v3(v2, v3)
        v3_vr = merged["vragen"][0]
        assert v3_vr["vak_code_in_pdf"] == "A"
        assert v3_vr["themas"] == ["voorraden"]
        assert v3_vr["wets_verwijzingen"] == ["KB WVV art. 3:42"]

    def test_adr022_velden_behouden(self):
        v2 = _v2_doc([
            {
                "id": "vr1",
                "vraagtekst": "x",
                "vraag_herkomst": "studocu",
                "vraag_volledigheid": "compleet",
                "vraag_herinterpreteerd": True,
                "mc_opties_gestructureerd": [{"label": "A", "tekst": "X"}],
                "antwoord_hint_in_vraag": "FIFO",
                "vraagtekst_blokken": [],
            }
        ])
        v3 = _v3_doc([{"id": "vr1", "vraagtekst": "x", "vraagtekst_blokken": []}])
        merged, diff = M.merge_v2_in_v3(v2, v3)
        v3_vr = merged["vragen"][0]
        assert v3_vr["vraag_herinterpreteerd"] is True
        assert v3_vr["antwoord_hint_in_vraag"] == "FIFO"
        assert v3_vr["mc_opties_gestructureerd"][0]["label"] == "A"
        assert diff["adr022_behouden"] == 1

    def test_subvragen_label_merge(self):
        v2 = _v2_doc([
            {
                "id": "vr1",
                "vraagtekst": "x",
                "vraagtekst_blokken": [],
                "subvragen": [
                    {"label": "a", "correct_antwoord": "A1", "antwoord_motivering": "M"},
                    {"label": "b", "correct_antwoord": "B1"},
                ],
            }
        ])
        v3 = _v3_doc([
            {
                "id": "vr1",
                "vraagtekst": "x",
                "vraagtekst_blokken": [],
                "subvragen": [{"label": "a"}, {"label": "b"}],
            }
        ])
        merged, _ = M.merge_v2_in_v3(v2, v3)
        sv = merged["vragen"][0]["subvragen"]
        assert sv[0]["correct_antwoord"] == "A1"
        assert sv[0]["antwoord_motivering"] == "M"
        assert sv[1]["correct_antwoord"] == "B1"

    def test_id_verlies_in_diff(self):
        v2 = _v2_doc([
            {"id": "vr1", "vraagtekst": "x", "vraagtekst_blokken": []},
            {"id": "vr2", "vraagtekst": "y", "correct_antwoord": "A",
             "vraagtekst_blokken": []},
        ])
        v3 = _v3_doc([{"id": "vr1", "vraagtekst": "x", "vraagtekst_blokken": []}])
        merged, diff = M.merge_v2_in_v3(v2, v3)
        assert "vr2" in diff["verloren_ids_uit_v2"]
        assert diff["v2_met_antwoord"] == 1
        assert diff["antwoorden_behouden"] == 0

    def test_gap_report_behouden(self):
        v2 = _v2_doc([
            {
                "id": "vr1",
                "vraagtekst": "x",
                "record_gap_report": {"type": "vraagtekst_onduidelijk"},
                "vraagtekst_blokken": [],
            }
        ])
        v3 = _v3_doc([{"id": "vr1", "vraagtekst": "x", "vraagtekst_blokken": []}])
        merged, diff = M.merge_v2_in_v3(v2, v3)
        assert merged["vragen"][0]["record_gap_report"] == {
            "type": "vraagtekst_onduidelijk"
        }
        assert diff["gap_reports_behouden"] == 1
