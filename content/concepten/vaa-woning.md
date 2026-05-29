---
title: "VAA — terbeschikkingstelling onroerend goed"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/vaa-woning.json"
---

_Regime_ · ook: VAA woning · woon-VAA

## Definitie

Wanneer een werkgever of vennootschap een onroerend goed (woning, appartement, villa) gratis of tegen onderprijs ter beschikking stelt aan een werknemer of bedrijfsleider, vormt het privé-bewoningsvoordeel een belastbaar voordeel van alle aard (VAA). De waardering is forfaitair op basis van het kadastraal inkomen (KI), via een formule die in 2019 werd uniform gemaakt (wet van 27 mei 2019 — eerder bestonden twee tarieven naargelang het KI hoger of lager dan 745 EUR was, een onderscheid dat na rechtspraak werd geschrapt): VAA = KI (geïndexeerd) × 100/60 × 2. Indien de woning gemeubileerd is, wordt het VAA verhoogd met 5/3 (factor 1,666...). De indexering en het samengestelde resultaat geven voor 2026 een effectieve coëfficient van ongeveer 5,3 op het ongeïndexeerd KI — exact opzoekbaar in het Cijferzakboekje.

<small>🔗 KB/WIB92 — art. 18 §3 2° — _kb_ · Wet 27 mei 2019 — uniforme coëfficient — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Praktisch: voor een woning met KI 1.500 EUR (geïndexeerd ~3.265 EUR voor 2026) komt het VAA op ongeveer 1.500 × 5,3 ≈ 7.950 EUR per jaar (illustratief — exacte indexcoëfficient bevestigen). Bij hoog-KI directievilla's loopt het VAA snel op naar 15.000–25.000 EUR per jaar — substantieel hoger dan voor 2019 toen de lagere factor van toepassing was op KI ≤ 745 EUR. Door deze hervorming is de fiscale aantrekkelijkheid van directiewoning-pakketten flink afgenomen. De werkelijke huurwaarde van de woning kan in theorie hoger zijn dan het forfait; de wet stipuleert dat het VAA mag verhoogd worden tot de werkelijke huurwaarde indien die hoger is — in de praktijk wordt het forfait gebruikt.

<small>🔗 KB/WIB92 — art. 18 §3 2° — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Kadastraal-inkomen-based waardering vermijdt jaarlijkse waarderingen van werkelijke huurwaarde. De factor 100/60 is een terugrekening van het netto-KI naar een bruto-huurwaarde-grootheid. De factor 2 die de wetgever er bovenop legt, vangt het feit op dat KI's vaak verouderd zijn (laatste herziening 1980-cijfer) en geactualiseerd worden via een index én een verhogingsfactor. Sinds Grondwettelijk Hof 2017 oordeelde dat het verschil tussen KI ≤ 745 EUR (factor 1,25) en KI > 745 EUR (factor 3,8) gelijkheidsbeginsel schond, is in 2019 één uniforme factor 2 ingevoerd.

<small>🤖 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-01-01** · basis: KB/WIB92 art. 18 §3 2° + Wet 27 mei 2019 (uniforme coëfficient)

Sinds 1 januari 2019: één uniforme factor 2 (was vroeger 1,25 voor klein KI, 3,8 voor groot KI — discriminatie volgens Grondwettelijk Hof). KI wordt jaarlijks geïndexeerd via aparte coëfficient — voor 2026 die opzoeken in Cijferzakboekje.

**✅ Voor**
- 📖 Werknemers of bedrijfsleiders aan wie hun werkgever/vennootschap een woning, appartement of ander onroerend goed gratis of tegen onderprijs ter beschikking stelt — voor privébewoning, niet voor exclusief professioneel gebruik (kantoor).

**🚫 Niet voor**
- 🔗 Onroerend goed met exclusief professionele bestemming (kantoor zonder bewoning, opslag, productie-eenheid). Een gemengd gebruik (deels privé/deels professioneel) leidt tot een pro rata-verdeling.
- 🔗 Werknemer die zelf huurt en daarvoor een huurvergoeding ontvangt van werkgever — andere regels (huurvergoeding behoort bezoldiging, geen forfait-VAA).

