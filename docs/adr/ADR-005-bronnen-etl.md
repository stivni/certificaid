# ADR-005: Bronnen-ETL

**Status**: Draft
**Datum**: 2026-05-12 (v2)
**Vervangt**: archive/ADR-014 (oude ETL-pipeline), ADR-008 (`bron_rol` nu hier ingebed)

## Context

Bronnen voor de Certificaid-kennisbank komen uit ~zes kanalen met elk een eigen formaat:

- ejustice.fgov.be PDFs (Belgische wetteksten in officiële opmaak)
- fisconetplus PDFs (fiscale wetteksten, andere layout)
- ejustice/justel HTML
- EU-richtlijn-PDFs (tweetalige layout met afwijkende even/oneven kolommen)
- CBN-website HTML (boekhoudkundige adviezen)
- ITAA-publicaties (PDF normen, gidsen) en IFAC-PDFs (ISA/ISAE/ISRS)

Doel: alle bronnen omzetten naar uniforme markdown met behoud van structurele
headings, tabellen en bron-traceerbaarheid, gestuurd door één configuratiebestand
zodat een nieuwe bron geen nieuw script vereist.

## Beslissing

### 1. Drie-fasige ETL-pipeline

```
raw (PDF/HTML) ── Extract ──► ruwe MD ── Transform ──► interpreteerbare MD ── Load ──► chunks
```

Strikt gescheiden verantwoordelijkheden:

**Extract** = format-specifiek. Eén concrete extractor per bron-formaat (of subtype),
optioneel geparametriseerd via abstracte basis-extractors:

- Format → tekst (PDF, HTML)
- Kolom-detectie (bbox-info uit PDF)
- Kop-/voettekst strippen (page-positie-afhankelijk)
- Page-artefacten verwijderen (`\x0c` form-feed, page-numbers)
- Output: tuple `(body, partial_frontmatter)`:
  - `body` is markdown met `# Titel` + paragrafen + lijsten + ruwe tabellen.
    Extract MAG `##/###/...` semantische headings emitteren als die **inherent**
    in de bron staan (HTML `<h2>`, PDF-bookmarks); ze zijn vrije winst en mogen
    niet weggegooid worden om in transform her-uitgevonden te worden. Een
    transformer als `inject_headings_*` skipt-of-aanvult wanneer er al
    semantische headings zijn.
  - `partial_frontmatter` is een dict met velden die de extractor zelf kan
    afleiden uit de raw: `bron_taal` (NL/FR/EN-detectie), `images: [...]`
    (geëxtraheerde figures), `pdf_bookmarks: [...]` (bron-TOC), `extract_meta:
    {pages, tables_n, footnotes_n}`. Transform's `emit_frontmatter` mergent dit
    met de transform-bijdrage (chunk-config) en de pipeline-provenance.

**Transform** = format-agnostisch, werkt op tekst. Een chain van kleine
transformers, default afhankelijk van de extractor:

- Heading-injectie ("Artikel 5." → `## Artikel 5.`) — bronsoort-specifiek
- Heading-hiërarchie normaliseren (max 6 niveaus, parent-child invariant)
- TOC strippen
- Sentence-merge over line-breaks (incl. hyphenated word-merge)
- Voetnoot-syntax normaliseren (`[1]` → `[^1]`)
- Tabellen valideren/repareren
- Frontmatter emitten (laatste step: chunk-config + provenance)

**Load** = markdown → embedding → ChromaDB. Eén pad voorlopig:
`tools/rag/rag_index.py` chunkt op `chunk.level`-headings (ADR-006), embedt
en upsertet naar ChromaDB met stabiele chunk-ids. Een tweede pad
(bronnen → Quartz HTML) is uitgesteld tot er behoefte aan is.

**Deterministisch herloadbaar — geen tussentijdse manipulatie**

Een bron herinladen = `raw → Extract → Transform → Load`. Nooit beginnen klooien
op tussentijdse markdowns. Als de output onjuist is, fix je de extractor of een
transformer en draai je de pipeline opnieuw — de markdown in
`resources/bronnen/` is een artefact, geen werkbestand.

Gevolgen:

- De **body** + **`provenance:`-blok** van een bron-MD is volledig bepaald door
  `raw + extractor + extract.params + transform.chain + pipeline_version`
  (modulo `provenance.generated_at`). Identieke input + identieke pipeline-versie
  ⇒ identieke output. Geverifieerd door `test_pipeline_is_idempotent_modulo_generated_at`.
- **`provenance.trust`** is een aparte beoordelings-laag bovenop het
  deterministische artefact; alleen `qa_bron.py` (Laag 1) en `mark_trusted.py`
  (Laag 2 + mens-override) muteren dit blok. Body en de andere provenance-velden
  blijven read-only voor humans.
