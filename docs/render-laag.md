# Render-laag — schema 2.1 v1.5

Spec voor de render-laag (Quartz/markdown) die concept-records van schema 2.1 v1.5 omzet naar leerbare fiches.

**Bron-van-waarheid schema**: [`data/concepten/schema-2.1.schema.json`](../data/concepten/schema-2.1.schema.json)
**Canonieke spec v1.5**: [`docs/schema-v15-besluit.md`](schema-v15-besluit.md) — geconsolideerd referentie-document met alle 21 besluiten + finale structuur + operations-model
**Design-rationale**: [`docs/adr/ADR-029-schema-21-operaties-model.md`](adr/ADR-029-schema-21-operaties-model.md)
**Werk-tracking**: [`docs/TODO.md`](TODO.md) §Fase 7

---

## Kernprincipes voor de render-laag

1. **Schema 2.1 v1.5 is de finale data-laag** — 396 records in v1.5-shape (legacy v2.0 records in `data/concepten/_archive/`).
2. **Render-laag mapt abstracte schema-keys naar Nederlandse labels** — schema heeft `mechanisme` (niet "hoe het werkt"), `gebruikscontext` (niet "wanneer kies je dit"). Render kent labels per `concept_type`.
3. **`kern`-wrapper omvat de drie "wat-is-dit"-claims** — `inhoud.kern.{definitie?, substantie?, rationale?}`. Idem voor elk `element` (fractale recursie).
4. **Confidence-iconen per claim** — elke claim heeft `grondslag.confidence ∈ {geciteerd, afgeleid, verondersteld, betwijfeld, weerlegd}`. Render toont icoon: 📖 / 🔗 / 🤖 / ❓ / ❌.
5. **`relaties` op top-level**, niet in `inhoud`. Render bouwt cross-link-pagina's.
6. **Operations-model**: `metadata.changelog[]` toont welke operaties zijn uitgevoerd. Render kan kwaliteits-meter tonen.
7. **Drie didactische arrays op concept-niveau**: `valkuilen[]`, `speelruimtes[]`, `syntheses[]`.

---

## Schema 2.1 v1.5 — top-level structuur

```json
{
  "id": "kapitaalvermindering",                    // kebab-slug
  "naam": {                                         // recursief overal toepasbaar
    "primair": "Kapitaalvermindering",
    "afkorting?": "...",
    "synoniemen?": [...],
    "vertaling?": {"en": "..."}                    // ← was "andere_talen" in v1.4; vertaling? optioneel
  },
  "concept_type": "verrichting",                   // 10 waarden: instrument | verrichting | procedure | balanspost | ratio | regime | methode | kader | principe | actor
  "schema_version": "2.1",

  "metadata": {
    "status": "seed | gevalideerd | te_herzien",
    "ankers": ["1.1.II.T", "3.0.IV"],              // ← unified (was linked_anchors + dekt_tdks in v1.4)
    "provenance": { "model": "...", "wave_id": "..." },
    "changelog": [
      {
        "operatie": "beschrijven",                  // verplicht
        "timestamp": "2026-05-23T...",
        "model": "claude-sonnet-4-5",
        "wave_id?": "wave-2-20260523",
        "wijziging?": "...",
        "metriek?": {...}
      }
    ]
  },

  "inhoud": {
    "kern": {                                       // ← NIEUW: wrapper voor de 3 "wat-is-dit"-claims; ≥1 verplicht
      "definitie?":  { "tekst": "...", "grondslag": {...}, "weergaven?": [...], "relaties?": [...] },
      "substantie?": { ... },                       // economische substantie
      "rationale?":  { ... }                        // waarom werkt het zo
    },
    "voorkennis_leespad?": { ... },                 // ingevuld door `leespad_aanvullen`-operatie
    "gebruikscontext?": {                           // ALLE sub-velden zijn nu arrays
      "voor": [...], "niet_voor": [...],
      "voorwaarden": [...], "uitsluitingen": [...],
      "indicaties": [...], "contra_indicaties": [...],
      "trigger_start": [...], "trigger_einde": [...],
      "voordeel": [...], "risico": [...]
    },
    "elementen?":  [ element ],                     // fractale recursie (zelfde shape als concept-niveau-inhoud)
    "voorbeelden?": [ voorbeeld ],                  // unified (was voorbeeld_inline + voorbeeld_case)
    "valkuilen?": [ valkuil ],                      // ← NIEUW didactisch
    "speelruimtes?": [ speelruimte ],               // ← NIEUW didactisch
    "accountant_perspectieven?": [ perspectief ],   // ← HERNOEMD (was rollen_per_perspectief.perspectieven[])
    "syntheses?": [ synthese ]                      // ← VERVANGT keuzekader; met type-discriminator
  },

  "relaties": [                                     // top-level concept-naar-concept graph
    { "type": "...", "target": "...", "grondslag?": {...}, "toelichting?": "..." },
    { "type": "vergelijkbaar_met", "target": "...", "gelijkenissen": [...], "verschillen": [...], "verwarring_risico?": "...", "render_hint?": "..." }
  ]
}
```

