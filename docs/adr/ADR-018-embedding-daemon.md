# ADR-018: Embedding-daemon voor concept-extractie

**Status**: Draft
**Datum**: 2026-05-08
**Verwante ADRs**: ADR-006 (RAG-strategie, bge-m3 als bi-encoder), ADR-008 (concept-extractie flow)

## Context

Tijdens concept-extractie (ADR-008 fase C) indexeert de Opus-subagent elk nieuw concept-record:

1. `index_concept_incremental.py --duplicaat-check "<naam>"` — embed naam, query `concepten`-collection
2. `index_concept_incremental.py --concept <pad>` — embed record, upsert in `concepten`-collection

Elk script-aanroep laadt het bge-m3 model van disk (~1.2 GB, ~5–15 sec cold-start). Voor één PO met 74 anchors (PO 1.1 Algemene boekhouding) betekent dat 148 model-loads = **~20–30 minuten puur cold-start overhead**, voor een totale extractie-batch van ~90 minuten Opus-reasoning.

Tweede zorg: als meerdere extractie-runs parallel draaien (bv. ADR-007-schema-werk in worktree A, productie-extractie in worktree B), willen we **geen drie bge-m3-instances in geheugen** (3.6 GB, MPS-contention, tragere device-warmups). Eén gedeelde service is logischer.

Derde zorg: de extractie-flow vereist **strikte read-after-write consistency** in de `concepten`-collection (ADR-008 fase C: concept N+1 moet concept N kunnen vinden in zijn duplicate-check). Met meerdere ChromaDB-clients tegelijk schrijvend ontstaat staleness-risico.

## Beslissing

Bouw een **long-running embedding-daemon** die:
- bge-m3 één keer laadt en in memory houdt
- de **enige schrijver** is voor de `concepten`-collection
- via HTTP op `localhost:8765` bereikbaar is voor concurrent clients
- automatisch start bij login via een macOS LaunchAgent
- bij downtime gracieus degradeert: clients vallen terug op in-process embedding

### Architectuur

```
┌────────────────────┐         ┌─────────────────────────┐
│ Agent #1 (PO 4.0)  │──┐      │ embedding_daemon.py     │
│ Agent #2 (PO 4.1)  │──┼─►    │ - FastAPI op :8765       │
│ index_*.py CLI     │──┘      │ - bge-m3 in memory      │
│                              │ - ChromaDB-client open  │
│                              │ - MPS-device (auto-     │
│                              │   detect)                │
│                              └─────────────────────────┘
│                                       │
│                                       ▼
│                              ┌─────────────────────────┐
│                              │ data/rag/4.0/     │
│                              │   concepten-collection  │
│                              └─────────────────────────┘
```

### Endpoints

| Endpoint | Method | Body | Response | Doel |
|---|---|---|---|---|
| `/health` | GET | — | `{status, model, device, collection_size, last_write}` | sanity-check, monitoring |
| `/embed` | POST | `{texts: [str]}` | `{embeddings: [[float]]}` | losse embedding-call (zelden gebruikt extern) |
| `/duplicate-check` | POST | `{naam: str, threshold: float}` | `{matches: [{id, score, naam}]}` | concept-collection bevragen tijdens extractie |
| `/index-concept` | POST | `{record: {...}, chroma_path: str}` | `{id, chunk_count, ok: bool}` | concept-record embedden + upserten |
| `/refresh` | POST | `{chroma_path: str}` | `{ok: bool}` | force-reopen ChromaDB-client (bij externe writes) |

Alle endpoints geven nette JSON-errors terug (`{error: str, code: int}`) bij failure; clients handlen falen-zacht.

### Concurrency-model

- **FastAPI + uvicorn** met async request-handling
- **Eén** model-instance gedeeld over alle requests (read-only na load, thread-safe)
- **Eén** ChromaDB-client per `chroma_path` gedeeld (open clients in een dict, lazy-init bij eerste call)
- **Inferentie-queue**: opeenvolgende `/embed` of `/duplicate-check`-calls worden serialiseerd op de MPS/CPU — tweede client wacht enkele 100ms, geen probleem voor een batch-pipeline
- **Schrijf-serialisatie**: `/index-concept`-calls worden semaforisch geserialiseerd zodat ChromaDB-upserts niet interleaven

### Eigenaarschap collecties

| Collection | Eigenaar | Schrijvers |
|---|---|---|
| `concepten` | embedding-daemon | **enkel** de daemon (alle extractie-tools gaan via `/index-concept`) |
| `bronnen` | `tools/rag/rag_index.py` | rag_index.py exclusief; daemon enkel voor reads (toekomstig: `/query-bronnen`) |

Dit voorkomt write-conflicts en stale snapshots.

### Consistency-garanties

