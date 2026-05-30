# Architecture Decision Records — Index

Architectuurbeslissingen voor het Certificaid-project. Deze set is herzien op 2026-05-07; de oude set is gearchiveerd in [`archive/`](archive/) en blijft leesbaar als referentie.

**Status-definities:**
- `Draft` — vastgelegd richting; details kunnen nog evolueren zonder nieuw ADR
- `Accepted` — vastgelegd na expliciete validatie; wijzigen vereist nieuw ADR
- `Superseded` — vervangen door later ADR (oud blijft leesbaar)

---

## Leesvolgorde

De ADRs zijn ontworpen om in nummervolgorde leesbaar te zijn: cross-cutting concerns vooraan (lagen-architectuur, scoping, reprocessing, provenance), daarna per laag van ruwste input naar uiteindelijk product.

| ADR | Onderwerp | Status |
|---|---|---|
| [ADR-001](ADR-001-lagen-architectuur.md) | Lagen-architectuur (kapstok) | Draft |
| [ADR-002](ADR-002-examenprogramma-scoping.md) | Examenprogramma als scoping-anker | Draft |
| [ADR-003](ADR-003-reprocessing-evaluatie.md) | Reprocessing & evaluatie | Draft |
| [ADR-004](ADR-004-provenance.md) | Provenance & versionering | Draft |
| [ADR-005](ADR-005-bronnen-etl.md) | Bronnen-ETL | Draft |
| [ADR-006](ADR-006-rag-strategie.md) | RAG-strategie (bronnen + concepten) | Draft |
| [ADR-007](ADR-007-conceptmodel.md) | Conceptmodel | Draft |
| [ADR-008](ADR-008-concept-extractie.md) | Concept-extractie via bron-first matching | Accepted |
| [ADR-009](ADR-009-examenpatronen.md) | Examenpatronen (parallelle observatielaag) | Draft |
| [ADR-010](ADR-010-leermateriaal-tutor.md) | Leermateriaal & tutor | Draft |
| [ADR-018](ADR-018-embedding-daemon.md) | Embedding-daemon voor concept-extractie | Draft |
| [ADR-019](ADR-019-records-api.md) | Centrale records-API + RAG-parity discipline | Draft |
| [ADR-020](ADR-020-modelantwoorden-voorbeeldexamens.md) | Modelantwoorden voor voorbeeldexamenvragen | Draft |
| [ADR-021](ADR-021-examenvragen-extractie-v2.md) | Examenvragen-extractie v2 + gestructureerde vraagtekst-blokken | Accepted |
| [ADR-022](ADR-022-vraag-herinterpretatie-draft.md) | Vraag-herinterpretatie (herinnering-stijl voorbeeldexamens) | Draft |
| [ADR-023](ADR-023-gestructureerde-antwoorden-en-vraag-v3.1.md) | Gestructureerde antwoorden (`correct_antwoord_blokken[]`) + vraag-cleanup v3.1 | Draft |
| [ADR-024](ADR-024-visuele-llm-interpretatie-examenvragen.md) | Visuele LLM-interpretatie van examenvragen via per-vraag artefacten | Accepted |
| [ADR-025](archive/ADR-025-schema-20-didactische-conceptlaag.md) | Schema 2.0 — didactische concept-laag (rol × perspectief · element-vocabulaire · kader/familie kinds) | Superseded — vervangen door ADR-029 |
| [ADR-026](ADR-026-tarief-extractie-pijplijn.md) | Tarief-extractie pijplijn (records-laag + Sonnet-subagent extract + MCP-server `certificaid-tarieven`) | Accepted |
| [ADR-027](ADR-027-bundle-aware-extract-architectuur.md) | Bundle-aware extract (2-pass) + daemon v2.0 (batching, gating, concurrent index) | Accepted — bundle-prompt verplaatst naar `prompts/operaties/` (zie ADR-029) |
| [ADR-029](ADR-029-schema-21-operaties-model.md) | Schema 2.1 (v1.5) — didactische conceptlaag + operations-model (`beschrijven`, `claims_checken`, `relaties_aanvullen`, `accountant_perspectief`, `didactisch_verrijken`, `kandidaat_review`, `leespad_aanvullen`) | Draft |
| [ADR-030](ADR-030-granulariteit-typologie.md) | Granulariteit-typologie voor concept-records — 4 super-categorieën + werkingsregels A-J (incl. Regel J geïntegreerde Regeling: één fenomeen × N dimensies = één record) + bundel-concept-patroon + `#anchor`-relaties. Vervangt 10 `concept_type`-waarden uit ADR-029. | Draft |
| [ADR-031](ADR-031-herinnering-pdf-vraag-isolatie-bbox-indent.md) | Vraag-isolatie voor herinnering-stijl examen-PDFs via woord-bbox-indent-detectie (top-letters x0 ≤ 80pt vs sub-stellingen op 90pt). Lost de "11 vakken i.p.v. 49 hoofdvragen"-fout in `parse_2024_1` op. ID-conventie `vr{vak}{letter}` (bv. vr7A). | Accepted |
| [ADR-032](ADR-032-examen-vragen-render-per-programmaonderdeel.md) | Voorbeeldexamenvragen renderen per programmaonderdeel (`po-1.1.md` t/m `po-4.0.md`) i.p.v. per bronbestand. Multi-PO vragen verschijnen in alle relevante pagina's. Per-examen pagina's vervallen. | Accepted |
| [ADR-033](ADR-033-scope-metadata-extractie-guidance.md) | `metadata.scope.in[]` + `metadata.scope.out[]` toegevoegd aan schema 2.1 v1.5 als optionele extractie-guidance (vrije strings, geen integriteit-check). Voorkomt scope-creep + content-duplicatie tussen verwante records tijdens extractie-operaties. Materialiseert per-record-afbakening uit granulariteit-skelet-cluster-sparring. | Draft |
| [ADR-034](ADR-034-bron-leeshulp-injectie.md) | Bron-leeshulp via injectie in publicatie-laag: `resources/bronnen/` (heilig) + `resources/leeshulp/` (didactische callouts) → `content/bronnen/` (gegenereerd). Houdt bron/commentaar gescheiden; leeshulp leeft náást Fase 7 concept-render (verschillende leesmodi). POC op `ITAA-norm-algemene-controlenorm`. | Draft |
| [ADR-035](ADR-035-schema-22-geldigheid-en-element-scope.md) | Schema 2.2: geldigheid in inhoud + element-scope + versioning-consolidatie. Vervangt schema-uitbreidingen uit ADR-029 + ADR-033. | Accepted |
| [ADR-036](ADR-036-drie-lagen-leermateriaal.md) | Drie-lagen leermateriaal: **concept-fiche** (per record) · **themafiche** (per cluster, "kapstok voor herhaling") · **minicursus** (per PO, "verhaal en routekaart"). Supersedeert Fase D (competenties-destillatie) + Fase E (leerpad-opstelling) uit ADR-008. | Draft |

