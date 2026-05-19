# ADR-022: Herinterpretatie van herinnering-stijl voorbeeldexamens (DRAFT)

**Status**: Draft
**Datum**: 2026-05-19
**Pilot-scope**: 2024-1 (11 vragen)

## Context

ADR-021 ging er stilzwijgend van uit dat elke `data/programma/examen_vragen/*.json`-file dezelfde aard heeft: een officieel gepubliceerde wedstrijdtekst van ITAA/BIBF, met volledige vraagstellingen, MC-opties, casus-data en (vroeger) puntenverdeling. Voor de bibf-bundels 2003/2008 en voor de ITAA-jaargangen 2013-1, 2013-2, 2014-1 en 2015-1 klopt die aanname — die PDFs zijn de officiële vragenbundels met "Vraag N … / X punten"-headers, ingevulde tabellen en duidelijke MC-stam + alternatieven.

De PDF `Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf` is **fundamenteel anders**. Visuele inspectie + pdfplumber-extract (2026-05-19):

- Geen puntentoekenning per vraag
- Geen formele "Vraag N … / punten"-header, alleen een nummer + thema ("1 Vennootschapsrecht")
- Per vraag een lijst hoofd-letters A/B/C/D/E die elk **een eigen subvraag** zijn, niet een MC-optie van één hoofdvraag
- Binnen sommige subvragen wel echte MC-alternatieven (lowercase a/b/c/d) — daar is duidelijk dat het een gestructureerde MC betreft
- Sommige sub-letters bevatten alleen een **onderwerp-aanduiding** zonder de stellingen ("Stellingen Juist of Fout ivm omzettingen")
- Sommige sub-letters bevatten een vraag + reeds gegeven antwoord-hint ("Toenemende eisbaarheid", "100.000 – 10.000 tantième = 90.000 euro")
- Typo's en onafgemaakte fragmenten ("Fifi" voor FIFO, "Kosten voor voorbereiding van een terrein……?", "Takxshelter")

Dit zijn de kenmerken van een **herinnering-reconstructie** door stagiairs die zich het examen herinneren — niet van een officiële vragenbundel. Hetzelfde patroon kan voorkomen op latere jaren (2025+) waar geen officiële bundel werd gepubliceerd.

ADR-021 v2-extract levert dus formeel correcte JSON-records voor 2024-1, maar de inhoud van `vraagtekst` is **niet** vergelijkbaar met die van een officiële PDF. Het modelantwoord-pipeline (ADR-020) gaat ervan uit dat de vraagtekst de officiële vraagstelling is — voor herinnering-stijl-vragen is dat een verkeerde aanname die leidt tot:

- Halfaf modelantwoorden die rusten op onvolledige vraag-fragmenten
- Onmogelijkheid om "correcte" MC-optie te kiezen omdat de opties zelf onduidelijk zijn
- `vraagtekst_onduidelijk`-gap-rapporten zonder duidelijk pad voorwaarts

## Beslissing

### 1. Vraag-herkomst expliciet classificeren

Per vraag wordt een nieuw veld `vraag_herkomst` ingevuld, met drie waarden:

| Waarde | Betekenis |
|---|---|
| `officieel` | Vraag komt uit een gepubliceerde ITAA/BIBF-vragenbundel met volledige stam + opties + (waar van toepassing) puntenverdeling. Vraagtekst is in principe letterlijk uit PDF. |
| `herinnering` | Vraag komt uit een stagiair-reconstructie van wat hij of zij zich herinnert. Stam is meestal aanwezig in fragment-vorm; opties en casus-data zijn onvolledig of dubbelzinnig. |
| `hybride` | Examen is hoofdzakelijk officieel maar bevat geannoteerde of reconstructie-fragmenten (zeldzaam). |

**Default voor nieuwe extracts**: indien onbekend → `officieel` (oude assumptie). Pilot 2024-1 zet alle 11 vragen op `herinnering`.

### 2. Vraag-volledigheid expliciet classificeren

Naast herkomst-classificatie ook een veld `vraag_volledigheid` met drie waarden:

| Waarde | Betekenis |
|---|---|
| `volledig` | Vraagstam + alle MC-opties + alle casus-data aanwezig en eenduidig. Modelantwoord-pipeline kan zonder risico draaien. |
| `fragment` | Vraagstam aanwezig (kort, mogelijk in trefwoordvorm) maar één of meer essentiële elementen ontbreken: MC-opties, casus-cijfers, of stellingen die het J/F-set vormen. |
| `stam_zonder_opties` | Alleen onderwerp-aanduiding zonder vraagstelling ("Stellingen Juist of Fout ivm omzettingen"). Niet beantwoordbaar zonder externe context. |