- **Bron-verandering reset trust**: als één van `inputs.sha256`,
  `pipeline_version`, `extractor` of `transform.chain` wijzigt, worden bestaande
  `layer1`/`layer2`-verdicts gemarkeerd `stale: true` en wordt `trust.status`
  teruggezet naar `unreviewed`. Zonder uitzondering — ook een eerdere
  `confirmed_by: human` overleeft een bron-update niet, want de inhoud die de
  mens beoordeelde is niet meer wat er nu staat. Zie §7 voor de cascade.
- **Snapshot-tests bouwen op deze garantie**: een snapshot legt vast wat de
  pipeline produceert; updates gebeuren via `pytest --snapshot-update` na
  een echte pipeline-wijziging, nooit als reactie op een ad-hoc edit.

### 2. `resources/source_config.yaml` — enige bron van waarheid

Twee top-level blokken: `extractors:` (met per extractor de default transform-chain)
en `sources:` (de eigenlijke bronnen).

```yaml
extractors:
  pdf_ejustice:
    transform_chain:
      - merge_hyphens
      - merge_wrapped_lines
      - strip_toc
      - inject_headings_wettekst
      - organize_headings
      - normalize_tables
      - normalize_footnotes
      - emit_frontmatter
  html_cbn:
    transform_chain:
      - inject_headings_advies          # skip-or-merge als headings al aanwezig
      - organize_headings
      - protect_source_typos
      - emit_frontmatter
  # ...

sources:
  WIB92:
    bron_rol: itaa_lex
    raw: resources/raw/wetteksten/WIB92.pdf
    output: resources/bronnen/wetteksten/WIB92.md
    tags: [...]
    extract:
      extractor: custom_wib92            # ref naar extractors:-blok
      params: { ... }                    # extractor-specifiek
    # transform_chain: [...]             # optioneel — override default van extractor
```

**Compilatie-bronnen** (één raw-bestand met N zelfstandige bronnen, bv.
`WBTW-KB-compilatie.pdf` = 32 koninklijke besluiten): de compilatie-extractor
splitst de raw zelf en schrijft N outputs op basis van een **output-template
met placeholders**. Geen expliciete `splits:`-lijst per item — de extractor
detecteert hoeveel er zijn en welke variabelen (nr, korte titel, …) elke split
oplevert.

```yaml
sources:
  WBTW-KBs:
    bron_rol: itaa_lex
    raw: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
    extract:
      extractor: pdf_compilatie_kb
      params:
        inner_extractor: pdf_ejustice
        output_template: 'resources/bronnen/wetteksten/WBTW-KB{nr}-{slug}.md'
```

Welke template-variabelen (`{nr}`, `{slug}`, …) beschikbaar zijn, documenteert
elke compilatie-extractor in zijn docstring. Output-namen blijven stabiel
omdat ze direct uit raw-content afgeleid worden (chunk-id-stabiliteit,
ADR-006 §3.1).

### 3. Extractors (`tools/etl/extractors/`)

**Abstracte basis** (parametriseerbaar):

- `base.Extractor` — interface `extract(raw_path, params) -> (body: str, partial_frontmatter: dict)`
- `pdf_columns.PdfColumnsExtractor` — kolom-aware PDF-leessysteem,
  parameters: `columns: 1|2`, `even_odd_margins: bool`, `column_split_threshold: float`
- `pdf_compilatie.PdfCompilatieExtractor` — abstracte basis voor PDF-compilaties
  (1 raw → N outputs); concrete subclasses (`pdf_compilatie_kb`,
  `pdf_compilatie_mb`, …) implementeren het bron-specifieke split-patroon en
  publiceren welke template-variabelen ze leveren

**Concrete extractors:**

| Naam | Doel | Basis |
|---|---|---|
| `pdf_ejustice` | Belgische ejustice.fgov.be wetteksten | `pdf_columns` (1 kol) |
| `pdf_wetboek` | Wetboeken via pymupdf met bbox-info | eigen (pymupdf) |
| `pdf_eu_directive` | EU-richtlijnen (even/oneven marges) | `pdf_columns` (params) |
| `pdf_staatsblad` | Staatsblad-PDFs | `pdf_columns` |
| `pdf_compilatie_kb` | WBTW KB-compilatie | `pdf_compilatie` |
| `html_cbn` | CBN-adviezen HTML | eigen (html.parser) |
| `html_justel` | Justel HTML | eigen |
| `pdf_handcrafted` | Bron met `params.reason` — geen scriptbaar patroon | passthrough |

**Output-contract** (gemeenschappelijk voor alle extractors):

- Returnt `(body: str, partial_frontmatter: dict)`.
- `body` is markdown, UTF-8, met `# <bron-titel>` als enige H1, plus paragrafen,
  lijsten en ruwe tabellen. H2-H6 zijn toegestaan **alleen** wanneer ze inherent
  uit de bron komen (HTML-heading-tags, PDF-bookmarks); ad-hoc heading-promotie
  hoort thuis in transform.
