# Certificaid

Kennisbank voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant. Destilleert uit het officiële ITAA-programma (TDKs per vak) + wetteksten + normen + voorbeeldexamens het studiemateriaal dat ontbreekt.

**Doelpubliek**: Stagiairs GA/GBA met boekhoudkundige en fiscale basiskennis — geen juristen.

**Bij het examen beschikbaar**: ITAA-LEX (wettekstenbundel) + Cijferzakboekje (tarieven en bedragen). Wat getoetst wordt: concepten begrijpen, uitzonderingen herkennen, correct redeneren — niet cijfers uit het hoofd kennen.

---

## Wegwijzer

| Taak | Zie |
|---|---|
| Fiche schrijven (materie, competentie, PO) | [`docs/content-richtlijnen.md`](docs/content-richtlijnen.md) |
| PO-build uitvoeren | [`docs/po-builder.md`](docs/po-builder.md) |
| Bron toevoegen of verwerken | [`docs/bronnen-pipeline.md`](docs/bronnen-pipeline.md) |
| Architectuurbeslissing opzoeken of toevoegen | [`docs/adr/INDEX.md`](docs/adr/INDEX.md) |
| RAG-index herbouwen of querien | `tools/rag_index.py`, `tools/rag_query.py` |

---

## Absolute regels

Deze regels gelden bij elke sessie en elke agent:

1. **Geen wetsinhoud zonder bronverwijzing.** Onzeker? → `⚠️ te verifiëren`. Liever leeg dan onzeker.

2. **Confidence-labeling is verplicht.** ⚖️ = direct traceerbaar naar een bron (grounded). 🤖 = redenering of constructie (inferred). Elke claim krijgt een label; Claude mag niet weglaten bij twijfel.

3. **Geen Claude API voor bulk-operaties zonder expliciete akkoord.** Keyword-generatie, herindexering, batch-extractie: gebruik lokale tools (KeyBERT, YAKE). Interactieve tutor en concept-extractie: Sonnet is OK.

4. **Raadpleeg de ADR-index vóór je begint** aan indexering, model-wijzigingen, bronnen toevoegen of concept-extractie. Zie taak→ADR mapping in [`docs/adr/INDEX.md`](docs/adr/INDEX.md).

5. **Alle beslissingen worden vastgelegd als ADR** — technisch én domein. Draft-status is OK; vastleggen is verplicht.

6. **Twee werkwijzen — weet welke actief is** (zie ADR-014):
   - **Design/sparring-modus**: we bespreken een beslissing samen. Het resultaat *moet* landen in een nieuw of bijgewerkt ADR vóór de uitvoering start.
   - **Werk-modus**: zelfstandige uitvoering (indexeren, fiches schrijven, bronnen verwerken, ...). Werkt altijd binnen de spelregels van de bestaande ADRs — geen nieuwe ontwerpkeuzes maken zonder terug te schakelen naar design-modus.

---

## Technisch

### Mappenstructuur

```
certificaid/
├── CLAUDE.md                    # Deze wegwijzer
├── docs/
│   ├── content-richtlijnen.md  # Schrijfregels voor fiches
│   ├── po-builder.md           # PO-build procesflow
│   ├── bronnen-pipeline.md     # Bronnen toevoegen en verwerken
│   └── adr/                    # Architecture Decision Records
├── content/
│   ├── programmaonderdelen/    # PO-fiches (catalogus per vak)
│   ├── competenties/           # Competentie-fiches (technieken)
│   ├── materie/                # Materie-fiches (concepten)
│   └── bronnen/                # Primaire bronnen als site-content
├── resources/
│   ├── bronnen/                # Doorzoekbare bronbestanden (grep/Read)
│   │   ├── wetteksten/         # Wetteksten als markdown
│   │   ├── normen/             # ITAA-normen
│   │   └── adviezen/           # CBN-adviezen
│   ├── source_config.yaml      # Enige bron van waarheid voor alle bronnen
│   └── po-builder-prompt.md    # Startbericht po-builder scheduled agent
├── tools/
│   ├── lib/                    # Gedeelde bibliotheken (retrieval, cleanup)
│   ├── rag_index.py            # ChromaDB-index bouwen
│   ├── rag_query.py            # RAG bevragen (CLI)
│   ├── convert.py              # Wetteksten converteren
│   ├── generate_keywords.py    # Chunk-level keywords (KeyBERT, lokaal)
│   └── concept_extractor.py   # Concept records genereren
├── tutor/app.py                # Streamlit tutor
├── data/
│   ├── chroma_db/              # ChromaDB (gitignored, herbouwbaar)
│   └── concept_records/        # Gegenereerde concept records (gitignored)
└── .github/workflows/deploy.yml
```

### Publicatie

- Site: https://stivni.github.io/certificaid
- Lokaal testen: `npm install && npm run dev` → http://localhost:8080
- Deploy triggert automatisch bij wijzigingen in `content/`, `quartz.config.ts` of `quartz.layout.ts`

### Quartz

Bij wijzigingen aan Quartz layout of styling:
1. Controleer https://quartz.jzhao.xyz/layout voor beschikbare componenten
2. Controleer `quartz/components/` voor de precieze API
3. Pas daarna `quartz.layout.ts` of `quartz/styles/custom.scss` aan
