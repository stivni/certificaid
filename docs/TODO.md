# TODO — Certificaid roadmap

_Centrale inhoudsopgave van openstaand werk, geordend per afhankelijkheid._
_Voor de gedetailleerde issues: zie de gelinkte bronbestanden — dit document
houdt het overzicht, geen content-duplicatie._

**Laatste update**: 2026-05-18 (na schema 1.5-rollout + EXTRACT v4-pilots op PO 1.5)

## Logica van de volgorde

```
1. Infrastructuur (records-API + matches-store + content-sync)  [klaar]
   ↓
2. Schema 1.5 + EXTRACT v4-prompt                                [klaar]
   ↓
3. PO 1.x content-review via EXTRACT v4 + VERIFY-feedback-loop  [in uitvoering: PO 1.5 wave 1]
   ↓
4. Bronnen-laag uitbreiden (1.1 ETL-fix + 1.2 fiscale gidsen)   [pending]
   ↓
5. Andere PO's uitrollen (3.0, 4.0, 2.x)                         [pending]
   ↓
6. Render-laag-revisie (ADR-010): minicursus als primair         [pending]
```

---

## Fase 1 — Infrastructuur (klaar — 2026-05-18)

✅ **records-API** (ADR-019) — atomair disk + concept-RAG + content-fiche-render. Pre-commit parity-hook. 35 tests groen.
- Cold-start timeout (60s eerste call) + ghost-recovery + orphan-management
- Idempotent daemon-endpoints documented

✅ **Matches-store** (ADR-005 §9.1) — `data/extractie/matches.sqlite3` met state-fingerprints (`chunk_sha`, `anchor_vector_hash`). Delta-driven matching ipv volledige N×M-rebuild.

✅ **Embedding-daemon** (ADR-018) — LaunchAgent met `/health`, `/index-concept`, `/delete-concept`, `/duplicate-check`, `/embed`, `/refresh` endpoints.

---

## Fase 2 — Schema 1.5 + EXTRACT v4 (klaar — 2026-05-18)

✅ **Schema 1.5** (ADR-007) — 6 node_types (`begrip` / `regel` / `cluster` / `synthese` / `autoriteit` / `competentie`), 7 canonieke edge-types, drie concretiserings-velden (`in_praktijk` / `voorbeelden` / `illustraties`) multi-niveau.

✅ **Migratie 1.4 → 1.5** — 345 records mechanisch gemigreerd (Phase A + A++). 85 competenties van YAML naar JSON-records. Totaal 430 records, alle schema 1.5.

✅ **EXTRACT v4-prompt** (`prompts/concept-extractie-v4.md`) — research-and-draft-agent met event-driven scope, gevalideerd via 6+ PO 1.5-pilots, 7+ patch-rondes (timeout-mitigatie, deprecated-edges, begrip-valkuilen, cijfer-consistentie, bron-verificatie, bestaansreden-test, reflectieve rijkheid, bron≠concept, multi-concept-smell, naming-conventie, impliciete-tegenhanger).

✅ **VERIFY-prompt** uitgebreid met bron-als-concept + bestaansreden-test + compositie-naam-smell checks.

✅ **concept-schrijfregels.md** geconsolideerd; `content-richtlijnen.md` uitgefaseerd.

---

## Fase 3 — PO 1.x content-review (in uitvoering, focus 1.5)

EXTRACT v4 per anchor, centraal-first strategie. Records-API met orphan-management (delete + rename auto-cascadeert edges).

### 3.1 — PO 1.5 wave 1 — Top-level anchors (centraal)

Status 2026-05-18:

- ✅ **1.5.I** — `richtlijn-2013-34-eu` (bron-record) → `eu-harmonisatie-jaarrekeningenrecht` (cluster, 5 bouwstenen). 5 records propageerden anchor.
- ✅ **1.5.II** — `ifrs-verordening-1606-2002` endorsement-criteria + ARC. *Pre-patches; eventueel revisit met latest patches.*
- ✅ **1.5.III** — `wijziging-boekhoudkundig-referentiestelsel` van procedure → cluster + hallucinatie-fix (delisting/jojo-claims verwijderd, scope tot statutair-only).
- 🔄 **1.5.IV** — consolidatie-overkoepelend, 10 records — *Opus-agent loopt (2026-05-18 namiddag)*
- ⏳ **1.5.V** — leasing-overkoepelend, 15 records
- ⏳ **1.5.taak.1** — PO-taak, 4 records

### 3.2 — PO 1.5 wave 2 — Sub-anchors

- ✅ **1.5.IV.B** — IAS 1 cleanup (pre-patches; eventueel revisit)
- ✅ **1.5.V.A** — impairment-IAS-36 stappen-structuur + illustraties
- ✅ **1.5.V.C** — leasing-ifrs regel → cluster (sale-and-leaseback record toegevoegd)
- ⏳ **1.5.IV.A** (1 record), **1.5.IV.C** (4 records, 1787-chunk bundle), **1.5.V.B**, **1.5.V.D**, **1.5.V.E**

### 3.3 — Revisit-pass voor pre-patches anchors

1.5.II + 1.5.III + 1.5.IV.B + 1.5.V.A + 1.5.V.C werden geëxtraheerd vóór de naming-conventie + reflectieve-rijkheid + impliciete-tegenhanger patches. Korte revisit om die toe te passen.

### 3.4 — Daarna PO 1.6 t/m 1.9

Idem strategie. Special case voor PO 1.6: `randvoorwaarden-controle` (huidig `voorgesteld:randvoorwaarden`) moet beslist worden — bouwsteen van `aanvaarden-audit-opdracht`-competentie of zelfstandige regel?

### 3.5 — Touch-up PO 1.1-1.4

