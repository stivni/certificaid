# ADR-004: Provenance & versionering

**Status**: Draft
**Datum**: 2026-05-07 (gewijzigd 2026-05-08: `trust:` subkey toegevoegd aan schema)

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
  trust:                         # zie ADR-005 §5 — kwaliteits-gate output
    status: "unreviewed"         # unreviewed | trusted | needs-rework | rejected
    qa_version: null             # run-id van qa_bron.py / verdicts-bestand
    confirmed_at: null           # ISO-datum van laatste status-wijziging
    confirmed_by: null           # "human" | "subagent-sonnet-4-6" | "default" | …
    rationale: null              # 1-3 zinnen optionele toelichting
```

**Per artefact-type plek**:
- Markdown-bronnen: in YAML frontmatter
- RAG-chunks: als metadata-velden in ChromaDB
- Concept-records: als top-level `_provenance` veld in JSON; **per veld een eigen sub-blok** zodat veld-precieze stale-marking mogelijk is (zie ADR-008 §6 — `main_rule`-veld kan stale worden zonder dat `exceptions` stale wordt). Concept-record `_provenance` is de **autoritatieve permanente provenance-laag** voor downstream-impactanalyses (`remove_bron.py`, `mark_stale.py`); tijdelijke extractie-artefacten zoals vermoeden- en retrieval-JSONs in `data/extractie/` mogen op elk moment opgeruimd worden zonder dependency-verlies (zie ADR-008 §7).
- Snapshot-fiches: in YAML frontmatter

**Stale-marking**: input-hash verandert → `tools/lib/provenance.py` cascadeert `stale: true` + reden naar alle downstream artefacten. Geen automatische regeneratie (zie ADR-003).

**Trust-marking**: `trust.status` is de operationele output van de kwaliteits-gate (ADR-005 §5). Default `unreviewed` voor alle nieuwe of bestaande bronnen zonder expliciete beoordeling. Wordt door `tools/etl/mark_trusted.py` op `trusted | needs-rework | rejected` gezet, eventueel vanuit een subagent-verdict-bestand. `tools/rag/rag_index.py` filtert default op `trust.status == "trusted"`.

Verband met stale: een ETL-update die een bron hercreëert kan beschouwd worden als reden om de vorige trust-confirmatie te laten vervallen (terug naar `unreviewed`). Die cascade is nog niet geïmplementeerd; voorlopig blijft trust expliciet door de mens beheerd via `mark_trusted.py`.

**Chunk-id-stabiliteit als requirement**: voor incremental rebuild (alleen veranderde chunks her-embedden, alleen stale concept-velden her-extraheren) moeten chunk-ids stabiel zijn over runs zolang de chunk-strategie ongewijzigd is.

- Chunk-ids volgen een deterministisch patroon op basis van bron-stem + structureel anker (zie ADR-006 §3.1 — wettekst: `__art_<nr>`; norm: `__sec_<slug>`; advies: enkel `__sec_<slug>` indien gesplitst).
- Per chunk wordt zijn content-sha256 als metadata-veld in ChromaDB opgeslagen (`chunk_sha`). Een re-run vergelijkt nieuwe chunk-sha tegen opgeslagen waarde:
  - sha gelijk → skip (chunk ongewijzigd, embedding hergebruikt)
  - sha verschilt → upsert (her-embedden, downstream concept-velden via input-id `<chunk-id>` als stale gemarkeerd)
  - chunk-id verdwijnt → delete (downstream concepten met die chunk-id als input → stale + reden "input verdwenen")
- Als de chunk-strategie zelf verandert (config gewijzigd: andere splitting-grenzen, ander breadcrumb-format) bumpt `pipeline_version` van `rag_index`. Dat is een tooling-input-verandering die alle chunks stale maakt (ook als content gelijk is) → full rebuild.

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
