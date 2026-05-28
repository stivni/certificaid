---
title: "Autokosten"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
  - 2.3.taak.3
  - 2.4.taak.4
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/autokosten.json"
---

# Autokosten

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · `2.3.taak.3` · `2.4.taak.4` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

> [!warning] **Uitdovend regime** — wordt afgebouwd; check sinds-/tot-data.

**Synoniemen**: wagenkost · voertuigkost · bedrijfswagen-kosten — **Vertalingen**: fr: frais de voiture

## Definitie

🔗 Autokosten = het cluster van fiscale en boekhoudkundige regels rond de kosten verbonden aan een personenwagen, auto voor dubbel gebruik of minibus (artikel 65 WIB 92) die voor beroeps- of vennootschapsdoeleinden wordt gebruikt. Het regime regelt vier afzonderlijke maar verstrengelde dimensies: (1) de boekhoudkundige opname onder klasse 61 'Diensten en diverse goederen' en klasse 63 'Afschrijvingen'; (2) de aftrek-beperking in PB en VenB via een CO2-cascade (art. 66 §1 + 198bis WIB 92) met als basisformule 100 % − [120 % − (0,5 % × coëfficiënt × gr CO2/km)], maximaal 50 % en minimaal 40 % (60 % vanaf 200 gr/km); (3) de belasting van het persoonlijk gebruik via het voordeel van alle aard (VAA) op naam van de verkrijger (art. 36 §2 WIB 92) — cataloguswaarde × CO2-percentage × leeftijdspercentage × 6/7; en (4) de BTW-aftrek-beperking tot maximaal 50 % (art. 45 §2 WBTW), te bepalen via één van drie administratieve methodes.

<small>📚 WIB92 — art. 66 §1 — _wettekst_ · WIB92 — art. 198bis — _wettekst_ · WIB92 — art. 36 §2 — _wettekst_ · WIB92 — art. 198 §1, 9° en 9°bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Voor een gecertificeerd accountant is 'autokosten' een van de meest klassieke verworpen-uitgaven-bronnen in de VenB-aangifte (codes 1205 en 1206) en één van de typische valkuilen in de PB van bedrijfsleiders die een wagen via de vennootschap aanhouden. De kern-redenering: één economische uitgave (bijvoorbeeld een lease van 800 EUR/maand + 200 EUR brandstof) wordt voor de berekening van de belastbare basis driedubbel beperkt. Eerst wordt boekhoudkundig 100 % geboekt op klasse 61/63. Vervolgens wordt fiscaal slechts een percentage tussen 40 % en 100 % (vanaf AJ 2027 voor nieuwe wagens: doorgaans 0 %, behalve elektrisch) aanvaard — het verschil verschijnt als verworpen uitgave (code 1205). Wanneer de wagen ook privé wordt gebruikt en de werkgever-vennootschap de brandstof ten laste neemt, wordt bovenop 1205 een tweede VU geboekt: 40 % van het VAA (code 1206), dat tegelijk als beroepsinkomen wordt belast in de PB van de bedrijfsleider/werknemer. BTW-zijdig is maximaal 50 % aftrekbaar, met een dwingende keuze tussen drie ramings-methodes. De accountant beheert dus parallel: (a) MAR-klasse 61 boeking, (b) CO2-aftrek-formule per voertuig, (c) VAA-berekening per verkrijger, (d) BTW-methode-keuze.

<small>📚 WIB92 — art. 66 §1 — _wettekst_ · WIB92 — art. 198 §1, 9° en 9°bis — _wettekst_ · WIB92 — art. 36 §2 — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — codes 1205-1206 — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De wetgever wou twee doelen tegelijk realiseren: (1) het sociaal-fiscaal voordeel van een gratis bedrijfswagen weer correct belasten (art. 36 §2 — anders zou een loonsverhoging via wagen-on-top altijd voordeliger zijn dan cash); en (2) milieugedrag sturen door de aftrek te koppelen aan CO2-uitstoot. Sinds de hervorming-De Croo (W 25.11.2021) loopt een uitdoof-traject: wagens gekocht/geleased/gehuurd vóór 1 juli 2023 blijven onder de oude regel (max 100 %, min 50 %); wagens vanaf 1 juli 2023 tot 31 december 2025 zijn geplafonneerd op 50 %; wagens vanaf 1 januari 2026 zijn 0 % aftrekbaar tenzij CO2-uitstoot = 0 (volledig elektrisch). De overgangsbepaling staat in artikel 550 WIB 92 en bouwt het aftrektarief af tussen AJ 2026 (75 %) en AJ 2031 (50 %) voor wagens van vóór 1 januari 2018. Dat verklaart waarom de stagiair op het examen voertuig-per-voertuig moet redeneren op basis van AANKOOPDATUM, niet aanslagjaar.

<small>📚 WIB92 — art. 550 — _wettekst_ · WIB92 — art. 66 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `uitdovend` · sinds **2023-07-01** · basis: Wet 25.11.2021 houdende fiscale en sociale vergroening van de mobiliteit (B.S. 03.12.2021) + W 22.12.2023

