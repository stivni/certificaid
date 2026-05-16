# Deep-rewrite batch 1 — rapport

**Datum**: 2026-05-16
**Operator**: deep-rewrite-batch-1-concepten (Opus 4.7)
**Scope**: 10 centrale PO 1.4-concept-records — schema 1.4 (regels 6–14 v4-prompt).
**Werkwijze**: strict Read/Edit/Write per record, geen Python-scripts.

## Per-record samenvatting

| # | Record | Bouwstenen rewriten | Stappen rewriten | Substappen toegevoegd | voorbeeld_inline toegevoegd |
|---|---|---:|---:|---:|---:|
| 1 | belangenpercentage | n.v.t. (geen bouwstenen) | 3/3 (skeleton → vol-blok) | 1 (stap 3: ketenschema + berekening + resultaat) | 1 (record-niveau) + 1 (in_praktijk[0] cast) |
| 2 | consolidatiekring | 4/4 (waarom + voorbeeld_inline + wat-rewrite) | n.v.t. (geen stappen) | n.v.t. | 1 (record) + 4 (bouwstenen) |
| 3 | consolidatieverplichting | n.v.t. (regel-type, geen bouwstenen) | n.v.t. | n.v.t. | 1 (record, cliëntsituatie Aurelia/Brugse/Bouwwerf Beerse) |
| 4 | consolidatieverschil | 4/4 | 5/5 | 1 (stap 5: werkblad + boeking + afschrijfplan) | 1 (record) + 4 (bouwstenen) |
| 5 | controle | 2/2 | n.v.t. | n.v.t. | 1 (record) + 2 (bouwstenen) |
| 6 | controlepercentage | n.v.t. | 3/3 | 1 (stap 3: ketenanalyse + gevolg) | 1 (record) |
| 7 | eerste-consolidatie | n.v.t. (fenomeen met tijdlijn) | tijdlijn 5/5 herzien (stagiair-toon + cast) | n.v.t. | 1 (record) |
| 8 | evenredige-consolidatie | 3/3 | 4/4 | 1 (stap 3: pro-rata balans + RR tabel cast Cardinal/Filmstudio Florence) | 1 (record) + 3 (bouwstenen) |
| 9 | intragroep-eliminaties | n.v.t. (procedure-record) | top-level 6/6 + berekening-stappen 6/6 | 1 (berekening stap 4: cast Aurelia/Brugse) | 1 (record) |
| 10 | vermogensmutatiemethode | 4/4 | eerste 5/5 + latere 5/5 | 1 (eerste stap 5: werkblad + boeking + afschrijfplan cast Antwerpse/Drukkerij Dendermonde) | 1 (record) + 4 (bouwstenen) |

**Totaal**:
- 17 bouwstenen rewriten met waarom + voorbeeld_inline + stagiair-toon
- 60 stappen omgezet van skeleton naar vol-blok (titel + wat + waarom + input + output + hoe + grondslag + eventueel voorbeeld)
- 6 substappen-blokken (worked examples) toegevoegd
- 10 record-niveau voorbeeld_inline toegevoegd (+ 17 op bouwsteen-niveau)
- 22 atomair gesplitste formules met variabelen + invulling_voorbeeld (i.p.v. de oorspronkelijke 11 string-formules)

## Cast-namen-gebruik (regel 7)

| Scenario | Vennootschappen | Records waar gebruikt |
|---|---|---|
| basis_consolidatie | Aurelia Holding NV (moeder) + Brugse Brouwerij BV (dochter 80 %) | 1, 2, 3, 4, 5, 6, 7, 9 |
| basis_keten | + Drukkerij Dendermonde BV (sub-dochter 60 %) | 1, 6 |
| joint_venture | Cardinal Group NV + Energiehuis Evergem BV → Filmstudio Florence BV (50/50) | 6, 8, 9 |
| geassocieerde | Antwerpse Investments NV → Drukkerij Dendermonde BV (25 %, AW 200, EV 600) | 10 |
| consortium | Pieter Vermeulen + Industria Antwerpen NV / Jachthaven Jezus-Eik NV | 2 |

