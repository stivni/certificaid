---
title: "Gerechtelijke reorganisatie"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.X
  - 3.0.X.B
  - 3.0.X.C
  - 3.0.X.D
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/gerechtelijke-reorganisatie.json"
---

# Gerechtelijke reorganisatie

_Procedure_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.X` · `3.0.X.B` · `3.0.X.C` · `3.0.X.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: GR — **Synoniemen**: wet continuïteit ondernemingen · WCO (oud) · réorganisation judiciaire

## Definitie

📖 De gerechtelijke reorganisatie (GR) is een gerechtelijke procedure binnen boek XX van het Wetboek van Economisch Recht (WER) die de continuïteit van een onderneming in moeilijkheden beoogt. Tijdens een wettelijke 'opschorting' (initiële maximumduur: 4 maanden, verlengbaar tot 12 maanden) worden uitvoeringsmaatregelen van schuldeisers tijdelijk geneutraliseerd, zodat de schuldenaar ruimte krijgt om een herstelplan uit te werken. De wet biedt drie modaliteiten als uitkomst: een minnelijk (individueel) akkoord met geselecteerde schuldeisers, een collectief akkoord dat alle schuldeisers bindt na homologatie, of een overdracht van het geheel of een deel van de onderneming onder gerechtelijk gezag.

<small>📚 WER — art. XX.39 e.v. — _wettekst_ · WER — art. XX.41 § 1 — _wettekst_ · WER — art. XX.84-86 (drie modaliteiten) — _wettekst_</small>

## Substantie

🔗 Voor de onderneming is GR een tijdsbuffer onder rechterlijk toezicht. Tijdens de opschorting blijft het bestuur normaal verder werken (geen curator-overname), maar wel onder controle van een gedelegeerd rechter. Lopende contracten blijven gelden, leveranciers en banken kunnen niet meer eenzijdig opzeggen wegens betalingsachterstand vóór de opschorting (art. XX.59/1). Voor de accountant is GR vaak de eerste-keuze-route: ze laat ruimte om de onderneming te restructureren, schulden te kwijtschelden via plan, of een onderdeel te verkopen — alles zonder de stigmatiserende werking van een faillissement.

<small>📚 WER — art. XX.59/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 GR vertaalt het EU-'tweede-kans'-principe (richtlijn 2019/1023): vroegtijdige restructurering levert meer waarde voor schuldeisers dan een eind-faillissement. De 2023-hervorming voegde een 'besloten' (vertrouwelijke) variant toe — zonder bekendmaking — voor ondernemingen die hun klantenrelatie willen beschermen. Categorisering van schuldeisers en 'cross-class cram-down' (art. XX.83/18) zorgen ervoor dat een minderheid van schuldeisers niet meer een herstelbaar plan kan blokkeren.

<small>📚 WER — W 2023-06-07/07, omzetting richtlijn 2019/1023 — _wettekst_ · WER — art. XX.83/18 (cross-class cram-down) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2018-05-01** · basis: WER boek XX, titel V (W 11-08-2017, ingrijpend uitgebreid W 7-06-2023 — invoering besloten variant + categorisering schuldeisers)

**✅ Voor**
- 📖 Ondernemingen waarvan de continuïteit onmiddellijk of op termijn bedreigd is — maar waar herstel via plan of overdracht nog realistisch lijkt.

**🚫 Niet voor**
- 📖 Ondernemingen waar de toestand zo grondig verloren is dat geen redelijk vooruitzicht op herstel meer bestaat — daar wijst de rechter de homologatie van het reorganisatieplan af (art. XX.83/17 § 2) en faillissement is aangewezen.

**▶️ Trigger start**
- 📖 Schuldenaar dient verzoekschrift in bij de ondernemingsrechtbank (art. XX.41), met als verplichte bijlagen: 2 recentste jaarrekeningen, boekhoudkundige staat actief/passief + resultatenrekening niet ouder dan 3 maanden (bijgestaan door gecertificeerd accountant of bedrijfsrevisor), begroting voor de duur van de opschorting, schuldeiserslijst.

**⏹ Trigger einde**
- 📖 Drie mogelijke uitkomsten: (1) homologatievonnis dat het plan goedkeurt — procedure wordt afgesloten (art. XX.83/38); (2) overdracht onder gerechtelijk gezag uitgevoerd; (3) beëindiging zonder slagen → vaak omslag naar faillissement (art. XX.69).

**👍 Voordeel**
- 🔗 Continuïteit blijft mogelijk; bestuur blijft aan boord; lopende contracten blijven gelden; gunstige fiscale en sociale behandeling (geen verbeurdverklaring openstaande verliezen).

