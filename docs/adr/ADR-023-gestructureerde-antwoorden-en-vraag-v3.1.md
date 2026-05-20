# ADR-023: Gestructureerde antwoorden (`correct_antwoord_blokken[]`) + vraag-cleanup v3.1

**Status**: Draft
**Datum**: 2026-05-20
**Pilot-scope**: alle 7 voorbeeldexamen-bestanden — 253 vragen, 99 + 13 = 112 modelantwoorden, 49+ subvragen die nog op modelantwoord wachten.

## Context

Sinds ADR-021 v3.0 (2026-05-20) zijn vraagteksten **typed gestructureerd**: een vraag is een `vraagtekst_blokken[]`-lijst met `vraag_instructie`, `casus_context`, `boeking`-achtige typed blokken (`proef_saldibalans`, `inventaris`, ...), `mc_optie` etc. De render-laag toont een vraag als een rijk gerenderde mini-pagina met markdown-tabellen, callouts en quote-blocks.

De modelantwoorden uit ADR-020 + `prompts/modelantwoord-checklists.md` v1.0 zijn **platte tekst** in `correct_antwoord` (string) en `antwoord_motivering` (string met markdown — codeblocks, tabellen, bold, ⚖️/🤖). Visuele inspectie 2026-05-20 (user-observatie 2003-bibf-vrA1):

> User: "geef de boekingen" wordt nu beantwoord als platte tekst, terwijl de vraag al typed is. Asymmetrie + waarde-verlies — een boekings-blok in het antwoord zou als typed `boeking` met `regels[]` veel rijker rendebaar zijn (gekleurde D/C-kolom, totaal-controle, render-laag-uniformiteit met de `proef_saldibalans` in de vraag).

Pattern-scan 2026-05-20 over de 112 bestaande modelantwoorden (zie `data/extractie/v4-antwoord-pattern-scan-2026-05-20.md`) bevestigt dat er **9 structurele element-categorieën** in de motiveringen voorkomen die als typed blokken te lichten zijn, zonder nieuwe inhoud te verzinnen:

- 76/112 hebben een grondslag-alinea (`_Grondslag: KB WVV art. X._`)
- 30/112 hebben een genummerde lijst met bold lemma's (typisch `opsomming`-vorm)
- 18/112 hebben Debet/Credit-boekingen (in codeblock of inline)
- 13/112 hebben een definitie-zin
- 12/112 hebben een formule + cijfer-toepassing
- 9/112 hebben een markdown-tabel
- 6/112 hebben procedure-stappen
- 5/112 hebben een conclusie/antwoord-slot
- Plus: `motivatie`-paragrafen als fallback

Tegelijk merkte de user op dat v3-extract drie semantische lagen in vraagteksten nog deels samenpakt (steekproef 2003-bibf-vrA1):

1. **Vraag-onderwerp** — "Kapitaalsubsidies" als één-woord-titel boven de casus. Niet apart gevangen; verdwijnt in eerste `tekst`-blok.
2. **Casus-context** — verhalende setup ("Gedurende 2002 werd een machine aangekocht voor 100.000 EUR..."). v3 vangt dit deels via `casus_context`-detector, maar afbakening is niet scherp — vaak komt casus-tekst in een `tekst`-blok ipv `casus_context`-blok.
3. **Vraag-instructie** — imperatief ("geef de afsluitingsboekingen"). Wordt wel als typed blok gevangen, maar met "Vraag :"-residue erin (11 records).

Dit ADR adresseert beide gebrekken in één samenhangend pakket:

- **v3.1 vraag-cleanup**: nieuw top-level veld `vraag_onderwerp`, scherpere `casus_context`-afbakening, residue-strippen ("Vraag :", "Antwoord", "N PUNTEN") uit `vraag_instructie`-/`tekst`-blokken
- **ADR-023 antwoord-restructurering**: nieuwe veld `correct_antwoord_blokken[]` parallel aan `correct_antwoord` (string) — additieve typed structuur op de 112 bestaande modelantwoorden, **zonder nieuwe inhoud**

