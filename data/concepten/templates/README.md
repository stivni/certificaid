# Balans- en Resultatenrekening-templates

Deze map bevat **referentie-skeletons** voor de meest voorkomende boekhoudkundige artefacten die in `voorbeeld.substappen[].data`-velden van concept-records en competentie-yamls verschijnen.

## Doel

Stagiairs leren consolidatie via concrete balansen en resultatenrekeningen. Concept-records gebruiken deze structuren in substappen van voorbeelden. Templates dwingen **consistente rubrieken** af en helpen de extractor/enricher om correcte structuren te produceren — **niet** als render-time substitutie maar als kennis-bron tijdens prompting.

## Hoe een extractor deze templates gebruikt

1. Lees de relevante template (bv. `balans-geconsolideerd.md`) als referentie
2. Bouw de substap-data in dezelfde rubriek-volgorde
3. Vul de waarden met cast-namen en realistische bedragen in €
4. Mechanische check via VERIFY: activa-totaal = passiva-totaal; opbrengsten − kosten = resultaat

## Mechanische validatie

VERIFY-aspecten (ADR-008 §17):
- `balans.klopt-niet` — activa ≠ passiva
- `balans.rubriek-ontbreekt` — kerncategorie (Vaste activa / EV / Schulden) mist
- `resultatenrekening.klopt-niet` — Opbrengsten − Kosten ≠ Resultaat

## Bestanden

- `balans-verkort.md` — 2 hoofdcategorieën activa/passiva (Vaste/Vlottende + EV/Schulden)
- `balans-volledig.md` — alle KB WVV-rubrieken op enkelvoudig niveau
- `balans-geconsolideerd.md` — met Belangen van derden + Consolidatieverschillen + Vennootschappen waarop vermogensmutatie
- `resultatenrekening-verkort.md` — netto-resultaat-structuur
- `resultatenrekening-volledig.md` — bedrijfs/financieel/uitzonderlijk resultaat
- `boekingsregel.md` — debet/credit-tabel voor één boeking
