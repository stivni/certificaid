---
title: "Belasting niet-inwoners (BNI)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - kader
ankers:
  - 2.8.IV
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/belasting-niet-inwoners.json"
---

_Kader_ · afk: **BNI** · ook: non-resident tax · belasting niet-rijksinwoners · impôt des non-résidents · INR

## Definitie

De belasting van niet-inwoners (BNI) is de Belgische inkomstenbelasting die enkel slaat op de van België afkomstige inkomsten van personen of vennootschappen die GEEN Belgisch rijksinwoner zijn. Drie categorieën belastingplichtigen (art. 227 WIB92): (1) niet-rijksinwoners (natuurlijke personen) → BNI/nat; (2) buitenlandse vennootschappen → BNI/ven; (3) buitenlandse rechtspersonen zonder winstoogmerk → BNI/rp. De BNI is een spiegel-belasting van PB/VenB/RPB: dezelfde structuur, dezelfde tarieven, maar met TERRITORIAAL beperkte grondslag — uitsluitend de inkomsten met Belgische bron (art. 228 WIB92).

<small>📖 WIB92 — art. 227 — _wettekst_ · WIB92 — art. 228 — _wettekst_ · WIB92 — art. 238 — _wettekst_</small>

## Substantie

Stel: een Nederlandse zelfstandige consultant doet projectwerk in Antwerpen via een Belgische vaste inrichting. Hij is fiscaal Nederlands inwoner (geen Belgische woonplaats) — dus geen PB. Maar zijn Belgische bron-inkomsten (de winst van de vaste inrichting) worden in België belast via BNI/nat: zelfde tarieven als de PB, zelfde belastingschijven, maar enkel op die Belgische winst — niet op zijn Nederlandse inkomen. De BNI is dus de fiscaliteits-poortwachter voor wie wél een Belgisch economisch aanknopingspunt heeft maar fiscaal geen Belgisch inwoner is. Voor vennootschappen werkt het analoog: een Duitse GmbH met een Belgische verkoopfiliaal (vaste inrichting) wordt belast in BNI/ven op de winst van die filiaal — niet op haar wereldwijde winst.

<small>🔗 WIB92 — art. 227 — 2° — _wettekst_ · WIB92 — art. 228 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De BNI implementeert het territorialiteitsbeginsel: een staat heeft heffingsbevoegdheid over inkomsten die uit zijn grondgebied voortkomen, ongeacht de residentie van de ontvanger. Zonder BNI zou een buitenlandse onderneming gratis kunnen profiteren van de Belgische markt (klanten, infrastructuur, rechtsorde) zonder bij te dragen. Tegelijk voorkomt de territoriaal beperkte grondslag ongeoorloofde fiscale soevereiniteit-uitbreiding: België belast NIET het Nederlandse loon van de consultant, want dat heeft geen Belgisch aanknopingspunt. Dubbelbelastingverdragen verzachten verder: voor inkomsten waar het DBV de heffingsbevoegdheid aan de woonstaat toewijst (bv. zelfstandige beroepsinkomsten zonder VI in BE), wijkt de BNI terug.

<small>🔗 WIB92 — art. 227-228 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 227-248

Stabiele structuur sinds invoering WIB92. Bijzonder regime buitenlandse kaderleden vervangen in 2022 door het BBIB/BBIO-regime (artikel 32/1 e.v. WIB92).

**✅ Voor**
- 📖 Elke belastingplichtige die fiscaal geen Belgisch rijksinwoner is (geen woonplaats en geen zetel van fortuin in België) maar wel Belgische bron-inkomsten verkrijgt. Concreet: buitenlandse werknemers met salary-split (deel bezoldiging voor in BE uitgevoerd werk), buitenlandse zelfstandigen met Belgische vaste inrichting, buitenlandse eigenaars van Belgisch onroerend goed, buitenlandse vennootschappen met Belgische filiaal, etc.

