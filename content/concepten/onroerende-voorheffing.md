---
title: "Onroerende voorheffing"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.7.I.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/onroerende-voorheffing.json"
---

# Onroerende voorheffing

_Regime_

📋 Regeling · Anchors: `2.7.I.B` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: OV — **Vertalingen**: fr: précompte immobilier

## Definitie

📖 De onroerende voorheffing (OV) is een jaarlijkse gewestelijke belasting op onroerend goed, gebaseerd op het kadastraal inkomen (KI) van het goed. Sinds de zesde staatshervorming is de OV een volledige gewestelijke materie: Vlaanderen, Brussel en Wallonië bepalen zelf het basistarief, de vrijstellingen en de verminderingen. Het basistarief is in Vlaanderen 3,97 %, in Brussel en Wallonië 1,25 %. Daarbij komen provinciale (verdwenen in Vl sinds 2018) en gemeentelijke opcentiemen die het effectief tarief vermenigvuldigen.

<small>📚 WIB92 — art. 251 — _wettekst_ · WIB92 — art. 255 — _wettekst_</small>

## Substantie

🔗 De OV is in de praktijk een 'samengestelde' jaarlijkse vastgoedbelasting: bij een Vlaamse gezinswoning met geïndexeerd KI 2.000 EUR + 1.500 gemeentelijke opcentiemen: 2.000 × 3,97 % × 16 = 1.270 EUR. Voor de eigenaar is dat één van de belangrijkste vaste lasten op vastgoed (na hypotheekrente). De OV is verschuldigd door de eigenaar of de houder van een zakelijk recht (vruchtgebruiker, erfpachter, opstalhouder) op 1 januari van het aanslagjaar. Bij doorverhuur kan de OV contractueel aan de huurder worden doorgerekend voor commerciële huur (niet voor woninghuur — gewestelijk verbod in Vl/W).

<small>📚 WIB92 — art. 251 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Klassiek: belasting op vermogenshouder van onroerend goed (Vermögensteuer) — onroerend goed levert (theoretisch) een gebruikswaarde of huurwaarde op, en de OV is de fiscale prijs daarvan. Het KI is een geforfaitiseerde geschatte nettohuurwaarde uit de jaren '70 (laatste perekwatie 1979–1980), wat tot scheve verhoudingen leidt tussen oude en nieuwe woningen. Sinds 2014 volledig gewestelijke bevoegdheid — gewesten gebruiken het tarief en de verminderingen als beleidsinstrument (huisvestingsbeleid, gezinsbeleid, energiebeleid).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 251-260 (federaal kader) + VCF Titel 2.1 (Vl) + decreten/ordonnanties Wallonië en Brussel

OV is gewestelijk sinds 2014 (zesde staatshervorming). Vlaanderen heeft het regime aanzienlijk hervormd en sterk geïntegreerd in de VCF. Brussel en Wallonië volgen nog grotendeels de oorspronkelijke WIB92-structuur.

**✅ Voor**
- 📖 Eigenaar, vruchtgebruiker, erfpachter, opstalhouder of bezitter (zelfs zonder titel) van een in België gelegen onroerend goed (gebouwd of ongebouwd) op 1 januari van het aanslagjaar. Voor een gewoon huis: de eigenaar betaalt. Bij vruchtgebruik: de vruchtgebruiker (geniet de gebruiksvruchten). Bij appartement: de mede-eigenaar pro rata zijn aandeel.

**⛔ Uitsluitingen**
- 🔗 Vrijstellingen: openbaar domein, religieuze gebouwen voor erediensten, scholen, ziekenhuizen onder voorwaarden, monumenten (Vl: vermindering), onroerend goed voor industriële productie (deeltijds, voor 'outillage'). Verminderingen voor gezinswoning + kinderen ten laste + handicap + energetische renovatie (Vl).

**👍 Voordeel**
- 🔗 Vermindering gezinswoning + kinderen ten laste (Vl): vanaf 2 kinderen ten laste een vermindering — orde van grootte 8-20 % van de OV. Vermindering voor handicap. Korting voor energetisch presterende nieuwbouw (E-peil-grens). Exacte bedragen + voorwaarden in Cijferzakboekje of VCF.

## Bouwstenen

### 💡 Kadastraal inkomen als basis  
_`begrip`_

