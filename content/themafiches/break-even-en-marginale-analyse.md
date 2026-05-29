---
title: "Themafiche — Break-even & marginale analyse"
description: "Themafiche voor sub-cluster break-even + marginale analyse (PO 1.8): formules, beslisboom, valkuilen"
tags:
  - themafiche
  - po-1.8
  - cluster-analytische-boekhouding
---

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Twee beslissings-instrumenten naast elkaar: break-even-analyse (winstgevoeligheid) + marginale analyse (incrementele beslissingen). Verhaal en routekaart: [[leerpaden/1.8|minicursus PO 1.8]].

</div>

---

## Take-away

- **Break-even** = wanneer dekken opbrengsten alle kosten? → *winstgevoeligheids-meting*
- **Marginale** = wat verandert bij déze beslissing? → *keep-or-drop · make-or-buy · special-order*
- Beide bouwen op **contributiemarge** (CM = prijs − variabele kost)
- **Vermijdbaar = relevant. Sunk = irrelevant.** Vaste overhead = irrelevant voor marginale beslissing
- Hoge vaste kosten ⇒ hoog BEP ⇒ hoge operationele hefboom ⇒ winst-gevoelig voor volume

---

## Twee analyses naast elkaar

| Dimensie | **Break-even-analyse** | **Marginale analyse** |
|---|---|---|
| Vraag | *Vanaf welk volume winst?* | *Verandert deze beslissing iets ten goede?* |
| Tijds-horizon | Korte termijn (lineair, vast bereik) | Eenmalig of korte termijn |
| Welke kosten tellen? | Alle vaste + variabele (in CM) | Alleen **relevante** (= vermijdbaar) |
| Sleutelvariabele | Contributiemarge per eenheid | Marginale kost ↔ marginale opbrengst |
| Klassieke toepassing | Productie-ondernemingen, dienstenketen | Special order · outsourcing · productmix · keep-or-drop |
| Output | BEP-volume + veiligheidsmarge | Beslissings-tabel met netto-effect |

---

## Beslisboom — welke analyse?

```mermaid
flowchart TD
    A[Welke beslissing?] -->|Volume / prijs / kostenstructuur<br/>over hele jaar| BE[Break-even-analyse]
    A -->|Eenmalige order onder kostprijs?| MA1[Marginale: dekken opbrengsten<br/>variabele + vermijdbare vaste kost?]
    A -->|Make-or-buy?| MA2[Marginale: vermijdbare<br/>vs externe kost]
    A -->|Productlijn schrappen?| MA3[Marginale: contributiemarge<br/>tegen vermijdbare vaste kosten]
    A -->|Knelpunt productiemix?| MA4[Marginale: contributiemarge<br/>per knelpunt-eenheid]
    BE -.->|let op| N1[Lineariteit alleen binnen<br/>relevant range — niet extrapoleren]
    MA1 -.->|let op| N2[Cannibalisatie:<br/>verdringt order normale verkoop?]
    MA2 -.->|let op| N3[Kwaliteit/levertijd<br/>kwalitatief weegt zwaar]
```

---

## Formules

**Break-even — punt in eenheden**
$$
\text{BEP}_{\text{eenheden}} = \frac{\text{Vaste kosten}}{\text{Contributiemarge per eenheid}}
$$

**Break-even — punt in omzet**
$$
\text{BEP}_{\text{omzet}} = \frac{\text{Vaste kosten}}{\text{CM-percentage}} \quad \text{waar CM\%} = \frac{\text{CM per eenheid}}{\text{Verkoopprijs}}
$$

**Veiligheidsmarge**
$$
\text{Veiligheidsmarge} = \frac{\text{Werkelijke omzet} - \text{BEP}_{\text{omzet}}}{\text{Werkelijke omzet}}
$$

**Marginale beslissing — special order**
$$
\Delta \text{Winst} = (P_{\text{order}} - C_{\text{variabel}}) \times Q_{\text{order}} - C_{\text{vermijdbare vaste}}
$$

**Marginale beslissing — bij knelpunt**
$$
\text{Voorkeur} = \max\left(\frac{\text{CM per eenheid}}{\text{Knelpunt-verbruik per eenheid}}\right)
$$

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| BEP extrapoleren buiten relevant range | Lineariteit geldt alleen binnen capaciteit + productmix | Bij grote uitbreiding: nieuwe vaste kosten → nieuw BEP |
| Multi-product BEP als één product | Gewogen-gemiddelde CM verandert mee met mix | BEP geldt alleen bij constante mix; mix-shift → her-berekenen |
| Vaste overhead toerekenen bij marginale beslissing | Niet-vermijdbare overhead loopt door, ongeacht beslissing | Alleen **vermijdbare** kosten zijn relevant |
| Sunk cost als argument om door te gaan | Reeds gemaakte uitgaven beïnvloeden toekomstige cash niet | Alleen toekomstige kosten/opbrengsten tellen |
| Gunstige variantie negeren | Onverwacht gunstig is even verdacht als ongunstig | Onderzoek beide: gunstig kan kwaliteitsdaling verbergen |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**De twee analyses**
- [[break-even-analyse]] — CVP-analyse + veiligheidsmarge + multi-product
- [[marginale-analyse]] — relevant cost + sunk cost + opportunity cost

**Voedingsbasis (kostprijs-methodes)**
- [[direct-costing]] — contributiemarge als bouwsteen
- [[full-costing]] — wat NIET in marginale analyse hoort

**Verwante themafiches**
- [[themafiches/kostprijsmethoden|Themafiche — Kostprijsmethoden]]
- `Themafiche — Budget & variantieanalyse` *(nog te maken)*

</div>

---

*Themafiche afgeleid uit cluster analytische-boekhouding (PO 1.8). Status: voorgesteld.*
