# ADR-002: Chunk-strategie — small-to-big met breadcrumb-prefix en gestructureerd path

**Status**: Draft (versie 2)
**Datum**: 2026-05-07
**Vervangt**: ADR-002 versie 1 (zie git history; oude versie definieerde "indexeer per artikel" zonder splitser-anker en gebruikte een vlak `parent_section`-veld dat enkel de meest recente structurele heading bevatte)

## Context

Twee conflicterende behoeften:
1. **Retrieval**: kleine chunks geven precieze embeddings — één concept per vector
2. **Generatie**: Sonnet heeft context nodig rondom een gevonden passage — een geïsoleerd artikel of halve adviesalinea is onvoldoende

Naive parent retrieval (laad de volledige wet als match gevonden) is onbruikbaar: WIB92 is 400K+ chars, WER is nog groter. Dat past niet in context en is ook niet nuttig.

**Drie tekortkomingen aan v1 die deze versie adresseert:**

1. **Geen domein-anker in de embedding.** v1 zette enkel `## Art. 47` als heading bovenaan de chunk. De wetnaam ("Antiwitwaswet") zat alleen in metadata. bge-m3 embedt de chunk-tekst, niet metadata, dus een query "antiwitwaswet meldingsplicht" matchte slecht op chunks die het woord "antiwitwaswet" niet bevatten.
2. **`parent_section` was te grof.** Alleen de meest recente structurele heading werd opgeslagen — typisch `HOOFDSTUK II.` zonder naam en zonder TITEL-context. WIB92 had 798 chunks met slechts 16 unieke `parent_section`-waarden (bv. `HOOFDSTUK II.` ×281, `HOOFDSTUK III.` ×211). Ondisambigueerbaar.
3. **Splitser splitste op àlle headings (H1-H4), niet enkel op artikelen.** Sub-headings binnen een artikel (`### §1`) kregen een eigen chunk. Daardoor klopte de "±2 buurartikelen"-belofte niet: `chunk_index ± 2` kon sub-secties van hetzelfde artikel pakken i.p.v. buurartikelen.

## Beslissing

**Indexeer per natuurlijke eenheid (artikel voor wetteksten), prepend een breadcrumb-prefix met semantische namen aan de chunk-tekst, en bewaar de structurele hiërarchie als gestructureerd path in metadata.**

### 1. Splitsing — strikte artikel-grens

Splits **uitsluitend** op artikel-headings. `_is_article_heading()` is de gezagsbron (matcht `## Art.` en `## Par.`-patronen). Sub-headings binnen een artikel (`### §1`, `### A. Werknemers`) blijven inline binnen dezelfde chunk.

Voor bronnen zonder artikel-structuur (CBN-adviezen, ITAA-normen, praktijkgidzen): zie per-brontype-regels hieronder.

### 2. Breadcrumb-prefix in embedded tekst — namen, niet markers

Elke chunk krijgt een prefix-regel met de **semantische namen** van de structurele context. Niet "TITEL III" maar "Onderworpen entiteiten". Markers zonder naam ("HOOFDSTUK II") zijn semantisch leeg voor bge-m3.

Voorbeeld voor een wettekst:

```
[Antiwitwaswet 2017 → Onderworpen entiteiten → Specifieke analyse → Beoordelingsverplichting]

## Art. 46

In de gevallen bedoeld in...
```

Per brontype:

| Brontype | Breadcrumb-format |
|---|---|
| **Wet** | `[<wet-naam> → <titel-naam> → <hoofdstuk-naam> → <afdeling-naam>]` (alleen niveaus die voorkomen) |
| **CBN-advies** (klein, 1 chunk) | `[CBN-advies <nr> — <onderwerp-titel>]` |
| **CBN-advies** (groot, gesplitst op `##`) | `[CBN-advies <nr> — <onderwerp-titel> → <sectie-naam>]` |
| **ITAA-norm** | `[Norm <naam> — <sectie-naam>]` |
| **Praktijkgids** | TODO (zie open vragen onderaan) |
| **TDK / fiche / concept** | `[<bron-naam> — <heading>]` (één niveau) |

Het nummer (`Titel III`, `KB nr. 1`) staat in de metadata-path, niet in de breadcrumb-tekst — naam alleen volstaat semantisch.

