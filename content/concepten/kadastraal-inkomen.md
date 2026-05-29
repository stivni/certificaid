---
title: "Kadastraal inkomen"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.V
  - 2.2.V.A
  - 2.7.II.A
  - 2.7.II.B
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/kadastraal-inkomen.json"
---

_Instrument_ · afk: **KI** · ook: revenu cadastral · kadastraal inkomen onroerend goed

## Definitie

Het kadastraal inkomen (KI) is het door de fiscale administratie (AAPD — Algemene Administratie van de Patrimoniumdocumentatie, voorheen 'Kadaster') vastgestelde forfaitaire jaarlijkse netto-huurinkomen dat aan elk Belgisch kadastraal perceel wordt toegekend, geraamd naar het referentietijdstip 1 januari 1975 (art. 486 WIB92). Het KI is een fiscale grootheid — geen werkelijke huur — die dient als gemeenschappelijke grondslag voor (1) het belastbaar onroerend inkomen in de personenbelasting, (2) de onroerende voorheffing (gewestelijke belasting), (3) bepaalde lokale belastingen en (4) sommige fiscale herkwalificatie-grenzen (zoals bedrijfsleidersbezoldiging). Voor toepassing in art. 7-11 WIB92 en art. 221, 1° wordt het KI jaarlijks geïndexeerd aan het CPI (art. 518).

<small>📖 WIB92 — art. 471 — _wettekst_ · WIB92 — art. 472 — _wettekst_ · WIB92 — art. 486 — _wettekst_ · WIB92 — art. 518 — _wettekst_</small>

## Substantie

Economisch wil het KI zeggen: 'hoeveel netto-huurinkomen zou dit perceel jaarlijks opbrengen indien het in 1975 normaal werd verhuurd'. Voor een gebouw wordt het normaal bruto-huur (1975) verminderd met 40 % wegens onderhouds- en herstellingskosten (art. 477 §2). Voor een grond wordt het bruto-huurinkomen verminderd met 10 % (art. 479 §2). Bij gebrek aan eigen marktgegevens werkt AAPD met vergelijkingspunten ('schatting bij vergelijking') uit gelijkaardige percelen in dezelfde of naburige gemeente. Een nieuw of verbouwd pand wordt na voltooiing herschat (art. 494) en het nieuwe KI geldt vanaf de eerste dag van de maand na voltooiing. Doordat de referentiehuren al 50 jaar oud zijn én er sinds 1980 geen algemene perekwatie meer is geweest, ligt het effectieve geïndexeerde KI doorgaans (ver) onder de werkelijke marktwaarde — vandaar het fiscale voordeel bij particuliere verhuur (zie onroerend-inkomen-pb).

<small>🔗 WIB92 — art. 477 — _wettekst_ · WIB92 — art. 479 — _wettekst_ · WIB92 — art. 494 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De ratio legis is administratieve efficiëntie: door één forfaitair bedrag per perceel vast te leggen, kan de fiscus zonder telkens werkelijke huurcontracten op te vragen het belastbaar onroerend inkomen berekenen. Daarnaast is het KI een politiek-economische realiteit: een algemene perekwatie (aanpassing aan actuele huurwaarden) zou tot massale belastingverhogingen leiden voor eigenaars, en wordt al 45 jaar uitgesteld. De indexering (art. 518) compenseert deels deze veroudering, maar volgt de algemene inflatie, niet de specifieke vastgoedmarkt. Het systeem behoudt zo zijn fiscale gunstigheid voor de modale eigenaar-bewoner en particuliere verhuurder.

<small>🔗 WIB92 — art. 486 — _wettekst_ · WIB92 — art. 518 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **1975-01-01** · basis: WIB92 art. 471-504 + KB van 10.10.1979 + Vlaamse Codex Fiscaliteit (overgenomen voor onroerende voorheffing sinds 2014)

Stabiel sinds 1975-perekwatie. Sinds 1 januari 2014 zijn de gewesten bevoegd voor de toepassing van het KI in de onroerende voorheffing (Vlaamse Codex Fiscaliteit art. 5.0.0.0.1 §1) — de federale vaststelling van het KI door AAPD blijft echter centraal.

