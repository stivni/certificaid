---
title: Tabel van waardemutaties (mutatietabel vaste activa)
tags:
- concept
- cluster
- po-1-9
linked_anchors:
- 1.9.IV.B
- 1.9.IV
programmaonderdelen:
- '1.9'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/tabel-waardemutaties.json
gegenereerd_op: '2026-05-18'
---
# Tabel van waardemutaties (mutatietabel vaste activa) ⚖️

> [!summary] Korte inhoud
> De tabel van waardemutaties toont voor elke rubriek vaste activa de bewegingen van het boekjaar: aanschaffingen, desinvesteringen, overdrachten, afschrijvingen, waardeverminderingen en hun terugnemingen.

> [!info] Behoort tot: [[jaarrekening-als-studieobject]]

De tabel van waardemutaties toont voor elke rubriek vaste activa de bewegingen van het boekjaar: aanschaffingen, desinvesteringen, overdrachten, afschrijvingen, waardeverminderingen en hun terugnemingen. Ze verbindt de openingsbalans met de eindbalans en is bron voor de kasstroomanalyse.

_Bron: KB WVV — toelichtingsstaten volledig schema (NBB-modellen)_


## Bouwstenen

### Vier soorten bewegingen per rubriek ⚖️

Per vaste-activa-rubriek (immateriële, materiële, financiële) toont de tabel: (1) aanschaffingen + overdrachten, (2) desinvesteringen + buitengebruikstellingen, (3) overdrachten naar andere rubrieken, (4) afschrijvingen + waardeverminderingen en hun terugnemingen.

**Waarom?** Door de bewegingen apart te tonen kan de analist de investerings-kasstroom uit het kasstroomoverzicht reconstrueren — wat balansvergelijking alleen niet toelaat.


_Grondslag: KB WVV toelichtingsstaten_

### Brug naar kasstroom uit investeringen 🤖

De aanschaffingen (cash uitstroom) en desinvesteringen (cash instroom) uit de tabel zijn rechtstreekse input voor de investerings-kasstroom van het kasstroomoverzicht.

**Waarom?** Zonder de mutatietabel kan een analist de investerings-kasstroom niet correct schatten — afschrijvingen zijn niet-kas (mogen niet in CFI) maar wijzigen wel de balans-eindwaarde.


_Grondslag: Vakdoctrine — gebruik van mutatietabel in kasstroomanalyse_


## In de praktijk

<h3 id="1.9.IV.B">Examen-vraag herkenning</h3>

> [!tip]- Examen-vraag herkenning
> Wanneer een vraag balanseindwaarden vergelijkt met openingswaarden en de afschrijvingen kent: gebruik de mutatietabel-formule (begin + aanschaffingen − afschrijvingen − desinvesteringen = einde) om aanschaffingen of desinvesteringen te isoleren. 🤖


## Zie ook

- **Vereist kennis van**: [[kasstroomoverzicht-drie-segmenten]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `KB-WVV-toelichting-vaste-activa`
[^2]: `anchor-1.9.IV.B`
