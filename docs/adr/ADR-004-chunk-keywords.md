# ADR-004: Chunk-level semantische keywords voor wetteksten

**Status**: Accepted  
**Datum**: 2026-05-06

## Context

CBN-adviezen hebben een rijke `themas`-lijst in hun frontmatter (gemiddeld 7,1 keywords per advies, 1.548 unieke termen zoals `"eigendomsvoorbehoud"`, `"boekhoudkundige continuïteit"`). Deze keywords worden als metadata meegegeven aan elke chunk en verbetert de retrieval.

Wetteksten hebben enkel `tags: ["XVII", "4.0"]` — ITAA-LEX sectienummers, geen semantische informatie. Op wet-niveau keywords toevoegen is te grof: WIB92 bestrijkt beroepskosten, meerwaarden, kaaimantaks en honderden andere onderwerpen.

Keywords op chunk-niveau (per artikel) prependen aan de chunk-tekst is de cleanste oplossing: de embedding neemt ze mee zonder extra metadata-logica.

## Beslissing

**Genereer 5–10 semantische keywords per wettekst-chunk via Claude, prepend aan de chunk-tekst.**

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

- Eenmalig script `tools/generate_keywords.py`: laadt elke wettekst, chunked op artikelen, vraagt Claude per chunk om 5–10 keywords
- Output: per wettekst een `resources/bronnen/wetteksten/keywords/NAAM.json` (map artikel-heading → keywords)
- `rag_index.py` leest dit bestand bij het indexeren en prepend de keywords aan de chunk-tekst
- Bronbestanden (`.md`) worden **niet** gewijzigd — keywords leven apart

### Prioriteit

Eerst de meest bevraagde bronnen: AWW, WIB92, WBTW, WVV, Wet-ITAA, WER. Daarna de rest iteratief.

## Gevolgen

- Eenmalig API-kost voor keyword-generatie (Claude Haiku, goedkoop)
- Keywords-bestanden leven in `resources/bronnen/wetteksten/keywords/` (gitignored of gecommit — te beslissen)
- Bij update van een bronbestand: keywords opnieuw genereren voor dat bestand
