---
title: "Opstart BTW-formaliteiten"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 2.4.II
  - 2.4.taak.1
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/opstart-btw-formaliteiten.json"
---

# Opstart BTW-formaliteiten

_Procedure_

📅 Gebeurtenis · 📋 Regeling · Anchors: `2.4.II` · `2.4.taak.1` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: aanvangsaangifte btw · 604A-procedure · btw-identificatie

## Definitie

📖 Opstart BTW-formaliteiten is de procedure die elke nieuwe btw-belastingplichtige moet doorlopen vóór hij belastbare handelingen verricht: (1) indienen van de aanvangsaangifte 604A (art. 53 §1 1° W.BTW) bij het bevoegd btw-kantoor; (2) toekenning van een uniek btw-identificatienummer (BE + ondernemingsnummer, art. 50 W.BTW); (3) keuze van btw-regime — gewoon regime, vrijstellingsregeling voor kleine ondernemingen (KO, art. 56bis), forfaitaire regeling (afgeschaft sinds 2028, uitdovend), of toetreding tot een btw-eenheid; (4) keuze van aangiftefrequentie (kwartaal- of maandaangifte); (5) optioneel: aanmelden bij OSS voor grensoverschrijdende handelingen.

<small>📚 W.BTW — art. 50 — _wettekst_ · W.BTW — art. 53 §1 1° — _wettekst_ · W.BTW — art. 56bis — _wettekst_</small>

## Substantie

🔗 Praktisch is de aanvangsaangifte het beslismoment waarop de meeste keuzes voor de levensduur van de onderneming worden vastgelegd. Het btw-regime is niet vrijblijvend: een verkeerd gekozen regime kost geld (KO kan voordeliger zijn voor B2C-spelers met lage omzet; gewoon regime is voordeliger voor B2B met veel input-btw). De aangiftefrequentie heeft direct cashflow-impact: kwartaalaangifte = btw-schuld 1-3 maanden later betalen, maar wel voorschotten in december voor 4e kw; maandaangifte = sneller btw-teruggave (gunstig bij investeringen of negatieve marge). Voor digitaal-aanwezige ondernemers is de OSS-keuze (One Stop Shop) bepalend voor grensoverschrijdende afstandsverkopen. Het 604A-formulier wordt sinds 2003 digitaal ingediend via MyMinFin.

<small>📚 W.BTW — art. 53 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De vooraf-identificatie dient drie doelen: (1) controle — de fiscus weet wie zich op de markt begeeft en kan compliance opvolgen; (2) keten-integriteit — een geldig btw-nummer is voorwaarde voor B2B-aftrek bij de afnemer (klant kan btw maar aftrekken als leverancier een geldig nummer heeft, art. 45 W.BTW); (3) economisch — keuze van regime laat aanpassing toe aan profiel (klein vs groot, B2B vs B2C). De richtlijn 2006/112/EG (art. 213) verplicht lidstaten een dergelijk identificatiesysteem op te zetten — België implementeert dit via art. 50 W.BTW.

<small>📚 BTW-richtlijn 2006/112/EG — art. 213-214 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: W.BTW art. 50, 53 §1 1°, 56bis + K.B. nr. 10

Procedure stabiel sinds 1969 W.BTW. Belangrijke wijzigingen: forfaitaire regeling uitdovend (afschaffing nieuwe inschrijvingen sinds 2028); KO-drempel sinds 1-1-2025 op 25.000 EUR omzet (was 25.000 EUR sinds 2016, eerder 15.000 EUR); OSS sinds 1-7-2021 voor e-commerce.

**✅ Voor**
- 📖 Elke nieuwe onderneming die btw-belastbare handelingen zal verrichten in België — natuurlijke persoon, vennootschap, vzw met economische activiteit, vereniging. Ook wijziging van bestaande activiteit (uitbreiding naar btw-belastbare tak) triggert een 604B-aanpassingsaangifte.

**🚫 Niet voor**
- 📖 Loutere particulieren zonder economische activiteit. Verenigingen met uitsluitend vrijgestelde activiteiten (art. 44 W.BTW — onderwijs, gezondheidszorg, sociale dienstverlening) — die hoeven geen btw-nummer aan te vragen, tenzij ze intracommunautaire verwervingen >11.200 EUR doen (art. 50 §1 2°).

