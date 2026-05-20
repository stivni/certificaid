# Sessie-handoff 2026-05-21 — Schema 2.0 + Fase 2-launch

**Voor**: nieuwe Claude Code-sessie die de schema 2.0 herextract voortzet
**Status bij handoff**: alle infrastructuur staat; pilot Wave 0 niet gestart; bronnen-werk loopt parallel (user)
**Examen-deadline**: ca. 2026-05-30 — krap maar haalbaar via parallelle subagent-fleet

---

## TL;DR voor de nieuwe sessie

1. Lees [ADR-025](adr/ADR-025-schema-20-didactische-conceptlaag.md) — schema 2.0 spec
2. Lees [pilot-fase2-pipeline.md](pilot-fase2-pipeline.md) — operational plan
3. Bekijk een referentie-mockup: [content/experiment/obligatielening-v7.md](../content/experiment/obligatielening-v7.md)
4. Verifieer MCP-server: `/mcp` slash-command — `certificaid-rag` moet actief zijn
5. Volgende concrete stap: skeleton-voorstel-run op PO 1.1 via Opus-subagent met [prompts/skeleton-voorstel-v1.md](../prompts/skeleton-voorstel-v1.md)

---

## 1. Waar we staan in de reis

### Wat al achter ons ligt

- **Mockup-cyclus** (2026-05-20/21): 8 markdown-mockups in `content/experiment/` om empirisch schema 2.0 te valideren — instrument, operatie, regime, ratio, kader (3), familie (3)
- **ADR-025** geschreven met volledige schema 2.0-spec
- **EXTRACT v5 + VERIFY v3 + skeleton-voorstel-v1** prompts klaar
- **Archief-script** getest (66 records voor PO 1.1)
- **MCP-server** (`certificaid-rag`) gebouwd + `.mcp.json` config live + preload-thread
- Alles gecommit en gepushed op `main`

### Wat NU klaar staat voor launch

- Pilot Wave 0 op PO 1.1: skeleton-voorstel-run als eerste echte test van het systeem

### Wat in parallel loopt (user)

- Bronnen-werk: Cijferzakboekje + extra fiscale bronnen (gebruiker doet zelf; via bestaande ETL-pipeline)

### Wat NIET gestart is

- Skeleton-voorstel-run (wacht op nieuwe sessie zodat MCP geladen wordt)
- Wave 0 launch
- VERIFY-pass uitvoering
- Render-laag-update voor collapsibility (parallel toekomstig werk)

---

## 2. Belangrijkste design-beslissingen (en waarom)

### Schema 2.0 i.p.v. 1.7

**Beslissing**: major-bump, niet incremental.
**Reden**: nieuwe top-volgorde + rol × perspectief + element-vocabulaire + kader/familie kinds zijn fundamenteel — geen velden-toevoeging maar een **didactische herframing**. ADR-025 §gevolgen.

### Rol × perspectief als verplichte structuur

**Beslissing**: tweelaagse matrix-sectie (klant-perspectief × accountant-hoed).
**Reden** (uit brainstorm 2026-05-21): de accountant zet verschillende **hoeden** op voor verschillende klanten (adviseur · boekhouder · controleur · fiscaal · begeleider · …). Empirisch getest op obligatielening: matrix is dun-bezet (~30-40% cellen vol) en geen overlap. Geen schema-jargon ("rol_van_de_accountant" als publieke sectienaam, niet "perspectieven_per_actor").

### Element-vocabulaire (inhoud_type + weergaven, één-op-veel)

**Beslissing**: scheiding tussen *wat is dit conceptueel* (`inhoud_type`) en *hoe tonen we het* (`weergaven[]`).
**Reden**: een mechanisme als "disagio" toont natuurlijk via berekening + boeking + balans-snapshot — drie weergaven van één concept-eenheid, niet drie losse rubrieken. Render-laag kiest per weergave-type de component.

