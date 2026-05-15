# Prompt: Per-anker concept-extractie — Fase C (v2)

**Doel**: Extraheer uit een bundel bronchunks alle concepten die voor één ITAA-anker relevant zijn — inclusief begrippen die in de bundle wel impliciet aanwezig zijn maar geen eigen anker hebben. Output volgt ADR-007 schema v1.2.

**Model**: claude-opus-4-7 (subagent — zie ADR-008 §2; geen externe API).

**Verschil met v1**:
- Cross-bron-synthese expliciet aangemoedigd (enumeraties uit verspreide chunks aggregeren).
- Liberaal nieuwe concepten aanmaken — geen 1-op-1 anker-mapping.
- Vijf nieuwe schema-velden voor patronen die examens vragen.
- Bron-aanbevelingen output naar aparte queue.
- Dangling-references loggen voor must-have-detectie.

---

## Context

Je krijgt een bundle-JSON met:
- **`anchor`**: het ITAA-anker (tekst, verbose, synoniemen).
- **`bundle`**: een lijst bronchunks (wetteksten, ITAA-normen, CBN-adviezen) gesorteerd op cosine-similariteit met de anker-tekst.

## Taak

Extraheer **alle** concepten die uit de bundle af te leiden zijn. Niet 1 concept per anker — wat **er staat** is wat je extraheert:

1. **Hoofdconcepten** die direct overeenkomen met het anker — gewoonlijk 1-3 records.
2. **Sub-concepten** die in chunks voorkomen als afzonderlijke fenomenen zonder eigen anker — voorbeelden: "controlepercentage", "invloed van betekenis", "geassocieerde onderneming" worden in chunks gebruikt om hoofdconcepten te definiëren. Maak daar **een eigen record voor** zodra je ze in 2+ chunks van 2+ bronnen tegenkomt.
3. **Casus-records** als chunks expliciete voorbeelden bevatten (CBN-adviezen, ITAA-tuchtdossiers).

**Anti-twijfel-regel**: bij twijfel "is dit een eigen record of een sub-aspect" → kies "eigen record". Liever 30% meer concepten dan een gap. Records kunnen later samengevoegd worden via een dedup-pass; missende records zijn moeilijker te detecteren.

Een concept = een **tijdloos studieonderwerp** (een fenomeen, een beginsel, een procedure, een afwegingskader) — niet een wetsartikel en niet een vakindeling. Examen-specifieke gewichten of vraagvormen horen NIET in concept-records (zie ADR-009 `examenfocus` voor die brug-objecten).

## Cross-bron synthese — verplicht

Het examen toetst herhaaldelijk kennis die over **meerdere bronnen verspreid** is. Concrete instructie:

- **Voor elke claim**: scan alle bundle-chunks. Als hetzelfde fenomeen in 2+ chunks uit verschillende bronnen wordt aangehaald, **aggregeer** tot één expliciete enumeratie / lijst / vergelijking.
- **Voor enumeraties**: als je "vier voornaamste oorzaken" / "drie voorwaarden" patronen ziet, ook al noemt geen enkele chunk er alle vier expliciet — combineer over chunks heen.
- **Confidence**: gebruik `"inferred-from-aggregation"` voor synthese-claims die uit combinatie van bronnen voortkomen (geen enkele bron noemt alle items). Anders `"grounded"` of `"inferred"` zoals v1.
- **Provenance**: lijst **alle** chunk-id's die bijdragen — niet alleen de meest dominante. Dit maakt traceerbaar dat het een synthese is.

Dit is een **abstracte instructie** — niet bron-specifiek. Voor elke materie waar de bundle uitwaaiert over CBN+wetteksten+normen, doe de synthese.

## Recursive deepening — verplicht

Na het opstellen van een concept-record (vooral hoofdconcepten):

