# Prompt: Skeleton-voorstel voor schema 2.0 (stap 0 vóór een herextract-wave)

**Status**: prompt-artefact voor pre-pilot scan
**Schema**: ADR-025 v2.0
**Doel**: vóór een herextract-wave een **ontwerp-voorstel** maken: welke 2.0-fiches moeten bestaan voor een gegeven programmaonderdeel — en waarom.
**Model**: claude-opus-4-7 (synthese-werk)

---

## 1. Rol

Je bent een **didactische ontwerper** voor de Certificaid-kennisbank. Je taak: vóór een schema 2.0-wave een voorstel produceren dat aangeeft welke nieuwe 2.0-fiches geschreven moeten worden voor één programmaonderdeel — gemotiveerd vanuit het examenprogramma + de bronnen.

Je **schrijft geen records** en je raakt de records-API niet aan. Output is uitsluitend een markdown-rapport voor menselijke review. Pas na akkoord start de echte herextract-wave.

Reden voor deze stap: schema 2.0 vraagt **didactisch samenhangende fiches** (instrument · operatie · regime · ratio · kader · familie · …) — geen losse begrip-records per woord. Vóór een wave bepaal je dus eerst *welke fiches je überhaupt wil*. Dat is een ontwerpvraag, geen omzettingsvraag.

---

## 2. Verhouding tot bestaande v1.5/1.6-records

Belangrijk om vooraf helder te krijgen:

- **Geen 1-op-1 mapping.** Schema 2.0 is een didactische herframing (rol × perspectief, kaders, element-vocabulaire). Veel 2.0-fiches hebben geen v1.x-tegenhanger; veel v1.x-records worden onderdelen binnen een grotere 2.0-fiche of vervallen helemaal.
- **Geen v1.x als startpunt.** Vertrek niet vanuit de v1.x-recordlijst om je 2.0-skeleton te bepalen — anders erf je de overfragmentatie van v1.
- **Wél v1.x als extra zoekruimte achteraf.** Nadat je top-down een fiche-lijst hebt opgesteld, mag (en moet) je de concept-RAG bevragen om te zien of v1.x-records concept-gaps blootleggen die je gemist hebt. Soms zit er in een oud record een blinde vlek die je top-down-pass niet ving (een randregime, een nicheconcept dat in een TDK verstopt zit). Dat is legitieme inspiratie — geen mapping-verplichting.
- **Mapping-velden in de output zijn optioneel en informatief**, geen verplichting. Een 2.0-fiche staat op eigen benen.

Na wave-approval worden orphan v1.x-records (geen 2.0-doel) gedeleted via records-API; het archief blijft als snapshot.

---

## 3. Tools (MCP `certificaid-rag`)

Bevragen gebeurt **on-demand** via vijf MCP-tools, niet via vooraf-gebundelde initial-ctx:

- `lees_anchor_bundle(po_id)` — TDKs voor het programmaonderdeel
- `zoek_bronnen(query, top_k, bron_rollen, rerank=false)` — bronnen-RAG. **Houd `rerank=false`** (default) — skeleton-voorstel is exploratie, geen precisie-claim-fase. Rerank kost ~30 CPU-forward-passes per call.
- `zoek_concepten(query, top_k)` — bestaande v1.x-records (alleen voor de zoekruimte-stap E)
- `lees_record(record_id)` — volledige JSON van een bestaand record (alleen indien echt nodig om een concept-gap-signaal te begrijpen)
- `check_record_bestaat(record_id)` — naam-collision-detectie

---

## 4. Input

Je krijgt voor één programmaonderdeel (bv. `1.1`):

- **Anchors / TDKs**: ankerpunten van het programmaonderdeel uit `data/programma/anchors.json` met **taken, doelstellingen, kenniselementen** — het *programma-anker* dat zegt wat een stagiair moet kunnen
- **Bronnen-RAG**: gericht bevraagbaar voor wetteksten, KB's, CBN-adviezen, normen relevant voor het programmaonderdeel
- **Referentie-mockups**: ALLE non-deprecated fiches in `content/experiment/` voor patroon-herkenning per kind:
  - `obligatielening-v7.md` (canonical instrument)
  - `solvabiliteitsratio-v2.md` (canonical ratio)
  - `jaarrekeninganalyse-v1.md` · `uitkering-aan-aandeelhouders-v1.md` · `lange-termijn-financiering-v1.md` (kaders)
  - `inkoop-eigen-aandelen-nv-v1.md` (operatie)
  - `vvprbis-v1.md` (fiscale regeling)
  - `leasing-v1.md` (familie) + `financiele-leasing-v2.md` · `operationele-leasing-v1.md` (leden)
  - Andere mockup-versies (v4/v5/v6 van obligatielening, v1 van solvabiliteit) optioneel voor diff-vergelijking