### Vijfde confidence-label ❌ tegenstrijdig

**Beslissing**: naast ⚖️ · 🔗 · 🧭 · ⚠️ ook ❌ `tegenstrijdig`.
**Reden**: ⚠️ = nog niet gecheckt (mogelijk OK); ❌ = gecheckt en fout volgens bron. Fundamenteel verschillende actie-eis. User-feedback: "🧭 → ⚠️ bij tegenspraak is te zwak; dat is fout".

### 🧭-gradatie-regel

**Beslissing**: vuistregels mogen voor *strategisch advies* (wanneer kies je · voor wie · hoofdrisico/voordeel · speelruimte · valkuilen-in-uitvoering), niet voor *procedures · cijfers · wettelijke voorwaarden · rekening-codes · tarieven*.
**Reden**: anders LLM-hallucinaties verkocht als wettelijke regels. User-feedback: bewust koerswijziging om fiches voller te maken zonder kwaliteit te verliezen.

### Cross-PO-completeness per record

**Beslissing**: bij eerste aanraking van een concept (bv. `obligatielening` in PO 1.1) behandelt de agent ALLE perspectieven (boekhoudkundig + fiscaal + audit) in één pass.
**Reden**: voorkomt re-extract-waste. User-formuleerde dit expliciet als regel.

### Lock-based parallelisatie zonder overlap

**Beslissing**: orchestrator wijst elk **2.0-doel-fiche** aan precies één agent toe. First-write-wins voor ontbrekende dependencies.
**Reden**: geen twee agents werken aan dezelfde fiche. Cross-PO-completeness binnen één agent garandeert volledigheid. Eventuele rommel → Fase 3.

### Top-down skeleton-voorstel (NIET vanuit oude records)

**Beslissing**: stap 0 vertrekt vanuit TDKs + bronnen + patroon-mockups; bestaande v1.x-records zijn alleen content-input voor extract-agents (geen structurele input voor skeleton).
**Reden**: v1.5/1.6 had overfragmentatie; vertrekken vanuit oude records besmet het 2.0-ontwerp met v1-framing. User-feedback: "kunnen we niet vragen welke concepten die gewoon herkent in alle gekregen context?".

### Geen formele mapping oud→nieuw

**Beslissing**: na wave-approval worden orphan v1.x-records gewoon gedeleted via records-API. Geen formele "mapping"-administratie.
**Reden**: skeleton-voorstel hoeft niet structureel afhankelijk te zijn van oude records. Archief blijft als snapshot voor herstel.

### Examen-vragen NOOIT als extract-input

**Beslissing**: hard rule (uit EXTRACT v4 behouden + expliciet in v5).
**Reden**: circulair (je extract wat in de test staat ipv wat erin hoort). Conceptlaag moet tijdloos en domein-onafhankelijk zijn. VERIFY mag ze post-hoc gebruiken voor dekking-toets (test-time, geen extract-driver).

### VERIFY v3 = soft guidelines, geen blockers

**Beslissing**: VERIFY schrijft suggesties, blokkeert geen records.
**Reden**: user expliciet: "ik heb schrik om het té dicht te timmeren". Dichtgetimmerd regelvolg-gedrag ondergraaft didactische kwaliteit.

### MCP-server voor on-demand retrieval

**Beslissing**: 5 tools via MCP i.p.v. vooraf-gebundelde initial-ctx.
**Reden**: 30k tokens chunks/matches pre-loaded werd ineffectief; agents gebruikten 20-30%. MCP geeft focused queries, iteratieve verfijning, cross-record awareness tijdens schrijven. Voor 460+ records significante token-besparing.

### Skeleton-voorstel gebruikt ALLE non-deprecated mockups

**Beslissing**: agent krijgt verwijzing naar `content/experiment/`-folder en kiest zelf relevante mockups.
**Reden**: user: "we hebben er meer, waarom geven we ze niet allemaal mee?". Niet parsimonous zijn.

