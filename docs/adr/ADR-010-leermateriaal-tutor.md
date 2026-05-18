# ADR-010: Leermateriaal & tutor

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-18 (interpretatieve-laag-shift + bidirectionele edges + glue v3)
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
- Fiche-template per node-type (begrip-fiche ziet er anders uit dan cluster-fiche of regel-fiche)

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
| `voorbeelden[*]` op record-niveau (schema 1.5; was: `voorbeeld_inline`) | `> [!example]-` | ja | "Voorbeeld" |
| `bouwsteen.voorbeelden[*]` (schema 1.5; was: `bouwsteen.voorbeeld_inline`) | `> [!example]-` | ja | "Voorbeeld" (compact) |
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

### Leermateriaal-laag als interpretatieve laag (2026-05-18)

Tot nu toe was de impliciete aanname dat leermateriaal = render van de concept-laag (één-op-één-mapping van record naar fiche, plus minicursus-skeleton dat wikilinks rondom een leerpad weeft). Sessie-feedback 2026-05-18 zette die aanname om: een student leest concepten niet zoals een graph ze codificeert. Leermateriaal moet de modellaag **interpreteren**, niet renderen.

Deze sectie codificeert die shift en de gevolgen voor schema, render-paden en prompts.

#### Heuristiek: hoort dit in de concept-laag of de leermateriaal-laag?

```
Wanneer wil je dit aanpassen?
├── Samen met de regel/definitie (een nieuwe regelwijziging dwingt dit mee) → concept-laag
└── Bij het schrijven van een specifieke minicursus (per leerpad anders)   → leermateriaal-laag
```

**Concept-laag** (data, samen-aanpassen-met-regel):
- `definitie`, `main_rule`, `bouwstenen[]`, `uitzonderingen[]`, edges
- `situering` (schema 1.6, ADR-007): waarom bestaat dit concept, in welk veld zit het
- `in_praktijk[]`: hoe gebruik je dit (praktische kenmerken / handelingen)
- `rationale.text`: welk beginsel verklaart dit
- `voorbeelden[]`, `illustraties[]`: concrete cases met cast

**Leermateriaal-laag** (interpretatief, per leerpad):
- Verhaallijn en volgorde
- Transities en bruggen tussen secties
- Pedagogische framing per PO ("dit is een van drie reserves; vergelijk met X en Y")
- Examenfocus-rubriek (ADR-009 §6)
- Synthese-records ingebed in leerverhaal
- Compactie / herverwoording / parafrase (mits traceerbaar)

#### Implicatie 1 — Concept-fiche blijft "naked reference"

Concept-fiches zijn opzoek-vorm + tutor-RAG-context, **geen** zelfdragend leesmateriaal. De structuur "hoofdregel-bouwstenen-uitzonderingen-voorbeelden" mag mechanisch aanvoelen — dat is correct voor een referentie-document. Het missende verbindweefsel zit in de minicursus, niet op de fiche.

Wel toegevoegd op de fiche: **situering**-paragraph (ADR-007 schema 1.6) bovenaan, boven TL;DR. Dat is data-laag-content (samen-aanpassen-criterium) en biedt minimale zelfdragendheid voor wie via tutor of zoek-resultaat binnenkomt zonder de minicursus te lezen.

`render_concept_fiche.py` aanpassing: na frontmatter → situering-paragraph (indien aanwezig) → TL;DR-callout → rest. Geen callout-wrapper rond situering (zie ADR-007 §situering).

#### Implicatie 2 — Synthese-records: geen losse fiche, wel volwaardig record

`node_type: synthese`-records (vergelijkingstabel + mermaid-beslisboom + kerninzichten) zijn pedagogische clusters die uitsluitend zin hebben binnen een leerverhaal. Een losse synthese-fiche zou:
- Decontextualiseerd zijn (wat moet de student er mee zonder leerpad-omhulling?)
- Duplicatie produceren met de minicursus die hem hoe dan ook inbedt
- Een 1:1-mapping suggereren tussen records en content-files, die juist *niet* meer geldt

**Wat verandert** (alleen het render-pad concept-fiche):
- `render_concept_fiche.py` skipt records waar `node_type == "synthese"`
- Geen losse pagina `content/concepten/<synthese-id>.md` op de site
- Bestaande gerenderde synthese-fiches worden bij volgende render verwijderd door content-sync (ADR-019)

