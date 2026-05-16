# ADR-010: Leermateriaal & tutor

**Status**: Draft
**Datum**: 2026-05-07
**Vervangt**: archive/ADR-007 (confidence-labeling — geherframed als output-conventie), archive/ADR-011 (Streamlit), archive/ADR-013 (Quartz)

## Context

Twee output-vormen vragen tegengestelde stabiliteits-eisen:

- **Tutor** — interactief; lage latency tussen wijziging in concept en wat de student ziet is een feature ("ah, ik heb het concept verbeterd, de tutor weet het meteen")
- **Leermateriaal** — fiches die de student bestudeert; *moet* stabiel zijn want anders verandert leerstof onder de student z'n voeten

Beide putten uit dezelfde concepten-laag, maar via verschillende paden.

Daarnaast: studenten moeten weten of een uitspraak in een tutor-antwoord of fiche direct uit een gezagsvolle bron komt of een redenering is. Een fout geciteerde wet of stilzwijgend "grounded" claim kan tot foutieve examen-antwoorden leiden.

## Beslissing

### 1. Tutor draait *direct* op concepten

- Leest live `data/concepten/records/` en `data/programma/exam_patterns/` via NetworkX (ADR-007) + concepten-RAG (ADR-006)
- Wijziging in concept → onmiddellijk reflecteerbaar in tutor-antwoord
- Frontend: Streamlit (lokaal), `tutor/app.py`

### 2. Leermateriaal = release-snapshot

```
[concepten-set huidig]
   → snapshot trigger (handmatig)
   → fiches genereren (concept × output-template)
   → versie-tag (`v2026.05.07`)
   → committed naar `content/snapshots/v2026.05.07/`
   → changelog.md per snapshot (welke concepten veranderden t.o.v. vorige snapshot)
```

**Append-only**: oude snapshots blijven leesbaar. Tussentijdse concept-wijzigingen verschijnen *niet* in de gepubliceerde leerstof tot een nieuwe snapshot getrokken wordt.

### 3. Confidence-labeling overal (⚖️/🤖)

| Label | Symbool | Betekenis |
|---|---|---|
| `grounded` | ⚖️ | Direct traceerbaar naar bron met hoge autoriteit (`itaa_lex` of `interpretatief`) |
| `inferred` | 🤖 | Redenering, constructie, analogie zonder directe bronverwijzing |

- **In tutor**: elke claim inline gelabeld
- **In fiches**: per sectie of blok
- **In concept-records**: per veld (zie ADR-008)

Bron-claim zonder verwijzing = ⚠️ te verifiëren, **nooit** stilzwijgend ⚖️. Tutor-systeemprompt en fiche-generator dwingen dit af.

### 4. Fiche-structuur

- Eén concept = één fiche (in de snapshot)
- Programmaonderdeel-fiches zijn navigatie (welke concepten, welke voorbeeldvragen) + voorbeeldvragen, geen content-duplicatie
- Fiche-template per node-type (begrip-fiche ziet er anders uit dan procedure-fiche of beginsel-fiche)

### 5. Site-generator

Quartz (Obsidian-compatibel, wikilinks, GitHub Pages). Leeft op `content/snapshots/<huidige>/` voor publieke site; oudere snapshots blijven via versie-routes bereikbaar.

### 6. Kenniselement-dekkingscheck als release-gate

Vóór een snapshot publiceerbaar is moet de kenniselement-dekkingscheck (ADR-002) groen zijn voor de programmaonderdelen in scope. Anders: blocking warning + lijst gaten.

## Drie-lagen render-architectuur (2026-05-15)

Uitbreiding op §4 (fiche-structuur): drie aparte content-types, elk met eigen render-pad.

```
BRON → CONCEPT-records → [deterministisch] → content/concepten/<id>.md
                       → [deterministisch] → content/competenties/<id>.md
                       → [skeleton + Opus-glue] → content/studiemateriaal/<X.Y>/minicursus.md
```

**Concept-fiche** (`render_concept_fiche.py`): volledig deterministisch uit `data/concepten/records/<id>.json` (schema 1.4 sinds 2026-05-16, ADR-007). Geen LLM. Output: Quartz-markdown met frontmatter, TL;DR-callout (uit eerste-zin definitie), edges-breadcrumb per type (onderdeel-van/bevat/uitzondering-op), bouwsteen-blok (titel/wat/waarom/voorbeeld_inline/grondslag), formule-blok (formules[] met variabelen + invulling_voorbeeld), aspect-ankers, stap-blok-render (substappen met type-iconen 📊🧮📝💬🌊), vergelijkingsparen-collapsible (alleen verwarring-risico), voorbeeld-minimum-callout `> [!todo]` bij gap, "Zie ook"-sectie, provenance-footnotes.

