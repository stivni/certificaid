---
title: "Meerwaarde op aandelen — vennootschapsbelasting"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.I
  - 2.3.II.J
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/meerwaarde-aandelen-venb.json"
---

_Regime_ · ook: meerwaarde aandelen VenB · art. 192 WIB92

## Definitie

Art. 192 §1 WIB92 stelt meerwaarden op aandelen vrij van vennootschapsbelasting wanneer drie cumulatieve voorwaarden vervuld zijn: (1) taxatievoorwaarde — de inkomsten van de aandelen zouden in aanmerking komen voor de DBI-aftrek (art. 202-203 WIB92), wat betekent dat de uitkerende vennootschap zelf aan een normaal belastingregime onderworpen is; (2) deelnemingsvoorwaarde — minstens 10 % van het kapitaal OF een aanschaffingswaarde van minstens 2,5 mio EUR; (3) permanentievoorwaarde — de aandelen worden in volle eigendom gedurende minstens 1 jaar ononderbroken aangehouden. Als alle drie vervuld: vrijstelling 0 %. Indien deelnemings- en permanentievoorwaarde NIET vervuld maar taxatievoorwaarde wel: belasting aan 25 % (gewoon tarief). Bij geen voorwaarde vervuld: belasting aan 25 %.

<small>📖 WIB92 — art. 192 §1 — _wettekst_ · WIB92 — art. 202-203 — _wettekst_</small>

## Substantie

Praktisch: een holding-vennootschap die deelnemingen in dochters of marktparticipaties verkoopt, kan onder voorwaarden 100 % van de meerwaarde belastingvrij innen. Dit is een van de hoeksteen van het Belgische holding-regime en parallel aan de DBI-aftrek voor dividenden: dezelfde inkomstenbron (deelneming in werkmaatschappij) wordt zowel op dividend-niveau (DBI) als op meerwaarde-niveau (art. 192) fiscaal beschermd. Sinds wet 25-12-2017 zijn de voorwaarden geharmoniseerd met DBI: vóór 2018 gold een afzonderlijk regime met enkel taxatievoorwaarde + 1 jaar houdperiode (en sanctie 25,5 % bij niet-permanentie). De handelsportefeuille van kredietinstellingen is uitgesloten — die aandelen worden steeds belast.

<small>🔗 WIB92 — art. 192 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Ratio legis: vermijden van dubbele belasting binnen vennootschappen-groepen. De winst van een werkmaatschappij is al in haar hoofde belast met VenB. Wanneer de moedervennootschap dividend ontvangt uit die winst: DBI-aftrek voorkomt dubbele belasting. Wanneer de moeder de aandelen later verkoopt aan meerwaarde: art. 192 voorkomt dat dezelfde latente winst opnieuw belast wordt. De voorwaarden (taxatie + deelneming + permanentie) garanderen dat het om substantiële, langdurige deelnemingen gaat — geen kortetermijn-speculatie via lege constructies.

<small>🔗 WIB92 — art. 192 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 192 §1 (vrijstelling) + art. 202-203 (taxatievoorwaarde via DBI-link)

Sinds VenB-hervorming 2018 (wet 25-12-2017) geharmoniseerd met DBI: deelnemings- en permanentievoorwaarde toegevoegd. Vóór 2018: alleen taxatie + 1 jaar. Beruchte 0,4 %-mini-VenB op meerwaarden zonder permanentievoorwaarde afgeschaft vanaf AJ 2019.

**✅ Voor**
- 🔗 Vennootschap die meerwaarden realiseert op aandelen van andere vennootschappen — typisch holding-vennootschappen die deelnemingen in werkmaatschappijen verkopen, of operationele vennootschappen die strategische participaties hebben.

**🚫 Niet voor**
- 📖 Aandelen die behoren tot de handelsportefeuille van kredietinstellingen — die worden steeds belast als handelswinst. Aandelen waarvan de inkomsten niet voldoen aan de DBI-taxatievoorwaarde (bv. aandelen in vennootschappen gevestigd in jurisdicties zonder gemeenrechtelijke belasting): geen vrijstelling.

