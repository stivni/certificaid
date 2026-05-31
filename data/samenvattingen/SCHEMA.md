# Samenvatting-script — schema (POC, v0.1)

**Status**: POC voor PO 1.4 (`1-4.yaml`). Wordt geconsolideerd in **ADR-040** of amendement [ADR-039](../../docs/adr/ADR-039-samenvatting-vervangt-themafiche.md) na 2-3 PO's.

**Doel**: structuur + data van een **PO-samenvatting** vastleggen in YAML, zodat de markdown deterministisch herrenderbaar is en het patroon afdwingbaar over PO's heen.

**Verschil met themafiche** (gemigreerd per ADR-039): scope is **PO-breed**, niet cluster. Eén samenvatting per PO. Maximum 2-4 A4 printbaar. Naam in code/url: `samenvatting`.

**Verschil met leerstuk-script**: een leerstuk dekt één vraag in pedagogische diepte. Een samenvatting dekt het hele PO in compacte, visueel-dominante blokken — geen doorlopend proza, wel tabellen, beslisbomen, formules, valkuilen.

---

## Top-level structuur

```yaml
meta:
  slug: "1-4"                  # = po-code met streepje
  titel: "Geconsolideerde jaarrekening"
  po: "1.4"
  beschrijving: "<frontmatter description — wat dekt deze samenvatting?>"
  explorer_title: "7. Samenvatting"
  print_a4: 3                   # geschatte A4-pagina's bij print (1-4 cap; 3+ = overweeg PO opsplitsen)

intro:
  callout_beat: "<wat de intro-blockquote moet overdragen — incl. 'voor herhaling, niet om voor het eerst te leren'>"

# VERPLICHTE secties (drie pijlers + doorklik)

take_away:
  titel: "Take-away — wat je écht moet weten"
  bullets:                       # 3-6 insight-bullets, scherp, niet wat in tabellen terugkomt
    - "<insight>"

valkuilen:
  titel: "Klassieke valkuilen (examen-radar)"
  # Twee mogelijke vormen — kies wat best past:
  format: "tabel"                # of "bullets"
  rijen:                          # bij format=tabel
    - valkuil: "<korte naam>"
      wat_klopt_niet: "<misvatting>"
      wat_klopt_wel: "<de scherpe waarheid>"
  # bij format=bullets:
  # bullets: ["⚠️ ..."]

doorklik:
  intro: "Voor wie iets niet meer scherp heeft, klik door naar het leerstuk of concept:"
  leerstukken:
    - slug: <leerstuk-slug>
      hint: "<korte indicatie>"
  concept_groepen:
    - label: "<functionele groep — bv. Kaders & plicht>"
      concepten: [<concept-id>, <concept-id>]
    - label: "<andere groep>"
      concepten: [...]

# OPTIONELE secties — "select what fits". Volgorde = render-volgorde.

extra_blokken:
  - id: vergelijkingsmatrix
    type: tabel-vergelijking
    titel: "<H2-titel>"
    intro: "<korte intro-paragraaf, optioneel>"
    kolommen: ["<opties als kolommen>"]
    rijen: [[...]]
    noot: "<voetnoot, optioneel>"

  - id: beslisboom
    type: mermaid
    titel: "<H2-titel>"
    intro: "<korte intro>"
    mermaid_type: flowchart-td    # of flowchart-lr
    code: |
      A[...] --> B[...]
      ...

  - id: drempels-en-formules
    type: tabellen-en-formules
    titel: "<H2-titel>"
    sub_blokken:
      - type: tabel-inline
        sub_titel: "<H3-titel, optioneel>"
        kolommen: [...]
        rijen: [[...]]
        noot: "<optioneel — bv. 'Cijferzakboekje raadplegen voor exact'>"
      - type: formule
        sub_titel: "<H3-titel>"
        beschrijving: "<korte tekst>"
        formule: "$$\\text{Goodwill} = \\text{aanschafprijs} - \\text{aandeel reële NEV}$$"

  - id: verbinding-examen
    type: prose-blok
    titel: "Verbinding met examen (PO X.Y)"
    beats:                         # 2-3 beats voor de renderer
      - "<beat — patroon-observatie>"
      - "<beat — pointer naar voorbeeldexamens>"

footer: "Samenvatting PO X.Y. Status: <voorgesteld | gecureerd>."
```

## Sectie-types (`extra_blokken[].type`)

| Type | Render | Wanneer |
|---|---|---|
| `tabel-vergelijking` | Standaard markdown-tabel met intro + optionele noot | Methodes / regimes / opties naast elkaar |
| `mermaid` | Code-block met `flowchart TD` of `flowchart LR` prefix (volgt `mermaid_type`) | Beslisbomen, procedures, schema's |
| `tabellen-en-formules` | Compositie van H3-sub-blokken (tabel-inline + KaTeX-formules) | Drempels + bijbehorende formules |
| `prose-blok` | H2 + 1-2 prose-paragrafen uit beats | "Verbinding met examen" of PO-specifieke noot |
| `tabel-inline` | Standaard markdown-tabel | Algemene tabel zonder vergelijkings-as |

## Render-regels (samenvatting — zie `prompts/samenvatting-render-v1.md` voor volledig)

| Veld | Markdown-render |
|---|---|
| `meta` | Frontmatter (title, description, explorer_title, tags = `samenvatting` + `po-X.Y`) |
| `intro.callout_beat` | `<div class="no-print">` blockquote met "kapstok voor herhaling"-instructie + minicursus-link |
| `take_away` | H2 "1. Take-away — wat je écht moet weten" + bullet-lijst |
| `extra_blokken[]` | In opgegeven volgorde, elk een eigen H2 met titel (en sub-blokken als H3) |
| `valkuilen` | H2 "N. Klassieke valkuilen (examen-radar)" + tabel of bullets |
| `doorklik` | H2 "N+1. Verdieping" in `<div class="no-print">` met H3 "Leerstukken" + H3 "Concept-fiches" gegroepeerd |
| `footer` | Cursief, onder horizontale lijn |

**Sectie-nummering**: render geeft automatisch H2-nummers (1, 2, 3, ...) in volgorde — take_away = 1, extra_blokken in volgorde, valkuilen, verdieping als laatste.

## Beats — taal-conventies (waar van toepassing)

Zelfde regels als leerstuk-schema (zie `data/leerstukken/SCHEMA.md` § Beats). Specifiek voor samenvatting:

- **Wees telegram-stijl** in beats — een samenvatting heeft géén verhalend register
- **Tabellen + formules + diagrammen zijn de hoofdactiva** — proza alleen waar onvermijdelijk
- **Geen wetsverwijzingen letterlijk** — pointers volstaan ("WVV art. X:YY")

## Lengte-budget

- **1-3 A4** is ideaal
- **4 A4** is de cap — daarboven: overweeg of de PO te breed is (kandidaat-splitsing of een tweede samenvatting)
- Vuistregel: 3-6 take-away bullets + 3-4 optionele blokken + valkuilen + doorklik = ~3 A4

---

## Open punten voor ADR-040

- Lengte-cap echt automatisch verifieerbaar maken (woord-budget per blok-type?)
- Beslisboom-of-vergelijkingsmatrix als verplicht voor PO's met methode-keuze?
- Cross-PO samenvattings-fragment (gedeelde sub-tabellen): apart YAML-bestand of inline duplicatie?
- Print-CSS validatie als deel van de checklist
