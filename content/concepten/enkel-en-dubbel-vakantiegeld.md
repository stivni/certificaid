---
title: "Enkel en dubbel vakantiegeld"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/enkel-en-dubbel-vakantiegeld.json"
---

_Regime_ · ook: vakantiegeld · wettelijk vakantiegeld

## Definitie

Het wettelijk vakantiegeld omvat twee componenten: (1) enkel vakantiegeld — het gewone maandloon dat de werknemer doorbetaald krijgt tijdens zijn jaarlijkse vakantiedagen; (2) dubbel vakantiegeld — een bijkomende uitkering die ongeveer overeenkomt met 92 % van het bruto-maandloon, eenmalig uitbetaald in de hoofdvakantiemaand (typisch mei of juni). Het regime verschilt fundamenteel tussen bedienden (werkgever betaalt rechtstreeks) en arbeiders (de Rijksdienst voor Jaarlijkse Vakantie — RJV — betaalt op basis van werkgeversbijdragen). Het vakantiegeld wordt berekend op het loon van het voorgaande dienstjaar (vakantiedienstjaar V-1) — niet op het lopende jaar.

<small>📖 Gecoördineerde wetten van 28 juni 1971 — jaarlijkse vakantie werknemers — art. 1-9 — _wettekst_ · KB 30 maart 1967 — uitvoering wetten jaarlijkse vakantie — art. 38-39 — _kb_</small>

## Substantie

Voor de bediende is het enkel vakantiegeld 'verstopt' in zijn doorlopende maandloon tijdens de vakantie — boekhoudkundig dus niets aparts. Het dubbel vakantiegeld daarentegen is een herkenbare extra storting in mei/juni, vaak gepercipieerd als 'gratis geld'. Voor de arbeider werkt het anders: de werkgever stort de werkgevers-RSZ-bijdrage van 15,2 % (waarvan een groot deel naar de RJV) en de werknemer ontvangt zijn vakantiegeld in mei van de RJV — niet van zijn werkgever. Boekhoudkundig is dit cruciaal: voor bedienden moet de werkgever een provisie aanleggen voor het dubbel vakantiegeld dat in mei zal moeten worden uitbetaald (= verplichte provisie op klasse 456); voor arbeiders niet, omdat de RJV de betaling doet.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Het dubbel vakantiegeld is historisch ingevoerd om de werknemer effectief in staat te stellen op vakantie te gaan zonder financieel ten onder te gaan: het 'extra' bedrag dekt de bijkomende uitgaven van vakantie (huur vakantieverblijf, reis, leisure). Het wordt berekend op het voorgaande jaar (V-1) om de werkgever toe te laten te budgetteren én om nieuwe werknemers niet onmiddellijk recht te geven op een volledig vakantiegeld in het jaar van indiensttreding (= sociaal-rechtelijke buffer tegen 'vakantiegeld-shopping' van werknemers).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Wetten van 28 juni 1971 (gecoördineerd) + KB 30 maart 1967

Stabiel regime sinds decennia; jaarlijkse aanpassing van werkgeversbijdrage RJV via KB.

**✅ Voor**
- 📖 Alle werknemers met een arbeidsovereenkomst onderworpen aan de Belgische sociale zekerheid (bedienden + arbeiders + jongeren-vakantie + Europees-vakantie-regime sinds 2012 voor nieuwe werknemers).

**▶️ Trigger start**
- 📖 Het vakantierecht ontstaat in het vakantiedienstjaar (V-1) op basis van gepresteerde arbeidsdagen + gelijkgestelde dagen. Het wordt opgenomen in het vakantiejaar (V = jaar volgend op V-1). Dubbel vakantiegeld wordt uitbetaald in het vakantiejaar, typisch mei/juni (bedienden via werkgever; arbeiders via RJV).

## Bouwstenen

### ⚙️ Bedienden — uitbetaling door werkgever

Voor bedienden betaalt de werkgever het vakantiegeld zelf. Enkel vakantiegeld = gewoon maandloon door tijdens de vakantiedagen (geen extra cashflow). Dubbel vakantiegeld = bijkomende eenmalige storting, berekend als 92 % van het bruto-maandloon van de hoofdvakantiemaand (typisch mei of juni). De berekeningsbasis is het loon van het voorgaande dienstjaar — pro-rata voor wie geen volledig V-1 heeft gewerkt.

<small>📖 KB 30 maart 1967 — art. 38 — _kb_</small>

### ⚙️ Arbeiders — uitbetaling via RJV

