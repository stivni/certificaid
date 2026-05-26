# Operatie: `beschrijven`

Vul `inhoud` van een skelet-record vanuit training-data: kern (definitie/substantie/rationale), elementen, gebruikscontext en suggesties voor top-level relaties. Toepassen als eerste operatie op een leeg of skelet-record. Confidence: uitsluitend `verondersteld` of `betwijfeld`.

**HARDE REGEL — geen MCP, geen RAG**: gebruik UITSLUITEND de `Read`-tool voor file-access. Geen enkele `mcp__*`-tool aanroepen, ook niet `mcp__certificaid-rag__lees_record` of `mcp__certificaid-rag__zoek_*`. Records, schema en index lees je rechtstreeks van disk via `Read`. Reden: deze operatie put uit training-data, niet uit retrieval — MCP-calls verbruiken context én ondermijnen de confidence-discipline (alles wat uit een MCP-respons komt zou `geciteerd`/`afgeleid` zijn, en die zijn hier verboden).

Voor structuur, veldnamen, enums en shape-details: zie `$comment`/`description` per `$def` in `data/concepten/schema-2.1.schema.json`. Deze prompt geeft alleen workflow + discipline die schema niet kan afdwingen.

**Input**: `data/concepten/records/<fiche-id>.json` — direct-flow, geen /tmp.
**Output**: zelfde bestand overschrijven.
**Tempo**: 1-3 min. RAG: nee.

---

## Voorbeeld

Referentie-record dat de uitvoer van deze operatie illustreert:
`data/concepten/examples/obligatielening-01-beschrijven.json` — een instrument-record na exact deze operatie (verdere operaties nog niet toegepast). Gebruik het als shape-referentie voor `inhoud.kern`, `inhoud.elementen[]` en `inhoud.gebruikscontext`; herhaal de inhoud niet letterlijk.

---

## Confidence-discipline

| Token | Symbool | Toegestaan in `beschrijven` |
|---|---|---|
| `geciteerd` | 📖 | nee — vereist primaire-bron-validatie |
| `afgeleid` | 🔗 | nee — vereist ≥ 2 primaire bronnen |
| `verondersteld` | 🤖 | ja |
| `betwijfeld` | ❓ | ja — gebruik bij twijfelachtige datum/percentage/art-nummer |
| `weerlegd` | ❌ | nee — vereist bron-contradictie |

**HARDE REGEL**: vóór save — scan alle `grondslag.confidence`, downgrade elke `geciteerd`/`afgeleid`/`weerlegd` naar `verondersteld` of `betwijfeld`.

AI-bron-vorm: `{"type": "ai_model", "naam": "claude-sonnet-4-6", "datum": "<vandaag>"}`.

---

## Scope-respect (ADR-033)

Lees `metadata.scope` indien aanwezig vóór je `inhoud` schrijft:

- **`scope.in[]`** — topics die DIT record MOET behandelen. Elke topic minstens in `inhoud.kern` of als `inhoud.elementen[]`-entry weerspiegelen.
- **`scope.out[]`** — topics die EXPLICIET NIET in dit record komen + verwijzing naar record-id dat het wel behandelt. Bij elke claim die je wil schrijven: check of die onder een `scope.out`-topic valt. Zo ja: **schrijf de claim niet**; voeg in plaats daarvan een korte cross-reference toe in `inhoud.kern.rationale.tekst` of `inhoud.gebruikscontext` (één zin: "Voor X zie `<record-id>`").
- Geen `scope`-veld in metadata? → werk volgens normale "Scope-grenzen en plaatsingsregel"-logica hieronder.

**Anti-pattern**: content schrijven dat in `scope.out` staat = scope-violation. Eindrapport vermeldt aantal `scope.out`-topics dat je tegenkwam + niet behandelde (= 0 violations gewenst).

---

## Scope-grenzen en plaatsingsregel

Litmus: "gebeurt dit ongeacht of er een accountant bij betrokken is?"
- **Ja** → `inhoud.elementen[]` (concept-intrinsiek)
- **Nee** → `inhoud.accountant_perspectieven[].rollen[].elementen[]` (handelings-kennis) — **NIET vullen in `beschrijven`**

