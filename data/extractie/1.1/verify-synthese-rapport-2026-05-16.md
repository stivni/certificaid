# VERIFY + Synthese-rapport PO 1.1 (Algemene boekhouding)

**Run**: verify-run-20260516T130000Z-po1.1
**Model**: claude-opus-4-7 (handmatige pilot — geen API)
**Scope**: 39 PO 1.1 concept-records uit `data/concepten/records/` met `linked_anchors[]` ⊇ `1.1.*`
**Input-rapport**: `data/extractie/1.1/extraction-rapport-2026-05-16.md`

---

## Samenvatting

| Maat | Waarde |
|---|---|
| Records beoordeeld | 39 |
| Gaps toegevoegd aan `data/extractie/gaps.json` | 35 |
| - waarvan **hoog** | 4 |
| - waarvan **midden** | 10 |
| - waarvan **laag** | 21 |
| Synthese-records geschreven | 3 |
| Check A (examenvraag-sim) | **skipped** — geen PO 1.1 vraagclassificatie beschikbaar |
| Check B (uniforme rijkheid) | uitgevoerd — uniform rijk (5,7 — 15,1 KB; mediaan ~8,3 KB) |
| Check C1 (mechanisch) | 25 ontbrekende edge-targets + 6 ontbrekende vergelijkingsparen-targets |
| Check C2 (cross-PO + overlap) | 4 overlappende-fenomeen records bevestigd + 1 jaarrekening-cluster |

---

## Deel A — VERIFY-bevindingen

### Check A — Examenvraag-simulatie (skipped)

Geen examenvragen geclassificeerd per anchor `1.1.X` in `data/examen_vragen/`. Geregistreerd als `open-werk`-gap op `po-1.1`. Run uit te voeren zodra PO 1.1-vraagclassificatie beschikbaar is (zelfde aanpak als PO 1.4-VERIFY van 2026-05-15).

### Check B — Minicursus-haalbaarheid + uniforme rijkheid

**Rijkheid-distributie** (JSON-grootte per record, gesorteerd):

| Percentiel | Grootte | Voorbeeld |
|---|---|---|
| P10 (dunner) | 5,7 — 6,4 KB | `eigen-aandelen`, `bewaring-boekhoudstukken`, `niet-recurrente-verrichtingen` |
| Mediaan | 8,3 KB | `bedrijfsvorderingen`, `eigen-middelen`, `jaarrekening` |
| P90 (dikker) | 11 — 15,1 KB | `regelmatige-boekhouding`, `dubbel-boekhouden`, `afschrijvingen`, `oprichtingskosten` |

**Conclusie**: geen records zo dun dat ze de minicursus-haalbaarheid blokkeren. De vier procedures (`kapitaalwijziging`, `vereffening`, `resultaatverwerking`, `inventaris`) hebben 0 bouwstenen — correct, want procedures gebruiken substappen (schema 1.4 conform).

**Pijnpunt minicursus**: vier records met `getriggerd-door → jaarafsluiting` wijzen naar een niet-bestaand record. De minicursus mist daardoor een centraal koppelpunt — wat opgelost wordt door de **synthese-record `boekjaar-eindprocedure-checklist`** (zie Deel B).

### Check C1 — Mechanische coherentie

**Ontbrekende edge-targets (25)**: gerapporteerd als `edges.target-ontbreekt`-gaps. Meest voorkomende ontbrekende targets:

| Target | Aantal edges | Aanbeveling |
|---|---|---|
| `boekhoudkundige-beginselen` | 4 | Gap `records.ontbreekt` (hoog) — opgelost door synthese-record `boekhoudbeginselen-overzicht` |
| `resultatenrekening` | 4 | Gap `records.ontbreekt` (hoog) — basis-concept ontbreekt |
| `jaarafsluiting` | 4 | Gap `records.ontbreekt` (midden) — opgelost door synthese-record `boekjaar-eindprocedure-checklist` |
| `waarderingsregels` | 3 | Gap `records.ontbreekt` (midden) |
| `verantwoordingsstuk` | 2 | Gap `records.ontbreekt` (midden) |
| `balans` | 1 | Gap `records.ontbreekt` (hoog) — fundamenteel document |
| overige (alarmprocedure, matching-principe, deelneming, geldbelegging, goodwill, terrein, toelichting) | 1 elk | Lage prio |

