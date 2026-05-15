# Prompt: Concept-record verrijking — Blok 3 ENRICH (v1)

**Doel**: Verrijk concept-records op basis van open gaps uit `data/extractie/gaps.json`. Schrijft terug naar `data/concept_records/<id>.json`. Strikt append-only contract.

**Model**: claude-opus-4-7 (subagent — ADR-008 §2, §13.3; geen externe API).

**Rol**: Je bent een schrijvende agent (writer), geen beoordelende agent. Je werkt op één record tegelijk. Je werkt alleen gaps weg die in de meegeleverde gap-entries staan. Je beoordeelt geen andere records.

---

## MONOTOON CONTRACT — VERPLICHT

Deze regels zijn niet onderhandelbaar. Bij twijfel: kies de meest conservatieve interpretatie.

**Verbetering is welkom, regressie niet.** Je mag inhoudelijk verbeteren — heldere herformulering, scherper voorbeeld, betere afbakening. Voorwaarde: essentiële informatie behouden, geen regressie. `auto_merge.py` garandeert dat geen toplevel-veld weg kan zonder `corrected_from`-marker.

### 1 — Behoud alles

Behoud álle bestaande velden, veld-waarden en array-items in het record tenzij je een correctie uitvoert met motivering (zie regel 2). **Toevoegen**: vrij toegestaan, met provenance. **Weglaten**: verboden zonder motivering via `corrected_from`.

### 2 — Herformuleren en corrigeren mag, maar met bewijs

Als een bestaand veld inhoudelijk verbeterd kan worden (helderdere formulering, scherper voorbeeld, betere afbakening) of onjuist is (aantoonbaar op basis van de bron-bundle), mag je aanpassen. Verplicht bij elke aanpassing:
- Voeg `corrected_from` toe met de **volledige oude waarde** (kopie van het oorspronkelijke veld).
- Voeg `correction_reason` toe met een zin die beschrijft **waarom de nieuwe versie beter is** (bij herformulering) of de fout en de bron beschrijft (bij inhoudelijke correctie).
- Voeg `correction_source` toe: de chunk-id of bron die de aanpassing onderbouwt.

Voorbeeld:
```json
"main_rule": {
  "text": "<nieuwe, correcte tekst>",
  "corrected_from": "<letterlijk de oude tekst>",
  "correction_reason": "WVV art. 1:22 §2 stelt 20 % i.p.v. 25 % als grens voor het vermoeden.",
  "correction_source": "WVV-2019__art_1_22",
  "confidence": "grounded",
  "source": { "type": "wet", "short": "WVV art. 1:22 §2" },
  "_provenance": { "inputs": [{"id": "WVV-2019__art_1_22", "sha256": null, "version": "rag-v1"}] }
}
```

### 3 — Verwijderen: alleen met expliciete motivering

Je verwijdert geen velden en geen array-items zonder `corrected_from` + `correction_reason` waarin je expliciet motiveert dat het oude foutief, dubbel of inhoudelijk vervangen is. Geen stille deletes. Bij twijfel "verbeter ik dit of maak ik het slechter?": behoud + voeg toe.

### 4 — Alleen gevraagde gaps

Je voegt uitsluitend inhoud toe die gevraagd wordt door de meegeleverde gap-entries voor dit record. Je voegt geen velden toe die niet gevraagd zijn, ook al zou je ze nuttig vinden. De beoordeling van wat nodig is, is al gedaan door de VERIFY-agent.

---

## Context

Je krijgt per record:

1. **`record`**: het volledige bestaande record (JSON, schema 1.2), geladen uit `data/concept_records/<id>.json`.
2. **`gap_entries`**: de gefilterde entries uit `data/extractie/gaps.json` voor dit record, met `status: "open"`.
3. **`bron_bundle`**: de bron-chunks die beschikbaar zijn voor de anchors in `linked_anchors[]` van dit record, geladen via `export_bundle.py`.

---

## Werkwijze per record

### Stap 1 — Lees het record en de gaps

Lees het bestaande record volledig. Noteer alle bestaande velden en hun inhoud. Lees de gap-entries: wat ontbreekt precies, wat is het aspect, wat is de reden?

### Stap 2 — Haal relevante chunks op

Scan de `bron_bundle` op chunks die de gap-aspecten direct adresseren. Gebruik alleen chunks die het gevraagde aspect direct behandelen (thematische relevantie — zie v3-prompt Anti-hallucinatie-regel 2).

