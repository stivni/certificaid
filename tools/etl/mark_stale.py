"""Scan bron-MD's, compare recorded input-hashes against current inputs, flag stale.

See docs/adr/ADR-003-reprocessing-evaluatie.md (workflow) and ADR-004-provenance.md (schema).

Usage:
  python tools/etl/mark_stale.py resources/bronnen/wetteksten/
  python tools/etl/mark_stale.py resources/bronnen/wetteksten/Antiwitwaswet-2017.md
  python tools/etl/mark_stale.py resources/bronnen/ --dry-run
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import (  # noqa: E402
    Input,
    detect_stale,
    hash_file,
    read_provenance,
    write_provenance,
)


def check_one(md_path: Path, *, dry_run: bool = False) -> tuple[str, str]:
    """Returns (status, detail).

    status ∈ {fresh, stale-already, became-stale, recovered, no-provenance, missing-input}
    """
    prov = read_provenance(md_path)
    if prov is None:
        return "no-provenance", ""

    if not prov.inputs:
        # No inputs declared — nothing to compare. Leave state untouched.
        # Typical case: 'pre-Fase-0' stale-markers on concept-records (ADR-008).
        return ("stale-already" if prov.stale else "no-inputs-declared"), (
            prov.stale_reason or "no inputs in provenance"
        )

    current_inputs: list[Input] = []
    for recorded in prov.inputs:
        if recorded.sha256 is None:
            # URL-sourced; no local file to hash, carry forward unchanged
            current_inputs.append(recorded)
            continue
        input_path = ROOT / recorded.id
        if not input_path.exists():
            return "missing-input", recorded.id
        current_inputs.append(
            Input(id=recorded.id, sha256=hash_file(input_path), version=recorded.version)
        )

    is_stale, reason = detect_stale(prov, current_inputs)

    if not is_stale:
        if prov.stale:
            if not dry_run:
                prov.stale = False
                prov.stale_reason = None
                write_provenance(md_path, prov)
            return "recovered", "inputs match recorded hashes again"
        return "fresh", ""

    if prov.stale:
        return "stale-already", prov.stale_reason or reason or ""

    if not dry_run:
        prov.stale = True
        prov.stale_reason = reason
        write_provenance(md_path, prov)
    return "became-stale", reason or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", help="MD files or directories to scan")
    ap.add_argument("--dry-run", action="store_true", help="Report only; do not modify files")
    args = ap.parse_args()

    targets: list[Path] = []
    for p in args.paths:
        path = Path(p)
        if path.is_dir():
            md = sorted(path.rglob("*.md"))
            jsn = sorted(path.rglob("*.json"))
            targets.extend(md + jsn)
        elif path.is_file():
            targets.append(path)
        else:
            print(f"warning: {p} not found", file=sys.stderr)

    counts: dict[str, int] = {}
    interesting = {"became-stale", "recovered", "missing-input"}
    for t in targets:
        status, detail = check_one(t, dry_run=args.dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status in interesting:
            print(f"  {status:18s}  {t}  ({detail})")

    print(f"\nScanned {len(targets)} files{' (dry-run)' if args.dry_run else ''}:")
    for status, n in sorted(counts.items()):
        print(f"  {status:18s}  {n}")


if __name__ == "__main__":
    main()
