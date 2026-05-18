---
title: Herstructurering van de resultatenrekening
tags:
- concept
- cluster
- po-1-9
linked_anchors:
- 1.9.III.B
- 1.9.III.C
- 1.9.III
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/herstructurering-resultatenrekening.json
gegenereerd_op: '2026-05-18'
---
# Herstructurering van de resultatenrekening 🤖

> [!summary] Korte inhoud
> De resultatenrekening wordt herwerkt zodat ze leesbaar wordt vanuit economisch perspectief: opbrengsten en kosten worden gegroepeerd in bedrijfs-, financiële, uitzonderlijke en belastingblokken; binnen het bedrijfsblok wordt de toegevoegde waarde geïsoleerd.

De resultatenrekening wordt herwerkt zodat ze leesbaar wordt vanuit economisch perspectief: opbrengsten en kosten worden gegroepeerd in bedrijfs-, financiële, uitzonderlijke en belastingblokken; binnen het bedrijfsblok wordt de toegevoegde waarde geïsoleerd. Voor verkort/microschema's vraagt dat meer werk omdat sommige rubrieken samengevoegd zijn.

_Bron: Financiële analyse — NBB-balansanalyse_


## Bouwstenen

### Vier blokken: bedrijf, financieel, uitzonderlijk, belasting ⚖️

Groepeer de RR-rubrieken volgens hun aard: bedrijfsopbrengsten/kosten (60-64 + 70-74), financiële opbrengsten/kosten (65 + 75), uitzonderlijke opbrengsten/kosten (66 + 76 — verdwijnt in NIEUW WVV-schema), belastingen op resultaat (67 + 77).

**Waarom?** Elk blok beantwoordt een ander analyse-onderwerp: bedrijf = winstgevendheid kernactiviteit; financieel = financieringskost-impact; uitzonderlijk = eenmalige items te filteren; belasting = effectieve aanslagvoet.


_Grondslag: KB WVV — schema resultatenrekening_

### Isoleer de toegevoegde waarde 🤖

Binnen het bedrijfsblok wordt eerst de toegevoegde waarde berekend (zie [[toegevoegde-waarde-financiele-analyse]]). Onder de TW staan: personeelskosten, afschrijvingen, andere bedrijfskosten — als verdeling.

**Waarom?** Dit maakt de RR een productiviteits-document: TW per VTE wordt zichtbaar, en de verdeling personeel/kapitaal/overheid is uitleesbaar.


_Grondslag: Vakdoctrine financiële analyse_

### Verkort/microschema vraagt meer werk ⚖️

In verkort schema (rubrieken 60/61 samengevoegd) of microschema (verdere samenvoegingen) zijn aankopen handelsgoederen en diensten in één post — de TW-berekening vereist een schatting of toelichting.

**Waarom?** Een grondige analyse van een kleine BV (verkort/micro) vraagt om bijkomende informatie buiten de jaarrekening (toelichting, navragen bij bestuursorgaan). Dit is een gekende beperking, geen fout in de analyse.


_Grondslag: KB WVV — verkort en microschema_


> [!info]- Niet verwarren met [[analytische-balans]]
> Analytische balans = herstructurering van de balans (activa/passiva op functioneel-economische rubrieken); herstructurering RR = herstructurering van de resultatenrekening (opbrengsten/kosten in vier blokken + TW-isolatie). Beide samen vormen de basis voor ratio-analyse.
>
> _Trigger_: Examenvraag 'herstructurering jaarrekening': beide aspecten benoemen, niet alleen balans.


## Zie ook

- **Vereist kennis van**: [[analytische-balans]]
- **Vereist kennis van**: [[toegevoegde-waarde-financiele-analyse]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `anchor-1.9.III.B`
[^2]: `KB-WVV-schema-RR`
