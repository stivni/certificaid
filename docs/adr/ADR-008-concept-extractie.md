# ADR-008: Concept-extractie

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-08 (twee revisies — eerst: geen-API-tijdens-build, kenniselement-gestuurde retrieval, live duplicate-check, variabel record-aantal. Daarna: bi-only retrieval als default, PO-niveau batching, just-in-time chunk loading, synoniem-via-LLM, embedding-daemon integratie)

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

#### A. Vermoedensruimte — op programmaonderdeel-niveau

Vermoedensruimte werkt op **PO-niveau, niet per taakblok**. Reden: concept = fenomeen, vakoverschrijdend is regel (ADR-007 designprincipe 1). Een vermoeden zoals "beroepsgeheim" hoort bij heel deontologie, niet bij D1.1 of D1.2 apart. Splitsen per taakblok zou dezelfde vermoedens 2-3× laten verschijnen, met merge-werk downstream.

Subagent (in Claude Code) krijgt:
- Programmaonderdeel-titel + parent-context
- **Heel programmaonderdeel**: alle taakblokken met hun taken + doelstellingen + kenniselementen
- Conceptmodel-schema (node-types + edge-types)
- Concept-schrijfregels (`docs/concept-schrijfregels.md`) inclusief de "Wat is een concept?"-sectie
- Lijst van bestaande concept-naburen (om duplicatie te vermijden)

**Token-budget**: een PO-input is typisch 5–15 KB (titels + 3-10 taakblokken × KE-teksten). Output 50–150 vermoedens × ~200 tokens ≈ 10–30K. Totale call ~30–50K tokens — fractie van Opus' 200K. Geen issue.

Output per vermoeden — **gestructureerd schema** (verplicht voor downstream stappen):

```json
{
  "naam": "<volledige naam, simpele taal>",
  "node_type": "<11 types, of voorgesteld:<naam>>",
  "rationale": "<één zin: waarom dit concept hier relevant is>",
  "taakblokken": ["4.0.D1.1", "4.0.D1.2"],            // 1+ verplicht — multi voor vakoverschrijdend
  "taken_doelstellingen": ["4.0.D1.1.taak.1", "..."], // optioneel, multi
  "kenniselementen": ["4.0.I.D.7", "..."],            // optioneel, multi
  "synoniemen": ["geheim toevertrouwd", "..."],       // 3–5 voor query-time retrieval-expansion
  "schaal_signaal": "<klein|middel|groot>"            // hint voor granulariteit
}
```

50–150 vermoedens per programmaonderdeel (afhankelijk van PO-grootte). **Geen main_rule/exceptions** in deze fase — pure vermoedensruimte.

**Multiplicity-regels**:
- `taakblokken`: 1+ verplicht. Een vermoeden hoort bij minstens één taakblok; mag bij meerdere als het cross-block-relevant is.
- `taken_doelstellingen`: leeg toegestaan (pure begrippen zonder taak-anker).
- `kenniselementen`: leeg toegestaan (pure procedure/skill zonder KE-anker).
- `synoniemen`: 3–5 aanbevolen voor goede retrieval-expansion; lege lijst toegestaan als de canonische naam zelf overal voorkomt in bronteksten.

LLM mag een **niet-voorgedefinieerd node-type voorstellen** (`node_type: "voorgesteld:<naam>"`). Voorgestelde types verzamelen in review-queue (ADR-007).

#### B. Multi-level retrieval

Per vermoeden retrieval op vijf niveaus tegen `bronnen`-collection (ADR-006). Niveau 3 is optioneel (alleen als vermoeden kenniselementen koppelt):

1. **Programmaonderdeel-niveau**: programmaonderdeel-titel + samenvatting → brede thematische context
2. **Taakblok-niveau**: taken + doelstellingen + kenniselementen samen → mid-level
3. **Kenniselement-niveau** (optioneel): tekst van elk gekoppeld kenniselement (incl. parent + subitems) → formele scope-anker. **Skipt** als `kenniselementen` leeg is.
4. **Vermoeden-niveau**: vermoeden-naam + rationale → granulair, concept-specifiek
5. **Synoniem-niveau** (LLM-gegenereerd): query-time expansion via `vermoeden.synoniemen[]` → overbrugt vocabulairekloven

