---
title: "Liquiditeitsratio's"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.3.II.C
  - 1.9.V.D
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/liquiditeits-ratios.json"
---

# Liquiditeitsratio's

_Ratio_

🏛️ Kader · Anchors: `1.3.II.C` · `1.9.V.D` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: liquiditeitsindicatoren · kortetermijn-ratio's — **Vertalingen**: en: liquidity ratios · fr: ratios de liquidité

## Definitie

🔗 Liquiditeitsratio's meten het vermogen van een onderneming om haar kortetermijn-verplichtingen (≤ 1 jaar) na te komen met haar kortetermijn-middelen. Vier kerngetallen vormen de standaardset: (1) current ratio (vlottende activa / kortlopende schulden); (2) quick ratio of acid test (vlottende activa − voorraden / kortlopende schulden); (3) cash ratio (liquide middelen / kortlopende schulden); (4) cash conversion cycle (DSO + DIO − DPO in dagen). Samen schetsen ze een gelaagd beeld van betaalcapaciteit: van breed (alle vlottende activa beschikbaar) tot eng (alleen pure cash) en dynamisch (hoeveel dagen kapitaal vastgepind in werkkapitaal).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Liquiditeit is het 'survival-vraag' — kan de onderneming morgen haar leverancier betalen, haar salarissen, haar BTW-aanslag? Een onderneming kan winstgevend zijn op papier en toch failliet gaan wegens liquiditeitsproblemen ('profitable insolvency'). Vandaar de centrale plaats in elke analyse — vooral voor crediteuren en banken die op kortetermijn-zekerheid kijken. De vier ratio's zijn complementair, niet vervangend: een gezonde current ratio kan een liquiditeitscrisis verbergen wanneer de voorraden onverkoopbaar zijn (vandaar quick ratio); een gezonde quick ratio kan misleidend zijn wanneer de vorderingen oninbaar zijn (vandaar cash ratio); en alle stand-ratio's negeren de tijdsdimensie (vandaar cash conversion cycle).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een aparte categorie? Liquiditeit en solvabiliteit zijn fundamenteel verschillend. Solvabiliteit kijkt langetermijn (kan de onderneming uiteindelijk al haar schulden afbetalen?) — liquiditeit kijkt kortetermijn (kan ze deze maand betalen?). Een bedrijf kan zeer solvabel zijn (veel langetermijn-eigen-vermogen) en toch liquiditeitsproblemen hebben (alle cash in voorraad gestoken). Banken differentieren expliciet: liquiditeit voor kasfaciliteit, solvabiliteit voor investeringskrediet. De vier liquiditeitsratio's bieden een gradiënt — van mild (current) naar streng (cash ratio) — die toelaat de werkelijke 'kasknepen' te lokaliseren.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Krediet-beoordeling kortetermijn — banken bij kasfaciliteit, leveranciers bij krediet-toekenning, kredietverzekeraars.
- 📖 Going-concern-toets — ISA 570 lijst kortetermijn-liquiditeitsproblemen als trigger-indicator (negatieve werkkapitaal-positie, kortlopende schulden > vlottende activa).
- 🔗 Bank-covenants — kredietovereenkomsten bevatten vaak minimumdrempels voor current ratio (typisch ≥ 1,0 of ≥ 1,2). Breach activeert clausules (renteverhoging, vervroegde opeisbaarheid).

**⚠️ Risico**
- 🔗 Window-dressing risico (zie ook valkuilen): liquiditeitsratio's worden vaak gemanipuleerd rond balansdatum via tijdelijke factoring, late betalingen of cash-laad-en-los-bewegingen.

## Sub-concepten

### 📦 Current ratio (algemene liquiditeit)  
_`ratio` (subconcept)_

#### Definitie

🔗 Current ratio = vlottende activa / kortlopende schulden. Vlottende activa = voorraden (3) + vorderingen ≤ 1 jaar (40-41) + geldbeleggingen (50-53) + liquide middelen (54-58) + overlopende rekeningen actief (490). Kortlopende schulden = schulden ≤ 1 jaar (42-48) + overlopende rekeningen passief (492).

<small>📚 KB W.Venn. — MAR — klasse 3-5 + 42-49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 De breedste liquiditeitsmaat — geeft aan hoeveel keer de onderneming haar kortlopende schulden zou kunnen dekken als ze al haar vlottende activa zou liquideren. Vuistregel current ratio ≥ 1: vlottende activa volstaan voor kortlopende schulden. Maar: sterk sectorafhankelijk.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes per sector  
_`drempel`_

🔗 Algemene vuistregel: 1,5-2,0 voor industriële KMO is comfortabel. Onder 1,0: alarmsignaal. Boven 2,5: mogelijk te conservatief (cash- en voorraadoverschot). Sector-specifiek: supermarktketens 0,5-0,8 (extreme voorraadrotatie + leverancierskrediet); industriële productie 1,5-2,5; bouw 1,0-1,5 (hoge voorraad + lopende werken); IT-dienstverlening 2,0-3,0 (lage voorraad, snelle inning).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💡 Current ratio — Zelena Bio NV (20X4) 🔗

