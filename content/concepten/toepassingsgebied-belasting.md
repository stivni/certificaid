---
title: "Toepassingsgebied van belasting"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 2.1.VIII
  - 2.1.VIII.A
  - 2.1.VIII.B
  - 2.1.VIII.C
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/toepassingsgebied-belasting.json"
---

# Toepassingsgebied van belasting

_Kader_

🏛️ Kader · Anchors: `2.1.VIII` · `2.1.VIII.A` · `2.1.VIII.B` · `2.1.VIII.C` · Wave: `fase2-fiscale-beginselen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: personeel/materieel/territoriaal/temporeel toepassingsgebied

## Definitie

🔗 Het toepassingsgebied van een belasting bakent vier dimensies af: (1) persoonlijk — wie is belastingplichtig?; (2) materieel — wat wordt belast?; (3) territoriaal — waar (Belgische bron, buitenlandse bron, dubbele heffing)?; (4) temporeel — wanneer (welk aanslagjaar, welk belastbaar tijdperk)?. Bij elke fiscale vraag moet de stagiair eerst deze vier dimensies aflopen om te bepalen of, hoe en in welk wetboek de belasting drukt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Het schema 'persoonlijk-materieel-territoriaal-temporeel' is voor de stagiair een onmisbaar diagnose-instrument. Bij elke fiscale casus: doorloop deze vier dimensies om de juiste belasting te identificeren. Een verkoop tussen Belgische vennootschap en Duitse cliënt: persoonlijk (verkoper = Belgische vennootschap onderworpen aan VenB), materieel (winst uit verkoop), territoriaal (waar is de prestatie verricht? heeft het DBV België-Duitsland invloed?), temporeel (welk boekjaar?). Verkeerd antwoord op één dimensie leidt vaak tot toepassing van het verkeerde wetboek.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege`

Klassiek doctrinair schema — stabiel.

## Bouwstenen

### 💡 Persoonlijk toepassingsgebied  
_`begrip`_