### Sub-structuren

**`tekst`-type** (universele bron-van-eenheid voor elke claim):
```json
{
  "tekst": "...",                          // ← was "text" in v1.4
  "grondslag": { "confidence": "...", "bronnen": [...], "checked_at?": "...", "claim_hash?": "...", "weerlegging?": "..." },
  "rationale?": "...",                     // optioneel — waarom-deze-claim
  "weergaven?": [ weergave ],
  "relaties?": [ relatie ]                 // inline-relaties vanaf deze claim
}
```

**`element`** (fractale recursie — gelijke shape als concept-niveau-inhoud):
```json
{
  "id": "kebab-slug",
  "naam": { "primair": "..." },
  "inhoud_type": "<enum 12>",              // begrip | stap | drempel | regel | uitzondering | vuistregel | mechanisme | risico | formule | principe | subconcept | beperking
  "kern": {                                // ← idem als concept-niveau; ≥1 verplicht
    "definitie?":  tekst,
    "substantie?": tekst,
    "rationale?":  tekst
  },
  "weergaven?": [ weergave ],
  "elementen?": [ element ],               // recursie max 3 niveaus
  "voorbeelden?": [ voorbeeld ],
  "valkuilen?": [ valkuil ],
  "speelruimtes?": [ speelruimte ]
}
```

Geen `beschrijving` meer (zat in v1.4 maar nu vervangen door `kern`). Geen `verwijst_naar` meer (relateert via `relaties[]` op claims).

**`voorbeeld`** (unified):
```json
{
  "id?": "kebab-slug",
  "titel": "...",
  "context?": "...",                       // intro-tekst ("NV ABC heeft...")
  "grondslag?": { ... },
  "weergaven?": [ weergave ],
  "elementen?": [ element ]                // recursie naar stap-elementen
}
```

**`valkuil`** (didactisch — vaak verkeerd gedacht):
```json
{
  "titel": "...",
  "verkeerde_assumptie": "...",
  "kernpunt": "...",
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
  "vuistregel?": "...",
  "grondslag": { ... }
}
```

**`synthese`** (vervangt v1.4 `keuzekader`):
```json
{
  "type": "keuzekader | tijdslijn | beslisboom | matrix | dashboard",
  "intro?": "...",
  "inhoud": { ... }                        // type-afhankelijk payload-schema
}
```

**`accountant_perspectieven`** (vereenvoudigde hiërarchie — 1 nesting-laag weg t.o.v. v1.4):
```json
[
  {
    "id": "uitgever-vennootschap",
    "naam": { "primair": "Uitgevende vennootschap" },
    "rollen": [
      {
        "rol": "adviseur | boekhouder | begeleider | fiscaal | auditor",
        "elementen": [ element ]
      }
    ]
  }
]
```

(In v1.4 zat dit als `inhoud.rollen_per_perspectief.perspectieven[]` — nu rechtstreeks `inhoud.accountant_perspectieven[]`.)

---

## Render-mapping per `concept_type`

Render-laag moet **labels kiezen per concept_type** uit dezelfde schema-velden. Voorbeeld:

| Schema-veld | `instrument` | `verrichting` | `procedure` | `regime` | `ratio` | `kader` | `methode` |
|---|---|---|---|---|---|---|---|
| `kern.definitie` | "Definitie" | "Definitie" | "Definitie" | "Definitie" | "Wat meet de ratio" | "Definitie" | "Aanpak" |
| `kern.substantie` | "Wat er economisch echt gebeurt" | "Economische substantie" | "Wat de procedure oplost" | "Wat het regime doet" | "Wat de indicator weergeeft" | — | "Wat de methode opzet" |
| `kern.rationale` | "Achterliggende logica" | "Waarom deze verrichting" | "Waarom dit verloop" | "Waarom dit regime" | "Waarom deze ratio" | "Achterliggende denkraam" | "Waarom deze aanpak" |
| `gebruikscontext` | "Wanneer kies je dit?" | "Wanneer deze verrichting?" | "Wanneer getriggerd?" | "Wanneer is dit van toepassing?" | "Wanneer gebruiken?" | — | "Wanneer pas je deze methode toe?" |
| `elementen` | "Onderdelen" | "Verloop" | "Procedure-stappen" | "Werking" | "Berekening + interpretatie" | "Componenten" | "Stappen" |
| `valkuilen` | "Vaak verkeerd gedacht" | idem | idem | idem | idem | idem | idem |
| `speelruimtes` | "Wat kun je kiezen?" | idem | idem | idem | idem | idem | idem |
| `syntheses[type=keuzekader]` | — | — | — | — | — | "Welke variant kiezen?" | "Welke aanpak kiezen?" |

