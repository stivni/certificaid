# ADR-007: Conceptmodel

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-08 (schema 1.1 — type-specifieke sleutelvelden, `references[]`, inline provenance, edge-richting-conventie)
**Vervangt**: archive/ADR-006 (drie-lagenmodel — concept-laag absorbeert), archive/ADR-009 (concept-record-schema v2)
**Schema-versie**: 1.1 (was 1.0 in eerste draft)

## Changelog

- **2026-05-15 (1.2)** — Patroon-driven uitbreiding (additief, geen breaking
  changes). Quality-check op PO 1.4 + ADR-009 patroon-labeling op 188 examenvragen
  + coverage-analyse over 15 complexiteitspatronen onthulden structurele kennis-
  vormen die v1.1 niet gestructureerd hield. **Zes** nieuwe optionele named
  fields (consistent met v1-naming-pattern, niet via generic container):

  - `oorzaken[]` — voor patroon "geef N oorzaken van X". Aggregeer cross-bron;
    nieuwe confidence-waarde `"inferred-from-aggregation"` voor synthese-claims.
  - `drempelwaarden[]` — kritische numerieke grenzen met juridisch gevolg
    (`naam`, `waarde`, `eenheid`, `gevolg`). Kan ook categorisering-criteria
    bevatten (drempel = criterium, niet alleen getal).
  - `tijdlijn[]` — wettelijke termijnen voor procedurele concepten
    (`stap`, `termijn`, `actor`, `actie`).
  - `vergelijkingsparen[]` — concepten die met andere verward worden
    (`vergelijking_met`, `verschil`, `trigger`).
  - `berekeningsmethode[]` — voor 23% van examenvragen (28 berekening + 16
    open-berekening-motiveer). Block met `naam`, `formule`, `ratio`, `stappen[]`
    (algemene methode-stappen), optioneel `concreet_voorbeeld` (sub-block met
    scenario + berekening + resultaat).
  - `in_praktijk[]` — concrete invulling van het abstract begrip / handeling.
    Eén veld voor twee gebruiken (afhankelijk van node-type):
    * Voor `begrip` / `actor` / `fenomeen`: praktische kenmerken ("hoe herken
      je een coöperatief karakter? wisselende leden, stemrecht per persoon, ...").
    * Voor `regel` / `procedure` / `methode`: concrete handelingen ("wat doet
      de accountant bij alarmbel?").
    Block-shape: `aspect`, `betekenis`, optioneel `herkenningspunt`,
    `wereld_voorbeeld`, source, provenance.

  **Stappen[]-shape uitgebreid**: optioneel `actor`-veld voor
  procedure-records (`complex-procedure-rol-bevoegdheid`-patroon vraagt
  "wie doet wat").

  **Niet** toegevoegd (overlap met bestaande velden):
  - `verborgen_vereiste[]` — overlap met `valkuilen[]` (v1). Prompt v2
    instrueert in plaats daarvan om `valkuilen[]` actiever te vullen met die
    impliciete kennis (red-herring-elementen, verborgen vereisten, vaak-
    foutgedaan-stappen).
  - `enumeraties[]` generic container — overbodig, named fields werken al.
  - `rekenvoorbeelden[]` (case-only) — vervangen door `berekeningsmethode[]`
    (methode + optioneel voorbeeld; methode is herhaalbaar mentaal recept).
  - `praktijk_kenmerken[]` + `praktijk_handelingen[]` (twee aparte velden) —
    samengevoegd tot één `in_praktijk[]`-veld met flexibele shape.

  Examen-specifieke metadata (gewicht, vraagvorm-frequentie) hoort NIET in
  concept-records — dat zit in `examenfocus`-objecten (ADR-009).

- **2026-05-08 (1.1)** — Eerste seed-record (`clientacceptatiebeleid.json`) onthulde drie schema-tekortkomingen die hier rechtgezet worden:
  1. `main_rule` werd voor álle node-types gebruikt — semantisch fout voor `procedure`, `methode`, `afwegingskader`. Type-specifieke sleutelvelden vastgelegd (zie §"Type-specifieke sleutelvelden").
  2. Designprincipe 7 ("verwijzingen als gestructureerde child-property") was abstract — agent gooide artikelnummers inline in prose. Concrete `references[]`-blok-spec toegevoegd.
  3. `_provenance` zat als losstaand top-level blok — moeilijk te onderhouden bij velduitbreiding. Inline `_provenance` per veld; top-level alleen voor record-metadata.
  4. Edge-richting was impliciet (`getriggerd-door` werd in fout-richting gebruikt). Expliciete conventie vastgelegd.

## Context

Een concept = een **tijdloos studieonderwerp** (een fenomeen), niet een wetsartikel en niet een vakindeling. Een eerdere poging met een plat schema (`main_rule` / `exceptions` / `obligations` / `pitfalls`) kraakte op de diversiteit van de ITAA-domeinkennis: een definitie is geen procedure, een drempel is geen casus, een beginsel vergt oordeel terwijl een regel een verplichting is. Het examen toetst vooral **relaties** tussen die soorten kennis.

Een uniform schema kan dat niet vasthouden. Een **getypeerde knowledge graph** wel: nodes per kennis-type met type-specifieke velden, verbonden door getypeerde edges met conditie- en scope-velden.

## Beslissing

### Architectuur

- **Nodes** = JSON-files in `data/concepten/records/<id>.json` (één file per node)
- **Edges** = uitgaande velden binnen de bron-node
- **Walking** via NetworkX (in-memory laden, walks in milliseconden, ~500–1500 nodes verwacht)
- **Vector-zoek** via ChromaDB-collection `concepten` (ADR-006); edges meegedragen als metadata
- **Schema-evolutie** = veld toevoegen, geen migrations. Sparse fields zijn de norm.
- **Open node- en edge-typering** — de initiële lijsten (zie onder) zijn geen limiet. Tijdens extractie mag een nieuw type voorgesteld worden via `node_type: "voorgesteld:<naam>"` of een edge-type `voorgesteld:<naam>`. Voorgestelde types worden verzameld in `data/concepten/records/_voorgestelde_types.yaml` voor menselijke review; pas na akkoord wordt het schema gebumpt en records hernoemd.

### Designprincipes

1. **Concept = fenomeen**, niet artikel of vakindeling. Vakoverschrijdend is de regel.
2. **Sparse fields** zijn norm; partiële records zijn geldig.
3. **Schema-evolutie** = veld toevoegen. Schema-versie per record (`schema_version`); wijzigen schema → records `stale` (ADR-004).
4. **Accountant-taal in hoofdtekst** — actief, direct, met concrete situaties. Juridisch jargon enkel in `source.citation`.
5. **Voorbeelden in eigen veld** (`voorbeeld_inline`), niet in `definitie`/`tekst`. Casus-nodes blijven enkel voor échte gevallen (jurisprudentie, voorbeeldexamenvraag, CBN-advies-feitenset).
6. **Compositie boven duplicatie — opt-in**. Default sub-stap = inline. Aparte node alleen als twee procedures écht dezelfde sub raken.
7. **Verwijzingen als gestructureerde child-property**, niet inline in prose. Cross-references staan als getypeerde edge-velden direct op het blok. Detectie en lifting tijdens concept-extractie (ADR-008), niet tijdens chunking.
8. **Edges op block-level** mogelijk (binnen een specifieke regel-tekst, een uitzondering, één procedure-stap). NetworkX-laden tilt block-edges automatisch op naar node-niveau voor walks; block-anker blijft bewaard voor display.

### Node-types (initieel 11, mag groeien)

`begrip` · `regel` · `beginsel` · `procedure` · `methode` · `drempel` · `skill` · `casus` · `afwegingskader` · `actor` · `fenomeen`

### Type-specifieke sleutelvelden

Elk node-type krijgt een hoofdveld dat past bij de aard van de kennis. **`main_rule` is exclusief voor verplichtings-types**; voor andere types is het geen escape-hatch.

| Node-type | Hoofdveld | Secundaire structuur | Toelichting |
|---|---|---|---|
| `begrip`, `actor`, `fenomeen` | `definitie` | — | Wat is dit ding? |
| `regel`, `beginsel` | `main_rule` | — | Wat is de verplichting/het principe? |
| `drempel` | `main_rule` (de drempelregel) | `waarde` (het getal/criterium) | "Boven X EUR moet je Y doen." |
| `procedure` | `verplichting` (waarom moet je dit doen) | `stappen[]` (geordende lijst) | Lineair recept met meetbare stappen |
| `methode` | `doel` (waartoe dient deze methode) | `bouwstenen[]` of `criteria[]` | Aanpak/techniek met componenten |
| `afwegingskader` | `doel` | `bouwstenen[]` (afwegingsdimensies) | Beslisruimte; geen vast recept |
| `casus` | `feiten`, `uitspraak` | — | Concreet geval (jurisprudentie, voorbeeldexamen-feitenset) |
| `skill` | `omschrijving` | `subvaardigheden[]` | Vaardigheid met eventuele componenten |

Elk hoofdveld is een **block-object** (zelfde shape: `text` + `confidence` + `source` + optioneel `references[]` + `_provenance`). Stappen, bouwstenen en subvaardigheden zijn arrays van zulke blocks met optioneel een extra veld (`volgorde` voor stappen).

**Schema-fragment voor type-specifieke velden:**

```json
{
  "node_type": "procedure",
  "verplichting": {
    "text": "<korte zin: wie moet dit volgen en waarom>",
    "confidence": "grounded",
    "source": { ... },
    "references": [ ... ],
    "_provenance": { "inputs": [...] }
  },
  "stappen": [
    {
      "volgorde": 1,
      "text": "<wat de uitvoerder doet in deze stap>",
      "outcome": "<wat het resultaat is dat de volgende stap voedt>",
      "confidence": "grounded",
      "source": { ... },
      "references": [ ... ],
      "_provenance": { "inputs": [...] }
    }
  ]
}
```

```json
{
  "node_type": "afwegingskader",
  "doel": {
    "text": "<wat dit kader moet bewerkstelligen>",
    "confidence": "grounded",
    "source": { ... }
  },
  "bouwstenen": [
    {
      "naam": "<korte label, bv. 'Risico-inschatting'>",
      "text": "<wat deze bouwsteen behelst>",
      "confidence": "grounded",
      "source": { ... },
      "_provenance": { "inputs": [...] }
    }
  ]
}
```

### Patroon-driven optionele velden (schema 1.2, additief)

Elk node-type kan onderstaande optionele velden bevatten als de bron-bundle ze ondersteunt. **Sparse fields zijn de norm** — een record met enkel `definitie` is volledig geldig.

**V1-velden (reeds in gebruik, blijven onveranderd)**: `voorwaarden[]`, `uitzonderingen[]`, `valkuilen[]`, `voorbeeld_inline`, `bouwstenen[]`, `stappen[]`, `voorwaarden_toepassing[]`.

**V1.2 nieuwe velden** (6 stuks, named fields i.p.v. generic container):

- **`oorzaken[]`** — items met cross-bron aggregatie voor "N voornaamste oorzaken van X". Confidence `"inferred-from-aggregation"` voor synthese-claims; provenance lijst alle bron-chunks.
- **`drempelwaarden[]`** — kritische numerieke grenzen of categorisering-criteria (`naam`, `waarde`, `eenheid`, `gevolg`).
- **`tijdlijn[]`** — wettelijke termijnen voor procedurele records (`stap`, `termijn`, `actor`, `actie`).
- **`vergelijkingsparen[]`** — concepten die met andere verward worden (`vergelijking_met`, `verschil`, `trigger`).
- **`berekeningsmethode[]`** — recept voor rekenkundige toepassing (`naam`, `formule`, `ratio`, `stappen[]`, optioneel `concreet_voorbeeld`). Voor procedures, methoden, en regels met numerieke output.
- **`in_praktijk[]`** — concretisering van het concept. Eén veld voor begrip-typen (praktische kenmerken/herkenningspunten) én voor regel-typen (handelingen + output). Block: `aspect`, `betekenis`, optioneel `herkenningspunt`, `wereld_voorbeeld`, source, provenance.

**Stappen[]-shape uitbreiding (v1.2)**: optioneel `actor`-veld per stap voor procedure-rol-bevoegdheid-patroon.

Het bestaande `valkuilen[]`-veld wordt in prompt v2 actiever gebruikt voor verborgen vereisten, red-herring-elementen en vaak-foutgedaan-stappen — geen aparte velden voor deze patronen.

Zie `prompts/concept-extractie-v2.md` voor exacte block-shapes en voorbeelden.

### Edge-types (initieel ~20, mag groeien)

`definieert` · `regelt` · `uitzondering-op` · `primeert-boven` · `getriggerd-door` · `vereist-kennis-van` · `toegepast-via` · `voorbeeld-van` · `bevat` / `onderdeel-van` · `vervangt` / `vervangen-door` · `bedreigt` / `bedreigd-door` · `ratio` · `alternatief-voor` · `schakelt-over-naar` · `gemeten-met` / `instrument-van` · `vernietigt-deel-van` · `contrasteert-met` · `van-toepassing-op`

Optionele velden op edges: `scope`, `conditie`, `scharnier`, `redenering`, `aspect`, `_dangling`, `notities[]`.

### Edge-richting — expliciete conventie

Edges leven op de **bron-node** (de node die de edge declareert) en wijzen naar een **target-node**. De richting volgt deze regels:

- **`X getriggerd-door Y`** → Y is de aanleiding, X is de actie/respons. Lees als "X wordt geactiveerd door Y". Op X verklaard.
- **`X schakelt-over-naar Y`** → wanneer voorwaarde voldaan is gaat de uitvoerder van X naar Y. Op X verklaard.
- **`X uitzondering-op Y`** → X is de uitzondering, Y is de hoofdregel. Op X verklaard.
- **`X bevat Y`** → Y is een sub-onderdeel van X. Op X verklaard.
- **`X onderdeel-van Y`** → omgekeerde van bovenstaande. Op X verklaard.
- **`X vereist-kennis-van Y`** → om X te begrijpen moet je Y kennen. Op X verklaard.
- **`X van-toepassing-op Y`** → X (regel/methode) wordt gebruikt op Y (cliënten/situaties). Op X verklaard.

Bij twijfel: stel de edge-naam in een actieve zin met X als onderwerp ("X *getriggerd-door* Y" = "X wordt getriggerd door Y"). Als de richting niet klopt, kies een ander edge-type of zet de edge op de andere node.

**Code-fout uit eerste seed-record** (illustratief): `Cliëntacceptatiebeleid getriggerd-door Meldingsplicht-CFI` werd geschreven, maar de bedoeling was "het beleid leidt soms tot meldingsplicht-overweging". Correct: `Cliëntacceptatiebeleid schakelt-over-naar Meldingsplicht-CFI` met `conditie` = "wanneer waakzaamheid niet uitvoerbaar is".

### Bronverwijzing — gestructureerd

Twee structuren:

**1. `source`** (per veld) — de **primaire bron** waarvan de tekst van het veld afgeleid is. Eén per veld.

```json
"source": {
  "type": "wet" | "kb" | "itaa-norm" | "cbn-advies" | "isa" | "jurisprudentie" | "voorbeeldexamen",
  "short": "AWW art. 47 §1",
  "ref": { ... },        // type-specifieke deelvelden
  "citation": "exact quote (optioneel)"
}
```

**2. `references[]`** (per veld, optioneel) — **secundaire pointers** naar onderliggende passages die de hoofdtekst impliceert maar niet uitschrijft. Operationaliseert designprincipe 7 ("verwijzingen als gestructureerde child-property, niet inline in prose").

```json
"references": [
  {
    "rol": "<grondslag|voorbeeldgeval|definitie-van-term|uitzondering-op-uitzondering|...>",
    "passage": "<korte beschrijving wat in deze referentie staat>",
    "source": { ... }
  }
]
```

**Wanneer `references[]` ipv inline in tekst**: als de hoofdtekst dreigt artikelnummers te bevatten ("voor de gevallen bedoeld in artikelen 37 tot 41 AWW"), parafraseer de inhoud in de tekst en lift de artikelverwijzing naar `references[]` met een korte uitleg wat daar staat. **Lift-rule**: artikelnummers/normpunten in prose zijn een smell; ze horen in `references[]`.

**Voorbeeld** — een uitzondering op het cliëntacceptatiebeleid:

```json
{
  "text": "Cliënten met een hoog risicoprofiel mogen pas worden aanvaard na een passend onderzoek én na akkoord op een geschikt hiërarchisch niveau (bv. een vennoot of compliance-officer). Dit geldt voor cliënten of verrichtingen die volgens de algemene risicobeoordeling als hoog risico zijn aangeduid, en voor situaties die de wet als hoog risico aanmerkt: politiek prominente personen, derde landen met hoog risico, en complexe of ongebruikelijke verrichtingen zonder duidelijk economisch doel.",
  "confidence": "grounded",
  "source": { "type": "itaa-norm", "short": "ITAA-norm AWW (richtlijn BIBF) punt 4.2", ... },
  "references": [
    {
      "rol": "grondslag-hoog-risico",
      "passage": "Risicocategorieën vastgesteld op grond van de algemene risicobeoordeling",
      "source": { "type": "wet", "short": "AWW art. 19 §2", ... }
    },
    {
      "rol": "wettelijk-aangeduide-hoogrisico-gevallen",
      "passage": "Verhoogde waakzaamheid: PEPs, derde landen met hoog risico, ongebruikelijke complexe verrichtingen",
      "source": { "type": "wet", "short": "AWW art. 37-41", ... }
    }
  ]
}
```

### Provenance — inline per veld

Elk block-veld krijgt een eigen `_provenance`-sub-object met de chunk-ids die het LLM voor dit veld gebruikt heeft. Top-level `_provenance` blijft, maar **alleen voor record-metadata** (run-id, schema_version, tijdstip).

**Per veld:**
```json
"main_rule": {
  "text": "...",
  "confidence": "grounded",
  "source": { ... },
  "_provenance": {
    "inputs": [{"id": "<chunk_id>", "sha256": "<chunk_sha>", "version": "rag-v1"}],
    "extracted_at": "2026-05-08T10:23:00Z",
    "extractor": "seed-v1"
  }
}
```

**Top-level (record-metadata):**
```json
{
  "id": "...",
  "naam": "...",
  "schema_version": "1.1",
  "_provenance": {
    "extractor_run": "seed-v1-2026-05-08T10:00:00Z",
    "model": "claude-opus-4-7",
    "reviewed_by": null
  }
}
```

**Voordelen** boven monolithisch top-level provenance:
- Block-level stale-flagging mogelijk: één chunk wijzigt → alleen velden die die chunk gebruikten worden `stale`.
- Schema-evolutie: nieuw veld toevoegen krijgt automatisch eigen provenance-slot.
- Visuele cohesion bij review: source + chunk-inputs van één veld staan fysiek bij elkaar.

**`sha256`-veld**: implementatie-eis. ChromaDB-metadata bevat `chunk_sha` (ADR-006 §3.1); de extractor moet die kopiëren naar `_provenance.<veld>.inputs[].sha256`. Niet ingevuld → staleness-detectie onmogelijk.

### Status-flow per node — welke velden in welke fase

| Status | Aangevulde velden (cumulatief) | Trigger naar volgende fase |
|---|---|---|
| `seed` | `id`, `naam`, `node_type`, `schema_version`, top-level `_provenance` (run-metadata), **type-specifiek hoofdveld** (zie §"Type-specifieke sleutelvelden") met inline `_provenance`, eventueel eerste `edges` | LLM-extractor heeft genoeg bron-context om uitzonderingen + scope te formuleren |
| `partieel` | + `exceptions`, `scope`, eerste batch `edges` (mogelijk dangling) | Edges grotendeels geresolveerd; bron-RAG levert geen nieuwe info op verdiepende queries |
| `gevuld` | + `pitfalls`, `voorbeeld_inline`, gerelateerde casussen | Menselijke review |
| `geverifieerd` | identiek; alleen status-flag | — |

Voorbeelden, valkuilen en cases worden **pas in `gevuld`** toegevoegd, niet in `seed` (zie ADR-008 voor extractie-volgorde).

`seed` ontstaat ofwel uit programma-/bron-gestuurde extractie, ofwel als dangling-target van een edge in een ander concept; `geverifieerd` vereist menselijke bevestiging.

### Confidence-labels — string-tags, geen emoji in data

Elke claim met confidence-veld:
```json
"confidence": "grounded"   // ⚖️ — direct traceerbaar naar bron in source.ref
"confidence": "inferred"   // 🤖 — LLM-gegenereerde redenering of synthese
```

Emoji (⚖️/🤖) zijn UI-/render-conventie (tutor, fiches, conversaties) — niet in JSON-data.

### Concept-laag is dependency-vrij naar boven

Concept-records bevatten **geen** verwijzingen naar programmaonderdelen, kenniselementen, taken, doelstellingen of examenvragen. Dependencies stromen één kant op (programma → concepten, examen → concepten). De koppeling kenniselement → concept leeft uitsluitend in de programmaonderdeel-JSON (zie ADR-002):

```json
// data/programma/programma.json (PO 4.0 = code "4.0" in dat bestand) — ENIGE WAARHEID
"kenniselementen": [
  {"deel": 1, "code": "4.0.I.D.7", "tekst": "Beroepsgeheim",
   "concepten": ["beroepsgeheim-gecertificeerd-accountant", "doorbreking-beroepsgeheim"]}
]
```

Concepten zijn zo portable — bij hervorming van het examenprogramma (codes herschikt) raakt de conceptenset niet.

**Bron-input via chunks** (provenance) is geen schending van deze regel: als een passage uit een voorbeeldexamen-toelichting of Mvt geciteerd wordt voor een concept-veld, gaat dat als chunk-id in `_provenance.inputs[]` — niet als examenvraag-link in een inhoudelijk veld. Het concept weet alleen "deze chunk is mijn bron"; chunk-metadata bepaalt of het een wettekst, norm of voorbeeldexamen-passage was.

Dekkingschecks die "welke kenniselementen dekt concept X af?" willen beantwoorden, bouwen op aanvraag een in-memory reverse-index uit programmaonderdeel-JSON's (`tools/lib/coverage.py`). Geen state op concepten zelf.

### Schrijfregels concept-content

Aparte content-conventie in [`docs/concept-schrijfregels.md`](../concept-schrijfregels.md). Bevat zowel **stijlregels** (taal, afkortingen, confidence-labels) als **conceptkeuze-regels** ("Wat is een concept?", "Wat is GEEN concept?", granulariteit, smell-tests). Wordt geladen bij prompt-opbouw voor de extractor en bij menselijke review.

Niet in deze ADR — schrijfregels zijn geen architectuurbeslissing.

### Vermoeden-schema (input voor concept-extractie, ADR-008)

Vermoedens (kandidaat-concepten) hebben een eigen lichtgewicht schema dat als input dient voor de seed-extractie. Vermoedensruimte werkt op **programmaonderdeel-niveau**, niet per taakblok — een vermoeden kan vakoverschrijdend zijn (designprincipe 1).

```json
{
  "naam": "<volledige naam>",
  "node_type": "<11 types of voorgesteld:<naam>>",
  "rationale": "<één zin: waarom relevant>",
  "taakblokken": ["4.0.D1.1", "4.0.D1.2", ...],     // 1+ verplicht
  "taken_doelstellingen": ["4.0.D1.1.taak.1", ...], // optioneel, multi
  "kenniselementen": ["4.0.I.D.7", ...],            // optioneel, multi
  "synoniemen": ["geheim toevertrouwd", ...],       // 3-5 aanbevolen; lege lijst geldig als canonische naam overal voorkomt
  "schaal_signaal": "<klein|middel|groot>"          // hint voor granulariteit
}
```

**Multiplicity is overal toegestaan**: één vermoeden kan bij meerdere taakblokken, meerdere taken/doelstellingen of meerdere kenniselementen horen. Geen artificiële 1-op-1-koppeling. `taakblokken` is verplicht als minstens-één-element-array (waar duikt het op?); de andere optionele anker-velden mogen leeg zijn voor pure procedurele taken (kenniselement leeg) of pure begrippen (taken_doelstellingen leeg).

Vermoedens leven in `data/extractie/<programmaonderdeel>/vermoedens/<programmaonderdeel>.json` — **één bestand per PO**, niet per taakblok. Top-level wrapper:

```json
{ "po": "<code>", "vermoedens": [ ... ] }
```

## Gevolgen

- `data/concepten/records/` = volledige conceptenset
- `tools/lib/graph.py` (nieuw) — NetworkX-laden, walks, dangling-detectie
- Schema-evoluties expliciet in `schema_version`-veld + ADR-changelog
- `tools/lib/cross_refs.py` — utility om referenties (`art. 33-35`, `§ 1`) te detecteren tijdens extractie (ADR-008)
- Bestaande concept-records (oud schema) krijgen `_provenance.stale: true` en worden in fasen gemigreerd

### Migratie-impact 1.0 → 1.1

- Eén bestaand record (`clientacceptatiebeleid.json`) moet hertypeerd worden van `procedure` naar `afwegingskader` en de top-level `_provenance` moet inline gemaakt worden. Geen separaat migratiescript — handmatig of regenereren.
- `prompts/seed-v1.md` wordt herschreven om type-specifieke sleutelvelden, `references[]` en inline `_provenance` voor te schrijven.
- `tools/extractie/index_concept_incremental.py` raakt provenance-paden niet aan voor embedding (gebruikt enkel `naam`-veld) — geen aanpassing nodig.
- Latere tooling (`mark_stale.py`, `remove_bron.py`) leest provenance via inline-paden (`record["main_rule"]["_provenance"]["inputs"]`) ipv top-level. Nog niet bestaand, dus geen breaking change.
