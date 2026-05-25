# Wave-2 launch — beschrijven + accountant_perspectief

## Context (status per 2026-05-23)

- Schema 2.1 v1.5 live. Canonieke spec: `docs/schema-v15-besluit.md`. JSON Schema: `data/concepten/schema-2.1.schema.json`.
- 396 records in `data/concepten/records/`. Alle records hebben minstens `inhoud.kern`.
- 371 records zijn **placeholders** (`inhoud.kern.definitie.tekst == naam.primair`, geen `elementen[]`).
- 25 records zijn al gevuld (gemigreerd vanuit schema 2.0).
- **CLAUDE.md regel 3**: geen `anthropic.Anthropic()`-calls vanuit scripts. Alle LLM-werk uitsluitend via Agent-tool in Claude Code.

---

## Doel

**Pass 1 (verplicht)**: `beschrijven` op **alle 396 records — aanvullend**. Voor placeholders = cold-start (vul kern + elementen + gebruikscontext). Voor al-gevulde records = augment: verrijk waar dunner, herschrijf niet als bestaande inhoud klopt, voeg ontbrekende elementen toe. Confidence uitsluitend `verondersteld` of `betwijfeld`.

**Pass 2 (selectief)**: `accountant_perspectief` op records waar beroepsrol-werk zinvol is. Vuistregel: vul voor `instrument`, `procedure`, `regime`, `verrichting`, `balanspost` en inhoudelijke `kader`-records. Sla over voor `ratio`-records en abstracte kaders zonder handelingsdimensie. Schatting: 60-70% van 396 (~240-280).

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

4. Bouw de queue van alle 396 fiche-ids (placeholders + al-gevulde):

   ```bash
   python3 -c "
   import pathlib
   ids = [p.stem for p in sorted(pathlib.Path('data/concepten/records').glob('*.json'))]
   print('\n'.join(ids))
   print(f'# totaal: {len(ids)}')
   "
   ```

5. Start de **rolling pool** van 12 via Agent-tool (zie spawn-template hieronder).

---

## Workflow — **rolling** 12-parallel, direct-flow, aanvullend

**Rolling = NIET batch**. Niet "spawn 12, wacht op alle 12, spawn volgende 12". Wel:

1. Initialiseer queue = lijst van 396 fiche-ids.
2. Spawn de eerste 12 agents (één per fiche). Markeer "in-flight: 12".
3. **Bij elke notification dat één sub-agent klaar is**:
   - Run auto-fix + validate op die record (zie sequentie hieronder)
   - Log resultaat (success / fix-list / error)
   - **Direct** pop de volgende fiche-id uit de queue en spawn een nieuwe agent
   - In-flight blijft 12 (tot queue leeg is)
4. Wanneer queue empty + alle in-flight klaar: einde.

Voordelen rolling boven batch: snelle agents wachten niet op trage; volledige throughput; minder dode tijd.

**Direct-flow**: sub-agent schrijft direct naar `data/concepten/records/<fiche-id>.json`. Geen `/tmp` staging.

**Aanvullend (additive)**: voor records die al gevuld zijn (heeft `inhoud.elementen[]` met content), behoud bestaande inhoud waar correct; alleen aanvullen waar dun, ontbrekende elementen toevoegen, gebruikscontext-arrays uitbreiden. Niet overschrijven, niet zonder reden herschrijven.

**Spawning uitsluitend via Agent-tool**, geen Python-script met Anthropic API (cf. CLAUDE.md regel 3).

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

**MODUS — aanvullend** (additive):
- Als record al `inhoud.elementen[]` met content heeft: BEHOUD bestaande items. Vul aan waar dun, voeg ontbrekende toe. Niet zonder reden herschrijven.
- Als record placeholder is (geen `elementen[]`): cold-start vullen.
- Vergelijk bestaande inhoud met je gegenereerde inhoud — bij overlap: keep de bestaande (heeft mogelijk wettekst-bronnen die je nu niet kan reproduceren).

**VERBODEN**:
- Geen MCP-calls (`zoek_bronnen`, `lees_record`, etc.) — uitsluitend training-data
- Geen `/tmp` schrijven — direct naar `data/concepten/records/<FICHE-ID>.json`
- Confidence `geciteerd`/`afgeleid`/`weerlegd` — alleen `verondersteld` of `betwijfeld` (downgrade bestaande `geciteerd`/`afgeleid` NIET; laat staan)

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

## Files op disk, geen git-commits

- Sub-agenten **schrijven direct naar `data/concepten/records/<fiche-id>.json`** — de wijzigingen zijn meteen zichtbaar op het filesystem (Finder, editor, `cat`, etc.). Geen `/tmp`-staging.
- **Niet `git commit` draaien tijdens de run.** Files blijven als "modified / unstaged" in `git status` tot wave-2 klaar is en de gebruiker beslist over commit-strategie.
- Bij abort: bestanden blijven staan zoals laatst geschreven; gebruiker beslist over `git restore` (rollback) of `git add` + commit (behoud).

---

## Stopcriteria

- **Queue empty** — normaal einde.
- **Schema-failure-rate > 20% na auto-fix** over een loop van 24 opeenvolgende afgeronde records — stop, analyseer root cause, pas spawn-template of prompt aan voor verdere records.
- **Gebruiker breekt af** — stop rolling, laat in-flight afronden, dan rapport.

---

## Rapportage tussendoor

Elke 25 afgeronde records (geteld over rolling completion-stream):

```
=== Wave-2 voortgang ===
Pass 1 beschrijven: X/396 klaar | in-flight: 12 | queue: Y | failures: Z
Auto-fixes recent top-3: [...]
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

- Pass 1 rolling (396 records, 12-parallel, ~2-3 min effectief/record): **~1.5-2u** continu rolling
- Pass 2 (~250 records, 12-parallel): **~30-45 min**

---

## Aannames in dit document

- De Agent-tool-syntax in de spawn-template is de standaard Claude Code syntax. Pas aan als de actieve sessie een afwijkende syntax gebruikt.
- `is_skelet()` in `multi_pass_extract.py` detecteert `inhoud == {}` — niet bruikbaar voor onze placeholder-detectie (de 371 hebben `inhoud.kern`). Geen filter nodig: de queue bevat ALLE 396, prompts hanteren aanvullend-modus.
- Voor Pass 2: gebruik `data/concepten/examples/obligatielening-02-accountant_perspectief.json` als shape-referentie.
