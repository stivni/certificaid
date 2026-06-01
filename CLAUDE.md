# Certificaid

Kennisbank voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant. Destilleert uit het officiële ITAA-examenprogramma (taken, doelstellingen en kenniselementen per programmaonderdeel) + wetteksten + normen + voorbeeldexamens het studiemateriaal dat ontbreekt.

**Doelpubliek**: Stagiairs GA/GBA met boekhoudkundige en fiscale basiskennis — geen juristen.

**Bij het examen beschikbaar**: ITAA-LEX (wettekstenbundel) + Cijferzakboekje (tarieven en bedragen). Wat getoetst wordt: concepten begrijpen, uitzonderingen herkennen, correct redeneren — niet cijfers uit het hoofd kennen.

**Actuele status + openstaand werk**: zie [`docs/TODO.md`](docs/TODO.md). De huidige hoofdactiviteit is **Fase 7** (schema 2.1 v1.5 + extractie v6 + render-laag-revisie). Examen-deadline ca. 2026-05-30.

---

## Doc-discipline — welk document is waarvoor?

Bij twijfel "waar zoek ik X?": deze tabel beslist. Pak nooit een handoff of memory voor info die in een ADR of TODO hoort.

| Doc-type | Locatie | Rol | Levensduur |
|---|---|---|---|
| **ADR** | `docs/adr/ADR-NNN-*.md` | Architectuurbeslissing — de waarheid over een keuze + rationale | Permanent (kan superseded worden door later ADR) |
| **Schrijfregels** | `docs/concept-schrijfregels.md`, `docs/studiemateriaal-schrijfregels.md` | Inhoudelijke conventie — hoe content geschreven moet | Permanent (incrementeel bijgewerkt) |
| **Werkpakket-spec** | `docs/schema-v15-besluit.md`, `docs/render-laag.md` | Gedetailleerde spec voor een lopende implementatie-ronde | Tot werkpakket klaar; daarna bevroren of geabsorbeerd in ADR |
| **TODO / roadmap** | `docs/TODO.md` | Openstaand werk + fase-status + mindset-principes — *de* status-bron. Voltooid werk leeft hier niet (zie ADR/git). | Levend |
| **Prompt** | `prompts/<naam>.md` of `prompts/operaties/<operatie>.md` | Uitvoeringsinstructie aan een (Sonnet) agent | Eén canonieke versie per type; oude versies weg |
| **Memory** | `~/.claude/projects/.../memory/` | Evergreen gedragsregels + design-rationale die niet in een ADR leeft | Levend; bij stale → archive/ |
| **Handoff / sessie-md** | n.v.t. | **Bestaat niet**. Sessie-handoffs worden niet als permanente docs bewaard — info gaat naar TODO/ADR. | n.v.t. |

Regel 9 ("geen leftovers") geldt voor docs evenzeer als voor code: superseded ADR → `docs/adr/archive/`, oude prompt-versie → `git rm`, sessie-handoff → info redistribueren + weg.

---

## Wegwijzer