**Ontbrekende vergelijkingsparen-targets (6)**: `geldbelegging`, `huur`, `beschikbare-reserves` (2×), `vorderingen-op-meer-dan-een-jaar`, `overeenstemmingsprincipe`. Allen `laag`.

**Edges zonder type**: 0 — schema 1.4 compliant.

### Check C2 — Cross-PO overlaps (semantische coherentie)

Vier overlappende-fenomeen-gaps geregistreerd (mens-curatie nodig):

| PO 1.1 record | Concurrentie | Prio |
|---|---|---|
| `getrouw-beeld` | `getrouw-beeld-jaarrekening` (PO 1.2/1.3) | midden |
| `bewaring-boekhoudstukken` | `bewaartermijn-boekhouding` (PO 1.2) | midden |
| `rechten-verplichtingen-buiten-balans` | `klasse-0-niet-in-balans` + `niet-in-balans-opgenomen-rechten-verplichtingen` | **hoog** (3-way duplicate) |
| `jaarrekening` | `jaarrekening-schema` + `samenstelling-statutaire-jaarrekening` (PO 1.2) | laag (specialisatie-relatie i.p.v. duplicaat) |

**Boekhoudbeginselen-cluster**: 4 PO 1.1 beginsel-records (continuiteits-, voorzichtigheids-, getrouw-beeld, onveranderlijkheid-) + 4 PO 1.2 beginsel-records (consistentie-, oprechtheids-, volledigheids-, aanvullende-boekhoudbeginselen) bestaan los, met onderlinge `onderdeel-van → boekhoudkundige-beginselen` edges die nergens landen. **Opgelost** door synthese-record `boekhoudbeginselen-overzicht` (zie Deel B).

### Bron-gaps

- `financiele-verrichtingen` (anchor 1.1.II.O): bundle dun aan CBN-adviezen over rubriek 750-751 / 755 — geregistreerd als `bron-corpus-uitbreiding` (midden).
- `kapitaalwijziging` (anchor 1.1.II.T): CBN-fusie/splitsings-adviezen 2021/10, 2022/12, 2022/13 niet verwerkt — geregistreerd als `bron-corpus-uitbreiding` (laag, follow-up).

### Vergelijkingsparen.ontbreekt (3 nieuwe)

- `niet-recurrente-verrichtingen` ↔ `bedrijfsresultaat` (recurrent vs niet-recurrent + KB 21/10/2018-overgang)
- `eigen-aandelen` ↔ `financiele-vaste-activa` (eigen aandelen niet als activa)
- `bewaring-boekhoudstukken` ↔ fiscale bewaartermijn (7 jaar boekhouding vs 10 jaar fiscaal)

---

## Deel B — Synthese-records voorgesteld

Drie synthese-records aangemaakt in `data/concepten/records/`. Elk schema 1.4 + `node_type: synthese`, met inleiding, vergelijkingstabel (markdown met wikilinks), beslisboom (Mermaid `flowchart TD`), kerninzichten + `_provenance.inputs[]`.

### 1. `boekhoudbeginselen-overzicht`

**Anchors**: 1.1.I, 1.1.I.B, 1.1.II.S, 1.2.V, 1.2.V.A
**Cluster**: 7 beginselen + 1 begrip (aanvullende-boekhoudbeginselen)
**Sleutel-inzicht**: drie-lagen-structuur (voorwaarden / waardering / eindbeginsel) i.p.v. platte lijst. Lost impliciet de hoog-prio gap `records.ontbreekt: boekhoudkundige-beginselen` op.
**Mermaid-flowchart**: drie kolommen met de 7 beginselen + cross-edges via `vereist-kennis-van`.
**Cast-namen**: Meubelzaak Mertens BV, Transport Tongeren BV.

### 2. `boekjaar-eindprocedure-checklist`

**Anchors**: 1.1.I, 1.1.I.A, 1.1.II.L, 1.1.II.Q, 1.1.II.S, 1.1.taak.1, 1.2.taak.1
**Cluster**: 9 records (regelmatige-boekhouding, inventaris, overlopende-rekeningen, afschrijvingen, waardeverminderingen, voorzieningen, jaarrekening, resultaatverwerking, wettelijke-reserve)
**Sleutel-inzicht**: bindende volgorde (14 stappen) van proefbalans tot neerlegging bij de NBB; wettelijke termijnen (AV binnen 6 maanden, neerlegging binnen 30 dagen na AV).
**Mermaid-flowchart**: lineaire flow met sub-branches voor eindejaarsverrichtingen + winst/verlies-verdeling.
**Cast-namen**: Naaiatelier Ninove BV (boekjaar 31 dec).
**Lost impliciet de midden-prio gap `records.ontbreekt: jaarafsluiting` op** (vier records verwijzen ernaar).

