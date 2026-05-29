---
title: "BTW-aangifte"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.taak.4
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-aangifte.json"
---

_Procedure_ · ook: BTW-listing · INTERVAT-aangifte · periodieke aangifte

## Definitie

De BTW-aangifte is de periodieke verklaring waarin de belastingplichtige aan de fiscus rapporteert hoeveel BTW hij in het tijdvak heeft aangerekend op zijn verkopen (uitgaande BTW), hoeveel hij betaald heeft op zijn aankopen (recht op aftrek = inkomende BTW) en welk saldo daaruit volgt — te betalen aan de Staat of terug te vorderen. Ze wordt elektronisch ingediend via INTERVAT, in beginsel maandelijks; kwartaalindiening is mogelijk onder omzetdrempels (zie KB nr. 1 art. 17 §2). Naast de periodieke aangifte bestaan een aantal nevenaangiften: de intracommunautaire opgave (IC-listing) en de jaarlijkse klantenlisting van belastingplichtige Belgische klanten.

<small>📖 WBTW — art. 53 §1, eerste lid, 2° — _wettekst_ · KB nr. 1 — art. 17 §1 — _kb_ · CBN-advies 2010/13 — Algemeen — _cbn_</small>

## Substantie

De aangifte heeft een 'verklaring + afrekening'-functie. Op het voorblad staan roosters waarin de belastingplichtige zijn handelingen per categorie samenvat (uitvoer, intracommunautaire leveringen, binnenlandse leveringen per tarief, …) en de BTW per categorie berekent. Daarnaast geeft hij de aftrekbare BTW aan. Het saldo (rooster 71 = te betalen, rooster 72 = te vorderen) wordt afgerekend via de BTW-rekening-courant: een positief saldo aan de Staat wordt betaald binnen dezelfde termijn als de aangifte; een negatief saldo wordt overgedragen naar de volgende periode of, op verzoek en onder voorwaarden, teruggegeven (KB nr. 24 art. 7 + KB nr. 4).

<small>🔗 WBTW — art. 53 — _wettekst_ · KB nr. 24 — art. 7 — _kb_ · Richtlijn 2006/112/EG — art. 183 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

BTW is een zelfaanslag-belasting: de belastingplichtige berekent zélf zijn verschuldigde BTW en stort die door (zelfafrekening). De periodieke aangifte is het document waarop de Staat én de belastingplichtige hun positie vastleggen. Door verkopen en aankopen tegen elkaar weg te strepen wordt de toegevoegde waarde belast, niet de bruto-omzet. De korte termijnen (20ste / 25ste van de volgende maand) zorgen voor cashflow naar de Staat met beperkte vertraging.

<small>🔗 Richtlijn 2006/112/EG — art. 250-252 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 53 + KB nr. 1 + KB nr. 24

Elektronische aangifte via INTERVAT is verplicht voor alle belastingplichtigen tenzij ze niet over de geïnformatiseerde middelen beschikken (KB nr. 1 + analogie WIB92 art. 307bis). Sinds 2025 zijn de aangifte-modaliteiten verfijnd (KB 2024-09-29/05).

**📋 Voorwaarden**
- 📖 De aangifte moet elektronisch worden ingediend via INTERVAT. Papieren indiening is enkel toegelaten zolang de belastingplichtige of zijn gemachtigde niet over de nodige geïnformatiseerde middelen beschikt (uitzondering wordt smal geïnterpreteerd).

**▶️ Trigger start**
- 🔗 Identificatie als BTW-belastingplichtige (aanvraag BTW-nummer) genereert de aangifteverplichting per tijdvak vanaf de eerste werkdag van de activiteit.

## Sub-concepten

### 📦 Maandaangifte vs kwartaalaangifte

#### Definitie

Het BTW-tijdvak is in beginsel de kalendermaand (KB nr. 1 art. 17 §1). De belastingplichtige mag een kwartaalaangifte indienen wanneer cumulatief: (1) zijn jaaromzet exclusief BTW niet meer bedraagt dan 2.500.000 EUR; (2) jaaromzet ≤ 250.000 EUR voor bepaalde gevoelige producten (energieproducten, mobiele telefonie/computers, landvoertuigen met motor); (3) hij niet maandelijks IC-opgave moet indienen (art. 53sexies §1). Wanneer een drempel overschreden wordt, gaat hij over naar maandaangifte vanaf het eerstvolgende kwartaal.

<small>📖 KB nr. 1 — art. 17 §2 — _kb_ · KB nr. 1 — art. 17 §3 — _kb_</small>

#### Substantie

Voor kleinere onderneming is kwartaal handig: minder administratie en cashflow-voordeel (gemiddeld halve kwartaal-extra-uitstel ten opzichte van maand). Voor grotere belastingplichtigen met BTW-tegoed is maand voordeliger (sneller teruggaaf).