## Beslissing — v3.1 (vraag-cleanup, additief)

### v3.1.1 Nieuw top-level vraag-veld `vraag_onderwerp`

| Veld | Type | Verplicht | Doel |
|---|---|---|---|
| `vraag_onderwerp` | `string` of `null` | nee | Korte boekhoud-thematitel boven de casus, bv. `"Kapitaalsubsidies"`, `"Voorraden"`, `"Afschrijvingen"`. **Niet** de vraag-prefix (`"Vraag 4"`, `"A.2"`) — die zit in `vraag_prefix`. |

**Detector**: heuristiek (conservatief — pattern-scan toont dat slechts ~1 % van de 253 vragen een echte titel heeft):

- Eerste niet-lege regel van het eerste `tekst`-blok
- Gevolgd door `.` of `\n` + casus-tekst
- ≤ 4 woorden
- Begint met hoofdletter
- Niet gevolgd door `?` (anders is het al een vraag-zin)
- Niet `"Vraag"`, niet `"Antwoord"`, niet een vraag-prefix-fragment

Bij geen match → `vraag_onderwerp = null`. Default.

### v3.1.2 Scherpere `casus_context`-afbakening

Bestaande v3-detector vangt `casus_context` op "De BVBA X", "NV Y", "De heer Z" + verhalende paragraaf. v3.1 voegt **opzuig-logica** toe: na `vraag_onderwerp`-detectie wordt alle tekst tussen `vraag_onderwerp` en eerste `vraag_instructie` opgezogen als `casus_context`-blok, **mits**:

- ≥ 50 tokens verhalende tekst
- Geen imperatief-zin (start niet met "Geef", "Bereken", "Bepaal", ...)
- Geen typed cijfer-blok (`proef_saldibalans`, `inventaris`, ...) — die blijven los

Bij minder dan 50 tokens of detectie van een imperatief blijft het als `tekst`-blok.

### v3.1.3 Residue-strippen uit `vraag_instructie`

`_INSTRUCTIE_RE` in `_v3_blok_detectoren.py` accepteert al `Vraag\s*:\s*` als prefix vóór de imperatief-werkwoorden. v3.1 verbreedt:

- `"Vraag :"`, `"Vraag:"`, `"Vraag."`, `"Vraag?"` — verwijderd uit `inhoud`
- `"Antwoord"` als residue aan begin/einde van `tekst`-blok — verwijderd (komt 110× voor in de v3-extract, want elke PDF heeft "Antwoord" als rubriek-kop bij elk modelantwoord)
- `"N PUNTEN"`/`"/ N punten"` residue dat niet door `lift_top_level_velden` is gevangen — verwijderd

Restant-fragmenten zoals `"o. Er werd ..."` (geobserveerd 1×) worden opgezogen door het nieuwe `casus_context`-opzuig-mechanisme.

### v3.1.4 Migratie

v3.1 is een **additief minor-revisie** van schema 3.0 — geen schema-bump naar 3.1, geen breaking change. Alle bestaande velden blijven. Re-extract via `migrate_to_v3.py` (geen nieuw migratie-script):

- Bestaande modelantwoorden + classificatie + ADR-022-velden + gap-reports worden onveranderd doorgegeven (zie `migrate_to_v3.py` `ALLE_BEHOUDEN`-lijst)
- `vraag_onderwerp` toegevoegd waar detector hem vindt; elders `null`
- `casus_context`-blokken geherstructureerd waar de nieuwe opzuig-logica triggert
- `vraag_instructie`-`inhoud` gestript van residues

## Beslissing — ADR-023 (antwoord-blokken)

### 1. Nieuw veld `correct_antwoord_blokken[]`

Per vraag (en per subvraag, indien `correct_antwoord` daar gepopulariseerd is) een nieuw veld:

```json
"correct_antwoord_blokken": [
  {"type": "definitie", "lemma": "...", "definitie_zin": "...", "confidence": "grounded"},
  {"type": "motivatie", "inhoud": "...", "confidence": "inferred"},
  {"type": "grondslag", "bronnen": ["KB WVV art. 3:50", "CBN-advies 2018/02"]}
]
```

`correct_antwoord` (string) en `antwoord_motivering` (string) **blijven** als-is — backward-compat fallback voor consumenten die de typed structuur niet lezen, en als bewijs van de bron-tekst die de blokken parafraseren. Geen verlies.

### 2. Blok-types — 9 types, gebaseerd op pattern-scan

Verplichte velden zijn met `*` gemarkeerd. `confidence` is overal optioneel (default `"inferred"` of weglaten).

#### `motivatie` (fallback — alle 112 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `inhoud`* | string (markdown) | ja | `"Voorraad eindigt op de balans aan de **lagere** van aanschaffingswaarde en marktwaarde."` |
| `kop` | string | nee | `"Vergelijk met andere oordeel-types"`, `"Scenario A — Meerwaarde gespreid gerealiseerd"` |
| `confidence` | `"grounded"` / `"inferred"` | nee | — |

Wanneer toepassen: paragraaf-redenering die niet onder een specifieker blok past. Vergelijking-alinea (`**Vergelijk met X**`), voorbeeld-alinea (`**Voorbeelden**`), scenario-header (`**Scenario A**`) — alle drie krijgen `motivatie` + `kop`.

#### `boeking` (18 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `regels`* | `list[{zijde, rekening, naam, bedrag}]` | ja | `[{"zijde": "D", "rekening": "416", "naam": "Diverse vorderingen", "bedrag": 10000.0}, ...]` |
| `context` | string | nee | `"Stap 1: Bij toezegging"`, `"Bij aanschaffing van de machine"` |
| `eenheid` | string | nee, default `"EUR"` | — |
| `confidence` | string | nee | — |

Per `regels[i]`:
- `zijde`*: `"D"` of `"C"` (in display: "Debet"/"Credit")
- `rekening`*: string (MAR-code, bv. `"15"`, `"416"`, `"7530"`)
- `naam`*: string (rekening-naam, bv. `"Kapitaalsubsidies"`)
- `bedrag`*: float (in `eenheid`)

Wanneer toepassen: bestaande Debet/Credit-codeblock óf inline boekings-tekst. Eén `boeking`-blok per logisch boekings-moment (per `context`). Bij user-voorbeeld 2003-vrA1: 4 `boeking`-blokken (toezegging, aanschaffing, afschrijving, subsidie-opname).

#### `berekening` (12+ records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `formule`* | string | ja | `"Operationele cashflow = Resultaat + Afschrijvingen + Voorzieningen"` |
| `componenten` | `list[{naam, bedrag, eenheid?}]` | nee | `[{"naam": "Resultaat", "bedrag": 100000}, ...]` |
| `tussenstappen` | `list[string]` | nee | `["100.000 + 25.000 = 125.000"]` |
| `resultaat` | float of string | nee | `54.46` |
| `eenheid` | string | nee | `"%"`, `"EUR"` |
| `interpretatie` | string | nee | `"Goed boven sectorgemiddelde van 35%."` |
| `confidence` | string | nee | — |

Wanneer toepassen: vraagtype `berekening` of `kwalificatie` met cijfer-uitwerking. Eén blok per onafhankelijke formule-toepassing.

#### `opsomming` (30 records — alle 7 `opsomming`-types + binnen `casus` en `definitie`)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `items`* | `list[{lemma, toelichting?, confidence?}]` | ja | `[{"lemma": "Onder-gewaardeerde activa", "toelichting": "werkelijke waarde > boekwaarde", "confidence": "grounded"}, ...]` |
| `kop` | string | nee | `"De vier voornaamste oorzaken van een positief consolidatieverschil"` |
| `volgorde_vast` | bool | nee (default `false`) | — bij wettelijk vastgelegde volgorde |

