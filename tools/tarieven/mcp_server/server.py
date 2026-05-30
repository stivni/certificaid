"""
MCP-server certificaid-tarieven (ADR-026).

Stelt vier tools beschikbaar voor agents en het tutor-platform:

  - lijst_tabellen(categorie?)
       Lijst alle tarief-records, optioneel gefilterd op categorie.
       Compacte representatie (id, titel, categorie, wetsbasis).

  - lees_tabel(record_id)
       Volledig JSON-record on-demand.

  - zoek_tabellen(query, top_k?)
       Text-match op titel / wetsbasis / samenvatting / tags. Geen embeddings.

  - query_tabel(record_id, vraag)
       Helper voor "geef alleen X uit deze tabel" — v1: retourneert het volledige
       record + de vraag-context; agent extraheert zelf het cijfer. Latere versies
       kunnen veld-routing toevoegen.

Architectuur:
  - In-process disk-reads, geen daemon-roundtrip
  - Geen RAG-collection (ADR-026 — disk is enige bron-van-waarheid)
  - Stateless: elke call leest disk vers (atomair, geen stale cache)

Start (stdio-transport, standaard voor Claude Code MCP):
  python3 -m tools.tarieven.mcp_server.server
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
import sys
from pathlib import Path
from typing import Any

# Voeg root toe aan sys.path zodat tools.lib imports werken
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from tools.lib import tarieven_api  # noqa: E402

logger = logging.getLogger(__name__)

RECORDS_DIR = ROOT / "data" / "tarieven" / "records"


# ---------------------------------------------------------------------------
# Tool-implementaties
# ---------------------------------------------------------------------------

def _compact(record: dict) -> dict:
    """Compacte representatie voor lijsten."""
    return {
        "id": record["id"],
        "titel": record["titel"],
        "categorie": record["categorie"],
        "wetsbasis": [f"{w['bron']} art. {w['artikel']}" for w in record.get("wetsbasis", [])],
        "samenvatting": record.get("samenvatting", "")[:200],
        "confidence": record.get("confidence"),
        "trusted": record.get("metadata", {}).get("trusted", False),
    }


def _alle_records() -> list[dict]:
    if not RECORDS_DIR.exists():
        return []
    out = []
    for pad in sorted(RECORDS_DIR.glob("*.json")):
        try:
            out.append(json.loads(pad.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Kon record %s niet laden: %s", pad, exc)
    return out


def _lijst_tabellen(categorie: str | None = None) -> str:
    records = _alle_records()
    if categorie:
        records = [r for r in records if r.get("categorie") == categorie]
    return json.dumps(
        {
            "totaal": len(records),
            "tabellen": [_compact(r) for r in records],
            "filter": {"categorie": categorie},
        },
        indent=2,
        ensure_ascii=False,
    )


def _lees_tabel(record_id: str) -> str:
    try:
        record = tarieven_api.load_record(record_id)
    except tarieven_api.TariefRecordNotFoundError:
        return json.dumps({"error": f"Record niet gevonden: {record_id}"})
    return json.dumps(record, indent=2, ensure_ascii=False)


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> set[str]:
    return set(_TOKEN_RE.findall(text.lower()))


def _score(record: dict, query_tokens: set[str]) -> float:
    """Eenvoudige token-overlap met veldgewichten."""
    if not query_tokens:
        return 0.0
    weights = {
        "titel": 3.0,
        "samenvatting": 1.5,
        "wetsbasis": 2.5,
        "tags": 2.0,
        "categorie": 1.5,
        "criteria_naam": 1.0,
    }
    score = 0.0
    titel_tok = _tokenize(record.get("titel", ""))
    score += weights["titel"] * len(query_tokens & titel_tok)
    samen_tok = _tokenize(record.get("samenvatting", ""))
    score += weights["samenvatting"] * len(query_tokens & samen_tok)
    wet_tok = _tokenize(
        " ".join(f"{w.get('bron','')} {w.get('artikel','')}" for w in record.get("wetsbasis", []))
    )
    score += weights["wetsbasis"] * len(query_tokens & wet_tok)
    tag_tok = _tokenize(" ".join(record.get("tags", [])))
    score += weights["tags"] * len(query_tokens & tag_tok)
    cat_tok = _tokenize(record.get("categorie", ""))
    score += weights["categorie"] * len(query_tokens & cat_tok)
    crit_tok = _tokenize(" ".join(c.get("naam", "") for c in record.get("criteria", [])))
    score += weights["criteria_naam"] * len(query_tokens & crit_tok)
    return score


def _zoek_tabellen(query: str, top_k: int = 5) -> str:
    qtok = _tokenize(query)
    if not qtok:
        return json.dumps({"error": "Lege query"})
    records = _alle_records()
    scored = [(r, _score(r, qtok)) for r in records]
    scored.sort(key=lambda x: x[1], reverse=True)
    hits = [(r, s) for r, s in scored if s > 0][:top_k]
    return json.dumps(
        {
            "query": query,
            "hits": [
                {"score": round(s, 2), **_compact(r)} for r, s in hits
            ],
        },
        indent=2,
        ensure_ascii=False,
    )


def _query_tabel(record_id: str, vraag: str) -> str:
    """v1: returnt volledig record + vraag-context. Agent interpreteert."""
    try:
        record = tarieven_api.load_record(record_id)
    except tarieven_api.TariefRecordNotFoundError:
        return json.dumps({"error": f"Record niet gevonden: {record_id}"})
    return json.dumps(
        {
            "record": record,
            "vraag": vraag,
            "hint": "Lees record['criteria'] voor cijferinhoud. Gebruik wetsbasis voor wetsverwijzing.",
        },
        indent=2,
        ensure_ascii=False,
    )


# ---------------------------------------------------------------------------
# MCP-server setup
# ---------------------------------------------------------------------------

app = Server("certificaid-tarieven")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="lijst_tabellen",
            description=(
                "Lijst alle tarief-records (compacte representatie). Optioneel filteren op "
                "categorie: 'groottecriteria' · 'personenbelasting' · 'vennootschapsbelasting' · "
                "'voorafbetalingen' · 'btw' · 'sociale-zekerheid' · 'indexcoefficient' · "
                "'roerende-voorheffing' · 'registratierechten' · 'successierechten' · 'overig'."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "categorie": {
                        "type": "string",
                        "description": "Optioneel categoriefilter",
                    },
                },
            },
        ),
        Tool(
            name="lees_tabel",
            description=(
                "Lees volledig tarief-record on-demand. Returns alle velden inclusief criteria, "
                "wetsbasis, geldigheidsperiode en bron."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "record_id": {
                        "type": "string",
                        "description": "Slug, bv. 'drempels-groep-beperkte-omvang'",
                    },
                },
                "required": ["record_id"],
            },
        ),
        Tool(
            name="zoek_tabellen",
            description=(
                "Text-match-zoek over titel, wetsbasis, samenvatting, tags en categorie. "
                "Geen embeddings — token-overlap met veldgewichten. Returns top-K hits met score."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natuurlijke-taal-query, bv. 'drempels groep van beperkte omvang' of 'WVV 1:26'",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Aantal hits (default 5, max 20)",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="query_tabel",
            description=(
                "Helper: returnt volledig record + context-hint zodat de agent een specifiek "
                "veld kan extraheren (bv. 'wat is de werknemers-drempel?'). v1: agent-interpretatie. "
                "Latere versies kunnen veld-routing toevoegen."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "record_id": {"type": "string"},
                    "vraag": {"type": "string"},
                },
                "required": ["record_id", "vraag"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    try:
        if name == "lijst_tabellen":
            result = _lijst_tabellen(categorie=arguments.get("categorie"))
        elif name == "lees_tabel":
            result = _lees_tabel(record_id=arguments["record_id"])
        elif name == "zoek_tabellen":
            result = _zoek_tabellen(
                query=arguments["query"],
                top_k=arguments.get("top_k", 5),
            )
        elif name == "query_tabel":
            result = _query_tabel(
                record_id=arguments["record_id"],
                vraag=arguments["vraag"],
            )
        else:
            result = json.dumps({"error": f"Onbekende tool: {name}"})
    except KeyError as exc:
        result = json.dumps({"error": f"Missing parameter: {exc}"})
    except Exception as exc:  # noqa: BLE001
        logger.exception("Tool-fout %s", name)
        result = json.dumps({"error": f"Onverwachte fout in {name}: {exc}"})
    return [TextContent(type="text", text=result)]


async def _main_async() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


def main() -> int:
    logging.basicConfig(level=logging.WARNING)
    try:
        asyncio.run(_main_async())
        return 0
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
