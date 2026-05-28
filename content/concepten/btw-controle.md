---
title: "BTW-controle"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.taak.5
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-controle.json"
---

# BTW-controle

_Procedure_

📋 Regeling · Anchors: `2.4.taak.5` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: BTW-onderzoek · fiscale controle BTW

## Definitie

🔗 De BTW-controle is het geheel van onderzoeksbevoegdheden van de BTW-administratie om de juistheid van de aangiften en de naleving van de BTW-verplichtingen te verifiëren. Drie hoofdvormen: (1) bureau-controle (administratief — op basis van aangifte + listings + cross-checks); (2) controle ter plaatse (visus op de boekhouding van de belastingplichtige + meelopen in productie); (3) vraag om inlichtingen (schriftelijk of mondeling). Vindt zich aanvullend op de algemene fiscale controle, met BTW-specifieke regels in art. 59-63 WBTW.

<small>📚 WBTW — art. 59-63 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Substantie

📖 Voor de belastingplichtige betekent BTW-controle: medewerking verlenen (geen passieve houding), boekhouding voorleggen, beroepslokalen toegankelijk maken tijdens werkuren, antwoorden binnen de gestelde termijnen (vaak 1 maand). Sancties zijn proportionele geldboeten gekoppeld aan de aard van de overtreding (KB nr. 41). Bij vaststelling van onregelmatigheden volgt regularisatie + nabetaling met interest + boete. Wie spontaan een vergissing aangeeft vóór de controle, krijgt typisch lagere boetes (KB nr. 41 differentieert tussen 'op tijdstip van controle nog niet geregulariseerd' versus 'spontaan voor controle geregulariseerd').

<small>📚 WBTW — art. 70 + art. 84 — _wettekst_ · KB nr. 41 — Tabellen B-J — _kb_</small>

## Rationale

🔗 BTW is een self-assessment-belasting: de Staat kan slechts effectief innen wat de belastingplichtige zelf aangeeft. Controle is dus de tegenmacht die het systeem doet werken — zonder controle zou frauduleus gedrag niet kunnen ontdekt worden. Het uitgebreide arsenaal aan onderzoeksbevoegdheden (verder gaand dan in inkomstenbelasting wegens BTW-fraude-risico via carrousels en factuurzwendel) is hierop afgestemd.

<small>📚 claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 59-66 + KB nr. 41 (boetes) + KB nr. 4 (teruggaaf-procedure)

Controle-termijn standaard 3 jaar (te tellen vanaf 1 januari volgend op het kalenderjaar waarin de BTW opeisbaar werd, art. 81 WBTW). Verlengd tot 7 jaar bij fraude-aanwijzingen of niet-ingediende aangifte; 10 jaar bij ernstige fraude.

**▶️ Trigger start**
- 🔗 Trigger-events voor selectie: (1) anomalieën in BTW-aangiften (rooster 71 plots laag, rooster 72 plots hoog, sprong in IC-leveringen); (2) cross-check listings ↔ klantenlisting toont verschil; (3) sector-acties (horeca, bouw, voertuigen); (4) klacht of denuntiatie; (5) data-analyse via fraude-scoring-algoritmen FOD Financiën.

## Sub-concepten

### 📦 Onderzoeksbevoegdheden (WBTW art. 60-63)  
_`regime` (subconcept)_

#### Definitie

🔗 Vier kernbevoegdheden: (1) art. 60 — bewaren en voorleggen van boekhouding: 10 jaar bewaartermijn; ambtenaren mogen op elk ogenblik inzage vragen; (2) art. 61 — recht op vrije toegang tot beroepslokalen tijdens werkuren (5u-21u) met aanstellingsbewijs; (3) art. 62 — vraag om inlichtingen: schriftelijk of mondeling; antwoord binnen 1 maand verplicht; sancties bij niet-antwoord (art. 70 §4); (4) art. 62bis — onderzoek bij derden (banken, leveranciers, klanten) over de belastingplichtige.

<small>📚 WBTW — art. 60-63 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 📦 Regularisatie-procedure  
_`procedure` (subconcept)_

#### Definitie

📖 Wanneer de controle een onregelmatigheid vaststelt (te weinig aangegeven verschuldigde BTW, ten onrechte afgetrokken BTW, ontbrekende facturen, foutieve roosters): (1) opmaak van een proces-verbaal van regularisatie of een 'kennisgeving van rechtzetting'; (2) belastingplichtige kan reageren met opmerkingen (binnen de gestelde termijn, typisch 1 maand); (3) bij akkoord: regularisatie via volgende BTW-aangifte (roosters 61/62) of via dwangbevel; (4) bij betwisting: bezwaar bij de gewestelijke directeur en uiteindelijk fiscale rechtbank (cross fiscale-procedure-record).

<small>📚 WBTW — art. 84 — _wettekst_</small>

#### Substantie

