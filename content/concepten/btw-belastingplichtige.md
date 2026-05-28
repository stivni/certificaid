---
title: "BTW-belastingplichtige"
concept_type: "actor"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 2.4.II
  - 2.4.II.A
  - 2.4.II.B
tags:
  - concept
  - schema-2.2
  - type-actor
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-belastingplichtige.json"
---

# BTW-belastingplichtige

_Actor_

🏢 Entiteit · 📋 Regeling · Anchors: `2.4.II` · `2.4.II.A` · `2.4.II.B` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: btw-plichtige · assujetti TVA — **Vertalingen**: fr: assujetti à la TVA

## Definitie

📖 Een btw-belastingplichtige is eenieder die in de uitoefening van een economische activiteit geregeld en zelfstandig — met of zonder winstoogmerk, hoofdzakelijk of aanvullend — leveringen van goederen of diensten verricht die in het W.BTW zijn omschreven, ongeacht waar de economische activiteit wordt uitgeoefend. De definitie staat in art. 4, §1 W.BTW en bevat vier cumulatieve kenmerken: (a) economische activiteit, (b) geregeld karakter, (c) zelfstandigheid, (d) leveringen of diensten in de zin van het W.BTW.

<small>📚 W.BTW — art. 4, §1 — _wettekst_</small>

## Substantie

🔗 Wie als btw-belastingplichtige kwalificeert, treedt toe tot het btw-stelsel als 'doorgever': hij rekent btw aan op zijn verkopen (output-btw) en mag de btw op zijn aankopen aftrekken (input-btw, zie `btw-aftrek`). Hij krijgt een btw-identificatienummer (BE0XXX.XXX.XXX), is verplicht facturen uit te reiken volgens KB nr. 1 en moet periodiek aangifte doen. Niet de wettelijke vorm telt (een vzw of feitelijke vereniging kan belastingplichtig zijn), maar wel de aard van de activiteit. De toets is feitelijk-economisch — een werknemer is uitgesloten (geen zelfstandigheid), een occasionele verkoper ook (geen geregeld karakter).

<small>📚 W.BTW — art. 4, §1, tweede lid — _wettekst_ · W.BTW — art. 50 + art. 53 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio: btw moet drukken op het verbruik, niet op de productiefactoren. Wie geregeld en zelfstandig deelneemt aan het economisch verkeer is logischerwijs de inner-doorgever van de belasting. De ruime functionele definitie (geen oogmerk-vereiste, geen winstvereiste, geen vormvereiste) zorgt ervoor dat ook vzw's, vrije beroepen, holdings, overheidsbedrijven en buitenlandse ondernemingen onder het stelsel kunnen vallen — telkens wanneer ze leveringen of diensten verrichten die binnen de scope van het W.BTW vallen.

<small>📚 W.BTW — art. 4 — _wettekst_ · Richtlijn 2006/112/EG — art. 9 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 📖 Elke ondernemer (natuurlijk persoon, vennootschap, vereniging) die regelmatig en zelfstandig economische handelingen verricht: handelaars, vrije beroepen, ambachtslui, vastgoedontwikkelaars, holdings die actief management voeren, buitenlandse ondernemingen met Belgische klanten.

**🚫 Niet voor**
- 📖 Loontrekkenden en personen in een ondergeschiktheidsverhouding worden expliciet uitgesloten (art. 4, §1, tweede lid). Ook particulieren die occasioneel iets verkopen (geen geregeld karakter), zuivere holdings die enkel aandelen aanhouden zonder actief management, en de overheid voor zover ze gezagshandelingen verricht (jure imperii).

**📋 Voorwaarden**
- 📖 Cumulatief vereist: (1) economische activiteit — exploitatie van een goed of recht met het oog op duurzaam inkomen; (2) geregeld karakter — herhaaldelijke en niet-occasionele handelingen; (3) zelfstandigheid — geen ondergeschiktheid; (4) leveringen of diensten in de zin van het W.BTW. Het winstoogmerk is GEEN voorwaarde — ook een vzw kan belastingplichtig zijn.

