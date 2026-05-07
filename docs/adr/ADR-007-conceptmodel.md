# ADR-007: Conceptmodel

**Status**: Draft
**Datum**: 2026-05-07
**Vervangt**: archive/ADR-006 (drie-lagenmodel — concept-laag absorbeert), archive/ADR-009 (concept-record-schema v2)

## Context

Een concept = een **tijdloos studieonderwerp** (een fenomeen), niet een wetsartikel en niet een vakindeling. Een eerdere poging met een plat schema (`main_rule` / `exceptions` / `obligations` / `pitfalls`) kraakte op de diversiteit van de ITAA-domeinkennis: een definitie is geen procedure, een drempel is geen casus, een beginsel vergt oordeel terwijl een regel een verplichting is. Het examen toetst vooral **relaties** tussen die soorten kennis.

Een uniform schema kan dat niet vasthouden. Een **getypeerde knowledge graph** wel: nodes per kennis-type met type-specifieke velden, verbonden door getypeerde edges met conditie- en scope-velden.

## Beslissing

### Architectuur

- **Nodes** = JSON-files in `data/concept_records/<id>.json` (één file per node)
- **Edges** = uitgaande velden binnen de bron-node
- **Walking** via NetworkX (in-memory laden, walks in milliseconden, ~500–1500 nodes verwacht)
- **Vector-zoek** via ChromaDB-collection `concepten` (ADR-006); edges meegedragen als metadata
- **Schema-evolutie** = veld toevoegen, geen migrations. Sparse fields zijn de norm.
- **Open node- en edge-typering** — de initiële lijsten (zie onder) zijn geen limiet. Tijdens extractie mag een nieuw type voorgesteld worden via `node_type: "voorgesteld:<naam>"` of een edge-type `voorgesteld:<naam>`. Voorgestelde types worden verzameld in `data/concept_records/_voorgestelde_types.yaml` voor menselijke review; pas na akkoord wordt het schema gebumpt en records hernoemd.

### Designprincipes

1. **Concept = fenomeen**, niet artikel of vakindeling. Vakoverschrijdend is de regel.
2. **Sparse fields** zijn norm; partiële records zijn geldig.
3. **Schema-evolutie** = veld toevoegen. Schema-versie per record (`schema_version`); wijzigen schema → records `stale` (ADR-004).
4. **Accountant-taal in hoofdtekst** — actief, direct, met concrete situaties. Juridisch jargon enkel in `source.citation`.
5. **Voorbeelden in eigen veld** (`voorbeeld_inline`), niet in `definitie`/`tekst`. Casus-nodes blijven enkel voor échte gevallen (jurisprudentie, voorbeeldexamenvraag, CBN-advies-feitenset).
6. **Compositie boven duplicatie — opt-in**. Default sub-stap = inline. Aparte node alleen als twee procedures écht dezelfde sub raken.
7. **Verwijzingen als gestructureerde child-property**, niet inline in prose. Cross-references staan als getypeerde edge-velden direct op het blok. Detectie en lifting tijdens concept-extractie (ADR-008), niet tijdens chunking.
8. **Edges op block-level** mogelijk (binnen een specifieke regel-tekst, een uitzondering, één procedure-stap). NetworkX-laden tilt block-edges automatisch op naar node-niveau voor walks; block-anker blijft bewaard voor display.

### Node-types (initieel 11, mag groeien)

`begrip` · `regel` · `beginsel` · `procedure` · `methode` · `drempel` · `skill` · `casus` · `afwegingskader` · `actor` · `fenomeen`

Per type eigen sleutel-velden (zie archive/ADR-009 voor volledige uitwerking, of `tools/extractie/schemas/` voor de levende definitie).

### Edge-types (initieel ~20, mag groeien)

`definieert` · `regelt` · `uitzondering-op` · `primeert-boven` · `getriggerd-door` · `vereist-kennis-van` · `toegepast-via` · `voorbeeld-van` · `bevat` / `onderdeel-van` · `vervangt` / `vervangen-door` · `bedreigt` / `bedreigd-door` · `ratio` · `alternatief-voor` · `schakelt-over-naar` · `gemeten-met` / `instrument-van` · `vernietigt-deel-van` · `contrasteert-met` · `van-toepassing-op`

Optionele velden op edges: `scope`, `conditie`, `scharnier`, `redenering`, `aspect`, `_dangling`, `notities[]`.

