---
title: "Personeelskosten"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.M
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/personeelskosten.json"
---

_Balanspost_ · ook: loonkosten · klasse 62 · bezoldigingen sociale lasten en pensioenen

## Definitie

Personeelskosten zijn alle kosten die een onderneming maakt in verband met haar werknemers (niet bedrijfsleiders). Boekhoudkundig komen ze terecht in klasse 62 van het Minimum Algemeen Rekeningenstelsel (MAR): 620 'Bezoldigingen en rechtstreekse sociale voordelen', 621 'Werkgeversbijdragen voor sociale verzekeringen', 622 'Werkgeverspremies voor buitenwettelijke verzekeringen', 623 'Andere personeelskosten', 624 'Pensioenen'. In de resultatenrekening verschijnen ze onder rubriek 'Bezoldigingen, sociale lasten en pensioenen' (rubriek 62 in het schema KB WVV). In de toelichting worden ze gedetailleerd in de sociale balans (jaarrekening-bijlage).

<small>📖 KB 12 september 1983 — MAR — klasse 62 — _kb_ · KB WVV uitvoering — art. 3:90 — _kb_</small>

## Substantie

Personeelskosten zijn vaak een van de grootste kostenposten in de resultatenrekening — voor een dienstenbedrijf kan 60-80 % van de totale kosten in klasse 62 vallen. Voor een productieonderneming wordt een deel van klasse 62 doorgeschoven naar de kostprijs van de productie (allocatie naar voorraad of bedrijfskostprijs). De drie hoofd-onderverdelingen tonen het volledige fiscaal-sociaal kostenplaatje: 620 = bruto loon naar werknemer, 621 = werkgevers-RSZ aan RSZ, 622 = buitenwettelijke voordelen (groepsverzekering, hospitalisatie), 624 = pensioenuitkeringen aan ex-werknemers (bij directe pensioentoezegging). De stagiair moet kunnen onderscheiden tussen klasse 62 (werknemers met arbeidsovereenkomst) en 618 (bedrijfsleiders) — twee verschillende juridisch-fiscale regimes.

<small>🔗 CBN-advies 2016/15 — Boekingen tijdens het boekjaar — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Personeelskosten zitten in een eigen klasse (62) — niet samen met andere bedrijfskosten (klasse 61) — omdat ze voor de jaarrekening apart moeten worden gerapporteerd. De wetgever wil transparantie over de werkgelegenheids- en sociale-kost-impact van een onderneming: hoeveel personen werken er, welke kostencategorieën, welke sociale lasten worden afgedragen. De sociale balans (jaarrekening-bijlage) verdiept dit verder: gemiddeld personeelsbestand, geleverde uren, opleidingskosten, in-/uitstroom. Deze afzonderlijke rapportering ondersteunt zowel werkgevers-statistieken (FOD ECONOMIE), CAO-overleg op sectoraal niveau, als de schuldeisers- en aandeelhoudersbescherming bij analyse van de financiële gezondheid van de onderneming.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB 12 september 1983 (MAR) + KB WVV uitvoering Boek 3

**✅ Voor**
- 🔗 Iedere onderneming die personeel tewerkstelt onder arbeidsovereenkomst — KMO's, grote ondernemingen, vzw's. Boekhoudkundige verplichting via klasse 62; rapporteringsverplichting in jaarrekening + sociale balans (afhankelijk van groottecriteria).

## Bouwstenen

### 💡 620 — Bezoldigingen en rechtstreekse sociale voordelen

Bevat alle brutobezoldigingen aan werknemers: lonen + 13e maand + dubbel vakantiegeld + commissies + premies + voordelen alle aard (VAA bedrijfswagen, GSM, ...). Sub-rekeningen voor segmentering: 6200 (arbeiders), 6201 (bedienden), 6202 (directiepersoneel), 6203 (uitzendkrachten). De totale jaarsom op 620 moet aansluiten met de som van de fiches 281.10 van alle werknemers.

