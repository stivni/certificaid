---
title: "DBI-aftrek (Definitief Belaste Inkomsten)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/dbi-aftrek.json"
---

_Regime_ · afk: **DBI**

## Definitie

De DBI-aftrek — Definitief Belaste Inkomsten — is een Belgisch VenB-aftrekregime waardoor dividenden die een Belgische vennootschap ontvangt uit een 'gekwalificeerde deelneming' tot 100 % aftrekbaar zijn van haar belastbare winst (art. 202-205 WIB92). Vóór aanslagjaar 2019 was de aftrek beperkt tot 95 %; sinds de hervorming van de vennootschapsbelasting door wet 25 december 2017 is de aftrek opgetrokken tot 100 %. Het regime implementeert de EU-Moeder-dochter-richtlijn 2011/96/EU en breidt ze uit tot dividenden van vennootschappen uit derde landen (mits taxatievoorwaarde). Daarnaast bestaat een gerelateerd regime voor meerwaarden op DBI-aandelen (art. 192 WIB92): bij verkoop van een gekwalificeerde deelneming is de meerwaarde vrijgesteld onder dezelfde voorwaarden.

<small>📖 WIB92 — art. 202 — _wettekst_ · WIB92 — art. 203 — _wettekst_ · WIB92 — art. 204 — _wettekst_ · WIB92 — art. 205 — _wettekst_ · WIB92 — art. 192 — _wettekst_ · Richtlijn 2011/96/EU (Moeder-dochter) — art. 4 — _richtlijn_</small>

## Substantie

Cumulatieve voorwaarden voor de DBI-aftrek (art. 202-203 WIB92). (1) Participatie-voorwaarde — de Belgische moeder bezit ofwel minstens 10 % van het kapitaal van de uitkerende vennootschap, OF haar deelneming heeft een aanschaffingswaarde van minstens 2.500.000 EUR. (2) Houdperiode — de aandelen werden of zullen ononderbroken in volle eigendom gehouden gedurende minstens 1 jaar. (3) Taxatievoorwaarde (art. 203) — de uitkerende vennootschap is onderworpen aan een 'normale' VenB of vergelijkbare buitenlandse belasting; geen DBI-aftrek voor dividenden van vennootschappen in tax-haven-jurisdicties of die genieten van een afwijkend voordelig fiscaal regime. Operationeel: de Belgische moeder neemt het bruto-dividend op in haar winst (art. 202, 1°) en trekt het terug af via de DBI-aftrek in de aangifte (vakken 1631-1650). Het surplus dat in een belastbaar tijdperk niet kan worden afgetrokken wegens gebrek aan winst, is onbeperkt overdraagbaar (art. 205 §3 — codes 1701-1704).

<small>📖 WIB92 — art. 202 §2 — _wettekst_ · WIB92 — art. 203 — _wettekst_ · WIB92 — art. 205 §3 — _wettekst_ · aangifte-VenB-2025-dbi-detail — _aangifte_</small>

## Rationale

Zonder DBI-aftrek zou dezelfde winst meermaals worden belast in de keten van vennootschappen: dochter betaalt VenB op haar winst → keert dividend uit → moeder zou er VenB op betalen → keert door naar grootmoeder → … = economische dubbel- of veelvuldige belasting. De DBI-aftrek neutraliseert dit door uitkerend dividend uit een gekwalificeerde deelneming vrij te stellen op moederniveau. De taxatievoorwaarde (art. 203) verhindert dat het regime gebruikt wordt om winst uit laagbelastende jurisdicties belastingvrij naar België te halen. Het Belgische regime is genereuzer dan het EU-minimum (Richtlijn 2011/96/EU): de EU vraagt enkel 'vrijstelling-bij-keten' tussen EU-moeder-dochter; België past de DBI ook toe op derde-land-dividenden mits taxatievoorwaarde, en heeft de aftrek opgetrokken van 95 % naar 100 %.

<small>🔗 Richtlijn 2011/96/EU (Moeder-dochter) — Considerans + art. 4 — _richtlijn_ · WIB92 — art. 203 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-01-01** · basis: Art. 202-205 WIB92 — fundament sinds 1991, hervormd tot 95 %-aftrek in 1992, opgetrokken tot 100 % door wet 25-12-2017 (toepasselijk vanaf AJ 2019, boekjaren vanaf 01-01-2018). EU-grondslag: Richtlijn 2011/96/EU (Moeder-dochter, hercodificatie van Richtlijn 90/435/EEG).

