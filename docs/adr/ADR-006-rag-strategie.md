# ADR-006: RAG-strategie

**Status**: Draft
**Datum**: 2026-05-07 (gewijzigd 2026-05-09: §4 frontmatter-driven chunking + per-wet hiërarchie-detectie; 2026-05-14: §4.2 adaptive sub-chunking + definitie-detectie; 2026-05-15: §5 concepten-collectie geherdefinieerd — chunking direct uit `data/concepten/records/*.json` + `data/concepten/competenties/*.yaml` (source of truth), één chunk per record. Vervangt oude per-node-veld-strategie en de 38 seed-records. Render-output in `content/` is géén bron voor de index.)
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

### 3. Vector-DB: ChromaDB met twee collections

Persistent, lokaal in `data/rag/main/`. **Twee collections**:
- `bronnen` — alle wetteksten + normen + adviezen samen, met `bron_rol` als metadata-veld (`wettekst` / `norm` / `advies` / ...) voor optionele filtering bij retrieval
- `concepten` — concept-records (zie ADR-007)

**Waarom unified `bronnen` ipv per-brontype-collection** (eerder design):
- Per-collection top-N is kunstmatige diversiteit-cap. Een AWW-vraag waarvan de top-20 chunks alle uit normen zouden moeten komen, krijgt forced "top-50 wettekst + top-50 norm + top-50 advies = 150 ruisige kandidaten". Reranker moet dat opruimen — extra werk.
- Cross-brontype-overlap (een vraag raakt zowel wettekst als norm) wordt artificieel in aparte queries gesneden.
- Filtering "alleen wetteksten" werkt even goed via metadata-where-filter (`where={"bron_rol": "wettekst"}`).
- Schema-evolutie: nieuwe brontype toevoegen = nieuw `bron_rol`-waarde, geen nieuwe collection-codepath.

Chunk-strategie blijft per brontype (zie §4) — alleen de storage is unified.

### 3.1. Chunk-id-stabiliteit (vereiste voor incremental rebuild)

Chunk-ids moeten stabiel zijn over re-runs zolang de chunk-strategie ongewijzigd is:
- Wettekst: `<bron-stem>__art_<nr>` (bv. `Antiwitwaswet-2017__art_5`)
- Wettekst sub-chunk (adaptive, zie §4.2):
  - Definitie-mode: `<bron-stem>__art_<nr>__sub_<N>deg` (bv. `WIB92__art_2__sub_5deg`).
    Suffixen voor bis/ter en slash-nummering blijven in de label: `__sub_5degbis`,
    `__sub_4deg_1` (voor `4°/1`).
  - Bin-pack-mode: `<bron-stem>__art_<nr>__sub_<marker><start>-<eind>`
    (bv. `WBTW__art_44__sub_par1-par3` voor § 1–§ 3, `__sub_a-c` voor a)–c)).
    Single-item bin krijgt `__sub_par1` zonder range.
- Norm: `<bron-stem>__sec_<sectie-naam-slug>`
- Advies (één-chunk): `<bron-stem>` ; gesplitst: `<bron-stem>__sec_<sectie-naam-slug>`

**Defensieve uniqueness** (2026-05-15): voor het zeldzame geval dat een chunk-id
collidert (duplicate art-nrs in een wettekst met overlappende sub-structuur),
krijgt de tweede instance een `__dup<N>`-suffix. Voorkomt Chroma DuplicateIDError
zonder content te verliezen. Geïmplementeerd in `tools/rag/rag_index.py`
final-loop van `split_wettekst`.

Als chunk-strategie verandert (bv. splitting-config gewijzigd): full rebuild nodig. Dan bumpt de pipeline-versie in provenance, wat de cascade triggert.

### 4. Chunking — bronnen-RAG

**Frontmatter-driven**: chunk-keuzes leven in frontmatter, niet in code. Per bron:

```yaml
chunk:
  level: 6            # MD-heading-niveau waarop chunk-grens ligt
  type: "Art."        # exacte match — geen fallback (2026-05-15)
```

De chunker is **data-driven** (leest frontmatter), niet **convention-driven** (hardcoded per bron-rol). Heterogene wetten met verschillende structurele dieptes werken zonder per-wet codepad.

**Expliciete `chunk.type`** (2026-05-15, Phase 2 cleanup): elke bron MOET een
`chunk.type` declareren die exact overeenkomt met de heading-tekst in de body:

| Type | Voor |
|---|---|
| `"Art."` | Belgische wetteksten (`###### Art. N`) |
| `"Par."` | paragraaf-genummerde wetten (`###### Par. N`) |
| `"Artikel"` | EU-richtlijnen/verordeningen/verdragen (`###### Artikel N`) |
| `"Klasse"` | MAR-rekeningplannen (`## Klasse 1`) |

Geen `_ARTICLE_TYPE_SET`-fallback meer — als de frontmatter "Art." declareert
maar de body heeft "Artikel"-headings, vindt de chunker geen grenzen en valt
het bron in de generic-pad. Voorheen werd dit gemaskeerd via een fallback;
dat verbergde echte frontmatter/extractor-mismatches.

`sub_strategy` is verwijderd uit het schema (Phase 2 cleanup). Sub-chunking is
nu automatisch adaptive (zie §4.2) — een aparte config-knop is niet nodig.

| Brontype | Eenheid | `chunk.level` | `chunk.type` |
|---|---|---|---|
| Wettekst | per artikel | dynamisch per wet (zie §4.1) | `Art.` of `Par.` |
| CBN-advies (≤40K chars) | hele advies | n/a (één chunk) | n/a |
| CBN-advies (>40K chars) | per sectie | uit `heading_stats.py` | null |
| ITAA-norm | per sectie | uit `heading_stats.py` | null |
| Praktijkgids | heading-fallback | uit `heading_stats.py` | null |

**Hard max chunk-grootte**: 8.000 chars (gelijk aan HARD_THRESHOLD, zie §4.2). Boven die grens: adaptive sub-split of `split_long_chunk` als fallback, identieke `path` en breadcrumb, suffix `__partN` op `id`.

#### 4.1 Wettekst — hiërarchie afgeleid uit het document

Wetten verschillen sterk in structurele diepte (Wet-ITAA-2019 heeft HOOFDSTUK > AFDELING > ONDERAFDELING > Art.; WVV heeft DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING > Art.). Geen universele hardcoded mapping past op alle.

**Hiërarchie-detectie** per wet: scan welke structuurlabels aanwezig zijn en orden ze volgens de vaste Belgische wettekst-hiërarchie (DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING). De volgorde is altijd dezelfde; alleen de aanwezigheid varieert per wet. Implementatie in `tools/lib/headings.py`, aangeroepen vanuit `tools/etl/convert.py` (zie ADR-005 §2 stap 3). Voorbeelden:

| Wet | Detected ranks |
|---|---|
| Wet-ITAA-2019 | HOOFDSTUK > AFDELING > ONDERAFDELING > Art. |
| Antiwitwaswet | BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING > Art. |
| WIB92 | TITEL > DEEL > HOOFDSTUK > AFDELING > ONDERAFDELING > Art. |
| WVV (na conversie-fix) | DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING > Art. |

**Mapping naar markdown-niveaus:**

- **H1** = wet-naam (vast, breadcrumb-root via `path[0].type = "wet"`)
- **H2** = hoogste structuurlabel uit detectie
- **H3–H6** = volgende ranks
- **Artikel** = laagste rank (= `chunk.level` voor die wet)

**Conditional flattening** — alleen bij overflow (>5 niveaus tussen H2 en H6 nodig):