**🚫 Niet voor**
- 🔗 Belgische rijksinwoners (zij betalen PB op het wereldwijde inkomen — art. 5 WIB92, niet BNI).
- 📖 Belgische vennootschappen met statutaire of werkelijke leiding in België (zij betalen VenB op het wereldwijde resultaat — art. 179 WIB92, niet BNI/ven).
- 📖 Inkomsten die op grond van art. 230 WIB92 expliciet zijn VRIJGESTELD van BNI: bv. interesten en royalty's toegerekend op een buitenlandse inrichting van de schuldenaar; sommige bezoldigingen voor in het buitenland uitgevoerd werk (art. 230 — 3°).

**📋 Voorwaarden**
- 🔗 Cumulatief: (1) belastingplichtige is geen Belgisch rijksinwoner (natuurlijk persoon) of geen Belgische vennootschap (heeft voornaamste inrichting of zetel van bestuur in het buitenland); (2) hij verkrijgt 'Belgische' inkomsten zoals limitatief opgesomd in art. 228 (onroerend, beroeps, roerend, divers); (3) inkomsten zijn niet vrijgesteld door art. 230 WIB92 of door een toepasselijk DBV; (4) eventueel bestaat een vaste inrichting waarop de inkomsten zijn toegerekend.

**⚠️ Risico**
- 🔗 Onterecht GEEN BNI-aangifte indienen: een buitenlandse vennootschap die werk uitvoert in België via een tijdelijke aanwezigheid (>6 maanden = vermoeden VI) loopt risico op ambtshalve aanslag in BNI/ven met belastingverhoging (art. 444 WIB92 — 10 tot 200 %). De fiscus kan tot 7 jaar terugwerken bij fraude (art. 354 WIB92).
- 🔗 Verkeerde aangifte-vorm: BNI/nat gebruikt aangifte 276.1; BNI/ven gebruikt aangifte 276.2. Geen onderscheid maken leidt tot weigering van de aangifte en boete.

## Sub-concepten

### 📦 BNI/nat — belasting niet-inwoners natuurlijke personen

#### Definitie

BNI/nat treft niet-rijksinwoners (natuurlijke personen) die in België belastbare inkomsten verkrijgen. De heffing volgt de structuur van de personenbelasting (zelfde tarieven, zelfde schijven, art. 130 WIB92) maar met enkel Belgische inkomsten in de grondslag. Drie subcategorieën: (1) met tehuis in België (volledige PB-gelijkenis, art. 244); (2) zonder tehuis (art. 243 — eenvoudiger berekening); (3) bijzonder regime ingekomen belastingplichtigen (BBIB sinds 2022 — art. 32/1).

<small>📖 WIB92 — art. 227 — 1° — _wettekst_ · WIB92 — art. 243-244 — _wettekst_</small>

#### 📜 BNI/nat MET tehuis in België (art. 244)

Een 'tehuis in België' = een woning of verblijfplaats die ter beschikking blijft staan voor regelmatig persoonlijk gebruik. De BNI-belastingplichtige met tehuis krijgt een berekening die de PB-regels integraal volgt (belastingvrije som, gezinsmodulering, ...) maar de grondslag blijft enkel de Belgische inkomsten. Typisch voor expats die regelmatig naar BE komen maar hun gezin elders hebben.

<small>📖 WIB92 — art. 244 — _wettekst_</small>

#### 📜 BNI/nat ZONDER tehuis in België (art. 243)

Geen tehuis in BE = vereenvoudigde berekening: tarieven van art. 130 WIB92 worden toegepast op het netto-belastbaar Belgisch inkomen, MAAR de belastingvrije som en de meeste persoonlijke aftrekken (huwelijksquotient, kinderlast) zijn UITGESLOTEN, tenzij art. 243/1 toepasselijk is (75 %-regel: belastbaar inkomen in BE ≥ 75 % van wereldwijd belastbaar inkomen → wel toegang tot persoonlijke aftrekken — Schumacker-doctrine HvJ).

<small>📖 WIB92 — art. 243 — _wettekst_ · WIB92 — art. 243/1 — _wettekst_</small>

### 📦 BNI/ven — belasting niet-inwoners vennootschappen

#### Definitie

