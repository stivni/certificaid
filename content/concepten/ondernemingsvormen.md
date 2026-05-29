---
title: "Ondernemingsvormen"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - entiteit
ankers:
  - 3.0.I
  - 3.0.I.A
  - 3.0.I.B
  - 3.0.I.C
  - 3.0.taak.1
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/ondernemingsvormen.json"
---

_Kader_ · ook: vennootschapsvormen · rechtsvormen · juridische ondernemingsvormen · business entity types · company forms

## Definitie

Ondernemingsvormen zijn de juridische verschijningsvormen waarin een economische activiteit in België kan worden uitgeoefend. Het Wetboek van vennootschappen en verenigingen (WVV, Wet 23 maart 2019) somt limitatief op (art. 1:5 + 1:6): één vennootschap zonder rechtspersoonlijkheid (maatschap), zes vennootschappen met rechtspersoonlijkheid (VOF, CommV, BV, CV, NV, SE, SCE), en de verenigingen (VZW, IVZW). Naast die WVV-vormen blijft de eenmanszaak (natuurlijke persoon die zelfstandig handelt — geen aparte rechtspersoon) bestaan. De vorm bepaalt vier kern-eigenschappen: (1) al dan niet eigen rechtspersoonlijkheid, (2) aansprakelijkheid van de vennoten/aandeelhouders, (3) kapitaal-/inbrengvereisten, (4) bestuurs- en winstdelings-regime.

<small>📖 WVV — art. 1:5 — _wettekst_ · WVV — art. 1:6 — _wettekst_</small>

## Substantie

Praktisch: vóór een onderneming start moet een rechtsvorm gekozen worden — de keuze bepaalt mee de boekhoudplicht (dubbel vs vereenvoudigd, CBN-advies 2019/11), de fiscale aanknoping (PB voor eenmanszaak/maatschap; VenB voor BV/NV/CV/CommV/VOF), de aansprakelijkheid bij faillissement en de mate van procedure-zwaarte bij oprichting. WVV 2019 reduceerde drastisch het aantal toegelaten vormen (afschaffing CVOA, ESV, Comm.VA, LV, S-BVBA): wat vóór 2019 een 'kapitaalvennootschap' (BVBA-NV) heette is nu een BV/NV, waarbij de BV haar minimumkapitaal-vereiste verloor (kapitaalloos — art. 4:13 MvT) en de NV haar 61.500 EUR-vereiste behield (art. 7:2).

<small>🔗 WVV — art. 1:5 — _wettekst_ · WVV — art. 4:13 — _wettekst_ · CBN 2019/11 — Beoogde personen - rechtsvorm — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De ratio legis van de WVV-reductie (15→7 vennootschapsvormen) is tweevoudig: (1) eenvoudig en aantrekkelijk Belgisch vennootschapsrecht voor inwerving van buitenlandse investeringen, en (2) modernisering — kapitaalbescherming als bescherming-via-vermogen is achterhaald, een groot deel van de NV-regels werd in een meer flexibele BV-versie gegoten als 'default-vorm'. De vorm-keuze faciliteert vier doelen: vermogensafscheiding (rechtspersoonlijkheid), aansprakelijkheids-beperking (kapitaalvennootschappen), winstdelings-organisatie (statuten), en fiscale optimalisatie (PB vs VenB).

<small>🔗 WVV-MvT — Inleidende bepalingen — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: Wet 23 maart 2019 houdende het Wetboek van vennootschappen en verenigingen (BS 4 april 2019)

WVV is van toepassing sinds 1 mei 2019 voor nieuwe vennootschappen; bestaande vennootschappen moesten uiterlijk 1 januari 2024 hun statuten aanpassen. Vroegere W.Venn.-vormen (BVBA, CVOA, Comm.VA, LV, S-BVBA) zijn vanaf 1 januari 2024 niet langer toegestaan — automatische omzetting naar de dichtstbijzijnde WVV-vorm.

**✅ Voor**
- 🔗 Elke beslissing om een nieuwe activiteit op te starten — vóór registratie KBO + statuten-akte moet de rechtsvorm gekozen worden, want die bepaalt notariële vereisten, financieel plan, aansprakelijkheidsrisico en fiscale opvolging.

