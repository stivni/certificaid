# Prompt: Per-anker concept-extractie — Fase C (v4)

**Doel**: Extraheer uit een bundel bronchunks alle concepten die voor één ITAA-anker relevant zijn. Output volgt **ADR-007 schema v1.4** (stap-blok + edges-activatie + node_type synthese + naam-cast). Schrijft naar flat `data/concepten/records/<concept-slug>.json`.

**Model**: claude-opus-4-7 (subagent — zie ADR-008 §2; geen externe API).

**Basis**: deze prompt is een **delta op v3**. Lees eerst `prompts/concept-extractie-v3.md` voor alle regels en schema-1.2/1.3-velden die ongewijzigd blijven (centraliteit, anti-hallucinatie, dangling-references-logging, etc.). Dit document beschrijft alleen wat **anders** is.

---

## Nieuwe regels in v4 (schema 1.4)

### Regel 6 — Stagiair-toon verplicht (niet alleen jargon-vrij)

Concept-records moeten **uitvoerbaar** zijn voor een stagiair-accountant zonder juristen-opleiding. Niet alleen "vervang woord X door Y", maar **schrijf zinnen die de stagiair kan toepassen**.

**Foute zin** (te zwaar, niet uitvoerbaar):
> "Compenseer de boekwaarde van de deelneming met het overeenkomstig deel van het eigen vermogen van de dochter op verwervingsdatum."

**Goeie zin** (uitvoerbare instructie):
> "1. Open de balans van Aurelia Holding, zoek de post **Deelnemingen** (bv. 320 voor Brugse Brouwerij).
> 2. Open de balans van Brugse Brouwerij op verwervingsdatum, bereken het eigen vermogen totaal (kapitaal + reserves + overgedragen resultaat = bv. 300).
> 3. Bereken jouw aandeel: belangenpercentage × eigen vermogen dochter (80% × 300 = 240).
> 4. Schrap beide bedragen uit de geconsolideerde balans.
> 5. Verschil (320 − 240 = **80**) registreer je als **Consolidatieverschillen**."

**Operationele criteria**:
- Korte zinnen (max 25 woorden)
- Geen jargon zonder uitleg ("primauteit", "consoliderende vennootschap", "eigen-vermogenposten")
- Eerste keer een afkorting: voluit + (afkorting). Voorbeeld: "algemene vergadering (AV)"
- Vermijd buzzword-stapeling ("compenseren / verwervingsdatum / boekwaarde / eigen vermogen" in één zin = onleesbaar)
- Bouwsteen-titels: max 6 woorden, **geen wetsartikel in titel**. Wetsartikel hoort op laatste regel als `_Grondslag: KB WVV art. 3:127_`.

### Regel 7 — Naam-cast verplicht voor voorbeelden

Lees `data/concepten/casts/globaal.yaml` en gebruik **uitsluitend** namen uit die cast voor voorbeelden. **Geen** "M / D / D1 / D2 / X / Y / ABC / DEF" meer.

Kies een passend scenario-template (basis-consolidatie / joint-venture / geassocieerde / consortium / subconsolidatie / groep-van-beperkte-omvang / afwijkende-afsluitingsdatum) en gebruik de bijhorende namen consistent.

**Voorbeeld**: voor een vermogensmutatie-voorbeeld → scenario `geassocieerde` → moeder = "Antwerpse Investments NV", geassocieerde = "Drukkerij Dendermonde BV", belang = 25%, aanschaffingswaarde = 200, EV geassocieerde = 600.

Natuurlijke personen (consortium-leider, bestuurder, aandeelhouder): kies uit cast (Pieter Vermeulen, Marleen De Cock, Robert Vandenberghe). Geen "natuurlijke persoon X".

### Regel 8 — Stap-blok-schema (schema 1.4)

`stappen[]` is geen lijst van strings of `{volgorde, text}`-dicts meer. Elk item is een **blok**:

```yaml
stappen:
  - nr: 2
    titel: "Compenseer boekwaarde van deelneming"
    wat: "Twee posten tegen elkaar afzetten, het verschil als consolidatieverschil registreren."
    waarom: "Vermijdt dubbeltelling: dochter-EV en aanschaffingswaarde representeren dezelfde economische waarde."
    
    input:
      - artefact: "Balans moeder"
        veld: "Deelnemingen"
        type: "boekhoudkundig-bedrag"
      - artefact: "Balans dochter op verwervingsdatum"
        veld: "Eigen vermogen totaal"
        type: "boekhoudkundig-bedrag"
      - artefact: "Aandelenkoopovereenkomst"
        veld: "Belangenpercentage"
        type: "percentage"
    
    output:
      - artefact: "Geconsolideerde balans"
        veld: "Deelnemingen"
        type: "geëlimineerde-post"
      - artefact: "Geconsolideerde balans"
        veld: "Consolidatieverschillen"
        type: "nieuwe-balanspost"
    
    hoe: |
      1. Open balans Aurelia Holding, zoek 'Deelnemingen' (320 voor Brugse Brouwerij).
      2. Open balans Brugse Brouwerij op verwervingsdatum, bereken eigen vermogen.
      3. Bereken jouw aandeel: 80% × eigen vermogen Brugse Brouwerij (80% × 300 = 240).
      4. Schrap beide bedragen uit de geconsolideerde balans.
      5. Verschil (320 − 240 = 80) registreer je als 'Consolidatieverschillen'.
    
    voorbeeld:
      scenario: "Aurelia Holding NV verwerft op 1 januari 20X1 een belang van 80% in Brugse Brouwerij BV voor 320."
      substappen:
        - nr: 1
          titel: "Vertrekpunt: balans Aurelia Holding (vóór consolidatie)"
          type: balans
          data: |
            | Aurelia Holding — Activa            |      |
            |-------------------------------------|-----:|
            | Vaste activa                        | 1000 |
            | **Deelnemingen** (Brugse Brouwerij) | **320** |
            | Vlottende activa                    |  800 |
            | **Totaal**                          | **2120** |
        - nr: 2
          titel: "Balans Brugse Brouwerij op verwervingsdatum"
          type: balans
          data: |
            | Brugse Brouwerij — Passiva |      |
            |----------------------------|-----:|
            | Kapitaal                   |  200 |
            | Reserves                   |  100 |
            | **Eigen vermogen totaal**  | **300** |
            | Schulden                   |  800 |
            | **Totaal**                 | **1100** |
        - nr: 3
          titel: "Compensatie + berekening consolidatieverschil"
          type: berekening
          data: |
            Aandeel Aurelia in EV Brugse  = 80% × 300 = **240**
            Aanschaffingswaarde           =           = **320**
            Consolidatieverschil          = 320 − 240 = **80** (positief)
            Belangen van derden           = 20% × 300 = **60**
        - nr: 4
          titel: "Geconsolideerde balans (resultaat)"
          type: balans
          data: |
            | Geconsolideerde balans — Activa     |      |
            |-------------------------------------|-----:|
            | Vaste activa (Aurelia + Brugse)     | 1600 |
            | ~~Deelnemingen~~                    |    — |
            | **Consolidatieverschillen** (nieuw) |  **80** |
            | Vlottende activa (Aurelia + Brugse) | 1300 |
            | **Totaal**                          | **2980** |
    
    valkuilen:
      - advies: "Reken het verschil eerst toe aan onder/overgewaardeerde activa en passiva."
        vaak_fout: "Het volledige verschil meteen als consolidatieverschil boeken."
        grondslag: "[[consolidatieverschil]] §toerekening"
    
    grondslag: "[[consolidatieverschil]] §berekening, KB WVV art. 3:127 a, art. 3:128"
```

**Verplichte velden** per stap: `nr`, `titel`, `wat`, `hoe`, `grondslag`.
**Aanbevolen velden**: `waarom`, `input[]`, `output[]`, `voorbeeld`, `valkuilen[]`.

