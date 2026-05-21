---
title: Verticale analyse (percentageanalyse, common-size)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.I.C
- 1.3.II.B
- 1.3.II.C
- 1.3.taak.1
- 1.9.III
- 1.9.III.E
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/verticale-analyse-jaarrekening.json
gegenereerd_op: '2026-05-21'
---
# Verticale analyse (percentageanalyse, common-size) 🔗

De samenstelling van balans en resultatenrekening uitdrukken in procenten van een gemeenschappelijke noemer (balanstotaal voor de balans, omzet voor de resultatenrekening). Zo wordt vergelijking tussen ondernemingen van verschillende grootte mogelijk.



## Bouwstenen

### Balanspost als % van balanstotaal 🤖

Voor elke balanspost: deel door het balanstotaal en druk uit als percentage. Het totaal van de actief-zijde is 100 %; idem passiefzijde.

**Waarom?** Zo zie je de structuur: hoeveel vaste activa, vlottende activa, eigen vermogen, lange schulden, korte schulden — zonder dat schaal de blik verstoort.



Rotex Roeselare NV (balanstotaal € 30.000.000): vaste activa € 18.000.000 = 60 %; vlottende activa € 12.000.000 = 40 %. Eigen vermogen 40 %; lange schulden 43 %; korte schulden 17 %.

_Grondslag: Vakdoctrine_

### Resultatenpost als % van omzet 🤖

Voor elke kost en opbrengst: deel door de omzet. Omzet is 100 %; alle andere posten een percentage daarvan.

**Waarom?** Toont kostenstructuur en marges. Geeft direct zicht op brutomarge, bedrijfsresultaatmarge, nettomarge.



Rotex Roeselare NV (omzet € 50.000.000): handelsgoederen € 30.000.000 = 60 %; personeelskosten € 8.000.000 = 16 %; afschrijvingen € 1.500.000 = 3 %; nettowinst € 2.500.000 = 5 %.

_Grondslag: Vakdoctrine_


## Berekening

### Common-size balans en resultatenrekening

**Verticale-analyse-percentage** 
```
aandeel_post = (post / noemer) × 100
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `post` | Te analyseren balans- of resultatenpost | EUR |
| `noemer` | Balanstotaal (voor balans) of omzet (voor resultatenrekening) | EUR |

**Voorbeeld-invulling**: Personeelskosten Rotex 20X1 = € 8.000.000; omzet = € 50.000.000

```
(€ 8.000.000 / € 50.000.000) × 100 = 16,0 %
```

_Resultaat in %_
*Door alles als percentage van eenzelfde noemer uit te drukken, zijn balansen of resultatenrekeningen van zeer verschillende grootte rechtstreeks vergelijkbaar — zowel met andere ondernemingen als met sectorgemiddelden.*

### 1. Kies noemer per overzicht

Balans → balanstotaal; resultatenrekening → omzet (of bedrijfsopbrengsten als omzet niet bruikbaar is).

**🛠️ Hoe**:

1. Voor Rotex Roeselare NV: balans-noemer € 30.000.000; resultatenrekening-noemer omzet € 50.000.000.


**Grondslag**: Vakdoctrine

### 2. Bereken percentages per post

Voor elke post: (post / noemer) × 100.

**🛠️ Hoe**:

1. Bv. eigen vermogen Rotex: € 12.000.000 / € 30.000.000 × 100 = 40 %.
2. Bv. personeelskosten Rotex: € 8.000.000 / € 50.000.000 × 100 = 16 %.


> [!example]- Voorbeeld: Rotex Roeselare NV — common-size balans (kant passief, boekjaar 20X1)
> Rotex Roeselare NV — common-size balans (kant passief, boekjaar 20X1).
>
> 1. **Common-size passief** 📊
>
>    | Rubriek                          | Bedrag (€)     | Aandeel |
>    |----------------------------------|---------------:|--------:|
>    | Eigen vermogen                   |     12.000.000 |   40 %  |
>    | Voorzieningen + uitgest. bel.    |      1.000.000 |    3 %  |
>    | Schulden > 1 jaar                |     13.000.000 |   43 %  |
>    | Schulden ≤ 1 jaar                |      3.800.000 |   13 %  |
>    | Overlopende rekeningen passief   |        200.000 |    1 %  |
>    | **Balanstotaal**                 | **30.000.000** | **100 %** |
>

**Grondslag**: Vakdoctrine

### 3. Vergelijk met sector of vorig boekjaar

De common-size cijfers laten zich direct vergelijken met sectormediaan of met vorig boekjaar — schaalverschillen verdwijnen.

**🛠️ Hoe**:

1. Vergelijk Rotex passief-mix (40 % EV) met sectormediaan (32 % EV) → conclusie: Rotex is robuuster gefinancierd dan sector.
2. Bv. de personeelskosten-marge stijgt van 14 % naar 16 % over 2 jaar → productiviteit onder druk.


**Grondslag**: Vakdoctrine

**Voorbeeld**: Rotex Roeselare NV — common-size resultatenrekening boekjaar 20X1; omzet € 50.000.000.

```
Handelsgoederen € 30M / € 50M = 60 %; personeelskosten € 8M / € 50M = 16 %; afschrijvingen € 1,5M / € 50M = 3 %; bedrijfsresultaat € 4,2M / € 50M = 8,4 %; nettowinst € 2,5M / € 50M = 5 %.
```

Resultaat: Brutomarge 40 % (na handelsgoederen); bedrijfsmarge 8,4 %; nettomarge 5 %. In één tabel zichtbaar; vergelijkbaar met sectorgemiddelden en met vorig boekjaar.

> [!info]- Niet verwarren met [[horizontale-analyse-jaarrekening]]
> Verticaal = samenstelling op één moment (alle posten als % van zelfde noemer). Horizontaal = evolutie over tijd (elke post vs. basisjaar). Verticaal toont structuur, horizontaal toont trend.
>
> _Trigger_: Examen 'samenstelling of trend?': samenstelling = verticaal; trend = horizontaal.


## Valkuilen

> [!warning]- Bij vennootschappen zonder echte 'omzet' (financieel actief, holding) is omzet als noemer onbruikbaar
> ⚠️ Bij vennootschappen zonder echte 'omzet' (financieel actief, holding) is omzet als noemer onbruikbaar. Gebruik dan 'bedrijfsopbrengsten' of een totaal-noemer. 🔗
>
> _Bron: Financial analysis_



## Zie ook

- **Wordt voorondersteld in** (1): [[analytische-balans]]
## Bronnen

[^1]: `anchor-1.3.I.C`
