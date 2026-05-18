# ADR-019: Centrale records-API + RAG-parity discipline

**Status**: Draft
**Datum**: 2026-05-17
**Verwante ADRs**: ADR-018 (embedding-daemon — schrijft naar `concepten`-collection), ADR-008 (concept-extractie — bevat 7 van de 9 huidige schrijvers), ADR-007 (conceptmodel — schema dat geschreven wordt)

## Context

Concept-records leven op twee plekken tegelijk: op disk in `data/concepten/records/*.json` én geïndexeerd in de `concepten`-collection van `data/rag/main` (ADR-006, ADR-018). Beide zijn nodig — disk is source-of-truth, RAG is de doorzoekbare projectie die SYNTHESIZE / VERIFY / tutor gebruiken voor globale record-awareness.

Vandaag schrijven **zeven scripts** naar disk zonder centrale RAG-discipline:

- `tools/leermateriaal/propose_competenties.py`
- `tools/leermateriaal/lib/frontmatter.py`
- `tools/etl/remove_bron.py`
- `tools/etl/mark_stale.py`
- `tools/extractie/verify_records.py`
- `tools/extractie/index_concept_incremental.py` (wel met daemon-call)
- `tools/rag/rag_index.py`

> Update 2026-05-18: `enrich_records.py` en `auto_merge.py` zijn verwijderd (ADR-008 §18 — EXTRACT v4 vervangt ENRICH/AUTO-MERGE). De refactor-tabel hieronder noemt ze nog als historische scope-uitleg.

Symptomen die we al gemeten hebben (snapshot 2026-05-17):

- **Concept-RAG bevroren** op 2026-05-15 (69 items) terwijl 344 records op disk stonden, allemaal schema 1.4. Indexer-run was nooit aangeroepen na schema-migratie.
- **39 ghost-entries** in de collection na heropbouw: 30× `concept:`-prefix + 9× `competentie:`-prefix uit een eerdere id-conventie. Records waren op disk hernoemd zonder dat de oude id uit RAG verdween. ChromaDB's upsert-per-id is atomair maar schrijft geen oude ids weg.
- **Geen mechanisme om afwijkingen vroeg te detecteren** — drift werd pas zichtbaar toen we manueel telden.

Twee meta-problemen:

1. **Disciplinepatroon ontbreekt**: niets dwingt af dat een record-write ook RAG bijwerkt. Een nieuwe schrijver-script (of een refactor) kan de regel "altijd RAG updaten" trivial overslaan.
2. **Id-mutaties (rename/delete) hebben geen contract**: een record schrijven met nieuwe id zonder de oude te verwijderen leidt stilletjes tot ghosts. Hetzelfde geldt voor een file-delete zonder RAG-verwijdering.

## Beslissing

Bouw één centrale module `tools/lib/records_api.py` als **enige toegestane interface** voor mutaties aan `data/concepten/records/*.json`. Alle bestaande schrijvers refactor'en om hem te gebruiken. Een pre-commit hook beschermt tegen omzeiling.

### API-oppervlak

```python
# tools/lib/records_api.py

def save_record(record: dict) -> None:
    """
    Atomair: schrijf record naar disk + upsert in concept-RAG.
    Faalt loud als daemon niet bereikbaar — geen disk-only writes.
    Bestaande id → in-place update (zowel disk als RAG).
    Nieuwe id → nieuwe entry in beide.
    """

def rename_record(old_id: str, new_record: dict) -> None:
    """
    Atomair: verwijder old_id uit RAG + verwijder oud bestand,
    schrijf nieuw bestand + upsert nieuwe id in RAG.
    new_record['id'] moet ≠ old_id zijn.
    """

def delete_record(record_id: str) -> None:
    """
    Atomair: verwijder bestand + verwijder uit RAG.
    Faalt als record niet op disk of niet in RAG.
    """

def audit_parity() -> dict:
    """
    Returnt {
      'disk_ids': set[str],
      'rag_ids': set[str],
      'ghosts': list[str],     # in RAG, niet op disk
      'missing': list[str],    # op disk, niet in RAG
      'ok': bool,
    }
    Read-only. Geen mutaties. Veilig om vaak te draaien.
    """
```

### Atomiciteitscontract

Beste-inspanning-atomair via volgorde:

