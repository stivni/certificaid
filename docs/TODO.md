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

### 3.4b — Examenvragen-classificatie uitbreiden (BLOKKEERT VERIFY Check A)

Status 2026-05-18: `_programmaonderdeel_classificatie.json` bevat **70 vragen** — 5 oude PO 1.4-seed entries + 65 BIBF-entries (28 uit 2003-bibf + 37 uit 2008-bibf, ingelopen 2026-05-18). De ~180 ITAA-vragen uit 2013-1/2/2014-1/2015-1/2024-1 blijven onverklassificeerd. Onze 5 EXTRACT v4-passes op PO 1.5 hadden dus **geen examen-vraag-input** bij VERIFY Check A — Check werd silently geskipt.

7 examen-PDFs zijn nu verwerkt (`data/programma/examen_vragen/<jaar>-N.json`, inclusief 2003-bibf + 2008-bibf). Wat ontbreekt:

1. **Classificatie-subagent draaien** (instructies in `_classificatie-instructies.md`) om elke ITAA-vraag aan een PO te koppelen. Verwacht: ~180 extra classifications voor PO 1.1-1.9 + 2.x + 3.x + 4.0. De BIBF-vragen zijn al deterministisch geclassificeerd (zie de 65 entries met `vraag_id` beginnend met `2003-bibf-` / `2008-bibf-` in `_programmaonderdeel_classificatie.json`).
2. **VERIFY-prompt-input bouwen**: voor elke EXTRACT v4-pass moet de orchestrator de relevante examen-vragen voor die PO meegeven als prompt-input. Geen ChromaDB-indexering nodig (VERIFY werkt op de prompt-input, niet via RAG).
3. **Eventueel retrospectief VERIFY-pass** op de 5 al-gemuteerde PO 1.5-anchors zodra examen-classificatie er is.
4. **Patroon-relabeling**: het oude `tools/examen/extract_exam_patterns.py` was kapot (stale path + schond CLAUDE.md regel 3 via directe Anthropic-API-call) en is verwijderd. Vervangen door eenmalige subagent-relabeling per refresh-event (geen permanent script — `complexiteitspatronen.json` + `vraagvormen.json` zijn de source of truth). Refresh-protocol staat gedocumenteerd in `data/programma/exam_patterns/_labeling-rapport.md`.

Blokkerend voor: échte v1.0-validatie van PO 1.5+ records.

### 3.6 — Feedback-loop consolidatie + prompt-aanpassingen (review-sessie 2026-05-18)

Bij review van `data/concepten/quality_checks/` (nu verwijderd) kwamen drie verbeteringen naar boven die de feedback-loop op records harmoniseren:

1. ✅ **Gaps-feedback consolideren naar één formaat + locatie** (uitgevoerd 2026-05-18). Vandaag (vóór deze pass) schreef EXTRACT v4 naar twee plekken (`quality_checks/<po>/dangling-references-<run_id>.json` apart + `data/extractie/gaps.json`), plus een legacy examen-eval-format. Nu: alle gestructureerde feedback op records (`dangling-reference`, `records.ontbreekt`, `bron-gap`, `granulariteit.beslissing-nodig`, `context-edge-ontbreekt`, examen-evaluatie-aspecten) gaat naar `data/extractie/gaps.json` append-only. Aangepast: `prompts/concept-extractie-v4.md` §Gaps.json (was: Dangling-references + Gaps.json apart), `prompts/concept-verify-v1.md` aspect-vocabulaire (twee nieuwe waarden), [docs/adr/ADR-008-concept-extractie.md](docs/adr/ADR-008-concept-extractie.md) §166-170 + §13.5 (globale artefacten-tabel), [CLAUDE.md](CLAUDE.md) mappenstructuur (`quality_checks/` verwijderd). Narratieve patroon-rapporten horen in `v4-extraction-rapport.md` / VERIFY-rapport, niet in gaps.json.

2. **Schema 1.6 — `oorzaken[]` / `componenten[]` enumeratie-veld.** Vandaag heeft schema 1.5 wel `bouwstenen[]` (structureel-decompositioneel, "uit welke onderdelen bestaat X") en `voorbeelden[]` (illustratief), maar geen gestructureerde causale lijst ("waarom ontstaat X"). Historische examenvragen vragen herhaaldelijk "geef de N voornaamste oorzaken" (positief consolidatieverschil: 4 oorzaken — examen 2013-2-vr8 én 2015-1-vr11 identiek). Voorstel: optioneel veld `oorzaken[]` (of `componenten[]` — naam-keuze) op `begrip`/`regel`-records, sub-shape `{label, text, confidence, source, _provenance}`. Wanneer de wet geen lijst geeft maar doctrine wel: `confidence: inferred` of `doctrine-grounded` mits bron-passage gedocumenteerd. Additive, geen breaking change. Sluit aan bij andere schema 1.6-werk in §6.0 (situering-paragraph).

