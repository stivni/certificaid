---
title: "Beroepskosten"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.VI.B
  - 2.2.taak.3
  - 2.3.II.D
  - 2.3.II.E
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/beroepskosten.json"
---

_Regime_ · ook: aftrekbare beroepskosten · frais professionnels

## Definitie

Beroepskosten zijn de uitgaven die de belastingplichtige in het belastbare tijdperk werkelijk heeft gedaan of gedragen om belastbare beroepsinkomsten te verkrijgen of te behouden, en waarvan hij de echtheid en het bedrag verantwoordt door bewijsstukken (art. 49 WIB92). Ze worden afgetrokken van het brutobedrag van het beroepsinkomen om het belastbaar netto-beroepsinkomen te bepalen. De wet kent zowel werkelijk-bewezen aftrek (art. 49-52 WIB) als forfaitaire aftrek (art. 51 WIB voor sommige PB-categorieën). Aftrekbeperkingen (art. 53, 65-66, 198) gelden gelijktijdig.

<small>📖 WIB92 — art. 49 — _wettekst_</small>

## Substantie

Beroepskosten zijn één van de drie hefbomen in de PB- én VenB-grondslag (naast vrijstellingen en aftrekken). De vier voorwaarden van art. 49 vormen één toets, maar de wetgever heeft daarboven een 'opsommend' systeem gebouwd: art. 52 noemt voorbeelden van wat zeker aftrekbaar is, art. 53 verbiedt categorieën uitgaven (persoonlijke uitgaven, geldboeten, niet-bewezen autokosten...), en art. 65-66 + 198 leggen kwantitatieve aftrekbeperkingen op. In PB kiest de belastingplichtige per categorie tussen forfait (art. 51) en werkelijke kosten. In VenB bestaat geen forfait — alleen werkelijke kosten, en niet-aftrekbare gedeelten worden via de Eerste Bewerking 'verworpen uitgaven' (code 1200-reeks aangifte) bij de boekhoudkundige winst opgeteld.

<small>🔗 WIB92 — art. 49, 51, 52, 53, 66, 198 — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — codes 1200-1240 — _aangifte_</small>

## Rationale

Het principe is symmetrie: alleen netto-arbeidsinkomen wordt belast. De vier-voorwaarden-test van art. 49 voorkomt dat private uitgaven verkapt als beroepsuitgaven worden afgetrokken. De aftrekbeperkingen (50 % auto, 30 % restaurant) zijn beleidsinstrumenten: ze ontmoedigen luxe-uitgaven, verzachten privé/beroep-vermenging, en compenseren BTW-aftrekbeperkingen die niet integraal het beroepsmatig karakter weerspiegelen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 49-66bis (PB); art. 183 + 195-198bis (VenB-koppeling)

**✅ Voor**
- 📖 Bij elke berekening netto belastbaar beroepsinkomen (PB) of belastbare winst (VenB).

**⚠️ Risico**
- 🔗 Bij gebrek aan bewijsstukken: forfait of administratieve raming (ambtshalve aanslag art. 342 WIB). Bij gemengd gebruik zonder onderbouwing: verwerping deelaftrek + boetes.

## Bouwstenen

### 📜 Vier-voorwaarden-test art. 49 WIB

Een uitgave is aftrekbaar als beroepskost als cumulatief: (1) causaal verband — gedaan in functie van de beroepsactiviteit; (2) tijdperk — werkelijk betaald of gedragen in het belastbare tijdperk (of als zekere en vaststaande schuld geboekt); (3) bewijs — echtheid én bedrag verantwoord door bewijsstukken (factuur, contract, fiche) of subsidiair door andere bewijsmiddelen behalve de eed; (4) finaliteit — gedaan om belastbare inkomsten te verkrijgen of te behouden.

<small>📖 WIB92 — art. 49 — _wettekst_</small>

### ↪️ Niet-aftrekbare uitgaven art. 53 WIB

Art. 53 sluit uitdrukkelijk uit (catalogus van 23+ rubrieken): persoonlijke uitgaven (huur woning, onderwijs gezin), personenbelasting + voorheffingen, aanvullende gemeentebelasting, geldboeten van alle aard (transactioneel, administratief, strafrechtelijk), kledij die niet specifiek beroepskledij is, kosten jacht/visvangst/pleziervaartuigen, kosten 'op onredelijke wijze' boven beroepsbehoeften, ten-laste-genomen verliezen van vennootschappen (behoudens bedrijfsleidersuitzondering).