**Substap-types**: `balans` / `berekening` / `boekingsregel` / `opmerking` / `flowchart`. Render-tijd icoon-mapping. Markdown-tabel in `data` wordt as-is gerendered.

**Geen voorbeeld** is toegestaan bij abstracte stappen (bv. "Inventariseer de groep"), maar bij stappen die rekenen / boeken / een bedrag produceren is `voorbeeld.substappen[]` met minstens één `balans`-substap **verplicht** (Regel 2-uitbreiding).

### Regel 9 — Edges activeren met types

`edges[]` was tot v3 een leeg veld. Vanaf v4: **populeren**. Edge-types:
- `onderdeel-van` / `specialisatie-van` — render als breadcrumb bovenaan ("Behoort tot ...")
- `bevat` — "Bestaat uit: ..."
- `vergelijkt-met` — alleen voor verwarring-risico, render als collapsible "Niet verwarren met"
- `getriggerd-door` / `vereist-kennis-van` — "Zie ook" onderaan
- `uitzondering-op` — "Uitzondering op X" onder TL;DR

**Verschil met `vergelijkingsparen[]`**:
- `vergelijkingsparen[]` blijft bestaan, maar **alleen** voor paren met écht verwarring-risico (typisch examenvalkuilen).
- "X is onderdeel van Y" of "X triggert Y" of "X is een specialisatie van Y" hoort in `edges[]`, niet in `vergelijkingsparen[]`.

**Test voor vergelijkingsparen**:
- Heeft het paar een `trigger` waarin een student écht kan kiezen tussen X en Y in een examen-situatie? → houden
- Is het verschil een definitorisch onderdeel (X bevat Y of X is een specifiek geval van Y)? → naar edges

### Regel 10 — node_type: synthese (nieuw)

Een **synthese-record** verbindt meerdere concepten zonder zelf een nieuw fenomeen te beschrijven. Bijvoorbeeld: `consolidatiemethodes-vergelijking` vergelijkt integrale + evenredige + vermogensmutatie + horizontale consolidatie.

**Schema voor synthese-record**:
```yaml
id: consolidatiemethodes-vergelijking
naam: "De vier consolidatiemethodes vergeleken"
node_type: synthese
schema_version: "1.4"
linked_anchors: [...]
gebaseerd_op_concepten:
  - integrale-consolidatie
  - evenredige-consolidatie
  - vermogensmutatiemethode
  - horizontale-consolidatie
vergelijkingstabel: |
  | Methode | Controle-niveau | Wat verschijnt op balans | Belangen van derden? |
  |---|---|---|---|
  | Integrale consolidatie | Exclusieve controle | Activa/passiva voor 100% | Ja, apart op passiefzijde |
  | Evenredige consolidatie | Gezamenlijke controle | Activa/passiva pro-rata | Nee, niet apart |
  | Vermogensmutatiemethode | Invloed van betekenis | Eén balanspost (één regel) | Nee, niet van toepassing |
  | Horizontale consolidatie | Consortium (geen moeder) | Activa/passiva voor 100% per lid | Ja, per consortium-lid |
beslisboom: |
  ```mermaid
  flowchart TD
    A[Welk type relatie?] --> B{Exclusieve controle?}
    B -->|Ja| C[Integrale consolidatie]
    B -->|Nee| D{Gezamenlijke controle?}
    D -->|Ja| E[Evenredige consolidatie]
    D -->|Nee| F{Invloed van betekenis?}
    F -->|Ja| G[Vermogensmutatiemethode]
    F -->|Nee| H[Geen consolidatie]
  ```
_provenance: ...
```

Geen `definitie`/`main_rule` (verwijst naar onderliggende concepten). Wel `vergelijkingstabel` (multiline markdown) en optioneel `beslisboom` (mermaid of geneste lijst).

ENRICH-pass detecteert cohesie-clusters (concepten met ≥ 3 onderlinge cross-refs) en stelt synthese-records voor.

### Regel 11 — Bouwsteen-blok geformaliseerd

In v1.2/1.3 was een bouwsteen vaak één lange wettekst-zin met wetsartikel in de titel:

> **Integrale opname (KB WVV art. 3:126)**: Alle actief- en passiefbestanddelen van de consoliderende vennootschap en van de in de consolidatie opgenomen dochterondernemingen worden in de geconsolideerde balans opgenomen. ⚖️

In v4 schrijf je een **blok** met vijf velden:

```yaml
bouwstenen:
  - titel: "Volledige opname van beide balansen"   # max 6 woorden, geen wetsartikel
    wat: "Alle bezittingen en schulden van moeder en dochter komen samen in de geconsolideerde balans — voor 100%."
    waarom: "De groep wordt voorgesteld als één economische entiteit; je doet alsof het één bedrijf is."
    voorbeeld_inline: "Aurelia heeft activa 1000, Brugse Brouwerij heeft activa 600 → geconsolideerd: 1600 (vóór intragroep-eliminaties)."
    grondslag: "KB WVV art. 3:126"
    confidence: "grounded"
    _provenance: { inputs: [{"id": "...", "sha256": null, "version": "rag-v1"}] }
```

- **titel** ≤ 6 woorden, geen wetsartikel, stagiair-toon
- **wat** 1-2 zinnen in eigen woorden — geen letterlijke wettekst-citatie
- **waarom** rationale (welk beginsel zit erachter?)
- **voorbeeld_inline** één-zin-voorbeeld met cast-namen (optioneel; verplicht voor centrale bouwstenen)
- **grondslag** wetsartikel op laatste regel
- **confidence** ongewijzigd

### Regel 12 — Formule-blok geformaliseerd

In v1.2/1.3 was `formule` één string die alles op één regel duwde — onleesbaar:

> `Geconsolideerde post = (post moeder) + (post dochter × 100 %) − intragroep-eliminaties; Aandeel derden = (1 − belang%) × eigen vermogen of resultaat dochter`

In v4 splits je dit in losse, genummerde formules met variabelen en voorbeeld:

```yaml
berekeningsmethode:
  - naam: "Consolidatieverschil bij eerste consolidatie"
    formules:
      - id: "pro-rata-aandeel"
        naam: "Pro-rata aandeel in eigen vermogen"
        wiskunde: |
          aandeel = belangenpercentage × eigen vermogen dochter
        variabelen:
          - { symbool: "belangenpercentage", betekenis: "Stemrechtenaandeel moeder in dochter", eenheid: "%" }
          - { symbool: "eigen vermogen dochter", betekenis: "EV op verwervingsdatum", eenheid: "EUR" }
        invulling_voorbeeld:
          waarden: "belangenpercentage = 80%, eigen vermogen dochter = 300"
          berekening: "80% × 300 = 240"
          eenheid_resultaat: "EUR"
      
      - id: "consolidatieverschil"
        naam: "Consolidatieverschil"
        wiskunde: |
          consolidatieverschil = aanschaffingswaarde − pro-rata aandeel
        afhankelijk_van: ["pro-rata-aandeel"]
        variabelen:
          - { symbool: "aanschaffingswaarde", betekenis: "Wat moeder betaalde voor de aandelen", eenheid: "EUR" }
          - { symbool: "pro-rata aandeel", betekenis: "Resultaat eerste formule", eenheid: "EUR" }
        invulling_voorbeeld:
          waarden: "aanschaffingswaarde = 320, pro-rata aandeel = 240"
          berekening: "320 − 240 = 80 (positief)"
          eenheid_resultaat: "EUR"
```

**Regels**:
- Eén `formule` per concept = één wiskundige relatie (max 1 `=` en 1-2 operators)
- Bij meerstapse berekeningen: split in meerdere formules met `afhankelijk_van`-keten
- Elke formule verplicht `variabelen[]` (uitleg per symbool) + `invulling_voorbeeld` (concrete cijfers met cast-namen)
- `wiskunde` is leesbare pseudo-formule (geen LaTeX-vereiste) — Quartz-render kan KaTeX inzetten waar zinvol

### Regel 13 — Voorbeeld-minimum per node-type

