# Examenvraag-antwoord-pipeline — werkpakket-spec

**Status**: POC actief op PO 1.4 (6 vragen, 4 unieke topics na dedup-check).
**Doel**: pasklare student-ready antwoorden op alle voorbeeldexamen-vragen, RAG-gegrond aan bronnen, met per-claim confidence (schema 2.1 v1.5 tokens).
**Laatste update**: 2026-05-26.

Dit document is een werkpakket-spec (per CLAUDE.md doc-discipline) — leeft tot het werkpakket klaar is. Beslissingen die stabiel zijn, migreren straks naar een ADR. Dagelijkse werk-status in [`TODO.md`](TODO.md).

---

## Architectuur — drielagig

Per examenvraag:

1. **Interpretatie** (bestaand, schema 1.2) — `data/programma/examen_vragen/_interpretaties/<examen>/<vraag>.json`
   - Visie-bron: PNG-segmenten + OCR-tekst
   - Velden: `vraag_onderwerp`, `themas`, `programmaonderdeel_ids`, `context_blokken[]`, `vragen[]`, `kwaliteits_flags`
   - Vision-her-interpretatie verplicht bij `kwaliteits_flags: ["tabel_in_pdf_zichtbaar"]` of vraagstelling met "(zie schema)" / "onderstaande tabel". Tekst-only interpretatie van schema/tabel kan fundamenteel fout zijn — zie vr8-incident (pijlrichtingen verkeerd, antwoord volledig fout).

2. **Antwoord** (schema 1.1) — `data/programma/examen_vragen/_antwoorden/<examen>/<vraag>.json`
   - Hier zit het LLM-werk. Sonnet-agent met MCP `certificaid-rag`.
   - Per deelvraag `vraag_antwoorden[].blokken[]` met typed-blok-types.
   - Per blok `confidence` + `bron_refs`.

3. **Merge + render** (schema 4.0, bestaand) — `_merged/<examen>.json` → `content/voorbeeldexamens/po-<code>.md`
   - Tooling: `tools/examen/merge_examen_artefacten.py --alle` + `tools/examen/render_merged_v4.py --po <code>`.

---

## v3 antwoord-prompt-regels (canoniek)

**Tool-budget** (gevonden via POC):
- Max 4 RAG-calls per agent (parallel batches; geen sequentiële 17-call cascade).
- `zoek_bronnen`: `rerank=False` (default; spaart RAM/tijd), `top_k=5`.
- Geen self-verifier-pas in dezelfde agent (verdubbelde tijd, geen kwaliteitswinst).

**Blok-volgorde verplicht**:
1. **HET ANTWOORD ZELF** — type `conclusie` (1 zin / 1 cijfer) of `tabel` (ingevulde tabel) of `definitie`. Eén blok, kort en scherp.
2. **REDENERING** — `berekening` / `motivatie` / `opsomming`. Compact, geen herhaling van rekenregels.
3. **EXTRA INFO (optioneel)** — `motivatie` met `kop: "Vermeldenswaard"` / `"Valkuil"` / `"Nuance"`. Eén meerwaarde-feit (uitzondering, veelgemaakte fout, verband met ander concept).
4. **GRONDSLAG** — `grondslag` met compacte wettelijke verwijzingen.

**Compactheid**: lengte schaalt aan vraag-aard. Feitelijke vraag "Hoeveel maanden?" → 1 conclusie + 1 grondslag. Geen pedagogische essays.

