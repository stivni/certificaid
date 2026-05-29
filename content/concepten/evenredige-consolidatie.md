---
title: "Evenredige consolidatie"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.4.I.D
  - 1.4.I.E
  - 1.4.II.C
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/evenredige-consolidatie.json"
---

_Verrichting_ · ook: proportional consolidation · proportionele integratie

## Definitie

Evenredige consolidatie (proportionele integratie) is de techniek waarbij de activa, passiva, opbrengsten en kosten van een gemeenschappelijke dochter (joint venture) niet integraal maar in verhouding tot het deelnemingspercentage in de geconsolideerde jaarrekening worden opgenomen. Lijn per lijn: % van het gebouw, % van de voorraad, % van de omzet, % van de kostprijs. Er ontstaan geen 'belangen van derden' omdat enkel het eigen aandeel verschijnt.

<small>📖 KB-WVV — art. 3:139 — _wettekst_ · WVV — art. 1:20 — _wettekst_</small>

## Substantie

Evenredige consolidatie zit tussen integrale consolidatie (100 %) en vermogensmutatie (één lijn) in. Ze past bij joint ventures waar twee of meer partners gezamenlijke controle uitoefenen — geen van hen kan alleen beslissen, dus integrale opname is niet correct, maar elke partner draagt economisch een aandeel in alle activa en risico's, dus vermogensmutatie is te afstandelijk. Belangrijk: onder IFRS is evenredige consolidatie sinds IFRS 11 (2013) NIET meer toegestaan voor joint ventures — enkel voor 'joint operations' wordt nog pro-rata opgenomen. Onder B-GAAP blijft evenredige consolidatie toegelaten voor gemeenschappelijke dochterondernemingen.

<small>📖 KB-WVV — art. 3:139 — _wettekst_ · IFRS 11 — §24, §B16 — _norm_</small>

## Rationale

Het pro-rata-principe weerspiegelt dat in een joint venture de partner geen exclusieve macht heeft maar wel een evenredig economisch belang. Een 50/50-partner heeft elk 50 % zeggenschap én 50 % blootstelling — evenredige consolidatie maakt deze evenredigheid zichtbaar in de balans. IFRS 11 koos om die transparantie op te geven voor de duidelijkheid van 'joint ventures = aparte entiteit met netto-vorderings-relatie' — een keuze die veel kritiek kreeg maar standaard werd.

<small>🔗 IFRS 11 — §BC22-BC25 — _norm_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB-WVV art. 3:139 (B-GAAP — toegelaten voor gemeenschappelijke dochters). Onder IFRS niet meer toegelaten voor joint ventures sinds IFRS 11 (2013); wel voor joint operations (IFRS 11 §20-21).

Belangrijke divergentie B-GAAP / IFRS. Een groep die rapporteert onder beide regimes kan voor dezelfde joint venture: B-GAAP evenredig + IFRS vermogensmutatie.

**✅ Voor**
- 📖 B-GAAP: gemeenschappelijke dochterondernemingen waarvan het bedrijf nauw geïntegreerd is met de groep (art. 3:139 KB-WVV). IFRS: joint operations (rechten op individuele activa en verplichtingen) — IFRS 11 §20-23.

**🚫 Niet voor**
- 📖 Onder IFRS: joint ventures (§24-25 IFRS 11) — daar is vermogensmutatie verplicht. Onder B-GAAP: gemeenschappelijke dochters waarvan het bedrijf niet nauw geïntegreerd is met de groep mogen alternatief via vermogensmutatie (art. 3:142 § 1 KB-WVV).

## Sub-concepten

### 📦 Techniek pro-rata-opname

#### Definitie

Per balans- en resultatenrekeningpost: vermenigvuldig met het deelnemingspercentage van de groep. Combineer met de cijfers van moeder en andere integraal geconsolideerde dochters. Elimineer intercompany pro-rata (= % aandeel × intercompany-saldo).

<small>📖 KB-WVV — art. 3:139 — _wettekst_ · KB-WVV — art. 3:140 — _wettekst_</small>

### 📦 Geen rubriek 'belangen van derden'

#### Definitie

In tegenstelling tot integrale consolidatie verschijnt geen 'belangen van derden' op het passief. Reden: enkel het eigen aandeel werd opgenomen — er zijn dus geen 'derden' om apart te tonen. Dit maakt evenredige consolidatie technisch eenvoudiger dan integrale: geen minderheidsbelang-berekening op resultaat en eigen vermogen.

