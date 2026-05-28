---
title: "Eigen vermogen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.IV.A
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/eigen-vermogen.json"
---

# Eigen vermogen

_Balanspost_

🏢 Entiteit · Anchors: `3.0.IV.A` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: EV — **Synoniemen**: equity · kapitalen en reserves · shareholders' equity — **Vertalingen**: fr: capitaux propres

## Definitie

📖 Het eigen vermogen (EV) is het deel van het balans-totaal dat toekomt aan de eigenaars (aandeelhouders) van de vennootschap. Boekhoudkundig: het verschil tussen het totaal der activa en het totaal der schulden (passiva-zijde = vreemd vermogen + EV). Het EV wordt op de balans (passiva-zijde) gepresenteerd in zes rubrieken op rekeningen klasse 1 (10-15) volgens KB MAR + WVV art. 3:89: I. Kapitaal/Inbreng (10/11), II. Uitgiftepremies (11 in NV), III. Herwaarderingsmeerwaarden (12), IV. Reserves (13: wettelijke, onbeschikbare, beschikbare, belastingvrije), V. Overgedragen winst/verlies (14), VI. Kapitaalsubsidies (15). Sinds WVV (2019) heeft de BV geen kapitaal meer (vervangen door 'inbreng buiten kapitaal' op rekening 110-111).

<small>📚 WVV — art. 3:89 — _wettekst_ · KB MAR (KB 29 april 2019) — Klasse 1 rekeningen 10-15 — _kb_ · WVV — art. 5:1-5:5 — _wettekst_</small>

## Substantie

🔗 Economisch: het eigen vermogen is de 'buffer' tussen de vennootschap en haar crediteurs. Een groot EV beschermt schuldeisers (meer dekking bij vereffening) en wordt door financiers gewaardeerd als solvabiliteits-indicator. De solvabiliteitsratio (EV / totaal passief) geeft de structurele financiële gezondheid weer — typisch streven: > 30-40% voor stabiel bedrijf, > 50% voor cyclisch of risicodragend bedrijf. Het EV beweegt door: (a) **inbrengen** — kapitaalverhogingen in geld of natura; (b) **resultaten** — winsten verhogen EV (via reserves of overgedragen resultaat), verliezen verlagen EV; (c) **uitkeringen** — dividenden en kapitaalverminderingen verlagen EV; (d) **herwaarderingen** — vaste activa kunnen worden geherwaardeerd met tegenboeking in herwaarderingsmeerwaarden (rekening 12, onbeschikbaar tot realisatie).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 De boekhoudkundige presentatie en de wettelijke regels rond eigen vermogen (onbeschikbare reserves, uitkeringsbeperkingen, alarmbel) dienen ÉÉN doel: schuldeisersbescherming. De aandeelhouders mogen niet eenzijdig 'de pot leegmaken' door dividenden of kapitaalverminderingen wanneer dit schuldeisers in gevaar brengt. Vandaar de gelaagde uitkerings-tests: in BV de dubbele test (netto-actief-test EN liquiditeitstest art. 5:142-143); in NV de netto-actief-test (art. 7:212). De alarmbel-procedure (5:153/7:228) verplicht het bestuur tot actief ingrijpen wanneer EV onder kritieke drempel daalt — geen wachten tot faillissement.

<small>📚 WVV — art. 5:142 — _wettekst_ · WVV — art. 5:143 — _wettekst_ · WVV — art. 5:153 — _wettekst_ · WVV — art. 7:212 — _wettekst_ · WVV — art. 7:228 — _wettekst_</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV (Wet 23 maart 2019) + KB MAR (KB 29 april 2019); WIB92 art. 184 voor fiscaal EV-concept.

WVV-hervorming heeft BV-kapitaal afgeschaft. NV behoudt kapitaalconcept. WIB92 art. 537 (notionele-interestaftrek) bevroren sinds AJ 2020, definitief afgeschaft AJ 2024.

**✅ Voor**
- 📖 Eigen-vermogen-rubriek aanwezig in elke entiteit met dubbele boekhouding: BV, NV, CV, CommV, VOF, VZW (vanaf middelgroot), stichting (vanaf middelgroot). Geen EV op balans bij vereenvoudigde boekhouding (kleine vereniging of natuurlijk persoon zonder dubbele boekhouding-verplichting).

