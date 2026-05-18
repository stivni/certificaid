---
title: Berekenen en interpreteren van budgetverschillen (verschillenboekhouding)
tags:
- concept
- competentie
- po-1-8
linked_anchors:
- 1.8.taak.1
- 1.8.VI
- 1.8.VI.D
- 1.8.III.C
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/berekenen-interpreteren-budgetverschillen.json
gegenereerd_op: '2026-05-18'
---
# Berekenen en interpreteren van budgetverschillen (verschillenboekhouding) 🤖

Competentie waarmee de stagiair budgetverschillen splitst, kwantificeert en interpreteert: totaal-verschil decomposeren in prijs- en hoeveelheidcomponenten (materiaal), tarief- en efficiëntiecomponenten (arbeid), volume- en bestedingsverschil (overhead). Eindproduct: een verschillen-rapport per kostencentrum dat aanwijst wélke factor moet bijgestuurd worden — verkoop (volume), inkoop (materiaalprijs), HR (tarief), productie (efficiëntie). Sluit aan op de vijfde fase van budgetprocedure (periodieke opvolging) en is hartstuk van management-stuurinformatie.


## Stappen

### 1. Voorbereiden van de vergelijkingsbasis

Zorg dat budget (voorbepaalde kosten) en werkelijke realisatie op vergelijkbare basis staan: hetzelfde volume, dezelfde periode, dezelfde scope.

**Waarom?** Een budget op 25.000 stuks vergelijken met realisatie op 22.000 stuks zonder flexibilisering levert een volume-effect dat de echte oorzaken maskeert.

**📥 Input**:
- Statisch of flexibel budget uit [[opstellen-master-budget]] → **Budget per kostensoort per periode** _(boekhoudkundig-bedrag)_
- Werkelijke cijfers uit boekhouding → **Werkelijke kost per soort + werkelijk volume** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Vergelijkingsbasis (gefixeerd op werkelijk volume) → **Flexibel-budget + werkelijk** _(document)_

**🛠️ Hoe**:

1. Lees [[flexibel-budget]] §gebruik-in-variantie-analyse: zonder flexibilisering loop je
   het volume-effect en het efficiëntie-effect door elkaar.
2. Herbereken het budget op het werkelijke volume voor variabele kosten
   (vaste kosten blijven gelijk).
3. Resultaat: drie kolommen — statisch budget, flexibel budget (werkelijk volume),
   werkelijke realisatie.


**Grondslag**: [[flexibel-budget]] §gebruik-in-variantie-analyse, [[verschillenboekhouding]] §basis

### 2. Splitsen van het materiaalverschil in prijs- en hoeveelheidsverschil

Bereken voor elke grondstof het prijsverschil (werkelijke − standaard prijs × werkelijke hoeveelheid) en het hoeveelheidsverschil ((werkelijke − standaard hoeveelheid) × standaardprijs).

**Waarom?** De splitsing toont wie verantwoordelijk is: inkoop bij prijsverschil, productie bij hoeveelheidsverschil.

**📥 Input**:
- Materiaal-norm + realisatie → **Standaard kg/stuk, standaardprijs, werkelijk verbruik, werkelijke prijs** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Prijs- en hoeveelheidsverschil materiaal → **€ + gunstig/ongunstig** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas de splitsing toe volgens [[verschillenboekhouding]] §materiaalverschil:
   Prijsverschil = (werkelijke prijs − standaardprijs) × werkelijke hoeveelheid.
   Hoeveelheidsverschil = (werkelijke − standaard hoeveelheid) × standaardprijs.
2. Positief = ongunstig (kost meer dan begroot); negatief = gunstig.
3. Het totaal van beide verschillen = totaal materiaalverschil.


> [!example]- Voorbeeld: Yperse Werkplaats BV — wol-verbruik voor productie van 22.000 tapijten
> Yperse Werkplaats BV — wol-verbruik voor productie van 22.000 tapijten. Standaard 5 kg per tapijt aan € 5,00/kg. Werkelijk 116.000 kg aan € 5,30/kg.
>
> 1. **Berekening prijs- en hoeveelheidsverschil** 🧮
>
>    Standaard kg voor 22.000 tapijten = 22.000 × 5 = 110.000 kg.
>    
>    Prijsverschil = (€ 5,30 − € 5,00) × 116.000 kg = **€ 34.800 ongunstig**
>    
>    Hoeveelheidsverschil = (116.000 − 110.000) × € 5,00 = **€ 30.000 ongunstig**
>    
>    Totaal materiaalverschil = € 34.800 + € 30.000 = **€ 64.800 ongunstig**
>    
>
> 2. **Interpretatie** 💬
>
>    Inkoop kocht duurder dan begroot (€ 34.800) — onderzoek leverancierscontract.
>    Productie verbruikte meer (€ 30.000) — onderzoek uitval / herwerking.
>    
>

**Grondslag**: [[verschillenboekhouding]] §materiaalverschil

### 3. Splitsen van het arbeidsverschil in tarief- en efficiëntieverschil

Bereken voor elke loongroep het tariefverschil (werkelijk − standaard uurtarief × werkelijke uren) en het efficiëntieverschil ((werkelijke − standaard uren) × standaard uurtarief).

