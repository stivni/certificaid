---
title: "Samenvatting PO 1.8 — Analytische boekhouding"
description: "Spickzettel voor cijfervak — vier methodes in één blik, formule-arsenaal per gebruikscontext, stappenplannen voor BEP / variantie / keep-or-drop / methode-keuze, klassieke valkuilen. Printbaar op 2-3 A4."
explorer_title: "6. Samenvatting"
tags:
  - samenvatting
  - po-1.8
---

<div class="no-print">

> **Samenvatting — spickzettel voor de week vóór het examen.** 1.8 is een cijfervak — deze samenvatting bundelt de formules en stappenplannen die je op het examen moet kunnen. Niet bedoeld om voor het eerst te leren — daar zijn de leerstukken voor. Voor verhaal en routekaart: [[studiemateriaal/1-8|overzicht PO 1.8]]. Voor actief doorrekenen: [[studiemateriaal/1-8/oefening|oefening Patisserie Beauclair]].

</div>

## 1. Take-away — wat je écht moet weten

- **Geen methode is intrinsiek juist** — keuze volgt het *doel*. Full = jaarrekening · Direct = beslissing · ABC = strategisch overhead-inzicht · Standaard = sturing + variantie.
- **Contributiemarge = motor** van break-even én marginale analyse. Bij capaciteit-knelpunt: CM **per knelpunt-eenheid**, niet per product-eenheid.
- **Alleen vermijdbare kosten tellen** in een beslissing. Sunk costs negeren · vaste OH die toch doorloopt negeren · opportunity cost meenemen ook al staat ze niet in de boekhouding.
- **Variantie = prijs-effect + hoeveelheids-effect** per kostencategorie. Som van sub-varianties = totale variantie (sluittoets — anders rekenfout).

---

## 2. Vier methodes in één blik

Eén rij per methode — doel, kostprijs-essentie, wanneer kiezen. Voor diepte: zie [[kostprijsmethoden-kiezen]].

| Methode | Doel | Kostprijs (essentie) | Wanneer kiezen? |
|---|---|---|---|
| **Full costing** | Voorraadwaardering · JR | Variabel + (vast / **normale** capaciteit) | Jaarrekening · IAS 2-compliance |
| **Direct costing** | Beslissingsanalyse | Enkel variabele kost | Special order · make-or-buy · BEP |
| **ABC** | Strategisch overhead-inzicht | Variabel + Σ (activity-pool × driver-verbruik) | Complexe overhead-mix · cross-subsidie ontmaskeren |
| **Standaardkosten** | Sturing + prestatie-meting | Norm-prijs × norm-hoeveelheid (alle componenten) | Budget-cyclus · variantie-opvolging |

---

## 3. Formule-arsenaal

### Kostprijs

**Full**: vaste OH delen door *normale* capaciteit (niet werkelijke productie), anders absorbeert voorraad onbenutte capaciteit. **Direct**: alleen variabele kost in product; vaste OH = periodekost. **ABC**: som over activity-pools, elk met eigen cost-driver. Onderbenutting bij full → *idle capacity* direct in resultaat (IAS 2 § 13).

$$
\text{Full} = \frac{\text{Variabel}}{\text{Werkelijke prod.}} + \frac{\text{Vast OH}}{\text{Normale capaciteit}} \qquad \text{ABC} = \sum_i (\text{Pool}_i \times \text{Driver-verbruik}_i)
$$

### Beslissing — contributiemarge en break-even

**CM** per eenheid is de bouwsteen. **BEP** in eenheden én in omzet — let op het verschil. **Veiligheidsmarge** = (Werkelijke omzet − BEP-omzet) / Werkelijke omzet. Lineariteit geldt alleen binnen *relevant range*; bij capaciteitsuitbreiding → nieuw BEP.

$$
\text{CM} = P - C_{\text{var}} \qquad \text{CM\%} = \tfrac{\text{CM}}{P} \qquad \text{BEP}_{\text{Q}} = \frac{\text{Vast}}{\text{CM}} \qquad \text{BEP}_{\text{omzet}} = \frac{\text{Vast}}{\text{CM\%}}
$$

### Beslissing — special order, knelpunt, keep-or-drop

**Special order**: alleen *vermijdbare* kosten tellen — bij volle capaciteit ook opportunity cost van verdrongen productie. **Knelpunt**: rangschik op CM ÷ schaarse-resource-eenheid (niet CM per product). **Keep-or-drop**: CM-verlies bij stop vergeleken met vermijdbare vaste kosten.

$$
\Delta_{\text{order}} = (P_{\text{order}} - C_{\text{var}})\,Q - C_{\text{vermijd. vast}} \qquad \text{Voorkeur} = \max\!\left(\frac{\text{CM}}{\text{Knelpunt-verbruik}}\right) \qquad \Delta_{\text{drop}} = -\text{CM}_{\text{lijn}} + C_{\text{vermijd. vast}}
$$

### Variantieanalyse

Per kostencategorie (materiaal, arbeid, OH) splits totaal-variantie in **prijs-effect** (P-verschil × Q-werk) en **hoeveelheids-effect** (Q-verschil × P-norm). Σ alle sub-varianties = totaal. Klopt het niet → reken-fout. Materieel (≥ 5 %) → pro-rata over voorraad én KGV (IAS 2).

