"""Extractor voor `custom_wib92` — WIB92.pdf NL-kolom uit een tweetalige PDF.

Logica gekopieerd uit `tools/etl/convert-wib92.py`. Het oude script schreef de
output (incl. frontmatter) zelf weg; deze handler retourneert alleen de
gestructureerde NL-tekst (markdown body) zodat de orchestrator de gedeelde
cleanup en heading-injection kan uitvoeren.

NB: WIB92 heeft een vast pagina-bereik (42–1315) en kolom-coördinaten in de YAML
expliciet leeg gelaten — we vallen terug op dezelfde defaults als het
oorspronkelijke convert-wib92.py.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Maak `tools.lib.cleanup`-import beschikbaar (zelfde pad-truc als oude scripts).
sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import (  # noqa: E402
    fix_broken_words,
    merge_heading_continuations,
    merge_wrapped_lines,
)

# Defaults uit convert-wib92.py
_START_PAGE = 42
_END_PAGE = 1315
_COL_X = 300
_COL_W = 295
_PAGE_H = 842


def _extract_page(pdf_path: str, page: int,
                  col_x: int, col_w: int, page_h: int) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout",
         "-f", str(page), "-l", str(page),
         "-x", str(col_x), "-y", "0", "-W", str(col_w), "-H", str(page_h),
         pdf_path, "-"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt op pagina {page}: {result.stderr}")
    return result.stdout


def _clean_lines(text: str) -> str:
    """Verwijder ruis: paginanummers, URL, form feeds, decoratieve lijnen."""
    lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if re.match(r"^\d+$", stripped):  # paginanummer
            continue
        if re.match(r"^(net|fisconet|www\.).*", stripped, re.I):  # URL-fragment
            continue
        if stripped in ("——", "–", "—", "–––"):
            continue
        if stripped == "\x0c":
            continue
        lines.append(line)
    return "\n".join(lines)


def _normalize_whitespace(text: str) -> str:
    """Normaliseert meerdere spaties tot één (artefact van kolom-extractie)."""
    lines = []
    for line in text.split("\n"):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        normalized = re.sub(r"  +", " ", stripped)
        lines.append(" " * min(indent, 4) + normalized)
    return "\n".join(lines)


def _to_markdown(text: str) -> str:
    """Zet koppen en artikelnummers om naar markdown-structuur."""
    lines = text.split("\n")
    md_lines: list[str] = []
    prev_empty = False

    for line in lines:
        stripped = line.strip()

        art_match = re.match(r"^Art\.\s+(\d+[\w/]*)$", stripped)
        if art_match:
            art_num = art_match.group(1)
            if not prev_empty:
                md_lines.append("")
            md_lines.append(f"## Art. {art_num}")
            md_lines.append("")
            prev_empty = True
            continue

        if re.match(r"^TITEL\s+[IVXLC]+\.?\s*[-–]", stripped):
            if not prev_empty:
                md_lines.append("")
            md_lines.append(f"### {stripped}")
            md_lines.append("")
            prev_empty = True
            continue

        if re.match(r"^HOOFDSTUK\s+", stripped):
            if not prev_empty:
                md_lines.append("")
            md_lines.append(f"#### {stripped}")
            md_lines.append("")
            prev_empty = True
            continue

        if re.match(r"^(Afdeling|Onderafdeling)\s+", stripped):
            if not prev_empty:
                md_lines.append("")
            md_lines.append(f"##### {stripped}")
            md_lines.append("")
            prev_empty = True
            continue

        if not stripped:
            if not prev_empty:
                md_lines.append("")
            prev_empty = True
            continue

        md_lines.append(stripped)
        prev_empty = False

    return "\n".join(md_lines)


def extract(cfg: dict, source_name: str) -> str:
    """Extract WIB92 NL-kolom → gestructureerde markdown body (zonder frontmatter)."""
    raw_rel = cfg.get("raw") or "resources/raw/wetteksten/WIB92.pdf"
    pdf_path = ROOT / raw_rel
    if not pdf_path.exists():
        raise FileNotFoundError(f"WIB92 PDF niet gevonden: {pdf_path}")

    start_page = cfg.get("start_page") or _START_PAGE
    end_page = cfg.get("end_page") or _END_PAGE
    col_x = cfg.get("col_x") or _COL_X
    col_w = cfg.get("col_w") or _COL_W
    page_h = cfg.get("page_h") or _PAGE_H

    pages: list[str] = []
    for page in range(start_page, end_page + 1):
        raw = _extract_page(str(pdf_path), page, col_x, col_w, page_h)
        pages.append(_clean_lines(raw))

    full_text = "\n".join(pages)
    full_text = fix_broken_words(full_text)
    full_text = _normalize_whitespace(full_text)
    full_text = _to_markdown(full_text)
    full_text = re.sub(r"\n{3,}", "\n\n", full_text)
    full_text = merge_wrapped_lines(full_text)
    full_text = merge_heading_continuations(full_text)
    return full_text
