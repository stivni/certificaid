---
title: Cash ratio (liquiditeit in strenge zin)
tags:
- concept
- cluster
- po-1-3
linked_anchors:
- 1.3.II.C
- 1.3.taak.1
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/cash-ratio.json
gegenereerd_op: '2026-05-18'
---
# Cash ratio (liquiditeit in strenge zin) 🤖

Cash ratio = (geldbeleggingen + liquide middelen) / schulden op ten hoogste een jaar. Het is de strengste liquiditeitstoets: ze meet hoeveel van de korte schulden onmiddellijk kunnen worden voldaan zonder beroep te doen op vorderingen of voorraden. In voorraadintensieve sectoren is dit de meest waardevolle van de drie liquiditeitsratio's omdat ze de illusie van liquiditeit door grote voorraden uitsluit.

> [!summary] Korte inhoud
> De cash ratio is de verhouding tussen de meest liquide vlottende activa (geldbeleggingen + liquide middelen) en de schulden op ten hoogste een jaar.

> [!info] Behoort tot: [[liquiditeitsratio]]

De cash ratio is de verhouding tussen de meest liquide vlottende activa (geldbeleggingen + liquide middelen) en de schulden op ten hoogste een jaar. Ze toont in welke mate de onderneming haar korte schulden onmiddellijk en zonder operationele tussenstappen zou kunnen voldoen.

_Bron: Algemene financial-analysis-doctrine_


## Bouwstenen

### Enkel cash en cash-equivalenten 🤖

Tel rubriek VIII (geldbeleggingen) + rubriek IX (liquide middelen) op en deel door de schulden op ten hoogste een jaar. Voorraden en handelsvorderingen worden — anders dan bij quick ratio en current ratio — niet meegerekend.

**Waarom?** Geldbeleggingen en liquide middelen zijn binnen de dag beschikbaar. Vorderingen vergen nog inning; voorraad vergt nog verkoop. Bij acute crisis valt enkel echte cash terug.



Rotex Roeselare NV: geldbeleggingen € 500.000 + liquide middelen € 800.000 = € 1.300.000. Korte schulden € 4.000.000. Cash ratio = € 1.300.000 / € 4.000.000 = 0,325.

_Grondslag: Vakdoctrine financial analysis_

### Strengste van de drie 🤖

Current ratio > quick ratio > cash ratio. Hoe lager je in deze hiërarchie zakt, hoe strenger de toets en hoe minder vlottende-activa-categorieën meetellen.

**Waarom?** Een lage cash ratio is niet meteen alarmerend (bedrijven houden bewust weinig kasreserve), maar samen met andere zwakke signalen (lage solvabiliteit, dalende quick ratio) wordt ze diagnostisch.




_Grondslag: Vakdoctrine_


## Berekening

### Berekening cash ratio

