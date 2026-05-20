# EXTRACT v4 — gap-resolution event PO 3.0 (2026-05-20)

**Run-id**: `concept-extractie-v4-2026-05-20T15:00Z` t/m `…T15:20Z`
**Event-type**: feedback-set uit VERIFY (6 high-priority gaps)
**Scope**: 6 missende records geïdentificeerd door VERIFY-pass + dangling refs
**State vóór**: 666 records, schema 1.6, audit groen
**State na**: 674 records, audit groen (disk = RAG = 674; content = 620)

## Records — 8 nieuw, 0 bijgewerkt, 0 hernoemd, 0 verwijderd

| # | Id | node_type | linked_anchors | Bron-grondslag |
|---|---|---|---|---|
| 1 | `omzetting-vennootschap` | cluster | 3.0.IX, 3.0.taak.3, 1.6.I.A, 1.7.taak.1 | WVV art. 14:1-14:14 (Boek 14, nationale omzetting) |
| 2 | `individueel-controlerecht-aandeelhouder` | regel | 3.0.IV, 3.0.VI | WVV art. 3:101 (BV), art. 7:148 (NV) |
| 3 | `confirmatiebrieven` | begrip | 3.0.IX, 1.6.I.A, 1.7.taak.1 | ISA 505 'External Confirmations' |
| 4 | `inbreng-in-natura` | regel | 3.0.I, 3.0.IX, 1.7.taak.1 | WVV art. 5:7 (BV), 6:8 (CV), 7:7 (NV) |
| 5 | `vereffeningsdeskundige` | begrip | 3.0.X, 3.0.X.D | WER art. XX.85, XX.88, XX.90, XX.92 |
| 6 | `statuten-vennootschap` | cluster | 3.0.I, 3.0.VI, 3.0.IX | WVV art. 5:12, 6:13, 7:13 |
| 7 | `voorstel-omzetting-vennootschap` | regel | 3.0.IX | WVV art. 14:3, 14:5, 14:6 (sub-record van 1) |
| 8 | `controleverslag-omzetting` | regel | 3.0.IX, 3.0.taak.3, 1.6.I.A | WVV art. 14:6, 14:7, 14:10 (sub-record van 1) |

## Gap-resolution-status

| Gap (VERIFY) | Opgelost door | Status |
|---|---|---|
| `omzetting-vennootschap` ontbrekend (61 examen-punten) | cluster + 2 sub-records (voorstel + controleverslag) | resolved |
| `individueel-controlerecht-aandeelhouder` (8 pt, 2013-2-vr20) | regel `individueel-controlerecht-aandeelhouder` | resolved |
| `confirmatiebrieven` (9 pt, 2015-1-vr27) | begrip `confirmatiebrieven` | resolved |
| `inbreng-in-natura` als eigen regel (11 pt, 2003-bibf-vrI2) | regel `inbreng-in-natura` (los van `-verslag`) | resolved |
| `vereffeningsdeskundige` (2 dangling refs) | begrip `vereffeningsdeskundige` als specialisatie van `insolventiefunctionaris` | resolved |
| `statuten-vennootschap` (dangling ref uit SHA + bestaande gap) | cluster `statuten-vennootschap` | resolved |

NB: bestaande gap-entries in `data/extractie/gaps.json` zijn niet gemuteerd (status-updates voorbehouden aan aparte EXTRACT-feedback-event-pass). De resolution wordt gedocumenteerd in dit rapport en zal door de orchestrator achteraf in `gaps.json` gemerged worden.

## Edges — cross-record relaties geschreven

Hoofdcluster `omzetting-vennootschap` linkt expliciet naar:
- `omzetting-vennootschap-opdracht` (bestaand, het verslag-cluster)
- `opstellen-verslag-omzetting-vennootschap` (bestaande competentie)
- `controleverslag-omzetting` + `voorstel-omzetting-vennootschap` (nieuwe sub-records)
- `bijzondere-verslagen-overzicht` (onderdeel-van)
- `fusie-splitsing-controleopdracht` (vergelijkt-met)

`individueel-controlerecht-aandeelhouder`:
- `vraagrecht-aandeelhouder` + `agenderingsrecht-aandeelhouder` (vergelijkt-met — bestaande records)

`confirmatiebrieven`:
- `controlemiddelen-ic`, `opstellen-verslag-omzetting-vennootschap`, `inbreng-in-natura-verslag`, `omzetting-vennootschap`

