---
title: "Belasting op inverkeerstelling"
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
gegenereerd_uit: "data/concepten/records/belasting-inverkeerstelling.json"
---

_Regime_ · afk: **BIV**

## Definitie

De belasting op inverkeerstelling (BIV) is een eenmalige gewestelijke belasting die verschuldigd is bij de eerste inschrijving in België van een voertuig (auto, motorfiets, vliegtuig, boot) op naam van een belastingplichtige, of bij de overdracht/wijziging van titularis indien een nieuwe inschrijvingsaanvraag nodig is. Het tarief verschilt fundamenteel per gewest: Vlaanderen hanteert sinds 2012 een ecoboni-malus-systeem gebaseerd op CO2-uitstoot + brandstof + euronorm + leeftijd; Brussel en Wallonië hanteren een klassieke tabel gebaseerd op cilinderinhoud (PK/cc) en ouderdom van het voertuig.

<small>🔗 WIGB — Titel V — BIV — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Economisch: een 'aankoopbelasting' op voertuigen, geheven eenmalig bij eerste inschrijving van het voertuig op naam van de eigenaar. Voor een typische nieuwe wagen (benzine, 1.4 L, 4-5 PS-klasse) in Vlaanderen: tussen 100 en 1.000 EUR; voor een 'maluswagen' (hoge CO2, diesel pré-Euro 6): 2.000-10.000 EUR. Het Vlaamse ecoboni-malus-systeem stuurt actief de keuze richting milieuvriendelijke voertuigen (elektrische wagens: 0 EUR BIV). In Wallonië/Brussel is het tarief gematigder en stabieler maar minder ecologisch gestuurd. Het vroegere inkomenscriterium (BIV lager voor kleine inkomens) is afgeschaft.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Klassiek deel: budgettair — de eerste inschrijving van een wagen genereert eenmalig een fors bedrag voor het gewest. Modern (Vl): sturend instrument om de wagenpark-vergroening te versnellen. Het ecoboni-malus-systeem maakt nieuwe milieuonvriendelijke wagens duurder (malus) en milieuvriendelijke goedkoper of gratis (boni) — een vorm van Pigou-belasting op CO2-externaliteit.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIGB Titel V (federaal kader) + gewestelijke decreten (VCF Titel 2.4 voor Vlaanderen; decreet Wallonië; ordonnantie Brussel)

Vlaanderen herziet jaarlijks de CO2-grenzen en parameters van het ecoboni-malus-systeem. Brussel en Wallonië werken nog grotendeels met cc-tabel. Inkomenscriterium dat vroeger BIV deed dalen bij lage inkomens is afgeschaft.

**✅ Voor**
- 🔗 Iedere eerste inschrijving in België van een voertuig op naam van een belastingplichtige (natuurlijke of rechtspersoon). Ook: hertaxatie bij overdracht aan een nieuwe titularis (tenzij familievrijstelling).

**⛔ Uitsluitingen**
- 🔗 Vrijstellingen: voertuigen voor militair/diplomatiek gebruik; personen met handicap onder voorwaarden; oldtimers > 30 jaar (vlak forfait, niet de tabel); overdracht tussen echtgenoten of bloedverwanten in rechte lijn (familiale vrijstelling); elektrische voertuigen in Vlaanderen (BIV = 0 EUR sinds 2024 — controleer huidige status).

## Bouwstenen

### 🧮 Vlaamse formule: ecoboni-malus

BIV-Vl = basisbedrag (functie cilinderinhoud OF kW elektrisch) × correctiecoëfficiënt(CO2) × correctiecoëfficiënt(brandstof + euronorm) × ouderdomscorrectie. Hoe hoger CO2 + hoe slechter euronorm → malus (verhoging). Elektrisch + waterstof: 0 EUR. Sinds 2012 jaarlijks bijgesteld. Vooral CO2-component vermindert de BIV voor zuinige wagens en verhoogt ze fors voor 'maluswagens' (vroeger diesel, grote SUV's).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Klassieke cc-tabel (Brussel, Wallonië)

In Brussel en Wallonië wordt de BIV nog berekend volgens de klassieke tabel uit het WIGB: per schijf van cilinderinhoud (cc) of fiscale paardenkracht (PK), met een ouderdomsdegressie (oudere wagen = lagere BIV). Range typisch 61,5 EUR (kleine wagen, > 10 jaar) tot 4.957 EUR (grote benzine-/dieselwagen, nieuw).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ CO2-correctie (Vlaanderen)

Per gram CO2/km boven of onder een referentiewaarde (recent ca. 100 g voor benzine, 95 g voor diesel) wordt een correctiebedrag toegevoegd (malus) of afgetrokken (boni). De referentiewaarde wordt jaarlijks bijgesteld om de transitie naar lagere-CO2-wagens te volgen. Effect: tussen twee identieke voertuigen kan de BIV honderden EUR verschillen op basis van enkele grammen CO2.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- BIV en verkeersbelasting verwarren
> **Verkeerde assumptie**: BIV en jaarlijkse verkeersbelasting zijn dezelfde belasting met andere namen.
>
> **Kernpunt**: BIV = EENMALIGE belasting bij inschrijving (aankoop / overdracht). Verkeersbelasting = JAARLIJKS verschuldigd zolang het voertuig ingeschreven blijft. Beide zijn gewestelijk maar functioneel anders: BIV stuurt aankoopkeuze, verkeersbelasting stuurt gebruiksduur.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Tarieven over de gewesten heen veralgemenen
> **Verkeerde assumptie**: Een Vlaamse BIV-berekening geldt ook voor Brussel of Wallonië.
>
> **Kernpunt**: De drie gewesten hanteren totaal verschillende methoden: Vlaanderen ecoboni-malus (CO2 + euronorm), Brussel/Wallonië klassieke cc-tabel. De gewestelijke woonplaats van de titularis bepaalt het toepasselijke regime. Voor identiek voertuig kan BIV honderden EUR verschillen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Vennootschap met wagenpark

_De accountant die wagenparkbeheer en fiscale optimalisatie begeleidt._

#### 💰 Fiscaal adviseur

##### 👣 BIV als kost in TWR

BIV is een fiscaal aftrekbare kost voor de vennootschap. Bij voertuigkeuze (firmawagen): vergelijk de totale wagenkost (TWR = total cost of ownership) inclusief BIV, jaarlijkse verkeersbelasting, BTW-aftrek (gedeeltelijk geblokkeerd voor personenwagens), CO2-bijdrage RSZ, VAA werknemer. Een 'maluswagen' kost niet enkel meer BIV maar typisch ook meer VAA en RSZ.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Verkeersbelasting (jaarlijks) → [[verkeersbelasting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[lokale-en-regionale-belastingen]]
### `vergelijkbaar_met`
- [[verkeersbelasting]]
    - **Gelijkenissen**:
        - Beide zijn gewestelijke voertuigbelastingen
        - Beide gebaseerd op cilinderinhoud / kW (klassiek)
    - **Verschillen**:
        - BIV: éénmalig, bij inschrijving
        - Verkeersbelasting: jaarlijks, zolang ingeschreven
    - ⚠️ **Verwarringsrisico**: Cliënten vragen vaak 'wat ben ik voor mijn wagen verschuldigd?' — duidelijk maken welk van beide bedragen het is.
