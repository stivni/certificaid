# Pattern-scan modelantwoorden — voor ADR-023

**Datum**: 2026-05-20
**Scope**: 112 ingeschreven modelantwoorden (99 op vraag-niveau + 13 op subvraag-niveau) in `data/programma/examen_vragen/*.json`.
**Doel**: structurele elementen in bestaande `correct_antwoord` + `antwoord_motivering`-platte tekst herkennen, zodat ADR-023 typed `correct_antwoord_blokken[]` kan voorstellen zonder nieuwe inhoud te verzinnen.

## Globaal beeld

| Niveau | Aantal records | Met `correct_antwoord` |
|---|---:|---:|
| Vraag-niveau | 253 | 99 |
| Subvraag-niveau | 455 | 13 |
| **Totaal modelantwoorden** | — | **112** |

`antwoord_type`-verdeling over de 112 records:

| `antwoord_type` | Aantal |
|---|---:|
| (leeg / `null`) | 30 |
| `kwalificatie` | 27 |
| `definitie` | 13 |
| `casus` | 13 |
| `berekening` | 9 |
| `opsomming` | 9 |
| `procedure` | 6 |
| `presentatie` | 3 |
| `drempel_cijfer` | 2 |

> 30 vraagsplitsings-`casus`-records hebben geen `antwoord_type` op vraag-niveau (alle inhoud zit in subvragen). De 13 subvraag-antwoorden zijn alle binnen 5 vragen geclassificeerd als `casus`.

## Per element-categorie (gedetecteerd)

Pattern-frequentie over de hele set (vraag- en subvraag-records samen). Telling per record (niet per voorkomen). De percentages zijn als richtsnoer; de samples zijn de eerste 2-3 hits.

### 1. Grondslag-alinea (76/112 = 68 %)

Een afsluit-blok in `antwoord_motivering` dat de wetsbron noemt: `_Grondslag: KB WVV art. 3:50; CBN-advies 2018/02._`

Voorbeelden: `2003-bibf-vrA1`, `2003-bibf-vrA2`, `2003-bibf-vrB1`.

**Bevinding**: 68 % van de antwoorden eindigt met een expliciete grondslag-alinea. Dit is de natuurlijke kandidaat-blok-type `grondslag`. Bij de overige 32 % is de grondslag soms inline (in een `⚖️`-claim met `_KB WVV art. X_`) of ontbreekt hij — die laatste 32 % hoeven dus geen `grondslag`-blok te krijgen.

### 2. Confidence-markers ⚖️ / 🤖 (72 + 57 = 129 records)

`⚖️` (grounded): 72/112 records (64 %).
`🤖` (inferred): 57/112 records (51 %).
Gemengd in 50+ records.

**Bevinding**: confidence-discipline is dominant. Per blok moet optioneel een `confidence`-veld kunnen komen (`grounded` / `inferred`).

### 3. Wikilinks (48/112 = 43 %)

`[[hulpdagboeken]]`, `[[berekenen-controle-en-belangenpercentage]]` etc.

**Bevinding**: cross-record-referenties zijn alom aanwezig. Geen apart blok-type nodig — gewoon behouden in tekst. Wel: render-laag moet `[[...]]`-syntax in elk blok-type kunnen renderen.

### 4. Genummerde lijst met bold lemma's (30/112 = 27 %)

`1. **Onder-gewaardeerde activa** — werkelijke waarde > boekwaarde. ⚖️`

Voorbeelden: `2003-bibf-vrB1`, `2003-bibf-vrB3`, `2003-bibf-vrB5`.

**Bevinding**: standaardvorm voor `opsomming`-vragen (alle 7 `opsomming`-records hebben dit) en voor genummerde redeneringen bij `casus`/`definitie`. Kandidaat-blok-type `opsomming` met `items[{lemma, toelichting, confidence}]`.

### 5. Boekings-codeblock (12/112)

```
Debet 6340 Waardeverminderingen op voorraden  € 100
Credit 3209 Geboekte waardeverminderingen     € 100
```

