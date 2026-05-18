# ADR-009: Examenpatronen

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-18 (render-rubriek in minicursus + AI-varianten + eenrichtingsverkeer)

## Changelog

- **2026-05-18** — Drie verfijningen na ontwerp leermateriaal-laag (ADR-010 §interpretatieve-laag):
  1. **Eenrichtingsverkeer concept ↔ patroon** expliciet gemaakt. `examenfocus`-objecten verwijzen naar concept-IDs; concepten verwijzen **niet terug** — geen edge-type `getoetst-door` in concept-records. Reden: anti-circulariteit (ADR-008 §0). Examenvragen mogen voortbouwen op concepten; concepten mogen niet vormgegeven worden door examenvragen. Render-laag (minicursus) doet de back-reference run-time door alle `examenfocus`-objecten te scannen voor `concept_id in {records van deze PO}`.
  2. **Render-plek in minicursus** vastgelegd als **eind-rubriek per minicursus** (niet per sectie). Reden: studenten moeten "ken ik deze stof voldoende?" kunnen toetsen *zonder* tijdens het lezen al naar de patroon-camouflage geduwd te worden. Rubriek-vorm: `> [!question]-` callouts (collapsed) met examenpatroon-titel, optioneel link naar voorbeeldvraag-tekst. Geen vraag-spoilers in fiche- of sectie-headers.
  3. **AI-gegenereerde varianten** (`gvraag--*.json` in `data/generated_questions/`) krijgen **verplicht `confidence: "inferred"`** (🤖) en worden in render altijd als 🤖 gemarkeerd — niet visueel verwisselbaar met echte ITAA-vragen. Per `gvraag` ook verplicht een `voorbeeld_oplossing`-veld (eveneens 🤖) zodat de student de patroon-instantiatie kan beoordelen zonder zelf op te lossen. Render-laag groepeert eerst echte vragen, dan 🤖-varianten, in twee subkoppen onder de eind-rubriek.

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

### 6. Render-integratie in minicursus (2026-05-18)

Examenpatronen + voorbeeldvragen + AI-varianten verschijnen voor de student **uitsluitend** via de minicursus-render (ADR-010 §interpretatieve-laag), nooit op een concept- of competentie-fiche.

**Plek**: eind-rubriek per minicursus, vaste sectie-titel "Examenfocus" als laatste H2 vóór eventuele "Verder lezen"-sectie. Reden: pre-toetsing zonder camouflage-spoilers.

**Vorm**: `> [!question]-` callouts (collapsed), één callout per `examenfocus`-object of `gvraag`:
- Titel: examenpatroon-naam (uit `vraagvorm` + `complexiteit`-labels) — geen vraag-tekst in de titel
- Body (geopend): vraag-tekst zelf, plus optioneel `> [!success]-` collapsed met `voorbeeld_oplossing` of `redenering`

**Confidence-presentatie**:
- Echte ITAA-vragen (`examenfocus`-objecten met `bron: itaa_examen_<jaar>`): ⚖️
- AI-gegenereerde varianten (`gvraag--*.json`): altijd 🤖, plus subkop "Synthetische oefenvarianten (🤖)" als visuele groepering
- Geen mixing in dezelfde lijst — twee subkoppen onder de eind-rubriek

**Eenrichtings-edge (anti-circulariteit)**: `examenfocus.concept_ids[]` verwijst naar concept-records; concept-records hebben **geen** `getoetst-door`-edge terug. Reden: een concept-record mag niet vorm krijgen door een examenvraag (zie ADR-008 §0). Render-laag doet de back-reference run-time: minicursus voor PO X scant alle `examenfocus`-objecten en selecteert die waarvan `concept_ids` ⊆ records van PO X.

**Onderhoudscyclus** (nieuwe vraag uit voorbeeldexamen-sessie):
1. Vraag-tekst + oplossing in `data/programma/examen_vragen/<jaar>.json`
2. `examenfocus--*.json` aanmaken of bestaand patroon uitbreiden met deze vraag-ID
3. `concept_ids[]` invullen (welke concepten zijn nodig om dit te beantwoorden)
4. Minicursus voor betrokken PO's herrenderen — eind-rubriek pakt de update vanzelf op

**AI-variant-genereren** (optioneel, op verzoek):
1. Patroon-template × concept-record → `gvraag--*.json` via `tools/examen/generate.py`
2. Verplichte velden: `vraag_tekst`, `voorbeeld_oplossing`, `redenering`, `confidence: "inferred"`, `gebaseerd_op_patroon: <patroon_id>`, `gebaseerd_op_concepten: [<concept_ids>]`
3. Render groepeert onder de "Synthetische oefenvarianten (🤖)"-subkop

### 7. Wat NIET in examenpatronen-objecten hoort

- **Concept-definities of bouwstenen**: die zitten in concept-records. Examenpatronen verwijzen alleen.
- **Pedagogische framing**: "let goed op dit type vraag, het komt vaak terug" hoort in minicursus-glue, niet in patroon-object.
- **Studieadvies**: hoe te oefenen, hoe te onthouden — leermateriaal-laag (ADR-010), niet observatielaag.

## Gevolgen

- `data/programma/exam_patterns/` — `vraagvorm--*.json` + `complexiteit--*.json`
- `data/exam_focus/` — `examenfocus--*.json` (brug-objecten)
- `data/generated_questions/` — `gvraag--*.json`
- `tools/examen/` — extract, label, generate, review
- Patronen krijgen provenance net als andere artefacten (ADR-004); examenfocus verwijst expliciet naar concept-IDs zodat een concept-update tot stale-flag op de focus leidt
- Anti-oogkleppen-regel uit ADR-008 blijft gelden: een patroon-vraag definieert nooit een nieuw concept, hooguit een nieuwe focus op een bestaand concept