**⚠️ Risico**
- 📖 Alarmbel-triggers bij eigen-vermogen-daling: **BV (art. 5:153)** — bestuursorgaan moet binnen 2 maanden buitengewone AV bijeenroepen wanneer (a) nettoactief negatief dreigt of geworden is, OF (b) niet voldaan aan liquiditeitstest voor de komende 12 maanden. **NV (art. 7:228)** — bijeenroeping verplicht wanneer (a) nettoactief gedaald onder helft van het kapitaal (alarmbel-1) of onder een vierde (alarmbel-2), OF (b) onder het wettelijk minimumkapitaal van 61.500 EUR. Niet-naleving = vermoeden van fout in geval van later faillissement (art. XX.225 WER) → bestuurdersaansprakelijkheid.

## Sub-concepten

### 📦 Kapitaal (NV) / Inbreng (BV-CV)  
_`balanspost` (subconcept)_

#### Definitie

📖 **NV — Kapitaal (rekening 10)**: nominale waarde van de uitgegeven aandelen, vast bedrag dat statutair is bepaald. Minimum 61.500 EUR (art. 7:2 WVV). Onderscheid:
- *Geplaatst kapitaal*: het bedrag waarvoor aandelen zijn uitgegeven (bv. 1.000 aandelen × 100 EUR = 100.000 EUR).
- *Onbeschikbaar kapitaal*: niet uitkeerbaar als dividend (onaantastbaar voor schuldeisersbescherming).
- *Gestort vs niet-opgevraagd*: aandeelhouders moeten minstens 1/4 storten + volledige volstorting bij oprichting voor natura-inbreng (art. 7:11). Niet-opgevraagd kapitaal staat als afzonderlijke rekening 101 'Niet-opgevraagd kapitaal' (correctie debet op activa-zijde).

**BV/CV — Inbreng (rekening 110/111)**: sinds WVV is er GEEN kapitaal meer in BV/CV. Inbrengen worden geboekt op rekening 110 'Beschikbare inbreng' (vrij uitkeerbaar mits dubbele test) en 111 'Onbeschikbare inbreng' (statutair beschermd). De statuten bepalen of inbrengen 'beschikbaar' of 'onbeschikbaar' zijn — flexibiliteit van WVV.

**Fiscaal kapitaal (WIB92 art. 184)**: het fiscaal kapitaal is een AFZONDERLIJK concept. Voor de fiscus is 'kapitaal' = werkelijk volgestort kapitaal/inbreng dat fiscaal ook als kapitaal kwalificeert. Belang: dividenden ten laste van fiscaal kapitaal = belastingvrij (geen RV — kapitaalvermindering, art. 18 1°). Dividenden ten laste van reserves/uitgiftepremies (zonder fiscale kapitaal-kwalificatie) = wel RV (30% of 15%).

<small>📚 WVV — art. 7:2 — _wettekst_ · WVV — art. 5:1-5:5 — _wettekst_ · KB MAR — Rekening 10 (NV) + 110/111 (BV-CV) — _kb_ · WIB92 — art. 184 — _wettekst_</small>

### 📦 Uitgiftepremies (rekening 11)  
_`balanspost` (subconcept)_

#### Definitie

📖 Het verschil tussen de emissieprijs en de nominale (of fractie-)waarde van uitgegeven aandelen — alleen relevant in NV (in BV is alles 'inbreng' op 110/111). Bv. NV emitteert 1.000 nieuwe aandelen met nominale waarde 100 EUR aan emissieprijs 150 EUR: kapitaal stijgt 100.000 EUR (rekening 100); uitgiftepremie 50.000 EUR (rekening 11).

**Status**: in principe onbeschikbaar zoals kapitaal — niet uitkeerbaar als dividend tenzij omzetting naar reserves of incorporatie in kapitaal door statutenwijziging. **Fiscaal**: kwalificeert als 'fiscaal kapitaal' onder voorwaarden van art. 184 WIB92 (volgestort, blokkering, ...), dus kan via kapitaalvermindering belastingvrij worden teruggegeven.

<small>📚 KB MAR — Rekening 11 Uitgiftepremies — _kb_ · WIB92 — art. 184 — _wettekst_</small>

### 📦 Herwaarderingsmeerwaarden (rekening 12)  
_`balanspost` (subconcept)_

#### Definitie

