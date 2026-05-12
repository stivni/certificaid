# Certificaid

Kennisbank voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant. Destilleert uit het officiële ITAA-examenprogramma (taken, doelstellingen en kenniselementen per programmaonderdeel) + wetteksten + normen + voorbeeldexamens het studiemateriaal dat ontbreekt.

**Doelpubliek**: Stagiairs GA/GBA met boekhoudkundige en fiscale basiskennis — geen juristen.

**Bij het examen beschikbaar**: ITAA-LEX (wettekstenbundel) + Cijferzakboekje (tarieven en bedragen). Wat getoetst wordt: concepten begrijpen, uitzonderingen herkennen, correct redeneren — niet cijfers uit het hoofd kennen.

> **Status (2026-05-07)**: Architectuur herzien. Fase 0 (provenance-plumbing) is af; Fase 1 (Bronnen-ETL) is de volgende. Zie [`docs/roadmap.md`](docs/roadmap.md) voor fasering en DoD per fase, en [`docs/adr/INDEX.md`](docs/adr/INDEX.md) voor de 10 nieuwe ADRs (oude set in `docs/adr/archive/`).

---

## Wegwijzer

| Taak | Zie |
|---|---|
| Roadmap & fase-status | [`docs/roadmap.md`](docs/roadmap.md) |
| Architectuurbeslissing opzoeken of toevoegen | [`docs/adr/INDEX.md`](docs/adr/INDEX.md) |
| Bron toevoegen of verwerken | [`docs/bronnen-pipeline.md`](docs/bronnen-pipeline.md) *(legacy; ADR-005 bij Fase 1)* |
| Bronnen-overzicht (type + trust-status per bron) | [`resources/bronnen/INDEX.md`](resources/bronnen/INDEX.md) — auto-gegenereerd via `python3 tools/lib/bronnen_index.py --force`; machine-leesbaar in `data/bronnen-index.json` |
| Provenance van een artefact bekijken / stale-flaggen | `tools/etl/add_provenance.py`, `tools/etl/mark_stale.py` |
| RAG-index herbouwen of bevragen | `tools/rag/rag_index.py`, `tools/rag/rag_query.py` *(wacht op Fase 2)* |
| Fiche schrijven / programmaonderdeel-build *(legacy)* | [`docs/content-richtlijnen.md`](docs/content-richtlijnen.md), [`docs/po-builder.md`](docs/po-builder.md) *(vervalt bij Fase 5)* |

---

## Absolute regels

Deze regels gelden bij elke sessie en elke agent:

1. **Geen wetsinhoud zonder bronverwijzing.** Onzeker? → `⚠️ te verifiëren`. Liever leeg dan onzeker.

2. **Confidence-labeling is verplicht.** ⚖️ = direct traceerbaar naar een bron (grounded). 🤖 = redenering of constructie (inferred). Elke claim krijgt een label; Claude mag niet weglaten bij twijfel.

3. **Geen Claude API in de build-pipeline.** LLM-werk tijdens build (concept-extractie, vermoedensruimte, seed-bouw, verdiep) gebeurt **lokaal via een Claude Code subagent** in dev-omgeving — niet via `anthropic.Anthropic()`-calls vanuit scripts. Helper-scripts in `tools/extractie/` doen alleen deterministisch werk (retrieval, embedding, JSON-IO). Keyword-generatie en herindexering: lokale tools (KeyBERT, YAKE, bge-m3). De **gedeployde tutor** draait wel op de Anthropic API — dat is een productie-eindpunt, geen build-stap.

4. **Raadpleeg de ADR-index vóór je begint** aan indexering, model-wijzigingen, bronnen toevoegen of concept-extractie. Zie taak→ADR mapping in [`docs/adr/INDEX.md`](docs/adr/INDEX.md).

5. **Alle beslissingen worden vastgelegd als ADR** — technisch én domein. Draft-status is OK; vastleggen is verplicht.

