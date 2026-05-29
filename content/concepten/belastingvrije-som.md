---
title: "Belastingvrije som"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.III
  - 2.2.XVI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/belastingvrije-som.json"
---

_Regime_ · afk: **BVS** · ook: vrijgesteld minimum · belastingvrij minimum

## Definitie

De belastingvrije som is dat deel van het belastbaar inkomen waarop geen personenbelasting verschuldigd is. Het bedrag bestaat uit een basisbedrag (4.785 EUR niet-geïndexeerd, art. 131 WIB92) — eventueel verhoogd met +870 EUR als de belastingplichtige zelf gehandicapt is — vermeerderd met toeslagen voor personen ten laste (art. 132) en andere bijzondere situaties (art. 133, bv. alleenstaande ouder). De vrijgestelde som wordt niet 'afgetrokken' van het inkomen, maar gebruikt om een belastingvermindering te berekenen die de basisbelasting (art. 130) reduceert: de fictieve belasting op de BVS-schijven (25/30/40/45/50%) wordt afgehaald.

<small>📖 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 134 — _wettekst_</small>

## Substantie

Economisch effect: iedereen krijgt een minimum-inkomen vrijgesteld van PB — een sociale ondergrens die het bestaansminimum beschermt. Het basisbedrag is uniform, maar wordt verhoogd in functie van gezinslast (kinderen, ouders/grootouders, zijverwanten ten laste) en persoonlijke factoren (handicap belastingplichtige, alleenstaande ouder). Mechanisch werkt dat zo: de basisbelasting wordt berekend volgens art. 130 (progressieve schijven 25/40/45/50%), en daarvan wordt de 'belasting op de BVS' afgetrokken. Die belasting op de BVS volgt een eigen schaal (25 → 50%) gestructureerd zodat de eerste schijf van het inkomen volledig wordt vrijgesteld (effectief tarief 25% verlies = 25% besparing). Voor lagere inkomens die niet de volledige BVS kunnen 'opbruiken': het surplus dat betrekking heeft op kinder-toeslagen (art. 132,1°-6°) wordt omgezet in een terugbetaalbaar belastingkrediet (art. 134 §3, plafond 550 EUR per kind niet-geïndexeerd).

<small>📖 WIB92 — art. 134 — _wettekst_</small>

## Rationale

Ratio legis: de belastingvrije som is een verticaal-rechtvaardigheidsinstrument. Het garandeert dat een minimum-bestaansinkomen wordt vrijgesteld van PB (sociale ondergrens) en het differentieert de belastingdruk in functie van gezinslast en handicap (draagkracht-correctie). De gestructureerde toerekeningsvolgorde van art. 134 (basisbedrag + handicaptoeslag → toeslagen art. 132,7°+8° en 133 → toeslagen art. 132,1°-6°) verzekert dat het deel dat 'verloren' zou gaan voor lage inkomens, juist het deel betreft dat kinderen ten laste betreft — exact het deel dat in terugbetaalbaar krediet wordt omgezet om gezinnen met kinderen extra te beschermen.

<small>🔗 WIB92 — art. 134 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 131-145

Stabiel kader sinds WIB92. Basisbedrag is jaarlijks geïndexeerd; politieke maatregel: tijdelijk verhoogd basisbedrag voor lagere inkomens onder bepaalde regeringen (zie historische versies).

**✅ Voor**
- 📖 Alle aan de PB onderworpen belastingplichtigen (rijksinwoners) — basisbedrag is universeel.

**📋 Voorwaarden**
- 📖 Voor verhogingen voor personen ten laste (art. 132): die personen moeten op 1 januari AJ deel uitmaken van het gezin en netto-bestaansmiddelen onder plafond hebben (art. 136). Voor handicap-verhoging (art. 131, lid 2 + art. 135): erkenning van de handicap moet worden aangetoond. Voor de toeslag van art. 133, 1° (alleenstaande ouder): geen gemeenschappelijke aanslag + één of meer kinderen ten laste.

