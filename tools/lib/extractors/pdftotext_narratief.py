"""Extractor voor `pdftotext_narratief` — narratieve praktijkgidsen (Type 3 PDFs).

Wrapper rond `pdftotext_ejustice.extract` met `simple_mode=True`. Bedoeld voor
PDFs zonder artikel-hiërarchie (toelichtingen, gidsen, mementos) waarbij de
standaard `inject_headings_wettekst`-transformer niet bruikbaar is.

De extract-logica is identiek aan `pdftotext_ejustice` met `simple_mode: true`.
Het aparte extractor-type maakt het mogelijk om een eigen transformer-chain
te koppelen via `DEFAULT_CHAINS` in `tools/etl/convert.py`.
"""
from __future__ import annotations

from tools.lib.extractors.pdftotext_ejustice import _pdftotext_simple
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def extract(cfg: dict, source_name: str) -> str:
    """Extraheer tekst uit een narratieve PDF via pdftotext zonder -layout."""
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"raw-pad ontbreekt voor {source_name}")
    raw_path = ROOT / raw
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw PDF niet gevonden: {raw_path}")

    extract_cfg = cfg.get("extract") or {}
    params = extract_cfg.get("params") or {}
    start_page = params.get("start_page") or cfg.get("start_page", 1)
    end_page = params.get("end_page") or cfg.get("end_page")

    return _pdftotext_simple(str(raw_path), start_page, end_page)
