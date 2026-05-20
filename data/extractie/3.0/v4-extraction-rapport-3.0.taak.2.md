# EXTRACT v4 — rapport anchor 3.0.taak.2

**Anchor**: `3.0.taak.2` — *Verlenen van advies en diensten met betrekking tot de overdracht of ontbinding van de onderneming*
**Type**: competentie-anchor (PO 3.0 wave 1 vervolg)
**Datum**: 2026-05-20
**Run-ids**: `concept-extractie-v4-3.0.taak.2-batch{1,2,2b,3}-*`
**Schema**: 1.6

---

## Recordvolume

| Categorie | Aantal |
|---|---:|
| Nieuwe records | 8 |
| Bijgewerkte records | 0 |
| Hernoemd | 0 |
| Verwijderd | 0 |

**Disk-totaal voor/na**: 624 → 632 (+8). Synthese-aantal 51 → 52 (+1). Audit groen.

### Nieuwe records (allemaal `status: seed`)

| ID | Node_type | Linked anchors |
|---|---|---|
| `adviseren-overdrachtsroute-onderneming` | competentie | 3.0.taak.2, 3.0.V, 3.0.VI |
| `begeleiden-due-diligence-overname` | competentie | 3.0.taak.2, 3.0.V |
| `opstellen-overname-verslaggeving-accountant` | competentie | 3.0.taak.2, 3.0.V, 3.0.VI |
| `adviseren-ontbindingsroute-vennootschap` | competentie | 3.0.taak.2, 3.0.IX |
| `begeleiden-vereffening-vennootschap` | competentie | 3.0.taak.2, 3.0.IX |
| `signaleren-risicos-overdracht-of-ontbinding` | competentie | 3.0.taak.2, 3.0.IV/VII/IX/X |
| `exit-routes-onderneming-overzicht` | synthese | 3.0.taak.2, 3.0.V/VI/IX/X |
| `begeleiden-waardering-onderneming-bij-overdracht` | competentie | 3.0.taak.2, 3.0.V, 3.0.VI |

## Edges-overzicht

Alle 8 records verwijzen naar bestaande PO 3.0-I-X kennisclusters via `vereist-kennis-van`-edges. Geen `target_status: pending` — alle targets bestaan op disk:

- 3.0.V-records: `asset-deal-versus-share-deal`, `overnameovereenkomst`, `due-diligence-overname`, `representations-and-warranties`, `indemnification-overname`, `purchase-price-mechanismen`, `closing-condities-precedent`, `confidentiality-overname`, `transfer-bedrijfstak-algemeenheid`
- 3.0.VI: `controleverwerving-methodes`, `aandeelhoudersovereenkomst`
- 3.0.IX: `ontbinding-vennootschap`, `vrijwillige-ontbinding`, `gerechtelijke-ontbinding`, `vereffening-in-een-akte`, `vereffeningsprocedure-klassiek`, `klassieke-versus-een-akte-vereffening`, `vereffenaar`, `staat-van-activa-en-passiva-ontbinding`, `omstandige-staat-vereffening`, `sluiting-vereffening`, `liquidatiebonus`, `heropening-vereffening`, `vereffenaarsaansprakelijkheid`
- 3.0.X: `gerechtelijke-reorganisatie`, `faillissement`, `insolventietriage-beslisboom`, `besloten-voorbereiding-faillissement`, `verdachte-periode-faillissement`
- 3.0.IV: `nettoactieftest`, `liquiditeitstest-bv`
- 3.0.VII: `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering`
- PO 1.7: `inbreng-in-natura-verslag`, `quasi-inbreng-verslag`, `fusie-splitsing-controleopdracht`

Synthese `exit-routes-onderneming-overzicht` heeft 9 `vereist-kennis-van`-edges naar cluster-records (gebaseerd-op-concepten).

## Migraties oud → nieuw schema

Geen — alle 8 records zijn nieuw geschreven volgens schema 1.6 (geen oude `doel`/`voorbeeld_inline`/`fenomeen`/`actor`/`skill`-velden).

## Gaps.json — toegevoegde entries (4 nieuw)

| Aspect | Onderwerp | Prio |
|---|---|---|
| `records.ontbreekt` | Kapstok-clusters `fusie-vennootschappen` + `splitsing-vennootschappen` (Boek 12 WVV) | midden |
| `records.ontbreekt` | `overdracht-onder-gerechtelijk-gezag` (WER art. XX.85-XX.87) | midden |
| `records.ontbreekt` | `familieonderneming-gunsttarief-vlaanderen` (schenkings-/successierechten gunsttarief) | laag |
| `context-edge-ontbreekt` | `fusie-splitsing-controleopdracht` mist `onderdeel-van` naar nog-niet-bestaande fusie/splitsing-clusters | laag |

Gaps-totaal: 1016 → 1020.

## Claims inferred-from-aggregation

