# ADR-024: Visuele LLM-interpretatie van examenvragen via per-vraag artefacten

**Status**: Accepted (2026-05-21 — POC op 6 vragen empirisch gevalideerd, schema 1.1 vastgelegd)
**Datum**: 2026-05-20 (Draft) · 2026-05-21 (Accepted — schema 1.1 + POC-lessons)
**Supersedes (deels)**: ADR-021 v3.x (regex-detectoren blijven als baseline-laag, niet als waarheid), ADR-022 (herinterpretatie wordt regel, niet uitzondering), ADR-020 (modelantwoord-pipeline herzien), ADR-023 (blok-types-schema vervangen door v1.1 — `mc_keuze`/`juist_fout`/`topic_syllabus` als blok-type vervallen)

## Context

ADR-021 v2/v3 hebben een deterministische ETL-stack opgebouwd om examen-PDFs te parsen naar `vraagtekst_blokken[]` met 16+ typed blok-types. De stack werkt voor de **officiële** ITAA/BIBF-bundels (2013–2015, 2003-bibf, 2008-bibf): puntenkop aanwezig, vraagstam volledig, MC-alternatieven duidelijk afgebakend. Pdfplumber + 1323 regels regex-detectoren produceren bruikbare structuur.

De realiteit van de bredere examen-pool is anders. ADR-022 documenteerde dat 2024-1 een **herinnering-reconstructie** is: geen punten, fragmenten als "Stellingen Juist of Fout ivm omzettingen" zonder de stellingen zelf, typo's ("Fifi", "Takxshelter"), antwoord-hints die in de vraagtekst zijn geslopen ("100.000 – 10.000 tantième = 90.000 euro"). 2025+ zal vermoedelijk hetzelfde patroon volgen — officiële bundels worden niet meer gepubliceerd.

Voor herinnering-bronnen is "deterministisch parsen" een verkeerd kader. **Er is geen objectief juiste parse** — er is alleen een redelijke reconstructie. De huidige aanpak heeft drie symptomen:

1. **Pdfplumber-flat-text vernielt tabellen, balansen, inventarissen** die niet als visuele 2D-tabel gemarkeerd zijn. Inline proef-saldibalansen worden lopende tekst. Regex-detectoren werken voor patroon-stabiele gevallen (officiële kop "Vraag N / X punten"), niet voor versplinterde herinnering-fragmenten.
2. **Modelantwoorden zijn handgeschreven en éénmaal in `<examen>.json` gemerged.** Re-extract van de PDF kan ze stilletjes overschrijven of stale citaten produceren. Niet reproduceerbaar in de "fresh checkout → run pipeline → krijg git-state" zin.
3. **Fragment-vragen zonder echte vraagstelling worden geforceerd geïnterpreteerd** als ware het een normale vraag. Modelantwoord-pipeline schrijft dan generieke regels op een vraag die niet bestaat (zie ADR-022 §pilot, vr10 sub-A).

CLAUDE.md regel 3 verbiedt Claude API-calls in de build-pipeline. Maar regel 3 staat **niet** in de weg van lokale Claude Code subagent-runs in dev: dat is precies hoe EXTRACT v4 (concept-extractie) werkt — het prompt-artefact is permanent (`prompts/concept-extractie-v4.md`), de output landt als gecommitteerd record. Hetzelfde patroon is hier toepasbaar.

## Beslissing

### 1. Per-vraag artefact-architectuur

De waarheid verschuift van **één samengestelde `<examen>.json`** naar **per vraag drie artefacten**:

```
data/programma/examen_vragen/
├── _segmenten/<examen>/<vraag-id>/
│   ├── tekst.txt          # v2-extract tekst-segment (deterministisch)
│   ├── pagina.png         # page.to_image() of bbox-crop (deterministisch)
│   └── meta.json          # pagina-nummers, bbox, examen-id, vraag-positie
├── _interpretaties/<examen>/<vraag-id>.json
│   # LLM-output: gestructureerde vraag (vraagtekst_blokken, herkomst,
│   # volledigheid, topic-classificatie bij fragment-zonder-vraag)
├── _antwoorden/<examen>/<vraag-id>.json
│   # LLM-output: correct_antwoord_blokken[] + grondslag-citaten +
│   # eventueel record_gap_report
└── <examen>.json
    # Deterministisch samengesteld eindartefact (merger).
    # Niet handmatig editbaar; herrunbaar.
```

Drie consequenties:

- **Eén vraag = één bewerkbare eenheid.** Verbeter je 2013-1-vr8, dan raakt dat alleen `_interpretaties/2013-1/vr8.json` en evt. `_antwoorden/2013-1/vr8.json`. Andere vragen blijven onaangeraakt.
- **De grote JSON is afgeleid.** `<examen>.json` wordt opnieuw opgebouwd door de merger zodra een bouwsteen wijzigt. Re-extract van PDF kan handgeschreven werk niet overschrijven — vraag-interpretaties en antwoorden zitten in eigen paden.
- **Reproduceerbaarheid** = "fresh checkout → run merger → krijg dezelfde `<examen>.json` als in git". De LLM-stap is niet bit-exact reproduceerbaar, maar de output ervan is gecommitteerd artefact, geen runtime-call.

### 2. Vraag-isolatie (deterministisch, geen LLM)

Per examen-PDF wordt elke vraag in twee vormen geïsoleerd:

**Tekst-segment** (`tekst.txt`)
: Hergebruik van de bestaande v2-extract: vraag-header-detector knipt de PDF in vraag-stukken. Levert een tekst-fragment per vraag-id.

**Visueel segment** (`pagina.png`)
: `pdfplumber.Page.to_image(resolution=200)` levert een PNG per pagina. Voor vragen die op één pagina zitten: hele pagina-PNG. Voor vragen die meerdere pagina's beslaan: meerdere PNGs (`pagina_01.png`, `pagina_02.png`, ...). Bbox-crop tot de exacte vraag-rect is **optioneel** — alleen toepassen als het v2-segment betrouwbaar de start- en eind-y-coördinaat kan leveren. Bij twijfel: volledige pagina, met een hint in `meta.json` over de y-range.

**Meta** (`meta.json`)
: `{examen_id, vraag_id, pagina_nummers: [int], bbox_hint: [x0,y0,x1,y1]?, herkomst_pdf: "..."}`.

PNGs **niet in git** standaard (gitignore `_segmenten/**/*.png`); regenereerbaar via `python3 -m tools.examen.isoleer_vragen --examen 2014-1`. Tekst en meta wél in git zodat de agent-input volledig versioneerbaar is zonder repo-bloat.

### 3. Vraag-interpretatie-schema v1.1 (LLM, lokaal subagent)

Permanent artefact: `prompts/vraag-interpretatie-v1.md` (v1.1, 2026-05-21 — vervangt v1.0 op basis van POC-feedback).

**Conceptueel model**:
- Top-niveau is **één PDF-vraag-eenheid** (zoals "Vraag 3 / 8 punten" — wat ITAA waardeert). Houdt `vraag_id`.
- Binnen-niveau is `vragen[]`: één of meer **deelvragen binnen dezelfde context**. Elke deelvraag heeft een lokaal `id` (typisch `a`, `b`, `c` of `i1`, `i2`).
- Geen kunstmatig "items/subvragen/sets"-onderscheid. Als binnen-vragen een andere context hebben → splits in twee aparte vraag-eenheden.

**Vraagtypes — gereduceerde enum** (vraag-mechaniek, niet antwoord-vorm):
- `open` — vrij tekst-antwoord (kan boeking, berekening, definitie, procedure, motivatie zijn — die vorm komt in het antwoord)
- `mc_keuze` — kies één uit `opties[]`
- `juist_fout` — beoordeel één stelling
- `onbekend` — guard-rail bij topic_only-deelvragen waar we het type niet weten

**Volledigheid is een per-deelvraag flag, geen vraagtype**:
- `volledig` — vraagstelling + alle elementen aanwezig
- `fragment` — vraagstelling aanwezig, één of meer elementen ontbreken
- `topic_only` — alleen onderwerp bekend, geen vraagstelling. Niet beantwoorden — later vraag-generatie

**`motivatie_verwacht`**: orthogonale bool. J/F-met-motivatie wordt `vraagtype: juist_fout` + `motivatie_verwacht: true`.

**`themas[]`** op vraag-niveau: keywords voor clustering, search en latere vraag-generatie.

**Schema**:

```json
{
  "schema_versie": "1.1",
  "examen_id": "2024-1",
  "vraag_id": "2024-1-vr10",
  "interpretatie_datum": "2026-05-21T...",
  "interpretatie_model": "claude-opus-4-7",
  "vraag_herkomst": "officieel | herinnering | hybride",
  "vraag_onderwerp": "Analyse en kritische beoordeling van de jaarrekening",
  "themas": ["financiële onafhankelijkheid", "balansrubrieken", "afschrijvingen"],
  "context_blokken": [
    {"type": "casus_context", "tekst": "..."},
    {"type": "balans", "actief": {"headers": ["Rubriek", "Jaar 2012", "Jaar 2011"], "rows": [["...", "...", "..."]]},
                       "passief": {"headers": ["Rubriek", "Jaar 2012", "Jaar 2011"], "rows": [["...", "...", "..."]]}},
    {"type": "gegevens_tabel", "titel": "Resultaatverwerking 2011", "rijen": [{"label": "Te bestemmen winst", "bedrag": 15000}]}
  ],
  "vragen": [
    {
      "id": "a",
      "label_in_pdf": "A",
      "vraagtype": "juist_fout",
      "vraagstelling": null,
      "motivatie_verwacht": true,
      "volledigheid": "topic_only",
      "topic_only_onderwerp": "Stellingen ivm financiële onafhankelijkheid"
    },
    {
      "id": "e",
      "label_in_pdf": "E",
      "vraagtype": "mc_keuze",
      "vraagstelling": "Alfa is verlieslatend. Verhoging van de afschrijving op gebouwen ... heeft welk effect op de bruto verkoopmarge?",
      "opties": [
        {"id": "a", "tekst": "Stijging"},
        {"id": "b", "tekst": "Daling"},
        {"id": "c", "tekst": "Geen"},
        {"id": "d", "tekst": "Stijging op voorwaarde dat ..."}
      ],
      "motivatie_verwacht": true,
      "volledigheid": "volledig"
    }
  ],
  "antwoord_hint_in_vraag": null,
  "herinterpretatie_motivering": "...",
  "kwaliteits_flags": []
}
```

**Toegestane `context_blokken[].type`-waardes**:
- Structuur: `casus_context`, `bijlage_verwijzing`
- Cijfermateriaal: `tabel`, `gegevens_tabel` *(titel + rijen[{label,bedrag}], vervangt platte `berekening_gegeven`)*, `balans` *(actief + passief als aparte sub-tabellen, vervangt het naast-elkaar-formaat)*, `resultatenrekening`, `proef_saldibalans`, `rekeningstaat`, `inventaris`, `marktwaarde`, `aanpassing`, `formule`
- Visueel: `figuur`
- Vrije tekst: `tekst` (fallback)

`vraag_instructie`, `vraag_prefix`, `punten` (als veld of blok), `topic_aanduiding`, `mc_optie` op context-niveau zijn **uit het schema verwijderd** (v1.0 → v1.1 cleanup). Vraagstelling staat per deelvraag in `vragen[].vraagstelling`. MC-opties staan in `vragen[].opties`. Topic-only is een per-deelvraag-flag.

Discipline-regels en werkwijze: zie `prompts/vraag-interpretatie-v1.md` §4.

### 4. Topic-only is een per-deelvraag-flag, geen vraagtype

Bij herinnering-fragmenten waar enkel het onderwerp van een deelvraag bekend is (bv. "Stellingen J/F over financiële onafhankelijkheid"), gebruikt de interpretatie:

- `vraagtype` = de beste gok over de mechaniek (`juist_fout`, `mc_keuze`, `open`, of `onbekend`)
- `volledigheid: "topic_only"`
- `topic_only_onderwerp`: de samenvatting van het topic

Modelantwoord-laag schrijft **geen** topic-syllabus meer (POC-feedback: pedagogische waarde te laag, verbergt vraag-generatie-gap). In plaats daarvan krijgt de deelvraag `antwoord_status: "wacht_op_vraag_generatie"` in het antwoord-artefact, met lege `blokken[]`. Een latere vraag-generatie-pipeline (buiten ADR-024-scope) kan deze items opvolgen.

### 5. Modelantwoord-schema v1.1 (LLM, lokaal subagent)

Permanent artefact: `prompts/modelantwoord-v1.md` (v1.1).

**Conceptueel model**: één antwoord per deelvraag, gekoppeld via `id`. Primair antwoord (gekozen_optie_id, oordeel, of vrije blokken) op deelvraag-niveau. `blokken[]` is optionele motivering bij mc_keuze/juist_fout én het hele antwoord bij open vragen.

**Schema**:

```json
{
  "schema_versie": "1.1",
  "examen_id": "...",
  "vraag_id": "...",
  "antwoord_datum": "...",
  "antwoord_model": "claude-opus-4-7",
  "vraag_antwoorden": [
    {
      "id": "a",
      "antwoord_status": "beantwoord",
      "gekozen_optie_id": "c",
      "blokken": [
        {"type": "motivatie", "tekst": "Afschrijving is een kost onder ...", "confidence": "inferred", "bron_refs": []}
      ]
    },
    {
      "id": "b",
      "antwoord_status": "beantwoord",
      "oordeel": true,
      "blokken": [
        {"type": "motivatie", "tekst": "...", "confidence": "...", "bron_refs": []}
      ]
    },
    {
      "id": "c",
      "antwoord_status": "beantwoord",
      "blokken": [
        {"type": "boeking", "regels": [{"zijde": "D", "rekening": "...", "naam": "...", "bedrag": 1200.0}], "confidence": "...", "bron_refs": []},
        {"type": "grondslag", "tekst": "...", "wetsref": "art. 3:90 WVV", "confidence": "grounded", "bron_refs": ["WVV-art-3-90"]}
      ]
    },
    {
      "id": "d",
      "antwoord_status": "wacht_op_vraag_generatie",
      "blokken": []
    },
    {
      "id": "e",
      "antwoord_status": "hard_blocked",
      "blokken": [],
      "record_gap_report": {"niveau": "c", "type": "concept_ontbreekt", "beschrijving": "...", "voorgesteld_record": "..."}
    }
  ]
}
```

**`antwoord_status`-enum**: `beantwoord | wacht_op_vraag_generatie | hard_blocked`.

**Validatie-regels** (afgedwongen door schema-tests):
- `vraagtype: mc_keuze` + `beantwoord` → `gekozen_optie_id` aanwezig en matcht een `opties[].id`
- `vraagtype: juist_fout` + `beantwoord` → `oordeel: bool` aanwezig
- `vraagtype: open` + `beantwoord` → `blokken[]` niet leeg, minstens één primair-content blok (boeking/berekening/definitie/procedure/motivatie/conclusie/tabel/opsomming)
- `motivatie_verwacht: true` + `beantwoord` → `blokken[]` bevat minstens één `motivatie`/`grondslag`/`conclusie`
- `wacht_op_vraag_generatie` → `blokken: []`, geen primair antwoord-veld
- `hard_blocked` → `blokken: []`, `record_gap_report` gevuld

**Blok-types** (allen met verplicht `type`, `confidence`, `bron_refs`):
- `motivatie` — `tekst`
- `boeking` — `regels: [{zijde, rekening, naam, bedrag}]`, optioneel `toelichting`
- `berekening` — `formule`, `stappen[]`
- `definitie` — `lemma`, `uitleg`
- `procedure` — `stappen[]`
- `tabel` — `headers`, `rows`
- `opsomming` — `items[]`
- `conclusie` — `tekst`
- `grondslag` — `tekst`, `wetsref`

`mc_keuze`/`juist_fout`/`topic_syllabus` zijn **geen** blok-types meer. mc_keuze en juist_fout zitten als primair antwoord op deelvraag-niveau; topic_syllabus is volledig vervallen.

Discipline-regels en werkwijze: zie `prompts/modelantwoord-v1.md` §4.

### 6. Merger (deterministisch, idempotent)

Nieuw tool: `tools/examen/merge_examen_artefacten.py`. Leest alle `_interpretaties/<examen>/*.json` + `_antwoorden/<examen>/*.json` voor één examen en produceert `<examen>.json` met `schema_versie: "4.0"`. Discipline:

- **Fail-loud** bij ontbrekende interpretatie voor een vraag-id die wel in `_segmenten/` zit. Geen stille fallback naar v3-regex-output.
- **Fail-loud** bij ontbrekend antwoord — gap-rapport in `_antwoorden/<vraag-id>.json` telt als geldige output, missende file niet.
- **Idempotent**: twee runs geven byte-identieke output.
- **Geen Claude API** in de merger. Pure file-IO + JSON-validatie.

### 7. CLAUDE.md regel 3 compliance

Twee LLM-stappen (vraag-interpretatie en modelantwoord) gebeuren via **lokale Claude Code subagent-runs**, niet via `anthropic.Anthropic()` in build-scripts. Prompt-artefacten (`prompts/vraag-interpretatie-v1.md`, `prompts/modelantwoord-v1.md`) zijn permanent en versioneerbaar. Output is gecommitteerd in git. Build/CI roept géén LLM aan — het runt alleen de merger op gecommitteerde input.

## Wat blijft bestaan uit ADR-021/022/023