**Competentie-fiche** (`render_competentie_fiche.py`): volledig deterministisch uit `data/concepten/competenties/<id>.yaml` (competentie-schema 1.1 sinds 2026-05-16). Anti-fabricatie-validator (`validate_competentie.py`) runs vóór render — skip bij fouten. Output: procedure-grondslag-badge + stap-blok-render (wat/waarom/input[]/output[]/hoe/voorbeeld.substappen/valkuilen) + beslisboom + voorbeelden + concept-grid. Valkuilen renderen `> [!warning]`-callout met `advies` als titel (correcte aanbeveling) — niet meer de foute aanname.

**Minicursus** (`render_minicursus.py`): twee-fase render. Fase 1 deterministisch (skeleton + cheatsheet + wikilinks uit leerpad). Fase 2 via Opus-subagent (glue-prompt `prompts/minicursus-glue-v1.md`) die placeholders vult — uitsluitend rationale/transities/pedagogische inleiding, geen feiten-claims. **Examenfocus**-sectie krijgt `> [!question]`-callouts uit `_programmaonderdeel_classificatie.json` × `examen_vragen/<jaar>.json`.

**Fase D** (`propose_competenties.py`): schrijft subagent-instructies voor Opus om competentie-YAML's te destilleren. Input: anchors + records + exam_patterns (NIET examenvragen — ADR-008 §0). Verplichte prompt: `prompts/competentie-destillatie-v2.md`.

**Fase E** (`propose_leerpad.py`): schrijft subagent-instructies voor Opus om leerpad-YAML op te stellen. Vereist: competenties met status `voorgesteld` of `gecureerd`.

**Naam-cast** (`data/concepten/casts/globaal.yaml`): vaste fictieve namen + scenario-templates die alle records/competenties consistent gebruiken in voorbeelden. Vervangt ad-hoc M/D/X/Y/ABC/DEF.

**Synthese-records** (node_type: synthese): cluster-records met vergelijkingstabel + Mermaid-beslisboom + kerninzichten. Tweede render-tak in concept-fiche-template (alleen voor synthese-type-records).

Verwijzingen: ADR-007 §schema 1.4 (stap-blok + bouwsteen-blok + formule-blok + edges-types + node_type synthese + cast-conventie + voorbeeld-minimum); ADR-008 §14–17.

### Records → RAG-index → rendered fiche

De source-of-truth voor zowel **leermateriaal** als **RAG-index** zijn de records in `data/concepten/records/` (concepten, schema 1.3) en `data/concepten/competenties/` (competenties, schema 1.0). Daaruit lopen twee onafhankelijke renderpaden:

```
data/concepten/records/<id>.json  ──┬─► [render_concept_fiche.py]  ─► content/concepten/<id>.md   (leermateriaal)
                                    └─► [rag_index.py concepten]    ─► chroma:concepten            (retrieval)

data/concepten/competenties/<id>.yaml ──┬─► [render_competentie_fiche.py] ─► content/competenties/<id>.md
                                        └─► [rag_index.py concepten]       ─► chroma:concepten
```

Beide paden zijn deterministisch en starten vanuit hetzelfde record. De RAG-index leest **niet** uit `content/` — anders zou een Quartz- of template-aanpassing zonder kenniswijziging de embeddings veranderen. Zie ADR-006 §5 voor de embed-tekst-compositie en metadata-velden.

Volgorde-discipline bij wijzigingen:
1. Record wijzigen
2. Re-render fiche (`tools/leermateriaal/render_*`)
3. Re-index `concepten`-collectie (`tools/rag/rag_index.py --collection concepten`)
4. Tutor: cache-TTL volstaat in dev; in productie expliciete rerun

Tutor-interactie: een retrieval-hit uit de `concepten`-collectie kan optioneel de bijbehorende rendered markdown uit `content/concepten/<id>.md` als volle context aan Claude geven — record-projectie voor recall, rendered fiche voor leesbaarheid bij de generatie.

## Gevolgen

- `tutor/app.py` — Streamlit, leest concept-laag direct
- `tools/leermateriaal/` — drie-lagen render-tooling (concept, competentie, minicursus)
- `content/concepten/` — deterministisch gegenereerde concept-fiches
- `content/competenties/` — deterministisch gegenereerde competentie-fiches
- `content/studiemateriaal/<X.Y>/minicursus.md` — skeleton + Opus-glue
- `data/concepten/competenties/` — competentie-YAML's (schema 1.0)
- `data/concepten/leerpaden/` — leerpad-YAML's per programmaonderdeel
- Tutor en renderer delen template-logica voor confidence-labeling en wikilink-resolutie
