---
title: "Financiële-analyse-software"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.9.VII
  - 1.9.VII.A
  - 1.9.VII.B
  - 1.9.VII.C
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/financiele-analyse-software.json"
---

# Financiële-analyse-software

_Procedure_

🏛️ Kader · Anchors: `1.9.VII` · `1.9.VII.A` · `1.9.VII.B` · `1.9.VII.C` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: financial analysis tools · JR-analyse-platformen — **Vertalingen**: en: financial analysis software · fr: logiciels d'analyse financière

## Definitie

🔗 Financiële-analyse-software bundelt het ecosysteem van tools dat de accountant gebruikt om jaarrekeningen te analyseren en te benchmarken. Drie hoofd-categorieën in de Belgische praktijk: (1) commerciële platformen — Belfius Companyweb, Trends Top, Graydon, Coface — leveren kant-en-klare ratio-bibliotheek, peer-vergelijking, kredietrating en sector-benchmarks; (2) NBB-bronnen — Balanscentrale (jaarrekeningen) + sector-aggregaten + API voor bulk-toegang; (3) spreadsheet-modelling — Excel of Google Sheets met eigen ratio-template, vrij maatwerk maar tijdsintensief. De keuze hangt af van volume (occasioneel vs portfolio), benodigde diepgang en budget.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Software vervangt het rekenwerk maar niet het denkwerk. Een Companyweb-rapport levert in 30 seconden 40 ratio's + sector-vergelijking — wat de accountant 2 uur Excel zou kosten. Het uitleg-gedeelte ('het bedrijf scoort onder sector-gemiddelde op liquiditeit') is echter algoritme-gegenereerd en mist nuance. De accountant moet de output kunnen lezen, toetsen op consistentie, en zelf de diagnose schrijven — niet de tekst van het rapport copy-pasten. Belangrijk: tools zijn niet uniform — Companyweb en Trends Top kunnen verschillende ratio-definities en sector-indelingen hebben, wat tot uiteenlopende oordelen leidt over hetzelfde bedrijf.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een eigen procedure naast de methodologie? Omdat efficiënt tool-gebruik een eigen vaardigheid is: weten welke tool waarvoor geschikt is, hoe data te importeren (Excel-export, CSV, XBRL via NBB-API), hoe ratio-definities tussen tools te reconciliëren, en vooral: hoe de output kritisch te lezen. Zonder deze tool-discipline verdwaalt de accountant tussen rapporten of vertrouwt hij blind algoritme-conclusies. Bovendien stelt het examenprogramma expliciet vragen over kennis van deze tools (PO 1.9 VII).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Snelle eerste-orde-screening bij nieuwe cliënt of due-diligence — Companyweb-rapport in 5 minuten.
- 🔗 Sector-benchmark bouwen voor diagnose-rapport — NBB-aggregaten + commerciële tools combineren.
- 🔗 Portfolio-monitoring voor commissaris of bank — geautomatiseerde rating + alerts bij verslechtering.

## Bouwstenen

### 💡 Belfius Companyweb  
_`begrip`_

🔗 Belgisch platform met JR-database (~500.000 BE-vennootschappen) + 40 ingebouwde ratio's + 5-jaar-trends + sector-peer-vergelijking + kredietrating + alarmsignalen (RSZ/btw achterstanden). Abonnementen variëren van occasioneel-rapport tot enterprise. Sterk in: peer-vergelijking, kredietrating, alarmen. Beperkt in: maatwerk-analyses, IFRS-cijfers.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Trends Top  
_`begrip`_

🔗 Belgisch platform van Mediafin (Trends/Tendances magazine). Database JR + sector-rangschikkingen + Top-200-lijsten + commerciële intelligence. Sterk in: sector-rangschikkingen, commerciële context (sales lead generation), trend-analyses. Beperkt voor: pure financiële diagnose (Companyweb is daarin sterker).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 NBB-balanscentrale + API  
_`begrip`_

🔗 Publieke NBB-database van alle neergelegde jaarrekeningen (sinds 1992). Gratis raadpleegbaar op nbb.be — één rapport per zoek-opdracht. Bulk-toegang via NBB-API (XBRL-formaat) voor portfolio-monitoring. Naast individuele JR ook sector-aggregaten op NACE-niveau. Onmisbaar als bron-van-waarheid voor sector-benchmark.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Spreadsheet-modelling (Excel / Google Sheets)  
_`mechanisme`_

🔗 Eigen template met formules voor alle ratio-categorieën + automatische peer-vergelijking + DCF / NPV / IRR / Altman-Z. Voordelen: volledig maatwerk, gratis (al hardware-kost), goede leerschool voor stagiair. Nadelen: tijdsintensief in opbouw, geen automatische data-feed (handmatige input of CSV-import nodig). Best practices: gebruik named ranges, scheiding input-blad / berekeningsblad / output-blad, version control, gevoeligheidstabellen voor scenario's.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Output-discipline (geen blind vertrouwen)  
_`vuistregel`_

🔗 Vijf checks bij elk software-rapport: (1) Welke ratio-definitie wordt gebruikt? Companyweb's 'current ratio' kan andere componenten hebben dan Excel's. (2) Welke sector-indeling? NACE-2-cijfer is generiek; sub-sector relevant voor benchmark. (3) Welke benchmark-bron? Mediaan over alle bedrijven of alleen vergelijkbare grootte? (4) Welke periode-vergelijking? Boekjaar of kalenderjaar? (5) Wat is missing/non-applicable in de tool? Sommige sectoren (vastgoed, vzw, holdings) krijgen waarschuwingen die genegeerd worden. Documenteer keuzes in diagnose-rapport.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Algoritme-tekst overnemen als diagnose

**Verkeerde assumptie**: Het Companyweb-rapport bevat al de conclusies.

**Kernpunt**: Tool-output is template-tekst die niet rekening houdt met bedrijfs-specifieke context, sector-uitzonderingen of kwalitatieve signalen. De accountant moet de output lezen, interpreteren en zelf de diagnose schrijven — niet copy-pasten. Tool = data-leverancier, niet oordeel-leverancier.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Verschillende tools mengen zonder reconciliatie

**Verkeerde assumptie**: Companyweb en Trends Top geven dezelfde cijfers voor zelfde bedrijf.

**Kernpunt**: Ratio-definities en sector-indelingen verschillen tussen tools — een ROE in Companyweb (na uitzonderlijk resultaat) kan anders zijn dan in Trends Top (zonder uitzonderlijk). Bij gemengd gebruik: documenteer expliciet de bron + methode per tabel.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Sector-mismatch onopgemerkt laten

**Verkeerde assumptie**: De tool kiest de juiste sector-benchmark automatisch.

**Kernpunt**: NACE-codes zijn historisch en niet altijd up-to-date. Een tech-startup met NACE 'klein zakelijk advies' krijgt verkeerde benchmark. Controleer in de tool of de sector-keuze inhoudelijk klopt en pas indien nodig manueel aan.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Ratio-interpretatie (methodologie) → [[ratio-interpretatie]] _(moet-verwijzen)_
- → Jaarrekeninganalyse Σ (overkoepelend) → [[jaarrekeninganalyse]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]]
### `vereist`
- [[jaarrekening]]
### `beinvloed_door`
- [[ratio-interpretatie]] — Methodologische kennis is nodig om tool-output kritisch te lezen.
