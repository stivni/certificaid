---
title: "Current ratio"
concept_type: "ratio"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/current-ratio.json"
---

# Current ratio

_Ratio_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Afk.**: CR — **Synoniemen**: vlottende-activaratio · liquiditeitsratio in ruime zin

## Voorkennis & leespad

**Voorvereisten**: [[voorraden]] · [[handelsvorderingen]] · [[schulden-op-korte-termijn]] · [[geldbeleggingen-en-liquide-middelen]]
**Naast relevant**: [[quick-ratio]] · [[cash-ratio]] · [[werkkapitaalbehoefte]]
**Volgkennis**: [[jaarrekeninganalyse]] · [[faillissementspredictie-modellen]]

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**🟢 Indicaties**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Formule  
_`formule`_

#### Weergave · `formule_expressie` 🤖

```json
{
  "expressie": "CR = Vlottende activa / Schulden op korte termijn",
  "eenheid": "dimensieloos (verhouding)"
}
```

### Teller — vlottende activa 🤖  
_`subconcept`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Noemer — schulden op korte termijn 🤖  
_`subconcept`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Interpretatie — drempelwaarden 🤖  
_`vuistregel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Beperking — voorraden zijn niet altijd liquide 🤖  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Sectorafhankelijkheid 🤖  
_`vuistregel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Relatie met werkkapitaalbehoefte 🤖  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Beperking — momentopname op balansdatum 🤖  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `vergelijkbaar_met`
- [[quick-ratio]] — De quick ratio sluit voorraden uit de teller uit, waardoor een strengere liquiditeitsmeting ontstaat; de current ratio is ruimer en overschat de liquiditeit als de voorraden illiquide zijn.
    - **Gelijkenissen**:
        - Beide meten kortetermijnliquiditeit als verhouding van activa tot schulden op korte termijn.
        - Beide zijn gebaseerd op balanswaarden per afsluitdatum.
    - **Verschillen**:
        - Quick ratio sluit voorraden (en soms overlopende posten) uit.
        - Current ratio is altijd ≥ quick ratio voor dezelfde onderneming.
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken de termen soms door elkaar; de keuze hangt af van hoe liquide de voorraden zijn.
- [[cash-ratio]] — De cash ratio is de meest conservatieve liquiditeitsratio: alleen geldbeleggingen en liquide middelen in de teller. Relevant bij acute liquiditeitsnood.
    - **Gelijkenissen**:
        - Beide zijn liquiditeitsratios die kortlopende schulden als noemer gebruiken.
    - **Verschillen**:
        - Cash ratio bevat enkel de meest liquide activa; current ratio bevat alle vlottende activa.
        - Cash ratio < quick ratio ≤ current ratio voor dezelfde onderneming.
    - ⚠️ **Verwarringsrisico**: De drie liquiditeitsratios worden soms verward; ze vormen een spectrum van liquiditeitsstringentie.
### `beinvloed_door`
- [[werkkapitaalbehoefte]] 🤖 — Een stijgende werkkapitaalbehoefte druk de current ratio omlaag als de financiering niet mee groeit.
- [[voorraden]] 🤖 — Omvang en liquiditeit van de voorraden bepalen mede de betrouwbaarheid van de current ratio als liquiditeitsmaatstaf.
- [[schulden-op-korte-termijn]] 🤖 — Elke toename van de kortlopende schulden (bv. herschikking van langlopend naar kortlopend deel) vermindert de current ratio direct.
### `valt_onder`
- [[jaarrekeninganalyse]] 🤖
### `triggert`
- [[faillissementspredictie-modellen]] 🤖 — Een structureel lage current ratio is een van de inputvariabelen in modellen zoals Altman Z-score en Daelen-model voor faillissementspreventie.
- [[continuiteit-going-concern]] 🤖 — Een aanhoudend lage of dalende current ratio is een indicator die de auditor in overweging neemt bij de beoordeling van de going-concern-veronderstelling.