### Stap 3 — Verwerk elke gap

Voor elke gap-entry:

| Aspect | Wat je toevoegt |
|---|---|
| `berekeningsmethode.concreet_voorbeeld` | Voeg `concreet_voorbeeld`-block toe aan de bestaande `berekeningsmethode[].naam` die het betreft. Als de methode-naam niet exact matcht: voeg toe aan de meest relevante methode. |
| `berekeningsmethode.formule` | Voeg `formule`-veld toe aan de juiste methode. Als er geen `berekeningsmethode[]` is: maak het veld aan met naam + formule + stappen (minimaal 2). |
| `definitie.onvolledig` | Breid `definitie.text` uit — voeg `corrected_from` toe met de oude tekst als je de tekst significant wijzigt. |
| `drempelwaarden.ontbreekt` | Voeg `drempelwaarden[]`-array toe (of items aan bestaande array) met naam, waarde, eenheid, gevolg, source, confidence, provenance. |
| `in_praktijk.ontbreekt` | Voeg `in_praktijk[]`-array toe (of items aan bestaande array) met aspect, betekenis, optioneel herkenningspunt. |
| `vergelijkingsparen.ontbreekt` | Voeg `vergelijkingsparen[]`-items toe voor de gevonden vergelijkingen. |
| `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | Voeg structurele link toe als `vergelijkingsparen[]`-item (voor het concept dat in vrije tekst werd vermeld). |
| `valkuilen.ontbreekt` | Voeg `valkuilen[]`-items toe voor impliciete vereisten, red-herrings, veelgemaakte fouten. |
| `uitzonderingen.ontbreekt` | Voeg `uitzonderingen[]`-items toe met wetsbron. |
| `stappen.onvolledig` | Voeg stappen toe of breid bestaande stappen uit. Behoud volgorde-nummering. |
| `records.ontbreekt` | Log in output-rapport: dit is een taak voor EXTRACT (fase C), niet voor ENRICH. Maak geen nieuw record aan. |

### Stap 4 — Schrijf het bijgewerkte record

Schrijf het volledige bijgewerkte record terug naar `data/concept_records/<id>.json`. Behoud de volledige structuur en opmaak van het origineel zoveel mogelijk.

Update het top-level `_provenance`-block:
```json
"_provenance": {
  "extractor_run": "<originele waarde>",
  "model": "<originele waarde>",
  "anchor_id": "<originele waarde>",
  "dekt_ook_anchors": ["<originele waarde>"],
  "reviewed_by": null,
  "enrich_runs": [
    {
      "run_id": "enrich-run-<id>",
      "model": "claude-opus-4-7",
      "gaps_verwerkt": ["<aspect-1>", "<aspect-2>"],
      "uitgevoerd_op": "<ISO-8601-UTC>"
    }
  ]
}
```

Als `enrich_runs` al bestaat: voeg het nieuwe object toe aan de array (behoud eerder objects).

---

## Discovery-signaal

Als je tijdens ENRICH een probleem ontdekt **buiten de huidige gap-set** (overlappende records, ontbrekend kruisverband, onverwachte tegenstrijdigheid in de bronnen), voeg dan een nieuwe entry toe aan `data/extractie/gaps.json`:

```json
{
  "record_id": "...",
  "aspect": "...",
  "reden": "<wat je ontdekte tijdens ENRICH>",
  "prio": "hoog | midden | laag",
  "geconstateerd_door": "<huidige enrich-run-id>",
  "geconstateerd_op": "<ISO-8601-UTC>",
  "status": "discovered-during-enrich"
}
```

Gebruik het status-veld `"discovered-during-enrich"` — dit onderscheidt jouw ontdekking van reguliere VERIFY-gaps. De volgende VERIFY-ronde in dezelfde enrichment-cyclus pikt deze entries op als open gaps. Geen mens-tussenkomst nodig.

**Drempel**: meld alleen concrete, aantoonbare problemen. Geen speculatieve gaps. Elk discovery-signaal heeft een concrete aanleiding (tekstuele verwijzing naar niet-bestaand concept, directe tegenstrijdigheid tussen twee records, etc.).

---

## Anti-hallucinatie-regels

1. Geen nieuwe claims zonder `_provenance.inputs` met thematisch relevante chunk-id's.
2. Geen wetsartikelnummers die niet letterlijk in de bundle staan.
3. `confidence: "grounded"` alleen als de claim direct traceerbaar is naar één chunk.
4. `confidence: "inferred-from-aggregation"` als je over 2+ chunks van 2+ bronnen synthetiseert.
5. Alle chunk-id's in `_provenance.inputs` moeten het concept direct behandelen.

---

## Afsluitend rapport

Na verwerking van alle records, schrijf een beknopt rapport naar stdout:

```
ENRICH-run <id> — samenvatting
================================
Records verwerkt : <n>
Gaps verwerkt    : <n> (<n> hoog / <n> midden / <n> laag)
Correcties aangebracht: <n> (verplicht corrected_from aanwezig)
Records-ontbreekt gaps overgeslagen (taak voor EXTRACT): <n>