<small>📖 WIB92 — art. 53 — _wettekst_</small>

### 📜 Aftrekbaarheidspercentages — cascade

Wettelijke aftrek-percentages voor specifieke uitgaven (gemeenschappelijk PB + VenB):

<small>📖 WIB92 — art. 53-8°, 53-8°bis, 53-9°, 66 — _wettekst_</small>

### ⚙️ Keuze forfait vs werkelijke kosten (PB)

In de PB kiest de belastingplichtige per categorie inkomsten (werknemer, bedrijfsleider, baten, winst) tussen forfait (automatisch, art. 51) en werkelijke kosten (verantwoorde uitgaven, art. 49). De keuze gebeurt impliciet: vermeldt de belastingplichtige werkelijke kosten in de aangifte (rubriek 'eigen werkelijke beroepskosten') én is het bedrag hoger dan het forfait, dan worden de werkelijke kosten toegepast. Anders: forfait. Per categorie kan onafhankelijk worden gekozen. In VenB bestaat geen forfait.

<small>📖 WIB92 — art. 49, 51 — _wettekst_ · aangifte-PB-2025-bezoldigingen — code 1258, 1271 — _aangifte_</small>

### ⚙️ Boekhoudkundige verwerking — klasse 6 + verworpen uitgaven (VenB)

In een vennootschap worden alle uitgaven boekhoudkundig geboekt op klasse 6 (Kosten) — de boekhouding bepaalt het commerciële resultaat. Fiscaal worden niet-aftrekbare gedeelten via de Eerste Bewerking op de aangifte VenB als 'verworpen uitgaven' (code 1200-reeks) bij de winst toegevoegd. Voorbeelden: niet-aftrekbaar deel autokosten (code 1205), niet-aftrekbaar deel VAA-autokosten gelijk aan VAA (code 1206), niet-aftrekbare restaurantkosten 31 % (code 1208), niet-aftrekbare receptiekosten 50 % (code 1209), boeten (code 1207).

<small>📖 aangifte-VenB-2025-verworpen-uitgaven — codes 1205-1209, 1215 — _aangifte_ · WIB92 — art. 198 — _wettekst_</small>

### 📜 Afschrijvingen (art. 61 WIB)

Afschrijvingen zijn beroepskosten naargelang ze gegrond zijn op de aanschaffings- of beleggingswaarde, noodzakelijk zijn en samengaan met een waardevermindering die zich werkelijk heeft voorgedaan in het belastbare tijdperk. Aanschaffingswaarde = aanschaffingsprijs, vervaardigingsprijs of inbrengwaarde (volgens boekhoudwetgeving). Afschrijvingsritme: lineair, degressief (art. 64), of versneld bij KMO (art. 196/197 WIB).

<small>📖 WIB92 — art. 61 — _wettekst_</small>

## Voorbeelden

> [!example]- Zelfstandige arts — restaurant- en receptiekosten in jaaraangifte
> _Vrijberoeper besteedt in jaar X: € 4.000 restaurant met klanten + € 1.500 receptie (productlancering) + € 500 reclamepennen met logo. Werkt in PB-baten._
>
> **Berekening:**
>
> Aftrekbaarheid per uitgave:
>
> | Uitgave | Bedrag | Aftrekbaar | Berekening |
> |---|---|---|---|
> | Restaurantkosten | € 4.000 | 69 % | 4.000 × 0,69 = **€ 2.760** |
> | Receptiekosten | € 1.500 | 50 % | 1.500 × 0,50 = **€ 750** |
> | Reclamepennen (opvallend + logo) | € 500 | 100 % | 500 × 1,00 = **€ 500** |
> | **Totaal aftrekbaar** | € 6.000 bruto | | **€ 4.010** |
> | Niet-aftrekbaar gedeelte | | | € 1.240 + € 750 = **€ 1.990** |
>
> In de aangifte PB worden alleen de aftrekbare bedragen meegenomen in 'werkelijke beroepskosten'. Bij keuze forfait (28,7 % / 10 % / 5 % / 3 % op schijven) vervalt deze detaillering.
>
> <small>🔗 WIB92 — art. 53-8°, 53-8°bis — _wettekst_</small>

