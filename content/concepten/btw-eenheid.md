---
title: "BTW-eenheid"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 2.4.III
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-eenheid.json"
---

_Regime_ · afk: **BTW-E** · ook: groepsbtw · VAT group · btw-groep

## Definitie

De btw-eenheid is een keuzeregime (art. 4 § 2 W.BTW + KB nr. 55) waarbij meerdere in België gevestigde belastingplichtigen die juridisch onafhankelijk zijn maar financieel, organisatorisch én economisch nauw met elkaar verbonden zijn, voor de toepassing van het btw-wetboek als één belastingplichtige worden behandeld. De groep krijgt één uniek btw-nummer, één periodieke btw-aangifte ingediend door een aangeduide vertegenwoordiger, en de onderlinge leveringen tussen de leden vallen buiten het toepassingsgebied van de btw (geen btw aanrekenen tussen leden onderling). De leden blijven hoofdelijk aansprakelijk voor alle btw-schulden van de eenheid tegenover de Staat.

<small>📖 W.BTW — art. 4 § 2 — _wettekst_ · KB nr. 55 — art. 1 § 1-3 — _kb_ · CBN-advies — 2010/13 — _cbn_</small>

## Substantie

Economisch effect: een groep verbonden vennootschappen die intern veel onderlinge prestaties uitwisselt (managementdiensten, IT-shared services, doorbelastingen) wordt verlost van de cash-flow- en administratielast van btw op die interne stromen. Vooral cruciaal als één van de leden een vrijgestelde activiteit verricht (bank, ziekenhuis, vzw): zonder btw-eenheid zou hij btw moeten betalen op interne dienstprestaties en die niet kunnen recupereren — een verborgen kost in een verbonden groep. Met btw-eenheid: die interne stromen verdwijnen voor btw, en de groep heft alleen btw aan externe klanten en recupereert alleen btw van externe leveranciers, met één gezamenlijke aftrek-pro-rata-toepassing.

<small>🔗 CBN-advies — 2010/13 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Ratio legis: economisch gezien is een verbonden groep één onderneming — de interne verschuivingen zijn 'geen echte handel' maar interne organisatie. De btw als consumptiebelasting hoort die intra-groep-stromen niet te belasten. De Europese btw-richtlijn (art. 11) laat de lidstaten toe een btw-groep in te voeren; België deed dat in 2007 (KB nr. 55, 9 maart 2007) om concurrentieneutraliteit met andere lidstaten (Nederland, Duitsland, Frankrijk) te waarborgen. De drie cumulatieve verbondenheidscriteria (financieel, organisatorisch, economisch) zorgen ervoor dat enkel feitelijke economische groepen kwalificeren — niet louter contractuele samenwerkingen.

<small>🔗 BTW-richtlijn 2006/112/EG — art. 11 — _wettekst_ · KB nr. 55 — art. 1 § 1 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2007-04-01** · basis: W.BTW art. 4 § 2 + KB nr. 55 (9 maart 2007)

Ingevoerd op 1 april 2007. Stabiel regime; periodieke verfijning via administratieve circulaires.

**✅ Voor**
- 🔗 Groepen verbonden vennootschappen die intern veel onderlinge dienstprestaties of leveringen hebben — vooral wanneer minstens één lid een (deels) vrijgestelde activiteit verricht (bank, verzekeraar, ziekenhuis, vzw). De btw-eenheid elimineert dan de niet-aftrekbare btw op interne stromen.

**📋 Voorwaarden**
- 📖 Cumulatief (art. 1 KB nr. 55): (1) financieel nauw verbonden — vermoeden bij directe of indirecte controleverhouding, automatisch bij deelneming >50 %; (2) organisatorisch nauw verbonden — gemeenschappelijke leiding, gezamenlijk overleg of gemeenschappelijke controle door één persoon; (3) economisch nauw verbonden — gelijksoortige activiteit, complementaire activiteit of activiteit die geheel/gedeeltelijk ten behoeve van de anderen wordt uitgeoefend. Alle drie moeten vervuld zijn; missen één criterium volstaat om de eenheid te weigeren.
- 📖 Gemotiveerd verzoek door de vertegenwoordiger bij het bevoegde btw-controlekantoor. De administratie heeft één maand om te beslissen; bij geen reactie of positieve beslissing wordt de btw-eenheid aangemerkt als één belastingplichtige vanaf de eerste dag van de maand volgend op het verstrijken van de termijn (art. 2 § 4 KB nr. 55).
- 📖 Minimumduur: de optie geldt minstens tot en met 31 december van het derde jaar volgend op de aanvang van de btw-eenheid (art. 2 § 1 KB nr. 55). Drie-jaars-lock-in - niet zomaar tussentijds uitstappen.

