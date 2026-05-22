# Operatie: `beschrijven` (vervangt run-1)

Schema-versie: 2.1 v1.5 (zie `data/concepten/schema-2.1.schema.json` voor de finale structurele waarheid — `$comment`/`description` per `$def` is bron-van-zelfsturing; deze prompt geeft werkwijze en discipline).

**Doel**: vul `inhoud` van het skelet-record met **alle proza + structuur uit je training-data**. Geen RAG, geen MCP-calls. Snel.

**Output**: overschrijf `/tmp/<fiche-id>.json` met het uitgebreide record.

---

## Confidence-tokens (overzicht)

| Token | Symbool | Wanneer toegestaan in `beschrijven` |
|---|---|---|
| `geciteerd` | 📖 | ❌ — vereist primaire-bron-validatie → `claims_checken` |
| `afgeleid` | 🔗 | ❌ — vereist combinatie ≥ 2 primaire bronnen → `claims_checken` |
| `verondersteld` | 🤖 | ✅ — claim uit training-data, `ai_model`-bron |
| `betwijfeld` | ❓ | ✅ — twijfel over precisie (datum, percentage, art-nummer) |
| `weerlegd` | ❌ | ❌ — vereist bron-contradictie → `claims_checken` |

**HARDE REGEL**: tijdens `beschrijven` alleen `verondersteld` of `betwijfeld`. Self-check vóór save: scan alle `grondslag.confidence` — downgrade elke `geciteerd`/`afgeleid`/`weerlegd` naar `verondersteld` of `betwijfeld`.

**AI-bron-vorm**:
```json
{"type": "ai_model", "naam": "claude-sonnet-4-6", "datum": "<vandaag>"}
```

---

## Scope-grenzen

- Wat MOET een **gecertificeerd accountant** weten over dit concept?
- **WEL** schrijven in deze operatie: definitie · economische substantie · ratio legis · mechanisme van het concept zelf · sub-concepten · wettelijke voorwaarden · concept-intrinsieke procedures (wat gebeurt er ongeacht wie kijkt — bv. schuldeisersbeschermingstermijn bij kapitaalvermindering).
- **NIET hier** schrijven: juridisch detail enkel voor notaris/jurist · inhoud die in ander concept-record thuishoort (check `records-index.compact.txt`).
- **NIET hier** schrijven, hoort in `accountant_perspectief`-operatie (= `inhoud.accountant_perspectieven`): boekhoudkundige verwerking + rekening-codes · audit-procedures · aangifte-stappen · advies-checklist · begeleidings-stappen. Zie *Plaatsingsregel* hieronder.

### Plaatsingsregel: "wat is het" vs "wat doet de accountant"

**Litmus-vraag**: "gebeurt dit ongeacht of er een accountant bij betrokken is?"
- **Ja** → top-level `inhoud.elementen[]` (concept-intrinsiek)
- **Nee, alleen als de accountant handelt** → `inhoud.accountant_perspectieven[].rollen[].elementen[]` (handelings-kennis)

| Inhoud | Plek |
|---|---|
| Boekhoudkundige verwerking · rekening-codes · boekingsmoment | `accountant_perspectieven` (rol=`boekhouder`) |
| Audit-procedures · risico-drempels · controle-aandachtspunten | `accountant_perspectieven` (rol=`auditor`) |
| Aangifte-codes · fiscale optimalisatie-stappen | `accountant_perspectieven` (rol=`fiscaal`) |
| Advies-checklist · alternatieven-afweging | `accountant_perspectieven` (rol=`adviseur`) |
| Begeleidings-stappen bij transactie/procedure | `accountant_perspectieven` (rol=`begeleider`) |
| Wettelijke voorwaarden van het concept zelf | `inhoud.elementen[]` |
| Mechanisme · sub-concepten · formules · concept-intrinsieke stappen | `inhoud.elementen[]` |

