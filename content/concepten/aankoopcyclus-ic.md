---
title: "Aankoopcyclus interne controle"
concept_type: "procedure"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/aankoopcyclus-ic.json"
---

# Aankoopcyclus interne controle

_Procedure_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: inkoopproces · purchase cycle · procure-to-pay cyclus · P2P-cyclus

## Voorkennis & leespad

**Kader**: [[governance-actoren-ic]]
**Voorvereisten**: [[interne-controle-coso]] · [[functiescheiding]]
**Naast relevant**: [[verkoopcyclus-ic]] · [[voorraadcyclus-ic]] · [[hr-cyclus-ic]] · [[productiecyclus-ic]]
**Volgkennis**: [[evaluatie-interne-controle]] · [[ontwerp-interne-controle]]

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**▶️ Trigger start**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⏹ Trigger einde**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Behoeftebepaling en aankoopauthorisatie 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Leverancierskeuze en contractering 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Plaatsen van de bestelling (purchase order) 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Ontvangst en kwaliteitscontrole (goods receipt) 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Facturatieverificatie en drieweg-matching 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Boekhoudkundige verwerking van de leveranciersschuld 🤖  
_`stap`_

#### Weergave · `boeking` 🤖

```json
{
  "omschrijving": "Basisboeking bij ontvangst en goedkeuring factuur (goederen, met btw)",
  "debets": [
    {
      "rekening": "60xx/22xx",
      "label": "Aankopen / Materiële vaste activa",
      "bedrag": "Netto-bedrag"
    },
    {
      "rekening": "4111",
      "label": "Terugvorderbare btw (aftrekbare btw)",
      "bedrag": "Btw-bedrag"
    }
  ],
  "credits": [
    {
      "rekening": "440x",
      "label": "Leveranciers",
      "bedrag": "Totaal factuurbedrag incl. btw"
    }
  ]
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Betalingsprocedure en afsluiting 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `valt_onder`
- [[interne-controle-coso]] 🤖 — De aankoopcyclus is een specifieke procedurecyclus binnen het bredere COSO-kader van interne controle.
### `vereist`
- [[functiescheiding]] 🤖 — Functiescheiding (autoriseren / ontvangen / betalen) is de basisvereiste voor een effectieve aankoopcyclus.
### `vergelijkbaar_met`
- [[verkoopcyclus-ic]] 🤖 — Spiegelproces: verkoopcyclus beheert de uitstroom van goederen en ontvangst van klantbetalingen; aankoopcyclus de instroom van goederen en betaling aan leveranciers.
    - **Gelijkenissen**:
        - Beide cyclussen gebruiken documentstroom en drieweg-matching (bestelling / levering / factuur)
        - Functiescheiding is in beide cyclussen de primaire controlespillar
        - Beide worden door de auditor getest op volledigheid en nauwkeurigheid van de balansposities
    - **Verschillen**:
        - Verkoopcyclus: opbrengstverantwoording is het primaire risico; aankoopcyclus: frauduleuze betalingen en volledigheid schulden
        - Richting geldstroom: aankoopcyclus = uitbetalingen; verkoopcyclus = ontvangsten
- [[voorraadcyclus-ic]] 🤖 — De ontvangstfase van de aankoopcyclus raakt direct aan de voorraadcyclus: goederen die worden ontvangen, worden in de voorraadadministratie opgenomen.
    - **Gelijkenissen**:
        - Beide cyclussen delen de ontvangstbon als sleuteldocument
        - Voorraadtellingen zijn een controlemaatregel die beide cyclussen beïnvloedt
    - **Verschillen**:
        - Voorraadcyclus focust op beheer en waardering van de fysieke voorraden; aankoopcyclus focust op het betalingsproces en de leveranciersschulden
### `gecontroleerd_door`
- [[evaluatie-interne-controle]] 🤖 — De opzet en werking van de aankoopcyclus worden door de accountant/auditor geëvalueerd als onderdeel van de beoordeling van het interne-controlesysteem.
### `beinvloed_door`
- [[fraude]] 🤖 — Onvoldoende interne controle op de aankoopcyclus is een van de meest voorkomende oorzaken van boekhoudkundige fraude (fictieve leveranciers, overbilling).
### `triggert`
- [[schulden-op-korte-termijn]] 🤖 — Goedgekeurde leveranciersfacturen resulteren in leveranciersschulden op korte termijn op de balans.