1. **save_record**: daemon `/index-concept` → 200 OK → disk write → render concept-fiche. Disk-write-fout → daemon `/delete-concept` om RAG terug consistent te krijgen + raise. Render-fout → log warning, geen rollback (markdown is afgeleid artefact, altijd herbouwbaar).
2. **rename_record**: daemon `/delete-concept(old_id)` → daemon `/index-concept(new)` → disk delete oud + write nieuw → render nieuw + verwijder oude markdown. Bij stap 2 of 3 falen: rollback van eerder gelukte stappen + raise. Render-fout → log warning, geen rollback.
3. **delete_record**: disk delete → daemon `/delete-concept` → verwijder markdown. Bij stap 2 falen: log loud (state nu wel consistent: niets op disk, oude entry nog in RAG — zal opnieuw kunnen worden weggehaald). Markdown-verwijdering na stap 3: log warning bij falen, geen raise.

### Content-sync

**Probleem**

De records-API garandeert na elke succesvolle write dat `data/concepten/records/<id>.json` en de `concepten` ChromaDB-collection in sync zijn (§Atomiciteitscontract). Maar `content/concepten/<id>.md` — de Quartz-gepubliceerde markdown-fiche — wordt alleen bijgewerkt als iemand handmatig `render_concept_fiche.py` aanroept. Drift sluipt onzichtbaar in: een record dat geüpdatet is via `save_record` kan een verouderde fiche in `content/concepten/` hebben die Quartz publiceert.

Andere render-scripts (`render_minicursus.py` → `content/studiemateriaal/`, `render_competentie_fiche.py` → `content/competenties/`) produceren output op programmaonderdeel- of competentieniveau — niet één-op-één per concept-record. Die vallen buiten scope van de records-API (eigen cadans, eigen triggers).

**Beslissing**

De records-API roept na elke succesvolle RAG + disk operatie ook `render_concept_fiche.render_naar_bestand()` aan voor het geraakte record. De render-stap is de derde stap in de atomaire flow:

```
save_record:   RAG (daemon) → disk → render
rename_record: RAG delete(oud) → RAG upsert(nieuw) → disk → render(nieuw) + markdown delete(oud)
delete_record: disk → RAG → markdown delete
```

**Render-semantiek**

- Render-fout (ImportError, TemplateError, OSError op write) → log `WARNING` maar fail `save_record`/`rename_record` NIET. Markdown is afgeleid en altijd herbouwbaar via `render_concept_fiche --alle`. Een render-fout blokkeert de record-write niet.
- Render is idempotent: zelfde record-input → zelfde markdown-output (deterministisch via Jinja2-templates). Veilig om vaak aan te roepen.
- Bij `delete_record`: verwijder ook `content/concepten/<id>.md` als die bestaat. Ontbrekend bestand is geen fout (no-op).

**Audit-uitbreiding**

`audit_parity()` krijgt een derde check naast disk-RAG parity: vergelijking van records op disk met markdown-fiches in `content/concepten/`. De functie retourneert extra sleutels:

```python
{
  'disk_ids': set[str],
  'rag_ids': set[str],
  'content_ids': set[str],         # ids met bestaande markdown-fiche
  'ghosts': list[str],             # in RAG, niet op disk
  'missing': list[str],            # op disk, niet in RAG
  'content_ontbreekt': list[str],  # op disk, niet als markdown-fiche
  'content_extra': list[str],      # markdown-fiche bestaat, niet op disk
  'ok': bool,                      # True alleen als alles in sync
}
```

Drie staten per record (ter documentatie):

| Status | disk | RAG | markdown |
|---|---|---|---|
| `disk_only` | ja | nee | nee |
| `disk_and_rag` | ja | ja | nee |
| `disk_and_rag_and_content` | ja | ja | ja |

Alleen `disk_and_rag_and_content` = volledig OK. `ok` in het resultaat is `True` alleen als er geen ghosts, geen missing, geen content_ontbreekt en geen content_extra zijn.

**Pre-commit hook uitbreiding**

De bestaande hook `scripts/git-hooks/pre-commit-records-parity.sh` wordt uitgebreid: `audit_parity()` faalt nu ook bij content-drift (ontbrekende of extra markdown-fiches). Dezelfde exit-1-semantiek als bij disk/RAG drift.

