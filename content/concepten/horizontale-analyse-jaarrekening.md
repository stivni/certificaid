---
title: Horizontale analyse (evolutie-analyse)
tags:
- concept
- cluster
- po-1-3
- po-1-9
linked_anchors:
- 1.3.I.C
- 1.3.II.A
- 1.3.II.C
- 1.3.taak.1
- 1.9.III
- 1.9.III.D
- 1.9.taak.1
programmaonderdelen:
- '1.3'
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/horizontale-analyse-jaarrekening.json
gegenereerd_op: '2026-05-18'
---
# Horizontale analyse (evolutie-analyse) 🤖

> [!summary] Korte inhoud
> De evolutie van balans- en resultatenposten over meerdere boekjaren in kaart brengen.

De evolutie van balans- en resultatenposten over meerdere boekjaren in kaart brengen. Elke post wordt uitgedrukt als verandering tegenover een basisjaar (in absolute euro's of in procenten), zodat trends zichtbaar worden.

_Bron: Algemene financial-analysis-doctrine_


## Bouwstenen

### Vergelijking met vorig boekjaar of basisjaar 🤖

Voor elke balanspost en resultatenrekening-post: bereken het verschil met het vorige boekjaar (of een vast basisjaar) — absoluut en in procenten.

**Waarom?** Eén boekjaar alleen toont niet of de onderneming groeit, stagneert of krimpt. Trends zijn meestal belangrijker dan momentopnames.


_Grondslag: Vakdoctrine_

### KB WVV verplicht vergelijkende cijfers 🤖

Het Belgisch jaarrekeningenrecht verplicht het opnemen van de cijfers van het voorgaande boekjaar naast die van het lopende boekjaar — dat is de bouwsteen waarop horizontale analyse rust.

**Waarom?** Zonder vergelijkende cijfers zou elke jaarrekening op zichzelf staan en zou trendanalyse onmogelijk zijn.


_Grondslag: KB WVV (vergelijkende cijfers — algemene regel)_


## Berekening

### Horizontale evolutie

**Horizontale evolutie-index** 
```
index_boekjaar = (waarde_boekjaar / waarde_basisjaar) × 100
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `waarde_boekjaar` | Waarde van de post in het te analyseren boekjaar | EUR |
| `waarde_basisjaar` | Waarde van dezelfde post in het basisjaar | EUR |

**Voorbeeld-invulling**: Omzet Rotex 20X2 = € 55.000.000; basisjaar 20X0 = € 45.000.000

```
(€ 55.000.000 / € 45.000.000) × 100 = 122,2
```

_Resultaat in index_
*Het basisjaar krijgt index 100. Volgende boekjaren krijgen index = (boekjaar / basisjaar) × 100. Het verschil met 100 is direct het cumulatief groei- of krimppercentage.*

### 1. Kies basisjaar

Selecteer een basisjaar — meestal het oudste in de analyseperiode.

**🛠️ Hoe**:

1. Voor een 5-jarige trendanalyse van Rotex Roeselare NV: kies boekjaar 20X0 als basis.


**Grondslag**: Vakdoctrine

### 2. Bereken indexen per post

Voor elke balans- of resultaatpost: index = (waarde boekjaar / waarde basisjaar) × 100.

**🛠️ Hoe**:

1. Voor de omzet: 20X0 = € 45.000.000 → index 100; 20X1 = € 50.000.000 → index 111,1; 20X2 = € 55.000.000 → index 122,2.
2. Doe hetzelfde voor: voorraden, vorderingen, schulden, ...


> [!example]- Voorbeeld: Rotex Roeselare NV — drie opeenvolgende boekjaren, omzetevolutie
> Rotex Roeselare NV — drie opeenvolgende boekjaren, omzetevolutie.
>
> 1. **Indextabel omzet** 🧮
>
>    | Boekjaar | Omzet (€)      | Index (basis 100) |
>    |----------|---------------:|------------------:|
>    | 20X0     |     45.000.000 |              100,0 |
>    | 20X1     |     50.000.000 |              111,1 |
>    | 20X2     |     55.000.000 |              122,2 |
>

**Grondslag**: Vakdoctrine

### 3. Vergelijk evoluties tussen posten

Plot de evolutie van verschillende posten naast elkaar. Verschillen in groeitempo wijzen op structurele wijzigingen.

**🛠️ Hoe**:

1. Als omzet stijgt met 22 % maar voorraden met 75 %: voorraadrotatie verslechtert → mogelijk verkoopprobleem.
2. Als personeelskosten stijgen met 40 % maar omzet met 22 %: productiviteit daalt.


**Grondslag**: Vakdoctrine

**Voorbeeld**: Rotex Roeselare NV: omzet 20X0=€45M; 20X1=€50M; 20X2=€55M. Voorraden 20X0=€2M; 20X1=€2,5M; 20X2=€3,5M.

```
Omzet-indexen: 100 / 111,1 / 122,2. Voorraad-indexen: 100 / 125,0 / 175,0.
```

Resultaat: Voorraden groeien sneller dan omzet → vraag stelt zich of verkoop dezelfde tempo aanhoudt en of waardeverminderingen nodig zijn.

> [!info]- Niet verwarren met [[verticale-analyse-jaarrekening]]
> Horizontale analyse = evolutie in tijd (boekjaar-op-boekjaar). Verticale analyse = samenstelling binnen één boekjaar (elke post als % van balanstotaal of omzet).
>
> _Trigger_: Examenvraag 'evolutie of structuur?': over de tijd = horizontaal; samenstelling op één moment = verticaal.


## Valkuilen

> [!warning]- Bij sterk fluctuerende waarden krijgt een laag basisjaar gevolg op alle indexen — een 'goed' basisjaar (gemiddeld of pre-crisis) kiezen is e…
> ⚠️ Bij sterk fluctuerende waarden krijgt een laag basisjaar gevolg op alle indexen — een 'goed' basisjaar (gemiddeld of pre-crisis) kiezen is essentieel. 🤖
>
> _Bron: Financial analysis_



## Bronnen

[^1]: `anchor-1.3.I.C`
