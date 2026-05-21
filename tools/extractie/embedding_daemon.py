"""
Embedding-daemon voor Certificaid concept-extractie (ADR-018).

Laad bge-m3 en de cross-encoder reranker één keer; bedien meerdere extractie-
agents via HTTP op localhost:8765. Enige schrijver voor de `concepten` ChromaDB-
collection — garandeert read-after-write consistency voor duplicate-checks.

Optimalisaties (v2):
  1. Request-batching voor rerank: concurrent /duplicate-check calls binnen
     een korte window worden gebundeld in één PyTorch forward-pass.
     N sequentiële calls (~N × 20s) → één batched call (~25-30s total).
  2. Gating: sla de cross-encoder reranker over als de bi-encoder al sterk is
     (top-1 score >= top1_threshold EN alternatieven >= alt_threshold).
  3. Gescheiden locks: model-inference en DB-writes blokkeren elkaar niet meer.
     Index-writes draaien in een thread-pool zodat embedding-berekening en
     ChromaDB-upserts gelijktijdig kunnen lopen.

Configuratie: tools/extractie/daemon_config.yaml (batch-window, gating-drempels).

Start:
  python tools/extractie/embedding_daemon.py --port 8765

Of via LaunchAgent (automatisch bij login):
  tools/extractie/install_daemon.sh

Zie ADR-018 voor architectuur en concurrency-model.
"""

from __future__ import annotations

import asyncio
import logging
import sys
import concurrent.futures
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))

