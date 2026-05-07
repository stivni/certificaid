# ADR-008: Concept-extractie

**Status**: Draft
**Datum**: 2026-05-07 · **Bijgewerkt**: 2026-05-07 (extractie-volgorde, vermoedensruimte, examen-driven naar Fase 5)

## Context

Concepten ontstaan niet vanzelf. Drie ingangen leveren materiaal, en geen van de drie alleen volstaat:

- **Het examenprogramma** zegt *welke* concepten nodig zijn (scope), niet *wat* ze inhouden. Belangrijk: niet alleen kenniselementen leveren input — ook **taken** (wat de accountant doet) en **doelstellingen** (wat hij moet kunnen). Alleen kenniselementen indexeren laat de procedurele kant onbelicht.
- **Bronnen** leveren juridische inhoud, maar niet alle bronnen zijn even gezagsvol en niet alle relevante kennis staat letterlijk in een artikel.
- **Voorbeeldexamens** tonen de toetsings-realiteit (welke diepte, welke uitzonderingen worden bevraagd), maar als je extractie alleen daarop baseert loop je met oogkleppen — je dekt enkel wat eerder gevraagd werd.

Daarom: programma-gestuurd + bron-gestuurd in Fase 3 (initiële conceptenset), examen-gestuurd pas in Fase 5 (validatie + gerichte bijbouw). Iteratief proces dat het schema kan laten evolueren wanneer nieuw soort kennis niet past.

## Beslissing

### 1. Drie ingangen, gefaseerd ingezet

| Ingang | Vraag | Wanneer | Werkwijze |
|---|---|---|---|
| **Programma-gestuurd** | Welke concepten dekken dit taakblok / kenniselement? | Fase 3 | Vermoedensruimte → multi-level retrieval → seed-records → verdieping |
| **Bron-gestuurd** | Welke fenomenen zitten in deze bron die we nog niet hebben? | Fase 3 (parallel) | Iteratieve scan van bron-MD's met concept-spotting prompt |
| **Examen-gestuurd** | Welke concepten waren nodig om deze vraag op te lossen? Wat ontbreekt nog? | **Fase 5 cross-cutting** | Voorbeeldexamen-vraag oplossen met huidige conceptenset → gat = uitbreiding |

**Waarom examen-driven naar Fase 5**: het is niet zinvol om examenvragen als extractie-input te gebruiken voordat een werkende basis-conceptenset bestaat. Anders ontstaat circulaire bias ("ik maak concepten zodat dít examen oplosbaar is" ≠ "ik maak concepten zodat de student het domein begrijpt en daarmee elk examen aankan"). In Fase 5 wordt examen-driven een **validator** ("kan de huidige conceptenset deze vraag oplossen?") en pas bij gaps een gerichte extra extractie-input.

### 2. Programma-gestuurde extractie — vier fases

```
A. Vermoedensruimte genereren (LLM, geen retrieval)
   ↓
B. Multi-level retrieval per vermoeden
   ↓
C. Seed-records bouwen (LLM-synthese)
   ↓
D. Verdieping per concept (iteratief)
```

#### A. Vermoedensruimte

LLM krijgt:
- Programmaonderdeel-titel + parent-context
- Eén taakblok in zijn geheel: taken + doelstellingen + kenniselementen
- Conceptmodel-schema (node-types + edge-types)
- Concept-schrijfregels (`docs/concept-schrijfregels.md`)
- Lijst van bestaande concept-naburen (om duplicatie te vermijden)

Output: 10–30 vermoedens per taakblok, elk met (a) voorgestelde naam, (b) voorgesteld node-type, (c) waarom-vermoed-gepost-aan-welk-onderdeel-van-het-taakblok. Géén main_rule/exceptions nog — pure vermoedensruimte.

LLM mag een **niet-voorgedefinieerd node-type voorstellen** (`node_type: "voorgesteld:<naam>"`). Voorgestelde types verzamelen in review-queue (ADR-007).

#### B. Multi-level retrieval

Per vermoeden retrieval op drie niveaus tegen `bronnen`-collection (ADR-006):

1. **Programmaonderdeel-niveau**: het hele programmaonderdeel-document als query → "thematische" chunks (overzicht van het domein)
2. **Taakblok-niveau**: taken + doelstellingen + kenniselementen samen als query → mid-level
3. **Vermoeden-niveau**: de vermoeden-naam + LLM-gegenereerde sub-queries → granulair

Multi-query retrieve via `tools/lib/retrieval.py::multi_query_retrieve` (bestaat al). Optioneel: `bron_rol`-filter voor brontype-targeting per vermoeden.

#### C. Seed-records bouwen

LLM krijgt per vermoeden:
- Het vermoeden + parent-context (taakblok + programmaonderdeel)
- 15–30 chunks uit de retrieval (met breadcrumb + path-metadata)
- Concept-schrijfregels (geladen via `docs/concept-schrijfregels.md`)
- Conceptmodel-schema

Output: seed-record met **alleen velden die uit de chunks gerechtvaardigd zijn**:
- `id`, `naam`, `node_type`, `source`
- `main_rule` of `definitie` (verbatim/paraphrase met `confidence: "grounded"` + bronverwijzing)
- Initiële `edges` (mogelijk `_dangling: true`)
- Status: `seed`

