# ADR-009: Conceptlaag — domeinmodel als getypeerde knowledge graph

**Status**: Draft (versie 2)  
**Datum**: 2026-05-06  
**Vervangt**: ADR-009 versie 1 (zelfde nummer; zie git history voor de oude versie met `main_rule`/`exceptions`/`obligations`/`pitfalls`/`examples`-schema)

## Context

Een eerste poging tot een conceptlaag (versie 1 van dit ADR) gebruikte één plat JSON-schema met velden zoals `main_rule`, `exceptions`, `obligations`, `pitfalls`, `examples`. Het schema paste redelijk op één type kennis (een norm-met-uitzonderingen, zoals AWW-meldingsplicht), maar kraakte op andere soorten kennis.

Verkenning van bronnen, materie- en competentie-fiches en examenvragen toonde aan dat het ITAA-domein een **mix aan soorten kennis** is: definities, juridische regels, beginselen die oordeel vergen, gestructureerde procedures, methodes met methode-keuze, jaarlijks indexerende drempels, casuïstiek uit jurisprudentie en CBN-adviezen, deontologische normen, skills en overkoepelende fenomenen. Het examen toetst vooral **relaties** tussen deze nodes (uitzonderingen, primaat, contrasten, triggers, procedurele volgorde) — niet definities.

Een uniform schema kan dat niet vasthouden. Het domeinmodel is een **getypeerde knowledge graph**: nodes met type-specifieke velden, verbonden door getypeerde edges met conditie- en scope-velden.

## Beslissing

### Architectuur

- **Nodes** = JSON-files in `data/concept_records/<id>.json`. Eén file per node.
- **Edges** = veld *binnen* de bron-node (uitgaande edges). Bidirectioneel walken via in-memory index.
- **Graph-walks** (paden, primaat-ketens, "wat hangt rond X?") via **NetworkX** — alle JSON in geheugen, walks in milliseconden.
- **Vector-zoek** (semantische match) blijft ChromaDB. Edges meedragen als metadata zodat een query een sub-graph teruggeeft.
- **Schema-evolutie** = veld toevoegen in JSON. Geen migrations.
- **Geen aparte graph-DB** voor de huidige schaal (~500–1500 nodes verwacht).

### Designprincipes

1. **Het record reflecteert het domein** — niet het examenprogramma, niet de tutor, niet de Quartz-fiches.
2. **Groeibaarheid first-class** — schema mag (en zal) evolueren. Sparse fields zijn de norm; partieel ingevulde records zijn geldig.
3. **Concept = fenomeen, niet artikel of vak** — vakoverschrijdend is de regel.
4. **Collecties zijn Fenomeen-nodes** met `bevat`-edges. PO's, "BTW-aangifte", "relatiegeschenken" zijn zo gemodelleerd. Eén abstractie, geen aparte view-laag.
5. **Compositie boven duplicatie — opt-in.** Default sub-stap = inline. Pas een aparte node maken als de modelleur expliciet ziet dat twee procedures echt dezelfde sub raken.
6. **Temporal flexibel** — Drempel heeft `versies[]`-array; node kan ook `valid_from`/`valid_to` hebben; Casus (jurisprudentie) heeft eigen relatie via edges zoals `vernietigt-deel-van`.
7. **Iteratief proces, geen one-shot extractie** — een concept-extractie genereert nieuwe candidate-nodes in een queue voor volgende rondes via `_dangling: true`-flag op edges naar nog-niet-bestaande targets.
8. **Breedte én diepte** — niet diepgang boven dekking. Eerste records mogen ruim/diep zijn als schema-bewijs; einddoel is dekking met voldoende diepte.
9. **Accountant-taal in de hoofdtekst** — `tekst`, `definitie`, `omschrijving` worden geschreven in de praktijktaal van een accountant: actief, direct, met concrete situaties. Niet in juridisch jargon ("onderworpen entiteit", "in voorkomend geval"). Letterlijke wetcitaten leven apart in `source.citation`.
10. **Voorbeelden hebben een eigen veld** — synthetische praktijkvoorbeelden leven niet in `definitie`/`tekst` maar in `voorbeeld_inline` (string of array). Casus-nodes blijven enkel voor échte gevallen (jurisprudentie, voorbeeldexamenvraag, CBN-advies-feitenset).
11. **Jargon-glossary verplicht** — termen die niet door elke target-lezer (stagiair GA/GBA met basiskennis) intuïtief gevat worden, krijgen een eigen Begrip-node en worden vanuit het gebruik gelinkt via `vereist-kennis-van`. Concrete eerste lijst (zie ronde C-implementatie): *actief, passief, balans, resultatenrekening, boekwaarde, vaste-activa, voorheffing, verrichting, onderworpen-entiteit, cliënt*.
12. **Geen tags voorlopig** — tags zoals `["1.2", "boekhouding"]` bleken weinig operationele waarde te hebben. Domein-/PO-koppeling loopt via `bevat`-edges van Fenomeen-nodes. Eventueel later operationele tags (post-2020, exam-frequent, regio) als de tutor of indexering ze nodig blijken.
13. **Verwijzingen als gestructureerde child-property, niet inline in prose** — een `regel`/`uitzondering`/`definitie`/`stap`-blok bevat de tekst in accountant-taal *zonder* parenthetische artikelverwijzingen. Cross-references staan als getypeerde edge-velden direct op het blok (zie "Edges op block-level" hieronder). Twee winsten: (a) de prose blijft leesbaar, conform principe #9, en (b) edges zijn machinaal walkbaar zonder regex op tekst. Detectie en lifting gebeurt tijdens **concept-extractie** (stap 4), niet tijdens chunking — een chunk blijft de bron-tekst integraal weergeven.

