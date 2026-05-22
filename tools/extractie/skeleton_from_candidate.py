"""Genereer een schema-2.1 (v1.5) skelet-record uit een candidates-DB entry.

Output: schema-valid JSON met `inhoud: {}` en `relaties: []`. Vormt
startpunt voor multi-pass extract-pipeline (operatie `beschrijven`).

Schema v1.5 wijzigingen (t.o.v. v1.4):
- `linked_anchors` + `dekt_tdks` → unified veld `ankers`
- Velden `primary_po`, `tags`, `cross_po`, `dekt_tdks`, `andere_talen`
  worden niet langer in het output-record geschreven. De candidates-DB
  blijft ze WEL bewaren (geen wijziging aan DB-schema).
- `schema_version` staat op top-level (niet meer in metadata)
- Changelog-entry-format consistent met v1.5 (zonder `datum`, wel `timestamp`)

CLI:
    # Single candidate
    python3 -m tools.extractie.skeleton_from_candidate <fiche-id>
    python3 -m tools.extractie.skeleton_from_candidate <fiche-id> --out /tmp/x.json

    # Alle openstaande candidates dumpen naar data/concepten/records/
    python3 -m tools.extractie.skeleton_from_candidate --all-pending
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CANDIDATES_DB = REPO_ROOT / "data" / "extractie" / "candidates.sqlite3"
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"

# Map candidate.kind → schema-2.1 concept_type
KIND_NAAR_CONCEPT_TYPE: dict[str, str] = {
    "instrument": "instrument",
    "operatie": "verrichting",
    "verrichting": "verrichting",
    "procedure": "procedure",
    "balanspost": "balanspost",
    "ratio": "ratio",
    "regime": "regime",
    "fiscale-regeling": "regime",
    "kader": "kader",
    "familie": "kader",
    "begripscluster": "kader",
    "principe": "principe",
    "methode": "methode",
    "actor": "actor",
}


SQL_COLS = (
    "fiche_id, kind, primary_po, linked_anchors, dekt_tdks, "
    "voorgesteld_door_pos, cross_po, motivatie"
)


def laad_candidate(fiche_id: str) -> dict:
    conn = sqlite3.connect(CANDIDATES_DB)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            f"SELECT {SQL_COLS} FROM candidates WHERE fiche_id = ?", (fiche_id,)
        ).fetchone()
    finally:
        conn.close()
    if not row:
        raise SystemExit(f"FOUT: candidate '{fiche_id}' niet gevonden in {CANDIDATES_DB}")
    return dict(row)


def laad_alle_openstaande_candidates() -> list[dict]:
    conn = sqlite3.connect(CANDIDATES_DB)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            f"SELECT {SQL_COLS} FROM candidates "
            f"WHERE gerealiseerd = 0 ORDER BY fiche_id"
        ).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


def fiche_id_naar_naam(fiche_id: str) -> str:
    """Kebab-slug → Title Case Nederlands."""
    return fiche_id.replace("-", " ").capitalize()


def parse_json_kolom(value, default):
    """Candidates-DB stockeert sommige velden als JSON-string."""
    if value is None:
        return default
    if isinstance(value, (list, dict)):
        return value
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return default


def bouw_ankers(candidate: dict) -> list[str]:
    """Unified `ankers`-lijst opbouwen uit candidates-DB.

    Schema v1.5 voegt `linked_anchors` en `dekt_tdks` samen in één
    `ankers`-veld. We mergen beide met behoud van volgorde en deduplicatie.
    Fallback op `primary_po` als beide leeg zijn.
    """
    linked = parse_json_kolom(candidate.get("linked_anchors"), [])
    dekt = parse_json_kolom(candidate.get("dekt_tdks"), [])
    primary_po = candidate.get("primary_po") or ""

    ankers: list[str] = []
    seen: set[str] = set()
    for bron in (linked, dekt):
        if not isinstance(bron, list):
            continue
        for item in bron:
            if not isinstance(item, str):
                continue
            if item and item not in seen:
                seen.add(item)
                ankers.append(item)

    if not ankers and primary_po:
        ankers = [primary_po]
    return ankers


def bouw_skelet(candidate: dict) -> dict:
    """Schema-2.1 (v1.5) skelet met lege inhoud."""
    naam_str = fiche_id_naar_naam(candidate["fiche_id"])
    kind = candidate.get("kind", "instrument")
    concept_type = KIND_NAAR_CONCEPT_TYPE.get(kind, "instrument")

    ankers = bouw_ankers(candidate)

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    skelet = {
        "id": candidate["fiche_id"],
        "naam": {"primair": naam_str},
        "concept_type": concept_type,
        "schema_version": "2.1",
        "metadata": {
            "status": "seed",
            "ankers": ankers,
            "provenance": {
                "model": "skeleton-from-candidate",
                "wave_id": "skeleton-dump",
                "extract_prompt": "tools.extractie.skeleton_from_candidate",
                "iteratie": "v0",
            },
            "changelog": [
                {
                    "operatie": "skeleton",
                    "timestamp": now_iso,
                    "model": "skeleton-from-candidate",
                    "wijziging": "Skelet aangemaakt uit candidates-DB; inhoud leeg.",
                }
            ],
        },
        "inhoud": {},
        "relaties": [],
    }
    return skelet


def schrijf_skelet(skelet: dict, pad: Path, *, force: bool) -> str:
    pad.parent.mkdir(parents=True, exist_ok=True)
    if pad.exists() and not force:
        return f"SKIP (bestaat): {pad.name}"
    pad.write_text(json.dumps(skelet, ensure_ascii=False, indent=2) + "\n")
    return f"OK: {pad.name}"


def cmd_single(args: argparse.Namespace) -> int:
    candidate = laad_candidate(args.fiche_id)
    skelet = bouw_skelet(candidate)
    out_pad = Path(args.out) if args.out else RECORDS_DIR / f"{args.fiche_id}.json"
    print(schrijf_skelet(skelet, out_pad, force=args.force))
    return 0


def cmd_dump_all(args: argparse.Namespace) -> int:
    candidates = laad_alle_openstaande_candidates()
    print(f"▶ {len(candidates)} openstaande candidates te dumpen naar {RECORDS_DIR}")
    aantal_ok = 0
    aantal_skip = 0
    for c in candidates:
        skelet = bouw_skelet(c)
        pad = RECORDS_DIR / f"{c['fiche_id']}.json"
        result = schrijf_skelet(skelet, pad, force=args.force)
        if result.startswith("OK"):
            aantal_ok += 1
        else:
            aantal_skip += 1
    print(f"Klaar: {aantal_ok} geschreven, {aantal_skip} overgeslagen (bestaande)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Schema-2.1 (v1.5) skelet uit candidates-DB.")
    grp = parser.add_mutually_exclusive_group(required=True)
    grp.add_argument("fiche_id", nargs="?", help="Eén candidate fiche_id")
    grp.add_argument("--all-pending", action="store_true", help="Dump alle openstaande candidates")
    parser.add_argument("--out", help="Output-pad (alleen voor single mode; default: data/concepten/records/<id>.json)")
    parser.add_argument("--force", action="store_true", help="Overschrijf bestaande bestanden")
    args = parser.parse_args()

    if args.all_pending:
        return cmd_dump_all(args)
    return cmd_single(args)


if __name__ == "__main__":
    sys.exit(main())