**Andere disciplines**:
- `antwoord_model: "claude-sonnet-4-6"` (correcteren bij oude records die "opus" zeggen).
- `bron_refs` = enkel bestand-pad (bv. `resources/bronnen/wetteksten/KB-WVV-2019.md`). GEEN `#anchor`-fragmenten verzinnen.
- PNG-Read verplicht bij visuele vragen (tabellen, schema's).
- Geen wetsinhoud zonder bron. Bij twijfel → confidence verlagen of skip.

---

## Confidence-tokens — schema 2.1 v1.5

| Token | Icoon | Wanneer |
|---|:---:|---|
| `geciteerd` | 📖 | (Quasi-)letterlijk in bron, incl. parafrase |
| `afgeleid` | 🔗 | Logische conclusie uit ≥1 bronnen |
| `verondersteld` | 🤖 (AI) / 🧠 (mens) | Aanname met redelijke zekerheid, geen citaat |
| `betwijfeld` | ❓ | Expliciete twijfel |
| `weerlegd` | ❌ | Bron tegenspreekt, claim nog niet gecorrigeerd |

**Backward-compat in render** (`tools/examen/render_merged_v4.py`):
- `grounded` → 📖 (mapt naar `geciteerd`)
- `inferred` → 🔗 (mapt naar `afgeleid` — meestal wel uit bronnen geredeneerd)

**Render-dedup**: blok-niveau icoon wordt overgeslagen als de tekst al eindigt op een confidence-marker. Voorheen kreeg je `(...). ⚖️ ⚖️` (één van agent, één van renderer).

---

## Visuele vraag-elementen — render-laag-handlers (deze sessie toegevoegd)

- **`groepsschema`-context-blok** → Mermaid `graph TD` (Quartz OFM heeft `mermaid: true` default). Knopen + relaties met percentages. Tekst-fallback eronder voor non-mermaid lezers. Voorbeeld: vr8 met M→A 70%, M→C 30%, A→B 60%, C→B 20%.
- **Tekst-fallback voor typed blokken**: `definitie`, `berekening`, `boeking`, `procedure`, `tabel`, `opsomming` renderen nu de `tekst`-field als typed velden (`formule`/`stappen`/`lemma`/`uitleg`/`rows`/...) leeg zijn. Schema-mismatch tussen schema 1.1 (`tekst` als markdown) en ADR-023 typed schema (`formule`/`stappen`/...) is daarmee defensief opgevangen.

**Bekend visueel-rendering-risico**: Mermaid binnen een Obsidian-callout (`> [!question]-`) — `> `-prefixes op elke regel kunnen de Quartz mermaid-parser theoretisch hinderen. Live-preview-test vereist.

---

## Performance — gemeten

| Setup | Tijd/vraag | RAG-calls | Notes |
|---|---:|---:|---|
| POC pas 1 (geen budget, self-verifier in same agent) | 23 min | 17 | Te traag, te duur |
| POC v2 (budget 4 calls, geen self-verifier, parallel) | 30-90 sec | 2-5 | Werkbaar |
| POC v3 (+blok-volgorde, +"vermeldenswaard") | 40-120 sec | 1-5 | Quality-uplift, geen tijd-cost |
| 6 parallel agents wall-clock | ~90-120 sec | n.v.t. | Voor 1 PO klaar in <2 min |

**Projectie 293 vragen** (alle PO's): parallel-batched per PO, ~20-40 min wall-clock totaal.

---

## Dedup-strategie (in opbouw)

**Vondst**: 33% duplicaten in PO 1.4 alleen.
- 2013-1-vr7 + 2014-1-vr7 → zelfde antwoord "3 maanden afsluitingsdatum"
- 2013-2-vr8 + 2015-1-vr11 → zelfde "positief consolidatieverschil: definitie + 4 oorzaken"

Projectie corpus: 50-100 duplicaten over 293 vragen.

**Eindvorm (gekozen 2026-05-26)**:
- **Cluster-record** per onderwerp groepeert duplicaten. Veld `examen_voorkomens: [<vraag_id>, ...]`.
- **Frequentie = belangsmaat**: vragen die N keer terugkomen krijgen render-badge "N× bevraagd" → student weet welke onderwerpen prioritair zijn.
- **Eén antwoord per cluster**, vraag-fiches verwijzen ernaar (besparing op antwoord-werk).
- **Vraag-fiches blijven per examen** voor "ik wil examen X doorlopen"-use-case.

**Detectie-aanpak**:
1. `vraag_onderwerp`-string-similarity (gratis, vangt makkelijke gevallen)
2. bge-m3 embedding op `vraag_onderwerp + vraagstelling`, cosine > 0.85 = cluster-kandidaat
3. LLM-pairwise op borderline-paren

**TODO**: cluster-detectie script schrijven (zie TODO-lijst onderaan).

---

## Anti-patterns (POC-lessen)

| Anti-pattern | Symptoom | Mitigatie |
|---|---|---|
| 17 sequentiële RAG-calls | 23 min/vraag | Hard limiet 4 calls, parallel batches |
| Self-verifier in zelfde agent | Tijd × 2, geen meetbare quality-uplift | Skip; eventueel aparte verifier-pas later |
| Antwoord-essay voor feitelijke vraag | "3 maanden" → 5 alinea's | Lengte-discipline; blok-volgorde dwingt structuur |
| Tekst-only interpretatie van schema/tabel | Factually wrong answers (vr8 case) | Visuele markers → vision-her-interpretatie verplicht |
| Confidence-icoon dubbel | `(...). ⚖️ ⚖️` | Render-dedup (tekst-eind-check) |
| Schema-mismatch tekst-veld vs typed | Leeg gerenderd antwoord | Tekst-fallback in alle typed-blok-handlers |
| `bron_refs` met verzonnen `#anchor` | Broken links | Prompt-regel: enkel bestand-pad |
| `antwoord_model: "opus"` waar Sonnet draaide | Foute meta | Prompt-regel expliciet "claude-sonnet-4-6" |

---

## Bijproduct: kennisbank-leemtes gevonden tijdens POC

Bij vr8 (2014-1) faalden 2 `lees_record`-calls — records bestonden niet:
- `berekenen-controle-en-belangenpercentage`
- `kiezen-consolidatiemethode`

**Inzicht**: de antwoord-pipeline produceert als bijproduct een kennisbank-audit. Elke `lees_record`-fail of `zoek_concepten`-miss is een signaal voor de concept-extractie-fase. Niet automatisch loggen voor nu; user-observeerbaar via agent-rapporten.

---

## Open TODOs

### Direct (eerstvolgende sessie)
- [x] **Cluster-detectie script** — ✅ [`tools/examen/cluster_vragen.py`](../tools/examen/cluster_vragen.py) (bge-m3 via daemon, cosine ≥ 0.80, borderline 0.75-0.80), agent-review, [`tools/examen/apply_cluster_review.py`](../tools/examen/apply_cluster_review.py). Output: 11 clusters in 8 PO's. Renderer toont gecombineerde herkomst + 🔁-badge.
- [x] **Prompt v2.0** — ✅ [`prompts/modelantwoord-v1.md`](../prompts/modelantwoord-v1.md) herschreven naar v2.0 met alle POC-leerlessen.
- [x] **Visuele-vraag-detectie** — ✅ [`tools/examen/detect_visuele_vragen.py`](../tools/examen/detect_visuele_vragen.py) flagt 50 visuele vragen (17%) met `vision_review_nodig`-veld.
- [ ] **Re-run 6 PO 1.4 vragen met v2.0-prompt** voor visuele consistentie tussen inline tekst-iconen en blok-iconen (huidige antwoorden hebben nog ⚖️/🤖 in tekst; backward-compat in renderer maar gemengd).
- [ ] **Scaling-run**: alle 282 unieke vragen (na cluster-dedup), parallel batches per PO, prompt v2.0. Verwachte wall-clock: 20-40 min.

### Vervolg
- [ ] **Schema-veld voor "wetsletter ↔ doctrine"-nuance** — terugkerend patroon: feit zit niet in wetstekst maar in IFRS/doctrine/CBN-advies. Nu in ad-hoc `_poc_notitie`-velden, zou structureel veld moeten worden (bv. `grondings_caveat` per `vraag_antwoord` of nieuw confidence-token).
- [ ] **Bron_refs-validatie** — bestaan de paden die agents schrijven? Script dat alle `bron_refs` controleert tegen `resources/bronnen/` filesystem + bronnen-index.
- [ ] **Render-laag-revisie voor cluster-vragen** — render badge "N× bevraagd", lijst van examen-voorkomens.
- [ ] **Cluster-record-schema** — formaliseer `examen_voorkomens[]`, `cluster_id` op interpretatie.

### Bij scaling (na PO 1.4 pilot)
- [ ] Pre-fetch RAG-bundle (deterministisch script vóór agent-launch) als tijd-budget krap wordt.
- [ ] ADR-034 schrijven zodra POC stabiel is — examenvraag-antwoord-pipeline + RAG-grounding-regels + dedup-strategie.

### Bijproduct
- [ ] Twee ontbrekende competentie-records signaleren naar concept-extractie-laag: `berekenen-controle-en-belangenpercentage`, `kiezen-consolidatiemethode`.

---

## Verwijzingen

- Schema 1.1 spec: [`prompts/modelantwoord-v1.md`](../prompts/modelantwoord-v1.md) — let op: zegt nog "POC: geen RAG-laag aangesloten"; wordt vervangen door v4.
- Referentie-record: `data/programma/examen_vragen/_antwoorden/2024-1/2024-1-vr7A.json`
- Renderer: [`tools/examen/render_merged_v4.py`](../tools/examen/render_merged_v4.py) — laatste fixes (2026-05-26): tekst-fallback voor typed blokken, mermaid-output voor `groepsschema`, schema 2.1 confidence-tokens + render-dedup.
- Merger: [`tools/examen/merge_examen_artefacten.py`](../tools/examen/merge_examen_artefacten.py) — gebruik `--alle` om alle interpretaties op te nemen (niet de oude POC-subset).
- Gerelateerde ADRs: ADR-020 (modelantwoord-pipeline-architectuur), ADR-023 (gestructureerde antwoorden + vraag-v3.1), ADR-024 (visuele LLM-interpretatie), ADR-031 (PDF-vraag-isolatie + bbox-indent), ADR-032 (examen-vragen-render-per-programmaonderdeel).
- MCP-server: [`tools/extractie/mcp_server/`](../tools/extractie/mcp_server/) — `zoek_concepten`, `zoek_bronnen`, `lees_record`, `lees_anchor_bundle`.
