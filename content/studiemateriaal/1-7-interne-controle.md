---
title: 1.7 Interne controle
tags:
- minicursus
- po-1-7
programmaonderdeel: '1.7'
gerelateerde_concepten:
- aankoopcyclus-ic
- actoren-interne-controle
- auditcomite
- auditrisico-1-7-context
- auditrisicomodel
- avg-interne-controle
- beheersactiviteiten
- bijzondere-verslagen-overzicht
- controle-begrip-algemeen
- controle-omgeving
- controlemiddelen-ic
- controleproces-organisatie
- coso-componenten-synthese
- coso-i-framework
- coso-ii-erm-framework
- cyberrisico-ic
- cyclus-analyse-ic
- drie-lijnen-model
- ethiek-organisatie-ic
- evaluatie-interne-controle
- evaluatiecriteria-ic
- externe-auditor-relatie-ic
- externe-controle
- fouten-en-fraude
- fouten-ic
- fraude
- functie-interne-auditor
- functiescheiding
- geinformatiseerde-omgeving-ic
- hr-cyclus-ic
- inbreng-in-natura-verslag
- informatie-en-communicatie-ic
- informatie-kwaliteit-ic
- informatiesysteem-onderneming
- intern-beheersingsrisico
- interne-audit
- interne-controle
- isa-standaarden-ic
- iso-31000-risicobeheer
- itaa-normen-ic
- kenmerken-interne-controle
- klokkenluiderregeling
- managementcontrole
- monitoring-interne-controle
- onderneming-begrip-ic
- opvolging-verrichtingen-ic
- productiecyclus-ic
- risico-inschatting-organisatie
- stromen-onderneming
- taakverdeling-ic
- toetsing-interne-beheersing
- uitvoering-interne-controle
- verkoopcyclus-ic
- verspilling
- voorraadcyclus-ic
- wettelijk-kader-ic
gegenereerd_op: '2026-05-17'
---
> [!warning]- Open beslissingen
> De volgende gaps zijn nog open voor dit programmaonderdeel — inhoud kan onvolledig zijn:
> - `edges.target-ontbreekt` op `intern-beheersingsrisico`: Concept 'intern-beheersingsrisico' (auditrisico-component) heeft geen edge naar PO1.7-record 'intern…
> - `edges.target-ontbreekt` op `toetsing-interne-beheersing`: Methode 'toetsing-interne-beheersing' (test of controls) heeft geen edge naar PO1.7-record 'interne-…
> - `in_praktijk.ontbreekt` op `aankoopcyclus-ic`: Record bevat enkel `verplichting` (189 chars over btw + KB 21.10.2018). Geen `bouwstenen`, geen `voo…
> - `in_praktijk.ontbreekt` op `verkoopcyclus-ic`: Record bevat enkel `verplichting` (77 chars). Geen IC-specifieke bouwstenen (controlepoorten, credit…
> - `in_praktijk.ontbreekt` op `productiecyclus-ic`: Record bevat enkel `verplichting` (78 chars). Geen bouwstenen voor productiebon-flow, voorraad-WIP-c…
> - `in_praktijk.ontbreekt` op `hr-cyclus-ic`: Record bevat enkel `verplichting` (82 chars). Geen bouwstenen voor ghost-employee-risico, loonbereke…
> - `in_praktijk.ontbreekt` op `voorraadcyclus-ic`: Record bevat enkel `verplichting` (69 chars, KB 21.10.2018) + 2 valkuilen. Geen bouwstenen voor inve…
> - `in_praktijk.ontbreekt` op `uitvoering-interne-controle`: Anchor 1.7.VIII.A "uitvoering van IC" — record bevat enkel `verplichting` + 2 valkuilen. Geen bouwst…
> - `in_praktijk.ontbreekt` op `evaluatie-interne-controle`: Anchor 1.7.VIII.F + 1.7.XI "evaluatie IC" — record bevat enkel `verplichting` (267 chars) + 1 in_pra…
> - `in_praktijk.ontbreekt` op `controleproces-organisatie`: Record bevat enkel `verplichting` (51 chars: "managementinstrument"). Geen bouwstenen voor planning/…
> - `in_praktijk.ontbreekt` op `inbreng-in-natura-verslag`: Record bevat enkel `verplichting` (227 chars). Geen bouwstenen voor inhoud verslag, waarderingsmetho…
> - `edges.target-ontbreekt` op `interne-controle`: edge `vergelijkt-met` wijst naar 'coso-i-erm-framework' — bestaat niet. Bedoeld is waarschijnlijk 'c…
> - `edges.target-ontbreekt` op `functiescheiding`: edge wijst naar 'vier-functies-segregatie' — record bestaat niet. De vier functies zijn beschreven a…
> - `records.overlappend-fenomeen` op `auditrisico-1-7-context`: Record beschrijft auditrisico in IC-context (1.7.V.E) maar 1.6 heeft al `auditrisicomodel` (IR x CR …
> - `vergelijkingsparen.vrije-tekst-niet-gespiegeld` op `externe-controle`: Record beschrijft externe controle door commissaris/accountant/fiscale-controleur (1.7.I.B). 1.2-con…
> - `in_praktijk.ontbreekt` op `cyclus-analyse-ic`: Synthese-record verwijst naar 5 cyclus-records (aankoop/productie/verkoop/hr/voorraad) die allemaal …

## Leesgids

Deze minicursus bouwt interne controle op in lagen: eerst begrippen en actoren, dan het COSO-raamwerk als denkkader, vervolgens risico, controle-activiteiten en de transactiecycli waar IC concreet landt. Synthese-fiches geven het overzicht; thematische blokken gaan in de diepte; competenties vertalen de leerstof naar handelingen. Lees de hoofdstukken in volgorde — elke laag bouwt op de vorige en de cyclus-analyse aan het eind veronderstelt dat je functiescheiding en COSO-component 3 al beheerst. Gebruik de cheatsheet onderaan om verwante begrippen (interne audit, externe controle, managementcontrole) uit elkaar te houden.

## Waarom dit programmaonderdeel telt

Interne controle is het scharnier tussen boekhoudorganisatie en externe audit: de externe auditor steunt erop, het management gebruikt het om de organisatie bestuurbaar te houden, de wetgever verwacht het voor bepaalde rechtsvormen. Op het examen komt IC zowel als zelfstandig thema terug (ontwerpvragen, fraude-detectie, functiescheiding) als verweven met andere onderdelen — een verkeerd ontworpen aankoopcyclus levert risico's voor de jaarrekening én voor de commissaris. De stof is breed maar repeteerbaar: vijf COSO-componenten, een handvol cycli, een vast onderscheid tussen fout en fraude. Wie het systeem-denken vasthoudt — design plus werking, met de drie lijnen als organisatorische vertaling — kan elke concrete situatie redeneren in plaats van uit het hoofd te leren.

## Waarom interne controle? Van procedure naar systeem

Elke organisatie zet eigen controlemechanismen op naast de externe controle, omdat bestuur, aandeelhouders, fiscus en werknemers elk hun eigen belang bij betrouwbare informatie hebben. Die mechanismen kunnen losse procedures lijken — een aftekening hier, een controle daar — maar examen-vragen draaien net om het onderscheid tussen losse handeling en geïntegreerd systeem. Het IC-systeem dient drie soorten doelstellingen: operationele efficiëntie, betrouwbare financiële rapportering en compliance met wet en regelgeving. Wie dat drieluik vasthoudt, kan elke deelvraag in PO 1.7 plaatsen.

## Kenmerken van interne controle

Vóór de details: welk soort beest is interne controle eigenlijk? Deze synthese geeft het mentale model — effectief, efficiënt, betrouwbaar, met redelijke (geen absolute) zekerheid — en de inherente beperkingen die elke verdere stof kleuren.

[[kenmerken-interne-controle|→ Volledige synthese-fiche]]

## Begrippen-fundament: interne controle, informatie en ethiek

Zes basisbegrippen leggen het canvas waarop alle latere blokken zitten: wat is "controle", wat is de onderneming als object, welke stromen en welk informatiesysteem maken haar zichtbaar, en welke ethische verwachting hangt eromheen. Lees ze als woordenboek dat je later terugslaat.

- [[controle-begrip-algemeen|Controle — begrip algemeen]] · `begrip`
- [[onderneming-begrip-ic|Onderneming (begrip in IC-context)]] · `begrip`
- [[stromen-onderneming|Stromen in de onderneming]] · `begrip`
- [[informatiesysteem-onderneming|Informatiesysteem van de onderneming]] · `begrip`
- [[informatie-kwaliteit-ic|Informatie en haar kwaliteitseisen]] · `begrip`
- [[ethiek-organisatie-ic|Ethiek in de organisatie (IC-context)]] · `begrip`

## Actoren van interne controle

Na het wat volgt het wie. Deze synthese ordent bestuur, management, auditcomité, interne en externe auditor en medewerkers tot één governance-plaat, met het drie-lijnen-model als rode draad.

[[actoren-interne-controle|→ Volledige synthese-fiche]]

## Actoren en organen: management, interne audit, auditcomité

Zoom in op de spelers die in examenvragen het vaakst verward worden: management (eerste lijn), interne audit (derde lijn), auditcomité (toezicht), externe auditor (extern). Wie wie controleert en wie aan wie rapporteert, bepaalt vaak het juiste antwoord.

- [[managementcontrole|Managementcontrole]] · `begrip`
- [[interne-audit|Interne audit]] · `fenomeen`
- [[functie-interne-auditor|Functie van de interne auditor]] · `actor`
- [[auditcomite|Auditcomité]] · `actor`
- [[drie-lijnen-model|Drie-lijnen-model (Three Lines of Defense)]] · `methode`
- [[externe-auditor-relatie-ic|Externe auditor en interne controle — relatie]] · `begrip`
- [[externe-controle|Externe controle]] · `begrip`

## COSO-componenten — synthese-overzicht

Dit is het centrale denkkader van PO 1.7: vijf componenten die samen het IC-systeem vormen. Elke competentie die volgt is terug te voeren op één of meer van deze componenten — ken ze niet als lijst, ken ze als raamwerk.

[[coso-componenten-synthese|→ Volledige synthese-fiche]]

## Ontwerpen van een intern-controlesysteem volgens de vijf COSO-componenten

Eerste handelings-competentie: hoe vertaal je het raamwerk naar een concreet systeem voor één organisatie. De procedure volgt de COSO-componenten als bouwblokken — controle-omgeving eerst, monitoring laatst.

[[competenties/ontwerpen-intern-controlesysteem-coso|→ Volledige procedure]]

## Risicobeheer en digitale omgeving: van auditrisicomodel naar cyberrisico

Risico is de motor van COSO-component 2: zonder risico-inschatting weet je niet welke controles je nodig hebt. Dit blok bouwt van het auditrisicomodel — bekend uit PO 1.6 — naar de specifieke IC-component, en eindigt bij de digitale omgeving waar IT-controles en cyberrisico verweven raken.

- [[auditrisicomodel|Auditrisicomodel (controlerisico)]] · `methode`
- [[auditrisico-1-7-context|Auditrisico's in IC-context]] · `begrip`
- [[intern-beheersingsrisico|Intern beheersingsrisico]] · `begrip`
- [[geinformatiseerde-omgeving-ic|Interne controle in geïnformatiseerde omgeving]] · `begrip`
- [[cyberrisico-ic|Cyberrisico in IC-context]] · `fenomeen`

## Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem

Concrete competentie achter COSO-component 2: hoe identificeer en weeg je risico's op het niveau van de organisatie, voordat je controles ontwerpt. De procedure schaalt van bedrijfsbreed naar transactieniveau.

[[competenties/uitvoeren-risicoanalyse-organisatie|→ Volledige procedure]]

## Implementeren van functiescheiding op kritieke transactiecycli

Functiescheiding is de hoeksteen van controle-activiteiten en de meest geëxamineerde IC-techniek. De competentie laat zien hoe je de vier basisfuncties splitst zonder de organisatie operationeel te blokkeren.

[[competenties/implementeren-functiescheiding-transactiecycli|→ Volledige procedure]]

## Controle-activiteiten en monitoring in detail

De uitvoeringszijde van het systeem: hoe verlopen controles in de praktijk, welke instrumenten staan ter beschikking, en hoe toetst de externe of interne auditor of die controles werken. Dit blok scharniert tussen ontwerp (COSO-componenten 1-3) en effectiviteits-evaluatie (component 5).

- [[uitvoering-interne-controle|Uitvoering van interne controle — aanpak]] · `procedure`
- [[controleproces-organisatie|Controleproces in de organisatie]] · `procedure`
- [[controlemiddelen-ic|Controlemiddelen — concrete instrumenten]] · `begrip`
- [[toetsing-interne-beheersing|Toetsing van interne beheersing (test of controls)]] · `methode`

## Opzetten van controle-activiteiten en monitoringsmechanismen

Vertaling van COSO-componenten 3 en 5 naar handeling: welke controles kies je per risico en hoe organiseer je de monitoring die ze werkend houdt? De procedure verbindt risico-inschatting met concrete controlekeuze.

[[competenties/opzetten-controleactiviteiten-en-monitoring|→ Volledige procedure]]

## Fouten en fraude — onderscheid in IC

Een eigen kapstok voor het drieluik fout-fraude-verspilling: drie verschillende fenomenen met elk hun eigen oorzaken, juridische gevolgen en detectie-strategie. Het examen verwart deze categorieën doelbewust.

[[fouten-en-fraude|→ Volledige synthese-fiche]]

## Identificeren van fouten, fraude en verspilling in een organisatie

De detectie-competentie: hoe herken je rode vlaggen, welke controles werken preventief versus detectief, en wanneer schakel je het auditcomité of de externe auditor in. De procedure leunt op de fraudedriehoek als denkmodel.

[[competenties/identificeren-fouten-fraude-verspilling|→ Volledige procedure]]

## Cyclusanalyse bij IC — synthese

Hier landt de stof op concrete bedrijfsprocessen. De synthese vergelijkt de vijf transactiecycli zij aan zij: typische risico's, kritische controles en de functiescheidings-eisen die per cyclus verschuiven.

[[cyclus-analyse-ic|→ Volledige synthese-fiche]]

## Transactiecycli in detail: aankoop, verkoop, productie, HR, voorraad

Per cyclus de eigen logica en de typische zwakke plekken — examenvragen putten hier graag uit met casus-stijl beschrijvingen waarin één functie ontbreekt of dubbel zit. De twee slot-records over taakverdeling en opvolging gelden cyclus-overschrijdend.

- [[aankoopcyclus-ic|Aankoopcyclus — interne controle]] · `procedure`
- [[verkoopcyclus-ic|Verkoopcyclus — interne controle]] · `procedure`
- [[productiecyclus-ic|Productiecyclus — interne controle]] · `procedure`
- [[hr-cyclus-ic|HR-cyclus — interne controle]] · `procedure`
- [[voorraadcyclus-ic|Voorraad — fysieke controle en veiligheid]] · `procedure`
- [[taakverdeling-ic|Taakverdeling binnen interne controle]] · `begrip`
- [[opvolging-verrichtingen-ic|Opvolging van verrichtingen]] · `begrip`

## Wettelijk kader voor interne controle in België

Het juridische skelet onder IC: welke bepalingen verplichten welke entiteiten tot welk niveau van interne controle. De synthese bundelt WVV, governance-code en de aanpalende kaders rond data en klokkenluider tot één overzicht.

[[wettelijk-kader-ic|→ Volledige synthese-fiche]]

## ISA-standaarden in IC-context

ISA's vormen de spiegel waarmee de externe auditor naar IC kijkt — en die spiegel stuurt indirect het IC-ontwerp en de interne-audit-aanpak. Hou de relevante standaarden vooral op meta-niveau vast: welke standaard welk aspect raakt.

[[isa-standaarden-ic|→ Volledige synthese-fiche]]

## ITAA-normen en interne controle

Naast ISA bestaan eigen ITAA-normen die het IC-werk van de gecertificeerd accountant en bedrijfsrevisor regelen. Deze synthese beperkt zich tot wat examenmatig vereist is — welke norm raakt welk aspect, zonder paragraaf voor paragraaf.

[[itaa-normen-ic|→ Volledige synthese-fiche]]

## Beoordelen van de effectiviteit van een intern-controlesysteem (interne audit)

De evaluatie-competentie: hoe toetst een interne auditor of het IC-systeem niet alleen op papier bestaat (design effectiveness) maar ook werkelijk werkt (operating effectiveness). Dit onderscheid keert in elke evaluatie-vraag terug.

[[competenties/beoordelen-effectiviteit-ic-via-interne-audit|→ Volledige procedure]]

## Opstellen van een intern-audit-rapport

Een interne auditor levert geen wettelijk verslag maar een managementrapport. De competentie behandelt structuur, toon en adressering — fundamenteel anders dan een commissarisverslag.

[[competenties/opstellen-intern-audit-rapport|→ Volledige procedure]]

## Integreren van AVG-compliance in het intern-controlesysteem

Privacy-regelgeving is geen apart eiland: AVG-verplichtingen rond persoonsgegevens, verwerkingsregister en datalekken vragen om controles binnen het IC-systeem. De competentie toont hoe je die integreert in plaats van naast te laten staan.

[[competenties/integreren-avg-compliance-in-ic|→ Volledige procedure]]

## Adviseren van het management bij IC-design als externe adviseur

De gecertificeerd accountant treedt vaak op als IC-adviseur — niet als auditor, maar als ontwerp-partner van het management. De competentie scherpt de positie aan: adviseren mag, maar onafhankelijkheid en deontologie blijven kaders.

[[competenties/adviseren-management-ic-design-als-externe-adviseur|→ Volledige procedure]]

## Bijzondere verslagen — overzicht

Bijzondere verslagen onder het WVV (inbreng in natura, quasi-inbreng, uitkeringen, ontbinding) verbinden IC-evaluatie met vennootschapsrechtelijke procedures. De synthese ordent wie welk verslag mag opstellen en bij welke verrichting het verplicht is.

[[bijzondere-verslagen-overzicht|→ Volledige synthese-fiche]]

## Opstellen van bijzondere verslagen en IC-evaluaties voor specifieke verrichtingen

De praktische tegenhanger van de synthese hierboven: hoe je een bijzonder verslag opbouwt, welke waarderingsmethode je kiest en hoe je de IC-evaluatie voor de specifieke verrichting documenteert.

[[competenties/opstellen-bijzondere-verslagen-en-ic-evaluaties|→ Volledige procedure]]

## Reflectie: interne controle als systeem, niet als procedurelijst

Drie inzichten houden PO 1.7 bij elkaar. Interne controle is geïntegreerd ontwerp én werking, niet een verzameling losse aftekenmomenten — zonder operating effectiveness blijft het design dode letter. De vijf COSO-componenten vormen een denkkader, geen checklist: ze leggen uit waaróm een controle zit waar ze zit. En het drie-lijnen-model maakt het systeem bestuurbaar door management, interne audit en externe controle elk in hun eigen rol te zetten. Wie deze drie samen vasthoudt, herkent de aansluiting met PO 1.6 (externe auditor steunt op IC-design en werking voor zijn risicoanalyse) en met PO 1.2 (boekhoudorganisatie en IC versterken elkaar als datastructuur en controlestructuur).


## Synthese-stappenplan

Vertrek bij een nieuwe casus altijd van de organisatie als context: wat zijn de stromen, welke informatie wordt waar geproduceerd, welke actoren zitten in welke lijn. Identificeer dan de relevante risico's per doelstellings-categorie — operationeel, financiële rapportering, compliance — en weeg ze op waarschijnlijkheid en impact. Kies vervolgens controle-activiteiten die het risico afdekken, met functiescheiding en opvolging van verrichtingen als basis-instrumenten. Plaats die controles binnen het COSO-raamwerk, zodat je weet welke component zwak blijft. Toets daarna of de controles ook werken: niet alleen aanwezig (design) maar ook uitgevoerd (operating). Schakel monitoring in via de drie lijnen — management op eerste lijn, risk en compliance op tweede, interne audit op derde — en laat de externe auditor zijn eigen toetsing doen. Documenteer telkens fout-fraude-verspilling-bevindingen en rapporteer aan de juiste geadresseerde. Sluit af met een evaluatie tegen de kenmerken effectief, efficiënt, adequaat en betrouwbaar.

## Cheatsheet

### Vergelijkingsparen-matrix

| Concept | Verwarrend met | Trigger |
|---|---|---|
| [[controle-begrip-algemeen]] | [[controle]] | Examen-context: gaat het over jaarrekening / IC / audit? → betekenis (1). Gaat het over consolidatie / groepen / belangenpercentage? → betekenis (2). |
| [[externe-controle]] | [[interne-controle]] | Wie betaalt en gebruikt het verslag? Externe stakeholder → externe controle. Het management zelf → interne controle of interne audit. |
| [[externe-controle]] | [[interne-audit]] | Behoort de controleur tot de onderneming? Ja → IA. Nee → externe controle. |
| [[interne-audit]] | [[externe-controle]] | Wie betaalt de auditor en wie krijgt het verslag? Eigen werknemer + intern verslag → IA. Externe firma + extern verslag → externe controle. |
| [[interne-audit]] | [[interne-controle]] | Voor elke 'controle': gebeurt het bij elke transactie (= IC) of periodiek/steekproefsgewijs (= IA)? |
| [[interne-controle]] | [[interne-audit]] | Vraagt het examen 'wie tekent de factuur af'? → IC. 'Wie evalueert of de procedure werkt?' → IA. |
| [[interne-controle]] | [[externe-controle]] | Examenvraag spreekt over 'wie steunt op wie': de externe auditor (Sofie Janssens) steunt op de interne controle om zijn werk te beperken — niet andersom. |
| [[managementcontrole]] | [[interne-controle]] | Vraagt het examen 'hoe wordt afwijking van plan vs werkelijk opgevolgd?' → managementcontrole. 'Hoe wordt fraude voorkomen bij betalingen?' → IC. |


## Examenfocus

Vragen op PO 1.7 testen vooral systeem-denken in plaats van losse feiten. Een eerste terugkerend patroon is het onderscheid tussen design en operating effectiveness: een controle die op papier staat maar niet wordt uitgevoerd is geen werkende controle. Een tweede patroon is rolverwarring tussen interne controle, interne audit, managementcontrole en externe controle — wie controleert, wie betaalt, wie krijgt het verslag. Een derde patroon zijn casus-vragen waarin één functie in een transactiecyclus dubbel of ontbrekend is en je de zwakte moet benoemen vanuit functiescheiding. Hou ook het drieluik fout-fraude-verspilling scherp: andere oorzaken, andere detectie, andere juridische afhandeling.

<!-- TODO: examenvragen via classify_vragen_naar_programmaonderdelen.py -->

## Competentie-index

<div class="two-column-list">

- [[competenties/adviseren-management-ic-design-als-externe-adviseur|Adviseren van het management bij IC-design als externe adviseur]]
- [[competenties/beoordelen-effectiviteit-ic-via-interne-audit|Beoordelen van de effectiviteit van een intern-controlesysteem (interne audit)]]
- [[competenties/identificeren-fouten-fraude-verspilling|Identificeren van fouten, fraude en verspilling in een organisatie]]
- [[competenties/implementeren-functiescheiding-transactiecycli|Implementeren van functiescheiding op kritieke transactiecycli]]
- [[competenties/integreren-avg-compliance-in-ic|Integreren van AVG-compliance in het intern-controlesysteem]]
- [[competenties/ontwerpen-intern-controlesysteem-coso|Ontwerpen van een intern-controlesysteem volgens de vijf COSO-componenten]]
- [[competenties/opstellen-bijzondere-verslagen-en-ic-evaluaties|Opstellen van bijzondere verslagen en IC-evaluaties voor specifieke verrichtingen]]
- [[competenties/opstellen-intern-audit-rapport|Opstellen van een intern-audit-rapport]]
- [[competenties/opzetten-controleactiviteiten-en-monitoring|Opzetten van controle-activiteiten en monitoringsmechanismen]]
- [[competenties/uitvoeren-risicoanalyse-organisatie|Uitvoeren van een risico-identificatie en -analyse voor het IC-systeem]]

</div>

## Concept-index

<div class="two-column-list">

- [[avg-interne-controle|AVG/GDPR in IC-context]] · `regel`
- [[aankoopcyclus-ic|Aankoopcyclus — interne controle]] · `procedure`
- [[actoren-interne-controle|Actoren van interne controle]] · `synthese`
- [[auditcomite|Auditcomité]] · `actor`
- [[auditrisico-1-7-context|Auditrisico's in IC-context]] · `begrip`
- [[auditrisicomodel|Auditrisicomodel (controlerisico)]] · `methode`
- [[beheersactiviteiten|Beheersactiviteiten (COSO-component 3)]] · `begrip`
- [[bijzondere-verslagen-overzicht|Bijzondere verslagen — overzicht]] · `synthese`
- [[coso-i-framework|COSO I — Internal Control Integrated Framework]] · `methode`
- [[coso-ii-erm-framework|COSO II — Enterprise Risk Management]] · `methode`
- [[coso-componenten-synthese|COSO-componenten — synthese-overzicht]] · `synthese`
- [[controle-begrip-algemeen|Controle — begrip algemeen]] · `begrip`
- [[controle-omgeving|Controle-omgeving (COSO-component 1)]] · `begrip`
- [[controlemiddelen-ic|Controlemiddelen — concrete instrumenten]] · `begrip`
- [[controleproces-organisatie|Controleproces in de organisatie]] · `procedure`
- [[cyberrisico-ic|Cyberrisico in IC-context]] · `fenomeen`
- [[cyclus-analyse-ic|Cyclusanalyse bij IC — synthese]] · `synthese`
- [[drie-lijnen-model|Drie-lijnen-model (Three Lines of Defense)]] · `methode`
- [[ethiek-organisatie-ic|Ethiek in de organisatie (IC-context)]] · `begrip`
- [[evaluatie-interne-controle|Evaluatie van de interne controle]] · `procedure`
- [[evaluatiecriteria-ic|Evaluatiecriteria voor interne controle]] · `begrip`
- [[externe-auditor-relatie-ic|Externe auditor en interne controle — relatie]] · `begrip`
- [[externe-controle|Externe controle]] · `begrip`
- [[fouten-en-fraude|Fouten en fraude — onderscheid in IC]] · `synthese`
- [[fouten-ic|Fouten in IC-context]] · `fenomeen`
- [[fraude|Fraude]] · `fenomeen`
- [[functie-interne-auditor|Functie van de interne auditor]] · `actor`
- [[functiescheiding|Functiescheiding (segregation of duties)]] · `methode`
- [[hr-cyclus-ic|HR-cyclus — interne controle]] · `procedure`
- [[isa-standaarden-ic|ISA-standaarden in IC-context]] · `synthese`
- [[iso-31000-risicobeheer|ISO 31000 — Risk Management Guidelines]] · `methode`
- [[itaa-normen-ic|ITAA-normen en interne controle]] · `synthese`
- [[informatie-en-communicatie-ic|Informatie en communicatie (COSO-component 4)]] · `begrip`
- [[informatie-kwaliteit-ic|Informatie en haar kwaliteitseisen]] · `begrip`
- [[informatiesysteem-onderneming|Informatiesysteem van de onderneming]] · `begrip`
- [[intern-beheersingsrisico|Intern beheersingsrisico]] · `begrip`
- [[interne-audit|Interne audit]] · `fenomeen`
- [[interne-controle|Interne controle]] · `begrip`
- [[geinformatiseerde-omgeving-ic|Interne controle in geïnformatiseerde omgeving]] · `begrip`
- [[kenmerken-interne-controle|Kenmerken van interne controle]] · `synthese`
- [[klokkenluiderregeling|Klokkenluiderregeling (interne meldkanaal)]] · `regel`
- [[managementcontrole|Managementcontrole]] · `begrip`
- [[monitoring-interne-controle|Monitoring (COSO-component 5)]] · `methode`
- [[onderneming-begrip-ic|Onderneming (begrip in IC-context)]] · `begrip`
- [[opvolging-verrichtingen-ic|Opvolging van verrichtingen]] · `begrip`
- [[productiecyclus-ic|Productiecyclus — interne controle]] · `procedure`
- [[risico-inschatting-organisatie|Risico-inschatting binnen de organisatie (COSO-component 2)]] · `methode`
- [[stromen-onderneming|Stromen in de onderneming]] · `begrip`
- [[taakverdeling-ic|Taakverdeling binnen interne controle]] · `begrip`
- [[toetsing-interne-beheersing|Toetsing van interne beheersing (test of controls)]] · `methode`
- [[uitvoering-interne-controle|Uitvoering van interne controle — aanpak]] · `procedure`
- [[verkoopcyclus-ic|Verkoopcyclus — interne controle]] · `procedure`
- [[inbreng-in-natura-verslag|Verslag bij inbreng in natura]] · `procedure`
- [[verspilling|Verspilling (rationeel gebruik van middelen)]] · `fenomeen`
- [[voorraadcyclus-ic|Voorraad — fysieke controle en veiligheid]] · `procedure`
- [[wettelijk-kader-ic|Wettelijk kader voor interne controle in België]] · `synthese`

</div>
