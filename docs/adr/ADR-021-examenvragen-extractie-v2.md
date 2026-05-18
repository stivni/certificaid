# ADR-021: Examenvragen-extractie v2 + gestructureerde vraagtekst-blokken

**Status**: Accepted
**Datum**: 2026-05-19

## Context

`tools/examen/extract_vragen.py` (v1) gebruikt enkel `pdfplumber.Page.extract_text()` — één platte 1D-string per page. Gevolg: tabellen, formules en cijfer-blokken verliezen hun structuur. Cellen worden naast elkaar gelust ("M 70 % 30 % 60 % 20 % A B C"), kolommen-headers raken zoek, balansen worden lineaire reeksen.

**Inventaris 253 voorbeeldexamen-vragen** (2026-05-19 scan):
- **~21 vragen (8 %)** zwaar geïmpacteerd — combinaties tabel + cijfers + percentages (consolidatie, balansen, ratio's)
- **~47 vragen (19 %)** mild geïmpacteerd — jaarrekening-content met balans-termen
- **~75 % vragen** zuiver tekstueel (geen structuur-verlies)

Net die 21+47 vragen zijn de **toepassings- en redeneer-vragen** waarvoor modelantwoorden (ADR-020) het meest waarde opleveren. Een platte `vraagtekst` waarin de tabel verminkt is, blokkeert betrouwbare modelantwoord-generatie: óf de pipeline weigert (`record_gap_report.type = "vraagtekst_onduidelijk"`), óf het modelantwoord rust op gokken over de tabel-structuur.

`tools/examen/normalize_vraagteksten.py` (2026-05-19) flagt deze problemen wel, maar lost ze niet op — het is een detector, geen reconstructor. De architecturale fix is de extractie zelf herwerken zodat structuur behouden blijft.

## Beslissing

### 1. Schema-bump examen_vragen v2

Top-level veld `schema_versie` op het examen-bestand. Per vraag en per subvraag: nieuw veld `vraagtekst_blokken[]` met typed elementen. Bestaand `vraagtekst`-veld blijft als concatenated platte fallback (backward-compat, geen breaking change voor consumenten die niet upgraden).

```json
{
  "examen_id": "2014-1",
  "schema_versie": "2.0",
  "vragen": [
    {
      "id": "2014-1-vr8",
      "vraagtekst": "Vraag 4 … / 9 punten Vul onderstaande tabel aan ...",
      "vraagtekst_blokken": [
        {"type": "tekst", "inhoud": "Vraag 4 … / 9 punten"},
        {"type": "tekst", "inhoud": "Vul onderstaande tabel aan op basis van volgende gegevens."},
        {"type": "tabel", "headers": ["Moeder", "Dochter", "Percentage"],
                         "rows": [["M", "A", "70 %"], ["M", "B", "30 %"], ["M", "C", "60 %"], ["M", "D", "20 %"]]},
        {"type": "tekst", "inhoud": "Antwoord"},
        {"type": "tabel", "headers": ["", "Controlepercentage", "Belangenpercentage", "Consolidatiemethode"],
                         "rows": [["M in A", "", "", ""], ["M in B", "", "", ""], ["M in C", "", "", ""], ["M in D", "", "", ""]]}
      ]
    }
  ]
}
```

### 2. Blok-types

| Type | Verplichte velden | Optionele velden | Wanneer |
|---|---|---|---|
| `tekst` | `inhoud` (string) | — | Reguliere vraagtekst-paragraaf |
| `tabel` | `rows` (list[list[str]]) | `headers` (list[str]), `bron_bbox` (page+bbox-coords) | Detecteerbare 2D-tabel met ≥ 2 kolommen en ≥ 2 rijen |
| `formule` | `inhoud` (string, plain of LaTeX) | `notatie` (`"plain"` of `"latex"`) | Niet automatisch gedetecteerd in v2.0 — opt-in via handmatige post-extract markup; uitgebreid in v2.1 |
| `figuur` | `bron_pdf`, `page`, `bbox` | `caption` | Niet automatisch in v2.0 — gepland voor v2.1 |

**v2.0-scope**: `tekst` + `tabel` zijn automatisch via pdfplumber. `formule` en `figuur` blijven handmatig of toekomstig werk — geen blokkers voor modelantwoord-pipeline (formules zitten meestal in tekst-vorm, figuren zijn zeldzaam).

### 3. Extractie-aanpak (extract_vragen v2)

Per page:
1. **Detect tabellen**: `page.extract_tables(table_settings)` met conservatieve settings (kolom-lijnen of consistente witruimte). Per tabel: `bbox` (top, bottom).
2. **Detect text-blokken tussen tabellen**: gebruik `page.extract_text()` als baseline, maar filter regels die binnen een tabel-bbox vallen. Splits resterende text rond de Y-coördinaten van tabellen.
3. **Reorder**: blokken op top-Y-coördinaat sorteren, zodat tekstvolgorde op page bewaard blijft.
4. **Compose**: typed `vraagtekst_blokken[]` per vraag, na vraag-splitsing op vraag-headers (Vraag N, A.N, vrA1, ...).
5. **Concat fallback**: bouw `vraagtekst` op uit blokken (tekst direct, tabel als markdown-tabel — voor backward-compat met flat consumers en voor zoek-/grep-doeleinden).

**Tabel-detection-tuning**: pdfplumber-defaults zijn agressief en hallucineren tabellen uit kolom-uitlijning (bv. tweekoloms-MC-opties). Conservatief overriden:
- `vertical_strategy="lines"` (alleen detecteren als er expliciete kolom-lijnen zijn) **of** `vertical_strategy="text"` met `min_words_horizontal=3`
- `horizontal_strategy="lines"` als de PDF gridlines heeft, anders `"text"` met validatie
- Per PDF tune (verschillende ITAA-pdfsoorten hebben verschillende lay-outs). Hyper-parameter in `EXAMEN_CONFIGS`.

**Validatie post-extract**:
- Elke gedetecteerde tabel moet ≥ 2 rijen en ≥ 2 kolommen hebben
- Cell-content niet leeg in > 70 % cellen
- Anders: tabel-detectie wordt verworpen, blok valt terug naar `tekst`

### 4. Migratie van bestaande examen-files

Re-extract gebeurt **destructief** — bestaande `vraagtekst`-content wordt vervangen door de v2-extract. Wat WEL bewaard blijft:
- Bestaande modelantwoorden (`correct_antwoord`, `antwoord_motivering`, `antwoord_bron`, `antwoord_provenance`, `record_gap_report`, `antwoord_type`)
- Bestaande classificatie (`vak_code_in_pdf`, `vak_naam_in_pdf`, `themas`, `wets_verwijzingen`)
- Bestaande subvragen-splitsing (`subvragen[]` structuur, indien al gepopulariseerd via `_sub_vragen_splitter.py`)
- Vraag-IDs (deterministisch — moeten stabiel blijven over re-extracts)

**Migratie-script** (`tools/examen/migrate_to_v2.py`):
1. Backup huidige `data/programma/examen_vragen/*.json` naar `_archive/v1/`
2. Re-extract elke PDF naar nieuwe v2-structuur
3. Per vraag in v2-output: zoek vraag met zelfde ID in v1-backup, kopieer antwoord-velden + classificatie-velden over
4. Schrijf v2-output, log diff (welke IDs verschoven, welke nieuw, welke verloren)
5. ID-stabiliteit fail-loud: als een vraag-ID uit v1 niet meer in v2 voorkomt → STOP, hand-review

### 5. Subvragen-impact

`_sub_vragen_splitter.py` splits vraagblok in `subvragen[]` op basis van platte tekst. Met blokken-structuur kunnen subvragen ook eigen `vraagtekst_blokken[]` krijgen (een subvraag die naar een tabel verwijst neemt die tabel-blok mee).

**v2.0-aanpak**: behoud bestaande splitter, voer eerst draaien op concat-`vraagtekst`. Indien een subvraag binnen een tabel-blok valt → tabel-blok hoort bij de subvraag waar de top-Y in valt. Latere v2.1: aparte sub-vragen-splitter die direct op blokken werkt.

### 6. Backward-compat + validatie

- `vraagtekst` blijft populated (concat van blokken — tabellen als markdown). Bestaande consumers (RAG, classify_vragen, modelantwoord-pipeline op flat-text vragen) blijven werken.
- Nieuw `schema_versie: "2.0"` veld op examen-bestand. Consumers die op v2 willen werken kunnen ernaar checken.
- Modelantwoord-pipeline (ADR-020) gebruikt **bij voorkeur** `vraagtekst_blokken[]` als beschikbaar; fallback naar `vraagtekst`. Wijziging in `prompts/modelantwoord-checklists.md` §2 "Vraagtekst-discipline".

### 7. Validator-tooling

Nieuwe `tools/examen/validate_examen_v2.py`:
- Schema-versie check
- Blok-types geldig
- Tabellen hebben coherente rij-lengtes
- Concat-`vraagtekst` matcht (binnen tolerantie) reconstructie uit blokken
- Tests in `tests/test_extract_vragen_v2.py` + `tests/test_examen_v2_schema.py`

## Werkwijze (per PDF van inkomend → v2-JSON)

```
[1] Backup huidige JSON       → data/programma/examen_vragen/_archive/v1/<examen>.json
[2] Open PDF                  → resources/raw/voorbeeldexamens/<bestand>.pdf
[3] Per page:
    [3a] extract_tables()     → list[Table met bbox]
    [3b] extract_text()       → string
    [3c] split text rond
         tabel-Y-ranges       → list[text_block met top_y]
    [3d] merge + sorteer      → list[Block]
    [3e] valideer tabellen    → reject < 2x2 of > 30% lege cellen
[4] Splits in vragen          → op vraag-headers (Vraag N, A.N, etc.)
[5] Per vraag:
    [5a] blokken samenstellen → vraagtekst_blokken[]
    [5b] concat fallback      → vraagtekst (markdown-tabellen)
    [5c] sub-vragen-splitter  → subvragen[] op concat-vraagtekst
[6] Merge antwoorden v1       → kopieer antwoord_*-velden, vraagtype, themas, etc.
                                bij overeenkomende vraag-ID
[7] Schrijf v2-JSON           → schema_versie: "2.0"
[8] Validator                 → fail-loud bij ID-verlies of schema-fout
[9] OCR-normalisator her-run  → controleer flag-reductie
```

## Gevolgen

**Nieuwe artefacten**:
- `tools/examen/extract_vragen_v2.py` — v2 extractor
- `tools/examen/migrate_to_v2.py` — migratie + antwoord-merge
- `tools/examen/validate_examen_v2.py` — schema-validator
- `tests/test_extract_vragen_v2.py` — pdfplumber-tabel-fixtures
- `tests/test_examen_v2_schema.py` — schema-conformance
- `data/programma/examen_vragen/_archive/v1/` — backup v1-JSON's

**Bestaande artefacten gewijzigd**:
- `data/programma/examen_vragen/*.json` — re-extract naar v2-schema, antwoorden behouden
- `tools/examen/extract_vragen.py` — vlaggen als deprecated (verwijst naar v2), niet verwijderen tot v2-stabiliteit bewezen
- `tools/examen/normalize_vraagteksten.py` — heroriënteer op v2 (broken_table heuristiek wordt overbodig zodra tabellen typed zijn; behoud trailing_ellipses + loose_caps voor de tekst-blokken)
- `prompts/modelantwoord-checklists.md` §2 — vraagtekst-discipline werkt op blokken bij voorkeur
- `tools/examen/_sub_vragen_splitter.py` — input nu concat-vraagtekst uit blokken (geen wijziging in werking)
- `docs/adr/ADR-020-modelantwoorden-voorbeeldexamens.md` — verwijzing naar ADR-021 in §6 (OCR-gate-context); blok-aware modelantwoord-formulering bij `kwalificatie`-/`berekening`-/`presentatie`-vraagtypes

**Niet-gewijzigd**:
- ADR-009 examenpatronen — examenfocus-objecten zijn agnostisch over interne vraagtekst-structuur
- ADR-010 render — minicursus-render toont vraagtekst via `> [!question]-` callouts, blok-rendering kan later toegevoegd (markdown-tabel in callout-body werkt out-of-the-box)
- Concept-records — geen impact
- Tests buiten examen-domein

**Risico's**:
- *pdfplumber tabel-detectie hallucineert* op multi-column-layouts → mitigatie: conservatieve settings, post-extract validatie, per-PDF tune
- *Antwoord-verlies bij migratie* → mitigatie: backup v1, fail-loud bij ID-verlies, dry-run mode in migratie-script
- *Subvragen-splitsing breekt* op concat met markdown-tabellen → mitigatie: tests op alle bestaande examens vóór destructief overschrijven
- *Modelantwoord-pipeline verslaat bestaande antwoorden* (vr11, vrB1, vrB2) → mitigatie: migratie kopieert per vraag-ID, geen run-over-runs door pipeline tenzij `correct_antwoord = null`

## Wat NIET in dit ADR

- **Formule-detectie** (LaTeX-extractie uit PDF) — uitgesteld naar v2.1
- **Figuur-extractie** (image-bbox + caption) — uitgesteld naar v2.1
- **Multi-column-layout PDF-parsing** (bv. tweekoloms-MC-opties) — handelt v2 niet expliciet af; bestaat al in `_sub_vragen_splitter.py` als convention
- **Vraag-ID-strategie** — bestaande deterministische generator (`<examen-id>-vr<nr>`) blijft; alleen stabiliteit gegarandeerd
- **OCR-fout-correctie** (loose_caps, weggevallen letters) — orthogonaal werk; blijft in `normalize_vraagteksten.py`-domein voor handmatige review-loop
- **Concept-/competentie-records** — geen wijziging; concept-laag is agnostisch over vraagtekst-structuur

## Changelog

- **v2.0 (2026-05-19)** — Eerste vastlegging na user-akkoord op aanpak (a) "ADR-021 eerst, dan re-extract". Status Accepted want de ontwerprichting is bekrachtigd; implementatie-details kunnen tijdens uitvoering nog verfijnd (PDF-specifieke tune van pdfplumber-settings) zonder ADR-update zolang het scope-binnen blijft.
