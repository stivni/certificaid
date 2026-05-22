# Schema 2.1 → v1.5 — besluit-document (23 mei 2026)

**Status**: 21 besluiten, 1 uitgesteld. Klaar voor implementatie.
**Voorgeschiedenis-tracker**: [`docs/adr/archive/schema-feedback-22mei.md`](adr/archive/schema-feedback-22mei.md) — volledige discussie + iteraties (gearchiveerd)
**Vorige spec**: schema 2.1 v1.4 — frozen in `data/concepten/schema-2.1.schema.json`. 396 records valideren tegen v1.4.

---

## Schema v1.5 — finale structuur

### Top-level (4 zones)

```json
{
  "id": "kebab-slug",
  "naam": { "primair": "...", "afkorting?": "...", "synoniemen?": [...], "vertaling?": {...} },
  "concept_type": "instrument | verrichting | procedure | balanspost | ratio | regime | methode | kader | principe | actor",
  "schema_version": "2.1",

  "metadata": {
    "status": "seed | gevalideerd | te_herzien",
    "ankers": [...],                  // ← unified (was linked_anchors + dekt_tdks)
    "provenance": { model, wave_id, ... },
    "changelog": [
      { "operatie": "...", "timestamp": "...", "model": "...", "wave_id?": "...", "wijziging?": "...", "metriek?": {...} }
    ]
  },

  "inhoud": {
    "kern": {
      "definitie?":  { "tekst": "...", "grondslag": {...}, "weergaven?": [...], "relaties?": [...] },  // wat IS het (juridisch hard of zacht — geen structuur-verschil)
      "substantie?": { ... },                                                                            // wat betekent het economisch
      "rationale?":  { ... }                                                                             // waarom werkt het zo
    },
    "voorkennis_leespad?": { ... },                              // BEHOUD als optioneel; ingevuld door aparte operatie `leespad_aanvullen`
    "gebruikscontext?": {                                         // alle sub-velden zijn ARRAYS
      "voor": [...], "niet_voor": [...],
      "voorwaarden": [...], "uitsluitingen": [...],
      "indicaties": [...], "contra_indicaties": [...],
      "trigger_start": [...], "trigger_einde": [...],            // ← arrays (was singular)
      "voordeel": [...], "risico": [...]                          // ← arrays
    },
    "elementen?":  [ element ],
    "voorbeelden?": [ voorbeeld ],                                // unified (was case + inline)
    "valkuilen?": [ valkuil ],                                    // NIEUW concept-niveau didactisch
    "speelruimtes?": [ speelruimte ],                             // NIEUW concept-niveau didactisch
    "accountant_perspectieven?": [ perspectief ],                 // HERNOEMD (was rollen_per_perspectief), 1 nesting-laag weg
    "syntheses?": [ synthese ]                                    // VERVANGT keuzekader; type-discriminator
  },

  "relaties": [ relatie ]                                          // top-level: concept-naar-concept graph
}
```

### Sub-structuren

**`tekst`-type** (universeel — bron-van-eenheid, was tekstblok+contextitem):
```json
{
  "tekst": "...",                          // ← property hernoemd uit "text"
  "grondslag": { confidence, bronnen[], checked_at?, claim_hash?, weerlegging? },
  "rationale?": "...",                     // optioneel — uitleg waarom deze claim
  "weergaven?": [ weergave ],              // optioneel — visualisaties van deze claim
  "relaties?": [ relatie ]                 // optioneel — inline-relaties vanaf deze claim
}
```

**`element`** (fractale recursie — gelijke shape als concept-niveau inhoud):
```json
{
  "id": "kebab-slug",
  "naam": { "primair": "...", ... },
  "inhoud_type": "<enum 12>",
  "kern": { "definitie?": tekst, "substantie?": tekst, "rationale?": tekst },   // ≥1 verplicht
  "weergaven?": [ weergave ],
  "elementen?": [ element ],                                                     // recursie max 3 niveaus
  "voorbeelden?": [ voorbeeld ],
  "valkuilen?": [ valkuil ],
  "speelruimtes?": [ speelruimte ]
}
```

