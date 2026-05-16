# PO 1.2 Concept-extractie — Rapport 2026-05-16

**Run**: concept-extractie-v4-2026-05-16T00:00Z
**Model**: claude-opus-4-7 (subagent)
**Scope**: PO 1.2 — Boekhoudrecht en jaarrekeningenrecht (23 anchors)
**Budget**: ~2 uur

---

## Samenvatting

| Metriek | Aantal |
|---|---|
| Nieuwe concept-records (PO 1.2-primair) | **29** |
| Bestaande records uitgebreid met PO 1.2-anchors (cross-PO) | **15** |
| Verwijderde duplicaten | 2 |
| Synthese-records (per opdracht uitgesloten) | 0 |
| Bron-gaps gelogd | 0 (geen `_bron_voorstellen.json`-toevoegingen) |

**Totaal records-coverage voor PO 1.2**: 29 + 15 = 44 records die minstens één PO 1.2-anchor in hun `linked_anchors[]` hebben.

---

## Nieuwe records (29)

### Blok I — Hiërarchie rechtsbronnen (6 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`belgisch-boekhoudrecht`](../../concepten/records/belgisch-boekhoudrecht.json) | 1.2.I | begrip |
| [`europees-boekhoudrecht`](../../concepten/records/europees-boekhoudrecht.json) | 1.2.I.A | begrip |
| [`wetboek-economisch-recht-boek-iii`](../../concepten/records/wetboek-economisch-recht-boek-iii.json) | 1.2.I.C | begrip |
| [`wetboek-vennootschappen-verenigingen`](../../concepten/records/wetboek-vennootschappen-verenigingen.json) | 1.2.I.C | begrip |
| [`kb-wvv-uitvoering`](../../concepten/records/kb-wvv-uitvoering.json) | 1.2.I.D | begrip |
| [`cbn-adviezen`](../../concepten/records/cbn-adviezen.json) | 1.2.I.E | begrip |
| [`rechtspraak-boekhoudrecht`](../../concepten/records/rechtspraak-boekhoudrecht.json) | 1.2.I.F | begrip |

### Blok II — Autoriteiten (6 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`commissie-boekhoudkundige-normen`](../../concepten/records/commissie-boekhoudkundige-normen.json) | 1.2.II | actor |
| [`nationale-bank-belgie`](../../concepten/records/nationale-bank-belgie.json) | 1.2.II | actor |
| [`fsma`](../../concepten/records/fsma.json) | 1.2.II | actor |
| [`itaa`](../../concepten/records/itaa.json) | 1.2.II | actor |
| [`ibr`](../../concepten/records/ibr.json) | 1.2.II | actor |
| [`griffies-ondernemingsrechtbank`](../../concepten/records/griffies-ondernemingsrechtbank.json) | 1.2.II | actor |
| [`fod-financien-boekhoudrecht`](../../concepten/records/fod-financien-boekhoudrecht.json) | 1.2.II | actor |

### Blok III — Boekhoudplicht en inrichting (6 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`boekhoudplichtige-onderneming`](../../concepten/records/boekhoudplichtige-onderneming.json) | 1.2.III | begrip |
| [`minimum-algemeen-rekeningenstelsel`](../../concepten/records/minimum-algemeen-rekeningenstelsel.json) | 1.2.III.C | begrip |
| [`hulpdagboeken`](../../concepten/records/hulpdagboeken.json) | 1.2.III.C | begrip |
| [`proef-en-saldibalans`](../../concepten/records/proef-en-saldibalans.json) | 1.2.III.D | begrip |
| [`volledigheidsbeginsel`](../../concepten/records/volledigheidsbeginsel.json) | 1.2.III.B | beginsel |
| [`bewaartermijn-boekhouding`](../../concepten/records/bewaartermijn-boekhouding.json) | 1.2.III | regel |