100 %-aftrek sinds AJ 2019. Vóór 2019 was de aftrek beperkt tot 95 % — voor lopende geschillen over oudere aanslagjaren geldt nog de oude regel. Aanverwante regimes: art. 192 (meerwaarden DBI-aandelen) — eveneens 100 % vrijstelling sinds 2018; oud regime kende een hertaxatie-mechanisme bij verkoop binnen 1 jaar.

**✅ Voor**
- 🔗 Bij elke Belgische vennootschap die een deelneming aanhoudt in een andere binnenlandse of buitenlandse vennootschap waaruit ze dividenden ontvangt. Houdt ze géén deelneming aan (financieel actief is geen aandelen): geen DBI-aftrek mogelijk — gewoon belastbaar.

**📋 Voorwaarden**
- 📖 Cumulatieve voorwaarden: (1) Belgische vennootschap is onderworpen aan VenB of BNI/Ven; (2) participatievoorwaarde — minstens 10 % deelneming OF aanschaffingswaarde ≥ 2.500.000 EUR; (3) ononderbroken volle eigendom gedurende minstens 1 jaar (mag al verstreken zijn op moment uitkering, of mag verbintenis zijn om te behouden — art. 192 §1, derde lid); (4) uitkerende vennootschap voldoet aan taxatievoorwaarde van art. 203 (geen tax-haven of bevoorrecht regime).

**⛔ Uitsluitingen**
- 📖 Geen DBI-aftrek voor: (a) dividenden van vennootschappen in 'laagbelastend' land of die genieten van een belastingregime dat 'aanzienlijk gunstiger' is dan de Belgische VenB (art. 203 §1, 1°); (b) financieringsvennootschappen, thesaurievennootschappen en beleggingsvennootschappen met bevoorrecht regime (art. 203 §1, 2°); (c) vennootschappen die met inkomsten uit een onroerend goed bevoorrecht zijn (art. 203 §1, 3°); (d) tussenliggende offshore-vehikels (art. 203 §1, 4°-5°). Vrijstellingen en uitzonderingen worden uitgewerkt in art. 203 §2-§5 (o.a. 90 %-drempel voor uitkeringen door beleggingsvennootschappen aandelen, 80 %-drempel voor vastgoedbevak).

## Bouwstenen

### 📏 Participatiedrempel: 10 % of 2,5 M EUR

Twee alternatieve criteria, voldoende dat één van beide vervuld is. (a) Kapitaalsdrempel — de deelneming bedraagt minstens 10 % van het maatschappelijk kapitaal van de uitkerende vennootschap. (b) Waarde-drempel — de deelneming heeft een aanschaffingswaarde van minstens 2.500.000 EUR (bedrag vast, niet geïndexeerd). Voor kredietinstellingen en verzekeringsondernemingen gelden uitzonderingen die het 10 %-criterium versoepelen.

<small>📖 WIB92 — art. 202 §2, eerste lid 1° — _wettekst_</small>

### 📏 Houdperiode: 1 jaar ononderbroken volle eigendom

De aandelen moeten gedurende minstens 12 maanden ononderbroken in volle eigendom gehouden worden. De periode mag voor de dividenduitkering reeds verstreken zijn (rugwaarts kijkend) of nog deels lopen (voorwaartse verbintenis om te behouden). Bij omruil ten gevolge van een belastingneutrale fusie/splitsing/verrichting (art. 211, 214 WIB92): de in ruil ontvangen aandelen worden geacht verkregen te zijn op datum van de oorspronkelijke aandelen — de houdperiode loopt ononderbroken door (art. 192 §1, zevende lid).

<small>📖 WIB92 — art. 192 §1, zevende lid — _wettekst_ · Wet 24-12-2002 — art. 17 (toevoeging art. 282 — 12-maandenregel voor RV-doorstroming) — _wettekst_</small>

### 📜 Taxatievoorwaarde (art. 203) — anti-laagbelasting

