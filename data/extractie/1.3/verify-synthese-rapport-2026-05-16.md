# VERIFY + synthese-record-voorstellen PO 1.3

**Programmaonderdeel**: 1.3 Analyse en kritische beoordeling van de jaarrekening
**Run**: `verify-run-po-1.3-2026-05-16T16:00Z`
**Model**: claude-opus-4-7 (live verify-pass, geen subagent)
**Schema**: 1.4
**Budget**: ~30 min

---

## Deel A — VERIFY-samenvatting

### Records beoordeeld

31 records (per extractie-rapport 2026-05-16). Steekproef-diepte: getrouw-beeld-jaarrekening, current-ratio, quick-ratio, solvabiliteitsratio, debt-equity-ratio, werkkapitaal, liquiditeitsratio, rentabiliteit-eigen-vermogen-roe, rentabiliteit-totaal-activa-roa, cashflow-analyse, doelstellingen-financiele-analyse, horizontale-analyse-jaarrekening + cross-PO `getrouw-beeld.json`. Overige 19 records (bestuursverslag, gebruikers, niet-in-balans, actor-records etc.) lichter gescand op coherentie.

### Check A — Examenvraag-simulatie

**Geskipt** voor PO 1.3. Reden: examenvragen 2013-/2014-/2015- hebben nog geen 1.3.* anchor-labels in `data/programma/examen_vragen/*-labels.json`. Zonder die labelling kunnen geen 'onbeantwoordbaar uit records'-strandpunten geconstateerd worden.

→ Gelogd als open werk in `gaps.json` (record_id `po-1.3-examenvragen`, aspect `examenvragen.labels-ontbreken`, prio midden).

### Check B — Minicursus-haalbaarheid

**Verdict: minicursus 1.3 bouwbaar.** Uniforme rijkheid per node-type is uitstekend (zie extractie-rapport "Voorbeeld-minimum status" — alle 31 records halen het minimum). Centrale concepten (`getrouw-beeld-jaarrekening`, ROE, ROA, current-ratio, solvabiliteitsratio, `doelstellingen-financiele-analyse`) hebben rijke bouwstenen + cijfervoorbeelden met cast Rotex Roeselare NV.

**Lichte rijkheidsverschillen** opgemerkt maar niet geblokkeerd:
- `liquiditeitsratio` (begrip-categorie) is dunner dan haar twee specifieke kinderen (current, quick) — dit is correct gedrag voor een categorie-begrip dat naar specialisaties wijst. Geen gap.
- `cashflow-analyse` (begrip) is functioneel dunner dan ROE/ROA (methode) — passend bij hun verschillende node-types.

### Check C — Semantische coherentie

#### C1 — Mechanische edge-/vergelijkingsparen-checks

1. **`getrouw-beeld-jaarrekening` → edges[0].target = `materieel-belang-financiele-analyse`**: target-record bestaat NIET. Verwarrend duplicate: `materieel-belang-jaarrekening` bestaat wel (zelfde linked_anchors 1.3.*).
   → gap `edges.target-ontbreekt` prio laag.

Geen andere edge-target-misses gevonden in de gescande records (current, quick, solvabiliteit, ROE, ROA, werkkapitaal, liquiditeit, cashflow, doelstellingen, debt-equity, getrouw-beeld-jaarrekening, horizontale-analyse). Alle andere targets (`doelstellingen-financiele-analyse`, `current-ratio`, `quick-ratio`, `liquiditeitsratio`, `solvabiliteitsratio`, `debt-equity-ratio`, `rentabiliteit-totaal-activa-roa`, `werkkapitaal`, `cashflow-analyse`) zijn aanwezig.

#### C2 — Vrije-tekst-niet-gespiegelde verwijzingen

2. **`werkkapitaal.in_praktijk[0]`** introduceert "werkkapitaalbehoefte" als examenrelevante tegenhanger zonder edge/vergelijkingspaar; bovendien bestaat geen record `werkkapitaalbehoefte`.
   → gap `vergelijkingsparen.vrije-tekst-niet-gespiegeld` prio midden + `records.ontbreekt` prio midden.

3. **`liquiditeitsratio.bouwstenen[0]`** introduceert "cash ratio" als derde hoofdvariant met numeriek voorbeeld, zonder edge/vergelijkingspaar of eigen record.
   → gap `vergelijkingsparen.vrije-tekst-niet-gespiegeld` prio laag + `records.ontbreekt` prio laag (laag omdat current/quick voldoen voor minicursus-niveau).

#### C3 — Cross-PO duplicates

4. **`getrouw-beeld-jaarrekening` ↔ `getrouw-beeld`**: twee records voor hetzelfde fenomeen (KB WVV art. 3:1), spreidt over PO 1.1/1.2/1.3. Reeds gerapporteerd in extractie-rapport §"Cross-PO overlap"; nu ook formeel gelogd.
   → gap `records.overlappend-fenomeen` prio midden.

### Confidence-consistentie financial-analysis-formules

8 records (current-ratio, quick-ratio, liquiditeitsratio, solvabiliteitsratio, debt-equity-ratio, werkkapitaal, horizontale-analyse, verticale-analyse) zijn correct gelabeld met `confidence: inferred-common-knowledge` + `_provenance.bron_gap`. Geen labeling-inconsistenties gevonden. ROE/ROA daarentegen zijn correct als `grounded` gelabeld (CBN-2011/14 levert Belgische bron).

→ Bron-gap geaggregeerd op PO-niveau: gap `bron-corpus-uitbreiding` (po 1.3, anchor 1.3.II.C) met voorstel Ooghe & Van Wymeersch + NBB-statistieken, prio midden.