### 3. Nieuw veld `vraag_herinterpreteerd`

Wanneer `vraag_herkomst != "officieel"` mag het modelantwoord-werk **niet** rusten op `vraagtekst` direct. Een handmatige herinterpretatie-stap herformuleert wat de vraag waarschijnlijk vroeg, expliciet gelabeld als interpretatie:

```json
"vraag_herinterpreteerd": {
  "tekst_geherinterpreteerd": "<volledige, leesbare vraag-formulering>",
  "interpretatie_motivering": "<korte uitleg waarom deze interpretatie>",
  "confidence": "grounded" | "inferred",
  "datum": "2026-05-19"
}
```

`confidence`-discipline analoog aan ADR-020 §7:

- `grounded` — vraag is letterlijk uit PDF, herformulering is louter cosmetisch (witruimte, hoofdletters, leestekens)
- `inferred` — vraag is gereconstrueerd of aangevuld uit fragment; interpretatie steunt op redenering over wat ITAA waarschijnlijk vroeg

Originele `vraagtekst` en `vraagtekst_blokken[]` blijven **ongewijzigd** — dit is een **additief** veld, geen breaking change. Modelantwoord-pipeline (ADR-020) gebruikt bij voorkeur `vraag_herinterpreteerd.tekst_geherinterpreteerd` als beschikbaar; fallback `vraagtekst`.

### 4. Gestructureerde MC-opties — nieuw veld `mc_opties_gestructureerd`

Bestaand `opties[]`-veld bevat platte `{label, tekst}`-paren zoals door v2-extractor geleverd, en kan opties bevatten die geen MC-opties zijn (bv. subvraag-headers). Voor MC-vragen die echte MC zijn (lowercase a/b/c/d-opties op een gestructureerde stam) komt een typed lijst:

```json
"mc_opties_gestructureerd": [
  {
    "label": "a",
    "tekst": "Niet verplicht van factuur uit te reiken: BTW opeisbaar 3/5/N",
    "juistheid": "onbekend" | "juist" | "fout",
    "motivering": "<optioneel — alleen indien duidelijk uit doctrine>"
  }
]
```

`juistheid: "onbekend"` is de default — pas opvullen na expliciete modelantwoord-pass.

Voor herinnering-vragen waar opties niet (volledig) zichtbaar zijn, blijft dit veld `null` of leeg.

### 5. Antwoord-hint in vraagtekst — nieuw veld `antwoord_hint_in_vraag`

Sommige herinnering-vragen hebben het antwoord al in de vraagtekst staan (de stagiair noteerde meteen het antwoord dat hij gaf of waarvan hij dacht dat het juist was):

- "In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt? **Toenemende eisbaarheid**"
- "Hoeveel bedraagt de belastbare basis van A voor AJ23? **100.000 – 10.000 tantième = 90.000 euro**"

Dat is geen vraagstelling-element en moet expliciet gemarkeerd:

```json
"antwoord_hint_in_vraag": {
  "aanwezig": true,
  "tekst": "Toenemende eisbaarheid",
  "interpretatie": "Vermoedelijk noteerde stagiair het antwoord. Vraag-zonder-hint = 'In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt?'",
  "datum": "2026-05-19"
}
```

Voor vragen zonder hint: `{"aanwezig": false}` of veld weglaten.

### 6. Confidence-discipline op vraag-niveau

Aanvullend op ADR-020 §7 (antwoord-niveau confidence): per herinterpretatie een **interpretatie-confidence**. Deze hangt vast aan de herinterpretatie zelf, niet aan het modelantwoord:

- ⚖️ `grounded` — herinterpretatie is letterlijk uit PDF afleidbaar
- 🤖 `inferred` — herinterpretatie steunt op redenering of aanvulling

Bij **modelantwoord-generatie** op herinnering-vragen (in opvolgwerk) wordt de antwoord-confidence **één niveau onder** de interpretatie-confidence geplafonneerd. Een antwoord gebaseerd op een `inferred`-interpretatie kan niet `grounded` zijn — anders zou je zekerheid claimen die de vraag-interpretatie niet schraagt.

### 7. Beslis-vuistregel voor andere PDFs

Per PDF in `resources/raw/voorbeeldexamens/`:

| Bron | Vermoedelijke herkomst | Actie |
|---|---|---|
| 2003-bibf, 2008-bibf | officieel (BIBF-bundels) | geen herinterpretatie nodig; steekproef op 1-2 vragen ter verificatie |
| 2013-1, 2013-2, 2014-1, 2015-1 | officieel (ITAA-wedstrijdtekst met "Vraag N / punten"-headers) | geen herinterpretatie nodig; steekproef op 1-2 vragen ter verificatie |
| 2024-1 | herinnering (ontbrekende puntenverdeling, fragment-stijl, typo's, antwoord-hints) | herinterpretatie verplicht voor elk van de 11 vragen — pilot in deze ADR |
| 2025+ (toekomstig) | onbekend; check eerst aanwezigheid puntenverdeling + formele vraag-headers + volledige MC-opties | conform pilot 2024-1 indien herinnering-stijl |

### 8. Pipeline-volgorde

```
[1] Schema-check per examen-file       → schema_versie + bron-PDF
[2] Klassificeer vraag_herkomst         → officieel / herinnering / hybride
[3] Als herkomst != officieel:
    [3a] Per vraag: vraag_volledigheid → volledig / fragment / stam_zonder_opties
    [3b] Per vraag: tekst_geherinterpreteerd schrijven (met confidence)
    [3c] Detecteer antwoord_hint_in_vraag → expliciet uitknippen
    [3d] Structureer mc_opties_gestructureerd waar opties echt MC zijn
[4] Indien stam_zonder_opties:           → modelantwoord-pipeline NIET draaien;
                                             record_gap_report.type =
                                             "vraagtekst_onvolledig_herinnering"
[5] Indien fragment of volledig:         → modelantwoord-pipeline mag draaien,
                                             gebruikt tekst_geherinterpreteerd
                                             als bron
[6] Indien officieel:                    → geen herinterpretatie nodig,
                                             pipeline werkt op vraagtekst direct
```

### 9. Schema-uitbreiding examen-file (additief)

Per vraag in `data/programma/examen_vragen/<jaar>.json` worden volgende velden toegevoegd:

| Veld | Type | Verplicht | Doel |
|---|---|---|---|
| `vraag_herkomst` | enum `"officieel" \| "herinnering" \| "hybride"` | aanbevolen | Bron-classificatie |
| `vraag_volledigheid` | enum `"volledig" \| "fragment" \| "stam_zonder_opties"` | bij herkomst != officieel | Volledigheids-classificatie |
| `vraag_herinterpreteerd` | object of `null` | bij herkomst != officieel + volledigheid != stam_zonder_opties | Geherformuleerde vraagstelling met confidence |
| `mc_opties_gestructureerd` | list[object] of `null` | bij MC met zichtbare opties | Typed MC-opties met juistheids-labels |
| `antwoord_hint_in_vraag` | object of `null` | wanneer hint aanwezig | Markering van antwoord-fragment dat per ongeluk in vraagtekst zit |

Bestaande velden (`vraagtekst`, `vraagtekst_blokken[]`, `opties[]`, `sub_vragen[]`, `correct_antwoord`, `antwoord_motivering`, ...) blijven onaangeroerd. **Geen breaking change**.

### 10. Wat NIET in dit ADR

- **Geen schema 3.0** — geen examen_vragen-schema-bump. Velden zijn additief.
- **Geen Claude API in build-pipeline** — herinterpretatie is een handmatige + Opus-subagent-pass, geen scripted call naar `anthropic.Anthropic()`.
- **Geen andere PDFs in pilot** — alleen 2024-1. Steekproef-verificatie van 2003/2008/2013/2014/2015 is opvolgwerk (niet in pilot).
- **Geen modelantwoord-herziening** — bestaande modelantwoorden op 2024-1-vr3, vr7, vr10 blijven staan zoals ze waren. Of ze herzien moeten worden op basis van de herinterpretatie is opvolgwerk.
- **Geen nieuwe records-API-functies** — examen-files gebruiken directe `json.load`/`json.dump` (ADR-020 §2). Herinterpretatie-edits zijn directe schrijfacties.
- **Geen aanpassing van de OCR-normalisatie-gate** — `vraagtekst_normalized_at` blijft staan voor de OCR-pass; herinterpretatie is een aparte tweede pass.

## Voorbeeld-JSON (pilot 2024-1-vr10, sub C)

Hieronder de structuur zoals ze er voor één deelvraag uitziet na herinterpretatie. Originele velden zijn weggelaten voor leesbaarheid; alleen nieuwe velden zijn getoond.

```json
{
  "id": "2024-1-vr10",
  "vraag_herkomst": "herinnering",
  "vraag_volledigheid": "fragment",
  "vraag_herinterpreteerd": {
    "tekst_geherinterpreteerd": "Casus financiële analyse, 5 deelvragen: A. Stellingen over financiële onafhankelijkheid (juist/fout — stellingen niet bewaard in herinnering). B. Welke ratio kan je niet berekenen op basis van een verkort schema? (Hint: n-dagen klantenkrediet). C. In welke volgorde zijn rubrieken op de passiefzijde van de balans gerangschikt? (Hint in herinnering: 'toenemende eisbaarheid'). D. Hoe wordt het eigen vermogen berekend uit het jaarrekening-kortmodel NBB voor een kapitaalvennootschap? E. MC — Alfa is verlieslatend. Verhoging van de afschrijving op gebouwen door verkorting van de verwachte levensduur heeft volgend effect op de bruto verkoopmarge: a. Stijging / b. Daling / c. Geen / d. Stijging op voorwaarde dat de verhoogde afschrijving als bedrijfskost is geboekt.",
    "interpretatie_motivering": "Vraag 10 in PDF is fragmentarisch: sub-A noemt alleen 'Stellingen ivm financiële onafhankelijkheid' zonder stellingen; sub-B en sub-C bevatten een hint (antwoord) verstrengeld met de vraagtekst; sub-E heeft volledige MC-opties.",
    "confidence": "inferred",
    "datum": "2026-05-19"
  },
  "antwoord_hint_in_vraag": {
    "aanwezig": true,
    "tekst": "Toenemende eisbaarheid (sub-C); n-dagen klanten krediet (sub-B)",
    "interpretatie": "Stagiair noteerde vermoedelijk het antwoord direct in de vraag. Sub-B: 'n-dagen klantenkrediet' = vermoedelijk de ratio die je niet kan berekenen. Sub-C: 'Toenemende eisbaarheid' = vermoedelijk het antwoord op de volgorde-vraag.",
    "datum": "2026-05-19"
  },
  "mc_opties_gestructureerd": [
    {
      "label": "a", "tekst": "Stijging",
      "juistheid": "fout", "motivering": "Een verhoogde afschrijving kan de marge niet doen stijgen."
    },
    {
      "label": "b", "tekst": "Daling",
      "juistheid": "fout", "motivering": "Alleen indien afschrijving deel van kostprijs verkopen — niet standaard voor gebouwen-afschrijving."
    },
    {
      "label": "c", "tekst": "Geen",
      "juistheid": "juist", "motivering": "Gebouwen-afschrijving wordt typisch onder algemene bedrijfskosten geboekt, niet onder kostprijs verkopen — geen effect op brutomarge."
    },
    {
      "label": "d", "tekst": "Stijging op voorwaarde dat de verhoogde afschrijving als bedrijfskost is geboekt",
      "juistheid": "fout", "motivering": "Verhoogde kost kan geen marge-stijging veroorzaken — wel een daling indien onder kostprijs verkopen."
    }
  ]
}
```

## Gevolgen

**Nieuwe artefacten**:
- `docs/adr/ADR-022-vraag-herinterpretatie-draft.md` — dit document
- `data/extractie/2024-1-herinterpretatie-rapport.md` — pilot-rapport
- Pilot-uitbreiding van `data/programma/examen_vragen/2024-1.json` met nieuwe velden (additief)

**Bestaande artefacten gewijzigd**:
- `data/programma/examen_vragen/2024-1.json` — uitgebreid met nieuwe velden, originele velden blijven intact

**Niet-gewijzigd in pilot**:
- ADR-020 modelantwoord-pipeline blijft van kracht; consumeert `vraag_herinterpreteerd` als beschikbaar
- ADR-021 v2-extract blijft van kracht; deze ADR voegt een **post-extract** herinterpretatie-laag toe
- Andere examen-files (2003, 2008, 2013, 2014, 2015) — pilot raakt ze niet aan
- Bestaande modelantwoorden op 2024-1-vr3, vr7, vr10 — blijven staan, mogelijk te herzien in opvolg-pass

**Risico's**:
- *Subjectiviteit van herinterpretatie* — twee reviewers kunnen verschillende formuleringen produceren. Mitigatie: pilot-pass door één agent + Opus-review; afspraken in deze ADR codificeren.
- *Cascade naar reeds geschreven modelantwoorden* — vr3/vr7/vr10 hebben modelantwoorden gebaseerd op de originele fragmentarische vraag. Mitigatie: opvolgwerk markeert deze als kandidaten voor herziening; geen automatische verandering.
- *Verleiding om herinnering-vragen "officieel te maken"* — interpretatie kan wegglijden naar bron-vervanging. Mitigatie: confidence-discipline strikt, `inferred` is de default voor alles wat niet letterlijk PDF is.

## Changelog

- **v0.1 (2026-05-19, DRAFT)** — Eerste vastlegging op basis van pilot 2024-1 (11 vragen). Status DRAFT — niet Accepted want pilot moet de schema-keuze valideren voordat ze breed gerold wordt.
