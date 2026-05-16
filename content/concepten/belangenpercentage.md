---
title: Belangenpercentage
tags:
- concept
- begrip
- po-1-4
linked_anchors:
- 1.4.I.C
- 1.4.I.D
- 1.4.I.E
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: inferred-from-aggregation
node_type: begrip
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/belangenpercentage.json
gegenereerd_op: '2026-05-16'
---
# Belangenpercentage 🤖

> Het economische eigendomsaandeel dat een moedervennootschap (direct en indirect, naar rato vermenigvuldigd langs elke ketenschakel) in een dochter- of geassocieerde onderneming aanhoudt. Het belangenpercentage bepaalt het deel van het eigen vermogen en het resultaat van die andere onderneming dat aan de moeder kan worden toegerekend; het complement (1 − belangenpercentage) is het aandeel van derden in een integrale consolidatie.
>
> _Bron: KB WVV art. 3:137 (toepassing aandeel van derden)_


> [!summary] Korte definitie
> Het economische eigendomsaandeel dat een moedervennootschap (direct en indirect, naar rato vermenigvuldigd langs elke ketenschakel) in een dochter- of geassocieerde onderneming aanhoudt.

> [!info] Behoort tot: [[minderheidsbelangen]]
## Berekening

### Belangenpercentage in een verticale keten

**Belangenpercentage in een verticale keten** 
```
belang% (M in B) = belang% (M in A) × belang% (A in B) × … (vermenigvuldiging over alle schakels)
```

*Een eigendomsbelang vloeit niet onverdund door schakels; elk niveau verdeelt een evenredig stuk eigendom over derden. Anders dan voor controle wordt het belangenpercentage dus wél vermenigvuldigd.*

### . 

**Voorbeeld**: Aurelia Holding NV bezit 80 % van A; A bezit 60 % van B (beide via kapitaal en stemrechten, geen preferente regelingen).

```
belang% (M in B) = 0,80 × 0,60 = 0,48 = 48 %
```

Resultaat: Aurelia Holding NV heeft een economisch belang van 48 % in B. Het aandeel van derden in B = 100 % − 48 % = 52 %. Indien B een resultaat van 100 heeft, bedraagt het aandeel van derden in het resultaat 52.

## In de praktijk

### Berekening in ketenstructuur {id="berekening-in-ketenstructuur"}

Belangenpercentages vermenigvuldigen zich langs een keten. In M → 80 % A → 60 % B bedraagt het belang van M in B = 0,80 × 0,60 = 48 %. 🤖

**Herkenningspunt**: Bij examen-tabellen 'M x % van A, A y % van B': het belangenpercentage van M in B = x % × y %.

### Bepaling aandeel van derden bij integrale consolidatie {id="bepaling-aandeel-van-derden-bij-integrale-consolidatie"}

Bij integrale consolidatie wordt 100 % van de activa en passiva van de dochter opgenomen. Het deel dat niet aan de moeder toebehoort (1 − belangenpercentage) wordt afgezonderd als 'belangen van derden' (balans) en 'aandeel van derden in het resultaat' (resultatenrekening). ⚖️


<details>
<summary><strong>Niet verwarren met</strong> (1 vergelijkingen)</summary>

- **vs [[controlepercentage]]** — Belang = kapitaal/winstrecht, wordt vermenigvuldigd over schakels. Controle = stemrechten/zeggenschap, wordt niet vermenigvuldigd zolang elke schakel exclusief gecontroleerd wordt.
  - _Trigger_: Examen: vraag eerst 'wat moet ik berekenen?' — winstaandeel/derden → belang; consolidatieverplichting/methode → controle.

</details>


## Valkuilen

- ⚠️ Belangenpercentage en controlepercentage worden vaak verward. Een opgave die zegt 'M bezit 60 %' kan twee dingen betekenen — 60 % van de stemrechten (controle) of 60 % van het kapitaal (belang); bij gewone aandelen vallen die samen, bij preferente niet. 🤖

## Zie ook

- **Vereist kennis van**: [[controle]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
