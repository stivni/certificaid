# Deep-rewrite batch 2 — rapport

**Datum**: 2026-05-16
**Operator**: deep-rewrite-batch-2-concepten (Opus 4.7)
**Scope**: 19 resterende PO 1.4-concept-records — schema 1.4 (regels 6–14 v4-prompt).
**Werkwijze**: strict Read/Edit/Write per record, geen Python-scripts.

## Status `eerste-consolidatie`

`eerste-consolidatie.json` droeg reeds een `_provenance.deep_rewrite_2026_05_16`-stempel uit batch 1 (zie batch-1-rapport, regel 7 in de tabel). **Overgeslagen**, conform de briefing-regel.

Effectieve set bewerkt in batch 2 = **19 records**.

## Per-record samenvatting

Legenda kolomwaarden: `n.v.t.` = niet aanwezig in dit record-type; getallen = aantal eenheden gewijzigd/toegevoegd.

| # | Record | Type | Bouwstenen | Stappen | Substappen-blokken | voorbeeld_inline | Formules atomair |
|---|---|---|---:|---:|---:|---:|---:|
| 1  | consortium                              | actor    | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + 3 in in_praktijk | n.v.t. |
| 2  | dochteronderneming                      | actor    | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 3  | exclusieve-controle                     | begrip   | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + 4 in in_praktijk + valkuil-cast | n.v.t. |
| 4  | geassocieerde-onderneming               | actor    | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk + drempel-cast | n.v.t. |
| 5  | geconsolideerd-jaarverslag              | begrip   | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 6  | geconsolideerde-jaarrekening            | begrip   | 5/5          | n.v.t. | n.v.t. | 1 (record) + 5 (bouwstenen) | n.v.t. |
| 7  | gemeenschappelijke-dochteronderneming   | actor    | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 8  | gezamenlijke-controle                   | begrip   | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 9  | groep-van-beperkte-omvang               | begrip   | n.v.t.       | n.v.t. | n.v.t. | 1 (record-cliëntsituatie) + cast in valkuil | n.v.t. |
| 10 | groottecriteria-consolidatie            | drempel  | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in valkuilen | n.v.t. |
| 11 | horizontale-consolidatie                | procedure| n.v.t.       | 5/5 (skeleton → vol-blok) | 1 (stap 3: balansen consortium-leden) | 1 (record) | n.v.t. |
| 12 | ifrs-consolidatieraamwerk               | begrip   | 2/2          | n.v.t. | n.v.t. | 1 (record) + 2 (bouwstenen) | n.v.t. |
| 13 | invloed-van-betekenis                   | begrip   | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 14 | minderheidsbelangen                     | fenomeen | n.v.t.       | 5/5 (skeleton → vol-blok) | 1 (stap 3: berekening + balans-fragment) | 1 (record) | 2 (was 1 string) |
| 15 | moedervennootschap                      | actor    | n.v.t.       | n.v.t. | n.v.t. | 1 (record) + cast in in_praktijk | n.v.t. |
| 16 | step-acquisition                        | fenomeen | 3/3          | n.v.t. | n.v.t. | 1 (record) + 3 (bouwstenen) | n.v.t. |
| 17 | uniforme-waarderingsregels-consolidatie | regel    | n.v.t.       | n.v.t. | n.v.t. | 1 (record-cliëntsituatie) + cast in in_praktijk | n.v.t. |
| 18 | vrijstelling-subconsolidatie            | regel    | n.v.t.       | n.v.t. | n.v.t. | 1 (record-cliëntsituatie subconsolidatie-cast) | n.v.t. |
| 19 | wijziging-consolidatiekring             | fenomeen | 4/4          | n.v.t. | n.v.t. | 1 (record) + 4 (bouwstenen) | n.v.t. |

**Totaal**:
- 14 bouwstenen rewriten met waarom + voorbeeld_inline + stagiair-toon (recs 6, 12, 16, 19)
- 10 stappen omgezet van skeleton naar vol-blok (recs 11, 14)
- 2 substappen-blokken (worked examples) toegevoegd (recs 11, 14)
- 19 record-niveau voorbeeld_inline toegevoegd (+ talrijke cast-voorbeelden in in_praktijk en valkuilen)
- 2 formules atomair gesplitst met variabelen + invulling_voorbeeld (rec 14: minderheidsbelangen — balans + RR)
- Alle 19 records hebben nu `_provenance.deep_rewrite_2026_05_16`-stempel

## Cast-namen-gebruik (regel 7)