**Wat NIET verandert** (synthese-record blijft volwaardig):
- ✅ Synthese-record blijft in `data/concepten/records/<id>.json` — voorgesteld door EXTRACT v4, gecheckt door VERIFY
- ✅ Records-API (`save_record` / `rename_record` / `delete_record` + audit-parity, ADR-019) werkt onveranderd
- ✅ Synthese-record blijft geïndexeerd in concepten-RAG-collectie (ADR-006) — tutor kan ernaar retrieven
- ✅ Tutor / NetworkX graph-walks (ADR-007) lezen synthese-records mee
- ✅ Wikilinks **vanuit andere records** naar `[[synthese-id]]` blijven geldig op data-niveau

**Inbedding in minicursus** (vervangt de losse fiche):
- `render_minicursus.py` pakt synthese-records uit het leerpad-YAML via `thematisch.synthese_id`-binding (of nieuw hoofdstuk-type `synthese` indien zinvoller — te beslissen bij §6.3-implementatie)
- Render plaatst vergelijkingstabel + mermaid-beslisboom inline op de aangewezen plek in het leerverhaal
- Wikilinks naar `[[synthese-id]]` resolveren naar een anchor-link **binnen die minicursus** (waar de synthese ingebed is)

**Wikilink-gedrag elders** (anti-dangling):
- Wikilink in concept-fiche A → `[[synthese-X]]`: er bestaat geen pagina synthese-X. Render-validator behandelt dit als dangling-wikilink: toont als platte tekst + curator-warning. Mitigatie: synthese-records moeten via edges-render bereikbaar zijn (impliciet, niet via expliciete wikilink in fiche-prose) of de synthese hoort niet in een fiche.
- Wikilink in minicursus B → `[[synthese-X]]`, maar minicursus B bedt synthese-X niet in: render-warning + platte-tekst-fallback.
- Wikilink in minicursus B → `[[synthese-X]]`, en minicursus B bedt synthese-X in: anchor-link binnen pagina, correct gedrag.

Samengevat: **"synthese-skip" betekent uitsluitend dat er geen losse pagina gerenderd wordt** — niet dat het record verwijderd of geblokkeerd wordt voor andere consumers. De synthese leeft als data-record en als ingebedde minicursus-sectie, niet als zelfdragend referentie-document.

#### Implicatie 3 — Minicursus mag parafraseren (glue-prompt v3)

Glue-prompt v2 (`prompts/minicursus-glue-v2.md`) verbiedt "feits-claims, wettekst-citaties, wikilinks bedenken" — correct voor een pure-render-architectuur, maar te streng voor de interpretatieve laag.

**Glue-prompt v3** (te schrijven: `prompts/minicursus-glue-v3.md`) versoepelt naar **parafrase-met-bronlink**:

| Toegestaan | Niet toegestaan |
|---|---|
| Parafraseren van een record-veld in cursus-stem, mits `[[concept-id]]`-wikilink bij de claim | Feit verzinnen zonder record-grondslag |
| Concept verbinden aan eerder behandeld concept ("zoals we zagen bij [[X]]") | Wikilink naar non-existent record |
| Compacte synthese: "kort: dit zijn drie reserves die elkaar opvolgen in prioriteit" mits afgeleid uit edges-structuur | Wettekst-citaat als prozetekst (citeren mag wel als blockquote met bron) |
| Pedagogische framing: "let op het verschil tussen X en Y" (verwijst naar bestaande `vergelijkingsparen[]`) | Examenvraag-spoiler of vraag-camouflage in framing |
| Voorbeeld-introductie ("stel je voor: …") als brug naar een record-voorbeeld | Voorbeeld bedenken (de illustraties komen uit records, niet uit de glue) |

**Anti-fabricatie-discipline**: élke claim met feitelijk gewicht krijgt `[[record-id]]`-wikilink in dezelfde zin. Render-laag valideert: een paragraaf zonder wikilink mag geen wettekst- of cijfer-claim bevatten. Validator faalt build bij overtreding (vergelijkbaar met `validate_competentie.py`).

