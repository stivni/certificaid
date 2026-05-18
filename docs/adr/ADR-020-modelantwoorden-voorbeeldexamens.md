# ADR-020: Modelantwoorden voor voorbeeldexamenvragen

**Status**: Draft
**Datum**: 2026-05-18

## Context

De concept- en competentie-laag is na schema 1.6 + EXTRACT v4 grotendeels operationeel (~434 records, alle PO 1.x in zicht). De `data/programma/examen_vragen/*.json`-pool bevat ~140 echte voorbeeldexamenvragen (ITAA + BIBF, 2003-2024), op één na zonder ingeschreven modelantwoord (`correct_antwoord`, `antwoord_motivering`, `antwoord_bron` allemaal `null`). ADR-009 §6 voorziet de render-plumbing om die antwoorden in de minicursus te tonen via `examenfocus`-objecten, maar laat open hoe de antwoorden zelf gegenereerd, ge-QA'd en ingeschreven worden.

Een steekproef op PO 1.4 (5 vragen, 18 mei 2026) bracht vier structurele issues aan het licht:

1. **OCR-rommel in vraagteksten** (bv. vr8 2014: tabel-structuur half kapot, weggevallen letters) waardoor antwoord-generatie op gokwerk-interpretaties moet steunen.
2. **Cluster-records met meerdere polen** (bv. `consolidatieverschil.md` heeft positief én negatief) waarvan varianten-specifieke secties (oorzaken, gevolgen, boeking) niet per pool gelabeld zijn — antwoorden op opsomming-vragen worden onbetrouwbaar.
3. **Onvolledige antwoorden zonder vaste checklist**: vr6 ("waar in resultatenrekening?") werd correct maar incompleet beantwoord — methode-conditionaliteit en aard van de post (toewijzing, geen kost/opbrengst) ontbraken omdat geen checklist afdwong dat alle presentatie-aspecten benoemd worden.
4. **Cirkelredeneerige definities**: "positief consolidatieverschil = positief residu" is geen definitie. EXTRACT-output heeft hier geen gate op.

Modelantwoorden zomaar inschrijven zou stagiairs verkeerd opleiden — antwoorden in fiches worden gelezen als waarheid. Dit ADR codificeert de pipeline + QA-loop zodat (a) antwoorden voldoen aan de redeneer- en presentatie-eisen die ITAA verwacht en (b) de oefening zelf de concept-laag versterkt in plaats van haar fouten te propageren.

## Beslissing

### 1. Pipeline is een dubbele feedback-loop

De modelantwoord-pipeline genereert antwoorden **én** signaleert gaps in de concept-laag. Een checklist die niet uit de records gevuld kan worden, is geen falend antwoord — het is een test-resultaat dat een concept-record incomplete of fout is. **Record-gap blokkeert het antwoord, niet andersom.**

Concreet: per voorbeeldexamenvraag draait de pipeline drie passes:
1. **Vraagtype-classificatie + checklist-template** kiezen
2. **Records-only antwoord-poging** (geen externe kennis, geen webfetch)
3. **VERIFY**: claim-per-claim confidence + record-citaat + circular/oorzaken-gates

Falen in pass 2 of 3 → record-gap-rapport, geen `correct_antwoord` schrijven. Falen pas oplossen door record te patchen, dan opnieuw door pipeline. Dit dwingt af dat record-gaps gepatched worden voordat antwoorden de pool ingaan.

### 2. Vraagtype-taxonomie

Acht vraagtypes met elk een vaste checklist van verplichte velden uit records. De checklists zelf leven in [`prompts/modelantwoord-checklists.md`](../../prompts/modelantwoord-checklists.md) (zelfdragend permanent artefact, zoals EXTRACT v4); de taxonomie hier in het ADR.

