---
title: Volledige kostencalculatie (full costing)
tags:
- concept
- methode
- po-1-8
linked_anchors:
- 1.8.III.A
- 1.8.III
programmaonderdelen:
- '1.8'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/volledige-kostencalculatie.json
gegenereerd_op: '2026-05-18'
---
# Volledige kostencalculatie (full costing) ⚖️

> [!summary] Korte inhoud
> De volledige kostencalculatie (synoniem: full costing, absorption costing) berekent een 'volledige kostprijs' per kostendrager door alle directe én alle (productie-)indirecte kosten op te tellen en aan het product toe te wijzen.

> [!info] Behoort tot: [[costing-methodes-vergelijking]]

De volledige kostencalculatie (synoniem: full costing, absorption costing) berekent een 'volledige kostprijs' per kostendrager door alle directe én alle (productie-)indirecte kosten op te tellen en aan het product toe te wijzen. Dit is de wettelijke aanpak voor de vervaardigingsprijs in de Belgische boekhouding (CBN 132/7), maar in management-accounting wordt full costing soms uitgebreid tot een 'volledige bedrijfskostprijs' die ook administratieve en commerciële overhead bevat — voor interne sturing.

_Bron: CBN 132/7 §2.1 jo. CBN 2012/15_


## Bouwstenen

### Stap 1: directe kosten direct toerekenen 🤖

Tel het verbruikte materiaal en de directe arbeid van elk product op via werkbonnen en materiaalbonnen.

**Waarom?** Directe kosten zijn ondubbelzinnig toewijsbaar — geen verdeel-discussie.

**Voorbeeld**: Yperse Werkplaats BV registreert per order 'partij tapijten': € 12.000 wol + € 4.500 directe arbeid = € 16.500 directe kost.


### Stap 2: indirecte kosten via sleutel 🤖

Verzamel alle indirecte kosten per kostencentrum. Bepaal een verdeelsleutel (directe arbeidsuren, machine-uren, materiaalkost). Bereken sleutel-tarief en pas toe op het product.

**Waarom?** Zonder verdeling zou je 'volledige' kost niet halen.

**Voorbeeld**: Yperse Werkplaats BV: € 1.200.000 indirect bij Weverij / 30.000 arbeidsuren = € 40/uur. Partij tapijten gebruikt 90 uur → € 3.600 toegerekend.


### Stap 3: vervaardigingsprijs of bedrijfskostprijs 🤖

Som direct + indirect = vervaardigingsprijs (wettelijk voor voorraad). Voor interne marge-analyse kan ook commerciële en administratieve overhead worden toegevoegd → 'bedrijfskostprijs'.

**Waarom?** Onderscheid: vervaardigingsprijs voor balans (CBN 132/7); bedrijfskostprijs voor prijszetting en winstgevendheid-analyse.

**Voorbeeld**: Yperse Werkplaats BV: vervaardigingsprijs partij tapijten = € 20.100. Bij toevoeging van commercieel + administratief (€ 1.800 via sleutel) → bedrijfskostprijs € 21.900. Verkoopprijs € 30.000 → marge € 8.100.



## In de praktijk

<h3 id="wettelijke-verankering">Wettelijke verankering</h3>

> [!tip]- Wettelijke verankering
> CBN-advies 2012/15: 'Voor de waardering van de bestellingen in uitvoering wordt uitgegaan van de volledige vervaardigingsprijs met inbegrip van alles wat de uitvoering van het bestelde inhoudt: zowel kosten van grondstoffen, hulpstoffen, ... als rechtstreeks toewijsbare kosten en evenredig deel van indirecte productiekosten.' Full costing is dus de standaard voor voorraadwaardering. ⚖️


> [!info]- Niet verwarren met [[direct-costing]]
> Full costing: alle (productie-)indirecte kosten in de kostprijs. Direct costing: enkel variabele kosten in de kostprijs; vaste overhead direct naar RR. Resultaat: full geeft hogere voorraadwaarde in groei, direct geeft lagere voorraad maar transparantere periodewinst.
>
> _Trigger_: Examen-vraag op voorraadwaardering of marge-analyse: identificeer welke methode wordt gebruikt en welke gevolg het heeft voor het periode-resultaat.

> [!info]- Niet verwarren met [[abc-methode]]
> Traditionele full costing: meestal 1-2 sleutels per kostencentrum (directe arbeidsuren / machine-uren). ABC: meerdere kostengroepen per centrum, elk met eigen cost driver. ABC is verfijning van full costing voor omgevingen met veel overhead.
>
> _Trigger_: Examen-vraag: 'als overhead 70 % is en de standaardsleutel arbeidsuren ondervangt het kostengedrag slecht, welke methode kies je?' → ABC.


## Valkuilen

> [!warning]- 'Volledig' betekent in wettelijke zin alleen productie-overhead; in management-zin kan het ook administratie + commercieel zijn
> ⚠️ 'Volledig' betekent in wettelijke zin alleen productie-overhead; in management-zin kan het ook administratie + commercieel zijn. Examen-valkuil: studenten gooien beide categorieën in dezelfde 'volledige' kostprijs zonder onderscheid → fout bij voorraadwaardering-vraag. 🤖



## Bronnen

[^1]: `CBN-2012-15-bestellingen-in-uitvoering__sec_waarderingsaspecten-n-a-v-de-toepassing-van-full-costing`
[^2]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_vervaardigingsprijs`
[^3]: `CBN-2012-15-bestellingen-in-uitvoering__sec_waarderingsaspecten-n-a-v-de-toepassing-van-direct-costing`
