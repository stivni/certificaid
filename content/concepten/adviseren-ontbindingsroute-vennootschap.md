---
title: Adviseren over de ontbindingsroute van een vennootschap (vrijwillig, gerechtelijk,
  één-akte, klassiek)
tags:
- concept
- competentie
- po-3-0
linked_anchors:
- 3.0.taak.2
- 3.0.IX
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/adviseren-ontbindingsroute-vennootschap.json
gegenereerd_op: '2026-05-21'
---
# Adviseren over de ontbindingsroute van een vennootschap (vrijwillig, gerechtelijk, één-akte, klassiek) 🔗

Adviesopdracht waarbij de gecertificeerd accountant met de cliënt-aandeelhouder de meest passende route kiest voor het beëindigen van een vennootschap: vrijwillige ontbinding (via algemene vergadering) of gerechtelijke ontbinding (rechtbank), en binnen vrijwillige ontbinding de keuze tussen klassieke vereffening (vereffenaar aangesteld, procedure-traject) of vereffening in één akte (art. 2:80 WVV — versnelde route bij eenvoudig saldo). De keuze heeft fiscale, kostprijs- en doorlooptijdgevolgen.



## In de praktijk

- De eerste vraag van de cliënt is meestal 'hoe snel kan het?' — geef altijd een eerlijk venster en niet de optimistische uitkomst.
- Bij vereffening in één akte: alle passiva moeten effectief op de bankafschriften betaald zijn vóór de algemene vergadering; 'in betaling' of 'gepland' is niet voldoende.
- Liquidatiebonus-belasting wordt vaak onderschat — communiceer expliciet het netto-bedrag dat aandeelhouders ontvangen, niet het brutosaldo.

## Stappen

### 1. Vaststellen van de feitelijke vermogenssituatie

Maak een actuele staat van activa en passiva van de vennootschap op — niet de jaarrekening, maar een snapshot op een recente datum die de werkelijke uitkeerbare positie toont.

**Waarom?** De ontbindingsroute hangt rechtstreeks af van of de vennootschap netto positief, neutraal of negatief is. Een vennootschap met netto negatief eigen vermogen kan niet via vereffening in één akte ontbonden worden — daar is een vereffenaar nodig of zelfs een faillissementsaangifte.

**📥 Input**:
- Boekhouding bijgewerkt → **Balans op recente datum** _(boekhoudkundig-overzicht)_
- Lijst schulden + voorzieningen → **Bestaande + verwachte** _(tabel)_

**📤 Output**:
- Voorlopige staat activa/passiva → **Werkversie** _(boekhoudkundig-overzicht)_

**🛠️ Hoe**:

1. Vraag laatste maandafsluiting of bouw zelf een staat op recente datum.
2. Toets passiva-volledigheid: alle leveranciers, bedrijfsvoorheffing, btw, sociale lasten, lopende fiscale geschillen, pensioenverplichtingen, hangende rechtszaken.
3. Bereken voorlopig saldo na vereffening (activa minus alle passiva minus geschatte vereffeningskosten).
4. Klassificeer: (a) ruim positief, (b) krap positief, (c) breakeven, (d) negatief — elke klasse stuurt naar een andere route.

**Grondslag**: [[staat-van-activa-en-passiva-ontbinding]]; WVV art. 2:71

### 2. Afwegen vrijwillige ontbinding versus alternatief (verkoop, fusie, herstructurering, insolventie)

Toets of ontbinding effectief de meest passende exit is, of dat een alternatief (verkoop aan derde, overdracht aan opvolgers, fusie in moeder, gerechtelijke reorganisatie of faillissement bij insolventie) commercieel of wettelijk verplicht is.

**Waarom?** Ontbinding is een 'definitieve' exit met fiscale gevolgen (liquidatiebonus belastbaar bij aandeelhouders). Soms is een verkoop fiscaal voordeliger (privé-meerwaarde-vrijstelling). Bij insolventie kan ontbinding zelfs verboden zijn — dan faillissementsaangifte verplicht.

**📥 Input**:
- Vermogensanalyse (stap 1) → **Netto-positie** _(boekhoudkundig-overzicht)_
- Drijfveren cliënt → **Pensioen, geen opvolging, mislukking activiteit, herstructurering** _(vrije-tekst)_

