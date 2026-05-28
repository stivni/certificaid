---
title: "Bezwaarprocedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.5.V
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/bezwaarprocedure.json"
---

# Bezwaarprocedure

_Procedure_

📅 Gebeurtenis · Anchors: `2.5.V` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: administratief beroep · bezwaar tegen aanslag — **Vertalingen**: fr: réclamation

## Definitie

📖 De bezwaarprocedure is het verplicht administratief beroep tegen een gevestigde inkomstenbelastingaanslag (WIB92 art. 366). De belastingplichtige dient binnen 6 maanden — vanaf de 1e dag van de derde maand na verzending van het aanslagbiljet — een gemotiveerd bezwaarschrift in bij de adviseur-generaal van de bevoegde gewestelijke directie. De directeur beslist (zonder dwingende beslistermijn) en die beslissing is voorwaarde om naar de rechtbank te kunnen.

<small>📚 WIB92 — art. 366-376 — _wettekst_</small>

## Substantie

🔗 Praktisch is bezwaar dé hefboom van de accountant: het is gratis, schriftelijk, en biedt de cliënt een tweede kans om feiten en argumenten naar voren te brengen die in de taxatiefase onvoldoende aan bod kwamen. Het bezwaar mag nieuwe grieven bevatten zolang de aanslag wordt betwist. De directeur kan de aanslag vernietigen, verminderen, of bevestigen — maar mag de aanslag niet verhogen (reformatio in pejus is verboden).

<small>📚 WIB92 — art. 375 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het bezwaar is een verplichte zeef vóór de rechter: het ontlast de rechtbanken en geeft de fiscus de kans haar eigen fout te corrigeren. Het is ook een waarborg voor de belastingplichtige (geen extra kosten, geen advocatenplicht). De 6-maand-termijn is van openbare orde — wie te laat is, verliest definitief het recht op betwisting (behoudens ambtshalve ontheffing art. 376 voor materiële vergissingen).

<small>📚 WIB92 — art. 371 + art. 376 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 366-376

**📋 Voorwaarden**
- 📖 (1) Er moet een gevestigde aanslag bestaan; (2) bezwaar wordt schriftelijk ingediend, gemotiveerd, en ondertekend door de belastingplichtige of zijn lasthebber; (3) bij de bevoegde adviseur-generaal (gewestelijke directie); (4) binnen de wettelijke termijn van 6 maanden.

**▶️ Trigger start**
- 📖 Verzending van het aanslagbiljet (datum vermeld op het biljet zelf) start de bezwaartermijn-klok — de termijn loopt vanaf de 1e dag van de derde maand erop.

**⏹ Trigger einde**
- 📖 Kennisgeving van de directeursbeslissing (of het verstrijken van 6 maanden zonder beslissing — fictieve afwijzing waarbij de belastingplichtige direct naar de rechter kan).

## Bouwstenen

### 📏 Termijn van 6 maanden  
_`drempel`_

📖 Het bezwaar moet zijn ingediend binnen 6 maanden vanaf de 1e dag van de derde maand die volgt op de verzending van het aanslagbiljet (art. 371 WIB92). Voorbeeld: aanslagbiljet verzonden 15 april 2026 → termijn loopt vanaf 1 juli 2026 → einddatum = 31 december 2026. Termijn is van openbare orde: niet-verlengbaar, niet-vatbaar voor herstel (behoudens overmacht).

<small>📚 WIB92 — art. 371 — _wettekst_</small>

### 📜 Vorm en inhoud van het bezwaarschrift  
_`regel`_

📖 Schriftelijk, ondertekend, gemotiveerd. Vermelding van: identificatie aanslag (artikel, aanslagjaar, kohier-nr), grieven (feitelijk + juridisch), gevorderd resultaat (vernietiging/vermindering). Indienen per aangetekende brief of via MyMinfin/Bizfin. Geen formulier verplicht. Een onvolledig of niet-ondertekend bezwaar is onontvankelijk.

<small>📚 WIB92 — art. 366 + art. 372 — _wettekst_</small>

### 👣 Beslissing door de directeur  
_`stap`_

📖 De adviseur-generaal (of zijn gemachtigde ambtenaar) onderzoekt het bezwaar. Hij kan vragen om bijkomende inlichtingen of stukken. Hij kan de aanslag vernietigen, verminderen of bevestigen. Hij kan de aanslag NIET verhogen (verbod reformatio in pejus, art. 375 WIB92). De beslissing wordt schriftelijk en gemotiveerd betekend.

