---
title: "Aangifteplicht"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - gebeurtenis
ankers:
  - 2.5.I
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/aangifteplicht.json"
---

_Kader_ · ook: fiscale aangifteplicht · aangifteverplichting

## Definitie

De aangifteplicht is de wettelijke verplichting voor elke belastingplichtige om uit eigen beweging, binnen een wettelijke termijn en in een voorgeschreven vorm, de elementen aan te geven die nodig zijn om de belasting te kunnen vestigen. Voor de inkomstenbelasting steunt deze plicht op artikel 305 WIB92: 'belastingplichtigen aan de personenbelasting, de vennootschapsbelasting, de rechtspersonenbelasting en de belasting van niet-inwoners ... zijn ertoe gehouden ieder jaar aan de administratie ... een aangifte over te leggen'. Voor btw geldt art. 53 §1 WBTW (periodieke aangifte).

<small>📖 WIB92 — art. 305 — _wettekst_ · WBTW — art. 53 §1 — _wettekst_</small>

## Substantie

De aangifteplicht is de hoeksteen van het Belgisch fiscaal stelsel: de fiscus heft niet uit eigen beweging, maar op basis van wat de belastingplichtige meedeelt. Voor de stagiair betekent dit: tijdig en volledig aangeven is de eerste fiscale plicht van elke cliënt. Niet-aangeven of laattijdig aangeven activeert escalerende mechanismes — aanslag van ambtswege (art. 351 WIB92, fiscus raamt zelf op basis van beschikbare info), belastingverhogingen (art. 444 WIB92, tot 200 %), administratieve geldboetes (art. 445 WIB92), en bij fraude ook strafrechtelijke vervolging (art. 449 WIB92).

<small>🔗 WIB92 — art. 351 — _wettekst_ · WIB92 — art. 444 — _wettekst_ · WIB92 — art. 305 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het Belgisch belastingstelsel is een aangifte-stelsel: efficiënt omdat de overheid niet elke belastingplichtige individueel hoeft te controleren, maar steunt op de medewerkingsplicht van de burger. De wetgever maakt deze plicht effectief door duidelijke termijnen, voorgeschreven formulieren en stevige sancties bij niet-naleving.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 305 (inkomstenbelasting); WBTW art. 53 (btw)

Indienings-termijnen + vormen evolueren jaarlijks (vooral Tax-on-Web-deadlines). Wet stabiel.

**✅ Voor**
- 📖 Elke belastingplichtige onderworpen aan inkomstenbelasting, btw, registratierechten, successierechten of een lokale belasting waarvoor het reglement een aangifte voorziet.

**▶️ Trigger start**
- 🔗 PB: ontvangst van het aangifteformulier (of voorstel van vereenvoudigde aangifte) door de FOD Financiën, doorgaans in mei van het aanslagjaar. VenB: einde boekjaar. Btw: einde aangifteperiode (maand of kwartaal).

**⚠️ Risico**
- 📖 Niet-aangeven of laattijdig aangeven: aanslag van ambtswege (fiscus raamt zelf op basis van beschikbare gegevens, art. 351 WIB92) + belastingverhoging tot 200 % (art. 444 WIB92 + KB/WIB92 art. 225-226) + administratieve geldboete (art. 445 WIB92). Bij opzet/fraude: verlengde aanslagtermijn (10 jaar art. 354 WIB92) + strafrechtelijke vervolging (art. 449 WIB92).

## Bouwstenen

### 📜 Wie moet aangifte indienen

Per belasting verschillend. Inkomstenbelasting (art. 305 WIB92): alle rijksinwoners onderworpen aan PB, alle vennootschappen onderworpen aan VenB, alle rechtspersonen onderworpen aan RPB, alle niet-inwoners met Belgische bron (BNI). Btw (art. 53 §1 WBTW): elke btw-belastingplichtige met periodieke aangifte (kwartaal of maand). Successierechten: de erfgenamen, legatarissen of begunstigden binnen 4 maanden na overlijden (Vlaams Gewest: art. 3.3.1.0.5 VCF). Registratierechten: in beginsel automatisch via de notariële akte, geen aparte aangifte. Lokale belastingen: volgens belastingreglement.

<small>📖 WIB92 — art. 305 — _wettekst_ · WBTW — art. 53 §1 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 3.3.1.0.5 — _wettekst_</small>

### 📜 Wat moet aangegeven worden

Inkomstenbelasting: alle belastbare inkomsten (beroeps-, onroerend, roerend, divers) + aftrekken + gezinslast + voorheffingen + buitenlandse rekeningen + juridische constructies. De aangifte volgt het aangifteformulier (deel 1 en deel 2 PB; aangifte 275.1 VenB; aangifte 276.5 BNI). Btw: belastbare handelingen, btw geheven van klanten (rooster 54/61), aftrekbare btw (rooster 59), verschuldigde of terug te vorderen saldo. Successierechten: alle goederen van de nalatenschap, schulden, eventuele schenkingen tijdens de drie jaren vóór overlijden.

<small>📖 WIB92 — art. 307 — _wettekst_ · WBTW — art. 53 §1 — 2° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📏 Wanneer indienen (termijnen)

