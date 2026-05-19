---
title: Eenvoudige integratie (registratiesysteem)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.IV.C
- 1.8.IV
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/registratiesysteem-eenvoudige-integratie.json
gegenereerd_op: '2026-05-18'
---
# Eenvoudige integratie (registratiesysteem) 🤖

Bij eenvoudige integratie neemt elke deelnemer of elke onderneming in eigen boekhouding rechtstreeks zijn aandeel in de kosten en opbrengsten op — zonder aparte 'tussen-boekhouding'. In analytische context betekent het: kosten en opbrengsten worden meteen aan de kostendrager toegerekend zonder extra registratielaag.

> [!info] Behoort tot: [[rekeningenstelsel-analytisch]]


## Bouwstenen

### Werking ⚖️

CBN 3/3: 'De eenvoudige integratie van de kosten en opbrengsten bestaat erin dat de deelgenoot in zijn eigen resultatenrekening diens aandeel opneemt.' Geanalogiseerd naar analytische boekhouding: kostendrager of kostencentrum krijgt rechtstreeks zijn aandeel uit de algemene boekhouding, zonder tussen-rekeningen.

**Waarom?** Eenvoudig, weinig administratielast, transparant voor beperkte complexiteit.



Yperse Werkplaats BV met eenvoudige integratie: de aankoopfactuur wol € 22.500 wordt onmiddellijk geboekt op kostencentrum Spinnerij (rekening 9300). Geen aparte voorraadboekhouding van wol per centrum.

_Grondslag: CBN 3/3 (analoog gebruik)_


## Berekening

### Inrichting eenvoudige integratie (klasse 9)

*Stappenschema waarmee in het Belgische MAR (klasse 9 vrij in te vullen) een eenvoudige integratie wordt opgezet: elke kost of opbrengst gaat rechtstreeks via één spiegel-boeking van klasse 6/7 naar klasse 9, zonder tussen-verdeling.*

### 1. Definieer kostendragers en kostencentra

Lijst per productlijn, dienst, opdracht of klant op welke kostendragers de onderneming wil rapporteren. Identificeer ook de kostencentra (afdelingen) die als 'verzamelpunt' kunnen dienen.

**🛠️ Hoe**:

Beperk de granulariteit: één kostencentrum per productie-afdeling, één kostendrager per productgroep is meestal voldoende. Te fijne granulariteit verzwaart de administratie zonder bruikbare meerwaarde.

**Grondslag**: [[kostendrager]] · [[kostencentrum]]

### 2. Open klasse-9-rekeningen per kostencentrum/kostendrager

Maak in het MAR een rekening 9XXX per kostencentrum (bv. 9300 Confectie, 9400 Spinnerij) of per kostendrager. Eén niveau, geen sub-verdeling.

**🛠️ Hoe**:

Klasse 9 is vrij in te vullen onder KB 21.10.2018 (MAR). Conventie: 90 reflectierekeningen (tegenpost van klasse 6/7), 92-94 kostencentra, 95-96 kostendragers, 98 verschillen-rekeningen.

**Grondslag**: KB 21.10.2018 — MAR klasse 9

### 3. Boek elke kost in klasse 6 én via spiegel-boeking in klasse 9

Bij elke uitgavenboeking in klasse 6 (bv. 600 Aankopen, 620 Lonen) maak je gelijktijdig een spiegel-boeking in klasse 9: 9XXX (kostencentrum debet) / 90X (reflectierekening credit). Geen verdeling tussen meerdere centra.

**🛠️ Hoe**:

Concreet: aankoopfactuur wol € 22.500 → 600/440 in klasse 6, én 9400 Spinnerij / 9060 Reflectie aankopen in klasse 9. Eén kostencentrum krijgt de hele kost; geen pro-rata.

**Grondslag**: [[reflectie-rekening]]

### 4. Genereer per centrum/drager periodieke totalen

Aan einde maand/kwartaal: extraheer per kostencentrum-rekening (9XXX) het totaal verbruikte kosten. Dit is de directe input voor kostprijs-berekening per kostendrager.

**🛠️ Hoe**:

Rapportage rechtstreeks uit het grootboek per analytische rekening. Geen extra verdeelboekingen nodig — alle kosten staan al op de juiste plaats.

**Grondslag**: Vakdoctrine

### 5. Reconciliatie met algemene boekhouding

Aan einde periode: totaal klasse 9 (alle kostencentra-rekeningen) = totaal klasse 6 + 7 (via reflectierekeningen). Controle op waarderingsneutraliteit.

**🛠️ Hoe**:

Indien verschil: oorzaken zijn typisch vergeten spiegel-boekingen of een kostpost zonder kostencentrum-toewijzing. Werk weg vóór jaarrekening-afsluiting.

**Grondslag**: [[registratiesysteem-waarderingsneutraal]]


> [!info]- Niet verwarren met [[registratiesysteem-proportionele-integratie]]
> Eenvoudig: direct toewijzen aan kostencentrum/-drager zonder pro-rata. Proportioneel: kosten en opbrengsten worden rubriek per rubriek pro-rata verdeeld over meerdere centra of partners.
>
> _Trigger_: Examen-vraag: 'past de onderneming pro-rata toe?' → nee = eenvoudig, ja = proportioneel.


## Bronnen

[^1]: `CBN-0003-03-advies-inzake-de-boekhoudkundige-verwerking-van-verrichtingen-van-tijdelijk__sec_de-eenvoudige-integratie-van-kosten-en-opbrengsten`
[^2]: `CBN-0003-03-advies-inzake-de-boekhoudkundige-verwerking-van-verrichtingen-van-tijdelijk__sec_de-proportionele-integratie-van-kosten-en-opbrengsten`
