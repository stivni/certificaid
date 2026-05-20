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
| [ADR-024](ADR-024-visuele-llm-interpretatie-examenvragen.md) | Visuele LLM-interpretatie van examenvragen via per-vraag artefacten | Draft |
| [ADR-025](ADR-025-schema-20-didactische-conceptlaag.md) | Schema 2.0 — didactische concept-laag (rol × perspectief · element-vocabulaire · kader/familie kinds) | Draft |

## Roadmap

[`docs/roadmap.md`](../roadmap.md) — fasering, DoD per fase, POC-strategie. Werkdocument, geen ADR.

## Taak → relevante ADRs

| Taak | Relevante ADRs |
|---|---|
| Bron toevoegen of herconverteren | ADR-005 (ETL), ADR-004 (provenance bij output), ADR-003 (reprocessing) |
| Bron als trusted markeren / kwaliteits-gate doorlopen | ADR-005 §7 (Laag 1 + Laag 2 + mens-override + snapshot-vangnet), ADR-004 (`provenance.trust` schema) |
| RAG-index + anchor-bundles synchroon houden na trust-mutatie | ADR-005 §9 (refresh-gate) — `tools/etl/mark_trusted.py --refresh` of `tools/etl/refresh_rag_and_matches.py` |
| Anchor-bundles selectief bijwerken (delta-driven matching) | ADR-005 §9.1 — `data/extractie/matches.sqlite3` + state-fingerprints |
| ETL-pipeline aanpassen (extractor of transformer) | ADR-005 §3 (extractors), §4 (transformers), §1 (determinisme) — vergeet snapshot-vangnet niet (`tests/test_pipeline_snapshots*.py`) |
| RAG-index bouwen of bevragen | ADR-006 (RAG-strategie) |
| Concept-record maken of aanvullen | ADR-007 (model, schema 1.1) **→ ADR-025 voor schema 2.0**, ADR-008 (extractie), ADR-002 (kenniselement-koppeling), ADR-010 (confidence-labeling), ADR-018 (embedding-daemon voor live duplicate-check), ADR-019 (records-API als enige schrijfweg) |
| Schema 2.0 concept-record (rol × perspectief, kader/familie) | ADR-025 + `prompts/concept-extractie-v5.md` + `prompts/concept-verify-v3.md` |
| Fase 2 herextract-pilot starten | `docs/pilot-fase2-pipeline.md` (werkdoc) + ADR-025 §migratie |
| Concept-record hernoemen of verwijderen | ADR-019 (`rename_record` / `delete_record` — geen directe disk-ops) |
| Embedding-daemon starten/stoppen/diagnose | ADR-018 |
| Concept-record opslaan, hernoemen of verwijderen (disk + RAG) | ADR-019 (records-API) |
| RAG-parity controleren of herstellen | ADR-019 — `python3 -m tools.lib.records_api audit [--fix]` |
| Examenvraag analyseren of genereren | ADR-009 (patronen), ADR-008 (extractie wanneer nieuw concept blijkt nodig) |
| Modelantwoord schrijven voor echte voorbeeldexamenvraag | ADR-024 (per-vraag artefact-pipeline, supersedes ADR-020 voor nieuwe vragen), ADR-009 §6 (render), ADR-008 (gap-niveau c → extractie) |
| OCR-vraagtekst normaliseren voor `data/programma/examen_vragen/` | ADR-024 (visuele agent-pass vervangt OCR-normalisatie); ADR-020 §6 voor legacy-flow |
| Examenvragen re-extracten (legacy v3 regex-pipeline) | ADR-021 (schema + werkwijze), `tools/examen/extract_vragen_v3.py` — vervalt na uitrol ADR-024 |
| Examenvraag isoleren + interpreteren + modelantwoord (nieuw) | ADR-024 — `_segmenten/` → `_interpretaties/` → `_antwoorden/` → merger |
| Leermateriaal-snapshot publiceren | ADR-010 (snapshots), ADR-002 (kenniselement-dekkingscheck) |
| Tutor-antwoord debuggen | ADR-010 (tutor live), ADR-006 (RAG), ADR-007 (graph-walks) |
| Iets reprocessen na bron-wijziging | ADR-003 (workflow), ADR-004 (provenance / stale-cascade) |

## Wanneer een nieuw ADR aanmaken?

Een ADR voor een beslissing die:
- niet triviaal omkeerbaar is (model wisselen, schema veranderen, laag toevoegen)
- andere onderdelen beïnvloedt (chunk-strategie raakt retrieval én generatie)
- in de toekomst niet meer duidelijk zou zijn waarom de keuze zo gemaakt is

**Geen** ADR voor: implementatiedetails, variabelenamen, kleine refactors, foutoplossingen. Die leven in code, in commit-berichten, of in `docs/`-werkdocumenten.

**Naamgeving**: `ADR-NNN-korte-slug.md`. Verhoog NNN sequentieel; gearchiveerde ADR-nummers worden niet hergebruikt.