**▶️ Trigger start**
- 📖 Trigger 1 — start activiteit: keuze tussen eenmanszaak (PB) en vennootschap (VenB). Trigger 2 — herstructurering: omzetting van bestaande vorm (art. 14:2 WVV behoudt rechtspersoonlijkheid). Trigger 3 — opvolging/uittreding: omzetting bv. naar BV om uittreding aandeelhouder mogelijk te maken.

**👍 Voordeel**
- 🔗 Door een passende rechtsvorm te kiezen: (a) aansprakelijkheid begrenzen tot het ingebrachte vermogen (kapitaalvennootschappen — niet bij maatschap/VOF), (b) fiscaal optimaliseren via VenB-tarief (25% standaard, 20% KMO-tarief op eerste 100.000 EUR voor kwalificerende kleine vennootschappen, art. 215 WIB92), (c) continuïteit verzekeren (rechtspersoonlijkheid overleeft individuele vennoot), (d) groei en kapitaalophaling mogelijk maken (NV — publieke uitgifte aandelen).

**⚠️ Risico**
- 🔗 Verkeerde vorm-keuze leidt tot: (a) onnodige administratiekost (NV-procedure waar BV volstaat), (b) onbeperkte hoofdelijke aansprakelijkheid bij maatschap/VOF — privévermogen vennoot aansprakelijk, (c) gemiste KMO-tarief door slechte invulling 'kleine vennootschap'-voorwaarden (art. 1:24 WVV), (d) ongewenste fiscale aanknoping (maatschap = transparant → fiscaliteit op niveau vennoot in PB).

## Sub-concepten

### 📦 WVV-systematiek

#### Definitie

Het WVV (Wet 23 maart 2019) is opgebouwd in 18 boeken. Boek 1 (Inleidende bepalingen) bevat de fundamentele definities en de limitatieve lijst van rechtsvormen (art. 1:5 vennootschappen + 1:6 verenigingen). Boeken 2-4 zijn algemene bepalingen die op alle vennootschappen toepasselijk zijn (Boek 2 — gemeenschappelijke bepalingen rechtspersonen; Boek 3 — jaarrekening + controle; Boek 4 — maatschap, VOF, CommV). Boeken 5-7 regelen elk een kapitaalvennootschap (5 BV · 6 CV · 7 NV). Boeken 8-11 betreffen erkenningen + verenigingen (Boek 9 VZW · 10 IVZW · 11 stichtingen). Boeken 12-14 herstructurering (fusie, splitsing, omzetting). Boek 15 SE/SCE-Europese vormen. Boek 16-18 ontbinding en handhaving.

<small>📖 WVV — structuur — boeken 1-18 — _wettekst_ · WVV-MvT — Inleidende bepalingen — _wettekst_</small>

#### Substantie

Het WVV vervangt twee historische wetboeken: het Wetboek van vennootschappen (W.Venn., 1999) en de wet van 27 juni 1921 betreffende de VZW's, IVZW's en stichtingen. Bij verwijzingen in oude akten of rechtspraak naar 'art. 52 W.Venn.' moet de stagiair terugvertalen naar het WVV-equivalent (vaak art. 4:14 WVV). De MvT bij het WVV is een belangrijk interpretatie-instrument omdat de wettekst beknopt is en de MvT de ratio legis expliciteert.

<small>🔗 WVV-MvT — Art. 4:13 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Fiscale keuze rechtsvorm

#### Definitie

De fiscale aanknoping volgt rechtstreeks uit de rechtsvorm. Eenmanszaak + maatschap zijn transparant → PB op het niveau van de natuurlijke-persoon-ondernemer/vennoot (art. 23 WIB92 — beroepsinkomsten). Vennootschappen met rechtspersoonlijkheid (BV/NV/CV/CommV/VOF/SE/SCE) zijn VenB-plichtig (art. 179 WIB92), in principe tegen 25 % (art. 215 WIB92), met een KMO-tarief van 20 % op de eerste 100.000 EUR winst voor kwalificerende kleine vennootschappen (cumulatieve voorwaarden — zie verlaagd-tarief-kleine-vennootschap). De winst van een vennootschap kan vervolgens uitgekeerd worden via dividend (RV 30 % of 15 % onder VVPRbis) of via bezoldiging zaakvoerder (PB-progressief + sociale bijdragen).