**👍 Voordeel**
- 🔗 Voor de vennootschap: de werkelijke kosten van de woning (afschrijving, onroerende voorheffing, onderhoud, verzekering, intresten op lening) blijven aftrekbaar (bezoldigingstheorie — kosten als bezoldiging gemaakt aan de bedrijfsleider zijn aftrekbaar mits gerechtvaardigd door werkelijke prestaties — Cassatie 2017).

**⚠️ Risico**
- 🔗 Sinds 2019-hervorming is het VAA-bedrag voor woningen met laag of middelmatig KI sterk gestegen — een loonpakket dat vroeger fiscaal voordelig was kan vandaag duurder zijn dan een cash-bezoldiging. Herevalueer bestaande directiewoning-constructies regelmatig.

## Bouwstenen

### 🧮 Basisformule VAA woning

VAA = (KI geïndexeerd) × 100/60 × 2. Het geïndexeerd KI = niet-geïndexeerd KI × indexatiecoëfficient van het AJ (voor AJ 2026 ~2,1763 — exact via Cijferzakboekje). De samengestelde factor van een ongeïndexeerd KI naar het VAA komt voor 2026 dan op ongeveer × 5,3. Voor een woning met ongeïndexeerd KI van 1.500 EUR: VAA ≈ 1.500 × 5,3 ≈ 7.950 EUR/jaar.

<small>🔗 KB/WIB92 — art. 18 §3 2° — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Verhoging voor gemeubileerde woning (5/3)

Indien de woning gemeubileerd ter beschikking wordt gesteld (inclusief huishoudtoestellen, witgoed), wordt het VAA verhoogd met factor 5/3 (≈ 1,666). Formule wordt dan: VAA gemeubileerd = (KI geïndexeerd) × 100/60 × 2 × 5/3. Voor een woning met KI 1.500 EUR komt dat neer op ongeveer 7.950 × 5/3 ≈ 13.250 EUR/jaar.

<small>📖 KB/WIB92 — art. 18 §3 2° — _kb_</small>

### ⚙️ Hervorming 2019 — uniforme factor 2

Vóór 2019: factor 1,25 voor woningen met KI ≤ 745 EUR; factor 3,8 voor woningen met KI > 745 EUR (én extra ×100/60 op KI × 2 bij ter beschikking via rechtspersoon). Grondwettelijk Hof oordeelde dit verschil ongrondwettig (schending gelijkheidsbeginsel). Wet 27 mei 2019: één uniforme factor 2 voor iedereen, ongeacht KI-niveau en aard van de verstrekker (natuurlijke persoon of rechtspersoon). Gevolg: VAA voor klein-KI-woningen steeg fors; voor groot-KI-woningen daalde licht. Adviespraktijk-rebalancing volgde.

<small>🔗 Wet 27 mei 2019 — art. 18 §3 2°-wijziging — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ✴️ Bezoldigingstheorie — aftrekbaarheid in vennootschap

Wanneer een vennootschap een woning aankoopt en ter beschikking stelt aan haar bedrijfsleider, blijven afschrijvingen, intrest op lening, onroerende voorheffing en onderhoud volledig aftrekbaar — voor zover die kosten 'verantwoord zijn door werkelijke prestaties' van de bedrijfsleider (bezoldigingstheorie, Cassatie 13/11/2017 en bevestigingen). De fiscus betwist soms aftrekbaarheid als de werkelijke kost (10.000+ EUR) niet in verhouding staat tot de prestaties (en bijhorende cash-bezoldiging). Voorzichtige praktijk: cash-bezoldiging + VAA in totaal afstellen op marktconforme directielonen.

<small>🔗 WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Alternatieve huurconstructie

