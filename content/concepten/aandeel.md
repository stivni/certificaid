---
title: "Aandeel"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.IV
  - 3.0.IV.A
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/aandeel.json"
---

# Aandeel

_Instrument_

🏢 Entiteit · Anchors: `3.0.IV` · `3.0.IV.A` · `3.0.IV.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: share · effect · participatie — **Vertalingen**: fr: action / part sociale

## Definitie

📖 Een aandeel is een deelbewijs dat een fractie van het eigen vermogen van een vennootschap vertegenwoordigt en de houder ervan ('aandeelhouder') rechten verleent jegens die vennootschap. Onder WVV zijn de kernrechten: (1) stemrecht in de algemene vergadering — proportioneel of meervoudig, behoudens stemrechtloze aandelen; (2) dividendrecht — aandeel in uitgekeerde winst; (3) liquidatie-aandeel — deel in eindrest bij ontbinding; (4) voorkeurrecht bij kapitaalverhoging (art. 5:128 / 7:188); (5) informatierecht. Sinds WVV (2019) is de figuur grondig hervormd: in de BV en CV is er GEEN kapitaal meer (vervangen door 'inbreng zonder kapitaal'-concept, art. 5:1-5:9); aandelen daar zijn fractiewaarden in het eigen vermogen zonder nominaal bedrag. In de NV blijft het klassieke 'kapitaal + nominale of fractie-aandelen'-model (minimumkapitaal 61.500 EUR).

<small>📚 WVV — art. 5:18 — _wettekst_ · WVV — art. 5:40 — _wettekst_ · WVV — art. 7:50 — _wettekst_</small>

## Substantie

📖 Economisch: een aandeel is een 'residueel' instrument — pas na voldoening van schuldeisers krijgt de aandeelhouder zijn deel. Het is risicodragend kapitaal (hoogste yield-verwachting, hoogste verlies-risico bij faillissement). Juridisch onderscheidt het zich van obligaties (vreemd vermogen, vast rendement, voorrang in vereffening). De WVV-flexibilisering laat veel statutaire creativiteit toe: meervoudig stemrecht (BV onbeperkt; niet-genoteerde NV ja; genoteerde NV max factor 2 — Wet 28 april 2020), aandelen zonder stemrecht (typisch in combinatie met preferent dividend), winstgerechtigdheid-categorieën (preferent dividend, cumulatief preferent, ...). Het aandeelhoudersregister (art. 5:25 BV / 7:34 NV) is het wettelijk bewijs van eigendom; aandelen zijn typisch op naam (BV) of op naam/gedematerialiseerd bij genoteerde NV.

<small>📚 WVV — art. 5:25 — _wettekst_ · WVV — art. 5:42 — _wettekst_ · WVV — art. 7:62 — _wettekst_</small>

## Rationale

🔗 Het aandelenconcept maakt risicokapitaal-verzameling mogelijk: meerdere personen kunnen samen een vennootschap kapitaliseren met verschillende inbrengvolumes, en hun belang wordt evenredig vertegenwoordigd. De flexibilisering door WVV (verschillende categorieën stem- en winstrechten) laat toe complexe structureringen voor familievennootschappen (controle behouden bij oudere generatie via meervoudig stemrecht) en investeerders-deals (preferent dividend voor venture capital). Tegelijkertijd worden minderheden beschermd via dwingende rechten (voorkeurrecht, informatierecht, minderheidsvordering).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV (Wet 23 maart 2019); meervoudig stemrecht NV-genoteerd: Wet 28 april 2020.

Grondige hervorming sinds WVV. BV en CV: geen kapitaal meer, enkel 'inbreng + eigen-vermogen-fractie' (art. 5:1-5:9). NV: kapitaalconcept behouden. Meervoudig stemrecht in alle vennootschapsvormen toegelaten (genoteerde NV: max factor 2).

**✅ Voor**
- 📖 Aandelen kunnen worden uitgegeven in BV, NV, CV, CommV (statutair) en omgevormde vennootschappen. In maatschap/VOF: niet 'aandelen' maar 'aandeel in vennootschap' als persoonsgebonden recht (geen verhandelbaar instrument). VZW/stichting: geen aandelen (geen kapitaal).

**👍 Voordeel**
- 📖 Belang voor de aandeelhouder: (a) participatie in de winsten (dividend); (b) waardestijging bij goede prestatie (potentiële meerwaarde bij verkoop — voor private personen art. 90 1° WIB92 = geen belasting indien normaal beheer privé-vermogen); (c) stem- en beslissingsmacht over fundamentele besluiten via AV; (d) liquidatie-deel; (e) participatie zonder onbeperkte aansprakelijkheid (beperkt tot inbreng).

**⚠️ Risico**
- 📖 Risico's voor aandeelhouder: (a) verlies van inbreng bij vereffening met onvoldoende vermogen; (b) volstortingsplicht bij niet-volstorte aandelen — kan worden opgevraagd door bestuur of curator (NV art. 7:65); (c) verwatering bij kapitaalverhoging zonder voorkeurrecht-uitoefening; (d) belastingdienstige gevolgen bij bedrijfsmatig houden (meerwaarde voor vennootschap = belastbaar tenzij art. 192 WIB92-vrijstelling).

## Sub-concepten

### 📦 Aandeelhouders-rechten en -plichten  
_`kader` (subconcept)_

#### Definitie

📖 De aandeelhouder beschikt over een set wettelijke en statutaire rechten en draagt enkele beperkte plichten.

**Rechten**:
1. **Stemrecht** (art. 5:42 BV / 7:50 NV) — proportioneel aan kapitaalfractie, behoudens statutair meervoudig stemrecht of stemrechtloos aandeel.
2. **Dividendrecht** — aandeel in uitgekeerde winst (art. 5:46 BV / 7:55 NV); kan preferent zijn.
3. **Voorkeurrecht** bij kapitaalverhoging in geld (art. 5:128 BV / 7:188 NV) — beschermt tegen verwatering.
4. **Informatierecht** (art. 5:88 / 7:139): jaarrekening, jaarverslag, commissarisverslag, vragen aan bestuur.
5. **Uittredingsrecht** in CV (art. 6:120) en in BV onder statutaire voorwaarden (art. 5:154).
6. **Liquidatie-aandeel** bij ontbinding (rest na voldoening schuldeisers).
7. **Minderheidsrechten** (art. 2:60 — minderheidsvordering 1% of 1,25 mio EUR; art. 5:155 — gerechtelijke uitsluiting/uittreding).

**Plichten**:
1. **Volstortingsplicht** — bij niet-volstorte aandelen plicht om bij oproep door bestuur het resterende bedrag te storten (NV: art. 7:65).
2. **Goede trouw** in uitoefening van zijn rechten — geen rechtsmisbruik.
3. **Geen onbeperkte aansprakelijkheid** in BV/NV (beperkt tot inbreng); WEL onbeperkt in VOF en CommV-beherende.

<small>📚 WVV — art. 5:42 — _wettekst_ · WVV — art. 5:88 — _wettekst_ · WVV — art. 7:50 — _wettekst_ · WVV — art. 7:65 — _wettekst_ · WVV — art. 2:60 — _wettekst_</small>

## Bouwstenen

### ⚙️ Categorieën van aandelen  
_`mechanisme`_

📖 WVV laat een grote diversiteit aan aandelencategorieën toe (statutair te definiëren):

**Gewone aandelen** — standaardstemrecht (1 stem per aandeel) + standaarddividendrecht (pro rata).

**Aandelen met meervoudig stemrecht** — meer dan één stem per aandeel; in BV/CV onbeperkt mogelijk; in niet-genoteerde NV ja; in genoteerde NV max factor 2 (loyaliteitsstemrecht na 2 jaar houden, Wet 28 april 2020). Typisch instrument voor familievennootschap waarin oudere generatie controle behoudt na overdracht aandelen.

**Stemrechtloze aandelen** — geen stemrecht in AV; meestal in combinatie met preferent dividend. In BV: art. 5:43; in NV: art. 7:62. Maximum 1/3 van uitgegeven aandelen in NV (art. 7:62 §1).

**Preferente aandelen** — voorrang in dividenduitkering en/of liquidatie-aandeel. Kan cumulatief (gemiste dividenden inhalen) of niet-cumulatief.

**Aandelen op naam vs gedematerialiseerd**:
- BV: ALLEEN aandelen op naam (art. 5:24 §1).
- NV: aandelen op naam OF gedematerialiseerde aandelen (giraal in clearing-systeem). Aandelen aan toonder zijn afgeschaft sinds 2014 (Wet 14 dec 2005).

**Soort-veranderingen** vereisen statutenwijziging via buitengewone AV.

<small>📚 WVV — art. 5:42 — _wettekst_ · WVV — art. 5:43 — _wettekst_ · WVV — art. 5:24 — _wettekst_ · WVV — art. 7:62 — _wettekst_ · WVV — art. 7:50 — _wettekst_</small>

### 📜 Overdraagbaarheid  
_`regel`_

📖 **BV**: principe = besloten karakter — aandelen zijn slechts overdraagbaar mits goedkeuring door minstens helft van de andere aandeelhouders met minstens 75% van de stemrechten (art. 5:62 WVV), tenzij statuten anders bepalen. Belangrijke uitzonderingen automatisch toegestaan (geen goedkeuring nodig): overdracht aan een andere aandeelhouder, aan echtgenoot/wettelijk samenwonende, aan bloedverwanten in rechte lijn (art. 5:63). Statuten kunnen het besloten karakter versoepelen (open BV) of verstrengen (extra-restrictief).

**NV**: principe = vrije overdraagbaarheid (art. 7:78). Statuten kunnen overdrachtsbeperkingen invoeren — typisch voorkooprechten, goedkeuringsclausule — maar mogen niet het aandeel principieel onverhandelbaar maken. Beperkingen moeten redelijk zijn (rechterlijke toets).

**CV**: zeer flexibel — uittreding en intreding via statuten (art. 6:120 e.v.).

**Vorm overdracht**: voor aandelen op naam volstaat inschrijving in aandeelhoudersregister als bewijs (art. 5:25 / 7:34). Geen notariële akte vereist voor de overdracht zelf (wel voor schenking of overlijden-overdracht via erfrecht).

<small>📚 WVV — art. 5:62 — _wettekst_ · WVV — art. 5:63 — _wettekst_ · WVV — art. 7:78 — _wettekst_ · WVV — art. 5:25 — _wettekst_</small>

### 💡 Aandeelhoudersregister  
_`begrip`_

📖 Verplicht register dat de vennootschap bijhoudt op haar zetel met identificatie van elke aandeelhouder (naam, adres, aantal aandelen, soort, datum van inschrijving en eventuele beperkingen). Wettelijk bewijs van eigendom — overschrijving in het register is constitutief voor overdracht (art. 5:25 §3 / 7:34). Vorm: papier of elektronisch (sinds 2019 ook digitaal register via online platforms zoals eRegistry van NBB).

Verplichte inhoud (art. 5:25 §2):
1. Identiteit aandeelhouder + aandelen per soort;
2. Inbrengen en het deel van de inbreng dat eventueel nog niet is volstort;
3. Wijze van overdracht;
4. Statutaire of conventionele overdrachtsbeperkingen.

Iedere aandeelhouder mag het register inzien (art. 5:25 §4) — niet-aandeelhouders niet (privacy).

<small>📚 WVV — art. 5:25 — _wettekst_ · WVV — art. 7:34 — _wettekst_</small>

### 💡 Waarde-aspecten — nominale waarde · fractiewaarde · marktwaarde  
_`begrip`_

🔗 Drie waardebegrippen die op een aandeel toepasbaar zijn:

**Nominale waarde** — alleen in NV met aandelen-met-nominale-waarde (= bedrag waarvoor aandeel in het kapitaal vertegenwoordigd is, bv. 61,50 EUR per aandeel bij 1.000 aandelen + minimumkapitaal 61.500 EUR). Onveranderlijk tenzij statutenwijziging. NV kan ook aandelen ZONDER nominale waarde uitgeven; dan geldt 'fractiewaarde'.

**Fractiewaarde** — kapitaal / aantal aandelen — variabele waarde die mee evolueert bij kapitaalverhogingen of -verminderingen. In NV: enkel administratief. In BV/CV: GEEN kapitaal meer, dus geen nominale waarde of fractiewaarde in klassieke zin; wel een 'fractie in het eigen vermogen' — boekhoudkundige eigen-vermogenswaarde / aantal aandelen.

**Marktwaarde / handelswaarde** — economische realiteit. Berekenbaar via diverse methodes:
- *Discounted cash flow* (DCF) — voor groei-bedrijven;
- *Multiplemethode* (vermenigvuldiger × EBITDA, of × omzet, of × winst);
- *Vermogenswaarde* (eigen vermogen + correcties);
- *Mixed*: gemiddelde van rendements- en vermogenswaarde.

Voor genoteerde NV: marktprijs = beurskoers. Voor niet-genoteerde: waardering door deskundige (vaak GA + bedrijfsrevisor).

<small>📚 WVV — art. 7:50 — _wettekst_ · WVV — art. 5:5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Opbrengsten — dividend + meerwaarde  
_`mechanisme`_

📖 **Dividend** — periodieke uitkering van winst aan aandeelhouder na AV-besluit:
- BV: liquiditeitstest art. 5:143 vóór elke uitkering (kan vennootschap de schulden 12 maanden lang nog betalen?).
- NV: nettoactief-test art. 7:212 (uitkeerbaar bedrag = nettoactief minus niet-uitkeerbare reserves).
- Roerende voorheffing 30% bij uitkering (verlaging 15% onder VVPRbis-regime art. 269 §2 WIB92).
- Boekhoudkundig in vennootschap: rekening 694 'Vergoeding aandelen' debet, 471 'Te betalen dividenden' credit; betaling: 471 debet, 453 'Ingehouden voorheffingen' credit (RV) + 550 'Bank' credit. In aandeelhouder-natuurlijke persoon: PB-RV is bevrijdend (geen verdere aangifte tenzij vrijwillige aangifte). In aandeelhouder-vennootschap: DBI-vrijstelling (art. 202-205 WIB92) indien deelneming ≥ 10% of ≥ 2,5 mio EUR en houdperiode 1 jaar.

**Meerwaarde bij overdracht** — verschil tussen verkoopprijs en boekwaarde/aanschafprijs:
- Privé-houder (NP): in beginsel onbelast als 'normaal beheer privé-vermogen' (art. 90 1° WIB92). Belastbaar in art. 90 9° (33%) bij 'speculatieve verrichting' of ≥ 25% controlerend belang verkocht aan rechtspersoon buiten EER (16,5%, art. 171 4°bis).
- Vennootschap-houder: principe = belastbaar in VenB (gewoon tarief), MAAR vrijstelling art. 192 WIB92 indien aan voorwaarden voldaan (taxatie-voorwaarde + 1-jaar houdperiode + deelneming-eis ≥ 10% of ≥ 2,5 mio EUR — voor 'kleine vennootschap' vereenvoudigd).

<small>📚 WVV — art. 5:143 — _wettekst_ · WVV — art. 7:212 — _wettekst_ · WIB92 — art. 90 — _wettekst_ · WIB92 — art. 192 — _wettekst_ · WIB92 — art. 269 — _wettekst_</small>

## Voorbeelden

### 💡 Familie-BV met meervoudig stemrecht voor ouders 🔗

_BV Familia: 1.000 aandelen, EV 500.000 EUR. Vader V wil zijn 60% (600 aandelen) schenken aan zijn drie kinderen (200 aandelen elk), maar wenst zelf controle te behouden. Oplossing: statutenwijziging — V's resterende 400 aandelen worden 'aandelen met meervoudig stemrecht (factor 5)'._

**Berekening:**
- Stap 1 — uitgangssituatie: V = 600 aandelen × 1 stem = 600 stemmen (60%). Andere aandeelhouder M = 400 × 1 = 400 (40%).
- Stap 2 — na schenking V → 3 kinderen + statutenwijziging meervoudig stemrecht V: V houdt 400 aandelen × 5 stemmen = 2.000 stemmen. M = 400 × 1 = 400. Kinderen = 600 × 1 = 600. Totaal stemmen: 3.000.
- Stap 3 — V's stemkracht: 2.000 / 3.000 = 66,7%. V heeft nog steeds blokkering > 25% en zelfs versterkte meerderheid > 75% binnen handbereik (door M te overtuigen).
- Stap 4 — fiscaal voordeel: schenking aandelen aan kinderen onder gunsttarief familiale onderneming (0% of 3% afhankelijk van regio en voorwaarden) → erfbelasting later vermeden voor 600 aandelen.
- Stap 5 — boekhoudkundig: schenking heeft GEEN impact op BV (interne wijziging aandeelhoudersregister). Notariële schenkingsakte voor kinderen, aandeelhoudersregister bijgewerkt.

→ **Resultaat**: Resultaat: V heeft de successieplanning gerealiseerd (3 × 200 = 600 aandelen overgedragen) zonder zeggenschap te verliezen (door meervoudig stemrecht). Risico: kinderen kunnen later met M alliëren — V's 66,7% nog steeds bedreigd indien meervoudig stemrecht statutair wordt teruggedraaid (vereist 75%-statutenwijziging waar V nu wel zelf 66,7% heeft — beveiligd zolang statuten niet wijzigen).

<small>📚 WVV — art. 5:42 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Overdracht BV-aandelen — goedkeuringsregime art. 5:62 🔗

_BV Sigma heeft 5 aandeelhouders A (40%), B (25%), C (15%), D (12%), E (8%). E wil zijn 80 aandelen verkopen aan derde X. Statuten verwijzen naar wettelijk regime (geen versoepeling)._

**Procedure art. 5:62 WVV**:

1. E informeert het bestuur van zijn voornemen aandeel-overdracht aan X (naam, prijs, eventueel voorwaarden).
2. Bestuur agendaert dit punt op AV of vraagt schriftelijke instemming aandeelhouders.
3. Goedkeuring vereist: minstens **helft van de andere aandeelhouders** (= minstens 2 van A,B,C,D) met **minstens 75% van hun gezamenlijke stemrechten**.
   - Stemrechten andere aandeelhouders = 100% − 8% (E) = 92%. 75% van 92% = 69%.
   - Voorbeeld: A + B = 40+25 = 65% — onvoldoende.
   - A + B + C = 40+25+15 = 80% — ja, voldoende.
4. Indien geen goedkeuring: andere aandeelhouders moeten zelf overnemen aan dezelfde prijs (art. 5:64) OF E mag verkopen aan X.

**Vrijgesteld** van goedkeuring (art. 5:63): overdracht aan andere aandeelhouder, echtgenoot, kinderen — automatisch toegelaten.

**Vorm overdracht**: notariële akte niet nodig (privé-onderhandse akte volstaat); inschrijving in aandeelhoudersregister door bestuur op dag van overdracht.

<small>📚 WVV — art. 5:62 — _wettekst_ · WVV — art. 5:63 — _wettekst_ · WVV — art. 5:64 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Dividenduitkering 50.000 EUR — boekhoudkundige en fiscale verwerking 🔗

_BV Tau (klein) keert dividend uit 50.000 EUR aan haar 2 aandeelhouders A (60%) en B (40%) na AV-besluit jaarrekening 2025. VVPRbis-regime toepasselijk (kleine vennootschap, drie volledige boekjaren) → roerende voorheffing 15% in plaats van 30%._

**Boeking:**


**Boeking:**


**Per aandeelhouder**: A ontvangt netto 30.000 × 85% = 25.500 EUR; B 20.000 × 85% = 17.000 EUR.

**Fiscaal voor aandeelhouder NP**: 15% RV is een definitieve belasting (geen verdere aangifte nodig); voor aandeelhouder-vennootschap: DBI-vrijstelling mogelijk indien aan voorwaarden voldaan.

**Doorstorting RV**: BV moet 7.500 EUR doorstorten aan FOD Financiën binnen 15 dagen na betaling/toekenning (art. 412 WIB92).

<small>📚 WIB92 — art. 269 §2 — _wettekst_ · WIB92 — art. 412 — _wettekst_ · KB MAR — Rekening 694 + 471 + 453 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ BV-aandeel heeft nominale waarde

**Verkeerde assumptie**: Een BV-aandeel heeft een nominale waarde van 1 EUR of meer.

**Kernpunt**: Sinds WVV (2019) is er in BV en CV GEEN kapitaal meer; daardoor is er ook geen nominale waarde of fractie-waarde in klassieke zin. Het aandeel vertegenwoordigt een 'fractie in het eigen vermogen' — een variabele economische waarde. In de NV blijft kapitaal bestaan en hebben aandelen wel een nominale of fractie-waarde (kapitaal/aantal aandelen).

<small>📚 WVV — art. 5:1 — _wettekst_ · WVV — art. 5:5 — _wettekst_</small>

### ⚠️ Meervoudig stemrecht = onbeperkt in alle vennootschapsvormen

**Verkeerde assumptie**: Sinds WVV mag elk aandeel meervoudig stemrecht hebben zonder beperking.

**Kernpunt**: BV/CV: meervoudig stemrecht onbeperkt mogelijk (geen factor-limiet). Niet-genoteerde NV: ook onbeperkt. Genoteerde NV: max factor 2 (loyaliteitsstemrecht na 2 jaar houden, Wet 28 april 2020). Daarboven niet toegestaan om markt-integriteit te bewaren.

<small>📚 WVV — art. 5:42 — _wettekst_ · WVV — art. 7:53 — _wettekst_</small>

### ⚠️ Aandelen op naam vereisen geen notaris

**Verkeerde assumptie**: Elke overdracht van aandelen vereist een notariële akte voor geldigheid.

**Kernpunt**: Voor aandelen op naam volstaat een onderhandse overdrachtsakte + inschrijving in aandeelhoudersregister door bestuur (art. 5:25 §3 / 7:34). Notariële akte ALLEEN nodig bij: (a) schenking (art. 931 oud BW); (b) overlijden-overdracht via successie (notaris voor aangifte nalatenschap); (c) statutenwijziging (bv. opname overdrachtsbeperking).

<small>📚 WVV — art. 5:25 — _wettekst_</small>

## Accountant-perspectieven

### Cliënt-vennootschap + aandeelhouder

_Twee perspectieven: (1) de vennootschap die aandelen uitgeeft of het register bijhoudt; (2) de aandeelhouder die fiscaal en boekhoudkundig de aandelen verwerkt._

#### 📒 Boekhouder

##### 👣 Boeking emissie + agio bij kapitaalverhoging  
_`stap`_

🔗 Bij uitgifte van nieuwe aandelen tegen prijs hoger dan nominale waarde (NV) of dan eigen-vermogen-fractie (BV):
- Verschil aandeelprijs vs nominale (of inbreng-cijfer in BV) = uitgiftepremie (agio).
- NV: rekening 100 'Kapitaal' credit voor nominale waarde × aantal; rekening 11 'Uitgiftepremies' credit voor verschil.
- BV: rekening 110 'Inbreng' credit voor het volledig bedrag (uitgiftepremie geen aparte rekening — alles is 'inbreng' sinds WVV).

Tegenboeking: 550 'Bank' debet (geld-inbreng) of vast actief-rekening (natura-inbreng).

<small>📚 KB MAR — Rekening 10-11-110 — _kb_ · WVV — art. 5:5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Aandeelhoudersregister actueel houden  
_`stap`_

📖 Routinematig: bij elke overdracht, elke nieuwe uitgifte, elke statutenwijziging het register actualiseren — papier of digitaal (eRegistry van NBB sinds 2019). Datum, identiteit, aantal aandelen, eventuele beperkingen registreren. Niet-actueel register = aansprakelijkheidsrisico bestuur.

<small>📚 WVV — art. 5:25 — _wettekst_ · WVV — art. 7:34 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 📜 Roerende voorheffing op dividend  
_`regel`_

📖 Bij dividenduitkering: vennootschap moet RV inhouden en doorstorten binnen 15 dagen (art. 412 WIB92). Standaardtarief 30%. Verlaagde tarieven mogelijk:
- VVPRbis 15% (art. 269 §2 WIB92) — kleine vennootschap + aandelen uitgegeven sinds 1 juli 2013 + houden vanaf 3 boekjaren na uitgifte.
- 5% — uitkering uit liquidatiereserve (na 5 jaar houden).
- 0% — DBI-bevrijde dividenden tussen vennootschappen.

Aangifte 273A binnen 15d. Aandeelhouder-NP: RV is bevrijdend; aandeelhouder-vennootschap: DBI-aftrek + verrekening RV mogelijk.

<small>📚 WIB92 — art. 269 — _wettekst_ · WIB92 — art. 412 — _wettekst_</small>

##### 📜 Meerwaarde bij overdracht — 4 regimes  
_`regel`_

📖 **Voor aandeelhouder-NP** (privé-belegger):
1. Normaal beheer privé-vermogen → onbelast (art. 90 1° WIB92).
2. Speculatieve verrichting → 33% (art. 90 1° in fine).
3. ≥ 25% controlerend belang verkocht aan rechtspersoon buiten EER → 16,5% (art. 90 9° + 171 4° bis).

**Voor aandeelhouder-vennootschap**:
1. Belastbaar in VenB tenzij art. 192 WIB92-vrijstelling:
   - Taxatie-voorwaarde: dividenden van die aandelen voldoen aan DBI-voorwaarden.
   - Houdperiode: ≥ 1 jaar in volle eigendom.
   - Deelneming-eis: ≥ 10% kapitaal OF aanschafwaarde ≥ 2,5 mio EUR.
2. Voor kleine vennootschap: vereenvoudigd — alleen taxatie-voorwaarde + 1-jaar-houden.
3. Bij vrijstelling: meerwaarde vrijgesteld op aangifte VenB; minwaarden alleen aftrekbaar bij liquidatie tot beloop werkelijk verlies.

Boekhoudkundig: bij verkoop rekening 76 'Niet-recurrente opbrengsten' credit; bij verlies 66 'Niet-recurrente kosten' debet.

<small>📚 WIB92 — art. 90 1° — _wettekst_ · WIB92 — art. 192 — _wettekst_ · WIB92 — art. 171 — _wettekst_</small>

#### 🧭 Adviseur

##### 👣 Advies statutaire aandelen-categorieën  
_`stap`_

🔗 Bij oprichting of statutenwijziging: bespreek met cliënt de behoefte aan verschillende aandelencategorieën. Typische scenario's:
- Familie-overdracht zonder controle-verlies → meervoudig stemrecht voor ouders.
- Investeerder-deal → preferent dividend voor investeerder (eerst x% return, dan pas gewone aandeelhouders).
- Werknemersparticipatie → stemrechtloze aandelen met dividend-rechten.
- Joint-venture → A- en B-categorieën met spiegelende rechten (50/50 deadlock-protection).

Documenteer statutair zeer precies: wat het stemrecht is per categorie, wat het dividendrecht is, wat de liquidatie-volgorde is, hoe omzettingen tussen categorieën verlopen.

<small>📚 WVV — art. 5:42 — _wettekst_ · WVV — art. 5:43 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Eigen-vermogen — aandeel als component van kapitaal → [[eigen-vermogen]] _(moet-verwijzen)_
- → Dividend-uitkering → [[winstuitkering]] _(moet-verwijzen)_
- → Voorkeurrecht bij nieuwe uitgifte → [[voorkeurrecht]] _(moet-verwijzen)_
- → Volstortingsplicht aandeelhouder → [[volstortingsplicht]] _(moet-verwijzen)_
- → Kapitaalverhoging als emissie-moment → [[kapitaalverhoging]] _(moet-verwijzen)_
- ↪ Fiscale meerwaarde aandelen — VenB-perspectief vrijstellingsregime → [[meerwaarde-aandelen-venb]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[eigen-vermogen]]
### `triggert`
- [[winstuitkering]] — Dividendrecht aandeel = causaal voor winstuitkering-procedure.
### `vereist`
- [[algemene-vergadering]] — AV beslist over uitgifte, categorie-wijziging, dividenden, kapitaalverhoging — aandeel-leven loopt via AV.
### `uitgevoerd_door`
- [[gecertificeerd-accountant]] — GA voor boeking emissie/dividend, advies categorisering, waardering bij overdracht, fiscale verwerking.
### `vergelijkbaar_met`
- [[obligatielening]]
    - **Gelijkenissen**:
        - Beide zijn financieringsinstrumenten uitgegeven door een vennootschap
        - Beide kunnen worden verhandeld of overgedragen
        - Beide hebben houders-rechten en periodieke opbrengsten
    - **Verschillen**:
        - Aandeel = eigen vermogen, residueel, risicodragend, in principe geen vaste opbrengst (dividend afhankelijk van winst + AV-besluit)
        - Obligatie = vreemd vermogen, vooraf gekend rendement (rente), terugbetaling op vervaldag, voorrang in vereffening
        - Aandeelhouder heeft stemrecht in AV; obligatiehouder geen (wel apart in vergadering obligatiehouders bij bepaalde besluiten)
        - Aandeel geeft eigendom van fractie eigen vermogen; obligatie geeft schuldvordering
    - ⚠️ **Verwarringsrisico**: Stagiairs verwarren soms 'aandeelhouder' (eigenaar-residueel) met 'obligatiehouder' (schuldeiser). In faillissement is dit cruciaal — aandeelhouders krijgen pas iets nadat alle obligatiehouders en andere schuldeisers betaald zijn (residueel karakter).
