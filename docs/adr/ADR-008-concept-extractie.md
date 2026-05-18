# ADR-008: Concept-extractie via bron-first matching

**Status**: Accepted
**Datum**: 2026-05-09 (laatst bijgewerkt 2026-05-18)
**Empirisch onderbouwd op**: PO 4.0 Deontologie, PO 1.1 Algemene boekhouding, PO 1.4 Geconsolideerde jaarrekening (enrichment-loop + schema 1.4-rewrite)

## Changelog

- **2026-05-18** — §18-uitvoering: ENRICH-stack en AUTO-MERGE verwijderd. `tools/extractie/enrich_records.py`, `tools/extractie/run_enrichment_cycle.py`, `tools/extractie/auto_merge.py` en `prompts/concept-enrich-v1.md` weg (vervangen door EXTRACT v4 + records-API direct-write). Anchor-bundles niet meer als JSON-snapshots in `data/extractie/<po>/bundles/` maar on-demand uit sqlite+ChromaDB via `tools/extractie/export_bundle.py` (stdout-only). Single source of truth: `matches.sqlite3` (membership) + ChromaDB (tekst). §13 blijft als historische context, §13.7 tooling-lijst gemarkeerd als vervangen.
- **2026-05-17** — §18 toegevoegd: EXTRACT v4 als research-and-draft-agent met event-driven scope. ENRICH wordt herzien als EXTRACT met gap-event (zelfde agent, andere initial-ctx). VERIFY-feedback splitst in tactisch (per-record gap-event) en strategisch (prompt-/cast-evolutie). Records hitten concept-RAG meteen via records-API (ADR-019). v1.0-mindset: geen draft-status. Coordinator-pattern uitgesteld tot post-pilot.
- **2026-05-18** — `prompts/concept-extractie-v4.md` herschreven als zelfdragend permanent artefact (v4, niet delta-op-v3). ADR-007 schema 1.5 geïntegreerd: 6 node-types (`begrip` · `regel` · `cluster` · `synthese` · `autoriteit` · `competentie`), 7 canonieke edge-types, drie concretiserings-soorten (`in_praktijk`, `voorbeelden`, `illustraties`). Migratie-mapping voor verouderde types. Gap-mining-patterns 1-5 omgezet in concrete regels: slug-resolver (§9), minimum-rijkheid-tabel (§10), near-duplicate-check (§11), corpus-blindheid-mitigatie (§12). `voorbeeld_inline` → `voorbeelden[]` migratie geïnstrueerd.
- **2026-05-16** — §17 toegevoegd: schema 1.4-implicaties voor extractie-prompts. Concept-extractie-v4 gebruikt stap-blok + bouwsteen-blok + formule-blok + cast-conventie (zie ADR-007 schema 1.4). VERIFY krijgt drie nieuwe aspect-types (`voorbeeld.ontbreekt`, `stap.skeleton`, `bouwsteen.geen-waarom`). ENRICH-prompt v1 dekt deze. Empirisch gevalideerd via twee deep-rewrite-batches op PO 1.4 (29/31 records → schema 1.4 op 2026-05-16).
- **2026-05-15** — §14 (Fase D: Competentie-destillatie), §15 (Fase E: Leerpad-opstelling), §16 (gaps.json type-discriminator) toegevoegd. Drie-lagen leermateriaal-uitbreiding (BRON → CONCEPT → COMPETENTIE → minicursus) gegrond in pedagogische output-vraag. Examenvragen blijven uitgesloten als input (anti-circulariteit); exam_patterns is wel toegestaan.
- **2026-05-15** — §13 toegevoegd: monotone enrichment-loop (4-bloks-flow EXTRACT → VERIFY → ENRICH → AUTO-MERGE+LOG). Records worden PO-overschrijdend flat in `data/concepten/records/<id>.json` opgeslagen; PO-linkage via `linked_anchors[]` per record. Gaps en enrich-warnings globaal in `data/extractie/`.
- **2026-05-15** — §4 bundling-strategie herzien naar knee-detectie (97.2% recall op gold-set).
- **2026-05-15** — §5.1 must-have-detectie via drie emergente mechanismen (geen pre-curated checklist).
- **2026-05-15** — §5.2 bron-aanbevelings-feedback-loop voor corpus-uitbreiding.

## Context

Concepten ontstaan niet vanzelf. Drie ingangen leveren materiaal:

- **Het examenprogramma** zegt *welke* concepten nodig zijn (scope) via taken, doelstellingen en kenniselementen — niet *wat* ze inhouden.
- **Bronnen** (wetteksten, ITAA-normen, CBN-adviezen) leveren juridische inhoud.
- **Voorbeeldexamens** tonen de toetsings-realiteit, maar zijn pas in Fase 5 als validatie-instrument inzetbaar (anti-oogkleppen-regel: extractie alleen op examens biedt circulaire bias).

De vraag is hoe je deze drie ingangen koppelt. Twee aanpakken zijn overwogen.

### Overwogen alternatief: vermoedensruimte (verworpen)

De aanvankelijke aanpak was *"LLM raadt eerst, dan zoeken we"*:

1. LLM genereert 50–150 vermoedens per programmaonderdeel op basis van taken/doelstellingen/kenniselementen
2. Per vermoeden multi-level retrieval over de bronnen-collection
3. Per vermoeden seed-record-extractie door LLM
4. Verdieping per concept iteratief

**Waarom verworpen**:
- **Drie zwakke schakels op een rij**: LLM kan vermoedens missen of er bedenken die niet in bronnen staan; retrieval kan slechte chunks ophalen; concept-bouw is afhankelijk van wat in stap 2 toevallig opdook.
- **Niet reproduceerbaar**: vermoedensruimte verschilt per LLM-run, fundamentele determinisme-tekort.
- **Geen dekking-garantie**: bronmateriaal dat geen vermoeden raakt valt door de mazen.
- **Niet compositioneel bij bron-update**: een nieuwe bron forceert hervraging van alle vermoedens of accepteert staleness.
- **LLM-creativiteit op de verkeerde plek**: de LLM moet vragen *"wat zou er kunnen bestaan?"* in plaats van *"wat staat hier?"*. Eerste vraag nodigt hallucinatie uit.
- **Twee dure LLM-passes** (vermoedensruimte + seed) waar één had volstaan.

### Aanvaarde aanpak: bron-first matching

Het experiment in mei 2026 (zie git-history van branch `experiment-bron-first-extractie`, samengevat in deze ADR) toont dat de vermoedensruimte-fase volledig vervangbaar is door **deterministische similarity-matching** tussen bron-chunks en TDK-anchors (taken/doelstellingen/kenniselementen). Dat verschuift de pipeline van *"LLM raadt eerst"* naar *"we zoeken eerst, LLM extraheert gegrond"*.

## Beslissing

### 1. Pipeline

```
A. Anchor-verrijking (LLM, eenmalig per PO, gegit)
   ↓
B. Bron-first matching (deterministisch)
   ↓
C. Per-anchor concept-extractie (LLM, één Opus-sessie per PO)
   ↓
D. Verdieping per concept (iteratief)
```