**👍 Voordeel**
- 📖 Vrijgestelde schijf van inkomen → de eerste euros van het inkomen worden niet belast. Per persoon ten laste komt er een toeslag bovenop. Belastingbesparing varieert van 25% van het toegerekende deel (lage inkomens, eerste BVS-schijf) tot 50% (hoge inkomens, hoogste BVS-schijf).
- 📖 Terugbetaalbaar belastingkrediet (art. 134 §3): voor zeer lage inkomens met kinderen ten laste betaalt de fiscus actief een bedrag uit als de BVS niet volledig kan worden 'verrekend' tegen de basisbelasting (max 550 EUR per kind, niet-geïndexeerd; helft bij co-ouderschap art. 132bis).

**⚠️ Risico**
- 🔗 Vergeten een verhoging te claimen: handicap-verhoging (+870 EUR), alleenstaande-ouder-toeslag (art. 133, 1°) of bijkomende toeslag voor lage-inkomen-alleenstaande-ouder (art. 133, lid 2). Deze worden niet automatisch toegekend zonder correcte aangifte (handicap-attest opvragen, vakje aankruisen).

## Bouwstenen

### 📏 Basisbedrag belastingvrije som (art. 131)

Basisbedrag: 4.785 EUR (niet-geïndexeerd, WIB92 art. 131, eerste lid). Voor de geïndexeerde versie van het AJ raadpleeg het Cijferzakboekje. Wanneer de belastingplichtige zelf gehandicapt is (zoals omschreven in art. 135), wordt het basisbedrag verhoogd met +870 EUR (niet-geïndexeerd, art. 131 laatste lid).

<small>📖 WIB92 — art. 131 — _wettekst_</small>

### 📜 Toeslagen voor personen ten laste (art. 132)

Het basisbedrag wordt verhoogd met progressieve toeslagen per persoon ten laste: kinderen (oplopend 870 EUR voor 1 kind → 8.120 EUR voor 4 kinderen + 3.100 EUR per kind boven het vierde), bijkomende toeslag van 325 EUR per kind <3 jaar (cf. anti-cumulatie met kinderoppas-vermindering art. 14535), toeslag van 2.610 EUR voor 66+-jarige zorgbehoevende ascendent of zijverwant ten laste, en een algemene toeslag van 870 EUR per andere persoon ten laste. Gehandicapt kind of persoon ten laste telt voor twee. Voor de details verwijzen naar [`kinderen-ten-laste`](kinderen-ten-laste).

<small>📖 WIB92 — art. 132 — _wettekst_</small>

### 📜 Toeslag alleenstaande ouder + jaar huwelijk (art. 133)

Twee bijkomende toeslagen bovenop art. 131-basis: (1) art. 133, 1°: +870 EUR voor een alleen-belastingplichtige met één of meer kinderen ten laste (incl. wanneer art. 132bis half-half-deling van toeslagen wordt toegepast); (2) art. 133, 2°: +870 EUR voor het jaar van huwelijk of verklaring van wettelijke samenwoning waar geen gemeenschappelijke aanslag wordt gevestigd, mits de echtgenoot/partner geen netto-bestaansmiddelen >1.800 EUR (niet-geïndexeerd) heeft gehad. Voor lage-inkomen-alleenstaande-ouder (belastbaar inkomen <10.700 EUR + voldoet aan strikte voorwaarden) wordt de toeslag van 1° bijkomend verhoogd met max +565 EUR (degressief in functie van inkomen).

<small>📖 WIB92 — art. 133 — _wettekst_</small>

### ⚙️ Toerekeningsvolgorde belastingvrije som (art. 134 §2, eerste lid)

De belastingvrije som wordt geacht achtereenvolgens te bestaan uit: (1) basisbedrag art. 131; (2) toeslagen art. 132, 7° en 8° (66+-zorgbehoevende ascendent + andere persoon ten laste) en art. 133 (alleenstaande ouder, jaar huwelijk); (3) toeslagen art. 132, 1° tot 6° (kinderen + jong-kind-toeslag). Deze volgorde is geen detail — ze bepaalt welk deel van de BVS in het terugbetaalbaar krediet (art. 134 §3) terechtkomt: enkel het laatste blok (kinderen-toeslagen) wordt omgezet in krediet wanneer de BVS-belasting de basisbelasting overschrijdt. Het deel van de BVS dat het belastbaar inkomen overschrijdt EN niet bestaat uit kinder-toeslagen, gaat verloren.

