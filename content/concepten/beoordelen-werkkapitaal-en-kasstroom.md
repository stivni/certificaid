---
title: Beoordelen van het werkkapitaal en de kasstroom van een onderneming
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.C
- 1.3.II.C.2
- 1.3.II.C.3
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/beoordelen-werkkapitaal-en-kasstroom.json
gegenereerd_op: '2026-05-18'
---
# Beoordelen van het werkkapitaal en de kasstroom van een onderneming 🤖


## Stappen

### 1. Berekenen van het werkkapitaal in twee richtingen

Bereken werkkapitaal volgens vlottende-activa-methode én permanent-kapitaal-methode.

**Waarom?** Beide methodes moeten hetzelfde getal opleveren — controle op consistente herwerking van de balans.

**📥 Input**:
- Analytische balans → **Vier blokken activa, vier blokken passiva** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkkapitaal in € → **Eén getal, met beide berekeningswijzen als controle** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bereken volgens [[werkkapitaal]] §absolute-tegenhanger op twee manieren:
   - **Methode 1 (van onder)**: Vlottende activa – schulden ≤ 1 jaar.
   - **Methode 2 (van boven)**: Permanent kapitaal – vaste activa.
2. Vergelijk: beide moeten identiek zijn. Verschil = rekenfout of vergeten herklassificatie.
3. Bereken het werkkapitaal op N, N-1 en N-2 voor evolutie-analyse.


> [!example]- Voorbeeld: Rotex Roeselare NV — werkkapitaal-controle
> Rotex Roeselare NV — werkkapitaal-controle.
>
> 1. **Beide methodes** 🧮
>
>    Methode 1: € 7.800.000 – € 4.800.000 = € 3.000.000
>    Methode 2: € 21.000.000 – € 18.000.000 = € 3.000.000
>    → Beide methodes geven € 3.000.000 → consistent.
>    
>

**Grondslag**: [[werkkapitaal]] §absolute-tegenhanger

### 2. Beoordelen van de behoefte aan werkkapitaal

Bereken werkkapitaalbehoefte als vorderingen ≤ 1 jaar + voorraden – leveranciersschulden.

**Waarom?** Toont hoeveel kapitaal de exploitatiecyclus permanent vraagt — niet hetzelfde als beschikbaar werkkapitaal.

**📥 Input**:
- Analytische balans → **Voorraden, vorderingen ≤ 1 jaar, leveranciersschulden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkkapitaalbehoefte in € → **Behoefte op N + evolutie** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bereken **werkkapitaalbehoefte (operationele cyclus)**: voorraden + vorderingen ≤ 1 jaar – leveranciers- en overige niet-bancaire korte schulden.
2. Vergelijk werkkapitaal (stap 1) met werkkapitaalbehoefte:
   - Werkkapitaal > werkkapitaalbehoefte → kasoverschot, comfortabel.
   - Werkkapitaal < werkkapitaalbehoefte → kastekort, gefinancierd via bankkrediet KT.
3. Plaats de evolutie van werkkapitaalbehoefte naast omzetgroei — sterk dalende behoefte zonder omzetdaling = efficiëntiewinst op werkkapitaal.


> [!example]- Voorbeeld: Rotex Roeselare NV — werkkapitaalbehoefte
> Rotex Roeselare NV — werkkapitaalbehoefte.
>
> 1. **Bouwstenen** 📊
>
>    | Post                                  | Bedrag       |
>    |---------------------------------------|-------------:|
>    | Voorraden                             | € 2.500.000  |
>    | Vorderingen ≤ 1 jaar (handelsvord.)   | € 3.500.000  |
>    | Leveranciersschulden                  | € 2.800.000  |
>    
>
> 2. **Berekening** 🧮
>
>    Werkkapitaalbehoefte = € 2.500.000 + € 3.500.000 – € 2.800.000 = **€ 3.200.000**
>    Werkkapitaal = € 3.000.000
>    → Werkkapitaal (3M) < Werkkapitaalbehoefte (3,2M) → klein kastekort van € 200.000.
>    
>
> 3. **Interpretatie** 💬
>
>    Kastekort € 200.000 wordt overbrugd via kort bankkrediet of overschrijding
>    rekening-courant. Niet alarmerend bij Rotex (sterke solvabiliteit) maar
>    wel een aandachtspunt: kleine omzetdaling zou de behoefte verder vergroten.
>    
>

**Grondslag**: [[werkkapitaal]] §positief-werkkapitaal, vakdoctrine