### 2. Geen externe LLM-API tijdens build-pipeline

Alle LLM-werk in de extractie-pipeline gebeurt **lokaal via een Claude Code subagent** in dev-omgeving. Geen `anthropic.Anthropic()`-calls vanuit build-tooling.

Helper-scripts in `tools/extractie/` doen alleen deterministisch werk (bron-first matching, bundle-export, JSON-IO, ChromaDB-updates). LLM-synthese gebeurt door subagents die deze helpers via Bash-tool aanroepen.

Alleen de **gedeployde tutor** mag op runtime de Anthropic API aanroepen — productie-eindpunt, geen build-stap.

#### Modelkeuze: Opus

De extractie-subagent draait op **Claude Opus**. Argumenten:

- Hoge leverage: één goed concept-record bespaart 10× zoveel mens-curatie.
- Multi-criteria reasoning: per anchor-bundel moet de agent simultaan beslissen over relevantie, granulariteit, node-type-keuze, kenniselement-koppeling, en eventueel split/merge.
- Synthese-kwaliteit: hoofdtekst-velden worden in simpele Nederlandse taal herschreven uit juridische brontekst, met behoud van precisie + confidence-labels + bronverwijzingen.

Sonnet/Haiku ongeschikt voor extractie, wel voor helper-script implementatie.

Provenance-veld: `tooling.model = "claude-opus-4-7"` op elk concept-record.

### 3. Anchor-verrijking — fase A

**Wat**: voor elk taakblok-element (taken, doelstellingen, kenniselementen + subitems) een verboser-versie + 3-5 synoniemen genereren via subagent.

**Output**: `data/extractie/<po>/anchors/<po>-anchors.json` (gegit).

**Schema per anchor**:
```json
{
  "anchor_id": "<po>.D1.1.taak.1 | <po>.I.D.7 | etc",
  "anchor_type": "taak | doelstelling | kenniselement",
  "tekst": "<originele tekst uit programmaonderdeel-JSON>",
  "verbose": "<2-3 zinnen vakjargon>",
  "synoniemen": ["...", "..."]
}
```

**Strikte instructie aan subagent**:
- Verbose-tekst dicht de imperatief-descriptief kloof (taken zijn imperatieven, bronnen zijn descriptief). 2-3 zinnen vakjargon.
- **Geen wetsartikelnummers**, **geen specifieke wetsnamen** in verbose of synoniemen — vermijdt self-fulfilling matching. Empirisch: 90-99% van score-winst is vocabulair, slechts 1-3% komt uit wetsverwijzingen.

**Mens reviewt anchors per PO** voor productie. Lage kost (eenmalig, 36-74 anchors per PO).

### 4. Bron-first matching — fase B

**Input**: enriched anchors + indexed bron-chunks (ADR-006 ChromaDB `bronnen`-collection).

**Werkwijze** (`tools/extractie/match_bronnen.py`):

1. Embed alle anchor verbose-teksten (+ synoniemen als concat) met bge-m3
2. Voor elk anchor: cosine-similarity tegen alle in-scope chunks
3. Per anchor: bundle = adaptive knee-detectie (zie strategie hieronder)
4. Per chunk: log welke anchors hem als top-K matchen (cross-anchor info)

**Bundling-strategie** (gewijzigd 2026-05-15 na empirische evaluatie op gold-set):

Twee strategieën beschikbaar via `--strategy`:

- **`margin`** (legacy): `score >= max(floor, top1 - margin)`. Vast verschil tot top-1, vast bottom-floor. Voordeel: simpel. Nadeel: bundles kunnen mega-groot worden voor anchors met flat distribution (max 1775 in onze corpus).

- **`knee`** (default vanaf 2026-05-15): `score >= max(floor, top1 × proportional_drop)`, geclipped naar `[min_bundle, max_bundle]`. Voordeel: adaptive — anchors met scherpe top krijgen kleine bundles (≈top-50), anchors met flat distribution krijgen grote bundles maar gecapped. Defaults: `floor=0.40`, `proportional_drop=0.75`, `min_bundle=20`, `max_bundle=300`.

**Empirische evaluatie** (`tools/extractie/match_experiment.py` op `tools/extractie/gold/matching-gold-set.json` — 12 manueel gecureerde anchor→bron-stem-paren):

| Strategie | mean recall | median bundle | max bundle | uncovered |
|---|---:|---:|---:|---:|
| `margin-0.55-0.15` (oud) | 95.6% | 185 | 1775 | 1 |
| `knee-0.40-0.75-min20-max300` | **97.2%** | **102** | **300** | **0** |

Knee-strategie geeft betere recall **én** kleinere bundles **én** dekt alle anchors (0 uncovered). De ene resterende gold-miss (anchor 2.3.I "Elementen van boekhouding" mist WVV) is borderline — anchor handelt over boekhouding-voor-vennootschapsbelasting, WVV is vennootschapsrecht.

**Output**: `data/extractie/matches/<run_id>.json` + `latest.json` symlink (gitignored, reproduceerbaar uit anchors + index).

### 5. Per-anchor concept-extractie — fase C

Subagent (Opus, één per PO) verwerkt anchors sequentieel.

**Input per anchor**: anchor + bundle (chunks met volledige tekst, gesorteerd op score).

**Vraag aan subagent**: *"Welke concepten worden in deze chunks behandeld?"* (meervoud expliciet — een bundle bevat doorgaans 5-18 fenomenen).

**Output per concept**:
- `naam`, `node_type` (uit ADR-007), `rationale` (1 zin)
- `supporting_chunks[]`: chunk-IDs uit de bundle die het concept onderbouwen
- `confidence`: `grounded` (verbatim/paraphrase) of `inferred` (redenering)
- `granulariteit`: signaal `klein|middel|groot`

**Strikte regels** (anti-hallucinatie):
- Geen concepten zonder `supporting_chunks` (anti-hallucinatie)
- Geen wetsartikelnummers verzinnen — alleen wat letterlijk in chunks staat
- `confidence` eerlijk: `grounded` alleen als chunk-tekst het concept bevat

**Cross-anchor context-accumulatie**: door anchors sequentieel binnen één Opus-sessie te verwerken, ziet de subagent eerder geschreven concepten en kan vakoverschrijdende fenomenen herkennen ("dit chunk hoort ook bij anchor X dat ik eerder behandelde → al-bestaand concept Y").

### 5.1 Must-have-detectie — emergent, niet pre-curated (2026-05-15)

**Probleem**: examenvragen toetsen begrippen die soms wel in de bronnen zitten (KB WVV art. 1:14, CBN-adviezen) maar niet als losse anker zijn benoemd ("controlepercentage", "invloed van betekenis", "geassocieerde onderneming"). Een gap-detectie is nodig.

**Anti-pattern**: pre-curated must-have-checklist door mens per PO. Niet schaalbaar, chicken-and-egg (je moet de inhoud kennen om te kiezen wat must-have is). **Niet doen.**

