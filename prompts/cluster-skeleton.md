# Cluster-skeleton — schrijf schema-2.2 skeletons voor een hele cluster

**Fase 1** van de extractie-pipeline. Output: N schema-2.2-valide JSON-records met `status: "skeleton"` in `data/concepten/records/`. Geen content — alleen structuur + scope + hints.

Voor **Fase 2** (content-extractie), zie `prompts/cluster-extract.md`.

## Wat is je input

1. **Skelet-doc** `docs/granulariteit-skelet.md` — leidende bron-van-waarheid voor cluster-structuur:
   - Cluster-sectie met tree-snapshot
   - Renames + acties-tabel
   - Cross-cluster overzicht
   - Sub-secties als sub-concept/bouwsteen-hints
2. **Anchors** `data/programma/anchors.json` voor PO-anchor-validatie
3. **Schema** `data/concepten/schema-2.2.schema.json` — leidend voor validatie
4. **Rationale-log** in skelet-doc voor beslissings-context per cluster
5. **Optioneel**: oude records-v21 voor anker-mapping (niet voor content)

## Wat is je output

Per record uit de cluster: één `data/concepten/records/<id>.json` met:

### Verplicht (Tier 1)
- `id` + `naam` (primair · synoniemen · afkorting indien praktijk-courant)
- `concept_type` (uit 9-enum: instrument · verrichting · procedure · balanspost · ratio · regime · kader · principe · actor)
- `metadata.schema_version: "2.2"`
- `metadata.status: "skeleton"`
- `metadata.categorieen[]` (K/E/G/R: kader · entiteit · gebeurtenis · regeling) — kan hybride
- `metadata.ankers[]` (PO-anchor-IDs uit anchors.json — verifieer bestaan)
- `metadata.scope.in[]` — wat behandelt dit record (extractie-guidance voor Fase 2)
- `metadata.scope.out[]` — wat NIET, met richting + ref (zie hieronder)
- `metadata.provenance.model: "cluster-skeleton-agent"`
- `metadata.provenance.wave_id: "skeleton-<cluster>-<datum>"`
- `metadata.changelog[]`: één entry `{operatie: "skeleton", timestamp: ..., wijziging: "..."}`
- `inhoud.kern.definitie.tekst`: placeholder `"⏳ Te beschrijven in Fase 2"` + grondslag (verondersteld + ai_model-bron)
- `relaties[]` cross-cluster + binnen-cluster top-level relaties

### Aanbevolen (hints voor Fase 2)
- `inhoud.subconcepten[]`: sub-concept-skeletons (= mini-concepten met eigen kern, recursief identiek)
- `inhoud.bouwstenen[]`: platte content-items met type uit 11-enum (begrip · stap · drempel · regel · uitzondering · vuistregel · mechanisme · risico · formule · principe · beperking)
- `inhoud.gebruikscontext.geldigheid`: voor regimes/regelingen (status: in-voege / uitdovend / afgeschaft / historisch / ontwerp)

## Scope.out structuur

Voor elke out-of-scope topic, expliciete richting:

```json
{
  "topic": "Beschrijving wat niet erbij hoort",
  "richting": "moet-verwijzen" | "mag-verwijzen" | "niet-verwijzen",
  "ref": "ander-record-id"
}
```

- `moet-verwijzen`: verplichte cross-link voor leespad-coherentie (parent-Σ → alternatieven, uitwerking elders)
- `mag-verwijzen`: optionele context-cross-link voor verdieping
- `niet-verwijzen`: semantische scheiding (verschillende werkvelden)

## Subconcepten vs bouwstenen — welk waarvoor?

- **Sub-concept** = mini-concept met eigen kern + sub-sub-decompositie potentieel. Recursief identiek aan parent-concept-shape. Voorbeelden: `balansschema` binnen `jaarrekening`; `consolidatiekring` binnen `consolidatie`.
- **Bouwsteen** = platte content-item, één van 11 inhoud-types. Voorbeelden: `boekingsregel-debet-credit` (bouwsteen_type: regel) · `nbb-neerlegging-30-dagen` (bouwsteen_type: stap) · `current-ratio-formule` (bouwsteen_type: formule).

**Litmus**: kan dit zelf weer subconcepten/bouwstenen dragen? → subconcept. Anders → bouwsteen.

**Anti-versplintering**: een sub-concept dat eigen accountant_perspectieven of scope nodig zou hebben = split-trigger naar **apart top-level record**, niet binnen het record.

## Werkwijze

1. **Lees skelet-doc cluster-sectie** integraal — tree-snapshot + renames-tabel + cross-cluster + open punten.
2. **Identificeer alle cluster-eigen records** (uit tree-snapshot, niet de cross-vermeldingen).
3. **Per record**:
   - id + naam (verifieer tegen oude records-v21 voor synoniemen)
   - ankers verifiëren tegen anchors.json (skip onbestaande)
   - concept_type uit 9-enum (zie schema $comment voor richtlijn)
   - categorieen uit K/E/G/R-mapping (consulteer skelet-doc + rationale-log)
   - **scope.in[]** uit sub-secties + cluster-positionering in skelet-doc
   - **scope.out[]** uit cross-cluster-tabel + buurconcepten-context (richting kiezen!)
   - **subconcepten[]** uit `#sub-sectie`-aanduidingen in skelet-doc tree-snapshot (substantiële sub-concepten)
   - **bouwstenen[]** uit kleinere anker-aanduidingen + werkveld-kennis (regels, stappen, formules, drempels)
   - **relaties[]** uit cross-cluster + binnen-cluster verwijzingen
   - **geldigheid** voor regimes (default: in-voege; markeer uitdovend/afgeschaft expliciet)
4. **Valideer** elk record tegen schema-2.2 (jsonschema.validate)
5. **Eindrapport**: aantal records + open beslis-punten voor mens-review

## Validatie

```python
import json, jsonschema
schema = json.load(open('data/concepten/schema-2.2.schema.json'))
for fp in glob.glob('data/concepten/records/*.json'):
    record = json.load(open(fp))
    jsonschema.validate(record, schema)
```

Schema is leidend — fix vóór je commit.

## Eindrapport

Aan het einde:
- Aantal records geschreven (`status: skeleton`)
- Renames toegepast (uit skelet-doc-acties)
- Sub-concepten + bouwstenen-hints per record (aantal)
- Cross-relaties aangemaakt
- Open beslis-punten voor mens-review (twijfels per record)
- Ankers die NIET in anchors.json gevonden (gaten in PO-coverage)

## Anti-pattern's vermijden

- ❌ Content schrijven in Fase 1 (kern.definitie blijft placeholder)
- ❌ Sub-concept met eigen scope/perspectieven (split-trigger → apart record)
- ❌ Bouwsteen met sub-secties die zelf concept-shape hebben (gebruik subconcept ipv bouwsteen)
- ❌ Ankers verzinnen die niet in anchors.json bestaan
- ❌ Concept_type=`methode` (gedropt in 2.2 — gebruik `procedure` of `kader`)
- ❌ Bouwsteen_type=`subconcept` (gedropt — gebruik `inhoud.subconcepten[]`)

## Workflow met mens

- Fase 1 (deze prompt): batch-skeleton voor hele cluster
- Mens reviewt twijfels uit eindrapport
- Mens patcht skeletons waar nodig
- Fase 2 (cluster-extract.md): content-vulling per record
