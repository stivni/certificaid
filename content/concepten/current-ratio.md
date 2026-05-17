---
title: Current ratio (liquiditeit in ruime zin)
tags:
- concept
- methode
- po-1-3
- po-1-9
linked_anchors:
- 1.3.II.C
- 1.3.taak.1
- 1.9.V.D
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/current-ratio.json
gegenereerd_op: '2026-05-17'
---
# Current ratio (liquiditeit in ruime zin) 🤖

> [!summary] Korte inhoud
> Meten of de vennootschap genoeg vlottende activa heeft tegenover haar schulden op ten hoogste een jaar.

> [!info] Behoort tot: [[liquiditeitsratio]]

Meten of de vennootschap genoeg vlottende activa heeft tegenover haar schulden op ten hoogste een jaar. De current ratio is de breedst gebruikte liquiditeitsratio in ruime zin.

_Bron: Algemene financial-analysis-doctrine_


## Bouwstenen

### Vlottende activa tegenover korte schulden 🤖

Tel alle vlottende activa op (voorraden, handelsvorderingen, geldbeleggingen, liquide middelen) en deel door de schulden op ten hoogste een jaar.

**Waarom?** Als de vennootschap morgen al haar korte schulden moest betalen, kan ze dan voldoende cash genereren uit haar vlottende activa? Een verhouding van meer dan 1 betekent: theoretisch wel.

**Voorbeeld**: Rotex Roeselare NV: vlottende activa € 8.000.000; schulden op ten hoogste een jaar € 4.000.000. Current ratio = € 8.000.000 / € 4.000.000 = 2,0.

_Grondslag: Vakdoctrine financial analysis_


## Berekening

### Berekening current ratio

**Current ratio** 
```
current ratio = vlottende activa / schulden op ten hoogste een jaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vlottende activa` | Voorraden + vorderingen ≤ 1 jaar + geldbeleggingen + liquide middelen + overlopende rekeningen actief | EUR |
| `schulden op ten hoogste een jaar` | Passief-rubriek IX (financiële, handels, fiscale, sociale en andere schulden ≤ 1 jaar) + overlopende rekeningen passief | EUR |

**Voorbeeld-invulling**: Rotex: vlottende activa € 8.000.000; korte schulden € 4.000.000

```
€ 8.000.000 / € 4.000.000 = 2,0
```

_Resultaat in verhoudingsgetal_
*De vlottende activa zijn middelen die binnen het jaar (typisch) cash worden; de korte schulden moeten binnen het jaar betaald worden. Een veilige verhouding geeft buffer voor onverwachte tegenslagen.*

### 1. Tel vlottende activa op

Som de balansposten: voorraden + handelsvorderingen + andere vorderingen op ten hoogste een jaar + geldbeleggingen + liquide middelen + overlopende rekeningen actiefzijde.

**Waarom?** Dit is de buffer waarmee de onderneming haar korte verplichtingen kan dekken.

**📥 Input**:
- Balans (actief) → **Voorraden, vorderingen, geldbeleggingen, liquide middelen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Totaal vlottende activa** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de balans van Rotex Roeselare NV.
2. Tel rubriek VI (voorraden + bestellingen) + VII (vorderingen op ten hoogste een jaar) + VIII (geldbeleggingen) + IX (liquide middelen) + X (overlopende rekeningen).
3. Voor Rotex: € 2.500.000 + € 4.000.000 + € 500.000 + € 800.000 + € 200.000 = € 8.000.000.


**Grondslag**: Vakdoctrine + KB WVV balansschema

### 2. Lees schulden op ten hoogste een jaar

Neem rubriek IX van de passiefzijde 'Schulden op ten hoogste een jaar' (financiële schulden ≤ 1 jaar, handelsschulden, fiscale en sociale schulden, andere) + overlopende rekeningen passiefzijde.

**Waarom?** Dit zijn de verplichtingen die binnen 12 maanden moeten worden voldaan.

