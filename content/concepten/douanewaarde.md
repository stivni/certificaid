---
title: "Douanewaarde"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.IX
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/douanewaarde.json"
---

# Douanewaarde

_Kader_

📋 Regeling · Anchors: `2.4.IX` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: customs value · transactiewaarde

## Definitie

📖 De douanewaarde is de wettelijk vastgestelde waarde van goederen bij invoer in de EU, die als grondslag dient voor de berekening van invoerrechten en — verhoogd met die rechten en bijkomende kosten — voor de invoer-BTW. Het Unierechtelijke kader is het Douanewetboek van de Unie (UCC — Verordening (EU) 952/2013, art. 69-76) met uitvoeringsregels in Verordening (EU) 2015/2447. Hoofdmethode: transactiewaarde = de werkelijk betaalde of te betalen prijs voor de goederen bij verkoop naar de EU.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 69-70 — _richtlijn_ · WBTW — art. 34 — _wettekst_</small>

## Substantie

🔗 De douanewaarde bepaalt rechtstreeks twee belastingsommen: (1) invoerrecht = douanewaarde × tariefpercentage (HS-code-specifiek); (2) invoer-BTW = (douanewaarde + invoerrecht + bijkomende kosten) × BTW-tarief. Een verkeerd te lage douanewaarde = onderbetaling rechten + BTW → boete + nabetaling met interest. Een verkeerd te hoge waarde = cashflow-verlies. Daarom is correcte waardebepaling essentieel — vooral bij verbonden partijen (cross-border-transfer-pricing-discussies).

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 + art. 71 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 De EU-douanewaarde stoelt op WTO-overeenkomst inzake artikel VII GATT (1994) — een wereldwijde standaard die manipulatie van invoerwaarden om rechten te ontwijken voorkomt. De hiërarchie van 6 methodes (transactiewaarde → 5 subsidiaire methodes in vaste volgorde) zorgt voor objectiviteit en voorspelbaarheid. Er is geen vrije keuze tussen methodes — pas een subsidiaire methode toe als de hogere objectief niet kan.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 74 (hiërarchie methodes) — _richtlijn_</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2016-05-01** · basis: UCC (Verordening (EU) 952/2013) + Uitvoeringsverordening (EU) 2015/2447

UCC vervangt de oude communautair douanewetboek (Vo. 2913/92) sinds 1 mei 2016. Stabiel sindsdien.

## Sub-concepten

### 📦 Hiërarchie 6 waarderingsmethodes  
_`procedure` (subconcept)_

#### Definitie

📖 UCC art. 74 schrijft een strikte volgorde voor: (1) transactiewaarde van de ingevoerde goederen (art. 70); (2) transactiewaarde van identieke goederen; (3) transactiewaarde van soortgelijke goederen; (4) deductieve waarde (verkoopprijs van identieke/soortgelijke goederen in EU, minus aftrekken); (5) computed value / berekende waarde (productiekost + winstmarge); (6) fall-back-methode (redelijke schatting consistent met WTO-principes). Methode (4) en (5) zijn verwisselbaar op verzoek van de aangever. Een lagere methode mag alleen worden gebruikt als de hogere niet toepasbaar is.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70-74 — _richtlijn_</small>

#### 💡 Transactiewaarde (hoofdmethode)  
_`begrip`_

📖 De transactiewaarde is de werkelijk betaalde of te betalen prijs voor de goederen bij verkoop naar het douanegebied van de Unie, mits gecorrigeerd voor art. 71 (toe te voegen elementen) en art. 72 (uit te sluiten elementen). Voorwaarden: er is een verkoop voor uitvoer naar de EU; geen beperkingen op het gebruik van de goederen door koper; de verkoopprijs is niet afhankelijk van voorwaarde of tegenprestatie zonder bepaalbare waarde; geen niet-aangepaste relatie tussen koper en verkoper. Bij niet-vervulling: doorgaan naar volgende methode.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 — _richtlijn_</small>

## Bouwstenen

### 📜 Aanpassingen — toe te voegen elementen (art. 71 UCC)  
_`regel`_

