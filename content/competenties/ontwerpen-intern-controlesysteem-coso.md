---
title: Ontwerpen van een intern-controlesysteem volgens de vijf COSO-componenten
tags:
- competentie
- po-1-7
programmaonderdelen:
- '1.7'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/ontwerpen-intern-controlesysteem-coso.yaml
gegenereerd_op: '2026-05-17'
---
# Ontwerpen van een intern-controlesysteem volgens de vijf COSO-componenten

**⚖️ 25% · 🤖 75%**

> Voor de Belgische KMO is er geen wettelijke verplichting tot opzet van een COSO-conform IC-systeem; ITAA-norm-kmo-controlenorm §96-§98 omschrijft het IC-begrip en de audit-toetsing ervan. WVV en Corporate Governance Code 2020 leggen wel verplichtingen op aan grote NV's en organisaties van openbaar belang. Het concrete ontwerp (proceslandschap, controle-activiteiten, dashboards) is overwegend praktijkmatig — COSO 2013 levert het internationale kader.

## Aanbevolen werkwijze

### 1. Vaststellen van doelstellingen en scope

Leg per organisatorische eenheid de doelstellingen vast in de drie COSO-categorieën: operationeel, financiële rapportering en compliance. Bepaal welke processen in scope vallen.

**Waarom?** Zonder expliciete doelstellingen is elke controle een controle 'voor de controle'. COSO eist dat doelstellingen vooraf bepaald zijn — anders kan men niet meten of het systeem werkt.

**📥 Input**:
- Strategisch plan + organogram Yperse Werkplaats BV → **Doelstellingen op groeps- en afdelingsniveau** _(document)_
- Risico-appetijt-verklaring bestuursorgaan → **Tolerantie per risicotype** _(document)_

**📤 Output**:
- Werkdocument 'IC-scope en doelstellingen' → **Drie kolommen (Operations / Reporting / Compliance) met meetbare doelen per proces** _(document)_

**🛠️ Hoe**:

1. Volg de drie doelstellingencategorieën uit [[interne-controle]] §drie-doelstellingen en [[coso-i-framework]] §kubus.
2. Vraag aan Pieter Vermeulen (zaakvoerder) welke processen kritisch zijn (typisch aankoop, productie, verkoop, loon, kas).
3. Schrijf per proces minstens één meetbare doelstelling per categorie: bv. "facturen worden binnen 5 werkdagen geboekt" (Operations), "omzet wordt periodecorrect erkend" (Reporting), "btw-aangifte tijdig en correct" (Compliance).
4. Laat het bestuursorgaan deze scopelijst goedkeuren — vergeet ook subdoelstellingen voor de IT-omgeving niet ([[geinformatiseerde-omgeving-ic]]).


**Grondslag**: [[coso-i-framework]] §kubus, [[interne-controle]] §drie-doelstellingen, ITAA-norm-kmo-controlenorm Bijlage 1

> [!warning]- Maak doelstellingen meetbaar en koppel ze aan één van de drie COSO-categorieën — anders mist het systeem zijn referentiepunt.
>
> _Vaak fout gedaan_: Doelstellingen formuleren als 'goed werken' of 'fouten vermijden' — niet toetsbaar, niet bruikbaar voor monitoring.
>
> _Grondslag_: [[interne-controle]] §drie-doelstellingen

### 2. Componenten 1 en 2 inrichten — controle-omgeving en risico-inschatting

Bouw de tone-at-the-top (gedragscode, integriteitsverklaring, organisatiestructuur) en leg een risico-register aan dat per proces inherente risico's en beheersingsdoelen koppelt.

**Waarom?** Componenten 1 en 2 zijn fundamenteel: zonder cultuur en zonder zicht op risico's kunnen controle-activiteiten (component 3) nooit gericht zijn.

**📥 Input**:
- Bestaande gedragscode + HR-richtlijnen → **Integriteit, klokkenluiderkanalen, anti-fraude-beleid** _(document)_
- Resultaten risicoanalyse (zie [[uitvoeren-risicoanalyse-organisatie]]) → **Risico-register met kans × impact** _(conclusie)_

**📤 Output**:
- Controle-omgeving-charter + risico-register → **Cultuurdocument + risicomatrix per proces** _(document)_

**🛠️ Hoe**:

1. Stel een gedragscode op die de drie pijlers van [[controle-omgeving]] dekt: integriteit en ethische waarden, governance-toezicht (raad van bestuur / auditcomité), competentie-eisen en accountability-structuur.
2. Bevestig de organisatiestructuur in een organogram met rapporteringslijnen en delegatieniveaus — wie tekent welk bedrag, wie keurt welk contract goed.
3. Voer een risico-inschatting uit volgens [[risico-inschatting-organisatie]] §stappen (identificatie, analyse kans × impact, respons) en documenteer per geïdentificeerd risico de gewenste IC-respons.
4. Knoop COSO 17 principes (zie [[coso-i-framework]] §principes) aan elk onderdeel — gebruik de 5 principes voor controle-omgeving (integriteit, governance, structuur, competentie, accountability).