`inbreng-in-natura`:
- `inbreng-in-natura-verslag` (vereist-kennis-van — bestaand verslag-cluster)
- `inbreng-vennootschap` (onderdeel-van — bestaand parent-begrip)
- `nijverheidsinbreng` (vergelijkt-met — wel/niet in kapitaal)

`vereffeningsdeskundige`:
- `insolventiefunctionaris` (specialisatie-van + vergelijkt-met — bestaand verzamelbegrip)

`statuten-vennootschap`:
- `aandeelhoudersovereenkomst` (vereist-kennis-van + vergelijkt-met — bestaand cluster, lost dangling ref op)
- `quorum-en-meerderheid-statutenwijziging` (verwijst-naar — bestaand)

Sub-records `voorstel-omzetting-vennootschap` en `controleverslag-omzetting`:
- `onderdeel-van: omzetting-vennootschap`
- `controleverslag-omzetting` ook `onderdeel-van: omzetting-vennootschap-opdracht`

## Audit

```
[audit] disk: 674 records (54 synthese), RAG: 674 records, content: 620 fiches
[audit] OK — disk, RAG en content zijn in sync.
```

Geen ghosts, geen missing, geen content-drift binnen records-API scope.

## Schema-naleving

- Alle 8 records dragen `schema_version: "1.6"` (verplicht).
- Alle 8 hebben `status: "seed"` (anti-hallucinatie §6).
- Top-level `_provenance` met `extractor_run`, `model: claude-opus-4-7`, `anchor_id`, `linked_anchors`, `reviewed_by: null`.
- Edges gebruiken uitsluitend de zeven canonieke types (`vereist-kennis-van`, `onderdeel-van`, `vergelijkt-met`, `specialisatie-van`, `uitzondering-op`, `verwijst-naar`); één typo (`vergelijkt-with`) gevangen vóór save.

## Migraties

Geen — alle 8 zijn nieuwe records, geen pre-1.6-schema, geen `voorbeeld_inline`, geen `doel`-veld, geen gedeprecieerde edge-types.

## Claims `inferred-from-aggregation`

- `omzetting-vennootschap.situering` (combinatie WVV Boek 14 + ITAA-context)
- `inbreng-in-natura.situering` (combinatie WVV regimes BV/CV/NV)
- Diverse in_praktijk- en voorbeeld-entries gemarkeerd `inferred` waar zij stagiair-context toevoegen buiten de directe wettekst.

Alle wettelijke regels en voorwaarden zijn `grounded` met WVV/WER chunk-ids in `_provenance.inputs`.

## Open observaties

- **`omzetting-vennootschap-opdracht`** en het nieuwe **`omzetting-vennootschap`**: licht overlappende scope (verslag-procedure vs. procedure-totaal). De edge `vereist-kennis-van` van het nieuwe naar het bestaande dekt dit; bij een latere consolidatie-pas kan men overwegen het oude cluster te hernoemen naar `omzettingsverslag` (om verwarring weg te nemen). Niet gedaan in deze pass — out of scope.
- **`controleverslag-omzetting`** heeft `onderdeel-van` naar zowel `omzetting-vennootschap` als `omzetting-vennootschap-opdracht`. Beide juist: het controleverslag is een procedure-bouwsteen van de omzetting als geheel en het hoofd-artefact van het verslag-cluster.
- **Grensoverschrijdende omzetting** (WVV art. 14:15-14:42) zit nu als bouwsteen in `omzetting-vennootschap`. Wanneer 3.0 een specifieke `grensoverschrijdende-omzetting`-gap heeft kan dat later als specialisatie-cluster met `specialisatie-van: omzetting-vennootschap`-edge worden uitgewerkt.
- **Vereffenaar (WVV)** versus **vereffeningsdeskundige (WER)**: woordelijk gelijkend, juridisch verschillend. Valkuil expliciet toegevoegd. Eventueel ontbreekt het record `vereffenaar-vennootschap` nog — buiten scope van deze run, te verifiëren bij volgende VERIFY-pass.

## Beperkingen / vervolgwerk

- Bestaande gap-entries niet gemuteerd (per prompt-protocol). Orchestrator moet status-update doen voor de 6 opgeloste gaps.
- Geen schema-validatie tegen examenvragen uitgevoerd (out of scope EXTRACT — fase 5 examen-vragen-coupling).
- Sub-records voor grensoverschrijdende omzetting niet aangemaakt — zou aparte specialisatie-cluster vereisen.