<small>📚 WIB92 — art. 374-375 — _wettekst_</small>

### ↪️ Ambtshalve ontheffing (art. 376)  
_`uitzondering`_

📖 Verlengde betwistingsmogelijkheid voor materiële vergissingen, dubbele belasting, of nieuwe bewijsmiddelen die de belastingplichtige niet kende: 5 jaar vanaf 1 januari van het aanslagjaar (art. 376 WIB92). Dit is geen bezwaar maar een verzoek tot ambtshalve ontheffing aan de adviseur-generaal. Beperkter dan bezwaar: alleen voor materiële vergissingen, niet voor juridische geschillen.

<small>📚 WIB92 — art. 376 — _wettekst_</small>

## Valkuilen

### ⚠️ Termijn begint NIET bij datum aanslagbiljet

**Verkeerde assumptie**: De 6 maanden lopen vanaf de datum op het aanslagbiljet of vanaf ontvangst.

**Kernpunt**: Termijn begint op de 1e dag van de derde maand die volgt op de verzendingsdatum. Vergrendel deze datum altijd dubbel in de agenda.

<small>📚 WIB92 — art. 371 — _wettekst_</small>

### ⚠️ Bezwaar schorst niet automatisch invordering

**Verkeerde assumptie**: Tijdens een lopend bezwaar moet de cliënt niets betalen.

**Kernpunt**: Het 'onbetwist verschuldigd deel' blijft onmiddellijk opeisbaar. Voor het betwiste deel kan de ontvanger bewarend beslag leggen. Adviseer cliënten te betalen onder voorbehoud bij grote bedragen, om beslag te vermijden.

<small>📚 WIB92 — art. 409-410 — _wettekst_</small>

### ⚠️ Reformatio in pejus is verboden — wel binnen het bezwaarvoorwerp

**Verkeerde assumptie**: De directeur kan tijdens het bezwaar nieuwe rechtzettingen vinden en de aanslag verhogen.

**Kernpunt**: De directeur mag de aanslag niet verhogen voor het deel waarover bezwaar werd ingediend (art. 375). Voor andere belastingelementen kan de fiscus wel een aanvullende aanslag vestigen binnen de algemene onderzoekstermijn.

<small>📚 WIB92 — art. 375 — _wettekst_</small>

## Syntheses

### 🧩 Synthese  
_`tijdslijn`_

Berekening bezwaartermijn aan de hand van een aanslagbiljet.

## Accountant-perspectieven

### Bezwaarschrift opstellen voor de cliënt

#### 💰 Fiscaal adviseur

##### 👣 Termijn-screening  
_`stap`_

🔗 Eerste actie bij ontvangst aanslagbiljet: bereken de bezwaartermijn (1e dag 3e maand + 6 maanden) en zet deze in de agenda — bij voorkeur met 1 maand veiligheidsmarge.

<small>📚 WIB92 — art. 371 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Grieven structureren  
_`stap`_

🔗 Identificeer per betwist element: (a) feitelijke grief (waar zit de fout?), (b) juridische grond (welke wetsbepaling/CBN-advies/rechtspraak?), (c) gevorderd resultaat in euro's. Houd het bezwaarvoorwerp ruim om later geen grieven verloren te zien gaan voor de rechter.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Indienen + opvolging  
_`stap`_

📖 Indienen per aangetekend schrijven (bewijs van verzending) of via MyMinfin/Bizfin. Bij stilzitten directeur > 6 maanden: overweeg overstap naar rechtbank (Ger.W. art. 1385undecies) of FBD-bemiddeling.

<small>📚 WIB92 — art. 366 — _wettekst_ · Ger.W. — art. 1385undecies — _wettekst_</small>

## Verder lezen (scope-out)

- → Gerechtelijke fase na afwijzing bezwaar → [[gerechtelijke-fase-belasting]] _(moet-verwijzen)_
- → Bemiddeling als parallelle weg → [[fiscale-bemiddelingsprocedure]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
### `triggert`
- [[gerechtelijke-fase-belasting]]
### `vergelijkbaar_met`
- [[fiscale-bemiddelingsprocedure]]
