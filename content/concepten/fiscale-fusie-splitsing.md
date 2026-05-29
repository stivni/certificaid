---
title: "Fiscale fusie-splitsing"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.taak.2
  - 3.0.taak.3
  - 2.3.III.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-fusie-splitsing.json"
---

_Regime_ · ook: fiscale neutraliteit fusie/splitsing · fiscaal-neutraal regime herstructurering · rollover-regime

## Definitie

Het regime van de fiscale fusie-splitsing is het fiscaal-neutrale regime in de vennootschapsbelasting voor fusies, splitsingen en met fusie of splitsing gelijkgestelde verrichtingen. De kern: latente meerwaarden die in de overgedragen activa schuilen worden niet onmiddellijk belast, op voorwaarde dat de verkrijgende vennootschap de waarderingen en fiscale historiek van de overdrager voortzet. Het regime is verankerd in artikelen 211 tot 214 WIB92, ondersteund door artikel 183bis (anti-misbruik) en — voor grensoverschrijdende verrichtingen — door de EU-Richtlijn 2009/133/EG.

<small>📖 WIB92 — art. 211 par. 1 — _wettekst_ · WIB92 — art. 212 — _wettekst_ · EU-Richtlijn 2009/133/EG (fusierichtlijn) — considerans 2 + art. 4 — _richtlijn_</small>

## Substantie

Zonder dit regime zou elke herstructurering economisch onmogelijk worden gemaakt door belasting. Stel: een vennootschap heeft een gebouw met boekwaarde 1.000.000 EUR en marktwaarde 3.000.000 EUR (latente meerwaarde 2.000.000 EUR). Bij een gewone verkoop wordt die meerwaarde belast tegen 25% VenB — een afrekening van 500.000 EUR. Bij een fiscaal-neutrale fusie wordt die belasting niet onmiddellijk geheven: de overnemer neemt het gebouw over tegen dezelfde boekwaarde 1.000.000 EUR en zet daar de latente meerwaarde voort. Pas wanneer de overnemer het gebouw later effectief verkoopt, wordt belast. Het is een 'uitstel' — niet een 'kwijtschelding'. Dat is het rollover-mechanisme.

<small>🔗 WIB92 — art. 211 par. 1 + art. 212 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het regime balanceert twee belangen. Enerzijds wil de wetgever herstructureringen niet bestraffen — dat is economisch nuttig en typisch belastingneutraal in werkelijkheid (geen geld stroomt naar buiten). Anderzijds wil de wetgever vermijden dat fusies en splitsingen worden gebruikt om meerwaarden zonder belasting te verzilveren, of om verliezen op te kopen die buiten de groep nooit fiscaal nuttig zouden zijn. Vandaar de voorwaarden: continuiteit (geen step-up in waardering) plus zakelijke motivering (geen kunstmatige constructie). De EU-richtlijn dwingt deze logica op alle lidstaten af om de Europese interne markt voor herstructurering open te houden.

<small>🔗 WIB92 — art. 211 + 183bis — _wettekst_ · EU-Richtlijn 2009/133/EG — considerans 2-5 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **1992-01-01** · basis: WIB92 art. 211-214 + 183bis; EU-Richtlijn 2009/133/EG (gecodificeerde versie)

**✅ Voor**
- 📖 Binnenlandse fusies, splitsingen en gelijkgestelde verrichtingen tussen Belgische vennootschappen onderworpen aan VenB.
- 📖 Grensoverschrijdende verrichtingen binnen de EU: een Belgische vennootschap wordt overgenomen door of fuseert met een intra-Europese vennootschap.

**🚫 Niet voor**
- 🔗 Verrichtingen met derde landen buiten de EU: deze vallen niet automatisch onder het neutraliteitsregime — er kunnen nationale verschillen of bilateraal verdrag spelen.
- 📖 Verrichtingen die kwalificeren als belastingontwijking onder art. 183bis WIB92 — neutraliteit wordt geweigerd of teruggedraaid.

