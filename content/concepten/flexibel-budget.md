---
title: Flexibel budget
tags:
- concept
- begrip
- po-1-8
linked_anchors:
- 1.8.VI.B
- 1.8.VI.D
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/flexibel-budget.json
gegenereerd_op: '2026-05-18'
---
# Flexibel budget 🤖

Een flexibel budget herrekent de oorspronkelijke budgetbedragen op basis van het werkelijke productie- of verkoopvolume. Variabele kosten worden aangepast aan werkelijk volume; vaste kosten blijven gelijk. Doel: een eerlijke vergelijking maken tussen budget en werkelijkheid. Bij sterk afwijkend volume verbergt een statisch budget de volume-impact in het totale verschil; een flexibel budget isoleert het volume-effect zodat efficiëntie- en prijsverschillen zichtbaar worden.

> [!summary] Korte inhoud
> Een flexibel budget herrekent het budget op basis van het werkelijke productie- of verkoopvolume.

> [!info] Behoort tot: [[budgetbeheer]]

Een flexibel budget herrekent het budget op basis van het werkelijke productie- of verkoopvolume. Variabele kosten worden aangepast aan werkelijke volume; vaste kosten blijven gelijk. Resultaat: een 'gecorrigeerd budget' dat eerlijker vergeleken kan worden met de realisatie.

_Bron: Management accounting — bron-gap_


## Berekening

### Flexibel-budget-herrekening

**Flexibel-budget-bedrag per kostensoort** 
```
flexibel_budget = vaste_kosten_budget + (variabele_kost_per_eenheid_budget × werkelijke_eenheden)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `vaste_kosten_budget` | Gebudgetteerde vaste kosten van de periode | EUR |
| `variabele_kost_per_eenheid_budget` | Gebudgetteerde variabele kost per stuk | EUR/stuk |
| `werkelijke_eenheden` | Werkelijk geproduceerd of verkocht aantal | stuks |

**Voorbeeld-invulling**: Yperse Werkplaats BV: vaste kosten weverij € 80.000/maand, variabele kost € 13/tapijt budget; werkelijk volume 9.500 tapijten (budget was 10.000)

```
€ 80.000 + (€ 13 × 9.500) = € 80.000 + € 123.500 = € 203.500
```

_Resultaat in EUR_
*Pas variabele kosten aan aan werkelijk volume; laat vaste kosten op de gebudgetteerde waarde staan.*

### 1. Identificeer vaste en variabele componenten in oorspronkelijk budget

Splits het statisch budget per kostensoort in een vast en een variabel deel. Vaste kosten blijven onveranderd; variabele worden aangepast.

**🛠️ Hoe**:

Bouw op de kostentypologie ([[vaste-kosten]], [[variabele-kosten]]) — vaak per kostensoort in het rekeningenstelsel zichtbaar.

**Grondslag**: [[typologie-van-kosten]]

### 2. Bereken variabele kost per eenheid

Deel het variabele deel van het budget door het oorspronkelijke (begrote) volume.

**🛠️ Hoe**:

variabele_kost_per_eenheid = variabel_deel_budget / begroot_volume.

**Grondslag**: Vakdoctrine

### 3. Pas aan naar werkelijk volume

Vermenigvuldig variabele kost per eenheid met het werkelijke volume; tel vaste kosten erbij op.

**🛠️ Hoe**:

Levert het 'flexibele' budgetbedrag dat eerlijk vergelijkbaar is met de werkelijke kost bij dat volume.

**Grondslag**: Vakdoctrine

### 4. Splits totaalverschil in volume-, efficiëntie- en prijsverschil

Totaal verschil = statisch budget − werkelijk. Volume-verschil = statisch budget − flexibel budget. Efficiëntie + prijs = flexibel budget − werkelijk.

**🛠️ Hoe**:

Drie-staps-decompositie geeft inzicht in oorzaken — volume is verkoopsverantwoordelijkheid; efficiëntie en prijs zijn productie/inkoop.

**Grondslag**: [[verschillenboekhouding]]


> [!info]- Niet verwarren met [[statisch-budget]]
> Statisch budget = oorspronkelijk plan, niet aangepast aan werkelijk volume. Flexibel budget = aangepast aan werkelijk volume. Vergelijking realisatie vs. statisch mengt volume- en efficiëntie-effect; flexibel scheidt beide.
>
> _Trigger_: Examen-vraag: 'is dit verschil te wijten aan andere productie of aan inefficiëntie?' → flexibel budget is nodig om te scheiden.


## Zie ook

- **Vereist kennis van**: [[verschillenboekhouding]]

## Voorbeelden

Yperse Werkplaats BV start met statisch budget Confectie: 7.500 tapijten, € 950.000 (€ 800.000 vast + € 150.000 variabel = € 20/stuk variabel). Realisatie: 9.000 tapijten, € 1.025.000. Flexibel budget bij 9.000 stuks = € 800.000 vast + 9.000 × € 20 = € 980.000. Werkelijk vs. flexibel: € 1.025.000 − € 980.000 = € 45.000 ongunstig. Werkelijk vs. statisch: € 1.025.000 − € 950.000 = € 75.000 ongunstig — waarvan € 30.000 'volume-effect' (logisch, want meer geproduceerd) en € 45.000 'echt' ongunstig.

