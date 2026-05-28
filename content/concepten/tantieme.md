---
title: "Tantième"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.IV.B
  - 2.3.II
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/tantieme.json"
---

# Tantième

_Regime_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.IV.B` · `2.3.II` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: winstaandeel bestuurder · variabele bestuurdersvergoeding op winst · veranderlijk tantième

## Definitie

📖 Een tantième is een veranderlijke vergoeding toegekend aan een bestuurder of zaakvoerder, berekend in functie van de nettowinst van het boekjaar, en goedgekeurd door de algemene vergadering bij de winstbestemming. Wettelijk gekwalificeerd als 'bezoldiging van een bedrijfsleider' (art. 32 WIB92), niet als dividend. Boekhoudkundig geboekt op rekening 695 'Bestuurders of zaakvoerders' als onderdeel van de winstverdeling (niet als gewone bedrijfskost).

<small>📚 WIB92 — art. 32 — _wettekst_ · CBN-advies 2016/15 — rekening 695 — bestuurders of zaakvoerders — _advies_</small>

## Substantie

🔗 Het tantième is een hybride concept: vennootschapsrechtelijk een winstuitkering (en dus onderworpen aan de kapitaalbescherming — netto-actief-test bij NV, dubbele test bij BV), maar fiscaal een bezoldiging. Dit dubbele karakter geeft een speciale fiscale eigenschap: een tantième beslist door de algemene vergadering tijdens jaar Y+1 (bij de behandeling van de jaarrekening van Y) is bij de vennootschap aftrekbaar in jaar Y — niet in Y+1. Dat is een uitzondering op het matching-principe en is fiscaal interessant: men kan na boekjaareinde nog beslissen om winst van Y te 'verlagen' door een tantième toe te kennen, dat dan in Y belast wordt bij de bestuurder en aftrek wordt bij de vennootschap voor datzelfde jaar Y.

<small>📚 WIB92 — art. 195 + art. 49 (aftrekbaarheid beroepskosten) — _wettekst_ · CBN-advies 2016/15 — tantieme als winstverdeling — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een tantième? Twee redenen. Eerste: prestatiekoppeling — bestuurders die meer winst genereren krijgen meer; verliesjaren leveren geen tantième. Tweede: fiscale optimalisatie van het KMO-tarief in VenB. Een kleine vennootschap betaalt 20% VenB op de eerste 100.000 EUR winst, op voorwaarde dat een bestuurder minstens 45.000 EUR bezoldiging krijgt (bezoldigingsregel art. 215 WIB92). Het tantième kan na boekjaareinde worden ingezet om die drempel alsnog te bereiken — flexibeler dan een vast maandloon.

<small>📚 WIB92 — art. 215 (bezoldigingsregel KMO-tarief) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 32 + 195; WVV (kapitaalbescherming uitkeringen); CBN-advies 2016/15

**✅ Voor**
- 🔗 Beloning van bestuurders in functie van bedrijfsprestaties — vooral in kleine vennootschappen waar bestuurder ook aandeelhouder is.
- 📖 Halen van de 45.000 EUR-bezoldigingsdrempel voor het KMO-tarief in VenB als de vaste bezoldiging niet volstaat.

**📋 Voorwaarden**
- 📖 Beslissing door de algemene vergadering bij de behandeling van de jaarrekening — als onderdeel van het winstbestemmings-besluit.
- 📖 Respect voor de kapitaalbescherming: het tantième mag niet leiden tot uitkering boven de uitkeerbare winsten (WVV art. 5:142 voor BV, art. 7:212 voor NV).
- 🔗 Tijdige boeking en bedrijfsvoorheffing: bij toekenning wordt op de bruto-tantieme bedrijfsvoorheffing ingehouden en aangegeven via fiche 281.20.

**👍 Voordeel**
- 🔗 Aftrekbaar in het jaar waarop het betrekking heeft (jaar Y), ook al wordt het toegekend in jaar Y+1 — laat fiscale planning toe na boekjaareinde.
- 🔗 Lager belast dan dividend in veel scenario's: tantième is beroepsinkomen (progressieve PB-tarieven na sociale bijdragen-aftrek) versus dividend (RV 30%, of VVPRbis 15%, of liquidatiereserve 10%).

**⚠️ Risico**
- 📖 Herkwalificatie als verkapte dividend-uitkering bij gebrek aan reele tegenprestatie (CBN 2016/15): de bezoldiging moet in redelijk verband staan tot de geleverde prestaties.
- 🤖 Sociale bijdragen: tantième valt onder de sociale bijdragen-grondslag van zelfstandige bedrijfsleiders — kan tot 21,5% kostprijs opdrijven boven de PB-belasting.

## Sub-concepten

### 📦 Aftrekbaarheid in jaar Y bij toekenning in jaar Y+1  
_`regime` (subconcept)_

#### Definitie

🔗 Het tantième beslist door de AV in jaar Y+1 (bij de behandeling van de jaarrekening van Y) is bij de vennootschap aftrekbaar in jaar Y. Dit is een afwijking van het matching-principe en de jaarlijkheidsregel: normaliter zijn kosten aftrekbaar in het jaar waarin ze worden toegekend. Voor tantièmes geldt de bijzondere regel dat ze aansluiten bij het boekjaar waarop ze betrekking hebben, mits boeking als schuld (rekening 489 of vergelijkbaar) en effectieve toekenning binnen redelijke termijn na boekjaareinde.

<small>📚 WIB92 — art. 195 + 49 — _wettekst_ · CBN-advies 2016/15 — boeking tantieme — _advies_</small>

#### Substantie

🔗 Praktisch verloop: 31/12/Y is balansdatum. De jaarrekening wordt opgesteld in jaar Y+1. De gewone algemene vergadering (binnen 6 maanden) keurt de jaarrekening goed en beslist de winstbestemming, inclusief eventueel tantième. Het tantième-bedrag wordt geboekt op 31/12/Y als schuld jegens bestuurder (rekening 489) en als last (resultaatbestemming, rekening 695). Belastbaar bij de bestuurder in jaar Y+1 (jaar van toekenning), aftrekbaar bij de vennootschap in jaar Y.

<small>📚 CBN-advies 2016/15 — tijdslijn boeking — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Tantième versus dividend  
_`kader` (subconcept)_

#### Substantie

🔗 Beide zijn winstbestemmingen, maar fundamenteel verschillend.

<small>📚 WIB92 — art. 32 versus art. 18 — _wettekst_</small>

**Weergave** `vergelijkingstabel`:

```json
{
  "titel": "Tantième versus dividend",
  "kolommen": [
    "Aspect",
    "Tantième",
    "Dividend"
  ],
  "rijen": [
    [
      "Ontvanger",
      "Bestuurder",
      "Aandeelhouder"
    ],
    [
      "Fiscale categorie",
      "Bedrijfsleidersbezoldiging (art. 32 WIB92)",
      "Roerend inkomen (art. 18 WIB92)"
    ],
    [
      "Belasting bij ontvanger",
      "Progressieve PB-tarieven (na aftrek sociale bijdragen)",
      "RV 30% (of VVPRbis 15%, liquidatiereserve 10%)"
    ],
    [
      "Aftrekbaar bij vennootschap?",
      "Ja — als beroepskost (rekening 695)",
      "Nee — winstuitkering, niet aftrekbaar"
    ],
    [
      "Aftrek in welk jaar?",
      "Jaar waarop het betrekking heeft (Y, ook al beslist in Y+1)",
      "Niet aftrekbaar"
    ],
    [
      "Sociale bijdragen?",
      "Ja — zelfstandige bedrijfsleider",
      "Nee"
    ],
    [
      "Bezoldigingsregel KMO?",
      "Telt mee voor 45.000 EUR-drempel",
      "Telt niet mee"
    ]
  ]
}
```

## Voorbeelden

### 💡 Tantième om KMO-tarief te halen 🔗

_BV Optima sluit 2025 af met een winst voor tantième en VenB van 120.000 EUR. De zaakvoerder ontving in 2025 een vaste bezoldiging van 30.000 EUR — te weinig voor de bezoldigingsregel (45.000 EUR) van het KMO-tarief. De AV in mei 2026 beslist een tantième van 15.000 EUR toe te kennen voor boekjaar 2025._

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Tantième als gewone bedrijfskost boeken

**Verkeerde assumptie**: Tantième is een vergoeding, dus boeking onder rekening 618 'Bezoldigingen, premies' of 600-reeks.

**Kernpunt**: Tantième is winstverdeling, geen bedrijfskost. Boeking op rekening 695 'Bestuurders of zaakvoerders' onder de resultaatverwerking (CBN 2016/15). Dat is niet alleen rubricering — boeking als bedrijfskost zou het bedrijfsresultaat verlagen en de bestemmings-volgorde verstoren.

<small>📚 CBN-advies 2016/15 — rekening 695 — _advies_</small>

### ⚠️ Aftrek in verkeerde jaar

**Verkeerde assumptie**: Tantième beslist in mei 2026 = aftrekbaar in 2026.

**Kernpunt**: Tantième is aftrekbaar in het jaar waarop het betrekking heeft (jaar Y), niet in het jaar van toekenning (Y+1). Mits correcte boeking op 31/12/Y als schuld en effectieve toekenning binnen redelijke termijn. Vergeet niet: voor de bestuurder is het wel belastbaar in Y+1 (jaar van toekenning).

<small>📚 WIB92 — art. 195 + 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Tantième bij verlies of onvoldoende uitkeerbare winsten

**Verkeerde assumptie**: Een tantième kan altijd worden toegekend om belasting te verlagen.

**Kernpunt**: Tantième is een winstuitkering en valt onder de kapitaalbescherming. Bij verlies of onvoldoende uitkeerbare winsten (cf. netto-actief-test in NV, dubbele test in BV) is toekenning verboden — overtreding kan leiden tot terugvordering en aansprakelijkheid van de bestuurder.

<small>📚 CBN-advies 2016/15 — kapitaalbescherming — _advies_</small>

### ⚠️ Niet-redelijke tantième als verkapte dividend

**Verkeerde assumptie**: Het tantième kan vrij worden gekozen om fiscale optimalisatie te maximaliseren.

**Kernpunt**: Het tantième moet in redelijk verband staan tot de geleverde prestaties. Bij excessieve tantièmes — vooral wanneer bestuurder en aandeelhouder dezelfde persoon zijn — kan de fiscus het herkwalificeren als verkapt dividend, met weigering van aftrek en RV-toepassing.

<small>📚 CBN-advies 2016/15 — herkwalificatie verkapte uitkering — _advies_</small>

## Speelruimtes

### 🎚️ Tantième versus bonus versus dividend

## Accountant-perspectieven

### Accountant als fiscaal adviseur — tantième-optimalisatie

#### 💰 Fiscaal adviseur

##### 👣 Tantième-advies bij jaarafsluiting  
_`stap`_

**Substantie**: 🔗 Stap 1: Bepaal voorlopige belastbare winst voor tantième. Stap 2: Controleer de gerealiseerde bezoldiging (vast + voordelen van alle aard) versus de 45.000 EUR-drempel voor KMO-tarief. Stap 3: Indien onder drempel: bereken het tantieme nodig om drempel te halen. Stap 4: Vergelijk gecombineerde belastingdruk (VenB + sociale bijdragen + PB) voor verschillende tantième-niveaus. Stap 5: Adviseer optimum + documenteer redelijkheid (in verband met prestaties) ter beveiliging tegen herkwalificatie.

<small>📚 WIB92 — art. 215 + 32 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boekingen tantième  
_`stap`_

**Substantie**: 📖 Op 31/12/Y (na AV-besluit van Y+1): boeking 695 'Bestuurders of zaakvoerders' tegen 489 'Andere schulden — bestuurders'. Bij betaling in Y+1: 489 tegen bank, inhouding bedrijfsvoorheffing en aangifte via fiche 281.20. Vermelding in toelichting jaarrekening Y onder winstverdeling.

<small>📚 CBN-advies 2016/15 — boeking tantieme — _advies_</small>

## Verder lezen (scope-out)

- → Winstuitkering-Sigma als parent → [[winstuitkering]] _(moet-verwijzen)_
- → Winstbestemming — toekenningsmoment → [[winstbestemming]] _(moet-verwijzen)_
- → Bedrijfsleidersbezoldiging — Sigma-context als bouwblok → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_
- ↪ KMO-tarief VenB-context (45.000 EUR bezoldigingsregel) → [[kmo-tarief-vennootschapsbelasting]] _(mag-verwijzen)_
- → Algemene vergadering — besluit → [[algemene-vergadering]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[winstuitkering]]
- [[bedrijfsleidersbezoldiging]]
### `triggert`
- [[winstbestemming]]
### `beinvloed_door`
- [[algemene-vergadering]]