<small>📖 WIB92 — art. 179 — _wettekst_ · WIB92 — art. 215 — _wettekst_ · WIB92 — art. 23 — _wettekst_</small>

#### Rationale

Kantelpunt eenmanszaak → vennootschap ligt voor de meeste cliënten rond een netto-winst van 35.000-45.000 EUR/jaar (orde van grootte — afhankelijk van gezinssituatie, sociale bijdragen, dividend-strategie). Beneden dit niveau is de PB-progressie aanvaardbaar en wegen de oprichtings- + boekhoud-kost van een vennootschap niet op tegen de fiscale besparing. Boven dit niveau biedt de VenB-flat-rate (25 % of 20 % KMO) substantieel voordeel.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Wanneer welke vorm

#### Definitie

Keuze-criteria voor de stagiair, getrapt: (1) Solo-ondernemer met beperkt risico → eenmanszaak (PB) bij beperkte winst, BV bij groei + aansprakelijkheidszorg. (2) Twee+ vennoten met operationele samenwerking → BV als default (kapitaalloos + soepele uittreding); NV alleen bij grote schaal / publieke uitgifte. (3) Coöperatief doel (samenwerking aan een gedeeld voordeel) → CV (vennoot mag verplicht zijn lid; coöperatief Boek 6 WVV). (4) Familiaal vermogensbeheer zonder activiteit naar buiten → maatschap (transparant, discreet, geen publicatieplicht jaarrekening). (5) Niet-winstgevende activiteit (cultuur, sport, verzorging) → VZW. (6) Hybride zelfstandige-met-actief-vennoot → CommV (combinatie van actieve gecommanditeerde-vennoot met onbeperkte aansprakelijkheid en stille commanditaire vennoten met beperkte aansprakelijkheid).

<small>🔗 WVV — art. 1:5 — _wettekst_ · WVV — art. 6:1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### ⚙️ Vergelijkingsmatrix 7 ondernemingsvormen

Synthetische matrix van de 7 hoofdvormen langs 5 dimensies. De matrix is een snel-overzicht; per cel wordt verwezen naar het eigen record voor de detail-regeling en uitzonderingen.

<small>🔗 WVV — art. 1:5 — _wettekst_ · WVV — art. 4:13 — _wettekst_ · WVV — art. 7:2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Dimensie kapitaal/inbreng — cascade na WVV

WVV schafte het minimumkapitaal-concept af voor de BV (vroegere BVBA had 18.550 EUR minimumkapitaal; nu enkel een 'toereikend aanvangsvermogen' — art. 5:3 WVV). De NV behoudt haar minimumkapitaal van 61.500 EUR volstort bij oprichting (art. 7:2 WVV). De CV heeft net als de BV geen minimumkapitaal meer. VOF, CommV en maatschap hadden nooit een wettelijk minimum. Het verdwijnen van het minimumkapitaal in de BV wordt gecompenseerd door (a) een verplicht financieel plan met onderbouwde liquiditeits- + solvabiliteitsprognoses (art. 5:4), (b) een striktere uitkeringstoets vóór winstuitdeling (dubbele toets: netto-actief + liquiditeit, art. 5:142-143), en (c) een bestuurdersaansprakelijkheid bij kennelijk-grove-fout (faillissement binnen 3 jaar na oprichting met ontoereikend aanvangsvermogen — art. 5:16).

<small>📖 WVV — art. 4:13 — _wettekst_ · WVV — art. 5:3 — _wettekst_ · WVV — art. 5:4 — _wettekst_ · WVV — art. 5:142 — _wettekst_ · WVV — art. 7:2 — _wettekst_</small>

### 📜 Dimensie aansprakelijkheid — drie niveaus

