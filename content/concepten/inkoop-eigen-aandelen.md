---
title: "Inkoop van eigen aandelen"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.IV.C
  - 3.0.IV
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/inkoop-eigen-aandelen.json"
---

# Inkoop van eigen aandelen

_Verrichting_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.IV.C` · `3.0.IV` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: verkrijging van eigen aandelen · share buyback · treasury shares acquisition — **Vertalingen**: fr: rachat d'actions propres

## Definitie

📖 **Inkoop van eigen aandelen** (treasury shares) is de verrichting waarbij een vennootschap haar eigen, door derden of door eigen aandeelhouders gehouden aandelen, terugkoopt. Bij **NV**: vereist beslissing van de algemene vergadering met **80%-meerderheid** (versterkt — art. 7:215 § 1 WVV) en respect voor de netto-actief-test (uitkeerbaarheid). Bij **BV**: beslissing van de AV met statutair vereiste meerderheid + dubbele test (netto-actief + liquiditeit, art. 5:145 WVV). Tot 2019 (W.Venn.) gold een wettelijke 20%-grens op uitstaand kapitaal; sinds WVV is deze limiet geschrapt en vervangen door de uitkeringstest.

<small>📚 WVV — art. 7:215 — _wettekst_ · WVV — art. 5:145 — _wettekst_</small>

## Substantie

📖 Economisch is inkoop een **uitkering aan vertrekkende aandeelhouders** waarbij de vennootschap zelf de tegenpartij is. De ingekochte aandelen worden boekhoudkundig op het actief geboekt (rekening 50 'Eigen aandelen') tegen een onbeschikbare reserve in EV (rekening 145 'Onbeschikbare reserve voor eigen aandelen', CBN 121/3). De vennootschap kan ze later: (a) **opnieuw verkopen** (geen resultaat tenzij voor andere prijs); (b) **vernietigen** (definitieve kapitaalvermindering — art. 7:218); (c) **uitkeren als personeelsaandelen**. Tijdens het bezit zijn de **stemrechten en dividendrechten opgeschort** (art. 7:217 WVV). Fiscaal: indien voorwaarden niet voldaan → **integrale herkwalificatie als dividend** (art. 18, 2°bis WIB92) → RV 30%.

<small>📚 WVV — art. 7:217 — _wettekst_ · WVV — art. 7:218 — _wettekst_ · CBN-advies 121/3 — Mutaties binnen het eigen vermogen — Verkrijging — _advies_ — (1995-01-01) · WIB92 — art. 18, 2°bis — _wettekst_</small>

## Rationale

🔗 Inkoop van eigen aandelen heeft **vier functies**: (1) **exit-mechanisme** voor vertrekkende aandeelhouder zonder dat overige aandeelhouders moeten kopen; (2) **alternatief voor dividend** (efficiënter dan dividenduitkering bij hoge buyback-prijzen door schaarste-effect op resterende aandelen); (3) **anti-dilutie** (bij latere uitgifte personeelsaandelen, gebruik treasury shares ipv nieuwe uitgifte); (4) **stabilisatie aandelenkoers** (genoteerde vennootschappen). De wettelijke voorwaarden (80%-AV-meerderheid, netto-actief-test, gelijkheid aandeelhouders) beschermen de minderheid + de schuldeisers tegen verkapte uitkeringen die de solvabiliteit ondermijnen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV (Wet 23-03-2019)

WVV 2019 schrapte de 20%-limiet (W.Venn. art. 620) en vervangt door netto-actief-test. Voor genoteerde NV: BNB-regelgeving + Wet 25-04-2014 nog steeds van toepassing.

**✅ Voor**
- 🔗 Bij **exit van een aandeelhouder** waarbij de overige aandeelhouders niet (volledig) kunnen of willen inkopen — vennootschap koopt zelf in tegen vergoeding uit eigen middelen.
- 🔗 Bij **uitvoering aandelenoptieplan voor personeel** (treasury shares uitkeren ipv nieuwe uitgifte → vermijdt dilutie bestaande aandeelhouders).

**📋 Voorwaarden**
- 📖 **AV-machtiging** vereist met 80%-meerderheid bij NV (art. 7:215 § 1 WVV) — geldig voor max. **5 jaar**. Machtiging bepaalt max-aantal, max- en min-prijs, en duur. Bij BV: statutair vereiste meerderheid.
- 📖 **Gelijkheid aandeelhouders** — bij NV: aanbod tot inkoop moet aan **alle aandeelhouders pro rata** worden gericht (art. 7:215 § 3) tenzij eenparig akkoord of beurstransactie. Bij BV: statutaire regeling primeert.
- 📖 **Netto-actief-test** (NV via verwijzing 7:215 → kapitaalbescherming-bepalingen; BV art. 5:145): vergoeding mag uitsluitend uit uitkeerbare bedragen worden gefinancierd — eigen vermogen min onbeschikbare componenten moet ≥ blijven. **BV**: ook **liquiditeitstest** (art. 5:143 jo. 5:145) — bestuur moet 12-maanden-solvabiliteit motiveren.
- 📖 **Onbeschikbare reserve** boeken voor de aanschaffingsprijs van de eigen aandelen (rekening 145 — CBN 121/3): EV blijft economisch geblokkeerd zolang aandelen op de balans staan.

**⚠️ Risico**
- 📖 **Fiscale herkwalificatie** (art. 18, 2°bis WIB92): bij niet-naleving van WVV-voorwaarden (geen AV-machtiging, geen netto-actief-respect, geen onbeschikbare reserve) wordt de inkoopprijs **integraal als dividend belast** bij de vertrekkende aandeelhouder → RV 30% over volledige verkoopprijs ipv enkel meerwaarde-deel. **Tip**: zelfs bij correcte uitvoering wordt het deel inkoopprijs > fiscaal gestort kapitaal × pro-rata behandeld als dividend.
- 📖 **Bestuurdersaansprakelijkheid** bij overtreding van netto-actief- of liquiditeitstest (art. 5:145 § 3 / 7:215 verwijzing) — hoofdelijke aansprakelijkheid bestuurders.

## Bouwstenen

### 📜 Voorwaarden inkoop eigen aandelen — NV vs BV  
_`regel`_

📖 **Vergelijking voorwaarden NV vs BV (WVV)**:

| Aspect | NV (art. 7:215-218) | BV (art. 5:145-146) |
|---|---|---|
| AV-meerderheid | 80% | Statutair (min. gewone meerderheid) |
| Duur machtiging | Max. 5 jaar | Statutair |
| Max-grens uitstaand | Geen wettelijk max (was 20% W.Venn.) | Geen wettelijk max |
| Netto-actief-test | Ja (via art. 7:215 verwijzing) | Ja (art. 5:145 § 1) |
| Liquiditeitstest | Nee (W.Venn. systeem) | Ja (12 mnd — art. 5:143) |
| Gelijkheid aandeelhouders | Ja (pro-rata aanbod, art. 7:215 § 3) | Statutair |
| Onbeschikbare reserve | Ja (klasse 145) | Ja (klasse 145) |
| Stemrecht eigen aandelen | Opgeschort (art. 7:217) | Opgeschort (art. 5:146) |
| Dividendrecht | Geen | Geen |

**Genoteerde NV**: bijkomende regels — markt-rapportering, koers-bandbreedte, gelijkheid via beurs (art. 7:215 § 4).

<small>📚 WVV — art. 7:215-7:218 — _wettekst_ · WVV — art. 5:145-5:146 — _wettekst_</small>

### 👣 Boekhoudkundige verwerking — CBN 121/3  
_`stap`_

📖 **Boekingsstappen** bij inkoop eigen aandelen (CBN 121/3):

1. **Verkrijging**:
```
D 500 Eigen aandelen (actief)
  C 550 Bank
