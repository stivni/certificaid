# Themafiche — schrijfregels v2

**Voor**: een Opus/Sonnet-agent of mens die een themafiche schrijft voor een sub-cluster.
**Canoniek**: [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md).
**Gold-standard mockups** (allemaal in `content/themafiches/`): `consolidatie` · `kostprijsmethoden` · `jaarrekeninganalyse-aanpak` · `ratio-families` · `kasstroom-analyse` · `continuiteit-en-diagnose` · `registratierechten` · `successierechten-en-erfrecht` · `successieplanning`.

---

## Doel

Een themafiche is een **kapstok-document op 1-2 A4** dat alles van een sub-cluster samenvat — visueel dominant, tekst minimaal. Bedoeld als:
- **Herhalings-tool** in de week vóór het examen ("hoe zat die formule ook al weer?")
- **Printbaar referentiekaart** (Cmd+P → PDF werkt out-of-the-box)
- **Snelle scan** naar specifieke valkuilen / formules / vergelijkingen

**De themafiche is NIET** bedoeld voor wie de stof voor het eerst leert. Daarvoor zijn de [minicursus](minicursus-schrijfregels.md) (verhaal + routekaart) en de losse concept-fiches (diepgang).

---

## Zeven kern-principes (vastgelegd 2026-05-29 sparring)

1. **Granulariteit**: 1 themafiche per **sub-cluster** (functionele groepering binnen een skelet-cluster), niet per skelet-cluster of per record. Typische PO heeft 2-5 themafiches.
2. **Doelgebruik**: pure herhaling — veronderstelt herkenning, geen uitleg. Termen als "NBK", "ROU-actief", "CCC" mogen onverklaard.
3. **Lengte-budget**: streef 1 A4 print; toleereer 2 A4 voor zware sub-clusters. Drie A4 → splits verder of herzie sub-cluster.
4. **Blokken**: "select what fits". Drie verplicht (take-away · valkuilen · doorklik), de rest optioneel afhankelijk van stof.
5. **Geen examen-radar** in de themafiche — alleen ⚠️ valkuilen.
6. **Cross-PO**: één gedeelde themafiche per sub-cluster met multiple PO-tags in frontmatter. Niet dupliceren per PO.
7. **Geen wetsverwijzingen** — pointers volstaan ("WVV art. 5:153"); geen letterlijke wettekst.

---

## Doelgroep en toon

- **Doelgroep**: ITAA-stagiair die de stof al kent.
- **Toon**: schematisch, telegram-stijl. Volledige zinnen alleen waar onvermijdelijk. **Tabellen, formules, beslisbomen** zijn de hoofdactiva.
- **Geen** "ik" / "wij". Impersonal of imperatief.
- **Tarief-bandbreedtes**: geef richtwaarden + "Cijferzakboekje bij examen raadplegen" als pointer. Géén harde tarieven die kunnen verschuiven.

---

## Vaste blok-structuur

### Verplicht (drie blokken)

#### A. Intro-callout (verplicht, web-only)
Wrap in `<div class="no-print">...</div>` met blank lines errond:

```markdown
<div class="no-print">

> **Themafiche — kapstok voor herhaling.** [Eén zin context]. Voor verhaal en routekaart: [[leerpaden/X.Y|minicursus PO X.Y]].

</div>
```

#### B. Take-away (verplicht)
3-5 **insight-bullets** (geen herhaling van wat in tabellen volgt). Mikpunt: scherpe inzichten die niet uit een tabel af te lezen zijn.

✅ Goed: *"Géén methode is intrinsiek juist — keuze volgt het doel"*
❌ Slecht: *"Vier methodes worden besproken"*

#### C. Valkuilen-tabel ⚠️ (verplicht)
3-koloms tabel: `Valkuil · Wat klopt er niet · Wat klopt wél`. 4-6 rijen. Bron: `inhoud.valkuilen[]` van records in sub-cluster.

#### D. Doorklik (verplicht, web-only)
Wrap in `<div class="no-print">` met blank lines:
- Lijst losse concept-fiches gegroepeerd per functie
- Verwijzing naar verwante themafiches

---

### Optioneel — "select what fits"

#### E. Vergelijkingsmatrix
Voor sub-clusters met keuze-aspect (methodes, regimes, varianten). Kolommen = opties, rijen = dimensies (4-8 rijen typisch). Laatste rij vaak voor B-GAAP↔IFRS-verschil of gewestelijke variatie.