De uitkerende vennootschap moet onderworpen zijn aan een 'normale' VenB (Belgisch tarief) of een vergelijkbare buitenlandse belasting. De norm: het buitenlandse tarief mag niet 'aanzienlijk gunstiger' zijn dan de Belgische VenB (concreet: niet minder dan de helft, dus ca. < 12,5 %). De KB-lijst van laagbelastende landen vormt een vermoeden van uitsluiting. Specifieke voorwaarden gelden voor uitkeringen door beleggingsvennootschappen (90 %-doorstoot-drempel art. 203 §4) en vastgoedbevak's (80 %-drempel art. 203 §5).

<small>📖 WIB92 — art. 203 §1 — _wettekst_</small>

### 📜 Onbeperkte overdraagbaarheid surplus DBI (art. 205 §3)

Als de DBI-aftrek in een belastbaar tijdperk de belastbare winst overstijgt (gebrek aan restwinst), wordt het surplus overgedragen naar het volgende tijdperk — onbeperkt in tijd. In de aangifte: code 1701 (saldo uit voorgaand AJ) + 1702 (nieuwe overdracht dit jaar) − 1703 (effectief benut van voorraad) = 1704 (saldo overdraagbaar). Sinds Wet 21-12-2013 ingevoerd; EU-vereiste vanuit zaak Cobelfret (HvJ C-138/07).

<small>📖 WIB92 — art. 205 §3 — _wettekst_ · aangifte-VenB-2025-dbi-detail — _aangifte_</small>

### 📜 Verwante regel: vrijstelling meerwaarden op DBI-aandelen (art. 192)

Meerwaarden op aandelen die voor DBI-aftrek in aanmerking komen (dezelfde voorwaarden: 10 % of 2,5 M EUR + 1 jaar houdperiode + taxatievoorwaarde) zijn vrijgesteld van VenB onder art. 192 WIB92. Vóór 2018 gold een afzonderlijk tarief 0,4 % op meerwaarden van grote vennootschappen + heffing voor verkoop binnen 1 jaar; deze tarieven werden afgeschaft door de VenB-hervorming 2017. Sinds AJ 2019 dus volledig 100 % vrijgesteld, mits cumulatieve DBI-voorwaarden.

<small>📖 WIB92 — art. 192 §1 — _wettekst_</small>

## Voorbeelden

> [!example]- Dividend uit Luxemburgse dochter naar Belgische moeder
> _Belgische moeder NV bezit 25 % van haar Luxemburgse dochter SA (gewone Luxemburgse VenB-onderworpen, geen bevoorrecht regime). Deelneming sinds 5 jaar in volle eigendom. In jaar N keert SA een dividend uit van 500.000 EUR (na inhouding RV in Luxemburg)._
>
> <small>🔗 WIB92 — art. 202 — _wettekst_ · Richtlijn 2011/96/EU (Moeder-dochter) — art. 4 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- DBI = 95 % onthouden
> **Verkeerde assumptie**: Stagiairs leren de oude regel '95 % DBI-aftrek'.
>
> **Kernpunt**: Sinds aanslagjaar 2019 (boekjaren vanaf 01-01-2018) is de aftrek opgetrokken naar 100 % door de VenB-hervorming (Wet 25-12-2017). 95 % geldt nog voor oudere aanslagjaren en lopende bezwaarprocedures over die periode. Bij examenvraag eerst checken: welk aanslagjaar?
>
> <small>📖 WIB92 — art. 204 — _wettekst_</small>

> [!warning]- Participatie-voorwaarde stapelen (10 % AND 2,5 M EUR)
> **Verkeerde assumptie**: Beide voorwaarden moeten cumulatief vervuld zijn.
>
> **Kernpunt**: De wet zegt 'minstens 10 % OF aanschaffingswaarde ≥ 2.500.000 EUR' (art. 202 §2, 1°). Eén van beide volstaat. Een deelneming van 5 % met aanschaffingswaarde van 3 M EUR komt in aanmerking; een deelneming van 12 % met aanschaffingswaarde van 200.000 EUR komt ook in aanmerking.
>
> <small>📖 WIB92 — art. 202 §2, eerste lid 1° — _wettekst_</small>