### Records-API soft-validator geschrapt

**Beslissing**: geen schema-validator op records-API niveau.
**Reden**: soft-warnings zonder gevolg = waste. VERIFY-pass dekt het al.

### Kind als open tag-set, geen enum

**Beslissing**: `kind`-veld is open string; nieuwe waarden door agent voor te stellen via gaps.json.
**Reden**: voorkomt overstrenge typering die schema 1.6 al zwaar maakte.

### Niet-transitief in data, transitief in render

**Beslissing**: `heeft_lid` declareert alleen direct-onder; render-laag traverseert recursief.
**Reden**: kader-fiche hoeft niet alle eindbladen te kennen; render bouwt boomweergave uit hop-by-hop edges.

---

## 3. Inventaris artefacten (volledige lijst)

### Documentatie

| Bestand | Inhoud |
|---|---|
| [docs/adr/ADR-025-schema-20-didactische-conceptlaag.md](adr/ADR-025-schema-20-didactische-conceptlaag.md) | Schema 2.0 spec |
| [docs/adr/INDEX.md](adr/INDEX.md) | ADR-overzicht + taak→ADR mapping (bijgewerkt) |
| [docs/pilot-fase2-pipeline.md](pilot-fase2-pipeline.md) | Operational plan Fase 2 |
| [docs/sessie-2026-05-21-schema-20-handoff.md](sessie-2026-05-21-schema-20-handoff.md) | Dit document |

### Prompts

| Bestand | Doel |
|---|---|
| [prompts/concept-extractie-v5.md](../prompts/concept-extractie-v5.md) | EXTRACT v5 — schrijft 2.0-records via MCP-tools |
| [prompts/concept-verify-v3.md](../prompts/concept-verify-v3.md) | VERIFY v3 — soft guidelines |
| [prompts/skeleton-voorstel-v1.md](../prompts/skeleton-voorstel-v1.md) | Stap 0 — pre-pilot consolidatie-voorstel |
| [prompts/concept-extractie-v4.md](../prompts/concept-extractie-v4.md) | Vorige EXTRACT (schema 1.5/1.6) — referentie |

### Code

| Bestand | Doel |
|---|---|
| [tools/extractie/archive_voor_migratie.py](../tools/extractie/archive_voor_migratie.py) | Snapshot v1.x records vóór herextract |
| [tools/extractie/mcp_server/server.py](../tools/extractie/mcp_server/server.py) | MCP-server certificaid-rag |
| [tools/extractie/mcp_server/README.md](../tools/extractie/mcp_server/README.md) | MCP-server documentatie |
| [.mcp.json](../.mcp.json) | Project-MCP-config (server-registratie) |

### Referentie-mockups (in `content/experiment/`)

| Bestand | Kind | Wat het toont |
|---|---|---|
| `obligatielening-v7.md` | instrument | Canonical template — rol × perspectief volledig + MCP-aware |
| `obligatielening-v4.md` / `v5` / `v6` | instrument | Vergelijking-versies (boekingen-plaatsing) |
| `solvabiliteitsratio-v2.md` | ratio | Drempels conceptueel + acties per rol |
| `solvabiliteitsratio-v1.md` | ratio | Eerste versie (vergelijking) |
| `inkoop-eigen-aandelen-nv-v1.md` | operatie | Wettelijke voorwaarden + procedure |
| `vvprbis-v1.md` | fiscale-regeling | Voorwaarden + tarieven + niet-van-toepassing-op |
| `jaarrekeninganalyse-v1.md` | kader | Generieke discipline + cross-ratio-patroon |
| `uitkering-aan-aandeelhouders-v1.md` | kader | Keuze-tussen-alternatieven |
| `lange-termijn-financiering-v1.md` | kader | Schuld vs EV + matching looptijd |
| `leasing-v1.md` | familie | Substance-over-form + vergelijkingsmatrix |
| `financiele-leasing-v2.md` | instrument (lid) | Kwalificatie-criteria centraal |
| `operationele-leasing-v1.md` | instrument (lid) | Negatieve definitie + IFRS 16-waarschuwing |
| `obligatielening-v2-mockup.md` | index | Vergelijkingspagina van obligatielening-versies |

