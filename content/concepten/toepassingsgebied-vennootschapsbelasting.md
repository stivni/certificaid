---
title: "Toepassingsgebied vennootschapsbelasting"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.IV
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/toepassingsgebied-vennootschapsbelasting.json"
---

# Toepassingsgebied vennootschapsbelasting

_Kader_

📋 Regeling · Anchors: `2.8.IV` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: binnenlandse vs buitenlandse vennootschap · VenB-onderworpenheid

## Definitie

📖 Het toepassingsgebied van de vennootschapsbelasting (VenB) bepaalt welke vennootschappen aan welke belasting worden onderworpen op welk inkomen. Art. 179 WIB92 stelt: de binnenlandse vennootschappen zijn onderworpen aan de VenB op hun wereldwijde inkomsten. Art. 227 WIB92 omschrijft de buitenlandse vennootschap (vennootschap, vereniging, inrichting of instelling met rechtspersoonlijkheid die haar maatschappelijke zetel, haar voornaamste inrichting of haar zetel van bestuur of beheer NIET in België heeft) — die wordt belast onder de belasting van niet-inwoners-vennootschappen (BNI-VenB, art. 228-229) en dan enkel op haar Belgische bron-inkomsten via een vaste inrichting of bepaalde Belgische activa.

<small>📚 WIB92 — art. 179 — _wettekst_ · WIB92 — art. 2 §1, 5° — _wettekst_ · WIB92 — art. 227 — _wettekst_</small>

## Substantie

📖 Voor de Belgische fiscus is dit de eerste vraag voor elke vennootschap-cliënt: onder welke belasting valt zij? Een binnenlandse vennootschap betaalt VenB op de volledige wereldwinst (met DBV-vrijstelling voor sommige delen); een buitenlandse vennootschap betaalt enkel BNI-VenB op haar Belgische tak. De aanknopingspunten zijn alternatief: het volstaat dat één van de drie (maatschappelijke zetel, voornaamste inrichting, zetel van bestuur of beheer) in België ligt om de vennootschap binnenlands te maken. Sinds de hervorming van 2018 wordt vooral het criterium zetel van bestuur of beheer (substance) belangrijk — formele zetel-vehikels in laag-tarief-landen kunnen door de feitelijke leiding alsnog Belgisch worden.

<small>📚 WIB92 — art. 2 §1, 5° — _wettekst_</small>

## Rationale

🔗 De ratio legis is fiscale soevereiniteit + economic substance: een staat heeft het recht om de wereldwinst te belasten van vennootschappen die er hun economische thuis hebben, want zij genieten de Belgische rechtsorde, infrastructuur en arbeidsmarkt. Met meervoudige aanknopingspunten voorkomt België dat een vennootschap door louter formele zetel-vlucht aan de VenB ontsnapt — de substance-toets via 'zetel van bestuur of beheer' is een anti-vlucht-mechanisme. Voor buitenlandse vennootschappen is de territoriale benadering (BNI alleen op Belgisch deel) een logische pendant: België respecteert dat andere staten hun eigen vennootschappen belasten en heft enkel op de Belgische economische voet.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 2 §1, 5° + art. 179 + art. 227-229

Sinds WVV (2019) is de Belgische statutaire-zetel-theorie verlaten voor de werkelijke-zetel-theorie: art. 2:146 WVV bepaalt dat een vennootschap onderworpen is aan het Belgische vennootschapsrecht zodra haar statutaire zetel in België ligt — maar fiscaal blijft de meervoudige aanknopingstoets van art. 2 WIB92 gelden.

**✅ Voor**
- 📖 Een Belgische BV/NV met statutaire zetel + werkelijke leiding in België: binnenlandse vennootschap, VenB op wereldwinst.
- 📖 Een Nederlandse BV met enkel Belgische zetel-formaliteiten maar werkelijke leiding in Nederland: buitenlandse vennootschap, geen BE-VenB tenzij ze in BE een vaste inrichting heeft.

