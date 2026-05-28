---
title: "Masterbudget"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.8.VI.D
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/masterbudget.json"
---

# Masterbudget

_Procedure_

🏛️ Kader · Anchors: `1.8.VI.D` · Wave: `cluster-extract-management-accounting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: master budget · integrale budget · geïntegreerd budget — **Vertalingen**: fr: budget global

## Definitie

🔗 Het masterbudget is het integrale, geconsolideerde budget van een onderneming voor een komende periode (typisch één jaar) dat alle deelbudgetten samenbrengt: het operationeel budget (omzet en bedrijfskosten), het investerings-budget (kapitaaluitgaven), het financieel budget (financieringsbeslissingen, dividenden) en het cash-budget (geldverkeer). Output: een pro-forma resultatenrekening, pro-forma balans en pro-forma kasstromenoverzicht voor de budget-periode. Het masterbudget toont hoe de operationele plannen zich vertalen naar de jaarrekening + cashpositie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Het masterbudget is de cijfermatige stresstest van het strategisch plan. Pas wanneer je alle deelplannen consolideert in één pro-forma jaarrekening, zie je of de strategische ambitie haalbaar is met de beschikbare cashflow. Vaak struikelt het integratie-werk op één van twee zaken: (1) onvoldoende cash om de geplande investeringen te dragen — extra financiering of fasering nodig; (2) onhaalbaar verkoopcijfer gegeven de beschikbare productiecapaciteit — extra investering nodig of verkoopdoel verlagen. Het masterbudget dwingt die spanningen op tafel vóór het jaar begint, niet halverwege.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Losse deelbudgetten zonder integratie zijn waardevol op afdelingsniveau maar verbergen incoherenties: een ambitieus verkoopbudget zonder dekkende productiecapaciteit, of een investeringsplan zonder financieringsmiddelen. Het masterbudget integreert alle ambities en plannen tot één coherente set van pro-forma cijfers — daardoor wordt elke incoherentie zichtbaar en moet ze opgelost vóór het jaar begint.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Mid-size en grote ondernemingen met meerdere afdelingen, investeringscycli, financieringsbeslissingen. Banken en RvB-leden vragen het masterbudget als onderbouwing voor kredietverlening en strategie-evaluatie.

## Bouwstenen

### 💡 Vier deelbudgetten binnen het masterbudget  
_`begrip`_

🔗 (1) Operationeel budget: omzet-budget → productie-budget → grondstof-budget + arbeids-budget + overhead-budget → cost of goods sold → bruto-marge → verkoop- en administratieve kostenbudget → bedrijfsresultaat. (2) Investerings-budget: kapitaaluitgaven voor vaste activa met motivering en NPV-analyse per investering. (3) Financieel budget: financieringsbeslissingen (nieuwe lening, kapitaalsverhoging), aflossingen, dividend-uitkering, financiële opbrengsten en kosten. (4) Cash-budget: maandelijkse of wekelijkse cashflows — inkomsten uit verkoop (vertraagd door betalingstermijnen), uitgaven aan leveranciers en personeel, investeringen, financiering. Geeft de cash-positie maand per maand.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Opbouw-volgorde — start bij verkoop  
_`stap`_

🔗 Begin altijd met het verkoopbudget — dat bepaalt alles. Stap 1: verkoopbudget (volume × prijs per product per periode). Stap 2: productiebudget (verkoop + gewenste eindvoorraad − beginvoorraad = te produceren). Stap 3: directe-materialen-budget (productie × standaardverbruik × standaardprijs). Stap 4: arbeids-budget (productie × standaarduren × standaardloon). Stap 5: variabele- en vaste-overhead-budget. Stap 6: cost of goods sold + bruto-marge. Stap 7: verkoop- en administratieve kostenbudget. Stap 8: investerings- en financieel budget integreren. Stap 9: cash-budget afleiden uit alle voorgaande. Stap 10: pro-forma jaarrekening + ratio-analyse.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Scenario-modellen — best / base / worst case  
_`mechanisme`_

🔗 Een masterbudget op basis van één set veronderstellingen is een puntschatting — zegt niets over robuustheid bij wijziging. Drie scenario's: base case (meest waarschijnlijke verwachting), best case (gunstige omgeving, +10 à 20% omzet), worst case (recessie, −10 à 20% omzet). Bij elk scenario: pro-forma resultaat + cashpositie. Sleutelvraag: 'overleeft de onderneming worst case zonder extra financiering?'. Indien niet: dwingende noodzaak voor backup-kredietlijn, kostendispositie-plan of voorzichtigere investeringen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Iteratie + bijsturing tijdens opmaak  
_`regel`_

🔗 Het masterbudget is bijna nooit klaar in één doorloop. Eerste consolidatie blijkt typisch: onvoldoende productiecapaciteit, te zware cash-piek in Q1, of resultaat onder strategisch doel. Dan iteratie: aanpassen van productiecapaciteit, fasering investering, herzien verkoopprijs of kostenstructuur. Twee tot drie iteraties is normaal — bij meer dan vijf wijst dit op gebrek aan duidelijke strategische kaders (top-down te zwak). Eindafstemming met directie + RvB voor goedkeuring.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Aurelia Holding NV — cash-budget legt knelpunt bloot 🔗

_Aurelia plant 5.000.000 EUR omzet, 500.000 EUR investering in nieuwe productielijn (Q2), gemiddelde klantbetalingstermijn 60 dagen, leveranciers 30 dagen._

**Berekening:**
- Q1 omzet 1.000.000 → cashontvangst pas in Q2 door 60-dagen-termijn
- Q1 productiekosten 700.000 → betaling Q1 (loon onmiddellijk) + Q2 (leverancier)
- Q2 omzet 1.250.000 → cashontvangst Q3
- Q2 productiekosten 850.000 → betaling Q2/Q3
- Q2 investering 500.000 → cashuitstroom Q2
- Q1-Q2 cumulatief: cashontvangst 1.000.000; cashuitgave loon + leverancier + investering ≈ 2.300.000
- Cashtekort Q1-Q2 ≈ 1.300.000 EUR — als cashreserve onvoldoende is, moet een kredietlijn worden voorzien

→ **Resultaat**: Het masterbudget toont dat ook bij winst-perspectief het cash-knelpunt in Q1-Q2 fataal kan zijn. Actie: kredietlijn van 1.500.000 EUR vooraf onderhandelen, of investering faseren naar Q3-Q4.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Masterbudget = operationeel budget

**Verkeerde assumptie**: Het masterbudget is gewoon het operationeel budget met wat extra.

**Kernpunt**: Het masterbudget is de integratie van alle vier deelbudgetten — operationeel, investerings, financieel, cash. Veel ondernemingen stoppen bij het operationeel budget en ontdekken halverwege het jaar dat hun cashplanning niet klopt. Het masterbudget integreert expliciet de cash-impact van investeringen + financieringsbeslissingen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Pro-forma balans niet sluiten

**Verkeerde assumptie**: De pro-forma balans hoeft niet exact te kloppen — het is toch een voorspelling.

**Kernpunt**: De pro-forma balans MOET sluiten (activa = passiva). Wanneer hij niet sluit, is er een fout in de integratie. Een typisch fout: dividend uit te keren maar niet weggeschreven uit reserves; of investering geboekt in activa maar niet de financiering ervan in passiva. Sluitende balans = sanity-check op de coherentie van het hele masterbudget.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Kredietaanvraag — masterbudget als onderbouwing

_Cliente vraagt extra kredietlijn voor expansie — bank vraagt een onderbouwd masterbudget._

#### 🧭 Adviseur

##### 👣 Masterbudget opbouwen voor de bank  
_`stap`_

🔗 Banken willen drie scenario's (base, worst, best) met pro-forma jaarrekening + maandelijks cash-budget voor de looptijd van het krediet (typisch 5 jaar). Sleutel-ratio's die de bank zal opvragen: schuldgraad, current ratio, interest coverage, debt service coverage (cashflow / aflossingen + interesten). Een goed masterbudget toont expliciet dat ook in worst case de DSCR > 1,2 blijft. Onderbouw elke aanname met externe bron of historische data — banken vertrouwen niet op 'we denken dat de omzet stijgt'.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Budgetbeheer Σ (overkoepelend) → [[budgetbeheer]] _(moet-verwijzen)_
- ↪ Kasstroomanalyse (cash-budget-context) → [[kasstroom-analyse]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[budgetbeheer]]
### `vereist`
- [[kasstroom-analyse]] — Het cash-budget binnen het masterbudget is een prospectief kasstromenoverzicht.