Het oude regime (max 100 %, min 50 %) loopt uit voor wagens gekocht/geleased/gehuurd vóór 1 juli 2023. Wagens 1 juli 2023 – 31 december 2025 zijn intermediair (max 50 %). Wagens vanaf 1 januari 2026 zijn 0 % aftrekbaar tenzij volledig elektrisch (art. 66 §1/1 + art. 550 WIB 92). De aftrek voor laadstations daalt vanaf 1 januari 2030 naar 75 % (art. 66 §6 WIB 92). De stagiair moet per dossier de aankoopdatum nakijken voor de juiste regel.

**✅ Voor**
- 📖 Vennootschap die een bedrijfswagen aankoopt, leaset of huurt voor gebruik door bedrijfsleider of werknemer — al dan niet met persoonlijk gebruik.
- 📖 Zelfstandige in PB die een wagen gebruikt voor beroepsverplaatsingen — kostenaftrek met dezelfde CO2-cascade.
- 📖 Werknemer of bedrijfsleider die een eigen wagen gebruikt voor woon-werkverplaatsingen: forfait 0,15 EUR/afgelegde kilometer (art. 66 §4 WIB 92).

**🚫 Niet voor**
- 📖 Voertuigen uitsluitend gebruikt voor taxidienst, verhuring met bestuurder (vrijgesteld van verkeersbelasting), autorijschool-onderricht of uitsluitend verhuur aan derden — geen aftrekbeperking.
- 🔗 Lichte vrachtwagens en bestelwagens (N1-categorie volgens WIGB) — die vallen onder de algemene beroepskostenaftrek, niet onder de CO2-cascade. Let op: door bouw kan een wagen die als 'auto voor dubbel gebruik' wordt gepresenteerd toch fiscaal een personenwagen zijn.

**▶️ Trigger start**
- 📖 Aanschaf / lease-start / huur-start van een voertuig art. 65 WIB 92 door de onderneming of door bedrijfsleider/werknemer voor beroepsdoel. De AANKOOPDATUM bepaalt het toepasselijke regime (vóór 01.07.2023 = oud; 01.07.2023 – 31.12.2025 = intermediair; vanaf 01.01.2026 = nieuw).

**⚠️ Risico**
- 📖 Dubbele verworpen-uitgave-fout: 1205 (CO2-aftrek-beperking op TOTALE kost incl. brandstof) en 1206 (40 % of 17 % van VAA) worden BEIDE geboekt; ze zijn cumulatief en niet alternatief. Schermt de stagiair dat niet correct af, dan onder-schat hij de belastbare basis met meerdere duizenden euro per wagen.
- 📖 Valse-hybride-trap: oplaadbare hybride aangekocht vanaf 1 januari 2018 met batterij < 0,5 kWh/100 kg of CO2 > 50 gr/km wordt fiscaal gelijkgesteld met het overeenkomstig brandstof-voertuig (× 2,5 als geen equivalent bestaat). Vergeten te checken = veel te hoge aftrek én te laag VAA.
- 📖 Forgetten plug-in-hybride brandstof-minimum 50 % vanaf 01.01.2023 — voor benzine-/dieselkosten van een vanaf 01.01.2023 aangekocht oplaadbaar hybridevoertuig is het aftrek-percentage minstens 50 %, ongeacht de gewone CO2-formule.

## Bouwstenen

### 🧮 CO2-aftrekformule (art. 66 §1 + 198bis WIB 92)  
_`formule`_

📖 Aftrek-tarief = 100 % − [120 % − (0,5 % × coëfficiënt × gr CO2/km)], met coëfficiënt = 1 voor diesel · 0,95 voor benzine/andere · 0,90 voor aardgas < 12 fiscale PK. Resultaat in PB en VenB BEGRENSD op maximaal 50 % en minimaal 40 %. Uitzondering: 60 % indien CO2 ≥ 200 gr/km of geen CO2-data bij DIV. Resultaat wordt afgerond tot de hogere/lagere tiende naargelang het cijfer van de honderdsten al dan niet 5 bereikt.

<small>📚 WIB92 — art. 66 §1 — _wettekst_ · WIB92 — art. 198bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1205 — aftrekformule autokosten — _aangifte_</small>

**Rationale**: 🔗 De formule is een dubbele cascade: hoe meer CO2 een voertuig uitstoot, hoe lager de aftrek. Onder 200 gr/km blijft minstens 40 % aftrekbaar; boven 200 gr/km bedraagt het tarief vast 60 % (let op: een hard 60 % zonder minimum 40 % is HOGER dan wat de formule onder 200 gr/km soms zou geven — de wetgever heeft hier een 'cliff' ingebouwd om sterk vervuilende wagens niet onbeperkt nadelig te behandelen).

<small>📚 WIB92 — art. 66 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 VAA-auto-formule (art. 36 §2 WIB 92)  
_`formule`_

