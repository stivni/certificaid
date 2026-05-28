---
title: "Rentabiliteitsratio's"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.3.II.C
  - 1.9.V.B
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/rentabiliteits-ratios.json"
---

# Rentabiliteitsratio's

_Ratio_

🏛️ Kader · Anchors: `1.3.II.C` · `1.9.V.B` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: winstgevendheid-ratio's · profitability ratios · marge-ratio's — **Vertalingen**: en: profitability ratios · fr: ratios de rentabilité

## Definitie

🔗 Rentabiliteitsratio's meten hoe winstgevend een onderneming opereert ten opzichte van haar omzet, haar geïnvesteerd kapitaal of haar totale activa. Vijf kernratio's bouwen een gelaagde piramide: (1) brutomarge — verkoopwinst per euro omzet vóór operationele kosten; (2) nettomarge — winst na alle kosten en belastingen per euro omzet; (3) EBITDA-marge — operationele winst voor afschrijvingen, rente en belastingen (kapitaal-onafhankelijke maatstaf); (4) rentabiliteit eigen vermogen (return on equity, ROE) — winst per euro eigen vermogen; (5) rentabiliteit totaal activa (return on assets, ROA) — winst per euro geïnvesteerd kapitaal. Samen tonen ze of winst voortkomt uit margekracht (prijs vs kost) of uit kapitaal-efficiëntie (omloopsnelheid van de activa).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Rentabiliteit is de 'eindscore' van het ondernemen — wat blijft over voor de eigenaren na alle inspanningen? Zonder voldoende rentabiliteit verdroogt het bedrijf: geen reserves om herinvesteringen te doen, geen aantrekkingskracht voor extern kapitaal, geen buffer voor tegenslag. De vijf ratio's belichten verschillende niveaus: brutomarge meet productie-efficiëntie; nettomarge meet alles-inclusief; EBITDA meet operationele cash-generatie; ROE meet wat de aandeelhouder krijgt; ROA meet wat de activa opbrengen, los van financierings-mix. De DuPont-decomposition koppelt deze: ROE = nettomarge × omloopsnelheid activa × financiële hefboom — vertelt waarom een ROE laag of hoog is.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een aparte categorie? Liquiditeit en solvabiliteit meten overlevings-capaciteit; activiteit meet efficiëntie; rentabiliteit meet bestaansrecht. Een onderneming die jaren na jaar te lage rentabiliteit boekt verkleurt — zelfs als ze liquide en solvabel blijft, verliezen aandeelhouders interesse en investeren ze elders. Centrale benchmark: rentabiliteit moet hoger zijn dan de kapitaalkost (WACC) — anders vernietigt het bedrijf economische waarde, los van wat de boekhoudkundige winst zegt. Banken kijken in eerste instantie naar EBITDA-marge (capaciteit om interesten te dragen); aandeelhouders kijken naar ROE; analisten gebruiken ROA voor vergelijking tussen sectoren met verschillende kapitaalstructuren.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Aandeelhouders-rapportering en dividend-beleid — ROE en nettomarge zijn de hoofd-KPI's voor aandeelhouderswaarde.
- 🔗 Bank-kredietanalyse — EBITDA-marge wordt gebruikt om de interest coverage ratio (EBITDA / interest) te bouwen; standaard-covenant in bedrijfsleningen.
- 🔗 Strategische diagnose — DuPont-decomposition van ROE legt de oorzaak van rentabiliteit-tekort bloot (margekrachten? kapitaalbeslag? hefboom?).

## Sub-concepten

### 📦 Brutomarge  
_`ratio` (subconcept)_

#### Definitie

🔗 Brutomarge = (omzet − kostprijs verkopen) / omzet × 100 %. In de Belgische JR: (rubriek 70 − rubriek 60) / rubriek 70 voor handelsondernemingen; voor industriële ondernemingen: (omzet − aankopen − wijziging voorraad goed/bewerking) / omzet. Geeft de marge tussen verkoop en directe inkoopkost — basis-productiviteit van het businessmodel.

<small>📚 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubrieken 70 + 60 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 Brutomarge meet de prijszettings-macht. Hoog = waardevolle producten met lage kostprijs (luxe, merknamen, IP). Laag = commodities, prijsconcurrentie. Trend-daling is bijna altijd structureel: nieuwe concurrenten, dalende pricing power, of kostprijs-inflatie (grondstoffen) die niet doorgerekend kan worden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule brutomarge  
_`formule`_

