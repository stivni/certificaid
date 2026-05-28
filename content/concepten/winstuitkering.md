---
title: "Winstuitkering"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 3.0.IV.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/winstuitkering.json"
---

# Winstuitkering

_Regime_

🏛️ Kader · 📋 Regeling · Anchors: `3.0.IV.B` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: dividenduitkering · winstverdeling aan aandeelhouders · uitkering aan vennoten

## Definitie

📖 Winstuitkering is de overkoepelende verrichting waarbij een vennootschap waarde aan haar aandeelhouders teruggeeft. Het WVV definieert 'uitkering' breed: regulier dividend, interim dividend, tantieme, inkoop eigen aandelen, kapitaalvermindering met terugbetaling, liquidatieboni — alles wat netto-actief uit de vennootschap doet vloeien naar aandeelhouders kwalificeert. Voor BV's geldt sinds het WVV (2019) een dubbele uitkeringstest: netto-actief-test (sluit het kapitaal en niet-uitkeerbare reserves af) PLUS liquiditeitstest (vennootschap moet in staat blijven om opeisbare schulden te voldoen). Voor NV's geldt enkel de netto-actief-test (art. 7:212 WVV). Fiscaal wordt het meeste uitgekeerde belast als dividend (art. 18 WIB92) met roerende voorheffing 30% (of verlaagd: VVPRbis 15%, liquidatiereserve 10%).

<small>📚 WVV — art. 5:141 + 5:142 (BV) — _wettekst_ · WVV — art. 7:212 + 7:213 (NV) — _wettekst_ · WIB92 — art. 18 + 269 — _wettekst_ · CBN-advies 2021/02 — winstverdeling NV — _advies_</small>

## Substantie

🔗 Een vennootschap die winst maakt staat voor een keuze: winst houden (overdragen naar volgend boekjaar of reserveren) of uitkeren aan aandeelhouders. Bij uitkering kiest men de vorm: regulier dividend (eenvoud, RV 30%), interim dividend (tussentijdse uitkering, vereist tussentijdse balans), tantieme (alleen aan bestuurder, telt mee voor KMO-bezoldigingsregel), inkoop eigen aandelen (alleen via specifieke procedure WVV), of liquidatiereserve (10% direct + 5% wachtperiode-RV bij latere uitkering). Elke vorm heeft een eigen fiscale druk, eigen procedure en eigen administratieve last. De keuze is geen detail — het verschil tussen RV 30% (regulier) en 10% (liquidatiereserve na 5 jaar) op 100.000 EUR uitkering is 20.000 EUR.

<small>📚 WIB92 — art. 269 + 184quater — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom is uitkering zo strikt gereguleerd? Omwille van schuldeisersbescherming. Een vennootschap heeft beperkte aansprakelijkheid — schuldeisers kunnen zich alleen verhalen op het vermogen van de vennootschap, niet op het privevermogen van aandeelhouders. Als aandeelhouders vrijuit kunnen uitkeren zou de vennootschap leegt geplunderd worden voordat schuldeisers betaald zijn. Vandaar de netto-actief-test (vermogen mag niet onder kapitaal + onbeschikbare reserves zakken) en, sinds het WVV voor BV's, ook de liquiditeitstest (vennootschap moet in staat blijven schulden te betalen). Schending leidt tot bestuurdersaansprakelijkheid en terugvordering van aandeelhouders.

<small>📚 CBN-advies 2021/14 — alarmbelprocedure + netto-actief — _advies_ · WVV — art. 5:142 (BV liquiditeitstest) — _wettekst_</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV art. 5:141/142 (BV) + art. 7:212/213 (NV); WIB92 art. 18 + 269 + 184quater

**📋 Voorwaarden**
- 📖 Voor NV: netto-actief-test — netto-actief na uitkering blijft minstens gelijk aan gestort kapitaal (of opgevraagd kapitaal indien hoger) plus niet-uitkeerbare reserves (wettelijke reserve, statutair onbeschikbare reserve, herwaarderingsmeerwaarde, kapitaalsubsidies, ...).
- 📖 Voor BV: dubbele test — netto-actief-test (analoog NV maar zonder 'kapitaal'-concept: vergelijken met onbeschikbare inbreng) PLUS liquiditeitstest (vennootschap blijft in staat opeisbare schulden ten minste 12 maanden te voldoen).
- 📖 AV-besluit op basis van goedgekeurde jaarrekening (regulier dividend) of tussentijdse balans (interim dividend bij NV, niet toegelaten bij BV behalve via bestuursorgaan binnen statutaire grenzen).
- 📖 Inhouding bedrijfsvoorheffing/roerende voorheffing bij uitbetaling: standaard 30% (art. 269 WIB92), verlaagd 15% (VVPRbis voor kleine vennootschappen 3+ jaar oud), 5% bij verdere wachtperiode op liquidatiereserve, of vrijstelling onder DBI-voorwaarden voor moeder-vennootschap-aandeelhouders.