Drie aansprakelijkheidsregimes: (1) Onbeperkte hoofdelijke aansprakelijkheid op het volledige privévermogen — maatschap (art. 4:14), VOF, en gecommanditeerden in een CommV. (2) Beperkt tot de inbreng — aandeelhouders van BV/NV/CV en commanditaire vennoten in een CommV. (3) Geen persoonlijke aansprakelijkheid — leden van een VZW (zij hebben geen aandeel, geen inbreng-verplichting). Voor bestuurders bestaat een eigen aansprakelijkheidsregime onder boek 2 WVV (zie record bestuurdersaansprakelijkheid) — beperkt door wettelijke caps die per vennootschapsgrootte verschillen (art. 2:57 WVV).

<small>📖 WVV — art. 4:14 — _wettekst_ · WVV — art. 5:1 — _wettekst_ · WVV — art. 2:57 — _wettekst_</small>

### 📜 Dimensie fiscale aanknoping

Twee fiscale categorieën: (a) transparante vormen — eenmanszaak (art. 23 WIB92), maatschap (art. 29 WIB92): de winst wordt rechtstreeks belast bij de natuurlijke persoon / vennoten in PB, progressief tarief tot 50 %. (b) VenB-plichtige vormen — alle andere WVV-vennootschappen met rechtspersoonlijkheid (BV/NV/CV/VOF/CommV/SE/SCE), tegen 25 % standaardtarief of 20 % KMO-tarief op eerste 100.000 EUR winst (art. 215 WIB92, mits voorwaarden art. 1:24 WVV-klein vervuld + bezoldiging minimum aan minstens één bedrijfsleider). VZW: rechtspersonenbelasting (RPB, art. 220 WIB92) — beperkt tot bepaalde inkomsten — of VenB indien commerciële activiteit overweegt (art. 181-182).

<small>📖 WIB92 — art. 23 — _wettekst_ · WIB92 — art. 29 — _wettekst_ · WIB92 — art. 179 — _wettekst_ · WIB92 — art. 215 — _wettekst_ · WIB92 — art. 220 — _wettekst_</small>

### 📜 Dimensie boekhoudplicht — vereenvoudigd vs dubbel

Een BV, CV, NV, SE of SCE moet steeds een dubbele boekhouding voeren — ongeacht omzet. Vereenvoudigde boekhouding (kasdagboek, aankoopdagboek, verkoopdagboek + inventarisboek) is voorbehouden aan: natuurlijke personen (eenmanszaak), organisaties zonder rechtspersoonlijkheid, VOF en CommV, mits de omzet beneden 500.000 EUR (excl. BTW) blijft.

<small>📖 CBN 2019/11 — Beoogde personen - rechtsvorm — _advies_ · WER — art. III.85 — _wettekst_</small>

### 📜 Behoud van rechtspersoonlijkheid bij omzetting

Wanneer een vennootschap een andere WVV-rechtsvorm aanneemt (omzetting), blijft haar rechtspersoonlijkheid onveranderd voortbestaan in de nieuwe vorm. Geen vereffening, geen nieuwe rechtspersoon, fiscale continuïteit. Praktisch: een vroegere BVBA werd in 2024 automatisch BV; een NV die omschakelt naar BV behoudt haar KBO-nummer + activa/passiva + lopende contracten.

<small>📖 WVV — art. 14:2 — _wettekst_</small>

## Voorbeelden