**✅ Voor**
- 📖 Elk Belgisch onroerend goed (gebouwd of ongebouwd) krijgt een KI van AAPD toegewezen. Voor in het buitenland gelegen onroerende goederen werd sinds 2021 ook een KI vastgesteld (na arresten Hof van Justitie EU over discriminatie).

**📋 Voorwaarden**
- 🔗 Eigenaar (of houder van zakelijk recht) moet aangifte doen aan AAPD binnen 30 dagen na (1) voltooiing nieuwbouw, (2) ingebruikneming nieuw materieel/outillage of (3) wijziging die aanleiding kan geven tot herschatting. AAPD betekent vervolgens het nieuwe KI per aangetekend schrijven. Bezwaartermijn = 2 maanden vanaf de betekening (art. 499 WIB92).

**▶️ Trigger start**
- 📖 Schatting van KI gebeurt bij: (1) nieuwbouw of in gebruik genomen nieuw materieel/outillage; (2) aanzienlijke wijziging (vergroting, herbouw, bestemmingsverandering met ≥15 % effect op KI of minstens €50); (3) verbetering bij schrijf- of rekenfout; (4) na aangifte door eigenaar (art. 473) van bouwwerk of bestemmingsverandering binnen 30 dagen na voltooiing/ingebruikneming.

**⚠️ Risico**
- 📖 Wie aangifte vergeet (bv. zwart bijgebouwde veranda, omvorming garage tot woonruimte) loopt het risico dat AAPD ambtshalve (art. 494 §1, 4°) een hoger KI vaststelt met terugwerkende kracht én bijkomende boete. Bovendien wordt elke renovatie ≥€50 KI-impact aangiftepliching. Stagiairs adviseren best aan elke vastgoedeigenaar om bij grote werken een formele aangifte voor te bereiden.

## Bouwstenen

### 🧮 Vaststellingsformule KI gebouwd onroerend goed

KI_gebouw = normale_netto-huurwaarde_1975 = normale_brutohuur_1975 × (1 − 40 %) = normale_brutohuur_1975 × 0,60. AAPD raamt de normale brutohuur 1975 hetzij rechtstreeks (uit bewijskrachtige huurcontracten van die periode), hetzij via vergelijking met gelijkaardige percelen waarvan het KI definitief is (art. 477 §1).

<small>📖 WIB92 — art. 477 §2 — _wettekst_ · WIB92 — art. 477 §1 — _wettekst_</small>

### 🧮 Vaststellingsformule KI ongebouwd onroerend goed

KI_grond = normale_netto-huurwaarde_1975 = normale_brutohuur_1975 × (1 − 1/10) = brutohuur_1975 × 0,90. Voor gronden wordt enkel 10 % forfaitair afgetrokken (geen gebouw, dus minder onderhoud). Minimum-KI per hectare = €2 (art. 482, derde lid). Voor bouwlanden, hooilanden, weilanden en moestuinen werkt AAPD met vaste KI-tarieven per hectare.

<small>📖 WIB92 — art. 479 — _wettekst_ · WIB92 — art. 482 — _wettekst_</small>

### 🧮 Indexeringsformule KI (art. 518)

Indexeringscoëfficiënt = (gemiddelde CPI van het jaar dat voorafgaat aan het inkomstenjaar) / (gemiddelde CPI 1988-1989). Het KI uitgedrukt in 1975-euro's wordt zo herrekend naar de CPI van het 'voorgaande jaar'. AAPD past dit jaarlijks toe en publiceert de coëfficiënt vóór 31 maart. Voor inkomstenjaar 2024 (AJ 2025) ≈ 2,0915 (Cijferzakboekje raadplegen voor exact bedrag).

<small>📖 WIB92 — art. 518 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Aangifteplicht eigenaar (art. 473)

Elke eigenaar of houder van zakelijk recht moet binnen 30 dagen na (a) voltooiing nieuwbouw of verbouwing, (b) ingebruikneming nieuw materieel/outillage, (c) sloop, (d) bestemmingsverandering die aanleiding kan geven tot herschatting (≥15 % KI-impact of ≥€50) AAPD via een formele aangifte verwittigen. AAPD voert dan een schatting/herschatting uit volgens de procedure van art. 477-482 en betekent het nieuwe KI.