**⚠️ Risico**
- 🔗 Schending van de netto-actief-test of liquiditeitstest: bestuurders zijn hoofdelijk aansprakelijk voor schade aan vennootschap en derden; aandeelhouders moeten onrechtmatige uitkering terugbetalen.
- 🤖 Niet-tijdige inhouding RV: aansprakelijkheid voor onbetaalde belasting + boetes.

## Sub-concepten

### 📦 Regulier (jaarlijks) dividend  
_`verrichting` (subconcept)_

#### Definitie

📖 Het klassieke jaardividend uitgekeerd door de AV bij goedkeuring van de jaarrekening, als onderdeel van het winstbestemmings-besluit. Standaard RV 30% (art. 269 WIB92). Toepasselijk op alle vennootschappen.

<small>📚 WIB92 — art. 18 + 269 — _wettekst_</small>

### 📦 Interim (tussentijds) dividend  
_`verrichting` (subconcept)_

#### Definitie

📖 Tussentijdse uitkering tijdens het boekjaar, op basis van het tussentijdse resultaat plus overgedragen winst minus overgedragen verlies. Bij NV: enkel toegelaten als statutair voorzien en op basis van tussentijdse balans (art. 7:213 WVV). Bij BV: niet voorzien in WVV — bestuursorgaan kan op basis van statuten binnen voorwaarden uitkeren, mits netto-actief- en liquiditeitstest. Zelfde RV-tarief als regulier dividend.

<small>📚 WVV — art. 7:213 — _wettekst_</small>

### 📦 VVPRbis — verlaagd dividend voor kleine vennootschap  
_`regime` (subconcept)_

#### Definitie

📖 Verlaagd RV-tarief (15%) voor dividenden uit kleine vennootschappen onder de voorwaarden van art. 269 par. 2 WIB92: kapitaalinbreng vanaf 1 juli 2013 in nieuwe vennootschap of bestaande BV/NV; aandelen op naam zonder preferente rechten; verlaagd tarief van 20% in jaar Y2 (tweede uitkering), 15% vanaf jaar Y3. Vereist dat bestaande aandelen ten minste even goed gehouden zijn en dat de vennootschap als 'klein' (criteria art. 1:24 WVV) kwalificeert.

<small>📚 WIB92 — art. 269 par. 2 (VVPRbis) — _wettekst_</small>

### 📦 Liquidatiereserve  
_`regime` (subconcept)_

#### Definitie

📖 Een kleine vennootschap kan elk jaar (een deel van) haar boekhoudkundige nettowinst aanleggen als 'liquidatiereserve' (art. 184quater WIB92). Bij aanleg: 10% afzonderlijke aanslag in VenB (afzonderlijk van de gewone VenB). Bij latere uitkering: 5% RV indien minimum 5 jaar gewacht; 20% RV indien sneller; 0% bij liquidatie. Cumulatieve fiscale druk bij goede timing: 10% + 5% = 15% — substantieel onder de 30% RV op regulier dividend.

<small>📚 WIB92 — art. 184quater + 21, 11° — _wettekst_</small>

### 📦 Inkoop eigen aandelen als uitkeringsvorm  
_`verrichting` (subconcept)_

#### Definitie

📖 De vennootschap koopt haar eigen aandelen terug van de aandeelhouders. Het positief verschil tussen verkrijgingsprijs en aandeel in gerevaloriseerd gestort kapitaal wordt fiscaal behandeld als dividend (art. 186 WIB92, aangifte code 1302). Strikte procedure WVV (besluit AV met gekwalificeerde meerderheid, maximum 20% kapitaal, financiering uit uitkeerbare winsten).

<small>📚 WIB92 — art. 186 — _wettekst_ · aangifte-VenB-2025-uitgekeerde-dividenden — code 1302 — _aangifte_</small>

### 📦 Vergelijking uitkeringsvormen  
_`kader` (subconcept)_

#### Substantie

📖 Overzicht fiscale druk per uitkeringsvorm (kleine vennootschap, aandeelhouder natuurlijke persoon).

<small>📚 WIB92 — art. 269 + 184quater — _wettekst_</small>

**Weergave** `vergelijkingstabel`:

```json
{
  "titel": "RV-druk per uitkeringsvorm",
  "kolommen": [
    "Uitkeringsvorm",
    "RV-tarief",
    "Voorwaarden",
    "Procedure"
  ],
  "rijen": [
    [
      "Regulier dividend",
      "30%",
      "Geen specifieke (alleen netto-actief-test)",
      "AV-besluit bij jaarrekening"
    ],
    [
      "VVPRbis (jaar 3+)",
      "15%",
      "Kleine venn, aandelen-op-naam, kapitaalinbreng vanaf 1-7-2013",
      "AV-besluit + RV-aangifte VVPRbis"
    ],
    [
      "VVPRbis (jaar 2)",
      "20%",
      "Idem, in jaar 2 na inbreng",
      "Idem"
    ],
    [
      "Liquidatiereserve (5 jaar)",
      "5% bij uitkering + 10% bij aanleg = 15%",
      "Kleine venn; aanleg uit boekhoudkundige nettowinst; uitkering na 5 jaar",
      "Jaarlijkse aanleg-aangifte + RV-aangifte bij uitkering"
    ],
    [
      "Liquidatiereserve (binnen 5 jaar)",
      "20% + 10% bij aanleg = 30%",
      "Versnelde uitkering",
      "Idem"
    ],
    [
      "Liquidatiereserve bij liquidatie",
      "0% + 10% bij aanleg = 10%",
      "Bij effectieve liquidatie",
      "Bij liquidatie"
    ],
    [
      "Tantieme aan bestuurder",
      "PB progressief + sociale bijdragen",
      "Bestuurder, in redelijk verband",
      "AV-besluit bij winstbestemming"
    ],
    [
      "Kapitaalvermindering (terugbetaling)",
      "0% (pro rata uit gestort kapitaal) + 30% (pro rata uit belaste reserves)",
      "Pro-rata-regel art. 18 WIB92",
      "AV-besluit + 2-maanden-wachtperiode (schuldeisers)"
    ]
  ]
}
```

## Bouwstenen

### 📜 Netto-actief-test  
_`regel`_

📖 Het netto-actief van de vennootschap (totaal activa minus voorzieningen, schulden en niet-afgeschreven oprichtingskosten / O&O) mag na uitkering niet zakken onder het bedrag van het gestorte kapitaal (of opgevraagd kapitaal indien hoger), vermeerderd met alle reserves die volgens wet of statuten niet mogen worden uitgekeerd. Voor BV: vergelijkbaar concept maar met 'onbeschikbare inbreng' in plaats van 'gestort kapitaal'. Toets gebeurt op basis van de laatste goedgekeurde jaarrekening, mits geen materieel waardeverlies sindsdien.

<small>📚 CBN-advies 2021/02 — netto-actief-test NV — _advies_ · CBN-advies 2021/14 — netto-actief-begrip WVV — _advies_ · WVV — art. 7:212 — _wettekst_</small>

### 📜 Liquiditeitstest (BV)  
_`regel`_

📖 Specifiek voor de BV (art. 5:142 WVV): het bestuursorgaan toetst of de BV, na uitkering, gedurende ten minste 12 maanden in staat zal blijven om haar opeisbare schulden te voldoen. De toets is een vooruitkijkende analyse — op basis van een prognose, niet alleen van de balans. Het bestuursverslag dat de toets documenteert is verplicht; het ontbreken ervan maakt bestuurders aansprakelijk.

<small>📚 WVV — art. 5:142 — _wettekst_ · CBN-advies 2021/14 — liquiditeitstest — _advies_</small>

### 🧮 Uitkeerbare winsten — concept en berekening  
_`formule`_

📖 Uitkeerbare winsten = (winst van het boekjaar + overgedragen winst van vorige boekjaren - overgedragen verlies - dotaties aan wettelijke reserve en niet-uitkeerbare reserves). Deze winst kan worden bestemd voor dividend, tantieme, kapitaalverhoging via uitkering of overdracht naar volgend boekjaar.

<small>📚 CBN-advies 2021/02 — uitkeerbare winsten — _advies_</small>

## Valkuilen

### ⚠️ Liquiditeitstest vergeten bij BV

**Verkeerde assumptie**: De netto-actief-test volstaat voor BV (zoals voor NV).

**Kernpunt**: Voor BV gelden sinds het WVV TWEE tests: netto-actief-test EN liquiditeitstest. Het ontbreken van het bestuursverslag over de liquiditeitstest maakt de uitkering onrechtmatig — terugbetaling van aandeelhouders en bestuurdersaansprakelijkheid kunnen volgen.

<small>📚 WVV — art. 5:142 — _wettekst_</small>

### ⚠️ Liquidatiereserve verwarren met liquidatie-bonus

**Verkeerde assumptie**: Liquidatiereserve is hetzelfde als wat bij ontbinding van de vennootschap wordt uitgekeerd.

**Kernpunt**: Liquidatiereserve is een fiscaal mechanisme van proactieve reservering tijdens de levensduur van de vennootschap (art. 184quater WIB92), waarbij 10% afzonderlijke aanslag wordt betaald bij aanleg. Liquidatie-bonus is het overschot bij ontbinding na vereffening. Twee verschillende concepten — maar liquidatiereserve geeft het privilege dat bij effectieve liquidatie de RV op de reserve 0% is.

