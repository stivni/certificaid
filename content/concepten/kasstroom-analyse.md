---
title: "Kasstroomanalyse"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.9.IV
  - 1.9.IV.A
  - 1.9.IV.B
  - 1.9.IV.C
  - 1.9.IV.D
  - 1.9.IV.E
  - 1.9.IV.F
  - 1.9.IV.G
  - 1.9.IV.H
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/kasstroom-analyse.json"
---

# Kasstroomanalyse

_Kader_

🏛️ Kader · Anchors: `1.9.IV` · `1.9.IV.A` · `1.9.IV.B` · `1.9.IV.C` · `1.9.IV.D` · `1.9.IV.E` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: kasstroomoverzicht · cash flow statement · kasstroomstaat — **Vertalingen**: en: cash flow statement · fr: tableau de flux de trésorerie

## Definitie

📖 Een kasstroomanalyse maakt zichtbaar hoeveel cash een onderneming in een periode genereerde en aanwendde — verdeeld over drie categorieën die de bron én bestemming van cash tonen. IAS 7 (verplicht voor IFRS-rapporterende ondernemingen + voor de geconsolideerde jaarrekening in België) onderscheidt: (1) kasstromen uit bedrijfsvoering — operationele kern (cash van klanten min cash naar leveranciers en personeel); (2) kasstromen uit investeringen — aankoop/verkoop materiële, immateriële en financiële vaste activa; (3) kasstromen uit financiering — bewegingen in eigen vermogen en lange schuld. De som verklaart de stand-mutatie van liquide middelen tussen openings- en slotbalans.

<small>📚 IAS 7 — Cash Flow Statements — paragraaf 6 (definities) en 10 (3 categorieën) — _norm_</small>

## Substantie

🔗 De resultatenrekening vertelt 'hoeveel verdiende je?' op accrual-basis (toerekening). De kasstroomanalyse vertelt 'hoeveel cash kwam binnen en ging buiten?'. Beide horen je samen te lezen — winst zonder cash is gevaarlijk (lopende factoring, kapitalisatie van kosten, agressieve omzeterkenning kunnen winst tonen zonder kasinstroom). Klassiek diagnose-patroon: structureel hoge winst maar lage operationele kasstroom → controle van werkkapitaal (DSO, DIO stijgend?), accrual-componenten (voorzieningen, afschrijvings-keuzes) en mogelijke earnings management. Voor banken is operationele kasstroom de echte interestcoverage-bron — niet de winst.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 Waarom een afzonderlijk overzicht naast resultatenrekening + balans? Omdat winst en cash structureel uiteenlopen door (a) niet-kas-kosten (afschrijvingen, waardeverminderingen, voorzieningen), (b) werkkapitaal-bewegingen (omzet komt vóór de cash), (c) investeringen (capex passeert balans, niet resultatenrekening) en (d) financierings-bewegingen (lening opnemen ≠ winst). Pas een kasstroomanalyse maakt de werkelijke cash-cyclus zichtbaar en toetst de continuïteit. ISA 570 stelt 'negative cash flows from operating activities' expliciet als trigger-indicator voor going-concern-risico.

<small>📚 ISA 570 (herzien) — Going Concern — paragraaf A3 (events or conditions) — _norm_</small>

## Gebruikscontext


**✅ Voor**
- 📖 Geconsolideerde jaarrekening — IAS 7 verplicht kasstroomoverzicht; in België voor genoteerde ondernemingen + grote groepen. KMO-statutaire JR: niet verplicht maar sterk aanbevolen.
- 📖 Continuïteits-toets — ISA 570 + CBN-advies 2010/14 vragen om kasstroomprognose 12 maanden vooruit bij twijfel. Historische kasstroomanalyse vormt de basis voor de prognose.
- 🔗 Bedrijfswaardering — Discounted Cash Flow (DCF) methode bouwt op vrije kasstroom (FCF), die afgeleid wordt uit het kasstroomoverzicht.

**⚠️ Risico**
- 📖 Classificatie-fouten — IAS 7 laat keuze voor interest paid en dividend received (bedrijfsvoering of financiering); inconsequente keuze over jaren maakt vergelijking onmogelijk. Documenteer in waarderingsregels.

## Sub-concepten

### 📦 Drie kasstroom-categorieën (IAS 7)  
_`kader` (subconcept)_

#### Definitie

📖 IAS 7 paragrafen 13-17 verdelen cash-bewegingen verplicht in drie categorieën. Beslissingscriterium: de aard van de onderliggende activiteit, niet het balansrubriek waaruit ze komt. Voorbeeld: aflossing leasing-schuld → financiering; betaling huur operationele lease → bedrijfsvoering.

<small>📚 IAS 7 — paragrafen 13-17 — _norm_</small>

#### 💡 Kasstromen uit bedrijfsvoering  
_`begrip`_

📖 Operationele cash van/naar klanten, leveranciers, personeel, fiscus (bedrijfsbelastingen, btw saldo). Indicator van vermogen om operationeel cash te genereren — gewenst structureel positief. Sluit interest en dividend in OF uit afhankelijk van consequente keuze (IAS 7 par. 31-34).

<small>📚 IAS 7 — paragraaf 14 — _norm_</small>

#### 💡 Kasstromen uit investering  
_`begrip`_

📖 Aankoop/verkoop van vaste activa (materieel, immaterieel, financieel). Capex = aankoop materieel + immaterieel; desinvestering = verkoop. Typisch netto negatief bij groeiende onderneming; positief bij desinvesterende of inkrimpende onderneming.

