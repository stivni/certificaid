"""TDD-tests voor tools.examen.isoleer_vragen (ADR-024 §2).

Roept de CLI end-to-end aan op de POC-subset en verifieert dat per vraag een
tekst.txt, meta.json en minstens één pagina_NN.png ontstaan onder
data/programma/examen_vragen/_segmenten/<examen_id>/<vraag_id>/.

Idempotentie wordt getest door twee opeenvolgende runs: mtimes van bestaande
artefacten mogen niet wijzigen.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

pdfplumber = pytest.importorskip("pdfplumber")
PIL = pytest.importorskip("PIL")
from PIL import Image  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBSET_PATH = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_poc_subset.json"
SEGMENTEN_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_segmenten"
PDF_DIR = REPO_ROOT / "resources" / "raw" / "voorbeeldexamens"


def _laad_subset() -> list[dict]:
    return json.loads(SUBSET_PATH.read_text(encoding="utf-8"))["selectie"]


def _heeft_pdfs() -> bool:
    for entry in _laad_subset():
        # mapping examen_id -> pdf_bestand zit in extract_vragen_v2.EXAMEN_CONFIGS_V2
        # — we testen alleen dat de subset-pdfs aanwezig zijn (anders skip)
        pass
    return PDF_DIR.exists()


@pytest.fixture(scope="module")
def run_cli():
    """Roep de CLI eenmalig aan en geef de stdout/return-code terug."""
    if not SUBSET_PATH.exists():
        pytest.skip("POC-subset ontbreekt")
    if not PDF_DIR.exists():
        pytest.skip("voorbeeldexamens-PDFs ontbreken")

    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    res = subprocess.run(
        [sys.executable, "-m", "tools.examen.isoleer_vragen"],
        cwd=str(REPO_ROOT),
        env=env,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert res.returncode == 0, f"CLI faalde: {res.stderr}\n{res.stdout}"
    return res


class TestSegmentArtefacten:
    @pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
    def test_segment_map_bestaat(self, run_cli, entry):
        seg_dir = SEGMENTEN_DIR / entry["examen_id"] / entry["vraag_id"]
        assert seg_dir.is_dir(), f"{seg_dir} ontbreekt"

    @pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
    def test_tekst_bestand_niet_leeg(self, run_cli, entry):
        tekst = SEGMENTEN_DIR / entry["examen_id"] / entry["vraag_id"] / "tekst.txt"
        assert tekst.is_file(), f"{tekst} ontbreekt"
        inhoud = tekst.read_text(encoding="utf-8")
        assert inhoud.strip(), f"{tekst} is leeg"

    @pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
    def test_meta_json_schema(self, run_cli, entry):
        meta_p = SEGMENTEN_DIR / entry["examen_id"] / entry["vraag_id"] / "meta.json"
        assert meta_p.is_file()
        meta = json.loads(meta_p.read_text(encoding="utf-8"))

        verplichte_velden = {
            "examen_id",
            "vraag_id",
            "pagina_nummers",
            "pdf_bestand",
            "bbox_hint",
        }
        ontbreekt = verplichte_velden - set(meta.keys())
        assert not ontbreekt, f"verplichte velden ontbreken: {ontbreekt}"

        assert meta["examen_id"] == entry["examen_id"]
        assert meta["vraag_id"] == entry["vraag_id"]
        assert isinstance(meta["pagina_nummers"], list)
        assert all(isinstance(p, int) for p in meta["pagina_nummers"])
        assert len(meta["pagina_nummers"]) >= 1
        # bbox_hint mag None zijn
        assert meta["bbox_hint"] is None or isinstance(meta["bbox_hint"], list)
        assert isinstance(meta["pdf_bestand"], str) and meta["pdf_bestand"].endswith(".pdf")

    @pytest.mark.parametrize("entry", _laad_subset(), ids=lambda e: e["vraag_id"])
    def test_minstens_een_png(self, run_cli, entry):
        seg_dir = SEGMENTEN_DIR / entry["examen_id"] / entry["vraag_id"]
        pngs = sorted(seg_dir.glob("pagina_*.png"))
        verwacht_aantal = entry["pagina_tot"] - entry["pagina_van"] + 1
        assert len(pngs) >= 1, f"geen PNGs in {seg_dir}"
        assert len(pngs) == verwacht_aantal, (
            f"verwacht {verwacht_aantal} PNGs, kreeg {len(pngs)}"
        )
        for png in pngs:
            assert png.stat().st_size > 0, f"{png} is 0 bytes"
            with Image.open(png) as img:
                img.verify()
            with Image.open(png) as img:
                assert img.mode in ("RGB", "RGBA"), f"{png} mode={img.mode}"


class TestIdempotentie:
    def test_tweede_run_wijzigt_niets(self, run_cli):
        # Verzamel mtimes van alle artefacten na eerste run
        artefacten: dict[Path, float] = {}
        for entry in _laad_subset():
            seg_dir = SEGMENTEN_DIR / entry["examen_id"] / entry["vraag_id"]
            for p in seg_dir.iterdir():
                artefacten[p] = p.stat().st_mtime

        assert artefacten, "geen artefacten gevonden om idempotentie te testen"

        # Tweede run
        env = os.environ.copy()
        env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
        res = subprocess.run(
            [sys.executable, "-m", "tools.examen.isoleer_vragen"],
            cwd=str(REPO_ROOT),
            env=env,
            capture_output=True,
            text=True,
            timeout=300,
        )
        assert res.returncode == 0, f"tweede run faalde: {res.stderr}"

        for p, m in artefacten.items():
            assert p.exists(), f"{p} verdwenen bij tweede run"
            assert p.stat().st_mtime == m, f"{p} gewijzigd bij tweede run"


class TestSelectieFilters:
    def test_examen_filter(self, tmp_path):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
        res = subprocess.run(
            [
                sys.executable,
                "-m",
                "tools.examen.isoleer_vragen",
                "--vraag",
                "2013-1-vr1",
            ],
            cwd=str(REPO_ROOT),
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
        )
        assert res.returncode == 0, res.stderr
        seg_dir = SEGMENTEN_DIR / "2013-1" / "2013-1-vr1"
        assert (seg_dir / "tekst.txt").is_file()
        assert (seg_dir / "meta.json").is_file()
