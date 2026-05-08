# ADR-008: Concept-extractie

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-08 (geen-API-tijdens-build, kenniselement-gestuurde retrieval, live duplicate-check, variabel record-aantal)

## Context

Concepten ontstaan niet vanzelf. Drie ingangen leveren materiaal, en geen van de drie alleen volstaat:

- **Het examenprogramma** zegt *welke* concepten nodig zijn (scope), niet *wat* ze inhouden. Belangrijk: niet alleen kenniselementen leveren input — ook **taken** (wat de accountant doet) en **doelstellingen** (wat hij moet kunnen). Alleen kenniselementen indexeren laat de procedurele kant onbelicht.
- **Bronnen** leveren juridische inhoud, maar niet alle bronnen zijn even gezagsvol en niet alle relevante kennis staat letterlijk in een artikel.
- **Voorbeeldexamens** tonen de toetsings-realiteit (welke diepte, welke uitzonderingen worden bevraagd), maar als je extractie alleen daarop baseert loop je met oogkleppen — je dekt enkel wat eerder gevraagd werd.

Daarom: programma-gestuurd + bron-gestuurd in Fase 3 (initiële conceptenset), examen-gestuurd pas in Fase 5 (validatie + gerichte bijbouw). Iteratief proces dat het schema kan laten evolueren wanneer nieuw soort kennis niet past.

## Beslissing

### 0. Geen externe LLM-API tijdens build-pipeline

Alle LLM-werk in de extractie-pipeline (vermoedensruimte / seed / verdiep / bron-driven) gebeurt **lokaal via een Claude Code subagent** in de dev-omgeving. Geen `anthropic.Anthropic()`-calls vanuit build-tooling.

Alleen de **gedeployde tutor** mag op runtime de Anthropic API aanroepen — dat is een productie-eindpunt, geen build-stap.

Concreet voor build-tooling:
- Helper-scripts in `tools/extractie/` doen **deterministisch werk** (vermoedens laden, retrieval orkestreren, JSON wegschrijven, Chroma-collection updaten)
- Geen LLM-calls in deze scripts; geen `anthropic` import
- LLM-synthese gebeurt door een Claude Code subagent die deze helpers via Bash-tool aanroept

Dit aligneert met CLAUDE.md regel 3 (geen API voor batch-extractie zonder akkoord) — voor de build-pipeline is de regel verscherpt naar "nooit", omdat alle output meegedeployed wordt.

#### Modelkeuze voor de subagent: Opus

De extractie-subagent draait op **Claude Opus** (huidige versie: claude-opus-4-7). Argumenten:

- **Hoge leverage**: één goed seed-record bespaart 10× zoveel mens-curatie. Slechte seeds vervuilen de hele kennisbank stroomafwaarts.
- **Multi-criteria reasoning**: per vermoeden moet de agent simultaan beslissen over relevantie (rerank-score-interpretatie), duplicate-check (semantische overlap met bestaande concepten), granulariteit (klein/middel/groot per schrijfregels), node-type-keuze, kenniselement-koppeling, en eventueel split/merge. Deze gelaagde beslisruimte rechtvaardigt het sterkste model.
- **Synthese-kwaliteit**: hoofdtekst-velden worden in simpele Nederlandse taal herschreven uit juridische brontekst, met behoud van precisie + confidence-labels + bronverwijzingen. Vereist sterke taalbeheersing en domeinaanvoelen.
- **Decisielog**: kept/merged/rejected/split-redeneringen zijn input voor mens-curatie; ze moeten transparant en consistent zijn.

Sonnet/Haiku zijn ongeschikt voor extractie-werk — wel voor helper-script implementatie en routine codewijzigingen.

Provenance-veld: `tooling.model = "claude-opus-4-7"` op elk concept-record dat door deze pipeline geproduceerd is.

### 1. Drie ingangen, gefaseerd ingezet

