---
title: Informatiesysteem van de onderneming
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.II.B
- 1.7.II.C
- 1.7.II.D
- 1.7.II
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/informatiesysteem-onderneming.json
gegenereerd_op: '2026-05-18'
---
# Informatiesysteem van de onderneming 🤖

Het informatiesysteem (boekhoud-IT, ERP, rapportagestructuren) is in PO 1.7 een aparte invalshoek omdat IC-effectiviteit erop staat of valt. Voor de stagiair komt dit terug in elke audit-opdracht: ISA 315 verplicht hem om vóór risk assessment het informatiesysteem te doorgronden. In adviesopdrachten is dit waar 'IT-general-controls' binnenkomen — toegangsbeheer, change management, back-ups. Examen-vragen testen de koppeling IS ↔ COSO-component 'informatie en communicatie'.

> [!summary] Korte inhoud
> Het informatiesysteem is het geheel van procedures, mensen, software en hardware dat data in een onderneming verzamelt, verwerkt, opslaat en distribueert.

> [!info] Behoort tot: [[interne-controle]]

Het informatiesysteem is het geheel van procedures, mensen, software en hardware dat data in een onderneming verzamelt, verwerkt, opslaat en distribueert. Voor interne controle is het cruciaal: zonder betrouwbare informatie kan het management niet sturen, kan de boekhouding niet kloppen en kan de externe auditor niet steunen op de cijfers.


## Bouwstenen

### Vier IS-functies — initiëren, registreren, verwerken, rapporteren ⚖️

Het informatiesysteem van de financiële verslaggeving doorloopt vier functies: (1) transacties initiëren (bv. inkooporder), (2) registreren (bv. boeking ontvangst), (3) verwerken (matching, validatie, journaalpost), (4) rapporteren (saldi naar grootboek, jaarrekening). Elke functie heeft eigen controle-aangrijpingspunten.

**Waarom?** Voor risk assessment (ISA 315) splitst de auditor het systeem in deze vier functies om risico's per fase in te schatten en application controls te identificeren.


**In de praktijk**: Stagiair-oefening: voor de aankoopcyclus van Yperse Werkplaats BV, benoem per functie één application control (initiëren: 4-ogen-goedkeuring boven € 5.000; registreren: 3-way-match bestelbon-ontvangst-factuur; verwerken: automatische BTW-verdeling; rapporteren: maand-afsluitings-controle).


_Grondslag: ISA 315 (herzien-2019) Bijlage 3 §15_

### Wat het informatiesysteem doet voor de financiële verslaggeving ⚖️

Het IS van de financiële verslaggeving initieert, registreert, verwerkt en rapporteert transacties — en verzorgt verantwoording over activa, passiva en eigen vermogen. Ook: omgaan met 'doorbroken' interne beheersing (override) en informatie verzamelen voor toelichtingen.

**Waarom?** Begrip van deze rol is voorwaarde om risico's op het niveau van beweringen in te schatten.




_Grondslag: ISA 315 (herzien-2019) Bijlage 3 §15_

### Application controls versus IT-general-controls 🤖

Application controls = controles binnen één applicatie (validatieregels, autorisatieworkflows). IT-general-controls = controles op de IT-omgeving zelf (toegangsbeheer, change management, back-up).

**Waarom?** Geen application control werkt zonder werkende IT-general-controls — een rolverdeling in een ERP is zinloos als iedereen admin-rechten heeft.


**In de praktijk**: Bij IC-review: vraag aan IT-verantwoordelijke of er een gedocumenteerd change-management-proces is. 'Iedereen mag wijzigen' = rode vlag.


_Grondslag: ISA 315 (herzien-2019)_

### Kwaliteit van informatie bepaalt sturing en rapportering ⚖️

De kwaliteit van informatie beïnvloedt zowel managementbeslissingen als betrouwbaarheid van financiële verslagen — slechte data leidt tot fout management én fouten in de cijfers.

**Waarom?** De relatie informatiesysteem ↔ COSO-component 4 is bidirectioneel: IS levert info, communicatie zorgt dat ze tot de juiste mensen geraakt.




_Grondslag: ISA 315 Bijlage 3 §17_


## In de praktijk

<h3 id="drie-soorten-stromen-1-7-ii-c">Drie soorten stromen (1.7.II.C)</h3>

> [!tip]- Drie soorten stromen (1.7.II.C)
> (1) Fysieke stromen — goederen, voorraden die door de onderneming bewegen. (2) Financiële stromen — geld, betalingen, vorderingen. (3) Informatiestromen — data en documenten die de eerste twee begeleiden. De drie moeten op elkaar afgestemd zijn: als een goederenontvangst niet in de informatiestroom belandt, weet niemand dat er moet betaald worden. 🤖

<h3 id="kwaliteitseisen-informatie-1-7-ii-d">Kwaliteitseisen informatie (1.7.II.D)</h3>

> [!tip]- Kwaliteitseisen informatie (1.7.II.D)
> Informatie moet zijn: relevant (raakt de beslissing), betrouwbaar (klopt), tijdig (op tijd beschikbaar), volledig (geen kritieke ontbrekende elementen), en begrijpelijk voor de gebruiker. Het ontbreken van één van deze ondermijnt de stuurkracht. 🤖


## Valkuilen

> [!warning]- Examen-val: alle IT-issues bij 'application controls' onderbrengen
> ⚠️ Examen-val: alle IT-issues bij 'application controls' onderbrengen. Een zwak wachtwoordbeleid is GEEN application control — het is een IT-general-control. Beide zijn nodig. 🤖



## Zie ook

- **Vereist kennis van**: [[geinformatiseerde-omgeving-ic]]
- **Vereist kennis van**: [[it-general-controls]]
- **Vereist kennis van**: [[it-application-controls]]

## Voorbeelden

Yperse Werkplaats BV werkt met Odoo ERP. Inkoopfacturen worden gescand en automatisch gematcht met bestelbon en goederenontvangst (application controls); de IT-verantwoordelijke heeft alleen Pieter Vermeulen + Sofie Janssens admin-rechten gegeven (IT-general-control toegangsbeheer); wekelijkse externe back-up via versleutelde cloud.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3`