Voorbeelden: `2003-bibf-vrA2`, `2008-bibf-vrB1`, `2013-1-vr2`. Alle 12 vallen onder `kwalificatie` (9), `berekening` (2), `casus` (1).

Daarnaast 6 records waar de boeking inline in tekst staat zonder code-fences — totaal 18 records hebben boekingen.

**Kandidaat-blok-type**: `boeking` met `regels[{zijde, rekening, naam, bedrag, eenheid}]` + optioneel `context` (bv. "Bij aanschaffing", "Jaarlijkse afschrijving"). User-observatie 2003-vrA1: 4 boekings-stappen ("Bij toezegging", "Aanschaffing", "Afschrijving", "Subsidie-opname") — elk een eigen `boeking`-blok met `context`.

### 6. Markdown-tabel (9/112)

Voorbeelden: `2003-bibf-vrC2` (operationele cashflow per component), `2013-1-vr3` (kostencategorieën activeerbaar?), `2014-1-vr8` (controlepercentage-tabel).

**Bevinding**: bestaande consumers renderen reeds markdown-tabellen. Kandidaat-blok-type `tabel` (analoog aan v3 vraagtekst_blokken-tabel) — `headers[]` + `rows[][]`.

### 7. Scenario/Variant/Optie-headers (7/112)

`**Scenario A — Meerwaarde gespreid gerealiseerd via afschrijvingen**`
`**Optie A: Toegelaten** — overboeking naar reserves`

Voorbeelden: `2013-2-vr1`, `2014-1-vr3/a)`, `2014-1-vr3/c)`.

**Bevinding**: 7 antwoorden bespreken twee of meer alternatieven (wat-als-cijfer-anders, scenario-A-vs-B). Kandidaat-blok-type `alternatief` met `varianten[{naam, inhoud, confidence}]` — of simpeler: meerdere `motivatie`-blokken elk met een eigen `kop`-veld. **Beslissing voor ADR-023**: niet als apart blok-type, maar `motivatie`-blok krijgt optioneel `kop`-veld. Onder-engineering vermijden bij 7 records.

### 8. MC-keuze-aanduiding (6/112)

`**Van de vier MC-opties is optie 3 "..." juist** ⚖️`

Voorbeelden: `2013-2-vr1`, `2014-1-vr3/a)`, `2014-1-vr5`. Allen `kwalificatie` of `berekening`.

**Bevinding**: bij MC-vragen wordt het juiste alternatief expliciet benoemd. Kandidaat-blok-type `mc_keuze` met `gekozen_label` + `motivering` + `confidence`. **Beslissing**: niet apart blok-type — past in `conclusie`-blok of inline in `motivatie` met markering. Bij 6 records weegt het niet op tegen extra complexiteit.

### 9. Conclusie/Antwoord-kop (5/112)

`**Conclusie**: ...`
`**Antwoord**: ...`

Voorbeelden: `2014-1-vr3/c)` (uitrekening), `2014-1-vr5`, `2015-1-vr1`. Alle `berekening`/`casus`.

**Bevinding**: 5 records hebben een expliciete "Conclusie"-paragraaf na een lange uitwerking. Kandidaat-blok-type `conclusie` met `inhoud` + optioneel `confidence`.

### 10. Definitie-lemma (4/112)

`**Een onthouding van oordeel** is een ...`

Voorbeelden: `2013-2-vr11`, `2014-1-vr1`, `2024-1-vr3`, `2024-1-vr7`.

**Bevinding**: alle 13 `definitie`-records hebben in feite een definitie-zin, maar maar 4 hebben een expliciete fettte lemma-kop. Kandidaat-blok-type `definitie` met `lemma` + `definitie_zin` + `kerneigenschappen[]` + optioneel `vergelijking[]`/`voorbeelden[]`.

### 11. Vergelijking/Voorbeeld (1+1 records)

`**Vergelijk met andere oordeel-types**`
`**Voorbeelden** van situaties die ...`

Beide alleen in `2013-2-vr11` (onthouding van oordeel). **Te zeldzaam voor apart blok-type** — past in `motivatie`-blok met `kop`.

### 12. Stap-headers (1/112)

