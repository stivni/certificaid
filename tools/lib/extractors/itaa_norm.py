"""ITAA-norm extractor voor de collection-pipeline (ADR-005 §2 + collections-uitbreiding).

Inputs:
    cfg = {
        "bron-pdf": "<lokaal pad>"   # voorkeur — wijst direct naar raw PDF
        "online":   "<URL>"          # fallback — vereist download (nog niet ondersteund)
        ...                          # andere frontmatter-velden uit de huidige MD
    }
    source_name = bestand-stem (bv. "ITAA-norm-effectennorm")

Output:
    string met de markdown-body (geen frontmatter — de orchestrator bouwt die).

De PDF-route gebruikt :func:`tools.lib.normen_extractie.extract_nl_column` voor
twee-kolom NL/FR-PDFs, gevolgd door :func:`fix_norm_artefacts` en
:func:`inject_norm_headings`. Voor items zonder lokale PDF wordt
``NotImplementedError`` opgegooid; de orchestrator vangt dit en skipt het item.

Voor MD-bestanden waarvan we de PDF-mapping kennen (via
``extract_norm_twocolumn.KNOWN_PDFS``) kan de PDF-pad automatisch geresolveerd
worden — zo werken bestaande items zonder cfg-aanpassing.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from tools.lib.normen_extractie import (
    extract_nl_column,
    fix_norm_artefacts,
    inject_norm_headings,
)


def _resolve_pdf_path(cfg: dict, source_name: str) -> Path | None:
    """Bepaal de raw PDF-locatie voor een norm-item.

    Voorkeursvolgorde:
      1. Expliciete ``bron-pdf:`` (relatief t.o.v. repo-root) of ``raw:`` in cfg.
      2. KNOWN_PDFS-mapping in extract_norm_twocolumn (legacy mapping per MD-naam).
    """
    from tools.etl.extract_norm_twocolumn import KNOWN_PDFS, ROOT

    raw = cfg.get("bron-pdf") or cfg.get("raw")
    if raw:
        p = Path(raw)
        if not p.is_absolute():
            p = ROOT / raw
        return p if p.exists() else None

    # Fallback: KNOWN_PDFS mapped op MD-bestandsnaam.
    md_name = f"{source_name}.md"
    entry = KNOWN_PDFS.get(md_name)
    if entry:
        p = entry["pdf"]
        return p if p.exists() else None

    return None


def _resolve_column_split(cfg: dict, source_name: str) -> int | None:
    """Lees column-split uit cfg of KNOWN_PDFS."""
    from tools.etl.extract_norm_twocolumn import KNOWN_PDFS

    if "column_split" in cfg:
        return int(cfg["column_split"])

    md_name = f"{source_name}.md"
    entry = KNOWN_PDFS.get(md_name)
    if entry and "column_split" in entry:
        return int(entry["column_split"])

    return None


_KNOWN_LAYOUT_TYPES = {"nl-singlecol", "bilingual", "vereisten", "nl-docx"}


def _resolve_type(cfg: dict, source_name: str) -> str | None:
    """Lees layout-type-hint uit cfg of KNOWN_PDFS.

    Het document-eigen ``type:`` veld in de frontmatter (bv. ``type: norm``)
    is een domeinvlag, geen layout-routing — daarom matchen we eerst tegen
    ``KNOWN_PDFS`` en accepteren we cfg["type"] alleen als het een bekend
    layout-type is.
    """
    from tools.etl.extract_norm_twocolumn import KNOWN_PDFS

    md_name = f"{source_name}.md"
    entry = KNOWN_PDFS.get(md_name)
    if entry and "type" in entry:
        return str(entry["type"])

    cfg_type = cfg.get("type")
    if cfg_type and str(cfg_type) in _KNOWN_LAYOUT_TYPES:
        return str(cfg_type)

    return None


def _extract_docx_body(docx_path: Path) -> str:
    """Lees alle paragrafen uit een DOCX en lever plain-text body.

    We gebruiken python-docx om elke paragraaf op te halen. Style-namen
    die eruit zien als heading (``Heading 1``, ``Heading 2``, ``Kop 1``,
    ``Titel``, …) krijgen een markdown-prefix zodat ``inject_norm_headings``
    de structuur verder kan oppakken. Lege paragrafen worden bewaard als
    paragraaf-scheider.
    """
    try:
        import docx  # type: ignore  # python-docx
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "python-docx ontbreekt — installeer met `pip install python-docx`"
        ) from e

    doc = docx.Document(str(docx_path))
    out_lines: list[str] = []
    for para in doc.paragraphs:
        text = (para.text or "").strip()
        style_name = (para.style.name or "").lower() if para.style is not None else ""
        if not text:
            out_lines.append("")
            continue
        # Heading-styles → markdown heading-prefix
        if style_name.startswith("heading ") or style_name.startswith("kop "):
            # Probeer het niveau (1..6) te bepalen
            tail = style_name.split(" ", 1)[1] if " " in style_name else ""
            try:
                lvl = max(1, min(6, int(tail.strip())))
            except (ValueError, AttributeError):
                lvl = 2
            out_lines.append(f"{'#' * lvl} {text}")
        elif style_name in {"title", "titel"}:
            out_lines.append(f"# {text}")
        else:
            out_lines.append(text)

    body = "\n".join(out_lines)
    # Comprimeer 3+ blanco regels naar dubbele blanco
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def extract(cfg: dict, source_name: str) -> str:
    """Re-extract een ITAA-norm-PDF naar markdown-body.

    Raised:
      - NotImplementedError als alleen een ``online:`` URL bekend is (geen lokale PDF).
      - FileNotFoundError als de cfg een PDF aanduidt die niet bestaat.
    """
    pdf_path = _resolve_pdf_path(cfg, source_name)
    if pdf_path is None:
        # Bepaal de juiste foutsoort op basis van wat er wél in cfg stond.
        if cfg.get("online") or cfg.get("url"):
            raise NotImplementedError(
                f"{source_name}: alleen online-URL bekend, geen lokale PDF — "
                f"download-pad is nog niet ondersteund in de collection-extractor."
            )
        raise FileNotFoundError(
            f"{source_name}: geen PDF-pad gevonden (cfg.bron-pdf={cfg.get('bron-pdf')!r}, "
            f"geen mapping in KNOWN_PDFS)."
        )

    if not pdf_path.exists():
        raise FileNotFoundError(f"{source_name}: PDF bestaat niet op {pdf_path}")

    type_hint = _resolve_type(cfg, source_name)

    if type_hint == "nl-singlecol":
        # NL-only enkelkolom-PDF: gebruik pdftotext -layout direct, omzeil
        # de bilingual-blok-decompositie (die FR-false-positives genereert).
        body = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    elif type_hint == "nl-docx":
        # NL-only DOCX: gebruik python-docx voor paragraph-extractie.
        # Levert plain text op, daarna lopen fix_norm_artefacts en
        # inject_norm_headings er nog over voor heading-promotie.
        body = _extract_docx_body(pdf_path)
    else:
        column_split = _resolve_column_split(cfg, source_name)
        # 1. NL-kolom uit twee-kolom PDF
        body = extract_nl_column(pdf_path, column_x_split=column_split)

    # 2. Fix-artefacten (form-feed, page-numbers, OCR-fixes, TOC-stippen)
    body, _fixes = fix_norm_artefacts(body)

    # 3. Promote bold-titels en structuurlabels naar ##-headings
    body, _n_headings = inject_norm_headings(body)

    return body