**▶️ Trigger start**
- 🔗 De belastingplicht begint vanaf het ogenblik dat de persoon de intentie heeft een economische activiteit aan te vatten en daartoe voorbereidende handelingen verricht (bv. investeringen, huur lokaal). Formele identificatie via 604A-aangifte bij de FOD Financiën — uiterlijk vóór de start van de activiteit.

**⏹ Trigger einde**
- 📖 Belastingplicht eindigt bij stopzetting van de economische activiteit, te melden via 604C-aangifte. Bij overdracht van algemeenheid of bedrijfstak (art. 11 W.BTW) volgt geen btw-heffing — de overnemer treedt in de schoenen van de overdrager.

**⚠️ Risico**
- 🔗 Bij twijfelgevallen (vzw met commerciële nevenactiviteit, vermogensvennootschap met af-en-toe-verhuur, particulier-handel) kan de fiscus achteraf belastingplicht vaststellen — met regularisatie van uitgaande btw zonder dat de afnemers nog kunnen worden geïnd. Cash-effect: btw moet uit eigen middelen worden bijgepast.

## Sub-concepten

### 📦 Vier categorieën btw-belastingplichtige  
_`kader` (subconcept)_

#### Substantie

🔗 Naargelang de mix van uitgaande handelingen onderscheidt het W.BTW vier categorieën, elk met eigen aftrek-rechten en aangifte-verplichtingen. De categorie bepaalt mede de boekhoudkundige verwerking van input-btw.

<small>📚 W.BTW — art. 44 + art. 45 + art. 46 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Vergelijking vier categorieën  
_`vuistregel`_

**Substantie**: 🔗 Vier categorieën — verschil zit in aftrekrecht.

<small>📚 W.BTW — art. 44 + art. 45 + art. 46 — _wettekst_</small>

### 📦 Wie kan btw-belastingplichtige zijn?  
_`kader` (subconcept)_

#### Substantie

📖 De definitie is rechtsvorm-neutraal — het W.BTW spreekt over 'eenieder'. Concreet: natuurlijke personen (zelfstandige, vrij beroep, eenmanszaak), vennootschappen (BV, NV, CommV, Maatschap met rechtspersoonlijkheid), verenigingen (vzw, feitelijke vereniging), openbare instellingen (voor zover ze niet als overheid jure imperii handelen) en buitenlandse ondernemingen die belastbare handelingen verrichten in België.

<small>📚 W.BTW — art. 4 — _wettekst_ · W.BTW — art. 6 — _wettekst_</small>

## Voorbeelden

### 💡 Vier casussen — wel of geen btw-belastingplichtige? 🔗

_Toets de definitie van art. 4 W.BTW telkens op de vier kenmerken: economische activiteit · geregeld · zelfstandig · leveringen/diensten W.BTW._

| Casus | Belastingplichtig? | Reden |
| --- | --- | --- |
| Werknemer bij accountantskantoor, doet daarnaast occasioneel een vriendendienst tegen betaling | Nee | Ondergeschiktheidsverhouding + occasioneel karakter — geen 'geregeld + zelfstandig' |
| Particulier verkoopt twee oude auto's via tweedehandsplatform | Nee | Geen geregeld karakter — incidenteel |
| Vzw die jaarlijks 200 sportworkshops organiseert tegen betaling | Ja | Geregeld + zelfstandig + dienstverrichting onder bezwarende titel — winstoogmerk irrelevant. Mogelijk wel vrijgesteld onder art. 44, §2, 3° |
| Holding zonder activiteit (enkel aandelenportefeuille en dividend) | Nee | Geen economische activiteit (passief beheer van vermogen) — geen aftrekrecht op kosten |
| Holding die ook actief management-fees factureert aan dochters | Ja, gemengd of gedeeltelijk | Het management-deel is een dienstverrichting onder bezwarende titel — gedeeltelijke belastingplicht |

