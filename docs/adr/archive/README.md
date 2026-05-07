# Gearchiveerde ADRs

Op 2026-05-07 is de ADR-set herzien en geherstructureerd. De ADRs in deze map zijn de oorspronkelijke set zoals ze stonden vóór de herziening — ze worden **niet** meer als geldend beschouwd, maar blijven leesbaar als referentie voor:

- de oorspronkelijke redenering achter een keuze (waarom bge-m3? waarom block-level edges? waarom mark_appendices?)
- gedetailleerde implementatie-notities die niet in de nieuwe (kortere) ADRs zijn opgenomen
- historische context bij commit-berichten van vóór 2026-05-07

De nieuwe set staat in [`../INDEX.md`](../INDEX.md) en is *strategisch* van opzet (problem / decision / consequences in één pagina). Implementatie-detail leeft in code, in [`docs/`](../..) en hier in de archive.

## Mapping (oud → nieuw)

| Oud ADR | Nieuwe ADR(s) waar de beslissing in landt |
|---|---|
| ADR-001 (bge-m3) | ADR-006 (RAG-strategie) |
| ADR-002 (chunk-strategie) | ADR-006 (RAG-strategie) |
| ADR-003 (reranking) | ADR-006 (RAG-strategie) |
| ADR-004 (chunk-keywords) | ADR-006 (open vraag — keyword-enrichment hervalueren) |
| ADR-005 (query-strategie) | ADR-006 (RAG-strategie) — implementatie-detail, geen aparte ADR meer |
| ADR-006 (drie-lagenmodel) | ADR-001 (lagen-architectuur), ADR-007 (conceptmodel), ADR-010 (leermateriaal & tutor) |
| ADR-007 (confidence-labeling) | ADR-010 (leermateriaal & tutor) — confidence als output-conventie |
| ADR-008 (bron_rol) | ADR-005 (bronnen-ETL) — bron_rol als classificatie binnen ETL |
| ADR-009 (concept-record-schema v2) | ADR-007 (conceptmodel) |
| ADR-010 (ChromaDB) | ADR-006 (RAG-strategie) |
| ADR-011 (Streamlit) | ADR-010 (leermateriaal & tutor) |
| ADR-012 (model-keuze) | ADR-006 (model-keuze inline); ADR-005 (agent-QA model-keuze inline) |
| ADR-013 (Quartz) | ADR-010 (leermateriaal & tutor) |
| ADR-014 (bron-etl-pipeline) | ADR-005 (bronnen-ETL) |
| ADR-015 (tools-organisatie) | geen — implementatie-detail, leeft in `tools/` zelf |

## Wat *niet* in de archive zit

Twee onderwerpen zijn nieuw en hadden geen voorganger in de oude set:

- **ADR-002 (TDK als scoping-anker)** — externe scope-definitie was er nog niet expliciet
- **ADR-003 (Reprocessing & evaluatie) + ADR-004 (Provenance & versionering)** — fundament voor iteratief werken, eerder impliciet
- **ADR-009 (Examenpatronen)** — bestond als ontwerp in `docs/examenpatronen-ontwerp.md` en in memory, nu verheven tot ADR
