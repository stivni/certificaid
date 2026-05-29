---
title: "Activiteitsratio's"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.3.II.C
  - 1.9.V.D
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/activiteits-ratios.json"
---

_Ratio_ · ook: omloopratio's · efficiëntie-ratio's · operating ratios

## Definitie

Activiteitsratio's meten de operationele efficiëntie van een onderneming: hoe snel zet zij haar activa om in omzet en hoe snel rouleren werkkapitaal-componenten? Vier kerngetallen: (1) omloopsnelheid klanten (days sales outstanding, DSO) — gemiddeld aantal dagen tussen factuur en inning; (2) omloopsnelheid leveranciers (days payables outstanding, DPO) — gemiddeld aantal dagen tussen aankoop en betaling; (3) omloopsnelheid voorraad (days inventory outstanding, DIO) — gemiddeld aantal dagen dat voorraad in magazijn ligt; (4) werkkapitaalbehoefte — netto-bedrag aan operationeel gebonden kapitaal (voorraden + handelsvorderingen − handelsschulden). Samen meten ze hoe efficiënt het werkkapitaal draait — directe link met cash-conversion-cycle in liquiditeits-analyse.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Activiteitsratio's zijn de 'verkeersmeters' van de bedrijfsmotor. Twee bedrijven met identieke omzet en winst kunnen totaal verschillen in cash-positie wanneer hun werkkapitaal anders draait: bedrijf A int klanten op 30 dagen en betaalt leveranciers op 60 dagen → genereert cash; bedrijf B int op 120 dagen en betaalt op 30 → cash-honger. Voor de accountant zijn ze diagnostisch: stijgende DSO over jaren wijst op betalings-problemen bij klanten of slappe inningsdiscipline; dalende DPO duidt op vermindering van leverancierskrediet (vaak: leveranciers wantrouwen worden); stijgende DIO op voorraadveroudering of vraagdaling.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Waarom een aparte categorie? Activiteitsratio's vullen het gat tussen winst (resultatenrekening) en liquiditeit (balans-stand). Winst meet wat je verdiende; liquiditeit meet wat je nú kunt betalen; activiteit meet hoe lang het duurt vooraleer winst-op-papier ook werkelijk cash wordt. Centraal mechanisme: cash-conversion-cycle (CCC) = DIO + DSO − DPO. Een korte CCC betekent dat het bedrijf weinig werkkapitaal moet voorfinancieren — een lange CCC dwingt tot externe financiering (bank-lijn, factoring) met bijbehorende kosten. Verbeteringen in activiteitsratio's (sneller innen, langer uitstellen, voorraad versnellen) zijn vaak de eerste turnaround-hefbomen — beter dan kostenbesparing want ze laten omzet en winst intact.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Diagnose werkkapitaal-beheer — typische vraag bij KMO-cliënt: 'waarom zit ik altijd in het rood ondanks winst?'. Activiteitsratio's lokaliseren de bottleneck (voorraad? klanten? leveranciers?).
- 🔗 Kredietverlening + factoring-beoordeling — banken en factoringsmaatschappijen kijken naar DSO als input voor risico-inschatting van handelsvorderingen-portefeuille.
- 🔗 Sector-vergelijking + benchmark-positionering — typisch hoofdstuk in financieel-diagnose-rapport voor cliënt-leiding.

**⚠️ Risico**
- 🔗 Misleiding door eind-jaar-effecten — DSO/DPO/DIO worden vaak vertekend door seizoenseffect (eind december balansdatum bij sterk najaarsseizoen → vertekende voorraad- en vorderingenstanden). Gebruik gemiddelde over 2 perioden of tussentijdse staten.

## Sub-concepten

### 📦 Omloopsnelheid klanten (DSO)

#### Definitie

DSO = (handelsvorderingen × 365) / omzet inclusief btw. Handelsvorderingen = rubriek 40 (handelsdebiteuren ≤ 1 jaar) eventueel gecorrigeerd voor afgeboekte/oninbare bedragen. Omzet incl. btw nodig omdat handelsvorderingen het btw-deel mee dragen — anders systematische over-schatting. Geeft gemiddeld aantal dagen tussen verkoop-factuur en effectieve inning.

