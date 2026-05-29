---
title: "Vaste activa"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.B
  - 1.1.II.A
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/vaste-activa.json"
---

_Balanspost_ · ook: immobilisaties · non-current assets

## Definitie

Vaste activa zijn duurzaam aangehouden bezittingen — bedoeld om de bedrijfsactiviteit te ondersteunen op langere termijn (> 1 jaar), niet om te worden verkocht in het kader van de gewone exploitatie. In het Belgische MAR (KB 21.10.2018) zitten ze in klasse 2: 20 oprichtingskosten · 21 immateriële vaste activa · 22 terreinen en gebouwen · 23 installaties, machines en uitrusting · 24 meubilair en rollend materieel · 25 leasing en soortgelijke rechten · 26 overige materiële vaste activa · 27 vaste activa in aanbouw en vooruitbetalingen · 28 financiële vaste activa. Subrekeningen eindigen verplicht op 0 (aanschaffingswaarde), 8 (geboekte meerwaarden), 9 (geboekte afschrijvingen + waardeverminderingen — negatief teken).

<small>📖 MAR-KB 21.10.2018 — Bijlage 1 — Klasse 2 — _kb_</small>

## Substantie

Drie groepen — drie waarderings-logica's: (1) immateriële vaste activa (klasse 21) = niet-fysiek + identificeerbaar + lange levensduur (software, licenties, ontwikkelingskosten, goodwill). (2) Materiële vaste activa (klasse 22-27) = fysiek, productief gebruikt (gebouwen, machines, voertuigen). (3) Financiële vaste activa (klasse 28) = duurzame deelnemingen + LT-vorderingen verbonden partijen. Boekhoudkundige cyclus voor elk: aanschaffing → eventueel kapitalisatie bijkomende kosten en geactiveerde rente → systematische afschrijving over levensduur → eventueel bijzondere waardevermindering of herwaardering → desinvestering met meer- of minderwaarde. Examen-aandachtspunten: keuze afschrijvingsmethode (lineair vs degressief — CBN 2010/15), waardering bij inbreng, behandeling kleine investeringen (< 1.000 EUR vrijstelling fiscaal).

<small>🔗 CBN-advies 2010/15 — Afschrijvingsmethoden — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De categorie 'vast' vs 'vlottend' (klasse 3-5) is geen formele indeling maar een functionele: vlottende activa worden binnen één cyclus van de bedrijfsuitoefening omgezet in cash; vaste activa blijven langer. Dit drijft drie verschillende analytische logica's: liquiditeit (op vlottende activa), solvabiliteit (op vaste activa als 'duurzame inzet'), en jaarrekening-analyse (verhouding vaste vs vlottend = financiële structuur). De drie sub-categorieën (IMA/MVA/FVA) hebben verschillende risico-profielen — vandaar aparte rubrieken: IMA meer schatting + impairment-risico, MVA standaard-afschrijving, FVA waarderings-risico (deelneming).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 20 — Oprichtingskosten

#### Definitie

Oprichtingskosten zijn de kosten verbonden aan oprichting, uitbreiding of herstructurering van de vennootschap, die niet meteen ten laste van het lopend boekjaar worden gebracht. Sub-rubrieken: 200 kosten van oprichting · 201 kosten bij uitgifte van leningen + disagio · 202 overige oprichtingskosten · 204 herstructureringskosten. Afschrijving: art. 3:42 KB WVV verplicht binnen max. 5 jaar (lineair of versnelder). Speciale categorie omdat het geen actief is in de strikte zin — louter geactiveerde kost.

<small>📖 CBN-advies 2010/15 — Oprichtingskosten — afschrijving — _cbn_ · KB 29.04.2019 — art. 3:42 — _kb_</small>

### 📦 21 — Immateriële vaste activa

#### Definitie

Sub-rubrieken: 210 kosten van onderzoek en ontwikkeling · 211 concessies, octrooien, licenties, knowhow, merken en soortgelijke rechten · 212 goodwill · 213 vooruitbetalingen. Identificatie-criterium (CBN 2012/13): identificeerbaar, gecontroleerd door onderneming, toekomstig economisch voordeel. Onderzoekskosten worden in principe niet geactiveerd (klasse 6); ontwikkelingskosten kunnen wél onder strikte voorwaarden (CBN 2016/27).

<small>📖 CBN-advies 2012/13 — IMA — herkenningscriteria — _cbn_ · CBN-advies 2016/27 — Onderzoek vs ontwikkeling — _cbn_</small>

### 📦 22-27 — Materiële vaste activa

#### Definitie

22 terreinen en gebouwen · 23 installaties, machines en uitrusting · 24 meubilair en rollend materieel · 25 leasing en soortgelijke rechten · 26 overige MVA · 27 vaste activa in aanbouw en vooruitbetalingen. Per rubriek 3 hoofd-sub: ...0 aanschaffingswaarde · ...8 herwaarderingsmeerwaarden · ...9 geboekte afschrijvingen (-). Aanschaffingswaarde = aankoopprijs + bijkomende kosten (transport, installatie, niet-aftrekbare btw, registratierechten) + eventueel geactiveerde rente (art. 38 KB).

<small>📖 MAR-KB — Bijlage 1 klasse 22-27 — _kb_ · KB 29.04.2019 — art. 36-40 (aanschaffingswaarde) — _kb_</small>

