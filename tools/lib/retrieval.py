"""
Gedeelde retrieval-bibliotheek voor Certificaid RAG.

Implementeert de twee-fase pipeline (ADR-003):
  1. Bi-encoder (bge-m3): snel, hoge recall — haal top-N kandidaten op
  2. Cross-encoder (bge-reranker-v2-m3): precies, lage latency — rerank en filter

Context-uitbreiding (ADR-002):
  - Wetteksten: gevonden artikel ± 2 omliggende artikelen (begrensd, geen volledige wet)
  - Adviezen: chunk IS al het volledige advies (voor < 40K chars); geen extra uitbreiding nodig

Gebruik:
  from lib.retrieval import build_retrieval_stack, retrieve_and_rerank, RetrievalResult
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from sentence_transformers import CrossEncoder

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "BAAI/bge-m3"
RERANKER_MODEL  = "BAAI/bge-reranker-v2-m3"
CHROMA_PATH     = Path(__file__).parent.parent.parent / "data" / "chroma_db"

ALL_COLLECTIONS = ["bronnen", "concepten"]   # ADR-006: twee collections
BRONNEN_COLS    = ["bronnen"]


# ---------------------------------------------------------------------------
# Dataclass
# ---------------------------------------------------------------------------

@dataclass
class RetrievalResult:
    collection:   str
    chunk_id:     str
    score:        float   # bi-encoder cosine similarity (0–1)
    rerank_score: float   # cross-encoder score (0–1); -1 = niet gereranked
    bron:         str
    artikel:      str
    text:         str     # chunk-tekst (mogelijk uitgebreid met context)
    meta:         dict = field(default_factory=dict)

    def label(self) -> str:
        """Korte bronvermelding voor display."""
        return f"{self.bron} — {self.artikel}" if self.artikel else self.bron


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

def _detect_device() -> str:
    """
    Default device voor retrieval (query-time): CPU.

    Bewust CPU als default omdat:
    - Een query is één korte zin → bi-encoder embedding in <100ms op CPU
    - Reranker scoort hooguit ~50 (query, chunk) paren → snel op CPU
    - MPS geheugen blijft vrij voor zwaardere taken (indexering, tutor, andere apps)
    - Vermijdt MPS allocator concurrentie met Claude Desktop op machines met
      beperkt unified memory

    Override via build_retrieval_stack(device="mps") indien expliciet gewenst.
    """
    return "cpu"


def build_retrieval_stack(
    chroma_path: Path = CHROMA_PATH,
    device: str | None = None,
    reranker_device: str | None = None,
):
    """
    Laad ChromaDB-client, embedding-functie en reranker (gecached door Streamlit).

    device: device voor de bi-encoder (query-embedding). Default = CPU.
    reranker_device: device voor de cross-encoder. Default = CPU.

    Splitsing is bewust: de reranker voert een forward-pass uit over (query, chunk)-paren
    en verbruikt significant meer actief MPS-geheugen dan de bi-encoder. Op een Mac met
    Claude Desktop actief (5–6 GiB MPS bezet) kan dit leiden tot OOM. Tutor gebruikt
    daarom MPS voor de bi-encoder en CPU voor de reranker.
    """
    device = device or _detect_device()
    reranker_device = reranker_device or "cpu"
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device=device)
    client = chromadb.PersistentClient(path=str(chroma_path))
    reranker = CrossEncoder(RERANKER_MODEL, device=reranker_device)
    return client, ef, reranker


def open_collections(client, ef, names: list[str] = ALL_COLLECTIONS) -> dict:
    """Open bestaande ChromaDB-collections; sla ontbrekende stil over."""
    cols = {}
    for name in names:
        try:
            cols[name] = client.get_collection(name, embedding_function=ef)
        except Exception:
            pass
    return cols


# ---------------------------------------------------------------------------
# Fase 1: bi-encoder retrieval
# ---------------------------------------------------------------------------

def _retrieve_candidates(
    collections: dict,
    query: str,
    selected_cols: list[str],
    bi_top_n: int,
    bron_rollen: list[str] | None = None,
) -> list[RetrievalResult]:
    """
    Haal bi_top_n kandidaten op per collection.
    bron_rollen: optionele where-filter op metadata `bron_rol`
    (bv. ["wettekst", "norm"] beperkt resultaten in de `bronnen`-collection).
    """
    results: list[RetrievalResult] = []
    for name in selected_cols:
        col = collections.get(name)
        if col is None:
            continue
        count = col.count()
        if count == 0:
            continue

        where = None
        if bron_rollen and name == "bronnen":
            if len(bron_rollen) == 1:
                where = {"bron_rol": {"$eq": bron_rollen[0]}}
            else:
                where = {"bron_rol": {"$in": bron_rollen}}

        res = col.query(
            query_texts=[query],
            n_results=min(bi_top_n, count),
            include=["documents", "metadatas", "distances"],
            where=where,
        )
        for doc, meta, dist, cid in zip(
            res["documents"][0], res["metadatas"][0],
            res["distances"][0], res["ids"][0],
        ):
            results.append(RetrievalResult(
                collection=name,
                chunk_id=cid,
                score=round(1 - dist, 4),
                rerank_score=-1.0,
                bron=meta.get("bron", ""),
                artikel=(
                    meta.get("artikel_ref")
                    or meta.get("sectie")
                    or meta.get("veld", "")
                ),
                text=doc,
                meta=meta,
            ))
    return results


# ---------------------------------------------------------------------------
# Fase 2: cross-encoder reranking
# ---------------------------------------------------------------------------

def _rerank(
    results: list[RetrievalResult],
    query: str,
    reranker: CrossEncoder,
) -> list[RetrievalResult]:
    if not results:
        return results
    pairs = [(query, r.text) for r in results]
    scores = reranker.predict(pairs)
    for r, s in zip(results, scores):
        r.rerank_score = float(s)
    results.sort(key=lambda x: x.rerank_score, reverse=True)
    return results


# ---------------------------------------------------------------------------
# Context-uitbreiding voor wetteksten (ADR-002)
# ---------------------------------------------------------------------------

def _art_nr_from_id(chunk_id: str) -> int:
    """Extraheer het artikel-nummer uit een chunk_id als `<bron>__art_<nr>`."""
    try:
        return int(chunk_id.split("__art_")[1])
    except (IndexError, ValueError):
        return 0


def _expand_wetteksten_context(
    result: RetrievalResult,
    collections: dict,
    n_neighbors: int = 2,
) -> str:
    """
    Laad het gevonden artikel ± n_neighbors omliggende artikelen.
    Bovengrens: 2 buren aan elke kant = max ~5 artikelen in context.
    Laadt NOOIT de volledige wettekst.

    Twee id-schema's:
    - ADR-006 §3.1 (unified bronnen): `<bron-stem>__art_<nr>`
      Artikel-nummer staat in het chunk_id; niet in metadata.
    - Legacy (wetteksten-collection): `<bestand>__chunk<n>`
      Nummer staat in `chunk_index`-metadata.
    """
    col = collections.get("bronnen") or collections.get("wetteksten")
    if col is None:
        return result.text

    meta = result.meta
    chunk_id = result.chunk_id
    use_art_schema = "__art_" in chunk_id

    if use_art_schema:
        bron_stem = chunk_id.split("__art_")[0]
        try:
            art_nr = int(chunk_id.split("__art_")[1])
        except (IndexError, ValueError):
            return result.text  # niet-numeriek artikelnummer (bv. "5bis") — geen uitbreiding
        neighbor_ids = [
            f"{bron_stem}__art_{art_nr + delta}"
            for delta in range(-n_neighbors, n_neighbors + 1)
            if delta != 0 and (art_nr + delta) >= 1
        ]
    elif meta.get("chunk_index") is not None:
        # Legacy id-schema (`<bestand_stem>__chunk{n}`)
        bestand_stem = meta.get("bestand", "").replace(".md", "")
        if not bestand_stem:
            return result.text
        chunk_idx = int(meta["chunk_index"])
        neighbor_ids = [
            f"{bestand_stem}__chunk{chunk_idx + delta}"
            for delta in range(-n_neighbors, n_neighbors + 1)
            if delta != 0 and (chunk_idx + delta) >= 1
        ]
    else:
        return result.text

    if not neighbor_ids:
        return result.text

    # In de unified `bronnen`-collection halen we ook wetteksten van andere bron-rollen op
    # als we alleen op ids filteren. Geen extra where-filter nodig: de neighbor_ids bevatten
    # al de bron-stem, dus we raken nooit norm- of advieschunks van dezelfde wettekst.
    try:
        res = col.get(ids=neighbor_ids, include=["documents", "metadatas"])

        if use_art_schema:
            # Sorteer op artikel-nummer in het chunk_id (niet in metadata)
            triples = sorted(
                zip(res["ids"], res["documents"], res["metadatas"]),
                key=lambda x: _art_nr_from_id(x[0]),
            )
            before = [doc for cid, doc, _ in triples if _art_nr_from_id(cid) < art_nr]
            after  = [doc for cid, doc, _ in triples if _art_nr_from_id(cid) > art_nr]
        else:
            # Legacy: sorteer op chunk_index in metadata
            pairs = sorted(
                zip(res["documents"], res["metadatas"]),
                key=lambda x: int(x[1].get("chunk_index", 0)),
            )
            before = [doc for doc, m in pairs if int(m.get("chunk_index", 0)) < chunk_idx]
            after  = [doc for doc, m in pairs if int(m.get("chunk_index", 0)) > chunk_idx]

        return "\n\n---\n\n".join(before + [result.text] + after)
    except Exception as exc:
        logger.debug("Context-uitbreiding mislukt voor %s: %s", result.chunk_id, exc)
        return result.text


# ---------------------------------------------------------------------------
# Hoofdfunctie
# ---------------------------------------------------------------------------

def retrieve_and_rerank(
    query: str,
    collections: dict,
    selected_cols: list[str],
    reranker: CrossEncoder | None,
    *,
    bi_top_n: int = 50,
    rerank_threshold: float = 0.60,
    max_results: int = 20,
    expand_context: bool = True,
    n_neighbors: int = 2,
    bron_rollen: list[str] | None = None,
) -> list[RetrievalResult]:
    """
    Volledige retrieval-pipeline (ADR-006):

    1. Bi-encoder: haal bi_top_n kandidaten op per collection
       bron_rollen: optionele where-filter op bron_rol-metadata in `bronnen`-collection
    2. Cross-encoder reranking (optioneel — reranker=None slaat stap over):
       - Rerank alle kandidaten gezamenlijk
       - Filter: alles met rerank_score >= rerank_threshold, cap op max_results
       - Fallback: als 0 resultaten boven drempel → top-5 zonder drempel
    3. Zonder reranker: dedup + top max_results op bi-encoder score
    4. Context-uitbreiding voor wetteksten (±n_neighbors artikelen, begrensd)
    """
    candidates = _retrieve_candidates(collections, query, selected_cols, bi_top_n, bron_rollen)
    if not candidates:
        return []

    if reranker is None:
        # Reranker overgeslagen: sorteer op bi-encoder score, dedup, cap op max_results.
        seen: set[str] = set()
        filtered: list[RetrievalResult] = []
        for r in sorted(candidates, key=lambda x: x.score, reverse=True):
            if r.chunk_id not in seen:
                seen.add(r.chunk_id)
                filtered.append(r)
            if len(filtered) >= max_results:
                break
    else:
        ranked = _rerank(candidates, query, reranker)

        seen = set()
        filtered = []
        for r in ranked:
            if r.chunk_id in seen:
                continue
            seen.add(r.chunk_id)
            if r.rerank_score >= rerank_threshold:
                filtered.append(r)
            if len(filtered) >= max_results:
                break

        # Fallback als niets boven de drempel uitkomt
        if not filtered:
            filtered = [r for r in ranked if r.chunk_id not in (
                set(x.chunk_id for x in filtered)
            )][:5]

    # Context-uitbreiding: wettekst-chunks krijgen omliggende artikelen.
    # ADR-006: wetteksten zitten nu in de unified `bronnen`-collection, herkenbaar via
    # bron_rol-metadata. Legacy `wetteksten`-collection wordt ook ondersteund.
    if expand_context:
        for r in filtered:
            is_wettekst = (
                r.collection == "wetteksten"
                or (r.collection == "bronnen" and r.meta.get("bron_rol") == "wettekst")
            )
            if is_wettekst:
                r.text = _expand_wetteksten_context(r, collections, n_neighbors)

    return filtered


# ---------------------------------------------------------------------------
# Hulpfunctie: meerdere sub-queries samenvoegen (concept-extractie)
# ---------------------------------------------------------------------------

def multi_query_retrieve(
    sub_queries: list[str],
    collections: dict,
    selected_cols: list[str],
    reranker: CrossEncoder,
    *,
    bi_top_n: int = 80,
    rerank_threshold: float = 0.50,
    max_per_query: int = 30,
    expand_context: bool = True,
    bron_rollen: list[str] | None = None,
) -> list[RetrievalResult]:
    """
    Voer meerdere gerichte sub-queries uit en voeg de resultaten samen.
    Deduplicatie op chunk_id over alle sub-queries heen.
    Bedoeld voor concept-extractie (hoge recall).
    """
    seen: set[str] = set()
    all_results: list[RetrievalResult] = []

    for q in sub_queries:
        results = retrieve_and_rerank(
            q, collections, selected_cols, reranker,
            bi_top_n=bi_top_n,
            rerank_threshold=rerank_threshold,
            max_results=max_per_query,
            expand_context=expand_context,
            bron_rollen=bron_rollen,
        )
        for r in results:
            if r.chunk_id not in seen:
                seen.add(r.chunk_id)
                all_results.append(r)

    # Sorteer gecombineerde resultaten op rerank_score
    all_results.sort(key=lambda x: x.rerank_score, reverse=True)
    return all_results
