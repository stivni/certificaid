---
title: "Vorderingen op meer dan één jaar"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.D
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/vorderingen-op-meer-dan-een-jaar.json"
---

_Balanspost_ · ook: LT-vorderingen · langetermijn-vorderingen

## Definitie

Klasse 29 omvat vorderingen op derden met restduur > 1 jaar vanaf balansdatum. Sub-rubrieken: 290 handelsvorderingen op meer dan één jaar · 291 overige vorderingen · 292 te innen wissels · 294/295 borgtochten · 298 geboekte waardeverminderingen (-). Onderscheid met klasse 28 (FVA): klasse 29 = vorderingen op klanten/derden (commercieel of overig); klasse 28 = duurzame deelnemingen + LT-vorderingen op verbonden ondernemingen. Bij herklassering (LT-vordering wordt ≤ 1 jaar): verschuiven naar klasse 40 'vervallend binnen het jaar' bij eindejaars-presentatie.

<small>📖 MAR-KB 21.10.2018 — Bijlage 1 klasse 29 — _kb_</small>

## Substantie

De kerngedachte van rubriek 29 is matching met de balansstructuur: vlottend (≤ 1 jaar, klasse 3-5) versus duurzaam (> 1 jaar, klasse 2). Bij vorderingen ontstaat een specifieke vraag: moet de waarde gediscontered worden naar contante waarde? Art. 3:45 KB WVV antwoordt: ja, bij vorderingen zonder rente of met abnormaal lage rente + looptijd > 1 jaar → boeking aan contante waarde + jaarlijkse rentecomponent in resultaat (CBN 137/4). Bij commercieel-gangbare rente: nominale waarde volstaat. Klassiek voorbeeld: lening aan personeel zonder rente over 5 jaar — actuele waarde berekenen met marktrente.

<small>📖 KB 29.04.2019 — art. 3:45 § 2 lid 1 c — _kb_ · CBN-advies 137/4 — Renteloze LT-vorderingen — _cbn_</small>

## Rationale

De disconteringsregel reflecteert het voorzichtigheidsbeginsel en het tijdsvoorkeurs-principe: 1.000 EUR die je over 5 jaar terugkrijgt is vandaag minder waard dan 1.000 EUR nu. Voor renteloze LT-vorderingen wordt het 'gemiste rendement' (geïmpliceerde rentecomponent) tijdens de looptijd terug opgebouwd via rubriek 75. Dit voorkomt dat de balans gefavoriseerd is door fictief-hoge vorderingen + onmiddellijk-erkend rente-resultaat dat in werkelijkheid over jaren wordt verdiend.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 290 — Handelsvorderingen > 1 jaar

#### Definitie

Niet-gebruikelijk in dagelijkse handel, maar kan voorkomen bij langlopende contracten met termijnbetalingen (bv. levering op afbetaling, leveringsovereenkomst met betalingstermijn 18-36 maanden, ICT-implementaties). Bij ontstaan: actief 290 D / 700 (omzet) C. Indien renteloos of laag-rente: disconteren (zie CBN 137/4).

<small>📖 MAR-KB — rubriek 290 — _kb_</small>

### 📦 291 — Overige LT-vorderingen

#### Definitie

Niet-commerciële vorderingen > 1 jaar: leningen aan personeel, voorschotten aan bestuurders, vorderingen op fiscus voor recuperatie over meerdere jaren, gestort kapitaal in joint-venture vóór effectieve uitkering.

<small>📖 MAR-KB — rubriek 291 — _kb_</small>

### 📦 Discontering renteloze LT-vordering

#### Definitie

Art. 3:45 § 2 lid 1 c KB WVV: LT-vorderingen zonder rente of met rente lager dan marktrente worden geboekt tegen contante waarde (actuele waarde = nominaal / (1 + i)^n). Verschil nominaal - actuele waarde = nog niet verdiende rente (oprichtingskost-achtige techniek of via 4901 'over te dragen kosten'). Tijdens looptijd: pro rata rente-component naar resultaat (rubriek 7510 'opbrengsten uit vlottende activa' of 7521 specifiek voor LT-vorderingen).

<small>📖 KB 29.04.2019 — art. 3:45 § 2 lid 1 c — _kb_ · CBN-advies 137/4 — Renteloze vorderingen — _cbn_</small>

> [!example]- Renteloze lening 10.000 EUR aan personeelslid over 5 jaar (marktrente 4%)
> _Actuele waarde = 10.000 / (1,04)^5 = 8.219 EUR. Verschil 1.781 = geïmpliceerde rente._
>
> **📒 (1) Toekenning lening**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 291 — Overige LT-vorderingen — nominaal | 10.000 |  |
> | 4901 — Over te dragen rentecomponent (-) |  | 1.781 |
> | 550 — Bank |  | 8.219 |
>
> **📒 (2) Jaar 1 — pro rata rente in resultaat**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 4901 — Over te dragen rentecomponent | 329 |  |
> | 7510 — Opbrengsten uit vlottende activa (rente) |  | 329 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Discontering vergeten bij renteloze LT-vordering
> **Verkeerde assumptie**: Nominale waarde 100.000 EUR over 10 jaar = waardering 100.000 EUR.
>
> **Kernpunt**: Art. 3:45 § 2 c KB WVV verplicht discontering bij renteloos of laag-rente + LT > 1 jaar. Nominale waarde overschat actief + verlaagt voorzichtigheidsbeginsel. Toets: zou een derde deze vordering vandaag kopen voor de nominale waarde? Bij rente 0% en looptijd > 1 jaar: nee.
>
> <small>📖 KB 29.04.2019 — art. 3:45 § 2 c — _kb_</small>

> [!warning]- Klasse 29 vs klasse 28 verwarren
> **Verkeerde assumptie**: Alle LT-vorderingen gaan in klasse 29.
>
> **Kernpunt**: LT-vorderingen op VERBONDEN ondernemingen (moeder, dochter, zuster, deelneming) gaan onder klasse 28 (financiële vaste activa, sub 283/284). Klasse 29 is voor LT-vorderingen op niet-verbonden derden. Belangrijk voor consolidatie + transfer-pricing-rapportering.
>
> <small>📖 MAR-KB — klasse 28 vs 29 — _kb_</small>

## Accountant-perspectieven

### Onderneming zelf

#### 📒 Boekhouder

##### 👣 Restduur-toets bij elke vordering

Per vordering bij ontstaan + elk eindejaar: vraag de restduur tot vervaldag. > 1 jaar → klasse 29; ≤ 1 jaar → klasse 40-41 (handel) of klasse 416 (overige). Bij overgang van LT naar KT (vordering nadert vervaldag): herklassering bij volgende balansopstelling.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Discontering-toets bij renteloze LT-vorderingen

Steekproef klasse 29: vraag onderliggend contract op + check rente-clausule. Bij rente 0% of laag (< 50% marktrente): toets actualisatie. Bij ontbreken: aanpassing voorstellen (waardevermindering op nominaal — discontering-saldo).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ balans — Eind van vaste-activa-blok — boven de splitsing vast/vlottend.
### `vergelijkbaar_met`
- [[handelsvorderingen]]
    - **Gelijkenissen**:
        - Beide vorderingen op derden
    - **Verschillen**:
        - Klasse 29 > 1 jaar; klasse 40-41 ≤ 1 jaar
        - Disconteringsplicht bij LT-renteloos
### `triggert`
- [[eindejaarsverrichtingen]]
