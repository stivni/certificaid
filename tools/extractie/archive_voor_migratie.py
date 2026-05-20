"""
Archiveer concept-records voor schema 2.0 migratie (ADR-025).

Kopieert (niet verplaatst) records met een gegeven anchor-prefix naar
`data/concepten/_archive/v2.0-migratie/<timestamp>/<po>/`.

Originelen blijven in `data/concepten/records/` zodat:
- Quartz-rendering ongestoord verder werkt op de huidige content
- Records-API kan blijven lezen tijdens overgangsperiode
- save_record() van een 2.0-versie de oude markdown atomair overschrijft

Eenmalige read-only snapshot per migratie-wave. Voor herstel: kopiëren
vanuit archief terug.

Gebruik:
  python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1
  python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1 --dry-run
  python3 -m tools.extractie.archive_voor_migratie --all  # alle records
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
ARCHIVE_BASE = ROOT / "data" / "concepten" / "_archive" / "v2.0-migratie"


def _verzamel_records_voor_anchor(prefix: str | None) -> list[Path]:
    """Geef records terug die minstens één linked_anchor met de prefix hebben."""
    paden: list[Path] = []
    for p in sorted(RECORDS_DIR.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"  ⚠️  Skip {p.name}: kan niet lezen ({e})", file=sys.stderr)
            continue
        if prefix is None:
            paden.append(p)
            continue
        anchors = data.get("linked_anchors", []) or []
        if any(str(a).startswith(prefix) for a in anchors):
            paden.append(p)
    return paden


def _archiveer(paden: list[Path], archief_dir: Path, dry_run: bool) -> int:
    """Kopieer records naar archief. Geef aantal gekopieerd terug."""
    archief_dir.mkdir(parents=True, exist_ok=True)
    aantal = 0
    for p in paden:
        doel = archief_dir / p.name
        if dry_run:
            print(f"  [dry-run] kopieer → {doel.relative_to(ROOT)}")
        else:
            shutil.copy2(p, doel)
            print(f"  ✓ {p.name} → {doel.relative_to(ROOT)}")
        aantal += 1
    return aantal


def _schrijf_manifest(archief_dir: Path, prefix: str | None, aantal: int) -> None:
    """Schrijf een manifest met snapshot-metadata."""
    manifest = {
        "snapshot_tijd": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "anchor_prefix": prefix or "ALL",
        "aantal_records": aantal,
        "doel": (
            "Read-only snapshot vóór schema 2.0 herextract (ADR-025). "
            "Records blijven in data/concepten/records/ tot save_record() ze overschrijft. "
            "Voor herstel: kopieer manueel terug."
        ),
    }
    manifest_pad = archief_dir / "_manifest.json"
    manifest_pad.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"\nManifest: {manifest_pad.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    grp = parser.add_mutually_exclusive_group(required=True)
    grp.add_argument(
        "--anchor-prefix",
        help="Anchor-prefix om te filteren (bv. '1.1' voor PO 1.1, '1' voor alle PO 1.x)",
    )
    grp.add_argument(
        "--all",
        action="store_true",
        help="Archiveer ALLE records (gebruik voorzichtig)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon wat er gekopieerd zou worden, schrijf niets",
    )
    parser.add_argument(
        "--label",
        help="Optioneel sub-label voor archief-folder (default = tijdstempel)",
    )
    args = parser.parse_args()

    if not RECORDS_DIR.exists():
        print(f"Records-folder bestaat niet: {RECORDS_DIR}", file=sys.stderr)
        return 1

    prefix = None if args.all else args.anchor_prefix
    paden = _verzamel_records_voor_anchor(prefix)

    label = args.label or dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    folder_name = f"{label}-po-{prefix}" if prefix else f"{label}-all"
    archief_dir = ARCHIVE_BASE / folder_name

    omschr = f"anchor-prefix '{prefix}'" if prefix else "ALLE records"
    print(f"Archief-doel: {archief_dir.relative_to(ROOT)}")
    print(f"Filter: {omschr}")
    print(f"Records gevonden: {len(paden)}")
    if args.dry_run:
        print("\n[dry-run] geen schrijfacties:")
    else:
        print("\nKopiëren:")

    aantal = _archiveer(paden, archief_dir, dry_run=args.dry_run)

    if not args.dry_run:
        _schrijf_manifest(archief_dir, prefix, aantal)
        print(f"\nKlaar — {aantal} record(s) gearchiveerd.")
        print(
            "\nNB: originele records blijven in data/concepten/records/."
            " Quartz-rendering werkt ongestoord."
        )
    else:
        print(f"\n[dry-run] zou {aantal} record(s) archiveren.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
