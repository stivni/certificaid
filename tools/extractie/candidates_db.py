"""
Gedeelde kandidaten-database voor skeleton-voorstel-passes (ADR-025).

Single SQLite-file waar alle skeleton-agents naar schrijven tijdens
parallelle runs over de 19 PO's. Verkleinen dubbel werk door:
- INSERT-OR-MERGE op fiche_id (geen duplicates)
- Embedding-similarity-search vóór nieuwe entry (agent ziet wat anderen
  al hebben voorgesteld)
- Append-only voorgesteld_door_pos[] + per-PO rationale-tracking

Geen schrijfacties via records-API; dit is een pre-extract-fase-DB.
Pas na akkoord wordt de eigenlijke 2.0-extract gestart.

Gebruik:
  from tools.extractie.candidates_db import (
      voorstel_kandidaat,
      zoek_kandidaten,
      lees_kandidaat,
      aanvul_kandidaat,
      lijst_kandidaten,
  )

Embeddings worden door de caller berekend (MCP-server gebruikt bge-m3
uit de retrieval-stack); deze module slaat ze op en doet cosine-search.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

# Module-level paths
ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = ROOT / "data" / "extractie" / "candidates.sqlite3"

# Thread-local connection cache
_local = threading.local()


# ---------------------------------------------------------------------------
# Schema + connection
# ---------------------------------------------------------------------------

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS candidates (
    fiche_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    primary_po TEXT NOT NULL,
    linked_anchors TEXT NOT NULL DEFAULT '[]',
    dekt_tdks TEXT NOT NULL DEFAULT '[]',
    cross_po INTEGER NOT NULL DEFAULT 0,
    motivatie TEXT NOT NULL DEFAULT '',
    verwachte_onderdelen TEXT NOT NULL DEFAULT '[]',
    edges_voorgesteld TEXT NOT NULL DEFAULT '{}',
    depends_on_fiches TEXT NOT NULL DEFAULT '[]',
    v1_hints TEXT NOT NULL DEFAULT '[]',
    rol_perspectieven TEXT NOT NULL DEFAULT '[]',
    embedding BLOB,
    embedding_dim INTEGER,
    voorgesteld_door_pos TEXT NOT NULL DEFAULT '[]',
    rationale_per_po TEXT NOT NULL DEFAULT '{}',
    aanvullings_log TEXT NOT NULL DEFAULT '[]',
    aangemaakt_op TEXT NOT NULL,
    laatste_wijziging TEXT NOT NULL,
    -- Realisatie-tracking (ingevuld bij Fase 2 record-write)
    gerealiseerd INTEGER NOT NULL DEFAULT 0,
    gerealiseerd_als_record_id TEXT,
    gerealiseerd_op TEXT,
    extract_wave_id TEXT
);

CREATE INDEX IF NOT EXISTS ix_candidates_kind ON candidates(kind);
CREATE INDEX IF NOT EXISTS ix_candidates_primary_po ON candidates(primary_po);
-- ix_candidates_gerealiseerd wordt aangemaakt in _migrate_schema na ALTER TABLE
"""


def _migrate_schema(conn: sqlite3.Connection) -> None:
    """Voeg nieuwe kolommen toe aan bestaande DBs (idempotent)."""
    existing_cols = {row[1] for row in conn.execute("PRAGMA table_info(candidates)").fetchall()}
    migrations = [
        ("gerealiseerd", "ALTER TABLE candidates ADD COLUMN gerealiseerd INTEGER NOT NULL DEFAULT 0"),
        ("gerealiseerd_als_record_id", "ALTER TABLE candidates ADD COLUMN gerealiseerd_als_record_id TEXT"),
        ("gerealiseerd_op", "ALTER TABLE candidates ADD COLUMN gerealiseerd_op TEXT"),
        ("extract_wave_id", "ALTER TABLE candidates ADD COLUMN extract_wave_id TEXT"),
    ]
    for col, sql in migrations:
        if col not in existing_cols:
            conn.execute(sql)
    conn.execute("CREATE INDEX IF NOT EXISTS ix_candidates_gerealiseerd ON candidates(gerealiseerd)")
    conn.commit()


