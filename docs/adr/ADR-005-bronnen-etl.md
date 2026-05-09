# ADR-005: Bronnen-ETL

**Status**: Draft
**Datum**: 2026-05-07 (gewijzigd 2026-05-08: §5 kwaliteits-gate uitgewerkt met trust-marker; 2026-05-09: §3 frontmatter `chunk:`-blok + §7 wettekst-hiërarchiedetectie; 2026-05-09 v2: §2 unified conversie-pipeline — patches geschrapt + 1-op-N compilatie + auto-trust workflow met agent-diff-review en sample-tracking)
**Vervangt**: archive/ADR-014 (oude ETL-pipeline), ADR-008 (bron_rol nu hier ingebed)

## Context

Bronnen komen uit verschillende kanalen (ejustice-PDF's, FOD-PDF's, CBN-website-HTML, BeExcellent-platform, ITAA-publicaties als PDF, IFAC-PDF's voor ISA/ISAE/ISRS) en hebben verschillende structuur (artikelen, secties, krantenkolommen, schema's). Doel: een **uniforme markdown-output** met behoud van structurele headings en tabellen, gestuurd door één configuratiebestand.

De vorige iteratie had een proliferatie van type-strings (`ejustice_nl`, `wib92`, `wetboek`, `split`, `skip`, ...) zonder duidelijke schema-discipline. Het ADR-017-extract-schema heeft dat al deels rechtgetrokken — die richting wordt hier voortgezet.

**Tweede pijnpunt** (vastgesteld 2026-05-09): de pipeline groeide tot ~23 ETL-scripts waaronder een reeks post-conversie patch-scripts (`inject_wettekst_headings.py`, `inject_norm_headings.py`, `fix_advies_artefacts.py`, `fix_norm_artefacts.py`, `split-kb-compilatie.py`). Conversie was niet idempotent: `convert.py` schreef ruwe markdown, daarna patchten meerdere scripts erin. Bij elke iteratie raakte de markdown verder af van de raw bron, git-diffs werden onleesbaar, regressies sloop in. Tegelijk: `WBTW-KB-compilatie.md` bevatte 32 KBs in één bestand én er waren 32 derived MDs als kopie — 33 bestanden voor 32 KBs, met split-script als enige link.

Tegelijk: regressies sluipen in. Nieuwe ejustice-snapshots breken de cleanup-pipeline op subtiele manieren (nieuwe paginavoetregel, gewijzigde TOC-format). Een **agent-gebaseerde QA-check** als gate boven op een golden-set vangt die regressies vóór ze de RAG-index bereiken.

## Beslissing

### 1. Enige bron van waarheid

`resources/source_config.yaml` met per bron:

```yaml
SourceName:
  bron_rol: itaa_lex | normatief | interpretatief | praktijkgids | formulier
  raw: resources/raw/wetteksten/X.pdf  # of source_url voor HTML
  output: resources/bronnen/wetteksten/X.md
  tags: [...]
  status: volledig | toc_only | nieuw
  extract:
    method: pdftotext_ejustice | pymupdf4llm | custom_wib92 | custom_wetboek |
            justel_html | cbn_advies_html | pdftotext_compilatie_btw_kb | handcrafted
    params: { ... }   # methode-specifiek
```

`extract.method: handcrafted` vereist `params.reason` — geen ongedocumenteerde uitzonderingen.

**1-op-N output (compilatie-PDFs)** — als één raw-bestand meerdere zelfstandige
bronnen bevat (bv. `WBTW-KB-compilatie.pdf` = 32 KB-besluiten in één PDF), wordt
`output:` vervangen door `splits:`. De convert-pipeline schrijft dan N aparte MDs:

```yaml
WBTW-KBs:
  bron_rol: itaa_lex
  raw: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
  extract:
    method: pdftotext_compilatie_btw_kb
  splits:
    - kb_id: "1"
      output: resources/bronnen/wetteksten/WBTW-KB1-voldoening.md
      wet: "Koninklijk besluit nr. 1 ..."
    - kb_id: "2"
      output: resources/bronnen/wetteksten/WBTW-KB2-forfaitaire.md
      wet: "..."
    # ...
```

Bestaande output-namen blijven gehandhaafd voor chunk-id-stabiliteit (ADR-006 §3.1).
Het oude artefact-paar (compilatie-MD + 32 derived MDs) verdwijnt: één PDF → 32 MDs
direct, geen split-script, geen `derived_from`-relatie.