**Cash ratio** 
```
cash ratio = (geldbeleggingen + liquide middelen) / schulden op ten hoogste een jaar
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `geldbeleggingen` | Balansrubriek VIII (geldbeleggingen, kortlopende effecten) | EUR |
| `liquide middelen` | Balansrubriek IX (kas, bank, postcheque) | EUR |
| `schulden op ten hoogste een jaar` | Passiefrubriek IX (financiële, handels, fiscale, sociale en andere schulden ≤ 1 jaar) + overlopende rekeningen passief | EUR |

**Voorbeeld-invulling**: Rotex: geldbeleggingen € 500.000; liquide middelen € 800.000; korte schulden € 4.000.000

```
(€ 500.000 + € 800.000) / € 4.000.000 = € 1.300.000 / € 4.000.000 = 0,325
```

_Resultaat in verhoudingsgetal_
*De onmiddellijk beschikbare middelen tegenover de schulden die binnen het jaar betaald moeten worden. Strenger dan current of quick omdat enkel cash en cash-equivalenten in de teller staan.*

### 1. Lees geldbeleggingen en liquide middelen

Open de balans, neem de bedragen uit rubriek VIII (geldbeleggingen) en rubriek IX (liquide middelen) op activazijde.

**Waarom?** Dit zijn de twee balansrubrieken die binnen de dag in cash beschikbaar zijn.

**📥 Input**:
- Balans (actief) → **Rubrieken VIII en IX** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Totaal cash + equivalenten** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Voor Rotex: rubriek VIII = € 500.000, rubriek IX = € 800.000.
2. Som = € 1.300.000.


**Grondslag**: KB WVV balansschema

### 2. Lees schulden op ten hoogste een jaar

Neem passiefrubriek IX (financiële, handels, fiscale, sociale, andere schulden ≤ 1 jaar) + overlopende rekeningen passief.

**Waarom?** Dit zijn de verplichtingen die binnen 12 maanden moeten worden voldaan.

**📥 Input**:
- Balans (passief) → **Rubriek IX + overlopende rekeningen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad → **Totaal korte schulden** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Voor Rotex: rubriek IX totaal = € 3.800.000 + overlopende rekeningen passief = € 200.000.
2. Som = € 4.000.000.


**Grondslag**: KB WVV balansschema

### 3. Bereken de verhouding

Deel cash + equivalenten door de korte schulden.

**Waarom?** Geeft de strengste maatstaf: kan de onderneming morgen zonder hulp van vorderingen of voorraden alle korte schulden voldoen?

**📥 Input**:
- Werkblad → **Teller en noemer** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Ratio-tabel → **Cash ratio** _(verhoudingsgetal)_

**🛠️ Hoe**:

1. € 1.300.000 / € 4.000.000 = 0,325.
2. Plaats in evolutie + samen met current en quick: trio toont volledig liquiditeitsbeeld.


> [!example]- Voorbeeld: Rotex Roeselare NV — boekjaar 20X1
> Rotex Roeselare NV — boekjaar 20X1.
>
> 1. **Inputgegevens balans** 📊
>
>    | Rotex Roeselare NV — extractie balans      | Bedrag (€) |
>    |--------------------------------------------|-----------:|
>    | Geldbeleggingen (VIII)                     |    500.000 |
>    | Liquide middelen (IX)                      |    800.000 |
>    | **Totaal cash + equivalenten**             | **1.300.000** |
>    | Schulden ≤ 1 jaar (incl. overlopende pass) |  4.000.000 |
>
> 2. **Berekening cash ratio** 🧮
>
>    Cash ratio = € 1.300.000 / € 4.000.000 = **0,325**
>

**Grondslag**: Vakdoctrine financial analysis

**Voorbeeld**: Rotex Roeselare NV: geldbeleggingen € 500.000 + liquide middelen € 800.000 = € 1.300.000; korte schulden € 4.000.000.

```
Cash ratio = € 1.300.000 / € 4.000.000 = 0,325.
```

Resultaat: Een cash ratio van 0,325 betekent dat Rotex met onmiddellijk beschikbare cash slechts 32,5 % van haar korte schulden zou kunnen voldoen. Voor een productie-onderneming met current ratio 2,0 en quick ratio 1,375 is dit niet alarmerend — voorraden en vorderingen vullen de rest aan. Bij een dienstverlener zonder voorraden zou diezelfde cash ratio te laag zijn.

## In de praktijk

<h3 id="1.3.II.C">Strengste liquiditeitstoets</h3>

> [!tip]- Strengste liquiditeitstoets
> Bij examenvragen 'welke ratio test de meest acute betaalkracht?' of 'welke ratio sluit voorraden én vorderingen uit?' is het antwoord altijd cash ratio. Ze meet de pure kassituatie zonder operationele tussenschakels. 🤖

<h3 id="1.3.II.C">Geen vaste norm</h3>

> [!tip]- Geen vaste norm
> Anders dan current ratio (norm rond 1-2) of quick ratio (norm rond 1) heeft cash ratio geen algemeen aanvaarde minimumwaarde. Bedrijven optimaliseren bewust hun kaspositie: te hoge cash = niet productief belegd; te lage cash = liquiditeitsrisico. Interpretatie gebeurt steeds sectorgebonden en samen met de andere twee ratio's. 🤖


> [!info]- Niet verwarren met [[quick-ratio]]
> Quick ratio neemt naast cash ook handelsvorderingen mee (alles behalve voorraden). Cash ratio sluit ook vorderingen uit en houdt alleen geldbeleggingen + liquide middelen. Cash is strenger.
>
> _Trigger_: Examenvraag 'liquiditeit in enge of strengste zin?': enge = quick (zonder voorraden); strengste = cash (zonder voorraden én vorderingen).

> [!info]- Niet verwarren met [[current-ratio]]
> Current ratio neemt alle vlottende activa (inclusief voorraden + vorderingen). Cash ratio kijkt alleen naar onmiddellijk beschikbare middelen. Het verschil is groot voor voorraadintensieve sectoren.
>
> _Trigger_: Examenvraag 'liquiditeit in ruime versus strengste zin?': ruim = current; strengst = cash.


## Valkuilen

> [!warning]- Een lage cash ratio is niet automatisch alarmerend
> ⚠️ Een lage cash ratio is niet automatisch alarmerend. Bedrijven met sterke handelskrediet-positie en betrouwbare klanten houden bewust weinig cash aan om geen renteverlies te lijden. Bekijk altijd samen met quick ratio, rotatie van vorderingen en bankkredietruimte. 🤖
>
> _Bron: Financial analysis_


> [!warning]- Geldbeleggingen onder rubriek VIII zijn niet altijd echt liquide
> ⚠️ Geldbeleggingen onder rubriek VIII zijn niet altijd echt liquide. Termijndeposito's op meer dan 3 maanden of niet-beursgenoteerde participaties horen er soms in maar zijn niet onmiddellijk te gelde te maken. Controleer de toelichting bij de geldbeleggingen vóór je ze als cash beschouwt. 🤖
>
> _Bron: Financial analysis_



## Bronnen

[^1]: `anchor-1.3.II.C`
