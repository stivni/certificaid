#!/usr/bin/env python3
"""
One-off migratie: alle bron-MD's krijgen `provenance.trust.status: unreviewed`.

Loopt door `resources/bronnen/{wetteksten,normen,adviezen}/*.md` en zet voor elk
bestand met provenance een default-trust-blok (unreviewed). Bestaande
trust-blokken worden NIET overschreven (idempotent).

Bestanden zonder provenance worden geskipt met een waarschuwing — die moeten
eerst via `tools/etl/add_provenance.py` worden voorzien.

Achtergrond: ADR-005 §5 (kwaliteits-gate met trust-marker) +
ADR-004 (`provenance.trust` schema-uitbreiding).

Gebruik:
  python tools/etl/backfill_trust_unreviewed.py            # alles
  python tools/etl/backfill_trust_unreviewed.py --dry-run  # toon zonder schrijven
  python tools/etl/backfill_trust_unreviewed.py --bron-rol wettekst
  python tools/etl/backfill_trust_unreviewed.py --collection cbn-adviezen
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    Trust,
    default_trust,
    read_provenance,
    write_provenance,
)

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}

COLLECTION_TO_DIR = {
    "wetteksten":   BRON_DIRS["wettekst"],
    "itaa-normen":  BRON_DIRS["norm"],
    "cbn-adviezen": BRON_DIRS["advies"],
}

SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}


def iter_targets(bron_rol: str | None, collection: str | None) -> list[Path]:
    """Verzamel alle bron-MD-bestanden volgens scope-opties."""
    if collection:
        if collection not in COLLECTION_TO_DIR:
            raise SystemExit(
                f"Onbekende collection: {collection!r}. "
                f"Geldig: {sorted(COLLECTION_TO_DIR)}"
            )
        dirs = [COLLECTION_TO_DIR[collection]]
    elif bron_rol:
        if bron_rol not in BRON_DIRS:
            raise SystemExit(
                f"Onbekende bron-rol: {bron_rol!r}. "
                f"Geldig: {sorted(BRON_DIRS)}"
            )
        dirs = [BRON_DIRS[bron_rol]]
    else:
        dirs = list(BRON_DIRS.values())

    files: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name in SKIP_FILES:
                continue
            files.append(f)
    return files


def process_file(path: Path, *, dry_run: bool) -> str:
    """Backfill één bestand. Returnt status-string voor rapport.

    Statussen:
      - skipped-no-provenance: geen provenance-blok aanwezig
      - skipped-has-trust:     trust al gezet
      - written:               default trust toegevoegd
      - dry-run-would-write:   zou trust toevoegen (alleen --dry-run)
    """
    prov = read_provenance(path)
    if prov is None:
        return "skipped-no-provenance"
    if prov.trust is not None:
        return "skipped-has-trust"

    new_trust = default_trust()
    if dry_run:
        return "dry-run-would-write"

    prov.trust = new_trust
    write_provenance(path, prov)
    return "written"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dry-run", action="store_true", help="toon zonder te schrijven")
    p.add_argument("--bron-rol", choices=sorted(BRON_DIRS), help="beperk tot één bron-rol")
    p.add_argument("--collection", choices=sorted(COLLECTION_TO_DIR), help="beperk tot één collection")
    args = p.parse_args()

    if args.bron_rol and args.collection:
        raise SystemExit("Gebruik --bron-rol of --collection, niet beide.")

    targets = iter_targets(args.bron_rol, args.collection)
    if not targets:
        print("Geen bestanden gevonden.")
        return

    counters: dict[str, int] = {}
    print(f"=== backfill_trust_unreviewed {'(dry-run) ' if args.dry_run else ''}===")
    print(f"Scope: {len(targets)} bestand(en)")
    print()

    no_prov_files: list[str] = []
    for f in targets:
        result = process_file(f, dry_run=args.dry_run)
        counters[result] = counters.get(result, 0) + 1
        if result == "skipped-no-provenance":
            no_prov_files.append(str(f.relative_to(ROOT)))

    print("Resultaten:")
    for k in sorted(counters):
        print(f"  {k:30s} {counters[k]:>5d}")

    if no_prov_files:
        print()
        print("Bestanden zonder provenance (run eerst tools/etl/add_provenance.py):")
        for f in no_prov_files[:10]:
            print(f"  {f}")
        if len(no_prov_files) > 10:
            print(f"  ... ({len(no_prov_files) - 10} meer)")

    print()
    if args.dry_run:
        print("Dry-run: niets geschreven. Verwijder --dry-run om wijzigingen toe te passen.")


if __name__ == "__main__":
    main()
