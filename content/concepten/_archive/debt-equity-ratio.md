---
title: Debt-equity ratio (schuldgraad)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.II.C
- 1.3.taak.1
- 1.9.V.C
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/debt-equity-ratio.json
gegenereerd_op: '2026-05-21'
---
# Debt-equity ratio (schuldgraad) 🔗

Direct meten hoe groot de vreemde-vermogen-financiering is tegenover het eigen vermogen. Toont de hefboom: 1,5 betekent dat er € 1,50 vreemd vermogen tegenover elke € 1 eigen vermogen staat.

> [!info] Behoort tot: [[doelstellingen-financiele-analyse]]



## Bouwstenen

### Schulden totaal tegenover eigen vermogen 🤖

Tel alle schulden samen (voorzieningen + uitgestelde belastingen + schulden > 1 jaar + schulden ≤ 1 jaar + overlopende rekeningen passief) en deel door eigen vermogen.

**Waarom?** Schuldgraad maakt de hefboom rechtstreeks zichtbaar: bij stijgend resultaat versterkt schuld het ROE; bij dalend resultaat versterkt schuld ook het verlies voor de aandeelhouder.



Rotex Roeselare NV: schulden totaal € 18.000.000; eigen vermogen € 12.000.000. Debt-equity = € 18.000.000 / € 12.000.000 = 1,5.

_Grondslag: Vakdoctrine financial analysis_


## Berekening

### Berekening debt-equity ratio

**Debt-equity ratio** 
```
debt-equity = totaal vreemd vermogen / totaal eigen vermogen
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vreemd vermogen` | Voorzieningen + uitgestelde belastingen + schulden > 1 jaar + schulden ≤ 1 jaar + overlopende rekeningen passief | EUR |
| `eigen vermogen` | Som kapitaal + reserves + overgedragen resultaat (rubrieken I-VI van passief) | EUR |

**Voorbeeld-invulling**: Rotex: schulden € 18.000.000; eigen vermogen € 12.000.000

```
€ 18.000.000 / € 12.000.000 = 1,5
```

_Resultaat in verhoudingsgetal_
*Het is de directe spiegel van de solvabiliteit. Hoge schuldgraad = grote hefboomwerking = meer risico maar potentieel hogere ROE.*

### 1. Tel alle schulden

Som de schulden op meer dan een jaar + schulden op ten hoogste een jaar + voorzieningen + uitgestelde belastingen + overlopende rekeningen passief.

**Waarom?** Alle schuldcomponenten samen = vreemd vermogen.

**📥 Input**:
- Balans (passief) → **Schuldcomponenten alle rubrieken** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Teller — totaal schulden** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open passiefzijde balans Rotex.
2. Som rubrieken VII (voorzieningen) + VIII (schulden > 1 jaar) + IX (schulden ≤ 1 jaar) + X (overlopende rekeningen).
3. Voor Rotex: € 1.000.000 + € 13.000.000 + € 3.800.000 + € 200.000 = € 18.000.000.


**Grondslag**: KB WVV balansschema

### 2. Deel door eigen vermogen

Neem totaal eigen vermogen en deel de schulden erdoor.

**📥 Input**:
- Balans → **Eigen vermogen totaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Debt-equity ratio** _(verhoudingsgetal)_

**🛠️ Hoe**:

1. Eigen vermogen Rotex = € 12.000.000.
2. Debt-equity = € 18.000.000 / € 12.000.000 = 1,5.
3. Plaats in vergelijking en bankcovenants (typisch < 2,5 voor industriebedrijf).


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Inputgegevens balans** 📊
>
>    | Rotex Roeselare NV — passiefzijde         | Bedrag (€) |
>    |-------------------------------------------|-----------:|
>    | Eigen vermogen totaal                     | 12.000.000 |
>    | Voorzieningen + uitgestelde belastingen   |  1.000.000 |
>    | Schulden > 1 jaar                         | 13.000.000 |
>    | Schulden ≤ 1 jaar                         |  3.800.000 |
>    | Overlopende rekeningen (passief)          |    200.000 |
>    | **Totaal schulden**                       | **18.000.000** |
>
> 2. **Berekening** 🧮
>
>    Debt-equity ratio = € 18.000.000 / € 12.000.000 = **1,5**
>

**Grondslag**: Vakdoctrine

**Voorbeeld**: Rotex Roeselare NV: totaal schulden € 18.000.000; eigen vermogen € 12.000.000.

```
€ 18.000.000 / € 12.000.000 = 1,5.
```

Resultaat: Schuldgraad 1,5 = € 1,50 schuld tegenover € 1 eigen vermogen. Voor een industrieel bedrijf nog comfortabel; voor een dienstverlener al stevig.

## In de praktijk

<h3 id="1.3.I.D">Bankcovenant</h3>

> [!tip]- Bankcovenant
> Banken nemen vaak een maximum-debt-equity op in kredietovereenkomsten. Overschrijding triggert default-clausules. Bij een commerciële analyse altijd de geldende covenants checken vóór conclusies. 🤖


> [!info]- Niet verwarren met [[solvabiliteitsratio]]
> Solvabiliteitsratio = EV / balanstotaal (één deel van de taart). Debt-equity = VV / EV (verhouding twee delen). Wiskundig samenhangend (als solvabiliteit = 40 %, dan EV = 0,4 × totaal en VV = 0,6 × totaal, dus D/E = 0,6/0,4 = 1,5).
>
> _Trigger_: Beide drukken financieringsstructuur uit; context bepaalt welke courant is — bankcovenants gebruiken D/E, ratingagentschappen vaker solvabiliteit.


## Valkuilen

> [!warning]- Voorzieningen tellen mee als vreemd vermogen — soms vergeten studenten ze
> ⚠️ Voorzieningen tellen mee als vreemd vermogen — soms vergeten studenten ze. Ook overlopende rekeningen passief (vooral 'kosten te betalen') zijn schulden. 🔗
>
> _Bron: Financial analysis_


> [!warning]- Soms zie je 'net debt to equity' — die variant trekt liquide middelen en geldbeleggingen af van het vreemd vermogen
> ⚠️ Soms zie je 'net debt to equity' — die variant trekt liquide middelen en geldbeleggingen af van het vreemd vermogen. Niet gelijkstellen aan klassieke debt-equity zonder dat te vermelden. 🔗
>
> _Bron: Financial analysis_



## Zie ook

- **Wordt voorondersteld in** (2): [[financiering-met-derdenkapitaal]] · [[ratio-covenants]]
## Bronnen

[^1]: `anchor-1.3.II.C`
