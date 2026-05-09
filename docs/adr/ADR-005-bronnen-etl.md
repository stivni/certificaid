# ADR-005: Bronnen-ETL

**Status**: Draft
**Datum**: 2026-05-07 (gewijzigd 2026-05-08: §5 kwaliteits-gate uitgewerkt met trust-marker; 2026-05-09: §3 frontmatter `chunk:`-blok + §7 wettekst-hiërarchiedetectie)
**Vervangt**: archive/ADR-014 (oude ETL-pipeline), ADR-008 (bron_rol nu hier ingebed)

## Context

Bronnen komen uit verschillende kanalen (ejustice-PDF's, FOD-PDF's, CBN-website-HTML, BeExcellent-platform, ITAA-publicaties als PDF, IFAC-PDF's voor ISA/ISAE/ISRS) en hebben verschillende structuur (artikelen, secties, krantenkolommen, schema's). Doel: een **uniforme markdown-output** met behoud van structurele headings en tabellen, gestuurd door één configuratiebestand.

De vorige iteratie had een proliferatie van type-strings (`ejustice_nl`, `wib92`, `wetboek`, `split`, `skip`, ...) zonder duidelijke schema-discipline. Het ADR-017-extract-schema heeft dat al deels rechtgetrokken — die richting wordt hier voortgezet.

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
            justel_html | handcrafted
    params: { ... }   # methode-specifiek
  cleanup: [...]       # optionele post-processing
```

`extract.method: handcrafted` vereist `params.reason` — geen ongedocumenteerde uitzonderingen.

### 2. Cleanup-pipeline (default, idempotent)

`remove_page_artifacts → fix_broken_words → normalize_whitespace → collapse_blank_lines → merge_wrapped_lines → merge_heading_continuations → mark_appendices`

Plus optionele bron-specifieke stappen (`remove_toc_ejustice`, `remove_french_lines`, `ensure_article_headings`, ...).

**Invariant**: cleanup verandert nooit de juridische tekst — enkel opmaak en metadataruis.

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

### 5. Kwaliteits-gate (drie lagen → trust-marker)

Bij ~580 bronnen is handmatig elk MD-bestand controleren niet realistisch, maar
blind alles indexeren ondermijnt RAG-precisie. De gate is daarom drie lagen
diep, met een expliciete trust-marker als operationele output.

**Laag 1 — Deterministische checks** (`tools/etl/qa_bron.py`)

Per bron-MD machine-controleerbare criteria:

- frontmatter compleet voor bron-rol; provenance-blok valide (inputs+sha256, tooling, generated_at)
- ≥ N `##`-headings voor bestand >X chars (anders: degraded chunking)
- langste sectie tussen `##` < 24K chars (RAG-bovengrens, ADR-006)
- geen extractie-artefacten: `\x0c` form feed, `....\d+$` TOC-rest, `Page N of N`,
  `[A-Z][a-z]+\s{20,}[A-Z]` kolom-bleed, runs van >5 lege regels, OCR-flags
  (`lAB`, `lBR`, l/I-verwarring op verdachte plekken)

Output: `data/qa/<run-id>.json` met per bron `pass | warn | fail` + concrete
vindplaatsen. Hergebruikt detectiepatronen uit `inject_norm_headings.py`.

**Laag 2 — Subagent-judgment** (`tools/etl/qa_subagent_prompt.md`)

Voor wat regels niet kunnen beoordelen — leesbaarheid, scrambled-words,
verdwenen secties, abrupt einde, mismatch naam vs. inhoud. Een Claude Code
subagent (Sonnet of Opus, lokaal — geen externe API per ADR-008 §0) leest de
gemarkeerde bronnen plus het Laag-1-rapport en produceert per bron:

```json
{
  "bestand": "...",
  "aanbevolen_status": "trusted | needs-rework | rejected",
  "rationale": "1-3 zinnen onderbouwing",
  "concrete_problemen": [{"regel": N, "type": "...", "voorbeeld": "..."}],
  "concrete_sterke_punten": ["..."]
}
```

Heuristiek: conservatief — bij twijfel `needs-rework`, niet `trusted`. De
output (`data/qa/<run-id>-verdicts.json`) is een aanbeveling, geen autoriteit.

**Laag 3 — Mens-confirmatie** (`tools/etl/mark_trusted.py`)

