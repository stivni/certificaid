# EXTRACT v4 — PO 3.0.X wave 2, helft 1 (sub-anchors A + B + C)

**Run-ID**: `concept-extractie-v4-2026-05-20T13:30:00Z`
**Model**: claude-opus-4-7
**Scope**: 3.0.X.A (Werking rechtbanken / Regsol / insolventiefunctionaris), 3.0.X.B (Opsporing ondernemingen in moeilijkheden / kamers handelsonderzoek), 3.0.X.C (Ondernemingsbemiddelaar).
**Stand vóór run**: 658 records, audit groen.
**Stand na run**: 661 records, audit groen (`ok: True`, ghosts: 0, missing: 0).

## Records

### Nieuw (3)

| ID | node_type | sub-anchor | Korte definitie |
|---|---|---|---|
| `regsol-platform` | begrip | 3.0.X.A | Het centrale digitale insolventieregister — Boek XX noemt het generiek "het register" (XX.15), operationeel "Regsol". Authentieke bron voor alle akten in een insolventiedossier. |
| `insolventiefunctionaris` | begrip | 3.0.X.A | Overkoepelend begrip voor curator, gerechtelijk bewindvoerder, vereffeningsdeskundige en herstructureringsdeskundige. Boek XX gebruikt sinds 2023 ook "gerechtsmandataris" als verzamelterm. |
| `ondernemingsrechtbank-bevoegdheid-insolventie` | regel | 3.0.X.A | COMI-test (art. XX.12) + uitbreidingen voor verbonden ondernemingen (XX.13) en onbeperkt aansprakelijke vennoten (XX.14). Driemaanden-vermoeden bij zetelverplaatsing. |

### Bijgewerkt (9)

| ID | Wijziging |
|---|---|
| `kamer-ondernemingen-in-moeilijkheden` | linked_anchors += `3.0.X`, `3.0.X.B`; 4 edges toegevoegd (was 0): onderdeel-van insolventieprocedures-belgie, vereist-kennis-van + getriggerd-door vroegtijdige-waarschuwing-insolventie, verwijst-naar meldingsplicht-accountant-continuiteit. |
| `vroegtijdige-waarschuwing-insolventie` | linked_anchors += `3.0.X.A`, `3.0.X.B`; edges naar `regsol-platform` en `ondernemingsrechtbank-bevoegdheid-insolventie`. |
| `curator-faillissement` | linked_anchors += `3.0.X.A`; edge `specialisatie-van: insolventiefunctionaris`. |
| `rechter-commissaris-insolventie` | linked_anchors += `3.0.X.A`; edge `vergelijkt-met: insolventiefunctionaris` (magistraat vs. mandataris). |
| `insolventieprocedures-belgie` | linked_anchors += `3.0.X.A`, `3.0.X.B`; 3 verwijst-naar edges toegevoegd. |
| `meldingsplicht-accountant-continuiteit` | linked_anchors += `3.0.X.B`; edge naar kamer-ondernemingen-in-moeilijkheden. |
| `besloten-voorbereiding-faillissement` | linked_anchors += `3.0.X.A`; edges naar insolventiefunctionaris en regsol-platform. |
| `faillissement` | linked_anchors += `3.0.X.A`; 3 verwijst-naar edges. |
| `gerechtelijke-reorganisatie` | linked_anchors += `3.0.X.A`; 2 verwijst-naar edges. |

### Hernoemd / Verwijderd

Geen.

## Gaps (5 nieuw)

| Aspect | Prio | Reden (samengevat) |
|---|---|---|
| bron-gap | midden | Sub-anchor 3.0.X.C "Ondernemingsbemiddelaar" — figuur uit WER Titel II Afdeling 3 — is **opgeheven** sinds 2023-09-01 (W 2023-06-07/07 art. 44). Bundle pulled enkel minnelijke-schuldbemiddelaar (Boek XIX) en fiscale intermediair-definities. Geen record onder oude naam gecreëerd. Anchor-tekst-herziening voorgesteld. |
| records.ontbreekt | midden | `herstructureringsdeskundige` (XX.30-XX.35) — gerechtsmandataris bij dreigende onbestuurbaarheid, conservatoire functie buiten lopende GRO. Specialisatie van insolventiefunctionaris. |
| records.ontbreekt | midden | `gerechtelijk-bewindvoerder` (XX.32) — bij beheersontneming. |
| records.ontbreekt | midden | `vereffeningsdeskundige` (XX.85, XX.94) — bij overdracht onder gerechtelijk gezag. Aparte verwarringsmagneet naast curator en vereffenaar. |
| records.ontbreekt | laag | `centraal-register-economische-knipperlichten` (XX.21 § 2) — apart van Regsol, FOD Justitie als verwerkingsverantwoordelijke. Voorlopig ingebed onder vroegtijdige-waarschuwing-insolventie, valkuil in `regsol-platform`. |

## Schema-migraties

Geen — alle 9 bijgewerkte records waren al schema 1.6.

## inferred-from-aggregation claims

- `regsol-platform.situering` — combinatie XX.15-XX.19, beheerstructuur niet expliciet één-op-één in chunks.
- `insolventiefunctionaris.situering` — historiek terminologie 2017 → 2023 over meerdere wetswijzigingen.
- `ondernemingsrechtbank-bevoegdheid-insolventie.situering` — relatie met EU 2015/848 Insolventieverordening (achtergrond, niet letterlijk in bundle).

## Open observaties

1. **Bundle 3.0.X.C retrieval-probleem**. De anchor-synonyms in `anchors.json` voor 3.0.X.C zijn waarschijnlijk te breed of mismatched: retrieval pulled "minnelijke schuldbemiddelaar" (Boek XIX) als top-hits in plaats van Boek XX-context. Aangezien Boek XX Titel II Afdeling 3 leeg is sinds 2023, is dit ook een legitieme bron-gap — niet enkel een retrieval-fout.
2. **"Het register" vs "Regsol" terminologie**. Boek XX gebruikt zelf nergens de naam "Regsol" — alleen "het register". De koppeling Regsol-as-implementation-name is praktijk-kennis (KB die de beheerder aanwijst). Goed gedocumenteerd in `regsol-platform.situering` met inferred-from-aggregation-label.
3. **"Insolventiefunctionaris" als wettelijke term**. XX.13 spreekt nog van "gemeenschappelijke insolventiefunctionaris" terwijl de rest van het wetboek doorgaans "gerechtsmandataris" gebruikt. Dit is een gevolg van de hervorming W 2023-06-07/07 die niet overal volledig is doorgetrokken. De stagiair krijgt beide termen voorgeschoteld; record dekt beide expliciet.
4. **Wave 2 helft 2 voorbereiding**. Gaps voor `herstructureringsdeskundige`, `gerechtelijk-bewindvoerder` en `vereffeningsdeskundige` zijn natuurlijke kandidaten voor helft 2 (sub-anchors D-F). Volgorde-suggestie: eerst herstructureringsdeskundige (raakt voorlopige maatregelen), dan vereffeningsdeskundige (raakt overdracht onder gerechtelijk gezag), dan gerechtelijk-bewindvoerder.

## Audit-check

```
disk_ids: 661 (was 658)
rag_ids:  661
ok:       True
ghosts:   0
missing:  0
content_ontbreekt: 0
content_extra:     0
```

Atomiciteitscontract gerespecteerd voor alle 12 save_record-calls (3 nieuw + 9 update).
