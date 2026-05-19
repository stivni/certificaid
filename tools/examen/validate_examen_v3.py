"""Schema-validator voor examen_vragen v3 (ADR-021 v3.0).

Checks:
- schema_versie == "3.0"
- Elke vraag heeft vraagtekst_blokken[] (mag [] zijn als vraagtekst leeg is)
- Blok-types ∈ geldige v3-set
- Per blok-type: verplichte velden aanwezig + type-checks

CLI:
    python3 -m tools.examen.validate_examen_v3                 # alle examens
    python3 -m tools.examen.validate_examen_v3 --examen 2014-1
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
    "tekst", "tabel", "formule", "figuur",
    "proef_saldibalans", "rekeningstaat", "balans", "resultatenrekening",
    "inventaris", "marktwaarde", "aanpassing",
    "casus_context", "vraag_instructie", "bijlage_verwijzing",
    "mc_optie", "berekening_gegeven",
}

# Per blok-type: (verplichte velden, ...
_REQUIRED: dict[str, list[str]] = {
    "tekst": ["inhoud"],
    "tabel": ["rows"],
    "formule": ["inhoud"],
    "figuur": [],
    "proef_saldibalans": ["regels"],
    "rekeningstaat": ["regels"],
    "balans": [],
    "resultatenrekening": ["regels"],
    "inventaris": ["regels"],
    "marktwaarde": ["bedrag"],
    "aanpassing": ["bedrag"],
    "casus_context": ["inhoud"],
    "vraag_instructie": ["inhoud"],
    "bijlage_verwijzing": ["beschrijving"],
    "mc_optie": ["label", "tekst"],
    "berekening_gegeven": ["formule"],
}


def _check_regels_lijst(
    rows: Any,
    verplichte_velden: list[str],
    path: str,
) -> list[str]:
    fouten: list[str] = []
    if not isinstance(rows, list):
        fouten.append(f"{path}: 'regels' is geen list")
        return fouten
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            fouten.append(f"{path}.regels[{i}]: geen dict")
            continue
        for v in verplichte_velden:
            if v not in r:
                fouten.append(f"{path}.regels[{i}]: veld '{v}' ontbreekt")
    return fouten


def valideer_blok(blok: Any, path: str) -> list[str]:
    """Valideer één blok-dict. Returnt foutmeldingen."""
    fouten: list[str] = []
    if not isinstance(blok, dict):
        return [f"{path}: blok is geen dict"]
    btype = blok.get("type")
    if btype not in GELDIGE_BLOK_TYPES:
        fouten.append(f"{path}: ongeldig blok-type {btype!r}")
        return fouten
    for v in _REQUIRED.get(btype, []):
        if v not in blok:
            fouten.append(f"{path}: type={btype} mist veld '{v}'")
    # Type-specifieke checks
    if btype == "tekst":
        if "inhoud" in blok and not isinstance(blok["inhoud"], str):
            fouten.append(f"{path}: tekst-blok 'inhoud' is geen string")
    elif btype == "tabel":
        rows = blok.get("rows")
        if isinstance(rows, list):
            for i, r in enumerate(rows):
                if not isinstance(r, list):
                    fouten.append(f"{path}.rows[{i}]: geen list")
                else:
                    for j, c in enumerate(r):
                        if not isinstance(c, str):
                            fouten.append(f"{path}.rows[{i}][{j}]: geen string")
            if rows:
                lengtes = {len(r) for r in rows if isinstance(r, list)}
                if len(lengtes) > 1:
                    fouten.append(f"{path}: rijen niet even lang ({sorted(lengtes)})")
            headers = blok.get("headers")
            if headers is not None:
                if not isinstance(headers, list) or not all(isinstance(h, str) for h in headers):
                    fouten.append(f"{path}: 'headers' is geen list[str]")
                elif rows and headers:
                    row_len = len(rows[0]) if isinstance(rows[0], list) else 0
                    if len(headers) != row_len:
                        fouten.append(f"{path}: header-lengte {len(headers)} ≠ rij-lengte {row_len}")
    elif btype == "proef_saldibalans":
        fouten.extend(_check_regels_lijst(blok.get("regels"), ["rekening", "naam", "zijde", "bedrag"], path))
    elif btype == "rekeningstaat":
        fouten.extend(_check_regels_lijst(blok.get("regels"), ["rekening", "naam", "bedrag"], path))
    elif btype == "inventaris":
        fouten.extend(_check_regels_lijst(blok.get("regels"), ["post", "bedrag"], path))
    elif btype == "resultatenrekening":
        fouten.extend(_check_regels_lijst(blok.get("regels"), ["post", "bedrag"], path))
    elif btype == "balans":
        for kant in ("activa", "passiva"):
            r = blok.get(kant)
            if r is not None and not isinstance(r, list):
                fouten.append(f"{path}: '{kant}' is geen list")
    elif btype == "marktwaarde":
        b = blok.get("bedrag")
        if b is not None and not isinstance(b, (int, float)):
            fouten.append(f"{path}: 'bedrag' is geen number")
    elif btype == "aanpassing":
        b = blok.get("bedrag")
        if b is not None and not isinstance(b, (int, float)):
            fouten.append(f"{path}: 'bedrag' is geen number")
    elif btype == "casus_context":
        if "inhoud" in blok and not isinstance(blok["inhoud"], str):
            fouten.append(f"{path}: 'inhoud' is geen string")
    elif btype == "vraag_instructie":
        if "inhoud" in blok and not isinstance(blok["inhoud"], str):
            fouten.append(f"{path}: 'inhoud' is geen string")
    elif btype == "mc_optie":
        for v in ("label", "tekst"):
            if v in blok and not isinstance(blok[v], str):
                fouten.append(f"{path}: '{v}' is geen string")
    return fouten


def valideer_vraag(vraag: dict[str, Any], idx: int) -> list[str]:
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
    # Subvragen
    for veld in ("subvragen", "sub_vragen"):
        sv = vraag.get(veld)
        if isinstance(sv, list):
            for j, s in enumerate(sv):
                if not isinstance(s, dict):
                    continue
                sb = s.get("vraagtekst_blokken")
                if isinstance(sb, list):
                    for k, b in enumerate(sb):
                        fouten.extend(valideer_blok(b, f"vraag {vid}.{veld}[{j}].blok[{k}]"))
    return fouten


def valideer_examen(examen_file: Path) -> list[str]:
    fouten: list[str] = []
    try:
        doc = json.loads(examen_file.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{examen_file.name}: kon niet parsen: {e}"]

    if doc.get("schema_versie") != "3.0":
        fouten.append(
            f"{examen_file.name}: schema_versie != '3.0' "
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
            for fout in fouten[:30]:
                print(f"  - {fout}")
            if len(fouten) > 30:
                print(f"  ... ({len(fouten) - 30} meer)")
        else:
            print(f"[{f.name}] OK")
        totaal_fouten += len(fouten)

    print(f"\nTotaal fouten: {totaal_fouten}")
    return 1 if totaal_fouten > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
