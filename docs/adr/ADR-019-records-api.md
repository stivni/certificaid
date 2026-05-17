# ADR-019: Centrale records-API + RAG-parity discipline

**Status**: Draft
**Datum**: 2026-05-17
**Verwante ADRs**: ADR-018 (embedding-daemon — schrijft naar `concepten`-collection), ADR-008 (concept-extractie — bevat 7 van de 9 huidige schrijvers), ADR-007 (conceptmodel — schema dat geschreven wordt)

## Context

Concept-records leven op twee plekken tegelijk: op disk in `data/concepten/records/*.json` én geïndexeerd in de `concepten`-collection van `data/rag/main` (ADR-006, ADR-018). Beide zijn nodig — disk is source-of-truth, RAG is de doorzoekbare projectie die SYNTHESIZE / VERIFY / tutor gebruiken voor globale record-awareness.

Vandaag schrijven **negen scripts** naar disk zonder centrale RAG-discipline:

- `tools/leermateriaal/propose_competenties.py`
- `tools/leermateriaal/lib/frontmatter.py`
- `tools/etl/remove_bron.py`
- `tools/etl/mark_stale.py`
- `tools/extractie/enrich_records.py`
- `tools/extractie/auto_merge.py`
- `tools/extractie/verify_records.py`
- `tools/extractie/index_concept_incremental.py` (wel met daemon-call)
- `tools/rag/rag_index.py`

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

1. **save_record**: daemon `/index-concept` → 200 OK → disk write. Disk-write-fout → daemon `/delete-concept` om RAG terug consistent te krijgen + raise.
2. **rename_record**: daemon `/delete-concept(old_id)` → daemon `/index-concept(new)` → disk delete oud + write nieuw. Bij stap 2 of 3 falen: rollback van eerder gelukte stappen + raise.
3. **delete_record**: disk delete → daemon `/delete-concept`. Bij stap 2 falen: log loud (state nu wel consistent: niets op disk, oude entry nog in RAG — zal opnieuw kunnen worden weggehaald).

Daemon-uitbreiding nodig (ADR-018): nieuw endpoint `POST /delete-concept {id, chroma_path}`. Serialiseert via dezelfde `_operatie_lock` als `/index-concept`.

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
| `tools/extractie/auto_merge.py` | `Path.write_text(json.dumps(record))` | `records_api.save_record(record)` |
| `tools/extractie/enrich_records.py` | idem | idem |
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
  - `scripts/pre-commit-records-parity.sh` — git hook (strict)
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

Fixture-strategie: aparte test-ChromaDB onder `tmp_path`, daemon gemockt via `monkeypatch` of een lichte fake-server. Tests mogen niet afhankelijk zijn van de live LaunchAgent-daemon.

### Verificatie na rollout

1. `python3 -m tools.lib.records_api audit` → 0 ghosts, 0 missing
2. `pytest tests/test_records_api.py` → groen
3. Pre-commit hook detecteert handmatig geïntroduceerde drift (test door directe `rm` van een record-file zonder API)
4. Geen `Path.write_text` of `json.dump` calls meer op `data/concepten/records/` paden in de codebase (grep-check)
5. `tools/extractie/index_concept_incremental.py` is `git rm`'d en geen verwijzingen meer in scripts of docs (grep-check)

## Out-of-scope

- **Competenties + leerpaden**: schrijfdiscipline voor `data/concepten/competenties/*.yaml` en `data/concepten/leerpaden/*.yaml` komt mee wanneer competenties first-class burgers worden (toekomstig ADR, vermoedelijk ADR-020 of -021). Tot dan blijven die met hun huidige writers (`propose_competenties.py`, `propose_leerpad.py`).
- **Bronnen-collection**: heeft al exclusieve writer in `rag_index.py`. Geen drift-probleem gemeten.
- **Concurrency tussen meerdere terminals/worktrees**: daemon serialiseert al via `_operatie_lock` (ADR-018). API erft die garantie.
- **Schema-validatie van records**: out-of-scope — records-API checkt id-consistentie, niet schema-conformiteit. Dat is werk van VERIFY (ADR-008 §13.2).
- **Migratie van bestaande prefix-ghosts**: al uitgevoerd op 2026-05-17 (zie commit-context). Niet meer relevant voor implementatie.