**⚠️ Risico**
- 📖 Tijd is een vijand: opschorting is initieel 4 maanden (verlengbaar tot 12). Slaagt het plan niet binnen die termijn, dan kantelt de procedure typisch naar faillissement (art. XX.69), met retroactieve datum van staking van betaling — wat het risico van bestuurdersaansprakelijkheid vergroot.

## Sub-concepten

### 📦 Modaliteit 1 — Individueel (minnelijk) akkoord  
_`regime` (subconcept)_

#### Definitie

📖 De schuldenaar onderhandelt onder rechterlijk toezicht een minnelijk akkoord met **één of meer geselecteerde schuldeisers** (art. XX.84 + XX.83/30). Andere schuldeisers worden niet gebonden. Het akkoord wordt door de ondernemingsrechtbank gehomologeerd, krijgt uitvoerbare kracht en — belangrijk — de erbij betrokken schuldeisers genieten een immuniteit: het minnelijk akkoord en de handelingen ter uitvoering ervan zijn niet onderworpen aan een latere actio pauliana (art. XX.83/30 § 2).

<small>📚 WER — art. XX.84 — _wettekst_ · WER — art. XX.83/30 § 2-3 — _wettekst_</small>

#### Substantie

🔗 Praktisch: ideaal voor situaties met enkele grote schuldeisers (bv. bank + één hoofdleverancier) waar onderhandelen voldoende oplossing biedt. Snel, vertrouwelijk, en zonder dat alle kleine schuldeisers moeten meebeslissen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Modaliteit 2 — Collectief akkoord  
_`regime` (subconcept)_

#### Definitie

📖 De schuldenaar legt een reorganisatieplan voor dat **alle schuldeisers in de opschorting** bindt na stemming en homologatie (art. XX.83 e.v.). Sinds 2023 onderscheidt de wet twee regimes: een 'KMO'-regime voor kleine en middelgrote ondernemingen (eenvoudige meerderheid van schuldeisers vertegenwoordigend de helft van de schulden) en een 'grote-ondernemingen'-regime met indeling in schuldeiserscategorieën en mogelijke 'cross-class cram-down' (art. XX.83/18) — een instemmende categorie kan een niet-instemmende overrulen mits bescherming van het belang van de niet-instemmende schuldeisers.

<small>📚 WER — art. XX.83/14 (stemming) — _wettekst_ · WER — art. XX.83/17 (homologatie-criteria) — _wettekst_ · WER — art. XX.83/18 (cross-class cram-down) — _wettekst_</small>

#### Substantie

🔗 Het plan kan kwijtschelding van schuld bevatten (vaak tot 80% van gewone schuldvorderingen), gespreide afbetaling, omzetting in aandelen, of een combinatie. Fiscale en sociale schuldeisers genieten bijzondere bescherming: hun schulden mogen worden gespreid maar niet kwijtgescholden tenzij de wettelijke voorwaarden voldaan zijn.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Modaliteit 3 — Overdracht onder gerechtelijk gezag  
_`regime` (subconcept)_

#### Definitie

📖 Het geheel of een deel van de onderneming wordt onder rechterlijk toezicht verkocht aan een derde (art. XX.86 + XX.84). Een gerechtsmandataris organiseert de verkoop via offertes; de meest gunstige (qua prijs en behoud van werkgelegenheid) wordt geselecteerd en de rechtbank homologeert. Schuldeisers worden uitbetaald uit de verkoopopbrengst volgens rangorde — niet uit de overgenomen onderneming, die schuldenvrij overgaat. Dit is een hybride tussen reorganisatie (continuïteit van de activiteit) en faillissement (vereffening van het oude juridische omhulsel).

<small>📚 WER — art. XX.86 — _wettekst_ · WER — art. XX.84 — _wettekst_</small>

#### Rationale

🔗 Voor onhoudbaar verlieslatende ondernemingen die wel rendabele onderdelen bevatten: deze modaliteit redt de banen en de going-concern-waarde, terwijl de schuldenpost achterblijft bij het oude juridische omhulsel dat vereffend wordt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Besloten vs openbare gerechtelijke reorganisatie  
_`kader` (subconcept)_

#### Definitie

