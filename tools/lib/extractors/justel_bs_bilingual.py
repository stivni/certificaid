"""Extractor voor `justel_bs_bilingual` — bilinguele B.S. PDF's (KB zonder Justel HTML).

Hergebruikt `extract_bs_bilingual_nl` + `clean_bs_bilingual_text` uit
`tools/etl/convert_justel.py`. Geeft alleen de markdown-body terug; de
orchestrator zorgt voor frontmatter + heading-chunk-blok.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from etl import convert_justel as _legacy  # type: ignore  # noqa: E402


def extract(cfg: dict, source_name: str) -> str:
    """Extract NL-kolom uit één of meer B.S. PDFs en lever cleane markdown-body."""
    params = (cfg.get("extract") or {}).get("params") or {}
    raw_files = params.get("raw_files", [])
    if not raw_files:
        raw_single = cfg.get("raw")
        if raw_single:
            raw_files = [raw_single]
        else:
            raise ValueError(
                f"extract.params.raw_files of raw ontbreekt voor {source_name}"
            )

    nl_col_x = params.get("nl_col_x", 290)
    pdf_paths = [str(ROOT / f) for f in raw_files]
    for p in pdf_paths:
        if not Path(p).exists():
            raise FileNotFoundError(f"PDF niet gevonden: {p}")

    raw_text = _legacy.extract_bs_bilingual_nl(pdf_paths, nl_col_x=nl_col_x)
    return _legacy.clean_bs_bilingual_text(raw_text)
