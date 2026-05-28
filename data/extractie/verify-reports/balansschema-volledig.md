# Verify-rapport: balansschema-volledig

## Status
- Record-bestand: **NIET AANWEZIG** in `data/concepten/records/`
- Sample-task verwacht `balansschema-volledig.json` maar dit bestand bestaat niet in de records-folder

## Vaststelling
- Wel aanwezig als bouwsteen `balansschema-volledig` IN `jaarrekening.json` (samen met `balansschema-verkort` + `balansschema-micro`)
- Mogelijk een ontwerpkeuze: de drie schema-varianten leven als bouwstenen onder `jaarrekening` en hebben (nog) geen eigen top-level record

## Aanbeveling
Twee mogelijke acties voor Pass 3:
1. **Bevestig keuze 'bouwsteen onder jaarrekening'**: dan task-spec voor verify aanpassen — geen apart record verwachten
2. **Promoveren tot eigen records**: indien examen-vragen frequent uitsplitsen naar specifieke schema-keuze + commissaris-trigger + sociale-balans-impact, kan een eigen record nuttig zijn (cluster-extract op nieuw skeleton)

## Severity
- N.v.t. — geen record om te verifiëren. Status: **OUT-OF-SAMPLE**
