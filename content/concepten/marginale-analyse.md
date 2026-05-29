---
title: "Marginale analyse"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.8.III.E
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/marginale-analyse.json"
---

_Procedure_ · ook: marginal analysis · relevant cost analysis · incrementele kostenanalyse

## Definitie

De marginale analyse (ook 'relevant cost analysis' of 'incrementele analyse') beoordeelt beslissingen op basis van enkel de kosten en opbrengsten die door de beslissing veranderen — niet op basis van de gemiddelde of de full-cost. Marginale kost = de extra kost van één extra eenheid. Marginale opbrengst = de extra opbrengst. Beslissingsregel: doe de beslissing als marginale opbrengst > marginale kost (over alle relevante eenheden). Toepassingen: accept-or-reject special order, make-or-buy, doorgaan of stoppen met productlijn, voorrang geven aan welk product bij capaciteitsbeperking.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

De stagiair moet leren onderscheid maken tussen drie soorten kosten: relevante kosten (veranderen door de beslissing — alleen die tellen), sunk costs (al gemaakt — irrelevant) en opportunity costs (gemiste alternatieve opbrengst — wél relevant, ook al staan ze niet in de boekhouding). Bij make-or-buy: alleen de vermijdbare vaste kosten + variabele kosten van 'make' tellen versus de inkoopprijs van 'buy' — een fabriekshuur die toch doorloopt is irrelevant. Bij special-order-aanvaarding: alleen de variabele kosten + opportunity cost van capaciteit tellen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Marginale analyse is decision-driven kostenboekhouding. Veel verkeerde beslissingen ontstaan omdat managers redeneren op basis van gemiddelde kosten of full-cost — daardoor accepteren ze geen orders die contributiemarge opleveren, of houden ze verlies-makende productlijnen aan op basis van 'doorlopende vaste kosten'. De marginale analyse dwingt het denken naar 'wat verandert hier door deze beslissing?', wat bijna altijd een ander resultaat geeft dan 'wat is het gemiddelde?'.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Korte-termijn-beslissingen waarbij de capaciteit en de organisatie-structuur vaststaan: accept-or-reject special order, make-or-buy bij vrije capaciteit, productlijn-keep-or-drop, optimale product-mix bij bottleneck, prijsverlaging om volume aan te trekken.

**🚫 Niet voor**
- 🔗 Strategische lange-termijn-beslissingen waar de vaste kostenbasis zelf de variabele is (nieuwe fabriek, nieuwe vestiging, fundamentele technologie-keuze). Daar moet je naar de volledige cashflow-impact kijken via NPV-analyse (investeringsevaluatie), niet alleen naar marginale kosten op korte termijn.

## Bouwstenen

### 📜 Relevant cost test — drie criteria