📖 VAA = cataloguswaarde × CO2-percentage × leeftijdspercentage × (6/7). De cataloguswaarde is de catalogusprijs nieuw incl. opties en werkelijk betaalde BTW, zónder kortingen. Het CO2-basispercentage bedraagt 5,5 % bij een referentie-CO2 van 95 gr/km (diesel) of 115 gr/km (benzine/LPG/aardgas), met ±0,1 %-punt per gram afwijking, begrensd op 4 % (min) en 18 % (max). Het leeftijdspercentage daalt per schijf van 12 maanden vanaf eerste inschrijving: 100 % (0-12 m) → 94 % → 88 % → 82 % → 76 % → 70 % (vanaf 61 maanden). Het VAA mag nooit minder bedragen dan 820 EUR per jaar (niet-geïndexeerd basisbedrag; jaarlijks geïndexeerd in het Cijferzakboekje). Eigen bijdrage van de verkrijger wordt in mindering gebracht.

<small>📚 WIB92 — art. 36 §2 eerste tot twaalfde lid — _wettekst_</small>

### 📜 BTW-aftrek max 50 % personenwagen (art. 45 §2 WBTW)  
_`regel`_

🔗 Voor BTW geheven op de aankoop, huur, lease, brandstof, onderhoud en herstellingen van een personenwagen / auto voor dubbel gebruik is de aftrek beperkt tot maximaal 50 %. Het werkelijke beroepsmatige gebruik wordt geraamd via één van drie administratieve methodes (administratieve beslissing E.T.119.650 van 20.10.2011 + opvolgers): (1) METHODE 1 — werkelijk gebruik via volledige kilometeradministratie per wagen per jaar; (2) METHODE 2 — semi-forfait met formule: % privé = ((afstand-woon-werk × 200 × 2) + 6.000) / totale_km × 100, vervolgens % beroep = 100 − % privé, geplafonneerd op 50 %; (3) METHODE 3 — algemeen forfait 35 % beroepsgebruik (toepasbaar op heel het wagenpark mits ≥ 4 wagens en geen werkelijk gebruik). Eens gekozen geldt de methode per kalenderjaar.

<small>📚 WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

**Rationale**: 🔗 De 50 %-cap is een onweerlegbaar plafond: zelfs als een wagen 100 % beroepsmatig zou worden gebruikt, blijft de BTW-aftrek beperkt tot 50 %. Dat is een Europese afwijking onder art. 176 BTW-Richtlijn. Methode 1 is precies maar administratief zwaar (volle km-registratie); methode 2 is een redelijke mix; methode 3 is alleen interessant voor flottes ≥ 4 wagens.

<small>📚 WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Verworpen uitgave code 1205 — niet-aftrekbare autokosten  
_`regel`_

📖 Het niet-aftrekbare gedeelte van TOTALE autokosten (lease, afschrijving, brandstof, onderhoud, verzekering, BIV, verkeersbelasting) en het niet-aftrekbare gedeelte van verwezenlijkte minderwaarden op autovoertuigen wordt geboekt als verworpen uitgave onder code 1205 in de VenB-aangifte. Berekening per voertuig op basis van de CO2-cascade (zie co2-formule-venb). Voor minderwaarden geldt een aparte ratio: tarief = 100 − [(som fiscaal aanvaarde afschrijvingen, per BT beperkt tot 100 %) / (som geboekte afschrijvingen voor dezelfde BT)] × 100.

<small>📚 aangifte-VenB-2025-verworpen-uitgaven — code 1205 — _aangifte_ · WIB92 — art. 66 §1 vijfde lid — _wettekst_ · WIB92 — art. 198bis — _wettekst_</small>

### 📜 Verworpen uitgave code 1206 — autokosten ten belope van gedeelte VAA  
_`regel`_

📖 Voor voertuigen die kosteloos of niet voor persoonlijk gebruik ter beschikking zijn gesteld, is een ADDITIONEEL stuk autokost verworpen: (a) 40 % van het VAA (vóór bijdrage van de verkrijger) wanneer de brandstofkosten verbonden met dit persoonlijk gebruik geheel of gedeeltelijk door de vennootschap ten laste worden genomen (art. 198 §1, 9°bis WIB 92); (b) 17 % van het VAA wanneer geen brandstof door de vennootschap wordt gedragen (art. 198 §1, 9° WIB 92). Dit komt BOVENOP code 1205 — niet in de plaats van.

<small>📚 WIB92 — art. 198 §1, 9° — _wettekst_ · WIB92 — art. 198 §1, 9°bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1206 — _aangifte_</small>

**Rationale**: 🔗 Economische logica: de vennootschap genereert een aftrekbare loonkost (de wagen + brandstof) maar slechts een deel daarvan wordt geneutraliseerd door belasting op de werknemer (het VAA). Het verschil tussen werkelijke kostprijs en VAA is een 'verborgen' loonsubsidie. De wetgever recupereert die door 40 %/17 % van het VAA als VU aan de vennootschap aan te rekenen.

<small>📚 WIB92 — art. 198 §1, 9°bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Overgangsregime aftrek per aankoopdatum (art. 550 WIB 92)  
_`regel`_

