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

_Procedure_ · ook: master budget · integrale budget · geïntegreerd budget

## Definitie

Het masterbudget is het integrale, geconsolideerde budget van een onderneming voor een komende periode (typisch één jaar) dat alle deelbudgetten samenbrengt: het operationeel budget (omzet en bedrijfskosten), het investerings-budget (kapitaaluitgaven), het financieel budget (financieringsbeslissingen, dividenden) en het cash-budget (geldverkeer). Output: een pro-forma resultatenrekening, pro-forma balans en pro-forma kasstromenoverzicht voor de budget-periode. Het masterbudget toont hoe de operationele plannen zich vertalen naar de jaarrekening + cashpositie.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Het masterbudget is de cijfermatige stresstest van het strategisch plan. Pas wanneer je alle deelplannen consolideert in één pro-forma jaarrekening, zie je of de strategische ambitie haalbaar is met de beschikbare cashflow. Vaak struikelt het integratie-werk op één van twee zaken: (1) onvoldoende cash om de geplande investeringen te dragen — extra financiering of fasering nodig; (2) onhaalbaar verkoopcijfer gegeven de beschikbare productiecapaciteit — extra investering nodig of verkoopdoel verlagen. Het masterbudget dwingt die spanningen op tafel vóór het jaar begint, niet halverwege.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Losse deelbudgetten zonder integratie zijn waardevol op afdelingsniveau maar verbergen incoherenties: een ambitieus verkoopbudget zonder dekkende productiecapaciteit, of een investeringsplan zonder financieringsmiddelen. Het masterbudget integreert alle ambities en plannen tot één coherente set van pro-forma cijfers — daardoor wordt elke incoherentie zichtbaar en moet ze opgelost vóór het jaar begint.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Mid-size en grote ondernemingen met meerdere afdelingen, investeringscycli, financieringsbeslissingen. Banken en RvB-leden vragen het masterbudget als onderbouwing voor kredietverlening en strategie-evaluatie.

## Sub-concepten

### 📦 Kasstroomprognose / rolling forecast

#### Definitie

Een kasstroomprognose is een cash-budget op een kortere horizon dan het masterbudget, typisch een **13-weken-prognose** die maandelijks (of zelfs wekelijks) wordt geüpdatet. Doelstelling: een actueel beeld van de liquiditeitspositie + scenario-analyse op korte termijn (baseline / pessimistisch / optimistisch). Waar het cash-budget binnen het masterbudget jaarlijks-statisch is, is de rolling forecast continu bijgewerkt — oudste week valt weg, nieuwste week komt erbij.

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

#### Substantie

Bouwstenen van de rolling forecast: (a) **inkomende kasstromen** op basis van DSO (gemiddelde klanten-betalingstermijn) toegepast op verkoop-pipeline; (b) **uitgaande kasstromen** = vaste kosten (loon, huur, leningaflossingen) + DPO-gestuurde leveranciersbetalingen; (c) seizoeneffecten (BTW-betalingen op kwartaalbasis, voorafbetalingen VenB); (d) geplande kapitaal-investeringen; (e) belastingbetalingen; (f) dividend-uitkeringen. Output: cash-positie per week + de kortste-tijdshorizon waarin een krediet-faciliteit moet worden aangesproken.

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

#### Rationale