Merge-groups (semantisch samenhangend; één label fungeert als groepering van het andere):
- `[DEEL, BOEK]` — "DEEL X - BOEK Y" als één heading
- `[AFDELING, ONDERAFDELING]` — onderafdeling is direct kind van afdeling

WVV-voorbeeld (7 niveaus → 2 merges → 5 niveaus):
```
## DEEL 1 - BOEK 1. Inleidende bepalingen.
### TITEL 1. Vennootschap, vereniging en stichting.
#### HOOFDSTUK 1. Definitie.
##### Afdeling 1 - Onderafdeling 1. Algemene bepalingen.
###### Art. 1:1
```

Niet-samenhangende merges (bv. TITEL+HOOFDSTUK) worden **niet** automatisch toegepast — informatieverlies te groot. Wetten met overflow zonder bruikbare merge-group vereisen handmatige beslissing per wet.

#### 4.2 Sub-artikel chunking — adaptive (2026-05-14)

Sub-artikel granulariteit wordt **niet** als MD-heading geforceerd. De chunker detecteert sub-grenzen automatisch via `detect_sub_markers()` **na** chunken op artikel-niveau.

**Threshold-tiers** (constants `SOFT_THRESHOLD=4000`, `HARD_THRESHOLD=8000`):

| Chunk-grootte | Actie |
|---|---|
| `< SOFT_THRESHOLD` (4000 chars) | Nooit sub-splitsen |
| `SOFT ≤ size ≤ HARD` (4000–8000) | Sub-splitsen ALS markers gevonden; anders ongewijzigd |
| `> HARD_THRESHOLD` (>8000 chars) | Sub-splitsen verplicht; `split_long_chunk` als fallback als geen markers |

**Marker-detectie** — geordend op prioriteit (eerste marker die ≥3 keer voorkomt wint):

1. `N°` (BE definitieblok): `^\s*\d+°(bis|ter|...)[\s.]` — 10.466 occurrences
2. `§ N` (BE paragraaf): `^\s*§\s*\d+` — 4.576 occurrences
3. `N.` (EU lid): `^\d+\.\s+[A-ZÀ-ÿ]` — 1.391 occurrences
4. `a) b) c)` (lettered): `^\s*[a-z]\)\s+\S` — 4.013 occurrences
5. `N)` (haak-genummerd): `^\d+\)\s+\S` — 351 occurrences
6. `i) ii) iii)` (Romein-klein): optioneel, diep genest — 220 occurrences

Streepje (`-`) is bewust **niet** geïmplementeerd als marker: 30%+ valse vrienden (tabelcellen, historiekregels).

**Definitie-blok-modus** (auto-detect via `is_definitie_blok()`):
Triggert als artikel bevat:
- Intro-patroon: `wordt verstaan onder :`, `gelden de volgende definities :`, etc. — **OF** heading-naam bevat `definit`/`begrip`/`interpretat`/`terminolog`
- **EN** ≥3 `N°`-items of letter-items

Bij trigger: **één chunk per item** (geen bin-pack). Bin-pack-modus is standaard voor paragraaf/EU-leden.

**Chunk-id-formaat sub-chunks**:
- Definitie-item `1°` → `__sub_1deg`
- Definitie-item `4°bis` → `__sub_4deg_bis`
- Paragraaf `§1`–`§3` in 1 bin → `__sub_par1-par3`
- EU lid `3.` → `__sub_lid3`
- Letter `a)` → `__sub_a`
- Haak `2)` → `__sub_n2`

**Phase 2 cleanup** (2026-05-15, commit 1e3b30b6): `chunk.sub_strategy`-veld
verwijderd uit frontmatter (was opt-in `per_definitieblok` voor 6 BE-bronnen
WIB92/WVV/Antiwitwaswet/Successierechten-federaal/WBTW-KB4/WBTW-KB22). Niet
meer nodig — adaptive detectie verwerkt deze automatisch. `_ARTICLE_TYPE_SET`-
fallback in `_is_chunk_boundary` verwijderd; elke bron moet expliciete
`chunk.type` declareren (zie §4 boven). MAR-bronnen: `type: "Klasse"`;
EU-bronnen met `Artikel`-headings: `type: "Artikel"`.