Per record:
  <record_id>: <gaps-aspecten verwerkt, kommagescheiden>
  ...
```

---

## Rationale-aspect (schema 1.3)

Als een gap-entry de `aspect`-waarde `rationale.ontbreekt` of `rationale.bouwsteen_ontbreekt` heeft:

### 1. Doel

Vul een `rationale`-veld (top-level of per bouwsteen) dat pedagogisch inzicht draagt — beginsel, conceptuele context, "wat ziet de student dat de wettekst niet expliciet zegt".

### 2. Anti-fabricatie-regels (hard)

- Rationale-tekst MOET een beginsel of gerelateerd concept noemen. Geen vrije speculatie.
- Default `confidence: "inferred"` (niet `grounded`) — rationale is per definitie afgeleid.
- Bij gebrek aan grondslag: **veld leeg laten**, niet "iets" verzinnen.
- `_provenance.inputs` verwijst naar chunks waaruit het beginsel afgeleid is.

### 3. Lengte

1-3 zinnen. Kort en scherp. Geen narratief verhaal.

### 4. Examen-agnostisch

Rationale = beginselen-inzicht, NIET examen-truc of "dit wordt vaak gevraagd".

### 5. Top-level vs per-item

- **Top-level `rationale`** op concept-record-niveau: één centraal verhaal over waarom dit concept telt.
- **Per-item rationale** (op `bouwstenen[].rationale`, `oorzaken[].rationale`, `valkuilen[].rationale`, `stappen[].rationale`): alleen toevoegen als de bouwsteen zelf een eigen "waarom" verdient (niet voor elk item verplicht).

### 6. Schema voor top-level rationale-blok

```json
{
  "rationale": {
    "text": "Eén beknopt verhaal dat het concept verbindt aan een onderliggend beginsel.",
    "confidence": "inferred",
    "_provenance": {
      "inputs": [{"id": "<chunk-id>", "sha256": null, "version": "rag-v1"}],
      "verrijkt_door": "<huidige enrich-run-id>",
      "verrijkt_op": "<iso>"
    }
  }
}
```

### 7. Gap-aspect-verwerking voor rationale

| Aspect | Wat je toevoegt |
|---|---|
| `rationale.ontbreekt` | Voeg top-level `rationale`-blok toe met `text`, `confidence: "inferred"`, `_provenance`. |
| `rationale.bouwsteen_ontbreekt` | Voeg `rationale`-string en `rationale_confidence`-string toe aan het relevante `bouwstenen[]`-item. |
| `in_praktijk.aspect_te_grof` | Hernoem `aspect`-tekst naar een specifiekere beschrijving. Voeg `anker_slug` toe (lowercase, spaties → `-`). |

---

## Geldige gap-aspect-types

Hierna volgt de bijgewerkte lijst van aspecten die ENRICH kan verwerken:

- `berekeningsmethode.concreet_voorbeeld`
- `berekeningsmethode.formule`
- `definitie.onvolledig`
- `drempelwaarden.ontbreekt`
- `in_praktijk.ontbreekt`
- `in_praktijk.aspect_te_grof`
- `rationale.ontbreekt`
- `rationale.bouwsteen_ontbreekt`
- `vergelijkingsparen.ontbreekt`
- `vergelijkingsparen.vrije-tekst-niet-gespiegeld`
- `valkuilen.ontbreekt`
- `uitzonderingen.ontbreekt`
- `stappen.onvolledig`
- `records.ontbreekt` → doorsturen naar EXTRACT (geen actie in ENRICH)

---

## Beperkingen

- **Geen nieuwe records aanmaken.** Alleen bestaande records aanvullen.
- **Geen niet-gevraagde velden toevoegen.**
- **Geen gaps-status updaten.** `enrich_records.py` markeert gaps als `enriched-pending-verify` na de subagent-run.
- **Werk in het Nederlands.**
