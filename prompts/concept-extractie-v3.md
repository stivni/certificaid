# Prompt: Per-anker concept-extractie — Fase C (v3)

**Doel**: Extraheer uit een bundel bronchunks alle concepten die voor één ITAA-anker relevant zijn. Output volgt ADR-007 schema v1.2. Schrijft naar flat `data/concept_records/<concept-slug>.json` — geen PO-subdirs.

**Model**: claude-opus-4-7 (subagent — zie ADR-008 §2; geen externe API).

**Verschil met v2**:
- Vijf verplichte kwaliteitsregels toegevoegd (§"KWALITEITS-REGELS").
- Records-locatie is flat: `data/concept_records/<id>.json`.
- Elk record krijgt `linked_anchors[]` (lijst van anchor-id's).
- PO-agnostisch: geen PO-1.4-specifieke instructies.
- Bouwstenen van bestaande records moeten expliciet behouden worden bij upgrade.

---

## KWALITEITS-REGELS — VERPLICHT

Deze vijf regels gelden boven alle andere instructies. Bij twijfel: kies de striktere interpretatie.

### Regel 1 — Centraliteit impliceert volledigheid

Hoe vaker een concept door andere records wordt aangeroepen via `vergelijkingsparen[]`, vrije tekst of `edges[]`, hoe completer zijn eigen record moet zijn. Basisconcepten die als vertrekpunt dienen voor meerdere andere fenomenen — de "ankerpunten" van het domein — krijgen méér aandacht, niet minder.

**Controlevraag voor elk record**: is dit concept een vertrekpunt voor andere concepten? Zo ja: vul `definitie`/`main_rule`, `in_praktijk[]`, `drempelwaarden[]` (indien relevant), `vergelijkingsparen[]` en `valkuilen[]` zo volledig mogelijk in.

### Regel 2 — Berekenbaar concept verplicht numeriek voorbeeld

Elk record met minstens één `berekeningsmethode[].formule` of `berekeningsmethode[].stappen[]` krijgt **verplicht** een `berekeningsmethode[].concreet_voorbeeld` met:
- `scenario`: een concrete feitensituatie (getallen, percentages, bedragen)
- `berekening`: de uitgewerkte berekening stap voor stap
- `resultaat`: de einduitkomst in leesbare zin

"Rekenuitwerking elders" of "zie ander record" is niet toegestaan. Het voorbeeld staat in hetzelfde record als de methode.

### Regel 3 — Eén fenomeen, één record

Twee records mogen hetzelfde fenomeen niet overlappend beschrijven. Meerdere perspectieven op hetzelfde fenomeen (bv. balans-kant én resultatenrekening-kant van minderheidsbelangen) passen als aparte velden of array-items binnen één record — niet als twee aparte records die naar hetzelfde wetsartikel verwijzen.

**Test**: als twee records dezelfde primaire bron (`source.short`) hebben en meer dan 60 % van hun inhoud overlapt → samenvoegen. Gebruik een sectie-structuur binnen één record om de twee perspectieven te scheiden.

### Regel 4 — Vrije-tekst-verwijzing = ook structurele verwijzing

Als de tekst van veld X verwijst naar concept B ("zie ook B", "vergelijk met B", "wanneer B van toepassing is"), dan staat B ook als item in `vergelijkingsparen[]` of als edge in `edges[]`. Vrije-tekst-only verwijzingen zijn dood gewicht voor graph-walks en cross-record retrieval.

**Test**: na het schrijven van een record, scan de volledige tekst van alle velden op namen van andere concepten. Elk gevonden concept dat niet als structurele link is vastgelegd → toevoegen aan `vergelijkingsparen[]` of `edges[]`.

### Regel 5 — Uniforme rijkheid binnen node-type

Alle records van hetzelfde `node_type` krijgen vergelijkbare velden-rijkheid. Geen "dit had ik haast" en "dit heb ik diep".

**Minimum per node-type** (cumulatief, alle onderstaande velden verplicht als bundle het ondersteunt):

| node_type | Verplicht naast hoofdveld | Sterk aanbevolen als bundle het toelaat |
|---|---|---|
| `begrip`, `actor`, `fenomeen` | `definitie` | `in_praktijk[]`, `vergelijkingsparen[]`, `valkuilen[]` |
| `regel`, `beginsel` | `main_rule` | `uitzonderingen[]`, `voorwaarden[]`, `vergelijkingsparen[]` |
| `drempel` | `main_rule`, `drempelwaarden[]` | `vergelijkingsparen[]`, `in_praktijk[]` |
| `procedure` | `verplichting`, `stappen[]` (≥2) | `tijdlijn[]`, `valkuilen[]` |
| `methode`, `afwegingskader` | `doel`, `bouwstenen[]` of `berekeningsmethode[]` | `vergelijkingsparen[]`, `concreet_voorbeeld` per methode |
| `casus` | `feiten`, `uitspraak` | — |
| `skill` | `omschrijving` | `subvaardigheden[]` |

---

## Context

Je krijgt een bundle-JSON met:
- **`anchor`**: het ITAA-anker (tekst, verbose, synoniemen, anchor_id, programmaonderdeel).
- **`bundle`**: een lijst bronchunks (wetteksten, ITAA-normen, CBN-adviezen) gesorteerd op cosine-similariteit.
- Optioneel: **`bestaande_records`** — een lijst van bestaande records die linked_anchors hebben die overlappen met dit anker. Behandel deze als context: niet overschrijven, wel aanvullen of verwijzen.

## Taak

Extraheer **alle** concepten die uit de bundle af te leiden zijn. Niet 1 concept per anker:

1. **Hoofdconcepten** die direct overeenkomen met het anker — gewoonlijk 1-3 records.
2. **Sub-concepten** die in chunks voorkomen als afzonderlijke fenomenen zonder eigen anker. Maak een eigen record zodra je ze in 2+ chunks van 2+ bronnen tegenkomt.
3. **Casus-records** als chunks expliciete voorbeelden bevatten (CBN-adviezen, ITAA-tuchtdossiers).

**Anti-twijfel-regel**: bij twijfel "eigen record of sub-aspect" → kies "eigen record". Liever 30 % meer concepten dan een gap. Records kunnen later samengevoegd worden; missende records zijn moeilijker te detecteren.

**Samenvoeg-test (Regel 3)**: controleer voordat je een nieuw record aanmaakt of er al een record bestaat (in `bestaande_records`) dat hetzelfde fenomeen beschrijft vanuit een ander perspectief. Zo ja: voeg toe als sub-veld of array-item — maak geen tweede record.

## Cross-bron synthese — verplicht

Het examen toetst kennis die over meerdere bronnen verspreid is. Instructie:

- Voor elke claim: scan alle bundle-chunks. Als hetzelfde fenomeen in 2+ chunks uit verschillende bronnen wordt aangehaald, **aggregeer** tot één expliciete enumeratie of vergelijking.
- Voor enumeraties: als "vier voornaamste oorzaken" / "drie voorwaarden" patronen herkenbaar zijn, combineer over chunks heen.
- **Confidence**: gebruik `"inferred-from-aggregation"` voor synthese-claims. Alle bijdragende chunk-id's in `_provenance.inputs`.
- **Thematische relevantie-eis**: elk chunk-id in `_provenance.inputs` moet thematisch relevant zijn voor die specifieke claim. Een niche-sectie over een zijdelings onderwerp is geen geldige provenance-bron voor een centrale definitie-claim.

## Recursive deepening — verplicht

Na het opstellen van elk hoofd-record:

1. Identificeer begrippen die in `definitie.text` of `main_rule.text` ingebakken zijn.
2. Check: heeft elk van deze begrippen al een eigen record (in `bestaande_records` of eerder in deze sessie aangemaakt)?
3. Zo nee én het begrip wordt in 2+ chunks van de huidige bundle gebruikt: maak een eigen record aan.
4. Zo nee én het begrip wordt slechts éénmalig genoemd: log als dangling-reference.

## Bestaande records upgraden

Als `bestaande_records` een record bevat voor een concept dat ook in de huidige bundle zit:

- **Behoud álle bestaande velden en items** — ook als ze niet in de huidige bundle worden ondersteund.
- Voeg toe waar de bundle nieuwe inhoud biedt.
- Als een bestaande bouwsteen of item incorrect is: corrigeer met `corrected_from` (oude waarde) + `correction_reason` (1 zin) + bron.
- Schrijf het bijgewerkte record terug naar dezelfde `<id>.json` — geen versie-suffix.

## Schema — ADR-007 v1.2

Elk concept-record is een JSON-bestand. Bestandsnaam: `<concept-slug>.json` (lowercase, koppeltekens, geen spaties).

### Verplichte top-level velden

```json
{
  "id": "<concept-slug>",
  "naam": "<leesbare naam>",
  "node_type": "<zie onderstaande lijst>",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": ["<anchor_id>", "<andere_anchor_id_indien_van_toepassing>"],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-<ISO-8601-UTC>",
    "model": "claude-opus-4-7",
    "anchor_id": "<primair anker dat deze extractie triggerde>",
    "dekt_ook_anchors": ["<andere anchor_ids als dit concept ook hen dekt>"],
    "reviewed_by": null
  }
}
```

**`linked_anchors[]`**: lijst van alle anchor-id's (van eender welk programmaonderdeel) die dit concept raken. Altijd minstens het primaire anker. Meerdere anchors als het concept voor meerdere ankerpunten relevant is.

### Node-types (ADR-007 §"Node-types")

| type | hoofdveld | optioneel |
|---|---|---|
| `begrip`, `actor`, `fenomeen` | `definitie` | — |
| `regel`, `beginsel` | `main_rule` | — |
| `drempel` | `main_rule` | `waarde` |
| `procedure` | `verplichting`, `stappen[]` | — |
| `methode`, `afwegingskader` | `doel` | `bouwstenen[]` |
| `casus` | `feiten`, `uitspraak` | — |
| `skill` | `omschrijving`, `subvaardigheden[]` | — |

Nieuw type nodig? `node_type: "voorgesteld:<naam>"` — wordt verzameld voor review.

### Optionele velden (schema 1.2)

**V1-velden** (blijven onveranderd):
`voorwaarden[]`, `uitzonderingen[]`, `valkuilen[]`, `voorbeeld_inline`, `bouwstenen[]`, `stappen[]`, `voorwaarden_toepassing[]`

**Stappen[]-shape**: optioneel `actor`-veld per stap (voor "wie doet wat"-vragen).

**V1.2 nieuwe velden** (gebruik waar bundle ze ondersteunt):

#### `oorzaken[]`
Voor patronen "N voornaamste oorzaken van X". Aggregeer cross-bron; confidence `"inferred-from-aggregation"` voor synthese-claims.

```json
"oorzaken": [
  {
    "text": "Overpaid goodwill — moeder betaalt premie boven net asset value",
    "confidence": "inferred-from-aggregation",
    "source": { "type": "kb", "short": "KB WVV art. 3:131" },
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

#### `drempelwaarden[]`
Voor kritische numerieke grenzen met juridisch gevolg. Ook voor weerlegbare vermoedens als kwantitatief criterium.

```json
"drempelwaarden": [
  {
    "naam": "Vermoeden invloed van betekenis",
    "waarde": "≥ 20 %",
    "eenheid": "deelnemingspercentage",
    "gevolg": "weerlegbaar vermoeden van invloed van betekenis → vermogensmutatiemethode",
    "source": { "type": "wet", "short": "WVV art. 1:22 §2" },
    "confidence": "grounded",
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

#### `tijdlijn[]`
Voor procedurele records met wettelijke termijnen.

```json
"tijdlijn": [
  {
    "stap": "vaststelling negatief netto-actief",
    "termijn": "2 maanden",
    "actor": "bestuursorgaan",
    "actie": "bijeenroeping algemene vergadering",
    "source": { "type": "wet", "short": "WVV art. 7:228 §2" },
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

#### `vergelijkingsparen[]`
Voor concepten die met andere verward worden. Elk paar vermeldt een record-id (zie Regel 4).

```json
"vergelijkingsparen": [
  {
    "vergelijking_met": "integrale-consolidatie",
    "verschil": "Vermogensmutatiemethode behoudt de deelneming als één post; integrale consolidatie neemt activa/passiva regel voor regel op.",
    "trigger": "Bij controle (>50 %) → integraal. Bij invloed van betekenis (20–50 %) → vermogensmutatie.",
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

#### `berekeningsmethode[]`
Verplicht `concreet_voorbeeld` als de methode numeriek toepasbaar is (Regel 2).

```json
"berekeningsmethode": [
  {
    "naam": "Bepaling aandeel van derden in het resultaat",
    "formule": "(1 − belang%) × resultaat_dochter",
    "ratio": "De moeder consolideert 100 % van de dochter; het deel buiten de groep wordt afgetrokken.",
    "stappen": [
      { "volgorde": 1, "text": "Bepaal het belang van de moeder (%) in de dochter." },
      { "volgorde": 2, "text": "Bereken (1 − belang%) × het volledige resultaat van de dochter." }
    ],
    "concreet_voorbeeld": {
      "scenario": "M bezit 80 % van D; D realiseert een nettowinst van 100.",
      "berekening": "(1 − 0,80) × 100 = 0,20 × 100 = 20",
      "resultaat": "Aandeel van derden in het resultaat: 20 — te presenteren als afzonderlijke post in de geconsolideerde resultatenrekening."
    },
    "source": { "type": "kb", "short": "KB WVV art. 3:137" },
    "confidence": "grounded",
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

#### `in_praktijk[]`
Concretisering van het concept. Voor `begrip`/`actor`/`fenomeen`: herkenningspunten. Voor `regel`/`procedure`/`methode`: concrete handelingen.

```json
"in_praktijk": [
  {
    "aspect": "Herkenning in examensituatie",
    "betekenis": "Bij een tabel met moeder M, dochter A en kleindochter B: controleer altijd eerst of M via A volledige controle heeft — dan geldt het controlepercentage voor B volledig, niet multiplicatief.",
    "herkenningspunt": "Tabelopgaven met 'M x% van A; A y% van B'-structuur",
    "source": { "type": "wet", "short": "WVV art. 1:14 §2" },
    "confidence": "grounded",
    "_provenance": { "inputs": [{"id": "...", "sha256": null, "version": "rag-v1"}] }
  }
]
```

**Velden**: `aspect` + `betekenis` (verplicht), `herkenningspunt` + `wereld_voorbeeld` (optioneel), `source` + `confidence` + `_provenance`.

#### `valkuilen[]`
Actief vullen met impliciete vereisten die de wet niet expliciet labelt maar die in de praktijk essentieel zijn — verborgen vereisten, red-herring-elementen, vaak-foutgedaan-stappen.

### Block-object

Elk hoofdveld en elk array-item heeft: `text` (of `naam`+`betekenis` etc.) + `confidence` + `source` + optioneel `references[]` + `_provenance.inputs`.

## Anti-hallucinatie-regels

1. **Elke claim verplicht `_provenance.inputs`** met chunk_id(s).
2. **Thematische relevantie**: chunk_id's moeten het concept direct behandelen — geen niche-secties die slechts zijdelings raken.
3. **Geen wetsartikelnummers verzinnen.** Niet letterlijk in chunks → niet schrijven.
4. **Confidence-types**:
   - `"grounded"` — direct traceerbaar naar één chunk
   - `"inferred-from-aggregation"` — synthese over 2+ chunks (cross-bron)
   - `"inferred"` — redenering buiten chunk-inhoud (gebruik spaarzaam, geef ratio)
5. **Lift-rule**: artikelnummers en normpunten in prose zijn een smell; zij horen in `references[]` of `source.short`.
6. **`status: "seed"`** altijd op nieuwe records.

## Output-instructies

### Concept-records

Schrijf naar `/Users/stivni/Documents/ITAA/certificaid/data/concept_records/<concept-slug>.json`.

**Geen PO-subdirs.** Bestaande records op dezelfde locatie worden bijgewerkt, niet overschreven.

### Dangling-references-output

Voor begrippen die je ziet maar geen record voor maakt, schrijf naar:
`/Users/stivni/Documents/ITAA/certificaid/data/quality_checks/<po>/dangling-references-<run_id>.json`

```json
{
  "po": "<po-code>",
  "run_id": "concept-extractie-v3-<ISO-datum>",
  "items": [
    {
      "term": "<term>",
      "voorkomens": [
        { "chunk_id": "...", "context": "...de term in context..." }
      ],
      "agent_oordeel": "voldoende-vermeld-geen-record-gemaakt | bewust-uit-scope | onzeker",
      "suggestie": "<optionele aanbeveling>"
    }
  ]
}
```

### Bron-voorstellen-output

Bij structurele kennishiaten, voeg toe aan:
`/Users/stivni/Documents/ITAA/certificaid/data/extractie/_bron_voorstellen.json` (append-only)

```json
{
  "po": "<po-code>",
  "anchor_id": "<anchor_id>",
  "ontbrekende_kennis": "<vrije tekst>",
  "voorgestelde_bronnen": [
    {
      "naam": "<naam>",
      "url": "<url>",
      "publiek": true,
      "license": "<licentie>",
      "redenering": "<waarom>"
    }
  ],
  "geconstateerd_door": "<run_id>",
  "geconstateerd_op": "<ISO-datum>",
  "human_decision": null
}
```

### Afsluitend rapport

`/Users/stivni/Documents/ITAA/certificaid/data/extractie/<po>/v3-extraction-rapport.md` met:
- Aantal concept-records (nieuw / bijgewerkt)
- Aantal dangling-references gelogd
- Aantal bron-voorstellen
- Claims `inferred-from-aggregation`
- Schema-veld-gebruik per v1.2-veld
- Open observaties

## Beperkingen

- **NIET edges produceren** — apart pass na alle records.
- **NIET examen-vragen raadplegen** tijdens extractie (conceptlaag = tijdloos).
- **NIET de bundle-JSONs aanpassen**.
- **Werk in het Nederlands** voor records-inhoud en rapport.