**📤 Output**:
- Alternatieven-analyse → **Verkoop vs ontbinding vs fusie vs insolventie** _(tekst-document)_

**🛠️ Hoe**:

1. Als netto-vermogen negatief en geen redding mogelijk: insolventie-triage (zie [[insolventietriage-beslisboom]]) — ontbinding mogelijk niet meer beschikbaar, faillissementsaangifte mogelijk verplicht.
2. Als netto-vermogen positief en cliënt wil cash-out: vergelijk fiscaal verkoop (meerwaarde-belasting privé vs liquidatiebonus belasting 30% roerende voorheffing).
3. Als alleen reden 'geen activiteit meer': vereffening + uitkering liquidatiebonus is meestal de eenvoudigste route.
4. Als opvolging mogelijk: schenking aandelen + voortzetting onder de opvolger.

**Grondslag**: [[ontbinding-vennootschap]]; [[insolventietriage-beslisboom]]; WIB92 art. 269 (roerende voorheffing op liquidatieboni)

> [!warning]- Bij twijfelachtige continuïteit: signaleren-plicht naar bestuur (waarschuwing in continuïteits-toepassing) heeft voorrang op ontbindingsadvies. Niet eerst adviseren te ontbinden terwijl het bestuur eigenlijk continuïteit moet beoordelen.
>
> _Vaak fout gedaan_: Adviseren te ontbinden terwijl voorwaarden voor faillissement vervuld zijn — wettelijk verboden en deontologisch problematisch.

### 3. Vrijwillige ontbinding gekozen: afwegen één-akte versus klassieke procedure

Toets of de vennootschap voldoet aan de drie cumulatieve voorwaarden voor vereffening in één akte (art. 2:80 WVV): geen passief (of alle schulden voldaan vóór de vergadering), alle vennoten/aandeelhouders aanwezig of vertegenwoordigd, unanieme beslissing tot ontbinding en sluiting.

**Waarom?** Vereffening in één akte is sneller (één notariële akte volstaat) en goedkoper (geen vereffenaar, geen tussentijdse verslagen). Maar de drie voorwaarden zijn strikt — bij twijfel over volledigheid passiva of bij dispuut tussen aandeelhouders: klassieke procedure verplicht.

**📥 Input**:
- Aandeelhoudersregister → **Aanwezigheidskans algemene vergadering** _(structuur)_
- Voorlopige staat activa/passiva (stap 1) → **Bevestiging geen openstaand passief** _(boekhoudkundig-overzicht)_

**📤 Output**:
- Route-aanbeveling vereffening → **Eén-akte of klassiek** _(tekst-document)_

**🛠️ Hoe**:

1. Check voorwaarde 1 (geen passief): zorg dat alle leveranciers, fiscus, sociale zekerheid effectief betaald zijn vóór de vergadering — niet als 'in betaling' maar als 'voldaan'.
2. Check voorwaarde 2 (allen aanwezig): is dat realistisch? Bij familieconflicten meestal niet.
3. Check voorwaarde 3 (unanimiteit): bij meerderheidsbeslissing of dispuut → klassiek.
4. Detail in [[vereffening-in-een-akte]] en [[vereffeningsprocedure-klassiek]]; vergelijking in [[klassieke-versus-een-akte-vereffening]].
5. Als één-akte: voorbereid pakket voor notaris (staat activa/passiva + verklaring bestuur + commissaris/accountant-rapport indien vereist).

**Grondslag**: WVV art. 2:80; [[klassieke-versus-een-akte-vereffening]]

### 4. Plannen tijdslijn, kosten en fiscale impact

Stel met de cliënt een tijdslijn op (typisch 2-3 maanden voor één-akte, 6-18 maanden voor klassiek), een kosten-raming (notaris, accountant, eventueel commissaris, vereffenaar-honorarium) en de fiscale impact (liquidatiebonus, vennootschapsbelasting op vereffeningsresultaat).

**Waarom?** Cliënten denken vaak dat 'ontbinding' enkele weken duurt — bij klassieke procedure is dat meestal niet zo. Kosten kunnen tussen € 2.500 (één-akte BV) en € 25.000 (middelgrote NV klassiek) liggen. Fiscale impact: roerende voorheffing 30% op liquidatiebonus is een schok voor aandeelhouders die niet voorbereid zijn.

