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

### Callout-conventies (2026-05-16)

Quartz-callouts (`> [!type]`) zijn de visuele drager voor "pedagogische kruimels" in render. **Conventie: elk schema-veld met didactische context-functie krijgt een vast callout-type**. Geen callout in plain markdown-paragraaf laten staan.

| Schema-veld | Callout-type | Collapsible | Titel-veld |
|---|---|---|---|
| TL;DR (eerste zin uit `definitie.text` of `main_rule.text`) | `> [!summary]` | nee | "Korte inhoud" |
| `voorbeeld_inline` op record-niveau | `> [!example]-` | ja | "Voorbeeld" |
| `bouwsteen.voorbeeld_inline` | `> [!example]-` | ja | "Voorbeeld" (compact) |
| `berekeningsmethode[*].formules[*].invulling_voorbeeld` | `> [!example]-` | ja | "Voorbeeld-invulling" |
| `voorbeeld.scenario` + `voorbeeld.substappen[*]` (op stap-niveau) | `> [!example]-` | ja | "Voorbeeld: {scenario-1-zin}" |
| `valkuilen[*]` (één per item) | `> [!warning]-` | ja | het `advies`-veld (correcte aanbeveling) |
| `vergelijkingsparen[*]` (één per paar) | `> [!info]-` | ja | "Niet verwarren met [[concept]]" |
| `in_praktijk[*].herkenningspunt` | `> [!tip]-` | ja | "Herkennen op het examen" |
| Voorbeeld-minimum-gap (geen voorbeeld in record) | `> [!todo]` | nee | "Voorbeeld ontbreekt" |
| Open gap-entry uit `gaps.json` voor dit record | `> [!todo]` | ja | het `aspect`-veld |
| Examenvraag in minicursus (uit `_programmaonderdeel_classificatie.json`) | `> [!question]-` | ja | "{examen_id}-vr{nr} ({punten} punten)" |
| Edges van type `onderdeel-van` / `specialisatie-van` (concept-fiche) | inline `> [!info]` | nee | "Behoort tot: [[X]] · ..." (één regel) |
| Edges van type `uitzondering-op` | inline `> [!info]` | nee | "Uitzondering op: [[X]]" |
| Edges van type `getriggerd-door` / `vereist-kennis-van` | sectie "## Zie ook" met bullets, géén callout | — | — |

**Render-regels**:
- Collapsible (callout-type met `-` suffix) vermindert visuele clutter — alle illustratie-content is collapsible
- TL;DR-callout altijd open (kerncategorie, geen ruis)
- Voorbeeld-minimum-todo altijd open (signaal voor curator)
- Niet-collapsibele inline-callouts (breadcrumb-style) blijven tot maximaal 1 regel
- Geen geneste callouts (bv. valkuil binnen voorbeeld) — splits in twee aparte callouts

### Jinja2-template-discipline (2026-05-16)

Quality-pass na Sessie 4 onthulde een terugkerend patroon van rendering-bugs door het samenspel van Jinja2 `trim_blocks=True` (zie `tools/leermateriaal/lib/jinja_env.py`) en CommonMark blockquote-lazy-continuation. Discipline-regels voor alle templates in `tools/leermateriaal/templates/`:

1. **Twee blank lines tussen callout en volgende blok** — `trim_blocks` eet de newline na een `{% endif %}` of `{% endfor %}` op. Eén bron-blank-line wordt dus één output-newline, wat Quartz/CommonMark als lazy-continuation behandelt: de volgende paragraaf wordt opgenomen in de callout. **Vereist**: twee bron-blank-lines tussen `> [!type]`-callout en wat erna komt.

2. **Twee blank lines binnen `{% for %}`-loops** met opeenvolgende callouts (bv. valkuilen, vergelijkingsparen) — zelfde oorzaak: één blank-line tussen iteraties wordt na trim één newline, dus consecutive callouts mergden in één blokquote. **Vereist**: twee bron-blank-lines aan het einde van de loop-body.

3. **Geen geneste callouts** — Quartz rendert `> > [!type]` niet als geneste expandable; splits in twee parallelle callouts.

4. **`> `-prefix op elke regel binnen een callout** — `{{ tekst | indent(2) }}` is FOUT voor callout-content (2 spaces breken eruit). Gebruik `{{ tekst | replace('\n', '\n> ') }}` om elke regel als blockquote-content te houden.

5. **`eerste_zin`-filter i.p.v. `.split('.')[0]`** voor callout-titels — `.split('.')` brak op Belgische €-bedragen (€ 1.600.000) en juridische afkortingen (WVV art. 1:26). De `eerste_zin`-filter (in `jinja_env.py`) is duizendtal- en afkorting-veilig.

6. **Loop-separators met `loop.last`-check** — `[[X]] · {% endfor %}` produceert een dangling ` · ` aan het einde. Gebruik altijd `{% if not loop.last %} · {% endif %}` of het Jinja `join`-filter.

7. **Render-output-bescherming** — `render_minicursus.py` overschrijft geen bestaande minicursus.md wanneer die geen `<!-- TODO: Opus-glue` placeholders meer bevat (Opus-glue is dan al ingevuld). Override via `--forceer`-flag.

Render-implementatie in `tools/leermateriaal/templates/partials/*.md.j2` — wijzigingen aan deze conventie vereisen template-aanpassing + tests in `tests/test_leermateriaal_render.py`.

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
