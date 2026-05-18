---
title: Berekenen en interpreteren van de liquiditeitsratio's
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.C
- 1.3.II.C.2
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/berekenen-interpreteren-liquiditeitsratios.json
gegenereerd_op: '2026-05-18'
---
# Berekenen en interpreteren van de liquiditeitsratio's 🤖

Competentie om vanuit de analytische balans de liquiditeitsratio's (current, quick, cash) te berekenen en in evolutie en sectorvergelijking te interpreteren. De stagiair leert dat één ratio nooit volstaat — current + quick moeten samen gelezen worden.


## Stappen

### 1. Vertrekken vanuit de analytische balans

Gebruik de geherklasseerde analytische balans als basis, niet de officiële balans.

**Waarom?** Herklassificaties (zoals effectenportefeuille van vast naar vlottend) wijzigen de teller of noemer en dus de ratio.

**📥 Input**:
- Analytische balans uit competentie [[opstellen-analytische-balans]] → **Vier blokken activa, vier blokken passiva** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad liquiditeit → **Te gebruiken bedragen + bron-cellen** _(document)_

**🛠️ Hoe**:

1. Open de analytische balans uit [[analytische-balans]] §herwerking.
2. Markeer de cellen die je nodig hebt: voorraden, vorderingen ≤ 1 jaar, geldbeleggingen, liquide middelen, schulden ≤ 1 jaar.
3. Noteer per cel of er een herklassificatie is gebeurd (bv. effectenportefeuille verplaatst).
4. Zet de bedragen klaar in je werkblad.


**Grondslag**: [[analytische-balans]] §herwerking

### 2. Berekenen van de current ratio (algemene liquiditeit)

Bereken (vlottende activa) / (schulden ≤ 1 jaar).

**Waarom?** Dit toont of de onderneming haar korte schulden kan dekken met haar volledige korte termijn-actief.

**📥 Input**:
- Werkblad liquiditeit uit stap 1 → **Voorraden + vorderingen + geldbeleggingen + liquide** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Current ratio → **Verhouding (kommagetal of percentage)** _(percentage)_

**🛠️ Hoe**:

1. Tel volgens [[current-ratio]] §vlottende-activa-tegenover-korte-schulden alle vlottende activa op: voorraden + vorderingen ≤ 1 jaar + geldbeleggingen + liquide middelen + overlopende rekeningen actief.
2. Tel alle schulden ≤ 1 jaar + overlopende rekeningen passief op.
3. Deel teller door noemer.
4. Lees af: > 1 = comfortzone; ongeveer 1 = grens; < 1 = ontoereikend zonder her-onderhandeling.
5. Vergelijk met de sectormediaan ([[sectorvergelijking-financiele-analyse]] §mediaan-boven-gemiddelde).


> [!example]- Voorbeeld: Rotex Roeselare NV — current ratio voor boekjaar N
> Rotex Roeselare NV — current ratio voor boekjaar N.
>
> 1. **Bouwstenen** 📊
>
>    | Element                       | Bedrag       |
>    |-------------------------------|-------------:|
>    | Voorraden                     | € 2.500.000  |
>    | Vorderingen ≤ 1 jaar          | € 3.800.000  |
>    | Geldbeleggingen + liquide     | € 1.500.000  |
>    | **Vlottende activa totaal**   | **€ 7.800.000** |
>    | Schulden ≤ 1 jaar             | € 4.800.000  |
>    
>
> 2. **Berekening** 🧮
>
>    Current ratio = € 7.800.000 / € 4.800.000 = **1,63**
>    
>
> 3. **Interpretatie** 💬
>
>    1,63 > 1 → comfortzone. Sectormediaan voor industriële NV's ligt rond
>    1,3-1,5. Rotex zit boven mediaan — gezonde liquiditeit op het eerste
>    gezicht. Test wordt verfijnd met quick ratio (stap 3).
>    
>

**Grondslag**: [[current-ratio]] §formule, vakdoctrine

### 3. Berekenen van de quick ratio (verfijnde liquiditeit)

Bereken (vlottende activa – voorraden) / (schulden ≤ 1 jaar).

**Waarom?** Voorraden zijn de minst liquide vlottende activa — door ze weg te nemen zie je de echte korte-termijn-betaalcapaciteit.

