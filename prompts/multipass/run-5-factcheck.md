# Operatie: `claims_checken` (run-5)

Schema-versie: 2.1 v1.5 (zie `data/concepten/schema-2.1.schema.json` — `$comment`/`description` per `$def` is bron-van-zelfsturing).

**Doel**: upgrade `verondersteld`/`betwijfeld`-claims naar `geciteerd` of `afgeleid` waar primaire bron gevonden. Markeer als `weerlegd` waar bron tegenspreekt. Behoud `verondersteld`/`betwijfeld` als geen bron gevonden.

**Input**: `/tmp/<fiche-id>.json` (na voorgaande operaties).

**Output**: record met geüpgrade `grondslag` per claim. Inhoud-tekst (`tekst`) NIET wijzigen — alleen `grondslag` aanpassen + weerleggingen loggen voor latere correctie.

---

## Confidence-tokens (overzicht — deze operatie kan ALLE waarden zetten)

| Token | Symbool | Wanneer |
|---|---|---|
| `geciteerd` | 📖 | Bron bevestigt claim quasi-letterlijk of duidelijke parafrasering |
| `afgeleid` | 🔗 | Bron ondersteunt deels; ≥ 2 primaire bronnen samen onderbouwen |
| `verondersteld` | 🤖 | Geen bron gevonden — behoud |
| `betwijfeld` | ❓ | Geen bron + expliciete twijfel — behoud |
| `weerlegd` | ❌ | Primaire bron contradicteert claim — log voor correctie |

**Dit is de enige operatie die `geciteerd`/`afgeleid`/`weerlegd` mag zetten.**

---

## Tools

- **`zoek_bronnen(query, top_k, bron_rollen, rerank=false)`** — RAG. Default `rerank=false`; **max 1× `rerank=true`** per record voor finale verificatie van kritieke claim.
- **`lees_record(record_id)`** — voor cross-record-fact-check.
- **`check_record_bestaat(record_id)`** — voor relatie-targets indien relevant.

---

## v1.5-veldnamen (let op)

- Claim-tekst staat in veld `tekst` (was `text`).
- Anchors in `metadata.ankers` (was `linked_anchors`) — niet hier wijzigen.
- Definitie/substantie/rationale onder `inhoud.kern.{...}`.
- Element-claims: `element.kern.{definitie,substantie,rationale}` + `element.weergaven[]`.
- Voorbeelden: `inhoud.voorbeelden[].context` / `.elementen[]` / `.weergaven[]`.

Loop ALLE `grondslag`-objecten in:
- `inhoud.kern.{definitie,substantie,rationale}.grondslag`
- `inhoud.elementen[].kern.*.grondslag` + recursie via `elementen[].elementen[]`
- `inhoud.gebruikscontext.{voor,voorwaarden,...}[].grondslag` (waar van toepassing)
- `inhoud.voorbeelden[].grondslag` + recursief in `elementen`
- `inhoud.valkuilen[].grondslag` · `inhoud.speelruimtes[].grondslag` · `inhoud.syntheses[].grondslag`
- `inhoud.accountant_perspectieven[].rollen[].elementen[].kern.*.grondslag`
- `relaties[].grondslag`

---

## Werkwijze per claim

Voor elke claim met `grondslag.confidence ∈ {verondersteld, betwijfeld}`:

1. **Stale-check**: als `grondslag.checked_at` aanwezig is EN `grondslag.claim_hash` matcht huidige `sha256(tekst)`, skip — al gecheckt.
2. **Zoek primaire bron** met `zoek_bronnen`:
   - Wettelijke claim → `bron_rollen=['wettekst']`
   - Boekhoudkundige → `bron_rollen=['kb','cbn']`
   - Norm → `bron_rollen=['norm']`
   - Aangifte-code → `bron_rollen=['aangifte']`
   - Tarief / bedrag → `bron_rollen=['tarief']`