**⛔ Uitsluitingen**
- 📖 Enkel in België gevestigde belastingplichtigen kunnen lid zijn (art. 4 § 2 W.BTW + art. 1 § 1 KB nr. 55). Buitenlandse vaste inrichtingen van een Belgische groepsvennootschap zitten niet in de eenheid; cross-border btw-groepen bestaan niet.
- 📖 Een belastingplichtige kan maar lid zijn van één enkele btw-eenheid (art. 1 § 4 KB nr. 55). Bij verwerving van een meerderheidsdeelneming in een lid van een andere btw-eenheid, schuift dat lid mee over naar de eenheid van de nieuwe controlerende vennootschap.

**👍 Voordeel**
- 🔗 Eliminatie van btw op onderlinge prestaties: factor 21 % cash-flow- en (indien lid vrijgesteld) definitieve kost-eliminatie. Eén btw-aangifte voor de hele groep: minder administratie. Bij gemengde activiteiten: één aftrek-pro-rata op groepsniveau in plaats van per lid, met optimalisatie van werkelijk gebruik.

**⚠️ Risico**
- 📖 Hoofdelijke aansprakelijkheid: elk lid is hoofdelijk aansprakelijk voor alle btw-schulden van de eenheid tegenover de Staat (art. 51bis § 4 W.BTW + CBN 2010/13). Een sterk gezond lid kan zo aansprakelijk worden voor btw-schulden ontstaan in een ander, in moeilijkheden verkerend, lid.
- 🔗 Herziening bedrijfsmiddelen bij toetreding/uittreding: investeringsgoederen die zich nog in de herzieningsperiode (5 of 15 jaar) bevinden, kunnen aanleiding geven tot positieve of negatieve herzieningen wanneer een lid de eenheid binnenkomt of verlaat (zie btw-herziening-bedrijfsmiddelen). Vereist becijfering vóór toetreding.

## Bouwstenen

### 📜 Drie cumulatieve verbondenheidscriteria

Art. 1 § 1 KB nr. 55 vereist cumulatief: (1) financiële verbondenheid - minstens rechtstreekse of onrechtstreekse controleverhouding; deelneming >50 % geldt als bewezen vermoeden (§ 2); (2) organisatorische verbondenheid - gemeenschappelijke leiding, gezamenlijk werkoverleg, of controle door één persoon; (3) economische verbondenheid - gelijksoortige of complementaire activiteiten, of activiteit ten behoeve van de andere leden. Eén criterium ontbreken = geen btw-eenheid mogelijk, tenzij weerlegging van het 50 %-vermoeden lukt.

<small>📖 KB nr. 55 — art. 1 § 1, 1°-3° — _kb_ · KB nr. 55 — art. 1 § 2 — _kb_</small>

### 💡 Vertegenwoordiger van de btw-eenheid

De leden duiden één van hen aan als vertegenwoordiger (art. 1 § 3 KB nr. 55). Hij houdt een gecentraliseerde btw-boekhouding, dient de periodieke btw-aangifte in onder het btw-identificatienummer van de eenheid, en is het aanspreekpunt voor de btw-administratie (controles, verzoeken, kennisgevingen). De vertegenwoordiger handelt 'in naam en voor rekening van' alle leden - een soort fiscaal mandaathouder binnen de groep. Vaak is dit de moedervennootschap of de hoofdactieve vennootschap.

<small>📖 KB nr. 55 — art. 1 § 3, derde lid — _kb_ · CBN-advies — 2010/13 — _cbn_</small>

### ⚙️ Onderlinge prestaties buiten btw-toepassingsgebied