Per item:
- `lemma`*: string (de fettte beschrijving — wat is gebold in `**...**`)
- `toelichting`: optioneel — wat na het em-dash of de dubbele punt staat
- `confidence`: `"grounded"` / `"inferred"`

#### `procedure` (6 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `stappen`* | `list[{nummer, beschrijving, confidence?}]` | ja | `[{"nummer": 1, "beschrijving": "Brief-opmaak: auditor stelt de inhoud op met saldo uit boekhouding.", "confidence": "grounded"}, ...]` |
| `kop` | string | nee | — |
| `valkuilen` | `list[string]` | nee | — |

#### `definitie` (13 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `lemma`* | string | ja | `"Onthouding van oordeel"` |
| `definitie_zin`* | string | ja | `"De accountant ... wanneer hij onmogelijk voldoende assurance kan verkrijgen ..."` |
| `kerneigenschappen` | `list[{eigenschap, confidence?}]` | nee | `[{"eigenschap": "Cumulatief: scope-beperking + diepgaande gevolgen", "confidence": "grounded"}]` |
| `confidence` | string | nee | — |

#### `tabel` (9 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `rows`* | `list[list[str]]` | ja | `[["100.000", "10%", "10.000"], ...]` |
| `headers` | `list[str]` | nee | `["Component", "Bedrag (€)"]` |
| `kop` | string | nee | — |
| `confidence` | string | nee | — |

#### `conclusie` (5+6 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `inhoud`* | string | ja | `"Optie 3 is juist: bij vervreemding moet de meerwaarde via reserves of kapitaal."` |
| `gekozen_mc_label` | string | nee | `"3"`, `"c"`, `"juist"` |
| `confidence` | string | nee | — |

#### `grondslag` (76 records)

| Veld | Type | Verplicht | Voorbeeld |
|---|---|---|---|
| `bronnen`* | `list[string]` | ja | `["KB WVV art. 3:50", "CBN-advies 2018/02 'Kapitaalsubsidies'"]` |
| `confidence` | string | nee | — |

Wanneer toepassen: aparte afsluit-alinea `_Grondslag: ..._`. **Niet** dubbel met `antwoord_bron`-veld (object-list per claim) — die structuur is granulair per ⚖️-claim; `grondslag`-blok is de aggregerende afsluit-alinea zoals de stagiair hem visueel ziet.

### 3. Nieuwe `antwoord_type`-enum-waardes — 3 additief

Bestaande set blijft (`definitie`, `drempel_cijfer`, `opsomming`, `presentatie`, `kwalificatie`, `berekening`, `procedure`, `casus`).

Toegevoegd:

| Nieuw type | Wanneer | Frequentie verwacht | Motivatie |
|---|---|---:|---|
| `boeking` | "Geef de afsluitingsboekingen", "Boek de subsidie" — hoofdleverbare is een typed boekings-set | ~12 (uit huidige 27 `kwalificatie`-records) | `kwalificatie` is classificatie-vraag (welke methode?). Een vraag waar het hoofd-output een boekings-set is, hoort niet onder classificatie. Past niet onder `berekening` want het is geen formule-toepassing. |
| `waardering` | "Waardeer de voorraad", "bepaal de aanschaffingswaarde" — klemtoon op waarderingsregel + voorzichtigheidsbeginsel | ~5 | Overlapt met `berekening` maar de leerstof is de waarderingsregel zelf (lagere van AW en MW), niet de formule. Past niet onder `kwalificatie` want geen methodekeuze tussen meerdere opties. |
| `advies` | "Geef advies aan de cliënt", "Wat raadt u aan?" — aanbeveling + motivatie + waarschuwing | ~3 (2008-bibf-vrK2/K3, ...) | Past niet onder `kwalificatie` (geen classificatie), niet onder `procedure` (geen vaste stappen-set), niet onder `casus` (heeft geen subvragen). Heeft eigen output-vorm: `motivatie` + `conclusie` (aanbeveling) + optioneel `procedure` voor de actie-stappen. |