Daemon-uitbreiding nodig (ADR-018): nieuw endpoint `POST /delete-concept {id, chroma_path}`. Serialiseert via dezelfde `_operatie_lock` als `/index-concept`.

### Orphan-management (aanvulling 2026-05-18)

**Probleem**

De records-API garandeert na elke write dat disk, RAG en content in sync zijn voor het gemuteerde record zelf. Maar andere records kunnen `edges[].target` of `vergelijkingsparen[].vergelijking_met` bevatten die naar het gemuteerde id wijzen. Bij `delete_record(X)` of `rename_record(X → Y)` worden die verwijzingen in andere records niet bijgewerkt — VERIFY detecteert ze pas achteraf als broken refs.

Tijdens de 1.5.V EXTRACT v4-pass bleek dat ook twee bijkomende reference-types stale refs kunnen bevatten: `gebaseerd_op_concepten[]` (synthese-records) en `[[wikilinks]]` in vrije tekstvelden.

**Beslissing**

Bij `delete_record(X)`:
1. Scan alle records op disk op verwijzingen naar X (vier types — zie Scan-algoritme hieronder). Vóór disk-delete, zodat de scan nog werkzaam is.
2. Verwijder/degradeer die verwijzingen in elk geraakt record via `_verwijder_edges_naar()`.
3. Sla elk geraakt record opnieuw op via `save_record()` (cascadeert naar RAG + content).
4. Log per geraakt record: `"removed dangling edge to {X} from {Y}"` op WARNING-niveau.
5. Daarna delete X zelf (disk + RAG + content).

Bij `rename_record(X → Y)`:
1. Voer de rename zelf volledig uit (disk delete X, disk write Y, RAG delete X, RAG upsert Y, markdown delete X, render Y).
2. Scan alle records op disk op verwijzingen naar X (ná disk-write Y, zodat nieuw record al bestaat).
3. Update verwijzingen naar Y in elk geraakt record via `_redirect_edges_naar()`.
4. Sla elk geraakt record opnieuw op via `save_record()`.
5. Log per geraakt record: `"redirected edge {X} → {Y} in {Z}"` op INFO-niveau.

**Geen IncomingEdgesError** — silently auto-correct, met loud logging zodat de operator het ziet.

**Scan-algoritme**

`_scan_incoming_edges(target_id)` controleert per record vier referentie-types:

1. `edges[].target == target_id` — directe edges.
2. `vergelijkingsparen[].vergelijking_met == target_id` — vergelijkingsparen.
3. `target_id in gebaseerd_op_concepten[]` — exacte string match in de array van synthese-records.
4. `[[target_id]]` of `[[target_id|Display]]` wikilinks — recursief gescand via `_wikilink_ids_in_waarde()` over de volledige record-boom (dicts, lists, strings). Display-tekst na `|` wordt genegeerd bij het matchen; alleen het id-deel (vóór `|`) telt.

**Mutatiestrategie per reference-type bij delete**

| Type | Actie |
|---|---|
| `edges[].target` | Entry verwijderd uit lijst |
| `vergelijkingsparen[].vergelijking_met` | Entry verwijderd uit lijst |
| `gebaseerd_op_concepten[]` | target_id verwijderd uit array |
| `[[target_id]]` wikilink | Vervangen door plain tekst (target_id of display-naam) — de informatie blijft behouden, alleen de kapotte link verdwijnt |
| `[[target_id\|Display]]` wikilink | Vervangen door `Display` (plain tekst) |

Voorbeeld delete:
```
"Onderdeel van [[beroepsgeheim]] en [[aansprakelijkheid]]"
→ "Onderdeel van beroepsgeheim en [[aansprakelijkheid]]"
```

**Mutatiestrategie per reference-type bij rename (X → Y)**

| Type | Actie |
|---|---|
| `edges[].target` | old_id → new_id |
| `vergelijkingsparen[].vergelijking_met` | old_id → new_id |
| `gebaseerd_op_concepten[]` | old_id → new_id in de array |
| `[[old_id]]` wikilink | `[[old_id]]` → `[[new_id]]` |
| `[[old_id\|Display]]` wikilink | `[[old_id\|Display]]` → `[[new_id\|Display]]` |

Voorbeeld rename (beroepsgeheim → beroepsgeheim-gecertificeerd-accountant):
```
"Zie [[beroepsgeheim|Beroepsgeheim]] voor details."
→ "Zie [[beroepsgeheim-gecertificeerd-accountant|Beroepsgeheim]] voor details."
```

