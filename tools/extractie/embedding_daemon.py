"""
Embedding-daemon voor Certificaid concept-extractie (ADR-018).

Laad bge-m3 en de cross-encoder reranker één keer; bedien meerdere extractie-
agents via HTTP op localhost:8765. Enige schrijver voor de `concepten` ChromaDB-
collection — garandeert read-after-write consistency voor duplicate-checks.

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
from contextlib import asynccontextmanager
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

# Eén lock serialiseert alle model-aanroepen én DB-schrijven zodat:
#   - MPS/CPU geen concurrente kernels krijgt
#   - ChromaDB upserts niet interleaven
#   - read-after-write consistentie gegarandeerd is
_operatie_lock = asyncio.Lock()

@asynccontextmanager
async def _lifespan(app: FastAPI):  # noqa: ARG001
    await _startup()
    yield


app = FastAPI(title="Certificaid Embedding Daemon", version="1.0", lifespan=_lifespan)


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
            bron_short = veld.get("source", {}).get("short", "")
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
# Startup
# ---------------------------------------------------------------------------

async def _startup():
    global _ef, _reranker, _model_device, _started_at
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
    _started_at = datetime.now(timezone.utc).isoformat()
    logger.info("✓ Embedding-daemon klaar (ADR-018)")


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


class RefreshRequest(BaseModel):
    chroma_path: str


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
    return {
        "status": "ok",
        "model": EMBEDDING_MODEL,
        "device": _model_device,
        "started_at": _started_at,
        "last_write": _last_write,
        "collectie_groottes": collectie_groottes,
    }


@app.post("/embed")
async def embed(req: EmbedRequest):
    if not req.texts:
        raise HTTPException(status_code=400, detail="texts mag niet leeg zijn")
    async with _operatie_lock:
        try:
            embeddings = _ef(req.texts)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    return {"embeddings": [list(e) for e in embeddings]}


@app.post("/duplicate-check")
async def duplicate_check(req: DuplicaatCheckRequest):
    chroma_path = req.chroma_path or str(ROOT / "data" / "chroma_db")
    try:
        # Collectie ophalen buiten de lock (metadata-call, geen model)
        collectie = _get_concepten_collectie(chroma_path)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    count = collectie.count()
    if count == 0:
        return {"matches": [], "top1": None, "total_in_collection": 0}

    top_n = min(req.top_n, count)

    async with _operatie_lock:
        try:
            res = collectie.query(
                query_texts=[req.naam],
                n_results=top_n,
                include=["documents", "metadatas", "distances"],
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

        paren = [(req.naam, k["text"]) for k in kandidaten]
        scores = _reranker.predict(paren)
        for k, s in zip(kandidaten, scores):
            k["rerank_score"] = round(float(s), 4)

    boven_drempel = [k for k in kandidaten if k["rerank_score"] >= req.threshold]
    boven_drempel.sort(key=lambda x: x["rerank_score"], reverse=True)

    alle_gesorteerd = sorted(kandidaten, key=lambda x: x["rerank_score"], reverse=True)
    top1 = alle_gesorteerd[0] if alle_gesorteerd else None

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

    async with _operatie_lock:
        try:
            collectie.upsert(
                ids=[concept_id],
                documents=[tekst],
                metadatas=[meta],
            )
            # Forceer persistentie zodat de volgende duplicate-check de write ziet
            _get_chroma_client(chroma_path).heartbeat()
            _last_write = datetime.now(timezone.utc).isoformat()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Upsert mislukt: {exc}")

    logger.info("✓ Concept geïndexeerd: %s", concept_id)
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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="Certificaid embedding-daemon (ADR-018)"
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
