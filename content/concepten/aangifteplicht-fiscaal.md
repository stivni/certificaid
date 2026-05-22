---
title: "Aangifteplicht fiscaal"
concept_type: "kader"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/aangifteplicht-fiscaal.json"
---

# Aangifteplicht fiscaal

_Kader_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: belastingaangifte · fiscale aangifte · aangifte

## Voorkennis & leespad

**Voorvereisten**: [[fiscale-beginselen]] · [[fiscale-actoren]] · [[toepassingsgebied-belasting]]
**Naast relevant**: [[fiscale-procedure-belastingplichtige]] · [[taxatieprocedure]] · [[aanslagtermijnen-fiscaal]]
**Volgkennis**: [[aangifte-pb]] · [[aangifte-vennootschapsbelasting]] · [[belasting-niet-inwoners]]

## Gebruikscontext


**✅ Voor**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**📋 Voorwaarden**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**🟢 Indicaties**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Soorten belastingaangiften 🤖  
_`begrip`_

#### Personenbelasting (PB) 🤖  
_`begrip`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

#### Vennootschapsbelasting (VenB) 🤖  
_`begrip`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

#### Rechtspersonenbelasting (RPB) 🤖  
_`begrip`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

#### Belasting der niet-inwoners — natuurlijke personen (BNI/nat) 🤖  
_`begrip`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

#### Belasting der niet-inwoners — vennootschappen (BNI/ven) 🤖  
_`begrip`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Indieningstermijnen 🤖  
_`regel`_

#### Weergave · `tabel`

```json
{
  "kolommen": [
    "Belasting",
    "Indieningstermijn (standaard)",
    "Platform",
    "Mandataris-termijn"
  ],
  "rijen": [
    [
      "PB",
      "Eind juni (papier) / eind juli (online)",
      "MyMinfin / Tax-on-web",
      "Oktober (jaar na inkomstenjaar)"
    ],
    [
      "VenB",
      "7 maanden na afsluiting boekjaar (min. 1 maand na AV)",
      "Biztax",
      "Zelfde als vennootschap"
    ],
    [
      "RPB",
      "Zelfde als VenB",
      "Biztax",
      "Zelfde als rechtspersoon"
    ],
    [
      "BNI/nat",
      "Parallel aan PB",
      "MyMinfin",
      "Oktober"
    ],
    [
      "BNI/ven",
      "Parallel aan VenB",
      "Biztax",
      "Zelfde"
    ]
  ]
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Ambtshalve aanslag bij niet-aangifte 🤖  
_`risico`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Elektronische indiening en mandaat 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Volledigheid en correctheid van de aangifte 🤖  
_`principe`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Vooraf ingevulde gegevens en gegevensuitwisseling 🤖  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Rechtzetting van een ingediende aangifte 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Fiscale fiches door derden-betalers 🤖  
_`mechanisme`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `bevat`
- [[aangifte-pb]] — Personenbelasting-aangifte is het uitvoeringsinstrument van de aangifteplicht voor rijksinwoners (nat. personen).
- [[aangifte-vennootschapsbelasting]] — VenB-aangifte is het uitvoeringsinstrument voor vennootschappen.
- [[belasting-niet-inwoners]] — BNI is het regime voor niet-rijksinwoners; de aangifteplicht geldt ook hier.
### `vereist`
- [[fiscale-actoren]] — Kennis van wie belastingplichtige is en wie de administratie is, is voorwaarde voor toepassing.
- [[fiscale-beginselen]] — Beginselen zoals legaliteitsbeginsel en rechtszekerheid vormen de grondslag van de aangifteplicht.
### `beinvloed_door`
- [[aanslagtermijnen-fiscaal]] — De aanslagtermijn bepaalt hoe lang na de aangifte de administratie nog kan aanslaan of rechtzetten.
### `triggert`
- [[taxatieprocedure]] — Niet-indiening of onvolledige aangifte triggert de ambtshalve aanslagprocedure.
### `vergelijkbaar_met`
- [[fiscale-procedure-belastingplichtige]] — Aangifte is de eerste stap in de bredere fiscale procedure (aangifte → aanslag → bezwaar → beroep).
    - **Gelijkenissen**:
        - Beide zijn onderdeel van het fiscale controlesysteem
        - Beide raken de verhouding belastingplichtige–administratie
    - **Verschillen**:
        - Aangifteplicht is het indienen van gegevens; fiscale procedure omvat ook bezwaar, beroep, invordering
        - Aangifteplicht is een actieve plicht; procedurerechten zijn reactief
