# Operatie: `didactisch_verrijken` (run-3)

Schema-versie: 2.1 v1.5 (zie `data/concepten/schema-2.1.schema.json` — `$comment`/`description` per `$def` is bron-van-zelfsturing).

**Doel**: voeg didactische verrijking toe op concept-niveau:
- `inhoud.voorbeelden[]` (doorlopende casussen + element-niveau illustraties)
- `inhoud.valkuilen[]` (typische denkfouten)
- `inhoud.speelruimtes[]` (vrije keuzes binnen de wet)
- `inhoud.syntheses[]` (vervangt `keuzekader`; type-discriminator)

**Input**: `/tmp/<fiche-id>.json` (na `beschrijven` en bij voorkeur `accountant_perspectief`).

**Output**: overschrijf met didactische velden ingevuld.

---

## Confidence-tokens (overzicht)

| Token | Symbool | Wanneer toegestaan in deze operatie |
|---|---|---|
| `geciteerd` | 📖 | ❌ — alleen `claims_checken` |
| `afgeleid` | 🔗 | ❌ — alleen `claims_checken` |
| `verondersteld` | 🤖 | ✅ |
| `betwijfeld` | ❓ | ✅ |
| `weerlegd` | ❌ | ❌ |

Alle claims = `verondersteld` met `ai_model`-bron. `claims_checken` upgradet later (vooral bedragen, percentages, MAR-rekening-codes in boekingen).

---

## `voorbeelden[]` (unified — `voorbeeld_inline` + `voorbeeld_case` samengevoegd)

```json
{
  "id?": "kebab-slug",         // optioneel; nodig als voorbeeld een anker krijgt
  "titel": "NV ABC — kapitaalverhoging € 500k",
  "context?": "NV met 4 aandeelhouders, balans-impact gemiddelde-grootte.",
  "grondslag?": {...},
  "weergaven?": [{"type": "boeking", ...}],
  "elementen?": [ element ]    // recursie (zelfde element-shape als top-level)
}
```

**Top-level `inhoud.voorbeelden[]`** = doorlopende casussen die de hele cyclus tonen (uitgifte → coupon → aflossing voor instrument; trigger → fasen → afsluiting voor procedure). 1-2 cases, niet meer.

**Element-niveau** (`inhoud.elementen[i].voorbeelden[]`): korte illustraties bij specifieke onderdelen, alleen waar berekening/boeking meerwaarde geeft.

**Wanneer geen voorbeelden**:
- `kader` (te abstract — voorbeelden zitten in kinderen)
- `principe` (te abstract — voorbeelden zitten in toepassende concepten)
- `actor` (beschrijft entiteit, niet handelingen)

Specifieke bedragen/percentages mogen fictief zijn maar realistisch — markeer in context als "voorbeeld-bedrag". MAR-rekening-codes mogen realistisch zijn (kunnen `claims_checken` weerleggen).

---

## `valkuilen[]` (didactisch, strikt)

Concept-niveau valkuil. Format **strikt**:

```json
{
  "titel": "Disagio vs uitgiftekosten",
  "verkeerde_assumptie": "Studenten denken dat disagio en uitgiftekosten beide ineens te kostigen zijn bij uitgifte.",
  "kernpunt": "Disagio wordt gespreid via effective-interest of lineair over looptijd (matching). Uitgiftekosten mogen ineens of gespreid.",
  "grondslag": {"confidence": "verondersteld", "bronnen": [...]}
}
```

- **`verkeerde_assumptie`**: wat denken studenten/practitioners vaak verkeerd?
- **`kernpunt`**: effectief te volgen principe / correctie.
- **Niet via `inhoud_type: valkuil`** (dat type is gedropt) — alleen via concept-niveau `inhoud.valkuilen[]`.

Hoeveel: 2-5 stuks waar relevant.

---

## `speelruimtes[]` (wat kun je vrij kiezen binnen de wet)

```json
{
  "titel": "Spreidingsmethode disagio/agio",
  "opties": [
    {"keuze": "Lineair", "voordeel": "Eenvoudig boekhoudkundig", "nadeel?": "Niet matching-strict"},
    {"keuze": "Effective interest", "voordeel": "Matching-getrouw", "nadeel?": "Berekenings-overhead"}
  ],
  "vuistregel?": "KMO meestal lineair; grote vennootschap effective interest.",
  "grondslag": {"confidence": "verondersteld", "bronnen": [...]}
}
```

