# Certificaid — Openstaand werk

Eén bron voor *wat er nog moet gebeuren*. Voltooide fases leven niet hier — git-history en ADRs zijn de plek voor "wat hebben we gedaan en waarom".

**Laatste update**: 2026-05-30 (ADR-026 tarief-pijplijn volledig operationeel: `tarieven_api` + MCP-server + chunker + 2 prompts + **82 records** geëxtraheerd uit Cijferzakboekje 2026 via 8 parallel Sonnet-subagents. Records zijn **pure data-laag** — géén content/-render; toegang via MCP-server voor LLM-tutors en leerstuk-auteurs. Verify-pass open punt. Vorige update 2026-05-28 over Fase 2 massa-extractie blijft van kracht.)

---

## 🚀 Status snapshot 2026-05-28

| Laag | Status | Details |
|---|---|---|
| **Skeleton (Fase 1 schema 2.2)** | ✅ 359/359 | alle records met scope.in/out + sub-concept-hints |
| **Concept-extract (Fase 2)** | ✅ 359/359 | content gevuld via bundle-flow (chunks pre-fetched); 5 waves × 8-9 agents parallel |
| **Verify (Pass 2)** | ⏳ 0/359 | didactische kwaliteits-check per record |
| **Verbeter (Pass 3)** | ⏳ 0/359 | verwerk verify-feedback |
| **Render-laag (Fase 7)** | ✅ basis | tools/leermateriaal/render_concept_v22.py + render_index_v22.py — 359 fiches in content/concepten/ + 4 index-pagina's |
| **Quartz-build** | ⚠️ niet getest | render-output zou bruikbaar moeten zijn; build lokaal valideren |

**Wat een student nu kan doen**: openen `content/concepten/_index.md` → kies PO / type / categorie → klik door naar fiches. Elke fiche heeft definitie+substantie+rationale, bouwstenen (regel/stap/formule/...), voorbeelden met concrete €-bedragen+klasse-codes, valkuilen, accountant-perspectieven, relaties. Confidence-iconen (📖/🔗/🤖) markeren bron-zekerheid per claim.

---

---

## Mindset (architectuur-principes)

Deze gelden bij elke keuze:

- **POC met protoduction-aanname** — alle code wordt productie-code. We bouwen geen wegwerpprototype.
- **Vertical slice eerst** — één programmaonderdeel, end-to-end (ruwe bron → leesbare bron → bron-RAG → concepten → fiche → tutor → oefenvraag) vóór we horizontaal verbreden naar alle programmaonderdelen.
- **"Never done"-DoD** — *"goed genoeg om door te schuiven + regressietest aanwezig"*. Niet "100%". Bij nieuwe inzichten kunnen we terugkeren naar elke laag zonder de hele pipeline te moeten herbouwen.
- **Iteratief, niet sequentieel** — fases kunnen overlappen. Voorbeeldexamens-laag en examenprogramma-laag worden parallel opgebouwd; examenpatronen lopen parallel aan concept-extractie.

---

## Cross-cutting (loopt continu mee)

