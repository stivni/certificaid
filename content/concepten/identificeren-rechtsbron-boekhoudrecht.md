---
title: Identificeren van de toepasselijke rechtsbron bij een vraag uit het boekhoudrecht
tags:
- concept
- competentie
- po-1-2
linked_anchors:
- 1.2.I
- 1.2.I.A
- 1.2.I.C
- 1.2.I.D
- 1.2.I.E
- 1.2.I.F
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/identificeren-rechtsbron-boekhoudrecht.json
gegenereerd_op: '2026-05-18'
---
# Identificeren van de toepasselijke rechtsbron bij een vraag uit het boekhoudrecht 🤖


## Stappen

### 1. Kwalificeer het type vraag

Bepaal of de vraag gaat over de boekhoudplicht zelf, de jaarrekening, een waardering, openbaarmaking of een toezichtskwestie.

**Waarom?** Verschillende vragen vallen onder verschillende bronnen — WER versus WVV versus KB-WVV.

**📥 Input**:
- Cliëntdossier of examenvraag → **Onderwerp van de vraag** _(document)_

**📤 Output**:
- Werknotitie → **Categorie van de vraag (boekhoudplicht / jaarrekening / waardering / openbaarmaking / toezicht)** _(conclusie)_

**🛠️ Hoe**:

1. Lees de vraag bij Meubelzaak Mertens BV: gaat het over hoe de boekhouding gevoerd wordt of over de jaarrekening?
2. Plaats de vraag in één van vijf rubrieken volgens [[belgisch-boekhoudrecht]] §domeinen: boekhoudplicht, jaarrekening, waardering, openbaarmaking, toezicht.
3. Bij overlap (bv. een waarderingsregel die ook de jaarrekening raakt): noteer beide categorieën — dat kan tot meerdere bronnen leiden.


**Grondslag**: [[belgisch-boekhoudrecht]] §domeinen

### 2. Pas de bronhiërarchie toe

Loop de hiërarchie van rechtsbronnen door van hoog naar laag tot de vraag beantwoord is.

**Waarom?** Hogere bronnen primeren op lagere — beginnen bij EU of WER bespaart fouten.

**📥 Input**:
- Werknotitie stap 1 → **Categorie van de vraag** _(conclusie)_

**📤 Output**:
- Bronlijst voor de vraag → **Hiërarchisch geordende lijst van toepasselijke bronnen** _(document)_

**🛠️ Hoe**:

1. Begin bovenaan met [[europees-boekhoudrecht]] (Richtlijn 2013/34/EU, IFRS-Verordening voor genoteerde groepen). Vraag: legt EU rechtstreeks iets op?
2. Daal af naar wet-niveau: voor boekhoudplicht en bewaren → [[wetboek-economisch-recht-boek-iii]] art. III.82-III.95. Voor jaarrekening + vennootschapsstructuur → [[wetboek-vennootschappen-verenigingen]] Boek 3.
3. Daal af naar het uitvoerings-KB: [[kb-wvv-uitvoering]] regelt MAR, schema's, waarderingsregels.
4. Stop zodra de vraag rechtstreeks beantwoord is — noteer artikel-referenties.


> [!example]- Voorbeeld: Sofie Janssens krijgt van Meubelzaak Mertens BV de vraag: 'moet onze BV verkort of volledig schema gebruiken?'
> Sofie Janssens krijgt van Meubelzaak Mertens BV de vraag: 'moet onze BV verkort of volledig schema gebruiken?'
>
> 1. **Categorie** 💬
>
>    Vraag over jaarrekening-presentatie → categorie 'jaarrekening'.
>    
>
> 2. **Toepasselijke bronnen** 💬
>
>    | Niveau | Bron | Artikel | Relevant? |
>    |---|---|---|---|
>    | EU | Richtlijn 2013/34/EU | art. 14, 16 | Indirect (geïmplementeerd in WVV) |
>    | Wet | WVV | art. 3:5 en 3:6, art. 1:24 | Ja — kernregel |
>    | KB | KB-WVV | bijlagen 1-3 | Ja — bevat de schema's zelf |
>    | Advies | CBN | 2022/03 | Aanvullend voor grenstoetsing |
>    
>

**Grondslag**: [[belgisch-boekhoudrecht]] §hiërarchie

### 3. Raadpleeg CBN-adviezen en rechtspraak voor interpretatie

Zoek aanvullende CBN-adviezen of rechtspraak als de wettekst meerduidig is.

**Waarom?** Adviezen en rechtspraak verduidelijken hoe een open norm in de praktijk wordt toegepast — niet bindend, wel gezaghebbend.

**📥 Input**:
- Bronlijst stap 2 → **Wettekst-passages** _(document)_

**📤 Output**:
- Interpretatienota → **Toepassingscriteria + grondslag** _(document)_

**🛠️ Hoe**:

1. Is de wettekst eenduidig? Stop hier.
2. Open de CBN-adviezenbank en zoek op het sleutelwoord (bv. 'groottecriteria'). Zie [[cbn-adviezen]] §gezag.
3. Plaats het advies in zijn context: een advies legt uit hoe het wettelijke begrip in een concrete situatie wordt ingevuld. Niet-bindend maar gezaghebbend.
4. Heeft een hof van beroep of het Hof van Cassatie zich uitgesproken? Raadpleeg [[rechtspraak-boekhoudrecht]] §gezag-rechtspraak.
5. Documenteer in het dossier: wet → advies → eventueel rechtspraak.


**Grondslag**: [[cbn-adviezen]] §toepassing, [[rechtspraak-boekhoudrecht]] §gezag

> [!warning]- Beschouw een CBN-advies nooit als bindend recht — vermeld het altijd als aanvullende doctrine.
>
> _Vaak fout gedaan_: Een CBN-advies citeren als ware het een wetsartikel.
>
> _Grondslag_: [[cbn-adviezen]] §gezag

### 4. Formuleer het antwoord met grondslag-vermelding

Schrijf het cliëntantwoord en vermeld voor elke claim de exacte bron.

**Waarom?** Zonder traceerbare grondslag is het advies niet verdedigbaar — kernregel voor de stagiair.

**📥 Input**:
- Bronlijst + interpretatienota → **Wetsartikelen + advies-nummers** _(document)_

**📤 Output**:
- Cliëntnota → **Antwoord + grondslagen** _(document)_

**🛠️ Hoe**:

1. Schrijf één conclusiezin per vraag.
2. Voeg per claim de bronnen toe in volgorde: wet (WER/WVV-art.) → KB-artikel → CBN-advies → rechtspraak.
3. Vermeld het type bron expliciet ('bindend', 'doctrinair', 'rechtspraak hof X').


**Grondslag**: [[belgisch-boekhoudrecht]] §grondslag-vermelding (praktijk-discipline)