> [!example]- Aankoop machine 10.000 EUR + 500 transport + 100 installatie
> **📒 Boeking aanschaffing (aanschaffingswaarde = 10.600 EUR)**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 2300 — Installaties, machines en uitrusting — aanschaffingswaarde | 10.600 |  |
> | 411 — Terug te vorderen btw | 2.226 |  |
> | 440 — Leveranciers |  | 12.826 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 28 — Financiële vaste activa

#### Definitie

Sub-rubrieken: 280-281 deelnemingen in verbonden ondernemingen + ondernemingen met deelnemingsverhouding · 282 andere deelnemingen · 283-284 LT-vorderingen op verbonden ondernemingen · 285-288 borgtochten + overige. Duurzaam karakter onderscheidt FVA van speculatieve geldbeleggingen (klasse 50-53). Waardering: kostprijs minus eventuele waardevermindering bij duurzame waardedaling.

<small>📖 MAR-KB — Bijlage 1 klasse 28 — _kb_</small>

### 📦 Afschrijvings-cascade

#### Definitie

Per jaar: (1) basis = aanschaffingswaarde (+ geactiveerde rente, herwaardering); (2) levensduur kiezen volgens verwachte gebruiksduur (machine 10 j, kantoorapparatuur 4-5 j, gebouw 20-33 j); (3) methode kiezen (CBN 2010/15): lineair = standaard, degressief (max 2× lineair en niet onder lineair eindjaren) toegelaten voor MVA niet voor gebouwen; (4) boeking: 630 afschrijvingen (debet, kost) tegenover 22x9 / 23x9 / etc (credit, vermindering actief).

<small>📖 CBN-advies 2010/15 — Afschrijvingsmethoden — _cbn_ · KB 29.04.2019 — art. 3:42 — _kb_</small>

## Valkuilen

> [!warning]- Bijkomende kosten niet activeren
> **Verkeerde assumptie**: Aanschaffingswaarde = aankoopprijs zonder meer.
>
> **Kernpunt**: Aanschaffingswaarde = aankoopprijs + alle bijkomende kosten om actief gebruiksklaar te krijgen: transport, installatie, niet-aftrekbare btw, registratierechten, douane. Voor zelf gebouwde activa: productiekost incl. directe lonen + grondstoffen + (optioneel) deel indirecte productiekosten + geactiveerde rente (art. 38 KB).
>
> <small>📖 KB 29.04.2019 — art. 36-39 — _kb_</small>

> [!warning]- Klasse 25 leasing-verwarring
> **Verkeerde assumptie**: Alle leasing-overeenkomsten worden geactiveerd onder klasse 25.
>
> **Kernpunt**: Be-GAAP: enkel financiële leasing (eigendoms-overdracht of optie aan koopwaarde ≤ 15%) gaat naar klasse 25 als vast actief. Operationele leasing blijft kost in klasse 612 (geen activering). IFRS 16 (vanaf 2019) activeert ALLE leases ≥ 12 maanden — Be-GAAP en IFRS verschillen hier fundamenteel.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Onderneming zelf — boekhouding vaste activa

#### 📒 Boekhouder

##### 👣 Investeringsregister bijhouden

Per actief: aanschaffingsdatum, aanschaffingswaarde, afschrijvingsmethode (lineair/degressief), levensduur, restwaarde, jaarlijkse afschrijving, geaccumuleerde afschrijving, boekwaarde. Verplicht volgens art. 3:42 KB WVV. Bij desinvestering: boekwaarde uitboeken + verschil naar 763 (meerwaarde) of 663 (minderwaarde) of klasse 6/7 indien courant.

<small>📖 KB 29.04.2019 — art. 3:42 — _kb_</small>

#### 🔍 Auditor

##### 👣 Existentie en eigendom vaste activa

Steekproef materiële activa: fysieke inspectie (machine in fabriek, voertuig). Eigendom: factuur + eigendomsdocument (kadaster gebouwen, kentekenbewijs voertuigen, license-akte software). Voor IMA: contract + bewijs van controle. Toets afschrijvingstabel mathematisch: open-saldo + nieuwe + afschrijvingen − desinvesteringen = eind-saldo.

<small>🔗 ISA 501 — Audit-bewijs vaste activa — _norm_</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale vs boekhoudkundige afschrijving

WIB92 art. 61-64: fiscaal aftrekbare afschrijving = boekhoudkundige afschrijving, mits methode (lineair OK, degressief beperkt) en levensduur niet te kort. Bij eerste boekjaar: pro rata temporis voor MVA (art. 196 WIB92). Investeringsaftrek (art. 68-77 WIB92) als bonus-mechanisme. Aandacht: 0% aftrek autovoertuigen sinds AJ 2027 boven CO2 < 95 gram.

<small>📖 WIB92 — art. 61-77 — _wettekst_</small>

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ balans — Eerste hoofdrubriek actief — boven vlottende activa.
### `bevat`
- [[immateriele-vaste-activa]]
- [[materiele-vaste-activa]]
- [[deelneming-financieel-vast-actief]]
### `triggert`
- [[eindejaarsverrichtingen]] — Afschrijvingen + waardevermindering jaarlijks bij afsluit.
### `alternatief_referentiestelsel`
- [[ifrs]] — IAS 16 (MVA) + IAS 38 (IMA) + IAS 36 (impairment) — verschillen op herwaardering en levensduur.