Verworpen:
- `analyse` — te dichtbij `kwalificatie`. Een analyse-vraag is een kwalificatie-vraag met meer redenering.
- `juist_fout` — bestaande `kwalificatie` + `conclusie`-blok met `gekozen_mc_label` volstaat.

**Geen herclassificatie in scope**: de 27 huidige `kwalificatie`-records houden hun veld; een opvolg-classificatie-pass kan ze herklassiferen na ADR-acceptatie.

### 4. Behoud-discipline

Velden die **niet verloren mogen gaan** in de Fase 4-pass:

- `correct_antwoord` (string) — blijft als-is, dient als bron-tekst + backward-compat
- `antwoord_motivering` (string, markdown) — blijft als-is, dient als bron-tekst voor de typed blokken
- `antwoord_bron` (list[object]) — blijft als-is (granulaire claim-bron-mapping uit ADR-020 §7)
- `antwoord_provenance` (object) — blijft als-is + krijgt nieuw veld `correct_antwoord_blokken_geextracteerd_op: ISO-datum` wanneer de Fase 4-pass over hem heen ging
- `antwoord_confidence` (`"grounded"` / `"inferred"`) — blijft als-is
- `antwoord_type` (enum) — blijft als-is voor de 112 bestaande records; nieuwe enum-waardes vanaf §3 zijn voor toekomstige records
- `record_gap_report` — blijft als-is

Plus: ADR-022-velden (`vraag_herkomst`, `vraag_volledigheid`, ...), classificatie-velden (`vak_code_in_pdf`, `themas`, ...), v3-velden (`vraagtekst_blokken`, `punten`, `vraag_prefix`, ...).

### 5. Confidence per blok

Elk blok-type heeft een optioneel `confidence`-veld met enum-waardes `"grounded"` / `"inferred"`. Mapping uit bron-tekst:

- ⚖️ in de gerelateerde markdown-paragraaf → `confidence: "grounded"`
- 🤖 in de gerelateerde markdown-paragraaf → `confidence: "inferred"`
- Geen marker → veld weglaten (geen impliciete default)

Aggregaat `antwoord_confidence` op vraag-niveau blijft onveranderd uit ADR-020 §7.

### 6. STRICT geen nieuwe inhoud

De Fase 4-tool (`tools/examen/structureer_antwoorden.py`) is een **deterministische parser** — geen Claude API, geen LLM-call. Hij **leest** `correct_antwoord` + `antwoord_motivering`, **splitst** in blokken, **classificeert** elk blok als een van de 9 types, en **kopieert** de tekst over naar typed velden.

Wat hij **niet** doet:
- Geen nieuwe motivering verzinnen
- Geen wetsartikelen toevoegen die niet in de bron-tekst staan
- Geen confidence-label invullen waar geen ⚖️/🤖 marker staat
- Geen blok structureren waarvan de classificatie onzeker is — bij twijfel valt het hele antwoord terug op één `motivatie`-blok met de volledige `antwoord_motivering` als `inhoud`

Een antwoord dat "onstructureerbaar" is, krijgt:

```json
"correct_antwoord_blokken": [
  {"type": "motivatie", "inhoud": "<volledige antwoord_motivering>"}
]
```

Dat is een veilige fallback — de inhoud is nooit weg.

### 7. Schema-versie

Geen bump naar `schema_versie: "4.0"`. v3.1 + ADR-023-velden zijn **additief**. Bestaande consumenten die alleen `correct_antwoord` (string) lezen blijven werken. Nieuwe consumenten die de typed structuur willen, checken `correct_antwoord_blokken != null`.

### 8. Validator

`tools/examen/validate_antwoord_blokken_v1.py` (analoog aan `validate_examen_v3.py`):

