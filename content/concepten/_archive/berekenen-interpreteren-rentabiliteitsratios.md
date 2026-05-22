---
title: Berekenen en interpreteren van de rentabiliteitsratio's
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.C
- 1.3.II.C.4
- 1.3.I.A
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/berekenen-interpreteren-rentabiliteitsratios.json
gegenereerd_op: '2026-05-21'
---
# Berekenen en interpreteren van de rentabiliteitsratio's 🔗

Competentie om de rentabiliteit van een onderneming te meten via ROE (eigen vermogen) en ROA (totaal activa), in netto en bruto vorm. De stagiair leert het verschil tussen bedrijfsrentabiliteit en netto rentabiliteit, en hoe het financiële hefboomeffect daartussen werkt.



## Stappen

### 1. Klaarzetten van de bouwstenen uit balans en resultatenrekening

Verzamel resultaat, eigen vermogen en totaal activa op de juiste basis (netto en bruto).

**Waarom?** ROE en ROA bestaan in netto- en brutovariant; je moet de juiste cijfers voor elk berekenen.

**📥 Input**:
- Resultatenrekening N → **Resultaat na belasting, financiële kosten, afschrijvingen + waardeverminderingen** _(boekhoudkundig-bedrag)_
- Analytische balans → **Eigen vermogen, totaal activa** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad rentabiliteit → **Vier bouwstenen klaargezet** _(document)_

**🛠️ Hoe**:

1. Lees uit de resultatenrekening van Rotex Roeselare NV: resultaat van het boekjaar na belasting, financiële kosten, en afschrijvingen + waardeverminderingen.
2. Bereken **netto resultaat** = resultaat na belasting.
3. Bereken **bruto resultaat** = resultaat na belasting + financiële kosten + afschrijvingen + waardeverminderingen (= cashflow vóór financiering, conform [[cashflow-analyse]] §resultaat-plus-niet-kaskosten).
4. Neem **EV** en **totaal activa** uit de analytische balans (idealiter gemiddelde van begin- en eind-boekjaar voor stabielere ratio).


**Grondslag**: [[cashflow-analyse]] §cashflow-definitie, [[analytische-balans]] §herwerking

### 2. Berekenen van de rentabiliteit van het eigen vermogen (ROE)

Bereken netto ROE = netto resultaat / EV en bruto ROE = cashflow / EV.

**Waarom?** ROE toont het rendement voor de aandeelhouders; de bruto-variant filtert het effect van afschrijvingen weg.

**📥 Input**:
- Werkblad rentabiliteit → **Netto resultaat, cashflow, EV** _(boekhoudkundig-bedrag)_

**📤 Output**:
- ROE-paar (netto + bruto) → **Twee percentages** _(percentage)_

**🛠️ Hoe**:

1. Pas de formules toe uit [[rentabiliteit-eigen-vermogen-roe]] §nettorentabiliteit en §brutorentabiliteit:
   - **Netto ROE** = (resultaat na belasting / gemiddeld EV) × 100%.
   - **Bruto ROE** = (cashflow / gemiddeld EV) × 100%.
2. Bereken beide en zet ze naast elkaar.
3. Lees af tegen vuistregel: ROE moet minstens de risicovrije rente + risicopremie overschrijden om aantrekkelijk te zijn.
4. Vergelijk met sectormediaan.


> [!example]- Voorbeeld: Rotex Roeselare NV — resultaat na belasting € 2.500.000, afschrijvingen € 1.200.000, financiële kosten € 400.000, gemidd…
> Rotex Roeselare NV — resultaat na belasting € 2.500.000, afschrijvingen € 1.200.000, financiële kosten € 400.000, gemiddeld EV € 12.000.000.
>
> 1. **Bouwstenen** 🧮
>
>    - Netto resultaat: € 2.500.000
>    - Cashflow = € 2.500.000 + € 1.200.000 + € 400.000 = € 4.100.000
>    - Gemiddeld EV: € 12.000.000
>    
>
> 2. **ROE-berekening** 🧮
>
>    Netto ROE = € 2.500.000 / € 12.000.000 × 100% = **20,8%**
>    Bruto ROE = € 4.100.000 / € 12.000.000 × 100% = **34,2%**
>    
>
> 3. **Interpretatie** 💬
>
>    Netto ROE 20,8% — ruim boven risicopremie. Bruto ROE 34,2% bevestigt
>    sterke kasstroomgeneratie. Sector-mediaan industriële NV's: 10-15%.
>    Rotex presteert bovengemiddeld.
>    
>

**Grondslag**: [[rentabiliteit-eigen-vermogen-roe]] §formule (CBN-2011/14)

### 3. Berekenen van de rentabiliteit van het totaal activa (ROA)

Bereken netto ROA en bruto ROA — beide vóór financiële kosten van schulden.

