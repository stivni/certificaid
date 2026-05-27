# Operatie: `relaties_aanvullen`

Valideer en verrijk top-level `relaties[]` — graph-edges naar andere records. Suggesties uit `beschrijven` worden nu gecheckt tegen de records-index en eventueel aangevuld via MCP-discovery. Toepassen na `beschrijven`. Confidence: `verondersteld` of `betwijfeld`; `claims_checken` upgradet wettelijke relaties later.

Voor structuur, veldnamen, enums en shape-details: zie `$comment`/`description` per `$def` in `data/concepten/schema-2.1.schema.json`. Deze prompt geeft alleen workflow + discipline die schema niet kan afdwingen.

**Input**: `data/concepten/records/<fiche-id>.json` — direct-flow, geen /tmp.
**Output**: zelfde bestand overschrijven.
**Tempo**: 1-3 min. RAG: compacte-index + MCP `check_record_bestaat` + `zoek_concepten`.

---

## Voorbeeld

Referentie-record dat de uitvoer van deze operatie illustreert:
`data/concepten/examples/obligatielening-04-relaties_aanvullen.json` — een instrument-record na exact deze operatie. Gebruik het als shape-referentie voor de top-level `relaties[]`, met name hoe `vergelijkbaar_met`-relaties uitgewerkt zijn (`gelijkenissen`, `verschillen`, `verwarring_risico`).

---

## Confidence-discipline

| Token | Symbool | Toegestaan |
|---|---|---|
| `geciteerd` | 📖 | nee — `claims_checken` upgradet wettelijke `vereist`-relaties |
| `afgeleid` | 🔗 | nee |
| `verondersteld` | 🤖 | ja |
| `betwijfeld` | ❓ | ja |
| `weerlegd` | ❌ | nee |

**HARDE REGEL**: geen relatie schrijven zonder bestaand target. Beter rapporteren als gap dan ongeldig target invullen.

---

## Scope-respect (ADR-033)

Lees `metadata.scope` indien aanwezig.

- **`scope.out[]`-topics signaleren relatie-kandidaten**: elke `scope.out`-entry verwijst naar een record-id ("Voor X zie `<record-id>`"). Voeg een relatie toe naar dat record (`soort` afhankelijk van semantiek — `cross-link` of `verder-detail-in` als die enum-waarden bestaan, anders dichtste alternatief). Zo wordt `scope.out` materieel afgedwongen via de graph.
- **`scope.in[]`-topics check** als plausibility: relaties moeten consistent zijn met wat het record behandelt — een relatie naar een topic dat niet in `scope.in` raakt is een smell.

Geen `scope`-veld? → werk volgens normale relaties-logica.

---

## Target-validatie

Voor elke kandidaat-relatie:
1. Zoek ID in `data/concepten/records-index.compact.txt` (snelst voor exact match).
2. Bij twijfel: MCP `check_record_bestaat(record_id)`.
3. Voor discovery van `vergelijkbaar_met`/`valt_onder`/vergelijkbare types: MCP `zoek_concepten(query, top_k=5)` → valideer gevonden IDs daarna met `check_record_bestaat`.

Als target niet bestaat: **niet schrijven** — log als gap in eindrapport.

---

## `vergelijkbaar_met` — rijk uitwerken

```json
{
  "type": "vergelijkbaar_met",
  "target": "<record-id>",
  "gelijkenissen": ["...", "..."],
  "verschillen": ["...", "..."],
  "verwarring_risico": "...",
  "render_hint": "als_keuze",
  "grondslag": {"confidence": "verondersteld", "bronnen": [...]}
}
```

- 2-5 `gelijkenissen` + 2-5 `verschillen`.
- `verwarring_risico` invullen waar studenten/practitioners de twee verwarren.
- `render_hint`: `als_keuze` (gelijkwaardige alternatieven) · `als_glossarium` (begripsuitleg) · `als_waarschuwing` (verwarring-gevaar).

---

## Werkwijze

1. Lees `data/concepten/records/<fiche-id>.json`.
2. Lees `data/concepten/schema-2.1.schema.json` `$defs/relatie` voor veldnamen en relatie_type-enum.
3. Bekijk bestaande `relaties[]`-suggesties uit eerdere operaties.
4. Lees `data/concepten/records-index.compact.txt`.
5. Per kandidaat-relatie: valideer target, schrijf of log als gap.
6. Voor `vergelijkbaar_met`: vul `gelijkenissen` + `verschillen` + `verwarring_risico` rijk.
7. Self-check (zie CRITICAL hieronder).
8. Schrijf record naar `data/concepten/records/<fiche-id>.json`.
9. Voeg changelog-entry toe: `{"operatie": "relaties_aanvullen", "timestamp": "<ISO>", "model": "<jouw-model>"}`.

---

## CRITICAL self-checks

- **R2** — `target`-veldnaam is altijd `target`, nooit `naar`/`naar_concept`/`to`.
- `relaties[]` staat op top-level van het record, NIET binnen `inhoud`.
- Auto-afgeleiden (omgekeerden zoals `bevat` ↔ `valt_onder`, `triggert` ↔ `getriggerd_door`) NIET schrijven — render bouwt deze automatisch.
- Geen `geciteerd`/`afgeleid` — ook niet voor wettelijke `vereist`-relaties.

---

## Eindrapport

- Aantal relaties per type.
- Ontbrekende targets als gap-suggesties voor latere wave (per concept-naam wat ontbreekt).
- Confidence-mix.
