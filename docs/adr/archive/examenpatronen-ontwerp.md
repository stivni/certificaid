# Examenpatronen — Ontwerp en principes

> ℹ️ **Designdocument** vóór de ADR-herziening op 2026-05-07. De architecturale kern is geabsorbeerd in [ADR-009 Examenpatronen](adr/ADR-009-examenpatronen.md). Dit document blijft staan voor de implementatie-detail (vraagvorm/complexiteitspatroon/examenfocus-schema's, camouflage-taxonomy, generatie-templates) die in de korte ADR niet werd hernomen. Wordt geconsolideerd zodra Fase 3-4 examenpatroon-tooling gebouwd wordt.

## Kernprincipe

Concepten zijn **tijdloze kennislaag** (wetteksten, echte wereld). Examenpatronen zijn een **aparte observatielaag** over hoe ITAA die kennis toetst. De twee mogen niet vermengd worden.

Enige toegelaten brug: **pitfalls** in concept records kunnen gevoed worden door wat examenvragen onthullen over typische denkfouten. Maar een concept record "weet" niets van examens — dat is éénrichtingsverkeer.

---

## Drie aparte objecttypes

### 1. `vraagvorm` — hoe de vraag gesteld wordt (format-agnostisch)

Puur over de **presentatievorm**, los van onderwerp en complexiteit.

```json
{
  "id": "vraagvorm:uitzondering-in-reeks",
  "naam": "Uitzondering in reeks",
  "versie": "20260506.1",
  "beschrijving": "Reeks van 4–6 uitspraken over een regel, waarvan 1–2 fout zijn door een randgeval of uitzondering.",
  "vraagtypen": ["J/F", "MC"],
  "cognitieve_laag": "toepassen",
  "typische_formulering": [
    "Zijn de volgende beweringen juist of fout? Motiveer.",
    "Welke uitspraak is JUIST?"
  ],
  "format_valkuil": "Student past de hoofdregel toe op alle items en herkent het specifieke element niet dat één item naar de uitzondering trekt."
}
```

**Bekende vraagvormen** (te extraheren uit examens):
- `uitzondering-in-reeks`
- `bereken-en-motiveer`
- `grensgeval-herkenning`
- `procedure-stappen`
- `rol-en-bevoegdheid`
- `vergelijk-behandeling`
- `identificeer-de-fout`
- `adviseer-en-onderbouw`

---

### 2. `complexiteitspatroon` — structurele complexiteit van de vereiste kennis

De **moeilijkheidsknoppen** die de examinator instelt. Vier onafhankelijke dimensies:

#### Dimensie 1 — Kennisdiepte

| Waarde | Wat vereist |
|---|---|
| `artikel` | Één regel kennen |
| `uitzondering` | De uitzondering op de regel |
| `uitzondering-op-uitzondering` | Het geval waarbij de uitzondering zelf niet geldt |
| `samenspel` | Meerdere artikelen die elkaar beïnvloeden |

#### Dimensie 2 — Contextspecificiteit

| Waarde | Wat vereist |
|---|---|
| `generiek` | Regel in de algemene situatie |
| `business-context` | Correct toepassen in specifieke sector (horeca, vrij beroep, KMO, ...) |
| `context-uitzondering` | Uitzondering herkennen die alleen in die context geldt |

#### Dimensie 3 — Analytische breedte

| Waarde | Wat vereist |
|---|---|
| `enkelvoudig` | Één berekening of beoordeling |
| `meervoudig-gerelateerd` | Meerdere berekeningen die op elkaar inwerken |
| `meervoudig-ongerelateerd` | Meerdere losstaande vragen in één casus |

#### Dimensie 4 — Camouflage

| Waarde | Wat het vraagt |
|---|---|
| `geen` | Vraag is wat ze lijkt |
| `red-herring` | Irrelevant element aanwezig — student moet het negeren |
| `schijngelijkenis` | Situatie lijkt op X maar is Y — student moet het onderscheid herkennen |
| `verborgen-vereiste` | Voer X uit, maar correct antwoord vereist ook dat je Y signaleert (timing, fout, compliance-issue, ...) |

> **Bewuste keuze**: `timing-trigger` is geen apart type — het is een instantie van `verborgen-vereiste` waarbij Y toevallig een tijdstip-gerelateerde verplichting is. De categorie beschrijft het structurele patroon, niet het soort Y.

> **Cross-domein**: voorlopig buiten de taxonomy — waarschijnlijk niet van toepassing bij ITAA.

**Schema:**
```json
{
  "id": "complexiteit:context-uitzondering-met-verborgen-vereiste",
  "naam": "Contextuitzondering met verborgen vereiste",
  "versie": "20260506.1",
  "dimensies": {
    "kennisdiepte": "context-uitzondering",
    "contextspecificiteit": "business-context",
    "analytische_breedte": "enkelvoudig",
    "camouflage": "verborgen-vereiste"
  },
  "cognitieve_laag": "integratie",
  "signalen_in_vraag": [
    "Casusbeschrijving met sectorspecifiek detail",
    "Extra omstandigheid die een impliciet signaal vereist"
  ],
  "echte_voorbeelden": []
}
```

---

### 3. `examenfocus` — hoe ITAA een specifiek concept toetst

De brug tussen een concept en de vraagvormen/complexiteitspatronen waarmee het getoetst wordt.

```json
{
  "id": "examenfocus:meldingsplicht-aww-toepassen",
  "versie": "20260506.1",
  "concepten": ["concept:meldingsplicht-aww"],
  "niveau": "toepassen",
  "business_context": null,
  "typische_vraagvormen": [
    "vraagvorm:uitzondering-in-reeks",
    "vraagvorm:grensgeval-herkenning"
  ],
  "typische_complexiteit": {
    "kennisdiepte": "uitzondering",
    "contextspecificiteit": "generiek",
    "analytische_breedte": "enkelvoudig",
    "camouflage": "geen"
  },
  "inhoudelijke_valkuilen": [
    "Verwarring tussen vermoeden (voldoende) en zekerheid (niet vereist)",
    "Meldingsplicht niet van toepassing denken bij kleine bedragen"
  ],
  "echte_voorbeelden": [
    {
      "examen": "2013-1",
      "po": "4.0",
      "vraagvorm_id": "vraagvorm:uitzondering-in-reeks",
      "vraag_samenvatting": "5 stellingen over wie meldingsplichtig is en wanneer"
    }
  ]
}
```

---

## Relaties tussen de lagen

```
concept_record          ← tijdloze kennis (wetteksten, echte wereld)
      ↓ éénrichtings (pitfalls kunnen terugvloeien)
examenfocus             ← hoe ITAA dit concept toetst, op welk niveau, in welke context
      ↓ verwijzing
vraagvorm               ← herbruikbaar format-template
complexiteitspatroon    ← structurele complexiteit (onafhankelijk van topic)
      ↓ instantie
generated_question      ← concept × vraagvorm × complexiteitspatroon
```

---

## Bestandsstructuur

```
data/
├── exam_patterns/
│   ├── vraagvorm--uitzondering-in-reeks.json
│   ├── vraagvorm--bereken-en-motiveer.json
│   ├── complexiteit--context-uitzondering-met-verborgen-vereiste.json
│   └── ...
├── exam_focus/
│   ├── examenfocus--meldingsplicht-aww-toepassen.json
│   └── ...
├── voorbeeldvragen-synthetisch/
│   ├── voorbeeldvraag--aww-meldingsplicht-reeks-001.json
│   └── ...
└── concept_records/
    └── (ongewijzigd — geen examenvelden)
```

---

## Versioning

Formaat: `JJJJMMDD.N` (bv. `20260506.1`, `20260506.2`)

- Datum + volgnummer binnen die dag
- Wanneer een patroon een nieuwe versie krijgt → alle synthetische voorbeeldvragen die dat patroon gebruiken krijgen `herzieningsstatus: "stale"`
- Review via `python3 tools/examen/question_review.py --flag --revise`

---

## Bouwvolgorde (besloten)

**A — Analyse eerst, generatie daarna** (bewuste keuze)

```
Stap 1  Concept records bouwen
        Prioriteit: onderwerpen uit de 5 examens
        (deontologie, BTW, VennB, WVV, AWW, alarmbelprocedure, ratio-analyse)

Stap 2  Echte examenvragen oplossen met concept records + RAG
        → welke concepten waren nodig?
        → hoe diep? welke uitzondering?
        → was er iets verborgen?

Stap 3  Complexiteitspatronen + vraagvormen afleiden uit die oplossingen
        → nu weet je wat de examinator werkelijk vroeg

Stap 4  Patronen als generatieve templates voor andere vakken
        → generate_question(concept, vraagvorm, complexiteitspatroon)
```

**Rationale**: door de echte vragen eerst op te lossen via de concepten, zie je precies welke kennisdiepte vereist was. Dat is rijker dan Claude laten raden uit ruwe PDF-tekst.

---

## Generated question schema

```json
{
  "id": "voorbeeldvraag:aww-meldingsplicht-reeks-001",
  "concept_id": "concept:meldingsplicht-aww",
  "po": "4.0",
  "vraagvorm_id": "vraagvorm:uitzondering-in-reeks",
  "vraagvorm_versie": "20260506.1",
  "complexiteit": {
    "kennisdiepte": "uitzondering",
    "contextspecificiteit": "generiek",
    "analytische_breedte": "enkelvoudig",
    "camouflage": "geen"
  },
  "vraagtype": "J/F",
  "cognitieve_laag": "toepassen",
  "vraag": "...",
  "antwoord": "...",
  "gegenereerd_op": "2026-05-06",
  "gegenereerd_door": "claude-sonnet-4-6",
  "status": "actief",
  "herzieningsstatus": null,
  "herzieningsreden": null
}
```

---

## Openstaande beslissingen

- `examenfocus`-records: manueel aanmaken of automatisch extraheren uit opgeloste examenvragen?
- Welke concept records zijn minimaal nodig vóór we de exam solver kunnen draaien?
- Tutor-integratie: bij vraaggeratie zowel `vraagvorm` als `complexiteitspatroon` als parameters aanbieden, of één gecombineerde "moeilijkheidsinstelling"?
