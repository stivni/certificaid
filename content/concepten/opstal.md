---
title: "Opstalrecht"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.1.II.X
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/opstal.json"
---

# Opstalrecht

_Instrument_

📋 Regeling · Anchors: `1.1.II.X` · Wave: `cluster-extract-balansposten-activa-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: opstal · recht van opstal — **Vertalingen**: en: right of superficies · fr: droit de superficie

## Definitie

📖 Opstalrecht (Boek 3 BW, hervorming 2021 — daarvoor Wet 10/01/1824) is een zakelijk recht om gebouwen, werken of beplantingen te hebben (of op te richten, te bezitten, te wijzigen) op, boven of onder een onroerend goed van een andere persoon. Karakteristieken: (1) zakelijk recht ingeschreven in kadaster; (2) looptijd tot 99 jaar (kan ook korter, geen wettelijk minimum); (3) tegenprestatie meestal eenmalige prijs + soms periodieke vergoeding; (4) opstalhouder heeft eigendomsrecht op de werken die hij oprichten op de grond — gescheiden van de grondeigenaar (uitzondering op natrekkingsprincipe art. 3.50 BW). Bij einde: werken worden eigendom grondeigenaar (natrekking) — eventueel mits vergoeding.

<small>📚 BW Boek 3 — art. 3.177 e.v. (opstal) — _wettekst_ · CBN-advies 2015/5 — Opstalrecht — _cbn_</small>

## Substantie

📖 Opstal wordt vooral gebruikt voor 'bouwen op andermans grond': (a) windturbines op landbouwgrond — exploitant heeft opstalrecht voor 25-50 jaar op grond van landbouwer; (b) opslagloodsen op haventerrein — havenautoriteit blijft eigenaar grond; (c) joint-venture-vastgoed waarbij grondeigenaar inbrengt via opstal i.p.v. eigendom. Belangrijk onderscheid met erfpacht: bij erfpacht heb je het VOL genot van een BESTAAND goed; bij opstal heb je het RECHT om TE BOUWEN op andermans grond (en de eigendom van wat je bouwt). Boekhoudkundig (CBN 2015/5): bij opstalhouder activering van bouwwerk op klasse 22-23 (afschrijving over kortste van technische levensduur OF opstaltermijn).

<small>📚 CBN-advies 2015/5 — Opstalrecht en onzelfstandig opstalrecht — _cbn_</small>

## Rationale

🔗 Het bestaan van opstal als afzonderlijk zakelijk recht doorbreekt het Romeinse natrekkings-principe ('superficies solo cedit': wat op grond staat is van grondeigenaar). De wetgever liet dit toe omdat moderne vastgoed-projecten eigendom-splitsing eisen: grondeigenaar wil grond behouden, exploitant wil zekerheid op bouwwerk. Opstal lost dit op. De maximumduur 99 jaar verzoent de drie belangen (natrekking grondeigenaar, eigendomszekerheid opstalhouder, voorkomen 'eeuwig' recht).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2021-09-01** · basis: Boek 3 BW

Boek 3 BW (Wet 04.02.2020) heeft opstal uit Wet 10.01.1824 hervormd. Geen wettelijk minimum-termijn meer (vroeger 0-50 j); max 99 jaar.

**✅ Voor**
- 🔗 Windturbines + zonnepanelen op landbouwgrond.
- 🔗 Joint-venture-vastgoed met grondeigenaar-inbreng via opstal.

## Sub-concepten

### 📦 Zelfstandig vs onzelfstandig opstalrecht  
_`regime` (subconcept)_

#### Definitie

📖 ZELFSTANDIG opstalrecht: apart zakelijk recht, ingeschreven in kadaster, opposable aan derden. Max 99 j. ONZELFSTANDIG opstal (CBN 2015/5): vervat in een ander recht (vruchtgebruik, erfpacht). Zelden apart geactiveerd — onderdeel van het hoofdrecht.

<small>📚 CBN-advies 2015/5 — Opstalrecht en onzelfstandig opstalrecht — _cbn_</small>

### 📦 Boekhoudkundige cascade bij opstalhouder  
_`procedure` (subconcept)_

#### Definitie

📖 Bij vestiging opstal + bouw: eenmalige prijs + notaris + registratierechten + bouwkosten activeren op klasse 22 (gebouwen) of 23 (installaties). Afschrijving over kortste van technische levensduur OF opstaltermijn. Bij einde: indien volledig afgeschreven → boekwaarde 0; bij vergoeding voor natrekking → opbrengst 763 (meerwaarde realisatie).

<small>📚 CBN-advies 2015/5 — Boekingen opstal — _cbn_</small>

## Valkuilen

### ⚠️ Opstal = recht op grond

**Verkeerde assumptie**: Bij opstalrecht word je eigenaar van de grond.

**Kernpunt**: Opstal geeft eigendom van het BOUWWERK (gebouw, installatie) — NIET van de grond. Grondeigenaar blijft eigenaar grond. Belangrijk verschil met erfpacht (vol genot bestaand goed) en gewone aankoop (volle eigendom grond + werk).

<small>📚 BW Boek 3 — art. 3.50 e.v. natrekking + 3.177 opstal — _wettekst_</small>

## Accountant-perspectieven

### Opstalhouder

#### 📒 Boekhouder

##### 👣 Activering bouwwerk + afschrijving  
_`stap`_

📖 Per opstal-contract: documenteer opstaltermijn (X jaar) + technische levensduur bouwwerk (Y jaar). Afschrijven op klasse 22 over min(X, Y). Bij verlenging opstal: herziening afschrijvingsplan.

<small>📚 CBN-advies 2015/5 — Afschrijving — _cbn_</small>

## Verder lezen (scope-out)

- → Opsplitsing-eigendom — overkoepelende vergelijking → [[opsplitsing-eigendom]] _(moet-verwijzen)_
- ↪ Vaste-activa-context (boekhouding) → [[vaste-activa]] _(mag-verwijzen)_
- ↪ Registratierechten (fiscaal) → [[registratie-en-successierechten]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[opsplitsing-eigendom]]
### `vergelijkbaar_met`
- [[erfpacht]]
    - **Gelijkenissen**:
        - Beide tot 99 jaar zakelijk recht
    - **Verschillen**:
        - Opstal: recht TE BOUWEN op andermans grond + eigendom werk
        - Erfpacht: vol genot bestaand goed
