"""Tests voor tools/lib/extractors/pdftotext_compilatie_btw.

Deze tests prikken op de pure helpers (`_clean_body`, `_build_splits`) en
mocken de pdftotext-stap, zodat we niet van een echte PDF afhankelijk zijn.
"""
from __future__ import annotations

from unittest import mock

import pytest

from tools.lib.extractors import pdftotext_compilatie_btw as ext


def test_clean_body_strips_fod_headers_and_page_numbers():
    raw = (
        "FOD Financiën — Btw KB nr. 1\n"
        "echte inhoud\n"
        "- 7 -\n"
        "Btw KB nr. 1 - bijw. 06.03.2020\n"
        "nog meer inhoud\n"
    )
    cleaned = ext._clean_body(raw)
    assert "echte inhoud" in cleaned
    assert "nog meer inhoud" in cleaned
    assert "FOD Financiën" not in cleaned
    assert "- 7 -" not in cleaned
    assert "bijw. 06.03.2020" not in cleaned


def test_build_splits_hoists_extra_metadata_keys():
    cfg = {
        "splits": [
            {
                "kb_id": 1,
                "output": "resources/bronnen/wetteksten/WBTW-KB1-x.md",
                "wet": "K.B. nr. 1",
                "tags": ["VI.B", "2.4"],
                "itaa_sectie": "VI.B",
                "bijgewerkt": "29.12.1992",
            },
        ],
    }
    splits = ext._build_splits(cfg)
    assert len(splits) == 1
    s = splits[0]
    assert s.kb_id == "1"
    assert s.output.endswith("WBTW-KB1-x.md")
    assert s.wet == "K.B. nr. 1"
    # Top-level extra keys worden in extra_metadata gehoist.
    assert s.extra_metadata["tags"] == ["VI.B", "2.4"]
    assert s.extra_metadata["bijgewerkt"] == "29.12.1992"


def test_extract_compilatie_routes_splits(tmp_path, monkeypatch):
    """Smoketest: handler returneert dict met body per output-pad."""
    # Maak een fake PDF-pad (pdftotext wordt gemockt).
    fake_pdf = tmp_path / "fake.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 fake")

    fake_text = (
        "FOD Financiën — Btw KB nr. 1\n"
        "inhoud-1\n"
        "FOD Financiën — Btw KB nr. 2\n"
        "inhoud-2\n"
    )

    cfg = {
        "raw": str(fake_pdf.relative_to(tmp_path)),  # niet realistisch, we mocken
        "splits": [
            {"kb_id": "1", "output": "out/kb1.md", "wet": "KB 1"},
            {"kb_id": "2", "output": "out/kb2.md", "wet": "KB 2"},
        ],
    }

    # Forceer raw_path-resolution naar onze tmp_path-PDF en pdftotext-output.
    monkeypatch.setattr(ext, "ROOT", tmp_path)
    monkeypatch.setattr(ext, "_pdftotext_layout", lambda _p: fake_text)

    result = ext.extract_compilatie(cfg, "WBTW-KBs")
    assert set(result.keys()) == {"out/kb1.md", "out/kb2.md"}
    assert "inhoud-1" in result["out/kb1.md"]
    assert "inhoud-2" in result["out/kb2.md"]
    # Page-headers gestript door _clean_body
    assert "FOD Financiën" not in result["out/kb1.md"]


def test_extract_compilatie_requires_splits(tmp_path, monkeypatch):
    fake_pdf = tmp_path / "fake.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4")
    cfg = {"raw": "fake.pdf"}
    monkeypatch.setattr(ext, "ROOT", tmp_path)
    monkeypatch.setattr(ext, "_pdftotext_layout", lambda _p: "x")
    with pytest.raises(ValueError, match="splits"):
        ext.extract_compilatie(cfg, "WBTW-KBs")
