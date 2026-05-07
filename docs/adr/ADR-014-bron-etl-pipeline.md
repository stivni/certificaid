# ADR-014: Bron ETL-pipeline

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Het Certificaid-project verwerkt drie categorieën bronnen:

- **Wetteksten** — 83 `.md`-bestanden in `resources/bronnen/wetteksten/`
- **CBN-adviezen** — ~1.500+ bestanden in `resources/bronnen/adviezen/`
- **Normen** — ITAA-normen, ISA/ISAE/ISRS in `resources/bronnen/normen/`

Elke categorie heeft een eigen herkomst en ETL-aanpak. Er is geen uniforme pipeline: de drie bronsoorten komen via fundamenteel verschillende kanalen binnen en vragen andere verwerking.

## Beslissing

**Drie afzonderlijke ingest-paden, elk met eigen tooling.**

---

### Pad 1 — Wetteksten (PDF → markdown via `convert.py`)

**Herkomst**: ejustice.just.fgov.be (gecoördineerde teksten als PDF), FOD Financiën/Fisconet, of handmatig opgebouwde markdown.

**Conversietypes** (geconfigureerd in `source_config.yaml`):

| Type | Aanpak |
|---|---|
| `ejustice_nl` | `pdftotext` NL-only + cleanup-pipeline |
| `ejustice_bilingual` | `pdftotext` met kolomselectie voor NL + cleanup-pipeline |
| `wib92` | Eigen `convert-wib92.py` (afwijkende FOD-lay-out) |
| `wetboek` | Markdown al beschikbaar; enkel cleanup-pipeline |

**Cleanup-pipeline** (standaard, altijd):
```
remove_page_artifacts → fix_broken_words → normalize_whitespace → collapse_blank_lines
                     → merge_wrapped_lines → merge_heading_continuations
```
`remove_page_artifacts` omvat ejustice running footers (`Pagina X van Y Copyright Belgisch S taatsblad`, incl. OCR-artefact "S taatsblad" met spatie).

`merge_heading_continuations` herstelt structurele headings (`### TITEL`, `#### HOOFDSTUK`, `##### Afdeling`, `Onderafdeling`, `BOEK`, `DEEL`, …) die de PDF-extractor over meerdere regels heeft afgebroken (bv. `### TITEL I. - DE VERSCHILLENDE` + `INKOMSTENBELASTINGEN`). Werkt op markdown-output, ná article-detectie. Zes detectieregels (zie `tools/lib/cleanup.py`); idempotent.

Optionele bron-specifieke stappen via `cleanup:` in `source_config.yaml`:
- `remove_toc_ejustice` — inhoudsopgave verwijderen
- `remove_french_lines` / `remove_french_blocks` — FR-kolom nafilteren
- `ensure_article_headings` — inline `Art. X. tekst` → `## Art. X\n\ntekst` (verplicht voor ejustice: `rag_index.py` chunked op `##`-headings)
- `remove_inline_metadata` — losse Staatsblad-referenties, datumregels

**Twee commando's, twee bedoelingen**:
- `tools/etl/convert.py --source NAAM` — volledige herconversie vanuit PDF (destructief)
- `tools/etl/convert.py --cleanup-only --source NAAM` — enkel opmaak bijwerken (veilig, idempotent)

**Invariant**: cleanup verandert nooit de juridische tekst — enkel opmaak en metadataruis.

**`source_config.yaml`** is de enige bron van waarheid voor alle wetteksten: type, paden, bron_rol, tags, cleanup-stappen en status (`volledig` / `toc_only` / `nieuw`).

---

### Pad 2 — CBN-adviezen (web scrape → markdown via `download-cbn-adviezen.py`)

**Herkomst**: CBN-website (publiek toegankelijk). Adviezen zijn beschikbaar als HTML-pagina's.

**Tooling**: `tools/download/download-cbn-adviezen.py` + `tools/etl/reprocess_cbn_adviezen.py`

**Output**: één `.md`-bestand per advies in `resources/bronnen/adviezen/`, met YAML frontmatter (`titel`, `themas`, `datum`).

**Structuur**: adviezen hebben een rijke `themas`-lijst in frontmatter (gemiddeld 7,1 keywords per advies). `rag_index.py` gebruikt deze thema's als metadata bij het indexeren.

**Refresh**: bij nieuwe CBN-publicatie → download-script opnieuw draaien voor het betreffende advies.

---

### Pad 3 — Normen (download → markdown via `download_beexcellent_normen.py`)

**Herkomst**: BeExcellent-platform (ITAA-normen) en ISA/ISAE/ISRS (IFAC-publicaties).

**Tooling**: `tools/download/download_beexcellent_normen.py` + `tools/etl/process_normen.py`

**Output**: één `.md`-bestand per norm in `resources/bronnen/normen/`, met YAML frontmatter.

**Structuur**: normen worden op `##`-sectieniveau gechunked (per paragraaf), niet op artikelniveau.

---

### Gemeenschappelijke principes

- **Geen bron wordt overgeslagen**: elke bron in `resources/bronnen/` heeft een gekend ingest-pad en is traceerbaar naar zijn herkomst.
- **Frontmatter is verplicht**: elk bronbestand heeft minimaal `titel`, `bron_rol` en `tags` in YAML frontmatter. Dit stuurt de RAG-collectie en de weergave in de tutor.
- **Refresh-beleid**: bij gewijzigde bronpublicatie → ingest-pad opnieuw draaien voor die bron → keywords opnieuw genereren (ADR-004) → index herbouwen (ADR-001/ADR-002).

## Gevolgen

- Nieuwe wettekst: entry in `source_config.yaml` → `tools/etl/convert.py --source NAAM` → `tools/extractie/generate_keywords.py` → `tools/rag/rag_index.py`
- Nieuw CBN-advies: `tools/download/download-cbn-adviezen.py` voor dat advies → `tools/rag/rag_index.py --collection adviezen`
- Nieuwe norm: `tools/download/download_beexcellent_normen.py` → `tools/rag/rag_index.py --collection normen`
- Handmatige correcties in wettekst-`.md`-bestanden gaan verloren bij herconversie; `--cleanup-only` is veilig
- Buiten scope: keyword-generatie (ADR-004), chunk-strategie (ADR-002), bron_rol-classificatie (ADR-008)
