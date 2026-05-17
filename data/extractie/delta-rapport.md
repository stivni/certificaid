# Delta-rapport — bron-refresh-impact

_Gegenereerd op 2026-05-17T13:30:57.522035+00:00._
_Vergelijking: `run-20260515T060527Z.json` → `run-20260517T100230Z.json`_

## Samenvatting

- **Records met delta**: 344 (van 344)
  - HIGH (bron-gap of inferred + primaire delta): **251**
  - MEDIUM (primaire delta, grounded record): 93
  - LOW (alleen secundaire delta): 0
- **Anchors met orphan-chunks** (mogelijk nieuwe fenomenen): 428

## Per programmaonderdeel

| PO | Records HIGH | MEDIUM | LOW | Orphan primaire-chunks |
|---|---|---|---|---|
| 1.1 | 29 | 13 | 0 | 5965 |
| 1.2 | 44 | 0 | 0 | 2105 |
| 1.3 | 30 | 0 | 0 | 5108 |
| 1.4 | 32 | 0 | 0 | 1439 |
| 1.5 | 4 | 23 | 0 | 3728 |
| 1.6 | 16 | 43 | 0 | 6154 |
| 1.7 | 39 | 14 | 0 | 13454 |
| 1.8 | 44 | 0 | 0 | 5539 |
| 1.9 | 13 | 0 | 0 | 7236 |
| 2.1 | 0 | 0 | 0 | 1645 |
| 2.2 | 0 | 0 | 0 | 1467 |
| 2.3 | 0 | 0 | 0 | 2353 |
| 2.4 | 0 | 0 | 0 | 1155 |
| 2.5 | 0 | 0 | 0 | 1658 |
| 2.6 | 0 | 0 | 0 | 1555 |
| 2.7 | 0 | 0 | 0 | 436 |
| 2.8 | 0 | 0 | 0 | 2711 |
| 3.0 | 0 | 0 | 0 | 4024 |
| 4.0 | 0 | 0 | 0 | 4936 |

## Top HIGH-prio records (bron-upgrade-kandidaten)

Records met een expliciete `bron_gap` of `inferred-common-knowledge`-claim, waar nu primaire bronnen beschikbaar zijn.

