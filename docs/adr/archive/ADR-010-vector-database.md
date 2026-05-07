# ADR-010: ChromaDB als vector-database

**Status**: Draft  
**Datum**: 2026-05-06

## Context

De RAG-pipeline vereist een vector-database die embeddings opslaat en efficiënt doorzoekbaar maakt op cosine-similarity. De oplossing moet lokaal draaien (geen cloud-afhankelijkheid), gratis zijn, en eenvoudig te onderhouden.

## Beslissing

**ChromaDB** (`chromadb` Python-package, PersistentClient op `data/chroma_db/`).

Redenen:
- Volledig lokaal, geen API-sleutel of cloudservice nodig
- Native Python-integratie met sentence-transformers embedding functions
- Eenvoudige `upsert`/`query` API, goed gedocumenteerd
- Gratis en open-source (Apache 2.0)

Nadelen die we accepteren:
- Geen ingebouwde reranking — opgelost via ADR-003 (externe CrossEncoder)
- Rust-backend in recente versies heeft UUID-caching issues bij delete+recreate (workaround in `rag_index.py`: nieuwe client na delete)
- Geen multi-user of authenticatie (bewust: lokaal gebruik)

## Gevolgen

- `data/chroma_db/` is gegenereerde data — gitignored, lokaal herbouwbaar
- Bij schema-wijzigingen (nieuwe metadata-velden): volledige rebuild vereist
- Concurrent schrijven werkt niet betrouwbaar — index altijd sequentieel per collection bouwen
