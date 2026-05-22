# Operatie: `relaties_aanvullen` (run-4)

Schema-versie: 2.1 v1.5 (zie `data/concepten/schema-2.1.schema.json` — `$comment`/`description` per `$def` is bron-van-zelfsturing).

**Doel**: vul top-level `relaties[]` — graph-edges naar andere records.

**Input**: `/tmp/<fiche-id>.json` (na voorgaande operaties). `beschrijven` plaatste mogelijk suggesties — die nu valideren + verrijken.

**Output**: definitieve `relaties[]` (top-level, NIET binnen `inhoud`).

---

## Confidence-tokens (overzicht)

| Token | Symbool | Wanneer toegestaan in deze operatie |
|---|---|---|
| `geciteerd` | 📖 | ❌ — alleen `claims_checken` |
| `afgeleid` | 🔗 | ❌ — alleen `claims_checken` |
| `verondersteld` | 🤖 | ✅ |
| `betwijfeld` | ❓ | ✅ |
| `weerlegd` | ❌ | ❌ |

Elke relatie krijgt `grondslag.confidence = "verondersteld"` met `ai_model`-bron. `claims_checken` upgradet waar primaire bron gevonden (bv. wettelijke `vereist`-relatie).

---

## `relatie_type` enum (14 — onveranderd uit v1.4)

**Structureel**
- `bevat` — parent → child (alleen voor kader of abstract parent)
- `valt_onder` — child → parent

**Causaal / conditioneel**
- `triggert` — A zet B in werking
- `beinvloed_door` — A wordt gemodificeerd door B
- `vereist` — A heeft B nodig om te bestaan
- `is_uitzondering_op` — A is uitzondering op B (algemene regel)
- `niet_combineerbaar_met` — A en B sluiten elkaar uit

**Comparatief** (rijk)
- `vergelijkbaar_met` — met `gelijkenissen[]`, `verschillen[]`, `verwarring_risico`, `render_hint`

**Actor**
- `uitgevoerd_door` · `gecontroleerd_door` · `gepubliceerd_via` · `goedgekeurd_door` · `gedocumenteerd_in`

**Bijzonder**
- `alternatief_referentiestelsel` (bv. BE-GAAP ↔ IFRS)

**Auto-derive omgekeerden** (NIET schrijven): render bouwt `getriggerd_door`, `beinvloedt`, `voorwaarde_voor`, `heeft_uitzondering`, `bevat` ↔ `valt_onder` automatisch.

---

## v1.5-structuur

```json
{
  "type": "<relatie_type>",
  "target": "canonical-ref",            // record-id of record-id#element-id
  "grondslag?": {"confidence": "verondersteld", "bronnen": [...]},
  "toelichting?": "string of tekst-object",
  // alleen voor type = "vergelijkbaar_met":
  "gelijkenissen?": [...], "verschillen?": [...], "verwarring_risico?": "...", "render_hint?": "..."
}
```

**Plaats**: `relaties[]` staat op **top-level** van het record (samen met `id`, `naam`, `concept_type`, `metadata`, `inhoud`). **NIET binnen `inhoud`**.

Voor inline-relaties op een specifieke claim of element: gebruik `tekst.relaties[]` (binnen het `tekst`-blok zelf) — dat is een aparte aanvulling, niet de top-level array.

---

## Target-validatie (MCP + compacte index)

Voor elke relatie moet `target` bestaan in records. Twee opties:

1. **Pre-check via compacte index** (`data/concepten/records-index.compact.txt`): doorzoek IDs. Snelste.
2. **MCP `check_record_bestaat(record_id)`** voor twijfelgevallen.

Als target niet bestaat: **niet schrijven**. Log in eindrapport als "ontbrekend kader/regime" voor latere wave.

---

## `vergelijkbaar_met` discipline (rijk uitwerken)

```json
{
  "type": "vergelijkbaar_met",
  "target": "banklening-investeringskrediet",
  "gelijkenissen": ["beide schuldfinanciering lange termijn", "rentekost-aftrekbaar uitgever"],
  "verschillen": ["obligatie publiek toegankelijk", "banklening flexibeler vervroegde aflossing"],
  "verwarring_risico": "studenten verwarren obligatielening soms met achtergestelde lening",
  "render_hint": "als_keuze",
  "grondslag": {"confidence": "verondersteld", "bronnen": [...]}
}
```

- 2-5 `gelijkenissen` + 2-5 `verschillen`.
- `verwarring_risico` waar studenten/practitioners de twee verwarren.
- `render_hint` opties: `als_keuze` (vergelijkbare alternatieven) · `als_glossarium` (begrip-uitleg) · `als_waarschuwing` (verwarring-gevaar).

---

## Discipline

- **Suggesties uit `beschrijven`** valideren tegen records-index; behouden of weggooien.
- **Geen relatie zonder bestaand target.** Beter rapporteren in eindrapport (= gap voor latere wave).
- **Geen `geciteerd`/`afgeleid`** — `claims_checken`-werk (bv. wettelijke `vereist`).
- **`tekst`** (niet `text`); **`ankers`** in metadata (niet `linked_anchors`) — niet hier wijzigen.

---

## Werkwijze

1. Lees `/tmp/<fiche-id>.json` (na voorgaande operaties).
2. Bekijk eventuele suggesties in `relaties[]` van eerdere operatie.
3. Lees `data/concepten/records-index.compact.txt` om bestaande targets te vinden.
4. Voor elke kandidaat-relatie:
   - Target bestaat? → schrijf.
   - Target hoort bij `vergelijkbaar_met`? → vul `gelijkenissen` + `verschillen` rijk.
5. Voor `vergelijkbaar_met`: 2-5 gelijkenissen + 2-5 verschillen + `verwarring_risico` indien relevant.
6. Schrijf record terug naar `/tmp/<fiche-id>.json`.
7. Update `metadata.changelog`:
   ```json
   {"operatie": "relaties_aanvullen", "timestamp": "<ISO>", "model": "<jouw-model>"}
   ```

**Tempo**: 1-3 min. Compacte-index-lookup; geen RAG.

---

## Eindrapport

- Aantal relaties per type.
- Ontbrekende targets (= gap-suggesties voor latere wave).
- Confidence-mix.
