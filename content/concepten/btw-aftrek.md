---
title: "BTW-aftrek"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.III
  - 2.4.IV
  - 2.4.VII
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-aftrek.json"
---

# BTW-aftrek

_Kader_

📋 Regeling · Anchors: `2.4.III` · `2.4.IV` · `2.4.VII` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: recht op aftrek · voorbelasting · aftrek voorbelasting

## Definitie

📖 Het recht op BTW-aftrek (art. 45 WBTW) is het basismechanisme dat ervoor zorgt dat BTW een belasting blijft op de eindverbruiker en niet op de schakels in de productieketen. Elke belastingplichtige mag van de BTW die hij aan zijn afnemers aanrekent (verschuldigde BTW), de BTW aftrekken die hij zelf heeft betaald op zijn aankopen (voorbelasting), in de mate dat die aankopen worden gebruikt voor zijn belaste uitgaande handelingen. Het saldo wordt afgerekend in de periodieke BTW-aangifte.

<small>📚 WBTW — art. 45 §1 — _wettekst_ · Richtlijn 2006/112/EG — art. 167-168 — _richtlijn_</small>

## Substantie

🔗 Zonder aftrek zou BTW cascade-belasting worden: elke schakel zou belasting betalen op het volledige bedrag inclusief de BTW van de vorige schakel. Met aftrek wordt enkel de toegevoegde waarde belast. De voorwaarden zijn drieërlei: (1) je moet belastingplichtige zijn (uitsluiting art. 44 = vrijstelling zonder aftrek); (2) de aankoop moet bestemd zijn voor belaste uitgaande handelingen (directe + onmiddellijke band); (3) je moet over een regelmatige factuur beschikken (KB nr. 3 art. 3). Bij gemengd gebruik (deels belast, deels vrijgesteld): pro-rata-aftrek.

<small>📚 WBTW — art. 45 §1 — _wettekst_ · KB nr. 3 — art. 3 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 Het BTW-stelsel berust op het beginsel van fiscale neutraliteit (Richtlijn 2006/112 art. 1.2): de belasting moet 'strikt evenredig zijn aan de prijs van de goederen en diensten, ongeacht het aantal handelingen vóór de heffing'. Het aftrekrecht realiseert die neutraliteit: hoeveel schakels er ook zijn, elke schakel betaalt enkel op de toegevoegde waarde. Daarom is het aftrekrecht een 'fundamenteel beginsel van het BTW-stelsel' (vaste rechtspraak Hof van Justitie).

<small>📚 Richtlijn 2006/112/EG — art. 1.2 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 45 + KB nr. 3 (basis 1969)

Het recht op aftrek is stabiel sinds invoering BTW (1971). Recente aanpassingen aan art. 45 §1, 3° met ingang van 01-01-2025 (W 21-03-2024) verfijnden de definitie van diensten die in aftrek mogen komen. De uitsluitingen art. 45 §3 (kosten van logies/spijzen/dranken, onthaal) zijn stabiel.

**📋 Voorwaarden**
- 📖 Drie cumulatieve voorwaarden om aftrek uit te oefenen: (1) materiële voorwaarde — directe + onmiddellijke band tussen de aankoop en een belaste uitgaande handeling (HvJ-rechtspraak BLP, Midland Bank); (2) tijdvoorwaarde — recht ontstaat op het tijdstip waarop de BTW opeisbaar wordt (art. 2 KB nr. 3); (3) formele voorwaarde — regelmatige factuur in bezit, met alle verplichte vermeldingen (art. 3 KB nr. 3).

## Sub-concepten

### 📦 Pro-rata bij gemengde belastingplichtige  
_`procedure` (subconcept)_

#### Definitie

📖 Een gemengde belastingplichtige verricht zowel belaste handelingen (met aftrek) als handelingen vrijgesteld zonder aftrek (art. 44 WBTW). Voorbeeld: een advocaat met BTW-plichtige diensten + medische adviezen (vrijgesteld). De aftrek wordt beperkt tot het deel dat overeenstemt met de belaste activiteit. Twee methodes: (1) algemeen verhoudingsgetal — één jaarbreuk omzet-met-aftrek / totale omzet × inkomende BTW; (2) werkelijk gebruik (= directe toerekening) — aankoop per aankoop bekijken: 100 % aftrek bij belaste activiteit, 0 % bij vrijgestelde, pro-rata bij gemengde aankoop.

