# Minicursus — schrijfregels

**Voor**: een Sonnet-agent of mens die een minicursus schrijft voor een programmaonderdeel (PO).
**Canonieke beslissing**: [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md).
**Mockup-referentie**: [`content/leerpaden/1.4.md`](../content/leerpaden/1.4.md) (PO 1.4 — Geconsolideerde jaarrekening).

---

## Doel

Een minicursus is een PO-niveau studiedocument dat de kandidaat-gecertificeerd-accountant:
- het *verhaal* van het vak geeft (waarom dit vak, hoe past het in het bredere examenprogramma)
- de *taak* ontrafelt (wat moet de kandidaat kunnen, per rol)
- een *leesroute* aanbiedt (in welke volgorde naar de concept-fiches en themafiche(s))
- een *examen-radar* geeft (wat is in de praktijk bevraagd)

De minicursus *verwijst* naar concept-fiches en themafiches — ze lijfen die niet in.

## Doelgroep en toon

- **Doelgroep**: ITAA-stagiair (Gecertificeerd Accountant of Gecertificeerd Belastingadviseur). Heeft boekhoudkundige en fiscale basiskennis, is geen jurist, mag geen wetteksten uit het hoofd kennen (heeft ITAA-LEX bij examen).
- **Toon**: kandidaat-gericht. Schrijf in de tweede persoon ("jij die zich voorbereidt", "wat je moet kunnen") of impersoonlijk ("de kandidaat", "een accountant die"). Vermijd "we" / "ik" / project-jargon.
- **Vermijden**:
  - Interne field-namen: `accountant_perspectieven`, `inhoud.kern.definitie`, `linked_anchors`
  - Codes uit programma.json: `1.4.taak.1.doel.4` (gebruik wel verbatim de tekst van de doelstelling)
  - Document-type-jargon: "cluster-synthese", "scope-records", "ankers"
  - Format-jargon: "wikilink", "frontmatter"

## Vaste structuur — zes secties

Een minicursus heeft **deze zes secties in deze volgorde**:

### 1. Waarom dit vak?

- Eén of twee inleidende paragrafen die het bestaansrecht van het vak duiden — wat onderscheidt deze stof van andere vakken?
- **Subsection ### Hoe past dit in het bredere programma?** met tabel:
  - Kolommen: `Andere PO` · `Relatie tot dit vak`
  - 3-5 rijen voor de meest verwante PO's
  - Voor elke andere PO: een zin die de inhoudelijke relatie beschrijft (overlap, voorkennis, raakvlak, contrast)

### 2. Wat is dit vak?

- **Geen** tussentitel als "(het verhaal in vijf paragrafen)" of soortgelijk
- Vijf H3-sub-secties met doorlopend proza. Suggested H3-templates:
  - `### Het probleem` — wat is de praktische uitdaging die het vak adresseert?
  - `### De oplossing` — hoe biedt het vak het antwoord?
  - `### Het [plichten-spel / werkingsveld / wettelijk kader / etc.]` — wat zijn de juridische randen?
  - `### Drie [technieken / werkstromen / hoofdvarianten]` — wat zijn de centrale methodes?
  - `### Wat doet de accountant hier?` — welke rollen kruisen elkaar?
- Elke H3-sectie is 3-5 zinnen. Verbonden lopend proza, geen bullet-lijsten.
- Sluit de "Wat doet de accountant hier?"-sectie af met: *"In elke concept-fiche vind je per rol concrete acties die de accountant uitvoert."*

### 3. Wat moet je kunnen?

- **Citaat-blok bovenaan** met de hoofdtaak verbatim uit `programma.json`:
  ```markdown
  > *Opstellen van de individuele en geconsolideerde jaarrekening*
  ```
- Intro-paragraaf die het onderscheid **Kern** vs **Rakend** introduceert.
- **Sub-sectie `### De kern — <korte beschrijving>`** met per accountant-rol een bullet-lijst:
  - **Als boekhouder:** [bullets met `[[concept-id|verb fragment]]` of `[[concept-id]]`]
  - **Als commissaris of bedrijfsrevisor:** [...]
  - **Als adviseur:** [...]
  - Bullets zijn vol-zin-of-fragment in mensentaal, niet schema-uittreksels. Bron: `accountant_perspectieven.rollen[].elementen[]` van de relevante records.
  - Alleen rollen vermelden die werkelijk in de records leven. Skip bv. "adviseur" als geen enkel relevante record een advies-rol bevat.
- **Sub-sectie `### Rakend — <korte beschrijving>`** voor doelstellingen die gedeeld zijn met andere PO's:
  - Eén paragraaf die de gedeelde stof situeert
  - Bullet-lijst van doorklik-minicursussen: `- **Minicursus PO X.Y — <thema>** *(nog te maken)*` indien niet bestaand, anders directe wikilink
- **Sub-sectie `### Wat je daarvoor moet kennen`** als verzamelplek voor:
  - Records die niet via een rol-actie in "De kern" zijn genoemd. Groepeer onder vetgedrukte sub-headers ("Het hoofdbegrip", "De scope-vraag", "De drie methodes", "Verrichtingen en mutaties", "Wettelijke kaders")
  - Wettelijke kaders als context, met expliciete vermelding "geen aparte fiches — ze zitten verweven in de records"

