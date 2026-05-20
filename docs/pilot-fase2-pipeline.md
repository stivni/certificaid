# Pilot Fase 2 — Schema 2.0 herextract-pipeline

**Status**: werkdocument (geen ADR)
**Verband**: ADR-025 (schema 2.0), EXTRACT v5, VERIFY v3
**Doel**: pilot-run om EXTRACT v5 + schema 2.0 te valideren op echte concept-volumes binnen 24–36 u

---

## Doel & succescriteria

**Doel**: 460+ bestaande records herextract'en in schema 2.0 met behoud van inhoudelijke kennis + opvulling van didactische tekortkomingen (rol × perspectief · economische substantie · kader-cross-links).

**Succescriteria pilot**:
- 30–50 records geherextract op één PO als referentie
- ≥ 80 % van records voldoet aan kind-completeness (VERIFY)
- ≤ 15 % hallucinatie-risico (VERIFY bron-validatie)
- Geen catastrofale data-loss (oude records gearchiveerd, herstelbaar)
- Mens-in-de-loop steekproef bevestigt kwaliteits-stijging t.o.v. 1.6

**Succescriteria Fase 2 volledig**:
- Alle 460+ records in 2.0
- Kader-fiches voor 5–8 belangrijke domeinen (jaarrekeninganalyse, uitkering, financiering, …)
- Familie-fiches waar gepast
- ≥ 80 % kind-completeness over alle records
- Cross-PO-completeness: geen record dat "fiscaal volgt later" zegt

---

## Pre-pilot voorbereiding

### Foundations check (eenmalig, klaar in 2026-05-21)

- [x] ADR-025 spec
- [x] EXTRACT v5 prompt
- [x] VERIFY v3 prompt
- [x] Skeleton-voorstel prompt voor stap 0 (`prompts/skeleton-voorstel-v1.md`)
- [x] 8 mockup-referentie-fiches in `content/experiment/`
- [x] Archief-mechanisme (`tools/extractie/archive_voor_migratie.py`)
- [ ] Bronnen-werk: cijferzakboekje + extra fiscale bronnen (parallel, jouw werk)
- ~~Records-API soft-validator~~ — geschrapt; VERIFY-pass volstaat

## Stap 0 — Skeleton-voorstel (pre-pilot)

Vóór elke wave: een Opus-subagent draait `prompts/skeleton-voorstel-v1.md` op de PO.

Input voor de agent:
- alle v1.x-records met `linked_anchors[]` op de PO
- `data/programma/anchors.json` (TDKs voor de PO)
- referentie-mockups uit `content/experiment/`

**Geen examen-vragen** — niet als input voor extract noch voor stap-0-consolidatie
(conceptlaag is tijdloos en domein-onafhankelijk; examenvragen mogen geen
extract-keuzes sturen). Zie regel in EXTRACT v5 §16.

Output: markdown-rapport in `data/extractie/<PO>/skeleton-voorstel-<timestamp>.md` met:
- Inventaris bestaande records + voorstel-kind per record
- Voorgestelde 2.0-fiche-clusters (welke v1.x-records samenvatten tot welke 2.0-fiche)
- Voorgestelde nieuwe kader/regime-fiches
- Records die verdwijnen of mergen
- TDK-dekking-check
- Open vragen voor menselijke review

**Mens-in-de-loop**: jij reviewt het voorstel vóór herextract start. Aanpassingen via commentaar terug naar de agent of direct in het rapport.

Geschatte tijd: 10-20 min Opus-tijd per PO. Eénmalige scan; herhalen alleen bij wezenlijke wijziging.

### Wave-planning per PO

Volgorde voor pilot (kleine controleerbare batch eerst):

1. **Wave 0 (pilot)**: PO 1.1 — kern boekhoudkundige operaties (~30–50 records)
2. **Wave 1**: PO 1.x — andere boekhoud-gerichte PO's
3. **Wave 2**: PO 2.x — fiscaliteit
4. **Wave 3**: PO 3.x — vennootschapsrecht
5. **Wave 4**: PO 4.x — audit
6. **Wave 5+**: overige PO's
7. **Wave laatste**: kader- en familie-fiches die over alle waves heen relevant zijn

**Cross-PO-completeness**: per record worden ALLE relevante PO's in één extract afgehandeld. Bv. obligatielening (gestart in wave 0 voor PO 1.1) krijgt meteen ook fiscale + audit perspectieven mee.

---

## Pilot run — Wave 0

### Stap 1 — Archivering

```bash
# Dry-run om te zien wat gekopieerd zou worden
python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1 --dry-run

# Echte archivering
python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1
```

Records worden **gekopieerd** (niet verplaatst) naar
`data/concepten/_archive/v2.0-migratie/<timestamp>-po-1.1/`. Originelen blijven
in `data/concepten/records/`; Quartz blijft renderen op de huidige content.
Pas wanneer `save_record()` een 2.0-versie schrijft, overschrijft het de oude
markdown atomair.

### Stap 2 — Subagent-fleet met lock-based parallelisatie

