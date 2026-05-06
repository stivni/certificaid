# ADR-005: Query-strategie — concept-extractie vs. tutor

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Twee fundamenteel verschillende use cases stellen verschillende eisen aan retrieval:

- **Concept-extractie** (batch, offline): uitputtend — alle relevante bronnen moeten gevonden worden zodat Claude een volledig en correct concept record kan genereren
- **Tutor** (real-time, interactief): gefocust — de student wacht op een antwoord; 3–10 relevante passages volstaan

Een gedeelde `retrieve()`-functie met één vaste top-N dient beide slecht.

## Beslissing

### Concept-extractie (`tools/extractie/concept_extractor.py`)

```
Per concept: 5 gerichte sub-queries
  1. "{concept} definitie toepassingsgebied"        → alle collections
  2. "{concept} uitzondering tenzij behalve"         → wetteksten + normen
  3. "{concept} procedure stappen termijn verplichting" → wetteksten + normen
  4. "{concept} sanctie gevolg niet-naleving"        → wetteksten
  5. "{concept} voorbeeld praktijk"                  → adviezen + praktijkgidsen

Per sub-query: bi-encoder top-80 → reranker → drempel ≥ 0,50 → max 60 chunks
Context-uitbreiding: ja (±2 artikelen voor wetteksten, volledig advies voor CBN)
Deduplicatie: op chunk_id vóór doorsturen naar Claude
```

### Tutor (`tutor/app.py`)

```
Pass 1: query concepts-collection
  → bi-encoder top-10 → reranker → drempel ≥ 0,65
  → gevonden: stuur concept record naar Claude
  → niet gevonden: ga naar Pass 2

Pass 2: query wetteksten + normen + adviezen
  → bi-encoder top-30 → reranker → drempel ≥ 0,60 → max 10 chunks
  → context-uitbreiding: ja (begrensd, zie ADR-002)
  → fallback als < 3 resultaten boven drempel: top-5 zonder drempel

Optioneel: PO-filter als hint (niet blokkerend) via tags-metadata
```

### Gedeelde bibliotheek

Beide use cases gebruiken `tools/lib/retrieval.py`:
```python
retrieve_and_rerank(
    query: str,
    collections: list[str],
    client, ef, reranker,
    bi_top_n: int = 50,
    rerank_threshold: float = 0.60,
    max_results: int = 20,
    expand_context: bool = True,
) → list[RetrievalResult]
```

## Gevolgen

- `tools/lib/retrieval.py`: nieuwe gedeelde module
- `concept_extractor.py`: 5 sub-queries, hoge recall-instellingen
- `tutor/app.py`: twee-pass flow, lage latency-instellingen
- De tutor is primarily concept-gedreven; de bronnenlaag is een fallback en verificatielaag
