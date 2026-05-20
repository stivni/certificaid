"""Schema-validator voor `correct_antwoord_blokken[]` (ADR-023 v1).

Checks per blok-type uit ADR-023 §2:
- type ∈ geldige set
- verplichte velden aanwezig + type-correct
- confidence ∈ {"grounded", "inferred"} (indien gezet)
- per blok-type-specifieke checks (zijde D/C in boeking, items in opsomming, ...)

CLI:
    python3 -m tools.examen.validate_antwoord_blokken_v1                # alle examens
    python3 -m tools.examen.validate_antwoord_blokken_v1 --examen 2014-1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXAMEN_DIR = BASE_DIR / "data" / "programma" / "examen_vragen"

GELDIGE_BLOK_TYPES = {
    "motivatie", "boeking", "berekening", "opsomming", "procedure",
    "definitie", "tabel", "conclusie", "grondslag",
}

GELDIGE_CONFIDENCE = {"grounded", "inferred"}


def _check_string(d: dict, veld: str, path: str, vereist: bool = True) -> list[str]:
    fouten: list[str] = []
    if veld not in d:
        if vereist:
            fouten.append(f"{path}: veld '{veld}' ontbreekt")
        return fouten
    if not isinstance(d[veld], str):
        fouten.append(f"{path}: veld '{veld}' is geen string")
    return fouten


def valideer_blok(blok: Any, path: str) -> list[str]:
    fouten: list[str] = []
    if not isinstance(blok, dict):
        return [f"{path}: blok is geen dict"]
    btype = blok.get("type")
    if btype not in GELDIGE_BLOK_TYPES:
        fouten.append(f"{path}: ongeldig blok-type {btype!r}")
        return fouten
    # confidence (overal optioneel)
    if "confidence" in blok and blok["confidence"] not in GELDIGE_CONFIDENCE:
        fouten.append(f"{path}: confidence {blok['confidence']!r} niet in {GELDIGE_CONFIDENCE}")

    if btype == "motivatie":
        fouten.extend(_check_string(blok, "inhoud", path))
    elif btype == "definitie":
        fouten.extend(_check_string(blok, "lemma", path))
        fouten.extend(_check_string(blok, "definitie_zin", path))
        if "kerneigenschappen" in blok:
            ke = blok["kerneigenschappen"]
            if not isinstance(ke, list):
                fouten.append(f"{path}: kerneigenschappen geen list")
            else:
                for i, k in enumerate(ke):
                    if not isinstance(k, dict):
                        fouten.append(f"{path}.kerneigenschappen[{i}]: geen dict")
                    elif "eigenschap" not in k:
                        fouten.append(f"{path}.kerneigenschappen[{i}]: 'eigenschap' ontbreekt")
    elif btype == "boeking":
        regels = blok.get("regels")
        if not isinstance(regels, list):
            fouten.append(f"{path}: 'regels' is geen list")
        else:
            for i, r in enumerate(regels):
                if not isinstance(r, dict):
                    fouten.append(f"{path}.regels[{i}]: geen dict")
                    continue
                if r.get("zijde") not in ("D", "C"):
                    fouten.append(f"{path}.regels[{i}]: zijde moet 'D' of 'C' zijn (kreeg {r.get('zijde')!r})")
                for v in ("rekening", "naam"):
                    if v not in r or not isinstance(r[v], str):
                        fouten.append(f"{path}.regels[{i}]: '{v}' ontbreekt of geen string")
                if "bedrag" in r and not isinstance(r["bedrag"], (int, float)):
                    fouten.append(f"{path}.regels[{i}]: 'bedrag' is geen number")
    elif btype == "berekening":
        if "formule" not in blok and "componenten" not in blok:
            fouten.append(f"{path}: minstens 'formule' of 'componenten' verplicht")
        if "formule" in blok and not isinstance(blok["formule"], str):
            fouten.append(f"{path}: 'formule' geen string")
    elif btype == "opsomming":
        items = blok.get("items")
        if not isinstance(items, list) or not items:
            fouten.append(f"{path}: 'items' is geen niet-lege list")
        else:
            for i, it in enumerate(items):
                if not isinstance(it, dict):
                    fouten.append(f"{path}.items[{i}]: geen dict")
                    continue
                if "lemma" not in it or not isinstance(it["lemma"], str):
                    fouten.append(f"{path}.items[{i}]: 'lemma' ontbreekt of geen string")
                if "confidence" in it and it["confidence"] not in GELDIGE_CONFIDENCE:
                    fouten.append(f"{path}.items[{i}]: confidence ongeldig")
    elif btype == "procedure":
        stappen = blok.get("stappen")
        if not isinstance(stappen, list) or not stappen:
            fouten.append(f"{path}: 'stappen' is geen niet-lege list")
        else:
            for i, st in enumerate(stappen):
                if not isinstance(st, dict):
                    fouten.append(f"{path}.stappen[{i}]: geen dict")
                    continue
                if "beschrijving" not in st or not isinstance(st["beschrijving"], str):
                    fouten.append(f"{path}.stappen[{i}]: 'beschrijving' ontbreekt of geen string")
                if "nummer" in st and not isinstance(st["nummer"], int):
                    fouten.append(f"{path}.stappen[{i}]: 'nummer' is geen int")
    elif btype == "tabel":
        rows = blok.get("rows")
        if not isinstance(rows, list) or not rows:
            fouten.append(f"{path}: 'rows' is geen niet-lege list")
        else:
            for i, r in enumerate(rows):
                if not isinstance(r, list) or not all(isinstance(c, str) for c in r):
                    fouten.append(f"{path}.rows[{i}]: geen list[str]")
        headers = blok.get("headers")
        if headers is not None and (not isinstance(headers, list) or not all(isinstance(h, str) for h in headers)):
            fouten.append(f"{path}: 'headers' geen list[str]")
    elif btype == "conclusie":
        fouten.extend(_check_string(blok, "inhoud", path))
    elif btype == "grondslag":
        bronnen = blok.get("bronnen")
        if not isinstance(bronnen, list) or not bronnen:
            fouten.append(f"{path}: 'bronnen' is geen niet-lege list")
        else:
            for i, b in enumerate(bronnen):
                if not isinstance(b, str):
                    fouten.append(f"{path}.bronnen[{i}]: geen string")
    return fouten


def valideer_vraag(vraag: dict[str, Any], idx: int) -> list[str]:
    fouten: list[str] = []
    vid = vraag.get("id", f"#{idx}")
    blokken = vraag.get("correct_antwoord_blokken")
    if blokken is not None:
        if not isinstance(blokken, list):
            return [f"vraag {vid}: 'correct_antwoord_blokken' geen list"]
        for i, b in enumerate(blokken):
            fouten.extend(valideer_blok(b, f"vraag {vid}.antwoord_blok[{i}]"))
    for sleutel in ("subvragen", "sub_vragen"):
        sv = vraag.get(sleutel)
        if isinstance(sv, list):
            for j, s in enumerate(sv):
                if not isinstance(s, dict):
                    continue
                sb = s.get("correct_antwoord_blokken")
                if sb is None:
                    continue
                if not isinstance(sb, list):
                    fouten.append(f"vraag {vid}.{sleutel}[{j}]: 'correct_antwoord_blokken' geen list")
                    continue
                for k, b in enumerate(sb):
                    fouten.extend(valideer_blok(
                        b, f"vraag {vid}.{sleutel}[{j}].antwoord_blok[{k}]",
                    ))
    return fouten


def valideer_examen(examen_file: Path) -> list[str]:
    fouten: list[str] = []
    try:
        doc = json.loads(examen_file.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{examen_file.name}: kon niet parsen: {e}"]
    for i, v in enumerate(doc.get("vragen", [])):
        fouten.extend(valideer_vraag(v, i))
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
            if p.name.startswith("_") or p.name.endswith("-labels.json"):
                continue
            examen_files.append(p)
    totaal = 0
    for f in examen_files:
        fouten = valideer_examen(f)
        if fouten:
            print(f"\n[{f.name}] {len(fouten)} fouten:")
            for x in fouten[:30]:
                print(f"  - {x}")
            if len(fouten) > 30:
                print(f"  ... ({len(fouten) - 30} meer)")
        else:
            print(f"[{f.name}] OK")
        totaal += len(fouten)
    print(f"\nTotaal fouten: {totaal}")
    return 1 if totaal > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