$$
\text{Prijsvariantie} = (P_{\text{werk}} - P_{\text{norm}})\,Q_{\text{werk}} \qquad \text{Hoeveelheidsvariantie} = (Q_{\text{werk}} - Q_{\text{norm}})\,P_{\text{norm}}
$$

---

## 4. Stappenplannen — wat je doet op het examen

### BEP berekenen — 3 stappen

| Stap | Wat doe je? | Formule / check |
|---|---|---|
| 1 | Vaste kosten optellen | F = Σ alle vaste posten |
| 2 | CM per eenheid berekenen | CM = P − C-variabel |
| 3 | BEP-volume + BEP-omzet | BEP_Q = F / CM · BEP_omzet = F / CM% |

💡 Multi-product: **gewogen CM** op basis van mix in eenheden (niet in omzet). Mix-shift → herberekenen — BEP is mix-afhankelijk.

### Variantie decomposeren — 4 stappen

| Stap | Wat doe je? | Resultaat |
|---|---|---|
| 1 | Totale variantie = Werkelijke kost − Standaardkost | Eén bedrag (gunstig = werk < norm; ongunstig = werk > norm) |
| 2 | Per categorie: prijsvariantie + hoeveelheidsvariantie | 2 sub-bedragen per kostencategorie |
| 3 | Sluittoets: Σ alle sub-varianties = totaal? | ✓ of reken-fout in stap 2 |
| 4 | Materialiteit ≥ 5 %? | Ja → pro-rata voorraad + KGV (IAS 2). Nee → integraal in resultaat. |

💡 Voor variabele én vaste overhead is decompositie iets complexer (efficiëntie- vs bestedings-variantie); kern blijft: prijs × hoeveelheid.

### Keep-or-drop beoordelen — 3 stappen

| Stap | Wat doe je? | Check |
|---|---|---|
| 1 | Te verliezen CM bij stop optellen | Σ CM per eenheid × volume van de lijn |
| 2 | Vermijdbare vaste kosten identificeren | **Niet** alle vaste kosten zijn vermijdbaar (vast contract chef-patissier blijft) |
| 3 | Beslis: −CM + vermijdbare vaste = netto-effect | Positief → stoppen verbetert resultaat. Negatief → behouden. |

💡 Full-costing-verlies ≠ daadwerkelijk verlies bij stop. Het product 'erft' de niet-vermijdbare overhead niet — die wordt herverdeeld over de rest. Verkeerde keuze van methode → verkeerde beslissing.

### Methode kiezen — 2 vragen

| Vraag | Antwoord → methode |
|---|---|
| 1. Heb ik de cijfers nodig voor de jaarrekening? | Ja → **Full** (verplicht onder IAS 2). Nee → ga naar vraag 2. |
| 2. Heb ik vooraf-vastgelegde normen nodig voor sturing? | Ja → **Standaardkosten**. Nee → **Direct** voor beslissing, of **ABC** als overhead complex en gevarieerd is. |

---

## 5. Klassieke valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Vaste OH delen door **werkelijke** productie (full costing) | Bij onderbenutting absorbeert voorraad onbenutte capaciteit | Normale capaciteit als deler. Idle capacity → periodekost (IAS 2 § 13). |
| CM per **eenheid** vergelijken bij capaciteitsknelpunt | Hoge CM/eenheid kan een lage CM/knelpunt-uur verbergen | Rangschik op CM ÷ knelpunt-verbruik per eenheid |
| Stoppen met 'verlieslatend' product op basis van full-costing | Niet-vermijdbare overhead loopt door — wordt herverdeeld over de rest | CM-verlies vs vermijdbare vaste kosten — alleen vermijdbare telt |
| Variantie direct in resultaat bij materiële afwijking | Verstoort resultaat én voorraadwaardering | ≥ 5 %: pro-rata over voorraad + KGV. < 5 %: mag in resultaat. |
| Sunk cost als argument om door te gaan | Reeds gemaakte uitgaven beïnvloeden toekomstige cash niet | Alleen toekomstige, vermijdbare kosten + opbrengsten |

---

<div class="no-print">

## 6. Verdieping

Werkt iets niet scherp? Klik door naar het leerstuk dat het uitwerkt of het concept dat het definieert:

### Leerstukken — voor pedagogische opfris

- [[wat-is-analytische-boekhouding]] — stelsel, klassen 8/9, drie registratiesystemen, kostentypologie
- [[kostprijsmethoden-kiezen]] — vier methodes uitgewerkt op Meridia, met cross-subsidie-omkering in ABC
- [[break-even-en-marginale-beslissing]] — BEP solo + multi-product, special order, make-or-buy, knelpunt, keep-or-drop
- [[budget-en-variantieanalyse]] — masterbudget, variantie-decompositie, herzieningstriggers

### Concept-fiches — voor definitorisch detail

**Overkoepelend** — [[analytische-boekhouding]] · [[kostprijsmethoden]] · [[budgetbeheer]]

**De vier kostprijsmethodes** — [[full-costing]] · [[direct-costing]] · [[activity-based-costing]] · [[standaardkostenmethode]]

**Beslissings- en sturings-instrumenten** — [[break-even-analyse]] · [[marginale-analyse]] · [[variantieanalyse]] · [[masterbudget]]

</div>

---

*Samenvatting PO 1.8. Status: voorgesteld — rewrite naar spickzettel-vorm (formule-arsenaal + recepten) per gebruiker-sparring 2026-05-31. Vorige merge-versie (181 r., themafiche-overgenomen) vervangen.*