<small>📖 KB 12 september 1983 — MAR — rekening 620 — _kb_ · CBN-advies 2016/15 — Boekingen 620 — _advies_</small>

### 💡 621 — Werkgeversbijdragen voor sociale verzekeringen

Bevat de werkgevers-RSZ-bijdragen (≈ 25 % van bruto, sector-afhankelijk), Fonds voor Sluiting van Ondernemingen, sectorale Sociaal Fonds-bijdragen, jaarlijkse vakantiegeld-bijdrage voor arbeiders (15,2 % × 108 % bruto). Tegen-boeking: 454 (RSZ — totaal werknemer + werkgever).

<small>📖 KB 12 september 1983 — MAR — rekening 621 — _kb_</small>

### 💡 622 — Werkgeverspremies voor buitenwettelijke verzekeringen

Bevat premies voor extra-legale voordelen die niet onder de wettelijke sociale zekerheid vallen: groepsverzekering (2e-pijler pensioen), hospitalisatieverzekering, arbeidsongevallenverzekering (FEDRIS) bovenop wettelijk minimum, ambulante zorgverzekering. Deze voordelen kwalificeren fiscaal vaak gunstig (geen RSZ-werknemer, beperkte VAA-impact).

<small>📖 KB 12 september 1983 — MAR — rekening 622 — _kb_</small>

### 💡 623 — Andere personeelskosten

Verzamelrekening voor heterogene kosten: maaltijdcheques (werkgeversbijdrage), ecocheques, kosten arbeidsgeneeskunde, sociaal secretariaat-fee, opleidingsuren personeel, kantine-toelagen, kerstcadeau-vouchers, ontslagvergoedingen die niet als 'bezoldiging' gekwalificeerd worden, juridische kosten arbeidsrechtbank. Voor een KMO is dit vaak de 'rest-categorie' waar alles in beland dat niet onder 620-622 valt.

<small>🔗 KB 12 september 1983 — MAR — rekening 623 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 624 — Pensioenen

Bevat de pensioenuitkeringen die de onderneming rechtstreeks (= zonder verzekeringsmaatschappij) betaalt aan gepensioneerde ex-werknemers (directe pensioentoezeggingen). Komt minder en minder voor — moderne pensioenplannen lopen via groepsverzekeringen (rekening 622). Bij overgang van directe toezegging naar externe verzekering: provisie pensioen op rekening 16 (voorzieningen voor pensioenen en soortgelijke verplichtingen) wordt geliquideerd.

<small>🔗 KB 12 september 1983 — MAR — rekening 624 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Sociale balans (jaarrekening-bijlage)

Voor middelgrote en grote ondernemingen (boven groottecriteria-drempel) verplichte bijlage bij de jaarrekening: gedetailleerde aantal werknemers + uren + opleidingen + diversiteits-statistieken. Geconsolideerde data wordt door de NBB gepubliceerd voor sectorbenchmarking. De sociale balans is een aanvullende discloseering bovenop klasse 62 — niet een dubbele boeking.

<small>🔗 KB WVV uitvoering — art. 3:104 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Kostenallocatie productie vs administratie

In productieondernemingen wordt een deel van klasse 62 doorgeboekt naar de kostprijs van productie via klasse 90-99 (analytische rekeningen) of via 'doorboeking aan productie' (rekening 71 — wijzigingen voorraden + bestellingen in uitvoering). Concreet: directe productieloons worden in de voorraadwaarde van afgewerkte producten of in 'goederen in bewerking' opgenomen. Resultaat: niet alle klasse 62 verschijnt in de jaarwinst als kost — een deel zit verstopt in de voorraadwaardering op 31/12.