Per vermoeden: combineer chunks uit alle niveaus, dedupliceer op chunk-id, top-N (~20) doorgeven aan stap C.

**Waarom kenniselement-niveau apart**: een kenniselement zoals `4.0.I.D.7 Beroepsgeheim` is een formele scope-anker; zijn tekst hint vaak naar de exacte wetsartikelen. Zonder dit niveau zit retrieval te dicht op de generieke vermoeden-naam en mist het gezagsbron-passages.

**Waarom synoniem-niveau via LLM**: bi-encoder-embeddings overbruggen niet altijd vocabulairekloven tussen canonische termen en juridische omschrijvingen. Voorbeeld: "beroepsgeheim" matcht zwak op art. 458 SW dat spreekt van "geheimen die hun zijn toevertrouwd". De vermoedensruimte-LLM voegt 3–5 synoniemen toe aan elk vermoeden (zie `prompts/vermoedensruimte-v1.md`); die worden als extra sub-queries gevoerd. Geen handmatige keyword-curatie, geen index-time augmentatie — query-time expansion via het LLM dat het vermoeden zelf bedacht.

**Retrieval-modus — bi-only als default, rerank optioneel**:

| Modus | Wanneer | Snelheid | Output `rerank_score` |
|---|---|---|---|
| **Bi-only** (default) | Build-pipeline op CPU/MPS | ~2 sec/vermoeden | `-1.0` (sentinel) |
| **Single-pass rerank** | Productie-rebuild op GPU/MPS | ~5–10 sec/vermoeden | 0.0 – 1.0 |

Reden voor bi-only default: cross-encoder (bge-reranker-v2-m3) loopt 15+ min/vermoeden op CPU — onpraktisch. MPS doet 5–10 sec/vermoeden maar vereist een ingerichte Mac met voldoende geheugen. Default = bi-only, optie via `--no-rerank` weglaten.

**Drempels voor relevantie-check** (zie §C.2):

| Modus | Top score | Actie |
|---|---|---|
| rerank | ≥ 0.50 | `seed` |
| rerank | 0.30–0.50 | `seed` met "zwak gegrond"-notitie |
| rerank | < 0.30 | `rejected` |
| bi-only | ≥ 0.25 | `seed` |
| bi-only | 0.20–0.25 | `seed` met "zwak gegrond"-notitie |
| bi-only | < 0.20 | `rejected` |

Bi-only drempels zijn lager omdat bi-encoder-cosine-scores in een ander bereik zitten (typisch 0.15–0.40 voor relevant materiaal; 0.25 = solide).

Implementatie: `multi_query_retrieve` in `tools/lib/retrieval.py` + `bi_only_retrieve` / `single_pass_rerank` in `tools/extractie/retrieve_batch.py`.

#### B-bis. Bestandstructuur — één vermoedens-bestand, één retrieval-bestand per PO

Vermoedensruimte (§A) werkt op PO-niveau, dus zowel vermoedens als retrieval leven als **één bestand per programmaonderdeel**:

```
data/extractie/<po>/vermoedens/<po>.json   ← LLM-output, gegit, hergebruikbaar
data/extractie/<po>/retrieval/<po>.json    ← bi-encoder-output, ephemeral (§7)
```

**Geen** combine-stap nodig — vermoedensruimte produceert al de PO-aggregaat.

**Twee-niveau-rationale**:

| Niveau | Bestand | Levensduur | Waarom apart? |
|---|---|---|---|
| Vermoedens | `vermoedens/<po>.json` | Persistent (gegit) | Cache van dure LLM-call. Hergebruikbaar bij bron-/index-updates zonder LLM te hervragen. |
| Retrieval | `retrieval/<po>.json` | Ephemeral | Reproduceerbaar uit vermoedens + index. Mag in `.gitignore`. |