De mens bevestigt trust-statussen, hetzij per bron, per collection, of bulk
vanuit een verdicts-bestand. Het resultaat landt als `provenance.trust` in de
bron-MD (zie ADR-004 §schema-uitbreiding).

**Vier trust-statussen:**

| Status | Betekenis | rag_index gedrag |
|---|---|---|
| `unreviewed` | Default; nog niet beoordeeld | Geskipt |
| `trusted` | Bevestigd OK voor RAG | Geïndexeerd |
| `needs-rework` | Gemarkeerd: ETL-fix nodig | Geskipt |
| `rejected` | Niet bruikbaar; weglaten | Geskipt |

**Default-state strict**: bij introductie krijgen alle bestaande bronnen
`unreviewed`. Niets in de RAG-index tot bewust `trusted` gemaakt
(`tools/etl/backfill_trust_unreviewed.py`).

**Golden-set regressietest** (parallel aan de drie lagen):
5–10 bronnen handmatig OK-bevonden, hash-vergelijking bij re-run. Diff-rapport
bij verschil. Bedoeld om regressies in de ETL-pipeline te vangen, niet om de
inhoudelijke trust-beslissing te vervangen. Aparte tooling, niet in dezelfde
PR.

### 7. Wettekst-hiërarchie afgeleid uit document

De ETL voor wetteksten doet structuur-detectie **per wet** in plaats van een
universele hardgecodeerde label-naar-niveau mapping. Pipeline:

1. **Conversie-audit** vóór heading-injectie: ontbreekt het hoogste
   structuurlabel of het eerste artikel? (WVV mist DEEL 1 / BOEK 1 / TITEL 1 /
   Art. 1:1 in onze conversie — sanity-check tegen officiële bron.)

2. **Containment-detectie** (`tools/etl/inject_wettekst_headings.py`):
   - Voor elk paar (A, B), tel hoe vaak B voorkomt tussen twee opeenvolgende A's
   - Topo-sort levert ranks (hoogste = bevat meeste andere types tussen z'n
     opeenvolgende instances)
   - Niet "eerste verschijning" — dat geeft fouten bij wetten als WVV waar DEEL
     pas mid-document verschijnt maar BOEKs groepeert

3. **Mapping H2 → H6** met conditional flattening bij overflow:
   - Hoogste rank → H2; volgende ranks → H3, H4, ... ; artikel = laagste rank
   - Bij >5 niveaus: pas merge-groups toe (`[DEEL, BOEK]`,
     `[AFDELING, ONDERAFDELING]`)
   - Niet-samenhangende merges (TITEL+HOOFDSTUK) worden niet automatisch gedaan

4. **Frontmatter-update**: schrijft `chunk.level`, `chunk.type`, en de
   `chunk.sub_strategy` (default null).

Sub-artikel chunking (definitieblokken, paragrafen) wordt niet als
MD-heading geforceerd — zie ADR-006 §4.2.

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

## Gevolgen

- `tools/etl/convert.py` is dispatcher — `extract.method` selecteert de handler
- `tools/etl/qa_bron.py` (nieuw) — Laag 1 deterministische checks
- `tools/etl/qa_subagent_prompt.md` (nieuw) — Laag 2 prompt-template (geen executable; mens kopieert in Claude Code Task-tool)
- `tools/etl/mark_trusted.py` (nieuw) — Laag 3 mens-tool om trust te zetten
- `tools/etl/backfill_trust_unreviewed.py` (one-off) — initiële migratie van bestaande bronnen
- `tools/etl/inject_wettekst_headings.py` — wettekst structuurlabels → MD-headings; bevat per-wet hiërarchie-detectie en conditional flattening (zie §7)
- `tools/etl/audit_wettekst_toplevels.py` (nieuw, TODO) — conversie-bug audit: detecteert wetten waar het hoogste structuurlabel of eerste artikel ontbreekt
- `tools/rag/rag_index.py` — krijgt trust-filter en `--include-unreviewed` flag
- `tools/lib/provenance.py` — krijgt `Trust` dataclass (zie ADR-004)
- `resources/eval/golden/` — referentie-outputs voor regressietest (later)
- Open punten uit migratie blijven gelden: `justel_html`-handler implementeren, Oud-BW herconverteren, 104 legacy `type:`-bronnen migreren
- ChromaDB-rebuild draait pas na groene gates + trust-confirmatie op de POC-bronnen