<small>📚 WIB92 — art. 184quater + 209 — _wettekst_</small>

### ⚠️ Reguliere dividend mengen met VVPRbis-kapitaal

**Verkeerde assumptie**: Vennootschap kan zelf kiezen of een dividend onder VVPRbis valt.

**Kernpunt**: VVPRbis is geen keuze maar een gevolg van de kapitaalstructuur: alleen aandelen uit nieuwe inbrengen vanaf 1 juli 2013 (op naam, zonder preferente rechten) komen in aanmerking. Bestaande kapitaal blijft onder 30% RV. Vennootschappen met gemengde kapitaalstructuur moeten per dividend afzonderlijk berekenen welk deel onder 30% versus 15% valt.

<small>📚 WIB92 — art. 269 par. 2 — _wettekst_</small>

### ⚠️ Tantieme als variant van dividend behandelen

**Verkeerde assumptie**: Tantieme is gewoon een dividend voor de bestuurder.

**Kernpunt**: Tantieme is bedrijfsleidersbezoldiging (art. 32 WIB92), niet roerend inkomen. Het is aftrekbaar bij de vennootschap, telt mee voor de KMO-bezoldigingsregel, en wordt belast tegen progressieve PB-tarieven plus sociale bijdragen — fundamenteel anders dan een dividend.

<small>📚 WIB92 — art. 32 — _wettekst_</small>

## Speelruimtes

### 🎚️ Keuze van uitkeringsvorm bij kleine vennootschap

## Accountant-perspectieven

### Accountant als adviseur bij winstuitkering

#### 🧭 Adviseur

##### 👣 Uitkeringsstrategie ontwerpen  
_`stap`_

**Substantie**: 🔗 Stap 1: bepaal cash-behoefte aandeelhouders versus cash-positie en investerings-behoefte vennootschap. Stap 2: identificeer toepasselijke regimes (VVPRbis-kapitaal? Klein? Liquidatiereserve-historiek?). Stap 3: bereken fiscale druk per uitkeringsvorm. Stap 4: maak een meerjarenplan: jaarlijkse aanleg liquidatiereserve + uitkeringscyclus. Stap 5: documenteer netto-actief-test (NV en BV) + liquiditeitstest (BV) — bewaar bestuursverslag.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boekingen bij winstuitkering  
_`stap`_

**Substantie**: 🔗 Bij AV-besluit: rekening 692 'Toevoeging aan reserves' of 694 'Uit te keren tantieme/dividend' tegen 477 'RV te betalen' (30% inhouding) + 471 'Schuld aan aandeelhouders'. Bij betaling: 477 + 471 tegen bank. RV-aangifte binnen 15 dagen na inhouding (Article 95 WIB-uitvoering). Bij VVPRbis: aparte aangifte voor 15% deel.

<small>📚 CBN-advies 2021/02 — boekingen uitkering — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Winstbestemming — wettelijke reserves + dividend-toewijzing → [[winstbestemming]] _(moet-verwijzen)_
- → Tantieme als afzonderlijk record → [[tantieme]] _(moet-verwijzen)_
- → Kapitaalbescherming — netto-actief-test en uitkeringstest → [[kapitaalbescherming]] _(moet-verwijzen)_
- → Inkoop eigen aandelen — alternatief uitkeringsvorm → [[inkoop-eigen-aandelen]] _(moet-verwijzen)_
- → Kapitaalvermindering — pro-rata-toerekening winstverdeling-aspect → [[kapitaalvermindering]] _(moet-verwijzen)_
- ↪ Liquidatiereserve VenB-mechanisme (10% afzonderlijke heffing) → [[liquidatiereserve]] _(mag-verwijzen)_
- ↪ VVPRbis — verlaagd RV-tarief kleine venn met nieuw kapitaal → [[vvprbis]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsrecht]]
### `vereist`
- [[kapitaalbescherming]]
- [[winstbestemming]]
### `vergelijkbaar_met`
- [[inkoop-eigen-aandelen]] — Inkoop eigen aandelen is een specifieke vorm van winstuitkering met eigen procedure en fiscale behandeling als dividend (art. 186 WIB92).
    - **Gelijkenissen**:
        - Beide laten waarde uit vennootschap naar aandeelhouders vloeien
        - Beide vallen onder kapitaalbescherming
    - **Verschillen**:
        - Regulier dividend gaat naar alle aandeelhouders pro rata; inkoop selectief
        - Inkoop reduceert aantal uitstaande aandelen
### `beinvloed_door`
- [[algemene-vergadering]]