| Scenario | Vennootschappen | Records waar gebruikt |
|---|---|---|
| basis_consolidatie | Aurelia Holding NV (moeder) + Brugse Brouwerij BV (dochter 80 %) | 2, 3, 5, 6, 7, 8, 9, 10, 14, 15, 17, 19 |
| basis_keten | + Bouwwerf Beerse BV (dochter 100 %) | 2, 6, 19 |
| joint_venture | Cardinal Group NV + Energiehuis Evergem NV → Filmstudio Florence BV (50/50) | 7, 8, 13 |
| geassocieerde | Antwerpse Investments NV → Drukkerij Dendermonde BV (25 %, AW 200, EV 600) | 4, 13, 16, 19 |
| consortium | Pieter Vermeulen + Industria Antwerpen NV / Jachthaven Jezus-Eik NV | 1, 9, 10, 11, 17 |
| subconsolidatie | Kappers Köln GmbH (top, DE) + Aurelia (tussen) + Brugse (dochter) | 17, 18 |
| ifrs / genoteerd | Aurelia Holding NV (beursgenoteerd op Euronext Brussels) | 12 |
| groep_van_beperkte_omvang | Aurelia + Gent Garantie BV | 9, 10 |

Geen voorkomens meer van "M", "D", "X", "Y", "ABC", "DEF" in nieuwe content. De `voorbeeld_inline`-objecten op record-niveau gebruiken voortaan plain strings (consistent met batch-1-pattern) i.p.v. de oude `{text, confidence, source, _provenance}`-objecten — dat brengt de records in lijn met regel 13 minimum-eisen.

## Voorbeeld-minimum (regel 13)

Alle 19 records halen het minimum:

| Record | Type | Minimum-regel | Voldaan via |
|---|---|---|---|
| consortium                              | actor    | ≥1 voorbeeld_inline rol-context | record + bewijsregels in in_praktijk |
| dochteronderneming                      | actor    | ≥1 voorbeeld_inline rol-context | record (cast Aurelia/Brugse) |
| exclusieve-controle                     | begrip   | ≥1 voorbeeld_inline             | record + drempel-gevolg + valkuil-cast |
| geassocieerde-onderneming               | actor    | ≥1 voorbeeld_inline rol-context | record (cast Antwerpse/Drukkerij Dendermonde) |
| geconsolideerd-jaarverslag              | begrip   | ≥1 voorbeeld_inline             | record (cast keten Aurelia + dochters) |
| geconsolideerde-jaarrekening            | begrip   | ≥1 voorbeeld_inline             | record + 5× bouwsteen-voorbeeld |
| gemeenschappelijke-dochteronderneming   | actor    | ≥1 voorbeeld_inline rol-context | record (cast joint_venture) |
| gezamenlijke-controle                   | begrip   | ≥1 voorbeeld_inline             | record (cast joint_venture) |
| groep-van-beperkte-omvang               | begrip   | ≥1 voorbeeld_inline cliëntsituatie | record (Aurelia + Gent Garantie met drempelcijfers) |
| groottecriteria-consolidatie            | drempel  | ≥1 voorbeeld_inline             | record + cast in valkuilen |
| horizontale-consolidatie                | procedure| ≥1 worked example               | substappen stap 3 (cast Industria/Jachthaven) + 5 stappen vol-blok |
| ifrs-consolidatieraamwerk               | begrip   | ≥1 voorbeeld_inline             | record + 2× bouwsteen-cast |
| invloed-van-betekenis                   | begrip   | ≥1 voorbeeld_inline             | record + cast in in_praktijk |
| minderheidsbelangen                     | fenomeen | ≥1 voorbeeld_inline             | record + 5× stap-voorbeeld + worked example stap 3 + 2× formule-invulling + concreet_voorbeeld |
| moedervennootschap                      | actor    | ≥1 voorbeeld_inline rol-context | record + cast-keten in in_praktijk |
| step-acquisition                        | fenomeen | ≥1 voorbeeld_inline             | record + 3× bouwsteen-cast |
| uniforme-waarderingsregels-consolidatie | regel    | ≥1 voorbeeld_inline cliëntsituatie | record + cast in valkuilen |
| vrijstelling-subconsolidatie            | regel    | ≥1 voorbeeld_inline cliëntsituatie | record (subconsolidatie-cast) |
| wijziging-consolidatiekring             | fenomeen | ≥1 voorbeeld_inline             | record + 4× bouwsteen-cast |

Geen synthese-voorbeelden (regel 14 bron 3) nodig: alle cijfers komen uit cast-scenario-defaults (`basis_consolidatie`: 320/300/80 %; `geassocieerde`: 200/600/25 %; `groep_van_beperkte_omvang`: 20 mln / 12 mln / 180 wpf) of zijn intern consistent uitgewerkt vanuit bestaande `concreet_voorbeeld`-blokken in eerdere versies van de records (rec 14 minderheidsbelangen: 80 % × 500 = 100; 20 × 100 = 20 enz.).

## Edges-types verifieerd (regel 9) — significante correcties

