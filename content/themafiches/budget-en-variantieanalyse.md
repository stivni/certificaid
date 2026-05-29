---
title: "Themafiche — Budget & variantieanalyse"
description: "Themafiche voor sub-cluster budget + variantieanalyse (PO 1.8): masterbudget-structuur, variantie-decompositie, valkuilen"
tags:
  - themafiche
  - po-1.8
  - cluster-analytische-boekhouding
---

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Budget = vooraf, variantie = achteraf — samen het sturings-instrument. Verhaal en routekaart: [[leerpaden/1.8|minicursus PO 1.8]].

</div>

---

## Take-away

- **Budget** ≠ forecast — budget is een *afspraak* (commitment), forecast is een *voorspelling* (prediction)
- **Masterbudget** = integratie van 4 deelbudgetten — pro-forma balans **moet sluiten**
- **Variantie** = werkelijk − norm — opsplitsen naar **prijs** en **hoeveelheid**
- Variantie = *diagnostisch signaal*, geen schuldvraag
- Gunstige varianties even verdacht als ongunstige

---

## Masterbudget — vier deelbudgetten

```mermaid
flowchart TD
    S[Strategisch plan] --> O[1. Operationeel budget<br/>omzet · COGS · OpEx]
    S --> I[2. Investerings-budget<br/>CapEx · afschrijvingen]
    S --> F[3. Financieel budget<br/>schuld · EV · rente]
    O --> C[4. Cash-budget<br/>liquiditeit week/maand]
    I --> C
    F --> C
    C --> P[Pro-forma jaarrekening<br/>balans + RR + KSO]
    P -.->|integratie-toets| T[Balans sluit?<br/>Cash positief?]
```

**Twee struikelblokken**:
1. **Pro-forma balans sluit niet** → fout in integratie (typisch: dividend niet in EV verwerkt)
2. **Cash-budget negatief** → werkkapitaal of financiering ontbreekt

---

## Variantie-decompositie

| | **Norm-prijs × Norm-hoeveelheid** | **Norm-prijs × Werk-hoeveelheid** | **Werk-prijs × Werk-hoeveelheid** |
|---|---|---|---|
| Begrip | *Wat zou het kosten?* | *Wat had het mogen kosten?* | *Wat heeft het gekost?* |
| Verschil-as | | Hoeveelheidsvariantie ← | → Prijsvariantie |

**Decompositie-formules:**

$$
\text{Totale variantie} = (\text{Norm} - \text{Werk}) \times P_{\text{norm}} \times Q_{\text{norm}}
$$

$$
\text{Prijsvariantie} = (P_{\text{norm}} - P_{\text{werk}}) \times Q_{\text{werk}}
$$

$$
\text{Hoeveelheidsvariantie} = (Q_{\text{norm}} - Q_{\text{werk}}) \times P_{\text{norm}}
$$

---

## Types varianties — verantwoordelijkheid

| Type variantie | Causaal verantwoordelijk | Onderzoek bij |
|---|---|---|
| Materiaal-prijs | Inkoop | Marktbeweging vs onderhandelingskracht |
| Materiaal-hoeveelheid | Productie | Verspilling · kwaliteit-grondstof |
| Arbeids-tarief | HR · marktconform loon | Loonindexering · ploegenwerk |
| Arbeids-efficiency | Productie · planning | Onervaren personeel · machine-storing |
| Overhead-volume | Capaciteits-planning | Onderbenutting · vraag-vermindering |
| Overhead-efficiency | Productie | Slecht gebruik machines · stilstand |
| Verkoop-prijs | Sales · marketing | Discount-beleid · markt-druk |
| Verkoop-volume | Sales · marketing | Marktaandeel · productlevenscyclus |

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Budget als straf-instrument | Defensief budgetteren · slack inbouwen · onbetrouwbare cijfers | Budget als *afspraak* en *leerinstrument* — niet schuld-toewijzing |
| Budget = forecast | Budget = commitment, forecast = inschatting | Twee aparte processen: budget ambitieus, forecast realistisch |
| Masterbudget = operationeel budget | Mist investering · financieel · cash → geen pro-forma balans | Volledige integratie verplicht — anders geen sluitende pro-forma |
| Pro-forma balans niet sluiten | Activa ≠ Passiva = integratie-fout | Sluiten is noodzakelijke voorwaarde — fouten lokaliseren via deelbudget-controle |
| Variantie als schuldvraag | Defensief gedrag · gemiste leer-kansen | Diagnostisch signaal — onderzoek oorzaak vóór toewijzing |
| Alleen ongunstige varianties onderzoeken | Gunstige varianties verbergen vaak risico (kwaliteit, productiviteit) | Beide kanten onderzoeken — gunstig kan kwaliteitsdaling betekenen |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Overkoepelend kader**
- [[budgetbeheer]] — cluster-hoofdrecord
- [[masterbudget]] — integratie + sub-concept kasstroomprognose

**Variantie-werkstroom**
- [[variantieanalyse]] — decompositie + verantwoordelijkheid
- [[standaardkostenmethode]] — voorafbepaalde normen

**Verwante themafiches**
- [[themafiches/kostprijsmethoden|Themafiche — Kostprijsmethoden]]
- [[themafiches/break-even-en-marginale-analyse|Themafiche — Break-even & marginale analyse]]

</div>

---

*Themafiche afgeleid uit cluster analytische-boekhouding (PO 1.8). Status: voorgesteld.*
