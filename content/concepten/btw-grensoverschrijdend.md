---
title: "Grensoverschrijdende btw"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - kader
ankers:
  - 2.4.VI
  - 2.4.taak.3
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-grensoverschrijdend.json"
---

# Grensoverschrijdende btw

_Kader_

📋 Regeling · 🏛️ Kader · Anchors: `2.4.VI` · `2.4.taak.3` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: cross-border BTW · intracommunautaire BTW-handelingen · IC-handelingen

## Definitie

📖 Grensoverschrijdende btw is het deel van het btw-stelsel dat regelt waar en door wie btw verschuldigd is wanneer goederen of diensten een landsgrens overschrijden. Voor verkeer tussen EU-lidstaten gelden de specifieke regels van intra-communautaire (IC) leveringen en verwervingen (WBTW art. 25bis, 25ter en 39bis); voor verkeer van of naar derde landen gelden de regels van invoer en uitvoer. De plaats van handeling — de lidstaat die mag heffen — wordt bepaald door art. 14-15 (goederen) en art. 21 / 21bis (diensten) van het WBTW, gestoeld op de overeenkomstige bepalingen van Richtlijn 2006/112/EG.

<small>📚 WBTW — art. 25bis — _wettekst_ · WBTW — art. 25ter — _wettekst_ · Richtlijn 2006/112/EG — art. 23 — _richtlijn_ · Richtlijn 2006/112/EG — art. 138 — _richtlijn_</small>

## Substantie

🔗 Het basisprincipe is bestemmingsland-heffing: btw is verschuldigd in de lidstaat waar het goed of de dienst eindigt, niet waar het vertrekt. Dat principe wordt geoperationaliseerd via drie mechanismen: (1) vrijstelling-met-recht-op-aftrek aan de vertrekzijde (IC-levering, uitvoer), (2) verwerving of invoer aan de aankomstzijde die btw doet ontstaan bij de afnemer, en (3) de verleggingsregeling die de schuldenaar verlegt van de leverancier naar de afnemer. Voor consumentenstromen (B2C) is de hoofdregel sinds 2021 ook bestemmingsland-heffing — daarom werd de One-Stop-Shop (OSS) ingevoerd om te vermijden dat een verkoper zich in elke afzetlidstaat moet registreren. Voor extra-EU goederenverkeer komt er douane bij: btw wordt geheven bij invoer en goederen verlaten de EU btw-vrij bij uitvoer.

<small>📚 WBTW — art. 15 — _wettekst_ · WBTW — art. 39bis — _wettekst_ · Richtlijn 2006/112/EG — art. 138 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio legis is dubbel: (1) fiscale neutraliteit tussen lidstaten — elk lid-staat heft btw op de eigen consumptie zonder dat de plaats van vestiging van de verkoper de heffing scheeftrekt; (2) vermijden van dubbele of niet-heffing op grensoverschrijdende stromen, doordat de vrijstelling aan de vertrekzijde gekoppeld wordt aan een verwerving aan de ontvangstzijde. Het systeem is een tijdelijk regime ingevoerd in 1993 bij de afschaffing van de binnengrenzen — het 'definitieve' bestemmingsland-regime is nog in ontwerp. Voor B2C werd het bestemmingsland-principe afgemaakt via de e-commerce-hervorming van 1 juli 2021 (Richtlijn EU 2017/2455), die de drempel voor verkopen-op-afstand op 10.000 EUR EU-wijd zette en de OSS-aangifte invoerde.

<small>📚 Richtlijn 2006/112/EG — art. 138 — _richtlijn_ · Richtlijn EU 2017/2455 — e-commerce-hervorming 1 juli 2021 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **1993-01-01** · basis: WBTW + Richtlijn 2006/112/EG (algemeen IC-stelsel sinds 1993) + Richtlijn EU 2017/2455 (e-commerce-pakket vanaf 1 juli 2021)

