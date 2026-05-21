"""Merge twee kandidaten in candidates-DB: loser → winner, cascade refs.

Combineert: linked_anchors, dekt_tdks, edges_voorgesteld (deep merge), depends_on_fiches,
v1_hints, voorgesteld_door_pos, rationale_per_po. Behoudt de langste motivatie standaard;
override met --motivatie 'tekst'.

Usage:
    python3 -m tools.extractie.consolidatie.merge_kandidaat <loser> <winner>
    python3 -m tools.extractie.consolidatie.merge_kandidaat --dry-run <loser> <winner>
    python3 -m tools.extractie.consolidatie.merge_kandidaat --batch <batch.json>

Batch-format (JSON):
    [{"loser": "...", "winner": "...", "reason": "...", "motivatie": "optional override"}, ...]
"""

import sqlite3
import json
import sys
import argparse
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data" / "extractie" / "candidates.sqlite3"


def _walk_replace(obj, old, new):
    """Vervang elk voorkomen van `old` (string) door `new` in geneste JSON."""
    if isinstance(obj, str):
        return (new, True) if obj == old else (obj, False)
    if isinstance(obj, list):
        out = []
        changed = False
        for item in obj:
            new_item, ch = _walk_replace(item, old, new)
            out.append(new_item)
            changed = changed or ch
        return out, changed
    if isinstance(obj, dict):
        out = {}
        changed = False
        for k, v in obj.items():
            new_v, ch = _walk_replace(v, old, new)
            out[k] = new_v
            changed = changed or ch
        return out, changed
    return obj, False


def _union_list(a: list, b: list) -> list:
    """Union van twee lijsten, behoud volgorde, dedup."""
    seen = set()
    out = []
    for item in list(a) + list(b):
        key = json.dumps(item, sort_keys=True) if not isinstance(item, str) else item
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def _merge_edges(a: dict, b: dict) -> dict:
    """Deep merge van edges_voorgesteld dicts: edge_type → list-union."""
    out = dict(a)
    for k, v in b.items():
        if k in out:
            if isinstance(out[k], list) and isinstance(v, list):
                out[k] = _union_list(out[k], v)
            elif isinstance(out[k], str) and isinstance(v, str):
                out[k] = _union_list([out[k]], [v])
            else:
                out[k] = v
        else:
            out[k] = v
    return out