> [!example]- Keuze: 2 vennoten starten een ICT-consultancy
> _Alex en Brigitte willen samen een ICT-consultancy starten. Beiden brengen 15.000 EUR cash in (totaal 30.000 EUR aanvangsvermogen). Verwachte omzet jaar 1: 120.000 EUR; jaar 3: 250.000 EUR. Geen externe investeerders._
>
> **Berekening:**
>
> - Stap 1 — uitsluiten: maatschap en VOF (onbeperkte aansprakelijkheid; ICT-activiteit = aansprakelijkheidsrisico voor klanten). NV uitsluiten (overhead 61.500 EUR-kapitaal + zwaar bestuur niet gerechtvaardigd op deze schaal).
> - Stap 2 — overwegen: BV (default-keuze WVV). 30.000 EUR aanvangsvermogen is 'toereikend' indien het financieel plan een liquiditeitsbuffer van minstens 12-18 maanden aantoont voor vaste kosten. Financieel plan uitwerken (art. 5:4 WVV).
> - Stap 3 — fiscale toets: bij 250.000 EUR omzet en geschatte 80.000 EUR winst → VenB tegen 20 % KMO-tarief = 16.000 EUR (verlaagd-tarief mits 'klein' + bezoldiging min. 50.000 EUR/jaar aan minstens één bedrijfsleider, art. 215 §3 WIB92). In eenmanszaak (PB): 80.000 EUR × ca. 50 % marginaal = 40.000 EUR PB + sociale bijdragen. Vennootschap is duidelijk gunstiger op deze schaal.
> - Stap 4 — beslissing: BV met 30.000 EUR aanvangsvermogen, financieel plan, twee bestuurders (Alex + Brigitte), pro rata 50/50-aandelenverdeling.
>
> → **Resultaat**: BV gekozen. Notariële akte ca. 1.500-2.500 EUR + administratiekosten; aansprakelijkheid begrensd tot ingebracht vermogen; fiscaal optimaal op deze schaal.
>
> <small>🔗 WVV — art. 5:3 — _wettekst_ · WIB92 — art. 215 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Keuze: familiale vermogensstructuur ouders + 3 kinderen
> _Familie X (ouders 60+) wil een effectenportefeuille van 1.200.000 EUR overdragen naar de 3 kinderen met behoud van controle bij de ouders. Geen actieve commerciële uitbating — louter portefeuillebeheer._
>
> **Berekening:**
>
> - Stap 1 — vorm: maatschap. Geen rechtspersoonlijkheid → geen publicatieplicht jaarrekening (discretie); fiscale transparantie → inkomsten uit portefeuille belast bij vennoten in PB; statuten + zaakvoerder-mandaat ouders ⇒ controle behouden.
> - Stap 2 — schenking aandelen: 1.200.000 EUR portefeuille ingebracht in maatschap voor 1.200.000 EUR delen (300 delen à 4.000 EUR). Ouders schenken via bankgift 300 delen aan 3 kinderen, 100 delen elk. Schenkbelasting: 3 % (Vlaanderen, in rechte lijn) op 1.200.000 EUR = 36.000 EUR — of 0 % bij niet-registratie + overleven 3 jaar.
> - Stap 3 — controle: ouders blijven statutair zaakvoerder van de maatschap met exclusieve beslissingsbevoegdheid over aan-/verkoop effecten en uitkeringen. Kinderen zijn vennoten maar hebben geen bestuursbevoegdheid tot statutaire wijziging.
> - Stap 4 — risico-controle: bij niet-bestuurs-vennoten beperkt het persoonlijke verhaal-recht van schuldeisers zich tot hun aandeel in de maatschap; persoonlijke schuldeisers van een vennoot kunnen geen uitwinning vragen van de portefeuille zelf (art. 4:15 WVV).
>
> → **Resultaat**: Maatschap-structuur biedt: (a) successieplanning via schenking aandelen (lage tarief), (b) behoud controle ouders via statuten, (c) fiscale transparantie zonder VenB-overhead, (d) discretie.
>
> <small>🔗 WVV — art. 1:5 §1 — _wettekst_ · WIB92 — art. 29 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Verplichte omzetting BVBA → BV (vóór 1 januari 2024)
> _Bestaande BVBA met 18.550 EUR maatschappelijk kapitaal (oude minimum), opgericht in 2015, twee aandeelhouders 60/40, zaakvoerder X._
>
> **Berekening:**
>
> - Stap 1 — automatische omzetting van rechtswege: vanaf 1 januari 2020 zijn de dwingende bepalingen van het WVV (boek 5) van toepassing op de BVBA, die nu BV heet — ook zonder statutenwijziging.
> - Stap 2 — uiterlijk 1 januari 2024: statuten formeel aanpassen aan het WVV. Het bestaande maatschappelijk kapitaal (18.550 EUR) wordt automatisch omgezet in een 'statutair onbeschikbare eigen vermogenrekening' — geen meer 'kapitaal'-rubriek in de BV.
> - Stap 3 — ondernemingsnummer (KBO), bankrekeningen, contracten: geen wijziging — art. 14:2 garandeert continuïteit rechtspersoonlijkheid.
> - Stap 4 — fiscaal: geen impact — geen vereffening, geen meerwaardebelasting; aandeelhouders behouden hun aandeel-belang.
>
> → **Resultaat**: Continuïteit zonder fiscale gevolgen; nieuwe naam 'BV' verplicht in alle externe communicatie + facturen + KBO-inschrijving.
>
> <small>📖 WVV — art. 14:2 — _wettekst_ · WVV — art. 41 — _wettekst_</small>

