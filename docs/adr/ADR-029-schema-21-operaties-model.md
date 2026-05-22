# ADR-029 — Schema 2.1 + operaties-model

**Status**: draft (2026-05-22, herzien naar v1.5 op 2026-05-23)
**Vervangt deels**: ADR-025 (schema 2.0)
**Gerelateerd**: dit ADR documenteert de migratie van pipeline-model (runs 1-5) naar operatie-model (willekeurige verbeter-operaties).

**Canonieke spec v1.5**: [`docs/schema-v15-besluit.md`](../schema-v15-besluit.md) — geconsolideerd referentie-document met alle 21 v1.5-besluiten + finale schema-structuur + operations-model. Lees dat document als bron-van-waarheid voor de actuele structuur; deze ADR documenteert de ontwerpredenering en evolutie.

**Voorgeschiedenis-tracker**: [`docs/adr/archive/schema-feedback-22mei.md`](archive/schema-feedback-22mei.md) — discussie + iteraties tussen v1.4 en v1.5 (gearchiveerd).

## Beslissing

Schema voor concept-records gaat van versie **2.0 → 2.1**, met:
- Abstractere veldnamen (`mechanisme` ipv `hoe_het_werkt`, `verrijken` ipv proza-zinnen)
- 10 node_types incl. `methode` en `actor` (was 7)
- Vier zones: identiteit · metadata · inhoud · relaties
- 5 confidence-tokens: `geciteerd`/`afgeleid`/`verondersteld`/`betwijfeld`/`weerlegd`
- Verplichte `grondslag` per claim met ≥1 bron (incl. `ai_model`/`mens` als bron-types)
- Render-laag bepaalt labels (geen NL-zinnen in keys)

**Bron-van-waarheid**: `data/concepten/schema-2.1.schema.json` (JSON Schema 2020-12). Mens-leesbare uitleg in `$comment`/`description` per def. Voorganger-specs (`schema-2.0-canonical-spec.md`, `schema-2.1-canonical-spec.md` als markdown) zijn verwijderd; alle ontwerpredenering leeft in deze ADR + `docs/schema-v15-besluit.md`.

## Operaties-model (vervangt sequentiële runs)

Concept-extractie en -verrijking gebeurt via **willekeurig-toepasbare operaties** op een record, niet via vaste run-volgorde:

| Operatie | RAG nodig? | Wat verbetert |
|---|---|---|
| `beschrijven` | nee | inhoud uitvullen met training-data; **alleen `verondersteld`/`betwijfeld`** — `geciteerd`/`afgeleid`/`weerlegd` verboden in deze operatie |
| `claims_checken` | ja (bronnen-RAG) | `verondersteld` → `geciteerd`/`afgeleid`/`weerlegd`; voegt wettekst-bronnen toe aan `grondslag.bronnen[]` |
| `relaties_aanvullen` | ja (concept-RAG) | `vergelijkbaar_met`-gelijkenissen/verschillen; bevat-edges valideren |
| `accountant_perspectief` | optioneel (normen/IBR-RAG) | rollen × perspectief uitwerken |
| `didactisch_verrijken` | nee | rationale uitbreiden, voorbeelden toevoegen, mensentaal |
| `kandidaat_review` | nee | proeflezen door studentbril, gaps signaleren |
| `cijfer_validatie` | ja (Cijferzakboekje-RAG) | tarieven/drempels exact valideren |
| `examenvragen_aansluiting` | ja (examenvragen-RAG) | koppel concept aan examenvragen die het dekt |
| `consistentie_check` | nee | terminologie consistent met sibling-records |
| `volledigheid_check` | nee | node_type-specifieke checklist, gap-rapport |

**Naamkeuze `beschrijven` vs `uitleggen`**: `beschrijven` is gekozen omdat de eerste operatie neutraal observeert (wat IS dit concept), terwijl `uitleggen` didactiek-georiënteerd is (concept voor student verteren). Didactiek hoort bij latere operatie `didactisch_verrijken`.

