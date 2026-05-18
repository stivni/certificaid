---
title: Verwerven van kennis van de cliënt en zijn omgeving in een audit-opdracht
tags:
- concept
- competentie
- po-1-6
linked_anchors:
- 1.6.taak.1
- 1.6.II.A
- 1.6.II.B
programmaonderdelen:
- '1.6'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verwerven-kennis-van-clientonderneming-audit.json
gegenereerd_op: '2026-05-18'
---
# Verwerven van kennis van de cliënt en zijn omgeving in een audit-opdracht 🤖


## Stappen

### 1. Externe omgeving en sector in kaart brengen

Verzamel inzicht in de sector, het regelgevende kader en de macro-economische context waarbinnen de cliënt opereert.

**Waarom?** Sectorrisico's en wijzigingen in regelgeving zijn vaak hoofdoorzaken van inherente risico's bij belangrijke posten (omzet-erkenning, voorraadwaardering, voorzieningen).

**📥 Input**:
- Sectorrapporten (Graydon, NBB, brancheorganisaties) → **Trends, concurrentie, prijsdruk** _(document)_
- Toepasselijke regelgeving → **Sectorale wetten, vergunningen, milieuverplichtingen** _(document)_

**📤 Output**:
- Werkpapier 'externe omgeving' → **Sectorrisico's + impact op jaarrekening** _(document)_

**🛠️ Hoe**:

1. Identificeer de NACE-code en de sector van Rotex Roeselare NV (machinebouw).
2. Raadpleeg sectorrapporten en NBB-statistieken voor sectortrends — krimpende marges, voorraadrotatie, debiteurenrisico.
3. Identificeer specifieke regelgeving — bv. milieuvergunningen, CE-markering, BTW-regimes voor uitvoer.
4. Documenteer per externe factor de potentiële impact op jaarrekeningposten (volgens [[kennis-van-onderneming-omgeving]] §externe-factoren).


**Grondslag**: [[kennis-van-onderneming-omgeving]] §externe-factoren, ITAA KMO-controlenorm §54

### 2. Interne organisatie en strategie begrijpen

Verwerf kennis over de aandeelhoudersstructuur, het bestuur, de operationele inrichting, de financieringsstructuur en de boekhoudkundige principes.

**Waarom?** De interne werking bepaalt waar fouten en fraude waarschijnlijk worden — bv. eenmansbestuur zonder controles, complexe groepsstructuur, recente herstructurering.

**📥 Input**:
- Statuten, UBO-register, bestuurdersregister → **Aandeelhouders + bestuurders + verbonden partijen** _(document)_
- Boekhoudhandleiding + waarderingsregels → **Toegepaste regels per rubriek** _(document)_
- Interview met financieel directeur → **Strategie, financiering, recente gebeurtenissen** _(document)_

**📤 Output**:
- Permanent dossier sectie 'cliëntprofiel' → **Organogram + significante feiten + waarderingsregels** _(document)_

**🛠️ Hoe**:

1. Lees de statuten en het UBO-register; bouw een organogram met Aurelia Holding NV als 100 %-aandeelhouder van Rotex Roeselare NV indien van toepassing.
2. Interview de financieel directeur en operationeel verantwoordelijke; vraag naar recente acquisities, vestigingen, IT-migraties.
3. Identificeer verbonden partijen via [[verbonden-partijen-audit]] §opsporing — managementloon, leningen aan bestuurders, transacties met zustervennootschappen.
4. Documenteer per significant onderdeel de impact op jaarrekening-rubrieken.


**Grondslag**: [[kennis-van-onderneming-omgeving]] §interne-organisatie, ITAA KMO-controlenorm §56

> [!warning]- Verbonden partijen actief opsporen, ook als het management ze niet spontaan vermeldt.
>
> _Vaak fout gedaan_: Vertrouwen op de bestuurdersverklaring 'geen verbonden partijen' zonder cross-check via UBO en notulen.
>
> _Grondslag_: [[verbonden-partijen-audit]] §opsporing

### 3. Continuïteit beoordelen op niveau van kennisverwerving

Toets of er signalen zijn dat de continuïteitsveronderstelling van de jaarrekening niet gerechtvaardigd is.

**Waarom?** Indicaties van continuïteitsproblemen bepalen mee de scope van de audit en triggeren specifieke vermeldingen in het controleverslag.

**📥 Input**:
- Recente jaarrekeningen + tussentijdse cijfers → **Resultaat, eigen vermogen, werkkapitaal** _(boekhoudkundig-bedrag)_
- Lopende kredietlijnen + convenanten → **Beschikbare middelen + ratio-verplichtingen** _(document)_

**📤 Output**:
- Werkpapier 'continuïteitsindicatie' → **Risicocategorie geen / verhoogd / materieel onzeker** _(conclusie)_

**🛠️ Hoe**:

1. Bereken de evolutie van het eigen vermogen, werkkapitaal en netto bedrijfskapitaal over drie boekjaren.
2. Toets aan de signalen uit [[continuiteitsveronderstelling-audit]] §indicatoren — twee opeenvolgende verliesjaren, negatief eigen vermogen, opgezegde kredietlijnen.
3. Klasseer de continuïteit als 'geen verhoogd risico', 'verhoogd risico' of 'materiële onzekerheid' — dat bepaalt de stappen in [[opstellen-controleverslag-en-formuleren-oordeel]].


**Grondslag**: [[continuiteitsveronderstelling-audit]] §indicatoren, ITAA KMO-controlenorm §122

### 4. Boekhoudsysteem en interne beheersing op hoog niveau begrijpen

Beschrijf het boekhoud- en IT-systeem en de basisstructuur van de interne beheersing — voldoende voor risico-inschatting, geen volledige test.

**Waarom?** Pas met inzicht in het systeem kan je in [[uitvoeren-risico-inschatting-en-materialiteit-audit]] uitspraak doen over inherent + intern beheersingsrisico per bewering.

**📥 Input**:
- Boekhoudpakket-documentatie (Exact, BOB50, SAP, ...) → **Functionele scheidingen, audit-trail** _(document)_
- Procedure-flowcharts per cyclus (inkoop, verkoop, personeel, voorraad) → **Wie boekt, wie keurt goed, wie betaalt** _(document)_

**📤 Output**:
- Werkpapier 'systeembeschrijving + IC-flow' → **Per cyclus: belangrijkste controlepunten** _(document)_

**🛠️ Hoe**:

1. Vraag een rondgang bij de boekhoudafdeling van Rotex Roeselare NV — interview de hoofdboekhouder over de cyclus 'inkoop tot betaling'.
2. Documenteer per cyclus: triggers, sleutelcontroles, scheiding van functies — op het niveau van een narrative of een eenvoudig flowchart.
3. Toets oppervlakkig (walkthrough): volg één transactie van order tot betaling om te bevestigen dat het beschreven systeem effectief werkt.
4. Markeer reeds in deze fase de cycli waar IC zwak of afwezig blijkt — die krijgen voorrang in [[uitvoeren-risico-inschatting-en-materialiteit-audit]] §interne-beheersingsrisico.


**Grondslag**: [[kennis-van-onderneming-omgeving]] §boekhoudsysteem, ITAA KMO-controlenorm §60


> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

