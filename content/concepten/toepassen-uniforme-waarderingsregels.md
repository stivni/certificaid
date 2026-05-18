---
title: Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige
  cijfers
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.D
- 1.4.I.B
- 1.4.I.G
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/toepassen-uniforme-waarderingsregels.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers 🤖

Een toepassingscompetentie binnen het Belgische boekhoudrecht-consolidatieregime (KB WVV Boek 3, Titel 2). De stagiair identificeert waarderingsverschillen tussen groepsleden en brengt de enkelvoudige cijfers in lijn met de groeps-waarderingsregels vóór ze de eliminaties en aggregaties uitvoert.


## Stappen

### 1. Inventariseren van de waarderingsregels

Maak een matrix van de waarderingsregels per balanspost over alle vennootschappen in de kring.

**Waarom?** Verschillen moeten zichtbaar worden voordat ze geüniformeerd kunnen worden.

**📥 Input**:
- Toelichting bij enkelvoudige jaarrekeningen van Aurelia en dochters → **Beschrijving waarderingsregels** _(document)_

**📤 Output**:
- Vergelijkingsmatrix waarderingsregels → **Per balanspost: regel per vennootschap** _(document)_

**🛠️ Hoe**:

1. Open de toelichting bij de enkelvoudige jaarrekening van Aurelia Holding NV en lees de hoofdrubriek 'Waarderingsregels'.
2. Doe hetzelfde voor elke dochter in de kring (Brugse Brouwerij BV, Holsters Horst BV, ...).
3. Maak een tabel met als kolommen: balanspost, regel Aurelia, regel Brugse, regel Holsters, ... Vul in voor elke materiële balanspost (afschrijvingen, voorraadwaardering, voorzieningen).
4. Markeer in de tabel waar de regels van een dochter afwijken van die van Aurelia.


**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §inventarisatie (praktijk)

### 2. Toetsen aan de waarderingsregels van de consoliderende vennootschap

Vergelijk de regels van elke dochter met de regels van de consoliderende vennootschap.

**Waarom?** KB WVV art. 3:116 lid 1 vereist dat de geconsolideerde jaarrekening dezelfde waarderingsregels hanteert als de enkelvoudige jaarrekening van de moeder.

**📥 Input**:
- Vergelijkingsmatrix uit stap 1 → **Per balanspost de regels per vennootschap** _(document)_

**📤 Output**:
- Lijst afwijkende dochters → **Per dochter: welke regels afwijken** _(document)_

**🛠️ Hoe**:

1. Stel de waarderingsregels van Aurelia Holding NV vast als referentie.
2. Voor elke dochter: lijst per balanspost op waar de regel afwijkt.
3. Bv. Holsters Horst BV waardeert voorraad op LIFO, Aurelia op FIFO → afwijking voor de balanspost 'Voorraden'.
4. Documenteer per afwijking: aard, vermoedelijke impact op de balanspost, dochter waar de afwijking voorkomt.


**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §verplichting, KB WVV art. 3:116 lid 1

### 3. Doorvoeren van aanpassingsboekingen voor afwijkende dochters

Boek consolidatieboekingen die de cijfers van de dochter omzetten naar de uniforme regels.

**Waarom?** Zonder herwaardering zou de geconsolideerde jaarrekening inconsistent zijn en geen getrouw beeld geven.

**📥 Input**:
- Lijst afwijkende dochters uit stap 2 → **Afwijkingen + financiële impact** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Consolidatiedossier → **Aanpassingsboekingen per dochter** _(boekingsregel)_

**🛠️ Hoe**:

1. Voor elke afwijking: bereken het bedrag waarmee de balanspost moet worden aangepast.
2. Bv. Holsters Horst BV waardeert voorraad LIFO op 100. Bij toepassing FIFO (regel Aurelia) zou de voorraad 130 zijn → aanpassing van +30.
3. Boek de aanpassing in het consolidatiedossier (NIET in de enkelvoudige jaarrekening van de dochter): debet Voorraden +30, credit Reserves +30 (of resultaat boekjaar, naargelang aard).
4. Documenteer per aanpassing: oude waardering, nieuwe waardering, bedrag, motivering en grondslag (KB WVV art. 3:116).


> [!example]- Voorbeeld: Holsters Horst BV (dochter van Aurelia Holding NV) waardeert voorraad volgens LIFO
> Holsters Horst BV (dochter van Aurelia Holding NV) waardeert voorraad volgens LIFO. Aurelia past FIFO toe. Op balansdatum: voorraadwaarde LIFO bij Holsters = 100; voorraadwaarde FIFO zou = 130.
>
> 1. **Berekening aanpassing** 🧮
>
>    aanpassing voorraad = waarde FIFO − waarde LIFO
>                        = 130 − 100
>                        = **+30**
>    
>
> 2. **Boeking in consolidatiedossier** 📝
>
>    Debiteer: Voorraden (Holsters)               30
>    Crediteer: Geconsolideerde reserves          30
>    → Voorraad bij Holsters in geconsolideerde balans = 130 i.p.v. 100.
>    
>

