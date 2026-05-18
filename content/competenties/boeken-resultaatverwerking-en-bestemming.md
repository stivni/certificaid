---
title: Boeken van resultaatverwerking en bestemming (reserves, dividenden, belasting)
tags:
- competentie
- po-1-1
programmaonderdelen:
- '1.1'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/boeken-resultaatverwerking-en-bestemming.json
gegenereerd_op: '2026-05-18'
---
# Boeken van resultaatverwerking en bestemming (reserves, dividenden, belasting)

**⚖️ 75% · 🤖 25%**

> De volgorde (eerst vennootschapsbelasting, dan wettelijke reserve, dan beschikbare reserves, dan dividend) en de wettelijke reserve-plicht (WVV art. 5:114, 7:128) zijn wettelijk verankerd. De keuze tussen reserveren en dividend uitkeren is een bestuurs-/AV-beslissing — praktijk.

## Aanbevolen werkwijze

### 1. Bereken het te bestemmen resultaat van het boekjaar

Bepaal winst of verlies vóór belastingen op basis van resultatenrekening, daarna trek vennootschapsbelasting af.

**Waarom?** Te bestemmen resultaat is het saldo dat op de algemene vergadering ter bestemming wordt voorgelegd.

**📥 Input**:
- Resultatenrekening → **Som klasse 70-74 minus klasse 60-66** _(berekening)_

**📤 Output**:
- Te bestemmen resultaat-bedrag → **Winst of verlies vóór bestemming** _(berekening)_

**🛠️ Hoe**:

1. Bereken resultaat vóór belastingen = ∑ opbrengsten (klasse 70-74) - ∑ kosten (klasse 60-66 + 65 financieel + 66 niet-recurrent).
2. Bereken vennootschapsbelasting volgens fiscaal resultaat (niet identiek aan boekhoudkundig). Boek: Debet 6700 Verschuldigde belastingen; Credit 4500 Te betalen vennootschapsbelasting.
3. Bij Meubelzaak Mertens BV — opbrengsten € 1.250.000, kosten € 1.183.000, winst vóór belasting € 67.000. Vpb tarief 25% verlaagd op KMO-deel (€ 100.000 → 20%) = € 67.000 × 20% = € 13.400. Winst na belasting € 53.600.
4. Boek netto-resultaat: Debet 6920 Toevoeging overgedragen resultaat; Credit 14 Overgedragen winst (bij verlies omgekeerd via 6921 / 14).


**Grondslag**: [[bedrijfsresultaat]] §netto-resultaat-berekening, KB-WVV art. 3:90

### 2. Toets de plicht tot dotatie wettelijke reserve

Indien de wettelijke reserve nog niet 10% van het kapitaal bereikt heeft, doteer minstens 5% van het boekjaar-resultaat.

**Waarom?** WVV verplicht deze dotatie tot het maximumplafond is bereikt — kapitaalbeschermende reserve voor schuldeisers.

**📥 Input**:
- Balans-saldi rubriek 100 en 130 → **Kapitaal + bestaande wettelijke reserve** _(balans)_

**📤 Output**:
- Dotatie-bedrag wettelijke reserve → **5% van resultaat of saldo tot 10% kapitaal** _(berekening)_

**🛠️ Hoe**:

1. Bereken huidig saldo 130 Wettelijke reserve.
2. Bereken maximum = 10% kapitaal (rubriek 100).
3. Indien 130 < maximum → dotatie 5% van winst van boekjaar (zie [[wettelijke-reserve]] §dotatieplicht).
4. Indien dotatie + saldo > maximum → beperk tot maximum.
5. Voor Meubelzaak Mertens BV — kapitaal € 200.000, max wettelijke reserve € 20.000. Huidig saldo € 14.500. Dotatie 2026: 5% × € 53.600 = € 2.680. Eindsaldo wordt € 17.180, nog onder max.
6. Boek: Debet 6921 Toevoeging aan wettelijke reserve; Credit 130 Wettelijke reserve.


**Grondslag**: [[wettelijke-reserve]] §dotatieplicht, WVV art. 5:114 / 7:128

### 3. Bereken eventuele dotaties aan beschikbare reserves

Bestem deel van het resultaat aan vrije beschikbare reserves volgens AV-besluit.

**Waarom?** Reserveren versterkt eigen vermogen, ondersteunt latere investeringen en verhoogt solvabiliteit.

**📥 Input**:
- Bestuursvoorstel + AV-besluit → **Voorgestelde bestemming** _(document)_

