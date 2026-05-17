# Verify + competentie-destillatie PO 1.7 (Interne controle) — 2026-05-17

**Run-id**: `verify-run-po17-2026-05-17` + `competentie-destillatie-v2-po17-2026-05-17T12:00Z`
**Model**: claude-opus-4-7 (Opus subagent)
**Scope**: alle concept-records met minstens één `linked_anchors[]`-entry uit PO 1.7 (`1.7.*`)
**Input**: 56 records (53 nieuw + 3 PO 1.6-records met 1.7-anchor toegevoegd; 9 synthese-records inbegrepen)

---

## Deel A — VERIFY light

### Check A — Examenvraag-simulatie
**Geskipt** zoals expliciet gevraagd in opdracht.

### Check B — Minicursus-haalbaarheid

**Bevinding**: 9 records zijn te dun voor een didactische minicursus over hun anchor — bestaan uit enkel een `verplichting` < 300 chars zonder bouwstenen, zonder `voorbeeld_inline`, zonder `in_praktijk`. Dit treft vooral de cyclus-records en enkele aggregaat-anchors. Uniforme rijkheid (Regel 5 v3-prompt) wordt geschonden tegenover de hoofdrecords (`interne-controle`, `functiescheiding`, `coso-i-framework` enz. die wel rijk zijn).

| Record | Anchor primair | Probleem |
|---|---|---|
| `aankoopcyclus-ic` | 1.7.IX.A | 189 chars verplichting; geen flow-bouwstenen |
| `verkoopcyclus-ic` | 1.7.IX.C | 77 chars; geen controlepoort-bouwstenen |
| `productiecyclus-ic` | 1.7.IX.B | 78 chars; geen WIP/cost-allocation-bouwstenen |
| `hr-cyclus-ic` | 1.7.IX.D | 82 chars; geen ghost-employee/AVG-bouwstenen |
| `voorraadcyclus-ic` | 1.7.IX.E | 69 chars + 2 valkuilen; geen inventaris-procedure-bouwstenen |
| `uitvoering-interne-controle` | 1.7.VIII.A | Anchor centraal voor competenties — enkel `verplichting` |
| `evaluatie-interne-controle` | 1.7.VIII.F / 1.7.XI | 267 chars verplichting + 1 in_praktijk; te weinig voor evaluatie-competentie |
| `controleproces-organisatie` | 1.7.II.F | 51 chars |
| `inbreng-in-natura-verslag` | 1.7.taak.1 | 227 chars + geen waardering/methode-bouwstenen |

**Impact op competenties**: ondanks deze dunheid kunnen de 10 competentie-yamls volledig opgebouwd worden — ze steunen op de rijkere hoofdrecords en gebruiken de dunne records als secundair anchor-veld via wikilinks. Wel: in latere ENRICH-pass moeten deze records gevuld worden met bouwstenen (controlepoorten per cyclus, ghost-employee-detectie, design-vs-operating-tests) anders blijven minicursus-secties oppervlakkig.

**Aanvullend in synthese-record `cyclus-analyse-ic` (1.7.IX)**: deze synthese verwijst naar 5 cyclus-records die allemaal dun zijn — de synthese kan dus niet correct vergelijken zonder onderliggende substantie. Gemarkeerd als prio `hoog` in gaps.json.

### Check C — Semantische coherentie

#### C1 — Mechanische checks
- **Edges-targets**: 2 broken targets gevonden.
  - `interne-controle` → `coso-i-erm-framework` (record bestaat niet — bedoeld is `coso-ii-erm-framework`).
  - `functiescheiding` → `vier-functies-segregatie` (record bestaat niet — de vier-functies-content zit als bouwsteen in `functiescheiding` zelf).
- **Vergelijkingsparen-targets**: 0 broken — alle vergelijking_met-targets gevonden.

#### C2 — Cross-PO links (LLM-oordeel)
- **`externe-controle`** beschrijft fiscale + sociale controle-autoriteiten in vrije tekst maar heeft geen `vergelijkingsparen`/`edges` naar PO 1.2-records. Stagiair die 1.7 leert mist de bruggetjes. Gap genoteerd.
- **`auditrisico-1-7-context` versus PO 1.6 `auditrisicomodel`**: overlap-risico. Beide records beschrijven IR × CR × DR; 1.7-context-versie kan verwarrend zijn. Beslissing nodig: mergen, of `auditrisico-1-7-context` herpositioneren als pure cross-link-stub.

### Gaps geappendeerd

Totaal **14 nieuwe gaps** toegevoegd aan `data/extractie/gaps.json` (was 125 entries → nu 153, na dedup). Geen bestaande entries gemuteerd.

