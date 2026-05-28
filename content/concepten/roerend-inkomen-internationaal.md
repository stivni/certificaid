---
title: "Roerend inkomen internationaal"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.VIII
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/roerend-inkomen-internationaal.json"
---

# Roerend inkomen internationaal

_Kader_

📋 Regeling · Anchors: `2.8.VIII` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: internationale dividenden interest royalty's · cross-border RV-regime · DBV-tarieven roerend

## Definitie

📖 Roerend inkomen internationaal omvat de fiscale regels die gelden wanneer dividenden, interesten of royalty's grensoverschrijdend worden uitgekeerd — typisch tussen een betalende vennootschap in één land en een uiteindelijk gerechtigde in een ander land. Drie lagen werken samen: (1) interne bronheffing van de betaalstaat (in BE: roerende voorheffing 30 % op dividenden + interest); (2) verdragsbeperking via DBV (art. 10-12 OESO-MV) — meestal verlaagde tarieven 0/5/10/15 %; (3) EU-richtlijnen voor intra-EU-uitkeringen — moeder-dochterrichtlijn (2011/96/EU) voor dividenden tussen verbonden vennootschappen en interest-royalty-richtlijn (2003/49/EG) voor interest en royalty's tussen verbonden vennootschappen. Bij de ontvanger: vrijstelling of FBB-verrekening om dubbele belasting te vermijden.

<small>📚 OESO-modelverdrag — art. 10 + 11 + 12 — _modelverdrag_ · Richtlijn 2011/96/EU (moeder-dochter) — art. 1-5 — _richtlijn_ · Richtlijn 2003/49/EG (interest-royalty) — art. 1 — _richtlijn_</small>

## Substantie

🔗 Voor de Belgische accountant is dit dé vraag bij elke grensoverschrijdende uitkering: welk tarief wordt geheven, en hoe de belastinglast minimaliseren? Stappenplan: (a) Heeft betaalstaat een interne bronheffing? Belgische dividenden: standaard 30 % RV. (b) Geldt een DBV-tariefverlaging? Voor de meeste Belgische DBV's: 5 % bij ≥ 10 %-deelneming (moeder-dochter), 15 % bij portfolio. (c) Geldt een EU-richtlijn? Moeder-dochter: 0 % bronheffing bij ≥ 10 %-belang + 1 jaar bezit. Interest-royalty: 0 % bij ≥ 25 %-belang + 2 jaar bezit. (d) Bij de ontvanger: DBI-aftrek (voor dividend) of FBB (interest/royalty) om dubbele belasting te vermijden. (e) Beneficial owner-test: het ontvangende vehikel moet de werkelijke uiteindelijk gerechtigde zijn — anti-treaty-shopping.

<small>📚 OESO-modelverdrag — art. 10-12 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De rationale van het regime is dubbel. (1) Voorkoming dubbele belasting: zonder regeling zouden grensoverschrijdende roerende inkomsten zowel in de betaalstaat (bronheffing) als de woonstaat (gewone belasting) worden geheven — een belemmering voor kapitaalmobiliteit. DBV's en EU-richtlijnen elimineren of milderen dit. (2) Anti-misbruik: maar omgekeerd mag dit niet leiden tot dubbele non-belasting via treaty-shopping (een ontvanger-vehikel kunstmatig in een gunstige jurisdictie plaatsen). Vandaar anti-misbruik-clausules (beneficial owner, principal purpose test, anti-conduit-regels). Sinds BEPS Action 6 (2017) staan in de meeste moderne DBV's expliciete misbruik-bepalingen.

<small>📚 OESO-modelverdrag — art. 10-12 + 29 (PPT) — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: OESO-MV art. 10-12; Richtlijn 2011/96/EU (moeder-dochter, herziene versie); Richtlijn 2003/49/EG (interest-royalty); WIB92 art. 269 e.v. (Belgische RV); art. 285-289 (FBB); art. 202-205 (DBI)

Sinds BEPS-MLI-implementatie hebben veel Belgische DBV's PPT-clausules — verdragsvoordelen kunnen worden geweigerd bij misbruik. EU-richtlijnen blijven gelden zoals voorzien maar met anti-misbruik-clausule (art. 1, lid 4 moeder-dochter).

**✅ Voor**
- 📖 Belgische vennootschap die dividend uitkeert aan een EU-moeder met ≥ 10 %-deelneming: 0 % RV onder moeder-dochterrichtlijn.
- 📖 Belgische BV ontvangt buitenlandse interest van Amerikaanse obligaties: BE-belastbaar in VenB, FBB-verrekening voor de Amerikaanse bronheffing.

