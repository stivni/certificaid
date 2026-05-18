"""Schema-validator voor examen_vragen v2 (ADR-021 §7).

Checks:
- schema_versie == "2.0"
- Elke vraag heeft vraagtekst_blokken[] (mag [] zijn als vraagtekst leeg is)
- Blok-types ∈ {tekst, tabel, formule, figuur}
- Tabel-blokken: rows is list[list[str]], alle rijen even lang
- Headers (indien aanwezig): zelfde aantal kolommen als rows
- Concat-reconstructie van blokken matcht vraagtekst (modulo whitespace)

CLI:
    python3 -m tools.examen.validate_examen_v2                 # alle examens
    python3 -m tools.examen.validate_examen_v2 --examen 2014-1
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

from tools.examen.extract_vragen_v2 import (
    Blok,
    concat_blokken_naar_vraagtekst,
    render_tabel_als_markdown,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"
GELDIGE_BLOK_TYPES = {"tekst", "tabel", "formule", "figuur"}


def _collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def valideer_blok(blok: dict, path: str) -> list[str]:
    """Valideer één blok-dict. Returnt foutmeldingen."""
    fouten: list[str] = []
    btype = blok.get("type")
    if btype not in GELDIGE_BLOK_TYPES:
        fouten.append(f"{path}: ongeldig blok-type {btype!r}")
        return fouten
    if btype == "tekst":
        if "inhoud" not in blok:
            fouten.append(f"{path}: tekst-blok mist 'inhoud'")
        elif not isinstance(blok["inhoud"], str):
            fouten.append(f"{path}: tekst-blok 'inhoud' is geen string")
    elif btype == "tabel":
        rows = blok.get("rows")
        if not isinstance(rows, list):
            fouten.append(f"{path}: tabel-blok 'rows' is geen list")
            return fouten
        for i, r in enumerate(rows):
            if not isinstance(r, list):
                fouten.append(f"{path}.rows[{i}]: geen list")
                return fouten
            for j, c in enumerate(r):
                if not isinstance(c, str):
                    fouten.append(f"{path}.rows[{i}][{j}]: geen string ({type(c).__name__})")
        if rows:
            lengtes = {len(r) for r in rows}
            if len(lengtes) > 1:
                fouten.append(f"{path}: rijen niet even lang ({sorted(lengtes)})")
        headers = blok.get("headers")
        if headers is not None:
            if not isinstance(headers, list) or not all(isinstance(h, str) for h in headers):
                fouten.append(f"{path}: 'headers' is geen list[str]")
            elif rows and headers:
                row_len = len(rows[0])
                if len(headers) != row_len:
                    fouten.append(f"{path}: header-lengte {len(headers)} ≠ rij-lengte {row_len}")
    return fouten


def valideer_vraag(vraag: dict, idx: int) -> list[str]:
    fouten: list[str] = []
    vid = vraag.get("id", f"#{idx}")
    blokken = vraag.get("vraagtekst_blokken")
    if blokken is None:
        fouten.append(f"vraag {vid}: 'vraagtekst_blokken' ontbreekt")
        return fouten
    if not isinstance(blokken, list):
        fouten.append(f"vraag {vid}: 'vraagtekst_blokken' is geen list")
        return fouten
    for i, b in enumerate(blokken):
        fouten.extend(valideer_blok(b, f"vraag {vid}.blok[{i}]"))

    # Concat-reconstructie check: alleen waarschuwen, niet falen (tabellen
    # kunnen vrijwillig in vraagtekst opgenomen zijn als markdown; lichte
    # divergentie is OK door normalisatie)
    if vraag.get("vraagtekst") and blokken:
        reconstr = concat_blokken_naar_vraagtekst(blokken)
        if _collapse_ws(reconstr) != _collapse_ws(vraag["vraagtekst"]):
            # Niet hard falen; wel rapporteren als zachte warning via aparte
            # return-channel? We loggen het via stderr.
            sys.stderr.write(
                f"  [warn] vraag {vid}: concat-blokken ≠ vraagtekst (mogelijk normalisatie)\n"
            )
    return fouten


def valideer_examen(examen_file: Path) -> list[str]:
    fouten: list[str] = []
    try:
        doc = json.loads(examen_file.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{examen_file.name}: kon niet parsen: {e}"]

    if doc.get("schema_versie") != "2.0":
        fouten.append(
            f"{examen_file.name}: schema_versie != '2.0' "
            f"(is {doc.get('schema_versie')!r})"
        )
    for i, vraag in enumerate(doc.get("vragen", [])):
        fouten.extend(valideer_vraag(vraag, i))
    return fouten


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examen", type=str, default=None)
    args = parser.parse_args(argv)

    examen_files: list[Path] = []
    if args.examen:
        p = EXAMEN_DIR / f"{args.examen}.json"
        if not p.exists():
            print(f"Niet gevonden: {p}", file=sys.stderr)
            return 1
        examen_files = [p]
    else:
        for p in sorted(EXAMEN_DIR.glob("*.json")):
            if p.name.startswith("_"):
                continue
            if p.name.endswith("-labels.json"):
                continue
            examen_files.append(p)

    totaal_fouten = 0
    for f in examen_files:
        fouten = valideer_examen(f)
        if fouten:
            print(f"\n[{f.name}] {len(fouten)} fouten:")
            for fout in fouten:
                print(f"  - {fout}")
        else:
            print(f"[{f.name}] OK")
        totaal_fouten += len(fouten)

    print(f"\nTotaal fouten: {totaal_fouten}")
    return 1 if totaal_fouten > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