1. **Identificeer** de begrippen die in `definitie.text` of `main_rule.text` zijn ingebakken (bv. "boekwaarde", "fractie eigen vermogen", "moedervennootschap-dochter-relatie", "werkelijke waarde").
2. **Check**: heeft elk van deze begrippen al een eigen record in deze of een eerder verwerkte anker-bundle?
3. **Zo nee én** het begrip wordt in 2+ chunks van de huidige bundle gebruikt: **maak een eigen record aan** (mechanisme #2 in ADR-008 fase C). De anti-twijfel-regel hierboven geldt.
4. **Zo nee én** het begrip wordt slechts éénmalig genoemd: **log als dangling-reference** in de output (zie "Dangling-references-output" hieronder).

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
  "_provenance": {
    "extractor_run": "concept-extractie-v2-<ISO-8601-UTC>",
    "model": "claude-opus-4-7",
    "anchor_id": "<primair anker dat deze extractie triggerde>",
    "dekt_ook_anchors": ["<andere anchor_ids als dit concept ook hen dekt>"],
    "reviewed_by": null
  }
}
```

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

### Nieuwe optionele velden (v1.2)

Voeg toe waar de bundle ze ondersteunt. Niet alle records hebben alle velden — sparse fields zijn de norm.

**Reeds bestaande v1-velden die blijven** (geen wijziging — gebruik ze waar passend):
- `voorwaarden[]`, `uitzonderingen[]`, `valkuilen[]`, `voorbeeld_inline`, `bouwstenen[]`, `stappen[]`, `voorwaarden_toepassing[]`. Block-shape zoals in v1.
- **Stappen[]-shape uitgebreid**: optioneel `actor`-veld per stap (voor procedure-rol-bevoegdheid-vragen — "wie doet wat").

**Zes nieuwe optionele velden in v1.2:**

#### `oorzaken[]`

Voor patronen "geef N voornaamste oorzaken van X". Aggregeer over alle bundle-chunks. Cross-bron synthese verplicht: als geen enkele chunk er N opsomt maar verschillende bronnen elk 1-2 oorzaken noemen, **combineer**. Items met `confidence: "inferred-from-aggregation"` mits provenance naar alle bron-chunks.

```json
"oorzaken": [
  {
    "text": "Overpaid goodwill — moedermaatschappij betaalt premie boven net asset value",
    "confidence": "grounded",
    "source": {...},
    "_provenance": {"inputs": [...]}
  },
  {
    "text": "Niet-erkenbare immateriële activa onder BE-GAAP (klantenrelaties, merken)",
    "confidence": "inferred-from-aggregation",
    "source": {...},
    "_provenance": {"inputs": [...]}
  }
]
```

#### `drempelwaarden[]`

Voor elke kritische numerieke grens met juridisch gevolg:

```json
"drempelwaarden": [
  {
    "naam": "Alarmbel-drempel netto-actief",
    "waarde": "minder dan helft gestort kapitaal",
    "eenheid": "EUR (relatief)",
    "gevolg": "bestuursorgaan moet AV bijeenroepen binnen 2 maanden",
    "source": {"type": "wet", "short": "WVV art. 7:228"},
    "confidence": "grounded",
    "_provenance": {"inputs": [...]}
  }
]
```

#### `tijdlijn[]`

Voor procedurele records met wettelijke termijnen:

```json
"tijdlijn": [
  {
    "stap": "vaststelling negatief netto-actief",
    "termijn": "2 maanden",
    "actor": "bestuursorgaan",
    "actie": "bijeenroeping algemene vergadering",
    "source": {...},
    "_provenance": {"inputs": [...]}
  }
]
```

#### `valkuilen[]` (bestaand veld, uitgebreide instructie)

V1 had al `valkuilen[]`. In v2 wordt dit veld actief gevuld met vereisten die in de wet niet expliciet als "vereiste" worden gelabeld maar uit praktijk/jurisprudentie/normen blijken essentieel — wat een ervaren beoefenaar weet bovenop de letterlijke regel.

```json
"valkuilen": [
  {
    "text": "De accountant verstuurt de bevestigingsbrief zelf naar de derde; niet via de klant.",
    "ratio": "Anders is er risico op manipulatie van het antwoord — fundamenteel auditrisico.",
    "source": {"type": "itaa-norm", "short": "Algemene controlenorm §..."},
    "confidence": "grounded",
    "_provenance": {"inputs": [...]}
  }
]
```

#### `vergelijkingsparen[]`

Voor concepten die met andere concepten verward worden — bekende schijngelijkenissen. Reële kennis (verschil tussen A en B is leerlinghulp).

```json
"vergelijkingsparen": [
  {
    "vergelijking_met": "integrale-consolidatie",
    "verschil": "Vermogensmutatiemethode behoudt de deelneming als één post in financiële vaste activa; integrale consolidatie regel-voor-regel-opname van activa/passiva van de dochter.",
    "trigger": "Wanneer de moeder controle heeft (>50%) → integraal. Bij invloed van betekenis (20-50%) → vermogensmutatie.",
    "_provenance": {"inputs": [...]}
  }
]
```

#### `berekeningsmethode[]`

Voor rekenkundige aspecten — een herhaalbaar mentaal recept (geen one-off voorbeeld). Voor concepten waar berekening relevant is (afschrijvingen, consolidatieverschillen, fiscale herzieningen, BTW-roosters, ...).

```json
"berekeningsmethode": [
  {
    "naam": "Lineaire afschrijving",
    "formule": "Jaarbedrag = (Aanschaffingswaarde − Restwaarde) / Levensduur",
    "ratio": "Geschikt wanneer gebruik gelijkmatig is over levensduur.",
    "stappen": [
      {"volgorde": 1, "text": "Bepaal aanschaffingswaarde (incl. bijkomende kosten)"},
      {"volgorde": 2, "text": "Bepaal restwaarde (vaak 0)"},
      {"volgorde": 3, "text": "Bepaal economische levensduur in jaren"},
      {"volgorde": 4, "text": "Pas formule toe — gelijk bedrag per jaar"}
    ],
    "concreet_voorbeeld": {
      "scenario": "Machine 100.000 EUR, restwaarde 10.000, levensduur 10 jaar",
      "berekening": "(100.000 − 10.000) / 10 = 9.000 EUR/jaar",
      "resultaat": "9.000 EUR afschrijving per jaar gedurende 10 jaar"
    },
    "source": {"type": "kb", "short": "KB WVV art. 3:42"},
    "confidence": "grounded",
    "_provenance": {"inputs": [...]}
  }
]
```

Een record kan meerdere methoden hebben (bv. lineair + degressief + prestatiegebonden afschrijving) — array.

#### `in_praktijk[]`

**Doel**: maak abstracte begrippen of regels concreet. Eén veld dat twee soorten "wat betekent dit in de praktijk" dekt:
- Voor **`begrip` / `actor` / `fenomeen`-records**: praktische kenmerken, herkenningspunten, voorbeelden uit de wereld. Bv. wat is een "coöperatief karakter" concreet? Wisselende leden, stemrecht per persoon, ...
- Voor **`regel` / `procedure` / `methode`-records**: concrete handelingen, output/deliverable, triggers die alarmeren. Bv. wat doet de accountant bij alarmbel? Stelt netto-actief vast, roept AV bijeen, ...

Zelfde block-shape voor beide gebruiken:

```json
"in_praktijk": [
  {
    "aspect": "Wisselende ledenstructuur",
    "betekenis": "Leden van de coöperatie kunnen in- en uittreden zonder dat de vennootschap ontbonden of de statuten gewijzigd moeten worden.",
    "herkenningspunt": "Statuten met 'open' lidmaatschap-clausule; soms een minimum kapitaaldeelname",
    "wereld_voorbeeld": "Cera (oorspronkelijk Boerenbond) — duizenden vennoten, vrij in/uit",
    "source": {"type": "wet", "short": "WVV art. 6:1"},
    "confidence": "grounded",
    "_provenance": {"inputs": [...]}
  },
  {
    "aspect": "Bijeenroeping algemene vergadering",
    "betekenis": "Het bestuursorgaan organiseert een AV binnen 2 maanden na vaststelling van negatief netto-actief, met een verslag dat de oorzaken én voorgestelde maatregelen behandelt.",
    "herkenningspunt": "Interim-balans met netto-actief < 50% van gestort kapitaal",
    "source": {"type": "wet", "short": "WVV art. 7:228 §2"},
    "confidence": "grounded",
    "_provenance": {"inputs": [...]}
  }
]
```

**Velden**:
- `aspect` — het label dat de student onthoudt (verplicht)
- `betekenis` — concrete beschrijving (verplicht)
- `herkenningspunt` — signaal of indicator dat dit speelt (optioneel)
- `wereld_voorbeeld` — concrete entiteit/voorbeeld uit de praktijk (optioneel)
- `source` + `confidence` + `_provenance` — zoals elk block

**Niet** alle records hebben dit veld. Voor begrippen die louter formeel zijn (bv. een wetshistorische verwijzing) kan het ontbreken.

### Block-object (elk hoofdveld + items)

Zoals in v1: `text` + `confidence` + `source` + `references` + `_provenance.inputs`. De nieuwe velden hierboven gebruiken dezelfde block-shape (of arrays daarvan).

## Anti-hallucinatie-regels

Strikter dan v1:

1. **Elke claim verplicht `_provenance.inputs`** met chunk_id(s).
2. **Geen wetsartikelnummers verzinnen.** Niet letterlijk in chunks → niet schrijven.
3. **Confidence-types**:
   - `"grounded"` — direct traceerbaar naar één chunk
   - `"inferred-from-aggregation"` — synthese over 2+ chunks (cross-bron) of recursive deepening
   - `"inferred"` — redenering buiten chunk-inhoud (gebruik spaarzaam, geef ratio)
4. **Lift-rule**: artikelnummers, normpunten en verwijzingen horen in `references[]` of `source.short`, niet als inline tekst.
5. **`status: "seed"`** altijd — verfijning komt in latere passes.

## Output-instructies

### Concept-records

Schrijf naar `/Users/stivni/Documents/ITAA/certificaid/data/concept_records/<po>/<concept-slug>.json`.

Maak de directory aan als die niet bestaat.

### Dangling-references-output

Voor begrippen die je in chunks tegenkomt maar voor wie je géén record maakt (te eenmalig, of buiten scope), schrijf één aggregaat-bestand:

`/Users/stivni/Documents/ITAA/certificaid/data/quality_checks/<po>/dangling-references-<run_id>.json`:

```json
{
  "po": "1.4",
  "run_id": "concept-extractie-v2-2026-05-...",
  "items": [
    {
      "term": "controlepercentage",
      "voorkomens": [
        {"chunk_id": "...", "context": "...wordt het controlepercentage berekend op basis van..."}
      ],
      "agent_oordeel": "voldoende-vermeld-geen-record-gemaakt | bewust-uit-scope | onzeker",
      "suggestie": "begrip-record nodig bij volgende pass"
    }
  ]
}
```

### Bron-voorstellen-output

Als je tegen een **kennisgat** aanloopt waar de huidige corpus structureel tekortschiet (bv. examen toetst "COSO 17 principes" maar onze corpus heeft alleen IBR-aanbevelingen), voeg een entry toe aan:

`/Users/stivni/Documents/ITAA/certificaid/data/extractie/_bron_voorstellen.json` (append, niet overschrijven):

```json
{
  "voorstellen": [
    {
      "po": "1.7",
      "anchor_id": "1.7.XII.D",
      "ontbrekende_kennis": "Volledige 5-componenten COSO-framework + 17 onderliggende principes",
      "voorgestelde_bronnen": [
        {
          "naam": "COSO Internal Control – Integrated Framework 2013",
          "url": "https://www.coso.org/Pages/ic.aspx",
          "publiek": true,
          "license": "publieke samenvatting + betaalde detail",
          "redenering": "Onze corpus mist de gestructureerde 5-component-laag; CBN en IBR refereren ernaar maar lijsten ze niet zelf op."
        }
      ],
      "geconstateerd_door": "<run_id>",
      "geconstateerd_op": "<ISO-datum>",
      "human_decision": null
    }
  ]
}
```

### Afsluitend rapport

Markdown-bestand `/Users/stivni/Documents/ITAA/certificaid/data/extractie/<po>/v2-extraction-rapport.md` met:

- Aantal concept-records (incl. delta vs v1)
- Aantal dangling-references gelogd
- Aantal bron-voorstellen gegenereerd
- Cross-bron synthese-statistiek: hoeveel claims `inferred-from-aggregation`?
- Schema-veld-gebruik: aantal records per nieuw v1.2-veld
- Open observaties

## Belangrijke beperkingen

- **NIET edges produceren** — apart pass na alle records.
- **NIET examen-vragen of patronen raadplegen** tijdens extractie (conceptlaag = tijdloos).
- **NIET de bundle-JSONs aanpassen**.
- **Werk in het Nederlands** voor records-inhoud + rapport.

## Iteratie-status

Schema bumpt van 1.1 → 1.2 (additief). Bestaande v1.1-records blijven geldig — gebruik de nieuwe velden alleen als de bundle ze ondersteunt.
