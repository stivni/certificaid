---
title: "Vrije kasstroom (Free Cash Flow)"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.9.IV.C
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/free-cash-flow.json"
---

_Ratio_ · afk: **FCF** · ook: free cash flow · vrije kasstroom · beschikbare cash flow

## Definitie

Vrije kasstroom (Free Cash Flow, FCF) is de cash die overblijft na operationele uitgaven en investeringen die nodig zijn om de bedrijfsactiviteiten op huidig niveau te onderhouden. Twee varianten: (1) FCFF (Free Cash Flow to the Firm) — cash beschikbaar voor alle kapitaalverschaffers (aandeelhouders + schuldeisers); (2) FCFE (Free Cash Flow to Equity) — cash beschikbaar enkel voor aandeelhouders, na rente en schuldaflossing. FCFF wordt verdisconteerd met WACC; FCFE met de eigen-kapitaalkost. FCF is daarmee de centrale input voor Discounted Cash Flow (DCF) waardering.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

FCF is de centrale waardering-maatstaf — wat zou een rationele koper bereid zijn te betalen voor de cash-stromen die het bedrijf produceert? Waar nettowinst beïnvloed kan worden door afschrijvings-keuzes, voorzieningen en accrual-discretie, is FCF veel moeilijker te manipuleren: het is écht binnenkomende cash min écht uitgaande cash voor onderhoud. Een groeiende onderneming heeft typisch lage FCF (groei-capex slokt op), wat haar niet minder waardevol maakt — wel meer afhankelijk van toekomstige verbetering. Mature onderneming = hoge FCF = directe cash-output voor aandeelhouders.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Waarom een aparte definitie naast operationele kasstroom? Operationele kasstroom (cash flow from operations, CFO) houdt geen rekening met capex — een productiebedrijf met +500 CFO en 600 onderhoudscapex heeft −100 FCF en glijdt achteruit, terwijl de winst-rekening misschien zelfs positief is. FCF maakt de werkelijke 'overschot na onderhoud' zichtbaar. DCF-waardering bouwt op deze toekomstige FCF-stroom: ondernemingswaarde = Σ FCFFt / (1 + WACC)^t + eindwaarde.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 DCF-bedrijfswaardering — discontering van toekomstige FCFF tegen WACC geeft ondernemingswaarde (Enterprise Value).
- 🔗 Dividend-capaciteit — hoeveel cash kan duurzaam uitgekeerd worden? FCFE is de bovengrens.
- 🔗 Schuldcapaciteit / leverage-analyse — FCFF na onderhoud is de basis waaruit interest + aflossing van potentiële schuld komt.

## Sub-concepten

### 📦 Free Cash Flow to the Firm (FCFF)

#### Definitie

FCFF = bedrijfsresultaat na belastingen (NOPAT) + afschrijvingen − werkkapitaal-toename − onderhoudscapex. Geeft cash beschikbaar voor ALLE kapitaalverschaffers (aandeelhouders + schuldeisers), vóór financierings-keuzes. Wordt verdisconteerd met WACC (gewogen kapitaalkost) om Enterprise Value te krijgen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

FCFF is 'leverage-onafhankelijk' — het kapitaalstructuur-neutraal cash beeld. Daarom geschikt voor vergelijking tussen ondernemingen met verschillende schuldgraad. Bij overname-waardering: koper kijkt naar FCFF want hij kan na overname de kapitaalstructuur wijzigen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule FCFF

FCFF = EBIT × (1 − belastingsvoet) + afschrijvingen + waardeverminderingen − Δ werkkapitaalbehoefte − capex onderhoud. Alternatief vanuit kasstroomoverzicht: FCFF = operationele kasstroom + interestlasten × (1 − belastingsvoet) − onderhoudscapex.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Free Cash Flow to Equity (FCFE)

#### Definitie

FCFE = FCFF − rentebetalingen × (1 − belastingsvoet) − netto schuldaflossing. Geeft cash beschikbaar enkel voor aandeelhouders, ná interest en aflossing. Wordt verdisconteerd met de eigen-kapitaalkost (Ke) om de equity-waarde te krijgen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

