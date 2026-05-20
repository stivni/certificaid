# EXTRACT v4 — PO 3.0, wave 2, anchor 3.0.V, helft 1 (sub-anchors A+B+C+D)

**Run-id**: concept-extractie-v4-2026-05-20 (wave 2 — gap-fill na wave 1)
**Scope**: sub-anchors `3.0.V.A` (do's & don'ts SPA-drafting), `3.0.V.B` (asset deal vs share deal — garanties koper), `3.0.V.C` (juridische draagwijdte intentieverklaring), `3.0.V.D` (voor-/nadelen due diligence)
**Vooraf**: wave 1 leverde 13 records op het parent-anker `3.0.V`. Deze pass is gap-fill-modus: minimale toevoegingen + linked_anchors verfijning.

## Records — overzicht

| Status | ID | Type | Toelichting |
|---|---|---|---|
| **Nieuw** | `precontractuele-aansprakelijkheid-overname` | begrip | Culpa in contrahendo, diligentieplicht, informatieplicht (BW boek 5 art. 5.16); raakt V.C én V.D |
| Update | `due-diligence-overname` | cluster | +bouwsteen "Voor- en nadelen"; +linked_anchors V.A/V.D; +edge naar precontract |
| Update | `letter-of-intent-overname` | begrip | +linked_anchors V.C; +edge naar precontract |
| Update | `overnameovereenkomst` | cluster | +linked_anchors V.A |
| Update | `representations-and-warranties` | cluster | +linked_anchors V.A/V.B |
| Update | `indemnification-overname` | cluster | +linked_anchors V.A/V.B |
| Update | `purchase-price-mechanismen` | synthese | +linked_anchors V.A |
| Update | `escrow-en-zekerheidsmechanismen-overname` | cluster | +linked_anchors V.A |
| Update | `closing-condities-precedent` | cluster | +linked_anchors V.A |
| Update | `material-adverse-change-clausule` | begrip | +linked_anchors V.A |
| Update | `non-compete-overname` | regel | +linked_anchors V.A |
| Update | `confidentiality-overname` | begrip | +linked_anchors V.A/V.C |
| Update | `asset-deal-versus-share-deal` | synthese | +linked_anchors V.B |
| Update | `transfer-bedrijfstak-algemeenheid` | cluster | +linked_anchors V.B |

**Totaal**: 1 nieuw record, 13 updates (waarvan 2 met inhoudelijke verrijking: bouwsteen + edge).

## Aantal gaps aangemaakt

Geen — wave-1 records dekken de inhoud van V.A-V.D volledig na de nieuwe bouwsteen en het nieuwe begrip. De ruis in de bundles (IFRS-, ISA-, IESBA-chunks) is irrelevant voor SPA-drafting/M&A-praktijk en hoeft niet geadresseerd te worden.

## Migraties

- Geen schema-1.4 → 1.5 hernoemingen (alle wave-1 records waren al v1.5).
- Geen `voorbeeld_inline` → `voorbeelden[]` (records waren al up-to-date).

## Claims `inferred-from-aggregation`

- `due-diligence-overname` § bouwsteen "Voor- en nadelen" — synthese over IBA §3.1.1, §4.1, §4.2 (drie chunks uit één bron). De voor-/nadelen-uitsplitsing per partij combineert algemene DD-best-practice (IBA §3.1.1 — vendor DD) met de Belgische diligentieplicht (§4.1) en de impact-op-transactieparameters (§4.2). `confidence: inferred-from-aggregation`.

## Open observaties (narratief, niet record-specifiek)

1. **Bundle-ruis V.A/V.B**: ~50–60 % van de top-150 chunks zijn IFRS-/ISA-fragmenten (geconsolideerde IFRS, ISA 600/315/500/300/210/800, IESBA). Voor M&A-SPA-drafting niet relevant. Suggestie voor `tools.extractie.export_bundle` of de alarmbel: een eerstegraads-filter op bron-categorie (M&A-juridisch vs jaarrekening-audit) zou de scope verkleinen voor SPA-anchors. Niet als gap geregistreerd — dit is corpus-engineering, niet een content-tekort.

2. **Onderlinge dichtheid V.E-G niet aangeraakt**: schadeloosstelling + concurrentie + closing-procedures komen in de volgende batch (helft 2). De nu toegevoegde `precontractuele-aansprakelijkheid-overname` raakt V.C inhoudelijk; mogelijk komt zij ook indirect voor in V.E (schadeloosstelling vóór closing) — dat ankert dan automatisch via linked_anchors-update bij die batch.

3. **Sterke wave-1-positie bevestigd**: de hypothese in de scope-declaratie ("vermoedelijk al gedekt door wave-1 cluster") klopt; één nieuw record + bouwsteen-verrijking volstaat. Dit valideert de wave-planning-heuristiek voor gerelateerde sub-anchors.

## Audit-check

```
records-API audit_parity():
  ok: True
  disk_ids: 652 (+1 vs 651 bij start)
  rag_ids: 652 (parity)
  ghosts: 0
  missing: 0
  content_ontbreekt: 0
  content_extra: 0
```

State na helft 1: 652 records, audit groen.