| Record | Oude edge | Nieuwe edge | Reden |
|---|---|---|---|
| dochteronderneming         | dubbel contrasteert-met consolidatiekring | onderdeel-van consolidatiekring | Saneren overlap; vereist-kennis-van controle toegevoegd. |
| exclusieve-controle        | typo `contrasteert-with` | `contrasteert-met` | Tikfout; ook getriggerd-door integrale-consolidatie toegevoegd. |
| geassocieerde-onderneming  | contrasteert-met vermogensmutatiemethode | getriggerd-door vermogensmutatiemethode | Functionele relatie, geen contrast; vereist-kennis-van invloed-van-betekenis toegevoegd. |
| geconsolideerd-jaarverslag | contrasteert-met geconsolideerde-jaarrekening | onderdeel-van + getriggerd-door consolidatieverplichting + vereist-kennis-van | Compositionele relatie, niet contrast. |
| geconsolideerde-jaarrekening | contrasteert-met geconsolideerd-jaarverslag / consolidatieverplichting | bevat geconsolideerd-jaarverslag + getriggerd-door consolidatieverplichting | Compositioneel/functioneel. |
| groep-van-beperkte-omvang  | contrasteert-met consolidatieverplichting | uitzondering-op consolidatieverplichting + vereist-kennis-van groottecriteria | Logisch uitzondering, geen contrast. |
| groottecriteria-consolidatie | contrasteert-met consolidatieverplichting | getriggerd-door consolidatieverplichting + vereist-kennis-van groep-van-beperkte-omvang | Functionele afhankelijkheid. |
| gezamenlijke-controle      | contrasteert-met gemeenschappelijke-dochteronderneming | getriggerd-door gemeenschappelijke-dochteronderneming + getriggerd-door evenredige-consolidatie | Constitutieve relatie. |
| horizontale-consolidatie   | contrasteert-met consortium | onderdeel-van consortium + vereist-kennis-van integrale-consolidatie | Procedure binnen structuur-concept. |
| ifrs-consolidatieraamwerk  | alternatief-voor consolidatieverplichting | alternatief-voor geconsolideerde-jaarrekening + getriggerd-door consolidatieverplichting | IFRS is alternatief raamwerk, niet een alternatieve plicht. |
| invloed-van-betekenis      | contrasteert-met geassocieerde-onderneming | getriggerd-door geassocieerde-onderneming + getriggerd-door vermogensmutatiemethode | Constitutieve relatie. |
| minderheidsbelangen        | dubbel onderdeel-van + getriggerd-door integrale-consolidatie | enkel onderdeel-van integrale-consolidatie; onderdeel-van belangenpercentage → vereist-kennis-van | Eenduidige hiërarchie. |
| moedervennootschap         | contrasteert-met dochteronderneming | bevat dochteronderneming + onderdeel-van consolidatiekring + getriggerd-door consolidatieverplichting + vereist-kennis-van controle | Correlatieve relatie (moeder bevat dochters). |
| step-acquisition           | dubbel contrasteert-met wijziging-consolidatiekring / eerste-consolidatie | specialisatie-van wijziging-consolidatiekring + getriggerd-door eerste-consolidatie + vereist-kennis-van consolidatieverschil | Hiërarchische relatie. |
| uniforme-waarderingsregels-consolidatie | contrasteert-met integrale-consolidatie | onderdeel-van geconsolideerde-jaarrekening + uitzondering-op | Compositionele randvoorwaarde, geen contrast. |
| vrijstelling-subconsolidatie | dubbel contrasteert-met consolidatieverplichting + uitzondering-op | enkel uitzondering-op consolidatieverplichting; contrast met groottecriteria naar vergelijkingsparen | Eenduidige uitzondering; vergelijkingsparen met examen-keuze-trigger behouden. |
| wijziging-consolidatiekring | dubbel contrasteert-with consolidatiekring / eerste-consolidatie | van-toepassing-op consolidatiekring + bevat eerste-consolidatie + bevat step-acquisition | Stand vs. beweging; eerste-consolidatie + step-acquisition als sub-gevallen. |

`vergelijkingsparen` blijft alleen behouden waar echte examen-keuze-trigger geldt:
- `dochteronderneming` ↔ geassocieerde-onderneming (controle-test)
- `horizontale-consolidatie` ↔ integrale-consolidatie (relatie-type)
- `vrijstelling-subconsolidatie` ↔ groottecriteria-consolidatie (welke vrijstelling kies je?)
- `exclusieve-controle` ↔ gezamenlijke-controle (overeenkomst-test)
- `gezamenlijke-controle`: behouden bestaand vergelijkingspaar exclusieve-controle/invloed-van-betekenis impliciet als edges
- `invloed-van-betekenis`: edges vervangen vergelijkingsparen volledig (geen examen-keuze-trigger meer)

## Stagiair-toon-substituties (regel 6)