```
Gelijktijdig: vorming onbeschikbare reserve (vanuit beschikbare reserves of overgedragen winst):
```
D 133 Beschikbare reserves (of 14 Overgedragen winst)
  C 145 Onbeschikbare reserve voor eigen aandelen
```

2. **Bezit/aanhouding** — geen tussentijdse verwerking; eventueel waardevermindering boeken bij duurzaam waardeverlies (CBN 121/3 → tegenboeking met overzetting onbeschikbare → beschikbare reserve voor het verminderingsbedrag).

3. **Wederverkoop hogere prijs**:
```
D 550 Bank (verkoopprijs)
  C 500 Eigen aandelen (boekwaarde)
  C 759 Andere financiële opbrengsten (meerwaarde)
D 145 Onbeschikbare reserve
  C 133 Beschikbare reserves
```
Meerwaarde gaat door resultatenrekening; reserve wordt vrijgegeven.

4. **Vernietiging** (CBN 121/3):
```
D 100 Geplaatst kapitaal (fractiewaarde × aantal vernietigde aandelen)
D 145 Onbeschikbare reserve (verschil)
  C 500 Eigen aandelen (boekwaarde)
```
Geen resultaat — netto-effect: kapitaal ↓, reserve ↓, eigen aandelen-actief verdwijnt.

<small>📚 CBN-advies 121/3 — Verkrijging + Vernietiging — _advies_ — (1995-01-01)</small>

### 📜 Fiscale impact bij de vertrekkende aandeelhouder  
_`regel`_

📖 **PB-aandeelhouder (natuurlijke persoon)** — twee scenario's:

- **Voorwaarden art. 7:215-218 WVV gerespecteerd**: het deel inkoopprijs > 'pro rata fiscaal gestort kapitaal' wordt als **dividend** (art. 18, 2°bis WIB92) belast → RV 30% door vennootschap ingehouden. Het kapitaal-deel (pro rata fiscaal gestort) is belastingvrij. Aandelen-meerwaarde voor het kapitaal-deel is meestal vrijgesteld als 'normaal beheer privé-vermogen'.
- **Voorwaarden NIET gerespecteerd** (bv. geen AV-machtiging): **integrale herkwalificatie** — volledige inkoopprijs = dividend → RV 30% op volledige bedrag, geen aftrek fiscaal gestort kapitaal.

**VenB-aandeelhouder (vennootschap)** — DBI-regime kan toepassen (art. 202-204 WIB92) op het dividend-deel onder voorwaarden (1 jaar bezit + min. 10% of €2,5M deelneming).

<small>📚 WIB92 — art. 18, 2°bis — _wettekst_ · WIB92 — art. 186 — _wettekst_ · WIB92 — art. 202-204 — _wettekst_</small>

## Voorbeelden

### 💡 BV ExitCo — inkoop aandelen vertrekkende aandeelhouder 🔗

_BV ExitCo heeft 3 aandeelhouders: Alice 50%, Bart 30%, Cindy 20% — kapitaal/inbreng €100.000 (1.000 aandelen × €100), beschikbare reserves €150.000. Cindy wil eruit voor €60.000 (200 aandelen × €300/aandeel). De vennootschap koopt zelf in (Alice en Bart willen niet financieren). Netto-actief-test: na inkoop EV = 100+150-60 = €190.000 → boven onbeschikbare inbreng €100.000 ✓. Liquiditeitstest: bestuur bevestigt 12-mnd-solvabiliteit ✓._

**Boeking:**


**Balans-snapshot**: ``

```json
{
  "titel": "Eigen vermogen — VOOR vs NA inkoop",
  "kolommen": [
    "Rubriek",
    "VOOR (€)",
    "NA (€)"
  ],
  "rijen": [
    [
      "Onbeschikbare inbreng (klasse 11)",
      "100.000",
      "100.000"
    ],
    [
      "Beschikbare reserves (klasse 133)",
      "150.000",
      "90.000"
    ],
    [
      "Onbeschikbare reserve eigen aandelen (klasse 145)",
      "0",
      "60.000"
    ],
    [
      "TOTAAL EV",
      "250.000",
      "250.000 (incl. eigen aandelen)"
    ],
    [
      "Eigen aandelen op actief (klasse 50)",
      "0",
      "60.000"
    ],
    [
      "NETTO EV (gecorrigeerd)",
      "250.000",
      "190.000"
    ]
  ],
  "conclusie": "Boekhoudkundig totaal EV blijft €250.000, maar economisch (gecorrigeerd voor eigen aandelen op actief): €190.000. Onbeschikbare reserve van €60.000 blokkeert die fractie tot vernietiging of wederverkoop."
}
```

**Berekening:**
- Stap 1 — Verhouding: fiscaal gestort kapitaal Cindy-aandelen = €100 × 200 = €20.000
- Stap 2 — Inkoopprijs €60.000; kapitaal-deel €20.000 (belastingvrij); 'dividend'-deel €40.000
- Stap 3 — RV 30% × €40.000 = €12.000 ingehouden door BV
- Stap 4 — Netto-uitkering Cindy: €60.000 - €12.000 = €48.000
- Conclusie: Cindy ontvangt netto €48.000; €12.000 RV doorgestort door BV aan FOD

<small>📚 WVV — art. 5:145 — _wettekst_ · CBN-advies 121/3 — _advies_ — (1995-01-01)</small>

### 💡 Vernietiging van ingekochte eigen aandelen — vervolg ExitCo 🔗

_Een jaar later beslist BV ExitCo om de 200 eigen aandelen definitief te vernietigen (definitieve uitsluiting Cindy uit kapitaal). AV-besluit + notariële akte (art. 7:218 / 5:146 WVV)._

**Boeking:**


_Onbeschikbare inbreng vermindert met fractiewaarde × aantal (200 × €100); rest van boekwaarde komt ten laste van de onbeschikbare reserve. Geen resultaat (CBN 121/3 Vernietiging)._

<small>📚 WVV — art. 7:218 — _wettekst_ · CBN-advies 121/3 — Vernietiging — _advies_ — (1995-01-01)</small>

### 💡 Niet-naleving voorwaarden — integrale herkwalificatie 🔗

_BV InformeleCo koopt eigen aandelen in zonder voorafgaande AV-machtiging en zonder de netto-actief-test te documenteren. Inkoopprijs €100.000. Fiscaal gevolg: integrale herkwalificatie (art. 18, 2°bis WIB92)._

**Weergave** `vergelijkingstabel`:

```json
{
  "titel": "Correct vs niet-conform — fiscale impact",
  "kolommen": [
    "Scenario",
    "Belastbaar bedrag dividend",
    "RV 30%",
    "Netto-uitkering aandeelhouder"
  ],
  "rijen": [
    [
      "Correct (WVV-voorwaarden voldaan): kapitaal-deel €20.000 vrij + dividend-deel €80.000",
      "€80.000",
      "€24.000",
      "€76.000"
    ],
    [
      "Niet-conform (geen AV-machtiging): integrale herkwalificatie €100.000 dividend",
      "€100.000",
      "€30.000",
      "€70.000"
    ]
  ],
  "conclusie": "Niet-naleving = €6.000 méér belasting op €100.000 (= 6% extra). Eenmalige notariskosten + AV-bijeenroeping (~€2.000) is ruim goedmaakkost voor correcte procedure."
}
```

<small>📚 WIB92 — art. 18, 2°bis — _wettekst_</small>

## Valkuilen

### ⚠️ 20%-limiet bestaat nog

**Verkeerde assumptie**: Inkoop van eigen aandelen is wettelijk beperkt tot 20% van het uitstaand kapitaal.

**Kernpunt**: De 20%-grens van art. 620 W.Venn. is **geschrapt** door WVV 2019. Vervangen door netto-actief-test (NV) of dubbele test (BV). Wel: voor genoteerde NV gelden bijkomende beurs-rapporteringsregels. Statuten van individuele vennootschap kunnen vrijwillig een statutaire grens vastleggen.

<small>📚 WVV — art. 7:215 — _wettekst_</small>

### ⚠️ Stemrecht eigen aandelen telt nog

**Verkeerde assumptie**: Eigen aandelen die de vennootschap zelf bezit, kunnen meestemmen op de AV voor strategische beslissingen.

**Kernpunt**: Art. 7:217 / 5:146 WVV: stemrecht én dividendrecht verbonden aan eigen aandelen zijn **van rechtswege opgeschort** zolang ze door de vennootschap worden gehouden. Voor AV-quorum en stemresultaat tellen ze niet mee.

<small>📚 WVV — art. 7:217 — _wettekst_</small>

### ⚠️ Inkoop = vrij van RV

**Verkeerde assumptie**: Bij correcte inkoop volgens WVV is de hele inkoopprijs vrij van roerende voorheffing.

**Kernpunt**: Art. 18, 2°bis WIB92: **enkel het deel inkoopprijs = pro rata fiscaal gestort kapitaal** is RV-vrij. Het overige deel = dividend → RV 30%. Berekenen via verhouding (fiscaal gestort kapitaal) / (kapitaal + belaste reserves).

<small>📚 WIB92 — art. 18, 2°bis — _wettekst_</small>

## Speelruimtes

### 🎚️ Wat doen met ingekochte aandelen — aanhouden, verkopen of vernietigen?

## Accountant-perspectieven

### Vanuit de inkopende vennootschap

#### 📒 Boekhouder

##### 👣 Boekhouding eigen aandelen + reserve  
_`stap`_

📖 Bij verkrijging: gelijktijdig (a) eigen aandelen-actief op klasse 50 boeken aan aanschaffingsprijs, en (b) onbeschikbare reserve vormen op rekening 145 voor zelfde bedrag — bronnen: beschikbare reserves (klasse 133) of overgedragen winst (klasse 14) (CBN 121/3). Bij latere mutaties (verkoop, vernietiging, waardevermindering): reserve gelijktijdig aanpassen.

<small>📚 CBN-advies 121/3 — _advies_ — (1995-01-01)</small>

#### 💰 Fiscaal adviseur

##### 👣 RV-aangifte + pro-rata-toerekening  
_`stap`_

🔗 **Stappen RV bij inkoop**: (1) bevestigen dat alle WVV-voorwaarden vervuld zijn (AV-machtiging, netto-actief, gelijkheid); (2) berekenen pro-rata fiscaal gestort kapitaal vs reserves; (3) RV 30% toepassen op het dividend-deel; (4) RV inhouden bij de aandeelhouder en doorstorten via formulier 273A binnen 15 dagen; (5) DBI-attest opmaken voor VenB-aandeelhouders die DBI claimen; (6) fiscale tabel bijwerken in aangifte VenB.

<small>📚 WIB92 — art. 18, 2°bis, art. 269, art. 186 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kapitaalbescherming — netto-actief-test + liquiditeitstest → [[kapitaalbescherming]] _(moet-verwijzen)_
- → Winstuitkering — alternatieve vorm + RV-herkwalificatie → [[winstuitkering]] _(moet-verwijzen)_
- → Aandeel als onderliggend object → [[aandeel]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ vennootschapsrecht
### `vereist`
- [[kapitaalbescherming]]
### `beinvloed_door`
- [[algemene-vergadering]]
### `vergelijkbaar_met`
- [[winstuitkering]]
    - **Gelijkenissen**:
        - Beide zijn uitkeringen uit eigen vermogen aan aandeelhouders
        - Beide vereisen netto-actief-test (BV ook liquiditeitstest)
        - Beide leiden tot RV 30% op (deels) het uitgekeerde bedrag
    - **Verschillen**:
        - Dividend = uniforme uitkering aan alle aandeelhouders pro rata; inkoop = mogelijk asymmetrisch (alleen vertrekkende aandeelhouder)
        - Dividend uit overgedragen winst → reserves dalen direct; inkoop blokkeert via onbeschikbare reserve
        - Dividend = 100% dividend; inkoop = pro-rata-deel kapitaal vrij + dividend-deel belast
    - ⚠️ **Verwarringsrisico**: Inkoop wordt fiscaal vaak 'dividend genoemd' maar juridisch is het een eigendomstransactie; verkeerde communicatie naar aandeelhouder kan leiden tot foute aangifte.
- [[kapitaalvermindering]]
    - **Gelijkenissen**:
        - Beide kunnen leiden tot definitieve daling van EV (bij vernietiging eigen aandelen)
        - Beide kennen pro-rata-toerekening tussen kapitaal en belaste reserves
    - **Verschillen**:
        - Inkoop = aandeelhouder geeft aandelen af tegen prijs; kapitaalvermindering = uitkering naar alle aandeelhouders zonder noodzakelijk afstand aandelen
        - Inkoop heeft tussenstap (treasury); kapitaalvermindering is rechtstreekse uitkering
        - Kapitaalvermindering vereist 75% AV; inkoop NV 80%
    - ⚠️ **Verwarringsrisico**: Beide raken EV; gebruik van een 'inkoop met vernietiging' is in feite equivalent aan een asymmetrische kapitaalvermindering — fiscale uitkomst kan verschillen.
