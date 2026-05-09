"""Tests voor de `custom_wetboek` extractor.

De belangrijkste regressie die hier afgevangen wordt: de truthy-bug
waardoor `col_x: 0` (NL-kolom links) in `or 300` viel en de FR-kolom
werd uitgesneden. Zie taak G3 (mei 2026) voor context.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.extractors import custom_wetboek  # noqa: E402


class _FakeResult:
    def __init__(self, stdout: str = "", returncode: int = 0) -> None:
        self.stdout = stdout
        self.stderr = ""
        self.returncode = returncode


def _capture_pdftotext_calls(monkeypatch: pytest.MonkeyPatch) -> list[list[str]]:
    """Vervang subprocess.run zodat we de pdftotext-args kunnen inspecteren."""
    calls: list[list[str]] = []

    def fake_run(cmd, *args, **kwargs):
        calls.append(list(cmd))
        if cmd and cmd[0] == "pdfinfo":
            return _FakeResult(stdout="Pages: 9\n")
        # pdftotext: lever een hapje placeholder-tekst zodat de cleanup niet
        # crasht; de unit-test inspecteert alleen de cmd-args.
        return _FakeResult(stdout="Artikel 1\n\nNL-tekst.\n")

    monkeypatch.setattr(custom_wetboek.subprocess, "run", fake_run)
    return calls


def test_extract_bilingual_col_x_zero_uses_left_column(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Regressie: `col_x: 0` mag NIET via een truthy-fallback op 300 belanden.

    Vóór de fix gebruikte `_extract_nl_text` `col_x = cfg.get("col_x") or 300`
    waardoor de geldige waarde 0 (NL-kolom links) door `or` werd genegeerd en
    pdftotext de FR-kolom uitsneed.
    """
    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n")

    cfg = {
        "raw": str(pdf.relative_to(tmp_path)) if False else "fake.pdf",
        "extract": {
            "method": "custom_wetboek",
            "params": {
                "mode": "bilingual",
                "col_x": 0,
                "start_page": 8,
            },
        },
    }
    # raw moet bestaan; patch de pad-resolutie naar tmp_path.
    monkeypatch.setattr(custom_wetboek, "ROOT", tmp_path)
    cfg["raw"] = "fake.pdf"

    calls = _capture_pdftotext_calls(monkeypatch)
    custom_wetboek.extract(cfg, "fake-bron")

    pdftotext_calls = [c for c in calls if c and c[0] == "pdftotext"]
    assert pdftotext_calls, "Geen pdftotext-aanroep waargenomen"
    # Voor elke pagina-call moet -x op 0 staan (NL links), niet op 300 (FR rechts).
    for cmd in pdftotext_calls:
        assert "-x" in cmd, f"verwacht -x flag in {cmd}"
        x_value = cmd[cmd.index("-x") + 1]
        assert x_value == "0", (
            f"col_x:0 viel terug op '{x_value}' — truthy-bug niet gefixt"
        )


def test_extract_bilingual_default_col_x_is_left_not_right(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Default voor bilingual is NL-links (col_x=0), niet FR-rechts (col_x=300).

    De Fisconet/JUSTEL-PDFs voor BE-wetboeken hebben NL standaard links;
    de oude default 300 sneed de FR-kolom uit. Wanneer geen `col_x` gegeven
    wordt, moet de extractor x=0 gebruiken.
    """
    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n")

    cfg = {
        "raw": "fake.pdf",
        "extract": {
            "method": "custom_wetboek",
            "params": {
                "mode": "bilingual",
                "start_page": 1,
            },
        },
    }
    monkeypatch.setattr(custom_wetboek, "ROOT", tmp_path)

    calls = _capture_pdftotext_calls(monkeypatch)
    custom_wetboek.extract(cfg, "fake-bron")

    pdftotext_calls = [c for c in calls if c and c[0] == "pdftotext"]
    assert pdftotext_calls
    for cmd in pdftotext_calls:
        x_value = cmd[cmd.index("-x") + 1]
        assert x_value == "0", f"verwachte default col_x=0, kreeg {x_value}"


def test_extract_reads_params_from_extract_block(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """`mode`, `col_x` en `start_page` kunnen ook onder `extract.params` staan.

    De legacy-config plaatste deze velden top-level; nieuwe config plaatst
    ze onder `extract.params`. Beide moeten werken; `extract.params` heeft
    voorrang wanneer beide gezet zijn.
    """
    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n")

    cfg = {
        "raw": "fake.pdf",
        # Top-level legacy-veld dat door extract.params overschreven wordt:
        "col_x": 300,
        "extract": {
            "method": "custom_wetboek",
            "params": {
                "mode": "bilingual",
                "col_x": 0,  # voorrang
                "start_page": 5,
            },
        },
    }
    monkeypatch.setattr(custom_wetboek, "ROOT", tmp_path)

    calls = _capture_pdftotext_calls(monkeypatch)
    custom_wetboek.extract(cfg, "fake-bron")

    pdftotext_calls = [c for c in calls if c and c[0] == "pdftotext"]
    assert pdftotext_calls
    for cmd in pdftotext_calls:
        x_value = cmd[cmd.index("-x") + 1]
        assert x_value == "0", "extract.params.col_x:0 moet voorrang hebben op top-level col_x:300"
    # start_page=5 → eerste pagina-aanroep heeft -f 5
    first_page = pdftotext_calls[0]
    assert first_page[first_page.index("-f") + 1] == "5"