try:
    import uvicorn
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
except ImportError:
    print(
        "fastapi en uvicorn zijn vereist.\n"
        "Installeer via: pip install fastapi 'uvicorn[standard]'",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from sentence_transformers import CrossEncoder

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

EMBEDDING_MODEL     = "BAAI/bge-m3"
RERANKER_MODEL      = "BAAI/bge-reranker-v2-m3"
COLLECTIE_NAAM      = "concepten"
ALLOWED_DATA_PREFIX = str(ROOT / "data")

CONFIG_PATH = Path(__file__).parent / "daemon_config.yaml"

# ---------------------------------------------------------------------------
# Configuratie laden
# ---------------------------------------------------------------------------

def _laad_config() -> dict:
    """Laad daemon_config.yaml; val terug op veilige defaults als het bestand ontbreekt."""
    defaults: dict = {
        "rerank_batch": {"window_sec": 0.15, "max_size": 8},
        "gating": {
            "enabled": True,
            "top1_threshold": 0.80,
            "alt_threshold": 0.65,
            "margin": 0.05,
            "extra_k": 3,
        },
        "index_write": {"max_workers": 4},
    }
    if yaml is None or not CONFIG_PATH.exists():
        logger.warning("daemon_config.yaml niet gevonden of yaml niet beschikbaar — defaults gebruikt")
        return defaults
    try:
        with CONFIG_PATH.open() as fh:
            loaded = yaml.safe_load(fh) or {}
        # Merge met defaults zodat ontbrekende sleutels worden aangevuld
        for sectie, waarden in defaults.items():
            if sectie not in loaded:
                loaded[sectie] = waarden
            else:
                for k, v in waarden.items():
                    loaded[sectie].setdefault(k, v)
        return loaded
    except Exception as exc:
        logger.error("Fout bij laden daemon_config.yaml: %s — defaults gebruikt", exc)
        return defaults


_config: dict = {}

# ---------------------------------------------------------------------------
# Globale state (geladen bij startup)
# ---------------------------------------------------------------------------

_ef: Optional[SentenceTransformerEmbeddingFunction] = None
_reranker: Optional[CrossEncoder] = None
_model_device: str = "cpu"
_started_at: str = ""
_last_write: Optional[str] = None

# Één ChromaDB-client per chroma_path, lazy-geïnitialiseerd
_chroma_clients: dict[str, chromadb.PersistentClient] = {}

# Gescheiden locks (optimalisatie 3):
#   _model_lock: beschermt MPS/CPU forward-passes (bi-encoder + standalone reranker)
#   _db_write_lock: beschermt ChromaDB-upserts en -deletes
#
# /duplicate-check gebruikt de batch-queue; de lock daar is per-batch intern.
# /embed gebruikt _model_lock direct.
# /index-concept en /delete-concept gebruiken _db_write_lock + thread-pool.
_model_lock   = asyncio.Lock()
_db_write_lock = asyncio.Lock()

# Thread-pool voor CPU/MPS-gebonden werk buiten de event-loop
_thread_pool: Optional[concurrent.futures.ThreadPoolExecutor] = None

# ---------------------------------------------------------------------------
# Request-batching voor rerank (optimalisatie 1)
# ---------------------------------------------------------------------------

@dataclass
class _RerankerItem:
    """Één /duplicate-check request wachtend in de batch-queue."""
    query: str
    kandid: list[dict]                            # [{"text": ..., ...}, ...]
    start_offset: int                             # start-index in de gezamenlijke pairs-lijst
    future: asyncio.Future = field(default_factory=asyncio.get_event_loop)


# Queue voor binnenkomende rerank-verzoeken
_rerank_queue: asyncio.Queue  # geïnitialiseerd in _startup

# Taak die de queue verwerkt
_rerank_worker_task: Optional[asyncio.Task] = None


async def _rerank_worker():
    """
    Achtergrond-coroutine die de rerank-queue leegloopt.

    Wacht tot de batch-window vol is (window_sec) of de batch-grootte bereikt is
    (max_size), voert dan één gezamenlijke cross_encoder.predict() uit en stuurt
    de scores terug naar de wachtende callers.
    """
    window_sec = _config["rerank_batch"]["window_sec"]
    max_size   = _config["rerank_batch"]["max_size"]

    while True:
        # Wacht op het eerste item in de queue
        first: _RerankerItem = await _rerank_queue.get()
        batch = [first]

        # Wacht nog even op meer items (batch-window)
        deadline = asyncio.get_event_loop().time() + window_sec
        while len(batch) < max_size:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                break
            try:
                item = await asyncio.wait_for(_rerank_queue.get(), timeout=remaining)
                batch.append(item)
            except asyncio.TimeoutError:
                break

        # Bouw alle (query, doc) paren samen
        all_pairs: list[tuple[str, str]] = []
        offsets: list[tuple[int, int]] = []  # (start, eind) per batch-item
        for item in batch:
            start = len(all_pairs)
            for k in item.kandid:
                all_pairs.append((item.query, k["text"]))
            offsets.append((start, len(all_pairs)))

        # Voer één batched forward-pass uit in de thread-pool
        loop = asyncio.get_event_loop()
        try:
            scores = await loop.run_in_executor(
                _thread_pool,
                lambda pairs=all_pairs: _reranker.predict(pairs),
            )
            logger.info(
                "Rerank-batch: %d requests, %d paren in één forward-pass",
                len(batch), len(all_pairs),
            )
        except Exception as exc:
            # Fout: stuur exception door naar alle wachtende callers
            for item in batch:
                if not item.future.done():
                    item.future.set_exception(exc)
            continue

        # Verdeel scores terug naar de callers
        for item, (start, eind) in zip(batch, offsets):
            item_scores = [float(s) for s in scores[start:eind]]
            if not item.future.done():
                item.future.set_result(item_scores)


async def _rerank_via_batch(query: str, kandid: list[dict]) -> list[float]:
    """
    Stuur een rerank-verzoek naar de batch-worker en wacht op het resultaat.
    kandid: lijst van dicts met minimaal {"text": str}
    Geeft een lijst van float-scores terug (zelfde volgorde als kandid).
    """
    loop = asyncio.get_event_loop()
    future: asyncio.Future = loop.create_future()
    item = _RerankerItem(
        query=query,
        kandid=kandid,
        start_offset=0,   # wordt in de worker berekend
        future=future,
    )
    await _rerank_queue.put(item)
    return await future


# ---------------------------------------------------------------------------
# Gating-logica (optimalisatie 2)
# ---------------------------------------------------------------------------

def _gating_check(kandidaten: list[dict], gating_cfg: dict) -> tuple[bool, list[dict]]:
    """
    Controleer of rerank overgeslagen kan worden op basis van bi-encoder scores.

    Retourneert (skip_rerank: bool, uitgebreide_kandidaten: list[dict]).
    Als skip_rerank=True zijn de bi_score's al gesorteerd en eventueel uitgebreid
    met extra resultaten (dynamische top_k).
    """
    if not gating_cfg.get("enabled", True):
        return False, kandidaten
    if not kandidaten:
        return False, kandidaten

    gesorteerd = sorted(kandidaten, key=lambda k: k["bi_score"], reverse=True)
    top1_score = gesorteerd[0]["bi_score"]

    if top1_score < gating_cfg["top1_threshold"]:
        return False, kandidaten  # top-1 is niet sterk genoeg

    # Controleer of alternatieven ook boven de drempel liggen
    alternatieven = gesorteerd[1:3]  # top-2 en top-3
    if len(alternatieven) > 0:
        min_alt = min(k["bi_score"] for k in alternatieven)
        if min_alt < gating_cfg["alt_threshold"]:
            return False, kandidaten  # alternatieven te zwak

    # Dynamische uitbreiding: als extra items binnen de margin liggen, voeg ze toe
    margin      = gating_cfg.get("margin", 0.05)
    extra_k     = gating_cfg.get("extra_k", 3)
    drempel_extra = top1_score - margin
    uitgebreid = list(gesorteerd)  # al gesorteerd

    # Voeg reeds meer resultaten toe als ze binnen de margin vallen
    # (de caller zal toch nog filteren op threshold, maar dit geeft meer opties)
    extra_count = 0
    for k in gesorteerd[3:]:
        if k["bi_score"] >= drempel_extra and extra_count < extra_k:
            extra_count += 1
        else:
            break

    return True, uitgebreid


# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------

@asynccontextmanager
async def _lifespan(app: FastAPI):  # noqa: ARG001
    await _startup()
    yield
    # Shutdown: stop de worker-taak
    if _rerank_worker_task and not _rerank_worker_task.done():
        _rerank_worker_task.cancel()
        try:
            await _rerank_worker_task
        except asyncio.CancelledError:
            pass
    if _thread_pool:
        _thread_pool.shutdown(wait=False)


app = FastAPI(title="Certificaid Embedding Daemon", version="2.0", lifespan=_lifespan)


async def _startup():
    global _ef, _reranker, _model_device, _started_at, _config
    global _rerank_queue, _rerank_worker_task, _thread_pool

    _config = _laad_config()
    logger.info("Daemon-config geladen: batch_window=%.2fs, max_size=%d, gating=%s",
                _config["rerank_batch"]["window_sec"],
                _config["rerank_batch"]["max_size"],
                _config["gating"]["enabled"])

    _model_device = _detect_device()
    logger.info("→ bge-m3 laden op device=%s …", _model_device)
    _ef = SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        device=_model_device,
    )
    # Warm-up: zorg dat het model volledig geladen is vóór de eerste request
    _ef(["warm-up"])

    logger.info("→ cross-encoder reranker laden op cpu …")
    _reranker = CrossEncoder(RERANKER_MODEL, device="cpu")
    _reranker.predict([("warm-up query", "warm-up document")])

    # Thread-pool voor blocking model-calls buiten de event-loop
    max_workers = _config["index_write"]["max_workers"]
    _thread_pool = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers,
        thread_name_prefix="daemon-worker",
    )

    # Batch-queue + achtergrond-worker starten
    _rerank_queue = asyncio.Queue()
    _rerank_worker_task = asyncio.create_task(_rerank_worker())

    _started_at = datetime.now(timezone.utc).isoformat()
    logger.info("✓ Embedding-daemon v2 klaar (ADR-018, batching + gating actief)")