## Valkuilen

> [!warning]- Denken dat de BV nog een minimumkapitaal heeft
> **Verkeerde assumptie**: Stagiairs herinneren zich '18.550 EUR' uit oude opleidingen of denken dat élke vennootschap een minimumkapitaal moet hebben.
>
> **Kernpunt**: Sinds WVV (1 mei 2019): de BV heeft GEEN minimumkapitaal meer (art. 5:3 WVV — 'toereikend aanvangsvermogen'). Het 'minimum' wordt geconcretiseerd via het verplichte financieel plan (art. 5:4) dat een liquiditeits- + solvabiliteitsprognose moet bevatten. De NV behoudt wél haar 61.500 EUR minimumkapitaal (art. 7:2). CV is ook kapitaalloos.
>
> <small>📖 WVV — art. 5:3 — _wettekst_ · WVV — art. 4:13 — _wettekst_ · WVV — art. 7:2 — _wettekst_</small>

> [!warning]- Maatschap = 'gewoon een onderonsje' — geen aansprakelijkheid
> **Verkeerde assumptie**: Omdat de maatschap 'geen rechtspersoon' is en vaak in familiale context gebruikt wordt, denken stagiairs dat er geen vennootschapsrechtelijke aansprakelijkheid is.
>
> **Kernpunt**: Maatschap heeft géén rechtspersoonlijkheid → onbeperkte hoofdelijke aansprakelijkheid van ALLE vennoten op hun privévermogen voor de schulden van de maatschap (art. 4:14 WVV). In familiale-maatschap-context is dat aanvaardbaar (geen externe schulden); in operationele activiteiten is een maatschap doorgaans onverantwoord.
>
> <small>📖 WVV — art. 4:14 — _wettekst_</small>

> [!warning]- VOF en CommV als 'eenvoudige' alternatief voor BV/NV
> **Verkeerde assumptie**: Stagiairs zien VOF en CommV als 'simpele' kapitaalvennootschappen omdat ze geen minimumkapitaal hebben en eenvoudig op te richten zijn.
>
> **Kernpunt**: VOF en CommV (gecommanditeerden) → onbeperkte hoofdelijke aansprakelijkheid op privévermogen. Wel rechtspersoonlijkheid (anders dan maatschap) maar dat doet niets af aan de aansprakelijkheid. In de praktijk vooral nuttig in fiscaal-transparante constructies (CommV als doorkijk-vennootschap) of bij familiale verticale structuren.
>
> <small>📖 WVV — art. 4:14 — _wettekst_ · WVV — art. 1:5 — _wettekst_</small>

> [!warning]- VZW gebruiken voor commerciële activiteit
> **Verkeerde assumptie**: VZW wordt soms verkozen voor de 'gratis' aansprakelijkheidsbeperking + kapitaalloosheid, ook bij commerciële activiteiten.
>
> **Kernpunt**: Een VZW mag commerciële activiteiten verrichten (WVV 2019 — soepeler dan vroeger), maar (a) winst mag niet uitgekeerd worden aan leden — surplus moet binnen het belangeloos doel blijven (art. 9:23), (b) bij significant commerciële activiteit wordt de VZW VenB-plichtig (i.p.v. RPB), wat het fiscale 'voordeel' tenietdoet, (c) misbruik kan leiden tot herkwalificatie (art. 9:21 — ontbinding bij doel-overtreding).
>
> <small>📖 WVV — art. 9:1 — _wettekst_ · WVV — art. 9:23 — _wettekst_ · WIB92 — art. 181 — _wettekst_</small>

