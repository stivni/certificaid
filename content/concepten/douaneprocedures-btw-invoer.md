---
title: "Douaneprocedures BTW-invoer"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.IX
  - 2.4.X
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/douaneprocedures-btw-invoer.json"
---

_Procedure_ · ook: invoer-BTW · BTW bij import uit derde landen · ET 14.000

## Definitie

Bij invoer van goederen uit derde landen (= buiten EU) in België is BTW verschuldigd. Het 'belastbaar feit' voor invoer-BTW is het in het vrije verkeer brengen van de goederen op het Belgische douanegebied (WBTW art. 23-25). De BTW wordt geheven samen met eventuele invoerrechten via het Enig Document (DAU — Document Administratif Unique, in EU-jargon SAD). De importeur kan kiezen tussen twee betalingsregimes: (1) onmiddellijke betaling bij de douane (KB nr. 7 art. 4 — default); (2) verlegging van de betaling naar de BTW-aangifte mits vergunning ET 14.000 (KB nr. 7 art. 5 §2 — cashflow-voordeel).

<small>📖 WBTW — art. 23-25 — _wettekst_ · WBTW — art. 51 §2, 1° — _wettekst_ · KB nr. 7 — art. 4-5 — _kb_</small>

## Substantie

De maatstaf van heffing voor invoer-BTW is de DOUANEWAARDE (zie record douanewaarde) verhoogd met de invoerrechten, accijnzen en bijkomende kosten tot de eerste bestemming in België (vervoer, verzekering, commissie). Op dit totaal komt het Belgische BTW-tarief (typisch 21 %, soms 6 % voor specifieke goederen zoals boeken, geneesmiddelen). De BTW is recupereerbaar voor BTW-belastingplichtige importeur via rooster 87 (IC- en derde-landen-aankopen) + 59 (aftrek), mits verlegging-vergunning of effectieve betaling.

<small>📖 WBTW — art. 34 — _wettekst_ · KB nr. 7 — art. 1-4 — _kb_</small>

## Rationale

Invoer-BTW realiseert het 'bestemmingsprincipe': BTW wordt geheven waar de consumptie plaatsvindt. Een Chinese fabrikant betaalt geen Belgische BTW bij export naar België — die wordt pas bij invoer in de EU geheven. Het verleggingsregime (ET 14.000) elimineert de cashflow-druk voor importeurs (ze hoeven geen BTW vooraf te storten aan de douane en dan terug te vragen via de aangifte) — een vereiste voor het concurrentievermogen van Belgische logistiek-knooppunten zoals de haven van Antwerpen.

<small>🔗 KB nr. 7 — art. 5 §2 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 23-25 + KB nr. 7 + EU Douanewetboek (UCC, Vo. 952/2013)

Sinds 2016 toepassing UCC. ET 14.000-vergunning sinds 2017 sterk vereenvoudigd (afschaffing borg-vereiste voor gevestigde belastingplichtigen).

## Sub-concepten

### 📦 Enig Document (DAU) — invoeraangifte

#### Definitie

Het Enig Document is het EU-uniforme aangifteformulier voor douaneoperaties — invoer, uitvoer, doorvoer. Sinds 2020 elektronisch via PLDA (België) of het Customs Decision-systeem. Bevat: identificatie importeur, beschrijving goederen (HS-code), oorsprong, douanewaarde, douaneregime, verschuldigde rechten + BTW. Het Enig Document is het officiële BEWIJSSTUK van invoer en gemaakte aangifte — zonder DAU geen BTW-aftrek mogelijk.

<small>🔗 KB nr. 7 — art. 4 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 📦 Vergunning ET 14.000 — verlegging invoer-BTW

#### Definitie

Met vergunning ET 14.000 (KB nr. 7 art. 5 §2) wordt de BTW bij invoer NIET aan de douane betaald, maar verlegd naar de eerstvolgende BTW-aangifte van de importeur: rooster 87 (IC- en niet-EU-aankopen) als maatstaf, rooster 57 (BTW verschuldigd) en rooster 59 (BTW aftrekbaar) gelijktijdig → cashflow-neutraal (nul effect bij volledig recht op aftrek). Voorwaarden: belastingplichtige met periodieke aangifte; goede compliance-staat; sinds 2017 geen borg meer vereist voor in België gevestigde belastingplichtigen.

