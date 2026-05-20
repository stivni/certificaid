# EXTRACT v4 — PO 3.0.X wave 2, helft 2 (D + E + F)

**Datum**: 2026-05-20
**Run**: concept-extractie-v4 (Opus subagent)
**Scope**: Sub-anchors 3.0.X.D (Gerechtelijke reorganisatie, procedure — 85 chunks), 3.0.X.E (Faillissement, voorwaarden en procedure — 56 chunks), 3.0.X.F (Rehabilitatie en verbodsbepalingen — 163 chunks)
**State voor**: 661 records, audit groen
**State na**: 666 records, audit groen (disk=rag=666, 0 ghosts, 0 missing)

## Nieuwe records (5)

| ID | node_type | Anchor | Sleutel-bron |
|---|---|---|---|
| `herstructureringsdeskundige` | autoriteit | 3.0.X.D | WER art. XX.30, XX.83/22 |
| `homologatie-collectief-akkoord` | regel | 3.0.X.D | WER art. XX.79, XX.83/17, XX.83/38 |
| `overdracht-onder-gerechtelijk-gezag` | cluster | 3.0.X.D | WER art. XX.84-XX.91 (titel V/II) |
| `beroepsverbod-na-insolventie` | regel | 3.0.X.F | WER art. XX.229-XX.232 |
| `rehabilitatie-gefailleerde` | regel | 3.0.X.F | WER art. XX.237-XX.241 |

### Beslissingen per record

- **herstructureringsdeskundige** als `autoriteit`: rechterlijk mandataris, sinds 2023 (omzetting Richtlijn (EU) 2019/1023). Onderscheidt zich functioneel van curator/gerechtelijk-bewindvoerder (geen bestuursvervanging). Edge `onderdeel-van: insolventiefunctionaris` + `onderdeel-van: gerechtelijke-reorganisatie` + `vergelijkt-met: curator-faillissement`.
- **homologatie-collectief-akkoord** als `regel`: hoofdregel + voorwaarden + uitzonderingen (art. XX.72-XX.73-XX.83/17). KMO-regime versus grote-ondernemingen-regime met cross-class cram-down beide gedekt. Best-interests-of-creditors-test en absolute-voorrangsregel expliciet.
- **overdracht-onder-gerechtelijk-gezag** als `cluster`: aparte titel V/II (sinds 2023 niet meer onder gerechtelijke reorganisatie). 5 bouwstenen + 2 vergelijkingsparen (met gerechtelijke-reorganisatie en met faillissement). Pending edge naar `vereffeningsdeskundige` (gap blijft open).
- **beroepsverbod-na-insolventie** als `regel`: voorwaarden art. XX.229 §1 (kennelijke grove fout) en §2 (verzuim boekhoudverplichtingen art. XX.146). Onderscheid burgerlijk (WER) versus strafrechtelijk (Strafwetboek art. 48, 57) expliciet. Niet automatisch — getriggerd door vordering OM/curator/schuldeiser.
- **rehabilitatie-gefailleerde** als `regel`: voorwaarde art. XX.237 (alle bedragen volledig betaald) + procedure XX.238-XX.240. Modus-explicatie: rehabilitatie als historisch instrument, sinds 2018-kwijtschelding-regime grotendeels achterhaald maar relevant voor gefailleerden zonder kwijtschelding. Onderscheid kwijtschelding (schulden geschrapt) versus rehabilitatie (alles betaald) als kerncontrast.

## Updates (6)

