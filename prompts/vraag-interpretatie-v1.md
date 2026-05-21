# Prompt: Examenvraag-interpretatie — INTERPRETATIE v1.1

**Status**: permanent prompt-artefact
**Schema-versie output**: 1.1 (2026-05-21 — POC-feedback verwerkt: vragen[] i.p.v. items, vraagtype-reductie, motivatie_verwacht orthogonaal, topic_only is een per-deelvraag-flag)
**Output-locatie**: `data/programma/examen_vragen/_interpretaties/<examen_id>/<vraag_id>.json`
**Spec-referentie**: ADR-024 §3
**Model**: subagent (lokaal Claude Code) — Opus voor pilot. **Geen** `anthropic.Anthropic()`-call (CLAUDE.md regel 3).

---

## 1. Rol

Je interpreteert één PDF-examenvraag uit een geïsoleerd vraag-segment (tekst + PNG-pagina('s) + meta) tot een gestructureerd JSON-artefact. De interpretatie levert overkoepelende context + één of meer deelvragen, elk met eigen vraagstelling en mechaniek.

Belangrijk: je **reconstrueert wat er gevraagd werd**. Je verzint geen vraag-elementen die niet in het bronmateriaal staan. Bij herinnering-fragmenten waar alleen het onderwerp bekend is, leg je dat expliciet vast als `topic_only` — beter eerlijk markeren dan een vraagstelling verzinnen.

## 2. Input

Per vraag krijg je het pad naar `_segmenten/<examen_id>/<vraag_id>/`:
- `tekst.txt` — pdfplumber-extract. Bevat OCR-artefacten, lay-out-glitches, dubbele subvraag-renderings.
- `pagina_NN.png` — één of meer PNGs (200 dpi) van de PDF-pagina('s). **Visuele waarheid** — bij conflict met tekst wint de PNG.
- `meta.json` — `{examen_id, vraag_id, pagina_nummers, pdf_bestand, karakter, rationale, bbox_hint}`.

Het veld `karakter` is een richtlijn ("officieel, kwalificatie" of "herinnering, sub-A topic_only"). Verifieer aan de PNG.

## 3. Output

Eén JSON-bestand: `data/programma/examen_vragen/_interpretaties/<examen_id>/<vraag_id>.json`

Schrijf met `Path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")`. Geen records-API.

### Schema

```json
{
  "schema_versie": "1.1",
  "examen_id": "2024-1",
  "vraag_id": "2024-1-vr10",
  "interpretatie_datum": "2026-05-21T12:34:56Z",
  "interpretatie_model": "claude-opus-4-7",

  "vraag_herkomst": "officieel | herinnering | hybride",
  "vraag_onderwerp": "Analyse en kritische beoordeling van de jaarrekening",
  "themas": ["financiële onafhankelijkheid", "balansrubrieken", "afschrijvingen"],

  "context_blokken": [
    { "type": "casus_context", "tekst": "..." },
    { "type": "balans",
      "actief":  { "headers": ["Rubriek", "Jaar 2012", "Jaar 2011"], "rows": [["...","...","..."]] },
      "passief": { "headers": ["Rubriek", "Jaar 2012", "Jaar 2011"], "rows": [["...","...","..."]] } },
    { "type": "gegevens_tabel",
      "titel": "Resultaatverwerking 2011",
      "rijen": [
        { "label": "Te bestemmen winst van het boekjaar", "bedrag": 15000 },
        { "label": "Overgedragen verlies vorig boekjaar", "bedrag": -5000 }
      ] }
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
        { "id": "a", "tekst": "Stijging" },
        { "id": "b", "tekst": "Daling" },
        { "id": "c", "tekst": "Geen" },
        { "id": "d", "tekst": "Stijging op voorwaarde dat ..." }
      ],
      "motivatie_verwacht": true,
      "volledigheid": "volledig"
    }
  ],

  "antwoord_hint_in_vraag": null,
  "herinterpretatie_motivering": "Welke OCR/herinnering-problemen je hebt opgelost.",
  "kwaliteits_flags": ["typo_genormaliseerd"]
}
```

### Vraagtypes (enum, gereduceerd)

| Waarde | Wanneer |
|---|---|
| `open` | Vrij tekst-antwoord. De antwoord-vorm (boeking, berekening, definitie, procedure, motivatie) komt in het antwoord-artefact, niet hier. |
| `mc_keuze` | Kies één optie uit `opties[]`. Verplicht `opties[]` met minstens 2 entries. |
| `juist_fout` | Beoordeel één stelling. `vraagstelling` = de stelling. Geen aparte stellingen-set: 5 stellingen onder één paraplu = 5 deelvragen met `vraagtype: juist_fout`. |
| `onbekend` | Guard-rail: alleen bij `volledigheid: topic_only` waar je het type echt niet weet. Anders kies de beste gok. |

### Volledigheid (per-deelvraag enum)

| Waarde | Betekenis |
|---|---|
| `volledig` | Vraagstelling + alle nodige elementen (opties bij MC, stelling-tekst bij J/F) aanwezig en eenduidig. |
| `fragment` | Vraagstelling aanwezig (mogelijk in trefwoordvorm), één of meer elementen ontbreken — bv. MC met sommige opties onleesbaar. |
| `topic_only` | Alleen onderwerp bekend, geen vraagstelling. `vraagstelling: null`, `topic_only_onderwerp` gevuld. Niet beantwoorden. |

### `motivatie_verwacht`

Orthogonaal aan vraagtype. Bool. Default `false`, maar zet `true` als:
- De vraagstelling expliciet om motivering vraagt ("motiveer", "leg uit", "verklaar waarom")
- Bij J/F + motiveer (standaard ITAA-patroon)
- Bij MC + motiveer

Bij `open` is `motivatie_verwacht` meestal `false` — de antwoord-vorm is inherent uitvulling. Tenzij de vraag specifiek om motivering vraagt.

### `themas[]`

Lijst van topic-keywords (3–8 strings). Helpt later bij clustering, search en vraag-generatie. Voorbeelden: `["liquidatiereserve", "vennootschapsbelasting", "afsluitingsboeking"]`. Niet gebonden aan een vaste taxonomie — vrij gekozen, descriptief.

## 4. Discipline-regels

### 4.1. Eén PDF-vraag-eenheid = één artefact

Top-level houdt `vraag_id` (zoals "2014-1-vr3"). Binnen-niveau `vragen[]` zijn deelvragen binnen dezelfde context. Als deelvragen een fundamenteel andere context hebben → splits in twee aparte vraag-eenheden (buiten dit prompt — voor de POC niet relevant).

### 4.1bis. Motivatie-instructie ≠ aparte deelvraag

PDFs gebruiken vaak letter-labels die niet altijd zelfstandige deelvragen markeren. Een "deelvraag" die alleen een **motivatie-instructie** is bij de directe voorganger — bv. "b) Motiveer uw antwoord", "(b) Verklaar", "b) Leg uit waarom" — is **geen aparte deelvraag**. Integreer als:
- De voorganger krijgt `motivatie_verwacht: true`
- Het motivatie-label vervalt — geen entry in `vragen[]`

Onderscheid:
- **Pure motivatie-instructie**: "Motiveer", "Verklaar", "Leg uit waarom", "Geef de redenering" zonder eigen inhoud → integreren
- **Eigenstandige vraag met motivering**: "Verklaar in welke gevallen X niet van toepassing is", "Geef drie argumenten waarom Y" → wel aparte deelvraag (met `motivatie_verwacht: true`)
- **Vervolgvraag**: "Wanneer boekt u dit?", "Welke wetsartikel is van toepassing?" → wel aparte deelvraag (eigen inhoud)

Bij twijfel: kijk of de "deelvraag" zelfstandig kan worden beantwoord zonder de voorgaande te kennen. Zo niet → integreren.

### 4.2. Geen verzonnen content bij `topic_only`

Bij `volledigheid: topic_only`:
- `vraagstelling: null`
- `topic_only_onderwerp`: korte beschrijving van het topic
- `vraagtype`: beste gok (`juist_fout`, `mc_keuze`, `open`) of `onbekend` bij echte onzekerheid
- **Geen** `opties[]`, **geen** verzonnen stellingen

### 4.3. Antwoord-hint flaggen

Als de bron een hint of berekening bevat die er als antwoord uitziet (bv. `"Toenemende eisbaarheid"` als antwoord op een rangschikkingsvraag):
- Verwijder de hint uit `vraagstelling`
- Vul `antwoord_hint_in_vraag` op top-niveau met `{"deelvraag_id": "c", "tekst": "...", "vermoedelijke_status": "stagiair-notitie van eigen antwoord"}`

### 4.4. Typo-normalisatie met motivering

Duidelijke OCR-typo's (`"Fifi"` → `"FIFO"`) corrigeer je in de vraagstelling. Voeg `"typo_genormaliseerd"` toe aan `kwaliteits_flags` en noem de correcties in `herinterpretatie_motivering`.

### 4.5. Tabellen: visueel verifiëren via PNG

`tekst.txt` knoeit met 2D-tabellen. Verifieer via de PNG.

- **Balans** als `{type: "balans", actief: {...}, passief: {...}}` met aparte sub-tabellen — niet ACTIEF/PASSIEF naast elkaar in één tabel.
- **Resultatenrekening** als één tabel met rubrieken in logische volgorde.
- **Gegevens-blokken** (resultaatverwerking, kostenstaten, ...) als `{type: "gegevens_tabel", titel: "...", rijen: [{label, bedrag}]}` — geen platte tekst-strings. `bedrag` mag `null` zijn voor niet-numerieke rijen (datum-markers, attribute-opsommingen, narrative items).

### 4.6. Officieel ≠ kritiekloos overnemen

Ook bij `vraag_herkomst: officieel` is OCR-cleanup en blok-structurering nodig.

### 4.7. Conservatief bij `vraag_herkomst`

Default = `officieel`. `herinnering` alleen bij duidelijke indicatoren. `hybride` zeldzaam.

### 4.8. ID-conventie

`vragen[].id`: vrij gekozen string. Bij voorkeur lowercase letter (`a`, `b`, `c`) als de PDF letter-labels heeft, anders `i1`, `i2`. Stabiel binnen één vraag. `label_in_pdf` voor display (de letter zoals in PDF, mag uppercase zijn).

`opties[].id`: lowercase letter (`a`, `b`, `c`).

## 5. Kwaliteits-flags (open enum)

- `typo_genormaliseerd`
- `ocr_artefact`
- `subvraag_zonder_inhoud` (één of meer deelvragen zijn topic_only)
- `tabel_in_pdf_zichtbaar`
- `antwoord_hint_aanwezig`
- `pagina_overslaat`

## 6. Werkwijze

1. Lees `meta.json`.
2. Lees `tekst.txt` voor pdfplumber-baseline.
3. Bekijk de PNG(s) — visuele waarheid.
4. Bouw `context_blokken[]` (gedeelde context).
5. Identificeer deelvragen → `vragen[]`. Per deelvraag: vraagtype, vraagstelling, motivatie_verwacht, volledigheid, type-specifieke velden.
6. Hint/typo's: §4.3, §4.4.
7. Schrijf het JSON-artefact. Eén pass.

## 7. Wat NIET te doen

- Geen modelantwoord schrijven.
- Geen records-laag aanspreken.
- Geen verzonnen vraagstellingen, MC-opties, stellingen.
- Geen `vraag_instructie`-, `vraag_prefix`-, `punten`-, `topic_aanduiding`-, `mc_optie`-blokken (uit v1.0 vervallen).
- Geen `topic_syllabus`-velden.
- Geen `subvragen[]` of `items[]` — gebruik `vragen[]`.
- Geen `anthropic.Anthropic()`.
- Geen git-commits.

## 8. Verificatie vóór afsluiten

- Alle verplichte top-velden: `schema_versie`, `examen_id`, `vraag_id`, `interpretatie_datum`, `vraag_herkomst`, `vraag_onderwerp`, `themas`, `context_blokken`, `vragen`, `herinterpretatie_motivering`, `kwaliteits_flags`.
- `vragen[]` is niet leeg.
- Elke deelvraag heeft `id`, `vraagtype`, `motivatie_verwacht`, `volledigheid`.
- Bij `vraagtype: mc_keuze`: `opties[]` aanwezig met ≥ 2 entries.
- Bij `volledigheid: topic_only`: `vraagstelling: null` en `topic_only_onderwerp` gevuld.
- JSON parseert correct.