<small>📖 WIB92 — art. 134 — _wettekst_</small>

### 🧮 Tarieven belasting op BVS (art. 134 §2)

De belasting op de belastingvrije som (= belastingvermindering) wordt berekend volgens progressieve schijven (niet-geïndexeerd):
• 25% voor de schijf van 0,01 EUR tot 5.705 EUR
• 30% voor de schijf van 5.705 EUR tot 8.120 EUR
• 40% voor de schijf van 8.120 EUR tot 13.530 EUR
• 45% voor de schijf van 13.530 EUR tot 24.800 EUR
• 50% voor de schijf boven 24.800 EUR

Deze schijven sporen ongeveer met de PB-tarief-schijven (25-40-45-50%) — wat verzekert dat de BVS zijn werking aan de 'onderkant' van het inkomen heeft: een belastingplichtige in de 50%-marginaal-tarief-schijf bespaart méér op zijn marginaal tarief dan op de BVS-vermindering, dus de BVS werkt netto-vermindering op de eerste schijven.

<small>📖 WIB92 — art. 134 — _wettekst_</small>

### ⚙️ Terugbetaalbaar belastingkrediet (art. 134 §3)

Wanneer de berekende belasting op de BVS (art. 134 §2) groter is dan de basisbelasting (art. 130), is het surplus normaal verloren. Voor het deel van het surplus dat overeenstemt met kinder-toeslagen (art. 132, 1°-6°) wordt het echter omgezet in een terugbetaalbaar belastingkrediet. Plafond: 550 EUR per kind ten laste (niet-geïndexeerd; voor kind onder art. 132bis: helft). Gehandicapt kind: telt voor twee. Voor bijkomende toeslag art. 133, lid 2 (lage-inkomen-alleenstaande-ouder) geldt eveneens omzetting in terugbetaalbaar krediet.

<small>📖 WIB92 — art. 134 — _wettekst_</small>

### 💡 Definitie 'gehandicapt' (art. 135)

'Gehandicapt' in de zin van de BVS-verhogingen omvat: (1) personen wier verdienvermogen door pre-65-feiten verminderd is tot 1/3 of minder (algemene arbeidsmarkt); of een vermindering van zelfredzaamheid ≥9 punten (medisch-sociale schaal); of na primaire ongeschiktheid een verdienvermogen ≤1/3; of een administratief/gerechtelijk vastgestelde blijvende handicap ≥66%; (2) kinderen met ten minste 66% handicap door één of meerdere aandoeningen. Erkenning gebeurt door FOD Sociale Zekerheid, Medex of ziekenfonds-arts.

<small>📖 WIB92 — art. 135 — _wettekst_</small>

### ↪️ Niet-meetellende bestaansmiddelen (art. 143)

Bij het berekenen van de netto-bestaansmiddelen van een persoon ten laste (cf. art. 136-plafond), tellen volgende inkomsten NIET mee: (1) wettelijke kinderbijslagen, kraamgelden, adoptiepremies, niet-rechten-opbouwende studiebeurzen, voorhuwelijkssparen; (2) tegemoetkomingen aan personen met een handicap (wet 27 februari 1987); (3) pensioenen/renten verkregen door 66+-zorgbehoevende ten laste tot 14.500 EUR/jaar; (4) bezoldigingen verkregen door gehandicapten in erkende beschutte werkplaatsen; (5) achterstallige onderhoudsuitkeringen na het belastbaar tijdperk; en meer. Deze uitsluitingen verklaren waarom een persoon met sociale uitkeringen toch nog ten laste kan blijven.

<small>📖 WIB92 — art. 143 — _wettekst_</small>

## Voorbeelden