## Speelruimtes

### 🎚️ Eenmanszaak vs vennootschap — kantelpunt

### 🎚️ BV vs NV — wanneer NV verkiezen?

## Accountant-perspectieven

### Adviseur — startende ondernemer/herstructurering

_De accountant adviseert een cliënt over de keuze van een rechtsvorm bij start of bij wijziging van de activiteit._

#### 🧭 Adviseur

##### 👣 Vorm-keuze-advies stappenplan

Stappenplan vorm-advies: (1) Inventariseer activiteit, omvang, aantal vennoten, risicoprofiel. (2) Schat netto-winst jaar 1-3 + financieringsbehoefte. (3) Bepaal of de cliënt aansprakelijkheidsbeperking wenst (in 99 % van commerciële activiteiten: ja). (4) Doe het PB-vs-VenB-vergelijking met realistische cijfers. (5) Adviseer BV als default tenzij duidelijke reden voor NV/CV/maatschap. (6) Stel financieel plan op (art. 5:4 WVV) — een verplichte deliverable die ook het advies onderbouwt en de bestuurdersaansprakelijkheid (art. 5:16) afdekt.

<small>🔗 WVV — art. 5:4 — _wettekst_ · WVV — art. 5:16 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Opstellen financieel plan oprichting

Het financieel plan (art. 5:4 voor BV; analoog 6:5 voor CV; 7:3 voor NV) moet bevatten: nauwkeurige beschrijving van de voorgenomen activiteit, projecties van inkomsten + uitgaven voor minimum 2 jaar, een overzicht van de financiering, hypothesen + verantwoording. Doel: aantonen dat het aanvangsvermogen 'toereikend' is voor minstens 24 maanden activiteit. De accountant adviseert + structureert maar de oprichters tekenen zelf. Bij faillissement binnen 3 jaar wordt het plan opgevraagd door de curator — gebreken triggeren bestuurdersaansprakelijkheid (art. 5:16).

<small>📖 WVV — art. 5:4 — _wettekst_ · WVV — art. 5:16 — _wettekst_ · WVV — art. 7:3 — _wettekst_</small>

##### 👣 Begeleiden bij oprichting eenmanszaak

Stappenplan voor de accountant bij oprichting eenmanszaak: (1) **Inschrijving in de KBO** — ondernemingsnummer aanvragen via een ondernemingsloket (Acerta, Securex, Liantis, ...). (2) **BTW-keuze** — regulier BTW-regime vs vrijstellingsregeling kleine onderneming (omzet-drempel **25.000 EUR** — orde van grootte AJ 2026, exacte drempel te verifiëren in Cijferzakboekje). (3) **Sociaal statuut** — aansluiting bij een sociale-verzekeringskas voor zelfstandigen, **vóór** aanvang activiteit. (4) **Voorafbetalingen personenbelasting** bepalen — vermijden van verlies van bonifications en van vermeerderingen wegens onvoldoende voorafbetaling. (5) **Boekhoudplicht** vastleggen — vereenvoudigde vs dubbele boekhouding, afhankelijk van WER Boek III-grootte-categorie (omzet > 500.000 EUR excl. BTW = dubbele boekhouding verplicht — verifieer in CBN-advies 2019/11 + WER art. III.85). (6) **Pro-forma-begroting eerste boekjaar** — omzet/kosten/winst-prognose + cash-positie + break-even-analyse. (7) **BTW-aangifte-ritmiek** — maandelijks (omzet > 2,5 M EUR) / kwartaal (default) / jaarlijks (vrijstellingsregeling), afhankelijk van omzet. Bonus: opening klanten-dossier triggert [[antiwitwaspreventie]]-KYC; geschillen met fiscus volgen [[fiscale-procedure]].

