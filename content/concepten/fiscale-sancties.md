---
title: "Fiscale sancties"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 2.5.IV
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-sancties.json"
---

# Fiscale sancties

_Kader_

🏛️ Kader · 📋 Regeling · Anchors: `2.5.IV` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: sancties bij fiscale overtreding · belastingverhoging + boete — **Vertalingen**: fr: sanctions fiscales

## Definitie

📖 Fiscale sancties zijn de gevolgen die de wetgever koppelt aan inbreuken op de fiscale wet. WIB92 onderscheidt drie hoofdcategorieën: (1) belastingverhoging (art. 444) — proportionele verhoging van de aanslag van 10 % tot 200 % bij niet-aangifte of onjuiste aangifte; (2) administratieve geldboete (art. 445) — vast bedrag (50 EUR-1.250 EUR per inbreuk) voor procedurele overtredingen; (3) strafrechtelijke sancties (art. 449-450) — gevangenisstraf en/of geldboete bij fiscale fraude met opzet.

<small>📚 WIB92 — art. 444-450 — _wettekst_</small>

## Substantie

🔗 Voor de accountant is het verschil cruciaal: de belastingverhoging (proportioneel) is automatisch en vrij voorzichtig schaalbaar (10/20/50/100/200 % afhankelijk van herhaling en opzet, schaal in KB van 27 augustus 1993). De administratieve boete is een vast bedrag per overtreding. De strafrechtelijke sanctie veronderstelt opzet (bedrieglijk inzicht) en wordt opgelegd door de strafrechter, niet door de fiscus. Een fiscale fraude-dossier escaleert typisch: eerst BBI-onderzoek met belastingverhoging 50-200 %, daarna parquet-overdracht voor strafvervolging.

<small>📚 KB — 27 augustus 1993 — schaal belastingverhoging — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De getrapte schaal volgt het beginsel van proportionaliteit: lichte overtreding (eerste keer, geen opzet) → lichte belastingverhoging; herhaling met opzet → zware belastingverhoging; bewuste fraude → strafrechtelijke vervolging. De combinatie administratieve sanctie + strafvervolging botst met het non-bis-in-idem-beginsel (Engel-criteria EHRM) — dit is een actief discussiepunt in de rechtspraak. Sinds 2018: 'una via'-keuze tussen fiscus en parquet.

<small>📚 Wet — Una-via-wet 20 september 2012 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 444-450 + KB 27 augustus 1993

Schaal belastingverhoging gewijzigd door KB 13 september 2017. Una-via-keuze tussen administratief en strafrechtelijk pad sinds wet 20 september 2012.

## Bouwstenen

### ⚙️ Belastingverhoging (art. 444 WIB92)  
_`mechanisme`_

📖 Proportionele sanctie bij niet-aangifte, laattijdige aangifte of onjuiste aangifte. Schaal in KB van 27 augustus 1993: van 10 % (lichte overtreding zonder opzet) tot 200 % (herhaalde fraude met opzet). De verhoging wordt op het ontdoken bedrag berekend, niet op de totale aanslag. Eerste lichte fout: doorgaans 0-10 %. Niet-aangifte zonder opzet: 10-50 %. Met opzet: vanaf 50 %.

<small>📚 WIB92 — art. 444 — _wettekst_ · KB 27 augustus 1993 — schaal belastingverhoging — _kb_</small>

### ⚙️ Administratieve geldboete (art. 445 WIB92)  
_`mechanisme`_

📖 Vast bedrag per inbreuk voor procedurele overtredingen die geen rechtstreekse belastingontwijking inhouden: laattijdige indiening, ontbrekende fiches, weigering inlichtingen geven. Bedrag tussen 50 EUR en 1.250 EUR (geïndexeerd). Schaal in administratieve aanschrijvingen; vermeerdert bij herhaling.

<small>📚 WIB92 — art. 445 — _wettekst_</small>

### ⚙️ Strafrechtelijke sancties (art. 449-450 WIB92)  
_`mechanisme`_

📖 Gevangenisstraf (8 dagen tot 2 jaar gewoon; tot 5 jaar bij zware fraude) en/of geldboete (250 EUR tot 500.000 EUR; te vermenigvuldigen met opdeciem 8x). Vereist OPZET: 'bedrieglijk inzicht of met het oogmerk om te schaden'. Wordt opgelegd door de strafrechter (correctionele rechtbank) na parquet-overdracht door de fiscus (BBI of CFI-melding).

<small>📚 WIB92 — art. 449-450 — _wettekst_</small>

### ✴️ Una-via keuze (non-bis-in-idem)  
_`principe`_

📖 Sinds de wet van 20 september 2012: één enkel sanctie-pad mag bewandeld worden. Ofwel administratieve sanctie (belastingverhoging/boete) ofwel strafrechtelijke vervolging — niet beide voor hetzelfde feit. Het Openbaar Ministerie en de fiscus overleggen om de keuze te maken. Dit operationaliseert het non-bis-in-idem-beginsel zoals het EHRM uitlegt via de Engel-criteria.

<small>📚 Wet — Wet 20 september 2012 (una-via) — _wettekst_</small>

## Valkuilen

### ⚠️ Belastingverhoging is geen straf — maar wel een sanctie volgens EHRM

**Verkeerde assumptie**: Belastingverhoging is alleen een administratieve correctie zonder strafrechtelijke karakter.

**Kernpunt**: Volgens de Engel-criteria (EHRM) is een belastingverhoging van 50 % of meer 'penal' in autonoom Europees-rechtelijk opzicht — daardoor gelden waarborgen zoals non-bis-in-idem en proportionaliteit. Praktisch gevolg: een belastingverhoging die hoog uitvalt kan bij de rechter aangevochten worden op proportionaliteit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Sancties zijn rechter-toetsbaar

**Verkeerde assumptie**: Een opgelegde belastingverhoging staat vast — daar is niets aan te doen.

**Kernpunt**: De rechter heeft volle rechtsmacht over fiscale sancties: hij kan ze niet alleen vernietigen maar ook verminderen (mits proportionaliteit). Vergeet niet de sanctie zelf in het bezwaarschrift en de gerechtelijke procedure te betwisten — geen automatisme.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Vergelijking tussen de drie soorten fiscale sancties.

## Verder lezen (scope-out)

- ↪ Beginselen behoorlijk bestuur (proportionaliteit) → [[beginselen-behoorlijk-bestuur]] _(mag-verwijzen)_
- ↪ Non-bis-in-idem → [[fiscale-beginselen]] _(mag-verwijzen)_
- → Bezwaar tegen sanctie → [[bezwaarprocedure]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
