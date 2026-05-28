# Cluster-verify — Pass 2 kwaliteit-check

Review concept-records die uit Fase 2 (cluster-extract) komen. Identificeer gaten + foute claims. Output: feedback-rapport per record + lijst verbeter-acties.

## Input

- `data/concepten/records/<id>.json` (status: `concept` na Fase 2)
- `data/extractie/bundles/<id>.json` (bundle met chunks — om citaat-correctheid te checken)
- `data/concepten/schema-2.2.schema.json`

## Verify-checklist per record

### 1. Schema 2.2 valide
```python
import json, jsonschema
schema = json.load(open('data/concepten/schema-2.2.schema.json'))
record = json.load(open('data/concepten/records/<id>.json'))
jsonschema.validate(record, schema)
```

### 2. Volledigheid scope.in[] dekking
- Voor elke `metadata.scope.in[]`-string: wordt het topic effectief behandeld in `inhoud`?
- Gaten → flag

### 3. Voorbeelden-kwaliteit
- Minstens 2 voorbeelden? (verplicht voor regelingen/regimes/verrichtingen)
- Bevatten concrete €-bedragen?
- Klasse-codes voor boekingen?
- Balans-snapshot vóór/na waar verrichting?
- Tijdslijn/diagram voor procedures?

### 4. Bron-citaat-discipline
- Per claim met `confidence: "geciteerd"`: bron-ref is correct (artikel-nummer, advies-code)?
- Geen verzonnen wettekst-refs
- Voor primaire bronnen: `ref` veld verplicht
- AI-model-only claims: confidence wel `afgeleid` of `verondersteld`, niet `geciteerd`

### 5. Cross-relaties consistent
- Voor elke `relaties[].target`: bestaat het target-record?
- Voor `type: vergelijkbaar_met`: gelijkenissen + verschillen aanwezig?
- Geen circulaire valt_onder
- `grondslag` aanwezig

### 6. Sub-concepten en bouwstenen
- Subconcepten hebben eigen kern (definitie minimaal)
- Bouwstenen hebben `bouwsteen_type` uit enum
- Geen "subconcept" als bouwsteen_type

### 7. Accountant_perspectieven
- Minstens 1 perspectief per regeling/verrichting
- Rollen uit enum (boekhouder · auditor · fiscaal · adviseur · begeleider)
- Geen lege rollen-arrays

### 8. Geldigheid (voor regimes/regelingen)
- `inhoud.gebruikscontext.geldigheid` aanwezig?
- Status uit enum (in-voege · uitdovend · afgeschaft · historisch · ontwerp)
- Bij uitdovend/afgeschaft: `sinds`/`tot` + `wettelijke_basis`

### 9. Diagrammen waar zinvol
- Procedures: flow-diagram aanwezig (mermaid in proza-weergave)?
- Beslissings-cascades: beslisboom?

## Output-formaat per record

Schrijf naar `data/extractie/verify-reports/<id>.md`:

```markdown
# Verify-rapport: <id>

## Status
- Schema 2.2: ✓/✗
- Scope.in dekking: X/Y topics gedekt
- Voorbeelden: N (≥2 vereist)
- Bron-discipline: OK/issues
- Cross-relaties: OK/issues

## Issues
- [ ] Issue 1 (severity: critical/major/minor)
- [ ] Issue 2 (...)

## Verbeter-acties
- Voor elke critical/major issue: concrete verbeter-instructie voor Pass 3
```

## Werkwijze

Werk per cluster (input: lijst record-ids):
1. Per record: check de 9 checklists
2. Schrijf verify-rapport per record
3. Aggregatie-rapport per cluster (`data/extractie/verify-reports/_cluster-<naam>.md`)
4. Geen wijzigingen aan records — alleen rapporten

## Output-rapport aan einde

- Aantal records verified
- Verdeling severity (critical / major / minor / OK)
- Top 5 voorkomende issues (voor prompt-verfijning)