(geen `beschrijving` meer, geen `verwijst_naar` meer — relateert via `relaties[]` op claims)

**`voorbeeld`** (unified):
```json
{
  "id?": "kebab-slug",                     // optioneel; nodig voor top-level voorbeelden die anker krijgen
  "titel": "...",                          // verplicht, korte titel
  "context?": "...",                       // optioneel intro ("NV ABC heeft...")
  "grondslag?": { ... },
  "weergaven?": [ weergave ],
  "elementen?": [ element ]                // recursie
}
```

**`valkuil`** (didactisch, strict — vaak verkeerd gedacht):
```json
{
  "titel": "...",
  "verkeerde_assumptie": "...",            // wat denken studenten/practitioners vaak verkeerd
  "kernpunt": "...",                       // effectief te volgen principe
  "grondslag": { ... }
}
```

**`speelruimte`** (didactisch — wat kun je vrij kiezen binnen de wet):
```json
{
  "titel": "Spreidingsmethode disagio/agio",
  "opties": [
    { "keuze": "Lineair", "voordeel": "...", "nadeel?": "..." },
    { "keuze": "Effective interest", "voordeel": "...", "nadeel?": "..." }
  ],
  "vuistregel?": "...",                    // praktijk-advies bij de keuze
  "grondslag": { ... }
}
```

**`synthese`** (vervangt keuzekader, generieker):
```json
{
  "type": "keuzekader | tijdslijn | beslisboom | matrix | dashboard",
  "intro?": "...",
  "inhoud": { ... }                        // type-afhankelijk schema (TBD per type)
}
```

**`relatie`** (top-level concept-naar-concept):
```json
{
  "type": "<relatie_type>",                // 14 types (zie schema)
  "target": "canonical-ref",
  "grondslag?": { ... },
  "toelichting?": string | tekst,
  // alleen voor type=vergelijkbaar_met:
  "gelijkenissen?": [...], "verschillen?": [...], "verwarring_risico?": "...", "render_hint?": "..."
}
```

**`accountant_perspectieven`** (vereenvoudigde hiërarchie):
```json
[
  {
    "id": "uitgever-vennootschap",
    "naam": { "primair": "..." },
    "rollen": [
      {
        "rol": "adviseur | boekhouder | begeleider | fiscaal | auditor",   // 5 rollen
        "elementen": [ element ]
      }
    ]
  }
]
```

### `inhoud_type` enum (12 types)

```
begrip · stap · drempel · regel · uitzondering · vuistregel · mechanisme
· risico · formule · principe · subconcept · beperking
```

(was 19; gedropt: `berekening` `vergelijking` `moment_in_tijd` `eigenschap` `valkuil` `voorwaarde` `procedure_stap` `stap_in_cyclus` `keuze` `component`. Renames: `procedure_stap`+`stap_in_cyclus` → `stap`; `component` → `subconcept`. Nieuw: `beperking` (inherente zwakte van indicator).)

### `weergave_type` enum (11 types)

```
proza · tabel · boeking · balans_snapshot · resultatenrekening_snapshot
· stappenlijst · tijdslijn · vergelijkingstabel · formule_expressie
· berekening · beslisboom
```

(was 14; gedropt `t_rekening` (variant boeking), `voorbeeld` (was nooit weergave), `diagram` (te vaag), `casus` (was renamed to voorbeeld). Behouden `beslisboom`.)

**Detail-schemas (TBD na v1.5)**: per `boeking` / `balans_snapshot` / `tabel` een sub-schema dat de payload-structuur valideert (rekeningen[], actief/passief, kolommen+rijen).

**Nieuwe types**: agent rapporteert in eindrapport (NIET in JSON). Orchestrator scant frequentie en bouwt schema-uitbreiding.

### `confidence`-tokens (onveranderd uit v1.4)

