---
title: "Aangifte vennootschapsbelasting"
concept_type: "procedure"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/aangifte-vennootschapsbelasting.json"
---

# Aangifte vennootschapsbelasting

_Procedure_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Afk.**: aangifte VenB

## Gebruikscontext


**📋 Voorwaarden**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**🟢 Indicaties**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**▶️ Trigger start**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⏹ Trigger einde**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: ❓  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Stap 1 — Bepalen boekhoudkundig resultaat  
_`stap`_

### Stap 2 — Verworpen uitgaven bijtellen  
_`stap`_

### Stap 3 — Andere positieve correcties  
_`stap`_

### Stap 4 — Aftrekken in volgorde (DBI, innovatie, investeringsaftrek, …)  
_`stap`_

### Stap 5 — Belastbare grondslag en tarief toepassen  
_`stap`_

### Stap 6 — Verrekening voorheffingen, voorafbetalingen en vermeerderingen  
_`stap`_

### Stap 7 — Indiening via Biztax en bewaking termijnen  
_`stap`_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]] 🤖 — De aangifte is de uitvoering van de compliance-verplichting binnen het bredere regime van de vennootschapsbelasting.
### `vereist`
- [[belastbare-grondslag-vennootschapsbelasting]] 🤖 — De aangifte kan pas worden ingevuld na berekening van de belastbare grondslag via de fiscale correctieronde.
- [[voorafbetalingen-vennootschapsbelasting]] 🤖 — Tijdige voorafbetalingen zijn een integraal onderdeel van de aangifte-cyclus: onvoldoende voorafbetaling wordt in de aangifte verrekend als vermeerdering.
### `triggert`
- [[aanslag-cyclus]] 🤖 — De ingediende aangifte is de formele trigger voor de aanslag-cyclus door de administratie.
### `beinvloed_door`
- [[verworpen-uitgaven]] 🤖 — De omvang van verworpen uitgaven heeft directe invloed op het fiscale resultaat in de aangifte.
- [[overgedragen-verliezen]] 🤖 — Overgedragen verliezen uit vorige aanslagjaren worden in de aangifte als aftrek verrekend en beïnvloeden de belastbare grondslag.
- [[bijzondere-aanslagen-venb]] 🤖 — Bijzondere aanslagen (bv. op geheime commissielonen, verworpen uitgaven geheime aard) worden via de aangifte of ambtshalve aanslag gevestigd en verhogen de belastingdruk.
### `vergelijkbaar_met`
- [[aangifte-pb]] 🤖 — Beide zijn jaarlijkse verplichte aangiften bij de directe belastingen, maar het toepassingsgebied (rechtspersonen vs. natuurlijke personen) en de aangifte-structuur (Biztax vs. Tax-on-web) verschillen fundamenteel.
    - **Gelijkenissen**:
        - Jaarlijkse indieningsplicht via elektronisch platform
        - Correctieronde op boekhoudkundig/werkelijk inkomen
        - Bezwaarprocedure na aanslag
    - **Verschillen**:
        - VenB: Biztax / Personenbelasting: Tax-on-web
        - VenB: vennootschapsrechtspersonen / PB: natuurlijke personen
        - VenB: geen belastingvrije som, eigen aftrekkenstructuur / PB: belastingvrije som, heffingsschijven
    - ⚠️ **Verwarringsrisico**: Zelfstandigen die zowel PB (baten/winst) als mandaat in een vennootschap (VenB) hebben, kunnen de twee aangiftes verwarren.