def _get_conn() -> sqlite3.Connection:
    """Thread-local SQLite-connectie met WAL-mode voor concurrent writes."""
    conn = getattr(_local, "conn", None)
    if conn is None:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(DB_PATH), timeout=30.0)
        conn.row_factory = sqlite3.Row
        # WAL voor parallelle skeleton-agents
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA busy_timeout=30000")
        conn.executescript(SCHEMA_SQL)
        _migrate_schema(conn)
        conn.commit()
        _local.conn = conn
    return conn


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Embedding helpers
# ---------------------------------------------------------------------------

def _serialize_embedding(emb: list[float] | np.ndarray) -> tuple[bytes, int]:
    """Maak (bytes, dim) van een float-vector."""
    arr = np.asarray(emb, dtype=np.float32)
    return arr.tobytes(), int(arr.shape[0])


def _deserialize_embedding(blob: bytes, dim: int) -> np.ndarray:
    return np.frombuffer(blob, dtype=np.float32, count=dim)


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity tussen twee vectoren (genormaliseerd niet vereist)."""
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def voorstel_kandidaat(
    fiche_id: str,
    kind: str,
    primary_po: str,
    voorgesteld_door_po: str,
    *,
    linked_anchors: list[str] | None = None,
    dekt_tdks: list[str] | None = None,
    cross_po: bool = False,
    motivatie: str = "",
    verwachte_onderdelen: list[str] | None = None,
    edges_voorgesteld: dict[str, list[str]] | None = None,
    depends_on_fiches: list[str] | None = None,
    v1_hints: list[str] | None = None,
    rol_perspectieven: list[str] | None = None,
    embedding: list[float] | np.ndarray | None = None,
    rationale: str = "",
) -> dict[str, Any]:
    """
    Insert-or-merge een kandidaat.

    Bij bestaand fiche_id wordt:
    - linked_anchors gemerged (set-union)
    - dekt_tdks gemerged
    - edges_voorgesteld diepe merge (set-union per edge_type)
    - depends_on_fiches gemerged
    - v1_hints gemerged
    - rol_perspectieven gemerged
    - voorgesteld_door_pos krijgt nieuwe PO erbij (als nog niet aanwezig)
    - rationale_per_po krijgt nieuwe entry per PO
    - aanvullings_log krijgt entry
    - laatste_wijziging bijgewerkt

    cross_po wordt true als ≥ 2 verschillende voorgesteld_door_pos.

    Geeft dict terug met: {"actie": "created"|"merged", "fiche_id": ..., "details": ...}.
    """
    conn = _get_conn()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    now = _now()

    if row is None:
        # Insert
        emb_blob, emb_dim = (None, None) if embedding is None else _serialize_embedding(embedding)
        cur.execute(
            """
            INSERT INTO candidates (
                fiche_id, kind, primary_po, linked_anchors, dekt_tdks,
                cross_po, motivatie, verwachte_onderdelen, edges_voorgesteld,
                depends_on_fiches, v1_hints, rol_perspectieven,
                embedding, embedding_dim,
                voorgesteld_door_pos, rationale_per_po, aanvullings_log,
                aangemaakt_op, laatste_wijziging
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                fiche_id, kind, primary_po,
                json.dumps(linked_anchors or [], ensure_ascii=False),
                json.dumps(dekt_tdks or [], ensure_ascii=False),
                1 if cross_po else 0,
                motivatie,
                json.dumps(verwachte_onderdelen or [], ensure_ascii=False),
                json.dumps(edges_voorgesteld or {}, ensure_ascii=False),
                json.dumps(depends_on_fiches or [], ensure_ascii=False),
                json.dumps(v1_hints or [], ensure_ascii=False),
                json.dumps(rol_perspectieven or [], ensure_ascii=False),
                emb_blob, emb_dim,
                json.dumps([voorgesteld_door_po], ensure_ascii=False),
                json.dumps({voorgesteld_door_po: rationale} if rationale else {}, ensure_ascii=False),
                json.dumps([{"po": voorgesteld_door_po, "actie": "created", "tijd": now}], ensure_ascii=False),
                now, now,
            ),
        )
        conn.commit()
        return {"actie": "created", "fiche_id": fiche_id, "primary_po": primary_po}

    # Merge
    bestaande = dict(row)
    bestaande_anchors = set(json.loads(bestaande["linked_anchors"]))
    bestaande_tdks = set(json.loads(bestaande["dekt_tdks"]))
    bestaande_edges = json.loads(bestaande["edges_voorgesteld"]) or {}
    bestaande_deps = set(json.loads(bestaande["depends_on_fiches"]))
    bestaande_hints = set(json.loads(bestaande["v1_hints"]))
    bestaande_roles = set(json.loads(bestaande["rol_perspectieven"]))
    bestaande_pos = list(json.loads(bestaande["voorgesteld_door_pos"]))
    bestaande_rat = json.loads(bestaande["rationale_per_po"])
    bestaande_log = json.loads(bestaande["aanvullings_log"])

    nieuw_anchors = sorted(bestaande_anchors | set(linked_anchors or []))
    nieuw_tdks = sorted(bestaande_tdks | set(dekt_tdks or []))
    # Edges diepe merge per edge_type
    nieuw_edges: dict[str, list[str]] = dict(bestaande_edges)
    for et, targets in (edges_voorgesteld or {}).items():
        nieuw_edges[et] = sorted(set(nieuw_edges.get(et, [])) | set(targets))
    nieuw_deps = sorted(bestaande_deps | set(depends_on_fiches or []))
    nieuw_hints = sorted(bestaande_hints | set(v1_hints or []))
    nieuw_roles = sorted(bestaande_roles | set(rol_perspectieven or []))
    if voorgesteld_door_po not in bestaande_pos:
        bestaande_pos.append(voorgesteld_door_po)
    if rationale:
        bestaande_rat[voorgesteld_door_po] = rationale
    bestaande_log.append({
        "po": voorgesteld_door_po,
        "actie": "merged",
        "tijd": now,
        "added_anchors": sorted(set(linked_anchors or []) - bestaande_anchors),
        "added_tdks": sorted(set(dekt_tdks or []) - bestaande_tdks),
        "added_hints": sorted(set(v1_hints or []) - bestaande_hints),
    })
    nieuw_cross = 1 if len(bestaande_pos) >= 2 else (1 if cross_po else bestaande["cross_po"])

    # Embedding alleen overschrijven als nieuwe meegegeven (eerste embedding wint typisch)
    if embedding is not None and bestaande["embedding"] is None:
        emb_blob, emb_dim = _serialize_embedding(embedding)
    else:
        emb_blob, emb_dim = bestaande["embedding"], bestaande["embedding_dim"]

    # Motivatie: behoud bestaande (eerste wint); voeg nieuwe aan rationale_per_po toe
    nieuw_motivatie = bestaande["motivatie"] or motivatie

    cur.execute(
        """
        UPDATE candidates SET
            linked_anchors = ?, dekt_tdks = ?, cross_po = ?,
            motivatie = ?, verwachte_onderdelen = ?, edges_voorgesteld = ?,
            depends_on_fiches = ?, v1_hints = ?, rol_perspectieven = ?,
            embedding = ?, embedding_dim = ?,
            voorgesteld_door_pos = ?, rationale_per_po = ?, aanvullings_log = ?,
            laatste_wijziging = ?
        WHERE fiche_id = ?
        """,
        (
            json.dumps(nieuw_anchors, ensure_ascii=False),
            json.dumps(nieuw_tdks, ensure_ascii=False),
            nieuw_cross,
            nieuw_motivatie,
            json.dumps(sorted(set(json.loads(bestaande["verwachte_onderdelen"])) | set(verwachte_onderdelen or [])), ensure_ascii=False),
            json.dumps(nieuw_edges, ensure_ascii=False),
            json.dumps(nieuw_deps, ensure_ascii=False),
            json.dumps(nieuw_hints, ensure_ascii=False),
            json.dumps(nieuw_roles, ensure_ascii=False),
            emb_blob, emb_dim,
            json.dumps(bestaande_pos, ensure_ascii=False),
            json.dumps(bestaande_rat, ensure_ascii=False),
            json.dumps(bestaande_log, ensure_ascii=False),
            now,
            fiche_id,
        ),
    )
    conn.commit()
    return {
        "actie": "merged",
        "fiche_id": fiche_id,
        "voorgesteld_door_pos": bestaande_pos,
        "cross_po": bool(nieuw_cross),
    }


