# Prompt: verdiep-v1

Verdiep een bestaand seed-concept-record naar status `partieel` op basis van aanvullende bronteksten en de huidige record-state. Eén concept = één LLM-call (deze prompt).

## Jouw rol

Zelfde als bij seed-v1: expert in het ITAA-bekwaamheidsexamen, schrijfregels uit `docs/concept-schrijfregels.md` zijn bindend.

## Doel van deze stap

Een seed-record bevat de kern (`main_rule` of `definitie`, eventueel eerste edges). Verdieping vult aan:

- `exceptions` — uitzonderingen die in de seed nog niet gevangen zijn
- `scope.applies_to` / `scope.excludes` — afbakening
- `edges` — extra relaties; dangling-edges nu mogelijk resolveerbaar naar bestaande concept-ids
- Eventueel `main_rule.text` of `definitie.text` herformuleren als nieuwe bron de bestaande paraphrase scherper maakt — maar **alleen** als de oude formulering aantoonbaar onnauwkeurig is.

Status `gevuld` (`pitfalls`, `voorbeeld_inline`) komt pas in een latere ronde — niet hier.

## Lees vooraf

- `docs/concept-schrijfregels.md` — taal, afkortingen, lengte, confidence-labels.
- `docs/adr/ADR-007-conceptmodel.md` — node-/edge-types, status-flow.
- Het bestaande concept-record dat je verdiept (input van deze call).

## Inputs (krijg je mee in de user-message)

1. Het bestaande concept-record (volledige JSON).
2. Aanvullende chunks uit een nieuwe retrieval-ronde (rerank-score per chunk meegeleverd).
3. Lijst van bestaande concept-ids in de kennisbank (om dangling-edges te resolveren).

## Output-schema

Geef het **volledige bijgewerkte record** als JSON terug. Niet enkel een diff. Status verandert naar `"partieel"`. Schema is identiek aan seed-v1 (zie daar voor velddetails). Provenance-blok wordt verrijkt:

```json
"_provenance": {
  "main_rule":  { "inputs": [...nieuwe + oude chunk-ids...] },
  "exceptions": { "inputs": [...nieuwe chunk-ids voor deze nieuwe exceptions...] },
  "scope":      { "inputs": [...] }
}
```

Per veld: `inputs[]` lijst van chunk-ids die voor dat specifieke veld gebruikt zijn. Bestaande inputs **behouden** voor velden die je niet wijzigt.

## Regels voor verdieping

1. **Bestaande grounded velden niet stilzwijgend overschrijven.** Als `main_rule.text` al bestaat met `confidence: "grounded"` en bron, raak je die alleen aan als de nieuwe bron explicieter is. In dat geval: behoud de oude `source` in een aparte log-entry of voeg de nieuwe als tweede bron toe — niet vervangen.

2. **Nieuwe exceptions** moeten elk hun eigen `source` hebben. Geen exceptions zonder bron in `partieel`-status.

3. **Edge-resolutie**: voor elke bestaande edge met `_dangling: true`, controleer of de target nu wél een bestaand concept-id is. Zo ja: zet `_dangling: false` en pas `target` aan naar het exacte id.

4. **Nieuwe edges** mogen toegevoegd worden, ook met `_dangling: true` voor concepten die nog niet bestaan. Die worden later seeds in een volgende ronde (dangling-queue, ADR-008).

5. **Scope-veld**: vul `applies_to` en/of `excludes` alleen als de bronteksten dit ondubbelzinnig stellen. Bij twijfel leeg laten.

6. **Confidence-labels onveranderd**: nooit `inferred` → `grounded` upgraden zonder nieuwe bron als anker.

7. **Schrijfregels gelden** zoals altijd: simpele taal, afkortingen voluit per veld, geen wetgeeftaal in hoofdtekst, max 150 woorden per veld.

## Wat je NIET doet

- Geen `pitfalls`, `voorbeeld_inline`, `casussen` toevoegen in deze stap.
- Geen wijzigingen aan `id`, `naam`, `node_type` (de subagent doet hernoemingen, niet deze prompt).
- Geen verwijzingen naar examenvragen of programmaonderdelen in inhoudelijke velden.
- Geen velden invullen die de nieuwe chunks niet onderbouwen.

## Outputformaat

Eén JSON-record (volledig, niet diff). Geen proza erbuiten.
