---
title: "Driehoeksverkeer-vereenvoudiging"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.VI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/driehoeksverkeer-vereenvoudiging.json"
---

# Driehoeksverkeer-vereenvoudiging

_Regime_

📋 Regeling · Anchors: `2.4.VI` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: ABC-driehoeksverkeer · art. 25ter §1 lid 2, 3° WBTW · triangulation

## Definitie

📖 Driehoeksverkeer-vereenvoudiging is een EU-administratieve faciliteit (art. 141 Richtlijn 2006/112, omgezet in WBTW art. 25ter) voor de specifieke B2B-keten van drie achtereenvolgende verkopen in drie verschillende EU-lidstaten waarbij de goederen RECHTSTREEKS van de eerste leverancier (A) naar de eindafnemer (C) reizen — dus B fungeert als 'tussenpersoon' op papier maar krijgt de goederen nooit fysiek. Zonder vereenvoudiging zou B zich moeten BTW-registreren in lidstaat C (waar IC-verwerving plaatsvindt). De vereenvoudiging schrapt die registratieplicht door de BTW te verleggen naar C zelf.

<small>📚 Richtlijn 2006/112/EG — art. 141 — _richtlijn_ · WBTW — art. 25ter §1 lid 2, 3° — _wettekst_</small>

## Substantie

🔗 Zonder vereenvoudiging zou B in een dergelijke keten moeten: (1) een IC-verwerving aangeven in lidstaat C (= waar de goederen aankomen); (2) zich daarvoor BTW-identificeren in lidstaat C; (3) een binnenlandse levering in C aangeven aan C-koper. Drie BTW-formaliteiten in een vreemde lidstaat. Met de vereenvoudiging: B doet dit allemaal via zijn EIGEN lidstaat (lidstaat B), met aanpassing van de factuur ('toepassing art. 141 — BTW verlegd') en aangifte van de doorverkoop op de IC-listing onder een speciale code. De eindafnemer C voldoet de BTW via verlegging in zijn eigen aangifte.

<small>📚 Richtlijn 2006/112/EG — art. 141 + art. 197 — _richtlijn_ · WBTW — art. 25ter §1 lid 2, 3° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Triangulair handelsverkeer is courant in EU-distributieketens (bv. Italiaanse fabrikant levert via Belgische groothandel aan Duitse retailer). Zonder vereenvoudiging zou elk Belgisch tussenpersoon zich in tientallen lidstaten moeten registreren bij grensoverschrijdende handel. De faciliteit verlaagt administratieve drempel + bewaart het neutraliteitsbeginsel (BTW wordt uiteindelijk geheven in lidstaat C, waar het verbruik plaatsvindt).

<small>📚 claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 25ter §1 lid 2, 3° + Richtlijn 2006/112 art. 141

EU-geharmoniseerd regime, stabiel sinds invoering interne markt 1993. Sinds 2020 strengere documentatie-eisen (Quick Fixes EU-richtlijn 2018/1910).

**📋 Voorwaarden**
- 📖 Vijf cumulatieve voorwaarden: (1) keten van drie achtereenvolgende leveringen tussen drie verschillende EU-lidstaten (A in lidstaat 1, B in lidstaat 2, C in lidstaat 3); (2) B handelt onder zijn BTW-nummer van een andere lidstaat dan die van vertrek (A) en aankomst (C); (3) B verricht de IC-verwerving in lidstaat C met het oog op de daaropvolgende levering aan C; (4) goederen worden rechtstreeks van A naar C verzonden of vervoerd; (5) C is een BTW-belastingplichtige met BTW-nummer in lidstaat C (vereenvoudiging werkt niet B2C).

## Bouwstenen

### 💡 Positie van B — de 'tussenpartij'  
_`begrip`_

🔗 B is de tussenliggende belastingplichtige die koopt van A en doorverkoopt aan C zonder de goederen zelf in zijn hoofdvestiging te ontvangen. B is gevestigd of geïdentificeerd in een DERDE EU-lidstaat (verschillend van A's en C's vestigingsland). Zonder de vereenvoudiging zou hij verplicht zijn een BTW-identificatie in lidstaat C aan te vragen. Klassiek voorbeeld: Belgische groothandel (B) die goederen van een Duitse fabrikant (A) verkoopt aan een Franse retailer (C). De goederen reizen rechtstreeks Duitsland → Frankrijk; B raakt ze nooit aan.

<small>📚 Richtlijn 2006/112/EG — art. 141 b) — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

### 📜 Verplichte factuurvermeldingen bij driehoeksverkeer  
_`regel`_

📖 De factuur van B aan C moet expliciet vermelden: (1) 'Vereenvoudigde regeling van driehoeksverkeer — art. 141 Richtlijn 2006/112 / art. 25ter WBTW'; (2) 'BTW verlegd naar afnemer' ('reverse charge') — de BTW is voldaan door C; (3) BTW-nummer van B (lidstaat B) én BTW-nummer van C (lidstaat C). Vermelding ontbreekt = vereenvoudiging niet toepasselijk = B moet zich alsnog registreren in C. Strikte naleving.

<small>📚 Richtlijn 2006/112/EG — art. 226, 11 + art. 197 — _richtlijn_ · KB nr. 1 — art. 5 §1, 7° — _kb_</small>

### 👣 Aangifte-mechaniek voor B  
_`stap`_

🔗 Voor de Belgische tussenpersoon B (Belgisch BTW-nummer): (1) inkomende factuur van A — vermeld in IC-verwerving (rooster 86 in BE-aangifte, maar zonder rooster 55-BTW want vereenvoudiging); (2) uitgaande factuur aan C — vermeld in IC-listing van B onder code 'T' (triangulation), apart van gewone IC-leveringen. Geen Belgische BTW verschuldigd, geen aftrek nodig — neutraal effect in BE-aangifte. C boekt in zijn aangifte een IC-verwerving met verlegging.

