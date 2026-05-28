---
title: "Overdracht van een onderneming"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - gebeurtenis
  - regeling
ankers:
  - 3.0.taak.2
  - 3.0.taak.3
  - 2.3.III.B
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/overdracht-onderneming.json"
---

# Overdracht van een onderneming

_Kader_

🏛️ Kader · 📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.taak.2` · `3.0.taak.3` · `2.3.III.B` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: M&A-transactie · overname · verkoop van een onderneming

## Definitie

🔗 Overdracht van een onderneming is de transactie waarbij de controle of het eigenaarschap van een actieve onderneming overgaat van de overdrager (verkoper) naar de overnemer (koper). De twee basisstructuren zijn share-deal (verkoop van de aandelen van de vennootschap die de onderneming uitbaat — de juridische huid blijft, alleen de eigenaar wisselt) en asset-deal (verkoop van het handelsfonds zelf — de activa, contracten, klantenbestand en eventueel personeel gaan over naar een andere vennootschap, terwijl de oorspronkelijke vennootschap voortbestaat zonder die activiteit). Geregeld via koop-verkoop-overeenkomst (Share Purchase Agreement of Asset Purchase Agreement); valt buiten WVV boek 12 want het is een gewone contractuele transactie tussen zelfstandige partijen.

<small>📚 WVV — art. 7:41 (overdracht aandelen NV) — _wettekst_ · WVV — art. 5:42 (overdracht aandelen BV) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Economisch leveren share-deal en asset-deal vaak hetzelfde resultaat: de koper krijgt de operationele activiteit, de verkoper krijgt cash. Maar fiscaal, juridisch en boekhoudkundig lopen ze grondig uiteen. Bij share-deal blijft alles in de vennootschap: contracten lopen door, vergunningen blijven geldig, schulden volgen mee. Bij asset-deal moet alles individueel worden overgedragen — sommige contracten vergen instemming van tegenpartij; vergunningen moeten soms opnieuw worden aangevraagd; schulden blijven bij de verkoper (tenzij expliciet overgenomen). De keuze tussen beide structuren bepaalt de fiscale druk, het risicoprofiel en de complexiteit van de transactie — vandaar dat dit een sleutel-vergelijking is in elke M&A-context.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom bestaan twee aparte structuren? Omdat verkoper en koper tegengestelde fiscale belangen hebben. De verkoper verkiest doorgaans share-deal: meerwaarde op aandelen is in VenB grotendeels vrijgesteld (art. 192 WIB92) of tegen verlaagd tarief; in PB onder voorwaarden vrijgesteld. De koper verkiest doorgaans asset-deal: een hogere boekwaarde van activa en goodwill leidt tot grotere afschrijvingen en dus lagere belastbare winst. Dit fiscale asymmetrie is het kernpunt van elke prijsonderhandeling — wie de fiscale 'win' wegneemt, moet daar prijs voor betalen.

<small>📚 WIB92 — art. 192 (vrijstelling meerwaarde aandelen VenB) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 192; Wbtw art. 11 + KB nr. 1 art. 11; WVV (overdracht aandelen); CAO 32bis (overdracht onderneming + werknemers); Burgerlijk Wetboek (koop)

**✅ Voor**
- 🤖 Een ondernemer wil zijn activiteit verkopen aan een externe overnemer (familie zonder opvolger, financiële investeerder, strategische koper).
- 🤖 Een groep wil een niet-strategische activiteit afstoten via verkoop van een dochtervennootschap (carve-out via share-deal) of via verkoop van losse activa (carve-out via asset-deal).

**📋 Voorwaarden**
- 🔗 Schriftelijke overeenkomst (SPA/APA) met alle elementen: prijs, beschrijving voorwerp, garanties, vrijwaringen, opschortende voorwaarden, closing-procedure.
- 📖 Bij asset-deal die kwalificeert als overdracht van een algemeenheid of bedrijfsafdeling (art. 11 Wbtw): vaststelling in een geschrift dat aan elke partij wordt overhandigd, met datum, identificatie, beschrijving voorwerp en prijs (KB nr. 1 art. 11).
- 🔗 Bij overdracht onderneming met personeel: respecteer CAO 32bis — werknemers gaan over met behoud van anciënniteit en arbeidsvoorwaarden.

**👍 Voordeel**
- 🔗 Snelheid en flexibiliteit: een gewone koop-verkoop hoeft geen WVV-boek 12-procedure te doorlopen — geen voorstel, geen revisorverslag op de transactie zelf, geen wettelijke wachttermijn.
- 🤖 Contractuele vrijheid om risico's, garanties en vrijwaringen op maat te onderhandelen — zelfde overdracht kan zeer verschillend worden geprijsd afhankelijk van de garantie-pakket.

**⚠️ Risico**
- 🔗 Bij share-deal: koper neemt alle historische schulden mee — bekend (in balans) en onbekend (latente fiscale claims, milieuverplichtingen, geschillen). Vandaar de cruciale rol van due diligence + R&W-garanties.
- 🤖 Bij asset-deal: contracten die niet 'overdraagbaar' zijn (intuitu personae, change-of-control-clausules) vergen instemming van tegenpartijen — risico op weigering of heronderhandeling.
- 🤖 Fiscale herkwalificatie: een asset-deal kan door de fiscus worden gezien als verkapte vereffening; een share-deal kan worden gezien als verkapte dividend-uitkering — anti-misbruik blijft mogelijk.

## Sub-concepten

### 📦 Share-deal — aandelenovername  
_`verrichting` (subconcept)_

#### Definitie

🔗 De koper neemt de aandelen van de vennootschap die de onderneming uitbaat. De vennootschap blijft juridisch ongewijzigd — alleen haar aandeelhouders veranderen. Alle activa, passiva, contracten en arbeidsovereenkomsten blijven in de vennootschap; geen individuele overdracht nodig.

<small>📚 WVV — art. 7:41 + 5:42 (overdracht aandelen) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

📖 Fiscaal voor verkoper-vennootschap: meerwaarde op aandelen onder DBI-voorwaarden vrijgesteld (art. 192 WIB92). Fiscaal voor verkoper-natuurlijke persoon: meestal vrijgesteld als 'normaal beheer privévermogen' (art. 90, 9°/1 WIB92), tenzij speculatie. Voor koper: aankoopprijs zit in de boekwaarde van de deelneming — niet afschrijfbaar. Btw: geen btw op aandelen.

<small>📚 WIB92 — art. 192 — _wettekst_ · WIB92 — art. 90, 9° — _wettekst_</small>

### 📦 Asset-deal — handelsfonds-overname  
_`verrichting` (subconcept)_

#### Definitie

🔗 De koper neemt het handelsfonds (activa, klantenbestand, voorraden, goodwill) over zonder de juridische schil. Schulden blijven bij de verkoper, tenzij specifiek overgenomen. Contracten gaan niet automatisch over — vereist instemming van tegenpartij of overdracht in de overeenkomst.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

📖 Fiscaal voor verkoper: meerwaarde op de overgedragen activa belast als beroepsinkomen (in PB) of in VenB tegen 25% — meestal hoger dan share-deal. Voor koper: aankoopprijs verdeeld over de overgenomen activa op basis van marktwaarde — goodwill is afschrijfbaar (typisch 10 jaar of conform economische gebruiksduur). Btw: in principe btw op de prijs, maar art. 11 Wbtw stelt vrij van btw bij overdracht van een 'algemeenheid van goederen' of 'bedrijfsafdeling', mits het kopende vennootschap btw-plichtig is en de overdracht ervan zo wordt voortgezet.

<small>📚 Wbtw — art. 11 — _wettekst_ · KB nr. 1 — art. 11 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Vergelijking share-deal versus asset-deal  
_`kader` (subconcept)_

#### Substantie

🔗 De keuze tussen share-deal en asset-deal is meestal het resultaat van een fiscale onderhandeling tussen koper (asset-voorkeur) en verkoper (share-voorkeur).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

**Weergave** `vergelijkingstabel`:

```json
{
  "titel": "Share-deal versus asset-deal — vergelijkingsmatrix",
  "kolommen": [
    "Aspect",
    "Share-deal",
    "Asset-deal"
  ],
  "rijen": [
    [
      "Voorwerp",
      "Aandelen van de vennootschap",
      "Activa, contracten, goodwill"
    ],
    [
      "Wat blijft bij verkoper?",
      "Niets (volledige verkoop) of restant-aandeel",
      "De juridische schil + niet-overgedragen passiva"
    ],
    [
      "Schulden",
      "Mee over naar koper (in de venn.)",
      "Blijven bij verkoper (tenzij expliciet overgenomen)"
    ],
    [
      "Contracten",
      "Lopen door (mits geen change-of-control-clausule)",
      "Vergen instemming tegenpartij voor overdracht"
    ],
    [
      "Vergunningen",
      "Behouden (mits persoonsgebonden)",
      "Mogelijk opnieuw aan te vragen"
    ],
    [
      "Personeel",
      "Geen specifieke overdracht — blijft in de vennootschap",
      "CAO 32bis: gaat over met behoud anciënniteit en voorwaarden"
    ],
    [
      "Verkoper-fiscaal",
      "Meerwaarde aandelen typisch vrijgesteld (VenB art. 192, PB art. 90 9°)",
      "Meerwaarde op activa volledig belast (VenB 25%, of verlaagd tarief PB)"
    ],
    [
      "Koper-fiscaal",
      "Aandelen niet afschrijfbaar",
      "Activa + goodwill afschrijfbaar"
    ],
    [
      "Btw",
      "Geen btw",
      "In principe btw, maar art. 11 Wbtw stelt overdracht algemeenheid vrij"
    ],
    [
      "Due diligence",
      "Diepgaand — alle historische risico's reizen mee",
      "Beperkter — alleen overgedragen activa relevant"
    ],
    [
      "Garanties (R&W)",
      "Uitvoerig pakket vereist",
      "Beperkter — koper kan zelf nakijken wat hij koopt"
    ],
    [
      "Snelheid",
      "Eenvoudig (notariele/onderhandse akte voor aandelen)",
      "Trager (per actief vaak aparte stappen)"
    ]
  ]
}
```

### 📦 Due diligence — boekenonderzoek voorafgaand aan transactie  
_`procedure` (subconcept)_

#### Definitie

🤖 Onderzoek door de koper (of zijn adviseurs) van de financiele, fiscale, juridische en operationele situatie van de doelvennootschap, voorafgaand aan ondertekening van de overeenkomst. Het doel: identificeren van risico's, valoriseren van de doel, en formuleren van garanties en vrijwaringen in de SPA. Typische dimensies: financieel (boekhoudkundige juistheid, EBITDA-normalisatie), fiscaal (latente claims, niet-aangegeven verschuldigde belastingen), juridisch (lopende geschillen, contractuele change-of-control-clausules), commercieel (klantenconcentratie, marktrisico), operationeel (key persons, IT-systemen).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Garanties en vrijwaring (R&W + indemnification)  
_`instrument` (subconcept)_

#### Definitie

🤖 Contractuele bepalingen in de SPA waarmee de verkoper zich engageert dat bepaalde uitspraken over de doelvennootschap juist zijn (Representations & Warranties — R&W) en dat hij voor bepaalde risico's of onbekende schulden zal opdraaien (vrijwaring / indemnification). Bij schending: schadevergoeding aan koper, vaak met cap (maximum), basket (drempel), survival (tijdsbeperking) en mechanisme (escrow op de prijs, of W&I-verzekering).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Latente belastingen niet meerekenen in share-deal-prijs

**Verkeerde assumptie**: De netto-actiefwaarde uit de balans = de waarde van de aandelen.

**Kernpunt**: Bij share-deal nemen koper alle latente belastingen mee (bv. op latente meerwaarden, herwaarderingsmeerwaarden, vrijgestelde reserves bij latere uitkering). Een correcte aandelenwaardering houdt rekening met deze 'latente belastingschuld' — vaak via discounted future tax-modellering of door een afslag op de aankoopprijs.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Btw-vrijstelling art. 11 Wbtw toepassen waar niet aan de voorwaarden voldaan

**Verkeerde assumptie**: Elke asset-deal valt onder art. 11 Wbtw en is vrij van btw.

**Kernpunt**: Art. 11 Wbtw vereist (a) overdracht van een 'algemeenheid van goederen' of een 'bedrijfsafdeling' — dus een functioneel geheel dat zelfstandig kan worden uitgebaat, (b) de overnemer is btw-plichtig en (c) zet de activiteit voort. Een verkoop van losse activa zonder dat ze samen een bedrijfsafdeling vormen valt NIET onder art. 11 en is btw-plichtig. De fiscale impact (21% btw op alle activa) kan aanzienlijk zijn.

<small>📚 Wbtw — art. 11 — _wettekst_ · KB nr. 1 — art. 11 — _kb_</small>

### ⚠️ Personeels-overdracht vergeten bij asset-deal

**Verkeerde assumptie**: Bij asset-deal kan de koper kiezen welk personeel mee overgaat.

**Kernpunt**: CAO 32bis dwingt af dat alle werknemers van de overgedragen onderneming/afdeling mee overgaan met behoud van anciënniteit en arbeidsvoorwaarden. De koper kan dus niet selectief 'cherry-picken'. Ontslag in de context van overdracht is bovendien strikt beperkt — overtredingen leiden tot zware schadevergoedingen.

<small>📚 CAO 32bis (overdracht onderneming) — art. 7 + art. 9 — _norm_</small>

### ⚠️ Change-of-control-clausules over het hoofd zien bij share-deal

**Verkeerde assumptie**: Bij share-deal gaan alle contracten automatisch en zonder problemen door.

**Kernpunt**: Veel contracten (bankleningen, klantcontracten, vergunningen, intuitu personae-contracten) bevatten 'change-of-control'-clausules: bij wijziging van controle kan de tegenpartij het contract opzeggen of nieuwe voorwaarden bedingen. Due diligence moet deze clausules in kaart brengen — sommige vergen pre-closing-instemming.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Speelruimtes

### 🎚️ Share-deal versus asset-deal — onderhandelingsruimte

## Accountant-perspectieven

### Accountant als adviseur bij overdracht

_Bij M&A-transacties wordt de gecertificeerd accountant typisch ingeschakeld voor financiele due diligence, waardering en fiscale structurering._

#### 🧭 Adviseur

##### 👣 Financial due diligence  
_`stap`_

**Substantie**: 🤖 Stap 1: review van de jaarrekeningen van de laatste 3-5 jaar. Stap 2: EBITDA-normalisatie (correctie voor niet-recurrente posten, eigenaar-gebonden lasten). Stap 3: analyse working-capital-cyclus en debt-positie. Stap 4: identificatie quality-of-earnings issues (timing van revenue, kostenverschuivingen). Stap 5: opmaken DD-rapport voor de koper met geidentificeerde risico's en aanbevolen garanties.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 Fiscale structurerings-advies  
_`stap`_

**Substantie**: 🤖 Modelleer de gecombineerde fiscale impact voor verkoper en koper onder beide scenario's (share-deal en asset-deal). Bepaal de 'fiscale wig' — het bedrag dat fiscaal niet betaald wordt onder share-deal versus asset-deal. Adviseer over de optimale verdeling van die wig in de prijsonderhandeling. Overweeg alternatieven: inbreng-bedrijfstak gevolgd door verkoop van aandelen, gefaseerde overdracht, ruling-aanvraag bij DVB.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Overnameovereenkomst-SPA als contractueel instrument → [[overnameovereenkomst-spa]] _(moet-verwijzen)_
- → Aandeel — object van share-deal → [[aandeel]] _(moet-verwijzen)_
- → Inbreng-bedrijfstak-of-algemeenheid — alternatieve structurering → [[inbreng-bedrijfstak-of-algemeenheid]] _(moet-verwijzen)_
- → Aandeelhoudersovereenkomsten — pre-overdracht-context → [[aandeelhoudersovereenkomsten]] _(moet-verwijzen)_
- → Reorganisatie-Sigma — alternatieve herstructurerings-route → [[reorganisatie]] _(moet-verwijzen)_
- ↪ Meerwaarde-aandelen VenB — verkoperskant → [[meerwaarde-aandelen-venb]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ vennootschapsrecht
### `vereist`
- [[overnameovereenkomst-spa]]
### `vergelijkbaar_met`
- [[reorganisatie]] — Beide brengen activiteiten over, maar reorganisatie wijzigt de juridische structuur (WVV boek 12) terwijl overdracht een gewone contractuele transactie is.
    - **Gelijkenissen**:
        - Beide brengen activiteiten of waarde over van A naar B
        - Beide vergen due diligence en correcte waardering
    - **Verschillen**:
        - Reorganisatie: structuur-wijziging (fusie/splitsing/inbreng) met universele rechtsopvolging via WVV boek 12; overdracht: contractuele transactie (SPA/APA)
        - Reorganisatie: fiscale neutraliteit mogelijk (art. 211 WIB92); overdracht: typisch realisatie van meerwaarden
- [[inbreng-bedrijfstak-of-algemeenheid]] — Alternatief voor asset-deal: in plaats van een handelsfonds te verkopen kan het worden ingebracht in een nieuwe vennootschap waarvan dan de aandelen worden verkocht (= structurering).
    - **Gelijkenissen**:
        - Beide laten een operationele eenheid (bedrijfstak / handelsfonds) overgaan
        - Beide vergen identificatie van activa, passiva en contracten
    - **Verschillen**:
        - Inbreng: fiscale neutraliteit (art. 46 WIB92) + universele rechtsopvolging; overdracht: typisch realisatie + individuele overdracht
        - Inbreng: aandelen blijven bij inbrenger; overdracht: cash naar verkoper
### `beinvloed_door`
- [[aandeelhoudersovereenkomsten]]
