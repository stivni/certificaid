# Oefening-render — v1 (Sonnet)

**Doel**: genereer een markdown-oefening uit een YAML-script + schrijfregels, mét lichte MCP-verificatie van wettelijke claims.

**Voor**: Sonnet-uitvoeringsagent (of mens die het deterministisch hand-rendert).

**Output**: één markdown-bestand op `content/leerpaden/<po-slug>/oefening.md` (PO-specifiek) of `content/oefeningen/<slug>.md` (cross-PO).

**Verschil met leerstuk-render**:
- Oefening = opgave bovenaan + uitwerking per stap in `<details>`-blok. Markdown krijgt interactieve `<details><summary>`-structuur (toonbaar in Quartz).
- Beperkter call-budget — meeste claims zijn al in onderliggende leerstukken geverifieerd. **Maximaal 3-5 RAG-calls** voor de oefening (alleen claims die expliciet nieuw zijn t.o.v. de leerstukken).

---

## Standaard prompt-template

Plak in een `Agent`-call (general-purpose subagent_type) en vul de placeholders.

```markdown
Je bent een Sonnet-uitvoeringsagent in het certificaid-project. Je opdracht:
genereer een markdown-oefening uit een YAML-script + schrijfregels.

Output: één bestand `<<OUTPUT_PATH>>`.

## Lees deze inputs in deze volgorde

1. **`data/oefeningen/SCHEMA.md`** — schema-uitleg + visualisatie-types
2. **`data/oefeningen/<<SLUG>>.yaml`** — het oefening-script
3. **`docs/leerstuk-schrijfregels.md`** — algemene stijl (tweede persoon, geen wetsartikels in lopende tekst, etc.)
4. **`data/leerstukken/<<RELEVANT_LEERSTUK>>.yaml`** — voor consistentie met onderliggende uitleg (alleen waar oefening op bouwt)
5. Eventueel referentie-oefening voor STIJL (als bestaand):
   - `content/leerpaden/1-4/oefening.md` (Nordica — eerste POC)

## Call-budget — MAX 5 RAG-calls

Concept-records en bestaande leerstuk-markdown zijn baseline. Voor de oefening:
- Verifieer alleen wettelijke claims die in de oefening NIEUW zijn t.o.v. de gerefereerde leerstukken (lijst die het script bij `wettelijk_fundament` opgeeft is al door de leerstukken bevestigd — niet opnieuw verifiëren)
- Bij twijfel over een drempel of percentage in de opgave-data: 1 RAG-call
- Spendeer eerder tokens aan didactische precisie van de uitwerking-prose

## Render-regels

**Frontmatter** uit `meta`:
```yaml
---
title: "<meta.titel>"
description: "<meta.beschrijving als één lijn>"
explorer_title: "6. Oefening"           # bij plaatsing in een minicursus-leerpad
tags:
  - oefening
  - po-<meta.po>
  - cluster-<meta.cluster>
  - studietijd-<bv. 60-75min>
---
```

**Intro-callout** (verplicht, met expliciete "doe-eerst-zelf"-instructie):
```markdown
<div class="no-print">

> **Oefening — doe eerst zelf, controleer dan.** <inhoud op basis van intro.callout_beat>. Voor verhaal en routekaart: [[leerpaden/<po-slug>|minicursus PO <po>]].

</div>
```

**Opgave-sectie** (H2 `## Opgave`):
- Render `opgave.scenario_beats` als 1-2 prose-paragrafen
- Daarna ALLE opgave-data (groep, tabellen, balansen, resultatenrekening, intra-groep-transacties) in heldere sub-secties (H3) zodat de student één keer kan bekijken vóór hij begint
- Visualisaties volgens types uit `data/leerstukken/SCHEMA.md` (balans-paar = `<div class="balans-twee-koloms">` etc.)