**Schrijfregel — geen inline wettekst in body**: alle art-nummer-verwijzingen leven in `grondslag.bronnen[]` met `type: "wettekst"` + `ref`-veld, niet in `text`/`beschrijving`-proza. Dit maakt `claims_checken` makkelijker (per-bron-valideren ipv proza-parsing).

**Volgorde-onafhankelijk** behalve voor de eerste 2 stappen:
1. `skeleton` (deterministisch, geen LLM) — wordt automatisch gegenereerd uit candidates-DB
2. `beschrijven` (eerste keer) — vult lege `inhoud` met training-data

Daarna: elke operatie kan in elke volgorde op elk concept worden toegepast.

## State-tracking

Per concept: `metadata.changelog[]` houdt bij welke operaties zijn uitgevoerd:

```json
{
  "datum": "2026-05-22",
  "wave_id": "operate-claims-checken-20260523",
  "model": "claude-opus-4-7",
  "operatie": "claims_checken",
  "wijziging": "Upgraded 36 claims naar geciteerd/afgeleid; 5 weerlegd geflagd"
}
```

`metadata.status` blijft op `seed` tot eerste `beschrijven` is gedaan, daarna `gevalideerd` na bv. `claims_checken` + `kandidaat_review`.

## Workflow-voorbeeld (rolling)

Voor 396 records, gebruiker kiest:

```bash
# 1. Skeletten (al gedaan, deterministisch)
python3 -m tools.extractie.skeleton_from_candidate --all-pending

# 2. Eerste pas voor alle: beschrijven
#    Via chat-orchestrator (Claude Code Agent-tool): 12 agents parallel per batch
#    Of: gebruiker draait via dump-batch-prompts

# 3. Selectieve verbeteringen:
multi_pass operate --operatie claims_checken --node-type regime
multi_pass operate --operatie didactisch_verrijken --fiche obligatielening,leasing
multi_pass operate --operatie kandidaat_review --primary-po 1.1
```

## Naamgeving open beslispunten

- Naam `beschrijven` (huidige keuze) vs `verrijken_basis` voor eerste operatie
- Bron-types `ai_model`/`mens` toegestaan voor `verondersteld`-claims
- `weerlegging`-veld op `grondslag` voor `weerlegd`-confidence

## Schema 2.0 → 2.1 migratie

Voor de 600+ bestaande v2.0-records (nu in `data/concepten/_archive/v2.0-pre-schema-2.1-…`):
- Mechanische normalisatie (kind→node_type, paargroep platslaan, etc.) — script in toekomstige sprint
- Of: laat archief intact, geen migratie (records verschijnen niet in nieuwe pipeline)

Voor de 396 nieuwe skelet-records: born-on-2.1, geen migratie.

## Gevolgen

- **`tools/extractie/multi_pass_extract.py`** vervangen door `operate`-CLI met operatie-naam als arg
- **`prompts/operaties/<naam>.md`** — 5 slanke operatie-prompts (schema-driven, 60-93 regels elk; `prompts/multipass/` verwijderd 2026-05-23)
- **`metadata.changelog[].operatie`** verplicht (na deze ADR)
- Validator hoeft niet aangepast: schema 2.1 is operatie-agnostisch
- ADR-025 §schema-2.0-records-fields verouderd — verwijst nu naar dit ADR

## Bewijzen van waarde (22 mei 2026)

- A/B-test schema-prompt vs proza-prompt: 106 schema-errors → 0
- Multi-pass op kapitaalvermindering: 5 inhoudelijke fouten gevonden door `claims_checken`
- Opus vs Sonnet bench op notionele-interestaftrek: Opus accurater op art-precisie + historische context
- Scale-test 12 parallel Sonnet-agents: ~3 min wall-clock voor 12 records, 0 hangs
- 27/396 records gevuld als bewijs dat pipeline werkt

---

## Update v1.5 (2026-05-23) — finale structuur en operations-model