📖 Voor voertuigen aangekocht/geleased/gehuurd VÓÓR 1 JANUARI 2026 geldt art. 550 WIB 92 ipv het nieuwe art. 66 §1/1. Drie subregimes: (a) Aankoop VÓÓR 1.7.2023 — oude formule, min 50 %, max 100 % (uitz. 40 % bij ≥ 200 gr/km of geen DIV-data); voor vóór-2018-wagens een uitdoof-traject naar AJ (min 75 % AJ 2026 → 70 % AJ 2027 → 65 % AJ 2028 → 60 % AJ 2029 → 55 % AJ 2030 → 50 % vanaf AJ 2031). (b) Aankoop 1.7.2023 – 31.12.2025 — formule met max 50 % (tenzij CO2 = 0: dan ongeplafonneerd). (c) Plug-in hybride aangekocht 1.7.2023 – 31.12.2025 — eigen tarievenstaffel. Vanaf 1.1.2026 (= art. 66 §1/1) zijn niet-elektrische wagens 0 % aftrekbaar.

<small>📚 WIB92 — art. 550 — _wettekst_</small>

### ↪️ Valse-hybride-correctie (art. 36 §2 tiende lid)  
_`uitzondering`_

📖 Een oplaadbare hybride aangekocht vanaf 1 januari 2018 met (a) batterij met energiecapaciteit < 0,5 kWh per 100 kg wagengewicht OF (b) CO2-uitstoot > 50 gr/km (resp. > 75 gr/km bij Euro 6e-bis-1-norm of later) wordt als VALSE HYBRIDE behandeld. De in aanmerking te nemen CO2-uitstoot wordt dan gelijkgesteld met die van het OVEREENSTEMMEND voertuig met enkel een verbrandingsmotor en dezelfde brandstof. Bestaat geen overeenstemmend voertuig, dan wordt de uitstootwaarde × 2,5. De FOD Financiën publiceert een lijst valse hybrides. Niet van toepassing op hybrides aangekocht vóór 01.01.2018.

<small>📚 WIB92 — art. 36 §2 tiende lid — _wettekst_ · KB/WIB 92 — art. 19 — _kb_</small>

### ⚙️ Boekhoudkundige plaatsing autokosten — MAR klasse 61 + 63  
_`mechanisme`_

📖 Autokosten worden boekhoudkundig opgedeeld over de MAR-rekeningen: lease- en huurkosten op 61040 'Huur rollend materieel: bedrijfswagens' / 61041 'Huur rollend materieel: personenwagens'; onderhoud en herstellingen op 61140 / 61141; brandstof, verzekering, BIV, verkeersbelasting en parking op andere 61-subrekeningen of op 64 (Andere bedrijfskosten — voor belastingen als verkeersbelasting/BIV als bedrijfskost). Afschrijvingen op 6302 'Afschrijvingen op materiële vaste activa'. De BOEKHOUDKUNDIGE opname is volledig (100 %); de FISCALE beperking gebeurt extra-comptabel in de aangifte via codes 1205 en 1206.

<small>📚 MAR — KB 21.10.2018 Bijlage 1 — klasse 6, rekeningen 610-611-630 — _kb_ · CBN-advies 2016/26 — boekhoudkundige verwerking kilometerheffing — diensten en diverse goederen — _cbn_</small>

**Rationale**: 🔗 De scheiding boekhoudkundig (100 %) / fiscaal (beperkt) is een vaste accountant-reflex: in de jaarrekening verschijnt de werkelijke economische kost, in de fiscale aangifte wordt het niet-aftrekbare deel toegevoegd aan de belastbare basis via verworpen uitgaven. Daardoor blijft de boekhouding consistent met de werkelijkheid en wordt de fiscale correctie traceerbaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 BIV en verkeersbelasting (Vlaams gewest — VCF)  
_`regel`_

📖 De Belasting op de Inverkeerstelling (BIV) voor personenauto's, auto's voor dubbel gebruik en minibussen wordt in Vlaanderen berekend volgens een CO2-gebaseerde formule (VCF art. 2.3.4.1.2 voor wagens vóór 1.1.2021; art. 2.3.4.1.2/1 voor nieuwere). De belasting bedraagt nooit minder dan 41,99 EUR en nooit meer dan 10.497,70 EUR; voor wegvoertuigen die ≥ 30 jaar geleden voor de eerste keer in het verkeer kwamen geldt het minimum van 41,99 EUR (oldtimer-regeling, art. 2.3.4.1.3). Voor wagens zonder gekende CO2-uitstoot wordt deze afgeleid uit brandstof, cilinderinhoud en euronorm (art. 2.3.4.1.6). Brussel en Wallonië hebben eigen formules.

<small>📚 VCF — art. 2.3.4.1.2 — _wettekst_ · VCF — art. 2.3.4.1.2/1 — _wettekst_ · VCF — art. 2.3.4.1.3 — _wettekst_ · VCF — art. 2.3.4.1.6 — _wettekst_</small>

### 📜 Woon-werk-km-vergoeding met eigen wagen — forfait 0,15 EUR/km  
_`regel`_

📖 Wie zijn eigen wagen gebruikt voor verplaatsingen tussen woonplaats en plaats van tewerkstelling kan in PB de beroepskosten daarvoor forfaitair aftrekken aan 0,15 EUR per afgelegde kilometer (art. 66 §4 WIB 92), op voorwaarde dat het voertuig zijn eigendom is, op zijn naam ingeschreven, via bestendige huur/lease ter beschikking is, of toebehoort aan werkgever/vennootschap met VAA op naam belast (art. 66 §5). Voor twee echtgenoten of ouder-kind die samen rijden mag het forfait slechts aan één persoon worden toegekend voor het gezamenlijk afgelegde traject. Voor woon-werk met bedrijfswagen valt deze forfait WEG (er is dan VAA in plaats van km-vergoeding).

