---
title: "BTW-bonnen en vouchers"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 2.4.IV
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-bonnen-vouchers.json"
---

# BTW-bonnen en vouchers

_Regime_

🏢 Entiteit · 📋 Regeling · Anchors: `2.4.IV` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: voucher BTW-behandeling · cadeaubon BTW · geschenkbon

## Definitie

📖 Een voucher (WBTW art. 1, 1°) is een instrument dat de verplichting inhoudt om het als (volledige of gedeeltelijke) tegenprestatie te aanvaarden voor leveringen van goederen of diensten, en waarbij op het instrument zelf of in de bijbehorende documentatie de te verrichten goederen/diensten of de identiteit van de potentiële verrichters vermeld staan. Voor BTW-doeleinden bestaan twee types: (a) voucher voor enkelvoudig gebruik (SPV — single-purpose) waarbij op uitgiftedatum zowel de plaats van levering ALS het BTW-tarief vaststaan; (b) voucher voor meervoudig gebruik (MPV — multi-purpose) waarbij minstens één van die twee elementen onbekend is.

<small>📚 WBTW — art. 1, 1°-3° — _wettekst_ · Richtlijn (EU) 2016/1065 — art. 30bis Richtlijn 2006/112 — _richtlijn_</small>

## Substantie

📖 Het sleutelonderscheid stuurt het moment van BTW-opeisbaarheid: bij SPV wordt elke overdracht behandeld als de levering zelf — BTW wordt verschuldigd bij elke verkoop in de keten (uitgever, tussenhandel, eindverkoper) volgens het tarief van het onderliggende goed. De feitelijke inwisseling tegen het goed is fiscaal géén afzonderlijk feit meer. Bij MPV daarentegen wordt BTW pas verschuldigd bij effectieve inwisseling (= moment waarop het goed wordt geleverd of de dienst verricht). De uitgifte en doorverkoop van een MPV zijn fiscaal neutrale verrichtingen.

<small>📚 WBTW — art. 22ter §1 — _wettekst_ · WBTW — art. 26 §2 — _wettekst_</small>

## Rationale

🔗 Vóór 2019 leidden vouchers tot onzekerheid en fraude (verschillende lidstaten kwalificeerden ze anders → dubbele heffing of niet-heffing). De voucher-richtlijn 2016/1065 brengt EU-harmonisatie. Het onderscheid SPV/MPV is praktisch: bij SPV is alle informatie er om BTW correct te heffen bij uitgifte (= eenvoudig administratief); bij MPV wachten we tot inwisseling want pas dan kennen we het tarief en de plaats — het zou anders gokken zijn.

<small>📚 Richtlijn (EU) 2016/1065 — Considerans — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-01-01** · basis: W 11-02-2019 (omzetting Richtlijn 2016/1065)

Nieuwe regels van toepassing op vouchers uitgegeven na 31-12-2018.

## Sub-concepten

### 📦 Voucher voor enkelvoudig gebruik (SPV)  
_`regime` (subconcept)_

#### Definitie

📖 SPV = voucher waarbij OP UITGIFTEMOMENT bekend is: (1) de plaats van de levering of dienst waarop hij betrekking heeft (i.e. welk land BTW heft), én (2) het BTW-tarief verschuldigd over die levering. Klassiek voorbeeld: cadeaubon van een Belgisch boekenwinkel-keten (alleen boeken aan 6 % → tarief gekend, plaats = België → bekend). Behandeling: elke overdracht (uitgever → tussenhandel → consument) = belastbare levering tegen 6 %; feitelijke afhaling boek is geen aparte BTW-handeling meer.

<small>📚 WBTW — art. 1, 2° — _wettekst_ · WBTW — art. 22ter §1 — _wettekst_</small>

### 📦 Voucher voor meervoudig gebruik (MPV)  
_`regime` (subconcept)_

#### Definitie

📖 MPV = alle vouchers die geen SPV zijn (WBTW art. 1, 3°). Praktisch: voucher voor een keten van winkels die meerdere tarieven verkoopt (bv. supermarkt: 6 % voeding + 21 % non-food), of cross-border voucher (Belgische supermarkt-keten die ook in Nederland verkoopt → plaats van levering onbekend bij uitgifte). Behandeling: uitgifte en alle tussenoverdrachten = fiscaal neutraal (geen BTW); BTW wordt pas verschuldigd bij INWISSELING tegen het concrete goed door de eindverkoper. Maatstaf = tegenprestatie betaald voor de voucher (art. 26 §2).

