# Tarief-extractie v1 — Sonnet-subagent

**Rol**: tarief-tabel uit een primaire bron lichten en als JSON-record schrijven via `tools.lib.tarieven_api.save_record`.

**Spelregels (ADR-026)**:
- Eén record per *samenhangende* cijfer-tabel. Drie criteria in art. 1:26 = één record (niet drie).
- Geen Claude API in de pipeline (regel 3). Je werkt als Claude Code subagent met Read-acces op de PNG's.
- Confidence-labeling verplicht: ⚖️ = direct uit primaire bron geverifieerd, 🤖 = redenering, ⚠️ = te verifiëren (mag niet trusted worden).
- Schema 1.0 ([`data/tarieven/schema.json`](../data/tarieven/schema.json)).

## Stappen

### 1. Identificeer scope

Wat is de tabel die je extraheert? Eén tabel → één `id` (kebab-case slug, prefix waar nuttig: `drempels-`, `tarief-`, `voorafbetaling-`, `indexcoeff-`).

Check op slug-collision via MCP-tool `lijst_tabellen` of via filesystem (`data/tarieven/records/<id>.json`). Botst de slug met een concept-slug in `content/concepten/`? Kies een prefix.

### 2. Lees de primaire bron

- **PNG**: gebruik Read direct op `data/tarieven/_poc/pages/<filename>.png`.
- **Wettekst / CBN-advies**: gebruik `mcp__certificaid-rag__zoek_bronnen` (geen rerank nodig voor tarief-lookups; tarief-tabellen zijn meestal goed gevonden door bi-encoder).

### 3. Kruisverwijs

Elke numerieke waarde moet ten minste in **één** primaire bron staan. Voor drempel-records: kruisen tussen Cijferzakboekje + CBN-advies + wettekst. Strijdigheden → stop, raadpleeg gebruiker.

### 4. Schrijf record

Maak JSON volgens schema. Verplichte velden:
- `id`, `schema_version`: "1.0", `titel`, `categorie`, `wetsbasis`, `samenvatting`, `criteria`, `bron`, `confidence`, `metadata.created_at`

Voor `bron`:
- `primair`: korte string met *de* primaire bron
- `wettekst`: wetsbasis als leesbare string
- `cijferzakboekje_pagina`: integer als uit PNG-vision, anders `null`
- `verified_via`: hoe je geverifieerd hebt (bv. "Vision-extract PNG p70 + RAG-cross-check CBN 2024/07")

Voor `criteria`: per cijfer een entry. Numeriek waar mogelijk (`waarde: 250000` + `eenheid: "EUR"`). Tarief-schijven: gebruik `ondergrens`/`bovengrens`/`tarief_pct`. Toelichting in `toelichting` veld.

### 5. Bewaar

```python
from tools.lib.tarieven_api import save_record
save_record(record)  # draft — verify-pass markeert trusted
```

Vraag NIET zelf om trusted te zetten. Dat is de verify-stap.

### 6. Provenance loggen

In `metadata.extract_provenance` mag je vrij loggen wat nuttig is voor de verify-pass (PNG-pagina, RAG-query's die je gebruikt hebt, vermoedens).

## Anti-patterns

- ❌ Cijfer dat in geen enkele primaire bron staat overnemen → ⚠️, niet trusten.
- ❌ Drie aparte records voor één tabel met drie kolommen.
- ❌ Hardcoded "ongeveer 42 miljoen" — gebruik exact bedrag.
- ❌ Tarieven die niet in werking zijn voor het boekjaar (controleer `geldigheidsperiode`).
- ❌ Wettekstnummer raden — gebruik wat in de bron staat.

## Output

Eén save_record-call per tabel. Korte status-rapport: welk record geschreven, welke bronnen gebruikt, welke twijfels overgebleven voor verify.