`accountant_perspectieven` zelf invullen gebeurt in operatie `accountant_perspectief`, **niet** in `beschrijven`. Hier in `beschrijven`: gewoon weglaten wat daar thuishoort.

---

## Top-level structuur — vier zones (NIET wijzigen aan identiteit)

```
id · naam · concept_type · schema_version        (identiteit — niet wijzigen)
metadata                                          (admin — alleen changelog/provenance bijwerken)
inhoud                                            (vul jij in deze operatie)
relaties                                          (top-level array, NIET binnen inhoud)
```

`metadata.ankers` (was `linked_anchors`) — niet wijzigen.

---

## `inhoud.kern` — verplicht ≥ 1 sub-veld

Nieuwe v1.5-structuur: definitie/substantie/rationale zitten gegroepeerd onder `inhoud.kern`:

```json
"inhoud": {
  "kern": {
    "definitie?":  { "tekst": "...", "grondslag": {...} },
    "substantie?": { "tekst": "...", "grondslag": {...} },
    "rationale?":  { "tekst": "...", "grondslag": {...} }
  }
}
```

- **`definitie`** (≤ 2 zinnen): wat IS het — juridisch hard of zacht; geen structuur-verschil.
- **`substantie`** (1 zin): wat betekent het economisch.
- **`rationale`** (1 alinea): waarom werkt het zo — student-vraag, mensentaal.

Per concept_type — welke sub-velden bij voorkeur (allemaal optioneel; ≥ 1 verplicht):

| Veld | instrument | verrichting | procedure | ratio | regime | balanspost | methode | kader | principe | actor |
|---|---|---|---|---|---|---|---|---|---|---|
| `definitie`  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `substantie` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |
| `rationale`  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |

---

## `tekst`-type (universele claim-eenheid)

Bron-van-eenheid voor elke claim — `tekstblok` en `contextitem` zijn weggevallen. Veld heet nu `tekst` (was `text`).

```json
{
  "tekst": "...",
  "grondslag": { "confidence": "verondersteld", "bronnen": [...] },
  "rationale?": "...",
  "weergaven?": [ weergave ],
  "relaties?": [ relatie ]
}
```

### CRITICAL — geen inline wettekst-citaten in proza

**Plaats GEEN art-nummers in `tekst`**:
- ❌ "Volgens art. 205bis WIB92 geldt..." in `definitie.tekst`
- ❌ "art. 7:194 WVV vereist..." in proza

**Wel**: wettekst-verwijzing als bron in `grondslag.bronnen[]`:

```json
{
  "tekst": "Het verlaagd tarief van 15% geldt op kwalificerende aandelen.",
  "grondslag": {
    "confidence": "betwijfeld",
    "bronnen": [
      {"type": "wettekst", "naam": "WIB92 art. 269 §1, 2°", "ref": "wib92-art-269-1-2", "datum": "2026-05-23"},
      {"type": "ai_model", "naam": "claude-sonnet-4-6", "datum": "2026-05-23"}
    ]
  }
}
```

Voor `beschrijven` (geen RAG):
- Art-nummer uit training-data bekend? → voeg als `wettekst`-bron toe met `confidence: "betwijfeld"` (nog niet gevalideerd; nooit `geciteerd`/`afgeleid`).
- Twijfelt? → laat art-nummer weg; alleen `ai_model`-bron met `verondersteld`. `claims_checken` voegt later art-refs toe na bron-validatie.

---

## `inhoud_type` enum (12 — v1.5 getrimd)

```
begrip · stap · drempel · regel · uitzondering · vuistregel · mechanisme
· risico · formule · principe · subconcept · beperking
```

