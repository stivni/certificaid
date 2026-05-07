# ADR-004: Chunk-level semantische keywords voor wetteksten

**Status**: Draft  
**Datum**: 2026-05-06

## Context

CBN-adviezen hebben een rijke `themas`-lijst in hun frontmatter (gemiddeld 7,1 keywords per advies, 1.548 unieke termen zoals `"eigendomsvoorbehoud"`, `"boekhoudkundige continuïteit"`). Deze keywords worden als metadata meegegeven aan elke chunk en verbetert de retrieval.

Wetteksten hebben enkel `tags: ["XVII", "4.0"]` — ITAA-LEX sectienummers, geen semantische informatie. Op wet-niveau keywords toevoegen is te grof: WIB92 bestrijkt beroepskosten, meerwaarden, kaaimantaks en honderden andere onderwerpen.

Keywords op chunk-niveau (per artikel) prependen aan de chunk-tekst is de cleanste oplossing: de embedding neemt ze mee zonder extra metadata-logica.

## Beslissing

**Genereer 5–10 semantische keywords per wettekst-chunk via KeyBERT (bge-m3, lokaal), prepend aan de chunk-tekst.**

```
# Vóór:
Art. 47

De onderworpen entiteiten ... melden aan de CFI ...

# Na:
[meldingsplicht, CFI, vermoeden witwassen, antiwitwaswetgeving,
 onderworpen entiteit, melding terrorismefinanciering]

Art. 47

De onderworpen entiteiten ... melden aan de CFI ...
```

### Aanpak

- Eenmalig script `tools/extractie/generate_keywords.py` (gebruikt KeyBERT met bge-m3 als backbone — volledig lokaal, geen API conform ADR-012): laadt elke wettekst, chunked op artikelen, extraheert 5–10 keywords per chunk
- Output: per wettekst een `resources/bronnen/wetteksten/keywords/NAAM.json` (map artikel-heading → keywords)
- `rag_index.py` leest dit bestand bij het indexeren en prepend de keywords aan de chunk-tekst
- Bronbestanden (`.md`) worden **niet** gewijzigd — keywords leven apart

### Prioriteit

Eerst de meest bevraagde bronnen: AWW, WIB92, WBTW, WVV, Wet-ITAA, WER. Daarna de rest iteratief.

### Pipeline-volgorde

Keywords zijn **per chunk** (per artikel-heading). De volgorde in de bronnen-pipeline is daardoor strikt:

1. **Chunken** volgens ADR-002 v2 (per artikel, met breadcrumb-prefix en path-metadata)
2. **Keywords genereren** met KeyBERT op die chunks → `resources/bronnen/wetteksten/keywords/<naam>.json`
3. **Indexeren** met `rag_index.py` — leest het keywords-bestand en prepend per chunk

Bij wijziging van de chunk-strategie (nieuwe ADR-002-versie, splitser-aanpassing): keywords opnieuw genereren. Anders zit de keyword-mapping op verouderde artikel-grenzen.

Bij update van een bronbestand: idem — eerst chunken, dan keywords her-genereren, dan indexeren.

## Gevolgen

- Lokale rekenkost voor keyword-generatie (KeyBERT met bge-m3 als backbone — geen Claude API conform ADR-012)
- Keywords-bestanden leven in `resources/bronnen/wetteksten/keywords/` (gitignored of gecommit — te beslissen)
- Bij update van een bronbestand: keywords opnieuw genereren voor dat bestand
- Bij chunk-strategie-wijziging (ADR-002): alle keywords opnieuw genereren