**👍 Voordeel**
- 🔗 EU-richtlijnen vrijstellen bronheffingen bij groepsuitkeringen — directe cash-besparing van 10-30 % per uitkering.

**⚠️ Risico**
- 🔗 Weigering verdragsvoordelen door PPT/beneficial-owner-test bij tussen-vennootschappen zonder substance. Resultaat: volle bronheffing zonder verrekening. Substance + documentatie van zakelijke redenen zijn essentieel.

## Bouwstenen

### 📜 Dividenden onder art. 10 DBV  
_`regel`_

📖 Art. 10 OESO-MV: dividenden uit een verdragsstaat mogen worden belast in de woonstaat van de ontvanger; de bronstaat behoudt een beperkt heffingsrecht via bronheffing. OESO-modeltarieven (variabel per DBV): 5 % bij ≥ 25 %-vennootschapsdeelneming (moeder-dochter), 15 % in andere gevallen (portfolio). Belgische DBV's gebruiken vaak 5 % bij ≥ 10 %-deelneming (overlap met moeder-dochterrichtlijn) en 15 % in portfolio. Sinds 2017 staat in de meeste Belgische DBV's een minimum-bezitsperiode van 365 dagen voor de 5 %-toepassing — BEPS Action 6-implementatie.

<small>📚 OESO-modelverdrag — art. 10 §2 — _modelverdrag_</small>

### 📜 Interesten onder art. 11 DBV  
_`regel`_

📖 Art. 11 OESO-MV: interesten uit een verdragsstaat mogen in de woonstaat worden belast; bronstaat heeft beperkt heffingsrecht (typisch 10 % max). Veel Belgische DBV's verlagen tot 0 % voor inter-vennootschapsleningen of voor specifieke schuldvorderingen (bv. bankleningen). Onder interest-royalty-richtlijn (2003/49/EG): 0 % bij ≥ 25 %-belang + 2 jaar bezit + beide entiteiten in EU. Voor portfolio-interest: art. 11 §2-tarief van DBV.

<small>📚 OESO-modelverdrag — art. 11 §2 — _modelverdrag_ · Richtlijn 2003/49/EG — art. 1 — _richtlijn_</small>

### 📜 Royalty's onder art. 12 DBV  
_`regel`_

📖 Art. 12 OESO-MV: royalty's zijn in principe slechts belastbaar in de woonstaat van de uiteindelijk gerechtigde (geen bronheffing, mits Belgische DBV's deze regel volgen — niet alle landen, sommige laten bronheffing toe). Praktisch: voor Belgische uitkeringen van royalty's naar EU-vennootschap met ≥ 25 %-belang geldt 0 % via Interest-Royalty-richtlijn. Voor portfolio-royalty's of niet-EU-ontvangers: DBV-tarief (vaak 0-10 %).

<small>📚 OESO-modelverdrag — art. 12 §1 — _modelverdrag_ · Richtlijn 2003/49/EG — art. 1 — _richtlijn_</small>

### ⚙️ Moeder-dochterrichtlijn: 0 % bronheffing + DBI-aftrek  
_`mechanisme`_

📖 Richtlijn 2011/96/EU (herziene moeder-dochter): voor intra-EU-dividenden tussen verbonden vennootschappen (a) geen bronheffing in de uitkerende lidstaat (art. 5); (b) vrijstelling in de ontvangende lidstaat (art. 4 — Belgisch geïmplementeerd via DBI-aftrek art. 202-205 WIB92). Voorwaarden: minstens 10 %-deelneming + 1 jaar bezitsduur. Sinds 2015 anti-misbruik-clausule (art. 1 lid 4): voordeel wordt geweigerd bij kunstmatige arrangements met als hoofddoel belastingvoordeel.

<small>📚 Richtlijn 2011/96/EU — art. 1, 4 + 5 — _richtlijn_</small>

### ⚙️ Interest-royalty-richtlijn: 0 % bronheffing  
_`mechanisme`_

📖 Richtlijn 2003/49/EG: voor intra-EU-uitkeringen van interest en royalty's tussen verbonden vennootschappen (≥ 25 %-belang + 2 jaar bezit) geldt 0 % bronheffing in de uitkerende lidstaat. Ontvangende lidstaat belast normaal. Voorwaarden: beide vennootschappen onderworpen aan een opgesomde lijst van EU-vennootschapsbelastingen; uiteindelijk gerechtigde-vereiste. Anti-misbruik-clausule sinds 2015.

