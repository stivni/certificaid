# Cluster-verbeter — Pass 3 (verwerk verify-feedback)

Verwerk verify-rapport per record + breng kwaliteits-verbeteringen aan.

## Input

- `data/concepten/records/<id>.json` (status: `concept` na Pass 1)
- `data/extractie/verify-reports/<id>.md` (feedback uit Pass 2)
- `data/extractie/bundles/<id>.json` (bron-chunks indien extra info nodig)
- `data/concepten/schema-2.2.schema.json`

## Werkwijze

Per record:
1. Lees verify-rapport — focus op `critical` + `major` issues
2. Lees huidig record
3. Voor elke verbeter-actie:
   - **Voorbeelden ontbreken** → voeg toe (concrete cijfers + boekingen)
   - **Diagrammen ontbreken** → voeg mermaid in proza-weergave
   - **Bron-citaat fout** → corrigeer ref of degradeer confidence
   - **Scope.in topic niet gedekt** → vul in inhoud
   - **Cross-relatie target onbestaand** → schrap of vervang
   - **Geldigheid ontbreekt voor regime** → vul status + sinds/wettelijke_basis
4. Schema 2.2 valideren
5. `metadata.changelog[]` append: `{operatie: "cluster-verbeter", timestamp, wijziging: "Verify-feedback verwerkt: ..."}`
6. Commit per cluster

## Output

Overschrijf `data/concepten/records/<id>.json` met verbeterde versie. Status blijft `concept` (escalatie naar `gevalideerd` is mens-actie).

## Rapport

- Aantal records verbeterd
- Issues verwerkt per severity
- Resterende minor-issues (niet kritisch)
- Schema-validatie 100%