Delta-rapport toont 135 HIGH-stale records in 1.1-1.4 (vooral 1.3 ratio-records met IFRS-9-bronnen). Lichter werk dan 1.5-1.9 omdat records al schema 1.4 deep-rewriten hadden, maar v4-prompt-bevindingen (bron-prefix, multi-concept-smell) moeten toegepast.

---

## Fase 4 — Bronnen-laag uitbreiden

Blokkeert sommige PO-rollouts. Niet kritisch voor PO 1.x.

### 4.1 — Wet-beroepskwalificaties-2008 — ETL-fix
- Issue: `Art. N_WAALS_GEWEST`-varianten splitsen één artikel in twee secties.
- Trigger voor: PO 4.0 (deontologie).

### 4.2 — 8 fiscale gidsen — ETL-fixes (needs-rework)
Narratieve type-3 PDFs, ETL-uitdagingen. Trigger voor: PO 2.1-2.8 (fiscaliteit, 8 PO's).

### 4.3 — Refresh-gate na elke trust-promotie (regel, al vastgelegd in ADR-005 §9.1)

---

## Fase 5 — Andere PO's uitrollen

Pas na Fase 3 + 4. Per PO: standaardproces via EXTRACT v4 per anchor.

### 5.1 — PO 3.0 — Vennootschapsrecht
Primaire bronnen al trusted (WVV + KB-WVV-2019). Niet blocked door Fase 4.

### 5.2 — PO 4.0 — Deontologie
Vereist Fase 4.1 (Wet-beroepskwalificaties). Primaire bronnen: IESBA-code + ITAA-normen (deels trusted).

### 5.3 — PO 2.1 t/m 2.8 — Fiscaliteit (8 PO's)
Vereist Fase 4.2 (8 fiscale gidsen). Volgorde binnen 2.x: nog te bepalen.

---

## Fase 6 — Render-laag-revisie (ADR-010)

Gepland, niet gestart. Doel: concept-fiches als **reference**, minicursus als **didactisch primair**. Schema 1.5-data (records + illustraties + voorbeelden + in_praktijk) is hier op afgestemd; render-laag moet volgen.

### 6.1 — Bidirectionele edge-weergave bij rendering
`A onderdeel-van B` → B-fiche toont *"bevat: A"*. Data-laag blijft één-richting; render leest beide kanten.

### 6.2 — Minicursus-architectuur als primair leerpad
Concept-fiches naar achtergrond. Minicursus voor leerflow, fiche voor opzoek-werk + tutor-RAG.

### 6.3 — Studiemateriaal-schrijfregels (apart doc)
Render-laag verdient eigen schrijfgids — concept-schrijfregels gaat over data-laag.

---

## Doorlopend — Onderhoud

### Bron-genaamde records (13 gesignaleerd, deels onderweg)
Geïdentificeerd 2026-05-18:
- ✅ `richtlijn-2013-34-eu` → `eu-harmonisatie-jaarrekeningenrecht` (1.5.I)
- ⏳ `ifrs-verordening-1606-2002` → split in `verplichte-ifrs-eu-beursgenoteerden` + `endorsement-procedure-eu`
- ⏳ `kb-wvv-uitvoering`, `wetboek-vennootschappen-verenigingen`, `wetboek-economisch-recht-boek-iii` — verspreiden over fenomenen
- ⏳ 6 `ias-1-*` records — prefix-removal (regel 11 v4-prompt)
- Andere `ias-*`, `ifrs-*`, `cbn-*` records — per-anchor evaluatie

### Multi-concept-smell records (27 gesignaleerd)
Meeste competenties met "X en Y"-naming. Per-anchor beoordelen of écht splits.

### 36 procedure-records — hercategorisatie
Phase A heeft `procedure`-type behouden voor case-by-case Phase B. Hercategoriseren naar `cluster` of `competentie` per EXTRACT-touch.

### `voorgesteld:randvoorwaarden` — 1 anomalie
Bij PO 1.6 EXTRACT beslissen: bouwsteen van `aanvaarden-audit-opdracht`-competentie of zelfstandige regel?

### ADR-017 bronnen-migratie (12/116 done)
Eenvormig extract-schema. Backlog: 104 bronnen. Long-running achtergrond.

### Backup-tags archeology (8+ tags)
Plus nieuwe: `backup/pre-schema-1.5-migration-2026-05-18`. Bij geen issue gedurende 30 dagen: tags verwijderbaar.

---

## Open ADR-punten

- **ADR-008 §13.2**: content-pattern-based VERIFY-checks (open punt sinds 2026-05-15)
- **ADR-008 §18.7** open punten: coordinator-pattern, sub-agent eigenaarschap voor verwijderingen, loop-limiet bij gap-events
- **ADR-010**: revisie pending — concept-fiches als reference, minicursus als primair
- **ADR-019**: `anchor_propagation_log` veld dat een 1.5.I-agent introduceerde — niet in schema 1.5 gedocumenteerd, te normaliseren

---

## Achtergrondinfo

- **Memory-snapshots**: `memory/project_*.md` per onderwerp. Update na grote mijlpalen.
- **Architectuur-fasering**: `docs/roadmap.md` toont architectuur-evolutie.
- **Pilot-rapporten**: `/tmp/extract-v4-*-rapport.md`, `/tmp/verify-rapport-2026-05-18.md`, `/tmp/fix-extract-feedback-2026-05-18.md`, `/tmp/competentie-migration-rapport.md`, `/tmp/gap-mining-rapport.md`

## Onderhoud van deze TODO

- Nieuwe taak: voeg toe aan correcte fase.
- Taak afgerond: streep door + commit, of verwijder bij definitief klaar.
- Bij grote sessie-shifts: actualiseer "laatste update" datum.
- Diepere details: link naar ADRs of pilot-rapporten — geen content-duplicatie.
