---
title: "Voorheffingen en verrekeningen VenB"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.J
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/voorheffingen-en-verrekeningen-venb.json"
---

# Voorheffingen en verrekeningen VenB

_Kader_

📋 Regeling · Anchors: `2.3.II.J` · Wave: `cluster-extract-fiscaliteit-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: verrekeningen vennootschapsbelasting · VenB-verrekeningen — **Vertalingen**: en: withholding taxes and tax credits — corporate income tax · fr: précomptes et imputations à l'impôt des sociétés

## Definitie

📖 Het regime van voorheffingen + verrekeningen bij vennootschapsbelasting (VenB) regelt hoe vooruitbetaalde of bronheffings-belastingen worden afgezet tegen de uiteindelijke VenB-aanslag. Vier hoofd-categorieën: (1) voorafbetalingen — vrijwillige kwartaal-stortingen om de vermeerderings-bijdrage te vermijden (WIB art. 218); (2) verrekenbare voorheffingen — roerende voorheffing (RV) op door de vennootschap ontvangen dividenden/interesten, en bedrijfsvoorheffing (BV) op de aan haar betaalde bezoldigingen (zelden van toepassing); (3) forfaitair gedeelte buitenlandse belasting (FBB) — verrekening van buitenlandse bronheffing op roerende inkomsten (art. 285-292); (4) belastingkredieten (research-O&O, energetische renovatie, ...). Saldo na verrekening = werkelijk verschuldigde of terug te krijgen VenB.

<small>📚 WIB 92 — art. 276-292 (verrekeningen) + 218 (voorafbetalingen) — _wettekst_</small>

## Substantie

🔗 Het vermijden van dubbele belasting is de drijvende logica. Als een Belgische vennootschap dividenden krijgt uit een Franse dochter, zijn die in Frankrijk al belast (bronheffing) en in België bij ontvangst (RV 30 %). Zonder verrekenings-mechanisme zou dezelfde euro 2-3 keer belast worden. De FBB (forfaitair gedeelte buitenlandse belasting) geeft een fictieve verrekening voor de buitenlandse bronheffing; de RV op binnenkomende dividenden wordt verrekend tegen VenB. Voor de stagiair gecertificeerd-accountant zit het werk in het correct invullen van de aangifte VenB (formulier 275.1) — verkeerde invulling = teveel betaald of fout terugvragen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom geen samenvoeging met PB-aftrekken? De logica is fundamenteel anders. In de PB worden voorheffingen aangerekend op de uiteindelijke PB-schuld van de natuurlijke persoon — bedrijfsvoorheffing op zijn loon, roerende voorheffing op zijn dividenden. In de VenB komt bedrijfsvoorheffing NOOIT bij de vennootschap terug (die is voor de werknemer); enkel ROERENDE voorheffing op door de vennootschap ontvangen inkomsten is relevant. Bovendien werkt VenB met voorafbetalings-vermeerdering (art. 218) die in PB niet bestaat. Daarom: aparte fenomeen-records, geen samenvoeging.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Opstellen aangifte VenB — saldo-berekening: verschuldigde VenB − voorafbetalingen − RV-verrekening − FBB = te betalen of terug te krijgen.
- 📖 Kwartaal-planning voorafbetalingen — vermeerderings-bijdrage vermijden (typisch 6,75 % over te weinig voorafbetaalde grondslag).
- 🔗 Internationale dividend-flow — verrekening FBB voor buitenlandse bronheffing.

## Sub-concepten

### 📦 Voorafbetalingen VenB  
_`regime` (subconcept)_

#### Definitie

📖 Vrijwillige kwartaal-stortingen door de vennootschap om de eind-VenB voor te financieren en de vermeerderings-bijdrage te vermijden. Vier vervaltermijnen (VA1 t/m VA4): 10 april, 10 juli, 10 oktober, 20 december. Elke storting krijgt een 'bonificatie-percentage' dat het belastings-effect bepaalt — vroege betaling = hogere bonificatie. Indien onvoldoende voorafbetaald: vermeerderings-bijdrage van typisch 6,75 % (AJ 2025) op de te weinig voorafbetaalde grondslag.

<small>📚 WIB 92 — art. 218 — _wettekst_</small>

#### Substantie

🔗 Voor de KMO-accountant: zelfs zonder cashbehoefte zijn voorafbetalingen vaak fiscaal voordelig — 6,75 % vermeerdering is duurder dan kortlopende bankrente. Vuistregel: betaal in VA1 (april) zoveel als mogelijk = hoogste bonificatie. Starters genieten gedurende 3 jaar vrijstelling van vermeerdering — typische 'starter-faciliteit'.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 RV-verrekening bij VenB  
_`regime` (subconcept)_

#### Definitie

📖 Roerende voorheffing (typisch 30 %) ingehouden op aan de vennootschap betaalde dividenden, interesten, royalty's is verrekenbaar tegen haar uiteindelijke VenB-schuld (WIB art. 276 + 281). Voorwaarden: (a) inkomsten zijn opgenomen in belastbare grondslag (of vrijgesteld via DBI); (b) RV werkelijk ingehouden + gestort. Bij DBI-aftrek: de RV blijft verrekenbaar zelfs op het vrijgestelde dividend (dubbele beneficiaire behandeling). Niet-verrekend overschot: terugbetaald.

<small>📚 WIB 92 — art. 276 + 281 — _wettekst_</small>

#### Substantie

🔗 Praktisch frequent bij dividenden uit dochter-vennootschappen waar de moeder onder de DBI-drempel zit (geen 95 %-vrijstelling). Voorbeeld: Aurelia Holding krijgt 100 KEUR brutodividend van een 8 %-deelneming → RV 30 KEUR ingehouden + Aurelia ontvangt 70 KEUR netto. Aurelia geeft 100 KEUR aan in haar VenB-grondslag, krijgt 30 KEUR RV-verrekening tegen verschuldigde VenB.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Forfaitair gedeelte buitenlandse belasting (FBB)  
_`regime` (subconcept)_

#### Definitie

📖 FBB is een fictieve verrekening voor buitenlandse bronheffing op door de Belgische vennootschap ontvangen roerende inkomsten — typisch op interesten en royalty's (zelden op dividenden, omdat die meestal DBI-vrijgesteld zijn). Berekening: 15/85 van het werkelijk ontvangen bedrag (forfaitair) of de werkelijke ingehouden buitenlandse bronheffing — afhankelijk van DBV. Verrekenbaar tegen Belgische VenB tot max. de bedragen die de werkelijke buitenlandse heffing toelaten. Niet-verrekend overschot is NIET terugbetaalbaar (in tegenstelling tot RV).

<small>📚 WIB 92 — art. 285-292 — _wettekst_</small>

#### Substantie

🔗 Belangrijk voor multinationale groep-structuren. Voorbeeld: Belgische moeder krijgt 100 KEUR interest van Italiaanse dochter; Italië heft 15 % bronheffing (per DBV) = 15 KEUR; België belast netto 85 KEUR + verrekent FBB = 15/85 × 85 = 15 KEUR (gelijk aan werkelijke heffing). Voor dividenden uit klein-deelneming (geen DBI): vaak combinatie RV-verrekening + FBB-verrekening voor zelfde brutostroom.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Saldo-berekening VenB — Zelena Bio NV (AJ 2025) 🔗

_Zelena Bio NV: VenB op belastbare grondslag = 83.625 EUR. Voorafbetalingen VA1 30.000 + VA2 25.000 + VA3 20.000 + VA4 10.000 = 85.000. Ontvangen dividend 100 KEUR met 30 % RV (= 30.000) gestort. Belastingjaar 2025._



<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Bedrijfsvoorheffing voor VenB rekenen

**Verkeerde assumptie**: BV op aan medewerkers betaalde lonen mag de vennootschap verrekenen.

**Kernpunt**: Bedrijfsvoorheffing wordt ingehouden DOOR de vennootschap en gestort aan de fiscus — voor rekening van de werknemer. Voor de vennootschap is BV een doorgeefluik, geen verrekening. De werknemer recupereert BV in zijn PB-aangifte. Verwarring leidt tot dubbele aanrekening + naheffing.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ RV verrekenen op DBI-vrijgesteld dividend vergeten

**Verkeerde assumptie**: DBI-vrijgesteld dividend → geen RV-verrekening mogelijk.

**Kernpunt**: DBI-vrijstelling + RV-verrekening zijn cumulatief. Dividend is voor 100 % vrijgesteld via DBI, MAAR de RV (30 %) blijft verrekenbaar tegen andere VenB-schuld. Dubbele begunstiging is bewust — wet wil cross-border dividenden niet penaliseren.

<small>📚 WIB 92 — art. 276 + 281 — _wettekst_</small>

### ⚠️ FBB als terugbetaalbaar krediet behandelen

**Verkeerde assumptie**: FBB-overschot wordt terugbetaald zoals RV-overschot.

**Kernpunt**: FBB is alleen verrekenbaar tot beloop van de Belgische VenB-schuld op de buitenlandse inkomsten. Overschot NIET terugbetaald (in tegenstelling tot RV). Reden: FBB compenseert dubbele belasting; geen dubbele belasting = geen recht op terugbetaling.

<small>📚 WIB 92 — art. 287 — _wettekst_</small>

### ⚠️ Vermeerderings-bijdrage onderschatten bij groeiende vennootschap

**Verkeerde assumptie**: Voorafbetaling op basis van vorig-jaar-VenB volstaat.

**Kernpunt**: Bij snel groeiende vennootschap (sterke winststijging) → voorafbetaling op basis van vorig jaar = onvoldoende → vermeerderings-bijdrage 6,75 % over tekort. Vuistregel: schat verwachte VenB tijdig (bij Q3-cijfers) en pas VA aan. Starters (eerste 3 jaar): vrijstelling vermeerdering.

<small>📚 WIB 92 — art. 218 §2 (starter-vrijstelling) — _wettekst_</small>

## Verder lezen (scope-out)

- → Voorafbetalingen (generiek + VenB-perspectief) → [[voorafbetalingen]] _(moet-verwijzen)_
- → Roerende voorheffing (instrument) → [[roerende-voorheffing]] _(moet-verwijzen)_
- → Bedrijfsvoorheffing (instrument) → [[bedrijfsvoorheffing]] _(moet-verwijzen)_
- ↪ DBI-aftrek (vrijstelling vs FBB-verrekening) → [[dbi-aftrek]] _(mag-verwijzen)_
- ↪ Internationaal-fiscaal kader _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]]
### `vereist`
- [[voorafbetalingen]]
### `bevat`
- [[forfaitair-gedeelte-buitenlandse-belasting]] — FBB is één van de verrekenings-mechanismen.
### `beinvloed_door`
- [[roerende-voorheffing]] — RV op binnenkomende inkomsten is verrekenbaar tegen VenB.
### `vergelijkbaar_met`
- [[dbi-aftrek]]
    - **Gelijkenissen**:
        - Beide vermijden dubbele belasting op grensoverschrijdende dividenden
    - **Verschillen**:
        - DBI = vrijstelling 100 % (geen belasting); FBB = verrekening van werkelijke buitenlandse heffing
    - ⚠️ **Verwarringsrisico**: Studenten denken vaak dat DBI en FBB elkaar uitsluiten — ze zijn cumuleerbaar op zelfde dividend.