**Drie emergente mechanismen** (zonder mens-pre-werk):

1. **Cross-referentie-detectie tijdens extractie** — wanneer een record verwijst naar een term ("...uitgaande van het belangenpercentage...", "...wanneer invloed van betekenis bestaat...") en die term geen eigen record heeft, log de term als gap-entry in `data/extractie/gaps.json` met `aspect: dangling-reference` (zie `prompts/concept-extractie-v4.md` §Gaps.json voor schema). Termen die >3× over chunks van >2 bronnen verwezen worden = sterke kandidaat voor eigen record (mens-cureert).

2. **Recursive deepening tijdens extractie** — voor elk hoofd-concept, identificeer ingebakken begrippen in `definitie.text` of `main_rule.text`. Als ze in 2+ chunks van 2+ bronnen voorkomen: **direct als eigen record aanmaken** (extractor heeft toestemming, geen wacht-en-vraag). Liberale aanpak — anti-twijfel-regel: bij twijfel "is dit een eigen record?" kies "ja".

3. **Agent-judgment in VERIFY Check A** — een tweede agent (Opus, via `concept-verify-v1`) probeert examenvragen met enkel concept-records op te lossen en flagt expliciet ontbrekende begrippen of niet-beantwoordbare vragen. Output gaat naar dezelfde `data/extractie/gaps.json` met aspecten als `records.ontbreekt`, `definitie.onvolledig`, `valkuilen.ontbreekt`, etc. (Voorheen schreef een legacy `quality-check-v1`-agent een apart `examen-eval-*.json`-bestand naar `data/concepten/quality_checks/<po>/`; die route is opgeheven 2026-05-18 ten gunste van unified gaps-stroom.)

Outputs van de drie mechanismen zijn input voor **prompt v4 hercirculatie**: de volgende extractie-pass krijgt de dangling/missing-list als "expand-here"-instructie (feedback-set event — zie §18.2).

**Mens-rol**: cureren van de gerapporteerde kandidaten (accept/reject), geen pre-werk. Zelfde dynamiek als de caveat-policy (ADR-005 §5): agent stelt voor, mens beslist.

### 5.2 Bron-aanbevelingen — feedback-loop voor corpus-uitbreiding (2026-05-15)

Wanneer een extractor structureel tekortschiet door **kennis die niet in de huidige corpus zit** (bv. COSO-framework principes, IFRS-detailteksten, accountancy-handboek-niveau enumeraties), schrijft hij een entry naar `data/extractie/_bron_voorstellen.json` (append-only).

Schema per voorstel:
- `po`, `anchor_id`, `ontbrekende_kennis` (vrije tekst)
- `voorgestelde_bronnen[]` met `naam`, `url`, `publiek`, `license`, `redenering`
- `geconstateerd_door` (run_id), `geconstateerd_op`, `human_decision` (default `null`)

Mens-rol: per voorstel beslissen of de bron wordt toegevoegd aan het corpus, ergens anders staat, of dat de extractie het zonder moet doen. Voorstellen blijven in het bestand als geschiedenis.

### 6. Verdieping per concept — fase D

Voor elke seed → status `partieel` → eventueel `gevuld`:
- Verdiepende retrieval-queries met cumulatieve concept-state als input
- LLM vult `exceptions`, `scope`, edge-targets verder in
- Status `gevuld` (later, eventueel handmatig of via tweede LLM-pass): `valkuilen[]`, `voorbeelden[]`

### 7. Bestaande concepten als anchor

Vanaf de tweede iteratie: bestaande concepten doen mee als anchors in fase B. Effecten:
- Nieuwe chunk met bestaand concept als top-hit → geen nieuw concept, alleen verrijking
- Cross-PO duplicate-detectie inherent
- Anchor-set groeit incrementeel met de kennisbank

### 8. Bron-update workflow (compositioneel)

Een nieuwe bron toegevoegd aan de index → **bron-first matching opnieuw draaien** voor alle anchors (cheap: bi-encoder cosine, geen LLM). Output:
- Welke anchors hebben nu een sterkere match dan voorheen → concepten heroverwegen
- Welke chunks van de nieuwe bron raken geen anchor → mogelijk buiten-scope of aanduiding van een nieuw kenniselement-gat

Dit vervangt de niet-compositionele aanpak waar een bronwijziging alle vermoedens in twijfel trekt.

### 9. Confidence-labeling per veld

Elk veld erft een `confidence` string-tag (zie ADR-007 voor waarden — `"grounded"` / `"inferred"`):
- `bron_rol` van de chunks waaruit het is afgeleid (`itaa-lex`, `wettekst`, `norm` → `grounded`)
- Type extractie-stap (verbatim/paraphrase → `grounded`; geconstrueerde redenering → `inferred`)

Een veld zonder bronverwijzing krijgt nooit stilzwijgend `grounded`.

### 10. Per-veld provenance — inline (schema 1.1)

`_provenance` leeft **inline per veld** (zie ADR-007 §"Provenance — inline per veld" voor volledige spec).

```json
{
  "main_rule": {
    "text": "...",
    "confidence": "grounded",
    "source": { ... },
    "_provenance": {
      "inputs": [{"id": "Antiwitwaswet-2017__art_5", "sha256": "<chunk_sha>", "version": "rag-v1"}],
      "extracted_at": "2026-05-09T12:00:00Z",
      "extractor": "bron-first-v1"
    }
  }
}
```

Bij **bron-update** (chunk-content-hash verandert) → `mark_stale.py` walkt block-level: welke velden in welke concept-records hebben deze chunk-id? → die velden worden `stale: true`.

### 11. Permanent vs ephemeral provenance-artefacten

| Artefact | Locatie | Levensduur | Status |
|---|---|---|---|
| **Anchors** | `data/extractie/<po>/anchors/<po>-anchors.json` | Permanent — gegit | curatie-artefact |
| **Matches** | `data/extractie/matches.sqlite3` | Permanent — gegit; single source voor anchor-bundle-membership (ADR-005 §9.1) | authoritative |
| **VERIFY-run payloads** | `data/extractie/<po>/verify-runs/{records,anchors,examen_vragen}-*.json` | Ephemeral — gitignored, reproduceerbaar | wegwerpbaar |
| **VERIFY-rapporten** | `data/extractie/<po>/verify-runs/{instructies,rapport}-*.md` | Permanent — gegit voor traceability | curatie-artefact |
| **Concept-records** | `data/concepten/records/<id>.json` | Permanent — duurzame kennislaag, **gegit** (sinds 2026-05-15) | authoritative |
| **Concept-records archief** | `data/concepten/_archive/<po-versie>/` | Permanent lokaal, **gitignored** (alleen voor lokale traceability bij grote schema-overgangen) | historisch |

De permanente provenance leeft uitsluitend in concept-record `_provenance`-velden. Andere artefacten zijn een tussenstadium.

### 12. Schema-evolutie tijdens extractie

