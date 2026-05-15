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
schema_version: '1.2'
gegenereerd_uit: data/concepten/records/minderheidsbelangen.json
gegenereerd_op: '2026-05-15'
---
# Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen) ⚖️

> Het deel van het eigen vermogen en van het resultaat van integraal geconsolideerde dochters dat kan worden toegerekend aan aandelen die worden gehouden door andere personen dan de consoliderende vennootschap of de in de consolidatie opgenomen dochters. Op de geconsolideerde balans verschijnen die als 'Belangen van derden' aan passiefzijde; in de geconsolideerde resultatenrekening als 'Aandeel van derden in het resultaat'. Dit fenomeen ontstaat uitsluitend bij integrale consolidatie van een dochter waar de moeder minder dan 100 % van het kapitaal aanhoudt.
>
> _Bron: KB WVV art. 3:137 (resultaat); art. 3:130 (herberekening)_


## Berekening

### Aandeel van derden — balans en resultatenrekening

**Formule**: `Belangen van derden (balans) = (1 − belang%) × eigen vermogen dochter op afsluitingsdatum;
Aandeel van derden in resultaat = (1 − belang%) × resultaat van het boekjaar van de geconsolideerde dochter`

*De moeder consolideert 100 % van de activa, passiva, opbrengsten en kosten van de dochter; het deel dat economisch aan derden toebehoort wordt afgezonderd zodat de geconsolideerde gegevens transparant tonen welk deel van eigen vermogen en resultaat aan de groep en welk deel aan minderheidsaandeelhouders toekomt.*

**Stappen**:
1. {'volgorde': 1, 'text': 'Bepaal het belangenpercentage van de moeder in de dochter (rechten in kapitaal).'}
2. {'volgorde': 2, 'text': 'Bereken (1 − belang%) — dit is het derden-percentage.'}
3. {'volgorde': 3, 'text': "Vermenigvuldig met het eigen vermogen van de dochter op afsluitingsdatum → 'Belangen van derden' op de balans (passiefzijde)."}
4. {'volgorde': 4, 'text': "Vermenigvuldig met het resultaat van het boekjaar van de dochter → 'Aandeel van derden in het resultaat' (resultatenrekening)."}
5. {'volgorde': 5, 'text': "Indien actief- en passiefbestanddelen van de dochter werden herberekend (KB WVV art. 3:130, lid 1), wordt het aandeel van derden in die herberekeningen geboekt in de post 'Belangen van derden' aan passiefzijde (KB WVV art. 3:130, lid 4)."}

**Voorbeeld**: M bezit 80 % van D (integrale consolidatie). Eigen vermogen van D op afsluitingsdatum = 500 (incl. resultaat boekjaar 100). Resultaat boekjaar D = 100.

```
Belang% (M in D) = 80 %. Derden-percentage = 20 %.
Belangen van derden (balans, passief) = 20 % × 500 = 100.
Aandeel van derden in het resultaat (resultatenrekening) = 20 % × 100 = 20.
M-deel van het resultaat (na aftrek derden) = 80 % × 100 = 80.
```

Resultaat: In de geconsolideerde balans verschijnen 'Belangen van derden' voor 100; in de geconsolideerde resultatenrekening verschijnt 'Aandeel van derden in het resultaat' voor 20. De resterende 80 wordt toegerekend aan de moedervennootschap (geconsolideerd resultaat van de groep).

## In de praktijk

### Enkel bij integrale consolidatie {id="enkel-bij-integrale-consolidatie"}

Minderheidsbelangen verschijnen enkel bij integrale consolidatie (waarbij 100 % van de dochter wordt opgenomen). Bij evenredige consolidatie wordt het derden-deel gewoon niet opgenomen → geen aparte derden-post nodig. Bij vermogensmutatie wordt enkel het pro-rata aandeel van de moeder geboekt → ook geen derden-post. ⚖️

**Herkenningspunt**: Examen: zie je een post 'Belangen van derden' in een balans? → integrale consolidatie. Geen 'Belangen van derden' → evenredig of vermogensmutatie.

### Negatief aandeel van derden {id="negatief-aandeel-van-derden"}

Indien een dochter een verlies maakt en de moeder integraal consolideert, kan het derden-aandeel ook negatief zijn (wat het derden-belang op de balans vermindert). Geen specifieke beperking zoals bij vermogensmutatie (waar boekwaarde niet onder nul gaat); bij integrale consolidatie wordt het volledige resultaat opgenomen, en het derden-deel volgt naar evenredigheid. 🤖


## Vergelijkingsparen

| Verwarrend met | Verschil | Trigger |
|---|---|---|
| [[belangenpercentage]] | Belangenpercentage = het deel van de moeder. Minderheidsbelangen / derden-aandeel = het complement (1 − belang%). Twee zijden van dezelfde munt. | — |
| [[integrale-consolidatie]] | Minderheidsbelangen zijn een direct gevolg van integrale consolidatie wanneer belang < 100 %. Geen integrale consolidatie → geen post 'Belangen van derden'. | — |
| [[evenredige-consolidatie]] | Evenredige consolidatie neemt alleen het pro-rata deel op en kent dus geen 'Belangen van derden'-post. Integrale neemt 100 % op met een afzonderlijke derden-post. | — |

## Valkuilen

- ⚠️ Het derden-aandeel wordt berekend op het eigen vermogen van de dochter ná herberekening van onder-/overgewaardeerde activa (KB WVV art. 3:130, lid 4). De derden-correctie wordt dus ook toegepast op de stille meer-/minderwaarden die bij eerste consolidatie zijn vastgesteld — niet enkel op het boekhoudkundige EV. ⚖️

## Bronnen

[^1]: `KB-WVV-2019__art_3_108`
[^2]: `KB-WVV-2019__art_3_102`
[^3]: `KB-WVV-2019__art_3_111`
