"""Tests voor de v3-schema-validator (tools.examen.validate_examen_v3)."""
from __future__ import annotations

import json
from pathlib import Path

from tools.examen import validate_examen_v3 as V


def _schrijf_examen(tmp_path: Path, doc: dict) -> Path:
    p = tmp_path / "test.json"
    p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return p


def _basis_doc(**overrides) -> dict:
    doc = {
        "examen_id": "test",
        "schema_versie": "3.0",
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


class TestValideerBlokBasis:
    def test_geldig_tekst(self):
        assert V.valideer_blok({"type": "tekst", "inhoud": "hi"}, "test") == []

    def test_ongeldig_type(self):
        f = V.valideer_blok({"type": "image", "inhoud": "x"}, "test")
        assert any("ongeldig blok-type" in x for x in f)

    def test_tekst_mist_inhoud(self):
        f = V.valideer_blok({"type": "tekst"}, "test")
        assert any("mist veld 'inhoud'" in x for x in f)

    def test_blok_geen_dict(self):
        f = V.valideer_blok("nope", "test")
        assert any("geen dict" in x for x in f)


class TestValideerBlokTabel:
    def test_geldig_tabel_met_headers(self):
        b = {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]}
        assert V.valideer_blok(b, "t") == []

    def test_tabel_uneven_rijen(self):
        b = {"type": "tabel", "rows": [["a", "b"], ["c"]]}
        f = V.valideer_blok(b, "t")
        assert any("niet even lang" in x for x in f)

    def test_tabel_headers_mismatch(self):
        b = {"type": "tabel", "headers": ["A"], "rows": [["1", "2"]]}
        f = V.valideer_blok(b, "t")
        assert any("header-lengte" in x for x in f)


class TestValideerBlokV3Typed:
    def test_proef_saldibalans_geldig(self):
        b = {
            "type": "proef_saldibalans",
            "regels": [
                {"rekening": "32", "naam": "X", "zijde": "D", "bedrag": 500.0},
                {"rekening": "34", "naam": "Y", "zijde": "D", "bedrag": 7000.0},
            ],
            "eenheid": "EUR",
        }
        assert V.valideer_blok(b, "t") == []

    def test_proef_saldibalans_mist_zijde(self):
        b = {
            "type": "proef_saldibalans",
            "regels": [{"rekening": "32", "naam": "X", "bedrag": 500.0}],
        }
        f = V.valideer_blok(b, "t")
        assert any("zijde" in x for x in f)

    def test_proef_saldibalans_mist_regels(self):
        b = {"type": "proef_saldibalans"}
        f = V.valideer_blok(b, "t")
        assert any("regels" in x for x in f)

    def test_rekeningstaat_geldig(self):
        b = {
            "type": "rekeningstaat",
            "regels": [{"rekening": "230000", "naam": "Installaties", "bedrag": 32000.0}],
        }
        assert V.valideer_blok(b, "t") == []

    def test_inventaris_geldig(self):
        b = {
            "type": "inventaris",
            "regels": [{"post": "Handelsgoederen", "bedrag": 8500.0}],
        }
        assert V.valideer_blok(b, "t") == []

    def test_marktwaarde_geldig(self):
        b = {"type": "marktwaarde", "post": "Handelsgoederen", "bedrag": 8250.0}
        assert V.valideer_blok(b, "t") == []

    def test_marktwaarde_mist_bedrag(self):
        b = {"type": "marktwaarde", "post": "X"}
        f = V.valideer_blok(b, "t")
        assert any("bedrag" in x for x in f)

    def test_marktwaarde_bedrag_geen_number(self):
        b = {"type": "marktwaarde", "bedrag": "veel"}
        f = V.valideer_blok(b, "t")
        assert any("geen number" in x for x in f)

    def test_aanpassing_geldig(self):
        b = {"type": "aanpassing", "subtype": "afprijzing", "bedrag": 75.0}
        assert V.valideer_blok(b, "t") == []

    def test_casus_context_geldig(self):
        b = {"type": "casus_context", "inhoud": "De BVBA X heeft …"}
        assert V.valideer_blok(b, "t") == []

    def test_vraag_instructie_geldig(self):
        b = {"type": "vraag_instructie", "inhoud": "Geef de boekingen."}
        assert V.valideer_blok(b, "t") == []

    def test_bijlage_geldig(self):
        b = {"type": "bijlage_verwijzing", "beschrijving": "In bijlage de balans"}
        assert V.valideer_blok(b, "t") == []

    def test_bijlage_mist_beschrijving(self):
        b = {"type": "bijlage_verwijzing"}
        f = V.valideer_blok(b, "t")
        assert any("beschrijving" in x for x in f)

    def test_mc_optie_geldig(self):
        b = {"type": "mc_optie", "label": "A", "tekst": "FIFO"}
        assert V.valideer_blok(b, "t") == []

    def test_mc_optie_mist_label(self):
        b = {"type": "mc_optie", "tekst": "X"}
        f = V.valideer_blok(b, "t")
        assert any("label" in x for x in f)


class TestValideerExamen:
    def test_geldig_doc(self, tmp_path):
        p = _schrijf_examen(tmp_path, _basis_doc())
        assert V.valideer_examen(p) == []

    def test_verkeerde_schema_versie(self, tmp_path):
        p = _schrijf_examen(tmp_path, _basis_doc(schema_versie="2.0"))
        fouten = V.valideer_examen(p)
        assert any("schema_versie" in x for x in fouten)

    def test_vraag_zonder_blokken(self, tmp_path):
        doc = _basis_doc()
        doc["vragen"][0].pop("vraagtekst_blokken")
        p = _schrijf_examen(tmp_path, doc)
        fouten = V.valideer_examen(p)
        assert any("'vraagtekst_blokken' ontbreekt" in x for x in fouten)

    def test_subvragen_blokken_gevalideerd(self, tmp_path):
        doc = _basis_doc()
        doc["vragen"][0]["subvragen"] = [
            {"label": "a", "vraagtekst_blokken": [{"type": "ongeldig"}]}
        ]
        p = _schrijf_examen(tmp_path, doc)
        fouten = V.valideer_examen(p)
        assert any("ongeldig blok-type" in x for x in fouten)
