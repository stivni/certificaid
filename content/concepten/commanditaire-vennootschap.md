---
title: "Commanditaire vennootschap"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.I
  - 3.0.I.A
  - 3.0.I.B
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/commanditaire-vennootschap.json"
---

# Commanditaire vennootschap

_Instrument_

🏢 Entiteit · Anchors: `3.0.I` · `3.0.I.A` · `3.0.I.B` · Wave: `cluster-extract-vennootschapsvormen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: CommV — **Synoniemen**: Comm.V (oud) · société en commandite (SComm) · limited partnership — **Vertalingen**: fr: société en commandite (SComm)

## Definitie

📖 De commanditaire vennootschap (CommV) is een personenvennootschap met rechtspersoonlijkheid (art. 1:5 §2 WVV) met TWEE typen vennoten: (a) gecommanditeerde (beherende) vennoten — onbeperkt hoofdelijk aansprakelijk + bevoegd om de vennootschap te besturen en te vertegenwoordigen; (b) commanditaire (stille) vennoten — aansprakelijkheid beperkt tot hun inbreng + verboden om de vennootschap naar derden toe te besturen (art. 4:18 WVV — verbod van inmenging). Geen minimumkapitaal vereist. Geregeld in WVV boek 4 (samen met maatschap en VOF). Onderscheid met VOF: in een VOF zijn ALLE vennoten beherend + hoofdelijk aansprakelijk; in CommV bestaat de mix beherend/stil.

<small>📚 WVV — art. 1:5 — _wettekst_ · WVV — art. 4:14 — _wettekst_ · WVV — art. 4:18 — _wettekst_</small>

## Substantie

🔗 Praktisch: CommV is geschikt waar één persoon (gecommanditeerd) actief de zaak runt en investeerders (commanditaire vennoten) kapitaal inbrengen met beperkte aansprakelijkheid maar zonder bestuursinvloed. Toepassingen: (a) familiale opvolging waar een ouder als gecommanditeerd het familievermogen bestuurt en kinderen als stille vennoten in beperkte aansprakelijkheid delen, (b) investeringsstructuren (private equity fondsen — limited partnership-model — historisch via CommV), (c) zelfstandige met external private-investor. Soepele oprichting (geen notariële akte verplicht), geen minimumkapitaal, vereenvoudigde boekhouding mogelijk (omzet < 500.000 EUR — CBN 2019/11). Risico voor stille vennoten: ze mogen niet besturen — anders verliezen ze hun aansprakelijkheidsbescherming en worden behandeld als gecommanditeerde (art. 4:18 §2 WVV).

<small>📚 WVV — art. 4:18 — _wettekst_ · CBN 2019/11 — Beoogde personen - rechtsvorm — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De CommV bestaat al sinds de 19e eeuw als instrument om een soepele combinatie te maken tussen actief ondernemerschap (gecommanditeerd, met persoonlijke betrokkenheid via volle aansprakelijkheid) en passieve investering (commanditair, met aansprakelijkheidsbescherming). Historisch was zij een belangrijke vorm vóór de opkomst van de BVBA als beperkte-aansprakelijkheidsvorm; vandaag is haar rol vooral nog in familievermogensplanning + fonds-structuren. Het verbod van inmenging (art. 4:18 WVV) is essentieel voor de aansprakelijkheidsverdeling — wie zich gedraagt als beherend vennoot, moet ook de aansprakelijkheid dragen (anti-misbruik).

<small>📚 WVV — art. 4:18 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV boek 4

**✅ Voor**
- 🔗 Geschikt voor: familievermogensplanning (ouder = gecommanditeerd-bestuurder; kinderen = stille vennoten); investeringsstructuren (private equity LP-model); zelfstandige met externe stille investeerders; doorstroom-vehikels in fiscale planning waarbij een natuurlijke persoon de gecommanditeerde is en een rechtspersoon commanditair.

**🚫 Niet voor**
- 🔗 Niet voor: pure commerciële activiteit met derden-risico waar ALLE vennoten beperkt aansprakelijk willen zijn → BV verkiezen.

**📋 Voorwaarden**
- 📖 Oprichting: (1) minstens 2 vennoten (één gecommanditeerd + één commanditair), (2) statuten (onderhands kan — geen notariële akte verplicht), (3) inschrijving KBO + publicatie BS waarin namen GECOMMANDITEERDEN vermeld worden (niet de commanditaire — die mogen anoniem blijven, art. 4:21 WVV).

**👍 Voordeel**
- 📖 (a) Stille vennoten genieten beperkte aansprakelijkheid (zoals BV-aandeelhouders) zonder dat ze in de openbare publicatie moeten verschijnen — discretie. (b) Gecommanditeerde behoudt volledige bestuursmacht zonder verdunning. (c) Geen minimumkapitaal. (d) Geen notariële akte voor oprichting. (e) Vereenvoudigde boekhouding mogelijk.

**⚠️ Risico**
- 📖 (a) Gecommanditeerde: volle hoofdelijke aansprakelijkheid op privévermogen — typisch zijn beroepsbestaan staat op het spel bij faillissement. (b) Stille vennoot die zich inmengt in bestuur of zich extern als bestuurder presenteert → verliest beschermd statuut (art. 4:18 §2) — wordt aansprakelijk als gecommanditeerde voor verbintenissen ontstaan tijdens inmenging. (c) Indien enige gecommanditeerde komt te overlijden of uittreedt → CommV moet vereffend worden of nieuwe gecommanditeerde aangewezen.

## Bouwstenen

### ⚙️ Twee categorieën vennoten  
_`mechanisme`_

📖 Gecommanditeerde vennoot: actief beherend; volle hoofdelijke aansprakelijkheid op privévermogen voor alle verbintenissen van de CommV (art. 4:14). Naam moet vermeld in statuten + KBO + publicatie BS. Commanditaire (stille) vennoot: louter financier; aansprakelijkheid begrensd tot inbreng (zoals BV-aandeelhouder); mag NIET besturen of de CommV naar derden toe vertegenwoordigen (art. 4:18 — verbod inmenging); zijn naam hoeft niet in publicatie BS.

<small>📚 WVV — art. 4:14 — _wettekst_ · WVV — art. 4:18 — _wettekst_ · WVV — art. 4:21 — _wettekst_</small>

### 📜 Verbod van inmenging stille vennoot  
_`regel`_

📖 Art. 4:18 WVV: een commanditaire vennoot mag geen daad van beheer stellen voor rekening van de vennootschap, ook niet krachtens een volmacht. Inbreuk → de stille vennoot wordt tov derden behandeld alsof hij gecommanditeerde was — hoofdelijk aansprakelijk voor de verbintenissen van de CommV ontstaan tijdens of door zijn inmenging. Toegelaten: interne adviesactiviteit, deelname aan AV met informatierecht, controle op de gecommanditeerde via statuten (rapportage-verplichtingen).

<small>📚 WVV — art. 4:18 — _wettekst_</small>

### 📜 Bestuur — alleen gecommanditeerden  
_`regel`_

📖 Het bestuur van de CommV wordt uitsluitend uitgeoefend door de gecommanditeerde vennoten (art. 4:22 WVV mutatis mutandis). Indien er meerdere gecommanditeerden zijn: default samen, statuten kunnen anders bepalen. Een derde-niet-vennoot kan in principe niet als bestuurder optreden zonder de gecommanditeerde-positie aan te nemen (en dus aansprakelijkheid).

<small>📚 WVV — art. 4:22 — _wettekst_ · WVV — art. 4:18 — _wettekst_</small>

### 📜 Fiscale aanknoping CommV — VenB  
_`regel`_

📖 CommV is een vennootschap met rechtspersoonlijkheid → VenB-plichtig (art. 179 WIB92). Tarief 25 % standaard / 20 % KMO (art. 215). Bezoldigingen aan gecommanditeerden: behandeld als bedrijfsleidersbezoldiging (art. 32 WIB92) — aftrekbaar voor CommV, belastbaar in PB bij gecommanditeerde. Uitkeringen aan commanditairen: dividend (RV 30 % of 15 % VVPRbis indien voorwaarden vervuld).

<small>📚 WIB92 — art. 179 — _wettekst_ · WIB92 — art. 32 — _wettekst_ · WIB92 — art. 215 — _wettekst_ · WIB92 — art. 269 — _wettekst_</small>

## Voorbeelden

### 💡 CommV familievermogensplanning ouder + 2 kinderen 🔗

_Vader X (62 j) wil zijn winkelketen (3 winkels, eigendom + activa 800.000 EUR) inbrengen in een vennootschap om geleidelijk over te dragen aan zoon A en dochter B. Vader wil de operationele controle behouden tot zijn 75ste._

**Berekening:**
- Stap 1 — structuur: CommV opgericht; Vader = enige gecommanditeerde (volle bestuur + volle aansprakelijkheid); A en B = commanditaire vennoten (beperkte aansprakelijkheid + geen bestuursinmenging).
- Stap 2 — inbreng: Vader brengt winkelketen in voor 800.000 EUR → 800 aandelen à 1.000 EUR. Schenkt 200 aandelen aan A en 200 aandelen aan B (totaal 400 aandelen geschonken). Schenkbelasting Vlaanderen rechte lijn 3 % op 400.000 EUR = 12.000 EUR (of 0 % bij niet-registratie + overlevingsperiode 3 j).
- Stap 3 — boekingen oprichting: D 240/220 Inbreng winkelketen 800.000 / C 100 Inbreng 800.000. Schenking aandelen: geen boekhoudkundige impact in CommV (overgang aandelenhouder).
- Stap 4 — verloop: Vader (gecommanditeerd) bestuurt + ontvangt bedrijfsleidersbezoldiging; A en B (commanditair) ontvangen dividend pro rata aandeel. A/B mogen niet besturen — overtreding triggert hoofdelijke aansprakelijkheid (art. 4:18 §2).
- Stap 5 — opvolging: bij Vader's stopzetting kan structuur omgevormd worden naar BV (art. 14:2 — behoud rechtspersoonlijkheid) waarin A + B beiden bestuurder worden zonder hun aansprakelijkheidsbescherming te verliezen.

→ **Resultaat**: CommV als overgangs-structuur familiale opvolging: Vader behoudt controle + krijgt aansprakelijkheid (consistent met zijn actieve rol); A en B krijgen geleidelijk eigendom + beperkte aansprakelijkheid + dividend-recht. Geleidelijke schenkings-overdracht 3 % schenkbelasting.

<small>📚 WVV — art. 4:18 — _wettekst_ · WVV — art. 4:21 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Stille vennoot die zich inmengt — gevolgen 🔗

_CommV 'Restaurant De Steeg' met gecommanditeerde Frank en commanditaire vennoot Anna (50.000 EUR inbreng, 30 % aandelen). Frank wordt ziek; Anna ondertekent gedurende 2 maanden alle leveranciers-contracten en betaalt-orders namens de CommV. Tijdens deze periode ontstaan 80.000 EUR aan leveranciersschulden._

**Berekening:**
- Stap 1 — Anna handelde extern als bestuurder van de CommV (ondertekening contracten + betaalorders) — voldoet aan art. 4:18 daad van beheer.
- Stap 2 — gevolg art. 4:18 §2: Anna wordt tov derden behandeld als gecommanditeerde voor de verbintenissen ontstaan tijdens of door haar inmenging — de 80.000 EUR leveranciersschulden.
- Stap 3 — concrete aansprakelijkheid: indien de CommV de 80.000 EUR niet kan betalen, kunnen leveranciers Anna PERSOONLIJK voor het volle bedrag aanspreken — niet beperkt tot haar 50.000 EUR-inbreng zoals een normale commanditaire vennoot.
- Stap 4 — niet-inmenging-perioden: voor de schulden die vóór of na de inmengings-periode ontstonden, blijft Anna's aansprakelijkheid beperkt tot haar 50.000 EUR inbreng (art. 4:18 onschuldigt niet retroactief alle schulden — enkel die van de inmengings-periode).
- Stap 5 — preventie: Anna had via een volmacht via statuten dit kunnen vermijden, of via een operations manager-aanstelling door Frank (waarbij Anna niet als bestuurder figureert).

→ **Resultaat**: Anna's aansprakelijkheid stijgt van 50.000 EUR (inbreng) naar onbeperkt voor 80.000 EUR inmengings-periode-schulden. Praktisch advies: stille vennoten moeten zich onthouden van externe bestuursdaden.

<small>📚 WVV — art. 4:18 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Investeringsfonds-structuur via CommV 🔗

_Private equity-manager Pierre richt een investeringsfonds op met 5 institutionele investeerders die elk 2.000.000 EUR willen inbrengen (totaal 10.000.000 EUR). Pierre wil discretionaire investeringsbevoegdheid behouden + 2/20-fee-structuur._

**Berekening:**
- Stap 1 — structuur: CommV opgericht; Pierre (of zijn management-vehikel) = gecommanditeerde (vol bestuur + aansprakelijkheid begrensd door management-vennootschap-structuur boven hem); 5 investeerders = commanditaire vennoten.
- Stap 2 — kapitaalverdeling: Pierre brengt 100.000 EUR in (1 % — gecommanditeerd belang) — voldoende voor co-investment-incentive; 5 investeerders elk 2.000.000 EUR — totaal 10.100.000 EUR.
- Stap 3 — winst-verdeling statutair: 2/20-structuur = jaarlijkse management fee 2 % AUM aan Pierre + 20 % van winst boven hurdle rate (8 % p.a.). Statutair gedetailleerd uitgewerkt.
- Stap 4 — discretie: namen commanditaire investeerders NIET in publicatie BS (art. 4:21) — vertrouwelijkheid.
- Stap 5 — boekingen: D 550 Bank 10.100.000 / C 100 Inbreng 10.100.000. Bij investering in target-vennootschap: D 28 Financiële vaste activa (deelneming) / C 550 Bank. Management fee jaar 1: D 618 Bezoldigingen / C 489 Schuld aan Pierre — 200.000 EUR (2 % van 10 mln.).

→ **Resultaat**: PE-fonds gestructureerd als CommV: Pierre behoudt volledige investeringsbevoegdheid + zorgt voor aansprakelijkheidsfilter via boven-vennootschap; investeerders genieten beperkte aansprakelijkheid + discretie + recht op dividend. Klassieke LP-model in Belgisch recht.

<small>📚 WVV — art. 4:18 — _wettekst_ · WVV — art. 4:21 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Commanditaire vennoot laten 'meedoen' in bestuur

**Verkeerde assumptie**: Stille vennoot tekent gewoon mee in bestuursvergaderingen of vertegenwoordigt occasioneel de CommV.

**Kernpunt**: Verbod inmenging (art. 4:18 WVV) is strikt. Externe bestuurshandelingen door commanditair → onbeperkte aansprakelijkheid voor verbintenissen tijdens inmenging. Toegestaan zijn: interne advisering, deelname AV met informatierecht. Verboden: ondertekenen extern, vertegenwoordigen tov derden, betaalorders namens de CommV.

<small>📚 WVV — art. 4:18 — _wettekst_</small>

### ⚠️ CommV verwarren met BV

**Verkeerde assumptie**: Student denkt dat alle CommV-vennoten beperkt aansprakelijk zijn (zoals BV-aandeelhouders).

**Kernpunt**: Alleen commanditaire vennoten zijn beperkt aansprakelijk; gecommanditeerden zijn ONBEPERKT hoofdelijk aansprakelijk — net zoals VOF-vennoten. De CommV is een hybride personenvennootschap, geen kapitaalvennootschap.

<small>📚 WVV — art. 4:14 — _wettekst_ · WVV — art. 5:1 — _wettekst_</small>

### ⚠️ Enige gecommanditeerde vergeten te vervangen

**Verkeerde assumptie**: Bij overlijden of uittreding van de enige gecommanditeerde 'gaat de CommV gewoon door' met de commanditaire vennoten.

**Kernpunt**: Zonder gecommanditeerde kan een CommV niet voortbestaan (geen bestuur mogelijk — commanditaire mogen niet besturen). Statuten moeten een opvolgingsmechanisme voorzien (aanwijzing nieuwe gecommanditeerde, automatische vorm-conversie naar BV bij overlijden) — anders dreigt ontbinding.

<small>📚 WVV — art. 4:18 — _wettekst_ · WVV — art. 4:22 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Adviseur — CommV familieplanning + investerings-structuur

_De accountant begeleidt cliënten bij opzetten + voeren van CommV, met aandacht voor verbod inmenging en discretie._

#### 🧭 Adviseur

##### 👣 CommV-opzet adviseren  
_`stap`_

🔗 Adviesstap bij CommV-opzet: (1) Identificeer wie ACTIEF bestuurt (= gecommanditeerd) vs wie kapitaal levert (= commanditair). (2) Stel statuten op met duidelijke opvolgingsregeling gecommanditeerde + winstverdelingsmechanisme + opzeg/uittredingsmodaliteiten commanditaire vennoten. (3) Wijs cliënt op verbod inmenging — geef geschreven instructies aan commanditaire vennoten over wat WEL/NIET toegelaten. (4) Overweeg verzekering bedrijfsleider-aansprakelijkheid voor gecommanditeerde (vol hoofdelijke aansprakelijkheid).

<small>📚 WVV — art. 4:18 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale stromen CommV (bezoldiging vs dividend)  
_`regel`_

📖 Gecommanditeerde ontvangt bedrijfsleidersbezoldiging (art. 32 WIB92) — aftrekbaar voor CommV. Commanditaire vennoten ontvangen dividend (geen bezoldiging — ze besturen niet) → RV 30 % of 15 % VVPRbis indien voorwaarden art. 269 §2 WIB92 vervuld (kleine vennootschap + nieuwe aandelen). De accountant adviseert bezoldiging-niveau gecommanditeerde dat KMO-tarief 20 % VenB veiligstelt (minimum bezoldiging cf. art. 215 §3 WIB92).

<small>📚 WIB92 — art. 32 — _wettekst_ · WIB92 — art. 215 — _wettekst_ · WIB92 — art. 269 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vergelijking met andere vormen → [[ondernemingsvormen]] _(moet-verwijzen)_
- → Verwante vorm: VOF → [[vennootschap-onder-firma]] _(moet-verwijzen)_
- → Aansprakelijkheid bestuurders → [[bestuurdersaansprakelijkheid]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[ondernemingsvormen]]
### `vergelijkbaar_met`
- [[vennootschap-onder-firma]]
    - **Gelijkenissen**:
        - Beide personenvennootschappen WVV boek 4
        - Beide met rechtspersoonlijkheid
        - Beide geen minimumkapitaal
        - Beide VenB-plichtig
        - Beide mogen vereenvoudigde boekhouding voeren
    - **Verschillen**:
        - VOF: alle vennoten beherend + hoofdelijk aansprakelijk · CommV: twee soorten (beherend gecommanditeerd vol-aansprakelijk + stille commanditair beperkt-aansprakelijk)
        - VOF: namen alle vennoten in publicatie · CommV: alleen gecommanditeerden in publicatie BS (art. 4:21)
    - ⚠️ **Verwarringsrisico**: Beide vormen lijken qua oprichting + boekhouding identiek; verschil zit in twee-trapse aansprakelijkheidsstructuur CommV.