<small>📖 WIB92 — art. 473 — _wettekst_ · WIB92 — art. 494 §1 en §2 — _wettekst_</small>

### 📏 Drempel 'aanzienlijke wijziging' (art. 494 §2)

Een wijziging is 'aanzienlijk' (en dus aangifteplichtig + KI-herschatting waardig) wanneer ze een KI-vermeerdering of -vermindering tot gevolg kan hebben van minstens €50 OF minstens 15 % van het bestaande KI. Voorbeeld: een woning met KI €1.200 — verbouwing moet KI met minstens €180 wijzigen om aanzienlijk te zijn. Kleinere ingrepen (schilderwerk, verwarmingsketel vervangen) zijn niet aangifteplichtig.

<small>📖 WIB92 — art. 494 §2, 1° — _wettekst_</small>

### ⚙️ Algemene perekwatie + buitengewone herziening

Een 'algemene perekwatie' is een wettelijk voorziene veralgemening van alle KI's aan een nieuw referentietijdstip — bedoeld om de 1975-basis bij te werken. Sinds 1980 (laatste perekwatie) is dit telkens uitgesteld om politieke redenen. Tussentijds bestaat de 'buitengewone herziening' (art. 490): kan ambtshalve door de Minister van Financiën worden voorgeschreven, of op gemotiveerde aanvraag van burgemeester of een groep van 1/10e van de percelen die kunnen aantonen dat de werkelijke netto-huurwaarde ≥15 % afwijkt van het KI. Hiermee kan een gemeentelijke recht-zetting plaatsvinden zonder algemene perekwatie.