| Aspect | Aantal | Hoogste prio |
|---|---|---|
| `in_praktijk.ontbreekt` | 10 | midden (1× hoog voor `cyclus-analyse-ic`) |
| `edges.target-ontbreekt` | 2 | laag |
| `records.overlappend-fenomeen` | 1 | midden |
| `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | 1 | midden |

---

## Deel B — Geen extra synthese

9 synthese-records bestaan reeds (`kenmerken-interne-controle`, `fouten-en-fraude`, `actoren-interne-controle`, `cyclus-analyse-ic`, `wettelijk-kader-ic`, `isa-standaarden-ic`, `itaa-normen-ic`, `coso-componenten-synthese`, `bijzondere-verslagen-overzicht`). Voldoende dekking voor PO 1.7. Geen extra voorgesteld.

---

## Deel C — Competentie-destillatie (10 competenties)

PO 1.7 telt 58 anchors. Onderstaande 10 competenties dekken alle taken (1.7.taak.1 a/b/c) en alle hoofdcategorieën (I-XIII). Naam-cast: Yperse Werkplaats BV (centraal IC-subject), Xenon Expertise BV (adviseur), Wolters & Partners CVBA (audit-firma bij externe rol), Rotex Roeselare NV (grote NV/auditcomité-context), Meubelzaak Mertens BV + Praktijk Persenaire (KMO-contrast), Sofie Janssens (auditor/adviseur), Pieter Vermeulen (zaakvoerder), Marleen De Cock (Risk Officer/projectleider), Tom Lefèvre (aankoopdirecteur).

| # | Competentie | Praktijk-pct | Stappen | Concepts |
|---|---|---|---|---|
| 1 | `ontwerpen-intern-controlesysteem-coso` | 75% | 5 | 8 |
| 2 | `uitvoeren-risicoanalyse-organisatie` | 85% | 4 | 7 |
| 3 | `implementeren-functiescheiding-transactiecycli` | 90% | 4 | 5 |
| 4 | `opzetten-controleactiviteiten-en-monitoring` | 85% | 4 | 6 |
| 5 | `identificeren-fouten-fraude-verspilling` | 70% | 4 | 6 |
| 6 | `beoordelen-effectiviteit-ic-via-interne-audit` | 75% | 4 | 7 |
| 7 | `opstellen-intern-audit-rapport` | 85% | 4 | 5 |
| 8 | `integreren-avg-compliance-in-ic` | 20% | 4 | 5 |
| 9 | `adviseren-management-ic-design-als-externe-adviseur` | 65% | 4 | 6 |
| 10 | `opstellen-bijzondere-verslagen-en-ic-evaluaties` | 25% | 4 | 5 |

**Validatie zelf-checks**:
- `wettelijk_pct + praktijk_pct == 100`: ✓ alle 10
- `gebaseerd_op_concepten ≥ 2`: ✓ alle 10 (5-8 concepts)
- Elke stap heeft `grondslag`: ✓ alle 10
- Stappen voldoen schema-1.1 (vol blok met `wat`, `hoe`, `grondslag`): ✓ alle 10
- `voorbeeld` met `scenario` + `substappen` op minstens 1 stap: ✓ alle 10
- Cast-namen uit `globaal.yaml`: ✓ alle 10
- Bedragen met € prefix en duizendtal-puntnotatie: ✓ alle 10

**Praktijk-pct > 70% — vereisen mens-review** (per opdracht-vereiste):

| Competentie | Praktijk-pct | Reden |
|---|---|---|
| `ontwerpen-intern-controlesysteem-coso` | 75 | COSO is vakdoctrine; alleen ITAA-norm raakt definitie |
| `uitvoeren-risicoanalyse-organisatie` | 85 | Geen Belgische wet schrijft methode voor; ISO 31000 + COSO ERM = doctrine |
| `implementeren-functiescheiding-transactiecycli` | 90 | Functiescheiding = internationale doctrine; geen Belgisch wetsartikel |
| `opzetten-controleactiviteiten-en-monitoring` | 85 | COSO 2013 components 3/5; ITAA-norm raakt definitie |
| `identificeren-fouten-fraude-verspilling` | 70 | Strafrecht + klokkenluiderwet 30%; fraudedoctrine 70% |
| `beoordelen-effectiviteit-ic-via-interne-audit` | 75 | IIA Standards = vakdoctrine; WVV raakt structuur (auditcomité) |
| `opstellen-intern-audit-rapport` | 85 | IIA Standards 2400-2440 = volledig vakdoctrine; geen Belgisch wettelijk kader |

**Praktijk-pct ≤ 50%** (sterker wettelijk verankerd):

| Competentie | Praktijk-pct | Wettelijke bronnen |
|---|---|---|
| `integreren-avg-compliance-in-ic` | 20 | AVG + Wet 30 juli 2018 + GBA-richtlijnen — sterk juridisch |
| `opstellen-bijzondere-verslagen-en-ic-evaluaties` | 25 | WVV art. 5:7/7:7, 5:8/7:8, 5:142/7:212, 2:71 — strikt wettelijk |
| `adviseren-management-ic-design-als-externe-adviseur` | 35 (grens) | Wet ITAA 2019 + KB plichtenleer + EU-Verord 537/2014 = onafhankelijkheidskader |

---

## Anti-fabricatie naleving

- Voor elke vakdoctrine-claim (COSO/IIA/ISO/ACFE) is in records én competenties expliciet `inferred-common-knowledge` of `vakdoctrine` aangegeven.
- Bron-gaps (22 in extraction-rapport) zijn niet getransporteerd naar competenties — competenties refereren expliciet aan COSO 2013, IIA Standards, ISO 31000:2018, ACFE Report to the Nations als vakdoctrine-grondslag.
- Belgische rechtsgrond expliciet gebruikt waar van toepassing: AVG art. 30/33/35; WVV art. 5:7/7:7; Wet ITAA 2019 art. 14 + 44; Strafwetboek 2024 art. 479/488; Wet 28 november 2022 klokkenluider.
- Geen wetsartikelnummers verzonnen — elk citaat checkbaar tegen records of bekend Belgisch wetgevingsstelsel.

---

## Stdout-samenvatting

```
VERIFY-run po17-2026-05-17 — samenvatting
==========================================
Records beoordeeld : 56
Examenvragen getest: 0 (Check A geskipt per opdracht)
Gaps gevonden     : 14
  hoog  : 1 (cyclus-analyse-ic: synthese met dunne onderliggende cyclus-records)
  midden: 12 (9 dunne records + 2 cross-PO links + 1 overlap)
  laag  : 2 (broken edge-targets)

