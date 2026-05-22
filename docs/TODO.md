# TODO — Certificaid roadmap

_Centrale inhoudsopgave van openstaand werk, geordend per afhankelijkheid._
_Voor de gedetailleerde issues: zie de gelinkte bronbestanden — dit document
houdt het overzicht, geen content-duplicatie._

**Laatste update**: 2026-05-23 (Fase 7 toegevoegd — schema 2.1 v1.5 + extractie v6 + render-laag)

## Logica van de volgorde

```
1. Infrastructuur (records-API + matches-store + content-sync)  [klaar]
   ↓
2. Schema 1.5 + EXTRACT v4-prompt                                [klaar]
   ↓
3. PO 1.x content-review via EXTRACT v4 + VERIFY-feedback-loop  [klaar — 2026-05-19]
   ↓
4. Bronnen-laag uitbreiden (1.1 ETL-fix + 1.2 fiscale gidsen)   [pending]
   ↓
5. Andere PO's uitrollen (3.0, 4.0, 2.x)                         [pending]
   ↓
6. Render-laag-revisie (ADR-010): minicursus als primair         [klaar — 2026-05-18]
   ↓
7. Schema 2.1 v1.5 + extractie v6 (multipass-operaties) + render-laag-revisie  [in uitvoering]
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

## Fase 3 — PO 1.x content-review (✅ volledig af — 2026-05-19)

**Eindstaat 2026-05-19**: 463 records (was 431), allemaal op schema 1.6 met situering. 0 open hoog-prio gaps (was 19). Commit [5de6e9d0](commit/5de6e9d0).

EXTRACT v4 per anchor, centraal-first. Per PO strategie volgens ADR-008 §18.7:
- PO 1.5 (14 anchors): waves + revisit-pass (eerder afgewerkt)
- PO 1.6 (20 anchors): wave 1 (5 batches) + wave 2 parent-batched (4 batches) + cross-cutting hoog-prio (1 batch, 5 nieuwe records)
- PO 1.7 (58 anchors): wave 1 (7 batches) + wave 2 parent-batched (9 batches)
- PO 1.1-1.4: touch-up + structurele cleanup (4 agents)
- PO 1.8 (53 records): one-shot ✅ — empirisch bewezen tot ~55 records
- PO 1.9 (44 records): one-shot ✅
- Eindgap-resolution: 6 open hoog-prio resolved (4 nieuwe records)

Empirische lessen vastgelegd in ADR-008 §18.7 (wave-planning + one-shot), ADR-019 §Worktree-isolatie (records-API divergentie + workaround), `prompts/concept-extractie-v4.md` (scope-trust, gaps.json-bescherming).

**Resterend Fase 3-werk (laag-prio)**:
- 82 open gaps midden/laag-prio (deels strategic-pass-archief)
- 7 minicursussen curator-pass (1.1-1.3, 1.6-1.9) — andere sessie
- TODO ADR-019: aanpassing records-API om disk-pad te resolven tegen daemon-known repo-root (maakt worktree-veilig)

---

## Fase 3-historie (gearchiveerd — pre-2026-05-19)

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

Wave-strategie per PO, gestuurd door anchor-count (zie ADR-008 §18.7):

| PO | Anchors | Aanpak |
|---|---|---|
| 1.6 | 20 | Wave 1 top-level (I, II, III, IV, taak.1) + parent-batched wave 2 (per parent één agent voor alle sub-anchors) |
| 1.7 | tbd | < 10 anchors → één agent of parent-batched |
| 1.8 | tbd | klein → één agent voor hele PO |
| 1.9 | tbd | klein → één agent voor hele PO |

Centraal-first blijft de regel: top-level vóór sub-anchors. Status PO 1.6 (2026-05-18): wave 1 compleet (I, II, III, IV, taak.1), wave 2 sub-anchors lopend (1.6.I.A klaar; parent-batched voor de rest).

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

## Fase 6 — Leermateriaal-laag als interpretatieve laag (✅ volledig af — 2026-05-18)

Ontwerp vastgelegd én code-werk uitgevoerd in één werkdag. Heuristiek: concept-laag = samen-aanpassen-met-regel; leermateriaal-laag = per leerpad interpretatief.

| Sub-taak | Status | Commit |
|---|---|---|
| §6.0 `docs/studiemateriaal-schrijfregels.md` | ✅ | andere sessie (`7a6938f2`) |
| §6.1 bidirectionele edge-render | ✅ | `00c90162` |
| §6.2 situering-render + synthese-skip | ✅ | `28973997` + Quartz-fix `5f8fe13e` |
| §6.3 minicursus-glue-v3 + synthese-inbedding | ✅ | `ae3ffe5f` |
| §6.4 examenfocus-rubriek (één lijst + bootstrap-data) | ✅ | `01ada764` (v2) |
| §6.5 examenprogramma sturend (taak-binding) | ✅ | `b2f4a4ad` |
| §6.6 pilot PO 1.5 + validator | ✅ | `8a45a08a` |
| §6.7 diff-changelog | ✅ | `ef34f941` (badges → Quartz native lastmod in `5f8fe13e`) |

**Plus extra in deze sessie**:
- `tools/examen/_vraagtekst_normalisatie.py` (commit `7843fb1f`) — PDF-extract opkuisen aan bron
- `tools/examen/_sub_vragen_splitter.py` (commit `9408a56d`) — sub_vragen[] per j/f-set / MC / open
- `tools/examen/genereer_examenfocus_uit_classificatie.py` — bootstrap-generator
- Glue v3-vulling PO 1.5 (commits `52f15740` + `dbce6ab5`) — eerste live-test
- `belgisch-gaap` + `ifrs` begrip-records + synthese-stub `ifrs-16-lessee-vs-lessor-overzicht` (commit `1adeccdb`)
- Leerpad 1.5.yaml schoongemaakt (9 dangling refs vervangen)
- Quartz `Component.ArticleTitle()` hersteld (commit `93c941f3`)

### Follow-up (geen blockers, in te plannen)

1. **Curator-pass §6.5-output op 7 minicursussen** (1.1, 1.2, 1.3, 1.6, 1.7, 1.8, 1.9). Die hebben ingevulde glue maar missen oriëntatie + taak-markers + dashboard (glue dateert van vóór §6.5 in template). Per PO kiezen: A. forceer-rerender + glue v3 opnieuw vullen, of B. handmatige injectie van §6.5-blocks zonder glue te raken. PO 1.4 wacht ook (glue verloren door pilot --forceer).
2. **Tweede pilot op andere PO** (bv. 1.4 of 1.7) om de render-pipeline op een ander niveau-type te valideren.
3. **v1.0-tag** wanneer PO 1.x volledig is — diff-changelog kan dan default werken zonder `--basis-tag`.

---

## Fase 7 — Schema 2.1 v1.5 + extractie v6 + render-laag (in uitvoering)

**Doel**: nieuwe data-laag (schema 2.1 v1.5) + multipass-operaties-pipeline (extractie v6) + render-laag-revisie. Vervangt schema 2.0 + EXTRACT v5.

**Canonieke documenten**:
- [`docs/adr/ADR-029-schema-21-operaties-model.md`](adr/ADR-029-schema-21-operaties-model.md) — design-rationale + operations-model + v1.0 → v1.5 changelog
- [`docs/schema-v15-besluit.md`](schema-v15-besluit.md) — geconsolideerde spec (21 besluiten + finale structuur)
- [`data/concepten/schema-2.1.schema.json`](../data/concepten/schema-2.1.schema.json) — bron-van-waarheid
- [`docs/render-laag.md`](render-laag.md) — render-laag werkpakket-spec
- [`prompts/multipass/`](../prompts/multipass/) — 5 operatie-prompts (run-1 t/m run-5 = `beschrijven`, `rollen`, `voorbeelden`, `relaties`, `factcheck`)

### 7.1 — Schema + migratie (klaar — 2026-05-23)

- ✅ Schema v1.4 → v1.5 in `data/concepten/schema-2.1.schema.json`
- ✅ Migratie 396 records v1.4 → v1.5 via `tools/extractie/migrate_records_to_v15.py`
- ✅ Plaatsingsregel "wat-is-het" vs "wat-doet-de-accountant" (E3) geformaliseerd in schema + prompts (ADR-029 §E3)

### 7.2 — Wave-2 beschrijven-operatie (open)

371 lege records vullen via 12-parallel Sonnet `beschrijven`-operatie (~1.5u wall-clock geschat). Alleen `verondersteld`/`betwijfeld` confidence — upgrade volgt in `claims_checken`-pass.

- Status: voorbereiding klaar, wave-2 nog niet gestart
- Prompt: `prompts/multipass/run-1-draft.md`

### 7.3 — Render-laag-revisie (open)

Render-template + script herschrijven voor schema 2.1 v1.5. Detail in [`docs/render-laag.md`](render-laag.md) §Render-todos. Hoofdtaken:

- **A. Template-update** (5 sub-taken): `ConceptFiche.tsx` rebuild, label-mapping per `concept_type`, `kern`-wrapper rendering, confidence-iconen per claim, conditional rendering
- **B. Concept-specifieke views** (6 sub-taken): fractale `elementen` recursie, `weergaven` type-specifiek, `accountant_perspectieven` matrix, `voorbeelden` walkthrough, `valkuilen`/`speelruimtes` blokken, `syntheses` per type
- **C. Cross-record navigatie** (2 sub-taken): `relaties` backlinks-pagina, `vergelijkbaar_met` 2-kolom-tabel
- **D. Status + operatie-tracking** (2 sub-taken): operaties-historiek-balk, status-badge afgeleid uit `metadata.changelog[]`
- **E. Markdown-bridge** (1 sub-taak): nieuw JSON → markdown render-script (legacy `render_concept_fiche.py` is voor schema 2.0)

Open beslispunten (7 stuks): zie [`docs/render-laag.md`](render-laag.md) §Open beslispunten.

### 7.4 — Overige operaties uitbouwen (roadmap, post wave-2)

In ADR-029 §Operaties-model gedefinieerde maar nog niet uitgevoerde operaties:

- `claims_checken` — RAG-validatie, upgrade `verondersteld` → `geciteerd`/`afgeleid` of flag `weerlegd`
- `relaties_aanvullen` — `vergelijkbaar_met` + bevat-edges rijk maken
- `accountant_perspectief` — `accountant_perspectieven[]` per actor invullen
- `didactisch_verrijken` — `valkuilen[]`/`speelruimtes[]`/`voorbeelden[]` toevoegen
- `kandidaat_review` — proeflezen studentbril
- `leespad_aanvullen` — `inhoud.voorkennis_leespad` op basis van ankers + vereist-relaties

Niet prioritair voor wave-2 (per ADR-029): `cijfer_validatie`, `examenvragen_aansluiting`, `consistentie_check`, `volledigheid_check`.

### 7.5 — Schema 2.0 → archive (klaar — 2026-05-23)

- ✅ Legacy v2.0 records bewaard in `data/concepten/_archive/v2.0-pre-schema-2.1-...`
- ✅ ADR-025 verplaatst naar `docs/adr/archive/`
- ✅ `prompts/concept-extractie-v5.md` + `v5-bundle.md` verwijderd
- ✅ `docs/pilot-fase2-pipeline.md` + `sessie-2026-05-21-schema-20-handoff.md` verwijderd (info in ADR-029 + git-history)

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

### Dode code daemon (uit avond-handoff 2026-05-21)
- `_bronnen_rerank()` in `tools/extractie/embedding_daemon.py:548` is dode code sinds rerank verplaatst werd naar MCP-server in-process. Verwijderen na verificatie geen call-sites.

### Aandelen-fiche concept-record (uit avond-handoff 2026-05-21)
- Structurele asymmetrie tussen obligatielening (compleet) en aandelen (geen record). Onder Fase 7 wave-2-beschrijven mee te nemen.

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
