---
title: Rentabiliteit van het eigen vermogen (ROE)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.I.A
- 1.3.II.C
- 1.3.taak.1
- 1.9.V
- 1.9.V.B
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/rentabiliteit-eigen-vermogen-roe.json
gegenereerd_op: '2026-05-21'
---
# Rentabiliteit van het eigen vermogen (ROE) 🔗

Meten welk rendement de onderneming behaalt op het eigen vermogen — het kapitaal dat de aandeelhouders hebben ingezet of laten staan. ROE staat voor 'Return On Equity'. Het kerngetal voor aandeelhouders die willen weten of hun ingezet kapitaal voldoende oplevert.

> [!info] Behoort tot: [[doelstellingen-financiele-analyse]]



## Bouwstenen

### Nettorentabiliteit van het eigen vermogen ⚖️

Verhouding tussen de winst (of verlies) van het boekjaar na belastingen — vóór resultaatverwerking — en het eigen vermogen op balansdatum.

**Waarom?** Geeft het direct uitkeerbare of beschikbare rendement aan voor de aandeelhouder — wat overblijft nadat de fiscus is bediend.



Rotex Roeselare NV: winst boekjaar € 2.500.000; eigen vermogen € 12.000.000. Nettorentabiliteit EV = € 2.500.000 / € 12.000.000 = 20,8 %.

_Grondslag: CBN-2011/14 §rentabiliteit eigen vermogen_

### Brutorentabiliteit van het eigen vermogen ⚖️

Verhouding tussen de cashflow (nettoresultaat na belasting + niet-kaskosten zoals afschrijvingen, waardeverminderingen en voorzieningen) en het eigen vermogen.

**Waarom?** Filtert boekhoudkundige niet-kaselementen weg en toont wat de onderneming echt aan middelen genereert tegenover het eigen vermogen.



Rotex Roeselare NV: nettoresultaat € 2.500.000 + afschrijvingen € 1.500.000 + waardeverminderingen € 200.000 = cashflow € 4.200.000. Brutorentabiliteit EV = € 4.200.000 / € 12.000.000 = 35,0 %.

_Grondslag: CBN-2011/14 §rentabiliteit eigen vermogen_


## Berekening

### Berekening ROE (netto en bruto)

**Nettorentabiliteit van het eigen vermogen** 
```
netto ROE = winst (verlies) van het boekjaar / eigen vermogen
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `winst van het boekjaar` | Resultaat na belastingen, vóór resultaatverwerking, uit de resultatenrekening | EUR |
| `eigen vermogen` | Totaal eigen vermogen op balansdatum (passiefzijde balans) | EUR |

**Voorbeeld-invulling**: winst Rotex Roeselare NV = € 2.500.000; eigen vermogen = € 12.000.000

```
€ 2.500.000 / € 12.000.000 = 0,2083 = 20,8 %
```

_Resultaat in %_
**Brutorentabiliteit van het eigen vermogen (op cashflow)** (volgt op: cashflow)
```
bruto ROE = cashflow / eigen vermogen
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `cashflow` | Nettoresultaat na belasting + niet-kaskosten (afschrijvingen, waardeverminderingen, voorzieningen) | EUR |
| `eigen vermogen` | Totaal eigen vermogen op balansdatum | EUR |

**Voorbeeld-invulling**: cashflow Rotex = € 4.200.000; eigen vermogen = € 12.000.000

```
€ 4.200.000 / € 12.000.000 = 0,3500 = 35,0 %
```

_Resultaat in %_
*De aandeelhouder wil weten of zijn geld 'aan het werk' is. Vergelijk de oogst (winst of cashflow) met de zaak die hij liet staan (eigen vermogen).*

### 1. Lees winst van het boekjaar uit de resultatenrekening

Neem het bedrag 'Winst (verlies) van het boekjaar' (rubriek na belastingen, vóór resultaatverwerking) uit de resultatenrekening van de onderneming.

**Waarom?** Dit cijfer is wat de aandeelhouder potentieel kan toe-eigenen via dividend of reserve.

**📥 Input**:
- Resultatenrekening → **Winst (verlies) van het boekjaar na belastingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad analyse → **Teller netto-ROE** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de resultatenrekening van Rotex Roeselare NV.
2. Zoek de regel 'Winst van het boekjaar' onderaan, na belastingen op het resultaat.
3. Noteer het bedrag (bv. € 2.500.000).


**Grondslag**: CBN-2011/14 §rentabiliteit eigen vermogen

### 2. Lees eigen vermogen uit de balans

Neem de totaalrubriek 'Eigen vermogen' uit de passiefzijde van de balans op afsluitingsdatum.

**Waarom?** Dat is het bedrag waaraan we het resultaat zullen relateren — wat de aandeelhouders aan kapitaal en reserves in de zaak hebben staan.

**📥 Input**:
- Balans (passief) → **Eigen vermogen totaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad analyse → **Noemer ROE** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de balans van Rotex Roeselare NV.
2. Tel kapitaal + uitgiftepremies + herwaarderingsmeerwaarden + reserves + overgedragen resultaat (eventueel + kapitaalsubsidies).
3. Noteer het totaal (bv. € 12.000.000).


**Grondslag**: KB WVV (balansschema)

### 3. Bereken nettorentabiliteit

Deel de winst door het eigen vermogen. Druk uit als percentage.

**Waarom?** Het percentage maakt vergelijking mogelijk met sector, historiek en alternatieve beleggingen.

**📥 Input**:
- Werkblad → **Winst boekjaar** _(boekhoudkundig-bedrag)_
- Werkblad → **Eigen vermogen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Netto-ROE** _(percentage)_

**🛠️ Hoe**:

1. Bereken: € 2.500.000 / € 12.000.000 = 0,208.
2. Vermenigvuldig met 100 = 20,8 %.
3. Plaats in evolutie- en sectorvergelijking (bv. ROE Rotex vorig jaar 18 %; sector-mediaan 12 %).


> [!example]- Voorbeeld: Rotex Roeselare NV — grote NV met volledig schema
> Rotex Roeselare NV — grote NV met volledig schema. Resultatenrekening en balans boekjaar 20X1.
>
> 1. **Inputgegevens uit jaarrekening** 📊
>
>    | Rotex Roeselare NV — uittreksel        | Bedrag (€) |
>    |----------------------------------------|-----------:|
>    | Winst van het boekjaar (na belastingen)|  2.500.000 |
>    | Eigen vermogen (passief totaal)        | 12.000.000 |
>
> 2. **Berekening netto-ROE** 🧮
>
>    Netto-ROE = € 2.500.000 / € 12.000.000 = 0,2083 → **20,8 %**
>

**Grondslag**: CBN-2011/14 §rentabiliteit eigen vermogen

### 4. Bereken bruto-ROE met cashflow

Tel bij de winst de niet-kaskosten op (afschrijvingen, waardeverminderingen, voorzieningen). Deel die cashflow door het eigen vermogen.

**Waarom?** Bruto-ROE filtert boekhoudkundige niet-kaselementen weg en toont het kasgenererend vermogen.

**📥 Input**:
- Resultatenrekening → **Afschrijvingen, waardeverminderingen, voorzieningen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Bruto-ROE** _(percentage)_

**🛠️ Hoe**:

1. Zoek de niet-kaskosten van Rotex (bv. afschrijvingen € 1.500.000, waardeverminderingen € 200.000).
2. Cashflow = winst € 2.500.000 + niet-kaskosten € 1.700.000 = € 4.200.000.
3. Bruto-ROE = € 4.200.000 / € 12.000.000 = 35,0 %.


**Grondslag**: CBN-2011/14 §rentabiliteit eigen vermogen (cashflow-variant)

**Voorbeeld**: Rotex Roeselare NV: winst € 2.500.000; afschrijvingen € 1.500.000; waardeverminderingen € 200.000; eigen vermogen € 12.000.000.

```
Netto-ROE = € 2.500.000 / € 12.000.000 = 20,8 %. Cashflow = € 2.500.000 + € 1.700.000 = € 4.200.000. Bruto-ROE = € 4.200.000 / € 12.000.000 = 35,0 %.
```

Resultaat: Een netto-ROE van 20,8 % is sterk; verschil met bruto-ROE (35 %) signaleert dat de niet-kaskosten een aanzienlijk deel van de bruto-cashgeneratie afromen — relevant voor financieringsbeslissingen.

## In de praktijk

<h3 id="1.3.II.C">Vergelijken in tijd en sector</h3>

> [!tip]- Vergelijken in tijd en sector
> Eén ROE-cijfer zegt weinig. Vergelijk met de ROE van vorige boekjaren (evolutie) en met de mediaan-ROE in de sector. Een ROE van 8 % kan goed zijn in een kapitaalintensieve sector en zwak in dienstverlening. ⚖️

> [!tip]- Herkennen op het examen
> Examenvalkuil: ROE-conclusie geven zonder context-referentie.

<h3 id="1.3.II.C">Effect van een herwaardering</h3>

> [!tip]- Effect van een herwaardering
> Een herwaardering doet het eigen vermogen stijgen, waardoor de ROE daalt — ook al is de winst dezelfde. CBN-2011/14 wijst op dit effect: een herwaarderingsmeerwaarde mag alleen geboekt worden als de rentabiliteit aanvaardbaar blijft. ⚖️

> [!tip]- Herkennen op het examen
> Bij een onderneming die net herwaardeerde — neem dat mee in je interpretatie.


> [!info]- Niet verwarren met [[rentabiliteit-totaal-activa-roa]]
> ROE meet rendement tegenover het eigen vermogen (perspectief aandeelhouder). ROA meet rendement tegenover het volledige balanstotaal (economisch perspectief, los van financieringswijze). Het verschil tussen beide signaleert het leverage-effect: hoge ROE bij lage ROA betekent dat schulden de winst voor de aandeelhouder versterken.
>
> _Trigger_: Examenvraag 'welke ratio voor welke vraag?': aandeelhoudersrendement = ROE; economische winstgevendheid van de bedrijfsmiddelen = ROA.


## Valkuilen

> [!warning]- Een hoog ROE kan komen door een laag eigen vermogen (hefboomeffect met veel schuld), niet door sterke winstgevendheid
> ⚠️ Een hoog ROE kan komen door een laag eigen vermogen (hefboomeffect met veel schuld), niet door sterke winstgevendheid. Combineer ROE altijd met solvabiliteit en ROA voor een eerlijk beeld. 🔗
>
> _Bron: Financial analysis_


> [!warning]- Neem het eigen vermogen op afsluitingsdatum — niet op aanvangsdatum
> ⚠️ Neem het eigen vermogen op afsluitingsdatum — niet op aanvangsdatum. Sommige varianten werken met gemiddeld eigen vermogen ((begin + einde) / 2); vermeld in de toelichting welke variant je gebruikt. 🔗
>
> _Bron: Financial analysis_



## Zie ook

- **Vereist kennis van**: [[cashflow-analyse]]
- **Wordt voorondersteld in** (2): [[cashflow-analyse]] · [[financiering-met-eigen-vermogen]]
## Bronnen

[^1]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteit-van-het-eigen-vermogen-voorbeeldmethoden`
[^2]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteitsvoorwaarden_part1`
[^3]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteitsvoorwaarden_part2`
[^4]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteit-van-het-totaal-van-de-activa-voorbeeldmethoden`