📖 Bij snelle spontane regularisatie (vóór controle): boete typisch 3-5 % (KB nr. 41 Tabel B). Wachten tot na controle = 10-20 %. Verzwarende omstandigheid 'kwade trouw' kan boete oplopen tot 100 % of strafrechtelijke vervolging.

<small>📚 KB nr. 41 — Tabel B + Art. 6 — _kb_</small>

## Bouwstenen

### ⚙️ Vraag om inlichtingen (art. 62 WBTW)  
_`mechanisme`_

🔗 De BTW-administratie mag elke belastingplichtige en elke derde verzoeken om inlichtingen over verrichtingen of activiteiten. Schriftelijk (aangetekend) of mondeling met PV. Antwoord verplicht binnen 1 maand (verlengbaar bij overmacht). Niet-antwoord = administratieve boete (art. 70 §4) + risico op ambtshalve aanslag (art. 66). Het beroepsgeheim van bv. accountant/advocaat beperkt de antwoordplicht in beperkte mate; het BTW-beroepsgeheim primeert echter zelden bij directe verrichtingen van de belastingplichtige.

<small>📚 WBTW — art. 62 — _wettekst_ · WBTW — art. 70 §4 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 📏 Proportionele geldboeten (KB nr. 41)  
_`drempel`_

📖 Boete-tabellen KB nr. 41 koppelen percentage aan type overtreding. Voorbeelden: ten onrechte afgetrokken BTW: 5 % (≤ 1.250 EUR/jaar) of 10 % (> 1.250 EUR/jaar); niet-uitreiken van factuur zonder BTW-effect: 60 % van de op de handelingen verschuldigde belasting; niet-uitreiken met BTW-effect: 100 %; ontbreken of onjuistheden in factuurvermeldingen: 100 %. Voor 'louter toevallige overtredingen' (te goeder trouw): vaak nihil of beperkt. De boetes zijn proportioneel aan de fraude-omvang.

<small>📚 KB nr. 41 — Tabel B + Tabel C — _kb_</small>

### ⚙️ Ambtshalve aanslag (art. 66 WBTW)  
_`mechanisme`_

📖 Wanneer de belastingplichtige zijn aangifte niet, te laat of onvolledig indient en niet binnen het maand op de aanmaning reageert, kan de administratie een ambtshalve aanslag vestigen: de fiscus schat zelf de verschuldigde BTW (op basis van vorige aangiftes, sectoriële cijfers, indirecte aanwijzingen). De bewijslast keert om: de belastingplichtige moet aantonen dat de schatting overdreven is. Verbonden met opcentiemen van boete (typisch 20 %).

<small>📚 WBTW — art. 66 — _wettekst_</small>

### ⚠️ Carrousel-fraude — speciale alertheid  
_`risico`_

🔗 BTW-administratie heeft bijzondere aandacht voor carrousel-fraude bij grensoverschrijdende handelingen: missing-trader keten waarbij één lid van de keten verdwijnt na BTW-aftrek te claimen zonder verschuldigde BTW door te storten. Sectoren: mobiele telefonie, computers, voertuigen, energie (vandaar 250.000 EUR-drempel kwartaal/maand). Wie 'wist of moest weten' van betrokkenheid in fraude-keten verliest het aftrekrecht (HvJ-rechtspraak Kittel + Bonik).

<small>📚 HvJ — Kittel/Bonik — _rechtspraak_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 BTW-controle ter plaatse — verloop 🔗