> [!example]- BV — boekingen klasse 6 + verworpen uitgaven aangifte
> _Een BV heeft in jaar X: € 10.000 restaurantkosten + € 5.000 boetes (verkeer) + € 60.000 brutobezoldiging zaakvoerder + € 8.000 autokosten op een wagen 165 g CO2/km._
>
> Boekhoudkundige boekingen (klasse 6 — alle uitgaven 100 % geboekt):
>
> | Rekening | Omschrijving | Debet | Credit |
> |---|---|---|---|
> | 6131 | Restaurantkosten | 10.000 | |
> | 64 | Andere bedrijfskosten — geldboeten | 5.000 | |
> | 618 | Bezoldigingen bestuurders | 60.000 | |
> | 6402 | Brandstof + onderhoud voertuig | 8.000 | |
> | | aan 5500 Bank / 440 Lev. | | 83.000 |
>
> **Berekening:**
>
> Fiscale correctie via verworpen uitgaven (Eerste Bewerking VenB):
>
> | Uitgave | Boekhoudkundig | Aftrekbaar | Verworpen uitgave | Aangifte VenB code |
> |---|---|---|---|---|
> | Restaurantkosten 10.000 | 10.000 | 6.900 (69 %) | **3.100** | 1208 |
> | Geldboeten 5.000 | 5.000 | 0 | **5.000** | 1207 |
> | Autokosten 8.000 (CO2 165 → ca. 50 % aftrek art. 198bis) | 8.000 | 4.000 | **4.000** | 1205 |
> | Bezoldiging bestuurder 60.000 | 60.000 | 60.000 | 0 | — |
> | **Totaal verworpen uitgaven** | | | **€ 12.100** | |
>
> Gevolg: belastbare winst VenB = boekhoudkundige winst + € 12.100 (vóór andere bewerkingen).
>
> <small>🔗 WIB92 — art. 53-6°, 53-8°bis, 198, 198bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — codes 1205, 1207, 1208 — _aangifte_</small>

> [!example]- Loontrekkende — forfait vs werkelijke kosten
> _Werknemer bruto € 50.000, woont 40 km van werk (10.000 km woon-werk/jr in personenauto), kantoor aan huis 1 dag/week (€ 1.200 jaar), IT/telefoon € 400/jr._
>
> **Berekening:**
>
> Vergelijking:
>
> | Optie | Berekening | Bedrag |
> |---|---|---|
> | Forfait art. 51-1° | 50.000 × 30 % = 15.000, begrensd op € 2.950 (niet-geïnd.) | **€ 2.950** |
> | Werkelijke kosten | woon-werk 10.000 km × € 0,15 = 1.500 + kantoor 1.200 + IT 400 | **€ 3.100** |
>
> → Werkelijke kosten gunstig (€ 150 meer aftrek). Aangifte: code 1258-03 (werkelijke kosten — sociale bijdr. niet ingehouden) en code 1271-87 (rubriek A.21 andere beroepskosten). Cliënt moet alle bewijsstukken (kilometerstaten, facturen, energieafrekening kantoor) bewaren minstens 7 jaar.
>
> <small>🔗 WIB92 — art. 49, 51-1°, 66-2° (woon-werk forfait 0,15 €/km) — _wettekst_ · aangifte-PB-2025-bezoldigingen — codes 1258, 1271 — _aangifte_</small>

## Valkuilen

> [!warning]- Boekhoudkundig 100 % geboekt = fiscaal 100 % aftrekbaar (mis)
> **Verkeerde assumptie**: Wat op klasse 6 staat, is automatisch aftrekbaar in de aangifte VenB.
>
> **Kernpunt**: De boekhouding boekt àlle uitgaven 100 % in klasse 6 — fiscaal moet je via de Eerste Bewerking de niet-aftrekbare gedeelten als 'verworpen uitgaven' (codes 1200-reeks) bij de winst optellen. Het commerciële resultaat is niet hetzelfde als de belastbare winst.
>
> <small>🔗 WIB92 — art. 183, 198 — _wettekst_</small>

> [!warning]- VAA-autokosten dubbele correctie
> **Verkeerde assumptie**: Wanneer een wagen met VAA wordt verstrekt, hoeven enkel de gewone autokosten te worden gecorrigeerd via art. 198bis.
>
> **Kernpunt**: Bij een wagen met VAA moet een vennootschap dubbel corrigeren: (1) niet-aftrekbaar deel autokosten op basis van CO2-formule (code 1205); (2) bovendien 17 % (of 40 % bij brandstofkostvergoeding) van het VAA-bedrag als verworpen uitgave (code 1206 — art. 198 § 1, 9° WIB).
>
> <small>📖 WIB92 — art. 198 § 1, 9°, 198bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1206 — _aangifte_</small>

