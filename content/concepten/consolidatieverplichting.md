---
title: "Consolidatieverplichting"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.4.I.C
  - 1.4.II.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/consolidatieverplichting.json"
---

# Consolidatieverplichting

_Regime_

📋 Regeling · Anchors: `1.4.I.C` · `1.4.II.B` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: consolidatieverplichting-bgaap · consolidatieplicht — **Vertalingen**: fr: obligation de consolidation · en: consolidation requirement

## Definitie

📖 De consolidatieverplichting is de juridische plicht voor een moedervennootschap (of de consortium-leden samen) om een geconsolideerde jaarrekening en een geconsolideerd jaarverslag op te stellen wanneer zij — alleen of gezamenlijk — één of meer dochterondernemingen controleert. De plicht volgt uit art. 3:22 e.v. WVV en geldt enkel voor vennootschappen met rechtspersoonlijkheid. De groep wordt vrijgesteld wanneer ze als 'groep van beperkte omvang' kwalificeert op basis van de groottecriteria (art. 3:25 WVV in samenhang met art. 1:24 § 6 WVV).

<small>📚 WVV — art. 3:22 — _wettekst_ · WVV — art. 3:25 — _wettekst_ · CBN-advies 2022/09 — Consolidatieverplichting – Consoliderende vennootschap — _cbn_</small>

## Substantie

🔗 De vraag 'moet ik consolideren?' beantwoord je in twee stappen: (1) is er een groep met controle-relatie? (verticaal: moeder + dochters, of horizontaal: consortium met centrale leiding); (2) is die groep groot genoeg om consolidatieplichtig te zijn? Als één van beide vragen 'nee' is, vervalt de plicht. Voor IFRS-rapporteerders geldt een parallel pad via IFRS 10 (control-test) maar zonder algemene 'kleine groep'-vrijstelling — IFRS 10 § 4 bevat enkel een vrijstelling voor tussenholdings die zelf geconsolideerd worden door een hoger niveau dat IFRS-conforme cijfers publiceert.

<small>📚 WVV — art. 3:22-3:25 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De wetgever wil dat groepen die een wezenlijke economische voetafdruk hebben (omzet · personeelsbestand · balanstotaal boven drempels) transparante groepscijfers publiceren. Kleine familiale groepen krijgen vrijstelling om de administratieve last evenredig te houden. De plicht ligt bij de moedervennootschap (of, bij consortium, collectief bij de leden) omdat zij economisch het 'gezicht' van de groep zijn naar derden — schuldeisers, fiscus, leveranciers.

<small>📚 WVV — art. 3:25 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WVV art. 3:22 e.v. (sinds 1 januari 2020). Drempelwaarden 'kleine groep' verhoogd door wijziging 2023 in uitvoering van Richtlijn (EU) 2023/2775.

Drempels groottecriteria (art. 1:24 § 6 WVV — geconsolideerde of geaggregeerde basis): 50 werknemers, balanstotaal en omzet (geïndexeerd; exacte bedragen in Cijferzakboekje).

**✅ Voor**
- 📖 Belgische moedervennootschappen met rechtspersoonlijkheid die één of meer dochterondernemingen controleren. Ook consortium-leden gezamenlijk wanneer zij onder centrale leiding staan.

**🚫 Niet voor**
- 📖 Vzw's, ivzw's, stichtingen en maatschappen — zij kunnen nooit moedervennootschap zijn. Zelfs als zij feitelijk een groep controleren (bv. familiale stichting boven een verticale groep) berust de consolidatieplicht bij de onderliggende vennootschappen.

**⛔ Uitsluitingen**
- 📖 Vrijstelling 'groep van beperkte omvang' (kleine groep, art. 3:25 WVV): wanneer de groep op geconsolideerde of geaggregeerde basis niet meer dan één van de drempelwaarden van art. 1:24 § 6 WVV overschrijdt. Vrijstelling vervalt voor groepen waarvan minstens één onderneming een organisatie van openbaar belang is.
- 📖 Sub-consolidatie-vrijstelling (art. 3:26 WVV): een Belgische tussen-moedervennootschap kan vrijgesteld worden van eigen consolidatieplicht wanneer zij zelf geconsolideerd wordt door een Europese moeder die geconsolideerde cijfers volgens gelijkwaardige normen publiceert.