Doorgevoerde substituties (per record genoteerd in `_corrected_from`):

| Jargon / problematische formulering | Vervangen door |
|---|---|
| "consoliderende vennootschap" (resten) | "moeder" |
| "in beginsel verplicht" | "in principe" / "moet" |
| "onherroepbaar" | "onherroepelijk" |
| "in beginsel" | "in principe" |
| "indruisen tegen het getrouwe beeld" | "verstoren van het getrouwe beeld" |
| "gerealiseerd" (in context aandelenverkoop) | "verkocht" |
| "consoliderende moeder die in een concreet consolidatie-oefening" | (geschrapt — zelfreferentieel) |
| "aanwending van het vermogen" | "beheer van het vermogen" |
| "vervreemding" | "verkoop" |
| "bekendgemaakt" | "gepubliceerd" |
| "consolidatiebevoegdheid uitoefenen" | "controle uitoefenen" |
| "aanmerkelijke wijziging" | "wezenlijke verandering" |
| "voorgangsregels" / "primauteit" | "voorrang" |
| "uitsluitingsgronden cumulatief beoordeeld" | "samen toetsen" |
| "M / D / X / Y / ABC / DEF" (resten) | Cast-namen (Aurelia / Brugse / Cardinal / Antwerpse / Drukkerij Dendermonde / Industria / Jachthaven / Pieter Vermeulen / Kappers Köln / ...) |

## Anti-fabricatie-discipline

- Alle cijfers in nieuwe substappen, `invulling_voorbeeld`-blokken en cast-voorbeelden komen uit cast-scenario-defaults of zijn intern consistent met bestaande `concreet_voorbeeld`-blokken in eerdere versies.
- Geen wetsartikelen verzonnen; bestaande grondslag-strings behouden of aangevuld vanuit `references`-arrays.
- `_provenance.inputs` (chunk-ID's) integraal behouden bij elke wijziging.
- Confidence-labels behouden: `grounded` voor wettekst-claims, `inferred-from-aggregation` voor synthese-procedures, `inferred` voor nieuwe edge-redeneringen zonder specifieke wetstekst-grondslag.

## Mens-review-flags

Geen blokkerende issues. Drie kleine punten ter overweging bij een latere pass:

1. **`ifrs-consolidatieraamwerk`** — IFRS 3, 10, 11, 12 zelf zitten niet in het Certificaid-corpus. Het record erkent dat expliciet en blijft op overzichtsniveau. Detail-extractie uit IFRS-tekst zou in een latere fase met die bronnen toegevoegd kunnen worden, maar valt buiten het bereik van schema 1.4 deep-rewrite.

2. **`minderheidsbelangen`** — De berekening houdt geen rekening met derden-aandeel in herberekende stille meerwaarden in de `formules[]` zelf (alleen in stap 5 en valkuilen). Een derde formule "Belangen van derden incl. herberekeningen" zou toevoegbaar zijn, maar verhoogt redundantie zonder didactisch winst (regel 12: één wiskundige relatie per formule; herberekeningen zitten in stap 5).

3. **`wijziging-consolidatiekring`** — Het record vermeldt vijf typische gevallen maar werkt er vier uit als bouwstenen. Het vijfde geval (kringintegratie van voorheen uitgesloten dochters) blijft impliciet via de algemene definitie. Voor een examen volstaat dat; een bijkomende bouwsteen voor dat geval zou de structuur kunnen versterken in een latere pass.

## Tempo

- Start: 2026-05-16T02:25Z (na verkenning + lezen van referentiedocumenten).
- Eind: 2026-05-16T04:20Z.
- Effectieve doorlooptijd: ~115 minuten voor 19 records (verwacht ~100-130 min).
- Geen records overgeslagen behalve `eerste-consolidatie` (was al voltooid in batch 1).

## Verificatie

Mentale check per record na write:
- Bouwstenen (waar van toepassing): alle met `waarom` + `voorbeeld_inline`.
- Stappen (recs 11, 14): alle skeleton-stappen omgezet naar volledige vol-blokken met `wat` + `waarom` + `hoe` + `grondslag` + (voor rekenende stappen) `voorbeeld.substappen`.
- Formules (rec 14): gesplitst in atomair-aparte formules met `variabelen[]` + `invulling_voorbeeld`.
- `_corrected_from`-trail consistent per gewijzigd veld.
- `schema_version: "1.4"` behouden.
- `_provenance.deep_rewrite_2026_05_16`-stempel op elk record toegevoegd (run-id "deep-rewrite-batch-2-concepten", tijdstempels conform werkvolgorde).
- Edges: redeneringen volledig uitgeschreven (geen meer afgekapte zinnen op halve komma).
- Cast-namen: geen "M", "D", "X", "Y", "ABC", "DEF" meer in nieuwe content.

Geen commit uitgevoerd — wacht op menselijke review.