Sinds 2019-hervorming overweegt de praktijk vaker huurconstructies waarbij de bedrijfsleider zelf eigenaar is en zijn woning verhuurt aan de vennootschap (die ze dan ter beschikking stelt aan hemzelf — split-rental). Risico: anti-misbruik (art. 344 §1 WIB92) — de fiscus kan stellen dat de constructie geen ander doel heeft dan belasting te ontwijken. Vereist economisch reëel en niet artificieel zijn; conform marktconforme huurprijs.

<small>🔗 WIB92 — art. 344 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Directievilla ter beschikking gesteld aan zaakvoerder
> _Aurelia Holding NV stelt een villa ter beschikking aan zaakvoerder Pieter. De woning is gemeubileerd. Niet-geïndexeerd kadastraal inkomen: 2.500 EUR. AJ 2026 — indexatiecoëfficient ~2,1763 (Cijferzakboekje raadplegen)._
>
> **Berekening:**
>
> - Stap 1 — Geïndexeerd KI = 2.500 × 2,1763 ≈ 5.441 EUR
> - Stap 2 — Basis-VAA = 5.441 × 100/60 × 2 = 5.441 × 3,333 ≈ 18.137 EUR/jaar
> - Stap 3 — Verhoging gemeubileerd × 5/3: 18.137 × 5/3 ≈ 30.228 EUR/jaar
> - Stap 4 — VAA op fiche 281.20 van Pieter: 30.228 EUR (bezoldigingen)
> - Stap 5 — Bij marginaal tarief 50 % + gemeente: PB-impact ~16.000 EUR netto-belasting
> - Stap 6 — Vergelijk werkelijke huurwaarde: indien marktconforme huur ~24.000 EUR/jaar zou bedragen — VAA forfait ligt hoger dan werkelijke huur → fiscaal nadelig
>
> → **Resultaat**: 30.228 EUR VAA per jaar voor de gemeubileerde directievilla. Voor de vennootschap blijven de afschrijvingen + intresten aftrekbaar (bezoldigingstheorie). Tot 2019 zou het VAA ongeveer twee keer lager geweest zijn voor dezelfde woning.
>
> **📒 Aankoop villa door Aurelia Holding NV (vereenvoudigd)**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 222 — Gebouwen | 400.000 |  |
> | 21 — Grond | 100.000 |  |
> | 440 — Leveranciers / 173 — Banklening |  | 500.000 |
>
> <small>🔗 KB/WIB92 — art. 18 §3 2° — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Werkelijke huurwaarde i.p.v. forfait gebruiken
> **Verkeerde assumptie**: Studenten gebruiken soms de marktconforme huurwaarde als VAA in plaats van het KI-gebaseerd forfait.
>
> **Kernpunt**: Het forfait is leidend (KB/WIB92 art. 18 §3). Alleen wanneer de werkelijke huurwaarde HOGER is dan het forfait, mag de fiscus zich op het hogere bedrag baseren — niet andersom. In de praktijk is het forfait sinds 2019 voor de meeste woningen HOGER dan de marktconforme huurwaarde, wat de fiscale aantrekkelijkheid van het regime verlaagde.
>
> <small>📖 KB/WIB92 — art. 18 §3 2° — _kb_</small>

> [!warning]- Oude factor 3,8 of 1,25 hanteren
> **Verkeerde assumptie**: Studenten leren soms nog 'KI ≤ 745 EUR → factor 1,25 / KI > 745 EUR → factor 3,8'.
>
> **Kernpunt**: Sinds 1 januari 2019 één UNIFORME factor 2 (KB/WIB92 art. 18 §3 2°, gewijzigd door wet 27 mei 2019). Het oude tweelagig-tarief is geschrapt na rechtspraak van het Grondwettelijk Hof. Bij examen: alleen factor 2 hanteren — Cijferzakboekje 2026.
>
> <small>📖 Wet 27 mei 2019 — art. 18 §3 2°-wijziging — _wettekst_ · KB/WIB92 — art. 18 §3 2° — _kb_</small>

