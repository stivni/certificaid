"""
SQLite-gebaseerde matches-store voor anchor-bron-matches (ADR-005 §9.1).

Schema (matches-tabel):
  anchor_id   TEXT  — identificatie van de anchor (bv. "1.1.taak.1")
  chunk_id    TEXT  — identificatie van de chunk in ChromaDB
  score       REAL  — cosine-similarity score (0–1)
  in_bundle   INTEGER (0|1) — 1 als chunk in de definitieve bundle voor dit anchor zit
  chunk_sha   TEXT  — sha256-vingerafdruk van de chunk-inhoud (6 hex-tekens uit ChromaDB metadata)
  anchor_vector_hash TEXT — sha256-vingerafdruk van de anchor-vector (eerste 16 hex)

Twee indices:
  - (anchor_id, in_bundle) voor get_bundle-queries
  - (chunk_id)             voor delta-detectie bij chunk-mutaties

State-fingerprints (ADR-005 §9.1):
  - chunk_sha    → muteert als ChromaDB-chunk-inhoud verandert
  - anchor_vector_hash → muteert als anchor-vector herberekend is

Helper-functies:
  open_store(db_path) -> sqlite3.Connection      — opent DB, initialiseert schema indien leeg
  get_bundle(conn, anchor_id) -> list[tuple]     — [(chunk_id, score)] gesorteerd aflopend
  current_chunks_with_sha(chroma_path) -> dict   — {chunk_id: chunk_sha} uit ChromaDB
  current_anchors_with_hash(anchors_path) -> dict — {anchor_id: vector_hash} uit anchors.json
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import struct
from pathlib import Path

import chromadb
import numpy as np

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_DB_PATH = ROOT / "data" / "extractie" / "matches.sqlite3"
DEFAULT_CHROMA_PATH = ROOT / "data" / "rag" / "main"
DEFAULT_ANCHORS_PATH = ROOT / "data" / "programma" / "anchors.json"

_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS matches (
    anchor_id          TEXT NOT NULL,
    chunk_id           TEXT NOT NULL,
    score              REAL NOT NULL,
    in_bundle          INTEGER NOT NULL DEFAULT 0,
    chunk_sha          TEXT,
    anchor_vector_hash TEXT,
    PRIMARY KEY (anchor_id, chunk_id)
);
"""

_CREATE_INDEX_ANCHOR = """
CREATE INDEX IF NOT EXISTS idx_matches_anchor_bundle
    ON matches (anchor_id, in_bundle);
"""

_CREATE_INDEX_CHUNK = """
CREATE INDEX IF NOT EXISTS idx_matches_chunk
    ON matches (chunk_id);
"""

# Sla een fingerprint op van de complete ChromaDB-staat (alle chunk_ids + hun shas)
# zodat de delta-detectie onderscheid kan maken tussen "chunk al gezien maar te laag"
# en "chunk echt nieuw". Slaat sha256 op van de gesorteerde chunk_id:sha-combinaties.
_CREATE_META = """
CREATE TABLE IF NOT EXISTS meta (
    sleutel TEXT PRIMARY KEY,
    waarde  TEXT NOT NULL
);
"""


def open_store(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """
    Open de SQLite matches-store en initialiseer het schema indien nog niet aanwezig.

    De DB-file wordt aangemaakt als hij niet bestaat; de tabel + indices worden
    alleen aangemaakt als ze ontbreken (CREATE IF NOT EXISTS is idempotent).
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute(_CREATE_TABLE)
    conn.execute(_CREATE_INDEX_ANCHOR)
    conn.execute(_CREATE_INDEX_CHUNK)
    conn.execute(_CREATE_META)
    conn.commit()
    return conn


def get_bundle(conn: sqlite3.Connection, anchor_id: str) -> list[tuple[str, float]]:
    """
    Retourneer de bundle-chunks voor een anchor, gesorteerd op score (aflopend).

    Alleen rijen met in_bundle = 1 worden teruggegeven.

    Returns:
        Lijst van (chunk_id, score) tuples.
    """
    rows = conn.execute(
        "SELECT chunk_id, score FROM matches WHERE anchor_id = ? AND in_bundle = 1 ORDER BY score DESC",
        (anchor_id,),
    ).fetchall()
    return [(row[0], row[1]) for row in rows]


def current_chunks_with_sha(
    chroma_path: Path = DEFAULT_CHROMA_PATH,
) -> dict[str, str | None]:
    """
    Haal alle chunk_id → chunk_sha op uit ChromaDB (collection 'bronnen').

    chunk_sha is de waarde uit de metadata die door rag_index.py geschreven wordt.
    Ontbrekende sha → None (chunk is dan altijd stale).
    """
    if not chroma_path.exists():
        raise FileNotFoundError(
            f"ChromaDB-pad niet gevonden: {chroma_path}. "
            "Bouw eerst de RAG-index via `tools/rag/rag_index.py`."
        )
    client = chromadb.PersistentClient(path=str(chroma_path))
    col = client.get_collection("bronnen")
    data = col.get(include=["metadatas"])
    return {
        chunk_id: meta.get("chunk_sha")
        for chunk_id, meta in zip(data["ids"], data["metadatas"])
    }


def current_anchors_with_hash(
    anchors_path: Path = DEFAULT_ANCHORS_PATH,
) -> dict[str, str]:
    """
    Haal alle anchor_id → vector_hash op uit anchors.json.

    vector_hash = sha256 van de aaneengeschakelde float32-bytes van de vector,
    eerste 16 hex-tekens. Dit garandeert dat een herinbedding (andere vector)
    altijd een andere hash oplevert.

    Raises SystemExit als anchors.json ontbreekt of anchors zonder vector heeft.
    """
    if not anchors_path.exists():
        raise SystemExit(
            f"anchors.json niet gevonden op {anchors_path}. "
            "Draai eerst `python3 -m tools.extractie.embed_anchors`."
        )
    data = json.loads(anchors_path.read_text(encoding="utf-8"))
    result: dict[str, str] = {}
    missing = []
    for anchor in data["anchors"]:
        anchor_id = anchor["anchor_id"]
        vector = anchor.get("vector")
        if vector is None:
            missing.append(anchor_id)
            continue
        vector_hash = _vector_hash(vector)
        result[anchor_id] = vector_hash
    if missing:
        raise SystemExit(
            f"{len(missing)} anchors hebben geen vector: {missing[:5]}... "
            "Draai `python3 -m tools.extractie.embed_anchors`."
        )
    return result


def _vector_hash(vector: list[float]) -> str:
    """
    Bereken een sha256-vingerafdruk van een float-vector.

    Pakt de vector als aaneengeschakelde float32-bytes (little-endian),
    hash met sha256, geeft eerste 16 hex-tekens terug.
    """
    packed = struct.pack(f"{len(vector)}f", *vector)
    return hashlib.sha256(packed).hexdigest()[:16]