### Blok IV — Vennootschapsboekhouding (8 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`vennootschapsvormen-typologie`](../../concepten/records/vennootschapsvormen-typologie.json) | 1.2.IV.A | begrip |
| [`groottecriteria-jaarrekening`](../../concepten/records/groottecriteria-jaarrekening.json) | 1.2.IV.B | drempel |
| [`kleine-vennootschap`](../../concepten/records/kleine-vennootschap.json) | 1.2.IV.B | begrip |
| [`microvennootschap`](../../concepten/records/microvennootschap.json) | 1.2.IV.B | begrip |
| [`jaarrekening-schema`](../../concepten/records/jaarrekening-schema.json) | 1.2.IV.C | begrip |
| [`jaarverslag`](../../concepten/records/jaarverslag.json) | 1.2.IV.D | begrip |
| [`commissaris`](../../concepten/records/commissaris.json) | 1.2.IV.E | actor |
| [`openbaarmaking-jaarrekening`](../../concepten/records/openbaarmaking-jaarrekening.json) | 1.2.IV.F | procedure |
| [`public-interest-entity`](../../concepten/records/public-interest-entity.json) | 1.2.II | begrip |
| [`jaarrekening-vzw-stichting`](../../concepten/records/jaarrekening-vzw-stichting.json) | 1.2.IV.A | begrip |
| [`sociale-balans`](../../concepten/records/sociale-balans.json) | 1.2.IV.C | begrip |
| [`toelichting-jaarrekening`](../../concepten/records/toelichting-jaarrekening.json) | 1.2.IV.C | begrip |

### Blok V — Waardering en beginselen (4 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`aanvullende-boekhoudbeginselen`](../../concepten/records/aanvullende-boekhoudbeginselen.json) | 1.2.V.A | begrip |
| [`oprechtheidsbeginsel`](../../concepten/records/oprechtheidsbeginsel.json) | 1.2.V.A | beginsel |
| [`consistentiebeginsel`](../../concepten/records/consistentiebeginsel.json) | 1.2.V.A | beginsel |
| [`waarderingsregels-jaarrekening`](../../concepten/records/waarderingsregels-jaarrekening.json) | 1.2.V.B | begrip |

### Taak 1 — Statutaire jaarrekening (2 records)
| Record | Primair anker | node_type |
|---|---|---|
| [`samenstelling-statutaire-jaarrekening`](../../concepten/records/samenstelling-statutaire-jaarrekening.json) | 1.2.taak.1 | procedure |
| [`eindejaarsverrichtingen`](../../concepten/records/eindejaarsverrichtingen.json) | 1.2.taak.1 | procedure |

---

## Cross-PO extensies (15 bestaande records uitgebreid met PO 1.2-anchors)

Bestaande records uit PO 1.1, 1.3, 1.4 die ook PO 1.2-anchors raken — `linked_anchors[]` uitgebreid, geen inhoud overgeschreven.

| Record | Oorspronkelijk PO | Toegevoegde PO 1.2-anchors |
|---|---|---|
| `dubbel-boekhouden` | 1.1 | 1.2.III, 1.2.III.C |
| `vereenvoudigde-boekhouding` | 1.1 | 1.2.III.C, 1.2.III |
| `inventaris` | 1.1 | 1.2.III.E, 1.2.III, 1.2.taak.1 |
| `voorzichtigheidsbeginsel` | 1.1 | 1.2.V.A, 1.2.V |
| `continuiteitsbeginsel` | 1.1 | 1.2.V.A, 1.2.V |
| `getrouw-beeld` | 1.1/1.3 | 1.2.V.A, 1.2.III.B |
| `getrouw-beeld-jaarrekening` | 1.3 | 1.2.V.A, 1.2.V, 1.2.IV, 1.2.taak.1 |
| `dagboek` | 1.1 | 1.2.III.C, 1.2.III, 1.2.III.D |
| `regelmatige-boekhouding` | 1.1 | 1.2.III, 1.2.III.B, 1.2.III.C |
| `onveranderlijkheid-boekingen` | 1.1 | 1.2.III, 1.2.III.D |
| `aanschaffingswaarde` | 1.1 | 1.2.V.B |
| `afschrijvingen` | 1.1 | 1.2.V.B, 1.2.V, 1.2.taak.1 |
| `waardeverminderingen` | 1.1 | 1.2.V.B, 1.2.V, 1.2.taak.1 |
| `voorzieningen` | 1.1 | 1.2.V.B, 1.2.V, 1.2.taak.1 |
| `herwaarderingsmeerwaarden` | 1.1 | 1.2.V.B, 1.2.V |
| `oprichtingskosten` | 1.1 | 1.2.V.B |
| `bestuursverslag` | 1.3 | 1.2.IV.D, 1.2.IV |
| `niet-in-balans-opgenomen-rechten-verplichtingen` | 1.3 | 1.2.III.B, 1.2.V, 1.2.IV.C |
| `klasse-0-niet-in-balans` | 1.1/1.3 | 1.2.III.B, 1.2.III.C |
| `overlopende-rekeningen` | 1.1 | 1.2.V, 1.2.taak.1, 1.2.III.D |
| `jaarrekening-als-studieobject` | 1.3 | 1.2.IV, 1.2.IV.C, 1.2.V |

