---
title: "Minderheidsbelangen"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.4.I.D
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/minderheidsbelangen.json"
---

_Kader_ · ook: belangen van derden · non-controlling interests · NCI · minority interests

## Definitie

Minderheidsbelangen (BE-GAAP: 'belangen van derden'; IFRS: 'non-controlling interests' of NCI) zijn het aandeel in het eigen vermogen en het resultaat van een integraal geconsolideerde dochter dat NIET toekomt aan de moedervennootschap. Ze ontstaan zodra de moeder minder dan 100 % van het EV-belang in de dochter bezit terwijl zij toch de controle uitoefent (anders zou de dochter niet integraal worden geconsolideerd). In de geconsolideerde balans verschijnen ze in een aparte rubriek IX 'Belangen van derden', tussen het groeps-EV en het vreemd vermogen; in de resultatenrekening als afzonderlijke lijn onder het geconsolideerd resultaat.

<small>📖 KB WVV — art. 3:132 — _kb_ · KB WVV — art. 3:145 — _kb_</small>

## Substantie

Economisch: de groep behandelt de hele dochter alsof zij van haar is (integrale opname), maar erkent dat een deel van het vermogen en het resultaat eigenlijk toebehoort aan externe aandeelhouders van de dochter. Die externe aandeelhouders zijn geen schuldeisers (geen recht op terugbetaling), maar ook geen groepsaandeelhouders (geen recht op groepsdividend). Daarom een eigen rubriek tussen EV en VV: 'Belangen van derden' is een soort 'EV van anderen'. Op resultaatniveau wordt eerst het volledige resultaat van de dochter in de geconsolideerde RR opgenomen; daarna wordt het deel dat toekomt aan minderheden afgetrokken om tot het groepsresultaat te komen.

<small>🔗 KB WVV — art. 3:132 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Ratio: het volledig opnemen van een 60%-dochter zou zonder afzonderlijke minderheidsaanduiding misleidend zijn — de gebruiker zou denken dat het hele vermogen aan de groepsaandeelhouders toekomt. De rubriek 'Belangen van derden' herstelt dat door zichtbaar te maken hoeveel vermogen aan externe partijen toekomt. Het verzoent de 'one-entity-view' (groep als economische eenheid) met de 'parent-view' (alleen wat aan moeder-aandeelhouders toebehoort).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB WVV art. 3:132 + art. 3:145; IFRS 10 (Verordening 2023/1803) + IFRS 3 voor goodwill-keuze

Stabiele regeling. Een grote IFRS-wijziging: sinds IFRS 3 (2008) kan goodwill bij overname op twee manieren gewaardeerd worden — full-goodwill (inclusief NCI) of partial-goodwill (alleen moeder-aandeel).

**✅ Voor**
- 🔗 Verschijnt altijd wanneer een dochter integraal geconsolideerd wordt en de moeder minder dan 100 % bezit. Geldt ook bij de-facto-controle zonder meerderheid stemrechten — dan zijn de minderheidsbelangen relatief groot.

**🚫 Niet voor**
- 🔗 Niet bij 100%-dochters (geen minderheidsbelang, hoogstens een rubriek 'IX. Belangen van derden = 0'). Niet bij vermogensmutatiemethode (één-regel-presentatie — minderheidsbelang gaat op in het VMM-saldo). Niet bij evenredige consolidatie (alleen pro-rata-deel opgenomen, dus geen 'overschot' voor derden).

## Bouwstenen

### 📜 EV-presentatie — rubriek IX

In de geconsolideerde balans verschijnen 'Belangen van derden' in rubriek IX, na het eigen vermogen van de groep (rubrieken I-VIII) en vóór het vreemd vermogen. Onder IFRS staat het binnen het totale eigen vermogen ('Equity'), gerubriceerd onder 'Non-controlling interests' apart van 'Equity attributable to owners of the parent'. Berekening op verkrijgingsdatum: aandeel derden × EV dochter op die datum. Daarna wordt het aandeel jaarlijks bijgewerkt voor het deel van derden in het resultaat en in EV-mutaties.

<small>📖 KB WVV — art. 3:132 — _kb_ · Verordening (EU) 2023/1803 — IFRS 10 alinea 22 — _wettekst_</small>

### 📜 Resultaat-presentatie — afzonderlijke lijn

Het volledige resultaat van de dochter wordt regel-per-regel in de geconsolideerde RR opgenomen (omzet, kosten, bedrijfsresultaat, ...) tot aan het netto-resultaat. Daaronder twee lijnen: 'Aandeel van de groep in het resultaat' + 'Aandeel van derden in het resultaat'. Het aandeel van derden = % belang derden × netto-resultaat dochter (na aanpassingen). Bij IFRS-presentatie staat dit als 'profit attributable to owners of the parent' + 'profit attributable to non-controlling interests'.

<small>📖 KB WVV — art. 3:145 — _kb_ · Verordening (EU) 2023/1803 — IFRS 10 alinea 22, B94 — _wettekst_</small>

### 🧮 Berekening minderheidsbelang

Op verkrijgingsdatum: NCI = % aandeel derden × identifiable net assets dochter (BE-GAAP: boekhoudkundig EV). Daarna jaarlijks bijwerken: NCI(t) = NCI(t-1) + (% derden × resultaat dochter jaar t) - (% derden × dividend dochter jaar t) ± andere EV-mutaties.