<small>📚 WBTW — art. 1, 3° — _wettekst_ · WBTW — art. 26 §2 — _wettekst_</small>

## Bouwstenen

### ⚙️ Voucher vs betalingsinstrument  
_`mechanisme`_

🔗 Een voucher impliceert een ACCEPTATIEVERPLICHTING voor de verkoper en is gekoppeld aan een specifieke set goederen/diensten of verkopers. Een betalingsinstrument (bv. bankkaart, betalingstoken) is daarentegen een algemeen geldverkeer-middel — geen koppeling met specifieke goederen, geen acceptatieverplichting van één partij. Praktisch verschil: een 'cadeaubon van Aurelia Holding' = voucher; een 'algemene Bancontact-kaart' = betalingsinstrument. Een 'oplaadbare betaalkaart' van een gesloten netwerk-uitgever ligt grijzig en wordt soms voucher genoemd, vandaar de CBN-2018/11-uitleg.

<small>📚 WBTW — art. 1, 1° — _wettekst_ · CBN-advies 2018/11 — Verkoop van (oplaadbare) betaalkaarten — _cbn_</small>

### ⚙️ Voucher vs prijsvermindering / korting  
_`mechanisme`_

🔗 Een voucher geeft RECHT op een levering (volledig of deels); een prijsvermindering is een algemene korting op de toekomstige aankoop zonder vooraf-betaling. Verschil: voucher = betaald + later in te wisselen; korting = op factuur-moment toegekend, geen voorafgaande betaling. BTW-effect: voucher volgt SPV/MPV-regime; korting vermindert de maatstaf van heffing op het moment van de feitelijke verkoop (art. 28 WBTW).

<small>📚 WBTW — art. 28 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 🧮 Maatstaf van heffing bij MPV-inwisseling  
_`formule`_

📖 Bij inwisseling MPV (art. 26 §2): maatstaf van heffing = de tegenprestatie effectief betaald voor de voucher (verminderd met de BTW). Bij ontbreken informatie over die tegenprestatie: monetaire waarde op de voucher zelf of in begeleidende documentatie, minus BTW. Voorbeeld: een MPV gekocht voor 100 EUR (waarvan klant betaalt) en ingewisseld voor goederen aan 21 %: maatstaf = 100 / 1,21 = 82,64 EUR, BTW = 17,36 EUR.

<small>📚 WBTW — art. 26 §2 — _wettekst_</small>

## Voorbeelden

### 💡 Boekenbon Standaard Boekhandel — SPV 🔗

_Standaard Boekhandel BVBA (NL) verkoopt cadeaubonnen 'Goed voor 50 EUR aan boeken in elke Standaard-vestiging in België'. Tarief op boeken = 6 % (Tabel A XIX). Plaats = België. → SPV._

**Berekening:**
- Stap 1 — Kwalificatie: op uitgiftemoment is plaats (België) + tarief (6 %) bekend → SPV
- Stap 2 — Verkoop bon aan consument voor 50 EUR (incl. BTW): maatstaf = 50 / 1,06 = 47,17 EUR; BTW = 2,83 EUR
- Stap 3 — Boeking bij Standaard: D 550 Bank 50,00 / C 70 Omzet 47,17 + C 451 BTW 2,83 (rooster 01: 47,17, rooster 54: 2,83)
- Stap 4 — Inwisseling tegen boek 6 maanden later: geen extra BTW-handeling. Aflevering boek geboekt: D 489 Diverse schulden 50,00 / C 60 Voorraad-afname (afname inventaris). De BTW was al afgerekend op uitgiftemoment.

→ **Resultaat**: Eénmaal BTW geheven bij uitgifte, geen dubbele heffing bij inwisseling.

<small>📚 WBTW — art. 22ter — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Cadeaubon Aurelia Supermarkt — MPV 🔗

_Aurelia Supermarkt BVBA verkoopt 100-EUR-cadeaubonnen geldig voor alle producten (voeding 6 %, drogerij 21 %, alcohol 21 %, ...). Tarief onbekend bij uitgifte → MPV._

**Berekening:**
- Stap 1 — Kwalificatie: tarief onbekend op uitgiftemoment → MPV
- Stap 2 — Verkoop bon voor 100 EUR: GEEN BTW-handeling. Boeking: D 550 Bank 100 / C 489 'Te leveren tegoed cadeaubonnen' 100
- Stap 3 — Inwisseling 60 dagen later: klant koopt 40 EUR voeding (6 %) + 60 EUR drogerij (21 %)
- Stap 4 — BTW-opeisbaarheid bij inwisseling: voeding 40 / 1,06 = 37,74 (maatstaf) + 2,26 BTW; drogerij 60 / 1,21 = 49,59 + 10,41 BTW
- Stap 5 — Boeking inwisseling: D 489 'Cadeaubonnen' 100 / C 70 Omzet 87,33 + C 451 BTW 12,67 (rooster 01: 37,74, rooster 03: 49,59, rooster 54: 12,67)

