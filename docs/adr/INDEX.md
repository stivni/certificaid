# Architecture Decision Records — Index

Alle architectuurbeslissingen voor het Certificaid-project.

**Status-definities:**
- `Proposed` — idee, nog niet geïmplementeerd
- `Draft` — geïmplementeerd maar nog bijstuurbaar; kleine optimalisaties zijn welkom zonder procedure
- `Accepted` — vastgelegd na expliciete validatie; wijzigen vereist een nieuw ADR
- `Superseded` — vervangen door een later ADR (oud ADR blijft leesbaar)

---

## Overzicht

| ADR | Onderwerp | Status | Domein |
|---|---|---|---|
| [ADR-001](ADR-001-embedding-model.md) | Embedding model: BAAI/bge-m3 | Draft | RAG |
| [ADR-002](ADR-002-chunk-strategie.md) | Chunk-strategie: small-to-big, begrensd context-venster | Draft | RAG |
| [ADR-003](ADR-003-reranking.md) | Twee-fase retrieval: bi-encoder + cross-encoder reranker | Draft | RAG |
| [ADR-004](ADR-004-chunk-keywords.md) | Chunk-level semantische keywords voor wetteksten | Draft | RAG |
| [ADR-005](ADR-005-query-strategie.md) | Query-strategie: concept-extractie vs. tutor | Draft | RAG |
| [ADR-006](ADR-006-drie-lagenmodel.md) | Drie-lagenmodel: materie / competentie / synthese | Draft | Content |
| [ADR-007](ADR-007-confidence-labeling.md) | Confidence-labeling: grounded (⚖️) vs. inferred (🤖) | Draft | Content + RAG |
| [ADR-008](ADR-008-bron-rol.md) | bron_rol classificatiesysteem (5 niveaus) | Draft | Bronnen |
| [ADR-009](ADR-009-concept-record-schema.md) | Concept record JSON-schema | Draft | Conceptlaag |
| [ADR-010](ADR-010-vector-database.md) | ChromaDB als vector-database | Draft | Infrastructuur |
| [ADR-011](ADR-011-tutor-interface.md) | Streamlit als tutor-interface | Draft | Infrastructuur |
| [ADR-012](ADR-012-model-keuze.md) | Model-keuze: Sonnet voor generatie, lokaal voor bulk | Draft | Infrastructuur |
| [ADR-013](ADR-013-site-generator.md) | Quartz als static site generator | Draft | Infrastructuur |

---

## Taak → relevante ADRs

Raadpleeg deze mapping vóór je aan een taak begint.

| Taak | Relevante ADRs |
|---|---|
| **Bron toevoegen** (nieuw `.md` + source_config.yaml) | ADR-008 (bron_rol), ADR-004 (keywords genereren na toevoeging) |
| **RAG-index herbouwen** | ADR-001 (model), ADR-002 (chunk-strategie), ADR-004 (keywords), ADR-010 (ChromaDB) |
| **Queries testen / tutor draaien** | ADR-003 (reranking), ADR-005 (query-strategie), ADR-011 (Streamlit) |
| **Concept record genereren** | ADR-005 (query-strategie), ADR-007 (confidence), ADR-009 (schema) |
| **Materie-fiche schrijven** | ADR-006 (drie-lagen), ADR-007 (confidence-labeling) |
| **Competentie-fiche schrijven** | ADR-006 (drie-lagen, canonieke thuisplaats) |
| **PO-fiche bijwerken** | ADR-006 (drie-lagen, taak→competentie mapping) |
| **Keyword-generatie draaien** | ADR-004 (strategie), ADR-012 (lokaal model — geen Claude API) |
| **Model wisselen** | ADR-001 (embedding), ADR-003 (reranker companion), ADR-012 (generatiemodel) |
| **Site publiceren** | ADR-013 (Quartz, deploy-flow) |

---

## Wanneer een nieuw ADR aanmaken?

Maak een ADR als je een beslissing neemt die:
- **Niet trivial omkeerbaar** is (bv. model wisselen, schema veranderen, tool vervangen)
- **Andere onderdelen van het systeem beïnvloedt** (bv. een chunk-strategie beïnvloedt retrieval en generatie)
- **In de toekomst niet meer duidelijk** zal zijn waarom deze keuze gemaakt is

Maak **geen** ADR voor: implementatiedetails, variabelenamen, kleine refactors, foutoplossingen.

**Naamgeving**: `ADR-NNN-korte-slug.md` in `docs/adr/`. Verhoog NNN sequentieel.
