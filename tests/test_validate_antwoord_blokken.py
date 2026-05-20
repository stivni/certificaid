"""Tests voor `validate_antwoord_blokken_v1.py` (ADR-023)."""
from __future__ import annotations

from tools.examen import validate_antwoord_blokken_v1 as V


class TestValideerBlok:
    def test_motivatie_ok(self):
        f = V.valideer_blok({"type": "motivatie", "inhoud": "X"}, "p")
        assert f == []

    def test_motivatie_geen_inhoud(self):
        f = V.valideer_blok({"type": "motivatie"}, "p")
        assert any("inhoud" in x for x in f)

    def test_ongeldig_type(self):
        f = V.valideer_blok({"type": "onbekend"}, "p")
        assert any("ongeldig" in x for x in f)

    def test_boeking_zijde_invalid(self):
        b = {
            "type": "boeking",
            "regels": [{"zijde": "X", "rekening": "15", "naam": "K", "bedrag": 100.0}],
        }
        f = V.valideer_blok(b, "p")
        assert any("zijde" in x for x in f)

    def test_boeking_ok(self):
        b = {
            "type": "boeking",
            "regels": [{"zijde": "D", "rekening": "15", "naam": "K", "bedrag": 100.0}],
        }
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_definitie_ok(self):
        b = {"type": "definitie", "lemma": "X", "definitie_zin": "X is Y"}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_definitie_zonder_lemma(self):
        b = {"type": "definitie", "definitie_zin": "X is Y"}
        f = V.valideer_blok(b, "p")
        assert any("lemma" in x for x in f)

    def test_opsomming_ok(self):
        b = {"type": "opsomming", "items": [{"lemma": "A"}, {"lemma": "B"}]}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_opsomming_leeg(self):
        b = {"type": "opsomming", "items": []}
        f = V.valideer_blok(b, "p")
        assert any("niet-lege" in x for x in f)

    def test_procedure_ok(self):
        b = {"type": "procedure", "stappen": [{"nummer": 1, "beschrijving": "X"}]}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_tabel_ok(self):
        b = {"type": "tabel", "headers": ["A", "B"], "rows": [["1", "2"]]}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_grondslag_ok(self):
        b = {"type": "grondslag", "bronnen": ["KB WVV art. 3:50"]}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_grondslag_leeg(self):
        b = {"type": "grondslag", "bronnen": []}
        f = V.valideer_blok(b, "p")
        assert any("bronnen" in x for x in f)

    def test_confidence_invalid(self):
        b = {"type": "motivatie", "inhoud": "X", "confidence": "vast"}
        f = V.valideer_blok(b, "p")
        assert any("confidence" in x for x in f)

    def test_confidence_grounded_ok(self):
        b = {"type": "motivatie", "inhoud": "X", "confidence": "grounded"}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_conclusie_ok(self):
        b = {"type": "conclusie", "inhoud": "Optie 3"}
        f = V.valideer_blok(b, "p")
        assert f == []

    def test_berekening_minstens_formule_of_componenten(self):
        b = {"type": "berekening"}
        f = V.valideer_blok(b, "p")
        assert any("formule" in x or "componenten" in x for x in f)

    def test_berekening_met_formule(self):
        b = {"type": "berekening", "formule": "a + b"}
        f = V.valideer_blok(b, "p")
        assert f == []