**📋 Voorwaarden**
- 📖 Drie cumulatieve voorwaarden voor 0 % vrijstelling: (1) TAXATIE: inkomsten uit de aandelen zouden in aanmerking komen voor DBI-aftrek — uitkerende vennootschap onderworpen aan normaal belastingregime in haar woonstaat (geen tax haven, geen afwijkend gunstig regime); (2) DEELNEMING: minstens 10 % van het kapitaal van de uitkerende vennootschap OF aanschaffingswaarde minstens 2.500.000 EUR; (3) PERMANENTIE: aandelen sinds minstens 1 jaar onafgebroken in volle eigendom.

**👍 Voordeel**
- 📖 0 % VenB op meerwaarden — totaal vrijgesteld in belastbare basis. Bij verkoop van substantiële deelneming kan dit honderdduizenden tot miljoenen EUR voordeel opleveren. Geen aftrek-volgorde-impact (vrijstelling = niet in belastbare basis, niet 'aftrek').

**⚠️ Risico**
- 📖 Bij niet-naleving deelnemings- of permanentievoorwaarde (maar wel taxatie): belasting 25 % VenB. Bij niet-naleving taxatievoorwaarde (bv. tax-haven-deelneming): 25 % zonder verzachting. CFC-meerwaarden op aandelen van eerder belaste CFC-winst: vrijstelling beperkt tot dat eerder belaste bedrag (art. 192 §4 — circulaire 2024/C/82 van 13-12-2024).

## Bouwstenen

### 📜 Taxatievoorwaarde (via DBI-link)

De inkomsten uit de aandelen moeten voldoen aan de DBI-taxatievoorwaarde (art. 202-203 WIB92): de uitkerende vennootschap is onderworpen aan een normaal belastingregime in haar woonstaat. Uitgesloten: vennootschappen gevestigd in landen zonder VenB of met gunstig afwijkend regime (art. 203 §1 1°), tax-haven-jurisdicties op de EU-lijst van niet-coöperatieve jurisdicties, beleggingsvennootschappen met afwijkend regime, financierings-/thesaurie-/beleggingsvennootschappen met afwijkend gunstig regime.

<small>📖 WIB92 — art. 203 §1 — _wettekst_</small>

### 📏 Deelnemingsvoorwaarde — 10 % of 2,5 mio EUR

Voor vrijstelling moet de moeder op het ogenblik van de verkoop ofwel minstens 10 % van het kapitaal van de uitkerende vennootschap aanhouden, ofwel aandelen voor een aanschaffingswaarde van minstens 2.500.000 EUR. Alternatieve voorwaarden — één van beide volstaat. Geïntroduceerd in 2018 — vóór 2018 was er geen deelnemingsvoorwaarde voor de art. 192-vrijstelling (wel voor DBI).

<small>📖 WIB92 — art. 202 §2 — _wettekst_</small>

### 📏 Permanentievoorwaarde — 1 jaar volle eigendom

De aandelen moeten gedurende een ononderbroken periode van minstens 1 jaar in volle eigendom aangehouden zijn op het ogenblik van de realisatie van de meerwaarde. Vruchtgebruik of tijdelijke aandelenleningen tellen niet als 'volle eigendom'. Periode-onderbreking (zelfs kort) reset de telling. Vóór 2018: zelfde 1-jaar-voorwaarde gold maar niet-naleving leidde tot 25,5 %-tarief (mini-VenB); sinds 2018: niet-naleving = gewoon 25 % VenB.

<small>📖 WIB92 — art. 192 §1 — _wettekst_</small>

### ⚙️ Tarieven afhankelijk van voorwaarde-naleving

Scenario's: (a) alle drie voorwaarden vervuld → 0 % vrijstelling (volledig); (b) taxatievoorwaarde vervuld, deelnemings- of permanentievoorwaarde niet → 25 % gewoon VenB-tarief op de meerwaarde; (c) taxatievoorwaarde NIET vervuld (bv. tax-haven-aandelen) → 25 % VenB, geen vrijstelling. Vóór 2018: bestond een tussentarief van 25,5 % wanneer 1-jaar-permanentievoorwaarde niet vervuld; geschrapt vanaf AJ 2019.

<small>📖 WIB92 — art. 192 §1 — _wettekst_ · WIB92 — art. 215 — _wettekst_</small>

### 📜 Minwaarden op aandelen — niet aftrekbaar