3. **Match-beslissing**:
   - Bron bevestigt quasi-letterlijk → `confidence: "geciteerd"`, `bronnen: [{type, naam, ref}]`
   - ≥ 2 bronnen onderbouwen samen → `confidence: "afgeleid"`
   - Bron spreekt tegen → `confidence: "weerlegd"`, log claim voor latere correctie
   - Geen bron gevonden → behoud
4. **Set `checked_at` + `claim_hash`** (sha256 van `tekst`) zodat latere runs niet herchecken.

---

## Stop-criteria

- Maximaal **15 `zoek_bronnen`-calls** per record. Boven dat: noteer in eindrapport hoeveel claims niet gefactcheckt zijn.
- Als bundel-bronnen al voldoende dekken (skim de bundle als die bestaat): hergebruik.
- Max **1× `rerank=true`** voor de duurste verificatie.

---

## Weerlegde claims

Markeer als `weerlegd` en log, maar **WIJZIG DE `tekst` NIET** in deze operatie. Een volgende operatie (handmatig of `kandidaat_review`) corrigeert. Bewaar de tegensprekende bron in `grondslag.bronnen[]` en vul `grondslag.weerlegging` met korte uitleg.

Eindrapport vermeldt:

```
WEERLEGD CLAIMS:
- /inhoud/elementen[2]/kern/substantie — claim "5:1 schuld/EV-ratio"
  bron: WIB92 art. 198 §1, 11° zegt eigenlijk 5:1 als verhouding van schulden van groepsverbonden ondernemingen
  → check definitie-precisie
```

---

## Prioriteit-volgorde claims

Sorteer op kritisch belang vóór je het call-budget toewijst:

1. `inhoud.kern.definitie` (de definiërende claim)
2. `inhoud.elementen[].kern.*` (mechanisme-claims)
3. `inhoud.gebruikscontext.*` (toepassings-claims)
4. `inhoud.valkuilen[]` + `inhoud.speelruimtes[]` (didactische claims)
5. `relaties[]` (graph-claims — vooral `vereist` / `is_uitzondering_op`)
6. `inhoud.accountant_perspectieven[].rollen[]` (rol-claims)
7. `inhoud.voorbeelden[]` (illustraties — laagste prioriteit)

---

## Discipline

- **`tekst` niet wijzigen** — alleen `grondslag` aanpassen + weerleggingen loggen.
- **Geen platte-dict / top-level weergaven** introduceren (oude pitfalls).
- **Geen MCP-bron-naam = ref** verwarren: `naam` is mensleesbaar (bv. "WIB92 art. 269 §1, 2°"); `ref` is canonical-slug (bv. `wib92-art-269-1-2`).
- **`ai_model`-bron behouden** als secondary bron na een primaire bron-upgrade — beide horen in `bronnen[]`.

---

## Werkwijze

1. Lees `/tmp/<fiche-id>.json`.
2. Identificeer alle claims (alle `grondslag`-objecten — zie lijst hierboven).
3. Sorteer op kritisch belang.
4. Loop door (binnen budget van 15 calls):
   - Per claim: zoek bron, upgrade `grondslag`, set `checked_at` + `claim_hash`.
5. Schrijf record terug.
6. Update `metadata.changelog`:
   ```json
   {"operatie": "claims_checken", "timestamp": "<ISO>", "model": "<jouw-model>",
    "metriek": {"upgraded_geciteerd": N, "upgraded_afgeleid": N, "weerlegd": N, "behouden": N, "calls": N}}
   ```

**Tempo**: 5-8 min (RAG-intensief).

---

## Eindrapport

- Aantal claims voor/na:
  - `verondersteld → geciteerd`
  - `verondersteld → afgeleid`
  - `verondersteld → weerlegd`
  - `verondersteld behouden`
  - `betwijfeld → geciteerd/afgeleid` (resolved twijfel)
- Weerlegde claims-lijst (path + claim + tegensprekende bron).
- Aantal MCP-calls totaal · aantal `rerank=true`-calls.
- Open punten voor vervolg-operaties (`kandidaat_review`, `consistentie_check`).
