# Sessie-handoff 2026-05-21 avond — Bulk-extract klaar voor wave-launches

**Voor**: nieuwe Claude Code-sessie die de schema 2.0 bulk-extract gaat draaien
**Status bij handoff**: alle infra-optimalisaties live + 16 schema 2.0 records geschreven + kwaliteit-audit beschikbaar
**Volgende stap**: pilot-wave-extract met geoptimaliseerde stack + reindex-wave per batch

---

## TL;DR voor de nieuwe sessie

1. **Lees CLAUDE.md** — status + wegwijzer (concept-extractie-spoor + tarieven-spoor parallel)
2. **Lees [ADR-027](adr/ADR-027-bundle-aware-extract-architectuur.md)** — bundle-aware extract + daemon v2.0
3. **Verifieer MCP**: `/mcp` slash-command — `certificaid-rag` moet active zijn. **Mogelijk Optie A geactiveerd** (in-process bronnen-queries) — bij twijfel check `tools/extractie/mcp_server/server.py` commit-history
4. **Health-check daemon**: `curl localhost:8765/health`
5. **Volgende concrete stap**: wave-1 extract (6 fiches parallel), eindigend met `reindex-wave` voor batch RAG-sync

---

## 1. Waar we staan

### Wat klaar is (live in main)

**Infrastructure**:
- ✅ Skeleton-fase compleet (425 → 404 kandidaten na consolidatie, [skeleton-overzicht](../data/extractie/_global/skeleton-overzicht-20260521T034254Z.md))
- ✅ Schema 2.0 + ADR-025 §4bis (5-rol-set, eigen-kantoor, 8 consolidatie-regels)
- ✅ Bundle-aware extract architectuur (ADR-027) — full 2-pass, kind-specifieke queries
- ✅ Embedding-daemon v2.0 — request-batching, gating, concurrent index-writes
- ✅ Records-API CLI met `save --wave-id` + `--bulk` + `reindex-wave <wave-id>`
- ✅ Jinja2-templates schema 2.0 (alle 4 render-bugs gefixed)
- ✅ Bundle-builder Tier 1+ (in-process bronnen voor build_bundles_batch sequencieel)
- ✅ Kwaliteits-audit script `tools/extractie/kwaliteits_audit.py` (7 dimensies, vervangt gameable ⚠️-%)
- ✅ Rerank-cap ≤ 1 in prompt (bundle bi-encoder is meestal voldoende)

**Parallel spoor (door user in andere sessie)**:
- ✅ 214 tarief-records (Cijfers-Tarieven 2026, ADR-026)
- ✅ 14 aangifte-PB-walkthrough bronnen (ADR-028)
- ✅ Beide trusted + RAG-geïndexeerd op 13:37 UTC

### 16 schema 2.0-records geschreven

| Record | Model | Score | Wave-tag |
|---|---|---|---|
| liquidatiereserve | Sonnet | **8.44** | wave-bench2-sonnet-liquidatiereserve-20260521 |
| dbi-aftrek | Opus | 8.23 | wave-0a-pilot-20260521 |
| vennootschapsbelasting | Opus | 7.49 | wave-bench-opus-20260521 |
| aandeelhoudersovereenkomst | Opus | 7.24 | wave-bundle-test-opus-20260521 |
| kapitaalverhoging | Sonnet | 6.93 | (geen tag) |
| oeso-modelverdrag | Opus | 6.57 | wave-bench-opus-20260521 |
| alarmbel | Sonnet | 6.25 | (geen tag) |
| werkkapitaalbehoefte | Sonnet | 6.24 | (geen tag) |
| investeringsaftrek | ? | 5.81 | wave-full2pass-test-20260521 |
| roerend-inkomen-internationaal | Opus | 5.77 | wave-bench2-opus-roerend-inkomen-20260521 |
| groepbijdrage | ? | 5.76 | wave-cli-test-groepbijdrage-20260521 |
| fraude | ? | 5.52 | wave-bench-opus-20260521 |
| boekhoudkundige-schattingen | Opus | 5.42 | wave-bench2-opus-boekhoudkundige-schattingen-20260521 |
| verbonden-partijen | Sonnet | 4.86 | (geen tag) |
| innovatie-aftrek | ? | 3.75 | wave-bundle-test-sonnet-20260521 |
| faillissement | Opus | **3.33** | wave-bench2-opus-faillissement-20260521 |