Glue-output blijft compact (richtlijn 700–1100 woorden per minicursus, conform v2). Compactheid + parafrase-vrijheid = grotere informatie-dichtheid per zin, niet meer woorden.

#### Implicatie 4 — Examenfocus als eind-rubriek (verwijzing)

Zie ADR-009 §6. Eind-rubriek "Examenfocus" na alle inhoudelijke H2's; collapsed `> [!question]-`-callouts; AI-varianten visueel apart met 🤖 in eigen subkop. Eenrichtingsverkeer: concept-records hebben geen edge terug naar `examenfocus`.

#### Implicatie 5 — Examenprogramma sturend in minicursus (taak-binding)

Het ITAA-examenprogramma (`data/programma/programma.json`) heeft per PO **niveau** (kennen / begrijpen / toepassen / integratie), **taken** met **doelstellingen**, en hiërarchische **kenniselementen**. Tot 2026-05-18 droeg de minicursus niets van die structuur uit — de student leerde wel de leerstof maar wist niet *wat het examen van hem verwacht*. Drie render-toevoegingen koppelen de minicursus expliciet aan de examen-eisen.

##### A — Vroege oriëntatie-sectie "Wat verwacht het examen van jou?"

Eerste H2 van elke minicursus, vóór alle inhoudelijke hoofdstukken. Bevat:

- **Niveau-callout** (`> [!abstract]`, niet collapsible): "Dit programmaonderdeel wordt getoetst op niveau *{niveau}*." plus één-zin-toelichting per niveau-type. Niveau staat prominent omdat het diepte van studeren bepaalt (een *toepassen*-PO leer je anders dan een *kennen*-PO).
- **Taken-lijst**: korte titels + doelstellingen-aantal. Compact — geen volledige verbose tekst (die zit in programma.json voor wie doorklikt).
- **Geen kenniselementen-dump** in oriëntatie — kenniselementen mappen op concept-wikilinks elders in de cursus.

Brontekst voor de niveau-toelichtingen wordt vastgelegd in `docs/studiemateriaal-schrijfregels.md` (§6.3, te schrijven) zodat alle minicursussen consistent zijn.

##### B — Per-hoofdstuk taak-marker (inline)

Aan begin van elke inhoudelijke H2: `> [!info]` callout (niet collapsible, één regel) met "Hoort bij taak X: *{korte taak-titel}*" of "Hoort bij taken X, Y, Z" indien meerdere. Maakt taak-binding zichtbaar tijdens lezen, niet alleen aan einde.

Voorbereidings-hoofdstukken (zie D) krijgen géén taak-marker maar een eigen `> [!note]`-callout: "*Voorbereidende kennis — fundament voor de taken hierna.*"

##### C — Eind-dekking-dashboard "Heb je deze taken in de vingers?"

Eindsectie van de minicursus, **vóór** de examenfocus-rubriek (ADR-009 §6). Zelftoets-vorm: lijst van alle taken van het PO, per taak:

- ✓/⚠/✗-indicator (gedekt via N secties / deels gedekt / niet gedekt in deze cursus)
- Bij gedekt: "→ secties §{N}, §{M}" (anchor-links binnen de minicursus)
- Bij niet gedekt: "→ behandeld in [[minicursus-X.Y]]" indien cross-PO, anders curator-warning

Toon: zelftoets, niet examen-vraag. Bv. *"Kun je nu zelf [taak-formulering] aanpakken? Loop §3 en §5 nog eens door als je twijfelt."*

##### Automatische taak-binding (render-tijd lookup)

```
hoofdstuk
  → records in wikilinks
    → record.linked_anchors[]  (schema 1.5+ standaard veld)
      → anchor.anchor_id
        ├── "X.Y.taak.N"           → direct: taak X.Y.taak.N
        └── "X.Y.<ke-code>"        → kenniselement → doelstelling.anchor_role
                                     → taak (via programma.json hiërarchie)
```

Geen schema-bump op records — `linked_anchors` + `_provenance.anchor_id` + `_provenance.dekt_ook_anchors` bestaan al sinds schema 1.5. Implementatie als `tools/leermateriaal/lib/taak_binding.py` (nieuw): één functie `resolve_taken(hoofdstuk, programma_json) → set[taak_code]`.

