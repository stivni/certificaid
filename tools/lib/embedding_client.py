"""
HTTP-client voor de Certificaid embedding-daemon (ADR-018).

Biedt twee operaties:
  - duplicate_check(naam, chroma_path, threshold) → dict
  - index_concept(record, chroma_path) → str (concept_id)

Probeert altijd eerst de daemon op localhost:8765. Als de daemon niet bereikbaar
is of een timeout geeft, valt de functie terug op een in-process bge-m3-load.
Scripts en agents kunnen beide functies aanroepen zonder te weten of de daemon
draait — degradatie is transparant.

Gebruik:
  from lib.embedding_client import duplicate_check, index_concept

  resultaat = duplicate_check(
      "Beroepsgeheim van de gecertificeerd accountant",
      chroma_path="data/chroma_db",
  )
  # resultaat = {"matches": [...], "top1": {...}, "total_in_collection": N}

  concept_id = index_concept(record, chroma_path="data/chroma_db")
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Optional

import requests

logger = logging.getLogger(__name__)

DAEMON_URL = "http://127.0.0.1:8765"
HEALTH_TIMEOUT  = 2    # seconden — snelle liveness-check
REQUEST_TIMEOUT = 60   # seconden — embedding + upsert mag even duren

ROOT = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# Daemon-liveness
# ---------------------------------------------------------------------------

def is_daemon_alive() -> bool:
    """Controleer snel of de daemon bereikbaar is."""
    try:
        r = requests.get(f"{DAEMON_URL}/health", timeout=HEALTH_TIMEOUT)
        return r.status_code == 200
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Daemon-calls
# ---------------------------------------------------------------------------

def _post(endpoint: str, payload: dict) -> Optional[dict]:
    """
    POST naar daemon-endpoint. Geeft None bij elke fout (connectie, timeout,
    HTTP-error) zodat de caller kan terugvallen op in-process.
    """
    try:
        r = requests.post(
            f"{DAEMON_URL}/{endpoint}",
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        logger.debug("Daemon niet bereikbaar op %s", DAEMON_URL)
        return None
    except requests.exceptions.Timeout:
        logger.warning("Daemon timeout voor /%s (>%ds)", endpoint, REQUEST_TIMEOUT)
        return None
    except Exception as exc:
        logger.warning("Daemon-fout bij /%s: %s", endpoint, exc)
        return None


# ---------------------------------------------------------------------------
# In-process fallback (laadt bge-m3 lokaal als daemon down is)
# ---------------------------------------------------------------------------

def _local_duplicate_check(
    naam: str,
    chroma_path: str,
    threshold: float,
    top_n: int,
) -> dict:
    """Fallback: duplicate-check zonder daemon (traag — laadt bge-m3 in process)."""
    from lib.retrieval import build_retrieval_stack
    from sentence_transformers import CrossEncoder

    logger.warning(
        "Daemon niet beschikbaar — in-process duplicate-check (cold-start ~15s)"
    )
    chroma_pad = Path(chroma_path) if not Path(chroma_path).is_absolute() \
        else Path(chroma_path)
    client, ef, reranker = build_retrieval_stack(chroma_pad)

    try:
        collectie = client.get_collection("concepten", embedding_function=ef)
    except Exception:
        collectie = client.get_or_create_collection("concepten", embedding_function=ef)

    count = collectie.count()
    if count == 0:
        return {"matches": [], "top1": None, "total_in_collection": 0}

    n = min(top_n, count)
    res = collectie.query(
        query_texts=[naam],
        n_results=n,
        include=["documents", "metadatas", "distances"],
    )
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

    scores = reranker.predict([(naam, k["text"]) for k in kandidaten])
    for k, s in zip(kandidaten, scores):
        k["rerank_score"] = round(float(s), 4)

    boven = [k for k in kandidaten if k["rerank_score"] >= threshold]
    boven.sort(key=lambda x: x["rerank_score"], reverse=True)
    alle = sorted(kandidaten, key=lambda x: x["rerank_score"], reverse=True)

    return {
        "matches": boven,
        "top1": alle[0] if alle else None,
        "total_in_collection": count,
    }


def _local_index_concept(record: dict, chroma_path: str) -> str:
    """Fallback: concept indexeren zonder daemon (laadt bge-m3 in process)."""
    from lib.retrieval import build_retrieval_stack

    logger.warning(
        "Daemon niet beschikbaar — in-process indexering (cold-start ~15s)"
    )
    chroma_pad = Path(chroma_path) if Path(chroma_path).is_absolute() \
        else ROOT / chroma_path
    client, ef, _ = build_retrieval_stack(chroma_pad)

    try:
        collectie = client.get_collection("concepten", embedding_function=ef)
    except Exception:
        collectie = client.get_or_create_collection("concepten", embedding_function=ef)

    concept_id = record.get("id") or record.get("naam", "onbekend")
    tekst = _bouw_embed_tekst_local(record)
    meta  = _bouw_metadata_local(record)

    collectie.upsert(ids=[concept_id], documents=[tekst], metadatas=[meta])
    return concept_id


def _bouw_embed_tekst_local(record: dict) -> str:
    delen = []
    naam = record.get("naam", "").strip()
    if naam:
        delen.append(naam)
    node_type = record.get("node_type", "").strip()
    if node_type:
        delen.append(f"({node_type})")
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


def _bouw_metadata_local(record: dict) -> dict:
    edge_targets = [
        e.get("target", "") for e in record.get("edges", []) if e.get("target")
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
# Publieke API
# ---------------------------------------------------------------------------

def duplicate_check(
    naam: str,
    chroma_path: str | None = None,
    threshold: float = 0.80,
    top_n: int = 10,
) -> dict:
    """
    Controleer of een conceptnaam al bestaat in de `concepten`-collection.

    Probeert de daemon; valt terug op in-process bij daemon-downtime.

    Returns:
        {
          "matches": [{"concept_id", "naam", "bi_score", "rerank_score", "text"}],
          "top1": <top-kandidaat ongeacht drempel, of None>,
          "total_in_collection": int,
        }
    """
    resolved_path = chroma_path or str(ROOT / "data" / "chroma_db")
    # Zet relatief pad om naar absoluut
    if not Path(resolved_path).is_absolute():
        resolved_path = str(ROOT / resolved_path)

    resultaat = _post("duplicate-check", {
        "naam": naam,
        "threshold": threshold,
        "chroma_path": resolved_path,
        "top_n": top_n,
    })
    if resultaat is not None:
        return resultaat

    return _local_duplicate_check(naam, resolved_path, threshold, top_n)


def index_concept(
    record: dict,
    chroma_path: str | None = None,
) -> str:
    """
    Embed één concept-record en upsert in de `concepten`-collection.

    Probeert de daemon; valt terug op in-process bij daemon-downtime.

    Returns:
        concept_id (str)
    """
    resolved_path = chroma_path or str(ROOT / "data" / "chroma_db")
    if not Path(resolved_path).is_absolute():
        resolved_path = str(ROOT / resolved_path)

    resultaat = _post("index-concept", {
        "record": record,
        "chroma_path": resolved_path,
    })
    if resultaat is not None:
        return resultaat.get("id", record.get("id", "onbekend"))

    return _local_index_concept(record, resolved_path)