| Ingang | Vraag | Wanneer | Werkwijze |
|---|---|---|---|
| **Programma-gestuurd** | Welke concepten dekken dit taakblok / kenniselement? | Fase 3 | Vermoedensruimte → multi-level retrieval → seed-records → verdieping |
| **Bron-gestuurd** | Welke fenomenen zitten in deze bron die we nog niet hebben? | Fase 3 (parallel) | Iteratieve scan van bron-MD's met concept-spotting prompt |
| **Examen-gestuurd** | Welke concepten waren nodig om deze vraag op te lossen? Wat ontbreekt nog? | **Fase 5 cross-cutting** | Voorbeeldexamen-vraag oplossen met huidige conceptenset → gat = uitbreiding |

**Waarom examen-driven naar Fase 5**: het is niet zinvol om examenvragen als extractie-input te gebruiken voordat een werkende basis-conceptenset bestaat. Anders ontstaat circulaire bias ("ik maak concepten zodat dít examen oplosbaar is" ≠ "ik maak concepten zodat de student het domein begrijpt en daarmee elk examen aankan"). In Fase 5 wordt examen-driven een **validator** ("kan de huidige conceptenset deze vraag oplossen?") en pas bij gaps een gerichte extra extractie-input.

### 2. Programma-gestuurde extractie — vier fases

```
A. Vermoedensruimte genereren (LLM, geen retrieval)
   ↓
B. Multi-level retrieval per vermoeden
   ↓
C. Seed-records bouwen (LLM-synthese)
   ↓
D. Verdieping per concept (iteratief)
```

#### A. Vermoedensruimte

Subagent (in Claude Code) krijgt:
- Programmaonderdeel-titel + parent-context
- Eén taakblok in zijn geheel: taken + doelstellingen + kenniselementen
- Conceptmodel-schema (node-types + edge-types)
- Concept-schrijfregels (`docs/concept-schrijfregels.md`) inclusief de "Wat is een concept?"-sectie
- Lijst van bestaande concept-naburen (om duplicatie te vermijden)

Output per vermoeden — **gestructureerd schema** (verplicht voor downstream stappen):

```json
{
  "naam": "<volledige naam, simpele taal>",
  "node_type": "<11 types, of voorgesteld:<naam>>",
  "rationale": "<één zin: waarom dit concept hier relevant is>",
  "kenniselementen": ["4.0.I.D.7", ...],   // optioneel — leeg als vermoeden uit pure taak/skill komt
  "taken_doelstellingen": ["4.0.D1.1.taak.1", "..."],   // optioneel — voor procedure/skill-types
  "schaal_signaal": "<klein|middel|groot>"  // hint voor granulariteit (zie schrijfregels)
}
```

10–30 vermoedens per taakblok. **Geen main_rule/exceptions** in deze fase — pure vermoedensruimte.

Belangrijk: `kenniselementen` mag een lege lijst zijn. Niet elk concept heeft een direct kenniselement-anker — een procedure of skill kan louter uit een taak/doelstelling komen. Forceer geen mapping als die er niet is.

LLM mag een **niet-voorgedefinieerd node-type voorstellen** (`node_type: "voorgesteld:<naam>"`). Voorgestelde types verzamelen in review-queue (ADR-007).

#### B. Multi-level retrieval

Per vermoeden retrieval op vier niveaus tegen `bronnen`-collection (ADR-006). Niveau 3 is optioneel (alleen als vermoeden kenniselementen koppelt):

1. **Programmaonderdeel-niveau**: programmaonderdeel-titel + samenvatting → brede thematische context
2. **Taakblok-niveau**: taken + doelstellingen + kenniselementen samen → mid-level
3. **Kenniselement-niveau** (optioneel): tekst van elk gekoppeld kenniselement (incl. parent + subitems) → formele scope-anker. **Skipt** als `kenniselementen` leeg is.
4. **Vermoeden-niveau**: vermoeden-naam + rationale → granulair, concept-specifiek

Per vermoeden: combineer chunks uit alle 4 niveaus, dedupliceer op chunk-id, rerank gezamenlijk, top-N (~10–15) doorgeven aan stap C.

**Waarom kenniselement-niveau apart**: een kenniselement zoals `4.0.I.D.7 Beroepsgeheim` is een formele scope-anker; zijn tekst hint vaak naar de exacte wetsartikelen. Zonder dit niveau zit retrieval te dicht op de generieke vermoeden-naam en mist het gezagsbron-passages.