**Validatie**:
- Hoofdstuk met `type != voorbereiding` en 0 resolveerbare taken → curator-warning (signaal voor slechte binding of ontbrekend `voorbereiding`-label). Niet fail-build.
- Taak zonder dekking in eind-dashboard krijgt expliciet ✗-indicator + curator-warning — een ongeziene taak in eind-dashboard is een echt gat.

**Niveau-respect in glue-prompt v3**: glue krijgt PO-niveau als input. Voor *toepassen*/*integratie*-PO's: werkwoorden in hoofdstuk-intro's mogen niet beperkt zijn tot *kennen*/*begrijpen* ("we leren wat X is" is te dun voor toepassen-niveau; "je leert X toepassen op casussen met..." past). Concrete stijl-richtlijn landt in `docs/studiemateriaal-schrijfregels.md` (open punt §6.3).

##### D — Voorbereiding als hoofdstuk-type (leerpad-schema 1.1)

Sommige hoofdstukken zijn fundament voor de taken zonder zelf één-op-één op een taak te mappen (bv. *"Wat is een geconsolideerde balans"* — concept-cluster dat alle latere taken nodig hebben). Drie patronen voor zo'n hoofdstuk:

1. Niet labelen → validator klaagt over 0 taak-binding (vervelend voor curator)
2. Forceren-en-loggen → fout signaal naar student ("dit hoort bij taak 1" terwijl het bij taak 1+2+3 hoort)
3. **Expliciet `type: voorbereiding`-hoofdstuk** ← gekozen

Leerpad-schema bumpt naar 1.1 met nieuw hoofdstuk-type:

```yaml
- type: voorbereiding
  titel: "De drie consolidatie-methodes — fundament"
  concepten:
    - integrale-consolidatie
    - evenredige-consolidatie
    - vermogensmutatiemethode
  rationale_hint: "fundament voor taken 1.4.taak.1 t/m 1.4.taak.4"
```

Render-gedrag voor `voorbereiding`-hoofdstukken:
- Géén taak-marker (B), wel `> [!note]` "Voorbereidende kennis — fundament voor de taken hierna."
- Komen in eind-dashboard **niet** voor — student wordt niet "getoetst" op fundament.
- Validator: een PO mag niet voor 100% uit `voorbereiding`-hoofdstukken bestaan (dan klopt de taak-mapping niet).

Granulariteits-keuze: voorbereiding bestaat alleen op **hoofdstuk-niveau**, niet op concept-niveau binnen een ander hoofdstuk. Reden: een concept zonder taak-binding binnen een taak-hoofdstuk is fundament-voor-die-taak — geen apart label nodig.

Zie ADR-007 §leerpad-schema voor de volledige schema 1.1-shape.

### Bidirectionele edge-render (§6.1, 2026-05-18)

Data-laag bewaart edges één-richting (op de source-node, ADR-007 §edge-richting). Render-laag toont edges **bidirectioneel** via een pre-render index-pass.

**Pre-render index-pass** (één keer per render-run):

```python
inverse_edges: dict[str, list[tuple[str, str]]] = {}
for record in load_all_records():
    for edge in record["edges"]:
        inverse_edges.setdefault(edge["target_id"], []).append(
            (record["id"], edge["type"])
        )
```

Templates lezen zowel `record["edges"]` (uitgaand) als `inverse_edges[record["id"]]` (inkomend) en plaatsen ze conform onderstaande tabel.

**Omkerings-labels per edge-type** (target-perspectief):

| Edge (source → target) | Render op source-fiche | Render op target-fiche (inverse) | Bidirectional |
|---|---|---|---|
| `onderdeel-van` (X → Y) | "Behoort tot: [[Y]]" (breadcrumb) | "Bestaat uit: [[X]], [[…]]" (onder TL;DR) | ✅ |
| `specialisatie-van` (X → Y, regime=Z) | "Specialisatie van: [[Y]] (regime: Z)" | "Specialisaties per regime: [[X]] (Z), …" | ✅ |
| `vereist-kennis-van` (X → Y) | "Vereist kennis van: [[Y]]" (Zie ook) | "Wordt voorondersteld in: [[X]], …" (Zie ook) | ✅ |
| `vergelijkt-met` (X ↔ Y) | "Vergelijk met: [[Y]]" (info-callout) | symmetrisch (zelfde label) | ✅ (symmetrisch) |
| `getriggerd-door` (X → Y) | "Getriggerd door: [[Y]]" | "Triggert: [[X]], …" | ✅ |
| `uitzondering-op` (X → Y) | "Uitzondering op: [[Y]]" (onder TL;DR) | "Uitzonderingen: [[X]], …" (sectie op target) | ✅ |
| `verwijst-naar` (X → Y) | "Verwijst naar: [[Y]]" (Zie ook) | — (te ruis als catch-all) | ❌ opt-out |

