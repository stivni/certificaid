# Samenvatting-render — v1 (Sonnet of mens)

**Doel**: genereer een markdown-samenvatting uit een YAML-script + schrijfregels. Lichte MCP-verificatie (call-budget < 3) — meeste claims zijn al in de leerstukken geverifieerd.

**Voor**: Sonnet-uitvoeringsagent OF mens die deterministisch hand-rendert.

**Output**: één markdown-bestand op `content/studiemateriaal/<po-slug>/samenvatting.md`.

**Verschil met leerstuk-render** + **oefening-render**:
- Geen `<details>`-blokken (anders dan oefening)
- Geen pedagogische "Antwoord in één blik"-structuur (anders dan leerstuk)
- Wel: vaste blok-structuur (take-away + optionele blokken + valkuilen + doorklik), telegram-stijl, tabellen/diagrammen/formules dominant

---

## Standaard prompt-template

Plak in een `Agent`-call (general-purpose subagent_type) en vul placeholders.

```markdown
Je bent een Sonnet-uitvoeringsagent in het certificaid-project. Je opdracht:
genereer een markdown-samenvatting uit een YAML-script + schrijfregels.

Output: één bestand `<<OUTPUT_PATH>>`.

## Lees deze inputs in deze volgorde

1. **`data/samenvattingen/SCHEMA.md`** — schema-uitleg + sectie-types
2. **`data/samenvattingen/<<SLUG>>.yaml`** — het samenvatting-script
3. **`docs/samenvatting-schrijfregels.md`** — stijl-regels (telegram-stijl, tabellen-dominant, 2-4 A4 cap)
4. Eventueel: bestaande PO 1.4 samenvatting `content/studiemateriaal/1-4/samenvatting.md` als stijl-referentie

## Call-budget — MAX 3 RAG-calls

Claims in een samenvatting zijn al door de leerstukken bevestigd. Verifieer alleen:
- Drempelbedragen of tarieven die je expliciet citeert
- Wettelijke verwijzingen die in geen enkel leerstuk staan (zeldzaam)
- Bij twijfel: overschrijf gewoon de wikilink-pointer, niet de wettekst

## Render-regels

**Frontmatter** uit `meta`:
```yaml
---
title: "Samenvatting PO <po> — <titel>"
description: "<meta.beschrijving>"
explorer_title: "<meta.explorer_title>"
tags:
  - samenvatting
  - po-<po>
---
```

**Intro-callout** (verplicht, web-only):
```markdown
<div class="no-print">

> **Samenvatting — kapstok voor herhaling.** <inhoud uit intro.callout_beat>. Voor verhaal en routekaart: [[studiemateriaal/<po-slug>|minicursus PO <po>]].

</div>
```

**Sectie-nummering**: render automatisch H2-nummers in volgorde:
1. Take-away (verplicht, altijd H2 nr 1)
2. Elke `extra_blokken[]` in opgegeven volgorde (H2 nr 2, 3, ...)
3. Valkuilen (H2)
4. Verdieping (H2, in `<div class="no-print">`)

**Take-away**:
```markdown
## 1. Take-away — wat je écht moet weten

- <insight-bullet 1>
- <insight-bullet 2>
- ...
```

**Extra blok — `tabel-vergelijking`**:
```markdown
## <N>. <titel>

<intro-paragraaf, indien aanwezig>

| <kolom 1> | <kolom 2> | ... |
|---|---|---|
| ... | ... | ... |

> **Noot.** <noot-tekst>
```

**Extra blok — `mermaid`**:
```markdown
## <N>. <titel>

<intro-paragraaf>

```mermaid
flowchart <TD of LR — uit mermaid_type>
    <code uit yaml>
```
```

**Extra blok — `tabellen-en-formules`** (compositie van H3 sub-blokken):
```markdown
## <N>. <titel>

### <sub_titel van eerste sub_blok>

<inhoud — tabel of formule>

### <sub_titel van volgend sub_blok>
...
```

Voor `type: formule` sub-blok: `<beschrijving>` als 1 zin proza, dan `$$<formule>$$` op aparte regel.

**Extra blok — `prose-blok`**:
```markdown
## <N>. <titel>

