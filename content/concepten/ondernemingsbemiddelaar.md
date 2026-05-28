---
title: "Ondernemingsbemiddelaar"
concept_type: "actor"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.X
  - 3.0.X.A
tags:
  - concept
  - schema-2.2
  - type-actor
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/ondernemingsbemiddelaar.json"
---

# Ondernemingsbemiddelaar

_Actor_

🏢 Entiteit · Anchors: `3.0.X` · `3.0.X.A` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

> [!warning] **Uitdovend regime** — wordt afgebouwd; check sinds-/tot-data.

**Synoniemen**: médiateur d'entreprise · minnelijk schuldbemiddelaar voor ondernemingen

## Definitie

🔗 De ondernemingsbemiddelaar is een door de voorzitter van de ondernemingsrechtbank aangewezen neutrale derde (vaak een advocaat, gecertificeerd accountant of bedrijfsrevisor met ervaring in herstructureringen) die een onderneming in moeilijkheden begeleidt bij het tot stand brengen van een **minnelijk akkoord** met haar schuldeisers. De bemiddelaar werkt buitengerechtelijk en vertrouwelijk — er is geen openbare procedure, geen opschorting van uitvoeringsmaatregelen, en zijn aanstelling wordt niet gepubliceerd. Hij heeft geen beslissingsbevoegdheid; hij faciliteert en stelt voor.

<small>📚 WER — art. XX.36 (oud, opgeheven 2023) — _wettekst_ · WER — art. XX.39 + XX.83/22 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Praktisch: de bemiddelaar zit met de schuldenaar én de hoofdschuldeisers rond de tafel en zoekt naar een betalingsregeling die voor iedereen aanvaardbaar is — vaak een gespreide afbetaling, gedeeltelijke kwijtschelding, of bijkomende zekerheden. Voordeel boven gerechtelijke reorganisatie: geen publieke procedure, geen gerechtskosten op publieke schaal, geen opname in Regsol. Nadeel: geen wettelijke opschorting; één onwillige schuldeiser kan de operatie laten falen door uitvoering te eisen. Vandaar dat de bemiddelaar vaak een 'plan B' (gerechtelijke reorganisatie) in petto houdt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ondernemingsbemiddelaar is het 'ultra-zachte' instrument in de WER-trap. Hij richt zich op ondernemingen die structureel solvabel zijn maar tijdelijk illiquide, en op situaties waar een gerechtelijke procedure (met haar publieke stigma) de cliëntrelaties zou verwoesten. De 2023-hervorming heeft de ondernemingsbemiddelaar als zelfstandige figuur grotendeels weggewerkt en vervangen door de 'herstructureringsdeskundige' binnen een (eventueel besloten) gerechtelijke reorganisatie — maar het concept van vertrouwelijke bemiddeling blijft het organiserend principe.

<small>📚 WER — W 2023-06-07/07, art. 44 (opheffing art. XX.36) — _wettekst_ · WER — art. XX.83/22 (herstructureringsdeskundige) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `uitdovend` · sinds **2023-09-01** · basis: Vroegere WER art. XX.36 opgeheven door W 7-06-2023, art. 44. De rol leeft conceptueel verder via de 'herstructureringsdeskundige' (art. XX.83/22) in een besloten gerechtelijke reorganisatie.

Voor de exam-stof blijft de figuur belangrijk omdat veel handboeken en praktijkliteratuur het pre-2023 model nog beschrijven. De moderne equivalent is de herstructureringsdeskundige binnen een besloten gerechtelijke reorganisatie — vergelijkbare functie (neutrale bemiddelaar, vertrouwelijk) maar met rechterlijke aanstelling én bescherming.

**✅ Voor**
- 🔗 Ondernemingen in vroege moeilijkheden waar publieke bekendmaking schade zou berokkenen (B2B-dienstverleners, advocatenkantoren, accountantskantoren). Hier helpt bemiddeling om informeel tot betalingsregelingen te komen.

**🚫 Niet voor**
- 🔗 Ondernemingen met een groot aantal kleine schuldeisers of waar een hoofdschuldeiser absoluut weigert mee te werken — daar werkt bemiddeling niet en is gerechtelijke reorganisatie aangewezen (de wettelijke opschorting + cross-class cram-down dwingt mee).

