---
title: Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem
tags:
- competentie
- po-1-7
programmaonderdelen:
- '1.7'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/uitvoeren-risicoanalyse-organisatie.yaml
gegenereerd_op: '2026-05-17'
---
# Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem

**⚖️ 15% · 🤖 85%**

> Geen Belgische wet schrijft een specifieke risicoanalyse-methode voor (uitgezonderd sectorale verplichtingen zoals NIS-2 cyberrisico en AVG art. 35 DPIA). De methodologie volgt uit internationale vakdoctrine (COSO ERM 2017, ISO 31000:2018, ITAA-norm-kmo-controlenorm §96). Voor organisaties van openbaar belang verplicht WVV een risico-rapport door bestuursorgaan.

## Aanbevolen werkwijze

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

> [!example]- Praktijk Persenaire (eenmanszaak vrij beroep, 1 medewerker) vraagt: 'risicoanalyse hoort toch alleen bij grote bedrijven…
> **Conclusie**: Ook bij eenmanszaak nuttig — proportioneel. Maak één A4 met drie kolommen: top-5 risico's (bv. cliëntfraude, AVG-lek, ziekte zaakvoerder, fiscale boete door late aangifte, banksaldofout) + kans/impact-inschatting + één compensatie-actie per risico. Externe accountant doet jaarlijkse check.
>
> **Grondslag**: [[risico-inschatting-organisatie]] §proportionaliteit
>
> **Redenering**: Aanvalsvlak is kleiner maar concentratiegevoel hoger (één persoon = single point of failure). Minimale gestructureerde aanpak vermindert blinde vlekken.

> [!example]- Bij Rotex Roeselare NV ontdekt Sofie Janssens (commissaris) dat het risico-register geen cyberrisico's bevat hoewel er e…
> **Conclusie**: Communiceer als 'significant deficiency' aan het auditcomité ([[communicatie-met-management-governance]]). Het management moet een DPIA-achtige cyberrisico-analyse opzetten met aandacht voor de SAP-migratie. Voor de audit zelf: verhoog het ingeschatte controle-risico (CR) voor IT-afhankelijke beweringen.
>
> **Grondslag**: [[cyberrisico-ic]] §typologie, [[communicatie-met-management-governance]] §deficiency
>
> **Redenering**: Significante ICT-verandering zonder bijhorende risicoanalyse is een design-gebrek in component 2 (risk assessment). ISA 315 vereist auditrespons.


## Gebaseerd op concepten

[[risico-inschatting-organisatie]] · [[coso-ii-erm-framework]] · [[iso-31000-risicobeheer]] · [[fouten-en-fraude]] · [[fraude]] · [[fouten-ic]] · [[cyberrisico-ic]]
## Voortkomend uit

- **Taken**: 1.7.taak.1
- **Kenniselementen**: 1.7.III.B, 1.7.XII.E, 1.7.XII.F, 1.7.VI, 1.7.VI.A, 1.7.VI.B, 1.7.VIII.E