- **ADR-021 v2-laag** (pdfplumber-segment-detector) blijft als baseline voor `_segmenten/<vraag-id>/tekst.txt`. De v3-regex-detectoren (`_v3_blok_detectoren.py`) zijn niet meer de waarheid en zijn kandidaat voor cleanup na uitrol.
- **ADR-022** schema-velden zijn opgegaan in v1.1: `vraag_herkomst` blijft, `vraag_volledigheid` is per-deelvraag (`volledigheid`), `vraag_herinterpreteerd` is vervallen (herinterpretatie is impliciet de agent-output).
- **ADR-023** `correct_antwoord_blokken[]` is vervangen door `vraag_antwoorden[].blokken[]` met expliciete `gekozen_optie_id`/`oordeel` op deelvraag-niveau. `mc_keuze`, `juist_fout` en `topic_syllabus` zijn vervallen als blok-types.

## POC-resultaat (2026-05-21, empirisch gevalideerd)

**Schaal**: 6 vragen uit 4 PDFs (2013-1, 2014-1, 2003-bibf, 2008-bibf, 2024-1). Representatief: officieel ITAA + officieel BIBF + herinnering. Test-set in `data/programma/examen_vragen/_poc_subset.json`.

**Bevestigd**:
1. Per-vraag artefact-architectuur werkt — één vraag = één bewerkbare eenheid, merger is idempotent en fail-loud.
2. Visuele PNG-input (200 dpi, volle pagina, gitignored, regenereerbaar) is voldoende voor de agent. Bbox-crop niet nodig.
3. CLAUDE.md regel 3-compliance via lokale Claude Code subagent zonder `anthropic.Anthropic()`-call werkt.
4. Schema 4.0 voor samengesteld `<examen>.json` is breaking — geen poging tot additieve migratie.
5. Modelkeuze: **Sonnet voor interpretatie** (uitrol-fase), Opus voor antwoorden waar records-laag aansluit (latere fase).
6. JSON-schema-tests + visuele Quartz-review zijn voldoende verificatie — geen tweede LLM-pass nodig.

**Geleerd uit POC (verwerkt in schema 1.1 + prompts v1.1)**:
- `items[]` → `vragen[]` (deelvragen zijn gewoon vragen binnen dezelfde context).
- `vraagtype` reduceert tot `open | mc_keuze | juist_fout | onbekend` — boeking/berekening/definitie/procedure zijn antwoord-vormen, geen vraagtypes.
- `motivatie_verwacht` is orthogonaal aan vraagtype. J/F + motiveer = één deelvraag met `juist_fout` + `motivatie_verwacht: true`.
- `topic_only` is een per-deelvraag-flag, geen vraagtype. Bij topic_only antwoord → `wacht_op_vraag_generatie`, geen syllabus.
- Pure motivatie-instructies ("Motiveer uw antwoord", "Verklaar") als aparte b)-letter in PDF → **niet** als aparte deelvraag opnemen; integreren als `motivatie_verwacht: true` op de voorganger.
- Balans als gesplitst `{actief, passief}` met aparte sub-tabellen, niet ACTIEF/PASSIEF in één tabel.
- Gegevens-blokken (resultaatverwerking, kostenstaten, ...) als `{type: "gegevens_tabel", titel, rijen: [{label, bedrag}]}` — niet platte tekst.
- `vraag_prefix`, `punten` (als blok), `topic_syllabus`, `mc_optie` (als context-blok) zijn allemaal vervallen.
- Antwoord-blokken: mc-keuze en oordeel zijn primair antwoord op deelvraag-niveau, niet als blok-type.
- Inferred antwoorden zonder RAG hebben beperkte pedagogische waarde — antwoord-pass uitstellen tot records-laag dekkend is.

## Uitrol-volgorde (na POC)

1. **Vraag-isolatie schalen**: `tools/examen/isoleer_vragen.py` voor alle 253 vragen. Pagina-range autodetectie uit bestaande `<examen>.json` (`pdf_pagina[N]` tot `pdf_pagina[N+1] − 1`, minimaal 1 pagina).
2. **Interpretatie alleen** (geen antwoorden): Sonnet-subagent per examen-batch (7 examens). Antwoorden in latere fase wanneer records-laag aansluit.
3. **Merger** opnieuw op alle examens → `_merged/<examen>.json` schema 4.0.
4. **Cleanup-evaluatie**: `tools/examen/structureer_antwoorden.py` en grote stukken van `_v3_blok_detectoren.py` zijn kandidaat voor verwijdering (CLAUDE.md regel 9). Pas weghalen wanneer alle examens succesvol door v1.1-pipeline zijn.