**Atomiciteitsimplicaties**

Cascade-saves zijn niet atomair ten opzichte van elkaar: als save_record faalt in stap N, zijn eerder geslaagde cascade-records al bijgewerkt. Dit is acceptabel — de cascade is een best-effort opruiming. Fouten in individuele cascade-saves worden gelogd op ERROR-niveau maar blokkeren de oorspronkelijke delete/rename niet.

**Performantie**

Scan over 430 records kost ~50ms (bestandssysteem-IO, geen RAG-call). Acceptabel. De recursieve wikilink-scan voegt per record een kleine constante factor toe (regex over string-leaves) — verwaarloosbaar.

**Hulpfuncties**

- `_scan_incoming_edges(target_id)` — scant alle records op vier referentie-types, retourneert lijst van `{record, pad}`
- `_verwijder_edges_naar(record, target_id)` — verwijdert edges/vergelijkingsparen/gebaseerd_op_concepten-entries; wikilinks → plain tekst
- `_redirect_edges_naar(record, old_id, new_id)` — vervangt old_id door new_id in alle vier referentie-types
- `_wikilink_ids_in_waarde(waarde)` — recursieve scanner, retourneert set van wikilink-ids
- `_vervang_wikilinks_in_waarde(waarde, old_id, new_id)` — recursieve vervanger; `new_id=None` → plain tekst (delete), `new_id` opgegeven → link-update (rename)
- `_iter_strings(waarde)` — yield alle string-leaves voor teldoeleinden (logging)

### Timeout-mitigatie (pilot-bevinding 2026-05-18)

De volgorde "daemon → 200 OK → disk write" werkt bij een nette daemon-fout (HTTP 4xx/5xx) maar **breekt bij timeout**: de client weet niet of de server het deed. In de EXTRACT v4-pilot op anchor 1.5.V.C gebeurde precies dat — eerste `save_record` hit timeout op cold-start (10s te kort voor bge-m3-warm-up), client raisde `DaemonUnavailableError`, maar daemon had de upsert wél doorgevoerd. Resultaat: ghost in RAG, niets op disk, geen automatische rollback.

Drielagige mitigatie:

1. **Verlengde cold-start timeout**: eerste `save_record`-call na proces-start krijgt 60s timeout (vs. 10s default). Voldoende voor bge-m3 cold-start (~5-15s) plus ChromaDB-init.
2. **Idempotente daemon-endpoints**: `/index-concept` is al idempotent (ChromaDB upsert per id), `/delete-concept` ook (DELETE WHERE id = ? is no-op als id niet bestaat). Client mag dus veilig retry'en bij timeout. Documenteer dit als contract.
3. **Post-failure parity-recovery**: na elke `save_record`-fout (timeout of anders) draait client automatisch `audit_parity()`. Detecteert ghost (record in RAG, niet op disk) → roept `/delete-concept` aan om RAG-state te herstellen. Logt loud zodat operator weet dat een recovery is gebeurd.

Pseudocode-update voor `save_record`:

```python
def save_record(record):
    try:
        daemon_post("/index-concept", record, timeout=cold_start_timeout())
        disk_write(record)
    except (Timeout, DaemonUnavailableError, OSError) as e:
        # Mogelijk consistente staat onbekend — verifieer
        parity = audit_parity()
        ghost = record['id'] in parity['ghosts']
        if ghost:
            daemon_post("/delete-concept", {'id': record['id']})
            log.warn("Rollback ghost na save_record-fout: %s", record['id'])
        raise
```

Failure modes-tabel uitgebreid:

| Scenario | Detectie | Reactie |
|---|---|---|
| Daemon-call timeout op cold start | `requests.Timeout` met elapsed < 30s | Behandel als mogelijke succes; audit_parity bepaalt of rollback nodig |
| Daemon-call timeout op warm call | `requests.Timeout` met elapsed > 30s | Idem; cold-start uitgesloten dus ofwel daemon-bug ofwel zware load |
| Daemon-restart tijdens save | `ConnectionError` op disk-write | audit_parity → rollback indien ghost |

Verificatie-eis (aanvulling op §"Unit tests"): test voor `save_record` met gesimuleerde daemon-timeout waar daemon *wel* upsertte — verwacht: ghost wordt automatisch opgeruimd en exception bubblet door.

