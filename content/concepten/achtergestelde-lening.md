---
title: "Achtergestelde lening"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/achtergestelde-lening.json"
---

# Achtergestelde lening

_Instrument_

📋 Regeling · Anchors: `3.0.IV.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: subordinated loan · junior debt · subordinated debt — **Vertalingen**: fr: prêt subordonné · en: subordinated loan

## Definitie

📖 Een achtergestelde lening is een lening waarbij de schuldeiser contractueel aanvaardt dat bij vereffening of faillissement van de debiteur eerst alle andere ('gewone') schuldeisers worden betaald, en pas daarna - met het saldo dat overblijft - de achtergestelde lening. De aflossingen en interesten worden tijdens de looptijd normaal betaald, maar bij financiële problemen kunnen ze geschorst of definitief verloren worden. Boekhoudkundig blijft een achtergestelde lening vreemd vermogen, ingeschreven onder de balansrubriek 17/4 (schulden op meer dan een jaar - achtergestelde leningen).

<small>📚 CBN-advies 159/2 — Specifiek achtergestelde leningen — _cbn_ · IFRS 9 (Verordening (EU) 2023/1803) — B4.1.19 — _wettekst_</small>

## Substantie

🔗 Voor de uitlener is een achtergestelde lening risicovoller dan een gewone lening - hij staat achteraan in de rij bij faillissement. Voor de vennootschap-debiteur fungeert ze als een soort 'tussenkapitaal': andere kredietverstrekkers (banken) krijgen meer comfort omdat de achtergestelde schuldeiser hen voorgaat in betaling. Daardoor wordt het instrument vaak gebruikt om de solvabiliteitsratio op te krikken zonder aandeelhouders te dwingen formeel kapitaal in te brengen. De rente ligt typisch hoger dan bij een gewone lening - de achterstelling wordt vergoed door een rentepremie. In de praktijk verstrekken zaakvoerders, aandeelhouders of de moedervennootschap deze leningen, vaak met een dubbele functie: financiering én signaal van vertrouwen tegenover externe kredietverleners.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De achterstelling is een contractuele constructie die de rangorde van schuldeisers herschikt. In het Belgische faillissementsrecht gelden bevoorrechte schuldeisers, gewone schuldeisers en in laatste instantie de aandeelhouders. Door zich vrijwillig in te schrijven onder de aandeelhouders maar nog boven hen, creëert de achtergestelde schuldeiser een tussenlaag. Voor het vennootschapsrecht blijft het juridisch een schuld - terugbetaling is afdwingbaar tegen de vennootschap als ze niet in financiële problemen verkeert. Voor het solvabiliteitsoordeel van banken en ratingbureaus telt het echter mee als 'quasi-eigen vermogen': de hogere rangorde van de bank wordt door de achterstelling waargemaakt.

<small>📚 CBN-advies 159/2 — Specifiek achtergestelde leningen - functie en balansplaatsing — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Algemeen contractenrecht (BW) + boekhoudreglementering (KB 29-04-2019 op de jaarrekening - rekening 17/4)

**✅ Voor**
- 🔗 Versterken van de solvabiliteit van een KMO zonder formele kapitaalverhoging: typisch wanneer een bank een minimumsolvabiliteit eist voor een investeringskrediet en de aandeelhouders een lening verstrekken in plaats van kapitaal in te brengen.
- 🔗 Brug-financiering: tijdelijke financiering tijdens een overname of herstructurering, waarbij banken vereisen dat een deel van de financiering achtergesteld is op hun eigen kredieten.

**👍 Voordeel**
- 🔗 Voor de vennootschap: hogere solvabiliteit zonder kapitaalverhoging (geen statutenwijziging, geen verwatering van bestaande aandeelhouders). Rente blijft fiscaal aftrekbaar (binnen de grenzen van art. 198/1 WIB92). Flexibel: meestal vrij vroeg afbetaalbaar zodra de bank dat toelaat.

**⚠️ Risico**
- 🔗 Voor de uitlener: bij faillissement van de vennootschap krijgt hij wellicht niets terug. Bij een zaakvoerder of aandeelhouder die zelf de lening verstrekte, kan dat zijn persoonlijke vermogen treffen.
- 🔗 Herkwalificatie-risico: een lening van een zaakvoerder of aandeelhouder kan door de fiscus geherkwalificeerd worden als dividend onder art. 18 WIB92 wanneer de rente of de hoofdsom-omvang excessief is in verhouding tot het kapitaal (thin-cap-regels) of wanneer de werkelijke aard van de verrichting eerder op inbreng dan op lening wijst.

## Bouwstenen

### 💡 Balansrubriek 17/4 - Achtergestelde leningen  
_`begrip`_

📖 Een achtergestelde lening met algemene achterstelling (= ten gunste van alle schuldeisers) wordt op het passief geboekt onder rubriek VIII.A.1 'Achtergestelde leningen' (rekening 17/4). Bij specifieke achterstelling - enkel ten gunste van één of meer met naam genoemde schuldeisers - moet volgens CBN 159/2 het criterium van art. 8 van het jaarrekeningbesluit gevolgd worden: inschrijven onder die rubriek die voor het voorgelegde geval het meest passend is. Dat is dan typisch een 'andere lening' onder rubriek VIII.B-D, niet 17/4.

<small>📚 CBN-advies 159/2 — Specifiek achtergestelde leningen — _cbn_ · KB 29-04-2019 jaarrekening — MAR rubriek 17/4 — _kb_</small>

### ⚙️ Algemene vs specifieke achterstelling  
_`mechanisme`_

📖 Bij algemene achterstelling treedt de schuldeiser terug ten opzichte van álle huidige en toekomstige schuldeisers van de debiteur: hij komt pas aan bod nadat iedereen anders betaald is. Bij specifieke achterstelling treedt hij enkel terug ten opzichte van met naam genoemde schuldeisers of voor welbepaalde vorderingen - bv. enkel ten gunste van de hoofdbankier. Tussen beide ligt een aanzienlijk verschil in risicoprofiel en in solvabiliteitswaarde voor derden: alleen algemene achterstelling versterkt het beeld van een 'quasi-eigen-vermogen-laag'.

<small>📚 CBN-advies 159/2 — Onderscheid algemene vs beperkte achterstellingsclausule — _cbn_</small>

### 📜 Blijft juridisch vreemd vermogen  
_`regel`_

📖 Hoeveel zekerheid een achtergestelde lening ook biedt aan andere schuldeisers, juridisch blijft ze een schuldvordering. De schuldeiser behoudt contractuele rechten op aflossing en rentebetaling. De vennootschap moet de schuld erkennen op de passiefzijde. Een achtergestelde lening is dus geen eigen vermogen voor het WVV (geen aandelen, geen stemrecht) en geen eigen vermogen voor de jaarrekening (geen rubriek IV-VI). Wel kan ze in bepaalde solvabiliteitsbeoordelingen (bancaire ratio's, ratingmethodologieën) als 'quasi-eigen vermogen' meetellen.

<small>📚 IFRS 9 (Verordening (EU) 2023/1803) — B4.1.19 — _wettekst_</small>

### ⚠️ Fiscale herkwalificatie rente -> dividend (art. 18 WIB92)  
_`risico`_

📖 Wanneer een lening verstrekt is door een bedrijfsleider of een aandeelhouder, en de rente overschrijdt de marktrente of de schuld-/kapitaalverhouding bepaalde grenzen, kan de fiscus de excessieve rente herkwalificeren als dividend (art. 18, 4° WIB92). Gevolgen: rente niet meer aftrekbaar voor de vennootschap, wel onderworpen aan roerende voorheffing als dividend bij de uitlener. De grens 'rente vs dividend' moet bij elke aandeelhouderslening expliciet getoetst worden bij opname én bij ratevolatiliteit.

<small>📚 WIB92 — art. 18, 4° — _wettekst_</small>

### 📜 Thin-cap en financieringskostensurplus (art. 198/1 WIB92)  
_`regel`_

📖 De algemene aftrekbaarheidsbeperking voor financieringskostensurplus (art. 198/1 WIB92, omzetting van ATAD) geldt ook voor de rente op achtergestelde leningen. De interestaftrek wordt beperkt tot het hoogste van 3 miljoen EUR of 30% van het fiscaal EBITDA. Niet-aftrekbare interesten kunnen overgedragen worden in de tijd of (via een interestaftrekovereenkomst onder art. 198/1 §4) binnen de groep. Renteoverdrachten en groepsovereenkomsten moeten gedocumenteerd worden.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Financieringskostensurplus + interestaftrekovereenkomst — _cbn_</small>

## Voorbeelden

### 💡 Solvabiliteit verhogen voor een bankkrediet 🔗

_BV Optima wil een investeringskrediet van 500.000 EUR aangaan voor een nieuwe productielijn. Haar huidige eigen vermogen bedraagt 200.000 EUR; haar balanstotaal 800.000 EUR. Solvabiliteitsratio = 200/800 = 25%. De bank vraagt minstens 35%. De aandeelhouders willen geen kapitaalverhoging._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "Stap 1 - aandeelhouders verstrekken een achtergestelde lening van 100.000 EUR aan BV Optima, contractueel achtergesteld op alle bestaande en toekomstige schuldeisers.",
    "Stap 2 - balansboeking: D 55 Bank | C 174 Achtergestelde leningen 100.000 EUR.",
    "Stap 3 - solvabiliteit zoals bekeken door de bank: eigen vermogen 200 + achtergestelde lening 100 = 300 quasi-eigen-vermogen. Op een (verhoogd) balanstotaal van 900: 300/900 = 33,3%.",
    "Stap 4 - bank kan eventueel akkoord gaan (afhankelijk van precieze methodologie); zonder de achtergestelde lening zou een formele kapitaalverhoging van 100.000 EUR nodig zijn (statutenwijziging, notaris, ...).",
    "Stap 5 - belangrijk: rente op de achtergestelde lening moet aan marktconforme rentevoet zijn om herkwalificatie naar dividend (art. 18 WIB92) te voorkomen."
  ],
  "resultaat": "Solvabiliteitsdoel bereikt zonder kapitaalverhoging. Wel: rente fiscaal binnen 198/1-perimeter en geen herkwalificatie-risico."
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Achtergestelde lening = eigen vermogen

**Verkeerde assumptie**: Een achtergestelde lening telt mee als eigen vermogen op de balans van de vennootschap.

**Kernpunt**: Boekhoudkundig blijft een achtergestelde lening vreemd vermogen, geboekt onder rubriek VIII.A.1 (rekening 17/4). De achterstelling verandert de RANGORDE bij vereffening, niet de aard van de post. Voor het WVV (kapitaalbescherming, alarmbel) telt het niet mee als eigen vermogen of als 'inbreng'. Wel kan een bank of ratingbureau het bij hun eigen analyse als quasi-eigen-vermogen meerekenen.

<small>📚 CBN-advies 159/2 — Specifiek achtergestelde leningen - balansplaatsing onder schulden — _cbn_</small>

### ⚠️ Aandeelhouderslening = altijd vrij van fiscale impact

**Verkeerde assumptie**: Aandeelhouders kunnen onbeperkt rente vragen op een achtergestelde lening aan hun vennootschap.

**Kernpunt**: Art. 18, 4° WIB92 herkwalificeert excessieve rente als dividend. Twee criteria: (1) marktconforme rentevoet; (2) verhouding lening/kapitaal binnen redelijke grenzen. Wanneer een aandeelhouder bv. 10.000 EUR kapitaal heeft en 500.000 EUR achtergestelde lening aan 8% verstrekt, riskeert het volledige bedrag boven een redelijke schuld/kapitaal-ratio plus de rente daarop dividend-herkwalificatie. Gevolg: niet-aftrekbare rente + roerende voorheffing.

<small>📚 WIB92 — art. 18, 4° — _wettekst_</small>

### ⚠️ Algemene en specifieke achterstelling als hetzelfde behandelen

**Verkeerde assumptie**: Achterstelling is achterstelling - de balansrubriek is altijd 17/4.

**Kernpunt**: Volgens CBN 159/2 is dit alleen correct voor algemene achterstelling (ten gunste van alle schuldeisers). Bij specifieke achterstelling (enkel ten gunste van bv. één bank) moet de lening worden ingeschreven onder de rubriek die het beste het werkelijke karakter weergeeft - typisch een gewone 'andere lening'. De toelichting bij de jaarrekening moet de aard van de achterstelling verduidelijken voor de lezer.

<small>📚 CBN-advies 159/2 — Onderscheid algemene/specifieke achterstelling - rubricering — _cbn_</small>

## Accountant-perspectieven

### Debiteur-vennootschap

_De accountant die de boekhoudkundige en fiscale verwerking van een achtergestelde lening bij de cliënt-vennootschap begeleidt._

#### 🧭 Adviseur

##### 📜 Afweging financieringsmix - kapitaal vs achtergestelde lening  
_`regel`_

🔗 Bij een verzoek tot bijkomende eigen middelen voor solvabiliteitsverbetering: weeg af tussen (1) een formele kapitaalverhoging - notariskosten, statutenwijziging, geen aftrekbare rente, maar volledig eigen vermogen; (2) een achtergestelde lening - lichte formaliteit, aftrekbare rente, maar herkwalificatie-risico en juridisch nog steeds schuld. Aandachtspunten bij keuze achtergestelde lening: marktconforme rente, redelijke schuld/kapitaal-ratio, schriftelijke overeenkomst met expliciete achterstellingsclausule, en wettelijke documentatie van de marktconformiteit (transfer pricing bij groepsfinanciering).

<small>📚 WIB92 — art. 18, 4° — _wettekst_ · WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boeking opname en rentebetaling  
_`stap`_

🔗 Opname: D 55 Bank | C 174 Achtergestelde leningen (algemene achterstelling) of relevante andere rubriek (specifieke achterstelling). Jaarlijkse rentebetaling: D 65 Financiële kosten | C 55 Bank. Bij aandeelhouderslening: roerende voorheffing op rente toepassen (in beginsel 30%); aangifte 273 indienen. Bij groepslening: documenteer marktconformiteit (benchmark-studie of vergelijkbare bancaire offerte).

<small>📚 KB 29-04-2019 jaarrekening — MAR rubriek 17/4 + rekening 65 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Banklening - primaire vergelijking als 'gewone' financiering → [[banklening-investeringskrediet]] _(moet-verwijzen)_
- → Obligatielening - alternatief instrument met effecten-statuut → [[obligatielening]] _(moet-verwijzen)_
- → Eigen vermogen - afbakening (achtergestelde lening = nog steeds vreemd vermogen) → [[eigen-vermogen]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ lening
### `vergelijkbaar_met`
- [[banklening-investeringskrediet]]
    - **Gelijkenissen**:
        - Beide zijn schulden op meer dan een jaar, contractueel afspraak tussen vennootschap en kredietverlener
        - Beide genereren aftrekbare interestlasten binnen de grenzen van art. 198/1 WIB92
    - **Verschillen**:
        - Bankleningen zijn 'gewoon' geprivilegieerd of pari passu; achtergestelde lening staat achteraan in de rij
        - Bankleningen worden door kredietinstellingen verstrekt; achtergestelde leningen vaak door aandeelhouders/zaakvoerders/moedervennootschap
        - Bankleningen tellen niet als quasi-eigen vermogen; achtergestelde lening wel (in beoordelingen door derden)
        - Bankleningen hebben strikte covenants; achtergestelde leningen typisch soepeler maar met hogere rente
    - ⚠️ **Verwarringsrisico**: Beide staan onder rubriek VIII (schulden op meer dan een jaar). Verwar 17/4 (achtergesteld) niet met 17/0 (gewone bankleningen).
- [[obligatielening]]
    - **Gelijkenissen**:
        - Beide zijn vreemd vermogen op meer dan een jaar
        - Beide kunnen achtergesteld of niet-achtergesteld zijn
    - **Verschillen**:
        - Obligatielening is een effecten-instrument, verhandelbaar, doorgaans aan meerdere investeerders uitgegeven
        - Achtergestelde lening is een bilaterale contractuele relatie, meestal niet-verhandelbaar
        - Obligatielening kent vaste coupons en aflossingsschema in effecten-vorm; achtergestelde lening in beginsel vrije contractuele modaliteiten
    - ⚠️ **Verwarringsrisico**: Een achtergestelde obligatielening combineert beide concepten - in dat geval geldt het regime van de obligatielening plus de achterstellingsclausule.
### `beinvloed_door`
- [[eigen-vermogen]] — Een achtergestelde lening verhoogt het 'quasi-eigen vermogen' zoals beoordeeld door externe partijen, maar telt voor het juridische eigen-vermogen-begrip (WVV) niet mee.
