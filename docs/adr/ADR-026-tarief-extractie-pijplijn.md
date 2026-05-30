# ADR-026 — Tarief-extractie pijplijn

**Status**: Accepted (2026-05-30)
**Gerelateerd**: [ADR-019](ADR-019-records-api.md) (analoog records-API-patroon voor concepten), [ADR-037](ADR-037-leerstuk-vierde-leerlaag.md) (leerstuk-aanleiding voor tarief-records)

---

## Context

Het ITAA-bekwaamheidsexamen verwijst voortdurend naar cijfers — drempels groottecriteria, vennootschapsbelasting-tarief, voorafbetalings-percentages, indexcoëfficiënten, btw-drempels. Bij het examen heeft de stagiair het **Cijferzakboekje van het ITAA** als naslagwerk. Het studiemateriaal (leerstukken, concept-fiches, themafiches, minicursussen) moet daarnaar wijzen — niet zelf hard-coderen — om twee redenen:

1. **Actualiteit**: cijfers veranderen jaarlijks (indexatie, wetswijzigingen). Hardcoded cijfers in lopende tekst raken stil obsoleet.
2. **Single source of truth**: bij examen-vragen telt wat in het Cijferzakboekje staat. Studiemateriaal moet daar zonder wrijving naar kunnen wikilinken.

Sparring ADR-037 maakte het probleem concreet: stagiair raakt verward bij hardcoded "~42,5 mln" in een leerstuk — actueel of niet? Een leerstuk hoort op rechte wijze naar het Cijferzakboekje te kunnen wijzen.

**Schaal-orde**: 80-130 leerstukken × ~2-5 tarief-referenties = mogelijk 200-600 verwijzingen, naar geschat 30-80 unieke tarief-tabellen.

## Beslissing

Voeg een **vierde records-laag** toe: tarief-records. Parallel aan concept-records (ADR-019) en tarieven-records hebben hun eigen schema, API, MCP-server en render-pad.

### Layer-architectuur

| Aspect | Concept-records (ADR-019) | Tarief-records (ADR-026) |
|---|---|---|
| Atoom | Eén domein-concept | Eén samenhangende cijfer-tabel |
| Disk-pad | `data/concepten/records/<id>.json` | `data/tarieven/records/<id>.json` |
| Render | `content/concepten/<id>.md` (leeslaag voor stagiair) | **Geen content/-render** — pure data-laag |
| MCP-server | `certificaid-rag` (extractie/mcp_server) | `certificaid-tarieven` (tarieven/mcp_server) |
| RAG-parity | Verplicht (ChromaDB-collection `concepten`) | **Niet** — disk is enige bron-van-waarheid |
| Daemon-afhankelijkheid | Ja (bge-m3 + ChromaDB) | **Nee** — text-match op title/wetsbasis |
| Schrijf-API | `tools.lib.records_api` | `tools.lib.tarieven_api` (geen render) |

**Waarom geen RAG-parity voor tarieven?** Tarief-records zijn klein (~30-80 records), tabellaire structuur, ze leven van exacte cijfers en wetsverwijzingen — niet van semantische gelijkenis. Text-match op `titel`, `wetsbasis` en `categorie` heeft prima recall voor deze schaal. Embeddings toevoegen zou een tweede ChromaDB-collection + daemon-koppeling vergen zonder duidelijke winst. Bij groeiscenario (~300+ records) kan dit herzien worden.

### Record-schema (v1.0)

Minimaal-noodzakelijk schema voor versie 1. Volledig schema: [`data/tarieven/schema.json`](../../data/tarieven/schema.json).