Het IC-stelsel is een tijdelijk regime ingevoerd bij de afschaffing van de fysieke EU-binnengrenzen op 1 januari 1993. Het 'definitieve regime' (heffing bij de verkoper voor rekening van het bestemmingsland) is door de Europese Commissie meermaals voorgesteld maar nog niet aangenomen. Het tijdelijke regime functioneert dus als blijvend regime.

**✅ Voor**
- 🔗 Elke btw-belastingplichtige die goederen levert aan, verwerft van, of diensten verricht voor of ontvangt van een tegenpartij buiten België — zowel binnen de EU (IC-handeling) als met derde landen (invoer/uitvoer).

**🟢 Indicaties**
- 🔗 Op de inkoopfactuur staat een buitenlands btw-nummer of helemaal geen btw aangerekend met de vermelding 'btw verlegd' / 'reverse charge' / 'art. 138 Dir. 2006/112'. Op de verkoopfactuur naar een EU-klant staat 'BTW vrijgesteld — IC-levering art. 39bis WBTW'. Bij vervoer-documenten (CMR, vrachtbrief) wordt het goed fysiek over een EU-grens vervoerd.

## Bouwstenen

### ✴️ Bestemmingsland-principe  
_`principe`_

🔗 Btw wordt geheven in de lidstaat van consumptie — niet in de lidstaat van oorsprong. Voor grensoverschrijdende stromen vertaalt dit zich in: vrijstelling (met behoud van recht op aftrek) aan vertrekzijde + heffing aan aankomstzijde. Het beschermt de neutraliteit tussen lidstaten: een Belgische klant betaalt 21 % Belgische btw, of het goed nu uit Aalst komt of uit Aachen.

<small>📚 Richtlijn 2006/112/EG — art. 138 — _richtlijn_ · WBTW — art. 25ter — _wettekst_</small>

### 👣 Eerste vraag: goederen of diensten?  
_`stap`_

📖 De keuze-cascade begint bij de aard van de prestatie. Goederen volgen art. 14 (algemene plaats = waar de verzending begint) gecorrigeerd door art. 15 (verkopen-op-afstand) en art. 25bis/25ter (IC-verwerving). Diensten volgen art. 21 (B2B = woonplaats afnemer) en art. 21bis (B2C = woonplaats dienstverrichter, behoudens lange lijst uitzonderingen). Een verkeerde categorisering (bv. software-as-a-service als 'goed' ipv 'dienst') leidt tot de verkeerde plaats-van-handeling en dus tot foute heffing.

<small>📚 WBTW — art. 14 — _wettekst_ · WBTW — art. 21 — _wettekst_ · WBTW — art. 21bis — _wettekst_</small>

### 👣 Tweede vraag: B2B of B2C?  
_`stap`_

🔗 De status van de afnemer bepaalt de heffingsregel. B2B = afnemer is btw-belastingplichtige (controleerbaar via VIES-database voor zijn btw-nummer). B2C = afnemer is particulier of niet-belastingplichtige. De accountant noteert het btw-nummer van de afnemer in het dossier vóór elke grensoverschrijdende prestatie — geen btw-nummer = vermoeden B2C tenzij tegenbewijs.

<small>📚 WBTW — art. 21 — _wettekst_ · WBTW — art. 21bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Derde vraag: intra-EU of extra-EU?  
_`stap`_

📖 Intra-EU goederen: IC-levering (vrijgesteld art. 39bis WBTW) bij verkoper + IC-verwerving (belastbaar art. 25ter WBTW) bij koper. Extra-EU goederen: uitvoer (vrijgesteld art. 39 §1 WBTW) of invoer (belastbaar art. 23 WBTW + douaneformaliteiten, vaak met verlegging via vergunning ET 14.000). De grens EU/niet-EU bepaalt of er een douaneformaliteit nodig is — voor diensten is er geen vergelijkbare douane-hindernis.

<small>📚 WBTW — art. 39bis — _wettekst_ · WBTW — art. 25ter — _wettekst_ · Richtlijn 2006/112/EG — art. 23 — _richtlijn_</small>

