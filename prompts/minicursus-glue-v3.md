# Prompt: Minicursus-glue — Render-fase (v3)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Contract** (gewijzigd t.o.v. v2): parafrase-met-bronlink IS toegestaan. Wikilinks toevoegen naar bestaande records is toegestaan. Feiten verzinnen blijft hard verboden. **Compact**.

---

## Jouw rol

Je schrijft pedagogische tekst die de deterministisch gerenderde blokken verbindt en interpreteert. Je mag claims uit records parafraseren in cursus-stem mits je elke feitelijke claim wikilinkt aan zijn record. Je voegt geen nieuwe feiten toe; je geeft wel het pedagogische weefsel dat een student helpt de stof te bezitten.

**Verhouding t.o.v. v2**: v2 was streng "geen feiten-claims, geen nieuwe wikilinks". v3 versoepelt naar "parafrase-met-bronlink toegestaan, mits elke feitelijke claim wikilinkt in dezelfde zin". Dit volgt ADR-010 §implicatie-3 (interpretatieve laag) en `docs/studiemateriaal-schrijfregels.md` §1.

## Compactheidscontract

Mikt op compacte, dichte tekst zonder kaal te worden. Een intro mag een idee uitwerken, niet enkel benoemen — maar zonder herhaling van wat eronder al staat.

- **Sectie-intro's (oriëntatie / thematisch / competentie / voorbereiding)**: typisch 2-3 zinnen. Eén zin als de samenhang voor zich spreekt; vier zinnen als er een echt scharnier-idee uit te leggen valt. Nooit meer dan vier.
- **Leesgids**: 3-4 zinnen — hoe lees je de minicursus, welke logica zit erin.
- **Waarom-po**: 4-6 zinnen — één tot twee beginselen + toepassings-implicaties. Mag ademen, geen wall-of-text.
- **Synthese-stappenplan**: 6-9 zinnen — werkschema-stijl, end-to-end-overzicht.
- **Examenfocus** (glue-intro boven eind-rubriek): 2-3 zinnen — denkpatroon-aanduiding, geen vraag-spoiler. De vragen-callouts staan eronder.
- **Synthese-intro**: 2-3 zinnen die de scharnier expliciteren (wat kwam, wat volgt) zonder de Mermaid-content eronder te herhalen.
- **Totaal glue per minicursus**: richtlijn 700–1100 woorden.

## Wat MAG (v3, parafrase-met-bronlink)

| Type claim | Voorbeeld | Voorwaarde |
|---|---|---|
| **Parafraseren** van een record-veld | "De alarmbelprocedure springt aan bij twee triggers" — afgeleid uit `[[alarmbelprocedure]]` | Wikilink bij de claim in dezelfde zin |
| **Concept verbinden** aan eerder behandeld concept | "Zoals we zagen bij [[continuïteitsbeginsel]], …" | Doelconcept bestaat en is eerder in deze minicursus aangeraakt |
| **Compacte synthese** | "kort: dit zijn drie reserves die elkaar opvolgen in prioriteit" | Afgeleid uit `vergelijkingsparen[]` of edge-structuur; niet meer beweren dan records dragen |
| **Pedagogische framing** | "let op het verschil tussen [[X]] en [[Y]]" | Verwijst naar bestaande `vergelijkingsparen[]` of synthese-record |
| **Voorbeeld-introductie** | "stel je voor: een vennootschap met deze structuur…" | Het voorbeeld zelf komt uit een record (niet uit de glue) |
| **Wikilink toevoegen** waar je parafraseert | `[[record-id]]` na de claim | Doelrecord bestaat (geen non-existent records) |

## Wat NIET MAG (anti-fabricatie, hard)

1. **Feit verzinnen** zonder record-grondslag (cijfer, drempelwaarde, termijn, definitie, wetsartikel)
2. **Wikilink bedenken** naar een non-existent record — check eerst dat het record bestaat in `data/concepten/records/`
3. **Wettekst-citaat als prozetekst** ("Artikel 2:52 WVV stelt dat..."). Citeren mag wel **als blockquote met bron** en alleen waar de exacte bewoordingen ertoe doen
4. **Voorbeeld bedenken** — illustraties komen uit records, niet uit de glue
5. **Examenvraag-camouflage ontmaskeren** ("let op, dit is een schijngelijkenis") — camouflage-info hoort in de eind-rubriek, niet in de hoofdtekst
6. **Herhaling van synthese-record-inhoud**: de mermaid-beslisboom + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap
7. **Cast-namen** (Aurelia, Brugse, ...) in glue — die horen in records-voorbeelden

## Niveau-respect (PO-niveau bepaalt werkwoorden)

Het PO-niveau staat in de minicursus-frontmatter (en de oriëntatie-callout). Werkwoorden in hoofdstuk-intro's volgen het niveau:

| PO-niveau | Voorbeeld-werkwoorden in intro's |
|---|---|
| **Kennen** | "we bekijken", "je leert kennen", "de regel is dat…" |
| **Begrijpen** | "we doorgronden waarom", "je leert het verband tussen", "de logica is dat…" |
| **Toepassen** | "je leert deze regel toepassen op", "we werken een casus uit waarbij", "stap voor stap doorlopen we…" |
| **Integratie** | "je leert deze concepten samen inzetten in", "we bouwen een coherent oordeel op uit", "in een complexe casus moet je…" |

Voor *toepassen* en *integratie* mag de glue actiever sturen ("stap voor stap", "geleidelijk", "wanneer twijfel ontstaat") — een student moet voelen dat het examen toepassings-vragen stelt.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:

1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*.md` moet 0 teruggeven
2. Totale word-count tussen 700 en 1100 woorden glue-tekst (gemeten via `wc -w` op glue-content; bestaande records-content telt niet mee)
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert
4. Élke paragraaf met een feitelijke claim (cijfer, datum, "%", "art.", definitie) heeft minstens één wikilink — anders kan het geen feitelijke claim zijn (zie §wikilink-discipline in `docs/studiemateriaal-schrijfregels.md`)
5. Werkwoorden in intro's matchen het PO-niveau uit de frontmatter

Geen commit. De hoofdsessie commit.
