---
title: "Fiscale actoren"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - entiteit
ankers:
  - 2.1.VII
  - 2.1.taak.1
  - 2.1.taak.2
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-actoren.json"
---

# Fiscale actoren

_Kader_

🏛️ Kader · 🏢 Entiteit · Anchors: `2.1.VII` · `2.1.taak.1` · `2.1.taak.2` · Wave: `fase2-fiscale-beginselen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: actoren in het fiscaal recht · partijen fiscale procedure

## Definitie

🔗 De fiscale actoren zijn de partijen die in het fiscaal recht een rol vervullen: de belastingplichtige (wie betaalt), de fiscale administratie (wie heft en controleert), het openbaar ministerie (bij strafvervolging fiscale fraude), de rechter (geschilbeslechting) en de adviseur (accountant, belastingadviseur, advocaat — die de belastingplichtige bijstaat).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Voor de stagiair-accountant is dit actoren-landschap praktisch essentieel: bij een fiscaal probleem moet je weten wie de bevoegde gesprekspartner is. Federale inkomstenbelasting → FOD Financiën AAFisc. Mogelijk fraude → AABBI (Bijzondere Belastinginspectie). Btw → AAFisc btw-controle. Gewestbelasting Vlaanderen → VLABEL. Lokale belastingen → gemeentelijke financiële dienst. Geschil → Rechtbank van Eerste Aanleg, fiscale kamer. Internationale dimensie EU-recht → HvJ EU. Wie de juiste deur vindt, bespaart maanden tijd.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege`

Organisatiestructuur FOD Financiën wordt periodiek hervormd (laatste grote reorganisaties: COPERFIN 2010s, modernisering 2020s). Algemene actor-categorieën blijven stabiel.

## Bouwstenen

### 💡 Belastingplichtige  
_`begrip`_

🔗 De belastingplichtige is de persoon op wie de belasting juridisch drukt. Hij is degene die de wet aanwijst als schuldenaar — niet noodzakelijk wie de economische last draagt (vooral bij indirecte belastingen). Categorieën: (1) natuurlijke persoon (PB, BNI-natuurlijke persoon, registratie- en successierechten); (2) vennootschap (VenB, BNI-vennootschappen); (3) rechtspersoon onderworpen aan rechtspersonenbelasting (vzw, openbare instellingen — RPB); (4) belastingplichtige zonder rechtspersoonlijkheid (sommige feitelijke verenigingen, btw-eenheden via art. 4 §2 WBTW); (5) erfgenaam (successierechten); (6) verkrijger (registratierechten op onroerende verkopen).

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · WBTW — art. 4 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ FOD Financiën — Algemene Administraties  
_`mechanisme`_

🔗 De Federale Overheidsdienst Financiën heft en int de federale belastingen via vier Algemene Administraties met elk een eigen werkveld: (1) AAFisc — Algemene Administratie van de Fiscaliteit: heffing en controle PB/VenB/btw/RV/BV; (2) AABBI — Algemene Administratie van de Bijzondere Belastinginspectie: bestrijding ernstige fiscale fraude; (3) AAII — Algemene Administratie van de Inning en Invordering: invordering openstaande schulden; (4) AAII-douane (Douane en Accijnzen): douanerechten en accijnzen; (5) AAGO — Algemene Administratie van de Patrimoniumdocumentatie (vroeger): kadaster en hypotheekkantoren. Daarnaast: AAPD (Patrimoniumdiensten — schenkingsrechten waar federaal bevoegd).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Gewestelijke fiscale administraties  
_`mechanisme`_

🔗 Sinds de overdracht van fiscale bevoegdheden naar de gewesten hebben de gewesten eigen administraties opgericht: (1) Vlaanderen — VLABEL (Vlaamse Belastingdienst): heft en int onroerende voorheffing, schenkings- en erfbelasting, verkeersbelasting/BIV, registratiebelasting onroerende verkopen, leegstandsheffing; (2) Wallonië — DGO7 / SPW Fiscalité: zelfde categorieën voor Waalse rechtspersonen/onroerende goederen; (3) Brussel — Brussel Fiscaliteit. Sommige bevoegdheden worden nog door de federale FOD Financiën uitgeoefend in opdracht van de gewesten (overgangsregeling).

<small>📚 Bijzondere Financieringswet — 16 januari 1989 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 3.1 e.v. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Lokale overheden — gemeente + provincie  
_`mechanisme`_

🔗 Gemeenten en provincies kunnen aanvullende belastingen heffen (opcentiemen op PB, opcentiemen op onroerende voorheffing) en eigen gemeentebelastingen invoeren (tweede verblijven, leegstand, terrasvergoedingen, ...). De fiscale dienst van de gemeente vestigt en int deze belastingen volgens een belastingreglement van de gemeenteraad. Geschillen lopen via een eigen bezwaarprocedure naar het college van burgemeester en schepenen, daarna naar de Rechtbank van Eerste Aanleg.

