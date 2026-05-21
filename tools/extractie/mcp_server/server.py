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

Architectuur (ADR-027 §vervolg):
  - zoek_bronnen(rerank=False): volledig in-process via ChromaDB + bge-m3
    bi-encoder. Geen HTTP-roundtrip, geen daemon-overhead, geen queue-wachttijd.
    Dit is het standaard-pad voor de meerderheid van agent-calls.
  - zoek_bronnen(rerank=True): in-process met cross-encoder (reranker). De
    reranker wordt pas geladen bij de eerste rerank=True call (lazy, apart gecached
    van de bi-encoder stack). Bij reranker-laadfouten: graceful fallback naar
    bi-encoder-only resultaten.
  - zoek_concepten: in-process via dezelfde bi-encoder stack.
  - Geen daemon-roundtrips voor read-only bronnen-queries.
  - Reads JSON-records via filesystem (geen RAG nodig voor specifieke records).
  - Geen schrijfacties via deze server — save_record blijft via records-API.

Twee aparte caches voor minimale geheugendruk bij 6-parallel-agent-scenario:
  _bi_stack:     (client, ef) — altijd geladen; bge-m3 bi-encoder
  _reranker_obj: CrossEncoder — alleen geladen bij rerank=True calls

Start (stdio-transport, standaard voor Claude Code MCP):
  python3 -m tools.extractie.mcp_server.server

Test (manueel):
  python3 -c "from tools.extractie.mcp_server.server import _zoek_bronnen; \
              print(_zoek_bronnen('matching-beginsel rente', 5))"

Activering: MCP-server-code-wijzigingen vereisen een nieuwe Claude Code-sessie
om te activeren (per .mcp.json config — Claude Code herstart de server dan).
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
    open_collections,
    retrieve_and_rerank,
    _retrieve_candidates,
)
from tools.extractie import candidates_db  # noqa: E402

logger = logging.getLogger(__name__)

# Pad-conventies — ADR-019 records-API gebruikt data/rag/main als bron van waarheid
CHROMA_PATH = ROOT / "data" / "rag" / "main"
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
ANCHORS_PATH = ROOT / "data" / "programma" / "anchors.json"
PROGRAMMA_PATH = ROOT / "data" / "programma" / "programma.json"

# ---------------------------------------------------------------------------
# Twee aparte lazy-init caches voor minimale geheugendruk (ADR-027 §vervolg).
#
# _bi_stack: (client, ef, reranker=None) — bge-m3 bi-encoder + ChromaDB.
#   Altijd geladen bij eerste zoek_*-call. Geen CrossEncoder hier.
#   reranker=None wordt doorgegeven aan retrieve_and_rerank → bi-encoder-only.
#
# _reranker_obj: CrossEncoder — alleen geladen bij zoek_bronnen(rerank=True).
#   Laad ~3-5s extra, ~300MB RAM. Bij 6 parallelle agents met rerank=False:
#   reranker wordt in geen van de processen geladen → significant minder druk.
# ---------------------------------------------------------------------------
_bi_stack: tuple | None = None        # (client, ef, reranker=None)
_reranker_obj = None                  # CrossEncoder | None


def _get_bi_stack() -> tuple:
    """Lazy-init bge-m3 bi-encoder + ChromaDB-client. Reranker NIET geladen.

    Laadt alleen SentenceTransformerEmbeddingFunction (bi-encoder) + chromadb-client.
    Geen CrossEncoder — dat is de kern van de optimalisatie voor parallelle agents.
    Eerste call kost ~5-10s. Daarna gecached als module-level singleton.
    """
    global _bi_stack
    if _bi_stack is None:
        logger.info("Initialiseer bi-encoder stack (eenmalig, ~5-10s)...")
        import chromadb
        from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
        from tools.lib.retrieval import EMBEDDING_MODEL
        ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL, device="cpu")
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        _bi_stack = (client, ef, None)
    return _bi_stack


