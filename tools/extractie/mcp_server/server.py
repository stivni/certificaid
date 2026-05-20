"""
MCP-server voor Certificaid extract-pipeline (ADR-025 §EXTRACT v5).

Stelt vijf tools beschikbaar aan extract-subagenten zodat ze on-demand
relevante context kunnen ophalen i.p.v. een vooraf-gebundelde initial-ctx.

Tools:
  - zoek_bronnen(query, top_k, bron_rollen, rerank)
       Bevraag de bronnen-RAG (wetteksten, KB's, CBN-adviezen, normen).
  - zoek_concepten(query, top_k)
       Bevraag de concepten-RAG voor near-duplicate-check of cross-record-buren.
  - lees_record(record_id)
       Lees het JSON-record on-demand vanaf disk (records-API-equivalent voor
       reads, geen writes).
  - lees_anchor_bundle(po_id)
       Geef alle anchors + TDKs voor een programmaonderdeel.
  - check_record_bestaat(record_id)
       Bestaat dit record-id al? Voor near-duplicate-check vóór save_record.

Architectuur:
  - Hits ChromaDB direct via tools/lib/retrieval.py (geen daemon-roundtrip)
  - Reads JSON-records via filesystem
  - Geen schrijfacties via deze server — save_record blijft via records-API
    (subagent gebruikt records-API direct)

Start (stdio-transport, standaard voor Claude Code MCP):
  python3 -m tools.extractie.mcp_server.server

Test (manueel):
  python3 -c "from tools.extractie.mcp_server.server import _zoek_bronnen; \
              print(_zoek_bronnen('matching-beginsel rente', 5))"
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

# Voeg root toe aan sys.path zodat tools.lib imports werken
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

# MCP SDK
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

# Bestaande infrastructure
from tools.lib.retrieval import (  # noqa: E402
    build_retrieval_stack,
    open_collections,
    retrieve_and_rerank,
    _retrieve_candidates,
)

logger = logging.getLogger(__name__)

# Pad-conventies — ADR-019 records-API gebruikt data/rag/main als bron van waarheid
CHROMA_PATH = ROOT / "data" / "rag" / "main"
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
ANCHORS_PATH = ROOT / "data" / "programma" / "anchors.json"
PROGRAMMA_PATH = ROOT / "data" / "programma" / "programma.json"

# Lazy-init retrieval-stack (bge-m3 + reranker laden duurt ~5-15s)
_retrieval_stack: tuple | None = None


def _get_retrieval_stack():
    """Lazy-init bge-m3 + reranker. Eerste call kost 5-15s; daarna gecached."""
    global _retrieval_stack
    if _retrieval_stack is None:
        logger.info("Initialiseer retrieval-stack (eenmalig, ~5-15s)...")
        _retrieval_stack = build_retrieval_stack(chroma_path=CHROMA_PATH)
    return _retrieval_stack


def _formatteer_resultaten(results, max_text_chars: int = 1200) -> str:
    """Formatteer retrieval-resultaten als compact JSON voor agent-consumptie."""
    output = []
    for i, r in enumerate(results, 1):
        score = (
            f"rerank={r.rerank_score:.3f} bi={r.score:.3f}"
            if r.rerank_score >= 0
            else f"bi={r.score:.3f}"
        )
        text = r.text[:max_text_chars]
        if len(r.text) > max_text_chars:
            text += f"... [{len(r.text) - max_text_chars} chars truncated]"
        output.append({
            "rank": i,
            "score": score,
            "bron": r.bron,
            "artikel": r.artikel,
            "chunk_id": r.chunk_id,
            "collection": r.collection,
            "text": text,
            "meta": {k: v for k, v in r.meta.items() if k in ("bron_rol", "datum", "trust")},
        })
    return json.dumps(output, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Tool-implementaties (zonder MCP-decoratoren — gebruikbaar via _-prefix voor tests)
# ---------------------------------------------------------------------------

def _zoek_bronnen(
    query: str,
    top_k: int = 10,
    bron_rollen: list[str] | None = None,
    rerank: bool = False,
) -> str:
    """
    Bevraag bronnen-RAG. bron_rollen filtert op type (bv. ['wettekst', 'cbn']).

    rerank: default False (bi-encoder alleen — snel, lage CPU). Zet True voor
    precisie-kritieke calls (bv. bronvermelding voor een ⚖️-claim die je gaat
    save_record'en). Rerank kost ~50 cross-encoder forward passes per call op CPU.
    """
    client, ef, reranker = _get_retrieval_stack()
    cols = open_collections(client, ef, ["bronnen"])
    if not cols:
        return json.dumps({"error": "bronnen-collection niet beschikbaar"})

    if rerank:
        results = retrieve_and_rerank(
            query, cols, ["bronnen"], reranker,
            bi_top_n=max(top_k * 3, 30),  # was *5 / 50 — verlaagd voor CPU-warmte
            rerank_threshold=0.0,
            max_results=top_k,
            expand_context=False,
            bron_rollen=bron_rollen,
        )
    else:
        results = _retrieve_candidates(
            cols, query, ["bronnen"], bi_top_n=top_k, bron_rollen=bron_rollen
        )
        results.sort(key=lambda x: x.score, reverse=True)
        results = results[:top_k]

    return _formatteer_resultaten(results)


def _zoek_concepten(query: str, top_k: int = 10) -> str:
    """Bevraag concepten-RAG (near-duplicate-check + cross-record-buren)."""
    client, ef, _ = _get_retrieval_stack()
    cols = open_collections(client, ef, ["concepten"])
    if not cols:
        return json.dumps({"error": "concepten-collection niet beschikbaar"})

    results = _retrieve_candidates(
        cols, query, ["concepten"], bi_top_n=top_k, bron_rollen=None
    )
    results.sort(key=lambda x: x.score, reverse=True)
    return _formatteer_resultaten(results[:top_k], max_text_chars=2000)


def _lees_record(record_id: str) -> str:
    """Lees JSON-record on-demand. Geen RAG-roundtrip nodig."""
    pad = RECORDS_DIR / f"{record_id}.json"
    if not pad.exists():
        return json.dumps({"error": f"Record niet gevonden: {record_id}"})
    try:
        data = json.loads(pad.read_text(encoding="utf-8"))
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (OSError, json.JSONDecodeError) as e:
        return json.dumps({"error": f"Fout bij lezen {record_id}: {e}"})


def _lees_anchor_bundle(po_id: str) -> str:
    """Geef alle anchors + TDKs voor een programmaonderdeel (bv. '1.1')."""
    if not ANCHORS_PATH.exists():
        return json.dumps({"error": f"anchors.json niet gevonden: {ANCHORS_PATH}"})
    try:
        data = json.loads(ANCHORS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return json.dumps({"error": f"Fout bij lezen anchors.json: {e}"})

    # Filter op anchors die met po_id beginnen (bv. "1.1.II.V" begint met "1.1")
    matches = {}
    bron = data if isinstance(data, dict) else {"anchors": data}
    anchors = bron.get("anchors", bron)
    if isinstance(anchors, dict):
        for aid, content in anchors.items():
            if str(aid).startswith(po_id):
                matches[aid] = content
    elif isinstance(anchors, list):
        # anchors.json gebruikt 'anchor_id' (formaat: '1.1.taak.1' / '1.1.doelstelling.3' / '1.1.kenniselement.5')
        matches = [
            a for a in anchors
            if str(a.get("anchor_id", a.get("id", ""))).startswith(po_id + ".")
            or str(a.get("anchor_id", a.get("id", ""))) == po_id
        ]
    return json.dumps(matches, indent=2, ensure_ascii=False)


def _check_record_bestaat(record_id: str) -> str:
    """Bestaat dit record-id al? Snel filesystem-check zonder JSON-parse."""
    pad = RECORDS_DIR / f"{record_id}.json"
    return json.dumps({"record_id": record_id, "bestaat": pad.exists()})


# ---------------------------------------------------------------------------
# MCP-server setup
# ---------------------------------------------------------------------------

app = Server("certificaid-rag")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Tool-declaraties die de subagent ziet."""
    return [
        Tool(
            name="zoek_bronnen",
            description=(
                "Bevraag de bronnen-RAG (wetteksten, KB's, CBN-adviezen, normen) "
                "met een natuurlijke-taal-query. Returns top-K chunks met bron, "
                "artikel-nummer en tekst. Standaard rerank-mode voor precisie."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natuurlijke-taal-query, bv. 'matching-beginsel rente prorata'",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Aantal chunks (default 10, max 30)",
                        "default": 10,
                    },
                    "bron_rollen": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "Optioneel filter op bron-type: 'wettekst' · 'kb' · 'cbn' "
                            "· 'norm' · 'advies'. Leeg = alle."
                        ),
                    },
                    "rerank": {
                        "type": "boolean",
                        "description": (
                            "Gebruik cross-encoder rerank (precisie ↑, CPU-kost ↑). "
                            "Default false (bi-encoder alleen — snel). Zet true voor "
                            "precisie-kritieke calls vóór save_record (bv. final "
                            "bronvermelding voor een ⚖️-claim). Kost ~30 forward "
                            "passes per call."
                        ),
                        "default": False,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="zoek_concepten",
            description=(
                "Bevraag de concepten-RAG voor near-duplicate-check of "
                "cross-record-buren. Returns top-K bestaande concept-records "
                "met hun samenvatting. Gebruik vóór save_record om duplicates te vermijden."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Concept-naam of beschrijving, bv. 'inkoop eigen aandelen'",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Aantal hits (default 10)",
                        "default": 10,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="lees_record",
            description=(
                "Lees volledige JSON-inhoud van een concept-record on-demand. "
                "Sneller dan RAG-query voor specifieke records. "
                "Gebruik wanneer je een record-id kent (uit een zoek-resultaat of edge)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "record_id": {
                        "type": "string",
                        "description": "Record-id (slug), bv. 'obligatielening'",
                    },
                },
                "required": ["record_id"],
            },
        ),
        Tool(
            name="lees_anchor_bundle",
            description=(
                "Geef alle anchors + TDKs (taken, doelstellingen, kenniselementen) "
                "voor een programmaonderdeel. Bv. po_id='1.1' levert alle anchors die "
                "met '1.1' beginnen."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "po_id": {
                        "type": "string",
                        "description": "PO-prefix, bv. '1.1' of '2.3'",
                    },
                },
                "required": ["po_id"],
            },
        ),
        Tool(
            name="check_record_bestaat",
            description=(
                "Snelle filesystem-check of een record-id al bestaat. "
                "Gebruik vóór save_record om naam-conflicten te voorkomen of om "
                "te besluiten of een nieuw record nodig is."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "record_id": {"type": "string"},
                },
                "required": ["record_id"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Tool-dispatcher."""
    try:
        if name == "zoek_bronnen":
            result = _zoek_bronnen(
                query=arguments["query"],
                top_k=arguments.get("top_k", 10),
                bron_rollen=arguments.get("bron_rollen"),
                rerank=arguments.get("rerank", False),
            )
        elif name == "zoek_concepten":
            result = _zoek_concepten(
                query=arguments["query"],
                top_k=arguments.get("top_k", 10),
            )
        elif name == "lees_record":
            result = _lees_record(record_id=arguments["record_id"])
        elif name == "lees_anchor_bundle":
            result = _lees_anchor_bundle(po_id=arguments["po_id"])
        elif name == "check_record_bestaat":
            result = _check_record_bestaat(record_id=arguments["record_id"])
        else:
            result = json.dumps({"error": f"Onbekende tool: {name}"})
    except KeyError as e:
        result = json.dumps({"error": f"Missing parameter: {e}"})
    except Exception as e:
        logger.exception("Tool-fout %s", name)
        result = json.dumps({"error": f"Onverwachte fout in {name}: {e}"})

    return [TextContent(type="text", text=result)]


def _preload_retrieval_stack_async() -> None:
    """
    Preload bge-m3 + reranker in achtergrond-thread zodat de eerste tool-call
    niet 10s hoeft te wachten. Blokkeert server-startup NIET — Claude Code kan
    al `list_tools` aanroepen terwijl de modellen laden.
    """
    import threading

    def _worker() -> None:
        try:
            logger.info("Preload bge-m3 + reranker in achtergrond...")
            _get_retrieval_stack()
            logger.info("Preload klaar — eerste zoek_*-call wordt snel.")
        except Exception as e:  # noqa: BLE001
            logger.warning("Preload-fout (niet kritiek; lazy-fallback): %s", e)

    threading.Thread(target=_worker, daemon=True, name="retrieval-preload").start()


async def _main_async() -> None:
    """Start MCP-server op stdio (standaard transport voor Claude Code)."""
    # Trigger preload onmiddellijk — niet blokkerend voor handshake
    _preload_retrieval_stack_async()

    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


def main() -> int:
    import asyncio

    logging.basicConfig(level=logging.WARNING)
    try:
        asyncio.run(_main_async())
        return 0
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