<small>📚 WBTW — art. 46 — _wettekst_ · KB nr. 3 — art. 12-14 — _kb_ · Richtlijn 2006/112/EG — art. 173-175 — _richtlijn_</small>

#### Substantie

📖 Algemeen verhoudingsgetal is administratief eenvoudig maar grof (één breuk voor heel het bedrijf); werkelijk gebruik is precieser maar arbeidsintensief. Sinds 2018: keuze 'werkelijk gebruik' moet expliciet aangevraagd worden bij de fiscus via elektronische kennisgeving (vroeger: ambtshalve toestemming). De voorlopige aftrek voor het lopende jaar gebeurt op basis van het verhoudingsgetal van het voorgaande jaar; einde jaar = herziening op basis van werkelijke cijfers (art. 175 Richtlijn).

<small>📚 KB nr. 3 — art. 12-19 — _kb_ · Richtlijn 2006/112/EG — art. 175 — _richtlijn_</small>

#### 🧮 Algemeen verhoudingsgetal  
_`formule`_

📖 Verhoudingsgetal = (omzet handelingen met recht op aftrek) / (omzet alle handelingen). Op jaarbasis. Afgerond op hogere eenheid (art. 175 Richtlijn). Bij definitief 80 %: 80 % van inkomende BTW wordt afgetrokken.

<small>📚 Richtlijn 2006/112/EG — art. 174-175 — _richtlijn_</small>

### 📦 Uitsluitingen van aftrek (art. 45 §3 WBTW)  
_`regime` (subconcept)_

#### Definitie

📖 Bepaalde kosten zijn uitgesloten van aftrek (= 0 %) zelfs als ze gebruikt worden in de belaste activiteit. Belangrijkste categorieën: (1) tabaksfabricaten (1°); (2) kosten van geestrijke dranken niet bestemd voor wederverkoop (2°); (3) kosten van logies, spijzen en dranken (3°) — uitzondering voor personeelskosten 'op verplaatsing' en horeca-belastingplichtigen die de diensten doorverkopen; (4) kosten van onthaal (4°). Daarnaast: autokosten beperkt tot 50 % door art. 45 §2 (zie record btw-bedrijfswagen).

<small>📚 WBTW — art. 45 §3 — _wettekst_ · WBTW — art. 45 §3, 3°-4° — _wettekst_</small>

#### ↪️ Kosten van onthaal (4°)  
_`uitzondering`_

📖 Kosten gemaakt voor het 'onthaal' van klanten of zakenrelaties (recepties, feestjes, geschenken bij klantenbezoek) zijn 100 % uitgesloten van BTW-aftrek. Onderscheid met restaurantkosten op verplaatsing (3°) en publiciteitskosten (wel aftrekbaar): pure relatiekost = niet aftrekbaar.

<small>📚 WBTW — art. 45 §3, 4° — _wettekst_</small>

#### ↪️ Logies, spijzen en dranken (3°)  
_`uitzondering`_

📖 Kosten van logies, spijzen en dranken in de zin van art. 18 §1 lid 2, 10°-11° zijn niet aftrekbaar — TENZIJ: (a) personeel buiten de onderneming met levering of dienstverrichting (= 'op verplaatsing'); (b) belastingplichtige die zelf dezelfde diensten onder bezwarende titel verstrekt (= horeca-uitbater die zijn input recupereert).

<small>📚 WBTW — art. 45 §3, 3° — _wettekst_</small>

## Bouwstenen

### 📜 Tijdstip ontstaan aftrekrecht (art. 2 KB nr. 3)  
_`regel`_

📖 Het aftrekrecht ontstaat op hetzelfde moment als de BTW-opeisbaarheid bij de leverancier — gewoonlijk de factuurdatum of de leveringsdatum (art. 16-17 WBTW). Voor invoer-BTW: op het ogenblik dat de invoer-BTW opeisbaar wordt. Voor IC-verwervingen: op het moment van opeisbaarheid (art. 25sexies). Praktisch: in de aangifte van het tijdvak waarin de factuur valt.

<small>📚 KB nr. 3 — art. 2 — _kb_ · Richtlijn 2006/112/EG — art. 167 + art. 179 — _richtlijn_</small>

### 📜 Regelmatige factuur — formele voorwaarde  
_`regel`_

📖 Om aftrek uit te oefenen moet de belastingplichtige in het bezit zijn van een factuur die voldoet aan alle verplichte vermeldingen van art. 5 KB nr. 1 (naam + adres + BTW-nummer van beide partijen, datum, factuurnummer, beschrijving, maatstaf van heffing, tarief, bedrag BTW). Een onregelmatige factuur kan tot aftrekverlies leiden bij controle — al heeft HvJ in recente jaren tussen formele en materiële voorwaarden onderscheiden (substantieel recht primeert).