---

## 4. Hoe een nieuwe sessie verder gaat

### Stap 0 — Sessie-start checks

1. **Lees CLAUDE.md** (status-update over schema 2.0 bovenaan)
2. **Verifieer MCP**: `/mcp` slash-command. `certificaid-rag` moet active zijn. Zo niet: project-MCP-permissie verlenen.
3. **Health-check MCP-tools** (één call om bge-m3 te warmen):
   ```
   check_record_bestaat("obligatielening") → {bestaat: true}
   ```

### Stap 1 — Skeleton-voorstel op PO 1.1

Launch Opus-subagent met:
- System-prompt: inhoud van `prompts/skeleton-voorstel-v1.md`
- Initial context: "Genereer skeleton-voorstel voor PO 1.1. Output naar `data/extractie/1.1/skeleton-voorstel-<timestamp>.md`."
- Tools: MCP `certificaid-rag` (alle 5)

Verwachte tijd: ~10-20 min Opus.
Output: markdown-rapport voor mens-in-de-loop review.

### Stap 2 — User reviewt skeleton-voorstel

Mens-in-de-loop. Belangrijke checks:
- Klopt de top-down identificatie van 2.0-fiches?
- Zijn kader-voorstellen pertinent?
- TDK-dekking volledig?
- Open vragen oplosbaar?

Aanpassingen via commentaar terug naar agent of direct in rapport.

### Stap 3 — Archief van v1.x records

```bash
python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1
```

Manifest in `data/concepten/_archive/v2.0-migratie/<timestamp>-po-1.1/_manifest.json`.

### Stap 4 — Wave 0 launchen (subagent-fleet)

Orchestrator-agent leest skeleton-voorstel-rapport, wijst doel-fiches toe aan ~6-10 parallel Opus-subagents (4-5 fiches elk).

Per subagent:
- System-prompt: inhoud van `prompts/concept-extractie-v5.md`
- Toegewezen fiche-lijst
- Tools: MCP `certificaid-rag` + records-API write-toegang
- Cross-PO-completeness: behandel alle perspectieven van toegewezen fiche

Verwachte tijd: ~3-6u parallel.

### Stap 5 — VERIFY-pass

Sonnet-subagent met `prompts/concept-verify-v3.md`. Schrijft suggesties naar `gaps.json` met severity `suggestion` of `error` (bij `tegenstrijdig`).

### Stap 6 — Orphan-cleanup

Helper-script nog te bouwen: `tools/extractie/cleanup_orphans.py` — vergelijkt archief-snapshot vs huidige records; orphans worden `delete_record()`'d.

### Stap 7 — Steekproef mens-in-de-loop

10% van records (5 uit ~33): handmatig lezen in Quartz-render, vergelijken met archief-versie. Bevestig kwaliteits-stijging.

### Stap 8 — Beslismoment

- ✅ Doorgaan met Wave 1 (volgende PO)
- 🔁 Iteratie: prompt-aanpassing + nieuwe pilot-wave
- ❌ Schema-revisie: pilot onthult fundamentele tekortkoming

---

## 5. Wat NIET te doen