- Blok-type ∈ {`motivatie`, `boeking`, `berekening`, `opsomming`, `procedure`, `definitie`, `tabel`, `conclusie`, `grondslag`}
- Per type: verplichte velden aanwezig
- Per `boeking`-blok: `regels[].zijde` ∈ {`"D"`, `"C"`}; `bedrag` is float
- Per `opsomming`-blok: `items[].lemma` is string
- Per `confidence`-veld: ∈ {`"grounded"`, `"inferred"`}

Fail-loud bij schema-overtreding. Geen automatische repair.

### 9. Render-impact

`tools/examen/render_alle_vragen.py` wordt uitgebreid om `correct_antwoord_blokken[]` te renderen:

- `boeking` → markdown-tabel met `Debet/Credit | Rekening | Naam | Bedrag`-kolommen
- `procedure` → genummerde lijst
- `motivatie` → paragraaf (met optionele bold `kop`)
- `definitie` → bold lemma + definitie-zin + bulleted kerneigenschappen
- `opsomming` → genummerde lijst met bold lemma's
- `berekening` → formule (code-block) + componenten-lijst + resultaat-regel
- `tabel` → markdown-tabel
- `conclusie` → bold "Conclusie:" prefix + inhoud (+ optioneel `> [!check] Gekozen: <label>`)
- `grondslag` → italic afsluit-alinea met komma-gescheiden bronnen
- `confidence`-markers (⚖️/🤖) zichtbaar per blok

Fallback bij ontbrekend `correct_antwoord_blokken[]`: render de bestaande `antwoord_motivering` als markdown (huidige gedrag).

### 10. Werkverdeling Opus ↔ Sonnet

| Stap | Wie |
|---|---|
| Pattern-scan + ADR-draft (deze) | Sonnet |
| v3.1-detector-implementatie + tests | Sonnet |
| `structureer_antwoorden.py` parser + classifier | Sonnet |
| Validator + tests | Sonnet |
| Render-uitbreiding + re-render | Sonnet |
| **Review van de gestructureerde output** | **Opus** (eindreview op willekeurige steekproef) |

## Werkwijze (per modelantwoord van platte tekst → typed blokken)

```
[1] Lees correct_antwoord + antwoord_motivering uit JSON
[2] Backup: deze velden raken niet aangepast
[3] Parse antwoord_motivering:
    [3a] Detecteer codeblocks → boekings-blokken (Debet/Credit)
    [3b] Detecteer markdown-tabellen → tabel-blokken
    [3c] Detecteer genummerde bold-lijsten → opsomming/procedure (afhankelijk van antwoord_type)
    [3d] Detecteer grondslag-alinea (_Grondslag:_) → grondslag-blok
    [3e] Detecteer conclusie-/antwoord-paragrafen
    [3f] Restant-paragrafen → motivatie-blokken (met optionele kop)
[4] Per blok: detecteer confidence-marker (⚖️/🤖) → confidence-veld
[5] Specifieke transformaties per antwoord_type:
    - antwoord_type='definitie': eerste paragraaf → definitie-blok (lemma + zin)
    - antwoord_type='procedure': genummerde lijst → procedure-blok
[6] Bij parse-fail: één motivatie-blok met volledige antwoord_motivering als inhoud
[7] Schrijf correct_antwoord_blokken[] terug in JSON
[8] Validator runnen
```

## Pilot

**Alle 7 examen-bestanden** in één pass. Doel:
- 112 antwoorden gestructureerd, 0 nieuwe inhoud
- Validator passeert
- Render-pagina toont herkenbare typed blokken voor minstens 50 % van de antwoorden (rest fallback `motivatie`)

Bij twijfel of falen op een specifiek record: blijft als single-`motivatie`-blok. Geen forcering.

## Wat NIET in dit ADR