**Grondslag**: [[controle-omgeving]] §definitie, [[risico-inschatting-organisatie]] §stappen, [[coso-i-framework]] §principes

### 3. Component 3 — beheersactiviteiten ontwerpen per kritische cyclus

Werk per transactiecyclus (aankoop, verkoop, kas, loon, voorraad, productie) een set van preventieve én detectieve beheersactiviteiten uit, met expliciete functiescheiding en autorisatie-niveaus.

**Waarom?** Beheersactiviteiten zijn waar IC 'tast en grijpt' — zonder concrete procedures blijft COSO theorie.

**📥 Input**:
- Procesbeschrijvingen per cyclus (flowcharts of narratives) → **Activiteiten + actoren per cyclus** _(document)_
- Risico-register stap 2 → **Welke risico's vereisen welke control** _(conclusie)_

**📤 Output**:
- Beheersmatrix per cyclus → **Per risico: control-type, frequentie, eigenaar, evidence** _(document)_

**🛠️ Hoe**:

1. Volg [[beheersactiviteiten]] §vier-categorieen: (a) autorisaties en goedkeuringen, (b) verificaties (reconciliaties, drie-weg-match), (c) functiescheiding, (d) fysieke beveiliging.
2. Pas [[functiescheiding]] §vier-functies expliciet toe op elke kritische transactie: scheid autoriseren, uitvoeren, bewaren en registreren.
3. Onderscheid preventieve controls (vooraf — bv. autorisatielimiet in ERP) en detectieve controls (achteraf — bv. maandelijkse cashreconciliatie). Per risico minstens één van elk.
4. Voor de IT-omgeving: leg algemene IT-controls (toegangsbeheer, change management, back-up) en applicatie-controls (input-validatie, edit-checks) vast — zie [[geinformatiseerde-omgeving-ic]].


**Grondslag**: [[beheersactiviteiten]] §vier-categorieen, [[functiescheiding]] §vier-functies, [[geinformatiseerde-omgeving-ic]] §IT-controls

> [!warning]- Per risico moet één eigenaar in de RACI verantwoordelijk zijn — niet 'het departement'.
>
> _Vaak fout gedaan_: Controls toewijzen aan een dienst zonder concrete persoon — bij personeelswissel valt de control weg.
>
> _Grondslag_: [[beheersactiviteiten]] §toewijzing

### 4. Componenten 4 en 5 — informatie/communicatie en monitoring inrichten

Bouw rapporteringsstromen die de juiste info op het juiste niveau krijgen, en zet doorlopende plus periodieke monitoring op.

**Waarom?** Zonder informatie weet niemand of controles werken; zonder monitoring verzwakt elk systeem in de tijd.

**📥 Input**:
- Beheersmatrix stap 3 → **Welke evidence elk control produceert** _(document)_

**📤 Output**:
- Rapportering-kalender + monitoring-plan → **Wie krijgt welke rapport wanneer; welke spot-checks per kwartaal** _(document)_

**🛠️ Hoe**:

1. Volg [[informatie-en-communicatie-ic]] §kwaliteit: relevant, accuraat, tijdig, toegankelijk. Bouw een KPI-dashboard voor Pieter Vermeulen met maandelijkse cijfers per cyclus.
2. Communicatie loopt drie richtingen: top-down (beleid, doelstellingen), bottom-up (afwijkingen, incidenten via klokkenluiderkanaal — zie [[klokkenluiderregeling]]), en horizontaal (tussen departementen).
3. Stel monitoring op via [[monitoring-interne-controle]] §twee-niveaus: doorlopende monitoring (afstemmingen in dagelijkse processen) en periodieke evaluaties (interne audit, walk-throughs).
4. Plan jaarlijks een formele evaluatie van het IC-systeem als geheel — Sofie Janssens (interne auditor of externe adviseur) voert deze uit en rapporteert aan het auditcomité.


**Grondslag**: [[informatie-en-communicatie-ic]] §kwaliteit, [[monitoring-interne-controle]] §twee-niveaus, [[klokkenluiderregeling]] §intern-kanaal

### 5. Documenteren en formaliseren van het IC-systeem

Leg het volledige systeem vast in een IC-handboek met procesbeschrijvingen (flowcharts en narratives), beheersmatrices, RACI en verantwoordelijkheidstoewijzing.

**Waarom?** Zonder documentatie is het systeem niet auditbaar door interne audit én niet betrouwbaar voor de externe auditor om op te steunen ([[toetsing-interne-beheersing]]).

**📥 Input**:
- Stappen 1-4 deliverables → **Scope, charter, beheersmatrices, monitoring-plan** _(document)_