Wanneer een concept niet past in het huidige conceptmodel:
- Subagent genereert expliciet schema-uitbreidingsvoorstel (nieuw veld, nieuw node-type, nieuw edge-type)
- Voorstel landt in `data/concepten/records/_voorgestelde_types.yaml` (zie ADR-007)
- Pas na menselijke bevestiging wordt het schema bijgewerkt

### 13. Monotone enrichment-loop (2026-05-15) — **VERVANGEN door §18 (2026-05-17)**

> **Historische sectie.** EXTRACT v4 (§18) verving deze 4-bloks-flow door één agent met event-driven scope + records-API direct-write. ENRICH en AUTO-MERGE zijn niet meer als aparte stappen aanwezig. De principes uit §13.1 (vijf prompt-principes) zijn opgenomen in `prompts/concept-extractie-v4.md`; de monotoniteit van §13.3 leeft als prompt-regel in v4, niet meer als script-garantie.

Na empirische validatie op PO 1.4 (zie `data/extractie/1.4/v1-vs-v2-vergelijking.md` + `stress-test-reflectie.md`) bleek dat een tweede extractie-pass op dezelfde anchors structureel content van de eerste pass verliest, omdat de LLM telkens van scratch herkiest. Drie regressies werden geconstateerd in v2 t.o.v. v1 (bodemwaarde bij vermogensmutatie, stichting-voorbeeld bij consortium, maatschap-uitzondering bij vrijstelling-subconsolidatie) zonder dat de LLM motiveerde waarom.

De pipeline krijgt daarom een 4-bloks-flow per programmaonderdeel, waarbij blok 2 en 3 strikt gescheiden hoedjes hebben (judge ≠ writer = geen self-grading) en blok 4 mechanisch monotonie afdwingt.

```
1. EXTRACT  (de-novo, anchor-gestuurd, prompt v4)
       ↓
2. VERIFY   (read-only judge-agent → globale gaps.json)
       ↓
3. ENRICH   (write-agent, append-only contract, input = records + gaps)
       ↓
4. AUTO-MERGE + LOG  (mechanisch script; toplevel-loss reverten, item-loss loggen)
```

**Locatie van records**: concepten zijn **PO-overschrijdend**, één file per concept in flat `data/concepten/records/<id>.json`. Geen PO-subdirs, geen versie-suffixen (`-v2`, `-enriched`). Versionering = git. Migratie van huidige `data/concepten/records/1.4/` en `1.4-v2/` naar flat structure is onderdeel van de eerste enrichment-cyclus.