- **Kenniselement-dekkingscheck** — voor elk kenniselement uit het examenprogramma: minstens één concept dat hem afdekt + minstens één voorbeeldvraag of examenpatroon dat hem toetst. Eerste-orde regressietest. ([ADR-002](adr/ADR-002-examenprogramma-scoping.md))
- **Voorbeeldexamens-corpus** — vroeg ingelezen en gestructureerd; ground truth voor concepten én patronen. Nooit geforceerd ("dit examen vraagt X dus we maken concept X" is verboden — zie [ADR-008](adr/ADR-008-concept-extractie.md)).
- **Examenpatronen-laag** — bouwt parallel aan concept-extractie. Drie functies: lens bij extractie, validator van conceptenset, generator van oefenvragen. ([ADR-009](adr/ADR-009-examenpatronen.md))
- **Reprocessing-strategie** — input verandert → stale-cascade, geen auto-regen. Mens kiest of/wanneer. ([ADR-003](adr/ADR-003-reprocessing-evaluatie.md))
- **Granulariteit-skelet** — concept-tree-opbouw per cluster ([`docs/granulariteit-skelet.md`](granulariteit-skelet.md) + [ADR-030](adr/ADR-030-granulariteit-typologie.md)). Sparring-werk dat vooraf gaat aan record-herstructurering. **Voltooid**: mobiliteit · kapitaalstructuur · werknemers-vergoedingen · overdracht-onderneming · schuldfinanciering · **controle-opdracht** (laag-2 sub-Kader `controle`, PO 1.6) · **interne-controle** (laag-2 sub-Kader `controle`, PO 1.7, met 3 shared records `coso-framework` · `cyclus-analyse` · `auditcomite`) · **ondernemingsvormen** (thema-cluster vennootschapsrecht, PO 3.0.I + taak.1, 2026-05-26 — lost OP-EC.7 op; 7 vormen als E-instrumenten + Σ-overzicht + `vennootschap-groottecategorieen`). **Shared-records-pattern + perspectief-vs-eigen-record-principe**: zelfde fenomeen × verschillende werk-as = perspectieven, niet aparte records. **Open clusters PO 3.0**: bestuur-en-aansprakelijkheid (II + VII) · vennootschapsgeschillen (VIII) · winstuitkering (IV.B) · insolventie (IX + X). **Open clusters andere**: reorganisatie · fiscale-voordelen-vennootschap · anti-misbruik · beroepsbeoefening · loon-en-payroll (K-techniek) · 3 overige sub-Kaders van `controle` (beoordelings-opdracht · isae-opdrachten · overeengekomen-procedures — kleiner werk per stuk). **Per voltooide cluster**: test-case-validatie via examen-vragen (6 vragen per cluster). **Mapping-fase** (post-skelet): bestaande 396 records herstructureren naar skelet — incl. audit-perspectief op 8 Gebeurtenis-records voor bijzondere revisor-verslagen (OP-EC.E) + COSO/cyclus-record-absorptie naar shared records (OP-IC.E) + **naam-smell-scan** op suffixen `-cluster` / `-rechtsvorm` / `-ic` / `-fiscaal` (= perspectief-vermomming) over alle records + `#initiele-inbreng` sub-sectie toevoegen aan `oprichting-vennootschap`.

---

## Fase 1 — Schema 2.1 v1.5 + extractie v6 + render-laag (in uitvoering)

**Doel**: nieuwe data-laag (schema 2.1 v1.5) + multipass-operaties-pipeline (extractie v6) + render-laag-revisie. Vervangt schema 2.0 + EXTRACT v5.

**Canonieke documenten**:
- [ADR-029](adr/ADR-029-schema-21-operaties-model.md) — design-rationale + operations-model + v1.0 → v1.5 changelog
- [`docs/schema-v15-besluit.md`](schema-v15-besluit.md) — geconsolideerde spec (21 besluiten + finale structuur)
- [`data/concepten/schema-2.1.schema.json`](../data/concepten/schema-2.1.schema.json) — bron-van-waarheid
- [`docs/render-laag.md`](render-laag.md) — render-laag werkpakket-spec
- [`prompts/operaties/`](../prompts/operaties/) — 5 slanke operatie-prompts (5 incl. scope-respect ADR-033)

### 1.0 — 🚨 BLOCKER: Daemon-schema-2.1-compatibiliteit

**Symptoom**: elke `records_api.save_record`-call op een schema-2.1-record faalt met `AttributeError: 'dict' object has no attribute 'strip'`. Daemon-endpoint `/index-concept` crasht.

**Root cause**: `tools/extractie/embedding_daemon.py:389` (`_bouw_embed_tekst`) is geschreven voor schema 1.x — verwacht `record["naam"]` als string en `record["node_type"]`/`main_rule`/`definitie`/`verplichting`/`doel` als top-level velden. In schema 2.1 v1.5 is `naam` een dict (`{"primair": ...}`), `concept_type` (niet `node_type`), en inhoud-velden zitten onder `inhoud.kern.definitie.tekst`.

**Impact**:
- ❌ Wave-2 (1.1) — blokkeert het invullen van 371 lege records
- ❌ Scope.in bootstrap-migratie (script staat klaar op de plank — `tools/lib/migrate_scope_in_bootstrap.py`)
- ❌ Elke andere `save_record`-call op een schema-2.1-record

**Fix-scope** (te onderzoeken vóór uitvoer):
- Port `_bouw_embed_tekst()` naar schema 2.1 v1.5 (`naam.primair`, `concept_type`, `inhoud.kern.definitie.tekst`)
- Scan rest van `embedding_daemon.py` op andere schema-1.x-veld-references
- Mogelijk ook `_render_concept_fiche` in `records_api.py` herzien
- Restart daemon na fix
- Verifieer met 1 record voor bulk-werk hervat

**Werkpunt**: aparte sparring-sessie + ADR (daemon-schema-2.1-compatibiliteit) + zorgvuldige port. Niet ad-hoc fixen.

### 1.1 — Wave-2 beschrijven-operatie

371 lege records vullen via 12-parallel Sonnet `beschrijven`-operatie (~1.5u wall-clock geschat). Alleen `verondersteld`/`betwijfeld` confidence — upgrade volgt in `claims_checken`-pass.