Voor arbeiders verloopt het vakantiegeld via de Rijksdienst voor Jaarlijkse Vakantie (RJV) of een sectoraal Vakantiefonds. De werkgever stort een aparte werkgeversbijdrage (15,2 % van 108 % van het bruto-loon — de '108 %' compenseert het feit dat arbeiders worden uitbetaald per gepresteerde dag) bij elke loonafrekening. In mei betaalt de RJV één bedrag uit dat zowel enkel als dubbel vakantiegeld omvat (typisch 15,38 % × bruto-loon van het vakantiedienstjaar V-1). De werknemer ziet dus geen vakantiegeld op de loonstrook van zijn werkgever.

<small>🔗 Gecoördineerde wetten van 28 juni 1971 — art. 17-19 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Verplichte provisie dubbel vakantiegeld (bedienden)

Op 31/12 moet de werkgever voor zijn bedienden een provisie aanleggen voor het dubbel vakantiegeld dat in het volgende jaar zal moeten worden uitbetaald. CBN-praktijk: 18,2 % van de in jaar N gepresteerde bruto-bezoldigingen (omvat 92 % dubbel vakantiegeld + werkgevers-RSZ + eventuele anciënniteits-vakantie). Boeking op 456 of een sub-rekening provisie vakantiegeld. Niet-aanleggen = onderschatting loonkost in jaar N + overschatting winst.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 BV op dubbel vakantiegeld — afzonderlijke schaal

Op het dubbel vakantiegeld wordt geen reguliere maandelijkse BV-schaal toegepast, maar een afzonderlijke schaal voor exceptionele vergoedingen (KB/WIB92 Bijlage III). Tarief hangt af van het bruto-jaarloon en levert typisch een hoger inhoudingspercentage. Bij arbeiders houdt de RJV de BV zelf in vóór uitbetaling; bij bedienden houdt de werkgever ze in.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Europees vakantie-regime (sinds 2012)

Sinds 2012 moet België een 'Europees vakantie-regime' toepassen voor nieuwe werknemers: in het jaar van indiensttreding moeten zij na 3 maanden anciënniteit reeds vakantiedagen kunnen opnemen, niet pas in jaar N+1. De werkgever moet bij de eerste betaling van vakantiegeld in jaar N+1 het 'Europees vakantiegeld' (= vakantiegeld op basis van de gewerkte maanden in N) verrekenen met het wettelijk vakantiegeld van jaar N+1. Praktisch: ingewikkelde berekening die typisch door het sociaal secretariaat wordt uitgevoerd.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Bediende — dubbel vakantiegeld op bruto € 3.500
> _Sven, bediende bij Aurelia Holding NV, bruto-maandloon € 3.500. Volledig V-1 gewerkt. Dubbel vakantiegeld uitbetaald door werkgever in mei._
>
> **Berekening:**
>
> - Stap 1 — bruto dubbel vakantiegeld: 92 % × 3.500 = 3.220,00 EUR
> - Stap 2 — RSZ-werknemer 13,07 %: 3.220 × 13,07 % = 420,85 EUR
> - Stap 3 — belastbaar: 3.220 − 420,85 = 2.799,15 EUR
> - Stap 4 — BV afzonderlijke schaal exceptionele vergoedingen (indicatief 37 %): ≈ 1.035 EUR — exact tarief Cijferzakboekje
> - Stap 5 — netto dubbel vakantiegeld: ≈ 1.764 EUR
> - Stap 6 — werkgevers-RSZ 25 %: 805 EUR — totale loonkost werkgever ≈ 4.025 EUR
>
> → **Resultaat**: Op 3.220 EUR bruto dubbel vakantiegeld blijft ≈ 1.764 EUR netto over (≈ 55 %). De werkgever heeft hiervoor in jaar N reeds een provisie aangelegd van 18,2 % × bruto-jaarloon (≈ 7.644 EUR voor Sven).
>
> **📒 Jaareinde-provisie dubbel vakantiegeld (CBN-vuistregel 18,2 %)**
>
> _Eind december jaar N voor bediende Sven, bruto-jaarloon 42.000 EUR (12 × 3.500)_
>
> | Rekening | Debet | Credit | Omschrijving |
> | --- | --- | --- | --- |
> | 620 — Bezoldigingen | 6.262,40 |  | 92 % × 6.808 (= 16,2 % bruto-jaarloon, dubbel + enkel-extra) |
> | 621 — Werkgeversbijdragen sociale verzekeringen | 1.381,20 |  | RSZ-werkgever ≈ 22 % over provisie |
> | 456 — Provisie voor te betalen bezoldigingen |  | 7.643,60 | Provisie dubbel vakantiegeld jaar N+1 (≈ 18,2 % × 42.000) |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Provisie voor bedienden vergeten op jaareinde
> **Verkeerde assumptie**: Dubbel vakantiegeld wordt in mei betaald — dus mei-kost, geen impact op de jaarrekening van het voorgaande jaar.
>
> **Kernpunt**: Onjuist. CBN-praktijk en accrual-principe vereisen dat een provisie wordt aangelegd op 31/12 voor het dubbel vakantiegeld dat in jaar N+1 zal worden betaald maar dat economisch toebehoort aan de prestaties van jaar N. Vuistregel: 18,2 % × bruto-jaarloon-bedienden. Onderschatten van deze provisie is een courant audit-bevinding bij KMO-jaarrekeningen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Arbeiders-provisie aanleggen die niet nodig is
> **Verkeerde assumptie**: Voor arbeiders moet je ook een provisie 18,2 % aanleggen.
>
> **Kernpunt**: Onjuist. Voor arbeiders wordt het vakantiegeld door de RJV uitbetaald, niet door de werkgever. De werkgever heeft zijn bijdrage van 15,2 % al maandelijks gestort aan de RSZ — geen toekomstige verplichting meer. Geen provisie nodig. Wel een correcte cut-off van de werkgeversbijdragen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- 92 % is niet 'extra 92 %' — verwarring berekeningsbasis
> **Verkeerde assumptie**: Dubbel vakantiegeld = 192 % van het maandloon (enkel 100 % + dubbel 92 %).
>
> **Kernpunt**: Het 'dubbel vakantiegeld' is een aparte uitkering van 92 % van het bruto-maandloon, bovenop het normaal doorbetaalde maandloon tijdens de vakantieperiode. Het enkel vakantiegeld is dus reeds 'in' het maandloon verstopt — de werkgever betaalt geen extra enkel vakantiegeld. In mei: gewoon maandloon + dubbel vakantiegeld (92 %).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever-cliënt (gemengde tewerkstelling)