**Belangrijkste insight**: kwaliteit varieert niet primair door model maar door **prompt-discipline op moment van schrijven**. Veel records hebben 0/10 op Slot-sections (`veelvoorkomende_verwarringen`/`familie_en_alternatieven`/`bronnen_en_verwijzingen`) omdat ze geschreven werden vóór de prompt-update §3 die ze verplicht stelde.

**Aanbeveling**: laagscorende records (< 5.5) heroverwegen voor re-extract met huidige prompt. Top-5 zijn bench-baseline.

### 404 kandidaten openstaand (-21 t.o.v. 425 start)

Per kind:
- procedure: 88
- kader: 85 (was 96)
- begripscluster: 67
- regime: 50
- fiscale-regeling: 30
- instrument: 25
- operatie: 18
- ratio: 16
- familie: 15
- balanspost: 10

---

## 2. Bench-resultaten (vergelijkingsbasis)

### Bench2 — 6-parallel met alle optimalisaties (2026-05-21 namiddag)

| Agent | Model | Kind | Wall-clock | Score |
|---|---|---|---|---|
| liquidatiereserve | Sonnet | fiscale-regeling | 5:17 | 8.44 |
| roerend-inkomen-internationaal | Opus | kader (5 deps) | 5:51 | 5.77 |
| boekhoudkundige-schattingen | Opus | begripscluster | 6:52 | 5.42 |
| verbonden-partijen | Sonnet | begripscluster | 7:09 | 4.86 |
| **faillissement** | Opus | procedure | **14:27** (outlier) | 3.33 |
| **kapitaalverhoging** | Sonnet | operatie | **16:54** (outlier) | 6.93 |

**Gemiddelde 9:24**. Bench1 (geen optimalisaties): 22 min. = **-57%**.

**Outliers** waren steeds 3 rerank=true-calls. **Rerank-cap ≤ 1 (now live)** elimineert dit patroon — verwacht voortaan ~5-7 min/fiche consistent.

### 3-way compare (bestuur-vennootschap)

| Variant | Wall-clock | Hallucinatie? |
|---|---|---|
| Opus SPEED | **5:38** | ⚠️ ja (art-nummers uit geheugen als ⚖️) |
| Sonnet | 11:00 | klein |
| Opus standaard | 22:38 | laag |

**Conclusie**: Sonnet is voldoende voor meeste fiches. Opus standaard 2× langzamer maar diepgaander didactisch. Opus SPEED snel maar **niet veilig zonder VERIFY-vangnet**.

---

## 3. Configuratie + tools voor de nieuwe sessie

### Daemon + MCP

```bash
# Daemon health-check
curl -s localhost:8765/health | python3 -m json.tool

# Daemon hot-reload (na config-wijziging)
launchctl kickstart -k gui/$(id -u)/com.certificaid.embedding-daemon

# MCP-server: automatisch gestart door Claude Code per sessie (.mcp.json)
```

### Bundle-builder

```bash
# Single fiche
python3 -m tools.extractie.build_context_bundle <fiche_id>

# Bulk (sequencieel, gebruikt in-process)
python3 -m tools.extractie.build_bundles_batch --po 2.3 --all
python3 -m tools.extractie.build_bundles_batch --from-file fiches.txt
```

### Records-API CLI

```bash
# Voor bulk-extract (skip daemon-RAG tijdens save):
python3 -m tools.lib.records_api save /tmp/<fiche_id>.json --bulk --wave-id wave-1

# Na elke wave: batch reindex
python3 -m tools.lib.records_api reindex-wave wave-1 --dry-run  # preview
python3 -m tools.lib.records_api reindex-wave wave-1            # execute

# Audit RAG-parity
python3 -m tools.lib.records_api audit
```

### Kwaliteits-audit