📖 Het kadastraal inkomen (KI) is een geforfaitiseerde schatting van de jaarlijkse netto-huurwaarde van het onroerend goed, vastgelegd door de Administratie van het Kadaster bij ingebruikname of bij wijziging. Het wordt jaarlijks geïndexeerd. Geïndexeerd KI = nominaal KI × indexcoëfficiënt. De laatste algemene perekwatie dateert van 1980 — het KI is dus structureel verouderd en gemiddeld lager dan de werkelijke huurwaarde. Een nieuwe perekwatie wordt in alle gewesten besproken maar nog niet uitgevoerd.

<small>📚 WIB92 — art. 471 e.v. — _wettekst_</small>

### 📏 Basistarief Vlaanderen 3,97 %  
_`drempel`_

📖 Het Vlaamse basistarief is 3,97 % van het geïndexeerde KI (verhoogd in vergelijking met de 'federale 1,25 % traditie' bij overdracht in 2014). Brussel en Wallonië hebben 1,25 % behouden. Het Vlaamse hogere basistarief wordt gecompenseerd door specifieke verminderingen (gezinswoning, kinderen) zodat de effectieve OV op een gezinswoning niet noodzakelijk hoger is dan in BHG/W.

<small>📚 WIB92 — art. 255 — _wettekst_</small>

### 📜 Belastingplichtige op 1 januari  
_`regel`_

📖 De OV is verschuldigd door wie op 1 januari van het aanslagjaar eigenaar of zakelijk rechthebbende is. Bij verkoop in de loop van het jaar: in beginsel betaalt de verkoper (was eigenaar op 1 januari), maar in de praktijk wordt via notariële akte een pro rata-verrekening overeengekomen tussen verkoper en koper. Bij vruchtgebruik: de vruchtgebruiker (niet de blote eigenaar).

<small>📚 WIB92 — art. 251 — _wettekst_</small>

## Voorbeelden

### 💡 OV Vlaanderen — gezinswoning met 3 kinderen 🔗

_Gezinswoning Vlaanderen, geïndexeerd KI 2.000 EUR. Gemeentelijke opcentiemen 1.500. Gezin met 3 kinderen ten laste — vermindering kinderen ten laste._

**Berekening:**
- Stap 1 — basis-OV Vl = 2.000 × 3,97 % = 79,4 EUR.
- Stap 2 — opcentiemen-factor = 1 + 1.500/100 = 16.
- Stap 3 — bruto OV-totaal = 79,4 × 16 = 1.270 EUR.
- Stap 4 — vermindering kinderen ten laste (Vl, illustratief, bv. 7,75 EUR per kind × 16 = 124 EUR voor 3 kinderen — exact bedrag in Cijferzakboekje): aftrek ≈ 372 EUR.
- Stap 5 — netto OV ≈ 898 EUR.

→ **Resultaat**: Aanzienlijk verminderd door gezinsvermindering. Exact bedrag per kind opzoeken in Cijferzakboekje / VCF.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Verwarring met de vroegere PB-rubriek 'onroerend inkomen'

**Verkeerde assumptie**: De OV is dezelfde belasting als de onroerende inkomstenbelasting binnen de personenbelasting.

**Kernpunt**: De OV is een jaarlijkse gewestelijke vastgoedbelasting, los van de PB. Daarnaast belast de PB het 'onroerend inkomen' van de eigenaar (KI van eigen woning is vrijgesteld; verhuurde panden: KI of werkelijke huurwaarde). Voor verhuurde panden geldt: KI vermeld in de aangifte + de OV is verrekenbaar in beperkte mate (bedrijfsmatige verhuur).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Cliënt-vastgoedeigenaar / verhuurder

_De accountant die fiscale planning rond vastgoed begeleidt._

#### 💰 Fiscaal adviseur

##### 👣 Verminderingen claimen  
_`stap`_

🔗 Controleer jaarlijks bij het aanslagbiljet OV of alle verminderingen correct zijn toegepast: gezinswoning + kinderen ten laste + handicap + energetische renovatie. Bij ontbrekende vermindering: bezwaarschrift bij FOD/gewestelijke administratie (binnen 3 maanden in Vl bij Vlaamse Belastingdienst). Voor verhuurd vastgoed: nakijken of huurder/eigenaar correct de OV draagt volgens huurovereenkomst.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Gemeentelijke opcentiemen detail → [[gemeentelijke-opcentiemen-onroerende-voorheffing]] _(moet-verwijzen)_
- ↪ PB-cross (verrekening) → [[personenbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[lokale-en-regionale-belastingen]]
### `vereist`
- [[kadastraal-inkomen]]
### `bevat`
- [[gemeentelijke-opcentiemen-onroerende-voorheffing]] — Gemeentelijke opcentiemen zijn een onlosmakelijk onderdeel van de uiteindelijke OV-aanslag.
