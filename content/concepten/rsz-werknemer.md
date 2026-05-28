---
title: "RSZ-werknemer"
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
gegenereerd_uit: "data/concepten/records/rsz-werknemer.json"
---

# RSZ-werknemer

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: persoonlijke RSZ-bijdrage · sociale zekerheidsbijdragen werknemer · ingehouden RSZ — **Vertalingen**: fr: cotisations personnelles ONSS

## Definitie

🔗 De RSZ-werknemersbijdrage is de persoonlijke sociale-zekerheidsbijdrage die op het brutoloon van de werknemer wordt ingehouden door de werkgever en doorgestort aan de Rijksdienst voor Sociale Zekerheid (RSZ). Het standaardpercentage bedraagt 13,07 % en is sinds decennia stabiel (Belgisch hoofdtarief). De bijdrage is een bevrijdende inhouding-aan-bron — wat ingehouden is, hoeft de werknemer niet meer apart te betalen. Daarbovenop komt nog de bijzondere bijdrage voor de sociale zekerheid (BBSZ), een aanvullende heffing die gezinsinkomensafhankelijk is. Voor lage lonen wordt de RSZ-werknemersbijdrage verminderd via de werkbonus.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Het inhoudingsmechanisme maakt dat de werknemer de RSZ-bijdrage nooit zelf op zijn rekening krijgt — zij verlaat het brutoloon vóór bedrijfsvoorheffing wordt afgehouden. De berekeningsvolgorde op een loonfiche is: (1) brutoloon → (2) min RSZ-werknemer 13,07 % = belastbaar inkomen → (3) min bedrijfsvoorheffing → (4) netto. De ingehouden RSZ is fiscaal aftrekbaar als beroepskost (art. 52, 7° WIB92), wat de belastinglast op het brutoloon verlaagt — een dubbel voordeel dat de bruto-netto-spreiding niet zo groot maakt als naïef gerekend. De werkgever boekt de inhouding NIET als kost (kost zit al in 620 — bezoldigingen): de inhouding leidt tot een schuld op rekening 454 (RSZ) en een lagere netto-schuld op 455 (lonen).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🤖 De werknemersbijdrage maakt de werknemer mede-financier van de sociale zekerheid die hem beschermt: pensioen, ziekteverzekering, werkloosheid. Het bronafhouding-systeem garandeert volledige inning — niemand kan ontsnappen, anders dan bij een fiscale aanslag. De vaste 13,07 % is bewust simpel: één tarief voor alle inkomens, geen schijven. De gezinsmodulatie zit dan elders — in de bijzondere bijdrage (BBSZ) die naar inkomensschijven kijkt, en in de werkbonus voor de laagste lonen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2026-01-01**

13,07 % is een structureel stabiel percentage. De werkbonus en de BBSZ-tabel worden wel regelmatig geïndexeerd — exacte bedragen via Cijferzakboekje.

**✅ Voor**
- 🔗 Elke werknemer met een arbeidsovereenkomst onderworpen aan de Belgische sociale zekerheid (DIMONA-aangifte). Geldt voor arbeiders, bedienden, kaderleden, leerlingen — verschillen zitten in bijkomende sectorbijdragen en verminderingen, niet in het hoofdpercentage.

**🚫 Niet voor**
- 🔗 Bedrijfsleiders zonder dienstverband (zelfstandigen — eigen sociaal statuut zelfstandigen via sociaal verzekeringsfonds). Buitenlandse detachering naar België met A1-formulier (bijdragen in herkomstland). Studenten met studentenovereenkomst tot 600 uur per jaar (gunstige solidariteitsbijdrage van 5,42 % gezamenlijk in plaats van 13,07 %).

**👍 Voordeel**
- 🔗 De ingehouden RSZ-werknemer is aftrekbaar als beroepskost in de PB (art. 52, 7° WIB92) — verlaagt het belastbaar inkomen. Voor de werknemer betekent dit dat 13,07 % bruto al wordt opgevangen door een lagere PB-belastinggrondslag — netto blijft de pijn van de inhouding kleiner.

## Bouwstenen

### 📏 Standaardtarief 13,07 %  
_`drempel`_