> [!example]- Alleenstaande zonder personen ten laste — basis-BVS
> _Alleenstaande belastingplichtige, geen kinderen ten laste, geen handicap. Belastbaar inkomen 30.000 EUR. Bedragen niet-geïndexeerd WIB92-niveau._
>
> **Berekening:**
>
> - Stap 1 — BVS = basisbedrag art. 131 = 4.785 EUR (niet-geïndexeerd).
> - Stap 2 — belasting op BVS (art. 134 §2): 4.785 EUR valt volledig in eerste schijf (0 → 5.705): 4.785 × 25% = 1.196,25 EUR.
> - Stap 3 — basisbelasting (art. 130) op 30.000 EUR (gestileerd): 25% × 8.000 + 40% × (15.000−8.000) + 45% × (24.000−15.000) + 50% × (30.000−24.000) = 2.000 + 2.800 + 4.050 + 3.000 = 11.850 EUR.
> - Stap 4 — netto basisbelasting na BVS-vermindering: 11.850 − 1.196,25 = 10.653,75 EUR.
> - Stap 5 — geen terugbetaalbaar krediet relevant (BVS volledig 'opgebruikt' tegen basisbelasting + geen kinder-toeslagen).
>
> → **Resultaat**: Belastingbesparing dankzij BVS: 1.196,25 EUR (= 25% van basis-BVS) — universeel sociaal vangnet. Geïndexeerd zal het effect groter zijn.
>
> <small>🔗 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 134 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Gehandicapte belastingplichtige met 3 kinderen — gecumuleerde verhogingen
> _Gezin met gemeenschappelijke aanslag. Belastingplichtige A is gehandicapt (art. 135), heeft 3 kinderen ten laste (waarvan 1 gehandicapt en 1 <3 jaar). Geen co-ouderschap._
>
> **Berekening:**
>
> - Stap 1 — basisbedrag art. 131 = 4.785 EUR.
> - Stap 2 — handicap-verhoging belastingplichtige: +870 EUR.
> - Stap 3 — kinderen: gehandicapt kind telt voor twee → effectief 4 kinderen. Toeslag art. 132, 4° = 8.120 EUR.
> - Stap 4 — bijkomende toeslag <3 jaar: +325 EUR (mits geen kinderoppas-vermindering art. 14535 voor dat kind).
> - Stap 5 — totale BVS = 4.785 + 870 + 8.120 + 325 = 14.100 EUR (niet-geïndexeerd).
> - Stap 6 — belasting op BVS (art. 134 §2): 25% × 5.705 + 30% × (8.120−5.705) + 40% × (13.530−8.120) + 45% × (14.100−13.530) = 1.426,25 + 724,5 + 2.164 + 256,5 = 4.571,25 EUR.
> - Stap 7 — die ≈4.571 EUR wordt afgehaald van de basisbelasting (art. 130). Voor een gezin met laag inkomen (waar basisbelasting <4.571 zou zijn): surplus wordt omgezet in terugbetaalbaar krediet voor zover het deel betreft van kinder-toeslagen (8.120 + 325 = 8.445 EUR van de BVS), tot plafond 550 EUR × 4 kinderen-equivalent = 2.200 EUR.
>
> → **Resultaat**: De toerekenings-volgorde van art. 134 §2 zorgt ervoor dat de basisbedrag + handicap-verhoging + alleenstaande-toeslag eerst worden 'verbruikt' tegen de basisbelasting, en pas dan de kinder-toeslagen — die laatste komen dus precies in aanmerking voor terugbetaalbaar krediet.
>
> <small>🔗 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 132 — _wettekst_ · WIB92 — art. 134 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Jaar van huwelijk — toeslag art. 133, 2°
> _A trouwt met B in juli van inkomstenjaar N. B heeft geen netto-bestaansmiddelen meer dan 1.800 EUR gehad gedurende het jaar. Voor jaar N wordt geen gemeenschappelijke aanslag gevestigd (art. 126 §2, 1° WIB92): elk een individuele aanslag._
>
> **Berekening:**
>
> - Stap 1 — beide echtgenoten worden individueel belast (art. 126 §2 — jaar huwelijk).
> - Stap 2 — A claimt in zijn individuele aanslag de toeslag van art. 133, 2°: +870 EUR (niet-geïndexeerd) omdat B in jaar N geen netto-bestaansmiddelen >1.800 EUR had.
> - Stap 3 — BVS van A wordt dus: 4.785 (art. 131) + 870 (art. 133, 2°) = 5.655 EUR.
> - Stap 4 — belasting op BVS: 5.655 × 25% = 1.413,75 EUR (volledig in eerste schijf 0 → 5.705).
> - Stap 5 — B heeft een eigen BVS-basisbedrag van 4.785 EUR (= 1.196,25 EUR vermindering), maar weinig of geen belastbaar inkomen — surplus van zijn BVS gaat verloren tenzij hij kinderen ten laste heeft (dan terugbetaalbaar krediet).
>
> → **Resultaat**: Concreet verschil dankzij art. 133, 2°: +870 × 25% = 217,50 EUR extra besparing voor A. Volgend AJ (= jaar ná huwelijk) wordt overgeschakeld naar gemeenschappelijke aanslag met integrale toepassing van het huwelijksquotient.
>
> <small>📖 WIB92 — art. 133 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- BVS verwarren met aftrek 'aan onderkant'
> **Verkeerde assumptie**: De BVS wordt afgetrokken van het belastbaar inkomen vóór tarieftoepassing.
>
> **Kernpunt**: De BVS wordt NIET van het inkomen afgetrokken. De PB wordt eerst berekend op het volledige belastbaar inkomen via de tariefschijven (art. 130). Dan wordt op de BVS een fictieve belasting berekend met eigen progressieve schaal (25/30/40/45/50% — art. 134 §2) en die wordt afgetrokken. Dit verklaart waarom hogere inkomens 'meer' BVS-voordeel halen (op de hogere schijven), maar het netto-effect blijft een vrijstelling van de eerste schijven inkomen.
>
> <small>📖 WIB92 — art. 134 — _wettekst_</small>

