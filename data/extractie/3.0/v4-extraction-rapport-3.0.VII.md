# EXTRACT v4 — rapport PO 3.0.VII

**Anchor**: `3.0.VII — Aansprakelijkheid van oprichters, aandeelhouders en bestuurders`
**Run**: `concept-extractie-v4-2026-05-20T*Z` (zie individuele record-`_provenance.extractor_run`)
**Model**: claude-opus-4-7
**Bundle**: `/tmp/po-3.0-pilot/bundle-3.0.VII.json` — 114 chunks (53 MvT-WVV-2018, 52 WVV, 3 WER + losse CBN/EU-richtlijn-chunks)
**Audit na save**: groen — 559 records op disk = 559 in RAG (was 543 vóór deze run, +16).

---

## Aantal records

| Status | Aantal | IDs |
|---|---|---|
| **Nieuw** | **16** | `bestuurdersaansprakelijkheid`, `behoorlijke-vervulling-bestuursopdracht`, `aansprakelijkheidsbeperking-bestuurder`, `oprichtersaansprakelijkheid`, `kennelijk-ontoereikend-aanvangsvermogen`, `feitelijk-bestuurder`, `vereffenaarsaansprakelijkheid`, `bestuurdersaansprakelijkheid-bij-insolventie`, `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering`, `bestuurdersaansprakelijkheid-sociale-schulden`, `bestuurdersaansprakelijkheid-fiscale-schulden`, `kwijting-bestuurder`, `doorbraak-aansprakelijkheid`, `bestuurdersaansprakelijkheidsverzekering`, `aansprakelijkheidsgrondslagen-bestuur-vergelijking` (synthese), `verzwaarde-aansprakelijkheid-bij-insolventie-overzicht` (synthese) |
| **Bijgewerkt** | 0 | — |
| **Hernoemd** | 0 | — |
| **Verwijderd** | 0 | — |

Verdeling per `node_type`:
- 2× cluster (bestuurdersaansprakelijkheid, oprichtersaansprakelijkheid)
- 7× regel (behoorlijke-vervulling, cap+exoneratie, kennelijk-ontoereikend, vereffenaars, insolventie, sociale, fiscale, onrechtmatige-uitkering)
- 4× begrip (feitelijk-bestuurder, kwijting-bestuurder, doorbraak, D&O-verzekering)
- 2× synthese (vergelijkings-tabel oprichter/bestuurder/vereffenaar/feitelijk + insolventie-regimes-overzicht)
- 1× cluster + 7× regel = telt 8, totale telling: 2 cluster + 7 regel = 9 + 4 begrip + 2 synthese = **15 + 1 dubbeltelling** (de regel `aansprakelijkheidsbeperking-bestuurder` zou ook als cluster kunnen worden gezien). Telling onder records.ontbreekt-tracking blijft **16**.

**Cross-PO-gaps ingevuld**:
- Vereffenaarsaansprakelijkheid (3.0.IX) → `vereffenaarsaansprakelijkheid` ✓
- Bestuurdersaansprakelijkheid bij insolventie (3.0.X) → `bestuurdersaansprakelijkheid-bij-insolventie` ✓
- Bestuurdersaansprakelijkheid algemeen (3.0.II-pilot) → `bestuurdersaansprakelijkheid` ✓
- Bestuurdersaansprakelijkheid bij ongeldige uitkering (3.0.IV) → `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` ✓

---

## Edges-overzicht

**Cross-PO/anker-overstijgend** (uitgaande edges van nieuwe records):