# ---------------------------------------------------------------------------
# Helpers: device, model, ChromaDB
# ---------------------------------------------------------------------------

def _detect_device() -> str:
    try:
        import torch
        if torch.backends.mps.is_available():
            return "mps"
    except ImportError:
        pass
    return "cpu"


def _get_chroma_client(chroma_path: str) -> chromadb.PersistentClient:
    """Geef ChromaDB-client terug voor dit pad; maak aan indien nodig."""
    if not chroma_path.startswith(ALLOWED_DATA_PREFIX):
        raise ValueError(
            f"chroma_path moet binnen {ALLOWED_DATA_PREFIX}/ liggen, "
            f"niet: {chroma_path}"
        )
    if chroma_path not in _chroma_clients:
        _chroma_clients[chroma_path] = chromadb.PersistentClient(path=chroma_path)
        logger.info("ChromaDB-client geopend: %s", chroma_path)
    return _chroma_clients[chroma_path]


def _get_concepten_collectie(chroma_path: str):
    client = _get_chroma_client(chroma_path)
    try:
        return client.get_collection(COLLECTIE_NAAM, embedding_function=_ef)
    except Exception:
        return client.get_or_create_collection(COLLECTIE_NAAM, embedding_function=_ef)


def _bouw_embed_tekst(record: dict) -> str:
    """Bouw de tekst die geëmbed wordt voor dit concept (schema 1.1)."""
    delen = []
    naam = record.get("naam", "").strip()
    if naam:
        delen.append(naam)
    node_type = record.get("node_type", "").strip()
    if node_type:
        delen.append(f"({node_type})")
    # Type-specifiek hoofdveld (ADR-007 §type-specifieke sleutelvelden)
    for veldnaam in ("main_rule", "definitie", "verplichting", "doel"):
        veld = record.get(veldnaam)
        if isinstance(veld, dict):
            tekst = veld.get("text", "").strip()
            if tekst:
                delen.append(tekst[:500])
                break
        elif isinstance(veld, str) and veld.strip():
            delen.append(veld.strip()[:500])
            break
    return " — ".join(delen) if delen else naam