📖 Bij de transactiewaarde MOETEN worden toegevoegd, voor zover niet al inbegrepen: (a) commissies en courtage (behalve aankoopcommissie); (b) kosten van verpakking en verpakkingsmateriaal; (c) waarde van 'assists' = materialen, gereedschap, ontwerpen die door koper gratis of tegen verminderde prijs aan verkoper geleverd zijn voor gebruik in productie; (d) royalty's en licentievergoedingen i.v.m. de goederen die de koper moet betalen als voorwaarde voor de verkoop; (e) deel van opbrengst van wederverkoop dat aan verkoper toekomt; (f) kosten van vervoer + verzekering tot de plaats van binnenkomst in EU.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 71 — _richtlijn_</small>

### 📜 Uit te sluiten elementen (art. 72 UCC)  
_`regel`_

📖 NIET in de douanewaarde mogen worden opgenomen, mits afzonderlijk aantoonbaar: (a) kosten van vervoer NA invoer in de EU (= post-import-vervoer); (b) kosten van bouw, montage of onderhoud na invoer; (c) interesten op uitgestelde betalingen; (d) rechten voor reproductie van de ingevoerde goederen in de EU; (e) aankoopcommissies; (f) invoerrechten zelf en andere binnen-EU-belastingen verschuldigd bij invoer. Onderscheid 'voor' vs 'na' invoer is essentieel — een transparante factuurspecificatie helpt.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 72 — _richtlijn_</small>

### ⚠️ Verbonden partijen — bijzondere aandacht  
_`risico`_

📖 Wanneer koper en verkoper VERBONDEN zijn (intra-groep-handel — bv. moeder-dochter), kan de transactiewaarde slechts behouden blijven als de relatie de prijs niet heeft beïnvloed. Bewijslast: de aangever moet aantonen dat de prijs vergelijkbaar is met arms-length-transactiewaarde (intercompany-verkoop tussen onafhankelijken; vergelijking met douanewaarde van identieke/soortgelijke goederen uitgevoerd door derde partijen). Bij twijfel: de douane kan overstappen naar subsidiaire methodes. Strong overlap met transfer-pricing-documentatie.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 lid 3-4 — _richtlijn_</small>

## Voorbeelden

### 💡 Eenvoudige import — transactiewaarde 🔗

_Aurelia Holding importeert machines uit Japan. Factuurprijs FOB Yokohama: 100.000 USD ≈ 92.000 EUR. Vervoer per schip Yokohama → Antwerpen: 5.000 EUR. Verzekering: 800 EUR. Commissie aan inkoop-agent in Japan: 2.000 EUR._

**Berekening:**
- Stap 1 — Toets transactiewaarde toepasselijk: verkoop voor uitvoer naar EU ✓, geen gebruikbeperking ✓, geen verbonden partijen ✓ → methode 1
- Stap 2 — Vertrek: factuurprijs = 92.000 EUR (FOB-prijs)
- Stap 3 — Art. 71 toevoegen: vervoer tot binnenkomstplaats EU (5.000) + verzekering (800) = 5.800 EUR. Commissie aan inkoop-agent NIET toevoegen (= aankoopcommissie, art. 71 uitzondering)
- Stap 4 — Art. 72 uitsluiten: niet van toepassing hier (alle aangevoerde kosten zijn vóór invoer)
- Stap 5 — Douanewaarde = 92.000 + 5.800 = 97.800 EUR

→ **Resultaat**: Douanewaarde 97.800 EUR — basis voor invoerrecht (bv. 4 % machines = 3.912 EUR) en invoer-BTW maatstaf (97.800 + 3.912 + eventueel vervoer-binnen-EU = ca. 102.000 × 21 % = 21.420 EUR BTW).

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 + art. 71 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 💡 Import met royalty — toevoeging 📖

_Aurelia importeert luxe handtassen uit Italië die ze in België verkoopt onder een merk. Aurelia betaalt jaarlijks 8 % royalty aan de merk-houder (Italiaans hoofdkwartier) op basis van haar EU-omzet. Factuurprijs handtassen 50.000 EUR._