<small>📚 Richtlijn 2003/49/EG — art. 1 + 5 — _richtlijn_</small>

### 📜 Beneficial owner-vereiste  
_`regel`_

📖 DBV-voordelen (art. 10/11/12) zijn enkel beschikbaar voor de uiteindelijk gerechtigde (beneficial owner) van het inkomen. Een tussen-vennootschap die optreedt als loutere doorgeefluik (conduit) zonder werkelijke economische functie kwalificeert niet. HvJ in Danish Cases (C-115/16 e.v., 2019) bevestigde een ruime EU-conform interpretatie van het beneficial-owner-begrip. Praktisch: substance-toets op het ontvangende vehikel.

<small>📚 OESO-modelverdrag — art. 10 §2 + 11 §2 + 12 §1 — _modelverdrag_ · HvJ Danish Cases C-115/16 e.v. — 26 februari 2019 — _rechtspraak_</small>

### 📜 Anti-treaty-shopping (PPT — BEPS Action 6)  
_`regel`_

📖 MLI art. 7 PPT (Principal Purpose Test): verdragsvoordelen worden geweigerd indien een van de hoofddoelen van een arrangement was om dat voordeel te verkrijgen, tenzij de toekenning in lijn ligt met het doel en strekking van het verdrag. Belgische DBV's na MLI-ratificatie (gefaseerd 2019-2024) bevatten PPT. Resultaat: planning vereist legitieme zakelijke redenen + substance, niet enkel formele vehikels.

<small>📚 MLI — art. 7 (PPT) — _modelverdrag_</small>

### ⚙️ Keuze FBB vs DBI (ontvanger-zijde)  
_`mechanisme`_

📖 Bij ontvangst van buitenlands roerend inkomen door BE-vennootschap: dividenden → DBI-aftrek (art. 202-205, 100 % vrijstelling mits voorwaarden); interesten + royalty's → FBB (art. 285-289, forfait 15/85 verrekening). Bij ontvangst door PB-rijksinwoner-natuurlijke-persoon: normale RV-tarief op het bruto-inkomen + eventuele FBB-aftrek voor de buitenlandse bronheffing (afhankelijk van DBV).

<small>📚 WIB92 — art. 202 + 285 — _wettekst_</small>

## Voorbeelden

### 💡 Belgische moeder ontvangt dividend van Franse dochter 🔗

