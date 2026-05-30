# Leerpad-skelet — v1 (Opus)

**Doel**: voor een nieuwe PO een **gecoördineerd skelet** voorstellen van minicursus + leerstukken in één gedachtegang, op basis van de officiële taken/doelstellingen + voorbeeldexamens.

**Voor**: Opus tijdens sparring met de gebruiker. Eén Opus-run produceert het overzicht; de mens reviewt; daarna pas scripts schrijven en renderen.

**Output**: één markdown-document `docs/leerpad-skelet-<po>.md` dat als sparring-startpunt en als input voor de scripts-stap dient.

---

## Achtergrond — waarom samen, niet apart

Minicursus en leerstukken zijn één pedagogische eenheid voor een PO:
- De **minicursus** vertelt het verhaal (waarom dit vak, wat is het, wat moet je kunnen) en wijst naar leerstukken
- De **leerstukken** dekken elk één samenhangende didactische vraag binnen het PO
- Een PO heeft typisch 4-7 leerstukken (volgens ADR-037 granulariteits-stelregel)

Splitsen in twee passes (eerst leerstukken bedenken, dan minicursus daaromheen schrijven) creëert mismatch-risico. Skelet-eerst-aanpak verbindt ze meteen.

---

## Standaard prompt-template

Plak in een Opus-sessie (of Agent met opus-model override) met:

```markdown
Je werkt aan het skelet voor een PO van het certificaid-project. Doel: voor PO <<PO_CODE>> een gecoördineerd voorstel van minicursus + leerstukken neerleggen, op basis van het officiële examenprogramma + voorbeeldexamens.

Output: één markdown-bestand `docs/leerpad-skelet-<<PO_SLUG>>.md` (waar <<PO_SLUG>> de slug-vorm is — bv. `1-4` voor PO 1.4).

## Lees deze inputs

1. **Het PO-blok in `data/programma/programma.json`** — taken, doelstellingen, kenniselementen per anchor. Filter op je PO.
2. **`data/programma/anchors.json`** — anchor-metadata.
3. **Voorbeeldexamens voor dit PO**: zoek in `content/voorbeeldexamens/po-<<PO_CODE>>.md` (indien bestaand) — welke vraag-eenheden + patronen?
4. **ADR-037** (`docs/adr/ADR-037-leerstuk-vierde-leerlaag.md`) — vier-lagen-model + granulariteits-stelregel.
5. **`docs/leerstuk-schrijfregels.md`** — wat een leerstuk wel/niet doet.
6. **`docs/leerstuk-procedure.md`** — verwijst terug naar dit document; lees voor context.
7. **Referentie**: `docs/leerpad-skelet-1-4.md` indien al bestaand (gold-standard voor PO 1.4).
8. **Concept-records die deze PO raken**: via MCP `mcp__certificaid-rag__zoek_concepten` met PO-zoektermen (bv. "consolidatie" voor 1.4, "BTW-vrijstellingen" voor 2.4).

## Werkstroom

### Stap 1: programma-analyse

Lijst de officiële taken en doelstellingen op. Identificeer de hoofdtaak (meestal één per PO). Splits in:
- **Kern** — wat specifiek bij dit PO hoort
- **Rakend** — wat met andere PO's gedeeld is (vermeld welke andere)

### Stap 2: voorbeeldexamen-patronen

Welke vragen-types verschijnen herhaaldelijk? Welke concepten worden bevraagd? Welke valkuilen verschijnen? Dat verankert je leerstuk-keuze in examen-realiteit.

### Stap 3: leerstuk-voorstel

Stel 4-7 leerstukken voor. Per leerstuk:
- **Slug** (kebab-case, vraag-gericht óf thema-aspect)
- **Vraag** die het beantwoordt (in mensentaal — "wat is X?", "hoe doe je Y?")
- **Type**: entry / scope / techniek / specifiek / proces / enkelvoudig (vrij — maar consistency met PO 1.4 mockups helpt)
- **Gedekte taken/doelstellingen** (lijst van anchor-IDs of doelstelling-tekst)
- **Gedekte concepten** (3-8 concept-slugs uit `data/concepten/records/` die het leerstuk integreert)
- **Korte rationale** (waarom dit een eigen leerstuk verdient, niet een sub-sectie elders)

**Granulariteit-stelregel**: eerder samen dan splitsen. Sub-vragen worden secties binnen een leerstuk, geen apart leerstuk.

### Stap 4: gap-check

Lijst per officiële taak/doelstelling welke leerstuk(en) hem dekken. Identificeer gaten:
- Taak/doelstelling niet gedekt? → extra leerstuk OF rakend-naar-andere-PO-noot
- Concept centraal in PO maar niet in een leerstuk? → reflectie nodig

### Stap 5: minicursus-skelet

Volg de canonieke 5-secties-structuur van ADR-036 (sinds 1.4 samenvoeging §3+§4):

1. **Waarom dit vak?** — Korte motivatie + tabel "Hoe past dit in het bredere programma?"
2. **Wat is dit vak?** — Het verhaal in compacte sub-secties met wikilinks naar leerstukken voor detail (1-2 paragrafen per sub-sectie, geen volle uitleg)
3. **Wat moet je kunnen + hoe pak je het aan** — Leerstukken-leesroute + themafiche-verwijzing
4. **Examen-radar** — Voorbeeldexamen-patronen + bevraagde concepten
5. **Concepten cross-PO** — Tabel met concepten die ook elders relevant zijn

Voor elke sectie: noteer welke wikilinks erin komen + welke beats.

### Stap 6: voorbeeldgroep-data

Stel voor: één centrale mock-case (analoog aan Aurelia voor PO 1.4) die door alle leerstukken heen wordt gebruikt. Schets:
- Naam + rechtsvorm
- Welke relaties / cijfers nodig?
- Welke documenten (balansen, resrek, boekingen) genereren we?

Of als de PO meerdere onafhankelijke voorbeelden vraagt: voorbeeld-per-leerstuk.

### Stap 7: themafiche-mapping

Voor elke leerstuk: welk(e) themafiche(s) bestaan al die het cluster dekken? Vermeld of een nieuwe themafiche nodig is.

## Output-formaat

Schrijf alles in `docs/leerpad-skelet-<<PO_SLUG>>.md` met deze structuur:

```markdown
# Leerpad-skelet PO <<PO_CODE>> — <<PO_TITEL>>