<small>🔗 KB WVV uitvoering — art. 3:24 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Volledige personeelskosten — KMO bediende
> _Aurelia Holding NV — bediende Sven, bruto-jaarloon 42.000 EUR, inclusief 13e maand 3.500 EUR en dubbel vakantiegeld 3.220 EUR (jaarbasis). + VAA bedrijfswagen 4.800 EUR/jaar. + groepsverzekering werkgeversbijdrage 2.000 EUR/jaar. + maaltijdcheques 7 EUR × 220 dagen × werkgeversaandeel 5,91 EUR = 1.300 EUR/jaar._
>
> **📋 Klasse 62 — jaaroverzicht voor Sven**
>
> - {'rekening': '620 — Bezoldigingen', 'bedrag': 46800, 'omschrijving': '42.000 bruto + 4.800 VAA wagen'}
>
> - {'rekening': '621 — Werkgevers-RSZ', 'bedrag': 10500, 'omschrijving': '≈ 25 % × 42.000'}
>
> - {'rekening': '622 — Buitenwettelijke verzekeringen', 'bedrag': 2000, 'omschrijving': 'Groepsverzekering'}
>
> - {'rekening': '623 — Andere personeelskosten', 'bedrag': 1300, 'omschrijving': 'Maaltijdcheques werkgeversaandeel'}
>
> - {'rekening': 'Totaal personeelskost Sven', 'bedrag': 60600, 'omschrijving': 'Volledige loonkost voor werkgever'}
>
> **📒 Maandelijkse loonboeking — gemiddeld**
>
> | Rekening | Debet | Credit | Omschrijving |
> | --- | --- | --- | --- |
> | 620 — Bezoldigingen | 3.900 |  | Bruto-equivalent Sven (3.500 + 1/12 13e + 1/12 dubbel + 1/12 VAA) |
> | 621 — Werkgeversbijdragen sociale verzekeringen | 875 |  | RSZ-werkgever 25 % |
> | 622 — Buitenwettelijke verzekeringen | 166,67 |  | 1/12 groepsverzekering |
> | 623 — Andere personeelskosten | 108,33 |  | 1/12 maaltijdcheques |
> | 453 — Ingehouden voorheffingen |  | 850 | BV |
> | 454 — RSZ |  | 1.332,45 | RSZ werknemer + werkgever |
> | 456 — Provisies bezoldigingen |  | 583,33 | Provisie 13e maand + dubbel vakantiegeld |
> | 455 — Bezoldigingen te betalen |  | 2.284,22 | Netto-loon |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Bedrijfsleidersbezoldiging op 620 boeken (klasse 62)
> **Verkeerde assumptie**: Het loon van de zaakvoerder is ook een 'personeelskost' — boeken op 620.
>
> **Kernpunt**: Bedrijfsleidersbezoldigingen (zaakvoerders, bestuurders, werkende vennoten zonder arbeidsovereenkomst) horen op 618 (Bezoldigingen, premies voor buitenwettelijke verzekeringen, ouderdoms- en overlevingspensioenen van bestuurders, zaakvoerders en werkende vennoten) — NIET op klasse 62. Andere fiche (281.20 ipv 281.10), andere RSZ-regime (zelfstandigen, niet werknemers). Verkeerd boeken = foutieve jaarrekening + fiche-fout.
>
> <small>📖 CBN-advies 2016/15 — Vergoedingen aan bestuurders en werkende vennoten — _advies_</small>

> [!warning]- Maaltijdcheques als bezoldiging op 620 boeken
> **Verkeerde assumptie**: Maaltijdcheques zijn een loon-vorm — boeken op 620.
>
> **Kernpunt**: Maaltijdcheques (en ecocheques, geschenkcheques, sport- en cultuurcheques) horen op 623 (Andere personeelskosten), niet op 620. Reden: ze zijn fiscaal-sociaal anders behandeld (niet-belastbaar binnen plafonds, geen RSZ) en horen niet bij fiche 281.10 bezoldigingen. Boekhoudkundige scheiding ondersteunt deze fiscaal-sociale scheiding.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vakantiegeld-provisie vergeten — onderschatting klasse 62 jaar N
> **Verkeerde assumptie**: Klasse 62 = effectief betaalde loonkost in jaar N.
>
> **Kernpunt**: Volgens accrual-principe moeten provisies voor toekomstige verplichtingen (dubbel vakantiegeld bedienden jaar N+1, eindejaarspremie/13e maand jaar N+1) in jaar N geboekt worden. Vuistregel: 18,2 % × bruto-jaarloon bedienden + sectorale eindejaarspremie. Onderschatting op 31/12 → onderschatting klasse 62 → overschatting winst → IRS/fiscale fraude-risico bij audit.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### KMO-werkgever — jaarrekening en analyse