📖 Niet-gerealiseerde meerwaarden op vaste activa die door herwaardering worden geboekt (bv. herwaardering onroerend goed van 500.000 EUR naar 750.000 EUR → herwaarderingsmeerwaarde 250.000 EUR rekening 12). Onbeschikbaar tot realisatie: zolang het actief niet verkocht of afgeschreven is, mag deze meerwaarde NIET worden uitgekeerd. Bij realisatie (verkoop): overboeking naar beschikbare reserves of resultaat. Bij afschrijving: jaarlijkse overboeking pro rata van de afschrijving van de meerwaarde naar resultaat.

Fiscaal: in principe belastbaar in jaar van realisatie. Voor materieel/immaterieel vast actief: gespreide-belasting-regime mogelijk (art. 47 WIB92 — herinvesteringsverplichting binnen 3-5 jaar).

<small>📚 KB MAR — Rekening 12 Herwaarderingsmeerwaarden — _kb_ · WIB92 — art. 47 — _wettekst_</small>

### 📦 Reserves (rekening 13)  
_`balanspost` (subconcept)_

#### Definitie

📖 Geaccumuleerde winsten die door AV-besluit zijn 'gereserveerd' (niet uitgekeerd) — versterken de financiële basis. Subcategorieën:

**Wettelijke reserve (rekening 130)**: verplichte reservering van 5% van de jaarwinst tot de wettelijke reserve 10% van het kapitaal heeft bereikt (NV: art. 7:211; BV: niet verplicht onder WVV — afgeschaft met afschaffing kapitaal). Onbeschikbaar tot opname als kapitaal of bij speciale wettelijke uitzondering.

**Onbeschikbare reserves (rekening 131)**: door statuten of AV-besluit onbeschikbaar verklaard. Niet uitkeerbaar zonder statutenwijziging. Vaak gebruikt voor 'reserve eigen aandelen' (verplicht bij inkoop eigen aandelen, art. 7:215/5:147).

**Beschikbare reserves (rekening 133)**: vrije reserves; AV kan beslissen ze om te zetten in dividend of kapitaal.

**Belastingvrije reserves (rekening 132)**: fiscaal vrijgestelde reserves (bv. investeringsreserve onder bepaalde voorwaarden, gespreide belasting meerwaarden). Geen RV bij uitkering. Maar 'belastingvrij' = voorwaardelijk: bij uitkering of overdracht aan eigen vermogen kunnen ze alsnog belastbaar worden.

**Liquidatiereserve (afzonderlijk in 133/13 onderverdeling)**: vanaf AJ 2014/2015 mogelijk — vennootschap betaalt 10% afzonderlijke aanslag (art. 219quater WIB92) en de gereserveerde winst kan later worden uitgekeerd aan 5% RV (in plaats van 30%) na 5 jaar houden, of 0% bij liquidatie.

<small>📚 WVV — art. 7:211 — _wettekst_ · KB MAR — Rekening 130-133 — _kb_ · WIB92 — art. 219quater — _wettekst_</small>

### 📦 Overgedragen winst / verlies (rekening 14)  
_`balanspost` (subconcept)_

#### Definitie

📖 Rekening 14 'Overgedragen resultaat' = cumulatieve niet-bestemde winsten/verliezen van vorige boekjaren. Bij positief saldo: 'overgedragen winst' (uitkeerbaar onder uitkerings-tests). Bij negatief saldo: 'overgedragen verlies' (vermindert eigen vermogen direct — verliescompensatie via toekomstige winsten).

Alternatief bij groot overgedragen verlies: kapitaalvermindering ter zuivering van het verlies (boekhoudkundig 'sanering') — het kapitaal wordt verminderd en het verlies geschrapt; geen werkelijke uitgave aandeelhouders. Wel formeel statutenwijziging vereist (NV) of inbreng-vermindering (BV art. 5:144).

<small>📚 KB MAR — Rekening 14 — _kb_ · WVV — art. 5:144 — _wettekst_</small>

### 📦 Kapitaalsubsidies (rekening 15)  
_`balanspost` (subconcept)_

#### Definitie

