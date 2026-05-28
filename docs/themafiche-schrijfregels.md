# Themafiche — schrijfregels

**Voor**: een Sonnet-agent of mens die een themafiche schrijft voor een cluster uit de granulariteit-skelet.
**Canonieke beslissing**: [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md).
**Mockup-referentie**: [`content/experiment/synthese-consolidatie-v1.md`](../content/experiment/synthese-consolidatie-v1.md) (cluster `consolidatie`, PO 1.4). Verplaatsen naar `content/themafiches/<cluster>.md` zodra structuur volledig bevroren.

---

## Doel

Een themafiche is een **kapstok-document op één of twee A4-pagina's** dat alles van een cluster (uit [`docs/granulariteit-skelet.md`](granulariteit-skelet.md)) samenvat. Bedoeld als:
- **Herhalings-tool** in de week vóór het examen (snel doorlopen wat al gezien is)
- **Visueel oriëntatie-anker** voor wie het terrein wil overzien zonder details
- **Printbaar referentiekaart** (Cmd+P → PDF werkt out-of-the-box via `@media print` in `quartz-custom/styles/custom.scss`)

De themafiche is **niet** bedoeld om voor het eerst te leren — daarvoor is de minicursus + concept-fiches. Themafiche = dichtheid en overzicht boven alles.

## Doelgroep en toon

- **Doelgroep**: zelfde als minicursus (ITAA-stagiair). Maar in de gebruikssituatie heeft de kandidaat de stof al gezien — ze zoekt herinnering, vergelijking, valkuil-radar.
- **Toon**: schematisch, telegram-stijl waar mogelijk. Volledige zinnen alleen waar noodzakelijk. **Tabellen, bullets, formules, beslisbomen** krijgen voorrang boven proza.
- **Lengte-richtlijn**: 600-1200 woorden, 1-2 A4 als PDF.

## Vaste structuur — zeven blokken

Een themafiche heeft **deze zeven blokken in deze volgorde**. Niet elk blok is altijd zinvol — bv. een cluster zonder regel-keuze heeft geen beslisboom; sla over indien niet van toepassing.

### 1. Take-away (wat je écht moet weten)

- 4-6 bullets met de essentie. Elk bullet ≤ 2 zinnen.
- Suggested aanpak: één bullet per "vraag-categorie" — wat? wanneer? hoe? wat als? wat valt op?
- Géén verhalend proza in dit blok — dat hoort in de minicursus.

### 2. Vergelijkingstabel

Verplicht voor clusters die een onderscheid bevatten (drie methodes, twee regimes, twee perspectieven). Voorbeelden:
- Consolidatie: 3 methodes × 8 dimensies
- Aangifte PB vs VenB: 2 regimes × N kenmerken
- ISA vs ISRE vs ISRS: 3 opdrachttypes × N attributes

- **Belangrijk**: laatste rij of expliciete callout voor **B-GAAP ↔ IFRS-verschillen** waar van toepassing (klassieke examen-valkuil)

### 3. Beslisboom (mermaid)

Voor clusters met een procedurele beslissing ("moet ik consolideren?", "welke aangifte?", "welk regime?", "welke methode?"). Mermaid `flowchart TD`.

- Compact houden — ≤ 10 nodes, ≤ 12 edges
- Print-CSS schaalt mermaid-SVG automatisch naar max 65% breedte / 9cm hoogte
- Skip dit blok voor clusters zonder beslis-aspect (puur beschrijvend cluster)

### 4. Drempels & formules

- **Drempel-tabellen** voor numerieke randen (consolidatieplicht, KMO-criteria, materialiteit, etc.). Aparte kolom voor de drempel + de regel-bron.
- **Formules in KaTeX** voor wiskundige relaties: `$$ \text{Goodwill} = ... $$`.
- ⚠️-callouts voor uitzonderingen op de regel ("beursgenoteerd altijd plichtig").

### 5. Klassieke valkuilen (examen-radar)

Tabel met kolommen: `Valkuil` · `Wat klopt er niet` · `Wat klopt wél`. Bron: `inhoud.valkuilen[]` van het hoofd-record van het cluster + andere records waar relevante valkuilen leven.