### 📏 10.000 EUR-drempel voor B2C-EU-afstandsverkopen  
_`drempel`_

📖 Voor intra-communautaire afstandsverkopen aan consumenten (B2C-EU) en voor elektronische / telecommunicatiediensten aan consumenten in andere lidstaten geldt sinds 1 juli 2021 één EU-wijde drempel van 10.000 EUR (excl. btw) per kalenderjaar. Onder de drempel: btw van de lidstaat van vertrek (België) — boven de drempel of bij optie: btw van de lidstaat van bestemming, ofwel via lokale btw-registratie ofwel via OSS-aangifte in België. De drempel is een totaal voor alle lidstaten samen, niet per lidstaat zoals vóór 2021.

<small>📚 WBTW — art. 15 §1 tweede lid 3° — _wettekst_</small>

### 📏 11.200 EUR-drempel IC-verwerving voor niet-aftrekgerechtigden  
_`drempel`_

📖 Belastingplichtigen zonder recht op aftrek (vrijgestelde belastingplichtigen art. 44, kleine ondernemingen art. 56bis) en niet-belastingplichtige rechtspersonen die IC-verwervingen verrichten zijn pas btw-plichtig op die verwervingen vanaf 11.200 EUR (geïndexeerd opzoeken in het Cijferzakboekje — niet-geïndexeerd basisbedrag in WBTW). Onder die drempel: btw van vertrekland blijft van toepassing tenzij ze opteren voor IC-belasting (art. 25ter §1 tweede lid 2°). Een gemeente, ziekenhuis of huisarts die voor 8.000 EUR meubels uit Duitsland bestelt betaalt dus Duitse btw, geen Belgische verwervings-btw.

<small>📚 WBTW — art. 25ter §1 tweede lid 2° — _wettekst_ · WBTW — art. 50 §1 eerste lid 2° — _wettekst_</small>

### 📜 Vrijstellingsvoorwaarden IC-levering (art. 39bis WBTW)  
_`regel`_

📖 Cumulatief: (1) levering aan een belastingplichtige of een niet-belastingplichtige rechtspersoon die voor btw-doeleinden is geïdentificeerd in een andere lidstaat; (2) goederen worden door of voor rekening van verkoper of koper fysiek vervoerd naar die andere lidstaat; (3) de koper deelt zijn buitenlands btw-nummer mee en de verkoper vermeldt de levering in zijn IC-opgave (art. 53sexies). Sinds 2020 (quick fixes) zijn voorwaarden (1) en (3) materieel-substantieel — geen geldig btw-nummer of geen opname in IC-opgave = vrijstelling vervalt. Documenteer met buitenlands btw-nummer + VIES-print + CMR / vrachtbrief / leveringsbon.

<small>📚 WBTW — art. 39bis — _wettekst_ · Richtlijn 2006/112/EG — art. 138 — _richtlijn_</small>

### 📜 Plaats van diensten: B2B vs B2C-hoofdregel  
_`regel`_

📖 B2B (art. 21 §2 WBTW / art. 44 Richtlijn): plaats van de dienst = waar de afnemer zijn zetel van economische activiteit (of vaste inrichting) heeft. Gevolg: bij grensoverschrijdende B2B-dienst tussen EU-belastingplichtigen is de Belgische dienstverrichter geen btw verschuldigd; de buitenlandse afnemer past de verleggingsregeling toe. B2C (art. 21bis §1 WBTW / art. 45 Richtlijn): plaats = waar de dienstverrichter is gevestigd. Op deze twee hoofdregels staan tientallen uitzonderingen (onroerend goed = situs · vervoer · restaurant · evenementen · elektronische diensten = afnemer · ...) — voor het volledige overzicht: zie record plaats-van-handeling-btw.

<small>📚 WBTW — art. 21 — _wettekst_ · WBTW — art. 21bis — _wettekst_ · Richtlijn 2006/112/EG — art. 44 — _richtlijn_</small>

