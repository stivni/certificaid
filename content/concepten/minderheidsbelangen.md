---
title: Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen)
tags:
- concept
- fenomeen
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.I.F
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: fenomeen
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/minderheidsbelangen.json
gegenereerd_op: '2026-05-16'
---
# Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen) ⚖️

> Het deel van het eigen vermogen en van het resultaat van een integraal geconsolideerde dochter dat toebehoort aan andere aandeelhouders dan de moeder of de andere dochters in de consolidatiekring. Op de geconsolideerde balans verschijnt dat als 'Belangen van derden' aan passiefzijde; in de geconsolideerde resultatenrekening als 'Aandeel van derden in het resultaat'. Dit fenomeen ontstaat enkel bij integrale consolidatie van een dochter waarvan de moeder minder dan 100 % bezit.
>
> _Bron: KB WVV art. 3:137 (resultaat); art. 3:130 (herberekening)_


> [!summary] Korte definitie
> Het deel van het eigen vermogen en van het resultaat van een integraal geconsolideerde dochter dat toebehoort aan andere aandeelhouders dan de moeder of de andere dochters in de consolidatiekring.

> [!info] Behoort tot: [[integrale-consolidatie]]
## Berekening

### Aandeel van derden — balans en resultatenrekening

**Belangen van derden (balans, passiefzijde)** 
```
belangen van derden = (1 − belangenpercentage moeder) × eigen vermogen dochter op afsluitingsdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter (zie [[belangenpercentage]]) | % |
| `eigen vermogen dochter op afsluitingsdatum` | Kapitaal + reserves + overgedragen resultaat + resultaat boekjaar van de dochter, einde boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; EV Brugse op afsluitingsdatum = 500

```
(1 − 80 %) × 500 = 20 % × 500 = 100
```

_Resultaat in EUR_
**Aandeel van derden in het resultaat (resultatenrekening)** 
```
aandeel derden in resultaat = (1 − belangenpercentage moeder) × resultaat dochter boekjaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal dochter | % |
| `resultaat dochter boekjaar` | Winst of verlies van de dochter in dit boekjaar | EUR |

**Voorbeeld-invulling**: belangenpercentage Aurelia = 80 %; resultaat Brugse boekjaar = 100

```
(1 − 80 %) × 100 = 20 % × 100 = 20
```

_Resultaat in EUR_
*Bij integrale consolidatie wordt 100 % van de cijfers van de dochter samengevoegd, ook al houdt de moeder slechts (bv.) 80 %. Het deel dat economisch aan minderheidsaandeelhouders toebehoort, wordt apart gepresenteerd zodat de geconsolideerde jaarrekening transparant toont welk deel aan de groep toekomt en welk deel aan derden.*

### . 

**Voorbeeld**: Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV (integrale consolidatie). Eigen vermogen van Brugse op afsluitingsdatum = 500 (incl. resultaat boekjaar 100). Resultaat boekjaar Brugse = 100.

```
Belang% (Aurelia in Brugse) = 80 %. Derden-percentage = 20 %.
Belangen van derden (balans, passief) = 20 % × 500 = 100.
Aandeel van derden in het resultaat (resultatenrekening) = 20 % × 100 = 20.
Deel van het resultaat voor Aurelia (na aftrek derden) = 80 % × 100 = 80.
```

Resultaat: In de geconsolideerde balans: 'Belangen van derden' = 100 (passiefzijde). In de geconsolideerde resultatenrekening: 'Aandeel van derden in het resultaat' = 20. De resterende 80 zit in het geconsolideerd resultaat van de groep dat aan Aurelia toekomt.

## In de praktijk

### Enkel bij integrale consolidatie {id="enkel-bij-integrale-consolidatie"}

Minderheidsbelangen verschijnen alleen bij integrale consolidatie (waarbij 100 % van de dochter wordt opgenomen). Bij evenredige consolidatie wordt het derden-deel gewoon niet opgenomen → geen aparte derden-post nodig. Bij vermogensmutatie zit alleen het pro-rata aandeel van de moeder in de balans → ook geen derden-post. ⚖️

**Herkenningspunt**: Examen: zie je een post 'Belangen van derden' op een geconsolideerde balans? → integrale consolidatie. Geen 'Belangen van derden' → evenredige consolidatie of vermogensmutatie.

### Negatief aandeel van derden {id="negatief-aandeel-van-derden"}

Maakt een dochter een verlies en consolideert de moeder integraal, dan kan het derden-aandeel ook negatief uitkomen (waardoor 'Belangen van derden' op de balans afneemt). Anders dan bij vermogensmutatie (waar de boekwaarde niet onder nul mag gaan) wordt bij integrale consolidatie het volledige resultaat opgenomen, en het derden-deel volgt naar evenredigheid — ook in min. 🤖


## Valkuilen

- ⚠️ Het derden-aandeel bereken je op het eigen vermogen van de dochter ná herberekening van onder- of overgewaardeerde bezittingen en schulden (KB WVV art. 3:130, lid 4). De derden-correctie geldt dus ook voor stille meer- of minderwaarden die bij eerste consolidatie zijn vastgesteld — niet enkel voor het boekhoudkundige EV. Voorbeeld: bij Brugse Brouwerij BV werden terreinen 50 opgewaardeerd; dan komt 20 % × 50 = 10 erbij in 'Belangen van derden'. ⚖️

## Zie ook

- **Vereist kennis van**: [[belangenpercentage]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `KB-WVV-2019__art_3_102`
[^3]: `KB-WVV-2019__art_3_111`