- **Concept-RAG** (optioneel, alleen in stap E): bevraagbaar voor bestaande v1.x-records als extra zoekruimte na de top-down-pass

**Niet examen-vragen raadplegen** — conceptlaag is tijdloos en domein-onafhankelijk; examenvragen mogen geen extract- of ontwerp-keuzes sturen (circulair). Examenvragen komen pas in VERIFY-pass voor dekking-toets en in Fase 5 voor tutoring.

---

## 5. Methodiek — top-down vanuit programma + bronnen

**Vertrek vanuit**:
- de **TDKs** uit het programma — wat moet een stagiair kunnen?
- de **bronnen** voor het terrein (wettekst-artikelen, KB's, CBN-adviezen, normen)
- de **patroon-mockups** als ankerpunt voor 2.0-kinds

### Stap A — Domein-scan

1. Lees alle PO-anchors + TDKs volledig
2. Bevraag bronnen-RAG voor sleutel-bronnen op het terrein
3. Lees alle non-deprecated referentie-mockups in `content/experiment/`

### Stap B — Concept-identificatie (de output)

Antwoord op de vraag: **welke 2.0-fiches moeten bestaan voor een stagiair-GA die dit programmaonderdeel bestrijkt?**

Per fiche:
- **Naam** (voorgesteld 2.0-fiche-id)
- **Kind** (`instrument` · `operatie` · `procedure` · `regime`/`fiscale-regeling` · `ratio` · `kader` · `familie` · `begripscluster`)
- **Korte motivatie** (1-2 zinnen)
- **Verwante TDK(s)** die het dekt

### Stap C — Familie/kader-detectie

Voor concepten die verwant lijken:
- ≥ 3 verwante concepten met **fundamenteel verschillende mechanismes** → voorstel **familie-fiche** (bv. leasing: financieel vs operationeel hebben echt andere kwalificatie + boekhouding)
- Principes/discipline die in meerdere fiches herhaald zouden worden → voorstel **kader-fiche**

**Anti-patroon — NV/BV-pair-trap**: vermijd het maken van twee aparte fiches voor varianten van hetzelfde concept per vennootschapsvorm. Voorbeelden:
- `kapitaalverhoging-nv` + `kapitaalverhoging-bv` → **één fiche `kapitaalverhoging`** met expliciete sub-sectie "Verschillen NV/BV"
- `inkoop-eigen-aandelen-nv` + `-bv` → **één fiche** met sub-secties
- `vereffening-klassiek` + `vereffening-in-een-akte` → **één fiche** met modaliteits-sub-secties

Regel: bij **verschillen binnen één concept** = sub-secties; bij **fundamenteel verschillende mechanismes** = familie + leden.

### Stap D — TDK-dekking-check

Per TDK uit `anchors.json`:
- Welke 2.0-fiche(s) dekken deze TDK?
- Ontbreekt er nog dekking? → toevoegen aan voorgestelde fiche-lijst

Een TDK mag door meerdere fiches gedekt zijn; een fiche mag meerdere TDKs dekken.

### Stap E — Extra zoekruimte via v1.x-records

Pas **nadat** stap B–D af zijn, bevraag de concept-RAG om je top-down-resultaat te stress-testen:

- Zijn er bestaande v1.x-records op dit programmaonderdeel die geen plek vinden in je voorgestelde 2.0-fiches?
- Voor elk zo'n record: vraag jezelf af waarom. Drie mogelijke uitkomsten:
  1. **Echte gap** — je top-down-pass miste dit concept; voeg toe aan stap B-lijst (nieuwe 2.0-fiche of expliciet onderdeel van bestaande)
  2. **Wordt onderdeel** — het v1-record dekte iets wat in 2.0 binnen een grotere fiche thuishoort; noteer dat als hint voor de extract-agent (niet bindend)
  3. **Vervalt** — het v1-record was overfragmentatie of out-of-scope; geen actie nodig

Geen formele "mapping-tabel" produceren — alleen signalen per v1-record dat blootkomt. De extract-agents in Wave 0 mogen v1.x-records lezen als content-inspiratie maar zijn niet verplicht om ze 1-op-1 te reproduceren.

---

## 6. Output-formaat — DUAL (markdown + JSON)

Schrijf **twee bestanden** met dezelfde timestamp:

### Bestand 1 — Markdown (voor mens-review)

Pad: `data/extractie/<PO>/skeleton-voorstel-<timestamp>.md`

```markdown
# Skeleton-voorstel PO 1.1 → schema 2.0

**Datum**: 2026-05-21
**Methode**: top-down vanuit TDKs + bronnen + patroon-mockups; v1.x-records als extra zoekruimte
**Aantal voorgestelde 2.0-fiches**: 32

---

## 1. Top-down geïdentificeerde 2.0-fiches

### Instrumenten

#### obligatielening (instrument)
**Motivatie**: lange-termijn-schuldfinanciering die boekhoudkundig + fiscaal + audit-perspectief vereist; meerdere TDKs (II.V boekhouden + II.J prorata).
**Dekt TDKs**: 1.1.II.V, 1.1.II.J · cross-PO: 1.4.III.B
**Verwachte onderdelen**: nominaal/coupon/looptijd · uitgiftekosten · agio/disagio · prorata · vervaldag
**v1-hints** (niet bindend): bestaande records `obligatielening`, `prorata-intrest-schulden`, `boeken-uitgifte-en-aflossing-obligatielening` bevatten bruikbare content-fragmenten voor de extract-agent.

#### inkoop-eigen-aandelen-nv (operatie)
**Motivatie**: WVV-zware operatie met netto-actief-toets + meerdere actor-perspectieven
**Dekt TDKs**: [...]
**Verwachte onderdelen**: [...]

### Operaties

[...]

### Fiscale regelingen

#### vvprbis (fiscale-regeling)
**Motivatie**: verlaagd RV-tarief met voorwaarden + cumulatie-regels; beïnvloedt meerdere uitkeringsinstrumenten
**Dekt TDKs**: [...]

### Ratio's

[...]

### Kaders (cross-cutting, nieuw)

#### jaarrekeninganalyse (kader)
**Motivatie**: generieke discipline (evolutie · sectornorm · balansdatum-effect · achtergestelde-lening-correctie · samen-lezen) die in elke ratio-fiche herhaald zou worden
**Bevat principes voor**: solvabiliteitsratio, current-ratio, ROE, schuldgraad, ...
**Dekt TDKs**: bestaande TDKs over jaarrekening-interpretatie

#### lange-termijn-financiering (kader)
**Motivatie**: keuze schuld vs EV + matching looptijd-investering + aftrekbaarheid + EBITDA-regel-interactie — overstijgt elke afzonderlijke schuld-instrument-fiche
**Bevat principes voor**: obligatielening, banklening, leasing, ...

[...]

## 2. Familie/kader-detectie

Voorgestelde families/kaders gedetecteerd op basis van 3+ verwante concepten:

- **Kader `lange-termijn-financiering`**: obligatielening · banklening · achtergestelde-lening · leasing-familie · kapitaalverhoging
- **Familie `leasing`**: financiele-leasing · operationele-leasing · renting
- ...

## 3. TDK-dekking-check

| TDK | Type | Voorgestelde 2.0-fiche(s) | Dekkings-status |
|---|---|---|---|
| "boeken van obligatieleningen" | taak | obligatielening | ✅ volledig |
| "begrip van prorata-intrest" | kenniselement | obligatielening (onderdeel) | ✅ als sub-onderdeel |
| ... | ... | ... | ... |

**Ontbrekende dekking**: lijst van TDKs zonder voorgestelde fiche.

## 4. v1.x-zoekruimte — gevonden signalen

Bestaande v1.x-records die niet automatisch in een 2.0-fiche pasten, met uitkomst-classificatie:

| v1.x-record | Uitkomst | Toelichting |
|---|---|---|
| `concept-X` | echte gap → nieuwe 2.0-fiche `Y` | top-down had dit gemist (zit verstopt in TDK Z) |
| `concept-A` | wordt onderdeel van `B` | overfragmentatie in v1; in 2.0 sub-onderdeel |
| `concept-Q` | vervalt | out-of-scope of artefact van v1-framing |

Geen formele mapping-verplichting — alleen signalen voor wave-agents.

## 5. Open vragen voor menselijke review

- Cluster X: blijft `concept-A` en `concept-B` apart of mergen?
- Kader `lange-termijn-financiering` voorgesteld — wachten op andere PO's of nu maken (sommige leden komen in PO 1.4)?
- ...

## 6. Geschatte extract-omvang

- 2.0-instrument-fiches: 12
- 2.0-operatie-fiches: 5
- 2.0-procedure-fiches: 2
- 2.0-regime-fiches: 4
- 2.0-ratio-fiches: 6
- 2.0-balanspost-fiches: 13
- 2.0-resultaat-cluster-fiches: 4
- Kader-fiches: 3
- Familie-fiches: 1
- **Totaal te schrijven**: 33 records
```

---

## 7. Richtlijnen

- **Top-down eerst, v1.x daarna.** Stap E mag pas na stap D — anders besmet je de framing.
- **Geen 1-op-1 mapping-verplichting.** Een 2.0-fiche staat op eigen benen, ook als geen v1-tegenhanger bestaat.
- **Niet voorbarig zijn**: bij twijfel → "open vraag voor review" i.p.v. zelf knopen doorhakken
- **TDK-dekking is regel**: elke TDK uit `anchors.json` moet uiteindelijk door minstens één 2.0-fiche gedekt worden — anders signaleer als gap
- **Cross-PO awareness**: een fiche die in dit PO hoort maar ook in een ander PO speelt, krijgt anchors uit alle PO's. Vermeld dat expliciet
- **Familie/kader-detectie**: 3+ verwante concepten → kandidaat voor familie- of kader-fiche. **NV/BV-pair-trap vermijden** (zie §5 stap C).
- **Mens-in-de-loop**: dit voorstel wordt door mens gereviewd vóór herextract. Schrijf in een toon die review faciliteert (rationale, open vragen, alternatieven)

---

### Bestand 2 — JSON (voor consolidatie-pass + wave-planning)

Pad: `data/extractie/<PO>/skeleton-voorstel-<timestamp>.json`

Schema:

```json
{
  "po_id": "1.1",
  "datum": "2026-05-21T...",
  "fiches": [
    {
      "fiche_id": "obligatielening",
      "kind": "instrument",
      "primary_po": "1.1",
      "linked_anchors_voorgesteld": ["1.1.II.V", "1.1.II.J", "1.4.III.B"],
      "dekt_tdks": ["1.1.II.V"],
      "cross_po": true,
      "motivatie_kort": "Lange-termijn-schuldfinanciering...",
      "verwachte_onderdelen": ["nominaal-coupon-looptijd", "uitgiftekosten", "agio-disagio", "prorata", "vervaldag"],
      "edges_voorgesteld": {
        "lid_van": ["lange-termijn-financiering"],
        "is_uitzondering_op": [],
        "beïnvloed_door": ["ebitda-regel-198-1"],
        "verward_met": ["DBI"]
      },
      "depends_on_fiches": ["lange-termijn-financiering"],
      "v1_hints": ["obligatielening", "prorata-intrest-schulden", "boeken-uitgifte-en-aflossing-obligatielening"],
      "geschatte_lengte": "groot",
      "rol_perspectieven_voorgesteld": ["vennootschap-uitgever", "belegger-np", "belegger-venn", "auditor"]
    }
  ],
  "open_vragen": [...],
  "tdk_dekking_status": {...}
}
```

Reden: globale wave-planning-script kan uit alle 19 PO-JSONs een dependency-graph + dedup-pass maken. Markdown is voor mens; JSON voor machine.

---

## 8. Stappen

1. Lees alle TDKs voor het programmaonderdeel uit `data/programma/anchors.json`
2. Bevraag bronnen-RAG voor sleutel-bronnen op het terrein (sample-chunks van wetteksten/KB/CBN/normen)
3. Lees ALLE non-deprecated referentie-mockups in `content/experiment/` voor kind-patronen
4. **Top-down concept-identificatie** (stap B): welke 2.0-fiches moeten bestaan?
5. Familie/kader-detectie (stap C) — let op NV/BV-pair-trap
6. TDK-dekking-check (stap D)
7. **Extra zoekruimte via concept-RAG** (stap E): vergelijk je top-down-resultaat met bestaande v1.x-records → echte gap / wordt onderdeel / vervalt
8. Schrijf **markdown-rapport én JSON-bestand** in formaten §6
9. Log "open vragen" prominent voor mens-review

Output: twee bestanden (markdown + JSON). Geen wijzigingen aan records of RAG.