def merge_one(conn: sqlite3.Connection, loser: str, winner: str, motivatie_override: str = None, dry_run: bool = False) -> dict:
    """Merge loser INTO winner. Delete loser, cascade refs."""
    cur = conn.cursor()
    cur.row_factory = sqlite3.Row

    L = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (loser,)).fetchone()
    W = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (winner,)).fetchone()

    if not L:
        return {"loser": loser, "winner": winner, "status": "skipped", "reason": "loser niet gevonden"}
    if not W:
        return {"loser": loser, "winner": winner, "status": "skipped", "reason": "winner niet gevonden"}

    # Combineer attributen
    new_anchors = _union_list(json.loads(W["linked_anchors"]), json.loads(L["linked_anchors"]))
    new_tdks = _union_list(json.loads(W["dekt_tdks"]), json.loads(L["dekt_tdks"]))
    new_edges = _merge_edges(json.loads(W["edges_voorgesteld"]), json.loads(L["edges_voorgesteld"]))
    new_deps = _union_list(json.loads(W["depends_on_fiches"]), json.loads(L["depends_on_fiches"]))
    new_hints = _union_list(json.loads(W["v1_hints"]), json.loads(L["v1_hints"]))
    new_pos = _union_list(json.loads(W["voorgesteld_door_pos"]), json.loads(L["voorgesteld_door_pos"]))
    new_rol = _union_list(json.loads(W["rol_perspectieven"]), json.loads(L["rol_perspectieven"]))
    new_ond = _union_list(json.loads(W["verwachte_onderdelen"]), json.loads(L["verwachte_onderdelen"]))

    # Motivatie: override OF langste van de twee
    if motivatie_override:
        new_motivatie = motivatie_override
    else:
        new_motivatie = W["motivatie"] if len(W["motivatie"]) >= len(L["motivatie"]) else L["motivatie"]

    # rationale_per_po: merge dicts
    new_rationale = {**json.loads(L["rationale_per_po"]), **json.loads(W["rationale_per_po"])}

    # aanvullings_log: union (preserve history)
    new_log = json.loads(W["aanvullings_log"]) + [{"merge_in": loser, "merged_at_iso": "now()"}] + json.loads(L["aanvullings_log"])

    # cross_po flag: union → True als meerdere PO's
    new_cross_po = 1 if len(new_pos) > 1 or W["cross_po"] or L["cross_po"] else 0

    # Find cascade-targets
    cascade_updates = []
    for row in cur.execute("SELECT fiche_id, edges_voorgesteld, depends_on_fiches FROM candidates WHERE fiche_id NOT IN (?, ?)", (loser, winner)).fetchall():
        e = json.loads(row["edges_voorgesteld"] or "{}")
        d = json.loads(row["depends_on_fiches"] or "[]")
        ne, ec = _walk_replace(e, loser, winner)
        nd, dc = _walk_replace(d, loser, winner)
        if ec or dc:
            cascade_updates.append((row["fiche_id"], json.dumps(ne, ensure_ascii=False), json.dumps(nd, ensure_ascii=False)))

    if dry_run:
        return {
            "loser": loser, "winner": winner, "status": "dry-run",
            "new_anchors_count": len(new_anchors),
            "new_tdks_count": len(new_tdks),
            "new_pos": new_pos,
            "cascade_count": len(cascade_updates),
            "cascade_sample": [c[0] for c in cascade_updates[:5]],
            "motivatie_chosen": "override" if motivatie_override else ("winner" if W["motivatie"] == new_motivatie else "loser"),
        }

    try:
        # Update winner
        cur.execute("""
            UPDATE candidates SET
                linked_anchors = ?, dekt_tdks = ?, edges_voorgesteld = ?,
                depends_on_fiches = ?, v1_hints = ?, voorgesteld_door_pos = ?,
                rol_perspectieven = ?, verwachte_onderdelen = ?,
                motivatie = ?, rationale_per_po = ?, aanvullings_log = ?,
                cross_po = ?, laatste_wijziging = datetime('now')
            WHERE fiche_id = ?
        """, (
            json.dumps(new_anchors, ensure_ascii=False),
            json.dumps(new_tdks, ensure_ascii=False),
            json.dumps(new_edges, ensure_ascii=False),
            json.dumps(new_deps, ensure_ascii=False),
            json.dumps(new_hints, ensure_ascii=False),
            json.dumps(new_pos, ensure_ascii=False),
            json.dumps(new_rol, ensure_ascii=False),
            json.dumps(new_ond, ensure_ascii=False),
            new_motivatie,
            json.dumps(new_rationale, ensure_ascii=False),
            json.dumps(new_log, ensure_ascii=False),
            new_cross_po,
            winner,
        ))
        # Cascade
        for fiche_id, edges_json, deps_json in cascade_updates:
            cur.execute(
                "UPDATE candidates SET edges_voorgesteld = ?, depends_on_fiches = ?, laatste_wijziging = datetime('now') WHERE fiche_id = ?",
                (edges_json, deps_json, fiche_id),
            )
        # Delete loser
        cur.execute("DELETE FROM candidates WHERE fiche_id = ?", (loser,))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {"loser": loser, "winner": winner, "status": "error", "reason": str(e)}

    return {
        "loser": loser, "winner": winner, "status": "merged",
        "new_anchors_count": len(new_anchors),
        "new_tdks_count": len(new_tdks),
        "new_pos": new_pos,
        "cascade_count": len(cascade_updates),
        "cascade_sample": [c[0] for c in cascade_updates[:5]],
    }


def main():
    ap = argparse.ArgumentParser(description="Merge twee kandidaten in candidates-DB.")
    ap.add_argument("loser", nargs="?", help="Fiche_id dat verdwijnt")
    ap.add_argument("winner", nargs="?", help="Fiche_id dat blijft (krijgt loser-attributen erbij)")
    ap.add_argument("--motivatie", help="Override motivatie voor winner (optional)")
    ap.add_argument("--batch", help="JSON-file met [{'loser':..., 'winner':..., 'motivatie':..., 'reason':...}]")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    results = []

    if args.batch:
        batch = json.loads(Path(args.batch).read_text())
        for item in batch:
            r = merge_one(conn, item["loser"], item["winner"], item.get("motivatie"), dry_run=args.dry_run)
            r["reason"] = item.get("reason", "")
            results.append(r)
    elif args.loser and args.winner:
        results.append(merge_one(conn, args.loser, args.winner, args.motivatie, dry_run=args.dry_run))
    else:
        ap.error("specify <loser> <winner> OR --batch <file>")

    print(json.dumps(results, indent=2, ensure_ascii=False))
    n_merged = sum(1 for r in results if r["status"] == "merged")
    n_dry = sum(1 for r in results if r["status"] == "dry-run")
    n_skipped = sum(1 for r in results if r["status"] == "skipped")
    n_error = sum(1 for r in results if r["status"] == "error")
    print(f"\n=== Samenvatting ===", file=sys.stderr)
    print(f"  merged:  {n_merged}", file=sys.stderr)
    print(f"  dry-run: {n_dry}", file=sys.stderr)
    print(f"  skipped: {n_skipped}", file=sys.stderr)
    print(f"  error:   {n_error}", file=sys.stderr)
    conn.close()
    sys.exit(1 if n_error else 0)


if __name__ == "__main__":
    main()