def aanvul_kandidaat(
    fiche_id: str,
    po_id: str,
    veld: str,
    waarde: Any,
    *,
    rationale: str = "",
) -> dict[str, Any]:
    """
    Expliciete partiële update + log-entry.

    veld kan zijn: 'anchor' (één), 'tdk' (één), 'edge' (dict {edge_type: target}),
    'dependency' (één fiche_id), 'hint' (één v1-record-id), 'rol' (één),
    'verwacht_onderdeel' (één).

    Append-only semantiek: alle wijzigingen worden gelogd in aanvullings_log.
    """
    conn = _get_conn()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    if row is None:
        return {"error": f"Kandidaat niet gevonden: {fiche_id}"}

    bestaande = dict(row)
    log = json.loads(bestaande["aanvullings_log"])
    now = _now()
    log_entry: dict[str, Any] = {"po": po_id, "actie": f"aanvul-{veld}", "tijd": now, "waarde": waarde}

    field_map = {
        "anchor": ("linked_anchors", lambda lst: sorted(set(lst) | {waarde})),
        "tdk": ("dekt_tdks", lambda lst: sorted(set(lst) | {waarde})),
        "dependency": ("depends_on_fiches", lambda lst: sorted(set(lst) | {waarde})),
        "hint": ("v1_hints", lambda lst: sorted(set(lst) | {waarde})),
        "rol": ("rol_perspectieven", lambda lst: sorted(set(lst) | {waarde})),
        "verwacht_onderdeel": ("verwachte_onderdelen", lambda lst: sorted(set(lst) | {waarde})),
    }

    if veld in field_map:
        col_name, update_fn = field_map[veld]
        huidig = json.loads(bestaande[col_name])
        nieuw = update_fn(huidig)
        log.append(log_entry)
        cur.execute(
            f"UPDATE candidates SET {col_name} = ?, aanvullings_log = ?, laatste_wijziging = ? WHERE fiche_id = ?",
            (json.dumps(nieuw, ensure_ascii=False), json.dumps(log, ensure_ascii=False), now, fiche_id),
        )
    elif veld == "edge":
        if not isinstance(waarde, dict) or len(waarde) != 1:
            return {"error": "Voor 'edge' geef waarde als {'edge_type': 'doel_fiche_id'}"}
        edge_type, target = next(iter(waarde.items()))
        edges = json.loads(bestaande["edges_voorgesteld"]) or {}
        edges[edge_type] = sorted(set(edges.get(edge_type, [])) | {target})
        log.append(log_entry)
        cur.execute(
            "UPDATE candidates SET edges_voorgesteld = ?, aanvullings_log = ?, laatste_wijziging = ? WHERE fiche_id = ?",
            (json.dumps(edges, ensure_ascii=False), json.dumps(log, ensure_ascii=False), now, fiche_id),
        )
    else:
        return {"error": f"Onbekend veld: {veld}"}

    # Optionele rationale-update
    if rationale:
        rat = json.loads(bestaande["rationale_per_po"])
        rat[po_id] = rationale
        cur.execute(
            "UPDATE candidates SET rationale_per_po = ? WHERE fiche_id = ?",
            (json.dumps(rat, ensure_ascii=False), fiche_id),
        )

    conn.commit()
    return {"actie": "aanvuld", "fiche_id": fiche_id, "veld": veld}


