# Resume-handoff — pilot Wave 0a geparkeerd voor weekly-limit-reset

**Datum**: 2026-05-21 ~06:15 UTC
**Reden**: gebruiker hit weekly Claude-limit; reset in 1-2u
**Status**: skeleton-fase 100% klaar; pilot-extract niet gestart

---

## Wat klaar is

- **5 batches skeleton-voorstel-runs voltooid** — alle 19 PO's gedekt
- **Candidates-DB**: 425 kandidaten, 177 cross-PO (~42%), 0 gerealiseerd
- **19 PO-rapporten** in `data/extractie/<PO>/skeleton-voorstel-*.md`
- **Aggregaat-rapport**: `data/extractie/_global/skeleton-overzicht-20260521T034254Z.md`
- **Archieven v1.x** klaar voor pilot-PO's:
  - 1.1: 66 records (`data/concepten/_archive/v2.0-migratie/20260521T034538Z-po-1.1/`)
  - 1.3: 47 records (`...20260521T034544Z-po-1.3/`)
  - 2.3: 0 records (greenfield bevestigd voor dbi-aftrek)

## Wat NIET klaar is

- **Pilot Wave 0a-extract** — 6 fiches niet geschreven
- VERIFY-pass
- Orphan-cleanup

---

## Wat fout ging in deze sessie

### 3-agent parallelle pilot crashte stilzwijgend

3 Opus-agents (afe27f2d7bfe649e6, acc031a40aa9ae2c0, a6b3a754a5c78c474) gelijktijdig launched voor 2 fiches elk. Alle 3 stopten op **exact dezelfde seconde** (06:02:57) met JSONLs van 138-348 KB, **geen completion-notification**, **geen records op disk**, **geen DB-realisaties**.

**Vermoedelijke oorzaak**: parallel `zoek_bronnen(rerank=true)`-calls op bge-m3 (MPS) → cross-encoder-OOM of timeout in MCP-server. Cross-encoder rerank kost ~30 forward passes per call; 3 agents × meerdere parallelle calls = mogelijk te veel voor MPS-memory.

**Diagnostic-single-agent** (adea481f38d872ec7) toen gelaunched met defensieve defaults (rerank=false, time-box 25 min, 1 fiche). User hit weekly limit → agent gestopt na alleen kandidaat + mockup-read (minimal burn).

---

## Resume-plan voor volgende sessie

### Stap 1 — Pre-flight

```bash
# Verifieer MCP-server actief
# /mcp slash-command in CLI
# Health-check:
curl -s localhost:8765/health  # bge-m3 daemon
python3 -m tools.extractie.candidates_db stats  # bevestig 425/0
```

### Stap 2 — Pilot Wave 0a launch (defensief)

Launch **1 Opus-agent tegelijk, sequentieel**, met deze defaults:
- `rerank=false` als default voor `zoek_bronnen`; alleen rerank=true voor 1-2 final ⚖️-claims per fiche
- Time-box 25 min per fiche
- 1 fiche per agent (geen 2 — was te ambitieus)

Volgorde (uit aggregaat-rapport §7):

| # | Fiche | Kind | Primary | Bijzonderheid |
|---|---|---|---|---|
| 1 | `obligatielening` | instrument | 1.1 | Canonical mockup obligatielening-v7 |
| 2 | `oprichtingskosten` | balanspost | 1.1 | Balanspost-skelet POC |
| 3 | `solvabiliteitsratio` | ratio | 1.3 | Drempels + acties per rol |
| 4 | `jaarrekening` | kader | 1.1 | Meest cross-cutting (5 PO's) |
| 5 | `inkoop-eigen-aandelen` | operatie | 1.1 | Pair-trap-test (NV+BV één fiche) |
| 6 | `dbi-aftrek` | fiscale-regeling | 2.3 | **Gap-stress-test** (greenfield) |

**Aanpak A — Sequentieel (veilig)**: 1 agent, 1 fiche, wachten op completion, dan volgende. Schatting: 25 min × 6 = 2.5-3u wall-clock. Geeft schone diagnostic of single-agent stabiel is.

**Aanpak B — Parallel-2 (sneller, na bewezen single-agent)**: na succesvolle eerste fiche, launch 2 agents parallel met elk 1 fiche, alle defensieve defaults. Risico op MCP-stress kleiner dan 3 agents × 2 fiches.

**Aanbeveling**: start met aanpak A voor fiche 1 (obligatielening). Als die binnen ~20 min schrijft → schakel over op aanpak B voor 2+3, 4+5, dan 6 solo.

### Stap 3 — Per-agent prompt-template

Zie `data/extractie/_global/skeleton-overzicht-20260521T034254Z.md` §7 voor toewijzingen + de prompts die ik hier eerder formuleerde (laatste agent-call in deze conversatie heeft de schoonste defensieve versie — agent adea481f38d872ec7).

Kern-instructies per agent:
- Eerste stap: lees `prompts/concept-extractie-v5.md` volledig
- `rerank=false` default
- Time-box 25 min
- save_record via `tools/lib/records_api.py`
- `markeer_kandidaat_gerealiseerd(fiche_id=..., extract_wave_id='wave-0a-pilot-20260521')`
- Return-message: pad naar markdown + JSON, wall-clock, MCP-call-breakdown, ⚠️-percentage, errors

### Stap 4 — Fase 4 STOP voor mens (zoals oorspronkelijk plan)

Na 6 fiches: rapport in `data/extractie/_global/wave-0a-pilot-rapport-<ts>.md` + STOP voor mens-akkoord vóór bulk-extract.

---

## Bekende issues om mee te nemen

1. **MCP-bug `aanvul_kandidaat(veld='edge')`** — blokkeert; workaround = edges direct in `voorstel_kandidaat` of in record-frontmatter
2. **MCP-bug `voorgesteld_door_pos` wordt niet ge-extend** bij `aanvul_kandidaat`-calls
3. **Worktree-routing**: PO 1.6 ran in een Claude-worktree; rapport handmatig gekopieerd. Mogelijk speelt dit ook met andere agents — check `.claude/worktrees/` als rapporten niet vindbaar zijn
4. **MPS-rerank-overload**: parallelle `rerank=true` op bge-m3 lijkt onstabiel — vermijden in parallel-runs

---

## Task-tracker-status

| # | Status | Taak |
|---|---|---|
| 1-5 | ✅ completed | Skeleton batches 1-5 |
| 6 | ✅ completed | Fase 2: aggregaat-rapport |
| 7 | ⏸ pending | Fase 3: pilot Wave 0a (geparkeerd) |
| 8 | ⏸ pending | Fase 4: wave-0a pilot-rapport + STOP |

---

## Belangrijk: vóór resume

- Controleer dat MCP-server `certificaid-rag` nog actief is (mogelijk preload nog warm)
- Lees dit document + `data/extractie/_global/skeleton-overzicht-20260521T034254Z.md`
- Geen `git commit` nodig vóór resume — alle artefacten staan op disk
