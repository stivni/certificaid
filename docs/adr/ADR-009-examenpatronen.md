# ADR-009: Examenpatronen

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-18 (render-rubriek in minicursus + AI-varianten + eenrichtingsverkeer + schema-detail examenfocus/gvraag)

## Changelog

- **2026-05-18 (later)** — Schema-detail voor `examenfocus--*.json` en `gvraag--*.json` vastgepind in §7. Beide objecttypes hadden tot dan toe een impliciet schema; nu expliciet met validatie-regels (`tools/examen/validate_examenfocus.py`, `tools/examen/validate_gvraag.py`). Confidence-afleiding ⚖️/🤖 op render-tijd vanuit voorbeeldvragen-tier (geen `bron`-veld op examenfocus zelf — multi-tier-aggregatie). Stale-detectie op concept-/patroon-update via `rebuild_triggers[]` op gvraag, run-time scan op examenfocus. §7 oorspronkelijk "Wat NIET in" → hernummerd naar §8.
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

**Vorm**: `> [!question]-` callouts (collapsed), **één callout per voorbeeldvraag** (niet per examenfocus-object). Bij multi-voorbeeldvragen onder dezelfde examenfocus krijgt elke voorbeeldvraag een eigen callout met dezelfde patroon-aanduiding maar verschillende examen-bron:
- **Titel**: `<examenpatroon-naam> · <examen-ID> vraag <vraag-nr>` — geen vraag-tekst in de titel (anti-spoiler)
- **Body (geopend)**: de exacte vraag-tekst uit `data/programma/examen_vragen/<examen_id>.json`
- **Optioneel binnen body**: `> [!success]-` collapsed met `antwoord_motivering` (uit examen-vragen-JSON, indien `antwoord_bron` gevuld) of `redenering` (voor `gvraag`)

Voor `gvraag--*.json` is er per object steeds één voorbeeldvraag (de gegenereerde vraag zelf) → één callout per gvraag.

**Render-sortering** binnen de "Voorbeeldvragen"-subkop: tier A → B → C uit `voorbeeldvragen[].tier` (zie §7 schema), zodat moderne, meer representatieve vragen bovenaan staan.

**Confidence-presentatie**:
- Echte ITAA/BIBF-vragen (callout afgeleid uit `examenfocus.voorbeeldvragen[].tier ∈ {A, B, C}`): ⚖️
- AI-gegenereerde varianten (`gvraag--*.json`, `confidence: "inferred"`): altijd 🤖, plus subkop "Synthetische oefenvarianten (🤖)" als visuele groepering
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

### 7. Schema-detail voor `examenfocus`- en `gvraag`-objecten (2026-05-18)

§6 noemt beide objecttypes maar laat het schema impliciet. Deze sectie pinnt het schema vast. Beide leven niet in `data/programma/exam_patterns/` (waar de patroon-types `vraagvorm` en `complexiteit` wonen) — `examenfocus` woont in `data/exam_focus/`, `gvraag` in `data/generated_questions/`, juist omdat zij **instantiaties** zijn (concept × patroon × bron) en niet de patroon-types zelf.

#### `examenfocus--<slug>.json` (schema 1.0)

Brug-object tussen concept-records en patroon-records, met minstens één voorbeeldvraag als bewijslast.