- `body` bevat geen page-artefacten meer (`\x0c`, page-numbers, herhalende
  headers/footers).
- `partial_frontmatter` bevat alleen velden die uit raw-content afleidbaar zijn
  (`bron_taal`, `images`, `pdf_bookmarks`, `extract_meta`). Bron-rol, tags, wet-naam
  e.d. komen uit `source_config.yaml`; chunk-config en provenance worden in
  transform/pipeline toegevoegd.

Compilatie-extractors (subclasses van `PdfCompilatieExtractor`) leveren in plaats
van één tuple een sequentie `[(body, partial_frontmatter, template_vars), …]`,
waar `template_vars` de placeholders (`{nr}`, `{slug}`, …) invullen voor de
output-padresolutie.

### 4. Transformers (`tools/etl/transformers/`)

Elke transformer is een pure functie `(body: str, frontmatter: dict) ->
(body: str, frontmatter: dict)`. Ze worden gechained per extractor — de
default-chain staat in `source_config.yaml` onder `extractors:` (zie §2),
override per bron via `transform_chain:` op de source-entry.

**Catalogus:**

| Naam | Verantwoordelijkheid |
|---|---|
| `merge_hyphens` | `kred-\nietinstellingen` → `kredietinstellingen` |
| `merge_wrapped_lines` | soft-wrapped paragrafen mergen tot één regel |
| `strip_toc` | TOC-blok herkennen + verwijderen |
| `split_merged_headings` | `## Afdeling X. - Onderafdeling Y. ...` → twee aparte regels (PDF-artefact-fix). **MOET vóór `inject_headings_wettekst` lopen** in de chain — anders ondoet hij de bewuste Afdeling+Onderafdeling-merge die conditional flattening produceert (§4.1 ADR-006). |
| `inject_headings_wettekst` | `DEEL/BOEK/TITEL/HOOFDSTUK/AFDELING/ONDERAFDELING/Art.` → `##..######`. Past conditional flattening toe (`DEEL+BOEK`, `AFDELING+ONDERAFDELING` merges) wanneer >5 ranks aanwezig. |
| `normalize_artikel_to_art` | `Artikel N` (kolom 0) of `## Artikel N` (markdown-prefix) → `Art. N`. Voor pdftotext-output en EU-bronnen waar het volle woord wordt gebruikt. |
| `inject_headings_narratief` | sectie-detectie voor narratieve praktijkgidzen (geen Art.-hiërarchie) |
| `promote_norm_section_labels` | bold-titel-promotie voor ITAA-normen, plus structuurlabels (`CABINET`, `KANTOORNIVEAU`) |
| `strip_norm_toc_residue` | TOC-blokken met dotted/dashed/underscore-leaders + bijhorende `Inhoudstafel`-header strippen (norm-specifiek) |
| `strip_norm_column_bleed` | tweekoloms-PDF-artefacten in ITAA-normen: `## VEREISTEN TOEPASSINGSMODALITEITEN` + bilingue NL+FR-headings |
| `strip_itaa_norm_footers` | ITAA-norm-specifieke page-footers: `© ITAA – ...`, `Goedgekeurd HREB ... N/M`, `goedgekeurd door de Raad van ...`, standalone paginanummers + `Inhoud`-residu |
| `organize_headings` | hiërarchie normaliseren (max 6 niveaus, parent-child) |
| `normalize_tables` | markdown-table-syntax repareren |
| `normalize_footnotes` | `[1]` / `(1)` → `[^1]` |
| `protect_source_typos` | annotate "dit is een bron-typo, niet een artefact" |
| `emit_frontmatter` | **laatste in chain** — schrijft YAML frontmatter (chunk + provenance + bron_rol) |

**Chain-volgorde-invariant**: `split_merged_headings` moet vóór `inject_headings_wettekst` lopen in alle wettekst-chains, en `strip_norm_column_bleed` moet ná `promote_norm_section_labels` lopen (column-bleed-detectie werkt op gepromoveerde `##`-headings). Geverifieerd via `tests/test_convert_chain_order.py`.

**Default-chain per extractor** wordt in `resources/source_config.yaml` onder
`extractors:` gedeclareerd (zie §2). De pipeline leest die default; een
source-entry kan met `transform_chain:` een eigen chain forceren wanneer de bron
afwijkt van zijn extractor-default.

### 5. Output-format

```yaml
---
titel: "..."
bron_rol: itaa_lex
tags: [...]
chunk:                   # frontmatter-driven chunking (ADR-006 §4)
  level: 6               # MD-niveau waarop chunk-grens ligt
  type: "Art."           # exacte match — "Art." | "Par." | "Artikel" | "Klasse"
                         # (geen fallback meer per 2026-05-15; bron MOET expliciet)
provenance: { ... }      # zie ADR-004
---

# <bron-titel>

## ...
```