Het kern-effect: leveringen van goederen en diensten tussen leden van een btw-eenheid vallen niet onder het btw-toepassingsgebied (CBN 2010/13). Er wordt géén btw aangerekend en géén btw afgetrokken op interne facturen. De interne factuur is een 'pro forma' boekhoudkundig document - voor btw-doeleinden bestaat ze niet. Externe leveringen (door één lid aan een derde) en externe aankopen (door één lid van een derde) worden wel verwerkt, maar dan in de geconsolideerde btw-aangifte van de eenheid.

<small>📖 CBN-advies — 2010/13 — _cbn_</small>

### ⚠️ Hoofdelijke aansprakelijkheid van de leden

Tegenover de Staat zijn alle leden hoofdelijk aansprakelijk voor alle btw-schulden van de eenheid (art. 51bis § 4 W.BTW). De fiscus kan dus elke individuele lid aanspreken voor de volledige btw-schuld, ongeacht welke handeling die schuld heeft veroorzaakt. Tussen de leden onderling regelen ze de verdeelsleutel via privaatrechtelijke overeenkomsten (groepscharter, kostenverdeling), maar dat is niet tegenstelbaar aan de fiscus.

<small>📖 W.BTW — art. 51bis § 4 — _wettekst_</small>

### 📏 Drie-jaar-lock-in en in/uittreding

De optie geldt minstens tot en met 31 december van het derde jaar volgend op de aanvang (art. 2 § 1 + art. 4 § 1 KB nr. 55). Een nieuw lid dat na de aanvang toetreedt, is daarna ook gebonden tot 31 december van het derde jaar volgend op zijn toetreding. Het '>50 %-deelneming = automatisch lid'-vermoeden (art. 1 § 2) maakt vrijwillig uittreden van controlemeerderheden moeilijk: bij verkoop van een dochter <50 % vervalt het automatisme.

<small>📖 KB nr. 55 — art. 2 § 1 — _kb_ · KB nr. 55 — art. 4 § 1 — _kb_</small>

### 💡 Sub-btw-nummer per lid

Naast het unieke btw-identificatienummer van de eenheid behoudt elk lid een sub-btw-identificatienummer (art. 50 § 1 lid 1 6° W.BTW). Op de facturen die het lid uitreikt aan derden vermeldt het uitsluitend dat sub-btw-nummer (art. 30 KB nr. 1). Het sub-nummer dient om de externe handeling te lokaliseren bij het juiste lid voor controle-doeleinden - terwijl de aangifte zelf op niveau van de eenheid gebeurt.

<small>📖 W.BTW — art. 50 § 1, eerste lid, 6° — _wettekst_ · KB nr. 1 — art. 30, tweede lid — _kb_</small>

## Voorbeelden

