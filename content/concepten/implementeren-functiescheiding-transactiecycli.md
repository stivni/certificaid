---
title: Implementeren van functiescheiding op kritieke transactiecycli
tags:
- concept
- competentie
- po-1-7
linked_anchors:
- 1.7.taak.1
- 1.7.VII
- 1.7.VIII.B
- 1.7.IX
- 1.7.IX.A
- 1.7.IX.C
- 1.7.IX.D
- 1.7.X.C
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/implementeren-functiescheiding-transactiecycli.json
gegenereerd_op: '2026-05-18'
---
# Implementeren van functiescheiding op kritieke transactiecycli 🤖

Deze competentie vertaalt het abstracte vier-functies-principe naar een concrete inrichting van transactiecycli (aankoop, verkoop, kas/bank, loon, voorraad). De stagiair moet per cyclus de functietoewijzingsmatrix kunnen opstellen, SOD-conflicten kunnen detecteren, compenserende controles kunnen ontwerpen en ERP-rolprofielen kunnen valideren. Examen-vragen testen vaak een KMO-context waarin volledige scheiding niet haalbaar is.


## Stappen

### 1. Vier kritische functies identificeren per cyclus

Map per kritische transactiecyclus de vier functies — autoriseren, uitvoeren, bewaren, registreren — op concrete personen en systemen.

**Waarom?** Functiescheiding is geen abstract principe maar een concrete toewijzing: wie tekent de aankooporder, wie ontvangt de goederen, wie betaalt, wie boekt?

**📥 Input**:
- Procesflowcharts per cyclus uit IC-handboek → **Activiteiten + actoren** _(document)_
- Organogram + ERP-rolprofielen → **Toegangsrechten en mandaatlimieten** _(document)_

**📤 Output**:
- Functietoewijzingsmatrix per cyclus → **Per activiteit: autorisatie / uitvoering / bewaring / registratie + naam persoon + ERP-rol** _(document)_

**🛠️ Hoe**:

1. Volg [[functiescheiding]] §vier-functies: autoriseren (mag de transactie?), uitvoeren (doe de handeling), bewaren (bewaar het activum), registreren (boek het in).
2. Werk cyclus per cyclus volgens [[cyclus-analyse-ic]]: aankoop, verkoop, kas/bank, loon, voorraad, productie.
3. Voor elke transactiestap noteer wie autoriseert (bv. CFO bij betaling > € 5.000), wie uitvoert (boekhouder bij invoer in ERP), wie bewaart (magazijnier voor goederen), wie registreert (boekhouder voor boeking).
4. Vergelijk met [[taakverdeling-ic]] §verantwoordelijkheidsmatrix om generieke template-rollen te koppelen.


**Grondslag**: [[functiescheiding]] §vier-functies, [[taakverdeling-ic]] §matrix

### 2. Incompatibele combinaties detecteren en oplossen

Scan de functietoewijzingsmatrix op verboden combinaties (kasontvangst + bankboeking; voorraadbeheer + voorraadtelling; HR-aanmelding + loonbetaling; goederontvangst + factuurgoedkeuring).

**Waarom?** Een verboden combinatie geeft één persoon de macht om een fictieve transactie te creëren én de boekhoudkundige sporen te wissen.

**📥 Input**:
- Functietoewijzingsmatrix stap 1 → **Per activiteit toegewezen personen** _(document)_

**📤 Output**:
- Lijst van geïdentificeerde SOD-conflicten + remediation-plan → **Per conflict: bron, risico, voorgestelde oplossing** _(document)_

**🛠️ Hoe**:

1. Test alle combinaties tegen [[functiescheiding]] §incompatibele-combinaties — minstens vier paren.
2. Voor elk conflict: kies één van drie oplossingen.
   a. Splits taken op (extra persoon).
   b. Voer compenserende controle in (review door bovenliggende laag).
   c. Roteer taken periodiek tussen meerdere medewerkers.
3. In een IT-omgeving: gebruik SOD-rapporten uit ERP (bv. SAP GRC, Microsoft Dynamics) om systeemrollen te toetsen — zie [[geinformatiseerde-omgeving-ic]] §IT-controls.
4. Documenteer aanvaarde residuele conflicten met expliciete management-handtekening en compensaties.


**Grondslag**: [[functiescheiding]] §incompatibele-combinaties, [[geinformatiseerde-omgeving-ic]] §SOD

> [!warning]- Test SOD-conflicten zowel op personen (mens) als op ERP-rollen (systeem) — twee aparte testen.
>
> _Vaak fout gedaan_: Enkel personeels-niveau toetsen terwijl één persoon vier ERP-rollen heeft — systeem-niveau SOD-conflict wordt gemist.
>
> _Grondslag_: [[geinformatiseerde-omgeving-ic]] §toegangsbeheer

