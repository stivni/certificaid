---
title: Toepassen van direct costing en contributiemarge-analyse
tags:
- competentie
- po-1-8
programmaonderdelen:
- '1.8'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toepassen-direct-costing-en-contributiemarge.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van direct costing en contributiemarge-analyse

**⚖️ 10% · 🤖 90%**

> Direct costing en contributiemarge-analyse zijn management-accounting-doctrine zonder Belgische wettelijke verankering. Wettelijk raakvlak is uitsluitend dat CBN 2012/15 direct costing aanvaardt voor analytische rapportering mits voorraad op de balans aan vervaardigingsprijs gewaardeerd blijft. Vereist mens-review wegens praktijk_pct > 70%.

## Aanbevolen werkwijze

### 1. Identificeren van variabele versus vaste kosten

Klasseer alle kostensoorten op de gedrags-as: variabel (verandert mee met productievolume) of vast (blijft gelijk binnen de relevant range).

**Waarom?** De hele direct-costing-logica steunt op deze tweedeling — verkeerde classificatie verstoort de contributiemarge.

**📥 Input**:
- Kostenoverzicht → **Bedragen per kostensoort, eventueel ook drijvers** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Lijst gesplitst variabel/vast → **Bedrag + classificatie + drijver** _(document)_

**🛠️ Hoe**:

1. Pas [[variabele-kosten]] §gedrag toe: kost evolueert evenredig met output
   (grondstoffen, directe arbeid, energie productiemachines).
2. Pas [[vaste-kosten]] §gedrag toe: kost blijft gelijk binnen de relevant range
   (huur, afschrijvingen, leiding-salarissen).
3. Behandel semi-variabele kosten apart: splits in vast deel + variabel deel
   (bv. energie-grondtarief + verbruik) met de hoog-laag-methode.
4. Documenteer het gedrags-bereik: tot welk volume blijft 'vast' werkelijk vast?


**Grondslag**: [[variabele-kosten]] §gedrag, [[vaste-kosten]] §gedrag

> [!warning]- Onderscheid steeds de gedrag-as (variabel/vast) van de toewijsbaarheids-as (direct/indirect).
>
> _Vaak fout gedaan_: Variabel gelijkstellen met direct of vast gelijkstellen met indirect — twee assen door elkaar halen.
>
> _Grondslag_: [[directe-kosten]] §verschil-met-variabele, [[costing-methodes-vergelijking]] §twee-assen

### 2. Berekenen van de contributiemarge per eenheid

Bereken contributiemarge = verkoopprijs − variabele kost per eenheid.

**Waarom?** De contributiemarge toont wat elke verkochte eenheid bijdraagt aan dekking van vaste kosten en winst.

**📥 Input**:
- Verkoopprijslijst → **Prijs per product** _(boekhoudkundig-bedrag)_
- Variabele kostprijs uit stap 1 → **Bedrag per eenheid** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Contributiemarge per eenheid → **€ per stuk + marge-percentage** _(percentage)_

**🛠️ Hoe**:

1. Bereken volgens [[contributiemarge]] §per-eenheid:
   contributiemarge = verkoopprijs − variabele kost per eenheid.
2. Bereken het contributiemarge-percentage:
   contributiemarge-% = contributiemarge / verkoopprijs.
3. Onderscheid contributiemarge per eenheid (vergelijk producten) van totale
   contributiemarge (verkoopvolume × marge per eenheid).
4. Voor multi-product-context: bereken een gewogen gemiddelde contributiemarge
   op basis van de productmix.


> [!example]- Voorbeeld: Yperse Werkplaats BV — tapijt-standaard met verkoopprijs € 60 en variabele kost € 13 per stuk
> Yperse Werkplaats BV — tapijt-standaard met verkoopprijs € 60 en variabele kost € 13 per stuk.
>
> 1. **Berekening contributiemarge per eenheid** 🧮
>
>    Contributiemarge per tapijt = € 60 − € 13 = **€ 47**
>    
>    Contributiemarge-% = € 47 / € 60 = **78,3 %**
>    
>
> 2. **Totale contributiemarge bij verkoop 25.000 stuks** 🧮
>
>    Totale contributiemarge = 25.000 × € 47 = **€ 1.175.000**
>    
>    Dekt vaste kosten € 800.000 → winst = € 375.000.
>    
>

**Grondslag**: [[contributiemarge]] §per-eenheid, [[contributiemarge]] §percentage

### 3. Direct-costing-resultatenrekening opstellen

Herorganiseer de resultatenrekening volgens direct-costing-logica: omzet − variabele kost = contributiemarge − vaste kost = bedrijfsresultaat.

**Waarom?** De direct-costing-volgorde maakt zichtbaar hoe het volume de winst stuurt, en welk vast kostenniveau gedekt moet worden.