### 3. Path in metadata — gestructureerd

Naast de breadcrumb-tekst bewaart elke chunk een `path`-array als JSON-string in de metadata:

```python
"path": json.dumps([
    {"type": "wet",       "nr": "",    "naam": "Antiwitwaswet 2017"},
    {"type": "TITEL",     "nr": "III", "naam": "Onderworpen entiteiten"},
    {"type": "HOOFDSTUK", "nr": "II",  "naam": "Specifieke analyse"},
    {"type": "AFDELING",  "nr": "2",   "naam": "Beoordelingsverplichting"},
    {"type": "Art.",      "nr": "46",  "naam": ""}
])
```

Drie consumenten:
1. **Citatie-rendering** in tutor-UI: "Antiwitwaswet, Titel III — Onderworpen entiteiten, Hoofdstuk II — Specifieke analyse, Afdeling 2, Art. 46" zonder string-parsing.
2. **Filtering** op deelhiërarchie ("alleen chunks onder Titel III").
3. **Concept-extractie** (ADR-009): de extractor weet snel in welke structurele context een artikel staat, zonder het breadcrumb-veld te parsen.

ChromaDB ondersteunt geen geneste objecten; daarom JSON-string. Vervangt het v1-veld `parent_section` volledig.

### 4. Per-brontype-regels

#### Wetteksten

- Indexeer per artikel (zie regel 1)
- Bewaar in metadata: `chunk_index`, `path` (JSON-string)
- Bij retrieval: laad het gevonden artikel + maximaal **±2 buurchunks** (= ±2 artikelen, omdat chunk = artikel)
- Reden: definities staan vaak net daarvoor, uitzonderingen net daarna
- Bovengrens context-venster: ~5 artikelen ≈ 1.500–3.000 tokens

#### CBN-adviezen

- Een advies behandelt één concept — het is zinvol als geheel
- Indexeer als **één chunk** als het advies ≤ 40.000 chars (≈ 8.000 tokens, past in bge-m3 window). 403/436 adviezen vallen binnen deze grens (~93%).
- Adviezen > 40.000 chars: split op `##`-secties; elke sectie krijgt de adviestitel als breadcrumb-prefix met sectie-naam erachter
- Bij retrieval: geen context-uitbreiding (de chunk *is* het advies of een betekenisvolle sectie ervan)

#### ITAA-normen

- Per sectie chunken (zelfde principe als wetteksten)
- Bij retrieval: ±1 omliggende sectie

#### Praktijkgidzen

Praktijkgidzen hebben **geen `## Art.`-headings** (fiscaal-memento gebruikt `## HOOFDSTUK X`/`### N.`; toelichting-PB gebruikt `## VAK I-XIII`/`### A./B./C.`). De artikel-strict splitser (`split_wettekst_v2`) levert daardoor 0 chunks.

**Pragmatische graceful fallback**: in `index_wetteksten` wordt automatisch teruggevallen op `split_generic_headings` als `split_wettekst_v2` 0 chunks oplevert. De praktijkgids krijgt dan een minimaal path (`[wet, sectie]`) en breadcrumb `[wet-naam]` of `[wet-naam → heading]`.

Een eigen, op heading-structuur afgestemde strategie blijft een **TODO** voor later (zie open vragen). De fallback is goed genoeg voor recall.

#### TDKs / programmaonderdelen

- Per kenniselement + doelstelling (zoals in v1)
- Breadcrumb: `[<PO-naam> — <kenniselement>]`

#### Concept records (concepts-collection)

- Per veld van een node, zoals in v1
- Edges meedragen als metadata zodat retrieval een sub-graph teruggeeft (ADR-009)

### 5. Buurchunks-uitbreiding

`chunk_index ± n_neighbors` op de wetteksten-collection. Default `n_neighbors=2`. Vervalt voor andere brontypes.

`prev_chunk_id` en `next_chunk_id` worden **niet** als metadata-velden opgeslagen; ze zijn afgeleid uit `chunk_index ± delta` en het `bestand`-veld. Dit is een wijziging t.o.v. v1 — de daar genoemde velden bestonden in de tekst maar niet in de implementatie, en zijn niet nodig.