**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §aanpassingsboeking, KB WVV art. 3:116

> [!warning]- De waarderingsregels van de consoliderende vennootschap gelden op consolidatieniveau, ook voor buitenlandse dochters.
>
> _Vaak fout gedaan_: Aannemen dat een dochter haar eigen waarderingsregels mag behouden zolang die wettelijk zijn in haar land van vestiging.
>
> _Grondslag_: [[uniforme-waarderingsregels-consolidatie]] §buitenlandse-dochters

### 4. Beoordelen van afwijkingen in uitzonderingsgevallen

Beoordeel of een afwijking van de standaardwaarderingsregels strookt met het wettelijk kader.

**Waarom?** KB WVV staat afwijkingen toe mits gemotiveerd en wettelijk verdedigbaar. Ontbrekende motivering schendt de plicht.

**📥 Input**:
- Afwijkingsvoorstellen → **Aard + motivering** _(document)_

**📤 Output**:
- Toelichting bij geconsolideerde jaarrekening → **Motivering per afwijking + grondslag** _(document)_

**🛠️ Hoe**:

1. Open elk voorstel tot afwijking van de standaardwaarderingsregels (uitzondering KB WVV art. 3:116 lid 2).
2. Toets aan twee voorwaarden: (a) is de afwijking verdedigbaar volgens Titel 1 KB WVV en het hoofdstuk Geconsolideerde jaarrekening? (b) is een motivering opgesteld?
3. Beide ja → neem de motivering op in de toelichting. Onthoud: lezer moet uit motivering kunnen afleiden waarom de afwijking nodig was.
4. Een van beide nee → wijs de afwijking af; pas de standaardwaarderingsregels alsnog toe.


**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §uitzonderingen, KB WVV art. 3:116 lid 2

### 5. Hercorrigeren van fiscale distorsies

Draai economisch niet-verantwoorde fiscaal-gedreven afschrijvingen of waardeverminderingen terug op consolidatieniveau.

**Waarom?** Het getrouw beeld vraagt economisch verantwoorde waardering; fiscale distorsies horen niet in de geconsolideerde jaarrekening.

**📥 Input**:
- Jaarrekeningen dochters → **Fiscaal-gedreven boekingen op gebouwen, voorzieningen, passiva** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Consolidatiedossier → **Hercorrectie-boekingen** _(boekingsregel)_

**🛠️ Hoe**:

1. Identificeer per dochter waar fiscaal-gedreven boekingen voorkomen die economisch niet verantwoord zijn. Vaak: versnelde afschrijvingen, eenmalige waardeverminderingen, voorzieningen behouden enkel om fiscaal voordeel.
2. Bv. Holsters Horst BV heeft 200 versnelde afschrijving op een gebouw geboekt; economisch verantwoorde afschrijving zou 50 zijn → 150 hercorrigeren.
3. Boek in het consolidatiedossier: debet gebouw +150, credit Geconsolideerde reserves +150.
4. Motiveer in de toelichting waarom de hercorrectie is doorgevoerd (KB WVV art. 3:118).


**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §fiscale-distorsies, KB WVV art. 3:118

### 6. Waarborgen van stelselmatigheid in de tijd

Verifieer dat de waarderingsregels identiek zijn aan die van het vorige geconsolideerde boekjaar, of motiveer een wijziging.

**Waarom?** Stelselmatigheid is een wettelijke vereiste. Wijzigingen vereisen motivering én aanpassing van de vergelijkbaarheid.

**📥 Input**:
- Geconsolideerde jaarrekening vorig boekjaar → **Waarderingsregels** _(document)_
- Geconsolideerde jaarrekening huidig boekjaar → **Waarderingsregels** _(document)_

**📤 Output**:
- Toelichting bij geconsolideerde jaarrekening → **Bevestiging stelselmatigheid OF motivering wijziging + retroactieve correctie** _(document)_

**🛠️ Hoe**:

1. Vergelijk de waarderingsregels van het huidige boekjaar met die van het vorige geconsolideerde boekjaar.
2. Identiek? → bevestig in toelichting.
3. Wijziging? → motiveer aan de hand van KB WVV art. 3:117 (belangrijke wijziging in bedrijf, vermogensstructuur, economische of technologische omstandigheden).
4. Bij wijziging: corrigeer de vergelijkende cijfers van het vorige boekjaar retroactief, zodat ze met de nieuwe regels berekend zijn.
5. Documenteer impact op de vergelijkbare cijfers in de toelichting.


**Grondslag**: [[uniforme-waarderingsregels-consolidatie]] §stelselmatigheid, KB WVV art. 3:117


## Voorbeelden