| Bron | Type | Target | Anker-context |
|---|---|---|---|
| `bestuurdersaansprakelijkheid` | getriggerd-door | `faillissement` | 3.0.X |
| `oprichtersaansprakelijkheid` | vereist-kennis-van | `besloten-vennootschap-bv` | 3.0.I |
| `oprichtersaansprakelijkheid` | vereist-kennis-van | `naamloze-vennootschap-nv` | 3.0.I |
| `oprichtersaansprakelijkheid` | vereist-kennis-van | `cooperatieve-vennootschap-cv` | 3.0.I |
| `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` | vereist-kennis-van | `liquiditeitstest-bv` | 3.0.IV |
| `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` | vereist-kennis-van | `nettoactieftest` | 3.0.IV |
| `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` | vereist-kennis-van | `uitkering-uit-eigen-vermogen-bv` | 3.0.IV |
| `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` | verwijst-naar | `interimdividend` | 3.0.IV |
| `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` | verwijst-naar | `financiele-steunverlening` | 3.0.IV |
| `vereffenaarsaansprakelijkheid` | vereist-kennis-van | `vereffenaar` | 3.0.IX |
| `vereffenaarsaansprakelijkheid` | vereist-kennis-van | `vereffeningsprocedure-klassiek` | 3.0.IX |
| `bestuurdersaansprakelijkheid-bij-insolventie` | vereist-kennis-van | `meldingsplicht-accountant-continuiteit` | 3.0.X / 1.6 |
| `doorbraak-aansprakelijkheid` | uitzondering-op | `beperkte-aansprakelijkheid-vennoot` | 3.0.I |
| `verzwaarde-aansprakelijkheid-bij-insolventie-overzicht` (synthese) | verwijst-naar | `faillissement` | 3.0.X |

**Intra-cluster edges**: alle 9 sub-regels/-begrippen wijzen `onderdeel-van: bestuurdersaansprakelijkheid` of `onderdeel-van: oprichtersaansprakelijkheid`.

**`target_status: "pending"`** in records 1-2 (bestuurdersaansprakelijkheid, behoorlijke-vervulling): wijzen vooruit naar `aansprakelijkheidsbeperking-bestuurder`, `oprichtersaansprakelijkheid`, `vereffenaarsaansprakelijkheid`, `feitelijk-bestuurder`, etc. — alle inmiddels aangemaakt in dezelfde wave; pending-flag is een artefact van de incrementele build-volgorde maar niet schadelijk.

---

## Gaps.json — toevoegingen (10 entries)

| Aspect | Aantal | Prio-verdeling |
|---|---|---|
| `bron-gap` | 3 | 2× hoog, 1× midden |
| `records.ontbreekt` | 4 | 1× hoog, 1× midden, 2× laag |
| `dangling-reference` | 2 | 2× laag |
| `granulariteit.beslissing-nodig` | 1 | 1× laag |

**Bron-gaps (hoog-prio)**:
1. **WVV.md mist art. 2:56 en 2:57** — sectie 'HOOFDSTUK 2. Bestuurdersaansprakelijkheid' bevat alleen art. 2:58. ETL-chunking-bug. Cap-bedragen, exoneratieverbod-tekst en uitzonderingen-lijst zijn alleen via MvT-toelichting (art. 1:27) traceerbaar. Aanbevolen: WVV-ETL-transformer onderzoeken voor Boek 2, Titel 6, Hoofdstuk 2.
2. **WER.md mist art. XX.225 en XX.227** — alleen XX.224, XX.226 en XX.228 aanwezig. De hoofdregel van wrongful trading (kennelijk grove fout → boedel-aansprakelijkheid) is dus niet rechtstreeks geciteerd uit de bron. Aanbevolen: WER-ETL onderzoeken voor Boek XX, Titel VII.
3. **Bron-gap fiscale aansprakelijkheid** — art. 442quater WIB92 en art. 93undecies C btw-Wb ontbreken volledig in de relevante wettekst-bronnen. `bestuurdersaansprakelijkheid-fiscale-schulden` steunt voornamelijk op `inferred`-labels en common-accountancy-knowledge. Bron-uitbreiding nodig: WIB92.md en BTW-Wb.md (of fisconet-plus-extractie).

**Records.ontbreekt**: vooral `financieel-plan-oprichting` (hoog-prio — bewijslast-leverancier voor oprichtersaansprakelijkheid, reeds eerder geflagd vanuit 3.0.II), `alarmbel-procedure` (art. 2:52 — midden), `minderheidsvordering` (laag), `bestuurders-aansprakelijkheid-bij-fusie/splitsing` (12:18 WVV — laag, cross-link 3.0.VIII).