def _get_reranker():
    """Lazy-init cross-encoder reranker. Alleen geladen bij rerank=True calls.

    Eerste call kost ~3-5s extra. Daarna gecached als module-level singleton.
    Retourneert None als laden mislukt (graceful fallback naar bi-encoder).
    """
    global _reranker_obj
    if _reranker_obj is None:
        from sentence_transformers import CrossEncoder
        from tools.lib.retrieval import RERANKER_MODEL
        try:
            logger.info("Initialiseer cross-encoder reranker (eenmalig, ~3-5s)...")
            _reranker_obj = CrossEncoder(RERANKER_MODEL, device="cpu")
        except Exception as e:
            logger.warning("Reranker laden mislukt (%s) — bi-encoder fallback.", e)
            return None
    return _reranker_obj


def _get_retrieval_stack() -> tuple:
    """Legacy-wrapper: retourneert (client, ef, None).

    Alleen gebruikt door _embed_text (zoek_kandidaten, voorstel_kandidaat).
    Die code heeft alleen de embedding-functie nodig, geen reranker.
    Retourneert (client, ef, None) — reranker wordt NIET geladen.
    """
    client, ef, _ = _get_bi_stack()
    return client, ef, None


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
    Bevraag bronnen-RAG volledig in-process (geen daemon-roundtrip).

    rerank=False (standaard): bi-encoder alleen — snel, lage CPU, reranker
    wordt NIET geladen. Optimaal voor 6-parallel-agent-scenario's.

    rerank=True: cross-encoder rerank in-process. Reranker wordt lazy geladen
    bij eerste rerank=True call (~3-5s extra, daarna gecached). Bij laadfouten:
    graceful fallback naar bi-encoder resultaten.

    Beide paden zijn volledig in-process — geen HTTP-roundtrip naar daemon.
    """
    client, ef, _ = _get_bi_stack()   # reranker NIET geladen hier
    cols = open_collections(client, ef, ["bronnen"])
    if not cols:
        return json.dumps({"error": "bronnen-collection niet beschikbaar"})

    if rerank:
        reranker = _get_reranker()    # lazy-laden, None bij laadfouten
        if reranker is not None:
            results = retrieve_and_rerank(
                query, cols, ["bronnen"], reranker,
                bi_top_n=max(top_k * 3, 30),
                rerank_threshold=0.0,
                max_results=top_k,
                expand_context=False,
                bron_rollen=bron_rollen,
            )
        else:
            # Reranker laden mislukt — graceful fallback naar bi-encoder
            logger.warning("Reranker niet beschikbaar; fallback naar bi-encoder voor rerank=True call.")
            results = _retrieve_candidates(
                cols, query, ["bronnen"], bi_top_n=top_k, bron_rollen=bron_rollen
            )
            results.sort(key=lambda x: x.score, reverse=True)
            results = results[:top_k]
    else:
        results = _retrieve_candidates(
            cols, query, ["bronnen"], bi_top_n=top_k, bron_rollen=bron_rollen
        )
        results.sort(key=lambda x: x.score, reverse=True)
        results = results[:top_k]

    return _formatteer_resultaten(results)


def _zoek_concepten(query: str, top_k: int = 10) -> str:
    """Bevraag concepten-RAG (near-duplicate-check + cross-record-buren).

    In-process via bi-encoder stack (geen daemon-roundtrip). Reranker niet nodig.
    """
    client, ef, _ = _get_bi_stack()
    cols = open_collections(client, ef, ["concepten"])
    if not cols:
        return json.dumps({"error": "concepten-collection niet beschikbaar"})

    results = _retrieve_candidates(
        cols, query, ["concepten"], bi_top_n=top_k, bron_rollen=None
    )
    results.sort(key=lambda x: x.score, reverse=True)
    return _formatteer_resultaten(results[:top_k], max_text_chars=2000)


def _zoek_vragen(
    query: str,
    top_k: int = 5,
    programmaonderdeel_id: str | None = None,
    vraag_herkomst: str | None = None,
) -> str:
    """
    Bevraag de vragen-RAG (examenvraag-interpretaties, schema v1.2).

    Optionele filters:
      - programmaonderdeel_id: bv. "1.7" — filtert op programmaonderdeel_ids-metadata
        (comma-separated string; match als de opgegeven id erin voorkomt via $contains)
      - vraag_herkomst: "officieel" | "herinnering" | "hybride"

    Returns: compacte lijst van vraag-metadata + similarity-score (geen chunk-tekst).
    """
    client, ef, _ = _get_bi_stack()
    cols = open_collections(client, ef, ["vragen"])
    if not cols:
        return json.dumps({"error": "vragen-collection niet beschikbaar — run eerst: python3 -m tools.rag.rag_index --add-vragen"})

    # Bouw where-filter op basis van optionele parameters
    where_filters: list[dict] = []
    if programmaonderdeel_id:
        # programmaonderdeel_ids is comma-separated string, bv. "1.6,3.0"
        # ChromaDB $contains zoekt substring — werkt voor "1.7" in "1.7" en "1.6,1.7"
        where_filters.append({"programmaonderdeel_ids": {"$contains": programmaonderdeel_id}})
    if vraag_herkomst:
        where_filters.append({"vraag_herkomst": {"$eq": vraag_herkomst}})

    where = None
    if len(where_filters) == 1:
        where = where_filters[0]
    elif len(where_filters) > 1:
        where = {"$and": where_filters}

    col = cols["vragen"]
    count = col.count()
    if count == 0:
        return json.dumps({"error": "vragen-collection is leeg"})

    res = col.query(
        query_texts=[query],
        n_results=min(top_k, count),
        include=["metadatas", "distances"],
        where=where,
    )

    output = []
    for meta, dist, cid in zip(
        res["metadatas"][0],
        res["distances"][0],
        res["ids"][0],
    ):
        score = round(1 - dist, 4)
        output.append({
            "vraag_id":               meta.get("vraag_id", cid),
            "examen_id":              meta.get("examen_id", ""),
            "vraag_herkomst":         meta.get("vraag_herkomst", ""),
            "programmaonderdeel_ids": meta.get("programmaonderdeel_ids", ""),
            "vraagtypes":             meta.get("vraagtypes", ""),
            "themas":                 meta.get("themas", ""),
            "similarity_score":       score,
        })
    return json.dumps(output, indent=2, ensure_ascii=False)


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


_ANCHOR_BUNDLE_VELDEN = {
    "anchor_id",
    "po",
    "po_titel",
    "tekst",
    "verbose",
    "synoniemen",
    "references",
}
"""Velden die naar de agent gaan. Embedding-vectoren (`vector`, `embedding_text`,
`embedding_text_sha`, `vector_sha`) zijn intern voor de daemon — ze blazen de
output op tot ~700k chars per PO en zijn voor de agent waardeloos."""


def _slim_anchor(anchor: dict) -> dict:
    """Strip embedding-velden uit een anchor voor agent-output."""
    return {k: v for k, v in anchor.items() if k in _ANCHOR_BUNDLE_VELDEN}


def _lees_anchor_bundle(po_id: str) -> str:
    """
    Geef alle anchors + TDKs voor een programmaonderdeel (bv. '1.1').

    Geeft alleen agent-bruikbare velden terug (anchor_id, po, po_titel, tekst,
    verbose, synoniemen, references). Embedding-vectoren worden niet meegestuurd
    — die zijn intern voor de embedding-daemon en zouden de response opblazen.
    """
    if not ANCHORS_PATH.exists():
        return json.dumps({"error": f"anchors.json niet gevonden: {ANCHORS_PATH}"})
    try:
        data = json.loads(ANCHORS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return json.dumps({"error": f"Fout bij lezen anchors.json: {e}"})

    bron = data if isinstance(data, dict) else {"anchors": data}
    anchors = bron.get("anchors", bron)

    if isinstance(anchors, dict):
        matches: list | dict = {
            aid: _slim_anchor(content) if isinstance(content, dict) else content
            for aid, content in anchors.items()
            if str(aid).startswith(po_id)
        }
    elif isinstance(anchors, list):
        # anchors.json gebruikt 'anchor_id' (formaat: '1.1.taak.1' / '1.1.doelstelling.3' / '1.1.kenniselement.5')
        matches = [
            _slim_anchor(a) for a in anchors
            if str(a.get("anchor_id", a.get("id", ""))).startswith(po_id + ".")
            or str(a.get("anchor_id", a.get("id", ""))) == po_id
        ]
    else:
        matches = []

    return json.dumps(matches, indent=2, ensure_ascii=False)


def _check_record_bestaat(record_id: str) -> str:
    """Bestaat dit record-id al? Snel filesystem-check zonder JSON-parse."""
    pad = RECORDS_DIR / f"{record_id}.json"
    return json.dumps({"record_id": record_id, "bestaat": pad.exists()})


# ---------------------------------------------------------------------------
# Skeleton-candidates DB tool-implementaties (ADR-025 §wave-planning)
# ---------------------------------------------------------------------------

def _embed_text(text: str) -> list[float]:
    """Genereer bge-m3-embedding voor een string via de bi-encoder stack."""
    _, ef, _ = _get_bi_stack()
    emb = ef([text])[0]
    if hasattr(emb, "tolist"):
        return emb.tolist()
    return list(emb)


def _zoek_kandidaten(query: str, top_k: int = 10, min_similarity: float = 0.0) -> str:
    """Embedding-similarity-search over de candidates-DB."""
    emb = _embed_text(query)
    hits = candidates_db.zoek_kandidaten(emb, top_k=top_k, min_similarity=min_similarity)
    # Compacte representatie — geen volledige aanvullings_log etc.
    compact = []
    for h in hits:
        compact.append({
            "fiche_id": h["fiche_id"],
            "kind": h["kind"],
            "primary_po": h["primary_po"],
            "similarity_score": round(h["similarity_score"], 4),
            "motivatie": h["motivatie"][:300],
            "voorgesteld_door_pos": h["voorgesteld_door_pos"],
            "cross_po": h["cross_po"],
            "dekt_tdks": h["dekt_tdks"],
        })
    return json.dumps(compact, indent=2, ensure_ascii=False)


def _lees_kandidaat(fiche_id: str) -> str:
    """Volledige kandidaat-record."""
    result = candidates_db.lees_kandidaat(fiche_id)
    if result is None:
        return json.dumps({"error": f"Kandidaat niet gevonden: {fiche_id}"})
    return json.dumps(result, indent=2, ensure_ascii=False)


def _voorstel_kandidaat(
    fiche_id: str,
    kind: str,
    primary_po: str,
    voorgesteld_door_po: str,
    motivatie: str = "",
    linked_anchors: list[str] | None = None,
    dekt_tdks: list[str] | None = None,
    cross_po: bool = False,
    verwachte_onderdelen: list[str] | None = None,
    edges_voorgesteld: dict | None = None,
    depends_on_fiches: list[str] | None = None,
    v1_hints: list[str] | None = None,
    rol_perspectieven: list[str] | None = None,
    rationale: str = "",
    skip_embedding: bool = False,
) -> str:
    """Insert-or-merge een kandidaat. Embedding wordt automatisch berekend uit fiche_id + motivatie."""
    embedding = None
    if not skip_embedding:
        text = f"{fiche_id}. {motivatie}".strip(". ")
        if text:
            embedding = _embed_text(text)
    result = candidates_db.voorstel_kandidaat(
        fiche_id=fiche_id,
        kind=kind,
        primary_po=primary_po,
        voorgesteld_door_po=voorgesteld_door_po,
        linked_anchors=linked_anchors,
        dekt_tdks=dekt_tdks,
        cross_po=cross_po,
        motivatie=motivatie,
        verwachte_onderdelen=verwachte_onderdelen,
        edges_voorgesteld=edges_voorgesteld,
        depends_on_fiches=depends_on_fiches,
        v1_hints=v1_hints,
        rol_perspectieven=rol_perspectieven,
        embedding=embedding,
        rationale=rationale,
    )
    return json.dumps(result, indent=2, ensure_ascii=False)


def _aanvul_kandidaat(fiche_id: str, po_id: str, veld: str, waarde, rationale: str = "") -> str:
    """Partiële update van bestaande kandidaat (anchor, tdk, edge, dependency, hint, rol, verwacht_onderdeel)."""
    result = candidates_db.aanvul_kandidaat(
        fiche_id=fiche_id, po_id=po_id, veld=veld, waarde=waarde, rationale=rationale
    )
    return json.dumps(result, indent=2, ensure_ascii=False)


def _lijst_kandidaten(
    po_id: str | None = None,
    kind: str | None = None,
    cross_po_only: bool = False,
    gerealiseerd: bool | None = None,
) -> str:
    """Filter-view over de candidates-DB."""
    cands = candidates_db.lijst_kandidaten(
        po_id=po_id, kind=kind, cross_po_only=cross_po_only, gerealiseerd=gerealiseerd
    )
    # Compacte representatie
    compact = []
    for c in cands:
        compact.append({
            "fiche_id": c["fiche_id"],
            "kind": c["kind"],
            "primary_po": c["primary_po"],
            "voorgesteld_door_pos": c["voorgesteld_door_pos"],
            "cross_po": c["cross_po"],
            "dekt_tdks": c["dekt_tdks"],
            "gerealiseerd": c.get("gerealiseerd"),
            "gerealiseerd_als_record_id": c.get("gerealiseerd_als_record_id"),
        })
    return json.dumps({
        "totaal": len(compact),
        "kandidaten": compact,
        "filter": {"po_id": po_id, "kind": kind, "cross_po_only": cross_po_only, "gerealiseerd": gerealiseerd},
    }, indent=2, ensure_ascii=False)


def _markeer_kandidaat_gerealiseerd(
    fiche_id: str,
    record_id: str | None = None,
    extract_wave_id: str | None = None,
) -> str:
    """Markeer een kandidaat als gerealiseerd (record geschreven)."""
    result = candidates_db.markeer_gerealiseerd(
        fiche_id=fiche_id, record_id=record_id, extract_wave_id=extract_wave_id
    )
    return json.dumps(result, indent=2, ensure_ascii=False)


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
            name="zoek_vragen",
            description=(
                "Bevraag de examenvragen-RAG (schema v1.2-interpretaties). "
                "Returns top-K vragen met vraag_id, examen_id, PO-ids, themas en "
                "similarity-score (geen chunk-tekst — compact voor agent-gebruik). "
                "Optioneel filteren op programmaonderdeel_id (bv. '1.7') of "
                "vraag_herkomst ('officieel'/'herinnering'/'hybride')."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Semantische query, bv. 'fraude door boekhouder interne controle'",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Aantal resultaten (default 5, max 20)",
                        "default": 5,
                    },
                    "programmaonderdeel_id": {
                        "type": "string",
                        "description": "Optioneel filter op PO, bv. '1.7' of '2.4'",
                    },
                    "vraag_herkomst": {
                        "type": "string",
                        "description": "Optioneel filter: 'officieel' | 'herinnering' | 'hybride'",
                        "enum": ["officieel", "herinnering", "hybride"],
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
        # ---- Skeleton-candidates DB (ADR-025 §wave-planning) ----
        Tool(
            name="zoek_kandidaten",
            description=(
                "Embedding-similarity-search over de gedeelde skeleton-candidates-DB. "
                "Gebruik VOORDAT je voorstel_kandidaat aanroept om te zien of een "
                "vergelijkbare fiche al door een andere PO-skeleton-pass is voorgesteld. "
                "Bij score > 0.85: overweeg aanvul_kandidaat i.p.v. nieuw voorstel."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Naam + korte motivatie van de kandidaat, bv. 'obligatielening lange-termijn schuldfinanciering'",
                    },
                    "top_k": {"type": "integer", "default": 10},
                    "min_similarity": {"type": "number", "default": 0.0},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="lees_kandidaat",
            description="Lees volledige kandidaat-record (inclusief aanvullings_log en rationale_per_po).",
            inputSchema={
                "type": "object",
                "properties": {"fiche_id": {"type": "string"}},
                "required": ["fiche_id"],
            },
        ),
        Tool(
            name="voorstel_kandidaat",
            description=(
                "Insert-or-merge een 2.0-fiche-kandidaat in de gedeelde DB. "
                "Bij bestaand fiche_id wordt gemerged (anchors/tdks/edges/hints union; "
                "voorgesteld_door_pos append; cross_po=true bij 2+ PO's). "
                "Embedding wordt automatisch berekend uit fiche_id + motivatie via bge-m3."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "fiche_id": {"type": "string", "description": "Slug, bv. 'obligatielening'"},
                    "kind": {"type": "string", "description": "instrument · operatie · procedure · regime · ratio · kader · familie · begripscluster · balanspost"},
                    "primary_po": {"type": "string", "description": "PO waar dit fiche primair thuishoort, bv. '1.1'"},
                    "voorgesteld_door_po": {"type": "string", "description": "PO van de huidige skeleton-pass"},
                    "motivatie": {"type": "string"},
                    "linked_anchors": {"type": "array", "items": {"type": "string"}},
                    "dekt_tdks": {"type": "array", "items": {"type": "string"}},
                    "cross_po": {"type": "boolean", "default": False},
                    "verwachte_onderdelen": {"type": "array", "items": {"type": "string"}},
                    "edges_voorgesteld": {"type": "object", "description": "{'lid_van': [...], 'beïnvloed_door': [...]}"},
                    "depends_on_fiches": {"type": "array", "items": {"type": "string"}},
                    "v1_hints": {"type": "array", "items": {"type": "string"}, "description": "v1.x-record-ids als content-inspiratie voor extract-agents"},
                    "rol_perspectieven": {"type": "array", "items": {"type": "string"}},
                    "rationale": {"type": "string", "description": "Waarom dit fiche vanuit deze PO wordt voorgesteld"},
                },
                "required": ["fiche_id", "kind", "primary_po", "voorgesteld_door_po", "motivatie"],
            },
        ),
        Tool(
            name="aanvul_kandidaat",
            description=(
                "Partiële update van een bestaande kandidaat. Append-only logging. "
                "Veld kan zijn: 'anchor' · 'tdk' · 'dependency' · 'hint' · 'rol' · 'verwacht_onderdeel' (waarde = string) "
                "of 'edge' (waarde = {'edge_type': 'doel_fiche_id'})."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "fiche_id": {"type": "string"},
                    "po_id": {"type": "string"},
                    "veld": {"type": "string", "enum": ["anchor", "tdk", "edge", "dependency", "hint", "rol", "verwacht_onderdeel"]},
                    "waarde": {"description": "string of object afhankelijk van veld"},
                    "rationale": {"type": "string"},
                },
                "required": ["fiche_id", "po_id", "veld", "waarde"],
            },
        ),
        Tool(
            name="lijst_kandidaten",
            description=(
                "Filter-view over de candidates-DB (compacte representatie zonder logs). "
                "Gebruik gerealiseerd=False bij re-runs om alleen openstaande kandidaten te zien."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "po_id": {"type": "string"},
                    "kind": {"type": "string"},
                    "cross_po_only": {"type": "boolean", "default": False},
                    "gerealiseerd": {
                        "type": "boolean",
                        "description": "true = alleen gerealiseerd; false = alleen openstaand; weglaten = alles",
                    },
                },
            },
        ),
        Tool(
            name="markeer_kandidaat_gerealiseerd",
            description=(
                "Markeer een kandidaat als gerealiseerd (record geschreven). "
                "Wordt typisch automatisch gedaan door records-API save_record hook; "
                "deze tool is voor expliciete markering door extract-agents of voor "
                "het tagging van een wave-id (extract_wave_id parameter)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "fiche_id": {"type": "string"},
                    "record_id": {"type": "string", "description": "Default = fiche_id"},
                    "extract_wave_id": {"type": "string", "description": "bv. 'wave-0a-2026-05-21'"},
                },
                "required": ["fiche_id"],
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
        elif name == "zoek_vragen":
            result = _zoek_vragen(
                query=arguments["query"],
                top_k=arguments.get("top_k", 5),
                programmaonderdeel_id=arguments.get("programmaonderdeel_id"),
                vraag_herkomst=arguments.get("vraag_herkomst"),
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
        elif name == "zoek_kandidaten":
            result = _zoek_kandidaten(
                query=arguments["query"],
                top_k=arguments.get("top_k", 10),
                min_similarity=arguments.get("min_similarity", 0.0),
            )
        elif name == "lees_kandidaat":
            result = _lees_kandidaat(fiche_id=arguments["fiche_id"])
        elif name == "voorstel_kandidaat":
            result = _voorstel_kandidaat(
                fiche_id=arguments["fiche_id"],
                kind=arguments["kind"],
                primary_po=arguments["primary_po"],
                voorgesteld_door_po=arguments["voorgesteld_door_po"],
                motivatie=arguments.get("motivatie", ""),
                linked_anchors=arguments.get("linked_anchors"),
                dekt_tdks=arguments.get("dekt_tdks"),
                cross_po=arguments.get("cross_po", False),
                verwachte_onderdelen=arguments.get("verwachte_onderdelen"),
                edges_voorgesteld=arguments.get("edges_voorgesteld"),
                depends_on_fiches=arguments.get("depends_on_fiches"),
                v1_hints=arguments.get("v1_hints"),
                rol_perspectieven=arguments.get("rol_perspectieven"),
                rationale=arguments.get("rationale", ""),
            )
        elif name == "aanvul_kandidaat":
            result = _aanvul_kandidaat(
                fiche_id=arguments["fiche_id"],
                po_id=arguments["po_id"],
                veld=arguments["veld"],
                waarde=arguments["waarde"],
                rationale=arguments.get("rationale", ""),
            )
        elif name == "lijst_kandidaten":
            result = _lijst_kandidaten(
                po_id=arguments.get("po_id"),
                kind=arguments.get("kind"),
                cross_po_only=arguments.get("cross_po_only", False),
                gerealiseerd=arguments.get("gerealiseerd"),
            )
        elif name == "markeer_kandidaat_gerealiseerd":
            result = _markeer_kandidaat_gerealiseerd(
                fiche_id=arguments["fiche_id"],
                record_id=arguments.get("record_id"),
                extract_wave_id=arguments.get("extract_wave_id"),
            )
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
    Preload bge-m3 bi-encoder in achtergrond-thread zodat de eerste tool-call
    niet hoeft te wachten. Blokkeert server-startup NIET — Claude Code kan
    al `list_tools` aanroepen terwijl het model laadt.

    De reranker wordt NIET pregeload — alleen geladen bij rerank=True calls.
    Dit bespaart ~3-5s startup-tijd en ~300MB RAM bij agents die nooit reranken.
    """
    import threading

    def _worker() -> None:
        try:
            logger.info("Preload bge-m3 bi-encoder in achtergrond...")
            _get_bi_stack()
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