<small>📚 KB nr. 3 — art. 3 §1 — _kb_ · KB nr. 1 — art. 5 — _kb_</small>

### ✴️ Directe en onmiddellijke band  
_`principe`_

🔗 Vaste HvJ-rechtspraak (BLP, Midland Bank, Cibo): aftrek vereist een directe en onmiddellijke band tussen de aankoop en (a) een belaste uitgaande handeling, of (b) de algemene economische activiteit van de belastingplichtige (overheadkosten). Kosten die geen band hebben met economische activiteit (puur privé, niet-economische activiteiten) → géén aftrek. Voor gemengde activiteit → pro-rata.

<small>📚 Richtlijn 2006/112/EG — art. 168 — _richtlijn_ · HvJ — BLP Group, Midland Bank, Cibo Participations — _rechtspraak_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Handelaar — eenvoudige aftrek 🔗

_Zelena Bio NV koopt grondstoffen voor 10.000 EUR + 2.100 EUR BTW (21 %). Verkoopt afgewerkt product voor 15.000 EUR + 3.150 EUR BTW._

**Berekening:**
- Verschuldigde BTW verkopen (rooster 54): 3.150 EUR
- Aftrekbare BTW aankopen (rooster 59): 2.100 EUR
- Saldo rooster 71 te betalen: 3.150 − 2.100 = 1.050 EUR

→ **Resultaat**: Zelena betaalt netto 1.050 EUR BTW = 21 % op de toegevoegde waarde van 5.000 EUR. Boeking aftrek: D 411 'Terug te vorderen BTW' 2.100 / C 440 'Leverancier' 12.100.

<small>📚 WBTW — art. 45 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Gemengd advocatenkantoor — algemeen verhoudingsgetal 🔗

_Advocaat Aurelia heeft in 2025: belaste consultaties 200.000 EUR + vrijgestelde pro-Deo / sociale activiteit 50.000 EUR. Inkomende BTW op kantoorkosten en computers: 21.000 EUR._

**Berekening:**
- Verhoudingsgetal = 200.000 / (200.000 + 50.000) = 200.000 / 250.000 = 80 %
- Afgerond op hogere eenheid: 80 % (al heel)
- Aftrekbare BTW = 21.000 × 80 % = 16.800 EUR
- Niet-aftrekbare BTW (= kostprijs) = 21.000 × 20 % = 4.200 EUR

→ **Resultaat**: In rooster 59 komt 16.800 EUR. De resterende 4.200 EUR wordt geboekt als kostprijs (in de 6-klasse waar de aankoop hoort). Bij voorlopige aftrek volgens vorig jaar gebruikt Aurelia het VG van vorig jaar; einde jaar herziening op basis van werkelijke cijfers.

<small>📚 WBTW — art. 46 — _wettekst_ · Richtlijn 2006/112/EG — art. 175 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Receptiekosten — geen aftrek mogelijk 📖

_Aurelia Holding NV organiseert eindejaarsreceptie voor klanten: 5.000 EUR + 1.050 EUR BTW (21 %)._

**Berekening:**
- Stap 1 — kwalificatie: 'kosten van onthaal' (art. 45 §3, 4°)
- Stap 2 — uitsluiting van aftrek: 100 %
- Stap 3 — geen rooster 59-opname; volledige factuur 6.050 EUR wordt kostprijs
- Stap 4 — boekhoudkundige verwerking: D 615 'Diverse diensten' 6.050 (incl. BTW als kost)

→ **Resultaat**: Cumulatief: VenB beperking 50 % op netto (1207-code): 5.000 × 50 % = 2.500 EUR niet-aftrekbaar als beroepskost. De BTW (1.050) is volledig kost; de helft van het netto-bedrag is verworpen uitgave.

<small>📚 WBTW — art. 45 §3, 4° — _wettekst_ · WIB92 — art. 53, 8° — _wettekst_</small>

## Valkuilen

### ⚠️ Vergeten dat vrijstelling art. 44 = geen aftrek

**Verkeerde assumptie**: 'Belastingplichtige = automatisch aftrek.'