### ⚙️ IC-opgave (listing intracommunautaire handelingen)  
_`mechanisme`_

📖 Periodieke (maandelijkse of kwartaal-) aangifte naast de gewone btw-aangifte waarin de Belgische leverancier per buitenlandse afnemer (btw-nummer) het totaalbedrag van zijn IC-leveringen en B2B-diensten naar die afnemer aangeeft (art. 53sexies WBTW). De lidstaten wisselen die gegevens uit via het VIES-systeem: het bedrag dat verkoper in lidstaat A opgeeft, moet matchen met de aangegeven verwerving van koper in lidstaat B. Mismatch = automatische controle-trigger.

<small>📚 Richtlijn 2006/112/EG — art. 265 — _richtlijn_ · WBTW — art. 53sexies — _wettekst_</small>

### ⚙️ Σ-vergelijking: welke regeling kies ik?  
_`mechanisme`_

🔗 Vijf hoofdregelingen worden vaak met elkaar verward maar lossen elk een ander probleem op: (1) IC-levering/verwerving (art. 25ter, 39bis): standaard B2B-EU-goederenstroom. (2) Verleggingsregeling (art. 51 §2): schuldenaar wordt de afnemer ipv leverancier — werkt voor B2B-diensten EU en voor specifieke binnenlandse stromen (bouw, onderaanneming). (3) OSS / IOSS (art. 58ter-quater): B2C-EU-afstandsverkopen en e-commerce — vermijdt registratie in elke lidstaat. (4) Driehoeksverkeer-vereenvoudiging (art. 25quinquies): A-B-C-stroom over drie lidstaten waarbij B niet hoeft te registreren in lidstaat A of C. (5) Fiscaal vertegenwoordiger (art. 55, KB 31): voor niet-EU-belastingplichtigen die in België belastbare handelingen verrichten — verplichte vertegenwoordiging.

<small>📚 WBTW — art. 25ter — _wettekst_ · WBTW — art. 25quinquies — _wettekst_ · WBTW — art. 51 §2 — _wettekst_ · WBTW — art. 55 — _wettekst_ · WBTW — art. 58ter — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 IC-levering — Belgische groothandelaar aan Duitse winkel 🔗

_Zelena Bio NV (België, btw-nr. BE 0123.456.789) verkoopt biologische voedingsmiddelen aan SonnenMarkt GmbH (Duitsland, btw-nr. DE 123456789) voor 10.000 EUR. Goederen worden per vrachtwagen vanuit Aalst naar Düsseldorf vervoerd. SonnenMarkt deelt haar Duits btw-nummer mee, Zelena controleert de geldigheid via VIES._

**Berekening:**
- Stap 1 — Zelena factureert 10.000 EUR zonder btw, met vermelding 'Btw vrijgesteld — IC-levering art. 39bis WBTW / art. 138 Richtlijn 2006/112/EG'.
- Stap 2 — Zelena geeft de levering aan in rooster 46 van haar Belgische btw-aangifte én op de IC-opgave (listing) van die periode — afnemer DE 123456789 voor 10.000 EUR.
- Stap 3 — SonnenMarkt doet in Duitsland een IC-verwerving: zelf 19 % Duitse btw aanrekenen (= 1.900 EUR) én diezelfde 1.900 EUR onmiddellijk aftrekken indien volledig recht op aftrek — netto-effect = nul, maar wel administratie + IC-controle.
- Stap 4 — Documentatie in dossier Zelena: VIES-controle Duits btw-nummer, factuur, CMR-vrachtbrief, leveringsbevestiging klant. Bij ontbreken van bewijs van fysiek vervoer = vrijstelling vervalt en Belgische 6 % / 21 % btw verschuldigd.

→ **Resultaat**: Netto-btw bij Zelena = 0 EUR (vrijgestelde levering met recht op aftrek). Bij SonnenMarkt = 0 EUR netto (verwerving + aftrek). Bestemmingsland-principe gerealiseerd: Duitsland zou heffen als de eindafnemer een particulier was.