Na ~10 iteratie-rondes (gedocumenteerd in `docs/adr/archive/schema-feedback-22mei.md`) is schema 2.1 geconvergeerd op **v1.5**. Alle 21 besluiten en de finale shape leven in [`docs/schema-v15-besluit.md`](../schema-v15-besluit.md); hieronder enkel de samenvatting van wat ten opzichte van v1.4 verandert en waarom.

### Velden gedropt

| Veld | Reden |
|---|---|
| `naam.andere_talen` | Nooit gebruikt; meertalig hoort niet in concept-record. |
| `metadata.dekt_tdks` | Overlap met `metadata.ankers` (zelfde anker-keten). Unified naar `ankers`. |
| `metadata.tags` | Vrije-vorm-tags duplicaat van `concept_type` + `ankers`; render gebruikt structuur. |
| `metadata.cross_po` | Afleidbaar uit `ankers` (multi-programmaonderdeel). |
| `metadata.primary_po` | Afleidbaar uit `ankers[0]`. |
| `element.beschrijving` | Vervangen door fractale `element.kern.{definitie,substantie,rationale}`. |
| `element.verwijst_naar` | Vervangen door `relaties[]` (graph-edges op concept- of claim-niveau). |
| `inhoud.keuzekader` | Generieker vervangen door `syntheses[]` met `type`-discriminator. |
| `voorbeeld_inline` + `voorbeeld_case` | Geünificeerd naar `voorbeelden[]`. |

### Hernoemingen

| v1.4 | v1.5 | Reden |
|---|---|---|
| `metadata.linked_anchors` | `metadata.ankers` | Korter, NL-consistent, unified met dekt_tdks. |
| `tekst.text` | `tekst.tekst` | NL-consistentie binnen `tekst`-type. |
| `inhoud_type: component` | `inhoud_type: subconcept` | "subconcept" leest natuurlijker voor render. |
| `inhoud.rollen_per_perspectief` | `inhoud.accountant_perspectieven` | 1 nesting-laag weg + explicieter (accountant-rol). |

### Toegevoegd

- **`inhoud.kern`-wrapper** ({`definitie?`, `substantie?`, `rationale?`} — ≥1 verplicht): groepeert de drie "wat-is-dit"-claims, zowel op concept-niveau als binnen elk `element`. Hard juridisch versus zacht-economisch onderscheid leeft in `grondslag.confidence`, niet in de structuur.
- **`inhoud.valkuilen[]`**: didactisch concept-niveau-veld voor "wat denkt iedereen verkeerd". Sub-shape: `{titel, verkeerde_assumptie, kernpunt, grondslag}`.
- **`inhoud.speelruimtes[]`**: didactisch concept-niveau-veld voor "wat kun je vrij kiezen binnen de wet". Sub-shape: `{titel, opties[], vuistregel?, grondslag}`.
- **`inhoud.syntheses[]`**: generieker dan keuzekader, met type-discriminator (`keuzekader | tijdslijn | beslisboom | matrix | dashboard`).

### Fractale recursie als kern-principe

`element` heeft nu dezelfde shape als concept-niveau-`inhoud`: een `element` mag zelf `elementen[]`, `voorbeelden[]`, `valkuilen[]`, `speelruimtes[]`, `weergaven[]` bevatten plus een eigen `kern`-wrapper. Recursie tot max 3 niveaus. Dit elimineert het verschil "concept versus element" — een sub-concept is gewoon een element met meer diepte.

### Trim enums

- **`inhoud_type`**: 19 → 12 (`begrip · stap · drempel · regel · uitzondering · vuistregel · mechanisme · risico · formule · principe · subconcept · beperking`). Gedropt: `berekening`, `vergelijking`, `moment_in_tijd`, `eigenschap`, `valkuil`, `voorwaarde`, `procedure_stap`, `stap_in_cyclus`, `keuze`, `component`. Hernoemingen: `procedure_stap`+`stap_in_cyclus` → `stap`, `component` → `subconcept`. Nieuw: `beperking` (inherente zwakte van een indicator).
- **`weergave_type`**: 14 → 11 (`proza · tabel · boeking · balans_snapshot · resultatenrekening_snapshot · stappenlijst · tijdslijn · vergelijkingstabel · formule_expressie · berekening · beslisboom`). Gedropt: `t_rekening` (variant van `boeking`), `voorbeeld` (was nooit een weergave), `diagram` (te vaag), `casus` (hernoemd naar `voorbeeld`-array op inhoud-niveau).
- **Nieuwe types**: agent rapporteert nieuwe `inhoud_type`/`weergave_type`-suggesties in eindrapport (niet in JSON). Orchestrator scant frequentie en bouwt schema-uitbreiding.

