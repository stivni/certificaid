"""Vraag-isolatie (ADR-024 §2): deterministische segmenten per examenvraag.

Per vraag schrijft deze tool drie artefacten naar
`data/programma/examen_vragen/_segmenten/<examen_id>/<vraag_id>/`:

- `tekst.txt`     — hergebruikt het bestaande `vraagtekst`-veld uit
                    `<examen_id>.json` (geen her-extractie). Subvragen (indien
                    aanwezig) worden achteraan geconcat met
                    `=== subvraag X ===`-headers.
- `pagina_NN.png` — `pdfplumber.Page.to_image(resolution=200)` voor elke
                    pagina in de range (1-geïndexeerd, inclusief).
- `meta.json`     — examen_id, vraag_id, pagina_nummers (list[int]),
                    pdf_bestand, karakter, rationale, bbox_hint=None.

Twee bronnen voor de pagina-range:

1. **POC-subset** (default): leest `_poc_subset.json` met expliciete
   `pagina_van` / `pagina_tot` per vraag.
2. **--alle**: autodetectie uit `<examen>.json`. Per examen worden de vragen
   op `pdf_pagina` gesorteerd; voor vraag i is `pagina_van = pdf_pagina[i]`
   en `pagina_tot = pdf_pagina[i+1] - 1` (of `aantal_pdf_paginas` voor de
   laatste). Als `pdf_pagina[i+1] == pdf_pagina[i]`, valt `pagina_tot` terug
   op `pagina_van` (overlap tussen vragen op dezelfde pagina is OK).
   Vragen zonder `pdf_pagina` worden geskipt met een waarschuwing.
   `aantal_pdf_paginas` wordt uit de PDF zelf gelezen (top-level veld is
   doorgaans `None`).

Idempotent: bestaande PNGs worden niet opnieuw gerenderd; tekst.txt en
meta.json worden alleen herschreven als de inhoud verandert. POC- en
--alle-modus schrijven naar dezelfde paden — runs herschrijven elkaars
output alleen als de inhoud verschilt.

Geen LLM, geen netwerk, geen aanpassingen aan bestaande `<examen>.json`.

CLI:
    python3 -m tools.examen.isoleer_vragen                   # POC-subset
    python3 -m tools.examen.isoleer_vragen --examen 2024-1   # POC-subset, één examen
    python3 -m tools.examen.isoleer_vragen --vraag 2013-1-vr1
    python3 -m tools.examen.isoleer_vragen --alle            # alle vragen, autodetect
    python3 -m tools.examen.isoleer_vragen --alle --examen 2024-1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

import pdfplumber
from PIL import Image

from tools.examen.extract_vragen_v2 import EXAMEN_CONFIGS_V2

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_VRAGEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
SUBSET_PATH = EXAMEN_VRAGEN_DIR / "_poc_subset.json"
SEGMENTEN_DIR = EXAMEN_VRAGEN_DIR / "_segmenten"
PDF_DIR = BASE_DIR / "resources" / "raw" / "voorbeeldexamens"

PNG_RESOLUTIE = 200


def _laad_subset() -> list[dict]:
    return json.loads(SUBSET_PATH.read_text(encoding="utf-8"))["selectie"]


def _laad_examen_json(examen_id: str) -> dict:
    p = EXAMEN_VRAGEN_DIR / f"{examen_id}.json"
    return json.loads(p.read_text(encoding="utf-8"))


def _vind_examen_ids() -> list[str]:
    """Alle examen-IDs die een `<id>.json` in examen_vragen-dir hebben.

    Skipt files met `_`-prefix (zoals `_poc_subset.json`) en `*-labels.json`.
    """
    ids: list[str] = []
    for p in sorted(EXAMEN_VRAGEN_DIR.glob("*.json")):
        naam = p.stem
        if naam.startswith("_"):
            continue
        if naam.endswith("-labels"):
            continue
        ids.append(naam)
    return ids


def _aantal_pdf_paginas(pdf_pad: Path) -> int:
    with pdfplumber.open(str(pdf_pad)) as pdf:
        return len(pdf.pages)


def _autodetect_entries(examen_id: str) -> tuple[list[dict], list[str]]:
    """Bepaal per vraag een (pagina_van, pagina_tot) op basis van pdf_pagina.

    Sorteert vragen op `pdf_pagina` ascending. Voor vraag i op pagina P:
    - pagina_van = P
    - pagina_tot = max(P, next_pdf_pagina - 1) bij volgende vraag
    - pagina_tot = aantal_pdf_paginas voor de laatste

    Vragen zonder `pdf_pagina` (None / ontbrekend) worden geskipt; hun
    vraag_ids komen in de waarschuwingen-lijst terecht.
    """
    cfg = EXAMEN_CONFIGS_V2.get(examen_id)
    if not cfg:
        raise RuntimeError(f"Geen EXAMEN_CONFIGS_V2-entry voor {examen_id}")
    pdf_pad = PDF_DIR / cfg["pdf_bestand"]
    if not pdf_pad.is_file():
        raise FileNotFoundError(f"PDF ontbreekt: {pdf_pad}")

    examen_doc = _laad_examen_json(examen_id)
    vragen = examen_doc.get("vragen", [])

    waarschuwingen: list[str] = []
    bruikbaar: list[tuple[int, str]] = []  # (pdf_pagina, vraag_id)
    for v in vragen:
        vid = v.get("id") or v.get("vraag_id")
        pp = v.get("pdf_pagina")
        if not vid:
            waarschuwingen.append(f"vraag zonder id in {examen_id}.json (skip)")
            continue
        if pp is None:
            waarschuwingen.append(f"{vid}: geen pdf_pagina (skip)")
            continue
        try:
            pp_int = int(pp)
        except (TypeError, ValueError):
            waarschuwingen.append(f"{vid}: pdf_pagina={pp!r} niet-numeriek (skip)")
            continue
        bruikbaar.append((pp_int, vid))

    if not bruikbaar:
        return [], waarschuwingen

    # Stable sort op pdf_pagina; vraag_id als tiebreak voor reproduceerbaarheid
    bruikbaar.sort(key=lambda x: (x[0], x[1]))

    pdf_paginas = _aantal_pdf_paginas(pdf_pad)

    entries: list[dict] = []
    for i, (pp, vid) in enumerate(bruikbaar):
        if i + 1 < len(bruikbaar):
            volgende_pp = bruikbaar[i + 1][0]
            if volgende_pp == pp:
                pagina_tot = pp
            else:
                pagina_tot = max(pp, volgende_pp - 1)
        else:
            pagina_tot = max(pp, pdf_paginas)
        entries.append(
            {
                "examen_id": examen_id,
                "vraag_id": vid,
                "pagina_van": pp,
                "pagina_tot": pagina_tot,
                "karakter": f"auto-isolatie {vid} pagina {pp}"
                if pp == pagina_tot
                else f"auto-isolatie {vid} pagina {pp}-{pagina_tot}",
                "rationale": "alle-vragen-modus",
            }
        )
    return entries, waarschuwingen


def _vind_vraag(examen_doc: dict, vraag_id: str) -> Optional[dict]:
    for v in examen_doc.get("vragen", []):
        if v.get("id") == vraag_id or v.get("vraag_id") == vraag_id:
            return v
    return None


def _subvraag_label(sub: dict, idx: int) -> str:
    return str(sub.get("label") or sub.get("sub_id") or f"sub{idx + 1}")


def _subvraag_tekst(sub: dict) -> str:
    """Render één subvraag naar platte tekst.

    Schema's verschillen per examen-parser:
    - v2-stijl: {label, tekst, punten, vraagtekst_blokken}
    - 2024-stijl: {sub_id, type, stem, context, opties, stellingen}
    Bij twijfel: dump bekende veld-strings, sla lege over.
    """
    onderdelen: list[str] = []
    if sub.get("tekst"):
        onderdelen.append(str(sub["tekst"]).strip())
    if sub.get("stem"):
        onderdelen.append(str(sub["stem"]).strip())
    if sub.get("context"):
        onderdelen.append(str(sub["context"]).strip())
    opties = sub.get("opties")
    if isinstance(opties, list) and opties:
        for o in opties:
            if isinstance(o, dict):
                lbl = o.get("label", "")
                tk = o.get("tekst") or o.get("inhoud") or ""
                onderdelen.append(f"{lbl}) {tk}".strip())
            else:
                onderdelen.append(str(o).strip())
    stellingen = sub.get("stellingen")
    if isinstance(stellingen, list) and stellingen:
        for i, s in enumerate(stellingen, 1):
            if isinstance(s, dict):
                onderdelen.append(f"({i}) {s.get('tekst') or s.get('stelling') or ''}".strip())
            else:
                onderdelen.append(f"({i}) {s}".strip())
    return "\n".join(o for o in onderdelen if o)


def _bouw_tekst(vraag: dict) -> str:
    """Concat vraagtekst + subvragen (indien aanwezig) tot één tekstblok."""
    delen: list[str] = []
    hoofd = (vraag.get("vraagtekst") or "").strip()
    if hoofd:
        delen.append(hoofd)

    subs = vraag.get("subvragen") or vraag.get("sub_vragen") or []
    for idx, sub in enumerate(subs):
        label = _subvraag_label(sub, idx)
        rendered = _subvraag_tekst(sub)
        if not rendered:
            continue
        delen.append(f"=== subvraag {label} ===\n{rendered}")

    return "\n\n".join(delen).rstrip() + "\n"


def _schrijf_als_anders(pad: Path, inhoud: str) -> bool:
    """Schrijf bestand alleen als content verschilt. Returnt True bij schrijf."""
    if pad.exists():
        bestaand = pad.read_text(encoding="utf-8")
        if bestaand == inhoud:
            return False
    pad.write_text(inhoud, encoding="utf-8")
    return True


def _render_pagina_pngs(
    pdf_pad: Path,
    pagina_van: int,
    pagina_tot: int,
    seg_dir: Path,
) -> list[Path]:
    """Render één PNG per pagina in [pagina_van, pagina_tot] (1-indexed, inclusief).

    Idempotent: skip pagina's waarvoor de PNG al bestaat (> 0 bytes).
    """
    gewenste_paden: list[Path] = []
    nog_te_renderen: list[int] = []
    for pp in range(pagina_van, pagina_tot + 1):
        png_pad = seg_dir / f"pagina_{pp:02d}.png"
        gewenste_paden.append(png_pad)
        if png_pad.exists() and png_pad.stat().st_size > 0:
            continue
        nog_te_renderen.append(pp)

    if not nog_te_renderen:
        return gewenste_paden

    with pdfplumber.open(str(pdf_pad)) as pdf:
        for pp in nog_te_renderen:
            # pdfplumber.pages is 0-indexed
            page = pdf.pages[pp - 1]
            page_image = page.to_image(resolution=PNG_RESOLUTIE)
            # pdfplumber levert standaard mode "P" (palette). Voor downstream
            # LLM-consumers + breed beeld-tool-support converteren naar RGB.
            pil_img = page_image.original
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")
            pil_img.save(str(seg_dir / f"pagina_{pp:02d}.png"), format="PNG")
    return gewenste_paden


def isoleer_vraag(entry: dict) -> dict[str, Any]:
    """Verwerk één subset-entry. Return rapport-dict."""
    examen_id = entry["examen_id"]
    vraag_id = entry["vraag_id"]
    pagina_van = int(entry["pagina_van"])
    pagina_tot = int(entry["pagina_tot"])

    cfg = EXAMEN_CONFIGS_V2.get(examen_id)
    if not cfg:
        raise RuntimeError(f"Geen EXAMEN_CONFIGS_V2-entry voor {examen_id}")
    pdf_bestand = cfg["pdf_bestand"]
    pdf_pad = PDF_DIR / pdf_bestand
    if not pdf_pad.is_file():
        raise FileNotFoundError(f"PDF ontbreekt: {pdf_pad}")

    examen_doc = _laad_examen_json(examen_id)
    vraag = _vind_vraag(examen_doc, vraag_id)
    if not vraag:
        raise RuntimeError(f"Vraag {vraag_id} niet gevonden in {examen_id}.json")

    seg_dir = SEGMENTEN_DIR / examen_id / vraag_id
    seg_dir.mkdir(parents=True, exist_ok=True)

    # 1. tekst.txt
    tekst = _bouw_tekst(vraag)
    if not tekst.strip():
        raise RuntimeError(f"Lege vraagtekst voor {vraag_id} — niets om te schrijven")
    tekst_gewijzigd = _schrijf_als_anders(seg_dir / "tekst.txt", tekst)

    # 2. PNGs
    png_paden = _render_pagina_pngs(pdf_pad, pagina_van, pagina_tot, seg_dir)

    # 3. meta.json
    meta = {
        "examen_id": examen_id,
        "vraag_id": vraag_id,
        "pagina_nummers": list(range(pagina_van, pagina_tot + 1)),
        "pdf_bestand": pdf_bestand,
        "karakter": entry.get("karakter"),
        "rationale": entry.get("rationale"),
        "bbox_hint": None,
    }
    meta_inhoud = json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    meta_gewijzigd = _schrijf_als_anders(seg_dir / "meta.json", meta_inhoud)

    return {
        "examen_id": examen_id,
        "vraag_id": vraag_id,
        "seg_dir": str(seg_dir.relative_to(BASE_DIR)),
        "tekst_gewijzigd": tekst_gewijzigd,
        "meta_gewijzigd": meta_gewijzigd,
        "pngs": [str(p.relative_to(BASE_DIR)) for p in png_paden],
    }


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Vraag-isolatie (ADR-024 §2): tekst.txt + pagina_NN.png + meta.json per vraag.",
    )
    parser.add_argument("--examen", help="Beperk tot één examen_id (bv. 2024-1).")
    parser.add_argument("--vraag", help="Beperk tot één vraag_id (bv. 2013-1-vr1).")
    parser.add_argument(
        "--alle",
        action="store_true",
        help="Verwerk ALLE vragen in alle examen-JSONs (autodetect pagina-range).",
    )
    args = parser.parse_args(argv)

    entries: list[dict]
    waarschuwingen: list[str] = []

    if args.alle:
        examen_ids = _vind_examen_ids()
        if args.examen:
            examen_ids = [e for e in examen_ids if e == args.examen]
        if not examen_ids:
            print("Geen examen-JSONs gevonden.", file=sys.stderr)
            return 1
        # POC-vraag-IDs nooit aanraken in --alle-modus: hun karakter/rationale
        # zijn handgepenned en mogen niet door auto-isolatie overschreven worden.
        poc_vraag_ids = {e["vraag_id"] for e in _laad_subset()} if SUBSET_PATH.exists() else set()
        entries = []
        for eid in examen_ids:
            eid_entries, eid_warns = _autodetect_entries(eid)
            entries.extend(e for e in eid_entries if e["vraag_id"] not in poc_vraag_ids)
            waarschuwingen.extend(eid_warns)
        if args.vraag:
            entries = [e for e in entries if e["vraag_id"] == args.vraag]
    else:
        entries = _laad_subset()
        if args.examen:
            entries = [e for e in entries if e["examen_id"] == args.examen]
        if args.vraag:
            entries = [e for e in entries if e["vraag_id"] == args.vraag]

    if not entries:
        print("Geen entries match het filter.", file=sys.stderr)
        return 1

    SEGMENTEN_DIR.mkdir(parents=True, exist_ok=True)

    for w in waarschuwingen:
        print(f"[WARN ] {w}", file=sys.stderr)

    for entry in entries:
        rapport = isoleer_vraag(entry)
        veranderd = rapport["tekst_gewijzigd"] or rapport["meta_gewijzigd"]
        status = "WRITE" if veranderd else "SKIP "
        print(
            f"[{status}] {rapport['examen_id']:>12} / {rapport['vraag_id']:<18} "
            f"-> {rapport['seg_dir']} ({len(rapport['pngs'])} PNG)",
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