**Berekening:**
- Stap 1 — Royalty-toets: betaling i.v.m. de goederen (handtassen) ✓; voorwaarde voor verkoop (Aurelia mag merk alleen voeren mits royalty-betaling) ✓ → toevoeging vereist art. 71, d)
- Stap 2 — Royalty te alloceren op deze zending: 8 % × 50.000 = 4.000 EUR
- Stap 3 — Douanewaarde = 50.000 + 4.000 + vervoer/verzekering tot EU = 54.000+
- Resultaat — Hogere douanewaarde → hogere invoerrechten + hogere BTW-maatstaf

<small>📚 UCC — Verordening (EU) 952/2013 — art. 71 d) — _richtlijn_</small>

## Valkuilen

### ⚠️ Vervoer-na-invoer mee in douanewaarde rekenen

**Verkeerde assumptie**: Alle vervoerkosten op de leveringsfactuur tellen in de douanewaarde.

**Kernpunt**: Enkel vervoerkosten TOT de plaats van binnenkomst in de EU (typisch: havendrempel Antwerpen, luchthaven Brussel) horen erin. Het vervoer van Antwerpen → magazijn-eindgebruiker is post-import (art. 72 a) — uit te sluiten mits afzonderlijk gefactureerd. Belang van een transparante vervoer-specificatie op de factuur.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 71 + art. 72 — _richtlijn_</small>

### ⚠️ Aankoopcommissie meetellen

**Verkeerde assumptie**: Commissies aan tussenpartijen tellen altijd in de douanewaarde.

**Kernpunt**: Onderscheid: VERKOOPcommissie (toegevoegd, art. 71 a) — commissie aan tussenpartij die voor de verkoper handelt; AANKOOPcommissie (NIET toegevoegd) — commissie aan tussenpartij die voor de KOPER handelt (bv. een inkoop-bureau in China). Bewijslast: koper-importeur moet aantonen dat tussenpartij zijn agent was, niet die van verkoper.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 71 a + art. 72 e — _richtlijn_</small>

### ⚠️ Verbonden-partijen-prijs onverbiddelijk aanvaarden

**Verkeerde assumptie**: Intra-groep-prijs is de transactiewaarde, klaar.

**Kernpunt**: Bij verbonden partijen kan de douane de transactiewaarde betwisten als ze niet-marktconform lijkt. Aangever moet bewijzen: prijs is vergelijkbaar met arms-length-transactie, of valt binnen aanvaardbare marges. Transfer-pricing-documentatie volgens OESO-richtlijnen is sterke bouwsteen voor douanewaarde-verdediging. Inconsistenties tussen transfer-pricing-aangifte en douanewaarde zijn risicozone.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 lid 3-4 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Kantoor adviseert importeur over douanewaarde

_De accountant of douane-adviseur bij waardebepaling van invoer._

#### 🧭 Adviseur

##### 🧭 Factuur structureren voor optimale douanewaarde  
_`vuistregel`_

🔗 Vraag bij de buitenlandse leverancier facturen die DUIDELIJK splitsen: (1) FOB-prijs of EXW-prijs; (2) vervoer tot binnenkomst EU; (3) vervoer NA binnenkomst EU (afzonderlijk); (4) verzekering pre/post; (5) bijkomende diensten (montage, onderhoud na invoer — uitsluiten). Een goed gestructureerde factuur kan honderden tot duizenden EUR aan invoerrechten + BTW besparen — vooral op grote zendingen.

<small>📚 UCC — Verordening (EU) 952/2013 — art. 71 + art. 72 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

##### 🧭 Alignering douanewaarde ↔ transfer-pricing  
_`vuistregel`_

🔗 Voor multinationals met intra-groep-invoer: zorg dat transfer-pricing-documentatie (OESO-CbCR + lokale TP-file) consistent is met de douanewaarde aangegeven op DAU's. Inconsistente waardes = audit-risico bij zowel fiscus (transfer-pricing) als douane. Bij wijziging van transfer-pricing-methodologie: ook douanewaardes herzien via Advance Customs Valuation Ruling (ACV-ruling).

<small>📚 UCC — Verordening (EU) 952/2013 — art. 70 lid 3-4 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Douaneprocedures bij invoer (DAU + ET 14.000) → [[douaneprocedures-btw-invoer]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscaal-recht]]
### `vereist`
- [[douaneprocedures-btw-invoer]] — Douanewaarde is de maatstaf-basis bij invoer (rechten + BTW).
