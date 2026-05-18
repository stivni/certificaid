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
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/kostenanalyse-make-or-buy.json
gegenereerd_op: '2026-05-18'
---
# Make-or-buy-analyse 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


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



## In de praktijk

<h3 id="standaard-examen-valkuil">Standaard examen-valkuil</h3>

> [!tip]- Standaard examen-valkuil
> Studenten vergelijken de volledige kostprijs van zelf produceren met de offerteprijs. Dat is fout: gebruik de vermijdbare kost. Volledige kostprijs bevat namelijk overhead die ook na uitbesteden moet betaald worden (en dan op andere producten zou drukken). 🤖


## Zie ook

- **Vereist kennis van**: [[marginale-kostprijs]]
- **Vereist kennis van**: [[variabele-kosten]]
- **Wordt voorondersteld in** (1): [[sunk-cost]]