> [!warning]- Houdperiode vereist voltooide 12 maanden vóór uitkering
> **Verkeerde assumptie**: De deelneming moet al 12 maanden in eigendom zijn vóór de dividenduitkering.
>
> **Kernpunt**: De houdperiode kan voor- of na de uitkering vervuld worden. Het volstaat dat de moeder zich verbindt om de aandelen tot na het verstrijken van 12 maanden in volle eigendom te houden. Bij vroegtijdige verkoop binnen die periode: terugname van de DBI-aftrek.
>
> <small>📖 WIB92 — art. 192 §1, zevende lid — _wettekst_ · Wet 24-12-2002 — art. 17 — _wettekst_</small>

> [!warning]- Verschil met Moeder-dochter-richtlijn-vrijstelling
> **Verkeerde assumptie**: DBI-aftrek = automatische EU-vrijstelling onder Moeder-dochter-richtlijn.
>
> **Kernpunt**: Twee gerelateerde maar verschillende dingen. (a) Moeder-dochter-richtlijn: EU-lidstaat van de moeder moet het dividend vrijstellen ÉN EU-lidstaat van dochter mag geen bronheffing op het dividend houden. (b) DBI-aftrek: Belgisch nationaal regime dat de richtlijn implementeert maar ook verder gaat (dividenden uit derde landen mits taxatievoorwaarde). Bij EU-dividenden: beide regimes gelden cumulatief — geen bronheffing in dochter-land + DBI-aftrek in BE.
>
> <small>🔗 Richtlijn 2011/96/EU (Moeder-dochter) — art. 4, 5 — _richtlijn_ · WIB92 — art. 202-205 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### VenB-aangifte: DBI-aftrek toepassen

_De accountant past de DBI-aftrek toe in de VenB-aangifte en bewaakt voorwaarden over meerdere jaren._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijkse voorwaarden-check per deelneming

Stap 1 — inventariseer alle ontvangen dividenden in het boekjaar; sorteer per uitkerende vennootschap. Stap 2 — per dividend: voldoet de deelneming aan participatiedrempel (10 % of 2,5 M EUR)? Stap 3 — toets houdperiode op uitkeringsdatum (al 12 maanden of verbintenis). Stap 4 — taxatievoorwaarde: is de uitkerende vennootschap niet in KB-lijst tax-haven + geen bevoorrecht regime? Stap 5 — verdeel dividenden over codes 1631 (EER-dochter Belgisch dividend), 1633 (EER-buitenlands), 1635 (andere Belgisch) of 1637 (andere buitenlands). Stap 6 — bereken DBI-aftrek + check restwinst-bottleneck.

<small>🔗 aangifte-VenB-2025-dbi-detail — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 🧭 Surplus-overdracht over meerdere jaren administreren

Houd een meerjarig DBI-overdrachtsregister bij: per AJ saldo begin + nieuwe overdracht + effectief benut + saldo einde (codes 1701-1704). Aansluiting met aangifte VenB elk jaar verifieren. Bij toekomstige verlies-tijdperken: het DBI-overschot is goud waard want het is onbeperkt overdraagbaar (sinds Cobelfret-arrest C-138/07 + Wet 21-12-2013).

<small>🔗 WIB92 — art. 205 §3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Structurering deelnemingen — DBI-eligibility optimaliseren

Bij investeringsbeslissingen: streef naar 10 %-participatie OF aanschaffingswaarde > 2,5 M EUR om DBI-eligible te zijn. Onder 10 % en onder 2,5 M EUR = geen DBI = volledig belastbaar dividend → effectieve dubbele belasting in keten. Bij grensoverschrijdende structurering: kies dochter-jurisdicties die taxatievoorwaarde halen (niet KB-lijst, geen bevoorrecht regime). Anti-misbruik: ATAD/AAMB-risico bij kunstmatige drempel-haal-structuren — substantie cruciaal.

<small>🔗 WIB92 — art. 203 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Dividend-uitkering (winstuitkering) → ⏳ dividend-uitkering _(moet-verwijzen)_
- ↪ Σ-keuzekader VenB-voordelen → [[fiscale-voordelen-vennootschap]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-voordelen-vennootschap]]
### `beinvloed_door`
- ⏳ dividend-uitkering
### `vergelijkbaar_met`
- ⏳ dividend-uitkering — DBI = ontvanger-perspectief; dividend-uitkering = betaler-perspectief. Twee kanten van dezelfde munt.