Implementatie: `multi_query_retrieve` in `tools/lib/retrieval.py` (bestaat al, accepteert lijst van sub-queries).

#### C. Seed-records bouwen

Subagent verwerkt vermoedens **één voor één**, met deze flow per vermoeden:

1. **Live duplicate-check** tegen bestaande concepten:
   - Embed vermoeden (naam + rationale) → query `concepten` ChromaDB-collection
   - Top-1 rerank-score > 0.80 → mogelijk duplicaat → subagent beslist expliciet:
     - **Merge**: voeg eventuele nieuwe info toe aan bestaand record, log als alias
     - **Distinct**: motiveer waarom dit toch een ander concept is (dan toch nieuwe seed)
   - Tussen 0.65–0.80 → grijze zone, subagent meldt expliciet in log
   - < 0.65 → veilig nieuw concept

2. **Relevantie-check** (anti-hallucinatie):
   - Top rerank-score uit retrieval (stap B) < 0.30 → vermoeden niet gegrond → status `rejected`
   - 0.30–0.50 → status `seed` met note "zwak gegrond, te verifiëren"
   - ≥ 0.50 → status `seed`

3. **Seed-record schrijven** wanneer relevantie-check passeert en geen merge:
   - `id`, `naam`, `node_type`, `source`
   - `main_rule` of `definitie` (paraphrase uit chunks met `confidence: "grounded"` + bronverwijzing)
   - Initiële `edges` (mogelijk `_dangling: true`)
   - Status: `seed` (of `rejected` bij stap 2)
   - Velden die niet gerechtvaardigd zijn blijven leeg — sparse is de norm (ADR-007)

4. **Onmiddellijk indexeren in `concepten`-collection**: nieuwe concepten worden direct embedded en in ChromaDB geschreven, zodat het volgende vermoeden ze in stap 1 kan terugvinden.

5. **Programmaonderdeel-JSON updaten**: voeg de nieuwe concept-id toe aan `kenniselementen[<code>].concepten` voor elk kenniselement dat het concept afdekt (ADR-002). Ook voor taken/doelstellingen-concepten via `taakblokken[].taken[].concepten` of `taakblokken[].doelstellingen[].concepten`.

#### Variabel record-aantal: agent mag splitsen / mergen / rejecteren / toevoegen

Vertrek met N vermoedens per taakblok, eindig met M ≷ N records. De subagent mag:
- **Mergen**: twee vermoedens blijken hetzelfde concept → één record (live duplicate-check)
- **Splitsen**: één vermoeden bevat eigenlijk twee fenomenen → twee records
- **Rejecteren**: vermoeden niet gegrond in bronnen → géén record (relevantie-check)
- **Toevoegen** (dangling-resolutie): main_rule verwijst naar concept dat nog niet bestaat → extra seed voor de target

Beslissingslog per run: `data/extractie/<po>/seed_log_<taakblok>.json` met per vermoeden de beslissing (`kept`/`merged_into:<id>`/`rejected:reason`/`split_into:[id, id]`) + duplicate-check rerank-scores. Dit is mens-curatie input.

#### D. Verdieping per concept

Voor elke seed → status `partieel`:
- **Verdiepende retrieval-queries** met cumulatieve concept-state als input:
  - Concept-naam + synoniemen
  - Bestaande veld-content (`main_rule`, `exceptions`) als context
  - Edge-targets (gerelateerde concept-namen)
  - LLM-multi-query-expansion op basis van wat al gekend is
- LLM vult `exceptions`, `scope`, edge-targets verder in
- Dangling-edges → seed-queue voor volgende extractie-ronde

Status `gevuld` (later, eventueel handmatig of via tweede LLM-pass): `pitfalls`, `voorbeeld_inline`. Examen-driven cases komen pas in Fase 5.

### 3. Bron-gestuurde extractie

Iteratieve scan over bron-MD's: voor elk artikel/sectie laat een concept-spotting prompt LLM een lijst opstellen van fenomenen die in deze passage opduiken die nog géén concept zijn. Output convergeert in dezelfde `data/concept_records/`-map; dedupe via concept-id-similarity.