```bash
# Single record
python3 -m tools.extractie.kwaliteits_audit liquidatiereserve

# Alle records (top-5 best, bottom-5 worst)
python3 -m tools.extractie.kwaliteits_audit --all

# Specifieke wave
python3 -m tools.extractie.kwaliteits_audit --wave wave-bench2-sonnet-liquidatiereserve-20260521

# Verbose (alle dimensie-details)
python3 -m tools.extractie.kwaliteits_audit faillissement --verbose
```

### Candidates-DB

```bash
python3 -m tools.extractie.candidates_db stats
python3 -m tools.extractie.candidates_db lijst <po>  # bv. lijst 2.3
python3 -m tools.extractie.candidates_db lees <fiche_id>
```

### Daemon-benchmark

```bash
python3 -m tools.extractie.benchmark_daemon         # synthetic rerank-batching test
python3 -m tools.extractie.benchmark_bundle_build   # daemon vs in-process bundle build
```

### Tail agent-progress

```bash
python3 -m tools.extractie.tail_agent <agent-id-prefix> --watch  # leesbare event-stream
```

---

## 4. Pending werk

### Optie A — MCP-server lazy-init bi-encoder vs reranker ✅ KLAAR

**Commit**: `8eb0e0a6` — `tools/extractie/mcp_server/server.py`

**Belangrijke vondst**: MCP-server was al volledig in-process voor `zoek_bronnen`. Bench2-queue-contention kwam niet van MCP→daemon-HTTP. Wat A wel deed:
- Gesplitste lazy-init: `_bi_stack` (bge-m3) bij 1e `zoek_bronnen`-call, `_reranker_obj` (CrossEncoder) pas bij 1e `rerank=true`-call
- ~300 MB RAM-besparing per parallel-agent (1.8 GB voor 6 parallel)
- Startup 3-5s sneller per agent
- Graceful fallback als CrossEncoder-load faalt

**Activering**: vereist nieuwe Claude Code-sessie — Claude Code spawnt MCP-server bij sessie-start volgens `.mcp.json`. **Bij start van deze nieuwe sessie is A al actief.**

**Implicatie voor bench2-bottleneck**: de 5+ min queue bij 3-parallel rerank moet andere oorzaak hebben — mogelijk MPS-GPU-resource-sharing, of save_record daemon-write-queue. Voor diagnose: run benchmark in nieuwe sessie en vergelijk daemon-vs-MCP-loads tijdens 6-parallel.

### Wave-extract plan (volgende-sessie)

Volgorde voor pilot Wave 0a relaunch:

**Wave 1 — re-extract laagscorende fiches (~30 min)**:
- innovatie-aftrek (3.75)
- faillissement (3.33)
- verbonden-partijen (4.86)
- boekhoudkundige-schattingen (5.42)
- fraude (5.52)

Met huidige prompt + caps verwacht ~5-7 min/fiche × 6 parallel = ~5-7 min totaal. Plus reindex-wave aan einde.

**Wave 2-N — nieuwe fiches uit candidates-DB**:
Selecteer per wave 6 niet-gerealiseerde kandidaten uit verschillende PO's. Bouw bundles vooraf via `build_bundles_batch.py`. Launch 6 parallel met `--bulk --wave-id wave-N`. Reindex aan einde.

Voor 404 - 16 = 388 te-extracten records → ~65 waves van 6 = ~7-12u totale agent-tijd.

Plus voorbereiding tijd (bundle-build, orchestration): +2-3u.

**Plus VERIFY-pass** als 2e doorgang: 388 records × ~5 min = ~32u. Of slimmer: alleen records met audit-score < 7.0 verifiëren = ~50-100 records × ~5 min = ~4-8u.

### Andere openstaande items

- Cleanup `_bronnen_rerank()` dode code in daemon (bekend)
- Optionele Tier 2: pre-rerank in bundle voor "lastige" kaders/families
- Render-template: `_Bron:_` is gefixt; nog niet alle weergave-types getest (formule-expressie, tabel, tijdslijn, casus)

---

## 5. Belangrijkste lessen-leerlingen

### Schema-discipline (in prompt vastgelegd)

- `text` (niet `inhoud`/`tekst`)
- `source` als string (niet dict)
- `rol_van_de_accountant` = `perspectieven[].rollen[]`-array, géén platte dict
- `weergaven[]` genest in `hoe_het_werkt.onderdelen[].elementen[]`
- `actor`-veld op perspectief (template-vereiste)
- `emoji`-veld per rol (defaults: 🎯/📋/🔍/🛡️/💰)

