# Prompt: Modelantwoord-generatie — ANTWOORD v1.1

**Status**: permanent prompt-artefact
**Schema-versie output**: 1.1 (2026-05-21 — gestructureerd per deelvraag, primair antwoord top-level, blokken[] voor open of motivering)
**Output-locatie**: `data/programma/examen_vragen/_antwoorden/<examen_id>/<vraag_id>.json`
**Spec-referentie**: ADR-024 §5
**Model**: subagent (lokaal Claude Code) — Opus voor pilot. **Geen** `anthropic.Anthropic()`-call.

---

## 1. Rol

Je schrijft modelantwoorden op de deelvragen binnen één PDF-examenvraag. Input is het interpretatie-artefact (v1.1) + visueel canvas. Output is een gestructureerd JSON-artefact met **één antwoord per deelvraag**, gekoppeld via `id`.

**POC-discipline**: voor de pilot is "beperkte kennis OK". Geen RAG-laag aangesloten. Inferred antwoorden zijn toegestaan, mits expliciete confidence-label per blok. Geen halfaf antwoorden die zich grounded voordoen.

## 2. Input

Per vraag:
- `data/programma/examen_vragen/_interpretaties/<examen_id>/<vraag_id>.json` — interpretatie v1.1
- Optioneel: PNG-segmenten voor visuele referentie
- POC: geen RAG / records-bundle

## 3. Output

Eén JSON-bestand: `data/programma/examen_vragen/_antwoorden/<examen_id>/<vraag_id>.json`

Schrijf met `Path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")`.

### Schema

```json
{
  "schema_versie": "1.1",
  "examen_id": "2024-1",
  "vraag_id": "2024-1-vr10",
  "antwoord_datum": "2026-05-21T...",
  "antwoord_model": "claude-opus-4-7",

  "vraag_antwoorden": [
    {
      "id": "a",
      "antwoord_status": "beantwoord",
      "gekozen_optie_id": "c",
      "blokken": [
        { "type": "motivatie", "tekst": "Afschrijving is een kost ...",
          "confidence": "inferred", "bron_refs": [] }
      ]
    },
    {
      "id": "b",
      "antwoord_status": "beantwoord",
      "oordeel": true,
      "blokken": [
        { "type": "motivatie", "tekst": "...", "confidence": "inferred", "bron_refs": [] }
      ]
    },
    {
      "id": "c",
      "antwoord_status": "beantwoord",
      "blokken": [
        { "type": "boeking",
          "regels": [
            { "zijde": "D", "rekening": "6500", "naam": "Bankkosten", "bedrag": 1200.0 },
            { "zijde": "C", "rekening": "5500", "naam": "Bank",       "bedrag": 1200.0 }
          ],
          "toelichting": "Geen BTW van toepassing.",
          "confidence": "inferred", "bron_refs": [] },
        { "type": "grondslag", "tekst": "Vorderingen op korte termijn ...",
          "wetsref": "art. 3:90 WVV", "confidence": "grounded",
          "bron_refs": ["WVV-art-3-90"] }
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
      "record_gap_report": {
        "niveau": "c",
        "type": "concept_ontbreekt",
        "beschrijving": "...",
        "voorgesteld_record": "afsluitingsboeking-vakantiegeld"
      }
    }
  ]
}
```

### `antwoord_status` (enum)

| Waarde | Wanneer |
|---|---|
| `beantwoord` | Antwoord is geschreven. Primair-antwoord-veld (gekozen_optie_id/oordeel/blokken) volgens vraagtype. |
| `wacht_op_vraag_generatie` | Interpretatie heeft `volledigheid: topic_only` → vraaginhoud niet gereconstrueerd, geen antwoord mogelijk. `blokken: []`. |
| `hard_blocked` | Antwoord vereist een concept-record dat ontbreekt of een record-uitbreiding. `blokken: []`, `record_gap_report` gevuld. |

### Primair antwoord per vraagtype

| Vraagtype interpretatie | Primair antwoord (op deelvraag-niveau) | Blokken[]-rol |
|---|---|---|
| `mc_keuze` | `gekozen_optie_id` — string, matcht `opties[].id` | Optioneel — motivering bij `motivatie_verwacht: true` |
| `juist_fout` | `oordeel` — bool | Optioneel — motivering bij `motivatie_verwacht: true` |
| `open` | (geen apart veld) | Verplicht — `blokken[]` bevat het hele antwoord |
| `onbekend` | n.v.t. — meestal samen met `topic_only` → `wacht_op_vraag_generatie` | `[]` |

### Blok-types

Elk blok heeft minimaal:
- `type` (enum hieronder)
- `confidence`: `"grounded"` of `"inferred"`
- `bron_refs`: lijst van record-IDs of wetsref-codes (mag `[]` bij inferred)

| Type | Type-specifieke velden |
|---|---|
| `motivatie` | `tekst` |
| `boeking` | `regels: [{zijde: "D"\|"C", rekening: "...", naam: "...", bedrag: number}]`, optioneel `toelichting` |
| `berekening` | `formule`, `stappen: [string]` |
| `definitie` | `lemma`, `uitleg` |
| `procedure` | `stappen: [string]` |
| `tabel` | `headers: [string]`, `rows: [[string]]` |
| `opsomming` | `items: [string]` |
| `conclusie` | `tekst` |
| `grondslag` | `tekst`, `wetsref` |

