"""
Bron-first matching — delta-driven, SQLite-store (ADR-005 §9.1).

Globale matching: alle anchors van alle 19 PO's tegelijk tegen alle bron-chunks.
Geen per-PO scope-filter — een chunk kan in bundles van meerdere ankers belanden,
ook cross-PO. Anchor-vectors zijn pre-computed in `data/programma/anchors.json` (eenmalig
ge-embed), dus geen runtime-embedding meer.

Delta-algoritme (ADR-005 §9.1):
  1. Vergelijk huidige ChromaDB-chunks met store (chunks_weg, chunks_nieuw, chunks_stale).
  2. Vergelijk huidige anchors.json-vectorhashes met store (anchors_weg, anchors_nieuw, anchors_stale).
  3. DELETE rijen voor verwijderde chunks + verwijderde anchors.
  4. Herberekening: alle anchors die geraakt worden door nieuwe/stale chunks of
     eigen vector-wijziging krijgen een nieuwe cosine-pass. Batch-gewijs via numpy.
  5. Strict re-rank: per geraakte anchor, herbereken de bundle (in_bundle flag bijwerken).
  6. Samenvatting: aantal chunks toegevoegd/verwijderd, rijen verwijderd, anchors herrankt.

Gebruik:
  python3 -m tools.extractie.match_bronnen
  python3 -m tools.extractie.match_bronnen --threshold 0.55 --margin 0.15
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

import chromadb
import numpy as np
from tqdm import tqdm

from tools.lib.matches_store import (
    DEFAULT_ANCHORS_PATH,
    DEFAULT_CHROMA_PATH,
    DEFAULT_DB_PATH,
    current_anchors_with_hash,
    current_chunks_with_sha,
    open_store,
    _vector_hash,
)

ROOT = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# Cosine-helpers
# ---------------------------------------------------------------------------

def cosine_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Cosine-similarity matrix tussen rijen van a en b."""
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return a_norm @ b_norm.T


# ---------------------------------------------------------------------------
# Anchors laden
# ---------------------------------------------------------------------------

def load_anchors(anchors_path: Path) -> tuple[list[dict], np.ndarray]:
    """Laad anchors en hun vectors uit anchors.json."""
    if not anchors_path.exists():
        raise SystemExit(
            f"data/programma/anchors.json niet gevonden — run build_anchors.py + embed_anchors.py"
        )
    data = json.loads(anchors_path.read_text(encoding="utf-8"))
    anchors = data["anchors"]
    missing = [a["anchor_id"] for a in anchors if a.get("vector") is None]
    if missing:
        raise SystemExit(
            f"{len(missing)} anchors hebben geen vector — run "
            f"`python3 -m tools.extractie.embed_anchors`"
        )
    vectors = np.array([a["vector"] for a in anchors], dtype=np.float32)
    return anchors, vectors


# ---------------------------------------------------------------------------
# Chunks laden uit ChromaDB
# ---------------------------------------------------------------------------

def load_chunks(
    chroma_path: Path,
) -> tuple[list[str], np.ndarray, list[dict]]:
    """Laad alle chunk-ids, embeddings en metadatas uit ChromaDB."""
    if not chroma_path.exists():
        raise SystemExit(f"data/rag/main niet gevonden — bouw eerst de RAG-index")
    client = chromadb.PersistentClient(path=str(chroma_path))
    col = client.get_collection("bronnen")
    print(f"  ChromaDB collection 'bronnen': {col.count()} chunks totaal")
    print(f"  embeddings ophalen (kan even duren bij grote corpus)...")
    data = col.get(include=["embeddings", "metadatas"])
    return data["ids"], np.array(data["embeddings"], dtype=np.float32), data["metadatas"]


# ---------------------------------------------------------------------------
# Delta-berekening
# ---------------------------------------------------------------------------

def _chroma_fingerprint(huidige_chunks: dict[str, str | None]) -> str:
    """
    Bereken een fingerprint van de volledige ChromaDB-staat.

    Sha256 van gesorteerde 'chunk_id:sha' paren. Detecteert toevoegen/verwijderen/
    wijzigen van chunks ook als ze nooit boven de threshold komen (en dus niet in de
    matches-tabel staan). Eerste 16 hex-tekens.
    """
    parts = sorted(f"{cid}:{sha or ''}" for cid, sha in huidige_chunks.items())
    combined = "\n".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:16]