### 2. Conversie-pipeline (één atomaire stap, geen patches)

**Principe (vastgesteld 2026-05-09)**: `convert.py` produceert in één aanroep een
finale markdown die zo de RAG-index in kan. Geen post-processing patch-scripts.
Functies die voorheen in losse scripts zaten (`inject_wettekst_headings`,
`inject_norm_headings`, `fix_advies_artefacts`, `fix_norm_artefacts`,
`split-kb-compilatie`) verhuizen naar `tools/lib/` als bibliotheekmodules en
worden vanuit `convert.py` aangeroepen.

**Volgorde binnen convert.py**:

```
raw bron → extract (per method) → cleanup → heading-injection
        → frontmatter (incl. chunk-config + provenance) → MD-output
```

Sub-stappen:

1. **Extract**: per `extract.method` een handler. PDF→tekst (`pdftotext_*`),
   HTML→markdown (`cbn_advies_html`), 2-koloms NL+FR (`extract_norm_twocolumn`),
   compilatie-splits (`pdftotext_compilatie_*` schrijft N outputs uit één raw).

2. **Cleanup**: idempotente pipeline
   `remove_page_artifacts → fix_broken_words → normalize_whitespace →
    collapse_blank_lines → merge_wrapped_lines → merge_heading_continuations →
    mark_appendices`. Plus bron-specifieke stappen waar nodig.
   **Invariant**: cleanup raakt nooit juridische tekst aan — enkel opmaak/metadataruis.

3. **Heading-injection** (wetteksten): hiërarchie-detectie volgens vaste Belgische
   wettekst-volgorde `DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING`.
   Aanwezigheidsdetectie + mapping H2→H6 met conditional flattening (merge-groepen
   `[DEEL,BOEK]`, `[AFDELING,ONDERAFDELING]`). Voor normen/adviezen: type-specifiek
   (sectie-headings, bold-titel-promotie, ...).

4. **Frontmatter**: schrijft `chunk.level`, `chunk.type`, `chunk.sub_strategy`
   (per heading-injection bepaald), `bron_rol`, `wet`, `tags`, `provenance`
   (zie ADR-004), `provenance.trust.status` = `unreviewed` (default).

5. **Output**: schrijft naar **staging**: `data/etl-staging/<bron>.md`.
   Promotie naar `resources/bronnen/...` gebeurt via een aparte stap (zie §5),
   na QA-gate. Dit voorkomt dat een halfgare conversie de canonieke MDs
   overschrijft tijdens iteratie.

**Idempotentie als test**: `convert.py X` tweemaal achter elkaar moet identieke
output produceren (modulo `provenance.generated_at`). Een unit-test verifieert dit.

### 3. Output-format

Markdown met YAML frontmatter:
```yaml
---
titel: "..."
bron_rol: itaa_lex
tags: [...]
chunk:                   # frontmatter-driven chunking (ADR-006 §4)
  level: 5               # MD-niveau waarop chunk-grens ligt
  type: "Art."           # filter op heading-type bij chunken
  sub_strategy: null     # opt-in voor sub-artikel chunking (toekomstig)
provenance: { ... }      # zie ADR-004
---
```

**Heading-niveaus** (zie ADR-006 §4.1 voor wettekst-detectie):
- H1 = wet-naam / advies-titel / norm-titel (vast, breadcrumb-root)
- H2 = hoogste structuurlabel (per wet dynamisch gedetecteerd)
- H3–H6 = diepere structuurlabels
- Artikel-headings (`Art.`, `Par.`) op `chunk.level`-niveau

Tabellen als markdown-tabellen. Schema's als losse PNG's in `<bron>-img/` (pymupdf4llm).

### 4. Bron-rollen (5 niveaus)

| Waarde | Autoriteit | Bij examen citeerbaar? |
|---|---|---|
| `itaa_lex` | Hoogste — wettekst | ✅ Ja |
| `normatief` | Hoog — wettekst buiten ITAA-LEX | ❌ |
| `interpretatief` | Middel — CBN/ITAA-normen | ❌ |
| `praktijkgids` | Laag — toelichtingen, gidsen | ❌ |
| `formulier` | Referentie — aangifteformulieren | ❌ |

Stuurt confidence (ADR-010) en retrieval-filtering (ADR-006).

### 5. Kwaliteits-gate en auto-trust workflow

