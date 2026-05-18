---
title: Uitvoeren van een break-even-analyse en bepalen van de veiligheidsmarge
tags:
- competentie
- po-1-8
programmaonderdelen:
- '1.8'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-break-even-analyse.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van een break-even-analyse en bepalen van de veiligheidsmarge

**⚖️ 0% · 🤖 100%**

> Break-even-analyse is zuivere management-accounting-doctrine zonder Belgische trusted wettelijke of CBN-bron. Geheel gebaseerd op vakdoctrine (CVP-analysis). Vereist mens-review wegens praktijk_pct > 70%.

## Aanbevolen werkwijze

### 1. Inventariseren van vaste en variabele kosten + contributiemarge

Verzamel de drie inputs van het break-even-model: totaal vaste kosten op jaarbasis, variabele kost per eenheid en verkoopprijs per eenheid.

**Waarom?** Het break-even-model rust op deze drie grootheden; ontbreekt er één of zit er een rubriceringfout in, dan klopt het volume niet.

**📥 Input**:
- Budget vaste kosten → **Totaal € per jaar** _(boekhoudkundig-bedrag)_
- Direct-costing-RR uit [[toepassen-direct-costing-en-contributiemarge]] → **Variabele kost en verkoopprijs per eenheid** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Inputtabel break-even → **V, P, F** _(document)_

**🛠️ Hoe**:

1. Klasseer vaste/variabele kosten volgens
   [[toepassen-direct-costing-en-contributiemarge]] stap 1.
2. Bereken contributiemarge per eenheid via [[contributiemarge]] §per-eenheid.
3. Verifieer dat de relevant range realistisch is: zijn de vaste kosten echt
   constant binnen het verwachte volume?


**Grondslag**: [[break-even-analyse]] §inputs, [[vaste-kosten]] §relevant-range

### 2. Berekenen van het break-even-volume

Bereken break-even = totale vaste kosten / contributiemarge per eenheid.

**Waarom?** Dit volume markeert waar totale opbrengst = totale kost; eronder maakt de onderneming verlies, erboven winst.

**📥 Input**:
- Inputtabel uit stap 1 → **F, V, P** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Break-even-volume + break-even-omzet → **Stuks en € omzet** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas de formule toe volgens [[break-even-analyse]] §volume-formule:
   break-even volume = vaste kosten / (verkoopprijs − variabele kost per eenheid).
2. Bereken break-even-omzet = break-even-volume × verkoopprijs.
3. Of bereken rechtstreeks via contributiemarge-percentage:
   break-even-omzet = vaste kosten / contributiemarge-%.
4. Rond niet vroegtijdig af; weergeven met passende afronding bij rapportering.


> [!example]- Voorbeeld: Yperse Werkplaats BV — tapijt-standaard
> Yperse Werkplaats BV — tapijt-standaard. Verkoopprijs € 60, variabele kost € 13, vaste kosten € 800.000.
>
> 1. **Contributiemarge en break-even** 🧮
>
>    Contributiemarge per tapijt = € 60 − € 13 = **€ 47**
>    
>    Break-even volume = € 800.000 / € 47 = **17.022 tapijten**
>    
>    Break-even omzet = 17.022 × € 60 = **€ 1.021.320**
>    
>
> 2. **Controle via contributiemarge-percentage** 🧮
>
>    CM-% = 47 / 60 = 78,33 %
>    
>    Break-even omzet = € 800.000 / 0,7833 = **€ 1.021.300** (klein afrondingsverschil)
>    
>

**Grondslag**: [[break-even-analyse]] §volume-formule, [[break-even-analyse]] §omzet-formule

### 3. Berekenen van veiligheidsmarge en sensitiviteit

Bereken de veiligheidsmarge (verwacht volume − break-even-volume) en toets de gevoeligheid bij wijziging van prijs, variabele kost of vaste kosten.

**Waarom?** Een onderneming met een verwacht volume dicht bij break-even is kwetsbaar; sensitiviteits-analyse toont de impact van parameter-wijzigingen.

**📥 Input**:
- Verwacht verkoopvolume uit budget → **Stuks per jaar** _(boekhoudkundig-bedrag)_
- Break-even-volume uit stap 2 → **Stuks** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Veiligheidsmarge in % en € + sensitiviteits-tabel → **Procent en €** _(percentage)_

**🛠️ Hoe**:

1. Bereken volgens [[break-even-analyse]] §veiligheidsmarge:
   veiligheidsmarge-% = (verwacht volume − break-even-volume) / verwacht volume.
2. Voer drie scenario's door:
   - Verkoopprijs daalt met 5 %.
   - Variabele kost stijgt met 10 %.
   - Vaste kosten stijgen met € 50.000.
   Herbereken break-even voor elk scenario.
3. Beoordeel: bij welk scenario komt break-even gevaarlijk dichtbij het verwacht volume?
4. Rapporteer aan directie met grafiek (omzet × volume) als beslissingsondersteuning.


> [!example]- Voorbeeld: Yperse Werkplaats BV — verwacht volume 25.000 tapijten
> Yperse Werkplaats BV — verwacht volume 25.000 tapijten. Break-even 17.022.
>
> 1. **Veiligheidsmarge** 🧮
>
>    Veiligheidsmarge in stuks = 25.000 − 17.022 = **7.978 tapijten**
>    
>    Veiligheidsmarge-% = 7.978 / 25.000 = **31,9 %**
>    
>
> 2. **Sensitiviteit prijs −5 %** 🧮
>
>    Nieuwe verkoopprijs = € 57; CM = € 44.
>    
>    Nieuw break-even = € 800.000 / € 44 = **18.182 tapijten**.
>    
>    Veiligheidsmarge daalt naar 27,3 %.
>    
>

**Grondslag**: [[break-even-analyse]] §veiligheidsmarge, [[break-even-analyse]] §sensitiviteit

> [!warning]- Hou rekening met productmix — multi-product break-even vereist gewogen contributiemarge of opsplitsing per productlijn.
>
> _Vaak fout gedaan_: Eén break-even-volume berekenen voor een onderneming met sterk verschillende producten.
>
> _Grondslag_: [[contributiemarge]] §multi-product-gewogen

> [!warning]- Verifieer dat 'vaste kosten' werkelijk constant blijven binnen het scenario-bereik.
>
> _Vaak fout gedaan_: Vaste kosten extrapoleren ver buiten relevant range — een nieuwe productiehal verhoogt de vaste kost trapsgewijs.
>
> _Grondslag_: [[vaste-kosten]] §relevant-range


## Voorbeelden

> [!example]- Yperse Werkplaats BV met vaste kosten € 800.000, prijs € 60, variabele kost € 13
> **Conclusie**: Break-even bij 17.022 tapijten; veiligheidsmarge 31,9 % bij verwacht volume 25.000.
>
> **Grondslag**: [[break-even-analyse]] §volume-formule, [[break-even-analyse]] §veiligheidsmarge
>
> **Redenering**: Standaard CVP-toepassing op één homogeen product. Sensitiviteit toont dat een prijsdaling van 5 % de veiligheidsmarge tot 27 % verlaagt — significante kwetsbaarheid.


## Gebaseerd op concepten

[[break-even-analyse]] · [[contributiemarge]] · [[vaste-kosten]] · [[variabele-kosten]] · [[direct-costing]]
## Voortkomend uit

- **Taken**: 1.8.taak.1
- **Kenniselementen**: 1.8.III, 1.8.III.D, 1.8.II.A