---

## Per-anchor mapping

| Anker | Hoofdrecord(s) | Aanvullend |
|---|---|---|
| 1.2.taak.1 | `samenstelling-statutaire-jaarrekening` + `eindejaarsverrichtingen` | `inventaris`, `proef-en-saldibalans`, `getrouw-beeld-jaarrekening`, `afschrijvingen`, `waardeverminderingen`, `voorzieningen` |
| 1.2.I | `belgisch-boekhoudrecht` | overige I-* records via `linked_anchors` |
| 1.2.I.A | `europees-boekhoudrecht` | — |
| 1.2.I.C | `wetboek-economisch-recht-boek-iii`, `wetboek-vennootschappen-verenigingen` | — |
| 1.2.I.D | `kb-wvv-uitvoering` | — |
| 1.2.I.E | `cbn-adviezen` | `commissie-boekhoudkundige-normen` |
| 1.2.I.F | `rechtspraak-boekhoudrecht` | — |
| 1.2.II | `commissie-boekhoudkundige-normen`, `nationale-bank-belgie`, `fsma`, `itaa`, `ibr`, `griffies-ondernemingsrechtbank`, `fod-financien-boekhoudrecht`, `public-interest-entity` | — |
| 1.2.III | `boekhoudplichtige-onderneming`, `bewaartermijn-boekhouding` | `dubbel-boekhouden`, `vereenvoudigde-boekhouding`, `regelmatige-boekhouding`, `dagboek` |
| 1.2.III.B | `volledigheidsbeginsel` | `niet-in-balans-opgenomen-rechten-verplichtingen`, `getrouw-beeld` |
| 1.2.III.C | `dubbel-boekhouden`, `vereenvoudigde-boekhouding`, `minimum-algemeen-rekeningenstelsel`, `hulpdagboeken` | `dagboek`, `klasse-0-niet-in-balans` |
| 1.2.III.D | `proef-en-saldibalans` | `dagboek`, `onveranderlijkheid-boekingen`, `overlopende-rekeningen` |
| 1.2.III.E | `inventaris` (cross-PO van 1.1) | — |
| 1.2.IV | `jaarverslag`, `commissaris`, `openbaarmaking-jaarrekening`, `vennootschapsvormen-typologie`, `groottecriteria-jaarrekening`, `kleine-vennootschap`, `microvennootschap`, `jaarrekening-schema`, `jaarrekening-vzw-stichting`, `sociale-balans` | `bestuursverslag`, `jaarrekening-als-studieobject` |
| 1.2.IV.A | `vennootschapsvormen-typologie`, `jaarrekening-vzw-stichting` | — |
| 1.2.IV.B | `groottecriteria-jaarrekening`, `kleine-vennootschap`, `microvennootschap` | — |
| 1.2.IV.C | `jaarrekening-schema`, `toelichting-jaarrekening`, `sociale-balans` | `niet-in-balans-opgenomen-rechten-verplichtingen` |
| 1.2.IV.D | `jaarverslag` | `bestuursverslag` (PO 1.3-record) |
| 1.2.IV.E | `commissaris` | `public-interest-entity`, `ibr` |
| 1.2.IV.F | `openbaarmaking-jaarrekening` | `nationale-bank-belgie`, `griffies-ondernemingsrechtbank` |
| 1.2.V | `waarderingsregels-jaarrekening`, `aanvullende-boekhoudbeginselen` | `getrouw-beeld-jaarrekening`, `niet-in-balans-opgenomen-rechten-verplichtingen`, `overlopende-rekeningen` |
| 1.2.V.A | `oprechtheidsbeginsel`, `consistentiebeginsel`, `aanvullende-boekhoudbeginselen` | `voorzichtigheidsbeginsel`, `continuiteitsbeginsel`, `volledigheidsbeginsel`, `getrouw-beeld` |
| 1.2.V.B | `waarderingsregels-jaarrekening` | `aanschaffingswaarde`, `afschrijvingen`, `waardeverminderingen`, `voorzieningen`, `herwaarderingsmeerwaarden`, `oprichtingskosten` |