6. **Twee werkwijzen — weet welke actief is**:
   - **Design/sparring-modus**: we bespreken een beslissing samen. Het resultaat *moet* landen in een nieuw of bijgewerkt ADR vóór de uitvoering start.
   - **Werk-modus**: zelfstandige uitvoering (indexeren, fiches schrijven, bronnen verwerken, ...). Werkt altijd binnen de spelregels van de bestaande ADRs — geen nieuwe ontwerpkeuzes maken zonder terug te schakelen naar design-modus.

7. **Werkverdeling Opus ↔ Sonnet**:
   - **Opus** is de design-autoriteit: ADR-werk, sparring, plan-validatie, eindreview op grote diffs.
   - **Sonnet** voert de uitvoering uit binnen de spelregels van het ADR. Concreet werk (scripts schrijven, refactoren, conversie draaien, tests uitvoeren) wordt door Opus **gedelegeerd via de Agent-tool** zodra het plan duidelijk is. Opus blijft de gespreksmodus; Sonnet-agenten zijn werkpaarden.
   - Sonnet pingt terug naar Opus bij design-onduidelijkheid (bv. een edge-case die niet in het ADR staat). Sonnet maakt geen nieuwe ontwerpkeuzes zelfstandig.
   - In een Sonnet-sessie zonder design-werk geldt deze regel niet — daar werkt Sonnet rechtstreeks binnen het bestaande ADR.

8. **Geen afkortingen in code, docs en schema's.** Volledige namen overal: `programmaonderdeel` (niet `PO`), `kenniselement` (niet `TDK`), enzovoort. Geldt voor bestandsnamen, veldnamen, mapnamen, ADR-titels en commit-messages. In een gesprek met de gebruiker zijn afkortingen wél OK — daar gaat snelheid boven volledigheid.

9. **Geen leftovers — ongebruikte code weg.** Scripts, modules, tests, frontmatter-velden en docstring-verwijzingen die geen functie meer hebben gaan weg (`git rm`), niet "voor later". One-off migratie- en backfill-scripts worden verwijderd zodra ze hun werk gedaan hebben. ADRs en docstrings die naar verwijderde code refereren worden in dezelfde commit bijgewerkt. Bij twijfel: kort vragen, anders weg.

---

## Technisch

### Mappenstructuur

```
certificaid/
├── CLAUDE.md                    # Deze wegwijzer
├── docs/
│   ├── content-richtlijnen.md  # Schrijfregels voor fiches
│   ├── po-builder.md           # Programmaonderdeel-build procesflow (legacy)
│   ├── bronnen-pipeline.md     # Bronnen toevoegen en verwerken
│   └── adr/                    # Architecture Decision Records
├── content/
│   ├── programmaonderdelen/    # Programmaonderdeel-fiches (catalogus per vak, legacy)
│   ├── competenties/           # Competentie-fiches (technieken)
│   ├── materie/                # Materie-fiches (concepten)
│   └── bronnen/                # Primaire bronnen als site-content
├── resources/
│   ├── bronnen/                # Doorzoekbare bronbestanden (grep/Read)
│   │   ├── wetteksten/         # Wetteksten als markdown
│   │   ├── normen/             # ITAA-normen
│   │   └── adviezen/           # CBN-adviezen
│   ├── source_config.yaml      # Enige bron van waarheid voor alle bronnen
│   └── po-builder-prompt.md    # Startbericht po-builder scheduled agent (legacy)
├── tools/
│   ├── download/               # Bron ophalen (CBN-adviezen, ITAA-normen)
│   ├── etl/                    # PDF/HTML → markdown wetteksten + reprocessing
│   ├── rag/                    # ChromaDB-index bouwen + bevragen
│   ├── extractie/              # Concept- en keyword-extractie
│   ├── examen/                 # Examenpatronen + question review
│   ├── export/                 # Externe exports (NotebookLM)
│   └── lib/                    # Gedeelde bibliotheken (retrieval, cleanup)
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