**Render-data location**: suggestie YAML/JSON-mapping `tools/leermateriaal/render_labels.yaml` of inline in Jinja-template per concept_type.

---

## Confidence-tokens + render-iconen (onveranderd uit v1.4)

| Token | Wanneer | Render-icoon | Kleur (suggestie) |
|---|---|---|---|
| `geciteerd` | (quasi-)letterlijk in bron, parafrase OK | 📖 | groen |
| `afgeleid` | af te leiden uit ≥2 bronnen | 🔗 | blauw |
| `verondersteld` | AI/mens-aanname zonder citaat, redelijke zekerheid | 🤖 (ai_model bron) of 🧠 (mens-bron) | geel |
| `betwijfeld` | claim met expliciete twijfel | ❓ | oranje |
| `weerlegd` | bron tegenspreekt, claim nog niet gecorrigeerd | ❌ | rood |

**Belangrijk voor render**: agent kan in `beschrijven`-operatie alleen `verondersteld` of `betwijfeld` produceren. `geciteerd`/`afgeleid`/`weerlegd` komen pas na `claims_checken`. Render moet daarom student bewust maken dat `verondersteld`-claims **mogelijk hallucinatie zijn**.

---

## Operations-model (v1.5 — uit ADR-029 + besluit-document)

Records evolueren via **willekeurig-toepasbare operaties** ipv vaste runs. Zeven operaties actief uitgewerkt:

| Operatie | Wat verbetert |
|---|---|
| `beschrijven` | inhoud uitvullen (eerste pas) — alleen `verondersteld`/`betwijfeld` |
| `claims_checken` | RAG-validatie, confidence-upgrade naar `geciteerd`/`afgeleid` of flag `weerlegd` |
| `relaties_aanvullen` | `vergelijkbaar_met` + bevat-edges rijk maken |
| `accountant_perspectief` | `accountant_perspectieven[]` per relevante actor invullen |
| `didactisch_verrijken` | `valkuilen[]`, `speelruimtes[]`, `voorbeelden[]` toevoegen; `rationale` expandeert |
| `kandidaat_review` | proeflezen door studentbril, gaps signaleren |
| `leespad_aanvullen` | `inhoud.voorkennis_leespad` invullen op basis van anker-positie + vereist-relaties |

(`cijfer_validatie`, `examenvragen_aansluiting`, `consistentie_check`, `volledigheid_check` blijven op de roadmap maar niet prioritair voor wave-2.)

**Voor render**: per record toon welke operaties zijn uitgevoerd (kwaliteit-indicator). Een record met alleen `beschrijven` = "draft"; met `+claims_checken` = "bron-gevalideerd"; etc. State leeft in `metadata.changelog[].operatie` — render kan daaruit een unieke set afleiden.

---

## Fractale recursie als render-principe

`element` heeft in v1.5 **dezelfde shape** als concept-niveau-`inhoud`: een element mag zelf `elementen[]`, `voorbeelden[]`, `valkuilen[]`, `speelruimtes[]`, `weergaven[]` bevatten plus een eigen `kern`-wrapper. Render-template kan dus dezelfde component recursief instantiëren tot max 3 niveaus diep.

Praktische gevolgen voor render:
- Eén `<ElementBlock>`-component die zichzelf recursief aanroept
- Conditional rendering: skip lege sub-arrays
- Indentatie/collapse per niveau om diep geneste records leesbaar te houden

---

## Render-todos voor de nieuwe sessie

### A. Template-update (Quartz custom)

1. **`quartz-custom/components/ConceptFiche.tsx`** (of equivalent): rebuild voor schema 2.1 v1.5
2. **Render-mapping**: implementeer `concept_type × inhoud-key → label` (zie tabel hierboven)
3. **`kern`-wrapper rendering**: `definitie`/`substantie`/`rationale` als drie cards/secties, conditional op aanwezigheid
4. **Confidence-icoon per claim**: walk-through `grondslag.confidence` overal in `inhoud`/`relaties`
5. **Conditional rendering**: skip lege secties (kern.definitie OK, substantie optioneel, etc.)

### B. Concept-specifieke views

6. **`elementen` fractale recursie**: max 3 niveaus diep; collapsible sub-elementen — één component voor alle niveaus
7. **`weergaven` per element/claim**: type-specifieke render (boeking → t-rekening style; balans_snapshot → kolommen; formule_expressie → LaTeX/KaTeX; etc.). 11 types in v1.5.
8. **`accountant_perspectieven`**: matrix-view (perspectief horizontaal × rol verticaal? of accordion-per-perspectief?)
9. **`voorbeelden`**: walkthrough-style (titel + context + weergaven + element-stappen)
10. **`valkuilen` / `speelruimtes`**: aparte didactische blokken (waarschuwingsbox voor valkuilen, keuze-tabel voor speelruimtes)
11. **`syntheses`**: type-specifieke render — `keuzekader` als beslisboom of vergelijkingstabel; `tijdslijn` als horizontale tijdsbalk; etc.

