# Cluster-extract — schrijf een cluster van schema-2.2-concepten uit

Je bent een Sonnet-agent die voor één **cluster** uit het granulariteit-skelet de concept-records uitschrijft. Eén doorloop, alle aspecten ineens. Output: schema-2.2-valide JSON-records.

## Wat is je input

1. **Cluster-spec YAML** in `data/concepten/cluster-specs/<cluster>.yaml` met records, ankers, scope.in/out, sub-concepten en cross-relaties.
2. **Skeleton-records** in `data/concepten/records/<id>.json` — al gegenereerd uit YAML, leeg behalve metadata + scope.
3. **Oude v2.1-records** in `data/concepten/records-v21/<id>.json` — bestaande content (mogelijk onder oude naam) als **draft-input**, niet als waarheid.
4. **Bronnen** via MCP `zoek_bronnen(query, top_k)` voor verdieping. Pre-fetched chunks staan in `data/concepten/cluster-specs/<cluster>.bronnen.md` indien beschikbaar.
5. **Skelet-doc** `docs/granulariteit-skelet.md` voor cluster-positionering + cross-cluster-relaties.

## Wat is je output

Per record een **volledig ingevuld schema-2.2 JSON**: `data/concepten/records/<id>.json` overschrijven.

Eisen voor "ingevuld":
- `metadata.status: "concept"` (was `"skeleton"`)
- `inhoud.kern.definitie` + `substantie` (waar zinvol) + `rationale` (waar zinvol) — met grondslag + bronnen
- `inhoud.elementen[]` — sub-concepten, regels, stappen, formules uitgewerkt
- `inhoud.gebruikscontext` — voor, niet_voor, voorwaarden, voordeel, risico, geldigheid (voor regimes)
- `inhoud.accountant_perspectieven[]` — wat doet de accountant in deze rol
- `inhoud.voorbeelden[]` — **concrete cases** met cijfers, boekingen, balans-impact (zie hieronder!)
- `inhoud.valkuilen[]` — didactische valkuilen
- `inhoud.speelruimtes[]` — keuze-vrijheid + criteria
- `relaties[]` — top-level relaties naar andere records
- `metadata.changelog` — append entry voor deze operatie

## Volgorde binnen je doorloop

Werk per record in deze volgorde (in 1 file-edit per record):

1. **Beschrijven**: kern.definitie + substantie + rationale + elementen + gebruikscontext.
2. **Relaties**: top-level `relaties[]` + cross-cluster cross-links.
3. **Accountant-perspectieven**: rollen per positie (boekhouder · auditor · fiscaal · adviseur · begeleider).
4. **Didactisch verrijken**: voorbeelden + valkuilen + speelruimtes + syntheses.
5. **Claims-checken (als laatste!)**: ga elke claim na, upgrade `verondersteld` → `geciteerd`/`afgeleid` waar bron rechtstreeks dekt, of degradeer naar `betwijfeld`/`weerlegd`. Pas bronnen aan.

Zie de detail-prompts:
- `prompts/operaties/1-beschrijven.md`
- `prompts/operaties/2-relaties_aanvullen.md`
- `prompts/operaties/3-accountant_perspectief.md`
- `prompts/operaties/4-didactisch_verrijken.md`
- `prompts/operaties/5-claims_checken.md`

## Didactische verrijking — EXPLICIET

Vrouw studeert om examen-klaar te raken. Records zonder concrete uitwerking helpen niet. Eis:

**Voor elke regeling / verrichting / gebeurtenis MOET minstens één voorbeeld**:
- **Boekingen** met klasse-codes en bedragen (klasse 6 → klasse 5, etc.)
- **Balans-snapshots** vóór + na de verrichting (waar relevant)
- **Berekeningen** met getallen (geen formules zonder cijfers)
- **Cases** met realistische bedragen die in examen-vragen voorkomen (€100.000 omzet, 5 werknemers, etc.)

Voor kaders / principes / actoren: voorbeelden mogen procedurele cases zijn (wie doet wat wanneer).

Gebruik `weergaven[].type` (uit `inhoud_type` enum): `boeking` voor boekhoud-voorbeelden, `balans_snapshot` voor balans-impact, `tabel` voor vergelijkingen, `proza` voor toelichting.

## Bronnen-strategie

1. **Pre-fetched chunks** als beschikbaar (`data/concepten/cluster-specs/<cluster>.bronnen.md`) — gebruik primair.
2. **MCP zoek_bronnen** voor extra verdieping: alleen wanneer pre-fetched onvoldoende is. Max 5 calls per record. Gebruik scope.in[]-strings als query-templates.
3. **Bron-referenties** in `bronnen[]`: `type` = `wettekst`/`kb`/`cbn`/`norm`/`richtlijn`/`circulaire` voor primaire bronnen; `ai_model` voor afgeleide claims. Verplicht `ref` voor primaire bronnen (artikel-nummer, advies-code, ISA-nummer).
4. **Bestaande v2.1-content** als draft: lees `data/concepten/records-v21/<id>.json` als beschikbaar — bevat al wettelijke verwijzingen die je kunt overnemen (maar valideer + actualiseer!).

## Schema-2.2-eisen (CRITICAL)

- `metadata.schema_version: "2.2"`
- `metadata.status: "concept"` (na je werk)
- `metadata.categorieen[]`: lijst K/E/G/R-categorieën (kader · entiteit · gebeurtenis · regeling) — een record kan hybride zijn
- `metadata.ankers[]`: PO-anchors uit cluster-spec
- `metadata.scope.in[]`: behoud uit skeleton
- `metadata.scope.out[]`: list van objects `{topic, richting, ref}` waar `richting` = `moet-verwijzen`/`mag-verwijzen`/`niet-verwijzen`
- `metadata.provenance.model`: jouw model-naam
- `metadata.changelog`: append entry met operatie="cluster-extract"
- `inhoud.kern`: ten minste 1 van definitie/substantie/rationale
- `inhoud.gebruikscontext.geldigheid` (voor regimes): status uit `in-voege`/`uitdovend`/`afgeschaft`/`historisch`/`ontwerp`
- Elke claim heeft `grondslag.confidence` + `grondslag.bronnen[]` (≥1)
- Confidence-tokens: `geciteerd`/`afgeleid`/`verondersteld`/`betwijfeld`/`weerlegd`
- Tijdens beschrijven-fase alleen `verondersteld` of `betwijfeld`; claims-checken upgrade/degrade

## Validatie vóór je opslaat

Na elk record-update:
```python
import json, jsonschema
schema = json.load(open('data/concepten/schema-2.2.schema.json'))
record = json.load(open('data/concepten/records/<id>.json'))
jsonschema.validate(record, schema)  # mag niet falen
```

Als validatie faalt: fix vóór je verder gaat. Schema is leidend.

## Eindrapport

Aan het einde van je doorloop:
- Aantal records klaar (`status=concept`)
- Aantal claims per confidence-token (geciteerd/afgeleid/verondersteld/betwijfeld)
- Cross-cluster relaties aangemaakt (top-level relaties[])
- Open punten / gaten / vragen voor mens-review
- Bron-coverage: welke records hebben primaire bron-citaten, welke niet
