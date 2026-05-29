---
title: "Deelneming als financieel vast actief"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.C
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/deelneming-financieel-vast-actief.json"
---

_Balanspost_ · ook: deelneming · financial fixed asset

## Definitie

Klasse 28 'financiële vaste activa' (FVA) omvat duurzaam aangehouden aandelen + LT-vorderingen op verbonden ondernemingen. Sub-rubrieken: 280 deelnemingen in verbonden ondernemingen · 281 vorderingen op verbonden ondernemingen · 282 deelnemingen in ondernemingen met deelnemingsverhouding · 283 vorderingen op ondernemingen met deelnemingsverhouding · 284 andere aandelen · 285 andere vorderingen · 286 borgtochten · 288 overige FVA. Begrip 'deelneming': maatschappelijk belang als bedoeld in art. 1:14 WVV — aandelen of effecten met duurzaamheids- of strategisch karakter. 'Verbonden onderneming' = controle, gezamenlijke controle of significante invloed (art. 1:20 WVV).

<small>📖 MAR-KB 21.10.2018 — Bijlage 1 klasse 28 — _kb_ · WVV — art. 1:14 + 1:20 — _wettekst_</small>

## Substantie

Onderscheid klasse 28 ↔ klasse 51 zit in INTENTIE + DUUR: klasse 28 = strategisch/duurzaam aanhouden om relatie te onderhouden, controle uit te oefenen, of via dividend stabiel rendement te krijgen; klasse 51 = speculatief of liquide-overschot. Waardering Be-GAAP: at-cost (CBN 126/8) — aanschaffingswaarde + eventueel waardevermindering bij duurzame waardedaling. Equity-method (proportioneel aandeel in eigen vermogen dochter) is BeGAAP-vrije keuze in enkelvoudige jaarrekening; verplicht voor geassocieerde deelnemingen in geconsolideerde jaarrekening. IFRS 9 (financiële instrumenten) hanteert reële-waarde-waardering met verwerking via OCI (waardestijging niet via P&L) of via P&L (FVTPL) afhankelijk van business model.

<small>📖 CBN-advies 126/8 — FVA-waardering — _cbn_ · Verordening (EU) 2023/1803 — IFRS 9 + IAS 28 — _wettekst_</small>

## Rationale

Aparte FVA-rubriek bestaat omdat deelnemingen anders functioneren dan zowel andere vaste activa (gen afschrijving — geen verbruik door tijd) als andere financiële instrumenten (gen direct verkoop — strategisch karakter). Voorzichtigheidsbeginsel verbiedt herwaardering naar boven (geen 'goodwill-creatie'), maar verplicht waardevermindering bij duurzame waardedaling. Voor de stagiair: bij analyse van groep-vennootschappen is FVA + LT-vorderingen op verbonden ondernemingen typisch grote post — vraag altijd transfer-pricing-documentatie en deelnemingen-overzicht.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Deelneming vs kortetermijn-belegging — afgrenzing

#### Definitie

WVV art. 1:14 § 1: 'deelneming' = maatschappelijke rechten in andere onderneming, bestemd om door duurzaam verband bij te dragen tot eigen werkzaamheid. Vermoeden van deelneming (lid 2): aandelenbezit ≥ 10%. Onder 10%: kan deelneming zijn mits aangetoond duurzaam karakter (raad-positie, strategische samenwerking, langetermijn-overeenkomst).

<small>📖 WVV — art. 1:14 — _wettekst_</small>

### 📦 280 — Deelnemingen in verbonden ondernemingen

#### Definitie

Verbonden = controle (> 50%) of joint control (= 50%) of significante invloed (≥ 20%). Sub: 2800 aanschaffingswaarde · 2808 herwaarderingsmeerwaarden · 2809 waardeverminderingen (-). Boeking bij aankoop: 2800 D / 55 (bank) C. Bij waardedaling duurzaam: 633 (waardevermindering FVA) D / 2809 C.

<small>📖 MAR-KB — klasse 280 — _kb_ · WVV — art. 1:20 verbonden onderneming — _wettekst_</small>

> [!example]- Aurelia Holding koopt 60% Zelena Bio voor 1.500.000 EUR
> _Strategische deelneming voor verticale integratie._
>
> **📒 Boeking aankoop**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 2800 — Deelnemingen verbonden ond. — aanschaffingswaarde | 1.500.000 |  |
> | 550 — Bank |  | 1.500.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 281 — LT-vorderingen op verbonden ondernemingen

#### Definitie

Inter-companylening van moeder aan dochter (of omgekeerd) met termijn > 1 jaar. Transfer-pricing: marktconforme rente verplicht voor fiscaal motief (art. 26 WIB92, circulaire 2020/C/35). Disconteringsregel art. 3:45 KB WVV: bij renteloze of laag-rente LT-vordering aan contante waarde.

<small>📖 WIB92 — art. 26 — _wettekst_ · Circulaire 2020/C/35 — Transfer pricing — _circulaire_</small>

### 📦 At-cost vs equity-method

#### Definitie