Spiegelbeeld van de vrijstelling: minwaarden op aandelen zijn NIET aftrekbaar als beroepskost (art. 198 §1 7° WIB92), behalve bij vereffening van de uitkerende vennootschap en dan beperkt tot het verlies aan inbrengkapitaal. Waardeverminderingen op aandelen geboekt op de balans = verworpen uitgave. Dit is consistent met de vrijstelling van meerwaarden — hetzelfde regime geldt symmetrisch.

<small>📖 WIB92 — art. 198 §1 7° — _wettekst_</small>

## Voorbeelden

> [!example]- Aurelia Holding NV verkoopt 100 % Zelena Bio NV
> _Aurelia Holding bezit sinds 5 jaar 100 % van Zelena Bio NV (aanschaffingswaarde 800.000 EUR). In jaar N verkoopt Aurelia alle aandelen aan een externe koper voor 3.000.000 EUR. Meerwaarde: 2.200.000 EUR. Zelena is een Belgische werkmaatschappij onderworpen aan VenB._
>
> **Berekening:**
>
> - Stap 1 — taxatievoorwaarde: Zelena is Belgische VenB-vennootschap → vervuld.
> - Stap 2 — deelnemingsvoorwaarde: 100 % van het kapitaal > 10 %-drempel én aanschaffingswaarde 800.000 < 2,5 mio (alternatief niet vereist want 10 % ruim vervuld). Vervuld.
> - Stap 3 — permanentievoorwaarde: 5 jaar in volle eigendom > 1 jaar. Vervuld.
> - Stap 4 — alle voorwaarden vervuld → vrijstelling 0 % VenB op meerwaarde 2.200.000 EUR. Belastingbesparing: 2.200.000 × 25 % = 550.000 EUR.
> - Stap 5 — boekhoudkundig: meerwaarde 2.200.000 als opbrengst geboekt (rekening 763 of 769). Fiscaal: aftrek 2.200.000 in vak 'aanpassingen in meer/min' van de aangifte VenB (code 1051).
> - Stap 6 — netto: 2.200.000 EUR meerwaarde volledig in handen Aurelia Holding (kan later via DBI-stroom of liquidatie/dividend doorvloeien).
>
> → **Resultaat**: Volledige fiscale vrijstelling. Geen aftrek-volgorde-impact (vrijstelling i.p.v. aftrek).
>
> <small>🔗 WIB92 — art. 192 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Vrijstelling toepassen op handelsportefeuille
> **Verkeerde assumptie**: Elke verkoop van aandelen door een vennootschap valt onder art. 192.
>
> **Kernpunt**: Aandelen in de handelsportefeuille van kredietinstellingen (art. 192 §1 vierde lid WIB92) zijn EXPLICIET uitgesloten — die meerwaarden zijn altijd belastbaar als handelswinst. Ook voor andere vennootschappen kan een 'handelsportefeuille'-discussie ontstaan: aandelen worden gehouden voor speculatieve doelen i.p.v. langdurige deelneming → fiscus kan vrijstelling betwisten op basis van algemene anti-misbruikbepaling.
>
> <small>📖 WIB92 — art. 192 §1 vierde lid — _wettekst_</small>

> [!warning]- Vrijstelling i.p.v. correctie bij beperkte vrijstelling toepassen
> **Verkeerde assumptie**: Bij meerwaarde wordt altijd ofwel 0 % ofwel 25 % toegepast op de volledige meerwaarde.
>
> **Kernpunt**: Belangrijke beperking (art. 192 §1 tweede lid): vrijstelling slechts voor zover de meerwaarde hoger is dan het totaal van vroeger aanvaarde waardeverminderingen op die aandelen verminderd met meerwaarden eerder belast (art. 24 1° 3° WIB92). Concreet: als eerder een waardevermindering geboekt is en als verworpen uitgave verwerkt, en die wordt later teruggenomen door een waardestijging, dan moet die terugneming eerst worden 'opgevuld' — pas de meerwaarde daarboven is vrijgesteld.
>
> <small>📖 WIB92 — art. 192 §1 tweede lid — _wettekst_ · WIB92 — art. 24 1° 3° — _wettekst_</small>