Een kost is 'relevant' (= mee te tellen in marginale analyse) als ze cumulatief aan drie criteria voldoet: (1) ze is toekomstig (geen sunk cost); (2) ze verschilt tussen de alternatieven (een kost die in beide scenario's identiek is, valt weg in het verschil); (3) ze is een uitgaande cashflow of een opportunity cost (boekhoudkundige allocaties van overhead die geen werkelijke cashbeweging veroorzaken zijn meestal niet-relevant). Pas-toe-vraag: 'verandert deze kost door deze beslissing?'. Zo nee: weglaten.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Opportunity cost — gemiste alternatieve waarde

Opportunity cost = de waarde van het beste niet-gekozen alternatief. Belangrijk omdat ze niet in de boekhouding staat maar wel relevant is voor de beslissing. Voorbeeld: een productiehal die ofwel voor product A ofwel voor product B kan gebruikt worden — als A gekozen wordt, is de opportunity cost = gederfde marge op B. Bij volledige capaciteit en aanvraag voor extra order: opportunity cost = gederfde marge op het normaal-prijs verkocht product dat moet wijken.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Make-or-buy beslissing

Bij make-or-buy: vergelijk de relevante kost van zelf maken (variabele productiekost + vermijdbare vaste kosten + opportunity cost van vrijgekomen capaciteit) versus de inkoopprijs bij externe leverancier. Niet-vermijdbare vaste kosten (huur fabriek die doorloopt, afschrijving al-aangekochte machine) zijn irrelevant — ze blijven in beide scenario's. Maak indien relevante kost-zelf < inkoopprijs; koop indien relevante kost-zelf > inkoopprijs. Vergeet niet kwalitatieve factoren: betrouwbaarheid leverancier, intellectueel eigendom, kerncompetentie.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Accept-or-reject special order

Bij een eenmalige aanvraag onder de normale prijs: aanvaarden indien aangeboden prijs > variabele kost per eenheid + eventuele opportunity cost van capaciteitsbeslag. Bij vrije capaciteit: opportunity cost = 0; elke prijs > variabele kost levert positieve contributiemarge. Bij volle capaciteit: opportunity cost = gederfde CM van het normaal-prijs product; aangeboden prijs moet hoger zijn dan variabele kost + gederfde CM. Belangrijk: special orders mogen geen olievlek worden — als de cliente regelmatig op special-order-prijzen verkoopt, ondermijnt ze haar eigen prijszetting voor reguliere verkoop.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Productlijn keep-or-drop

Bij beslissing om productlijn te stoppen: een productlijn met negatief volledig resultaat is niet noodzakelijk een drop-kandidaat. Drop alleen als de contributiemarge negatief is (verlies op variabele kost) OF als de vermijdbare vaste kosten + opportunity cost van vrijgekomen capaciteit groter zijn dan de CM van de productlijn. Niet-vermijdbare overhead-allocaties die de productlijn 'krijgt toegewezen' moeten weggehaald worden uit de analyse — ze lopen toch door.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Bottleneck — optimale product-mix

Bij capaciteitsbeperking (machine-uren, arbeidsuren, schaarse grondstof): rangschik producten naar contributiemarge per eenheid bottleneck (niet per eenheid product). Het product met de hoogste CM per bottleneck-eenheid eerst tot bottleneck-capaciteit op is. Voorbeeld: tafel met CM 250 EUR en 5 machine-uren versus stoel met CM 60 EUR en 1 machine-uur — stoel heeft CM/uur = 60 (hoger dan tafel = 50). Met beperkte machine-uren: stoelen eerst.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Zelena Bio NV — special order met vrije capaciteit
> _Zelena Bio normale verkoopprijs tafel: 500 EUR. Variabele kost: 250 EUR. Vaste kosten/maand: 100.000 EUR. Een hotelketen vraagt 50 tafels voor 350 EUR/stuk. Zelena heeft vrije capaciteit (geen verdringing normale verkoop)._
>
> **Berekening:**
>
> - Relevante kost = alleen variabele kost = 50 × 250 = 12.500 EUR (vaste kosten lopen toch door)
> - Opportunity cost = 0 (vrije capaciteit)
> - Marginale opbrengst = 50 × 350 = 17.500 EUR
> - Marginale winst = 17.500 − 12.500 = +5.000 EUR (= 100 EUR contributiemarge × 50)
>
> → **Resultaat**: Aanvaarden — de order genereert 5.000 EUR extra winst zonder verdringing. Op basis van full cost (450 EUR/tafel) had het lijken op een verlies van 100 EUR/tafel — een misleidende redenering die de order onterecht zou weigeren.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Make-or-buy — Aurelia Holding NV en sub-component
> _Aurelia maakt zelf een sub-component voor 80 EUR/stuk (50 variabel + 30 vast/stuk). Een leverancier biedt 70 EUR/stuk. Volume: 1.000 stuks/jaar. Bij outsourcing zou 20 EUR/stuk vaste kosten kunnen vermeden worden (deel van afschrijving + onderhoud op specifieke machine die verkocht kan worden); 10 EUR/stuk blijft hoe dan ook (algemene fabriekshuur)._
>
> **Berekening:**
>
> - Relevante kost zelf maken = variabele 50 + vermijdbare vast 20 = 70 EUR/stuk × 1.000 = 70.000 EUR
> - Relevante kost inkopen = 70 EUR/stuk × 1.000 = 70.000 EUR
> - Identiek — break-even op basis van directe vergelijking
> - Kwalitatieve factoren bepalen: leveringszekerheid, kerncompetentie, IP, productieflexibiliteit
> - Niet-vermijdbare vaste kost (10 EUR/stuk × 1.000 = 10.000 EUR) blijft in beide scenario's en is irrelevant
>
> → **Resultaat**: Op puur cijfer-basis indifferent. De keuze valt op kwalitatieve factoren: blijft de leverancier betrouwbaar? Wat met onverwachte vraagpieken? Wordt de capaciteit op een nuttige manier hergebruikt? Indien geen waardevolle alternatieve aanwending: zelf blijven maken.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Vaste overhead-allocatie als relevant beschouwen
> **Verkeerde assumptie**: Een productlijn 'kost' wat de full-cost-allocatie zegt — inclusief vaste overhead.
>
> **Kernpunt**: Niet-vermijdbare vaste overhead is irrelevant voor een keep-or-drop, make-or-buy of special-order-beslissing. Die kosten lopen toch door, ongeacht het besluit. Alleen vermijdbare kosten (die werkelijk wegvallen bij stop) tellen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Sunk cost gebruiken als argument om door te gaan
> **Verkeerde assumptie**: 'We hebben al zo veel geïnvesteerd, we moeten doorzetten om het terug te verdienen.'
>
> **Kernpunt**: Sunk cost is irrelevant. De vraag is alleen: 'wat brengen de toekomstige opbrengsten op versus de toekomstige kosten?' Reeds gemaakte uitgaven niet meenemen — ze veranderen niet door de huidige beslissing.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Special-order-prijs als reguliere prijs
> **Verkeerde assumptie**: Wat goed werkt voor een eenmalige order kan ook structureel.
>
> **Kernpunt**: Special-order-prijzen werken alleen bij vrije capaciteit + eenmalig + onzichtbaarheid naar reguliere markt. Structureel onder full cost verkopen leidt over de cyclus tot verlies en ondergraaft de markt voor reguliere verkoop. Vuistregel: max 10-20% van capaciteit als special-order.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Decision support — beslissingsadvies

_De gecertificeerd accountant ondersteunt management-beslissingen door relevant-cost-analyses op te zetten._

#### 🧭 Adviseur

##### 👣 Alternatieven scherp formuleren

Marginale analyse vergelijkt alternatieven — niet één optie tegen 'niets'. Eerst de alternatieven scherp formuleren: 'maken in eigen fabriek' versus 'inkopen bij X' versus 'inkopen bij Y'. Dan voor elk alternatief: welke kosten veranderen? Welke opportunity costs? Welke cashflow-impact? Pas dan vergelijken. Veel beslissingen lopen mis omdat het alternatief niet expliciet gedefinieerd is.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Direct costing (variabele-kost-basis) → [[direct-costing]] _(moet-verwijzen)_
- ↪ Investeringsevaluatie (make-or-buy + NPV-context) → [[investeringsevaluatie]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[analytische-boekhouding]]
### `vereist`
- [[direct-costing]] — Marginale analyse bouwt op de variabele-kosten-redenering uit direct costing.