**Parallelisatie zonder overlap** — orchestrator wijst elk **2.0-fiche-doel** (uit
het skeleton-voorstel) toe aan precies één Opus-subagent. Bij ~30-50 doel-fiches
voor PO 1.1 → ~6-10 subagents tegelijk, elk 4-5 fiches.

**Lock-discipline**:
- Orchestrator pakt de fiche-lijst uit het skeleton-voorstel
- Wijst elke fiche aan precies één agent toe (agent A doet `obligatielening`,
  agent B doet `inkoop-eigen-aandelen-nv`, …)
- Geen twee agents werken aan hetzelfde 2.0-fiche-doel
- **Cross-PO-completeness binnen agent**: agent die `obligatielening` doet,
  behandelt alle perspectieven (boekhoudkundig + fiscaal + audit) ongeacht in welke
  PO-wave we zitten — zo gebeurt het in één pass, niet "fiscaal later"
- **First-write-wins voor nieuwe records**: als agent X tijdens extract een
  ontbrekend record signaleert dat agent Y ook nodig heeft → agent X maakt het,
  Y leest de versie van X via concept-RAG bij eigen extract
- Eventuele overlap-rommel → opgelost in Fase 3 (refinement) via VERIFY-suggesties

**Orchestrator-prompt** (sketch):
```
Je orchestreert een parallelle herextract-wave voor PO X.

Input: skeleton-voorstel rapport (lijst van 2.0-fiches te schrijven).

Verdeel de fiches over N subagents (4-5 per agent). Per agent:
- prompts/concept-extractie-v5.md als systeem-instructie
- minstens 3 referentie-mockups uit content/experiment/ (kind-specifiek)
- De toegewezen fiches + alle archief-records die er onderdeel van worden
- Anchors + RAG-access

Wijs nooit hetzelfde fiche aan twee agents toe. Volgorde: kader/regime-fiches
eerst (zodat instrument-fiches er edges naar kunnen leggen), dan instrumenten
en operaties, dan ratio's.

Resultaat: nieuwe 2.0-records via records-API geschreven.
```

**Subagent-prompt per batch**:
```
Lees prompts/concept-extractie-v5.md voor volledige instructies + de drie
referentie-fiches uit content/experiment/.

Schrijf deze 2.0-fiches:
- doelfiche-A (kind: instrument, samenvatting van archief-records X, Y, Z)
- doelfiche-B (kind: operatie, samenvatting van W)
- ...

Voor elk: lees archief-records als seed, raadpleeg RAG voor extra bronnen,
volg top-volgorde + rol × perspectief, schrijf via save_record. Geen
overlap met je collega-agents (vooraf afgebakende fiche-lijst).
```

### Stap 2.5 — Orphan-cleanup na wave-approval

Na elke wave:
1. Mens-in-de-loop steekproef (zie stap 4) → wave goedgekeurd
2. Identificeer **orphan v1.x-records**: records die in archief zitten maar geen 2.0-doel hebben (geen overschrijvende `save_record` van een nieuwe versie)
3. Voor elke orphan: `delete_record(record_id)` via records-API — schoont disk + RAG + markdown
4. Archief blijft (snapshot vóór wave); orphans zijn alleen weg uit de live-set

```bash
# Helper-script (te bouwen):
python3 -m tools.extractie.cleanup_orphans \
  --archief data/concepten/_archive/v2.0-migratie/20260521T140000Z-po-1.1 \
  --dry-run

# Echte cleanup (na approval):
python3 -m tools.extractie.cleanup_orphans \
  --archief data/concepten/_archive/v2.0-migratie/20260521T140000Z-po-1.1
```

Vergelijkt archief-snapshot vs huidige `data/concepten/records/`; alles in archief wat niet meer als 2.0-versie bestaat = orphan.

### Stap 3 — VERIFY-pass (na elke wave)

```bash
python3 -m tools.extractie.verify --prompt prompts/concept-verify-v3.md \
  --records "1.1.*" \
  --rapport-out data/extractie/verify-reports/wave-0-rapport.md
```

VERIFY draait soft — schrijft suggesties naar `gaps.json` en het rapport. Geen blocker.

### Stap 4 — Steekproef-review (mens-in-de-loop)

10 % van records (5 uit 50): handmatig lezen in Quartz-render, vergelijken met archief-versie.

Vragen voor de review:
1. Is de nieuwe versie didactisch sterker?
2. Bevat ze alle inhoud van de oude versie (geen verlies)?
3. Past de rol × perspectief structuur?
4. Werken de cross-record-edges?
5. Welke patronen zie ik dat naar prompt-aanpassing wijzen?

### Stap 5 — Beslismoment

Na pilot:
- ✅ Doorgaan met Wave 1: criteria gehaald, prompt OK
- 🔁 Prompt-aanpassing: enkele iteraties op EXTRACT v5 + opnieuw pilot
- ❌ Schema-revisie: pilot onthult fundamentele tekortkoming → ADR-025 bijwerken

---

## Volledige Fase 2 — schaling

### Parallelle waves

