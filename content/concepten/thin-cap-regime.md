---
title: "Thin-cap-regime (interestaftrekbeperking)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.XVI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/thin-cap-regime.json"
---

# Thin-cap-regime (interestaftrekbeperking)

_Regime_

📋 Regeling · Anchors: `2.8.XVI` · Wave: `fiscale-voordelen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: ATAD-interestbeperking · art. 198/1 WIB92 · EBITDA-rule

## Definitie

📖 Het thin-cap-regime of EBITDA-regel (art. 198/1 WIB92) beperkt de aftrekbaarheid van het financieringskostensurplus van vennootschappen — d.i. interestlasten min interestopbrengsten — tot het hoogste van twee drempels: (a) 30 % van de fiscale EBITDA, of (b) 3.000.000 EUR (safe-harbour-drempel). Het regime implementeert artikel 4 van de EU-anti-belastingontwijkingsrichtlijn (ATAD, richtlijn 2016/1164/EU) en geldt sinds aanslagjaar 2020 voor boekjaren die op of na 1-1-2019 starten. Doel: tegengaan van excessieve schuldfinanciering en winstverschuiving binnen multinationale groepen via interne leningen.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · ATAD (richtlijn 2016/1164/EU) — art. 4 — _richtlijn_</small>

## Substantie

📖 Concreet: een vennootschap berekent het financieringskostensurplus = aftrekbare interesten betaald MIN belastbare interesten ontvangen. Daarna berekent ze de fiscale EBITDA = belastbaar resultaat + interestlasten + afschrijvingen − interestopbrengsten − niet-belastbare bestanddelen. Indien financieringskostensurplus ≤ max(30 % × EBITDA ; 3 mio): alles aftrekbaar. Indien hoger: het overschot wordt VERWORPEN UITGAVE in het lopende jaar, maar onbeperkt overdraagbaar naar volgende jaren (waar het opnieuw aan de toets onderworpen wordt). Het regime heeft geen impact op KMO's (de 3 mio-drempel beschermt ze de facto) en op puur eigen-vermogen-gefinancierde vennootschappen.

<small>📚 WIB92 — art. 198/1 §1 — _wettekst_ · WIB92 — art. 194sexies — _wettekst_ · CBN-advies — 2020/06 — Financieringskostensurplus art. 194sexies — _cbn_</small>

## Rationale

🔗 Ratio legis: multinationals kunnen winst verschuiven naar laag-belaste jurisdicties door binnen een groep een schuldconstructie op te zetten — de Belgische vennootschap leent van een groepsmaatschappij in een belastingparadijs, betaalt aftrekbare intrest, en de groepsmaatschappij ontvangt deze intrest aan een laag tarief. EBITDA-regel doorbreekt dit door interestaftrek te plafonneren ongeacht aan wie de intrest betaald wordt. ATAD-richtlijn wil unilateraal misbruik tegengaan binnen de EU; België implementeerde minimum-standaard. De 3 mio safe-harbour beschermt KMO's en niet-systemische schulden — alleen substantiële financieringsstromen worden geraakt.

<small>📚 ATAD — art. 4 + considerans 6-12 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-01-01** · basis: WIB92 art. 198/1 + KB/WIB92 art. 73/4/2 (uitvoeringsmaatregelen)

Geldt voor boekjaren die op of na 1-1-2019 aanvangen (AJ 2020 en volgende). Standstill-clausule voor leningen aangegaan vóór 17-6-2016 verviel op 31-12-2024 — sindsdien gelden ALLE leningen onder dit regime.

**✅ Voor**
- 🔗 Vennootschappen met aanzienlijk financieringskostensurplus, typisch: multinationale groepen met interne leningen, kapitaalintensieve sectoren (vastgoed, infrastructuur, private equity), vennootschappen met externe schuldfinanciering > 3 mio interest/jaar. De facto geldt het regime hoofdzakelijk voor middelgrote tot grote vennootschappen — KMO's blijven onder de 3 mio drempel.

**⛔ Uitsluitingen**
- 📖 Het regime is NIET van toepassing op: (a) zelfstandige vennootschappen (geen onderdeel van groep én geen vaste inrichting buitenland — strikt gedefinieerd); (b) financiële ondernemingen (banken, verzekeraars, AICB's met afwijkende regels); (c) leningen voor lange-termijn-openbare-infrastructuur-projecten (specifieke EU-uitzondering).

**⚠️ Risico**
- 📖 Bij overschrijden drempel: het overschot wordt VERWORPEN UITGAVE in het lopende boekjaar — dus geen aftrek tegen 25 % VenB-tarief, effectieve kost = 25 % × niet-aftrekbaar bedrag. Niet-aftrekbaar saldo onbeperkt overdraagbaar, maar moet elk jaar opnieuw de toets ondergaan. Bij groep met interestaftrekovereenkomst (CBN-advies 2020/06): mogelijkheid om overschotten van een vennootschap met EBITDA-marge over te dragen naar een groepslid met overschot — boekhoudkundige verwerking vereist regularisatie van geraamde belastingen.

## Bouwstenen

### 📏 30 %-EBITDA-drempel  
_`drempel`_

📖 Het financieringskostensurplus is aftrekbaar tot 30 % van de fiscale EBITDA. EBITDA = belastbaar resultaat (vóór art. 198/1) + financieringskostensurplus + afschrijvingen − niet-belastbare opbrengsten − bij verdrag vrijgestelde winst. Bij negatieve EBITDA: het deel boven 0 telt, anders 30 % × 0 = 0 (geen EBITDA-aftrekruimte — alleen safe-harbour 3 mio).

<small>📚 WIB92 — art. 198/1 §1 — _wettekst_</small>

### 📏 Safe-harbour 3 mio EUR  
_`drempel`_

📖 Naast 30 % EBITDA: vennootschap mag steeds tot 3.000.000 EUR financieringskostensurplus aftrekken, ongeacht EBITDA. De vennootschap kiest het HOOGSTE van beide drempels (max(30 % EBITDA ; 3 mio)). Dit beschermt KMO's en vennootschappen met tijdelijk lage EBITDA. Drempel per BELASTINGGROEP toegepast (niet per individuele vennootschap) wanneer Belgische groep — verdeling over groepsleden volgens art. 73/4/2 KB/WIB92.

<small>📚 WIB92 — art. 198/1 §1 tweede lid — _wettekst_</small>

### 🧮 Financieringskostensurplus — definitie  
_`formule`_

📖 Financieringskostensurplus = bruto-interestlasten van het belastbaar tijdperk (aftrekbaar van de belastbare basis) MIN bruto-interestopbrengsten van het belastbaar tijdperk (belastbaar). Begrip 'interest' is ruim: nominale interest + economisch equivalent (discount/agio op leningen, bepaalde derivaten, gekapitaliseerde interest, ...). Niet inbegrepen: kosten van eigen aandelen (zoals dividenden — die zijn niet aftrekbaar én niet interest).

<small>📚 WIB92 — art. 198/1 §1 tweede lid — _wettekst_</small>

### ⚙️ Overdracht niet-aftrekbaar overschot  
_`mechanisme`_

📖 Niet-aftrekbaar surplus van het lopende boekjaar is onbeperkt overdraagbaar naar volgende belastbare tijdperken (art. 198/1 §2 WIB92). In volgend jaar telt het overschot mee in het financieringskostensurplus, samen met het nieuwe surplus van dat jaar — opnieuw onderworpen aan de toets. Belang: vennootschappen kunnen jaren van hoge interest 'uitsmeren' over jaren van hoge EBITDA. Geen vervaltermijn.

<small>📚 WIB92 — art. 198/1 §2 — _wettekst_</small>

### ⚙️ Groeps-interestaftrekovereenkomst (art. 194sexies)  
_`mechanisme`_

📖 Belgische vennootschappen die deel uitmaken van eenzelfde groep kunnen via formele overeenkomst niet-gebruikte aftrekruimte 'overdragen': vennootschap A met EBITDA-overschot draagt aftrekruimte over aan vennootschap B met financieringskostensurplus boven haar eigen drempel. Vergoeding tussen partijen mogelijk (CBN-advies 2020/06 geeft boekhoudkundig kader). Voorwaarden: schriftelijke overeenkomst, beide vennootschappen Belgisch, deel van zelfde groep, ondertekening vóór indiening aangifte VenB.

<small>📚 WIB92 — art. 194sexies — _wettekst_ · CBN-advies — 2020/06 — _cbn_</small>

## Voorbeelden

### 💡 Grote vennootschap met substantiële financiering 🔗

_Vastgoed Holding NV heeft in jaar N: interestlasten 8 mio EUR, interestopbrengsten 1 mio EUR (op cash-deposito's); belastbaar resultaat vóór art. 198/1: 15 mio EUR; afschrijvingen: 4 mio EUR; geen bij-verdrag-vrijgestelde winst._

**Berekening:**
- Stap 1 — financieringskostensurplus = 8.000.000 − 1.000.000 = 7.000.000 EUR.
- Stap 2 — EBITDA = 15.000.000 (belastbaar resultaat) + 7.000.000 (FKS) + 4.000.000 (afschrijvingen) − 0 = 26.000.000 EUR.
- Stap 3 — drempels: 30 % × 26.000.000 = 7.800.000 EUR  ;  safe-harbour = 3.000.000 EUR. Max = 7.800.000 EUR.
- Stap 4 — aftrekbaar surplus = min(7.000.000 ; 7.800.000) = 7.000.000 EUR → alles aftrekbaar.
- Stap 5 — geen verworpen uitgave, geen overdracht. Vennootschap blijft binnen drempel.

→ **Resultaat**: Geen impact art. 198/1 dit jaar. Maar: bij toename interestlasten naar 12 mio in volgend jaar zou FKS = 11 mio en drempel 7,8 mio (constante EBITDA) overschreden worden → 3,2 mio verworpen uitgave.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Drempels optellen i.p.v. maximum nemen

**Verkeerde assumptie**: Aftrekruimte = 30 % EBITDA + 3 mio safe-harbour.

**Kernpunt**: De wet schrijft het HOOGSTE van beide voor (max-functie, niet som). Concreet: een vennootschap met EBITDA 20 mio heeft aftrekruimte max(30 % × 20 mio = 6 mio ; 3 mio) = 6 mio. NIET 9 mio. Klassieke berekenfout bij studenten.

<small>📚 WIB92 — art. 198/1 §1 tweede lid — _wettekst_</small>

### ⚠️ Boekhoudkundige EBITDA i.p.v. fiscale EBITDA

**Verkeerde assumptie**: EBITDA uit jaarrekening = EBITDA voor art. 198/1.

**Kernpunt**: Fiscale EBITDA vertrekt van het belastbaar resultaat (na alle verwerping uitgaven, na DBI-aftrek-buiten-volgorde aanpassingen, ...), niet van het boekhoudkundig resultaat. Specifiek: bij-verdrag-vrijgestelde winst wordt UITGESLOTEN — een vennootschap met grote buitenlandse vaste inrichting kan dus lager EBITDA hebben dan boekhoudkundig verwacht.

<small>📚 WIB92 — art. 198/1 §1 tweede lid — _wettekst_</small>

### ⚠️ Standstill-uitzondering voor pre-2016-leningen blijven gebruiken

**Verkeerde assumptie**: Leningen aangegaan vóór 17-6-2016 vallen buiten het regime.

**Kernpunt**: De standstill-clausule voor pre-17-6-2016-leningen verviel op 31-12-2024. Vanaf AJ 2025 (boekjaren in 2024) gelden ALLE leningen onder het regime, ongeacht aanvangsdatum. Belangrijk voor langlopende vastgoedfinanciering of inter-company-leningen die vóór 2016 werden aangegaan.

<small>📚 WIB92 — art. 198/1 (overgangsregeling vervallen) — _wettekst_</small>

## Accountant-perspectieven

### Vennootschap met substantiële interestlasten

_Accountant van een vennootschap die jaarlijks de art. 198/1-toets moet doen._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijkse 198/1-toets  
_`stap`_

🔗 Per boekjaar: (1) bereken financieringskostensurplus uit grootboek (interestkosten 65x − interestopbrengsten 75x, met aandacht voor economische equivalenten); (2) bereken fiscale EBITDA vertrekkend van belastbaar resultaat vóór art. 198/1, optellen FKS + afschrijvingen 6300/6301, aftrekken niet-belastbare opbrengsten en bij-verdrag-vrijgestelde winst; (3) bereken max(30 % EBITDA ; 3 mio); (4) bepaal niet-aftrekbaar surplus; (5) opname verworpen uitgave in aangifte + overdracht in tabel niet-aftrekbaar surplus.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Overweging groeps-interestaftrekovereenkomst  
_`regel`_

📖 Bij Belgische vennootschap-groep: indien één vennootschap aftrekruimte over heeft en andere boven drempel zit, formele overeenkomst sluiten (art. 194sexies). Voordeel: ongebruikte ruimte in groep wordt benut. Vergoeding tussen partijen mogelijk (arms-length-prijs). Boekhoudkundige verwerking volgens CBN-advies 2020/06: vennootschap met overschot ontvangt vergoeding, vennootschap met tekort betaalt — geraamde belastingen worden geregulariseerd.

<small>📚 WIB92 — art. 194sexies — _wettekst_ · CBN-advies — 2020/06 — _cbn_</small>

#### 🔍 Auditor

##### 👣 Controle berekening FKS + EBITDA  
_`stap`_

🔗 Bij audit: nagaan dat alle interestlasten en -opbrengsten correct geïdentificeerd zijn (inclusief economische equivalenten zoals embedded interest in leasing-overeenkomsten, factoring, ...). Reconciliatie tussen boekhoudkundige interestposten en fiscale FKS. Cross-check met aangifte: drempels correct toegepast, overgedragen overschot uit vorig jaar correct meegenomen, groeps-overeenkomst documentatie consistent.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → ATAD-richtlijn (grondslag) → [[atad-richtlijn]] _(moet-verwijzen)_
- → Σ-keuzekader anti-misbruik → [[anti-misbruik]] _(moet-verwijzen)_
- ↪ Schuldfinanciering (cross-cluster) → [[schuldfinanciering]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[anti-misbruik]]
### `beinvloed_door`
- [[atad-richtlijn]] — Implementatie van art. 4 ATAD-richtlijn 2016/1164/EU.
### `triggert`
- [[aangifte-vennootschapsbelasting]] — Verworpen uitgave + tabel overdracht overschot in aangifte VenB.
