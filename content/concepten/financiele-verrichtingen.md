---
title: "Financiële verrichtingen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - gebeurtenis
ankers:
  - 1.1.II.O
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/financiele-verrichtingen.json"
---

# Financiële verrichtingen

_Balanspost_

🏢 Entiteit · 📅 Gebeurtenis · Anchors: `1.1.II.O` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: financieel resultaat · klasse 65-75

## Definitie

📖 **Financiële verrichtingen** zijn de **terugkerende** financiële kosten en opbrengsten van een onderneming, geboekt in **MAR-klasse 65** (kosten) en **MAR-klasse 75** (opbrengsten). Ze vormen het **financieel resultaat** dat tussen het bedrijfsresultaat (klasse 60-65/70-74 voor het bedrijfsdeel — exclusief 65) en het niet-recurrent resultaat (66/76) op de resultatenrekening verschijnt. Typische posten: **rentelasten op leningen**, **rente-opbrengsten op vorderingen**, **disconto- en provisiekosten** bij bankverrichtingen, **agio bij obligatie-uitgifte**, **valutaresultaten** en **waardeverminderingen op financiële vaste activa**.

<small>📚 KB 21-10-2018 — Bijlage 1 MAR — Klasse 65 + 75 — _kb_</small>

## Substantie

📖 **MAR-klasse 65 — Financiële kosten** (selectie):
- **650 Rentekosten** op schulden (banklening, obligatie, kasgeld-kredieten)
- **651 Provisiekosten** voor bankgaranties, kredieten
- **652 Minderwaarden op realisatie van vlottende activa** (excl. handels-)
- **653 Disconto op vorderingen** (factoring-kosten)
- **654 Negatieve wisselresultaten**
- **656 Voorzieningen voor financiële risico's**
- **657 Negatieve waardeverminderingen op vlottende activa**

**MAR-klasse 75 — Financiële opbrengsten**:
- **750 Opbrengsten uit financiële vaste activa** (dividenden, interest)
- **751 Opbrengsten uit vlottende financiële activa** (intresten op deposito's, kasbons)
- **752 Meerwaarden op realisatie van vlottende activa**
- **753 Subsidies in kapitaal en in intrest** (rentesubsidies)
- **754 Positieve wisselresultaten**
- **756 Terugnemingen van voorzieningen voor financiële risico's**

**Onderscheid met klasse 66/76**: financiële verrichtingen zijn **recurrent** — een lening die loopt sinds jaren genereert elk boekjaar interest. Niet-recurrente verrichtingen zijn éénmalig of buitengewoon.

<small>📚 KB 21-10-2018 — Bijlage 1 MAR — Klasse 65 + 75 — _kb_</small>

## Rationale

🔗 De afscheiding van financiële verrichtingen van het bedrijfsresultaat heeft een belangrijk **analytisch doel**: lezers van de jaarrekening kunnen het **operationele rendement** (bedrijfsresultaat) onderscheiden van het effect van de **financieringsstructuur** (financieel resultaat). Twee identieke ondernemingen met dezelfde EBIT (bedrijfsresultaat) maar verschillende leverage (eigen vermogen versus banklening) zullen dezelfde bedrijfsmarge tonen maar een verschillend financieel resultaat — wat ratio-analyse zoals dekking-rente-lasten of EBITDA-margin transparant maakt.

<small>📚 claude-opus-4-7 — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### ⚙️ Rentelast op banklening (650)  
_`mechanisme`_

📖 **Scenario**: Banklening van 200.000 EUR aan 4 % jaarlijkse rente, kwartaal-betaling.

**Kwartaalboeking** (rente = 200.000 × 4% / 4 = 2.000 EUR):
```
650 Rentekosten op schulden       D 2.000
   55 Bank                         C 2.000
```

Voor de **toerekening per boekjaar**: bij een banklening die kwartalen doorloopt op balansdatum is een **toe-te-rekenen rente** (492) nodig voor de fractie tussen laatste betalingsdatum en jaareinde.

<small>📚 KB 21-10-2018 — MAR — Rekening 650 — _kb_</small>

### ⚙️ Valutaresultaat — wisselverschillen op vorderingen/schulden  
_`mechanisme`_

📖 **Scenario**: Een factuur van 10.000 USD wordt verstuurd bij koers 0,90 EUR/USD = 9.000 EUR boekwaarde. Betaling ontvangen 3 maanden later bij koers 0,95 EUR/USD = 9.500 EUR.

**Initiële boeking**:
```
400 Vorderingen op klanten        D 9.000
   70 Omzet                       C 9.000
```

**Bij betaling**:
```
55 Bank                           D 9.500
   400 Vorderingen                 C 9.000
   754 Positieve wisselresultaten  C 500
```

Bij **balansdatum** voor nog niet vereffende vreemdvalutavorderingen: herwaardering aan slotkoers met boeking van het verschil (754 of 654). Bij waardedaling: **657 Negatieve waardeverminderingen op vlottende activa** (volgens art. 3:43 KB).

<small>📚 KB 29-04-2019 WVV — art. 3:43-44 — _kb_</small>

## Valkuilen

### ⚠️ Klasse 65/75 verwarren met 66/76

**Verkeerde assumptie**: Alle wisselverliezen of waardeverminderingen op financiële activa horen bij 'uitzonderlijk' (66).

**Kernpunt**: **Recurrente** financiële operaties (jaarlijkse interest, normale valutaresultaten op exporten, waardeverminderingen op vlottende handels-vorderingen) horen in **65/75**. Klasse **66/76** is voor **eenmalige, materiële, niet-recurrente** gebeurtenissen — meerwaarde bij verkoop van een dochteronderneming, herstructureringskost, schade-uitkering bij brand.

<small>📚 KB 21-10-2018 — MAR — Klasse 65/75 vs 66/76 — _kb_</small>

## Verder lezen (scope-out)

- → Niet-recurrente verrichtingen (klasse 66/76) → [[niet-recurrente-verrichtingen]] _(moet-verwijzen)_
- ↪ Schuldfinanciering (rente-context) _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vergelijkbaar_met`
- [[niet-recurrente-verrichtingen]]
    - **Gelijkenissen**:
        - Beide buiten het bedrijfsresultaat
        - Beide hebben symmetrische kost-/opbrengstklassen (65/75 vs 66/76)
    - **Verschillen**:
        - Financieel = recurrent + financierings-gerelateerd
        - Niet-recurrent = eenmalig + materieel + buitengewoon
    - ⚠️ **Verwarringsrisico**: Stagiairs classificeren een grote eenmalige meerwaarde verkeerd in klasse 75 ipv 76.
