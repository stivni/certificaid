"""Library voor norm-PDF-extractie en post-processing.

Bundelt logica uit drie historische scripts:

  - `tools/etl/extract_norm_twocolumn.py` → :func:`extract_nl_column`
  - `tools/etl/inject_norm_headings.py`   → :func:`inject_norm_headings`
  - `tools/etl/fix_norm_artefacts.py`     → :func:`fix_norm_artefacts`

De originele scripts blijven werken (CLI-entrypoints) en delen tijdens
deze tussenfase hun zware logica met deze module via re-exports. In een
latere fase wordt die logica volledig hier ondergebracht en de scripts
omgezet tot dunne CLI-wrappers.

Geen filesystem-IO in deze module behalve PDF-read in :func:`extract_nl_column`.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

# ─── Re-exports uit de historische scripts ─────────────────────────────────
#
# We importeren de (interne) helpers expliciet uit de drie ETL-scripts. Dat
# vermijdt code-duplicatie tijdens de tussenfase: zolang de bron-scripts nog
# bestaan blijven ze single source of truth. Wanneer ze geschrapt worden
# (fase D) verhuist de implementatie naar deze module zelf.

from tools.etl.extract_norm_twocolumn import (  # noqa: E402
    _RE_FRENCH_ACCENTS,
    _RE_FRENCH_MARKER,
    _RE_FRENCH_START,
    _RE_NL_ACCENTED_WORDS,
    _RE_NL_ONLY_WORDS,
    _is_likely_french_line,
    _strip_fr_lines_from_nl_block,
    clean_block_text,
    extract_bilingual,
    is_page_noise,
    merge_intra_block_soft_wraps,
)
from tools.etl.fix_norm_artefacts import (  # noqa: E402
    remove_inline_page_numbers,
    replace_ocr_lab,
    strip_form_feeds,
    strip_toc_dot_lines,
)
from tools.etl.inject_norm_headings import inject_headings  # noqa: E402


# ─── Publieke API ──────────────────────────────────────────────────────────


_DEFAULT_COLUMN_SPLIT = 415
"""Standaard x-grens voor de NL-kolom in BeExcellent-PDFs (landschap A4)."""


def extract_nl_column(
    pdf_path: str | Path,
    *,
    column_x_split: int | None = None,
    start_page: int = 1,
    end_page: int | None = None,
) -> str:
    """Extraheer de NL-kolom uit een tweetalige BeExcellent-PDF.

    Wikkelt :func:`tools.etl.extract_norm_twocolumn.extract_bilingual` met:

    - soft-wrap merge binnen blokken
    - filteren van Franse regels op basis van diacritics + functiewoord-tellers

    Parameters
    ----------
    pdf_path
        Pad naar de PDF (str of Path).
    column_x_split
        x-coördinaat (in PDF-punten) die de NL- en FR-kolom scheidt.
        ``None`` → gebruik de default (215 voor portrait, 415 voor landscape
        BeExcellent-A4). Wordt rechtstreeks aan ``extract_bilingual`` doorgegeven.
    start_page, end_page
        Pagina-bereik (1-based, inclusief). Op dit moment ondersteunt
        ``extract_bilingual`` geen page-slicing; deze parameters worden
        bewaard voor toekomstig gebruik (raise als gebruiker iets anders
        meegeeft dan de default).

    Returns
    -------
    str
        De NL-tekst als markdown-body (zonder frontmatter).
    """
    pdf_path = Path(pdf_path)
    split = float(column_x_split) if column_x_split is not None else float(_DEFAULT_COLUMN_SPLIT)

    if start_page != 1 or end_page is not None:
        # Niet ondersteund in de huidige bron-implementatie. Liever expliciet
        # falen dan stilzwijgend de hele PDF lezen.
        raise NotImplementedError(
            "Pagina-slicing is nog niet ondersteund in extract_nl_column. "
            "Verwerk de hele PDF en knip post-hoc in de body."
        )

    return extract_bilingual(pdf_path, split)


def inject_norm_headings(body: str, *, filename: str = "") -> tuple[str, int]:
    """Promoot bold-titels en structuurlabels naar ``##``-headings.

    Wikkelt :func:`tools.etl.inject_norm_headings.inject_headings`.

    Parameters
    ----------
    body
        Markdown-body (zonder frontmatter).
    filename
        Optioneel — bestandsnaam (bv. ``"ITAA-norm-aww-geconsolideerd.md"``).
        Activeert file-specifieke overrides voor sectie-titels die in de
        NL-kolom-extractie verloren zijn gegaan (two-column glitch).

    Returns
    -------
    tuple
        ``(nieuwe_body, aantal_promoties)`` — de telling geeft het verschil
        in aantal ``##``-headings vóór en na injectie.
    """
    if not body:
        return body, 0

    before = _count_h2(body)
    new_body = inject_headings(body, filename=filename, use_bilingual=False)
    after = _count_h2(new_body)
    return new_body, max(0, after - before)


def fix_norm_artefacts(body: str) -> tuple[str, list[str]]:
    """Verwijder veelvoorkomende artefacten in genormaliseerde norm-MDs.

    Combineert een vaste set generieke fixes:

    - :func:`strip_form_feeds` — verwijder ``\\x0c`` form-feed characters
    - :func:`remove_inline_page_numbers` — losse ``1/4``- en ``Page N of N``-regels
    - :func:`replace_ocr_lab` — OCR-fout ``lAB``→``IAB`` enz.
    - :func:`strip_toc_dot_lines` — TOC-stippenregels

    Parameters
    ----------
    body
        Markdown-body (zonder frontmatter).

    Returns
    -------
    tuple
        ``(nieuwe_body, beschrijvingen)`` waarbij ``beschrijvingen`` een
        lijst is van human-readable strings per fix die toegepast werd.
    """
    fixes: list[tuple[str, Callable[[str], tuple[str, object]]]] = [
        ("strip_form_feeds", strip_form_feeds),
        ("remove_inline_page_numbers", remove_inline_page_numbers),
        ("replace_ocr_lab", replace_ocr_lab),
        ("strip_toc_dot_lines", strip_toc_dot_lines),
    ]

    descriptions: list[str] = []
    new_body = body
    for _name, fn in fixes:
        new_body, result = fn(new_body)
        # FixResult heeft .applied + .note attributen; we documenteren
        # alleen toegepaste fixes.
        applied = getattr(result, "applied", False)
        note = getattr(result, "note", "")
        if applied:
            descriptions.append(note or _name)

    return new_body, descriptions


# ─── Internal ──────────────────────────────────────────────────────────────


_RE_H2 = re.compile(r"(?m)^##\s+\S")


def _count_h2(text: str) -> int:
    """Tel het aantal ``##``-headings in `text`."""
    return len(_RE_H2.findall(text))


__all__ = [
    "extract_nl_column",
    "inject_norm_headings",
    "fix_norm_artefacts",
    # Re-exports voor tests + power-users
    "_is_likely_french_line",
    "_strip_fr_lines_from_nl_block",
    "merge_intra_block_soft_wraps",
    "clean_block_text",
    "is_page_noise",
    "_RE_FRENCH_ACCENTS",
    "_RE_FRENCH_MARKER",
    "_RE_FRENCH_START",
    "_RE_NL_ACCENTED_WORDS",
    "_RE_NL_ONLY_WORDS",
    "strip_form_feeds",
    "remove_inline_page_numbers",
    "replace_ocr_lab",
    "strip_toc_dot_lines",
    "inject_headings",
]