### Bronverwijzing — gestructureerd

```json
"source": {
  "type": "wet" | "kb" | "itaa-norm" | "cbn-advies" | "isa" | "jurisprudentie" | "voorbeeldexamen",
  "short": "AWW art. 47 §1",
  "ref": { ... },        // type-specifieke deelvelden
  "citation": "exact quote (optioneel)"
}
```

### Status-flow per node — welke velden in welke fase

| Status | Aangevulde velden (cumulatief) | Trigger naar volgende fase |
|---|---|---|
| `seed` | `id`, `naam`, `node_type`, `source`, `main_rule` of `definitie` (verbatim/paraphrase met confidence) | LLM-extractor heeft genoeg bron-context om uitzonderingen + scope te formuleren |
| `partieel` | + `exceptions`, `scope`, eerste batch `edges` (mogelijk dangling) | Edges grotendeels geresolveerd; bron-RAG levert geen nieuwe info op verdiepende queries |
| `gevuld` | + `pitfalls`, `voorbeeld_inline`, gerelateerde casussen | Menselijke review |
| `geverifieerd` | identiek; alleen status-flag | — |

Voorbeelden, valkuilen en cases worden **pas in `gevuld`** toegevoegd, niet in `seed` (zie ADR-008 voor extractie-volgorde).

`seed` ontstaat ofwel uit programma-/bron-gestuurde extractie, ofwel als dangling-target van een edge in een ander concept; `geverifieerd` vereist menselijke bevestiging.

### Confidence-labels — string-tags, geen emoji in data

Elke claim met confidence-veld:
```json
"confidence": "grounded"   // ⚖️ — direct traceerbaar naar bron in source.ref
"confidence": "inferred"   // 🤖 — LLM-gegenereerde redenering of synthese
```

Emoji (⚖️/🤖) zijn UI-/render-conventie (tutor, fiches, conversaties) — niet in JSON-data.

### Concept-laag is dependency-vrij naar boven

Concept-records bevatten **geen** verwijzingen naar programmaonderdelen, kenniselementen, taken, doelstellingen of examenvragen. Dependencies stromen één kant op (programma → concepten, examen → concepten). De koppeling kenniselement → concept leeft uitsluitend in de programmaonderdeel-JSON (zie ADR-002):

```json
// data/programmaonderdelen/4.0-deontologie.json — ENIGE WAARHEID
"kenniselementen": [
  {"deel": 1, "code": "4.0.I.D.7", "tekst": "Beroepsgeheim",
   "concepten": ["beroepsgeheim-gecertificeerd-accountant", "doorbreking-beroepsgeheim"]}
]
```

Concepten zijn zo portable — bij hervorming van het examenprogramma (codes herschikt) raakt de conceptenset niet.

**Bron-input via chunks** (provenance) is geen schending van deze regel: als een passage uit een voorbeeldexamen-toelichting of Mvt geciteerd wordt voor een concept-veld, gaat dat als chunk-id in `_provenance.inputs[]` — niet als examenvraag-link in een inhoudelijk veld. Het concept weet alleen "deze chunk is mijn bron"; chunk-metadata bepaalt of het een wettekst, norm of voorbeeldexamen-passage was.

Dekkingschecks die "welke kenniselementen dekt concept X af?" willen beantwoorden, bouwen op aanvraag een in-memory reverse-index uit programmaonderdeel-JSON's (`tools/lib/coverage.py`). Geen state op concepten zelf.

### Schrijfregels concept-content

Aparte content-conventie in [`docs/concept-schrijfregels.md`](../concept-schrijfregels.md). Wordt geladen bij prompt-opbouw voor de extractor en bij menselijke review. Niet in deze ADR — schrijfregels zijn geen architectuurbeslissing.

## Gevolgen

- `data/concept_records/` = volledige conceptenset
- `tools/lib/graph.py` (nieuw) — NetworkX-laden, walks, dangling-detectie
- Schema-evoluties expliciet in `schema_version`-veld + ADR-changelog
- `tools/lib/cross_refs.py` — utility om referenties (`art. 33-35`, `§ 1`) te detecteren tijdens extractie (ADR-008)
- Bestaande concept-records (oud schema) krijgen `_provenance.stale: true` en worden in fasen gemigreerd
