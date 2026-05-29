---
title: "Verkeersbelasting"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.7.I.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/verkeersbelasting.json"
---

_Regime_ · ook: jaarlijkse verkeersbelasting

## Definitie

De verkeersbelasting is een jaarlijkse gewestelijke belasting verschuldigd door de titularis (inschrijver) van een motorvoertuig (auto, motorfiets, vrachtwagen, bus, autocar, aanhangwagen) zolang dat voertuig in België is ingeschreven. Het tarief verschilt per gewest: Vlaanderen heeft sinds 2016 een gemoduleerd systeem dat CO2-uitstoot, euronorm en brandstof in rekening brengt; Brussel en Wallonië hanteren nog grotendeels de klassieke tabel op basis van cilinderinhoud (cc/PK) of nuttige last. Voor voertuigen ≥ 25 jaar geldt een 'oldtimer-tarief': een vlak en sterk verlaagd forfait.

<small>🔗 WIGB — Titel II — Verkeersbelasting — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Voor een typische personenwagen (benzine, 1.4 L, recente euronorm) in Vlaanderen: 250-400 EUR per jaar. Voor een 'maluswagen' (diesel, oudere euronorm, hoge CO2): 700-1.500 EUR per jaar. Voor elektrische wagens: 0 EUR (volledige vrijstelling in Vlaanderen sinds 2016, beleidsbeslissing). Brussel/Wallonië hanteren tabellen rond 200-700 EUR voor courante wagens. Bedrijfswagens worden door de werkgever betaald; impact op TWR (total wagenkost) bij wagenkeuze. Voertuigen ≥ 25 jaar betalen een 'oldtimer-tarief' (Vl ca. 41 EUR; Wa/Br vergelijkbaar laag) onder voorwaarde van beperkt gebruik.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Klassiek: gebruikersbelasting voor het openbaar wegennet ('wie gebruikt, betaalt'). Modern (Vl): sturend instrument om ecologische voertuigkeuze te stimuleren — CO2-component verhoogt voor vervuilende wagens, vrijstelling voor elektrische wagens. Oldtimer-tarief: erkenning dat ≥ 25 jaar oude voertuigen geen 'dagelijks vervoer' meer zijn en bescherming van het historische erfgoed.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIGB Titel II (federaal kader) + VCF Titel 2.2 (Vl) + gewestelijke decreten Wallonië en Brussel

Volledig gewestelijk sinds zesde staatshervorming. Vlaamse hervorming met ecoscore-tarief 2016. Brussel en Wallonië onderzoeken vergelijkbare CO2-gestuurde hervormingen maar hanteren nog grotendeels klassieke tabel.

**✅ Voor**
- 🔗 Iedere natuurlijke of rechtspersoon op wiens naam een motorvoertuig is ingeschreven bij de DIV (Directie Inschrijving Voertuigen). Belasting volgt de inschrijving — eens een voertuig 'uit verkeer genomen' is en geschrapt, vervalt de belasting pro rata.

**⛔ Uitsluitingen**
- 🔗 Vrijstellingen: elektrische voertuigen (Vl: volledig vrijgesteld; Wa/Br: gedeeltelijk); personen met handicap onder voorwaarden; voertuigen voor militair/diplomatiek gebruik; voertuigen ≥ 25 jaar genieten oldtimer-tarief (geen vrijstelling maar sterk verminderd forfait).

## Bouwstenen

### 📜 Vlaams tarief personenwagen (gemoduleerd)

Vlaams systeem (sinds 2016): basisbedrag (functie cilinderinhoud cc OF kW elektrisch) × correctiecoëfficiënt(CO2) × correctiecoëfficiënt(brandstof + euronorm). Elektrisch: vrijstelling (basisbedrag × 0). Diesel + oude euronorm: malus tot 1,5× basis. Recente benzine zuinige wagen: licht verlaagd.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Klassiek tarief Brussel/Wallonië

In Brussel en Wallonië wordt het tarief nog grotendeels bepaald door de cc-tabel uit het WIGB: range 79-4.000 EUR/jaar afhankelijk van cilinderinhoud, leeftijd, en brandstof. Slechts beperkte CO2-correctie. Voor vrachtwagens: nuttige last als basis.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Oldtimer-tarief (voertuigen ≥ 25 jaar)

Voor voertuigen ≥ 25 jaar wordt een vlak verminderd tarief toegepast (Vl ca. 41 EUR/jaar incl. aanvullende verkeersbelasting — exact bedrag in Cijferzakboekje). Voorwaarden: voertuig in originele staat + beperkt gebruik (geen woon-werk, geen beroepsgebruik) + bewijs ouderdom. Voorheen was de drempel 30 jaar; verlaagd naar 25 jaar voor enkele jaren in Vlaanderen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- BIV en verkeersbelasting verwarren
> **Verkeerde assumptie**: BIV en jaarlijkse verkeersbelasting zijn dezelfde belasting.
>
> **Kernpunt**: BIV = EENMALIG bij inschrijving (aankoop / overdracht). Verkeersbelasting = JAARLIJKS zolang het voertuig ingeschreven blijft. Een voertuig betaalt typisch beide: eenmaal BIV, daarna elk jaar verkeersbelasting.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Tarief Vlaanderen veralgemenen naar Brussel/Wallonië
> **Verkeerde assumptie**: Het Vlaamse ecoscore-tarief geldt overal in België.
>
> **Kernpunt**: Verkeersbelasting is gewestelijk en de drie gewesten hanteren verschillende formules. Brussel/Wallonië rekenen nog op cilinderinhoud-basis. Bij verhuis naar ander gewest verandert de jaarlijkse verkeersbelasting.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Vennootschap met wagenpark

_De accountant die wagenparkfiscaliteit becijfert._

#### 💰 Fiscaal adviseur

##### 👣 Verkeersbelasting in wagenkeuze-analyse

Bij wagenkeuze: verkeersbelasting opnemen in de TCO/TWR-vergelijking. Elektrisch heeft 0 EUR verkeersbelasting (Vl) — significant verschil over 5 jaar leasing. Diesel + oudere euronorm: malus — kan een wagen € 5.000-10.000 duurder maken over leasingsperiode. Combinatie met BIV-malus, VAA-kost werknemer, BTW-aftrekbeperking levert het volledige plaatje op.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Belasting-inverkeerstelling (eenmalig) → [[belasting-inverkeerstelling]] _(moet-verwijzen)_
- ↪ Autokosten-fiscaal (bedrijfsauto) → [[autokosten]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[lokale-en-regionale-belastingen]]
### `vergelijkbaar_met`
- [[belasting-inverkeerstelling]]
    - **Gelijkenissen**:
        - Beide zijn gewestelijke voertuigbelastingen
        - Beide gebaseerd op cilinderinhoud / kW (klassiek) of CO2 (Vl modern)
    - **Verschillen**:
        - BIV: éénmalig bij inschrijving
        - Verkeersbelasting: jaarlijks zolang ingeschreven
    - ⚠️ **Verwarringsrisico**: Klassieke vraag van cliënten — duidelijk onderscheiden in advies.