> [!warning]- Forfait + werkelijke kosten cumulatie
> **Verkeerde assumptie**: Je kunt het forfait toepassen én daarbovenop nog specifieke werkelijke uitgaven (bv. autokosten woon-werk) claimen.
>
> **Kernpunt**: De keuze is exclusief per inkomenscategorie: óf het forfait (art. 51) dat alle beroepskosten dekt, óf werkelijke kosten waarin je àlles afzonderlijk verantwoordt. Uitzondering: het woon-werk-forfait van € 0,15/km onder art. 66-2° kan ook bij forfaitkeuze worden geclaimd voor specifieke beroepsverplaatsingen — niet voor woon-werk zelf.
>
> <small>🔗 WIB92 — art. 51, 66 — _wettekst_</small>

## Speelruimtes

### 🎚️ Forfait of werkelijke kosten (PB)

## Accountant-perspectieven

### Boekhouder/fiscaal — VenB-aangifte

_De stagiair moet 100 % geboekte kosten splitsen naar aftrekbaar deel + verworpen uitgaven via codes 1200-reeks._

#### 💰 Fiscaal adviseur

##### 👣 Cascade verworpen uitgaven (Eerste Bewerking)

**Substantie**: (1) Neem boekhoudkundige winst vóór belastingen. (2) Loop klasse 6-uitgaven door en filter beperkt-aftrekbare items (restaurant 31 % verwerpen, recepties 50 %, autokosten CO2-formule, VAA-autokosten 17 % of 40 %, geldboeten 100 %, jacht/pleziervaart 100 %). (3) Tel deze gedeelten op tot 'verworpen uitgaven' (totaal codes 1200-reeks). (4) Voeg bij belastbare winst-Eerste-Bewerking. (5) Documenteer in werkdossier met factuur-verwijzingen.

<small>🔗 WIB92 — art. 198, 198bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — _aangifte_</small>

### Fiscaal — PB-aangifte werknemer/bedrijfsleider

_Beslissing forfait of werkelijk per cliënt — pro forma berekening van beide om gunstigste te kiezen._

#### 💰 Fiscaal adviseur

##### 👣 Pro forma beide opties berekenen

**Substantie**: (1) Bereken theoretisch werkelijke kosten: woon-werk (km × € 0,15 of bewezen werkelijke autokosten), thuiswerkruimte, IT, opleiding. (2) Bereken forfait (% × bruto na RSZ, begrensd). (3) Kies hogere. (4) Bij werkelijke kosten: verzamel alle bewijsstukken in dossier. (5) Vul codes 1258 + 1271 (werknemer) of overeenkomstige codes vak XVI (bedrijfsleider) in.

<small>🔗 WIB92 — art. 49, 51, 66 — _wettekst_ · aangifte-PB-2025-bezoldigingen — _aangifte_</small>

## Verder lezen (scope-out)

- → Werknemersbezoldiging als beroepsinkomen waarop kosten aftrekbaar → [[werknemersbezoldiging]] _(moet-verwijzen)_
- → Verworpen uitgaven cascade VenB → [[verworpen-uitgaven]] _(moet-verwijzen)_
- → Autokosten + CO2-aftrekbeperking (mobiliteit-cluster) → [[autokosten]] _(moet-verwijzen)_
- → Beroepsinkomen-overzicht → [[beroepsinkomen-pb]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
- [[vennootschapsbelasting]]
### `triggert`
- [[verworpen-uitgaven]]
### `vergelijkbaar_met`
- [[verworpen-uitgaven]]
    - **Gelijkenissen**:
        - beide bewerkingen op fiscale grondslag
        - beide in WIB art. 53/198 verankerd
    - **Verschillen**:
        - beroepskosten = aftrek toegestaan, optimalisatie via volledige verantwoording
        - verworpen uitgaven = corrigerende toevoeging bij VenB-grondslag, gericht op niet-aftrekbare gedeelten
    - ⚠️ **Verwarringsrisico**: Bij vennootschap zijn beide kanten van dezelfde medaille — boeking 100 % in klasse 6 leidt tot zowel aftrek (deel) als verworpen uitgave (rest).