def lees_kandidaat(fiche_id: str) -> dict[str, Any] | None:
    """Volledige kandidaat-record als dict (JSON-velden ge-parsed)."""
    conn = _get_conn()
    row = conn.execute("SELECT * FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    if row is None:
        return None
    return _row_to_dict(row)


def zoek_kandidaten(
    query_embedding: list[float] | np.ndarray,
    top_k: int = 10,
    min_similarity: float = 0.0,
) -> list[dict[str, Any]]:
    """
    Embedding-similarity-search over alle kandidaten met een embedding.

    Returns list of dicts met extra veld 'similarity_score'.
    Gesorteerd op aflopende similarity.
    """
    conn = _get_conn()
    qv = np.asarray(query_embedding, dtype=np.float32)
    rows = conn.execute(
        "SELECT * FROM candidates WHERE embedding IS NOT NULL"
    ).fetchall()
    scored: list[tuple[float, dict[str, Any]]] = []
    for row in rows:
        emb = _deserialize_embedding(row["embedding"], row["embedding_dim"])
        score = _cosine(qv, emb)
        if score >= min_similarity:
            d = _row_to_dict(row)
            d["similarity_score"] = score
            scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:top_k]]


def lijst_kandidaten(
    po_id: str | None = None,
    kind: str | None = None,
    cross_po_only: bool = False,
    gerealiseerd: bool | None = None,
) -> list[dict[str, Any]]:
    """
    Filter-view over de candidates-DB.

    gerealiseerd:
      None  → alles
      False → alleen openstaande kandidaten (extract nog niet gedaan)
      True  → alleen al-gerealiseerde kandidaten (record bestaat)
    """
    conn = _get_conn()
    sql = "SELECT * FROM candidates WHERE 1=1"
    params: list[Any] = []
    if po_id:
        sql += " AND (primary_po = ? OR voorgesteld_door_pos LIKE ?)"
        params.extend([po_id, f"%{po_id}%"])
    if kind:
        sql += " AND kind = ?"
        params.append(kind)
    if cross_po_only:
        sql += " AND cross_po = 1"
    if gerealiseerd is True:
        sql += " AND gerealiseerd = 1"
    elif gerealiseerd is False:
        sql += " AND gerealiseerd = 0"
    sql += " ORDER BY primary_po, kind, fiche_id"
    rows = conn.execute(sql, params).fetchall()
    return [_row_to_dict(row) for row in rows]


