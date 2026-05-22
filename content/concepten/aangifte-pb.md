---
title: "Aangifte personenbelasting"
concept_type: "procedure"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/aangifte-pb.json"
---

# Aangifte personenbelasting

_Procedure_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Afk.**: Aangifte PB — **Synoniemen**: aangifte in de personenbelasting · belastingaangifte · aangifte-formulier model 1

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**📋 Voorwaarden**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**▶️ Trigger start**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⏹ Trigger einde**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Stap 1 — Documenten inzamelen en controleren 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 2 — Inkomenscategorieën kwalificeren 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 3 — Beroepskosten vaststellen (forfait of werkelijk) 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 4 — Federale en gewestelijke aftrekken en belastingverminderingen toepassen 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 5 — Gezinssituatie en belastingvrije som vaststellen 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 6 — Elektronisch indienen via Tax-on-Web 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 7 — Aanslagbiljet ontvangen en opvolgen 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `valt_onder`
- [[personenbelasting]] 🤖 — De aangifte is de uitvoerende procedure van het personenbelastingregime.
### `vereist`
- [[inkomstencategorieen-pb]] 🤖 — Correcte kwalificatie van inkomen per categorie is een basisvereiste voor invulling van de aangifte.
- [[beroepskosten-regime-pb]] 🤖 — Keuze tussen forfait en werkelijke kosten is een verplichte stap in de aangifte voor beroepsinkomsten.
- [[belastingberekening-pb]] 🤖 — Na de aangifte voert de belastingadministratie de belastingberekening uit op basis van de aangegeven gegevens.
### `triggert`
- [[aanslag-cyclus]] 🤖 — Indiening van de aangifte activeert de aanslagcyclus bij de belastingadministratie.
- [[aanslagbiljet-pb]] 🤖 — De aangifte leidt tot berekening en verzending van het aanslagbiljet.
### `vergelijkbaar_met`
- [[aangifte-vennootschapsbelasting]] 🤖 — Beide zijn jaarlijkse aangifteprocedures bij de Belgische belastingadministratie; aangifte-pb geldt voor rijksinwoners (natuurlijke personen), aangifte vennootschapsbelasting voor vennootschappen.
    - **Gelijkenissen**:
        - Jaarlijkse indieningstermijn via elektronisch platform
        - Kwalificatie van inkomsten en aftrekposten vóór belastingberekening
        - Aanslagbiljet na verwerking met bezwaarmogelijkheid
    - **Verschillen**:
        - Personenbelasting: progressieve tarieven + belastingvrije som; vennootschapsbelasting: proportioneel tarief
        - Personenbelasting: gewestelijke verminderingen en opcentiemen; vennootschapsbelasting: geen
        - Personenbelasting: gezinssituatie bepalend; vennootschapsbelasting: niet van toepassing
    - ⚠️ **Verwarringsrisico**: Bedrijfsleiders hebben zowel een aangifte-pb (privé) als hun vennootschap een aangifte-venb; de bezoldiging vult vak IV van de aangifte-pb in.
### `beinvloed_door`
- [[voorafbetalingen-pb]] 🤖 — Onvoldoende voorafbetalingen leiden tot een vermeerdering op het aanslagbiljet, wat de nettobelasting via de aangifte beïnvloedt.
- [[fiscale-procedure-pb]] 🤖 — De procedureregels (termijnen, aanslagtermijnen, bezwaartermijnen) kaderen de gehele aangifte-cyclus.