| Record | PO | echte-delta | Top bronnen (chunks) |
|---|---|---|---|
| `solvabiliteitsratio.json` | 1.3 | 1499 | IFRS-9-financiele-instrumenten (215), IFRS-7-financiele-instrumenten (84), IFRS-17-verzekeringscontracten (81) |
| `horizontale-analyse-jaarrekening.json` | 1.3 | 1478 | IFRS-9-financiele-instrumenten (176), IFRS-7-financiele-instrumenten (90), IFRS-17-verzekeringscontracten (70) |
| `debt-equity-ratio.json` | 1.3 | 1463 | IFRS-9-financiele-instrumenten (214), IFRS-7-financiele-instrumenten (84), IFRS-17-verzekeringscontracten (81) |
| `verticale-analyse-jaarrekening.json` | 1.3 | 1421 | IFRS-9-financiele-instrumenten (169), IFRS-7-financiele-instrumenten (89), IFRS-17-verzekeringscontracten (66) |
| `liquiditeitsratio.json` | 1.3 | 1352 | IFRS-9-financiele-instrumenten (167), IFRS-7-financiele-instrumenten (85), IFRS-17-verzekeringscontracten (77) |
| `analytische-balans.json` | 1.3 | 1347 | IFRS-9-financiele-instrumenten (139), IFRS-7-financiele-instrumenten (85), IFRS-17-verzekeringscontracten (64) |
| `rentabiliteit-eigen-vermogen-roe.json` | 1.3 | 1300 | IFRS-9-financiele-instrumenten (161), IFRS-7-financiele-instrumenten (82), IFRS-17-verzekeringscontracten (64) |
| `rentabiliteit-totaal-activa-roa.json` | 1.3 | 1300 | IFRS-9-financiele-instrumenten (161), IFRS-7-financiele-instrumenten (82), IFRS-17-verzekeringscontracten (64) |
| `cashflow-analyse.json` | 1.3 | 1299 | IFRS-9-financiele-instrumenten (171), IFRS-7-financiele-instrumenten (84), IFRS-17-verzekeringscontracten (74) |
| `current-ratio.json` | 1.3 | 1269 | IFRS-9-financiele-instrumenten (161), IFRS-7-financiele-instrumenten (83), IFRS-17-verzekeringscontracten (66) |
| `doelstellingen-financiele-analyse.json` | 1.3 | 1181 | IFRS-9-financiele-instrumenten (94), IFRS-7-financiele-instrumenten (74), IFRS-17-verzekeringscontracten (61) |
| `behoefte-aan-bedrijfskapitaal.json` | 1.9 | 1166 | IFRS-9-financiele-instrumenten (120), IFRS-17-verzekeringscontracten (73), IFRS-7-financiele-instrumenten (71) |
| `toegevoegde-waarde-financiele-analyse.json` | 1.9 | 1160 | IFRS-9-financiele-instrumenten (96), IFRS-7-financiele-instrumenten (67), IFRS-17-verzekeringscontracten (63) |
| `wijziging-boekhoudkundig-referentiestelsel.json` | 1.5 | 1160 | IFRS-9-financiele-instrumenten (105), IFRS-7-financiele-instrumenten (82), IFRS-17-verzekeringscontracten (62) |
| `sectorvergelijking-financiele-analyse.json` | 1.3 | 1156 | IFRS-9-financiele-instrumenten (165), IFRS-7-financiele-instrumenten (72), IFRS-17-verzekeringscontracten (58) |
| `historische-evolutie-financiele-analyse.json` | 1.3 | 1154 | IFRS-9-financiele-instrumenten (166), IFRS-7-financiele-instrumenten (73), IFRS-17-verzekeringscontracten (58) |
| `interpretatie-financiele-ratios.json` | 1.9 | 1151 | IFRS-9-financiele-instrumenten (102), IFRS-7-financiele-instrumenten (73), IFRS-17-verzekeringscontracten (73) |
| `cijferanalyses-controle-norm.json` | 1.3 | 1135 | IFRS-9-financiele-instrumenten (164), IFRS-7-financiele-instrumenten (71), ISA-315-herzien-2019 (55) |
| `ratio-covenants.json` | 1.3 | 1122 | IFRS-9-financiele-instrumenten (157), IFRS-7-financiele-instrumenten (71), ISA-315-herzien-2019 (55) |
| `jaarrekening-als-studieobject.json` | 1.2 | 1099 | IFRS-9-financiele-instrumenten (92), IFRS-7-financiele-instrumenten (73), IFRS-17-verzekeringscontracten (61) |
| `kasstroomoverzicht-drie-segmenten.json` | 1.9 | 1099 | IFRS-9-financiele-instrumenten (100), IFRS-17-verzekeringscontracten (70), IFRS-7-financiele-instrumenten (69) |
| `liquiditeitstoets-beslisboom.json` | 1.3 | 1075 | IFRS-9-financiele-instrumenten (160), IFRS-7-financiele-instrumenten (71), IFRS-17-verzekeringscontracten (55) |
| `ratio-vier-doelen-vergelijking.json` | 1.3 | 1062 | IFRS-9-financiele-instrumenten (158), IFRS-7-financiele-instrumenten (70), IFRS-17-verzekeringscontracten (53) |
| `getrouw-beeld-jaarrekening.json` | 1.2 | 992 | IFRS-9-financiele-instrumenten (89), IFRS-7-financiele-instrumenten (59), IFRS-17-verzekeringscontracten (44) |
| `resultaat-categorisatie-beslisboom.json` | 1.1 | 959 | IFRS-9-financiele-instrumenten (102), IFRS-7-financiele-instrumenten (54), ISA-315-herzien-2019 (30) |
| `werkkapitaal.json` | 1.3 | 958 | IFRS-9-financiele-instrumenten (165), IFRS-7-financiele-instrumenten (68), ISA-315-herzien-2019 (43) |
| `boekjaar-eindprocedure-checklist.json` | 1.1 | 941 | IFRS-9-financiele-instrumenten (68), IFRS-7-financiele-instrumenten (48), ISA-315-herzien-2019 (46) |
| `analytische-boekhouding.json` | 1.8 | 905 | IFRS-9-financiele-instrumenten (66), ISA-315-herzien-2019 (55), IFRS-7-financiele-instrumenten (44) |
| `intake-financiele-analyse.json` | 1.3 | 903 | IFRS-9-financiele-instrumenten (83), IFRS-7-financiele-instrumenten (56), ISA-315-herzien-2019 (39) |
| `quick-ratio.json` | 1.3 | 898 | IFRS-9-financiele-instrumenten (151), IFRS-7-financiele-instrumenten (67), ISA-315-herzien-2019 (43) |

_… +221 meer HIGH-records (zie JSON-rapport)._

## Top anchors met orphan-chunks (DISCOVER-kandidaten)

Anchors waar nieuwe primaire-bron-chunks beschikbaar zijn die nog géén record raken — mogelijk nieuwe fenomenen.