<small>📚 W.BTW — art. 4 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Vrijgestelde belastingplichtige ≠ niet-belastingplichtige

**Verkeerde assumptie**: Een arts of bank 'doet niet aan btw' — dus is geen belastingplichtige in de zin van art. 4 W.BTW.

**Kernpunt**: Een vrijgestelde belastingplichtige (art. 44 W.BTW: medisch, onderwijs, sociale zorg, financieel) is wel degelijk belastingplichtig in de zin van art. 4. Hij rekent geen btw aan en heeft geen aftrekrecht, maar hij valt onder het stelsel — denkt aan bepaalde rapportering, klantenlisting, intracommunautaire verwervingen waarop hij wél btw verschuldigd is. Niet-belastingplichtig is enkel de particulier of de overheid (jure imperii).

<small>📚 W.BTW — art. 4 + art. 44 — _wettekst_</small>

### ⚠️ Winstoogmerk is geen voorwaarde

**Verkeerde assumptie**: Een vzw is per definitie niet btw-plichtig want zonder winstoogmerk.

**Kernpunt**: Art. 4, §1 W.BTW zegt expliciet 'met of zonder winstoogmerk, hoofdzakelijk of aanvullend'. Een vzw die geregeld diensten of leveringen tegen betaling verricht is belastingplichtig — mogelijk vrijgesteld onder art. 44, §2 (sociale doelen) maar wel binnen het stelsel.

<small>📚 W.BTW — art. 4, §1 — _wettekst_</small>

### ⚠️ Holding-test: actief versus passief

**Verkeerde assumptie**: Elke holding-vennootschap is btw-plichtig.

**Kernpunt**: Een zuivere holding (enkel aandelen aanhouden + dividend incasseren) verricht geen economische activiteit en is geen btw-belastingplichtige — geen aftrekrecht op kosten. Pas wanneer de holding actief management-, advies- of administratieve diensten verricht tegen vergoeding aan haar dochters, wordt ze (gedeeltelijk) belastingplichtig. Vaste rechtspraak HvJ-EU (Polysar, Larentia + Minerva).

<small>📚 HvJ-EU Polysar (C-60/90) — 20-06-1991 — _rechtspraak_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Eigen kantoor — kwalificatie cliënt

_Bij intake van een nieuwe cliënt of nieuwe activiteit kwalificeert de accountant de btw-status._

#### 💰 Fiscaal adviseur

##### 👣 Intake-checklist btw-kwalificatie  
_`stap`_

**Substantie**: 🔗 Bij intake test de accountant: (1) is er een economische activiteit (vs zuiver passief vermogen)? (2) is ze geregeld (vs occasioneel)? (3) is ze zelfstandig (vs werknemer)? (4) valt ze binnen W.BTW (leveringen/diensten) of erbuiten (financieel, dividend)? Antwoord JA op alle vier → belastingplichtige. Tweede vraag: gewoon, vrijgesteld, gemengd of gedeeltelijk? Bepaalt het aftrekrecht-regime.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 👥 Begeleider

##### 👣 Begeleiding 604A-aangifte  
_`stap`_

**Substantie**: 🔗 Bij start: 604A-aangifte indienen bij FOD Financiën vóór aanvang activiteit. Verkrijg btw-identificatienummer (BE-formaat). Daarna: keuze maand- of kwartaalaangifte (KB nr. 1 art. 18: kwartaal als omzet < 2 500 000 EUR; uitzondering 250 000 EUR voor bepaalde sectoren), inschrijven in OSS bij e-commerce, configureren boekhoudpakket met juiste btw-codes.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-eenheid (groepsregime) → [[btw-eenheid]] _(moet-verwijzen)_
- → Vrijstellingsregeling kleine onderneming → [[vrijstellingsregeling-kleine-onderneming]] _(moet-verwijzen)_
- → Opstart-formaliteiten + 604-aangifte → [[opstart-btw-formaliteiten]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw]]