**Status**: voorstel (datum)
**Volgende stap**: scripts in `data/leerstukken/<slug>.yaml` per leerstuk + voorbeeldgroep in `data/voorbeeldgroepen/<naam>.yaml`.

## 1. Programma-analyse

(hoofdtaak, kern, rakend)

## 2. Voorbeeldexamen-patronen

(tabel, observaties)

## 3. Leerstuk-voorstel

(één h3 per leerstuk met slug/vraag/type/dekking/concepten/rationale)

## 4. Gap-check

(matrix taak/doelstelling × leerstuk; gaten gemarkeerd)

## 5. Minicursus-skelet

(5 secties met inhoud-indicatie + wikilinks)

## 6. Voorbeeldgroep

(naam + case-beschrijving + benodigde data)

## 7. Themafiche-mapping

(welke bestaan, welke nieuw)

## 8. Open vragen voor sparring

(beslismomenten waar de mens moet kiezen)
```

## Stijl-regels

- **Voorstellend, niet definitief**: alles is sparring-input. Markeer onzekerheden expliciet.
- **Bondig per leerstuk**: 5-8 zinnen voor de rationale, niet meer.
- **Verifieer claims via RAG** waar je een wetsverwijzing of cijfer noemt — geen training-only.
- **Verwijs naar bestaande artefacten** (concept-records, voorbeeldexamens) i.p.v. dingen te verzinnen.

## Rapport

Aan einde, max 6 bullets:
- Aantal leerstukken voorgesteld
- Hoofdtaak van het PO
- Gaten geïdentificeerd
- Of er een nieuwe voorbeeldgroep nodig is of een bestaande hergebruikt
- Belangrijkste onzekerheid voor sparring
- Volgende stap (script-schrijven per leerstuk)

Begin nu.
```

---

## Hoe in te zetten

1. Vul placeholders in:
   - `<<PO_CODE>>` — bv. `1.4` of `2.4`
   - `<<PO_SLUG>>` — bv. `1-4` of `2-4` (dash i.p.v. punt voor Quartz folder-compat)
   - `<<PO_TITEL>>` — bv. "Geconsolideerde jaarrekening" of "BTW"

2. Start Opus-sessie of Agent met opus-model override.

3. Wacht op skelet-document. Review samen met de gebruiker. Beslis welke leerstukken finaal worden.

4. Pas dan: scripts schrijven (`data/leerstukken/<slug>.yaml`) + voorbeeldgroep-data + render via `leerstuk-render-v1.md`.

## Werkbasis

| Artefact | Locatie | Status (PO 1.4 als referentie) |
|---|---|---|
| Skelet-document | `docs/leerpad-skelet-<po-slug>.md` | Nog niet retroactief voor 1.4 geschreven — kan post-hoc als template gebruikt worden |
| Scripts | `data/leerstukken/<slug>.yaml` | 6 stuks voor 1.4 |
| Voorbeeldgroep | `data/voorbeeldgroepen/<naam>.yaml` | `aurelia.yaml` voor 1.4 |
| Markdown-output | `content/leerpaden/<po-slug>/<slug>.md` | 5 leerstukken voor 1-4/ + 1 cross-PO in `content/leerstukken/` |
| Minicursus | `content/leerpaden/<po-slug>/index.md` | `1-4/index.md` |
| Themafiche | `content/themafiches/<cluster>.md` | `consolidatie.md` updated met tweelaags-doorklik |