**📥 Input**:
- Balans (passief) → **Schulden op ten hoogste een jaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Totaal korte schulden** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open passiefzijde balans Rotex.
2. Lees rubriek IX totaal (€ 3.800.000) + overlopende rekeningen passief (€ 200.000) = € 4.000.000.


**Grondslag**: KB WVV balansschema

### 3. Bereken de verhouding

Deel de vlottende activa door de korte schulden.

**Waarom?** Geeft één getal — boven 1 = positief, onder 1 = signaal van mogelijk liquiditeitsprobleem.

**📥 Input**:
- Werkblad → **Teller en noemer** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Current ratio** _(verhoudingsgetal)_

**🛠️ Hoe**:

1. € 8.000.000 / € 4.000.000 = 2,0.
2. Plaats in vergelijking: vorig jaar 1,7; sectormediaan 1,5. Conclusie: liquiditeit verbeterd, sterker dan sector.


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Inputgegevens balans** 📊
>
>    | Rotex Roeselare NV — extractie balans      | Bedrag (€) |
>    |--------------------------------------------|-----------:|
>    | Voorraden                                  |  2.500.000 |
>    | Handelsvorderingen ≤ 1 jaar                |  4.000.000 |
>    | Geldbeleggingen                            |    500.000 |
>    | Liquide middelen                           |    800.000 |
>    | Overlopende rekeningen (actief)            |    200.000 |
>    | **Totaal vlottende activa**                | **8.000.000** |
>    | Schulden ≤ 1 jaar (incl. overlopende pass) |  4.000.000 |
>
> 2. **Berekening current ratio** 🧮
>
>    Current ratio = € 8.000.000 / € 4.000.000 = **2,0**
>

**Grondslag**: Vakdoctrine financial analysis

**Voorbeeld**: Rotex Roeselare NV: vlottende activa € 8.000.000; schulden op ten hoogste een jaar € 4.000.000.

```
Current ratio = € 8.000.000 / € 4.000.000 = 2,0.
```

Resultaat: Een current ratio van 2,0 wordt traditioneel als comfortabel gezien. Lager dan 1 betekent dat de korte schulden de vlottende activa overschrijden — een waarschuwingssignaal.

## In de praktijk

<h3 id="1.3.II.C">Een waarde van 1 of meer is ondergrens</h3>

> [!tip]- Een waarde van 1 of meer is ondergrens
> Onder 1 = vlottende activa kleiner dan korte schulden = signaal van mogelijk acuut betalingsprobleem. Boven 2 = ruime liquiditeitsbuffer maar kan ook signaleren dat middelen niet productief worden ingezet. 🤖

> [!tip]- Herkennen op het examen
> Examenanalyse: niet alleen 'ratio = 2,0' maar plaats in evolutie + sectorvergelijking + samen met de quick ratio.


> [!info]- Niet verwarren met [[quick-ratio]]
> Current ratio neemt alle vlottende activa, ook voorraden. Quick ratio (zuurtegraad) sluit voorraden uit omdat die niet zo snel cash worden. Bij voorraadintensieve sectoren (groothandel, productie) ligt current ratio veel hoger dan quick ratio.
>
> _Trigger_: Examenvraag 'liquiditeit in ruime / enge zin?': ruim = current; eng = quick.


## Valkuilen

> [!warning]- Een hoge current ratio is niet automatisch goed
> ⚠️ Een hoge current ratio is niet automatisch goed. Bij overdreven voorraden of trage handelsvorderingen is de liquiditeit cijfermatig sterk maar operationeel zwak. Check altijd de quick ratio en de rotatie van voorraden/vorderingen. 🤖
>
> _Bron: Financial analysis_


> [!warning]- Sommige balansen tonen 'Vorderingen op meer dan een jaar' onder vaste activa
> ⚠️ Sommige balansen tonen 'Vorderingen op meer dan een jaar' onder vaste activa. Zorg dat je enkel vorderingen op ten hoogste een jaar in de teller meeneemt, anders overschat je de liquiditeit. 🤖
>
> _Bron: Financial analysis_



## Zie ook

- **Vereist kennis van**: [[werkkapitaal]]

## Bronnen

[^1]: `anchor-1.3.II.C`