`### Stap 1: Bij toezegging`

Alleen `2003-bibf-vrA1`.

**Bevinding**: ook al is dit één record, het is een **structureel patroon** dat boekings-blokken groepeert. Kandidaat: `boeking`-blok krijgt optioneel `context`-veld (bv. `"Stap 1: bij toezegging"`); geen apart `stap`-blok-type.

### 13. Formule-definitie (2/112)

`**Goodwill-percentage** = (Goodwill / EV) × 100`

Voorbeelden: `2015-1-vr2`, `2024-1-vr10`.

**Bevinding**: 2 records hebben een expliciete formule-definitie. Plus 5-6 records waar de formule inline staat in een `berekening`. Kandidaat-blok-type `berekening` met `formule` + `componenten[{naam, bedrag}]` + `resultaat` + `eenheid`.

## Voorgestelde blok-types voor ADR-023

Op basis van bovenstaande scan, en aansluitend bij de bestaande ADR-021 v3-vraagtekst-typering (zelfde namen waar betekenisvol gelijk):

| Type | Verplicht | Optioneel | Use case (frequentie) | Antwoord-types die hem vooral gebruiken |
|---|---|---|---|---|
| `motivatie` | `inhoud` (markdown-string) | `kop`, `confidence` | Algemene paragraaf-redenering, vergelijking, voorbeeld — **fallback** (alle 112 records hebben minstens één) | alle |
| `boeking` | `regels[{zijde, rekening, naam, bedrag}]` | `context`, `eenheid`, `confidence` | Debet/Credit-boeking (18 records, vooral `kwalificatie`/`berekening`) | `kwalificatie`, `berekening`, `casus` |
| `berekening` | `formule` (string) of `componenten[{naam, bedrag}]` | `tussenstappen[]`, `resultaat`, `eenheid`, `interpretatie`, `confidence` | Formule + ingevulde cijfers (12 records met `formule_equals`-pattern) | `berekening`, `kwalificatie` |
| `opsomming` | `items[{lemma, toelichting?, confidence?}]` | `volgorde_vast`, `kop` | Genummerde lijst met bold lemma's (30 records, alle 7 `opsomming`-records) | `opsomming`, `casus`, `definitie` |
| `procedure` | `stappen[{nummer, beschrijving, confidence?}]` | `werkdocument_per_stap`, `valkuilen[]` | Genummerde procedure-stappen (6 `procedure`-records + sub-records) | `procedure` |
| `definitie` | `lemma`, `definitie_zin` | `kerneigenschappen[]`, `confidence` | Definitie-blok bij `definitie`-antwoord (13 records) | `definitie` |
| `tabel` | `rows[][]` | `headers[]`, `kop`, `confidence` | Markdown-tabel (9 records) | `berekening`, `kwalificatie` |
| `conclusie` | `inhoud` | `confidence`, `gekozen_mc_label` | Slot-conclusie / MC-antwoord-keuze (5 + 6 records) | `kwalificatie`, `berekening`, `casus` |
| `grondslag` | `bronnen[]` (list[string]) | `confidence` | Afsluitende grondslag-alinea — typisch `KB WVV art. X`, `CBN-advies Y`, of `[[record]]`-link (76 records) | alle |

**Totaal: 9 blok-types**.

Verworpen (te zeldzaam of beter onder ander blok-type):
- `alternatief` (7 records) → `motivatie` met `kop`
- `mc_keuze` (6 records) → `conclusie` met `gekozen_mc_label`
- `vergelijking` / `voorbeeld` (1 + 1) → `motivatie` met `kop`
- `stap_header` (1) → `boeking`-blok krijgt `context`-veld

## Suggestie nieuwe `antwoord_type`-enum-waardes

Huidige set (8): `definitie`, `drempel_cijfer`, `opsomming`, `presentatie`, `kwalificatie`, `berekening`, `procedure`, `casus`.

Op basis van inhoud-scan + de praktijk dat 27 records nu onder `kwalificatie` gevangen worden terwijl ze structureel ofwel "geef de boekingen" ofwel "geef het advies" zijn:

| Voorgesteld nieuw type | Waarom niet onder bestaand? | Frequentie in 27 `kwalificatie`-records |
|---|---|---|
| `boeking` | "Geef de afsluitingsboekingen", "Boek de subsidie": het hoofd-leverbare is een typed boekings-set, niet een methodekeuze. `kwalificatie` is een classificatie-vraag, niet een register-vraag. | ~12 (2003-bibf-vrA1, 2003-bibf-vrA2, 2008-bibf-vrB1, ...) |
| `waardering` | "Waardeer de voorraad", "bepaal de aanschaffingswaarde". Structureel: formule + cijfer-toepassing + voorzichtigheidsbeginsel — overlapt met `berekening` maar met klemtoon op de waarderingsregel ipv puur cijfer. | ~5 |
| `advies` | "Geef advies aan de cliënt", "Wat raadt u aan?": antwoord = aanbeveling + motivatie + waarschuwing. Niet `kwalificatie` (geen classificatie), niet `procedure` (geen vaste stappen). | ~3 (2008-bibf-vrK2/K3, ...) |

Verworpen:
- `analyse` — overlapt te veel met `kwalificatie`. Een redeneer-vraag waarbij je iets analyseert is gewoon kwalificatie + motivatie.
- `juist_fout` — past al onder `kwalificatie` met expliciet `gekozen_mc_label` in `conclusie`-blok.

**Aanbeveling**: 3 nieuwe enum-waardes (`boeking`, `waardering`, `advies`). Bestaande records houden hun huidige `antwoord_type` voor nu; een opvolg-classificatie-pass kan herclassifiëren (out-of-scope ADR-023).

## v3.1 vraag-cleanup observaties

### `vraag_onderwerp`-kandidaten

Top-of-blok korte titel-zin (max 4 woorden, kapitaal-start, gevolgd door `.` en casus-tekst):

| ID | Onderwerp |
|---|---|
| `2003-bibf-vrA1` | `Kapitaalsubsidies` |
| `2013-2-vr28`, `2014-1-vr17` | `Dhr` (false positive — eigennaam, casus begint) |

True onderwerp-titels zijn dus zeldzaam in officiële BIBF/ITAA-bundels (≈1 % van de vragen heeft een echte titel). Detector moet zeer conservatief zijn: alleen klassieken zoals "Kapitaalsubsidies", "Voorraden", "Afschrijvingen" als één-woord boekhoud-thema → opzuigen als `vraag_onderwerp`. Voor de overige vragen blijft het veld `null`.

### Residue-strippen

| Residue-patroon | Voorkomen | Actie |
|---|---:|---|
| `Vraag :` / `Vraag:` in `tekst`-blok | 11 | strippen + restant naar volgende detectie |
| `Antwoord` als eerste woord (residue van examen-PDF antwoord-veld) | 110 | strippen — komt vrijwel in elke vraag voor want bij elke vraag staat in de PDF "Antwoord" als kop bij modelantwoord-veld |
| `N PUNTEN` residue in `tekst`-blok (niet al gelift) | 38 | strippen via verbeterde `_PUNTEN_UPPERCASE` |
| `o. Er werd ...` losse fragmenten | 1 | opzuigen naar voorgaande inventaris-/casus-blok |

### `vraag_instructie` zonder `casus_context`

90/253 vragen hebben wel een `vraag_instructie`-blok maar geen `casus_context` ervoor. Voor sommige past dat (korte vragen "Wat is X?"), voor andere is de casus-text gevangen in een algemeen `tekst`-blok. Scherper `casus_context`-detectie zou dat oplossen — bv. **alles tussen `vraag_onderwerp` en `vraag_instructie` opzuigen** als `casus_context` indien het verhalend is (≥ 50 tokens en geen imperatief).

## Wat NIET in deze scan

- Geen nieuwe inhoud verzinnen voor antwoord-blokken — pure structurele observatie.
- Geen herclassificatie van bestaande `antwoord_type`-waardes (out-of-scope).
- Geen aanpassing van `prompts/modelantwoord-checklists.md` v1.0 — wel relevant voor opvolg-pass na ADR-023.
