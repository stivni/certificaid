"""
Tests voor de SQLite matches-store en delta-driven match_bronnen.py (ADR-005 §9.1).

Alle tests draaien tegen tmp_path-SQLite + gemockte ChromaDB (in-memory of fake).
Geen afhankelijkheid van live data/rag/main of live anchors.json.
"""
from __future__ import annotations

import json
import sqlite3
import struct
import hashlib
from pathlib import Path
from unittest.mock import patch, MagicMock

import numpy as np
import pytest

from tools.lib.matches_store import (
    open_store,
    get_bundle,
    _vector_hash,
)
from tools.extractie import match_bronnen


# ---------------------------------------------------------------------------
# Hulpfuncties voor test-fixtures
# ---------------------------------------------------------------------------

def _maak_anchors_json(tmp_path: Path, anchors: list[dict]) -> Path:
    """Schrijf een minimaal anchors.json bestand."""
    path = tmp_path / "anchors.json"
    path.write_text(
        json.dumps({"version": "1", "anchors": anchors}, ensure_ascii=False),
        encoding="utf-8",
    )
    return path


def _maak_anchor(
    anchor_id: str,
    vector: list[float],
    po: str = "1.1",
    tekst: str = "test-anchor",
) -> dict:
    return {
        "anchor_id": anchor_id,
        "po": po,
        "tekst": tekst,
        "verbose": "",
        "synoniemen": [],
        "embedding_text": tekst,
        "embedding_text_sha": hashlib.sha256(tekst.encode()).hexdigest()[:16],
        "vector": vector,
    }


def _unit_vector(dim: int, seed: int = 0) -> list[float]:
    """Reproduceerbare eenheidsvector van `dim` dimensies."""
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(dim).astype(np.float32)
    v = v / np.linalg.norm(v)
    return v.tolist()


def _chunk_sha(text: str) -> str:
    """Simpele sha voor test-chunks."""
    return hashlib.sha256(text.encode()).hexdigest()[:8]


# ---------------------------------------------------------------------------
# Test 1: Schema-init
# ---------------------------------------------------------------------------

def test_schema_init_lege_db(tmp_path: Path):
    """Lege DB-file → schema correct geïnitialiseerd na eerste open."""
    db_path = tmp_path / "matches.sqlite3"
    assert not db_path.exists()

    conn = open_store(db_path)
    assert db_path.exists()

    # Controleer dat de tabel bestaat
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='matches'"
    ).fetchall()
    assert len(tables) == 1, "tabel 'matches' moet bestaan na schema-init"

    # Controleer kolommen
    info = conn.execute("PRAGMA table_info(matches)").fetchall()
    kolom_namen = {row[1] for row in info}
    verwachte_kolommen = {"anchor_id", "chunk_id", "score", "in_bundle", "chunk_sha", "anchor_vector_hash"}
    assert verwachte_kolommen <= kolom_namen, f"Ontbrekende kolommen: {verwachte_kolommen - kolom_namen}"

    # Controleer indices
    indices = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='matches'"
    ).fetchall()
    index_namen = {row[0] for row in indices}
    assert "idx_matches_anchor_bundle" in index_namen, "Index op (anchor_id, in_bundle) ontbreekt"
    assert "idx_matches_chunk" in index_namen, "Index op (chunk_id) ontbreekt"

    conn.close()


def test_schema_init_is_idempotent(tmp_path: Path):
    """Twee keer open_store → geen fout, schema stabiel."""
    db_path = tmp_path / "matches.sqlite3"
    conn1 = open_store(db_path)
    conn1.close()
    conn2 = open_store(db_path)
    # Zou geen fout mogen gooien
    count = conn2.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
    assert count == 0
    conn2.close()


# ---------------------------------------------------------------------------
# Test 2: get_bundle helper
# ---------------------------------------------------------------------------

def test_get_bundle_retourneert_alleen_in_bundle_1(tmp_path: Path):
    """get_bundle geeft alleen in_bundle = 1 chunks terug, score-gesorteerd."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    # Schrijf rijen: 2 in bundle, 1 niet
    conn.execute(
        "INSERT INTO matches (anchor_id, chunk_id, score, in_bundle) VALUES (?, ?, ?, ?)",
        ("a1", "c1", 0.90, 1),
    )
    conn.execute(
        "INSERT INTO matches (anchor_id, chunk_id, score, in_bundle) VALUES (?, ?, ?, ?)",
        ("a1", "c2", 0.75, 1),
    )
    conn.execute(
        "INSERT INTO matches (anchor_id, chunk_id, score, in_bundle) VALUES (?, ?, ?, ?)",
        ("a1", "c3", 0.50, 0),  # niet in bundle
    )
    conn.commit()

    resultaat = get_bundle(conn, "a1")
    assert len(resultaat) == 2, "Alleen in_bundle=1 rijen verwacht"
    chunk_ids = [r[0] for r in resultaat]
    scores = [r[1] for r in resultaat]
    assert chunk_ids[0] == "c1", "Hoogste score moet eerst komen"
    assert chunk_ids[1] == "c2"
    assert scores[0] > scores[1], "Score moet aflopend zijn"
    assert "c3" not in chunk_ids, "c3 heeft in_bundle=0 en mag niet teruggegeven worden"

    conn.close()


def test_get_bundle_leeg_voor_onbekend_anchor(tmp_path: Path):
    """Onbekend anchor → lege lijst, geen fout."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)
    resultaat = get_bundle(conn, "bestaat-niet")
    assert resultaat == []
    conn.close()


