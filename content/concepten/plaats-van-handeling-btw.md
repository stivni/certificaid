---
title: "Plaats van handeling — BTW"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.I
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/plaats-van-handeling-btw.json"
---

# Plaats van handeling — BTW

_Kader_

📋 Regeling · Anchors: `2.4.I` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: plaats-van-handeling-regels · lieu de la prestation — **Vertalingen**: fr: lieu de la livraison / prestation

## Definitie

📖 De 'plaats van handeling' is de wettelijk bepaalde plek waar een levering van goederen of een dienstverrichting voor btw-doeleinden geacht wordt te hebben plaatsgevonden — en bepaalt welk land heffingsbevoegd is. Voor goederen volgt de plaats het fysieke goed (art. 14-15 W.BTW: vertrek bij vervoer, ligging bij niet-vervoer); voor diensten geldt sinds 2010 een algemene B2B/B2C-tweedeling (art. 21 W.BTW): B2B = plaats van de afnemer; B2C = plaats van de dienstverrichter. Op deze hoofdregels bestaat een gedetailleerde lijst van uitzonderingen voor onroerende, vervoer-, restaurant-, evenement-, telecom- en elektronische diensten (art. 21bis).

<small>📚 W.BTW — art. 14 + art. 15 + art. 21 + art. 21bis — _wettekst_ · Richtlijn 2006/112/EG — art. 31-59 — _richtlijn_</small>

## Substantie

🔗 De plaats-van-handelingsregels zijn de scharnier van het btw-stelsel bij grensoverschrijdende handel: zij beslissen welk land btw int en tegen welk tarief. Foutieve toepassing leidt tot ofwel dubbele heffing (België én lidstaat-afnemer) ofwel niet-heffing (geen enkel land). De accountant moet voor elke factuur drie vragen beantwoorden: (1) goed of dienst? (2) B2B of B2C? (3) valt onder de algemene regel of onder een specifieke uitzondering? Wanneer de plaats van handeling buiten België ligt, factureert de Belgische belastingplichtige zonder Belgische btw — vaak met vermelding 'btw verlegd' (B2B-dienst) of 'vrijgestelde intracommunautaire levering' (goed).

<small>📚 W.BTW — art. 14-22 + art. 39bis + art. 51, §2, 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het beginsel is verbruikslocalisatie: btw drukt op het land waar het verbruik plaatsvindt — niet waar de productie of dienstverlening haar zetel heeft. Vandaar voor goederen het 'land van bestemming' (bij vervoer) en voor B2B-diensten het 'afnemer-land'. Bij B2C-diensten gold lange tijd het 'oorsprongslandbeginsel' (plaats van dienstverrichter — administratief eenvoudiger), maar voor digitale diensten en e-commerce werd dat sinds 2015 vervangen door het bestemmingslandbeginsel via OSS (One-Stop Shop). De talrijke uitzonderingen — onroerend goed waar het goed ligt, evenement waar het plaatsvindt — volgen telkens een feitelijk-verbruikscriterium.

<small>📚 Richtlijn 2006/112/EG — preambule + art. 31-59 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Plaats van levering — goederen  
_`regime` (subconcept)_

#### Definitie

📖 Goederen volgen de fysieke verplaatsing. Hoofdregels: (a) bij vervoer of verzending: plaats waar de verzending of het vervoer begint (art. 14, §2 W.BTW); (b) bij goederen die niet worden verzonden of vervoerd: plaats waar het goed zich bevindt op het tijdstip van de levering (art. 14, §1); (c) bij installatie of montage: plaats waar het goed wordt geïnstalleerd of gemonteerd (art. 14, §3); (d) bij goederen aan boord van schip, vliegtuig of trein binnen de EU: plaats van vertrek van het personenvervoer (art. 14, §4).

<small>📚 W.BTW — art. 14 — _wettekst_</small>

#### 🧭 Plaats van levering — goederen-scenario's  
_`vuistregel`_

**Substantie**: 📖 Scenario-overzicht voor goederen.

<small>📚 W.BTW — art. 14 + art. 15 — _wettekst_</small>

### 📦 Plaats van dienst — algemene B2B/B2C-regel  
_`regime` (subconcept)_

#### Definitie

