"""
Sync candidates-DB met huidige records (vangnet voor ontbrekende hooks).

Loopt over data/concepten/records/*.json en markeert overeenkomstige
kandidaten als `gerealiseerd=1`. Voor records die geen kandidaat hebben:
optioneel auto-create stub (--auto-create).

Idempotent + reversible. Veilig om periodiek te draaien (na wave, voor
re-run skeleton-pass, of als smoke-test).

Gebruik:
  # Sync alle records met DB
  python3 -m tools.extractie.sync_candidates_met_records

  # Met wave-id-tagging
  python3 -m tools.extractie.sync_candidates_met_records --wave wave-0a-2026-05-21

  # Dry-run
  python3 -m tools.extractie.sync_candidates_met_records --dry-run

  # Auto-create stub-kandidaten voor records zonder DB-entry
  python3 -m tools.extractie.sync_candidates_met_records --auto-create
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"

# Lokale import na sys.path setup
sys.path.insert(0, str(ROOT))
from tools.extractie import candidates_db  # noqa: E402


def _verzamel_record_ids() -> list[tuple[str, dict]]:
    """Lijst (record_id, partial-content) tuples voor alle records."""
    paden = sorted(RECORDS_DIR.glob("*.json"))
    result = []
    for p in paden:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"  ⚠️  Skip {p.name}: {e}", file=sys.stderr)
            continue
        record_id = data.get("id") or p.stem
        result.append((record_id, data))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--wave", help="Optioneel wave-id om te taggen bij markering")
    parser.add_argument("--dry-run", action="store_true", help="Toon wat zou gebeuren, schrijf niets")
    parser.add_argument(
        "--auto-create",
        action="store_true",
        help="Maak stub-kandidaat voor records zonder DB-entry (kind=onbekend, primary_po=onbekend)",
    )
    args = parser.parse_args()

    if not RECORDS_DIR.exists():
        print(f"Records-folder bestaat niet: {RECORDS_DIR}", file=sys.stderr)
        return 1

    records = _verzamel_record_ids()
    print(f"Records gevonden: {len(records)}")

    gemarkeerd = 0
    geskipt_al_gerealiseerd = 0
    geen_kandidaat = 0
    auto_created = 0
    errors = 0

    for record_id, data in records:
        bestaande = candidates_db.lees_kandidaat(record_id)
        if bestaande is None:
            if args.auto_create:
                if args.dry_run:
                    print(f"  [dry-run] AUTO-CREATE stub: {record_id}")
                    auto_created += 1
                    continue
                # Maak stub-kandidaat
                primary_po = "onbekend"
                if data.get("linked_anchors"):
                    eerste_anchor = str(data["linked_anchors"][0])
                    # Extract PO uit anchor (formaat: '1.1.taak.3' → '1.1')
                    parts = eerste_anchor.split(".")
                    if len(parts) >= 2:
                        primary_po = f"{parts[0]}.{parts[1]}"
                kind = data.get("kind") or data.get("node_type") or "onbekend"
                candidates_db.voorstel_kandidaat(
                    fiche_id=record_id,
                    kind=kind,
                    primary_po=primary_po,
                    voorgesteld_door_po=primary_po,
                    motivatie=data.get("naam", record_id),
                    linked_anchors=data.get("linked_anchors", []),
                )
                candidates_db.markeer_gerealiseerd(
                    record_id, record_id=record_id, extract_wave_id=args.wave
                )
                auto_created += 1
                print(f"  ➕ auto-create + gemarkeerd: {record_id}")
            else:
                geen_kandidaat += 1
                continue
        else:
            if bestaande.get("gerealiseerd"):
                geskipt_al_gerealiseerd += 1
                continue
            if args.dry_run:
                print(f"  [dry-run] MARKEER gerealiseerd: {record_id}")
                gemarkeerd += 1
                continue
            result = candidates_db.markeer_gerealiseerd(
                record_id, record_id=record_id, extract_wave_id=args.wave
            )
            if "error" in result:
                errors += 1
                print(f"  ❌ {record_id}: {result['error']}")
            else:
                gemarkeerd += 1
                print(f"  ✓ gemarkeerd: {record_id}")

    print("\n=== Samenvatting ===")
    print(f"  Nieuw gemarkeerd:           {gemarkeerd}")
    print(f"  Al gerealiseerd (skip):     {geskipt_al_gerealiseerd}")
    print(f"  Auto-created stubs:         {auto_created}")
    print(f"  Records zonder kandidaat:   {geen_kandidaat}  (gebruik --auto-create om stubs te maken)")
    print(f"  Errors:                     {errors}")

    if not args.dry_run:
        stats = candidates_db.statistieken()
        print(f"\nDB-state: {stats['totaal']} totaal, {stats['gerealiseerd']} gerealiseerd, "
              f"{stats['openstaand']} openstaand")

    return 0


if __name__ == "__main__":
    sys.exit(main())
