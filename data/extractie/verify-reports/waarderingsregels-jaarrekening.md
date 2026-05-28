# Verify-rapport: waarderingsregels-jaarrekening

## Status
- Record-bestand: **NIET AANWEZIG** in `data/concepten/records/`
- Wel aanwezig: `uniforme-waarderingsregels-consolidatie.json` (specifiek voor consolidatie-context)

## Vaststelling
- Generieke waarderingsregels worden afgehandeld:
  - Bouwsteen `waarderingsregels-vastlegging` in `jaarrekening.json`
  - Speelruimte `Waarderingsregels-keuze` in `jaarrekening.json`
  - Per balanspost in respectievelijke records (`voorraden` waardering, `voorzieningen` waardering, ...)
- Het concept "waarderingsregels" als zelfstandig fenomeen is niet als top-level record uitgewerkt — werkt als procedure-aspect binnen jaarrekening en als regime-specifieke variant in consolidatie

## Aanbeveling
Waarderingsregels-keuze + bestendigheid (art. 3:6 + 3:8 KB) + presentatie in toelichting zou op zich genoeg substantie hebben voor eigen record (CBN 2020/05 als hoofdbron) — overweeg skeleton + cluster-extract in nieuwe wave. Voor PO 1.1 verify-task: dekking is functioneel verspreid maar niet centraal vindbaar.

## Severity
- N.v.t. — geen record om te verifiëren. Status: **OUT-OF-SAMPLE**