📖 Sinds 01-01-2010 (BTW-pakket): hoofdregel voor diensten verschilt naargelang de afnemer. B2B (afnemer is belastingplichtige of voor btw geïdentificeerde rechtspersoon): plaats waar de afnemer de zetel van zijn economische activiteit heeft (art. 21, §2 W.BTW). B2C (afnemer is particulier): plaats waar de dienstverrichter de zetel van zijn economische activiteit heeft (art. 21, §1).

<small>📚 W.BTW — art. 21, §1 + §2 — _wettekst_</small>

#### 🧭 B2B versus B2C — beslismatrix  
_`vuistregel`_

**Substantie**: 📖 Hoofdregel diensten — afhankelijk van afnemer-status.

<small>📚 W.BTW — art. 21 — _wettekst_</small>

### 📦 Uitzonderingen op B2B/B2C-hoofdregel  
_`kader` (subconcept)_

#### Substantie

📖 Art. 21bis W.BTW somt categorieën diensten op waar de algemene regel wordt overschreven door een specifiek criterium (vaak 'plaats van werkelijk gebruik').

<small>📚 W.BTW — art. 21bis — _wettekst_</small>

#### 📜 Tabel uitzonderingen art. 21bis  
_`regel`_

**Substantie**: 📖 Zes categorieën diensten met specifieke plaatsbepaling — geldt zowel B2B als B2C tenzij anders aangegeven.

<small>📚 W.BTW — art. 21bis — _wettekst_</small>

## Valkuilen

### ⚠️ B2B-toets = btw-nummer afnemer

**Verkeerde assumptie**: Een afnemer in het buitenland kwalificeert automatisch als B2B-bedrijf.

**Kernpunt**: Voor B2B-kwalificatie moet de dienstverrichter het btw-identificatienummer van de afnemer verifiëren via het VIES-systeem (EU). Wanneer de afnemer geen geldig btw-nummer heeft, wordt hij voor de plaats-van-handelingsregels behandeld als B2C — dan is de dienst belastbaar in België (B2C-hoofdregel) met Belgische btw. Bij verlegging zonder VIES-verificatie loopt de Belgische dienstverrichter het risico zelf de btw te moeten dragen.

<small>📚 W.BTW — art. 21, §2 — _wettekst_ · Uitvoeringsverordening (EU) 282/2011 — art. 18 — _richtlijn_</small>

### ⚠️ Vastgoed-uitzondering trumpt hoofdregel

**Verkeerde assumptie**: Bij een Belgische makelaar die een Duits gebouw verkoopt voor een Duitse klant: B2B → plaats afnemer = Duitsland.

**Kernpunt**: Onroerende diensten (makelaarij, expertise, werk in onroerende staat, verhuur, hotel) worden altijd belast in het land waar het gebouw ligt (art. 21bis, §2, 1°) — ongeacht B2B of B2C, ongeacht waar leverancier of afnemer gevestigd is. In bovenstaand voorbeeld: Duitse btw, geen Belgische.

<small>📚 W.BTW — art. 21bis, §2, 1° — _wettekst_</small>

### ⚠️ Niet-vergeten: drempel B2C-afstandsverkopen 10 000 EUR

**Verkeerde assumptie**: Webshop in België die naar particulieren in andere EU-landen verkoopt, mag altijd Belgische btw aanrekenen.

**Kernpunt**: Sinds 01-07-2021 geldt voor B2C-afstandsverkopen binnen de EU een uniforme drempel van 10 000 EUR (totale grensoverschrijdende omzet alle lidstaten samen). Onder drempel: Belgische btw. Boven drempel: btw van het bestemmingsland — aangifte via OSS (One-Stop Shop). De drempel geldt cumulatief over alle bestemmingslanden samen.

<small>📚 W.BTW — art. 15, §2 + art. 58quater (OSS) — _wettekst_ · Richtlijn 2006/112/EG — art. 33 + art. 59quater — _richtlijn_</small>

## Syntheses

### 🧩 Synthese  
_`beslisboom`_

Beslisboom om de plaats van handeling voor btw-doeleinden vast te leggen.

## Verder lezen (scope-out)

- → Grensoverschrijdende BTW-regimes (IC-handelingen · OSS · verlegging) → [[btw-grensoverschrijdend]] _(moet-verwijzen)_
- ↪ BTW-tarieven (na bepalen plaats: welk tarief) → [[btw-tarieven]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw-levering-goederen]]
- [[btw-dienstverlening]]