**Geen aparte officiële-doelstellingen-tabel.** De doelstellingen zijn impliciet gedekt door Kern + Rakend + Wat je moet kennen. Dubbele info vermijden.

### 4. Studie-aanpak

**Studie-volgorde voor de kandidaat**: (1) deze minicursus eerst — verhaal + routekaart; (2) de concept-fiches in de leesroute hieronder voor de diepgang; (3) themafiche later als opfrissing wanneer de stof gezien is. Themafiches zijn complementair, geen onderdeel van de leesroute zelf.

- **Sub-sectie `### Leesroute door de fiches (X stappen)`** — genummerde lijst van 4-5 stappen, **uitsluitend door concept-fiches** (geen themafiche-stap):
  - Begint met de wikilink naar de fundament-fiches
  - Bevat een korte rationale-zin ("zonder de plicht en de kring is alles theoretisch")
  - Eindigt logischerwijs met de fiches die op examen het vaakst getoetst worden of de outputs van het proces
- **Sub-sectie `### Voor de herhaling — themafiche`** — start met deze formulering:
  > Wanneer je de stof grondig gezien hebt en het examen nadert, gebruik je een **themafiche** als opfrissingsdocument. Een themafiche is een kapstok op één pagina (printbaar als PDF) die alles van een onderwerp samenvat: vergelijkingstabel, beslisboom, formules, klassieke valkuilen. Niet bedoeld om voor het eerst te leren.
- Daarna een tabel met kolommen `Themafiche` · `Rol voor dit vak` (Kern / Vereist / Raakvlak). Themafiches die nog niet bestaan: markeer met `` `Themafiche <naam>` *(nog te maken)* ``.

### 5. Examen-radar — wat is in de praktijk al bevraagd?

- Intro-paragraaf met N (aantal unieke vraag-eenheden) en bron-examens.
- Tabel met kolommen: `Onderwerp` · `Hoe vaak?` · `Type vraag` · `Centraal concept` (wikilink).
- Onder de tabel: één paragraaf met patroon-observatie ("examen toetst niet X maar Y").
- Eindigen met doorklik: `→ De volledige vragen met uitgewerkte modelantwoorden vind je op de [voorbeeldexamen-pagina PO X.Y](../voorbeeldexamens/po-X.Y).`
- Bron-data: `content/voorbeeldexamens/po-<code>.md` — gebruik de `> [!question]-` callouts om de onderwerpen + frequenties te identificeren.

### 6. Concepten die ook in andere PO's leven

- Korte intro: *"Als je meerdere PO's tegelijk voorbereidt, herken hier de dubbele rendementen:"*
- Tabel met kolommen: `Concept` (wikilink) · `Ook actief in` · `Waarom relevant elders`
- 5-8 rijen, gericht op niet-triviale cross-PO-verbanden (niet bv. "PO 1.1 boekhouding" — te generiek)

### Footer

```markdown
---

*Minicursus afgeleid uit het officiële ITAA-examenprogramma (PO X.Y). Status: voorgesteld — nog niet inhoudelijk gecureerd.*
```

## Frontmatter (canoniek)

```yaml
---
title: "PO X.Y — <Volledige PO-titel> · minicursus"
description: "Minicursus voor PO X.Y: waarom dit vak, wat je moet kunnen, concept-kaart, leesroute"
tags:
  - minicursus
  - po-X-Y
---
```

## Stilistische regels

1. **Kolom-tabellen ipv mega-tabellen.** Max 4 kolommen, anders splitsen.
2. **Wikilinks ALTIJD voor concept-namen** die genoemd worden. `[[consolidatiekring]]` of met label: `[[consolidatiekring|de kring bepalen]]`.
3. **Geen taken-codes** (`1.4.taak.1.doel.4`). Wel: de tekst van de doelstelling verbatim.
4. **Confidence-labels** alleen waar wettelijke claims gedaan worden. In de minicursus zelden nodig — vermijd ⚖️/🤖-overload.
5. **Wettelijke artikelreferenties** mogen, maar als pointer: "WVV Boek 3, art. 3:22 e.v." — niet de wettekst zelf overnemen (regel 1: bron blijft heilig).
6. **Lengte-richtlijn**: 1500-2500 woorden voor een typische minicursus. Korter als het PO klein is.

## Pre-publicatie-checklist

- [ ] Frontmatter compleet (title + description + tags)
- [ ] Alle wikilinks wijzen naar bestaande records (run `python3 -m tools.lib.records_api check-links` of equivalent)
- [ ] Zes secties aanwezig, in volgorde
- [ ] Doelstellingen-tekst verbatim overgenomen uit `programma.json`
- [ ] Geen interne field-namen of project-jargon in de tekst
- [ ] Tone: kandidaat-gericht ("jij" / "de kandidaat") consistent doorheen het document
- [ ] Examen-radar gebaseerd op werkelijke `content/voorbeeldexamens/po-<code>.md`-inhoud
- [ ] Footer met status-disclaimer