**Kernpunt**: Belastingplichtigen met vrijgestelde activiteit art. 44 (artsen, advocaten in bepaalde activiteiten, financiële sector, onderwijs) hebben GEEN recht op aftrek op de aankopen voor die activiteit. Hun BTW op aankopen is een kostprijs. Wie zowel belaste als vrijgestelde activiteit heeft → gemengde belastingplichtige → pro-rata.

<small>📚 WBTW — art. 44 — _wettekst_ · WBTW — art. 45 §1 — _wettekst_</small>

### ⚠️ Restaurantkost op verplaatsing als 'onthaal' kwalificeren

**Verkeerde assumptie**: Elk restaurantbezoek met klanten = uitgesloten van BTW-aftrek.

**Kernpunt**: Art. 45 §3, 3° sluit kosten van spijzen en dranken uit, MAAR uitzondering (a): kosten voor het personeel buiten de onderneming belast met levering of dienstverrichting. Dus: een monteur die op verplaatsing een broodje eet → 100 % aftrekbaar; eindejaarsreceptie voor klanten op kantoor → niet aftrekbaar (= onthaal 4°). Onderscheid scherp bewaken in boekhouding.

<small>📚 WBTW — art. 45 §3, 3° + 4° — _wettekst_</small>

### ⚠️ BTW-aftrek vorderen zonder regelmatige factuur

**Verkeerde assumptie**: Met een gewone kassabon of leveringsbon kan ik mijn BTW aftrekken.

**Kernpunt**: Voor BTW-aftrek > 250 EUR op B2B-aankopen is een regelmatige factuur vereist (KB nr. 1 art. 5). Een kassabon of vereenvoudigde factuur volstaat niet als alle verplichte vermeldingen ontbreken. Vraag aan elke leverancier om factuur. Wel: HvJ-rechtspraak nuanceert (substance over form) — maar in praktijk is een factuur altijd vereist tijdens controle.

<small>📚 KB nr. 3 — art. 3 — _kb_ · KB nr. 1 — art. 5 — _kb_</small>

## Accountant-perspectieven

### Kantoor verwerkt aftrek-aanvragen cliënt

_De accountant die maandelijks/kwartaalheid de aankopen van de cliënt verwerkt en het aftrekrecht bewaakt._

#### 📒 Boekhouder

##### 👣 Codering aankopen per aftrekstatus  
_`stap`_

🔗 Bij elke ingaande factuur: (1) categoriseren als 100 % aftrekbaar, deel-aftrekbaar (pro-rata), 50 % (autokosten) of 0 % (onthaal, logies/spijzen niet-uitzondering); (2) BTW-bedrag splitsen tussen aftrekbaar deel (D 411) en niet-aftrekbaar deel (kostprijs in 6-rekening); (3) IC-aankoop = verlegging: D 411 + C 451 voor zelfde bedrag (cash-neutraal). Een verkeerde codering = boete + nabetaling bij BTW-controle.

<small>📚 WBTW — art. 45 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 🧭 Methode-keuze pro-rata: algemeen vs werkelijk gebruik  
_`vuistregel`_

🔗 Voor een cliënt met activiteit verdeeld over belast en vrijgesteld: simuleren beide methodes. Werkelijk gebruik is gunstig wanneer de vrijgestelde activiteit weinig BTW-belaste input vergt (bv. medisch advies = vrijgesteld maar gebruikt nauwelijks BTW-belaste input ten opzichte van de belaste consultatie-activiteit). Algemeen verhoudingsgetal is administratief simpel; werkelijk gebruik vraagt aankoopcategorisatie + voorafgaande kennisgeving aan fiscus.

<small>📚 WBTW — art. 46 §2 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Herziening bedrijfsmiddelen (15j vastgoed · 5j BM) → [[btw-herziening-bedrijfsmiddelen]] _(moet-verwijzen)_
- → BTW-bedrijfswagen 50%-regel + methodes → [[btw-bedrijfswagen]] _(moet-verwijzen)_
- → Vrijstellingen art 44 (geen aftrek) → [[btw-vrijstellingen]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[factuur-btw]] — Aftrek vereist regelmatige factuur (KB nr. 3 art. 3).
### `is_uitzondering_op`
- [[btw-vrijstellingen]] — Vrijstellingen art. 44 sluiten aftrek uit; aftrek geldt enkel voor belaste handelingen of vrijstellingen met aftrek (export, IC-leveringen).
### `triggert`
- [[btw-herziening-bedrijfsmiddelen]] — Aftrek op bedrijfsmiddelen kan herzien worden binnen 5 jaar (roerend) of 15 jaar (onroerend) bij bestemmingswijziging.