**Implementatie-discipline**:
- Inverse-rendering plaatst ALLE inkomende edges van het bidirectionele type in één gegroepeerde callout/sectie — geen lijst van afzonderlijke callouts per inkomende edge (visuele ruis).
- Bij meer dan ~7 inkomende edges van hetzelfde type: collapsible callout (`> [!info]-`) met aantal in de titel ("Bestaat uit: 12 onderdelen").
- `verwijst-naar` rendert alleen uitgaand. Reden: het is de catch-all-edge en zou anders elke node die ergens naar verwijst opspatten met dozijnen "verwezen-door"-entries.
- Edge-config gecentraliseerd in `tools/leermateriaal/lib/edge_render_config.py` (nieuw bestand). Single source of truth voor wat-rendert-bidirectioneel.

**Niet** in scope van §6.1: edges naar non-existent records (dangling). Die worden al gevangen door bestaande `_dangling`-flag (ADR-007). Render skip-rendert dangling-edges met een TODO-callout voor de curator.

### Versionering vervangen door diff-changelog (2026-05-18)

§2 van dit ADR ("Leermateriaal = release-snapshot" met `content/snapshots/<v>/`-append-only-pad) is **gesuperseded** door deze sectie. Achtergrond: het snapshot-model nam aan dat leermateriaal één-op-één een gerenderd record was en dus stabiel gevroren kon worden. De interpretatieve laag (§implicatie-1 t/m 5) maakt dat duurder dan nuttig — een minicursus is een net van wikilinks over levende records, en de hele dependency-tree bevriezen is overhead die niemand vraagt.

**Wat de student écht nodig heeft**: niet "de leerstof verandert niet meer", maar *"als hij verandert tussen mijn voorbereidingsruns, wil ik weten **wát** veranderd is zodat ik gericht kan terugkijken."*

#### Model — git-tag + diff-changelog

```
v1.0-tag (eerste publieke release; user-triggered "dit is v1.0")
  ↓
continu evoluerende content/  (records-API + render-pipeline blijven gewoon doorwerken)
  ↓
bij elke deploy: changelog-generator
  ↓
Quartz-site:
  - /changelog/ pagina  (chronologisch, alle wijzigingen sinds v1.0 of vorige tag)
  - per-fiche badge   ("Bijgewerkt sinds v1.0" indien recent gewijzigd)
```

**Geen** `content/snapshots/<v>/`-directory. **Geen** kopieën van content per release. Git-history *is* het snapshot-mechanisme; changelog-pagina is de leesvorm voor de student.

#### Changelog-generator (te bouwen — §6.7)

Een script `tools/leermateriaal/build_changelog.py` dat:
1. Git-diff vergelijkt tussen huidige HEAD en laatste publieke tag (default `v1.0`, overrideable)
2. Wijzigingen filtert tot `content/concepten/`, `content/competenties/`, `content/studiemateriaal/`
3. Wijzigingen classificeert per type:
   - **Inhoudelijk** — record-field-wijzigingen (definitie, bouwstenen, valkuilen, voorbeelden, ...). Hoog-signaal voor student.
   - **Render-only** — template- of styling-wijzigingen die de markdown vernieuwen zonder semantische verandering. Laag-signaal, gegroepeerd of weggelaten in changelog.
   - **Structureel** — nieuw record, verwijderd record, hernoemd record. Hoog-signaal.
4. Per minicursus aggregeert: welke onderliggende records (via wikilinks + leerpad-binding) zijn gewijzigd? Toont "minicursus X.Y: §3 raakt aan 2 gewijzigde concepten".
5. Renderet als `content/changelog/index.md` (chronologisch, nieuwste eerst) + `content/changelog/<concept-id>.md` voor diep-link per record.

