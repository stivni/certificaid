# Wave-2 launch — beschrijven + accountant_perspectief

## Context (status per 2026-05-23)

- Schema 2.1 v1.5 live. Canonieke spec: `docs/schema-v15-besluit.md`. JSON Schema: `data/concepten/schema-2.1.schema.json`.
- 396 records in `data/concepten/records/`. Alle records hebben minstens `inhoud.kern`.
- 371 records zijn **placeholders**: bevatten `inhoud.kern` maar **geen `inhoud.elementen[]`**. Dit zijn de doelrecords voor wave-2.
- 25 records zijn al gevuld (gemigreerd vanuit schema 2.0, hebben `inhoud.elementen[]`). Sla die over.
- 0 records hebben `beschrijven` in `metadata.changelog` — wave-2 is de eerste operatie-batch.
- 1 record heeft `inhoud.accountant_perspectieven` — alle overige 395 wacht op Pass 2.
- **CLAUDE.md regel 3**: geen `anthropic.Anthropic()`-calls vanuit scripts. Alle LLM-werk uitsluitend via Agent-tool in Claude Code.

### Concept-type verdeling van de 371 placeholders

| concept_type | count |
|---|---|
| kader | 158 |
| procedure | 78 |
| regime | 73 |
| instrument | 23 |
| verrichting | 15 |
| ratio | 14 |
| balanspost | 10 |

---

## Doel

**Pass 1 (verplicht)**: `beschrijven` op alle 371 placeholders. Vult `inhoud.kern`, `inhoud.elementen[]` en `inhoud.gebruikscontext` vanuit training-data. Geen RAG, geen MCP-calls. Confidence uitsluitend `verondersteld` of `betwijfeld`.

**Pass 2 (selectief)**: `accountant_perspectief` op records waar beroepsrol-werk zinvol is. Vuistregel: vul voor `instrument`, `procedure`, `regime`, `verrichting`, `balanspost` en inhoudelijke `kader`-records. Sla over voor `ratio`-records en abstracte kaders zonder handelingsdimensie. Schatting: 60-70% van de 371 records (~220-260).

### Open beslispunt voor uitvoerende sessie

Twee opties voor uitvoering:

1. **2 aparte passes** (aanbevolen): eerst alle 371 `beschrijven`, daarna selectief `accountant_perspectief`. Voordeel: Pass 1-resultaat is veiliggesteld; schema-failures in Pass 2 raken niet aan gevulde kern.
2. **1 gecombineerde pass**: `beschrijven` + `accountant_perspectief` in één prompt per record. Voordeel: minder agent-spawns (~371 ipv 371 + ~230). Risico: langere prompt verhoogt schema-fout-kans.

Kies voor aanvang. Dit document beschrijft de 2-passes-aanpak als default.

---

## Hoe begin je

1. Lees deze documenten in volgorde:
   - `CLAUDE.md` (project-context + 9 absolute regels)
   - `docs/schema-v15-besluit.md` (schema-spec v1.5 — bron-van-waarheid)
   - `docs/adr/ADR-029-schema-21-operaties-model.md` (operaties-model + state-tracking)
   - `prompts/operaties/beschrijven.md`
   - `prompts/operaties/accountant_perspectief.md` (voor Pass 2)

2. Lees referentie-example: `data/concepten/examples/obligatielening-01-beschrijven.json`

3. Verifieer pre-conditions:

   ```bash
   python3 tools/extractie/multi_pass_extract.py status
   # verwacht: X/396 gevuld, waarbij X = 25 (gemigreerde records)
   ls data/concepten/schema-2.1.schema.json
   ls data/concepten/records-index.compact.txt
   ls data/concepten/examples/obligatielening-01-beschrijven.json
   ```

4. Bouw de queue van 371 fiche-ids:

   ```bash
   python3 << 'EOF'
   import json, pathlib
   d = pathlib.Path('data/concepten/records')
   ids = [r.stem for r in sorted(d.glob('*.json'))
          if not json.loads(r.read_text()).get('inhoud', {}).get('elementen')]
   print('\n'.join(ids))
   print(f'\n# totaal: {len(ids)}')
   EOF
   ```

5. Start eerste batch van 12 via Agent-tool (zie spawn-template hieronder).

---

## Workflow — rolling 12-parallel direct-flow

- Geen `/tmp` staging. Sub-agent schrijft direct naar `data/concepten/records/<fiche-id>.json`.
- Sub-agent-spawning uitsluitend via **Agent-tool in Claude Code** — geen Python-scripts met Anthropic API.
- Queue beheer in orchestrator-hoofd (jij, Opus): Python-lijst van 371 ids, verwerk in batches van 12 parallel.
- Per batch: spawn 12 agents tegelijk, wacht tot alle 12 klaar zijn, voer dan auto-fix + validate uit per record, log failures, spawn volgende batch.
- Commits: na elke batch van 12 (of maximaal elke 25 records) een `git commit`.
- Steeds 12 agents in flight tot queue leeg.

---

## Sub-agent spawn-template

Spawn elke sub-agent via de Agent-tool. Prompt per agent (vervang `<FICHE-ID>`):