_Balans Zelena Bio NV per 31-12-20X4._

**Berekening:**
- Vlottende activa: voorraden 1.600 + handelsvorderingen 2.000 + liquide middelen 1.200 = 4.800 (1.000 EUR)
- Kortlopende schulden: handelsschulden 1.600 + overige schulden ≤ 1 jaar 1.600 = 3.200 (1.000 EUR)
- Current ratio = 4.800 / 3.200 = 1,50

→ **Resultaat**: 1,50 — gezond voor industriële KMO (benchmark 1,5-2,5). Boven 1,0-drempel, comfortabele buffer voor onverwachte vertragingen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Quick ratio (acid test)  
_`ratio` (subconcept)_

#### Definitie

🔗 Quick ratio = (vlottende activa − voorraden) / kortlopende schulden. Identiek aan current ratio maar voorraden (klasse 3) worden uit de teller gehaald. Reden: voorraden zijn de minst liquide vlottende activa — verkooptijd kan maanden zijn, en bij liquidatie vaak slechts 30-50 % van boekwaarde.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 Strenge liquiditeitsmaat — meet 'echte' kortetermijn-betaalkracht zonder afhankelijkheid van voorraadverkoop. Bij een handelsonderneming met grote voorraad (auto-dealer, juwelier) kan current ratio 2,0 en quick ratio 0,4 zijn — wat een totaal ander beeld geeft van kasknepen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Vuistregel quick ratio ≥ 1,0: vlottende activa zonder voorraden volstaan voor kortlopende schulden. Industriële KMO: 0,8-1,5 typisch. Dienstverlening (geen voorraad): quick ratio ≈ current ratio. Handel/distributie: vaak quick ratio veel lager dan current — 0,3-0,7 niet zeldzaam.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💡 Quick ratio — Zelena Bio NV (20X4) 🔗

_Zie balans Zelena Bio NV uit current-ratio voorbeeld._

**Berekening:**
- Vlottende activa zonder voorraden: 4.800 − 1.600 = 3.200
- Kortlopende schulden: 3.200
- Quick ratio = 3.200 / 3.200 = 1,00

→ **Resultaat**: 1,00 — minimaal aanvaardbaar. Combinatie current 1,50 en quick 1,00: voorraden vormen 1/3 van vlottende activa. Indien voorraad-verkoop traag zou zijn → onmiddellijke kasknepen. Werkpunt: voorraadrotatie verhogen of voorraad afbouwen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Cash ratio  
_`ratio` (subconcept)_

#### Definitie

🔗 Cash ratio = (liquide middelen + geldbeleggingen) / kortlopende schulden. Strengste stand-ratio: enkel rubrieken 50-58 (geldbeleggingen + liquide middelen) in de teller. Vorderingen ≤ 1 jaar worden weggehouden omdat hun werkelijke inning onzeker is.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 De 'crisis-ratio' — kan de onderneming morgen al haar schulden betalen zónder vorderingen te innen, zonder voorraad te verkopen, alleen met de huidige cash? Geen enkele onderneming streeft naar cash ratio = 1 (ongebruikt kapitaal); typisch 0,1-0,3 voldoende. Te hoog (> 0,5) wijst op cash-overschot zonder investeringsbestemming — kapitaalsverkwisting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Vuistregel: 0,1-0,3 voldoende. Onder 0,05: risicovol (geen buffer voor onverwachte vertraging). Boven 0,5: kapitaalsverkwisting tenzij voorbereiding voor grote uitgave (investering, dividend, overname).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💡 Cash ratio — Zelena Bio NV (20X4) 🔗

_Zie balans Zelena Bio NV._

**Berekening:**
- Liquide middelen: 1.200 (1.000 EUR)
- Kortlopende schulden: 3.200
- Cash ratio = 1.200 / 3.200 = 0,375

→ **Resultaat**: 0,375 — aan de hoge kant. Combinatie current 1,50 + quick 1,00 + cash 0,38: onderneming heeft voldoende cash maar wellicht te veel. Vraag: is dit voorbereiding op een specifieke uitgave (investering, dividend), of slordig kasbeheer? Cash-yield optimaliseren via geldbeleggingen of versnelde investering.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Cash conversion cycle (CCC)  
_`ratio` (subconcept)_

#### Definitie

🔗 CCC = DIO + DSO − DPO (in dagen). DIO = days inventory outstanding = (voorraden × 365) / kostprijs verkopen; DSO = days sales outstanding = (handelsvorderingen × 365) / omzet; DPO = days payables outstanding = (handelsschulden × 365) / aankopen. CCC = aantal dagen waarin geld 'vast zit' in het werkkapitaal — van betaling leverancier tot inning klant.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 De dynamische liquiditeitsmaat — voegt tijdsdimensie toe aan de stand-ratio's. Een CCC van 60 dagen betekent dat de onderneming 60 dagen werkkapitaal moet financieren (voorraad + klanten − leveranciers). Kortere CCC = minder werkkapitaal-financiering nodig = lagere financiële kosten. Sommige bedrijven hebben negatieve CCC (supermarkten: klanten betalen meteen, leveranciers pas na 30-60 dagen) — die genereren cash via groei.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Sector-specifiek. Supermarkt: -10 tot -30 dagen (negatieve cyclus, cash-genererend). Industriële KMO: 40-90 dagen typisch. Bouw: 90-180 dagen (lange werkduur + onderhandse marktwerking). Detailhandel non-food: 30-60 dagen. Stijgende CCC over jaren is alarmsignaal — voorraadprobleem of inningsprobleem of beide.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💡 Cash conversion cycle — Zelena Bio NV (20X4) 🔗

