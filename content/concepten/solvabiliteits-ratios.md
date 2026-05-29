---
title: "Solvabiliteitsratio's"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.3.II.C
  - 1.9.V.C
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/solvabiliteits-ratios.json"
---

_Ratio_ · ook: solvabiliteitsindicatoren · langetermijn-ratio's

## Definitie

Solvabiliteitsratio's meten het langetermijn-vermogen van een onderneming om aan al haar schulden te voldoen — niet enkel kortetermijn (zoals liquiditeitsratio's), maar de volledige schuldenlast tegenover het eigen vermogen en de winstcapaciteit. Vier kernindicatoren: (1) schuldgraad = vreemd vermogen / totaal vermogen; (2) solvabiliteitsratio = eigen vermogen / totaal vermogen (spiegelbeeld); (3) debt-to-equity = vreemd vermogen / eigen vermogen; (4) interest coverage ratio = EBIT / financiële kosten. Samen schetsen ze de financieringsstructuur (stock-perspectief: balans) en het schuld-bedieningsvermogen (flow-perspectief: resultatenrekening).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Solvabiliteit is de 'duurzaamheids-vraag' — kan de onderneming uiteindelijk al haar schulden afbetalen, zelfs als ze morgen zou liquideren? Eigen vermogen vormt de buffer tegen verliezen: hoe hoger het EV-aandeel, hoe meer verlies de onderneming kan dragen vóór de schuldeisers risico lopen. Een onderneming kan kortetermijn-liquide zijn maar langetermijn-insolvabel (negatief EV bij gestapelde verliezen — alarmbel WVV art. 5:153 / 7:228). Banken kijken voor langetermijn-financiering (investeringskrediet, hypothecaire lening) primair naar solvabiliteit; voor kortetermijn (kasfaciliteit) naar liquiditeit. De interest coverage ratio voegt een dynamisch element toe: kan de onderneming uit haar courante exploitatie de rentelasten dragen?

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Waarom een aparte categorie naast liquiditeit? Liquiditeit gaat over timing (kan ze déze week betalen?); solvabiliteit over substantie (heeft ze überhaupt genoeg eigen vermogen om alle schulden te dragen?). Een bedrijf kan liquide en insolvabel zijn (genoeg cash op korte termijn, maar negatief eigen vermogen door gestapelde verliezen) — typisch een 'walking dead'-onderneming, op weg naar faillissement. Omgekeerd: solvabel maar illiquide (veel eigen vermogen in vastgoed gestoken, weinig cash). Solvabiliteit is wettelijk verankerd via de alarmbel-procedure (WVV art. 5:153 BV / 7:228 NV): zodra netto-actief onder een drempel daalt, moet het bestuursorgaan formeel beslissen over voortzetting of ontbinding.

<small>📖 WVV — art. 5:153 (BV) / art. 7:228 (NV) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Langetermijn-financieringsbeoordeling door banken — investeringskrediet, hypothecaire lening, obligatie-uitgifte.
- 📖 Wettelijke alarmbel-toetsing (WVV art. 5:153 BV / art. 7:228 NV) — netto-actief vs drempelwaarden.
- 📖 Continuïteits-beoordeling (ISA 570 + CBN 2018/18) — negatief eigen vermogen is een sterke trigger-indicator.

**⚠️ Risico**
- 🔗 Eigen vermogen-vertekening door immateriële vaste activa en oprichtingskosten zonder reële waarde: schijnbare solvabiliteit dekt werkelijke insolventie.

## Sub-concepten

### 📦 Schuldgraad

#### Definitie

Schuldgraad = vreemd vermogen / totaal vermogen × 100 %. Vreemd vermogen = schulden > 1 jaar (rubriek 17) + schulden ≤ 1 jaar (42-48) + voorzieningen (16) + uitgestelde belastingen (168). Totaal vermogen = balanstotaal.

<small>🔗 KB W.Venn. — MAR — klasse 16-17 + 42-48 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

