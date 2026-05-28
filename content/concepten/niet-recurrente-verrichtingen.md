---
title: "Niet-recurrente verrichtingen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - gebeurtenis
ankers:
  - 1.1.II.P
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/niet-recurrente-verrichtingen.json"
---

# Niet-recurrente verrichtingen

_Balanspost_

🏢 Entiteit · 📅 Gebeurtenis · Anchors: `1.1.II.P` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: uitzonderlijke verrichtingen · klasse 66-76 · buitengewone resultaten

## Definitie

📖 **Niet-recurrente verrichtingen** zijn **eenmalige, materiële, niet-terugkerende** gebeurtenissen die buiten het gewone bedrijfsleven en buiten de gewone financiële cyclus van de onderneming vallen. Ze worden geboekt in **MAR-klasse 66** (niet-recurrente kosten) en **MAR-klasse 76** (niet-recurrente opbrengsten) en verschijnen als afzonderlijke lijn op de resultatenrekening, na het bedrijfsresultaat en het financieel resultaat. Typische voorbeelden: realisatie-meerwaarden of -minderwaarden bij verkoop van materiële of financiële vaste activa, herstructureringskosten, brand- of stormschade, dotaties of terugnemingen van uitzonderlijke voorzieningen, eenmalige uitkoop van een directielid.

<small>📚 KB 21-10-2018 — Bijlage 1 MAR — Klasse 66 + 76 — _kb_</small>

## Substantie

📖 **Drie cumulatieve criteria** voor classificatie als niet-recurrent:
1. **Eenmalig** — niet onderdeel van een terugkerend patroon;
2. **Materieel** — significante impact op het resultaat (niet bagatelle-bedragen);
3. **Niet-terugkerend** — los van de gewone activiteit (operating of financieel).

**MAR-klasse 66 — Niet-recurrente kosten** (selectie):
- **660 Niet-recurrente afschrijvingen + waardeverminderingen op oprichtingskosten + IVA/MVA/FVA**
- **661 Niet-recurrente waardeverminderingen op FVA**
- **662 Voorzieningen voor niet-recurrente bedrijfsrisico's en -kosten**
- **663 Niet-recurrente minderwaarden op realisatie van VA**
- **664-668 Andere niet-recurrente bedrijfskosten**

**MAR-klasse 76 — Niet-recurrente opbrengsten**:
- **760 Terugnemingen van niet-recurrente afschrijvingen**
- **761 Terugnemingen waardeverminderingen FVA**
- **762 Terugnemingen voorzieningen voor niet-recurrente risico's**
- **763 Niet-recurrente meerwaarden op realisatie van VA**
- **764-768 Andere niet-recurrente opbrengsten**

<small>📚 KB 21-10-2018 — Bijlage 1 MAR — Klasse 66 + 76 — _kb_</small>

## Rationale

🔗 De afscheiding van niet-recurrente posten is **essentieel voor financiële analyse**: lezers van de jaarrekening moeten het **duurzame, terugkerende** resultaat (operationeel + financieel) kunnen onderscheiden van **eenmalige, niet-projecteerbare** events. Een vennootschap met een nettowinst van 10 miljoen EUR waarvan 8 miljoen voortkomt uit een eenmalige verkoop van een bedrijfspand heeft een fundamenteel andere **toekomstig genererend vermogen** dan een vennootschap met diezelfde winst uit lopende activiteiten. Klasse 66/76 maakt deze onderscheiding zichtbaar — een belangrijke input voor ratio's zoals **operating margin** of **earning quality**.

<small>📚 claude-opus-4-7 — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### ⚙️ Realisatie-meerwaarde op materiële vaste activa (763)  
_`mechanisme`_

📖 **Scenario**: Verkoop van een bedrijfspand met boekwaarde 300.000 EUR (aanschaffingswaarde 500.000 - afschrijvingen 200.000) voor 450.000 EUR.

**Boeking afboeking activa**:
```
55 Bank                                         D 450.000
220 Afschrijvingen terreinen en gebouwen         D 200.000
   22 Terreinen en gebouwen                      C 500.000
   763 Niet-recurrente meerwaarden op realisatie C 150.000
```
De 150.000 EUR wordt geboekt als **niet-recurrente opbrengst** — eenmalig, materieel, geen onderdeel van de bedrijfsactiviteit.

<small>📚 KB 21-10-2018 — MAR — Rekening 763 — _kb_</small>

### ⚙️ Herstructureringskosten (662 + 663-665)  
_`mechanisme`_

📖 **Scenario**: Vennootschap besluit een productiesite te sluiten. Verwachte kosten: ontslagvergoedingen 800.000 EUR + afboeking machine-park 300.000 EUR + opzeggings-vergoedingen huur 100.000 EUR.

**Bij beslissing** (publieke aankondiging — IAS-37/IFRS-conform):
- Voorziening voor herstructurering aanleggen:
```
662 Voorzieningen voor niet-recurrente bedrijfsrisico's    D 1.200.000
   163 Voorzieningen voor andere risico's                   C 1.200.000
```

Bij **werkelijke aanwending** in latere boekjaren: rekening 163 wordt afgebouwd tegen de werkelijke kost.

<small>📚 KB 21-10-2018 — MAR — Rekening 662 — _kb_</small>

## Valkuilen

### ⚠️ Materialiteit onderschatten

**Verkeerde assumptie**: Elke uitzonderlijke gebeurtenis hoort in klasse 66/76, ongeacht het bedrag.

**Kernpunt**: Een gebeurtenis moet **materieel** zijn voor classificatie als niet-recurrent. Een kleine eenmalige post (bv. 500 EUR verlies bij verkoop kantoorbenodigdheden) blijft in de gewone klasse 64. De materialiteits-drempel volgt uit het algemene materialiteitsoordeel van de onderneming/commissaris — geen vaste regel, maar typisch een paar % van het resultaat.

<small>📚 claude-opus-4-7 — _ai_model_ — (2026-05-28)</small>

### ⚠️ Recurrent fenomeen als niet-recurrent boeken

**Verkeerde assumptie**: Een verkoop van een oude machine elk jaar is niet-recurrent omdat het 'eenmalig per machine' is.

**Kernpunt**: Realisatie-meerwaarden op MVA worden in **klasse 76** geboekt wanneer ze **uitzonderlijk en materieel** zijn. Bij een onderneming die structureel oude machines verkoopt (bv. autohandel-tweedehands) is dit **operationeel** — boeking in klasse 74 of 70. De vraag: zou je dit elk jaar verwachten?

<small>📚 claude-opus-4-7 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Financiële verrichtingen (klasse 65/75 — recurrent) → [[financiele-verrichtingen]] _(moet-verwijzen)_
- ↪ Eindejaarsverrichtingen (boekjaar-afsluit-context) → [[eindejaarsverrichtingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vergelijkbaar_met`
- [[financiele-verrichtingen]]
    - **Gelijkenissen**:
        - Beide buiten het bedrijfsresultaat
        - Symmetrische kost-/opbrengstklassen-structuur
    - **Verschillen**:
        - 65/75: recurrent + financierings-gerelateerd
        - 66/76: eenmalig + materieel + buitengewoon
    - ⚠️ **Verwarringsrisico**: Realisatie-meerwaarden of waardeverminderingen verkeerd classificeren tussen 65/75 en 66/76.