BNI/ven treft buitenlandse vennootschappen (en bepaalde verenigingen zonder rechtspersoonlijkheid die in de andere staat als vennootschap behandeld worden) op hun Belgische bron-inkomsten. Twee hoofdcategorieën Belgische inkomsten (art. 233 WIB92): (1) winst van een Belgische VASTE INRICHTING; (2) inkomsten uit Belgisch onroerend goed dat geen VI-onderdeel uitmaakt. De berekening volgt de VenB-regels (tarief 25 %, KMO-tarief 20 % onder voorwaarden), maar enkel toegerekend op de BE-VI-winst of BE-OG-inkomsten — niet op het wereldwijde resultaat.

<small>📖 WIB92 — art. 227 — 2° — _wettekst_ · WIB92 — art. 228 + 233 — _wettekst_</small>

## Bouwstenen

### 📜 Categorieën Belgische bron-inkomsten (art. 228)

Art. 228 §2 WIB92 somt limitatief de Belgische bron-inkomsten op die in BNI vallen: (1) inkomsten uit in België gelegen onroerende goederen; (2) inkomsten uit beroepsactiviteit uitgeoefend in België via vaste inrichting of zonder VI maar fysiek hier; (3) bezoldigingen voor in België uitgeoefend werk (loon, bedrijfsleiderbezoldiging); (4) pensioenen ten laste van Belgische werkgevers; (5) dividenden van Belgische vennootschappen; (6) roerende inkomsten waarvan de schuldenaar in BE woont/gevestigd is en het inkomen toerekent op zijn Belgische resultaten; (7) royalty's voor in BE gebruikt IP; (8) diverse inkomsten (sportbeoefenaars, artiesten, prijzen, meerwaarden op Belgisch onroerend goed of op aandelen Belgische vennootschappen, etc.); (9) onderhoudsuitkeringen ten laste van Belgische rijksinwoners aan EER-ontvangers.

<small>📖 WIB92 — art. 228 §2 1°-9° — _wettekst_</small>

### ↪️ Vrijgestelde inkomsten BNI (art. 230)

Art. 230 WIB92 sluit bepaalde 'Belgische' inkomsten expliciet uit van BNI: (1) roerende inkomsten toegerekend op een buitenlandse inrichting van de schuldenaar; (2) bezoldigingen voor in het buitenland uitgevoerd werk dat toegerekend wordt op een buitenlandse inrichting; (3) inkomsten gedekt door een DBV die de heffingsbevoegdheid aan de woonstaat toewijst; (4) bepaalde rente uit Belgische overheidsobligaties voor niet-inwoners (typisch via art. 264). Het idee: niet alles wat 'door een Belgische schuldenaar' wordt betaald is daarom Belgisch belastbaar — de economische bron moet werkelijk in BE liggen.

<small>📖 WIB92 — art. 230 — 1° tot 5° — _wettekst_</small>

### 📏 Drempel 2.500 EUR onroerende inkomsten (art. 232)

Voor niet-rijksinwoners (art. 227 — 1°) met enkel BNI-belastbare inkomsten uit in BE gelegen onroerende goederen, wordt GEEN aanslag gevestigd indien het totale bedrag van die onroerende inkomsten lager is dan 2.500 EUR (niet-geïndexeerd). Bij gemeenschappelijke aanslag: drempel per echtgenoot. Triviale-inkomstendrempel om administratie-overlast te vermijden voor kleinere buitenlandse eigenaars.

<small>📖 WIB92 — art. 232 tweede + derde lid — _wettekst_</small>

### ⚙️ BNI-cascade — beslisboom toepassing

Cascade om vast te stellen of en hoe BNI van toepassing is. Een didactische stap-voor-stap-analyse die de stagiair eerst moet doorlopen vóór hij naar de tarieven gaat.

<small>🔗 WIB92 — art. 227-248 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Gelijkstelling BNI met PB of VenB (art. 238)

Voor de toepassing van de verschillende WIB92-bepalingen (aftrek beroepskosten art. 53, niet-aftrekbare kosten art. 198, ...) wordt de BNI gelijkgesteld met de PB (voor BNI/nat) of met de VenB (voor BNI/ven). Praktisch effect: alle aftrek- en niet-aftrek-regels van de PB/VenB werken doorgaans identiek in BNI. Dat houdt de structurele coherentie van de Belgische inkomstenbelasting overeind.