Bij ~580 bronnen is handmatig elk MD-bestand controleren niet realistisch, maar
blind alles indexeren ondermijnt RAG-precisie. De gate werkt op de **staging-MD**
uit §2 stap 5 en bestaat uit drie lagen met een agent-gestuurde auto-trust-flow.
De mens komt enkel tussen voor een steekproef.

**Laag 1 — Deterministische checks** (`tools/etl/qa_bron.py`)

Per staging-MD machine-controleerbare criteria:

- frontmatter compleet voor bron-rol; provenance-blok valide (inputs+sha256, tooling, generated_at)
- chunk-config aanwezig (`chunk.level`, `chunk.type`)
- ≥ N headings op `chunk.level` voor bestand >X chars (anders: degraded chunking)
- langste sectie tussen `chunk.level`-headings < 24K chars (RAG-bovengrens, ADR-006)
- geen extractie-artefacten: `\x0c` form feed, `....\d+$` TOC-rest, `Page N of N`,
  `[A-Z][a-z]+\s{20,}[A-Z]` kolom-bleed, runs van >5 lege regels, OCR-flags
  (`lAB`, `lBR`, l/I-verwarring op verdachte plekken)

Output: `data/qa/<run-id>.json` met per bron `pass | warn | fail` + concrete
vindplaatsen.

**Laag 1.5 — Regressie-diff** (nieuw 2026-05-09; `tools/etl/diff_review.py`)

Voor elke bron die al een vorige versie heeft (`resources/bronnen/<bron>.md`
bestaat in HEAD), genereert de gate een **git-diff** tussen staging en HEAD.
Een Claude Code subagent (Sonnet, lokaal — geen externe API per ADR-008 §0)
beoordeelt de diff en produceert per bron:

```json
{
  "bestand": "...",
  "diff_verdict": "improvement | regression | structural_change | no_op",
  "rationale": "1-3 zinnen — wat veranderde, is het beter/slechter/equivalent",
  "kritieke_observaties": ["bv. juridische tekst gewijzigd; bv. articles weggevallen"]
}
```

`diff_verdict`:
- `improvement` — duidelijke verbetering (artefacten weg, headings beter, ...)
- `no_op` — niets verandert behalve provenance-timestamp
- `structural_change` — grote herstructurering; mens moet kijken
- `regression` — slechter dan HEAD; auto-trust geblokkeerd

Voor nieuwe bronnen (geen HEAD-versie): laag 1.5 wordt overgeslagen.

**Laag 2 — Inhoudelijke beoordeling** (`tools/etl/qa_subagent_prompt.md`)

Voor wat Laag 1 niet kan beoordelen — leesbaarheid, scrambled-words, verdwenen
secties, abrupt einde, mismatch naam vs. inhoud. Een Claude Code subagent (Sonnet,
lokaal) leest de gemarkeerde bronnen plus het Laag-1-rapport en produceert:

```json
{
  "bestand": "...",
  "aanbevolen_status": "trusted | needs-rework | rejected",
  "rationale": "1-3 zinnen onderbouwing",
  "concrete_problemen": [{"regel": N, "type": "...", "voorbeeld": "..."}],
  "concrete_sterke_punten": ["..."]
}
```

Heuristiek: conservatief — bij twijfel `needs-rework`, niet `trusted`.

**Auto-trust verdict-combinatie**:

| Laag 1 | Laag 1.5 | Laag 2 | Resultaat |
|---|---|---|---|
| `pass` | `improvement` of `no_op` | `trusted` | **auto-trust** → promote naar resources/bronnen/, trust=trusted |
| `pass` | `structural_change` | `trusted` | **review-pending** → promote, trust=trusted, sample-pick verplicht |
| `pass` | `regression` | * | **blocked** → blijft in staging, trust=needs-rework |
| `warn` | * | `trusted` | **review-pending** → promote, trust=trusted, sample-pick verplicht |
| `fail` | * | * | **blocked** → blijft in staging, trust=needs-rework |
| * | * | `needs-rework` of `rejected` | **blocked** → blijft in staging |

`promote_staging.py` voert de promotie uit en schrijft naar `provenance.trust`:

```yaml
trust:
  status: trusted
  qa_version: <run-id>
  agent_verdict_at: 2026-05-09T14:00:00Z
  confirmed_by: subagent-sonnet-4-6
  rationale: "..."
  sample_pick: false   # zie Laag 3
  sample_reviewed_at:  # leeg tot mens steekproef doet
  sample_reviewed_by:
```

**Laag 3 — Mens-steekproef** (`tools/etl/sample_review.py`)