<small>🔗 claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 📏 Drempel 2.500.000 EUR jaaromzet

Algemene drempel: jaaromzet exclusief BTW van de volledige economische activiteit ≤ 2.500.000 EUR. Boven deze drempel: verplicht maandaangifte.

<small>📖 KB nr. 1 — art. 17 §2, 1° — _kb_</small>

#### 📏 Drempel 250.000 EUR — gevoelige sectoren

Specifieke drempel van 250.000 EUR jaaromzet voor leveringen van energieproducten (art. 415 §1 programmawet 27-12-2004), toestellen voor mobiele telefonie en computers (incl. randapparatuur), en landvoertuigen met motor onderworpen aan inschrijvingsreglementering. Deze drempel is veel lager om carrousel-fraude in deze sectoren te beperken.

<small>📖 KB nr. 1 — art. 17 §2, 2° — _kb_</small>

### 📦 Roosters van de BTW-aangifte

#### Definitie

De aangifte is opgebouwd uit roosters die de handelingen per categorie samenvatten. Belangrijke roosters die elke stagiair moet kunnen plaatsen: 00 (vrijgesteld zonder BTW), 01-02-03 (belastbare verkopen aan 6/12/21 %), 44 (intracommunautaire diensten — afnemer is plichtig), 45 (binnenlandse verlegging), 46 (intracommunautaire leveringen vrijgesteld), 47 (uitvoer vrijgesteld), 48 (creditnota's uitgaande), 49 (overige correcties), 54-55-57 (BTW verschuldigd op verkopen / IC-aankopen / IC-diensten), 59 (aftrekbare BTW), 61 (regulariseringen), 62 (overige regulariseringen), 64 (creditnota's binnenkomend), 71 (eindsaldo te betalen) of 72 (te vorderen). De exacte nummering en omschrijving evolueert; raadpleeg de actuele toelichting INTERVAT.

<small>🔗 KB nr. 1 — Bijlage III — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 📏 Indieningstermijn — 20ste / 25ste

Maandaangifte: uiterlijk de 20ste dag van de maand volgend op het tijdvak (KB nr. 1 art. 17 §1). Kwartaalaangifte: uiterlijk de 25ste dag van de maand volgend op het kwartaal (KB nr. 1 art. 17 §2). De Richtlijn 2006/112/EG staat termijnen tot maximaal twee maanden toe (art. 252 §1) — België heeft binnen die marge gekozen voor de strikte korte termijn.

<small>📖 KB nr. 1 — art. 17 §1 — _kb_ · KB nr. 1 — art. 17 §2 — _kb_ · Richtlijn 2006/112/EG — art. 252 — _richtlijn_</small>

### 📜 Correctie materiële vergissing

Stelt de belastingplichtige na indiening een materiële vergissing vast vóór de indieningstermijn verstreken is, dan dient hij een nieuwe aangifte in voor dezelfde periode die de eerste vervangt. Kan dat niet vóór de termijn, dan corrigeert hij in de eerstvolgende aangifte (KB nr. 1 art. 17 §4). 'Materiële vergissing' is een onbedoelde fout of vergetelheid — geen heroverweging van een interpretatieve keuze.

<small>📖 KB nr. 1 — art. 17 §4 — _kb_</small>

### 📜 Sancties laattijdige aangifte

Bij laattijdige indiening loopt de belastingplichtige een administratieve geldboete op (KB nr. 41 — schaalboetes per maand vertraging) en kan de fiscus nalatigheidsinteresten aanrekenen. De exacte boete-tarieven staan in KB nr. 41 en evolueren — raadpleeg het Cijferzakboekje voor de actuele bedragen. Een aangifte van nul EUR is ook verplicht: ontbreekt ze, dan kan een ambtshalve aanslag (art. 66 WBTW) volgen.

<small>🔗 WBTW — art. 66 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### ⚙️ BTW-rekening-courant — saldo te betalen / terug te vorderen

Elk BTW-belastingplichtige heeft een BTW-rekening-courant bij de administratie. Saldi tussen aangifte-perioden worden daar bijgehouden. Saldo in het voordeel van de belastingplichtige (rooster 72) wordt overgedragen naar volgende periode of, op uitdrukkelijk verzoek en onder voorwaarden (KB nr. 4), teruggegeven (KB nr. 24 art. 7). Saldo in het voordeel van de Staat (rooster 71) moet betaald worden binnen dezelfde termijn als de aangifte. Boekhoudkundig (CBN 2010/13): klasse 411 'Terug te vorderen BTW' (debet) versus klasse 451 'Te betalen BTW' (credit).

