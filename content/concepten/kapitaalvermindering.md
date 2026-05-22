---
title: "Kapitaalvermindering"
concept_type: "verrichting"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/kapitaalvermindering.json"
---

# Kapitaalvermindering

_Verrichting_

Model: `claude-sonnet-4-6` · Wave: `multipass-bench-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: terugbetaling van kapitaal · restitutie van kapitaal

## Voorkennis & leespad

**Voorvereisten**: [[eigen-vermogen]] · [[kapitaalverhoging]] · [[vennootschapsrechtelijk-kader-wvv]]
**Naast relevant**: [[inkoop-eigen-aandelen]] · [[uitkering-aan-aandeelhouders]] · [[liquidatiereserve]] · [[roerende-voorheffing]] · [[alarmbel]]
**Volgkennis**: [[ontbinding-en-vereffening]]

## Gebruikscontext


**✅ Voor**
- 🔗  <small>📚 WVV — Art. 7:194, Art. 7:195, Art. 7:196 — _wettekst_</small>
- 🔗  <small>📚 WVV — Art. 7:194, Art. 7:195, Art. 7:196 — _wettekst_</small>
- 🔗  <small>📚 WVV — Art. 7:194, Art. 7:195, Art. 7:196 — _wettekst_</small>

**📋 Voorwaarden**
- ❌  <small>📚 WVV — Art. 7:140 (NV: drie vierden van uitgebrachte stemmen voor statutenwijziging); Art. 7:194 (kapitaalvermindering = statutenwijziging) — _wettekst_</small>
- 📖  <small>📚 WVV — Art. 7:195 — _wettekst_</small>
- 📖  <small>📚 MvT-WVV-2018 — Art. 5:121 (netto-actief BV: mag niet negatief worden na uitkering) — _wettekst_</small>

**⚠️ Risico**: 📖  <small>📚 WIB92 — Art. 18 lid 2-6 (pro-rata) + Art. 269 §1 1° (RV 30%) — _wettekst_</small>

## Inhoud

### Vormen van kapitaalvermindering 🔗  
_`begrip`_

#### Terugbetaling met kasuitstroom  
_`begrip`_

#### Aanzuivering van verliezen  
_`begrip`_

<small>📚 WVV — Art. 7:194-7:196 — _wettekst_</small>

### Boekhoudkundige verwerking 🔗  
_`stap`_

#### Weergave · `boeking` 🔗

```json
{
  "scenario": "Terugbetaling kapitaal aan aandeelhouders",
  "regels": [
    {
      "rekening": "100",
      "omschrijving": "Geplaatst kapitaal",
      "debet": "X",
      "credit": ""
    },
    {
      "rekening": "55",
      "omschrijving": "Kredietinstellingen (of te betalen schulden)",
      "debet": "",
      "credit": "X"
    }
  ]
}
```

#### Weergave · `boeking` 🔗

```json
{
  "scenario": "Aanzuivering overgedragen verliezen",
  "regels": [
    {
      "rekening": "100",
      "omschrijving": "Geplaatst kapitaal",
      "debet": "X",
      "credit": ""
    },
    {
      "rekening": "14",
      "omschrijving": "Overgedragen verlies",
      "debet": "",
      "credit": "X"
    }
  ]
}
```

<small>📚 CBN-advies 2019/13 — Pro rata-regel + boekingen — _advies_</small>

### Fiscaal volgestort kapitaal 🔗  
_`begrip`_

<small>📚 WIB92 — Art. 184 — _wettekst_</small>

### Pro-rata-berekening (fiscale toerekening) 🔗  
_`formule`_

#### Weergave · `formule_expressie` ❌

```json
{
  "expressie": "Belastingvrij deel = Terugbetaling × (Fiscaal volgestort kapitaal ÷ (Fiscaal volgestort kapitaal + Belaste reserves + Uitgiftepremies niet-gekapitaliseerd))"
}
```

#### 💡  🤖

##### Weergave · `berekening` 🤖

```json
{
  "tabel": {
    "kolommen": [
      "Post",
      "Bedrag (€)"
    ],
    "rijen": [
      [
        "Fiscaal volgestort kapitaal",
        "400.000"
      ],
      [
        "Belaste reserves",
        "200.000"
      ],
      [
        "Overgedragen winst (uitkeerbaar)",
        "100.000"
      ],
      [
        "Totaal eigen vermogen (noemer)",
        "700.000"
      ],
      [
        "Pro-rata volgestort kapitaal",
        "400.000 / 700.000 = 57,14%"
      ],
      [
        "Terugbetaling (voorbeeld-bedrag)",
        "140.000"
      ],
      [
        "Belastingvrij deel (57,14%)",
        "80.000"
      ],
      [
        "Dividend-deel (42,86%)",
        "60.000"
      ],
      [
        "Roerende voorheffing 30% op dividend-deel",
        "18.000"
      ],
      [
        "Netto-ontvangst aandeelhouders samen",
        "122.000"
      ]
    ]
  }
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

<small>📚 WIB92 — Art. 18 lid 2-6 — _wettekst_ · CBN-advies 2019/13 — Pro rata-berekening voorbeeld — _advies_</small>

### Schuldeisersbeschermingsprocedure 📖  
_`stap`_

<small>📚 WVV — Art. 7:195 — _wettekst_</small>

### Samenloop met alarmbelprocedure 🔗  
_`mechanisme`_

<small>📚 MvT-WVV-2018 — Art. 7:214 + Art. 312 — _wettekst_</small>

### Roerende voorheffing op dividend-deel 📖  
_`regel`_

<small>📚 WIB92 — Art. 269 §1 1° — _wettekst_</small>

### Audit- en adviespunten voor de accountant 🤖  
_`risico`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Voorbeelden

### 💡  🔗

_Twee doorlopende cases illustreren de twee hoofdvormen: een terugbetaling met kasuitstroom (inclusief fiscale pro-rata-splitsing) en een aanzuivering van boekhoudkundige verliezen zonder kasuitstroom. Alle bedragen zijn fictief en dienen louter ter illustratie.

BV Optima heeft 2 aandeelhouders (elk 50%). Eigen vermogen vóór verrichting: fiscaal volgestort kapitaal 400.000 €, belaste reserves 200.000 €, overgedragen winst 100.000 € — totaal 700.000 €. De BAV beslist het kapitaal te verminderen met 140.000 € (van 400.000 € naar 260.000 €) en dit bedrag terug te betalen aan de aandeelhouders (elk 70.000 €). Schuldvrij bedrijf — geen schuldeiser eist zekerheid._

#### Stap 1 — BAV-beslissing en bekendmaking ❌  
_`stap`_

<small>📚 WVV — Art. 7:140 + Art. 7:195 — _wettekst_</small>

#### Stap 2 — Fiscale pro-rata-berekening 🔗  
_`stap`_

<small>📚 CBN-advies 2019/13 — Pro rata voorbeeld (noemer = gestort kap + belaste reserves) — _advies_ · WIB92 — Art. 18 lid 2-6 — _wettekst_</small>

#### Stap 3 — Boeking en uitbetaling 🔗  
_`stap`_

##### Weergave · `boeking` 🔗

```json
{
  "scenario": "Terugbetaling 140.000 € kapitaal — deels belastingvrij, deels dividend met RV",
  "regels": [
    {
      "rekening": "100",
      "omschrijving": "Geplaatst kapitaal",
      "debet": "140.000",
      "credit": ""
    },
    {
      "rekening": "453",
      "omschrijving": "Roerende voorheffing te betalen (30% × 60.000)",
      "debet": "",
      "credit": "18.000"
    },
    {
      "rekening": "55",
      "omschrijving": "Kredietinstellingen (netto-uitbetaling aandeelhouders)",
      "debet": "",
      "credit": "122.000"
    }
  ]
}
```

<small>📚 CBN-advies 2019/13 — Boekingen kapitaalvermindering — _advies_</small>

#### Stap 4 — Afdracht roerende voorheffing 📖  
_`stap`_

<small>📚 WIB92 — Art. 412 (RV betaalbaar binnen 15 dagen na toekenning) — _wettekst_</small>

<small>📚 CBN-advies 2019/13 — Pro rata voorbeeld — _advies_ · WIB92 — Art. 18 lid 2-6 — _wettekst_</small>

### 💡  🔗

_NV DeltaFab heeft geplaatst kapitaal van 500.000 € en overgedragen verliezen van 180.000 € (rekening 14 debet). De BAV beslist het kapitaal te verminderen met 180.000 € om de verliezen te neutraliseren, zodat nadien opnieuw dividenduitkering mogelijk wordt. Geen kasuitstroom — puur boekhoudkundige operatie. Schuldeisersbeschermingsprocedure is ook hier verplicht, ook al verlaat er geen geld de vennootschap._

#### Stap 1 — BAV en schuldeisersbescherming ❌  
_`stap`_

<small>📚 WVV — Art. 7:196 — _wettekst_</small>

#### Stap 2 — Boeking verliesaanzuivering 🔗  
_`stap`_

##### Weergave · `boeking` 🔗

```json
{
  "scenario": "Kapitaalvermindering 180.000 € ter aanzuivering overgedragen verliezen",
  "regels": [
    {
      "rekening": "100",
      "omschrijving": "Geplaatst kapitaal",
      "debet": "180.000",
      "credit": ""
    },
    {
      "rekening": "14",
      "omschrijving": "Overgedragen verlies (aanzuivering)",
      "debet": "",
      "credit": "180.000"
    }
  ]
}
```

<small>📚 CBN-advies 151/1 — Boekhoudkundige verwerking verliesaanzuivering — _advies_ · CBN-advies 2019/13 — Boekingen — _advies_</small>

#### Stap 3 — Herstelde dividendcapaciteit 🔗  
_`stap`_

<small>📚 WVV — Art. 7:196 + Art. 5:121 (uitkeringstest) — _wettekst_</small>

<small>📚 WVV — Art. 7:196 (verliesaanzuivering: geen schuldeisersbescherming Art. 7:195) — _wettekst_</small>

## Relaties

### `vergelijkbaar_met`
- [[inkoop-eigen-aandelen]] 🔗 — Beide verrichtingen keren vermogen terug aan aandeelhouders, maar via verschillende mechanismen: kapitaalvermindering verlaagt de balanspost kapitaal terwijl inkoop eigen aandelen leidt tot een aparte post op het eigen vermogen.
    - **Gelijkenissen**:
        - Beide keren economisch vermogen terug aan aandeelhouders
        - Fiscale pro-rata-regels zijn in beide gevallen van toepassing op het niet-volgestort-kapitaal-deel
        - Beide vereisen een beslissing van de algemene vergadering of bestuursorgaan
        - Beide verlagen het eigen vermogen van de vennootschap
        - Schuldeisers kunnen in beide gevallen de solvabiliteit zien dalen
    - **Verschillen**:
        - Kapitaalvermindering vereist notariële akte bij NV en statutenwijziging; inkoop eigen aandelen vereist dit niet
        - Inkoop eigen aandelen maakt de aandelen tot eigen aandelen van de vennootschap (schorsing stemrecht); kapitaalvermindering gaat gepaard met evenredige intrekking van aandelen of verlaging van de nominale waarde
        - Schuldeisersbeschermingsprocedure (twee maanden) geldt uitsluitend bij kapitaalvermindering, niet bij inkoop eigen aandelen
        - Boekhoudkundige verwerking verschilt: bij inkoop eigen aandelen ontstaat rekening 519; bij kapitaalvermindering daalt rekening 100
        - Inkoop eigen aandelen is reversibel (aandelen kunnen worden herverkocht); kapitaalvermindering is definitief
    - ⚠️ **Verwarringsrisico**: Beide worden soms aangeduid als 'teruggave aan aandeelhouders' maar hebben fundamenteel andere boekhoudkundige, vennootschapsrechtelijke en fiscale gevolgen; de schuldeisersbeschermingsprocedure is het meest onderscheidende kenmerk
- [[uitkering-aan-aandeelhouders]] 🔗 — Een gewone dividenduitkering en een kapitaalvermindering met terugbetaling hebben hetzelfde economische effect (geld naar aandeelhouder) maar de fiscale behandeling verschilt fundamenteel: terugbetaling van volgestort kapitaal is belastingvrij.
    - **Gelijkenissen**:
        - Kasuitstroom van de vennootschap naar de aandeelhouders
        - Beslissing van de (buitengewone) algemene vergadering vereist
        - Vermindering van het eigen vermogen van de vennootschap
        - Fiscale inhouding en aangifte roerende voorheffing door de vennootschap (tenzij volledig belastingvrij)
    - **Verschillen**:
        - Terugbetaling van fiscaal volgestort kapitaal is belastingvrij voor de aandeelhouder; gewone dividenduitkering is steeds onderworpen aan roerende voorheffing (30%)
        - Kapitaalvermindering wijzigt de statuten en vereist notariële akte (bij NV); dividenduitkering niet
        - Schuldeisersbeschermingsprocedure van twee maanden geldt enkel bij kapitaalvermindering
        - Pro-rata-berekening van het volgestort kapitaal is verplicht bij kapitaalvermindering; bij dividend niet
        - Kapitaalvermindering verlaagt de kapitaalbasis (rekening 100); dividend verlaagt de overgedragen winst of reserves
    - ⚠️ **Verwarringsrisico**: Fiscale herkwalificatie is het grootste risico: als de pro-rata-berekening onjuist wordt uitgevoerd, wordt de vermeend belastingvrije terugbetaling alsnog als dividend geherkwalificeerd en onderworpen aan 30% roerende voorheffing
- [[kapitaalverhoging]] 🔗 — Kapitaalvermindering is de omgekeerde beweging van een kapitaalverhoging: bij kapitaalverhoging stroomt kapitaal de vennootschap in, bij kapitaalvermindering stroomt het (deels) terug uit.
    - **Gelijkenissen**:
        - Beide vereisen een beslissing van de buitengewone algemene vergadering met bijzondere meerderheid
        - Beide wijzigen de statuten en vereisen notariële akte bij NV
        - Beide hebben directe impact op de solvabiliteit en de kapitaalstructuur van de vennootschap
        - Beide worden gepubliceerd via de Kruispuntbank van Ondernemingen
    - **Verschillen**:
        - Kapitaalverhoging verhoogt het eigen vermogen en de solvabiliteit; kapitaalvermindering verlaagt die
        - Schuldeisersbeschermingsprocedure van twee maanden is enkel verplicht bij kapitaalvermindering
        - Fiscale pro-rata-berekening en roerende voorheffing spelen enkel bij kapitaalvermindering met terugbetaling
        - Kapitaalverhoging vergt inbreng van nieuw vermogen of incorporatie van reserves; kapitaalvermindering stoot vermogen af of neutraliseert verliezen
    - ⚠️ **Verwarringsrisico**: Beide zijn vennootschapsrechtelijke kapitaaloperaties met dezelfde procedurele vereisten (BAV, notaris), maar hebben tegengestelde gevolgen voor schuldeisers — wat leidt tot een asymmetrisch beschermingsregime
### `triggert`
- [[alarmbel]] 🔗 — Een kapitaalvermindering met terugbetaling kan het netto-actief doen dalen onder de drempelwaarden (minder dan de helft of een kwart van het maatschappelijk kapitaal bij NV; netto-actieftest bij BV) die de alarmbelprocedure activeren.
### `beinvloed_door`
- [[roerende-voorheffing]] 🔗 — Het dividend-deel van de kapitaalvermindering (het gedeelte dat niet als fiscaal volgestort kapitaal kwalificeert) is onderworpen aan roerende voorheffing van 30%, in te houden door de vennootschap.
- [[kapitaalbescherming-en-winstverdeling]] 🔗 — De kapitaalbeschermingsregels uit het WVV (netto-actieftest bij BV, kapitaaldrempelregels bij NV) begrenzen de maximale omvang en de uitvoerbaarheid van een kapitaalvermindering.
- [[eigen-vermogen]] 🔗 — De samenstelling van het eigen vermogen (verhouding fiscaal volgestort kapitaal t.o.v. belaste reserves en uitgiftepremies) bepaalt de uitkomst van de pro-rata-berekening en dus het belastbaar dividend-deel bij een kapitaalvermindering met terugbetaling.
### `vereist`
- [[algemene-vergadering]] 🔗 — Een kapitaalvermindering vereist altijd een beslissing van de buitengewone algemene vergadering, met bijzondere meerderheid (in beginsel twee derde van de uitgebrachte stemmen).
- [[vennootschapsrechtelijk-kader-wvv]] 🔗 — De volledige procedure voor kapitaalvermindering — schuldeisersbescherming, BAV-beslissing, notariële akte bij NV, netto-actieftest bij BV — is verankerd in het WVV.
### `valt_onder`
- [[financiele-verrichtingen-categorie]] 🔗 — Kapitaalvermindering is een financiële verrichting (structuurwijziging eigen vermogen) en valt onder de categorie van financiële verrichtingen.