Velden die niet gerechtvaardigd zijn blijven leeg. Sparse fields zijn de norm (ADR-007).

#### D. Verdieping per concept

Voor elke seed → status `partieel`:
- **Verdiepende retrieval-queries** met cumulatieve concept-state als input:
  - Concept-naam + synoniemen
  - Bestaande veld-content (`main_rule`, `exceptions`) als context
  - Edge-targets (gerelateerde concept-namen)
  - LLM-multi-query-expansion op basis van wat al gekend is
- LLM vult `exceptions`, `scope`, edge-targets verder in
- Dangling-edges → seed-queue voor volgende extractie-ronde

Status `gevuld` (later, eventueel handmatig of via tweede LLM-pass): `pitfalls`, `voorbeeld_inline`. Examen-driven cases komen pas in Fase 5.

### 3. Bron-gestuurde extractie

Iteratieve scan over bron-MD's: voor elk artikel/sectie laat een concept-spotting prompt LLM een lijst opstellen van fenomenen die in deze passage opduiken die nog géén concept zijn. Output convergeert in dezelfde `data/concept_records/`-map; dedupe via concept-id-similarity.

Anti-explosie-regel: bron-driven mag geen concepten genereren die buiten de scope van enige programmaonderdeel-kenniselement vallen — anders extraheer je de hele wet. Cap via "moet aan minstens één kenniselement koppelbaar zijn" (heuristiek, geen hard filter).

### 4. Examen-gestuurde extractie (Fase 5)

Pas wanneer een werkende conceptenset bestaat:
- Voorbeeldexamen-vraag oplossen met huidige concepten + bronnen-RAG
- Concepten die de oplossing nodig had: tag als `voorbeeldvraag-id` in concept-record (link naar voorbeeldexamen-record)
- Concepten die ontbraken (oplossing miste detail): markeer voor uitbreiding, voeg `pitfalls`/`voorbeeld_inline` toe op basis van vraag-redenering

Anti-oogkleppen-regel: examenvraag = **toetsings-instantie van een breder concept** (een examenfocus, ADR-009), géén concept op zich. Voorbeeld: "wanneer is melding aan CFI verplicht?" → instantie van `meldingsplicht-cfi`, niet een nieuw concept "wanneer-melding-CFI".

### 5. Confidence-labeling per veld

Elk veld erft een `confidence` string-tag (zie ADR-007 voor waarden — `"grounded"` / `"inferred"`):
- `bron_rol` van de chunks waaruit het is afgeleid (`itaa-lex`, `wettekst`, `norm` → `grounded`)
- Type extractie-stap (verbatim/paraphrase → `grounded`; geconstrueerde redenering → `inferred`)

Een veld zonder bronverwijzing krijgt nooit stilzwijgend `grounded`.

### 6. Per-veld provenance

Concept-record `_provenance` wordt fijnmaziger dan een file-level blok:

```json
"_provenance": {
  "main_rule": {
    "inputs": [{"id": "Antiwitwaswet-2017__art_5", "sha256": "...", "version": "etl-v1.2"}],
    "tooling": {"pipeline": "concept_extractor", "pipeline_version": "abc1234", "model": "claude-sonnet-4", "prompt_version": "extract-seed-v1"},
    "generated_at": "2026-05-08T12:00:00Z"
  },
  "exceptions": { ... mogelijk andere chunks ... }
}
```

Bij **bron-update** (chunk-content-hash verandert) → `mark_stale.py` walkt: welke concept-records hebben deze chunk-id als input voor welk veld? → die velden worden `stale: true`. Andere velden in hetzelfde concept blijven valide. Re-extraction-queue verzamelt stale velden.

Vereist **chunk-id-stabiliteit** (ADR-006 §3.1, ADR-004).

### 7. Schema-evolutie tijdens extractie

Wanneer een concept niet past in het huidige conceptmodel:
- Extractor genereert expliciet schema-uitbreidingsvoorstel (nieuw veld, nieuw node-type, nieuw edge-type)
- Voorstel landt in `data/concept_records/_voorgestelde_types.yaml` (zie ADR-007)
- Pas na menselijke bevestiging wordt het schema bijgewerkt; de extractor slaat het concept ondertussen als `partieel` op met een notitie

## Gevolgen

- `tools/extractie/concept_extractor.py` — orchestrator met sub-commands per fase (vermoedensruimte / multi-level-retrieval / seed-bouw / verdieping)
- `tools/extractie/queue.py` — dangling-edges → seed-queue
- `tools/lib/coverage.py` — bouwt op aanvraag een reverse-index (concept → kenniselementen) uit programmaonderdeel-JSON's voor dekkingsrapporten. Geen state op concepten zelf (ADR-002, ADR-007).
- LLM-cost: extractie is duur. Per-veld provenance + per-veld stale-marking maakt incremental re-runs **veld-precies** (alleen stale velden herextraheren, niet hele concept-records).
- Voorbeeldexamens worden vroeg gestructureerd (`data/voorbeeldexamens/`) als ground truth — maar pas in Fase 5 als extractie-input gebruikt
- Concept-schrijfregels (`docs/concept-schrijfregels.md`) als prompt-input bij elke LLM-call