### Pre-commit hook

`scripts/pre-commit-records-parity.sh`:

```bash
#!/usr/bin/env bash
if git diff --cached --name-only | grep -q "^data/concepten/records/"; then
  python3 -m tools.lib.records_api audit || exit 1
fi
```

`records_api.py audit` CLI-mode draait `audit_parity()`. Exit 0 als ok=True, exit 1 met ghost/missing-rapport anders.

Hook installeert via `scripts/install-hooks.sh` (nieuw bestand) of een Husky-equivalent. Override met `git commit --no-verify` blijft mogelijk voor noodgevallen — wordt niet aangemoedigd.

### Refactor-scope: 9 schrijvers

Elk script dat momenteel naar `data/concepten/records/` schrijft moet de API gebruiken:

| Script | Huidig gedrag | Na refactor |
|---|---|---|
| ~~`tools/extractie/auto_merge.py`~~ | ~~`Path.write_text(json.dumps(record))`~~ | **verwijderd 2026-05-18** (ADR-008 §18) |
| ~~`tools/extractie/enrich_records.py`~~ | ~~idem~~ | **verwijderd 2026-05-18** (ADR-008 §18) |
| `tools/extractie/verify_records.py` | leest alleen, schrijft niet → controleren | (no-op indien klopt) |
| `tools/extractie/index_concept_incremental.py` | leest record + daemon call | **verwijderd**; bulk-reindex via `records_api` CLI (`audit --fix`, `reindex-all`) |
| `tools/etl/mark_stale.py` | mute records (stale-flag) | `records_api.save_record(updated)` |
| `tools/etl/remove_bron.py` | scrubt bron-refs in records | `records_api.save_record(updated)` per gemuteerd record |
| `tools/leermateriaal/propose_competenties.py` | schrijft naar `competenties/*.yaml` — **andere collectie** | buiten scope (zie out-of-scope) |
| `tools/leermateriaal/lib/frontmatter.py` | helper voor rendering | controleren of écht een writer |
| `tools/rag/rag_index.py` | schrijft naar `bronnen`-collection, niet `concepten` | buiten scope |

Sonnet-agent zal per script vaststellen welke writers daadwerkelijk records muteren en welke false positives zijn.

### Bulk-operaties

`save_record` is veilig in een loop (daemon-call is ~50ms). De CLI van `records_api.py` voorziet:

- `reindex-all` — loop alle disk-records, `save_record` per stuk (vervangt `index_concept_incremental.py --alle`)
- `reindex` `<id>` — één record opnieuw indexeren

Optioneel later: `save_records_batch(records)` die de daemon één keer aanroept met meerdere records. Niet vereist in v1.

### Pre-commit hook gedrag — strict

Hook is **blokkerend** bij elke drift (geen lenient-modus, geen override-vlag op hook-niveau). `git commit --no-verify` blijft de enige ontsnapping en geldt als expliciete keuze van de gebruiker. Reden: lenient zou stilletjes drift toelaten — exact de fout die we vandaag aan het herstellen zijn.

### Failure modes

| Scenario | Detectie | Reactie |
|---|---|---|
| Daemon niet bereikbaar | `requests.ConnectionError` bij `/index-concept` | Raise `DaemonUnavailableError` — geen disk-write |
| Daemon-call traag (>10s) | timeout | Raise — caller moet retry beslissen |
| Daemon 500 bij upsert | non-200 response | Raise + log; geen disk-write |
| Disk write faalt na geslaagde RAG-upsert | OSError op write | Daemon `/delete-concept` om te rollbacken + raise |
| `rename_record` met new_id == old_id | sanity-check | Raise `ValueError` |
| `delete_record` voor onbestaande id | check disk + RAG vooraf | Raise `KeyError` |

## Gevolgen

- **Nieuwe bestanden**:
  - `tools/lib/records_api.py` — de API + CLI (`audit`, `audit --fix`, `reindex-all`, `reindex <id>`)
  - `tests/test_records_api.py` — unit tests (zie sectie hierboven)
  - `scripts/pre-commit-records-parity.sh` — git hook (strict, inclusief content-drift check)
  - `scripts/install-hooks.sh` — installer voor de hook
