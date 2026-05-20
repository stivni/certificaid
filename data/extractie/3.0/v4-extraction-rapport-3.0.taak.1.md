# EXTRACT v4 — 3.0.taak.1 rapport

**Anchor**: `3.0.taak.1` — "Begeleiding bij de oprichting van een onderneming"
**Run-id**: `concept-extractie-v4-3.0.taak.1-batch1..4-20260520`
**Datum**: 2026-05-20
**Model**: claude-opus-4-7

## Records overzicht

| # | id | node_type | nieuw / update | hoofdcategorie |
|---|---|---|---|---|
| 1 | `financieel-plan-oprichting` | cluster | nieuw | Wettelijk artefact (art. 5:4/6:5/7:3 WVV) |
| 2 | `opstellen-financieel-plan-oprichting` | competentie | nieuw | Accountantsopdracht |
| 3 | `adviseren-vennootschapsvormkeuze` | competentie | nieuw | Adviesopdracht |
| 4 | `begeleiden-inbreng-bij-oprichting` | competentie | nieuw | Procedurele begeleiding |
| 5 | `voorbereiden-oprichtingsakte` | competentie | nieuw | Statuten + verplichte vermeldingen |
| 6 | `begeleiden-registratie-onderneming-kbo` | competentie | nieuw | KBO + btw + UBO + sociaal fonds |
| 7 | `opstellen-openingsbalans-vennootschap` | competentie | nieuw | Eerste boekhouding |
| 8 | `signaleren-oprichtersaansprakelijkheid-risico` | competentie | nieuw | Risicocommunicatie |
| 9 | `oprichtingsproces-stappenplan` | synthese | nieuw | Chronologische orchestratie |

**Totaal**: 9 nieuwe records (1 cluster + 7 competenties + 1 synthese). Geen renames, geen deletes.

## Cross-PO edges (vereist-kennis-van)

Belangrijkste cross-PO links die de competenties leggen:

- → PO 3.0.I begrippen: `vennootschap-begrip`, `vennootschapsvormen-vergelijking`, `besloten-vennootschap-bv`, `naamloze-vennootschap-nv`, `cooperatieve-vennootschap-cv`, `personenvennootschap-met-rechtspersoonlijkheid`, `rechtspersoonlijkheid-vennootschap`, `inbreng-vennootschap`
- → PO 3.0.II: `bestuursmodel-vennootschap`, `bestuursorgaan`, `bevoegdheid-bestuursorgaan`
- → PO 3.0.VI: `aandeelhoudersovereenkomst`
- → PO 3.0.VII: `oprichtersaansprakelijkheid`, `kennelijk-ontoereikend-aanvangsvermogen`, `bestuurdersaansprakelijkheid`
- → PO 1.7: `inbreng-in-natura-verslag`, `quasi-inbreng-verslag`
- → PO 1.1: `boeken-oprichtings-en-kapitaalverhogingskosten`, `oprichtingskosten`

## Gaps aangemaakt (gaps.json)

8 nieuwe entries:

| Aspect | Term | Prio |
|---|---|---|
| `records.ontbreekt` | nijverheidsinbreng (BV/CV-specifiek inbreng-type, art. 5:8/6:11) | midden |
| `records.ontbreekt` | oprichtersverslag (apart van revisoren-inbrengverslag) | midden |
| `records.ontbreekt` | UBO-register (Ultimate Beneficial Owners, KB 30/07/2018) | **hoog** |
| `records.ontbreekt` | Kruispuntbank van Ondernemingen (KBO) + ondernemingsnummer | midden |
| `records.ontbreekt` | Btw-identificatie en 604A-procedure | midden |
| `records.ontbreekt` | Sociaal verzekeringsfonds voor zelfstandige bestuurders | laag |
| `records.ontbreekt` | Drag-along en tag-along clausules | laag |
| `granulariteit.beslissing-nodig` | opstellen-aandeelhoudersovereenkomst als eigen competentie of bouwsteen? | laag |

## Migraties

Geen — alle 9 records zijn nieuw aangemaakt onder schema 1.6. Geen oude types of voorbeeld_inline tegengekomen.