<small>📚 IAS 7 — paragraaf 16 — _norm_</small>

#### 💡 Kasstromen uit financiering  
_`begrip`_

📖 Bewegingen in lange-termijn-financiering: opnemen/aflossen leningen, kapitaalverhogingen/-verminderingen, dividenduitkeringen, terugkoop eigen aandelen. Saldo toont financierings-strategie: positief = aantrekken externe middelen, negatief = teruggeven aan kapitaalverschaffers.

<small>📚 IAS 7 — paragraaf 17 — _norm_</small>

### 📦 Indirecte vs directe methode  
_`kader` (subconcept)_

#### Definitie

📖 Twee methoden voor bedrijfsvoering-kasstroom — beide leveren hetzelfde totaal. Directe methode toont rechtstreeks de operationele cash-stromen (ontvangsten klanten, betalingen leveranciers, lonen, ...). Indirecte methode start van nettowinst en corrigeert voor (a) niet-kas-items (afschrijvingen, voorzieningen, waardeverminderingen), (b) werkkapitaal-bewegingen (Δ vorderingen, Δ voorraden, Δ handelsschulden), (c) reclassificatie naar investering/financiering. IAS 7 staat beide toe (par. 18); in praktijk gebruikt 90+ % de indirecte methode wegens lager aanlevervolume.

<small>📚 IAS 7 — paragrafen 18-20 — _norm_</small>

#### 👣 Indirecte methode — conciliatie-stappen  
_`stap`_

🔗 Vertrekpunt: nettoresultaat (rubriek 9904). Stap 1: tel niet-kas-kosten op (afschrijvingen 630, waardeverminderingen 631-634, voorzieningen 635-637). Stap 2: tel niet-kas-opbrengsten af (terugnames waardeverminderingen, vrijgevallen voorzieningen). Stap 3: corrigeer voor werkkapitaal-Δ — daling vorderingen = +cash, stijging voorraden = −cash, stijging handelsschulden = +cash. Stap 4: reclassificeer winst/verlies op verkoop activa naar 'investering'. Resultaat: operationele kasstroom.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Kasstroomoverzicht — Zelena Bio NV (20X4) 🔗

_Zelena Bio NV: nettowinst 285, afschrijvingen 320, Δ vorderingen +400, Δ voorraden +250, Δ handelsschulden +150, capex 800, opname LT-lening 500, dividenduitkering 100 (1.000 EUR)._



<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Winst gelijkstellen aan cash

**Verkeerde assumptie**: Hoge nettowinst betekent dat er voldoende cash is.

**Kernpunt**: Nettowinst is accrual-gebaseerd. Werkkapitaal-stijging, capex en afschrijvings-keuzes maken het verschil. Klassiek alarm: winst stijgt 30 %, operationele kasstroom daalt 50 % — verbergt agressieve omzeterkenning of vorderingen-explosie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Capex vergeten in cash-vrijheid

**Verkeerde assumptie**: Operationele kasstroom = beschikbare cash voor dividenden + schuldafbouw.

**Kernpunt**: Onderhoudscapex (vervanging versleten activa) MOET uit operationele kasstroom komen — anders verwatert het productieve apparaat. Vrije kasstroom (FCF) = operationele kasstroom − onderhoudscapex. Pas FCF is echt 'beschikbaar' voor aandeelhouders/schuldeisers.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Classificatie-keuzes negeren

**Verkeerde assumptie**: Alle bedrijven classificeren interest paid identiek.

**Kernpunt**: IAS 7 par. 31-34 staat keuze toe: interest paid in bedrijfsvoering OF financiering. Inconsequente keuze over jaren of tussen bedrijven maakt vergelijking onmogelijk. Lees de waarderingsregels in de toelichting; corrigeer voor vergelijking.

<small>📚 IAS 7 — paragrafen 31-34 — _norm_</small>

### ⚠️ Een jaar als representatief zien

**Verkeerde assumptie**: Operationele kasstroom dit jaar +200 → bedrijf is gezond.

**Kernpunt**: Werkkapitaal-bewegingen oscilleren sterk: een jaar van voorraad-afbouw kan operationele kasstroom kunstmatig boosten zonder duurzame verbetering. Analyseer 3-5 jaar evolutie en spreid investeringen + werkkapitaal-effecten over meerdere perioden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Free cash flow (DCF-context apart) → [[free-cash-flow]] _(moet-verwijzen)_
- → Activiteits-ratios#werkkapitaalbehoefte → [[activiteits-ratios]] _(moet-verwijzen)_
- ↪ Schuldfinanciering (kasstroom-impact) _(mag-verwijzen)_
- ↪ Kapitaalstructuur (EV-financiering kasstroom-impact) _(mag-verwijzen)_
- ↪ Cyclus-analyse (controleopdracht — operating cycle) _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]]
### `vereist`
- [[jaarrekening]]
### `bevat`
- [[free-cash-flow]] — Free cash flow wordt afgeleid uit het kasstroomoverzicht (operationele kasstroom − onderhoudscapex).
### `beinvloed_door`
- [[activiteits-ratios]] — Werkkapitaal-bewegingen (Δ vorderingen, Δ voorraden, Δ handelsschulden) zijn een grote driver van operationele kasstroom.
### `triggert`
- [[continuiteit]] — Negatieve operationele kasstroom is een ISA 570-indicator voor going-concern-risico.