**Uitwerking-sectie** (H2 `## Uitwerking`):
- Per stap één H3 met `meta.titel`
- `instructie_beats` als prose (de vraag aan de student), geformuleerd in tweede persoon imperatief ("Bepaal welke methode...", "Bereken het consolidatieverschil...")
- Daarna een `<details>` blok:

```markdown
<details>
<summary><strong>Oplossing — klik om te tonen</strong></summary>

<prose op basis van uitwerking_beats>

<eventuele uitwerking_visualisaties>

> **Let op.** <prose op basis van valkuil_beat, indien aanwezig>

</details>
```

**Belangrijk**: laat een blank line vóór én na `<details>` en `</details>` (Quartz/markdown-quirk — anders wordt de tabel binnenin niet correct gerenderd).

**Boeking-visualisaties** (inline of via ref) — CBN-stijl:
```markdown
**<titel>**

|     | MAR  | Omschrijving                    | Debet | Credit |
|-----|------|---------------------------------|------:|-------:|
|     | 22-3 | Activa Saga                     | 9,0   |        |
| aan | 280  | Deelneming Saga BVBA            |       | 6,8    |
```

**Reflectie-sectie** (H2 `## Reflectie`):
- Render `afsluiting.reflectie_beats` als prose
- Aan einde optioneel: lijstje "Doelstellingen gedekt" + "Valkuilen geoefend" (compact)

**Verder lezen** (web-only, in `<div class="no-print">`):
```markdown
## Wanneer dit zit, ga dan naar

- [[<slug>]] — <hint>
- ...

(eventueel) → De voorbeeldexamen-pagina van dit PO: [examen-radar](<examenvragen_link>)
```

**Wettelijk fundament** (H2): zelfde formaat als leerstuk-render — bullet-lijst.

**Footer**:
```markdown
---

*<meta.footer>*
```

## Stijl-regels

- Tweede persoon ("je", "bereken", "controleer") — instructie-toon
- Geen wetsartikel-nummers in opgave of uitwerking-prose (alleen in `## Wettelijk fundament`)
- Geen drempelbedragen hardcoded — Cijferzakboekje-pointer of tarief-record-wikilink
- Geen confidence-iconen
- Wikilinks zoals leerstuk-render
- **Mock-cijfers** zijn fictief en intern consistent — niet verifiëren

## Werkstroom

1. Lees alle inputs
2. **Plan call-budget** vóór je begint — welke 0-3 RAG-calls écht nodig (zo nodig)
3. Schrijf hele oefening in één doorloop via Write naar `<<OUTPUT_PATH>>`
4. Check checklist:
   - [ ] Frontmatter met `oefening`-tag
   - [ ] Intro-callout met expliciete "doe-eerst-zelf"-instructie
   - [ ] Opgave volledig vóór de eerste `<details>`
   - [ ] Elke stap: instructie als prose + `<details>` met oplossing
   - [ ] Blank lines rond `<details>`/`</details>`
   - [ ] Geen wetsartikel-nummers in lopende tekst
   - [ ] Wettelijk-fundament-sectie aan einde
5. Rapporteer max 6 bullets:
   - Woordaantal
   - RAG-calls (zou < 5 moeten zijn)
   - Aantal stappen + visualisaties gerenderd
   - Eventuele weerleggingen
   - Pedagogische gaps (script-verfijning?)

Begin nu.
```

---

## Hoe in te zetten

1. Vul placeholders:
   - `<<OUTPUT_PATH>>` — bv. `content/leerpaden/1-4/oefening.md`
   - `<<SLUG>>` — bv. `nordica-consolideren`
   - `<<RELEVANT_LEERSTUK>>` — bv. `hoe-consolideren` (waar de oefening op bouwt)

2. Start `Agent` met `subagent_type: general-purpose`.

3. Bij kleine wijzigingen (titel-tweak, beat-herformulering, getallencorrectie): **render zelf via Edit, niet via agent** — drempel verleggen volgens feedback uit eerdere render-batches.
