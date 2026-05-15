# ADR-009: Examenpatronen

**Status**: Draft
**Datum**: 2026-05-07

## Context

Concepten zijn de tijdloze kennislaag. Examenvragen toetsen die concepten via terugkerende patronen — vraagvormen, complexiteits-dimensies, camouflage-types. Patronen leven in een **aparte observatielaag**; vermengen met concepten zou de tijdloze laag contamineren met examen-toevalligheden ("ITAA vroeg in 2018 specifiek naar X dus we maken concept X").

Tegelijk zijn patronen niet bijzaak: ze sturen mee waar concept-extractie diep moet graven, ze zijn validator van conceptueel-volledig-zijn, en ze zijn de templates voor synthetische oefenvragen. Drie functies, één observatielaag.

## Beslissing

### 1. Drie objecttypes

- **`vraagvorm`** — hoe de vraag gesteld wordt (format, cognitieve laag, format-valkuil). Concept-agnostisch.
- **`complexiteitspatroon`** — vier dimensies: kennisdiepte / contextspecificiteit / analytische breedte / camouflage.
- **`examenfocus`** — brug tussen concept en patroon: hoe ITAA dit specifieke concept toetst (links naar vraagvorm + complexiteit + echte voorbeelden).

### 2. Camouflage-taxonomy (4 types)

`geen` · `red-herring` · `schijngelijkenis` · `verborgen-vereiste`

`verborgen-vereiste` = "stel vraag X, verwacht dat student ook Y signaleert" (timing, fout, compliance, ...). Timing-trigger is geen apart type — instantie van `verborgen-vereiste`.

### 3. Drie functies in de pipeline

- **Lens** bij concept-extractie (ADR-008): de patronen die op een concept zitten tonen welke diepte het examen verwacht. Stuurt de extractie-prompt en stress-tests.
- **Validator** van de conceptenset: dekken de huidige concepten de gevonden patronen? Gat-rapport (concept ontbreekt of is te oppervlakkig) → trigger voor extractie-uitbreiding.
- **Generator** van oefenvragen: patroon-templates × concept-record = synthetische oefenvragen, opgeslagen in `data/generated_questions/`.

### 4. Voorbeeldexamens als ground truth

Examenvragen worden eerst opgelost met de huidige conceptenset → de oplossing toont welke concepten + welke diepte nodig waren. Patronen worden afgeleid uit die oplossingen, niet uit de ruwe vraagtekst alleen.

Volgorde:
```
concepten (eerste versie) → vragen oplossen → patronen afleiden → patronen als template
```

Solving first reveals what depth was actually needed — richer dan guessing from raw PDF.

### 5. Versioning

`JJJJMMDD.N` (bv. `20260507.1`). Bij patroonupdate → stale-flag op alle generated questions met die patroon_id en lagere versie (zie ADR-003 voor stale-mechaniek).

## Gevolgen

- `data/programma/exam_patterns/` — `vraagvorm--*.json` + `complexiteit--*.json`
- `data/exam_focus/` — `examenfocus--*.json` (brug-objecten)
- `data/generated_questions/` — `gvraag--*.json`
- `tools/examen/` — extract, label, generate, review
- Patronen krijgen provenance net als andere artefacten (ADR-004); examenfocus verwijst expliciet naar concept-IDs zodat een concept-update tot stale-flag op de focus leidt
- Anti-oogkleppen-regel uit ADR-008 blijft gelden: een patroon-vraag definieert nooit een nieuw concept, hooguit een nieuwe focus op een bestaand concept