Heading-niveaus:
- H1 = wet-naam / advies-titel (vast, breadcrumb-root)
- H2-H6 = structuurlabels (bronsoort-specifiek, max 6)
- Artikel/Sectie-headings op `chunk.level`-niveau

Tabellen als markdown-tabellen. Schema's als losse PNGs in `<bron>-img/`
(via pymupdf-extractie).

### 6. Bron-rollen (5 niveaus)

| Waarde | Autoriteit | Bij examen citeerbaar? |
|---|---|---|
| `itaa_lex` | Hoogste — wettekst in ITAA-LEX | ✅ Ja |
| `normatief` | Hoog — wettekst buiten ITAA-LEX | ❌ |
| `interpretatief` | Middel — CBN-adviezen, ITAA-normen | ❌ |
| `praktijkgids` | Laag — toelichtingen, gidsen | ❌ |
| `formulier` | Referentie — aangifteformulieren | ❌ |

Stuurt confidence (ADR-010) en retrieval-filtering (ADR-006).

### 7. Kwaliteits-gate (Laag 1 + Laag 2 + mens-override + regressie-net)

Bij ~580 bronnen is handmatig elk MD-bestand controleren niet realistisch. Vier
mechanismen werken samen op elke bron-MD in `resources/bronnen/<rol-pad>/`:

**Laag 1 — Deterministische checks** (`tools/etl/qa_bron.py`)

Machine-controleerbare criteria, schrijft `provenance.trust.layer1`:

- Frontmatter compleet voor bron-rol; provenance valide (inputs+sha256, tooling, generated_at)
- `chunk.level` en `chunk.type` aanwezig
- ≥ N headings op `chunk.level` voor bestand >X chars
- Langste sectie tussen `chunk.level`-headings < 24K chars (RAG-bovengrens, ADR-006)
- Geen extractie-artefacten: `\x0c`, TOC-rest `....\d+$`, `Page N of N`,
  kolom-bleed, runs van >5 lege regels, OCR-flags (`lAB`, `lBR`, l/I-verwarring)

Status: `pass | warn | fail`. Bevestigt **nooit** trust uit zichzelf.

**Laag 2 — Inhoudelijke beoordeling** (`tools/etl/qa_subagent_prompt.md`)

Voor wat Laag 1 niet kan: leesbaarheid, scrambled-words, verdwenen secties,
abrupt einde, mismatch naam vs. inhoud. Claude Code subagent (Sonnet, lokaal —
geen API-call uit script, zie CLAUDE.md regel 3) leest bron + Laag-1-rapport en
schrijft naar `provenance.trust.layer2`:

```json
{
  "status": "trusted | needs-rework | rejected",
  "agent": "subagent-sonnet-4-6",
  "rationale": "1-3 zinnen onderbouwing",
  "concrete_problemen": [{"regel": N, "type": "...", "voorbeeld": "..."}]
}
```

Heuristiek: conservatief — bij twijfel `needs-rework`.

**Scope-beperking voor Laag 2** (2026-05-15): Laag 2 evalueert alleen
inhoud-kwaliteit. Issues die door de chunker zelf gehanteerd worden — zoals
"max-section > 24K chars" of "te weinig headings voor deze grootte" — zijn
*geen* Laag-2-concerns. Die vallen onder Laag 1 (statistieken) of onder de
chunker (adaptive sub-chunking, paragraph-cut fallback). Een agent die zo'n
issue in zijn verdict zet, leidt tot onnodige caveats — die filteren we
expliciet uit bij verdict-toepassing.

**Caveat-policy** (2026-05-15): Een agent mag in zijn verdict een caveat
*voorstellen* (in `concrete_problemen` of een aparte `caveat`-veld). Maar
`mark_trusted.py --apply-from-verdicts` schrijft een caveat **alleen** als
de mens hem expliciet doorgeeft via `--caveat "<tekst>"` of als de verdict-
status `trusted` is en de operator de hele verdict-file bewust applied.
Caveat-beslissingen blijven dus altijd human-in-the-loop — een agent kan
nooit autonoom een bron als "trusted-met-caveat" markeren.

**Verdict-toepassing** (`tools/etl/mark_trusted.py --apply-from-verdicts`):

| Laag 1 | Laag 2 | trust.status |
|---|---|---|
| `pass` of `warn` | `trusted` | `trusted`, `confirmed_by = <agent>` |
| `pass` of `warn` | `needs-rework` of `rejected` | overgenomen van Laag 2 |
| `fail` | * | `needs-rework` (Laag 2 hoeft niet te draaien) |

**Afgeleide regel** (ADR-004): `trust.status = trusted` ⇔
`layer2.status == "trusted"` OR `confirmed_by == "human"`. Anders `unreviewed`.

