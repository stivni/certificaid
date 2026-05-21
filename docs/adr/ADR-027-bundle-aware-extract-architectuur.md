# ADR-027 — Bundle-aware extract-architectuur (2-pass) + daemon-throughput

**Status**: Accepted (gevalideerd via empirische bench 2026-05-21)
**Datum**: 2026-05-21
**Bouwt op**: ADR-008 (concept-extractie), ADR-018 (embedding-daemon), ADR-019 (records-API), ADR-025 (schema 2.0)

---

## Context

Pilot Wave 0a (2026-05-21) toonde dat de eerste-generatie extract-pipeline (`concept-extractie-v5.md` met MCP-tools per-call) **38 minuten per fiche** kostte. Belangrijkste tijddrijvers:

1. **Initiële retrieval-roundtrips**: agent doet ~10-15 MCP-calls voor `lees_kandidaat`, `lees_anchor_bundle`, `lees_record`, `zoek_bronnen` voordat eigenlijk schrijven begint
2. **Daemon-contention bij parallel-runs**: bij 6 concurrent agents stijgt per-fiche-tijd van ~9 min (2-parallel) → ~22 min (6-parallel) door sequentiële cross-encoder rerank op MPS
3. **Exploratory overhead**: agent verkent paden, doet `ls`/`curl`/`grep`-Bash-calls (~3-5 min "warmup")
4. **Save_record overhead**: triggert daemon RAG-update; bij contention queue van 30-60s

Bulk-extract van 400 fiches in batches van 6 zou ~27u kosten op v1-stack. Te traag voor examen-deadline.

---

## Beslissing

### 1. Bundle-aware extract (full 2-pass)

Een Python-script `tools/extractie/build_context_bundle.py` doet **alle deterministische pre-fetch** vóór agent-launch:

| Pre-fetched | Bron | Doel |
|---|---|---|
| `kandidaat` | candidates.sqlite3 | Vervangt `lees_kandidaat`-MCP-call |
| `anchor_bundle` | anchors.json | Vervangt `lees_anchor_bundle`-MCP-call (vector-data stripped — ADR-018) |
| `v1_inspiratie` | data/concepten/records/*.json | Vervangt `lees_record`-MCP-calls voor top-3 v1_hints |
| `template_voorbeelden` | content/experiment/ + recente schema-2.0-records | Paden, geen content — agent leest zelf indien nodig |
| `bronnen_resultaten[].hits` | Daemon `/zoek-bronnen` endpoint | **Echte chunks** voor 4 vooraf-bepaalde queries (`full_2pass=true`) |

Agent doet bij start alleen `Read bundle.json`. Daarna max 1-3 eigen `zoek_bronnen(rerank=true)` voor wettelijke ⚖️-claim-gaten.

### 2. Kind-specifieke query-templates

`build_queries()` gebruikt **per-kind templates** ipv mechanische `naam + motivatie`-concat:

```python
QUERY_TEMPLATES_PER_KIND = {
    "ratio": ["{naam} formule berekening componenten", "{naam} drempels interpretatie ...", ...],
    "fiscale-regeling": ["{naam} voorwaarden toepassing", "{naam} berekening aftrek tarief WIB92", ...],
    "kader": ["{naam} definitie scope toepassingsgebied", ...],
    # ... 10 kinds totaal
}
```

3 kind-specifieke + 1 algemene query (`naam + motivatie[:100]`) = 4 queries per bundle. Verbetert bron-recall t.o.v. mechanische concat.

### 3. Daemon v2.0 — request-batching + gating + concurrent index

`tools/extractie/embedding_daemon.py` herschreven:

- **Rerank-batching**: async queue met 150ms window of max 8 requests bundelt cross-encoder forwards in één MPS-inference. Synthetic bench: 6 concurrent rerank in 6.1s (was 13.6s sequencieel) = **2.2× throughput**.
- **Gating**: skip rerank wanneer bi-encoder top-1 ≥ 0.80 EN top-2/3 ≥ 0.65. Conservatief — vooral effectief bij conceptnaam-queries.
- **Dynamische top_k-uitbreiding**: 1-2 extra resultaten als scores binnen 0.05-margin.
- **Concurrent index-writes**: `ThreadPoolExecutor(max_workers=4)` met aparte `_model_lock` en `_db_write_lock`. `/embed` blokkeert event-loop niet meer.
- **Nieuw endpoint**: `POST /zoek-bronnen` (bi-encoder + optioneel rerank via bestaande batch-queue).
- **Bugfix**: `definitie.source` accepteert nu zowel string (schema 2.0) als dict (schema 1.x).

Config in `tools/extractie/daemon_config.yaml` (batch-window, gating-threshold tunable).

### 4. Compact bundle-aware prompt

`prompts/concept-extractie-v5-bundle.md` vervangt `concept-extractie-v5.md` voor bulk-extract:

- §2a (full-2-pass standaard): geen initiële queries — bundle.bronnen_resultaten[].hits direct gebruiken
- §2b (legacy fallback): als `bundle.full_2pass=false` (daemon offline), agent doet de queries alsnog
- Caps: `zoek_bronnen` ≤ 3 (alleen creatieve), `rerank=true` ≤ 3
- §3 + §4bis: schema-discipline strikt (text/source als string, perspectieven[].rollen[]-array, weergaven genest in hoe_het_werkt.onderdelen[].elementen[])

### 5. Bulk-bundle-builder

`tools/extractie/build_bundles_batch.py` met `--po <code>` / `--all` / `--from-file` modes. Sequentieel; daemon-model 1× gewarmd.

---

## Consequences

### Positief

- **Per-fiche-tijd geschat**: 38 min (v1) → 9-15 min (v2 + bundle) = **~60% reductie**
- **MCP-calls per agent**: 10-15 → 1-3 (init retrieval volledig weg)
- **Daemon-contention bij parallel**: significant minder (bundles seq vooraf, agents doen ~1/4 query-load)
- **Bundle bouwt instant**: ~0.5-2.5s warm, ~10s cold (eenmalige ChromaDB cold-open)
- **Kind-specifieke queries**: betere bron-recall
- **Schema-discipline-prompt-update**: 100% schema-compliance in 6-agent bench (was eerder Sonnet-pitfall met platte dict)

### Negatief / trade-offs

- **Bundle-grootte**: 45-125 KB per bundle (was 30-80 KB met query-strings). Voor bulk: ~80 MB voor 400 bundles — manageable.
- **Bundle-build kost ~5-15s per fiche**: voor 400 fiches sequencieel ~30-60 min. Maar gebeurt vóór agent-launch, niet in agent-tijd.
- **Daemon-batching adds 150ms window-latency** voor single-request scenarios (geen verlies want enkel parallel-scenarios profiteren).
- **`_bronnen_rerank()` helper in daemon is dode code** (rerank via bestaande batch-infrastructure). Cleanup later.
- **ChromaDB `SentenceTransformerEmbeddingFunction` doet embedding 2×** (in query() én in onze custom helper). Verbeter via manuele query_embedding + `query_embeddings`-pad — bekende quick-win, ~1u werk.

### Empirisch gemeten (bench 2026-05-21)

| Scenario | Wall-clock per fiche | MCP-calls |
|---|---|---|
| Half-2-pass + daemon v1, single | 8-9 min | 5 |
| Half-2-pass + daemon v1, 6-parallel | 20-32 min | 10-30 |
| Full-2-pass + daemon v2, single | 9 min 24s | 2 |
| Full-2-pass + daemon v2, 6-parallel | nog te meten | verwacht ~10-15 min |

### Kwaliteit-impact

Bench-records (aandeelhoudersovereenkomst, fraude, vennootschapsbelasting, dbi-aftrek, innovatie-aftrek, investeringsaftrek):

- 100% schema-discipline (text/source/perspectieven-array/weergaven-genest)
- ⚠️-percentage 0-7% (acceptabel)
- Cell-fill matrix 30-50% (target 30-40%)
- Confidence-distributie typisch 60-80% grounded ⚖️ + 10-20% inferred 🔗 + 5-15% vuistregel 🧭

---

## Alternatives considered

### A. Inline-MCP-extract (geen bundle)

Status quo zoals concept-extractie-v5.md. **Verworpen**: te traag voor bulk, daemon-contention onhanteerbaar.

### B. LLM-formulering van queries (haiku-call per fiche)

Bundle-builder roept claude-haiku aan voor 4 contextueel-sterke queries per fiche. **Uitgesteld**: extra kosten + complexiteit; kind-templates zijn "goed-genoeg" volgens bench. Heroverwegen als bron-recall onvoldoende blijkt.

### C. Re-harvest skeleton-queries

Skeleton-agents (Opus) hadden tijdens skeleton-fase semantisch-sterke queries geformuleerd. Re-harvest uit JSONL en bewaar als `kandidaat.suggested_queries[]`. **Uitgesteld**: skeleton-queries waren PO-level discovery, niet fiche-level — mapping te fuzzy. Mogelijk in latere ronde als hybride.

### D. Volledig sync-MCP (geen daemon)

Vervang daemon door direct chromadb-import in MCP-server. **Verworpen**: model-load per agent (~3-5s), geen request-batching mogelijk, geen state-sharing.

---

## Volgende stappen

### Korte termijn (binnen huidige sessie)

1. **6-parallel bench met full-2-pass-stack** — fiches `liquidatiereserve`, `verbonden-partijen`, `kapitaalverhoging`, `roerend-inkomen-internationaal`, `boekhoudkundige-schattingen`, `faillissement`. Meet of theoretische tijdwinst (60%) ook in praktijk gerealiseerd wordt.
2. **Daemon query-cache + manuele query-embedding** — verwijdert ChromaDB-dubbele-embedding-pad. Bi-encoder 1.4s → ~0.3s.

### Middellange termijn

3. **Bundle-builder query-verbetering** — voeg standaard query toe voor "overdraagbaarheid" (geconstateerd als bundle-gap bij investeringsaftrek-test). Mogelijk meer kind-specifieke patronen.
4. **Inline save + markeer in records-API** (`save_record_completed`-functie) — 1 Bash-call ipv save + markeer-MCP apart. ~5-10s/fiche besparing.
5. **Cleanup**: `_bronnen_rerank()` dode code verwijderen.

### Lange termijn (na pilot Wave 0a-launch)

6. **Pilot Wave 0a relaunch** met full-2-pass-stack — 4 fiches uit oorspronkelijk pilot-plan + selecte van 6-bench-fiches.
7. **Bulk-extract van ~400 fiches** via parallel batches met de geoptimaliseerde stack.
8. **Render-template verbetering**: agent C constateerde dat `_Bron: _` leeg blijft voor definitie-source in markdown-output. Klein template-issue.
9. **Skeleton-query-re-harvest** (alternative C) als bron-recall in latere fiches tegenvalt.

---

## Verwijzingen

- Implementatie: `tools/extractie/build_context_bundle.py`, `tools/extractie/embedding_daemon.py`, `tools/extractie/build_bundles_batch.py`
- Config: `tools/extractie/daemon_config.yaml`
- Benchmark-script: `tools/extractie/benchmark_daemon.py`
- Prompt: `prompts/concept-extractie-v5-bundle.md`
- Bench-data: `data/extractie/_global/skeleton-overzicht-20260521T034254Z.md`
- Geschreven records (bench): `data/concepten/records/{aandeelhoudersovereenkomst,fraude,vennootschapsbelasting,dbi-aftrek,innovatie-aftrek,investeringsaftrek,werkkapitaalbehoefte,alarmbel,oeso-modelverdrag,voordelen-alle-aard}.json`
