# ADR-040 — Voorbeeldexamenvragen-pagina's binnen leerpadstructuur

**Status**: Accepted (2026-06-01)
**Supersedet (gedeeltelijk)**: ADR-032 — output-locatie van `render_merged_v4.py` verandert.
**Gerelateerd**: ADR-036 (drie-lagen leermateriaal) · ADR-037 (leerstuk-laag) · ADR-039 (samenvatting-laag)

## Context

ADR-032 plaatste de per-PO voorbeeldexamenvragen-pagina's onder `content/voorbeeldexamens/po-<code>.md`. Tegelijk groeide de leerpad-structuur (ADR-036 minicursus + ADR-037 leerstukken + ADR-039 samenvatting + POC-oefening) naar `content/studiemateriaal/<po-slug>/`-folders met meerdere sibling-bestanden. Resultaat:

- Een student die binnen één PO werkt zag de voorbeeldexamen-pagina *naast* het leerpad in de Quartz-explorer, niet *binnen* het leerpad. Dat doorbreekt het mentale model "alles van dit PO op één plek".
- De `content/studiemateriaal/`-folder bevatte een gemixte structuur: oudere PO's als flat `<po-code>.md`, nieuwere als folder. Geen uniforme regel.
- PO's zonder vrijgegeven examenvragen (bv. 1.8) hadden helemaal geen voorbeeldexamen-pagina — een gat in de navigatie i.p.v. een expliciete "nog niets"-signaal.

## Beslissing

### 1. Voorbeeldexamenvragen-pagina verhuist naar het leerpad

Per-PO output van `tools/examen/render_merged_v4.py`:

| Voor (ADR-032) | Na (ADR-040) |
|---|---|
| `content/voorbeeldexamens/po-<code>.md` | `content/studiemateriaal/<po-slug>/voorbeeldexamenvragen.md` |

De cross-PO overzichtspagina (`content/voorbeeldexamens/index.md`) en de "recent toegevoegd"-pagina (`content/voorbeeldexamens/nieuw.md`) blijven onder `content/voorbeeldexamens/`. Hun wikilinks wijzen naar de nieuwe per-PO locaties.

### 2. Alle studiemateriaal krijgen folder-structuur

Elk programmaonderdeel wordt voortaan een folder `content/studiemateriaal/<po-slug>/` met minstens `index.md` (minicursus) en `voorbeeldexamenvragen.md`. Geen `<po-code>.md` flat-bestanden meer in `content/studiemateriaal/`. Dit maakt sibling-toevoegingen (leerstukken, samenvatting, oefening) uniform.

### 3. Stub-pagina voor PO's zonder examenvragen

`render_alle()` schrijft ook een `voorbeeldexamenvragen.md` voor PO's die wél in `data/programma/programma.json` staan maar (nog) geen geclassificeerde vragen hebben — mits de `studiemateriaal/<po-slug>/`-folder bestaat. De stub bevat een `[!info]`-callout "Geen voorbeeldexamenvragen geclassificeerd voor dit programmaonderdeel" en wordt automatisch vervangen door echte content zodra vragen worden toegevoegd in `data/programma/examen_vragen/_interpretaties/`.

### 4. Auto-genummerd `explorer_title`

De render-script scant siblings in `studiemateriaal/<po-slug>/` voor frontmatter `explorer_title: "N. ..."` en kiest `(max + 1). Voorbeeldexamenvragen`. PO's met enkel `index.md` als sibling (geen leerstukken/samenvatting/oefening nog) krijgen kale label `Voorbeeldexamenvragen` zonder nummer. Zodra de leerpad uitgebouwd wordt met genummerde fiches, krijgt de voorbeeldexamenvragen-pagina bij de volgende render automatisch het juiste vervolgnummer.

### 5. Quartz-explorer sortFn

`quartz.layout.ts` sortFn pusht slug-segment `voorbeeldexamenvragen` altijd onderaan binnen de leerpad-folder, ongeacht alfabetische volgorde. Backup voor de zeldzame PO waar het nummer-prefix (nog) ontbreekt.

## Gevolgen

**Pluspunten**:
- Eén explorer-pad per PO: minicursus → leerstukken → samenvatting → oefening → voorbeeldexamenvragen.
- Stub-pagina's geven expliciet "nog leeg"-signaal i.p.v. stille afwezigheid.
- Uniforme studiemateriaal/-structuur (alleen folders, geen flat-files).
- Auto-numbering houdt de zichtbare volgorde stabiel zonder handmatig onderhoud.

**Minpunten**:
- 15 leerpad-bestanden van flat naar folder geconverteerd → wikilinks `studiemateriaal/X.Y` → `studiemateriaal/X-Y` herschreven door de codebase. Eenmalige migratie, niet recurrent.
- Cross-PO overzicht in `content/voorbeeldexamens/index.md` ligt nu op een andere "verdieping" dan de PO-pagina's. Werkbaar via wikilinks; geen functioneel probleem.

## Migratie (uitgevoerd 2026-06-01)

1. Flat `content/studiemateriaal/<po-code>.md` (met dot in bestandsnaam) → `content/studiemateriaal/<po-slug>/index.md` (met dash in foldernaam) voor 15 PO's (1.1, 1.2, 1.5, 1.6, 1.7, 2.1–2.8, 3.0, 4.0).
2. Stale duplicaten `content/studiemateriaal/{1.3,1.8,1.9}.md` verwijderd — folder-versies waren al canoniek.
3. `git mv content/voorbeeldexamens/po-<code>.md content/studiemateriaal/<po-slug>/voorbeeldexamenvragen.md` voor 18 bestaande pagina's.
4. `tools/examen/render_merged_v4.py` + templates (`po_pagina.md.j2`, `index_pagina.md.j2`) aangepast aan nieuwe paden + `explorer_title` + stub-pagina-renderer.
5. `quartz.layout.ts` sortFn-uitbreiding voor `voorbeeldexamenvragen`-positie.
6. Wikilinks `[[studiemateriaal/X.Y...]]` → `[[studiemateriaal/X-Y...]]` en `[[voorbeeldexamens/po-X.Y]]` → `[[studiemateriaal/X-Y/voorbeeldexamenvragen]]` repository-wide herschreven.

## Open punten

- `explorer_title` ontbreekt nog op de 15 net-omgezette `index.md`-files (1-1, 1-2, 1-5, 1-6, 1-7, 2-1..2-8, 3-0, 4-0) — fallback naar lange `title`. Toevoegen wanneer de minicursussen worden uitgewerkt.
- Pre-existerende wikilink-rendering-bug in `two-column-list` div van `content/index.md` en `content/studiemateriaal/index.md` (literal `[[...]]` in HTML) — los van deze ADR.