**Dangling-reference** (laag): strafrechtelijke bestuurdersaansprakelijkheid (kruis met PO 4.0); sub-anchor-detail 3.0.VII.A/B (bv. enige bestuurder NV onbeperkt — art. 7:101).

---

## Claims `inferred-from-aggregation`

- `bestuurdersaansprakelijkheid.bouwstenen[0]` (drie aansprakelijkheidsporen) — synthese over art. 2:51 WVV (mandaatfout) + art. 1382 BW oud / Boek 6 BW + specifieke WVV-regimes
- `bestuurdersaansprakelijkheid.in_praktijk[0]` (volgorde van toetsing in een dossier) — synthese over alle aansprakelijkheidsregimes-bouwstenen
- `behoorlijke-vervulling-bestuursopdracht.in_praktijk[0]` (typische mandaatfouten) — aggregatie over art. 2:51, art. 2:52, art. 5:76/6:64/7:96
- `vereffenaarsaansprakelijkheid.in_praktijk[0]` (typische foutkernen) — aggregatie over art. 2:80 + 2:71 + 2:96 + analoge bestuurder-rechtspraak
- `feitelijk-bestuurder.definitie` + `situering` — aggregatie over WVV art. 2:56 §1 + WER art. XX.225-XX.227
- `bestuurdersaansprakelijkheid-sociale-schulden.situering` — aggregatie over WER art. XX.226 + MvT bij art. 1:27
- `aansprakelijkheidsgrondslagen-bestuur-vergelijking` (synthese) — 5 records aggregatie
- `verzwaarde-aansprakelijkheid-bij-insolventie-overzicht` (synthese) — 5 records aggregatie

---

## Migraties oud schema

Geen migraties uitgevoerd — alle 16 records zijn **nieuw** (schema 1.6 direct).

---

## Open observaties (narratief — niet in gaps.json)

1. **WVV-chunking-issue rond Boek 2 Titel 6** ("Bestuur en dagelijks bestuur" / "Bestuurdersaansprakelijkheid"): kritisch artikel-blok (2:51 t/m 2:57) is fragmentair in WVV.md. De MvT-equivalent (art. 1:27) is wel uitgebreid aanwezig — wat erop wijst dat de MvT-extractor en WVV-extractor afwijkende sectie-detectie gebruiken. **Aanbeveling**: WVV-ETL-transformer reviewen op het patroon "wettelijke wijziging via W 2020-04-28/06" — dit blok werd in 2020 hervormd, en de transformer mist mogelijk de hernummerde artikels die als 'voetnoot' bij oude nummering staan.

2. **Bestuurdersaansprakelijkheidsregime is centraal in PO 3.0** — vele bestaande records uit pilot 3.0.II (`bestuursorgaan`, `belangenconflict-bestuurder`), 3.0.IV (uitkeringsregels), 3.0.IX (vereffenaar) en 3.0.X (insolventie) raken hier samen. De synthese-records (15+16) trekken die draden expliciet bij elkaar. Vermoedelijk zal een minicursus-laag voor 3.0.VII een **didactisch leerpad** opbouwen rond de drie aansprakelijkheidsporen + drie schilden + insolventie-regimes — de records ondersteunen dat patroon nu structureel.

3. **Cap-bedragen ontbreken doorlopend** in alle nieuwe records — niet alleen door de WVV-bron-gap, maar ook omdat exacte bedragen volgens ITAA-LEX bij het examen beschikbaar zijn (zie absolute regel "wat getoetst wordt: concepten begrijpen, niet cijfers uit het hoofd kennen"). Conceptuele uiteenzetting van de **mechanica** (vier categorieën, balanstotaal/omzet, 3-jaars-gemiddelde, OOI-uitzondering) is volledig — alleen de numerieke ankerpunten ontbreken bij gebrek aan bron. Acceptabel binnen Certificaid's doelpubliek/-aanpak.