## Claims `inferred-from-aggregation`

Beperkt gebruik. Belangrijkste:

- `adviseren-vennootschapsvormkeuze.situering` — vakdoctrine-aggregatie WVV Boek 4-7 + accountancy-vakpraktijk
- `oprichtingsproces-stappenplan.situering` — synthese over 8 onderliggende competentie-records
- `financieel-plan-oprichting.voorbeelden[0]` (scenario Pieter Vermeulen) — inferred met cast en plausibele cijfers

Alle overige inhoudelijke velden zijn `grounded` met directe verwijzing naar WVV-artikelen (5:4, 5:7, 5:9, 5:11-5:12, 5:16, 6:5, 6:11-6:15, 7:3, 7:7, 7:9, 7:13-7:14, 7:18, 2:7-2:8) of `inferred-from-aggregation` met chunk-ids.

## Open observaties (niet-record-specifiek)

1. **WVV-tweeling-artikelen tussen BV en NV**: art. 5:x in BV-boek heeft systematisch een NV-tegenhanger art. 7:y. Voor competentie-records was het effectief om beide artikelen in de grondslag-verwijzing op te nemen. Voor toekomstige PO 3.0-extracts: dit pattern verdient mogelijk een synthese-record dat de BV-NV-tweelingen mapt (overlapt met `oprichtingsproces-stappenplan.vergelijkingstabel` maar zou een diepere mapping kunnen geven).

2. **UBO-register als cross-PO**: het is technisch een PO 3.0-vereiste (registratie nieuwe vennootschap) maar verbindingsgrond zit in PO 4.0 (antiwitwas). Het record-design voor `ubo-register` moet beslissen waar het hoofdkanaal-anchor zit — best in PO 4.0 met `linked_anchors` ook naar 3.0.taak.1.

3. **Boekhoudkundige integratie met PO 1.1**: `opstellen-openingsbalans-vennootschap` overlapt deels met `boeken-oprichtings-en-kapitaalverhogingskosten` (PO 1.1). De edge is goed gelegd maar bij een latere review-pass moet bekeken worden of de twee records niet inhoudelijk te dicht bij elkaar liggen — competentie (3.0) vs PO-1.1-record dat (lijkt) ook procedure beschrijft.

4. **Aandeelhoudersovereenkomst onder oprichtingsproces**: ik heb bewust géén aparte competentie `opstellen-aandeelhoudersovereenkomst` gemaakt en het ondergebracht in `voorbereiden-oprichtingsakte` stap 4. Granulariteit-gap noteert deze keuze voor latere review.

## Zelf-evaluatie

**Sterke punten**:
- Volledige dekking van de 5 hoofdthema's uit anchor-verbose (vormkeuze, financieel plan, inbreng, oprichtingsformaliteiten, openingsbalans, statuten, risico) zonder herhaling van begrip-records uit 3.0.I-3.0.IX.
- Alle records hebben `vereist-kennis-van`-edges naar bestaande PO 3.0/1.1/1.7-records — geen geïsoleerde competenties.
- Cast consistent (Pieter Vermeulen + Sofie Janssens + Oprichtingen Oostende BV) over alle records, met plausibele cijfers (€ 25.000 cash + € 17.500 bestelwagen).
- BV-NV-tweelingen consistent benoemd in de procedure_grondslag.

**Aandachtspunten**:
- `oprichtingsproces-stappenplan` (synthese) krijgt geen content-fiche-render — bekende beperking voor synthese-type (51 syntheses op 624 records, slechts 573 fiches gerendered). Niet examen-blokkerend, wel render-laag-aandachtspunt.
- 8 gaps in gaps.json — vooral `ubo-register` (hoog) zou bij volgende PO 4.0-pass aangepakt moeten worden.
- Beoordelings_criteria zijn op alle 7 competenties aanwezig maar niet uniform geformatteerd — mogelijke template-conventie voor later.

**Audit-resultaat**: groen (624 records op disk = 624 in RAG; geen orphan-edges geïntroduceerd).
