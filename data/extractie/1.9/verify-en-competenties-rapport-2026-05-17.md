# VERIFY-pass + Competentie-destillatie PO 1.9 — rapport

**Programmaonderdeel**: 1.9 Financiële analyse (bekwaamheid)
**Run-id**: `verify-run-po-1.9-2026-05-17T03:00Z` + `competentie-destillatie-v2-po-1.9-run-2026-05-17T03:00Z`
**Model**: claude-opus-4-7 (subagent)
**Scope**: 38 records gelinkt aan PO 1.9 (13 nieuwe records + 25 uitgebreide PO 1.3-records)
**Budget**: ~1.5u

---

## Deel A — VERIFY light

### Check A — Examenvraag-simulatie

**Geskipt** (per opdracht). PO 1.9-examenvragen hebben nog geen 1.9-anchor-labels in `data/programma/examen_vragen/`; bovendien expliciet geskipt door opdrachtgever.

### Check B — Uniforme rijkheid van 38 records linked aan 1.9

**Verdict: rijkheid uniform per node-type — geen blokkerende dunheid.**

Mechanische rijkheid-check (`tools/lib/retrieval` niet gebruikt — directe JSON-inspectie):

#### methode-records (6 nieuwe + 2 uitgebreide)
| Record | doel | bouwstenen | berekening | stappen | drempels | in_praktijk | valkuilen | edges | vp |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| altman-z-score | ✓ | 2 | 1 | — | 3 | — | 2 | 3 | 1 |
| ohlson-o-score | ✓ | 2 | — | — | — | 1 | 1 | **1** | 1 |
| interpretatie-financiele-ratios | ✓ | — | — | 4 | — | 1 | 1 | 4 | — |
| herstructurering-resultatenrekening | ✓ | 3 | — | — | — | **—** | — | 2 | 1 |
| toegevoegde-waarde-financiele-analyse | ✓ | 2 | 1 | — | — | 1 | — | 2 | 1 |
| tabel-waardemutaties | ✓ | 2 | — | — | — | 1 | — | 2 | — |

Lichte rijkheidsverschillen:
- `ohlson-o-score` heeft slechts 1 edge tegenover 3 bij `altman-z-score`. Voor uniforme cross-linking gewenst: edges naar `solvabiliteitsratio`, `falen-van-de-onderneming` en `current-ratio` (de 9 Ohlson-variabelen raken die). → gap gelogd.
- `herstructurering-resultatenrekening` mist `in_praktijk[]` waar 4 van 6 methode-records het wel hebben. → gap gelogd (laag).

#### begrip-records (4 nieuwe)
| Record | definitie | bouwstenen | berekening | in_praktijk | valkuilen | edges | vp |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| behoefte-aan-bedrijfskapitaal | ✓ | 2 | 1 | — | 1 | 2 | 1 |
| financiele-analyse-software | ✓ | 2 | — | 1 | 1 | 2 | — |
| financiering-met-eigen-vermogen | ✓ | 2 | — | — | — | 3 | 1 |
| financiering-met-derdenkapitaal | ✓ | 2 | — | — | — | 3 | 1 |

Uniform per node-type. Geen gaps.

#### synthese-records (2 nieuwe)
| Record | vergelijkingstabel | beslisboom | in_praktijk | valkuilen | edges |
|---|:-:|:-:|:-:|:-:|:-:|
| kasstroomoverzicht-drie-segmenten | ✓ | ✓ | 2 | 1 | **0** |
| kwantitatieve-financiele-diagnose | ✓ | ✓ | 2 | — | **0** |

Beide synthese-records hebben `gebaseerd_op_concepten[]` maar geen `edges[]`-veld — formeel mis. Vergelijk met PO 1.3-synthese `ratio-vier-doelen-vergelijking` dat wel edges per onderdeel-concept heeft. → 2 gaps gelogd (laag, want RAG-graph-retrieval niet kritisch in fase 0).

#### fenomeen-record (1 nieuw)
- `falen-van-de-onderneming`: definitie ✓, 2 bouwstenen, 1 in_praktijk, 1 valkuil, 3 edges. Rijk.

### Check C — Semantische coherentie

#### C1 — Mechanische edge- en vergelijkingsparen-target-check

**Alle 23 edges en 8 vergelijkingsparen-targets resolven** naar bestaande records (341 in totaal). Geen target-misses. Geen gaps voor deze sub-check.

#### C2 — Wikilink-targets in vrije tekst

