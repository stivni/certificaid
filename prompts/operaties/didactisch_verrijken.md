# Operatie: `didactisch_verrijken`

Vul de didactische concept-niveau-secties: `inhoud.voorbeelden[]`, `inhoud.valkuilen[]`, `inhoud.speelruimtes[]` en `inhoud.syntheses[]`. Toepassen na `beschrijven` en bij voorkeur na `accountant_perspectief`. Geen RAG, geen MCP-calls. Confidence: uitsluitend `verondersteld` of `betwijfeld`.

Voor structuur, veldnamen, enums en shape-details: zie `$comment`/`description` per `$def` in `data/concepten/schema-2.1.schema.json`. Deze prompt geeft alleen workflow + discipline die schema niet kan afdwingen.

**Input**: `data/concepten/records/<fiche-id>.json` — direct-flow, geen /tmp.
**Output**: zelfde bestand overschrijven.
**Tempo**: 2-4 min. RAG: nee.

---

## Voorbeeld

Referentie-record dat de uitvoer van deze operatie illustreert:
`data/concepten/examples/obligatielening-03-didactisch_verrijken.json` — een instrument-record na exact deze operatie. Gebruik het als shape-referentie voor `inhoud.voorbeelden[]`, `inhoud.valkuilen[]`, `inhoud.speelruimtes[]` en `inhoud.syntheses[]`; let op het valkuil-format (`verkeerde_assumptie` + `kernpunt`) en hoe syntheses gestructureerd zijn.

---

## Confidence-discipline

| Token | Symbool | Toegestaan |
|---|---|---|
| `geciteerd` | 📖 | nee |
| `afgeleid` | 🔗 | nee |
| `verondersteld` | 🤖 | ja |
| `betwijfeld` | ❓ | ja — gebruik bij bedragen/percentages/MAR-codes |
| `weerlegd` | ❌ | nee |

**HARDE REGEL**: `claims_checken` valideert bedragen, percentages en MAR-rekening-codes. Markeer als `betwijfeld` als je twijfelt.

---

## Scope-grenzen

- **`voorbeelden[]`**: doorlopende casussen die de hele cyclus tonen (1-2 cases). Niet voor `kader`/`principe`/`actor` (te abstract).
- **`valkuilen[]`**: typische denkfout die student/practitioner maakt — `{titel, verkeerde_assumptie, kernpunt, grondslag}`. Hoeveel: 2-5 stuks. **Valkuil ≠ contra-indicatie** (contra-indicatie = situatie waar concept niet past, staat in `gebruikscontext`).
- **`speelruimtes[]`**: echte beleidskeuze binnen de wet — `{titel, opties[], vuistregel?, grondslag}`. Hoeveel: 1-4 stuks. **Speelruimte ≠ uitzondering** (uitzondering = afwijking van algemene regel door wet, is een `element` met `inhoud_type: "uitzondering"`).
- **`syntheses[]`**: discriminerende structuur met echte didactische meerwaarde. Types: `keuzekader` · `tijdslijn` · `beslisboom` · `matrix` · `dashboard`. Hoeveel: 0-2 stuks. Niet forceren.

---

## Werkwijze

1. Lees `data/concepten/records/<fiche-id>.json`.
2. Lees `data/concepten/schema-2.1.schema.json` `$defs/voorbeeld`, `$defs/valkuil`, `$defs/speelruimte`, `$defs/synthese` voor structuur.
3. **Voorbeelden**: bepaal of zinvolle walkthrough-cases bestaan. Schrijf 1-2 die de hele cyclus tonen.
4. **Valkuilen** (2-5): wat denken studenten typisch verkeerd? Welke fout maken practitioners?
5. **Speelruimtes** (1-4): wat zijn de echte beleidskeuzes binnen de wet? Sla over als er geen zijn.
6. **Syntheses** (0-2): is er een structuur die echt didactische meerwaarde geeft? Kies type bewust.
7. Self-check (zie CRITICAL hieronder).
8. Schrijf record naar `data/concepten/records/<fiche-id>.json`.
9. Voeg changelog-entry toe: `{"operatie": "didactisch_verrijken", "timestamp": "<ISO>", "model": "<jouw-model>"}`.

---

## CRITICAL self-checks

- **R4** — alle nieuwe `id`-velden (voorbeeld.id, element.id binnen voorbeelden) ASCII-kebab: geen unicode, geen underscores.
- Geen inline art-nummers in `tekst`-velden.
- Verouderde veldnamen verboden: niet `text`, niet `beschrijving`, niet `verwijst_naar`.
- Valkuil-format strikt: verplicht `titel` + `verkeerde_assumptie` + `kernpunt` + `grondslag`.
- Geen `inhoud_type: "valkuil"` op elementen — valkuilen horen uitsluitend in `inhoud.valkuilen[]`.

---

## Eindrapport

- Aantal cases · valkuilen · speelruimtes · syntheses (met type per synthese).
- Confidence-mix; open claims voor `claims_checken` (bedragen/percentages/MAR-codes).
- Ontbrekende synthese-types die schema niet biedt — rapporteer (gebruik ze NIET in JSON).
