# Samenvatting — schrijfregels v1

**Voor**: een Opus/Sonnet-agent of mens die een PO-samenvatting schrijft.
**Canoniek**: [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md). Vervangt `docs/themafiche-schrijfregels.md` (gearchiveerd onder `docs/archive/`).
**Gold-standard**: PO 1.4 — `content/leerpaden/1-4/samenvatting.md`.

---

## Doel

Een samenvatting is een **kapstok-document op 2-4 A4** dat het hele PO samenvat — visueel-dominant, tekst minimaal. Bedoeld als:
- **Herhalings-tool** in de week vóór het examen ("hoe zat die formule ook al weer?")
- **Printbare referentiekaart** (Cmd+P → PDF werkt out-of-the-box)
- **Snelle scan** naar specifieke valkuilen / formules / vergelijkingen

**De samenvatting is NIET** bedoeld voor wie de stof voor het eerst leert. Daarvoor zijn de [minicursus](minicursus-schrijfregels.md) (verhaal + routekaart) en de leerstukken (één vraag, helemaal doorgewerkt).

---

## Zeven kern-principes

1. **Granulariteit**: één samenvatting per **PO**, niet per cluster. Andere granulariteit alleen na expliciete beslissing in ADR (uitzonderlijk).
2. **Doelgebruik**: pure herhaling — veronderstelt herkenning, geen uitleg. Termen als "NBK", "ROU-actief", "CCC" mogen onverklaard.
3. **Lengte-budget**: streef 2-3 A4 print; toleereer 4 A4 voor zware PO's. 5+ A4 → overweeg PO-splitsing of herwerk.
4. **Vaste blok-structuur**: vier verplicht (intro-callout · take-away · valkuilen · verdieping), 0-3 optionele in opgegeven volgorde.
5. **Géén examen-radar in fragmenten** — alleen ⚠️ valkuilen. (Examen-radar leeft in de minicursus § "Examen-radar" + voorbeeldexamen-pagina.)
6. **Géén cross-PO refs in lopende tekst** — doorklik blijft binnen PO. Cross-PO concepten op concept-niveau staan vrij.
7. **Géén wetsverwijzingen letterlijk** — pointers volstaan ("WVV art. 5:153"); geen letterlijke wettekst (die is in ITAA-LEX bij examen beschikbaar).

---

## Doelgroep en toon

- **Doelgroep**: ITAA-stagiair die de stof al kent.
- **Toon**: schematisch, telegram-stijl. Volledige zinnen alleen waar onvermijdelijk. **Tabellen, formules, beslisbomen** zijn de hoofdactiva.
- **Geen** "ik" / "wij". Impersonal of imperatief.
- **Tarief-bandbreedtes**: geef richtwaarden + "Cijferzakboekje bij examen raadplegen" als pointer. Géén harde tarieven die kunnen verschuiven.

---

## Vaste blok-structuur

### Verplicht (vier blokken)

#### A. Intro-callout (web-only)
Wrap in `<div class="no-print">...</div>` met blank lines errond:

```markdown
<div class="no-print">

> **Samenvatting — kapstok voor herhaling.** [Eén zin context]. Voor verhaal en routekaart: [[leerpaden/X-Y|minicursus PO X.Y]].

</div>
```

#### B. Take-away
3-6 **insight-bullets** (geen herhaling van wat in tabellen volgt). Mikpunt: scherpe inzichten die niet uit een tabel af te lezen zijn.

✅ Goed: *"Géén methode is intrinsiek juist — keuze volgt het doel"*
❌ Slecht: *"Vier methodes worden besproken"*

#### C. Valkuilen ⚠️
Twee mogelijke vormen — kies wat best past:

- **Tabel** (3-koloms): `Valkuil · Wat klopt er niet · Wat klopt wél`. 4-6 rijen. Bron: `inhoud.valkuilen[]` van records.
- **Bullets**: `⚠️ **<valkuil>**: <korte uitleg>`. Voor PO's met minder structurele valkuilen.

#### D. Verdieping (web-only)
Wrap in `<div class="no-print">`. Twee sub-secties:
- **Leerstukken — voor pedagogische opfris**: lijst leerstukken (binnen PO) met `[[<slug>]]` + één hint per leerstuk
- **Concept-fiches — voor definitorisch detail**: per functionele groep een bullet met `[[concept-1]] · [[concept-2]] · ...`