<small>📚 WIB92 — art. 66 §4 — _wettekst_ · WIB92 — art. 66 §5 — _wettekst_</small>

### 📜 Aftrek laadstations elektrische wagens  
_`regel`_

📖 Kosten met betrekking tot laadstations voor elektrische wagens zijn 100 % aftrekbaar (uitzondering 5° in art. 66 §2 WIB 92). Vanaf 1 januari 2030 worden de kosten van vanaf die datum aangekochte/geleased/gehuurde laadstations slechts ten belope van 75 % aftrekbaar (art. 66 §6 nieuw).

<small>📚 WIB92 — art. 66 §2, 5° — _wettekst_ · WIB92 — art. 66 §6 (vanaf 1.1.2030) — _wettekst_</small>

## Voorbeelden

### 💡 VAA-berekening — werknemer met benzine-bedrijfswagen 18 maanden oud 🔗

_Een vennootschap stelt aan haar werknemer een benzine-personenwagen ter beschikking, ook voor persoonlijk gebruik. Catalogusprijs nieuw (incl. opties + werkelijk betaalde BTW): 50.000 EUR. CO2-uitstoot: 130 gr/km. Eerste inschrijving: 14 maanden geleden (= leeftijdsklasse 13-24 maanden → 94 %). De vennootschap neemt ook de brandstof voor persoonlijk gebruik ten laste. Geen eigen bijdrage van de werknemer. Referentie-CO2 benzine: 115 gr/km._

**Berekening:**
- Stap 1 — CO2-percentage: basis 5,5 % bij ref 115 g/km. Voertuig 130 g/km → 15 g boven referentie → 5,5 % + (15 × 0,1 %) = 7,0 %. (Plafond max 18 % niet bereikt.)
- Stap 2 — Leeftijdspercentage: 94 % (leeftijdsklasse 13-24 m).
- Stap 3 — Toepassen formule: VAA = 50.000 × 7,0 % × 94 % × (6/7) = 50.000 × 0,07 × 0,94 × 0,857142 = 2.820,00 EUR/jaar (afgerond).
- Stap 4 — Vergelijken met minimum 820 EUR (geïndexeerd in Cijferzakboekje). 2.820 > minimum → behouden.
- Stap 5 — Geen eigen bijdrage → belastbaar VAA op naam werknemer = 2.820 EUR/jaar.
- Stap 6 — VU in vennootschap (code 1206): 40 % × 2.820 = 1.128 EUR (brandstof door vennootschap gedragen → 40 %, niet 17 %).

→ **Resultaat**: Werknemer: 2.820 EUR belastbaar als beroepsinkomen. Vennootschap: 1.128 EUR verworpen uitgave (code 1206), bovenop CO2-aftrek-beperking (code 1205).

<small>📚 WIB92 — art. 36 §2 — _wettekst_ · WIB92 — art. 198 §1, 9°bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 CO2-aftrek-cascade — diesel-wagen 140 gr/km, aangekocht 2024 🔗

_Vennootschap heeft op 15 mei 2024 een diesel-personenwagen geleased voor 12.000 EUR/jaar (lease + onderhoud + verzekering). CO2-uitstoot: 140 gr/km. AJ 2026 (boekjaar = kalenderjaar 2025). Aankoop binnen vensters 1.7.2023 – 31.12.2025 → art. 550 vierde lid: tarief uit formule MET max 50 %._

**Berekening:**
- Stap 1 — Formule: 100 % − [120 % − (0,5 % × 1 × 140)] = 100 − [120 − 70] = 100 − 50 = 50 %.
- Stap 2 — Plafond toepassing: art. 550 vierde lid plafonneert op MAX 50 % voor wagens vanaf 1.7.2023 → resultaat blijft 50 %.
- Stap 3 — Aftrekbaar = 50 % × 12.000 = 6.000 EUR.
- Stap 4 — Verworpen uitgave (code 1205) = 12.000 − 6.000 = 6.000 EUR.
- Stap 5 — Indien dezelfde wagen vanaf 1.1.2026 zou worden aangekocht: art. 66 §1/1 → 0 % aftrek (niet-elektrisch) → VU 12.000 EUR.

<small>📚 WIB92 — art. 66 §1 — _wettekst_ · WIB92 — art. 550 — _wettekst_</small>

### 💡 Boekhoudkundige verwerking — maandelijkse lease bedrijfswagen + tankbeurt 🔗

_Maandelijkse lease-factuur 800 EUR + 21 % BTW = 968 EUR. Tankkaart-factuur brandstof voor de wagen: 200 EUR + 21 % BTW = 242 EUR. BTW-methode 2 met % beroep berekend op 50 % (max)._

**Boeking:**

- C `61040`  — Huur rollend materieel — bedrijfswagens
- C `411`  — Aftrekbare BTW (50 % van 168)
- C `61040`  — Niet-aftrekbare BTW als kost (50 % van 168)
- C `440`  — Leveranciers