## Sub-concepten

### 📦 Aanstelling en mandaat  
_`procedure` (subconcept)_

#### Definitie

🤖 De schuldenaar of de KOM verzoekt de voorzitter van de ondernemingsrechtbank om aanstelling van een ondernemingsbemiddelaar. De voorzitter benoemt iemand op de lijst van erkende bemiddelaars (vroegere wet) of een geschikte professional uit de praktijk. De aanstelling is geen openbaar vonnis; alleen schuldenaar en aangewezen schuldeisers worden in kennis gesteld. Het mandaat is meestal beperkt in tijd (3-6 maanden) en kan worden verlengd.

<small>📚 WER — art. XX.36 (oud) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Vertrouwelijkheid van de bemiddeling  
_`principe` (subconcept)_

#### Definitie

🔗 Alle uitwisselingen tijdens de bemiddeling zijn vertrouwelijk. Documenten, voorstellen en concessies kunnen niet als bewijs worden gebruikt in een latere gerechtelijke procedure — een fundamentele garantie zonder welke partijen geen vrije onderhandelingen zouden voeren. Dit beginsel verschilt fundamenteel van bv. een KOM-onderzoek, waar het verslag wél bij een latere reorganisatie kan worden gevoegd.

<small>📚 Ger.W. — art. 1728 (algemeen beginsel bemiddeling) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Minnelijk akkoord als beoogd resultaat  
_`instrument` (subconcept)_

#### Definitie

📖 De bemiddelaar werkt toe naar een schriftelijk minnelijk akkoord tussen de schuldenaar en (een aantal) schuldeisers. Het akkoord kan vrijblijvend blijven, of — sterker — kan worden voorgelegd aan de ondernemingsrechtbank voor **homologatie** binnen een gerechtelijke reorganisatie (art. XX.64 of art. XX.83/30 voor besloten variant). Pas na homologatie krijgt het akkoord uitvoerbare kracht en immuniteit tegen latere acties (zoals actio pauliana).

<small>📚 WER — art. XX.64 — _wettekst_ · WER — art. XX.83/30 — _wettekst_</small>

### 📦 Onderscheid met curator en gerechtelijke bewindvoerder  
_`kader` (subconcept)_

#### Definitie

🔗 **Curator** (faillissement, art. XX.123): neemt het beheer over van de gefailleerde, vereffent activa. **Gerechtelijke bewindvoerder/gerechtsmandataris** (GR of voorlopige maatregelen): vervangt het bestuur of staat het bij, met machtigingsbevoegdheid. **Ondernemingsbemiddelaar**: niet-bindend, faciliteert, neemt geen beheer over en heeft geen machtigingsbevoegdheid. De ondernemingsbemiddelaar is dus de zachte variant — zonder zwaard, alleen met spreek-en-luister-kracht.

<small>📚 WER — art. XX.123 e.v. (curator) — _wettekst_ · WER — art. XX.31 (voorlopige bewindvoerder) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 🚧 Geen wettelijke opschorting tijdens bemiddeling  
_`beperking`_

🔗 Anders dan bij gerechtelijke reorganisatie is er **geen wettelijke opschorting** van uitvoeringsmaatregelen. Schuldeisers kunnen tijdens de bemiddeling gewoon dagvaarden, beslag leggen of het faillissement vorderen. Het 'sociaal contract' tussen partijen om dat niet te doen tijdens de gesprekken is informeel — niet rechtens afdwingbaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Erelonen ten laste van de schuldenaar  
_`regel`_

🔗 De erelonen en kosten van de ondernemingsbemiddelaar zijn voor rekening van de schuldenaar (die ze meestal vooraf moet provisioneren). De rechtbank kan bij geschil de honorering achteraf vaststellen. Dit is een aandachtspunt: een onderneming die de bemiddelaar niet kan betalen, is meestal sowieso al voorbij het stadium waar bemiddeling kans van slagen heeft.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Bemiddeling redt accountantskantoor — Aurelia Tax & Audit 🔗

_Aurelia Tax & Audit BV (15 medewerkers) verloor twee grote klanten en kan haar bedrijfsleidersrekening + huur niet meer betalen. Een publieke gerechtelijke reorganisatie zou het vertrouwen van bestaande klanten ondermijnen._

