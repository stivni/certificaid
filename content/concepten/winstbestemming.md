---
title: "Winstbestemming"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.IV.B
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/winstbestemming.json"
---

# Winstbestemming

_Verrichting_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.IV.B` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: resultaatverwerking · winstverdeling-besluit · winstbestemmings-besluit

## Definitie

📖 Winstbestemming (ook 'resultaatverwerking') is het besluit van de algemene vergadering, genomen samen met de goedkeuring van de jaarrekening, over wat er met de boekhoudkundige nettowinst van het boekjaar gebeurt. Het besluit verdeelt de nettowinst (vermeerderd met het overgedragen resultaat uit voorgaande boekjaren) over vier bestemmingen: (1) wettelijke reserve, (2) andere reserves (statutair onbeschikbaar of vrijwillig), (3) tantieme aan bestuurders en dividend aan aandeelhouders, en (4) overdracht naar volgend boekjaar. De volgorde en grenzen worden bepaald door het WVV (kapitaalbescherming) en eventueel door de statuten van de vennootschap.

<small>📚 WVV — art. 7:196 (uitkeerbare winsten) — _wettekst_ · WVV — art. 7:197 (verplichte wettelijke reserve NV) — _wettekst_ · CBN-advies 2016/15 — boekingen resultaatverwerking — _advies_</small>

## Substantie

📖 Boekhoudkundig gebeurt de winstbestemming in een aparte rekening-reeks (klasse 69 — resultaatverwerking) die LOSSTAAT van het bedrijfsresultaat. Vergelijk: rekening 618 'Bezoldigingen, premies' (klasse 6) is een gewone bedrijfskost die het bedrijfsresultaat verlaagt; rekening 695 'Bestuurders of zaakvoerders' (klasse 69) verlaagt het bedrijfsresultaat NIET maar bestemt een deel van de winst. Hetzelfde geldt voor dotaties aan reserves (rekening 691-694): geen kost van het boekjaar, maar bestemming. Deze scheiding is geen rubricering-detail — ze respecteert het fundamenteel onderscheid tussen 'kosten' (verbruik tijdens het boekjaar) en 'winstbestemming' (verdeling achteraf).

<small>📚 CBN-advies 2016/15 — klasse 69 versus klasse 6 — _advies_ · KB WVV — art. 3:82 e.v. (resultatenrekening structuur) — _kb_</small>

## Rationale

🔗 De winstbestemming is het scharniermoment van het boekjaar — hier wordt beslist of de winst in de vennootschap blijft (reservering, overdracht) of eruit gaat (tantieme, dividend). Het is ook hier dat de wettelijke beschermingsmechanismen worden geactiveerd: verplichte wettelijke reserve voor NV (een vorm van 'gedwongen sparen' tot 10% kapitaal), check op uitkeerbare winsten, naleving van statutair onbeschikbare reserves. Voor de stagiair: dit is hét moment waar boekhoud, vennootschapsrecht en fiscaal recht samenkomen in een AV-besluit.

<small>📚 WVV — art. 7:197 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV art. 7:196-197 (NV) + art. 5:142-143 (BV); KB WVV art. 3:82 e.v.

**📋 Voorwaarden**
- 📖 Voorafgaande goedkeuring van de jaarrekening door de algemene vergadering — winstbestemming is een aansluitend besluit op die goedkeuring.
- 📖 Voor NV: verplichte aanleg wettelijke reserve van 5% van de nettowinst tot 10% van het kapitaal is bereikt (art. 7:197 WVV). Voor BV: geen verplichte wettelijke reserve (kapitaalloos in BV vanaf WVV).
- 📖 Tantieme- en dividend-toekenningen moeten passen binnen de uitkeerbare winsten (netto-actief-test in NV; netto-actief- en liquiditeitstest in BV).

## Sub-concepten

### 📦 Wettelijke volgorde van winstbestemming  
_`kader` (subconcept)_

#### Definitie

📖 De winstbestemming volgt een verplichte volgorde: (1) eerst aanvullen van overgedragen verlies (negatief openingssaldo); (2) wettelijke reserve (5% tot 10% kapitaal — NV); (3) statutair voorgeschreven dotaties (onbeschikbare statutaire reserves); (4) tantieme en dividend (in volgorde bepaald door statuten); (5) restant naar overgedragen resultaat. De volgorde mag niet worden omgekeerd: een dividend kan pas worden uitgekeerd nadat de wettelijke en statutaire dotaties zijn voldaan.

<small>📚 WVV — art. 7:197 — _wettekst_ · KB WVV — art. 3:175 (winstverdeling tabel) — _kb_</small>

### 📦 Wettelijke reserve (NV)  
_`balanspost` (subconcept)_

#### Definitie

📖 Een onbeschikbare reserve die de NV jaarlijks moet aanleggen door minstens 5% van de nettowinst van het boekjaar over te boeken naar deze reserve, tot deze reserve 10% van het kapitaal bereikt heeft (art. 7:197 WVV). Eens 10% bereikt: aanleg niet meer verplicht. Deze reserve is onbeschikbaar voor uitkering — ze beschermt schuldeisers tegen volledige uitkering van het kapitaal. Voor BV bestaat deze verplichting niet (BV is kapitaalloos sinds WVV; de wettelijke reserve uit een BVBA werd omgevormd naar onbeschikbare inbreng of vrije reserve — CBN 2019/14).

<small>📚 WVV — art. 7:197 — _wettekst_ · CBN-advies 2019/14 — omvorming wettelijke reserve BVBA-naar-BV — _advies_</small>

### 📦 Vrije en statutaire reserves  
_`balanspost` (subconcept)_

#### Definitie

🔗 Statutaire reserves: door de statuten verplichte dotaties (statutair onbeschikbaar). Vrije reserves: vrijwillige reservering door AV-besluit — kunnen later weer worden vrijgegeven voor uitkering of geactiveerd voor specifieke doelen (zoals liquidatiereserve, art. 184quater WIB92).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Overgedragen resultaat  
_`balanspost` (subconcept)_

#### Definitie

📖 Het saldo van de winst (of het verlies) dat niet werd bestemd voor reserves of uitkering, en dat dus wordt 'overgedragen' naar het volgend boekjaar. Op de balans rubriek 14 (overgedragen winst) of 14- (overgedragen verlies). Verschijnt bij opening van het volgend boekjaar als beginsaldo van het te bestemmen resultaat.

<small>📚 CBN-advies 2015/02 — boeking overgedragen winst — _advies_</small>

### 📦 Te bestemmen winstsaldo — berekening  
_`kader` (subconcept)_

#### Definitie

🔗 Te bestemmen winstsaldo = nettowinst van het boekjaar + overgedragen winst voorgaand boekjaar - overgedragen verlies voorgaand boekjaar. Op dit bedrag worden de bestemmings-besluiten genomen.

<small>📚 KB WVV — art. 3:175 (winstverdeling-schema) — _kb_</small>

## Bouwstenen

### 👣 Boekingen bij resultaatverwerking  
_`stap`_

**Substantie**: 📖 Klasse 69-rekeningen worden gebruikt voor de winstbestemming. Vergelijk klasse 6 (= bedrijfskost) versus klasse 69 (= winstbestemming).

<small>📚 CBN-advies 2016/15 — boekingen resultaatverwerking — _advies_</small>

| Rekening | Omschrijving | Tegenpost |
| --- | --- | --- |
| 691 | Toevoeging aan wettelijke reserve | 131 Wettelijke reserve |
| 692 | Toevoeging aan andere reserves | 133/14 Andere reserves |
| 693 | Overgedragen winst (debet) — saldo naar volgend boekjaar | 140 Overgedragen winst |
| 694 | Vergoeding van het kapitaal (dividend) | 471 Schuld aan aandeelhouders inzake dividenden |
| 695 | Bestuurders of zaakvoerders (tantieme) | 472 Tantiemes over het boekjaar |

## Voorbeelden

### 💡 Winstbestemming BV Optima — nettowinst 100.000 EUR 🔗

_BV Optima (NV-vorm, kapitaal 100.000 EUR, wettelijke reserve momenteel 6.000 EUR) sluit het boekjaar af met een nettowinst van 100.000 EUR. Overgedragen winst voorgaand: 20.000 EUR. AV beslist: maximumaanleg wettelijke reserve, tantieme zaakvoerder 15.000 EUR, dividend 60.000 EUR, rest overdragen._

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Volgorde van bestemming negeren

**Verkeerde assumptie**: AV kan vrij kiezen of ze eerst dividend, dan wettelijke reserve uitkeert.

**Kernpunt**: De volgorde is wettelijk: eerst wettelijke reserve (tot 10% kapitaal bereikt), dan statutaire dotaties, dan tantieme en dividend. Een dividend uitkeren zonder eerst de wettelijke reserve te dotteren is nietig en aanleiding tot bestuurdersaansprakelijkheid (en terugvordering bij aandeelhouders).

<small>📚 WVV — art. 7:197 — _wettekst_</small>

### ⚠️ Tantieme als bedrijfskost boeken (klasse 6 i.p.v. klasse 69)

**Verkeerde assumptie**: Tantieme is een bezoldiging, dus rekening 618.

**Kernpunt**: Tantieme is geen bedrijfskost van het boekjaar maar een winstbestemming. Boeking op rekening 695 (klasse 69) tegen 472 'Tantieme over het boekjaar' (CBN 2016/15). Boeking op 618 zou het bedrijfsresultaat verlagen en de winstbestemmings-volgorde verstoren.

<small>📚 CBN-advies 2016/15 — klasse 69 versus klasse 6 — _advies_</small>

### ⚠️ BV-wettelijke-reserve eisen onder WVV

**Verkeerde assumptie**: BV moet ook een wettelijke reserve aanleggen, zoals een NV.

**Kernpunt**: Onder WVV (sinds 2019) is de BV kapitaalloos en kent geen verplichte wettelijke reserve. Bestaande BVBA's met een wettelijke reserve omgevormd naar BV moeten die reserve omvormen — typisch naar onbeschikbare inbreng of vrije reserve (CBN 2019/14). Aanleg is niet meer verplicht.

<small>📚 CBN-advies 2019/14 — omvorming wettelijke reserve BVBA-BV — _advies_</small>

### ⚠️ Liquidatiereserve aanleg vergeten in winstbestemming

**Verkeerde assumptie**: Liquidatiereserve is een fiscaal mechanisme — alleen relevant bij de aangifte.

**Kernpunt**: De liquidatiereserve (art. 184quater WIB92) wordt boekhoudkundig aangelegd in de winstbestemming, vóór dividend en overdracht. Het bedrag wordt geboekt op rekening 132 'Belastingvrije reserves' tegen 692. Vergeet dit niet — de 10% afzonderlijke aanslag VenB wordt verschuldigd over het bedrag dat in de jaarrekening als liquidatiereserve is opgenomen (CBN 2015/06).

<small>📚 CBN-advies 2015/06 — boekhoudkundige verwerking liquidatiereserve — _advies_</small>

## Speelruimtes

### 🎚️ Hoeveel van de winst uitkeren versus reserveren?

## Accountant-perspectieven

### Accountant als boekhouder bij winstbestemming

#### 📒 Boekhouder

##### 👣 Voorbereiden van het winstbestemmings-voorstel  
_`stap`_

**Substantie**: 📖 Stap 1: bereken te bestemmen saldo (nettowinst boekjaar + overgedragen winst - overgedragen verlies). Stap 2: bepaal verplichte wettelijke reserve (5% van nettowinst tot 10% kapitaal bij NV). Stap 3: identificeer statutaire dotaties (statuten nakijken). Stap 4: optimaliseer fiscaal: liquidatiereserve, tantieme voor KMO-tarief. Stap 5: stel het winstbestemmings-schema op zoals voorgeschreven door KB WVV. Stap 6: presenteer aan AV met bestuurdersverslag over uitkeerbare winsten (netto-actief-test + liquiditeitstest BV).

<small>📚 KB WVV — art. 3:175 — _kb_ · CBN-advies 2016/15 — boekingen resultaatverwerking — _advies_</small>

##### 👣 Boekingen na AV-besluit  
_`stap`_

**Substantie**: 📖 Na AV: boeking via klasse 69-rekeningen. Wettelijke reserve: 691 versus 131. Liquidatiereserve: 692 versus 132. Tantieme: 695 versus 472. Dividend: 694 versus 471 (met RV-inhouding: 471 versus 477). Saldo: 693 versus 140 (winst) of 141 (verlies). RV-aangifte (291.1 of vergelijkbaar) binnen 15 dagen na inhouding.

<small>📚 CBN-advies 2016/15 — rekeningplan klasse 69 — _advies_</small>

## Verder lezen (scope-out)

- → Winstuitkering-Sigma als parent-keuzekader → [[winstuitkering]] _(moet-verwijzen)_
- → Tantieme als afzonderlijk record → [[tantieme]] _(moet-verwijzen)_
- → Eigen vermogen — reserves als component → [[eigen-vermogen]] _(moet-verwijzen)_
- → Algemene vergadering — besluit → [[algemene-vergadering]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[winstuitkering]]
### `beinvloed_door`
- [[algemene-vergadering]]
### `triggert`
- [[eigen-vermogen]]