### 3. `resultaat-categorisatie-beslisboom`

**Anchors**: 1.1.II.M, 1.1.II.N, 1.1.II.O, 1.1.II.P, 1.1.II.Q, 1.1.II.S
**Cluster**: 4 records (bedrijfsresultaat, financiele-verrichtingen, niet-recurrente-verrichtingen, resultaatverwerking)
**Sleutel-inzicht**: 'niet-recurrent' is sinds KB 21/10/2018 een **feitelijke** kwalificatie (eenmalig + niet-hervraagbaar), niet meer een formele 'uitzonderlijke' rubriek. Sectorafhankelijke 'normale exploitatie'-toets.
**Mermaid-flowchart**: drie criteria (normale exploitatie? — financieel activum? — eenmalig + niet-hervraagbaar?) leiden tot 3 categorieen + één 'toch bedrijfsresultaat'-fallback.
**Cast-namen**: Meubelzaak Mertens BV, Solaris Sint-Truiden BV, Verffabriek Veurne BV.
**Cross-domein**: bridge naar fiscaliteit (WIB art. 47 gespreide taxatie).

---

## Niet-gekozen kandidaten (uit briefing)

Drie kandidaten **niet** uitgewerkt om kwaliteit > kwantiteit te bewaken:

- **Balanscyclus-beslisboom** (factuur → grootboek → balans → jaarrekening): overlapt te sterk met `boekjaar-eindprocedure-checklist` en `regelmatige-boekhouding`. Toevoegen alleen zinvol als zoom-in op één transactie-cyclus, niet als synthese-record.
- **Vaste-vs-vlottende-activa-cascade**: nuttig maar minder examen-kritisch dan `resultaat-categorisatie-beslisboom`. Reservelijst voor latere pass.
- **Eigen-vs-vreemd-vermogen-overzicht**: te veel overlap met `eigen-middelen` + `schulden` records die al rijke bouwstenen hebben. Vergelijkingstabel als verrijking op `eigen-middelen` zelf is efficienter.

---

## Anti-fabricatie-controle

- Geen wetsartikelen verzonnen. Alle bron-verwijzingen via concrete `_provenance.inputs[]` chunk-id's uit RAG-v1 (CBN 174/1, CBN 2018/18, CBN 2010/12, CBN 2019/04, Richtlijn 2013/34/EU, WER art. III.83-89, KB WVV art. 3:1/3:6/3:8/3:66/3:68, MAR art. 1/6/7, WVV art. 3:1/3:10/7:211).
- Confidence-labels: alle hoofd-secties `inferred-from-aggregation`, individuele kerninzichten `grounded` waar directe bron, `inferred-from-aggregation` of `inferred` waar cross-bron-synthese.
- Cast-namen exclusief uit `data/concepten/casts/globaal.yaml`: Meubelzaak Mertens BV, Naaiatelier Ninove BV, Solaris Sint-Truiden BV, Verffabriek Veurne BV, Transport Tongeren BV.
- Bedragen in € + Belgische duizendtal-notatie: € 850.000, € 380.000, € 45.000, € 12.000, € 50.000, € 320.000, € 180.000.
- Mermaid-syntax: edge-labels zonder komma's of `(n)`-patronen (mechanisch gecontroleerd: 10 labels totaal, 0 issues).

---

## Top-3 aandachtspunten voor volgende pass

1. **`rechten-verplichtingen-buiten-balans`-trio mergen** (3-way duplicaat tussen PO 1.1 + 1.2 + 1.3). Hoog prio — gebruikersverwarring + edge-pollutie.
2. **`resultatenrekening` + `balans` als records aanmaken** — beide centrale concepten, 5 records verwijzen ernaar zonder canonical target.
3. **PO 1.1 examenvragen classificeren** zodat Check A in een volgende verify-pass uitgevoerd kan worden — dat is de enige check die nu structureel ontbreekt.
