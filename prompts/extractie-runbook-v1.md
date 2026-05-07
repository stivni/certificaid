# Runbook: concept-extractie per taakblok

Orkestratie-instructies voor een Claude Code subagent (Opus) die voor één taakblok de seed-extractie uitvoert. Implementeert ADR-008 §2 (Programma-gestuurde extractie, fases A–C).

> **Lees eerst** (in deze volgorde):
> 1. `CLAUDE.md` — vijf absolute regels, in het bijzonder regel 3 (geen API in build-pipeline) en regel 1 (geen wetsinhoud zonder bronverwijzing).
> 2. `docs/concept-schrijfregels.md` — wat IS een concept, taal, granulariteit, smell-tests, confidence.
> 3. `docs/adr/ADR-007-conceptmodel.md` — node-types, edge-types, source-schema, status-flow.
> 4. `docs/adr/ADR-008-concept-extractie.md` §2.B/C — multi-level retrieval, live duplicate-check, variabel record-aantal.
> 5. `prompts/seed-v1.md` — output-schema voor één seed-record (jij bent zelf de "LLM" voor seed-v1; je leest dit als spec, niet als external prompt).
> 6. `prompts/verdiep-v1.md` — alleen als deze run verdieping doet, niet bij seed-only runs.

## Inputs

Argumenten waarmee je opgestart wordt:

| Argument | Voorbeeld |
|---|---|
| Programmaonderdeel | `data/programmaonderdelen/4.0-deontologie.json` |
| Taakblok-code | `4.0.D1.1` |
| ChromaDB-pad | `data/chroma_db_4.0` (POC) of `data/chroma_db` (volledig) |

Afgeleide bestandspaden:
- Vermoedens: `data/extractie/<po>/vermoedens/<taakblok>.json` (al genormaliseerd via `normalize_vermoedens.py`)
- Retrieval-output: `data/extractie/<po>/retrieval/<taakblok>.json` (bouw je in stap 1)
- Seed-log: `data/extractie/<po>/seed_log_<taakblok>.json` (bouw je incrementeel doorheen de run)
- Concept-records: `data/concept_records/<id>.json`

## Stap 1 — Retrieval-batch ophalen

Run één keer aan het begin (alle queries in één model-load):

```bash
python tools/extractie/retrieve_batch.py \
    --vermoedens data/extractie/<po>/vermoedens/<taakblok>.json \
    --programmaonderdeel data/programmaonderdelen/<po-bestand>.json \
    --chroma <chroma-pad> \
    > data/extractie/<po>/retrieval/<taakblok>.json
```

Lees de output. Per vermoeden krijg je een lijst chunks met `rerank_score`, `bron`, `artikel`, `text`. Top rerank-score = relevantie-anker voor stap 4.

## Stap 2 — Per-vermoeden lus

Voor elk vermoeden in het retrieval-bestand: doorloop stappen 3 → 8.

Verwerk vermoedens **één voor één in volgorde**. Schrijf na elk concept eerst de file én de incrementele index voordat je naar het volgende gaat — het volgende vermoeden moet jouw zonet geschreven concept terugvinden in de duplicaat-check.

## Stap 3 — Duplicate-check

```bash
python tools/extractie/index_concept_incremental.py \
    --duplicaat-check "<naam-van-vermoeden>" \
    --chroma <chroma-pad> \
    --drempel 0.80
```

Interpretatie:
- **Score ≥ 0.80** op een bestaand concept → mogelijk duplicaat. Beoordeel: is het écht hetzelfde fenomeen?
  - Ja → `MERGE`-actie: voeg eventuele nieuwe info uit de chunks toe aan het bestaande record (verdiep-stijl), schrijf het terug, log als `merged_into:<bestaand-id>`. Géén nieuwe seed.
  - Nee → ga door als `DISTINCT`, motiveer het verschil in het seed-log.
- **Score 0.65 – 0.80** → grijze zone. Default = nieuwe seed, maar log expliciet de top-1 kandidaat + score zodat een mens later kan reviewen.
- **Score < 0.65** → veilig nieuw concept.

## Stap 4 — Relevantie-check

Kijk naar de top rerank-score van de chunks voor dit vermoeden in het retrieval-bestand:

| Top score | Actie |
|---|---|
| ≥ 0.50 | `SEED` — schrijf record met confidence-labels per claim |
| 0.30 – 0.50 | `SEED` met `_notitie: "zwak gegrond, te verifiëren"` op het zwakste veld |
| < 0.30 | `REJECT` — geen record schrijven; log met reden |

## Stap 5 — Seed-record schrijven (als niet REJECT/MERGE)

Volg `prompts/seed-v1.md` voor het output-schema. Belangrijke punten:

- `id` = slug van de naam (kleine letters, koppeltekens, ≤ 60 tekens)
- `status: "seed"`, `schema_version: "1.0"`
- `main_rule` of `definitie` (níet beide, behalve voor sommige beginsels)
- Per claim: `confidence` + `source` (verplicht voor `grounded`)
- Edges met `_dangling: true` voor targets die nog niet bestaan
- Per-veld provenance-blok met chunk-ids die je voor dat veld gebruikt hebt

