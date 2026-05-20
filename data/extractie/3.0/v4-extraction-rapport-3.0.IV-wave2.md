# EXTRACT v4 rapport — PO 3.0 wave 2 — sub-anchors 3.0.IV.A/B/C/D

**Run**: `concept-extractie-v4-2026-05-20T15:00Z`
**Scope**: gap-fill op kapitaal-detail-sub-anchors (3.0.IV.A quasi-inbreng, 3.0.IV.B tussentijdse dividenden, 3.0.IV.C inkoop eigen aandelen, 3.0.IV.D alarmbelprocedure).
**Wave-1-state vóór run**: 650 records, audit groen, 12 records onder anchor `3.0.IV`.
**Wave-1-state na run**: 651 records, audit groen.

## Records — nieuw (1)

| ID | type | linked_anchors | bouwstenen | edges | bron-mix |
|---|---|---|---|---|---|
| `alarmbelprocedure` | cluster | 3.0.IV, 3.0.IV.D, 3.0.IX | 7 (NV-drempels, BV-drempels, CV-drempels, detectie-stukken, procedurestappen, sanctie omkeer bewijslast, continuïteit + waarderingsregels) | 6 (2x vereist-kennis-van, vergelijkt-met nettoactieftest, getriggerd-door continuïteitsbeginsel [pending], 2x onderdeel-van BV/NV) | CBN-advies 2021/14 (primair), WVV art. 5:153/6:119/7:228-7:229, MvT art. 312, IBA Minority Shareholder Rights Belgium 2022 |

**Plaatsing**: één centrale regel-cluster met regime-bouwstenen (NV / BV / CV) ipv drie aparte regime-records, omdat de drempels verschillen maar de procedure-mechaniek (bestuur vaststelt → AV bijeen → bijzonder bestuursverslag → maatregelen → sanctie omkeer bewijslast) identiek is. Twee scenario-voorbeelden uitgewerkt: Brugse Brouwerij BV (liquiditeits-trigger) en Antwerpse Investments NV (kapitaal-trigger). Vergelijkingspaar met `nettoactieftest` (ex-ante barrière versus ex-post detectie).

## Records — bijgewerkt (10)

| ID | Wijziging |
|---|---|
| `quasi-inbreng-verslag` | **Inhoudelijke correctie**: definitie/situering/naam_alternatief geheel herschreven om duidelijk te maken dat de quasi-inbreng-procedure enkel onder Boek 7 NV (art. 7:8) bestaat, niet in de BV (zie MvT art. 5:7: regeling afgeschaft). Eerder record vermeldde foutief 'WVV art. 5:8 BV' — art. 5:8 gaat over volstorting van inbrengen, niet over quasi-inbreng. Met `corrected_from` + `correction_reason`. Bouwsteen 1 (drempel-test): uitzondering art. 7:9 toegevoegd. Bouwsteen 3 (AV-goedkeuring): nietigheid-sanctie uit art. 7:10 §1 toegevoegd. Twee nieuwe bouwstenen: '5 %-aandeelhouders kunnen waardering eisen' (art. 7:8 §3) en 'BV en CV: geen quasi-inbreng-procedure' (anti-confusion uit MvT). Voorbeeld-bug gefixed: '€ 75.000 < € 50.000 → ja' → '€ 75.000 > € 50.000 → ja'. Nieuw BV-voorbeeld toegevoegd (anti-confusion-rol). Twee nieuwe valkuilen (BV-niet-bestaan en 5 %-recht). Vergelijkingspaar geactualiseerd. linked_anchors `+= 3.0.IV.A`. |
| `interimdividend` | `linked_anchors += 3.0.IV.B`. |
| `inkoop-eigen-aandelen-nv` | `linked_anchors += 3.0.IV.C` + nieuwe edge `getriggerd-door: alarmbelprocedure` (facet: 'wanneer de inkoop het nettoactief onder de wettelijke drempels brengt'). |
| `inkoop-eigen-aandelen-bv` | `linked_anchors += 3.0.IV.C` + nieuwe edge `getriggerd-door: alarmbelprocedure` (facet: 'wanneer de inkoop het nettoactief negatief maakt of de liquiditeitstest doet falen'). |
| `nettoactieftest` | Nieuwe edge `vergelijkt-met: alarmbelprocedure` (facet: 'ex-ante barrière versus ex-post detectie van vermogensdaling'). |
| `liquiditeitstest-bv` | Nieuwe edge `vergelijkt-met: alarmbelprocedure` (facet: 'ex-ante barrière versus ex-post detectie van liquiditeitsklem'). |
| `uitkeringstest-vergelijking-bv-nv` | `linked_anchors += 3.0.IV.B, 3.0.IV.C`. |
| `uitkering-uit-eigen-vermogen-bv` | `linked_anchors += 3.0.IV.B`. |
| `kapitaalvermindering-nv` | `linked_anchors += 3.0.IV.C`. |
| `financiele-steunverlening` | `linked_anchors += 3.0.IV.C`. |

**Totaal linked_anchors-mutaties**: 9 records kregen een of meerdere nieuwe sub-anchors (3.0.IV.A op `quasi-inbreng-verslag`; 3.0.IV.B op 3 records; 3.0.IV.C op 5 records; 3.0.IV.D op 0 records buiten het nieuwe alarmbel-record zelf).