- `adviseren-overdrachtsroute-onderneming.situering` — synthese over WVV Boek 12 + IBA M&A Guide
- `begeleiden-due-diligence-overname.situering` — IBA-praktijkgids + vakdoctrine (geen wet)
- `signaleren-risicos-overdracht-of-ontbinding.situering` — WVV + WER + WIB92 + IESBA aggregaat
- `exit-routes-onderneming-overzicht.situering` + `definitie` — synthese over zes routes
- `begeleiden-waardering-onderneming-bij-overdracht.situering` — IBA + vakdoctrine

## Open observaties

1. **Bundle-bias richting ontbinding/vereffening.** Top-120 chunks van 2501 zijn dominant CBN-2022/04, CBN-2022/06, CBN-2022/07, MvT-WVV Boek 2 (ontbinding-vereffening artikelen 2:70-2:107), ITAA-norm-ontbinding-vereffening. Boek 12 (fusie/splitsing) verschijnt mager (1 chunk WVV 12:78, 2 MvT-chunks). M&A-stof komt vooral uit IBA-bron, niet uit ITAA-corpus. Logisch — accountantsrol-corpus is sterk ontbindings-georiënteerd; M&A is grotendeels juridisch/contractueel domein. De gemaakte competentie-records leggen daarom adviserende rol vast met inbedding in bestaande PO 3.0.V/VI-stof.

2. **Geen waarderings-theorie-records aangemaakt.** Bewust binnen scope-grens gehouden: `begeleiden-waardering-onderneming-bij-overdracht` is competentie-laag (toepassing) en verwijst naar PO 1.3 / 2.5 voor de diepe waarderingstheorie (WACC-bepaling, DCF-mechanica, peer-multiples-databases). Dit voorkomt PO-grens-overschrijding.

3. **Fusie/splitsing-stof niet in eigen records.** Gerefereerd via competenties en synthese, maar zonder eigen kapstok-cluster. Drie open gaps documenteren dit. Bundel bevatte voldoende seed-materiaal (MvT-WVV-2018 art. 12:58, 12:61; WVV art. 12:78) voor een latere extract-pass van 1-2 cluster-records, mits ankerbundel verbreed wordt naar 3.0.V-of-VI-fusie.

4. **IBA-bron als concretiseringsbron**, niet grondslag. Gerefereerd in `situering` en `voorbeelden` met `confidence: inferred-from-aggregation`. Voorbeelden zoals "5,5x EBITDA peer-multiple" zijn plausibel maar niet hardgecodeerd; concrete sector-multiples horen in cijferzakboekje-domein.

5. **Cross-PO programmaonderdelen-veld correct gezet**: `opstellen-overname-verslaggeving-accountant.programmaonderdelen = [3.0, 1.7]` (verslag-laag zit ook in PO 1.7); `begeleiden-waardering-onderneming-bij-overdracht.programmaonderdelen = [3.0, 1.3, 2.5]`.

6. **Procedure-grondslag verdeling**:
   - 3 competenties wettelijk-zwaar (75-80%): `opstellen-overname-verslaggeving-accountant`, `adviseren-ontbindingsroute-vennootschap`, `begeleiden-vereffening-vennootschap`
   - 3 competenties praktijk-zwaar (60-90%): `adviseren-overdrachtsroute-onderneming`, `begeleiden-due-diligence-overname`, `begeleiden-waardering-onderneming-bij-overdracht`
   - 1 hybride: `signaleren-risicos-overdracht-of-ontbinding` (55/45)

## Zelf-evaluatie

| Criterium | Status |
|---|---|
| 6-12 competentie-records | 7 competenties + 1 synthese = 8 ✓ |
| Cross-PO `vereist-kennis-van`-edges | Ja, naar 35+ unique targets ✓ |
| Geen bron-genaamde records | OK ✓ |
| Geen dupliceren van 3.0.I-X-begrippen | OK — alleen verwezen ✓ |
| Geen fiscale berekeningen (PO 2.x) | Liquidatiebonus + roerende voorheffing alleen als adviserende toepassing (geen tarief-tabellen) ✓ |
| Geen diepe waarderingstheorie | Bewust vermeden in record 8 ✓ |
| 1-2 syntheses | 1 (`exit-routes-onderneming-overzicht`) ✓ |
| Records-API + worktree-cwd | Alle saves via `os.chdir(hoofdrepo)` + `save_record` ✓ |
| Records vroeg en in mini-batches | Batch 1 (3) + batch 2 (2) + batch 2b (1) + batch 3 (2) ✓ |
| Audit groen na save | 632 records, sync ✓ |

## Volgende stappen (suggesties voor coordinator)

1. **Boek 12-extract**: trigger een verbredings-pass voor fusie/splitsing als eigen anchor of als boek-12-bundle. Drie gaps wijzen hierop.
2. **VERIFY-run** op deze 8 records om edge-richting (zijn `verwijst-naar` vs `vereist-kennis-van` correct?) en cross-record cijfer-consistentie (liquidatiebonus-rekenvoorbeeld in 2 records) te checken.
3. **PO 3.0.taak.3 (advies bij financiering)** als volgende wave-stap — dezelfde competentie-structuur, zwaartepunt PO 3.0.II/IV/VIII.