### Node-types (initieel 11; mag groeien)

| Type | Wat het is | Sleutel-velden | Voorbeeld |
|---|---|---|---|
| **begrip** | classificerende definitie of begrip met formule | `definitie`, optioneel `formule`, `variabelen[]`, `voorbeeld_inline`, `signalen`, `subtypes`, `kader` | UBO, atypische verrichting, marginale aanslagvoet, aanschaffingswaarde |
| **regel** | bindende verplichting/verbod | `tekst`, `source`, optioneel `modaliteiten`, `vervolgverplichtingen`, `sub_verboden`, `bescherming_melder` | meldingsplicht AWW art. 47, verbod-nevendiensten-assurance |
| **beginsel** | leidraad waarvan toepassing oordeel vereist | `tekst`, `facetten[]` (met `naam`, `alias`, `tekst`) | onafhankelijkheid (feitelijk/schijn), voorzichtigheid |
| **procedure** | gesequentieerde stappen | `doel`, `stappen[]` met per stap `nr`, `naam`, `type`, `beschrijving`, optioneel eigen `edges` en `source` | atypische-verrichting-opvolgen, belastingberekening-pb |
| **methode** | formule of methodekeuze | `formule`, `variabelen[]` (met node-ref), optioneel `omschakelregel`, `fiscale_beperkingen[]` | lineaire vs degressieve afschrijving |
| **drempel** | numerieke waarde met geldigheidsvenster | `versies[]` met `aanslagjaar`/`valid_from`/`valid_to`/`waarde`/`schijven`/`source`/`lookup` | belastingvrije som, contantengrens, PB-tarieven |
| **skill** | operationele vaardigheid (handelend werkwoord + object) | (uitwerking volgt bij eerstvolgende skill-modellering) | ratio interpreteren, opdrachtbrief opstellen |
| **casus** | referentie naar échte situatie (geen synthetische voorbeelden) | `feitenset`, optioneel `vraag`, `antwoord`, `uitspraak`, `source` (jurisprudentie/voorbeeldexamen/cbn-advies) | GwH 114/2020, voorbeeldvraag-2015-adjustments |
| **afwegingskader** | conditionele regel "als A+B+C dan X anders Y" | (uitwerking volgt bij CBN-advies-modellering) | inbreng-benadering bij herwaardering (CBN 2009/15) |
| **actor** | actor die in regels wordt aangeduid | `definitie`, `verantwoordelijkheden[]`, `rol` | AMLCO, Stafhouder, CFI |
| **fenomeen** | overkoepelend onderwerp, bundel andere nodes | `omschrijving`, `kerncomponenten_inline[]`, `bevat`-edges | antiwitwaswetgeving, BTW-aangifte |

**Facetten leven binnen een node** (geen aparte nodes), bv. *feitelijke* vs *schijn* van onafhankelijkheid.

**Synthetische voorbeelden** leven in een `voorbeeld_inline`-veld (string of array van strings/objecten met `situatie`/`uitkomst`). Niet in `definitie`/`tekst`. Casus-nodes blijven voor échte gevallen (jurisprudentie, voorbeeldexamenvraag, CBN-advies-feitenset).

**Boekhoudkundige verwerking** krijgt op nodes met boekhoudkundige relevantie een gestructureerd blok:

```json
"boekhoudkundige_verwerking": {
  "journaalpost": [
    {"debet": {"rekening": "6302", "naam": "Afschrijvingen materiële vaste activa"}, "credit": {"rekening": "22-27 (cumul.)", "naam": "Cumulatieve afschrijving"}}
  ],
  "balans_presentatie": "Onder vaste activa: aanschaffingswaarde – cumulatieve afschrijving = boekwaarde",
  "voorbeeldboeking": "Machine € 50.000, gebruiksduur 5j, lineair: jaarlijkse boeking 6302 / 22x = € 10.000"
}
```