```
Je bent een Certificaid draft-agent — operatie `beschrijven` (schema 2.1 v1.5).

**Fiche**: `<FICHE-ID>`
**File**: `data/concepten/records/<FICHE-ID>.json` — lees, bewerk, overschrijf direct.

**Lees vóór alles**:
1. `prompts/operaties/beschrijven.md` — volledige werkwijze en discipline
2. `data/concepten/schema-2.1.schema.json` — $comment/$description per $def is bron-van-waarheid
3. `data/concepten/records-index.compact.txt` — scope-anker (vermijd duplicatie, suggereer relaties)
4. `data/concepten/examples/obligatielening-01-beschrijven.json` — shape-referentie

**VERBODEN**:
- Geen MCP-calls (`zoek_bronnen`, `lees_record`, etc.) — uitsluitend training-data
- Geen /tmp schrijven — direct naar `data/concepten/records/<FICHE-ID>.json`
- Confidence `geciteerd`/`afgeleid`/`weerlegd` — alleen `verondersteld` of `betwijfeld`

**CRITICAL structuur (v1.5)**:
- `id`, `naam`, `concept_type`, `schema_version`, `metadata`, `inhoud`, `relaties` zijn top-level
- `relaties[]` NOOIT binnen `inhoud`
- Kern-velden onder `inhoud.kern.{definitie,substantie,rationale}` — NIET losse keys op `inhoud`
- Tekst-property heet `tekst` (niet `text`)
- Ankers staan in `metadata.ankers` (niet `linked_anchors`)

**AI-bron**: `{"type": "ai_model", "naam": "claude-sonnet-4-6", "datum": "<vandaag-ISO>"}`

**Changelog**: voeg entry toe `{"operatie": "beschrijven", "timestamp": "<ISO>", "model": "<jouw-model>"}`

**Eindrapport**: fiche-id, file-size (bytes), aantal `inhoud.elementen[]`, MCP-calls (verwacht: 0).
```

Voor Pass 2 (`accountant_perspectief`): gebruik dezelfde structuur maar vervang de prompt-referentie door `prompts/operaties/accountant_perspectief.md`. Controleer bij aanvang of `data/concepten/examples/obligatielening-02-accountant_perspectief.json` bestaat — per 2026-05-23 was dit bestand er niet.

---

## Auto-fix + validate sequentie

Na elke agent-completion, draai per record:

```python
import json, pathlib, sys
sys.path.insert(0, 'tools/extractie')
from multi_pass_extract import auto_fix_common_bugs, _validator

def fix_en_validate(fiche_id: str) -> tuple[bool, list[str]]:
    pad = pathlib.Path(f'data/concepten/records/{fiche_id}.json')
    rec = json.loads(pad.read_text())
    origineel = rec.copy()
    rec, fixes = auto_fix_common_bugs(rec, origineel)
    pad.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    errors = list(_validator().iter_errors(rec))
    if errors:
        paden = [' > '.join(str(p) for p in e.absolute_path) for e in errors[:3]]
        return False, fixes + [f'schema-error [{p}]: {e.message[:80]}'
                               for p, e in zip(paden, errors[:3])]
    return True, fixes
```

**Bij schema-failure**: re-spawn de agent 1x met expliciete melding van de error-paden. Bij tweede failure: skip + log fiche-id voor handmatige review.

---

## Commit-ritme

Na elke batch van 12:

```bash
git add data/concepten/records/
git commit -m "wave-2 beschrijven: batch <N> (<X>/<Y> records klaar)"
```

---

## Stopcriteria

- **Queue empty** — normaal einde.
- **Schema-failure-rate > 20% na auto-fix** over een batch van 24 records — stop, analyseer root cause, pas spawn-template of prompt aan voor verdere batches.
- **Gebruiker breekt af** — commit wat klaar is.

---

## Rapportage tussendoor

Elke 25 afgeronde records:

```
=== Wave-2 voortgang ===
Pass 1 beschrijven: X/371 klaar | queue: Y | failures: Z
Auto-fixes deze batch top-3: [...]
```

Bij failure: log fiche-id + de eerste 3 error-paden.

---

## Eindrapport

Geef aan het einde van Pass 1 (en opnieuw na Pass 2):

1. Totaal commits valid (records met 0 schema-errors na auto-fix)
2. Totaal failures (welke fiche-ids)
3. Auto-fix-frequentie per categorie (top-5, uit de `fixes`-lijsten)
4. Records met mogelijk info-verlies (meer dan 3 auto-fixes nodig)
5. Records die handmatige review vragen (2x re-spawn gefaald)
6. Pass 2 voorbereiding: lijst van fiche-ids die in aanmerking komen voor `accountant_perspectief`
7. Verificatie-commando: `python3 tools/extractie/multi_pass_extract.py progress`

---

## Verwacht looptijd

- Pass 1 (371 records, 12-parallel, 1-3 min/record): ~1.5-2u
- Pass 2 (~230 records, 12-parallel, 1-2 min/record): ~30-45 min

---

## Aannames in dit document

- `obligatielening-02-accountant_perspectief.json` bestaat mogelijk niet op disk — controleer bij aanvang van Pass 2.
- De Agent-tool-syntax in de spawn-template is de standaard Claude Code syntax. Pas aan als de actieve sessie een afwijkende syntax gebruikt.
- `is_skelet()` in `multi_pass_extract.py` detecteert `inhoud == {}`. De 371 placeholders in wave-2 zijn NIET skelet in die zin — ze hebben `inhoud.kern` maar geen `inhoud.elementen`. De `progress`-output toont ze als "Gevuld". Gebruik de queue-query hierboven (filtert op `elementen`) om de echte placeholder-lijst te bouwen.
- De 25 gemigreerde records (met `inhoud.elementen`) staan niet in de queue als je de query correct gebruikt.