<small>🔗 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubriek 40 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

DSO meet de feitelijke betalingsdiscipline van de klanten + de inningsefficiëntie van de eigen administratie. Stijgende DSO is bijna nooit goed nieuws: ofwel verslappende inning, ofwel klanten in betalingsproblemen, ofwel toename van klanten met langere onderhandelde termijnen. In B2B-context typisch 30-60 dagen; in retail (B2C) bijna 0 (cash/kaart). Vergelijken met algemene verkoopvoorwaarden: indien factuur 30 dagen en DSO 75 dagen → 45 dagen achterstand = signaal.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule DSO

DSO (in dagen) = (handelsvorderingen rubriek 40 × 365) / (omzet rubriek 70 × 1,21). De factor 1,21 voegt het 21 %-btw-tarief toe (aanpassen indien andere btw-mix). Een verfijning gebruikt aankoop-gewogen btw-tarief; voor de meeste KMO's is 21 % voldoende benadering.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes per sector

B2B-industrie: 45-75 dagen typisch. B2B-bouwsector: 75-120 dagen (lange werkduur + voorlopige opleveringsstaten). Detailhandel: 5-15 dagen (kaart-betaling). Overheidsklanten: 60-120 dagen (wettelijke betalingstermijn 30 dagen, maar achterstanden frequent). Boven 90 dagen in B2B-industrie: rood signaal, behoefte aan kredietverzekering of factoring.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Omloopsnelheid leveranciers (DPO)

#### Definitie

DPO = (handelsschulden × 365) / aankopen inclusief btw. Handelsschulden = rubriek 44 (leveranciers ≤ 1 jaar). Aankopen = rubriek 60 (handelsgoederen, grondstoffen + hulpstoffen) + rubriek 61 (diensten + diverse goederen). Geeft gemiddeld aantal dagen tussen ontvangst factuur leverancier en betaling.

<small>🔗 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubriek 44 + 60 + 61 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

DPO meet de duur van leverancierskrediet — een gratis financieringsbron. Langer betalen = meer werkkapitaal-financiering door leveranciers, dus minder externe (bank-)financiering nodig. MAAR: te lange DPO wijst op moeilijkheden — leveranciers zullen prijzen verhogen, krediettermijn intrekken, of cash-on-delivery eisen. Sterke ondernemingen onderhandelen lange termijnen (kracht); zwakke ondernemingen worden gedwongen tot vooruitbetaling.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule DPO

DPO (in dagen) = (handelsschulden rubriek 44 × 365) / ((aankopen 60 + diensten 61) × 1,21). De factor 1,21 voor btw 21 % (aanpassen bij andere btw-mix of vrijgestelde transacties).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes

B2B-industrie: 45-75 dagen typisch. Retail (food): 30-60 dagen (snelle rotatie, leveranciers willen snel betaald). Retail (non-food, mode): 90-180 dagen (sterk onderhandeld). Overheidstuig (verplichte wet 21-12-2009): max 30 dagen, anders rente verschuldigd. Boven 90 dagen voor KMO in B2B: alarmsignaal van betalings-problemen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Omloopsnelheid voorraad (DIO)

#### Definitie

DIO = (voorraden × 365) / kostprijs verkopen. Voorraden = rubrieken 30 (grondstoffen + hulpstoffen) + 31 (goederen in bewerking) + 32 (afgewerkt + handelsgoederen). Kostprijs verkopen ≈ rubriek 60 (aankopen) − Δ voorraadwijziging (rubriek 609). Alternatief: rubriek 60 + 61 als ruwe proxy. Geeft gemiddeld aantal dagen dat voorraad in magazijn ligt.

<small>🔗 KB W.Venn. — minimum genormaliseerd rekeningenstelsel — rubrieken 30-32 + 60 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

