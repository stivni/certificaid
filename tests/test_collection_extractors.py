"""Tests voor de collection-extractor pipeline (CBN-adviezen + ITAA-normen).

Deze tests mocken de scrape-/PDF-laag zodat ze geen netwerk of raw PDFs
nodig hebben. Eén optionele integration-test draait de echte
norm-extractor als de PDF lokaal aanwezig is.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.etl import convert as orchestrator  # noqa: E402
from tools.lib import extractors  # noqa: E402


def test_collection_handlers_registered() -> None:
    """De twee collection-handlers staan in METHOD_HANDLERS."""
    assert "cbn_advies" in extractors.METHOD_HANDLERS
    assert "extract_norm" in extractors.METHOD_HANDLERS


def _write_advies_md(dir_path: Path, name: str, body: str = "originele body\n") -> Path:
    """Schrijf een mini CBN-advies-MD met realistische frontmatter."""
    md_path = dir_path / f"{name}.md"
    md_path.write_text(
        '---\n'
        'nummer: "CBN-advies 99/9"\n'
        'datum: 2024-01-01\n'
        'themas:\n'
        '  - test\n'
        f'bron: https://www.cbn-cnc.be/nl/adviezen/{name}\n'
        '---\n\n'
        f'{body}',
        encoding="utf-8",
    )
    return md_path


def test_cbn_collection_writes_staging_with_chunk_and_keeps_existing_fields(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Convert_collection itereert over MDs, behoudt bron-velden, voegt chunk toe."""
    # Setup: nep collection-config + nep output-dir met 2 MDs
    bronnen_dir = tmp_path / "adviezen"
    bronnen_dir.mkdir()
    _write_advies_md(bronnen_dir, "CBN-9999-01-test-een")
    _write_advies_md(bronnen_dir, "CBN-9999-02-test-twee")

    fake_collection = {
        "bron_rol": "interpretatief",
        "output_dir": str(bronnen_dir.relative_to(tmp_path)),  # niet gebruikt
        "item_inputs": [{"field": "bron", "kind": "url"}],
    }
    # Patch load_collections + ROOT-resolutie
    monkeypatch.setattr(orchestrator, "load_collections",
                        lambda: {"cbn-adviezen": fake_collection})
    monkeypatch.setattr(orchestrator, "ROOT", tmp_path)

    # Patch fake collection_cfg om naar onze tmp dir te wijzen.
    fake_collection["output_dir"] = "adviezen"

    # Mock de scrape — geen netwerk
    fake_scrape = mock.Mock(return_value={
        "title": "Geteste advies-titel",
        "body": "## Inleiding\n\nDit is een test-paragraaf.\n\n## Besluit\n\nKlaar.\n",
        "footnotes": [],
        "attachments": [],
        "raw_html": "",
        "url": "",
    })
    from tools.lib.extractors import cbn_advies as cbn_mod
    monkeypatch.setattr(cbn_mod, "scrape_advies", fake_scrape)

    n_done = orchestrator.convert_collection("cbn-adviezen")
    assert n_done == 2

    # Output landt direct terug op het bronbestand (geen staging-tussenmap)
    out_path = bronnen_dir / "CBN-9999-01-test-een.md"
    assert out_path.exists()
    text = out_path.read_text(encoding="utf-8")

    # Bestaande frontmatter-velden behouden
    assert 'nummer: "CBN-advies 99/9"' in text
    assert "datum: 2024-01-01" in text
    assert "bron: https://www.cbn-cnc.be" in text

    # Chunk-blok toegevoegd
    assert re.search(r"^chunk:\s*$", text, re.MULTILINE) is not None
    assert re.search(r"^\s+level:\s+2\s*$", text, re.MULTILINE) is not None

    # Bron_rol toegevoegd uit collection-config
    assert "bron_rol: interpretatief" in text

    # Body bevat de nieuwe content (na scrape)
    assert "Geteste advies-titel" in text
    assert "Inleiding" in text


def test_collection_skips_md_without_frontmatter(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """MDs zonder frontmatter (zoals INDEX.md zonder fm) worden geskipped."""
    bronnen_dir = tmp_path / "adviezen"
    bronnen_dir.mkdir()
    # MD zonder frontmatter
    (bronnen_dir / "ZONDER-FM.md").write_text("# Geen frontmatter\n", encoding="utf-8")

    fake_collection = {
        "bron_rol": "interpretatief",
        "output_dir": "adviezen",
        "item_inputs": [],
    }
    monkeypatch.setattr(orchestrator, "load_collections",
                        lambda: {"cbn-adviezen": fake_collection})
    monkeypatch.setattr(orchestrator, "ROOT", tmp_path)

    n_done = orchestrator.convert_collection("cbn-adviezen")
    assert n_done == 0


def test_norm_extractor_skips_when_no_local_pdf(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Norm-extractor gooit NotImplementedError voor items zonder lokale PDF."""
    from tools.lib.extractors import itaa_norm

    # Geen bron-pdf, geen mapping in KNOWN_PDFS, wel online URL
    cfg = {"online": "https://example.org/norm.pdf"}
    with pytest.raises(NotImplementedError):
        itaa_norm.extract(cfg, "ITAA-norm-niet-bestaand")


def test_norm_extractor_uses_known_pdfs_mapping_when_pdf_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Als KNOWN_PDFS een entry heeft en de PDF bestaat, dispatcht extract naar de
    PDF-pipeline. We mocken extract_nl_column om feitelijke PDF-IO te vermijden."""
    from tools.lib.extractors import itaa_norm
    from tools.etl import extract_norm_twocolumn as etn

    # Maak een fake PDF-pad dat lijkt te bestaan
    fake_pdf = Path("/tmp/fake-norm-test.pdf")
    fake_pdf.write_bytes(b"%PDF-1.4\n%fake")

    monkeypatch.setitem(
        etn.KNOWN_PDFS,
        "ITAA-norm-fake.md",
        {"pdf": fake_pdf, "type": "vereisten", "column_split": 400},
    )

    monkeypatch.setattr(itaa_norm, "extract_nl_column",
                        lambda *a, **kw: "## Heading\n\nBody.\n")
    monkeypatch.setattr(itaa_norm, "fix_norm_artefacts",
                        lambda body: (body, []))
    monkeypatch.setattr(itaa_norm, "inject_norm_headings",
                        lambda body: (body, 0))

    body = itaa_norm.extract({}, "ITAA-norm-fake")
    assert "Heading" in body
    fake_pdf.unlink()


def test_cbn_extractor_raises_on_missing_url() -> None:
    """CBN-extractor gooit RuntimeError als 'bron' ontbreekt."""
    from tools.lib.extractors import cbn_advies
    with pytest.raises(RuntimeError):
        cbn_advies.extract({}, "CBN-zonder-url")