<small>📖 KB nr. 24 — art. 7 — _kb_ · Richtlijn 2006/112/EG — art. 183 — _richtlijn_ · KB 21-10-2018 (MAR) — Klasse 4 — rekeningen 411 + 451 — _kb_</small>

### 📜 Intracommunautaire opgave (IC-listing)

Naast de periodieke aangifte moet de belastingplichtige die intracommunautaire leveringen of diensten verricht een IC-opgave indienen (BTW-listing). Deel 1 (algemeen overzicht per buitenlandse afnemer) en deel 2 (correcties) worden elektronisch ingediend (KB nr. 50 art. 6 + 12). Termijn: in principe maandelijks (= zelfde tempo als de aangifte voor maandindieners); kwartaal mits drempelvoorwaarden (Richtlijn 2006/112 art. 271). Doel: cross-check tussen lidstaten voor IC-leveringen (VIES-systeem).

<small>📖 WBTW — art. 53sexies — _wettekst_ · KB nr. 50 (2019) — art. 6 — _kb_ · KB nr. 50 (2019) — art. 12 — _kb_ · Richtlijn 2006/112/EG — art. 271 — _richtlijn_</small>

### 📜 Jaarlijkse klantenlisting

Eén keer per jaar (uiterlijk 31 maart) moet de belastingplichtige een lijst indienen van alle Belgische BTW-belastingplichtige afnemers waaraan hij in het voorbije kalenderjaar voor meer dan 250 EUR (excl. BTW) geleverd of gepresteerd heeft. Doel: cross-check met de aftrek die de afnemers claimen — sterke fraude-control.

<small>🔗 WBTW — art. 53quinquies — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Maandaangifte handelsvennootschap — saldo te betalen
> _Zelena Bio NV (algemene belastingplichtige, maandaangifte) heeft in maart 2026: binnenlandse verkopen 100.000 EUR aan 21 % en 20.000 EUR aan 6 %; aankopen 50.000 EUR aan 21 %._
>
> **Berekening:**
>
> - Rooster 03 (verkopen 21 %): 100.000 EUR
> - Rooster 01 (verkopen 6 %): 20.000 EUR
> - Rooster 54 (BTW verschuldigd verkopen): 21.000 + 1.200 = 22.200 EUR
> - Rooster 81 (aankopen handelsgoederen excl. BTW): 50.000 EUR
> - Rooster 59 (aftrekbare BTW aankopen): 10.500 EUR
> - Rooster 71 (saldo te betalen): 22.200 − 10.500 = 11.700 EUR
>
> → **Resultaat**: Te storten op de BTW-rekening-courant uiterlijk 20 april 2026. Geboekt: D 451 'Te betalen BTW' 11.700 / C 550 'Bank' 11.700.
>
> <small>🔗 KB nr. 1 — art. 17 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

> [!example]- Kwartaalaangifte — BTW-tegoed
> _Aurelia Consulting BVBA (jaaromzet 800.000 EUR, kwartaalaangifte) heeft in Q1 2026 grote investeringen gedaan: aankopen 200.000 EUR excl. BTW aan 21 %; verkopen 60.000 EUR aan 21 %._
>
> **Berekening:**
>
> - Rooster 54 (BTW verschuldigd verkopen 21 %): 12.600 EUR
> - Rooster 59 (aftrekbare BTW aankopen 21 %): 42.000 EUR
> - Saldo: 12.600 − 42.000 = −29.400 EUR
> - Rooster 72 (te vorderen): 29.400 EUR
>
> → **Resultaat**: Bij standaard-behandeling: overdracht naar Q2 (rekening-courant-tegoed). Indien Aurelia teruggaaf wenst, moet ze daarvoor een aanvraag invullen — voorwaarden en minimum-drempels in KB nr. 4. Boekhoudkundig: D 411 'Terug te vorderen BTW' 29.400.
>
> <small>🔗 KB nr. 24 — art. 7 — _kb_ · Richtlijn 2006/112/EG — art. 183 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Aangifte vergeten in te dienen wanneer er geen activiteit was
> **Verkeerde assumptie**: 'Geen omzet en geen aankopen → geen aangifte nodig.'
>
> **Kernpunt**: Een nul-aangifte is verplicht. Wie geen aangifte indient, riskeert een ambtshalve aanslag (art. 66 WBTW) waarbij de fiscus zelf een schatting maakt. Voor elke periode moet er een aangifte zijn — ook als alle roosters nul tonen.
>
> <small>📖 WBTW — art. 53 + art. 66 — _wettekst_</small>