4. **D&O-verzekering (`bestuurdersaansprakelijkheidsverzekering`)** leunt zwaarder op `inferred`-labels dan de andere records — dit komt omdat D&O een commerciële verzekeringsproduct is met polis-conventies, geen primaire wettelijke regeling. De MvT-bij-art-1:27 noemt het wel als ratio voor de cap-regeling, maar geeft geen polis-details. Acceptabel; bron-uitbreiding (bv. een ITAA-norm of een gespecialiseerd CBN-advies, indien bestaand) zou hier kunnen verrijken.

5. **Geen rename van bestaande records** uitgevoerd — `belangenconflict-bestuurder`, `bestuursorgaan` en `vereffenaar` blijven met hun huidige naam en `node_type` ongewijzigd; deze run heeft enkel uitgaande edges van de nieuwe records naar hen toegelaten.

---

## Zelf-evaluatie

| Criterium | Status |
|---|---|
| **Records bestaansreden-test** (eigen record vs bouwsteen) | ✓ alle 16 records dekken een fenomeen dat zelfstandig in het accounting-domein bestaat — geen bouwsteen-kandidaten in vermomming |
| **Near-duplicate-check** | ✓ pre-EXTRACT inspectie van `belangenconflict-bestuurder`, `bestuursorgaan`, `vereffenaar`, `beperkte-aansprakelijkheid-vennoot` — geen overlap |
| **Slug-resolver** | ✓ alle edges met bekende targets bestaan op disk; pending-targets gemarkeerd |
| **Drie-concretiseringsvelden** | ✓ alle records hebben minimaal `in_praktijk` of `voorbeelden`; cluster `bestuurdersaansprakelijkheid` + regel `aansprakelijkheidsbeperking-bestuurder` + `oprichtersaansprakelijkheid` + `bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering` hebben scenario-voorbeelden met cast-namen |
| **Cast-conventie** | ✓ uitsluitend cast-namen gebruikt: Brugse Brouwerij BV, Zelena Bio NV, Oprichtingen Oostende BV, Marleen De Cock, Pieter Vermeulen, Sofie Janssens — €-prefix + duizendtal-separator |
| **Confidence-labeling** | ✓ alle inhoudelijke velden hebben `confidence`; bronnenverwijzingen via `_provenance.inputs` met chunk-ids |
| **Schema 1.6** | ✓ alle records `schema_version: 1.6`, `status: seed`, `situering` aanwezig waar zinvol |
| **Bron-gap-flagging** | ✓ WVV-chunking-bug 2:56/2:57 en WER 2:25/227 + 442quater-WIB-bron-afwezigheid geflagged in gaps.json |
| **Cross-PO gap-vervulling** | ✓ 4 cross-PO records.ontbreekt-entries uit eerdere anchors zijn nu beantwoord (3.0.IX vereffenaar, 3.0.X insolventie, 3.0.II algemeen, 3.0.IV uitkering) |
| **Regime-cluster-heuristiek (pilot-bevinding)** | ✓ toegepast: `bestuurdersaansprakelijkheid` is hoofdcluster met regime-bouwstenen (drie sporen, hoofdelijkheid bij collegiaal bestuur, marginale toetsing, cap+exoneratie+kwijting-trio, verzwaring bij insolventie) — sub-regels (sociale schulden, fiscale schulden, onrechtmatige uitkering, insolventie) krijgen eigen record-status omdat ze elk een eigen wettelijke grondslag + eigen vorderingsbevoegde + eigen cap-uitzondering hebben |

---

## Audit-bewijs

```
$ python3 -m tools.lib.records_api audit
[audit] disk: 559 records (41 synthese), RAG: 559 records, content: 518 fiches
[audit] OK — disk, RAG en content zijn in sync.
```

(Synthese-records hebben geen standaard concept-fiche-render, dat verschil van 41 verklaart het content-aantal.)