📖 Investeringssubsidies van overheid (Vlaanderen-VLAIO, regio-subsidies) ter financiering van vaste activa. Geboekt op rekening 15 'Kapitaalsubsidies'. Worden pro rata van de afschrijvingsperiode van het gesubsidieerde actief overgeboekt naar resultaat (rekening 753 'Kapitaal- en interestsubsidies'). Fiscaal: in principe belastbaar — maar bepaalde investeringssubsidies zijn vrijgesteld (art. 193 WIB92 onder voorwaarden — gewest-onderzoek-subsidies bv.).

<small>📚 KB MAR — Rekening 15 + 753 — _kb_ · WIB92 — art. 193 — _wettekst_</small>

## Bouwstenen

### ⚙️ Bewegingen in eigen vermogen  
_`mechanisme`_

🔗 Wat doet EV toenemen of afnemen tijdens een boekjaar?

**Toename (EV ↑)**:
- Kapitaalverhoging in geld of natura — nieuwe aandeelhouders of bestaande die bijstorten. Boeking: 550/22 debet, 100/110 + 11 credit.
- Winst van boekjaar (na bestemming) → reserves of overgedragen winst. Boeking: 69 'Resultaat te bestemmen' debet, 13/14 credit.
- Herwaardering vast actief (toename economische waarde) → rekening 12.
- Kapitaalsubsidie ontvangen — rekening 15.
- Inkoop eigen aandelen (zelden, technisch-balans-neutraal — vermindert vrije reserves via creatie 'onbeschikbare reserve eigen aandelen').

**Afname (EV ↓)**:
- Verlies van boekjaar → overgedragen verlies (rekening 14).
- Dividenduitkering (na AV-besluit) — rekening 694 debet, 471 credit voor brutobedrag.
- Kapitaalvermindering (terugbetaling aandeelhouders, of zuivering verlies) — rekening 100/110 debet.
- Tantième aan bestuurders ten laste van het resultaat (rekening 695).
- Realisatie en uitkering belastingvrije reserves zonder vrijstelling.

<small>📚 KB MAR — Klasse 1 + klasse 69 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Uitkerings-tests (BV-dubbele vs NV-enkelvoudige)  
_`regel`_

📖 **BV — dubbele test** (WVV art. 5:142-143):
1. **Netto-actief-test** (art. 5:142): geen uitkering toegelaten indien het netto-actief negatief is of door de uitkering negatief zou worden. Netto-actief = totaal activa − totaal vreemd vermogen − schulden − niet-aftrekbare reserves.
2. **Liquiditeits-test** (art. 5:143): het bestuursorgaan stelt vóór elke uitkering vast dat de vennootschap, op grond van de redelijkerwijze te verwachten ontwikkelingen, in staat zal blijven gedurende ten minste de twaalf volgende maanden haar opeisbare schulden te betalen. Verplichte rapportering in een notulen-stuk dat bij de jaarrekening wordt neergelegd.

**NV — enkelvoudige netto-actief-test** (art. 7:212): geen uitkering indien netto-actief, na uitkering, daalt onder het bedrag van het volgestorte kapitaal + onbeschikbare reserves (wettelijke + statutaire + reserve eigen aandelen + ...).

**Schending van test → bestuurdersaansprakelijkheid**: art. 5:144 BV / 7:214 NV — bestuurders hoofdelijk aansprakelijk voor uitkering die de tests niet doorstaat, ook al was AV-besluit aanwezig.

<small>📚 WVV — art. 5:142 — _wettekst_ · WVV — art. 5:143 — _wettekst_ · WVV — art. 5:144 — _wettekst_ · WVV — art. 7:212 — _wettekst_ · WVV — art. 7:214 — _wettekst_</small>

### 💡 Fiscaal eigen vermogen vs boekhoudkundig eigen vermogen  
_`begrip`_

📖 Twee parallelle EV-concepten:

**Boekhoudkundig EV** = rekeningen 10-15 in jaarrekening. Onderworpen aan KB MAR + WVV. Doel: weergave aan stakeholders.

**Fiscaal EV** (WIB92 art. 184 + 537) = subset van boekhoudkundig EV dat fiscaal als 'kapitaal' kwalificeert. Inclusief:
- Volgestort kapitaal/inbreng (en uitgiftepremies indien aan voorwaarden voldaan).
- Reserves die in eerdere boekjaren werden 'omgezet in kapitaal' bij statutenwijziging.
- Liquidatiereserve (5% RV-regime — apart fiscaal regime).

