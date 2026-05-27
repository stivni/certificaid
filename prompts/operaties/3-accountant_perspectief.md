# Operatie: `accountant_perspectief`

Vul `inhoud.accountant_perspectieven[]` — de rol × perspectief-matrix die beschrijft wat de accountant doet voor elke klant-context. Toepassen na `beschrijven`. Geen RAG, geen MCP-calls. Confidence: uitsluitend `verondersteld` of `betwijfeld`.

Voor structuur, veldnamen, enums en shape-details: zie `$comment`/`description` per `$def` in `data/concepten/schema-2.1.schema.json`. Deze prompt geeft alleen workflow + discipline die schema niet kan afdwingen.

**Input**: `data/concepten/records/<fiche-id>.json` — direct-flow, geen /tmp.
**Output**: zelfde bestand overschrijven.
**Tempo**: 1-2 min. RAG: nee.

---

## Voorbeeld

Referentie-record dat de uitvoer van deze operatie illustreert:
`data/concepten/examples/obligatielening-02-accountant_perspectief.json` — een instrument-record na exact deze operatie. Gebruik het als shape-referentie voor de perspectief × rol-matrix in `inhoud.accountant_perspectieven[]`; let op welke rollen gevuld zijn en welke weggelaten.

---

## Confidence-discipline

| Token | Symbool | Toegestaan |
|---|---|---|
| `geciteerd` | 📖 | nee |
| `afgeleid` | 🔗 | nee |
| `verondersteld` | 🤖 | ja |
| `betwijfeld` | ❓ | ja |
| `weerlegd` | ❌ | nee |

**HARDE REGEL**: alle claims = `verondersteld` met `ai_model`-bron. `claims_checken` upgradet later.

---

## Scope-respect (ADR-033)

Lees `metadata.scope` indien aanwezig.

- **`scope.in[]`** — perspectieven beschrijven wat de accountant DOET met dit fenomeen. Hun inhoud raakt typisch de `scope.in`-topics (= dat wat het record behandelt) plus de werk-handelingen erop.
- **`scope.out[]`** — als een rol-actie inherent over een `scope.out`-topic gaat, **schrijf de actie niet hier**; de rol-uitwerking hoort thuis bij het record waar dat topic woont. Bv: `controleopdracht` heeft scope.out "planning-detail → audit-planning". De `auditor`-rol-acties voor planning-detail (materialiteit-bepaling, risico-inschatting) horen in `audit-planning`'s perspectieven, niet hier.
- **Perspectief-vs-eigen-record-principe** (rationale-log 2026-05-26): 2 perspectieven op zelfde fenomeen ≠ 2 records. Als je merkt dat je een 2e identiek perspectief op een ander record schrijft, is dat een mapping-fase-flag (mogelijk record-duplicatie).

Geen `scope`-veld? → werk volgens normale plaatsingsregel hieronder.

---

## Plaatsingsregel (spiegel van `beschrijven`)

Litmus: "gebeurt dit ongeacht of er een accountant bij betrokken is?"
- **Ja** → `inhoud.elementen[]` (was al gedaan in `beschrijven`) — NIET hier herhalen
- **Nee** → hier, onder de juiste rol

| Inhoud | Rol |
|---|---|
| Boekhoudkundige verwerking · rekening-codes · boekingsmoment | `boekhouder` |
| Audit-procedures · risico-drempels · controle-aandachtspunten | `auditor` |
| Aangifte-codes · fiscale optimalisatie-stappen | `fiscaal` |
| Advies-checklist · alternatieven-afweging · vuistregels | `adviseur` |
| Begeleidings-stappen · formaliteiten · termijn-bewaking | `begeleider` |

**Migratie-check**: als `inhoud.elementen[]` items bevat die hier horen (bv. `procedure_stap` "Boekhoudkundige verwerking"), verplaats die — verwijder uit `elementen`, voeg toe onder juiste rol, log in changelog.

---

## Vijf-rol-set

Gebruik uitsluitend: `adviseur` · `boekhouder` · `begeleider` · `fiscaal` · `auditor`. Geen andere rollen.

---

## Werkwijze

1. Lees `data/concepten/records/<fiche-id>.json` (na `beschrijven`).
2. Lees `data/concepten/schema-2.1.schema.json` `$defs/perspectief` en `$defs/element` voor structuur.
3. Lees `data/concepten/casts/globaal.yaml` — gebruik cast-namen + scenario-archetype als rol-elementen voorbeeld-context bevatten (bv. `auditor` met casus "Wolters & Partners CVBA bij Rotex Roeselare NV"). Bedragen `€ + duizendtal-punt`.
4. Identificeer klant-perspectieven uit `inhoud.elementen` + `concept_type`:
   - instrument/regime → uitgever vs ontvanger vs belegger
   - verrichting → initiator vs ontvanger vs toezichthouder
   - procedure → actor-per-fase
   - ratio/balanspost → opsteller vs gebruiker/analist
5. Per perspectief: selecteer welke rollen echt iets te zeggen hebben — **geen lege rollen**.
6. Per rol: 1-3 elementen (kerntaak, niet alles). Element-shape = identiek aan top-level element (schema `$defs/element`).
7. Self-check (zie CRITICAL hieronder).
8. Schrijf record naar `data/concepten/records/<fiche-id>.json`.
9. Voeg changelog-entry toe: `{"operatie": "accountant_perspectief", "timestamp": "<ISO>", "model": "<jouw-model>"}`.

---

## CRITICAL self-checks

- **R1** — identiteit onveranderd: `id`, `naam`, `concept_type`, `metadata.schema_version` letterlijk identiek aan input.
- **R4** — alle nieuwe `id`-velden (perspectief.id, element.id) ASCII-kebab: geen unicode, geen underscores.
- Geen lege rollen — alleen rollen met inhoud schrijven.
- Geen overlap met `inhoud.elementen` — bij twijfel kruisverwijs via `relaties[]` op het element (niet dupliceren).

---

## Eindrapport

- Aantal perspectieven · aantal gevulde rol-cellen (perspectief × rol).
- Confidence-mix.
- Eventuele migratie: welke elementen verplaatst van `inhoud.elementen` naar rollen.
- Open vragen voor `claims_checken`.