→ **Resultaat**: BTW wordt pas geheven op het moment van werkelijke verkoop, tegen het juiste tarief van het concrete product.

<small>📚 WBTW — art. 26 §2 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Alle cadeaubonnen behandelen als MPV

**Verkeerde assumptie**: 'Cadeaubon = belastbaar bij inwisseling.'

**Kernpunt**: Veel cadeaubonnen zijn in werkelijkheid SPV's: een bon van een homogene winkelketen met uniform tarief (bv. boekhandel, fastfood-keten met enkel 12 %-eten). Bij SPV wordt BTW geheven OP UITGIFTEMOMENT. Verkeerd uitstellen tot inwisseling = late opeisbaarheid + boete + interesten.

<small>📚 WBTW — art. 1, 2° + art. 22ter — _wettekst_</small>

### ⚠️ Vervaldatum-tegoed van MPV negeren

**Verkeerde assumptie**: Een onbenutte MPV op vervaldatum heeft geen BTW-impact.

**Kernpunt**: Niet-gebruikte MPV op vervaldatum: het bedrag wordt opbrengst voor de uitgever (CBN-advies 2018/11). Boekhoudkundig: D 489 'Te leveren tegoed' / C 743 'Diverse bedrijfsopbrengsten'. BTW: omdat er geen levering plaatsvindt, is er GEEN BTW verschuldigd op deze 'verloren' tegoed. Dit verschilt van SPV waarbij de BTW al bij uitgifte werd afgerekend.

<small>📚 CBN-advies 2018/11 — Boeking op vervaldatum — _cbn_</small>

### ⚠️ Voucher en korting verwarren

**Verkeerde assumptie**: Een 'kortingsbon' = voucher.

**Kernpunt**: Een kortingsbon ('10 EUR korting bij volgende aankoop') ZONDER voorafgaande betaling is GEEN voucher in BTW-zin. Het is een gewone prijsvermindering die de maatstaf van heffing reduceert op het moment van de feitelijke verkoop (art. 28). Een voucher veronderstelt voorafgaande tegenprestatie van de koper. Bij twijfel: heeft de klant vooraf betaald voor de bon? Ja → voucher; Nee → korting.

<small>📚 WBTW — art. 1, 1° + art. 28 — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Kantoor begeleidt retailer met voucher-programma

_De accountant bij implementatie of audit van een cadeaubon- of voucher-systeem voor een retail-cliënt._

#### 🧭 Adviseur

##### 👣 Diagnose SPV vs MPV — twee vragen  
_`stap`_

🔗 Twee diagnostische vragen voor de cliënt: (1) Op uitgiftemoment: is het concrete goed/dienst bekend (en dus zijn tarief)? (2) Op uitgiftemoment: is de plaats van levering bekend? Beide ja → SPV (BTW bij uitgifte); minstens één nee → MPV (BTW bij inwisseling). Voor MPV: registreer voorzichtig de niet-ingewisselde voorraad (489-rekening) en monitor vervaldata.

<small>📚 WBTW — art. 1, 2°-3° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Aparte rekening voor vouchertegoeden  
_`stap`_

📖 MPV: gebruik aparte rekening 489 'Te leveren tegoed vouchers' om uitstaande voucher-saldo te tracken; bij inwisseling: D 489 / C 70 + C 451 BTW. SPV: gewone omzet-boeking bij uitgifte (D 550 / C 70 + C 451), inwisseling = enkel voorraad-verbruik. Bij eindejaarsinventaris: openstaande MPV-saldo onder schulden op de balans (CBN 2018/11).

<small>📚 CBN-advies 2018/11 — Boekingen verkoop + inwisseling — _cbn_</small>

## Verder lezen (scope-out)

- → Opeisbaarheid bij voucher-handeling → [[opeisbaarheid-btw]] _(moet-verwijzen)_
- ↪ Plaats van handeling voucher → [[plaats-van-handeling-btw]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `beinvloed_door`
- [[opeisbaarheid-btw]] — SPV verschuift opeisbaarheid naar uitgifte (art. 22ter); MPV laat opeisbaarheid bij inwisseling (art. 22).
