# ADR-003: Twee-fase retrieval — bi-encoder + cross-encoder reranker

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Een bi-encoder vergelijkt query en document als **onafhankelijke vectoren** — snel maar onnauwkeurig. Bij juridische tekst mist dit subtiele relevantie: `"meldingsplicht"` en `"verplichte aangifte bij de CFI"` beschrijven hetzelfde maar hun embeddings liggen semantisch ver uiteen.

Een vaste top-N (bv. 5 chunks) is arbitrair: voor sommige vragen zijn 2 chunks genoeg, voor andere zijn er 30 relevant. Een drempel op de score van de bi-encoder helpt niet veel omdat de absolute scores afhangen van het model en de documenten.

## Beslissing

**Twee-fase pipeline:**

```
Fase 1 — bi-encoder (bge-m3)
  → Snel, parallel over alle collections
  → Retrieval top-50 kandidaten
  → Doel: hoge recall (niets missen)

Fase 2 — cross-encoder reranker (BAAI/bge-reranker-v2-m3)
  → Langzamer: scoort elke kandidaat opnieuw samen met de query
  → Output: score 0–1 per kandidaat
  → Drempel: alles ≥ 0,60 mee; cutoff bij max 20 chunks
  → Doel: hoge precision (tipover-punt vinden)
```

**`bge-reranker-v2-m3`** is specifiek de companion-reranker voor `bge-m3`, samen getraind op hetzelfde corpus.

### Drempelwaarden per use case

| Use case | Bi-encoder top-N | Reranker drempel | Max chunks |
|---|---|---|---|
| Concept-extractie | 80 | ≥ 0,50 | 60 |
| Tutor (interactief) | 30 | ≥ 0,60 | 10 |
| Tutor (fallback) | 10 | geen | 5 |

Concept-extractie heeft bewust een lagere drempel en hogere max: recall primeert boven precision.

## Gevolgen

- Extra modeldownload: `bge-reranker-v2-m3` (~570MB)
- Latency tutor: fase 2 voegt ~200–500ms toe (acceptabel voor interactief gebruik)
- Latency concept-extractie: irrelevant (batch)
- Implementatie: `tools/lib/retrieval.py` — gedeelde `retrieve_and_rerank()` functie voor tutor én concept_extractor