**📋 Voorwaarden**
- 📖 De verkrijgende vennootschap is een binnenlandse of intra-Europese vennootschap onderworpen aan een belasting gelijkaardig aan de VenB.
- 📖 Boekhoudkundige en fiscale continuiteit: de verkrijger zet de waarderingen, afschrijvingen, voorzieningen en vrijgestelde reserves voort op dezelfde basis als bij de overdrager (art. 212 WIB92).
- 📖 De verrichting moet gebaseerd zijn op zakelijke overwegingen, niet op belastingfraude of -ontwijking als hoofddoel (art. 183bis WIB92 — omzetting van art. 15 EU-fusierichtlijn).
- 📖 De opleg in geld blijft binnen de 10%-grens (art. 2 — 6°/1 WIB92).

**👍 Voordeel**
- 📖 Geen onmiddellijke belasting van latente meerwaarden bij de overgedragen activa.
- 📖 Vrijgestelde reserves, kapitaalsubsidies en herwaarderingsmeerwaarden blijven onaangetast (overgenomen onder dezelfde voorwaarden).
- 📖 Fiscaal overgedragen verliezen, DBI-overschotten en niet-benutte aftrekken kunnen worden overgenomen (beperkt naar pro-rata fiscaal netto-actief, art. 206 par. 2 WIB92).
- 📖 Voor de aandeelhouder-natuurlijke persoon: vrijstelling van belasting op de aandelenruil onder art. 95 + 96 WIB92.

**⚠️ Risico**
- 📖 Herkwalificatie als belastingontwijking (art. 183bis): de fiscus weigert de neutraliteit en belast de meerwaarden, mogelijks met belastingverhoging.
- 📖 Doorbreking van de continuiteit (bv. door step-up in boekwaarde bij de overnemer): realisatie van meerwaarden wordt alsnog belast.
- 🔗 Verlies van fiscale neutraliteit bij niet-naleving van de onaantastbaarheidsvoorwaarde voor vrijgestelde reserves: heffing op die reserves bij latere uitkering.

## Sub-concepten

### 📦 Continuiteit van waardering

#### Definitie

De verkrijgende vennootschap neemt elk overgedragen actief over tegen de boekwaarde en fiscale waarde die het op het moment van de fusie/splitsing had in de boeken van de overdrager. Afschrijvingen lopen verder op de oorspronkelijke aanschaffingswaarde; vrijgestelde reserves blijven hun status behouden; voorzieningen worden in dezelfde context voortgezet. Voor latere meerwaarden geldt steeds de oorspronkelijke historische waarde als referentie (art. 212 WIB92).

<small>📖 WIB92 — art. 212 — _wettekst_</small>

### 📦 Anti-misbruik-test (art. 183bis WIB92)

#### Definitie

Een fusie of splitsing valt niet onder het neutraliteitsregime als belastingfraude of -ontwijking het hoofddoel of een van de hoofddoelen is. Een verrichting wordt vermoed door fraude/ontwijking gemotiveerd te zijn als ze niet plaatsvindt op grond van zakelijke overwegingen, zoals herstructurering of rationalisering van de activiteiten. Het bewijs van zakelijke overwegingen ligt bij de belastingplichtige.

<small>📖 WIB92 — art. 183bis — _wettekst_ · EU-Richtlijn 2009/133/EG — art. 15 — _richtlijn_</small>

#### Rationale

De wetgever wil voorkomen dat het neutraliteitsregime wordt misbruikt voor zuiver fiscale doeleinden — bv. een fusie die alleen bedoeld is om verliezen op te kopen, of een splitsing die in feite een verkapte liquidatie is. Het bestuursverslag dat aan de AV wordt voorgelegd, moet de zakelijke motivering documenteren — vandaar het belang van een goed onderbouwd bestuursverslag.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Verliesoverdracht bij fusie/splitsing

#### Definitie

Fiscaal overgedragen verliezen van de overgenomen vennootschap kunnen door de verkrijger worden voortgezet, maar slechts beperkt. De verkrijger mag verliezen aftrekken in verhouding tot het fiscaal netto-actief van de overgenomen vennootschap ten opzichte van het totale fiscaal netto-actief na fusie (art. 206 par. 2 WIB92). Dit voorkomt 'verliesopkoop'.

<small>📖 WIB92 — art. 206 par. 2 — _wettekst_ · WIB92 — art. 213 — _wettekst_</small>

#### Substantie

