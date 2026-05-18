---
title: Uitvoeren van een horizontale en verticale analyse van de jaarrekening
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.I.C
- 1.3.II.C
- 1.3.II.B.3
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-horizontale-verticale-analyse.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van een horizontale en verticale analyse van de jaarrekening 🤖


## Stappen

### 1. Voorbereiden van een werkmatrix over meerdere boekjaren

Zet balans en resultatenrekening van drie tot vijf boekjaren naast elkaar in één werkblad.

**Waarom?** Pas in matrixvorm worden trends en structuur-verschuivingen zichtbaar.

**📥 Input**:
- Werkmap met jaarrekeningen N tot N-4 → **Officiële balans + resultatenrekening per boekjaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Vergelijkingsmatrix → **Posten als rijen, boekjaren als kolommen** _(document)_

**🛠️ Hoe**:

1. Open de gedownloade jaarrekeningen uit competentie [[voorbereiden-financiele-analyse]] stap 3.
2. Maak één werkblad met posten in rijen en boekjaren in kolommen (N, N-1, N-2, eventueel N-3, N-4).
3. Controleer dat alle bedragen in dezelfde eenheid staan (euro, zonder duizendtal-verschillen).
4. Bij wijziging waarderingsregels: noteer dit in een kolom "Toelichting" — hercijferen of vergelijking met voorbehoud.


**Grondslag**: [[historische-evolutie-financiele-analyse]] §3-5-boekjaren

### 2. Uitvoeren van de horizontale analyse (evolutie in de tijd)

Bereken per post de procentuele verandering tegenover een basisjaar of het vorige boekjaar.

**Waarom?** Toont hoe elke balans- of resultatenpost zich ontwikkelt — versnelt opsporen van trends.

**📥 Input**:
- Vergelijkingsmatrix → **Bedragen per post per boekjaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Horizontale evolutie-tabel → **Per post een index of een %-wijziging** _(percentage)_

**🛠️ Hoe**:

1. Kies een basisjaar: meestal N-2 of het oudste beschikbare boekjaar.
2. Pas per post de formule toe uit [[horizontale-analyse-jaarrekening]] §vergelijking-met-basisjaar:
   - **Index**: post-N / post-basisjaar × 100. Een index van 120 = +20% groei.
   - Of **%-wijziging**: (post-N – post-N-1) / post-N-1 × 100%.
3. Bereken voor minstens balans-totalen + omzet + bedrijfsresultaat + EV + schulden.
4. Markeer posten met evolutie > 20% per jaar als aandachtspunt — vaak materieel.
5. Verklaar elk afwijking via de toelichting of via gesprek met cliënt.


> [!example]- Voorbeeld: Rotex Roeselare NV — omzet en bedrijfsresultaat over drie boekjaren
> Rotex Roeselare NV — omzet en bedrijfsresultaat over drie boekjaren.
>
> 1. **Horizontale evolutie-tabel** 🧮
>
>    | Post                | N-2 (basis)  | N-1          | N            | Index N    | %-wijz. N vs N-1 |
>    |---------------------|-------------:|-------------:|-------------:|-----------:|-----------------:|
>    | Omzet               | € 44.000.000 | € 47.000.000 | € 50.000.000 | 113,6      | + 6,4%           |
>    | Bedrijfsresultaat   | € 2.200.000  | € 2.700.000  | € 3.500.000  | 159,1      | + 29,6%          |
>    | Eigen vermogen      | € 10.500.000 | € 11.200.000 | € 12.000.000 | 114,3      | + 7,1%           |
>    
>
> 2. **Interpretatie** 💬
>
>    Bedrijfsresultaat groeit sneller dan omzet (index 159 vs 114) →
>    operationele hefboomwerking positief, marges verbeteren.
>    EV-groei volgt resultaat — winst wordt geherinvesteerd.
>    
>

**Grondslag**: [[horizontale-analyse-jaarrekening]] §methode, KB WVV verplicht vergelijkende cijfers

