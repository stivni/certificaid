---
title: "Forfaitair gedeelte van buitenlandse belasting (FBB)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.I
  - 2.8.VII
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/forfaitair-gedeelte-buitenlandse-belasting.json"
---

_Regime_ · afk: **FBB** · ook: quotité forfaitaire d'impôt étranger · QFIE · buitenlandse-belasting-verrekening

## Definitie

Het Forfaitair Gedeelte van Buitenlandse Belasting (FBB) is de Belgische verrekentechniek om dubbele belasting te vermijden op buitenlandse roerende inkomsten (interesten, royalty's — niet meer voor dividenden sinds AJ 1990). Geregeld in art. 285-289 WIB92. Op het netto-buitenlandse roerend inkomen wordt forfaitair 15/85 (= 17,65 %) als fictieve buitenlandse belasting bijgeteld; dat bedrag wordt vervolgens verrekend met de Belgische vennootschapsbelasting. Een eventueel overschot is in principe niet terugbetaalbaar en gaat verloren.

<small>📖 WIB92 — art. 285 — _wettekst_ · WIB92 — art. 286 — _wettekst_ · WIB92 — art. 287 — _wettekst_</small>

## Substantie

FBB compenseert de fiscale-soevereiniteits-overlap: de bronstaat heft (gedeeltelijk) op het inkomen via een bronheffing, en België belast het zelf integraal omdat de ontvanger Belgisch rijksinwoner-vennootschap is. Door FBB wordt de fiscale lekkage van die dubbele heffing forfaitair opgevangen. Het 15/85-tarief weerspiegelt een veronderstelde gemiddelde buitenlandse bronheffing — niet de werkelijk geheven belasting. Resultaat: een Belgische vennootschap die buitenlandse interest ontvangt, betaalt netto ongeveer de Belgische VenB minus 17,65 %-bijtelling op het netto-bedrag (mits voorwaarden).

<small>🔗 WIB92 — art. 286 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het forfait-karakter (15/85 in plaats van werkelijke buitenlandse belasting) was historisch een vereenvoudigings-mechanisme — geen bewijslast over werkelijk geheven bronheffingen, geen onderhandelingen per land. Sinds de jaren 90 is FBB beperkt tot interesten en royalty's: voor dividenden gebruikt België ofwel de DBI-aftrek (art. 202 WIB92, vrijstellingsmethode) ofwel — bij portfolio-dividenden — geen specifieke verrekening. De rationale is dus tweeledig: (1) bestaande dubbele belasting milderen; (2) administratieve eenvoud door forfait-bedrag in plaats van werkelijke verrekening.

<small>🔗 WIB92 — art. 285 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 285-289; concrete DBV's met FBB-clausule (art. 23B OESO-MV)

Beperkt tot buitenlandse interesten en royalty's. Dividenden hebben hun eigen regime via DBI-aftrek (art. 202 WIB92). Sinds AJ 1990 worden voor dividenden geen FBB meer toegekend.

**✅ Voor**
- 📖 Belgische binnenlandse vennootschap die in haar resultaat buitenlandse interest of royalty's ontvangt — verrekent FBB met haar vennootschapsbelasting.

**📋 Voorwaarden**
- 📖 Cumulatief: (1) het gaat om roerende inkomsten (interest, royalty) — niet dividend; (2) het inkomen is in het buitenland aan een belasting onderworpen (eis van werkelijke buitenlandse belastbaarheid); (3) er is een DBV met FBB-clausule of een unilateraal regime — voor niet-verdragslanden gelden striktere voorwaarden (art. 287 WIB92).

**⛔ Uitsluitingen**
- 🔗 Dividenden: geen FBB sinds AJ 1990; vervangen door DBI-aftrek. Inkomsten uit een land zonder enige effectieve heffing: geen FBB.

## Bouwstenen

### 🧮 Formule FBB (15/85)

Standaardformule (art. 286 WIB92): FBB = 15/85 × netto-buitenlands roerend inkomen. Het netto-bedrag is het bedrag na buitenlandse bronheffing maar voor Belgische belasting. Voorbeeld: netto interest 8.500 EUR — FBB = 8.500 × 15/85 = 1.500 EUR. De FBB wordt zowel bij het belastbaar inkomen geteld (bruto = 8.500 + 1.500 = 10.000 EUR) als verrekend met de eindbelasting. Resultaat: belasting op 10.000, minus verrekening 1.500 EUR.

<small>📖 WIB92 — art. 286 — _wettekst_</small>

### 📜 Verrekening zonder terugbetaling (overschot verloren)

De FBB wordt verrekend met de Belgische vennootschapsbelasting (art. 286 WIB92). Wanneer de FBB hoger is dan de eindbelasting (bv. bij verlieslijdende boekjaren), is het overschot niet-terugbetaalbaar en gaat het verloren — het kan in principe niet worden overgedragen naar volgende boekjaren. Dit verschilt van bijvoorbeeld verliesoverdracht of de DBI-aftrek, die wél overdraagbaar is.

<small>📖 WIB92 — art. 286 — _wettekst_ · WIB92 — art. 292 — _wettekst_</small>

### 📜 Voorwaarde: feitelijke buitenlandse belasting (art. 285)

FBB veronderstelt dat het inkomen in het buitenland aan een belasting van gelijkaardige aard als de Belgische werd onderworpen. Een nominale heffing van 0 % volstaat niet. Praktisch: bij interest uit een vrijgesteld regime in een laag-tarief-jurisdictie kan FBB worden geweigerd. Documentatie van buitenlandse belastbaarheid wordt aanbevolen.

<small>📖 WIB92 — art. 285 — _wettekst_</small>

### 📜 Bezitsduur-vereisten (art. 289)

Anti-misbruik-bepaling (art. 289 WIB92): de FBB wordt geweigerd indien de schuldvordering of het roerend goed niet gedurende een volle ononderbroken periode in volle eigendom werd gehouden. Voorkomt 'dividend stripping' analoog: kortstondige aankoop van een schuldvordering vlak voor coupon-uitkering om FBB te verkrijgen.

<small>📖 WIB92 — art. 289 — _wettekst_</small>

### ⚙️ FBB versus DBI-aftrek (afbakening)

Twee technieken voor buitenlandse vennootschap-inkomsten: FBB (art. 285-289, voor interest en royalty's) en DBI-aftrek (art. 202-205 WIB92, voor dividenden). FBB werkt via opwaardering bruto + verrekening met eindbelasting; DBI werkt via aftrek van 100 % van het netto-dividend van de belastbare grondslag. DBI vereist participatie ≥ 10 % of ≥ 2,5 mio EUR + 1 jaar bezitstermijn — strenger dan FBB. Voor een minderheidsbelegging in buitenlandse interestpapier: FBB. Voor een deelneming met dividenden: DBI.

<small>📖 WIB92 — art. 285 — _wettekst_ · WIB92 — art. 202 — _wettekst_</small>

## Voorbeelden

> [!example]- Belgische BV ontvangt interest op Nederlandse obligatielening
> _Aurelia Holding NV ontvangt in N: bruto interest 10.000 EUR uit Nederlandse obligaties; NL bronheffing 15 % = 1.500 EUR; netto ontvangen 8.500 EUR._
>
> **Berekening:**
>
> - Netto-buitenlands inkomen: 8.500 EUR.
> - FBB = 15/85 × 8.500 = 1.500 EUR.
> - Bruto belastbaar = netto + FBB = 8.500 + 1.500 = 10.000 EUR (= het oorspronkelijke bruto).
> - VenB op 10.000 EUR aan 25 % = 2.500 EUR.
> - Verrekening FBB = 1.500 EUR.
> - Netto BE-belasting = 2.500 − 1.500 = 1.000 EUR.
>
> → **Resultaat**: Totale belastingdruk: 1.500 (NL bronheffing) + 1.000 (BE netto) = 2.500 EUR op 10.000 EUR bruto = 25 % — dezelfde druk als bij een 100 % Belgisch inkomen.
>
> <small>🔗 WIB92 — art. 286 — _wettekst_</small>

## Valkuilen

> [!warning]- FBB toepassen op dividenden
> **Verkeerde assumptie**: Studenten verrekenen 15/85 op buitenlandse dividenden ontvangen door een BE-vennootschap.
>
> **Kernpunt**: Sinds AJ 1990 geen FBB op dividenden — dividenden in vennootschapsbelasting gaan via DBI-aftrek (art. 202 WIB92). De 15/85-FBB-formule geldt uitsluitend voor interest en royalty's.
>
> <small>📖 WIB92 — art. 285 — _wettekst_ · WIB92 — art. 202 — _wettekst_</small>

> [!warning]- FBB-overschot verwachten terug te krijgen
> **Verkeerde assumptie**: FBB die niet kan worden verrekend (door verlies of beperkte VenB) wordt overgedragen of terugbetaald.
>
> **Kernpunt**: FBB-overschot is in principe niet-terugbetaalbaar en gaat verloren als de eindbelasting onvoldoende is. Vooral relevant bij verliesjaren of vennootschappen met massieve aftrekposten. Plan FBB-realisatie in winstjaren.
>
> <small>📖 WIB92 — art. 286 + 292 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vrijstellingsmethode (alternatief — onroerend + actief inkomen) → [[vrijstelling-met-progressievoorbehoud]] _(moet-verwijzen)_
- → Internationale roerende inkomsten (toepassings-context) → [[roerend-inkomen-internationaal]] _(moet-verwijzen)_
- ↪ DBI-aftrek (parallelle techniek voor dividenden) → [[dbi-aftrek]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `vereist`
- [[dubbelbelastingverdrag]] — FBB-clausule (art. 23B OESO-MV) bepaalt of FBB toepasselijk is voor het inkomen uit een specifiek verdragsland.
### `vergelijkbaar_met`
- [[vrijstelling-met-progressievoorbehoud]]
    - **Gelijkenissen**:
        - Beide voorkomen dubbele belasting bij grensoverschrijdende inkomsten
        - Beide vinden hun basis in DBV-art. 23
    - **Verschillen**:
        - Vrijstelling: woonstaat heft niet — vrijgesteld inkomen verhoogt enkel het tarief
        - FBB: woonstaat heft volle belasting, vermindert via verrekening van forfaitaire buitenlandse belasting
        - Vrijstelling typisch voor onroerend + actief inkomen; FBB voor passieve roerende inkomsten
        - Bij FBB kan overschot verloren gaan; bij vrijstelling geen overschot-probleem
    - ⚠️ **Verwarringsrisico**: Beide methodes verschijnen in dezelfde aangifte. Toepassing afhankelijk van type inkomen + DBV-keuze, niet wisselbaar.
- [[dbi-aftrek]]
    - **Gelijkenissen**:
        - Beide milderen Belgische belasting op buitenlandse inkomsten
        - Beide vereisen formele bewijs van buitenlandse onderwerping
    - **Verschillen**:
        - FBB: voor interest + royalty; werkt via verrekening met eindbelasting
        - DBI: voor dividenden; werkt via aftrek van belastbare grondslag (100 %)
        - DBI vereist participatie ≥ 10 % of ≥ 2,5 mio EUR + 1 jaar bezit; FBB niet
        - DBI-overschot is overdraagbaar; FBB-overschot meestal niet
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken DBI op interest of FBB op dividend. Eerst type roerend inkomen kwalificeren (art. 18-20 WIB92).
### `triggert`
- [[roerend-inkomen-internationaal]] — FBB is de standaard verrekentechniek voor buitenlandse roerende inkomsten in VenB.
