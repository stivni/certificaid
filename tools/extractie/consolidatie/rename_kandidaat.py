"""Rename kandidaat in candidates-DB met cascade naar edges en depends_on.

Update fiche_id van een bestaande kandidaat. Cascadeert naar alle andere kandidaten
die naar de oude fiche_id verwijzen via edges_voorgesteld of depends_on_fiches.

Usage:
    python3 -m tools.extractie.consolidatie.rename_kandidaat <oud> <nieuw>
    python3 -m tools.extractie.consolidatie.rename_kandidaat --batch <batch.json>
    python3 -m tools.extractie.consolidatie.rename_kandidaat --dry-run --batch <batch.json>

Batch-format (JSON):
    [{"old": "...", "new": "...", "reason": "regel-A suffix-strip"}, ...]
"""

import sqlite3
import json
import sys
import argparse
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data" / "extractie" / "candidates.sqlite3"


def _walk_replace(obj, old, new):
    """Vervang elke voorkomen van `old` (string) door `new` in een geneste JSON-structuur."""
    changed = False
    if isinstance(obj, str):
        if obj == old:
            return new, True
        return obj, False
    if isinstance(obj, list):
        out = []
        for item in obj:
            new_item, ch = _walk_replace(item, old, new)
            out.append(new_item)
            changed = changed or ch
        return out, changed
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            new_v, ch = _walk_replace(v, old, new)
            out[k] = new_v
            changed = changed or ch
        return out, changed
    return obj, False


def rename_one(conn: sqlite3.Connection, old: str, new: str, dry_run: bool = False) -> dict:
    """Rename fiche_id van old → new, cascadeer refs in andere kandidaten."""
    cur = conn.cursor()
    cur.row_factory = sqlite3.Row

    # 1. Check old exists
    src = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (old,)).fetchone()
    if not src:
        return {"old": old, "new": new, "status": "skipped", "reason": "old fiche_id niet gevonden"}

    # 2. Check new doesn't exist (collision)
    dst = cur.execute("SELECT fiche_id FROM candidates WHERE fiche_id = ?", (new,)).fetchone()
    if dst:
        return {"old": old, "new": new, "status": "collision", "reason": f"nieuw fiche_id '{new}' bestaat al — gebruik merge_kandidaat ipv rename"}

    # 3. Find cascade-targets (andere kandidaten met refs naar old)
    cascade_updates = []
    for row in cur.execute("SELECT fiche_id, edges_voorgesteld, depends_on_fiches FROM candidates WHERE fiche_id != ?", (old,)).fetchall():
        edges = json.loads(row["edges_voorgesteld"] or "{}")
        deps = json.loads(row["depends_on_fiches"] or "[]")
        new_edges, ec = _walk_replace(edges, old, new)
        new_deps, dc = _walk_replace(deps, old, new)
        if ec or dc:
            cascade_updates.append((row["fiche_id"], json.dumps(new_edges, ensure_ascii=False), json.dumps(new_deps, ensure_ascii=False), ec, dc))

    if dry_run:
        return {
            "old": old, "new": new, "status": "dry-run",
            "cascade_count": len(cascade_updates),
            "cascade_sample": [c[0] for c in cascade_updates[:5]],
        }

    # 4. Execute: rename + cascade in single transaction
    try:
        cur.execute("UPDATE candidates SET fiche_id = ?, laatste_wijziging = datetime('now') WHERE fiche_id = ?", (new, old))
        for fiche_id, edges_json, deps_json, _, _ in cascade_updates:
            cur.execute(
                "UPDATE candidates SET edges_voorgesteld = ?, depends_on_fiches = ?, laatste_wijziging = datetime('now') WHERE fiche_id = ?",
                (edges_json, deps_json, fiche_id),
            )
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {"old": old, "new": new, "status": "error", "reason": str(e)}

    return {
        "old": old, "new": new, "status": "renamed",
        "cascade_count": len(cascade_updates),
        "cascade_sample": [c[0] for c in cascade_updates[:5]],
    }


def main():
    ap = argparse.ArgumentParser(description="Rename kandidaat in candidates-DB met cascade.")
    ap.add_argument("old", nargs="?", help="Oude fiche_id")
    ap.add_argument("new", nargs="?", help="Nieuwe fiche_id")
    ap.add_argument("--batch", help="JSON-file met [{'old':..., 'new':..., 'reason':...}, ...]")
    ap.add_argument("--dry-run", action="store_true", help="Toon wat zou gebeuren, voer niet uit")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    results = []

    if args.batch:
        batch = json.loads(Path(args.batch).read_text())
        for item in batch:
            r = rename_one(conn, item["old"], item["new"], dry_run=args.dry_run)
            r["reason"] = item.get("reason", "")
            results.append(r)
    elif args.old and args.new:
        results.append(rename_one(conn, args.old, args.new, dry_run=args.dry_run))
    else:
        ap.error("specify <old> <new> OR --batch <file>")

    # Print summary
    print(json.dumps(results, indent=2, ensure_ascii=False))
    n_renamed = sum(1 for r in results if r["status"] == "renamed")
    n_dry = sum(1 for r in results if r["status"] == "dry-run")
    n_collision = sum(1 for r in results if r["status"] == "collision")
    n_skipped = sum(1 for r in results if r["status"] == "skipped")
    n_error = sum(1 for r in results if r["status"] == "error")
    print(f"\n=== Samenvatting ===", file=sys.stderr)
    print(f"  renamed:   {n_renamed}", file=sys.stderr)
    print(f"  dry-run:   {n_dry}", file=sys.stderr)
    print(f"  collision: {n_collision} (vereisen merge)", file=sys.stderr)
    print(f"  skipped:   {n_skipped} (oude niet gevonden)", file=sys.stderr)
    print(f"  error:     {n_error}", file=sys.stderr)

    conn.close()
    sys.exit(1 if n_error else 0)


if __name__ == "__main__":
    main()