Schrijf naar `data/concept_records/<id>.json`. Gebruik `Write`-tool, niet bash heredocs.

**Splits/voeg toe**: als je tijdens schrijven merkt dat het vermoeden eigenlijk **twee** fenomenen bevat → schrijf twee records, log als `split_into:[<id1>, <id2>]`. Als een edge een dangling-target heeft die zelf een seed verdient → log als `added:<id>` en plaats het op de queue voor de volgende ronde (niet nu).

## Stap 6 — Concept incrementeel indexeren

Direct na het wegschrijven van het record:

```bash
python tools/extractie/index_concept_incremental.py \
    --concept data/concept_records/<id>.json \
    --chroma <chroma-pad>
```

Hierdoor vindt het volgende vermoeden jouw zonet geschreven concept terug bij zijn duplicate-check.

## Stap 7 — Programmaonderdeel-JSON updaten

Voor elk kenniselement in `vermoeden.kenniselementen` dat dit concept dekt: voeg `<id>` toe aan `kenniselementen[<code>].concepten` in het programmaonderdeel-bestand. Schrijf de file terug.

Als `vermoeden.kenniselementen` leeg is (vermoeden uit pure taak/skill): kijk of de taak/doelstelling in een `taakblokken[].taken[].concepten` of `.doelstellingen[].concepten` veld kan landen. Zo niet: niet forceren — sommige concepten leven enkel in `data/concept_records/` en worden via reverse-lookup ontdekt (`tools/lib/coverage.py`).

## Stap 8 — Seed-log bijwerken

Append een entry per vermoeden aan `data/extractie/<po>/seed_log_<taakblok>.json`:

```json
{
  "taakblok": "4.0.D1.1",
  "model": "claude-opus-4-7",
  "started_at": "<ISO timestamp>",
  "finished_at": "<ISO timestamp>",
  "decisions": [
    {
      "vermoeden": "Beroepsgeheim van de gecertificeerd accountant",
      "actie": "kept",
      "concept_id": "beroepsgeheim-gecertificeerd-accountant",
      "duplicate_check": { "top_id": null, "top_score": 0.42 },
      "relevantie": { "top_rerank": 0.71 },
      "notitie": ""
    },
    {
      "vermoeden": "Onafhankelijkheidsbeginsel",
      "actie": "merged_into",
      "merged_into": "onafhankelijkheid-accountant",
      "duplicate_check": { "top_id": "onafhankelijkheid-accountant", "top_score": 0.87 }
    },
    {
      "vermoeden": "Cliëntaanvaardingsbeleid",
      "actie": "rejected",
      "reden": "top rerank-score 0.18, geen gegronde bron in scope",
      "relevantie": { "top_rerank": 0.18 }
    },
    {
      "vermoeden": "Cliëntenonderzoek (Know Your Customer)",
      "actie": "split",
      "split_into": ["clientenonderzoek-procedure", "ubo-identificatie"],
      "reden": "Vermoeden bevatte zowel de procedure als het UBO-begrip"
    }
  ]
}
```

`actie`-waarden: `kept` · `merged_into` · `rejected` · `split` · `added` (voor extra seeds via dangling-resolutie).

## Stap 9 — Einde van de run

Aan het einde van de run:

1. Sluit het seed-log af met `finished_at`.
2. Dekkingscheck:

   ```bash
   python tools/lib/coverage.py --po <po> --gaten
   ```

   Print het naar de gebruiker: hoeveel kenniselementen in dit programmaonderdeel zijn nu gedekt door minstens één concept?
3. Geef een korte samenvatting (max 10 regels) terug aan de gebruiker:
   - N vermoedens verwerkt → M records geschreven
   - Aantal merged / rejected / split
   - Eventuele dangling-edges die nog seeds vereisen (voor volgende ronde)

## Spelregels (samengevat)

- **Geen anthropic.Anthropic()-calls.** Jij bent de LLM, je leest dit document, je gebruikt de Bash/Read/Write tools. Geen Python-script mag namens jou een API aanroepen.
- **Eén concept tegelijk.** Schrijf, indexeer, log → dan pas naar het volgende vermoeden.
- **Lege velden zijn OK.** Sparse-by-design (ADR-007). Liever niets dan iets onbewezen.
- **Confidence-labels per claim.** `grounded` vereist altijd een `source`. Bij twijfel `inferred` of veld weglaten.
- **Schrijfregels (`docs/concept-schrijfregels.md`) zijn bindend.** Wijken ze van een instructie hier af? Schrijfregels winnen.
- **Stop bij twijfel over scope-uitbreiding** (nieuw node-type, nieuw edge-type, nieuw veld). Voeg het toe aan `data/concept_records/_voorgestelde_types.yaml` en gebruik `voorgesteld:<naam>` in het record. Niet zelf het schema bumpen.
