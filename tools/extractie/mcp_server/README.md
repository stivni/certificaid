# Certificaid RAG MCP-server

Stelt vijf tools beschikbaar aan extract- en skeleton-subagenten via MCP
(stdio-transport). Vervangt het vooraf-bundelen van initial-ctx door
on-demand bevragingen — agent kiest zelf welke chunks hij wanneer ophaalt.

Beschreven in: ADR-025 §EXTRACT v5 + `prompts/concept-extractie-v5.md`.

## Beschikbare tools

| Tool | Doel |
|---|---|
| `zoek_bronnen(query, top_k, bron_rollen, rerank)` | RAG-query tegen wetteksten/KB/CBN/normen, met optionele cross-encoder rerank |
| `zoek_concepten(query, top_k)` | RAG-query tegen bestaande concept-records (near-duplicate-check) |
| `lees_record(record_id)` | Lees volledige JSON-inhoud van één record |
| `lees_anchor_bundle(po_id)` | Geef anchors + TDKs voor een programmaonderdeel |
| `check_record_bestaat(record_id)` | Filesystem-check voor record-id |

## Installatie

Eénmalig:

```bash
pip3 install mcp
```

(Toegevoegd aan `requirements.txt`.)

## Manueel starten (voor lokale test)

```bash
python3 -m tools.extractie.mcp_server.server
```

Loopt als stdio-server. Verwacht JSON-RPC-berichten op stdin.

## Manueel testen zonder MCP-client (functie-niveau)

```bash
python3 -c "
from tools.extractie.mcp_server.server import _zoek_bronnen, _lees_record
print(_zoek_bronnen('matching-beginsel rente prorata', 3))
print('---')
print(_lees_record('obligatielening')[:500])
"
```

Eerste call van `_zoek_bronnen` triggert bge-m3 + reranker laden (~5-15s).
Daaropvolgende calls zijn snel.

## Integratie met Claude Code

Project-MCP-config staat in [`.mcp.json`](../../../.mcp.json) op project-root.
Claude Code start de server automatisch bij sessie-begin (eerste tool-call
triggert bge-m3-laden, ~10s).

Subagenten in EXTRACT v5 of skeleton-voorstel zien de 5 tools in hun toolbox
en kunnen ze direct aanroepen.

**Verifiëren dat de server geladen is** in Claude Code:
- `/mcp` slash-command toont actieve servers
- Of een tool aanroepen: bv. `check_record_bestaat("obligatielening")`

Bij eerste sessie-start na clone/pull: Claude Code vraagt mogelijk toestemming
om de server te starten (één keer goedkeuren).

## Architectuur-noten

- **Geen schrijfacties**: deze server doet alleen reads. Schrijven gaat
  via `tools.lib.records_api.save_record()` direct vanuit subagent.
- **ChromaDB-pad**: `data/rag/main` (canoniek per ADR-019).
- **Lazy-init**: bge-m3 + reranker worden pas geladen bij eerste `zoek_*`-call.
- **Geen daemon-roundtrip**: queries gaan direct naar ChromaDB via
  `tools/lib/retrieval.py`. Embedding-daemon (`tools/extractie/embedding_daemon.py`)
  blijft bestaan voor write-side concept-indexering via records-API.

## Toekomstige tools (zoals nodig)

- `voorgestelde_buren(record_id, edge_types?)` — graph-walk over edges
- `lees_bron_md(bron_id, sectie?)` — directe markdown-read van een bron
- `lijst_records_in_po(po_id)` — filesystem-scan voor records met PO-anchors
