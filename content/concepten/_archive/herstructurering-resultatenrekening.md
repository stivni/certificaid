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
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/herstructurering-resultatenrekening.json
gegenereerd_op: '2026-05-21'
---
# Herstructurering van de resultatenrekening 🔗

De resultatenrekening wordt herwerkt zodat ze leesbaar wordt vanuit economisch perspectief: opbrengsten en kosten worden gegroepeerd in bedrijfs-, financiële, uitzonderlijke en belastingblokken; binnen het bedrijfsblok wordt de toegevoegde waarde geïsoleerd. Voor verkort/microschema's vraagt dat meer werk omdat sommige rubrieken samengevoegd zijn.



## Bouwstenen

### Vier blokken: bedrijf, financieel, uitzonderlijk, belasting ⚖️

Groepeer de RR-rubrieken volgens hun aard: bedrijfsopbrengsten/kosten (60-64 + 70-74), financiële opbrengsten/kosten (65 + 75), uitzonderlijke opbrengsten/kosten (66 + 76 — verdwijnt in NIEUW WVV-schema), belastingen op resultaat (67 + 77).

**Waarom?** Elk blok beantwoordt een ander analyse-onderwerp: bedrijf = winstgevendheid kernactiviteit; financieel = financieringskost-impact; uitzonderlijk = eenmalige items te filteren; belasting = effectieve aanslagvoet.



Rotex Roeselare NV — bedrijfsresultaat € 6.000.000, financieel resultaat − € 600.000, belastingen − € 1.500.000, nettoresultaat € 2.500.000 (geen uitzonderlijk in nieuw schema).

_Grondslag: KB WVV — schema resultatenrekening_

### Isoleer de toegevoegde waarde 🤖

Binnen het bedrijfsblok wordt eerst de toegevoegde waarde berekend (zie [[toegevoegde-waarde-financiele-analyse]]). Onder de TW staan: personeelskosten, afschrijvingen, andere bedrijfskosten — als verdeling.

**Waarom?** Dit maakt de RR een productiviteits-document: TW per VTE wordt zichtbaar, en de verdeling personeel/kapitaal/overheid is uitleesbaar.



Rotex Roeselare NV — TW € 18.000.000 − personeelskosten € 12.000.000 − afschrijvingen € 1.500.000 − andere bedrijfskosten = bedrijfsresultaat € 6.000.000 (na correctie).

_Grondslag: Vakdoctrine financiële analyse_

### Verkort/microschema vraagt meer werk ⚖️

In verkort schema (rubrieken 60/61 samengevoegd) of microschema (verdere samenvoegingen) zijn aankopen handelsgoederen en diensten in één post — de TW-berekening vereist een schatting of toelichting.

**Waarom?** Een grondige analyse van een kleine BV (verkort/micro) vraagt om bijkomende informatie buiten de jaarrekening (toelichting, navragen bij bestuursorgaan). Dit is een gekende beperking, geen fout in de analyse.



Meubelzaak Mertens BV (verkort schema): rubriek 60/61 = € 600.000 — onmogelijk om aankopen handelsgoederen van diensten te scheiden zonder toelichting. TW-detail blijft dus geschat.

_Grondslag: KB WVV — verkort en microschema_


## In de praktijk

<h3 id="1.9.III.B">Examen-relevantie: vier blokken én TW-isolatie</h3>

> [!tip]- Examen-relevantie: vier blokken én TW-isolatie
> Op het examen wordt getoetst of de stagiair een 'platte' resultatenrekening kan ontleden in (1) bedrijfs-, (2) financieel, (3) uitzonderlijk (oud schema) en (4) belastingblok, én daarbinnen de toegevoegde waarde kan isoleren. Vraag-type: 'herstructureer onderstaande RR' of 'bereken de TW uit volgende gegevens'. Antwoord moet beide niveaus tonen: blok-indeling én TW-detail. 🔗

<h3 id="1.9.III.C">Verkort/microschema vraagt expliciete vermelding van beperking</h3>

> [!tip]- Verkort/microschema vraagt expliciete vermelding van beperking
> Bij analyse van een verkort- of microschema (zoals een kleine BV) moet de stagiair in het antwoord uitdrukkelijk aangeven dat de TW-berekening onvolledig blijft zonder toelichtingsinformatie. De examencorrector beoordeelt het zien van de beperking, niet het magisch invullen van ontbrekende cijfers. 🔗

<h3 id="1.9.III.B">Concretisering Rotex Roeselare NV (volledig schema)</h3>

> [!tip]- Concretisering Rotex Roeselare NV (volledig schema)
> Volledig schema RR: omzet € 30.000.000 + andere bedrijfsopbrengsten € 500.000 − aankopen handelsgoederen € 12.500.000 = TW € 18.000.000. Daaronder: personeelskosten − € 12.000.000, afschrijvingen − € 1.500.000, andere bedrijfskosten ≈ − € 1.500.000 → bedrijfsresultaat ≈ € 3.000.000. Financieel resultaat − € 600.000, belastingen − € 1.500.000 → nettoresultaat ≈ € 900.000 (cijfers zijn illustratief). 🔗


> [!info]- Niet verwarren met [[analytische-balans]]
> Analytische balans = herstructurering van de balans (activa/passiva op functioneel-economische rubrieken); herstructurering RR = herstructurering van de resultatenrekening (opbrengsten/kosten in vier blokken + TW-isolatie). Beide samen vormen de basis voor ratio-analyse.
>
> _Trigger_: Examenvraag 'herstructurering jaarrekening': beide aspecten benoemen, niet alleen balans.


## Zie ook

- **Vereist kennis van**: [[analytische-balans]]
- **Vereist kennis van**: [[toegevoegde-waarde-financiele-analyse]]

## Bronnen

[^1]: `KB-WVV-schema-RR`
[^2]: `anchor-1.9.III.B`
[^3]: `anchor-1.9.III.C`