- Status: voorbereiding klaar, wave-2 nog niet gestart
- Prompt: `prompts/operaties/run-1-draft.md`

### 1.2 — Render-laag-revisie

Render-template + script herschrijven voor schema 2.1 v1.5. Detail in [`docs/render-laag.md`](render-laag.md) §Render-todos. Hoofdtaken:

- **A. Template-update** (5 sub-taken): `ConceptFiche.tsx` rebuild, label-mapping per `concept_type`, `kern`-wrapper rendering, confidence-iconen per claim, conditional rendering
- **B. Concept-specifieke views** (6 sub-taken): fractale `elementen` recursie, `weergaven` type-specifiek, `accountant_perspectieven` matrix, `voorbeelden` walkthrough, `valkuilen`/`speelruimtes` blokken, `syntheses` per type
- **C. Cross-record navigatie** (2 sub-taken): `relaties` backlinks-pagina, `vergelijkbaar_met` 2-kolom-tabel
- **D. Status + operatie-tracking** (2 sub-taken): operaties-historiek-balk, status-badge afgeleid uit `metadata.changelog[]`
- **E. Markdown-bridge** (1 sub-taak): nieuw JSON → markdown render-script (legacy `render_concept_fiche.py` is voor schema 2.0)

Open beslispunten (7 stuks): zie [`docs/render-laag.md`](render-laag.md) §Open beslispunten.

### 1.3 — Overige operaties uitbouwen (post wave-2)

In ADR-029 §Operaties-model gedefinieerd maar nog niet uitgevoerd:

- `claims_checken` — RAG-validatie, upgrade `verondersteld` → `geciteerd`/`afgeleid` of flag `weerlegd`
- `relaties_aanvullen` — `vergelijkbaar_met` + bevat-edges rijk maken
- `accountant_perspectief` — `accountant_perspectieven[]` per actor invullen
- `didactisch_verrijken` — `valkuilen[]`/`speelruimtes[]`/`voorbeelden[]` toevoegen
- `kandidaat_review` — proeflezen studentbril
- `leespad_aanvullen` — `inhoud.voorkennis_leespad` op basis van ankers + vereist-relaties

Niet prioritair voor wave-2 (per ADR-029): `cijfer_validatie`, `examenvragen_aansluiting`, `consistentie_check`, `volledigheid_check`.

### 1.4 — Drie-lagen leermateriaal: minicursussen + themafiches (ADR-036)

**Doel**: na concept-fiches als basis-laag, een tweede en derde laag bouwen voor kandidaat-gericht studiemateriaal — themafiches (kapstok per cluster) + minicursussen (verhaal + routekaart per PO).

**Canonieke spec**: [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md) · schrijfregels [`minicursus`](minicursus-schrijfregels.md) + [`themafiche`](themafiche-schrijfregels.md).

**POC voltooid (2026-05-28)**:
- Themafiche-mockup `content/experiment/synthese-consolidatie-v1.md` (cluster consolidatie, PO 1.4)
- Minicursus-mockup `content/leerpaden/1.4.md` (PO 1.4)
- Print-CSS + full-width-tabellen + `.no-print`-class in `quartz-custom/styles/custom.scss`

**Open werkpakket**:
- **Themafiches** voor alle uitgewerkte clusters uit granulariteit-skelet (~15-60 stuks, starten met de zwaarste/meest bevraagde — voorstel: consolidatie · jaarrekening · controle-opdracht · interne-controle · kapitaalstructuur · ondernemingsvormen · personenbelasting · vennootschapsbelasting · btw · mobiliteit · waarderingsregels · financiële-analyse · ifrs-rapportering · reorganisatie · winstuitkering). Mockup verhuizen van `experiment/` naar `content/themafiches/`.
- **Minicursussen** voor alle 19 PO's. Mockup `leerpaden/1.4` als referentie.
- **Generatie-prompts** voor Sonnet-agent (analoog aan operatie-prompts in `prompts/operaties/`) — pas zinvol na ≥3 voorbeelden van elk type (patroon bevroren).
- **Render-tooling-overweging**: blijven minicursus + themafiche handgeschreven (markdown) of komt er render-flow uit JSON-bron? Beslissen wanneer 50+ documenten bestaan.

---

## Fase 8 — Schema 2.2 massa-extractie + render-laag v22 (in uitvoering 2026-05-28)

**Doel**: alle 359 records van skeleton-status (Fase 1) naar concept-status (Fase 2), met didactische verrijking (voorbeelden, valkuilen, bouwstenen, perspectieven), via bundle-flow (ADR-027 pattern).

