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

- Leest live `data/concept_records/` en `data/exam_patterns/` via NetworkX (ADR-007) + concepten-RAG (ADR-006)
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

## Gevolgen

- `tutor/app.py` — Streamlit, leest concept-laag direct
- `tools/snapshot/` (nieuw) — concepten → fiches → versie-tag
- `content/snapshots/<versie>/` — gepubliceerde leerstof (Quartz-input)
- `content/` als losse-fiches-map verdwijnt geleidelijk; bestaande programmaonderdeel-, competentie- en materie-content gaat naar `_archive/` zodra de eerste snapshot stabiel is
- Tutor en snapshot-renderer delen template-logica voor confidence-labeling, citaties en wikilink-resolutie
