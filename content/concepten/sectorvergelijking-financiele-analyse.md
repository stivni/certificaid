---
title: Sectorvergelijking (benchmarking)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.II.A
- 1.3.II.C
- 1.3.taak.1
- 1.9.III.E
- 1.9.V.E
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/sectorvergelijking-financiele-analyse.json
gegenereerd_op: '2026-05-18'
---
# Sectorvergelijking (benchmarking) 🤖

De ratio's en kengetallen van een onderneming plaatsen tegenover de mediaan of het gemiddelde van haar sector. Een ratio die in absolute zin lijkt zwak (of sterk), kan in sectorcontext normaal zijn. Sectorvergelijking maakt de analyse interpreteerbaar.


## Bouwstenen

### Sectorgrenzen bepalen 🤖

Identificeer de sector waarin de onderneming actief is — bij voorkeur via NACE-code, anders door analyse van haar producten en markten. Beperkt tot vergelijkbare bedrijven (geografie, schaal, marktsegment).

**Waarom?** Een te brede definitie verwatert de vergelijking. Een te enge definitie laat te weinig vergelijkbare bedrijven over.



Rotex Roeselare NV (metaalconstructie B2B) wordt vergeleken met andere Vlaamse metaalconstructeurs van vergelijkbare grootte — niet met de bredere 'metallurgie'-sector.

_Grondslag: Vakdoctrine_

### Mediaan boven gemiddelde 🤖

De mediaan is meestal informatiever dan het gemiddelde, vooral bij sectoren met uitschieters (één zeer groot bedrijf vertekent het gemiddelde).

**Waarom?** De mediaan is robuust tegen extreme waarden; het gemiddelde is dat niet.



In de sector metaalconstructie heeft één multinational ROE 30 %; 9 KMO's hebben ROE rond 10 %. Gemiddelde = 12 %; mediaan = 10 % → de mediaan vertelt het accurater verhaal.

_Grondslag: Vakdoctrine statistiek_


## In de praktijk

<h3 id="1.3.II.A">Bronnen voor sectorcijfers</h3>

> [!tip]- Bronnen voor sectorcijfers
> Nationale Bank van België publiceert geaggregeerde sectorratios; sectorfederaties publiceren benchmark-rapporten; commerciële databases (Belfirst, Trends Top, ...) leveren peer-cijfers. 🤖


## Valkuilen

> [!warning]- Sectorgemiddelden kunnen verouderd zijn (publicatie 1-2 jaar na boekjaar)
> ⚠️ Sectorgemiddelden kunnen verouderd zijn (publicatie 1-2 jaar na boekjaar). Houd rekening met die vertraging — vooral in conjunctuurgevoelige sectoren. 🤖
>
> _Bron: Financial analysis_



## Zie ook

- **Vereist kennis van**: [[historische-evolutie-financiele-analyse]]
- **Wordt voorondersteld in** (3): [[financiele-analyse-software]] · [[historische-evolutie-financiele-analyse]] · [[interpretatie-financiele-ratios]]
## Bronnen

[^1]: `anchor-1.3.II.A`