# ---------------------------------------------------------------------------
# Test 3: vector_hash
# ---------------------------------------------------------------------------

def test_vector_hash_reproduceerbaar():
    """Dezelfde vector geeft altijd dezelfde hash."""
    v = [0.1, 0.2, 0.3, -0.4]
    assert _vector_hash(v) == _vector_hash(v)


def test_vector_hash_is_16_hex():
    """Hash is altijd 16 hex-tekens."""
    v = _unit_vector(128, seed=42)
    h = _vector_hash(v)
    assert len(h) == 16
    assert all(c in "0123456789abcdef" for c in h)


def test_vector_hash_verschilt_bij_andere_vector():
    """Andere vector → andere hash (met grote zekerheid)."""
    v1 = _unit_vector(128, seed=1)
    v2 = _unit_vector(128, seed=2)
    assert _vector_hash(v1) != _vector_hash(v2)


# ---------------------------------------------------------------------------
# Test 4: berekend_delta
# ---------------------------------------------------------------------------

def _vul_store(conn: sqlite3.Connection, rijen: list[dict]):
    """Helper: schrijf rijen in de store."""
    for r in rijen:
        conn.execute(
            "INSERT INTO matches (anchor_id, chunk_id, score, in_bundle, chunk_sha, anchor_vector_hash) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (r["anchor_id"], r["chunk_id"], r["score"], r["in_bundle"],
             r.get("chunk_sha"), r.get("anchor_vector_hash")),
        )
    conn.commit()


def test_delta_detectie_geen_delta(tmp_path: Path):
    """Identieke staat → alle delta-sets zijn leeg."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    vector_hash = "abcdef0123456789"
    chunk_sha = "sha1aaa"

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": chunk_sha, "anchor_vector_hash": vector_hash},
    ])

    huidige_chunks = {"c1": chunk_sha}
    huidige_anchors = {"a1": vector_hash}

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert chunks_weg == set()
    assert chunks_nieuw == set()
    assert chunks_stale == set()
    assert anchors_weg == set()
    assert anchors_nieuw == set()
    assert anchors_stale == set()
    conn.close()


def test_delta_detectie_chunks_weg(tmp_path: Path):
    """Chunk verwijderd uit ChromaDB → chunks_weg bevat die chunk_id."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": "sha1", "anchor_vector_hash": "hash1"},
        {"anchor_id": "a1", "chunk_id": "c2", "score": 0.7, "in_bundle": 1,
         "chunk_sha": "sha2", "anchor_vector_hash": "hash1"},
    ])

    # c2 is weg uit ChromaDB
    huidige_chunks = {"c1": "sha1"}
    huidige_anchors = {"a1": "hash1"}

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert "c2" in chunks_weg
    assert "c1" not in chunks_weg
    assert chunks_nieuw == set()
    assert chunks_stale == set()
    conn.close()


def test_delta_detectie_chunks_nieuw(tmp_path: Path):
    """Nieuwe chunk in ChromaDB → chunks_nieuw bevat die chunk_id."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": "sha1", "anchor_vector_hash": "hash1"},
    ])

    # c2 is nieuw in ChromaDB
    huidige_chunks = {"c1": "sha1", "c2": "sha2"}
    huidige_anchors = {"a1": "hash1"}

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert "c2" in chunks_nieuw
    assert chunks_weg == set()
    assert chunks_stale == set()
    conn.close()


def test_delta_detectie_chunks_stale(tmp_path: Path):
    """Gewijzigde chunk_sha → chunks_stale bevat die chunk_id."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": "sha-oud", "anchor_vector_hash": "hash1"},
    ])

    huidige_chunks = {"c1": "sha-nieuw"}  # sha veranderd
    huidige_anchors = {"a1": "hash1"}

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert "c1" in chunks_stale
    assert chunks_weg == set()
    assert chunks_nieuw == set()
    conn.close()