Voorbeeld: vennootschap A (overdrager) heeft 500.000 EUR overgedragen verliezen en een fiscaal netto-actief van 1.000.000 EUR. Vennootschap B (verkrijger) heeft eveneens 1.000.000 EUR fiscaal netto-actief. Na de fusie is het gecombineerd netto-actief 2.000.000 EUR. De overgedragen verliezen van A kunnen worden gebruikt door B, beperkt tot 500.000 EUR × (1.000.000 / 2.000.000) = 250.000 EUR. De helft van de verliezen wordt fiscaal 'verloren'.

<small>🔗 WIB92 — art. 206 par. 2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Vrijstelling aandeelhouder bij aandelenruil

#### Definitie

Voor de aandeelhouder-natuurlijke persoon (PB) en de aandeelhouder-vennootschap geldt een tijdelijke vrijstelling voor de meerwaarde gerealiseerd bij de aandelenruil. De ontvangen nieuwe aandelen vervangen fiscaal de oude — de aanschaffingswaarde wordt overgedragen (art. 95 + 96 WIB92, omzetting van art. 8 EU-fusierichtlijn). Effect: belasting wordt uitgesteld tot de uiteindelijke verkoop van de nieuwe aandelen door de aandeelhouder.

<small>📖 WIB92 — art. 95 — _wettekst_ · WIB92 — art. 96 — _wettekst_ · EU-Richtlijn 2009/133/EG — art. 8 — _richtlijn_</small>

## Bouwstenen

### ⚙️ Rollover-mechanisme — uitstel, geen kwijtschelding

Latente meerwaarden worden niet belast bij de fusie/splitsing zelf, maar de fiscale claim 'rolt' mee naar de verkrijger. Bij latere verkoop of realisatie door de verkrijger wordt alsnog belast — met als referentie de oorspronkelijke aanschaffingswaarde. Dat is uitstel, geen kwijtschelding.

<small>🔗 WIB92 — art. 212 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Bewijs van zakelijke overwegingen

De belastingplichtige moet aantonen dat de verrichting plaatsvindt op grond van zakelijke overwegingen. Aanvaardbare motieven: schaalvoordelen, herstructurering van activiteiten, vereenvoudiging van de groepsstructuur, financierings- of marktoverwegingen, opvolgingsplanning. Niet-aanvaardbare motieven: enkel verlies-opkoop, uitkering van reserves vermomd als kapitaalvermindering.

<small>🔗 WIB92 — art. 183bis — _wettekst_ · EU-Richtlijn 2009/133/EG — art. 15 — _richtlijn_</small>

## Voorbeelden

> [!example]- Latente meerwaarde op gebouw bij fusie Aurelia-Zelena
> _Aurelia Holding NV neemt Zelena Bio NV over. Zelena bezit een gebouw met boekwaarde 1.000.000 EUR, marktwaarde 3.000.000 EUR, latente meerwaarde 2.000.000 EUR._
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Neutraliteit verwarren met definitieve vrijstelling
> **Verkeerde assumptie**: De fiscale fusie elimineert de belastingclaim op latente meerwaarden.
>
> **Kernpunt**: Het regime is een uitstel, geen kwijtschelding. De fiscale claim 'rolt' mee naar de verkrijger. Bij latere verkoop door de verkrijger wordt alsnog belast op basis van de oorspronkelijke aanschaffingswaarde van de overdrager. Wat je vandaag niet betaalt, betaal je later.
>
> <small>📖 WIB92 — art. 212 — _wettekst_</small>

> [!warning]- Verliesoverdracht volledig achten
> **Verkeerde assumptie**: Alle overgedragen verliezen van de overgenomen vennootschap kunnen volledig worden gebruikt door de verkrijger.
>
> **Kernpunt**: De verliesoverdracht is beperkt naar verhouding van het fiscaal netto-actief van de overgenomen vennootschap ten opzichte van het gecombineerd fiscaal netto-actief na fusie (art. 206 par. 2 WIB92). Een deel van de verliezen kan dus fiscaal 'verloren' gaan — een belangrijke kost van fusie die in de pre-merger-due-diligence moet worden begroot.
>
> <small>📖 WIB92 — art. 206 par. 2 — _wettekst_</small>