```json
{
  "id": "drempels-groep-beperkte-omvang",
  "schema_version": "1.0",
  "titel": "Drempels groep van beperkte omvang",
  "categorie": "groottecriteria",
  "wetsbasis": [{"bron": "WVV", "artikel": "1:26 § 1"}],
  "geldigheidsperiode": {
    "vanaf_boekjaar": 2024,
    "tot_boekjaar": null,
    "wijziging_door": "Wet 28 maart 2024 (omzetting EU-richtlijn 2023/2775)"
  },
  "samenvatting": "Een groep is van beperkte omvang als ze op geconsolideerde basis niet meer dan één van drie criteria overschrijdt (werknemers · omzet · balanstotaal). Tweejaars-regel (art. 1:26 § 2 alinea 2).",
  "criteria": [
    {"naam": "Jaargemiddelde werknemers", "waarde": 250, "eenheid": "personen"},
    {"naam": "Jaaromzet (excl. btw)", "waarde": 42500000, "eenheid": "EUR"},
    {"naam": "Balanstotaal", "waarde": 21250000, "eenheid": "EUR"}
  ],
  "bron": {
    "primair": "CBN-advies 2024/07 §Verhoging drempelwaarden",
    "wettekst": "WVV art. 1:26 § 1",
    "cijferzakboekje_pagina": null,
    "verified_via": "RAG-zoek_bronnen, bedragen woordelijk bevestigd"
  },
  "confidence": "⚖️",
  "tags": ["consolidatie", "wvv", "groottecriteria"],
  "metadata": {
    "created_at": "2026-05-30",
    "trusted": true,
    "trusted_at": "2026-05-30"
  }
}
```

### Granulariteit

> **Eén record per samenhangende cijfer-tabel — niet per cijfer.**

`drempels-groep-beperkte-omvang` = één record met drie criteria. Niet drie records (werknemers/omzet/balanstotaal apart), want het didactische geheel ("meer dan één criterium overschreden") raakt zoek. Analoog aan ADR-030 voor concepten.

Sub-tabellen die *altijd samen* gelezen worden = één record (bv. PB-tariefschijven 2026 met 4 schijven). Sub-tabellen die los betekenis hebben (bv. drempels-kleine-vennootschap vs. drempels-groep-beperkte-omvang vs. drempels-microvennootschap) = aparte records ook al staan ze op één Cijferzakboekje-pagina.

### Extract-flow (vision via Sonnet-subagent)

Conform regel 3 (geen Claude API in build-pipeline) gebeurt vision-extractie via **Claude Code subagents** met directe Read-acces op de PNG's:

1. **Identificeer trigger-pagina's**: welke `Cijfers-Tarieven-2026_p0XX.png` bevat tabel X? Browse zoekt of indexbron raadplegen.
2. **Sonnet-extract-subagent** (prompt: [`prompts/tarief-extractie-v1.md`](../../prompts/tarief-extractie-v1.md)) leest PNG, kruist met RAG (`zoek_bronnen` voor wettekst/CBN-bevestiging), schrijft draft-record via `tarieven_api.save_record`.
3. **Sonnet-verify-subagent** (prompt: [`prompts/tarief-verify-v1.md`](../../prompts/tarief-verify-v1.md)) leest geschreven record, checkt elk cijfer tegen ten minste één RAG-bron, markeert trusted via `tarieven_api.mark_trusted` of stuurt terug naar extract met bevindingen.

Voor records waarvan de bedragen al volledig RAG-traceerbaar zijn (CBN-advies + wettekst-MvT bevatten exact dezelfde cijfers als het Cijferzakboekje), mag de PNG-stap worden overgeslagen — `cijferzakboekje_pagina` blijft dan `null` en `bron.verified_via` documenteert dat. Dit is de **POC-route voor de drempel-records van art. 1:24/1:25/1:26**.

### Chunker

`tools/tarieven/chunk_pdf.py` — dunne wrapper rond `pdftoppm` (poppler). Eén commando:

```bash
python3 -m tools.tarieven.chunk_pdf --default
```

