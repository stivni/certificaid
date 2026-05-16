# Certificaid Roadmap

Werkdocument — geen ADR. Beschrijft *welke fasen* in welke volgorde worden aangepakt en wat "klaar genoeg om door te schuiven" per fase betekent. Architecturale beslissingen leven in [`docs/adr/`](adr/INDEX.md).

## Mindset

- **POC met protoduction-aanname** — alle code wordt productie-code. We bouwen geen wegwerpprototype.
- **Vertical slice eerst** — één programmaonderdeel, end-to-end (ruwe bron → leesbare bron → bron-RAG → concepten → fiche → tutor → oefenvraag) vóór we horizontaal verbreden naar alle programmaonderdelen. Forceert dat elke laag werkelijk werkt, niet enkel ontworpen is.
- **"Never done" als framing** — DoD per fase is *"goed genoeg om door te schuiven + regressietest aanwezig"*. Niet "100%". Bij nieuwe inzichten kunnen we terugkeren naar elke laag zonder de hele pipeline te moeten herbouwen.
- **Iteratief, niet sequentieel** — fasen kunnen overlappen. De voorbeeldexamens-laag (ground truth) en de examenprogramma-laag worden parallel opgebouwd; examenpatronen lopen parallel aan concept-extractie.

## Fasen

### Fase 0 — Provenance-plumbing

**Doel**: elk artefact draagt zijn afkomst — anders is iteratief reprocessen handcrafting.

Concreet:
- Provenance-schema in YAML frontmatter / JSON body voor bron-MD, RAG-chunk, concept-record, fiche-snapshot
- `tools/lib/provenance.py` — read/write/cascade
- `tools/etl/mark_stale.py` — input-hash verandert → downstream `stale=true`

DoD: bestaande bron-MD's krijgen retroactief een provenance-blok; `mark_stale` gedraagt zich correct op een handmatig gewijzigde input.

ADR: [ADR-004](adr/ADR-004-provenance.md).

---

### Fase 1 — Bronnen ETL op punt

**Doel**: ruwe bron → leesbare markdown, met behoud van structurele headings, tabellen en bron-rol-classificatie.

Concreet:
- `extract.method`-dispatcher (zie ADR-005) afgewerkt voor alle voorkomende methodes
- Open punten:
  - `justel_html`-handler nog niet geïmplementeerd
  - Oud-BW herconverteren
  - 104 legacy `type:`-bronnen migreren naar `extract:`-schema
  - ~~**ITAA-norm-* produceren geen `##`-headings**~~ — opgelost 2026-05-14 via 3 norm-specifieke transformers (`strip_norm_toc_residue`, `strip_norm_column_bleed`, uitgebreide `strip_itaa_norm_footers`). 17/18 normen nu trusted (IESBA mist lokale PDF).
- Golden set: 5–10 referentie-bronnen handmatig OK-bevonden, vastgepind als regressietest
- Agent-QA-stap: LLM leest output-MD en flagt structurele problemen

DoD: golden tests groen + agent-QA-rapport voor de POC-bronnen "pass".

**Architecturale follow-ups** (geïdentificeerd 2026-05-15):
- **`inject_headings_wettekst` hardcoded `_chunk_type = "Art."`**: zet altijd `chunk.type: "Art."` in frontmatter ongeacht of body `Art.`- of `Artikel`-headings heeft. Voor EU-bronnen met `Artikel`-headings wordt de frontmatter handmatig overschreven na conversie. Bij re-conversie wordt die handmatige fix weggeschreven. Fix: `detect_hierarchy` artikel-type-detectie uitbreiden, of `inject_headings_wettekst` een `article_type`-parameter geven.
- **Body-niveau column-bleed** in 3 ITAA-normen (effectennorm, aww-geconsolideerd, omzetting-vennootschap): paragrafen interleaven door tweekoloms-PDF-extractie. Vereist column-aware PDF-extractie (pymupdf met blocks/columns), niet oplosbaar via text-transformer.
- **Bijlage-tabellen** in effectennorm + omzetting-vennootschap renderen als gefragmenteerde `##`-headings. Idem: vereist tabel-aware extractie.
- **5 wetteksten** met overgebleven structuur-issues open: Decr-Waals-Directe-Belastingen, MIGB-Brussel/Vlaanderen/Wallonie, Wet-beroepskwalificaties-2008. Per bron eigen oorzaak (regio-suffix, false-positive headings, mixed Art./Artikel) — case-by-case ETL-werk.
- **9 wetteksten needs-rework**: narratieve praktijkgidsen (almanakken, toelichtingen aangifte) — sub-optimale structuur, accepteerbaar als praktijkgids met caveat indien gewenst.

ADR: [ADR-005](adr/ADR-005-bronnen-etl.md).

---

### Fase 2 — Bronnen-RAG op punt

**Doel**: gegeven een query, retourneer de juiste passages uit de bron-corpus.

Concreet:
- ✅ bge-m3 embedding op MPS (chunker- + embedding-pipeline werkend)
- ✅ Adaptive sub-chunking met threshold-tiers + 6 marker-types + definitie-detectie (2026-05-14, ADR-006 §4.2)
- ✅ Eerste full-build (2026-05-15): **18.185 chunks in ChromaDB** (15295 wettekst + 270 norm + 2620 advies)
- ⏳ bge-reranker-v2-m3 voor twee-fase retrieval — implementatie nog te valideren
- ⏳ Vragen-testset (uit voorbeeldexamens) + top-k recall als regressie-metriek
- ⏳ `tools/rag/eval.py` voor reproduceerbare eval