**📋 Voorwaarden**
- 📖 Cumulatief: (1) belastingplichtige in de zin van art. 4 W.BTW (geregelde + zelfstandige economische activiteit, ongeacht winstoogmerk); (2) intentie om belastbare handelingen te verrichten in België; (3) ondernemingsnummer via KBO eerst aangevraagd; (4) 604A ingediend vóór de eerste belastbare handeling, idealiter 1-2 weken op voorhand om het btw-nummer tijdig te ontvangen.

**▶️ Trigger start**
- 🔗 Eerste voorgenomen belastbare handeling in België — verkoop van goederen, dienstverlening tegen vergoeding, eerste aankoop met voornemen tot doorverkoop. Bij twijfel over begindatum: 604A indienen op de datum van de eerste investerings- of voorbereidingskost (want al dan recht op aftrek inputs).

**⚠️ Risico**
- 📖 Laattijdige 604A leidt tot weigering van aftrek voor de pré-identificatie-periode (geen aftrek op aankopen vóór de aanvangsaangifte, art. 45 §1 W.BTW). Strafrechtelijk: art. 70 W.BTW boete 250-25.000 EUR per niet-tijdige aangifte. Pragmatische oplossing: 604A indienen vanaf het moment dat de eerste investering of huur wordt afgesloten — desnoods met activiteitstart in de toekomst.
- 📖 Verkeerde regime-keuze kan jaren niet-corrigeerbaar zijn. KO-regime kan niet zomaar verlaten worden tijdens het lopende jaar (overgang naar gewoon regime kan op 1 januari of bij overschrijden drempel). Forfaitaire regeling: nieuwe inschrijvingen sinds 1-1-2028 niet meer mogelijk (uitdovend regime — bestaande mogen blijven tot 31-12-2027).

## Bouwstenen

### 👣 Stap 1 — KBO-inschrijving  
_`stap`_

🔗 Vóór elke btw-aanvraag: ondernemingsnummer aanvragen bij Kruispuntbank van Ondernemingen (KBO) via ondernemingsloket (Liantis, Acerta, ...) of via de griffie (vennootschap). Kosten: ca. 100 EUR. Het BE-nummer wordt later de basis van het btw-nummer (BE + 10 cijfers).

<small>📚 Wet 16-01-2003 — art. III.16 WER — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Stap 2 — 604A indienen (aanvangsaangifte)  
_`stap`_

📖 Aanvangsaangifte 604A indienen elektronisch via MyMinFin (formulier via 'mijn dossier btw') of via een geaccrediteerde dienstverrichter. Verplichte gegevens: identiteit, ondernemingsnummer, aard activiteit (NACE-code), startdatum, vermoedelijke jaaromzet, gewenst btw-regime (gewoon / KO / forfait), gewenste aangiftefrequentie (maand/kwartaal), bankrekening voor terugbetalingen.

<small>📚 W.BTW — art. 53 §1 1° — _wettekst_ · K.B. nr. 10 van 29-12-1992 — art. 1 — _kb_</small>

### 👣 Stap 3 — Toekenning btw-nummer (binnen 14 dagen)  
_`stap`_

📖 De fiscus kent meestal binnen 5-14 werkdagen het btw-identificatienummer toe. Vorm: BE + 10 cijfers (zelfde als KBO + voorvoegsel BE). Vanaf dat moment is de belastingplichtige verplicht facturen op te maken met btw, btw-aangiften in te dienen volgens gekozen frequentie, en de boekhouding btw-conform te voeren.

<small>📚 W.BTW — art. 50 §1 1° — _wettekst_</small>

### 📏 KO-drempel 25.000 EUR  
_`drempel`_

📖 Vrijstellingsregeling voor kleine ondernemingen (KO, art. 56bis W.BTW): jaaromzet ≤ 25.000 EUR (excl. btw, alleen handelingen in België) → mogelijke vrijstelling. Voordelen: geen btw factureren, geen periodieke aangifte (wel jaarlijkse klantenlisting). Nadelen: geen btw-aftrek op inputs. Drempel-overschrijding tijdens het jaar → automatische overgang naar gewoon regime vanaf het kwartaal volgend op overschrijding.

<small>📚 W.BTW — art. 56bis — _wettekst_ · K.B. nr. 19 van 29-06-2014 — art. 2-5 — _kb_</small>

### 📜 Keuze aangiftefrequentie maand vs kwartaal  
_`regel`_