_Zelena Bio NV: omzet 5.700, kostprijs verkopen 3.600 (rubriek 60+61), aankopen ≈ 3.000._

**Berekening:**
- DIO = 1.600 × 365 / 3.600 = 162 dagen voorraadrotatie
- DSO = 2.000 × 365 / 5.700 = 128 dagen klantenkredieten
- DPO = 1.600 × 365 / 3.000 = 195 dagen leverancierskrediet
- CCC = 162 + 128 − 195 = 95 dagen

→ **Resultaat**: 95 dagen — boven sectorgemiddelde voedingsindustrie (typisch 40-70). Hoge DIO (162 d) en hoge DSO (128 d) wijzen op werkkapitaal-spanning. Werkpunt: voorraadrotatie versnellen + klantenkrediettermijn verkorten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Vuistregels universaal toepassen

**Verkeerde assumptie**: Current ratio < 1 = automatisch slecht.

**Kernpunt**: Sector-specifiek. Supermarkten (Delhaize, Carrefour) hebben structureel current ratio < 1 wegens razendsnelle voorraadrotatie + langere leverancierskrediettermijn. Vergelijken met sector-benchmark, niet met algemene vuistregel.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Voorraad-waardering negeren

**Verkeerde assumptie**: Voorraden zijn een betrouwbare component van vlottende activa.

**Kernpunt**: Voorraadwaardering is sterk schatting-afhankelijk: FIFO/gemiddelde kostprijs, waardeverminderingen op verouderde of incourante stock, lange productiecycli. Een current ratio van 2,0 met grotendeels obsolete voorraad is misleidend. Kijk altijd naar voorraadrotatie (DIO) en waardeverminderingen in toelichting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Window-dressing onopgemerkt laten

**Verkeerde assumptie**: Liquiditeitsratio's per balansdatum reflecteren de normale situatie.

**Kernpunt**: Ratio's worden vaak gemanipuleerd rond balansdatum: factoring zonder regres (vorderingen → cash), aflossing schulden net vóór jaareinde (terug opgenomen in januari), versnelde inningscampagne. Vergelijk balansdatum-ratio's met meerdere tussentijdse staten of mediaan over een jaar — niet enkel het 'snapshot'.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Stand-ratio's zonder dynamische check gebruiken

**Verkeerde assumptie**: Current/quick/cash ratio geven een volledig liquiditeitsbeeld.

**Kernpunt**: Stand-ratio's zijn momentopnames; ze missen de tijdsdimensie. Combineer altijd met cash conversion cycle (dynamisch) en kasstroomanalyse (operationele kasstroom). Onderneming met current 1,5 en CCC 180 dagen heeft veel werkkapitaal-financiering nodig — bank-buffer staat onder druk.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Eén-ratio-één-jaar-conclusies trekken

**Verkeerde assumptie**: Een current ratio van 1,2 is voldoende informatie om een liquiditeitsoordeel te geven.

**Kernpunt**: Combineer altijd: (a) vier liquiditeitsratio's; (b) trend over 3-5 jaar; (c) sectorbenchmark; (d) kwalitatieve signalen (rappels, betalingsachterstanden BTW/RSZ — gepubliceerd in jaarverslag). Eén-ratio-één-jaar wordt routinematig misleidend.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Ratio-interpretatie cross-categorie (DuPont · K-techniek) → [[ratio-interpretatie]] _(moet-verwijzen)_
- → Jaarrekeninganalyse Σ (parent) → [[jaarrekeninganalyse]] _(moet-verwijzen)_
- ↪ Financiële diagnose (geheel-oordeel) → [[financiele-diagnose]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]] — Eerste ratio-categorie binnen jaarrekening-analyse.
### `vereist`
- [[jaarrekening]] — Ratio's berekenen uit balans + resultatenrekening.
### `vergelijkbaar_met`
- [[solvabiliteits-ratios]]
    - **Gelijkenissen**:
        - Beide gaan over schuld-dekking
    - **Verschillen**:
        - Liquiditeit = korte termijn (≤ 1 jaar); solvabiliteit = lange termijn
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken 'liquide' en 'solvabel' soms door elkaar — liquide = momentaan kan betalen; solvabel = uiteindelijk al haar schulden kan afbetalen.
### `beinvloed_door`
- [[activiteits-ratios]] — Voorraadrotatie + klantenkrediettermijn (DIO + DSO) zijn componenten van CCC én indicatoren van activiteits-efficiëntie.
### `triggert`
- [[kasstroom-analyse]] — Liquiditeitsalarm via ratio's → grondige kasstroom-analyse voor diagnose.
