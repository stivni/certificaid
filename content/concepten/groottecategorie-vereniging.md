---
title: "Groottecategorie vereniging"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.2.IV.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/groottecategorie-vereniging.json"
---

_Regime_ · ook: groottecriteria vzw · groottecriteria vzw/stichting

## Definitie

De **groottecategorie vereniging** bepaalt of een vzw, ivzw of stichting onder een **micro-, klein- of groot regime** valt. De categorie volgt uit het overschrijden van drempelwaarden op de balansdatum van het laatst afgesloten boekjaar en cascadeert naar (1) het **boekhoudregime** (vereenvoudigd vs. dubbel) en (2) het **jaarrekeningschema** (vereenvoudigd / microschema / verkort / volledig). Drie cascade-trappen voor verenigingen die dubbele boekhouding voeren: **micro-vzw** (microschema mogelijk) · **kleine vzw** (verkort schema) · **grote vzw** (volledig schema). Daarnaast bestaat de categorie **"hele kleine" vzw** (lager dan micro) die met **vereenvoudigde boekhouding** mag werken (CBN-advies 2019/12).

<small>📖 CBN-advies 2019/12 — 2019/12 — Groottecriteria verenigingen en stichtingen — _cbn_ · WVV — art. 1:28, 1:29 — _wettekst_</small>

## Substantie

**Drie drempelparen voor verenigingen die dubbele boekhouding voeren** (perfect geharmoniseerd met de vennootschapscriteria sinds het WVV, art. 1:28-29):

**Kleine vzw** (één criterium mag overschreden zijn):
- Jaargemiddelde personeelsbestand: **50** werknemers
- Jaaromzet (excl. btw): **9.000.000 EUR**
- Balanstotaal: **4.500.000 EUR**

**Micro-vzw** (subset van klein — één criterium mag overschreden zijn):
- Jaargemiddelde personeelsbestand: **10** werknemers
- Jaaromzet (excl. btw): **700.000 EUR**
- Balanstotaal: **350.000 EUR**

**Vereenvoudigde-boekhouding-drempel** (apart, niet dezelfde als bij vennootschappen — CBN-advies 2019/12):
- Jaargemiddelde **5** werknemers
- **334.500 EUR** andere dan niet-recurrente ontvangsten
- **1.337.000 EUR** bezittingen
- **1.337.000 EUR** schulden

*Let op*: deze drempels worden periodiek herzien — controleer de actuele bedragen in het Belgisch Staatsblad of via CBN-advies 2024/07.

<small>📖 CBN-advies 2019/12 — 2019/12 — _cbn_</small>

## Rationale

Het Belgische verenigingsrecht erkent dat vzw's en stichtingen sterk verschillen in **economische omvang** — van een dorpsfanfare tot een ziekenhuiskoepel met honderden personeelsleden. De drempelstructuur **schaalt de administratieve last** aan de economische realiteit: hele kleine vzw's volstaan met een kasboek + jaarlijkse staat van ontvangsten en uitgaven; grote vzw's voeren een volwaardige dubbele boekhouding met volledig schema en commissaris-controle.

<small>🔗 claude-opus-4-7 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2020-01-01** · basis: WVV art. 1:28-29 (Wet 23-03-2019) + CBN-advies 2019/12

WVV-drempels gelden voor boekjaren startend na 31-12-2019. Drempels worden periodiek aangepast aan inflatie.

**✅ Voor**
- 📖 Voor elke **vzw, ivzw of stichting** die op de balansdatum moet bepalen welk boekhoudregime en welk jaarrekeningschema van toepassing is.

## Bouwstenen

### 📏 Drempel vereenvoudigde boekhouding vzw

Een vzw mag **vereenvoudigde boekhouding** voeren als ze op balansdatum **niet meer dan één** van de volgende vier criteria overschrijdt: (1) jaargemiddelde **5 werknemers**; (2) **334.500 EUR** niet-recurrente-ontvangsten (excl. btw); (3) **1.337.000 EUR** bezittingen; (4) **1.337.000 EUR** schulden. Het bestuursorgaan kiest **jaarlijks** of het deze optie licht (CBN 2019/12).

<small>📖 CBN-advies 2019/12 — 2019/12 — Criteria — _cbn_</small>

### 📏 Drempel kleine vzw (WVV art. 1:28)

