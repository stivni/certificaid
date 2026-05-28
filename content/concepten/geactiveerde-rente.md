---
title: "Geactiveerde rente"
concept_type: "principe"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.1.II.B
tags:
  - concept
  - schema-2.2
  - type-principe
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/geactiveerde-rente.json"
---

# Geactiveerde rente

_Principe_

📋 Regeling · Anchors: `1.1.II.B` · Wave: `cluster-extract-balansposten-activa-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: geactiveerde interest · capitalized borrowing costs — **Vertalingen**: en: capitalized borrowing costs · fr: intérêts intercalaires

## Definitie

📖 Art. 38 KB 29.04.2019 (uitvoering WVV) staat toe dat de financieringskosten (rente op leningen) die rechtstreeks verband houden met de productie of de constructie van een vast actief, geactiveerd worden als onderdeel van de aanschaffingswaarde — beperkt tot de periode tot het actief in gebruik wordt genomen. Het gaat om een KEUZE (niet verplicht): de onderneming kan ofwel rente direct in resultaat boeken (klasse 650 — financiële kosten) ofwel kapitaliseren op klasse 22-27. Onder IFRS (IAS 23): voor qualifying assets is activering VERPLICHT.

<small>📚 KB 29.04.2019 — art. 38 — _kb_ · Verordening (EU) 2023/1803 — IAS 23 — _wettekst_</small>

## Substantie

🔗 Stagiair moet begrijpen: rente op een 24-maandige bouwlening is een werkelijke kost — vraag is alleen WANNEER hij in het resultaat verschijnt. Als hij gekapitaliseerd wordt: hogere boekwaarde + jaarlijkse afschrijving = rente wordt gespreid over levensduur actief (bv. 33 jaar voor gebouw). Als hij direct in resultaat gaat: 'klap' in jaar bouw. Voor analyse: gekapitaliseerde rente flatteert het bedrijfsresultaat van het bouwjaar (geen kost), maar verhoogt afschrijving in latere jaren. Vermelding in toelichting bij jaarrekening is verplicht.

<small>📚 KB 29.04.2019 — art. 38 § 2 — vermelding toelichting — _kb_</small>

## Rationale

🔗 De keuze om rente te activeren reflecteert het 'matching-principle': rente tijdens constructie is een onvermijdelijke kost van het tot stand brengen van het actief — dezelfde logica als directe constructiekost (lonen bouwvakkers, materiaal). Activering verzoent het kost-resultaat met de gebruiksperiode van het actief. Be-GAAP laat dit als OPTIE; IFRS maakt het VERPLICHT voor qualifying assets (≥ substantial period of time to be ready for use — typisch > 12 maanden).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Voorwaarden activering rente  
_`regime` (subconcept)_

#### Definitie

📖 Art. 38 KB: (1) rente moet effectief gemaakt zijn op vreemd vermogen specifiek voor productie/constructie van het actief OF op algemene leningen pro rata (gewogen gemiddelde rente × geïnvesteerd bedrag in actief); (2) periode = tot ingebruikname actief; (3) keuze moet consistent zijn over boekjaren + tussen vergelijkbare activa; (4) toelichting bij jaarrekening: bedrag geactiveerde rente vermelden.

<small>📚 KB 29.04.2019 — art. 38 — _kb_</small>

### 📦 Boekhoudkundige verwerking  
_`procedure` (subconcept)_

#### Definitie

🔗 Bij keuze activering: jaarlijks tijdens constructie boeken 22 (gebouw in aanbouw — sub-rubriek 27) D / 651 (terug-geboekte gekapitaliseerde rente) C met als tegenboeking 650 (rente op leningen) blijft kost. Effect: 651 compenseert 650, netto rente in resultaat = 0; rente verschijnt op actief.

<small>📚 KB 29.04.2019 — art. 38 — _kb_ · CBN-advies 158/1 — Aanschaffingswaarde — _cbn_</small>

#### 💡 Bouw machine 24 maanden — rente 100.000 EUR geactiveerd 🔗

_Zelena Bio NV bouwt productie-installatie (1.000.000 EUR) over 24 maanden met bouwlening 5% rente._

**Boeking:**


**Boeking:**


<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Rente activeren na ingebruikname

**Verkeerde assumptie**: Rente op de bouwlening blijft activeren zolang de lening loopt.

**Kernpunt**: Art. 38 KB beperkt activering tot DE PERIODE TOT INGEBRUIKNAME. Na opening fabriek: rente direct in 650 als kost. Veelgemaakte fout bij langlopende projectfinanciering.

<small>📚 KB 29.04.2019 — art. 38 — _kb_</small>

### ⚠️ Activering niet vermeld in toelichting

**Verkeerde assumptie**: Activering is een interne keuze die niet hoeft te worden vermeld.

**Kernpunt**: Art. 38 § 2 KB: het bedrag van de geactiveerde financieringskosten moet expliciet in de toelichting bij de jaarrekening worden vermeld — voor vergelijkbaarheid en analyse-doeleinden.

<small>📚 KB 29.04.2019 — art. 38 § 2 — _kb_</small>

### ⚠️ IFRS-keuze verwarren met Be-GAAP-keuze

**Verkeerde assumptie**: Onder IFRS is activering ook optioneel.

**Kernpunt**: IAS 23 'Borrowing costs' (versie 2007): activering VERPLICHT voor qualifying assets (= activa die substantiële periode nodig hebben om gebruiksklaar te zijn — > 12 maanden typisch). Geen optie meer. Belangrijk verschil voor Be-GAAP → IFRS conversie.

<small>📚 Verordening (EU) 2023/1803 — IAS 23 § 8 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vaste activa generiek → [[vaste-activa]] _(moet-verwijzen)_
- ↪ IFRS — IAS 23 borrowing costs → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vaste-activa]]
### `alternatief_referentiestelsel`
- [[ifrs]] — IAS 23 'Borrowing costs' verplicht activering — Be-GAAP-optie.
