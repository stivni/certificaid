# ADR-005: Bronnen-ETL

**Status**: Draft
**Datum**: 2026-05-07
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
provenance: { ... }   # zie ADR-004
---
```

Per artikel `## Art. X`-headings (gezagsbron voor chunking, ADR-006). Tabellen als markdown-tabellen. Schema's als losse PNG's in `<bron>-img/` (pymupdf4llm).

### 4. Bron-rollen (5 niveaus)

| Waarde | Autoriteit | Bij examen citeerbaar? |
|---|---|---|
| `itaa_lex` | Hoogste — wettekst | ✅ Ja |
| `normatief` | Hoog — wettekst buiten ITAA-LEX | ❌ |
| `interpretatief` | Middel — CBN/ITAA-normen | ❌ |
| `praktijkgids` | Laag — toelichtingen, gidsen | ❌ |
| `formulier` | Referentie — aangifteformulieren | ❌ |

Stuurt confidence (ADR-010) en retrieval-filtering (ADR-006).

### 5. Kwaliteits-gate (twee stappen, beide groen)

1. **Golden-set regressietest**: 5–10 bronnen handmatig OK-bevonden, hash-vergelijking bij re-run. Diff-rapport bij verschil.
2. **Agent-QA**: LLM leest output-MD, scoort op structurele criteria (headings present, tabellen heel, geen leak van paginavoetregels, geen TOC-residu in body). Output: `pass` / `fail` / `warning` met concrete vindplaatsen.

Een bron is "klaar" pas als beide groen.

## Gevolgen

- `tools/etl/convert.py` is dispatcher — `extract.method` selecteert de handler
- `tools/etl/qa_agent.py` (nieuw) — LLM-QA per bron, deel van de gate
- `resources/eval/golden/` — referentie-outputs voor regressietest
- Open punten uit migratie blijven gelden: `justel_html`-handler implementeren, Oud-BW herconverteren, 104 legacy `type:`-bronnen migreren
- ChromaDB-rebuild draait pas na groene gates op de POC-bronnen
