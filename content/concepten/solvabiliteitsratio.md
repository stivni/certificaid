---
title: Solvabiliteitsratio
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
- 1.9.V.C
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/solvabiliteitsratio.json
gegenereerd_op: '2026-05-18'
---
# Solvabiliteitsratio 🤖

Meten welk aandeel van de balans gefinancierd is met eigen vermogen — een maatstaf voor structurele schokbestendigheid op middellange en lange termijn. Een vennootschap met hoge solvabiliteit kan tegenslag (verliezen, waardeverminderingen) opvangen zonder direct in betalingsproblemen te komen.

> [!info] Behoort tot: [[doelstellingen-financiele-analyse]]


## Bouwstenen

### Eigen vermogen tegenover balanstotaal 🤖

De klassieke solvabiliteitsratio = eigen vermogen / totaal passiva (balanstotaal). Uitgedrukt als percentage.

**Waarom?** Hoe groter het eigen vermogen tegenover het geheel, hoe meer ruimte voor verliezen zonder dat schuldeisers worden geraakt.



Rotex Roeselare NV: eigen vermogen € 12.000.000; balanstotaal € 30.000.000. Solvabiliteitsratio = € 12.000.000 / € 30.000.000 = 40 %.

_Grondslag: Vakdoctrine_


## Berekening

### Berekening solvabiliteitsratio (klassieke vorm)

**Solvabiliteitsratio (klassieke vorm)** 
```
solvabiliteitsratio = eigen vermogen / balanstotaal
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `eigen vermogen` | Totaal eigen vermogen op afsluitingsdatum (passief rubrieken I-VI) | EUR |
| `balanstotaal` | Som van alle activa (= som van alle passiva) | EUR |

**Voorbeeld-invulling**: Rotex: eigen vermogen € 12.000.000; balanstotaal € 30.000.000

```
€ 12.000.000 / € 30.000.000 = 0,40 = 40 %
```

_Resultaat in %_
*Hoe groter het deel van het balanstotaal dat met eigen middelen is gefinancierd, hoe minder afhankelijk de onderneming is van schuldeisers. Een dunne kapitaalbasis betekent dat verliezen snel het eigen vermogen wegvreten, met technisch faillissement als gevolg.*

### 1. Lees eigen vermogen totaal uit balans

Som kapitaal + uitgiftepremies + herwaarderingsmeerwaarden + reserves + overgedragen resultaat (+ kapitaalsubsidies).

**Waarom?** Het eigen vermogen is wat de aandeelhouders structureel in de vennootschap hebben staan.

**📥 Input**:
- Balans (passief) → **Eigen vermogen rubrieken** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Teller** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open balans Rotex.
2. Tel rubrieken I tot VI van eigen vermogen.
3. Noteer € 12.000.000.


**Grondslag**: KB WVV balansschema

### 2. Lees balanstotaal

Neem het totaal van activa (gelijk aan totaal passiva).

**📥 Input**:
- Balans → **Balanstotaal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Noemer** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Balanstotaal Rotex = € 30.000.000.


**Grondslag**: KB WVV balansschema

### 3. Bereken de verhouding

Deel eigen vermogen door balanstotaal; druk uit als percentage.

**Waarom?** Het percentage geeft direct interpreteerbaar beeld (>30 % = sterk, <15 % = zwak — vuistregels).

**🛠️ Hoe**:

1. € 12.000.000 / € 30.000.000 = 0,40 = 40 %.
2. Plaats in vergelijking: vorig jaar 35 %; sectormediaan 32 %. Conclusie: solvabiliteit sterk en verbeterend.


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Inputgegevens balans** 📊
>
>    | Rotex Roeselare NV — balans-extract | Bedrag (€) |
>    |-------------------------------------|-----------:|
>    | Kapitaal                            |  5.000.000 |
>    | Reserves                            |  4.000.000 |
>    | Overgedragen resultaat              |  3.000.000 |
>    | **Eigen vermogen totaal**           | **12.000.000** |
>    | **Balanstotaal**                    | **30.000.000** |
>
> 2. **Berekening** 🧮
>
>    Solvabiliteitsratio = € 12.000.000 / € 30.000.000 = 0,40 = **40 %**
>

**Grondslag**: Vakdoctrine

**Voorbeeld**: Rotex Roeselare NV: eigen vermogen € 12.000.000; balanstotaal € 30.000.000.

```
€ 12.000.000 / € 30.000.000 = 40 %.
```

Resultaat: Solvabiliteit 40 % geldt als sterk: 4 op 10 euro op de balans is met eigen middelen gefinancierd. Onder 20 % is meestal een waarschuwing — minder dan een vijfde van de balans is dan eigen middelen.

## In de praktijk

<h3 id="1.3.II.C">Sectorgevoelig</h3>

> [!tip]- Sectorgevoelig
> Vuistregels (>30 % sterk; <15 % zwak) variëren sterk per sector. Banken en verzekeraars hebben eigen wettelijke kapitaalvereisten; productiebedrijven dragen vaak meer eigen vermogen dan dienstverleners. 🤖

<h3 id="1.3.II.C">Herwaardering doet ratio stijgen</h3>

> [!tip]- Herwaardering doet ratio stijgen
> Een herwaarderingsmeerwaarde verhoogt zowel eigen vermogen als balanstotaal — maar het eigen vermogen relatief meer (de meerwaarde gaat 100 % naar EV terwijl het balanstotaal slechts gedeeltelijk stijgt door de meerwaarde). Resultaat: ratio stijgt cijfermatig zonder dat er nieuwe cash binnenkwam. CBN-2011/14 wijst op dit boekhoudkundig effect bij beoordeling. ⚖️


> [!info]- Niet verwarren met [[liquiditeitsratio]]
> Solvabiliteit = structurele kapitaalsamenstelling (lange termijn). Liquiditeit = betalingscapaciteit binnen het jaar (korte termijn). Een bedrijf kan tijdelijk illiquide zijn maar solvabel; omgekeerd kan een liquide bedrijf structureel zwak gefinancierd zijn.
>
> _Trigger_: Examenvraag 'structureel vs operationeel risico': structureel = solvabiliteit; KT betalingsrisico = liquiditeit.

> [!info]- Niet verwarren met [[debt-equity-ratio]]
> Solvabiliteitsratio = EV / balanstotaal. Debt-equity-ratio = vreemd vermogen / eigen vermogen. Beide drukken de financieringsstructuur uit; debt-equity geeft het hefboomeffect rechtstreeks weer.
>
> _Trigger_: Solvabiliteitsratio bij algemene structuuranalyse; debt-equity-ratio bij specifieke hefboom- of risicobeoordeling (bankcovenants).


## Valkuilen

> [!warning]- Bij ondernemingen met overgedragen verliezen of negatieve reserves daalt het eigen vermogen, soms onder nul
> ⚠️ Bij ondernemingen met overgedragen verliezen of negatieve reserves daalt het eigen vermogen, soms onder nul. Solvabiliteitsratio kan dan negatief worden — duidt op een technisch faillissementsrisico (alarmbel-procedure WVV). 🤖
>
> _Bron: Financial analysis_



## Bronnen

[^1]: `anchor-1.3.II.C`
[^2]: `CBN-2011-14-herwaarderingsmeerwaarden__sec_rentabiliteitsvoorwaarden_part2`