**Classificatie inhoudelijk vs render-only**: heuristisch op gewijzigde regels. Een commit met enkel template-aanpassingen in `tools/leermateriaal/templates/*.j2` produceert render-only wijzigingen ondanks dat alle fiches verschillen. Een commit met record-mutaties (via records-API) produceert inhoudelijke wijzigingen. Bij twijfel: inhoudelijk (false positive is goedaardig — laag-signaal-noise; false negative = student mist een echte wijziging).

#### Per-fiche "Bijgewerkt"-badge

Render-laag voegt aan elke concept-, competentie- en minicursus-fiche een badge toe wanneer:
- De onderliggende record-JSON gewijzigd is sinds vorige publieke tag, **én**
- De wijziging als "inhoudelijk" classificeert (niet render-only)

Badge-vorm: callout `> [!update] Bijgewerkt sinds v1.0` met link naar `/changelog/<id>` voor detail.

Vervalt automatisch bij volgende tag (v1.1) — badge toont alleen wijzigingen sinds de **laatste** publieke release de student gezien kan hebben.

#### User-triggered tagging

Tags worden **niet** automatisch gezet. De curator (jij) zegt expliciet *"dit is v1.0"* of *"dit wordt v1.1"* via `git tag`. Reden: changelogs moeten betekenisvolle releases markeren (na verwerken van examen-feedback, na een PO-uitrol-batch, ...) — niet elke push.

Gevolg: tussen v1.0 en v1.1 kan de site veel commits ver liggen — changelog accumuleert alle wijzigingen. Pas bij v1.1-tag wordt de teller gereset voor de "sinds vorige release"-vergelijking; absolute changelog (sinds v1.0) blijft chronologisch op `/changelog/`.

#### Wat hiermee vervalt

- `content/snapshots/<v>/`-directory — was nooit gemaakt, blijft afwezig
- Append-only-release-pad uit §2 — vervalt
- "Tussentijdse wijzigingen verschijnen niet tot nieuwe snapshot" — vervalt; alle wijzigingen verschijnen direct op de live site, met badge + changelog als context

#### Wat blijft uit §2

- **Confidence-labeling overal** (§3, ⚖️/🤖) — onveranderd, doorgaande discipline
- **Kenniselement-dekkingscheck als release-gate** (§6) — verschuift naar v1.0-tag-criterium in plaats van snapshot-criterium. Vóór je de v1.0-tag zet, moet de dekkingscheck groen zijn voor de PO's in scope. Na v1.0 mag de check ook geel staan op nieuwe PO's-in-uitrol — die tonen als "in ontwikkeling" op de site.

### Studiemateriaal-schrijfregels (§6.3, placeholder, 2026-05-18)

Een apart document `docs/studiemateriaal-schrijfregels.md` (te schrijven) is nodig — analoog aan `docs/concept-schrijfregels.md` voor de data-laag. Scope:

1. **Parafrase-grens**: wanneer mag je een record-claim herverwoorden, wanneer letterlijk citeren? Hoe markeer je wettekst-citaten?
2. **Wikilink-discipline**: élke feitelijke claim krijgt wikilink; geen wikilink = geen feitelijke claim toegestaan.
3. **Voice / stem**: minicursus spreekt de student aan ("jij ziet" / "let op"); concept-fiches niet (referentie-toon).
4. **Doorlink-conventies**: wanneer link je vanuit minicursus naar een concept-fiche door, wanneer parafraseer je intern? Heuristiek: parafraseer als de claim 1 zin nodig heeft; doorlink als hij 2+ zinnen vraagt.
5. **Examenrubriek-vorm**: vaste sectie-titel, callout-types, AI-variant-markering (kruisverwijzing ADR-009 §6).
6. **Synthese-inbedding**: hoe rendert een synthese-record binnen een minicursus-hoofdstuk?
7. **Compactheidscontract**: glue-richtlijn 700–1100 woorden totaal, intro's 2–3 zinnen, examenfocus eind-rubriek.
8. **Anti-fabricatie-grens**: wat valideert de glue-renderer, wat is reviewer-verantwoordelijkheid?

Status: te schrijven *na* deze ADR-revisie. Codewerk (template-aanpassingen, glue v3, edge-render-config) start parallel met dit doc — beide hangen aan deze ADR.

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