def _sla_meta_op(conn: sqlite3.Connection, sleutel: str, waarde: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO meta (sleutel, waarde) VALUES (?, ?)",
        (sleutel, waarde),
    )


def _lees_meta(conn: sqlite3.Connection, sleutel: str) -> str | None:
    row = conn.execute(
        "SELECT waarde FROM meta WHERE sleutel = ?", (sleutel,)
    ).fetchone()
    return row[0] if row else None


def _store_chunks(conn: sqlite3.Connection) -> dict[str, str | None]:
    """Lees huidige (chunk_id, chunk_sha) uit de store."""
    rows = conn.execute("SELECT DISTINCT chunk_id, chunk_sha FROM matches").fetchall()
    return {row[0]: row[1] for row in rows}


def _store_anchors(conn: sqlite3.Connection) -> dict[str, str | None]:
    """Lees huidige (anchor_id, anchor_vector_hash) uit de store — één rij per anchor is genoeg."""
    rows = conn.execute(
        "SELECT anchor_id, anchor_vector_hash FROM matches GROUP BY anchor_id"
    ).fetchall()
    return {row[0]: row[1] for row in rows}


def berekend_delta(
    conn: sqlite3.Connection,
    huidige_chunks: dict[str, str | None],
    huidige_anchors: dict[str, str],
) -> tuple[set[str], set[str], set[str], set[str], set[str], set[str]]:
    """
    Bepaal de delta tussen de huidige toestand en de store.

    Returns:
        chunks_weg       — chunk_ids die niet meer in ChromaDB bestaan
        chunks_nieuw     — chunk_ids die nieuw zijn (niet in store)
        chunks_stale     — chunk_ids waarvan chunk_sha veranderd is
        anchors_weg      — anchor_ids die niet meer in anchors.json bestaan
        anchors_nieuw    — anchor_ids die nieuw zijn (niet in store)
        anchors_stale    — anchor_ids waarvan vector_hash veranderd is
    """
    opgeslagen_chunks = _store_chunks(conn)
    opgeslagen_anchors = _store_anchors(conn)

    # Chunks
    chunks_weg = set(opgeslagen_chunks.keys()) - set(huidige_chunks.keys())
    chunks_nieuw = set(huidige_chunks.keys()) - set(opgeslagen_chunks.keys())
    chunks_stale: set[str] = set()
    for cid, sha in huidige_chunks.items():
        if cid in opgeslagen_chunks and opgeslagen_chunks[cid] != sha:
            chunks_stale.add(cid)

    # Anchors
    anchors_weg = set(opgeslagen_anchors.keys()) - set(huidige_anchors.keys())
    anchors_nieuw = set(huidige_anchors.keys()) - set(opgeslagen_anchors.keys())
    anchors_stale: set[str] = set()
    for aid, hash_val in huidige_anchors.items():
        if aid in opgeslagen_anchors and opgeslagen_anchors[aid] != hash_val:
            anchors_stale.add(aid)

    return chunks_weg, chunks_nieuw, chunks_stale, anchors_weg, anchors_nieuw, anchors_stale


# ---------------------------------------------------------------------------
# Anchors bepalen die herberekend moeten worden
# ---------------------------------------------------------------------------

def _anchors_getroffen_door_chunk_delta(
    conn: sqlite3.Connection,
    chunks_weg: set[str],
    chunks_nieuw: set[str],
    chunks_stale: set[str],
) -> set[str]:
    """
    Geef alle anchor_ids terug die een match hebben (of hadden) met gewijzigde chunks.

    Chunks die weg zijn of stale zijn kunnen bestaande bundels ongeldig maken —
    die anchors moeten herrankt worden. Nieuwe chunks zijn potentieel relevant
    voor ALLE anchors (we weten niet a-priori welke).
    """
    geraakt: set[str] = set()

    # Anchors geraakt door verwijderde of stale chunks (stonden al in store)
    betrokken = chunks_weg | chunks_stale
    if betrokken:
        placeholders = ",".join("?" * len(betrokken))
        rows = conn.execute(
            f"SELECT DISTINCT anchor_id FROM matches WHERE chunk_id IN ({placeholders})",
            list(betrokken),
        ).fetchall()
        for row in rows:
            geraakt.add(row[0])

    # Als er nieuwe chunks zijn: alle anchors (nieuwe chunks kunnen voor elk anchor relevant zijn)
    if chunks_nieuw:
        rows = conn.execute("SELECT DISTINCT anchor_id FROM matches").fetchall()
        for row in rows:
            geraakt.add(row[0])

    return geraakt


