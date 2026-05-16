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

> Het deel van het kapitaal (en dus van het winstrecht) dat een moeder in een dochter of geassocieerde onderneming bezit. Bij een keten van vennootschappen wordt het belangenpercentage van schakel tot schakel vermenigvuldigd. Het belangenpercentage bepaalt welk stuk van het eigen vermogen en het resultaat van die andere onderneming aan de moeder mag worden toegerekend; het complement (1 − belangenpercentage) is het aandeel van derden bij integrale consolidatie.
>
> _Bron: KB WVV art. 3:137 (toepassing aandeel van derden)_


> [!summary] Korte definitie
> Het deel van het kapitaal (en dus van het winstrecht) dat een moeder in een dochter of geassocieerde onderneming bezit.

> [!info] Behoort tot: [[minderheidsbelangen]]
## Berekening

### Belangenpercentage in een verticale keten

**Belangenpercentage in een verticale keten** 
```
belang (moeder in onderste dochter) = belang (moeder in schakel1) × belang (schakel1 in schakel2) × … × belang (schakeln-1 in onderste dochter)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belang (X in Y)` | Direct kapitaalaandeel van X in Y, uitgedrukt als breuk of percentage | % |

**Voorbeeld-invulling**: belang Aurelia in Brugse = 80 %; belang Brugse in Drukkerij Dendermonde = 60 %

```
0,80 × 0,60 = 0,48
```

_Resultaat in %_
**Aandeel van derden** 
```
aandeel van derden = 1 − belangenpercentage moeder
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Effectief belang van de moeder in de dochter (eventueel na ketenvermenigvuldiging) | % |

**Voorbeeld-invulling**: belangenpercentage Aurelia in Brugse = 80 %

```
1 − 80 % = 20 %
```

_Resultaat in %_
*Een eigendomsbelang vloeit niet onverdund door schakels; elke schakel verdeelt een evenredig stuk eigendom over derden. Anders dan voor controle wordt het belangenpercentage dus wél vermenigvuldigd over een keten.*

### . 

**Voorbeeld**: Aurelia Holding NV bezit 80 % van A; A bezit 60 % van B (beide via kapitaal en stemrechten, geen preferente regelingen).

```
belang% (M in B) = 0,80 × 0,60 = 0,48 = 48 %
```

Resultaat: Aurelia Holding NV heeft een economisch belang van 48 % in B. Het aandeel van derden in B = 100 % − 48 % = 52 %. Indien B een resultaat van 100 heeft, bedraagt het aandeel van derden in het resultaat 52.

## In de praktijk

### Berekening in ketenstructuur {id="berekening-in-ketenstructuur"}

Belangenpercentages vermenigvuldigen zich langs een keten. Voorbeeld: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV, en Brugse Brouwerij BV bezit 60 % van Drukkerij Dendermonde BV → belang van Aurelia in Drukkerij Dendermonde = 0,80 × 0,60 = 48 %. 🤖

**Herkenningspunt**: Examen-tabel 'X % van A, A heeft Y % van B' → belangenpercentage van X in B = X % × Y %.

### Bepaling aandeel van derden bij integrale consolidatie {id="bepaling-aandeel-van-derden-bij-integrale-consolidatie"}

Bij integrale consolidatie komt 100 % van de activa en schulden van de dochter in de geconsolideerde balans. Het deel dat niet aan de moeder toebehoort (1 − belangenpercentage) verschijnt apart als 'Belangen van derden' op de balans en als 'Aandeel van derden in het resultaat' op de resultatenrekening. ⚖️


<details>
<summary><strong>Niet verwarren met</strong> (1 vergelijkingen)</summary>

- **vs [[controlepercentage]]** — Belangenpercentage = aandeel in het kapitaal (en winst); wordt over een keten vermenigvuldigd. Controlepercentage = aandeel in de stemrechten (zeggenschap); wordt niet vermenigvuldigd zolang elke schakel exclusief gecontroleerd wordt door de bovenliggende.
  - _Trigger_: Examen: vraag eerst 'wat moet ik berekenen?' — winstaandeel of aandeel van derden → belangenpercentage; consolidatieverplichting of -methode → controlepercentage.

</details>


## Valkuilen

- ⚠️ Belangenpercentage en controlepercentage worden vaak verward. Een opgave die zegt 'Aurelia bezit 60 %' is dubbelzinnig — 60 % van de stemrechten (controle) of 60 % van het kapitaal (belang)? Bij gewone aandelen vallen die samen, bij preferente aandelen of certificaten kunnen ze uit elkaar lopen. 🤖

## Zie ook

- **Vereist kennis van**: [[controle]]
- **Getriggerd door**: [[integrale-consolidatie]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
