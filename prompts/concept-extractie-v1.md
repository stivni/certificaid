# Prompt: Per-anker concept-extractie — Fase C (v1)

**Doel**: Extraheer uit een bundel bronchunks één of meerdere concept-records voor één ITAA-anker (ADR-008 fase C). Output volgt ADR-007 schema v1.1.

**Model**: claude-opus-4-7 (via subagent — zie ADR-008 §2)

---

## Context

Je krijgt een bundle-JSON met:
- **`anchor`**: het ITAA-anker (tekst, verbose, synoniemen) dat dit concept moet dekken
- **`bundle`**: een lijst bronchunks (wetteksten, ITAA-normen, CBN-adviezen) die via embedding-matching geselecteerd zijn als relevant voor dit anker

De chunks zijn gerankt op cosine-similariteit; de meest relevante staan bovenaan.

## Taak

Lees de bundle aandachtig. Extraheer voor dit anker:
- **1–3 concept-records** als de bundle meerdere duidelijk afzonderlijke fenomenen dekt
- **1 concept-record** in het meest gebruikelijke geval
- **0 records** als de bundle onvoldoende inhoudelijke dekking biedt (schrijf dan een korte reden in je output)

Een concept = een **tijdloos studieonderwerp** (een fenomeen, een beginsel, een procedure, een afwegingskader) — niet een wetsartikel en niet een vakindeling.

## Schema — ADR-007 v1.1

Elk concept-record is een JSON-bestand. Bestandsnaam: `<concept-slug>.json` (lowercase, koppeltekens, geen spaties).

### Verplichte top-level velden

```json
{
  "id": "<concept-slug>",
  "naam": "<leesbare naam, bv. 'Onafhankelijkheidsbedreiging'>",
  "node_type": "<zie onderstaande lijst>",
  "schema_version": "1.1",
  "status": "seed",
  "_provenance": {
    "extractor_run": "concept-extractie-v1-<ISO-8601-UTC>",
    "model": "claude-opus-4-7",
    "anchor_id": "<anchor_id uit bundle>",
    "reviewed_by": null
  }
}
```

### Node-types (kies het meest passende)

| type | hoofdveld | optioneel |
|---|---|---|
| `definitie` | `omschrijving` | `voorwaarden[]`, `uitzonderingen[]` |
| `procedure` | `verplichting`, `stappen[]` | — |
| `afwegingskader` | `doel`, `bouwstenen[]` | — |
| `drempel` | `norm`, `grens`, `gevolg` | — |
| `beginsel` | `stelling`, `ratio` | — |
| `rol` | `taken[]`, `bevoegdheden[]` | — |
| `casus` | `feiten`, `uitspraak` | — |
| `skill` | `omschrijving`, `subvaardigheden[]` | — |

Nieuw type nodig? Gebruik `node_type: "voorgesteld:<naam>"` — wordt verzameld voor review.

### Block-object (elk hoofdveld)

```json
"<veldnaam>": {
  "text": "<inhoud — parafraseer, geen copy-paste>",
  "confidence": "grounded",
  "source": {
    "type": "wet" | "kb" | "itaa-norm" | "cbn-advies" | "isa" | "jurisprudentie",
    "short": "<bv. 'AWW art. 47 §1' of 'CBN-advies 2021/06'>",
    "ref": {}
  },
  "references": [],
  "_provenance": {
    "inputs": [
      {"id": "<chunk_id>", "sha256": "<chunk_sha of null>", "version": "rag-v1"}
    ],
    "extracted_at": "<ISO-8601-UTC>",
    "extractor": "concept-extractie-v1"
  }
}
```

## Kritieke anti-hallucinatie-regels

1. **Elke claim verplicht `_provenance.inputs`** met de chunk_id(s) uit de bundle die de claim steunen. Geen claim zonder bron-chunk.
2. **Geen wetsartikelnummers verzinnen.** Artikelnummers die niet letterlijk in de bundel-chunks staan, schrijf je niet op. Wel aanwezig maar te gedetailleerd? Lift naar `references[]` met een `passage`-beschrijving, nummer in de `source`.
3. **`confidence: "grounded"`** alleen als de claim direct traceerbaar is naar een chunk. Gebruik `"inferred"` (🤖) als je redeneert buiten wat de chunks zeggen — maar minimaliseer dit.
4. **Lift-rule**: articelnummers, normpunten en verwijzingen horen in `references[]`, niet als inline tekst. Proxy: als je een zin schrijft die "zie art. …" of "conform punt …" bevat, verplaats die verwijzing naar `references[]`.
5. **`status: "seed"`** altijd — nooit "partieel" of "gevuld" bij eerste extractie.

## Output-instructies

Schrijf voor elk concept-record:
1. De naam van het bestand (`data/concept_records/<po>/<concept-slug>.json`)
2. Het volledige JSON-record

Sluit af met een kort overzicht:
- Welke chunks waren het meest informatief?
- Welke deelonderwerpen van het anker zijn *niet* gedekt door de bundle?
- Suggesties voor Fase D (verdieping): welke velden zijn nog leeg of slechts gedeeltelijk gevuld?
