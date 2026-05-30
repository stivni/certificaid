# Leerstuk — schrijfregels v1

**Voor**: een Opus/Sonnet-agent of mens die een leerstuk schrijft.
**Canoniek**: [ADR-037](adr/ADR-037-leerstuk-vierde-leerlaag.md). Lees ook [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md) voor de positie tussen minicursus en concept.
**Gold-standard mockup**: [`content/leerpaden/1.4/wie-moet-consolideren.md`](../content/leerpaden/1.4/wie-moet-consolideren.md).
**Canonical pad**: PO-specifieke leerstukken onder `content/leerpaden/<po>/<slug>.md`; cross-PO leerstukken (toekomst) onder `content/leerstukken/<slug>.md`.

---

## Doel

Een leerstuk is **één samenhangende didactische vraag, helemaal doorwerkt**. Bedoeld voor de stagiair die de stof voor het eerst écht wil begrijpen — niet voor wie herhaalt (themafiche) en niet voor wie een definitie opzoekt (concept-fiche).

**Een leerstuk is**:
- Pedagogisch — leidt de lezer stap voor stap door één vraag
- Visueel-dominant — concretiseert via tabellen, diagrammen, voorbeelden, mock-jaarrekeningen
- In eigen woorden — verwijst naar concepten voor detail, herhaalt geen definities verbatim
- Begrensd — één vraag, geen overlap met andere leerstukken

**Een leerstuk is NIET**:
- Een verzameling concept-definities
- Een wetstekst-samenvatting
- Een examen-radar
- Een printbare kapstok (= themafiche)

---

## Doelgroep en toon

- **Doelgroep**: ITAA-stagiair die de stof voor het eerst grondig leert
- **Toon**: rustig, opbouwend, geruststellend. "We gaan dit samen uitwerken"-register
- **Persoon**: tweede persoon enkelvoud ("je"), niet "ik/wij" en niet onpersoonlijk
- **Lengte**: 800-2000 woorden voor "wat"- en "wie"-leerstukken; **tot ~4500 woorden** acceptabel voor "hoe"-leerstukken die meerdere technieken naast elkaar uitwerken mét praktijk-balansen (KB-WVV rubricering), balans-voor/na, doorgewerkte casus en eliminaties uitgelegd op boekingsniveau (journaalpost-stijl, sub-secties Situatie → Probleem → Oplossing). Korter → te dun voor "echt snappen". Langer → te lang voor één-leerzitting; splits of pak grover

---

## Granulariteits-stelregel

> **Eerder samen dan splitsen.** Een leerstuk mag groot zijn als het verhaal samenhangt.

Sub-vragen worden secties, geen apart leerstuk. Voorbeeld: "wie moet consolideren" omvat controle-test + kringafbakening + drempels + wijzigingen — vier sub-vragen, één leerstuk, want de stagiair stelt ze in één denkbeweging.

**Splits-criterium**: pas opsplitsen als de twee delen onafhankelijk bevraagd worden op examen, of als de lengte > 2000 woorden zou worden bij behoorlijke uitwerking.

---

## Slug-conventie

Twee patronen toegelaten — auteur kiest wat natuurlijk leest:

| Patroon | Voorbeeld |
|---|---|
| Vraag-gericht | `wie-moet-consolideren`, `hoe-consolideren`, `wat-is-een-geconsolideerde-jaarrekening` |
| Thema-aspect | `geconsolideerde-jaarrekening-opmaken`, `consolidatie-toepassingsgebied`, `individuele-jaarrekening-opmaken` |

**Hard requirement**: slug uniek binnen de hele `content/`-boom (botst niet met concept-, themafiche- of minicursus-slug). Check vóór aanmaken.

---

## Vaste blok-structuur

### Verplicht (vier blokken)

#### A. Frontmatter
```yaml
---
title: "<Leerstuk-titel — meestal de vraag voluit>"
description: "Leerstuk PO X.Y: <korte inhoud-indicatie>"
tags:
  - leerstuk
  - po-X.Y
  - cluster-<skelet-cluster-naam>
---
```

#### B. Intro-callout (verplicht)
Wrap in `<div class="no-print">...</div>` met blank lines errond:

```markdown
<div class="no-print">

> **Leerstuk — één vraag, helemaal doorgewerkt.** Voor verhaal en routekaart: [[leerpaden/X.Y|minicursus PO X.Y]]. Voor definitorische opzoek: zie wikilinks doorheen de tekst.

</div>
```

#### C. Antwoord in één blik (verplicht)
Direct na de intro: **1-3 zinnen** die de vraag beantwoorden. De lezer moet na het lezen van dit blok het kort-antwoord paraat hebben — de rest van het leerstuk is uitwerking en *onderbouwing*. Optioneel gevolgd door een beslisboom of compacte tabel die het antwoord visueel maakt.

#### D. Wettelijk fundament (verplicht, aan het einde)
Bundelt alle wetsverwijzingen op één plek:

```markdown
## Wettelijk fundament

- <Onderwerp>: <Wetbundel> <artikel-ref> [(eventuele toelichting)]
- ...
```

Geen letterlijke wettekst (te lang). Enkel artikel-pointers + één-zin context. Drempel-bedragen niet hardcoden — verwijs naar Cijferzakboekje.

---

### Verplicht (visualiteit)

Een leerstuk bevat **minstens twee** elementen uit deze lijst:

| Element | Wanneer | Voorbeeld |
|---|---|---|
| **Vergelijkingstabel** | Bij twee of meer opties / regimes | Drempels kleine groep vs kleine vennootschap |
| **Mock-jaarrekening** | Bij rapportering / opmaak / boekhoudkundige effecten | Vereenvoudigde Belgische balans **met officiële KB-WVV rubrieknummers** (II. immateriële, III. materiële, IV. financiële vaste activa, VI. voorraden, VII. vorderingen ≤ 1 jaar, IX. liquide middelen / IX. schulden ≤ 1 jaar; I-V voor eigen vermogen). Activa-tabel en passiva-tabel apart. Getallen die sluiten. Doorgewerkte balans-voor/na bij eliminaties of methode-toepassing |
| **Mermaid-diagram** | Bij groepsstructuur / proces / beslisboom | Moeder → dochter → JV → associate, met %-en |
| **Side-by-side scenario** | Bij "groep A wel/groep B niet" toets | Drie groepen met balanstotaal, omzet, werknemers + uitkomst-kolom |
| **T-rekening / boekingsschema** | Bij verwerking-vraag | **4-koloms tabel** `Debet · mln · Credit · mln` met optionele "Totaal"-rij om balanced-staat te tonen. ASCII-art code-blocks vermijden — niet responsive en niet styleable. Voorbeeld: zie boekingen in `hoe-consolideren.md` |
| **KaTeX-formule** | Bij wiskundig kern-element | Goodwill = aanschafprijs − aandeel-NEV |
| **Doorgewerkte voorbeeldcasus** | Verplicht voor "hoe"-leerstukken | Groep met 3 dochters, kringafbakening + methode-keuze stap voor stap |

**Pure-tekst leerstukken zijn een red flag.** Bij review: "kun je dit *zien*?" — zo niet, herwerken.

---

### Optioneel — "select what fits"

#### E. Doorgewerkte voorbeeldcasus
Concrete (mock) onderneming / groep met cijfers, doorheen de vraag heen gevoerd. Verplicht voor "hoe"-leerstukken; nuttig voor "wanneer"-leerstukken.

#### F. Valkuilen-blok (3 max)
Korte tegen-voorbeelden van wat de stagiair vaak fout doet. Niet uitputtend zoals in themafiche — leerstuk benadrukt de drie zwaarste valkuilen die uit de vraag-zelf voortkomen, niet alle valkuilen uit alle onderliggende concepten.

#### G. Verbinding met andere leerstukken
Korte sectie (3-5 bullets) "Wanneer je dit snapt, ga dan naar …" met wikilinks naar verwante leerstukken. Geeft de stagiair een natuurlijke vervolgrichting.

#### H. Doorklik naar concepten (web-only)
Wrap in `<div class="no-print">`. Lijst van atomaire concepten die in dit leerstuk genoemd zijn — voor wie het definitorisch detail wil opzoeken.

---

## Wikilink-regels

Leerstukken mogen linken naar:

| Target | Syntax | Wanneer |
|---|---|---|
| Andere leerstuk | `[[wie-moet-consolideren]]` | Verwijzing zonder dupliceren — eerder dan inhoud herhalen |
| Concept-fiche | `[[consolidatieverschil]]` | Voor definitorische opzoek-doorklik |
| Themafiche | `[[themafiches/consolidatie|Themafiche Consolidatie]]` | Voor de herhalings-zoom-uit |
| Minicursus | `[[leerpaden/1.4|minicursus PO 1.4]]` | In intro-callout en optioneel in afsluitsectie |

**Geen circulaire links**: een leerstuk wijst niet terug naar de minicursus waaruit hij oproept (de minicursus linkt al heen). Backlinks zijn render-laag-keuze.

**Concept-links spaarzaam**: vraag jezelf af "voegt dit toe?" — als de concept-fiche enkel hetzelfde herhaalt wat het leerstuk al uitlegt, laat de link weg.

---

## Wettekstreferenties — bundelregel

**Geen wetsartikel-nummers in lopende tekst.** Niet `(art. 3:22 e.v. WVV)` mid-zin. Wel: "De wet voorziet hier een vrijstelling voor groepen die klein genoeg blijven" + verwijzing in de "Wettelijk fundament"-sectie.

Uitzondering: een wetsartikel mág voorkomen in lopende tekst als het zélf het onderwerp is van een zin ("De drempels van art. 1:26 § 1 WVV zijn ook beslissend voor *consortia*"). Trip-vraag: "leest deze zin nog vlot uit?" — zo nee, verplaats naar voetsectie.

**Drempel-bedragen** komen uit het Cijferzakboekje — niet hardcoden. Schrijf "boven de drempel-cijfers in het Cijferzakboekje" en geef richting indien nodig ("orde van grootte: 250 werknemers · ~34 mln omzet · ~17 mln balans").

---

## Bron-traceerbaarheid (auteur-verantwoordelijkheid)

Geen confidence-iconen (📖/🔗/🤖) in de body — die zitten in concept-records. Maar:

- Geen claim zonder bron in het hoofd van de auteur
- Bij twijfel: herformuleren of weglaten — niet "⚠️"-labelen
- Bij feitelijke conflicten tussen concepten en wat je zou willen schrijven: stop en check de bron (RAG via `mcp__certificaid-rag__zoek_bronnen` of directe wettekst). Vertrouw nooit blind op een concept-record — die kan stale zijn

### Verplichte bron-verificatie via MCP-RAG (geen grep)

Voor élke harde claim — drempel, regel, timing, artikel-nummer, uitzondering — is verificatie via `mcp__certificaid-rag__zoek_bronnen` verplicht vóór publicatie. **Greppen door `resources/bronnen/` is geen vervanger** (mist context, vindt verouderde versies, structuur onzichtbaar). De RAG dekt wettekst + KB's + CBN-adviezen + IFRS-verordening; gebruik filter `bron_rollen=["wettekst"]` voor enkel de wet.

Voor snelheid: `rerank=false` (default) volstaat bij ruime zoekvragen. Zet `rerank=true` enkel wanneer je preciseer-kritisch zoekt naar één specifieke artikel-tekst of bij conflictsituaties.

### "Lees de hele paragraaf"-regel

Een RAG-hit toont **één chunk** van een paragraaf — niet de hele wetsbepaling. Zodra je een wetsregel samenvat:

- Identificeer alle alinea's van dezelfde paragraaf (klikbare context-pad bovenaan elke chunk in RAG-resultaat)
- Lees ze allemaal; controleer of ze elk een aparte regel bevatten
- Vermeld de aspecten samen of expliciteer welk aspect je behandelt — anders lijkt je samenvatting alsof het andere aspect niet bestaat

Voorbeeld-fout uit de POC-ronde van consolidatie: art. 1:26 § 2 heeft twee alinea's (meetdatum + tweejaars-regel). De eerste POC noemde alleen alinea 2, waardoor het leek alsof er geen meetdatum-regel was. Beide alinea's horen samen in de tekst.

### Concept-records ≠ waarheid

Concept-records zijn een snelle ingangspoort tot een onderwerp (welke begrippen leven hier, welke voorbeelden bestaan), maar **nooit een eindbron**. De POC-ronde vond:

- `consolidatieverplichting` verwees voor drempels naar art. 1:24 § 6 i.p.v. correct art. 1:26 § 1
- Drempel-bedragen mogelijk verouderd (pre-KB-2024)
- Overlappende uitleg over controle in drie records, telkens iets anders gefraseerd

Voor elke claim uit een concept-record: bevestig via wetsbron of CBN-advies vóór je hem in een leerstuk overneemt.

---

## Stilistische regels

1. **Eigen woorden** — niet kopiëren uit concept-records. Herformuleren is gewenst
2. **Concretiseer voortdurend** — elke abstract idee krijgt een voorbeeld of een visueel element
3. **Toon, schrijf niet alleen** — twee visuele elementen verplicht
4. **Vraag-antwoord-strakheid** — elke sectie dient de hoofdvraag van het leerstuk; sub-vragen mogen, maar geen uitweidingen
4b. **Achtergrond/aside in blockquote, niet in sub-sectie**. Een sub-sectie (h5/h6) signaleert een stap in de pedagogische hoofdverhaallijn (situatie · probleem · oplossing · valkuil). Achtergrondinfo die de hoofdlijn even onderbreekt voor context (bv. "waarom dit cijfer ≠ dat cijfer?", historische noot, een vergelijking met een ander stelsel) hoort in een blockquote met vetgedrukte intro. Vuistregel: kun je de paragraaf weglaten zonder dat de stappen-keten breekt? → blockquote. Verbreekt het weglaten de logische opbouw? → sub-sectie.
5. **Geen examen-radar** — die hoort in minicursus + themafiche
6. **Geen confidence-iconen** in de body
7. **Geen taken-codes** of interne field-namen (ITAA-jargon zoals "TDK" → voluit of vermijden)
8. **Geen "ik" / "wij"** — gebruik tweede persoon ("je") of imperatief
9. **Nederlandstalige terminologie** — geen onnodige Engelse termen (`margin` → `marge`, `goodwill` is OK want vaste term, `one-line consolidation` mag enkel met expliciete Nederlandse glossing). Bij twijfel: gebruik de Nederlandse term zoals in CBN-adviezen of WVV-tekst
10. **Abstracte stellingen krijgen een concreet mini-voorbeeld**. Beats als "leg X uit" of "noem nuance Y" produceren vage prose tenzij ze concretiseringsaanwijzing bevatten. Schrijfregel voor beats: koppel elke abstracte instructie aan een concretisering — een getallen-voorbeeld, een tegen-voorbeeld, "noem 3 voorbeelden van Z". Voorbeeld: "20 % is vermoeden, geen hard recht" → vaag. Beter: "20 % is vermoeden, geen hard recht — illustreer met '18 % maar toch RvB-controle = notabele invloed'". Voorkomt pedagogisch vlakke alinea's bij re-render

---

## Pre-publicatie-checklist

- [ ] Frontmatter compleet (title + description + tags incl. `leerstuk` + `po-X.Y` + `cluster-…`)
- [ ] Intro-callout in `<div class="no-print">` met blank lines errond
- [ ] "Antwoord in één blik" binnen de eerste 200 woorden
- [ ] Minstens twee visuele elementen (tabel / mermaid / KaTeX / mock-JR / doorgewerkte casus)
- [ ] "Wettelijk fundament"-sectie aan het einde
- [ ] Geen wetsartikel-nummers in lopende tekst (alleen in voetsectie)
- [ ] Geen drempels hardcoded (Cijferzakboekje-pointer)
- [ ] Wikilinks gechekt: bestaan de targets? (concepten of andere leerstukken)
- [ ] Slug uniek in `content/`-boom
- [ ] Lengte binnen budget (800-2000 woorden, of tot ~2500 voor "hoe"-leerstukken)
- [ ] **Elke wetsverwijzing geverifieerd via `zoek_bronnen`** (geen grep, geen training-only). Specifiek voor artikel-nummers: ik heb de RAG-hit gezien, niet alleen "ik denk dat dit klopt"
- [ ] **Volledige paragraaf gelezen, niet alleen de chunk-hit** — heeft de paragraaf meer alinea's die elk een eigen regel bevatten? Beide vermelden of expliciet zeggen welke je behandelt
- [ ] **Geen onnodige Engelse termen** in body of tabellen (margin, group, single-line, etc. → Nederlands gebruiken)
- [ ] Cmd+P → PDF preview oogt correct
