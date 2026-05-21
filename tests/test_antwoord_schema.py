"""Schema-validatie voor _antwoorden/<examen>/<vraag-id>.json (ADR-024 §5, v1.1).

Tests valideren dat het antwoord-artefact de v1.1-structuur respecteert,
met coupling per deelvraag via `id` en primair antwoord per vraagtype.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
POC_SUBSET = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_poc_subset.json"
INTERP_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"
ANTW_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_antwoorden"

SCHEMA_VERSIE_EXPECTED = "1.1"
VALID_STATUS = {"beantwoord", "wacht_op_vraag_generatie", "hard_blocked"}
VALID_BLOK_TYPES = {
    "motivatie", "boeking", "berekening", "definitie", "procedure",
    "tabel", "opsomming", "conclusie", "grondslag",
}
VALID_CONFIDENCE = {"grounded", "inferred"}
MOTIVERINGSBLOK_TYPES = {"motivatie", "grondslag", "conclusie"}
PRIMAIR_OPEN_BLOK_TYPES = {
    "motivatie", "boeking", "berekening", "definitie",
    "procedure", "tabel", "opsomming", "conclusie",
}
VERPLICHTE_TOP_VELDEN = {
    "schema_versie", "examen_id", "vraag_id", "antwoord_datum",
    "vraag_antwoorden",
}


def _laad_subset() -> list[dict]:
    return json.loads(POC_SUBSET.read_text(encoding="utf-8"))["selectie"]


def _antw_path(entry: dict) -> Path:
    return ANTW_DIR / entry["examen_id"] / f"{entry['vraag_id']}.json"


def _interp_path(entry: dict) -> Path:
    return INTERP_DIR / entry["examen_id"] / f"{entry['vraag_id']}.json"


def _load(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_antwoord_bestaat(entry):
    path = _antw_path(entry)
    assert path.exists(), f"Antwoord ontbreekt: {path}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_antwoord_is_geldige_json(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    assert isinstance(data, dict)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_schema_versie_1_1(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    assert data.get("schema_versie") == SCHEMA_VERSIE_EXPECTED


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_verplichte_top_velden(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    missing = VERPLICHTE_TOP_VELDEN - set(data.keys())
    assert not missing, f"{entry['vraag_id']}: ontbreekt {missing}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_metadata_matched(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    assert data["examen_id"] == entry["examen_id"]
    assert data["vraag_id"] == entry["vraag_id"]


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_alle_deelvragen_beantwoord(entry):
    """vraag_antwoorden[] bevat exact één entry per interpretatie.vragen[]."""
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_ids = sorted(v["id"] for v in interp["vragen"])
    antw_ids = sorted(va["id"] for va in antw["vraag_antwoorden"])
    assert interp_ids == antw_ids, (
        f"{entry['vraag_id']}: interp-ids {interp_ids} vs antwoord-ids {antw_ids}"
    )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_status_enum(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    for va in data["vraag_antwoorden"]:
        assert "antwoord_status" in va
        assert va["antwoord_status"] in VALID_STATUS


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_blokken_typed_met_confidence(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    for va in data["vraag_antwoorden"]:
        for b in va.get("blokken", []):
            assert "type" in b and b["type"] in VALID_BLOK_TYPES, (
                f"{entry['vraag_id']} deelvraag {va['id']}: ongeldig blok-type {b.get('type')!r}"
            )
            assert "confidence" in b and b["confidence"] in VALID_CONFIDENCE
            assert "bron_refs" in b and isinstance(b["bron_refs"], list)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_mc_keuze_primair_antwoord(entry):
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_by_id = {v["id"]: v for v in interp["vragen"]}
    for va in antw["vraag_antwoorden"]:
        iv = interp_by_id.get(va["id"])
        if iv is None or iv["vraagtype"] != "mc_keuze":
            continue
        if va["antwoord_status"] != "beantwoord":
            continue
        gekozen = va.get("gekozen_optie_id")
        assert isinstance(gekozen, str) and gekozen, (
            f"{entry['vraag_id']} deelvraag {va['id']}: mc_keuze beantwoord zonder gekozen_optie_id"
        )
        opt_ids = {o["id"] for o in iv.get("opties", [])}
        assert gekozen in opt_ids, (
            f"{entry['vraag_id']} deelvraag {va['id']}: gekozen_optie_id {gekozen} niet in opties"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_juist_fout_primair_antwoord(entry):
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_by_id = {v["id"]: v for v in interp["vragen"]}
    for va in antw["vraag_antwoorden"]:
        iv = interp_by_id.get(va["id"])
        if iv is None or iv["vraagtype"] != "juist_fout":
            continue
        if va["antwoord_status"] != "beantwoord":
            continue
        assert "oordeel" in va, (
            f"{entry['vraag_id']} deelvraag {va['id']}: juist_fout beantwoord zonder oordeel"
        )
        assert isinstance(va["oordeel"], bool)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_open_heeft_inhoudblok(entry):
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_by_id = {v["id"]: v for v in interp["vragen"]}
    for va in antw["vraag_antwoorden"]:
        iv = interp_by_id.get(va["id"])
        if iv is None or iv["vraagtype"] != "open":
            continue
        if va["antwoord_status"] != "beantwoord":
            continue
        types = {b.get("type") for b in va.get("blokken", [])}
        assert types & PRIMAIR_OPEN_BLOK_TYPES, (
            f"{entry['vraag_id']} deelvraag {va['id']}: open zonder primair-content blok"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_motivatie_verwacht_levert_motivering(entry):
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_by_id = {v["id"]: v for v in interp["vragen"]}
    for va in antw["vraag_antwoorden"]:
        iv = interp_by_id.get(va["id"])
        if iv is None or not iv.get("motivatie_verwacht"):
            continue
        if va["antwoord_status"] != "beantwoord":
            continue
        types = {b.get("type") for b in va.get("blokken", [])}
        assert types & MOTIVERINGSBLOK_TYPES, (
            f"{entry['vraag_id']} deelvraag {va['id']}: motivatie_verwacht=true maar geen motivatie/grondslag/conclusie-blok"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_topic_only_wacht_op_generatie(entry):
    interp = _load(_interp_path(entry))
    antw = _load(_antw_path(entry))
    if interp is None or antw is None:
        pytest.skip("artefacten ontbreken")
    interp_by_id = {v["id"]: v for v in interp["vragen"]}
    for va in antw["vraag_antwoorden"]:
        iv = interp_by_id.get(va["id"])
        if iv is None or iv["volledigheid"] != "topic_only":
            continue
        assert va["antwoord_status"] == "wacht_op_vraag_generatie", (
            f"{entry['vraag_id']} deelvraag {va['id']}: topic_only met status {va['antwoord_status']}"
        )
        assert va.get("blokken", []) == [], (
            f"{entry['vraag_id']} deelvraag {va['id']}: topic_only met blokken"
        )
        assert "gekozen_optie_id" not in va
        assert "oordeel" not in va


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_hard_block_consistent(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    for va in data["vraag_antwoorden"]:
        if va["antwoord_status"] != "hard_blocked":
            continue
        assert va.get("blokken", []) == []
        gap = va.get("record_gap_report")
        assert isinstance(gap, dict)
        assert gap.get("niveau") in {"a", "b", "c"}
        assert isinstance(gap.get("type"), str)
        assert isinstance(gap.get("beschrijving"), str)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_grounded_heeft_bron_refs(entry):
    data = _load(_antw_path(entry))
    if data is None:
        pytest.skip("artefact ontbreekt")
    for va in data["vraag_antwoorden"]:
        for b in va.get("blokken", []):
            if b.get("confidence") == "grounded":
                assert b.get("bron_refs"), (
                    f"{entry['vraag_id']} deelvraag {va['id']}: grounded blok zonder bron_refs"
                )