Chunked Cijferzakboekje 2026 (196 pagina's) naar `data/tarieven/pages/p001.png` … `p196.png`. PDF-bron: `resources/raw/wetteksten/Cijfers-Tarieven-2026.pdf`. TOC-extract via `pypdf` outline geeft per-entry pagina-locatie voor scope-bepaling van extract-subagents.

### MCP-server `certificaid-tarieven`

Vier tools (text-match v1, geen embeddings):

| Tool | Doel |
|---|---|
| `lijst_tabellen(categorie?)` | Alle records, optioneel gefilterd op categorie. Compacte representatie. |
| `lees_tabel(record_id)` | Volledig record on-demand. |
| `zoek_tabellen(query, top_k?)` | Text-match op titel/wetsbasis/tags/samenvatting. |
| `query_tabel(record_id, vraag)` | Eenvoudige veld-extractie (bv. "wat is de werknemers-drempel?" → return numerieke waarde). v1: alleen `lees_tabel` + agent-interpretatie. |

Implementatie: [`tools/tarieven/mcp_server/server.py`](../../tools/tarieven/mcp_server/server.py).

### Geen content/-render — tarief-records zijn data-laag

Tarief-records worden **niet** naar Quartz-`content/` geschreven. Ze zijn pure data voor:
- LLM-tutors die vraag-beantwoording doen (lopen tegen MCP-server `certificaid-tarieven`)
- Leerstuk-auteurs die actualiteit van een cijfer willen valideren tijdens schrijven
- Verify-pass-agents die claims in leerstukken kruisen

De leerlaag voor stagiairs blijft het Cijferzakboekje zelf (papier of PDF) — daar gaan ze toch heen tijdens het examen. Het wikilinken van leerstukken naar tarief-record-fiches voegt geen leeswaarde toe en zou content-onderhoud opzadelen met data-laag-mutaties.

Slug-discipline blijft: prefix `drempels-`, `tarief-`, `voorafbetaling-`, `indexcoeff-` waar dat helpt om uniek te blijven binnen de records-folder.

### Geen RAG-collection

In tegenstelling tot concept-records (die naar de `concepten` ChromaDB-collection schrijven via een daemon) hebben tarief-records geen RAG-parity. MCP-server leest disk direct. Dit reduceert de operationele oppervlakte significant: geen embedding-stap, geen daemon-cold-start, geen ghost-detectie. De prijs is dat `zoek_tabellen` text-match is, niet semantisch — voor 30-80 records is dat acceptabel.

## Implementatie

| Stap | Artefact | Status |
|---|---|---|
| 1 | `data/tarieven/schema.json` (JSON-schema v1.0) | Deze sessie |
| 2 | `tools/lib/tarieven_api.py` (`save_record`, `mark_trusted`, `audit_parity`, render) | Deze sessie |
| 3 | `tools/tarieven/mcp_server/server.py` (4 tools) | Deze sessie |
| 4 | `prompts/tarief-extractie-v1.md` + `prompts/tarief-verify-v1.md` | Deze sessie |
| 5 | POC-records: drempels art. 1:24/1:25/1:26 | Deze sessie (handmatig, RAG-bron) |
| 6 | Leerstuk `wie-moet-consolideren` wikilinkt naar drempel-record | Deze sessie |
| 7 | Chunker `tools/tarieven/chunk_pdf.py` (pdftoppm-wrapper) | Geleverd (2026-05-30, na PDF beschikbaar werd) |
| 8 | Aanvullende records (VenB-tarief, PB-schijven, voorafbetalingen, btw, OV, VAA, ...) | Batch-extract via parallel Sonnet-subagents (deze sessie / volgende sessie) |

## Wat dit superseert / amendeert

| Artefact | Status na ADR-026 | Reden |
|---|---|---|
| CLAUDE.md regels 46/55/56 | **Bijgewerkt** | Phantom-verwijzingen naar niet-bestaande tooling vervangen door actuele paden + chunker-uitstel-noot |
| ADR-037 open punten | **Aanleiding-vraag gesloten** | Tarief-record-laag bestaat; leerstuk-koppeling actief voor drempels-cluster |

## Veranderlog

- **2026-05-30** — ADR opgesteld. Aanleiding: ADR-037-sparring (stagiair verwart hardcoded drempel met actualiteit). Initiële scope: tarief-records-laag bouwen (schema + API + MCP-server + prompts) + 3 drempel-records als POC + leerstuk-koppeling. Vision-pipeline en chunker uitgesteld tot een tweede tarief-cluster (bv. VenB-tarieven van p070+) zinvol PNG-vision aanroept.
- **2026-05-30 (later)** — PDF beschikbaar gemaakt in `resources/raw/wetteksten/Cijfers-Tarieven-2026.pdf`. Chunker geleverd (`tools/tarieven/chunk_pdf.py`). 79 nieuwe records geëxtraheerd via 8 parallel Sonnet-subagents (totaal 82). Verify-pass blijft open punt.
- **2026-05-30 (nog later)** — Render naar `content/tarieven/` geschrapt: tarief-records blijven pure data-laag. Leeslaag voor stagiairs is het Cijferzakboekje zelf; LLM-tutors raadplegen via MCP-server. `tarieven_api.save_record` doet geen markdown-render meer; `render_markdown` bewaard als ad-hoc preview-helper. Leerstuk-wikilinks naar `[[tarieven/...]]` teruggedraaid in `wie-moet-consolideren.md`.
