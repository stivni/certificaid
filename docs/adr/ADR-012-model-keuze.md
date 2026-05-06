# ADR-012: Model-keuze — generatie en batch-verwerking

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Het systeem gebruikt taalmodellen op twee plaatsen: voor interactieve generatie (tutor-antwoorden, concept-extractie) en voor bulk-verwerking (keyword-generatie, patroon-extractie). Die hebben verschillende eisen: kwaliteit vs. snelheid/kost, en API vs. lokaal.

## Beslissing

**Twee niveaus:**

| Gebruik | Model | Locatie | Reden |
|---|---|---|---|
| Tutor-antwoorden, concept-extractie | `claude-sonnet-4-6` | Anthropic API | Beste kwaliteit voor juridisch redeneren in NL |
| Bulk keyword-generatie, patroon-extractie | Lokaal model (KeyBERT / YAKE / Ollama) | Lokaal | Geen API-kosten, geen toestemming nodig per run |

**Principe**: Claude API wordt **nooit automatisch** gebruikt zonder expliciete bevestiging van de gebruiker. Bulk-operaties (keyword-generatie, herindexering, concept-extractie in batch) draaien lokaal of vragen vooraf akkoord.

**Lokale keyword-extractie**: KeyBERT met bge-m3 als backbone (ADR-001 — zelfde model, geen extra download). Alternatief: YAKE (puur statistisch, geen model).

## Gevolgen

- `tools/generate_keywords.py` gebruikt KeyBERT/YAKE, geen Anthropic SDK
- `ANTHROPIC_API_KEY` is nodig voor tutor en concept_extractor, maar niet voor indexering
- Bij toekomstige model-upgrades: tutor en concept_extractor aanpassen, keywords-pipeline ongewijzigd