<small>📖 WIB92 — art. 238 — _wettekst_</small>

### 👣 BNI-aangifte en termijn (art. 305-308)

Aangifte-vorm: 276.1 voor BNI/nat (niet-rijksinwoners natuurlijke personen); 276.2 voor BNI/ven (buitenlandse vennootschappen). Termijn: standaard tegen einde september van het aanslagjaar (cijfer per aanslagjaar — Cijferzakboekje raadplegen). Buitenlandse vennootschappen die enkel Belgische onroerende goederen hebben: vaak via beperkte aangifte. Voor bezoldigingen aan buitenlandse werknemers werkt de bedrijfsvoorheffing typisch als bevrijdende inhouding (geen aangifte vereist als voldaan).

<small>🔗 WIB92 — art. 305-308 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Nederlandse zelfstandige consultant met Belgische vaste inrichting
> _Pieter de Bruin (Nederlandse rijksinwoner, gezin in Eindhoven) werkt 80 % van zijn tijd in Antwerpen, waar hij een gehuurd kantoor heeft als consultant. Belgisch jaaromzet 2026 = 120.000 EUR; bedrijfskosten 30.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — residentie: Pieter is Nederlands rijksinwoner (woonplaats + gezin Eindhoven) → geen Belgische PB.
> - Stap 2 — Belgisch aanknopingspunt: kantoor Antwerpen = vaste inrichting (art. 229 WIB92) → Belgische winst valt onder art. 228 §2 4° → BNI/nat van toepassing.
> - Stap 3 — DBV BE-NL: art. 7 OESO-MV (winst onderneming) → BE-VI-winst belastbaar in BE → BNI geldt.
> - Stap 4 — kwalificatie: BNI/nat (Pieter is natuurlijke persoon, geen vennootschap).
> - Stap 5 — berekening: heeft Pieter een 'tehuis' in BE? Nee (woont in Eindhoven, kantoor is enkel werkplek). → art. 243 (zonder tehuis). Netto VI-winst = 120.000 − 30.000 = 90.000 EUR. Tarieven PB toegepast op die 90.000 EUR. Belastingvrije som: geen (uitgesloten zonder tehuis), tenzij 75 %-regel art. 243/1 (80 % > 75 % → wel toegang tot Schumacker-aftrek).
> - Stap 6 — aangifte 276.1 indienen, deadline conform aanslagjaar.
>
> → **Resultaat**: BNI/nat op 90.000 EUR Belgische winst, met 75 %-regel toegang tot belastingvrije som omdat overwegend BE-inkomen.
>
> <small>🔗 WIB92 — art. 227 — 1° + art. 228 §2 4° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Duitse GmbH met Belgisch verkoopfiliaal
> _TechSolutions GmbH (Frankfurt) verkoopt machines in heel Europa. In 2024 opende ze een Brussels filiaal met 5 werknemers, eigen kantoor, lokale verkoopmanager met handtekenbevoegdheid. Belgisch resultaat 2026: omzet 2 M EUR, winst toe te rekenen aan VI = 250.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — residentie: TechSolutions GmbH heeft statutaire zetel + werkelijke leiding in Frankfurt → Duitse vennootschap, geen Belgische VenB.
> - Stap 2 — Belgisch aanknopingspunt: het Brusselse filiaal = vaste inrichting (art. 229 WIB92) + werknemers + handtekenbevoegdheid → VI bevestigd.
> - Stap 3 — DBV BE-DE: art. 7 → winst VI belastbaar in BE.
> - Stap 4 — kwalificatie: BNI/ven (art. 227 — 2°).
> - Stap 5 — berekening: VI-winst 250.000 EUR × 25 % VenB-tarief = 62.500 EUR Belgische BNI/ven (KMO-tarief 20 % niet beschikbaar — niet-residente entiteit).
> - Stap 6 — aangifte 276.2 indienen; voorafbetalingen volgens VenB-regime.
>
> → **Resultaat**: BNI/ven 62.500 EUR + eventuele opcentiemen/verhoging. In Duitsland mag GmbH die belasting verrekenen onder het DBV (vrijstellingsmethode in DE).
>
> <small>🔗 WIB92 — art. 227 — 2° + art. 233 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Alle Belgische uitkering = BNI-belastbaar
> **Verkeerde assumptie**: Elke euro die door een Belgische schuldenaar aan een buitenlandse partij wordt uitbetaald, is onderworpen aan BNI.
>
> **Kernpunt**: Art. 230 WIB92 sluit expliciet bepaalde uitkeringen UIT van BNI: roerende inkomsten toegerekend op een buitenlandse inrichting, bezoldigingen voor buitenlands werk, etc. Daarnaast kunnen DBVs de heffingsbevoegdheid aan de woonstaat toewijzen. Eerste check: art. 228 (BE-bron-inkomen?), tweede check: art. 230 (vrijgesteld?), derde check: DBV (toegewezen aan BE?).
>
> <small>📖 WIB92 — art. 230 — _wettekst_</small>