**📤 Output**:
- Boekingen reserves → **Per reserve dotatie + tegenboeking 14** _(boekingsregel)_

**🛠️ Hoe**:

1. Categorieën: 130 Wettelijke reserve (verplicht), 131 Onbeschikbare reserves (statutair), 132 Belastingvrije reserves (fiscaal), 133 Beschikbare reserves (vrij).
2. AV beslist wat naar welke rubriek gaat — verwijst naar statuten voor onbeschikbare reserves en fiscale wetgeving voor belastingvrije.
3. Boek per dotatie: Debet 6921 Toevoeging aan reserve; Credit 13X reserve-rubriek.
4. Bij Meubelzaak Mertens BV — AV besluit € 20.000 naar beschikbare reserves: D 6921 € 20.000; C 133 Beschikbare reserves € 20.000.


**Grondslag**: [[resultaatverwerking]] §reserves, [[eigen-middelen]] §reserve-typologie

### 4. Bereken en boek dividend (indien uitkering beslist)

Bereken bruto-dividend, roerende voorheffing en netto-dividend; boek schuld aan aandeelhouders.

**Waarom?** Dividend is een verminderingsbeweging in het eigen vermogen ten gunste van aandeelhouders; roerende voorheffing is wettelijke voorhouding.

**📥 Input**:
- AV-besluit → **Bruto-dividend totaal of per aandeel** _(berekening)_

**📤 Output**:
- Dividend-boekingen → **Bruto-dividend + RV + netto** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken bruto-dividend (totaal of per aandeel × aantal aandelen).
2. Bepaal RV-tarief: 30% standaard; 15% bij VVPR-bis voor jonge KMO's (kleine vennootschap, kapitaal opgericht ≥ 01/07/2013, drie volle boekjaren); 0% bij liquidatiereserve-uitkering > 5 jaar.
3. Boek: Debet 6940 Tussenkomst van vennoten in het verlies / 694 Dividenden (vermindering eigen vermogen); Credit 4530 Te betalen dividenden bruto.
4. Op uitkeringsdatum: Debet 4530; Credit 4530.1 RV op dividenden (30% inhouding) + Credit 5500 Bank (netto).
5. RV moet binnen 15 dagen aan de fiscus betaald worden: D 4530.1; C 5500.
6. Voor Meubelzaak Mertens BV — AV besluit € 25.000 bruto-dividend, KMO met VVPR-bis (15%): RV = € 3.750; netto € 21.250 aan aandeelhouders.


> [!example]- Voorbeeld: Meubelzaak Mertens BV — winst na belasting € 53.600
> Meubelzaak Mertens BV — winst na belasting € 53.600. AV besluit op 25/04/2027: dotatie wettelijke reserve € 2.680, beschikbare reserves € 20.000, bruto-dividend € 25.000 (VVPR-bis 15%), saldo naar overgedragen winst.
>
> 1. **Berekening verdeling** 🧮
>
>    Winst na belasting: € 53.600
>    - Dotatie wettelijke reserve (5% × € 53.600): € 2.680
>    - Dotatie beschikbare reserves: € 20.000
>    - Bruto-dividend: € 25.000
>    - Saldo overgedragen winst: € 53.600 - € 2.680 - € 20.000 - € 25.000 = € 5.920
>    RV op dividend (15% VVPR-bis): € 3.750
>    Netto-dividend aan aandeelhouders: € 21.250
>    
>
> 2. **Boeking resultaatverwerking AV-datum** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 25/04/2027 | 14 Overgedragen resultaat | bestemming | € 53.600,00 | |
>    | 25/04/2027 | 130 Wettelijke reserve | dotatie | | € 2.680,00 |
>    | 25/04/2027 | 133 Beschikbare reserves | dotatie | | € 20.000,00 |
>    | 25/04/2027 | 4530 Te betalen dividenden bruto | dividend | | € 25.000,00 |
>    | 25/04/2027 | 14 Overgedragen resultaat | saldo voorgedragen | | € 5.920,00 |
>    
>
> 3. **Boeking uitbetaling dividend + RV** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 05/05/2027 | 4530 Te betalen dividenden bruto | uitbetaling | € 25.000,00 | |
>    | 05/05/2027 | 4531 Roerende voorheffing op dividenden | RV 15% | | € 3.750,00 |
>    | 05/05/2027 | 5500 Bank | netto aan aandeelhouders | | € 21.250,00 |
>    | 18/05/2027 | 4531 Roerende voorheffing op dividenden | aangifte + betaling fiscus | € 3.750,00 | |
>    | 18/05/2027 | 5500 Bank | betaling RV | | € 3.750,00 |
>    
>

