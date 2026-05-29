---
title: "Taxatieprocedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.5.I
  - 2.5.II
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/taxatieprocedure.json"
---

_Procedure_ · ook: vestigingsprocedure · vestiging van de aanslag

## Definitie

De taxatieprocedure is de administratieve fase waarin de fiscus, op basis van de aangifte en eventueel onderzoek, het bedrag van de verschuldigde inkomstenbelasting vaststelt en kohier-vatbaar verklaart. Ze omvat drie hoofdsporen: (1) gewone aanslag conform aangifte, (2) aanslag na bericht van wijziging (BvW) wanneer de fiscus van de aangifte afwijkt, en (3) ambtshalve aanslag bij ontbrekende of niet-tijdige aangifte. De procedure wordt federaal geregeld in WIB92 art. 346-352.

<small>📖 WIB92 — art. 346-352 — _wettekst_</small>

## Substantie

Voor de cliënt is de taxatieprocedure het moment waarop de aangifte 'tegengelezen' wordt. De fiscus heeft drie middelen: een vraag om inlichtingen (informeel onderzoek), een bericht van wijziging (formele kennisgeving van een geplande rechtzetting) en — bij niet-meewerken — een ambtshalve aanslag waarbij de bewijslast omkeert. Het bericht van wijziging is hét moment waarop de accountant moet reageren binnen de strikte termijn van 1 maand: zwijgen wordt door de fiscus geïnterpreteerd als instemming.

<small>🔗 WIB92 — art. 346 + art. 351 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De procedure is opgebouwd rond het beginsel van tegensprekelijkheid: de fiscus moet zijn voorgenomen afwijking van de aangifte motiveren en aan de belastingplichtige meedelen (BvW) vóórdat hij de aanslag vestigt. Dit beschermt de belastingplichtige tegen verrassings-taxaties en is een operationalisering van de hoorplicht (audi alteram partem). De ambtshalve aanslag is de sanctie bij niet-meewerken: hij verschuift de bewijslast naar de belastingplichtige.

<small>🔗 WIB92 — art. 346 + art. 352 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 346-352

**▶️ Trigger start**
- 🔗 Ontvangst van de aangifte door de fiscus (of het verstrijken van de aangiftetermijn zonder aangifte) start de taxatieprocedure.

**⏹ Trigger einde**
- 📖 De inkohiering en betekening van het aanslagbiljet eindigt de taxatieprocedure en start de bezwaarperiode.

## Bouwstenen

### ⚙️ Vraag om inlichtingen (VOI)

Informeel onderzoeksinstrument: de fiscus stelt schriftelijke vragen aan de belastingplichtige of aan derden. Antwoordtermijn standaard 1 maand (verlengbaar op gemotiveerd verzoek). Niet of laattijdig antwoorden kan leiden tot ambtshalve aanslag en administratieve boete.

<small>📖 WIB92 — art. 316 + art. 351 — _wettekst_</small>

### ⚙️ Bericht van wijziging (BvW)

Formele kennisgeving waarin de fiscus aankondigt dat hij wil afwijken van de aangifte. Moet gemotiveerd zijn (welke bedragen, op welke gronden). De belastingplichtige heeft een dwingende antwoordtermijn van 1 maand (te rekenen vanaf de derde werkdag na verzending). Pas na het antwoord — of bij stilzitten — wordt de aanslag gevestigd. Een aanslag zonder voorafgaand BvW (waar dat verplicht was) is nietig.

<small>📖 WIB92 — art. 346 — _wettekst_</small>

### ⚙️ Aanslag van ambtswege

Sanctie-aanslag voor wie geen of een onbruikbare aangifte indient, niet antwoordt op vragen om inlichtingen, of weigert mee te werken aan een controle (art. 351 WIB92). De fiscus raamt de inkomsten zelf — vaak forfaitair op basis van tekenen-en-indiciën of vergelijking. Gevolg: de bewijslast keert om. De belastingplichtige moet vervolgens aantonen dat het juiste bedrag lager is (art. 352).

<small>📖 WIB92 — art. 351-352 — _wettekst_</small>

### 📏 Onderzoekstermijn

Standaard 3 jaar vanaf 1 januari van het aanslagjaar. Verlengd tot 6 jaar bij grensoverschrijdende dossiers, tot 10 jaar bij fraude (art. 333 WIB92). De fiscus moet binnen deze termijn de aanslag vestigen — daarna is hij verjaard.

<small>📖 WIB92 — art. 333 + art. 354 — _wettekst_</small>

## Voorbeelden

> [!example]- Aurelia Holding NV — bericht van wijziging op autokostenaftrek
> _Aurelia gaf in aangifte AJ 2025 90.000 EUR autokosten aan (BMW iX). De fiscus stuurt op 12 juni 2026 een BvW: aftrekbeperking volgens werkelijke CO₂ → slechts 60.000 EUR aftrekbaar._
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Antwoordtermijn BvW = 1 maand, niet 6 maanden
> **Verkeerde assumptie**: Op een bericht van wijziging kun je binnen 6 maanden reageren (verwarring met bezwaar).
>
> **Kernpunt**: De antwoordtermijn op een BvW is dwingend 1 maand. Pas op de aanslag zelf is de bezwaartermijn 6 maanden van toepassing. Verschillende fase, verschillende termijn.
>
> <small>📖 WIB92 — art. 346 — _wettekst_</small>

> [!warning]- Ambtshalve aanslag is niet 'pakken wat je krijgt'
> **Verkeerde assumptie**: Bij een ambtshalve aanslag kan de fiscus zomaar willekeurige bedragen vorderen.
>
> **Kernpunt**: Ook een ambtshalve aanslag moet redelijk en gemotiveerd zijn (beginsel van behoorlijk bestuur). Hij mag niet kennelijk onredelijk zijn. De belastingplichtige draagt wel de bewijslast om het juiste bedrag aan te tonen — niet de fiscus.
>
> <small>🔗 WIB92 — art. 352 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Reageren op bericht van wijziging

#### 💰 Fiscaal adviseur

##### 👣 Termijn agenderen + dossier ophalen

Onmiddellijk de antwoorddatum (3e werkdag na verzending + 1 maand) in de agenda zetten. Boekhouding + onderliggende stukken klaarzetten voor het betwiste punt.

<small>🔗 WIB92 — art. 346 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Gemotiveerd antwoord opstellen

Schriftelijk antwoord per aangetekende brief of via MyMinfin/Bizfin. Per voorgenomen rechtzetting: feitelijke + juridische motivering, met verwijzing naar boekstukken en wetsartikelen. Een akkoord kan een bezwaar later bemoeilijken — alleen tekenen wat onbetwistbaar is.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Termijnen detail → [[aanslagtermijnen]] _(moet-verwijzen)_
- → Cyclus-overzicht per aanslagjaar → [[aanslag-cyclus]] _(moet-verwijzen)_
- → Bewijsmiddelen → [[fiscale-bewijsmiddelen]] _(moet-verwijzen)_
- ↪ Behoorlijk bestuur als waarborg → [[beginselen-behoorlijk-bestuur]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
### `vereist`
- [[aanslagtermijnen]]
### `triggert`
- [[aanslag-cyclus]]
