"""Schema-validatie voor _interpretaties/<examen>/<vraag-id>.json (ADR-024 §3, v1.1).

Tests valideren de output van de vraag-interpretatie-subagent. Per POC-vraag
moet er een interpretatie-artefact zijn dat het v1.1-schema respecteert.

Tests zijn ROOD totdat de subagent gerund is op de POC-subset.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
POC_SUBSET = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_poc_subset.json"
INTERP_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"

SCHEMA_VERSIE_EXPECTED = "1.1"
VALID_HERKOMST = {"officieel", "herinnering", "hybride"}
VALID_VRAAGTYPE = {"open", "mc_keuze", "juist_fout", "onbekend"}
VALID_VOLLEDIGHEID = {"volledig", "fragment", "topic_only"}
VALID_CONTEXT_BLOK_TYPES = {
    "casus_context", "bijlage_verwijzing",
    "tabel", "gegevens_tabel", "balans", "resultatenrekening",
    "proef_saldibalans", "rekeningstaat", "inventaris",
    "marktwaarde", "aanpassing", "formule",
    "figuur",
    "tekst",
}
VERPLICHTE_TOP_VELDEN = {
    "schema_versie", "examen_id", "vraag_id", "interpretatie_datum",
    "vraag_herkomst", "vraag_onderwerp", "themas",
    "context_blokken", "vragen",
    "herinterpretatie_motivering", "kwaliteits_flags",
}
VERPLICHTE_VRAAG_VELDEN = {
    "id", "vraagtype", "motivatie_verwacht", "volledigheid",
}


def _laad_subset() -> list[dict]:
    return json.loads(POC_SUBSET.read_text(encoding="utf-8"))["selectie"]


def _interp_path(entry: dict) -> Path:
    return INTERP_DIR / entry["examen_id"] / f"{entry['vraag_id']}.json"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_interpretatie_bestaat(entry):
    path = _interp_path(entry)
    assert path.exists(), f"Interpretatie ontbreekt: {path}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_interpretatie_is_geldige_json(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_schema_versie_1_1(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data.get("schema_versie") == SCHEMA_VERSIE_EXPECTED


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_verplichte_top_velden(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = VERPLICHTE_TOP_VELDEN - set(data.keys())
    assert not missing, f"{entry['vraag_id']}: ontbrekende velden {missing}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_velden_match_subset_metadata(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["examen_id"] == entry["examen_id"]
    assert data["vraag_id"] == entry["vraag_id"]


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vraag_herkomst_enum(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["vraag_herkomst"] in VALID_HERKOMST


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_themas_is_lijst_strings(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    themas = data["themas"]
    assert isinstance(themas, list)
    for t in themas:
        assert isinstance(t, str) and t.strip(), (
            f"{entry['vraag_id']}: thema leeg of niet-string: {t!r}"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_context_blok_types_geldig(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        assert "type" in blok, f"{entry['vraag_id']}: context-blok zonder type"
        assert blok["type"] in VALID_CONTEXT_BLOK_TYPES, (
            f"{entry['vraag_id']}: onbekend context-blok-type {blok['type']!r}"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_balans_blok_heeft_actief_passief(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        if blok.get("type") != "balans":
            continue
        for sub in ("actief", "passief"):
            assert sub in blok, f"{entry['vraag_id']}: balans-blok mist {sub}"
            assert isinstance(blok[sub], dict)
            assert "headers" in blok[sub] and isinstance(blok[sub]["headers"], list)
            assert "rows" in blok[sub] and isinstance(blok[sub]["rows"], list)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_gegevens_tabel_blok(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for blok in data["context_blokken"]:
        if blok.get("type") != "gegevens_tabel":
            continue
        assert "titel" in blok and isinstance(blok["titel"], str)
        assert "rijen" in blok and isinstance(blok["rijen"], list) and blok["rijen"]
        for r in blok["rijen"]:
            assert "label" in r and isinstance(r["label"], str)
            assert "bedrag" in r and isinstance(r["bedrag"], (int, float))


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vragen_niet_leeg(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    vragen = data["vragen"]
    assert isinstance(vragen, list) and vragen, f"{entry['vraag_id']}: vragen[] leeg"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vragen_verplichte_velden(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        missing = VERPLICHTE_VRAAG_VELDEN - set(v.keys())
        assert not missing, (
            f"{entry['vraag_id']} deelvraag {v.get('id','?')}: ontbreekt {missing}"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vragen_enums(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        assert v["vraagtype"] in VALID_VRAAGTYPE
        assert v["volledigheid"] in VALID_VOLLEDIGHEID
        assert isinstance(v["motivatie_verwacht"], bool)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vragen_ids_uniek(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = [v["id"] for v in data["vragen"]]
    assert len(ids) == len(set(ids)), f"{entry['vraag_id']}: duplicate vragen-ids"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_mc_keuze_heeft_opties(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["vraagtype"] != "mc_keuze":
            continue
        opties = v.get("opties")
        assert isinstance(opties, list) and len(opties) >= 2, (
            f"{entry['vraag_id']} deelvraag {v['id']}: mc_keuze zonder >=2 opties"
        )
        opt_ids = [o["id"] for o in opties]
        assert len(opt_ids) == len(set(opt_ids)), (
            f"{entry['vraag_id']} deelvraag {v['id']}: duplicate optie-ids"
        )
        for o in opties:
            assert "id" in o and "tekst" in o


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_topic_only_consistent(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["volledigheid"] != "topic_only":
            continue
        assert v.get("vraagstelling") in (None, ""), (
            f"{entry['vraag_id']} deelvraag {v['id']}: topic_only met vraagstelling"
        )
        onderwerp = v.get("topic_only_onderwerp")
        assert isinstance(onderwerp, str) and onderwerp.strip(), (
            f"{entry['vraag_id']} deelvraag {v['id']}: topic_only zonder onderwerp"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_volledig_of_fragment_heeft_vraagstelling(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data["vragen"]:
        if v["volledigheid"] in ("volledig", "fragment"):
            vs = v.get("vraagstelling")
            assert isinstance(vs, str) and vs.strip(), (
                f"{entry['vraag_id']} deelvraag {v['id']}: {v['volledigheid']} "
                f"zonder vraagstelling"
            )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_motivering_niet_leeg(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    motivering = data.get("herinterpretatie_motivering", "")
    assert isinstance(motivering, str) and len(motivering.strip()) > 20


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_antwoord_hint_format(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    hint = data.get("antwoord_hint_in_vraag")
    if hint is None:
        return
    assert isinstance(hint, dict)
    assert "tekst" in hint and isinstance(hint["tekst"], str)
    assert "vermoedelijke_status" in hint
    # deelvraag_id is optioneel maar wenselijk
    if "deelvraag_id" in hint:
        deelvraag_ids = {v["id"] for v in data["vragen"]}
        assert hint["deelvraag_id"] in deelvraag_ids, (
            f"{entry['vraag_id']}: antwoord_hint deelvraag_id {hint['deelvraag_id']} "
            f"matcht geen vragen[].id"
        )


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_kwaliteits_flags_strings(entry):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    flags = data.get("kwaliteits_flags", [])
    assert isinstance(flags, list)
    for f in flags:
        assert isinstance(f, str)