#### F. Beslisboom (mermaid `flowchart TD`)
Voor sub-clusters met procedure / "welke X bij Y"-vraag. Compact: ≤ 10 nodes. Print-CSS schaalt mermaid-SVG; voor lange labels gebruik `<br/>` in node-tekst.

#### G. Formules (KaTeX)
Voor sub-clusters met wiskundig kerngeld. Inline `$...$` of display `$$...$$`. Beperk tot kern-formules; afgeleide varianten kunnen weg.

#### H. Schema / flow
Voor processen of opbouw-structuren (bv. masterbudget-flow, DuPont-decompositie). Mermaid of HTML/CSS.

#### I. Tarief-tabel
Voor fiscale sub-clusters met bandbreedtes per regime. Eind altijd met "Concrete cijfers: **Cijferzakboekje bij examen**".

---

## Frontmatter (canoniek)

```yaml
---
title: "Themafiche — <Sub-cluster naam>"
description: "Themafiche voor sub-cluster <naam> (PO X.Y): <korte inhoud-indicatie>"
tags:
  - themafiche
  - po-X.Y       # bij cross-PO: meerdere po-tags toevoegen
  - cluster-<skelet-cluster-naam>
---
```

---

## Footer (verplicht)

```markdown
---

*Themafiche afgeleid uit cluster <skelet-cluster> (PO X.Y). Status: voorgesteld.*
```

---

## Stilistische regels

1. **Dichtheid > verhaal** — themafiche is geen leesdocument
2. **KaTeX voor formules**; **mermaid voor diagrammen**
3. **Tabellen volle breedte** — gegarandeerd door `quartz-custom/styles/custom.scss`
4. **`<div class="no-print">`** voor web-only secties — blank lines errond verplicht
5. **Géén confidence-iconen** (📖/🔗/🤖) in themafiche — die horen in concept-records
6. **Géén taken-codes** of interne field-namen
7. **B-GAAP ↔ IFRS-verschillen** consequent expliciteren waar relevant (fiscale fiches: hetzelfde voor gewestelijke variatie Vl/Bru/Wal)
8. **Cross-references** tussen themafiches in §Doorklik

---

## Granulariteits-besluit per cluster (canoniek)

| Skelet-cluster | Sub-clusters / themafiches | PO |
|---|---|---|
| consolidatie | 1 (consolidatie) | 1.4 |
| financiele-analyse | 4 (aanpak · ratio-families · kasstroom · continuiteit-diagnose) | 1.3 + 1.9 |
| analytische-boekhouding (1.8) | 3 (kostprijsmethoden · break-even & marginale · budget & variantie) | 1.8 |
| registratie-en-successierechten | 3 (registratierechten · successierechten-erfrecht · successieplanning) | 2.6 |
| boekhouding (1.1 + 1.2) | TBD (4-5 vermoedelijk) | 1.1 + 1.2 |
| ifrs-rapportering | TBD (2-3 vermoedelijk) | 1.5 |
| controle-opdracht | TBD (3-4 vermoedelijk) | 1.6 |
| interne-controle | TBD (3-4 vermoedelijk) | 1.7 |
| personenbelasting | TBD (4-5 vermoedelijk) | 2.2 |
| vennootschapsbelasting | TBD (4-5 vermoedelijk) | 2.3 |
| btw | TBD (4-5 vermoedelijk) | 2.4 |
| fiscale-procedure | TBD (4-5 vermoedelijk) | 2.5 |
| ... | ... | ... |

---

## Pre-publicatie-checklist

- [ ] Frontmatter compleet (title + description + tags incl. `cluster-<naam>`)
- [ ] Intro-blockquote in `<div class="no-print">` met blank lines errond
- [ ] Alle wikilinks wijzen naar bestaande records of themafiches
- [ ] Verplichte blokken aanwezig (intro · take-away · valkuilen · doorklik)
- [ ] Optionele blokken aanwezig waar inhoud het vereist
- [ ] Geen wetsverwijzingen letterlijk (pointers OK)
- [ ] Geen examen-radar
- [ ] Tarieven via Cijferzakboekje-pointer (niet hardcoded waar mogelijk)
- [ ] Footer met status-disclaimer
- [ ] Cmd+P → PDF preview oogt correct (geen lege pagina, geen overflow)