### 3. Berekenen van de cashflow uit de resultatenrekening

Bereken cashflow = resultaat na belasting + afschrijvingen + waardeverminderingen + voorzieningen.

**Waarom?** Cashflow toont de werkelijke kasgeneratie — los van afschrijvingen en boekhoudkundige niet-kasbewegingen.

**📥 Input**:
- Resultatenrekening N → **Resultaat, afschrijvingen, waardeverminderingen, voorzieningen-mutatie** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Cashflow in € → **Bedrag + bouwstenen** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas de formule toe uit [[cashflow-analyse]] §resultaat-plus-niet-kaskosten: resultaat na belasting + afschrijvingen + waardeverminderingen + dotaties voorzieningen – terugnames voorzieningen.
2. Deze "vereenvoudigde cashflow" benadert de operationele kasgeneratie zonder volledig kasstroomoverzicht.
3. Vergelijk met afschrijvingen alleen — als cashflow ≈ afschrijvingen, dan is de onderneming nauwelijks winstgevend in cash.
4. Bereken cashflow/EV en cashflow/balanstotaal — alternatieve rentabiliteitsmaten ([[rentabiliteit-eigen-vermogen-roe]] §brutorentabiliteit).


> [!example]- Voorbeeld: Rotex Roeselare NV — cashflow boekjaar N
> Rotex Roeselare NV — cashflow boekjaar N.
>
> 1. **Bouwstenen** 🧮
>
>    - Resultaat na belasting: € 2.500.000
>    - Afschrijvingen: € 1.200.000
>    - Waardeverminderingen: € 100.000
>    - Netto-dotatie voorzieningen: € 300.000
>    
>
> 2. **Berekening** 🧮
>
>    Cashflow = € 2.500.000 + € 1.200.000 + € 100.000 + € 300.000 = **€ 4.100.000**
>    Cashflow/omzet = € 4.100.000 / € 50.000.000 = 8,2%
>    
>

**Grondslag**: [[cashflow-analyse]] §resultaat-plus-niet-kaskosten (CBN-2011/14)

### 4. Confronteren van cashflow met financiële verplichtingen

Toets of de cashflow voldoende is om aflossingen, rentelasten en investeringen te dragen.

**Waarom?** Dit is de echte test voor financiële houdbaarheid — winst zegt niets als de kas leeg loopt.

**📥 Input**:
- Cashflow uit stap 3 → **Operationele cashflow** _(boekhoudkundig-bedrag)_
- Aflossingstabel + investeringsplan → **LT aflossingen + capex** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Dekkings-tabel → **Per categorie: dekking ja/nee** _(conclusie)_

**🛠️ Hoe**:

1. Verzamel de geplande aflossingen op lange-termijn-schulden voor het komende jaar.
2. Voeg de geschatte investeringen (capex) toe op basis van het bestuursverslag of investeringsplan.
3. Tel rentelasten op (uit resultatenrekening of geprojecteerd).
4. Toets: cashflow – aflossingen – capex – rentelasten = vrije kasstroom.
5. Positief = onderneming financiert zichzelf; negatief = bijkomende financiering of EV-injectie nodig.


> [!example]- Voorbeeld: Rotex Roeselare NV — vrije kasstroomtest jaar N+1
> Rotex Roeselare NV — vrije kasstroomtest jaar N+1.
>
> 1. **Dekkings-tabel** 🧮
>
>    | Element                         | Bedrag       |
>    |---------------------------------|-------------:|
>    | Cashflow                        | + € 4.100.000 |
>    | Aflossingen LT-schulden         | – € 1.200.000 |
>    | Capex (investeringen N+1)       | – € 1.500.000 |
>    | Rentelasten                     | – € 400.000  |
>    | **Vrije kasstroom**             | **+ € 1.000.000** |
>    
>
> 2. **Interpretatie** 💬
>
>    Vrije kasstroom € 1M positief — Rotex genereert zelf voldoende kas om
>    aflossingen + capex + rente te dragen. Geen externe financieringsbehoefte.
>    
>

**Grondslag**: [[cashflow-analyse]] §cashflow-als-waarderingsfactor, vakdoctrine

> [!warning]- Trek altijd ook de geplande capex af, niet alleen de aflossingen.
>
> _Vaak fout gedaan_: Vrije kasstroom berekenen zonder capex — onderschat de werkelijke financieringsbehoefte van een groeiende onderneming.
>
> _Grondslag_: [[cashflow-analyse]] §cashflow-als-waarderingsfactor