| Inhoud | Plek |
|---|---|
| Wettelijke voorwaarden · mechanisme · formules · sub-concepten · concept-intrinsieke stappen | `inhoud.elementen[]` |
| Boekhoudkundige verwerking · rekening-codes · boekingsmoment | `accountant_perspectieven` (rol=`boekhouder`) |
| Audit-procedures · controle-aandachtspunten | `accountant_perspectieven` (rol=`auditor`) |
| Aangifte-codes · fiscale optimalisatie | `accountant_perspectieven` (rol=`fiscaal`) |
| Advies-checklist · alternatieven-afweging | `accountant_perspectieven` (rol=`adviseur`) |
| Begeleidings-stappen · formaliteiten | `accountant_perspectieven` (rol=`begeleider`) |

`inhoud.voorbeelden[]`, `valkuilen[]`, `speelruimtes[]`, `syntheses[]` en `accountant_perspectieven[]`: **niet vullen in `beschrijven`** — komen in latere operaties.

---

## Werkwijze

1. Lees `data/concepten/records/<fiche-id>.json` (skelet) — **met `Read`-tool, niet via MCP**.
2. Lees `data/concepten/schema-2.1.schema.json` — `$comment`/`description` per `$def` is bron-van-waarheid voor veldnamen, enums en shapes.
3. Lees `data/concepten/records-index.compact.txt` (scope-anker: vermijd duplicatie, suggereer relaties). **Géén `lees_record` op andere fiches** — relatie-suggesties komen uit training-data + index-titels, niet uit hun inhoud.
4. Lees `data/concepten/casts/globaal.yaml` — gebruik stabiele Vlaamse cast-namen in voorbeelden (`Uitgeverij Ukkel NV`, niet "NV ABC"); zoek scenario-archetype dat past bij dit concept_type. Bedragen `€ + duizendtal-punt` (`€ 1.000.000`).
4. Schrijf `inhoud.kern` (≥ 1 van `definitie`/`substantie`/`rationale`).
5. Bouw `inhoud.elementen[]` (5-8 stuks, elk met `kern` gevuld, geen lege schalen).
6. Vul `inhoud.gebruikscontext` (alle sub-velden zijn arrays).
7. Suggesties voor top-level `relaties[]` (geen MCP-validatie nodig — `relaties_aanvullen` valideert later).
8. Self-check (zie CRITICAL hieronder).
9. Schrijf record naar `data/concepten/records/<fiche-id>.json`.
10. Voeg changelog-entry toe: `{"operatie": "beschrijven", "timestamp": "<ISO>", "model": "<jouw-model>"}`.

---

## CRITICAL self-checks

- **R0** — geen MCP-calls gebruikt. Scan je eigen tool-historie: 0× `mcp__*` aanroepen. Indien wel: stop, verwijder/negeer de retrieval-resultaten, en bouw inhoud puur op training-data + de drie disk-files uit stap 1-3.
- **R1** — identiteit onveranderd: `id`, `naam`, `concept_type`, `metadata.schema_version` letterlijk identiek aan input.
- **R2** — relaties-veldnaam is `target`, nooit `naar`/`naar_concept`/`to`.
- **R3** — `relaties[]` staat op top-level van het record, NIET binnen `inhoud`.
- **R4** — alle `id`-velden ASCII-kebab: `^[a-z0-9][a-z0-9-]*[a-z0-9]$` — geen unicode (ë/é/ü), geen underscores, geen kapitalen.
- Geen inline art-nummers in `tekst`-velden — wettekst-verwijzingen horen in `grondslag.bronnen[]`.
- Geen verouderde veldnamen: niet `element.beschrijving`, niet `element.verwijst_naar`, niet `text` (gebruik `tekst`).

---

## Eindrapport

- File-size + aantal `inhoud.elementen` + aantal relatie-suggesties.
- Confidence-mix (`verondersteld` vs `betwijfeld`).
- Ontbrekende `inhoud_type`-waarden (niet in schema — rapporteer, gebruik ze NIET).
- Open vragen voor `claims_checken`.