def _bouw_metadata(record: dict) -> dict:
    edge_targets = [
        e.get("target", "") for e in record.get("edges", [])
        if e.get("target")
    ]
    bron_short = ""
    for veldnaam in ("main_rule", "definitie", "verplichting", "doel"):
        veld = record.get(veldnaam)
        if isinstance(veld, dict):
            source = veld.get("source", {})
            if isinstance(source, str):
                bron_short = source
            else:
                bron_short = source.get("short", "") if isinstance(source, dict) else ""
            if bron_short:
                break
    return {
        "concept_id":     record.get("id", ""),
        "naam":           record.get("naam", ""),
        "node_type":      record.get("node_type", ""),
        "status":         record.get("status", ""),
        "schema_version": str(record.get("schema_version", "")),
        "edge_targets":   ",".join(edge_targets),
        "bron_short":     bron_short,
    }


# ---------------------------------------------------------------------------
# Pydantic request-modellen
# ---------------------------------------------------------------------------

class EmbedRequest(BaseModel):
    texts: list[str]


class DuplicaatCheckRequest(BaseModel):
    naam: str
    threshold: float = 0.80
    chroma_path: Optional[str] = None
    top_n: int = 10


class IndexConceptRequest(BaseModel):
    record: dict
    chroma_path: Optional[str] = None


class DeleteConceptRequest(BaseModel):
    concept_id: str
    chroma_path: Optional[str] = None


class RefreshRequest(BaseModel):
    chroma_path: str


class ZoekBronnenRequest(BaseModel):
    query: str
    top_k: int = 5
    rerank: bool = False
    bron_rollen: Optional[list[str]] = None


# ---------------------------------------------------------------------------
# Bronnen-RAG helpers (voor /zoek-bronnen endpoint)
# ---------------------------------------------------------------------------

# Pad naar bronnen-RAG (zelfde als MCP-server — data/rag/main)
_BRONNEN_CHROMA_PATH = str(ROOT / "data" / "rag" / "main")

