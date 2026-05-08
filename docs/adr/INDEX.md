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
| [ADR-008](ADR-008-concept-extractie.md) | Concept-extractie | Draft |
| [ADR-009](ADR-009-examenpatronen.md) | Examenpatronen (parallelle observatielaag) | Draft |
| [ADR-010](ADR-010-leermateriaal-tutor.md) | Leermateriaal & tutor | Draft |
| [ADR-018](ADR-018-embedding-daemon.md) | Embedding-daemon voor concept-extractie | Draft |

## Roadmap

[`docs/roadmap.md`](../roadmap.md) — fasering, DoD per fase, POC-strategie. Werkdocument, geen ADR.

## Taak → relevante ADRs

| Taak | Relevante ADRs |
|---|---|
| Bron toevoegen of herconverteren | ADR-005 (ETL), ADR-004 (provenance bij output), ADR-003 (reprocessing) |
| Bron als trusted markeren / kwaliteits-gate doorlopen | ADR-005 §5 (drie-laag QA + trust-marker), ADR-004 (`provenance.trust` schema) |
| RAG-index bouwen of bevragen | ADR-006 (RAG-strategie) |
| Concept-record maken of aanvullen | ADR-007 (model, schema 1.1), ADR-008 (extractie), ADR-002 (kenniselement-koppeling), ADR-010 (confidence-labeling), ADR-018 (embedding-daemon voor live duplicate-check) |
| Embedding-daemon starten/stoppen/diagnose | ADR-018 |
| Examenvraag analyseren of genereren | ADR-009 (patronen), ADR-008 (extractie wanneer nieuw concept blijkt nodig) |
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