Empirische basis: `data/etl/qa/sub-marker-onderzoek.md` + `data/etl/qa/definitie-blokken-onderzoek.md`.

### 5. Chunking — concepten-RAG

**Eenheid: één chunk per record.** De `concepten`-collectie indexeert direct de **source-of-truth records** — niet de gerenderde markdown in `content/`.

#### 5.1 Bronnen voor de index

| Pad | Scope | Schema |
|---|---|---|
| `data/concepten/records/*.json` | `concept` | ADR-007 §schema 1.3 |
| `data/concepten/competenties/*.yaml` | `competentie` | ADR-007 §competentie-schema 1.0 |

`content/concepten/` en `content/competenties/` zijn render-output (ADR-010 §drie-lagen) en zijn **geen** bron voor de index. Indexeren vanuit `content/` zou betekenen dat een template-wijziging zonder record-wijziging de embeddings verandert — dat is rendering-bug-territorium, geen kennislaag-wijziging.

#### 5.2 Waarom per-record en niet per-veld of per-rendered-fiche

- **Cohesie**: een record is geschreven als één samenhangende kenniseenheid (definitie + bouwstenen + praktijk + valkuilen voor concepten; stappen + voorbeelden + valkuilen voor competenties). Een tutor-vraag valt zelden in één veld; per-veld zou top-1 een losse zin opleveren waar de student de samenhang verliest.
- **Schaal**: 30 concepten + 9 competenties = 39 chunks. Met bge-m3's 8192-token context past een record ruim in één chunk (mediaan ~3.5K chars na composing).
- **Determinisme**: 1-op-1 mapping record-bestand → chunk-id. Eén record gewijzigd = één re-embed.
- **De oude "per node-veld + edges-als-metadata"-strategie is verworpen**: graph-walks blijven waardevol bij ADR-007 §edges-redenering, maar de retrieval-context die een tutor leest is het samengestelde concept-verhaal, niet een veld-tuple.

#### 5.3 Chunk-id

- Concept: `concept:<id>` (bv. `concept:consolidatiekring`)
- Competentie: `competentie:<id>` (bv. `competentie:afbakenen-consolidatiekring`)

Stabiel zolang de record-`id` niet verandert. Rename = oude id verwijderd, nieuwe id geïndexeerd (cascade via provenance).

#### 5.4 Embed-tekst — compositie uit gestructureerde velden

De embed-tekst wordt deterministisch samengesteld uit het record. **`_provenance`-blokken worden uitgesloten** — die zijn audit-metadata en pollueren embeddings met UUID-achtige strings. Confidence-labels (`grounded` / `inferred`) gaan ook niet de tekst in; ze worden in metadata bewaard zodat de tutor ze achteraf kan tonen zonder dat ze als embedding-signaal meedoen.

**Concept-record** → vaste sectievolgorde:

```
[Concept → <programmaonderdelen> → <node_type> → <naam>]

# <naam>

<definitie.text>

## Bouwstenen
- <bouwstenen[0].naam>: <bouwstenen[0].text>
- <bouwstenen[1].naam>: <bouwstenen[1].text>
...

## In de praktijk
### <in_de_praktijk[0].aspect>
<in_de_praktijk[0].betekenis>
...

## Vergelijkingsparen
- vs. <vergelijkingsparen[0].vergelijking_met>: <vergelijkingsparen[0].verschil>
...

## Valkuilen
- <valkuilen[0].text>
...
```

**Competentie-YAML** → vaste sectievolgorde:

```
[Competentie → <programmaonderdelen> → <titel>]

# <titel>

Gebaseerd op concepten: <gebaseerd_op_concepten geconcateneerd>
Grondslag: <procedure_grondslag.motivering>

## Stappen
### Stap 1: <stappen[0].titel>
Input: <stappen[0].input>
Output: <stappen[0].output>
Waarom: <stappen[0].waarom>
Grondslag: <stappen[0].grondslag.ref>
[indien valkuilen aanwezig] Valkuil: <valkuilen[0].foute_aanname> → <valkuilen[0].correctie>
...

## Voorbeelden
### Voorbeeld 1
Situatie: <voorbeelden[0].situatie>
Conclusie: <voorbeelden[0].conclusie>
Redenering: <voorbeelden[0].redenering>
...
```

Wikilinks (`[[concept-id]]`) blijven als platte tekst in de embed — bge-m3 herkent ze als concept-referentie, en de slugs zijn betekenisvol genoeg om recall te verhogen op gerelateerde concepten.

Bovengrens: 8.000 chars (HARD_THRESHOLD, gelijk aan §4.2). Records die overshooten worden gelogd zodat een redactie-actie kan beslissen of het record gesplitst moet worden — niet automatisch ge-sub-chunked, want dat zou de "één chunk per record"-belofte breken.

#### 5.5 Metadata-velden

Per chunk in ChromaDB:

| Veld | Type | Bron in record |
|---|---|---|
| `scope` | `concept` / `competentie` | bestandslocatie |
| `id` | string | record-`id` |
| `naam` of `titel` | string | `naam` (concept) / `titel` (competentie) |
| `node_type` | string | `node_type` (alleen concept) |
| `programmaonderdelen` | JSON-string | concept: afgeleid uit `linked_anchors` (eerste segment); competentie: `programmaonderdelen` |
| `status` | string | `status` (`seed` / `voorgesteld` / `gecureerd` / ...) |
| `schema_version` | string | `schema_version` |
| `confidence_summary` | `grounded` / `inferred` / `mixed` | concept: `mixed` als er minstens één `confidence: inferred` in het record staat, anders `grounded`. Competentie: idem op stap-niveau. |
| `bron_shorts` | JSON-array | concept: alle `source.short` waarden uit definitie/bouwstenen/praktijk/valkuilen; competentie: alle `grondslag.ref` en wikilinks |
| `linked_concepts` | JSON-array | concept: doelen van `vergelijkingsparen`; competentie: `gebaseerd_op_concepten` |
| `extractor_run` | string | `_provenance.extractor_run` (voor staleness-detectie) |

`programmaonderdelen` blijft een filter-knop in retrieval (`where={"programmaonderdelen": {"$contains": "1.4"}}`).

#### 5.6 Indexeringsvolgorde en vervanging

Bij `tools/rag/rag_index.py --collection concepten`:
1. **Drop-and-rebuild**: de oude 38 seed-records worden volledig leeggemaakt. Geen migratie — die hoorden bij de in ADR-008-herziening verworpen vermoedensruimte-aanpak.
2. Scan `data/concepten/records/*.json` + `data/concepten/competenties/*.yaml`.
3. Voor elk record: compose embed-tekst (§5.4), bouw metadata (§5.5), embed met bge-m3, schrijf chunk.
4. Records met `status: rejected` of `status: archived` worden geskipt en gelogd.

#### 5.7 Retrieval-impact

In de twee-pass retrieval (ADR-006 §retrieval-pipeline) gebruikt de tutor de `concepten`-collectie als **eerste pass** met een hogere rerank-drempel (≥0.65). Hits uit deze collectie zijn pedagogisch sterker dan ruwe bron-chunks omdat ze al gestructureerd en gevalideerd zijn. De tutor toont ze met een `[concept]`-tag in de bronnenlijst en kan de bijbehorende **rendered fiche** (uit `content/concepten/<id>.md`) als volle context aanleveren aan Claude — record voor recall, rendered fiche voor leesbaarheid. De index zelf bevat alleen de record-projectie.

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
