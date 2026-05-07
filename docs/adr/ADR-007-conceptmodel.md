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
- **Vector-zoek** via ChromaDB-collection `concepts` (ADR-006); edges meegedragen als metadata
- **Schema-evolutie** = veld toevoegen, geen migrations. Sparse fields zijn de norm.

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

### Status-flow per node

`seed` → `partieel` → `gevuld` → `geverifieerd`

`seed` ontstaat als dangling-target van een edge; `geverifieerd` vereist menselijke bevestiging.

### TDK-koppeling (ADR-002)

Verplicht veld `afdekt_tdk: [...]` per node. Dekkingscheck draait per snapshot.

## Gevolgen

- `data/concept_records/` = volledige conceptenset
- `tools/lib/graph.py` (nieuw) — NetworkX-laden, walks, dangling-detectie
- Schema-evoluties expliciet in `schema_version`-veld + ADR-changelog
- `tools/lib/cross_refs.py` — utility om referenties (`art. 33-35`, `§ 1`) te detecteren tijdens extractie (ADR-008)
- Bestaande concept-records (oud schema) krijgen `_provenance.stale: true` en worden in fasen gemigreerd
