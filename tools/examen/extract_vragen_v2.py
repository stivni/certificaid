"""Vragen-extractie v2: structured blokken (tekst + tabel) per vraag.

ADR-021. Vervangt v1 (flat extract_text). Per page worden tabellen gedetecteerd
via pdfplumber.find_tables() en behouden als typed blokken. Tekst rond de
tabellen wordt gereconstrueerd via extract_words() met filtering op de
tabel-bboxes.

Output: data/programma/examen_vragen/<examen>.json met schema_versie: "2.0",
per vraag (en waar mogelijk per subvraag) een veld vraagtekst_blokken[].

Backward-compat: vraagtekst blijft populated (concat van blokken; tabellen
gerenderd als markdown-tabel).

CLI:
    python3 -m tools.examen.extract_vragen_v2                # alle examens
    python3 -m tools.examen.extract_vragen_v2 --examen 2014-1
    python3 -m tools.examen.extract_vragen_v2 --dry-run     # geen schrijf-actie
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import pdfplumber

from tools.examen._sub_vragen_splitter import splits_in_sub_vragen
from tools.examen._vraagtekst_normalisatie import normaliseer as normaliseer_vraagtekst
from tools.examen.extract_vragen import (
    EXAMEN_VAK_PATRONEN,
    detect_vraagtype,
    extract_themas,
    extract_wetsrefs,
    parse_2024_1,
    parse_opties,
    parse_subvragen,
    strip_studocu,
)
from tools.examen import extract_vragen_bibf

TOOL_ID = "vragen-extractie-v2"
PDF_LIB = "pdfplumber"
SCHEMA_VERSIE = "2.0"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
PDF_DIR = BASE_DIR / "resources" / "raw" / "voorbeeldexamens"

# Default conservatieve pdfplumber-tabel-settings. Mag per examen overruled
# worden via EXAMEN_CONFIGS_V2[examen_id]["pdfplumber_table_settings"].
DEFAULT_TABLE_SETTINGS: dict[str, Any] = {
    # Default-strategy = "lines" werkt goed op de ITAA-PDFs (gridlines aanwezig
    # rond tabellen). pdfplumber's default ("lines" v/h) is voldoende
    # conservatief voor de huidige inventaris.
}

# Minimale tabel-eisen (post-extract validatie)
TABEL_MIN_RIJEN = 2
TABEL_MIN_KOLOMMEN = 2
TABEL_MAX_LEGE_FRACTIE = 0.30  # > 30% lege cellen → verwerpen

EXAMEN_CONFIGS_V2: dict[str, dict[str, Any]] = {
    "2013-1": {
        "jaar": 2013,
        "sessie": 1,
        "pdf_bestand": "2013-1.pdf",
        "totaal_punten": 150,
        "parser": "itaa_standaard",
    },
    "2013-2": {
        "jaar": 2013,
        "sessie": 2,
        "pdf_bestand": "2013-2.pdf",
        "totaal_punten": 150,
        "parser": "itaa_standaard",
    },
    "2014-1": {
        "jaar": 2014,
        "sessie": 1,
        "pdf_bestand": "2014-1.pdf",
        "totaal_punten": 150,
        "parser": "itaa_standaard",
    },
    "2015-1": {
        "jaar": 2015,
        "sessie": 1,
        "pdf_bestand": "2015_1_-_bekwaamheidsexamen_ac_1.pdf",
        "totaal_punten": 150,
        "parser": "itaa_standaard",
    },
    "2024-1": {
        "jaar": 2024,
        "sessie": 1,
        "pdf_bestand": "Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf",
        "totaal_punten": None,
        "parser": "itaa_2024",
    },
    "2003-bibf": {
        "jaar": 2003,
        "sessie": 1,
        "pdf_bestand": "2003-bibf.pdf",
        "totaal_punten": 100,
        "parser": "bibf_anchor",
        "vraag_defs": "VRAGEN_2003",
        "has_answers": False,
    },
    "2008-bibf": {
        "jaar": 2008,
        "sessie": 1,
        "pdf_bestand": "2008-bibf.pdf",
        "totaal_punten": 100,
        "parser": "bibf_anchor",
        "vraag_defs": "VRAGEN_2008",
        "has_answers": True,
    },
}


# ---------------------------------------------------------------------------
# Datatypes
# ---------------------------------------------------------------------------

@dataclass
class Blok:
    """Eén pagina-blok (tekst of tabel) met positie."""

    type: str  # "tekst" | "tabel"
    inhoud: Optional[str] = None  # voor tekst
    rows: Optional[list[list[str]]] = None  # voor tabel
    headers: Optional[list[str]] = None  # voor tabel (eerste rij als header-vermoeden)
    bron_bbox: Optional[tuple[float, float, float, float]] = None  # (x0, top, x1, bottom)
    page: int = 0
    top_y: float = 0.0  # voor sortering binnen page


# ---------------------------------------------------------------------------
# Tabel-validatie
# ---------------------------------------------------------------------------

def _normalize_cell(cell: Any) -> str:
    if cell is None:
        return ""
    return str(cell).strip()


def tabel_is_geldig(rows: list[list[str]]) -> bool:
    """Validate of een tabel-extractie aan minimum-eisen voldoet.

    Eisen:
    - ≥ 2 rijen, ≥ 2 kolommen
    - Eerste rij vrijwel volledig gevuld (header-vermoeden) OF
      < 70 % van alle data-cellen leeg
    Doelstelling: invul-tabellen (intentioneel grotendeels leeg, maar met
    duidelijke header) niet verwerpen.
    """
    if len(rows) < TABEL_MIN_RIJEN:
        return False
    n_kol = max((len(r) for r in rows), default=0)
    if n_kol < TABEL_MIN_KOLOMMEN:
        return False
    totaal_cellen = sum(len(r) for r in rows)
    if totaal_cellen == 0:
        return False

    eerste_rij = rows[0]
    # Header-rij gevuld? (≥ 80 % cellen niet-leeg) → intentionele invul-tabel toegestaan
    if eerste_rij:
        gevuld_in_header = sum(1 for c in eerste_rij if c)
        header_gevuld_fractie = gevuld_in_header / len(eerste_rij)
    else:
        header_gevuld_fractie = 0.0

    if header_gevuld_fractie >= 0.8:
        return True

    # Anders: standaard ADR-021-regel — < 70 % leeg in alle data-cellen
    lege_cellen = sum(1 for r in rows for c in r if not c)
    if lege_cellen / totaal_cellen > (1.0 - TABEL_MAX_LEGE_FRACTIE):
        return False
    return True


def pad_rijen_naar_zelfde_lengte(rows: list[list[str]]) -> list[list[str]]:
    """Maak alle rijen even lang door rechts op te vullen met lege strings."""
    if not rows:
        return rows
    n_kol = max(len(r) for r in rows)
    return [r + [""] * (n_kol - len(r)) for r in rows]


# ---------------------------------------------------------------------------
# Per-page extractie
# ---------------------------------------------------------------------------

def _woord_in_bbox(woord: dict, bbox: tuple[float, float, float, float]) -> bool:
    """True als woord-positie binnen tabel-bbox valt."""
    x0, top, x1, bottom = bbox
    wx0 = woord["x0"]
    wx1 = woord["x1"]
    wtop = woord["top"]
    wbottom = woord["bottom"]
    # overlap-check: woord-midpoint binnen bbox
    mx = (wx0 + wx1) / 2
    my = (wtop + wbottom) / 2
    return x0 <= mx <= x1 and top <= my <= bottom


def _woorden_naar_regels(woorden: list[dict], y_tolerantie: float = 3.0) -> list[dict]:
    """Cluster woorden in regels op basis van top-y. Geeft list[{top, text}]."""
    if not woorden:
        return []
    # Sorteer eerst op top-y, dan x0
    woorden_gesorteerd = sorted(woorden, key=lambda w: (w["top"], w["x0"]))
    regels: list[dict] = []
    huidige_top: Optional[float] = None
    huidige_woorden: list[dict] = []
    for w in woorden_gesorteerd:
        if huidige_top is None or abs(w["top"] - huidige_top) <= y_tolerantie:
            huidige_woorden.append(w)
            if huidige_top is None:
                huidige_top = w["top"]
        else:
            huidige_woorden.sort(key=lambda x: x["x0"])
            regels.append({
                "top": huidige_top,
                "text": " ".join(x["text"] for x in huidige_woorden),
            })
            huidige_top = w["top"]
            huidige_woorden = [w]
    if huidige_woorden:
        huidige_woorden.sort(key=lambda x: x["x0"])
        regels.append({
            "top": huidige_top or 0.0,
            "text": " ".join(x["text"] for x in huidige_woorden),
        })
    return regels


def extract_blokken_uit_page(
    page: "pdfplumber.page.Page",
    page_nr: int,
    table_settings: Optional[dict[str, Any]] = None,
) -> tuple[list[Blok], list[dict]]:
    """Extract typed blokken (tekst + tabel) uit één PDF-page.

    Returns:
        (blokken, verworpen_tabellen) — verworpen_tabellen is een lijst dicts
        met diagnostics voor validatie-failures.
    """
    blokken: list[Blok] = []
    verworpen: list[dict] = []

    settings = dict(table_settings or {}) or None
    try:
        found_tables = page.find_tables(table_settings=settings) if settings else page.find_tables()
    except Exception:
        found_tables = []

    geldige_tabel_bboxes: list[tuple[float, float, float, float]] = []
    for tab in found_tables:
        try:
            raw_rows = tab.extract() or []
        except Exception:
            raw_rows = []
        rows = [[_normalize_cell(c) for c in r] for r in raw_rows]
        rows = pad_rijen_naar_zelfde_lengte(rows)
        if not tabel_is_geldig(rows):
            verworpen.append({
                "page": page_nr,
                "bbox": tab.bbox,
                "reden": "validatie_faalt",
                "n_rijen": len(rows),
                "n_kolommen": max((len(r) for r in rows), default=0),
            })
            continue
        # Eerste rij als headers-vermoeden: ≥ 2/3 cellen non-empty
        headers: Optional[list[str]] = None
        if rows:
            eerste = rows[0]
            n_gevuld = sum(1 for c in eerste if c)
            if n_gevuld >= max(2, int(0.66 * len(eerste))):
                headers = eerste
                data_rows = rows[1:]
            else:
                data_rows = rows
        else:
            data_rows = []
        blokken.append(Blok(
            type="tabel",
            rows=data_rows,
            headers=headers,
            bron_bbox=tuple(tab.bbox),
            page=page_nr,
            top_y=tab.bbox[1],
        ))
        geldige_tabel_bboxes.append(tuple(tab.bbox))

    # Words → filter buiten tabellen → regels → tekst-blokken gesplitst rond tabel-y-ranges
    try:
        words = page.extract_words(use_text_flow=False, keep_blank_chars=False)
    except Exception:
        words = []

    woorden_buiten_tabel = [
        w for w in words if not any(_woord_in_bbox(w, b) for b in geldige_tabel_bboxes)
    ]
    regels = _woorden_naar_regels(woorden_buiten_tabel)

    # Splits regels rond tabel-y-ranges
    if not geldige_tabel_bboxes:
        # Eén groot tekst-blok
        if regels:
            tekst = "\n".join(r["text"] for r in regels)
            blokken.append(Blok(
                type="tekst",
                inhoud=tekst,
                page=page_nr,
                top_y=regels[0]["top"],
            ))
    else:
        # Sorteer tabel-bboxes op top-y
        bboxes_sorted = sorted(geldige_tabel_bboxes, key=lambda b: b[1])
        y_grenzen = [(b[1], b[3]) for b in bboxes_sorted]
        # Verdeel regels in segmenten: voor eerste tabel, tussen tabellen, na laatste
        segmenten: list[list[dict]] = [[] for _ in range(len(y_grenzen) + 1)]
        for r in regels:
            y = r["top"]
            idx = 0
            for i, (top, bottom) in enumerate(y_grenzen):
                if y < top:
                    idx = i
                    break
                elif top <= y <= bottom:
                    idx = -1  # binnen tabel, sla over
                    break
                else:
                    idx = i + 1
            if idx == -1:
                continue
            segmenten[idx].append(r)
        for seg in segmenten:
            if not seg:
                continue
            tekst = "\n".join(r["text"] for r in seg)
            blokken.append(Blok(
                type="tekst",
                inhoud=tekst,
                page=page_nr,
                top_y=seg[0]["top"],
            ))

    # Sorteer alle blokken op top_y
    blokken.sort(key=lambda b: b.top_y)
    return blokken, verworpen


# ---------------------------------------------------------------------------
# Blok-rendering (concat naar markdown voor backward-compat)
# ---------------------------------------------------------------------------

def render_tabel_als_markdown(blok: Blok) -> str:
    """Render een tabel-blok als plain markdown-tabel."""
    headers = blok.headers
    rows = blok.rows or []
    if not rows and not headers:
        return ""
    if headers:
        n_kol = len(headers)
        data = rows
    else:
        n_kol = max((len(r) for r in rows), default=0)
        # Synthetische headers (lege)
        headers = [""] * n_kol
        data = rows
    # Pad data rijen
    data = [r + [""] * (n_kol - len(r)) for r in data]
    regel_hdr = "| " + " | ".join(headers) + " |"
    regel_sep = "|" + "|".join(["---"] * n_kol) + "|"
    regels_data = ["| " + " | ".join(r) + " |" for r in data]
    return "\n".join([regel_hdr, regel_sep, *regels_data])


def concat_blokken_naar_vraagtekst(blokken: list[dict]) -> str:
    """Bouw flat `vraagtekst` op uit blokken-list (markdown voor tabellen)."""
    parts: list[str] = []
    for b in blokken:
        if b["type"] == "tekst":
            parts.append(b.get("inhoud", "").strip())
        elif b["type"] == "tabel":
            tabel_blok = Blok(
                type="tabel",
                rows=b.get("rows", []),
                headers=b.get("headers"),
            )
            parts.append(render_tabel_als_markdown(tabel_blok))
        elif b["type"] == "formule":
            parts.append(b.get("inhoud", ""))
        elif b["type"] == "figuur":
            cap = b.get("caption") or ""
            parts.append(f"[figuur: {cap}]" if cap else "[figuur]")
    return "\n\n".join(p for p in parts if p)


def blok_naar_dict(blok: Blok) -> dict:
    """Serialize Blok naar JSON-vriendelijke dict (geen positie-velden)."""
    if blok.type == "tekst":
        return {"type": "tekst", "inhoud": (blok.inhoud or "").strip()}
    elif blok.type == "tabel":
        d: dict = {"type": "tabel", "rows": blok.rows or []}
        if blok.headers:
            d["headers"] = blok.headers
        if blok.bron_bbox:
            d["bron_bbox"] = {
                "page": blok.page,
                "x0": blok.bron_bbox[0],
                "top": blok.bron_bbox[1],
                "x1": blok.bron_bbox[2],
                "bottom": blok.bron_bbox[3],
            }
        return d
    else:
        return {"type": blok.type, "inhoud": blok.inhoud or ""}


# ---------------------------------------------------------------------------
# Vraag-splitsing (op concat-tekst van alle blokken)
# ---------------------------------------------------------------------------

VRAAG_HEADER_PATROON = re.compile(
    r"Vraag\s+(\d+[a-z]?)\s*[….]{0,3}\s*(?:/\s*([\d,]+)\s*punt(?:en)?)?",
    re.IGNORECASE,
)

WATERMARK_LINE_PATRONEN = [
    re.compile(r"^lOMoARcPSD\|"),
    re.compile(r"^Downloaded by"),
    re.compile(r"^Studocu"),
    re.compile(r"^Scan to open"),
    re.compile(r"^SSccaann"),
    re.compile(r"^SSttuuddooccuu"),
]


def filter_watermark_uit_blok(blok: Blok) -> Blok:
    """Strip watermerk-regels uit een tekst-blok."""
    if blok.type != "tekst" or not blok.inhoud:
        return blok
    schone_regels: list[str] = []
    for regel in blok.inhoud.split("\n"):
        if any(p.search(regel) for p in WATERMARK_LINE_PATRONEN):
            continue
        schone_regels.append(regel)
    blok.inhoud = "\n".join(schone_regels).strip()
    return blok


@dataclass
class VraagSegment:
    """Een vraag-segment bestaande uit een geordende reeks blokken."""

    vraag_nr: str
    punten: Optional[float]
    blokken: list[Blok] = field(default_factory=list)
    pdf_pagina: int = 1


def splits_blokken_in_vragen(blokken: list[Blok]) -> list[VraagSegment]:
    """Splits geordende blokken in vraag-segmenten op vraag-headers."""
    vragen: list[VraagSegment] = []
    huidige: Optional[VraagSegment] = None

    for blok in blokken:
        if blok.type == "tekst" and blok.inhoud:
            # Zoek vraag-headers in deze tekst
            matches = list(VRAAG_HEADER_PATROON.finditer(blok.inhoud))
            if not matches:
                if huidige is not None:
                    huidige.blokken.append(blok)
                continue
            # Splits tekst rond matches
            cursor = 0
            for m in matches:
                start = m.start()
                # Voorafgaande tekst hoort bij huidige vraag (als er één is)
                if start > cursor and huidige is not None:
                    prefix_tekst = blok.inhoud[cursor:start].strip()
                    if prefix_tekst:
                        huidige.blokken.append(Blok(
                            type="tekst",
                            inhoud=prefix_tekst,
                            page=blok.page,
                            top_y=blok.top_y,
                        ))
                # Start nieuwe vraag
                if huidige is not None:
                    vragen.append(huidige)
                vraag_nr = m.group(1)
                punten = float(m.group(2).replace(",", ".")) if m.group(2) else None
                huidige = VraagSegment(
                    vraag_nr=vraag_nr,
                    punten=punten,
                    blokken=[],
                    pdf_pagina=blok.page,
                )
                cursor = start
            # Resterende tekst na laatste match
            rest = blok.inhoud[cursor:].strip()
            if rest and huidige is not None:
                huidige.blokken.append(Blok(
                    type="tekst",
                    inhoud=rest,
                    page=blok.page,
                    top_y=blok.top_y,
                ))
        else:
            # Niet-tekst (tabel/figuur/formule): hoort bij huidige vraag
            if huidige is not None:
                huidige.blokken.append(blok)
            # Als er nog geen vraag is, gooien we het weg (vóór eerste vraag = header)

    if huidige is not None:
        vragen.append(huidige)
    return vragen


# ---------------------------------------------------------------------------
# Sectie-detectie (om vak_code per vraag te bepalen)
# ---------------------------------------------------------------------------

def detect_vak_per_vraag(
    vragen: list[VraagSegment],
    volledige_tekst: str,
    examen_id: str,
) -> list[tuple[str, str]]:
    """Geef per vraag (vak_code, vak_naam) op basis van sectietitel-posities.

    Een vraag krijgt het vak van de meest recente sectie-header die in de
    volledige-tekst-positie staat vóór de vraag-start.
    """
    if examen_id not in EXAMEN_VAK_PATRONEN:
        return [("onbekend", "Onbekend") for _ in vragen]
    patronen = EXAMEN_VAK_PATRONEN[examen_id]
    sectie_posities: list[tuple[int, str, str]] = []  # (pos, code, naam)
    for patroon, code, naam in patronen:
        for m in re.finditer(patroon, volledige_tekst, re.IGNORECASE):
            sectie_posities.append((m.start(), code, naam))
    sectie_posities.sort(key=lambda x: x[0])

    resultaat: list[tuple[str, str]] = []
    for v in vragen:
        # Bepaal positie van vraag in volledige_tekst (eerste tekst-blok inhoud)
        zoek_fragment = ""
        for b in v.blokken:
            if b.type == "tekst" and b.inhoud:
                zoek_fragment = b.inhoud[:60]
                break
        pos = volledige_tekst.find(f"Vraag {v.vraag_nr}")
        if pos < 0 and zoek_fragment:
            pos = volledige_tekst.find(zoek_fragment)
        if pos < 0:
            pos = 0
        # Laatste sectie vóór pos
        gekozen = ("onbekend", "Onbekend")
        for s_pos, code, naam in sectie_posities:
            if s_pos <= pos:
                gekozen = (code, naam)
            else:
                break
        resultaat.append(gekozen)
    return resultaat


# ---------------------------------------------------------------------------
# Hoofdpipeline
# ---------------------------------------------------------------------------

def _wrap_vraagtekst_als_tekst_blok(vraagtekst: str) -> list[dict]:
    """Wrap een platte vraagtekst-string als één tekst-blok (voor fallback-parsers)."""
    tekst = (vraagtekst or "").strip()
    if not tekst:
        return []
    return [{"type": "tekst", "inhoud": tekst}]


def _extract_examen_v2_itaa_2024(examen_id: str, config: dict[str, Any]) -> dict:
    """V2-extractie voor 2024-1: gebruikt parse_2024_1 + wrap als tekst-blok.

    De 2024-1 PDF heeft vraag-headers in een ander formaat ("1 Vennootschapsrecht"
    i.p.v. "Vraag 1"). Tabel-detectie wordt niet toegepast — vraagteksten zijn
    overwegend zuiver tekstueel.
    """
    pdf_path = PDF_DIR / config["pdf_bestand"]
    pagina_teksten: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        n_pages = len(pdf.pages)
        for page in pdf.pages:
            pagina_teksten.append(page.extract_text() or "")
    vragen_v1 = parse_2024_1(pagina_teksten)
    vragen_records: list[dict] = []
    for v in vragen_v1:
        blokken = _wrap_vraagtekst_als_tekst_blok(v["vraagtekst"])
        record = dict(v)
        record["vraagtekst_blokken"] = blokken
        vragen_records.append(record)
    return {
        "examen_id": examen_id,
        "schema_versie": SCHEMA_VERSIE,
        "jaar": config["jaar"],
        "sessie": config["sessie"],
        "bron_pdf": f"resources/raw/voorbeeldexamens/{config['pdf_bestand']}",
        "totaal_punten": config.get("totaal_punten"),
        "extractie": {
            "tool": TOOL_ID,
            "pdf_lib": PDF_LIB,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "n_vragen": len(vragen_records),
            "n_pages": n_pages,
            "n_tabellen_geaccepteerd": 0,
            "n_tabellen_verworpen": 0,
        },
        "vragen": vragen_records,
    }


def _extract_examen_v2_bibf(examen_id: str, config: dict[str, Any]) -> dict:
    """V2-extractie voor BIBF-examens: gebruikt anchor-extractie + wrap als tekst-blok.

    BIBF-vragen zijn overwegend tekstueel. Tabellen die voorkomen (zelden)
    worden niet als gestructureerde blokken behandeld in v2.0 — voldoende
    voor backward-compat met de bestaande BIBF-vraagteksten.
    """
    vraag_defs_naam = config["vraag_defs"]
    vraag_defs = getattr(extract_vragen_bibf, vraag_defs_naam)
    has_answers = config["has_answers"]
    doc = extract_vragen_bibf.process_examen(
        examen_id=examen_id,
        pdf_filename=config["pdf_bestand"],
        jaar=config["jaar"],
        sessie=config["sessie"],
        totaal_punten=config["totaal_punten"],
        vraag_defs=vraag_defs,
        has_answers=has_answers,
    )
    doc["schema_versie"] = SCHEMA_VERSIE
    doc["extractie"]["tool"] = TOOL_ID
    doc["extractie"]["n_tabellen_geaccepteerd"] = 0
    doc["extractie"]["n_tabellen_verworpen"] = 0
    for v in doc["vragen"]:
        v["vraagtekst_blokken"] = _wrap_vraagtekst_als_tekst_blok(v.get("vraagtekst", ""))
    return doc


def extract_examen_v2(examen_id: str, config: dict[str, Any]) -> dict:
    parser = config.get("parser", "itaa_standaard")
    if parser == "itaa_2024":
        return _extract_examen_v2_itaa_2024(examen_id, config)
    if parser == "bibf_anchor":
        return _extract_examen_v2_bibf(examen_id, config)
    # Default: itaa_standaard
    pdf_path = PDF_DIR / config["pdf_bestand"]
    table_settings = config.get("pdfplumber_table_settings") or DEFAULT_TABLE_SETTINGS
    if not table_settings:
        table_settings = None

    alle_blokken: list[Blok] = []
    pagina_teksten: list[str] = []
    n_pages = 0
    verworpen_totaal: list[dict] = []
    n_tabellen_geaccepteerd = 0

    with pdfplumber.open(pdf_path) as pdf:
        n_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            blokken, verworpen = extract_blokken_uit_page(page, i, table_settings)
            blokken = [filter_watermark_uit_blok(b) for b in blokken]
            blokken = [b for b in blokken if (b.type != "tekst" or (b.inhoud or "").strip())]
            alle_blokken.extend(blokken)
            verworpen_totaal.extend(verworpen)
            n_tabellen_geaccepteerd += sum(1 for b in blokken if b.type == "tabel")
            # Voor sectie-detectie: gebruik de flat extract_text op deze page
            pagina_teksten.append(page.extract_text() or "")

    volledige_tekst = strip_studocu("\n".join(pagina_teksten))

    # Splits in vragen
    vraag_segmenten = splits_blokken_in_vragen(alle_blokken)
    vak_toewijzing = detect_vak_per_vraag(vraag_segmenten, volledige_tekst, examen_id)

    vragen_records: list[dict] = []
    for idx, (segm, (vak_code, vak_naam)) in enumerate(zip(vraag_segmenten, vak_toewijzing), start=1):
        # Blokken → dicts + concat
        blok_dicts = [blok_naar_dict(b) for b in segm.blokken]
        concat = concat_blokken_naar_vraagtekst(blok_dicts)
        # Normaliseer alleen wanneer er geen tabel-blok bij zit; anders zou de
        # markdown-tabel beschadigd worden door reflow. Normalisatie blijft
        # nuttig voor zuiver-tekstuele vraagtekst.
        bevat_tabel = any(b["type"] == "tabel" for b in blok_dicts)
        if bevat_tabel:
            vraagtekst = concat
        else:
            vraagtekst = normaliseer_vraagtekst(concat)

        # Sub-vragen op concat-tekst (zonder tabel-markup)
        if bevat_tabel:
            # Voor sub-splitsing: alleen tekst-content meegeven
            alleen_tekst = "\n\n".join(
                b.get("inhoud", "").strip()
                for b in blok_dicts
                if b["type"] == "tekst" and b.get("inhoud", "").strip()
            )
            sub_input = normaliseer_vraagtekst(alleen_tekst)
        else:
            sub_input = vraagtekst
        sub_vragen = splits_in_sub_vragen(sub_input)

        # Opties + subvragen (legacy v1-velden, behouden voor compat)
        ruwe_concat = "\n".join(
            b.get("inhoud") or "" for b in blok_dicts if b["type"] == "tekst"
        )
        opties = parse_opties(ruwe_concat)
        subvragen_legacy = parse_subvragen(ruwe_concat)
        vraagtype = detect_vraagtype(ruwe_concat, opties)
        themas = extract_themas(ruwe_concat)
        wets_refs = extract_wetsrefs(ruwe_concat)

        record: dict = {
            "id": f"{examen_id}-vr{idx}",
            "vraag_nr": segm.vraag_nr,
            "punten": segm.punten,
            "pdf_pagina": segm.pdf_pagina,
            "vak_code_in_pdf": vak_code,
            "vak_naam_in_pdf": vak_naam,
            "vraagtype": vraagtype,
            "vraagtekst": vraagtekst,
            "vraagtekst_blokken": blok_dicts,
            "sub_vragen": sub_vragen,
            "correct_antwoord": None,
            "antwoord_motivering": None,
            "themas": themas,
            "wets_verwijzingen": wets_refs,
        }
        if opties:
            record["opties"] = opties
        if subvragen_legacy:
            record["subvragen"] = subvragen_legacy
        vragen_records.append(record)

    output = {
        "examen_id": examen_id,
        "schema_versie": SCHEMA_VERSIE,
        "jaar": config["jaar"],
        "sessie": config["sessie"],
        "bron_pdf": f"resources/raw/voorbeeldexamens/{config['pdf_bestand']}",
        "totaal_punten": config.get("totaal_punten"),
        "extractie": {
            "tool": TOOL_ID,
            "pdf_lib": PDF_LIB,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "n_vragen": len(vragen_records),
            "n_pages": n_pages,
            "n_tabellen_geaccepteerd": n_tabellen_geaccepteerd,
            "n_tabellen_verworpen": len(verworpen_totaal),
        },
        "vragen": vragen_records,
    }
    return output


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examen", type=str, default=None,
                        help="Eén examen-id (bv. 2014-1); default = alle")
    parser.add_argument("--dry-run", action="store_true",
                        help="Schrijf niets weg, print alleen samenvatting")
    args = parser.parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    examens = (
        [(args.examen, EXAMEN_CONFIGS_V2[args.examen])]
        if args.examen
        else list(EXAMEN_CONFIGS_V2.items())
    )

    for examen_id, config in examens:
        print(f"\n[{examen_id}] v2-extractie ...")
        out = extract_examen_v2(examen_id, config)
        n_tab = out["extractie"]["n_tabellen_geaccepteerd"]
        n_rej = out["extractie"]["n_tabellen_verworpen"]
        n_blok = sum(1 for v in out["vragen"] for _ in v["vraagtekst_blokken"])
        n_vr_met_tabel = sum(
            1 for v in out["vragen"] if any(b["type"] == "tabel" for b in v["vraagtekst_blokken"])
        )
        print(f"  → {out['extractie']['n_vragen']} vragen | {n_blok} blokken "
              f"| {n_tab} tabellen geaccepteerd, {n_rej} verworpen "
              f"| {n_vr_met_tabel} vragen met tabel-blok")
        if not args.dry_run:
            out_path = OUTPUT_DIR / f"{examen_id}.json"
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(out, f, ensure_ascii=False, indent=2)
            print(f"    geschreven: {out_path.relative_to(BASE_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