```
geciteerd (📖) · afgeleid (🔗) · verondersteld (🤖/🧠) · betwijfeld (❓) · weerlegd (❌)
```

Tijdens `beschrijven`-operatie alleen `verondersteld` en `betwijfeld` toegestaan.

### `bron_type` enum (onveranderd uit v1.4)

```
wettekst · kb · cbn · advies · norm · richtlijn · circulaire · rechtspraak
· modelverdrag · tarief · aangifte · ai_model · mens
```

Conditional-required: primaire bronnen vereisen `ref`; ai_model/mens vereisen `datum`+`naam`.

### `relatie_type` enum (onveranderd uit v1.4)

```
bevat · valt_onder · triggert · beinvloed_door · vereist · is_uitzondering_op
· niet_combineerbaar_met · vergelijkbaar_met · uitgevoerd_door · gecontroleerd_door
· gepubliceerd_via · goedgekeurd_door · gedocumenteerd_in · alternatief_referentiestelsel
```

---

## Implementatie-stappen v1.4 → v1.5

1. **Schema-update** `data/concepten/schema-2.1.schema.json`:
   - Drop velden (per spec hierboven)
   - Hernoemen `text`→`tekst`, `linked_anchors`→`ankers`, `component`→`subconcept`, etc.
   - Voeg toe: `kern`-wrapper, `valkuilen[]`, `speelruimtes[]`, `syntheses[]`
   - Trim enums
   - Rich `$comment`/`description` per def voor agent-zelfsturing (vermindert prompt-omvang)

2. **Records-migratie** `tools/extractie/migrate_records_to_v15.py`:
   - `linked_anchors` → `ankers`
   - `text` → `tekst` overal
   - `dekt_tdks`/`tags`/`cross_po`/`primary_po` weg uit metadata
   - `inhoud.definitie/substantie/rationale` → `inhoud.kern.{definitie,substantie,rationale}`
   - Idem voor element.kern
   - `rollen_per_perspectief` → `accountant_perspectieven` (drop top-level `perspectieven`-wrapper)
   - `voorbeeld_inline` + `voorbeeld_case` → `voorbeeld`
   - Drop `element.beschrijving`/`element.verwijst_naar` (verwijderen, of port naar relaties[])
   - Trim inhoud_type-waarden (rename + drop)
   - Trim weergave_type-waarden
   - `keuzekader` → `syntheses[0]` met `type: keuzekader`
   - `gebruikscontext.trigger_start/einde/voordeel/risico` naar arrays

3. **Prompts updaten**:
   - `prompts/multipass/run-1-draft.md` → naar `beschrijven`-operatie-prompt
   - Andere run-prompts naar operatie-naam
   - Schema-comments-driven (kortere prompts mogelijk)

4. **Scripts updaten**:
   - `skeleton_from_candidate.py`: gebruik nieuwe `ankers`, `kern.definitie`-structuur, etc.
   - `build_records_index.py`: lees `ankers` ipv linked_anchors
   - `multi_pass_extract.py`: idem

5. **ADR-029 update** met v1.5-finale beslissingen + dit document als referentie.

6. **Test-run** met 1-2 fiches om agent + schema te valideren vóór wave-2 op alle records.

---

## Bestand-paden (huidige status)

| Pad | Wat | Status |
|---|---|---|
| `data/concepten/schema-2.1.schema.json` | Schema (nu v1.4) | Te updaten naar v1.5 |
| `data/concepten/records/*.json` | 396 records (v1.4) | Te migreren v1.5 |
| `tools/extractie/skeleton_from_candidate.py` | Skelet-generator | Update structuren |
| `tools/extractie/build_records_index.py` | Index-builder | Update veldnamen |
| `tools/extractie/multi_pass_extract.py` | Orchestrator-helper | Update rapport-velden |
| `tools/extractie/migrate_records_to_v14.py` | Vorige migratie | Template voor v15 |
| `prompts/multipass/run-1-draft.md` | Beschrijven-prompt | Update naar nieuwe schema-structuur |
| `prompts/multipass/run-{2,3,4,5}-*.md` | Andere operatie-prompts | Update |
| `docs/adr/ADR-029-schema-21-operaties-model.md` | Operaties-model ADR | Update voor v1.5 |
| `docs/render-laag.md` | Render-laag spec | Werkpakket Fase 7 |
| `docs/adr/archive/schema-feedback-22mei.md` | Discussietracker | Bevroren (historisch) |
| `data/concepten/_archive/v2.0-pre-schema-2.1-…` | Legacy v2.0 records | Bewaard |

