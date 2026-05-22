---
title: "Liquidatiereserve"
concept_type: "regime"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/liquidatiereserve.json"
---

# Liquidatiereserve

_Regime_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: VVPR-bis alternatief voor liquidatie

## Voorkennis & leespad

**Voorvereisten**: [[verlaagd-tarief-kleine-vennootschap]] · [[roerende-voorheffing]] · [[vennootschapsbelasting]] · [[resultaatverwerking]]
**Naast relevant**: [[vvprbis]] · [[uitkering-aan-aandeelhouders]] · [[ontbinding-en-vereffening]]

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**🚫 Niet voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**📋 Voorwaarden**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⛔ Uitsluitingen**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**👍 Voordeel**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Aanleg van de liquidatiereserve 🤖  
_`stap`_

#### Weergave · `boeking` 🤖

```json
{
  "regels": [
    {
      "debet": "Resultaatverwerking (winst te bestemmen)",
      "credit": "Liquidatiereserve (passief)",
      "bedrag": "X"
    },
    {
      "debet": "Bijzondere aanslag op liquidatiereserve (belastingkost)",
      "credit": "Te betalen belastingen",
      "bedrag": "0,10 × X"
    }
  ],
  "toelichting": "De bijzondere aanslag van 10 % wordt verwerkt als een bijkomende vennootschapsbelasting in de aangifte van het aanlagjaar."
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Bijzondere aanslag van 10 % 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Uitkering bij effectieve liquidatie (ontbinding) 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Uitkering als dividend vóór 5 jaar na aanleg 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Uitkering als dividend na 5 jaar na aanleg 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Omvorming van bestaande belaste reserves (intern liquidatie-dividend) ❓  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Boekhoudkundige verwerking bijzondere aanslag 🤖  
_`regel`_

#### Weergave · `tabel` 🤖

```json
{
  "kolommen": [
    "Scenario",
    "Bijzondere aanslag",
    "Aanvullende RV bij uitkering",
    "Totale fiscale kost"
  ],
  "rijen": [
    [
      "Uitkering bij liquidatie (ontbinding)",
      "10 %",
      "0 %",
      "10 % (+ gewone VenB)"
    ],
    [
      "Uitkering als dividend na ≥ 5 jaar",
      "10 %",
      "5 %",
      "~14,5 % (+ gewone VenB)"
    ],
    [
      "Uitkering als dividend < 5 jaar",
      "10 %",
      "20 %",
      "~27 % (+ gewone VenB)"
    ],
    [
      "Gewoon dividend (geen regime)",
      "—",
      "30 %",
      "30 % RV (+ gewone VenB)"
    ]
  ]
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Kleine vennootschap als toepassingscriterium 🤖  
_`regel`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `vergelijkbaar_met`
- [[vvprbis]] 🤖 — Beide regimes verlagen de fiscale kost voor aandeelhouders van kleine vennootschappen, maar via verschillende mechanismen: VVPR-bis via nieuwe aandelen en verlaagd RV-tarief (15 % of 20 %), liquidatiereserve via winstparkering met bijzondere aanslag en vrijstelling bij liquidatie.
    - **Gelijkenissen**:
        - Beide gericht op kleine vennootschappen
        - Beide verminderen de totale fiscale druk op winstuitkering
        - Beide zijn niet van rechtswege: de vennootschap maakt een keuze
    - **Verschillen**:
        - VVPR-bis vereist nieuwe inbreng (aandelen na 1 juli 2013); liquidatiereserve is beschikbaar voor alle kleine vennootschappen
        - VVPR-bis geeft onmiddellijk verlaagd tarief; liquidatiereserve vereist wachten of aanvaarden van hogere kost bij vroeg uitkeren
        - Liquidatiereserve is volledig vrij van RV bij liquidatie; VVPR-bis niet
    - ⚠️ **Verwarringsrisico**: Studenten verwarren de twee regimes omdat beide een verlaagd RV-tarief vermelden; het onderscheid in toelatingsvoorwaarden en toepassingsmechanisme is cruciaal.
### `vereist`
- [[verlaagd-tarief-kleine-vennootschap]] 🤖 — Enkel kleine vennootschappen mogen liquidatiereserve aanleggen.
### `beinvloed_door`
- [[resultaatverwerking]] 🤖 — De liquidatiereserve wordt aangelegd als onderdeel van de resultaatverwerking na afsluit van het boekjaar.
- [[roerende-voorheffing]] 🤖 — Het regime beïnvloedt de verschuldigde roerende voorheffing: 0 % bij liquidatie, 5 % na ≥ 5 jaar, of 20 % bij vroege uitkering.
- [[vennootschapsbelasting]] 🤖 — De bijzondere aanslag van 10 % maakt deel uit van de vennootschapsbelasting-aangifte en wordt in dat kader opgelegd en ingevorderd.
- [[uitkering-aan-aandeelhouders]] 🤖 — De regels voor uitkering aan aandeelhouders (winstuitkeringstest, balanstest) gelden ook voor dividenduitkering uit de liquidatiereserve.
### `triggert`
- [[ontbinding-en-vereffening]] 🤖 — Bij effectieve ontbinding en vereffening wordt de liquidatiereserve vrijgesteld van RV; het regime is fiscaal het meest voordelig bij effectieve liquidatie.
