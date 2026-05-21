"""Voeg familie ↔ lid edges toe in candidates-DB (bypass MCP-bug).

Schrijft `heeft_lid` op familie + `lid_van` op elke lid. Update via JSON-rewrite in
edges_voorgesteld kolom.

Usage:
    python3 -m tools.extractie.consolidatie.add_familie_edges <familie> <lid1> [<lid2> ...]
    python3 -m tools.extractie.consolidatie.add_familie_edges --dry-run <familie> <lid1> ...
"""

import sqlite3
import json
import sys
import argparse
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data" / "extractie" / "candidates.sqlite3"


def add_edges(conn: sqlite3.Connection, familie: str, leden: list, dry_run: bool = False) -> dict:
    cur = conn.cursor()
    cur.row_factory = sqlite3.Row

    # Check familie exists + is kind=familie
    F = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (familie,)).fetchone()
    if not F:
        return {"familie": familie, "status": "error", "reason": "familie niet gevonden"}
    if F["kind"] != "familie":
        return {"familie": familie, "status": "warning", "reason": f"kind = {F['kind']}, niet 'familie' — toch doorgaan"}

    # Check leden bestaan
    missing = []
    for lid in leden:
        if not cur.execute("SELECT 1 FROM candidates WHERE fiche_id = ?", (lid,)).fetchone():
            missing.append(lid)
    if missing:
        return {"familie": familie, "status": "error", "reason": f"leden niet gevonden: {missing}"}

    # Update familie.heeft_lid (union)
    fam_edges = json.loads(F["edges_voorgesteld"] or "{}")
    cur_leden = fam_edges.get("heeft_lid", [])
    new_leden = list(dict.fromkeys(cur_leden + leden))  # union, preserve order
    fam_edges["heeft_lid"] = new_leden
    fam_edges_json = json.dumps(fam_edges, ensure_ascii=False)

    # Update elk lid.lid_van (union)
    lid_updates = []
    for lid in leden:
        L = cur.execute("SELECT edges_voorgesteld FROM candidates WHERE fiche_id = ?", (lid,)).fetchone()
        lid_edges = json.loads(L["edges_voorgesteld"] or "{}")
        cur_van = lid_edges.get("lid_van", [])
        if isinstance(cur_van, str):
            cur_van = [cur_van]
        if familie not in cur_van:
            cur_van = list(cur_van) + [familie]
        lid_edges["lid_van"] = cur_van
        lid_updates.append((lid, json.dumps(lid_edges, ensure_ascii=False)))

    if dry_run:
        return {
            "familie": familie,
            "status": "dry-run",
            "new_heeft_lid": new_leden,
            "lid_updates": [u[0] for u in lid_updates],
        }

    try:
        cur.execute("UPDATE candidates SET edges_voorgesteld = ?, laatste_wijziging = datetime('now') WHERE fiche_id = ?", (fam_edges_json, familie))
        for lid, edges_json in lid_updates:
            cur.execute("UPDATE candidates SET edges_voorgesteld = ?, laatste_wijziging = datetime('now') WHERE fiche_id = ?", (edges_json, lid))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {"familie": familie, "status": "error", "reason": str(e)}

    return {
        "familie": familie,
        "status": "edges-added",
        "heeft_lid": new_leden,
        "lid_van_updated": [u[0] for u in lid_updates],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("familie")
    ap.add_argument("leden", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    result = add_edges(conn, args.familie, args.leden, dry_run=args.dry_run)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    conn.close()
    sys.exit(0 if result["status"] in ("edges-added", "dry-run", "warning") else 1)


if __name__ == "__main__":
    main()