**Eén Opus-agent per PO** verwerkt de 50–150 vermoedens sequentieel. Cross-taakblok-context-accumulatie verbetert de kwaliteit:
- Edge-resolutie: een vermoeden uit D1.2 kan een dangling-target uit D1.1 oplossen.
- Terminologie-consistentie: dezelfde term gekozen voor "beroepsbeoefenaar" / "accountant" door alle blokken.
- Duplicate-detectie: vakoverschrijdende fenomenen (zoals "beroepsgeheim" met `taakblokken: ["4.0.D1.1", "4.0.D1.2"]`) worden eenmaal verwerkt.

##### Schema per vermoeden-record in retrieval-bestand

`retrieve_batch.py` neemt **alle velden** uit het vermoedens-bestand over en voegt `chunks[]` toe. Geen impliciete velden-filter:

```json
{
  "naam": "...",
  "node_type": "...",
  "rationale": "...",
  "taakblokken": ["4.0.D1.1", "4.0.D1.2"],
  "taken_doelstellingen": [...],
  "kenniselementen": [...],
  "synoniemen": [...],
  "schaal_signaal": "...",
  "chunks": [...]
}
```

**Bewaar-alle-velden-regel**: een toekomstig vermoeden-veld (bv. `verwante_concepten[]`, `prioriteit`, ...) wordt **automatisch** meegenomen mits `retrieve_batch.py` shallow-copy doet ipv hardcoded veld-witte-lijst.

Top-level structuur van het retrieval-bestand:

```json
{
  "po": "4.0",
  "vermoedens": [
    { ... vermoeden-record + chunks ... },
    ...
  ]
}
```

#### C. Seed-records bouwen

Subagent (één Opus-agent per programmaonderdeel) verwerkt vermoedens **één voor één**, met deze flow per vermoeden:

1. **Live duplicate-check** tegen bestaande concepten:
   - Embed vermoeden (naam + rationale) → query `concepten` ChromaDB-collection via embedding-daemon (zie ADR-018)
   - Top-1 score > 0.80 → mogelijk duplicaat → subagent beslist expliciet:
     - **Merge**: voeg eventuele nieuwe info toe aan bestaand record, log als alias
     - **Distinct**: motiveer waarom dit toch een ander concept is (dan toch nieuwe seed)
   - Tussen 0.65–0.80 → grijze zone, subagent meldt expliciet in log
   - < 0.65 → veilig nieuw concept

2. **Relevantie-check** (anti-hallucinatie): zie §B drempel-tabel — bi-only of rerank-modus bepaalt de drempelwaarden.

3. **Seed-record schrijven** wanneer relevantie-check passeert en geen merge:
   - `id`, `naam`, `node_type`, top-level `_provenance` (record-metadata)
   - **Type-specifiek hoofdveld** (zie ADR-007 §"Type-specifieke sleutelvelden"): `main_rule` voor `regel`/`beginsel`/`drempel`, `definitie` voor `begrip`/`actor`/`fenomeen`, `verplichting`+`stappen[]` voor `procedure`, `doel`+`bouwstenen[]` voor `methode`/`afwegingskader`, etc.
   - Elk veld is een block-object met `text`, `confidence`, `source`, optioneel `references[]`, en inline `_provenance`
   - Initiële `edges` (mogelijk `_dangling: true`) — let op edge-richting-conventie (ADR-007)
   - Status: `seed`
   - Velden die niet gerechtvaardigd zijn blijven leeg — sparse is de norm (ADR-007)
   - **Just-in-time chunk loading**: agent leest chunks pas wanneer hij naar dit vermoeden toekomt (`Read`-tool op het retrieval-bestand met range-filter), niet vooraf. Voorkomt context-explosie bij PO's met 100+ vermoedens.

4. **Onmiddellijk indexeren** via embedding-daemon: nieuwe concepten worden direct embedded en in `concepten`-collection geschreven, zodat het volgende vermoeden ze in stap 1 kan terugvinden.

5. **Programmaonderdeel-JSON updaten**: voeg de nieuwe concept-id toe aan `kenniselementen[<code>].concepten` voor elk kenniselement dat het concept afdekt (ADR-002). Ook voor taken/doelstellingen-concepten via `taakblokken[].taken[].concepten` of `taakblokken[].doelstellingen[].concepten`.

#### Variabel record-aantal: agent mag splitsen / mergen / rejecteren / toevoegen