<small>🔗 KB-WVV — art. 3:139 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Aurelia heeft 50 % van Vermeer Logistics SRL (joint venture)
> _Aurelia en groep DEF SA bezitten elk 50 % van Vermeer Logistics SRL — gemeenschappelijke controle. Bedrijf is nauw geïntegreerd met logistieke activiteiten van Aurelia. Balans Vermeer Logistics: totaal activa 2.000.000 EUR, eigen vermogen 800.000 EUR, schulden 1.200.000 EUR. Omzet boekjaar: 4.000.000 EUR. Resultaat: 200.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — bepaal pro-rata-aandeel: 50 %.
> - Stap 2 — opname in geconsolideerde balans: 50 % × 2.000.000 = 1.000.000 EUR activa (lijn per lijn verspreid over rubrieken), 50 % × 1.200.000 = 600.000 EUR schulden, 50 % × 800.000 = 400.000 EUR eigen vermogen.
> - Stap 3 — opname in geconsolideerde resultatenrekening: 50 % × 4.000.000 = 2.000.000 EUR omzet, 50 % × kosten, 50 % × 200.000 = 100.000 EUR resultaat.
> - Stap 4 — intercompany met Aurelia: 50 % van elke intercompany-vordering/schuld/omzet/kost elimineren (niet 100 % — anders zou er overcorrectie zijn).
> - Stap 5 — GEEN rubriek belangen van derden (de andere 50 % wordt simpelweg niet opgenomen).
>
> → **Resultaat**: Geconsolideerde balans toont 50 % van Vermeer Logistics gemengd met de cijfers van moeder en andere dochters. Vergelijking met integrale consolidatie: bij integraal zou 100 % opgenomen worden + 50 % als 'belangen van derden'; bij vermogensmutatie zou enkel 400.000 EUR op één lijn 'deelneming' staan.
>
> <small>🔗 KB-WVV — art. 3:139 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Evenredige consolidatie toepassen op een joint venture onder IFRS
> **Verkeerde assumptie**: Een 50/50-deelneming wordt evenredig geconsolideerd, ongeacht het referentiestelsel.
>
> **Kernpunt**: Sinds IFRS 11 (toepassing vanaf 1 januari 2013) is evenredige consolidatie voor joint ventures NIET meer toegestaan — vermogensmutatie verplicht. Enkel joint operations (rechten op specifieke activa/verplichtingen) krijgen nog pro-rata opname. B-GAAP staat evenredig nog wel toe — let op bij groepen die parallel B-GAAP en IFRS rapporteren.
>
> <small>📖 IFRS 11 — §24 — _norm_</small>

> [!warning]- Intercompany op 100 % elimineren bij evenredige opname
> **Verkeerde assumptie**: Intercompany-saldi tussen moeder en gemeenschappelijke dochter worden volledig geëlimineerd.
>
> **Kernpunt**: Bij evenredige consolidatie wordt enkel het pro-rata-aandeel van de joint venture opgenomen — dus enkel het pro-rata-aandeel van de intercompany-saldi moet geëlimineerd worden. Voorbeeld: vordering van Aurelia op Vermeer Logistics = 100 EUR; in geconsolideerde cijfers (50 % evenredig) wordt slechts 50 EUR aan de Vermeer-kant opgenomen → eliminatie van 50 EUR, geen 100 EUR.
>
> <small>🔗 KB-WVV — art. 3:140 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

> [!warning]- 'Belangen van derden' toevoegen bij evenredige consolidatie
> **Verkeerde assumptie**: De andere 50 % moet ergens verschijnen als 'belangen van derden'.
>
> **Kernpunt**: Bij evenredige opname is er geen 'derde-aandeel' om te tonen — de andere helft wordt simpelweg niet opgenomen. 'Belangen van derden' bestaan enkel bij integrale consolidatie waar 100 % is opgenomen + aandeel niet-groepsaandeelhouders apart op passief.
>
> <small>📖 KB-WVV — art. 3:134 — _wettekst_ · KB-WVV — art. 3:139 — _wettekst_</small>

## Accountant-perspectieven

### Joint-venture-partner

_Accountant van een groep die gezamenlijke controle heeft over een vennootschap._

#### 📒 Boekhouder

##### 👣 Evenredige opname uitvoeren

(1) Bekom volledige enkelvoudige jaarrekening van de joint venture; (2) herwerk waarderingsregels naar groepswaarderingsregels (KB-WVV art. 3:120: uniforme waarderingsregels); (3) vermenigvuldig elke post met het deelnemingspercentage; (4) elimineer intercompany pro-rata; (5) integreer in groepscijfers. Geen aparte 'belangen van derden'-berekening nodig.

<small>🔗 KB-WVV — art. 3:120 — _wettekst_ · KB-WVV — art. 3:139-3:140 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Consolidatiemethoden Σ-keuze-kader → [[consolidatiemethoden]] _(moet-verwijzen)_
- ↪ Andere methoden (vergelijking) → [[consolidatiemethoden]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[consolidatiemethoden]]
### `vergelijkbaar_met`
- [[integrale-consolidatie]]
    - **Gelijkenissen**:
        - Beide nemen activa/passiva lijn per lijn op
        - Beide vereisen intercompany-eliminatie
        - Beide passen uniforme waarderingsregels toe
    - **Verschillen**:
        - Integraal: 100 % opname + belangen van derden; evenredig: pro-rata opname + geen belangen van derden
        - Integraal: bij exclusieve controle; evenredig: bij gezamenlijke controle + nauw geïntegreerd bedrijf
        - IFRS staat integrale en vermogensmutatie toe, evenredig niet meer voor JV's
