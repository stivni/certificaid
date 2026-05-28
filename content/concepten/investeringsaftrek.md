---
title: "Investeringsaftrek"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.E
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/investeringsaftrek.json"
---

# Investeringsaftrek

_Regime_

📋 Regeling · Anchors: `2.3.II.E` · Wave: `fiscale-voordelen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: aftrek voor investeringen · art. 68-77 WIB92

## Definitie

📖 De investeringsaftrek (art. 68-77 WIB92) is een extra fiscale aftrek bovenop de gewone afschrijving van een nieuw bedrijfsactivum. Een percentage van de aanschaffingswaarde wordt afgetrokken van de belastbare winst, eenmalig (in het jaar van investering) of gespreid (over de afschrijvingsperiode). Het percentage hangt af van de categorie investering: basis (8 % voor KMO's) of verhoogd voor specifieke doelen (energiebesparing, milieuvriendelijke investeringen, beveiliging, octrooien, digitalisering, R&D, ...).

<small>📚 WIB92 — art. 68 — _wettekst_ · WIB92 — art. 69 — _wettekst_</small>

## Substantie

🔗 Het effect is een dubbel fiscaal voordeel: het activum wordt zowel afgeschreven (verlaagt belastbare winst gedurende afschrijvingsperiode) ALS profiteert van investeringsaftrek (extra verlaging in jaar van investering, of pro rata gespreid). Bv. een KMO koopt een productiemachine van 100.000 EUR: basis-aftrek 8 % = 8.000 EUR extra aftrek, bovenop afschrijving 10.000 EUR (over 10 jaar). Voor digitale investeringen (vanaf 2018): KMO-percentage tot 13,5 %; voor R&D: 13,5 % eenmalig of 20,5 % gespreid; voor energiebesparing: 13,5 %. Cijferzakboekje raadplegen voor actuele percentages — die wisselen per aanslagjaar door indexering.

<small>📚 WIB92 — art. 69 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: stimuleren van bedrijfsinvesteringen, vooral in beleidsprioritaire categorieën (groen, digitaal, R&D, KMO-investeringen). De aftrek werkt als een 'verborgen subsidie' via lager belastbaar inkomen i.p.v. directe steun. Voor de begroting goedkoper dan rechtstreekse subsidies; voor de onderneming flexibel inzetbaar zonder aparte aanvraag (mits attest waar vereist). De koppeling aan KMO-statuut versterkt het effect voor kleinere onderneminkingen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 68-77 + KB/WIB92

Stabiel basisregime sinds invoering WIB92, maar percentages en categorieën worden regelmatig aangepast (bv. digitale investeringen toegevoegd 2018; verhoging voor energie/groen 2022).

**✅ Voor**
- 📖 Vennootschap of zelfstandige met beroepsinkomen die NIEUWE afschrijfbare materiële of immateriële vaste activa verkrijgt of vervaardigt in België voor de beroepswerkzaamheid. KMO-status (art. 1:24 WVV) geeft toegang tot basis-aftrek 8 %; grote vennootschappen hebben enkel de verhoogde categorieën (R&D, octrooi, energie, ...).

**📋 Voorwaarden**
- 📖 Cumulatief: (1) nieuw afschrijfbaar activum; (2) verkregen of vervaardigd in het lopende belastbare tijdperk; (3) uitsluitend gebruikt voor beroepswerkzaamheid in België; (4) bij verhoogde aftrek: relevant attest (BELSPO voor R&D, gewestelijke attestering voor energie/milieu, ...); (5) opgave 276U bij de aangifte VenB.

**⛔ Uitsluitingen**
- 📖 Niet-aftrekbaar: tweedehands activa (behalve specifieke uitzonderingen), niet voor beroepsdoeleinden gebruikte activa, personenwagens (met uitzondering elektrische sinds 2023), activa die hoofdzakelijk in het buitenland gebruikt worden, activa waarvan het gebruiksrecht is afgestaan aan een derde die zelf niet voor de aftrek in aanmerking komt.

**👍 Voordeel**
- 📖 Onmiddellijke verlaging belastbare basis (eenmalig) of gespreid over afschrijvingsperiode. Combineerbaar met innovatie-aftrek (anders gegrond) en gespreide belasting meerwaarden. Niet-gebruikt deel overdraagbaar (basis-aftrek: onbeperkt; verhoogde aftrekken: variabel — Cijferzakboekje raadplegen).

**⚠️ Risico**
- 📖 Indien de voorwaarden niet volledig vervuld blijven gedurende een minimum-gebruiksperiode (bv. doorverkoop van activum binnen 3 jaar): terugneming van de aftrek + nalatigheidsinteresten. Bij verhoogde aftrek zonder geldig attest: aftrek wordt volledig verworpen.

## Bouwstenen

### 📏 Basis-investeringsaftrek (KMO)  
_`drempel`_

📖 Voor KMO's (art. 1:24 WVV): basis-aftrek 8 % van de aanschaffingswaarde, eenmalig in het jaar van investering. Geldt voor alle nieuwe afschrijfbare activa zonder bijzondere categorie. Geen attest vereist. NIET beschikbaar voor grote vennootschappen. Percentage indexeerbaar; in het Cijferzakboekje het actuele percentage opzoeken.

<small>📚 WIB92 — art. 69 §1 1° — _wettekst_ · WIB92 — art. 201 — _wettekst_</small>

### 📜 Verhoogde aftrekken — categorieën  
_`regel`_

📖 Verhoogde percentages voor specifieke investeringen (orde van grootte, geïndexeerd — Cijferzakboekje voor exact bedrag): (a) octrooien: 13,5 % eenmalig of 20,5 % gespreid; (b) energiebesparing: 13,5 %; (c) milieuvriendelijke R&D-investeringen: 13,5 % eenmalig of 20,5 % gespreid; (d) zeevaart, scheepsbouw: tot 30 %; (e) digitalisering (vanaf 2018): 13,5 % voor KMO; (f) beveiligingsinvesteringen: 20,5 % voor KMO. Beschikbaar voor zowel KMO als grote vennootschap (op enkele uitzonderingen na zoals digitale aftrek = KMO-only).

<small>📚 WIB92 — art. 69 §1 — _wettekst_ · WIB92 — art. 70 — _wettekst_</small>

### ⚙️ Eenmalig vs gespreid  
_`mechanisme`_

📖 Eenmalige aftrek: het volledige percentage × aanschaffingswaarde wordt in het jaar van investering afgetrokken. Gespreide aftrek (alleen voor R&D-investeringen en octrooien): het percentage × jaarlijkse afschrijving wordt elk jaar gedurende afschrijvingsperiode afgetrokken — geeft een hoger totaal-percentage (20,5 % i.p.v. 13,5 %), maar gespreid over afschrijvingsperiode. Keuze hangt af van fiscale planning: eenmalig bij voldoende huidige winst; gespreid bij verwachte hogere toekomstige winsten.

<small>📚 WIB92 — art. 70 — _wettekst_</small>

### ⚙️ Overdracht ongebruikte aftrek  
_`mechanisme`_

📖 Indien onvoldoende winst: ongebruikt deel kan worden overgedragen. Basis-aftrek KMO: onbeperkt overdraagbaar. Verhoogde aftrekken: overdraagbaar voor variabele duur (vroeger 1 jaar, nu meestal onbeperkt voor R&D/octrooi; voor andere verhoogde aftrekken specifieke regels). Investeringsaftrek wordt enkel toegepast op het Belgisch resultaat in de aangifte VenB (code 1437), niet op het buitenlandse deel.

<small>📚 WIB92 — art. 72 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — code 1437 — _aangifte_</small>

## Voorbeelden

### 💡 Zelena Bio NV (KMO) — basis-aftrek op nieuwe machine 🔗

_Zelena Bio NV koopt in jaar N een nieuwe productiemachine voor 150.000 EUR. Afschrijving lineair over 10 jaar = 15.000 EUR/jaar. Zelena is een KMO (art. 1:24 WVV)._

**Berekening:**
- Stap 1 — basis-investeringsaftrek 8 % × 150.000 = 12.000 EUR (eenmalig).
- Stap 2 — jaar N: belastbare winst wordt verlaagd met 15.000 (afschrijving) + 12.000 (investeringsaftrek) = 27.000 EUR.
- Stap 3 — jaren N+1 tot N+9: enkel afschrijving 15.000/jaar verlaagt belastbare basis.
- Stap 4 — bij VenB-tarief 25 %: extra fiscaal voordeel jaar N = 12.000 × 25 % = 3.000 EUR. Bij KMO-tarief 20 % op eerste schijf: 12.000 × 20 % = 2.400 EUR.
- Stap 5 — opgave 276U bij aangifte VenB, code 1437 in uiteenzetting winst.

→ **Resultaat**: Extra fiscaal voordeel van 3.000 EUR onmiddellijk, bovenop de gewone fiscale aftrek van afschrijvingen.

<small>📚 WIB92 — art. 69 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Tweedehands activa fiscaal aftrek opvoeren

**Verkeerde assumptie**: Investeringsaftrek geldt voor alle bedrijfsinvesteringen.

**Kernpunt**: Enkel NIEUWE afschrijfbare activa komen in aanmerking (art. 75 WIB92). Tweedehands wagens, gebruikte machines: geen investeringsaftrek. Uitzondering: tweedehands binnenvaartschepen onder bepaalde voorwaarden. Bij twijfel: factuur + leveranciersverklaring nakijken (nieuw vs gebruikt).

<small>📚 WIB92 — art. 75 — _wettekst_</small>

### ⚠️ Verhoogde aftrek opnemen zonder attest

**Verkeerde assumptie**: Een energiebesparende of R&D-investering geeft automatisch recht op verhoogde aftrek.

**Kernpunt**: Verhoogde aftrek vereist een formeel attest: BELSPO-attest (R&D), gewestelijk attest (energie/milieu) of certificatie (digitalisering). Aanvraag moet binnen specifieke termijnen gebeuren — soms vóór de investering. Zonder attest: enkel basis-aftrek (KMO) of nul (grote vennootschap).

<small>📚 WIB92 — art. 77 — _wettekst_ · WIB92 — art. 70 — _wettekst_</small>

### ⚠️ Investeringsaftrek op buitenlandse winst toepassen

**Verkeerde assumptie**: De aftrek kan op de totale winst toegepast worden.

**Kernpunt**: In de aangifte VenB wordt de investeringsaftrek enkel op het Belgisch resultaat toegepast (code 1437) — niet op het bij verdrag vrijgestelde buitenlandse deel, en niet op de niet-bij-verdrag-vrijgestelde buitenlandse winst. Voor multinationale activiteit: aftrek beperkt tot Belgische component.

<small>📚 aangifte-VenB-2025-uiteenzetting-winst — code 1437 — kolom Belgisch resterend resultaat — _aangifte_</small>

## Accountant-perspectieven

### KMO-vennootschap die investeert

_Accountant van een KMO die jaarlijks investeringen plant en de fiscale impact wenst te optimaliseren._

#### 💰 Fiscaal adviseur

##### 👣 Investerings-categorisatie + percentage  
_`stap`_

🔗 Voor elke nieuwe investering in het boekjaar: (1) check nieuwheid (factuur, leverancier-attest); (2) bepaal categorie: basis (8 %) of verhoogd (energie 13,5 %, R&D 13,5 %/20,5 %, digitaal 13,5 % KMO, beveiliging 20,5 % KMO, ...); (3) indien verhoogd: attest aanvragen binnen termijn (typisch 3 maanden na sluiting boekjaar); (4) opgave 276U bij aangifte. Cijferzakboekje raadplegen voor actueel percentage per AJ.

<small>📚 WIB92 — art. 69-77 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Keuze eenmalig vs gespreid  
_`regel`_

🔗 Voor R&D-investeringen en octrooien is keuze mogelijk: eenmalig 13,5 % nu of gespreid 20,5 % over afschrijvingsperiode. Vuistregel: bij voldoende huidige winst en geen verwachte sterke groei → eenmalig (sneller voordeel). Bij verwachte winstgroei en zekerheid over voortbestaan → gespreid (hoger totaal-percentage). Combineer met meerjaren-fiscale-planning.

<small>📚 WIB92 — art. 70 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ Σ-keuzekader VenB-voordelen → [[fiscale-voordelen-vennootschap]] _(mag-verwijzen)_
- ↪ Innovatie-aftrek (verwant — IP) → [[innovatie-aftrek]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-voordelen-vennootschap]]
### `triggert`
- [[aangifte-vennootschapsbelasting]] — Aftrek via code 1437 + opgave 276U.
### `vereist`
- [[afschrijvingen]] — Veronderstelt afschrijfbaar activum.
