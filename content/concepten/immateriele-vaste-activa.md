---
title: "Immateriële vaste activa (IFRS — IAS 38)"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.5.V.A
  - 1.5.V.B
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/immateriele-vaste-activa.json"
---

# Immateriële vaste activa (IFRS — IAS 38)

_Balanspost_

🏢 Entiteit · Anchors: `1.5.V.A` · `1.5.V.B` · Wave: `cluster-extract-balansposten-activa-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: intangible assets · IMA — **Vertalingen**: en: intangible assets · fr: immobilisations incorporelles

## Definitie

📖 IAS 38 definieert een immaterieel actief als een identificeerbaar niet-monetair actief zonder fysieke vorm. Drie cumulatieve voorwaarden voor opname: (1) identificeerbaar — afscheidbaar van entiteit OF voortvloeiend uit contractueel/wettelijk recht; (2) gecontroleerd door entiteit; (3) toekomstige economische voordelen waarschijnlijk + kostprijs betrouwbaar meetbaar. Typische voorbeelden: aangekochte software-licentie, octrooi, merk, klantenlijst, geactiveerde ontwikkelingskosten. Goodwill uit bedrijfscombinatie valt onder IFRS 3 — niet IAS 38 (afzonderlijk vanaf alinea 11).

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 8-17 — _wettekst_ · CBN-advies 2012/13 — Boekhoudkundige verwerking IMA — _cbn_</small>

## Substantie

📖 IAS 38 is restrictiever dan IAS 16 — om twee redenen: (1) Identificeerbaarheid moeilijker — een onderneming heeft veel waarde-creërende elementen (medewerkers, merk, klantenbasis) die NIET als IMA mogen worden opgenomen omdat ze niet voldoen aan de cumulatieve criteria. Internally generated goodwill is uitgesloten (alinea 48). (2) R&D-onderscheid (alinea 54-67): research-fase kosten worden altijd direct in resultaat opgenomen; alleen development-fase mag worden gekapitaliseerd mits zes voorwaarden cumulatief vervuld (technische haalbaarheid, intentie + capaciteit om af te werken, beschikbaarheid middelen, manier waarop voordelen worden gegenereerd, betrouwbare meting kosten). Levensduur (alinea 88): indefinite (geen voorzienbare grens — bv. bekend merknaam) of finite — indefinite worden niet afgeschreven maar jaarlijks getest op impairment.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 48, 54-67, 88-91 — _wettekst_ · CBN-advies 2016/27 — R&D-onderscheid — _cbn_</small>

## Rationale

🔗 De strikte identificeerbaarheids- en R&D-regels reflecteren de voorzichtigheidseis: IMA is moeilijker objectief te waarderen dan MVA. De wetgever wil voorkomen dat ondernemingen hun balans 'opblazen' met subjectief geschatte immateriële posten. Tegelijk laat IAS 38 wél development-kapitalisatie toe — omdat doel-georiënteerde uitgaven (met technische haalbaarheid en intentie) een legitiem actief vertegenwoordigen. Het herwaarderingsmodel is alleen toegelaten als er een actieve markt bestaat (alinea 72-75) — wat zelden voorkomt voor IMA (uitzondering: bepaalde vergunningen, productie-quota's).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Herkenningscriteria — identifiability + control + future economic benefits  
_`principe` (subconcept)_

#### Definitie

📖 (1) Identifiability (alinea 12): actief is afscheidbaar (kan apart verkocht/overgedragen worden) OF voortvloeit uit contractueel/wettelijk recht (bv. licentie). (2) Control (alinea 13): macht om voordelen te verkrijgen + anderen toegang weigeren. Klantenbasis: zelden 'gecontroleerd' (klanten kunnen vrij weggaan), dus niet kapitaliseerbaar tenzij door contract. (3) Future economic benefits (alinea 17): omzet, kostenbesparing, andere voordelen. Beoordeling op basis van redelijke en onderbouwde aannames.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 11-17 — _wettekst_</small>

### 📦 Research-fase vs development-fase  
_`principe` (subconcept)_

#### Definitie

📖 IAS 38 alinea 54-67. Research-fase (alinea 54-56): nieuwe kennis verkrijgen — alle kosten in resultaat. Voorbeelden: literatuurstudie, formulering ideeën, evaluatie alternatieven. Development-fase (alinea 57-67): toepassen onderzoek voor specifiek productontwerp. Activering verplicht mits alle zes voorwaarden vervuld: (a) technische haalbaarheid afronding; (b) intentie afronden + gebruiken/verkopen; (c) capaciteit om te gebruiken/verkopen; (d) manier waarop toekomstige voordelen worden gegenereerd; (e) beschikbaarheid technische/financiële/andere middelen; (f) betrouwbare meting van toerekenbare kosten.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 54-67 — _wettekst_ · CBN-advies 2016/27 — Onderzoek vs ontwikkeling — _cbn_</small>

### 📦 Finite-life vs indefinite-life IMA  
_`principe` (subconcept)_

#### Definitie

📖 IAS 38 alinea 88-110. Finite-life (alinea 97-106): bekende of geschatte einddatum (license met einddatum, octrooi). Afschrijving systematisch over gebruiksduur — restwaarde meestal nul. Indefinite-life (alinea 88-91): geen voorzienbare grens aan periode waarin toekomstige voordelen verwacht worden (bv. wereldwijd erkend merk Coca-Cola, eeuwig hernieuwbare licentie). NIET afschrijven; jaarlijks impairment-test (IAS 36) + herziening 'indefinite' classification.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 88-110 — _wettekst_ · CBN-advies 2012/13 — Beperkte vs onbeperkte levensduur — _cbn_</small>

## Valkuilen

### ⚠️ Internally generated goodwill kapitaliseren

**Verkeerde assumptie**: Sterke merknaam of klantenbasis intern opgebouwd = IMA op de balans.

**Kernpunt**: IAS 38 alinea 48-50 verbiedt expliciet kapitalisatie van interne goodwill, merken, mastheads, publishing titles, klantenlijsten die intern werden opgebouwd. Reden: niet identificeerbaar EN niet betrouwbaar te waarderen. Alleen via overname (IFRS 3) komt goodwill op de balans.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 48-50 — _wettekst_</small>

### ⚠️ R&D-uitgaven volledig activeren

**Verkeerde assumptie**: Alle R&D-uitgaven worden gekapitaliseerd als 'investering in toekomst'.

**Kernpunt**: Research-fase ALTIJD direct in P&L. Alleen development-fase MAG (verplicht) worden gekapitaliseerd mits alle zes voorwaarden vervuld. Twijfel = niet activeren. Documenteer per project waar de overgang research → development plaatsvindt — typische auditor-vraag.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 54-67 — _wettekst_</small>

### ⚠️ Indefinite-life automatisch toekennen

**Verkeerde assumptie**: Een merknaam of vergunning krijgt 'indefinite life' om afschrijving te vermijden.

**Kernpunt**: Indefinite-life vereist objectieve onderbouwing: geen voorzienbare grens. Een 20-jarige licentie zonder hernieuwbaarheidsclausule = finite. Een patent (max 20 jaar) = finite. Toekenning indefinite-life impliceert verplichte jaarlijkse impairment-test — extra audit-werk.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### IFRS-rapportering

#### 🔍 Auditor

##### 👣 R&D-classificatie research vs development  
_`stap`_

🔗 Per R&D-project: vraag projectdocumentatie (feasibility study, business plan), bekijk overgangsmoment naar development-fase. Toets de zes voorwaarden mits onderbouwing. Steekproef geactiveerde kosten — direct toerekenbare lonen + materialen + (gedeeltelijk) indirecte kosten. Toets begin-afschrijvings-moment (= start commerciële gebruik). Risico: management kan moment ergsubjectief naar voren of achteren schuiven afhankelijk van winstdoel.

<small>📚 Verordening (EU) 2023/1803 — IAS 38 — alinea 54-67 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 📜 R&D — fiscaal aftrek vs boekhoudkundige activering  
_`regel`_

📖 Fiscaal: belastingkrediet O&O (art. 289quater WIB92) + investeringsaftrek + verhoogde aftrek loonkosten onderzoekers (art. 275/3 WIB92). Onder Be-GAAP/IFRS gekapitaliseerde development-kosten worden fiscaal IFRS-gevolgd voor consolidaties; maar boekhoudkundige timing impact (kost in jaar X vs afschrijving spread over 5-10 jaar) creëert tijdelijke verschillen — deferred tax-positie.

<small>📚 WIB92 — art. 289quater + 275/3 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vaste activa B-GAAP-perspectief → [[vaste-activa]] _(moet-verwijzen)_
- → IFRS Σ overkoepelend → [[ifrs]] _(moet-verwijzen)_
- ↪ Consolidatieverschil/goodwill (apart, IFRS 3) → [[consolidatieverschil]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[ifrs]]
### `alternatief_referentiestelsel`
- [[vaste-activa]] — IAS 38 voor IMA onder IFRS; klasse 21 Be-GAAP-equivalent.
### `vereist`
- [[vaste-activa]]
### `vergelijkbaar_met`
- [[materiele-vaste-activa]]
    - **Gelijkenissen**:
        - Beide IFRS-vaste-activa-categorieën
    - **Verschillen**:
        - IMA = niet-fysiek + strenger op herkenning + R&D-onderscheid
        - MVA = fysiek, component-aanpak verplicht
### `beinvloed_door`
- [[consolidatieverschil]] — Goodwill uit bedrijfscombinatie valt onder IFRS 3, gerelateerd domein.