FCFE is wat de aandeelhouder mag verwachten als 'maximale duurzame dividenduitkering'. Indien FCFE > dividend → bedrijf bouwt cash-buffer op of geeft aandelen-inkoop. Indien dividend > FCFE → onhoudbaar (financiering door schuld of activa-verkoop).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- FCF-berekening — Zelena Bio NV (20X4)
> _Zelena Bio NV: EBIT 450, belastingsvoet 25 %, afschrijvingen 320, Δ werkkapitaal-behoefte +500, totaal capex 800 waarvan onderhoudscapex 350. Rentelast 50, schuldaflossing 100 (1.000 EUR)._
>
> **Berekening:**
>
> - NOPAT = EBIT × (1 − 0,25) = 450 × 0,75 = 337,5
> - + Afschrijvingen 320
> - − Δ werkkapitaal 500
> - − Onderhoudscapex 350
> - = FCFF = 337,5 + 320 − 500 − 350 = −192,5
> - − Rente na belasting = 50 × 0,75 = 37,5
> - − Schuldaflossing 100
> - = FCFE = −192,5 − 37,5 − 100 = −330
>
> → **Resultaat**: FCFF van −193 KEUR en FCFE van −330 KEUR: het bedrijf verbrandt cash. Diagnose: werkkapitaal-stijging (500) is de grote slokop — combinatie van groei + slechtere DSO/DIO. Onderscheid tussen onderhoudscapex (350) en groei-capex (450 = 800 − 350) is methodisch belangrijk: groei-capex is discretionair. Strikt genomen: FCF op onderhoudsbasis is wat duurzaam beschikbaar is. Aanbeveling: werkkapitaal-discipline en heroverweging groei-capex tot werkkapitaal onder controle.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Onderhoudscapex en groeicapex niet onderscheiden
> **Verkeerde assumptie**: Alle capex is onderhoud — alleen totaal-capex aftrekken voor FCF.
>
> **Kernpunt**: Onderhoudscapex (vervanging) is verplicht — moet uit FCF. Groeicapex (uitbreiding) is discretionair — beleidskeuze, niet verplicht. Voor DCF-waardering: gebruik onderhouds-FCF voor duurzaamheids-test; voor capex-budgettering: gebruik totaal-FCF. Schatting onderhoudscapex ≈ jaarlijkse afschrijvingen (vuistregel).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- FCFF en FCFE verwarren
> **Verkeerde assumptie**: Beide leiden naar dezelfde waarde via DCF.
>
> **Kernpunt**: FCFF verdisconteer je met WACC → resultaat is Enterprise Value (EV). FCFE verdisconteer je met Ke (eigen-kapitaalkost) → resultaat is equity-waarde direct. Equity-waarde = EV − netto schuld. Beide moeten consistent zijn; inconsistente match (FCFF + Ke, of FCFE + WACC) geeft systematisch verkeerde waarde.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Operationele kasstroom als FCF gebruiken
> **Verkeerde assumptie**: Cash flow from operations (CFO) uit het kasstroomoverzicht IS de FCF.
>
> **Kernpunt**: CFO is operationele cash VOOR capex. FCF = CFO − onderhoudscapex (eventueel ook FCFF aanpassing voor rente). Een bedrijf met CFO +500 en onderhoudscapex 600 heeft FCF −100, niet +500. Verwarring leidt tot systematische over-waardering bij DCF.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kasstroomanalyse Σ (algemeen kasstroom-overzicht) → [[kasstroom-analyse]] _(moet-verwijzen)_
- → Bedrijfswaardering (DCF-toepassing) → [[bedrijfswaardering]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[kasstroom-analyse]]
### `vereist`
- [[kasstroom-analyse]]
### `triggert`
- [[bedrijfswaardering]] — FCFF is de hoofd-input voor DCF-waarderings-techniek.