### C. Cross-record navigatie

12. **`relaties` → backlinks-pagina**: per record toon "valt_onder", "bevat", "vergelijkbaar_met" enz. Auto-derive omgekeerden (`getriggerd_door`, `bevat`↔`valt_onder`, etc.) — niet in data, render bouwt.
13. **`vergelijkbaar_met` rijk**: render `gelijkenissen` + `verschillen` als 2-kolom-tabel. `verwarring_risico` als waarschuwingsblok.

### D. Status + operatie-tracking

14. **Operaties-historiek-balk**: toon timeline van uitgevoerde operaties uit `metadata.changelog[]` (📋 beschrijven · ⚖️ claims_checken · 🎯 accountant_perspectief · ...).
15. **Status-badge per record**: afgeleid uit unieke set operaties. Bv. "draft" als alleen `beschrijven`; "gevalideerd" als ≥3 operaties incl. `claims_checken` + `kandidaat_review`.

### E. Markdown-bridge

16. **JSON → markdown render-script**: huidige `tools/leermateriaal/render_concept_fiche.py` is voor schema 2.0 (legacy). Schrijf nieuw voor schema 2.1 v1.5 — input JSON, output Quartz-friendly markdown.

---

## Open beslispunten voor render-sessie

1. **Label-mapping locatie**: YAML `tools/leermateriaal/render_labels.yaml` of inline in Jinja-template?
2. **Confidence-icoon plaatsing**: inline naast tekst, of in apart "betrouwbaarheid"-badge per claim?
3. **`relaties` rendering**: aparte sectie onderaan, of geïntegreerd in body waar relevant?
4. **`voorbeelden` met `betwijfeld`-claims**: tonen of verbergen tot factcheck?
5. **Operatie-historiek**: nodig dat student de wijzigingen-geschiedenis ziet, of alleen huidig?
6. **Mobile vs desktop**: keuzekader-tabel responsief? Fractale elementen-recursie inklapbaar op mobile?
7. **`valkuilen`/`speelruimtes` plaatsing**: bovenaan (didactisch eerst) of onderaan (na de hard content)?

---

## Render-test-set

Eén record per `concept_type` voor template-coverage:

- `kapitaalvermindering` (verrichting, multi-pass-rijk — happy path)
- `aangifte-pb` (procedure, 7 stappen)
- `algemene-vergadering` (kader, met synthese/keuzekader)
- `achtergestelde-lening` (instrument)
- `liquidatiereserve` (regime)
- `current-ratio` (ratio, met formule_expressie)

---

## Wat is bevroren, wat verandert nog

**Bevroren** (schema 2.1 v1.5 — 23 mei 2026):
- Top-level 4-zone-structuur (id/naam/concept_type/schema_version + metadata/inhoud/relaties)
- `inhoud.kern`-wrapper met definitie/substantie/rationale
- Fractale recursie van `element` (gelijke shape als concept-niveau-inhoud)
- Confidence-token-enum (5 waarden)
- `inhoud_type` (12) + `weergave_type` (11)
- `accountant_perspectieven`-shape (1 nesting-laag minder)
- Operations-model met 7 actieve operaties
- `valkuilen[]`, `speelruimtes[]`, `syntheses[]` arrays

**Open (na wave-2 mogelijk gewijzigd)**:
- Detail-schemas per `weergave_type` (`boeking`/`balans_snapshot`/`tabel` krijgen payload-validatie)
- Eventuele nieuwe `inhoud_type`/`weergave_type`-waarden uit agent-eindrapporten
- `accountant_perspectieven` rol-element-sturing (E3 — open beslispunt)

---

## Bestanden voor de render-laag

| Pad | Wat |
|---|---|
| `data/concepten/schema-2.1.schema.json` | **Bron-van-waarheid schema** (v1.5) |
| `docs/schema-v15-besluit.md` | **Canonieke spec v1.5** — alle 21 besluiten + finale structuur |
| `docs/adr/ADR-029-schema-21-operaties-model.md` | Design-rationale + changelog v1.0 → v1.5 |
| `data/concepten/records/*.json` | 396 records in v1.5-shape |
| `tools/leermateriaal/render_concept_fiche.py` | **Legacy** render-script voor schema 2.0 — niet gebruiken; herschrijven |
| `content/concepten/*.md` | **Legacy** Quartz-rendered records (schema 2.0) |