📖 Default: kwartaalaangifte (jaaromzet ≤ 2.500.000 EUR, vanaf 2025). Indien hoger of bepaalde activiteiten (telecom, energie, accijnsgoederen, AB-handelingen): maandaangifte verplicht. Optioneel: maandaangifte op verzoek voor wie systematisch btw-tegoed heeft (versnelde terugbetaling, gunstig bij investeringen). Voor kwartaalaangevers: voorschotten in vak 91 in december (1/3 vorige aangifte) — anti-cashflow-voordeel-correctie.

<small>📚 W.BTW — art. 53 §1 + art. 53octies §1 — _wettekst_ · K.B. nr. 1 — art. 18 — _kb_</small>

## Voorbeelden

### 💡 Startup SaaS — BV-oprichting + btw-opstart 🔗

_Oprichter Tom richt op 1 september een BV op (SaaS-product voor B2B-klanten in Belgium + EU). Hij investeert direct 50.000 EUR in software-ontwikkeling (btw 10.500 EUR) en huurt een kantoor (huur excl. btw 1.500 EUR/maand). Verwachte jaaromzet jaar 1: 80.000 EUR._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "1. Notaris richt BV op (10 dagen voor 1 sept) — KBO-nummer toegekend.",
    "2. Boekhouder dient 604A in op 25 augustus, met startdatum 1 september. Keuze: gewoon regime (niet KO, want B2B), kwartaalaangifte (omzet < 2,5 mio), bankrekening voor terugbetalingen.",
    "3. 1 september: btw-nummer toegekend (BE 0123.456.789).",
    "4. Eerste investeringsfacturen (software-ontwikkeling): 10.500 EUR input-btw aftrekbaar — eerste kwartaalaangifte (oktober) genereert btw-tegoed.",
    "5. Vraag versnelde terugbetaling (vak 72 = ja). Cashflow-voordeel: 10.500 EUR teruggekregen ~6 weken na kwartaalaangifte i.p.v. wachten tot saldo positief wordt."
  ],
  "resultaat": "Keuze gewoon regime is correct want B2B-klanten kunnen btw aftrekken — geen prijs-nadeel voor klant. KO had bouw-btw 10.500 EUR definitief verloren laten gaan. Maandaangifte zou nog sneller terugbetalingen geven maar meer admin."
}
```

<small>📚 W.BTW — art. 53 §1 — _wettekst_ · W.BTW — art. 56bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Yoga-coach particulier — KO-regime 🔗

_Sarah start als zelfstandige yoga-coach, B2C-cliënteel (particulieren). Verwachte jaaromzet 18.000 EUR. Inkopen: yoga-mats, boeken, marketing — ca. 2.000 EUR/jaar (btw 420 EUR)._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "1. KBO-inschrijving + ondernemingsnummer.",
    "2. 604A indienen — keuze KO-regime (omzet ≤ 25.000 EUR + B2C).",
    "3. Btw-nummer toegekend maar geen periodieke aangiften.",
    "4. Sarah factureert zonder btw aan klanten (verplichte vermelding 'Vrijgesteld van btw — bijzondere regeling kleine ondernemingen, art. 56bis W.BTW').",
    "5. Op 31 maart elk jaar: jaarlijkse klantenlisting indienen (jaaromzet boven 250 EUR per btw-plichtige klant)."
  ],
  "resultaat": "KO is voordelig: 420 EUR input-btw is verloren maar Sarah factureert ook 0 % btw aan klanten — bij B2C particulieren is dat prijsvoordeel groter dan het verlies. Bij overschrijden 25.000 EUR (bv. 28.000 EUR jaaromzet) → overgang naar gewoon regime vanaf volgend kwartaal, met vereiste maandaangifte indien grensbedragen overschreden."
}
```

<small>📚 W.BTW — art. 56bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ 604A indienen na de eerste aankoop

**Verkeerde assumptie**: Studenten denken dat de 604A pas hoeft te worden ingediend wanneer de eerste verkoop plaatsvindt.

**Kernpunt**: Art. 53 §1 1° W.BTW zegt 'voor de aanvang van de activiteit'. Inputs (huur, investering, software) die vóór de identificatie zijn aangekocht zijn niet-aftrekbaar (de fiscus weigert pre-identificatie-aftrek). Vuistregel: 604A indienen op het moment dat eerste contractuele verbintenissen worden aangegaan (huurovereenkomst, oprichting BV), zelfs als operationele start later komt.

