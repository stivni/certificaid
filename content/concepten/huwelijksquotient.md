---
title: "Huwelijksquotient"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.III
  - 2.2.IV
  - 2.2.XVI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/huwelijksquotient.json"
---

# Huwelijksquotient

_Regime_

📋 Regeling · Anchors: `2.2.III` · `2.2.IV` · `2.2.XVI` · Wave: `skeleton-pb-venb-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: huwelijksquotiënt · quotient conjugal — **Vertalingen**: fr: quotient conjugal

## Definitie

📖 Het huwelijksquotient is een fiscale techniek van inkomenstoerekening tussen echtgenoten of wettelijk samenwonenden die een gemeenschappelijke aanslag krijgen. Wanneer één echtgenoot geen of slechts beperkte beroepsinkomsten heeft, wordt automatisch een deel van de beroepsinkomsten van de andere echtgenoot aan hem/haar toegerekend voor de belastingberekening. Dat toegerekende deel bedraagt 30 % van die beroepsinkomsten, maar mag een wettelijk geïndexeerd plafond niet overschrijden (niet-geïndexeerd: 6.700 EUR per echtgenoot in WIB92).

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88 — _wettekst_</small>

## Substantie

🔗 Economisch effect: door een deel van de inkomsten van de hoogstverdiener te 'verschuiven' naar de minst-verdienende echtgenoot, worden de lagere belastingschijven van die laatste benut. De progressie van de personenbelasting maakt dat samen genomen minder belasting wordt betaald dan zonder toerekening. Het regime corrigeert dus voor de fiscale ongelijkheid tussen één-verdieners-gezinnen en twee-verdieners-gezinnen. Het is een automatische berekening van de fiscus — geen optie of keuze — die enkel wordt toegepast als ze gunstig is (of niet leidt tot een verhoging van bepaalde afzonderlijk belaste inkomsten).

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio legis is dubbel: (1) fiscale neutralisatie tussen één- en tweeverdieners-gezinnen — een gezin waar één partner thuis blijft of slechts beperkt verdient, zou anders onevenredig zwaar belast worden ten opzichte van een gezin met twee evenredig verdienende partners (gelijk gezinsinkomen, hogere aanslag wegens steilere progressie op één hoofd); (2) erkenning van de feitelijke gezinssolidariteit zonder volledige cumulatie van inkomens — elke echtgenoot blijft afzonderlijk belastbaar (art. 126 §1), maar de berekening houdt rekening met de gezinscontext.

<small>📚 WIB92 — art. 126 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 87-89 (toerekening) + art. 126 (gemeenschappelijke aanslag)

Stabiel regime sinds invoering WIB92. Wettelijk samenwonenden worden sinds AJ 2005 gelijkgesteld met echtgenoten (art. 2, 2° WIB92).

**✅ Voor**
- 📖 Gehuwden of wettelijk samenwonenden met een gemeenschappelijke aanslag waarbij één echtgenoot geen of slechts beperkte beroepsinkomsten heeft (minder dan 30 % van het totaal).

**🚫 Niet voor**
- 📖 Jaar van huwelijk of verklaring van wettelijke samenwoning · jaar na feitelijke scheiding · jaar van ontbinding huwelijk/samenwoning. In die jaren wordt geen gemeenschappelijke aanslag gevestigd en geldt het huwelijksquotient dus niet.
- 📖 Wanneer één echtgenoot beroepsinkomsten heeft van meer dan (niet-geïndexeerd) 6.700 EUR die bij internationaal verdrag zijn vrijgesteld en niet meetellen voor de belasting op zijn andere inkomsten — geen gemeenschappelijke aanslag, dus geen huwelijksquotient.

**📋 Voorwaarden**
- 📖 Cumulatief: (1) er wordt een gemeenschappelijke aanslag gevestigd (art. 126 WIB92); (2) de minst-verdienende echtgenoot heeft eigen beroepsinkomsten van minder dan 30 % van het totaal van de beroepsinkomsten van beide echtgenoten; (3) de toerekening leidt niet tot een verhoging van de belasting op bepaalde afzonderlijk belaste inkomsten (gunstigheidstoets art. 87/88 in fine).

**⛔ Uitsluitingen**
- 📖 Beroepsinkomsten die afzonderlijk worden belast (bv. achterstallen, opzeggingsvergoedingen) worden buiten beschouwing gelaten voor de toekenning en toerekening — het quotient grijpt enkel op gezamenlijk belaste beroepsinkomsten.

**👍 Voordeel**
- 🔗 Belastingbesparing door benutting van de lagere belastingschijven en belastingvrije som van de minst-verdienende echtgenoot, zonder dat die laatste effectief inkomsten ontvangt — louter een fiscale toerekening voor de berekening van de aanslag.

**⚠️ Risico**
- 🔗 Wanneer beide echtgenoten gelijkaardige inkomens hebben (elk meer dan 30 % van het totaal) is er geen huwelijksquotient — een misverstand bij stagiairs die denken dat élk gezin er recht op heeft. Het quotient is een 'asymmetrie-correctie', geen algemeen gezinsvoordeel.

## Bouwstenen

### 📏 30 %-drempel  
_`drempel`_

📖 Het huwelijksquotient wordt slechts toegepast wanneer de eigen beroepsinkomsten van de minst-verdienende echtgenoot minder dan 30 % bedragen van het totaal van de beroepsinkomsten van beide echtgenoten. De toerekening vult dan aan tot net 30 % (begrensd door het plafond).

<small>📚 WIB92 — art. 88 — _wettekst_</small>

### 📏 Plafondbedrag (geïndexeerd)  
_`drempel`_

📖 Het toegerekende bedrag mag het geïndexeerde plafond niet overschrijden. Niet-geïndexeerd basisbedrag in WIB92 = 6.700 EUR (art. 87 en 88). Het effectief toepasselijk plafond voor het lopende aanslagjaar wordt jaarlijks geïndexeerd — de exacte indexering opzoeken in het Cijferzakboekje (bij het examen beschikbaar).

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88 — _wettekst_</small>

### 🧮 Formule berekening huwelijksquotient  
_`formule`_

🔗 Toegerekend deel = min( 30 % × totaal beroepsinkomsten beide echtgenoten − eigen beroepsinkomsten minst-verdienende echtgenoot ; geïndexeerd plafond ). Indien minst-verdienende echtgenoot géén eigen beroepsinkomsten heeft (art. 87): toegerekend deel = min( 30 % × beroepsinkomsten van de andere echtgenoot ; geïndexeerd plafond ).

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Gunstigheidstoets  
_`regel`_

📖 Toerekening blijft achterwege wanneer ze tot een hogere belasting zou leiden op bepaalde afzonderlijk belastbare inkomsten (interesten/dividenden uit art. 17 §1 1°-3° en 6°, diverse inkomsten uit art. 90 1°, 6° en 9°, en meerwaarden op roerende waarden). De fiscus past het quotient dus enkel toe als het netto-gunstig is voor de belastingplichtige.

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88, tweede lid — _wettekst_</small>

### 📜 Evenredige samenstelling per categorie  
_`regel`_

📖 Wanneer de beroepsinkomsten van de hoogstverdiener uit meerdere categorieën komen (bv. bezoldigingen + winst), wordt het toegerekende deel evenredig samengesteld uit de verschillende categorieën. De aard van het toegerekende inkomen weerspiegelt dus de mix van de bronnen.

<small>📚 WIB92 — art. 89, tweede lid — _wettekst_</small>

### ⚙️ Afbakening tegenover meewerkinkomen (art. 86)  
_`mechanisme`_

📖 Het huwelijksquotient (art. 87-88) verschilt van het meewerkinkomen (art. 86). Meewerkinkomen veronderstelt dat de andere echtgenoot effectief meewerkt in de beroepsactiviteit van zijn partner (zelfstandige); het maximum is dan 30 % van die activiteitsinkomsten, en de meewerkende echtgenoot mag uit eigen activiteit niet meer dan (niet-geïndexeerd) 8.700 EUR verdienen. Het huwelijksquotient daarentegen is automatisch, vereist géén werkelijke medewerking en geldt voor alle soorten beroepsinkomsten — vooral bezoldigingen. Beide regimes kunnen niet voor dezelfde euro samengaan: art. 86 vraagt een toekenning van inkomen (echte allocatie), art. 87-88 betreft een toerekening voor de aanslagberekening.

<small>📚 WIB92 — art. 86 — _wettekst_ · WIB92 — art. 87 — _wettekst_</small>

## Voorbeelden

### 💡 Eénverdiener — bediende met huisvrouw/-man (art. 87) 🔗

_Echtgenoot A heeft 40.000 EUR netto-beroepsinkomsten (bezoldigingen). Echtgenoot B heeft géén eigen beroepsinkomsten. Gemeenschappelijke aanslag is van toepassing._

**Berekening:**
- Stap 1 — bereken 30 % van A's beroepsinkomsten: 30 % × 40.000 = 12.000 EUR.
- Stap 2 — vergelijk met geïndexeerd plafond (AJ 2026: ca. 13.050 EUR — exact bedrag in Cijferzakboekje opzoeken).
- Stap 3 — toegerekend deel = min(12.000 ; plafond) = 12.000 EUR (plafond niet bindend).
- Stap 4 — voor de aanslagberekening wordt 12.000 EUR fictief toegerekend aan B; A behoudt 28.000 EUR belastbaar.
- Stap 5 — belasting wordt afzonderlijk berekend op 28.000 EUR (A) + 12.000 EUR (B), elk met eigen belastingvrije som en lagere schijven; daarna samengevoegd in de gemeenschappelijke aanslag.

→ **Resultaat**: Effectief lagere totaalbelasting dan zonder quotient (waar 40.000 EUR volledig in de hogere schijven van A zou belast worden). Het cijferzakboekje is nodig voor het exacte plafond én voor de schijven om het netto-voordeel te becijferen.

<small>📚 WIB92 — art. 87 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Asymmetrische tweeverdiener (art. 88) 🔗

_Echtgenoot A: 50.000 EUR beroepsinkomsten. Echtgenoot B: 6.000 EUR beroepsinkomsten. Totaal = 56.000 EUR. B's aandeel = 6.000 / 56.000 ≈ 10,7 % — minder dan 30 %, dus art. 88 grijpt in._

**Berekening:**
- Stap 1 — totaal beroepsinkomsten = 50.000 + 6.000 = 56.000 EUR.
- Stap 2 — 30 % × 56.000 = 16.800 EUR (= doel-niveau voor B na toerekening).
- Stap 3 — aanvullingsbedrag = 16.800 − 6.000 = 10.800 EUR.
- Stap 4 — toets aan plafond: min(10.800 ; geïndexeerd plafond ≈ 13.050 EUR voor AJ 2026) = 10.800 EUR.
- Stap 5 — A behoudt 50.000 − 10.800 = 39.200 EUR belastbaar; B wordt belast op 6.000 + 10.800 = 16.800 EUR.

→ **Resultaat**: Door 10.800 EUR fictief naar B te schuiven, valt dit deel in B's eigen lagere schijven en wordt totaal minder belasting betaald. Het exacte plafond moet uit het Cijferzakboekje gehaald worden.

<small>📚 WIB92 — art. 88 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Huwelijksquotient verwarren met meewerkinkomen

**Verkeerde assumptie**: Studenten denken vaak dat art. 86 (meewerkinkomen) en art. 87-88 (huwelijksquotient) hetzelfde regime zijn omdat beide met '30 %' werken.

**Kernpunt**: Meewerkinkomen vereist effectieve medewerking in de beroepswerkzaamheid van de zelfstandige partner en is een toekenning van inkomen (allocatie); het huwelijksquotient is automatisch, vereist géén medewerking en is een louter fiscale toerekening. Andere drempel (8.700 vs 6.700 EUR niet-geïndexeerd) en andere voorwaarden.

<small>📚 WIB92 — art. 86 — _wettekst_ · WIB92 — art. 87 — _wettekst_</small>

### ⚠️ Niet-geïndexeerd vs geïndexeerd bedrag uit het hoofd 'kennen'

**Verkeerde assumptie**: Studenten leren 6.700 EUR uit het hoofd als 'het plafond' en zetten dat in een berekening.

**Kernpunt**: 6.700 EUR is het niet-geïndexeerde basisbedrag in WIB92. Het effectief toepasselijke plafond is jaarlijks geïndexeerd (voor recente AJ aanzienlijk hoger — orde van grootte 13.000 EUR). Bij het examen: altijd het Cijferzakboekje raadplegen voor het actuele bedrag, nooit het wettekst-basisbedrag gebruiken in een berekening.

<small>📚 WIB92 — art. 87 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Quotient toepassen wanneer er géén gemeenschappelijke aanslag is

**Verkeerde assumptie**: Voor het jaar van huwelijk, scheiding of overlijden 'gewoon' huwelijksquotient toepassen.

**Kernpunt**: Art. 126 §2 sluit gemeenschappelijke aanslag uit in die jaren — geen gemeenschappelijke aanslag betekent géén huwelijksquotient. Twee afzonderlijke aanslagen zonder toerekening tussen partners.

<small>📚 WIB92 — art. 126 §2 — _wettekst_</small>

## Accountant-perspectieven

### Particuliere cliënt (PB-aangifte gezin)

_De accountant die de PB-aangifte voor een gezin voorbereidt of nakijkt._

#### 💰 Fiscaal adviseur

##### 👣 Asymmetrie-check in de aangifte  
_`stap`_

🔗 Bij elk gezin met gemeenschappelijke aanslag eerst de verhouding eigen beroepsinkomsten van beide echtgenoten vergelijken. Indien één echtgenoot < 30 % heeft van het totaal: huwelijksquotient zal automatisch worden toegepast door de fiscus — controleer dat de aangifte-rubrieken correct ingevuld zijn zodat de berekeningsmodule het quotient kan toepassen.

<small>📚 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 88 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Afweging meewerkinkomen ↔ huwelijksquotient  
_`regel`_

🔗 Bij een zelfstandige cliënt waarvan de echtgenoot beperkt of niet werkt: nagaan of een formele toekenning van meewerkinkomen (art. 86) voordeliger is dan het automatisch huwelijksquotient (art. 87-88). Meewerkinkomen geeft eigen sociale rechten aan de meewerkende echtgenoot (pensioenrechten, ziekteverzekering) — een niet-fiscaal voordeel dat zwaarder kan doorwegen dan een kleine fiscale optimalisatie.

<small>📚 WIB92 — art. 33 — _wettekst_ · WIB92 — art. 86 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Uitleg aan cliënt — geen optie, wel automatisch  
_`vuistregel`_

🔗 Cliënten denken vaak dat ze 'het huwelijksquotient moeten vragen' of 'kunnen kiezen'. Het is automatisch en wordt door de fiscus toegepast als de voorwaarden vervuld zijn (en als het gunstig is). De adviseur licht toe waarom de aanslag van het gezin lager uitvalt dan op basis van een eenvoudige optelling van beide aanslagen zou worden verwacht.

<small>📚 WIB92 — art. 87 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Belastingberekening-procedure → [[belastingberekening-pb]] _(moet-verwijzen)_
- → Gezinssituatie + voorwaarden gemeenschappelijke aanslag → [[gezinssituatie]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `vereist`
- [[gezinssituatie]] — Veronderstelt een gemeenschappelijke aanslag (art. 126 WIB92) — gehuwden of wettelijk samenwonenden zonder feitelijke scheiding.
### `triggert`
- [[belastingberekening-pb]] — Toegerekend deel beïnvloedt de afzonderlijke vaststelling van het belastbaar inkomen per echtgenoot in de gemeenschappelijke aanslag.
### `vergelijkbaar_met`
- ⏳ meewerkinkomen
    - **Gelijkenissen**:
        - Beide werken met een 30 %-grens op het beroepsinkomen van de partner
        - Beide gelden enkel bij gemeenschappelijke aanslag (echtgenoten / wettelijk samenwonenden)
        - Beide reduceren de fiscale last van de hoogstverdiener door inkomen 'naar de andere echtgenoot te schuiven'
    - **Verschillen**:
        - Meewerkinkomen (art. 86): vereist effectieve medewerking in de beroepswerkzaamheid; toekenning (echte inkomensallocatie); plafond per activiteit; meewerkende echtgenoot mag max 8.700 EUR eigen inkomen hebben (niet-geïndexeerd)
        - Huwelijksquotient (art. 87-88): geen medewerking vereist; loutere fiscale toerekening (geen werkelijke inkomensbeweging); plafond 6.700 EUR niet-geïndexeerd; automatisch door fiscus toegepast
        - Meewerkinkomen geeft eigen sociale rechten aan de meewerkende echtgenoot; huwelijksquotient niet
    - ⚠️ **Verwarringsrisico**: Beide art-blokken (86 vs 87-88) staan onder dezelfde WIB92-rubriek 'Toekenning en toerekening van een deel van de beroepsinkomsten aan de echtgenoot' en gebruiken hetzelfde '30 %'-getal — examenstudenten halen ze regelmatig door elkaar.
