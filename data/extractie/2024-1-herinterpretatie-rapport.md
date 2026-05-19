# Pilot-rapport: herinterpretatie 2024-1 (ADR-022 DRAFT)

**Datum**: 2026-05-19
**ADR**: [`docs/adr/ADR-022-vraag-herinterpretatie-draft.md`](../../docs/adr/ADR-022-vraag-herinterpretatie-draft.md)
**Bron-PDF**: `resources/raw/voorbeeldexamens/Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf`
**Doel**: classificeren of 2024-1 een officiële vragenbundel of een herinnering-reconstructie is, en in het laatste geval per vraag herinterpreteren zonder breaking changes aan de bestaande JSON-structuur.

## Belangrijkste vaststelling

**2024-1 is een herinnering-reconstructie**, geen officiële ITAA-vragenbundel. Bewijs:

- Geen "Vraag N … / X punten"-headers zoals 2013/2014/2015. Alleen "1 Vennootschapsrecht" als sectie-titel.
- Geen puntentoekenning per vraag (`punten: null` op alle 11 vragen).
- Sub-letters A-E op vraagniveau zijn **deelvragen**, niet MC-opties van één hoofdvraag. Binnen sommige subvragen wel echte MC-opties (lowercase a/b/c/d).
- Verschillende subvragen bevatten alleen het **onderwerp** ("Stellingen Juist of Fout ivm omzettingen") zonder de stellingen zelf — onmogelijk uit officiële bron.
- Twee vragen bevatten een hint/antwoord direct in de vraagtekst (sub-D vr8: "100.000 – 10.000 tantième = 90.000 euro"; sub-B/C vr10: "n-dagen klantenkrediet", "Toenemende eisbaarheid").
- Typo's en onafgemaakte fragmenten: "Fifi" (FIFO), "Kosten voor voorbereiding van een terrein……?", "Takxshelter" (Taxshelter).

## Classificatie per vraag (11/11 op `herinnering`)

| ID | Vak | Volledigheid | Antwoord-hint | MC opgemerkt |
|---|---|---|---|---|
| vr1 | Vennootschapsrecht | fragment | nee | sub-C, sub-D (4+4) |
| vr2 | Externe controle | fragment | nee | sub-E (4) |
| vr3 | Interne controle | volledig | nee | sub-C, sub-D (4+3) |
| vr4 | Bijzondere mandaten | fragment | nee | — (J/F-set sub-A) |
| vr5 | Personenbelasting | volledig | nee | — |
| vr6 | Deontologie en AWW | fragment | nee | sub-A (4), sub-B (5) |
| vr7 | IFRS | fragment | nee | sub-A (4 J/F) |
| vr8 | Vennootschapsbelasting | fragment | **ja (sub-D)** | sub-E (9) |
| vr9 | Fiscale procedure | fragment | nee | — |
| vr10 | Analyse jaarrekening | fragment | **ja (sub-B, sub-C)** | sub-E (4) |
| vr11 | BTW | volledig | nee | sub-A/C/D/E (4+5+5+5) |

**Samenvatting**:
- `vraag_herkomst = herinnering`: 11 / 11
- `vraag_volledigheid = volledig`: 3 / 11 (vr3, vr5, vr11 — vragen waarbij stam + MC volledig in PDF zichtbaar)
- `vraag_volledigheid = fragment`: 8 / 11
- `vraag_volledigheid = stam_zonder_opties`: 0 / 11 (geen enkele vraag op zich is volledig leeg; sub-fragmenten zitten verspreid)
- `antwoord_hint_in_vraag = aanwezig`: 2 / 11 (vr8 sub-D, vr10 sub-B + sub-C)

## Voor/na — twee illustratieve voorbeelden

### Voorbeeld 1 — vr10 sub-C (hint in vraagtekst)

**Originele vraagtekst (uit PDF)**:
> C. In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt? Toenemende eisbaarheid

**Probleem**: "Toenemende eisbaarheid" lijkt onderdeel van de vraag, maar is vermoedelijk het antwoord dat de stagiair zelf noteerde. Een lezer zonder context denkt dat dit een gegeven is van de vraag — verwarrend.

**Geherinterpreteerd**:
> C. In welke volgorde zijn de rubrieken op de passiefzijde van de balans gerangschikt?
> Hint in vraagtekst: 'Toenemende eisbaarheid' (vermoedelijk het antwoord dat stagiair noteerde).

**`antwoord_hint_in_vraag`** maakt expliciet dat de hint geen vraag-element is. Modelantwoord-pipeline kan nu de echte vraag beantwoorden zonder verstoring.

### Voorbeeld 2 — vr8 sub-D (berekening-hint)

**Originele vraagtekst**:
> D. NV A BJ 31/12/22 winst voor belasting 100.000 euro (voor winstuitkering) Belgische belasting = 20.000 euro. De AV beslist om tantième van 10.000 euro toe te kennen en een gewoon dividend van 20.000 euro uit te keren. Hoeveel bedraagt de belastbare basis van A voor AJ23? 100.000 – 10.000 tantième = 90.000 euro

