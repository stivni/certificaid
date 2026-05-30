# Leerstuk-render — v1 (Sonnet)

**Doel**: genereer een markdown-leerstuk uit een YAML-script + voorbeeldgroep-data + schrijfregels, **mét verplichte MCP-verificatie van alle feitelijke claims**.

**Voor**: Sonnet-uitvoeringsagent. Gevalideerd op 5 succesvolle runs voor PO 1.4 leerstukken (mei 2026).

**Output**: één markdown-bestand op de canonical leerstuk-locatie (`content/leerpaden/<po-slug>/<slug>.md` voor PO-specifiek, of `content/leerstukken/<slug>.md` voor cross-PO).

---

## Standaard prompt-template

Plak onderstaande prompt in een `Agent`-call (general-purpose subagent_type) en vul de drie blokken met `<<PLACEHOLDERS>>` in vóór je hem verstuurt.

```markdown
Je bent een Sonnet-uitvoeringsagent in het certificaid-project. Je opdracht:
genereer een markdown-leerstuk uit een YAML-script + voorbeeldgroep-data +
schrijfregels, mét verplichte MCP-verificatie van alle feitelijke claims.

Output: één bestand `<<OUTPUT_PATH>>`.

## Lees deze inputs in deze volgorde

1. **`docs/leerstuk-schrijfregels.md`** — stilistische regels, blok-structuur, lengte-budget, wettekst-conventie.
2. **`data/leerstukken/SCHEMA.md`** — uitleg van het script-schema + visualisatie-types.
3. **`data/leerstukken/<<SLUG>>.yaml`** — het script dat je rendert.
4. **`data/voorbeeldgroepen/<<VOORBEELDGROEP>>.yaml`** — gedeelde data (groepsstructuur, balansen, boekingen, mock_geconsolideerd, mini_cases).
5. **Referentie-leerstukken voor STIJL** (lees alleen wat nodig):
   - `content/leerpaden/1-4/wat-is-een-geconsolideerde-jaarrekening.md` (entry-fiche stijl, korte + RAG-verificatie)
   - `content/leerpaden/1-4/hoe-consolideren.md` (complex "hoe"-leerstuk: diep geneste sub-secties, balans-paar, boekingen, blockquote-asides)
   - `content/leerpaden/1-4/goodwill-bij-consolidatie.md` (specifiek-fiche met afschrijvings-tabel + impairment-uitleg)

## Lengte volgt scope

Geen artificieel target. Script telt N hoofdsecties + M kinderen — schrijf wat het script vraagt, niet meer. Beats getrouw weergeven volstaat. Cap volgens schrijfregels: 800-2000 voor "wat"/"wie", tot ~4500 voor "hoe"-leerstukken die meerdere technieken uitwerken.

## Bron-verificatie via MCP (VERPLICHT vóór schrijven van prose)

Concept-records en het script zijn **baseline**, niet waarheid. Voor elke harde claim — wetsartikel, drempel, regel, timing, percentage, afschrijvingsperiode — verifieer je via MCP:

1. **`mcp__certificaid-rag__zoek_bronnen`** — wetsartikels + CBN-adviezen
   - Default `rerank=false` voor brede zoekvragen (snel)
   - `bron_rollen=["wettekst"]` filter voor enkel wet
   - **Lees de hele paragraaf**: chunks tonen één deel; wetsparagrafen hebben vaak meerdere alinea's met elk een aparte regel (klassiek voorbeeld: WVV art. 1:26 § 2 = meetdatum (alinea 1) + tweejaars-regel (alinea 2) → beide vermelden, niet alleen één)

2. **`mcp__certificaid-rag__lees_record`** + **`mcp__certificaid-rag__zoek_concepten`** — concept-records
   - Voor definitorische precisie in prose (bv. "Wat is goodwill?")
   - Concept-records zijn baseline maar nooit eindbron — bij conflict wint wettekst

3. **`mcp__certificaid-tarieven__zoek_tabellen`** + **`mcp__certificaid-tarieven__lees_tabel`** — cijfers
   - Bij elke wikilink in het script naar een tarief-record: verifieer dat het record bestaat. Indien niet: behoud de link (architecturale intentie), vermeld in rapport.
   - Bij richtcijfers in prose: bevestig of vermeld "Cijferzakboekje"-pointer.

### Specifiek voor dit leerstuk

<<SPECIFIEKE_CLAIMS_OM_TE_VERIFIËREN>>

(bv. "Verifieer KB-WVV art. 3:131 § 1 (afschrijvingsregels positief consolidatieverschil) + § 2 (negatief consolidatieverschil). Lees beide alinea's. Verifieer CBN-advies 2016/7 over de 10-jaar-maximum. Verifieer IFRS 3 en IAS 36 voor de IFRS-impairment-only-claim.")

### Conflict-protocol

- **Script vs wettekst**: vertrouw wettekst. Rapporteer: "Script-claim X weerlegd, gebruikt Y (bron: <ref>)"
- **Concept-record vs wettekst**: vertrouw wettekst. Rapporteer voor eventuele concept-opkuis.
- **Tarief-record bestaat niet, script linkt ernaar**: behoud link (architecturale intentie), vermeld in rapport.

### Wat NIET verifiëren

- Pedagogische metafoor en framing (beats — vertrouw)
- Voorbeeldgroep-cijfers (Aurelia is fictief en intern consistent)
- Vrije prose-keuzes (woordkeuze, alinea-volgorde binnen een sectie)

## Render-regels

**Frontmatter** uit `meta`:
```yaml
---
title: "<meta.titel>"
description: "<meta.beschrijving als één lijn>"
tags:
  - leerstuk
  - po-<meta.po>
  - cluster-<meta.cluster>
