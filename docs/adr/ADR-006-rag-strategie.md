# ADR-006: RAG-strategie

**Status**: Draft
**Datum**: 2026-05-07
**Vervangt**: archive/ADR-001 (embedding model), ADR-002 (chunk-strategie), ADR-003 (reranking), ADR-005 (query-strategie), ADR-010 (ChromaDB)

## Context

Twee RAG-collecties (bronnen + concepten) hebben dezelfde fundamentele eisen: Nederlandstalige juridische tekst, klein-tot-groot retrieval (precise embedding + voldoende context bij generatie), tipover-puntdetectie via reranking. Eén RAG-strategie volstaat voor beide collecties; alleen de chunking verschilt per artefact-type.

`all-MiniLM-L6-v2` faalde op Nederlandstalige juridische tekst (256-token context, Engelstalig getraind). Bge-m3 lost dat op. Verder: een vaste top-N produceert ofwel ruis (te veel) ofwel gemiste context (te weinig); een reranker-drempel is robuuster.

## Beslissing

### 1. Embedding-model: `BAAI/bge-m3`
Nederlandstalig getraind, 8192-token context, MIT, lokaal. Eenmalige indexbouw ~30–60 min.

### 2. Reranker: `BAAI/bge-reranker-v2-m3`
Companion van bge-m3. **Twee-fase pipeline**:
- Fase 1 (bi-encoder): top-50 kandidaten — recall-georiënteerd
- Fase 2 (cross-encoder): rescore → drempel ≥0,60 (tutor) of ≥0,50 (concept-extractie); cutoff bij 20 chunks

### 3. Vector-DB: ChromaDB
Persistent, lokaal in `data/chroma_db/`. Aparte collections: `wetteksten`, `adviezen`, `normen`, `concepts`.

### 4. Chunking — bronnen-RAG

| Brontype | Eenheid | Buurchunks |
|---|---|---|
| Wettekst | per artikel (`## Art. X` is gezagsbron) | ±2 artikelen |
| CBN-advies (≤40K chars) | per advies (één chunk) | geen |
| CBN-advies (>40K chars) | per `##`-sectie | geen |
| ITAA-norm | per `##`-sectie | ±1 |
| Praktijkgids | heading-fallback (`split_generic_headings`) | geen (TODO bron-specifiek) |

**Hard max chunk-grootte**: 24.000 chars (~6.000 tokens, bge-m3-marge). Boven die grens: split op alinea-grenzen, identieke `path` en breadcrumb, suffix `__partN` op `id`.

### 5. Chunking — concepten-RAG

Per node-veld een chunk. Edges meedragen als metadata zodat retrieval een sub-graph levert (zie ADR-007).

### 6. Breadcrumb-prefix in embedded tekst

Elke chunk krijgt een prefix-regel met **semantische namen** (geen kale markers):

```
[Antiwitwaswet 2017 → Onderworpen entiteiten → Specifieke analyse → Beoordelingsverplichting]

## Art. 46

In de gevallen bedoeld in...
```

Per brontype een eigen format (zie archive/ADR-002 voor volledige tabel). Marker-zonder-naam ("HOOFDSTUK II") is semantisch leeg voor bge-m3.

### 7. Gestructureerd `path` in metadata

Naast de breadcrumb-tekst: `path`-array als JSON-string in metadata. Drie consumenten:
1. Citatie-rendering in tutor zonder string-parsing
2. Filtering op deelhiërarchie
3. Concept-extractie (ADR-008)

### 8. Evaluatie

**Vragen-testset** met verwachte chunks (gegroeid uit voorbeeldexamens). Top-k recall is regressie-metriek. `tools/rag/eval.py` draait de testset, output is een rapport met per vraag: gevonden chunks, ontbrekende verwachte chunks, ruis.

## Gevolgen

- `tools/rag/rag_index.py` indexeert bronnen + concepten (collection-parameter)
- `tools/rag/rag_query.py` voor ad-hoc queries en eval
- `tools/lib/retrieval.py` — gedeelde `retrieve_and_rerank()` voor tutor en extractor
- Open vraag uit oude ADR-004: keyword-enrichment (KeyBERT op chunks). Draagt mogelijk bij aan recall, mogelijk overbodig met bge-m3. Hervalueer empirisch op vragen-testset; default = uit.
- Modeldownloads: bge-m3 (~570MB) + bge-reranker-v2-m3 (~570MB), eenmalig