<small>📖 WBTW — art. 51 §2, 1° — _wettekst_ · KB nr. 7 — art. 5 §2 — _kb_</small>

### 📦 Douanevertegenwoordiger — direct vs indirect

#### Definitie

Een douaneagent (expediteur) kan in twee hoedanigheden optreden (UCC art. 18): (1) DIRECTE vertegenwoordiging — in naam EN voor rekening van de aangever (importeur); aangever blijft enige schuldenaar van rechten en BTW; (2) INDIRECTE vertegenwoordiging — in eigen naam maar voor rekening van de importeur; vertegenwoordiger wordt hoofdelijk schuldenaar samen met importeur. Praktisch: indirecte vertegenwoordiging is vaker bij niet-EU-importeurs zonder Belgische BTW-identificatie; directe bij Belgische BTW-belastingplichtigen.

<small>📖 UCC — Verordening (EU) 952/2013 — art. 18 — _richtlijn_</small>

## Bouwstenen

### 🧮 Maatstaf van heffing invoer-BTW

Maatstaf = douanewaarde + invoerrechten + accijnzen + bijkomende kosten (vervoer, verzekering, commissie tot eerste bestemming in België). Voorbeeld: container Chinese kleding, douanewaarde 50.000 EUR + invoerrecht 12 % = 6.000 EUR + vervoer-naar-Brussel 2.000 EUR → maatstaf 58.000 EUR; BTW 21 % = 12.180 EUR.

<small>📖 WBTW — art. 34 — _wettekst_</small>

### ↪️ Vrijstellingen bij invoer

Belangrijkste vrijstellingen invoer-BTW: (1) kleine zendingen met geringe waarde (drempel ≤ 22 EUR sinds 2021 afgeschaft — nu vanaf 1 EUR BTW); (2) tijdelijke invoer met vrijstelling van invoerrechten (WBTW art. 42 §3); (3) goederen onder douane-entrepot of doorvoerregeling (BTW pas bij vrijgeven uit entrepot); (4) monsters van handelsstalen (mits voorwaarden); (5) terugkomende goederen (originaire EU-export die terugkomt); (6) diplomatieke / consulaire importen.

<small>🔗 WBTW — art. 40 + art. 42 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 👣 Betalingsmodaliteiten via PLDA

Op het elektronische PLDA-systeem worden invoeraangiftes ingediend. Op de aangifte komt één van de vermeldingen: (a) 'betaling' — BTW onmiddellijk te storten via PLDA-rekening; (b) 'uitstel van betaling' — verlegging naar BTW-aangifte (vergunning ET 14.000); (c) 'vrijstelling' — wettelijke vrijstellingsgrond aanduiden. Elke aangifte krijgt een DAU-referentie die in de boekhouding van de importeur als bewijsstuk dient.

<small>📖 KB nr. 7 — art. 4 — _kb_</small>

## Voorbeelden

> [!example]- Invoer container Chinese kleding — met ET 14.000
> _Aurelia Holding BVBA (BTW-belastingplichtige, ET 14.000-vergunning, maandaangifte) importeert in maart 2026 een container kleding uit China. Douanewaarde: 50.000 EUR. Invoerrecht 12 % (textiel). Vervoer Antwerpen → magazijn 2.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — Invoeraangifte (DAU) via PLDA: indienen door douane-expediteur (directe vertegenwoordiging)
> - Stap 2 — Invoerrechten: 50.000 × 12 % = 6.000 EUR — onmiddellijk te betalen aan de douane
> - Stap 3 — Maatstaf invoer-BTW: 50.000 + 6.000 + 2.000 = 58.000 EUR
> - Stap 4 — BTW 21 %: 12.180 EUR — VERLEGD (ET 14.000) → niet aan douane, wel in BTW-aangifte
> - Stap 5 — BTW-aangifte maart 2026: rooster 87 (aankopen 21 %): 58.000; rooster 57 (BTW verschuldigd verlegging): 12.180; rooster 59 (BTW aftrekbaar): 12.180 → netto-effect = nul (cashflow-neutraal)
> - Stap 6 — Boeking: D 60 'Aankopen handelsgoederen' 58.000 / C 44 'Te betalen China-leverancier' 50.000 + C 451 'Te betalen invoerrechten' 6.000 + C 489 'Diverse schulden vervoer' 2.000. BTW-verlegging: D 411 12.180 / C 451 12.180.
>
> → **Resultaat**: Zonder ET 14.000-vergunning zou Aurelia 12.180 EUR cash moeten voorschieten aan de douane en pas in de aangifte recupereren — cashflow-vertraging van enkele maanden. Met vergunning: nul vooruitbetaling.
>
> <small>🔗 WBTW — art. 34 + art. 51 §2 — _wettekst_ · KB nr. 7 — art. 4-5 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- ET 14.000-verlegging vergeten in de BTW-aangifte
> **Verkeerde assumptie**: 'Onder ET 14.000 is er geen BTW meer, dus niets te doen in de aangifte.'
>
> **Kernpunt**: Verlegging betekent dat de BTW VERSCHOVEN is naar de aangifte, NIET dat er geen BTW is. Vergeten te boeken in rooster 57 (verschuldigde verlegging) → boete + ambtshalve aanslag. Software moet automatisch DAU-data uit PLDA inlezen in de boekhouding. Een 'verlegging vergeten' is een typische bevinding bij BTW-controles van importeurs.
>
> <small>📖 WBTW — art. 51 §2 — _wettekst_</small>

