---
title: Make-or-buy-analyse
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.taak.1
- 1.8.III.E
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/kostenanalyse-make-or-buy.json
gegenereerd_op: '2026-05-21'
---
# Make-or-buy-analyse 🔗

De make-or-buy-analyse vergelijkt de kost van zelf produceren met de kost van uitbesteden, gericht op de relevante kosten (vermijdbare kosten bij uitbesteden vs. inkoopprijs + transactiekost). Sunk costs en niet-vermijdbare overhead doen niet ter zake.



## Bouwstenen

### Relevante versus niet-relevante kosten 🤖

Relevant: kosten die verdwijnen bij uitbesteden (vermijdbare variabele kosten, vermijdbare vaste kosten zoals afdelingshoofd dat niet meer nodig is). Niet-relevant: sunk costs (al gemaakt) en niet-vermijdbare overhead (algemene directie, hoofdkantoor).

**Waarom?** Volledige kostprijs bevat niet-vermijdbare kosten die ook na uitbesteden blijven bestaan — gebruik die niet in vergelijking.



Yperse Werkplaats BV overweegt Spinnerij te outsourcen. Volledige kostprijs Spinnerij: € 1.450.000/jaar. Maar bij uitbesteden vervalt loon Spinnerij-personeel (€ 850.000) + onderhoudscontract (€ 80.000) + variabele wol-aankoop (€ 350.000) = € 1.280.000 vermijdbaar. De overige € 170.000 (toegerekende algemene overhead, afschrijving gebouw) blijft. Vergelijk dus € 1.280.000 met de offerteprijs van € 1.380.000 → eigen productie € 100.000 goedkoper.


### Kwalitatieve factoren 🤖

Naast cijfers: levertijd-betrouwbaarheid, kwaliteitscontrole, intellectueel eigendom, capaciteit-flexibiliteit, afhankelijkheid van leverancier.

**Waarom?** Beslissing puur op kostprijs is risico bij strategische componenten.



Voor Yperse Werkplaats BV is wol-spinnen mogelijk een strategisch differentiatie-element (eigen recept). Zelfs als uitbesteden € 100.000 goedkoper is, kan eigen productie aangewezen blijven om kwaliteit en differentiatie te behouden.



## Berekening

### Make-or-buy beslissings-stappen

*Vijf-stappen-protocol om de keuze tussen zelf produceren (make) en uitbesteden (buy) financieel te onderbouwen — inclusief opportuniteitskosten en lange-termijn-overwegingen.*

### 1. Identificeer relevante kosten

Lijst kosten die wél veranderen door de beslissing: variabele productiekosten, vermijdbare directe vaste kosten (extra personeel, gehuurde machine), opportuniteitskosten van de inzet van vrije capaciteit.

**🛠️ Hoe**:

Schrap niet-relevante kosten: gemeenschappelijke vaste kosten (huur productiehal die je niet kan verminderen door uitbesteding), sunk costs (al gemaakte investering in machines).

**Grondslag**: [[sunk-cost]] · [[opportuniteitskost]]

### 2. Bereken make-kost

Som van relevante kosten bij zelf produceren: variabel materiaal + variabele arbeid + vermijdbare vaste kosten + opportuniteitskost van de schaarse middelen (machine, mensen, ruimte).

**🛠️ Hoe**:

Pas op met indirecte kosten: alleen vermijdbare meetellen, niet de volledig toegerekende overhead. Tip: vergelijk de incrementele kost van de make-optie, niet de full-cost-rapportage.

**Grondslag**: [[directe-kosten]] · [[indirecte-kosten]]

### 3. Bereken buy-kost

Externe prijs van leverancier + nevenkosten (transport, inkoopopvolging, kwaliteitscontrole, voorraadopslag). Subtraheer eventueel vermeden interne kosten.

**🛠️ Hoe**:

Externe offerte als basis; voeg verborgen kosten toe: keuringen, retourbeheer, dependency op leverancier (extra voorraad als buffer).

**Grondslag**: Vakdoctrine

### 4. Vergelijk + check strategische factoren

Financiële vergelijking + niet-financiële afweging: knowhow-behoud, leveringszekerheid, kwaliteitscontrole, IP-bescherming, sociaal-impact (jobverlies). Make wordt verkozen wanneer make-kost ≤ buy-kost en strategische factoren neutraal of pro-make. Buy bij omgekeerd plaatje.

**🛠️ Hoe**:

Maak een tabel: make-kost vs. buy-kost + 4-6 niet-financiële criteria met gewichten of pro/contra-notities.

**Grondslag**: Vakdoctrine

### 5. Gevoeligheidsanalyse

Test hoe de uitkomst verandert bij wijziging van volume (uitbesteder geeft schaalvoordeel? eigen productie schaalt minder?), prijsverandering leverancier, capaciteitsbenutting (overcapaciteit → make goedkoper).

**🛠️ Hoe**:

Twee à drie scenario's: pessimistisch (volume daalt 20 %), basis, optimistisch. Identificeer break-even-volume tussen make en buy.

**Grondslag**: Vakdoctrine


## In de praktijk

<h3 id="standaard-examen-valkuil">Standaard examen-valkuil</h3>

> [!tip]- Standaard examen-valkuil
> Studenten vergelijken de volledige kostprijs van zelf produceren met de offerteprijs. Dat is fout: gebruik de vermijdbare kost. Volledige kostprijs bevat namelijk overhead die ook na uitbesteden moet betaald worden (en dan op andere producten zou drukken). 🤖


## Zie ook

- **Vereist kennis van**: [[marginale-kostprijs]]
- **Vereist kennis van**: [[variabele-kosten]]
- **Wordt voorondersteld in** (1): [[sunk-cost]]
