---
title: "Aftrek voor innovatie-inkomsten"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.D
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/innovatie-aftrek.json"
---

# Aftrek voor innovatie-inkomsten

_Regime_

📋 Regeling · Anchors: `2.3.II.D` · Wave: `fiscale-voordelen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: innovatie-aftrek — **Synoniemen**: IP-aftrek nieuwe regime · aftrek innovatie-inkomsten art. 205/1

## Definitie

📖 De aftrek voor innovatie-inkomsten (art. 205/1 tot 205/4 WIB92) stelt 85 % van de netto-inkomsten uit kwalificerende intellectuele eigendomsrechten vrij van vennootschapsbelasting. Kwalificerende rechten zijn o.a. octrooien, kwekersrechten, auteursrechtelijk beschermde software ontwikkeld in een R&D-project, en weesgeneesmiddelen. Het regime geldt sinds 1 juli 2016 (wet 9-2-2017) en vervangt de oudere octrooi-inkomen-aftrek (80 %, art. 543 WIB92). Het volgt de OESO-nexus-benadering: de aftrek wordt evenredig beperkt naargelang het aandeel eigen R&D-uitgaven in de totale R&D-kosten van het IP-actief.

<small>📚 WIB92 — art. 205/1 §1 — _wettekst_ · WIB92 — art. 205/2 — _wettekst_</small>

## Substantie

🔗 Het effectief belastingtarief op netto-innovatie-inkomen daalt zo van 25 % naar 3,75 % (= 25 % × 15 %). Concreet: een softwarebedrijf met 1 mio EUR licentie-inkomsten betaalt — na aftrek R&D-kosten en nexus-correctie — slechts ca. 37.500 EUR belasting i.p.v. 250.000 EUR. Voor R&D-intensieve bedrijven (biotech, software, deep-tech) is dit het meest impactvolle fiscale regime. De aftrek wordt op de netto-IP-inkomsten toegepast: bruto-inkomsten minus rechtstreekse kosten (afschrijving IP, R&D-uitgaven, royalty's). Niet-gebruikte aftrek is onbeperkt overdraagbaar; sinds 2017 ook omzetbaar in een belastingkrediet (art. 289decies) — handig voor verlieslatende vennootschappen.

<small>📚 WIB92 — art. 205/1 — _wettekst_ · WIB92 — art. 289decies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: stimuleren van R&D-activiteit in België. De OESO heeft via BEPS Action 5 (2015) een 'nexus-approach' opgelegd om 'patent box'-regimes te beperken tot reële economische activiteit — anders zouden lege IP-holdings buitenlandse R&D-inkomsten kunnen onderbrengen in landen met gunstige aftrek. De nexus-formule koppelt de aftrek aan de eigen R&D-inspanning: hoe meer eigen R&D, hoe meer aftrek. Zo wordt fiscaal voordeel gekoppeld aan substantiële economische activiteit.

<small>📚 WIB92 — art. 205/2 §2 (nexus) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2016-07-01** · basis: WIB92 art. 205/1 tot 205/4 + art. 289decies (belastingkrediet) + opgave 275 INNO

Ingevoerd door wet 9-2-2017 ter vervanging van oude octrooi-aftrek (art. 543 WIB92, 80 %-aftrek alleen voor octrooi-inkomsten). Overgangsregime tot 30-6-2021 voor reeds ontwikkelde IP onder oude regime.

**✅ Voor**
- 📖 Vennootschap met inkomsten uit kwalificerend intellectueel eigendomsrecht: octrooien (incl. aanvullende beschermingscertificaten en aangevraagde octrooien), kwekersrechten, weesgeneesmiddelen, data- en marktexclusiviteit (regulatorische bescherming), auteursrechtelijk beschermde software ontwikkeld in een R&D-project.

**📋 Voorwaarden**
- 📖 Cumulatief: (1) volle eigendom, mede-eigendom, vruchtgebruik of licentierechten op het IP; (2) IP gekoppeld aan eigen R&D-activiteit (anders nexus-aftrek 0); (3) afzonderlijke boekhouding per IP-actief om netto-inkomsten, R&D-uitgaven en uitbestede kosten te kunnen identificeren; (4) opgave 275 INNO bij aangifte met gedetailleerde berekening.

**👍 Voordeel**
- 📖 Effectief tarief 3,75 % i.p.v. 25 % op netto-innovatie-inkomen. Combineerbaar met andere aftrekken (DBI, investeringsaftrek, ...). Onbeperkt overdraagbaar bij ontoereikende winst. Omzetbaar in belastingkrediet (art. 289decies × 25 %-tarief) — verzilverbaar zelfs bij verlieslijdende vennootschap binnen 5 jaar.

**⚠️ Risico**
- 🔗 Risico van te ruime kwalificatie ('alle software' i.p.v. 'software ontwikkeld in een echt R&D-project'). Bij controle: de fiscus eist documentatie van het R&D-project (projectplan, BELSPO-attest of equivalent, gewerkte uren, kostentoerekening). Geen reëel R&D = aftrek wordt verworpen + nalatigheidsinteresten.

## Bouwstenen

### 📏 85 %-vrijstelling  
_`drempel`_

📖 85 % van de netto-innovatie-inkomsten wordt vrijgesteld; slechts 15 % blijft belastbaar. Combineerd met VenB-tarief 25 %: effectief tarief = 25 % × 15 % = 3,75 % op het netto-innovatie-inkomen. Bij KMO-tarief 20 % op eerste schijf: effectief 3 %.

<small>📚 WIB92 — art. 205/1 §1 — _wettekst_</small>

### 🧮 Nexus-breuk  
_`formule`_

📖 De aftrek wordt vermenigvuldigd met een nexus-breuk: (kwalificerende R&D-uitgaven × 1,3) / totale R&D-uitgaven, met maximum 1. Kwalificerende R&D-uitgaven = eigen R&D + uitbestede R&D aan niet-verbonden partijen. Niet-kwalificerend = uitbestede R&D aan verbonden partijen + acquisitiekosten IP. Zo wordt aftrek beperkt naargelang de eigen substantiële R&D-inspanning.

<small>📚 WIB92 — art. 205/2 §2 — _wettekst_</small>

### 🧮 Netto-innovatie-inkomen  
_`formule`_

📖 Netto-innovatie-inkomen = bruto IP-inkomsten (royalty's, licenties, embedded IP-deel van productverkoop, schadevergoeding bij inbreuk) MIN rechtstreekse kosten van het IP (afschrijving IP-actief, lopende R&D-kosten, betaalde royalty's, ...). Bij negatief netto-inkomen in een jaar: te recapturen in volgende jaren tot het positief is. Aftrek = 85 % × netto-inkomen × nexus.

<small>📚 WIB92 — art. 205/2 §1 — _wettekst_ · WIB92 — art. 205/2 §3 (recapture) — _wettekst_</small>

### ⚙️ Omzetting in belastingkrediet (art. 289decies)  
_`mechanisme`_

📖 Indien de aftrek niet of niet volledig kon worden gebruikt door onvoldoende winst, kan ze worden omgezet in een belastingkrediet = bedrag van niet-gebruikte aftrek × 25 %. Dit krediet is verrekenbaar met VenB van de volgende 5 belastbare tijdperken, en eventueel terugbetaalbaar na uitputting. Belangrijk voor R&D-startups die nog verlieslatend zijn — fiscaal voordeel wordt verzilverd zonder winst.

<small>📚 WIB92 — art. 289decies — _wettekst_</small>

### 📜 Kwalificerende intellectuele eigendomsrechten  
_`regel`_

📖 Kwalificeren: (a) octrooien + aanvullende beschermingscertificaten + aangevraagde octrooien; (b) kwekersrechten; (c) auteursrechtelijk beschermde software ontwikkeld in een R&D-project (R&D-erkenning is belangrijk); (d) weesgeneesmiddelen; (e) data- en marktexclusiviteit voor geneesmiddelen of gewasbeschermingsmiddelen. NIET kwalificerend: handelsmerken, modellen, domeinnamen, knowhow zonder octrooi.

<small>📚 WIB92 — art. 205/1 §2 — _wettekst_</small>

## Voorbeelden

### 💡 TechLab BV — software in R&D-project 🔗

_TechLab BV ontwikkelt een SaaS-platform via een erkend R&D-project. Jaar N: licentie-inkomsten 1.000.000 EUR; directe kosten (afschrijving software 100.000 + lopende R&D 300.000) = 400.000 EUR. Eigen R&D-uitgaven over heel het project: 800.000 EUR; geen uitbestede R&D; geen acquisitie._

**Berekening:**
- Stap 1 — netto-innovatie-inkomen = 1.000.000 − 400.000 = 600.000 EUR.
- Stap 2 — nexus-breuk = min(1, (800.000 × 1,3) / 800.000) = min(1, 1,3) = 1 (volle nexus, want geen niet-kwalificerende uitgaven).
- Stap 3 — aftrek = 85 % × 600.000 × 1 = 510.000 EUR.
- Stap 4 — belastbaar deel innovatie-inkomen = 600.000 − 510.000 = 90.000 EUR.
- Stap 5 — bij VenB 25 %: belasting op innovatie-inkomen = 22.500 EUR i.p.v. 150.000 EUR (zonder aftrek). Effectief tarief = 22.500 / 600.000 = 3,75 %.

→ **Resultaat**: Fiscaal voordeel 127.500 EUR voor één boekjaar. Indien onvoldoende winst om hele aftrek te benutten: rest onbeperkt overdraagbaar of omzetbaar in belastingkrediet 510.000 × 25 % = 127.500 EUR.

<small>📚 WIB92 — art. 205/1-205/2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Oude octrooi-aftrek (80 %) en nieuwe innovatie-aftrek (85 %) verwarren

**Verkeerde assumptie**: Beide regimes zijn identiek; je kan de oude 80 % blijven gebruiken.

**Kernpunt**: De oude octrooi-aftrek (art. 543 WIB92, 80 %) gold ENKEL voor octrooi-inkomsten en heeft GEEN nexus-beperking. Het nieuwe regime (art. 205/1, 85 %) heeft een ruimere kwalificatie (incl. software) maar OOK nexus-correctie. Overgangsregime tot 30-6-2021 voor reeds ontwikkelde IP onder oude regime — daarna verplicht nieuwe regime.

<small>📚 WIB92 — art. 205/1 — _wettekst_ · WIB92 — art. 543 (oud) — _wettekst_</small>

### ⚠️ 'Alle software' kwalificeert

**Verkeerde assumptie**: Software die in de vennootschap ontwikkeld wordt komt automatisch in aanmerking.

**Kernpunt**: Software kwalificeert alleen als ze 'beschermd door auteursrecht' is EN 'ontwikkeld in een R&D-project'. R&D-erkenning is cruciaal: BELSPO-attest of equivalent, project-documentatie, gewerkte uren-registratie. Loutere bedrijfssoftware (CRM, ERP-customizing) zonder echt R&D-karakter = geen aftrek.

<small>📚 WIB92 — art. 205/1 §2 2° — _wettekst_</small>

### ⚠️ Bruto-inkomen i.p.v. netto-inkomen vrijstellen

**Verkeerde assumptie**: 85 % × bruto IP-inkomsten = aftrek.

**Kernpunt**: De aftrek is 85 % × NETTO-innovatie-inkomen = bruto MIN directe kosten (afschrijving IP-actief, lopende R&D-kosten, betaalde royalty's, ...). En vervolgens nog te beperken via nexus-breuk indien er niet-kwalificerende R&D-uitgaven zijn.

<small>📚 WIB92 — art. 205/2 §1 — _wettekst_</small>

## Accountant-perspectieven

### R&D-intensieve vennootschap (biotech/software/deep-tech)

_Accountant van een vennootschap met substantiële R&D-activiteit en IP-portfolio._

#### 💰 Fiscaal adviseur

##### 👣 Opgave 275 INNO opmaken  
_`stap`_

📖 Per kwalificerend IP-actief een aparte berekening: bruto IP-inkomsten, directe kosten, netto-inkomen, R&D-uitgaven (kwalificerend + niet-kwalificerend), nexus-breuk, aftrek 85 %. De opgave 275 INNO wordt elektronisch bij de aangifte VenB ingediend. Documentatie (project-plan, BELSPO-attest, kostentoerekening) gereed houden voor controle.

<small>📚 WIB92 — art. 205/3 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — code 1439 — opgave 275 INNO — _aangifte_</small>

##### 📜 Keuze: aftrek vs belastingkrediet  
_`regel`_

🔗 Voor verlieslatende of nipt-winstgevende vennootschappen: omzetting in belastingkrediet (art. 289decies) heeft voorkeur — krediet is verrekenbaar over 5 jaar en kan terugbetaald worden. Voor winstgevende vennootschappen: aftrek geeft groter onmiddellijk effect (vermindert belastbare basis 1-op-1; belastingkrediet is 25 % van zelfde bedrag). Bij overdraagbare aftrek + voldoende toekomstige winst: aftrek behouden.

<small>📚 WIB92 — art. 289decies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boekhoudkundige isolering van IP-inkomsten  
_`stap`_

🔗 Per kwalificerend IP-actief: aparte analytische rekening voor (a) bruto-inkomsten (royalty's, licenties, embedded IP-deel van productverkoop), (b) directe kosten (afschrijving 213/214, lopende R&D 61x), (c) R&D-uitgaven per categorie (eigen, uitbesteed verbonden, uitbesteed niet-verbonden, acquisitie). Zonder deze isolering: aftrek niet onderbouwbaar bij controle.

<small>📚 WIB92 — art. 205/3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ Σ-keuzekader VenB-voordelen → [[fiscale-voordelen-vennootschap]] _(mag-verwijzen)_
- ↪ Investeringsaftrek voor R&D (cumuleerbaar?) → [[investeringsaftrek]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-voordelen-vennootschap]]
### `triggert`
- [[aangifte-vennootschapsbelasting]] — Code 1439 + opgave 275 INNO in de aangifte VenB.
