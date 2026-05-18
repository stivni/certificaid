---
title: Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem
tags:
- concept
- competentie
- po-1-7
linked_anchors:
- 1.7.taak.1
- 1.7.III.B
- 1.7.XII.E
- 1.7.XII.F
- 1.7.VI
- 1.7.VI.A
- 1.7.VI.B
- 1.7.VIII.E
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/uitvoeren-risicoanalyse-organisatie.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem 🤖

Deze competentie operationaliseert COSO-component 2 (risico-inschatting) als concrete stagiair-handeling: voer een gestructureerde risico-identificatie + analyse uit voor een organisatie, lever een risico-register af, en integreer het in het IC-systeem. Geen Belgische wet schrijft een specifieke methode voor (uitgezonderd sectorale: NIS-2 cyberrisico, AVG art. 35 DPIA). De methodologie volgt uit internationale doctrine: COSO ERM 2017, ISO 31000:2018, en ITAA-controlenorm §96. Examen-vraagstellingen toetsen typisch het gestructureerd doorlopen van identificatie → analyse → respons → monitoring.


## Stappen

### 1. Risico's identificeren per proces en risicocategorie

Identificeer per kritische bedrijfsproces en per risicocategorie (strategisch, operationeel, financieel, compliance, cyber) potentiële gebeurtenissen die de doelstellingen kunnen frustreren.

**Waarom?** Wat niet geïdentificeerd is, kan niet beheerst worden. Identificatie vooraf is goedkoper dan een crisis achteraf.

**📥 Input**:
- Procesinventaris (uit IC-handboek) → **Kritische processen per cyclus** _(document)_
- Workshop-output bestuur en proceseigenaren → **Brainstorm-output per categorie** _(document)_

**📤 Output**:
- Risico-register versie 1 → **Risico-ID, beschrijving, proces, categorie, eigenaar** _(document)_

**🛠️ Hoe**:

1. Volg [[risico-inschatting-organisatie]] §stappen-1: bottom-up via proceseigenaren én top-down via bestuursorgaan-perspectief.
2. Gebruik vier hoofdcategorieën (COSO ERM 2017): strategisch, operationeel, rapportering, compliance — voeg expliciet cyber/IT toe via [[cyberrisico-ic]] §typologie.
3. Inventariseer per proces zowel fout-risico ([[fouten-ic]]: oordeels-, uitvoerings-, datafouten) als fraude-risico ([[fraude]] §driehoek: druk, gelegenheid, rationalisatie).
4. Onderscheid inherente risico's (los van controles) van residuele risico's (na bestaande controles) — werk in deze stap met inherent niveau.


**Grondslag**: [[risico-inschatting-organisatie]] §identificatie, [[coso-ii-erm-framework]] §risicocategorieen, [[fraude]] §driehoek

> [!warning]- Bevraag zowel bestuur (strategische blik) als operationele medewerkers (daadwerkelijke gebeurtenissen) — niet één van beide.
>
> _Vaak fout gedaan_: Risico-workshop enkel met directie — operationele kennis ontbreekt en blinde vlekken blijven.
>
> _Grondslag_: [[risico-inschatting-organisatie]] §bottom-up-top-down

### 2. Risico's analyseren — kans × impact + risk-appetite

Schat per risico de waarschijnlijkheid en de impact in (kwalitatief of kwantitatief) en confronteer met de door het bestuur bepaalde risk-appetite.

**Waarom?** Zonder ranking is elk risico even belangrijk en raakt het IC-budget verspreid in niet-prioritaire controles.

**📥 Input**:
- Risico-register versie 1 → **Geïdentificeerde risico's** _(document)_
- Risk-appetite-verklaring bestuursorgaan → **Tolerantie per categorie (€-drempel of impact-klasse)** _(document)_

**📤 Output**:
- Risicomatrix → **Heatmap kans × impact met risk-appetite-grens** _(document)_

**🛠️ Hoe**:

1. Pas een 5×5 of 3×3 schaal toe (kans: zeer laag → zeer hoog; impact: insignificant → catastrofaal) volgens [[iso-31000-risicobeheer]] §analyseproces.
2. Bepaal voor financiële impact concrete €-drempels (bv. < € 25.000 = laag, € 25.000-€ 250.000 = middel, > € 250.000 = hoog) — gebruik cast-cijfers uit context.
3. Plot elk risico op een heatmap. Risico's boven de risk-appetite-lijn vereisen respons.
4. Onderscheid bruto- (zonder controles) en netto- (na bestaande controles) inschatting — visualiseer de "control gap".


**Grondslag**: [[risico-inschatting-organisatie]] §analyse, [[iso-31000-risicobeheer]] §kans-impact, [[coso-ii-erm-framework]] §risk-appetite

### 3. Risico-respons kiezen per risico