**Notities-mechanisme** — zowel nodes als edges mogen een `notities[]`-array hebben voor open bedenkingen die niet in de hoofdcontent thuishoren ("twijfel of dit Begrip of Methode is", "te verifiëren na 2027 wetwijziging"). Eenvoudig formaat: `[{"tekst": "...", "datum": "YYYY-MM-DD"}]`. `datum` optioneel. Anders dan `status` (proces-flow): notities zijn semantische bedenkingen.

### Bronverwijzing — gestructureerd

```json
"source": {
  "type": "wet" | "kb" | "itaa-norm" | "cbn-advies" | "isa" | "jurisprudentie" | "voorbeeldexamen",
  "short": "AWW art. 47 §1",
  "ref": { ... },
  "citation": "exact quote (optioneel)"
}
```

`ref` per type:
- **wet**: `{wet, artikel, paragraaf}`
- **kb**: `{kb, artikel}`
- **itaa-norm**: `{norm, sectie, datum?}`
- **cbn-advies**: `{nummer, paragraaf?}`
- **jurisprudentie**: `{instantie, rolnummer, datum}`
- **voorbeeldexamen**: `{jaar, vak, type}`

### Edge-types (initieel ~20; mag groeien)

Conventie: `<bron-node> [edge-type] <target-node>` leest als een geldige zin.

| Edge | Lees-conventie | Voorbeeld |
|---|---|---|
| `definieert` | bron definieert target | Regel definieert Begrip |
| `regelt` | bron regelt target | Regel/Procedure regelt Fenomeen/Begrip |
| `uitzondering-op` | bron is uitzondering op target | Regel uitzondering-op Regel (met `scope`) |
| `primeert-boven` | bron primeert boven target | Regel primeert-boven Regel (met `conditie`) |
| `contrasteert-met` | bron contrasteert met target | any ↔ any (met `scharnier`) |
| `van-toepassing-op` | bron is van toepassing op target | Regel van-toepassing-op Begrip/Actor |
| `getriggerd-door` | bron wordt getriggerd door target | Regel/Procedure getriggerd-door Begrip |
| `vereist-kennis-van` | bron vereist kennis van target | Skill/Procedure/Stap vereist-kennis-van Begrip |
| `toegepast-via` | bron wordt toegepast via target | Beginsel toegepast-via Procedure/Methode/Regel |
| `voorbeeld-van` | bron is voorbeeld van target | Casus voorbeeld-van Regel/Beginsel (met `aspect`) |
| `bevat` / `onderdeel-van` | bron bevat target / bron is onderdeel van target | Fenomeen ↔ leden |
| `vervangt` / `vervangen-door` | temporal: opvolger | node ↔ node |
| `gemeten-met` / `instrument-van` | Begrip gemeten-met Methode | Begrip ↔ Methode |
| `bedreigt` / `bedreigd-door` | Begrip bedreigt Beginsel | bedreigingen voor onafhankelijkheid |
| `ratio` | Regel/Methode ratio Beginsel/Begrip | uitleg waarom een regel of methode bestaat (target bij voorkeur Beginsel); optionele velden `scharnier` (kort) en `redenering` (uitgebreid) |
| `alternatief-voor` | Methode alternatief-voor Methode | lineair vs degressief |
| `schakelt-over-naar` | Methode schakelt-over-naar Methode | degressief → lineair onder conditie |
| `vernietigt-deel-van` | Casus (jurisprudentie) vernietigt-deel-van Regel | GwH-arrest 114/2020 |

Edges hebben optionele velden: `scope`, `conditie`, `scharnier` (kort), `redenering` (uitgebreid), `aspect`, `_dangling`, `notities[]`.

**Ratio-edge bij voorkeur naar Beginsel** — een Regel die rust op het voorzichtigheidsbeginsel, een Methode die rust op stelselmatigheid: deze edges versterken de domein-coherentie. Niet altijd mogelijk (bv. tipping-off rust op opsporingseffectiviteit, geen Beginsel) — dan target = Begrip of `_dangling`.

### Edges op block-level

Conform designprincipe #13 mogen edges niet alleen op node-niveau staan, maar ook **op het niveau van een individueel blok** binnen een node (een specifieke `regel`-tekst, een specifieke `uitzondering`, één `stap` van een procedure, één `facet` van een beginsel). Voorbeeld:

```json
{
  "id": "regel:meldingsplicht-aww",
  "type": "regel",
  "tekst": "Onderworpen entiteiten melden aan de CFI wanneer ze weten, vermoeden of redelijke gronden hebben om te vermoeden dat er sprake is van witwassen of financiering van terrorisme.",
  "source": {"type": "wet", "short": "AWW art. 47 §1"},
  "getriggerd-door": [
    {"target": "regel:waakzaamheidsverplichting-clienten",  "aspect": "AWW art. 33 §1"},
    {"target": "regel:voortdurende-waakzaamheid",            "aspect": "AWW art. 34 §3"},
    {"target": "regel:actualiseringsverplichting",           "aspect": "AWW art. 35 §2"}
  ],
  "uitzondering-op": [],
  "modaliteiten": [
    {
      "naam": "Niet-uitvoering vergt eveneens melding",
      "tekst": "Ook wanneer de cliënt beslist de voorgenomen verrichting niet uit te voeren, blijft de meldingsplicht gelden.",
      "verwijst-naar": [{"target": "regel:tipping-off-verbod", "aspect": "verband met cliëntinformatie"}]
    }
  ]
}
```

NetworkX-laden tilt block-edges automatisch op naar node-niveau voor walks, maar bewaart het block-anker zodat de tutor kan tonen *waar precies* binnen een node de relatie zit.

**Concept-extractor (stap 4) doet de lifting**: leest de chunk-tekst, herkent referenties (`art. 33-35`, `§ 1`, "in de gevallen bedoeld in"), schrijft ze als block-level edges, schoont de prose op tot accountant-taal (principe #9). Een chunk blijft onaangeroerd; de extractie voegt structuur toe.

### Status-flow per node

| Status | Betekenis |
|---|---|
| `seed` | Alleen naam + type + minimale source. Ontstaat als dangling-target van een edge. |
| `partieel` | Basis-velden ingevuld; edges in één richting; nog _TODO-uitwerking. |
| `gevuld` | Volledig uitgewerkt; alle relevante edges geïdentificeerd. |
| `geverifieerd` | Door gebruiker bevestigd. |

### Iteratief werkproces voor concept-extractie

1. **Trigger** — concept-bril of open vraag.
2. **Bronnen-RAG** — query alle bron-collections.
3. **Eerste extractie** — maak node met type dat past, status `partieel` of `gevuld`.
4. **Edge-extractie** — verwijzingen naar nog-niet-bestaande nodes komen als `_dangling: true`-edges; hun targets vormen de seed-queue.
5. **Volgende rondes** — verwerk queue tot leeg of scope-grens.
6. **Schema-feedback** — als nieuw soort kennis niet past, breidt het schema uit. Bestaande records worden zo nodig aangevuld (sparse fields → geen breaking change).

## Gevolgen

- **`tools/extractie/concept_extractor.py`** moet herschreven worden: per node-type eigen prompt-strategie, queue-mechanisme, status-veld inschrijven, geen hardcoded schema.
- **`tools/rag/rag_index.py`** (functie `index_concepts`): per node-type eigen chunking; edges meedragen als metadata zodat retrieval een sub-graph teruggeeft.
- **`tools/lib/`** krijgt een nieuwe module `graph.py` voor NetworkX-laden, walks en dangling-detectie.
- **`tools/lib/cross_refs.py`** (nieuw) — regex-utility die referenties detecteert in tekst (`art. \d+ §\d+`, "in de gevallen bedoeld in", etc.). Gebruikt door de concept-extractor in stap 4 om referenties te lifteren naar block-level edges. **Niet** gebruikt tijdens chunking (chunk-tekst blijft integraal). Heuristiek voor wet-context: zelfde wet als de chunk tenzij expliciet anders aangegeven ("art. 5 BW", "art. 47 AWW"). Twijfelgevallen → `_dangling: true`.
- **Tutor (`tutor/app.py`)** kan een vraag eerst vector-matchen op concepts, dan via NetworkX-walk de buurt ophalen.
- **Bestaande `meldingsplicht-aww.json`** (oud schema) blijft staan tot de rebuild van de RAG-index; wordt dan vervangen door de gemigreerde nodes uit deze beslissing.
- **Schema-evolutie tijdens stress-tests** voegde 9 nieuwe edge-types toe (`vernietigt-deel-van`, `ratio`, `bedreigt`/`bedreigd-door`, `alternatief-voor`, `schakelt-over-naar`, `gemeten-met`/`instrument-van`) en 1 nieuwe source-type (`voorbeeldexamen`). Dit ADR vat ze samen.

## Open vragen

- **Begrip vs Regel-grens** — een artikel met een definitie *is* tegelijk Regel (bron-vermelding) en Begrip (definitie). Pragmatisch: één node, type bepaald door dominante karakter (verbod = Regel; definitie = Begrip).
- **Drempel-granulariteit** — eigen node ondanks single use, of attribuut binnen Regel? Tijdens stress-tests altijd eigen node (om temporal versionering uniform te houden), maar mag pragmatisch case-per-case worden.
- **Skill als apart node-type** — niet stress-getest in dit ADR; eerste poging volgt bij eerstvolgende skill-modellering.
- **Afwegingskader als apart node-type** — niet stress-getest; eerste poging bij CBN-advies-modellering.