| Type | Herkenningssignaal | Verplichte velden uit records |
|---|---|---|
| **Definitie** | "Wat is …?", "Definieer …" | lemma, definitie-zin (zonder lemma-hoofdwoord erin), kerneigenschappen, grondslag |
| **Drempel / cijfer** | "Hoeveel …?", "Wat is het maximum …?" | exact cijfer + eenheid, voorwaarde / clausule, grondslag |
| **Opsomming** | "Geef de N …", "Som op …" | exact N items, **per pool gelabeld** als het concept polen heeft (positief/negatief, integraal/evenredig), grondslag per item |
| **Presentatie** | "Waar in …", "Onder welke post …" | post-naam, schemacode-indien-aanwezig, zijde (actief/passief, kost/opbrengst/toewijzing), aard, methode-conditionaliteit, grondslag |
| **Kwalificatie / methodekeuze** | casus + "welke methode", "is X verplicht" | regel uit record, toepassing op cijfers, conclusie + tussenliggende toetsen, grondslag |
| **Berekening** | "Bereken …", tabel invullen | formule, ingevulde tussenstappen, resultaat + eenheid, interpretatie, grondslag |
| **Procedure** | "Hoe ga je te werk …", "Welke stappen …" | genummerde stappen uit competentie-record, grondslag per stap |
| **Casus / combinatie** | open vraag met meerdere deelvragen | combinatie van bovenstaande, expliciete gedeel per sub-vraag |

Subvragen (`subvragen[]` in JSON) krijgen elk een eigen vraagtype-classificatie — een `MC` met deelvragen a/b/c kan een Definitie + Opsomming combineren.

### 3. Wetsversie-policy

**Default**: huidige wettelijke verwijzing (KB WVV 2019, WVV, ITAA-wet, ISA Belgium 2025, ...) — de stagiair leest in 2026 en wordt getest op 2026-wetgeving.

**Uitzondering**: als een voorbeeldvraag uit een ouder examen een regel test die in de huidige wet **niet meer bestaat** of **fundamenteel anders luidt** (anders dan een artikelnummer-wissel), dan:
- Modelantwoord beantwoordt de vraag zoals de huidige wet hem zou stellen
- In `antwoord_motivering` een aparte alinea "Historische context": de regel die toen gold + waarom hij veranderd is + verwijzing naar de oude wetstekst

Een artikelnummer-wissel (oude KB W.Venn. → KB WVV 2019) zonder inhoudelijke wijziging is **geen** uitzondering — gewoon huidige verwijzing gebruiken.

**Concept-records blijven huidige-wet-only.** Historische wetscontext leeft alleen op antwoord-niveau, niet in records, anders verzieken we de tijdloze kennislaag met examen-toevalligheden (analoog aan ADR-009 §examenpatronen-niet-in-concepten).

### 4. Record-gap-flow

Wanneer de checklist van een vraagtype niet uit de records gevuld kan worden, classificeert de pipeline het gap-type:

| Gap-niveau | Voorbeeld | Actie |
|---|---|---|
| **(a) Patch** — kleine toevoeging aan bestaand record | "Aandeel van derden in resultaat" heeft geen vermelde schemacode | record-veld toevoegen, geen schema-wijziging |
| **(b) Uitbreiding** — nieuw veld / nieuwe sectie | cluster-record met polen mist pool-specifieke oorzaken-lijst | record-structuur uitbreiden binnen schema 1.6; mogelijk EXTRACT v4 hierop pingen voor andere records met polen |
| **(c) Nieuw concept** — fenomeen ontbreekt in de laag | vraag test concept dat geen record heeft | EXTRACT v4 draaien voor het nieuwe concept; gap-rapport vermeldt dit als blokkerende afhankelijkheid |

**Geen forceren**: zolang de checklist-fail open staat, blijft `correct_antwoord = null` in de JSON. De render-pipeline (ADR-009 §6) toont dan automatisch geen `> [!success]-`-callout met antwoord — de vraag verschijnt wel, maar zonder spoiler. Studenten krijgen dus nooit een halfaf antwoord; alles-of-niets.

