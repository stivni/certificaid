"""TDD-tests voor tools.examen.merge_examen_artefacten (ADR-024 §6).

Roept de CLI end-to-end aan op de POC-subset en verifieert dat per examen
één samengesteld `_merged/<examen>.json` ontstaat met schema 4.0. Test
idempotentie (twee runs → byte-identiek) en fail-loud (ontbrekend artefact
→ exit-code != 0).

POC-modus: output landt onder `_merged/<examen>.json`, niet over het
bestaande v3 `<examen>.json` heen.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMEN_VRAGEN_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen"
SUBSET_PATH = EXAMEN_VRAGEN_DIR / "_poc_subset.json"
INTERPRETATIES_DIR = EXAMEN_VRAGEN_DIR / "_interpretaties"
ANTWOORDEN_DIR = EXAMEN_VRAGEN_DIR / "_antwoorden"
SEGMENTEN_DIR = EXAMEN_VRAGEN_DIR / "_segmenten"
MERGED_DIR = EXAMEN_VRAGEN_DIR / "_merged"


def _laad_subset() -> list[dict]:
    return json.loads(SUBSET_PATH.read_text(encoding="utf-8"))["selectie"]


def _examens_met_volledige_artefacten() -> list[str]:
    """Examens waar elke POC-vraag zowel interpretatie als antwoord heeft."""
    per_examen: dict[str, list[dict]] = defaultdict(list)
    for entry in _laad_subset():
        per_examen[entry["examen_id"]].append(entry)

    resultaat: list[str] = []
    for examen_id, entries in per_examen.items():
        compleet = all(
            (INTERPRETATIES_DIR / examen_id / f"{e['vraag_id']}.json").is_file()
            and (ANTWOORDEN_DIR / examen_id / f"{e['vraag_id']}.json").is_file()
            for e in entries
        )
        if compleet:
            resultaat.append(examen_id)
    return sorted(resultaat)


def _run_cli(*args: str, expect_fail: bool = False) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    res = subprocess.run(
        [sys.executable, "-m", "tools.examen.merge_examen_artefacten", *args],
        cwd=str(REPO_ROOT),
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if not expect_fail:
        assert res.returncode == 0, f"CLI faalde: {res.stderr}\n{res.stdout}"
    return res


@pytest.fixture(scope="module", autouse=True)
def _backup_restore_merged():
    """Snapshot productie `_merged/`-state vóór tests, restore erna.

    De merger-CLI schrijft naar de echte productie-dir; deze fixture
    voorkomt dat de POC-subset-run de volledige `--alle`-uitrol-output
    overschrijft. Bij tests die nooit gedraaid hebben is dit een no-op.
    """
    if not MERGED_DIR.exists():
        yield
        return
    backup: dict[Path, bytes] = {}
    for p in MERGED_DIR.glob("*.json"):
        backup[p] = p.read_bytes()
    try:
        yield
    finally:
        # Cleanup test-artefacten die niet in backup zaten
        for p in MERGED_DIR.glob("*.json"):
            if p not in backup:
                p.unlink()
        # Restore originele content
        for p, data in backup.items():
            p.write_bytes(data)


@pytest.fixture(scope="module")
def run_cli():
    if not SUBSET_PATH.exists():
        pytest.skip("POC-subset ontbreekt")
    if not _examens_met_volledige_artefacten():
        pytest.skip("geen examen met volledige interpretatie+antwoord-artefacten")
    return _run_cli()


class TestMergerOutput:
    @pytest.mark.parametrize("examen_id", _examens_met_volledige_artefacten())
    def test_merged_file_bestaat(self, run_cli, examen_id):
        merged = MERGED_DIR / f"{examen_id}.json"
        assert merged.is_file(), f"{merged} ontbreekt na merger-run"

    @pytest.mark.parametrize("examen_id", _examens_met_volledige_artefacten())
    def test_schema_versie_4(self, run_cli, examen_id):
        merged = MERGED_DIR / f"{examen_id}.json"
        data = json.loads(merged.read_text(encoding="utf-8"))
        assert data["schema_versie"] == "4.0"
        assert data["examen_id"] == examen_id
        assert data["tool"] == "merge-examen-artefacten"
        assert isinstance(data["bron_pdf"], str) and data["bron_pdf"].endswith(".pdf")
        assert isinstance(data["merge_datum"], str)
        assert "vragen" in data and isinstance(data["vragen"], list)
        assert data["vragen"], "vragen-lijst is leeg"

    @pytest.mark.parametrize("examen_id", _examens_met_volledige_artefacten())
    def test_vragen_bevatten_interpretatie_en_antwoord(self, run_cli, examen_id):
        merged = MERGED_DIR / f"{examen_id}.json"
        data = json.loads(merged.read_text(encoding="utf-8"))
        verwachte_ids = {
            e["vraag_id"] for e in _laad_subset() if e["examen_id"] == examen_id
        }
        gevonden_ids = {v["vraag_id"] for v in data["vragen"]}
        assert gevonden_ids == verwachte_ids, (
            f"vraag-ids in merged file ({gevonden_ids}) "
            f"matchen niet met POC-subset voor {examen_id} ({verwachte_ids})"
        )
        for v in data["vragen"]:
            assert "interpretatie" in v and isinstance(v["interpretatie"], dict)
            assert "antwoord" in v and isinstance(v["antwoord"], dict)
            assert "segment_meta" in v and isinstance(v["segment_meta"], dict)
            # sanity: schema_versie van bron-artefact moet aanwezig zijn
            assert v["interpretatie"].get("vraag_id") == v["vraag_id"]
            assert v["antwoord"].get("vraag_id") == v["vraag_id"]
            assert v["segment_meta"].get("vraag_id") == v["vraag_id"]

    @pytest.mark.parametrize("examen_id", _examens_met_volledige_artefacten())
    def test_output_parseert_als_json(self, run_cli, examen_id):
        merged = MERGED_DIR / f"{examen_id}.json"
        # Moet zonder fouten parsen + UTF-8 zijn
        json.loads(merged.read_text(encoding="utf-8"))


class TestV3NietOverschreven:
    """ADR-024 POC: bestaande <examen>.json (schema 3.0) blijft staan."""

    @pytest.mark.parametrize("examen_id", _examens_met_volledige_artefacten())
    def test_v3_artefact_onaangeraakt(self, run_cli, examen_id):
        v3_pad = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
        if not v3_pad.is_file():
            pytest.skip(f"geen v3-artefact aanwezig voor {examen_id}")
        v3_data = json.loads(v3_pad.read_text(encoding="utf-8"))
        assert v3_data.get("schema_versie") != "4.0", (
            "v3 examen-bestand mag NIET door merger overschreven worden"
        )


class TestIdempotentie:
    def test_tweede_run_byte_identiek(self, run_cli):
        examens = _examens_met_volledige_artefacten()
        assert examens, "geen examens om te testen"

        # snapshot van inhoud + mtime na eerste run
        inhoud_voor: dict[str, bytes] = {}
        mtime_voor: dict[str, float] = {}
        for examen_id in examens:
            merged = MERGED_DIR / f"{examen_id}.json"
            inhoud_voor[examen_id] = merged.read_bytes()
            mtime_voor[examen_id] = merged.stat().st_mtime

        # tweede run
        _run_cli()

        for examen_id in examens:
            merged = MERGED_DIR / f"{examen_id}.json"
            assert merged.read_bytes() == inhoud_voor[examen_id], (
                f"{merged} is gewijzigd bij tweede run (niet byte-identiek)"
            )
            assert merged.stat().st_mtime == mtime_voor[examen_id], (
                f"{merged} is herschreven bij tweede run (mtime gewijzigd)"
            )


class TestFailLoud:
    def test_ontbrekend_antwoord_geeft_exit_1(self, tmp_path):
        """Renamen we tijdelijk een antwoord-artefact, dan moet de merger
        fail-loud crashen met exit-code != 0.

        We doen dit op een examen waar de POC-subset slechts één vraag heeft
        (2013-1 of 2014-1) zodat de mutatie minimal-invasive is.
        """
        examens = _examens_met_volledige_artefacten()
        if not examens:
            pytest.skip("geen geschikt examen om fail-loud te testen")

        # kies een examen met exact één POC-vraag
        per_examen: dict[str, list[dict]] = defaultdict(list)
        for entry in _laad_subset():
            per_examen[entry["examen_id"]].append(entry)
        kandidaten = [e for e in examens if len(per_examen[e]) == 1]
        if not kandidaten:
            pytest.skip("geen examen met exact één POC-vraag")
        examen_id = kandidaten[0]
        vraag_id = per_examen[examen_id][0]["vraag_id"]

        antwoord_bestand = ANTWOORDEN_DIR / examen_id / f"{vraag_id}.json"
        backup = tmp_path / f"{vraag_id}.json.bak"
        shutil.copy2(antwoord_bestand, backup)
        try:
            antwoord_bestand.unlink()
            res = _run_cli("--examen", examen_id, expect_fail=True)
            assert res.returncode != 0, (
                f"merger had moeten falen met exit-code != 0, kreeg {res.returncode}\n"
                f"stdout: {res.stdout}\nstderr: {res.stderr}"
            )
            # boodschap moet de ontbrekende vraag noemen
            output = (res.stdout + res.stderr).lower()
            assert vraag_id.lower() in output or "antwoord" in output, (
                f"foutboodschap noemt vraag-id of 'antwoord' niet: {res.stderr}"
            )
        finally:
            shutil.copy2(backup, antwoord_bestand)


class TestSingleExamenFilter:
    def test_examen_filter(self):
        examens = _examens_met_volledige_artefacten()
        if not examens:
            pytest.skip("geen examens om te testen")
        examen_id = examens[0]
        res = _run_cli("--examen", examen_id)
        assert res.returncode == 0
        merged = MERGED_DIR / f"{examen_id}.json"
        assert merged.is_file()
        data = json.loads(merged.read_text(encoding="utf-8"))
        assert data["examen_id"] == examen_id