Vertrek met N vermoedens per taakblok, eindig met M ≷ N records. De subagent mag:
- **Mergen**: twee vermoedens blijken hetzelfde concept → één record (live duplicate-check)
- **Splitsen**: één vermoeden bevat eigenlijk twee fenomenen → twee records
- **Rejecteren**: vermoeden niet gegrond in bronnen → géén record (relevantie-check)
- **Toevoegen** (dangling-resolutie): main_rule verwijst naar concept dat nog niet bestaat → extra seed voor de target

Beslissingslog per run: `data/extractie/<po>/seed_log_<po>.json` met per vermoeden de beslissing (`kept`/`merged_into:<id>`/`rejected:reason`/`split_into:[id, id]`) + duplicate-check rerank-scores. Dit is mens-curatie input.

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

### 2-bis. Coverage gap-fill (na PO-extractie)

Na een PO-batch-run draait `tools/lib/coverage.py --po <code> --gaten` en rapporteert kenniselementen die door 0 concepten gedekt zijn. Twee scenario's:

- **Echte gaten** (KE niet behandeld): vermoedensruimte-LLM heeft het gemist of het schaalvol-signaal was te breed. → tweede vermoedensruimte-ronde **gericht op die KE**, gevolgd door retrieval + extractie.
- **Verkapte dekking** (concept dekt KE maar koppeling ontbreekt in PO-JSON): handmatige PO-JSON-update om de koppeling toe te voegen.

**Belangrijk**: kenniselementen → concepten is geen 1:1-mapping. Eén KE als "Begrip witwaspraktijk en terrorismefinanciering" kan 3+ concepten genereren. Eén concept als "beroepsgeheim" kan over meerdere KEs spannen. De vermoedensruimte-prompt moet die meervoudigheid expliciet uitnodigen ("voor elk kenniselement, lijst alle fenomenen die nodig zijn om het te kennen") — geen plafond op aantal vermoedens.

Future: `tools/extractie/gap_vermoedens.py` automatiseert "lees coverage-rapport, bouw gerichte vermoedens voor ongedekte KEs" als helper-script. Niet in initiële Fase 3 — eerst een complete PO afmaken om patronen te zien.

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

### 6. Per-veld provenance — inline (schema 1.1)

Vanaf schema-versie 1.1 (ADR-007 changelog 2026-05-08) leeft `_provenance` **inline per veld**, niet langer als top-level dictionary. Top-level `_provenance` blijft, maar enkel voor record-metadata (`extractor_run`, `model`, `reviewed_by`).

```json
{
  "main_rule": {
    "text": "...",
    "confidence": "grounded",
    "source": { ... },
    "_provenance": {
      "inputs": [{"id": "Antiwitwaswet-2017__art_5", "sha256": "<chunk_sha>", "version": "rag-v1"}],
      "extracted_at": "2026-05-08T12:00:00Z",
      "extractor": "seed-v1"
    }
  },
  "exceptions": [
    {
      "text": "...",
      "_provenance": { "inputs": [...] }
    }
  ]
}
```

Zie ADR-007 §"Provenance — inline per veld" voor volledige spec.

Bij **bron-update** (chunk-content-hash verandert) → `mark_stale.py` walkt block-level: welke velden in welke concept-records hebben deze chunk-id? → die velden worden `stale: true`. Andere velden in hetzelfde concept blijven valide. Re-extraction-queue verzamelt stale velden.

Vereist **chunk-id-stabiliteit** (ADR-006 §3.1, ADR-004).

**Implementatie-status (2026-05-08)**: het schema voorziet `sha256`, maar de huidige extractor laat dat veld op `null`. Daarmee is staleness-detectie nog onmogelijk. Invullen van `sha256` met `chunk_sha` uit ChromaDB-metadata is een implementatie-eis voor de eerstvolgende extractie-tooling-iteratie.

### 7. Permanent vs ephemeral provenance-artefacten

Twee artefacten dragen tijdens extractie chunk-verwijzingen:

| Artefact | Locatie | Levensduur | Status |
|---|---|---|---|
| **Vermoeden** + **retrieval-resultaat** | `data/extractie/<po>/{vermoedens,retrieval}/*.json` | tijdelijk — extractie-hulpmiddel | ephemeral |
| **Concept-record `_provenance`** | `data/concept_records/<id>.json` | permanent — duurzame kennislaag | authoritative |

