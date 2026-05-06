# ADR-002: Chunk-strategie — small-to-big met begrensd context-venster

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Twee conflicterende behoeften:
1. **Retrieval**: kleine chunks geven precieze embeddings — één concept per vector
2. **Generatie**: Claude heeft context nodig rondom een gevonden passage — een geïsoleerd artikel of halve adviesalinea is onvoldoende

Naive parent retrieval (laad de volledige wet als match gevonden) is onbruikbaar: WIB92 is 400K+ chars, WER is nog groter. Dat past niet in context en is ook niet nuttig.

## Beslissing

**Indexeer kleine chunks, maar laad begrensd omliggende context bij retrieval.**

### Wetteksten

- Indexeer per artikel (`## Art. X`)
- Sla op in metadata: `chunk_index`, `prev_chunk_id`, `next_chunk_id`, `parent_section` (dichtstbijzijnde BOEK/TITEL/AFDELING-heading)
- Bij retrieval: laad het gevonden artikel + maximaal **2 omliggende artikelen** (prev + next)
- Reden: definities staan vaak net daarvoor, uitzonderingen net daarna
- Bovengrens context-venster: ~3 artikelen ≈ 1.500–3.000 tokens — beheersbaar

### CBN-adviezen

- Een advies behandelt één concept — het is zinvol als geheel
- Indexeer als **één chunk** als het advies ≤ 40.000 chars (≈ 8.000 tokens, past in bge-m3 window)
- Adviezen > 40.000 chars (~10% van 436): split op `##`-secties, elke sectie krijgt adviestitel als prefix
- Bij retrieval: laad de volledige chunkinhoud (geen uitbreiding nodig — de chunk IS al het advies)

### ITAA-normen

- Zelfde als wetteksten: per sectie chunken, ±1 omliggende sectie bij retrieval

### Praktijkgidsen en toelichtingen (`bron_rol: praktijkgids`)

- Toelichtingen zijn lopende tekst per code/vak, geen artikel-structuur
- Chunken op vaste grootte (~1.000 tokens) met 20% overlap
- Geen context-uitbreiding — toelichtingen zijn redactioneel en minder juridisch precies

## Gevolgen

- `rag_index.py`: chunk-metadata uitbreiden met `chunk_index`, `prev_chunk_id`, `next_chunk_id`, `parent_section`
- `retrieve()`-functie in tutor en concept_extractor: na retrieval context-uitbreiding toepassen
- Geen volledige documenten in context — bovengrens bewust gedefinieerd per brontype