_De accountant die jaareinde-werkzaamheden uitvoert bij een werkgever met bedienden en/of arbeiders._

#### 📒 Boekhouder

##### 👣 Jaareinde-provisie dubbel vakantiegeld (bedienden)

Bij elke jaareinde-afsluiting: bereken 18,2 % × bruto-jaarloon van alle bedienden en boek dit als provisie op 456 (debet 620 + 621, credit 456). Bij uitbetaling in mei jaar N+1: provisie liquideren en eventueel verschil door de resultatenrekening laten lopen. Het sociaal secretariaat levert vaak een concreet cijfer aan — controleer dat dit overeenstemt met de vuistregel.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit-controle provisie vakantiegeld

Materiële audit-test op de provisie dubbel vakantiegeld in de jaarrekening: (1) bereken de theoretische provisie als 18,2 % × bruto-jaarloon van alle bedienden in dienst op 31/12; (2) vergelijk met de geboekte provisie; (3) toelichten als afwijking > 5 %. Test verder voor anciënniteits-vakantie en jongerenvakantie (afwijkende percentages voor jonge werknemers). Klassieke audit-bevinding: provisie ontbreekt volledig of is forfaitair op een 'rond' bedrag zonder berekening.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Loon-en-payroll K-techniek (cascade-context) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Werknemers-vergoedingen Σ (alternatieven) → [[werknemers-vergoedingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[loon-en-payroll]]
### `vergelijkbaar_met`
- [[dertiende-maand]]
    - **Gelijkenissen**:
        - Beide zijn extra bezoldigingen bovenop het maandloon
        - Beide volledig RSZ-onderworpen en op afzonderlijke BV-schaal
        - Beide vragen maandelijkse provisioning bij bedienden
    - **Verschillen**:
        - Vakantiegeld: federaal wettelijk verplicht (Wetten 28-06-1971, KB 30-03-1967)
        - Dertiende maand: sectoraal CAO-recht (niet federaal verplicht)
        - Vakantiegeld: betaald in mei/juni; arbeiders via RJV, bedienden via werkgever
        - Dertiende maand: betaald in december, altijd door werkgever
    - ⚠️ **Verwarringsrisico**: Beiden zijn 'eindejaars-extra-loon' in de hoofden van werknemers, maar volgen totaal verschillende juridische en boekhoudkundige regimes.
