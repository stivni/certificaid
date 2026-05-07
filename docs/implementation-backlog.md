# Implementation Backlog

Werkdocument — geen ADR. Lijst van implementatie-werk dat volgt uit de design-ronde van 2026-05-08 (ADRs 002, 004, 006, 007, 008 bijgewerkt). Wordt afgevinkt naarmate code volgt.

## Fase 2 (Bronnen-RAG) — refactor naar unified `bronnen` collection

Driver: ADR-006 §3 herzien — twee collections (`bronnen` + `concepten`) ipv vier.

- [ ] `tools/rag/rag_index.py`
  - Schrijf alle wetteksten/normen/adviezen naar collection `bronnen` met `bron_rol`-metadata (`wettekst` / `norm` / `advies`)
  - Chunk-strategie blijft per brontype (artikel / sectie / heel-advies)
  - `index_*`-functies bouwen ids/texts/metadatas, één gedeelde upsert naar `bronnen`
  - Chunk-id-stabiliteit (ADR-006 §3.1, ADR-004): wettekst `<bron-stem>__art_<nr>`, norm `<bron-stem>__sec_<slug>`, advies (één-chunk) `<bron-stem>`
  - Per chunk: `chunk_sha` opslaan in metadata voor incremental rebuild (sha-vergelijking → skip/upsert/delete)
  - `--scope` blijft als POC-versnelling (file-filter + aparte chroma_db_<onderdeel>/)
  - Drop `--add-concepts` van deze tool; concept-indexering hoort in `tools/extractie/`

- [ ] `tools/lib/retrieval.py`
  - `ALL_COLLECTIONS = ["bronnen", "concepten"]` (was 6)
  - `_retrieve_candidates()`: één query op `bronnen` + optionele `where={"bron_rol": ...}` filter
  - `multi_query_retrieve()` blijft, alleen op één collection
  - Verwijder `tdks` en `bestaande_fiches` referenties (legacy)
  - Context-uitbreiding voor wetteksten blijft, op chunk_index of artikel-nr based

- [ ] `tools/rag/rag_query.py`
  - CLI-flag `--bron-rol wettekst,norm` ipv `--collections wetteksten,normen`
  - Default = alle bron-rollen

- [ ] `tutor/app.py`
  - Sidebar-filter: bron-rol checkboxes ipv collection-checkboxes
  - Citatie-rendering blijft via `path`-metadata

- [ ] **Eerst implementeren tegen huidige (3-collection) 4.0-POC-index**, dan testen of unified retrieval-API werkt door alle drie de bestaande collections te queryen alsof ze één waren. Pas daarna full rebuild naar één `bronnen`-collection.

## Fase 3 (Concept-extractie) — nieuw

Driver: ADR-007 + ADR-008 herzien.

- [ ] `tools/extractie/concept_extractor.py` — nieuwe orchestrator met sub-commands:
  - `vermoedensruimte` — taakblok + kenniselementen → 10–30 vermoedens (LLM, geen retrieval)
  - `seed` — vermoeden + multi-level retrieval → seed-record (LLM-synthese)
  - `verdiep` — seed/partieel-record → uitgebreide velden (LLM, met cumulatieve concept-state als query-input)
  - Per-veld provenance-blok bij elke schrijfactie
- [ ] `tools/extractie/queue.py` — dangling-edges → seed-queue
- [ ] `tools/lib/coverage.py` — bouwt op aanvraag een reverse-index (concept → kenniselementen) uit programmaonderdeel-JSON's voor dekkingsrapporten. Geen sync-script of cache op concepten zelf (ADR-002, ADR-007).
- [ ] `tools/extractie/index_concepts.py` — bouwt `concepten` ChromaDB-collection (was `index_concepts()` in `rag_index.py`)
- [ ] Prompt-templates in `prompts/` — geversioneerd, geladen met `prompt_version` in provenance
- [ ] Concept-schrijfregels (`docs/concept-schrijfregels.md`) inladen bij elke prompt-bouw
- [ ] Open-types-review-queue: `data/concept_records/_voorgestelde_types.yaml`

## Fase 0 / cross-cutting — provenance uitbreiden

Driver: ADR-004 herzien.

- [ ] `tools/lib/provenance.py`
  - Per-veld provenance voor concept-records (sub-blokken per veld)
  - `mark_stale.py`: walk per-veld bij chunk-update; markeer alleen velden waarvan input-chunk veranderd is
  - Chunk-sha-store: bij re-index, vergelijk nieuwe chunk-sha tegen opgeslagen waarde

## Stage 5 (later) — examen-driven extractie

Niet nu. Pas wanneer:
- Fase 3 een werkende basis-conceptenset oplevert voor minstens één programmaonderdeel
- Voorbeeldexamens gestructureerd zijn (vraag, oplossing, vereiste kennis)
- Examenpatronen-laag (ADR-009) operationeel is

Werk dan: validator-script ("kunnen voorbeeldvragen worden opgelost met huidige concepten?") + gerichte uitbreiding bij gaps.

## Open vragen / onderzoek

- **Device auto-detect** (MPS / CUDA / CPU): benchmark gaf 1.78× speedup op MPS. Geen blockers bij gebruik. Voeg toe aan `rag_index.py` + `retrieval.py`:
  ```python
  def detect_device():
      if torch.backends.mps.is_available(): return "mps"
      if torch.cuda.is_available(): return "cuda"
      return "cpu"
  ```
  Gebruik in `SentenceTransformer(model, device=detect_device())`. Override-flag `--device` voor CI / benchmarking. Klein werk (~10 regels totaal).
- **Online build-pipeline**: Modal / HF-IE / RunPod als cost-effective re-index-target bij bron-update. Pas onderzoeken na Fase 1 stabiel + chunk-id-stabiliteit gevalideerd.
- **Update-only herindexering**: vereist chunk-id-stabiliteit (ADR-004) + per-chunk sha-store. Validatie: kunnen we een gewijzigde Antiwitwaswet snel re-indexen zonder de volledige corpus te herbouwen?