### Quality > ⚠️-%

- ⚠️-% is gameable (agent zet geen ⚠️ = lijkt schoon)
- Kwaliteits-audit-script scoort op 7 dimensies:
  1. Bron-specificiteit (artikel-nummers in source)
  2. Concrete elementen (weergaven non-proza)
  3. Cell-fill matrix (rol×perspectief diepte)
  4. Slot-sections compleet (verwarringen/alternatieven/bronnen)
  5. Strategisch advies (hoofdrisico/voordeel + vuistregels 10-25%)
  6. Cross-PO completeness (multi-PO anchors)
  7. Hallucinatie-vlag (grounded zonder bron-ref)

### Anti-patterns vermeden

- ❌ `python3 -c "save_record({...})"` — SyntaxError bij grote records (gebruik CLI-save met `/tmp` JSON-file)
- ❌ Aparte markeer_kandidaat_gerealiseerd MCP-call (gebruik `--wave-id` flag)
- ❌ rerank=true cap > 1 (outliers 14-22 min vs 5-7 min)
- ❌ Save zonder `--bulk` tijdens 6-parallel extract (daemon-queue)
- ❌ `python3 reindex-all` mid-bulk (te traag voor 400 records; gebruik `reindex-wave`)

### Worktree-discipline

Sub-agents lopen vaak in worktrees (`.claude/worktrees/agent-<id>/`). Hun output moet meestal gekopieerd naar main repo voor effect. Workflow:
1. Agent rapporteert paden in worktree
2. Orchestrator kopieert relevante files naar main
3. Commit + push

**CLAUDE.md kopiëren** is fout omdat hij vaak door verschillende sessies tegelijk bewerkt wordt — handmatig samenvoegen.

---

## 6. Open vragen voor volgende sessie

1. **Welke records re-extracten** met huidige prompt voor kwaliteit-boost? Audit-score-cutoff bv. < 6.0?
2. **VERIFY-pass strategie**: per-wave of na alle waves? In-process of agent-based?
3. **Cross-PO consolidation**: 21 consolidaties gedaan (425→404). Verdere ronde nodig na nieuwe fiches?
4. **Render-template `eu-jaarrekeningenrichtlijn`**: moet die nog gemerged worden in `jaarrekening`-fiche (uit C9-bouwstenen-collapse-plan)?
5. **Aandelen-fiche maken**: structurele asymmetrie met obligatielening (gesproken over maar uitgesteld)
6. **GIL-issue parallel bundle-build**: in-process is langzamer dan daemon bij thread-parallelle build. Voor process-pool: niet geïmplementeerd. Workaround: use sequentieel (`build_bundles_batch`).

---

## 7. Sessie-statistieken

- **Commits vandaag**: 5 op main (78a70ba2 / 7c2c06c9 / a948b42f / 0bd92a7b / 12404f82)
- **ADRs nieuw of bijgewerkt**: ADR-025 §4bis, ADR-027 (nieuw), CLAUDE.md status (door user)
- **Schema 2.0 records geschreven**: 16
- **Bench-runs**: bench1 (6), bench2 (6), compare-test (3) = 15 agent-extracts
- **Kwaliteit-audit gemiddelde**: 6.2/10 (range 3.33 - 8.44)

---

## 8. Eerste 5 commando's bij sessie-start

```bash
# 1. Health-checks
curl -s localhost:8765/health
python3 -m tools.extractie.candidates_db stats

# 2. Git pull (voor het geval andere sessie pushte)
git pull --rebase

# 3. Check pending Opus A agent-status (mogelijk in worktree)
ls .claude/worktrees/ | grep afdb61

# 4. Quality-audit van alle records
python3 -m tools.extractie.kwaliteits_audit --all | tail -30

# 5. Eerste wave bundle-build
python3 -m tools.extractie.build_bundles_batch --from-file <waveplan.txt>
```

---

**Examen-deadline**: ca. 2026-05-30 — krap maar haalbaar met bulk-extract-cadans van ~6-12 fiches/uur via 6-parallel + reindex-wave.
