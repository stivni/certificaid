# Architecture Decision Records — Index

Alle architectuurbeslissingen voor het Certificaid-project.

**Status-definities:**
- `Proposed` — idee, nog niet geïmplementeerd
- `Draft` — geïmplementeerd maar nog bijstuurbaar; kleine optimalisaties zijn welkom zonder procedure
- `Accepted` — vastgelegd na expliciete validatie; wijzigen vereist een nieuw ADR
- `Superseded` — vervangen door een later ADR (oud ADR blijft leesbaar)

---

## Overzicht

| ADR | Onderwerp | Status | Domein | Keywords |
|---|---|---|---|---|
| [ADR-001](ADR-001-embedding-model.md) | Embedding model: BAAI/bge-m3 | Draft | RAG | bge-m3, embedding, multilingual, Nederlands, 8192 tokens |
| [ADR-002](ADR-002-chunk-strategie.md) | Chunk-strategie: small-to-big, begrensd context-venster | Draft | RAG | chunking, artikel, context-uitbreiding, prev/next, adviezen |
| [ADR-003](ADR-003-reranking.md) | Twee-fase retrieval: bi-encoder + cross-encoder reranker | Draft | RAG | reranker, bge-reranker, cross-encoder, score-drempel, tipover |
| [ADR-004](ADR-004-chunk-keywords.md) | Chunk-level semantische keywords voor wetteksten | Draft | RAG | keywords, KeyBERT, bge-m3, lokaal, wetteksten, embeddingenrichment |
| [ADR-005](ADR-005-query-strategie.md) | Query-strategie: concept-extractie vs. tutor | Draft | RAG | sub-queries, recall, precision, twee-pass, concepts-collection |
| [ADR-006](ADR-006-drie-lagenmodel.md) | Drie-lagenmodel: materie / competentie / synthese | Draft | Content | materie, competentie, synthese, canonieke-thuisplaats, concept, fenomeen |
| [ADR-007](ADR-007-confidence-labeling.md) | Confidence-labeling: grounded (⚖️) vs. inferred (🤖) | Draft | Content | grounded, inferred, bronvermelding, AI-labeling, ⚖️, 🤖 |
| [ADR-008](ADR-008-bron-rol.md) | bron_rol classificatiesysteem (5 niveaus) | Draft | Bronnen | bron_rol, itaa_lex, normatief, interpretatief, praktijkgids, formulier |
| [ADR-009](ADR-009-concept-record-schema.md) | Concept record JSON-schema | Draft | Conceptlaag | concept-record, JSON, schema, exceptions, main_rule, confidence, po_ref |
| [ADR-010](ADR-010-vector-database.md) | ChromaDB als vector-database | Draft | Infrastructuur | ChromaDB, vectorstore, persistent, lokaal, UUID-bug |
| [ADR-011](ADR-011-tutor-interface.md) | Streamlit als tutor-interface | Draft | Infrastructuur | Streamlit, tutor, lokaal, cache, chat |
| [ADR-012](ADR-012-model-keuze.md) | Model-keuze: Sonnet voor generatie, lokaal voor bulk | Draft | Infrastructuur | claude-sonnet-4-6, KeyBERT, YAKE, lokaal, geen-API-bulk |
| [ADR-013](ADR-013-site-generator.md) | Quartz als static site generator | Draft | Infrastructuur | Quartz, Obsidian, wikilinks, static, GitHub-Pages, ankers |
| [ADR-014](ADR-014-bron-etl-pipeline.md) | Bron ETL-pipeline: wetteksten, adviezen, normen | Draft | Bronnen | ETL, ejustice, pdftotext, cleanup, web-scrape, source_config, artikel-headings |
| [ADR-015](ADR-015-tools-organisatie.md) | Tools-map georganiseerd per pipeline-fase | Draft | Infrastructuur | tools/, submappen, download, etl, rag, extractie, examen, refactor |

---

## Taak → relevante ADRs

Raadpleeg deze mapping vóór je aan een taak begint.

| Taak | Relevante ADRs |
|---|---|
| **Bron toevoegen of herconverteren** | ADR-014 (ETL-pipeline), ADR-008 (bron_rol), ADR-004 (keywords) |
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

## ADR-bevestigingsronde (TODO)

Alle ADRs staan op `Draft`. Ze worden iteratief overlopen en bevestigd of bijgestuurd.
Ik breng elk ADR op bij het begin van de eerste taak waarvoor het relevant is.

| ADR | Nog te bespreken? | Opmerking |
|---|---|---|
| ADR-001 (bge-m3) | ✅ Besproken | Keuze duidelijk; index nog niet herbouwd |
| ADR-002 (chunk-strategie) | ✅ Besproken | prev/next gecodeerd, nog niet getest |
| ADR-003 (reranking) | ✅ Besproken | bge-reranker gekozen; nog niet gedraaid |
| ADR-004 (keywords) | ✅ Besproken | KeyBERT i.p.v. Claude; nog niet uitgevoerd |
| ADR-005 (query-strategie) | ✅ Besproken | twee-pass flow gecodeerd; nog niet getest |
| ADR-006 (drie-lagen) | ✅ Besproken | Fundamenteel akkoord; in CLAUDE.md verankerd |
| ADR-007 (confidence) | ✅ Besproken | ⚖️/🤖 systeem in gebruik |
| ADR-008 (bron_rol) | ✅ Besproken | 82 entries hebben bron_rol |
| ADR-009 (concept-schema) | ⏳ Te bespreken | Schema vastgelegd maar nog niet getest op schaal |
| ADR-010 (ChromaDB) | ⏳ Te bespreken | UUID-bug gefixt in code; rebuild nog nodig |
| ADR-011 (Streamlit) | ⏳ Te bespreken | Tutor gebouwd; deployment nog open |
| ADR-012 (model-keuze) | ✅ Besproken | KeyBERT voor bulk; Sonnet voor generatie |
| ADR-013 (Quartz) | ✅ Besproken | Deploy werkt; anker-conventies in content-richtlijnen |
| ADR-014 (ETL-pipeline) | ✅ Besproken | Fixes in cleanup.py gedaan; 10 bronnen opgeschoond |
| ADR-015 (tools-organisatie) | ⏳ Te bespreken | Refactor uitgevoerd; documentatie + paden bijgewerkt |

---

## Wanneer een nieuw ADR aanmaken?

Maak een ADR als je een beslissing neemt die:
- **Niet triviaal omkeerbaar** is (model wisselen, schema veranderen, tool vervangen)
- **Andere onderdelen beïnvloedt** (chunk-strategie beïnvloedt retrieval én generatie)
- **In de toekomst niet meer duidelijk** zal zijn waarom de keuze zo gemaakt is

Maak **geen** ADR voor: implementatiedetails, variabelenamen, kleine refactors, foutoplossingen.

**Naamgeving**: `ADR-NNN-korte-slug.md` in `docs/adr/`. Verhoog NNN sequentieel.