**▶️ Trigger start**
- 🔗 De plicht ontstaat vanaf het boekjaar waarin de moedervennootschap voor het eerst voldoet aan de combinatie 'controle bestaat' + 'groep niet meer klein'. Dit kan gebeuren door (1) verwerving van een dochter, (2) interne groei waardoor groep-drempels overschreden worden, of (3) wegvallen van een vrijstellingsgrond (bv. nieuwe organisatie van openbaar belang).

## Sub-concepten

### 📦 B-GAAP-spoor: controle + groottedrempel  
_`kader` (subconcept)_

#### Definitie

📖 Onder B-GAAP geldt de plicht zodra (1) er minstens één dochteronderneming wordt gecontroleerd EN (2) de groep groottedrempels overschrijdt. Drempelwaarden worden geconsolideerd of geaggregeerd berekend (art. 1:24 § 6 + § 7 WVV) zodat het ontwijken van consolidatie via opsplitsing in kleinere vennootschappen niet werkt.

<small>📚 WVV — art. 3:25 — _wettekst_ · WVV — art. 1:24 § 6 + § 7 — _wettekst_ · CBN-advies 2022/03 — Consolidatie moedervennootschap — _cbn_</small>

### 📦 IFRS-spoor: IFRS 10 control + EU-IAS-verordening  
_`kader` (subconcept)_

#### Definitie

📖 Voor entiteiten die onder de IAS-verordening (EG) 1606/2002 vallen (beursgenoteerde groepen + bepaalde banken/verzekeraars), geldt de IFRS-plicht: een moeder consolideert wanneer zij control heeft over een investee (IFRS 10 § 6). Control bestaat uit drie ingrediënten: power, exposure to variable returns, en de koppeling tussen power en returns. IFRS 10 § 4 bevat een 'investment entity'-uitzondering en een vrijstelling voor tussenholdings die op hoger niveau IFRS-geconsolideerd worden.

<small>📚 IFRS 10 — Geconsolideerde jaarrekening — §4-7 — _norm_ · Verordening (EU) 2023/1803 — IFRS 10 — _wettekst_</small>

## Voorbeelden

### 💡 Familiale groep onder drempel — vrijstelling 🔗

_Aurelia Holding NV bezit 100 % van Zelena Bio NV en 80 % van Vermeer Verpakking BV. Geconsolideerd: balanstotaal 5 mio EUR, omzet 8 mio EUR, gemiddeld 35 werknemers. Geen organisatie van openbaar belang in de groep._

Toets aan groottecriteria (geconsolideerd, exacte drempels in Cijferzakboekje):
- werknemers <= 50 OK
- balanstotaal onder drempel OK
- omzet onder drempel OK

Resultaat: groep van beperkte omvang (art. 1:24 § 6 WVV). Aurelia is vrijgesteld van consolidatieplicht (art. 3:25 WVV). Wel consolidatiekring blijven monitoren — vrijstelling kan vervallen bij groei.

<small>📚 WVV — art. 3:25 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Horizontale groep — consortium-plicht 📖

_Vennootschap X (15 werknemers, balans 3 mio) en vennootschap Y (40 werknemers, balans 12 mio) hebben dezelfde meerderheid van bestuurders. Geen moeder-dochter-relatie tussen X en Y. Geen overige dochters._

X + Y = consortium (gezamenlijke meerderheid van bestuurders = onweerlegbaar vermoeden centrale leiding, art. 1:19 WVV).
Geconsolideerd: 55 werknemers, 15 mio balanstotaal — boven werknemers-drempel (>50).
Resultaat: plicht ontstaat gezamenlijk bij X en Y (art. 3:24 lid 2 WVV). Beide consoliderende vennootschap; opmaakplicht en publicatieplicht gemeenschappelijk.

<small>📚 CBN-advies 2022/09 — Voorbeeld 1 — _cbn_</small>

## Valkuilen

### ⚠️ Groottedrempel op enkelvoudige basis berekenen

**Verkeerde assumptie**: De drempels werknemers/omzet/balans van art. 1:24 WVV gelden voor de moedervennootschap alleen.