**Boeking:**

- C `61210`  — Brandstof rollend materieel
- C `411`  — Aftrekbare BTW (50 %)
- C `61210`  — Niet-aftrekbare BTW als kost (50 %)
- C `440`  — Leveranciers

Effectief geboekte kost in 61040 + 61210 = 1.105 EUR (884 lease incl. niet-aftrekbare BTW + 221 brandstof incl. niet-aftrekbare BTW). Op deze 1.105 EUR wordt EXTRA-COMPTABEL de CO2-cascade toegepast voor de VenB-aangifte (code 1205). De niet-aftrekbare BTW wordt MEE in de basis voor 1205 genomen (zij maakt deel uit van de werkelijke autokost).

<small>📚 MAR — KB 21.10.2018 Bijlage 1 — rekeningen 61040, 61210 — _kb_ · WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ 1205 én 1206 zijn cumulatief, niet alternatief

**Verkeerde assumptie**: Stagiairs denken vaak dat als ze code 1205 hebben geboekt (CO2-aftrek-beperking op de totale wagenkost), code 1206 niet meer moet — omdat 'het VAA al fiscaal verwerkt is op de werknemer'.

**Kernpunt**: Code 1205 corrigeert de TOTALE wagenkost in de vennootschap voor het CO2-element. Code 1206 voegt DAARBOVENOP een extra verworpen uitgave toe van 40 % (brandstof door vennootschap) of 17 % (geen brandstof) van het VAA, want de fiscale wetgever wil het verschil tussen werkelijke wagenkost en VAA dat als 'loonsubsidie' werkt, opnieuw belasten. Beide codes moeten dus IN PARALLEL worden ingevuld.

<small>📚 WIB92 — art. 198 §1, 9° en 9°bis — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — codes 1205 + 1206 — _aangifte_</small>

### ⚠️ Aanslagjaar versus aankoopdatum

**Verkeerde assumptie**: De aftrek-regel volgt het aanslagjaar van de aangifte.

**Kernpunt**: Voor autokosten geldt het regime van de AANKOOP-/LEASE-/HUURDATUM van het voertuig, niet het aanslagjaar. Een wagen aangekocht op 30 juni 2023 valt onder het OUDE regime (min 50 %, max 100 %) tot zijn afschrijving op; een wagen aangekocht op 1 juli 2023 valt onder het MAX-50 %-regime; een wagen aangekocht vanaf 1 januari 2026 valt onder 0 %-aftrek. Op het examen moet de stagiair dus per voertuig opzoeken WANNEER de aanschaffingsovereenkomst werd getekend (art. 550 WIB 92).

<small>📚 WIB92 — art. 550 — _wettekst_</small>

### ⚠️ Valse hybride niet als hybride behandelen

**Verkeerde assumptie**: Een plug-in hybride krijgt automatisch het gunstige CO2-tarief uit de homologatie (typisch 30-50 gr/km).

**Kernpunt**: Sinds 1.1.2018 kwalificeert een plug-in hybride met batterij < 0,5 kWh per 100 kg of CO2 > 50 gr/km als VALSE HYBRIDE. Voor zowel art. 36 §2 (VAA) als art. 66 §1 (aftrek) wordt het CO2-cijfer dan VERVANGEN door dat van het equivalente brandstof-voertuig (of × 2,5 als geen equivalent bestaat). Niet checken = volledig verkeerde VAA en aftrek.

<small>📚 WIB92 — art. 36 §2 tiende lid — _wettekst_</small>

### ⚠️ BTW-aftrek 50 % blokkeert niet de bovengrens, maar PLAFONNEERT die

**Verkeerde assumptie**: Als je 80 % beroepsmatig gebruik aantoont via een volledig kilometerschrift, mag je 80 % BTW aftrekken.

**Kernpunt**: Ook bij methode 1 (werkelijk gebruik) is de BTW-aftrek op personenwagens art. 45 §2 WBTW HARD geplafonneerd op 50 %, ongeacht het werkelijke beroepsmatige gebruik. De methodes bepalen wel of je ONDER 50 % zit, nooit erboven. (Uitzondering: voor lichte vracht-wagens en voor wagens onder art. 66 §2 WIB 92 (taxidienst, verhuur, autorijschool, doorgerekend aan derden) gelden andere BTW-regels.)

<small>📚 WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Speelruimtes

### 🎚️ Keuze BTW-aftrek-methode personenwagen

### 🎚️ Wagen via vennootschap of cash-equivalent als loonsverhoging

## Accountant-perspectieven

### Vennootschap die wagen ter beschikking stelt

_De vennootschap is fiscaal-juridisch eigenaar of lessee van de wagen. De accountant beheert hier boekhouding, fiscale aangifte (codes 1205-1206 + VAA op fiche), BTW-aangifte en advies over wagenkeuze._

#### 📒 Boekhouder

##### 👣 Boekhoudkundige inboeking lease- of aankoopcyclus  
_`stap`_

