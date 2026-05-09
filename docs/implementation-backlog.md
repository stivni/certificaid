# Implementation Backlog

Werkdocument — geen ADR. Lijst van implementatie-werk dat volgt uit de design-ronde van 2026-05-08 (ADRs 002, 004, 006, 007, 008 bijgewerkt). Wordt afgevinkt naarmate code volgt.

## Fase 2 (Bronnen-RAG) — refactor naar unified `bronnen` collection

Driver: ADR-006 §3 herzien — twee collections (`bronnen` + `concepten`) ipv vier.

- [x] `tools/rag/rag_index.py`
  - Schrijft wetteksten/normen/adviezen naar collection `bronnen` met `bron_rol`-metadata ✓
  - Chunk-strategie per brontype (artikel / sectie / heel-advies) ✓
  - `index_*`-functies bouwen ids/texts/metadatas, één gedeelde upsert via `_batch_upsert` ✓
  - Chunk-id-stabiliteit (ADR-006 §3.1, ADR-004): `<bron-stem>__art_<nr>`, `__sec_<slug>`, `__volledig` ✓
  - `chunk_sha` in metadata; SHA-skip in `_batch_upsert` ✓
  - `--scope` blijft + aparte `chroma_db_<onderdeel>/` ✓
  - `--add-concepten` (concepten-collection apart via `index_concepten`); geen `--add-concepts` ✓
  - `detect_device()` MPS → CUDA → error; `--device`-override ✓

- [x] `tools/lib/retrieval.py`
  - `ALL_COLLECTIONS = ["bronnen", "concepten"]` ✓
  - `_retrieve_candidates()`: één query op `bronnen` + optionele `where={"bron_rol": ...}` filter ✓
  - `multi_query_retrieve()` op één collection ✓
  - Geen `tdks`/`bestaande_fiches` referenties ✓
  - Context-uitbreiding wetteksten via `__art_<nr>` chunk-id schema ✓

- [x] `tools/rag/rag_query.py`
  - `--bron-rol wettekst,norm` ipv `--collections wetteksten,normen` ✓
  - Default = alle bron-rollen ✓

- [x] `tutor/app.py`
  - Sidebar-filter: bron-rol checkboxes ipv collection-checkboxes ✓
  - Sidebar-infopaneel: tellingen per bron_rol via `get(where=...)` ✓
  - CHROMA_PATH via `CERTIFICAID_CHROMA_PATH`-env-var (default = `chroma_db_4.0`) ✓
  - Dead `selected_cols`-param uit `retrieve_two_pass()` verwijderd ✓
  - Dubbele PO-query-prefix gecorrigeerd ✓
  - Citatie-rendering blijft via `label()` (`bron` + `artikel`/`sectie`/`veld`-metadata)

- [x] **Unified bronnen-collection geïmplementeerd** — rag_index.py + retrieval.py + rag_query.py klaar. Full rebuild naar één `bronnen`-collection kan via `python tools/rag/rag_index.py --reset`.

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
- [x] `tools/extractie/match_bronnen.py` — `chunk_sha` uit ChromaDB-metadata toegevoegd aan
  bundle-items. `tools/extractie/export_bundle.py` geeft `chunk_sha` door (uit matches of
  rechtstreeks uit ChromaDB-metadata). Subagent kan sha invullen in concept-record provenance.
- [x] `tools/etl/mark_stale.py` voor concepten bouwen (ADR-008 §10).
  Nieuwe modus `--concepts`: walkt `data/concept_records/**/*.json`, vergelijkt
  opgeslagen `sha256` per veld-input met live `chunk_sha` uit ChromaDB.
  Default = dry-run; `--apply` schrijft `stale: true` + `stale_reason` + `stale_at`
  op het `_provenance`-sub-object van het getroffen veld. Edge-cases gedekt:
  `chunk_missing`, `sha_unknown` (null-sha), `al_stale`. Modus 1 (bron-MD's)
  blijft backwards-compatible.
- [x] `tools/etl/remove_bron.py` Laag 2 omgezet naar concept-records: scant
  `data/concept_records/**/*.json` op inline `_provenance.inputs[].id` die starten
  met de bron-stem. Toont getroffen records + velden; past niets automatisch aan.
- [x] Prompt-templates in `prompts/` voor concept-extractie — `prompts/anchor-verrijking-v1.md`
  (Fase A) en `prompts/concept-extractie-v1.md` (Fase C). Versioned, anti-hallucinatie-regels
  en output-formaat volledig beschreven.
- [ ] Programmaonderdeel-JSON tooling: nu handmatig geschreven (4.0, 1.1).
  Mechanische extractie uit `programma.pdf` zou helpen voor de overige PO's.

**Open ETL-revisies** (apart van ADR-008, zie ADR-008 "Open ETL-revisies"):
- [ ] Definitielijst-chunking — centroïde-pathologie. Aparte ADR-006-revisie.
- [ ] Art-familie chunking (458/bis/ter/quater, 1382-1384). Aparte ADR-006-revisie.
- [ ] Chunk-rol-tagging (`definitie`/`intro`/`inhoudelijk`/`bijlage`). Aparte ADR-006-revisie.

## Fase 0 / cross-cutting — provenance uitbreiden

Driver: ADR-004 herzien.

- [x] `tools/lib/provenance.py`
  - `walk_concept_provenance(record)`: iterator over (veldpad, prov-blok) voor alle
    block-velden met inline `_provenance`. Walkt recursief door geneste dicts/lijsten.
    Slaat top-level `_provenance` (record-metadata) over.
  - `mark_field_stale(record, veldpad, reden)`: zet `stale`, `stale_reason`, `stale_at`
    op `_provenance` van het veld — in-place; aanroeper schrijft naar schijf.
  - `sha_voor_chunk(chunk_id, chroma_collectie)`: haalt live `chunk_sha` op uit ChromaDB.
  - Modus 1 (bron-MD's via `check_one`) ongewijzigd; volledige backwards-compatibiliteit.

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

## ADR-018 (eerder open)

- [x] **ADR-018 prose bijgewerkt** — verwijzingen naar verwijderd `retrieve_batch.py` verwijderd;
  context bijgewerkt van "vermoedens" naar "anchors/bron-first" (ADR-008 fase C).

## Open vragen / onderzoek

- [x] **Device auto-detect** (MPS → CUDA → error; `--device cpu` als opt-out) geïmplementeerd in `rag_index.py`. `retrieval.py` gebruikt bewust CPU als default voor query-time (MPS-geheugen vrij houden voor tutor; zie `_detect_device()` in retrieval.py).
- **Online build-pipeline**: Modal / HF-IE / RunPod als cost-effective re-index-target bij bron-update. Pas onderzoeken na Fase 1 stabiel + chunk-id-stabiliteit gevalideerd.
- **Update-only herindexering**: vereist chunk-id-stabiliteit (ADR-004) + per-chunk sha-store. Validatie: kunnen we een gewijzigde Antiwitwaswet snel re-indexen zonder de volledige corpus te herbouwen?
