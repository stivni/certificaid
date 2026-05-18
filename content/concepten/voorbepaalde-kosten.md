---
title: Voorbepaalde kosten (standaardkostencalculatie)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.III.C
- 1.8.III
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voorbepaalde-kosten.json
gegenereerd_op: '2026-05-18'
---
# Voorbepaalde kosten (standaardkostencalculatie) 🤖

> [!summary] Korte inhoud
> Voorbepaalde kosten (standaardkosten) zijn vooraf vastgelegde normbedragen voor materiaal, arbeid en overhead per eenheid product.

> [!info] Behoort tot: [[costing-methodes-vergelijking]]

Voorbepaalde kosten (standaardkosten) zijn vooraf vastgelegde normbedragen voor materiaal, arbeid en overhead per eenheid product. Ze worden gebruikt om de werkelijke kosten meteen tegen een norm af te zetten en zo afwijkingen (verschillen) snel te detecteren. Dit ondersteunt budgetbeheer, kostencontrole en prijszetting.

_Bron: Management accounting — bron-gap_


## Bouwstenen

### Drie soorten standaarden 🤖

(1) Ideale standaard: theoretisch maximaal-efficiënt (geen uitval, geen wachttijd). Te streng als doel. (2) Verwachte standaard: realistisch haalbare prestatie onder normale omstandigheden. (3) Historische standaard: gebaseerd op de prestatie van vorig jaar (risico van inefficiëntie consolideren).

**Waarom?** De keuze bepaalt of standaarden motiverend, realistisch of behoudend zijn.



Yperse Werkplaats BV hanteert een verwachte standaard van € 25 directe arbeidskost per uur en 5 uur per tapijt. Standaard directe arbeidskost per tapijt = € 125. Werkelijke registratie: 5,3 uur × € 26 = € 137,80 → ongunstig verschil van € 12,80.


### Standaardkostprijskaart per product 🤖

Per product wordt een 'kaart' opgesteld met: hoeveel materiaal × prijs (standaard materiaalkost), hoeveel uren × tarief (standaard arbeidskost), overhead-toerekening (standaard).

**Waarom?** Maakt automatische berekening van toegestane kosten mogelijk zodra het werkelijke productievolume bekend is.



Standaardkaart tapijt Yperse: 1,2 kg wol × € 5/kg = € 6 materiaal; 5 uur × € 25 = € 125 arbeid; 5 uur × € 40 overhead = € 200. Standaard vervaardigingsprijs = € 331/tapijt.


### Verschillenanalyse 🤖

Werkelijke kost − standaardkost = verschil. Wordt verder opgesplitst in prijsverschil (afwijking in prijs/uurtarief) en hoeveelheidverschil (afwijking in gebruik).

**Waarom?** Verschillenanalyse lokaliseert oorzaak van afwijking — slechte aankoop (prijs) of slechte productie (hoeveelheid).



Yperse: standaard materiaal 1,2 kg × € 5 = € 6. Werkelijk: 1,3 kg × € 5,20 = € 6,76. Prijsverschil = 1,3 × (5,20 − 5,00) = € 0,26 ongunstig. Hoeveelheidverschil = (1,3 − 1,2) × € 5,00 = € 0,50 ongunstig.



## In de praktijk

<h3 id="boekhoudkundige-inschrijving">Boekhoudkundige inschrijving</h3>

> [!tip]- Boekhoudkundige inschrijving
> Standaardkosten worden in de analytische boekhouding direct op de kostendrager geboekt; werkelijke kosten gaan apart in klasse 6 in algemene boekhouding. Het verschil komt op een aparte 'verschillenrekening' (klasse 9 of subrekening). 🤖


> [!info]- Niet verwarren met [[werkelijke-kostencalculatie]]
> Standaardkosten: vooraf vastgelegd → snelle terugkoppeling. Werkelijke kosten: pas achteraf bekend → vertraging maar exact. Voor sturing standaardkosten; voor jaarrekening werkelijke kosten (of standaardkosten met verschillen tot werkelijke geboekt).
>
> _Trigger_: Examen-vraag: 'wat gebruik je voor maandelijkse kostencontrole?' → standaard.


## Valkuilen

> [!warning]- Standaardkostprijskaart actueel houden
> ⚠️ Standaardkostprijskaart actueel houden. Een standaard die drie jaar oud is reflecteert geen prijsstijgingen in materiaal of loonindex; verschillen worden dan permanent en ongunstig zonder dat dat operationele onderprestatie betekent. 🤖


> [!warning]- Voor jaarrekening (vervaardigingsprijs CBN 132/7): waardering op standaardkosten is alleen aanvaardbaar als de afwijking ten opzichte van we…
> ⚠️ Voor jaarrekening (vervaardigingsprijs CBN 132/7): waardering op standaardkosten is alleen aanvaardbaar als de afwijking ten opzichte van werkelijke kost beperkt is. Bij significante verschillen moeten die geïntegreerd worden in de voorraadwaardering. 🤖



## Zie ook

- **Vereist kennis van**: [[verschillenboekhouding]]