Regex-scan op `\[\[<slug>\]\]` in alle tekstvelden van de 13 nieuwe records: **0 unresolved**. Goed gespiegeld.

#### C3 — Overlappende fenomenen

Geen overlappende-fenomeen-detecties tussen de 13 nieuwe records onderling of t.o.v. de 25 uitgebreide PO 1.3-records. Wel een naderingsobservatie: `cashflow-analyse` (PO 1.3) en `kasstroomoverzicht-drie-segmenten` (PO 1.9, synthese) zijn complementair — niet overlappend. Het verschil is duidelijk in beide: cashflow = één bedrag (vereenvoudigde formule), kasstroomoverzicht = drie segmenten met Δ BBK. Goede behandeling.

### Gaps gevonden — telling

| Prio | Aantal | Aspecten |
|---|---:|---|
| hoog | 0 | — |
| midden | 2 | edges.target-ontbreekt (ohlson edges-dunheid), bron-corpus-uitbreiding (PO 1.9 vakdoctrine) |
| laag | 4 | edges.target-ontbreekt (kasstroomoverzicht-synthese), edges.target-ontbreekt (kwantitatieve-diagnose-synthese), in_praktijk.ontbreekt (herstructurering-RR), open-werk (anchor 1.9.IV.A) |

**Totaal: 6 nieuwe gap-entries appended in `data/extractie/gaps.json`.** Geen bestaande gaps gemuteerd.

### Top-3 aandachtspunten

1. **`ohlson-o-score`** is dunner gecross-linkd dan `altman-z-score`. ENRICH-pass kan dit symmetrisch maken zonder content-wijziging (alleen edges toevoegen).
2. **Bron-corpus-uitbreiding voor PO 1.9**: 9 van 13 nieuwe records hangen aan `inferred-common-knowledge`. Belgische vakliteratuur (Ooghe-Van Wymeersch, Vereeck) zou alle BBK-, kasstroom-, TW- en faillissement-claims tegelijk grounden. Hoog praktijk_pct in alle 1.9-competenties (60-95%) is direct gevolg hiervan.
3. **Synthese-records zonder `edges[]`**: een patroon — wellicht structureel niet vereist (gebaseerd_op_concepten doet het werk), maar voor consistentie met PO 1.3 `ratio-vier-doelen-vergelijking` aan te bevelen.

---

## Deel B — Synthese-record (optioneel)

**Verdict: geen nieuw synthese-record voorgesteld.**

Het suggestie-record `faillissement-modellen-vergelijking` zoals voorgesteld in de opdracht is reeds gedekt door het bestaande `kwantitatieve-financiele-diagnose` (synthese, PO 1.9.VI):
- Bevat een vergelijkingstabel Altman vs Ohlson (techniek, aantal variabelen, output, interpretatie).
- Bevat een mermaid-beslisboom voor model-keuze.
- Linkt `altman-z-score`, `ohlson-o-score` en `falen-van-de-onderneming` via `gebaseerd_op_concepten`.

Een nieuw synthese-record zou overlappen zonder pedagogische meerwaarde. **Beslissing: behoud `kwantitatieve-financiele-diagnose` als canonieke synthese voor faillissement-modellen.** Wel: bovenstaande C-gap (edges-veld toevoegen) blijft openstaan voor ENRICH.

### Andere overwogen synthese-records

- `kasstroom-bedrijfscyclus-overzicht` (voor anchor 1.9.IV.A "Kasstroom en bedrijfscyclus"): pedagogisch interessant maar de drie samenstellende records (`cashflow-analyse` + `behoefte-aan-bedrijfskapitaal` + `kasstroomoverzicht-drie-segmenten`) dekken de stof voldoende. Gelogd als open-werk gap (laag), niet als blokkerende ontbreking.

---

## Deel C — Competentie-destillatie (6 competenties)

### Strategie t.o.v. PO 1.3-competenties

PO 1.3 had 5 ratio-/diagnose-competenties (`berekenen-interpreteren-liquiditeitsratios`, `-solvabiliteitsratios`, `-rentabiliteitsratios`, `beoordelen-werkkapitaal-en-kasstroom`, `formuleren-financiele-diagnose-en-adviezen`). Voor PO 1.9 (bekwaamheid-niveau) zijn de zes nieuwe competenties **niet-overlappend met PO 1.3** en focussen op:

| Onderwerp | PO 1.3-equivalent | PO 1.9-competentie | Diepteverschil |
|---|---|---|---|
| Ratio-berekening | berekenen-interpreteren-{liquidit,solvabilit,rentabilit}-ratios | (NIET gedupliceerd) | PO 1.9 erft via referenties |
| Werkkapitaal + cashflow | beoordelen-werkkapitaal-en-kasstroom | **opstellen-driesegmenten-kasstroomoverzicht** + **bepalen-behoefte-aan-bedrijfskapitaal** | Drie segmenten i.p.v. één formule + BBK i.p.v. werkkapitaalbehoefte |
| RR-herwerking + TW | (niet aanwezig) | **herstructureren-resultatenrekening-en-toegevoegde-waarde** | PO 1.9-exclusief |
| Faillissement-modellen | (niet aanwezig) | **toepassen-faillissement-predictiemodellen** | PO 1.9-exclusief |
| IT-tools | (niet aanwezig) | **gebruiken-financiele-analyse-software** | PO 1.9-exclusief |
| Diagnose-formulering | formuleren-financiele-diagnose-en-adviezen | **stellen-bekwaamheid-financiele-diagnose** | Bekwaamheid-niveau: triangulair lezen + kwantitatieve modellen + management-aanbevelingen |

### De zes competenties — overzicht

| # | id | Stappen | wettelijk_pct | praktijk_pct | gebaseerd_op_concepten | flag mens-review |
|---|---|---:|---:|---:|---:|---|
| 1 | `herstructureren-resultatenrekening-en-toegevoegde-waarde` | 4 | 40 | 60 | 3 | ja (praktijk_pct = 60%) |
| 2 | `opstellen-driesegmenten-kasstroomoverzicht` | 4 | 25 | 75 | 6 | **ja (> 70%)** |
| 3 | `bepalen-behoefte-aan-bedrijfskapitaal` | 4 | 15 | 85 | 4 | **ja (> 70%)** |
| 4 | `toepassen-faillissement-predictiemodellen` | 4 | 5 | 95 | 4 | **ja (>> 70%)** |
| 5 | `gebruiken-financiele-analyse-software` | 4 | 10 | 90 | 4 | **ja (>> 70%)** |
| 6 | `stellen-bekwaamheid-financiele-diagnose` | 5 | 30 | 70 | 7 | ja (op grenslijn 70%) |

**Totaal stappen**: 25 stappen over 6 competenties.
**Alle competenties**: `praktijk_pct + wettelijk_pct = 100` (controle).
**Alle competenties**: ≥ 2 concepten in `gebaseerd_op_concepten` (anti-fabricatie hard-regel).
**Alle stappen**: hebben `grondslag` met wikilink of expliciete wetsverwijzing.

### Cast-discipline

Alle voorbeelden gebruiken cast-namen uit `data/concepten/casts/globaal.yaml`:
- **Rotex Roeselare NV** (hoofdcast, grote NV volledig schema, balanstotaal € 30M)
- **Verffabriek Veurne BV** (distress / vereffening — voor falen-modellen en negatieve diagnoses)
- **Meubelzaak Mertens BV** (kleine BV verkort schema — voor verkort-schema-beperkingen en RC-overschrijdings-case)
- **Zelena Bio NV** (beursgenoteerde IFRS — voor IAS 7 kasstroom-context en groei-leverage-patroon)
- **Sofie Janssens** (accountant-persona — voor uitspraken in conclusie-velden)

Geen ad-hoc "M / D / X / Y / ABC". Geen "natuurlijke persoon X".

### Praktijk_pct > 70% — bewuste keuze, mens-review-flag

PO 1.9 is bekwaamheid-niveau en sterk gestoeld op vakdoctrine (Belgische analyse-handboeken + internationale faillissement-modellen). De hoge `praktijk_pct` (60-95%) is intrinsiek aan de stof:
- Altman/Ohlson zijn vakdoctrine zonder Belgische wettelijke basis.
- BBK en kasstroom-3-segmenten zijn analytische conventies (KB WVV-schema kent geen verplicht kasstroomoverzicht in volledig schema).
- IT-tools zijn marktrealiteit zonder normatieve bron.

5 van 6 competenties zijn geflagd met `flag_mens_review`. Dit is **bewust** en niet onderhandelbaar zonder bron-corpus-uitbreiding (zie gap `po-1.9-bron-corpus`).

### Wikilinks-discipline

