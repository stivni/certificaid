---
title: "Achtergestelde lening"
concept_type: "instrument"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/achtergestelde-lening.json"
---

# Achtergestelde lening

_Instrument_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

## Voorkennis & leespad

**Voorvereisten**: [[eigen-vermogen]] · [[schulden-op-korte-termijn]] · [[vorderingen-op-meer-dan-een-jaar]]
**Naast relevant**: [[obligatielening]] · [[banklening-investeringskrediet]] · [[kapitaalverhoging]] · [[schuldgraad]]
**Volgkennis**: [[vennootschapsbelasting]] · [[liquidatiereserve]]

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
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**👍 Voordeel**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**⚠️ Risico**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Achterstellingsclausule  
_`regel`_

### Boekhoudkundige verwerking (Belgisch GAAP)  
_`regel`_

#### Weergave · `boeking`

```json
{
  "omschrijving": "Ontvangst achtergestelde lening",
  "debet": [
    {
      "rekening": "550",
      "omschrijving": "Kredietinstelling (rekening-courant)",
      "bedrag": "100.000"
    }
  ],
  "credit": [
    {
      "rekening": "173",
      "omschrijving": "Achtergestelde leningen (meer dan 1 jaar)",
      "bedrag": "100.000"
    }
  ]
}
```

### Rentebehandeling in de vennootschapsbelasting  
_`regel`_

### Thin capitalisation — renteaftrekbeperking  
_`drempel`_

### Terugbetaling en opzegging  
_`begrip`_

### Roerende voorheffing op rente  
_`regel`_

### Audit-aandachtspunten  
_`risico`_

## Relaties

### `vergelijkbaar_met`
- [[obligatielening]] 🤖 — Beide zijn schuldfinancieringsinstrumenten; obligatieleningen zijn evenwel verhandelbaar en doorgaans marktgebonden, terwijl achtergestelde leningen bilateraal en contractueel zijn.
    - **Gelijkenissen**:
        - Beide kwalificeren als vreemd vermogen op de balans
        - Beide genereren fiscaal aftrekbare interest (mits arm's length)
    - **Verschillen**:
        - Obligatielening is verhandelbaar op kapitaalmarkt; achtergestelde lening niet
        - Obligatielening vereist specifieke prospectus- en notificatieformaliteiten bij publieke uitgifte
        - Achterstelling is kenmerkend voor achtergestelde lening, niet automatisch bij obligatielening
    - ⚠️ **Verwarringsrisico**: Student kan ten onrechte aannemen dat een achtergestelde obligatielening en een gewone obligatielening boekhoudkundig identiek worden verwerkt — het achtergesteld karakter heeft implicaties voor de toelichting en de solvabiliteitsanalyse.
- [[banklening-investeringskrediet]] 🤖 — Beide zijn schuldfinancieringsvormen op meer dan één jaar, maar een banklening is gewone schuld (senior) terwijl een achtergestelde lening bewust in rang wordt achtergesteld.
    - **Gelijkenissen**:
        - Beide verwerkt als financiële schuld op meer dan één jaar (rekening 17x)
        - Beide genereren interestlasten die aftrekbaar kunnen zijn
    - **Verschillen**:
        - Banklening is senior schuld; achtergestelde lening staat lager in rangorde bij faillissement
        - Achtergestelde lening heeft doorgaans hogere rentevoet wegens hoger risico voor de kredietgever
        - Banklening vereist gebruikelijk zekerheden; achtergestelde lening heeft die minder snel
    - ⚠️ **Verwarringsrisico**: Verwarring mogelijk over waarom een achtergestelde lening van aandeelhouder beter scoort in bancaire solvabiliteitsanalyse dan een gewone aandeelhouderslening.
### `valt_onder`
- [[financiele-verrichtingen-categorie]] 🤖 — Een achtergestelde lening is een financieel instrument dat onder de bredere categorie van financieringsverrichtingen valt.
### `beinvloed_door`
- [[transfer-pricing]] 🤖 — Bij intra-groepsleningen moet de rente op een achtergestelde lening voldoen aan arm's length-voorwaarden; transfer pricing-documentatie is vereist bij overschrijding van drempels.
- [[vennootschapsbelasting]] 🤖 — Renteaftrek, thin capitalisation-beperking en mogelijke herkwalificatie als dividend zijn allen vennootschapsbelasting-vraagstukken die rechtstreeks de keuze voor en structurering van een achtergestelde lening beïnvloeden.
- [[schuldgraad]] 🤖 — Een achtergestelde lening verhoogt de schuldgraad-ratio, maar kan door sommige analisten worden herklassificeerd als quasi-eigen vermogen bij de berekening van de gecorrigeerde schuldgraad.
### `triggert`
- [[alarmbel]] 🤖 — Een achtergestelde aandeelhouderslening wordt soms ingezet om de alarm-bel-procedure te vermijden of op te lossen door de netto-actiefpositie te herstellen; omgekeerd kan de noodzaak ervan een signaal zijn dat de alarm-bel al of bijna aan de orde is.