**📋 Voorwaarden**
- 📖 Binnenlandse vennootschap (art. 2 §1, 5°): cumulatief 'vennootschap, vereniging, inrichting of instelling die regelmatig is opgericht, rechtspersoonlijkheid bezit en in België haar maatschappelijke zetel, haar voornaamste inrichting of haar zetel van bestuur of beheer heeft'. Eén voldoende criterium = binnenlands.

**⛔ Uitsluitingen**
- 📖 Art. 180 WIB92 sluit specifieke entiteiten uit van VenB ondanks rechtspersoonlijkheid (sommige overheidsinstellingen, NMBS, BIVR, etc.). Art. 181-182 onderwerpen sommige rechtspersonen aan RPB (rechtspersonenbelasting) in plaats van VenB — vzw's zonder commercieel oogmerk, gemeenten, intercommunales, etc.

## Bouwstenen

### 📏 Drie aanknopingspunten (art. 2 §1, 5°)  
_`drempel`_

📖 Een vennootschap is Belgisch binnenlands wanneer minstens één van drie elementen in België ligt: (1) maatschappelijke zetel — de statutair vastgelegde plaats; (2) voornaamste inrichting — locatie van de hoofdactiviteit; (3) zetel van bestuur of beheer — waar het beslissingscentrum effectief gevestigd is (substance over form). De drie zijn alternatief — eentje volstaat. Voor moderne anti-fraude is criterium (3) doorslaggevend: een vennootschap met formele zetel op Cyprus maar bestuursvergaderingen in Brussel is fiscaal binnenlands.

<small>📚 WIB92 — art. 2 §1, 5° — _wettekst_</small>

### ⚙️ Wereldwinst (binnenlandse) vs territoriaal (buitenlandse)  
_`mechanisme`_

📖 Binnenlandse vennootschap: VenB op de wereldwijde winst (art. 179 + 183 WIB92), met DBV-vrijstelling voor VI-winsten in verdragslanden (art. 23A) en/of DBI-aftrek voor dividenden uit deelnemingen. Buitenlandse vennootschap: BNI-VenB enkel op haar Belgische winst — concreet (a) winst van een Belgische inrichting (art. 228 §2, 3° + 229), (b) inkomsten van Belgische onroerende goederen, (c) bepaalde Belgische roerende inkomsten met bronheffing. Geen wereldwinst-belasting in BE.

<small>📚 WIB92 — art. 179 + 183 + 228 — _wettekst_</small>

### 📜 Substance over form-test  
_`regel`_

🔗 Voor het criterium zetel van bestuur of beheer is de werkelijke plaats van besluitvorming doorslaggevend, niet de formele papierwinkel. Indicatoren (rechtspraak Hof Cass.): waar vergadert de raad van bestuur? Waar verblijft de meerderheid van bestuurders? Waar gebeurt de strategische beslissingen, banktransacties, contractsluiting? Waar zit het personeel en de boekhouding? Bij twijfel-of-conflict: meerderheid van indicatoren in België = binnenlands; meerderheid in buitenland = buitenlands (mits DBV-tie-break-regel).

<small>📚 WIB92 — art. 2 §1, 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ DBV tie-break voor dubbele residentie  
_`mechanisme`_

📖 Wanneer twee staten een vennootschap als hun binnenlandse beschouwen (bv. statutaire zetel in BE + werkelijke leiding in NL), regelt het DBV de tie-break. Art. 4 OESO-MV (vennootschap): exclusieve residentie in de staat van werkelijke-leiding (place of effective management). Sinds BEPS-MLI (2017): tie-break vervangen door mutual agreement-procedure tussen bevoegde autoriteiten — niet langer automatisch. Praktisch: bij dubbele aanknoping moet eerst het DBV worden geconsulteerd voor de eindbeslissing.

<small>📚 OESO-modelverdrag — art. 4 §3 — _modelverdrag_</small>

### ⚙️ Fiscale gevolgen wijziging zetel (link naar exit)  
_`mechanisme`_