def test_delta_detectie_anchors_weg(tmp_path: Path):
    """Anchor verwijderd uit anchors.json → anchors_weg bevat die anchor_id."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": "sha1", "anchor_vector_hash": "hash1"},
        {"anchor_id": "a2", "chunk_id": "c1", "score": 0.6, "in_bundle": 0,
         "chunk_sha": "sha1", "anchor_vector_hash": "hash2"},
    ])

    # a2 is weg
    huidige_chunks = {"c1": "sha1"}
    huidige_anchors = {"a1": "hash1"}

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert "a2" in anchors_weg
    assert "a1" not in anchors_weg
    conn.close()


def test_delta_detectie_anchors_stale(tmp_path: Path):
    """Gewijzigde anchor_vector_hash → anchors_stale bevat die anchor_id."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    _vul_store(conn, [
        {"anchor_id": "a1", "chunk_id": "c1", "score": 0.8, "in_bundle": 1,
         "chunk_sha": "sha1", "anchor_vector_hash": "hash-oud"},
    ])

    huidige_chunks = {"c1": "sha1"}
    huidige_anchors = {"a1": "hash-nieuw"}  # hash veranderd

    (chunks_weg, chunks_nieuw, chunks_stale,
     anchors_weg, anchors_nieuw, anchors_stale) = match_bronnen.berekend_delta(
        conn, huidige_chunks, huidige_anchors
    )

    assert "a1" in anchors_stale
    assert anchors_weg == set()
    assert anchors_nieuw == set()
    conn.close()


# ---------------------------------------------------------------------------
# Test 5: herbereken_bundle_voor_anchors (strict re-rank)
# ---------------------------------------------------------------------------

def test_herbereken_bundle_strict_rerank(tmp_path: Path):
    """
    Strict re-rank: bestaand bundle met chunks A,B,C; voeg chunk D toe met hogere score
    → in_bundle flag herberekend zodat lagere chunks mogelijk eruit vallen.
    """
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    dim = 16
    # Anchor-vector
    anchor_vec = np.zeros((1, dim), dtype=np.float32)
    anchor_vec[0, 0] = 1.0  # puur in richting 0

    # Chunks: C1 is bijna gelijk aan anchor (hoge score), C2 matig, C3 laag
    chunk_vecs = np.zeros((3, dim), dtype=np.float32)
    chunk_vecs[0, 0] = 1.0   # C1: score ≈ 1.0
    chunk_vecs[1, 0] = 0.8   # C2: middel
    chunk_vecs[1, 1] = 0.6
    chunk_vecs[2, 0] = 0.3   # C3: laag
    chunk_vecs[2, 2] = 0.9

    # Normaliseer
    chunk_vecs = chunk_vecs / np.linalg.norm(chunk_vecs, axis=1, keepdims=True)

    chunk_ids = ["c1", "c2", "c3"]
    chunk_metas = [{"chunk_sha": f"sha{i}"} for i in range(3)]

    anchors = [{"anchor_id": "a1"}]

    vector_hash = "testhash12345678"
    anchor_vector_hashes = {"a1": vector_hash}

    # Threshold = 0.55, margin = 0.15
    # top1 ≈ 1.0, anchor_threshold = max(0.55, 1.0 - 0.15) = 0.85
    # Alleen c1 (score ≈ 1.0) en eventueel c2 komen boven 0.85

    match_bronnen.herbereken_bundle_voor_anchors(
        conn=conn,
        anchor_ids_te_herbereken={"a1"},
        anchors=anchors,
        anchor_vecs=anchor_vec,
        chunk_ids=chunk_ids,
        chunk_vecs=chunk_vecs,
        chunk_metas=chunk_metas,
        anchor_vector_hashes=anchor_vector_hashes,
        threshold=0.55,
        margin=0.15,
    )

    # C3 heeft een lage score en mag niet in de bundle zitten
    bundle = get_bundle(conn, "a1")
    bundle_chunk_ids = [r[0] for r in bundle]
    assert "c1" in bundle_chunk_ids, "c1 (hoge score) moet in bundle zitten"
    assert "c3" not in bundle_chunk_ids, "c3 (lage score) mag niet in bundle zitten"
    conn.close()