> [!warning]- Anti-misbruik onderschatten
> **Verkeerde assumptie**: Als de verrichting WVV-rechtelijk klopt, accepteert de fiscus de neutraliteit automatisch.
>
> **Kernpunt**: De fiscus toetst zelfstandig of er zakelijke overwegingen zijn (art. 183bis WIB92). Een vennootschapsrechtelijk geldige fusie kan fiscaal worden afgekeurd als bv. de hoofdmotivering verliesopkoop of dividend-vermijding is. Het bestuursverslag moet de zakelijke motivering documenteren — een ruling-aanvraag bij de Dienst Voorafgaande Beslissingen kan voor rechtszekerheid zorgen.
>
> <small>📖 WIB92 — art. 183bis — _wettekst_</small>

> [!warning]- Onaantastbaarheidsvoorwaarde vergeten bij vrijgestelde reserves
> **Verkeerde assumptie**: Vrijgestelde reserves blijven na de fusie zonder voorbehoud vrijgesteld.
>
> **Kernpunt**: De vrijgestelde reserves (bv. spreidings-meerwaarden, herinvesteringsmeerwaarden) moeten in de boeken van de verkrijger geboekt blijven op een onbeschikbare reserverekening, mits de onaantastbaarheidsvoorwaarde van art. 190 WIB92 (geen uitkering, geen vermindering eigen vermogen). Bij niet-naleving worden ze alsnog belast. CBN 2021/10 beschrijft de juiste boekhoudkundige verwerking.
>
> <small>📖 WIB92 — art. 190 + 212 — _wettekst_ · CBN-advies 2021/10 — wedersamenstelling vrijgestelde reserves — _advies_</small>

## Accountant-perspectieven

### Accountant als fiscaal adviseur

_De gecertificeerd accountant is het natuurlijke aanspreekpunt voor de fiscale neutraliteit-toets bij elke geplande herstructurering._

#### 💰 Fiscaal adviseur

##### 👣 Pre-fusie-checklist

**Substantie**: Stap 1: Verifieer of beide vennootschappen binnen- of intra-Europees zijn (art. 211 par. 1). Stap 2: Verifieer dat de continuiteitsregels haalbaar zijn — de verkrijger mag geen waarderingsbreuk doorvoeren. Stap 3: Documenteer zakelijke motivering in een bestuursverslag (art. 183bis). Stap 4: Begroot het verlies aan overdraagbare verliezen (art. 206 par. 2). Stap 5: Bewaar vrijgestelde reserves op de gepaste eigen-vermogensrekeningen. Stap 6: Overweeg ruling-aanvraag bij DVB voor zekerheid over art. 183bis-toets bij twijfelgevallen.

<small>🔗 WIB92 — art. 211 + 183bis + 206 par. 2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Accountant als boekhouder — rollover-boekingen

#### 📒 Boekhouder

##### 👣 Boeken volgens continuiteitsbeginsel

**Substantie**: Bij de verkrijger: neem activa en passiva over tegen boekwaarde van de overdrager. Boek vrijgestelde reserves op de juiste vrijgestelde reserverekening (geen winst, geen kapitaal). Verwerk de oorspronkelijke aanschaffingswaarden en afschrijvingsgrondslagen voort. Vermeld in de toelichting bij de jaarrekening van het fusiejaar de toepassing van het neutraliteitsregime + naam van de overdrager (art. 78 par. 6 KB WVV).

<small>📖 CBN-advies 2021/10 — boekhoudkundige verwerking — _advies_ · KB WVV — art. 3:77 par. 5-6 — _kb_</small>

## Verder lezen (scope-out)

- → Reorganisatie-Sigma als parent-keuzekader → [[reorganisatie]] _(moet-verwijzen)_
- → Fusie als vennootschapsrechtelijke modaliteit → [[fusie]] _(moet-verwijzen)_
- → Splitsing als vennootschapsrechtelijke modaliteit → [[splitsing]] _(moet-verwijzen)_
- → Inbreng-bedrijfstak — verwant fiscaal regime (art. 46 WIB92) → [[inbreng-bedrijfstak-of-algemeenheid]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[reorganisatie]]
### `vereist`
- [[fusie]]
- [[splitsing]]
