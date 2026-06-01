# ADR-007: Conceptmodel

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-18 (schema 1.6 — `situering` + leerpad-schema 1.1 — `voorbereiding`-hoofdstuk)
**Vervangt**: archive/ADR-006 (drie-lagenmodel — concept-laag absorbeert), archive/ADR-009 (concept-record-schema v2)
**Schema-versie**: 1.6 (concept-records); competentie-schema 1.1 + leerpad-schema 1.1

## Changelog

- **2026-05-18** — Leerpad-schema 1.1: nieuw hoofdstuk-type `voorbereiding` (naast bestaande `oriëntatie` / `competentie` / `thematisch`). Voor concept-clusters die fundament zijn voor meerdere taken zonder zelf één-op-één op één taak te mappen. Render-laag (ADR-010 §implicatie-5) plaatst geen taak-marker en omleidt deze hoofdstukken om het eind-dashboard "Heb je deze taken in de vingers?" — student wordt niet getoetst op fundament. Schema-shape: `{type: voorbereiding, titel, concepten[], rationale_hint?}`. Validatie: een PO mag niet voor 100% uit `voorbereiding`-hoofdstukken bestaan. Geen migratie — bestaande studiemateriaal (schema 1.0) blijven geldig; curator promoveert hoofdstukken naar `voorbereiding` waar zinvol bij volgende leerpad-touch.
- **2026-05-18 (later)** — Schema 1.6 herzien op empirische grond: `situering` op **alle 6 node-types** in plaats van alleen begrip/cluster. Aanleiding: 53/89 cluster-records gebruiken `doel`-veld dat semantisch overlapt met situering ("Het auditrisicomodel structureert de risico-aanpak van de auditor…" = functie + plaatsing in één). Eén uniform veld is schoner dan `doel` op cluster / `situering` op begrip. **`doel`-veld geschrapt** uit type-specifieke sleutelvelden. **Mechanische migratie**: 55 records (53 cluster + 1 begrip + 1 regel) hernoemen `doel` → `situering` via records-API. Competenties hebben empirisch geen `doel`-veld (essentie zit in `titel` + `stappen[]`) — krijgen `situering` als nieuwe veld bij natuurlijke EXTRACT-pass (geen migratie). Render-plek (ADR-010 §implicatie-1): bovenaan élke concept-fiche, boven TL;DR.
- **2026-05-18** — Schema 1.6 (oorspronkelijk voorstel, gesuperseded door bovenstaande): `situering` alleen op begrip/cluster met `doel` behouden. Verworpen wegens duplicatie cluster-`doel`/`situering`.
- **2026-05-18** — Schema 1.5 (deel 2): concretiserings-inhoud uitgewerkt. Drie velden vervangen `voorbeeld_inline`: `in_praktijk[]` (lijstje of rich), `voorbeelden[]` (eenvoudig of scenario), `illustraties[]` (boeking / balans-fragment / verslag-fragment / mermaid-diagram). Multi-niveau-placement: record-top, bouwsteen, berekeningsmethode + inline per competentie-stap. Illustraties **inline** binnen voorbeeld-scenarios. Migratie `voorbeeld_inline` → `voorbeelden[{vorm: eenvoudig}]` bij elke natuurlijke EXTRACT-pass.
- **2026-05-18** — Schema 1.5 (deel 1): node_type-taxonomie geconsolideerd van 11 → 6 (`begrip` · `regel` · `cluster` · `synthese` · `autoriteit` · `competentie`). `fenomeen` → `cluster`, `actor` → `autoriteit`, `skill` → `competentie`. `procedure`/`methode`/`afwegingskader`/`beginsel`/`drempel`/`casus` opgegaan in andere types. Bouwsteen-definitie expliciet gemaakt. Granulariteits-test verfijnd ("buiten één framework testbaar"). Edges-taxonomie van ~20 → 7 canonieke types. Nieuw patroon: regime-specialisatie via `specialisatie-van` met facet-veld `regime`. Concept en competentie wonen in hetzelfde format (records-API, ADR-019). Schrijfregels nu gecentraliseerd in [`docs/concept-schrijfregels.md`](../concept-schrijfregels.md) — `content-richtlijnen.md` is uitgefaseerd. Aanleiding: empirische analyse + gap-mining-rapport 2026-05-18 (5 systemic patterns) + EXTRACT v4-pilot op anchor 1.5.V.C. Migratie-mapping in §"Schema 1.5".

