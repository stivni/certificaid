# ADR-009: Concept record JSON-schema

**Status**: Draft  
**Datum**: 2026-05-06

## Context

De conceptlaag is de brug tussen ruwe wetteksten en de tutor. Een concept record is het resultaat van één extractieronde: Claude verwerkt RAG-chunks + TDK-anker tot een gestructureerd JSON-object. Dat object wordt zelf geïndexeerd in de `concepts` ChromaDB-collection.

Het schema moet:
- Alle examendimensies dekken (definitie, uitzonderingen, procedures, valkuilen, voorbeelden)
- Machineleesbaar zijn voor de twee-pass tutor (ADR-005)
- Confidence per veld bijhouden (ADR-007)
- Uitbreidbaar zijn zonder breuk van bestaande records

## Beslissing

**Canonical schema** (`data/concept_records/*.json`):

```json
{
  "id": "concept:naam-van-concept",
  "naam": "Naam van het concept",
  "po_ref": ["4.0"],
  "tdk_anker": "Omschrijving van de TDK die dit concept verankert",
  "main_rule": {
    "text": "De hoofdregel in één of twee zinnen.",
    "sources": [{"ref": "Art. 47 AWW", "bron_rol": "itaa_lex"}],
    "confidence": "grounded"
  },
  "exceptions": [
    {
      "naam": "Naam van de uitzondering",
      "text": "Beschrijving.",
      "sources": [{"ref": "Art. 54 AWW", "bron_rol": "itaa_lex"}],
      "confidence": "grounded"
    }
  ],
  "scope": {
    "applies_to": "Op wie/wat is het van toepassing?",
    "excludes": "Wat valt er expliciet buiten?",
    "sources": []
  },
  "obligations": [
    {"text": "Wat moet verplicht gebeuren?", "sources": [], "confidence": "grounded"}
  ],
  "pitfalls": [
    {"text": "Veelgemaakte redeneerfouten.", "confidence": "inferred"}
  ],
  "examples": [
    {"text": "Concreet voorbeeld.", "context": "situatieschets", "sources": [], "confidence": "inferred"}
  ],
  "related_concepts": ["concept:ander-concept"],
  "confidence": 0.85
}
```

**Regels:**
- `exceptions` zo volledig mogelijk — dit is het meest bevraagd op het examen
- `pitfalls` altijd `confidence: inferred` — dit zijn redeneringen, niet geciteerde feiten
- `confidence` (root) = gewogen gemiddelde van alle veld-confidences
- Elk record = één concept; nooit twee concepten samenvoegen in één record

## Gevolgen

- `tools/extractie/concept_extractor.py` genereert dit schema
- `tools/rag/rag_index.py` chunked het per veld voor de `concepts` collection
- Schema-wijzigingen vereisen herbouw van de concepts-collection
- Bestaande records zijn niet automatisch compatibel bij schema-breaking changes