**📥 Input**:
- Werkblad liquiditeit uit stap 1 → **Vlottende activa zonder voorraden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Quick ratio → **Verhouding (kommagetal)** _(percentage)_

**🛠️ Hoe**:

1. Neem de teller van current ratio en trek de voorraden af volgens [[quick-ratio]] §vlottende-activa-zonder-voorraden.
2. De noemer blijft schulden ≤ 1 jaar.
3. Deel teller door noemer.
4. Lees af: > 1 = sterke acid test; tussen 0,7 en 1 = aanvaardbaar voor onderneming met snel voorraadrotatie; < 0,7 = zwak.
5. Combineer met current ratio: groot gat tussen current en quick → voorraden domineren — sectorafhankelijk normaal of risicovol.


> [!example]- Voorbeeld: Rotex Roeselare NV — quick ratio voor boekjaar N
> Rotex Roeselare NV — quick ratio voor boekjaar N.
>
> 1. **Berekening** 🧮
>
>    Quick ratio = (€ 7.800.000 – € 2.500.000) / € 4.800.000
>                = € 5.300.000 / € 4.800.000
>                = **1,10**
>    
>
> 2. **Interpretatie** 💬
>
>    Quick ratio 1,10 > 1 — Rotex kan haar korte schulden dekken zonder een
>    enkele voorraadpost te verkopen. Verschil current (1,63) – quick (1,10)
>    = 0,53 wijst op significant voorraadbeslag. Normaal voor industriële NV;
>    geen alarmsignaal.
>    
>

**Grondslag**: [[quick-ratio]] §formule, vakdoctrine

> [!warning]- Voor handelsondernemingen met snelle voorraadrotatie is een quick ratio < 1 vaak gezond.
>
> _Vaak fout gedaan_: Mechanisch < 1 = problematisch toepassen ongeacht de sector.
>
> _Grondslag_: [[sectorvergelijking-financiele-analyse]] §sectorgrenzen

### 4. Vergelijken met sectormediaan en historische evolutie

Plaats current en quick ratio naast sectormediaan en de eigen evolutie over drie boekjaren.

**Waarom?** Een ratio krijgt pas betekenis door vergelijking — absoluut zegt het te weinig.

**📥 Input**:
- Berekende ratio's huidig boekjaar → **Current + quick ratio** _(percentage)_
- Ratio's N-1 en N-2 → **Idem voorgaande boekjaren** _(percentage)_
- Sectorgegevens (NBB, Belfius, Bel-first) → **Sectormediaan + spreiding** _(percentage)_

**📤 Output**:
- Interpretatie-paragraaf → **Diagnose liquiditeit** _(document)_

**🛠️ Hoe**:

1. Bereken current en quick ratio op N, N-1 en N-2.
2. Zet ze in een evolutie-tabel ([[historische-evolutie-financiele-analyse]] §3-5-boekjaren).
3. Vergelijk met sectormediaan; de mediaan is robuuster dan het gemiddelde tegen uitschieters.
4. Trek conclusies: dalende ratio's met vlakke sector = bedrijfsspecifieke verslechtering; gelijke beweging als sector = conjunctuur.
5. Documenteer in één paragraaf met cijfers + interpretatie.


> [!example]- Voorbeeld: Rotex Roeselare NV — evolutie en sectorvergelijking
> Rotex Roeselare NV — evolutie en sectorvergelijking.
>
> 1. **Evolutie- en vergelijkingstabel** 🧮
>
>    | Ratio          | N    | N-1  | N-2  | Sectormediaan |
>    |----------------|-----:|-----:|-----:|--------------:|
>    | Current ratio  | 1,63 | 1,52 | 1,48 | 1,40          |
>    | Quick ratio    | 1,10 | 1,02 | 0,98 | 0,95          |
>    
>
> 2. **Interpretatie** 💬
>
>    Beide ratio's stijgen geleidelijk en liggen boven sectormediaan.
>    Liquiditeitspositie versterkt zich; geen knipperlicht.
>    
>

**Grondslag**: [[sectorvergelijking-financiele-analyse]] §sectorgrenzen, [[historische-evolutie-financiele-analyse]] §3-5-boekjaren


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.taak.1`