<small>📚 KB nr. 50 (2019) — art. 9 — IC-listing met code T — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Driehoeksverkeer DE → BE-tussenpersoon → FR 🔗

_Aurelia BVBA (BE, BTW BE0123…) koopt machines van Müller GmbH (DE, BTW DE…) en verkoopt door aan Dupont SARL (FR, BTW FR…). Goederen worden rechtstreeks vanuit Düsseldorf verzonden naar Lyon. Geen vereenvoudiging zou betekenen: Aurelia moet zich BTW-registreren in Frankrijk._

**Berekening:**
- Stap 1 — toets cumulatieve voorwaarden: 3 verschillende EU-lidstaten ✓ (DE, BE, FR); B in andere lidstaat dan A en C ✓; goederen rechtstreeks A → C ✓; C is BTW-plichtig ✓ → vereenvoudiging toepasselijk
- Stap 2 — facturatie Müller GmbH aan Aurelia: 100.000 EUR vrijgesteld IC-levering art. 138 Richtlijn (geen DE-BTW)
- Stap 3 — facturatie Aurelia aan Dupont: 120.000 EUR, vermelding 'Vereenvoudigde regeling van driehoeksverkeer — art. 141 Richtlijn 2006/112 — BTW verlegd'
- Stap 4 — BE-aangifte Aurelia: IC-verwerving rooster 86 (100.000) zonder rooster 55 (vereenvoudiging); IC-listing: doorverkoop Dupont onder T-code (120.000)
- Stap 5 — FR-aangifte Dupont: IC-verwerving 120.000 EUR + Franse BTW via verlegging (20 % FR-tarief) — boekhoudkundig D 411 BTW + C 451 BTW (saldo nul), goederen geactiveerd 120.000

→ **Resultaat**: Aurelia hoeft GEEN Franse BTW-registratie aan te vragen. Administratieve last sterk gereduceerd. BTW wordt uiteindelijk geheven in Frankrijk (waar het verbruik plaatsvindt) via verlegging bij Dupont.

<small>📚 Richtlijn 2006/112/EG — art. 141 + art. 197 — _richtlijn_ · WBTW — art. 25ter §1 lid 2, 3° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Vier-partijen-keten dekken onder driehoeksverkeer

**Verkeerde assumptie**: Een keten A→B→C→D over vier lidstaten valt onder de vereenvoudiging.

**Kernpunt**: De vereenvoudiging geldt UITSLUITEND voor de klassieke ABC-driehoek over DRIE lidstaten. Bij vier (of meer) tussenpersonen geldt ze niet, en moet elk lid van de keten zich BTW-registreren in de lidstaten waar hij IC-verwervingen verricht. Bij twijfel: simulatieoefening op papier met partij-identificaties + goederen-flow.

<small>📚 Richtlijn 2006/112/EG — art. 141 — _richtlijn_</small>

### ⚠️ Vereenvoudiging toepassen zonder factuur-vermelding

**Verkeerde assumptie**: 'De voorwaarden zijn vervuld, dus de vereenvoudiging werkt automatisch.'

**Kernpunt**: De vereenvoudiging vereist een EXPLICIETE vermelding op de factuur van B aan C (verwijzing naar art. 141 + 'BTW verlegd'). Zonder vermelding kan de fiscus van C de vereenvoudiging weigeren — B moet zich dan retroactief registreren in C met boetes. Zorg dat de software-template van B deze vermelding standaard opneemt voor driehoeksverkoop-facturen.

<small>📚 Richtlijn 2006/112/EG — art. 226, 11 — _richtlijn_</small>

### ⚠️ Verkoop aan particulier C onder vereenvoudiging

**Verkeerde assumptie**: 'Mijn Franse klant is een natuurlijke persoon, maar de keten loopt over drie landen → vereenvoudiging.'

**Kernpunt**: C MOET een BTW-belastingplichtige zijn met BTW-nummer (Richtlijn art. 141 e + art. 197). Bij verkoop aan particulieren = vereenvoudiging niet toepasselijk. Voor B2C-verkoop in EU gelden andere regimes (afstandsverkopen-drempels, OSS, ...).

<small>📚 Richtlijn 2006/112/EG — art. 141 e + art. 197 — _richtlijn_</small>

## Accountant-perspectieven

### Kantoor begeleidt EU-distributie-cliënt

_De accountant bij een cliënt die als groothandel of distributeur in EU-driehoekstransacties handelt._

#### 💰 Fiscaal adviseur

##### 👣 Screening van handelsketen voor vereenvoudigings-eligibiliteit  
_`stap`_

🔗 Bij IC-leveringen waar cliënt B speelt: per keten verifiëren — drie verschillende EU-lidstaten? B-BTW-nummer ≠ A-LS en ≠ C-LS? Goederen direct A→C? C is BTW-plichtig met geldig nummer (VIES-check)? Bij ja: vereenvoudiging toepassen + factuur-template aanpassen. Bij nee: registratieplicht in lidstaat C of fall-back op normale regime.

<small>📚 Richtlijn 2006/112/EG — art. 141 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW grensoverschrijdend (algemeen IC-leveringen) → [[btw-grensoverschrijdend]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw-grensoverschrijdend]]
### `is_uitzondering_op`
- [[btw-grensoverschrijdend]] — Algemene IC-leveringen vereisen BTW-identificatie in alle lidstaten waar verwerving plaatsvindt; driehoeksverkeer-vereenvoudiging schrapt die plicht voor B.