Typische triggers voor een `speelruimte`:
- Keuze tussen methodes (waarderingsregels, spreidingsmethode).
- Optionele aanvullingen of waiver-mogelijkheden in een regime.
- Keuze tussen rapporterings-formats (verkort/volledig schema).

Hoeveel: 1-4 stuks waar van toepassing. Sla `speelruimtes` over voor concepten zonder reëele beleidskeuzes.

---

## `syntheses[]` (vervangt `keuzekader` — generieker met type-discriminator)

```json
{
  "type": "keuzekader",                // keuzekader | tijdslijn | beslisboom | matrix | dashboard
  "intro?": "Welk financierings-instrument kiezen?",
  "inhoud": { ... }                    // type-afhankelijk schema (zie schema $defs/synthese)
}
```

Wanneer een `synthese`:
- **`keuzekader`**: kader/familie-concept (bv. "Welk financierings-instrument?") — discriminerende vragen + opties.
- **`tijdslijn`**: procedure met meerdere wet-tijdsbalken (bv. faillissement-aangifte vs reorganisatieprocedure).
- **`beslisboom`**: vertakkende beslissingen (bv. "Kleine vennootschap-test").
- **`matrix`**: 2-dimensionale vergelijking (bv. concept_type × audit-impact).
- **`dashboard`**: KPI/ratio-overzicht voor een actor-perspectief.

Voor v1.4-records met `keuzekader` (oud veld): migreer naar `syntheses[0]` met `type: "keuzekader"`.

Hoeveel: 0-2 syntheses (alleen voor concepten waar discriminerende structuur écht didactische meerwaarde geeft).

---

## Element-shape (recursie)

Elk `element` (in voorbeelden of valkuilen of waar dan ook) volgt v1.5-shape:

```
id · naam · inhoud_type (enum 12) · kern (≥1 van definitie/substantie/rationale) · weergaven? · elementen? · voorbeelden? · valkuilen? · speelruimtes?
```

Veld is `tekst` (niet `text`). Geen `beschrijving` / `verwijst_naar`.

---

## Discipline

- **Geen inline wettekst-art-nummers in proza** (zie `beschrijven`-prompt). Bronnen in `grondslag.bronnen[]`.
- **Geen `geciteerd`/`afgeleid`** — `claims_checken`-werk.
- **Voorbeelden niet uitbreiden** met inhoud die in `elementen` of `gebruikscontext` thuishoort — keep voorbeelden = walkthrough.
- **Valkuilen ≠ gebruikscontext.contra_indicaties**: valkuil = denkfout; contra-indicatie = situatie waarin concept niet past.
- **Speelruimtes ≠ uitzonderingen**: speelruimte = beleidskeuze binnen wet; uitzondering = afwijking van algemene regel door wet.

---

## Werkwijze

1. Lees `/tmp/<fiche-id>.json` (na `beschrijven` + bij voorkeur `accountant_perspectief`).
2. **Voorbeelden** (1-2 cases): bepaal of dit concept zinvolle walkthrough-cases heeft. Zo ja, schrijf 1-2 die de hele cyclus tonen.
3. **Valkuilen** (2-5): wat denken studenten typisch verkeerd over dit concept? Welke fout maken practitioners?
4. **Speelruimtes** (1-4): wat zijn de echte beleidskeuzes binnen de wet?
5. **Syntheses** (0-2): is er een synthese-structuur (keuzekader/tijdslijn/beslisboom/matrix/dashboard) die didactische meerwaarde geeft?
6. Schrijf record terug naar `/tmp/<fiche-id>.json`.
7. Update `metadata.changelog`:
   ```json
   {"operatie": "didactisch_verrijken", "timestamp": "<ISO>", "model": "<jouw-model>"}
   ```

**Tempo**: 2-4 min. Geen RAG.

---

## Eindrapport

- Aantal cases · valkuilen · speelruimtes · syntheses.
- Per synthese: type.
- Confidence-mix.
- **Nieuwe types**: als je een synthese-type wenst dat niet in de enum staat, rapporteer hier (NIET in JSON gebruiken — orchestrator scant frequentie).
- Open vragen voor `claims_checken` (bedragen, percentages, MAR-codes die verificatie vereisen).