<2-3 paragrafen op basis van beats — telegram-stijl, geen verhalend register>
```

**Valkuilen** — `format: tabel`:
```markdown
## <N>. Klassieke valkuilen (examen-radar)

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| <valkuil> | <misvatting> | <scherpe waarheid> |
```

`format: bullets`:
```markdown
## <N>. Klassieke valkuilen (examen-radar)

- ⚠️ **<valkuil>**: <korte uitleg>
```

**Verdieping** (web-only):
```markdown
<div class="no-print">

## <N>. Verdieping

### Leerstukken — voor pedagogische opfris

Werkt iets niet meer scherp? Klik door naar het leerstuk dat het uitwerkt:

- [[<slug>]] — <hint>

### Concept-fiches — voor definitorisch detail

Voor wie een wettekst-pointer of nauwkeurige definitie zoekt:

**<label van groep>** — [[concept-1]] · [[concept-2]] · ...

**<label van volgende groep>** — [[concept-3]] · ...

</div>
```

**Footer**:
```markdown
---

*<meta.footer>*
```

## Stijl-regels (verplicht)

- **Telegram-stijl**: dichtheid > verhaal. Geen "wij" / "ik".
- **Geen wetsartikel-nummers** in lopende tekst — pointers OK ("WVV art. X:YY")
- **Geen drempelbedragen hardcoded** — Cijferzakboekje-pointer of tarief-record-wikilink
- **B-GAAP vs IFRS** expliciet waar relevant
- **Wikilinks**: `[[studiemateriaal/<po-slug>|minicursus PO <po>]]` voor minicursus; `[[<leerstuk-slug>]]` voor leerstukken in hetzelfde PO; `[[<concept-id>]]` voor concept-fiches
- **Mermaid horizontaal (LR)** voor stappenplannen; TD alleen voor hiërarchische bomen / beslisbomen met ja/nee-takken
- **Print-cap**: 2-4 A4. Bij overschrijding: rapporteer in `<<RAPPORT>>` en flag overschot

## Werkstroom

1. Lees alle inputs
2. **Plan call-budget** vóór je begint — welke 0-3 RAG-calls écht nodig
3. Schrijf hele samenvatting in één doorloop via Write naar `<<OUTPUT_PATH>>`
4. Check checklist:
   - [ ] Frontmatter met `samenvatting`-tag
   - [ ] Intro-callout met "kapstok voor herhaling"-instructie
   - [ ] Take-away als H2 nr 1
   - [ ] Verplichte blokken: take-away + valkuilen + verdieping
   - [ ] Optionele blokken in opgegeven volgorde
   - [ ] Geen wetsartikel-nummers in lopende tekst
   - [ ] Print-check: ≤ 4 A4 (visueel inschatten op basis van blok-count en tabel-rijen)
5. Rapporteer max 6 bullets:
   - Woordaantal + geschatte A4-cap-naleving
   - RAG-calls (zou < 3 moeten zijn)
   - Aantal blokken gerenderd (verplichte + optionele)
   - Eventuele weerleggingen
   - Pedagogische gaps (script-verfijning kandidaat?)

Begin nu.
```

---

## Hoe in te zetten

1. Vul placeholders:
   - `<<OUTPUT_PATH>>` — bv. `content/studiemateriaal/1-8/samenvatting.md`
   - `<<SLUG>>` — bv. `1-8`
   - `<<RAPPORT>>` — vrije tekst-tag voor het terug-rapport

2. Start `Agent` met `subagent_type: general-purpose`.

3. **Bij kleine wijzigingen** (titel-tweak, beat-herformulering, valkuil-rij toevoegen): render zelf via Edit op de markdown EN op de YAML — drempel verleggen volgens feedback uit eerdere render-batches.

4. **Bij eerste-versie van een PO-samenvatting**: render via agent voor consistente structuur; rapport-output gebruiken om YAML-script te verfijnen indien nodig.