Na elke conversie-batch trekt de tool een random steekproef (default 10%) uit
de auto-trusted bronnen en zet hun `provenance.trust.sample_pick: true`. De
mens bewerkt die bestanden in zijn editor; de tool toont een lijst:

```
$ python tools/etl/sample_review.py --status
Steekproef batch <run-id>:
  ⏳ resources/bronnen/wetteksten/WIB92.md         (gepickt, niet beoordeeld)
  ✓  resources/bronnen/wetteksten/Antiwitwaswet... (OK, 2026-05-09)
  ✗  resources/bronnen/normen/ITAA-norm-X.md       (problemen, 2026-05-09)
```

Detectie of de mens een bestand bewerkt heeft: vergelijk `mtime` met
`agent_verdict_at`. Als mtime > agent_verdict_at en het bestand is in
sample-pick: vul automatisch `sample_reviewed_at` in en vraag oordeel
(`--mark-ok` of `--mark-not-ok`).

Bij `--mark-not-ok` op één bron: alle auto-trusted bronnen in dezelfde batch
gaan terug naar `unreviewed` (de mens zal die ook willen herzien). Ook bronnen
met `review-pending` blijven `trusted` maar krijgen verplichte `sample_pick: true`.

**Vier trust-statussen** (zie ADR-004 §"Trust-schema-uitbreiding"):

| Status | Betekenis | rag_index gedrag |
|---|---|---|
| `unreviewed` | Default; nog niet beoordeeld | Geskipt |
| `trusted` | Bevestigd OK voor RAG | Geïndexeerd |
| `needs-rework` | Gemarkeerd: ETL-fix nodig | Geskipt |
| `rejected` | Niet bruikbaar; weglaten | Geskipt |

**Default-state strict**: bij introductie krijgen alle nieuwe bronnen
`unreviewed`. Niets in de RAG-index tot de auto-trust-flow ze op `trusted` zet.

### 6. Indexering filtert op trust

`tools/rag/rag_index.py` indexeert default alleen bronnen met
`provenance.trust.status == "trusted"`. Geskipte bronnen worden geteld in de
run-statistiek met reden. Een `--include-unreviewed` flag bestaat voor
experimenten maar is niet de productieflow.

Dankzij chunk-id-stabiliteit (ADR-004, ADR-006 §3.1), ChromaDB upsert én de
chunk-sha-skip (`_batch_upsert` in `rag_index.py`) is het toevoegen van een
nieuw-trusted bron volledig incrementeel: bestaande chunks behouden hun id én
worden niet opnieuw geëmbed (de SHA wordt vergeleken vóór de embedding-call),
nieuwe chunks worden toegevoegd. Conform ADR-004 §"Chunk-id-stabiliteit als
requirement". Geverifieerd in test (2026-05-08): 16/21 chunks overgeslagen bij
appenden van een tweede norm aan een collection met 16 bestaande chunks.

### 7. Wettekst-hiërarchie (samenvatting; detail in §2 stap 3)

Heading-injectie voor wetteksten gebruikt de **vaste Belgische wettekst-hiërarchie**
`DEEL > BOEK > TITEL > HOOFDSTUK > AFDELING > ONDERAFDELING`, gevolgd door
`Art.` als chunk-grens. Aanwezigheidsdetectie + mapping H2→H6, met conditional
flattening via merge-groepen `[DEEL, BOEK]` en `[AFDELING, ONDERAFDELING]` bij
overflow. Niet-samenhangende merges (bv. `[TITEL, HOOFDSTUK]`) worden niet
automatisch gedaan — zo'n bron krijgt een waarschuwing en handmatige beslissing.

**Conversie-bug-audit** (separate stap, vóór re-conversie):
`tools/etl/audit_wettekst_toplevels.py` detecteert wetten waar het hoogste
structuurlabel of het eerste artikel ontbreekt (bv. WVV mist DEEL 1 / BOEK 1
/ TITEL 1 / Art. 1:1). Aanname: de raw PDF bevat de data; betere `pdftotext`-
flags of een `justel_html`-fallback lossen het op tijdens re-conversie.

Sub-artikel chunking (definitieblokken, paragrafen) wordt niet als MD-heading
geforceerd — zie ADR-006 §4.2 (toekomstige opt-in via `chunk.sub_strategy`).

## Gevolgen

**Nieuwe / herziene scripts** (`tools/etl/`):