- `kwijtschelding-natuurlijke-persoon-gefailleerde`: + `linked_anchors: 3.0.X.F`, + edge `vergelijkt-met: rehabilitatie-gefailleerde`
- `insolventiefunctionaris`: + `linked_anchors: 3.0.X.D`, + edges naar `herstructureringsdeskundige` + `vereffeningsdeskundige (pending)`
- `gerechtelijke-reorganisatie`: + `linked_anchors: 3.0.X.D`, + edges naar `homologatie-collectief-akkoord`, `herstructureringsdeskundige`, `overdracht-onder-gerechtelijk-gezag`
- `faillissement`: + `linked_anchors: 3.0.X.E, 3.0.X.F`, + edges naar `beroepsverbod-na-insolventie`, `rehabilitatie-gefailleerde`
- `insolventieprocedures-belgie`: + edge `vereist-kennis-van: overdracht-onder-gerechtelijk-gezag`
- `curator-faillissement`: + `linked_anchors: 3.0.X.E`

## Gaps aangemaakt (5)

| Aspect | Concept | Prio |
|---|---|---|
| `records.ontbreekt` | `gerechtelijk-bewindvoerder` (WER art. XX.31) | midden |
| `records.ontbreekt` | `reorganisatieplan` (WER art. XX.67-XX.83) | midden |
| `records.ontbreekt` | `minnelijk-akkoord-buitengerechtelijk` (WER art. XX.64) | midden |
| `dangling-reference` | strafrechtelijk eerherstel (Sv. art. 621-634) — bewust-uit-scope | laag |
| `dangling-reference` | art. 442bis WIB92 / 93undecies BTW (fiscale-overdracht) — bewust-uit-scope, PO 2.x | laag |

**Niet opnieuw geflagd** (al in gaps): `herstructureringsdeskundige` (nu gemaakt), `vereffeningsdeskundige` (blijft open), `overdracht onder gerechtelijk gezag` (nu gemaakt).

## Migraties

Geen oud-type-migraties of voorbeeld_inline-conversies vereist — alle bestaande records waren reeds schema 1.5/1.6.

## Claims `inferred-from-aggregation`

- `herstructureringsdeskundige.situering`: aggregatie van WER art. XX.30 + XX.83/22 + Richtlijn 2019/1023-context
- `homologatie-collectief-akkoord.situering`: aggregatie KMO-regime (art. XX.78-XX.79) + grote-ondernemingen-regime (art. XX.83/17)
- `homologatie-collectief-akkoord.in_praktijk[2]`: cross-bron-synthese WER + CBN-advies 2018/18
- `overdracht-onder-gerechtelijk-gezag.situering`: aggregatie pre-2023-WCO + post-2023-titel-V/II
- `beroepsverbod-na-insolventie.situering`: aggregatie WER art. XX.229 + parallel-regime strafrecht (Sw art. 48, 57)
- `rehabilitatie-gefailleerde.situering` + `effect-clausule`: aggregatie WER art. XX.237 + XX.229 + kwijtschelding-regime art. XX.173

## Open observaties

- **Rehabilitatie versus kwijtschelding**: dit paar verwarring-risico is in beide records expliciet behandeld via `vergelijkt-met`-edge en valkuilen-blok. Render-laag zal "Niet verwarren met" prominent tonen.
- **3.0.X.F bundle had veel ruis**: 163 chunks, maar slechts ~8 echt-relevante chunks rond verbodsbepalingen en rehabilitatie (XX.229-XX.241). Veel chunks gingen over strafrecht-beroepsverbod, oud BW (beschermde personen) en WIB92 — bewust niet meegenomen.
- **Vereffeningsdeskundige blijft pending**: pending edge in `overdracht-onder-gerechtelijk-gezag` en `insolventiefunctionaris`. Een wave-3-batch (mocht die er komen) zou samen met `gerechtelijk-bewindvoerder` en `minnelijk-akkoord-buitengerechtelijk` de WER-insolventie-actorruimte kunnen voltooien.

## Sanity check

```
audit_parity: disk=666, rag=666, ghosts=0, missing=0  ✓
```

PO 3.0.X wave 2 is hiermee afgesloten. Wave 2-batch totaal (helft 1 + helft 2): wave-1 17 records → wave-2 +6 records → 23 records voor 3.0.X.