> [!warning]- Handicap-verhoging belastingplichtige zelf vergeten
> **Verkeerde assumptie**: De BVS-verhoging voor handicap geldt alleen voor kinderen of personen ten laste.
>
> **Kernpunt**: Art. 131 (laatste lid) voorziet expliciet: het basisbedrag wordt verhoogd met 870 EUR (niet-geïndexeerd) indien de BELASTINGPLICHTIGE ZELF gehandicapt is (zoals omschreven in art. 135). Vaak vergeten op aangifte als handicap-attest niet wordt aangevraagd of als de cliënt zijn handicap-status niet meldt.
>
> <small>📖 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 135 — _wettekst_</small>

> [!warning]- Toerekenings-volgorde van art. 134 §2 negeren
> **Verkeerde assumptie**: Alle toeslagen samen behandelen alsof ze één blok zijn voor het terugbetaalbaar krediet.
>
> **Kernpunt**: De volgorde basisbedrag → 132,7°-8° + 133 → 132,1°-6° bepaalt welk deel verloren gaat en welk deel in krediet omgezet wordt. Voor lage-inkomen-gezinnen is dit cruciaal: precies omdat de kinder-toeslagen 'laatst' komen, blijven ze voor het terugbetaalbaar krediet (art. 134 §3) gereserveerd.
>
> <small>📖 WIB92 — art. 134 — _wettekst_</small>

> [!warning]- Sociaal-rechtelijke uitkeringen klakkeloos meetellen voor bestaansmiddelen ten laste
> **Verkeerde assumptie**: Alle inkomsten van een persoon ten laste tellen mee voor het netto-bestaansmiddelen-plafond.
>
> **Kernpunt**: Art. 143 sluit explicit uit: kinderbijslag, studiebeurzen (niet rechten-opbouwend), tegemoetkomingen handicap, een eerste schijf van pensioenen van 66+-zorgbehoevenden, bezoldigingen in beschutte werkplaatsen, etc. Een ascendent met IGO-rente of een kind met een handicapuitkering kan dus toch ten laste blijven.
>
> <small>📖 WIB92 — art. 143 — _wettekst_</small>

## Syntheses

### 🧩 Matrix

Overzichtsmatrix BVS-verhogingen (welk artikel, welk bedrag, welke voorwaarde)