_BTW-controleur arriveert onaangekondigd bij Zelena Bio NV op 15 maart 2026 om 10u om controleperiode 2023-2025 te onderzoeken._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "Stap 1 — Aanmelding: controleur toont aanstellingsbewijs (art. 61 WBTW); medewerker brengt zaakvoerder.",
    "Stap 2 — Voorlegging boekhouding: aankoopdagboek + verkoopdagboek + facturen + bankuittreksels 2023-2025 (10-jaar-bewaartermijn art. 60).",
    "Stap 3 — Onderzoek: controleur steekproeft inkomende facturen op aftrek-uitsluitingen (autokosten, onthaal) en uitgaande op tarief-juistheid + factuurvermeldingen.",
    "Stap 4 — Vaststelling: 2024 — receptiekost 8.000 EUR + 1.680 EUR BTW ten onrechte volledig afgetrokken (= uitsluiting art. 45 §3, 4°).",
    "Stap 5 — Kennisgeving rechtzetting: 1.680 EUR terug te storten + boete 10 % (= 168 EUR) + nalatigheidsinteresten.",
    "Stap 6 — Reactie binnen 1 maand: Zelena stuurt opmerkingen of akkoord."
  ]
}
```

<small>📚 WBTW — art. 60-62 — _wettekst_ · WBTW — art. 45 §3, 4° — _wettekst_ · KB nr. 41 — Tabel B — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Spontane regularisatie vóór controle — boete-effect 📖

_Aurelia Holding ontdekt in januari 2026 dat ze in 2025 voor 10.000 EUR BTW ten onrechte heeft afgetrokken. Geen controle aangekondigd._

**Weergave** `vergelijkingstabel`:

```json
{
  "kolommen": [
    "Scenario",
    "Boete (KB nr. 41 Tabel B/H)",
    "Totaal"
  ],
  "rijen": [
    [
      "Spontane regularisatie via aangifte (rooster 61) + brief aan controleur",
      "5 % (overtreding > 1.250 EUR — Tabel H, kolom 'spontaan')",
      "500 EUR + nalatigheidsinteresten"
    ],
    [
      "Pas bij controle (2027) geregulariseerd",
      "10 % (overtreding > 1.250 EUR — Tabel H, kolom 'bij controle')",
      "1.000 EUR + boete + interesten"
    ]
  ]
}
```

<small>📚 KB nr. 41 — Tabel H — _kb_</small>

## Valkuilen

### ⚠️ BTW-controle gelijkstellen met fiscale controle (inkomstenbelasting)

**Verkeerde assumptie**: De controle-procedure is hetzelfde voor BTW en inkomstenbelasting.

**Kernpunt**: BTW heeft eigen onderzoeksregime (art. 59-63 WBTW) — verder gaand dan inkomstenbelasting: directe toegang tot lokalen tijdens werkuren zonder voorafgaande verwittiging, korte antwoord-termijnen (1 maand standaard), en specifieke boete-schalen (KB nr. 41). Beide kunnen evenwel gecombineerd worden in een 'multidisciplinaire controle'.

<small>📚 WBTW — art. 59-63 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### ⚠️ Niet-antwoord op vraag om inlichtingen onschadelijk vinden

**Verkeerde assumptie**: 'Als ik niet antwoord, gaat de controleur wel weg.'

**Kernpunt**: Niet-antwoord = boete art. 70 §4 (typisch 250-1.250 EUR per niet-antwoord) + omkering bewijslast: de fiscus kan ambtshalve aanslag vestigen (art. 66) en de bewijslast keert om — de belastingplichtige moet aantonen dat de schatting fout is. Antwoorden binnen 1 maand is altijd voordeliger, ook als het antwoord 'ik weet het niet meer' is (met onderbouwing).

<small>📚 WBTW — art. 62 + art. 66 + art. 70 §4 — _wettekst_</small>

## Accountant-perspectieven

### Kantoor begeleidt cliënt door BTW-controle

_De accountant die de cliënt voorbereidt op, vergezelt tijdens of begeleidt na een BTW-controle._

#### 👥 Begeleider

##### 👣 Voorbereiding op aangekondigde controle  
_`stap`_

🔗 Bij aankondiging controle: (1) self-audit van de controleperiode — risicozones identificeren (autokosten, onthaal, gemengde aftrek); (2) spontane regularisatie van vastgestelde fouten vóór controle (= boete halveert); (3) boekhouding en facturen klaarzetten in zoek-formaat; (4) cliënt instrueren: alleen antwoorden op gestelde vragen, geen vrije gesprekken met controleur; (5) zorgen voor aanwezigheid van bevoegde verantwoordelijke + accountant tijdens controle.

<small>📚 KB nr. 41 — Tabel H — spontaan vs bij controle — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 Betwisting van een kennisgeving van rechtzetting  
_`stap`_

🔗 Bij ontvangst rechtzetting: (1) binnen 1 maand schriftelijk reageren met onderbouwde opmerkingen — niet zwijgen want zwijgen = stilzwijgend akkoord; (2) bij blijvende betwisting: bezwaar bij gewestelijke directeur binnen 6 maanden; (3) indien beslissing ongunstig: dagvaarding voor de fiscale rechtbank (3 maanden). Cross-verwijzing fiscale procedure (zie fiscale-procedure-record). Het beroepsgeheim van de accountant verzet zich tegen bepaalde antwoorden over cliënten van de cliënt — adviseur moet hier balanceren.

<small>📚 WBTW — art. 84 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-aangifte (controle-basis) → [[btw-aangifte]] _(moet-verwijzen)_
- ↪ Fiscale controle generiek → [[fiscale-controle]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `beinvloed_door`
- [[btw-aangifte]] — Anomalieën in een ingediende aangifte triggeren vaak een controle (selectie-criterium).
### `vergelijkbaar_met`
- [[fiscale-controle]]
    - **Gelijkenissen**:
        - Beide zijn onderzoekprocedures door FOD Financiën
    - **Verschillen**:
        - BTW-controle gebruikt art. 60-63 WBTW met kortere termijnen en directe toegang; fiscale-controle gebruikt art. 315-345 WIB92 met andere modaliteiten
    - ⚠️ **Verwarringsrisico**: Stagiairs gebruiken 'fiscale controle' generiek terwijl BTW een eigen regime heeft.
