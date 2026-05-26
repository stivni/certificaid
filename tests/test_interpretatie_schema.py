"""Schema-validatie voor _interpretaties/<examen>/<vraag-id>.json.

Bron-van-waarheid: data/programma/examen_vragen/interpretatie-1.2.schema.json
(ADR-024 §3). Dit testbestand laadt dat schema en valideert elke interpretatie
in de POC-subset ertegen. Twee cross-reference checks die JSON-Schema niet
uitdrukt (uniciteit van deelvraag-ids + hint.deelvraag_id-koppeling) blijven
als Python-tests.

Tests zijn ROOD totdat de interpretatie-subagent gerund is op de POC-subset.
"""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
POC_SUBSET = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_poc_subset.json"
INTERP_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"
SCHEMA_PATH = REPO_ROOT / "data" / "programma" / "examen_vragen" / "interpretatie-1.2.schema.json"


def _laad_subset() -> list[dict]:
    return json.loads(POC_SUBSET.read_text(encoding="utf-8"))["selectie"]


def _interp_path(entry: dict) -> Path:
    return INTERP_DIR / entry["examen_id"] / f"{entry['vraag_id']}.json"


@pytest.fixture(scope="module")
def validator() -> jsonschema.Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_interpretatie_bestaat(entry):
    path = _interp_path(entry)
    assert path.exists(), f"Interpretatie ontbreekt: {path}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_interpretatie_valideert_tegen_schema(entry, validator):
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        msg = "\n".join(f"  {list(e.path)}: {e.message}" for e in errors)
        pytest.fail(f"{entry['vraag_id']} schema-violaties:\n{msg}")


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_velden_match_subset_metadata(entry):
    """Cross-check: examen_id en vraag_id in het artefact matchen de POC-subset-entry."""
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["examen_id"] == entry["examen_id"]
    assert data["vraag_id"] == entry["vraag_id"]


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_vragen_ids_uniek(entry):
    """Cross-check: deelvraag-ids zijn uniek binnen vragen[] (niet door schema afgedwongen)."""
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = [v["id"] for v in data.get("vragen", [])]
    assert len(ids) == len(set(ids)), f"{entry['vraag_id']}: duplicate vragen-ids {ids}"


@pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
def test_antwoord_hint_deelvraag_id_bestaat(entry):
    """Cross-check: hint.deelvraag_id (indien aanwezig) matcht een vragen[].id."""
    path = _interp_path(entry)
    if not path.exists():
        pytest.skip("artefact ontbreekt")
    data = json.loads(path.read_text(encoding="utf-8"))
    hint = data.get("antwoord_hint_in_vraag")
    if not isinstance(hint, dict) or "deelvraag_id" not in hint:
        return
    deelvraag_ids = {v["id"] for v in data.get("vragen", [])}
    assert hint["deelvraag_id"] in deelvraag_ids, (
        f"{entry['vraag_id']}: antwoord_hint.deelvraag_id "
        f"{hint['deelvraag_id']!r} matcht geen vragen[].id"
    )