### 5. VERIFY-uitbreidingen

Twee nieuwe gates in [`prompts/concept-verify-v1.md`](../../prompts/concept-verify-v1.md):

**Cluster-met-polen-gate**: records waarvan de body twee tegengestelde varianten beschrijft (positief/negatief, integraal/evenredig, met/zonder ...) moeten varianten-specifieke secties (oorzaken, gevolgen, boeking, valkuilen) per pool labelen. Detectie-heuristiek: als zowel `positief X` als `negatief X` (resp. de andere paren) ≥ 2× voorkomen in de body, **moet** elke sectie die varianten-afhankelijke inhoud heeft een H3/callout-niveau pool-aanduiding krijgen. Failt VERIFY → record-patch verplicht voor het bij modelantwoord-generatie gebruikt mag worden.

**Circular-definition-gate**: de eerste zin van de definitie (regel onder de H1) mag het lemma-hoofdwoord niet bevatten zonder semantische uitleg. Heuristiek:
- Lemma split op leestekens en stopwoorden → hoofdwoord = langste content-woord (bv. "Positief consolidatieverschil" → "consolidatieverschil")
- Komt hoofdwoord voor in de eerste 50 tokens van de definitie? → flag
- Acceptatie alleen als de hoofdwoord-voorkomst gevolgd wordt door een copula + semantisch onafhankelijke beschrijving ("een consolidatieverschil dat ontstaat wanneer ..." is OK; "het positieve consolidatieverschil is een positief residu" is niet OK)

Beide gates draaien onder `tools/extractie/verify_records.py` (bestaande tool, uitbreiden).

### 6. OCR-normalisatie als import-gate

Voor `data/programma/examen_vragen/*.json` bestaat geen import-gate; vraagteksten zijn rechtstreeks uit PDF-OCR overgenomen. Nieuwe regel: een vraag is pas **bruikbaar voor modelantwoord-generatie** nadat ze door `tools/examen/normalize_vraagteksten.py` is gegaan.

Regex-checks (per vraagtekst):
- Trailing/inline ellipsen `…` op verdachte plekken (binnen tabel-rijen, na cijfers)
- Losse tekens / weggevallen letters (een hoofdletter midden in een woord, hetzij weggevallen, hetzij OCR-fout)
- Kapotte tabel-markup (cijfers + percenttekens zonder kolomstructuur, zoals "M 70 % 30 % 60 % 20 % A B C")
- Niet-afgesloten "Antwoord …" prompts midden in vraagtekst

Flag-tabel in `data/extractie/vraagtekst_qa.json`. Vragen met flags → handmatige review-pass + correctie in source JSON (originele OCR blijft in `vraagtekst_raw`, gecorrigeerde tekst in `vraagtekst`). Niet-gevalideerde vragen worden **niet** door de modelantwoord-pipeline opgepakt.

### 7. Confidence-discipline per claim

Per `antwoord_motivering` is elke inhoudelijke claim gelabeld:

- **⚖️** = direct uit een concept-record + grondslag traceerbaar
- **🤖** = afgeleid (samenstelling, herformulering, kwalificatie van casus-cijfers)

Aggregaat-`confidence` op vraagniveau:
- Alle claims ⚖️ + geen casus-interpretatie → `grounded`
- Mix of casus-interpretatie → `inferred`

`antwoord_bron` is een list van citaten:
```json
"antwoord_bron": [
  {"record": "content/concepten/minderheidsbelangen.md", "sectie": "Berekening", "ondersteunt": "claim-1"},
  {"record": "content/concepten/integrale-consolidatie.md", "sectie": "In de praktijk", "ondersteunt": "claim-3"}
]
```

`antwoord_provenance` is metadata:
```json
"antwoord_provenance": {
  "generator": "claude-opus-4-7",
  "datum": "2026-05-18",
  "vraagtype": "presentatie",
  "checklist_versie": "1.0",
  "verify_passed": true,
  "policy_versie_wet": "huidig"
}
```