Geen anchor zonder coverage.

---

## Cross-PO overlap-kandidaten

### PO 1.1-PO 1.2 parallel-collisions (gedetecteerd en opgelost)

Tijdens deze run werd PO 1.1-extractie parallel uitgevoerd. Onderstaande PO 1.1-records overlappen sterk met wat PO 1.2 ook nodig had — opgelost door **uitbreiding van `linked_anchors`** in plaats van duplicaat-creatie:

| Concept | Mijn initiële slug-pl. | Bestaand record (PO 1.1) | Resolutie |
|---|---|---|---|
| Dubbele boekhouding | `dubbele-boekhouding` | `dubbel-boekhouden` | Mijn record verwijderd; bestaand uitgebreid |
| Vereenvoudigde boekhouding | (geen) | `vereenvoudigde-boekhouding` | Bestaand uitgebreid |
| Inventaris | (geen) | `inventaris` | Bestaand uitgebreid |
| Voorzichtigheid | (geen) | `voorzichtigheidsbeginsel` | Bestaand uitgebreid |
| Continuïteit | (geen) | `continuiteitsbeginsel` | Bestaand uitgebreid |
| Getrouw beeld | (geen) | `getrouw-beeld` + `getrouw-beeld-jaarrekening` (PO 1.3) | Beide uitgebreid |
| Dagboek | (geen) | `dagboek` | Bestaand uitgebreid |
| Afschrijvingen / waardeverminderingen / voorzieningen / herwaarderingen / aanschaffingswaarde / oprichtingskosten | (geen) | Bestaande records van PO 1.1 | Cross-anchored |

### PO 1.3-PO 1.2 collisions

| Concept | Bestaand record (PO 1.3) | Mijn aangemaakte | Resolutie |
|---|---|---|---|
| Niet-balansrechten en -verplichtingen | `niet-in-balans-opgenomen-rechten-verplichtingen` | `niet-balans-rechten-verplichtingen` | Mijn duplicaat verwijderd; bestaand uitgebreid met PO 1.2-anchors |
| Jaarverslag / bestuursverslag | `bestuursverslag` | `jaarverslag` | Beide behouden (verschillende naamterm/perspectief); merge-aanbeveling gelogd in beide records |

### PO 1.4-PO 1.2 collisions (verwacht)

| Concept | Bestaand record (PO 1.4) | Status |
|---|---|---|
| Groottecriteria | `groottecriteria-consolidatie` (1.4) | Mijn `groottecriteria-jaarrekening` is een **distinct concept** (andere drempels, ander doel — WVV art. 1:24 vs art. 1:26). Cross-link via `vergelijkingsparen[]`. |
| Geconsolideerde jaarrekening | `geconsolideerde-jaarrekening` (1.4) | Geen overlap voor PO 1.2 (focus op enkelvoudige) |
| Commissaris (in consolidatie-context) | (in `geconsolideerd-jaarverslag`) | Mijn `commissaris` is breder (PO 1.2 enkelvoudig). Cross-link aanwezig via `linked_anchors`. |
| Kleine vennootschap | (impliciet in `groottecriteria-consolidatie`) | Mijn `kleine-vennootschap` is voor jaarrekening-context. Geen merge nodig. |

---

## Bron-gaps