---
```

**Intro-callout** (verplicht), inclusief minicursus-link:
```markdown
<div class="no-print">

> **Leerstuk — één vraag, helemaal doorgewerkt.** <inhoud op basis van intro.callout_beat>. Voor verhaal en routekaart: [[leerpaden/<po-slug>|minicursus PO <po>]].

</div>
```

**Antwoord in één blik**:
- H2 `## Antwoord in één blik`
- Beats uitwerken tot 1-2 paragrafen
- Eventuele visualisaties direct daaronder
- Eventuele afsluiter als laatste paragraaf

**Opbouw secties** — render heading op basis van `niveau` veld (2 → `##`, 3 → `###`, 4 → `####`, 5 → `#####`). Voor elke sectie:
- Heading + titel
- Beats uitwerken tot vloeiende pedagogische prose (1-3 zinnen per beat, samengevoegd tot natuurlijke paragrafen). **Niet** letterlijk beat-bewoording overnemen — herformuleer
- Visualisaties op de juiste plek

**Sectie-type `blockquote-aside`** (geen h-tag):
```markdown
> **<intro vet>.** <prose uit beats — 2-3 zinnen samengevoegd>
```

**Visualisatie-types**:

| Type | Render |
|---|---|
| `mermaid` (ref) | ```mermaid blok met `flowchart TD` prefix + code uit `voorbeeldgroep.mermaid_diagrammen.<ref>` |
| `balans-paar` (ref) | `<div class="balans-twee-koloms">` + 2 markdown-tabellen (activa, passiva). Sub-totalen vetgedrukt op rij met **lege eerste cel**. `★` voor intra-groep. `<br>` voor wrap-controle |
| `resultatenrekening` (ref) | 2-koloms staffel-tabel uit `voorbeeldgroep.resultatenrekeningen.<ref>` |
| `boeking` (ref) | 4-koloms T-rekening-tabel `Debet ¦ mln ¦ Credit ¦ mln` uit `voorbeeldgroep.boekingen.<ref>` + Totaal-rij |
| `tabel-inline` (inline kolommen + rijen) | Standaard markdown-tabel |
| `tabel-vergelijking` (ref) | Markdown-tabel uit `voorbeeldgroep.<ref>` |
| `mock-mutatie-tabel` (ref) | Vergelijkings-tabel uit `voorbeeldgroep.mock_geconsolideerd.<ref>` of `voorbeeldgroep.balansen.<ref>` |

**Verder lezen** (web-only):
```markdown
<div class="no-print">

## Wanneer je dit snapt, ga dan naar

- [[<slug>]] — <hint>
- ...

## Doorklik naar concepten

Voor wie definitorisch detail wil opzoeken:

- [[concept-1]] · [[concept-2]] · ...

</div>
```

**Wettelijk fundament** (verplicht):
```markdown
---

## Wettelijk fundament

