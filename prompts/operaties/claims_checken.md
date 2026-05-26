# Operatie: `claims_checken`

Upgrade `verondersteld`/`betwijfeld`-claims naar `geciteerd` of `afgeleid` waar een primaire bron gevonden wordt. Markeer als `weerlegd` waar een bron tegenspreekt. **Dit is de enige operatie die `geciteerd`/`afgeleid`/`weerlegd` mag zetten.** Toepassen na alle overige operaties, of op aanvraag na inhoud-wijzigingen.

Voor structuur, veldnamen, enums en shape-details: zie `$comment`/`description` per `$def` in `data/concepten/schema-2.1.schema.json`. Deze prompt geeft alleen workflow + discipline die schema niet kan afdwingen.

**Input**: `data/concepten/records/<fiche-id>.json` — direct-flow, geen /tmp.
**Output**: zelfde bestand overschrijven (alleen `grondslag`-objecten aanpassen, `tekst` NIET wijzigen).
**Tempo**: 5-8 min. RAG: ja — `zoek_bronnen`, `lees_record`, `check_record_bestaat`.

---

## Voorbeeld

Referentie-record dat de uitvoer van deze operatie illustreert:
`data/concepten/examples/obligatielening-05-claims_checken.json` — een instrument-record na exact deze operatie. Gebruik het als shape-referentie voor `grondslag`-objecten: let op hoe `geciteerd`/`afgeleid`-claims een `bron_ref` met zowel `ref` (canonical-slug) als `naam` bevatten, en hoe `checked_at` + `claim_hash` ingevuld zijn.

---

## Confidence-discipline

| Token | Symbool | Wanneer |
|---|---|---|
| `geciteerd` | 📖 | bron bevestigt claim quasi-letterlijk of duidelijke parafrasering |
| `afgeleid` | 🔗 | ≥ 2 primaire bronnen onderbouwen samen |
| `verondersteld` | 🤖 | geen bron gevonden — behoud |
| `betwijfeld` | ❓ | geen bron + expliciete twijfel — behoud |
| `weerlegd` | ❌ | primaire bron contradicteert claim — log voor correctie |

**HARDE REGEL**: `tekst`-veld NIET wijzigen — alleen `grondslag` aanpassen. Weerlegde claims loggen voor latere correctie.

---

## Scope-respect (ADR-033)

Lees `metadata.scope` indien aanwezig.

- **`scope.in[]`** — claims die hier thuishoren krijgen normale claims-check-behandeling.
- **`scope.out[]`** — claims die onder een `scope.out`-topic vallen zijn **scope-violations** (komen uit eerdere operatie). Markeer ze in eindrapport als `scope_violation`. **Wijzig de claim niet** (`tekst`-veld blijft per harde regel intact); log voor mapping-fase-correctie. Voorbeeld: `controleopdracht` bevat een claim over materialiteit-formule — dat hoort in `audit-planning` (scope.out-topic). Niet upgrade-en, alleen flag.

Geen `scope`-veld? → werk volgens normale claims-check-logica.

---

## MCP-tools

- `zoek_bronnen(query, top_k, bron_rollen, rerank=false)` — RAG. Max **15 calls** per record. Max **1× `rerank=true`** voor de duurste verificatie.
- `lees_record(record_id)` — cross-record fact-check.
- `check_record_bestaat(record_id)` — relatie-target-verificatie.

Stale-check vóór elke claim: als `grondslag.checked_at` aanwezig is EN `grondslag.claim_hash` matcht `sha256(tekst)` — **skip**.

---

## Claim-prioriteit (budget-toewijzing)

1. `inhoud.kern.definitie`
2. `inhoud.elementen[].kern.*` (mechanisme-claims)
3. `inhoud.gebruikscontext.*`
4. `inhoud.valkuilen[]` + `inhoud.speelruimtes[]`
5. `relaties[]` (vooral `vereist` / `is_uitzondering_op`)
6. `inhoud.accountant_perspectieven[].rollen[]`
7. `inhoud.voorbeelden[]` (laagste prioriteit)

---

## Bron-rollen per claim-type

| Claim-type | `bron_rollen` |
|---|---|
| Wettelijke claim | `['wettekst']` |
| Boekhoudkundig | `['kb', 'cbn']` |
| Norm | `['norm']` |
| Aangifte-code | `['aangifte']` |
| Tarief / bedrag | `['tarief']` |

---

## Werkwijze

1. Lees `data/concepten/records/<fiche-id>.json`.
2. Lees `data/concepten/schema-2.1.schema.json` voor `$defs/grondslag` en `$defs/bron_ref`.
3. Identificeer alle `grondslag`-objecten (volledige loop — zie alle paden hieronder).
4. Sorteer op prioriteit.
5. Per claim (binnen budget 15 calls):
   a. Stale-check.
   b. `zoek_bronnen` met juiste `bron_rollen`.
   c. Upgrade `confidence` + vul `bronnen[]` + set `checked_at` + `claim_hash`.
6. Self-check (zie CRITICAL hieronder).
7. Schrijf record.
8. Voeg changelog-entry toe met metriek: `{"operatie": "claims_checken", "timestamp": "<ISO>", "model": "<jouw-model>", "metriek": {"upgraded_geciteerd": N, "upgraded_afgeleid": N, "weerlegd": N, "behouden": N, "calls": N}}`.

**Volledige claim-loop**: `inhoud.kern.{definitie,substantie,rationale}.grondslag` · `inhoud.elementen[].kern.*.grondslag` (recursief) · `inhoud.gebruikscontext.{voor,niet_voor,voorwaarden,...}[].grondslag` · `inhoud.voorbeelden[].grondslag` + recursief · `inhoud.valkuilen[].grondslag` · `inhoud.speelruimtes[].grondslag` · `inhoud.accountant_perspectieven[].rollen[].elementen[].kern.*.grondslag` · `relaties[].grondslag`. `inhoud.syntheses[]` heeft geen top-level grondslag.

---

## CRITICAL self-checks

- **`bron_ref.ref` verplicht** voor primaire bronnen (`wettekst` · `kb` · `cbn` · `norm` · `richtlijn` · `circulaire` · `modelverdrag`). `ref` = canonical-slug (bv. `wib92-art-269-1-2`). `naam` = mensleesbaar (bv. "WIB92 art. 269 §1, 2°"). Schema-validatie faalt zonder `ref`. Scan elke nieuwe `geciteerd`/`afgeleid`-claim vóór save.
- `ai_model`-bron behouden als secondary bron naast primaire bron — beide in `bronnen[]`.
- Naam en ref niet verwarren: `naam` ≠ `ref`.
- Weerlegde claims: `tekst` NIET wijzigen — voeg `grondslag.weerlegging` toe met korte uitleg + tegensprekende bron.

---

## Eindrapport

- Claims voor/na: `verondersteld→geciteerd` · `verondersteld→afgeleid` · `verondersteld→weerlegd` · `verondersteld behouden` · `betwijfeld→geciteerd/afgeleid` (resolved).
- Weerlegde claims-lijst: path + claim + tegensprekende bron.
- Aantal MCP-calls totaal · aantal `rerank=true`-calls.
- Open punten voor vervolg (`kandidaat_review`, `consistentie_check`).