### 8. Schema-uitbreiding `data/programma/examen_vragen/<jaar>.json`

Bestaande velden (`correct_antwoord`, `antwoord_motivering`, `antwoord_bron`, `antwoord_provenance`) blijven. Toegevoegd:

| Veld | Type | Verplicht | Doel |
|---|---|---|---|
| `vraagtekst_raw` | string | nee | originele OCR vóór normalisatie |
| `vraagtekst_normalized_at` | ISO-datum | bij gecorrigeerde vraag | wanneer OCR-correctie is gebeurd |
| `antwoord_type` | enum (zie §2) | bij gegenereerd antwoord | classificatie die de pipeline gebruikte. Bestaande veld `vraagtype` blijft = vraagformaat (`MC`/`open`/`jf`) — geen rename om backward-compat te bewaren. |
| `antwoord_confidence` | `grounded` / `inferred` | bij gegenereerd antwoord | aggregaat over claims |
| `record_gap_report` | object of null | bij blokkerend gap | wat ontbreekt + gap-niveau (a/b/c) |

Op `subvragen[]`-niveau dezelfde velden, zodat een combinatie-vraag per deelvraag een eigen status kan hebben.

### 9. Werkverdeling Opus ↔ Sonnet

| Stap | Wie | Reden |
|---|---|---|
| OCR-normalisatie-pass (`normalize_vraagteksten.py`) | Sonnet | deterministisch werk, regex + visuele review |
| Vraagtype-classificatie + checklist-vulling | **Opus** | redeneerwerk per vraag, kalibratie op ITAA-stijl |
| Antwoord-generatie + claim-labeling | **Opus** | core design-werk, niet delegeerbaar zonder kwaliteitsverlies |
| VERIFY-passes (cluster-met-polen, circular, claim-coverage) | Sonnet | regelgebaseerd, schaalbaar |
| Record-patch wanneer gap niveau (a) | Sonnet | mechanische velduitbreiding binnen schema |
| Record-uitbreiding wanneer gap niveau (b) | **Opus** | schema-impact, design-keuze |
| Nieuw concept wanneer gap niveau (c) | EXTRACT v4 (Opus-subagent) | bestaande pipeline |

Sonnet werkt binnen de spelregels van dit ADR. Onduidelijkheid (bv. een vraag die in geen enkel type past) → ping Opus, geen ad-hoc beslissing.

## Werkwijze (één vraag van inkomend → ingeschreven)

```
[ 1 ]  OCR-normalisatie-pass             →  vraagtekst.normalized
       (Sonnet, automatisch + flag-review)
                  │
                  ▼
[ 2 ]  Vraagtype-classificatie           →  vraagtype enum
       (Opus, ook deelvragen)
                  │
                  ▼
[ 3 ]  Records-only antwoord-poging      →  draft antwoord_motivering + claims
       (Opus, geen externe kennis)             + voorlopige antwoord_bron
                  │
                  ▼
[ 4 ]  Checklist-fill                    →  alle velden uit §2 ingevuld? 
       (Opus, eigen QA)                        ja → door · nee → §5
                  │
                  ▼
[ 5 ]  Record-gap detectie?              →  ja → record_gap_report, STOP
                                                 (antwoord niet inschrijven)
                                              nee → door
                  │
                  ▼
[ 6 ]  VERIFY-passes                     →  alle gates pass? 
       (Sonnet automatisch)                     ja → door · nee → §5 of §7
                  │
                  ▼
[ 7 ]  Wetsversie-policy toetsen         →  historische clausule nodig?
       (Opus)                                  zo ja: opname in motivering
                  │
                  ▼
[ 8 ]  Inschrijven in JSON               →  velden uit §8 vullen,
       (Sonnet, deterministisch)               git commit met ADR-020-tag
                  │
                  ▼
[ 9 ]  Render-validatie                  →  ADR-009 §6-render werkt
       (build + visuele inspectie)             zonder fouten
```

