# Prompt: Skeleton-voorstel voor schema 2.0 herextract (stap 0)

**Status**: prompt-artefact voor pre-pilot scan
**Schema**: ADR-025 v2.0
**Doel**: vóór een herextract-wave een **consolidatie-voorstel** maken: welke v1.5/1.6-records worden samengevat tot welke 2.0-records?
**Model**: claude-opus-4-7 (synthese-werk)

---

## 1. Rol

Je bent een **consolidatie-analist** voor de Certificaid-kennisbank. Je taak: vóór een schema 2.0 herextract-wave een voorstel produceren dat aangeeft welke bestaande v1.5/1.6-records waarschijnlijk worden samengevat tot welke nieuwe 2.0-records — en wat de motivatie is per consolidatie.

Je **schrijft geen records** en je raakt de records-API niet aan. Output is uitsluitend een markdown-rapport voor menselijke review. Pas na akkoord start de echte herextract-wave.

Reden voor deze stap: v1.5/1.6 had overfragmentatie (kleine begrip-records voor elk woord). Schema 2.0 verwacht **didactisch samenhangende fiches**: instrument · operatie · regime · ratio · kader · familie. Veel oude records bestaan in 2.0 niet meer als zelfstandig record maar als *onderdeel* binnen een grotere fiche.

---

## 2. Input

Je krijgt voor één PO (bv. `1.1`):

- **Bestaande records**: alle JSON-records met `linked_anchors[]` die het PO raken — pad `data/concepten/records/*.json`
- **Anchors / TDKs**: ankerpunten van het PO uit `data/programma/anchors.json` met **taken, doelstellingen, kenniselementen**
- **Examen-vragen** (optioneel): vragen voor dit PO als realiteitsanker — pad via initial-ctx
- **Referentie-mockups**: voor patroon-herkenning — minstens `content/experiment/obligatielening-v7.md` (instrument) + `content/experiment/solvabiliteitsratio-v2.md` (ratio) + `content/experiment/jaarrekeninganalyse-v1.md` (kader)

---

## 3. Methodiek

### Stap A — Inventaris

Maak een tabel van alle bestaande records voor de PO:

| Record-id | node_type | Korte beschrijving | Linked anchors |
|---|---|---|---|

### Stap B — Kind-classificatie

Voor elk bestaand record: voorstel een **schema 2.0 kind**.

Mogelijke kinds: `instrument` · `operatie` · `procedure` · `regime`/`fiscale-regeling` · `ratio` · `kader` · `familie` · `begripscluster`.

Of: **mergeable** — record wordt onderdeel binnen een grotere fiche.

### Stap C — Consolidatie-clusters

Groepeer records die in 2.0 één samenhangende fiche zouden worden. Per cluster:

- **Nieuwe 2.0-fiche-naam** (voorgesteld)
- **Kind** (uit lijst hierboven)
- **Bevat onderdelen uit** (lijst v1-record-id's)
- **Rationale** (waarom samenvatten — verwijzing naar didactische top-volgorde + rol × perspectief)

Voorbeeld:
- v1.5: `obligatielening` + `boeken-uitgifte-en-aflossing-obligatielening` + `prorata-intrest-schulden`
- v2.0: één fiche `obligatielening` (kind: instrument); onderdelen "boekingen bij uitgifte" en "prorata" zitten onder Rol > Boekhouder

### Stap D — Nieuwe records die ontbreken

Identificeer **kader-fiches** en **fiscale regelingen** die in 2.0 zouden bestaan maar in v1.5/1.6 ontbreken. Bv. voor PO 1.1:
- `jaarrekeninganalyse` (kader)
- `lange-termijn-financiering` (kader)
- `uitkering-aan-aandeelhouders` (kader)
- Eventuele specifieke regelingen die nog niet bestaan

Per voorstel:
- **Naam + kind**
- **Waarom nodig** (welke v1-records ernaar zouden refereren · welke onderdelen het zou dragen die nu in elke specifieke fiche herhaald worden)

### Stap E — Records die kunnen verdwijnen of mergen

Records die in 2.0 geen eigen bestaansrecht meer hebben:
- Kleine begrip-records die als sub-bouwsteen onder een 2.0-fiche passen
- Sterk gefragmenteerde records die per definitie samen horen
- Records met node_type `competentie` die als rol-cel in 2.0-fiche absorberen (per ADR-025 §competenties-inline)

Per voorgestelde verdwijning:
- **Record-id**
- **Absorptie-doel** (welke 2.0-fiche neemt deze inhoud over)

### Stap F — TDK-dekking-check

Vergelijk de voorgestelde 2.0-fiche-set met de **taken / doelstellingen / kenniselementen** van het PO uit `anchors.json`. Per TDK:

- Welke 2.0-fiche dekt deze?
- Ontbreekt er nog dekking? → voorstel extra fiche

---

## 4. Output-formaat

Markdown-bestand: `data/extractie/<PO>/skeleton-voorstel-<timestamp>.md`

```markdown
# Skeleton-voorstel PO 1.1 → schema 2.0

**Datum**: 2026-05-21
**Aantal v1.x-records geanalyseerd**: 66
**Aantal voorgestelde 2.0-fiches**: 32
**Aantal absorptie-merges**: 18
**Aantal nieuwe kader/regime-voorstellen**: 5

---

## 1. Inventaris v1.x

[Tabel met alle bestaande records + node_type + beschrijving + anchors]

## 2. Voorgestelde 2.0-fiches

### Instrumenten

#### obligatielening (instrument)
**Bevat onderdelen uit**: `obligatielening`, `boeken-uitgifte-en-aflossing-obligatielening`, `prorata-intrest-schulden`
**Rationale**: Eén didactische fiche per instrument. Boekingen onder Rol > Boekhouder; prorata als sub-onderdeel.
**Linked anchors**: 1.1.II.V, 1.1.II.J, 1.4.III.B (cross-PO)

#### inkoop-eigen-aandelen-nv (operatie)
**Bevat onderdelen uit**: `eigen-aandelen`, `inkoop-eigen-aandelen-nv`
...

### Regimes / fiscale regelingen

[...]

### Ratio's

[...]

### Kaders (nieuw)

#### jaarrekeninganalyse (kader)
**Bevat principes voor**: solvabiliteitsratio, current-ratio, ROE, schuldgraad, ...
**Rationale**: Generieke discipline (evolutie, sectornorm, balansdatum-effect, achtergestelde-lening-correctie, samen-lezen) leeft hier; per-ratio-fiche refereert ernaar.

[...]

## 3. Records die verdwijnen / mergen

| v1.x-record | Absorptie-doel | Rationale |
|---|---|---|
| `prorata-intrest-schulden` | onderdeel van `obligatielening` + `banklening` (dupliceren of in kader?) | te klein voor eigen fiche |
| ... | ... | ... |

## 4. TDK-dekking-check

| TDK | Type | Voorgestelde 2.0-fiche(s) |
|---|---|---|
| "boeken van obligatieleningen" | taak | obligatielening |
| "begrip van prorata-intrest" | kenniselement | obligatielening (onderdeel) |
| ... | ... | ... |

**Ontbrekende dekking**: ...

## 5. Open vragen voor menselijke review

- Cluster X: blijft `concept-A` en `concept-B` apart of mergen?
- Kader `lange-termijn-financiering` voorgesteld — wachten op andere PO's of nu maken?
- ...

## 6. Geschatte herextract-omvang

- V1.x-records: 66
- 2.0-fiches voorgesteld: 32 (instrumenten · operaties · regimes · ratios)
- Kader-fiches (nieuw): 3
- Familie-fiches (nieuw): 0
- **Totaal te schrijven**: 35 records
```

---

## 5. Richtlijnen

- **Niet voorbarig zijn**: bij twijfel → "open vraag voor review" i.p.v. zelf knopen doorhakken
- **TDK-dekking is regel**: elke TDK uit `anchors.json` moet uiteindelijk door minstens één 2.0-fiche gedekt worden — anders signaleer als gap
- **Cross-PO awareness**: een record dat in PO 1.1 hoort maar ook in PO 1.4 of 2.x speelt, krijgt anchors uit alle PO's. Vermeld dat expliciet
- **Familie/kader-detectie**: 3+ verwante records → kandidaat voor familie- of kader-fiche
- **Mens-in-de-loop**: dit voorstel wordt door mens gereviewd vóór herextract. Schrijf in een toon die review faciliteert (rationale, open vragen, alternatieven)

---

## 6. Stappen

1. Lees alle v1.x-records voor de PO + anchors + TDK's
2. Bekijk minstens één referentie-mockup per kind
3. Maak inventaris
4. Per record: voorstel kind of mergeable
5. Vorm consolidatie-clusters
6. Identificeer ontbrekende kader/regime-fiches
7. Doe TDK-dekking-check
8. Schrijf rapport in bovenstaand formaat
9. Log "open vragen" prominent voor mens-review

Output: rapport-bestand pad. Geen wijzigingen aan records of RAG.