# Lazy-geïnitialiseerde bronnen ChromaDB-client (apart van concepten-client)
_bronnen_client: Optional[chromadb.PersistentClient] = None
_bronnen_ef: Optional[SentenceTransformerEmbeddingFunction] = None


def _get_bronnen_client():
    """Geef ChromaDB-client voor bronnen-RAG. Hergebruikt _ef (zelfde model)."""
    global _bronnen_client, _bronnen_ef
    if _bronnen_client is None:
        if not _BRONNEN_CHROMA_PATH.startswith(ALLOWED_DATA_PREFIX):
            raise ValueError(
                f"bronnen chroma_path moet binnen {ALLOWED_DATA_PREFIX}/ liggen"
            )
        _bronnen_client = chromadb.PersistentClient(path=_BRONNEN_CHROMA_PATH)
        _bronnen_ef = _ef  # zelfde bge-m3 model
        logger.info("Bronnen-ChromaDB-client geopend: %s", _BRONNEN_CHROMA_PATH)
    return _bronnen_client, _bronnen_ef


def _bronnen_bi_query(query: str, top_k: int, bron_rollen: Optional[list[str]]) -> list[dict]:
    """Bi-encoder query op bronnen-collection. Returnt gesorteerde lijst van hit-dicts."""
    client, ef = _get_bronnen_client()
    try:
        col = client.get_collection("bronnen", embedding_function=ef)
    except Exception:
        return []

    count = col.count()
    if count == 0:
        return []

    n_results = min(top_k, count)
    where = None
    if bron_rollen:
        if len(bron_rollen) == 1:
            where = {"bron_rol": {"$eq": bron_rollen[0]}}
        else:
            where = {"bron_rol": {"$in": bron_rollen}}

    res = col.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
        where=where,
    )

    hits = []
    for doc, meta, dist, cid in zip(
        res["documents"][0], res["metadatas"][0],
        res["distances"][0], res["ids"][0],
    ):
        score = round(1 - dist, 4)
        hits.append({
            "chunk_id": cid,
            "bi_score": score,
            "bron": meta.get("bron", ""),
            "artikel": (
                meta.get("artikel_ref")
                or meta.get("sectie")
                or meta.get("veld", "")
            ),
            "text": doc,
            "meta": {k: v for k, v in meta.items() if k in ("bron_rol", "datum", "trust")},
        })

    hits.sort(key=lambda h: h["bi_score"], reverse=True)
    return hits[:top_k]


def _bronnen_rerank(query: str, hits: list[dict], reranker) -> list[dict]:
    """Synchrone cross-encoder rerank van bronnen-hits (bedoeld voor thread-pool)."""
    if not hits:
        return hits
    pairs = [(query, h["text"]) for h in hits]
    scores = reranker.predict(pairs)
    for h, s in zip(hits, scores):
        h["rerank_score"] = round(float(s), 4)
    hits.sort(key=lambda h: h["rerank_score"], reverse=True)
    return hits


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    collectie_groottes: dict[str, int] = {}
    for pad, client in _chroma_clients.items():
        try:
            col = client.get_collection(COLLECTIE_NAAM, embedding_function=_ef)
            collectie_groottes[pad] = col.count()
        except Exception:
            collectie_groottes[pad] = 0
    gating_cfg = _config.get("gating", {})
    return {
        "status": "ok",
        "model": EMBEDDING_MODEL,
        "device": _model_device,
        "started_at": _started_at,
        "last_write": _last_write,
        "collectie_groottes": collectie_groottes,
        "daemon_version": "2.0",
        "optimalisaties": {
            "rerank_batching": {
                "window_sec": _config["rerank_batch"]["window_sec"],
                "max_size": _config["rerank_batch"]["max_size"],
                "queue_grootte": _rerank_queue.qsize() if _rerank_queue else 0,
            },
            "gating": {
                "enabled": gating_cfg.get("enabled", True),
                "top1_threshold": gating_cfg.get("top1_threshold", 0.80),
                "alt_threshold": gating_cfg.get("alt_threshold", 0.65),
            },
        },
    }