- <onderwerp>: <ref>[. <noot indien aanwezig>]
- ...
```

**Footer**:
```markdown
---

*<meta.footer-string>*
```

## Stijl-regels (verplicht naleven)

- Tweede persoon ("je") — geen "ik/wij" en geen onpersoonlijk
- Pedagogisch, rustig, opbouwend register
- **Geen wetsartikel-nummers in lopende tekst** (alleen in `## Wettelijk fundament`)
- Geen drempelbedragen hardcoded — Cijferzakboekje-pointer of tarief-record wikilinks
- Geen confidence-iconen (📖/🔗/🤖)
- **Geen onnodige Engelse termen** — `margin` → `marge`, `goodwill` is OK (vaste term), `one-line consolidation` → "consolidatie op één lijn"
- Wikilinks: `[[<slug>]]` voor leerstukken en concepten; `[[leerpaden/<po-slug>|minicursus PO <po>]]` voor minicursus
- **Abstracte stellingen krijgen een mini-voorbeeld** (regel 10 van schrijfregels) — beat "20 % is vermoeden" zonder tegen-voorbeeld levert vage prose

## Werkstroom

1. Lees alle inputs
2. **Verifieer alle wetsclaims via MCP** vóór je begint te schrijven
3. Schrijf het hele leerstuk in één doorloop via Write naar `<<OUTPUT_PATH>>`
4. Tel woorden + check checklist:
   - [ ] Frontmatter compleet
   - [ ] Intro-callout in `<div class="no-print">` met blank lines errond
   - [ ] Antwoord-in-een-blik binnen 200 woorden van het begin
   - [ ] Minstens 2 visuele elementen
   - [ ] Geen wetsartikel-nummers in lopende tekst
   - [ ] Wettelijk-fundament-sectie aan einde
   - [ ] Footer met status-disclaimer
5. Rapporteer in maximaal 10 bullets:
   - Woord-aantal
   - Aantal RAG-calls + welke
   - Bevestigde claims (≥3 noemen)
   - **Weerlegde claims of conflicten** — script-claim vs werkelijke vondst
   - Tarief-records gemist
   - Welke visualisaties gerenderd
   - Beats samengevoegd vs één-op-één
   - Eventuele onduidelijkheden
   - **Eigen oordeel**: pedagogische gaps die het script niet dekt (voor schema-verfijning)

Begin nu.
```

---

## Hoe in te zetten

1. Vul de drie placeholders in:
   - `<<OUTPUT_PATH>>` — bv. `content/leerpaden/1-4/wie-moet-consolideren.md`
   - `<<SLUG>>` — bv. `wie-moet-consolideren`
   - `<<VOORBEELDGROEP>>` — bv. `aurelia`
   - `<<SPECIFIEKE_CLAIMS_OM_TE_VERIFIËREN>>` — lijstje wetsclaims die het script bevat (script.wettelijk_fundament als startpunt)

2. Start `Agent` met `subagent_type: general-purpose`.

3. Wacht op rapport. Bij weerleggingen → patch script. Bij pedagogische gaps → script-verfijning of beats-vocabularium-uitbreiding.

## Statistieken (mei 2026 — 5 runs)

| Run | Word count | RAG-calls | Weerleggingen | Tijd |
|---|---:|---:|---:|---:|
| wat-is-... (eerste POC, zonder RAG) | 2024 | 0 | n.v.t. | ~2,5 min |
| goodwill-bij-... (eerste met RAG) | 2181 | 6 | 0 | ~3 min |
| wat-is-... (afgeslankt + RAG) | 1350 | 4 | 0 | ~2 min |
| rapportering-en-controle | 2643 | 5+verfijning | 1 (KB-WVV 3:31) | ~4,5 min |
| individuele-jaarrekening | 2959 | 10 | 3 (3:31/2:74/218) | ~5 min |
| wie-moet-consolideren (re-render) | 2193 | 9 | 2 (1:20→1:21, 3:25→3:27) | ~3,5 min |
| hoe-consolideren (re-render) | 4716 | 6 | 0 | ~5 min |
| hoe-consolideren (na Stap 0) | 5274 | 2 | 0 | ~5 min |

Totaal weerleggingen over 8 runs: **6 wetsclaim-fouten gevangen** — bewijs van RAG-discipline-waarde.