🔗 Bij lease: maandelijkse factuur op 61040/61041 (Huur rollend materieel), niet-aftrekbare BTW (50 % cap of methode-specifiek) bijgevoegd op dezelfde kostrekening. Bij aankoop: actief op 241 'Rollend materieel' tegen aanschaffingswaarde + niet-aftrekbare BTW; afschrijving op 6302 over 4 of 5 jaar lineair (uitzondering: degressief uitgesloten voor personenwagens, art. 64 WIB 92). Brandstof op 61210, onderhoud op 61140/61141, verzekering op 615, BIV en verkeersbelasting op 640 (Andere bedrijfskosten — belastingen).

<small>📚 MAR — KB 21.10.2018 Bijlage 1 — klasse 61, 63, 64 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 VAA op fiche 281.10 (werknemer) of 281.20 (bedrijfsleider)  
_`stap`_

🔗 Het belastbaar VAA-bedrag voor het kalenderjaar wordt jaarlijks op fiche 281.10 (werknemer) of 281.20 (bedrijfsleider) vermeld onder code 'voordeel van alle aard — bedrijfswagen'. Maandelijks wordt op het loonbriefje een twaalfde geboekt; bedrijfsvoorheffing wordt berekend op brutoloon INCL. dat maandelijks VAA. Boekhoudkundig: 620 (Bezoldigingen) tegen 455 of 489 — afhankelijk van of een netto-uitbetaling of een louter VAA. In de praktijk wordt het VAA als 'gross-up' op brutoloon geboekt zodat bedrijfsvoorheffing klopt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 VenB-aangifte codes 1205 + 1206 invullen  
_`stap`_

📖 Bij vak Verworpen uitgaven (vak B van de VenB-aangifte): (1) code 1205 = niet-aftrekbaar deel van de TOTALE wagenkost (lease/afschrijving/brandstof/onderhoud/verzekering/verkeersbelasting/niet-aftrekbare BTW) op basis van de CO2-formule per wagen; (2) code 1206 = 40 % (brandstof door vennootschap) of 17 % (geen brandstof) van het VAA per begunstigde. Per wagen apart berekenen — een KMO met 5 verschillende wagens heeft 5 sub-berekeningen.

<small>📚 aangifte-VenB-2025-verworpen-uitgaven — codes 1205 + 1206 — _aangifte_ · WIB92 — art. 198 §1, 9° en 9°bis — _wettekst_</small>

##### 👣 BTW-methode-keuze + herziening  
_`stap`_

🔗 Eind van het kalenderjaar (uiterlijk in de aangifte van 1e kwartaal of januari N+1) wordt de werkelijke jaarlijkse beroepsmatige aftrek berekend en wordt een herziening geboekt (rooster 61 of 62 van de BTW-aangifte) om het verschil tussen de voorlopig toegepaste aftrek en het werkelijke percentage recht te zetten. Eens een methode voor een wagen gekozen is, blijft die voor het hele kalenderjaar gelden — wijziging mag enkel op 1 januari van een nieuw jaar.

<small>📚 WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Wagenkeuze-advies voor klanten — overgang 2026  
_`vuistregel`_

🔗 Voor klanten die in 2026 een nieuwe wagen overwegen: (1) niet-elektrisch = 0 % aftrek → economisch zelden te verantwoorden vergeleken met cash of mobiliteitsbudget; (2) volledig elektrisch = 100 % aftrek (afnemend in jaren) + lager VAA (geen brandstof-VU) + lagere RSZ-CO2-bijdrage; (3) lopende lease/eigendom: laten doorlopen onder art. 550 — wisselen kost potentiële minderwaarde. Reken altijd het integraal kost-plaatje per scenario over de volledige bezitstermijn (4-5 jaar) inclusief residu-waarde.

<small>📚 WIB92 — art. 66 §1/1 + 550 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Bedrijfsleider/werknemer met bedrijfswagen

_De persoon op wiens naam het VAA wordt belast. Vooral relevant voor de PB-aangifte van de bedrijfsleider — een dossier dat de accountant typisch ook voor zijn cliënt-natuurlijke-persoon behandelt._

#### 💰 Fiscaal adviseur

##### 👣 VAA-bedrijfswagen op PB-aangifte  
_`stap`_

🔗 Het VAA dat op fiche 281.10/281.20 staat, wordt overgenomen in vak IV (bezoldigingen werknemers) of vak XVII (bezoldigingen bedrijfsleiders) van de PB-aangifte. Het draagt eigen bedrijfsvoorheffing en sociale-zekerheids-effecten (in vennootschapscontext geen RSZ op VAA-wagen, maar wel CO2-solidariteits-bijdrage; in werknemerscontext WEL gewone RSZ op VAA op brutoloon-basis). De stagiair moet hier zorgen dat het VAA-bedrag op de fiche overeenstemt met de werkelijke periodes van terbeschikkingstelling.

<small>📚 WIB92 — art. 36 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Eigen bijdrage werknemer in mindering brengen  
_`regel`_

📖 Wanneer de werknemer een eigen bijdrage betaalt voor het persoonlijk gebruik van de wagen (typisch maandelijkse 'auto-bijdrage' van 50-200 EUR), wordt deze in mindering gebracht op het bruto-VAA (art. 36 §2 laatste lid). Resultaat: lager netto-VAA → lagere belasting. De accountant moet checken dat de eigen bijdrage daadwerkelijk wordt ingehouden op het loonbriefje (NIET enkel contractueel afgesproken).