3. **EXTRACT-prompt — context-via-edges proactief.** Schema 1.5 heeft 7 edge-types waarvan `specialisatie-van` (met `regime`-facet), `onderdeel-van` en `vereist-kennis-van` exact bedoeld zijn voor scope/regime/context. Probleem: de v4-prompt noemt dit alleen reactief, als regime-conflict-fix (regel 11 §510-525). Voorstel: aparte regel "Context-via-edges-verplichting" — élk record onder een specifiek regime, niveau of overkoepelend fenomeen moet expliciet een edge naar dat overkoepelende concept hebben (`right-of-use-actief` → `specialisatie-van: ifrs-16`, `consolidatieverschil` → `onderdeel-van: geconsolideerde-jaarrekening`, etc.). VERIFY-bevinding `context-edge-ontbreekt` als aspect in gaps.json voor records die deze edge missen. Voorkomt scope-verwarring (statutaire vs. geconsolideerde goodwill) zonder dat een dedicated `toepassingsniveau`/`regime`-veld nodig is.

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

## Fase 6 — Leermateriaal-laag als interpretatieve laag (ADR-010 §2026-05-18)

Ontwerp vastgelegd 2026-05-18 (ADR-007 schema 1.6 + ADR-009 §6 + ADR-010 §interpretatieve-laag). Code-werk niet gestart. Heuristiek: concept-laag = samen-aanpassen-met-regel; leermateriaal-laag = per leerpad interpretatief.

### 6.0 — `docs/studiemateriaal-schrijfregels.md` schrijven (§6.3, voorwaarde voor de rest)
Apart document analoog aan `docs/concept-schrijfregels.md`. Scope: parafrase-grens, wikilink-discipline, voice/stem, doorlink-conventies, examenrubriek-vorm, synthese-inbedding, compactheidscontract, anti-fabricatie-grens, niveau-toelichtingen (per kennen/begrijpen/toepassen/integratie één-zin-uitleg voor oriëntatie-sectie). Volledige scope in ADR-010 §studiemateriaal-schrijfregels. **Vereist vóór** glue v3 + code-aanpassingen.

**Open punt — hoe sturend?** Niveau-werkwoorden ("toepassen", "integreren") moeten doorklinken in glue-stem voor toepassen-/integratie-PO's, maar concrete stijl-richtlijn (één-zin in intro vs. expliciete framing vs. impliciet weefsel) is nog niet vastgelegd. Te beslissen tijdens schrijven §6.3.

### 6.1 — Bidirectionele edge-render (pre-render index-pass)
Omkerings-labels per edge-type (ADR-010 §bidirectionele-edge-render). 6/7 edges renderen bidirectioneel, `verwijst-naar` opt-out. Centrale config in nieuw bestand `tools/leermateriaal/lib/edge_render_config.py`. Templates concept-fiche + competentie-fiche aanpassen. Inverse-edges gegroepeerd renderen (één callout per type, niet per inkomende edge).

### 6.2 — Concept-fiche schema-1.6-fy + synthese-skip
- `render_concept_fiche.py`: situering-paragraph bovenaan boven TL;DR (ADR-007 schema 1.6).
- `render_concept_fiche.py`: skip records met `node_type == "synthese"` — geen losse fiche meer.
- Content-sync (ADR-019) verwijdert bestaande gerenderde synthese-fiches in volgende run.
- Templates voor schema 1.5-velden (`in_praktijk[]`, `voorbeelden[]`, `illustraties[]`) afronden — drie concretiserings-velden multi-niveau plaatsing (record-top + bouwsteen + berekeningsmethode + per-stap inline).

### 6.3 — Minicursus als interpretatieve laag (glue v3 + synthese-inbedding)
- `prompts/minicursus-glue-v3.md` schrijven: parafrase-met-bronlink-regels (ADR-010 §implicatie-3). Vervangt `prompts/minicursus-glue-v2.md`.
- Validator: paragraaf-zonder-wikilink mag geen feitelijke claim bevatten — fail build bij overtreding.
- `render_minicursus.py`: nieuw hoofdstuk-type `synthese` of `thematisch.synthese_id`-binding voor inline synthese-render (vergelijkingstabel + mermaid-beslisboom).
- Leerpad-YAML-schema bumpen indien nodig om synthese-binding mogelijk te maken.

### 6.4 — Examenfocus-eind-rubriek (ADR-009 §6)
- `render_minicursus.py`: eind-rubriek "Examenfocus" als laatste H2 vóór "Verder lezen".
- `> [!question]-` callouts, twee subkoppen (echte ITAA-vragen ⚖️ vs. synthetische varianten 🤖).
- Back-reference run-time: scan `data/exam_focus/*.json` voor `concept_ids` ⊆ records van PO X.
- `voorbeeldvraag--*.json` schema-veld `voorbeeld_oplossing` verplicht maken (ADR-009 §6).