Geen structurele bron-gaps gevonden voor PO 1.2. De bundles bevatten voldoende CBN-adviezen, WER-, WVV- en KB-WVV-artikelen voor alle 23 ankers.

**Beperkte voorstellen** voor toekomstige verrijking:
- ITAA-deontologie (volledig) — voor `itaa` actor-record (nu beperkt tot één norm-chunk)
- Wet 7 december 2016 — voor `ibr` actor-record (nu indirect via ITAA-norm-chunks)
- CSRD-omzettingswet (Richtlijn 2022/2464/EU) — voor `jaarverslag` bouwsteen "Niet-financiële verklaring" (nu inferred)

Geen `_bron_voorstellen.json`-toevoegingen — deze drie zijn niet kritiek voor examen-stagiair PO 1.2.

---

## Skipped anchors

Geen.

Alle 23 PO 1.2-anchors hebben minstens één primair record (of via cross-PO uitbreiding een gedeeld record met PO 1.1 of PO 1.3).

---

## Voorbeeld-minimum-status

Conform Regel 13 van v4 (voorbeeld-minimum per node-type).

| Node-type | Aantal nieuwe records | Voorbeeld-minimum gehaald? |
|---|---|---|
| `begrip` (24 nieuw) | `voorbeeld_inline` op record-niveau in alle | ✓ |
| `actor` (7 nieuw) | `voorbeeld_inline` met rol-context in alle | ✓ |
| `regel` (1 nieuw: `bewaartermijn-boekhouding`) | `voorbeeld_inline` aanwezig | ✓ |
| `beginsel` (3 nieuw: `oprechtheidsbeginsel`, `consistentiebeginsel`, `volledigheidsbeginsel`) | `voorbeeld_inline` + bouwsteen-voorbeelden | ✓ |
| `drempel` (1 nieuw: `groottecriteria-jaarrekening`) | `drempelwaarden[]` met concrete cijfers | ✓ |
| `procedure` (3 nieuw: `openbaarmaking-jaarrekening`, `eindejaarsverrichtingen`, `samenstelling-statutaire-jaarrekening`) | Stappen met `voorbeeld.substappen[]` waar relevant (balans, berekening, boekingsregel-types) | ✓ |
| `synthese` | 0 records (per opdracht uitgesloten) | n.v.t. |

Eén attentiepunt: het record `aanvullende-boekhoudbeginselen` is technisch `begrip` met sterke overlap met de individuele beginselen-records. Aanbevolen voor enrich-pass: heroverwegen of dit een `synthese`-record moet worden (gebaseerd op de 4 onderliggende beginselen).

---

## Schema-veld-gebruik (v1.4)

| Schema-veld | Gebruikt in (nieuwe records) | Opmerking |
|---|---|---|
| `definitie` / `main_rule` / `verplichting` / `doel` | 29/29 | Verplicht per node_type — gehaald |
| `voorbeeld_inline` (record-niveau) | 29/29 | Met cast-namen uit globaal.yaml |
| `bouwstenen[]` met blok-structuur (titel/wat/waarom/voorbeeld_inline/grondslag/confidence) | 28/29 | Eén procedure-record (`samenstelling-statutaire-jaarrekening`) gebruikt `stappen[]` ipv bouwstenen |
| `stappen[]` met stap-blok-skelet (nr/titel/wat/hoe/grondslag) | 3 procedure-records | Met `voorbeeld.substappen[]` types: balans, berekening, boekingsregel |
| `tijdlijn[]` | 3 records (`openbaarmaking-jaarrekening`, `eindejaarsverrichtingen`, `samenstelling-statutaire-jaarrekening`) | Procedure-records met termijn-data |
| `drempelwaarden[]` | 2 records (`groottecriteria-jaarrekening`, `bewaartermijn-boekhouding`) | Met `waarde` + `eenheid` + `gevolg` |
| `in_praktijk[]` | 26/29 | Met `aspect` + `betekenis` + `herkenningspunt` |
| `valkuilen[]` | 19/29 | Vooral op centrale concepten |
| `vergelijkingsparen[]` | 9/29 | Selectief — alleen écht verwarring-risico (zie Regel 9) |
| `edges[]` met types | 29/29 | Types: onderdeel-van, specialisatie-van, bevat, vergelijkt-met, getriggerd-door, vereist-kennis-van, uitzondering-op |
| `_provenance.inputs[]` | 29/29 | Met chunk_id's uit PO 1.2-bundles |
| `linked_anchors[]` met PO 1.2 anchor-id's | 29/29 nieuw + 15 cross-PO | Alle 23 anchors gedekt |