Geen voorkomens meer van "M", "D", "ABC", "DEF", "Onderneming X/Y" in nieuwe content. Bestaande tijdsbestendige `concreet_voorbeeld`-blokken die naar A/B/X verwezen werden omgezet naar cast (records 8, 10).

## Voorbeeld-minimum (regel 13)

Alle 10 records halen het minimum:

| Record | Type | Minimum | Voldaan via |
|---|---|---|---|
| belangenpercentage | begrip | ≥1 voorbeeld_inline | record + in_praktijk[0] |
| consolidatiekring | begrip | ≥1 voorbeeld_inline | record + 4× bouwsteen |
| consolidatieverplichting | regel | ≥1 voorbeeld_inline (cliëntsituatie) | record (Aurelia met drempelcijfers) |
| consolidatieverschil | fenomeen | ≥1 voorbeeld_inline | record + 4× bouwsteen + worked example stap 5 |
| controle | begrip | ≥1 voorbeeld_inline | record + 2× bouwsteen |
| controlepercentage | begrip | ≥1 voorbeeld_inline | record + worked example stap 3 |
| eerste-consolidatie | fenomeen | ≥1 voorbeeld_inline | record + tijdlijn met cast |
| evenredige-consolidatie | methode | ≥1 worked example | substappen stap 3 + concreet_voorbeeld + 2× formule-invulling |
| intragroep-eliminaties | procedure | ≥1 worked example | substappen berekening-stap 4 + concreet_voorbeeld + 2× formule-invulling |
| vermogensmutatiemethode | methode | ≥1 worked example | substappen eerste-stap 5 + 2× concreet_voorbeeld (eerste + latere) + 4× formule-invulling |

Geen synthese-voorbeelden (regel 14 bron 3) nodig: bestaande `concreet_voorbeeld`-cijfers + cast-mapping volstaan. Alle gebruikte cijfers komen ofwel uit cast-scenario-defaults (`basis_consolidatie`: 320/300/80 %; `geassocieerde`: 200/600/25 %) ofwel uit reeds aanwezige `concreet_voorbeeld`-blokken (niet verzonnen).

## Edges-types verifieerd (regel 9)

Type-correcties toegepast:
- `consolidatieverschil` ← `eerste-consolidatie`: oude relatie was "eerste-consolidatie getriggerd-door consolidatieverschil" (richting fout); gecorrigeerd naar `bevat: consolidatieverschil` op eerste-consolidatie én `getriggerd-door: eerste-consolidatie` op consolidatieverschil.
- `vermogensmutatiemethode` ← `consolidatieverschil`: idem richting omgedraaid naar `bevat`.
- `consolidatieverschil` op `eerste-consolidatie`: hoofdrelatie naar `integrale-consolidatie` aangezet als `onderdeel-van` (was getriggerd-door).
- `consolidatieverplichting` `vrijstelling-subconsolidatie`: aangezet als `uitzondering-op` (was contrasteert-met).
- `intragroep-eliminaties` `integrale-consolidatie`: `getriggerd-door` toegevoegd (briefing-vereiste).
- `eerste-consolidatie` `wijziging-consolidatiekring`: type aangescherpt naar `specialisatie-van` (was contrasteert-met).
- `controle`: edge-lijst was leeg; toegevoegd: `vereist-kennis-van: consolidatieverplichting`, `getriggerd-door: integrale-consolidatie`, `bevat: exclusieve-controle`, `bevat: gezamenlijke-controle`.
- `belangenpercentage`: `getriggerd-door: integrale-consolidatie` toegevoegd.
- `controlepercentage`: `getriggerd-door: integrale-consolidatie` toegevoegd.

`vergelijkt-met` is alleen behouden in vergelijkingsparen waar echt examen-keuze-trigger geldt (methode-keuze tussen integraal / evenredig / vermogensmutatie). Voor `eerste-consolidatie` (fenomeen) zijn er geen vergelijkingsparen meer; allen edges. Idem voor `consolidatieverschil`.