### 6.5 — Examenprogramma sturend in minicursus (ADR-010 §implicatie-5)
- Nieuw `tools/leermateriaal/lib/taak_binding.py`: `resolve_taken(hoofdstuk, programma_json) → set[taak_code]`. Ketting: hoofdstuk → records → `linked_anchors` → anchor_id → taak (direct of via kenniselement → doelstelling).
- `render_minicursus.py`: vroege oriëntatie-sectie "Wat verwacht het examen van jou?" — niveau-callout + taken-lijst (compact). Niveau-toelichtingen uit §6.0 schrijfregels.
- `render_minicursus.py`: per inhoudelijke H2 taak-marker `> [!info]` met "Hoort bij taak X: …". Voorbereidings-hoofdstukken (leerpad-schema 1.1) krijgen `> [!note]` "Voorbereidende kennis — fundament voor de taken hierna."
- `render_minicursus.py`: eind-dashboard "Heb je deze taken in de vingers?" vóór examenfocus-rubriek. Lijst alle taken met ✓/⚠/✗-indicator + secties-link of cross-PO-link.
- Leerpad-schema 1.1: `voorbereiding`-hoofdstuk-type uitrollen — bestaande leerpaden waar zinvol promoveren (curator-werk per PO).
- Validatie: hoofdstuk zonder taak-binding (en `type != voorbereiding`) → curator-warning. Taak zonder dekking in eind-dashboard → ✗ + warning. PO 100% voorbereiding → warning.
- Glue-prompt v3 (§6.3): PO-niveau als input, werkwoorden in hoofdstuk-intro's moeten niveau respecteren (open richtlijn — zie §6.0).

### 6.6 — Pilot-render PO 1.5 end-to-end (✅ gedaan 2026-05-18)

**Bevindingen**: pilot-rapport `/tmp/pilot-po-1.5-rapport.md`. Render-laag (§6.1, §6.2, §6.3, §6.5) is **gezond** — geen functionele bugs op PO 1.5. Eén render-fix doorgevoerd (kerninzichten-bullets newlines). Validator-helper geleverd als `tools/leermateriaal/validate_minicursus.py` (herhaalbaar voor alle PO's).

**Twee follow-up acties die volgen uit de pilot**:

1. **Curator-pass §6.5-output op 7 minicursussen**. PO 1.1, 1.2, 1.3, 1.6, 1.7, 1.8, 1.9 hebben ingevulde glue maar geen oriëntatie-sectie / niveau-callout / taak-markers / eind-dashboard (glue werd ingevuld vóór §6.5 in de template landde). Per PO kiezen: A. forceer-rerender + glue v3 opnieuw vullen, of B. handmatige injectie van §6.5-blocks zonder glue te raken.
2. **Data-issues doorgeven aan concept-extractie-sessie**:
   - 17 dangling fiche-wikilinks over 4 PO's (zie validator-output of pilot-rapport voor lijst)
   - 15 leerpad-refs ontbrekend in `leerpaden/1.5.yaml` (records hernoemd of opgegaan; al deels in TODO doorlopend onderhoud §"Bron-genaamde records")
   - 1 mogelijke synthese aan te maken: `ifrs-16-lessee-vs-lessor-overzicht`

**Notitie**: PO 1.4 en 1.5 glue is verloren door pilot --forceer-renders. Beide PO's wachten op nieuwe Opus-subagent-pass met glue-v3-prompt — perfect moment om v3 voor het eerst te valideren.

### 6.7 — Diff-changelog vanaf v1.0 (ADR-010 §versionering-vervangen)
- `tools/leermateriaal/build_changelog.py`: git-diff vs laatste publieke tag, filter content/concepten + competenties + studiemateriaal, classificeer inhoudelijk vs render-only, aggregeer per minicursus.
- `content/changelog/index.md` + `content/changelog/<id>.md` per record. Chronologisch nieuwste eerst.
- `render_*.py`: badge `> [!update] Bijgewerkt sinds v<tag>` op elke gewijzigde fiche, link naar `/changelog/<id>`.
- User-triggered tagging — geen automatische tag bij commit. Zet v1.0-tag pas bij eerste publieke release.
- Hangt aan: na §6.6 pilot (eerst content op orde, dan changelog erop bouwen). Niet blokkerend voor v1.0 — kan ook ná v1.0 als post-release feature.
- Vervangt: `content/snapshots/<v>/`-append-only-pad uit ADR-010 §2 (gesuperseded).

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
- ~~**ADR-010**: revisie pending — concept-fiches als reference, minicursus als primair~~ ✅ Vastgelegd 2026-05-18 (§interpretatieve-laag + 5 implicaties)
- **ADR-010 — tutor + synthese-records**: tutor retrievet via concepten-RAG ook synthese-records, maar §implicatie-2 verwijderde de losse fiche. Open: stuurt tutor ruwe record-JSON als context, of mini-render-on-the-fly (vergelijkingstabel + mermaid als markdown)? Niet urgent — geen synthese-records in productie tot §6.3 minicursus-render hen inbedt.
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