> [!warning]- DAU als handelsfactuur behandelen
> **Verkeerde assumptie**: 'Ik heb de factuur van de Chinese leverancier — dat volstaat voor BTW-aftrek.'
>
> **Kernpunt**: Bij invoer is het BEWIJSSTUK voor BTW-aftrek het DAU (Enig Document), NIET de handelsfactuur van de buitenlandse leverancier. Het DAU is het document waarop het BTW-bedrag van de invoer vermeld staat én die de Belgische douane bezit. Bewaartermijn: 10 jaar (BTW + douane).
>
> <small>🔗 KB nr. 7 — art. 4 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

> [!warning]- Indirecte vertegenwoordiging gelijkstellen met directe
> **Verkeerde assumptie**: 'Een douaneagent verzorgt de aangifte — voor mij is alles gelijk of hij direct of indirect handelt.'
>
> **Kernpunt**: Bij indirecte vertegenwoordiging wordt de agent HOOFDELIJK schuldenaar van rechten en BTW. Bij solvabiliteits-zorgen van de importeur kan dit zware risico's opleveren voor de agent — vandaar dat indirecte vertegenwoordiging meestal duurder is. Importeur en agent moeten contractueel scherp afspreken welk type vertegenwoordiging.
>
> <small>📖 UCC — Verordening (EU) 952/2013 — art. 18 + art. 77 — _richtlijn_</small>

## Accountant-perspectieven

### Kantoor begeleidt importeur

_De accountant bij een Belgisch BVBA/NV met substantiële invoer uit derde landen._

#### 🧭 Adviseur

##### 👣 Vergunning ET 14.000 aanvragen

Voor cliënten met substantiële invoer (drempel: meerdere invoeren per jaar of grote volumes): ET 14.000-vergunning aanvragen via FOD Financiën — formulier 14.000 + bewijs van goede BTW-discipline (geen openstaande dwangbevelen). Cashflow-voordeel = substantieel (geen 21 % vooruitbetalen aan douane). Sinds 2017 geen borg meer vereist voor BE-gevestigden.

<small>📖 KB nr. 7 — art. 5 §2 — _kb_</small>

#### 📒 Boekhouder

##### 👣 Verwerking DAU's in boekhouding

Per maandelijkse aangifte: alle DAU's verzamelen + checken op vermelding 'uitstel' of 'betaling'. Per DAU boeken: aankoopprijs (klasse 6) + invoerrechten (klasse 6 of als kostprijs activa); bij ET 14.000: BTW-verlegging in roosters 87 + 57 + 59 (cashflow-neutraal); bij directe betaling: BTW in rooster 81-83 + 59 (na betaling aan douane). DAU-referenties bewaren voor 10 jaar.

<small>🔗 WBTW — art. 51 §2 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Douanewaarde — basis voor invoerrechten + BTW → [[douanewaarde]] _(moet-verwijzen)_
- → Accijnzen bij invoer accijnsgoederen → [[accijnzen-basis]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[douanewaarde]] — Maatstaf invoer-BTW = douanewaarde + bijkomende kosten.
### `beinvloed_door`
- [[accijnzen-basis]] — Bij invoer van accijnsgoederen worden zowel BTW als accijnzen via het DAU geheven.
