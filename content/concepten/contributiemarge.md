---
title: Contributiemarge
tags:
- concept
- begrip
- po-1-8
linked_anchors:
- 1.8.III.B
- 1.8.III.D
- 1.8.III.E
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/contributiemarge.json
gegenereerd_op: '2026-05-18'
---
# Contributiemarge 🤖

> [!summary] Korte inhoud
> De contributiemarge is het verschil tussen verkoopprijs en variabele kost per eenheid (eenheidscontributie) of tussen omzet en totale variabele kosten (totale contributiemarge).

> [!info] Behoort tot: [[direct-costing]]

De contributiemarge is het verschil tussen verkoopprijs en variabele kost per eenheid (eenheidscontributie) of tussen omzet en totale variabele kosten (totale contributiemarge). Dit bedrag draagt eerst bij aan het dekken van de vaste kosten en daarna aan de winst.

_Bron: Management accounting — bron-gap_


## Berekening

### Eenheidscontributie en contributiemarge-ratio

**Eenheidscontributie** 
```
eenheidscontributie = verkoopprijs per eenheid − variabele kost per eenheid
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `verkoopprijs per eenheid` | Prijs aan klant per stuk | EUR/stuk |
| `variabele kost per eenheid` | Som van alle variabele kosten per stuk | EUR/stuk |

**Voorbeeld-invulling**: Yperse Werkplaats BV tapijt: verkoopprijs € 60; variabele kost € 13

```
€ 60 − € 13 = € 47
```

_Resultaat in EUR/stuk_
**Totale contributiemarge** (volgt op: eenheidscontributie)
```
totale contributiemarge = omzet − totale variabele kosten
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `omzet` | Verkochte eenheden × verkoopprijs | EUR |
| `totale variabele kosten` | Verkochte eenheden × variabele kost per stuk | EUR |

**Voorbeeld-invulling**: 10.000 stuks × € 60 = € 600.000 omzet; 10.000 × € 13 = € 130.000 variabele kost

```
€ 600.000 − € 130.000 = € 470.000
```

_Resultaat in EUR_
**Contributiemarge-ratio (CM-ratio)** (volgt op: eenheidscontributie)
```
CM-ratio = eenheidscontributie / verkoopprijs
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `eenheidscontributie` | Zie formule eenheidscontributie | EUR/stuk |
| `verkoopprijs` | Verkoopprijs per eenheid | EUR/stuk |

**Voorbeeld-invulling**: Eenheidscontributie € 47; verkoopprijs € 60

```
€ 47 / € 60 = 78,3 %
```

_Resultaat in %_
*Twee parallelle uitdrukkingen: per stuk in EUR (eenheidscontributie) of als percentage van omzet (contributiemarge-ratio).*

### 1. Bereken variabele kost per eenheid

Som van directe materiaalkost, directe arbeidskost (indien variabel), variabele indirecte kosten per eenheid.

**🛠️ Hoe**:

Verzamel materiaalbon (€ wol), uurregistratie × uurtarief, variabele machine-energie per eenheid.

**Grondslag**: [[variabele-kosten]]

### 2. Bereken eenheidscontributie

Verkoopprijs − variabele kost per eenheid.

**🛠️ Hoe**:

Eenvoudige aftrekking; output is het bedrag dat elke eenheid bijdraagt aan dekking vaste kost en winst.

**Grondslag**: [[direct-costing]]

### 3. Bereken contributiemarge-ratio

Eenheidscontributie / verkoopprijs × 100 % = percentage van elke euro omzet dat bijdraagt aan vaste kost + winst.

**🛠️ Hoe**:

Praktisch voor multi-product-mix: een ratio van 35 % betekent dat 35 % van elke verkochte euro voor vaste kost en winst beschikbaar is.

**Grondslag**: Vakdoctrine


## In de praktijk

<h3 id="multi-product-mix">Multi-product-mix</h3>

> [!tip]- Multi-product-mix
> Bij meerdere producten gebruikt men de gewogen gemiddelde contributiemarge: ∑ (mix-percentage × eenheidscontributie). Bij Yperse Werkplaats BV: 60 % tapijten (€ 47) + 40 % garen (€ 30) → gewogen CM = 0,60×47 + 0,40×30 = € 40,20. 🤖


## Zie ook

- **Vereist kennis van**: [[variabele-kosten]]
- **Vereist kennis van**: [[break-even-analyse]]

## Voorbeelden

Yperse Werkplaats BV verkoopt een tapijt voor € 60 met variabele kost € 13 per stuk. Eenheidscontributie = € 60 − € 13 = € 47. Bij 10.000 stuks: totale contributiemarge € 470.000.

