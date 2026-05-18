"""Lichte validator voor minicursus-render-output per programmaonderdeel.

Pilot-validatie-tool (ADR-010 §6.6) — scant gerenderde content op:
- dangling wikilinks (naar non-existent records)
- leerpad-refs (concepten/competenties/syntheses in leerpad-YAML die niet bestaan)
- ontbrekende synthese-content-fiche (verwacht conform §implicatie-2)
- aanwezigheid van vereiste minicursus-secties (oriëntatie, taak-markers, dashboard)

Géén volledige §6.3-validator (paragraaf-zonder-wikilink, glue-woordcount,
examenfocus-camouflage-spoilers) — die zijn complexer en horen bij glue-v3-pas.
Hier alleen de mechanische structuur-checks die §6.6-pilot-rapport reproduceert.

Gebruik:
  python3 -m tools.leermateriaal.validate_minicursus --programmaonderdeel 1.5
  python3 -m tools.leermateriaal.validate_minicursus --alle
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
CONTENT_DIR = ROOT / "content" / "concepten"
STUDIE_DIR = ROOT / "content" / "studiemateriaal"
LEERPADEN_DIR = ROOT / "data" / "concepten" / "leerpaden"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]+)?(?:#[^\]]+)?\]\]")


def _alle_record_ids() -> set[str]:
    return {p.stem for p in RECORDS_DIR.glob("*.json") if not p.name.startswith("_")}


def _synthese_ids() -> set[str]:
    result = set()
    for p in RECORDS_DIR.glob("*.json"):
        if p.name.startswith("_"):
            continue
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
            if r.get("node_type") == "synthese":
                result.add(p.stem)
        except json.JSONDecodeError:
            pass
    return result


def _records_voor_po(programmaonderdeel: str) -> set[str]:
    prefix = f"{programmaonderdeel}."
    result = set()
    for p in RECORDS_DIR.glob("*.json"):
        if p.name.startswith("_"):
            continue
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
            if any(a.startswith(prefix) for a in r.get("linked_anchors", []) or []):
                result.add(p.stem)
        except json.JSONDecodeError:
            pass
    return result


def _wikilinks_in(text: str) -> set[str]:
    return {m.group(1).strip().replace("competenties/", "") for m in WIKILINK_RE.finditer(text)}


def _minicursus_path(programmaonderdeel: str) -> Path | None:
    safe = programmaonderdeel.replace(".", "-")
    matches = list(STUDIE_DIR.glob(f"{safe}-*.md"))
    return matches[0] if matches else None


def valideer_po(programmaonderdeel: str) -> dict:
    """Run validatie voor één PO. Return rapport-dict."""
    all_records = _alle_record_ids()
    synthese_ids = _synthese_ids()
    po_records = _records_voor_po(programmaonderdeel)

    # Concept-fiches die zouden moeten bestaan (PO-records minus synthese)
    expected_fiches = po_records - synthese_ids

    # Dangling wikilinks in fiches
    fiches_dangling: dict[str, list[str]] = {}
    for rid in expected_fiches:
        fiche = CONTENT_DIR / f"{rid}.md"
        if not fiche.exists():
            continue
        wls = _wikilinks_in(fiche.read_text(encoding="utf-8"))
        dangling = sorted(wls - all_records)
        if dangling:
            fiches_dangling[rid] = dangling

    # Synthese-records met fiche (drift)
    synthese_in_po = po_records & synthese_ids
    synthese_drift = sorted(s for s in synthese_in_po if (CONTENT_DIR / f"{s}.md").exists())

    # Minicursus-checks
    mc_path = _minicursus_path(programmaonderdeel)
    mc_dangling: list[str] = []
    mc_structuur: dict[str, bool] = {}
    if mc_path and mc_path.exists():
        text = mc_path.read_text(encoding="utf-8")
        wls = _wikilinks_in(text)
        mc_dangling = sorted(wls - all_records)
        mc_structuur = {
            "oriëntatie-sectie": "## Wat verwacht het examen van jou?" in text,
            "niveau-callout": "[!abstract]" in text,
            "taak-markers": text.count("> [!info] Hoort bij ta") > 0,
            "eind-dashboard": "## Heb je deze taken in de vingers?" in text,
            "examenfocus-rubriek": "## Examenfocus" in text,
        }

    # Leerpad-refs valideren
    leerpad_path = LEERPADEN_DIR / f"{programmaonderdeel}.yaml"
    leerpad_missing = {"concept": [], "competentie": [], "synthese": []}
    if leerpad_path.exists():
        try:
            lp = yaml.safe_load(leerpad_path.read_text(encoding="utf-8"))
            for h in lp.get("hoofdstukken", []) or []:
                htype = h.get("type", "")
                if htype in ("thematisch", "voorbereiding"):
                    for cid in h.get("concepten", []) or []:
                        if cid not in all_records:
                            leerpad_missing["concept"].append(cid)
                elif htype == "competentie":
                    cid = h.get("competentie_id", "")
                    if cid and cid not in all_records:
                        leerpad_missing["competentie"].append(cid)
                elif htype == "synthese":
                    sid = h.get("synthese_id", "")
                    if sid and sid not in all_records:
                        leerpad_missing["synthese"].append(sid)
        except yaml.YAMLError:
            pass

    return {
        "programmaonderdeel": programmaonderdeel,
        "records_count": len(po_records),
        "synthese_count": len(synthese_in_po),
        "fiches_dangling": fiches_dangling,
        "synthese_drift": synthese_drift,
        "minicursus_path": str(mc_path.relative_to(ROOT)) if mc_path else None,
        "minicursus_dangling": mc_dangling,
        "minicursus_structuur": mc_structuur,
        "leerpad_missing": leerpad_missing,
    }


def _print_rapport(r: dict) -> bool:
    """Print rapport, return True als alles OK."""
    po = r["programmaonderdeel"]
    print(f"\n=== PO {po} ===")
    print(f"  Records: {r['records_count']} ({r['synthese_count']} synthese)")

    ok = True
    if r["fiches_dangling"]:
        total = sum(len(v) for v in r["fiches_dangling"].values())
        print(f"  ⚠ Fiches met dangling wikilinks: {len(r['fiches_dangling'])} ({total} links)")
        for src, targets in list(r["fiches_dangling"].items())[:5]:
            print(f"      {src}: {targets[:3]}")
        ok = False
    else:
        print("  ✓ Geen dangling wikilinks in concept-fiches")

    if r["synthese_drift"]:
        print(f"  ✗ Synthese-records mét fiche (ADR-010 §implicatie-2 schending): {r['synthese_drift']}")
        ok = False
    else:
        print("  ✓ Geen synthese-fiche-drift")

    if r["minicursus_path"]:
        print(f"  Minicursus: {r['minicursus_path']}")
        if r["minicursus_dangling"]:
            print(f"    ⚠ Dangling wikilinks: {len(r['minicursus_dangling'])}")
            for d in r["minicursus_dangling"][:8]:
                print(f"      {d}")
            ok = False
        for check, status in r["minicursus_structuur"].items():
            sym = "✓" if status else "✗"
            if not status:
                ok = False
            print(f"    {sym} {check}")
    else:
        print("  ⚠ Geen minicursus gerenderd")

    lp = r["leerpad_missing"]
    total_missing = sum(len(v) for v in lp.values())
    if total_missing:
        print(f"  ✗ Leerpad-refs ontbrekend ({total_missing}): "
              f"{len(lp['concept'])} concepten, {len(lp['competentie'])} competenties, "
              f"{len(lp['synthese'])} syntheses")
        for kind, ids in lp.items():
            for i in ids[:5]:
                print(f"      {kind}: {i}")
        ok = False
    else:
        print("  ✓ Leerpad-refs allemaal resolveerbaar")

    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    grp = parser.add_mutually_exclusive_group(required=True)
    grp.add_argument("--programmaonderdeel", help="Bv. '1.5'")
    grp.add_argument("--alle", action="store_true", help="Alle leerpaden")
    args = parser.parse_args()

    if args.alle:
        po_ids = sorted(p.stem for p in LEERPADEN_DIR.glob("*.yaml"))
    else:
        po_ids = [args.programmaonderdeel]

    alles_ok = True
    for po in po_ids:
        rapport = valideer_po(po)
        if not _print_rapport(rapport):
            alles_ok = False

    print(f"\n{'✓ Alles OK' if alles_ok else '✗ Issues gevonden (zie boven)'}")
    return 0 if alles_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
