"""Extractor voor `pdftotext_ejustice` — ejustice/B.S. NL-PDFs.

Logica gekopieerd uit `tools/etl/convert.py` (functies pdftotext_nl,
pdftotext_simple, pdftotext_bilingual + de extractie-helft van convert_ejustice)
zonder gedragswijzigingen. Cleanup en frontmatter zijn NIET hier — die doet de
orchestrator centraal.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def _pdftotext_nl(pdf_path: str, start_page: int = 1,
                  end_page: int | None = None) -> str:
    """Extraheer NL-tekst uit een NL-only PDF met pdftotext -layout."""
    cmd = ["pdftotext", "-layout"]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {result.stderr}")
    return result.stdout


def _pdftotext_simple(pdf_path: str, start_page: int = 1,
                      end_page: int | None = None) -> str:
    """pdftotext zonder -layout: lineaire tekst, beter voor meerkolomsdocs."""
    cmd = ["pdftotext"]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {result.stderr}")
    return result.stdout


def _pdftotext_bilingual(pdf_path: str, nl_col_x: int, start_page: int = 1,
                         end_page: int | None = None) -> str:
    """Extraheer enkel de NL-kolom uit een tweetalige PDF."""
    col_w = 595 - nl_col_x - 10
    page_h = 842

    cmd = ["pdftotext", "-layout",
           "-x", str(nl_col_x), "-y", "0",
           "-W", str(col_w), "-H", str(page_h)]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext bilingual mislukt: {result.stderr}")
    return result.stdout


def extract(cfg: dict, source_name: str) -> str:
    """Extraheer NL-tekst uit een ejustice-PDF (zie ADR-005 §2)."""
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"raw-pad ontbreekt voor {source_name}")
    raw_path = ROOT / raw
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw PDF niet gevonden: {raw_path}")

    start_page = cfg.get("start_page", 1)
    end_page = cfg.get("end_page")
    simple_mode = cfg.get("simple_mode", False)

    extract_cfg = cfg.get("extract") or {}
    params = extract_cfg.get("params") or {}
    bilingual = params.get("bilingual", False)

    if simple_mode:
        return _pdftotext_simple(str(raw_path), start_page, end_page)
    if bilingual:
        nl_col_x = cfg.get("nl_col_x", params.get("nl_col_x", 0))
        return _pdftotext_bilingual(str(raw_path), nl_col_x, start_page, end_page)
    return _pdftotext_nl(str(raw_path), start_page, end_page)