<small>📚 WIB92 — art. 36 §2 laatste lid — _wettekst_</small>

## Verder lezen (scope-out)

- → Mobiliteitsbudget als alternatief → [[mobiliteitsbudget]] _(moet-verwijzen)_
- → Cash-for-car (mobiliteitsvergoeding) → [[cash-for-car]] _(moet-verwijzen)_
- → Woon-werkverkeer + km-vergoeding zonder bedrijfswagen → [[woon-werkverkeer-en-km-vergoeding]] _(moet-verwijzen)_
- ↪ Vaste-activa-presentatie generiek → [[vaste-activa]] _(mag-verwijzen)_
- ↪ Verworpen-uitgaven-filter-categorie (algemeen) _(mag-verwijzen)_

## Relaties

### `vergelijkbaar_met`
- [[mobiliteitsbudget]] — Mobiliteitsbudget is een wettelijk alternatief voor de klassieke bedrijfswagen, met 3 pijlers (groene wagen / duurzame woning-vervoer / cash met sociale bijdrage). Vanaf 2026 wordt het regime relatief gunstiger naarmate niet-elektrische bedrijfswagens 0 % aftrek krijgen.
    - **Gelijkenissen**:
        - Beide regimes regelen vergoeding voor mobiliteit van werknemer/bedrijfsleider
        - Beide worden gekoppeld aan inhouding op brutoloon of werkgeversbijdrage
    - **Verschillen**:
        - Autokosten: vennootschap heeft eigendoms-/lease-relatie met de wagen + VAA-belasting; mobiliteitsbudget: budgetbedrag dat werknemer verdeelt over 3 pijlers
        - Autokosten: aftrek-beperking via CO2-cascade; mobiliteitsbudget: andere fiscale behandeling per pijler
        - Autokosten: vanaf 2026 0 % aftrek voor niet-elektrisch; mobiliteitsbudget: blijft toegankelijk
    - ⚠️ **Verwarringsrisico**: Een klant kan denken dat zijn 'auto via de zaak' al een mobiliteitsbudget IS — fout. Mobiliteitsbudget vereist expliciete keuze en wettelijke procedure (W 17.03.2019).
- [[cash-for-car]] — Cash-for-car (mobiliteitsvergoeding) is een UITDOVEND alternatief: werknemer gaf zijn bedrijfswagen op in ruil voor een cash-bedrag berekend op de cataloguswaarde × 20 % × 6/7. Geen nieuwe toegang sinds 1.1.2026; bestaande contracten lopen door.
    - **Gelijkenissen**:
        - Beide regimes vertrekken vanuit de cataloguswaarde van een hypothetische bedrijfswagen
        - Beide kennen een PB-impact en sociale-zekerheidsbehandeling
    - **Verschillen**:
        - Autokosten: werknemer rijdt MET een wagen + VAA + 1205/1206 in vennootschap; cash-for-car: werknemer rijdt zelf, vennootschap heeft GEEN wagen meer, krijgt cash
        - Cash-for-car is uitdovend (geen nieuwe instappers); autokosten blijven actief (zij het minder gunstig voor niet-elektrisch)
    - ⚠️ **Verwarringsrisico**: Het 6/7-mechanisme komt in beide voor (in VAA én in cash-for-car-formule), maar betekent fiscaal niet hetzelfde.
- [[woon-werkverkeer-en-km-vergoeding]] — Werknemer/bedrijfsleider die GEEN bedrijfswagen heeft maar zelf een wagen gebruikt voor woon-werkverplaatsing, valt onder de aparte km-vergoeding 0,15 EUR/km (art. 66 §4 WIB 92). Geen VAA, geen 1205/1206, maar ook geen brede vennootschapskostenaftrek.
    - **Gelijkenissen**:
        - Beide regimes regelen mobiliteit van werknemer naar de werkplek
    - **Verschillen**:
        - Autokosten (bedrijfswagen): vennootschap draagt + aftrek-beperking + VAA; km-vergoeding: werknemer draagt + forfait 0,15 EUR/km
        - Bij bedrijfswagen vervalt de forfaitaire km-aftrek volgens art. 66 §4
### `beinvloed_door`
- [[vaste-activa]] — Een AANGEKOCHTE wagen is een materieel vast actief op 241 'Rollend materieel' en wordt afgeschreven volgens algemene activa-regels (lineair, doorgaans 4-5 jaar — degressief uitgesloten voor personenwagens art. 64 WIB 92). De afschrijvingskost vormt een deel van de basis voor de CO2-aftrek-beperking en wordt geboekt op 6302.
### `valt_onder`
- [[verworpen-uitgaven-venb]] — Het niet-aftrekbare deel van de autokost + 40 %/17 % van VAA komt in vak B (codes 1205 en 1206) van de verworpen-uitgaven-rubriek van de VenB-aangifte.
### `vereist`
- [[co2-uitstoot-bepaling]] — Voor zowel CO2-aftrek-formule, VAA-formule, BIV-berekening als valse-hybride-correctie is een correct CO2-cijfer per voertuig vereist (uit DIV-databank, homologatie of formule-bepaling bij ontbreken).
