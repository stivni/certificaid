# ADR-008: Concept-extractie

**Status**: Draft
**Datum**: 2026-05-07

## Context

Concepten ontstaan niet vanzelf. Drie ingangen leveren materiaal, en geen van de drie alleen volstaat:

- **Het examenprogramma** zegt *welke* concepten nodig zijn (scope), niet *wat* ze inhouden
- **Bronnen** leveren juridische inhoud, maar niet alle bronnen zijn even gezagsvol en niet alle relevante kennis staat letterlijk in een artikel
- **Voorbeeldexamens** tonen de toetsings-realiteit (welke diepte, welke uitzonderingen worden bevraagd), maar als je extractie alleen daarop baseert loop je met oogkleppen — je dekt enkel wat eerder gevraagd werd

Daarom: alle drie de ingangen samen, in een iteratief proces dat het schema kan laten evolueren wanneer nieuw soort kennis niet past.

## Beslissing

### 1. Drie ingangen, gecombineerd

| Ingang | Vraag | Werkwijze |
|---|---|---|
| **Programma-gestuurd** | Welke concepten dekken dit kenniselement? | Per kenniselement: bronnen-RAG + LLM-prompt → kandidaat-concepten |
| **Bron-driven** | Welke concepten zitten verborgen in deze bron? | Bronnen-RAG iteratief met concept-spotting prompt; output = kandidaten + dangling-edges |
| **Examen-driven** | Welke concepten waren nodig om deze vraag op te lossen? | Voorbeeldexamen-vraag oplossen met huidige concepten + bronnen-RAG; gat = nieuw concept of uitbreiding |

De drie ingangen draaien parallel; hun output convergeert op dezelfde `data/concept_records/` map.

### 2. Iteratief proces

```
Trigger (kenniselement / open vraag / dangling-edge)
  → Bronnen-RAG (en concepten-RAG voor context)
  → Eerste extractie: node + edges (status `partieel` of `gevuld`)
  → Dangling-edges → seed-queue voor volgende ronde
  → Schema-feedback: nieuw soort kennis past niet → schema uitbreiden (ADR-007)
                                                   → bestaande records waar nodig stale-markeren
```

Elke ronde produceert provenance-volledige records (ADR-004) en statusovergangen (ADR-007).

### 3. Anti-oogkleppen-regel (examen-driven)

Examenvragen mogen *suggereren* welke concepten nodig zijn. Ze mogen *niet* het concept-niveau bepalen.

> Als examen X vraagt naar "wanneer is melding aan CFI verplicht?" en die vraag valt onder het bredere concept "antiwitwaswetgeving", dan is **antiwitwaswetgeving** het concept en de specifieke vraag is een **toetsings-instantie** (een examenfocus, ADR-009) — niet een eigen concept.

Deze regel voorkomt dat de conceptenset een uittreksel wordt van de voorbeeldexamens.

### 4. Confidence-labeling per veld (zie ADR-010)

Elk veld erft een ⚖️ (grounded) of 🤖 (inferred) label gebaseerd op:
- `bron_rol` van de chunks waaruit het is afgeleid (`itaa_lex` / `interpretatief` → ⚖️)
- het type extractie-stap (directe quote → ⚖️; geconstrueerde redenering → 🤖)

Een veld zonder bronverwijzing krijgt nooit stilzwijgend ⚖️.

### 5. Schema-evolutie tijdens extractie

Wanneer een concept niet past in het huidige conceptmodel:
- de extractor maakt expliciet een schema-uitbreidingsvoorstel (nieuw veld, nieuw node-type, nieuw edge-type)
- voorstel landt als open vraag in de ADR (of een aparte schema-changelog `data/concept_records/_schema_changelog.md`)
- pas na menselijke bevestiging wordt het schema bijgewerkt; de extractor wacht ondertussen of slaat het concept als `partieel` op met een notitie

## Gevolgen

- `tools/extractie/concept_extractor.py` — orchestrator; per ingang (programma / bron / examen) eigen entrypoint
- `tools/extractie/queue.py` — dangling-edges → seed-queue
- LLM-cost: extractie is duur. Provenance-tracking maakt incremental re-runs goedkoop (alleen `stale` records herextraheren).
- Voorbeeldexamens worden vroeg gestructureerd (vraag, oplossing, vereiste kennis) in `data/voorbeeldexamens/` als ground truth voor zowel deze ADR als ADR-009