> [!example]- Aurelia Group — IT-shared-services tussen moeder en dochter
> _Aurelia Holding NV bezit 100 % van Aurelia Operations NV. De holding centraliseert IT-infrastructuur en factureert jaarlijks 200.000 EUR managementdiensten aan de operationele vennootschap. Operations heeft een gemengde activiteit (deels btw-vrijgestelde verzekeringsdiensten — 60 %)._
>
> **Berekening:**
>
> - Stap 1 — situatie ZONDER btw-eenheid: holding factureert 200.000 + 42.000 btw (21 %) aan operations. Operations is gemengd belastingplichtige met 40 % aftrek -> kan slechts 16.800 EUR aftrekken. Verlies: 25.200 EUR btw die niet-aftrekbaar is en definitieve kost wordt in de groep.
> - Stap 2 — situatie MET btw-eenheid: factuur 200.000 EUR (geen btw, intra-eenheid). Geen btw aangerekend, geen aftrek nodig. Besparing: 25.200 EUR per jaar.
> - Stap 3 — voorwaarden check: financiële verbondenheid (100 % deelneming) OK; organisatorische (gemeenschappelijke leiding) OK; economische (holding-management ten behoeve van operations) OK. Btw-eenheid kan opgericht worden.
> - Stap 4 — beslissing: oprichting btw-eenheid 'Aurelia Group BTW-E' met holding als vertegenwoordiger. Verzoek bij btw-controle. Drie-jaars-lock-in start vanaf eerste dag maand volgend op stilzwijgende of expliciete goedkeuring.
>
> → **Resultaat**: Jaarlijkse besparing 25.200 EUR niet-aftrekbare btw, in ruil voor administratieve consolidatie en hoofdelijke aansprakelijkheid. Voor een Belgische groep met gemengde dochter is dit vaak een no-brainer.
>
> <small>🔗 KB nr. 55 — art. 1 — _kb_ · CBN-advies — 2010/13 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Zelena Vastgoed — herziening bij uittreding
> _Zelena Vastgoed NV is sinds 2019 lid van btw-eenheid Zelena Group BTW-E. In 2019 heeft Zelena een nieuw kantoorgebouw aangekocht (1.000.000 EUR + 210.000 EUR btw). De volledige btw is afgetrokken (Zelena gebruikte het gebouw voor belaste verhuur op groepsniveau). In 2026 wordt Zelena Vastgoed verkocht aan een externe groep en verlaat de btw-eenheid._
>
> **Berekening:**
>
> - Stap 1 — herzieningsperiode voor onroerend goed = 15 jaar (art. 9 KB nr. 3). Aankoop 2019, uittreding 2026: verstreken 7 jaar, resterend 8 jaar.
> - Stap 2 — bij uittreding wordt herzien als de bestemming wijzigt. Als Zelena Vastgoed na verkoop niet meer voor btw-belaste handelingen wordt gebruikt: positieve herziening = 8/15 x 210.000 = 112.000 EUR aan de Staat terug te storten.
> - Stap 3 — wie betaalt? Hoofdelijk de btw-eenheid (= de groep) ten tijde van uittreding, maar contractueel wordt dit typisch doorgerekend aan de uittredende vennootschap of geregeld in de verkoopovereenkomst.
> - Stap 4 — alternatief: als de koper Zelena Vastgoed voortzet voor btw-belaste handelingen en de overdracht kwalificeert als 'overdracht algemeenheid' (art. 11 W.BTW), kan herziening achterwege blijven.
>
> → **Resultaat**: Btw-eenheid lijkt eenvoudig 'in/uit' maar herzieningsmechaniek voor recente investeringen kan grote bedragen oproepen. Becijferen vóór uittreding (M&A-due-diligence).
>
> <small>🔗 W.BTW — art. 48 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Drie criteria vergeten — vermoeden bij 50 %+ is geen volwaardige test
> **Verkeerde assumptie**: Als de holding >50 % bezit, voldoet ze automatisch — geen verdere check nodig.
>
> **Kernpunt**: Art. 1 § 2 KB nr. 55 maakt enkel een vermoeden van vervulling. De partijen kunnen alsnog aantonen dat ze 'organisatorisch, economisch of omwille van andere omstandigheden niet met elkaar verbonden zijn'. Belangrijk: bij financiële holdings die enkel aandelen aanhouden zonder operationeel betrokken te zijn, kan de economische verbondenheid worden betwist.
>
> <small>📖 KB nr. 55 — art. 1 § 2 — _kb_</small>

> [!warning]- Btw-eenheid verwarren met fiscale consolidatie (VenB)
> **Verkeerde assumptie**: 'We hebben een btw-eenheid, dus we hebben ook fiscale consolidatie in de vennootschapsbelasting.'
>
> **Kernpunt**: Twee totaal verschillende regimes. Btw-eenheid = btw-recht (art. 4 § 2 W.BTW). Groepsbijdrage / fiscale consolidatie = vennootschapsbelasting (art. 205/5 WIB92, sinds AJ 2020). Andere voorwaarden, andere periode, andere voordelen. Een groep kan beide hebben, één van beide, of geen van beide.
>
> <small>🔗 W.BTW — art. 4 § 2 — _wettekst_ · WIB92 — art. 205/5 — _wettekst_</small>

> [!warning]- Hoofdelijke aansprakelijkheid onderschatten
> **Verkeerde assumptie**: 'Elk lid betaalt zijn eigen btw-deel; de hoofdelijke aansprakelijkheid is theoretisch.'
>
> **Kernpunt**: De fiscus kan elk lid aanspreken voor de volledige groepsschuld (art. 51bis § 4 W.BTW). In een groep met financieel zwakke leden kan een sterk lid plots ingestaan worden. Risico-allocatie via een groepscharter is een interne verhouding — niet tegenstelbaar aan de Staat.
>
> <small>📖 W.BTW — art. 51bis § 4 — _wettekst_</small>

