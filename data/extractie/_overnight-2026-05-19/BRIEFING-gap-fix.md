# Briefing — overnight gap-fix sessie 2026-05-19

**Lees dit eerst volledig voor je begint.**

## Context

Het PO 1.x werk is inhoudelijk af (463 records, schema 1.6, EXTRACT v4 operationeel). Maar er staan nog 225 gaps over PO 1.x: 82 open + 143 archived-strategic-pass. De gebruiker wil dat we deze nacht zoveel mogelijk wegwerken voor het ITAA-examen (deadline eind mei).

Jij krijgt **één** programmaonderdeel toegewezen. Je gap-batch staat in:

```
/Users/stivni/Documents/ITAA/certificaid/data/extractie/_overnight-2026-05-19/gap-batch-PO-<X.Y>.json
```

## Werkprotocol

### 0. CWD-discipline (CRITICAL — anders verlies je werk)

Je draait waarschijnlijk in een git-worktree. **Eerste actie altijd**:

```bash
cd /Users/stivni/Documents/ITAA/certificaid
```

en daarna voor elke records-API-call of file-write:

```python
import os
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
```

Voor `gaps.json` en de overnight-folder: gebruik **altijd absolute paden** vanaf `/Users/stivni/Documents/ITAA/certificaid/...`. Geen relatieve paden, ooit.

### 1. Lees de regels

- [`/Users/stivni/Documents/ITAA/certificaid/prompts/concept-extractie-v4.md`](prompts/concept-extractie-v4.md) — volledige EXTRACT v4-prompt incl. records-API protocol
- [`/Users/stivni/Documents/ITAA/certificaid/docs/concept-schrijfregels.md`](docs/concept-schrijfregels.md) — inhoudelijke conventies
- CLAUDE.md regels (zie repo-root) — vooral regel 1, 2, 8, 9
- ADR-007 (concept-schema 1.6), ADR-008 (architectuur), ADR-019 (records-API)

### 2. Schrijf nooit direct naar `data/concepten/records/`

Gebruik **uitsluitend** `tools/lib/records_api.py`:

```python
import os
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
from tools.lib.records_api import save_record, rename_record, delete_record

# Nieuw of bijgewerkt record:
save_record({
    'id': 'voorbeeld-record',
    'naam': '...',
    # ... volledige schema 1.6 fields
})
```

Reads via records-API helpers blijven daemon-canoniek (RAG).

### 3. Per-gap-protocol

Voor elke gap in je batch:

1. **Beoordeel** of de gap nog actueel is. Records kunnen al gewijzigd zijn sinds de gap werd genoteerd. Lees het record en de reden.
2. **Categoriseer**: kun je hem in deze sessie wegwerken, of niet?
3. **Beslis** en voer uit:
   - **Resolved**: pas record(s) aan via `save_record`, of voeg ontbrekende record toe.
   - **Won't-fix**: motiveer waarom (bv. vereist bron die niet beschikbaar is, of niet examenrelevant). Markeer als won't-fix.
   - **Bewaren-voor-later**: gap blijft staan, geen actie nodig.
4. **Log** je actie in het per-PO update-bestand (zie §4).

### 4. Gap-status-update protocol (per-PO, geen conflicten)

**Schrijf NIET direct in `gaps.json`** — dat kan andere parallelle agents data-loss bezorgen.

Schrijf je status-updates naar:

```
/Users/stivni/Documents/ITAA/certificaid/data/extractie/_overnight-2026-05-19/gap-updates-PO-<X.Y>.json
```

Formaat:

```json
{
  "programmaonderdeel": "1.5",
  "agent_run_id": "overnight-gap-fix-PO-1.5-2026-05-19",
  "afgerond_op": "2026-05-19T...",
  "updates": [
    {
      "match_op": {
        "record_id": "consolidatieverplichting",
        "aspect": "vergelijkingsparen.target-ontbreekt",
        "geconstateerd_op": "2026-05-15T14:10:18+00:00"
      },
      "nieuwe_status": "resolved",
      "applied_door": "overnight-gap-fix-PO-1.5-2026-05-19",
      "toelichting": "Target-record 'groottecriteria' aangemaakt; vergelijkingspaar werkt nu."
    }
  ],
  "nieuwe_gaps": [],
  "samenvatting": "32 open gaps behandeld: 28 resolved, 3 won't-fix, 1 bewaard. 4 nieuwe records aangemaakt."
}
```

Match-op-velden moeten **uniek** matchen op een entry in `gaps.json`. Bij twijfel: meer velden meegeven (status, prio, reden-prefix).

### 5. Scope-discipline

- **Blijf binnen jouw PO.** Cross-PO records mag je touchen als ze direct nodig zijn voor jouw gap, maar verbreed niet zelf naar buren-PO's.
- **Maak geen nieuwe ontwerpkeuzes** (CLAUDE.md regel 6 — werk-modus). Bij design-onduidelijkheid: log een nieuwe gap en ga door.

### 6. Quality bar

- Geen wetsinhoud zonder bronverwijzing (`⚖️` grounded vs `🤖` inferred).
- Onzeker? `⚠️ te verifiëren` of leeg laten.
- Volledige namen (geen afkortingen) — `programmaonderdeel`, `kenniselement`, etc.

### 7. Eindrapport

Stuur terug:
- Aantallen: open behandeld, won't-fix, bewaard, nieuwe records, hernoemde records, nieuwe gaps gelogd.
- Lijst van nieuwe records (id + node_type).
- Bekende open punten die je niet kon oplossen + waarom.
- Onder 800 woorden.

### 8. Geen commits

Laat alle git-werk aan de orchestrator. Schrijf alleen de records (via API) en je update-bestand.

---

**Veel succes. Houd de cwd-discipline streng — dat is de #1 bron van data-loss in deze pipeline.**