**Mens-override** (`tools/etl/mark_trusted.py --status trusted --confirmed-by human`):

Voor edge-cases (bv. legacy bulk, agent die het oneens is met de mens) zet de
mens expliciet `status: trusted`. `layer2.status` blijft onaangeroerd. Een
eerdere `confirmed_by: human` wordt nooit overschreven door een nieuw
agent-verdict.

**Vier trust-statussen**:

| Status | Betekenis | rag_index gedrag |
|---|---|---|
| `unreviewed` | Default; nog niet beoordeeld | Geskipt |
| `trusted` | Bevestigd OK voor RAG | Geïndexeerd |
| `needs-rework` | ETL-fix nodig | Geskipt |
| `rejected` | Niet bruikbaar; weglaten | Geskipt |

**Stale-cascade bij bron-verandering**

Beide QA-lagen krijgen een `stale: true|false` veld in hun blok. Bij elke
pipeline-run vergelijkt `pipeline.py` `inputs.sha256`, `pipeline_version`,
`extractor` en `transform.chain` met de waarden in het bestaande trust-blok:

| Wat verandert | Effect op `layer1.stale` | Effect op `layer2.stale` | `trust.status` |
|---|---|---|---|
| Niets (re-run met identieke inputs/pipeline) | `false` | `false` | behouden |
| `inputs.sha256` (raw veranderd) | `true` | `true` | reset naar `unreviewed` |
| `pipeline_version` | `true` | `true` | reset naar `unreviewed` |
| `extractor` of `transform.chain` (config) | `true` (deterministische check anders) | `true` (verdict mogelijk niet meer accuraat) | reset naar `unreviewed` |

Géén uitzondering voor `confirmed_by: human` — een mens-override is altijd op
specifieke inhoud; verandert de inhoud, dan vervalt de override. Re-run van
Laag 1 is goedkoop en gebeurt automatisch; Laag 2 vereist een nieuwe agent-pass
maar de oude verdict blijft (`stale: true`) als hint voor de mens of een
"smart re-QA" die alleen stale verdicts opnieuw beoordeelt.

**Regressie-bescherming via snapshot-testing**:

Elke extractor en transformer heeft test-fixtures + snapshots, beheerd met
**syrupy** (`pytest-snapshot` is een alternatief; syrupy is gekozen voor het
leesbare `.ambr`-bestandsformaat dat in git-diffs prima leesbaar is).

- `tests/fixtures/extract/<naam>/` — kleine raw inputs (HTML-fragment, mini-PDF) die elk
  gekend extract-patroon dekken (kolom-bleed, page-overgang, source-typo, OCR-confusion).
- `tests/fixtures/transform/<naam>.md` — platte markdown-inputs voor transformer-tests.
- `tests/__snapshots__/*.ambr` — verwachte outputs (text-format).

**Snel-pad en traag-pad** (verplicht onderscheid):

- **Snel** (`tests/test_pipeline_snapshots.py` e.d.): gebruikt **mocked**
  extractor-output — een fixed input-string per fixture, zonder echte raw-files
  te lezen. Milliseconds per fixture. Draait mee in de pre-commit hook.
- **Traag** (`@pytest.mark.slow`): integratie-tests die de echte raw uit
  `resources/raw/` lezen en de volledige extractor draaien. Wordt op aanvraag
  uitgevoerd (`pytest -m slow`), niet in pre-commit.

Bij elke test-run worden actual outputs gediff'd tegen snapshots. Failure ⇒ ofwel
regressie (fix code) ofwel bedoelde verbetering (`pytest --snapshot-update`).

Verplicht bij elke nieuwe extract/transform-fix: fixture + snapshot die het
gerepareerde geval vastlegt. Snapshots vervangen het oude "golden-set"-idee —
fijnmaziger en duidelijker te onderhouden.

Pre-commit hook (`scripts/git-hooks/pre-commit`) draait `pytest -q` (zonder
`-m slow`) zodat geen commit met rode snel-tests landt.

### 8. Indexering filtert op trust

`tools/rag/rag_index.py` indexeert default alleen bronnen met
`trust.status == "trusted"`. Geskipte bronnen worden geteld in de
run-statistiek met reden. `--include-unreviewed` voor experimenten.

Chunk-id-stabiliteit (ADR-004, ADR-006 §3.1) + ChromaDB upsert + chunk-sha-skip
maken het toevoegen van een nieuw-trusted bron volledig incrementeel: bestaande
chunks behouden hun id én worden niet opnieuw geëmbed.

### 9. Refresh-gate — trust-wijziging bindt index én bundles

**Regel**: een trust-statuswijziging die de set indexeerbare bronnen
verandert (`unreviewed`/`needs-rework`/`rejected` → `trusted`, of
omgekeerd) wordt onmiddellijk gevolgd door een herloop van de
RAG-index én de anchor-bundles. Pas daarna mag nieuw concept-extractie-
werk aanvangen op de bijgewerkte staat.