> [!warning]- Geen tehuis = geen aftrekken
> **Verkeerde assumptie**: Een BNI-belastingplichtige zonder Belgisch tehuis krijgt nooit toegang tot persoonlijke aftrekken zoals belastingvrije som of kinderlast.
>
> **Kernpunt**: Art. 243/1 WIB92 (Schumacker-regel) opent persoonlijke aftrekken voor EU-inwoners die ≥ 75 % van hun wereldwijd beroepsinkomen in BE behalen. HvJ-doctrine: niet-discriminatie vereist gelijke behandeling met BE-rijksinwoner wanneer de fiscale draagkracht in essentie in BE wordt belast. Vergeet die regel niet bij grensarbeiders en quasi-volledig-BE-werkenden zonder Belgische woning.
>
> <small>📖 WIB92 — art. 243/1 — _wettekst_</small>

> [!warning]- BNI/ven = vennootschapsbelasting
> **Verkeerde assumptie**: BNI/ven is gewoon een naam voor de Belgische vennootschapsbelasting voor buitenlanders.
>
> **Kernpunt**: BNI/ven volgt de VenB-mechanica (art. 238 gelijkstelling, tarieven 25 %) MAAR met fundamenteel andere grondslag: enkel Belgische bron-inkomsten (art. 233), niet het wereldwijde resultaat. Bovendien hebben BNI/ven-belastingplichtigen typisch GEEN toegang tot het KMO-tarief 20 % en sommige aftrekken (notionele-interestaftrek, ...). Examenvalkuil: behandel BNI/ven niet als 'kleine VenB'.
>
> <small>🔗 WIB92 — art. 227 — 2° + art. 233 + art. 238 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Buitenlandse ondernemer met Belgische activiteit

_De accountant die een buitenlandse cliënt begeleidt bij het opstarten van een Belgische activiteit (filiaal, vaste inrichting, onroerend goed)._

#### 💰 Fiscaal adviseur

##### 👣 Vaste-inrichting-toets vóór BNI-aangifte