## Records — hernoemd / verwijderd

Geen.

## Migraties oud type → nieuw type (schema 1.5/1.6)

Geen — alle bewerkte records waren al op schema 1.6.

## Migraties `voorbeeld_inline` → `voorbeelden[]`

Geen — alle bewerkte records gebruikten al de schema-1.5-vorm.

## Claims `inferred-from-aggregation`

`quasi-inbreng-verslag.bouwstenen[1]` ('Werkprogramma identiek aan inbreng in natura') — was reeds aggregatie tussen ITAA-norm en WVV-tekst; bleef ongewijzigd in dit wave.

## Gaps.json — mutaties

| Aspect | Actie | Aantal |
|---|---|---|
| `records.ontbreekt` (alarmbel-procedure) | 3 open entries → `status=resolved` met `resolved_with_record=alarmbelprocedure` (1 hoog-prio, 2 midden-prio) | 3 |
| `context-edge-ontbreekt` | Nieuw: edge `getriggerd-door: continuiteitsbeginsel` op `alarmbelprocedure` heeft `target_status=pending` — `continuiteitsbeginsel` is een ontbrekend record-kandidaat (WVV art. 2:52 algemene continuïteitsplicht). Prio: midden. | 1 |
| `records.ontbreekt` | Nieuw: belangenconflictenregeling-BV (WVV art. 5:76-5:78) — verdient een eigen record nu we het hebben vermeld als alternatief beschermingsmechanisme in `quasi-inbreng-verslag.bouwstenen.BV-uitsluiting`. Prio: midden. | 1 |
| `granulariteit.beslissing-nodig` | Nieuw: `quasi-inbreng-verslag` — moet de BV-niet-bestaans-noot een eigen kort record worden, of blijft het een bouwsteen-vermelding op het NV-verslag-record? Prio: laag (defaulted to one-record). | 1 |

**Netto gaps**: −3 + 3 = 0 saldo, maar hoog-prio alarmbel-gap is nu gesloten.

## Open observaties — narratieve patronen

1. **Het bestaande `quasi-inbreng-verslag`-record droeg een ingrijpende fout**: het claimde dat WVV art. 5:8 (BV) de quasi-inbreng regelt. Daadwerkelijke bron-verificatie (rechtstreekse lezing van WVV.md regels 1650-1670 + MvT-WVV-2018 chunk-3 over art. 5:7) toont dat art. 5:8 over volstorting van inbrengen gaat, en MvT art. 5:7 expliciet motiveert dat de quasi-inbreng-regeling in de BV is afgeschaft. Dit illustreert het belang van regel 8 uit `concept-extractie-v4.md` ('Discrepantie-driven bron-verificatie'). VERIFY-pass zou dit moeten oppakken; aanbeveling: laat VERIFY systematisch elke `references[].short` checken op bestaan in `resources/bronnen/...`.

2. **Alarmbel-procedure: drie regimes, één procedure-mechaniek**. De keuze om dit als één cluster met regime-bouwstenen te maken (ipv `alarmbelprocedure-nv` / `alarmbelprocedure-bv` als specialisaties) volgt de granulariteits-criteria: de drempels verschillen, maar de procedure-flow (vaststelling → bijeenroeping → bijzonder verslag → AV-besluit → sanctie omkeer bewijslast) is identiek. Mocht een latere PO-event veel regime-specifieke nuances opduiken, kan de cluster nog worden gesplitst met een algemene `alarmbelprocedure` + specialisaties.

3. **Symmetrie tussen uitkeringstest-cluster en alarmbel-cluster**: nettoactieftest + liquiditeitstest-bv functioneren in twee modi — *ex ante* als barrière voor uitkeringen (3.0.IV.A-C kapitaal-detail), *ex post* als trigger voor de alarmbel (3.0.IV.D). De toegevoegde `vergelijkt-met`-edges + de cross-edges `getriggerd-door: alarmbelprocedure` op de inkoop-records maken deze symmetrie expliciet zichtbaar voor render en RAG-walks.

4. **3.0.IV.A bevat veel NV-oprichtings-content** (inbreng in natura, fractiewaarde, art. 7:6-7:7). Het wave-1-record `inbreng-in-natura-verslag` dekt het verslag-aspect; de inbreng-in-natura *zelf* als fenomeen (definitie + waarderingsmethoden + 6-maand-uitzondering art. 7:7-1°-2°) is mogelijk een nog-niet-zelfstandig record. Niet aangepakt in deze pass — out-of-scope. Vermelden als open observatie (geen gap-entry, want het verslag-record dekt het werkprogramma-aspect; de fenomeen-vs-verslag-scheiding is een granulariteits-vraag voor een latere wave).

## Audit

| Check | Status |
|---|---|
| `audit_parity().disk_ids` | 651 |
| `audit_parity().rag_ids` | 651 |
| `disk_only` | 0 |
| `rag_only` | 0 |
| `alarmbelprocedure` op disk + in RAG | ja / ja |
| daemon `localhost:8765` | ok (laatste write 2026-05-20T15:xx, mps device) |

Audit groen na de wave.