**Weergave** `stappenlijst`:

```json
{
  "tekst": "Week 1: Aurelia vraagt ondernemingsbemiddelaar aan via KOM\nWeek 2: Voorzitter ondernemingsrechtbank stelt mediator aan (advocaat-curator)\nWeek 3-6: Vertrouwelijke gesprekken met (a) bank — uitstel kapitaalsaflossing 12 maanden; (b) verhuurder — spreiding huurachterstand over 6 maanden\nWeek 7: Minnelijk akkoord ondertekend door alle hoofdcrediteuren\nWeek 8: Optioneel: homologatie binnen besloten GR voor uitvoerbare kracht\nResultaat: cliënten merken niets. Aurelia blijft draaien."
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Bemiddelaar = curator

**Verkeerde assumptie**: De ondernemingsbemiddelaar neemt het beheer van de cliënt over.

**Kernpunt**: Onjuist. De ondernemingsbemiddelaar adviseert en bemiddelt; het bestuur blijft volledig in controle. Bestuur dat na aanstelling van een bemiddelaar lui wordt of beslissingen overlaat, blijft volledig aansprakelijk.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Vertrouwelijkheid = wettelijke opschorting

**Verkeerde assumptie**: Tijdens een bemiddeling kunnen schuldeisers geen uitvoeringsmaatregelen treffen.

**Kernpunt**: Vertrouwelijkheid geldt voor de inhoud van de gesprekken (mag niet als bewijs gebruikt worden). Maar er is geen wettelijke opschorting van betalingsverplichtingen of uitvoeringsmaatregelen. Een onwillige schuldeiser kan tijdens de bemiddeling gewoon dagvaarden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Minnelijk akkoord is automatisch beschermd

**Verkeerde assumptie**: Een minnelijk akkoord dat via bemiddeling is bereikt, is automatisch immuun voor latere actio pauliana.

**Kernpunt**: Immuniteit ontstaat pas na **homologatie** binnen een gerechtelijke reorganisatie (art. XX.83/30 § 2). Een puur buitengerechtelijk minnelijk akkoord kan bij een latere faillissementsprocedure worden aangevallen — vooral als één schuldeiser onevenredig werd bevoordeeld.

<small>📚 WER — art. XX.83/30 § 2 — _wettekst_</small>

## Accountant-perspectieven

### Gecertificeerd accountant als ondernemingsbemiddelaar

#### 👥 Begeleider

##### ✴️ Neutrale positie bewaken — geen advisering van één partij  
_`principe`_

🔗 Als bemiddelaar werkt de accountant voor alle partijen tegelijk. Dat betekent: geen advisering ten gunste van de schuldenaar of een schuldeiser, geen partij kiezen, geen vertrouwelijke informatie van de ene partij doorgeven aan de andere. Iedere schijn van partijdigheid kan tot wraking leiden en het hele proces ondermijnen.

<small>📚 ITAA-norm onafhankelijkheid — Algemeen — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Accountant van schuldenaar — voorbereiden op bemiddeling

#### 🧭 Adviseur

##### 👣 Compleet financieel dossier voorbereiden voor bemiddelaar  
_`stap`_

🔗 Maak: (a) actuele balans + resultatenrekening tussentijds; (b) 13-week + 12-maand cashflow-projectie; (c) gedetailleerde schuldeiserslijst met openstaande bedragen + zekerheden; (d) lijst van onderhandelbare punten per schuldeiser (uitstel, kwijtschelding, bijkomende zekerheid). Een goed gedocumenteerd vertrekpunt versnelt de bemiddeling en versterkt de geloofwaardigheid van de schuldenaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Parent kader — WER boek XX → [[insolventierecht-wer-boek-xx]] _(moet-verwijzen)_
- → KOM als toeleidings-instantie → [[kamers-voor-ondernemingen-in-moeilijkheden]] _(moet-verwijzen)_
- → Gerechtelijke reorganisatie als formeel vervolg → [[gerechtelijke-reorganisatie]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[insolventierecht-wer-boek-xx]]
### `uitgevoerd_door`
- [[kamers-voor-ondernemingen-in-moeilijkheden]]