**Probleem**: de berekening "100.000 – 10.000 tantième = 90.000 euro" hangt aan het einde van de vraagtekst. Dit is geen ITAA-formulering — het is wat de stagiair zelf opschreef. Een naïef gegenereerd modelantwoord zou deze berekening als "gegeven door ITAA" interpreteren en onderzoeksruimte verliezen (klopt 90.000 wel? dividend telt nog niet mee?).

**Geherinterpreteerd**:
> D. NV A — boekjaar 31/12/22, winst voor belasting 100.000 euro (voor winstuitkering). Belgische belasting = 20.000 euro. De algemene vergadering beslist een tantième van 10.000 euro toe te kennen en een gewoon dividend van 20.000 euro uit te keren. Hoeveel bedraagt de belastbare basis van A voor aanslagjaar 23?
> Hint in vraagtekst: 100.000 − 10.000 tantième = 90.000 euro (vermoedelijke schaduw van het verwachte antwoord).

## Welke modelantwoorden mogelijk moeten worden herzien

Drie vragen hebben reeds een ingeschreven modelantwoord van vóór deze pilot:

| Vraag | Volledigheid | Modelantwoord-status | Aanbeveling |
|---|---|---|---|
| vr3 (interne controle) | volledig | `inferred`, claim-coverage gepasseerd | **Mag blijven**. Stam en MC-opties zijn volledig, herinterpretatie was overwegend cosmetisch. |
| vr7 (IFRS) | fragment | `grounded` op sub-A, `record_gap_report` op sub-B/C/D | **Conform-status mag blijven**. Modelantwoord erkent reeds dat alleen sub-A volledig beantwoord is en flagt de rest als partieel extract. |
| vr10 (financiële analyse) | fragment | `inferred`, claim-coverage gepasseerd | **Te herzien** — sub-A is `stam_zonder_opties` (alleen onderwerp "Stellingen financiële onafhankelijkheid", geen stellingen). Huidig modelantwoord schrijft generieke regels alsof het de vraag beantwoordt; beter zou zijn dit deel te markeren als niet-beantwoordbaar (`record_gap_report.type = "vraagtekst_onvolledig_herinnering"` voor sub-A). Sub-B en sub-C zijn beantwoordbaar maar het modelantwoord moet expliciet maken dat de gegeven hint vermoedelijk al het antwoord is — eerder validatie dan reconstructie. |

## Aanbevelingen voor andere PDFs

| Bron | Verwacht patroon | Actie |
|---|---|---|
| `2003-bibf.json`, `2008-bibf.json` | officieel BIBF-bundel | steekproef 1-2 vragen — vraagtekst-headers controleren (puntentoekenning, formele stelling-formulering); geen massa-herinterpretatie verwacht |
| `2013-1.json`, `2013-2.json`, `2014-1.json`, `2015-1.json` | officieel ITAA-wedstrijdtekst | bevestigd: "Vraag N … / X punten"-headers, ingevulde tabellen, volledige MC. Geen herinterpretatie nodig — wel: zet expliciet `vraag_herkomst: "officieel"` op alle vragen (top-level marker is voldoende voor batch-flag) |
| `2024-1.json` | **herinnering — afgerond door deze pilot** | — |
| `2025+` (toekomstig) | onbekend; afwezigheid van puntentoekenning + fragment-stijl = vermoedelijk herinnering | per nieuwe PDF: checken vóór modelantwoord-werk; conform pilot 2024-1 indien herinnering-stijl |

## Wat NIET gedaan in deze pilot

- Geen modelantwoord-herziening van vr3 / vr7 / vr10 (zie tabel hierboven — opvolgwerk).
- Geen `vraag_herkomst`-stempel op andere examen-files. Steekproef-verificatie is opvolgwerk.
- Geen schema-bump examen_vragen v3.0. Alle nieuwe velden zijn additief.
- Geen aanpassing van ADR-020 modelantwoord-pipeline. De pipeline blijft van kracht; ADR-022 voegt een pre-pipeline herinterpretatie-stap toe en wijst de pipeline aan welke vraag-tekst-bron te gebruiken.

## Concrete next steps

1. Opus-review op deze ADR-draft + voor/na-tabel; bij akkoord → status `Accepted`.
2. Steekproef-verificatie (5 minuten) op `2013-1.json` en `2003-bibf.json` om de `officieel`-default te bevestigen — als dat klopt, top-level `vraag_herkomst_bestand: "officieel"` toevoegen aan die files.
3. Modelantwoord-herziening van vr10 (sub-A markeren als niet-beantwoordbaar; sub-B/C valideren tegen hint i.p.v. herconstrueren) — onder ADR-020 gap-flow.
4. Bij volgende PDF-import: voor modelantwoord-pass eerst herkomst-check, dan eventueel herinterpretatie-pass.