# ---------------------------------------------------------------------------
# Bundle-berekening (strict re-rank)
# ---------------------------------------------------------------------------

def herbereken_bundle_voor_anchors(
    conn: sqlite3.Connection,
    anchor_ids_te_herbereken: set[str],
    anchors: list[dict],
    anchor_vecs: np.ndarray,
    chunk_ids: list[str],
    chunk_vecs: np.ndarray,
    chunk_metas: list[dict],
    anchor_vector_hashes: dict[str, str],
    threshold: float,
    margin: float,
) -> tuple[int, int]:
    """
    Herbereken scores + in_bundle flag voor de opgegeven anchors.

    Batch-gewijs cosine-berekening (alleen de betrokken anker-rijen × alle chunks).

    Returns:
        (aantal_rijen_verwijderd, aantal_rijen_toegevoegd)
    """
    if not anchor_ids_te_herbereken:
        return 0, 0

    # Bouw index: anchor_id → positie in de anchors-lijst
    anchor_index: dict[str, int] = {a["anchor_id"]: i for i, a in enumerate(anchors)}
    chunk_sha_by_id: dict[str, str | None] = {
        cid: meta.get("chunk_sha") for cid, meta in zip(chunk_ids, chunk_metas)
    }
    chunk_id_to_idx: dict[str, int] = {cid: i for i, cid in enumerate(chunk_ids)}

    n_verwijderd = 0
    n_toegevoegd = 0

    # Verwerk in batches van 50 anchors om geheugengebruik beheersbaar te houden
    anchor_ids_lijst = sorted(anchor_ids_te_herbereken)
    batch_grootte = 50

    for batch_start in range(0, len(anchor_ids_lijst), batch_grootte):
        batch_anchor_ids = anchor_ids_lijst[batch_start: batch_start + batch_grootte]
        batch_indices = [anchor_index[aid] for aid in batch_anchor_ids if aid in anchor_index]
        if not batch_indices:
            continue

        # Cosine-matrix voor deze batch
        batch_vecs = anchor_vecs[batch_indices, :]  # (B, D)
        sim = cosine_matrix(batch_vecs, chunk_vecs)  # (B, N_chunks)

        for local_idx, anchor_id in enumerate(batch_anchor_ids):
            if anchor_id not in anchor_index:
                continue
            scores = sim[local_idx, :]  # (N_chunks,)
            top1_score = float(scores.max())
            anchor_threshold = max(threshold, top1_score - margin)

            # Welke chunks horen in de bundle?
            ranked_idx = np.argsort(-scores)
            bundle_set: set[str] = set()
            for j in ranked_idx:
                score = float(scores[j])
                if score >= anchor_threshold:
                    bundle_set.add(chunk_ids[j])
                else:
                    break

            vector_hash = anchor_vector_hashes.get(anchor_id, "")

            # Verwijder bestaande rijen voor dit anchor
            verwijderd = conn.execute(
                "DELETE FROM matches WHERE anchor_id = ?", (anchor_id,)
            ).rowcount
            n_verwijderd += verwijderd

            # Schrijf alle rijen (ook buiten bundle — voor re-rank bij toekomstige delta's)
            # Schrijf alleen de bundel-rijen + de directe runners-up (tot 2× de bundle-drempel)
            # om de store niet te laten exploderen. We schrijven alle chunks >= threshold.
            rijen: list[tuple] = []
            for j in ranked_idx:
                score = float(scores[j])
                if score < threshold:
                    break
                cid = chunk_ids[j]
                in_bundle = 1 if cid in bundle_set else 0
                chunk_sha = chunk_sha_by_id.get(cid)
                rijen.append((anchor_id, cid, score, in_bundle, chunk_sha, vector_hash))

            conn.executemany(
                "INSERT OR REPLACE INTO matches "
                "(anchor_id, chunk_id, score, in_bundle, chunk_sha, anchor_vector_hash) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                rijen,
            )
            n_toegevoegd += len(rijen)

    conn.commit()
    return n_verwijderd, n_toegevoegd


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.55,
        help="absolute floor cosine-drempel (default 0.55)",
    )
    parser.add_argument(
        "--margin",
        type=float,
        default=0.15,
        help="chunk in bundle als score >= max(threshold, top1 - margin) (default 0.15)",
    )
    parser.add_argument(
        "--db-path",
        type=Path,
        default=None,
        help="pad naar SQLite-store (default: data/extractie/matches.sqlite3)",
    )
    parser.add_argument(
        "--chroma-path",
        type=Path,
        default=None,
        help="pad naar ChromaDB (default: data/rag/main)",
    )
    parser.add_argument(
        "--anchors-path",
        type=Path,
        default=None,
        help="pad naar anchors.json (default: data/programma/anchors.json)",
    )
    args = parser.parse_args()

    db_path = args.db_path or DEFAULT_DB_PATH
    chroma_path = args.chroma_path or DEFAULT_CHROMA_PATH
    anchors_path = args.anchors_path or DEFAULT_ANCHORS_PATH

    print("[store] SQLite-store openen/initialiseren...")
    conn = open_store(db_path)
    print(f"  {db_path.relative_to(ROOT)}")

    print("[anchors] laden...")
    anchors, anchor_vecs = load_anchors(anchors_path)
    anchor_vector_hashes = current_anchors_with_hash(anchors_path)
    print(f"  {len(anchors)} anchors met vectors ({anchor_vecs.shape[1]} dims)")

    print("[chunks] laden uit ChromaDB...")
    chunk_ids, chunk_vecs, chunk_metas = load_chunks(chroma_path)
    n_chunks = len(chunk_ids)
    huidige_chunks = current_chunks_with_sha(chroma_path)
    print(f"  {n_chunks} chunks geladen")

    # Per bron_rol breakdown
    by_rol: dict[str, int] = {}
    for m in chunk_metas:
        rol = m.get("bron_rol", "?")
        by_rol[rol] = by_rol.get(rol, 0) + 1
    print(f"  per bron_rol: {by_rol}")

    print("[delta] diff berekenen...")
    # Bereken fingerprint van de huidige ChromaDB-staat (inclusief chunks die niet in store staan)
    huidige_chroma_fingerprint = _chroma_fingerprint(huidige_chunks)
    opgeslagen_chroma_fingerprint = _lees_meta(conn, "chroma_fingerprint")

    # Bereken fingerprint van de huidige anchors-staat
    huidige_anchors_fingerprint = _chroma_fingerprint(anchor_vector_hashes)
    opgeslagen_anchors_fingerprint = _lees_meta(conn, "anchors_fingerprint")

    # Idempotentie: als beide fingerprints overeenkomen → niks te doen
    if (huidige_chroma_fingerprint == opgeslagen_chroma_fingerprint
            and huidige_anchors_fingerprint == opgeslagen_anchors_fingerprint):
        store_rijen = conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
        if store_rijen > 0:
            print("\n[idempotent] Geen delta gedetecteerd — store is up-to-date. Niets te doen.")
            conn.close()
            return

    (
        chunks_weg,
        chunks_nieuw,
        chunks_stale,
        anchors_weg,
        anchors_nieuw,
        anchors_stale,
    ) = berekend_delta(conn, huidige_chunks, anchor_vector_hashes)

    is_eerste_run = (
        conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0] == 0
    )

    print(f"  chunks_weg: {len(chunks_weg)}")
    print(f"  chunks_nieuw: {len(chunks_nieuw)}")
    print(f"  chunks_stale: {len(chunks_stale)}")
    print(f"  anchors_weg: {len(anchors_weg)}")
    print(f"  anchors_nieuw: {len(anchors_nieuw)}")
    print(f"  anchors_stale: {len(anchors_stale)}")

    # Stap 1: DELETE verwijderde chunks
    n_chunk_rijen_verwijderd = 0
    if chunks_weg:
        print(f"\n[cleanup] {len(chunks_weg)} verwijderde chunks verwijderen uit store...")
        for cid in chunks_weg:
            n_chunk_rijen_verwijderd += conn.execute(
                "DELETE FROM matches WHERE chunk_id = ?", (cid,)
            ).rowcount
        conn.commit()
        print(f"  {n_chunk_rijen_verwijderd} rijen verwijderd")

    # Stap 2: DELETE verwijderde anchors
    n_anchor_rijen_verwijderd = 0
    if anchors_weg:
        print(f"[cleanup] {len(anchors_weg)} verwijderde anchors verwijderen uit store...")
        for aid in anchors_weg:
            n_anchor_rijen_verwijderd += conn.execute(
                "DELETE FROM matches WHERE anchor_id = ?", (aid,)
            ).rowcount
        conn.commit()
        print(f"  {n_anchor_rijen_verwijderd} rijen verwijderd")

    # Stap 3: Bepaal welke anchors herberekend moeten worden
    # - anchors_nieuw: moeten volledig ingevuld worden
    # - anchors_stale: eigen vector veranderd → volledig herberekenen
    # - anchors getroffen door chunks_weg/chunks_stale/chunks_nieuw: herranken

    anchors_te_herbereken: set[str] = set()
    anchors_te_herbereken |= anchors_nieuw
    anchors_te_herbereken |= anchors_stale

    # Anchors geraakt door chunk-delta
    geraakt_door_chunks = _anchors_getroffen_door_chunk_delta(
        conn, chunks_weg, chunks_nieuw, chunks_stale
    )
    anchors_te_herbereken |= geraakt_door_chunks

    # Bij eerste run: alle anchors
    if is_eerste_run or not conn.execute("SELECT 1 FROM matches LIMIT 1").fetchone():
        anchors_te_herbereken = {a["anchor_id"] for a in anchors}

    print(f"\n[herbereken] {len(anchors_te_herbereken)} anchors te herbereken "
          f"(threshold={args.threshold}, margin={args.margin})...")

    if anchors_te_herbereken:
        n_verwijderd, n_toegevoegd = herbereken_bundle_voor_anchors(
            conn=conn,
            anchor_ids_te_herbereken=anchors_te_herbereken,
            anchors=anchors,
            anchor_vecs=anchor_vecs,
            chunk_ids=chunk_ids,
            chunk_vecs=chunk_vecs,
            chunk_metas=chunk_metas,
            anchor_vector_hashes=anchor_vector_hashes,
            threshold=args.threshold,
            margin=args.margin,
        )
        print(f"  {n_verwijderd} rijen verwijderd, {n_toegevoegd} rijen toegevoegd")

    # Sla fingerprints op zodat volgende run idempotent-check kan doen
    _sla_meta_op(conn, "chroma_fingerprint", huidige_chroma_fingerprint)
    _sla_meta_op(conn, "anchors_fingerprint", huidige_anchors_fingerprint)
    conn.commit()

    # Samenvatting
    totaal_rijen = conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
    totaal_bundles = conn.execute("SELECT COUNT(*) FROM matches WHERE in_bundle = 1").fetchone()[0]
    anchors_met_bundle = conn.execute(
        "SELECT COUNT(DISTINCT anchor_id) FROM matches WHERE in_bundle = 1"
    ).fetchone()[0]
    anchors_zonder_bundle = len(anchors) - anchors_met_bundle

    print("\n[samenvatting]")
    print(f"  chunks toegevoegd (nieuw in ChromaDB): {len(chunks_nieuw)}")
    print(f"  chunks verwijderd (weg uit ChromaDB): {len(chunks_weg)}")
    print(f"  chunks stale (sha gewijzigd): {len(chunks_stale)}")
    print(f"  anchors nieuw: {len(anchors_nieuw)}")
    print(f"  anchors stale (vector gewijzigd): {len(anchors_stale)}")
    print(f"  anchors herrankt: {len(anchors_te_herbereken)}")
    print(f"  store: {totaal_rijen} rijen totaal, {totaal_bundles} in bundle")
    print(f"  anchors met bundle: {anchors_met_bundle}/{len(anchors)}")
    if anchors_zonder_bundle:
        print(f"  WAARSCHUWING: {anchors_zonder_bundle} anchors hebben geen bundle "
              f"(score te laag — controleer threshold)")
    print(f"\n  DB: {db_path.relative_to(ROOT)}")

    conn.close()


if __name__ == "__main__":
    main()