### 3. Uitvoeren van de verticale analyse (structuur op één moment)

Druk elke balanspost uit als % van balanstotaal en elke resultatenpost als % van omzet.

**Waarom?** Toont de samenstelling — welk aandeel heeft elke post in het geheel.

**📥 Input**:
- Vergelijkingsmatrix → **Bedragen per post per boekjaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Verticale structuur-tabel → **Per post een % van het totaal** _(percentage)_

**🛠️ Hoe**:

1. Bereken voor de balans volgens [[verticale-analyse-jaarrekening]] §balanspost-als-%-van-balanstotaal: post / balanstotaal × 100%.
2. Bereken voor de resultatenrekening volgens [[verticale-analyse-jaarrekening]] §resultatenpost-als-%-van-omzet: post / omzet × 100%.
3. Doe dit voor N, N-1 en N-2.
4. Plaats verticale percentages naast elkaar — zo zie je hoe de structuur evolueert.
5. Vergelijk met sectormediaan ([[sectorvergelijking-financiele-analyse]] §sectorgrenzen).


> [!example]- Voorbeeld: Rotex Roeselare NV — verticale structuur balans N (balanstotaal € 25.800.000)
> Rotex Roeselare NV — verticale structuur balans N (balanstotaal € 25.800.000).
>
> 1. **Verticale structuur-tabel** 🧮
>
>    | Post                          | Bedrag        | % van balanstotaal |
>    |-------------------------------|--------------:|-------------------:|
>    | Vaste activa                  | € 18.000.000  | 69,8%              |
>    | Voorraden                     | € 2.500.000   | 9,7%               |
>    | Vorderingen + liquide         | € 5.300.000   | 20,5%              |
>    | Eigen vermogen                | € 12.000.000  | 46,5%              |
>    | Voorzieningen                 | € 1.000.000   | 3,9%               |
>    | Schulden > 1 jaar             | € 8.000.000   | 31,0%              |
>    | Schulden ≤ 1 jaar             | € 4.800.000   | 18,6%              |
>    
>
> 2. **Interpretatie** 💬
>
>    70% vaste activa — kapitaalintensief productiebedrijf, typisch industrieel.
>    EV 46,5% sterk; permanent kapitaal (EV + voorzieningen + LT schuld) =
>    81,4% dekt vaste activa van 69,8% ruim → werkkapitaalreserve bevestigd.
>    
>

**Grondslag**: [[verticale-analyse-jaarrekening]] §methode

### 4. Combineren van horizontale en verticale analyse tot één diagnose

Lees de twee tabellen samen om structuur-verschuivingen te detecteren.

**Waarom?** Een post die % gelijk blijft maar in absoluut bedrag groeit, is iets anders dan een post die in % stijgt.

**📥 Input**:
- Horizontale evolutie-tabel → **Indexen of %-wijzigingen** _(percentage)_
- Verticale structuur-tabel → **%-aandelen in totaal** _(percentage)_

**📤 Output**:
- Structuurparagraaf in rapport → **Diagnose evolutie + structuur** _(document)_

**🛠️ Hoe**:

1. Leg de twee tabellen naast elkaar.
2. Zoek posten die zowel horizontaal sterk groeien als verticaal aan gewicht winnen → structuurverschuiving.
3. Pas materialiteits-test toe volgens [[materieel-belang-jaarrekening]] §relatief: een post die nog onder 5% van het totaal blijft is veelal niet materieel ondanks % groei.
4. Schrijf één paragraaf die de belangrijkste verschuivingen verklaart.


**Grondslag**: [[horizontale-analyse-jaarrekening]] §combinatie, [[verticale-analyse-jaarrekening]] §combinatie

> [!warning]- Lees horizontaal en verticaal samen voor je conclusies trekt.
>
> _Vaak fout gedaan_: Alleen %-wijzigingen rapporteren zonder het verticale gewicht — kleine posten met grote %-stijging worden onterecht alarmerend.
>
> _Grondslag_: [[materieel-belang-jaarrekening]] §relatief


