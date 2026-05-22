---
title: "Abc methode"
concept_type: "procedure"
schema_version: "2.1"
status: "seed"
tags:
  - concept
  - schema-2.1
  - ongeverifieerd
gegenereerd_uit: "data/concepten/records/abc-methode.json"
---

# Abc methode

_Procedure_

Model: `claude-sonnet-4-6` · Wave: `quick-pass-run1-20260522`

> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd
> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang `claims_checken` niet is uitgevoerd.

**Synoniemen**: Activity-Based Costing · ABC-kostprijsberekening

## Gebruikscontext


**🟢 Indicaties**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**🔴 Contra-indicaties**
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>
- 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

**▶️ Trigger start**: 🤖  <small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Inhoud

### Stap 1 — Identificatie van activiteiten 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 2 — Vorming van activiteitenpools (cost pools) 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 3 — Bepaling van kostendrijvers (cost drivers) 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 4 — Berekening van het kostendrijvertarief 🤖  
_`stap`_

#### Weergave · `formule_expressie`

```json
{
  "formule": "Kostendrijvertarief = Totale poolkost / Totaal aantal kostendrijvereenheden"
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 5 — Toewijzing van kosten aan kostendragers 🤖  
_`stap`_

#### Weergave · `formule_expressie`

```json
{
  "formule": "Indirecte kost kostendrager = Σ (verbruik activiteit_i × kostendrijvertarief_i)"
}
```

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

### Stap 6 — Interpretatie en beslissingsondersteunend gebruik 🤖  
_`stap`_

<small>📚 claude-sonnet-4-6 — _ai_model_ — (2026-05-22)</small>

## Relaties

### `valt_onder`
- [[kostprijsmethoden]] 🤖 — De abc-methode is één van de kostprijsmethoden (kader) naast full costing en direct costing.
### `vergelijkbaar_met`
- [[full-costing]] 🤖 — Beide methoden rekenen indirecte kosten toe aan producten, maar full costing gebruikt vereenvoudigde verdeelsleutels terwijl abc-methode activiteiten als tussenstation gebruikt.
    - **Gelijkenissen**:
        - Beide wijzen indirecte kosten toe aan kostendragers.
        - Beide resulteren in een volledig kostprijsinzicht inclusief overhead.
    - **Verschillen**:
        - Full costing gebruikt enkelvoudige verdeelsleutels (bv. directe arbeidsuren); abc-methode gebruikt meerdere activiteitsgebonden kostendrijvers.
        - Abc-methode is complexer in opzet maar levert accuratere kostprijzen bij diverse productenmix.
    - ⚠️ **Verwarringsrisico**: Studenten verwarren soms 'full costing met meerdere kostenplaatsen' met abc-methode; het onderscheid zit in de keuze van de kostendrijver (activiteit vs. volumemaatstaf).
- [[direct-costing]] 🤖 — Direct costing rekent enkel variabele kosten toe aan producten; abc-methode rekent ook vaste indirecte kosten via activiteiten toe — ander filosofisch vertrekpunt.
    - **Gelijkenissen**:
        - Beide zijn kostprijsmethoden gericht op beslissingsondersteuning.
    - **Verschillen**:
        - Direct costing sluit vaste kosten uit de productcalculatie; abc-methode includeert ze via activiteiten.
        - Direct costing is eenvoudiger in opzet; abc-methode is complexer maar vollediger.
    - ⚠️ **Verwarringsrisico**: Verwarring bij de vraag of vaste kosten al dan niet worden toegerekend: direct costing = neen, abc = ja (maar via activiteiten, niet via volumemaatstaf).
### `vereist`
- [[analytische-boekhouding]] 🤖 — De abc-methode vereist een goed functionerende analytische boekhouding als databasis voor de identificatie en meting van activiteiten en kostendrijvers.