<small>📖 WIB92 — art. 490 — _wettekst_ · WIB92 — art. 486 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Vaststelling KI bij nieuwbouw — vrijstaande woning
> _De heer Stevens bouwt een vrijstaande woning, 220 m² woonoppervlakte, voltooid op 15 maart 2024. AAPD vergelijkt met gelijkaardige woningen in de buurt met definitief KI. Vergelijkingspand: KI €1.450 voor 200 m². Stevens dient binnen 30 dagen aangifte in._
>
> **Berekening:**
>
> - Stap 1 — Stevens dient aangifte in bij AAPD binnen 30 dagen na 15 maart 2024 (uiterste datum 14 april 2024).
> - Stap 2 — AAPD bezoekt de woning (eventueel) en gebruikt vergelijkingsmethode (art. 477 §1) want geen marktgegevens 1975 voor nieuwbouw.
> - Stap 3 — KI vergelijkingspand €1.450 voor 200 m² → €7,25/m² (gestileerde berekening; in praktijk wegen ook andere kenmerken).
> - Stap 4 — KI nieuwbouw 220 m² ≈ €1.595 (na bijstellingen voor kwaliteit, ligging, ...).
> - Stap 5 — AAPD betekent KI €1.595 per aangetekend schrijven. Stevens heeft 2 maanden bezwaartermijn (art. 499).
> - Stap 6 — KI geldt vanaf 1 april 2024 (eerste dag van de maand volgend op voltooiing — art. 494 §5).
>
> → **Resultaat**: Stevens geeft vanaf AJ 2025 een niet-geïndexeerd KI van €1.595 aan in vak III rubriek 2 (indien tweede woning) of NIET aan (indien eigen woning, vrijgesteld). Geïndexeerd KI 2024: €1.595 × 2,0915 ≈ €3.336. Belastbaar in PB (× 1,40 brutering, niet-eigen-woning): €4.671.
>
> <small>🔗 WIB92 — art. 473 — _wettekst_ · WIB92 — art. 477 §1 — _wettekst_ · WIB92 — art. 494 §5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Aanzienlijke wijziging — kelderverdieping omgevormd tot praktijkruimte
> _Dr. Vermeulen (huisarts) zet de kelder van zijn woning om tot een aparte praktijkruimte van 60 m². Bestaande KI woning = €1.200. Door de bestemmingswijziging (woon → praktijk) stijgt het KI met geschatte €250._
>
> **Berekening:**
>
> - Stap 1 — drempel 'aanzienlijk' (art. 494 §2): KI-wijziging >= EUR 50 OF >= 15 % * EUR 1.200 = EUR 180.
> - Stap 2 — verwachte KI-wijziging €250 > beide drempels — aanzienlijk → aangifteplicht.
> - Stap 3 — Vermeulen dient aangifte in binnen 30 dagen na ingebruikneming praktijk.
> - Stap 4 — AAPD herschat: nieuw KI €1.450 (waarvan €250 voor praktijkdeel).
> - Stap 5 — proportionele splitsing: woongedeelte KI = €1.200, beroepsmatig gebruikt gedeelte KI = €250. Vermeulen vermeldt in PB-aangifte: vak III rubriek 1 (beroepsmatig) KI €250 (code 1105-59). Het woongedeelte (eigen woning) blijft federaal vrijgesteld en wordt NIET aangegeven.
>
> → **Resultaat**: Slechts het beroepsmatig-gebruikte deel KI €250 wordt aangegeven (rubriek 1) — wordt als beroepskost ingebracht door Vermeulen. Het woongedeelte (eigen woning) blijft federaal vrijgesteld.
>
> <small>🔗 WIB92 — art. 494 §1, 2° — _wettekst_ · WIB92 — art. 494 §2, 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Indexering KI — illustratie indexcoëfficiënt AJ 2025
> _Onroerend goed van mevr. Peeters: niet-geïndexeerd KI €1.500 (uit oorspronkelijke 1975-vaststelling, betekend in 1980). Inkomstenjaar 2024 → aanslagjaar 2025. Indexcoëfficiënt 2024 = 2,0915 (illustratief; exacte bedrag in Cijferzakboekje)._
>
> **Berekening:**
>
> - Stap 1 — niet-geïndexeerd KI uit AAPD-record: €1.500.
> - Stap 2 — geïndexeerd KI 2024 = €1.500 × 2,0915 = €3.137,25.
> - Stap 3 — voor onroerende voorheffing (gewest): basis = €3.137,25 — tarief Vlaanderen ≈ 2,5 % → €78,43 als gewestelijke basis (vóór opcentiemen gemeente + provincie).
> - Stap 4 — voor PB-onroerend inkomen bij niet-verhuurd gebouw (rubriek 2): belastbaar = €3.137,25 × 1,40 = €4.392,15.
> - Stap 5 — voor herkwalificatiegrens art. 32, 3° WIB92 (bedrijfsleider): grens = 5/3 × €1.500 × 5,46 (revalcoef AJ 2025) = €13.650. (Let op: deze formule gebruikt NIET-geïndexeerd KI × revalcoef.)
>
> → **Resultaat**: Eén basis-KI €1.500 leidt tot drie verschillende afgeleide bedragen voor drie verschillende fiscale toepassingen — vandaar de centrale rol van het KI als 'grond-grootheid' van het Belgisch onroerend-fiscaal recht.
>
> <small>🔗 WIB92 — art. 518 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Geïndexeerd KI verwarren met niet-geïndexeerd basis-KI
> **Verkeerde assumptie**: Studenten gebruiken een 'KI van €3.137' in een berekening en weten niet of dat geïndexeerd is of niet.
>
> **Kernpunt**: AAPD-records geven altijd het NIET-geïndexeerde KI (basis 1975, uitgedrukt in EUR). MyMinFin, aanslagbiljet onroerende voorheffing en hypotheekakte vermelden het niet-geïndexeerde bedrag. De indexering gebeurt door fiscus voor PB-doeleinden (art. 518). Voor de herkwalificatie-formule (bedrijfsleider) wordt het niet-geïndexeerde KI × revaloriseringscoëfficiënt gebruikt; voor PB-vak III geeft de belastingplichtige het niet-geïndexeerde KI aan en past de fiscus zelf coëfficiënt + × 1,40 toe.
>
> <small>📖 WIB92 — art. 518 — _wettekst_ · aangifte-PB-2025-bezoldigingen — Vak III 'KI's vermelden als niet-geïndexeerd bedrag' — _aangifte_</small>