```yaml
id: "examenfocus--<concept-slug>--<patroon-slug>"   # vrije slug toegestaan; conventie is concept+patroon voor leesbaarheid
schema_version: "1.0"
naam: "Alarmbelprocedure — feiten-met-schijngelijkenis"  # leesbaar, 1 regel

# Brug-aspecten — wat verbindt deze focus
concept_ids: ["alarmbelprocedure", "nettoactief-test"]
vraagvorm_id: "vraagvorm-jf-reeks-stellingen"
complexiteitspatroon_id: "complex-feiten-schijngelijkenis"

# Pedagogische framing van DEZE specifieke focus
wat_getoetst_wordt: |
  Kan de student de timing en triggerwaarde van de alarmbelprocedure
  correct toepassen op een gegeven nettoactief-situatie? Specifiek het
  onderscheid tussen 'nettoactief minder dan helft van kapitaal' en
  'nettoactief minder dan een vierde van kapitaal' — twee triggers, twee
  procedures, twee timings.
typische_formulering:
  - "De vennootschap heeft een nettoactief van X. Op welk moment moet de algemene vergadering bijeengeroepen worden?"
  - "Stelling: 'Bij nettoactief < ¼ kapitaal moet de AV binnen 3 maanden bijeen' — juist of fout?"
valkuil_specifiek: |
  Veel studenten kennen de ½-trigger maar verwarren de ¼-trigger met
  ontbinding-van-rechtswege of vermengen de termijnen.

# Bewijslast — minstens 1 echte voorbeeldvraag uit corpus
voorbeeldvragen:
  - examen_id: "2013-1"
    vraag_id: "2013-1-vr3"
    vraag_nr: "3"
    tier: "B"             # A/B/C uit examen-JSON top-level representativiteit_tier
  - examen_id: "2015-1"
    vraag_id: "2015-1-vr20"
    vraag_nr: "20"
    tier: "B"

_provenance:
  tool: "examenfocus-curation-v1"
  curator: "agent"        # "agent" als deterministisch afgeleid; "mens" als handmatig gecureerd
  created_at: "2026-05-18T12:00:00Z"
  updated_at: "2026-05-18T12:00:00Z"
  confidence: "grounded"  # grounded = directe afleiding uit corpus (minstens 1 voorbeeldvraag); inferred = synthetische groepering zonder corpus-echo
```

**Validatie-regels** (te implementeren in `tools/examen/validate_examenfocus.py`, parallel met `validate_competentie.py`):

| Regel | Falen → |
|---|---|
| `concept_ids[]` niet leeg | error |
| Elk `concept_id` bestaat in `data/concepten/records/` (records-API check) | error |
| `vraagvorm_id` bestaat in `vraagvormen.json` | error |
| `complexiteitspatroon_id` bestaat in `complexiteitspatronen.json` | error |
| `voorbeeldvragen[]` heeft minstens 1 entry | error |
| Elk `voorbeeldvragen[*].vraag_id` bestaat in `data/programma/examen_vragen/<examen_id>.json` | error |
| Geen voorbeeldvraag heeft `programmaonderdelen: []` in `_programmaonderdeel_classificatie.json` (filter-conventie INDEX.md) | error |
| `wat_getoetst_wordt` minstens 1 zin (≥40 chars) | warning |
| `typische_formulering[]` minstens 1 entry | warning |

**Eenrichtingsverkeer (anti-circulariteit, ADR-009 §6)**: concept-records linken niet terug. Render-laag doet back-reference run-time door `examenfocus`-objecten te scannen op `concept_ids ⊆ records(PO X)`.

**Stale-detectie** (concept- of bron-update → focus stale-flag):
- Bij elke concept-record-update (records-API write): scan `examenfocus--*.json` waar het concept-id in `concept_ids[]` zit → markeer met `_provenance.stale_concept: <concept_id>`.
- Bij elke vraag-record-update (zeldzaam — alleen bij correctie): idem voor `voorbeeldvragen[].vraag_id`.
- Curator handelt stale-flag af: bevestig (touch `updated_at`) of revisor schrijft focus opnieuw.

#### `gvraag--<slug>.json` (schema 1.0)

AI-gegenereerde oefenvraag, instantiatie van een patroon-template × concept-record(s). Niet visueel verwisselbaar met echte ITAA-vragen.