- **Verwijderde bestanden**:
  - `tools/extractie/index_concept_incremental.py` — gefunctioneerd door records-API
  - Verwijzingen in CLAUDE.md, docs/, andere scripts → updaten in dezelfde commit (CLAUDE.md regel 9)
- **Aanpassingen daemon (ADR-018)**:
  - `POST /delete-concept` endpoint toevoegen aan `tools/extractie/embedding_daemon.py`
  - `tools/lib/embedding_client.py` krijgt `delete_concept(id, chroma_path)` helper
- **Refactor**: 9 schrijvers (zie tabel) — Sonnet-agent kan dit in één pass met grep-driven scope-validatie
- **Niet geraakt**:
  - `bronnen`-collection (eigen exclusive writer in `rag_index.py`)
  - `competenties/*.yaml` (eigen schema, eigen collection wanneer first-class, andere ADR)
  - `leerpaden/*.yaml` (idem)
  - Daemon's bestaande endpoints
- **Initialisatie**:
  - Eenmalige `records_api audit --fix` na rollout om eventuele resterende drift op te ruimen
  - Hook activeert vanaf installatie; bestaande commits worden niet retroactief geverifieerd

### Unit tests

`tests/test_records_api.py` met minimaal:

- **Happy path per operatie**: `save_record` (nieuwe id én bestaande id), `rename_record`, `delete_record` — disk én RAG-state checken na elke call
- **Atomiciteit**: gesimuleerde daemon-fail bij `save_record` → geen disk-residu; gesimuleerde disk-fail na geslaagde daemon-call → RAG rolt terug
- **Audit-parity**: kunstmatig geïntroduceerde ghost en missing → `audit_parity` rapporteert ze correct
- **Edge cases**: `rename_record` met new_id == old_id → `ValueError`; `delete_record` op onbestaande id → `KeyError`; concurrente save's serialiseren correct (regression-test op daemon-lock)
- **CLI-modi**: `audit` exit-code 0/1, `reindex-all` raakt alle disk-ids
- **Content-sync**: `save_record` triggert render (mock render-functie, check call); `delete_record` ruimt markdown op; `rename_record` ruimt oude markdown op en maakt nieuwe aan; render-fout faalt `save_record` NIET (enkel warning); `audit_parity` detecteert content-drift (ontbrekende en extra markdown)

Fixture-strategie: aparte test-ChromaDB onder `tmp_path`, daemon gemockt via `monkeypatch` of een lichte fake-server. Render-functie gemockt via `monkeypatch` om te vermijden dat Jinja2-templates nodig zijn in unit-tests. Tests mogen niet afhankelijk zijn van de live LaunchAgent-daemon.

### Verificatie na rollout

1. `python3 -m tools.lib.records_api audit` → 0 ghosts, 0 missing, 0 content_ontbreekt, 0 content_extra
2. `pytest tests/test_records_api.py` → groen
3. Pre-commit hook detecteert handmatig geïntroduceerde drift (test door directe `rm` van een record-file zonder API)
4. Geen `Path.write_text` of `json.dump` calls meer op `data/concepten/records/` paden in de codebase (grep-check)
5. `tools/extractie/index_concept_incremental.py` is `git rm`'d en geen verwijzingen meer in scripts of docs (grep-check)
6. Smoke: `save_record` op een bestaand record → markdown in `content/concepten/` wordt opnieuw geschreven (check via mtime of diff)

## Out-of-scope

- **Competenties + leerpaden**: schrijfdiscipline voor `data/concepten/competenties/*.yaml` en `data/concepten/leerpaden/*.yaml` komt mee wanneer competenties first-class burgers worden (toekomstig ADR, vermoedelijk ADR-020 of -021). Tot dan blijven die met hun huidige writers (`propose_competenties.py`, `propose_leerpad.py`).
- **Bronnen-collection**: heeft al exclusieve writer in `rag_index.py`. Geen drift-probleem gemeten.
- **Concurrency tussen meerdere terminals/worktrees**: daemon serialiseert al via `_operatie_lock` (ADR-018). API erft die garantie.
- **Schema-validatie van records**: out-of-scope — records-API checkt id-consistentie, niet schema-conformiteit. Dat is werk van VERIFY (ADR-008 §13.2).
- **Migratie van bestaande prefix-ghosts**: al uitgevoerd op 2026-05-17 (zie commit-context). Niet meer relevant voor implementatie.
