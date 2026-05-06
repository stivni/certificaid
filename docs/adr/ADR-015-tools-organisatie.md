# ADR-015: Tools-map georganiseerd per pipeline-fase

**Status**: Draft
**Datum**: 2026-05-06

## Context

`tools/` was platgeslagen: 19 scripts plus `lib/` en losse files door elkaar, zonder visuele groepering. Bij meer dan ~10 scripts wordt het lastig om snel te zien welk script bij welke fase hoort. De scripts vallen in praktijk uiteen in heldere functionele groepen.

## Beslissing

Groeperen per pipeline-fase. `tools/` bevat alleen submappen, geen losse scripts:

- **`tools/download/`** — bronnen ophalen van het web (CBN-adviezen, ITAA-normen)
- **`tools/etl/`** — bron-conversie (PDF/HTML → markdown), reprocessing en normalisatie
- **`tools/rag/`** — ChromaDB-index bouwen en bevragen
- **`tools/extractie/`** — concept- en keyword-extractie als verrijking van bronnen
- **`tools/examen/`** — examenpatroon-extractie en question review
- **`tools/export/`** — externe exports (NotebookLM)
- **`tools/lib/`** — gedeelde bibliotheken (`cleanup.py` voor ETL, `retrieval.py` voor RAG/tutor)

`sectionFootnotes.ts` is verhuisd naar `quartz/plugins/transformers/`, waar Quartz-plugins thuishoren.

## Gevolgen

- Alle CLI-aanroepen krijgen één extra map-laag: `python3 tools/etl/convert.py` i.p.v. `python3 tools/convert.py`. Documentatie en docstrings zijn meegegaan.
- Scripts die paden naar de projectroot opbouwen via `Path(__file__).parent.parent` zijn aangepast naar `parent.parent.parent` (één niveau dieper).
- `convert.py` en `rag_query.py` blijven `from lib.X` importeren via `sys.path.insert(0, str(ROOT / "tools"))` — `lib/` blijft direct onder `tools/`.
- `tutor/app.py` blijft werken zonder wijziging aan zijn `sys.path`-setup.
- Toekomstige scripts horen meteen in een bestaande submap thuis. Past geen enkele submap? Eerst een nieuwe submap motiveren in een ADR-update — losse scripts in `tools/` zijn niet meer toegestaan.