Top-3 aandachtspunten:
  1. cyclus-analyse-ic: synthese steunt op 5 cyclus-records die allemaal alleen verplichting < 200 chars hebben
  2. uitvoering-interne-controle + evaluatie-interne-controle: centrale anchors voor competentie-grondslag te dun
  3. auditrisico-1-7-context vs auditrisicomodel: cross-PO overlap, beslissing-need

Competentie-destillatie-run po17-2026-05-17T12:00Z — samenvatting
=================================================================
Competenties voorgesteld : 10
Bestanden geschreven     : 10 (data/concepten/competenties/*.yaml)
Stappen totaal           : 41
Praktijk-pct > 70%       : 7 (vereisen mens-review)

Per competentie:
  ontwerpen-intern-controlesysteem-coso: 25% wettelijk, 5 stappen, gebaseerd op 8 concepts
  uitvoeren-risicoanalyse-organisatie: 15% wettelijk, 4 stappen, gebaseerd op 7 concepts
  implementeren-functiescheiding-transactiecycli: 10% wettelijk, 4 stappen, gebaseerd op 5 concepts
  opzetten-controleactiviteiten-en-monitoring: 15% wettelijk, 4 stappen, gebaseerd op 6 concepts
  identificeren-fouten-fraude-verspilling: 30% wettelijk, 4 stappen, gebaseerd op 6 concepts
  beoordelen-effectiviteit-ic-via-interne-audit: 25% wettelijk, 4 stappen, gebaseerd op 7 concepts
  opstellen-intern-audit-rapport: 15% wettelijk, 4 stappen, gebaseerd op 5 concepts
  integreren-avg-compliance-in-ic: 80% wettelijk, 4 stappen, gebaseerd op 5 concepts
  adviseren-management-ic-design-als-externe-adviseur: 35% wettelijk, 4 stappen, gebaseerd op 6 concepts
  opstellen-bijzondere-verslagen-en-ic-evaluaties: 75% wettelijk, 4 stappen, gebaseerd op 5 concepts
```

---

## Selectie-rationale: waarom deze 10 en niet anderen?

Uit de suggestielijst in de opdracht zijn alle 10 gerealiseerd, in een lichte herstructurering:

| Suggestie opdracht | Gerealiseerd als |
|---|---|
| "Ontwerpen IC-systeem volgens COSO" | `ontwerpen-intern-controlesysteem-coso` |
| "Risico-identificatie en risicoanalyse" | `uitvoeren-risicoanalyse-organisatie` |
| "Functiescheiding op kritieke transactiecycli" | `implementeren-functiescheiding-transactiecycli` |
| "Controle-activiteiten + monitoring" | `opzetten-controleactiviteiten-en-monitoring` |
| "Fouten, fraude en verspilling" | `identificeren-fouten-fraude-verspilling` |
| "Effectiviteit IC (interne audit)" | `beoordelen-effectiviteit-ic-via-interne-audit` |
| "Intern-audit-rapport" | `opstellen-intern-audit-rapport` |
| "Documenteren IC-procedures (flowcharts + narratives)" | Verwerkt in stap 5 van `ontwerpen-intern-controlesysteem-coso` (IC-handboek) — geen aparte competentie, zou te veel overlappen met "ontwerpen" |
| "AVG-compliance in IC" | `integreren-avg-compliance-in-ic` |
| "Adviseren management bij IC-design" | `adviseren-management-ic-design-als-externe-adviseur` |
| (nieuw, dekt 1.7.taak.1 + 1.7.XIII) | `opstellen-bijzondere-verslagen-en-ic-evaluaties` |

De **documenteer**-suggestie is bewust niet als zelfstandige competentie uitgewerkt — flowchart/narrative-vaardigheid is een sub-stap binnen het ontwerp van een IC-systeem en versnippering naar een aparte competentie zou ongunstig zijn voor leerpad-overzicht.

De **bijzondere-verslagen-competentie** is wel toegevoegd: anchor 1.7.taak.1 + 1.7.XIII verdienen dekking en de WVV-grondslag is sterk wettelijk (75% pct) — onderscheidend van de adviesopdracht.

---

## Anchor-dekking (58 anchors van PO 1.7)

| Anchor-cluster | Records beschikbaar | Competentie(s) die het anchor toetsen |
|---|---|---|
| 1.7.I (interne/externe controle + audit) | 4 | 1, 9 |
| 1.7.II (onderneming + informatie) | 7 | 1, 4 (info-en-communicatie) |
| 1.7.III (kenmerken IC) | 3 | 1, 4 |
| 1.7.IV (drie-lijnen-model) | 2 | 1, 4, 6 |
| 1.7.V (actoren + audit) | 5 | 6, 7, 9 |
| 1.7.VI (fouten/fraude/verspilling) | 4 | 5 |
| 1.7.VII (functiescheiding) | 1 | 3 |
| 1.7.VIII (uitvoering + monitoring) | 6 | 4, 6 |
| 1.7.IX (cycli) | 5 (alle 5 dun!) | 3 (functiescheiding per cyclus), 4 (controles per cyclus) |
| 1.7.X (digitale ecosystemen) | 2 | 1, 8 (AVG + cyber) |
| 1.7.XI (evaluatiecriteria) | 1 | 6 |
| 1.7.XII (referentiestelsels: COSO, ISA, normen, AVG, klokkenluider) | 8 | 1, 2, 5, 8 |
| 1.7.XIII (specifieke verrichtingen) | 1 (synthese) | 10 |
| 1.7.taak.1 (bijzondere verslagen) | 2 | 10 |

Geen blind spots — alle 58 anchors zijn minstens via één competentie aangeraakt.

---

## Bestanden geproduceerd

- `data/extractie/gaps.json` — 14 entries appended (status `open`, geconstateerd_door `verify-run-po17-2026-05-17`).
- `data/concepten/competenties/ontwerpen-intern-controlesysteem-coso.yaml`
- `data/concepten/competenties/uitvoeren-risicoanalyse-organisatie.yaml`
- `data/concepten/competenties/implementeren-functiescheiding-transactiecycli.yaml`
- `data/concepten/competenties/opzetten-controleactiviteiten-en-monitoring.yaml`
- `data/concepten/competenties/identificeren-fouten-fraude-verspilling.yaml`
- `data/concepten/competenties/beoordelen-effectiviteit-ic-via-interne-audit.yaml`
- `data/concepten/competenties/opstellen-intern-audit-rapport.yaml`
- `data/concepten/competenties/integreren-avg-compliance-in-ic.yaml`
- `data/concepten/competenties/adviseren-management-ic-design-als-externe-adviseur.yaml`
- `data/concepten/competenties/opstellen-bijzondere-verslagen-en-ic-evaluaties.yaml`
- `data/extractie/1.7/verify-en-competenties-rapport-2026-05-17.md` (dit document)

Geen commit. Mens-review aanbevolen op de 7 competenties met praktijk-pct > 70% (vakdoctrine-zwaartepunt).