### Gebruikscontext: arrays overal

Alle sub-velden van `gebruikscontext` zijn arrays geworden — ook `trigger_start`, `trigger_einde`, `voordeel`, `risico` (waren singular in v1.4). Reden: een verrichting kan meerdere triggers en meerdere risico's hebben; render-laag kan een bullet-list maken zonder normalisatie.

### Operations-model — actuele set

De v1.4-tabel met 10 operaties is verfijnd. De zeven operaties die actief uitgewerkt worden:

| Operatie | Wat doet ze |
|---|---|
| `beschrijven` | Eerste pas — vult `kern` + `elementen` + `gebruikscontext` met training-data. Alleen `verondersteld`/`betwijfeld`. |
| `claims_checken` | RAG-validatie van bestaande claims; upgrade naar `geciteerd`/`afgeleid` of flag `weerlegd`. |
| `relaties_aanvullen` | Concept-RAG-gedreven `relaties[]`-uitbouw, met name `vergelijkbaar_met`-paren. |
| `accountant_perspectief` | Vul `accountant_perspectieven[]` per relevante actor (vennootschap, aandeelhouder, accountant-zelf). |
| `didactisch_verrijken` | Voegt `valkuilen[]`, `speelruimtes[]`, `voorbeelden[]` toe; expandeert `rationale`. |
| `kandidaat_review` | Proefleesoperatie door studentbril; produceert gaps + suggestie-rapport. |
| `leespad_aanvullen` | Vult `inhoud.voorkennis_leespad`-veld op basis van anker-positie en `vereist`-relaties. |

`cijfer_validatie`, `examenvragen_aansluiting`, `consistentie_check`, `volledigheid_check` blijven op de roadmap maar zijn niet prioritair voor wave-2.

### Confidence-tokens (onveranderd uit v1.4)

`geciteerd (📖)` · `afgeleid (🔗)` · `verondersteld (🤖 of 🧠)` · `betwijfeld (❓)` · `weerlegd (❌)`.

Tijdens `beschrijven`-operatie alleen `verondersteld` of `betwijfeld` toegestaan; upgrade pas tijdens `claims_checken`.

### Bron-types (onveranderd uit v1.4)

`wettekst · kb · cbn · advies · norm · richtlijn · circulaire · rechtspraak · modelverdrag · tarief · aangifte · ai_model · mens`. Conditional-required: primaire bronnen vereisen `ref`; `ai_model`/`mens` vereisen `datum`+`naam`.

### Plaatsingsregel "wat-is-het" vs "wat-doet-de-accountant" (E3, vastgelegd 2026-05-23)

E3 was uitgesteld tot wave-2. Bij review van gemigreerde records (kapitaalvermindering: "Boekhoudkundige verwerking" zat als `procedure_stap` in `inhoud.elementen[]`) bleek de regel al impliciet hard in ADR-025 §190 en v5-prompts vastgelegd, maar **niet meegekopieerd naar v1.4/v1.5-prompts**. Op 2026-05-23 alsnog geformaliseerd in schema + run-1 + run-2 voordat wave-2 (371 records) start — anders herhaalt dezelfde drift zich.

**Litmus**: "gebeurt dit ongeacht of er een accountant bij betrokken is?" → ja → `inhoud.elementen[]`; → nee → `inhoud.accountant_perspectieven[].rollen[].elementen[]`.