📖 Verhuist een Belgische vennootschap haar werkelijke leiding naar het buitenland zodat ze niet langer binnenlands is? Dit triggert exit-belasting (art. 210bis WIB92 + ATAD art. 5): latente meerwaarden + niet-uitgekeerde reserves worden geacht uitgekeerd te zijn — belastbaar in BE bij het verlies van de binnenlandse-status. Omgekeerd: een vennootschap die haar werkelijke leiding naar België verlegt wordt binnenlands met als ingangsdatum de werkelijke verhuis — vanaf dan VenB op wereldwinst.

<small>📚 WIB92 — art. 210bis — _wettekst_</small>

## Valkuilen

### ⚠️ Alleen op statutaire zetel kijken

**Verkeerde assumptie**: Een vennootschap met statutaire zetel in Luxemburg is automatisch buitenlands voor BE-fiscaal.

**Kernpunt**: Art. 2 §1, 5° werkt met drie alternatieve criteria. Een Luxemburgse SARL met werkelijke leiding in Brussel is binnenlands voor de Belgische VenB ondanks de Luxemburgse statutaire zetel. Substance-toets is doorslaggevend.

<small>📚 WIB92 — art. 2 §1, 5° — _wettekst_</small>

### ⚠️ Buitenlandse vennootschap belasten op wereldwinst

**Verkeerde assumptie**: Studenten passen bij een buitenlandse vennootschap de wereldwinst-regel van art. 179 toe.

**Kernpunt**: Art. 179 geldt enkel voor binnenlandse. Buitenlandse vennootschap valt onder BNI-VenB (art. 228-229) en wordt enkel op Belgische bron-inkomsten belast. Geen Belgische heffing op haar buitenlandse activiteiten.

<small>📚 WIB92 — art. 228 + 179 — _wettekst_</small>

### ⚠️ VenB-onderworpen rechtspersonen door elkaar halen met RPB

**Verkeerde assumptie**: Elke rechtspersoon valt onder VenB.

**Kernpunt**: Art. 181-182 sluit bepaalde rechtspersonen uit van VenB en onderwerpt ze aan rechtspersonenbelasting (RPB): vzw's zonder commercieel oogmerk, gemeenten, intercommunales (deels), publiekrechtelijke rechtspersonen. Eerst kwalificatie van rechtspersoon checken.

<small>📚 WIB92 — art. 181-182 — _wettekst_</small>

## Syntheses

### 🧩 Synthese  
_`beslisboom`_

Beslisboom: welk regime is van toepassing op een vennootschap?

## Verder lezen (scope-out)

- → Fiscale residentie (PB-residentie en mapping) → [[fiscale-residentie]] _(moet-verwijzen)_
- → Belasting van niet-inwoners (BNI — VenB-pendant) → [[belasting-niet-inwoners]] _(moet-verwijzen)_
- → Vaste inrichting (toerekening voor BNI-VenB) → [[vaste-inrichting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]]
### `vereist`
- [[ondernemingsvormen]] — Eerst rechtspersoonlijkheid en vorm bepalen — niet elke entiteit komt in aanmerking voor VenB.
### `triggert`
- [[belasting-niet-inwoners]] — Een buitenlandse vennootschap met Belgische inkomsten valt automatisch onder BNI-VenB.
- [[exit-planning-vennootschap]] — Wijziging van binnenlandse status (door verhuis werkelijke leiding) triggert exit-belasting volgens art. 210bis.
### `vergelijkbaar_met`
- [[fiscale-residentie]]
    - **Gelijkenissen**:
        - Beide bepalen welke staat heffingsbevoegd is over wereldwinst vs territoriaal
        - Beide gebruiken substance-toets bij twijfel
        - Beide hebben DBV tie-break-regels
    - **Verschillen**:
        - Fiscale residentie: vooral PB-context voor natuurlijke personen (woonplaats, zetel van fortuin)
        - Toepassingsgebied VenB: vennootschapscontext, drie aanknopingspunten
        - PB-residentie: maandgrenzen + sociale relaties; VenB-binnenlandse: statutaire/inrichtingscriteria
    - ⚠️ **Verwarringsrisico**: Studenten passen PB-residentiecriteria toe op vennootschappen — fout. Vennootschap-residentie heeft eigen criteria.