- **Read-after-write binnen daemon**: na elke `/index-concept` doet de daemon een `client.heartbeat()` of `collection.count()` om persistentie te forceren vóór de response. Volgende `/duplicate-check` ziet de write.
- **Geen embedding-cache boven ChromaDB**: de daemon caches alleen het *model* en *open clients*, geen embeddings. Source of truth blijft ChromaDB op disk.
- **Externe writes**: als iets buiten de daemon naar `concepten` schrijft (niet voorzien), kan de daemon's snapshot stale worden. `/refresh` herstelt dat. Gebruikersconvenant: ga niet rechtstreeks naar `concepten`-collection schrijven.

### Lifecycle — LaunchAgent

```xml
<!-- ~/Library/LaunchAgents/com.certificaid.embedding-daemon.plist -->
<plist>
  <dict>
    <key>Label</key><string>com.certificaid.embedding-daemon</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/env</string>
      <string>python3</string>
      <string>/Users/stivni/Documents/ITAA/certificaid/tools/extractie/embedding_daemon.py</string>
      <string>--port</string><string>8765</string>
    </array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
    <key>StandardOutPath</key><string>~/Library/Logs/certificaid-embedding-daemon.log</string>
    <key>StandardErrorPath</key><string>~/Library/Logs/certificaid-embedding-daemon.err.log</string>
  </dict>
</plist>
```

Installatie:
```bash
launchctl load -w ~/Library/LaunchAgents/com.certificaid.embedding-daemon.plist
```

Stop:
```bash
launchctl unload ~/Library/LaunchAgents/com.certificaid.embedding-daemon.plist
```

`KeepAlive: true` zorgt voor automatische restart bij crash.

### Client-strategie — graceful degradation

`tools/lib/embedding_client.py`:

```python
def embed_or_fallback(texts: list[str]) -> list[list[float]]:
    if daemon_alive():
        return daemon_post("/embed", {"texts": texts})["embeddings"]
    else:
        # fallback: in-process bge-m3 load (langzaam, maar werkt)
        return _local_embed(texts)
```

Voordeel: scripts (`index_concept_incremental.py`, `rag_query.py`) blijven functioneren ook als de daemon niet draait. CI/eerste-run werkt zonder LaunchAgent.

### Foutmodi

| Scenario | Detectie | Reactie |
|---|---|---|
| Daemon niet bereikbaar | `requests.ConnectionError` | Fallback naar in-process |
| Daemon trage response (> 30s) | timeout | Fallback + log waarschuwing |
| Daemon `/health` rapporteert wrong device | health-check bij script-start | Log waarschuwing, ga door |
| Twee daemons starten (port conflict) | LaunchAgent + handmatige start | Tweede faalt met `EADDRINUSE` — geen split-brain |

### Beveiliging

- Bind enkel op `127.0.0.1` (localhost), niet op `0.0.0.0`. Daemon is een lokale dev-tool, geen netwerk-service.
- Geen authenticatie nodig (alleen lokale processen op de machine kunnen connecten).
- Geen schrijftoegang tot bestanden buiten `data/rag/` en `data/concepten/records/` — daemon mag pad-validatie afdwingen op `chroma_path`-parameters.

## Gevolgen

- **Nieuwe bestanden**:
  - `tools/extractie/embedding_daemon.py` — FastAPI-server
  - `tools/lib/embedding_client.py` — gedeelde HTTP-client met fallback
  - `~/Library/LaunchAgents/com.certificaid.embedding-daemon.plist` — auto-start config
  - `tools/extractie/install_daemon.sh` — installer voor de plist + dependencies-check
- **Aanpassingen**:
  - `tools/extractie/index_concept_incremental.py` — gebruikt `embedding_client` ipv directe bge-m3-load
  - `tools/rag/rag_query.py` — optioneel via daemon
- **Niet geraakt**:
  - `tools/rag/rag_index.py` — blijft zijn eigen bge-m3 laden voor bron-rebuilds (zelden, niet performance-kritisch)
  - `tutor/app.py` — productie-runtime, niet via daemon (heeft eigen sentence-transformer load)
- **Performance-impact**: ~20–30 min/PO sneller bij batch-extractie (cold-start eliminatie). Bij ad-hoc CLI-gebruik (één duplicate-check) ook merkbaar — eerste call ~5s (daemon-warm-up wachten), volgende calls instant.
- **Operational**: één extra LaunchAgent in `launchctl list`. Memory-footprint: ~1.5 GB residente bge-m3 + chromaDB-overhead. Bij geheugendruk: `launchctl unload` om hem af te zetten.

## Out-of-scope

- GPU/CUDA-detectie buiten MPS — niet relevant voor lokale Mac-dev. Toekomst: bij eventuele Linux/CI-deployment via container.
- Authenticated/encrypted endpoints — niet nodig voor localhost-only service.
- Distributed-mode (meerdere machines) — Certificaid is een single-developer-project, geen schaalprobleem.
- Caching van duplicate-check-resultaten — ChromaDB-queries zijn al ~10ms, niet de bottleneck.