<small>❓ WIB92 — art. 23 — _wettekst_ · WER — art. III.85 — _wettekst_ · claude-opus-4-7 — _ai_model_ — (2026-05-29)</small>

#### 💰 Fiscaal adviseur

##### 📜 Quick-scan PB vs VenB voor cliënt

Quick-scan-formule voor eenmanszaak → BV: bereken simulatie (a) PB op netto-winst (marginaal-tarief × winst) + sociale bijdragen + gemeentebelasting; (b) VenB op netto-winst − bezoldiging zaakvoerder (20 of 25 %) + RV/PB op uitkeringen (dividend 15 % VVPRbis na 3 j of bezoldiging in PB-progressief). Vergelijk netto-na-belasting. Boven ca. 40.000 EUR netto-winst gaat de balans meestal in voordeel van BV; daaronder is de eenvoud van de eenmanszaak vaak doorslaggevend.

<small>🔗 WIB92 — art. 215 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Begeleider bij vorm-omzetting

_De accountant begeleidt cliënt bij omzetting van bestaande vennootschap (bv. NV → BV)._

#### 👥 Begeleider

##### 👣 Omzettings-procedure stappen

Omzetting NV → BV stappen: (1) Voorstel omzetting + verslag bestuursorgaan + tussentijdse balans (max 3 maanden oud). (2) Verslag commissaris/bedrijfsrevisor (art. 14:3 e.v.). (3) Buitengewone algemene vergadering met 4/5-meerderheid (strengere quorum dan gewone statutenwijziging). (4) Notariële akte + neerlegging KBO + publicatie BS. (5) Statuten aanpassen aan BV-regime; kapitaal omzetten naar 'inbreng' (geen kapitaal-begrip meer); benoeming bestuurders BV. Rechtspersoonlijkheid blijft (art. 14:2) — geen fiscale gevolgen, geen vereffening.

<small>📖 WVV — art. 14:2 — _wettekst_ · WVV — art. 14:3 — _wettekst_</small>

## Verder lezen (scope-out)

- → Specifieke vorm: BV — default WVV-vorm sinds 2019 → [[besloten-vennootschap]] _(moet-verwijzen)_
- → Specifieke vorm: NV → [[naamloze-vennootschap]] _(moet-verwijzen)_
- → Specifieke vorm: CV — coöperatief doel → [[cooperatieve-vennootschap]] _(moet-verwijzen)_
- → Specifieke vorm: VOF — volle aansprakelijkheid → [[vennootschap-onder-firma]] _(moet-verwijzen)_
- → Specifieke vorm: CommV → [[commanditaire-vennootschap]] _(moet-verwijzen)_
- → Specifieke vorm: maatschap — geen rechtspersoonlijkheid · fiscaal-transparant → [[maatschap]] _(moet-verwijzen)_
- → Specifieke vorm: VZW → [[vereniging-zonder-winstoogmerk]] _(moet-verwijzen)_
- → Grootte-categorieën cascade (jaarrekening-schema · commissaris · consolidatie) → [[vennootschap-groottecategorieen]] _(moet-verwijzen)_
- → Oprichting van een vennootschap — keten-vervolg → [[oprichting-vennootschap]] _(moet-verwijzen)_
- → Aansprakelijkheid bestuurders + oprichters per vorm → [[bestuurdersaansprakelijkheid]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ vennootschapsrecht
### `bevat`
- [[besloten-vennootschap]]
- [[naamloze-vennootschap]]
- [[cooperatieve-vennootschap]]
- [[vennootschap-onder-firma]]
- [[commanditaire-vennootschap]]
- [[maatschap]]
- [[vereniging-zonder-winstoogmerk]]
- [[vennootschap-groottecategorieen]]
### `triggert`
- [[oprichting-vennootschap]]
### `beinvloed_door`
- [[boekhoudplicht]] — Boekhoudplicht en mogelijkheid van vereenvoudigde boekhouding hangen af van de rechtsvorm (CBN-advies 2019/11).
- [[vennootschapsbelasting]] — Aanknoping bij VenB volgt direct uit de rechtsvorm (art. 179 WIB92).