Schema 1.4 dwingt minimum voorbeeld-aanwezigheid af:

| Node-type | Minimum |
|---|---|
| `begrip` / `fenomeen` | ≥ 1 `voorbeeld_inline` (record-niveau of in bouwsteen) |
| `methode` / `procedure` | ≥ 1 `berekeningsmethode.formules[].invulling_voorbeeld` OF ≥ 1 stap met `voorbeeld.substappen[]` |
| `regel` / `verplichting` | ≥ 1 `voorbeeld_inline` met concrete cliëntsituatie |
| `synthese` | ≥ 1 worked example in `vergelijkingstabel` of `beslisboom` |
| `actor` | ≥ 1 `voorbeeld_inline` met rol-context (bv. "Bestuurder Marleen De Cock") |

Als minimum niet gehaald wordt: log expliciet in eindrapport. Render produceert `> [!todo] Voorbeeld ontbreekt`-callout.

### Regel 14 — Voorbeelden uit drie toegestane bronnen

In volgorde van voorkeur:

1. **Uit bron-chunks** (eerste keuze, `confidence: grounded`):
   - CBN-adviezen bevatten vaak praktijkvoorbeelden — zoek expliciet in §"Voorbeeld"-secties
   - KB-WVV-artikelen soms in toelichting

2. **Bestaand `concreet_voorbeeld`** (uit schema 1.2/1.3, bij rewrite): omzetten naar substappen-formaat of inline.

3. **Synthese met cast** (laatste keuze, `confidence: inferred`): mag wanneer 1+2 niet volstaan. Voorwaarden:
   - Bedragen plausibel (geen extreme waarden voor een BV)
   - Scenario illustreert het concept — laat zien hoe de regel/formule werkt
   - Intern consistent — geen contradicties tussen substappen
   - Cast-namen uit `casts/globaal.yaml` (kies passend scenario-template)
   - `confidence: inferred` markeren, `_provenance.inputs` blijft naar bron-chunks (waaruit de regel komt) — niet naar verzonnen cijfers

**Anti-fabricatie-discipline**: bedragen in synthese-voorbeelden zijn **didactische illustratie**, niet feitelijke claim. Een examen-stagiair die het voorbeeld leest leert HOE de regel werkt, niet WAT specifieke bedragen zijn.

---

## Wijzigingen aan v3-regels

### Regel 1 (Centraliteit) — uitgebreid

Toegevoegd: een centraal concept krijgt ook **een visueel voorbeeld** (substappen met balans-tabel) waar relevant, niet alleen rijke tekstvelden.

### Regel 2 (Berekenbaar concept → voorbeeld) — uitgebreid

Voorbeeld is voortaan **gestructureerd** met substappen (zie Regel 8). Geen platte tekst meer als acceptabel voorbeeld.

### Regel 4 (Relaties expliciet) — gesplitst

Voortaan twee plekken:
- Verwarring-risico → `vergelijkingsparen[]`
- Andere relaties (onderdeel-van, specialisatie, trigger, ...) → `edges[]`

---

## Output-locatie aangepast

Schrijf naar `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/<concept-slug>.json` (sinds reorganisatie 2026-05-15; was `data/concept_records/`).

Eindrapport naar `data/extractie/<po>/v4-extraction-rapport.md` (versie-aanduiding).

---

## Anti-fabricatie blijft hard

Alle regels uit v3 §"Anti-hallucinatie-regels" blijven onverkort gelden:
- Elke claim verplicht `_provenance.inputs` met chunk_id(s)
- Geen wetsartikelnummers verzinnen
- Voorbeelden enkel met namen uit `casts/globaal.yaml`
- Bedragen in voorbeelden: ofwel uit chunks ofwel uit scenario-template (geen fantasie-bedragen)
- Confidence-types ongewijzigd: `grounded` / `inferred-from-aggregation` / `inferred`

---

## Beperkingen ongewijzigd

- NIET examen-vragen raadplegen
- NIET de bundle-JSONs aanpassen
- Werk in het Nederlands
- `status: "seed"` op nieuwe records