**Kernpunt**: Voor de consolidatieplicht worden de drempels geconsolideerd of geaggregeerd berekend (art. 1:24 § 6 WVV). Een 'kleine' moedervennootschap kan toch consolidatieplichtig zijn omdat haar dochters bij optelling de drempels doen springen.

<small>📚 WVV — art. 1:24 § 6 + § 7 — _wettekst_ · CBN-advies 2022/03 — Consolidatie moedervennootschap — _cbn_</small>

### ⚠️ Sub-consolidatievrijstelling automatisch veronderstellen

**Verkeerde assumptie**: Een Belgische tussen-moeder onder een EU-groepsmoeder hoeft nooit zelf te consolideren.

**Kernpunt**: Art. 3:26 WVV vrijstelling kent strikte voorwaarden: (1) hogere moeder consolideert volgens gelijkwaardige normen; (2) cijfers worden in België neergelegd; (3) minderheidsaandeelhouders verzoeken niet om Belgische consolidatie. Onbeursgenoteerd niveau van hogere moeder of aandeelhouders met 10 % of meer kunnen de vrijstelling tegenhouden.

<small>📚 WVV — art. 3:26 — _wettekst_</small>

### ⚠️ Plicht enkel bij meerderheid van aandelen

**Verkeerde assumptie**: Wie geen meerderheid van aandelen heeft, hoeft niet te consolideren.

**Kernpunt**: Het criterium is controle (art. 1:14 WVV), niet aandelenmeerderheid. Controle in feite (stemrechten-meerderheid op laatste twee AVG's, aanstelling meerderheid van bestuurders, statutaire bevoegdheid) volstaat — ook met < 50 % aandelen. Een minderheidsaandeelhouder kan dus consolidatieplichtig zijn.

<small>📚 WVV — art. 1:14 — _wettekst_ · WVV — art. 1:15 — _wettekst_</small>

## Accountant-perspectieven

### Moedervennootschap

_De accountant die de moeder bijstaat bij het bepalen of consolidatie verplicht is._

#### 📒 Boekhouder

##### 👣 Jaarlijkse toets consolidatieplicht  
_`stap`_

🔗 Voor elke moedervennootschap op balansdatum: (1) inventariseer alle deelnemingen + bestuursmandaten + aandeelhoudersovereenkomsten; (2) bepaal welke leiden tot controle (art. 1:14 + 1:15 WVV); (3) bereken geconsolideerde of geaggregeerde groottedrempels (omzet, balanstotaal, werknemers); (4) check sub-consolidatie-vrijstelling (art. 3:26); (5) documenteer het resultaat — plicht of vrijgesteld + grond.

<small>📚 WVV — art. 3:22-3:26 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit volledigheid consolidatieplicht  
_`stap`_

🔗 De commissaris verifieert onafhankelijk de drempel-berekening en zoekt naar 'verzwegen' dochters: deelnemingen die niet als zodanig gerapporteerd worden maar feitelijk gecontroleerd. Aandachtsgebieden: SPV's, optie-/voorkooprechten, management-contracten, joint ventures die de facto controle geven. Niet-naleving van de plicht = inbreuk op WVV met mogelijk weigering van commissarisoordeel.

<small>📚 ISA 600 — Audits of Group Financial Statements — §21-23 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij groei langs drempel  
_`vuistregel`_

🤖 Wanneer een familiale groep dicht bij de drempelwaarden zit, vroegtijdig waarschuwen: in het jaar van drempel-overschrijding moet een consolidatie-infrastructuur (group reporting tools, uniforme waarderingsregels, intercompany-administratie) operationeel zijn. Voorbereiden vereist 6 à 12 maanden — niet wachten tot de plicht aanslaat.

<small>📚 claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Controle-test (basis voor wie-in-kring) → [[controle-bij-consolidatie]] _(moet-verwijzen)_
- → Consolidatiekring (wie zit erin operationeel) → [[consolidatiekring]] _(moet-verwijzen)_
- ↪ Groottecategorie-vennootschap (drempels groot/klein) → [[groottecategorie-vennootschap]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `vereist`
- [[controle-bij-consolidatie]]
### `triggert`
- [[consolidatiekring]]