**Achtergrond**: `mark_trusted.py` raakt op zich alleen de
provenance-frontmatter aan; de RAG-index (`data/rag/main`) en de
anchor-matches-store (`data/extractie/matches.sqlite3`) zijn pas
consistent nadat respectievelijk `rag_index.py` en `match_bronnen.py`
opnieuw gedraaid zijn. Tussen die twee momenten zit een venster waarin
extractie-bundles een nieuw-trustede bron volledig missen — wat in PO
1.5-1.9 voor ISA-bronnen en IFRS-wetteksten gebeurd is en concept-records
heeft opgeleverd zonder de juiste primaire referenties.

**Implementatie**:

- `tools/etl/refresh_rag_and_matches.py` voert beide stappen achter
  elkaar uit. Faalt stap 1 dan wordt stap 2 niet aangevuurd (anders
  mismatch tussen index en bundles).
- `tools/etl/mark_trusted.py --refresh` roept de wrapper aan zodra de
  trust-mutatie geschreven is. Dit is de aanbevolen route voor elke
  agent-batch-promotie (`--apply-from-verdicts ... --refresh`).
- Beide stappen zijn incrementeel: SHA-check in `rag_index.py` skipt
  ongewijzigde chunks; `match_bronnen.py` is delta-driven en herberekent
  alleen de anchors die geraakt worden door chunk- of vector-wijzigingen
  (ADR-005 §9.1 — SQLite-store met state-fingerprints).

**Operationele consequentie**: scripts die concept-bundles consumeren
(`tools/extractie/export_bundle.py`, downstream extractie-prompts) gaan
ervan uit dat `data/extractie/matches.sqlite3` synchroon is met de
huidige trust-state. Een hand-geschreven trust-promotie zonder `--refresh`
is een proces-fout, geen geldige tussenstand.

### 9.1. Matches-store — delta-driven SQLite met state-fingerprints

**Store**: `data/extractie/matches.sqlite3` — SQLite-database, gitignored
(herbouwbaar via `python3 -m tools.extractie.match_bronnen`).

**Schema** (tabel `matches`):

| Kolom | Type | Beschrijving |
|---|---|---|
| `anchor_id` | TEXT | anchor-identificatie (bv. `1.1.taak.1`) |
| `chunk_id` | TEXT | chunk-id uit ChromaDB |
| `score` | REAL | cosine-similarity (0–1) |
| `in_bundle` | INTEGER | 1 = in definitieve bundle, 0 = onder de drempel |
| `chunk_sha` | TEXT | vingerafdruk van chunk-inhoud (uit ChromaDB metadata) |
| `anchor_vector_hash` | TEXT | sha256 van anchor-vector bytes, eerste 16 hex |

Primaire sleutel: `(anchor_id, chunk_id)`.
Twee indices: `(anchor_id, in_bundle)` voor bundle-queries; `(chunk_id)` voor delta-detectie.

**Delta-algoritme**:

1. Vergelijk huidige ChromaDB-chunks met store op `chunk_sha`:
   → `chunks_weg`, `chunks_nieuw`, `chunks_stale`
2. Vergelijk huidige anchors.json-vectorhashes met store:
   → `anchors_weg`, `anchors_nieuw`, `anchors_stale`
3. DELETE rijen voor `chunks_weg` en `anchors_weg`.
4. Bepaal te herberekenen anchors:
   - `anchors_nieuw` + `anchors_stale` (eigen vector veranderd)
   - Alle anchors die een match hadden met `chunks_weg` of `chunks_stale`
   - Als er `chunks_nieuw` zijn: alle anchors in de store (nieuwe chunks kunnen voor elk anchor relevant zijn)
5. Herbereken cosine-scores voor geraakte anchors (batched numpy, 50 anchors per batch).
6. Strict re-rank per anchor: herbereken `in_bundle` flag op basis van
   `max(threshold, top1 - margin)`.
7. Idempotent: als er geen delta is én de store niet leeg is → 0 mutaties.

**Geen `--rebuild-all` mode**: het algoritme handelt massa-staleness
correct af via de batch-herberekening van alle geraakte anchors.

**Helpers** (`tools/lib/matches_store.py`):

- `open_store(db_path) -> sqlite3.Connection` — schema-init bij eerste call
- `get_bundle(conn, anchor_id) -> list[tuple[chunk_id, score]]` — alleen `in_bundle = 1`
- `current_chunks_with_sha(chroma_path) -> dict[chunk_id, chunk_sha]` — uit ChromaDB
- `current_anchors_with_hash(anchors_path) -> dict[anchor_id, vector_hash]` — uit anchors.json

### 9.1 Matches-store — delta-driven SQLite met state-fingerprints