NIET fiscaal kapitaal:
- Belastingvrije reserves (afzonderlijk fiscaal regime).
- Gewone beschikbare reserves uit eerdere winsten (deze zijn al belast in vennootschapsbelasting; bij uitkering nog 30% RV in privé-handen).

**Belang**: bij kapitaalvermindering (uitkering uit fiscaal kapitaal) → geen RV. Bij dividenduitkering uit reserves → wel RV (30% of 15%).

**Notionele-interestaftrek (afgeschaft)**: art. 537 WIB92, ook genaamd 'aftrek voor risicokapitaal'. Berekend op 'aangepast eigen vermogen' (= boekhoudkundig EV gecorrigeerd voor o.a. eigen aandelen, niet-fiscaal-kapitaal-elementen). Bevroren AJ 2020, definitief afgeschaft AJ 2024.

<small>📚 WIB92 — art. 184 — _wettekst_ · WIB92 — art. 537 — _wettekst_</small>

### 🧮 Solvabiliteits-context (EV / totaal passief)  
_`formule`_

🔗 Solvabiliteitsratio = Eigen Vermogen / Totaal Passief (× 100 = %). Geeft de structurele financiële sterkte weer.

- < 20%: zwakke solvabiliteit, hoge afhankelijkheid van schuldfinanciering, kwetsbaar bij economische schokken.
- 20-30%: gemiddeld, normaal voor groei-bedrijven met externe financiering.
- 30-50%: gezond, comfortabele buffer.
- > 50%: zeer sterk, mogelijk te conservatief gefinancierd (suboptimale ROE).

**Schuldratio** = inverse: totaal vreemd vermogen / totaal passief.

**Working capital-link**: positief EV is geen garantie op liquiditeit. Werkkapitaal-analyse (current ratio, quick ratio) loopt parallel.

**Bancair gebruik**: banken hanteren solvabiliteit als kredietratio bij beoordeling van leningsaanvragen. Onder 15-20% solvabiliteit weigeren vele commerciële banken nieuwe kredieten zonder bijkomende waarborgen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Eigen-vermogen-balans BV — voor en na dividend 🔗

_BV Gamma boekjaar 2025: balans-totaal 800.000 EUR. EV-componenten: inbreng 200.000 (rekening 110); wettelijke reserve afgeschaft (BV); beschikbare reserves 120.000 (rekening 133); overgedragen winst 80.000 (rekening 14); kapitaalsubsidie 30.000 (rekening 15). Totaal EV = 430.000 EUR. Schulden = 370.000 EUR. AV beslist dividend 50.000 EUR uit overgedragen winst._

**Balans-snapshot**: ``

```json
{
  "moment": "Vóór dividenduitkering",
  "passiva": [
    {
      "post": "110 Inbreng",
      "bedrag": 200000
    },
    {
      "post": "133 Beschikbare reserves",
      "bedrag": 120000
    },
    {
      "post": "14 Overgedragen winst",
      "bedrag": 80000
    },
    {
      "post": "15 Kapitaalsubsidies",
      "bedrag": 30000
    },
    {
      "post": "Totaal Eigen Vermogen",
      "bedrag": 430000
    },
    {
      "post": "Vreemd vermogen",
      "bedrag": 370000
    },
    {
      "post": "Totaal passief",
      "bedrag": 800000
    }
  ]
}
```

**Stap 1 — uitkerings-tests (art. 5:142-143):**
- *Netto-actief-test*: 430.000 - 50.000 = 380.000 EUR — nog steeds positief. ✅
- *Liquiditeits-test*: bestuur stelt vast dat BV Gamma haar opeisbare schulden 12m kan blijven betalen na uitkering. Notulen-stuk opgesteld. ✅

**Stap 2 — Boekingen:**
1. Toekenning dividend (AV-besluit): 14 'Overgedragen winst' debet 50.000 / 471 'Te betalen dividenden' credit 50.000.
2. Inhouding RV (30% — geen VVPRbis): 471 debet 50.000 / 453 'Ingehouden voorheffingen' credit 15.000 / 550 'Bank' credit 35.000.

**Balans-snapshot**: ``