_De accountant die de jaarrekening opmaakt, klasse 62 analyseert en sociale-balans-bijlage voorbereidt._

#### 📒 Boekhouder

##### 👣 Structurering sub-rekeningen klasse 62

Bij opzet rekeningen-stelsel: gebruik sub-rekeningen voor analytische rapportering. Standaard-segmentering: 6200 arbeiders / 6201 bedienden / 6202 directiepersoneel / 6203 uitzendkrachten. Voor productie-onderneming bovendien: per afdeling (productie, verkoop, administratie). Voor 622: sub per type verzekering (groepsverzekering, hospitalisatie). Dit faciliteert latere analyse, audit, en kostenallocatie naar voorraad.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Volledigheidstest klasse 62

Substantieve audit: (1) aansluiting jaartotaal klasse 62 ↔ som fiches 281.10 van alle werknemers; (2) recompute provisies vakantiegeld en eindejaarspremie/13e maand (18,2 % vuistregel of CBN-formule); (3) test cut-off december/januari — boeking van december-loon en provisies in jaar N, geen schuiven naar jaar N+1; (4) analytische review jaar-over-jaar: % personeelskosten / omzet — abnormale verandering trigger voor follow-up (turnover, herstructurering, fraude); (5) verifieer correcte boeking VAA bedrijfswagen volgens forfaitaire WIB92-formule (CO2 × ouderdom × cataloguswaarde).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Ratio-analyse personeelskosten

Twee belangrijke ratio's bij bedrijfsanalyse: (1) personeelskost-ratio = klasse 62 / omzet — sectoraal vergelijken (NBB-data). Dienstensector typisch 40-70 %, productie 15-30 %, retail 8-15 %. (2) productiviteit = toegevoegde waarde / klasse 62 — geeft aan hoeveel waarde elke euro personeelskost genereert. Trendwaarneming over 3 jaar belangrijker dan absolute waarde. Bij sterke afwijking: graven naar oorzaak (loonsverhogingen niet doorgerekend, overcapaciteit, gunstige sectorale CAO, ...).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Werknemers-vergoedingen Σ (advies-keuze loonpakket) → [[werknemers-vergoedingen]] _(moet-verwijzen)_
- → Loon-en-payroll K-techniek (cascade bruto→netto) → [[loon-en-payroll]] _(moet-verwijzen)_
- → Bedrijfskosten (klasse 60-65 algemeen) → [[bedrijfskosten]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `bevat`
- [[bruto-loon]]
- [[rsz-werkgever]]
- [[dertiende-maand]]
- [[enkel-en-dubbel-vakantiegeld]]
- [[opzegvergoeding]]
- [[outplacementkost]]
### `vergelijkbaar_met`
- [[bedrijfsleidersbezoldiging]]
    - **Gelijkenissen**:
        - Beide zijn bezoldigings-kosten in de resultatenrekening
        - Beide worden op de jaarrekening apart gerapporteerd
    - **Verschillen**:
        - Personeelskosten: klasse 62 (werknemers met arbeidsovereenkomst, RSZ-werknemer/werkgever)
        - Bedrijfsleidersbezoldiging: klasse 618 (zelfstandige bedrijfsleiders, sociale bijdragen zelfstandigen)
        - Fiches: 281.10 voor personeel; 281.20 voor bedrijfsleiders
        - Sociale balans: enkel werknemers in klasse 62
    - ⚠️ **Verwarringsrisico**: Bij familiale vennootschappen waar de zaakvoerder ook 'als bediende' werkt, kan beide regimes naast elkaar lopen — boekhouding moet zorgvuldig scheiden tussen klasse 62 en 618.