<small>🔗 KB WVV — art. 3:132 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Minderheidsbelang in CBN 2022/09 voorbeeld 10 (80%-dochter)
> _X koopt 80 % van X1 voor 200. EV X1 = 450. Aandeel X in EV = 360. Aandeel derden in EV = 90 (20 % × 450). Goodwill = 200 - 360 = -160 (negatief consolidatieverschil)._
>
> **📊 Geconsolideerde balans X + X1 — EV-deel**
>
> ```json
> {
>   "tekst": "Rubriek I-VIII (groeps-EV): Kapitaal 100 + Reserves 300 + Consolidatieverschil (passief) 160 = 560. Rubriek IX (Belangen van derden): 90. Totaal EV-zijde: 650."
> }
> ```
>
> <small>📖 CBN-advies — 2022/09 voorbeeld 10 — _cbn_</small>

## Valkuilen

> [!warning]- NCI = vreemd vermogen
> **Verkeerde assumptie**: Studenten zien 'Belangen van derden' en denken aan een schuld aan externe aandeelhouders.
>
> **Kernpunt**: NCI is géén schuld — minderheidsaandeelhouders hebben geen recht op terugbetaling, alleen op een aandeel in het EV en in dividenden. Daarom staat de rubriek aan de EV-kant van de balans (rubriek IX, vóór VV), niet onder schulden.
>
> <small>📖 KB WVV — art. 3:132 — _kb_</small>

> [!warning]- Verwarring met minderheidsvordering (WVV)
> **Verkeerde assumptie**: 'Minderheidsbelang' = de minderheidsvordering van art. 5:104 / 7:157 WVV.
>
> **Kernpunt**: Twee totaal verschillende begrippen die toevallig 'minderheid' delen. De minderheidsvordering is een vennootschapsrechtelijk procedureel recht (vordering namens vennootschap tegen bestuurders door aandeelhouders met ≥10 % BV / ≥1 % NV). Het minderheidsbelang in consolidatie is een boekhoudkundige presentatierubriek voor het EV-aandeel van niet-controlerende aandeelhouders.
>
> <small>📖 WVV — art. 5:104, 7:157 — _wettekst_ · KB WVV — art. 3:132 — _kb_</small>

> [!warning]- Verlies-NCI: negatief saldo
> **Verkeerde assumptie**: NCI kan niet negatief worden — bij verlies stopt men met afboeken.
>
> **Kernpunt**: Onder IFRS 10 (alinea B94) wordt het aandeel van derden in verlies onbeperkt afgeboekt, ook als NCI negatief wordt — minderheid draagt dus virtueel mee in verliezen. Onder BE-GAAP geldt dezelfde logica (totale toerekening van resultaat aan derden naar rato van belang).
>
> <small>📖 Verordening (EU) 2023/1803 — IFRS 10 alinea B94 — _wettekst_</small>

## Speelruimtes

### 🎚️ IFRS 3 — full-goodwill vs partial-goodwill voor NCI-waardering bij overname

## Accountant-perspectieven

### Groepsmoedervennootschap

_De accountant die de geconsolideerde jaarrekening opstelt en moet beslissen over NCI-presentatie en -waardering._

#### 📒 Boekhouder

##### 👣 Jaarlijkse update minderheidsbelang

Bij elke consolidatie: NCI(t-1) → NCI(t) door (1) aandeel derden in resultaat van dochter optellen, (2) aandeel derden in dividend van dochter aftrekken, (3) eventuele EV-mutaties (kapitaalverhogingen, herwaarderingsreserves, OCI-bewegingen) pro rata toewijzen. Bij wijziging van belang zonder controleverlies (bv. moeder koopt nog 10 % bij): NCI naar rato aanpassen tegen een EV-tegenpost (geen P&L-impact, IFRS 10 alinea 23).

<small>📖 Verordening (EU) 2023/1803 — IFRS 10 alinea 23, B96 — _wettekst_ · KB WVV — art. 3:132 — _kb_</small>

#### 🔍 Auditor

##### 👣 Audit NCI-allocatie + bewegingen

Verifieer (1) de juiste berekening van het %-belang derden (statuten + aandeelhoudersregister); (2) de openingsbalans NCI op verkrijgingsdatum (reproduceer EV-aandeel × %); (3) de jaarlijkse update (resultaat-allocatie + dividenduitkeringen); (4) de gekozen IFRS 3-methode (full vs partial goodwill) en haar consistente toepassing; (5) toelichting IFRS 12 par. 10-17 over significante NCI.

<small>📖 Verordening (EU) 2023/1803 — IFRS 12 par. 10-17 — _wettekst_ · ISA 600 — par. A23 + Bijlage 2 — _norm_</small>

## Verder lezen (scope-out)

- → Integrale consolidatie (ontstaans-context) → [[integrale-consolidatie]] _(moet-verwijzen)_
- → Consolidatieverschil (goodwill-context) → [[consolidatieverschil]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[consolidatiemethoden]]
### `vereist`
- [[integrale-consolidatie]] — Minderheidsbelangen ontstaan alleen bij integrale consolidatie van een niet-100%-dochter.
### `vergelijkbaar_met`
- [[consolidatieverschil]]
    - **Gelijkenissen**:
        - Beide ontstaan op verkrijgingsdatum bij eerste integrale consolidatie
        - Beide nemen het pro-rata-aandeel van de moeder versus derden in rekening
    - **Verschillen**:
        - Consolidatieverschil = excedent of tekort aanschaffingsprijs t.o.v. moeder-EV-aandeel → goodwill of badwill
        - Minderheidsbelang = derden-EV-aandeel op verkrijgingsdatum → eigen EV-rubriek
        - Goodwill kan ook NCI omvatten onder full-goodwill-methode (IFRS 3)