- **Nieuwe modelantwoorden schrijven**: blijft onder `prompts/modelantwoord-checklists.md` v1.0 + ADR-020. Dit ADR gaat alleen over de 112 bestaande antwoorden.
- **Herclassificatie van bestaande `antwoord_type`-waardes**: out-of-scope. Nieuwe enum-waardes (`boeking`, `waardering`, `advies`) zijn beschikbaar voor toekomstige records; bestaande blijven onveranderd.
- **Render in minicursussen**: `render_alle_vragen.py` (de "alle vragen"-pagina) wordt aangepast. De minicursus-render (ADR-009 §6 + ADR-010) is opvolgwerk.
- **Update van `prompts/modelantwoord-checklists.md`**: in een opvolg-pass krijgt de prompt instructies om direct in typed blokken te schrijven. Nu is alleen de parse-laag aan zet.
- **Wijziging van `antwoord_bron`-structuur**: blijft granular per claim (ADR-020 §7). `grondslag`-blok is aggregaat — beide bestaan parallel.
- **Anthropic API in build-pipeline**: niet — Fase 4-tool is een deterministische Python-parser.

## Gevolgen

**Nieuwe artefacten**:
- `docs/adr/ADR-023-gestructureerde-antwoorden-en-vraag-v3.1.md` — dit document
- `tools/examen/structureer_antwoorden.py` — parser/classifier
- `tools/examen/validate_antwoord_blokken_v1.py` — schema-validator
- `tests/test_structureer_antwoorden.py`
- `tests/test_validate_antwoord_blokken.py`
- `data/extractie/v4-antwoord-pattern-scan-2026-05-20.md` — pattern-scan rapport (al aanwezig)

**Bestaande artefacten gewijzigd**:
- `tools/examen/_v3_blok_detectoren.py` — v3.1 cleanup-detectoren (vraag_onderwerp, casus_context-opzuig, residue-strip)
- `tools/examen/extract_vragen_v3.py` — gebruikt de uitgebreide detectoren
- `tools/examen/render_alle_vragen.py` — rendert typed antwoord-blokken
- `data/programma/examen_vragen/*.json` — 7 bestanden krijgen `vraag_onderwerp`-velden waar detector triggert + scherpere `casus_context`-blokken + 112 antwoord-records krijgen `correct_antwoord_blokken[]`
- `tests/test_extract_vragen_v3.py` — nieuwe tests voor v3.1 cleanup
- `content/voorbeeldexamens/alle-vragen.md` — re-render

**Niet-gewijzigd**:
- ADR-020 modelantwoord-pipeline (checklists v1.0, gap-flow)
- ADR-021 v3.0 vraagtekst-schema (additieve velden)
- ADR-022 ADR-022-velden (vraag_herkomst, vraag_herinterpreteerd, ...)
- Concept-/competentie-records (schema 1.6)
- Records-API
- 802+ bestaande tests (alleen nieuwe tests toegevoegd)

**Risico's**:
- *Parser classificeert blok verkeerd*: mitigatie — bij twijfel valt het terug op `motivatie`-blok met volledige `antwoord_motivering` als `inhoud`. Geen verlies, alleen mindere typing.
- *v3.1 cleanup-detector strip te aggressief*: mitigatie — conservatieve heuristieken (4-woord-limiet voor `vraag_onderwerp`, ≥ 50 tokens voor opzuig naar `casus_context`).
- *Render-uitbreiding breekt bestaande "alle vragen"-pagina*: mitigatie — fallback-pad voor antwoorden zonder `correct_antwoord_blokken[]` blijft bestaand gedrag.
- *Toekomstige modelantwoord-passes vergeten typed structuur*: mitigatie — opvolg-update van `modelantwoord-checklists.md` brengt de typed structuur in de generator-prompt zelf (out-of-scope dit ADR, maar geflagd).

## Changelog

- **v0.1 (2026-05-20, DRAFT)** — Eerste vastlegging op basis van user-observatie 2026-05-20 (asymmetrie typed vragen vs platte antwoorden) + pattern-scan over 112 modelantwoorden. v3.1 vraag-cleanup en antwoord-blokken in één ADR omdat ze dezelfde rendering-pipeline raken. Status DRAFT — Accepted na review op gegenereerde output.
