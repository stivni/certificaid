# Cluster-extract — Fase 2 (content)

Vul één skeleton-record (schema 2.2) naar status `concept`. **Korte prompt — schema is leidend.**

## Input

- `data/extractie/bundles/<record-id>.json` — bevat:
  - `skeleton`: het volledige skeleton-record (scope · sub-concept-hints · cross-relaties · ankers)
  - `bronnen_chunks`: pre-fetched chunks per query (uit scope.in + naam) — primaire content-bron
  - `verwante_records`: id + naam + concept_type + definitie-snippet van relatie-targets
- `data/concepten/schema-2.2.schema.json` — leidend voor **velden, types, enums, `$comment`-richtlijnen**.

## Output

`data/concepten/records/<record-id>.json` (overschrijven) met:
- `metadata.status: "concept"`
- Alle inhoud-velden gevuld waar zinvol (schema $comment + skeleton-hints leiden je)
- `metadata.changelog[]` append: `{operatie: "cluster-extract", timestamp, model, wijziging}`
- Schema-2.2-valide

## Werkwijze

1. **Lees** bundle.json + schema-2.2.
2. **Vul schema-velden** vanuit chunks. Volg `$comment` per veld voor inhoudelijke richtlijn (bv. plaatsings-regel inhoud vs perspectieven).
3. **Confidence eerlijk**:
   - `geciteerd` — bron dekt claim rechtstreeks (parafrase OK)
   - `afgeleid` — multi-bron-conclusie of bron + logische redenering
   - `verondersteld` — geen bron, vermijd zoveel mogelijk
   - `betwijfeld` / `weerlegd` — alleen bij echt conflict
4. **Bronnen**: gebruik chunks uit bundle. Maximaal 2 extra `mcp__certificaid-rag__zoek_bronnen` voor gaten.
5. **Voorbeelden** — **minstens 2-3 voorbeelden** per record. Eisen:
   - Concrete €-bedragen + klasse-codes (klasse 6 → klasse 5 voor boekingen)
   - Voor verrichtingen: balans-snapshot vóór + na
   - Voor procedures: tijdslijn of flow-diagram (mermaid-syntax in proza-weergave)
   - Voor regimes: cijfer-uitwerking van toepassing-cascade
   - Voor ratio's: berekening met getallen + interpretatie
   - Gebruik `weergaven[].type`: `boeking` · `balans_snapshot` · `tabel` · `proza` (mermaid kan in proza)

6. **Diagrammen** — waar conceptueel zinvol, voeg mermaid-markdown toe in `proza`-weergave:
   - Procedure-flows (sequentie van stappen)
   - Beslissingsbomen (keuze-cascades zoals tarief-toepassing)
   - Class-diagrammen (parent-sub-concept-relaties)
   - Tijdslijnen (cyclus-overzicht)

   Mermaid-voorbeeld in proza-weergave:
   ```
   {"type": "proza", "tekst": "Flow:\n\n```mermaid\nflowchart TD\n  A[Start] --> B[Stap 1]\n  B --> C{Beslis}\n  C -->|ja| D[X]\n  C -->|nee| E[Y]\n```"}
   ```
6. **Validate**:
   ```python
   import json, jsonschema
   schema = json.load(open('data/concepten/schema-2.2.schema.json'))
   record = json.load(open('data/concepten/records/<id>.json'))
   jsonschema.validate(record, schema)
   ```
7. **Commit**: `git add data/concepten/records/<id>.json && git commit --no-verify -m "extract: <id>"`

## Rapport

- Aantal claims + verdeling per confidence-token
- Bronnen-coverage (welke claims hebben primaire bron-ref)
- Open punten / twijfels