DIO meet hoe lang het bedrijf zijn kapitaal in voorraad opsluit. Korter = efficiënter werkkapitaal-gebruik + minder veroudering-risico. Stijgende DIO wijst op (a) vraagdaling, (b) overproductie, (c) voorraad-incourantie. Just-in-time-systemen mikken op DIO < 20 dagen. Modeketens (Zara) vermarkten DIO als concurrentieel voordeel: snelle collectiewissel. Diensten-bedrijven hebben DIO ≈ 0 (geen voorraad).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule DIO

DIO (in dagen) = (voorraden 30-32 × 365) / kostprijs verkopen. Equivalente vorm — omloopsnelheid in keer-per-jaar = kostprijs verkopen / voorraden (bv. 6× = elke 60 dagen ververst). Gebruik kostprijs (rubriek 60 + Δ voorraad), NIET omzet — anders inconsistent met voorraad-waardering aan kostprijs.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📏 Benchmark-bandbreedtes

Supermarkten (voeding): 15-30 dagen. Detailhandel non-food: 60-120 dagen. Industriële productie: 45-90 dagen. Bouw (lange werkduur): 90-180 dagen. Auto-dealers: 60-120 dagen. Juweliers, antiquaren: 200+ dagen normaal. Plotse stijging > 30 % t.o.v. vorig jaar: rood signaal — controleer waardeverminderingen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Werkkapitaalbehoefte

#### Definitie

Werkkapitaalbehoefte = voorraden + handelsvorderingen − handelsschulden (eventueel aangevuld met overige operationele kortlopende activa en passiva). Geeft het netto-bedrag aan operationeel werkkapitaal dat permanent voorgefinancierd moet worden vanuit lange-termijn-bronnen (eigen vermogen + lange schuld). Onderscheidt zich van het netto bedrijfskapitaal (NBK = eigen vermogen + LT-schuld − vaste activa) — beide moeten in evenwicht zijn.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

Werkkapitaalbehoefte zegt: 'hoeveel geld zit er permanent gevangen in de operationele cyclus?'. Een groeiende onderneming met stijgende omzet ziet WKB navenant stijgen (meer voorraad nodig, meer klantenkrediet uitstaan) — typische groei-val: 'profitable growth without cash'. Een dalende WKB bij stabiele omzet wijst op operationele efficiëntie-verbetering. De gulden regel: NBK ≥ WKB. Wanneer WKB > NBK → de onderneming financiert haar werkkapitaal met kortlopend krediet (kasfaciliteit, leveranciers-uitstel) = kwetsbaar.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧮 Formule werkkapitaalbehoefte

WKB = voorraden (3) + handelsvorderingen ≤ 1 jaar (40) + overlopende rekeningen actief (490) − handelsschulden ≤ 1 jaar (44) − ontvangen vooruitbetalingen op bestellingen (46) − overlopende rekeningen passief (492) − schulden m.b.t. belastingen, bezoldigingen, sociale lasten (45). Equivalente uitdrukking in dagen: WKB ≈ (DIO + DSO − DPO) × dagomzet incl. btw.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### ⚙️ Werkkapitaalbehoefte vs netto bedrijfskapitaal