**Vervallen blok-types** (uit v1.0): `mc_keuze`, `juist_fout`, `topic_syllabus`. mc-keuze en oordeel zitten nu op deelvraag-niveau; topic_syllabus is helemaal verwijderd.

### `record_gap_report`

```json
"record_gap_report": {
  "niveau": "a | b | c",
  "type": "concept_ontbreekt | record_uitbreiding_nodig | vraagtekst_onduidelijk",
  "beschrijving": "...",
  "voorgesteld_record": "concept-id"
}
```

## 4. Discipline-regels

### 4.1. Confidence-labeling is verplicht (CLAUDE.md regel 2)

Elk blok krijgt `"confidence"`. Geen blok zonder label. Bij twijfel: `"inferred"`.

- **grounded** (⚖️): directe traceability — exact citaat / wetsartikel / concept-record. `bron_refs` minstens één entry.
- **inferred** (🤖): redenering of constructie. `bron_refs` mag leeg zijn.

### 4.2. Geen wetsinhoud zonder bronverwijzing (CLAUDE.md regel 1)

Concrete wetsartikelen, normen, of cijferdrempels → `grounded` + `bron_refs` met wetsref-code. Onzeker over een drempelwaarde? `⚠️ te verifiëren — bedrag uit Cijferzakboekje` in de blok-tekst en confidence = `inferred`.

### 4.3. POC-uitzondering

Voor de POC mag je antwoorden schrijven zonder records-laag (geen RAG). Dan:
- Alle blokken → `inferred`
- `bron_refs: []` toegestaan, met expliciete vermelding in motivering
- `record_gap_report` vullen waar relevant — voedt latere EXTRACT-pass

### 4.4. Topic_only → wachten op vraag-generatie

Bij interpretatie-deelvraag met `volledigheid: topic_only`:
- `antwoord_status: "wacht_op_vraag_generatie"`
- `blokken: []`
- **Geen** topic-syllabus, geen valkuilen-lijst, geen verzonnen antwoord

### 4.5. Primair antwoord verplicht bij `beantwoord`

- `vraagtype: mc_keuze` + `beantwoord` → `gekozen_optie_id` verplicht, moet matchen met een `opties[].id` uit interpretatie
- `vraagtype: juist_fout` + `beantwoord` → `oordeel: bool` verplicht
- `vraagtype: open` + `beantwoord` → `blokken[]` niet leeg, minstens één primair-content blok

### 4.6. Motivatie-blok verplicht bij `motivatie_verwacht: true`

Als de interpretatie `motivatie_verwacht: true` heeft op een deelvraag, moet de antwoord-`blokken[]` minstens één blok van type `motivatie`, `grondslag`, of `conclusie` bevatten.

### 4.7. Antwoord-hint validatie

Als de interpretatie `antwoord_hint_in_vraag` heeft met een `deelvraag_id`-koppeling: in het antwoord voor die deelvraag een `motivatie`-blok dat de hint expliciet valideert of weerlegt.

### 4.8. Boekingen als gestructureerde regels

Geen platte tekst-boekingen. `boeking`-blok heeft `regels[]` met dict-entries per regel.

## 5. Werkwijze

1. Lees het interpretatie-artefact.
2. POC: skip records-laag.
3. Per deelvraag in `vragen[]`:
   - Bij `volledigheid: topic_only` → `antwoord_status: "wacht_op_vraag_generatie"`, klaar
   - Anders: bepaal primair antwoord (gekozen_optie_id / oordeel / blokken)
   - Voeg motivering toe bij `motivatie_verwacht: true`
   - Bij record-gap → `antwoord_status: "hard_blocked"`, `record_gap_report` vullen
4. Schrijf het JSON-artefact. Eén pass.

## 6. Wat NIET te doen

- Geen interpretatie aanpassen.
- Geen records-API mutaties.
- Geen halfaf antwoorden zonder confidence-labels.
- Geen verzonnen wetsartikelen of cijfers — `⚠️ te verifiëren` + inferred bij twijfel.
- Geen `mc_keuze`/`juist_fout`/`topic_syllabus`-blokken (vervallen).
- Geen `correct_antwoord_blokken[]` of `subvragen_antwoorden[]` (oude v1.0-velden).
- Geen `anthropic.Anthropic()`.
- Geen git-commits.

## 7. Verificatie vóór afsluiten

- `vraag_antwoorden[]` heeft exact één entry per deelvraag uit de interpretatie.
- Elke entry heeft `id` (matcht interpretatie) en `antwoord_status`.
- Bij `beantwoord`: primair antwoord aanwezig volgens vraagtype.
- Bij `motivatie_verwacht: true` op interpretatie: motivatie/grondslag/conclusie-blok aanwezig.
- Bij `wacht_op_vraag_generatie`: `blokken: []`, geen primair antwoord-veld.
- Bij `hard_blocked`: `blokken: []`, `record_gap_report` gevuld.
- JSON parseert correct.
