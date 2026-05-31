# Leerstuk-script — schema (POC, v0.1)

**Status**: POC voor PO 1.4 (`wie-moet-consolideren`, `hoe-consolideren`). Wordt
geconsolideerd in **ADR-038** na ervaring met deze twee bestanden.

**Doel**: deterministische didactische structuur vastleggen, zonder prose te
serialiseren. Een script-YAML zegt wát er in welke volgorde moet komen en welke
visualisaties worden gebruikt — een Sonnet-renderer (of mens) levert de prose.

**Wat een script wél vangt**:
- Volgorde van pedagogische "beats" per sectie
- Heading-hiërarchie (h2 / h3 / h4 / h5)
- Welke visualisaties (balansen, boekingen, mermaid, tabellen) en welke data ze gebruiken
- Wettelijk-fundament-refs en doorklik-wikilinks
- Asides als blockquotes (vs sub-secties als heading-stap)

**Wat een script NIET vangt**:
- Exacte bewoordingen
- Bullet-uitsplitsing van een beat
- Lengte per beat (LLM mag een beat 1 zin of 1 paragraaf maken zolang het functioneel hetzelfde overdraagt)

---

## Top-level structuur

```yaml
meta:
  slug: <kebab-case slug>
  titel: "<Mensentaal titel>"
  po: "1.4"
  cluster: consolidatie
  voorbeeldgroep: aurelia              # ref naar data/voorbeeldgroepen/<naam>.yaml
  beschrijving: "<frontmatter description>"

intro:
  callout_beat: "<wat de intro-blockquote moet overdragen>"

antwoord_in_een_blik:
  beats: ["<beat 1>", "<beat 2>", ...]
  visualisaties:
    - type: mermaid
      ref: <key uit voorbeeldgroep.mermaid_diagrammen>

opbouw:
  - id: <sectie-slug>
    titel: "<H2-titel>"
    niveau: 2
    beats: ["<beat>", "<beat>", ...]
    visualisaties: [{type: ..., ref: ...}, ...]
    kinderen: []                       # optioneel — nested sub-secties

wettelijk_fundament:
  - onderwerp: "<wat de regel betreft>"
    ref: "<WVV art. X:YY of CBN-advies …>"

verder_lezen:
  leerstukken: [<slug>, <slug>]
  samenvatting:                          # optioneel; render automatisch als wikilink naar PO-samenvatting
    hint: "<korte omschrijving>"         # of `hint: null` om over te slaan (bv. cross-PO leerstukken zonder duidelijk PO)
  concepten: [<slug>, <slug>]
```

**Belangrijk** (ADR-039): het oude `themafiches: [{slug, hint}]`-veld is **vervangen** door `samenvatting: {hint}`. Eén samenvatting per PO; locatie + slug worden automatisch afgeleid uit `meta.po` (`[[leerpaden/<po-slug>/samenvatting|Samenvatting PO <po>]]`).

## Sectie-types (`type` veld; default = `sectie`)

| Type | Render | Wanneer |
|---|---|---|
| `sectie` (default) | h-tag (op basis van `niveau`) + content uit beats + visualisaties | Pedagogische hoofdstap |
| `blockquote-aside` | `> **<intro>**.` + prose uit beats | Achtergrond/uitweiding die hoofdverhaal niet hoort te onderbreken als heading |
| `intro-callout` | `<div class="no-print">` + blockquote | Eerste intro-block voor minicursus-link |

## Visualisatie-types

| Type | Render | Data-ref |
|---|---|---|
| `mermaid` | Mermaid code-block | `voorbeeldgroep.mermaid_diagrammen.<ref>` |
| `balans-paar` | `<div class="balans-twee-koloms">` met activa + passiva tabellen | `voorbeeldgroep.balansen.<ref>` |
| `resultatenrekening` | Staffel-tabel | `voorbeeldgroep.resultatenrekeningen.<ref>` |
| `boeking` | CBN-stijl tabel (`  · MAR · Omschrijving · Debet · Credit`) — eerste kolom leeg voor debet, `aan` voor credit. MAR-veld optioneel per regel. | `voorbeeldgroep.boekingen.<ref>` |
| `tabel-vergelijking` | Standaard markdown-tabel | Inline `kolommen` + `rijen` of `ref` |
| `mock-mutatie-tabel` | Vergelijkings-tabel met kolom per entiteit + mutatie + geconsolideerd | `voorbeeldgroep.mock_geconsolideerd.<ref>` |
| `tabel-inline` | Standaard markdown-tabel | Inline `kolommen` + `rijen` |

## Boeking-data-structuur (CBN-stijl)

Boekingen onder `voorbeeldgroep.boekingen.<ref>` volgen het CBN-advies-formaat:

```yaml
boekingen:
  <ref>:
    titel: "Boeking — <korte omschrijving>"
    eenheid: "mln EUR"          # of "EUR" — in titel/voetnoot, niet per kolom
    regels:
      - mar: "280"              # MAR-rekening; optioneel (leeg-string voor consolidatie-rubrieken zonder vaste MAR)
        omschrijving: "Deelneming Bellator"
        debet: 6.0              # vul ÓFWEL debet ÓFWEL credit, nooit beide
      - mar: "550"
        omschrijving: "Kredietinstellingen — rekening-courant"
        credit: 6.0
    totaal: 6.0                  # optioneel
```

Renderer geeft (eerste kolom = `aan` op credit-regels):

```
|     | MAR | Omschrijving                | Debet | Credit |
|-----|-----|-----------------------------|------:|-------:|
|     | 280 | Deelneming Bellator         | 6,0   |        |
| aan | 550 | Kredietinstellingen — R/C   |       | 6,0    |
```

Voor consolidatie-boekingen: MAR is vaak leeg of indicatief (geconsolideerde rubriekcodes zoals `9920` voor consolidatieverschil zijn informele praktijk, niet wettelijk opgelegde MAR-nummers).

## Beats — taal-conventies

Beats zijn instructies aan de renderer (mens of LLM). Schrijf ze in
mensentaal, **niet** als template-slots. Concrete voorbeelden:

| Goed | Slecht |
|---|---|
| "Introduceer eerst waar de cijfers vandaan komen — niet koud invallen" | `{intro_paragraph}` |
| "Toon balans Bellator vóór herwaardering, leg sub-rubrieken even uit" | `{balans_uitleg}` |
| "Blockquote-aside: leg goodwill uit als premium boven boekwaarde" | `{goodwill_section: ...}` |
| "Examen-valkuil: stagiairs vergeten stap 3 — concretiseer met cijfers" | `{valkuil}` |

Vuistregel: zou een nieuwe collega die de schrijfregels heeft gelezen begrijpen
wat je bedoelt zonder verdere uitleg? → goed.

---

## Open punten voor ADR-038

- Hoe valideren we dat een rerender de didactische volgorde echt vasthoudt?
  (regex-check op heading-titels? sectie-id's? aantal visualisaties?)
- Beats-vocabularium uitbreiden naar standaard-set (introduceer · toon · concretiseer · waarschuw · vergelijk · synthetiseer · …)?
- Render-pipeline: Sonnet-prompt per leerstuk vs één globale prompt met dispatch op `meta.type`?
- Versionering: hoe houden we generated markdown gesynchroniseerd met script-YAML? (timestamp? hash? handmatige bijwerkdiscipline?)
