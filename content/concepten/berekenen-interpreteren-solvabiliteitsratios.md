---
title: Berekenen en interpreteren van de solvabiliteitsratio's
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.C
- 1.3.I.D.5
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/berekenen-interpreteren-solvabiliteitsratios.json
gegenereerd_op: '2026-05-18'
---
# Berekenen en interpreteren van de solvabiliteitsratio's 🤖


## Stappen

### 1. Vertrekken vanuit de analytische balans

Gebruik de geherklasseerde analytische balans, met name het analytische eigen vermogen.

**Waarom?** Herklassificaties van uitgestelde belastingen of onuitkeerbare reserves wijzigen het echte economische eigen vermogen.

**📥 Input**:
- Analytische balans → **Eigen vermogen, totaal schulden, balanstotaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad solvabiliteit → **EV + schulden klaargezet** _(document)_

**🛠️ Hoe**:

1. Open de analytische balans uit [[opstellen-analytische-balans]].
2. Neem het **analytische eigen vermogen** (inclusief het permanent deel van uitgestelde belastingen).
3. Neem het **totaal vreemd vermogen** = voorzieningen (schuldachtig deel) + schulden > 1 jaar + schulden ≤ 1 jaar + overlopende rekeningen passief.
4. Controleer dat EV + VV = balanstotaal.


**Grondslag**: [[analytische-balans]] §herklassificaties-voor-analyse

### 2. Berekenen van de klassieke solvabiliteitsratio

Bereken eigen vermogen / balanstotaal × 100%.

**Waarom?** Toont welk deel van het actief gefinancierd is met eigen middelen — een eerste lakmoesproef voor financiële autonomie.

**📥 Input**:
- Werkblad solvabiliteit uit stap 1 → **EV en balanstotaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Solvabiliteitsratio → **Percentage (kommagetal × 100)** _(percentage)_

**🛠️ Hoe**:

1. Pas de formule toe uit [[solvabiliteitsratio]] §eigen-vermogen-tegenover-balanstotaal: EV / balanstotaal × 100%.
2. Lees af tegen vuistregels (vakdoctrine): > 35% = sterk; 20-35% = aanvaardbaar; < 20% = zwak.
3. Pas de vuistregels aan op sector — vastgoed en holdings hebben structureel lagere solvabiliteit, dienstverlening hogere.
4. Vergelijk met sectormediaan ([[sectorvergelijking-financiele-analyse]] §sectorgrenzen).


> [!example]- Voorbeeld: Rotex Roeselare NV — analytisch EV € 12.150.000, balanstotaal € 25.800.000
> Rotex Roeselare NV — analytisch EV € 12.150.000, balanstotaal € 25.800.000.
>
> 1. **Berekening** 🧮
>
>    Solvabiliteit = € 12.150.000 / € 25.800.000 × 100% = **47,1%**
>    
>
> 2. **Interpretatie** 💬
>
>    47,1% — ruim boven de 35%-grens. Sterke financiële autonomie. Industriële NV
>    sector-mediaan: ongeveer 35%. Rotex zit duidelijk boven mediaan.
>    
>

**Grondslag**: [[solvabiliteitsratio]] §klassieke-formule, vakdoctrine

### 3. Berekenen van de debt-equity ratio (schuldhefboom)

Bereken totaal vreemd vermogen / eigen vermogen.

**Waarom?** Spiegelt de hefboomwerking: hoeveel schuld draagt elke euro EV?

**📥 Input**:
- Werkblad solvabiliteit → **EV + totaal VV** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Debt-equity ratio → **Verhouding (kommagetal)** _(percentage)_

**🛠️ Hoe**:

1. Pas de formule toe uit [[debt-equity-ratio]] §schulden-totaal-tegenover-eigen-vermogen: VV / EV.
2. Lees af: < 1 = EV draagt meer dan schuld; 1-2 = matig hefboomgebruik; > 2 = zware hefboom.
3. Combineer met rentabiliteit: hoge hefboom is positief als rendement op activa boven kostprijs van schuld ligt — anders is het destructief.
4. Toets aan eventuele ratio-covenants in kredietovereenkomsten ([[ratio-covenants]] §typische-covenants).


> [!example]- Voorbeeld: Rotex Roeselare NV — VV = € 13.650.000, EV = € 12.150.000
> Rotex Roeselare NV — VV = € 13.650.000, EV = € 12.150.000.
>
> 1. **Berekening** 🧮
>
>    Debt-equity = € 13.650.000 / € 12.150.000 = **1,12**
>    
>
> 2. **Interpretatie** 💬
>
>    Hefboom 1,12 — elke euro EV draagt € 1,12 schuld. Matig hefboomgebruik.
>    Zolang ROA boven gemiddelde kostprijs vreemd vermogen ligt, werkt deze
>    hefboom positief op ROE.
>    
>

**Grondslag**: [[debt-equity-ratio]] §formule, vakdoctrine

> [!warning]- Beoordeel debt-equity altijd samen met rentabiliteit op totaal activa.
>
> _Vaak fout gedaan_: Een hoge debt-equity ratio per definitie als probleem zien — terwijl hij in winstgevende sectoren juist het ROE versterkt.
>
> _Grondslag_: [[debt-equity-ratio]] §hefboomwerking

### 4. Toetsen aan ratio-covenants uit kredietovereenkomsten

Vergelijk de berekende ratio's met de drempels die in bankcontracten staan.

**Waarom?** Schending van een covenant kan leiden tot vervroegde opeisbaarheid van krediet — een liquiditeitsschok die niet uit de cijfers zelf blijkt.

**📥 Input**:
- Kredietovereenkomsten + addenda → **Solvency covenant, leverage covenant, dekkingsratio's** _(document)_
- Berekende ratio's uit stap 2 en 3 → **Solvabiliteit + debt-equity** _(percentage)_

**📤 Output**:
- Compliance-tabel → **Per covenant: drempel, actueel, marge, signaal** _(conclusie)_

**🛠️ Hoe**:

1. Vraag de kredietovereenkomsten op bij de cliënt.
2. Identificeer de financial covenants ([[ratio-covenants]] §typische-covenants): solvabiliteitsdrempel (vaak min. 25-30%), leverage maximum (vaak max. 3-4 keer EBITDA), interest coverage.
3. Plaats de berekende ratio's naast de drempels.
4. Bereken de marge: hoeveel kan de ratio nog verslechteren vooraleer breach?
5. Bij marge < 10%: flag als knipperlicht in het rapport. Bij marge negatief: noodsignaal — informeer cliënt onmiddellijk.


> [!example]- Voorbeeld: Rotex Roeselare NV — bankcovenant: solvabiliteit ≥ 30%, debt-equity ≤ 1,5
> Rotex Roeselare NV — bankcovenant: solvabiliteit ≥ 30%, debt-equity ≤ 1,5.
>
> 1. **Compliance-tabel** 🧮
>
>    | Covenant                | Drempel | Actueel | Marge       | Signaal |
>    |-------------------------|--------:|--------:|------------:|---------|
>    | Solvabiliteit ≥ 30%     | 30%     | 47,1%   | + 17,1 ppt  | OK      |
>    | Debt-equity ≤ 1,5       | 1,5     | 1,12    | – 0,38      | OK      |
>    
>

**Grondslag**: [[ratio-covenants]] §testdatum-en-testfrequentie