> [!warning]- Termijn 20 vs 25 verwisselen tussen maand en kwartaal
> **Verkeerde assumptie**: Studenten onthouden 'de 20ste' als universele BTW-termijn.
>
> **Kernpunt**: Maandaangifte: 20ste. Kwartaalaangifte: 25ste. Verschil 5 dagen — niet triviaal voor planning bij kantoor met veel kwartaal-cliënten (alles op één hoop voor 25 jan/apr/jul/okt). Betalingstermijn loopt synchroon met indieningstermijn.
>
> <small>📖 KB nr. 1 — art. 17 §1 + §2 — _kb_</small>

> [!warning]- BTW-tegoed = automatische teruggaaf
> **Verkeerde assumptie**: Een negatief saldo (rooster 72) wordt vanzelf op de bankrekening gestort.
>
> **Kernpunt**: Default = overdracht naar volgende periode. Teruggaaf moet uitdrukkelijk gevraagd worden (vakje aankruisen) en is onderhevig aan minimum-drempels en kwartaal/maand-regels (KB nr. 4 art. 8). Voor maandindieners gelden ruimere teruggaaf-mogelijkheden dan voor kwartaalindieners.
>
> <small>📖 KB nr. 24 — art. 7 — _kb_ · Richtlijn 2006/112/EG — art. 183 — _richtlijn_</small>

## Accountant-perspectieven

### Kantoor doet de BTW-aangifte voor cliënt

_De accountant die maandelijks of per kwartaal de BTW-aangifte voorbereidt en indient namens zijn cliënt-belastingplichtige._

#### 📒 Boekhouder

##### 👣 Voorbereiding van de aangifte uit de boekhouding

Stappen: (1) afsluiten BTW-rekeningen 411 (terug te vorderen) en 451 (te betalen) van het tijdvak; (2) opmaken BTW-listing per rooster vanuit de BTW-codering op verkoop- en aankoopboekingen; (3) controle: optelling rooster 03 × 21 % = rooster 54-deelbedrag (intern consistentiecheck); (4) verwerken creditnota's (roosters 48/64) en regulariseringen (roosters 61/62); (5) indienen via INTERVAT vóór de 20ste/25ste; (6) overschrijven van het bedrag van rooster 71 vanaf de bankrekening van de cliënt.

<small>🔗 KB nr. 1 — art. 17 — _kb_ · CBN-advies 2010/13 — Algemeen — _cbn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

##### 👣 Boeking van het BTW-saldo

Bij saldo 'te betalen' (rooster 71): de gebundelde BTW-rekeningen worden afgesloten naar 451000 'Te betalen BTW vervallen'. Bij betaling: D 451 / C 550. Bij saldo 'te vorderen' (rooster 72): naar 411000 'Terug te vorderen BTW'. Bij overdracht naar volgende periode blijft het saldo openstaan op 411. Bij effectieve teruggaaf: D 550 / C 411.

<small>📖 KB 21-10-2018 (MAR) — Klasse 4 — rekeningen 411 + 451 — _kb_ · CBN-advies 2010/13 — Boekhoudkundige verwerking BTW — _cbn_</small>

#### 💰 Fiscaal adviseur

##### 🧭 Switch maand ↔ kwartaal — opportuniteit checken

Voor een groeiende cliënt: maand inplannen ruim vóór de omzetdrempel van 2.500.000 EUR wordt geraakt. Voor een cliënt met structureel BTW-tegoed (veel investeringen, export): maand kiezen want maandindieners hebben snellere teruggaaf-mogelijkheden. Bij sectorale fraudegevoeligheid (energie, mobiele telefonie, voertuigen): drempel 250.000 EUR — sneller in maandregime dan vermoed.

<small>🔗 KB nr. 1 — art. 17 §2 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

##### 🧭 Voorkomen van laattijdigheid

Aangifte-deadlines (20/25) zijn hard. Bij verwachte laattijdigheid (bv. wachten op leverancierfactuur die rooster 59 beïnvloedt): liever een aangifte indienen met materiële vergissing en die later corrigeren in de eerstvolgende aangifte (KB nr. 1 art. 17 §4), dan helemaal te laat zijn en boete + ambtshalve aanslag riskeren.

<small>🔗 KB nr. 1 — art. 17 §4 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-controle + regularisatie → [[btw-controle]] _(moet-verwijzen)_
- → BTW-aftrek wordt verrekend in aangifte → [[btw-aftrek]] _(moet-verwijzen)_
- ↪ Fiscale procedure (bezwaar/beroep) → [[fiscale-procedure]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `triggert`
- [[btw-controle]] — Een ingediende aangifte is het primaire object van een latere BTW-controle (cross-check met boekhouding + listings).
### `vereist`
- [[btw-aftrek]] — Aftrekbare BTW (rooster 59) wordt in de aangifte verrekend tegenover verschuldigde BTW (rooster 54).
- [[factuur-btw]] — Aftrekbare BTW vereist regelmatige factuur (art. 3 KB nr. 3).
