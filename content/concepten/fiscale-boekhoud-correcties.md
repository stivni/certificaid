---
title: "Fiscale boekhoud-correcties"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 2.3.I
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-boekhoud-correcties.json"
---

# Fiscale boekhoud-correcties

_Kader_

🏛️ Kader · 📋 Regeling · Anchors: `2.3.I` · Wave: `cluster-extract-fiscaliteit-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: fiscaal-boekhoudkundige correcties · boek-fiscale verschillen — **Vertalingen**: en: tax-accounting adjustments · fr: corrections fiscales comptables

## Definitie

📖 Fiscale boekhoud-correcties zijn de aanpassingen die de boekhoudkundige nettowinst van een vennootschap omzetten naar de belastbare grondslag voor vennootschapsbelasting (VenB). Het Belgisch systeem werkt op basis van primauteit boekhouding: WIB 92 art. 24 bepaalt dat het belastbaar resultaat van een onderneming gelijk is aan haar boekhoudkundig resultaat, tenzij de fiscale wet uitdrukkelijk anders bepaalt. Die uitzonderingen vormen de correctie-cascade: bepaalde kosten worden verworpen (verworpen uitgaven, VU), bepaalde inkomsten vrijgesteld (vrijgestelde reserves), bepaalde afschrijvingen of voorzieningen niet aanvaard, en tijdelijke verschillen genereren uitgestelde belastingen.

<small>📚 WIB 92 — art. 24, 49, 183 — _wettekst_</small>

## Substantie

🔗 Voor de stagiair is dit de kerntechniek van de aangifte VenB: de jaarrekening levert de startwaarde (boekhoudkundige nettowinst), maar pas na een reeks correcties bekom je de belastbare grondslag. Twee soorten verschillen: (a) permanente verschillen — definitieve niet-aftrekbaarheid (niet-aftrekbare beroepskost zoals geheime commissielonen, BTW-VAA voor wagens, autokosten boven aftrekbeperking); (b) tijdelijke verschillen — afwijking in tijd (boekhoudkundige afschrijving over 5 jaar versus fiscaal toegestane 4 jaar) die uiteindelijk uitvlakken maar leiden tot uitgestelde belastingen. Het onderscheid bepaalt of een correctie ook impact heeft op de boekhoudkundige rekening 'uitgestelde belastingen' (klasse 168) — alleen tijdelijke verschillen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een aparte cascade naast de boekhoudkundige winst? Omdat boekhoudregels (CBN, jaarrekening-recht) en fiscale regels (WIB) verschillende doelen dienen: boekhouding mikt op getrouw beeld voor stakeholders, fiscaliteit op gelijkmatige belastinginning + sturing van gedrag (investeringsaftrek stimuleren, overconsumptie afremmen via VU-autokosten). Daarom: boekhouding mag winst tonen die de fiscus niet wil belasten (vrijgesteld), of kosten erkennen die de fiscus niet wil aftrekken (VU). De accountant moet beide regimes gescheiden begrijpen en correct samenbrengen in de fiscale aangifte 275.1.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Opstellen aangifte VenB (formulier 275.1) — vertrekkend van rekening 9904 (te bestemmen winst) naar de finale belastbare grondslag.
- 🔗 Berekening uitgestelde belastingen (rubriek 168 passief) — tijdelijke verschillen worden gemultipliceerd met VenB-voet voor boekhoudkundige rapportering.
- 🔗 Fiscale planning + scenarios — vooraf simuleren hoe boekhoudkundige keuzes (afschrijvings-methode, voorzieningen-opbouw) doorwerken op belastbare grondslag.

## Bouwstenen

### ✴️ Primauteit van de boekhouding (WIB 92 art. 24)  
_`principe`_

📖 Fiscaal beginsel: belastbaar resultaat = boekhoudkundig resultaat, tenzij de fiscale wet uitdrukkelijk anders bepaalt. Concreet: alle bedragen in de aangifte VenB komen rechtstreeks uit de boekhouding (rubrieken volgens minimaal genormaliseerd rekeningenstelsel). Correctie alleen waar fiscale uitzondering geldt. Gevolg: boekhoudkundige keuzes (afschrijvings-methode, voorzieningen-opbouw) hebben directe fiscale impact — tenzij een fiscale anti-misbruik-regel ingrijpt.

<small>📚 WIB 92 — art. 24 — _wettekst_</small>

### 💡 Permanente verschillen  
_`begrip`_

📖 Definitieve niet-aftrekbaarheid: kosten of opbrengsten die boekhoudkundig wel maar fiscaal NIET (of omgekeerd) erkend worden, en die nooit zullen uitvlakken. Voorbeelden: (a) niet-aftrekbare beroepskosten — geheime commissielonen (309 % aanslag), restaurant > 69 %, geschenken aan klanten > 50 EUR; (b) autokosten boven aftrekbeperking (60-100 % afhankelijk van CO₂); (c) niet-aftrekbare belastingen — VenB zelf, fiscale boetes; (d) vrijgestelde meerwaarden op aandelen (DBI-regime). GEEN impact op uitgestelde belastingen — definitief.

<small>📚 WIB 92 — art. 198 (niet-aftrekbare beroepskosten) + 199 (overdrijven van kosten) — _wettekst_</small>

### 💡 Tijdelijke verschillen  
_`begrip`_

📖 Tijds-verschuiving tussen boekhoudkundige en fiscale erkenning — uitvlakt over de jaren maar genereert intussen uitgestelde belastingen. Voorbeelden: (a) afschrijvingen — boekhoudkundig over 10 jaar versus fiscaal over 5 jaar (versnelde afschrijving); (b) voorzieningen — boekhoudkundig opgebouwd als verwachte verplichting, fiscaal pas aftrekbaar bij werkelijke uitgave (tenzij specifieke fiscale erkenning); (c) waardeverminderingen handelsvorderingen — fiscaal aftrekbaar enkel bij geïndividualiseerde dossiers met aantoonbare betalingsmoeilijkheden. WEL impact op uitgestelde belastingen (klasse 168).

<small>📚 WIB 92 — art. 48 (voorzieningen) + 49 (afschrijvingen) — _wettekst_</small>

### 👣 Correctie-cascade van boekhouding naar belastbare grondslag  
_`stap`_

📖 Schematische volgorde (sluit aan op de 8 bewerkingen in art. 74 KB/WIB): (1) Vertrekpunt: boekhoudkundige nettowinst (rubriek 9904) gecorrigeerd voor reserves; (2) Bijtelling van verworpen uitgaven (VU) — niet-aftrekbare kosten; (3) Aftrek vrijgestelde meerwaarden op aandelen + DBI-aftrek; (4) Aftrek aftrekken (DBI · NIA · innovatie-aftrek · investeringsaftrek · gespreide belasting meerwaarden); (5) Aftrek overgedragen verliezen vorige jaren; (6) Resultaat = belastbare grondslag waarop het tarief (25 % of verlaagd KMO-tarief 20 % op eerste 100.000 EUR) wordt toegepast. Concrete uitwerking in belastbare-grondslag-vennootschapsbelasting.

<small>📚 KB/WIB 92 — art. 74-77 (volgorde bewerkingen) — _kb_</small>

### ⚙️ Boekhoudkundige verwerking uitgestelde belastingen  
_`mechanisme`_

📖 Tijdelijke verschillen leiden tot uitgestelde belastingen die boekhoudkundig erkend worden (KB/W.Venn. art. 76, CBN-advies 121/3). Berekening: tijdelijk verschil × VenB-voet (25 % standaard). Boeking: actief = uitgestelde belastings-vordering (rubriek 41) bij verwachte toekomstige aftrekbaarheid; passief = uitgestelde belastings-schuld (rubriek 168) bij verwachte toekomstige bijtelling. Doel: getrouw beeld van werkelijke fiscale lasten in de tijd, niet enkel op kasbasis.

<small>📚 CBN-advies 121/3 — uitgestelde belastingen — advies 121/3 — _cbn_</small>

## Voorbeelden

### 💡 Correctie-cascade VenB — Zelena Bio NV (boekjaar 20X4) 🔗

_Zelena Bio NV: boekhoudkundige nettowinst 285 KEUR. Verschillende correcties toepassen._



<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Permanente en tijdelijke verschillen verwarren

**Verkeerde assumptie**: Alle verworpen uitgaven leiden tot uitgestelde belastingen.

**Kernpunt**: Alleen tijdelijke verschillen vlakken uit en geven uitgestelde belastingen. Permanente verschillen (autokosten, restaurant > 69 %, geheime commissielonen) zijn DEFINITIEF niet-aftrekbaar → geen uitgestelde belastingen-boeking. Verwarring leidt tot foute klasse-168-saldi en getrouw-beeld-kritiek.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ VAA dubbel boeken (afgetrokken én verworpen)

**Verkeerde assumptie**: Niet-doorgerekend voordeel alle aard moet zowel als loonkost én als VU geboekt worden.

**Kernpunt**: VAA wordt OFWEL als loonkost geboekt (en de eigenaar betaalt PB) ofwel als rekening-courant-debet (en blijft niet-uitgekeerd). Bij niet-doorrekening: VU-bijtelling want voordeel niet 'op naam'. Niet beide tegelijk — dat zou dubbele belasting zijn.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Volgorde van bewerkingen omgooien

**Verkeerde assumptie**: DBI-aftrek mag op de eindwinst toegepast worden.

**Kernpunt**: KB/WIB art. 74-77 schrijft een specifieke volgorde voor: VU bijtellen vóór de aftrekken (DBI, NIA, innovatie). Bovendien: bepaalde aftrekken kennen een 'aftrek-volgorde' onderling (DBI vóór NIA vóór investeringsaftrek). Verkeerde volgorde leidt tot foute belastbare grondslag — fiscus corrigeert via taxatie.

<small>📚 KB/WIB 92 — art. 74-77 — _kb_</small>

### ⚠️ Overgedragen verlies op verkeerde manier afzetten

**Verkeerde assumptie**: Overgedragen verlies aftrekken vóór de VU-bijtelling.

**Kernpunt**: Overgedragen verlies wordt afgezet ná de VU-bijtelling en ná de aftrekken (DBI, NIA, ...) volgens de wettelijke cascade. Sinds aanslagjaar 2019 ook beperkt door minimum-belasting (mandement minimum-VenB): bij hoge winsten kan slechts deel overgedragen verlies worden afgezet.

<small>📚 WIB 92 — art. 207 (overgedragen verliezen) — _wettekst_</small>

## Verder lezen (scope-out)

- → Concrete cascade-stappen 8 bewerkingen → [[belastbare-grondslag-vennootschapsbelasting]] _(moet-verwijzen)_
- → Verworpen uitgaven als primaire correctie-categorie → [[verworpen-uitgaven]] _(moet-verwijzen)_
- → Uitgestelde belastingen (boekhoudkundig) → [[uitgestelde-belastingen]] _(moet-verwijzen)_
- ↪ Boekhoudbeginselen als fundament → [[boekhoudbeginselen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]]
### `triggert`
- [[belastbare-grondslag-vennootschapsbelasting]]
- [[uitgestelde-belastingen]] — Tijdelijke verschillen leiden tot boekhoudkundige uitgestelde belastingen.
### `vereist`
- [[boekhoudbeginselen]]
### `bevat`
- [[verworpen-uitgaven]] — VU zijn de primaire categorie permanente correcties.