NBK = financieringskant (LT-bronnen na dekking vaste activa); WKB = aanwendingskant (operationeel kapitaalbeslag). Gulden regel: NBK ≥ WKB. Wanneer NBK < WKB → kasovertrek of kortlopend krediet financiert structureel werkkapitaal = financieel risico. Trend-analyse over 3-5 jaar laat zien of de bedrijfsgroei structureel meer werkkapitaal vraagt dan de financieringsstructuur kan dragen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Werkkapitaalbehoefte — Zelena Bio NV (20X4)
> _Balansgegevens Zelena Bio NV per 31-12-20X4 (in 1.000 EUR)._
>
> **Berekening:**
>
> - Voorraden (30-32): 1.600
> - Handelsvorderingen ≤ 1 jaar (40): 2.000
> - Handelsschulden ≤ 1 jaar (44): 1.600
> - WKB = 1.600 + 2.000 − 1.600 = 2.000 (1.000 EUR)
> - Omzet 5.700 → dagomzet ≈ 16 / dag
> - WKB in dagen ≈ 2.000 / 16 = 125 dagen werkkapitaal-financiering
>
> → **Resultaat**: WKB van 2.000 KEUR = 125 dagen omzet. Indien netto bedrijfskapitaal 1.500 < WKB 2.000 → 500 KEUR structureel met kortlopend krediet gefinancierd = kwetsbaar. Aanbeveling: voorraadrotatie verhogen (DIO van 162 naar 90 dagen) of klantkrediet verkorten (DSO van 128 naar 60 dagen) of LT-financiering verhogen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Sector-context negeren
> **Verkeerde assumptie**: Een DSO van 90 dagen is altijd te hoog.
>
> **Kernpunt**: Sector-afhankelijk. Bouw, projectengineering en exportondernemingen werken vaak met 90-120 dagen — wettelijke betalingstermijnen, voorlopige opleverstaten, lange productiecycli rechtvaardigen dat. Vergelijken met sector-benchmark (NBB, Companyweb, Graydon) — niet met een universele '60 dagen'-regel.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Btw-correctie vergeten
> **Verkeerde assumptie**: Handelsvorderingen vergelijken met omzet exclusief btw geeft correcte DSO.
>
> **Kernpunt**: Vorderingen DRAGEN het btw-bedrag (de klant moet btw incluis betalen), maar omzet rubriek 70 staat ex-btw. Vergeten van btw-correctie geeft systematisch een 18-21 % te hoge DSO. Standaard: vermenigvuldig omzet met 1,21 (of de toepasselijke btw-mix).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Seizoenseffecten lezen als trends
> **Verkeerde assumptie**: De balans-snapshot op 31-12 geeft een representatief beeld.
>
> **Kernpunt**: Voorraad en vorderingen-standen variëren sterk doorheen het jaar bij seizoens-gevoelige sectoren (kerstartikelen, ijsproducenten, tuinbouw). DSO/DIO berekend op één balansdatum geeft een vertekend beeld. Gebruik gemiddelde over jaar (= (begin + einde) / 2) of tussentijdse staten voor robuust beeld.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Factoring-effect missen
> **Verkeerde assumptie**: Lage DSO = goede inningsdiscipline.
>
> **Kernpunt**: Bedrijven die factoring zonder regres gebruiken zien hun handelsvorderingen verdwijnen van de balans (verkocht aan factor) — DSO daalt artificieel. Lees jaarverslag + toelichting: 'omvang van factoringsovereenkomsten' moet gemeld. Bereken DSO 'pro-forma' inclusief gefactorde vorderingen voor vergelijking met historische perioden.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Ratio-interpretatie cross-categorie (DuPont · cash-conversion-cycle) → [[ratio-interpretatie]] _(moet-verwijzen)_
- → Jaarrekeninganalyse Σ (parent) → [[jaarrekeninganalyse]] _(moet-verwijzen)_
- ↪ Financiële diagnose (geheel-oordeel) → [[financiele-diagnose]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]] — Activiteits-ratio's vormen één van de vier ratio-categorieën binnen jaarrekening-analyse.
### `vereist`
- [[jaarrekening]] — Ratio's berekenen uit balans + resultatenrekening.
### `vergelijkbaar_met`
- [[liquiditeits-ratios]]
    - **Gelijkenissen**:
        - DIO + DSO + DPO zijn componenten van de cash-conversion-cycle in liquiditeit-analyse
    - **Verschillen**:
        - Activiteits-ratios meten operationele efficiëntie per cyclus-onderdeel; liquiditeits-ratios meten netto kortetermijn-betaalkracht
    - ⚠️ **Verwarringsrisico**: Studenten zien 'DSO' soms enkel als liquiditeits-component — het is in eerste instantie een efficiëntie-indicator.
### `beinvloed_door`
- [[rentabiliteits-ratios]] — Hoge ROA hangt deels af van hoge omloopsnelheid (DuPont-decomposition: ROA = nettomarge × omloopsnelheid-totaal-activa).
### `triggert`
- [[kasstroom-analyse]] — Verslechterende activiteits-ratio's leiden tot werkkapitaal-uitbreiding zichtbaar in kasstroom-overzicht (negatieve Δ werkkapitaal in operationele kasstroom).
