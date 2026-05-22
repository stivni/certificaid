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
3. Identificeer klant-perspectieven uit `inhoud.elementen` + `concept_type`:
   - instrument/regime → uitgever vs ontvanger vs belegger
   - verrichting → initiator vs ontvanger vs toezichthouder
   - procedure → actor-per-fase
   - ratio/balanspost → opsteller vs gebruiker/analist
4. Per perspectief: selecteer welke rollen echt iets te zeggen hebben — **geen lege rollen**.
5. Per rol: 1-3 elementen (kerntaak, niet alles). Element-shape = identiek aan top-level element (schema `$defs/element`).
6. Self-check (zie CRITICAL hieronder).
7. Schrijf record naar `data/concepten/records/<fiche-id>.json`.
8. Voeg changelog-entry toe: `{"operatie": "accountant_perspectief", "timestamp": "<ISO>", "model": "<jouw-model>"}`.

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