**Waarom?** Splitsing toont waar de afwijking zit: HR/personeelsdienst bij tarief, productieleiding bij efficiëntie.

**📥 Input**:
- Arbeid-norm + realisatie → **Standaard uren/stuk, € 25/u standaard, werkelijke uren, werkelijk tarief** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tarief- en efficiëntieverschil arbeid → **€ + gunstig/ongunstig** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas [[prijsverschil-arbeid]] §splitsing toe:
   Tariefverschil = (werkelijk tarief − standaardtarief) × werkelijke uren.
   Efficiëntieverschil = (werkelijke − standaard uren) × standaardtarief.
2. Standaardtarief Yperse: € 25/uur inclusief lasten.
3. Bekijk per kostencentrum apart — Spinnerij/Weverij/Confectie hebben mogelijk
   verschillende oorzaken.


> [!example]- Voorbeeld: Yperse Werkplaats BV — Confectie
> Yperse Werkplaats BV — Confectie. Standaard 0,2 arbeids-uur per tapijt aan € 25/u. 22.000 tapijten = 4.400 standaard-uren. Werkelijk: 4.700 uren aan € 26,50/u.
>
> 1. **Berekening** 🧮
>
>    Tariefverschil = (€ 26,50 − € 25,00) × 4.700 u = **€ 7.050 ongunstig**
>    
>    Efficiëntieverschil = (4.700 − 4.400) × € 25,00 = **€ 7.500 ongunstig**
>    
>    Totaal arbeidsverschil = **€ 14.550 ongunstig**
>    
>
> 2. **Interpretatie** 💬
>
>    Indexering deed het tarief stijgen (HR-/loon-oorzaak); productie verloor 300 uur
>    aan herwerking of vertragingen (productie-snelheid).
>    
>

**Grondslag**: [[prijsverschil-arbeid]] §splitsing, [[verschillenboekhouding]] §arbeidsverschil

### 4. Berekenen van indirecte-kosten- en volume-verschillen

Bereken voor indirecte productiekosten een budget- (uitgaven-) verschil en een capaciteits- (volume-) verschil.

**Waarom?** Bij vaste indirecte kosten hangt het verschil af van zowel uitgavenbeheersing als de bezettingsgraad — twee verschillende stuurbare effecten.

**📥 Input**:
- Indirect-budget + bezetting → **Begrote indirecte kost + normvolume + werkelijk** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Budget- en volume-verschil → **€** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bereken volgens [[verschillenboekhouding]] §indirecte-kosten-splitsing:
   Budgetverschil = werkelijke kost − geflexibiliseerd budget bij werkelijk volume.
   Volume-verschil = geflexibiliseerd budget − toegerekende kost
   (= (norm- − werkelijk volume) × standaard opslag-tarief).
2. Volume-verschil is enkel relevant bij vaste indirecte kosten — variabele
   indirecte kost wordt al door flexibilisering gevangen.
3. Interpretatie: budget-verschil = uitgavenbeheersing; volume-verschil = onder-
   of overbezetting van capaciteit.


**Grondslag**: [[verschillenboekhouding]] §indirecte-kosten-splitsing, [[vaste-kosten]] §bezettingsgraad

### 5. Rapporteren en koppelen aan bijsturing

Synthetiseer alle verschillen in een variantie-rapport en koppel oorzaken aan acties.

**Waarom?** Een variance-analyse zonder bijsturings-actie is een kostenpost zonder waarde — de cyclus moet sluiten.

**📥 Input**:
- Verschillen uit stappen 2-4 → **Volledige verschillenmatrix** _(document)_
- Gesprekken met afdelingsverantwoordelijken → **Toelichting bij significante verschillen** _(document)_

**📤 Output**:
- Variantie-rapport + actie-agenda → **Per significant verschil: oorzaak + actie + eigenaar** _(document)_

**🛠️ Hoe**:

1. Tabel per kostencategorie: budget, werkelijk, verschil €, verschil %, type.
2. Focus op significante verschillen (bv. > 5 % of > € 10.000).
3. Volg [[budgetbeheer]] §opvolging: koppel elk significant verschil aan een
   verantwoordelijke + corrigerende actie + deadline.
4. Update budget waar nodig (rolling-forecast-logica) voor resterend boekjaar.


**Grondslag**: [[budgetbeheer]] §opvolging, [[verschillenboekhouding]] §rapportage

> [!warning]- Vergelijk werkelijke realisatie tegen het flexibele budget (gefixeerd op werkelijk volume) — niet tegen het statische budget.
>
> _Vaak fout gedaan_: Werkelijk volume tegen statisch budget afzetten — vermengt volume-effect met efficiëntie.
>
> _Grondslag_: [[flexibel-budget]] §gebruik-in-variantie-analyse

> [!warning]- Splits prijs en hoeveelheid bij elke variabele kost-categorie.
>
> _Vaak fout gedaan_: Eén totaal materiaalverschil rapporteren zonder splitsing — onbruikbaar voor sturing.
>
> _Grondslag_: [[verschillenboekhouding]] §materiaalverschil


## Voorbeelden