**Linkage records ↔ programmaonderdelen** via veld `linked_anchors[]` op elk record (lijst van anchor-id's uit eender welk PO). Bij PO-scoped operaties (minicursus-bouw, stress-test, examenmatching) wordt via dit veld + de concepten-collection in ChromaDB gescoped — geen file-tree-discriminatie.

#### 13.1 EXTRACT — vijf algemene principes voor prompt v4

Gedistilleerd uit v2-bevindingen op PO 1.4, maar generiek geformuleerd:

1. **Centraliteit → volledigheid**. Hoe vaker een concept door andere records wordt aangeroepen (vergelijkingsparen, vrije tekst, edges), hoe completer zijn eigen record moet zijn. Basis-begrippen krijgen méér aandacht, niet minder.
2. **Berekenbaar concept → numeriek voorbeeld verplicht**. Elke `berekeningsmethode[]` krijgt minstens één `concreet_voorbeeld`. Geen "rekenuitwerking elders".
3. **Eén fenomeen = één record**. Geen overlappende records voor twee zijden van dezelfde munt — meerdere aspecten passen binnen één record als afzonderlijke velden of als items in een lijst.
4. **Relaties expliciet, niet enkel narratief**. Als de tekst van record A naar concept B verwijst, ook in `vergelijkingsparen[]` of `edges[]` opnemen. Vrije-tekst-only verwijzingen zijn dood gewicht — niet bruikbaar voor graph-walk of cross-record retrieval.
5. **Uniforme rijkheid binnen type**. Records van hetzelfde node-type krijgen vergelijkbare veldenrijkheid. Geen "deze had ik haast, deze heb ik diep". Concrete minimum-rijkheid wordt per node-type in de prompt vastgepind.

#### 13.2 VERIFY — read-only judge-agent

Eén **Sonnet**-subagent met enkel een oordeels-hoedje (judge-werk vereist geen Opus-synthese). Voert drie checks uit zonder records aan te raken:

1. **Examenvraag-simulatie**: kan de agent de top-examenvragen voor de gescopete anchors *mentaal* oplossen uit de records (geen tekst produceren)? Strandt-punten worden gelogd.
2. **Minicursus-haalbaarheid**: kan de agent *mentaal* een minicursus voor de gescopete anchors uitstippelen? Ontbrekende of te dunne records worden gelogd.
3. **Semantische coherentie**:
   - `vergelijkingsparen[].vergelijking_met` wijst naar bestaande record_id? (mechanisch deel)
   - `edges[].target` bestaat? (mechanisch deel)
   - Vrije-tekst-verwijzingen (`"zie X"`, `"vergelijk met Y"`) gespiegeld in vergelijkingsparen/edges? (LLM-deel)
   - Twee records die hetzelfde fenomeen behandelen? (LLM-deel)

**Output**: globale append-only `data/extractie/gaps.json`. Géén writes naar records.

**Open ontwerp-vraag**: de huidige mechanische coherentie-checks zijn schema-veld-gebonden (`berekeningsmethode[]` mist `concreet_voorbeeld`). Dit faalt zodra hetzelfde inhoudelijk via een ander veld wordt geleverd (bv. `stappen[]` met rekenwerk). Volgende iteratie: content-pattern-based checks die over alle velden scannen op eigenschappen (heeft-rekenwerk, heeft-procedure, heeft-vergelijking) in plaats van veld-existence. Schema-onafhankelijk, robuust bij schema-evolutie. Niet in scope van huidige bouw — vastgelegd als open punt.

Schema per gap-entry:
```json
{
  "record_id": "integrale-consolidatie",
  "aspect": "berekeningsmethode.concreet_voorbeeld",
  "reden": "Centrale methode zonder numeriek voorbeeld; strandt op examen-simulatie 2014-1-vr8",
  "prio": "hoog",
  "geconstateerd_door": "verify-run-<id>",
  "geconstateerd_op": "<iso>",
  "status": "open"
}
```

#### 13.3 ENRICH — write-only agent met monotoon contract

Eén Opus-subagent met enkel een schrijfhoedje. Input: bestaande records + `gaps.json` + bron-bundles (uit Fase B). Output: aangepaste records op dezelfde plek (`data/concepten/records/<id>.json`).

**Monotoon contract** in de prompt:
- *Behoud alles* wat in het bestaande record staat tenzij je expliciet corrigeert of verbetert.
- *Herformuleren en corrigeren mag* — maar verplicht met `corrected_from` (de oude waarde) + `correction_reason` (1 zin waarom de nieuwe versie beter is) + bron.
- *Verwijderen zonder motivering verboden.* Bij twijfel: behoud + voeg toe.
- *Niet-gevraagde velden toevoegen verboden.* Werk binnen wat in `gaps.json` voor dit record staat. Bestaande gouden velden blijven; nieuwe velden alleen als gap dat vraagt.

Verbetering is welkom, regressie niet. `auto_merge.py` garandeert dat geen toplevel-veld weg kan zonder `corrected_from`-marker.

#### 13.4 AUTO-MERGE + LOG — mechanisch script

Géén LLM, géén mens-blockade. Twee niveaus:

- **Hard (auto-merge)**: een toplevel-veld is verdwenen vergeleken met `git HEAD` en heeft geen `corrected_from`-marker → script zet het veld terug. Mechanisch eenvoudig (set-diff op JSON-keys). Geen conflict mogelijk omdat het veld weg is.
- **Soft (log)**: array-items binnen een behouden veld zijn verdwenen → script logt naar globale `data/extractie/enrich-warnings.json` (append-only) met de verloren content en de record-id. Geen automatische actie; latere pass (verify of mens) kan terugkijken.

`enrich-warnings.json` schema:
```json
{
  "record_id": "vermogensmutatiemethode",
  "veld_pad": "bouwstenen",
  "verloren_item": { ... },
  "verloren_in_run": "enrich-run-<id>",
  "verloren_op": "<iso>",
  "status": "unreviewed"
}
```

#### 13.5 Globale artefacten

| Artefact | Locatie | Levensduur |
|---|---|---|
| Gaps-backlog (unified) | `data/extractie/gaps.json` | Permanent, append-only — bevat dangling-references, ontbrekende records, examen-evaluatie-bevindingen, bron-gaps en granulariteits-twijfels (zowel EXTRACT- als VERIFY-output) |
| Enrich-warnings | `data/extractie/enrich-warnings.json` | Permanent, append-only |
| Bron-voorstellen | `data/extractie/_bron_voorstellen.json` | Permanent (zie §5.2) |
| Extraction-rapport | `data/extractie/<po>/v4-extraction-rapport.md` | Per-run snapshot (narratieve patronen, niet-record-specifieke observaties) |

#### 13.6 Loop-volgorde, niet altijd alle blokken

- **Eerste pas per PO**: blok 1 (EXTRACT) + blok 2 (VERIFY). Als gaps leeg → klaar.
- **Bij gaps**: blok 3 (ENRICH) + blok 4 (AUTO-MERGE). Daarna opnieuw blok 2 (VERIFY) — maar in regel hooguit één enrich-cyclus, geen eindeloze loop. Zie `run_enrichment_cycle.py` voor geautomatiseerde orchestratie.
- **Discovery-signal**: ENRICH mag nieuwe gaps toevoegen met `status: "discovered-during-enrich"`. Deze worden in de volgende VERIFY-ronde van dezelfde cyclus als open gaps behandeld.
- **Bij bron-update** (nieuwe wettekst, gewijzigde norm): blok 2 (VERIFY) op alle records die de gewijzigde chunk-id gebruikten + blok 3 indien gaps.

Geen vijf aspect-passes, geen aparte minicursus-stress-test als tooling-stap. De minicursus is een *eind-deliverable* (na alle blokken), niet een test-tool.

#### 13.7 Tooling — **bijgewerkt na §18 (2026-05-18)**

Actief:
- `tools/extractie/verify_records.py` — subagent-runner voor VERIFY (model: `VERIFY_MODEL = "claude-sonnet-4-6"`)
- `tools/extractie/export_bundle.py` — print anker-bundle naar stdout (sqlite-membership + ChromaDB-tekst)
- `tools/examen/classify_vragen_naar_programmaonderdelen.py` — one-off classificatie van examenvragen naar programmaonderdelen via Sonnet-subagent
- `prompts/concept-extractie-v4.md` — zelfdragende EXTRACT-prompt (schema 1.5, research-and-draft-agent, event-driven scope)
- `prompts/concept-verify-v1.md` — VERIFY-prompt (model: Sonnet)

Verwijderd (vervangen door §18):
- `tools/extractie/enrich_records.py` → ENRICH is EXTRACT met gap-event
- `tools/extractie/auto_merge.py` → records-API schrijft direct, geen merge-stap
- `tools/extractie/run_enrichment_cycle.py` → loop-orchestratie vervalt; max-iter + stall-review zit in §18.4
- `prompts/concept-enrich-v1.md` → vervangen door `concept-extractie-v4.md` met feedback-event-ctx

### 14. Fase D — Competentie-destillatie (schema 1.3, 2026-05-15)

Voorafgaande fasen (A → C, plus monotone enrichment-loop) produceren concept-records met grounded inhoud. Voor leermateriaal-generatie (ADR-010) is een tussenlaag nodig die **"hoe doe je X"** beantwoordt — pedagogische competenties die het examenprogramma toetst maar die versplinterd zit over meerdere concept-records.

**Input** (strikt — anti-circulariteit):
- `data/programma/programma.json` (taken + kenniselementen per PO)
- `data/programma/anchors.json` (verbose + synoniemen)
- `data/concepten/records/*.json` (gefilterd op `linked_anchors` van de doelPO)
- `data/programma/exam_patterns/*.json` (vraagvormen + complexiteitspatronen) — **WEL** input
- `data/programma/examen_vragen/*.json` — **NIET** input (zou circulariteit creëren: concept-set die we testen wordt afgeleid uit testvragen)

**Output**: `data/concepten/competenties/<id>.yaml` met `status: voorgesteld`. Schema in ADR-007 §"Competentie-schema". Anti-fabricatie afgedwongen door `tools/leermateriaal/lib/validate_competentie.py`:

- `gebaseerd_op_concepten` ≥ 2 verplicht
- Elke stap heeft `grondslag.ref` (concept-wikilink, wettekst, of `type: praktijk` met motivering)
- `procedure_grondslag.wettelijk_pct + praktijk_pct == 100`
- `praktijk_pct > 50` → mens-review verplicht vóór `gecureerd`
- Wikilinks moeten bestaande concept-records aanwijzen
- Voorbeelden alleen op basis van bron-chunks van gerefereerde records

**Workflow**: Opus-subagent (via `tools/leermateriaal/propose_competenties.py`) stelt ~6-10 competenties voor per PO. Mens-curatie is licht (5 min per competentie) — geen herschrijven, alleen status → `gecureerd` of `afgewezen`.

### 15. Fase E — Leerpad-opstelling (schema 1.3, 2026-05-15)

Leerpad ordent competenties + concepten + oriëntatie-blokken in een didactische volgorde per PO. Vervangt het ad-hoc "anchor-volgorde wordt minicursus-volgorde"-patroon dat empirisch te versnipperd bleek (PO 1.4 stress-test).

**Input**: alle competenties van een PO + concept-records voor `thematisch`-hoofdstukken + `programma.intro_tekst`.

**Output**: `data/concepten/leerpaden/<X.Y>.yaml` met drie hoofdstuk-types:
- `oriëntatie` (LLM-only, beginselen)
- `competentie` (refereert competentie-yaml)
- `thematisch` (concept-cluster zonder competentie-omhulling)

Schema in ADR-007 §"Leerpad-schema". Opus-subagent (via `tools/leermateriaal/propose_leerpad.py`) stelt voor; mens curates.

### 16. Gaps.json schema-uitbreiding (2026-05-15)

`data/extractie/gaps.json` wordt het centrale gaps-overzicht voor de drie lagen, met `aspect_type`-discriminator:

| `aspect_type` | Verwerking | Bron |
|---|---|---|
| `concept-gap` | ENRICH-pass op records | VERIFY of discovery tijdens ENRICH |
| `competentie-gap` | Fase D heractivatie of mens-curatie | validate_competentie of mens |
| `bron-gap` | Buiten loop — mens beslist over corpus-uitbreiding | Extractie- of competentie-pass die structureel tekortschoot |

`tools/extractie/run_enrichment_cycle.py` filtert op `aspect_type IN (concept-gap, competentie-gap)` als open-werk-criterium. `bron-gap` blokkeert nooit een cyclus.

**Nieuwe `aspect`-waarden** (schema 1.3):
- `rationale.ontbreekt` — record zonder top-level `rationale`
- `rationale.bouwsteen_ontbreekt` — bouwsteen van een centraal concept zonder rationale (signaal, geen blokker)
- `in_praktijk.aspect_te_grof` — `aspect`-tekst zo generiek dat slug onbruikbaar
- `competentie.stappen.te_vaag` — competentie-stap zonder concrete input/output
- `competentie.grondslag.ontbreekt` — competentie-stap zonder `grondslag.ref`
- `competentie.voorbeelden.ontbreken` — competentie zonder `voorbeelden[]`

**Migratie** van bestaande `_bron_voorstellen.json` naar `gaps.json` (`aspect_type: bron-gap`) gebeurt eenmalig via `tools/extractie/migrate_bron_voorstellen.py`. Oude file wordt verwijderd (CLAUDE.md regel 9 — geen leftovers).

### 17. Schema 1.4-implicaties voor extractie-prompts (2026-05-16)

ADR-007 schema 1.4 voegt **bouwsteen-blok**, **formule-blok**, **stap-blok**, **edges-types**, **node_type: synthese** en **cast-conventie** toe. Dat heeft gevolgen voor concept-extractie + verify + enrich:

**Concept-extractie-v4** (`prompts/concept-extractie-v4.md`) dekt schema 1.4 met 14 regels:
- Regel 6 — Stagiair-toon-rewrite verplicht (uitvoerbaar, niet alleen jargon-vrij)
- Regel 7 — Naam-cast uit `data/concepten/casts/globaal.yaml` (geen ABC/DEF/M/D)
- Regel 8 — Stap-blok met `input/output` als semantische arrays + `voorbeeld.substappen[]` met types
- Regel 9 — Edges activeren per type (onderdeel-van → breadcrumb, vergelijkt-met → collapsible, etc.)
- Regel 10 — `node_type: synthese` voor cluster-records
- Regel 11 — Bouwsteen-blok geformaliseerd (titel/wat/waarom/in_praktijk of voorbeelden[]/grondslag)
- Regel 12 — Formule-blok geformaliseerd (formules[] met variabelen + invulling_voorbeeld)
- Regel 13 — Voorbeeld-minimum per node-type
- Regel 14 — Voorbeelden uit drie toegestane bronnen (chunks > bestaand > synthese met cast)

**Competentie-destillatie-v2** (`prompts/competentie-destillatie-v2.md`) erft alle relevante regels van v4 + één conventie-tabel concept-procedure vs competentie (scope/grondslag-type/hoe-inhoud verschillen). Valkuilen krijgen schema-vernieuwing: `correctie` → `advies` (als titel), `foute_aanname` → `vaak_fout` (als sub-info).

**VERIFY-aspect-types** voor schema 1.4 (nieuw in gaps.json):
- `voorbeeld.ontbreekt` — record haalt voorbeeld-minimum niet (regel 13)
- `stap.skeleton` — stap heeft skeleton-titel (heuristisch eerste-N-woorden) zonder `wat`/`hoe`
- `bouwsteen.geen-waarom` — bouwsteen mist `waarom`-rationale
- `bouwsteen.geen-voorbeeld-inline` — bouwsteen mist illustratief voorbeeld
- `formule.geen-variabelen` — formule-blok zonder `variabelen[]`-uitleg
- `formule.geen-invulling-voorbeeld` — formule zonder `invulling_voorbeeld`
- `edges.geen-types` — record heeft edges zonder type-classificatie

ENRICH-prompt v1 wordt uitgebreid met deze aspect-types in de "rationale-aspect"-sectie.

**Naam-cast als infrastructuur** (`data/concepten/casts/globaal.yaml`) bevat ~13 vennootschapsnamen (A-L) + 5 natuurlijke personen + 7 scenario-templates. Prompt v4 + competentie-v2 verwijzen naar deze cast als verplichte naambron voor voorbeelden. Cast is aanvulbaar — nieuwe scenario's worden toegevoegd in de cast-yaml, niet ad-hoc verzonnen.

**Synthese-records** (node_type: synthese) verbinden meerdere concept-records via vergelijkingstabel + Mermaid-beslisboom + kerninzichten. Twee pilots voor PO 1.4 op 2026-05-16:
- `consolidatiemethodes-vergelijking` — vergelijking integrale/evenredige/vermogensmutatie/horizontale
- `consolidatieplicht-beslisboom` — vijfstappenboom "moet ik consolideren?"

ENRICH-pass kan synthese-records voorstellen wanneer ≥ 3 concept-records onderling cross-refs hebben.

### 18. EXTRACT v4 — research-and-draft-agent met event-driven scope (2026-05-17)

Herziening van §13. EXTRACT, VERIFY en ENRICH zijn formeel nog drie stappen, maar in de werkwijze convergeren EXTRACT en ENRICH tot **één agent met verschillende event-types**. De stage-naam ENRICH blijft alleen als procesfase ("oplossen van VERIFY-bevindingen"), niet als aparte tool of prompt.

#### 18.1 EXTRACT is een research-and-draft-agent

De agent krijgt:

- **Scope-declaratie**: één van drie event-types (zie §18.2)
- **Initial-ctx (bounded)**: kerncontext op basis van scope (chunks, records, anchors)
- **Retrieval-tools on-demand**: concept-RAG, bronnen-RAG, file-reads — agent beslist zelf wanneer hij meer ophaalt

De agent schrijft direct naar disk + concept-RAG via de records-API (ADR-019). Er is geen aparte "drafts"-laag, geen APPLY-stap. Wat de agent schrijft *is* de waarheid op het moment dat hij het schrijft.

**v1.0-mindset**: records hebben geen `draft`-status. Het *gedrag* is dat de agent v1.0-kwaliteit produceert — geen "we polijsten dat later wel"-houding. Iteratieve verbetering gebeurt op prompt- en cast-niveau, niet op record-niveau.

#### 18.2 Drie event-types — één agent

| Event | Scope | Initial-ctx (kern) |
|---|---|---|
| **Nieuwe PO** | Alle anchors van PO + cross-PO records die `linked_anchors` delen | Anchor-bundles + cross-PO records (via concept-RAG) |
| **Nieuwe bron** | Alle anchors waar bron-chunks raken + records op die anchors | Nieuwe bron-chunks + geraakte anchor-bundles + bestaande records |
| **Feedback-set uit VERIFY** | Records met VERIFY-feedback | Feedback-rapport (concrete punten per record) + de records + relevante chunks via hun anchors + neighbors via retrieval |

Bij elk event: zelfde agent, zelfde tools, zelfde records-API. Alleen het initial-ctx verschilt. Daarmee verdwijnt ENRICH als aparte tool — een gap-event is gewoon een EXTRACT-trigger met een ander initial-ctx.

#### 18.3 VERIFY blijft routinematig

Per EXTRACT-batch draait VERIFY automatisch op de gewijzigde records (niet per individuele record — per batch). VERIFY's initial-scope = de gewijzigde set, maar de agent mag (en moet vaak) **neighbors via retrieval ophalen** om vergelijkingen te kunnen maken: cross-record overlap-checks, edge-consistentie, terminologie-uniformiteit. VERIFY is dus zelf óók een research-agent — kleine startcontext, retrieval-on-demand.

Findings stromen op twee manieren terug:

- **Tactisch (per-record)**: VERIFY-feedback wordt zelf een event → triggert een nieuwe EXTRACT-run met dezelfde anchor-context aangevuld met de feedback-punten als input. Loop convergeert idealiter naar clean, maar 0-gaps is een doel, geen regel — sommige feedback is fundamenteel (bron mist info, examenvraag onoplosbaar). Max-iteraties + mens-review bij stall.
- **Strategisch (per-prompt)**: patronen over VERIFY-findings (bv. "5 records missen `in_praktijk`-blok") sturen prompt- of cast-evolutie. Periodiek, door mens of audit-agent.

VERIFY moet meestal niets vinden. Wanneer hij wél iets vindt, is dat een echt regressie-signaal. Hij blijft routinematig draaien ook al is hij meestal groen — discipline voorkomt sluipende erosie.

#### 18.4 Pipeline (vervangt §13's lineaire EXTRACT → VERIFY → ENRICH → AUTO-MERGE)

```
EVENT (nieuwe PO / nieuwe bron / gap-set)
   │
   ▼
EXTRACT (research-and-draft-agent)
   - Records → records-API → disk + concept-RAG (atomair, ADR-019)
   │
   ▼
VERIFY (regressienet, op gewijzigde set)
   │
   └─ feedback niet leeg → EVENT met feedback + zelfde anchor-context → EXTRACT
                                                 (loop met max-iter + stall-review)
```

AUTO-MERGE is overbodig: records-API schrijft direct, geen aparte merge-stap.

#### 18.5 Pilot-aanpak

Voor de eerste implementatie van §18 starten we **single-agent op kleinste scope** (één anchor met enkele chunks en bestaande records). Coordinator + sub-agenten zijn een mogelijke schaalstrategie maar pas-na-pilot-evaluatie. Eerst zien wat single-agent oplevert op realistische data.

#### 18.6 Agent-gedrag — bevindingen pilot 2026-05-18

Eerste pilot op anchor `1.5.V.C` (IAS 17 / IFRS 16 leasing) bevestigde een paar werkregels die we expliciet vastleggen voor toekomstige EXTRACT-runs:

- **Anchor-tekst volgen, niet verbeteren**. De anchor zei "IAS 17" terwijl de huidige standaard IFRS 16 is. Records dekken de huidige norm; de spanning wordt gedocumenteerd via `historische_noot` in het record zelf. `data/programma/anchors.json` reflecteert het aangeleverde examenprogramma woordelijk — wij wijzigen dat niet ook al voelt het outdated.
- **Edge-only-update op bestaande records mag** wanneer de tekst-inhoud al v1.0 is en de wijziging zuiver een cross-link is. Geen verplichting om elk geraakt record tekstueel te herschrijven. Bij twijfel: behoud + edge toevoegen is veilig.
- **Synthese-records hebben geen vast schema**. Schema 1.4 specificeert geen verplichte veld-shape voor `node_type: synthese` (geen `definitie`, geen `main_rule` top-level). De agent stelt de shape voor op basis van wat de synthese vereist (vergelijkingstabel, beslisboom, Mermaid-diagram). Het voorbeeld-minimum uit ADR-007 schema 1.4 blijft wel gelden — een uitgewerkt voorbeeld of vergelijking is verplicht.
- **Bron-gaps signaleren, niet maskeren**. Wanneer de chunker een bronstuk verbergt (bv. een heading niet als sectie-grens herkent waardoor cruciale alinea's onder een verkeerde sectie hangen), schrijft de agent een `bron-gap`-entry in `gaps.json` ipv het te omzeilen. De ETL-bug wordt apart behandeld; EXTRACT moet eerlijk zijn over wat retrieval mist.

#### 18.7 Wave-planning per PO — scope-granulariteit voor agent-launches (2026-05-18)

EXTRACT v4 is per-agent **scope-gebonden**: één agent verwerkt één scope-eenheid. De launcher (de gespreks-agent of de mens) beslist welke scope-eenheid. Bij PO 1.5 en 1.6 is empirisch vastgesteld dat de scope-granulariteit een sweet spot heeft: te klein verspilt tokens op overhead, te groot verzwakt prompt-discipline na ~30-40 record-mutaties.

**Indicator vooraf — anchor-count** + **record-count** (na 2026-05-19 update):

| Anchor-count | Voorspelde records | Aanbevolen aanpak | Bewijs |
|---|---|---|---|
| < 5 | < 20 | Eén agent voor hele PO | — |
| 5–13 anchors mét bestaande records | 25–60 | **One-shot**: één agent voor touch-up + lichte content-depth | PO 1.8 (53 records, 20 min, 180k tokens, 0 nieuwe gaps), PO 1.9 (44 records), PO 1.1–1.4 touch-ups (42–73 records elk) |
| 10–15 nieuwe / greenfield | onbekend | Twee waves: top-level + sub-anchors | PO 1.5 (14 anchors, ~150 records) |
| > 15 nieuwe / greenfield | > 100 | Wave 1 top-level + parent-batched wave 2 | PO 1.6 (20 anchors, ~165 records), PO 1.7 (58 anchors, 16 batches) |

**One-shot empirisch gevalideerd 2026-05-19**: voor PO's met grotendeels bestaande records (schema-bump + situering + naam_alternatief + lichte content-depth) is one-shot 3-4× efficiënter dan parent-batched. Voor greenfield-content blijft wave-strategie superieur (focus + bestaansreden-test-rigor).

Ruwe record-prognose: **anchor-count × 8–10 ≈ records**. PO 1.5 = 14 anchors → ~150 records. PO 1.6 = 20 anchors → ~165 records.

**Indicator na wave 1 — record-count per top-level**:

Na de wave-1 pass (één agent per top-level anchor) wordt de wave-2 granulariteit *empirisch* bepaald per parent-anchor:

- Parent met ~10-25 records over sub-anchors → **één parent-batched agent** voor alle sub-anchors van die parent (token-besparing, cross-sub-anchor coherentie).
- Parent met >25 records over sub-anchors → **per-sub-anchor agent** (kwaliteit voorop).

**Trade-offs samengevat**:

| Dimensie | Per-anchor | Parent-batched | Per-PO |
|---|---|---|---|
| Tijd (wall-clock) | Langzaamst (sequentieel) | Tussen | Snelst (mits scope past) |
| Tokens | Duurst (overhead × N) | 30–40 % goedkoper | Goedkoopst |
| Kwaliteit | Beste diepte per scope | Hogere cross-anchor coherentie | Risico op decay na 30+ mutaties |

Parallelle agents zijn **niet** veilig: sub-anchors delen records via `linked_anchors`, parallelle writes naar records-API geven last-write-wins en verloren mutaties. Disk-druk van meerdere worktrees verergert het.

**Centraal-first blijft de regel**: top-level anchors gaan vóór sub-anchors. Top-level past de structurele issues aan (type-migraties, bron-prefix renames, situering-velden, deprecated edges, naam_alternatief voor EN-termen) over de cross-anchor records. Sub-anchor passes focussen daarna op diepte en specificiteit.

#### 18.8 Resterende open punten

- **Sub-agent eigenaarschap voor verwijderingen**: mag een sub-agent records verwijderen die niet door hemzelf zijn aangemaakt? Veiliger om delete-suggesties via coordinator te leiden. *(Tot nu toe in praktijk: agent deletet alleen wat hij hernoemt of vervangt, niet onbeperkte cleanup.)*
- **Loop-limiet bij gap-events**: na N iteraties zonder convergentie → human review. Bestaande `run_enrichment_cycle.py`-mechanisme hergebruikt.
- **EXTRACT v4-prompt zelf**: concrete tekst van de prompt + cast-uitbreidingen worden iteratief vastgesteld op basis van pilot-uitkomsten, niet voor-de-pilot vastgelegd. *(Status 2026-05-18: 13+ patch-rondes, stabiel.)*

## Empirische onderbouwing

### PO 4.0 Deontologie

- 36 anchors (3 taken, 13 doelstellingen, 20 kenniselementen)
- 2883 chunks (1187 wettekst + 155 norm + uitbreiding na test)
- Anchor 4.0.I.D.7 Beroepsgeheim als test-case → 12 grounded concepten
- Centroïde-pathologie van 32/36 anchors (één definitielijst-chunk top-1) → 2/36 na clean enrichment
- 90-99% van enrichment score-winst is vocabulair, niet self-fulfilling
- 814/814 niet-relevante Strafwetboek-artikelen automatisch onder drempel (scope-validatie zonder curatie)

### PO 1.1 Algemene boekhouding

- 74 anchors (1 taak, 10 doelstellingen, 63 kenniselementen)
- 5275 chunks (3633 wettekst + 1478 advies + 164 norm)
- Anchor 1.1.II.B Vaste activa als test-case → 18 grounded concepten
- Mediane top-1 score per anchor: 0.706 (vs 0.699 in PO 4.0) — **drempels generaliseren zonder herkalibratie**
- CBN-adviezen werken **beter** als bron dan wetteksten: ~25% bundle-ruis (vs ~60% in PO 4.0), samenhangender, lager hallucinatierisico

## Gevolgen

### Helper-scripts in `tools/extractie/`

- `match_bronnen.py` — bron-first matching (deterministisch, geen LLM)
- `export_bundle.py` — exporteert anchor-bundle met volledige chunk-tekst voor LLM-pass
- `embedding_daemon.py` + `tools/lib/records_api.py` — concept-record indexering (ADR-018, ADR-019)

Geen `anthropic` import in deze scripts.

### LLM-werk

Twee subagent-passes per PO:
1. Anchor-verrijking (eenmalig, output gegit)
2. Per-anchor concept-extractie (één Opus-sessie verwerkt alle anchors sequentieel)

### Coverage gap-fill

Gap-detectie via "anchor zonder sterke match" werkt **niet betrouwbaar** — bge-m3 koppelt soms abstract-gecombineerde termen slecht ondanks aanwezige bronnen. Empirisch: 3 van 4 vermeende gaps voor PO 4.0 zaten wél in scope.

Voor productie: gap-detectie verschuift naar **examen-driven validatie in Fase 5** (echte voorbeeldexamens als toets-instrument), niet naar een aparte retrieval-pad. Anchors zonder sterke bundle worden gerapporteerd in een diagnostiek-rapport (mediane bundle-score, bundle-grootte per anchor) — geen actie zonder eerst te kijken naar patronen.

## Voorbehoud

- **Slechts twee PO's getest** uit ~30. Andere vakken (fiscaliteit, audit, vennootschapsrecht) hebben andere bron-mix en anchor-stijl. Hoeven geen blocker te zijn — de aanpak is robuust gebleken — maar kalibratie kan per PO nodig zijn.
- **Bestaande concepten als anchor** (§7) is empirisch onbevestigd. Ontwerpprincipe maar niet getest.
- **Cross-PO matrix** (anchors van meerdere PO's tegelijk) niet getest — komt pas bij volledige run.
- **Brede anchors hebben grote bundles** (PO 1.1 bundles tot 1053 chunks): adaptive bundling alleen volstaat niet altijd. Eventuele aanvullende filters in toekomstige iteratie. Geen blocker voor accept.

## Open ETL-revisies (separate ADR-006-revisies)

Niet onderdeel van deze ADR; uitgelicht als follow-ups die het systeem verder zouden verbeteren:

- **Definitielijst-chunking**: artikelen die enumeratieve definitielijsten zijn (bv. *"1° X: ...; 2° Y: ..."*) gedragen zich pathologisch (centroïde-effect). Alternatieve chunking of een `chunk_rol`-tag.
- **Art-familie chunking**: 458/bis/ter/quater (Strafwetboek) en 1382-1384 (BW) als één semantisch cluster i.p.v. losse chunks.
- **Chunk-rol-tagging in ETL**: metadata-veld `chunk_rol` (`definitie`/`intro`/`inhoudelijk`/`bijlage`/`voorbeeld`) met query-tijd prior — definitie-chunks lage prior bij concept-extractie.

## Open implementatie-eisen

- Concept-extractor moet `chunk_sha` uit ChromaDB-metadata kopiëren naar `_provenance.<veld>.inputs[].sha256` (nu `null`).
- `tools/etl/mark_stale.py` voor concepten bouwen: vergelijk opgeslagen `sha256` met live ChromaDB `chunk_sha`; flag mismatches.
- `tools/etl/remove_bron.py` Laag 2 omzetten: scan `data/concepten/records/**/_provenance.*.inputs[].id` voor chunk-impact-analyse.
