---
title: "Themafiche — Vaste inrichting"
description: "Themafiche voor sub-cluster vaste inrichting (PO 2.8): drempelvragen bij inbound/outbound + materieel vs personeel + winsttoerekening + BTW-VI vs IB-VI"
tags:
  - themafiche
  - po-2.8
  - cluster-europees-en-internationaal-fiscaal-recht
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/leerpaden/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Drempel-vragen + materieel/personeel-VI + agent-VI + DBV vs WIB92 + winsttoerekening + BTW-VI ≠ IB-VI. Voor verhaal en routekaart: [[leerpaden/2.8|minicursus PO 2.8]].

</div>

---

## Take-away

- **BTW-VI ≠ IB-VI — twee verschillende begrippen**: BTW-VI (VO 282/2011 art. 11) lagere drempel; IB-VI (art. 5 OESO-MV / WIB92 art. 229) hogere materiële drempel
- **DBV-drempels primeren op WIB92** (voor inbound) wanneer DBV bestaat — 12 maanden bouwwerken in OESO-MV vs 30 dagen WIB92
- **Dochtervennootschap = automatisch GEEN VI van moeder** (art. 5 §7 OESO-MV) — controle alleen volstaat niet
- **Drie VI-types**: materieel (fysieke installatie) · agent-VI (afhankelijke vertegenwoordiger) · dienst-VI (sommige DBV's, niet OESO-default)
- **Winsttoerekening "Authorised OECD Approach" (AOA)**: VI behandeld als afzonderlijke onderneming met eigen functies, activa en risico's
- **Anti-fragmentatie BEPS Actie 7 / MLI**: kunstmatig opsplitsen om VI-drempel te ontwijken niet toegestaan

---

## Drempelvragen — beslisboom

```mermaid
flowchart TD
    A["Buitenlandse aanwezigheid?"] --> B{Vorm?}
    B -->|Vaste plaats van bedrijfsuitoefening<br/>(kantoor, fabriek, werf)| C["Materiële VI"]
    B -->|Bouwwerf of installatieproject| D["Bouw-VI<br/>WIB 30 dgn / DBV 12 mnd"]
    B -->|Persoon afhankelijk vertegenwoordiger<br/>+ contractbevoegdheid| E["Agent-VI<br/>(art. 5 §5 OESO-MV)"]
    B -->|Persoon onafhankelijke makelaar/<br/>commissionair| NV["Geen VI<br/>(art. 5 §6)"]
    B -->|Voorbereidende of hulpactiviteit| NV2["Geen VI<br/>(art. 5 §4 exclusies)"]
    B -->|Dochter-vennootschap| NV3["Geen VI<br/>(art. 5 §7) — tenzij agent-VI-criteria"]
    C --> WT["Winsttoerekening AOA<br/>(functies + activa + risico's)"]
    D --> WT
    E --> WT
```

---

## Materiele VI — definitie (art. 5 §1 OESO-MV)

| Element | Vereiste |
|---|---|
| **Vaste plaats** | Geografisch geïdentificeerd + permanent (geen ad hoc-aanwezigheid) |
| **Plaats van bedrijfsuitoefening** | Plek waar activiteit wordt uitgeoefend (kantoor, fabriek, mijn, brongebruik) |
| **Door middel van** | Via die plaats activiteit voeren |
| **Duurzaamheid** | Typisch > 6 maanden (geen wettelijke regel — feitelijk criterium) |
| **Voorbeelden POSITIEF** | Filiaal, kantoor, fabriek, mijn, olie/gas-bron, bouwplaats > 12 mnd |
| **Voorbeelden NEGATIEF (art. 5 §4)** | Opslagplaats voorraad voor levering · inkoop-installatie · hulpkantoor · voorbereidende activiteit |

---

## Agent-VI (art. 5 §5)

| Voorwaarde | Inhoud |
|---|---|
| **Afhankelijke persoon** | Werknemer of vergelijkbaar onderschikt — niet zelfstandige makelaar |
| **Contractbevoegdheid** | Gewoonlijk contracten sluit in naam van moeder (substantieel rol bij sluiten) |
| **Vaste relatie** | Niet ad hoc |
| **Effect** | VI van moeder in agent-land — winsttoerekening via AOA |
| **Anti-fragmentatie BEPS** | Commissionnaire-structuur opgevangen — "substantieel rol" volstaat zelfs zonder formeel ondertekenen |

---

## Bouw-VI — DBV vs WIB92

| Bron | Drempel | Toepassing |
|---|---|---|
| **OESO-MV art. 5 §3** | 12 maanden | Standaard in BE-DBV's met verdragspartner |
| **WIB92 art. 229 §1, 8°** | 30 dagen | Eenzijdige BE-regel — voor inbound uit niet-verdragsland |
| **Conflict** | DBV primeert | Bij DBV-partner: 12 mnd. Bij niet-DBV-land: 30 dagen WIB92 |

⚠️ Examen-typisch: 30 dagen automatisch toepassen zonder DBV-check.

---

## Dienst-VI (sommige DBV's)

| Element | Toelichting |
|---|---|
| **Niet standaard OESO-default** | OESO-MV kent geen autonome dienst-VI |
| **BE-DBV's met dienst-VI** | Bijv. DBV met India, Thailand, sommige andere — drempel typisch 183 dagen dienst-uitvoering in 12 mnd |
| **Effect** | VI ontstaat door langdurige dienstverrichting zonder fysieke plaats |
| **Pas op** | Check elk DBV-specifiek protocol; geen algemene regel |

---

## Winsttoerekening — Authorised OECD Approach (AOA)

| Stap | Wat? |
|---|---|
| **1. Functionele analyse** | Welke functies voert VI uit (verkoop, R&D, productie, etc.) |
| **2. Activa-allocatie** | Welke activa zijn economisch toerekenbaar aan VI |
| **3. Risico-allocatie** | Welke risico's draagt VI |
| **4. Behandel VI als afzonderlijke onderneming** | "Significant people functions"-test |
| **5. Arm's length transactions intern (dealings)** | Hoofdkantoor ↔ VI = armslengte-prijs |
| **6. Winsttoerekening** | Op basis van functies/activa/risico's |

**BE-toepassing**: VenB op winst toegerekend aan VI (inbound) of vrijstelling met PV via DBV (outbound).

---

## BTW-VI vs IB-VI — verschillen

| Element | BTW-VI (VO 282/2011 art. 11) | IB-VI (OESO-MV art. 5 / WIB92 art. 229) |
|---|---|---|
| **Drempel** | Relatief laag: personeel + technische middelen om diensten af te nemen/leveren | Hoger: vaste plaats + duurzaamheid + materiële activiteit |
| **Doel** | Plaats van handeling BTW | Heffingsbevoegdheid VenB |
| **Voorbereidende activiteiten** | Kunnen kwalificeren | Uitgesloten (art. 5 §4) |
| **Dochter** | Kan dienen als BTW-VI (vergelijkbare middelen) | Geen automatische IB-VI |
| **Examen-typisch verwarringspunt** | "Vaste inrichting" zonder specificatie BTW of IB | Specificeer: welke heffing? |

---

## Inbound vs outbound — BE-perspectief

| Richting | BE-rol | Behandeling |
|---|---|---|
| **Inbound (buitenlandse moeder met VI in BE)** | BE = bronstaat | BNI-VenB op aan VI toegerekende winst (art. 229 WIB92) |
| **Outbound (Belgische moeder met VI in buitenland)** | BE = woonstaat | Vrijstelling met progressievoorbehoud via DBV (art. 23 OESO-MV) — buitenland heft |
| **Outbound zonder DBV** | BE = woonstaat | Buitenlandse winst belast in BE (geen DBV-voorkoming) — eenzijdige BE-voorkoming via art. 156 WIB92 |
| **VI-verlies outbound** | DBV-afhankelijk | Soms aftrekbaar tijdelijk in BE met recapture bij latere winst (art. 185/3 WIB92) |

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| BTW-VI = IB-VI | Eén "vaste-inrichting"-begrip | Twee verschillende rechtsbronnen + drempels. BTW-VI lagere drempel; IB-VI hogere materiële drempel |
| Dochter = VI van moeder | Controle = VI | Art. 5 §7 OESO-MV: dochter is aparte rechtspersoon. Alleen agent-VI-criteria kunnen VI doen ontstaan |
| WIB92 30-dagen-drempel automatisch | Voor élke bouwwerf 30 dgn | WIB92 30 dgn alleen voor niet-DBV-landen. Met DBV: 12 mnd OESO-MV |
| Voorbereidende activiteit = nooit VI | "Voorbereidend" ≠ VI | Anti-fragmentatie BEPS / MLI: kunstmatig fragmenteren wordt opgevangen — totale activiteit beoordelen |
| Agent-VI vereist formeel ondertekenen | Pas VI als agent contracten ondertekent | Substantieel rol bij sluiten (zelfs zonder formele ondertekening) sinds BEPS Actie 7 |
| Outbound VI-winst altijd in BE belast | BE belast wereldwijd | Vrijstelling met PV via DBV (art. 23) — buitenland heft. Geen DBV = voorkoming via WIB92 art. 156 (eenzijdig) |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Vaste inrichting**
- [[vaste-inrichting]] — definitie + types + drempels
- [[belasting-niet-inwoners]] — BNI-mechanisme voor inbound

**Cross-cutting internationaal**
- [[dubbelbelastingverdrag]] — DBV-kader
- [[internationaal-fiscaal]] — overkoepelend
- [[buitenlandse-winst-en-verlies]] — VI-verlies behandeling
- [[internationale-structurering-vennootschap]] — VI vs dochter-keuze
- [[transfer-pricing]] — TP voor VI-transacties (AOA)

**BTW-VI**
- [[plaats-van-handeling-btw]] — BTW-VI in plaats-van-handeling
- [[btw-belastingplichtige]] — VI-begrip BTW

**Verwante themafiches**
- [[themafiches/dbv-toepassing|Themafiche — DBV-toepassing]]
- [[themafiches/transfer-pricing-en-beps|Themafiche — Transfer pricing & BEPS]]
- [[themafiches/eu-fiscale-richtlijnen|Themafiche — EU fiscale richtlijnen]]

</div>

---

*Themafiche afgeleid uit cluster europees-en-internationaal-fiscaal-recht (PO 2.8). Status: voorgesteld.*
