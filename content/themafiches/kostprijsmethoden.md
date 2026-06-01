---
title: "Themafiche — Kostprijsmethoden"
description: "Themafiche voor sub-cluster kostprijsmethoden (PO 1.8): vier methodes naast elkaar — vergelijking, beslisboom, formules, valkuilen"
tags:
  - themafiche
  - po-1.8
  - cluster-analytische-boekhouding
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/studiemateriaal/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Vier kostprijsmethodes op één pagina: vergelijkingsmatrix, beslisboom, formules, valkuilen. Voor verhaal en routekaart: [[studiemateriaal/1-8|overzicht PO 1.8]]. Voor diepgang: de losse concept-fiches via §Doorklik.

</div>

---

## Take-away

- **Géén methode is intrinsiek "juist"** — keuze volgt het *doel*, niet de "correctheid"
- **Direct ↔ Full** worden vaak *parallel* gevoerd: direct voor beslissingen, full voor jaarrekening
- **Standaardkosten ↔ variantieanalyse** is een paar — zonder variantie heeft norm geen sturing-waarde
- **ABC** is duur in implementatie — alleen waard bij *sterk variërend overhead-verbruik* per product
- Bij **onderbenutting** overrapporteert full costing → vaste overhead naar normale capaciteit, niet werkelijke productie

---

## Vergelijkingsmatrix

| Dimensie | **Full costing** | **Direct costing** | **ABC** | **Standaardkosten** |
|---|---|---|---|---|
| Welke kosten in product? | Alle productiekosten | Enkel variabele | Alle, via cost-drivers | Norm-kosten (alle) |
| Vaste overhead-toerekening | 1 sleutel (volgens capaciteit) | Niet aan product — periodekost | Multiple activity-pools | Norm × werkelijk volume |
| Jaarrekening-conform? | ✅ Verplicht (IAS 2 + KB-WVV) | ❌ Niet voor externe rapportering | ✅ Mits onderbouwd | ✅ Mits varianties verwerkt |
| Primair doel | Voorraadwaardering · externe rapportering | Beslissings-analyse (CVP, marge) | Kosteninzicht · strategische prijszetting | Budgetsturing · prestatie-meting |
| Sterkte | Wettelijk gedragen · audit-friendly | Snel · transparant beslissingsinstrument | Realistisch bij complexe overhead-structuur | Norm geeft proactieve sturing |
| Klassieke valkuil | Volume-effect bij onderbenutting | Niet voor lange-termijn prijszetting | Implementatie-kost (time-studies) | Variantie-dispositie (IAS 2) |

---

## Beslisboom — welke methode wanneer?

```mermaid
flowchart TD
    A[Wat is het doel?] -->|Jaarrekening<br/>voorraadwaardering| F[Full costing]
    A -->|Eenmalige beslissing<br/>make-or-buy / prijszetting| D[Direct costing]
    A -->|Strategisch<br/>kosteninzicht| AB[ABC]
    A -->|Budgetsturing<br/>prestatie-meting| S[Standaardkosten]
    F -.->|let op| N1[Volume-correctie bij<br/>onderbenutting capaciteit]
    D -.->|niet voor| N2[Lange-termijn prijszetting<br/>contributiemarge ≠ winst]
    AB -.->|let op| N3[Implementatie-zwaar<br/>vereist management-buy-in]
    S -.->|let op| N4[Materiele varianties:<br/>pro-rata aan voorraad IAS 2]
```

---

## Formules

**Full costing** — kostprijs per eenheid
$$
\text{Kostprijs} = \frac{\text{Variabele kosten}}{\text{Werkelijke prod.}} + \frac{\text{Vaste kosten}}{\text{Normale capaciteit}}
$$

**Direct costing** — contributiemarge
$$
\text{Contributiemarge} = \text{Verkoopprijs} - \text{Variabele kost per eenheid}
$$

**ABC** — kost per product
$$
\text{Kost} = \sum_i \left( \text{Activity-pool}_i \times \text{Cost-driver}_i \times \text{Verbruik}_{\text{product}} \right)
$$

**Standaardkosten** — variantie-decompositie
$$
\text{Totale variantie} = \underbrace{(\text{Norm-prijs} - \text{Werkelijke prijs}) \times Q_{\text{werk}}}_{\text{Prijsvariantie}} + \underbrace{(Q_{\text{norm}} - Q_{\text{werk}}) \times P_{\text{norm}}}_{\text{Hoeveelheidsvariantie}}
$$

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| "Eén methode is dé juiste" | Methodes zijn niet vergelijkbaar in absolute zin | Doel-afhankelijke keuze: jaarrekening ≠ beslissing ≠ strategie |
| Vaste overhead delen door **werkelijke** productie (full costing) | Bij onderbenutting concentreert vast OH zich onterecht in voorraad | Volume-correctie: vast OH pro-rata-normaal → onderbenuttingsvariantie = periodekost |
| Direct costing-prijs als LT-prijs hanteren | Contributiemarge dekt alleen variabele kost; vaste kosten worden niet gedekt | Direct costing alleen voor LT-grens-beslissing; LT-prijs vereist volledige kosten-recovery |
| Variantie altijd direct in resultaat (standaardkosten) | Materiele varianties verstoren resultaat én jaarrekening-cijfers | IAS 2: materiele varianties pro-rata aan voorraad én KGV; niet-materieel mag in resultaat |

---

<div class="no-print">

## Verdieping

### Leerstukken — voor pedagogische opfris

Werkt iets niet meer scherp? Klik door naar het leerstuk dat het uitwerkt:

- [[kostprijsmethoden-kiezen]] — vier methodes naast elkaar uitgewerkt op Meridia, met beslisboom, cross-subsidie-omkering in ABC, en diensten-mini-case
- [[wat-is-analytische-boekhouding]] — kostentypologie + klassen 8/9 als bouwsteen voor methodekeuze
- [[break-even-en-marginale-beslissing]] — direct costing toegepast op beslissingen
- [[budget-en-variantieanalyse]] — standaardkost als norm voor variantieanalyse

### Concept-fiches — voor definitorisch detail

Voor wie een wettekst-pointer of nauwkeurige definitie zoekt:

**Overkoepelend** — [[analytische-boekhouding]] (cluster-hoofdrecord) · [[kostprijsmethoden]] (keuze-kader)

**De vier methodes** — [[full-costing]] (alle productiekosten, IAS 2-conform) · [[direct-costing]] (alleen variabele, voor beslissingen) · [[activity-based-costing]] (cost-drivers, realistische overhead) · [[standaardkostenmethode]] (norm-kosten + variantieanalyse)

### Andere themafiches in dit cluster

- [[themafiches/break-even-en-marginale-analyse|Themafiche — Break-even & marginale analyse]]
- [[themafiches/budget-en-variantieanalyse|Themafiche — Budget & variantieanalyse]]
- [[themafiches/analytische-boekhouding-stelsel|Themafiche — Analytische bh: stelsel & registratie]]

</div>

---

*Themafiche afgeleid uit cluster analytische-boekhouding (PO 1.8). Status: voorgesteld.*