**📥 Input**:
- Gekozen route (stap 3) → **Eén-akte of klassiek** _(categorie)_
- Geschatte uitkeerbare reserve → **Eigen vermogen − geplaatst kapitaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tijdslijn-tabel + kosten-raming + fiscale impactraming → **Maand voor maand** _(tabel)_

**🛠️ Hoe**:

1. Maak een Gantt-stijl tijdslijn per maand met deliverables: opdrachtbrief, staat activa/passiva, bestuursverslag, vergadering aanstelling vereffenaar, vereffeningstaken, sluiting.
2. Schat kosten per partij (notaris vlak rond € 1.500-3.500 per akte; accountant typisch € 3.000-12.000 voor staat+verslagen+begeleiding).
3. Bereken liquidatiebonus = uit te keren saldo − geplaatst kapitaal (gestort) − eventuele reserves vrijgesteld van VVPRbis-toepassing.
4. Roerende voorheffing 30% op de liquidatiebonus, in te houden bij uitkering — tenzij VVPRbis-tarief 20%/15% van toepassing (zie [[liquidatiebonus]]).

> [!example]- Voorbeeld: Renaat Vermeulen wil zijn 100%-aandeelhouderschap in Tongerse Adviesburo BV ontbinden bij pensioen
> Renaat Vermeulen wil zijn 100%-aandeelhouderschap in Tongerse Adviesburo BV ontbinden bij pensioen. Saldo na vereffening geschat op € 320.000. Geplaatst kapitaal € 18.600. Geen VVPRbis.
>
> 1. **Tijdslijn-keuze** 🧮
>
>    | Route | Doorlooptijd | Kostenraming |
>    |---|---|---:|
>    | Eén-akte | 6-8 weken | € 4.500 |
>    | Klassiek | 6-9 maanden | € 11.000 |
>    
>
> 2. **Liquidatiebonus + voorheffing** 🧮
>
>    Liquidatiebonus      = € 320.000 − € 18.600 = **€ 301.400**
>    Roerende voorheffing = 30% × € 301.400 = **€ 90.420**
>    Netto uitkering      = € 320.000 − € 90.420 = **€ 229.580**
>

**Grondslag**: [[liquidatiebonus]]; WIB92 art. 269; [[vereffeningsprocedure-klassiek]]

### 5. Formaliseren van het advies en next steps

Lever een schriftelijk advies aan cliënt met aanbevolen route, tijdslijn, kosten, fiscale impact en concrete next steps (opdrachtbrieven, contactnamen notaris, planning algemene vergadering).

**Waarom?** Cliënt neemt een beslissing met fiscale en juridische impact op zijn vermogen. Een schriftelijk advies maakt expliciet wat besproken is, vermindert misverstanden en is een element in de zorgvuldigheids-bewijslast bij later geschil.

**📥 Input**:
- Alle voorgaande analyses → **Route, tijdslijn, kosten, fiscaal** _(tekst-document)_

**📤 Output**:
- Adviesnota ontbinding → **Aanbeveling + onderbouwing + tijdslijn + next steps** _(wettelijk-document)_

**🛠️ Hoe**:

1. Max 2 pagina's; aanbeveling in één zin bovenaan.
2. Concrete kalender: 'aandeelhoudersvergadering rond DATUM, notariële akte rond DATUM, sluiting rond DATUM'.
3. Concrete next steps: 'wij verzorgen de staat van activa en passiva, jij regelt de notaris-afspraak'.
4. Laat cliënt formeel akkoord gaan vóór uitvoering start.

**Grondslag**: ITAA-deontologie


## Zie ook

- **Vereist kennis van**: [[ontbinding-vennootschap]]
- **Vereist kennis van**: [[vrijwillige-ontbinding]]
- **Vereist kennis van**: [[gerechtelijke-ontbinding]]
- **Vereist kennis van**: [[vereffening-in-een-akte]]
- **Vereist kennis van**: [[vereffeningsprocedure-klassiek]]
- **Vereist kennis van**: [[klassieke-versus-een-akte-vereffening]]
- **Vereist kennis van**: [[liquidatiebonus]]
- **Vereist kennis van**: [[insolventietriage-beslisboom]]

## Voorbeelden