| Taak | Zie |
|---|---|
| Openstaand werk + fase-status + mindset | [`docs/TODO.md`](docs/TODO.md) |
| Architectuurbeslissing opzoeken of toevoegen | [`docs/adr/INDEX.md`](docs/adr/INDEX.md) |
| **Schema 2.1 v1.5 concept-record schrijven** | [ADR-029](docs/adr/ADR-029-schema-21-operaties-model.md) + canonieke spec [`docs/schema-v15-besluit.md`](docs/schema-v15-besluit.md) + schema [`data/concepten/schema-2.1.schema.json`](data/concepten/schema-2.1.schema.json) |
| **Granulariteit — wanneer eigen record vs sub-sectie?** | [ADR-030](docs/adr/ADR-030-granulariteit-typologie.md) (rationale-meta + regels A-J) + **[`docs/granulariteit-skelet.md`](docs/granulariteit-skelet.md)** (concrete concept-tree voor hele corpus, in opbouw — sparring-document, wordt canonieke skelet-spec). Sparring-historiek typologie: [`docs/granulariteit-typologie-draft.md`](docs/granulariteit-typologie-draft.md). |
| **Operatie toepassen op schema 2.1-record** (extractie v6) | ADR-029 §Operaties-model — 7 operaties: `beschrijven` · `claims_checken` · `relaties_aanvullen` · `accountant_perspectief` · `didactisch_verrijken` · `kandidaat_review` · `leespad_aanvullen`. Prompts: [`prompts/operaties/`](prompts/operaties/) |
| **Render-laag schema 2.1 v1.5** | [`docs/render-laag.md`](docs/render-laag.md) — werkpakket-spec; werk-tracking in TODO.md §Fase 7 |
| **Skeleton-voorstel (pre-extractie stap 0)** | [`prompts/skeleton-voorstel-v1.md`](prompts/skeleton-voorstel-v1.md) — Opus-subagent met MCP-tools |
| Concept-record schrijven of bewerken (records-API) | [`tools/lib/records_api.py`](tools/lib/records_api.py) — `save_record` / `rename_record` / `delete_record` / `audit_parity`. Atomair disk + RAG + content. Pre-commit hook. ADR-019. |
| Concept-record-schrijfregels (taxonomie, taal, edges) | [`docs/concept-schrijfregels.md`](docs/concept-schrijfregels.md) *(wordt herzien voor schema 2.2)* |
| Daemon-status / restart | `curl localhost:8765/health` · `launchctl kickstart -k gui/$(id -u)/com.certificaid.embedding-daemon` |
| **MCP-server `certificaid-rag`** (on-demand retrieval) | [`tools/extractie/mcp_server/`](tools/extractie/mcp_server/) — `zoek_bronnen` · `zoek_concepten` · `zoek_vragen` · `lees_record` · `lees_anchor_bundle` · `check_record_bestaat` + candidates-DB tools. Config: [`.mcp.json`](.mcp.json) |
| **MCP-server `certificaid-tarieven`** (tarief-records) | [`tools/tarieven/mcp_server/`](tools/tarieven/mcp_server/) — `lijst_tabellen` · `zoek_tabellen` · `lees_tabel` · `query_tabel`. ADR-026. |
| Bronnen-overzicht (type + trust-status per bron) | [`resources/bronnen/INDEX.md`](resources/bronnen/INDEX.md) — auto-gegenereerd; machine-leesbaar in `data/bronnen-index.json` |
| Bron als trusted markeren + RAG verversen | `python3 -m tools.etl.mark_trusted --refresh` (ADR-005 §9) |
| Worktree-status / opkuis (stale agent-worktrees voorkomen) | `tools/worktree_status.sh` (lijst) · `tools/worktree_status.sh --prune-safe` (verwijdert MERGED zonder uncommitted + broken). Categorieën: MERGED · AHEAD=N (commits niet in main — handmatig nakijken) · BROKEN. |
| Provenance van een artefact bekijken / stale-flaggen | `tools/etl/add_provenance.py`, `tools/etl/mark_stale.py` |
| **Examenvragen indexeren / zoeken** | `python3 -m tools.rag.rag_index --add-vragen` · MCP-tool `zoek_vragen` (args: `query`, `top_k=5`, optioneel `programmaonderdeel_id`) |
| **Render leermateriaal** (fiches + minicursus) | `tools/leermateriaal/` — ADR-007, ADR-010 *(schema 2.0; render-laag voor schema 2.1 v1.5 in [`docs/render-laag.md`](docs/render-laag.md))* |
| **Overzicht schrijven** (UI-term; intern "minicursus" — PO-niveau verhaal + routekaart, gerendered op `studiemateriaal/<po-slug>/index.md`) | [ADR-036](docs/adr/ADR-036-drie-lagen-leermateriaal.md) + [`docs/minicursus-schrijfregels.md`](docs/minicursus-schrijfregels.md) + gold-standard `content/studiemateriaal/1-4/index.md` |
| **Samenvatting schrijven voor een PO** (geheugen-kapstok, printbaar 2-4 A4 — vervangt cluster-themafiches) | [`docs/samenvatting-procedure.md`](docs/samenvatting-procedure.md) (4 stappen + 3 pijlers: visueel-dominant · 2-4 A4 printbaar · geen cross-PO refs). Schema: [`data/samenvattingen/SCHEMA.md`](data/samenvattingen/SCHEMA.md). Render-prompt: [`prompts/samenvatting-render-v1.md`](prompts/samenvatting-render-v1.md). Schrijfregels: [`docs/samenvatting-schrijfregels.md`](docs/samenvatting-schrijfregels.md). Beleid: [ADR-039](docs/adr/ADR-039-samenvatting-vervangt-themafiche.md). Gold-standard: PO 1.4 ([`data/samenvattingen/1-4.yaml`](data/samenvattingen/1-4.yaml) — in opbouw). **POC-status** — themafiche-schrijfregels gearchiveerd (`docs/archive/themafiche-schrijfregels.md`). |
| **Volledig PO-studiemateriaal uitbouwen** (alle 5 leerlagen voor een nieuw PO) | **Orchestrator**: [`docs/leerstuk-procedure.md`](docs/leerstuk-procedure.md) (9 stappen: skelet → voorbeeldgroep → leerstuk-scripts → leerstuk-render → overzicht → samenvatting → oefening → voorbeeldexamenvragen → integratie). Resultaat: `content/studiemateriaal/<po-slug>/` met `index.md` + `<leerstuk>.md` × N + `samenvatting.md` + `oefening.md` + `voorbeeldexamenvragen.md`. ADRs: [ADR-036](docs/adr/ADR-036-drie-lagen-leermateriaal.md) (overzicht-laag) + [ADR-037](docs/adr/ADR-037-leerstuk-vierde-leerlaag.md) (leerstuk-laag) + [ADR-039](docs/adr/ADR-039-samenvatting-vervangt-themafiche.md) (samenvatting) + [ADR-040](docs/adr/ADR-040-voorbeeldexamenvragen-in-leerpadstructuur.md) (voorbeeldexamenvragen-structuur) + [ADR-041](docs/adr/ADR-041-rename-studiemateriaal-overzicht.md) (terminologie). Gold-standard: PO 1.4 (referentie-skelet: [`docs/leerpad-skelet-1-4.md`](docs/leerpad-skelet-1-4.md)). Stand-van-zaken: [`docs/leerstuk-status.md`](docs/leerstuk-status.md). **Terminologie**: in de UI "overzicht" (kop + sidebar) — in docs/prompts/code "minicursus" als interne term. |
| **Leerstuk schrijven of bewerken** (binnen bestaande PO-leerpad) | [`docs/leerstuk-procedure.md`](docs/leerstuk-procedure.md) Stap 3-4 + [`docs/leerstuk-schrijfregels.md`](docs/leerstuk-schrijfregels.md) + script-prompt [`prompts/leerstuk-scripts-v1.md`](prompts/leerstuk-scripts-v1.md) + render-prompt [`prompts/leerstuk-render-v1.md`](prompts/leerstuk-render-v1.md). Schema: [`data/leerstukken/SCHEMA.md`](data/leerstukken/SCHEMA.md). Gedeelde data: [`data/voorbeeldgroepen/`](data/voorbeeldgroepen/). |
| **Voorbeeldexamenvragen renderen** (per PO + cross-PO overview, auto) | [ADR-040](docs/adr/ADR-040-voorbeeldexamenvragen-in-leerpadstructuur.md). Run: `python3 -m tools.examen.render_merged_v4`. Output: `content/studiemateriaal/<po-slug>/voorbeeldexamenvragen.md` per PO (incl. stub voor PO's zonder vragen) + `content/voorbeeldexamens/index.md` (cross-PO overzicht) + `content/voorbeeldexamens/nieuw.md` (recent toegevoegde examens). Auto-genummerd `explorer_title` op basis van bestaande siblings. |
| **Leerstuk-feedback geven** (bestaand leerstuk verbeteren) | [`docs/leerstuk-procedure.md`](docs/leerstuk-procedure.md) §"Feedback op een bestaand leerstuk". Gouden regel: **bewerk nooit rechtstreeks de gegenereerde markdown** — script-YAML editen + re-render via prompt. Multi-leerstuk feedback: parallel subagenten |
| **Oefening schrijven voor een PO** (5e leerlaag — actieve doorwerk-case na de leerstukken) | [`docs/oefening-procedure.md`](docs/oefening-procedure.md) (4 stappen + 3 pijlers: geen hints in opgave · realistische individuele JR met aparte intra-groep mapping · niet-voorkauwende instructies). Schema: [`data/oefeningen/SCHEMA.md`](data/oefeningen/SCHEMA.md). Render-prompt: [`prompts/oefening-render-v1.md`](prompts/oefening-render-v1.md). Gold-standard: PO 1.4 Nordica ([`data/oefeningen/nordica-consolideren.yaml`](data/oefeningen/nordica-consolideren.yaml)). **POC-status** — na 2-3 PO's consolideren in ADR-038 of amendement ADR-036. |
| **Leerstuk-script schrijven of bewerken** | [`data/leerstukken/SCHEMA.md`](data/leerstukken/SCHEMA.md) (script-schema) + [`data/leerstukken/`](data/leerstukken/) als referentie (6 scripts voor PO 1.4) + gedeelde data in [`data/voorbeeldgroepen/`](data/voorbeeldgroepen/) |
| **Tarief-record schrijven of trusten** | [`tools/lib/tarieven_api.py`](tools/lib/tarieven_api.py) — `save_record` · `mark_trusted` · `audit`. Schrijft alleen `data/tarieven/records/<id>.json` (geen content/-render). Schema: [`data/tarieven/schema.json`](data/tarieven/schema.json). ADR-026. |
| **Tarief-extractie pipeline** (Sonnet-subagent + vision) | Chunker: `python3 -m tools.tarieven.chunk_pdf --default` (PDF→PNG via pdftoppm). Prompts: [`prompts/tarief-extractie-v1.md`](prompts/tarief-extractie-v1.md) + [`prompts/tarief-verify-v1.md`](prompts/tarief-verify-v1.md). Bron: `resources/raw/wetteksten/Cijfers-Tarieven-2026.pdf` (196 p.). ADR-026. |
| **Aangifte-walkthrough bron schrijven** (PB-vakken, VenB) | Vision-handcrafted-extract met **twee bron-PDFs** (voorbereiding + toelichting). Prompt: `prompts/aangifte-handcrafted-v1.md`. ADR-028. Stijl-canonical: `resources/bronnen/wetteksten/aangifte-PB-2025-bezoldigingen.md`. |
| EXTRACT v4 — legacy schema 1.6-flow | `prompts/concept-extractie-v4.md` *(legacy — schema 2.1 v1.5 + operatie-prompts is canoniek)* |

---

## Absolute regels

Deze regels gelden bij elke sessie en elke agent:

1. **Geen wetsinhoud zonder bronverwijzing.** Onzeker? → `⚠️ te verifiëren`. Liever leeg dan onzeker.

2. **Confidence-labeling is verplicht.** ⚖️ = direct traceerbaar naar een bron (grounded). 🤖 = redenering of constructie (inferred). Elke claim krijgt een label; Claude mag niet weglaten bij twijfel.

3. **Geen Claude API in de build-pipeline.** LLM-werk tijdens build (concept-extractie, vermoedensruimte, seed-bouw, verdiep) gebeurt **lokaal via een Claude Code subagent** in dev-omgeving — niet via `anthropic.Anthropic()`-calls vanuit scripts. Helper-scripts in `tools/extractie/` doen alleen deterministisch werk (retrieval, embedding, JSON-IO). Keyword-generatie en herindexering: lokale tools (KeyBERT, YAKE, bge-m3). De **gedeployde tutor** draait wel op de Anthropic API — dat is een productie-eindpunt, geen build-stap.

4. **Raadpleeg de ADR-index vóór je begint** aan indexering, model-wijzigingen, bronnen toevoegen of concept-extractie. Zie taak→ADR mapping in [`docs/adr/INDEX.md`](docs/adr/INDEX.md).

5. **Alle beslissingen worden vastgelegd als ADR** — technisch én domein. Draft-status is OK; vastleggen is verplicht.

6. **Twee werkwijzen — weet welke actief is**:
   - **Design/sparring-modus**: we bespreken een beslissing samen. Het resultaat *moet* landen in een nieuw of bijgewerkt ADR vóór de uitvoering start.
   - **Werk-modus**: zelfstandige uitvoering (indexeren, fiches schrijven, bronnen verwerken, ...). Werkt altijd binnen de spelregels van de bestaande ADRs — geen nieuwe ontwerpkeuzes maken zonder terug te schakelen naar design-modus.

7. **Werkverdeling Opus ↔ Sonnet**:
   - **Opus** is de design-autoriteit: ADR-werk, sparring, plan-validatie, eindreview op grote diffs.
   - **Sonnet** voert de uitvoering uit binnen de spelregels van het ADR. Concreet werk (scripts schrijven, refactoren, conversie draaien, tests uitvoeren) wordt door Opus **gedelegeerd via de Agent-tool** zodra het plan duidelijk is. Opus blijft de gespreksmodus; Sonnet-agenten zijn werkpaarden.
   - Sonnet pingt terug naar Opus bij design-onduidelijkheid (bv. een edge-case die niet in het ADR staat). Sonnet maakt geen nieuwe ontwerpkeuzes zelfstandig.
   - In een Sonnet-sessie zonder design-werk geldt deze regel niet — daar werkt Sonnet rechtstreeks binnen het bestaande ADR.

8. **Geen afkortingen in code, docs en schema's.** Volledige namen overal: `programmaonderdeel` (niet `PO`), `kenniselement` (niet `TDK`), enzovoort. Geldt voor bestandsnamen, veldnamen, mapnamen, ADR-titels en commit-messages. In een gesprek met de gebruiker zijn afkortingen wél OK — daar gaat snelheid boven volledigheid.

9. **Geen leftovers — ongebruikte code en docs weg.** Scripts, modules, tests, frontmatter-velden, docstring-verwijzingen, sessie-handoffs en superseded ADRs die geen functie meer hebben gaan weg (`git rm`) of naar archive/, niet "voor later". One-off migratie- en backfill-scripts worden verwijderd zodra ze hun werk gedaan hebben. ADRs en docstrings die naar verwijderde code refereren worden in dezelfde commit bijgewerkt. Bij twijfel: kort vragen, anders weg.

---

## Technisch

### Mappenstructuur

```
certificaid/
├── CLAUDE.md                    # Deze wegwijzer + doc-discipline + 9 absolute regels
├── docs/
│   ├── TODO.md                  # Openstaand werk + fase-status (source-of-truth)
│   ├── adr/                     # Architecture Decision Records
│   │   ├── INDEX.md             # ADR-index + taak→ADR mapping
│   │   └── archive/             # Superseded ADRs + bevroren werkdocs
│   ├── schema-v15-besluit.md    # Canonieke spec schema 2.1 v1.5
│   ├── render-laag.md           # Werkpakket-spec render-laag (Fase 7)
│   ├── concept-schrijfregels.md       # Inhoudelijke conventies concept-records
│   ├── studiemateriaal-schrijfregels.md
│   ├── minicursus-schrijfregels.md    # ADR-036 — schrijfregels voor PO-niveau minicursus
│   ├── themafiche-schrijfregels.md    # ADR-036 — schrijfregels voor cluster-niveau themafiche
├── prompts/                     # Uitvoeringsinstructies voor agents (één canonieke versie per type)
│   ├── operaties/               # Schema 2.1 v1.5 operatie-prompts (extractie v6)
│   ├── concept-extractie-v4.md  # Legacy schema 1.6
│   ├── skeleton-voorstel-v1.md
│   ├── aangifte-handcrafted-v1.md
│   └── tarief-{extractie,verify}-v1.md
├── content/
│   ├── concepten/               # Concept-fiches (rendered uit schema 2.2-records)
│   ├── studiemateriaal/         # Per-PO leerpad (ADR-036/037/039/040/041): <po-slug>/{index.md=overzicht, <leerstuk>.md×N, samenvatting.md, oefening.md, voorbeeldexamenvragen.md}
│   ├── themafiches/             # Cluster-themafiches (legacy ADR-036; wordt vervangen door per-PO samenvatting per ADR-039)
│   ├── experiment/              # Schema-mockups + POC-themafiches (referentie)
│   ├── voorbeeldexamens/        # Cross-PO overzicht (index.md + nieuw.md). Per-PO pagina's leven in studiemateriaal/ (ADR-040).
│   └── bronnen/                 # Primaire bronnen als site-content (eventueel met leeshulp, ADR-034)
├── resources/
│   ├── bronnen/                 # Doorzoekbare bronbestanden (wetteksten/, normen/, adviezen/)
│   └── source_config.yaml       # Enige bron-van-waarheid voor alle bronnen
├── tools/
│   ├── download/                # Bron ophalen
│   ├── etl/                     # PDF/HTML → markdown + reprocessing
│   ├── rag/                     # ChromaDB-index bouwen + bevragen
│   ├── extractie/               # Concept-extractie (incl. embedding_daemon, MCP-server)
│   ├── tarieven/                # Tarief-extractie (MCP-server + chunk_pdf)
│   ├── leermateriaal/           # Render-tooling (legacy schema 2.0; revisie in Fase 7)
│   ├── examen/                  # Examenpatronen + question review
│   ├── export/                  # Externe exports (NotebookLM)
│   └── lib/                     # Gedeelde bibliotheken (records_api, tarieven_api, retrieval)
├── tutor/app.py                 # Streamlit tutor
├── data/
│   ├── bronnen-index.json       # Bronnen-index (top-level, auto-gegenereerd)
│   ├── programma/               # Examenprogramma-input (programma.json + anchors.json + examen_vragen/)
│   ├── concepten/
│   │   ├── records/             # Schema 2.2 records (359 stuks — zie ADR-035)
│   │   ├── schema-2.1.schema.json
│   │   ├── schema-2.2.schema.json
│   │   └── _archive/            # Pre-2.1 records (gitignored) + gearchiveerde leerpad-YAML's (ADR-036)
│   ├── tarieven/                # Tarief-records (Cijferzakboekje, ADR-026)
│   ├── etl/qa/                  # QA-rapporten (gitignored)
│   ├── rag/                     # ChromaDB-instance (gitignored, herbouwbaar)
│   └── extractie/               # Werkfolder extractie-pipeline
└── .github/workflows/deploy.yml
```

### Publicatie

- Site: https://stivni.github.io/certificaid
- Lokaal testen: `npm install && npm run dev` → http://localhost:8080
- Deploy triggert automatisch bij wijzigingen in `content/`, `quartz.config.ts` of `quartz.layout.ts`

### Quartz

Bij wijzigingen aan Quartz layout of styling:
1. Controleer https://quartz.jzhao.xyz/layout voor beschikbare componenten
2. Controleer `quartz/components/` voor de precieze API
3. Pas daarna `quartz.layout.ts` of `quartz/styles/custom.scss` aan