```json
{
  "moment": "Na dividenduitkering",
  "passiva": [
    {
      "post": "110 Inbreng",
      "bedrag": 200000
    },
    {
      "post": "133 Beschikbare reserves",
      "bedrag": 120000
    },
    {
      "post": "14 Overgedragen winst",
      "bedrag": 30000,
      "toelichting": "Was 80.000, daalt met 50.000 dividend"
    },
    {
      "post": "15 Kapitaalsubsidies",
      "bedrag": 30000
    },
    {
      "post": "Totaal Eigen Vermogen",
      "bedrag": 380000
    },
    {
      "post": "Vreemd vermogen",
      "bedrag": 370000
    },
    {
      "post": "Doorstortbare RV",
      "bedrag": 15000
    },
    {
      "post": "Totaal passief",
      "bedrag": 765000
    }
  ]
}
```

**Solvabiliteitsratio**:
- Vóór: 430.000 / 800.000 = 53,75%.
- Na: 380.000 / 765.000 = 49,67%.

Nog steeds zeer gezond (> 30%). Dividenduitkering heeft de solvabiliteit licht verminderd maar geen alarmbel-issue.

<small>📚 WVV — art. 5:142 — _wettekst_ · WVV — art. 5:143 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 NV alarmbel — netto-actief gedaald onder helft kapitaal 🔗

_NV Delta heeft kapitaal 200.000 EUR (rekening 100). Door opeenvolgende verliezen in 2024 en 2025: overgedragen verlies -120.000 EUR (rekening 14). EV = 200.000 - 120.000 = 80.000 EUR._

**Alarmbel-toets art. 7:228 WVV**:

- Helft kapitaal = 200.000 / 2 = 100.000 EUR.
- Netto-actief 80.000 < 100.000 → **Alarmbel-1 getriggerd**.
- Een kwart kapitaal = 50.000 EUR.
- Netto-actief 80.000 > 50.000 → Alarmbel-2 NIET getriggerd (nog niet).

**Wettelijke verplichting bestuursorgaan**:
1. Binnen **2 maanden** na vaststelling: bijeenroeping buitengewone AV.
2. AV beraadslagen over: (a) ontbinding vennootschap, OF (b) saneringsmaatregelen.
3. Verplicht bijzonder verslag bestuur — toelichting van de toestand + voorgestelde maatregelen.

**Saneringsmaatregelen typisch**:
- Kapitaalverhoging — nieuwe inbreng van aandeelhouders.
- Kapitaalvermindering ter zuivering van het verlies (formaliteit zonder cash-effect).
- Kostenbesparingsplan + business-pivot.
- Conversie schulden naar kapitaal door geldschieters.

**Niet-naleving** alarmbel-procedure = vermoeden van fout in faillissementsaansprakelijkheid (art. XX.225 WER) → bestuurders persoonlijk aansprakelijk voor netto-passief.

**Boeking:**


Resultaat: na sanering kapitaal = 200.000 - 100.000 + 150.000 = 250.000 EUR; overgedragen verlies = -120.000 + 100.000 = -20.000 EUR; EV = 250.000 - 20.000 = 230.000 EUR. Helft van kapitaal = 125.000 < EV 230.000 → alarmbel opgeheven. Volgt notariële akte kapitaalvermindering + kapitaalverhoging + statutenwijziging.

<small>📚 WVV — art. 7:228 — _wettekst_ · WER — art. XX.225 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Solvabiliteitsratio — interpretatie en bancair gebruik 🔗

_Drie KMO's met verschillende kapitaalstructuren — vergelijking solvabiliteitsratio en banking-impact._

| Bedrijf | EV | Schulden | Totaal passief | Solvabiliteit | Beoordeling |
| --- | --- | --- | --- | --- | --- |
| BV A (start-up) | 50.000 | 450.000 | 500.000 | 10% | Zwak — bancair kredietverlening moeilijk zonder borg |
| BV B (gevestigd) | 300.000 | 700.000 | 1.000.000 | 30% | Gezond — normale bancaire voorwaarden |
| NV C (familie-holding) | 1.500.000 | 500.000 | 2.000.000 | 75% | Zeer sterk — mogelijk overkapitaliseerd (lage ROE) |

**Berekening:**
- BV A — Return on Equity (indien winst 25.000): 25.000 / 50.000 = 50% — gunstig ratio MAAR hoog risico door lage solvabiliteit.
- BV B — ROE (indien winst 60.000): 60.000 / 300.000 = 20% — gezonde combinatie risico/return.
- NV C — ROE (indien winst 75.000): 75.000 / 1.500.000 = 5% — laag — overweegt of kapitaal moet teruggegeven worden via kapitaalvermindering (fiscaal voordelig vs dividend bij voldoende fiscaal kapitaal).