- `convert.py` — orchestrator van de hele pipeline (extract + cleanup + headings + frontmatter); schrijft naar `data/etl-staging/`
- `diff_review.py` (nieuw) — Laag 1.5 regressie-diff via Claude Code subagent
- `promote_staging.py` (nieuw) — promotie van staging naar `resources/bronnen/`, schrijft `provenance.trust`
- `sample_review.py` (nieuw) — random steekproef-tracking, mtime-detectie, --mark-ok / --mark-not-ok
- `audit_wettekst_toplevels.py` — bestaand; conversie-bug-audit
- `qa_bron.py` — Laag 1 deterministische checks (op staging i.p.v. resources)
- `qa_subagent_prompt.md` — Laag 2 prompt-template
- `mark_trusted.py` — bestaande mens-tool (blijft voor handmatige overrides)
- `backfill_trust_unreviewed.py` — one-off migratie (kan na deze revisie geschrapt)

**Naar `tools/lib/` verhuisd of geschrapt**:

- `tools/lib/cleanup.py` — bestaande cleanup-pipeline blijft als module
- `tools/lib/headings.py` (nieuw) — wettekst-hiërarchie + heading-injection-logica uit `inject_wettekst_headings.py`
- `tools/lib/normen_extractie.py` (nieuw) — logica uit `inject_norm_headings.py`, `extract_norm_twocolumn.py`
- `tools/lib/cbn_advies_html.py` (nieuw) — scraper-logica uit `scrape_cbn_advies.py`
- `tools/lib/compilatie_split.py` (nieuw) — split-logica uit `split-kb-compilatie.py`
- `tools/lib/provenance.py` — bestaand; krijgt nieuwe trust-velden (`agent_verdict_at`, `sample_pick`, `sample_reviewed_at`, `sample_reviewed_by`); zie ADR-004
- **Geschrapt** als losse executables: `inject_wettekst_headings.py`, `inject_norm_headings.py`, `fix_advies_artefacts.py`, `fix_norm_artefacts.py`, `split-kb-compilatie.py`, `scrape_cbn_advies.py` (alleen de CLI; logica blijft in lib), `process_normen.py`, `bulk_refresh_adviezen.py`, `migrate_legacy_to_extract.py`, `add_provenance.py` (functionaliteit ingebouwd in `convert.py`)

**`source_config.yaml`**:

- Nieuw veld `splits:` voor 1-op-N compilatie (zie §1)
- Veld `cleanup:` verwijdert (cleanup is altijd default-pipeline; bron-specifieke stappen via `extract.params`)
- Veld `derived_from:` schrappen voor compilatie-derivaties (worden directe outputs van compilatie-raw)

**Workflow voor end-to-end re-conversie van alle bronnen**:

```
1. python tools/etl/convert.py --all                      → data/etl-staging/*.md
2. python tools/etl/qa_bron.py --staging                  → data/qa/<run-id>.json
3. python tools/etl/diff_review.py --staging              → data/qa/<run-id>-diff-verdicts.json
4. python tools/etl/qa_subagent_prompt.md                 → data/qa/<run-id>-content-verdicts.json
5. python tools/etl/promote_staging.py --run <run-id>     → resources/bronnen/*.md (auto-trust)
6. python tools/etl/sample_review.py --run <run-id> --pick 10%  → markeert sample-picks
7. mens beoordeelt picks in editor
8. python tools/etl/sample_review.py --status             → toont voortgang
9. python tools/rag/rag_index.py                          → indexeert trusted bronnen
```

**Open punten** (uit migratie en nieuw):

- WVV-conversie-bug oplossen via betere `pdftotext`-flags of `justel_html` (DEEL 1 / BOEK 1 / Art. 1:1 ontbreken)
- ChromaDB-rebuild draait pas na groene gates + trust-confirmatie op de POC-bronnen
- `resources/eval/golden/` — kleine handmatig-OK-bevonden set voor end-to-end regressie (lange termijn)

**Inmiddels opgelost** (sinds vorige draft, 9 mei 2026):

- `justel_html`-handler: ✓ Wet-verzekeringen-2014 (147 artikelen) en KB-voorafgaande-beslissingen-art22-2003 herconverteerd via `c28d063`
- Oud-BW: ✓ herconverteerd via `convert-oud-bw.py` met `custom_wetboek` (3186 artikelen, 0 plain-text labels)
- 118 legacy `type:`-bronnen: ✓ allemaal gemigreerd naar `extract:`-schema in `eabdfb0`
- Tweetalige norm-extractie: ✓ NL-only kolom + soft-wrap merge in `5863ff9`