---

## Open beslispunt (0)

E3 (rol-element sturing) is op 2026-05-23 gepromoveerd van "uitgesteld / light-touch" naar **vastgelegde plaatsingsregel** (zie hieronder). Diepere data-driven per-rol-element-typering blijft een wave-2-evaluatie, maar de basis-grens is nu hard.

---

## Plaatsingsregel "wat-is-het" vs "wat-doet-de-accountant" (vastgelegd 2026-05-23)

**Reden voor formalisatie nu** (niet wave-2): regel stond al in ADR-025, v5-prompts en sessie-handoffs, maar werd bij v1.4/v1.5-migratie niet meegekopieerd. Resultaat: records als `kapitaalvermindering` hebben "Boekhoudkundige verwerking" als top-level `inhoud.elementen[]` i.p.v. onder `accountant_perspectieven[rol=boekhouder]`. Voor de 371 wave-2-records moeten we nu sturen voordat dezelfde drift opnieuw ontstaat.

**Litmus**: "gebeurt dit ongeacht of er een accountant bij betrokken is?"
- **Ja** → `inhoud.elementen[]` (concept-intrinsiek)
- **Nee** → `inhoud.accountant_perspectieven[].rollen[].elementen[]` (handelings-kennis)

| Inhoud | Plek |
|---|---|
| Boekhoudkundige verwerking · rekening-codes · boekingsmoment | rol=`boekhouder` |
| Audit-procedures · risico-drempels · controle-aandachtspunten | rol=`auditor` |
| Aangifte-codes · fiscale optimalisatie-stappen | rol=`fiscaal` |
| Advies-checklist · alternatieven-afweging · vuistregels | rol=`adviseur` |
| Begeleidings-stappen bij transactie/procedure · formaliteiten | rol=`begeleider` |
| Wettelijke voorwaarden · concept-intrinsieke procedures · mechanisme · sub-concepten · formules | `inhoud.elementen[]` |

**Documentatie van deze regel**:
- Schema: `$comment` op `inhoud.elementen` + `$defs/perspectief` + `$defs/rol_invulling` in `data/concepten/schema-2.1.schema.json`
- Prompts: secties "Plaatsingsregel" in `prompts/multipass/run-1-draft.md` + `run-2-rollen.md`
- ADR: zie ADR-029 §E3 (geüpdatet)

**Open (wave-2)**: diepere per-rol-element-typering — bv. of `boekhouder.elementen[]` altijd één `weergave_type=boeking` moet hebben. Empirisch evalueren na ≥ 50 ingevulde records.

---

## Wat na schema v1.5-implementatie

- **Wave-2 start**: 371 lege records via 12-parallel `beschrijven`-operatie (~1.5u wall-clock geschat)
- **Render-sessie**: aparte chat met [`docs/render-laag.md`](render-laag.md) als werkpakket-spec
- **Operaties uitbouwen**: `claims_checken` met RAG, dan `relaties_aanvullen`, `accountant_perspectief`, etc.
- **Examen-deadline**: ca. 2026-05-30 (~7 dagen)

---

## Quick-start prompt voor volgende sessie (na /compact)

```
Lees docs/schema-v15-besluit.md voor volledige context. We zijn klaar voor implementatie:

1. Schema v1.4 → v1.5 update in data/concepten/schema-2.1.schema.json
2. Migratie-script v1.4 → v1.5 + records-port
3. Scripts en prompts updaten
4. Validatie + test-run

Begin met (1) schema-update.
```
