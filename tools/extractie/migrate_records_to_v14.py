"""Deterministische migratie van schema 2.1 v1.0-1.3 records naar v1.4.

Wijzigingen:
- `node_type` → `concept_type` (top-level rename)
- `metadata.changelog` → verwijderen (vervangen door operaties_uitgevoerd, mechanisch)
- Initialiseer `metadata.operaties_uitgevoerd: {}` (leeg)
- `voorbeeld_case` → `voorbeeld` (alleen geneste structuur; geen verandering in record-content)
- `weergave.type: "casus"` → `voorbeeld` (waar van toepassing)

Idempotent: tweede run = no-op.

CLI:
    python3 -m tools.extractie.migrate_records_to_v14 --dry-run
    python3 -m tools.extractie.migrate_records_to_v14            # voer uit
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"
SCHEMA_PATH = REPO_ROOT / "data" / "concepten" / "schema-2.1.schema.json"


def migrate(rec: dict) -> tuple[dict, list[str]]:
    """Pas v1.0-1.3 → v1.4 wijzigingen toe. Retourneert (rec, mutaties)."""
    mutaties: list[str] = []

    if "node_type" in rec and "concept_type" not in rec:
        rec["concept_type"] = rec.pop("node_type")
        mutaties.append("node_type → concept_type")

    md = rec.get("metadata", {})
    if "changelog" in md:
        md.pop("changelog")
        mutaties.append("metadata.changelog verwijderd")

    if isinstance(md, dict) and "operaties_uitgevoerd" not in md:
        md["operaties_uitgevoerd"] = {}
        mutaties.append("metadata.operaties_uitgevoerd = {} (init)")

    # weergave.type: "casus" → "voorbeeld" (recursief in elementen)
    def walk_weergaven(obj):
        if isinstance(obj, dict):
            if obj.get("type") == "casus" and "weergaven" not in obj:
                # weergave-obj (not voorbeeld_inline)
                obj["type"] = "voorbeeld"
                mutaties.append("weergave.type: casus → voorbeeld")
            for v in obj.values():
                walk_weergaven(v)
        elif isinstance(obj, list):
            for v in obj:
                walk_weergaven(v)

    walk_weergaven(rec.get("inhoud", {}))

    return rec, mutaties


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate records van schema 2.1 v1.0-1.3 → v1.4.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text())
    validator = Draft202012Validator(schema)

    paden = sorted(RECORDS_DIR.glob("*.json"))
    aantal_gewijzigd = 0
    aantal_post_invalide = 0
    for pad in paden:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError:
            print(f"  ⚠️ {pad.name}: JSON-fout, geskipt")
            continue
        migrated, muts = migrate(rec)
        if not muts:
            continue
        aantal_gewijzigd += 1
        errors = list(validator.iter_errors(migrated))
        if errors:
            aantal_post_invalide += 1
            print(f"  ✗ {pad.stem}: post-migration {len(errors)} errors — {errors[0].message[:80]}")
            continue
        if not args.dry_run:
            pad.write_text(json.dumps(migrated, ensure_ascii=False, indent=2) + "\n")
    print(f"\nKlaar: {aantal_gewijzigd}/{len(paden)} gemigreerd")
    if aantal_post_invalide:
        print(f"  ⚠️ {aantal_post_invalide} post-migration nog invalide — handmatig na te kijken")
    if args.dry_run:
        print("(dry-run — geen disk-writes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
