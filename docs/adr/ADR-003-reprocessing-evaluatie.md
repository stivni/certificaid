# ADR-003: Reprocessing & evaluatie

**Status**: Draft
**Datum**: 2026-05-07

## Context

Bronnen veranderen (errata, nieuwe wetgeving), het conceptmodel evolueert, tools verbeteren. Een niet-iteratief systeem zou bevriezen op de eerste versie en stilzwijgend verouderen. Tegelijk moet leermateriaal ergens stabiel zijn — anders verandert leerstof onder de student z'n voeten.

"100% af" is een foute frame: dat punt komt nooit. "Goed genoeg om door te schuiven + regressietest" is werkbaar.

Bovendien: gericht reprocessen ("bron X is foutief, regenereer alle downstream") is enkel mogelijk als we weten welk artefact uit welke input komt. Daarvoor: provenance (ADR-004).

## Beslissing

### 1. Per-laag DoD = "good enough to advance" + regressietest

| Laag | Gate |
|---|---|
| ETL | Golden set (5–10 reprocesste bronnen handmatig OK) groen + agent-QA-rapport "pass" |
| Bronnen-RAG | Top-k recall op vragen-testset boven afgesproken drempel |
| Concepten | Dekkingscheck TDK groen + voorbeeldexamen-vragen oplosbaar uit conceptenset |
| Examenpatronen | Voorbeeldexamens gelabeld; gat-rapport met concepten leeg |
| Leermateriaal | Student kan voorbeeldexamen-vragen oplossen na bestudering snapshot |

Geen "100%". Drempels zijn expliciet, herzienbaar, en groeien naarmate ground truth groeit.

### 2. Stale-cascade, geen auto-regen

Input verandert → downstream artefacten gemarkeerd `stale: true` (via provenance, ADR-004) met reden. **Mens beslist** of/wanneer reprocessing draait. Voorkomt cascade-storms en LLM-kostensplosies bij kleine inputwijzigingen.

### 3. Agent-gebaseerde QA-check

Per laag draait een LLM-agent als deel van de gate:
- ETL-QA: leest output-MD, flagt structurele problemen (kapotte tabellen, header-leak, paginavoetregels in body)
- Concept-QA: leest een set concepten, flagt schema-inconsistenties of dangling-edges
- Snapshot-QA: leest fiches, flagt onverklaarde claims of ⚖️/🤖-mislabeling

Agent-QA is *aanvulling* op golden-set en menselijke review, geen vervanging.

### 4. Snapshot = release voor leermateriaal

Concepten mogen continu churnen; fiches lopen achter via expliciete release-snapshots (ADR-010). Leermateriaal-snapshot heeft versie-tag + changelog. Tussentijdse concept-wijzigingen verschijnen *niet* in de gepubliceerde leerstof tot een volgende snapshot.

## Gevolgen

- Per laag een regressie-suite in de repo (`tools/<laag>/eval.py`)
- Eval-corpus (golden bronnen, vragen-testset, voorbeeldexamens) wordt eerste-klasse asset in `resources/eval/`
- Reprocessing is een expliciete operatie — `tools/reprocess.py <artefact>` of vergelijkbaar — niet een onzichtbaar achtergrondproces
- "Klaar"-uitspraken refereren altijd aan een specifieke gate, niet aan een gevoel