**Pipeline**: skeleton → bundle-build (`tools/extractie/build_skeleton_bundle.py`) → cluster-extract (Sonnet-agents, 8-9 parallel per wave) → cluster-verify (Pass 2) → cluster-verbeter (Pass 3).

**Status 2026-05-28 13:30 CEST**:

- ✅ Schema 2.2 + ADR-035 + records-API
- ✅ Skeletons 359/359 — alle clusters (boekhouding, jaarrekening-fundament/rest, financiele-analyse, consolidatie, IFRS, management-accounting, bedrijfsadvies, mobiliteit, werknemers-vergoedingen, loon-en-payroll, BTW, internationaal-fiscaal, PB, VenB, fiscale-procedure, fiscale-beginselen, reg-succ, lokaal-fiscaal, fiscale-voordelen, anti-misbruik, vennootschapsrecht-clusters)
- ✅ Cluster-extract Pass 1 — 359/359 concept-status
  - Wave 1: jaarrekening-fundament + vennootschapsvormen + werknemers-vergoedingen + financiele-analyse + bedrijfsadvies + management-accounting (~66 records)
  - Wave 2: vennootschapsrecht-rest + controle-beroep
  - Wave 3: BTW basis + internationaal-fiscaal start + cross-cutting (financiele-analyse)
  - Wave 4: consolidatie + balansposten + jaarrekening-rest + loon + RSZ/VAA + management-accounting + financiele-analyse-rest (~94 records)
  - Wave 5: BTW-rest + internationaal-treaties + VenB-internationaal + fiscale-beginselen + fiscale-procedure + reg-succ + lokaal + anti-misbruik + voordelen (~102 records)
- ✅ Render-laag v22 — `tools/leermateriaal/render_concept_v22.py` + `render_index_v22.py`, 359 fiches naar `content/concepten/` + 4 index-pagina's
- ⏳ Pass 2 Verify — 0/359 (didactische kwaliteits-check)
- ⏳ Pass 3 Verbeter — 0/359 (verwerk verify-feedback)
- ⏳ Quartz lokale build-test
- ⏳ Mens-validatie + escalatie concept → gevalideerd

**Prompts**: `prompts/cluster-skeleton.md`, `prompts/cluster-extract.md`, `prompts/cluster-verify.md`, `prompts/cluster-verbeter.md`.

**Concrete TODO's**:
- [ ] Pass 2 Verify per discipline (jaarrekening + PB + VenB + BTW + vennootschapsrecht + beroep+controle + fiscaliteit-klein + internationaal-fiscaal + cross-cutting)
- [ ] Pass 3 Verbeter — verwerk critical+major issues
- [ ] Quartz `npm run dev` lokaal testen — broken wikilinks/render-fouten zoeken
- [ ] Render-laag verfijnen (eventueel collapsibles voor lange subconcepten, navigatie-sidebar per cluster)
- [ ] PO-indexen verfijnen — multi-PO records nu maar in 1 PO; ook in secundaire PO's tonen
- [ ] Sub-concept-fiches zelf renderen als aparte pagina's? (now inline in parent — kan opzettelijk; check user-preference)
- [ ] Mens-validatie → escalatie naar `metadata.status: "gevalideerd"`

---

## Fase 2 — Bronnen-laag uitbreiden

Blokkeert sommige programmaonderdeel-rollouts. Niet kritisch voor PO 1.x.

### 2.1 — Wet-beroepskwalificaties-2008 — ETL-fix

- Issue: `Art. N_WAALS_GEWEST`-varianten splitsen één artikel in twee secties.
- Trigger voor: PO 4.0 (deontologie).

### 2.2 — 8 fiscale gidsen — ETL-fixes (needs-rework)