🔗 Handel: brutomarge = (70 − 60) / 70 × 100 %. Industrie: (70 + 71 wijziging voorraad − 60 − 600/602 grondstoffen) / 70 × 100 %. Diensten: meestal niet gerapporteerd (geen kostprijs van diensten in MAR — bouw zelf op uit lonen + diensten gerelateerd).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Supermarkten: 15-25 %. Detailhandel non-food: 35-55 %. Industrie: 30-45 %. Luxe-merken: 60-80 %. Software/SaaS: 70-90 %. Apotheek: 25-30 % (gereguleerd). Boekhandel: 30-40 %. Trend-vergelijking belangrijker dan absoluut niveau.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Nettomarge  
_`ratio` (subconcept)_

#### Definitie

🔗 Nettomarge = nettoresultaat / omzet × 100 %. Nettoresultaat = rubriek 9904 'te bestemmen winst (verlies) van het boekjaar' — na alle bedrijfsopbrengsten/kosten, financieel resultaat, uitzonderlijk resultaat, belastingen. Meet hoeveel van elke euro omzet uiteindelijk als winst voor de aandeelhouders overblijft.

<small>📚 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubriek 9904 + 70 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 Het 'alles-inclusief' eindgetal. Hier zit elke kost, elke fiscale tegenslag, elk uitzonderlijk item in. Lage nettomarge in een hoog-marge sector wijst op operationele inefficiëntie, te hoge schuld (rentekosten), of fiscale problemen. Vergelijking moet rekening houden met eenmalige effecten: een nettomarge boost door verkoop activa is niet duurzaam.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule nettomarge  
_`formule`_

🔗 Nettomarge = rubriek 9904 (te bestemmen winst boekjaar) / rubriek 70 (omzet) × 100 %. Voor zuiverder operationele vergelijking: bedrijfsresultaat-marge = rubriek 9901 / 70 × 100 % (REBIT = recurrent EBIT, zonder financieel + uitzonderlijk).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 KMO-gemiddelde Belgisch: 3-6 % nettomarge. Software: 15-30 %. Retail food: 1-3 % (volume-business). Industriële productie: 3-8 %. Bouw: 2-5 % (cyclisch). Negatief: alarmsignaal — meerjarige verliezen vragen continuïteits-toets.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 EBITDA-marge  
_`ratio` (subconcept)_

#### Definitie

🔗 EBITDA-marge = EBITDA / omzet × 100 %. EBITDA = bedrijfsresultaat (9901) + afschrijvingen en waardeverminderingen (630-631) + voorzieningen voor risico's en kosten (635-637). Maatstaf voor pure operationele cash-generatie — zuivert het beeld van afschrijvings-keuzes, kapitaalstructuur (interest) en fiscaliteit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 Bank-banker's favorite — toont 'echte' cash-genererings-capaciteit waaruit interesten betaald moeten worden. Gebruikt in interest coverage ratio (EBITDA / interestlasten ≥ 3-4× standaard-covenant) en debt service coverage. Ook gebruikt in M&A: EV/EBITDA-multiples zijn de standaard-waarderings-maatstaf. Aandacht: EBITDA verbergt kapitaalintensiteit — een 25 %-EBITDA-marge bij hoge afschrijvingen kan een 5 %-nettomarge worden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule EBITDA-marge  
_`formule`_

🔗 EBITDA = bedrijfsresultaat (rubriek 9901) + afschrijvingen + waardeverminderingen op immateriële + materiële vaste activa (630) + waardeverminderingen op voorraden en handelsvorderingen (631-634) + voorzieningen voor risico's en kosten (635-637). EBITDA-marge = EBITDA / omzet (70) × 100 %.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Industriële KMO: 8-15 %. Software/SaaS: 25-40 %. Retail food: 3-6 %. Telecom/utilities: 30-45 % (kapitaalintensief). Bouw: 5-10 %. Onder 5 % in industrie: kwetsbaar voor rente-stijging. Boven 30 % buiten software: vraag naar capex-cyclus.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Rentabiliteit eigen vermogen (ROE)  
_`ratio` (subconcept)_

#### Definitie