Vuistregels per rol:
- `boekhouder` → boekhoudkundige verwerking · rekening-codes · boekingsmoment
- `auditor` → audit-procedures · risico-drempels · controle-aandachtspunten
- `fiscaal` → aangifte-codes · fiscale optimalisatie-stappen
- `adviseur` → advies-checklist · alternatieven-afweging · vuistregels
- `begeleider` → begeleidings-stappen · formaliteiten · termijn-bewaking

Concept-intrinsieke procedures (wettelijke termijn, dwingende formaliteiten als onderdeel van een verrichting) blijven in `inhoud.elementen`. Bij dubbeling: kruisverwijs via `relaties[]` op de claim, niet dupliceren.

**Documentatie**: `$comment` op `inhoud.elementen` + `$defs/perspectief` + `$defs/rol_invulling` in schema; "Plaatsingsregel"-secties in `prompts/operaties/beschrijven.md` + `prompts/operaties/accountant_perspectief.md`; samengevat in `docs/schema-v15-besluit.md`.

**Open (na wave-2)**: diepere per-rol-element-typering — bv. of `rol=boekhouder.elementen[]` altijd één `weergave_type=boeking` moet hebben. Empirisch evalueren met ≥ 50 ingevulde records. Hier blijft licht-prompt-discipline gelden.

**Migratie-implicatie voor 396 bestaande records**: items in `inhoud.elementen[]` die volgens de plaatsingsregel onder een rol horen, worden bij `accountant_perspectief`-operatie verplaatst (deze records hebben nu nog geen `accountant_perspectieven` ingevuld; geen aparte migratie-batch nodig). Audit-script kan flaggen welke records `procedure_stap`-elementen hebben die mogelijk verplaatst moeten worden.

### Changelog

| Versie | Datum | Hoofdpunten |
|---|---|---|
| 2.1-v1.0 | 2026-05-22 | Eerste 2.1-draft: abstracte keys, 4-zone-structuur, 10 confidence-tokens, JSON Schema 2020-12. |
| 2.1-v1.1–v1.3 | 2026-05-22 | A/B-test schema-prompt, multi-pass-bench, schaal-test 12-parallel. |
| 2.1-v1.4 | 2026-05-22 | `node_type → concept_type`, `voorbeeld_case → voorbeeld`, `bron_ref` conditional-required, `inhoud_type` per-waarde-comments. |
| 2.1-v1.5 | 2026-05-23 | Drop 9 velden, hernoemen 4 velden, `kern`-wrapper, fractale recursie, `valkuilen`/`speelruimtes`/`syntheses` arrays, trim enums (12 inhoud_types + 11 weergave_types), operations-model uitgewerkt naar 7 actieve operaties. Canonieke spec in `docs/schema-v15-besluit.md`. |

### Migratie v1.4 → v1.5

Migratie-script (`tools/extractie/migrate_records_to_v15.py`, in parallelle agent) port alle 396 records. Belangrijkste transformaties:

- `linked_anchors` → `ankers`
- `text` → `tekst` overal (universele bron-van-eenheid binnen `tekst`-type)
- Drop `dekt_tdks`, `tags`, `cross_po`, `primary_po` uit `metadata`
- `inhoud.{definitie,substantie,rationale}` → `inhoud.kern.{definitie,substantie,rationale}` (idem voor `element.kern`)
- `rollen_per_perspectief.perspectieven[]` → `accountant_perspectieven[]` (top-level wrapper weg)
- `voorbeeld_inline` + `voorbeeld_case` → `voorbeelden[]`
- Drop `element.beschrijving`/`element.verwijst_naar` (waar zinvol porten naar `relaties[]`)
- Trim `inhoud_type` + `weergave_type` waarden (rename + drop)
- `keuzekader` → `syntheses[0]` met `type: keuzekader`
- `gebruikscontext.{trigger_start,trigger_einde,voordeel,risico}` naar arrays

Zie [`docs/schema-v15-besluit.md`](../schema-v15-besluit.md) §"Implementatie-stappen v1.4 → v1.5" voor exact-script-en-volgorde.