_Aurelia Holding NV (BE, 25 %-belang sinds 5 jaar) ontvangt bruto-dividend 1.000.000 EUR van Bordeaux SAS (FR-dochter)._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "Stap 1 — uitkerende kant (FR): moeder-dochterrichtlijn → 0 % bronheffing (≥ 10 % + ≥ 1 jaar).",
    "Stap 2 — ontvangende kant (BE): dividend opgenomen in resultaat 1.000.000 EUR.",
    "Stap 3 — DBI-aftrek art. 202 WIB92: 100 % aftrek mits taxatievoorwaarde (FR VenB) + bezitsduur + 10 %-minimum vervuld.",
    "Stap 4 — effectief belastbaar in BE: 0 EUR (volledige DBI-aftrek).",
    "Stap 5 — totale belastingdruk: enkel FR VenB op de winst waarmee het dividend werd uitgekeerd (geen bronheffing, geen BE-VenB)."
  ],
  "resultaat": "Optimale fiscale neutraliteit voor groepsuitkering. Voorwaarde: substance van Belgische moeder + bewijs taxatievoorwaarde dochter."
}
```

<small>📚 Richtlijn 2011/96/EU — art. 4 + 5 — _richtlijn_ · WIB92 — art. 202 — _wettekst_</small>

### 💡 Belgische particulier ontvangt portfolio-dividend uit Duitsland 🔗

_Mevrouw Z., BE-rijksinwoner, ontvangt 1.000 EUR bruto dividend van een Duitse beursvennootschap. DBV BE-DE: 15 %-bronheffing._

**Berekening:**
- Bruto dividend: 1.000 EUR.
- Duitse bronheffing 15 % (DBV-tarief): 150 EUR.
- Netto ontvangen: 850 EUR.
- BE RV op het netto: 850 × 30 % = 255 EUR.
- Geen FBB-verrekening op portfolio-dividenden in PB sinds AJ 1990.
- Netto-netto: 850 − 255 = 595 EUR.

→ **Resultaat**: Totale belastingdruk 405 EUR op 1.000 EUR bruto = 40,5 %. Belangrijk: geen FBB-compensatie voor PB-portfolio-dividenden — een veel-vergeten valkuil.

<small>📚 DBV BE-DE — art. 10 §2 b — _modelverdrag_ · WIB92 — art. 269 — _wettekst_</small>

## Valkuilen

### ⚠️ Moeder-dochterrichtlijn ook op niet-EU-dochter toepassen

**Verkeerde assumptie**: 0 %-bronheffing toepassen op dividend van een Zwitserse of UK-dochter omdat het moederbedrijf in BE staat.

**Kernpunt**: Moeder-dochterrichtlijn geldt enkel intra-EU. Voor Zwitserland: aparte BE-CH-overeenkomst die vergelijkbare 0 %-werking heeft. Voor UK post-Brexit: enkel DBV-tarieven (gewoonlijk 5 %). Eerst land-status checken.

<small>📚 Richtlijn 2011/96/EU — art. 2 (definitie EU-vennootschap) — _richtlijn_</small>

### ⚠️ Bezitsduur-eis voor moeder-dochter vergeten

**Verkeerde assumptie**: 0 %-bronheffing aanvragen voor een dividend van een recent verworven dochter.

**Kernpunt**: Moeder-dochterrichtlijn vereist 1-jaar minimumbezit (sommige lidstaten korter, BE 12 maanden). Bij niet-vervulling: lidstaten mogen bronheffing toepassen. Plan acquisities en dividenduitkeringen rond deze drempel.

<small>📚 Richtlijn 2011/96/EU — art. 3 — _richtlijn_</small>

### ⚠️ Beneficial-owner-vereiste onderschatten

**Verkeerde assumptie**: Een Belgische holding-vennootschap die dividend doorbetaalt naar offshore-aandeelhouders kan toch DBV-voordelen claimen.

**Kernpunt**: HvJ Danish Cases (2019): een conduit-vennootschap zonder werkelijke economische functie is geen beneficial owner. Bronstaat mag voordelen weigeren. Substance + reële beslissingsbevoegdheid in de tussen-vennootschap zijn essentieel.

<small>📚 HvJ Danish Cases C-115/16 e.v. — 26 februari 2019 — _rechtspraak_</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Tarief-matrix: welk regime voor welke uitkering?

## Verder lezen (scope-out)

- → Moeder-dochterrichtlijn (specifiek instrument) → [[moeder-dochterrichtlijn]] _(moet-verwijzen)_
- → Interest-royalty-richtlijn (specifiek instrument) → [[interest-royalty-richtlijn]] _(moet-verwijzen)_
- → FBB-verrekentechniek (toepassing) → [[forfaitair-gedeelte-buitenlandse-belasting]] _(moet-verwijzen)_
- → Belgische roerende inkomsten (PB-context) → [[roerend-inkomen-pb]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `vereist`
- [[dubbelbelastingverdrag]] — Tarief en methodologie volgen uit het concrete DBV en eventuele EU-richtlijnen.
### `triggert`
- [[forfaitair-gedeelte-buitenlandse-belasting]] — Bij ontvangst van buitenlandse interest of royalty in VenB-context: FBB-verrekening.
- [[dbi-aftrek]] — Bij ontvangst van buitenlands dividend in VenB-context (≥ 10 % + voorwaarden): DBI-aftrek.
### `beinvloed_door`
- [[moeder-dochterrichtlijn]] — Specifiek EU-regime voor intra-EU groepsdividenden — 0 %-bronheffing + ontvanger-vrijstelling.
- [[interest-royalty-richtlijn]] — Specifiek EU-regime voor intra-EU groepsinterest en -royalty's — 0 %-bronheffing.
### `vergelijkbaar_met`
- [[roerend-inkomen-pb]]
    - **Gelijkenissen**:
        - Beide handelen over roerende inkomsten (dividend, interest, royalty)
        - Beide gebruiken DBV-tariefverlagingen
    - **Verschillen**:
        - Internationaal: focus op grensoverschrijdende RV-modaliteiten + EU-richtlijnen
        - PB: focus op interne belastbaarheid van Belgische particulieren — RV-bevrijdend, geen DBI/FBB op portfolio voor PB
        - Ontvanger-behandeling verschilt: PB heeft geen DBI; VenB heeft DBI + FBB; PB-FBB sinds AJ 1990 afgeschaft
    - ⚠️ **Verwarringsrisico**: Studenten passen DBI of FBB toe op PB-portfolio-dividend — fout. PB-particulier heeft minder anti-dubbele-belasting-tools dan VenB-vennootschap.