De rolling forecast vertaalt de structurele [[functionele-balans#NT]]-evolutie (nettothesaurie als verschil tussen permanente financiering en duurzame behoefte) naar een week-by-week-praktijk: wat is de cash-positie op elk moment, met welke marge tegenover de gecommitteerde kredietlijnen?

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

#### 🧭 Waarom 13 weken?

13 weken = één kwartaal = voldoende horizon om de meeste cyclische cash-effecten te zien (BTW-aangifte, kwartaal-eindfacturatie, voorafbetaling VenB) zonder zo ver te gaan dat de prognose onbetrouwbaar wordt. Korter dan 4 weken: te kortzichtig voor liquiditeitsbeheer; langer dan 26 weken: assumpties te speculatief voor wekelijkse beslissingen.

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

#### ⚙️ Drie scenario's per update

Per update drie scenario's: (1) **baseline** = meest waarschijnlijke verwachting op basis van pipeline + historische DSO/DPO; (2) **pessimistisch** = late klantbetaling (DSO +15 dagen) + uitval grootste klant; (3) **optimistisch** = sneller incasso + extra order. Kortste-tijdshorizon-vraag: 'in welke week komt de cash-positie onder 0 in scenario pessimistisch?'.

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>


**✅ Voor**
- 🤖 CFO-dashboard, treasury-management, kredietnegotiatie met bank, bewaking van covenant-ratio's, faillissementsdreiging-monitoring.

## Bouwstenen

### 💡 Vier deelbudgetten binnen het masterbudget

(1) Operationeel budget: omzet-budget → productie-budget → grondstof-budget + arbeids-budget + overhead-budget → cost of goods sold → bruto-marge → verkoop- en administratieve kostenbudget → bedrijfsresultaat. (2) Investerings-budget: kapitaaluitgaven voor vaste activa met motivering en NPV-analyse per investering. (3) Financieel budget: financieringsbeslissingen (nieuwe lening, kapitaalsverhoging), aflossingen, dividend-uitkering, financiële opbrengsten en kosten. (4) Cash-budget: maandelijkse of wekelijkse cashflows — inkomsten uit verkoop (vertraagd door betalingstermijnen), uitgaven aan leveranciers en personeel, investeringen, financiering. Geeft de cash-positie maand per maand.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Opbouw-volgorde — start bij verkoop

Begin altijd met het verkoopbudget — dat bepaalt alles. Stap 1: verkoopbudget (volume × prijs per product per periode). Stap 2: productiebudget (verkoop + gewenste eindvoorraad − beginvoorraad = te produceren). Stap 3: directe-materialen-budget (productie × standaardverbruik × standaardprijs). Stap 4: arbeids-budget (productie × standaarduren × standaardloon). Stap 5: variabele- en vaste-overhead-budget. Stap 6: cost of goods sold + bruto-marge. Stap 7: verkoop- en administratieve kostenbudget. Stap 8: investerings- en financieel budget integreren. Stap 9: cash-budget afleiden uit alle voorgaande. Stap 10: pro-forma jaarrekening + ratio-analyse.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Scenario-modellen — best / base / worst case

Een masterbudget op basis van één set veronderstellingen is een puntschatting — zegt niets over robuustheid bij wijziging. Drie scenario's: base case (meest waarschijnlijke verwachting), best case (gunstige omgeving, +10 à 20% omzet), worst case (recessie, −10 à 20% omzet). Bij elk scenario: pro-forma resultaat + cashpositie. Sleutelvraag: 'overleeft de onderneming worst case zonder extra financiering?'. Indien niet: dwingende noodzaak voor backup-kredietlijn, kostendispositie-plan of voorzichtigere investeringen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Iteratie + bijsturing tijdens opmaak

Het masterbudget is bijna nooit klaar in één doorloop. Eerste consolidatie blijkt typisch: onvoldoende productiecapaciteit, te zware cash-piek in Q1, of resultaat onder strategisch doel. Dan iteratie: aanpassen van productiecapaciteit, fasering investering, herzien verkoopprijs of kostenstructuur. Twee tot drie iteraties is normaal — bij meer dan vijf wijst dit op gebrek aan duidelijke strategische kaders (top-down te zwak). Eindafstemming met directie + RvB voor goedkeuring.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Aurelia Holding NV — cash-budget legt knelpunt bloot
> _Aurelia plant 5.000.000 EUR omzet, 500.000 EUR investering in nieuwe productielijn (Q2), gemiddelde klantbetalingstermijn 60 dagen, leveranciers 30 dagen._
>
> **🧮 Cash-budget Q1-Q2 (vereenvoudigd)**
>
> - Q1 omzet 1.000.000 → cashontvangst pas in Q2 door 60-dagen-termijn
> - Q1 productiekosten 700.000 → betaling Q1 (loon onmiddellijk) + Q2 (leverancier)
> - Q2 omzet 1.250.000 → cashontvangst Q3
> - Q2 productiekosten 850.000 → betaling Q2/Q3
> - Q2 investering 500.000 → cashuitstroom Q2
> - Q1-Q2 cumulatief: cashontvangst 1.000.000; cashuitgave loon + leverancier + investering ≈ 2.300.000
> - Cashtekort Q1-Q2 ≈ 1.300.000 EUR — als cashreserve onvoldoende is, moet een kredietlijn worden voorzien
>
> → **Resultaat**: Het masterbudget toont dat ook bij winst-perspectief het cash-knelpunt in Q1-Q2 fataal kan zijn. Actie: kredietlijn van 1.500.000 EUR vooraf onderhandelen, of investering faseren naar Q3-Q4.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Masterbudget = operationeel budget
> **Verkeerde assumptie**: Het masterbudget is gewoon het operationeel budget met wat extra.
>
> **Kernpunt**: Het masterbudget is de integratie van alle vier deelbudgetten — operationeel, investerings, financieel, cash. Veel ondernemingen stoppen bij het operationeel budget en ontdekken halverwege het jaar dat hun cashplanning niet klopt. Het masterbudget integreert expliciet de cash-impact van investeringen + financieringsbeslissingen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Pro-forma balans niet sluiten
> **Verkeerde assumptie**: De pro-forma balans hoeft niet exact te kloppen — het is toch een voorspelling.
>
> **Kernpunt**: De pro-forma balans MOET sluiten (activa = passiva). Wanneer hij niet sluit, is er een fout in de integratie. Een typisch fout: dividend uit te keren maar niet weggeschreven uit reserves; of investering geboekt in activa maar niet de financiering ervan in passiva. Sluitende balans = sanity-check op de coherentie van het hele masterbudget.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Kredietaanvraag — masterbudget als onderbouwing

_Cliente vraagt extra kredietlijn voor expansie — bank vraagt een onderbouwd masterbudget._

#### 🧭 Adviseur

##### 👣 Masterbudget opbouwen voor de bank

Banken willen drie scenario's (base, worst, best) met pro-forma jaarrekening + maandelijks cash-budget voor de looptijd van het krediet (typisch 5 jaar). Sleutel-ratio's die de bank zal opvragen: schuldgraad, current ratio, interest coverage, debt service coverage (cashflow / aflossingen + interesten). Een goed masterbudget toont expliciet dat ook in worst case de DSCR > 1,2 blijft. Onderbouw elke aanname met externe bron of historische data — banken vertrouwen niet op 'we denken dat de omzet stijgt'.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Treasury / cash-monitoring

_De accountant ondersteunt CFO/zaakvoerder bij wekelijks of maandelijks cash-monitoring via een rolling forecast._

#### 🧭 Adviseur

##### 👣 Rolling forecast maandelijks updaten

Maandelijkse update-cyclus rolling forecast (4 stappen): (1) **Verzamel actuele realisaties** — werkelijke ontvangsten + uitgaven van afgelopen periode + revisie van prognose-assumpties (heeft DSO zich gewijzigd? heeft een grote klant uitstel gevraagd?). (2) **Update rolling forecast** — oudste week weg, nieuwste week erbij; pas baseline aan op basis van werkelijke realisaties. (3) **Identificeer afwijkingen** tegenover vorige baseline + actie-vereisten (extra incasso-druk? leverancier vragen voor verlenging DPO?). (4) **Communiceer naar management** — dashboard met cash-positie per week + waarschuwing bij dreigend tekort + aanbeveling kredietlijn.

<small>🤖 claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

## Verder lezen (scope-out)

- → Budgetbeheer Σ (overkoepelend) → [[budgetbeheer]] _(moet-verwijzen)_
- ↪ Kasstroomanalyse (cash-budget-context) → [[kasstroom-analyse]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[budgetbeheer]]
### `vereist`
- [[kasstroom-analyse]] — Het cash-budget binnen het masterbudget is een prospectief kasstromenoverzicht.