<small>📚 W.BTW — art. 53 §1 1° — _wettekst_ · W.BTW — art. 45 §1 — _wettekst_</small>

### ⚠️ KO blindelings kiezen omdat omzet laag is

**Verkeerde assumptie**: Studenten + starters kiezen KO omdat omzet < 25.000 EUR.

**Kernpunt**: KO is voordelig voor B2C met lage input-btw. Voor B2B (klant trekt btw af) is gewoon regime altijd voordeliger want: (a) klanten zijn niet gehinderd door de btw (aftrekken); (b) de starter recupereert de eigen input-btw. KO 'kost' dan netto de niet-aftrekbare input. Beslisregel: B2B = gewoon; B2C met lage marge en lage input = KO.

<small>📚 W.BTW — art. 56bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Forfaitaire regeling kiezen voor nieuwe inschrijvingen

**Verkeerde assumptie**: Studenten denken dat forfait nog beschikbaar is voor bakkers, slagers, kappers, ...

**Kernpunt**: De forfaitaire regeling (art. 56 W.BTW) is sinds 1-1-2022 niet meer toegankelijk voor nieuwe inschrijvingen; bestaande forfaitairen mogen het regime hanteren tot 31-12-2027 — daarna volledig afgeschaft. Bij elke nieuwe opstart: enkel KO of gewoon regime.

<small>📚 W.BTW — art. 56 — _wettekst_</small>

## Speelruimtes

### 🎚️ Maandaangifte vs kwartaalaangifte (binnen omzet ≤ 2,5 mio)

## Accountant-perspectieven

### Begeleiding van starters

_De accountant die een nieuwe ondernemer begeleidt vanaf oprichting tot eerste aangifte._

#### 👥 Begeleider

##### 👣 Btw-opstart-checklist 6 weken vóór startdatum  
_`stap`_

🔗 Vier weken vóór de geplande activiteitstart: regime-analyse (B2B vs B2C, omzet-projectie, input-volume); twee weken vóór start: 604A indienen + frequentie kiezen + bankrekening doorgeven; week 1 startdatum: btw-nummer ontvangen, eerste factuur opmaken volgens btw-vormvereisten (art. 5 K.B. nr. 1). Risico: btw-vermelding op factuur zonder geldig nummer = ongeldige factuur, klant kan niet aftrekken.

<small>📚 W.BTW — art. 53 §1 — _wettekst_ · K.B. nr. 1 van 29-12-1992 — art. 5 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Regime-keuze-advies vóór 604A  
_`vuistregel`_

🔗 Beslis-as: (1) klant-profiel B2B → gewoon regime always (klant trekt btw af, geen prijs-nadeel); (2) B2C + omzet ≤ 25.000 EUR → KO als input laag (≤ 2.000 EUR), gewoon regime als input hoog; (3) B2C + omzet > 25.000 EUR → gewoon regime verplicht. Documenteer keuze in cliëntdossier voor latere audit-traceability.

<small>📚 W.BTW — art. 56bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-belastingplichtige (begrip) → [[btw-belastingplichtige]] _(moet-verwijzen)_
- → Stopzetting BTW (spiegel) → [[stopzetting-btw]] _(moet-verwijzen)_
- → Regime-keuze (KO/forfait) → [[vrijstellingsregeling-kleine-onderneming]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw-belastingplichtige]] — Aanvangsaangifte 604A onderstelt belastingplichtig-statuut volgens art. 4.
### `triggert`
- [[btw-aftrek]] — Toekenning btw-nummer activeert recht op aftrek input-btw vanaf identificatiedatum.
### `vergelijkbaar_met`
- [[stopzetting-btw]]
    - **Gelijkenissen**:
        - Beide procedures handelen over identificatie/de-identificatie van btw-statuut
        - Beide vereisen een specifieke aangifte (604A vs 604C) binnen een termijn
        - Beide bevatten herzieningen van btw-positie
    - **Verschillen**:
        - 604A vóór aanvang activiteit; 604C binnen één maand na stopzetting
        - Opstart genereert aftrekrechten; stopzetting kan herzieningsschulden genereren
        - Opstart: regime-keuze; stopzetting: eindafrekening + voorraadbehandeling
    - ⚠️ **Verwarringsrisico**: Studenten verwarren de twee formulieren — 604A start, 604B wijziging, 604C einde.