**Geconsolideerd uit v1.4** (gebruik niet meer):
- `procedure_stap` + `stap_in_cyclus` → `stap`
- `component` → `subconcept`
- Gedropt (port naar passend type of weergave): `berekening` (→ `weergave` type `berekening`), `vergelijking` (→ `weergave` type `vergelijkingstabel` of relatie `vergelijkbaar_met`), `moment_in_tijd` (→ weglaten of `stap`), `eigenschap` (→ `begrip` of `subconcept`), `valkuil` (→ concept-niveau `inhoud.valkuilen[]`), `voorwaarde` (→ `inhoud.gebruikscontext.voorwaarden[]`), `keuze` (→ `inhoud.speelruimtes[]`).
- **Nieuw**: `beperking` — inherente zwakte van een indicator (bv. solvabiliteit-ratio negeert off-balance leasing).

Wanneer welk type:

| Type | Wanneer |
|---|---|
| `begrip` | Definiërende term, focus op WAT (bv. "verbonden vennootschap") |
| `stap` | Stap in sequentie — wet-gedreven of recurrent-cyclisch |
| `drempel` | Kwantitatieve grens (% / bedrag / jaren) die regime-overgang triggert |
| `regel` | Algemene normstelling met juridische kracht |
| `uitzondering` | Afwijking van algemene regel voor specifiek geval |
| `vuistregel` | Beroepswijsheid zonder formele bron, expert-rule-of-thumb |
| `mechanisme` | Hoe het economisch/juridisch werkt |
| `risico` | Wat kan misgaan + voor wie |
| `formule` | Wiskundige uitdrukking, ratio of bereken-recept |
| `principe` | Abstract beginsel met normatieve kracht |
| `subconcept` | Sub-onderdeel van het concept (was `component`) |
| `beperking` | Inherente zwakte van indicator/ratio/methode |

---

## `weergave_type` enum (11 — v1.5 getrimd)

```
proza · tabel · boeking · balans_snapshot · resultatenrekening_snapshot
· stappenlijst · tijdslijn · vergelijkingstabel · formule_expressie
· berekening · beslisboom
```

**Gedropt** (gebruik niet meer): `t_rekening` (→ `boeking`), `voorbeeld` (was geen weergave; nu top-level `voorbeeld`-type), `diagram` (te vaag — kies een specifieker type), `casus` (renamed naar `voorbeeld`).

---

## `element` — fractale recursie (zelfde shape als concept-niveau `inhoud`)

```json
{
  "id": "kebab-slug",
  "naam": { "primair": "..." },
  "inhoud_type": "<enum 12>",
  "kern": { "definitie?": tekst, "substantie?": tekst, "rationale?": tekst },  // ≥ 1 verplicht
  "weergaven?": [ weergave ],
  "elementen?": [ element ],            // recursie, max 3 niveaus diep
  "voorbeelden?": [ voorbeeld ],
  "valkuilen?": [ valkuil ],
  "speelruimtes?": [ speelruimte ]
}
```

**CRITICAL — geen lege schalen**: elk element moet ≥ 1 van `kern.definitie` / `kern.substantie` / `kern.rationale` gevuld hebben. Een element zonder enige proza-tekst is geen element.

**Niet meer gebruiken**:
- `element.beschrijving` (vervangen door `kern.definitie` / `kern.substantie`)
- `element.verwijst_naar` (vervangen door `relaties[]` op de relevante claim of element)

---

## `inhoud.gebruikscontext` — arrays overal

Alle sub-velden zijn nu ARRAYS (v1.4 had `trigger_start`/`trigger_einde`/`voordeel`/`risico` singular):

```json
"gebruikscontext": {
  "voor": [...], "niet_voor": [...],
  "voorwaarden": [...], "uitsluitingen": [...],
  "indicaties": [...], "contra_indicaties": [...],
  "trigger_start": [...], "trigger_einde": [...],
  "voordeel": [...], "risico": [...]
}
```

---

## `inhoud.voorbeelden` (unified) — top-level

`voorbeeld_inline` en `voorbeeld_case` zijn samengevoegd tot één `voorbeeld`-type:

```json
{
  "id?": "kebab-slug",         // optioneel; nodig als voorbeeld een anker krijgt
  "titel": "...",              // verplicht
  "context?": "NV ABC heeft...",
  "grondslag?": {...},
  "weergaven?": [...],
  "elementen?": [...]          // recursie
}
```

Voor `beschrijven`: skip voorbeelden — die komen in operatie `didactisch_verrijken`. Laat array leeg of weg.

---

## `inhoud.valkuilen` / `speelruimtes` / `syntheses` — concept-niveau didactisch

Nieuwe v1.5-secties. **Niet vullen in `beschrijven`** — komen in `didactisch_verrijken`.

- `valkuilen[]` — strikt: `{titel, verkeerde_assumptie, kernpunt, grondslag}`
- `speelruimtes[]` — wat je vrij kunt kiezen binnen de wet: `{titel, opties[{keuze, voordeel, nadeel?}], vuistregel?, grondslag}`
- `syntheses[]` (vervangt `keuzekader`) — `{type: keuzekader|tijdslijn|beslisboom|matrix|dashboard, intro?, inhoud}`

---

## `inhoud.accountant_perspectieven` (was `rollen_per_perspectief`)

Komt in operatie `accountant_perspectief`. **Niet vullen in `beschrijven`**.

---

## `relaties[]` (top-level, NIET binnen inhoud)

Voor `beschrijven`: suggesties OK (run `relaties_aanvullen` valideert + verrijkt). Twijfelt? Laat weg.

---

## Inputs

1. Skelet `/tmp/<fiche-id>.json` (al schema-valid; vul `inhoud`).
2. Schema `data/concepten/schema-2.1.schema.json` (structuur-anker — `$comment`/`description` per def is leading).
3. Records-index `data/concepten/records-index.compact.txt` (scope-anker; vermijd duplicatie, suggereer `valt_onder`/`vergelijkbaar_met`).

---

## Verboden

- Geen MCP-calls (`zoek_bronnen`/`lees_record`/etc.).
- Geen `content/experiment/*.md` raadplegen.
- Niet `wave_id` / `ankers` / `id` / `concept_type` aanpassen in metadata/identiteit.
- Geen `geciteerd`/`afgeleid`/`weerlegd` confidence.
- Geen inline wettekst-art-nummers in `tekst`-velden.
- Geen `element.beschrijving` / `element.verwijst_naar` (verouderd).
- Geen platte-dict / top-level weergaven / dict-source (oude Sonnet-pitfalls — zie schema-discipline).

---

## Werkwijze

1. Lees `/tmp/<fiche-id>.json` (skelet).
2. Lees `data/concepten/schema-2.1.schema.json` (let op `$comment`/`description` per `$def`).
3. Lees `data/concepten/records-index.compact.txt`.
4. Schrijf `inhoud.kern.{definitie,substantie,rationale}` (≥ 1).
5. Bouw `inhoud.elementen[]` (5-8 stuks, elk met `kern` gevuld).
6. Vul `inhoud.gebruikscontext` (arrays).
7. Suggesties voor `relaties[]` (top-level).
8. Schrijf record naar `/tmp/<fiche-id>.json` via Write-tool.
9. Update `metadata.provenance.model` + nieuwe entry in `metadata.changelog`:
   ```json
   {"operatie": "beschrijven", "timestamp": "<ISO>", "model": "<jouw-model>", "wave_id?": "..."}
   ```

**Tempo**: 1-3 min. Geen RAG = snel.

---

## Eindrapport

Vermeld:
- File-size + aantal `inhoud.elementen` + aantal relatie-suggesties.
- Confidence-mix (telling `verondersteld` vs `betwijfeld`).
- **Nieuwe types**: als je een `inhoud_type` of `weergave_type` mist dat niet in de enum staat, rapporteer hier (NIET in JSON gebruiken — orchestrator scant frequentie en bouwt schema-uitbreiding).
- Open vragen of twijfel die `claims_checken` moet oplossen.
