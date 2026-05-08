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

- [x] `tutor/app.py`
  - Sidebar-filter: bron-rol checkboxes ipv collection-checkboxes ✓
  - Sidebar-infopaneel: tellingen per bron_rol via `get(where=...)` ✓
  - CHROMA_PATH via `CERTIFICAID_CHROMA_PATH`-env-var (default = `chroma_db_4.0`) ✓
  - Dead `selected_cols`-param uit `retrieve_two_pass()` verwijderd ✓
  - Dubbele PO-query-prefix gecorrigeerd ✓
  - Citatie-rendering blijft via `label()` (`bron` + `artikel`/`sectie`/`veld`-metadata)

- [ ] **Eerst implementeren tegen huidige (3-collection) 4.0-POC-index**, dan testen of unified retrieval-API werkt door alle drie de bestaande collections te queryen alsof ze één waren. Pas daarna full rebuild naar één `bronnen`-collection.

## Fase 3 (Concept-extractie) — nieuw

Driver: ADR-007 + ADR-008 herzien (build-pipeline = geen externe API; LLM-werk via
Claude Code subagent in dev-omgeving).

**Modelkeuze**: extractie-subagent draait op **Claude Opus** (huidige versie: claude-opus-4-7).
Zie ADR-008 §0 voor argumentatie. Helper-scripts en code-onderhoud: Sonnet is fine.

- [x] `tools/extractie/concept_extractor.py` — **strippen** van alle `anthropic`-aanroepen.
  Behouden als deterministische helpers (laad vermoedens, build prompts, write records).
  Geen sub-command structuur meer — orkestratie loopt via subagent.
- [x] `tools/extractie/normalize_vermoedens.py` — leidt `kenniselementen: [code]` af uit
  `gekoppeld_aan` + taakblok-context van bestaande vermoedens. Inconsistente input
  ("Taak: ..." vs codes) wordt genormaliseerd. `kenniselementen: []` is geldig.
  Voegt ook lege `schaal_signaal`-placeholder toe als het veld ontbreekt.
  Alle 60 bestaande vermoedens (D1.1/D1.2/D1.3) genormaliseerd.
- [x] `tools/extractie/retrieve_batch.py` — leest een vermoedens-JSON, doet 4-niveau
  retrieval per vermoeden (programmaonderdeel + taakblok + kenniselementen + vermoeden),
  één bge-m3 model-load voor alle queries. Output: JSON naar stdout met chunks per vermoeden.
- [x] `tools/extractie/index_concept_incremental.py` — embed één concept-record en upsert
  in `concepten` ChromaDB-collection. Aangeroepen door subagent na elke nieuwe seed-write.
  Bevat ook `--duplicaat-check <naam>` voor live duplicate-check tijdens extractie.
- [ ] `tools/extractie/queue.py` — dangling-edges → seed-queue (later, bij iteratieve runs)
- [ ] `tools/lib/coverage.py` — bouwt op aanvraag een reverse-index (concept → kenniselementen) uit programmaonderdeel-JSON's voor dekkingsrapporten. Geen sync-script of cache op concepten zelf (ADR-002, ADR-007).
- [x] Prompt-templates in `prompts/` — versioneerd; subagent leest deze + `concept-schrijfregels.md`
  bij start van zijn run. Aanwezig: `vermoedensruimte-v1.md`, `seed-v1.md`,
  `verdiep-v1.md`, `extractie-runbook-v1.md` (orkestratie voor Opus-subagent).
- [ ] Open-types-review-queue: `data/concept_records/_voorgestelde_types.yaml` (auto-aangevuld)
- [ ] Beslissingslog: `data/extractie/<po>/seed_log_<taakblok>.json` (subagent schrijft
  kept/merged/rejected/split per vermoeden, met duplicate-check rerank-scores)

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

## ETL — chunking-kwaliteit (retrieval korte artikelen)

- [x] **Structuurheadings hersteld**: plain-text BOEK/TITEL/HOOFDSTUK/AFDELING-labels
  omgezet naar markdown-headings (`_herstel_structuurheadings()` in rag_index.py).
  138 labels in Strafwetboek-1867 waren plain text — nu zitten ze in de breadcrumb.
  Art. 458 SW: positie 59 → positie 6, score 0.06 → 0.16.
- [x] **Bis/ter/quater-merge**: `_merge_bis_ter()` voegt aaneengesloten artikelen
  met suffix samen in de chunk van het basisartikel (≤ MAX_CHUNK_CHARS).

## ETL — tweetalige normen (blocker voor goede retrieval)

Driver: bilingual ITAA-normen chunken slecht → grote gemengde NL+FR blobs → verwaterde embedding → lage bi-scores (~0.16–0.25) ook voor relevante passages.

- [ ] `tools/etl/` — fix voor tweetalige norm-bestanden:
  - Extraheer enkel de Nederlandse kolom vóór chunking
  - Normen als `ITAA-norm-intern-kwaliteitsmanagement.md` hebben NL+FR naast elkaar
    in één markdown-tabel of kolom-layout → split_generic maakt grote blobs
  - Na ETL-fix: incremental re-index via `--scope` + SHA-skip werkt automatisch
    (alleen gewijzigde chunks krijgen nieuwe SHA → nieuwe embedding)
  - Prioriteit: `ITAA-norm-intern-kwaliteitsmanagement.md` (onafhankelijkheid,
    beroepsgeheim uitwerking), daarna overige bilingual normen

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