Een **kleine vzw** is een vzw die op balansdatum van het laatst afgesloten boekjaar **niet meer dan één** van de volgende criteria overschrijdt: (1) **50** werknemers (jaargemiddelde); (2) **9.000.000 EUR** jaaromzet (excl. btw); (3) **4.500.000 EUR** balanstotaal. Een kleine vzw die dubbele boekhouding voert mag een **verkort schema** van jaarrekening opmaken en neerleggen.

<small>📖 WVV — art. 1:28 — _wettekst_ · CBN-advies 2019/12 — Grootte van een vzw die dubbele boekhouding voert — _cbn_</small>

### 📏 Drempel micro-vzw (WVV art. 1:29)

Een **micro-vzw** is een **kleine vzw** die op balansdatum bovendien **niet meer dan één** van de volgende drie verlaagde criteria overschrijdt: (1) **10** werknemers (jaargemiddelde); (2) **700.000 EUR** jaaromzet (excl. btw); (3) **350.000 EUR** balanstotaal. Een micro-vzw die dubbele boekhouding voert mag een **microschema** van jaarrekening opmaken — het meest beknopte schema.

<small>📖 WVV — art. 1:29 — _wettekst_ · CBN-advies 2019/12 — Grootte van een vzw die dubbele boekhouding voert — _cbn_</small>

### 📜 Cascade groottecategorie naar jaarrekeningschema

De cascade voor een vzw die **dubbele boekhouding** voert:
- **Micro-vzw** → microschema (KB 29-04-2019)
- **Kleine vzw, niet micro** → verkort schema
- **Grote vzw** (geen kleine vzw) → volledig schema + verplicht jaarverslag + (boven hogere drempels) commissaris

Voor een **vereenvoudigde-boekhouding-vzw**: vereenvoudigd schema, geen klassiek balans/ROW.

<small>📖 CBN-advies 2019/12 — 2019/12 — _cbn_</small>

## Voorbeelden

> [!example]- Vzw "Buurtwerk" — micro-vzw met dubbele boekhouding
> _Vzw met 7 werknemers, 600.000 EUR omzet (subsidies + dienstenverhuur), 280.000 EUR balanstotaal. De vzw heeft gekozen voor dubbele boekhouding.
>
> **Toetsing klein-criterium** (1:28): werknemers 7 ≤ 50, omzet 600.000 ≤ 9.000.000, balanstotaal 280.000 ≤ 4.500.000 — geen criterium overschreden → klein.
> **Toetsing micro-criterium** (1:29): werknemers 7 ≤ 10, omzet 600.000 ≤ 700.000, balanstotaal 280.000 ≤ 350.000 — geen criterium overschreden → micro.
>
> De vzw mag een **microschema** van jaarrekening opmaken en neerleggen._
>
> <small>🔗 CBN-advies 2019/12 — 2019/12 — _cbn_</small>

## Valkuilen

> [!warning]- Vereenvoudigde-boekhouding-drempel verwarren met klein-vzw-drempel
> **Verkeerde assumptie**: Onder "kleine vzw" mag vereenvoudigde boekhouding gevoerd worden.
>
> **Kernpunt**: Twee **verschillende drempels**: (1) **vereenvoudigde boekhouding vs. dubbele boekhouding** wordt bepaald door de vier criteria van CBN 2019/12 (5 VTE · 334.500 / 1.337.000 / 1.337.000 EUR); (2) **microschema vs. verkort vs. volledig** wordt bepaald door de WVV-criteria 1:28-29. Een kleine vzw moet dus wel dubbele boekhouding voeren als ze de eerste drempel overschrijdt.
>
> <small>📖 CBN-advies 2019/12 — 2019/12 — _cbn_</small>

## Verder lezen (scope-out)

- → Boekhoudplicht (algemeen wie-moet-boekhouden) → [[boekhoudplicht]] _(moet-verwijzen)_
- ↪ Vennootschap-groottecategorie → [[vennootschap-groottecategorieen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhoudplicht]]
### `vergelijkbaar_met`
- [[vennootschap-groottecategorieen]]
    - **Gelijkenissen**:
        - Cascade-mechaniek (drempels overschrijden bepaalt categorie)
        - Drempels micro en klein zijn geharmoniseerd met vennootschapsdrempels sinds WVV
    - **Verschillen**:
        - Verenigingen hebben een extra drempel voor vereenvoudigde boekhouding (CBN 2019/12)
        - Vennootschappen kennen ook 'zeer grote' categorie (extra commissaris-trigger); vzw's cascade stopt bij groot
    - ⚠️ **Verwarringsrisico**: Stagiairs passen vennootschapscascade reflexmatig toe op vzw's en vergeten de aparte vereenvoudigde-boekhouding-toets.