> [!warning]- Vergeten dat bezwaartermijn KI maar 2 maanden is
> **Verkeerde assumptie**: Bezwaar tegen KI wordt verward met bezwaar tegen aanslag → 6 maanden termijn.
>
> **Kernpunt**: Bezwaar tegen het door AAPD betekende KI moet binnen 2 maanden na de aangetekende betekening worden ingediend bij AAPD (art. 499 WIB92). Daarna is het KI definitief en geldt het voor alle afgeleide belastingen (PB, OV, lokale) tot de volgende herschatting. Het bezwaar tegen een specifieke PB-aanslag is iets anders en heeft wel een termijn van 6 maanden vanaf de derde werkdag na verzending van het aanslagbiljet (art. 366).
>
> <small>🔗 WIB92 — art. 499 — _wettekst_ · WIB92 — art. 366 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Bouwen-zonder-aangifte denken te ontsnappen
> **Verkeerde assumptie**: Een eigenaar bouwt zelf een veranda van €30.000 en doet geen aangifte aan AAPD, ervan uitgaande dat 'AAPD het toch niet ziet'.
>
> **Kernpunt**: AAPD krijgt automatisch een afschrift van elke bouwvergunning via gemeentelijke administraties. Bovendien werkt fiscus met luchtfoto's en periodieke detectiecampagnes. Wie aangifteplicht (art. 473) overtreedt, riskeert (1) ambtshalve herschatting (art. 494 §1, 4°), (2) verhoogd KI met terugwerkende kracht en (3) administratieve boete. De 'aanzienlijke wijziging'-drempel (≥€50 of ≥15 % KI) is laag — vrijwel elke significante verbouwing valt eronder.
>
> <small>📖 WIB92 — art. 473 — _wettekst_ · WIB92 — art. 494 §1, 4° — _wettekst_ · WIB92 — art. 494 §2, 1° — _wettekst_</small>

## Accountant-perspectieven

### Eigenaar bij verbouwing / nieuwbouw

_De accountant die een cliënt-eigenaar begeleidt bij KI-gerelateerde gebeurtenissen (nieuwbouw, verbouwing, bezwaar, herwaardering)._

#### 👥 Begeleider

##### 👣 Aangifte AAPD voorbereiden bij grote werken

Zodra een cliënt grote werken aankondigt (verbouwing >€10.000, bestemmingswijziging, sloop, nieuwbouw): (1) verifieer of werken aanzienlijk zijn (≥€50 of ≥15 % KI-impact); (2) noteer voltooiingsdatum + bewaar bouwvergunning + foto's; (3) bereid AAPD-aangifte voor (formulier 43B) binnen 30 dagen na voltooiing; (4) wacht op betekening nieuw KI en beoordeel bezwaartermijn 2 maanden. Bewaar dossier in client-vault voor minstens 5 jaar.

<small>📖 WIB92 — art. 473 — _wettekst_ · WIB92 — art. 494 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Bezwaar tegen KI-betekening

Bij ontvangst van een KI-betekening die te hoog lijkt: (1) vergelijk met KI's van gelijkaardige panden in de buurt (publieke registers); (2) bereken effect op alle afgeleide belastingen (PB + OV + lokale heffingen) om bezwaarwaardigheid te beoordelen; (3) verzamel marktgegevens 1975 of vergelijkingspunten; (4) dien bezwaar in bij AAPD binnen 2 maanden — vertraging = onontvankelijk. Bewijslast ligt bij belastingplichtige; AAPD-schatting heeft sterke vermoedensbescherming.

<small>🔗 WIB92 — art. 499 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Toepassing in PB-onroerend-inkomen (brutering × 1,40) → [[onroerend-inkomen-pb]] _(moet-verwijzen)_
- → Onroerende voorheffing als gewest-belasting op KI → [[onroerende-voorheffing]] _(moet-verwijzen)_
- ↪ Gebruik KI als grondslag voor lokale belastingen → [[lokale-en-regionale-belastingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `triggert`
- [[onroerende-voorheffing]] — OV-aanslag wordt elk jaar op basis van geïndexeerd KI berekend door gewest (Vlaams: 2,5 % federale grondslag + gemeentelijke en provinciale opcentiemen).
- [[onroerend-inkomen-pb]] — KI is de basis-grootheid voor de berekening van het belastbaar onroerend inkomen in vak III PB.
