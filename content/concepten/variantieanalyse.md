---
title: "Variantieanalyse"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.8.VI
  - 1.8.VI.C
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/variantieanalyse.json"
---

# Variantieanalyse

_Procedure_

🏛️ Kader · Anchors: `1.8.VI` · `1.8.VI.C` · Wave: `cluster-extract-management-accounting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: variance analysis · verschillen-boekhouding · afwijkingsanalyse — **Vertalingen**: fr: analyse des écarts

## Definitie

🔗 Variantieanalyse (variance analysis) is de gestructureerde uiteenrafeling van de afwijking tussen werkelijk gerealiseerde cijfers en een referentienorm — een budget of standaardkost. De totale variantie wordt opgesplitst naar oorzaak (prijs versus hoeveelheid, volume versus efficiency, markt versus operationeel) en naar verantwoordelijkheid (inkoop, productie, verkoop, ...). Doel: management-by-exception mogelijk maken — focus op materiële afwijkingen en verklaren waarom ze zijn ontstaan.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Variantieanalyse maakt twee soorten verschillen zichtbaar: prijs-effect (kostprijs of verkoopprijs per eenheid wijkt af van norm) en hoeveelheids-effect (verbruik of volume per eenheid wijkt af van norm). Door beide te isoleren wordt de verantwoordelijkheid duidelijk: een prijsstijging op grondstof is meestal niet aan productie te wijten — wel een hoger verbruik. Voor de gecertificeerd accountant is dit een controle-instrument: ongunstige varianties wijzen op procesinefficiëntie, prijsdruk of marktwijzigingen die actie vereisen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Zonder variantieanalyse blijft het verschil tussen 'budget' en 'werkelijk' een ondoorzichtige globale afwijking die niet stuurt — een budget-overschrijding van 50.000 EUR zegt niet of de organisatie meer verbruikt heeft, meer betaald heeft, of meer verkocht en daardoor logisch meer ingekocht. Door op te splitsen naar prijs × hoeveelheid wordt het verschil interpreteerbaar en kan de directie gericht ingrijpen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Periodieke (maandelijkse, kwartaal) management-rapportering · efficiency-opvolging productie · budget-control · post-mortem-analyse na projecten · oorzakelijk afwijkings-onderzoek bij forecasting-fouten.

## Bouwstenen

### 🧮 Twee basisformules — prijs × hoeveelheid  
_`formule`_

🔗 Voor elke kostencategorie (grondstof, arbeid, overhead) wordt de totale variantie opgesplitst in een prijsvariantie en een hoeveelheidsvariantie. Prijsvariantie (PV) = werkelijke hoeveelheid × (werkelijke prijs − standaardprijs). Hoeveelheidsvariantie (HV) = standaardprijs × (werkelijke hoeveelheid − standaardhoeveelheid). Som = totale variantie = werkelijke kost − standaardkost. Conventie: positieve variantie = ongunstig (werkelijk > standaard); negatieve = gunstig. De volgorde van decompositie heeft impact op de exacte cijfers — meest gebruikte conventie is PV op werkelijke hoeveelheid, HV op standaardprijs.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Soorten varianties — overzicht  
_`begrip`_

🔗 Per kostencategorie: grondstof-prijsvariantie + grondstof-hoeveelheidsvariantie (verbruik); arbeids-loontariefvariantie + arbeids-efficiencyvariantie (uren); variabele-overhead-spendingvariantie + efficiencyvariantie; vaste-overhead-budgetvariantie + volumevariantie (capaciteitsbenutting). Aan opbrengstkant: verkoop-prijsvariantie + verkoop-volumevariantie + verkoop-mixvariantie (welke producten verkocht). De optelsom van alle varianties verklaart het verschil tussen 'budgetwinst' en 'werkelijke winst'.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Verantwoordelijkheid per variantie  
_`regel`_

🔗 Prijsvariantie grondstof → inkoop (kan keuze van leverancier of timing van aankoop beïnvloeden). Hoeveelheidsvariantie grondstof → productie (verbruik per eenheid). Loontariefvariantie → personeel/HR. Efficiencyvariantie arbeid → productie. Volumevariantie vaste OH → verkoop (volume) + algemene directie (capaciteitsbeslissing). Verkoopprijsvariantie → commercieel. Een goede variantierapport benoemt expliciet de verantwoordelijke; alleen dan stuurt het management-actie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Management-by-exception — materialiteitsdrempel  
_`vuistregel`_

🔗 Niet elke variantie verdient management-aandacht. Gangbare drempels: absoluut bedrag (bv. > 5.000 EUR) en relatief percentage (bv. > 10% van de standaard). Onder de drempel: 'binnen norm', geen verdere actie. Boven de drempel: oorzaak-analyse + corrigerende actie. Het systeem moet zo gekalibreerd zijn dat 5-10% van de varianties boven de drempel uitkomt — anders is de drempel te laag (te veel ruis) of te hoog (significante problemen worden gemist).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Zelena Bio NV — grondstof-variantie tafel-productie 🔗

_Standaard: 2 kg eikenhout × 50 EUR/kg = 100 EUR per tafel. Maart: 100 tafels geproduceerd. Werkelijk: 220 kg gekocht aan 52 EUR/kg = 11.440 EUR._

**Berekening:**
- Standaardkost = 100 tafels × 100 = 10.000 EUR
- Werkelijke kost = 11.440 EUR
- Totale variantie = 11.440 − 10.000 = +1.440 EUR ongunstig
- Prijsvariantie = 220 kg × (52 − 50) = +440 EUR ongunstig (verantwoordelijke: inkoop — kunnen ze de hogere prijs vermijden?)
- Hoeveelheidsvariantie = 50 × (220 − 200) = +1.000 EUR ongunstig (verantwoordelijke: productie — waarom 220 kg in plaats van 200 kg?)
- Controle: 440 + 1.000 = 1.440 ✓

→ **Resultaat**: Productie heeft een groter probleem dan inkoop. Mogelijke oorzaken hoger verbruik: meer uitval, foute zaagmaten, kwaliteitsprobleem hout. Inkoop heeft een prijsstijging van 4% gerealiseerd — eventueel marktbeweging onderzoeken.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Variantie = schuldvraag

**Verkeerde assumptie**: Een ongunstige variantie wijst altijd een schuldige aan.

**Kernpunt**: Varianties zijn diagnostische signalen, geen veroordelingen. Een hogere prijsvariantie kan een legitieme marktbeweging zijn waar inkoop machteloos tegen is. Een ongunstige efficiencyvariantie kan veroorzaakt zijn door een verkeerde standaard (te ambitieus) of door externe omstandigheden (slechtere grondstof-kwaliteit). De variantie opent het gesprek; ze beantwoordt het niet.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Alleen ongunstige varianties onderzoeken

**Verkeerde assumptie**: Gunstige varianties zijn altijd goed nieuws — geen actie nodig.

**Kernpunt**: Onverwacht gunstige varianties zijn even verdacht als ongunstige. Een gunstige prijsvariantie kan wijzen op kwaliteitsdaling van grondstof; een gunstige efficiencyvariantie kan wijzen op verkorte productiestappen die de kwaliteit in gevaar brengen. Onderzoek beide kanten van de drempel.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Decompositie van varianties — overzicht per kostencategorie.

## Accountant-perspectieven

### Controller-rol — periodieke variantierapport

_De gecertificeerd accountant in een controller-rol bouwt het maandelijks variantierapport._

#### 📒 Boekhouder

##### 👣 Variantierapport opmaken  
_`stap`_

🔗 Maandelijks rapport bevat: (1) executive summary met de top-3 materiële varianties; (2) decompositie per kostencategorie met prijs- en hoeveelheidsvariantie; (3) korte schriftelijke verklaring per materiële variantie (van de verantwoordelijke afdeling); (4) corrigerende acties voor de volgende maand. Vorm: bondig (max 2-3 pagina's) en altijd vergelijkbaar met vorige maanden (trend-zichtbaarheid).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Standaardkostenmethode (input-normen) → [[standaardkostenmethode]] _(moet-verwijzen)_
- → Budgetbeheer Σ (parent) → [[budgetbeheer]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[budgetbeheer]]
### `vereist`
- [[standaardkostenmethode]] — Zonder voorafbepaalde standaarden of budget is variantieanalyse onmogelijk — er moet een norm zijn om tegen te vergelijken.
