# ADR-004: Provenance & versionering

**Status**: Draft
**Datum**: 2026-05-07

## Context

Reprocessing (ADR-003) is alleen werkbaar als elk artefact weet:
- uit welke inputs het is afgeleid
- met welke tooling- / model- / prompt-versie

Anders is "fout in bron X → wat moet ik regenereren?" handcrafting (grep + reasoning + hopen). En zonder versie-info is reprodusebaarheid onmogelijk: een concept dat met prompt-v2 is geëxtraheerd ziet er anders uit dan met prompt-v3, en je weet niet welk je voor je hebt.

Provenance is plumbing — onzichtbaar bij gebruik, fundamenteel voor de iteratief-werkwijze. Hoort daarom als eigen ADR (vindbaar, vervangbaar) en niet inline in elke laag-ADR (verstopt, dupliceert).

## Beslissing

Elk artefact (bron-MD, RAG-chunk, concept-record, snapshot-fiche) draagt een **provenance-blok**:

```yaml
provenance:
  inputs:
    - id: "raw/wetteksten/AWW-2017.pdf"
      sha256: "abc123..."
      version: "2024-12-15-ejustice-snapshot"
  tooling:
    pipeline: "etl/convert.py"
    pipeline_version: "a1b2c3"   # git short-sha of semver
    model: "claude-opus-4-7"     # null bij niet-LLM stappen
    prompt_version: "etl-qa-v3"  # idem
  generated_at: "2026-05-07T10:23:00Z"
  stale: false
  stale_reason: null
```

**Per artefact-type plek**:
- Markdown-bronnen: in YAML frontmatter
- RAG-chunks: als metadata-velden in ChromaDB
- Concept-records: als top-level `_provenance` veld in JSON
- Snapshot-fiches: in YAML frontmatter

**Stale-marking**: input-hash verandert → `tools/lib/provenance.py` cascadeert `stale: true` + reden naar alle downstream artefacten. Geen automatische regeneratie (zie ADR-003).

**Versie-conventies**:
- `pipeline_version`: git short-sha van de tool-commit als die in repo zit
- `model`: exacte modelnaam (incl. minor versie indien relevant)
- `prompt_version`: handmatige semver per prompt-template; templates leven in `prompts/`

## Gevolgen

- `tools/lib/provenance.py` is nieuwe module — read/write/cascade helpers
- Alle bestaande ETL-, indexering- en extractie-tools krijgen een provenance-write-stap
- `tools/etl/mark_stale.py` (nieuw) — input-veranderingen detecteren via hash-vergelijking, stale-flag cascaderen
- Bestaande artefacten zonder provenance worden geleidelijk gemigreerd; tot dan wordt afwezigheid van provenance gelijkgesteld aan `stale: unknown`
- Reprocessing-tooling (ADR-003) leest provenance om te beslissen wat te draaien