def markeer_gerealiseerd(
    fiche_id: str,
    record_id: str | None = None,
    extract_wave_id: str | None = None,
) -> dict[str, Any]:
    """
    Markeer een kandidaat als gerealiseerd (record geschreven).

    Aangeroepen door:
    - records_api.save_record() hook bij iedere write (real-time)
    - sync_candidates_met_records.py als vangnet

    Idempotent: meerdere calls hebben geen verkeerd effect.
    Als de kandidaat niet bestaat: return error (geen INSERT — kandidaat moet
    eerst via skeleton-pass bestaan).
    """
    conn = _get_conn()
    cur = conn.cursor()
    row = cur.execute("SELECT fiche_id FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    if row is None:
        return {"error": f"Kandidaat niet gevonden: {fiche_id}. Skeleton-pass eerst nodig."}

    record_id = record_id or fiche_id
    now = _now()
    cur.execute(
        """
        UPDATE candidates SET
            gerealiseerd = 1,
            gerealiseerd_als_record_id = COALESCE(?, gerealiseerd_als_record_id),
            gerealiseerd_op = COALESCE(gerealiseerd_op, ?),
            extract_wave_id = COALESCE(?, extract_wave_id),
            laatste_wijziging = ?
        WHERE fiche_id = ?
        """,
        (record_id, now, extract_wave_id, now, fiche_id),
    )
    conn.commit()
    return {
        "actie": "gemarkeerd_gerealiseerd",
        "fiche_id": fiche_id,
        "record_id": record_id,
        "extract_wave_id": extract_wave_id,
    }


def unmarkeer_gerealiseerd(fiche_id: str) -> dict[str, Any]:
    """
    Zet gerealiseerd-vlag terug naar 0 (voor delete-record of rollback).

    Gebruikt door records_api.delete_record() hook + bij wave-rollback.
    """
    conn = _get_conn()
    cur = conn.cursor()
    row = cur.execute("SELECT fiche_id FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    if row is None:
        return {"error": f"Kandidaat niet gevonden: {fiche_id}"}
    cur.execute(
        """
        UPDATE candidates SET
            gerealiseerd = 0,
            gerealiseerd_als_record_id = NULL,
            laatste_wijziging = ?
        WHERE fiche_id = ?
        """,
        (_now(), fiche_id),
    )
    conn.commit()
    return {"actie": "ungemarkeerd", "fiche_id": fiche_id}


def statistieken() -> dict[str, Any]:
    """Snelle samenvatting van DB-state."""
    conn = _get_conn()
    totaal = conn.execute("SELECT COUNT(*) FROM candidates").fetchone()[0]
    per_kind = conn.execute(
        "SELECT kind, COUNT(*) AS n FROM candidates GROUP BY kind ORDER BY n DESC"
    ).fetchall()
    cross_po_count = conn.execute("SELECT COUNT(*) FROM candidates WHERE cross_po = 1").fetchone()[0]
    met_embedding = conn.execute("SELECT COUNT(*) FROM candidates WHERE embedding IS NOT NULL").fetchone()[0]
    gerealiseerd_count = conn.execute("SELECT COUNT(*) FROM candidates WHERE gerealiseerd = 1").fetchone()[0]
    per_wave = conn.execute(
        "SELECT extract_wave_id, COUNT(*) AS n FROM candidates "
        "WHERE extract_wave_id IS NOT NULL GROUP BY extract_wave_id"
    ).fetchall()
    return {
        "totaal": totaal,
        "per_kind": {row["kind"]: row["n"] for row in per_kind},
        "cross_po": cross_po_count,
        "met_embedding": met_embedding,
        "gerealiseerd": gerealiseerd_count,
        "openstaand": totaal - gerealiseerd_count,
        "per_extract_wave": {row["extract_wave_id"]: row["n"] for row in per_wave},
        "db_path": str(DB_PATH.relative_to(ROOT)),
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    """SQLite-row naar Python dict met geparseerde JSON-velden."""
    d = dict(row)
    json_velden = [
        "linked_anchors", "dekt_tdks", "verwachte_onderdelen",
        "edges_voorgesteld", "depends_on_fiches", "v1_hints",
        "rol_perspectieven", "voorgesteld_door_pos", "rationale_per_po",
        "aanvullings_log",
    ]
    for v in json_velden:
        if v in d and d[v]:
            try:
                d[v] = json.loads(d[v])
            except (json.JSONDecodeError, TypeError):
                pass
    d["cross_po"] = bool(d.get("cross_po", 0))
    # Embedding niet teruggeven (te groot voor display); alleen aanwezigheid
    if d.get("embedding") is not None:
        d["heeft_embedding"] = True
    else:
        d["heeft_embedding"] = False
    d.pop("embedding", None)
    d.pop("embedding_dim", None)
    return d


# ---------------------------------------------------------------------------
# CLI voor smoke-test + statistieken
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "stats":
        print(json.dumps(statistieken(), indent=2, ensure_ascii=False))
    elif cmd == "lijst":
        po = sys.argv[2] if len(sys.argv) > 2 else None
        cands = lijst_kandidaten(po_id=po)
        for c in cands:
            print(f"[{c['kind']}] {c['fiche_id']} (po {c['primary_po']}, voorgesteld door {c['voorgesteld_door_pos']})")
    elif cmd == "lees":
        fiche_id = sys.argv[2]
        result = lees_kandidaat(fiche_id)
        print(json.dumps(result, indent=2, ensure_ascii=False) if result else f"niet gevonden: {fiche_id}")
    elif cmd == "smoke-test":
        print("Smoke-test...")
        result = voorstel_kandidaat(
            fiche_id="test-concept",
            kind="instrument",
            primary_po="9.9",
            voorgesteld_door_po="9.9",
            linked_anchors=["9.9.A"],
            motivatie="Smoke-test entry",
            embedding=[0.1] * 1024,
        )
        print("Voorstel:", result)
        result2 = voorstel_kandidaat(
            fiche_id="test-concept",
            kind="instrument",
            primary_po="9.9",
            voorgesteld_door_po="8.8",
            linked_anchors=["8.8.B"],
            rationale="Tweede PO bevestigt",
        )
        print("Merge:", result2)
        print("\nLees:")
        print(json.dumps(lees_kandidaat("test-concept"), indent=2, ensure_ascii=False))
        # Cleanup
        _get_conn().execute("DELETE FROM candidates WHERE fiche_id = 'test-concept'")
        _get_conn().commit()
        print("\nCleanup OK")
    else:
        print(f"Onbekend commando: {cmd}")
        print("Beschikbaar: stats | lijst [po] | lees <fiche_id> | smoke-test")