Be-GAAP standaard = at-cost: aanschaffingswaarde + waardevermindering bij duurzame daling. Geen impact op winst dochteronderneming. IFRS / consolidatie: equity-method (IAS 28 voor geassocieerde deelnemingen + joint ventures) — initieel aan kostprijs, daarna jaarlijks bijgesteld voor aandeel in winst/verlies + ontvangen dividenden. Boeking equity: 280 D / 7591 (aandeel in resultaat verbonden onderneming) C bij positief resultaat.

<small>📖 Verordening (EU) 2023/1803 — IAS 28 — _wettekst_ · CBN-advies 126/8 — FVA-waardering — _cbn_</small>

## Valkuilen

> [!warning]- Klasse 51 vs 280 verwarren
> **Verkeerde assumptie**: Aandelen in een dochter mogen onder 'aandelen 51' staan.
>
> **Kernpunt**: Strategische aandelen met deelnemingsverhouding (≥ 10% vermoedelijk, of expliciet duurzaam karakter) horen onder 280-282. Speculatieve aandelen (winstrealisatie korte termijn) → 51. Foutieve rubricering vertekent ratio-analyse (vaste-activa-ratio) en fiscale behandeling (DBI-aftrek alleen voor deelnemingen).
>
> <small>📖 WVV — art. 1:14 — _wettekst_</small>

> [!warning]- Inter-companylening renteloos boeken
> **Verkeerde assumptie**: Tussen moeder en dochter mag de lening renteloos zijn omdat het 'eigen geld' blijft.
>
> **Kernpunt**: Transfer-pricing (art. 26 WIB92) eist marktconforme rente — zo niet wordt 'abnormaal voordeel' belast bij debiteur OF rente bij crediteur fictief belast. Documenteer benchmarks (vergelijkbare leningen externe banken). Bij audit-cliënt grote post 281: vraag transfer-pricing-documentatie.
>
> <small>📖 WIB92 — art. 26 — _wettekst_</small>

> [!warning]- Waardevermindering = automatisch fiscaal aftrekbaar
> **Verkeerde assumptie**: Bij koersdaling beursaandeel in 280: waardevermindering 633 = direct in resultaat én fiscaal aftrekbaar.
>
> **Kernpunt**: WIB92 art. 198 7°: waardeverminderingen op aandelen zijn fiscaal NIET aftrekbaar (behalve in specifieke vereffenings-gevallen). Boekhoudkundig wel boeken, fiscaal toevoegen aan verworpen uitgaven. Onder DBI-regime kan meerwaarde wél vrijgesteld zijn — maar minderwaarde niet aftrekbaar (asymmetrie).
>
> <small>📖 WIB92 — art. 198 7° — _wettekst_</small>

## Accountant-perspectieven

### Onderneming zelf — deelnemings-beheer

#### 📒 Boekhouder

##### 👣 Deelnemingen-register bijhouden

Per deelneming: identiteit dochter + % aandelen + aanschaffingsdatum + aanschaffingswaarde + later geboekte meerwaarden/waardeverminderingen + boekwaarde. Bij ontvangen dividend: 750 (financiële opbrengst) D / 55 C. Jaarafsluit-check: vergelijk boekwaarde met aandeel in eigen vermogen dochter (uit dochters JR) — bij duurzame negatieve afwijking → waardevermindering boeken.

<small>🔗 CBN-advies 126/8 — FVA-waardering — _cbn_</small>

#### 🔍 Auditor

##### 👣 Waarderings-toets FVA

Per deelneming materieel bedrag: vraag laatste JR + financiële prognose dochter. Vergelijk boekwaarde met aandeel in eigen vermogen (impairment-indicator). Bij niet-genoteerd: due diligence van DCF-business plan. ISA 540 (schattingen). Bij meerderheidsdeelneming: wijs op consolidatieverplichting (art. 1:33 WVV).

<small>📖 ISA 540 — Boekhoudkundige schattingen — _norm_</small>

#### 💰 Fiscaal adviseur

##### 📜 DBI-aftrek bij dividenden uit deelneming

Dividenden uit klasse 280-282 deelnemingen kunnen 100% afgetrokken worden van VenB-basis (art. 202-205 WIB92) mits: (a) minimum 10% deelneming OF aanschaffingswaarde ≥ 2.500.000 EUR; (b) houdduur ≥ 1 jaar; (c) onderworpen aan vergelijkbaar VenB-tarief in land dochter (subject-to-tax-vereiste). Onder DBI-aftrek wordt economisch dubbel-belasten van groep-winst vermeden.

<small>📖 WIB92 — art. 202-205 — _wettekst_</small>

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vaste-activa]] — Klasse 28 = derde grote FVA-categorie.
### `vergelijkbaar_met`
- [[geldbeleggingen-en-liquide-middelen]]
    - **Gelijkenissen**:
        - Beide kunnen aandelen bevatten
    - **Verschillen**:
        - Klasse 28 = duurzaam; klasse 51 = speculatief
        - Fiscaal: DBI-aftrek alleen voor deelnemingen
### `triggert`
- [[eindejaarsverrichtingen]] — Jaarlijkse waardering tegen aandeel in EV dochter.
### `vereist`
- ⏳ consolidatie — Meerderheidsdeelneming triggert consolidatieverplichting.
### `alternatief_referentiestelsel`
- [[ifrs]] — IFRS 9 (financial instruments) + IAS 28 (associates) — equity-method standaard.
