# Oefening-script — schema (POC, v0.1)

**Status**: POC voor PO 1.4 (`nordica-consolideren`). Wordt geconsolideerd in **ADR-038** na ervaring met meerdere PO's.

**Doel**: data + didactische structuur van een **doorgewerkte oefencase** vastleggen in YAML, zodat de markdown deterministisch herrenderbaar is. Aanvullende leerlaag op de drie van ADR-036 (minicursus / leerstuk / themafiche) + leerstuk-variant uit ADR-037 — oefening is de **actieve** laag waar de student zelf het werk doet.

**Verschil met leerstuk-script**: een leerstuk legt iets uit (passief lezen). Een oefening geeft een opgave + uitgewerkte oplossing per stap — de student probeert eerst zelf, dan controleert hij/zij stap-per-stap door een `<details>`-blok te openen. Markdown-render gebruikt `<details>`/`<summary>` voor de uitwerking.

---

## Top-level structuur

```yaml
meta:
  slug: <kebab-case-slug>
  titel: "Oefening: <korte titel>"
  po: "1.4"
  cluster: <cluster-slug>
  beschrijving: "<frontmatter description>"
  studietijd: "60-75 min"
  niveau: "volledig"          # "volledig" = doorlopende mini-case · "scoped" = examen-stijl deelvragen

intro:
  callout_beat: "<wat de intro-blockquote moet overdragen — incl. instructie 'doe eerst zelf, klap pas dan open'>"

opgave:
  # Alle data die de student vóór de eerste stap krijgt
  scenario_beats:
    - "<beat — sets up the case>"
    - "<beat — extra context>"
  groep:
    moeder: { naam: ..., rechtsvorm: ... }
    deelneming:
      - naam: ...
        percentage: ...
        aanschafprijs: ...
        overnamedatum: ...
        boekwaarde_nev: ...
        reele_nev: ...
  balansen:
    <naam>:
      titel: "..."
      eenheid: "mln EUR"
      activa: [...]            # zie balans-structuur leerstuk-SCHEMA
      passiva: [...]
  resultatenrekening:
    <naam>: {...}
  intra_groep_transacties:
    - type: verkoop            # of: vordering | dividend | dienstprestatie
      van: <naam>
      aan: <naam>
      bedrag: ...
      details: {...}
  tabellen:
    <ref>:
      titel: "..."
      kolommen: [...]
      rijen: [...]

stappen:
  - id: stap-1-<slug>
    titel: "Stap 1 — <korte titel>"
    instructie_beats:
      - "<vraag aan de student, mensentaal>"
    uitwerking_beats:
      - "<beat 1 van de oplossing>"
      - "<beat 2>"
    uitwerking_visualisaties: [{type: ..., ref: ...}, ...]    # optioneel
    valkuil_beat: "<optionele waarschuwing voor typische fout>"

afsluiting:
  reflectie_beats:
    - "<beat — wat de student zou moeten meenemen>"
  doelstellingen_gedekt: ["1.4.doel.X.Y", "..."]              # programma.json-codes
  valkuilen_geoefend: ["IFRS 11-verbod evenredige", "..."]

verder_lezen:
  leerstukken: [{slug: ..., hint: ...}, ...]
  themafiches: [{slug: ..., hint: ...}]
  examenvragen_link: "voorbeeldexamens/po-X-Y"                # optioneel

wettelijk_fundament:                                          # zelfde structuur als leerstuk
  - onderwerp: ...
    ref: "WVV art. X:YY"
    noot: ...

footer: "Oefening PO X.Y. Status: ..."
```

## Render-regels (samenvatting — zie `prompts/oefening-render-v1.md` voor volledig)

| Veld | Markdown-render |
|---|---|
| `meta.titel` + frontmatter | Standaard frontmatter (title, description, tags = `oefening`, `po-X.Y`, `cluster-...`, `studietijd-XX-min`); optioneel `explorer_title` |
| `intro.callout_beat` | `<div class="no-print">` blockquote met expliciete "doe eerst zelf"-instructie |
| `opgave.scenario_beats` | H2 "Opgave" + prose-paragrafen |
| `opgave.balansen` / `resultatenrekening` / `tabellen` | Direct gerenderd onder "Opgave" of in eigen H3-secties |
| `stappen[]` | Eén H2 "Uitwerking" + per stap een H3 met `instructie_beats` als prose, daarna `<details><summary>**Oplossing — klik om te tonen**</summary>...uitwerking_beats + visualisaties...</details>` |
| `afsluiting.reflectie_beats` | H2 "Reflectie" + prose |
| `verder_lezen` | H2 "Wanneer dit zit, ga dan naar" in `<div class="no-print">` |
| `wettelijk_fundament` | Standaard H2 zoals leerstuk |
| `footer` | Cursief, onder horizontale lijn |

## Visualisatie-types (gedeeld met leerstuk-SCHEMA)

| Type | Bron | Render-regel |
|---|---|---|
| `balans-paar` | `opgave.balansen.<ref>` of inline | `<div class="balans-twee-koloms">` + 2 tabellen |
| `resultatenrekening` | `opgave.resultatenrekening.<ref>` | Staffel-tabel |
| `boeking` | `opgave.boekingen.<ref>` of inline | 5-koloms CBN-stijl (`  · MAR · Omschrijving · Debet · Credit`) |
| `tabel-vergelijking` / `mock-mutatie-tabel` | `opgave.tabellen.<ref>` | Standaard markdown-tabel |
| `tabel-inline` | inline `kolommen` + `rijen` | Idem |

## Beats — taal-conventies

Zelfde regels als leerstuk-schema (zie `data/leerstukken/SCHEMA.md` § Beats). Eén extra conventie voor oefeningen:

- **`instructie_beats`** zijn formuleringen aan de student ("Bepaal welke methode...", "Bereken het consolidatieverschil..."). Imperatief, helder, één-zin per beat.
- **`uitwerking_beats`** zijn beats die de oplossing pedagogisch opbouwen — niet de oplossing letterlijk dicteren maar instructies voor de renderer (mens of LLM) om er prose van te maken.

---

## Open punten voor ADR-038

- Stappen-aantal vrij of begrensd? (Nordica heeft er 5; complexere oefeningen kunnen tot 8 gaan)
- Hint-systeem: tussen instructie en oplossing een tussenlaag "hint" toevoegen?
- Multiple-choice variant: voor pure begrip-vragen zonder uitwerking-prose, alleen vier opties + correct antwoord
- Oefening-laag formaliseren in ADR-036 amendement of nieuw ADR-038