def test_herbereken_bundle_idempotent(tmp_path: Path):
    """Tweede herbereken zonder mutaties → zelfde staat, idempotent."""
    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    dim = 8
    anchor_vec = np.ones((1, dim), dtype=np.float32)
    anchor_vec = anchor_vec / np.linalg.norm(anchor_vec, axis=1, keepdims=True)

    chunk_vecs = np.ones((2, dim), dtype=np.float32)
    chunk_vecs[1, :] = -1.0  # tegenovergesteld
    chunk_vecs = chunk_vecs / np.linalg.norm(chunk_vecs, axis=1, keepdims=True)

    chunk_ids = ["c_pos", "c_neg"]
    chunk_metas = [{"chunk_sha": "sha_pos"}, {"chunk_sha": "sha_neg"}]
    anchors = [{"anchor_id": "a1"}]
    anchor_vector_hashes = {"a1": "hash1234abcd5678"}

    kwargs = dict(
        anchor_ids_te_herbereken={"a1"},
        anchors=anchors,
        anchor_vecs=anchor_vec,
        chunk_ids=chunk_ids,
        chunk_vecs=chunk_vecs,
        chunk_metas=chunk_metas,
        anchor_vector_hashes=anchor_vector_hashes,
        threshold=0.4,
        margin=0.2,
    )

    # Eerste run
    match_bronnen.herbereken_bundle_voor_anchors(conn=conn, **kwargs)
    bundle_1 = get_bundle(conn, "a1")

    # Tweede run
    match_bronnen.herbereken_bundle_voor_anchors(conn=conn, **kwargs)
    bundle_2 = get_bundle(conn, "a1")

    assert [r[0] for r in bundle_1] == [r[0] for r in bundle_2], \
        "Tweede run moet dezelfde bundle opleveren"
    conn.close()


# ---------------------------------------------------------------------------
# Test 6: eerste-run incrementele fill (end-to-end met gemockte ChromaDB)
# ---------------------------------------------------------------------------

def _maak_fake_chroma(chunk_ids: list[str], chunk_vecs: np.ndarray, chunk_shas: list[str]):
    """Bouw een minimale fake ChromaDB-response voor current_chunks_with_sha."""
    fake_col = MagicMock()
    fake_col.count.return_value = len(chunk_ids)
    fake_col.get.return_value = {
        "ids": chunk_ids,
        "embeddings": chunk_vecs.tolist(),
        "metadatas": [{"chunk_sha": sha} for sha in chunk_shas],
    }
    fake_client = MagicMock()
    fake_client.get_collection.return_value = fake_col
    return fake_client, fake_col


def test_eerste_run_vult_store(tmp_path: Path):
    """
    Eerste run: gemockte ChromaDB met 3 chunks + 2 anchors → store gevuld
    met de juiste rijen + bundles.
    """
    dim = 8
    # Twee anchors: a1 gericht op c1, a2 gericht op c3
    anchor_vecs = np.zeros((2, dim), dtype=np.float32)
    anchor_vecs[0, 0] = 1.0  # a1 → richting 0
    anchor_vecs[1, 3] = 1.0  # a2 → richting 3
    anchor_vecs = anchor_vecs / np.linalg.norm(anchor_vecs, axis=1, keepdims=True)

    chunk_vecs = np.zeros((3, dim), dtype=np.float32)
    chunk_vecs[0, 0] = 1.0  # c1: hoge score voor a1
    chunk_vecs[1, 1] = 1.0  # c2: laag voor beide
    chunk_vecs[2, 3] = 1.0  # c3: hoge score voor a2

    chunk_ids = ["c1", "c2", "c3"]
    chunk_shas = ["sha1", "sha2", "sha3"]

    anchors = [
        {"anchor_id": "a1"},
        {"anchor_id": "a2"},
    ]
    anchor_vector_hashes = {
        "a1": _vector_hash(anchor_vecs[0].tolist()),
        "a2": _vector_hash(anchor_vecs[1].tolist()),
    }

    db_path = tmp_path / "matches.sqlite3"
    conn = open_store(db_path)

    # Alle anchors herbereken (eerste run)
    match_bronnen.herbereken_bundle_voor_anchors(
        conn=conn,
        anchor_ids_te_herbereken={"a1", "a2"},
        anchors=anchors,
        anchor_vecs=anchor_vecs,
        chunk_ids=chunk_ids,
        chunk_vecs=chunk_vecs,
        chunk_metas=[{"chunk_sha": sha} for sha in chunk_shas],
        anchor_vector_hashes=anchor_vector_hashes,
        threshold=0.55,
        margin=0.15,
    )

    bundle_a1 = get_bundle(conn, "a1")
    bundle_a2 = get_bundle(conn, "a2")

    assert len(bundle_a1) >= 1, "a1 moet minstens c1 in zijn bundle hebben"
    assert bundle_a1[0][0] == "c1", "c1 moet top-1 zijn voor a1"
    assert bundle_a2[0][0] == "c3", "c3 moet top-1 zijn voor a2"

    totaal_rijen = conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
    assert totaal_rijen > 0, "Store moet rijen bevatten na eerste run"

    conn.close()