Eerste stap voor een buitenlandse vennootschap met activiteit in BE: bepaal of er een vaste inrichting bestaat (art. 229 WIB92 + art. 5 OESO-MV). Zonder VI: geen BNI/ven op beroepsinkomen, wel mogelijke RV-inhoudingen op andere stromen (onroerend, royalty's). Met VI: volledige BNI/ven-aangifteplicht + winstallocatie via OESO-richtsnoeren transfer pricing. Documenteer de feitelijke setup (kantoorruimte, werknemers, bevoegdheden) als bewijsmiddel.

<small>🔗 WIB92 — art. 229 — _wettekst_ · OESO-modelverdrag — art. 5 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 DBV-toetsing per inkomenscategorie

Voor elke verwachte Belgische bron-inkomst: check het DBV met de woonstaat van de cliënt. Welke heffingsbevoegdheid? BE-uitsluitend, BE-gedeeld of woonstaat-uitsluitend? Voorbeeld: art. 7 (winst onderneming) — BE belast indien VI; art. 10 (dividenden) — BE bron-belasting beperkt door verdragstarief; art. 12 (royalty's) — vaak woonstaat-uitsluitend in moderne verdragen. Pas BNI alleen toe waar DBV BE-heffingsbevoegdheid toelaat.

<small>🔗 OESO-modelverdrag — art. 7-22 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Expat-werknemer in België

_De accountant die een buitenlandse werknemer met activiteit in België fiscaal begeleidt._

#### 💰 Fiscaal adviseur

##### 👣 Salary-split en 75 %-regel

Voor expats die in meerdere landen werken: bepaal het BE-deel van de bezoldiging op basis van werkdagen in BE (art. 15 OESO-MV — 183-dagen-test). Alleen het BE-deel is BNI-belastbaar. Indien het BE-deel ≥ 75 % van het wereldwijd beroepsinkomen vertegenwoordigt: art. 243/1 WIB92 geeft toegang tot belastingvrije som en gezinsmodulering (Schumacker-doctrine). Belangrijk bij grensarbeiders Nederland-België of Luxemburg-België.

<small>📖 WIB92 — art. 243/1 — _wettekst_ · OESO-modelverdrag — art. 15 — _modelverdrag_</small>

## Verder lezen (scope-out)

- → Fiscale residentie (afbakening rijksinwoner) → [[fiscale-residentie]] _(moet-verwijzen)_
- → Bijzonder regime buitenlandse kaderleden → [[bijzonder-regime-buitenlandse-kaderleden]] _(moet-verwijzen)_
- → Vaste inrichting (BNI-VenB-context) → [[vaste-inrichting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `vergelijkbaar_met`
- [[personenbelasting]]
    - **Gelijkenissen**:
        - Zelfde tarieven (art. 130 WIB92) toegepast via gelijkstelling (art. 238)
        - Zelfde structuur belastbare inkomstencategorieën
        - Zelfde aftrek-/niet-aftrek-regels (art. 53 / 198)
    - **Verschillen**:
        - PB: belasting op wereldwijd inkomen (onbeperkt); BNI: enkel Belgische bron-inkomsten (beperkt)
        - PB-belastingplichtige: Belgisch rijksinwoner; BNI-belastingplichtige: niet-rijksinwoner
        - PB: volledige belastingvrije som + persoonlijke aftrekken; BNI zonder tehuis (art. 243): geen belastingvrije som tenzij 75 %-regel art. 243/1 (Schumacker)
        - PB-aangifte: 276.1 voor inwoners; BNI-aangifte: 276.1 voor niet-inwoners, 276.2 voor buitenlandse vennootschappen
    - ⚠️ **Verwarringsrisico**: Studenten dupliceren PB-regels naar BNI zonder na te denken over de beperking van de grondslag. Examen-aandachtspunt: in BNI komt nooit het wereldwijde inkomen in de grondslag.
- [[vennootschapsbelasting]]
    - **Gelijkenissen**:
        - Zelfde VenB-tarief (25 %)
        - Zelfde berekening winst (boekhoudkundig resultaat + correcties)
    - **Verschillen**:
        - VenB: belasting op wereldwijde winst Belgische vennootschap; BNI/ven: enkel Belgische VI-winst en BE-onroerend
        - BNI/ven heeft geen toegang tot KMO-tarief 20 % en sommige aftrekken (notionele-interestaftrek)
    - ⚠️ **Verwarringsrisico**: BNI/ven behandelen als 'VenB voor buitenlanders' onderschat het territorialiteitsverschil.
### `vereist`
- [[fiscale-residentie]] — BNI grijpt enkel in wanneer de belastingplichtige GEEN Belgische fiscale residentie heeft (art. 227 WIB92, spiegelbeginsel met art. 2).
### `beinvloed_door`
- [[vaste-inrichting]] — Voor BNI/ven en BNI/nat-zelfstandigen bepaalt het bestaan van een Belgische vaste inrichting (art. 229 WIB92 + art. 5 OESO-MV) of de winst überhaupt in BE belastbaar is.
- [[dubbelbelastingverdrag]] — DBVs wijzen de heffingsbevoegdheid toe per inkomenscategorie — kunnen de BNI-grondslag verder beperken of tarieven verlagen.