📖 Wie is belastingplichtig? Voor inkomstenbelastingen onderscheidt het WIB92 vier categorieën (art. 2 WIB92): (1) PB — natuurlijke personen die rijksinwoners zijn (art. 3); (2) VenB — binnenlandse vennootschappen, dit zijn vennootschappen met maatschappelijke zetel, voornaamste inrichting of plaats van bestuur in België (art. 179, art. 2 — 5°); (3) RPB — rechtspersonen die geen vennootschap zijn (vzw's, openbare instellingen) (art. 220); (4) BNI — niet-inwoners (natuurlijke personen en vennootschappen) met Belgische bron-inkomsten (art. 227). Voor btw: belastingplichtige = wie zelfstandig en geregeld economische activiteit uitoefent (art. 4 WBTW).

<small>📚 WIB92 — art. 2 — _wettekst_ · WIB92 — art. 3 — _wettekst_ · WIB92 — art. 179 — _wettekst_ · WIB92 — art. 220 — _wettekst_ · WIB92 — art. 227 — _wettekst_ · WBTW — art. 4 — _wettekst_</small>

### 💡 Materieel toepassingsgebied  
_`begrip`_

📖 Wat wordt belast? PB belast vier inkomenscategorieën (art. 6 WIB92): onroerende inkomsten (art. 7-16), roerende inkomsten (art. 17-22), beroepsinkomsten (art. 23-89) en diverse inkomsten (art. 90-103). VenB belast de winst van vennootschappen (art. 183 e.v. — wereldwijd inkomen, behoudens DBV). RPB belast specifieke inkomsten van rechtspersonen (geen volledige winstbelasting). BNI belast inkomsten met Belgische bron (art. 228 WIB92). Btw belast leveringen van goederen + diensten + intracommunautaire verwervingen + invoer (art. 2 WBTW). Successierechten belasten de nalatenschap. Registratierechten belasten transacties.

<small>📚 WIB92 — art. 6 — _wettekst_ · WIB92 — art. 183 — _wettekst_ · WIB92 — art. 228 — _wettekst_ · WBTW — art. 2 — _wettekst_</small>

### 💡 Territoriaal toepassingsgebied  
_`begrip`_

📖 Waar drukt de belasting? Belgisch territorialiteitsbeginsel kent twee aanknopingspunten. (1) Voor rijksinwoners (PB) en binnenlandse vennootschappen (VenB): wereldwijd inkomen (art. 5 WIB92) — alles wordt in België belast, los van waar het verworven is. (2) Voor niet-inwoners (BNI): enkel inkomsten met Belgische bron (art. 228 WIB92) — vaste inrichting in België, onroerende goederen in België, bezoldigingen voor in België verrichte arbeid. Bij grensoverschrijdende inkomsten passen DBV's (dubbele belastingverdragen, ca. 100 verdragen in Belgisch netwerk) de toewijzingsregels toe: woonstaat versus bronstaat, ontheffing of credit.

<small>📚 WIB92 — art. 5 — _wettekst_ · WIB92 — art. 228 — _wettekst_ · OESO-modelverdrag inkomsten en vermogen — art. 4 (woonplaats) + art. 7 (ondernemingswinst) — _modelverdrag_</small>

### 💡 Temporeel toepassingsgebied  
_`begrip`_

📖 Wanneer wordt belast? Twee centrale concepten: (1) Belastbaar tijdperk = de periode waarin het belastbaar feit zich voordoet — voor PB het kalenderjaar (art. 360, eerste lid WIB92); voor VenB het boekjaar van de vennootschap. (2) Aanslagjaar = het jaar waarin de aanslag wordt gevestigd — voor PB normaliter het kalenderjaar dat volgt op het belastbaar tijdperk (inkomsten 2025 → aanslagjaar 2026); voor VenB hangt het af van de afsluitingsdatum (boekjaar afgesloten in 2025 → AJ 2026 als afsluit ≥ 31-12-2024; AJ 2025 als afsluit < 31-12-2025). Het annaliteitsbeginsel (art. 171 GW) maakt elk aanslagjaar fiscaal autonoom.

<small>📚 WIB92 — art. 360 — _wettekst_ · Gecoördineerde Grondwet — art. 171 — _wettekst_</small>

## Voorbeelden

### 💡 Diagnose-schema — Duits-Belgische verkoop 🔗

_Aurelia Holding NV (Belgische vennootschap, zetel Antwerpen) verkoopt machines aan een Duitse klant. Levering ex-works in Antwerpen. Omzet boekjaar 2025: 500.000 EUR._

| Dimensie | Antwoord |
| --- | --- |
| Persoonlijk | Aurelia = binnenlandse vennootschap (zetel BE) → onderworpen aan VenB (art. 179 WIB92). Voor btw: Aurelia = btw-belastingplichtige. |
| Materieel | Winst uit verkoop: belastbaar onder VenB (art. 183 e.v.). Btw: intracommunautaire levering (art. 39bis WBTW) — vrijgesteld in BE, klant past verlegging toe in DE. |
| Territoriaal | Wereldwijd inkomen voor VenB (art. 5+183) — geen DBV-relevantie hier want geen vaste inrichting in DE. Btw: levering in BE (ex-works), maar vrijgesteld ICL. |
| Temporeel | Boekjaar = kalenderjaar 2025 → belastbaar tijdperk 2025, aanslagjaar 2026 voor VenB. Btw: aangifte periode levering 2025. |

<small>📚 WIB92 — art. 5 — _wettekst_ · WBTW — art. 39bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Wereldwijd-inkomen-principe negeren bij rijksinwoners

**Verkeerde assumptie**: Buitenlandse inkomsten van een Belgische rijksinwoner of binnenlandse vennootschap zijn niet belastbaar in België.

**Kernpunt**: Rijksinwoners (PB) en binnenlandse vennootschappen (VenB) worden in beginsel belast op wereldwijd inkomen (art. 5 WIB92). Buitenlandse inkomsten moeten worden aangegeven; ontheffing of credit kan volgen uit DBV of unilaterale regels (vrijstelling onder voorbehoud van progressie voor PB; DBI-aftrek voor VenB-dividenden).

<small>📚 WIB92 — art. 5 — _wettekst_</small>

### ⚠️ Aanslagjaar en belastbaar tijdperk verwisselen

**Verkeerde assumptie**: Aanslagjaar = jaar waarin de inkomsten zijn verworven.

**Kernpunt**: Aanslagjaar = jaar waarin de aanslag wordt gevestigd. Belastbaar tijdperk = periode waarin de inkomsten werden verworven. Voor PB: inkomsten kalenderjaar N → aanslagjaar N+1. Voor VenB: hangt af van boekjaardatum. Schema 'aanslagjaar = inkomstenjaar + 1' geldt enkel voor PB met kalenderjaar als belastbaar tijdperk.

<small>📚 WIB92 — art. 360 — _wettekst_</small>

## Verder lezen (scope-out)

- → Annaliteit als beginsel → [[fiscale-beginselen]] _(moet-verwijzen)_
- → Territorialiteit + internationale aspecten → [[internationaal-fiscaal]] _(moet-verwijzen)_
- ↪ Fiscale woonplaats voor PB → [[personenbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscaal-recht]]
### `vereist`
- [[fiscale-beginselen]]