DoD: top-k recall op vragen-testset boven drempel; reproduceerbaar via `tools/rag/eval.py`.

ADR: [ADR-006](adr/ADR-006-rag-strategie.md).

---

### Fase 3 — Conceptmodel + concept-extractie

**Doel**: het tijdloze fenomeen-niveau van het ITAA-domein vastgelegd als knowledge graph.

**Status 2026-05-16**: schema 1.4 vastgelegd, drie-lagen-pipeline (concepten + competenties + minicursus) operationeel op POC-programmaonderdeel 1.4 (31 records + 9 competenties + 2 synthese-pilots, allemaal deep-rewriten + gerenderd).

Concreet:
- Conceptmodel schema 1.4: stap-blok / bouwsteen-blok / formule-blok / edges-types / node_type synthese / cast-conventie / voorbeeld-minimum
- Concept-extractor v4 + competentie-destillatie v2 + VERIFY/ENRICH schema 1.4-aware
- Schema-evolutie expliciet (versie per record); wijziging schema → record-status `stale`
- Naam-cast (`data/concepten/casts/globaal.yaml`) als infrastructuur voor consistente voorbeelden

**POC DoD (gehaald op PO 1.4)**:
- ✅ Concepten-set "rond" voor PO 1.4 (29/31 deep-rewriten)
- ✅ Voorbeeld-minimum gehaald op 30/31 records
- ✅ Examenvragen-callouts in minicursus (5 geclassificeerde vragen)
- ✅ Synthese-records voor "consolidatiemethodes-vergelijking" + "consolidatieplicht-beslisboom"
- ✅ Quartz build 0 errors

**Open punten voor doorrol naar 27 overige PO's**:
- Cast aanvullen waar nieuwe scenario's nodig (bv. audit-PO heeft andere rollen)
- Anchor-verrijking voor 24 PO's (Fase A is alleen klaar voor 1.1, 1.4, 4.0)
- Bron-corpus aanvullen waar nodig (IFRS, fiscale instructies, audit-ISA's)

ADRs: [ADR-007](adr/ADR-007-conceptmodel.md) schema 1.4, [ADR-008](adr/ADR-008-concept-extractie.md) §13-17, [ADR-010](adr/ADR-010-leermateriaal-tutor.md) drie-lagen render-architectuur.

---

### Fase 4 — Concepten-RAG

**Doel**: concepten doorzoekbaar maken voor tutor (live) en voor zelf-extractie (concept-X verwijst naar concept-Y).

Concreet:
- Zelfde RAG-strategie (ADR-006), aparte ChromaDB-collection
- Per node-veld een chunk; edges meedragen als metadata zodat retrieval een sub-graph levert
- Eval: kunnen we de juiste concept-records terughalen voor een test-vraag?

DoD: tutor kan "wat is de meldingsplicht?" beantwoorden via concepten-RAG, niet meer via bronnen-RAG.

ADR: [ADR-006](adr/ADR-006-rag-strategie.md) (zelfde als bronnen-RAG, andere collection).

---

### Fase 5 — Leermateriaal-strategie

**Doel**: van concepten naar publiceerbare leerstof + interactieve tutor.

Concreet:
- Tutor live op concepten-laag (lage latency)
- Leermateriaal als release-snapshot (versie-tag + changelog), `content/snapshots/<versie>/`
- Voorbeeldvragen gegenereerd uit concept × examenpatroon
- Confidence-labeling overal (⚖️/🤖)

DoD: student kan voorbeeldexamen-vragen oplossen na bestudering van een snapshot; tutor kan dezelfde vragen beantwoorden vanuit concepten.

ADR: [ADR-010](adr/ADR-010-leermateriaal-tutor.md).

---

## Cross-cutting (loopt continu mee)

- **Kenniselement-dekkingscheck** — voor elk kenniselement uit het examenprogramma: minstens één concept dat hem afdekt + minstens één voorbeeldvraag of examenpatroon dat hem toetst. Eerste-orde regressietest. ([ADR-002](adr/ADR-002-examenprogramma-scoping.md))
- **Voorbeeldexamens-corpus** — vroeg ingelezen en gestructureerd; ground truth voor concepten én patronen. Nooit geforceerd ("dit examen vraagt X dus we maken concept X" is verboden — zie ADR-008).
- **Examenpatronen-laag** — bouwt parallel aan concept-extractie. Drie functies: lens bij extractie, validator van conceptenset, generator van oefenvragen. ([ADR-009](adr/ADR-009-examenpatronen.md))
- **Reprocessing-strategie** — input verandert → stale-cascade, geen auto-regen. Mens kiest of/wanneer. ([ADR-003](adr/ADR-003-reprocessing-evaluatie.md))

## POC-keuze (volgende stap)

Eén programmaonderdeel kiezen dat in een voorbeeldexamen écht getoetst is + waarvan de bronnen al gemigreerd zijn naar `extract:` (ADR-005). Eerste verticale slice doorlopen. Daarna verbreden.
