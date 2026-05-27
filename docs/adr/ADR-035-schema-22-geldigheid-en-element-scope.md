# ADR-035 — Schema 2.2: geldigheid in inhoud + element-scope + versioning-consolidatie

**Status**: aanvaard
**Datum**: 2026-05-27
**Vervangt**: schema-uitbreidingen ADR-029 (operaties-model) + ADR-033 (scope.in/out)
**Werkpakket**: voorbereiding content-extractie-fase (granulariteit-skelet → uitgewerkte records)

## Context

Drie problemen uit skelet-werk + werkveld-vs-programma-validatie 2026-05-27:

1. **Versioning-verwarring**: schema 2.1 had sub-versioning `v1.5`/`v1.6` naast major `2.1`. User-opmerking: "het doet me nog altijd raar om 2 versioning telling naast elkaar te zien". Twee assen onnodig — consolideren naar één.

2. **Geldigheid van regelingen/regimes**: bij werkveld-vs-programma-validatie viel op dat sommige regelingen niet meer in voege zijn (notionele-interestaftrek afgeschaft AJ 2024 · cash-for-car uitdovend) maar didactisch nog relevant blijven. User-principe: "ik zou sowieso bij alle regelingen / regimes aangeven als ze niet meer in voege zijn... dan mag alles bewaard worden". User-verfijning: "dat moet gene metadata zijn, maar dat heeft een plaats nodig in de inhoud". → geldigheid is **inhoud** (conceptueel verschillend regime), geen metadata.

3. **Sub-concept-structuur als renderbeslissing** (OP-META.A 2026-05-27): user-inzicht "als een subconcept gestructureerd zou zijn zoals een concept, kan het er in theorie snel uitgetrokken worden... het zou zelfs een renderbeslissing kunnen zijn". Schema 2.1 had al recursieve `element`-structuur — wat ontbrak was sub-concept-scope (extractie-guidance op element-niveau).

Plus drop van `metadata.status` (seed/gevalideerd/te_herzien) — werd in praktijk niet gebruikt; mechanische history via changelog volstaat.

## Beslissing

**Schema 2.2** als breaking-update vs schema 2.1:

### Wijziging 1 — Versioning-consolidatie

- Schema-versie: `"2.2"` (niet meer "2.1 v1.5/v1.6")
- Eén versie-as voor alle schema-evolutie
- `metadata.schema_version: { "const": "2.2" }` (vereist exacte match)

### Wijziging 2 — `inhoud.geldigheid` (NIEUW)

Nieuw kern-aspect in `inhoud` voor regelingen/regimes/instrumenten:

```json
{
  "inhoud": {
    "geldigheid": {
      "status": "afgeschaft",                          // enum
      "sinds": "AJ 2024",                              // ISO-datum of AJ-aanduiding
      "tot": null,                                     // bij uitdovend: laatste contractdatum
      "wettelijke_basis": "Wet 22-12-2023 art. 80",   // wijzigingswet
      "opvolger": "alternative-record-id",             // optioneel, canonical_ref
      "toelichting": "..."                             // overgangsregels, grandfathering, context
    }
  }
}
```

**Status-enum** (verplicht):
- `in-voege` — huidig actief regime (default — kan weggelaten worden, dan default-aanname)
- `uitdovend` — geen nieuwe gevallen, bestaande blijven (bv. `cash-for-car` sinds 2026)
- `afgeschaft` — volledig geschrapt, behoud voor overgang+historiek (bv. `notionele-interestaftrek` AJ 2024)
- `historisch` — lang afgeschaft, alleen examen-historiek
- `ontwerp` — aangekondigd, nog niet in werking

**Optionele sub-velden**: `sinds` · `tot` · `wettelijke_basis` · `opvolger` · `toelichting`.

**Waarom inhoud i.p.v. metadata**:
- Afgeschaft regime is **conceptueel anders** dan in-voege regime (toepassings-context, advies-rol, examen-vraag-type verschillen)
- Stagiair stelt "geldt dit nog?" als eerste content-vraag, niet als technische metadata
- Inhoud kan rijk zijn (overgangsregeling · vervanger · grandfathering) — past niet in metadata-tag

### Wijziging 3 — Element-niveau `scope` en `geldigheid`

Schema 2.1 had al recursieve `element`-shape, maar elementen konden geen eigen `scope.in[]/scope.out[]` of `geldigheid` hebben. Schema 2.2 voegt beide toe:

```json
{
  "inhoud": {
    "elementen": [
      {
        "id": "voorbeeld-element",
        "naam": {...},
        "kern": {...},
        "scope": {
          "in": ["topic A van element"],
          "out": ["topic B — zie ander-record#element"]
        },
        "geldigheid": {
          "status": "uitdovend",
          ...
        },
        "elementen": [...]
      }
    ]
  }
}
```

**Reden**: extractie-guidance op sub-concept-niveau + sub-regimes met eigen geldigheid (bv. een sub-regeling kan uitdovend zijn binnen een nog-in-voege parent). Operationaliseert OP-META.A (subconcept-structuur als renderbeslissing).

### Wijziging 4 — `metadata.status` enum gedropt

Was: `enum ["seed", "gevalideerd", "te_herzien"]` — handmatige status-flag.

Nu: gedropt. Content-progress enkel via `changelog` (mechanisch beheerd door operatie-uitvoeringen). Reden: enum werd in praktijk niet onderhouden + changelog dekt het functioneel.

`metadata.schema_version` + `metadata.ankers` + `metadata.provenance` blijven verplicht.

## Backwards compatibility

**Breaking**. Records met `schema_version: "2.1"` zijn ongeldig onder schema 2.2.

**Migratie-pad**: bestaande 396 records worden in fase B (mapping-fase) opnieuw gegenereerd. Skeleton-records (status=skeleton) worden direct in schema-2.2-JSON geschreven door agent of mens, vanuit het tree-skelet. Oude content (v21) fungeert als draft-input voor agent, niet als 1-op-1 migratie. Geen automatische `migrate-v21-v22.py`-script — herschrijven via agent is doel.

Oude records bewaard in `data/concepten/records-v21/` voor referentie (read-only).

## Implicaties

### Voor records-API (`tools/lib/records_api.py`)

- Validator update naar schema 2.2
- `save_record` accepteert nu `inhoud.geldigheid` + element-scope
- Default `metadata.schema_version: "2.2"` voor nieuwe records
- Oude API bewaard als `records_api_v21.py` (deprecated, alleen voor archief-lezen)

### Voor agent-prompts

- Operatie-prompts in `prompts/operaties/` (renumbered 1-5) updaten voor schema 2.2
- Nieuwe `prompts/cluster-extract.md` voor 1-doorloop-all-operaties
- `inhoud.geldigheid` is verplicht voor regimes/regelingen (concept_type=`regime`); optioneel voor andere types

### Voor rendering (Quartz)

- Geldigheid-badges per status: `⏳ uitdovend` · `⛔ afgeschaft sinds <datum>` · `📜 historisch` · `🔜 ontwerp`
- Element-scope niet rendered (extractie-only-info)
- Sub-concept-renderbeslissing: render-laag kiest inline-sub-sectie of aparte fiche o.b.v. sub-concept-content-omvang

## Rationale-traceability

Skelet-doc `docs/granulariteit-skelet.md` rationale-log entries 2026-05-27:
- "Geldigheid-conventie ... `inhoud.geldigheid` als nieuw kern-aspect"
- "Werkveld-vs-programma-validatie ... bedrijfsadvies-cluster + OP-META.B synthese-records"
- "Subconcept-structuur als renderbeslissing (OP-META.A)"

User-principes verankerd:
- "content hoort waar het in de praktijk leeft, niet in een specifiek PO"
- "minder aan de ankers koppelen, meer vanuit het werkveld denken"
- "bij alle regelingen / regimes aangeven als ze niet meer in voege zijn... dan mag alles bewaard worden"
- "dat moet gene metadata zijn, maar dat heeft een plaats nodig in de inhoud"

## Open punten

- **OP-META.B** synthese-/overzichts-records-pattern blijft open — niet in schema 2.2 verankerd; voor nu via `inhoud.syntheses[]` (al bestaand) of leerpad-niveau
- **OP-IFRS.A** Σ-promotie `vaste-activa` met sub-records (boekhouding-cluster) — toekomstige revisie
- Validator-tests voor schema 2.2 nog te schrijven (`tools/lib/records_api.py` audit_parity)

## Vervolg

1. **Folder migratie**: `data/concepten/records/` → `records-v21/` (read-only archief)
2. **records_api.py update** voor schema 2.2 + bewaar oude als `records_api_v21.py`
3. **Skeleton-JSON's direct schrijven**: per cluster genereert agent (of mens) schema-2.2-valide skeleton-records rechtstreeks in `data/concepten/records/`. Geen tussenformaat — JSON is bron-van-waarheid en schema-leidend.
4. **Prompt-renumbering** + `cluster-extract.md` (overkoepelend, 5 operaties in 1 doorloop)
5. **Test op boekhouding-cluster** (eerste batch, jaarrekening-fundament voor vrouw)
