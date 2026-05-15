# ADR-008: Concept-extractie via bron-first matching

**Status**: Accepted
**Datum**: 2026-05-09
**Empirisch onderbouwd op**: PO 4.0 Deontologie, PO 1.1 Algemene boekhouding

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

### 6. Verdieping per concept — fase D

Voor elke seed → status `partieel` → eventueel `gevuld`:
- Verdiepende retrieval-queries met cumulatieve concept-state als input
- LLM vult `exceptions`, `scope`, edge-targets verder in
- Status `gevuld` (later, eventueel handmatig of via tweede LLM-pass): `pitfalls`, `voorbeeld_inline`

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
| **Matches** | `data/extractie/<po>/matches/<po>-matches.json` | Ephemeral — kan in gitignore | reproduceerbaar |
| **Bundle exports** | `data/extractie/<po>/bundles/<po>-<anchor-id>.json` | Ephemeral — input voor LLM-pass | wegwerpbaar |
| **Concept-records** | `data/concept_records/<id>.json` | Permanent — duurzame kennislaag | authoritative |

De permanente provenance leeft uitsluitend in concept-record `_provenance`-velden. Andere artefacten zijn een tussenstadium.

### 12. Schema-evolutie tijdens extractie

Wanneer een concept niet past in het huidige conceptmodel:
- Subagent genereert expliciet schema-uitbreidingsvoorstel (nieuw veld, nieuw node-type, nieuw edge-type)
- Voorstel landt in `data/concept_records/_voorgestelde_types.yaml` (zie ADR-007)
- Pas na menselijke bevestiging wordt het schema bijgewerkt

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
- `embedding_daemon.py` + `index_concept_incremental.py` — concept-record indexering (ADR-018)

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
- `tools/etl/remove_bron.py` Laag 2 omzetten: scan `data/concept_records/**/_provenance.*.inputs[].id` voor chunk-impact-analyse.