| Anchor | PO | orphan-count | Top bronnen (chunks) |
|---|---|---|---|
| 4.0.II.A | 4.0 | 1145 | IFRS-7-financiele-instrumenten (91), IFRS-9-financiele-instrumenten (84), IFRS-17-verzekeringscontracten (60) |
| 1.9.taak.1 | 1.9 | 1041 | IFRS-9-financiele-instrumenten (86), IFRS-7-financiele-instrumenten (67), IFRS-17-verzekeringscontracten (60) |
| 1.5.IV.C | 1.5 | 901 | IFRS-9-financiele-instrumenten (81), IFRS-7-financiele-instrumenten (68), IFRS-17-verzekeringscontracten (53) |
| 1.1.II.D | 1.1 | 838 | IFRS-9-financiele-instrumenten (154), IFRS-7-financiele-instrumenten (65), IFRS-17-verzekeringscontracten (60) |
| 1.9.V.C | 1.9 | 795 | IFRS-9-financiele-instrumenten (158), IFRS-7-financiele-instrumenten (41), IFRS-17-verzekeringscontracten (38) |
| 1.3.I.C | 1.3 | 782 | IFRS-7-financiele-instrumenten (54), ISA-315-herzien-2019 (39), IFRS-9-financiele-instrumenten (39) |
| 1.3.II.C | 1.3 | 737 | IFRS-9-financiele-instrumenten (149), IFRS-7-financiele-instrumenten (59), ISA-315-herzien-2019 (41) |
| 1.3.II.A | 1.3 | 688 | IFRS-9-financiele-instrumenten (61), IFRS-7-financiele-instrumenten (32), ISA-315-herzien-2019 (32) |
| 1.6.II.A | 1.6 | 685 | ISA-315-herzien-2019 (58), ISA-600 (29), IFRS-9-financiele-instrumenten (28) |
| 2.8.taak.4 | 2.8 | 676 | IFRS-7-financiele-instrumenten (37), ISA-315-herzien-2019 (32), ISA-600 (25) |
| 1.8.I.A | 1.8 | 670 | ISA-315-herzien-2019 (55), IFRS-7-financiele-instrumenten (39), IFRS-9-financiele-instrumenten (36) |
| 1.3.I | 1.3 | 645 | IFRS-9-financiele-instrumenten (41), ISA-315-herzien-2019 (38), ISA-540-herzien (32) |
| 1.9.VII.C | 1.9 | 641 | IFRS-9-financiele-instrumenten (55), ISA-315-herzien-2019 (51), ISA-540-herzien (35) |
| 1.6.IV.C | 1.6 | 637 | ISA-315-herzien-2019 (32), ISA-600 (30), ISA-700-herzien (30) |
| 1.8.taak.1 | 1.8 | 637 | ISA-315-herzien-2019 (54), IFRS-9-financiele-instrumenten (47), IFRS-17-verzekeringscontracten (29) |
| 1.1.II.S | 1.1 | 605 | IFRS-7-financiele-instrumenten (32), ISA-315-herzien-2019 (29), ISA-600 (23) |
| 1.7.taak.1 | 1.7 | 601 | ISA-315-herzien-2019 (56), ISA-540-herzien (30), ISA-600 (28) |
| 1.7.XI | 1.7 | 599 | ISA-315-herzien-2019 (51), ISA-540-herzien (41), ISA-220-herzien (26) |
| 1.9.V.E | 1.9 | 585 | IFRS-9-financiele-instrumenten (63), IFRS-7-financiele-instrumenten (40), IFRS-17-verzekeringscontracten (36) |
| 1.6.II.C | 1.6 | 566 | ISA-315-herzien-2019 (52), ISA-540-herzien (35), ISA-600 (28) |
| 1.1.II.C | 1.1 | 559 | IFRS-9-financiele-instrumenten (110), IFRS-7-financiele-instrumenten (45), IFRS-3-bedrijfscombinaties (33) |
| 4.0.II.E | 4.0 | 557 | IFRS-9-financiele-instrumenten (50), ISA-315-herzien-2019 (45), ISA-700-herzien (26) |
| 2.3.I | 2.3 | 552 | IFRS-9-financiele-instrumenten (84), IFRS-7-financiele-instrumenten (49), IFRS-17-verzekeringscontracten (39) |
| 1.3.I.D | 1.3 | 551 | ISA-315-herzien-2019 (50), ISA-600 (28), ISA-700-herzien (25) |
| 4.0.II.C | 4.0 | 546 | ISA-315-herzien-2019 (52), ISA-540-herzien (30), ISA-600 (28) |
| 1.6.taak.1 | 1.6 | 542 | ISA-315-herzien-2019 (48), ISA-540-herzien (28), ISA-600 (27) |
| 1.7.III.B | 1.7 | 542 | ISA-315-herzien-2019 (53), ISA-540-herzien (34), ISA-600 (28) |
| 2.8.taak.2 | 2.8 | 541 | IFRS-9-financiele-instrumenten (55), IFRS-3-bedrijfscombinaties (34), IFRS-7-financiele-instrumenten (29) |
| 1.7.VIII.F | 1.7 | 539 | ISA-315-herzien-2019 (39), ISA-540-herzien (30), ISA-700-herzien (23) |
| 1.8.VI | 1.8 | 539 | IFRS-9-financiele-instrumenten (53), ISA-315-herzien-2019 (35), ISA-540-herzien (26) |

_… +398 meer anchors (zie JSON-rapport)._