- 4-6 rijen typisch
- Geen jurisprudentie-citaten — alleen de operationele valkuil

### 6. Verbinding met examen (PO X.Y)

Intro-paragraaf die de PO-structuur duidt (hoeveel taken, welke kenniselementen). Dan **per taak** een sub-tabel:

```markdown
**Taak X.Y.taak.N**: <verbatim taak-tekst>

| Doelstelling | Gedekt door |
|---|---|
| 1. <doelstelling-tekst verbatim> | → cluster **<andere-cluster>** OF synthese §X + [[wikilink]] |
| ...
```

- Voor doelstellingen die door een ander cluster gedekt worden: `→ cluster **<naam>**` (geen wikilink, want het is een themafiche-naam)
- Voor doelstellingen die door deze themafiche gedekt worden: verwijs naar sectie-nummers (`§1`, `§2`, etc.) + relevante records
- **Belangrijk**: vermeld expliciet de "operationele vaardigheden specifiek voor [cluster]" die niet in de doelstellingenlijst staan — die leven in `accountant_perspectieven` van de records. Verwijs naar §7 (concept-index) voor doorklik.

**Geen kenniselementen-tabel** in de themafiche (te veel detail). Wel impliciet door de mappings in §1-§5.

### 7. Concept-index — verdieping per record

Web-only sectie (wordt verborgen in print via `<div class="no-print">`):

```markdown
<div class="no-print">

## 7. Concept-index — verdieping per record

> Klik door voor de volledige fiche met bronnen, voorbeelden, valkuilen en *accountant_perspectieven* (waar de concrete acties per rol leven).

**<Categorie 1>**
- [[concept-id]] — één-zin omschrijving
- ...

**<Categorie 2>**
- ...

</div>
```

- Groeperingen volgen de natuurlijke functionele groepen van het cluster (Scope / Methodes / Verrichtingen / Opmaak — zie consolidatie-mockup voor referentie)
- Elke wikilink + één-zin-omschrijving die de rol in het cluster verduidelijkt
- Géén overlap met de tekst in §6 — §6 is de examen-mapping, §7 is de "zoek-een-concept"-index

## Frontmatter (canoniek)

```yaml
---
title: "Themafiche — <Cluster-naam>"
description: "Themafiche voor cluster <cluster> (PO X.Y): van plicht tot opmaak in één overzicht"
tags:
  - themafiche
  - po-X-Y
  - cluster-<cluster-naam>
---
```

## Stilistische regels

1. **Dichtheid > verhaal.** Themafiche is geen leesdocument; het is een ref-card.
2. **KaTeX voor formules** — wordt automatisch gerenderd door Quartz.
3. **Mermaid voor diagrammen** — gebruik `flowchart TD` voor beslisbomen.
4. **Tabellen op volle breedte** — gegarandeerd door `quartz-custom/styles/custom.scss` (`.table-container > table { width: 100% }`).
5. **`<div class="no-print">`** voor web-only secties. Blank lines errond — anders parseet markdown niet binnen de div.
6. **Geen interne field-namen** in de tekst zelf (`accountant_perspectieven`, `linked_anchors` etc.). Wel in §7 inleiding als nuttige hint voor de kandidaat om door te klikken.
7. **B-GAAP ↔ IFRS-verschillen** consequent expliciteren — examen-klassieker.
8. **Bron-citaten** alleen in §4 (Drempels & formules) en optioneel als ref in §1 (Take-away). Niet doorheen het hele document — anders verandert de fiche in een commentaarboek.

## Pre-publicatie-checklist

- [ ] Frontmatter compleet (title + description + tags incl. `cluster-<naam>`)
- [ ] Alle wikilinks wijzen naar bestaande records
- [ ] Zeven blokken aanwezig in juiste volgorde (skip alleen als niet van toepassing — gemotiveerd in commit-message)
- [ ] §7 in `<div class="no-print">` met blank lines errond
- [ ] Mermaid-diagram ≤ 10 nodes, print-vriendelijk
- [ ] Tabel-headers in `<th>` (markdown's `|---|` syntax doet dit automatisch)
- [ ] Cmd+P → PDF preview oogt correct (geen lege pagina, geen overflow)
- [ ] Footer met status-disclaimer