> [!warning]- Externe facturatie verwarren met intra-eenheid
> **Verkeerde assumptie**: Een lid factureert aan een derde-klant en denkt: 'we zijn één btw-eenheid, dus geen btw aanrekenen.'
>
> **Kernpunt**: Externe facturen aan klanten BUITEN de btw-eenheid worden volledig belast (normaal tarief). Enkel facturen tussen léden van dezelfde btw-eenheid vallen buiten btw. Op externe facturen vermeldt het lid wel zijn sub-btw-nummer, niet het hoofdnummer van de eenheid (art. 30 KB nr. 1).
>
> <small>📖 KB nr. 1 — art. 30 — _kb_ · CBN-advies — 2010/13 — _cbn_</small>

## Accountant-perspectieven

### Groep van verbonden vennootschappen

_De accountant die een groep met (potentieel) interne dienstprestaties begeleidt — opportuniteit-analyse en operationele werking._

#### 🧭 Adviseur

##### 👣 Kosten-baten-analyse btw-eenheid

Becijfer de niet-aftrekbare btw op huidige interne facturen (vooral relevant als één lid vrijgesteld is of gemengd met laag pro-rata). Weeg af tegen administratieve overhead (gecentraliseerde btw-boekhouding) en risico's (hoofdelijke aansprakelijkheid, herziening bij toetreding). Vuistregel: vanaf 50.000+ EUR jaarlijkse niet-aftrekbare btw op interne stromen is een btw-eenheid economisch interessant.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 🧭 Herziening-due-diligence bij in/uittreding

Bij toetreding van een lid met recente investeringen: lijst alle bedrijfsmiddelen op die nog in herzieningsperiode zitten (5 jaar roerend, 15 jaar onroerend, art. 9 KB nr. 3). Becijfer de potentiële positieve of negatieve herziening voor de eenheid. Bij uittreding: idem omgekeerd. Onverwachte herzieningsschuld kan tot honderdduizenden EUR oplopen voor een vastgoeddochter.

<small>🔗 W.BTW — art. 48 — _wettekst_ · KB nr. 3 — art. 9 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Gecentraliseerde btw-boekhouding + aangifte

Houd per lid een afzonderlijke btw-boekhouding (omzet- en kostenrekeningen blijven per vennootschap voor jaarrekeningdoeleinden). De vertegenwoordiger consolideert maandelijks/per kwartaal tot één btw-aangifte op groepsniveau (CBN 2010/13). Schakel boekhoudsoftware in die per lid kan boeken én aggregeren. Interne facturen krijgen geen btw-code maar wel een 'intra-eenheid'-flag om bij externe controle de eliminatie te kunnen tonen.

<small>📖 CBN-advies — 2010/13 — _cbn_</small>

#### 💰 Fiscaal adviseur

##### 👣 Aanmeldingsprocedure + opvolging in/uittredingen

Initieel verzoek (art. 2 KB nr. 55): gemotiveerd document + bewijzen van de drie verbondenheidscriteria + lijst leden + aanduiding vertegenwoordiger. Indienen bij controle van de vertegenwoordiger. Daarna: voor elke wijziging in samenstelling (nieuwe dochter >50 %, verkoop dochter, fusie tussen leden) tijdig kennisgeving aan controle. Houd een 'btw-eenheid-dossier' bij met alle correspondentie en beslissingen.

<small>📖 KB nr. 55 — art. 2-4 — _kb_</small>

## Verder lezen (scope-out)

- ↪ Aftrek-pro-rata binnen BTW-eenheid (gemengde belastingplichtige) → [[btw-aftrek]] _(mag-verwijzen)_
- ↪ BTW-vastgoed binnen BTW-eenheid (herziening bij toetreding/uittreding) → [[btw-vastgoed]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `bevat`
- [[btw-belastingplichtige]] — Een btw-eenheid is een verzameling van btw-belastingplichtigen die voor de btw als één belastingplichtige worden behandeld.
### `beinvloed_door`
- [[btw-aftrek]] — Bij gemengde belastingplichtige-leden geldt het algemeen verhoudingsgetal of werkelijk gebruik op groepsniveau, niet per lid.
### `triggert`
- [[btw-herziening-bedrijfsmiddelen]] — Toetreding tot of uittreding uit een btw-eenheid kan herzieningen op bedrijfsmiddelen activeren wanneer de bestemming wijzigt.