### Gaps gevonden — telling

| Prio | Aantal | Aspecten |
|---|---:|---|
| hoog | 0 | — |
| midden | 4 | overlappend-fenomeen, vrije-tekst-niet-gespiegeld (werkkapitaalbehoefte), records.ontbreekt (werkkapitaalbehoefte), bron-corpus-uitbreiding (vakdoctrine), examenvragen.labels-ontbreken |
| laag | 3 | edges.target-ontbreekt (materieel-belang-financiele-analyse), vrije-tekst-niet-gespiegeld (cash ratio), records.ontbreekt (cash ratio) |

(8 gaps totaal; 1 midden-gap betreft proces — labelling — niet record-content.)

### Top-3 aandachtspunten

1. **`getrouw-beeld-jaarrekening` vs `getrouw-beeld`** — cross-PO duplicate-merge nodig vóór minicursus 1.3 wordt gerenderd (anders dubbele kennis-laag op site). Aanbeveling: behoud `getrouw-beeld` als canonieke slug + neem 1.3-specifieke `in_praktijk[0]` (financiele-analyse-vertrekpunt) over.

2. **`werkkapitaal` mist `werkkapitaalbehoefte`-spiegeling** — examen-camouflage materiaal. Liquiditeitstekort = werkkapitaal < werkkapitaalbehoefte is een veelvoorkomende vraagvorm; zonder eigen record voor BFR/werkkapitaalbehoefte blijft die diagnose onuitgewerkt.

3. **Bron-corpus-uitbreiding voor financial-analysis-vakdoctrine** — 8 ratio-records hangen aan `inferred-common-knowledge`. Een Belgisch handboek (Ooghe & Van Wymeersch) zou alle ratio-formules grounden en het examen-vertrouwen verhogen.

---

## Deel B — Synthese-record voorstellen

**Twee** synthese-records voorgesteld en aangemaakt voor PO 1.3.

### 1. `ratio-vier-doelen-vergelijking` — De vier analyse-doelen en hun ratio's

**Motivering**: PO 1.3 cirkelt om vier doelen (liquiditeit/solvabiliteit/rentabiliteit/groei) en stagiairs verliezen het overzicht tussen 8+ ratio-records. Dit synthese-record geeft één overzicht: per doel welke ratio's, welke balans-/RR-componenten, welke gebruiker. Examen-relevant: typische vraag "welke ratio voor welke vraag?" wordt onbeantwoordbaar zonder dit overzicht. Combineert vergelijkingstabel + flowchart `gebruikersvraag → doel → ratio`.

- Pad: `data/concepten/records/ratio-vier-doelen-vergelijking.json`
- Linked anchors: 1.3.I.A, 1.3.II.C, 1.3.taak.1
- Gebaseerd op 12 concepten (4 doelstellingen + 8 ratio-records)
- 5 kerninzichten (geen verzonnen cijfers — voorbeelden uit bestaande records met Rotex Roeselare NV)
- Mermaid-discipline gerespecteerd: geen `()` of `,` in edge-labels

### 2. `liquiditeitstoets-beslisboom` — Welke liquiditeitstoets gebruik ik?

**Motivering**: Binnen de liquiditeitsfamilie (current, quick, werkkapitaal, cash, cashflow) verwarren stagiairs het strengheidsniveau en de schaal-as. Dit synthese-record geeft een beslisboom per gebruikersvraag (screening / stresstest / schaalvergelijking / kredietdossier) en koppelt aan de uitkomstinterpretatie (current < 1 → stresstest met quick → solvabiliteit als context). Bouwt voort op concrete cijfers van Rotex Roeselare NV en Meubelzaak Mertens BV (uit bestaande records).

- Pad: `data/concepten/records/liquiditeitstoets-beslisboom.json`
- Linked anchors: 1.3.II.C, 1.3.I.A, 1.3.taak.1
- Gebaseerd op 6 concepten (liquiditeit-familie + solvabiliteit + cashflow)
- 4 kerninzichten waaronder cash-ratio-gap (link naar verify-gap)
- Mermaid-flowchart gebruikt 14 nodes met scenario-uitkomsten

### Niet voorgesteld — overwogen alternatieven

- **`rentabiliteit-perspectief-vergelijking` (ROE vs ROA leverage)**: gecondenseerd opgenomen in synthese 1 als kerninzicht. Apart synthese-record zou overlap geven met de twee bestaande ratio-records die elk al een rijke `vergelijkingsparen`-entry hebben.
- **`getrouw-beeld-toezichtsketen-end-to-end`**: pedagogisch interessant maar zonder eerst de getrouw-beeld-merge op te lossen (gap-3) zou dit een synthese rond een gefragmenteerd fenomeen worden. Aanbevolen: ná dedup-merge.

---

## Bestanden gewijzigd

| Bestand | Wijziging |
|---|---|
| `data/extractie/gaps.json` | 8 nieuwe gap-entries appended (7 concept-gaps + 1 bron-gap), aspect_type `concept-gap`/`bron-gap`/`proces-gap`. Geen bestaande entries aangeraakt. |
| `data/concepten/records/ratio-vier-doelen-vergelijking.json` | Nieuw synthese-record (schema 1.4, node_type synthese). |
| `data/concepten/records/liquiditeitstoets-beslisboom.json` | Nieuw synthese-record (schema 1.4, node_type synthese). |
| `data/extractie/1.3/verify-synthese-rapport-2026-05-16.md` | Dit rapport. |

Geen records overschreven. Geen commit uitgevoerd.

---

**Einde rapport — VERIFY + synthese PO 1.3, 2026-05-16.**