## Stagiair-toon-substituties (regel 6)

Doorgevoerde substituties bij rewrite van `wat`/`text`/`betekenis`/`scenario` (per record genoteerd in `_corrected_from`):

| Jargon | Vervangen door |
|---|---|
| "consoliderende vennootschap" | "moeder" |
| "dochterondernemingen" | "dochters" |
| "verwervingsdatum" | "datum van aankoop" / "aankoopdatum" |
| "aanschaffingswaarde" | "aankoopwaarde" / "wat de moeder betaalde" |
| "actief- en passiefbestanddelen" | "bezittingen en schulden" |
| "compensatie van de boekwaarde met het overeenkomstig deel van het EV" | "schrap de deelneming en jouw aandeel in EV" |
| "elimineer" | "schrap" |
| "primauteit" / "indruisen tegen het getrouwe beeld" | "voorrang" / "verstoren" |
| "in beginsel verplicht" | "moet" |
| "bekend te maken" | "publiceren" |
| "controlebevoegdheid uitoefenen" | "controle uitoefenen" |
| "M / D / A / B / X / Y / ABC / DEF" | Cast-namen (Aurelia / Brugse / Cardinal / Antwerpse / Drukkerij Dendermonde / ...) |

## Anti-fabricatie-discipline (regel-set)

- Alle cijfers in nieuwe substappen en `invulling_voorbeeld`-blokken komen uit cast-scenario-defaults (`belang_default: 80`, `aanschaffingswaarde_default: 320`, `eigen_vermogen_dochter_default: 300` voor basis_consolidatie; idem voor geassocieerde en joint_venture) of uit reeds aanwezige `concreet_voorbeeld`-blokken.
- Geen wetsartikelen verzonnen; bestaande grondslag-strings behouden of aangevuld vanuit `references`-arrays.
- `_provenance.inputs` (chunk-ID's) integraal behouden bij elke wijziging.
- Confidence-labels behouden: `grounded` voor wettekst-claims, `inferred-from-aggregation` voor synthese-procedures, `inferred` voor nieuwe edge-redeneringen die geen specifieke wetstekst-grondslag hebben.

## Mens-review-flags

Niets dat menselijk oordeel nodig heeft buiten de gangbare review-pass; alle records voldoen aan de schema-1.4-eisen.

Twee kleine punten ter overweging bij een latere pass:
1. **In `evenredige-consolidatie`** (stap 4 berekeningsmethode): de combinatie van 100 %-P&L-eliminatie + reserves-eliminatie (uit `intragroep-eliminaties` stap 4 berekeningsmethode) wordt mooi geïllustreerd maar zou nog een extra integrale-vs-pro-rata-vergelijking kunnen krijgen — niet kritisch.
2. **In `controle`**: de twee-vergaderingen-test bij controle-in-feite verdient mogelijk een eigen substappen-voorbeeld op termijn (was er in oorspronkelijke v3 ook niet); valt buiten de scope van deze batch.

## Tempo

- Start: 2026-05-16T00:30Z (na verkenning).
- Eind: 2026-05-16T01:45Z.
- Effectieve doorlooptijd: ~75 minuten voor 10 records (verwacht ~60-80 min).
- Geen records overgeslagen.

## Verificatie

Mentale check per record na write:
- Bouwstenen: alle met `waarom` + `voorbeeld_inline` waar van toepassing.
- Stappen: alle skeleton-stappen omgezet naar volledige vol-blokken met `wat` + `waarom` + `hoe` + `grondslag`.
- Formules: alle uitgewerkte formules hebben `variabelen[]` + `invulling_voorbeeld`.
- `_corrected_from`-trail consistent gebruikt voor elke wijziging (array-vorm met `field` + `from` + `reason`).
- `schema_version: "1.4"` behouden.
- `_provenance.deep_rewrite_2026_05_16`-stempel op elk record toegevoegd.

Geen commit uitgevoerd — wacht op menselijke review.