```yaml
id: "gvraag--<slug>"
schema_version: "1.0"
vraag_tekst: |
  De BVBA Alfa heeft op 31/12/2025 een kapitaal van 100.000 EUR en een nettoactief van 25.000 EUR.
  De raad van bestuur heeft de jaarrekening op 15/03/2026 vastgesteld.
  Binnen welke termijn moet de algemene vergadering bijeengeroepen worden?

# Verplicht: AI-grond
confidence: "inferred"   # ALTIJD inferred — geen echte examenvraag

# Brug-aspecten — wat instantiseert deze gegenereerde vraag
gebaseerd_op_patroon: "complex-feiten-schijngelijkenis"   # mag vraagvorm-id OF complexiteitspatroon-id zijn (één van beide of beide)
gebaseerd_op_concepten: ["alarmbelprocedure", "nettoactief-test"]
gerelateerd_aan_examenfocus: "examenfocus--alarmbelprocedure--complex-feiten-schijngelijkenis"  # optioneel; welke focus illustreert

# Verplicht: AI-oplossing
voorbeeld_oplossing: |
  Twee maanden na vaststelling van het nettoactief, dus uiterlijk 15/05/2026.
  Nettoactief 25.000 EUR < ¼ kapitaal (25.000 EUR), dus art. 2:52 WVV
  trigger 2 maanden voor bijeenroeping van de AV met agenda 'ontbinding'.
redenering: |
  Stap 1: bepaal het nettoactief en vergelijk met de kapitaaldrempels. 25.000 EUR
  is gelijk aan ¼ van 100.000 EUR — exact op de grens. De wet zegt 'minder dan ¼',
  dus de ¼-trigger is hier strikt NIET geactiveerd; alleen de ½-trigger geldt (3 maanden).
  Stap 2: pas de termijn toe. Vaststelling 15/03/2026 + 3 maanden = 15/06/2026.

_provenance:
  tool: "tools/examen/generate.py"
  agent_run: "<run-id>"
  created_at: "2026-05-18T13:00:00Z"
  rebuild_triggers:           # invalidatie-set: één van deze wijzigt → gvraag stale
    - "concept:alarmbelprocedure"
    - "concept:nettoactief-test"
    - "patroon:complex-feiten-schijngelijkenis"
```

**Validatie-regels** (`tools/examen/validate_gvraag.py`):

| Regel | Falen → |
|---|---|
| `confidence == "inferred"` (verplicht, geen escape naar grounded) | error |
| `vraag_tekst`, `voorbeeld_oplossing`, `redenering` alle drie aanwezig en ≥40 chars | error |
| `gebaseerd_op_concepten[]` niet leeg en bestaande records | error |
| `gebaseerd_op_patroon` bestaat in patroon-libraries (vraagvorm OF complexiteit) | error |
| `rebuild_triggers[]` bevat alle concept- en patroon-IDs uit boven (consistentie) | error |
| `gerelateerd_aan_examenfocus` (indien gevuld) bestaat | warning |

**Stale-detectie**: bij elke concept- of patroon-update, scan `gvraag`-objecten waar de ID in `rebuild_triggers[]` zit → markeer stale → bij volgende run van `tools/examen/generate.py --rebuild-stale` worden ze opnieuw gegenereerd.

#### Render-confidence-afleiding (consumer-zijde)

Minicursus-render bepaalt ⚖️/🤖 niet uit een `bron`-veld op `examenfocus` zelf, maar afgeleid:

- Een `examenfocus`-object met minstens 1 `voorbeeldvragen[]` uit tier A/B/C examen-JSON → render ⚖️ in de minicursus-eindrubriek (echte vraag).
- Een `gvraag--*.json`-object → altijd 🤖 in de minicursus-eindrubriek (synthetische variant), gegroepeerd onder eigen subkop.
- Géén mixing van examenfocus en gvraag in dezelfde lijst — twee subkoppen onder "Examenfocus" (ADR-009 §6).

Reden voor afleiding (i.p.v. `bron`-veld op examenfocus): een examenfocus aggregeert vragen uit meerdere examens (multi-tier). Een single `bron`-veld zou geen recht doen aan die aggregatie. Tier-info zit op voorbeeldvraag-niveau, render-laag aggregeert.

### 8. Wat NIET in examenpatronen-objecten hoort

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