**Probleem**: de huidige `match_bronnen.py` berekent bij elke run een volledige cosine-matrix van ~1.500 anchors × ~21.860 chunks (~33M ops) en herschrijft `matches/latest.json` integraal. Bij één toegevoegde of getrustte bron met ~200 chunks is dat 100× te veel werk — en blokkeert het refresh-gate-flows in praktijk uren-lang. Bovendien is een herschreven JSON-blob niet selectief te updaten zonder de hele file te herschrijven.

**Beslissing**: vervang `matches/latest.json` door **`data/extractie/matches.sqlite3`** met state-fingerprints per rij, en herschrijf `match_bronnen.py` als delta-driven script dat de diff tussen actuele state en SQLite afleidt. Principe: correct + robuust > snel & afwijkende paden.

**Schema**:

```sql
CREATE TABLE matches (
    anchor_id           TEXT NOT NULL,
    chunk_id            TEXT NOT NULL,
    score               REAL NOT NULL,
    in_bundle           INTEGER NOT NULL,    -- 0/1, top-margin band
    chunk_sha           TEXT NOT NULL,       -- chunk-sha bij match-tijd
    anchor_vector_hash  TEXT NOT NULL,       -- anchor-vector-hash bij match-tijd
    matched_at          TEXT NOT NULL,       -- ISO8601 UTC
    PRIMARY KEY (anchor_id, chunk_id)
);
CREATE INDEX idx_matches_chunk         ON matches(chunk_id);
CREATE INDEX idx_matches_anchor_bundle ON matches(anchor_id, in_bundle);
```

`chunk_sha` en `anchor_vector_hash` zijn **state-fingerprints**: bij elke run vergelijkt het script de fingerprints met de actuele ChromaDB-shas en anchors.json-vectorhashes. Mismatch → rij is stale, wordt verwijderd en opnieuw berekend.

**Delta-algoritme** (één draaiing, ongeacht trigger):

```
huidig_chunks  = {chunk_id: chunk_sha} uit ChromaDB
huidige_anchors = {anchor_id: vector_hash} uit anchors.json

# Diff bepalen
chunks_weg     = SELECT chunk_id WHERE chunk_id NOT IN huidig_chunks
chunks_nieuw   = huidig_chunks.keys() - SELECT DISTINCT chunk_id
chunks_stale   = SELECT chunk_id WHERE chunk_sha != huidig_chunks[chunk_id]

anchors_weg    = SELECT anchor_id WHERE anchor_id NOT IN huidige_anchors
anchors_nieuw  = huidige_anchors.keys() - SELECT DISTINCT anchor_id
anchors_stale  = SELECT anchor_id WHERE anchor_vector_hash != huidige_anchors[anchor_id]

# Verwijderen
DELETE FROM matches WHERE chunk_id  IN chunks_weg  ∪ chunks_stale
DELETE FROM matches WHERE anchor_id IN anchors_weg ∪ anchors_stale

# Herberekenen
for chunk_id in chunks_nieuw ∪ chunks_stale:
    embedding = ChromaDB.get(chunk_id, include='embeddings')
    scores    = anchor_matrix @ embedding         # ~1.500 cosines per chunk
    INSERT rijen waar score ≥ floor

for anchor_id in anchors_nieuw ∪ anchors_stale:
    vector = anchors.json[anchor_id].vector
    scores = chunk_matrix @ vector                # ~21K cosines per anchor (eerstwerk)
    INSERT rijen waar score ≥ floor

# Strict re-rank per geraakte anchor
for anchor_id in unieke_geraakte_anchors:
    top1 = MAX(score) WHERE anchor_id = ?
    UPDATE matches SET in_bundle = (score >= MAX(floor, top1 - margin))
```

**Vijf event-typen die het algoritme zonder triggers afhandelt**:

| Event | Detectie | Actie |
|---|---|---|
| Chunk toegevoegd (nieuwe bron / nieuw-trusted) | `chunk_id ∈ chunks_nieuw` | cosine tegen alle anchors → insert |
| Chunk verwijderd (bron verwijderd / detrust) | `chunk_id ∈ chunks_weg` | `DELETE WHERE chunk_id = ?` |
| Chunk inhoud gewijzigd (her-ETL) | `chunk_sha != huidige_sha` | als verwijderd + nieuw |
| Anchor toegevoegd (examenprogramma-update) | `anchor_id ∈ anchors_nieuw` | cosine tegen alle chunks → insert |
| Anchor-vector veranderd (tekst-rewrite / model-upgrade) | `vector_hash != huidige_hash` | `DELETE WHERE anchor_id = ?` + opnieuw |

**Robuustheidsgevolg**: ook als refresh-gate niet wordt aangeroepen — bv. iemand muteert chunks via een omweg of het indexerproces crasht halverwege — vangt de volgende run het op via de fingerprint-vergelijking. Geen blind vertrouwen op trigger-discipline.

