---
title: "Aanslagbiljet pb"
concept_type: "procedure"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/aanslagbiljet-pb.json"
---

# Aanslagbiljet pb

_Procedure_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: aanslagkohier PB · belastingafrekening personenbelasting

## Voorkennis & leespad

**Kader**: [[fiscale-procedure-pb]]
**Voorvereisten**: [[aangifte-pb]] · [[belastingberekening-pb]] · [[voorheffingen-en-verrekeningen-venb]]
**Naast relevant**: [[aanslagtermijnen-fiscaal]] · [[aanslag-cyclus]]
**Volgkennis**: [[bezwaarprocedure-fiscaal]] · [[invorderingsprocedure-fiscaal]]

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**▶️ Trigger start**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⏹ Trigger einde**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Identificatiegegevens en aanslagjaar 🤖  
_`subconcept`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Samenvatting belastbare basis 🤖  
_`subconcept`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Berekening verschuldigde belasting 🤖  
_`formule`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Verrekening voorheffingen en voorafbetalingen 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Uiterste betaaldatum en betalingsmodaliteiten 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Bezwaartermijn en rechtsmiddelen 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Ambtshalve ontheffing na verstrijken bezwaartermijn 🤖  
_`uitzondering`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `valt_onder`
- [[fiscale-procedure-pb]] — Het aanslagbiljet is de formele uitkomst van de aanslag-fase binnen de fiscale procedure voor de personenbelasting.
- [[aanslag-cyclus]] — Het aanslagbiljet markeert het sluitstuk van de jaarlijkse aanslag-cyclus.
### `vereist`
- [[aangifte-pb]] — De aangifte personenbelasting is de voorwaarde voor de gewone aanslag; zonder aangifte volgt een ambtshalve aanslag.
### `triggert`
- [[bezwaarprocedure-fiscaal]] — Ontvangst van het aanslagbiljet opent de bezwaartermijn van drie maanden.
- [[invorderingsprocedure-fiscaal]] — Bij niet-tijdige betaling van het saldo treedt de invorderingsprocedure in werking.
### `beinvloed_door`
- [[belastingberekening-pb]] — De bedragen op het aanslagbiljet zijn het rechtstreekse resultaat van de belastingberekening personenbelasting.
- [[aanslagtermijnen-fiscaal]] — De datum waarop het aanslagbiljet ten laatste mag worden verstuurd is begrensd door de wettelijke aanslagtermijnen.
### `vergelijkbaar_met`
- [[aangifte-vennootschapsbelasting]] — Het aanslagbiljet personenbelasting is het pendant van de aanslag vennootschapsbelasting; de systematiek (aangifte → aanslag → bezwaar) is gelijkaardig maar de berekeningsregels verschillen fundamenteel.
    - **Gelijkenissen**:
        - Beide zijn formele overheidsbesluiten die een belastingschuld vaststellen
        - Bezwaartermijn van drie maanden geldt in beide gevallen
    - **Verschillen**:
        - PB kent progressieve tarieven en gemeentelijke opcentiemen; VenB kent een vlak tarief
        - PB-aanslag is persoonlijk; VenB-aanslag is op naam van de rechtspersoon
    - ⚠️ **Verwarringsrisico**: Studenten verwarren soms de aanslagtermijnen PB met die van VenB — de basisregels zijn gelijk maar de bijzondere verlengde termijnen kunnen afwijken.