| Anti-pattern | Waarom |
|---|---|
| Examen-vragen als extract-input gebruiken | Circulair; conceptlaag moet tijdloos zijn |
| 1-op-1 conversie v1.5/1.6 → 2.0 | Rol × perspectief is niet uit 1.5 af te leiden; lege secties |
| `--no-verify` zonder expliciete user-permissie | CLAUDE.md regel; user moet één-keer toestemming geven |
| Schema-validator dichttimmeren | VERIFY = soft guidelines, geen blockers |
| MCP-tools voor schrijfacties | save_record blijft via records-API direct |
| Schema-jargon in body van fiches | `node_type`/`kind`/`linked_anchors` alleen in frontmatter |
| Rekening-codes in "Hoe het werkt" | Alleen in Rol > Boekhouder (uitvoering) |
| Examen-context in body ("in examen-context: ...") | Fiches zijn naslagwerk voor elke accountant |
| Mappen op v1.x in skeleton-voorstel | Top-down vanuit TDKs + bronnen + mockups |
| Stille overschrijving van confidence-history | `_provenance.confidence_history[]` bijhouden |
| Familie en kader verwarren | Familie = leden met gedeelde mechaniek; kader = cross-cutting denkraam |

---

## 6. Open vragen / onzekerheden

| Vraag | Notes |
|---|---|
| Render-laag-update voor collapsibility | Parallel werk; default open 1-2-3-4, default dicht 7-8-9-10 |
| Browser-state voor user-confidence (vrouw-idea) | Bij render-laag-werk |
| Familie vs kader edge cases | Bv. leasing-familie zit IN lange-termijn-financiering-kader — werkbaar maar render-test nodig |
| Drempel "te veel 🧭" | 40% nu; empirisch tunen na pilot |
| Wave-overlap tussen PO's | Eerste PO waar concept aangeraakt wordt = owner; volgende waves slaan over |
| Cijferzakboekje-bron-format | User werkt eraan; pas geladen → claim-validatie-pass kan ⚠️/❌ → ⚖️ |
| Confidence-history bij refinement | Append-only lijst in `_provenance.confidence_history[]` |
| Cleanup-orphans script | Nog te bouwen voor wave-completion |
| Render-templates voor element-types | tools/leermateriaal/templates/ updaten — TODO Fase 2 of Fase 3 |

---

## 7. Strategische context

### Waarom dit werkt voor de examen-deadline

- Cross-PO-completeness vermindert herwerk
- Lock-based parallelisatie schaalt: 8 concurrent waves × 50 records = 400 records/nacht
- 24-36u Fase 2-doel haalbaar als pilot succesvol
- Fase 3 refinement loopt door zonder examen-druk

### Wat zou kunnen mislukken

| Risico | Mitigatie |
|---|---|
| EXTRACT v5 produceert dunne fiches | Pilot Wave 0 vangt het; prompt-aanpassing voor Wave 1+ |
| MCP-server crash tijdens lange runs | Lazy-init + retry logic; subagent kan herstart-poging |
| Hallucinatie-spike in 🧭-claims | VERIFY hallucinatie-detectie + steekproef |
| Records-API timeout bij batch | Bestaande cold-start-mitigatie (60s eerste call) |
| Render-laag-discrepantie | Markdown wordt automatisch overschreven door save_record() |

### Waar je vragen aan user moet stellen

- Wave-acceptatie-criterium (kwaliteits-drempel voor "deze wave goed genoeg")
- Wanneer kader-fiches schrijven (vóór leden of via cross-wave?)
- Hoeveel handmatige review per wave (10% standaard maar tunable)
- Render-laag-prioriteit (parallel met Fase 2 of na?)

---

## 8. Communicatie-stijl van user (kort)

- **Scherp en kritisch** — vragen lossen geen problemen op, ze ontmaskeren ze
- **Top-down denken** — kader > specifiek, niet specifiek > kader
- **Pragmatisch over speed** — wil tempo, accepteert imperfectie als refinement-pad bestaat
- **Eerlijk over onzekerheid** — apprecieert "ik weet het niet" boven "ik gok"
- **Niet té veel uitsplitsen** — vermijdt overfragmentatie
- **Examen-deadline-realistisch** — 9 dagen tot examen; doe wat moet
- **Bronnen-werk parallel** — gebruiker werkt zelf aan Cijferzakboekje + fiscale bronnen
