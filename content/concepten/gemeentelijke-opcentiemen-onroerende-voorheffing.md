---
title: "Gemeentelijke opcentiemen op de onroerende voorheffing"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.7.II.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/gemeentelijke-opcentiemen-onroerende-voorheffing.json"
---

# Gemeentelijke opcentiemen op de onroerende voorheffing

_Regime_

📋 Regeling · Anchors: `2.7.II.B` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: opcentiemen OV · gemeentelijke OV-opcentiemen

## Definitie

🔗 Gemeentelijke opcentiemen op de onroerende voorheffing (OV) zijn een vermenigvuldigingsfactor die de gemeente toepast op het basistarief van de onroerende voorheffing, om bijkomende lokale belasting te genereren. Een 'opcentiem' is 1/100 van het basisrecht: een gemeente die 1.500 opcentiemen heft, verhoogt de basis-OV met 1.500/100 = 15-voudig. Het basistarief OV is gewestelijk (Vlaanderen: 3,97 %; Brussel: 1,25 %; Wallonië: 1,25 % gewest); daarbij komen provinciale opcentiemen (vroeger relevant; in Vlaanderen sinds 2018 niet meer omdat provincies geen OV-opcentiemen meer heffen) en gemeentelijke opcentiemen (typisch 700-2.500 in Vlaanderen).

<small>📚 WIB92 — art. 464 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Praktisch effect: opcentiemen vermenigvuldigen de basis-OV met een factor 8-25. Voor een typisch huis met geïndexeerd kadastraal inkomen 2.000 EUR: basis-OV Vlaanderen = 2.000 × 3,97 % = 79,4 EUR. Met 1.500 gemeentelijke opcentiemen: 79,4 × (1 + 1500/100) = 79,4 × 16 = 1.270 EUR. Dat is de werkelijke OV die de eigenaar betaalt — bijna geheel bestemd voor de gemeente. De OV is daarmee een veruit belangrijkere inkomstenbron voor gemeenten dan de aanvullende gemeentebelasting op PB.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio is fiscaal-historisch: de OV is historisch ontworpen als een 'kadastrale belasting' met laag basistarief, met aanwijzing dat het gros van de heffing uit lokale opcentiemen komt. Voor de gemeente: stabiele en relatief inelastische inkomstenbron (onroerend goed is moeilijk te verplaatsen — anders dan natuurlijke personen die kunnen verhuizen wegens lage AGB-PB). Het maakt de OV één van de belangrijkste budgettaire knoppen van een gemeente.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 464 + VCF Titel 2.1 (Vl) + analoge gewestelijke wetgeving Br/W + gemeentelijke belastingreglementen

Vlaamse provincies heffen sinds 1-1-2018 geen provinciale opcentiemen meer op de OV (gecompenseerd door Vlaamse gewestelijke financiering). Brussel/Wallonië: provinciale opcentiemen variabel — actuele stand opzoeken.

**✅ Voor**
- 🔗 Iedere eigenaar (of bezwaarde met zakelijk recht) van onroerend goed in België — opcentiemen worden automatisch toegevoegd aan het basisbedrag van de OV en op één gecombineerd aanslagbiljet geheven.

## Bouwstenen

### 🧮 Volledige OV-formule  
_`formule`_

🔗 OV-totaal = (geïndexeerd KI × gewestelijk basistarief) × [1 + (provinciale opcentiemen + gemeentelijke opcentiemen) / 100]. Vlaanderen: basistarief 3,97 % (verlaagd voor gezinswoning + woning met voldoende energieprestatie). Brussel/Wallonië: 1,25 % gewestelijk. Opcentiemen variëren per gemeente (Vl typisch 700-2.000). Indexering KI: geïndexeerd KI = nominaal KI × indexcoëfficiënt (Cijferzakboekje).

<small>📚 WIB92 — art. 464 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Spreiding gemeentelijke opcentiemen Vlaanderen  
_`begrip`_

🔗 In Vlaanderen variëren gemeentelijke opcentiemen tussen ca. 700 (lage gemeentes — typisch rijke randgemeenten) en 2.500+ (hoge gemeentes — typisch industriële of probleemgemeenten). Gemiddelde rond 1.300-1.500. Voor een gezinswoning met geïndexeerd KI 1.800 EUR betekent een verschil van 800 opcentiemen ≈ 570 EUR/jaar verschil in OV. Significante factor in lokale concurrentie tussen gemeenten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Berekening OV-totaal voor Vlaamse gezinswoning 🔗

_Gezinswoning in Vlaams Gewest, KI 1.500 EUR (nominaal). Indexcoëfficiënt 2024: 2,0915 (illustratief). Gemeentelijke opcentiemen: 1.400. Provincie: 0 (sinds 2018)._

**Berekening:**
- Stap 1 — geïndexeerd KI = 1.500 × 2,0915 = 3.137 EUR.
- Stap 2 — basis-OV Vlaanderen = 3.137 × 3,97 % = 124,5 EUR.
- Stap 3 — opcentiemen-factor = 1 + (0 + 1.400)/100 = 15.
- Stap 4 — OV-totaal = 124,5 × 15 = 1.868 EUR.
- Stap 5 — eventueel verminderd door gezinswoning-korting + kinderen-korting (Vlaams).

→ **Resultaat**: De gemeentelijke opcentiemen vertegenwoordigen ≈ 93 % van het totaal (1.868 − 124,5 = 1.744 EUR). Indexcoëfficiënt + tarieven uit Cijferzakboekje opzoeken voor exacte berekening.

<small>📚 WIB92 — art. 464 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Opcentiemen verwarren met procent-tarief

**Verkeerde assumptie**: 1.500 opcentiemen = 1.500 % opslag = 15-voudig is correct, dus '1.500 opcentiemen op een basis van 100 EUR = 100.000 EUR'.

**Kernpunt**: 1 opcentiem = 1/100 van het basisrecht. 1.500 opcentiemen = 1.500/100 = 15 × het basisrecht (= 15 keer, niet 1.500 keer). De totale heffing = basis × (1 + 1.500/100) = basis × 16. Op een basis van 100 EUR: 1.600 EUR — niet 100.000 EUR.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Cliënt-vastgoedeigenaar

_De accountant die de OV-kost voor cliënten met onroerend goed becijfert._

#### 💰 Fiscaal adviseur

##### 👣 OV-totaal in cliëntbudget  
_`stap`_

🔗 Bij aankoopadvies of jaarlijkse vermogensanalyse: bereken de OV-totaal inclusief opcentiemen voor elk pand. Aandachtspunt: bij cliënten met meerdere onroerende goederen in verschillende gemeenten kan de OV-druk fors verschillen — opcentiemen-vergelijking is een nuttige tabel in het cliëntdossier.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Onroerende voorheffing (basis) → [[onroerende-voorheffing]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[onroerende-voorheffing]]
### `vereist`
- [[kadastraal-inkomen]] — Het geïndexeerd KI is de basis voor de OV-berekening; opcentiemen zijn de vermenigvuldigingsfactor erbovenop.