Bepaal per risico boven de appetite-lijn: vermijden, verminderen (controle toevoegen), delen (verzekering of outsourcing) of accepteren — en wijs een actiehouder toe.

**Waarom?** Een risicomatrix zonder respons-acties is een papier-oefening. De respons is het scharnier naar concrete controle-activiteiten.

**📥 Input**:
- Risicomatrix stap 2 → **Risico's boven appetite-grens** _(document)_

**📤 Output**:
- Actieplan risicoreductie → **Per risico: respons-type, actiehouder, deadline, kosten** _(document)_

**🛠️ Hoe**:

1. Pas de vier responsen toe uit [[risico-inschatting-organisatie]] §respons en [[iso-31000-risicobeheer]] §treatment.
2. Vermijden: stop met de risicovolle activiteit (bv. exotische valuta-handel).
3. Verminderen: introduceer of versterk een control — koppel aan een beheersactiviteit ([[beheersactiviteiten]]).
4. Delen: verzekering, hedging, of outsourcing aan gespecialiseerde partij.
5. Accepteren: documenteer expliciete bewuste keuze door bestuursorgaan (gemotiveerd).


**Grondslag**: [[risico-inschatting-organisatie]] §respons, [[iso-31000-risicobeheer]] §treatment

> [!warning]- Documenteer 'accepteren' altijd met expliciete bestuursbeslissing en motivering — anders is het verzuim, geen acceptatie.
>
> _Vaak fout gedaan_: Risico's stilzwijgend accepteren ('we doen er niets aan') — bij incident is er geen verdediging dat het bewust was.
>
> _Grondslag_: [[coso-ii-erm-framework]] §respons-types

### 4. Risico-register integreren in IC-systeem en jaarlijks updaten

Integreer het risico-register in het IC-handboek en plan een minimaal jaarlijkse update — én ad hoc bij significante veranderingen (nieuwe activiteit, regelwijziging, incident).

**Waarom?** Risico's evolueren. Cyber-, regelgevings- en bedrijfsrisico's veranderen sneller dan een jaarlijkse cyclus — monitoring is permanent.

**📥 Input**:
- Actieplan stap 3 → **Acties en deadlines** _(document)_

**📤 Output**:
- Risico-register versie 2 in IC-handboek → **Live document met versie-historiek** _(document)_

**🛠️ Hoe**:

1. Plan een vaste jaarlijkse risico-review (typisch bij budget- of strategie-cyclus) met bestuursorgaan + proceseigenaren.
2. Definieer triggers voor ad-hoc update: incident, nieuwe regelgeving (bv. NIS-2, AVG-aanpassing), nieuwe activiteit, M&A.
3. Rapporteer kwartaalstatus van actieplan-deadlines aan het auditcomité (indien aanwezig — [[auditcomite]]) of de zaakvoerder.
4. Zorg dat de externe auditor toegang krijgt tot het risico-register als input voor zijn eigen risico-inschatting ([[risico-inschatting-audit]]).


> [!example]- Voorbeeld: Yperse Werkplaats BV voert haar eerste structurele risicoanalyse uit met Marleen De Cock (interim Risk Officer aangeleve…
> Yperse Werkplaats BV voert haar eerste structurele risicoanalyse uit met Marleen De Cock (interim Risk Officer aangeleverd door Xenon Expertise BV). De workshop is 1 dag met bestuursorgaan + 5 proceseigenaren.
>
> 1. **Top-5 geïdentificeerde inherente risico's** 💬
>
>    1. Frauduleuze leveranciersfacturen (operationeel — kans midden, impact hoog: € 350.000/jaar potentieel)
>    2. Cyberaanval op ERP (cyber — kans midden, impact catastrofaal: > € 1.000.000)
>    3. Voorraadverspilling productie-restanten (operationeel — kans hoog, impact middel: € 80.000/jaar)
>    4. Verkeerde periodetoerekening omzet (rapportering — kans laag, impact middel)
>    5. AVG-inbreuk personeelsdata (compliance — kans laag, impact hoog: boete tot 4% omzet)
>    
>
> 2. **Risicomatrix-positionering** 💬
>
>    Boven appetite-grens (€ 100.000 of catastrofaal): risico 1, 2, 5.
>    Binnen appetite: risico 3, 4.
>    
>
> 3. **Gekozen respons** 💬
>
>    R1: verminderen (drie-weg-match + leverancierscredibiliteit)
>    R2: delen (cyberverzekering € 5M) + verminderen (back-up + MFA)
>    R3: accepteren (€ 80.000 binnen appetite, monitoring KPI)
>    R4: verminderen (cut-off-procedure einde maand)
>    R5: verminderen (AVG-register + DPIA — zie [[integreren-avg-compliance-in-ic]])
>    
>

**Grondslag**: [[risico-inschatting-organisatie]] §monitoring, [[coso-ii-erm-framework]] §continu, [[auditcomite]] §rapportering


## Voorbeelden