- **2026-05-16 (1.4)** — Didactische verrijking gestructureerd in schema (geen render-trick). Vijf samenhangende uitbreidingen op basis van stagiair-bril-feedback ("te zwaar, te weinig praktisch, geen visualisatie, fictieve namen lastig"):

  - **Stap-blok-schema** (vervangt simpele `stappen[]`-string-lijst). Elk item in `stappen[]` (concept-records én competenties) is voortaan een blok met:
    - `nr`, `titel`, `wat`, `waarom` (behouden van v1)
    - `input[]` en `output[]` als arrays van semantische artefacten:
      ```yaml
      input:
        - artefact: "Balans moeder"
          veld: "Deelnemingen"
          type: "boekhoudkundig-bedrag"
      ```
      `type` is een open string maar canonieke waarden: `boekhoudkundig-bedrag`, `percentage`, `datum`, `document`, `nieuwe-balanspost`, `geëlimineerde-post`, `boekingsregel`.
    - `hoe`: uitvoerbare instructie (multiline, 3-7 stappen, geen jargon-zinnen, beoogt "wat moet je echt doen")
    - `voorbeeld` als sub-object met `scenario` (1 zin) + `substappen[]`:
      ```yaml
      voorbeeld:
        scenario: "..."
        substappen:
          - nr: 1
            titel: "..."
            type: balans | berekening | boekingsregel | opmerking | flowchart
            data: |
              <markdown-tabel of -tekst>
      ```
      Substappen-type bepaalt render-icoon. Markdown-tabellen in `data` worden as-is gerenderd (waar relevant doorgehaalde rijen, vetgedrukte nieuwe posten).
    - `valkuilen[]` (behouden): `advies` (= correcte aanbeveling, als titel), `vaak_fout`, `grondslag`. Render `> [!warning]`-callout met advies als titel.
    - `grondslag`: één string met wikilinks + wetsartikel-citaten

  - **Edges activeren** (al in schema 1.2 gedefinieerd, nooit gevuld). ENRICH-pass populeert `edges[]` op basis van bestaande relaties; render-tijd plaatst edges per type:
    - `onderdeel-van` / `specialisatie-van` → **breadcrumb bovenaan** ("Behoort tot [[X]]")
    - `bevat` → "**Bestaat uit**: [[Y]], [[Z]]" onder TL;DR
    - `vergelijkt-met` → blijft `<details>` "Niet verwarren met" (verwarring-risico)
    - `getriggerd-door` / `vereist-kennis-van` → "**Zie ook**" onderaan
    - `uitzondering-op` → "**Uitzondering op** [[X]]" onder TL;DR
    
    `vergelijkingsparen[]` blijft bestaan maar **alleen voor paren met verwarring-risico**; andere relaties hoeven naar `edges[]`. Schrapt de "we hebben N paren waarvan maar 2 didactisch zijn"-pathologie.

  - **`node_type: synthese`** — nieuw record-type voor pedagogische clusters die meerdere concepten verbinden (bv. "consolidatiemethodes-vergelijking" voor PO 1.4). Synthese-records hebben:
    - `gebaseerd_op_concepten[]` (≥ 3 wikilinks, analoog aan competenties)
    - `vergelijkingstabel` (multiline markdown-tabel)
    - `beslisboom` (geneste lijst of mermaid-flowchart)
    - Geen eigen `definitie` (verwijst naar de gerefereerde concepten)
    
    ENRICH-pass detecteert cohesie-clusters (concepten met ≥ 3 cross-refs onderling) en stelt synthese-records voor.

  - **Naam-cast** — vaste set fictieve namen voor voorbeelden. Globaal in `data/concepten/casts/globaal.yaml` met scenario-templates per relatie-type (basis-consolidatie, joint-venture, geassocieerde, consortium, subconsolidatie, ...). Elke naam start met andere letter (Aurelia, Brugse, Cardinal, ...). Natuurlijke personen krijgen Vlaamse namen (Pieter Vermeulen, Marleen De Cock, ...). Prompt v4 dwingt cast-gebruik af — geen "M / D / D1 / ABC / DEF" meer.

  - **ITAA-LEX-bronnamen** (render-niveau, geen schema-wijziging). Render produceert pretty namen uit chunk-id's via een mapping `KB-WVV-2019__art_3_113` → "KB WVV — art. 3:113". Stagiair leert de ITAA-LEX-indeling herkennen (komt elk examen terug).

  **Volledig stap-blok-voorbeeld**: zie ADR-008 §13 prompt-bijlage of `prompts/concept-extractie-v4.md`.

  **Bouwsteen-blok geformaliseerd** (was: vrije tekst-bullet met wetsartikel in titel). Schema:
  ```yaml
  bouwstenen:
    - titel: "Korte titel max 6 woorden, geen wetsartikel"
      wat: "1-2 zinnen in stagiair-toon — geen letterlijke wettekst-citatie"
      waarom: "Rationale: welk beginsel zit hier achter?"
      voorbeeld_inline: "Eén-zin-voorbeeld met cast-namen (optioneel)"
      grondslag: "KB WVV art. 3:126"   # wetsartikel op laatste regel, niet in titel
      confidence: "grounded"
      _provenance: { inputs: [...] }
  ```
  ENRICH-pass migreert oude bouwstenen (string of `{tekst, source, confidence}`) naar dit blok-formaat. Verplichte velden: `titel`, `wat`, `grondslag`, `confidence`. Aanbevolen: `waarom`, `voorbeeld_inline`.

  **Formule-blok geformaliseerd**. `berekeningsmethode[].formule` was tot v1.3 één string. v1.4:
  ```yaml
  berekeningsmethode:
    - naam: "Consolidatieverschil bij eerste consolidatie"
      formules:
        - id: "pro-rata-aandeel"
          naam: "Pro-rata aandeel in eigen vermogen"
          wiskunde: |
            aandeel = belangenpercentage × eigen vermogen dochter
          variabelen:
            - { symbool: "belangenpercentage", betekenis: "...", eenheid: "%" }
            - { symbool: "eigen vermogen dochter", betekenis: "EV op verwervingsdatum", eenheid: "EUR" }
          invulling_voorbeeld:
            waarden: "belangenpercentage = 80%, eigen vermogen dochter = 300"
            berekening: "80% × 300 = 240"
            eenheid_resultaat: "EUR"
        - id: "consolidatieverschil"
          naam: "Consolidatieverschil"
          wiskunde: |
            consolidatieverschil = aanschaffingswaarde − pro-rata aandeel
          afhankelijk_van: [pro-rata-aandeel]   # forward-reference naar andere formule
          variabelen: [...]
          invulling_voorbeeld:
            waarden: "aanschaffingswaarde = 320, pro-rata aandeel = 240"
            berekening: "320 − 240 = 80 (positief)"
            eenheid_resultaat: "EUR"
  ```
  Render: KaTeX-block voor `wiskunde` (Quartz native support) of leesbare pseudo-formule + variabelen-tabel + invulling. Meerdere `formules[]` per `berekeningsmethode[]` zijn toegestaan met `afhankelijk_van[]`-verwijzing om volgorde te tonen.

  **Voorbeeld-minimum-regel per node-type**:
  
  | Node-type | Minimum voorbeeld |
  |---|---|
  | `begrip` / `fenomeen` | ≥ 1 `voorbeeld_inline` (op record-niveau of in een bouwsteen) |
  | `methode` / `procedure` | ≥ 1 `berekeningsmethode.formules[].invulling_voorbeeld` OF ≥ 1 stap met `voorbeeld.substappen[]` |
  | `regel` / `verplichting` | ≥ 1 `voorbeeld_inline` met concrete cliëntsituatie |
  | `synthese` | ≥ 1 worked example in `vergelijkingstabel` of `beslisboom` |
  | `actor` | ≥ 1 `voorbeeld_inline` met rol-context (bv. "Bestuurder Marleen De Cock") |
  
  Render produceert `> [!todo] Voorbeeld ontbreekt voor dit concept`-callout als minimum niet gehaald is. Zichtbare gap voor stagiair én voor curator. ENRICH-pass krijgt aspect-type `voorbeeld.ontbreekt` om dit mechanisch te detecteren.

  **Voorbeelden — drie toegestane bronnen**:
  1. **Uit bron-chunks**: CBN-adviezen bevatten praktijkvoorbeelden; KB-WVV-artikelen soms ook. Eerste keuze, hoogste confidence.
  2. **Bestaand `concreet_voorbeeld`** uit schema 1.2/1.3 platte-tekst — omzetten naar substappen of inline.
  3. **Synthese met cast** (nieuw, expliciet toegestaan): extractor mag een scenario opstellen met cast-namen en plausibele cijfers, mits:
     - bedragen plausibel (geen 100 miljard voor een BV)
     - scenario illustreert het concept (laat zien hoe de regel/formule werkt)
     - intern consistent (geen contradicties)
     - confidence `inferred` (niet `grounded`)
  Bron 3 mag pas ingezet worden als bron 1 + 2 niet volstaan. Anti-fabricatie-discipline: bedragen zijn didactische illustratie, geen feitelijke claim.

  **Stap-blok concept-procedure vs competentie — schema identiek, conventies verschillen**:
  
  | Aspect | Concept-procedure-stap | Competentie-stap |
  |---|---|---|
  | Scope | Eén wettelijke deelhandeling | Orchestratie van concepten |
  | `grondslag.ref` typisch | Eén wetsartikel | Eén of meer concept-wikilinks |
  | `grondslag.type` mogelijk | `wettekst` of `concept` | `concept` of `praktijk` |
  | `hoe`-inhoud | Uitvoerbaar op één procedure | Kan hele procedure aanroepen ("Volg [[concept-X]] §sectie") |
  | Voorbeeld | Eén casus illustreert procedure | Eén beslissings-scenario met takken |
  
  Geen schema-fork — beide gebruiken identiek stap-blok. Conventies dwingen het verschil af via prompts (concept-extractie-v4 vs competentie-destillatie-v2).