### 6. Hard maximum chunk-grootte

Bge-m3 (zie ADR-001) heeft een 8.192-token context-window. Tekst boven die grens wordt silently getruncated → informatie gaat verloren bij embedding.

Bij testing op WBTW bleek dat **enkele artikelen** die grens overschrijden:
- Art. 44 WBTW: ~26K chars / ~6.500 tok — genuine groot artikel met veel BTW-vrijstellingsparagrafen, past nét binnen window
- Art. 109 WBTW: ~58K chars — gerommeld door ETL-fout (Bijlage A en B aan het einde van het wetboek zijn aan het laatste artikel geplakt; zie open vragen)

**Regel**: chunks groter dan **24.000 chars** (~6.000 tokens, met marge) worden bij chunking gesplitst op **alinea-grenzen** (`\n\n`). Elke fragment krijgt `chunk_index = N.k` (bv. 47.1, 47.2) en een `__partN`-suffix in `id`. De path-array en breadcrumb blijven identiek (zelfde artikel, zelfde context).

Pseudocode:
```
if len(chunk_text) > MAX_CHUNK_CHARS:
    fragments = split_on_paragraphs(chunk_text, MAX_CHUNK_CHARS)
    yield each fragment as separate chunk with same path, suffixed id
else:
    yield chunk
```

Lossere alternatief (split op woordgrens met overlap) is fallback als één alinea zelf > MAX_CHUNK_CHARS is.

Bij retrieval: fragments van hetzelfde artikel zitten naast elkaar in `chunk_index`, dus context-uitbreiding (`±2`) trekt vanzelfsprekend de buur-fragmenten erbij. De gebruiker ziet effectief het hele artikel.

## Gevolgen

- **`tools/rag/rag_index.py`**:
  - `split_markdown_into_chunks` aanpassen: splitsen op `_is_article_heading()` (bestaat al, niet gebruikt), sub-headings inline laten
  - Nieuwe helper `_build_breadcrumb_prefix(fm, path)` voor de namen-prefix
  - Nieuwe helper `_build_path(fm, structurele_stack)` die de gestructureerde array opbouwt tijdens chunking
  - Per brontype-indexer: breadcrumb prependen, `path` als JSON-string in metadata
  - Verwijder `parent_section` overal
- **`tools/lib/retrieval.py`** (`_expand_wetteksten_context`): blijft werken, `chunk_index`-mechanisme is ongewijzigd
- **Citatie-rendering** in tutor: nieuwe helper die `path`-array → menselijk leesbare citatie omzet
- **ChromaDB rebuild**: vereist na implementatie. Oude collection-UUIDs in `data/chroma_db/` opschonen (zie ADR-010)
- **Keywords (ADR-004)**: keywords zijn per artikel-heading; volgorde-afhankelijkheid expliciet — eerst chunken, dan keywords genereren, dan indexeren

## Open vragen

- **Praktijkgidzen-specifieke strategie** — fallback via `split_generic_headings` werkt, maar respecteert de hoofdstuk-/vak-structuur niet als pad in metadata. Een eigen strategie (HOOFDSTUK → genummerde subsecties als pad) zou de retrieval scherper maken. Niet kritiek; de fallback levert recall.
- **Disambiguatie van Art. 1 in 87 wetten** — breadcrumb met wet-naam lost dit op voor de embedding, maar bij citaten naar "art. 5" zonder context is heuristiek nodig (zelfde wet tenzij anders aangegeven). Niet hier opgelost; concept-extractor zal dit moeten hanteren (ADR-009 stap 4).
- **Adviezen-titel uit H1**: bij sommige adviezen plakt de eerste paragraaf aan het H1 wegens ontbrekende lege regel in de markdown. De breadcrumb wordt hard-capped op 80 chars op woordgrens — niet perfect maar functioneel. ETL-detail; geen blocker.

## Opgeloste issues (mei 2026)

- ✅ Multi-line structurele headings in WIB92/WBTW: ETL-pipeline merget heading-vervolg op de volgende regel.
- ✅ Bijlages aan einde van wet (WBTW Bijlage A/B): ETL-pipeline geeft ze nu eigen `##`-heading.