### 3. Compenserende controles ontwerpen voor KMO-context

Bij beperkt personeel: ontwerp compenserende controles (review zaakvoerder, externe boekhouder, periodieke spot-checks) die het residuele SOD-risico tot acceptabel niveau brengen.

**Waarom?** Geen scheiding zonder compensatie = open deur voor fouten en fraude. ITAA-norm-kmo-controlenorm §96 erkent deze KMO-realiteit expliciet.

**📥 Input**:
- Lijst residuele SOD-conflicten → **Onoplosbare splits-conflicten** _(document)_

**📤 Output**:
- Compensatie-matrix → **Per conflict: compenserende control, frequentie, evidence** _(document)_

**🛠️ Hoe**:

1. Volg [[functiescheiding]] §KMO-uitdaging: zaakvoerderbetrokkenheid + externe revisie als typische compensaties.
2. Concrete compensaties: zaakvoerder reviewt maandelijks bankafschriften; externe accountant doet kwartaal-kasreconciliatie; jaarlijkse voorraadtelling door iemand buiten magazijn.
3. Voor elke compensatie definieer evidence (paraaf, screenshot, werkpapier) en bewaringstermijn (typisch 5-7 jaar in lijn met boekhoudkundige bewaarplicht).
4. Verkleinde KMO's met één werknemer: focus op externe controle (accountant) en automatisering (ERP met built-in checks).


> [!example]- Voorbeeld: Meubelzaak Mertens BV (8 werknemers): één boekhoudster doet kasontvangsten + bankreconciliatie + boekhouding
> Meubelzaak Mertens BV (8 werknemers): één boekhoudster doet kasontvangsten + bankreconciliatie + boekhouding. De externe accountant wil dit opvolgen.
>
> 1. **Geïdentificeerde SOD-conflict** 💬
>
>    Boekhoudster heeft alle vier functies voor kascyclus.
>    Inherent risico: verduistering door fictieve cash-uitgaves of niet-geboekte ontvangsten.
>    
>
> 2. **Compenserende controle** 💬
>
>    - Zaakvoerder Pieter Vermeulen tekent wekelijks bankuittreksels.
>    - Externe accountant Sofie Janssens doet maandelijkse kasreconciliatie via verrassings-controle.
>    - Camera in kasruimte (dissuasief).
>    - Kassasaldo nooit > € 1.000 (limiet via beleid).
>    
>
> 3. **Evidence** 💬
>
>    Bankuittreksels met paraaf zaakvoerder gearchiveerd; werkpapier kasreconciliatie door accountant (datum + paraaf); cameralogs 30 dagen bewaard.
>    
>

**Grondslag**: [[functiescheiding]] §KMO-uitdaging, ITAA-norm-kmo-controlenorm §96

### 4. ERP- en IT-toegangsrechten configureren conform functietoewijzing

Vertaal de functiematrix naar ERP-rolprofielen en IT-toegangsrechten. Zorg dat het systeem zelf SOD-violations technisch verhindert.

**Waarom?** Papieren matrix zonder systeemafdwinging blijft kwetsbaar — IT-control beveiligt structureel.

**📥 Input**:
- Functiematrix + compensatiematrix → **Definitieve toegangswensen** _(document)_

**📤 Output**:
- ERP-rolconfiguratie + toegangsrechten-overzicht → **Profiel per gebruiker met SOD-check** _(document)_

**🛠️ Hoe**:

1. Definieer rolprofielen in ERP zodat geen enkel profiel twee incompatibele transactietypes kan uitvoeren (zie [[geinformatiseerde-omgeving-ic]] §applicatie-controls).
2. Implementeer maker-checker workflows: invoer door A, goedkeuring door B vóór boeking definitief is.
3. Configureer betaallimieten in banking software: > € 5.000 vereist tweede goedkeuring; > € 25.000 vereist zaakvoerder.
4. Voer minstens jaarlijks een toegangsreview uit: matchen huidige rechten nog met huidige functies van personen? Gebruikers die uit dienst zijn → onmiddellijk deactiveren.


**Grondslag**: [[geinformatiseerde-omgeving-ic]] §toegangsbeheer, [[functiescheiding]] §IT-implementatie

> [!warning]- Plan een formele jaarlijkse access-recertification — bv. elke proceseigenaar tekent af op de actuele toegangslijst.
>
> _Vaak fout gedaan_: Toegangsrechten cumuleren bij interne mobiliteit (functie B krijgt rechten erbij maar A blijft) — leidt tot SOD-conflicten.
>
> _Grondslag_: [[geinformatiseerde-omgeving-ic]] §periodieke-review


## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

## Voorbeelden




## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3_part5`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
