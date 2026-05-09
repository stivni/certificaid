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

## Fase 3 (Concept-extractie) — bron-first matching

Driver: ADR-008 (bron-first matching, accepted 2026-05-09). Vermoedensruimte-pipeline
verworpen na empirisch experiment op 2 PO's; zie ADR-008 §"Overwogen alternatief".

**Modelkeuze**: extractie-subagent draait op **Claude Opus** (huidige versie: claude-opus-4-7).
Zie ADR-008 §2 voor argumentatie. Helper-scripts en code-onderhoud: Sonnet is fine.

**Pipeline-status**:
- [x] Fase A: Anchor-verrijking — eenmalige LLM-call per PO via subagent met clean-prompt
  (geen wetsverwijzingen). Output: `data/extractie/<po>/anchors/<po>-anchors.json` (gegit).
  Twee PO's gedaan (4.0 Deontologie, 1.1 Algemene boekhouding).
- [x] Fase B: Bron-first matching — `tools/extractie/match_bronnen.py`. Deterministisch,
  `score >= max(floor=0.55, top1 - margin=0.15)`. Output: `data/extractie/<po>/matches/`.
- [x] Fase C: Per-anchor concept-extractie — Opus-subagent verwerkt anchors sequentieel.
  Bundle-export via `tools/extractie/export_bundle.py`.
  Eén anchor per PO is ge-test; volledige PO-runs nog te doen.
- [ ] Fase D: Verdieping per concept (status `partieel` → `gevuld`). Niet gestart.

**Open implementatie-eisen** (zie ADR-008 §"Open implementatie-eisen"):
- [ ] `tools/extractie/match_bronnen.py` moet `chunk_sha` uit ChromaDB-metadata
  kopiëren naar concept-record `_provenance.<veld>.inputs[].sha256` (nu `null`).
- [ ] `tools/etl/mark_stale.py` voor concepten bouwen (ADR-008 §10).
- [ ] `tools/etl/remove_bron.py` Laag 2 omzetten naar `data/concept_records/**/_provenance.*.inputs[].id`.
- [ ] Prompt-templates in `prompts/` voor concept-extractie (anchor-verrijking + per-anchor extractie).
  Huidige extractie liep met ad-hoc subagent-prompts; productie-prompts moeten nog vastgelegd worden.
- [ ] Programmaonderdeel-JSON tooling: nu handmatig geschreven (4.0, 1.1).
  Mechanische extractie uit `programma.pdf` zou helpen voor de overige PO's.

**Open ETL-revisies** (apart van ADR-008, zie ADR-008 "Open ETL-revisies"):
- [ ] Definitielijst-chunking — centroïde-pathologie. Aparte ADR-006-revisie.
- [ ] Art-familie chunking (458/bis/ter/quater, 1382-1384). Aparte ADR-006-revisie.
- [ ] Chunk-rol-tagging (`definitie`/`intro`/`inhoudelijk`/`bijlage`). Aparte ADR-006-revisie.

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
