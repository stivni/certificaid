"""Tests voor de v2-schema-validator (tools.examen.validate_examen_v2)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.examen import validate_examen_v2 as V


def _schrijf_examen(tmp_path: Path, doc: dict) -> Path:
    p = tmp_path / "test.json"
    p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return p


def _basis_doc(**overrides) -> dict:
    doc = {
        "examen_id": "test",
        "schema_versie": "2.0",
        "vragen": [
            {
                "id": "test-vr1",
                "vraagtekst": "Wat is X?",
                "vraagtekst_blokken": [{"type": "tekst", "inhoud": "Wat is X?"}],
            }
        ],
    }
    doc.update(overrides)
    return doc


class TestValideerBlok:
    def test_geldig_tekst(self):
        f = V.valideer_blok({"type": "tekst", "inhoud": "hi"}, "test")
        assert f == []

    def test_geldig_tabel_met_headers(self):
        b = {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]}
        assert V.valideer_blok(b, "test") == []

    def test_ongeldig_type(self):
        f = V.valideer_blok({"type": "image", "inhoud": "x"}, "test")
        assert any("ongeldig blok-type" in x for x in f)

    def test_tabel_uneven_rijen(self):
        b = {"type": "tabel", "rows": [["a", "b"], ["c"]]}
        f = V.valideer_blok(b, "test")
        assert any("niet even lang" in x for x in f)

    def test_headers_mismatch_columns(self):
        b = {"type": "tabel", "headers": ["A"], "rows": [["1", "2"]]}
        f = V.valideer_blok(b, "test")
        assert any("header-lengte" in x for x in f)

    def test_tekst_zonder_inhoud(self):
        f = V.valideer_blok({"type": "tekst"}, "test")
        assert any("'inhoud'" in x for x in f)

    def test_tabel_rows_geen_list(self):
        f = V.valideer_blok({"type": "tabel", "rows": "nope"}, "test")
        assert any("geen list" in x for x in f)

    def test_tabel_cel_geen_string(self):
        b = {"type": "tabel", "rows": [["a", 1]]}
        f = V.valideer_blok(b, "test")
        assert any("geen string" in x for x in f)


class TestValideerExamen:
    def test_geldig_doc(self, tmp_path):
        p = _schrijf_examen(tmp_path, _basis_doc())
        assert V.valideer_examen(p) == []

    def test_verkeerde_schema_versie(self, tmp_path):
        p = _schrijf_examen(tmp_path, _basis_doc(schema_versie="1.0"))
        fouten = V.valideer_examen(p)
        assert any("schema_versie" in x for x in fouten)

    def test_vraag_zonder_blokken(self, tmp_path):
        doc = _basis_doc()
        doc["vragen"][0].pop("vraagtekst_blokken")
        p = _schrijf_examen(tmp_path, doc)
        fouten = V.valideer_examen(p)
        assert any("'vraagtekst_blokken' ontbreekt" in x for x in fouten)

    def test_concat_reconstructie_match_modulo_whitespace(self, tmp_path):
        doc = {
            "examen_id": "test",
            "schema_versie": "2.0",
            "vragen": [
                {
                    "id": "t-vr1",
                    "vraagtekst": "Vul   tabel\n\n| A | B |\n|---|---|\n| 1 | 2 |",
                    "vraagtekst_blokken": [
                        {"type": "tekst", "inhoud": "Vul tabel"},
                        {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]},
                    ],
                }
            ],
        }
        p = _schrijf_examen(tmp_path, doc)
        # Concat-mismatch is alleen een warning (stderr), niet een fail
        assert V.valideer_examen(p) == []