🔗 ROE = nettowinst / gemiddeld eigen vermogen × 100 %. Eigen vermogen = rubrieken 10-15 (kapitaal + uitgiftepremies + reserves + overgedragen resultaat). Gebruik gemiddelde (begin + einde) / 2 wanneer eigen vermogen sterk wijzigde door kapitaalverhoging of dividenduitkering. Meet hoeveel rente de eigenaren krijgen op hun ingebrachte + geherinvesteerde kapitaal.

<small>📚 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubrieken 10-15 + 9904 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 ROE is de aandeelhouders-KPI. Benchmark: vergelijken met de risicovrije rente (Belgische OLO) + risicopremie (typisch 5-7 % voor genoteerde, 8-12 % voor KMO). Een ROE < eigen kapitaalkost vernietigt aandeelhouderswaarde — ook als boekhoudkundig nog winst gemaakt wordt. Hoog ROE kan misleidend zijn wanneer het komt door hoge schuldfinanciering (financiële hefboom) — DuPont-decomposition isoleert dat effect.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule ROE + DuPont  
_`formule`_

🔗 ROE = nettoresultaat (9904) / gemiddeld EV × 100 %. DuPont-3-factor: ROE = nettomarge × omloopsnelheid totale activa × financiële hefboom = (winst/omzet) × (omzet/totaal-activa) × (totaal-activa/EV). Decomposeert ROE in margekracht, kapitaal-efficiëntie en schuldgraad-effect.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Belgische KMO-gemiddelde: 8-12 %. Boven 20 %: uitzonderlijk goed of door hoge hefboom. Onder 5 %: kapitaal-vernietigend (lager dan risicovrije rente + premie). Negatieve ROE: verlies. Stabiele 10-15 % over jaren = duurzame waardecreatie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Rentabiliteit totaal activa (ROA)  
_`ratio` (subconcept)_

#### Definitie

🔗 ROA = (nettowinst + rentelasten × (1 − belastingsvoet)) / gemiddeld totaal activa × 100 %. Gemiddeld totaal activa = balanstotaal — gemiddelde van begin en einde boekjaar. Belangrijk: tellen we de rente terug omdat ROA de productiviteit van het kapitaal meet onafhankelijk van de financierings-mix (schuld vs eigen).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🔗 ROA is de 'pure' rentabiliteit van het businessmodel — onafhankelijk van hoe gefinancierd. Daarom geschikt voor vergelijking tussen bedrijven met verschillende schuldgraden. Een onderneming met ROA > kost van kapitaal (WACC) creëert waarde; ROA < WACC vernietigt waarde. Onder 5 %: zwak gerendeerde activa-basis — vaak signaal van overcapaciteit of legacy activa.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule ROA  
_`formule`_

🔗 ROA-na-belastingen = (nettoresultaat 9904 + financiële kosten 65 × (1 − VenB-voet)) / gemiddeld balanstotaal × 100 %. Vereenvoudigde variant zonder hefboom-correctie: nettoresultaat / gemiddeld balanstotaal × 100 %. Pre-tax variant (ROCE — return on capital employed): bedrijfsresultaat / (EV + LT-schuld) × 100 %.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes  
_`drempel`_

🔗 Belgische KMO: 4-8 %. Kapitaalintensief (vastgoed, utility): 2-5 %. Light asset (consulting, software): 10-25 %. Retail food: 5-8 %. Onder 3 %: zwakke activa-rendement. ROE > ROA = positieve financiële hefboom (schuld voegt waarde toe); ROE < ROA = schuld te duur.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💡 DuPont-analyse — Zelena Bio NV (20X4) 🔗

_Zelena Bio NV: omzet 5.700, nettowinst 285, totaal activa 5.000, eigen vermogen 2.000 (1.000 EUR)._

**Berekening:**
- Nettomarge = 285 / 5.700 = 5,0 %
- Omloopsnelheid totale activa = 5.700 / 5.000 = 1,14×
- Financiële hefboom = 5.000 / 2.000 = 2,50×
- ROE (DuPont) = 5,0 % × 1,14 × 2,50 = 14,3 %
- ROA = 285 / 5.000 = 5,7 %
- Spread ROE − ROA = 8,6 % → positieve hefboom