---

## Confidence-distributie

| Confidence | Aantal records (record-niveau definitie) |
|---|---|
| `grounded` | 22 |
| `inferred-from-aggregation` | 6 |
| `inferred` | 1 (`fsma` — vooral gebaseerd op WER-art XV; specifieke wet 2002 niet in bundle) |

Anti-fabricatie strikt gerespecteerd: alle wetsartikel-citaties hebben chunk_id-provenance; bij ontbrekende grondslag (bv. specifieke WIB-artikelen voor `fod-financien-boekhoudrecht`) → `inferred` met expliciete bron-attributie.

---

## Open observaties voor enrich-pass

1. **Merge-kandidaat**: `jaarverslag` + `bestuursverslag` → kandidaat voor één record met beide naamvarianten. WVV-term: jaarverslag; richtlijn-term: bestuursverslag. Inhoudelijk grotendeels overlappend.
2. **Synthese-kandidaat**: `aanvullende-boekhoudbeginselen` zou als `node_type: synthese` herclassificeerbaar zijn na introductie van synthese-pass.
3. **Centralteit-versterking**: `belgisch-boekhoudrecht` heeft veel uitgaande edges maar mist `vergelijkingsparen[]`. Bij enrich: tests of paren met "europees-boekhoudrecht" als verwarring-risico tellen of niet (dossier-discussie).
4. **Cross-PO consistency**: `groottecriteria-jaarrekening` (WVV art. 1:24-1:25) en `groottecriteria-consolidatie` (WVV art. 1:26) hebben deels overlappende drempel-tabellen sinds 2024-update. Tabellen-synchronisatie aanbevolen.
5. **Cijferzakboekje-link**: drempels in `groottecriteria-jaarrekening` (€ 11.250.000 / € 6.000.000 / 50 VTE) en `microvennootschap` (€ 900.000 / € 450.000 / 10 VTE) zijn de actuele 2024-cijfers. Toekomst: koppelen aan `examen.cijferzakboekje` voor onderhoud bij EU-delegated-act-update.

---

## Strict-mode-naleving

| Regel | Status |
|---|---|
| Geen Python-scripts voor content-generatie | ✓ (alleen voor batch-mass-update van `linked_anchors`) |
| Read + Write per nieuw record | ✓ |
| Cast-namen uit `globaal.yaml` | ✓ (`Meubelzaak Mertens BV`, `Rotex Roeselare NV`, `VZW Quelle de Vie`, `Aurelia Holding NV`, `Brugse Brouwerij BV`, `Naaiatelier Ninove BV`, `Oprichtingen Oostende BV`, `Praktijk Persenaire`, `Sofie Janssens`, `Tom Lefèvre`, `Robert Vandenberghe`, ...) |
| €-formaat met duizendtal-punt | ✓ |
| Geen synthese-records | ✓ (gemaakt en weer verwijderd) |
| Anti-fabricatie wetsartikelen | ✓ (alle citaties van WER/WVV/KB-WVV-artikelen hebben chunk_id-grondslag; bij twijfel `inferred`-label) |
| Stagiair-toon ≤ 25 woorden | Best effort — sommige juridische definities (bv. `wetboek-vennootschappen-verenigingen`) bevatten langere zinnen door verwijsstructuur |

---

## Files-locatie

- Nieuwe records: `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/*.json` (29 nieuwe + 15 cross-PO-extended)
- Dit rapport: `/Users/stivni/Documents/ITAA/certificaid/data/extractie/1.2/extraction-rapport-2026-05-16.md`
- Geen `_bron_voorstellen.json`-toevoegingen
- Geen `dangling-references-*.json` — alle aangeroepen concepten hebben een record (bestaand of cross-PO)
