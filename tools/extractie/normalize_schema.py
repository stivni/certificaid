"""CLI om drift in schema 2.0 records te normaliseren.

Gebruik:
    # Dry-run op één record
    python3 -m tools.extractie.normalize_schema --record obligatielening --dry-run

    # Dry-run op een hele wave
    python3 -m tools.extractie.normalize_schema --wave wave-1-20260521 --dry-run

    # Echte rewrite van een wave (overschrijft JSON-files)
    python3 -m tools.extractie.normalize_schema --wave wave-1-20260521 \\
        --default-wave-id wave-1-20260521

    # Hele records-collectie checken
    python3 -m tools.extractie.normalize_schema --all --dry-run

Idempotent: tweede run = no-op. Loopt direct via disk-write (geen RAG-roundtrip);
draai daarna `records_api reindex-wave <id>` als batch om RAG te syncen.

Anomalieën (top-level inhoud_type/weergaven/onderdelen/edges/bronnen_grounded)
worden gerapporteerd maar NIET aangeraakt — die vereisen handmatige re-extract.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.lib.schema_v2 import (
    ValidationError,
    detect_anomalies,
    normalize_record,
    validate_schema_v2,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"


def _wave_id_van_record(record: dict) -> str | None:
    prov = record.get("_provenance") or {}
    return (
        prov.get("wave_id")
        or prov.get("extract_wave_id")
        or prov.get("wave")
        or None
    )


def selecteer_records(args: argparse.Namespace) -> list[Path]:
    if args.record:
        pad = RECORDS_DIR / f"{args.record}.json"
        if not pad.exists():
            sys.exit(f"FOUT: record niet gevonden: {pad}")
        return [pad]

    alle = sorted(RECORDS_DIR.glob("*.json"))
    if args.all:
        return alle

    if args.wave:
        treffers: list[Path] = []
        for pad in alle:
            try:
                rec = json.loads(pad.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            if rec.get("schema_version") != "2.0":
                continue
            if _wave_id_van_record(rec) == args.wave:
                treffers.append(pad)
        if not treffers:
            sys.exit(f"FOUT: geen schema-2.0 records gevonden voor wave='{args.wave}'")
        return treffers

    sys.exit("FOUT: geef --record, --wave of --all op")


def verwerk_record(
    pad: Path, default_wave_id: str | None, dry_run: bool
) -> tuple[str, list[str], list[str], bool]:
    """Retourneert (record_id, mutaties, anomalieën, was_valide_na_normalize)."""
    rec = json.loads(pad.read_text())
    record_id = rec.get("id", pad.stem)

    if rec.get("schema_version") != "2.0":
        return record_id, [], [], False  # skip

    # 1. Anomalie-detectie (vóór normaliseren — anomalieën worden niet aangeraakt)
    anomalieën = detect_anomalies(rec)

    # 2. Normaliseer
    normed, mutaties = normalize_record(rec, default_wave_id=default_wave_id)

    # 3. Validatie post-normalisatie
    try:
        validate_schema_v2(normed)
        valide = True
    except ValidationError:
        valide = False

    # 4. Schrijf indien echt-run + er waren mutaties + geen anomalieën
    if mutaties and not dry_run and not anomalieën:
        pad.write_text(json.dumps(normed, ensure_ascii=False, indent=2) + "\n")

    return record_id, mutaties, anomalieën, valide


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normaliseer schema 2.0 records (drift-fix)."
    )
    grp = parser.add_mutually_exclusive_group(required=True)
    grp.add_argument("--record", help="Eén record-id (slug, zonder .json)")
    grp.add_argument("--wave", help="Filter op _provenance.wave_id")
    grp.add_argument("--all", action="store_true", help="Alle schema-2.0 records")

    parser.add_argument(
        "--default-wave-id",
        help="Fallback wave_id als _provenance.wave_id leeg is en niet uit "
        "iteratie_log af te leiden. Verplicht voor --wave-runs als records "
        "leeg wave_id kunnen hebben.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon wat gewijzigd zou worden, schrijf niets.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Toon ook records zonder mutaties (no-op).",
    )

    args = parser.parse_args()

    paden = selecteer_records(args)
    print(f"▶ {len(paden)} record(s) geselecteerd ({'dry-run' if args.dry_run else 'rewrite'})")

    aantal_gewijzigd = 0
    aantal_anomalieën = 0
    aantal_invalide_na = 0

    for pad in paden:
        rid, muts, anoms, valide = verwerk_record(
            pad, default_wave_id=args.default_wave_id, dry_run=args.dry_run
        )

        if anoms:
            aantal_anomalieën += 1
            print(f"  ⚠️  {rid}: ANOMALIE — vereist handmatige re-extract")
            for a in anoms:
                print(f"      • {a}")
            if muts:
                print(f"      (normalisatie geskipt vanwege anomalie; {len(muts)} mutaties klaar)")
            continue

        if muts:
            aantal_gewijzigd += 1
            actie = "zou wijzigen" if args.dry_run else "gewijzigd"
            print(f"  ✏️  {rid}: {actie} ({len(muts)} mutaties)")
            for m in muts:
                print(f"      • {m}")
            if not valide:
                aantal_invalide_na += 1
                print(f"      ❌ POST-NORMALIZE INVALIDE — handmatige fix nodig")
        elif args.verbose:
            print(f"  ✓  {rid}: no-op (al canonical)")

    print()
    print(f"Klaar: {aantal_gewijzigd} gewijzigd, {aantal_anomalieën} anomalieën, "
          f"{aantal_invalide_na} invalide na normalisatie")
    if args.dry_run:
        print("(dry-run — geen disk-writes gedaan)")
    elif aantal_gewijzigd > 0:
        print(f"\nVolgende stap: python3 -m tools.lib.records_api reindex-wave <wave-id>")

    if aantal_anomalieën > 0 or aantal_invalide_na > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