---

### Optioneel — "select what fits"

#### E. Vergelijkingsmatrix
Voor PO's met keuze-aspect (methodes, regimes, varianten). Kolommen = opties, rijen = dimensies (4-8 rijen typisch). Laatste rij vaak voor B-GAAP↔IFRS-verschil of gewestelijke variatie.

#### F. Beslisboom (mermaid)
Voor PO's met procedure / "welke X bij Y"-vraag. **Mermaid horizontaal (`flowchart LR`)** voor stappenplannen; **`flowchart TD`** alleen voor hiërarchische bomen of beslisbomen met ja/nee-takken. Compact: ≤ 10 nodes. Print-CSS schaalt mermaid-SVG.

#### G. Formules (KaTeX) + drempels
Voor PO's met wiskundig kerngeld (kostprijs, ratios, drempels). Inline `$...$` of display `$$...$$`. Beperk tot kern-formules; afgeleide varianten kunnen weg. Combineer met tabel-inline voor drempels indien relevant.

#### H. Verbinding met examen
Voor PO's waar het examen-patroon een specifieke observatie verdient (bv. "examen toetst zelden volle berekening, wél fragmenten"). 2-3 paragrafen telegram-stijl + pointer naar `voorbeeldexamens/po-X-Y`.

---

## Frontmatter (canoniek)

```yaml
---
title: "Samenvatting PO X.Y — <titel-PO>"
description: "PO-samenvatting (geheugen-kapstok): <korte inhoud-indicatie>"
explorer_title: "7. Samenvatting"   # of de volgnummer die volgt op leerstukken + oefening
tags:
  - samenvatting
  - po-X.Y
---
```

---

## Footer

```markdown
---

*Samenvatting PO X.Y. Status: <voorgesteld | gecureerd>.*
```

---

## Stilistische regels

1. **Dichtheid > verhaal** — samenvatting is geen leesdocument
2. **KaTeX voor formules**; **mermaid voor diagrammen**
3. **Tabellen volle breedte** — gegarandeerd door `quartz-custom/styles/custom.scss`
4. **`<div class="no-print">`** voor web-only secties — blank lines errond verplicht
5. **Géén confidence-iconen** (📖/🔗/🤖) — die horen in concept-records
6. **Géén taken-codes** of interne field-namen
7. **B-GAAP ↔ IFRS-verschillen** consequent expliciteren waar relevant (fiscale PO's: hetzelfde voor gewestelijke variatie Vl/Bru/Wal)
8. **Cross-references** uitsluitend binnen het PO (leerstukken + concept-fiches). Wikilinks naar andere PO's vermijden.

---

## Pre-publicatie-checklist

- [ ] Frontmatter compleet (title + description + explorer_title + tags `samenvatting` + `po-X.Y`)
- [ ] Intro-callout in `<div class="no-print">` met blank lines errond
- [ ] Alle wikilinks wijzen naar bestaande records of leerstukken
- [ ] Vier verplichte blokken aanwezig (intro · take-away · valkuilen · verdieping)
- [ ] Optionele blokken aanwezig waar inhoud het vereist
- [ ] Geen wetsverwijzingen letterlijk (pointers OK)
- [ ] Tarieven via Cijferzakboekje-pointer (niet hardcoded waar mogelijk)
- [ ] Print-cap gerespecteerd: 2-4 A4 (visueel inschatten + Cmd+P preview)
- [ ] Footer met status-disclaimer
- [ ] Geen cross-PO wikilinks in lopende tekst

---

## Migratie uit themafiches

Voor PO's die meerdere cluster-themafiches hebben (zoals PO 1.8: 4 themafiches): merge tot één samenvatting volgens dit schema. Tactisch:

1. **Take-away combineren**: top 5-6 insights over alle themafiches heen
2. **Vergelijkingsmatrices mergen**: één per PO indien mogelijk; anders behouden als twee aparte blokken
3. **Beslisboom**: één beslisboom per PO; multiple → herzien voor PO-overzichts-flow
4. **Formules + drempels** consolideren in één blok
5. **Valkuilen**: ALLE valkuilen, geordend per relevantie (max 8 — kandidaat-splitsen indien meer)
6. **Verdieping**: doorklik naar alle leerstukken + concept-fiches van het PO

Bestaande themafiche-md's verwijderen na merge (zie ADR-039 § "Migratiepad").