**Waarom?** ROA toont de rendabiliteit van de exploitatie los van financieringsstructuur — direct vergelijkbaar tussen ondernemingen met verschillende schuldgraad.

**📥 Input**:
- Werkblad rentabiliteit → **Resultaat + financiële kosten, balanstotaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- ROA-paar (netto + bruto) → **Twee percentages** _(percentage)_

**🛠️ Hoe**:

1. Pas de formules toe uit [[rentabiliteit-totaal-activa-roa]] §nettorentabiliteit en §brutorentabiliteit:
   - **Netto ROA** = (resultaat na belasting + financiële kosten van schulden) / gemiddeld balanstotaal × 100%.
   - **Bruto ROA** = (cashflow) / gemiddeld balanstotaal × 100%.
2. Bereken beide.
3. Vergelijk netto ROA met de gemiddelde rente op schulden — verschil = hefboommarge.


> [!example]- Voorbeeld: Rotex Roeselare NV — balanstotaal gemiddeld € 25.000.000
> Rotex Roeselare NV — balanstotaal gemiddeld € 25.000.000.
>
> 1. **ROA-berekening** 🧮
>
>    Netto ROA = (€ 2.500.000 + € 400.000) / € 25.000.000 × 100% = **11,6%**
>    Bruto ROA = € 4.100.000 / € 25.000.000 × 100% = **16,4%**
>    
>
> 2. **Interpretatie** 💬
>
>    Netto ROA 11,6% > gemiddelde rente schulden (geschat 3%) → positieve
>    hefboom. Vreemd vermogen versterkt rendement op EV — verklaart waarom
>    ROE (20,8%) boven ROA (11,6%) ligt.
>    
>

**Grondslag**: [[rentabiliteit-totaal-activa-roa]] §formule (CBN-2011/14)

### 4. Verklaren van het verschil tussen ROE en ROA via hefboomeffect

Toon hoe schuldfinanciering ROE optilt boven ROA en wanneer dat omslaat in destructief effect.

**Waarom?** Een hoge ROE zonder hefboom-analyse is misleidend — kan teken zijn van risicovolle financieringsstructuur.

**📥 Input**:
- ROE en ROA uit stap 2 en 3 → **Beide percentages** _(percentage)_
- Debt-equity ratio uit [[berekenen-interpreteren-solvabiliteitsratios]] → **Hefboomgraad** _(percentage)_

**📤 Output**:
- Hefboom-paragraaf in rapport → **Diagnose financieringseffect** _(document)_

**🛠️ Hoe**:

1. Bereken het verschil ROE – ROA.
2. Verklaar het: als ROA > gemiddelde kostprijs vreemd vermogen, dan tilt elke euro extra schuld het ROE op. Omgekeerd vergroot ze het verlies.
3. Combineer met debt-equity uit competentie [[berekenen-interpreteren-solvabiliteitsratios]].
4. Conclusie: positief hefboomeffect = duurzaam zolang ROA stabiel boven kostprijs schuld blijft; signaal als ROA daalt richting kostprijs schuld.


**Grondslag**: [[rentabiliteit-eigen-vermogen-roe]] §hefboom-effect, vakdoctrine

> [!warning]- Een hoge ROE met negatieve hefboom betekent niet automatisch een gezonde onderneming.
>
> _Vaak fout gedaan_: ROE als de enige rentabiliteits-meter gebruiken zonder ROA en debt-equity ernaast te zetten.
>
> _Grondslag_: [[rentabiliteit-totaal-activa-roa]] §waarom-ROA

### 5. Plaatsen in historische evolutie en sectorvergelijking

Bereken ROE en ROA voor drie boekjaren en vergelijk met sectormediaan.

**Waarom?** Stijgende rentabiliteit in vlakke sector wijst op bedrijfsspecifieke kracht; dalende rentabiliteit in groeiende sector op zwakte.

**📥 Input**:
- ROE/ROA voor N, N-1, N-2 → **Zes percentages** _(percentage)_
- Sectormediaan → **Sectorale ratio's** _(percentage)_

**📤 Output**:
- Rentabiliteit-trendparagraaf → **Diagnose evolutie** _(document)_

**🛠️ Hoe**:

1. Bereken ROE en ROA op N, N-1 en N-2 conform [[historische-evolutie-financiele-analyse]] §3-5-boekjaren.
2. Isoleer eenmalige effecten (zie [[voorbereiden-financiele-analyse]] stap 4) — bv. uitzonderlijke meerwaarden.
3. Bereken een **recurrente ROE** = ROE zonder eenmalige effecten — vergelijk dat met sector.
4. Plaats in tabelvorm en interpreteer.


**Grondslag**: [[historische-evolutie-financiele-analyse]] §onderscheid-eenmalig-vs-structureel, [[sectorvergelijking-financiele-analyse]] §sectorgrenzen


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.taak.1`