> [!warning]- Gemeubileerd-verhoging vergeten
> **Verkeerde assumptie**: VAA-formule rechtstreeks op KI toepassen zonder te checken of de woning gemeubileerd ter beschikking is gesteld.
>
> **Kernpunt**: Bij gemeubileerde woning: verhoging × 5/3 op het basis-VAA. Verschil: een woning met KI 2.000 EUR onmubileerd ≈ 10.600 EUR VAA; gemeubileerd ≈ 17.667 EUR VAA. Vraag aan cliënt: zijn meubels, witgoed, gordijnen inbegrepen?
>
> <small>📖 KB/WIB92 — art. 18 §3 2° — _kb_</small>

> [!warning]- Geïndexeerd vs niet-geïndexeerd KI verwarren
> **Verkeerde assumptie**: De formule meteen toepassen op het niet-geïndexeerde KI dat bij de aankoopakte staat.
>
> **Kernpunt**: Eerst INDEXEREN met de AJ-coëfficient (~2,18 voor AJ 2026). Daarna pas × 100/60 × 2. Een niet-geïndexeerd KI van 1.500 EUR ≠ een geïndexeerd KI van 1.500 EUR — verschil van ruim 50 % op het einde-VAA.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Directiewoning-pakket fiscaal beoordelen

_De accountant die het loonpakket van een bedrijfsleider met directiewoning adviseert of de fiscale aangifte voorbereidt._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijkse VAA-berekening + fiche-vermelding

Op jaarafsluit: (1) opzoek niet-geïndexeerd KI in akte of via MyMinfin; (2) vermenigvuldig met AJ-indexatiecoëfficient (Cijferzakboekje); (3) × 100/60 × 2; (4) indien gemeubileerd × 5/3; (5) opnemen op fiche 281.20 (bedrijfsleider) of 281.10 (werknemer). Vergeet niet de eventuele cumulatie met VAA verwarming/elektriciteit indien werkgever ook nutsfacturen draagt.

<small>🔗 KB/WIB92 — art. 18 §3 2° — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Rebalancing-advies sinds wet 2019

Bestaande directiewoning-pakketten herevalueren. Door uniforme factor 2 + indexatie is het VAA voor middelgrote woningen vaak hoger dan een huurwaarde of een alternatief loon-in-cash. Mogelijke alternatieven: (1) split-rental (bedrijfsleider huurt zelf en de vennootschap betaalt huurvergoeding — fiscaal voordeliger maar anti-misbruik-risico); (2) verkoop van vennootschap-woning aan bedrijfsleider met lening; (3) afbouw richting cash-bezoldiging + privé-aankoop.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Bezoldigingstheorie — documenteren werkelijke prestaties

Voor de aftrekbaarheid van de kosten van een directiewoning in vennootschap: documenteer dat de totale beloning (cash + VAA + andere voordelen) verantwoord is door werkelijke prestaties van de bedrijfsleider. Houdt loonvergelijkingen aan met soortgelijke directiefuncties in de markt. Bij overdreven verhouding kost-woning vs prestaties: fiscus kan aftrekbaarheid betwisten (Cassatie 13/11/2017 — verworpen kosten 10 % à 100 %).

<small>🔗 WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Bedrijfsleider-bezoldigingsmix (overkoepelende advies-context) → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_
- ↪ Werknemer-loon → [[loon-en-payroll]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[werknemers-vergoedingen]]
### `vereist`
- [[bedrijfsleidersbezoldiging]] — VAA-woning maakt typisch deel uit van de bezoldigingsmix van een bedrijfsleider — bezoldigingstheorie nodig voor aftrekbaarheid in vennootschap.
### `vergelijkbaar_met`
- [[vaa-verwarming-en-elektriciteit]]
    - **Gelijkenissen**:
        - Beide forfaitaire VAA's onder KB/WIB92 art. 18 §3
        - Beide gecombineerd in klassieke directiewoning-pakketten
        - Beide leiden tot fiche-vermelding op 281.10/281.20
    - **Verschillen**:
        - VAA-woning: formule op KI × coëfficient — bedrag hangt af van vastgoed
        - Nutsvoorzieningen-VAA: vast forfait per element, afhankelijk van hoedanigheid (kaderlid/niet)