**📥 Input**:
- Verkoop- en productiegegevens periode → **Volume × prijs en variabele en vaste kosten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Direct-costing-RR → **Drie blokken** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bouw de drie blokken zoals [[direct-costing]] §RR-structuur voorschrijft:
   omzet − totale variabele kosten = totale contributiemarge.
   − totale vaste kosten = bedrijfsresultaat.
2. Vergelijk met de full-costing-RR via [[costing-methodes-vergelijking]] §RR-verschil:
   voorraadwijzigingen kunnen het resultaat in beide methoden anders weergeven.
3. Belangrijk: voor de balans-voorraadwaardering gebruikt België de vervaardigingsprijs;
   de direct-costing-RR is een interne rapporteringsvorm, geen jaarrekening.


**Grondslag**: [[direct-costing]] §RR-structuur, [[costing-methodes-vergelijking]] §RR-verschil

> [!warning]- Houd de direct-costing-rapportering strikt intern; voor de balans hanteer je vervaardigingsprijs.
>
> _Vaak fout gedaan_: Voorraden onder direct costing op de balans plaatsen — onder Belgisch jaarrekeningenrecht niet toegelaten als productie-overhead niet mee gewaardeerd is.
>
> _Grondslag_: [[vervaardigingsprijs]] §wettelijke-componenten, CBN 2012/15

### 4. Toepassen voor beslissingsanalyse (productmix, prijsondergrens, opportuniteit)

Gebruik contributiemarge om typische korte-termijn-beslissingen te onderbouwen: welke producten promoten, minimumprijs voor een extra order, opportuniteitskost van een knelpunt.

**Waarom?** Bij korte-termijn-keuzes zijn vaste kosten meestal sunk; relevant is de marginale of contributiebijdrage.

**📥 Input**:
- Contributiemarges per product uit stap 2 → **€ per stuk** _(boekhoudkundig-bedrag)_
- Knelpuntcapaciteit + alternatieve orders → **Beperkende factor (uren, m², kg grondstof)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Beslissingsadvies → **Productmix, minimumprijs of accepteer-order-conclusie** _(conclusie)_

**🛠️ Hoe**:

1. Voor productmix bij capaciteitsbeperking: bereken contributiemarge per
   eenheid van de schaarse resource (€ marge / machine-uur) volgens
   [[contributiemarge]] §per-schaarse-resource. Promoot het product met de hoogste marge.
2. Voor minimumprijs bij extra order: gebruik [[marginale-kostprijs]] §korte-termijn —
   extra order is winstgevend zodra prijs > variabele kost per eenheid + inkrementele vaste kost.
3. Bouw [[opportuniteitskost]] in als de extra order een andere order verdringt:
   relevante kost = variabele kost + verdrongen contributiemarge.
4. Let op: deze logica werkt enkel korte termijn; op lange termijn moeten ook
   vaste kosten gedekt worden.


> [!example]- Voorbeeld: Yperse Werkplaats BV ontvangt een eenmalige order van 500 tapijten aan € 35 per stuk
> Yperse Werkplaats BV ontvangt een eenmalige order van 500 tapijten aan € 35 per stuk. Variabele kost € 13; vaste kosten € 800.000 zijn reeds gedekt door normale productie. Geen verdrongen order.
>
> 1. **Bijdrage van de extra order** 🧮
>
>    Contributiemarge extra order = 500 × (€ 35 − € 13) = 500 × € 22 = **€ 11.000**
>    
>
> 2. **Beslissing** 💬
>
>    Aanvaarden — vaste kosten zijn sunk, € 11.000 extra winst.
>    Indien een gewone order van 500 stuks aan € 60 (marge € 47) verdrongen zou
>    worden: opportuniteitskost = 500 × € 47 = € 23.500. Dan extra-order weigeren
>    (€ 11.000 < € 23.500).
>    
>

**Grondslag**: [[contributiemarge]] §per-schaarse-resource, [[marginale-kostprijs]] §korte-termijn, [[opportuniteitskost]] §beslissingsregel


## Voorbeelden

> [!example]- Yperse Werkplaats BV evalueert een spot-order van 500 tapijten aan € 35
> **Conclusie**: Aanvaarden bij vrije capaciteit (€ 11.000 winst); weigeren bij verdringing van gewone order met marge € 47 (opportuniteitskost € 23.500).
>
> **Grondslag**: [[opportuniteitskost]], [[marginale-kostprijs]] §korte-termijn
>
> **Redenering**: Korte-termijn beslissing: vaste kosten zijn sunk, relevant is variabele kost ± opportuniteitskost.


## Gebaseerd op concepten

[[direct-costing]] · [[contributiemarge]] · [[variabele-kosten]] · [[vaste-kosten]] · [[volledige-kostencalculatie]] · [[costing-methodes-vergelijking]] · [[marginale-kostprijs]] · [[opportuniteitskost]] · [[kostprijs-per-eenheid]]
## Voortkomend uit

- **Taken**: 1.8.taak.1
- **Kenniselementen**: 1.8.III, 1.8.III.B, 1.8.III.E, 1.8.II, 1.8.II.A