🔗 Het basistarief van de RSZ-werknemersbijdrage bedraagt 13,07 % op het brutoloon. Het tarief is uniform — geen schijven, geen leeftijdsdifferentiatie. Sectorbijdragen (bv. solidariteitsbijdrage zware beroepen) kunnen erbij komen voor specifieke groepen, maar 13,07 % is voor het overgrote deel van de Belgische werknemers het werkbare percentage.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Bronafhouding-mechanisme  
_`mechanisme`_

🔗 De werkgever houdt de RSZ-bijdrage in op het brutoloon van de werknemer en stort die door aan de RSZ. De werknemer hoeft zelf niets te doen — geen aangifte, geen betaling. Per kwartaal voert de werkgever een DMFA-aangifte uit waarin per werknemer brutoloon, inhoudingen en verminderingen worden gerapporteerd.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Werkbonus — vermindering voor lage lonen  
_`uitzondering`_

🔗 Voor werknemers met een laag refertekwartaalloon wordt een vermindering op de RSZ-werknemersbijdrage toegepast: de werkbonus. Onder een onderste loongrens: maximale vermindering (forfait). Tussen onderste en bovenste grens: degressief afgebouwd. Boven de bovenste grens: geen vermindering. De werkbonus verhoogt het netto-loon zonder dat de werkgever extra kost draagt — een gericht middel om werkloosheidsval te vermijden. De fiscale werkbonus (PB-vermindering art. 289ter/1 WIB92) komt bovenop de RSZ-vermindering.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Bijzondere bijdrage sociale zekerheid (BBSZ)  
_`regel`_

🔗 Bovenop de 13,07 % betaalt de werknemer een bijzondere bijdrage voor de sociale zekerheid (BBSZ) — geheven via inhouding door de werkgever, maar berekend op gezinsinkomensbasis (referentie-inkomen vorig jaar). De heffing is sterk degressief: lage gezinsinkomens betalen vrijwel niets, hogere gezinsinkomens een vast bedrag per maand met een plafond. Het exacte rooster (drempels + bedragen) zit in het Cijferzakboekje.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Fiscale aftrekbaarheid (art. 52, 7° WIB92)  
_`regel`_

📖 De persoonlijke sociale-zekerheidsbijdragen (RSZ-werknemer + BBSZ) zijn aftrekbaar als beroepskost in de personenbelasting (art. 52, 7° WIB92). Concreet betekent dit dat het belastbaar beroepsinkomen wordt berekend als brutoloon − RSZ-werknemer − BBSZ. Daarna pas worden forfaitaire of werkelijke beroepskosten van toepassing en wordt de bedrijfsvoorheffing geheven.

<small>📚 WIB92 — art. 52, 7° — _wettekst_</small>

### ⚙️ Boekhoudkundige verwerking inhouding  
_`mechanisme`_

🔗 De RSZ-inhouding op het loon is GEEN bijkomende kost voor de werkgever — zij is een doorgeefluik. Boekhoudkundig: 620 (D, brutoloon) tegenover 454 (C, RSZ-schuld werknemer-deel) + 453 (C, BV-schuld) + 455 (C, netto-loon-schuld). De werkgeverskost zit op 621 (apart). De werknemer ziet enkel het netto-loon (455 → 55 bij betaling).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Inhouding RSZ-werknemer op brutoloon 3.000 EUR 🔗

_Jonas werkt bij Zelena Bio NV als bediende. Brutoloon: 3.000 EUR/maand. Geen werkbonus (loon > grens)._

**Berekening:**
- Stap 1 — Brutoloon = 3.000 EUR
- Stap 2 — RSZ-werknemer = 3.000 × 13,07 % = 392,10 EUR
- Stap 3 — Belastbaar inkomen (vóór BV) = 3.000 − 392,10 = 2.607,90 EUR
- Stap 4 — BBSZ: gezinsinkomensafhankelijk — uit Cijferzakboekje opzoeken (orde van grootte 10–60 EUR/maand)
- Stap 5 — Bedrijfsvoorheffing op 2.607,90 EUR via barema's (typisch ~400–600 EUR voor een alleenstaande)
- Stap 6 — Netto-loon = brutoloon − RSZ − BBSZ − BV ≈ 2.000 EUR (afhankelijk van gezinssituatie)

→ **Resultaat**: De RSZ-inhouding kost de werknemer 392 EUR; door de fiscale aftrekbaarheid zit dat reeds verrekend in een lager belastbaar bedrag, wat de netto-pijn verzacht.

**Boeking:**


<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ RSZ-werknemer dubbel opnemen — als kost én als inhouding