Alle stap-`grondslag`-velden gebruiken `[[concept-id]]`-wikilinks naar bestaande records:
- 13 nieuwe PO 1.9-records
- Bestaande PO 1.3-records (werkkapitaal, cashflow-analyse, analytische-balans, sectorvergelijking, horizontale-analyse, ratio-vier-doelen-vergelijking, liquiditeitsratio, solvabiliteitsratio, risicoparagraaf-bestuursverslag, falen-van-de-onderneming, interpretatie-financiele-ratios)

Geen wikilinks naar niet-bestaande slugs (gevalideerd via regex-scan).

### Schema 1.1-compliance

Alle 6 YAMLs volgen schema 1.1 (zie `prompts/competentie-destillatie-v2.md`):
- `schema_version: "1.1"`
- `status: voorgesteld`
- Elke stap heeft `nr`, `titel`, `wat`, `hoe`, `grondslag` (verplicht).
- Aanbevolen velden `waarom`, `input[]`, `output[]`, `voorbeeld`, `valkuilen[]` zijn ingevuld waar passend.
- `voorbeeld.substappen` met `type` (`balans` / `berekening` / `boekingsregel` / `opmerking`) bij berekenings- en balans-stappen.
- Valkuilen met `advies` (titel) + `vaak_fout` + `grondslag` (schema 1.1-conventie, niet meer `foute_aanname/correctie`).
- `_provenance.voorgesteld_door` met run-id `competentie-destillatie-v2-po-1.9-run-2026-05-17T03:00Z`.
- `_provenance.flag_mens_review` op alle 5 competenties met `praktijk_pct > 70%` plus competentie 6 op grenslijn.

---

## Bestanden gewijzigd / aangemaakt

| Bestand | Wijziging |
|---|---|
| `data/extractie/gaps.json` | 6 nieuwe gap-entries appended (4 concept-gap, 1 bron-gap, 1 proces-gap). Geen bestaande aangeraakt. |
| `data/concepten/competenties/herstructureren-resultatenrekening-en-toegevoegde-waarde.yaml` | Nieuw — schema 1.1, 4 stappen. |
| `data/concepten/competenties/opstellen-driesegmenten-kasstroomoverzicht.yaml` | Nieuw — schema 1.1, 4 stappen. |
| `data/concepten/competenties/bepalen-behoefte-aan-bedrijfskapitaal.yaml` | Nieuw — schema 1.1, 4 stappen. |
| `data/concepten/competenties/toepassen-faillissement-predictiemodellen.yaml` | Nieuw — schema 1.1, 4 stappen + beslisboom. |
| `data/concepten/competenties/gebruiken-financiele-analyse-software.yaml` | Nieuw — schema 1.1, 4 stappen. |
| `data/concepten/competenties/stellen-bekwaamheid-financiele-diagnose.yaml` | Nieuw — schema 1.1, 5 stappen + beslisboom. |
| `data/extractie/1.9/verify-en-competenties-rapport-2026-05-17.md` | Dit rapport. |

**Geen synthese-record toegevoegd** (kwantitatieve-financiele-diagnose dekt het reeds).
**Geen records overschreven.** **Geen commit uitgevoerd.**

---

## Open follow-ups (niet in deze run opgelost)

1. **ENRICH-pass voor `ohlson-o-score`** — edges symmetriseren met altman-z-score (vereist-kennis-van solvabiliteit, werkkapitaal, current-ratio + bevat-relatie van/naar kwantitatieve-financiele-diagnose).
2. **ENRICH-pass voor synthese-records** — `kasstroomoverzicht-drie-segmenten` en `kwantitatieve-financiele-diagnose`: `edges[]`-veld toevoegen voor consistente RAG-graph-coverage.
3. **Bron-corpus-uitbreiding** — Ooghe & Van Wymeersch + Vereeck handboeken als trusted bron registreren om de 9 `inferred-common-knowledge`-records (en 5 competenties met praktijk_pct > 70%) te grounden.
4. **Mens-review** — vooral op de 5 geflagde competenties: cast-bedragen plausibel-check, formule-juistheid Ohlson-coefficiënten, juridische verwijzing alarmbel-procedure (WVV art. 7:228 / 5:153), Z'/Z''-toepasbaarheid voor Belgische KMO's.
5. **PO 1.3 ↔ PO 1.9 minicursus-rendering** — bij rendering van minicursus 1.9 zal er expliciete cross-referencing naar PO 1.3 nodig zijn voor ratio-berekening (PO 1.9 erft, dupliceert niet). Render-tooling moet dit ondersteunen.

---

**Einde rapport — VERIFY + competentie-destillatie PO 1.9, 2026-05-17.**
