# Certificaid — Openstaand werk

Eén bron voor *wat er nog moet gebeuren*. Voltooide fases leven niet hier — git-history en ADRs zijn de plek voor "wat hebben we gedaan en waarom".

**Laatste update**: 2026-05-26 (controle-opdracht-cluster + interne-controle-cluster afgewerkt; discipline hernoemd `audit-en-assurance` → `controle`; shared-records-pattern formeel)

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
- **Granulariteit-skelet** — concept-tree-opbouw per cluster ([`docs/granulariteit-skelet.md`](granulariteit-skelet.md) + [ADR-030](adr/ADR-030-granulariteit-typologie.md)). Sparring-werk dat vooraf gaat aan record-herstructurering. **Voltooid**: mobiliteit · kapitaalstructuur · werknemers-vergoedingen · overdracht-onderneming · schuldfinanciering · **controle-opdracht** (laag-2 sub-Kader `controle`, PO 1.6, 2026-05-26) · **interne-controle** (laag-2 sub-Kader `controle`, PO 1.7, 2026-05-26 — incl. discipline-rename `audit-en-assurance` → `controle` + 3 shared records `coso-framework` · `cyclus-analyse` · `auditcomite`). **Shared-records-pattern**: records met meerdere thema's, zichtbaar in meerdere clusters, geen content-duplicatie. **Open clusters**: winstuitkering · reorganisatie · fiscale-voordelen-vennootschap · anti-misbruik · insolventie · beroepsbeoefening · loon-en-payroll (K-techniek) · vennootschap-typologie (incl. `vennootschap-groottecategorieen` — OP-EC.7) · 3 overige sub-Kaders van `controle` (`beoordelings-opdracht`, `isae-opdrachten`, `overeengekomen-procedures` — kleiner werk per stuk). **Per voltooide cluster**: test-case-validatie via examen-vragen (6 vragen per cluster, 2026-05-26) bevestigt tree-dekking vóór mapping-fase. **Mapping-fase** (post-skelet): bestaande 396 records herstructureren naar skelet — incl. audit-perspectief op 8 Gebeurtenis-records voor bijzondere revisor-verslagen (OP-EC.E) + COSO/cyclus-record-absorptie naar shared records (OP-IC.E) + `-cluster`-naam-smell-scan over alle records.

---

## Fase 1 — Schema 2.1 v1.5 + extractie v6 + render-laag (in uitvoering)

**Doel**: nieuwe data-laag (schema 2.1 v1.5) + multipass-operaties-pipeline (extractie v6) + render-laag-revisie. Vervangt schema 2.0 + EXTRACT v5.

**Canonieke documenten**:
- [ADR-029](adr/ADR-029-schema-21-operaties-model.md) — design-rationale + operations-model + v1.0 → v1.5 changelog
- [`docs/schema-v15-besluit.md`](schema-v15-besluit.md) — geconsolideerde spec (21 besluiten + finale structuur)
- [`data/concepten/schema-2.1.schema.json`](../data/concepten/schema-2.1.schema.json) — bron-van-waarheid
- [`docs/render-laag.md`](render-laag.md) — render-laag werkpakket-spec
- [`prompts/operaties/`](../prompts/operaties/) — 5 slanke operatie-prompts

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

## Onderhoud van deze TODO

- Voltooid werk verdwijnt hier (geen "Fase X — klaar"-eilanden). De rationale leeft in ADRs; de uitvoering in git-history.
- Nieuwe taak: voeg toe aan correcte fase, of "Doorlopend" als hij niet onder een fase past.
- Diepere details: link naar ADRs of werkpakket-specs — geen content-duplicatie.
- Bij grote sessie-shifts: actualiseer "Laatste update" datum.