→ **Resultaat**: **Advies-strategie**:
- BV A: actief eigen-vermogen-opbouw via winstreservering; eventueel additionele inbreng aandeelhouders.
- BV B: status quo — gezonde balans.
- NV C: overweeg kapitaalvermindering 500.000 EUR ten gunste van aandeelhouders (geen RV indien fiscaal kapitaal) — verhoogt ROE, behoudt voldoende solvabiliteit (resterend EV 1.000.000 / passief 1.500.000 = 67%).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ BV-kapitaal bestaat nog

**Verkeerde assumptie**: Een BV heeft een kapitaal-bedrag dat statutair is vastgelegd, vergelijkbaar met de NV.

**Kernpunt**: Sinds WVV (2019) is BV-kapitaal AFGESCHAFT. Geen 'kapitaal' rekening in BV-balans. Alleen 'inbreng' op rekening 110/111. Geen wettelijke minimum-inbreng meer (kan 1 EUR zijn, maar dan financieel-plan-toets cruciaal). Geen alarmbel op basis van 'helft kapitaal' meer; in plaats daarvan dubbele test (netto-actief negatief OF liquiditeitstest faalt).

<small>📚 WVV — art. 5:1 — _wettekst_ · WVV — art. 5:153 — _wettekst_</small>

### ⚠️ Dividend altijd belastbaar met 30% RV

**Verkeerde assumptie**: Elke uitkering uit eigen vermogen is dividend en wordt belast met 30% roerende voorheffing.

**Kernpunt**: Onderscheid is cruciaal: (a) **Dividend uit reserves of resultaat** = 30% RV (15% VVPRbis, 5% liquidatiereserve na 5j). (b) **Kapitaalvermindering uit fiscaal kapitaal** = GEEN RV (geen 'dividend' fiscaal, gewoon teruggave van inbreng). Tante voor de notaris bij kapitaalvermindering: art. 184 §3 WIB92 — proportionele heffing op wettelijk en statutair onbeschikbare reserves verplicht.

<small>📚 WIB92 — art. 184 — _wettekst_ · WIB92 — art. 18 — _wettekst_</small>

### ⚠️ Liquiditeitstest is een formaliteit

**Verkeerde assumptie**: De liquiditeitstest van art. 5:143 BV is een formele notulen-formule zonder echte impact.

**Kernpunt**: De liquiditeitstest is een SUBSTANTIËLE risico-analyse. Het bestuur moet redelijkerwijs vaststellen dat de vennootschap de komende 12 maanden haar opeisbare schulden kan blijven betalen ONDER REDELIJKE TOEKOMST-VERWACHTINGEN. Onderbouwen met: cashflow-prognose, debiteuren-aging, kredietlijnen, sectorele context. Pure formele tekst zonder substantie = bestuurdersaansprakelijkheid bij latere insolventie + verplichting tot terugbetaling dividend (art. 5:144).

<small>📚 WVV — art. 5:143 — _wettekst_ · WVV — art. 5:144 — _wettekst_</small>

## Accountant-perspectieven

### Cliënt-vennootschap

_De accountant volgt het EV nauwgezet — vooral voor solvabiliteits-analyse, alarmbel-monitoring, fiscale optimalisatie kapitaalvermindering vs dividend._

#### 📒 Boekhouder

##### 👣 Boeking resultaatbestemming na AV  
_`stap`_

🔗 Na AV-jaarvergadering: resultaat van het boekjaar (rekening 79 'Resultaat van het boekjaar') wordt bestemd volgens AV-besluit:

Standaard volgorde bestemming:
1. Wettelijke reserve (NV — 5% tot 10% kapitaal): 79 debet, 130 credit.
2. Tantième bestuurders (indien voorzien): 79 debet, 695 'Tantièmes' debet, 471 credit (te betalen).
3. Dividend AV-besluit: 79 debet, 694 debet, 471 credit (te betalen dividenden).
4. Reservering in beschikbare reserves: 79 debet, 133 credit.
5. Overgedragen winst — restant: 79 debet, 14 credit.

Alle '69x'-rekeningen worden afgesloten via overboeking naar 79 dat dan naar de EV-rekeningen wordt verdeeld. De som van resultaatbestemmingen = volledige winst (geen restant op 79).