Narratieve type-3 PDFs, ETL-uitdagingen. Trigger voor: PO 2.1-2.8 (fiscaliteit, 8 PO's).

### 2.3 — Refresh-gate na elke trust-promotie

Regel al vastgelegd in ADR-005 §9.1; gebruik `tools/etl/mark_trusted.py --refresh`.

### 2.4 — Architecturale follow-ups bronnen-ETL (geïdentificeerd 2026-05-15)

- **`inject_headings_wettekst` hardcoded `_chunk_type = "Art."`**: zet altijd `chunk.type: "Art."` ongeacht of body `Art.`- of `Artikel`-headings heeft. Voor EU-bronnen wordt frontmatter handmatig overschreven na conversie; bij re-conversie weggeschreven. Fix: `detect_hierarchy` artikel-type-detectie uitbreiden, of `inject_headings_wettekst` een `article_type`-parameter geven.
- **Body-niveau column-bleed** in 3 ITAA-normen (effectennorm, aww-geconsolideerd, omzetting-vennootschap): paragrafen interleaven door tweekoloms-PDF-extractie. Vereist column-aware PDF-extractie (pymupdf met blocks/columns), niet oplosbaar via text-transformer.
- **Bijlage-tabellen** in effectennorm + omzetting-vennootschap renderen als gefragmenteerde `##`-headings. Vereist tabel-aware extractie.
- **5 wetteksten** met structuur-issues open: Decr-Waals-Directe-Belastingen, MIGB-Brussel/Vlaanderen/Wallonie, Wet-beroepskwalificaties-2008. Per bron eigen oorzaak — case-by-case ETL-werk.
- **9 wetteksten needs-rework**: narratieve praktijkgidsen (almanakken, toelichtingen aangifte) — sub-optimale structuur, accepteerbaar met caveat.

---

## Fase 3 — Andere programmaonderdelen uitrollen

Pas na Fase 2 (bronnen) klaar is voor de relevante PO's. Per PO: standaardproces via operaties-pipeline op schema 2.1 v1.5.

### 3.1 — PO 3.0 — Vennootschapsrecht

Primaire bronnen al trusted (WVV + KB-WVV-2019). Niet blocked door Fase 2.

### 3.2 — PO 4.0 — Deontologie

Vereist Fase 2.1 (Wet-beroepskwalificaties). Primaire bronnen: IESBA-code + ITAA-normen (deels trusted).

### 3.3 — PO 2.1 t/m 2.8 — Fiscaliteit (8 PO's)

Vereist Fase 2.2 (8 fiscale gidsen). Volgorde binnen 2.x: nog te bepalen.

---

## Fase 4 — Examenvraag-antwoord-pipeline (POC actief)

Pasklare student-ready antwoorden op alle voorbeeldexamen-vragen, RAG-gegrond aan bronnen, per-claim confidence (schema 2.1 v1.5 tokens). Werkpakket-spec: [`docs/examen-antwoord-pipeline.md`](examen-antwoord-pipeline.md).

**Status 2026-05-26**: POC op PO 1.4 (6 vragen) succesvol — gemiddeld ~60-90 sec/vraag met 2-5 RAG-calls (vs. 23 min/vraag van eerste POC zonder budget). v3-prompt-regels gevonden, render-laag fixes gemerged, vision-her-interpretatie-noodzaak gedocumenteerd.

### 4.1 — Cluster-detectie + dedup — ✅ gerealiseerd
Pipeline: [`tools/examen/cluster_vragen.py`](../tools/examen/cluster_vragen.py) (bge-m3 embedding, cosine ≥ 0.80) → agent-review → [`tools/examen/apply_cluster_review.py`](../tools/examen/apply_cluster_review.py) stempelt interpretaties met `cluster_id` + `cluster_verdict`. Renderer ([`tools/examen/render_merged_v4.py`](../tools/examen/render_merged_v4.py)) groepeert cluster-leden: één canonical-render, gecombineerde herkomst-regel "Examens X & Y", multi-anchor, 🔁-badge. Eindstand: 11 clusters in 8 PO's, 282 unieke antwoord-units uit 293 vragen.

**Open vervolg**: antwoord-deduplicatie voor `echt_duplicaat` (één canoniek `_antwoorden/<cluster_id>.json` ipv per-vraag-records). Voor `varianten`-clusters: antwoord moet UNIE van alle subsets dekken (vereist cluster-context in antwoord-prompt — al gevangen in prompt v2.0 §9).

### 4.2 — Prompt v2.0 (canoniek antwoord-prompt) — ✅ gerealiseerd
[`prompts/modelantwoord-v1.md`](../prompts/modelantwoord-v1.md) herschreven naar v2.0. Bevat alle POC-leerlessen: tool-budget (max 4 RAG-calls, parallel, rerank=False), blok-volgorde verplicht, schema 2.1 v1.5 confidence-tokens + 📖/🔗/🤖/❓/❌-iconen, PNG-Read regel voor visuele vragen, cluster-bewustzijn voor varianten, compactheid per vraag-type, anti-patterns.

**Open vervolg**: re-run de 6 PO 1.4 vragen met canonical v2.0-prompt voor visuele consistentie (huidige tekst-iconen zijn nog ⚖️/🤖 — backward-compat in renderer maar visueel gemengd).

### 4.3 — Visuele-vraag-detectie — ✅ gerealiseerd
[`tools/examen/detect_visuele_vragen.py`](../tools/examen/detect_visuele_vragen.py) scant alle interpretaties op signalen: visuele `kwaliteits_flags`, typed `context_blokken[]` (tabel/groepsschema/balans), tekstpatronen ("zie onderstaande tabel", "vul aan", "kruis aan"). Output: `data/programma/examen_vragen/_visuele_vragen.json` + `--stamp`-modus voegt `vision_review_nodig`-veld toe aan 50 interpretaties (17% van corpus). Pipeline gebruikt dit veld om bij scaling automatisch PNG-Read te triggeren in antwoord-agent.

### 4.4 — Schema-veld voor "wetsletter ↔ doctrine"-nuance
Terugkerend patroon (3 vragen in PO 1.4 alleen): het examen-verwachte antwoord steunt op IFRS/doctrine/CBN-advies, niet op letterlijke wetstekst. Nu in ad-hoc `_poc_notitie`. Structureel veld nodig — bv. `grondings_caveat` per `vraag_antwoord` of een 6e confidence-token.

### 4.5 — Bron_refs-validatie
Script dat alle `bron_refs` in `_antwoorden/` controleert tegen filesystem `resources/bronnen/` en bronnen-index. Voorkomt verzonnen paden (al wel `#anchor`-fragmenten in prompt verboden — niet gevangen).

### 4.6 — ADR-034
Schrijven zodra POC stabiel is. Bundelt: pipeline-architectuur, RAG-grounding-regels, dedup-strategie, render-laag.

---

## Doorlopend — Onderhoud

### Bron-genaamde records (deels onderweg)

Geïdentificeerd 2026-05-18:
- `ifrs-verordening-1606-2002` → split in `verplichte-ifrs-eu-beursgenoteerden` + `endorsement-procedure-eu`
- `kb-wvv-uitvoering`, `wetboek-vennootschappen-verenigingen`, `wetboek-economisch-recht-boek-iii` — verspreiden over fenomenen
- 6 `ias-1-*` records — prefix-removal (regel 11 v4-prompt)
- Andere `ias-*`, `ifrs-*`, `cbn-*` records — per-anchor evaluatie

### Multi-concept-smell records (27 gesignaleerd)

Meeste competenties met "X en Y"-naming. Per-anchor beoordelen of écht splits.

### 36 procedure-records — hercategorisatie

Phase A behield `procedure`-type voor case-by-case Phase B. Hercategoriseren naar `cluster` of `competentie` per EXTRACT-touch.

### `voorgesteld:randvoorwaarden` — 1 anomalie

Bij PO 1.6 EXTRACT beslissen: bouwsteen van `aanvaarden-audit-opdracht`-competentie of zelfstandige regel?

### ADR-017 bronnen-migratie (12/116 done)

Eenvormig extract-schema. Backlog: 104 bronnen. Long-running achtergrond.

### Backup-tags archeology (8+ tags)

Plus `backup/pre-schema-1.5-migration-2026-05-18`. Bij geen issue gedurende 30 dagen: tags verwijderbaar.

### Dode code daemon

`_bronnen_rerank()` in `tools/extractie/embedding_daemon.py:548` is dode code sinds rerank verplaatst werd naar MCP-server in-process. Verwijderen na verificatie geen call-sites.

### Aandelen-fiche concept-record

Structurele asymmetrie tussen `obligatielening` (compleet) en `aandelen` (geen record). Onder Fase 1.1 wave-2-beschrijven mee te nemen.

### Curator-pass §6.5 op 7 minicursussen (legacy schema 1.6)

Minicursussen 1.1, 1.2, 1.3, 1.6, 1.7, 1.8, 1.9 hebben glue maar missen oriëntatie + taak-markers + dashboard (glue dateert van vóór §6.5 in template). Per PO kiezen: forceer-rerender + glue v3 opnieuw vullen, of handmatige injectie van §6.5-blocks. *(Wordt vervangen door render-laag-revisie Fase 1.2 voor schema 2.1.)*

### Tutor + synthese-records

Tutor retrievet via concepten-RAG ook synthese-records, maar ADR-010 §implicatie-2 verwijderde de losse fiche. Open: stuurt tutor ruwe record-JSON als context, of mini-render-on-the-fly (vergelijkingstabel + mermaid als markdown)? Niet urgent — geen synthese-records in productie tot render-laag-revisie hen inbedt.

### Worktree-rot voorkomen

Run `tools/worktree_status.sh` bij sessie-start om stale agent-worktrees te zien. Bij ≥3 dagen oude worktrees: `--prune-safe` (verwijdert MERGED zonder uncommitted + broken). Optioneel: SessionStart-hook in `.claude/settings.json` die `--warn-age 3` draait.

---

## Open ADR-punten

- **ADR-008 §13.2**: content-pattern-based VERIFY-checks (open punt sinds 2026-05-15)
- **ADR-008 §18.7**: coordinator-pattern, sub-agent eigenaarschap voor verwijderingen, loop-limiet bij gap-events
- **ADR-019**: `anchor_propagation_log` veld dat een 1.5.I-agent introduceerde — niet in schema 1.5 gedocumenteerd, te normaliseren. Plus: records-API resolve disk-pad tegen daemon-known repo-root (maakt worktree-veilig).
- **ADR-022** (Vraag-herinterpretatie herinnering-stijl) — status Draft/experimenteel

---

## Doorlopend — Opkuis na repo-verhuizing (2026-05-25)

Status bij verhuizing `~/Documents/ITAA/certificaid` → `~/Development/certificaid`: 5 commits gepusht (granulariteit-ADR-030, wave-2-prompts, wave-2-beschrijven-output 207 records, bronnen-uitbreiding PO 2.x/3.0/4.0, content-updates voorbeeldexamens). De volgende untracked-bestanden zijn **niet** mee gegaan in die commits — voor elk een open beslissing vóór ze landen of weg gaan:

### Generated work-folders — gitignore of tracken?

- `data/exam_focus/` — examenfocus-bootstrap-JSONs per voorbeeldexamen-vraag (vermoedelijk gegenereerd door `tools/examen/`). Tellen ze als input voor examenpatronen-laag (commit) of als per-run-output (gitignore)?
- `data/extractie/_bundles/`, `data/extractie/wave-2/` — wave-2 werk-artefacten (bundle-rapporten, log-files). Gitignore-kandidaat.
- `data/qa/` — onbekend, nieuw pad (let op: `data/etl/qa/` is wél gitignored — andere folder).

Eerste actie volgende sessie: `ls -R data/exam_focus data/extractie/_bundles data/extractie/wave-2 data/qa | head -50`; per folder bepalen wat het is en `.gitignore` aanpassen of `git add` doen.

### Losse docs — superseded of nog actief?

Pre-cleanup sparring/design-docs (timestamp mei 17-19, predateert Fase 9 opkuis van 2026-05-23 die `roadmap.md → TODO.md` mergede). Geen daarvan is referenced vanuit CLAUDE.md of een ADR:

- `docs/roadmap.md` — commit `d2d60a49` mergede dit document in TODO.md en verwijderde het. De huidige untracked-versie is een lokale resurrectie. **Actie**: vergelijk inhoud met huidige TODO.md; ofwel verwijderen (`git clean -f docs/roadmap.md`), ofwel als referentie naar `docs/adr/archive/` verplaatsen.
- `docs/sessie-2026-05-19-bronnen-uitbreiding.md` — **schendt doc-discipline** (CLAUDE.md: "Handoff / sessie-md ... Bestaat niet"). Bevat substantieve bronnen-uitbreiding-info per PO. **Actie**: relevante info redistribueren naar Fase 2 hierboven en/of een nieuwe ADR-draft voor bronnen-strategie; dan verwijderen.
- `docs/po-builder.md`, `docs/po-1.1-doorloop-prep.md`, `docs/bronnen-pipeline.md`, `docs/fisconet-mcp-strategie.md`, `docs/implementation-backlog.md`, `docs/examenpatronen-ontwerp.md` — pre-Fase-9 sparring-docs. Per doc beslissen: nog active werkdoc → committen + linken vanuit CLAUDE.md/TODO.md; superseded → verwijderen.

### Wave-2 in vlucht — sync-status

De 207 gecommitte records zijn schema-2.1-v1.5-output van rolling sub-agents (`beschrijven`-operatie, aanvullend-modus, confidence `verondersteld`/`betwijfeld`). Maar:

- **records_api.py-bypass**: agents schreven direct naar disk i.p.v. via `save_record()`. Daardoor zijn RAG (`data/rag/main/`) en `content/concepten/` mogelijk out-of-sync met de huidige record-snapshots. Reindex/render verifiëren in nieuwe sessie.
- **Wave-2 zelf**: niet 100% afgewerkt. De 396-records-queue is groter dan 207 gecommitte changes; 189 records nog niet aangeraakt of nog onderweg. Status bij hervatting: queue herbouwen via stap 4 uit `prompts/sessies/wave-2-launch.md` en doorgaan.
- **Pass 2 (`accountant_perspectief`)** nog niet gestart.

### Records-API integriteit-check

Na de records-bypass: `python3 -m tools.lib.records_api --audit-parity` draaien om disk ↔ RAG ↔ content drift te kwantificeren, vóór render-laag-revisie (Fase 1.2) start.

---

## Tarief-records (ADR-026) — stand 2026-05-30

**Pijplijn-status**: volledig operationeel (schema 1.0 · `tarieven_api` · MCP-server `certificaid-tarieven` · `chunk_pdf` chunker · 2 prompts v1). Cijferzakboekje 2026 (196 pagina's) volledig gechunkt naar `data/tarieven/pages/`.

**82 records geschreven via 8 parallel Sonnet-subagents** (allemaal draft, geen trust):

| Cluster | Aantal | Bron |
|---|---|---|
| Drempels (art. 1:24/1:25/1:26 WVV) | 3 | RAG (CBN 2024/07 + MvT-WVV) |
| PB-tariefschijven (aj 2024-2027) | 4 | PNG p70 + WIB92 art. 130 |
| BTW-cluster | 6 | PNG p14-p27 + KB nr. 20 + WBTW |
| Rechtspersonenbelasting | 2 | PNG p133-p134 + WIB92 art. 225/220 |
| Erven en schenken (3 gewesten × 2) | 6 | PNG p29-p41 + W.Reg + VCF + W.Succ |
| Onroerend goed (OV + reg. 3 gewesten) | 6 | PNG p43-p55 + VCF + W.Reg |
| PB eerste helft (kredieten, vrije sommen, beroepskosten, ...) | 13 | PNG p72-p105 |
| PB tweede helft (VAA, RV, voorafbet., cheques, ...) + CO2-taks + lichte vracht | 20 | PNG p106-p131 + p185-p186 |
| SZ-werknemers + SZ-zelfstandigen + VenB + Vennootschapsrecht-overige | 22 | PNG p137-p177 |

**Confidence-verdeling**: 78× ⚖️ (grounded), 4× 🤖 (complexe samengestelde tabellen).

**Verify-pass — TE DOEN** (open punt):
- Verify-subagents per cluster (`prompts/tarief-verify-v1.md`) — cijfers kruisen tegen tweede primaire bron + `mark_trusted` waar volledig match
- Open review-flags per record gedocumenteerd in `extract_provenance` van elk JSON-record. Bekendmaakte aandachtspunten:
  - BTW-drempels: OSS-uniforme €10.000 vs. Cijferzakboekje legacy €35.000 nationaal
  - BTW-boetes: KB nr. 44 toont oude bedragen vs. Cijferzakboekje escalatie €500/1.250/2.500/5.000
  - PB Belastingvrije sommen: discrepantie aj 2025 vs aj 2026 voor "kind ten laste van alleenstaande"
  - VenB-basis: bezoldigingsdrempel €45.000→€50.000 per 01.01.2026 (wetsontwerp hangende?)
  - Indexcoëfficiënt KI 2,3000 aj 2026: bron BS niet RAG-geverifieerd
  - Records 🤖: `tarief-pb-overige-belastingverminderingen`, `vaa-overige-leningen`, `publicatietarieven-vennootschappen`, `vergelijkende-tabel-vennootschapsvormen`

**Niet-geëxtraheerde TOC-entries** (bewust geskipped — examen-marge):
- H I BTW-agenda (p11-p13) — dagprogramma, geen records-waardig
- H IV Personeel (p57-p69) — arbeidsrecht-tekst (opzeggingstermijnen, klein verlet, ...) — concept-record-werk, geen tarief-tabel
- H XI Verkeer: BIV per gewest (p179-p183) + verkeersbelasting per gewest (p189-p195) + brandstof (p184) + kilometerheffing (p187) — examen-marginaal, kan later

**MCP-server activeren**: nieuwe Claude Code-sessie → `.mcp.json` boot `certificaid-tarieven` server → 82 records bevraagbaar via `mcp__certificaid-tarieven__zoek_tabellen`.

**Geen content/-render**: tarief-records leven uitsluitend op disk + via MCP. Leerstuk-auteurs raadplegen ze tijdens schrijven; stagiairs gebruiken het Cijferzakboekje zelf als leeslaag. Leerstuk-wikilinks naar `[[tarieven/...]]` worden teruggedraaid waar ze niet structureel zinvol zijn.

---

## Onderhoud van deze TODO

- Voltooid werk verdwijnt hier (geen "Fase X — klaar"-eilanden). De rationale leeft in ADRs; de uitvoering in git-history.
- Nieuwe taak: voeg toe aan correcte fase, of "Doorlopend" als hij niet onder een fase past.
- Diepere details: link naar ADRs of werkpakket-specs — geen content-duplicatie.
- Bij grote sessie-shifts: actualiseer "Laatste update" datum.
