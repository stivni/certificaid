---
title: "Themafiche — Jaarrekeninganalyse: aanpak & herrangschikking"
description: "Themafiche voor sub-cluster jaarrekeninganalyse + functionele balans (PO 1.3 + 1.9): horizontaal/verticaal, herrangschikking, NBK/BBK/NT-drieluik"
tags:
  - themafiche
  - po-1.3
  - po-1.9
  - cluster-financiele-analyse
---

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** De vier analyse-technieken + functionele balans op één pagina. Voor verhaal en routekaart: [[leerpaden/1.3|minicursus PO 1.3]] of [[leerpaden/1.9|minicursus PO 1.9]].

</div>

---

## Take-away

- **Eén jaar is geen analyse** — trend over 3-5 jaar is minimum; vergelijking met sector-benchmark is cruciaal
- **Herrangschikking is geen optie** — balans naar economische bestemming + resultatenrekening tot bedrijfsresultaat
- **Functionele balans-drieluik**: NBK · BBK · NT — beschrijft het *werkkapitaal-evenwicht* in één oogopslag
- **Gulden regel**: NBK ≥ BBK ⇒ NT ≥ 0; structureel negatieve NT signaleert kortlopende krediet-afhankelijkheid
- [[toegevoegde-waarde|TW]] = output − input (extern); maatstaf van bijdrage onderneming aan economie + verdeling onder stakeholders

---

## Vier analyse-technieken

| Techniek | Wat? | Hoe? | Sterkte | Beperking |
|---|---|---|---|---|
| **Horizontale analyse** | Trend over tijd | Basisjaar = 100; absolute & relatieve groei | Detecteert groei/krimp-patronen | Inflatie-vertekening; basisjaar-keuze |
| **Verticale analyse** | Interne structuur | % van balanstotaal of omzet (common-size) | Vergelijkbaar tussen ondernemingen | Verbergt absolute schaal |
| **Herrangschikking balans** | Economische lens | Operationeel vs niet-operationeel; LT vs KT | Activeert functionele balans + ratio's | Vereist kennis van klasse-codes |
| **Herrangschikking resultatenrekening** | Recurrent vs niet-recurrent | Bedrijfsresultaat isoleren; uitzonderlijke posten | Toont onderliggende winstkracht | Subjectief in beoordeling "uitzonderlijk" |

---

## Functionele balans — drieluik

**Definities** (formules):

$$
\text{NBK (werkkapitaal)} = \text{Permanent vermogen} - \text{Vaste activa} = \text{Vlottende activa} - \text{Schulden} \le 1 \text{ jaar}
$$

$$
\text{BBK (behoefte bedrijfskapitaal)} = \text{Exploitatie-vlottende activa} - \text{Exploitatie-schulden} \le 1 \text{ jaar}
$$

$$
\text{NT (nettothesaurie)} = \text{NBK} - \text{BBK}
$$

**Tekenleeskaart — 4 typische combinaties**:

| NBK | BBK | NT | Interpretatie |
|---|---|---|---|
| + | + (klein) | + | Gezonde liquiditeits-marge |
| + (klein) | + (groot) | − | Cyclische krediet-afhankelijkheid |
| − | + | − − | Acute liquiditeitskrapte (rode vlag) |
| + (groot) | − | + + | Over-financiering (lage rentabiliteit-risico) |

---

## Analyse-flow

```mermaid
flowchart TD
    A["Ruwe jaarrekening<br/>balans + RR + toelichting"] --> B[Herrangschikking balans<br/>economisch · LT/KT]
    A --> C[Herrangschikking RR<br/>recurrent isoleren]
    B --> D[Functionele balans<br/>NBK · BBK · NT]
    B --> E[Ratio-berekening<br/>4 families]
    C --> E
    D --> E
    E --> F[Trend over 3-5 jaar<br/>horizontaal]
    E --> G[Sector-benchmark<br/>NBB · Companyweb]
    F --> H[Financiële diagnose<br/>integrale oordeel]
    G --> H
```

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Eén jaar als analyse | Snapshot misleidt; jaareffecten en accidentele posten domineren | Minstens 3 jaar trend + sector-benchmark |
| NBK > 0 = gezond | Te hoge NBK = over-financiering, lage rentabiliteit | Verhouding NBK/BBK telt, niet absoluut niveau |
| Statisch lezen | Balansdatum vs operationele cyclus; seizoens-effect | Vergelijking meerdere jaren + sector + maand-data indien beschikbaar |
| TW met omzet/marge verwarren | TW = bijdrage onderneming aan economie; sector-vergelijkbaar | Omzet = volume; brutomarge = na grondstoffen; TW = na alle externe inputs |
| Liquiditeit alleen uit current ratio | Verbergt voorraad-overschatting + betalingsgewoonten | Combineren met BBK + DSO/DPO/DIO + cash-budget |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Overkoepelend**
- [[jaarrekeninganalyse]] — hoofdrecord (4 technieken + doelstellingen)
- [[functionele-balans]] — NBK/BBK/NT-drieluik
- [[toegevoegde-waarde]] — output − input

**Verwante themafiches**
- [[themafiches/ratio-families|Themafiche — Ratio-families]]
- [[themafiches/kasstroom-analyse|Themafiche — Kasstroom-analyse]]
- [[themafiches/continuiteit-en-diagnose|Themafiche — Continuïteit & financiële diagnose]]

</div>

---

*Themafiche afgeleid uit cluster financiele-analyse (PO 1.3 + 1.9). Status: voorgesteld.*