📖 Sinds de 2023-hervorming bestaan twee varianten: (a) **openbare GR** — bekendgemaakt in het Belgisch Staatsblad en Regsol; (b) **besloten GR** (art. XX.83/22 e.v.) — vertrouwelijk; alleen de schuldenaar en geselecteerde schuldeisers weten ervan; de rechtbank stelt een herstructureringsdeskundige aan. De besloten variant is bedoeld voor ondernemingen waar publieke bekendmaking de cliëntrelatie of het marktimago zou schaden (bv. dienstverlenende bedrijven, B2B-merken).

<small>📚 WER — art. XX.83/22 e.v. — _wettekst_</small>

## Bouwstenen

### ⚙️ Opschorting van uitvoeringsmaatregelen  
_`mechanisme`_

📖 Vanaf het openings-vonnis kunnen schuldeisers geen beslag meer leggen, dagvaardingen tot betaling lopen niet door, en bestaande beslagen worden geschorst. De schuldenaar mag wel betalen, maar selectieve betalingen kunnen aansprakelijkheidsrisico's voor het bestuur opleveren. Lopende contracten kunnen niet eenzijdig worden opgezegd wegens vroeger ontstane wanbetaling (art. XX.59/1).

<small>📚 WER — art. XX.49 (algemene opschorting) — _wettekst_ · WER — art. XX.59/1 (lopende contracten) — _wettekst_ · WER — art. XX.83/9 (besloten variant) — _wettekst_</small>

### 📏 Termijn opschorting: 4 maanden, verlengbaar tot 12 maanden  
_`drempel`_

📖 De initiële opschortingstermijn is maximaal 4 maanden (art. XX.46). Op gemotiveerd verzoek kan de rechtbank verlengen, maar nooit langer dan totaal 12 maanden vanaf het openingsvonnis. Daarna moet de procedure zijn afgesloten — door homologatie, overdracht of beëindiging.

<small>📚 WER — art. XX.46 — _wettekst_ · WER — art. XX.73 — _wettekst_</small>

### 💡 Gedelegeerd rechter — toezichthouder  
_`begrip`_

📖 Bij de openingsbeslissing stelt de rechtbank een 'gedelegeerd rechter' aan die toeziet op het verloop van de procedure, verslag uitbrengt aan de rechtbank en beslissingen voorbereidt over verlenging, betwistingen en het reorganisatieplan. Het bestuur blijft echter aan boord — de gedelegeerd rechter is geen curator, hij vervangt het bestuur niet.

<small>📚 WER — art. XX.39 (aanstelling) — _wettekst_</small>

### 📜 Homologatie-criteria voor reorganisatieplan  
_`regel`_

📖 De rechtbank homologeert een collectief plan alleen als (art. XX.83/17): (1) het plan is correct aangenomen door de schuldeisers; (2) de indeling in categorieën is correct gebeurd; (3) de neerlegging is gedaan; (4) niet-instemmende schuldeisers krijgen ten minste evenveel als bij faillissement zouden krijgen ('belang-van-de-schuldeisers-toets'); (5) eventuele nieuwe financiering is noodzakelijk en niet overmatig benadelend. Bovendien moet het plan redelijk vooruitzicht bieden op afwenden van faillissement of vereffening (§ 2). De rechtbank kan geen voorwaarden toevoegen die niet in het plan staan.

<small>📚 WER — art. XX.83/17 § 1-4 — _wettekst_</small>

## Voorbeelden

### 💡 Tijdslijn collectieve gerechtelijke reorganisatie — Aurelia Industrie BV 🔗

_Aurelia Industrie BV heeft 4 miljoen EUR schulden waarvan 2 miljoen aan banken en 1,5 miljoen aan handelsleveranciers. De onderneming is rendabel maar onderkapitaliseerd na een mislukte expansie._

**Weergave** `tijdslijn`:

```json
{
  "tekst": "Dag 0: Verzoekschrift met balans <3 maanden + begroting + schuldeiserslijst (art. XX.41)\nDag 14: Openingsvonnis → opschorting 4 maanden + gedelegeerd rechter aangesteld\nMaand 1-2: Onderhandelen met schuldeiserscategorieën (banken, leveranciers, RSZ/btw, achtergesteld)\nMaand 3: Neerlegging reorganisatieplan (kwijtschelding 70% gewone schuld + spreiding fiscale schuld over 5 jaar)\nMaand 4: Stemming door schuldeiserscategorieën\nMaand 4: Homologatievonnis (art. XX.83/17)\nMaand 4+: Plan-uitvoering onder toezicht herstructureringsdeskundige"
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Verlatenheid — de zwarte kant van GR

**Verkeerde assumptie**: Tijdens GR is de bestuurder beschermd tegen aansprakelijkheid omdat de rechtbank toeziet.

**Kernpunt**: Het bestuur blijft volledig verantwoordelijk. Indien de bestuurder de zaak laat verloederen of selectief grote schuldeisers betaalt ten koste van anderen, blijft hij blootgesteld aan bestuurdersaansprakelijkheid (gemeenrechtelijk + art. XX.225-226 bij latere omslag naar faillissement). 'Verlatenheid' (laisser-faire) tijdens de opschorting versnelt eerder dan vertraagt het aansprakelijkheidsrisico.

<small>📚 WER — art. XX.225 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ GR ≠ WVV-reorganisatie

**Verkeerde assumptie**: Een 'gerechtelijke reorganisatie' is hetzelfde als een 'reorganisatie' in de zin van het WVV boek 12 (fusie/splitsing).

**Kernpunt**: Twee totaal verschillende juridische concepten: GR (WER boek XX) is een procedure bij dreigende insolventie. WVV-reorganisatie (boek 12) is een vrijwillige herstructurering tussen gezonde vennootschappen (fusie, splitsing, inbreng van bedrijfstak). Lees in een examenvraag goed welke context bedoeld wordt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Plan zonder vooruitzicht wordt niet gehomologeerd

**Verkeerde assumptie**: Als de schuldeisers het plan goedkeuren, homologeert de rechter automatisch.

**Kernpunt**: Art. XX.83/17 § 2 geeft de rechter een eigen 'gezond verstand'-toets: als hij meent dat het plan geen redelijk vooruitzicht biedt op herstel, weigert hij — ook bij positieve stemming. Een goed plan moet operationele én financiële herstel-paden tonen, niet alleen schuldkwijtschelding.

<small>📚 WER — art. XX.83/17 § 2 — _wettekst_</small>

## Speelruimtes

### 🎚️ Keuze tussen drie modaliteiten

## Accountant-perspectieven

### Cliënt overweegt gerechtelijke reorganisatie

#### 🧭 Adviseur

##### 👣 Haalbaarheid toetsen vóór verzoekschrift  
_`stap`_

🔗 Maak een 13-weekse cashflow-projectie: kan de onderneming tijdens de 4-maanden-opschorting haar lopende lasten betalen (lonen, lopende huur, leveranciers vanaf nul) zonder externe injectie? Zo niet, dan is GR voortijdig — eerst herfinanciering zoeken of meteen faillissement aanvragen.

<small>📚 WER — art. XX.41 § 2, 6° (begroting opschorting verplicht) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Modaliteit kiezen op basis van schuldeisersstructuur  
_`stap`_

🔗 Schuldeisersmix analyseren: weinig grote crediteuren + onderhandelbaar → individueel akkoord. Veel kleine schuldeisers + kwijtscheldingsbehoefte → collectief. Niet-rendabele onderneming maar rendabele onderdelen → overdracht.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boekhoudkundige staat + begroting opmaken voor verzoekschrift  
_`stap`_

📖 Verplichte bijlagen bij verzoekschrift (art. XX.41 § 2, 5° + 6°): boekhoudkundige staat actief/passief + resultatenrekening niet ouder dan 3 maanden, en begroting voor de duur van de opschorting. Beide opgesteld met bijstand van gecertificeerd accountant, accountant, fiscaal accountant of bedrijfsrevisor. De begroting moet de Commissie-voor-Boekhoudkundige-Normen-modellen volgen indien voorhanden.

<small>📚 WER — art. XX.41 § 2, 5° + 6° — _wettekst_</small>

## Verder lezen (scope-out)

- → Parent kader — WER boek XX → [[insolventierecht-wer-boek-xx]] _(moet-verwijzen)_
- → Faillissement als alternatieve uitkomst → [[faillissement]] _(moet-verwijzen)_
- → Bestuurdersaansprakelijkheid bij verlatenheid → [[bestuurdersaansprakelijkheid]] _(moet-verwijzen)_
- ✂ Reorganisatie (WVV boek 12) — verwante naam maar conceptueel verschillend (vrijwillig vs insolventie-context)

## Relaties

### `valt_onder`
- [[insolventierecht-wer-boek-xx]]
### `vergelijkbaar_met`
- [[faillissement]]
    - **Gelijkenissen**:
        - Beide WER boek XX-procedures
        - Beide onder ondernemingsrechtbank
    - **Verschillen**:
        - GR zoekt continuïteit; faillissement vereffent
        - GR laat bestuur aan boord; faillissement plaatst curator
        - GR is tijdelijk (max 12 maanden); faillissement loopt tot sluiting
### `triggert`
- [[bestuurdersaansprakelijkheid]]
