"""
Dekkingscheck-utility (ADR-002).

Bouwt op aanvraag een reverse-index:
  concept-id → [kenniselement-codes die ernaar verwijzen]

Source of truth = programmaonderdeel-JSON's (data/programmaonderdelen/*.json).
Geen state op concept-records zelf (ADR-007: concept-laag is dependency-vrij).

Gebruik:
  python tools/lib/coverage.py                        # rapport voor alle POs
  python tools/lib/coverage.py --po 4.0               # één programmaonderdeel
  python tools/lib/coverage.py --gaten                # toon alleen kenniselementen zonder concepten
"""

import argparse
import json
from pathlib import Path

ROOT    = Path(__file__).resolve().parent.parent.parent
PO_DIR  = ROOT / "data" / "programmaonderdelen"
CON_DIR = ROOT / "data" / "concept_records"


# ---------------------------------------------------------------------------
# Reverse-index
# ---------------------------------------------------------------------------

def bouw_reverse_index(po_data: dict) -> dict[str, list[str]]:
    """
    Geef een dict concept-id → [kenniselement-codes] op basis van één PO-JSON.
    Leest zowel kenniselementen als taakblokken (concept-lijsten op taak/doelstelling-niveau).
    """
    index: dict[str, list[str]] = {}

    def registreer(code: str, concept_ids: list):
        for cid in concept_ids or []:
            index.setdefault(cid, []).append(code)

    # Kenniselementen (incl. subitems)
    for ke in po_data.get("kenniselementen", []):
        registreer(ke["code"], ke.get("concepten", []))
        for sub in ke.get("subitems", []):
            registreer(sub["code"], sub.get("concepten", []))

    # Taakblokken (taken / doelstellingen kunnen ook concepten-lijsten dragen)
    for tb in po_data.get("taakblokken", []):
        registreer(tb["code"], tb.get("concepten", []))
        for taak in tb.get("taken", []):
            registreer(f"{tb['code']}.taak", taak.get("concepten", []))
        for doel in tb.get("doelstellingen", []):
            registreer(f"{tb['code']}.doel", doel.get("concepten", []))

    return index


def laad_alle_po() -> list[dict]:
    pos = []
    for f in sorted(PO_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text())
            data["_bestand"] = f.name
            pos.append(data)
        except Exception as e:
            print(f"  Overgeslagen {f.name}: {e}")
    return pos


# ---------------------------------------------------------------------------
# Dekkingscheck per PO
# ---------------------------------------------------------------------------

def dekkingscheck(po_data: dict) -> dict:
    """
    Geeft rapport:
      - gedekte kenniselementen: hebben minstens één concept
      - ongedekte kenniselementen: geen concept
      - onbekende concept-ids: staan in de PO-JSON maar niet in data/concept_records/
    """
    po_nr    = po_data.get("programmaonderdeel", "?")
    gedekt   = []
    ongedekt = []
    onbekend = []

    def check_ke(code: str, tekst: str, concepten: list):
        if not concepten:
            ongedekt.append({"code": code, "tekst": tekst})
            return
        for cid in concepten:
            path = CON_DIR / f"{cid}.json"
            if not path.exists():
                onbekend.append({"concept_id": cid, "kenniselement": code})
        gedekt.append({"code": code, "tekst": tekst, "concepten": concepten})

    for ke in po_data.get("kenniselementen", []):
        if ke.get("deel") != 1:
            continue
        if "subitems" in ke:
            for sub in ke["subitems"]:
                check_ke(sub["code"], sub["tekst"], sub.get("concepten", []))
        else:
            check_ke(ke["code"], ke["tekst"], ke.get("concepten", []))

    return {
        "programmaonderdeel": po_nr,
        "gedekte_kenniselementen": len(gedekt),
        "ongedekte_kenniselementen": len(ongedekt),
        "ongedekt": ongedekt,
        "onbekende_concept_ids": onbekend,
    }


def print_rapport(rapport: dict, alleen_gaten: bool = False):
    po = rapport["programmaonderdeel"]
    gedekt   = rapport["gedekte_kenniselementen"]
    ongedekt = rapport["ongedekte_kenniselementen"]
    totaal   = gedekt + ongedekt

    print(f"\n{'='*60}")
    print(f"PO {po}: {gedekt}/{totaal} kenniselementen gedekt")
    print(f"{'='*60}")

    if rapport["ongedekte_kenniselementen"] == 0 and not alleen_gaten:
        print("  ✓ Alle kenniselementen hebben minstens één concept.")
    else:
        print(f"\n  Ongedekte kenniselementen ({ongedekt}):")
        for ke in rapport["ongedekt"]:
            print(f"    [{ke['code']}] {ke['tekst']}")

    if rapport["onbekende_concept_ids"]:
        print(f"\n  Onbekende concept-ids (staan in PO-JSON maar niet op schijf):")
        for item in rapport["onbekende_concept_ids"]:
            print(f"    {item['concept_id']} (gevraagd door {item['kenniselement']})")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Dekkingscheck kenniselementen ↔ concepten (ADR-002)")
    parser.add_argument("--po", help="Programmaonderdeel-nummer (bv. 4.0) — default: alle")
    parser.add_argument("--gaten", action="store_true", help="Toon alleen ongedekte kenniselementen")
    parser.add_argument("--json", action="store_true", help="Output als JSON ipv leesbaar rapport")
    args = parser.parse_args()

    pos = laad_alle_po()
    if args.po:
        pos = [p for p in pos if p.get("programmaonderdeel") == args.po]
        if not pos:
            print(f"Programmaonderdeel {args.po} niet gevonden in {PO_DIR}")
            return

    rapporten = [dekkingscheck(po) for po in pos]

    if args.json:
        print(json.dumps(rapporten, indent=2, ensure_ascii=False))
        return

    for rapport in rapporten:
        print_rapport(rapport, alleen_gaten=args.gaten)

    # Samenvattende totalen
    totaal_gedekt   = sum(r["gedekte_kenniselementen"] for r in rapporten)
    totaal_ongedekt = sum(r["ongedekte_kenniselementen"] for r in rapporten)
    totaal          = totaal_gedekt + totaal_ongedekt
    print(f"\n{'='*60}")
    print(f"TOTAAL: {totaal_gedekt}/{totaal} kenniselementen gedekt over {len(rapporten)} PO(s)")


if __name__ == "__main__":
    main()