**Beslissing**: de permanente provenance leeft uitsluitend in concept-record `_provenance`-velden. Vermoeden- en retrieval-JSONs zijn een wegwerpbaar tussenstadium dat opgeruimd mag worden zodra een vermoeden ofwel verworpen is, ofwel opgenomen in een concept-record met `status >= partieel`.

Implicaties:

- **Dependency-analyses werken op concept-records, niet op retrieval-JSONs.** Bijvoorbeeld: `tools/etl/remove_bron.py` Laag 2 (zie ADR-005 §5) scant `data/concept_records/**` voor inline-provenance-velden (vanaf schema 1.1: `<veld>._provenance.inputs[].id` per block; eerdere records met top-level `_provenance.<veld>.inputs[].id` blijven leesbaar via een compat-helper) op zoek naar chunk-IDs die op de te verwijderen bron wijzen — niet `data/extractie/.../retrieval/*.json`. Een retrieval-JSON die toevallig nog bestaat is bonusinformatie, geen vereiste.
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
  - `tools/extractie/retrieve_batch.py` — leest het PO-vermoedens-bestand, doet 5-niveau retrieval per vermoeden, schrijft één PO-retrieval-bestand. Embedding via daemon (ADR-018). Shallow-copy van vermoeden-velden naar output (geen hardcoded witte-lijst).
  - `tools/extractie/normalize_vermoedens.py` — legacy helper: bestond om singular `gekoppeld_aan` om te zetten naar arrays. Met de nieuwe vermoedensruimte-prompt (PO-niveau, multi-anker-arrays) is deze overbodig — de LLM produceert al het juiste schema. Kan verwijderd of gemarkeerd `archive/` na migratie.
  - `tools/extractie/index_concept_incremental.py` — daemon-client; embed één concept-record en upsert in `concepten`-collection via daemon
  - `tools/extractie/queue.py` — dangling-edges → seed-queue
  - **Geen `anthropic` import** in deze scripts. Geen LLM-calls.
- **LLM-werk** gebeurt door een Claude Code subagent in dev-omgeving die deze helpers via Bash-tool aanroept en zijn eigen reasoning gebruikt voor synthese. **Eén agent per programmaonderdeel** verwerkt alle vermoedens van het PO sequentieel — cross-taakblok-context-accumulatie is een kwaliteitsfactor.
- `tools/lib/coverage.py` — bouwt op aanvraag een reverse-index (concept → kenniselementen) uit programmaonderdeel-JSON's voor dekkingsrapporten. Geen state op concepten zelf (ADR-002, ADR-007).
- Per-veld provenance + per-veld stale-marking maakt incremental re-runs **veld-precies** (alleen stale velden herextraheren, niet hele concept-records).
- **Implementatie-eisen voor §6 + §7** (TODO):
  - Concept-extractor moet `chunk_sha` uit ChromaDB-metadata kopiëren naar `_provenance.<veld>.inputs[].sha256` (nu `null`).
  - `tools/etl/mark_stale.py` voor concepten bouwen: vergelijk opgeslagen `sha256` met live ChromaDB `chunk_sha`; flag mismatches.
  - `tools/etl/remove_bron.py` Laag 2 omzetten: scan `data/concept_records/**/_provenance.*.inputs[].id` (i.p.v. `data/extractie/.../retrieval/*.json`) voor chunk-impact-analyse.
- Voorbeeldexamens worden vroeg gestructureerd (`data/voorbeeldexamens/`) als ground truth — maar pas in Fase 5 als extractie-input gebruikt.
- Concept-schrijfregels (`docs/concept-schrijfregels.md`) zijn input voor elke subagent-invocatie. Schrijfregels evolueren — bij wijziging stale-mark lopende seeds.
- **Deployment**: gegenereerde `data/concept_records/` + `data/chroma_db/` (incl. `concepten`-collection) worden meegedeployed met de tutor-app. Tutor draait wel op de Anthropic API in productie (runtime chat), maar bouwt geen concepten meer op.