<small>📚 WBTW — art. 39bis — _wettekst_ · WBTW — art. 25ter — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 B2B-dienst — Franse consultant aan Belgische cliënt (verlegging) 🔗

_Aurelia Holding NV (België) krijgt een strategie-rapport van een Franse consultant (Cabinet Étoile SARL, FR-btw-nummer) voor 5.000 EUR._

**Berekening:**
- Stap 1 — plaats van handeling = afnemer (B2B-hoofdregel art. 21): België.
- Stap 2 — Franse consultant factureert 5.000 EUR zonder Franse btw met vermelding 'Autoliquidation — TVA due par le preneur art. 196 Dir. 2006/112'.
- Stap 3 — Aurelia past de verleggingsregeling toe (art. 51 §2 WBTW): boekt 21 % Belgische btw = 1.050 EUR als verschuldigd in rooster 56 en 1.050 EUR als aftrekbaar in rooster 59 — netto-effect = 0 EUR mits volledig recht op aftrek.
- Stap 4 — IC-opgave: NIET door Aurelia (zij is afnemer); WEL door Cabinet Étoile in zijn Franse IC-opgave-diensten (art. 53sexies-equivalent in Frankrijk).

→ **Resultaat**: Cash-neutraal voor Aurelia bij volledig recht op aftrek. Bij gemengde btw-belastingplichtige (bv. arts met bijberoep) blijft er per definitie een netto-kost over: 1.050 EUR Belgische btw, deels niet aftrekbaar volgens algemeen verhoudingsgetal.

<small>📚 WBTW — art. 21 — _wettekst_ · WBTW — art. 51 §2 — _wettekst_ · Richtlijn 2006/112/EG — art. 44 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Keuze-cascade: welk regime past? 🔗

_Toepassing van de Σ-keuze-flow via beslisboom op de meest voorkomende cases._

**Weergave** `beslisboom`:

```json
{
  "titel": "Σ-keuze-cascade grensoverschrijdende BTW",
  "code": "flowchart TD\n  A[Grensoverschrijdende handeling] --> B{Goederen of diensten?}\n  B -->|Goederen| C{Intra-EU of extra-EU?}\n  B -->|Diensten| D{B2B of B2C?}\n  C -->|Intra-EU| E{B2B of B2C?}\n  C -->|Extra-EU| F[Uitvoer art. 39 §1 / Invoer art. 23 — douaneformaliteit]\n  E -->|B2B| G[IC-levering art. 39bis + IC-verwerving art. 25ter]\n  E -->|B2C| H{Drempel 10.000 EUR overschreden?}\n  H -->|Nee| I[Btw vertrekland — standaard]\n  H -->|Ja of optie| J[OSS Union scheme of lokale registratie]\n  D -->|B2B| K[Plaats = afnemer art. 21 → verleggingsregeling]\n  D -->|B2C| L[Plaats = dienstverrichter art. 21bis — uitzonderingen vaak]\n  G --> M{Driehoek A-B-C?}\n  M -->|Ja| N[Driehoeksverkeer-vereenvoudiging art. 25quinquies]\n  M -->|Nee| O[Gewone IC-stroom]\n  F --> P{Niet-EU verkoper met BE-activiteit?}\n  P -->|Ja| Q[Fiscaal vertegenwoordiger verplicht]"
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Verlegging is geen vrijstelling

**Verkeerde assumptie**: Studenten denken dat 'btw verlegd' = 'geen btw verschuldigd, geen aangifte nodig'.

**Kernpunt**: Verleggingsregeling betekent dat de schuldenaar verschuift van leverancier naar afnemer — de btw blijft volledig verschuldigd en moet door de afnemer worden aangegeven in rooster 55-56 (en bij recht op aftrek in rooster 59 om netto = 0 te halen). Vergeten aan te geven = btw-tekort + boete, zelfs als er materieel geen cash-impact zou zijn.

<small>📚 WBTW — art. 51 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Drempel 10.000 EUR is EU-wijd, niet per lidstaat

**Verkeerde assumptie**: Studenten leren de oude drempels (35.000 / 100.000 EUR per lidstaat) van vóór 1 juli 2021 of denken dat de 10.000 EUR-drempel per bestemmingsland geldt.

**Kernpunt**: Sinds 1 juli 2021 (EU 2017/2455): één drempel van 10.000 EUR voor alle B2C-EU-afstandsverkopen en TBE-diensten samen — bv. 4.000 EUR naar Nederland + 5.000 EUR naar Frankrijk + 2.000 EUR naar Duitsland = boven drempel, met btw van élk bestemmingsland verschuldigd vanaf de overschrijdings-levering.

<small>📚 WBTW — art. 15 §1 tweede lid 3° — _wettekst_ · Richtlijn EU 2017/2455 — art. 1 — drempel 10.000 EUR — _richtlijn_</small>

### ⚠️ Btw-nummer afnemer 'wel of niet meegedeeld' is conditioneel voor de vrijstelling

**Verkeerde assumptie**: Het buitenlands btw-nummer 'controleren' is een formaliteit die later kan ingehaald worden — als de levering reëel is, blijft de vrijstelling overeind.

**Kernpunt**: Sinds de quick fixes van 1 januari 2020 (Richtlijn EU 2018/1910 → WBTW art. 39bis) is het meedelen + VIES-correctheid van het buitenlands btw-nummer + de opname in de IC-opgave een materieel-substantiële voorwaarde voor de vrijstelling. Geen geldig nummer = vrijstelling vervalt = Belgische btw (6 % of 21 %) verschuldigd door verkoper, plus boete.

<small>📚 WBTW — art. 39bis — _wettekst_ · Richtlijn EU 2018/1910 — quick fixes — _richtlijn_</small>

### ⚠️ Diensten verwarren met goederen voor de plaats-van-handeling

**Verkeerde assumptie**: Software-licenties, e-books, streaming worden behandeld als goederen omdat ze 'iets verkopen'.

**Kernpunt**: Elektronische diensten zijn diensten (art. 18 §2 WBTW) en volgen art. 21/21bis. B2C-elektronische diensten naar EU-consumenten = plaats = afnemer (uitzondering op de B2C-hoofdregel), met OSS-aangifte mogelijk. Goederen vereisen fysiek vervoer — kan een digitaal product per definitie niet hebben.

<small>📚 WBTW — art. 18 §2 — _wettekst_ · WBTW — art. 21bis §2 9° — _wettekst_</small>

## Speelruimtes

### 🎚️ Optie om B2C-afstandsverkopen onder drempel toch in bestemmingsland te belasten

## Syntheses

### 🧩 Synthese  
_`beslisboom`_

Kompas voor de stagiair: doorloop deze vier vragen bij elke grensoverschrijdende factuur.

## Accountant-perspectieven

### Belgische onderneming met grensoverschrijdende verkoop

_De accountant die het btw-dossier voert voor een KMO die levert aan of dienstverleent voor buitenlandse afnemers._

#### 📒 Boekhouder

##### 👣 Boekingsschema IC-levering  
_`stap`_

🔗 Voor een IC-levering: debet 400 Handelsvorderingen / credit 700 Verkopen (excl. btw) — geen btw-rekening, want vrijgesteld. Vermelding op factuur: 'BTW vrijgesteld — IC-levering art. 39bis WBTW'. Aangifte: rooster 46 (IC-leveringen) + IC-opgave (listing) per afnemer-btw-nummer.

<small>📚 WBTW — art. 39bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Boekingsschema IC-verwerving (afnemerszijde, België)  
_`stap`_

🔗 Voor een IC-verwerving van 10.000 EUR uit Duitsland: debet 604 Aankopen / debet 411 Aftrekbare btw (rooster 59) / credit 440 Handelsschulden + credit 451 Verschuldigde btw (rooster 55-56). Bij volledig recht op aftrek = cash-neutraal — alleen de twee btw-roosters compenseren elkaar.

<small>📚 WBTW — art. 25ter — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 VIES-controle als verplichte due-diligence  
_`stap`_

🔗 Bij elke nieuwe EU-afnemer: btw-nummer controleren via VIES (https://ec.europa.eu/taxation_customs/vies), screenshot of bevestigings-ID bewaren in het klantendossier. Hercontrole minstens jaarlijks voor recurring klanten — een btw-nummer kan worden ingetrokken zonder dat de afnemer dat meldt. Bij intrekking: vrijstelling vervalt = Belgische btw moet aangerekend worden vanaf de eerstvolgende factuur.

<small>📚 WBTW — art. 39bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 IC-opgave (listing) — deadline en aansluiting  
_`regel`_

🔗 De IC-opgave (listing) wordt ingediend in dezelfde periodiciteit als de btw-aangifte (maand of kwartaal), uiterlijk de 20e van de maand volgend op de aangifteperiode. Per buitenlandse afnemer wordt het totaalbedrag van IC-leveringen (code L) en B2B-diensten (code S) opgegeven. Controle in dossier: som van de listing = som van rooster 46 (leveringen) + rooster 44 (diensten) van de overeenstemmende btw-aangifte(s) van dezelfde periode.

<small>📚 WBTW — art. 53sexies — _wettekst_ · Richtlijn 2006/112/EG — art. 265 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Strategisch advies: welk regime past bij welke ambitie?  
_`vuistregel`_

🔗 Bij een KMO met EU-expansie-ambitie: vroeg OSS aanvragen vermijdt overgang midden-jaar wanneer drempel 10.000 EUR wordt overschreden. Bij een tussenhandelaar in een goederenketen (Belg koopt bij A, verkoopt aan C, beide in andere lidstaat dan B): driehoeksverkeer-vereenvoudiging onderzoeken — vermijdt verplichte btw-registratie in lidstaat A of C. Bij niet-EU-onderneming die opslag in België wil: fiscaal vertegenwoordiger is wettelijk vereist (art. 55 WBTW).

<small>📚 WBTW — art. 25quinquies — _wettekst_ · WBTW — art. 55 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → OSS / IOSS regeling → [[oss-regeling]] _(moet-verwijzen)_
- → Driehoeksverkeer-vereenvoudiging → [[driehoeksverkeer-vereenvoudiging]] _(moet-verwijzen)_
- → Fiscaal vertegenwoordiger BTW → [[fiscaal-vertegenwoordiger-btw]] _(moet-verwijzen)_
- → Verleggingsregeling (reverse charge) → [[verleggingsregeling]] _(moet-verwijzen)_
- → Plaats van handeling regels (volledige tabel B2B/B2C + uitzonderingen) → [[plaats-van-handeling-btw]] _(moet-verwijzen)_
- → Douaneprocedures BTW-invoer → [[douaneprocedures-btw-invoer]] _(moet-verwijzen)_
- ↪ Internationaal-fiscaal (DBV-context) → [[internationaal-fiscaal]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `bevat`
- [[oss-regeling]]
- [[driehoeksverkeer-vereenvoudiging]]
- [[verleggingsregeling]]
- [[fiscaal-vertegenwoordiger-btw]]
### `vereist`
- [[plaats-van-handeling-btw]] — De volledige tabel van plaats-van-handeling-regels (B2B/B2C + uitzonderingen onroerend goed/vervoer/restaurant/evenement/elektronische diensten) is een aparte voorvereiste.
### `beinvloed_door`
- [[btw-aangifte]] — Aangifte-roosters 44 (IC-diensten), 46 (IC-leveringen), 55-56 (IC-verwervingen + verlegging), 59 (aftrek verlegging) zijn de operationele neerslag van dit kader.
- [[factuur-btw]] — Factuur-vermeldingen 'BTW vrijgesteld art. 39bis' / 'Reverse charge art. 196 Dir.' zijn bewijslast voor de vrijstellingsregelingen.