<small>📚 KB MAR — Klasse 6-7 + klasse 1 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale optimalisatie via kapitaalvermindering  
_`regel`_

📖 Voor cliënt-vennootschap met aanzienlijk fiscaal kapitaal (volgestort, kwalificeert als kapitaal in zin art. 184 WIB92): overweeg kapitaalvermindering als alternatief voor dividend.

**Voordeel**: terugbetaling fiscaal kapitaal = onbelast (geen RV) — aandeelhouders ontvangen netto het volle bedrag.

**Voorwaarden**:
- Voldoende fiscaal kapitaal (niet alle inbreng/kapitaal kwalificeert — bv. omzettingen reserves naar kapitaal beneden bepaalde voorwaarden niet).
- Sinds Wet 25 december 2017: proportionele heffing — bij kapitaalvermindering moet pro rata ook op onbeschikbare reserves + uitgiftepremies + liquidatiereserves worden afgerekend (art. 184 §3 WIB92).
- Formaliteiten: buitengewone AV met 75%-meerderheid + notariële akte + neerlegging KBO + statutenwijziging.

**Voorbeeld**: kapitaal 500.000 (fiscaal: 400.000) + beschikbare reserves 200.000. Bij vermindering 100.000 EUR: pro rata 100 × 400/600 = 67k uit fiscaal kapitaal (geen RV) en 100 × 200/600 = 33k uit reserves (30% RV = 10k). Netto-effect: aandeelhouders ontvangen 90k netto in plaats van 70k bij volledig dividend (× 70%).

<small>📚 WIB92 — art. 184 — _wettekst_ · WIB92 — art. 18 2° — _wettekst_</small>

#### 🧭 Adviseur

##### 👣 Lopende EV-monitoring + alarmbel-bewaking  
_`stap`_

🔗 Bij elke kwartaal-rapportage of interne tussentijdse balans: nakijken evolutie EV:

1. **Verloop EV** sinds jaarbegin: toenames (winst, inbreng) vs afnames (verlies, dividenden).
2. **Solvabiliteitsratio** vergelijken met sector-mediaan + bancaire convenanten (vaak in kredietcontracten een minimumsolvabiliteit verplicht).
3. **Alarmbel-toets**:
   - BV: voorspelt liquiditeitstest 12m vooruit? Netto-actief blijft positief?
   - NV: netto-actief > helft kapitaal? > kwart kapitaal? > minimumkapitaal 61.500?
4. **Bij dreiging**: advies aan bestuur — preventieve maatregelen vs formele alarmbel.
5. **Bij feitelijk gedaald onder drempel**: formeel adviseren aan bestuur om binnen 2 maanden buitengewone AV bijeen te roepen — schriftelijk advies voor bewijslast.

<small>📚 WVV — art. 5:153 — _wettekst_ · WVV — art. 7:228 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Kapitaalverhoging — toename via inbreng → [[kapitaalverhoging]] _(moet-verwijzen)_
- → Kapitaalvermindering — afname → [[kapitaalvermindering]] _(moet-verwijzen)_
- → Winstuitkering — afname via dividend → [[winstuitkering]] _(moet-verwijzen)_
- → Alarmbel bij netto-actief gedaald onder helft kapitaal of negatief → ⏳ alarmbel-procedure _(moet-verwijzen)_
- → Winstbestemming — reserveringsstroom → [[winstbestemming]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekening]]
### `beinvloed_door`
- [[kapitaalverhoging]] — Kapitaalverhoging in geld of natura → toename EV op rekeningen 10/110.
- [[kapitaalvermindering]] — Kapitaalvermindering → afname EV; fiscaal interessant alternatief voor dividend bij voldoende fiscaal kapitaal.
- [[winstuitkering]] — Dividenduitkering → afname EV via overgedragen winst of beschikbare reserves.
- [[winstbestemming]] — Resultaatbestemming jaarvergadering → toewijzing winst naar reserves (rekening 13) of overgedragen winst (rekening 14).
### `triggert`
- ⏳ alarmbel-procedure — Daling EV onder drempelwaarden (BV: nettoactief negatief of liquiditeitstest faalt; NV: < 50% / 25% / minimumkapitaal) triggert wettelijke alarmbel-procedure.