**📤 Output**:
- IC-handboek Yperse Werkplaats BV → **Versie-beheerd document met alle procesbeschrijvingen + matrices** _(document)_

**🛠️ Hoe**:

1. Stel per kritische cyclus een flowchart op (proces) + narrative (toelichting) + control matrix (risico → control → evidence).
2. Versie-beheer: nummering, datum, eigenaar, jaarlijkse review-cyclus.
3. Maak het handboek toegankelijk voor alle medewerkers — typisch op intranet of in een GRC-tool.
4. Bouw de link met de externe auditor: zorg dat de structuur aansluit bij de werkwijze die de externe auditor gebruikt om IC te begrijpen ([[toetsing-interne-beheersing]]).


> [!example]- Voorbeeld: Yperse Werkplaats BV (productie-KMO, omzet € 8.500.000, 45 werknemers) implementeert haar eerste formele IC-systeem met…
> Yperse Werkplaats BV (productie-KMO, omzet € 8.500.000, 45 werknemers) implementeert haar eerste formele IC-systeem met begeleiding van Xenon Expertise BV. Pieter Vermeulen is zaakvoerder; Sofie Janssens treedt op als externe IC-adviseur.
>
> 1. **Doelstellingenmatrix (uittreksel)** 💬
>
>    Aankoopcyclus:
>    - Operations: aankooporders binnen 2 werkdagen verwerkt
>    - Reporting: aankopen periodecorrect geboekt
>    - Compliance: btw-aftrek correct + leverancierscredibiliteitscheck
>    
>
> 2. **Voorbeeld control matrix-rij** 💬
>
>    Risico: fictieve leveranciers in masterdata
>    Control: nieuwe leverancier vereist KBO-verificatie + ondertekend formulier + tweede goedkeuring CFO
>    Type: preventief
>    Frequentie: per nieuwe leverancier
>    Eigenaar: aankoopdirecteur Tom Lefèvre
>    Evidence: ondertekend formulier in leveranciersdossier
>    
>

**Grondslag**: [[interne-controle]] §dragers, [[toetsing-interne-beheersing]] §begrip, COSO 2013

> [!warning]- Documenteer met de externe auditor in gedachten — flowcharts + matrices verlagen de auditkost en geven evidence voor IC-betrouwbaarheid.
>
> _Vaak fout gedaan_: IC-handboek schrijven als interne procedure-bundel zonder zicht op auditbaarheid — externe auditor moet alles opnieuw mappen.
>
> _Grondslag_: [[toetsing-interne-beheersing]] §begrip-IC-omgeving


## Voorbeelden

> [!example]- Meubelzaak Mertens BV (kleine handels-BV, 8 werknemers) vraagt een KMO-vriendelijke IC-opzet
> **Conclusie**: Pas COSO toe in proportie. Componenten 1, 3 en 5 zijn niet-onderhandelbaar (basis-cultuur, basale functiescheiding, periodieke check zaakvoerder). Componenten 2 en 4 light: één jaarlijkse risico-discussie tussen zaakvoerder + accountant, en maandelijkse kasreconciliatie + bankafstemming als monitoring.
>
> **Grondslag**: [[interne-controle]] §proportionaliteit, [[functiescheiding]] §KMO-uitdaging
>
> **Redenering**: ITAA-norm-kmo-controlenorm §96 erkent expliciet KMO-context. Volledige COSO is niet vereist; de geest van controle moet er zijn met externe compensatie (boekhouder, accountant).

> [!example]- Rotex Roeselare NV (grote NV, beursgenoteerd) — moet COSO + ERM-uitbreiding (COSO II) integreren wegens beurseisen
> **Conclusie**: Pas COSO I als basis toe en breid uit met [[coso-ii-erm-framework]] §risk-appetite + portefeuille-visie op risico's. Voeg een Risk Officer (Marleen De Cock) toe in de tweede lijn van [[drie-lijnen-model]]. Auditcomité onder voorzitterschap van Robert Vandenberghe (onafhankelijk niet-uitvoerend bestuurder met financiële expertise).
>
> **Grondslag**: [[coso-ii-erm-framework]] §risk-appetite, [[drie-lijnen-model]] §lijn-twee, [[auditcomite]] §samenstelling
>
> **Redenering**: Beursnotering + grootte triggeren WVV-verplichtingen en Corporate Governance Code 2020. ERM-uitbreiding hoort bij organisatorische schaal.


## Gebaseerd op concepten

[[interne-controle]] · [[coso-i-framework]] · [[coso-componenten-synthese]] · [[controle-omgeving]] · [[risico-inschatting-organisatie]] · [[beheersactiviteiten]] · [[informatie-en-communicatie-ic]] · [[monitoring-interne-controle]]
## Voortkomend uit

- **Taken**: 1.7.taak.1
- **Kenniselementen**: 1.7.I.A, 1.7.III, 1.7.III.A, 1.7.III.B, 1.7.VIII.A, 1.7.XII.D
