# ADR-001: Embedding model — BAAI/bge-m3

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Het initieel gekozen model `all-MiniLM-L6-v2` is Engelstalig getraind en heeft een context window van slechts 256 tokens. Steekproeven toonden dat semantisch evidente queries volledig mislukten op Nederlandstalige juridische tekst:

- `"meldingsplicht cfI antiwitwaswet"` → retrieval gaf WBTW terug (score 0.398)
- `"btw opeisbaarheid factuur"` → retrieval gaf landbouwartikel terug (score 0.413)
- `"leasing boekhoudverwerking"` → werkte correct (score 0.792) omdat de terminologie toevallig ook in Engels courant is

## Beslissing

Gebruik **BAAI/bge-m3** als embedding model.

| Eigenschap | all-MiniLM-L6-v2 | BAAI/bge-m3 |
|---|---|---|
| Parameters | 22M | 560M |
| Context window | 256 tokens | 8.192 tokens |
| Talen | Engels | 100+ (incl. NL) |
| Kost | Gratis | Gratis (MIT) |
| Indexing snelheid | Snel | ~4× trager (eenmalig) |
| Query latency | ~15ms | < 30ms |

## Gevolgen

- Eenmalige herbouw van de volledige ChromaDB (~30–60 min)
- Grotere modeldownload (~570MB) bij eerste gebruik
- CBN-adviezen tot P90 (31K chars ≈ 6.250 tokens) passen nu in één chunk
- Query-kwaliteit verbetert fundamenteel voor Nederlandstalige juridische tekst