@app.post("/embed")
async def embed(req: EmbedRequest):
    if not req.texts:
        raise HTTPException(status_code=400, detail="texts mag niet leeg zijn")
    loop = asyncio.get_event_loop()
    try:
        # Bi-encoder embed in thread-pool zodat andere requests niet geblokkeerd worden
        embeddings = await loop.run_in_executor(
            _thread_pool,
            lambda texts=req.texts: _ef(texts),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"embeddings": [[float(x) for x in e] for e in embeddings]}


@app.post("/duplicate-check")
async def duplicate_check(req: DuplicaatCheckRequest):
    chroma_path = req.chroma_path or str(ROOT / "data" / "chroma_db")
    try:
        collectie = _get_concepten_collectie(chroma_path)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    count = collectie.count()
    if count == 0:
        return {"matches": [], "top1": None, "total_in_collection": 0}

    top_n = min(req.top_n, count)

    # Fase 1: bi-encoder query (wordt via thread-pool uitgevoerd — blokkeert event-loop niet)
    loop = asyncio.get_event_loop()
    try:
        res = await loop.run_in_executor(
            _thread_pool,
            lambda: collectie.query(
                query_texts=[req.naam],
                n_results=top_n,
                include=["documents", "metadatas", "distances"],
            ),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    kandidaten = [
        {
            "concept_id": cid,
            "naam":       meta.get("naam", ""),
            "bi_score":   round(1 - dist, 4),
            "text":       doc,
        }
        for doc, meta, dist, cid in zip(
            res["documents"][0], res["metadatas"][0],
            res["distances"][0], res["ids"][0],
        )
    ]

    if not kandidaten:
        return {"matches": [], "top1": None, "total_in_collection": count}

    # Fase 2: gating — sla rerank over als bi-encoder al beslist genoeg is
    gating_cfg = _config.get("gating", {})
    skip_rerank, kandidaten_gesorteerd = _gating_check(kandidaten, gating_cfg)

    if skip_rerank:
        # Gating: gebruik bi_score als proxy voor rerank_score
        logger.debug("Gating actief voor query '%s' (top-1 bi_score=%.3f)",
                     req.naam, kandidaten_gesorteerd[0]["bi_score"])
        for k in kandidaten_gesorteerd:
            k["rerank_score"] = k["bi_score"]
            k["gating_used"] = True
    else:
        # Fase 2b: rerank via batch-worker (optimalisatie 1)
        try:
            scores = await _rerank_via_batch(req.naam, kandidaten)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Rerank mislukt: {exc}")
        for k, s in zip(kandidaten, scores):
            k["rerank_score"] = round(float(s), 4)
            k["gating_used"] = False
        kandidaten_gesorteerd = sorted(kandidaten, key=lambda x: x["rerank_score"], reverse=True)

    boven_drempel = [k for k in kandidaten_gesorteerd if k["rerank_score"] >= req.threshold]
    top1 = kandidaten_gesorteerd[0] if kandidaten_gesorteerd else None

    return {
        "matches": boven_drempel,
        "top1": top1,
        "total_in_collection": count,
    }


@app.post("/index-concept")
async def index_concept(req: IndexConceptRequest):
    global _last_write
    chroma_path = req.chroma_path or str(ROOT / "data" / "chroma_db")
    try:
        collectie = _get_concepten_collectie(chroma_path)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    record     = req.record
    concept_id = record.get("id") or record.get("naam", "onbekend")
    tekst      = _bouw_embed_tekst(record)
    meta       = _bouw_metadata(record)

    # Embedding berekening + upsert in thread-pool (parallelliseerbaar met andere requests)
    loop = asyncio.get_event_loop()

    def _do_upsert():
        collectie.upsert(
            ids=[concept_id],
            documents=[tekst],
            metadatas=[meta],
        )
        _get_chroma_client(chroma_path).heartbeat()

    async with _db_write_lock:
        try:
            await loop.run_in_executor(_thread_pool, _do_upsert)
            _last_write = datetime.now(timezone.utc).isoformat()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Upsert mislukt: {exc}")

    logger.info("✓ Concept geïndexeerd: %s", concept_id)
    return {"id": concept_id, "ok": True}


@app.post("/delete-concept")
async def delete_concept(req: DeleteConceptRequest):
    global _last_write
    chroma_path = req.chroma_path or str(ROOT / "data" / "chroma_db")
    try:
        collectie = _get_concepten_collectie(chroma_path)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    concept_id = req.concept_id
    loop = asyncio.get_event_loop()

    def _do_delete():
        bestaand = collectie.get(ids=[concept_id], include=[])
        if not bestaand.get("ids"):
            raise KeyError(f"Concept niet gevonden in collectie: {concept_id}")
        collectie.delete(ids=[concept_id])
        _get_chroma_client(chroma_path).heartbeat()

    async with _db_write_lock:
        try:
            await loop.run_in_executor(_thread_pool, _do_delete)
            _last_write = datetime.now(timezone.utc).isoformat()
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Delete mislukt: {exc}")

    logger.info("✓ Concept verwijderd uit RAG: %s", concept_id)
    return {"id": concept_id, "ok": True}


@app.post("/refresh")
async def refresh(req: RefreshRequest):
    chroma_path = req.chroma_path
    if not chroma_path.startswith(ALLOWED_DATA_PREFIX):
        raise HTTPException(
            status_code=400,
            detail=f"chroma_path moet binnen {ALLOWED_DATA_PREFIX}/ liggen",
        )
    if chroma_path in _chroma_clients:
        del _chroma_clients[chroma_path]
        logger.info(
            "ChromaDB-client verwijderd: %s (heropend bij volgende call)", chroma_path
        )
    return {"ok": True, "chroma_path": chroma_path}


@app.post("/zoek-bronnen")
async def zoek_bronnen_endpoint(req: ZoekBronnenRequest):
    """
    Bevraag bronnen-RAG vanuit bundle-script (2-pass architectuur).

    Gebruik:
      - rerank=false (default): bi-encoder alleen, snel (~200ms per query)
      - rerank=true: bi-encoder + cross-encoder, preciezer (~2-5s per query)

    Resultaten worden opgeslagen in de bundle zodat agents ze niet opnieuw
    hoeven op te halen in pass-2.
    """
    loop = asyncio.get_event_loop()

    try:
        # Bi-encoder query (thread-pool — blokkeert event-loop niet)
        hits = await loop.run_in_executor(
            _thread_pool,
            lambda: _bronnen_bi_query(req.query, req.top_k, req.bron_rollen),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Bronnen-query mislukt: {exc}")

    if req.rerank and hits:
        # Rerank via bestaande batching-infrastructuur (cross-encoder forward-pass)
        # Opmerking: voor bundle-builds roept het script telkens slechts één /zoek-bronnen
        # aan — batching geeft hier geen snelheidswinst, maar houdt architectuur consistent.
        try:
            scores = await _rerank_via_batch(req.query, hits)
            for h, s in zip(hits, scores):
                h["rerank_score"] = round(float(s), 4)
            hits.sort(key=lambda h: h["rerank_score"], reverse=True)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Rerank mislukt: {exc}")
    else:
        for h in hits:
            h["rerank_score"] = None

    logger.info(
        "Bronnen-query: '%s' → %d hits (rerank=%s)",
        req.query[:60], len(hits), req.rerank,
    )
    return {
        "query": req.query,
        "top_k": req.top_k,
        "rerank": req.rerank,
        "results": hits,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="Certificaid embedding-daemon v2 (ADR-018, batching + gating)"
    )
    parser.add_argument(
        "--port", type=int, default=8765,
        help="HTTP-poort (default: 8765)",
    )
    parser.add_argument(
        "--host", default="127.0.0.1",
        help="Bind-adres (default: 127.0.0.1 — alleen localhost)",
    )
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