> [!warning]- Confusie tussen PB-regime en VenB-regime meerwaarde aandelen
> **Verkeerde assumptie**: Het meerwaarde-regime is hetzelfde voor natuurlijke personen en vennootschappen.
>
> **Kernpunt**: VenB-regime (art. 192): vrijstelling 0 % onder de drie voorwaarden, anders 25 %. PB-regime (art. 90 1° en 8° WIB92): normaal vrijstelling (privé-vermogensbeheer), behalve bij speculatieve transacties of belangrijke deelneming verkocht aan buitenlandse vennootschap. Verschillende systematiek, verschillende voorwaarden — niet door elkaar gebruiken.
>
> <small>📖 WIB92 — art. 192 — _wettekst_ · WIB92 — art. 90 1° en 8° — _wettekst_</small>

## Accountant-perspectieven

### Holding/operationele vennootschap die deelneming verkoopt

_Accountant bereidt de fiscale verwerking van een aandelenverkoop voor._

#### 💰 Fiscaal adviseur

##### 👣 Drie-voorwaarden-checklist vóór verkoop

Vóór ondertekening verkoopakte: (1) taxatie — woonstaat uitkerende vennootschap nagaan, EU-tax-haven-lijst checken; (2) deelneming — % kapitaal én aanschaffingswaarde berekenen (één van beide drempels vereist); (3) permanentie — datum verwerving + houdperiode > 1 jaar verifiëren. Bij twijfel over één voorwaarde: planning-mogelijkheid om verkoop met enkele weken te verschuiven (bv. tot houdperiode 1 jaar bereikt). Bij voorwaarde definitief niet vervuld: cliënt informeren dat 25 % VenB van toepassing is.

<small>🔗 WIB92 — art. 192 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Aangifte VenB — codes en aanpassing

Bij vrijstelling: meerwaarde opnemen in 'aanpassingen in meer' code 1051 (vrijstelling art. 192 §1 al. 1) en code 1068 (CFC-regeling art. 192 §4 — indien CFC-historiek). Bij niet-vrijstelling: meerwaarde wordt opgenomen in de gewone winst en belast tegen 25 %. Documentatie bewaren: aankoopfactuur/inbrengakte, verkoopakte, houdperiode-bewijzen, structuur uitkerende vennootschap (statuten + jaarrekeningen om taxatievoorwaarde te onderbouwen).

<small>📖 aangifte-VenB-2025-reserves — codes 1051 + 1068 — _aangifte_ · WIB92 — art. 192 — _wettekst_</small>

#### 🧭 Adviseur

##### 📜 Share-deal vs asset-deal — fiscale afweging

Bij verkoop van werkmaatschappij: share-deal (verkoop aandelen) profiteert van art. 192-vrijstelling indien voorwaarden vervuld → 0 % VenB. Asset-deal (verkoop bedrijfsactiva uit werkmaatschappij): meerwaarde op activa belast in werkmaatschappij (25 %), eventueel gespreid (art. 47) — koper krijgt step-up in fiscale basis (gunstig voor afschrijvingen). Share-deal voordeel ligt bij verkoper; asset-deal voordeel bij koper. Adviseur licht beide opties + step-up-impact toe.

<small>🔗 WIB92 — art. 192 — _wettekst_ · WIB92 — art. 47 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Aandeel-concept (kapitaalstructuur) → [[aandeel]] _(moet-verwijzen)_
- ↪ Σ-keuzekader VenB-voordelen → [[fiscale-voordelen-vennootschap]] _(mag-verwijzen)_
- ↪ Reorganisatie / fiscale-fusie-splitsing → [[fiscale-fusie-splitsing]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-voordelen-vennootschap]]
### `vereist`
- [[aandeel]] — Veronderstelt het concept aandeel als financieel instrument.
### `vergelijkbaar_met`
- [[dbi-aftrek]]
    - **Gelijkenissen**:
        - Beide voorkomen dubbele belasting binnen groepen
        - Beide vereisen taxatievoorwaarde (art. 203)
        - Beide harmonisering 2018: deelnemingsvoorwaarde 10 % of 2,5 mio + permanentie 1 jaar
    - **Verschillen**:
        - DBI: vrijstelling van DIVIDENDEN ontvangen door moeder
        - Art. 192: vrijstelling van MEERWAARDEN bij verkoop deelneming
        - DBI = aftrek in volgorde art. 207; art. 192 = vrijstelling in belastbare basis
    - ⚠️ **Verwarringsrisico**: Beide regimes voor holding-structuren — niet door elkaar gebruiken: dividend-stroom = DBI, aandelenverkoop = art. 192.