## Pilot

PO 1.4 (8 vragen) als pilot **na** ADR-acceptatie. Doel:
- Modelantwoord-checklists v1.0 valideren op echte vragen
- Aantal record-gaps tellen (verwachting: 2-5)
- Tijdsmeting per vraag (verwachting: 10-15 min Opus + 5 min Sonnet-VERIFY)

Bij succes pilot: doorgaan met PO 1.1-1.3, dan 1.5-1.9. Geen modelantwoord-werk op PO 2.x of 3.x tot de concept-laag daar af is.

## Wat NIET in dit ADR

- **Synthetische voorbeeldvragen** (`voorbeeldvraag--*.json`) en hun AI-oplossingen blijven onder ADR-009 §7. Dit ADR gaat alleen over **echte ITAA/BIBF-vragen** in `data/programma/examen_vragen/*.json`.
- **Render-plumbing** (hoe een ingeschreven antwoord in de minicursus verschijnt) blijft onder ADR-009 §6 + ADR-010.
- **Concept-extractie zelf** blijft onder ADR-008 / EXTRACT v4. Dit ADR levert *triggers* aan extractie (gap-niveau b/c) maar verandert de extractie-pipeline niet.
- **Specifieke checklists per vraagtype** leven in [`prompts/modelantwoord-checklists.md`](../../prompts/modelantwoord-checklists.md) (geschreven na ADR-acceptatie). Wijzigingen aan de checklists krijgen een changelog-entry daar, niet een nieuw ADR — tenzij de taxonomie zelf wijzigt.

## Gevolgen

**Nieuwe artefacten**:
- [`prompts/modelantwoord-checklists.md`](../../prompts/modelantwoord-checklists.md) — checklist per vraagtype
- `tools/examen/normalize_vraagteksten.py` — OCR-gate
- `tools/examen/generate_modelantwoord.py` — Opus-subagent runner (analoog aan `propose_competenties.py`)
- `tools/extractie/verify_records.py` uitbreiding — cluster-met-polen + circular-check gates
- `data/extractie/vraagtekst_qa.json` — OCR-flag-rapport

**Bestaande artefacten gewijzigd**:
- `data/programma/examen_vragen/*.json` — schema uitgebreid (§8); migratie alleen on-write per vraag (geen massale backfill)
- `prompts/concept-verify-v1.md` — twee nieuwe gates toegevoegd

**Eerste downstream-impact**:
- Bij pilot PO 1.4: minimaal 1 record-patch verwacht (`consolidatieverschil.md` oorzaken-sectie pool-splitting, gevonden in steekproef 18 mei 2026)
- Minicursus PO 1.4 krijgt voor het eerst **uitgewerkte modelantwoorden onder de Examenfocus-rubriek** — pedagogisch sprong voorwaarts t.o.v. de andere PO's

**Niet-gewijzigd**:
- 802 tests blijven groen (alleen nieuwe tests toegevoegd voor VERIFY-gates + OCR-normalisatie)
- Render-pipeline (Quartz) ongewijzigd
- ITAA-LEX, Cijferzakboekje, bronnen-pipeline ongewijzigd

**Risico's**:
- *Checklist te strikt* → te veel record-gaps, pilot stokt. Mitigatie: na pilot PO 1.4 checklist v1.1 herzien op basis van wat te streng of te los bleek.
- *Wetsversie-grijszone* → onduidelijk wanneer "fundamenteel anders" telt. Mitigatie: één of twee precedenten in PO 1.4-pilot ophelderen → opname in `prompts/modelantwoord-checklists.md` als beslis-vuistregel.
- *OCR-correcties niet perfect* → modelantwoord op verkeerde interpretatie. Mitigatie: bij twijfel op vraagtekst geen modelantwoord schrijven → `record_gap_report.type = "vraagtekst_onduidelijk"`.