→ **Resultaat**: ROE van 14,3 % is gezond (boven 12 %-benchmark). DuPont-decomposition toont: gematigde nettomarge (5 %) wordt versterkt door redelijke kapitaalomloop (1,14×) en gezonde hefboom (2,5× = schuldgraad ~60 %). De hefboom werkt positief: ROE > ROA → goedkope schuld levert toegevoegde waarde. Werkpunt: nettomarge omhoog door brutomarge-verbetering of kostenbeheersing — kapitaalomloop zit aan sectorlimiet.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Eénjaarse rentabiliteit als trend lezen

**Verkeerde assumptie**: Een ROE van 15 % betekent dat dit een rendabel bedrijf is.

**Kernpunt**: Eén jaar zegt weinig. Cyclische sectoren tonen hoge ROE in goede jaren, negatief in slechte. Beoordeel altijd over 3-5 jaar — gemiddelde + standaarddeviatie. Constante 10 % is beter dan jaren van 20 % afgewisseld met -5 %.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ ROE als universele KPI gebruiken

**Verkeerde assumptie**: Hogere ROE = beter bedrijf.

**Kernpunt**: Hoge ROE kan komen door extreme hefboom (sterke schuld) — wat het risico verhoogt. Vergelijk ROE altijd met ROA en kijk naar schuldgraad. Een ROE van 25 % met schuldgraad 90 % is fragiel; een ROE van 12 % met schuldgraad 40 % is solider.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Eenmalige effecten als duurzaam zien

**Verkeerde assumptie**: Nettomarge dit jaar 12 % is de nieuwe normaal.

**Kernpunt**: Boekwinsten op verkoop activa, terugname voorzieningen, uitzonderlijke fiscale credits — allemaal eenmalige boosters. Zuiver altijd: bedrijfsresultaat (9901) / omzet i.p.v. nettoresultaat als duurzaamheids-proxy. Lees rubrieken 76/66 (uitzonderlijke opbrengsten/kosten) in de toelichting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ EBITDA als 'cash flow' interpreteren

**Verkeerde assumptie**: Hoge EBITDA-marge = hoge cash-positie.

**Kernpunt**: EBITDA NEGEERT werkkapitaal-evolutie en capex. Een groeiend bedrijf met 20 % EBITDA-marge kan negatieve operationele kasstroom hebben wanneer werkkapitaal sterk stijgt. Combineer altijd EBITDA-marge met EBITDA-vs-operationele-kasstroom (capex moet ook gefinancierd) en EBITDA-vs-vrije-kasstroom.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Sector-mix negeren in vergelijkingen

**Verkeerde assumptie**: Bedrijf X heeft ROA 3 % en Y heeft ROA 18 %, dus Y is veel beter.

**Kernpunt**: ROA is sector-afhankelijk. Vastgoed-vennootschappen (hoog balansvolume): ROA 3-5 % is normaal. Consultancy (laag balansvolume): ROA 15-25 % is normaal. Vergelijk binnen sector, niet cross-sector.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Ratio-interpretatie cross-categorie (DuPont · cash-conversion-cycle) → [[ratio-interpretatie]] _(moet-verwijzen)_
- → Jaarrekeninganalyse Σ (parent) → [[jaarrekeninganalyse]] _(moet-verwijzen)_
- ↪ Financiële diagnose (geheel-oordeel) → [[financiele-diagnose]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]] — Rentabiliteits-ratio's vormen één van de vier ratio-categorieën binnen jaarrekening-analyse.
### `vereist`
- [[jaarrekening]] — Ratio's berekenen uit resultatenrekening + balans.
### `vergelijkbaar_met`
- [[solvabiliteits-ratios]]
    - **Gelijkenissen**:
        - Beide bouwen op eigen vermogen + balans-totaal
    - **Verschillen**:
        - Rentabiliteit = winst-perspectief; solvabiliteit = schuld-dekking-perspectief
    - ⚠️ **Verwarringsrisico**: ROE en schuldgraad zijn gekoppeld via DuPont-hefboomfactor — hoge ROE kan komen door zwakke solvabiliteit.
### `beinvloed_door`
- [[activiteits-ratios]] — DuPont-decomposition: ROA = nettomarge × omloopsnelheid activa. Activiteits-ratios bepalen mede de rentabiliteit.
### `triggert`
- [[ratio-interpretatie]] — Zwakke rentabiliteit triggert cross-categorie analyse via DuPont-decomposition.