De meest courante solvabiliteitsmaat: welk aandeel van het totale vermogen wordt door derden gefinancierd? Hoe hoger, hoe groter de afhankelijkheid van schuldeisers en hoe gevoeliger voor renteschommelingen en kredietweigering. Vuistregel ≤ 60-70 % aanvaardbaar; > 80 % verhoogd risico; > 100 % betekent negatief eigen vermogen (insolventie).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes

Sector-specifiek. Industriële KMO: 50-70 % typisch. Vastgoed: 60-80 % (hoge hefboom op stabiele activa). Bouw: 60-75 %. IT/consultancy: 30-60 % (weinig vaste activa, weinig schuld). Boven 80 %: alarm; boven 100 %: negatief EV — alarmbel WVV.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Schuldgraad — Zelena Bio NV (20X4)
> _Balans Zelena Bio NV per 31-12-20X4, balanstotaal 8.000.000 EUR._
>
> **Berekening:**
>
> - Vreemd vermogen: schulden > 1 jaar 2.000 + handelsschulden 1.600 + overige schulden ≤ 1 jaar 1.600 = 5.200 (1.000 EUR)
> - Totaal vermogen: 8.000
> - Schuldgraad = 5.200 / 8.000 × 100 = 65 %
>
> → **Resultaat**: 65 % — gezond voor industriële KMO (benchmark 50-70 %). Eigen vermogen-aandeel = 35 % — comfortabele buffer.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Solvabiliteitsratio (EV/totaal)

#### Definitie

Solvabiliteitsratio = eigen vermogen / totaal vermogen × 100 %. Spiegelbeeld van schuldgraad: solvabiliteitsratio + schuldgraad = 100 %.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes

Vuistregel ≥ 25 % voor KMO. Belgische sectorgemiddelden: industrie 30-40 %, dienstverlening 40-50 %, vastgoed 20-30 %. Onder 15 %: alarm. Negatief: insolventie.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Debt-to-equity (D/E)

#### Definitie

D/E = vreemd vermogen / eigen vermogen. Drukt de financiële hefboom expliciet uit: hoeveel euro schuld per euro eigen vermogen? D/E = 2 betekent 2 euro schuld voor elke euro eigen kapitaal.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

Equivalent aan schuldgraad maar in andere vorm. D/E ratio is standaard in IFRS/internationale literatuur; Belgische analyse gebruikt vaker schuldgraad. Conversie: schuldgraad 65 % ↔ D/E ≈ 1,86. Hoge D/E (> 2-3) verhoogt aandeelhouders-rendement bij goede tijden (hefboom werkt positief) maar versnelt insolventie bij verliezen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- D/E — Zelena Bio NV
> _Balans Zelena Bio NV 20X4._
>
> **Berekening:**
>
> - Vreemd vermogen: 5.200
> - Eigen vermogen: 2.800
> - D/E = 5.200 / 2.800 = 1,86
>
> → **Resultaat**: 1,86 — gezond. Hefboom positief in goede tijden; weinig risico in slechte tijden gegeven solide rentabiliteit.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Interest coverage ratio (ICR)

#### Definitie

ICR = EBIT / financiële kosten (rentebetalingen). Drukt uit hoeveel keer de bedrijfswinst de financiële lasten dekt. ICR = 5 betekent dat de winst 5 keer de rente kan dragen vóór er een tekort ontstaat.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

Dynamische solvabiliteitsmaat — vult de stock-ratio's (schuldgraad, D/E) aan met flow-perspectief. Een hoog leverbedrijf (lage schuldgraad) met aanhoudende verliezen kan toch in problemen komen wanneer ICR < 1 (EBIT volstaat niet voor rente). Banken hanteren ICR-covenants in kredietovereenkomsten — typisch ICR ≥ 2,0 of ≥ 3,0 (afhankelijk van rating).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark ICR

