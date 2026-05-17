"""Test voor `--items` filter op `convert_collection` (cascade-vermijding).

Sessie 2026-05-17: `convert.py --collection cbn-adviezen` zonder filter triggert
een trust-cascade (alle 437 items terug op `unreviewed`). De `--items` parameter
beperkt de batch tot specifieke stems zodat we 14 needs-rework CBN's kunnen
re-runnen zonder de andere 423 te raken.

Deze test mockt de scrape-laag — geen netwerk vereist.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import convert as orchestrator  # noqa: E402


def _write_advies_md(dir_path: Path, name: str) -> Path:
    md_path = dir_path / f"{name}.md"
    md_path.write_text(
        '---\n'
        'nummer: "CBN-advies 99/9"\n'
        'datum: 2024-01-01\n'
        'themas:\n'
        '  - test\n'
        f'bron: https://www.cbn-cnc.be/nl/adviezen/{name}\n'
        '---\n\n'
        'originele body\n',
        encoding="utf-8",
    )
    return md_path


def test_convert_collection_items_filter_processes_only_listed_stems(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Met `items=[stem]` verwerkt `convert_collection` alleen die ene MD.

    Vertrekken vanuit 3 MDs in de output-dir; filter beperkt tot 1 → return = 1.
    De andere twee MDs blijven onaangeraakt (originele body intact).
    """
    bronnen_dir = tmp_path / "adviezen"
    bronnen_dir.mkdir()
    _write_advies_md(bronnen_dir, "CBN-9999-01-test-een")
    _write_advies_md(bronnen_dir, "CBN-9999-02-test-twee")
    _write_advies_md(bronnen_dir, "CBN-9999-03-test-drie")

    fake_collection = {
        "bron_rol": "interpretatief",
        "output_dir": "adviezen",
        "item_inputs": [{"field": "bron", "kind": "url"}],
    }
    monkeypatch.setattr(orchestrator, "load_collections",
                        lambda: {"cbn-adviezen": fake_collection})
    monkeypatch.setattr(orchestrator, "ROOT", tmp_path)

    fake_scrape = mock.Mock(return_value={
        "title": "Geteste advies-titel",
        "body": "## Inleiding\n\nTest.\n",
        "footnotes": [],
        "attachments": [],
        "raw_html": "",
        "url": "",
    })
    from tools.lib.extractors import cbn_advies as cbn_mod
    monkeypatch.setattr(cbn_mod, "scrape_advies", fake_scrape)

    n_done = orchestrator.convert_collection(
        "cbn-adviezen", items=["CBN-9999-02-test-twee"],
    )

    assert n_done == 1, (
        f"Verwacht: 1 item verwerkt (de gefilterde), kreeg: {n_done}"
    )
    # Scrape mag maximaal éénmaal aangeroepen worden (alleen voor het filter-item)
    assert fake_scrape.call_count == 1, (
        f"Verwacht: 1 scrape-call, kreeg: {fake_scrape.call_count}"
    )

    # De twee niet-gefilterde MDs zijn niet aangeraakt
    untouched_one = (bronnen_dir / "CBN-9999-01-test-een.md").read_text(encoding="utf-8")
    untouched_three = (bronnen_dir / "CBN-9999-03-test-drie.md").read_text(encoding="utf-8")
    assert "originele body" in untouched_one
    assert "originele body" in untouched_three

    # De gefilterde MD is wel herschreven (bevat scraped content)
    touched = (bronnen_dir / "CBN-9999-02-test-twee.md").read_text(encoding="utf-8")
    assert "Geteste advies-titel" in touched
    assert "Inleiding" in touched


def test_convert_collection_items_filter_warns_on_unknown_stem(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture,
) -> None:
    """Onbekende stem in `items` wordt gemeld, niet stilzwijgend geskipped."""
    bronnen_dir = tmp_path / "adviezen"
    bronnen_dir.mkdir()
    _write_advies_md(bronnen_dir, "CBN-9999-01-test-een")

    fake_collection = {
        "bron_rol": "interpretatief",
        "output_dir": "adviezen",
        "item_inputs": [],
    }
    monkeypatch.setattr(orchestrator, "load_collections",
                        lambda: {"cbn-adviezen": fake_collection})
    monkeypatch.setattr(orchestrator, "ROOT", tmp_path)

    from tools.lib.extractors import cbn_advies as cbn_mod
    monkeypatch.setattr(cbn_mod, "scrape_advies",
                        mock.Mock(return_value={
                            "title": "x", "body": "## A\n\nb\n",
                            "footnotes": [], "attachments": [], "raw_html": "", "url": "",
                        }))

    n_done = orchestrator.convert_collection(
        "cbn-adviezen", items=["CBN-niet-bestaand"],
    )
    assert n_done == 0
    captured = capsys.readouterr()
    assert "CBN-niet-bestaand" in captured.out, (
        "Onbekende stem moet expliciet gemeld worden in de output."
    )