| Verhoging | Wettelijke basis | Bedrag niet-geïndexeerd | Voorwaarde |
| --- | --- | --- | --- |
| Basis | art. 131 | 4.785 EUR | Universeel |
| Handicap belastingplichtige | art. 131 + 135 | +870 EUR | Erkende handicap pre-65 |
| 1 kind ten laste | art. 132, 1° | +870 EUR | Cf. kinderen-ten-laste |
| 2 kinderen | art. 132, 2° | +2.240 EUR | Cf. kinderen-ten-laste |
| 3 kinderen | art. 132, 3° | +5.020 EUR | Cf. kinderen-ten-laste |
| 4 kinderen | art. 132, 4° | +8.120 EUR | Cf. kinderen-ten-laste |
| Bijkomend kind | art. 132, 5° | +3.100 per kind boven 4 | Cf. kinderen-ten-laste |
| Kind <3 jaar | art. 132, 6° | +325 EUR/kind | Geen kinderoppas-vermindering |
| Zorgbehoevende ascendent 66+ | art. 132, 7° | +2.610 EUR | Zelfredzaamheid ≥9 punten |
| Andere persoon ten laste | art. 132, 8° | +870 EUR | Cf. art. 136 |
| Alleenstaande ouder | art. 133, 1° | +870 EUR | Alleen belast + ≥1 kind |
| Lage-inkomen alleenstaande ouder | art. 133, lid 2 | tot +565 EUR | Belastbaar inkomen <10.700 EUR |
| Jaar huwelijk/samenwoning | art. 133, 2° | +870 EUR | Echtgenoot zonder bestaansmiddelen |

## Accountant-perspectieven

### Particuliere cliënt (PB-aangifte)

_De accountant die de PB-aangifte voorbereidt of nakijkt — BVS-verhogingen zijn de meest 'vergeten' opties._

#### 💰 Fiscaal adviseur

##### 👣 Checklist BVS-verhogingen bij PB-aangifte

Voor elke aangifte systematisch nagaan: (1) handicap-attest belastingplichtige zelf (Vak II, rubriek 'gehandicapt')? (2) personen ten laste — voor elk: kind, ascendent zorgbehoevend, andere zijverwant? (3) gehandicapt kind/persoon ten laste (telt voor twee)? (4) kind <3 jaar? (5) alleenstaande ouder met laag inkomen (art. 133, lid 2 bijkomende toeslag)? (6) jaar huwelijk met inactieve partner (art. 133, 2°)? Per gevonden rubriek: documentatie verzamelen (handicap-attest, geboorteakte, samenstelling gezin op 1/1 AJ uit gemeente).

<small>🔗 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 132 — _wettekst_ · WIB92 — art. 133 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Uitleg mechaniek BVS aan cliënt

Veel cliënten denken dat 'BVS verhoogd met 1.000 EUR' betekent 'ik betaal 1.000 EUR minder belasting'. In werkelijkheid bespaart men slechts het belastingvermindering-tarief (25-50%) op die 1.000 EUR — dus typisch 250-500 EUR. Uitleggen dat het verschil tussen de niet-geïndexeerde wetbedragen en de geïndexeerde effectieve bedragen in het Cijferzakboekje aanzienlijk is (orde van grootte 1.5×-1.7×). Voor lage-inkomen-cliënten met kinderen: het terugbetaalbaar krediet (max 550 × kind) kan effectief cash uit de fiscus zijn.

<small>🔗 WIB92 — art. 134 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kinderen-ten-laste voorwaarden + bedragen (art. 132) → [[kinderen-ten-laste]] _(moet-verwijzen)_
- → Belastingberekening-procedure waarop BVS wordt toegepast → [[belastingberekening-pb]] _(moet-verwijzen)_
- ↪ Concrete geïndexeerde bedragen (Cijferzakboekje) _(mag-verwijzen)_
- ↪ Gewestelijke opcentiemen (aanvullende gemeentebelasting + gewestelijke decimes) → [[aanvullende-gemeentebelasting-pb]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `beinvloed_door`
- [[kinderen-ten-laste]] — Kinderen ten laste leveren de art. 132-toeslagen — het grootste deel van de BVS-verhogingen.
- [[gezinssituatie]] — Burgerlijke staat bepaalt of er gemeenschappelijke aanslag is, en dus of toeslagen van art. 133 (alleenstaande ouder, jaar huwelijk) van toepassing zijn.
### `triggert`
- [[belastingberekening-pb]] — De BVS wordt toegepast via een belastingvermindering op de basisbelasting (art. 134 §2).