ICR ≥ 3,0: comfortabel; 1,5-3,0: aanvaardbaar voor stabiele cash-flow-sectoren; < 1,5: spanning; < 1,0: alarm (EBIT volstaat niet eens voor rente).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- ICR — Zelena Bio NV
> _Zelena Bio NV: EBIT 720, financiële kosten 90 (1.000 EUR)._
>
> **Berekening:**
>
> - EBIT: 720
> - Financiële kosten: 90
> - ICR = 720 / 90 = 8,0
>
> → **Resultaat**: 8,0 — zeer comfortabel. EBIT dekt rente 8 keer; ruim boven typische bank-covenant (≥ 3,0).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 📜 Alarmbel-procedure WVV art. 5:153 / 7:228

WVV koppelt expliciet wettelijke gevolgen aan solvabiliteits-crisis. BV: art. 5:153 — bestuursorgaan moet binnen 2 maanden algemene vergadering bijeenroepen wanneer netto-actief negatief dreigt te worden of beneden wettelijke drempels valt. NV: art. 7:228 — wanneer netto-actief < helft van inbreng (eerste drempel) of < kwart (tweede drempel). Daling onder absolute drempel (61.500 EUR voor BV) leidt tot mogelijke ontbinding door rechtbank. Solvabiliteitsratio's zijn dus niet enkel analyse-tool maar wettelijke alarm-indicator.

<small>📖 WVV — art. 5:153 (BV) / art. 7:228 (NV) — _wettekst_</small>

## Valkuilen

> [!warning]- Eigen vermogen ongecorrigeerd nemen
> **Verkeerde assumptie**: Eigen vermogen op de balans is reëel beschikbaar.
>
> **Kernpunt**: Voor analyse: corrigeer voor (a) oprichtingskosten (rubriek 20 — geen liquidatiewaarde, elimineren uit EV); (b) niet-opgevraagd kapitaal (101 — toekomstige bron, niet huidig EV); (c) eigen aandelen (16 — substractief). Reëel EV (na correcties) kan substantieel lager zijn dan boekwaarde EV. De analytische schuldgraad gebruikt het gecorrigeerde EV.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Achtergestelde leningen verkeerd classificeren
> **Verkeerde assumptie**: Achtergestelde leningen = vreemd vermogen.
>
> **Kernpunt**: Achtergestelde leningen van aandeelhouders kunnen voor analyse-doeleinden tot 'pseudo-eigen-vermogen' worden gerekend wanneer ze contractueel achtergesteld zijn aan alle andere schuldeisers en geen vaste terugbetalingsdatum hebben. Banken in kredietdossiers volgen die behandeling vaak — schuldgraad wordt dan beduidend lager. Bekend onder de term 'quasi equity'.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Off-balance financiering negeren
> **Verkeerde assumptie**: Schuldgraad uit balans is volledig.
>
> **Kernpunt**: Vóór IFRS 16 stond operationele leasing niet op de balans. In BE-GAAP staat operationele leasing nog steeds enkel als kost in resultatenrekening + verplichting in toelichting (niet-in-de-balans-verplichtingen). Voor reële schuldgraad: voeg gekapitaliseerde operationele leasing-verplichtingen toe aan vreemd vermogen + activa. Doet er sterk toe voor IFRS-comparabiliteit.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- ICR uit netto-resultaat berekenen
> **Verkeerde assumptie**: EBIT = nettoresultaat.
>
> **Kernpunt**: ICR gebruikt EBIT (bedrijfsresultaat — vóór financieel resultaat en belastingen). Netto-resultaat is al gecorrigeerd voor rente; ICR uit nettoresultaat berekenen geeft een veel te lage ratio. Correcte formule: EBIT / financiële kosten, of equivalent: (nettoresultaat + belastingen + rente) / rente.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Eigen kantoor — accountant als financieringsadviseur

_De gecertificeerd accountant adviseert het bestuursorgaan over stuur-maatregelen die de solvabiliteit beïnvloeden — vóór de wettelijke alarmbel-drempels (WVV art. 5:153 / 7:228) worden geraakt._

#### 🧭 Adviseur

##### 🧭 Solvabiliteits-positie sturen

**Substantie**: De accountant adviseert het bestuursorgaan over **stuur-maatregelen** die de solvabiliteitsratio's beïnvloeden vóór de wettelijke alarmbel-drempels worden geraakt. Vier hefbomen, gerangschikt van structureel naar incidenteel:

1. **Dividendpolitiek** — de uitkering moet zowel de **netto-actief-test** (BV: art. 5:142 WVV — netto-actief na uitkering ≥ 0 én geen daling onder het niet-uitkeerbare deel) als de **liquiditeitstest** (BV: art. 5:143 WVV — bestuursorgaan moet attesteren dat de vennootschap haar opeisbare schulden tijdens de twaalf maanden na uitkering kan blijven betalen) doorstaan. Bij lage solvabiliteit: **uitkering verlagen of opschorten** om eigen vermogen op te bouwen.

2. **Investeringsbeslissingen** — elk investerings-dossier wegen op het verwachte **return-on-investment** versus de impact op de **schuldgraad**. Vuistregel: financiering door schuld is verdedigbaar zolang de schuldgraad onder de sectorale benchmark blijft (industriële KMO ≤ 70%) **en** de interest coverage ratio comfortabel boven 3,0 blijft. Boven deze drempels: **kapitaalverhoging of leasing** verkiezen boven banklening.

3. **Schuldherstructurering** — bij oplopende schuldgraad: **looptijd verlengen** (kortetermijn-schuld omzetten naar langetermijn-schuld → verbetert liquiditeit én verlaagt rente-druk), **herfinancieren** tegen lagere rente, of achtergestelde-aandeelhouders-leningen onderhandelen (klasseren als quasi-equity in de analytische balans).

4. **Vermijden alarmbel-procedure** — actief monitoren van het netto-actief versus de wettelijke drempels: voor de **BV** geen kapitaal-drempel meer (WVV 2019) maar wel **negatief netto-actief**-trigger (art. 5:153 WVV); voor de **NV** klassieke drempels netto-actief < ½ of < ¼ van het kapitaal (art. 7:228 WVV). Tijdige bijsturing — via één van de drie bovenstaande hefbomen of via een **kapitaalverhoging** — voorkomt dat het bestuursorgaan formeel een algemene vergadering moet bijeenroepen.

Cross-link: [[winstuitkering]] (toetsen) en [[kapitaalbescherming]] (regels NV-kapitaal).

<small>📖 WVV — art. 5:142 + art. 5:143 + art. 5:153 — _wettekst_ · WVV — art. 7:228 — _wettekst_ · claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

_Waarom: De vier hefbomen zijn complementair en niet alternatief: een vennootschap met dalende solvabiliteit moet typisch **meerdere tegelijk** activeren. De volgorde structureel → incidenteel volgt de tijdshorizon: dividendpolitiek werkt permanent, schuldherstructurering geeft direct lucht, alarmbel-monitoring is de noodrem._

## Verder lezen (scope-out)

- → Ratio-interpretatie cross-categorie (DuPont · K-techniek) → [[ratio-interpretatie]] _(moet-verwijzen)_
- → Jaarrekeninganalyse Σ (parent) → [[jaarrekeninganalyse]] _(moet-verwijzen)_
- ↪ Financiële diagnose (geheel-oordeel) → [[financiele-diagnose]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]]
### `vereist`
- [[jaarrekening]]
### `vergelijkbaar_met`
- [[liquiditeits-ratios]]
    - **Gelijkenissen**:
        - Beide meten schuld-dekkings-capaciteit
    - **Verschillen**:
        - Liquiditeit = korte termijn; solvabiliteit = lange termijn + structureel
    - ⚠️ **Verwarringsrisico**: Studenten verwisselen liquiditeit en solvabiliteit — onthoud: liquide = nu betalen; solvabel = uiteindelijk betalen.
### `triggert`
- [[continuiteit]] — Negatief EV of schuldgraad > 100 % is sterke trigger voor going-concern-twijfel (ISA 570) en alarmbel-procedure (WVV).
### `beinvloed_door`
- [[rentabiliteits-ratios]] — Aanhoudende verliezen verlagen het eigen vermogen jaar na jaar en verzwakken solvabiliteit.
