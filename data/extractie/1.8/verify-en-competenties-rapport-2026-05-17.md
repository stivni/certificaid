# PO 1.8 — VERIFY + Competentie-destillatie rapport

**Datum**: 2026-05-17
**Run-tag**: `verify-en-competenties-1.8-2026-05-17T12:00Z`
**Model**: claude-opus-4-7 (subagent)
**Prompt-versies**: `prompts/concept-verify-v1.md` + `prompts/competentie-destillatie-v2.md` (delta op v1)
**Scope**: 44 PO 1.8 concept-records (zie `extraction-rapport-2026-05-17.md`)

---

## Deel A — VERIFY light

Check A (examenvraag-simulatie) overgeslagen volgens opdracht — `data/programma/examen_vragen/` is leeg (geen vragen voor 1.8). Alleen Check B + Check C uitgevoerd.

### Check B — Minicursus-haalbaarheid

#### Uniforme rijkheid per node-type

Richness-score per record berekend op basis van aanwezigheid van `definitie`, `main_rule`, `bouwstenen`, `berekeningsmethode`, `stappen`, `in_praktijk`, `vergelijkingsparen`, `valkuilen`.

| Node-type | Mediane richness | Onder-mediaan (dunne) |
|---|---|---|
| `begrip` (n=25) | 4 | `prijsverschil-arbeid`, `opportuniteitskost`, `flexibel-budget`, `statisch-budget`, `kostprijs-per-eenheid`, `algemene-boekhouding`, `kostensoort`, `sunk-cost`, `budgetboekhouding`, `gemiddelde-kostprijs`, `kostendrager` |
| `methode` (n=10) | 6,5 | `werkelijke-kostencalculatie`, `registratiesysteem-eenvoudige-integratie`, `registratiesysteem-proportionele-integratie`, `registratiesysteem-waarderingsneutraal` |
| `synthese` (n=3) | (niet vergelijkbaar — waarde zit in beslisboom + tabellen, niet in richness-score) | n.v.t. |
| `procedure`, `regel`, `fenomeen`, `afwegingskader` | OK | `kostenanalyse-make-or-buy` (afwegingskader zonder stappen) |

#### Geconstateerde gaps (14 nieuwe entries in `data/extractie/gaps.json`)

| record_id | aspect | prio |
|---|---|---|
| prijsverschil-arbeid | berekeningsmethode.formule | midden |
| prijsverschil-arbeid | berekeningsmethode.concreet_voorbeeld | midden |
| werkelijke-kostencalculatie | stappen.onvolledig | midden |
| registratiesysteem-waarderingsneutraal | stappen.onvolledig | laag |
| registratiesysteem-eenvoudige-integratie | stappen.onvolledig | laag |
| registratiesysteem-proportionele-integratie | stappen.onvolledig | laag |
| kostprijs-per-eenheid | berekeningsmethode.formule | midden |
| statisch-budget | in_praktijk.ontbreekt | laag |
| flexibel-budget | berekeningsmethode.concreet_voorbeeld | midden |
| opportuniteitskost | in_praktijk.ontbreekt | laag |
| kostendrager | vergelijkingsparen.ontbreekt | midden |
| budgetboekhouding | definitie.onvolledig | laag |
| verschillenboekhouding | records.overlappend-fenomeen | midden |
| kostenanalyse-make-or-buy | stappen.onvolledig | midden |

#### Hoogste-prioriteit aandachtspunten

1. **`prijsverschil-arbeid`** — alleen definitie. Mist berekeningsmethode + formules + numeriek voorbeeld terwijl het concept zelf precies daarover gaat (tariefverschil + efficiëntieverschil splitsen). Overweeg merge in `verschillenboekhouding` als sectie 'arbeidsverschil' óf uitwerken tot autonoom rijk record met formules + cast-voorbeeld.
2. **`werkelijke-kostencalculatie`** — node_type `methode` maar geen stappen/berekeningsmethode/in_praktijk. Alleen bouwsteen + vergelijkingspaar tegenover `voorbepaalde-kosten`. Voor minicursus te dun; ofwel rijker maken ofwel demoten tot `begrip` met expliciete cross-link.
3. **`kostprijs-per-eenheid`** — centraal-genoeg begrip dat drie gebruiksvormen (vervaardiging / volledig / variabel) heeft. Mist een berekeningsmethode-blok dat de drie waarden ontleedt met cast-bedragen.

### Check C — Semantische coherentie

#### C1 — Mechanische checks (deterministisch)