Na succesvolle pilot:
- Waves 1–5 kunnen **parallel** lopen — verschillende PO's, verschillende subagent-fleets
- Cross-PO-completeness garandeert dat records in één wave volledig zijn

Voorbeeld: bij 8 concurrent waves van 50 records elk → 400 records in één nacht-batch. Per record gemiddeld ~10 min Opus-tijd → totaal 67 u Opus-tijd, parallel verdeeld over 8 fleets → ~8 u wandklok.

### VERIFY tussendoor

VERIFY draait per wave automatisch — bevindingen accumuleren in `gaps.json` voor latere refining-passes (Fase 3).

### Bronnen-stroom (parallel)

Jouw bronnen-werk (Cijferzakboekje + extra fiscale bronnen) loopt parallel:
- Nieuwe bronnen → tools/etl pipeline → RAG-index update
- Records met `te_verifieren`-claims op nieuwe bronnen kunnen via VERIFY ge-upgrade worden naar `grounded`
- Dit gebeurt in Fase 3 (refinement), niet in Fase 2 (initial extract)

---

## Fase 3 — refinement

Na Fase 2: een refinement-loop met o.a. een **mechanische claim-validatie-pass**.

### Mechanische ⚠️ → ⚖️ upgrade-pass

Schema 2.0 maakt elke claim **structured queryable**: elk element heeft
`confidence` + `bron` + claim-tekst. Een refinement-script kan systematisch:

1. Alle records doorlopen
2. Per element met `confidence: te_verifieren`: gericht RAG-query op de claim-tekst tegen de huidige bronnen-RAG (incl. nieuw toegevoegde bronnen)
3. Indien match met voldoende score → `confidence: grounded` + `bron`-veld invullen
4. Indien geen match → blijft ⚠️, logt naar `gaps.json` als "bronnen-werk nodig voor concrete claim X"

Concreet helper-script `tools/extractie/herevalueer_te_verifieren.py` te bouwen
zodra Fase 2-output beschikbaar is.

Voordeel: jij voegt fiscale bronnen toe → script upgrade automatisch
relevante claims zonder mens-in-de-loop per claim.

### Overige refinement-acties

- VERIFY-suggesties verwerken (bv. `voorbeeld_ontbreekt` → bijwerken)
- Hallucinatie-risico claims onderzoeken (gerichte sub-pass)
- Cross-record edges aanvullen (`verward_met`-pairs symmetrisch maken)
- Kader- en familie-fiches verbeteren met inzichten uit specifieke leden
- Wave-stitching: records die in twee waves zijn aangeraakt → consolideer naar
  één canonical versie

Geen tijdsdoel; doorlopend werk.

---

## Renderlaag — parallel aan Fase 2

Quartz-component-update gebeurt parallel aan extract:
- Collapsible secties (default open: 1-2-3-4; default dicht: 7-8-9-10)
- Element-vocabulaire-renderers (boeking · balans-snapshot · t-rekening · …)
- Rol × perspectief layout (accordeon of matrix-grid)
- Familie-recursie-component (uitvouwbare boom)
- Browser-state-persistentie voor confidence-keuze (jouw "vrouw-confidence"-idee — default dicht voor non-essentiële, opt-in voor diepere lezing)

Geen blokkering voor extract — markdown-render werkt al; collapsible is verfijning bovenop.

---

## Risico's & mitigatie

| Risico | Mitigatie |
|---|---|
| Data-loss bij herextract | Oude records in `_archive/`; herstelbaar |
| Tijdsdruk Fase 2 | Parallelle subagent-fleet; cross-PO-completeness per record |
| Kwaliteits-regressie | VERIFY soft-pass + mens-in-de-loop steekproef |
| Records-API timeout bij batch | Existing cold-start-mitigatie (60 s eerste call); subagents zelf via worktree-discipline |
| Hallucinatie in 🧭-claims | VERIFY hallucinatie-detectie; 🧭-gradatie-regel in prompt |
| Kader-fiche-cyclus (afhankelijkheden) | Pre-EXTRACT scan; orchestrator beslist kader-eerst-volgorde |

---

## Open punten

- Records-API soft-validator-implementatie: uit te voeren in Python (`tools/lib/records_api.py` — `_valideer_schema_versie` helper)
- Archief-pad-conventie: `data/concepten/_archive/v1.x/po-XX/` of plat? Voorlopig plat.
- Hoe bewaren we `_provenance.verify_overrides`-history over meerdere passes? Append-only lijst.
- Render-component-spec: aparte werkdoc bij Quartz-update.

---

## Eerste acties (vandaag)

1. ADR-025 + prompts gepushed → klaar
2. Bronnen-werk (jij) parallel starten
3. Archief-mechanisme (`tools/extractie/archive_voor_migratie.py`) → klaar
4. Skeleton-voorstel-prompt (`prompts/skeleton-voorstel-v1.md`) → klaar
5. **Stap 0 op PO 1.1**: skeleton-voorstel laten draaien voor review → in te plannen
6. **Wave 0 launchen** zodra skeleton-voorstel akkoord → in te plannen