PB-papier: 30 juni aanslagjaar (richtlijn). PB-Tax-on-Web: medio juli aanslagjaar (richtlijn, jaarlijks aangekondigd). PB via cijferberoeper (mandataris): eind oktober aanslagjaar (richtlijn). VenB (Biztax): binnen de termijn vermeld op het formulier, doorgaans tussen 1 en 4 maanden na de algemene vergadering die de jaarrekening goedkeurde, maar nooit later dan 6 maanden na het einde van het belastbaar tijdperk. Btw (Intervat): 20e van de maand volgend op het aangiftetijdperk; jaarlijkse opgave van btw-belastingplichtige klanten (klantenlisting): 31 maart. Erfbelasting: 4 maanden na overlijden (overlijden in België; 5 maanden bij Europees overlijden, 6 maanden bij overzee). Exacte termijnen: jaarlijks raadplegen — Cijferzakboekje bij examen.

<small>🔗 WIB92 — art. 308 — _wettekst_ · WBTW — art. 53 §1 — 2° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Vorm van de aangifte

PB: voorbedrukt papieren formulier (uitdovend) of elektronisch via MyMinFin / Tax-on-Web (verplicht voor mandatarissen). VenB: verplicht elektronisch via Biztax. Btw: verplicht elektronisch via Intervat (uitzondering: ondernemingen die geen pc-toegang hebben). Successierechten Vlaams Gewest: papier of elektronisch via MyVlaanderen. Voor mandatarissen (cijferberoepers): verplicht elektronisch. Een papieren aangifte die elektronisch had gemoeten = geldige aangifte aanvaard, maar in toekomst beboetbaar volgens jurisprudentie en administratieve commentaar.

<small>🔗 WIB92 — art. 307bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Voorstel van vereenvoudigde aangifte (PB)

De FOD Financiën stuurt aan eenvoudige belastingplichtigen (loontrekkenden zonder bijkomende inkomsten, gepensioneerden, ...) een voorstel van vereenvoudigde aangifte. Reageert de belastingplichtige niet binnen de termijn (zelfde als gewone aangifte), dan geldt het voorstel als de definitieve aangifte. Reageert hij wel (wijzigingen of aanvullingen), dan vervangt zijn correctie het voorstel. Praktisch: voor stagiair-accountants beperken vereenvoudigde aangiften de werkdruk, maar verdient elk voorstel een snelle controle (vergeten aftrekken, fout kadastraal inkomen, ...).

<small>📖 WIB92 — art. 306 — _wettekst_</small>

### ⚠️ Gevolgen van niet-naleving

Cumulatieve mechanismes activeren bij niet-aangeven, laattijdige aangifte of onvolledige aangifte. (1) Aanslag van ambtswege (art. 351 WIB92): de fiscus raamt zelf en de bewijslast om die raming te weerleggen komt op de belastingplichtige. (2) Belastingverhoging (art. 444 WIB92 + KB/WIB92 art. 225-226): graad afhankelijk van overtreding — 10 % bij eerste overtreding zonder kwade trouw tot 200 % bij herhaalde fraude. (3) Administratieve geldboete (art. 445 WIB92): 50 tot 1.250 EUR per overtreding. (4) Verlengde aanslagtermijn bij niet-aangifte (5 jaar) of fraude (10 jaar) (art. 354 WIB92). (5) Strafrechtelijke vervolging bij opzet/valsheid (art. 449 e.v. WIB92).

<small>📖 WIB92 — art. 351 — _wettekst_ · WIB92 — art. 354 — _wettekst_ · WIB92 — art. 444 — _wettekst_ · WIB92 — art. 445 — _wettekst_ · WIB92 — art. 449 — _wettekst_</small>

## Valkuilen

> [!warning]- Uitstel = automatisch geen sanctie
> **Verkeerde assumptie**: Studenten denken dat indien de FOD Financiën een algemeen uitstel verleent, alle laattijdige aangiften zonder gevolg blijven.
>
> **Kernpunt**: Algemene uitstellen (vaak gepubliceerd door de minister) verschuiven de officiële deadline. Wie ook na de uitgestelde deadline indient, valt opnieuw onder de sanctieregeling. Een individueel uitstel moet vooraf aangevraagd en bevestigd worden.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vereenvoudigde aangifte = niets doen
> **Verkeerde assumptie**: Het volstaat om het voorstel van vereenvoudigde aangifte te negeren — de fiscus regelt het wel.
>
> **Kernpunt**: Bij ongewijzigd voorstel geldt dit inderdaad als aangifte. Maar bevat het voorstel fouten (vergeten kinderlast, fout KI, fout pensioenbedrag), dan is de belastingplichtige bij stilzwijgen verantwoordelijk voor de onjuiste aanslag. Steeds nakijken.
>
> <small>🔗 WIB92 — art. 306 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Sancties bij niet-naleving → [[fiscale-sancties]] _(moet-verwijzen)_
- → Aanslag-cyclus na aangifte → [[aanslag-cyclus]] _(moet-verwijzen)_
- ↪ PB-specifieke aangifte → [[aangifte-pb]] _(mag-verwijzen)_
- ↪ VenB-specifieke aangifte → [[aangifte-vennootschapsbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
### `triggert`
- [[aanslag-cyclus]]