Anti-explosie-regel: bron-driven mag geen concepten genereren die buiten de scope van enige programmaonderdeel-kenniselement vallen — anders extraheer je de hele wet. Cap via "moet aan minstens één kenniselement koppelbaar zijn" (heuristiek, geen hard filter).

### 4. Examen-gestuurde extractie (Fase 5)

Pas wanneer een werkende conceptenset bestaat:
- Voorbeeldexamen-vraag oplossen met huidige concepten + bronnen-RAG
- Concepten die de oplossing nodig had: tag als `voorbeeldvraag-id` in concept-record (link naar voorbeeldexamen-record)
- Concepten die ontbraken (oplossing miste detail): markeer voor uitbreiding, voeg `pitfalls`/`voorbeeld_inline` toe op basis van vraag-redenering

Anti-oogkleppen-regel: examenvraag = **toetsings-instantie van een breder concept** (een examenfocus, ADR-009), géén concept op zich. Voorbeeld: "wanneer is melding aan CFI verplicht?" → instantie van `meldingsplicht-cfi`, niet een nieuw concept "wanneer-melding-CFI".

### 5. Confidence-labeling per veld

Elk veld erft een `confidence` string-tag (zie ADR-007 voor waarden — `"grounded"` / `"inferred"`):
- `bron_rol` van de chunks waaruit het is afgeleid (`itaa-lex`, `wettekst`, `norm` → `grounded`)
- Type extractie-stap (verbatim/paraphrase → `grounded`; geconstrueerde redenering → `inferred`)

Een veld zonder bronverwijzing krijgt nooit stilzwijgend `grounded`.

### 6. Per-veld provenance

Concept-record `_provenance` wordt fijnmaziger dan een file-level blok:

```json
"_provenance": {
  "main_rule": {
    "inputs": [{"id": "Antiwitwaswet-2017__art_5", "sha256": "...", "version": "etl-v1.2"}],
    "tooling": {"pipeline": "concept_extractor", "pipeline_version": "abc1234", "model": "claude-sonnet-4", "prompt_version": "extract-seed-v1"},
    "generated_at": "2026-05-08T12:00:00Z"
  },
  "exceptions": { ... mogelijk andere chunks ... }
}
```

Bij **bron-update** (chunk-content-hash verandert) → `mark_stale.py` walkt: welke concept-records hebben deze chunk-id als input voor welk veld? → die velden worden `stale: true`. Andere velden in hetzelfde concept blijven valide. Re-extraction-queue verzamelt stale velden.

Vereist **chunk-id-stabiliteit** (ADR-006 §3.1, ADR-004).

**Implementatie-status (2026-05-08)**: het schema voorziet `sha256`, maar de huidige extractor laat dat veld op `null` (zie `data/concept_records/clientacceptatiebeleid.json`). Daarmee is staleness-detectie nog onmogelijk: er is geen vergelijkpunt voor "is deze input nog gegrond op de huidige chunk?". Het invullen van `sha256` met de actuele `chunk_sha` uit ChromaDB-metadata is een implementatie-eis die mee moet in de eerstvolgende extractie-tooling-iteratie. Pas dán kan `mark_stale.py` (nog te bouwen) zinvol werken.

### 7. Permanent vs ephemeral provenance-artefacten

Twee artefacten dragen tijdens extractie chunk-verwijzingen:

| Artefact | Locatie | Levensduur | Status |
|---|---|---|---|
| **Vermoeden** + **retrieval-resultaat** | `data/extractie/<po>/{vermoedens,retrieval}/*.json` | tijdelijk — extractie-hulpmiddel | ephemeral |
| **Concept-record `_provenance`** | `data/concept_records/<id>.json` | permanent — duurzame kennislaag | authoritative |

**Beslissing**: de permanente provenance leeft uitsluitend in concept-record `_provenance`-velden. Vermoeden- en retrieval-JSONs zijn een wegwerpbaar tussenstadium dat opgeruimd mag worden zodra een vermoeden ofwel verworpen is, ofwel opgenomen in een concept-record met `status >= partieel`.

Implicaties:

- **Dependency-analyses werken op concept-records, niet op retrieval-JSONs.** Bijvoorbeeld: `tools/etl/remove_bron.py` Laag 2 (zie ADR-005 §5) scant `data/concept_records/**/_provenance.*.inputs[].id` voor chunk-IDs die op de te verwijderen bron wijzen — niet `data/extractie/.../retrieval/*.json`. Een retrieval-JSON die toevallig nog bestaat is bonusinformatie, geen vereiste.
- **`mark_stale.py` werkt op concept-records.** Bij chunk-content-hash-verandering walkt het script door `data/concept_records/`, niet door retrieval-JSONs.
- **Retrieval-JSONs zijn cachebaar/wegwerpbaar.** Een gitignore op `data/extractie/.../retrieval/` is acceptabel; een gitignore op `data/concept_records/` is dat niet (geverifieerde records moeten gecommit worden).
- **Vermoedens-JSONs blijven tijdelijk getrackt** (curatie-artefact in `data/extractie/.../vermoedens/`) zolang we ze inhoudelijk hervragen tijdens curation. Maar de provenance-keten leunt er niet op.

Deze beslissing maakt de extractie-pipeline robuust tegen opruim-acties: oude retrieval-runs uit `data/extractie/` weggooien breekt niets — de duurzame links liggen in `data/concept_records/`.

### 8. Schema-evolutie tijdens extractie

Wanneer een concept niet past in het huidige conceptmodel:
- Extractor genereert expliciet schema-uitbreidingsvoorstel (nieuw veld, nieuw node-type, nieuw edge-type)
- Voorstel landt in `data/concept_records/_voorgestelde_types.yaml` (zie ADR-007)
- Pas na menselijke bevestiging wordt het schema bijgewerkt; de extractor slaat het concept ondertussen als `partieel` op met een notitie

## Gevolgen

- **Build-pipeline tooling** (Python-scripts in `tools/extractie/`) doet alleen deterministisch werk:
  - `tools/extractie/retrieve_batch.py` — leest vermoedens, doet 4-niveau retrieval, dumpt resultaat (één model-load voor alle queries)
  - `tools/extractie/normalize_vermoedens.py` — leidt `kenniselementen: [code]` af uit `gekoppeld_aan` + taakblok-context
  - `tools/extractie/index_concept_incremental.py` — embed één concept-record en upsert in `concepten` ChromaDB-collection
  - `tools/extractie/queue.py` — dangling-edges → seed-queue
  - **Geen `anthropic` import** in deze scripts. Geen LLM-calls.
- **LLM-werk** gebeurt door een Claude Code subagent in dev-omgeving die deze helpers via Bash-tool aanroept en zijn eigen reasoning gebruikt voor synthese.
- `tools/lib/coverage.py` — bouwt op aanvraag een reverse-index (concept → kenniselementen) uit programmaonderdeel-JSON's voor dekkingsrapporten. Geen state op concepten zelf (ADR-002, ADR-007).
- Per-veld provenance + per-veld stale-marking maakt incremental re-runs **veld-precies** (alleen stale velden herextraheren, niet hele concept-records).
- **Implementatie-eisen voor §6 + §7** (TODO):
  - Concept-extractor moet `chunk_sha` uit ChromaDB-metadata kopiëren naar `_provenance.<veld>.inputs[].sha256` (nu `null`).
  - `tools/etl/mark_stale.py` voor concepten bouwen: vergelijk opgeslagen `sha256` met live ChromaDB `chunk_sha`; flag mismatches.
  - `tools/etl/remove_bron.py` Laag 2 omzetten: scan `data/concept_records/**/_provenance.*.inputs[].id` (i.p.v. `data/extractie/.../retrieval/*.json`) voor chunk-impact-analyse.
- Voorbeeldexamens worden vroeg gestructureerd (`data/voorbeeldexamens/`) als ground truth — maar pas in Fase 5 als extractie-input gebruikt.
- Concept-schrijfregels (`docs/concept-schrijfregels.md`) zijn input voor elke subagent-invocatie. Schrijfregels evolueren — bij wijziging stale-mark lopende seeds.
- **Deployment**: gegenereerde `data/concept_records/` + `data/chroma_db/` (incl. `concepten`-collection) worden meegedeployed met de tutor-app. Tutor draait wel op de Anthropic API in productie (runtime chat), maar bouwt geen concepten meer op.
