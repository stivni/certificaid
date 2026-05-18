---
title: Altman Z-score (faillissement-predictiemodel)
tags:
- concept
- cluster
- po-1-9
linked_anchors:
- 1.9.VI.B
- 1.9.VI
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/altman-z-score.json
gegenereerd_op: '2026-05-18'
---
# Altman Z-score (faillissement-predictiemodel) 🤖

> [!summary] Korte inhoud
> Het Altman Z-model voorspelt het faillissementsrisico van een onderneming via een gewogen lineaire combinatie van vijf ratio's.

> [!info] Behoort tot: [[kwantitatieve-financiele-diagnose]]

Het Altman Z-model voorspelt het faillissementsrisico van een onderneming via een gewogen lineaire combinatie van vijf ratio's. Een lage Z-waarde signaleert verhoogd faillissementsrisico binnen 2 jaar; een hoge Z-waarde wijst op financiële gezondheid. Belangrijk: het is een discriminantmodel, geen waarschijnlijkheidsuitspraak.

_Bron: Altman (1968) — internationale financiële-analyse-doctrine_


## Bouwstenen

### Vijf ratio's gewogen via discriminant-analyse 🤖

Z combineert vijf ratio's: (1) NBK/TA (werkkapitaal/totaal activa) — liquiditeit; (2) IW/TA (ingehouden winst/totaal activa) — accumulatie; (3) EBIT/TA — operationele rentabiliteit; (4) MVE/VV (marktwaarde EV/totaal vreemd vermogen) — solvabiliteit; (5) O/TA (omzet/totaal activa) — activarotatie.

**Waarom?** Discriminant-analyse op een steekproef van gefailleerde + niet-gefailleerde ondernemingen gaf de optimale gewichten. Elk van de vijf ratio's vangt een ander aspect van financiële gezondheid op.

**Voorbeeld**: Rotex Roeselare NV — NBK/TA = 0,27, IW/TA = 0,07, EBIT/TA = 0,20, MVE/VV = 0,67, O/TA = 1,67 → Z = 1,2×0,27 + 1,4×0,07 + 3,3×0,20 + 0,6×0,67 + 1,0×1,67 = 0,32 + 0,10 + 0,66 + 0,40 + 1,67 = **3,15** → gezonde zone (Z > 2,99).

_Grondslag: Altman (1968)_

### Drie interpretatiezones 🤖

Originele cut-offs (publieke productiebedrijven, VS): Z < 1,81 = distress zone (hoog faillissementsrisico binnen 2 jaar); 1,81 ≤ Z < 2,99 = grey zone (onzeker); Z ≥ 2,99 = safe zone (financieel gezond).

**Waarom?** De cut-offs zijn empirisch: ze maximaliseren het onderscheid tussen de twee steekproef-groepen. De grey zone vraagt om aanvullende analyse — Altman alléén volstaat niet voor een diagnose.

**Voorbeeld**: Verffabriek Veurne BV in vereffening — Z = 0,8 (distress zone); Rotex Roeselare NV — Z = 3,15 (safe zone).

_Grondslag: Altman (1968)_


## Berekening

### Altman Z-score (origineel model)

**Z-score voor publieke productiebedrijven** 
```
Z = 1,2×(NBK/TA) + 1,4×(IW/TA) + 3,3×(EBIT/TA) + 0,6×(MVE/VV) + 1,0×(O/TA)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `NBK/TA` | Netto bedrijfskapitaal / totaal activa | ratio |
| `IW/TA` | Ingehouden winst / totaal activa | ratio |
| `EBIT/TA` | Operationeel resultaat vóór intrest en belasting / totaal activa | ratio |
| `MVE/VV` | Marktwaarde eigen vermogen / totaal vreemd vermogen (boekwaarde EV indien niet beursgenoteerd) | ratio |
| `O/TA` | Omzet / totaal activa | ratio |

**Voorbeeld-invulling**: Rotex Roeselare NV — NBK/TA = 0,27, IW/TA = 0,07, EBIT/TA = 0,20, MVE/VV = 0,67, O/TA = 1,67

```
1,2×0,27 + 1,4×0,07 + 3,3×0,20 + 0,6×0,67 + 1,0×1,67 = 3,15
```

_Resultaat in Z-score (dimensieloos)_

## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
| Distress zone | Z < 1,81 | Z-score | Hoog faillissementsrisico binnen 2 jaar — diepere diagnose vereist |
| Grey zone | 1,81 ≤ Z < 2,99 | Z-score | Onzekere uitkomst — aanvullende analyse vereist |
| Safe zone | Z ≥ 2,99 | Z-score | Financieel gezond op basis van het model |


> [!info]- Niet verwarren met [[ohlson-o-score]]
> Altman = discriminant-analyse (lineair, 5 ratio's, drie zones). Ohlson = logistische regressie (9 variabelen, geeft kansprobabiliteit tussen 0 en 1). Beide ontwikkeld voor faillissementsvoorspelling maar verschillen in techniek én input.
>
> _Trigger_: Examenvraag 'welk model gebruik je?': Altman geeft een score-positie; Ohlson een kans. Bij twijfel beide berekenen en triangulair lezen.


## Valkuilen

> [!warning]- Het originele Altman-model is geijkt op grote Amerikaanse productiebedrijven uit de jaren '60
> ⚠️ Het originele Altman-model is geijkt op grote Amerikaanse productiebedrijven uit de jaren '60. Voor Belgische KMO's of niet-productiebedrijven gelden andere cut-offs (Altman Z'-model voor niet-beursgenoteerd; Z''-model voor niet-productie). Pas dit niet blind toe. 🤖
>
> _Bron: Altman (1968) + latere herzieningen_


> [!warning]- Z-score is een statistisch signaal, geen voorspelling
> ⚠️ Z-score is een statistisch signaal, geen voorspelling. Een Z onder 1,81 zegt 'lijkt op gefailleerde bedrijven uit de steekproef' — niet 'failliet binnen X dagen'. Gebruik het samen met kwalitatieve elementen (markt, management, bestuursverslag). 🤖
>
> _Bron: Financiële diagnose_



## Zie ook

- **Vereist kennis van**: [[werkkapitaal]]
- **Vereist kennis van**: [[solvabiliteitsratio]]

## Bronnen

[^1]: `anchor-1.9.VI.B`