- **Vergelijkingsparen-targets**: alle 18+ vergelijkingsparen verwijzen naar bestaande record-ids.
- **Edges-targets**: alle edges (44 records, gemiddeld 4-8 edges per record) verwijzen naar bestaande record-ids.
- **Edges zonder type**: 0.

#### C2 — LLM-oordeel

- **Overlappende fenomenen** (jaccard-heuristiek op klassieke verwarringen):
  - `directe-kosten` ↔ `variabele-kosten`: 0,07 → goed afgebakend.
  - `indirecte-kosten` ↔ `vaste-kosten`: 0,08 → goed afgebakend.
  - `marginale-kostprijs` ↔ `gemiddelde-kostprijs`: 0,16 → goed afgebakend.
  - `statisch-budget` ↔ `flexibel-budget`: 0,20 → vergelijkingsparen aanwezig, OK.
  - `werkelijke-kostencalculatie` ↔ `voorbepaalde-kosten`: 0,08 → goed afgebakend.
  - `verschillenboekhouding` ↔ `prijsverschil-arbeid`: enige bouwsteen-overlap gevlagd (gap `records.overlappend-fenomeen`).
- **Vrije-tekst-verwijzingen niet gespiegeld**: bij steekproef niet aangetroffen — extractor heeft consequent vergelijkingsparen + edges gebruikt.

### Schema 1.4 mechanical aspects

Resultaten (na deterministische scan):

- `cast.niet-toegepast`: 0 — geen "M / D1 / X / Y / ABC / DEF" patroon in voorbeelden.
- `formule.geen-variabelen`: 0 — alle `formules[]` blokken hebben `variabelen[]`.
- `bedragen.format-incorrect`: 0 in voorbeelden (heuristiek vond enkel "2026" in provenance-metadata, geen echte bedragen).
- `balans.klopt-niet` / `boeking.klopt-niet`: niet manueel gecontroleerd in deze run (worden geadresseerd in een aparte balans-validatie-pass).

---

## Deel B — Synthese (max 1 extra)

**Beslissing**: GEEN extra synthese-record toegevoegd.

Overweging `kostentypologie-beslisboom`: bestaande synthese-record `typologie-van-kosten` dekt al beide assen (directe/indirecte × vast/variabel) via een mermaid-beslisboom én bevat in_praktijk-blok met CBN 132/7-grounding. Een nieuwe `kostentypologie-beslisboom`-synthese zou ≥ 60 % overlap geven zonder pedagogische meerwaarde. Conservatief skip.

---

## Deel C — Competentie-destillatie

### 9 competenties voorgesteld

Alle yamls in `data/concepten/competenties/`, schema-versie **1.1**, status **voorgesteld**, _provenance-tag `competentie-destillatie-v2-1.8-2026-05-17`.

| # | id | Stappen | wettelijk_pct | praktijk_pct | gebaseerd_op (n) |
|---|---|---|---|---|---|
| 1 | `opzetten-analytisch-rekeningenstelsel` | 5 | 25 | 75 | 10 |
| 2 | `toepassen-volledige-kostencalculatie` | 4 | 35 | 65 | 10 |
| 3 | `toepassen-direct-costing-en-contributiemarge` | 4 | 10 | 90 | 9 |
| 4 | `uitvoeren-break-even-analyse` | 3 | 0 | 100 | 5 |
| 5 | `opstellen-master-budget` | 5 | 5 | 95 | 9 |
| 6 | `berekenen-interpreteren-budgetverschillen` | 5 | 0 | 100 | 9 |
| 7 | `uitvoeren-make-or-buy-beslissing` | 4 | 0 | 100 | 8 |
| 8 | `bepalen-vervaardigingsprijs-kb-21-10-2018` | 5 | 75 | 25 | 9 |
| 9 | `toepassen-abc-methode-op-productlijn` | 5 | 5 | 95 | 8 |

**Totaal stappen**: 40
**`praktijk_pct` > 70 %** (mens-review nodig): 7/9 — verwacht voor PO 1.8 omdat de meeste methodes management-accounting-doctrine zijn zonder Belgische wetsverankering.

### Cast-conventie

Alle scenario's en substappen gebruiken **Yperse Werkplaats BV** (kostenanalyse-volledig-scenario uit `data/concepten/casts/globaal.yaml`) met de drie kostencentra Spinnerij / Weverij / Confectie en de productlijnen tapijt-standaard / tapijt-luxe / kleed-handgeknoopt. Bedragen consistent met extractie-rapport:

- Vaste kosten jaarbasis: € 800.000
- Verkoopprijs tapijt-standaard: € 60; variabele kost € 13; contributiemarge € 47
- Break-even-volume: 17.022 tapijten
- Verwacht volume: 25.000 tapijten → veiligheidsmarge 31,9 %
- Standaard arbeidsuurtarief: € 25/uur
- Vervaardigingsprijs tapijt-standaard berekend: € 61,40

### Anti-fabricatie-checks

- Alle competenties hebben `gebaseerd_op_concepten` ≥ 2 (range 5-10).
- `wettelijk_pct + praktijk_pct == 100` voor alle 9.
- Elke stap heeft een `grondslag`-veld (mechanisch geverifieerd na hervalidatie).
- Vakdoctrine-claims expliciet aangeduid via `inferred-common-knowledge`-confidence in onderliggende concept-records; competentie-motiveringen verwijzen consequent naar "vakdoctrine" of "management-accounting-doctrine".
- Wettelijke claims uitsluitend gegrond op:
  - **KB 21.10.2018** (art. 22 vervaardigingsprijs, art. 23 aanschaffingsprijs, art. 28 + 100 voorraadwaardering, MAR-bijlage 1 klasse 9)
  - **CBN 132/7** (vervaardigingsprijs §2.1, lagere-marktwaarde)
  - **CBN 2012/15** (direct costing toegelaten, voorraad op balans aan vervaardigingsprijs)
  - **CBN 3/3** (waarderingsneutraliteit-principe)

### Cross-competentie wikilinks

De volgende competenties verwijzen naar elkaar (didactisch dependency-graph):

- `toepassen-volledige-kostencalculatie` → gebruikt door `opstellen-master-budget`, `bepalen-vervaardigingsprijs-kb-21-10-2018`, `toepassen-abc-methode-op-productlijn`
- `opzetten-analytisch-rekeningenstelsel` → fundament voor alle andere
- `toepassen-direct-costing-en-contributiemarge` → fundament voor `uitvoeren-break-even-analyse`, `uitvoeren-make-or-buy-beslissing`
- `opstellen-master-budget` → fundament voor `berekenen-interpreteren-budgetverschillen`
- `bepalen-vervaardigingsprijs-kb-21-10-2018` → cross-link uit `toepassen-abc-methode-op-productlijn` (ABC kan voorraadwaardering voeden mits scope-restrictie)

---

## Open observaties / follow-ups

1. **`prijsverschil-arbeid`**: overweeg in een volgende enrich-pass mergen in `verschillenboekhouding` of zelf rijker maken met berekeningsmethode + formules + cast-voorbeeld.
2. **`werkelijke-kostencalculatie`**: ofwel demoten tot `begrip`, ofwel rijker maken met stappen (jaarafsluitings-procedure: standaardkost → werkelijke kost → herwaardering voorraad).
3. **`registratiesysteem-*`-trio**: methode-records zonder stappen; functioneren nu meer als type-omschrijvingen. Bij volgende enrich-pass beslissen of een gemeenschappelijke procedure-stap (klasse-6 ↔ klasse-9 koppeling) wordt toegevoegd of of het type wijzigt naar `begrip`.
4. **`kostenanalyse-make-or-buy`** (afwegingskader-record): nu via competentie `uitvoeren-make-or-buy-beslissing` afgedekt. Concept-record zelf zou een uitgewerkt afwegingsstappen-blok kunnen krijgen om autonome study-waarde te vergroten.
5. **Validator-schema-1.1**: `tools/leermateriaal/lib/validate_competentie.py` moet de nieuwe stap-blok-velden (`wat`, `hoe`, `voorbeeld.substappen`) accepteren — niet gedraaid in deze run; manueel via PyYAML geverifieerd.
6. **PO 1.1-coördinatie**: stub-records `algemene-boekhouding` en `voorraadwaardering` blijven aanwezig in PO 1.8-scope; bij PO 1.1-extractie eventueel mergen of expliciete cross-PO-relatie via primary-record.

---

## Status

- **`data/extractie/gaps.json`**: 14 nieuwe gaps toegevoegd (totaal 139).
- **`data/concepten/competenties/`**: 9 nieuwe YAMLs (schema 1.1, status `voorgesteld`).
- **Geen nieuwe synthese-record** toegevoegd (overlap met bestaande `typologie-van-kosten`).
- **Geen records bijgewerkt** — VERIFY is read-only volgens prompt.
- **Geen commit** — workflow eindigt hier; eventuele commit en validator-run gebeurt in een vervolg-task.