**Grondslag**: [[resultaatverwerking]] §dividend, WVV art. 5:142, 7:212

> [!warning]- Toets vóór dividendbeslissing aan de WVV-uitkeerbaarheids-tests — netto-actief-test (5:142, 7:212) + liquiditeitstoets (5:143, 7:213).
>
> _Vaak fout gedaan_: Dividend uitkeren zonder dubbele uitkeerbaarheidstoets, waardoor bestuurders persoonlijk aansprakelijk worden bij latere insolventie.
>
> _Grondslag_: [[eigen-middelen]] §uitkeerbaarheid; WVV art. 5:142 / 7:212

### 5. Boek het saldo overgedragen resultaat en sluit het boekjaar

Boek het deel dat noch reserve noch dividend wordt op overgedragen resultaat (14) en sluit het boekjaar boekhoudkundig.

**Waarom?** Overgedragen resultaat blijft als vrij beschikbaar saldo in eigen vermogen en kan volgend boekjaar opnieuw bestemd worden.

**📥 Input**:
- Bestemmingen stap 2-4 → **Reserves + dividenden** _(berekening)_

**📤 Output**:
- Slotboeking + heropeningsboeking → **14 saldo + opening volgend boekjaar** _(boekingsregel)_

**🛠️ Hoe**:

1. Bereken saldo = winst na belasting - dotaties reserves - bruto-dividend.
2. Indien positief: saldo blijft op 14 Overgedragen winst en wordt vermeld op balans.
3. Indien negatief (verlies overgedragen): blijft op 14 Overgedragen verlies; bestuur moet kapitaal-test (5:153 WVV) toetsen.
4. Sluit alle klasse 6 en 7-rekeningen op 31/12 (saldi naar 0); open ze opnieuw op 01/01.
5. Bij Mertens BV — saldo overgedragen winst € 5.920 → balans op 31/12/2026 toont rubriek 14 = € 5.920 (na bestemming AV in april 2027).


**Grondslag**: [[resultaatverwerking]] §overgedragen-resultaat, [[eigen-middelen]] §rubriek-14


## Voorbeelden

> [!example]- Meubelzaak Mertens BV — winst boekjaar 2026 na belasting € 53.600
> **Conclusie**: Dotatie wettelijke reserve verplicht 5% = € 2.680 (eindsaldo € 17.180 < max € 20.000). Reserve € 20.000. Dividend bruto € 25.000, RV € 3.750, netto € 21.250. Saldo overgedragen € 5.920.
>
> **Grondslag**: [[wettelijke-reserve]] §dotatieplicht; [[resultaatverwerking]] §volgorde
>
> **Redenering**: Volgorde wet → reserves → dividend respecteert de hiërarchie. VVPR-bis vereist KMO-vorm + voldoende oude inbreng + houdperiode.

> [!example]- Aurelia Holding NV maakt verlies boekjaar 2026 van € 180.000
> **Conclusie**: Geen winstbestemming — verlies wordt overgedragen via Debet 14 Overgedragen verlies € 180.000; Credit 6921 (omgekeerde resultaatverwerking). Bestuurder moet WVV art. 5:153/7:228 toetsen: indien netto-actief minder dan helft kapitaal → bijzondere AV binnen 2 maanden.
>
> **Grondslag**: [[resultaatverwerking]] §verlies; WVV art. 5:153
>
> **Redenering**: Verlies kan niet aan reserves of dividend; gaat naar overgedragen verlies. Mogelijk alarm-procedure indien materiële erosie eigen vermogen.

> [!example]- Naaiatelier Ninove BV — winst 2026 na belasting € 18.000
> **Conclusie**: GEEN verplichte dotatie wettelijke reserve (al op max). Dotatie beschikbare reserves € 18.000: D 14 € 18.000; C 133 € 18.000. Geen dividend, geen overgedragen winst-saldo.
>
> **Grondslag**: [[wettelijke-reserve]] §maximum; [[resultaatverwerking]] §reserves
>
> **Redenering**: Maximumplafond wettelijke reserve maakt verdere dotatie onnodig; vrije reserves zijn gebruiksvriendelijker.


## Gebaseerd op concepten

[[resultaatverwerking]] · [[wettelijke-reserve]] · [[eigen-middelen]] · [[uitgiftepremie]] · [[bedrijfsresultaat]]
## Voortkomend uit

- **Taken**: 1.1.taak.1
- **Kenniselementen**: 1.1.II.Q, 1.1.II.H