<small>📚 Decreet Lokaal Bestuur — Vlaamse versie 22-12-2017 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Fiscale rechter  
_`mechanisme`_

🔗 Geschillen tussen belastingplichtige en fiscus worden behandeld door de gewone hoven en rechtbanken — er bestaat geen aparte 'fiscale rechtbank' in België. (1) Rechtbank van Eerste Aanleg, fiscale kamer — bevoegd voor beroepen tegen beslissingen over bezwaar (federaal én gewest); (2) Hof van Beroep — hoger beroep; (3) Hof van Cassatie — cassatie (controle op de wetstoepassing, niet de feiten); (4) Grondwettelijk Hof — toetst fiscale wetten aan de Grondwet (vooral art. 10-11, 170-172); (5) Hof van Justitie EU — prejudiciële vragen over EU-recht (btw-richtlijn, vrij verkeer). De territoriale bevoegdheid is geregeld in art. 632 Gerechtelijk Wetboek (rechtbank van de plaats waar de belasting is gevestigd).

<small>📚 Gerechtelijk Wetboek — art. 632 — _wettekst_ · WIB92 — art. 1385decies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Openbaar Ministerie + fiscale strafvervolging  
_`mechanisme`_

🔗 Bij ernstige fiscale fraude (valsheid in geschrifte, witwas, gebruik valse stukken) kan het Openbaar Ministerie een strafvervolging instellen, naast of in plaats van de administratieve sanctie. De keuze tussen administratieve en strafrechtelijke afhandeling gebeurt via het 'una-via-overleg' tussen fiscus en parket — sinds een Cassatie-arrest (2014) en wijzigingen aan de Charter-procedure (Wet 5 mei 2019) gestructureerd om dubbele bestraffing (non-bis-in-idem) te vermijden.

<small>📚 WIB92 — art. 449-459 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Adviseur — cijferberoeper, belastingadviseur, advocaat  
_`mechanisme`_

🔗 De belastingplichtige laat zich vaak bijstaan door een adviseur. (1) Cijferberoeper — gecertificeerd accountant of belastingadviseur lid van het ITAA: adviseert, stelt aangiften op, vertegenwoordigt cliënt bij controle en bezwaar. (2) Advocaat: vertegenwoordigt in gerechtelijke procedures (vanaf bezwaar of beroep voor de rechtbank). De accountant heeft een eigen wettelijke vertegenwoordigingsbevoegdheid in administratieve fiscale procedures; voor de rechtbank wordt meestal een advocaat ingeschakeld. Het beroepsgeheim van de cijferberoeper (art. 53 Wet 17-03-2019) speelt een belangrijke rol in de relatie met de fiscus.

<small>📚 Wet 17 maart 2019 — art. 53 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ AABBI verwarren met gewone AAFisc-controle

**Verkeerde assumptie**: Een controle door de AABBI loopt zoals een gewone fiscale controle.

**Kernpunt**: De Bijzondere Belastinginspectie (AABBI) treedt enkel op bij ernstige fraude-indicaties (georganiseerde fraude, internationale constructies, witwas). Procedureel beschikt ze over verruimde onderzoeksmiddelen (verlengde aanslagtermijn, doorzoekingen) en speelt het strafrechtelijk perspectief mee. Krijgt een cliënt een AABBI-bericht: onmiddellijk doorverwijzen naar gespecialiseerd advocaat fiscaal strafrecht — andere strategie dan een gewone controle.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Geschil voor verkeerde rechter

**Verkeerde assumptie**: Studenten denken aan de Raad van State of een aparte fiscale rechtbank voor fiscale geschillen.

**Kernpunt**: Fiscale geschillen lopen via de gewone burgerlijke rechtbanken (Rechtbank van Eerste Aanleg → Hof van Beroep → Cassatie). De Raad van State is niet bevoegd voor individuele aanslagen — wel uitzonderlijk voor de annulatie van algemene fiscale reglementen of administratieve handelingen (bv. een gemeentelijk belastingreglement).

<small>📚 WIB92 — art. 1385decies — _wettekst_ · Gerechtelijk Wetboek — art. 632 — _wettekst_</small>

## Verder lezen (scope-out)

- → Accountant-rol als adviseur → ⏳ beroepsbeoefening _(moet-verwijzen)_
- → Fiscale-procedure als procedure-stappen → [[fiscale-procedure]] _(moet-verwijzen)_
- ↪ Vertegenwoordiging bij administratie → [[fiscale-controle]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscaal-recht]]