**Geen migratie**: bestaande `matches/latest.json` wordt verlaten. Bij eerste run is de SQLite leeg → alle chunks vallen in `chunks_nieuw` → algoritme vult incrementeel. Eerstwerk = volledige matrix (~33M ops in numpy ≈ seconden, niet uren — bge-m3-laden en niet-gebatchte numpy waren de oude bottlenecks). Volgende runs zijn delta.

**Geen aparte `--rebuild-all`-mode**: als massa anchor-vectoren stale worden (model-upgrade) handelt het algoritme dat correct af via `anchors_stale`. Trage een-keer-gebeurtenis acceptabel boven een afwijkend pad dat zelden gebruikt wordt en sneller stuk gaat.

**Embedding-source-of-truth blijft ChromaDB**: SQLite is alleen matches-store. Chunk-embeddings worden batched opgehaald via `collection.get(ids=[...], include=['embeddings'])` tijdens herberekening. Geen embedding-duplicatie.

**Consumer-aanpassing**: `tools/extractie/export_bundle.py` en downstream consumers lezen niet meer uit `matches/latest.json` maar via een query-helper (`tools/lib/matches_store.py`) die de SQLite leest. Top-margin-bundle per anchor → `SELECT chunk_id, score FROM matches WHERE anchor_id = ? AND in_bundle = 1`.

## Output-contract per fase (testbaarheid)

Elke fase produceert een testbaar artefact:

| Fase | Input | Output | Test-type |
|---|---|---|---|
| Extract | `raw/X.pdf` | platte markdown-string | Snapshot per fixture |
| Transform | platte markdown | interpreteerbare markdown | Snapshot + unit |
| Load | interpreteerbare markdown | chunks in ChromaDB | Idempotentie-test |

Dit maakt isolatie van fouten triviaal: een failing snapshot zegt direct of het
in extract of in transform stuk gaat.

## Gevolgen

**Modules** (`tools/etl/`):

- `pipeline.py` — orchestrator: leest config, kiest extractor + chain (uit `source_config.yaml`), past stale-cascade toe, schrijft output
- `extractors/` — alle extract-modules (zie §3)
- `transformers/` — alle transform-modules (zie §4); chains zijn config-driven, geen Python-defaults-dict
- `qa_bron.py` — Laag 1 deterministische checks
- `qa_subagent_prompt.md` — Laag 2 prompt-template
- `mark_trusted.py` — trust-derivatie + mens-override
- `audit_wettekst_toplevels.py` — conversie-bug-audit

**Tests** (`tests/`):

- `tests/test_extractors/test_<naam>.py` — per extractor, snapshot + unit
- `tests/test_transformers/test_<naam>.py` — per transformer, snapshot + unit
- `tests/test_pipeline.py` — orchestrator + idempotentie
- `tests/test_headings.py`, `tests/test_qa_bron_staging.py` — bestaande tests
- `tests/fixtures/`, `tests/__snapshots__/` — fixture + snapshot data
- Pre-commit hook draait `pytest -q`

**`source_config.yaml`**:

- Top-level `extractors:` blok met per extractor de default `transform_chain:`
- Per source: `extract.extractor` + `extract.params`; optioneel `transform_chain:` voor override
- Compilaties: `output_template` in `extract.params` (geen aparte `splits:` blok)

**Workflow voor end-to-end re-conversie**:

```
1. python tools/etl/pipeline.py --all                   → resources/bronnen/*.md (unreviewed)
2. python tools/etl/qa_bron.py --all                    → schrijft layer1-blok per bron
3. Claude Code subagent (Sonnet/Opus, lokaal) via Task-tool
   met qa_subagent_prompt.md                            → data/etl/qa/<run-id>-verdicts.json
4. python tools/etl/mark_trusted.py --apply-from-verdicts → trust.status afgeleid
5. python tools/rag/rag_index.py                        → indexeert trusted bronnen
```

Geen staging-directory; geen sample-review; mens-override voor edge-cases.

## Open punten

- WVV-extractie is stuk (slechts 1 artikel geëxtraheerd terwijl 1866 verwacht);
  gedetecteerd door `tests/test_headings.py::test_wvv_hierarchie_en_merges` (xfail strict).
  Fix vereist betere `pdf_wetboek`-extractie of `html_justel`-fallback.
- EU-richtlijn-PDFs met afwijkende kolom-marges tussen even/oneven pagina's —
  vereist parameter-uitbreiding in `pdf_columns.PdfColumnsExtractor`.
- Trust-percentage opvoeren (huidig 51%): patroon-clustering van
  needs-rework-rationales → gerichte transformer-fixes per cluster.
- Tweede load-pad (bronnen → Quartz HTML) — uitgesteld tot er een concrete vraag is.
