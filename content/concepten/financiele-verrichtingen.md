---
title: Financiële verrichtingen (kosten + opbrengsten)
tags:
- concept
- fenomeen
- po-1-1
linked_anchors:
- 1.1.II.O
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: fenomeen
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/financiele-verrichtingen.json
gegenereerd_op: '2026-05-17'
---
# Financiële verrichtingen (kosten + opbrengsten) ⚖️

> [!summary] Korte inhoud
> **Kosten en opbrengsten** uit de **financiële activiteit** van de onderneming: intresten op leningen en deposito's, kosten op leningen, opbrengsten/verliezen op effecten en deelnemingen, wisselkoersverschillen.

> [!info] Behoort tot: [[resultatenrekening]]

**Kosten en opbrengsten** uit de **financiële activiteit** van de onderneming: intresten op leningen en deposito's, kosten op leningen, opbrengsten/verliezen op effecten en deelnemingen, wisselkoersverschillen. Klasse 65 (financiële kosten) en 75 (financiële opbrengsten). Strikt gescheiden van het bedrijfsresultaat zodat de gebruiker operationele en financiële prestatie kan onderscheiden. Het verschil tussen klasse 75 en 65 = **financieel resultaat**.

_Bron: MAR klasse 65 + 75_


## Bouwstenen

### Klasse 65 — Financiële kosten ⚖️

(650) Kosten van schulden (intresten leningen, krediettoeslagen), (651) Waardeverminderingen op vlottende activa andere dan voorraden, (652) Minderwaarden op realisatie van vlottende activa, (653) Disconto kosten bij wissels, (654) Wisselkoersverliezen, (657) Diverse financiële kosten.

**Waarom?** Aparte rubriek voor de prijs van financiering en wisselkoersrisico. Helpt om operationele performance te scheiden van schuldlastdruk.

**Voorbeeld**: Uitgeverij Ukkel NV betaalt jaarlijks € 28.500 intrest op € 685.000 hypothecaire lening (4,16 %). Boeking: Debet 650 Intresten op leningen € 28.500 / Credit 550 Bank € 28.500.

_Grondslag: MAR klasse 65_

### Klasse 75 — Financiële opbrengsten ⚖️

(750) Opbrengsten van financiële vaste activa (typisch dividenden van deelnemingen), (751) Opbrengsten van vlottende activa (rente op deposito's, geldbeleggingen), (752) Diverse financiële opbrengsten (terugname waardeverminderingen, meerwaarden op realisatie effecten), (754) Wisselkoerswinsten.

**Waarom?** Symmetrische tegenhanger van klasse 65. Dividend van een deelneming staat in 750, niet in 70 omzet — duidelijk gescheiden van de operationele cyclus.

**Voorbeeld**: Aurelia Holding NV ontvangt dividend van Brugse Brouwerij BV € 80.000. Boeking: Debet 550 Bank € 80.000 / Credit 7501 Opbrengsten van deelnemingen in verbonden ondernemingen € 80.000.

_Grondslag: MAR klasse 75_

### Wisselkoersverschillen (654 / 754) ⚖️

Bij vorderingen of schulden in vreemde valuta ontstaan wisselkoersverschillen tussen contractdatum en betalingsdatum (of balansdatum). Gerealiseerde verschillen direct in resultaat (654/754). Niet-gerealiseerde verschillen op balansdatum: voorzichtigheidsbeginsel — negatieve in resultaat, positieve in toelichting.

**Waarom?** Wisselkoersrisico is geen operationeel maar financieel risico; aparte boeking maakt het zichtbaar voor analyse.

**Voorbeeld**: Uitgeverij Ukkel NV heeft een Britse vordering £ 50.000 (geboekt aan 1,20 = € 60.000) maar bij ontvangst is koers 1,15 → ontvangen € 57.500. Wisselkoersverlies € 2.500 op rekening 654.

_Grondslag: MAR + KB WVV art. 3:39_


## In de praktijk

<h3 id="intrestkost-vs-hoofdsom-betaling">Intrestkost vs hoofdsom-betaling</h3>

> [!tip]- Intrestkost vs hoofdsom-betaling
> Bij annuïtaire afbetaling van een lening betaal je elke maand een vast bedrag dat bestaat uit intrest (klasse 65) + aflossing hoofdsom (vermindering rekening 17/42). Aflossing hoofdsom is GEEN kost — alleen intrest is. ⚖️

> [!tip]- Herkennen op het examen
> Examen: maandannuïteit € 4.500, waarvan € 1.200 intrest, € 3.300 aflossing → € 1.200 op klasse 65, € 3.300 vermindert rekening 173.


## Valkuilen

> [!warning]- Aflossing van de hoofdsom van een lening is GEEN financiële kost — het vermindert enkel de schuld
> ⚠️ Aflossing van de hoofdsom van een lening is GEEN financiële kost — het vermindert enkel de schuld. Alleen intrest hoort in klasse 65. ⚖️
>
> _Bron: MAR_


> [!warning]- Dividenden ONTVANGEN = financiële opbrengst (klasse 750)
> ⚠️ Dividenden ONTVANGEN = financiële opbrengst (klasse 750). Dividenden UITGEKEERD = winstbestemming via rekening 694, NIET klasse 65. Andere kant van de balans. ⚖️
>
> _Bron: MAR klasse 6 vs 7_



## Bronnen

[^1]: `MAR-ondernemingen__art_6`
[^2]: `MAR-ondernemingen__art_7`