**Verkeerde assumptie**: Studenten boeken de werknemers-RSZ soms als extra kost op 621 (naast 620).

**Kernpunt**: De werknemers-RSZ is GÉÉN werkgeverskost — het is een inhouding op het brutoloon. De brutokost zit al volledig op 620. De inhouding leidt tot een schuld op 454 (deel werknemer) zonder een aanvullende kost. Enkel de patronale bijdrage (~25 %) zit op 621.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Werkbonus vergeten bij lage lonen

**Verkeerde assumptie**: Voor een werknemer met laag refertekwartaalloon wordt toch 13,07 % vol ingehouden.

**Kernpunt**: De werkbonus vermindert de RSZ-werknemerbijdrage substantieel voor lage lonen (kan tot ~200 EUR/maand schelen aan netto-loon). De RSZ-applicatie en payroll-software berekenen dit automatisch via de DMFA — maar bij manuele berekeningen of bij verificatie van de loonfiche moet dit expliciet meegenomen worden. Niet vergeten dat de fiscale werkbonus daarbovenop nog een PB-vermindering geeft.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ BBSZ op kwartaal- in plaats van gezinsbasis berekenen

**Verkeerde assumptie**: De BBSZ is een gewone werknemersbijdrage op het maandloon — net als 13,07 %.

**Kernpunt**: De BBSZ wordt wél ingehouden door de werkgever, maar berekend op gezinsinkomens-basis (referentie-inkomen vorig jaar) — niet op het maandloon zelf. De werkgever weet dit via een attest van de RSZ. Voor een fiscale optimalisatie-advies kan de adviseur het effect van gezinsinkomensveranderingen op de BBSZ inschatten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Loonfiche-verifier (werknemer-perspectief)

_De accountant die een loonfiche van een PB-cliënt nakijkt of de PB-aangifte voorbereidt._

#### 💰 Fiscaal adviseur

##### 👣 Controle inhoudingspercentage  
_`stap`_

🔗 Op de loonfiche: brutoloon × 13,07 % moet (bij benadering) overeenkomen met de afgehouden RSZ. Afwijking wijst op (1) werkbonus die actief is — netto-RSZ wordt lager dan 13,07 %; (2) sectorbijdrage extra (zwaar beroep, ploegen) — netto-RSZ wordt iets hoger; (3) fout. Bij twijfel: payroll-software-detail opvragen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 PB-aangifte — RSZ als aftrekbare kost  
_`stap`_

📖 In de PB-aangifte wordt op de fiche 281.10 het brutoloon én de ingehouden persoonlijke RSZ + BBSZ getoond. Het belastbaar bedrag dat in vak IV bezoldigingen komt = brutoloon − persoonlijke sociale bijdragen (art. 52, 7° WIB92). Tax-on-Web doet dit automatisch via de fiche-data; manuele aangiften vereisen aandacht voor het juiste vak.

<small>📚 WIB92 — art. 52, 7° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Loon-en-payroll K-techniek (cascade-context) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Werknemers-vergoedingen Σ (alternatieven) → [[werknemers-vergoedingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[loon-en-payroll]]
### `vergelijkbaar_met`
- [[rsz-werkgever]]
    - **Gelijkenissen**:
        - Beide zijn sociale-zekerheidsbijdragen op het brutoloon
        - Beide via dezelfde DMFA-aangifte gerapporteerd
        - Beide financieren de Belgische sociale zekerheid
    - **Verschillen**:
        - Werknemer-bijdrage (13,07 %) ingehouden op brutoloon — niet zichtbaar voor werknemer als 'kost'
        - Werkgever-bijdrage (~25 %) bovenop brutoloon — werkgeverskost
        - Werknemer-bijdrage stabiel uniform tarief; werkgever-bijdrage sectorvariatie + verminderingen
        - Werknemer-bijdrage is fiscaal aftrekbaar in PB (art. 52, 7°); werkgever-bijdrage is aftrekbaar in VenB/PB als bedrijfskost (klasse 621)
    - ⚠️ **Verwarringsrisico**: Op loonfiches en in cijfers verschijnt 'RSZ' vaak zonder verduidelijking welk deel bedoeld is. Op de fiche 281.10 staan beide afzonderlijk — let op de juiste regel.
### `triggert`
- [[werkbonus]] — Lage refertekwartaallonen activeren werkbonus die de werknemerinhouding vermindert.