## Roadmap

[`docs/TODO.md`](../TODO.md) — openstaand werk + fase-status + mindset-principes (incl. POC vertical-slice + "never done"-DoD). Werkdocument, geen ADR.

## Taak → relevante ADRs

| Taak | Relevante ADRs |
|---|---|
| Bron toevoegen of herconverteren | ADR-005 (ETL), ADR-004 (provenance bij output), ADR-003 (reprocessing) |
| Bron als trusted markeren / kwaliteits-gate doorlopen | ADR-005 §7 (Laag 1 + Laag 2 + mens-override + snapshot-vangnet), ADR-004 (`provenance.trust` schema) |
| RAG-index + anchor-bundles synchroon houden na trust-mutatie | ADR-005 §9 (refresh-gate) — `tools/etl/mark_trusted.py --refresh` of `tools/etl/refresh_rag_and_matches.py` |
| Anchor-bundles selectief bijwerken (delta-driven matching) | ADR-005 §9.1 — `data/extractie/matches.sqlite3` + state-fingerprints |
| ETL-pipeline aanpassen (extractor of transformer) | ADR-005 §3 (extractors), §4 (transformers), §1 (determinisme) — vergeet snapshot-vangnet niet (`tests/test_pipeline_snapshots*.py`) |
| RAG-index bouwen of bevragen | ADR-006 (RAG-strategie) |
| Concept-record maken of aanvullen | ADR-007 (model) → **ADR-029 voor schema 2.1 v1.5** (canoniek), ADR-008 (extractie), ADR-002 (kenniselement-koppeling), ADR-010 (confidence-labeling), ADR-018 (embedding-daemon voor live duplicate-check), ADR-019 (records-API als enige schrijfweg) |
| Schema 2.1 v1.5 concept-record (kern-wrapper, fractale elementen, valkuilen/speelruimtes/syntheses, accountant_perspectieven) | ADR-029 + `docs/schema-v15-besluit.md` (canonieke spec) + `data/concepten/schema-2.1.schema.json` + operatie-prompts in `prompts/operaties/` |
| Operatie toepassen op concept-record (`beschrijven`, `claims_checken`, `relaties_aanvullen`, `accountant_perspectief`, `didactisch_verrijken`, `kandidaat_review`, `leespad_aanvullen`) | ADR-029 §Operaties-model — `tools/extractie/multi_pass_extract.py operate --operatie <naam>` |
| Bundle-aware extract (2-pass — historisch v5; bundle-concepten leven door in operaties-pipeline) | ADR-027 (rationale + daemon v2.0) — `tools/extractie/build_context_bundle.py`, `tools/extractie/build_bundles_batch.py` |
| Daemon-throughput-tuning of restart | ADR-018 + ADR-027 — `tools/extractie/embedding_daemon.py` (v2.0 met batching/gating), config in `tools/extractie/daemon_config.yaml`, hot-reload `launchctl kickstart -k gui/$(id -u)/com.certificaid.embedding-daemon` |
| Concept-record hernoemen of verwijderen | ADR-019 (`rename_record` / `delete_record` — geen directe disk-ops) |
| Embedding-daemon starten/stoppen/diagnose | ADR-018 |
| Concept-record opslaan, hernoemen of verwijderen (disk + RAG) | ADR-019 (records-API) |
| RAG-parity controleren of herstellen | ADR-019 — `python3 -m tools.lib.records_api audit [--fix]` |
| Examenvraag analyseren of genereren | ADR-009 (patronen), ADR-008 (extractie wanneer nieuw concept blijkt nodig) |
| Modelantwoord schrijven voor echte voorbeeldexamenvraag | ADR-024 (per-vraag artefact-pipeline, supersedes ADR-020 voor nieuwe vragen), ADR-009 §6 (render), ADR-008 (gap-niveau c → extractie) |
| OCR-vraagtekst normaliseren voor `data/programma/examen_vragen/` | ADR-024 (visuele agent-pass vervangt OCR-normalisatie); ADR-020 §6 voor legacy-flow |
| Examenvragen re-extracten (legacy v3 regex-pipeline) | ADR-021 (schema + werkwijze), `tools/examen/extract_vragen_v3.py` — vervalt na uitrol ADR-024 |
| Examenvraag isoleren + interpreteren + modelantwoord (nieuw) | ADR-024 — `_segmenten/` → `_interpretaties/` → `_antwoorden/` → merger |
| Herinnering-PDF parser-fix (2024-1 vak-vragen) | ADR-031 — `parse_2024_1` via bbox-indent (x0 ≤ 80pt = top-letter) |
| Examen-vragen renderen (per programmaonderdeel) | ADR-032 — `tools/examen/render_merged_v4.py` → `content/voorbeeldexamens/po-<code>.md` (17 pagina's + index) |
| Interpretatie-schema bewerken of valideren | [`data/programma/examen_vragen/interpretatie-1.2.schema.json`](../../data/programma/examen_vragen/interpretatie-1.2.schema.json) (bron-van-waarheid, ADR-024 §3) + [`prompts/vraag-interpretatie-v1.md`](../../prompts/vraag-interpretatie-v1.md) + [`tests/test_interpretatie_schema.py`](../../tests/test_interpretatie_schema.py) |
| Leermateriaal-snapshot publiceren | ADR-010 (snapshots), ADR-002 (kenniselement-dekkingscheck) |
| **Minicursus** schrijven voor een PO (PO-niveau verhaal + routekaart) | ADR-036 + [`docs/minicursus-schrijfregels.md`](../minicursus-schrijfregels.md) + mockup [`content/leerpaden/1.4.md`](../../content/leerpaden/1.4.md) |
| **Themafiche** schrijven voor een cluster (kapstok-document voor herhaling) | ADR-036 + [`docs/themafiche-schrijfregels.md`](../themafiche-schrijfregels.md) + mockup [`content/experiment/synthese-consolidatie-v1.md`](../../content/experiment/synthese-consolidatie-v1.md) |
| Tutor-antwoord debuggen | ADR-010 (tutor live), ADR-006 (RAG), ADR-007 (graph-walks) |
| Iets reprocessen na bron-wijziging | ADR-003 (workflow), ADR-004 (provenance / stale-cascade) |
| Tarief- of drempel-record schrijven / trusten | ADR-026 — `tools/lib/tarieven_api.py` (`save_record`, `mark_trusted`, `audit_parity`, `render_all`) + schema `data/tarieven/schema.json` |
| Tarief-tabel uit PNG-bron extraheren | ADR-026 §Extract-flow — Sonnet-subagent met directe Read op `data/tarieven/_poc/pages/`; prompts `prompts/tarief-extractie-v1.md` + `prompts/tarief-verify-v1.md`. Chunker uitgesteld tot Cijferzakboekje 2027. |
| Tarief-records raadplegen vanuit een agent | ADR-026 §MCP-server — `certificaid-tarieven` (4 tools: `lijst_tabellen` · `lees_tabel` · `zoek_tabellen` · `query_tabel`) in `.mcp.json`. Text-match, geen embeddings. |

## Wanneer een nieuw ADR aanmaken?

Een ADR voor een beslissing die:
- niet triviaal omkeerbaar is (model wisselen, schema veranderen, laag toevoegen)
- andere onderdelen beïnvloedt (chunk-strategie raakt retrieval én generatie)
- in de toekomst niet meer duidelijk zou zijn waarom de keuze zo gemaakt is

**Geen** ADR voor: implementatiedetails, variabelenamen, kleine refactors, foutoplossingen. Die leven in code, in commit-berichten, of in `docs/`-werkdocumenten.

**Naamgeving**: `ADR-NNN-korte-slug.md`. Verhoog NNN sequentieel; gearchiveerde ADR-nummers worden niet hergebruikt.
