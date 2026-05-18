---
title: Quick ratio (liquiditeit in enge zin, zuurtegraad)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.II.C
- 1.3.taak.1
- 1.9.V.D
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/quick-ratio.json
gegenereerd_op: '2026-05-18'
---
# Quick ratio (liquiditeit in enge zin, zuurtegraad) 🤖

Strengere liquiditeitstoets: kan de vennootschap haar korte schulden betalen zónder dat ze voorraden moet verkopen? Voorraden zijn vaak niet snel cash te maken, vooral bij specifieke goederen of dalende vraag. Ook bekend als 'acid test' of 'zuurtegraad'.

> [!info] Behoort tot: [[liquiditeitsratio]]


## Bouwstenen

### Vlottende activa zonder voorraden 🤖

Schrap de voorraden uit de teller van de current ratio. Hou over: vorderingen, geldbeleggingen, liquide middelen. Deel door schulden op ten hoogste een jaar.

**Waarom?** Voorraden hebben een lange omloopcyclus (productie + verkoop + inning). In een liquiditeitscrisis zijn ze moeilijk snel te gelde te maken; zonder voorraden meet je de 'echte' kortetermijnsolventie.



Rotex Roeselare NV: vlottende activa € 8.000.000 minus voorraden € 2.500.000 = € 5.500.000; korte schulden € 4.000.000. Quick ratio = € 5.500.000 / € 4.000.000 = 1,375.

_Grondslag: Vakdoctrine financial analysis_


## Berekening

### Berekening quick ratio

**Quick ratio** 
```
quick ratio = (vlottende activa − voorraden) / schulden op ten hoogste een jaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vlottende activa` | Som vorderingen + geldbeleggingen + liquide middelen + overlopende rekeningen actief | EUR |
| `voorraden` | Voorraden en bestellingen in uitvoering | EUR |
| `korte schulden` | Schulden op ten hoogste een jaar + overlopende rekeningen passief | EUR |

**Voorbeeld-invulling**: Rotex: vlottende activa € 8.000.000; voorraden € 2.500.000; korte schulden € 4.000.000

```
(€ 8.000.000 − € 2.500.000) / € 4.000.000 = € 5.500.000 / € 4.000.000 = 1,375
```

_Resultaat in verhoudingsgetal_
*De voorraad is potentieel waarde maar geen onmiddellijke liquiditeit. Door ze uit te sluiten test je hoe snel je echt kan reageren in geval van een acuut betalingsprobleem.*

### 1. Bereken vlottende activa zonder voorraden

Trek de voorraden af van de totale vlottende activa.

**Waarom?** De voorraden zijn de minst liquide vlottende activa. Door ze uit te sluiten focus je op snel-cashbare componenten.

**📥 Input**:
- Balans → **Vlottende activa totaal** _(boekhoudkundig-bedrag)_
- Balans → **Voorraden + bestellingen in uitvoering** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Snel-vlottende activa** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Rotex: vlottende activa € 8.000.000 − voorraden € 2.500.000 = € 5.500.000.


**Grondslag**: Vakdoctrine

### 2. Deel door schulden op ten hoogste een jaar

Zelfde noemer als bij current ratio: schulden ≤ 1 jaar + overlopende rekeningen passief.

**Waarom?** Verhouding tussen direct beschikbare middelen en korte verplichtingen.

**📥 Input**:
- Balans → **Schulden op ten hoogste een jaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Quick ratio** _(verhoudingsgetal)_

**🛠️ Hoe**:

1. Korte schulden Rotex = € 4.000.000.
2. Quick ratio = € 5.500.000 / € 4.000.000 = 1,375.
3. Plaats in vergelijking: vorig jaar 1,2; sectormediaan 1,0. Conclusie: ook in enge zin sterk.


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Componenten** 📊
>
>    | Rotex Roeselare NV — extractie balans   | Bedrag (€) |
>    |-----------------------------------------|-----------:|
>    | Vlottende activa (totaal)               |  8.000.000 |
>    | − Voorraden                             | −2.500.000 |
>    | Snel-vlottende activa                   |  5.500.000 |
>    | Schulden ≤ 1 jaar                       |  4.000.000 |
>
> 2. **Berekening** 🧮
>
>    Quick ratio = € 5.500.000 / € 4.000.000 = **1,375**
>

**Grondslag**: Vakdoctrine

**Voorbeeld**: Rotex Roeselare NV: vlottende activa € 8.000.000 met voorraden € 2.500.000; korte schulden € 4.000.000.

```
Snel-vlottende activa = € 8.000.000 − € 2.500.000 = € 5.500.000. Quick ratio = € 5.500.000 / € 4.000.000 = 1,375.
```

Resultaat: Quick ratio van 1,375 = de korte schulden zijn 1,375 keer gedekt door direct cash-baar actief. Boven 1 is comfortabel; onder 1 = signaal van liquiditeitsrisico bij snelle marktverstoring.

## In de praktijk

<h3 id="1.3.II.C">Sectorgevoeligheid</h3>

> [!tip]- Sectorgevoeligheid
> In voorraad-intensieve sectoren (productie, handel) wijkt de quick ratio sterk af van de current ratio. In dienstensectoren liggen beide cijfers dicht bij elkaar omdat voorraad gering of nul is. 🤖


> [!info]- Niet verwarren met [[current-ratio]]
> Quick = current − voorraden in teller. Quick is strenger; toont kortetermijnsolventie zonder afhankelijkheid van voorraadverkoop.
>
> _Trigger_: Voorraad-intensiteit: in productie/handel altijd allebei berekenen om de spreiding te zien.


## Valkuilen

> [!warning]- Niet elke vordering ≤ 1 jaar is in de praktijk snel cash
> ⚠️ Niet elke vordering ≤ 1 jaar is in de praktijk snel cash. Twijfelachtige debiteuren (waarvan waardeverminderingen werden geboekt) zijn al gecorrigeerd, maar trage betalers blijven aan boord. Combineer quick ratio met de rotatie van handelsvorderingen. 🤖
>
> _Bron: Financial analysis_



## Bronnen

[^1]: `anchor-1.3.II.C`