- **2026-05-15 (1.3)** — Drie-lagen leermateriaal-uitbreiding op basis van
  gebruiker-discussie over render-generators. Concept-records krijgen optionele
  `rationale`-velden om pedagogisch inzicht ("welk beginsel? wat ziet de student
  dat de wet niet expliciet zegt?") te dragen — examen-agnostiek; rationale =
  beginselen-inzicht, niet examen-truc. Drie additieve uitbreidingen:

  - **Top-level `rationale`-blok** op concept-record (optioneel, default `confidence: inferred`).
    Shape: `{ text, confidence, _provenance }`. Vrije tekst, kort (1-3 zinnen),
    moet een beginsel of gerelateerd concept noemen — geen vrije speculatie.
  - **`rationale`-subveld** op items van `bouwstenen[]`, `oorzaken[]`,
    `valkuilen[]`, `stappen[]` (waar relevant). String + `rationale_confidence`
    string. Optioneel — records zonder rationale renderen prima.
  - **`in_praktijk[].anker_slug`** — auto-gegenereerd uit `aspect` als hij
    ontbreekt (slugify). Render-fase produceert `<h2 id="boekhoudkundige-verwerking">`
    per `in_praktijk[]`-blok zodat cross-PO concepten (bv. `leasing` met
    `boekhoudkundig` + `fiscaal` aspecten) natuurlijk wikilinkbaar zijn:
    `[[leasing#boekhoudkundige-verwerking]]`.

  **Anti-fabricatie-regels** voor rationale-vulling via ENRICH:
  - Rationale MOET beginsel of gerelateerd concept noemen
  - Default confidence `inferred` (niet `grounded`) — rationale is per definitie afgeleid
  - ENRICH-prompt: "Verbind aan beginselen die in andere concept-records of bron-chunks staan. Bij gebrek aan grondslag: laat rationale leeg."
  - `_provenance.inputs` verwijst naar chunks waaruit het beginsel afgeleid is

  **Nieuwe schema's** (apart, naast concept-record):
  - **Competentie-schema 1.0** in `data/concepten/competenties/<id>.yaml` —
    pedagogische "hoe doe je X" laag. Zie §"Competentie-schema".
    Hard anti-fabricatie via verplichte `gebaseerd_op_concepten` (≥2 concept-refs),
    `procedure_grondslag` met ⚖️ X% · 🤖 Y% transparantie, en grondslag-per-stap.
  - **Leerpad-schema 1.0** in `data/concepten/studiemateriaal/<X.Y>.yaml` —
    ordening van competenties + oriëntatie-blokken per programmaonderdeel.
    Zie §"Leerpad-schema".

  **Niet** een nieuw node_type "competentie" op concept-records — competenties
  zijn een aparte schicht, niet een concept-variant. Drie redenen:
  - Concept-records gegrond in bronnen; competenties gegrond in concepten
  - Lifecycle verschilt (records ↔ enrich-loop; competenties ↔ destillatie-loop)
  - Render-output verschilt (referentiewerk ↔ procedureel-doelgericht)

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

### Node-types (schema 1.5 — 6 types, mag groeien)

`begrip` · `regel` · `cluster` · `synthese` · `autoriteit` · `competentie`

Empirische bevinding (2026-05-18): de oorspronkelijke 11 types waren een organische groei met echte overlap. De geconsolideerde set houdt vast aan duidelijke vragen-onderscheid in plaats van bron-categorisering:

| Type | Definiërende vraag | Voorbeelden |
|---|---|---|
| **begrip** | "Wat is X?" | arbeidskosten, right-of-use-actief, beroepsgeheim |
| **regel** | "Wat schrijft de norm voor?" | art. 3:96 KB WVV, continuïteitsbeginsel, kleine-vennootschap-criteria |
| **cluster** | "Hoe hangt dit fenomeen samen?" — samengesteld onderwerp dat regels, begrippen en bouwstenen samenbrengt | leasing, consolidatie, COSO ERM, jaarrekening-vzw |
| **synthese** | "Hoe vergelijk of beslis ik tussen N records?" | consolidatiemethoden-vergelijking, liquiditeitstoets-beslisboom |
| **autoriteit** | "Welke institutionele actor doet wat?" | FSMA, ITAA, FOD Financiën |
| **competentie** | "Wat moet de stagiair kunnen?" | kwalificeren-en-boeken-leasing, beoordelen-getrouw-beeld |

Inhoudelijke schrijfregels (granulariteits-test, bouwsteen-definitie, regime-specialisatie-patroon, smell-tests) staan in [`docs/concept-schrijfregels.md`](../concept-schrijfregels.md).

### Migratie 1.4 → 1.5 — type-mapping

Bestaande records met oude `node_type`-waarden hercategoriseren bij elke EXTRACT- of edit-pass op het record:

| Oud type | Nieuw type | Beslisregel |
|---|---|---|
| `fenomeen` | `cluster` | Hernoeming, geen schema-wijziging |
| `actor` | `autoriteit` | Hernoeming |
| `skill` | `competentie` | Hernoeming |
| `procedure` | `competentie` (focus op kunnen) of `cluster` met `stappen[]`-bouwsteen (focus op descriptief domein-object) | Case-by-case |
| `methode` | `cluster` | Een methode = samengesteld onderwerp met bouwstenen |
| `afwegingskader` | `cluster` | Bouwstenen worden afwegingsdimensies |
| `beginsel` | `regel` | Beginselen zijn hoog-niveau normatieve regels |
| `drempel` | `regel` | Met `drempelwaarden[]`-veld (al bestaand in schema 1.2) |
| `casus` | géén eigen type | Wordt `voorbeeld_inline` of `in_praktijk.wereld_voorbeeld` op het bijhorende cluster/begrip |

Migratie gebeurt **niet** via een batch-script — bij elke natuurlijke EXTRACT-pass op een record wordt het oude type vervangen. De `_voorgestelde_types.yaml`-route vervalt: nieuwe types worden voorgesteld via een ADR-update, niet via een YAML-bumping.

### Concept en competentie in één format

Beide leven in `data/concepten/records/<id>.json` met dezelfde records-API (ADR-019). Onderscheid via `node_type: competentie` of een ander type. De aparte map `data/concepten/competenties/*.yaml` is historisch — bij EXTRACT v4-pass krijgen records hetzelfde format.

### Bouwsteen — expliciete definitie

Een **bouwsteen** is een sub-aspect van een record dat niet zelfstandig in het domein bestaat. Voorbeeld: "tweestappentest IFRS 16" leeft als bouwsteen binnen `leasing-ifrs`, niet als eigen begrip — buiten IFRS 16-classificatie bestaat het concept niet.

Een bouwsteen wordt promoveerbaar tot eigen record wanneer:
- hetzelfde concept elders in het domein opduikt (cross-context relevantie), OF
- er twee evenwaardige varianten van ontstaan (beide-record-aanpak, geen primair + uitzondering), OF
- een examenvraag de bouwsteen specifiek toetst los van zijn context

### Granulariteits-test (verfijnd)

Domein-onafhankelijkheid + samenhang, niet examenvraag-frequentie:

1. **Bestaat dit zelfstandig in het accounting-domein**, los van een specifiek toepassingscontext? Zo nee → bouwsteen.
2. **Bestaat dit al onder een andere naam** in concept-RAG (semantische similarity op `definitie` + `bouwstenen.text`, niet alleen naam)? Zo ja → merge of synthese ipv duplicaat.

Een **balanspost binnen één regulatorisch regime** is een bouwsteen van dat regime, geen eigen begrip. `right-of-use-actief` voldoet wél (IAS 36 + IFRS 5 erkennen het ook); `leaseverplichting-ifrs` niet (alleen onder IFRS 16 zin).

### Concretiserings-inhoud (schema 1.5) — drie soorten, multi-niveau

Drie complementaire content-velden vervangen het oude `voorbeeld_inline`:

| Veld | Vorm | Plaatsen waar toegestaan |
|---|---|---|
| `in_praktijk[]` | Plain-language uitleg. **Twee vormen**: lijstje (`["X", "Y", "Z"]`) of rich (`[{aspect, betekenis, confidence, source}]`) | Record-top, bouwsteen |
| `voorbeelden[]` | Concrete cases met cast. **Twee vormen**: eenvoudig (`{vorm: eenvoudig, omschrijving, cast?}`) of scenario (`{vorm: scenario, titel, omschrijving, stappen[], illustraties[]?}`) | Record-top, bouwsteen, berekeningsmethode |
| `illustraties[]` | Gestructureerde artefacten — boeking, balans-fragment, verslag-fragment, mermaid-diagram | Record-top, bouwsteen, berekeningsmethode |

Per competentie-stap: optioneel **inline** `voorbeeld` (single) en `illustratie` (single) — niet plural, want één stap = één concrete demonstratie.

**Inline-principe voor illustraties binnen voorbeelden**: een illustratie binnen een voorbeeld-scenario wordt inline geserialiseerd, niet als edge-reference. Een illustratie hoort bij zijn scenario en zou duplicatie-arm zijn als hij echt op record-niveau hoort.

**Illustratie-types startset**:

- `boeking` — `rijen[{rekening, debet, credit, omschrijving?}]` + optioneel `context`, `datum`. Render valideert debet=credit.
- `balans-fragment` — `activa[]` + `passiva[]` (of `posten[]` voor één-zijdig). Render valideert activa=passiva.
- `verslag-fragment` — `tekst` (markdown) + `verslag_type` + `paragraaf_context`.
- `mermaid-diagram` — `code` (Mermaid) + `caption`. First-class type ipv markdown-inline.

Alle illustraties hebben `confidence`, optioneel `source`, optioneel `cast_used`.

**Migratie `voorbeeld_inline` → `voorbeelden[]`**: bestaand schema 1.2-veld `voorbeeld_inline` (block met `text`) wordt bij EXTRACT-pass omgezet naar `voorbeelden: [{vorm: "eenvoudig", omschrijving: <text>, cast: [...], confidence, source}]`. Geen batch-migratie — bij elke natuurlijke EXTRACT-touch op een record. Tijdens overgang lezen agents beide vormen; nieuwe records schrijven enkel de nieuwe vorm.

### Situering (schema 1.6) — context-veld op alle node-types

`situering` is een **optionele string** (2–4 zinnen, geen markdown-blocks) bovenaan elk record (alle 6 node-types) die antwoordt op:

- *Waarom bestaat dit concept?* (welk probleem of belang lost het op?)
- *In welk veld zit het?* (vennootschapsrecht-kapitaalbescherming, boekhoudrecht-jaarrekening, fiscaal-DBI, …)
- *Waar staat het in het grotere geheel?* (één zin oriëntatie, geen volledige edges-render)

**Vervangt `doel`-veld**: tot 2026-05-18 droegen 53/89 cluster-records (60%) een `doel`-veld dat empirisch precies dit deed — *"Het auditrisicomodel structureert de risico-aanpak van de auditor…"* combineert functie en plaatsing in één paragraaf. Schoner: één uniform veld dat overal hetzelfde betekent.

**Per node-type — hoe vult situering zich**:

| Node-type | Wat situering antwoordt | Voorbeeld |
|---|---|---|
| `begrip` | Waarom bestaat dit, in welk veld? | *aanschaffingswaarde*: "Basiswaarde voor alle activa op de balans; fundament voor afschrijvingen, waardeverminderingen en eliminaties bij consolidatie. Zit onder de waarderingsregels van het Belgisch boekhoudrecht." |
| `regel` | In welk regime, welk probleem reguleert het? | *getrouw-beeld-jaarrekening*: "Externe gebruikers (aandeelhouders, kredietverleners, fiscus) moeten op basis van de jaarrekening correcte beslissingen kunnen nemen. Getrouw beeld is de overkoepelende eis in WVV en Boekhoudbesluit." |
| `cluster` | Wat structureert dit cluster, in welk vakgebied? | *auditrisicomodel*: "Structureert de risico-aanpak van de auditor. Verbindt controlerisico, inherent risico en detectierisico tot één werkbare formule. Centraal in ISA 200 en in de ITAA-controlemethodiek." |
| `autoriteit` | Welk veld, welk mandaat? | *FSMA*: "Belgische toezichthouder op de financiële markten. Houdt toezicht op beursgenoteerde vennootschappen, gereguleerde tussenpersonen en marktintegriteit; werkt samen met ECB en ESMA." |
| `synthese` | Welke beslissing of vergelijking faciliteert deze synthese? | *consolidatiemethoden-vergelijking*: "Faciliteert de keuze tussen integrale, evenredige en vermogensmutatiemethode op basis van zeggenschap. Brengt de drie scenarios samen in één beslisboom." |
| `competentie` | In welke werkcontext, welk type opdracht? | *aanvaarden-audit-opdracht*: "Eerste stap van elke wettelijke controle. Zonder onafhankelijkheid-, integriteit- en bekwaamheidstoets mag de stagiair geen opdracht aanvaarden. Reguleerd door ITAA-normen en IESBA-code." |

**Onderscheid t.o.v. nabije velden** (begrip-voorbeeld "wettelijke reserve"):

| Veld | Vraag | Voorbeeld |
|---|---|---|
| `definitie` | Wat is dit? | "5% van nettowinst die in reserve gehouden wordt tot 10% van kapitaal bereikt is." |
| `situering` | Waarom bestaat dit, in welk veld? | "Onderdeel van het regime kapitaalbescherming in het WVV. Beschermt schuldeisers tegen uitkering van inbreng als dividend." |
| `rationale.text` | Welk beginsel verklaart dit? | "Operationaliseert het beginsel 'kapitaal als waarborg voor crediteuren' — buffer voorkomt dat winstuitkering eigen vermogen onder geplaatst kapitaal duwt." |
| `in_praktijk[*]` | Hoe gebruik je dit? | `aspect: "Berekening jaarlijks"`, `betekenis: "Bij elke winstverdeling toetsen tot 10% bereikt is."` |

**Schrijfregels**:
- Compact: één paragraaf, geen lijst, geen wikilinks (situering moet leesbaar zijn zónder edges-resolutie)
- Wetreferentie alleen als hij het regime-veld benoemt (bv. "het WVV", "het Boekhoudbesluit") — geen artikel-citaties
- Confidence-label: `grounded` als het regime-veld direct uit de bron komt; `inferred` als het een synthetische plaatsing is

**Render**: bovenaan de concept-fiche, **boven** de TL;DR-callout, als plain paragraph (geen callout). Reden: het is contextuele oriëntatie, geen kerncategorie — een callout zou het visueel even zwaar maken als de definitie zelf. Zie ADR-010 §callout-conventies.

**Migratie `doel` → `situering`** (eenmalig, 2026-05-18): 55 records (53 cluster + 1 begrip + 1 regel) hernoemen via records-API. Veldwaarde 1:1 overgenomen; `_provenance.veld_renamed_at` ingesteld. Geen content-wijziging, alleen veldnaam. Voor records zonder bestaand `doel`-veld: geen migratie — `situering` is optioneel en wordt door EXTRACT v4 bij natuurlijke pass aangevuld. Sparse-fields-norm (§Designprincipes) blijft gelden.

**Laag-heuristiek (waarom hier, niet in leermateriaal)**: situering verandert mee wanneer de regel/definitie verandert (een nieuwe wettelijke regime-shift wijzigt zowel hoofdregel als situering). Dat is het criterium voor data-laag (ADR-010 §interpretatieve-laag): samen-aanpassen → concept-laag; bij-cursus-schrijven → leermateriaal-laag. Pedagogische framing per leerpad ("dit is één van drie reserves; vergelijk met onbeschikbare en beschikbare") hoort daarom **niet** hier maar in de minicursus.

### Regime-specialisatie — algemene cluster + specialisaties

Wanneer hetzelfde fenomeen onder meerdere regulatorische regimes wezenlijk verschillend wordt behandeld:

```
leasing                    (cluster — algemene, regime-overstijgende kern)
├── leasing-be-gaap        (cluster — specialisatie)
└── leasing-ifrs           (cluster — specialisatie)
```

Verbonden via edge `specialisatie-van` met optioneel facet-veld `regime`. Geen aparte `node_type` voor specialisaties — zij blijven `cluster`. Triggers: *"onder IFRS / BE-GAAP"*, *"art. KB W.Venn. vs IAS"*, *"fiscaal versus boekhoudkundig"*.

### Type-specifieke sleutelvelden

Elk node-type krijgt een hoofdveld dat past bij de aard van de kennis. **`main_rule` is exclusief voor verplichtings-types**; voor andere types is het geen escape-hatch.

| Node-type | Hoofdveld | Secundaire structuur | Toelichting |
|---|---|---|---|
| `begrip`, `autoriteit`, `cluster` | `definitie` | — | Wat is dit ding of fenomeen? |
| `regel` | `main_rule` | — | Wat is de verplichting/het principe? |
| `competentie` | `titel` + `stappen[]` | `beoordelings_criteria`, `voorbeelden[]` | Wat moet de stagiair kunnen? |
| `synthese` | `gebaseerd_op_concepten[]` | `vergelijkingstabel`, `beslisboom`, `kerninzichten` | Cross-record vergelijking of beslisboom |

**`doel`-veld geschrapt** (schema 1.6, 2026-05-18): voorheen op cluster (60% gebruik) en op competentie (theoretisch hoofdveld). Op cluster overlapte het met de nieuwe `situering` — beide werden gemigreerd. Op competentie bleek empirisch dat geen enkele competentie-record een `doel`-veld droeg; de essentie zit in `titel` + `stappen[]`. Daarom: `doel` als veldnaam gepensioneerd; functie van situerende paragraaf zit voortaan in het uniforme `situering`-veld (zie §situering).

> **Historische mapping (schema 1.4 → 1.5)**: `actor` → `autoriteit`, `fenomeen` → `cluster`, `skill` → `competentie`, `methode` → `cluster`, `afwegingskader` → `cluster`, `beginsel` → `regel`, `drempel` → `regel`. Zie §"Migratie 1.4 → 1.5" voor beslisregels.

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

### Rationale-velden (schema 1.3, additief)

Concept-records mogen optionele `rationale`-velden bevatten die pedagogisch inzicht dragen — antwoorden op "welk beginsel? waarom telt dit? wat ziet de student dat de wettekst niet expliciet zegt?". Examen-agnostiek; geen examen-tips, wel beginselen-inzicht.

**Top-level `rationale` (record-niveau)**:
```json
{
  "rationale": {
    "text": "Eén beknopt verhaal (1-3 zinnen) dat het concept verbindt aan een onderliggend beginsel.",
    "confidence": "inferred",
    "_provenance": {
      "inputs": [{"id": "<chunk-id>", "sha256": "..."}],
      "verrijkt_door": "enrich-run-<id>",
      "verrijkt_op": "<iso>"
    }
  }
}
```

**Per-item `rationale` (bouwsteen/oorzaak/valkuil/stap)** — optioneel, alleen voor centrale concepten waar nuttig:
```json
{
  "bouwstenen": [
    {
      "tekst": "Eliminatie van de deelneming tegen het aandeel in eigen vermogen",
      "source": {...},
      "confidence": "grounded",
      "rationale": "Voorkomt dubbeltelling: het kapitaal van de dochter zit al in de geconsolideerde activa.",
      "rationale_confidence": "inferred"
    }
  ]
}
```

**Anti-fabricatie-regels** (cruciaal — granulaire rationale heeft groot hallucinatie-risico):
- Rationale-tekst MOET een beginsel of gerelateerd concept noemen, geen vrije speculatie
- Default `confidence: "inferred"` (niet `grounded`) — rationale is per definitie afgeleid
- Bij gebrek aan grondslag: **veld leeg laten**, niet "iets" verzinnen
- ENRICH-prompt v2 wordt uitgebreid met expliciete regels (zie ADR-008 §13.3)

### Aspect-anker (schema 1.3, additief)

`in_praktijk[].anker_slug` is een optioneel veld dat de render-fase gebruikt als HTML-anker voor het corresponderende H2-blok. Als afwezig: auto-gegenereerd uit `aspect` via slugify (lowercase, spaces → `-`, accenten weg).

Effect: cross-PO concepten zoals `leasing` waarvan `in_praktijk[]` zowel een `Boekhoudkundige verwerking`-blok als een `Fiscale behandeling`-blok bevat, krijgen automatisch twee subsecties die wikilinkbaar zijn als `[[leasing#boekhoudkundige-verwerking]]` resp. `[[leasing#fiscale-behandeling]]`. Geen handmatig anker-werk; volgt organisch uit records.

### Competentie-schema (schema 1.0)

Competenties leven in `data/concepten/competenties/<id>.yaml`. Schema:

```yaml
id: bepalen-consolidatieverplichting
titel: "Bepalen of de moeder de geconsolideerde jaarrekening moet opmaken"
status: voorgesteld                          # voorgesteld → gecureerd
schema_version: 1.0
programmaonderdelen: [1.4]
voortkomend_uit:
  taken: [1.4.taak.1]                        # anchor-id's uit programma.json
  kenniselementen: [1.4.I.B, 1.4.I.D]
gebaseerd_op_concepten:                       # verplicht ≥ 2 — anti-fabricatie
  - groottecriteria-consolidatie
  - consolidatieverplichting
  - vrijstelling-subconsolidatie
procedure_grondslag:                          # verplicht
  wettelijk_pct: 80                            # ⚖️
  praktijk_pct: 20                             # 🤖
  motivering: "Drempels wettelijk; volgorde van toetsen is gebruikelijke werkwijze."
stappen:
  - nr: 1
    titel: "Inventariseer de groep"
    input: "Aandeelhoudersregister + statuten + AV-notulen van de moeder"
    output: "Lijst kandidaat-dochters en geassocieerde ondernemingen"
    waarom: "De scope hangt af van wie effectief gecontroleerd wordt."
    grondslag:                                 # verplicht — concept-wikilink of expliciete 🤖
      type: concept                            # concept | wettekst | praktijk
      ref: "[[controle]]"
    valkuilen:
      - foute_aanname: "Alleen kijken naar % aandelenbezit."
        correctie: "Ook controle-in-feite tellen."
        grondslag: "[[exclusieve-controle]]"
beslisboom:                                    # optioneel
  - vraag: "Drempels overschreden?"
    ja: "Vrijstellingen toetsen → bij geen vrijstelling: consolideren"
    nee: "Geen verplichting voor de moeder"
voorbeelden:                                   # Situatie → Conclusie → Grondslag → Redenering (v0.1-patroon)
  - situatie: "Familie-groep met moeder + 3 dochters; geaggregeerd 25 mln omzet, 18 mln balans, 80 wpf"
    conclusie: "Niet verplicht — slechts 1 criterium overschreden (wpf)."
    grondslag: "[[groottecriteria-consolidatie]] §drempels"
    redenering: "Twee van drie drempels niet overschreden → 'groep van beperkte omvang'."
_provenance:
  voorgesteld_door: "competentie-destillatie-v1-<run-id>"
  voorgesteld_op: "<iso>"
  gecureerd_door: null                         # mens-veld bij review
  gecureerd_op: null
```

**Anti-fabricatie-regels** (afgedwongen door `validate_competentie.py`):

1. **`gebaseerd_op_concepten` ≥ 2** — competentie zonder concept-verankering wordt geweigerd
2. **Elke stap heeft `grondslag.ref`** — `[[concept-id]]`, expliciete wettekst, of `type: praktijk` met motivering
3. **`procedure_grondslag.wettelijk_pct + praktijk_pct == 100`** — gedwongen transparantie
4. **`praktijk_pct > 50` triggert verplicht mens-review** (geen auto-`gecureerd`)
5. **Wikilinks naar concept-records** moeten bestaande records aanwijzen
6. **Voorbeelden** moeten gebaseerd zijn op scenario's uit bron-chunks van gerefereerde concept-records (geen verzonnen casussen)

**Competentie-type** is geen frontmatter-enum — types ontstaan organisch uit data (v0.1 had impliciet: procedure, berekening, beoordeling, advies, controle). Optioneel veld `competency_type: <string>` voor toekomstige UI-filtering, geen validatie op waarde.

### Leerpad-schema (schema 1.0)

Leerpaden leven in `data/concepten/studiemateriaal/<programmaonderdeel>.yaml`. Schema (1.1 sinds 2026-05-18 — `voorbereiding`-type toegevoegd):

```yaml
programmaonderdeel: "1.4"
titel: "Geconsolideerde jaarrekening"
status: voorgesteld                          # voorgesteld → gecureerd
schema_version: 1.1
hoofdstukken:
  - type: oriëntatie                          # LLM-glue, geen records-binding
    titel: "Wat is consolideren? Waarom?"
    rationale_hint: "groep-fictie + economische realiteit + bescherming derden"

  - type: voorbereiding                       # fundament voor meerdere taken (geen taak-marker)
    titel: "De drie consolidatie-methodes — fundament"
    concepten:
      - integrale-consolidatie
      - evenredige-consolidatie
      - vermogensmutatiemethode
    rationale_hint: "fundament voor taken 1.4.taak.1 t/m 1.4.taak.4"

  - type: competentie                         # references één competentie-yaml
    competentie_id: bepalen-consolidatieverplichting

  - type: thematisch                          # concept-cluster zonder pedagogische omhulling
    titel: "Eliminaties bij integrale consolidatie"
    concepten:
      - eliminatie-interne-transacties
      - eliminatie-deelneming-eigen-vermogen

_provenance:
  voorgesteld_door: "leerpad-propose-v1-<run-id>"
  voorgesteld_op: "<iso>"
  gecureerd_door: null
  gecureerd_op: null
```

Vier hoofdstuk-types:
- **`oriëntatie`** — LLM-only, voor "wat is X?" / "waarom?" / introductie. Geen records-binding maar oriëntatie-prompt verplicht expliciete verwijzing naar bestaande concept-records (anti-fabricatie). Krijgt geen taak-marker (oriëntatie ≠ taak-werk).
- **`voorbereiding`** — concept-cluster dat fundament is voor *meerdere* taken zonder één-op-één-mapping. Render-laag plaatst `> [!note]` "Voorbereidende kennis — fundament voor de taken hierna" in plaats van taak-marker. Wordt **niet** opgenomen in eind-dashboard "Heb je deze taken in de vingers?" — student wordt niet op fundament getoetst. Optioneel veld `rationale_hint` benoemt welke taken het fundament dekt (curator-leesbaar, geen render-functie).
- **`competentie`** — references één competentie-yaml via `competentie_id`. Taak-marker via competentie.linked_anchors-resolve.
- **`thematisch`** — concept-cluster zonder pedagogische omhulling (referentie-luik). Taak-marker via concepten[].linked_anchors-resolve.

**Validatie schema 1.1**:
- Een PO mag niet voor 100% uit `voorbereiding`-hoofdstukken bestaan (curator-warning, geen build-fail).
- Een hoofdstuk met `type != voorbereiding` en 0 resolveerbare taken via concepten/competentie → curator-warning (slechte binding of ontbrekend `voorbereiding`-label).
- Bestaande studiemateriaal met `schema_version: 1.0` blijven geldig — schema 1.1 is additief, geen migratie vereist.

### Edge-types (schema 1.5 — 7 canonieke types)

Geconsolideerd van ~20 → 7 op basis van empirische usage-analyse (2026-05-18):

| Type | Betekenis | Optioneel facet-veld |
|---|---|---|
| `vereist-kennis-van` | Prerequisite voor begrip | — |
| `onderdeel-van` | Compositioneel (child → parent) | — |
| `vergelijkt-met` | Parallel of contrast | `aspect` |
| `getriggerd-door` | Causation, gebeurtenis-keten | `conditie` |
| `specialisatie-van` | Regime-/sub-type-specialisatie | `regime` |
| `uitzondering-op` | Exception op een regel | `scope` |
| `verwijst-naar` | Generieke catch-all | — |

Optionele velden op alle edges: `scope`, `conditie`, `aspect`, `redenering`, `regime`, `notities[]`, `_dangling`.

**Verdwenen edge-types** (gedeprecieerd 2026-05-18):

- `bevat` → vervangen door inverse `onderdeel-van` (graph navigeerbaar in beide richtingen)
- `contrasteert-met` → gefold in `vergelijkt-met` met `aspect`-facet
- `vervangt` / `vervangen-door` / `alternatief-voor` / `van-toepassing-op` → `verwijst-naar` of specifiekere edge
- `definieert`, `regelt`, `primeert-boven`, `toegepast-via`, `voorbeeld-van`, `bedreigt`, `ratio`, `schakelt-over-naar`, `gemeten-met`, `vernietigt-deel-van` → nooit of nauwelijks gebruikt, weggelaten

Bestaande records met gedeprecieerde edges worden bij elke natuurlijke EXTRACT-pass herwerkt naar de canonieke 7.

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

### Granulariteit-beslisregels (schema 1.4, 2026-05-16)

Voor de vraag "wordt deze claim een eigen concept-record of blijft het een bouwsteen-met-wikilink van een groter concept" zijn drie criteria. **ENRICH past deze autonoom toe** — alleen het echte twijfelgeval flagt een `granulariteit.beslissing-nodig`-gap voor mens-review.

**APART CONCEPT** wanneer **alle drie** voldaan zijn:

1. **Eigen primaire bron**: het fenomeen heeft een eigen wettelijk artikel of normpunt als primaire bron (niet alleen een paragraaf binnen een groter artikel). Bv. `consolidatieverschil` heeft KB WVV art. 3:130-3:131 als eigen artikel; "compensatie van deelneming" (KB WVV art. 3:127 a) is één bullet binnen integrale-consolidatie-procedure → bouwsteen.

2. **Cross-referentie-druk**: het fenomeen wordt aangeroepen door ≥ 3 andere records via wikilinks of bouwstenen. Bv. `controle` is gebaseerd-op bij 6+ andere records → apart concept. "Vermoedelijke gebruiksduur" verschijnt alleen in `consolidatieverschil` → geen apart concept.

3. **Independent definieerbaar**: het fenomeen heeft een 1-zin definitie zonder afhankelijke kwalificatie ("binnen de context van X"). Bv. "Pro-rata aandeel" is een afhankelijke berekening — geen apart concept. "Consolidatiekring" definieert zichzelf — apart concept.

**BOUWSTEEN MET WIKILINK** (niet flaggen, refereer) wanneer 2 of 3 criteria onvoldaan zijn. ENRICH zet de claim in `bouwstenen[]` met wikilink naar gerelateerd concept.

**FLAG `granulariteit.beslissing-nodig`** (mens-review) wanneer:
- 1 criterium voldaan, 2 niet, EN het concept > 100 woorden uitleg vergt
- Of: 2 criteria voldaan maar bron-set is ambigu (bv. CBN-advies én KB-artikel die elk een ander aspect dekken)

Anti-fabricatie-discipline: ENRICH mag een claim NIET autonoom als nieuw concept-record schrijven. Wel autonoom: claim refactoren naar bouwsteen met wikilink. Voor nieuwe records → mens-curatie van `granulariteit.beslissing-nodig`-flag.

### Balans- en resultatenrekening-templates (schema 1.4, 2026-05-16)

Voor concept-records die boekhoudkundige artefacten illustreren (consolidatie-balansen, intragroep-eliminaties, vermogensmutatie-boekingen) bestaan **referentie-skeletons** in [`data/concepten/templates/`](../../data/concepten/templates/):

- `balans-verkort.md` / `balans-volledig.md` / `balans-geconsolideerd.md`
- `resultatenrekening-verkort.md` / `resultatenrekening-volledig.md`
- `boekingsregel.md`

Templates zijn **kennis-bron voor de extractor/enricher** — niet render-time substitutie. Een substap met `type: balans` schrijft de extractor handmatig met de juiste rubriek-structuur uit het template. LLM-vrijheid voor scenario's; mechanische check via VERIFY:

- `balans.klopt-niet` — activa-totaal ≠ passiva-totaal
- `balans.rubriek-ontbreekt` — Vaste activa / Eigen vermogen / Schulden mist
- `resultatenrekening.klopt-niet` — opbrengsten − kosten ≠ resultaat
- `boeking.klopt-niet` — som debet ≠ som credit

Aanvulbaar wanneer nieuwe boekhoudkundige patronen nodig zijn (bv. kasstroom-overzicht voor IFRS, fiscale aangifte voor PO 2.x).

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
- `tools/lib/records_api.py` (ADR-019) raakt provenance-paden niet aan voor embedding (gebruikt enkel `naam`-veld via de daemon) — geen aanpassing nodig.
- Latere tooling (`mark_stale.py`, `remove_bron.py`) leest provenance via inline-paden (`record["main_rule"]["_provenance"]["inputs"]`) ipv top-level. Nog niet bestaand, dus geen breaking change.
