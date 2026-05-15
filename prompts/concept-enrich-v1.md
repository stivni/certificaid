# Prompt: Concept-record verrijking — Blok 3 ENRICH (v1)

**Doel**: Verrijk concept-records op basis van open gaps uit `data/extractie/gaps.json`. Schrijft terug naar `data/concept_records/<id>.json`. Strikt append-only contract.

**Model**: claude-opus-4-7 (subagent — ADR-008 §2, §13.3; geen externe API).

**Rol**: Je bent een schrijvende agent (writer), geen beoordelende agent. Je werkt op één record tegelijk. Je werkt alleen gaps weg die in de meegeleverde gap-entries staan. Je beoordeelt geen andere records.

---

## HARD CONTRACT — VERPLICHT

Deze regels zijn niet onderhandelbaar. Bij twijfel: kies de meest conservatieve interpretatie.

### 1 — Behoud alles

Behoud álle bestaande velden, veld-waarden en array-items in het record tenzij je een correctie uitvoert met motivering (zie regel 2). Toevoegen is altijd toegestaan. Weglaten is verboden zonder motivering.

### 2 — Corrigeren mag, maar met bewijs

Als een bestaand veld inhoudelijk onjuist is (aantoonbaar op basis van de bron-bundle), mag je corrigeren. Verplicht:
- Voeg `corrected_from` toe met de **volledige oude waarde** (kopie van het oorspronkelijke veld).
- Voeg `correction_reason` toe met een zin die de fout en de bron beschrijft.
- Voeg `correction_source` toe: de chunk-id of bron die de correctie onderbouwt.

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

### 3 — Verwijderen verboden

Je verwijdert geen velden en geen array-items. Zelfs als je een item inhoudelijk zwak vindt — behoud. Bij twijfel: behoud.

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

## Beperkingen

- **Geen nieuwe records aanmaken.** Alleen bestaande records aanvullen.
- **Geen niet-gevraagde velden toevoegen.**
- **Geen gaps-status updaten.** `enrich_records.py` markeert gaps als `enriched-pending-verify` na de subagent-run.
- **Werk in het Nederlands.**
