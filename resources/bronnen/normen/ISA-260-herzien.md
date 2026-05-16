---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 260 (herzien) — Communicatie met de met governance belaste personen
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-260_(herzien)_nl_2023.pdf
    sha256: 8ac42fe9df5603a1b680fb91130bcb589af1c27a944d1992bfb9008bb250abeb
    version: 2026-05-16
  stale: false
  stale_reason: null
  tooling:
    model: null
    pipeline: tools/download/scrape_ibr_isa.py (subagent a2fee1b5)
    pipeline_version: '1.0'
    prompt_version: null
  trust:
    status: needs-rework
    confirmed_at: '2026-05-16T20:31:37Z'
    confirmed_by: subagent-qa-2026-05-16
    rationale: >-
      QA-pass 2026-05-16: pymupdf-conversie via tools/download/scrape_ibr_isa.py extraheerde
      tekst lineair zonder structurele heading-injectie (0 ##-headings in body). Page-footers
      ('ALGEHELE DOELSTELLINGEN ... ISA 200 NBA-IBR 2022 N/M Originele bron: Handbook ... Versie
      2023') repeteren ~elke pagina inline. Paragraph-numbers ('1.', '2.') staan op aparte
      regels van hun body-tekst, en bullets ('• item') zijn losgekoppeld van hun bullet-marker.
      RAG-chunking faalt zonder heading-grenzen — ETL-fix nodig: inject_headings_isa +
      strip_isa_page_footers transformers.
    layer1: null
    layer2: null
status: beschikbaar
tags:
- ISA
- controle
- audit
- bedrijfsrevisor
- po-1.6
- po-1.7
title: ISA 260 (herzien) — Communicatie met de met governance belaste personen
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 260 (herzien) — Communicatie met de met governance belaste personen

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-260_(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `8ac42fe9df5603a1b680fb91130bcb589af1c27a944d1992bfb9008bb250abeb`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard 260 (herzien) 
ISA 260 (herzien) 
 
Communicatie met de met 
governance belaste personen

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
2/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Over de IAASB 
 
Copyright IFAC 
 
Deze Internationale controlestandaard (ISA) werd in 2022 in de Engelse taal gepubliceerd door de 
International Auditing and Assurance Standards Board (IAASB) van de International Federation of 
Accountants (IFAC). Deze ISA werd in 2022 vertaald naar het Nederlands door de Nederlandse 
Beroepsorganisatie van Accountants (NBA), met medewerking van het Belgisch Instituut van de 
Bedrijfsrevisoren (IBR), en werd verspreid met toestemming van IFAC. Het proces voor het vertalen van 
de Internationale controlestandaard (ISA) 260 (herzien) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 
260 (herzien) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 260 (herzien) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 260 (herzien) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 260 (Revised), Communication with Those Charged 
with Governance. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, 
and Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
3/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
INTERNATIONALE CONTROLESTANDAARD 260 (herzien) 
 
COMMUNICATIE MET DE MET GOVERNANCE BELASTE 
PERSONEN 
 
(Van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten) 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ...........................................................................................................  1 -3 
De rol van communicatie  ..................................................................................................................... 4-7 
Ingangsdatum.......................................................................................................................................................  8 
Doelstellingen ........................................................................................................................................ 9 
Definities ...................................................................................................................................................... 10 
Vereisten 
De met governance belaste personen ...............................................................................................11-13 
Mee te delen aangelegenheden 
 ................................................................................................  14-17 
Het communicatieproces .................................................................................................................  18-22 
Documentatie ........................................................................................................................................  23 
Toepassingsgerichte en overige verklarende teksten 
De met governance belaste personen ............................................................................................. A1-A8 
Mee te delen aangelegenheden .................................................................................................... A9-A36 
Het communicatieproces ............................................................................................................. A37-A53 
Documentatie ....................................................................................................................................... A54  
 
Bijlage 1:  
Specifieke vereisten in ISQM 1 en andere ISA’s met betrekking tot de communicatie 
met de met governance belaste personen 
Bijlage 2:  
Kwalitatieve aspecten van praktijken inzake administratieve verwerking 
 
 
International Standard on Auditing (ISA) 260 (herzien), “Communicatie met de met governance belaste 
personen”, moet worden gelezen in samenhang met ISA 200, “Algehele doelstellingen van de 
onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de International 
Standards on Auditing”.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
4/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Inleiding 
 
Toepassingsgebied van deze ISA 
 
1. 
Deze International Standard on Auditing (ISA) behandelt de communicatieverantwoordelijkheid 
van de auditor ten aanzien van de met governance belaste personen bij een controle van 
financiële overzichten. Hoewel deze ISA van toepassing is ongeacht de governance-structuur of 
de omvang van een entiteit, zijn er bijzondere overwegingen van toepassing wanneer alle met 
governance belaste personen betrokken zijn bij het leiden van de entiteit, alsmede voor 
beursgenoteerde entiteiten. Deze ISA stelt geen vereisten vast met betrekking tot de 
communicatie van de auditor met het management of met de eigenaren van een entiteit tenzij zij 
ook een rol hebben in het kader van governance. 
 
2. 
Deze ISA is opgesteld in de context van een controle van financiële overzichten maar kan ook, 
naargelang nodig aangepast aan de omstandigheden, van toepassing zijn op controles van andere 
historische financiële informatie wanneer de met governance belaste personen een 
verantwoordelijkheid hebben om toezicht uit te oefenen op het opstellen van die informatie. 
 
3. 
Vanuit het inzicht dat effectieve wederzijdse communicatie bij een controle van financiële 
overzichten belangrijk is, voorziet deze ISA in een algemeen kader voor de communicatie van de 
auditor met de met governance belaste personen en stelt hij enkele specifieke aangelegenheden 
vast die aan de met governance belaste personen moeten worden meegedeeld. In andere ISA’s 
zijn aangelegenheden vastgesteld die in aanvulling op de vereisten van deze ISA moeten worden 
meegedeeld (zie bijlage 1). Daarnaast stelt ISA 2651 specifieke vereisten vast inzake het 
meedelen aan de met governance belaste personen van significante tekortkomingen in de interne 
beheersing die de auditor tijdens de controle heeft geïdentificeerd. Het meedelen van overige 
aangelegenheden, hoewel niet vereist op grond van deze of andere ISA’s, kan wel vereist zijn op 
grond van wet- of regelgeving, op grond van afspraken met de entiteit of op grond van aanvullende 
vereisten die op de opdracht van toepassing zijn, bijvoorbeeld de standaarden van een nationale 
beroepsorganisatie voor accountancy. Niets in deze ISA belet de auditor enige andere 
aangelegenheid aan de met governance belaste personen mee te delen. (Zie par. A33-A36) 
 
De rol van communicatie 
 
4. 
Deze ISA is in de eerste plaats gericht op mededelingen van de auditor aan de met governance 
belaste personen. Niettemin is effectieve wederzijdse communicatie belangrijk om: 
 
(a) 
de auditor en de met governance belaste personen te helpen inzicht te verwerven in 
aangelegenheden die met de controle verband houden en bij het ontwikkelen van een 
constructieve werkrelatie. Deze relatie wordt ontwikkeld met inachtneming van de 
onafhankelijkheid en objectiviteit van de auditor; 
(b) 
de auditor te helpen voor de controle relevante informatie te verkrijgen van de met 
governance belaste personen. De met governance belaste personen kunnen de auditor 
bijvoorbeeld bijstaan bij het verwerven van inzicht in de entiteit en haar omgeving, bij het 
aanwijzen van passende bronnen voor controle-informatie en bij het verschaffen van 
informatie over specifieke transacties of gebeurtenissen; en 
(c) 
de met governance belaste personen te helpen hun verantwoordelijkheid te vervullen voor 
het houden van toezicht op het proces van financiële verslaggeving, waardoor de risico’s 
op een afwijking van materieel belang in de financiële overzichten worden beperkt. 
 
5. 
Hoewel de auditor verantwoordelijk is voor het meedelen van aangelegenheden die op grond van 
deze ISA zijn vereist, heeft het management ook een verantwoordelijkheid om aangelegenheden 
die van belang zijn in het kader van governance aan de met governance belaste personen mee te 
delen. 
Communicatie 
door 
de 
auditor 
ontslaat 
het 
management 
niet 
van 
deze 
 
1  
ISA 265, Meedelen van tekortkomingen in de interne beheersing aan de met governance belaste personen en het 
management.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
5/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
verantwoordelijkheid. Evenmin ontslaat het meedelen door het management aan de met 
governance belaste personen van aangelegenheden waarvan de auditor wordt vereist dat hij ze 
meedeelt, de auditor van zijn verplichting om deze zelf ook mee te delen. Het door het 
management meedelen van deze aangelegenheden kan echter van invloed zijn op de vorm of 
timing van de communicatie van de auditor met de met governance belaste personen. 
 
6. 
Het duidelijk meedelen van specifieke aangelegenheden die overeenkomstig de ISA’s vereist te 
worden meegedeeld, vormt een integraal onderdeel van iedere controle. ISA’s vereisen echter van 
de auditor niet om werkzaamheden uit te voeren die er specifiek op gericht zijn te bepalen welke 
eventuele andere aangelegenheden aan de met governance belaste personen moeten worden 
meegedeeld. 
 
7. 
Mogelijk wordt het meedelen van bepaalde aangelegenheden door de auditor aan de met 
governance belaste personen door wet- of regelgeving beperkt in bepaalde rechtsgebieden. Wet- 
of regelgeving kan specifiek verbieden dat een mededeling wordt gedaan of een andere actie 
wordt ondernomen die een nadelige invloed zou kunnen hebben op een onderzoek dat door een 
bevoegde instantie naar een daadwerkelijke dan wel een vermoede illegale handeling wordt 
uitgevoerd, inclusief het hierop attenderen van de entiteit. Bijvoorbeeld wanneer van de auditor is 
vereist om de geïdentificeerde of vermoede niet-naleving te rapporterenan een bevoegde instantie 
krachtens anti-witwas wetgeving. In deze omstandigheden kunnen de kwesties die worden 
overwogen door de auditor complex van aard zijn en kan de auditor het geschikt achten om 
juridisch advies in te winnen. 
 
Ingangsdatum 
 
8. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten.  
 
Doelstellingen 
 
9. 
De doelstellingen van de auditor zijn: 
 
(a) 
de verantwoordelijkheden van de auditor met betrekking tot de controle van de financiële 
overzichten, alsmede een overzicht van de geplande reikwijdte en timing van de controle 
duidelijk aan de met governance belaste personen mee te delen; 
(b) 
van de met governance belaste personen voor de controle relevante informatie te 
verkrijgen; 
(c) 
tijdig aan de met governance belaste personen waarnemingen te verschaffen die 
voortkomen uit de controle en die significant en relevant zijn voor hun verantwoordelijkheid 
om toezicht uit te oefenen op het proces van financiële verslaggeving; en 
(d) 
doeltreffende wederzijdse communicatie tussen de auditor en de met governance belaste 
personen te bevorderen. 
 
Definities 
 
10. 
Voor de toepassing van de ISA’s hebben de volgende termen de hierna weergegeven 
betekenis: 
 
(a) 
de met governance belaste personen – De persoon (personen) of organisatie(s) 
(bijvoorbeeld: een trustee van een vennootschap), met verantwoordelijkheid voor het 
uitoefenen van toezicht op de strategische richting van de entiteit en op de 
verantwoordingsplicht van de entiteit. Deze verantwoordelijkheid omvat het uitoefenen van 
toezicht op het proces van financiële verslaggeving. Voor bepaalde entiteiten in sommige 
rechtsgebieden kan ook leidinggevend personeel behoren tot de met governance belaste 
personen, bijvoorbeeld bij het dagelijks bestuur betrokken leden van een governance-
orgaan van een entiteit in de private of publieke sector of een eigenaar-bestuurder. Zie de

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
6/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
paragrafen A1-A8 voor een bespreking van de verschillende vormen van governance-
structuren. 
(b) 
het management – De persoon (personen) met de met het dagelijks bestuur verband 
houdende verantwoordelijkheid voor het uitvoeren van de activiteiten van de entiteit. Voor 
bepaalde entiteiten in sommige rechtsgebieden behoren sommige of alle met governance 
belaste personen tot het management, bijvoorbeeld bij het dagelijks bestuur betrokken 
leden van een governance-orgaan of een eigenaar-bestuurder. 
 
Vereisten 
 
De met governance belaste personen  
 
11. 
De auditor dient te bepalen wie de geschikte persoon (personen) binnen de governance-structuur 
van de entiteit is (zijn) om mee te communiceren. (Zie par. A1-A4) 
 
Het communiceren met een subgroep van de met governance belaste personen 
 
12. 
Indien de auditor met een subgroep van de met governance belaste personen communiceert, 
bijvoorbeeld een auditcomité, of met een individu, dient de auditor te bepalen of het noodzakelijk 
is dat hij eveneens communiceert met de hele groep van met governance belaste personen. (Zie 
par. A5-A7) 
 
Wanneer alle met governance belaste personen betrokken zijn bij het leiden van de entiteit 
 
13. 
In bepaalde gevallen zijn alle met governance belaste personen, betrokken bij het leiden van de 
entiteit, bijvoorbeeld een kleine onderneming waar een enkele eigenaar leiding geeft aan de 
entiteit en niemand anders een rol in het kader van governance vervult. Indien aangelegenheden 
die op grond van deze ISA zijn vereist, worden meegedeeld aan een persoon (personen) met 
leidinggevende verantwoordelijkheden en die persoon (personen) tevens met governance 
verband houdende verantwoordelijkheden heeft (hebben), hoeven in deze gevallen de 
aangelegenheden niet opnieuw te worden meegedeeld aan dezelfde persoon (personen) in zijn 
(hun) rol in het kader van governance. Deze aangelegenheden zijn toegelicht in paragraaf 16(c). 
De auditor dient desalniettemin ervan overtuigd te zijn dat de mededeling die gericht is aan de 
persoon (personen) met leidinggevende verantwoordelijkheden, leidt tot het adequaat informeren 
van al degenen met wie de auditor in andere omstandigheden zou communiceren in hun rol in 
het kader van governance. (Zie par. A8) 
 
Mee te delen aangelegenheden 
 
De verantwoordelijkheden van de auditor met betrekking tot de controle van financiële overzichten 
 
14. 
De auditor dient zijn verantwoordelijkheden met betrekking tot de controle van financiële 
overzichten aan de met governance belaste personen mee te delen, met inbegrip van het feit dat: 
 
(a) 
hij verantwoordelijk is voor het vormen en het tot uitdrukking brengen van een oordeel over 
de financiële overzichten die onder het toezicht van de met governance belaste personen 
door het management zijn opgesteld; en 
(b) 
de controle van de financiële overzichten het management of de met governance belaste 
personen niet ontslaat van hun verantwoordelijkheden. (Zie par. A9-A10) 
 
De geplande reikwijdte en timing van de controle 
 
15. 
De auditor dient een overzicht van de geplande reikwijdte en de timing van de controle aan de 
met governance belaste personen mee te delen, welke de communicatie bevat over de 
significante risico’s die door de auditor zijn geïdentificeerd. (Zie par. A11-A16)

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
7/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Specifieke bevindingen uit de controle 
 
16. 
De auditor dient de volgende aangelegenheden aan de met governance belaste personen mee 
te delen: (Zie par. A17-A18) 
 
(a) 
de zienswijze van de auditor over significante kwalitatieve aspecten met betrekking tot de 
praktijken inzake administratieve verwerking van de entiteit, met inbegrip van de 
grondslagen voor financiële verslaggeving, de schattingen en de in de financiële 
overzichten opgenomen toelichtingen. Indien van toepassing, dient de auditor aan de met 
governance belaste personen uit te leggen waarom hij een significante praktijk inzake 
administratieve verwerking, die aanvaardbaar is overeenkomstig het van toepassing zijnde 
stelsel inzake financiële verslaggeving, niet beschouwt als de meest passende in de 
specifieke omstandigheden van de entiteit; (Zie par. A19-A20) 
(b) 
eventuele significante problemen die zich gedurende de controle hebben voorgedaan; (Zie 
par. A21) 
(c) 
tenzij alle met governance belaste personen betrokken zijn bij het leiden van de entiteit: 
 
(i) 
tijdens de controle aan de orde gekomen significante aangelegenheden die met het 
management werden besproken of onderwerp van correspondentie met het 
management zijn geweest; en (Zie par. A22)  
 
(ii) 
schriftelijke bevestigingen die de auditor heeft gevraagd;  
 
(d) 
eventuele omstandigheden die de vorm en inhoud van de controleverklaring beïnvloeden; 
en (Zie par. A23-A25) 
(e) 
alle andere tijdens de controle aan de orde gekomen significante aangelegenheden die op 
grond van de professionele oordeelsvorming van de auditor relevant zijn voor het toezicht 
op het proces van financiële verslaggeving. (Zie par. A26-A28).  
 
Onafhankelijkheid van de auditor 
 
17. 
Indien het een beursgenoteerde entiteit betreft, dient de auditor het volgende aan de met 
governance belaste personen mee te delen:  
 
(a) 
een verklaring dat het opdrachtteam en, indien passend, andere personen binnen het 
kantoor, het kantoor, en, indien van toepassing, de kantoren die tot het netwerk behoren, 
hebben voldaan aan relevante ethische voorschriften met betrekking tot onafhankelijkheid; 
 
(i) 
alle relaties en andere aangelegenheden tussen het kantoor, de kantoren die tot het 
netwerk behoren en de entiteit waarvan op grond van de professionele 
oordeelsvorming van de auditor redelijkerwijs kan worden verwacht dat zij 
consequenties hebben voor de onafhankelijkheid. Hieronder vallen ook alle 
vergoedingen die gedurende de verslagperiode waarop de financiële overzichten 
betrekking hebben, in rekening zijn gebracht voor op controle en niet op controle 
gerichte diensten die door het kantoor en de tot het netwerk behorende kantoren zijn 
verleend aan de entiteit en aan de groepsonderdelen waarover de entiteit 
zeggenschap heeft. Deze vergoedingen dienen in geschikte categorieën te worden 
ondergebracht om de met governance belaste personen te helpen het effect 
inschatten van de dienstverlening op de onafhankelijkheid van de auditor; en 
(ii) 
de daarmee verband houdende maatregelen die zijn getroffen om de 
geïdentificeerde bedreigingen van de onafhankelijkheid weg te nemen (Zie par. A29-
A32). 
 
Het communicatieproces 
 
Het tot stand brengen van het communicatieproces

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
8/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
18. 
De auditor dient aan de met governance belaste personen de vorm, de timing en de verwachte 
algemene inhoud van de communicatie mee te delen. (Zie par. A37-A45) 
 
Vormen van communicatie 
 
19. 
De auditor dient significante bevindingen uit de controle schriftelijk aan de met governance 
belaste personen mee te delen indien, op grond van de professionele oordeelsvorming van de 
auditor, mondeling communiceren niet adequaat zou zijn. In schriftelijke mededelingen hoeven 
niet alle aangelegenheden te worden opgenomen die in de loop van de controle aan de orde zijn 
gekomen. (Zie par. A46-A48) 
 
20. 
De auditor dient schriftelijk met de met governance belaste personen te communiceren over de 
onafhankelijkheid van de auditor indien dit vereist is op grond van paragraaf 17. 
 
Timing van communicatie 
 
21. 
De auditor dient tijdig met de met governance belaste personen te communiceren. (Zie par. A49-
A50) 
 
De adequaatheid van het communicatieproces 
 
22. 
De auditor dient te evalueren of de wederzijdse communicatie tussen de auditor en de met 
governance belaste personen adequaat is geweest voor het doel van de controle. Indien dat niet 
het geval is geweest, dient de auditor een evaluatie te maken van het eventuele effect daarvan 
op zijn inschatting van de risico’s op een afwijking van materieel belang alsmede op de 
mogelijkheid om voldoende en geschikte controle-informatie te verkrijgen, en dient hij de 
passende actie te ondernemen. (Zie par. A51-A53) 
 
Documentatie 
 
23. 
Wanneer aangelegenheden die overeenkomstig deze ISA dienen te worden meegedeeld, 
mondeling worden meegedeeld, dient de auditor deze in de controledocumentatie op te nemen, 
alsmede het tijdstip waarop en de namen van de personen aan wie ze zijn meegedeeld. Wanneer 
aangelegenheden schriftelijk zijn meegedeeld, dient de auditor een kopie van de mededeling te 
bewaren als onderdeel van de controledocumentatie2. (Zie par. A54) 
 
 
**** 
 
 
Toepassingsgerichte en overige verklarende teksten 
 
De met governance belaste personen (Zie par. 11) 
 
A1. 
Governance-structuren verschillen per rechtsgebied en per entiteit en worden onder meer 
beïnvloed 
door 
verschillende 
culturele 
en 
juridische 
achtergronden, 
omvang 
en 
eigendomskenmerken. Bijvoorbeeld: 
 
• 
in sommige rechtsgebieden bestaat een (geheel of grotendeels niet met het dagelijks 
bestuur belaste) raad van toezicht die wettelijk gescheiden is van een met het dagelijks 
bestuur belaste raad (een dualistische bestuursstructuur). In andere rechtsgebieden 
behoren zowel de toezichthoudende als de met het dagelijks bestuur verband houdende 
 
2  
ISA 230, Controledocumentatie, paragrafen 8-11 en A6.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
9/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
taken tot de wettelijke verantwoordelijkheid van één enkele of een één geheel vormende 
raad (een monistische bestuursstructuur); 
• 
in sommige entiteiten bekleden de met governance belaste personen posities die een 
integrerend onderdeel vormen van de wettelijke structuur van de entiteit, bijvoorbeeld de 
directeuren van vennootschappen. In andere gevallen, bijvoorbeeld voor bepaalde 
entiteiten binnen de overheid, is een instantie die geen deel uitmaakt van de entiteit, belast 
met governance; 
• 
in sommige gevallen zijn enkele of alle met governance belaste personen betrokken bij het 
leiden van de entiteit. In andere gevallen bestaan de met governance belaste personen en 
het management uit verschillende personen. 
• 
in sommige gevallen zijn de met governance belaste personen verantwoordelijk voor het 
goedkeuren3 van de financiële overzichten van de entiteit (in andere gevallen heeft het 
management deze verantwoordelijkheid). 
 
A2. 
In de meeste entiteiten is governance een collectieve verantwoordelijkheid van een groep van 
met governance belaste personen, zoals een raad van bestuur, een raad van toezicht, partners, 
eigenaren, een bestuursdelegatie, een raad van beheerders, bewindvoerders dan wel 
gelijkwaardige personen. In kleinere entiteiten is het echter mogelijk dat één persoon, 
bijvoorbeeld de eigenaar-bestuurder, wanneer er geen andere eigenaren zijn, dan wel één enkele 
bewindvoerder 
belast 
is 
met 
governance. 
Wanneer 
governance 
een 
collectieve 
verantwoordelijkheid is, kan een subgroep zoals een auditcomité of zelfs een individu belast zijn 
met specifieke taken om de groep van met governance belaste personen bij te staan bij het 
nakomen van haar verantwoordelijkheden. Als alternatief kan een subgroep of één enkele 
persoon specifieke, bij wet vastgelegde verantwoordelijkheden dragen die verschillen van die van 
de groep van met governance belaste personen. 
 
A3. 
Een dergelijke diversiteit betekent dat het niet mogelijk is om in deze ISA voor alle controles de 
persoon (personen) te specificeren aan wie de auditor bepaalde aangelegenheden moet 
meedelen. Tevens is het mogelijk dat in sommige gevallen de geschikte personen om mee te 
communiceren niet duidelijk te bepalen zijn aan de hand van het van toepassing zijnde juridische 
kader of aan de hand van andere omstandigheden met betrekking tot de opdracht, bijvoorbeeld 
bij entiteiten waar de governance-structuur niet formeel is vastgelegd, zoals bij sommige 
familiebedrijven, sommige non-profitorganisaties alsmede sommige entiteiten binnen de 
overheid. In dergelijke gevallen kan het voor de auditor noodzakelijk zijn om met de 
opdrachtgevende partij te bespreken en overeen te komen met welke relevante persoon 
(personen) moet worden gecommuniceerd. Bij het bepalen van de personen met wie moet 
worden gecommuniceerd, is het inzicht van de auditor in de governance-structuur en –processen 
van een entiteit, dat is verworven in overeenstemming met ISA 315 (herzien)4, relevant. De 
geschikte persoon (personen) om mee te communiceren kan (kunnen) verschillen afhankelijk van 
de aangelegenheid waarover moet worden gecommuniceerd. 
 
A4. 
ISA 600 bevat specifieke aangelegenheden die door de groepsauditors aan de met governance 
belaste personen moeten worden meegedeeld5. Indien de entiteit een onderdeel uitmaakt van 
een groep, is (zijn) voor de auditor van het groepsonderdeel de geschikte persoon (personen) om 
mee te communiceren, afhankelijk van de omstandigheden van de opdracht en van de 
aangelegenheid waarover moet worden gecommuniceerd. In sommige gevallen kan een aantal 
groepsonderdelen dezelfde activiteiten uitvoeren binnen hetzelfde systeem van interne 
beheersing en dezelfde praktijken inzake administratieve verwerking hanteren. Wanneer de met 
governance belaste personen van deze groepsonderdelen dezelfde zijn (bijv. een 
 
3  
Zoals uiteengezet in paragraaf A68 van ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële 
overzichten, betekent “het hebben van de verantwoordelijkheid voor het goedkeuren” in deze context “het hebben van de 
bevoegdheid om vast te stellen dat alle overzichten waaruit de financiële overzichten bestaan, met inbegrip van de daarmee 
verband houdende toelichtingen, zijn opgesteld”. 
4  
ISA 315 (herzien 2019), Risico’s op een afwijking van materieel belang identificeren en inschatten. 
5  
ISA 600, Bijzondere overwegingen – Controles van financiële overzichten van een groep (inclusief de werkzaamheden van 
auditors van groepsonderdelen), paragraaf 49.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
10/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
gemeenschappelijke raad van bestuur) kan overlapping worden voorkomen door in het kader van 
de communicatie deze groepsonderdelen gezamenlijk te behandelen. 
 
Communiceren met een subgroep van de met governance belaste personen (Zie par. 12) 
 
A5. 
Wanneer de auditor overweegt om met een subgroep van de met governance belaste personen 
te communiceren, kan hij rekening houden met aangelegenheden als: 
 
• 
de respectievelijke verantwoordelijkheden van deze subgroep en van de groep van met 
governance belaste personen; 
• 
de aard van de aangelegenheid die moet worden meegedeeld; 
• 
relevante door wet- of regelgeving gestelde vereisten; 
• 
de vraag of deze subgroep de bevoegdheid heeft om actie te ondernemen met betrekking 
tot de meegedeelde informatie, en verdere informatie en uitleg kan geven die de auditor 
nodig kan hebben. 
 
A6. 
In zijn beslissing of er een noodzaak bestaat om informatie volledig of in de vorm van een 
samenvatting aan de groep van met governance belaste personen mee te delen, kan de auditor 
worden beïnvloed door zijn inschatting van de effectiviteit en de geschiktheid van de wijze waarop 
de subgroep relevante informatie aan de groep van met governance belaste personen meedeelt. 
De auditor kan bij de overeenstemming over de opdrachtvoorwaarden op expliciete wijze stellen 
dat hij zich, tenzij dit door wet- of regelgeving is verboden, het recht voorbehoudt om op directe 
wijze met de groep van met governance belaste personen te communiceren. 
 
A7. 
Auditcomités (of gelijksoortige subgroepen met andere namen) bestaan in veel rechtsgebieden. 
Hoewel de specifieke bevoegdheden en functies daarvan zouden kunnen verschillen, is 
communiceren met het auditcomité, wanneer dit bestaat, een essentieel aspect geworden van 
de communicatie van de auditor met de met governance belaste personen. De beginselen van 
goede governance veronderstellen dat: 
 
• 
de auditor zal worden uitgenodigd om regelmatig vergaderingen van het auditcomité bij te 
wonen; 
• 
de voorzitter van het auditcomité en, wanneer dit relevant is, de andere leden van het 
auditcomité regelmatig contact onderhouden met de auditor; 
• 
het auditcomité ten minste eenmaal per jaar met de auditor zal vergaderen zonder de 
aanwezigheid van het management. 
 
Gevallen waarin alle met governance belaste personen betrokken zijn bij het leiden van de entiteit (Zie 
par. 13) 
 
A8. 
In sommige situaties zijn alle met governance belaste personen betrokken bij het leiden van de 
entiteit en wordt de toepassing van de communicatievereisten aan deze situatie aangepast. In 
dergelijke gevallen is het mogelijk dat bij het communiceren met de persoon (personen) met 
leidinggevende verantwoordelijkheden niet alle personen met wie de auditor in andere 
omstandigheden in hun governance-functie zou communiceren, op adequate wijze worden 
geïnformeerd. Wanneer bijvoorbeeld in een vennootschap alle bestuurders zijn betrokken bij het 
leiden van de entiteit, is het mogelijk dat sommige bestuurders (bijv.  degene die verantwoordelijk 
is voor marketing) niet op de hoogte zijn van significante aangelegenheden die met een andere 
bestuurder zijn besproken (bijv.  degene die verantwoordelijk is voor het opstellen van de 
financiële overzichten). 
 
Mee te delen aangelegenheden 
 
De verantwoordelijkheden van de auditor met betrekking tot de controle van financiële overzichten (Zie 
par. 14)

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
11/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A9. 
De verantwoordelijkheden van de auditor met betrekking tot de controle van financiële 
overzichten worden dikwijls vermeld in de opdrachtbrief of in een andere passende vorm van een 
schriftelijke 
overeenkomst 
waarin 
de 
overeengekomen 
opdrachtvoorwaarden 
worden 
vastgelegd6. Wet- en regelgeving of de governance-structuur van de entiteit kan van de met 
governance belaste personen vereisen dat zij met de auditor overeenstemming bereiken over de 
voorwaarden van de opdracht. Wanneer dit niet het geval is kan het verstrekken van een kopie 
van deze opdrachtbrief of een andere geschikte vorm van een schriftelijke overeenkomst aan de 
met governance belaste personen kan een passende manier zijn om met hen te communiceren 
over aangelegenheden als: 
 
• 
de verantwoordelijkheden van de auditor voor het uitvoeren van de controle 
overeenkomstig de ISA’s, die gericht is op het tot uitdrukking brengen van een oordeel over 
de financiële overzichten. Daarom omvatten de aangelegenheden die overeenkomstig de 
ISA’s dienen te worden meegedeeld, onder meer de significante aangelegenheden die 
tijdens de controle van de financiële overzichten aan de orde zijn gekomen en die relevant 
zijn voor de met governance belaste personen om toezicht uit te oefenen op het proces 
van financiële verslaggeving; 
• 
het feit dat de ISA’s niet vereisen dat de auditor specifieke werkzaamheden opzet om te 
bepalen welke aanvullende aangelegenheden aan de met governance belaste personen 
moeten worden meegedeeld; 
• 
als ISA 7017 van toepassing is, de verantwoordelijkheden van de auditor om kernpunten 
van de controle te bepalen en te communiceren in de controleverklaring; 
• 
indien van toepassing, de verantwoordelijkheid van de auditor voor het meedelen van 
specifieke aangelegenheden die vereist zijn op grond van wet- of regelgeving, op grond 
van afspraken met de entiteit of op grond van aanvullende vereisten die van toepassing 
zijn op de opdracht, bijvoorbeeld de standaarden van een nationale beroepsorganisatie 
voor accountancy. 
 
A10. Bij wet- of regelgeving, een overeenkomst met de entiteit dan wel aanvullende vereisten die op 
de opdracht van toepassing zijn, kan een ruimere communicatie met de met governance belaste 
personen zijn voorgeschreven. Als voorbeelden zijn te noemen, (a) een overeenkomst met de 
entiteit kan bepalen dat specifieke aangelegenheden moeten worden meegedeeld wanneer zij 
aan de orde komen bij andere diensten dan de controle van financiële overzichten die worden 
verleend door een kantoor of een kantoor dat tot het netwerk behoort; of (b) de opdracht van een 
auditor in de publieke sector kan bepalen dat aangelegenheden moeten worden meegedeeld die 
onder de aandacht van de auditor komen als gevolg van andere werkzaamheden, zoals 
doelmatigheidscontroles. 
 
De geplande reikwijdte en timing van de controle (Zie par. 15) 
 
A11. Communicatie met betrekking tot de geplande reikwijdte en timing van de controle kan: 
 
(a) 
de met governance belaste personen helpen de gevolgen van het werk van de auditor 
beter te begrijpen, kwesties inzake risico en het begrip materialiteit met de auditor te 
bespreken, alsmede te bepalen op welke gebieden deze personen aan de auditor kunnen 
vragen aanvullende werkzaamheden te verrichten; en 
(b) 
de auditor helpen de entiteit en haar omgeving beter te begrijpen. 
 
A12. Het communiceren van significante risico’s die door de auditor zijn geïdentificeerd helpt de met 
governance belaste personen om die aangelegenheden en de reden waarom zij vastgesteld zijn 
als significante risico’s te begrijpen. De communicatie over significante risico’s kan de met 
governance belaste personen helpen bij het vervullen van hun verantwoordelijkheid om toezicht 
uit te oefenen op het proces van financiële verslaggeving. 
 
 
6  
ISA 210, Het overeenkomen van de voorwaarden van controleopdrachten, paragraaf 10. 
7  
ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijke auditor.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
12/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A13. Aangelegenheden die worden meegedeeld, zijn onder meer: 
 
• 
de wijze waarop de auditor plant om in te spelen op de significante risico’s op een afwijking 
van materieel belang als gevolg van fraude of fouten; 
• 
de wijze waarop de auditor plant om in te spelen op gebieden met een hoger ingeschat 
risico op een afwijking van materieel belang; 
• 
de wijze waarop de auditor de voor het systeem van interne beheersing van de entiteit 
benadert; 
• 
het toepassen van het begrip materialiteit in de context van een controle8; 
• 
de aard en omvang van specialistische vaardigheden of kennis die noodzakelijk zijn om de 
geplande controlewerkzaamheden uit te voeren of om de controleresultaten te evalueren, 
inclusief het gebruik van een door de auditor ingeschakelde deskundige9; 
• 
als ISA 701 van toepassing is, de voorlopige visie van de auditor over aangelegenheden 
die bij de controle significante aandacht van de auditor vereisen en derhalve kernpunten 
van de controle kunnen zijn; 
• 
de geplande aanpak van de auditor om de gevolgen te behandelen voor de afzonderlijke 
overzichten en de toelichtingen van alle belangrijke wijzigingen in het van toepassing zijnde 
stelsel inzake financiële verslaggeving of in de omgeving van de entiteit, de financiële 
toestand of activiteiten. 
 
A14. Andere planningsaangelegenheden die passend kunnen zijn om met de met governance belaste 
personen te bespreken, zijn onder meer: 
 
• 
wanneer de entiteit beschikt over een interne auditfunctie, de manier waarop de auditors 
en de interne auditors het beste op een constructieve en elkaar aanvullende wijze kunnen 
samenwerken, inclusief eventueel gepland gebruik van de werkzaamheden van de interne 
auditfunctie en de aard en mate van elk gepland gebruikmaken van de interne auditors om 
directe ondersteuning te verlenen10; 
• 
de zienswijzen van de met governance belaste personen over: 
 
o 
de geschikte persoon (personen) binnen de governance-structuur om mee te 
communiceren; 
o 
de verdeling van de verantwoordelijkheden tussen de met governance belaste 
personen en het management; 
o 
de doelstellingen en strategieën van de entiteit, alsmede de daarmee verband 
houdende bedrijfsrisico's die kunnen leiden tot afwijkingen van materieel belang; 
o 
aangelegenheden die volgens de met governance belaste personen tijdens de 
controle bijzondere aandacht vereisen, alsmede de eventuele gebieden waarop zij 
om aanvullende werkzaamheden verzoeken; 
o 
significante communicatie tussen de entiteit en regelgevende of toezichthoudende 
instanties andere aangelegenheden die volgens de met governance belaste 
personen van invloed zijn op de controle van de financiële overzichten; 
 
• 
de houding, de kennis en de acties van de met governance belaste personen met 
betrekking tot (a) de interne beheersing van de entiteit en het belang daarvan binnen de 
entiteit, met inbegrip van de wijze waarop de met governance belaste personen toezicht 
houden op de effectiviteit van de interne beheersing; en (b) het detecteren van fraude of 
de mogelijkheid van fraude; 
 
• 
de acties van de met governance belaste personen die inspelen op ontwikkelingen in 
financiële verslaggevingsstandaarden, praktijken inzake corporate governance, regels 
inzake beursnoteringen, alsmede daaraan gerelateerde aangelegenheden en het effect 
 
8  
ISA 320, Materialiteit bij planning en uitvoering van een controle. 
9  
Zie ISA 620, Gebruikmaken van de werkzaamheden van een door de auditor ingeschakelde deskundige. 
10  ISA 610 (herzien 2013), Gebruikmaken van de werkzaamheden van interne auditors, paragrafen 20 en 31.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
13/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
van dergelijke ontwikkelingen op, bijvoorbeeld de algehele presentatie, structuur en inhoud 
van de financiële overzichten, waaronder: 
 
o 
de relevantie, betrouwbaarheid, vergelijkbaarheid en begrijpelijkheid van de 
informatie die gepresenteerd wordt in de financiële overzichten informatie; en 
o 
overwegen of de financiële overzichten worden ondermijnd door de opname van 
informatie die niet relevant is of die een goed begrip van de toegelichte 
aangelegenheden verhult. 
 
• 
de reacties van de met governance belaste personen op eerdere mededelingen van de 
auditor; 
• 
de documenten die de andere informatie vormen (zoals gedefinieerd in ISA 720 (herzien)) 
en de geplande wijze en timing van de publicatie van dergelijke documenten. Wanneer de 
auditor verwacht andere informatie te verkrijgen na de datum van de controleverklaring, 
kunnen besprekingen met de personen belast met governance ook de maatregelen 
omvatten die passend of noodzakelijk kunnen zijn als de auditor concludeert dat er een 
afwijking van materieel belang in de andere informatie bestaat in andere informatie die is 
verkregen na de datum van de controleverklaring. 
 
A15. Hoewel de communicatie met de met governance belaste personen de auditor kan helpen de 
reikwijdte en tijdfasering van de controle plannen, doet zij niets af aan de ongedeelde 
verantwoordelijkheid van de auditor om de algehele controleaanpak voor de opdracht en het 
controleprogramma vast te stellen, met inbegrip van de aard, timing en omvang van de 
werkzaamheden die noodzakelijk zijn om voldoende en geschikte controle-informatie te 
verkrijgen. 
 
A16. Om de effectiviteit van de controle niet in het gedrang te brengen, is voorzichtigheid nodig 
wanneer met de met governance belaste personen wordt gecommuniceerd over de geplande 
reikwijdte en timing van de controle, met name wanneer sommige of alle met governance belaste 
personen betrokken zijn bij het leiden van de entiteit. Zo kan communicatie over de aard en timing 
van gedetailleerde controlewerkzaamheden deze te voorspelbaar maken en bijgevolg ten koste 
gaan van de effectiviteit ervan. 
 
Significante bevindingen uit de controle (Zie par. 16) 
 
A17. Het meedelen van bevindingen uit de controle kan inhouden dat de met governance belaste 
personen om verdere informatie wordt verzocht teneinde de verkregen controle-informatie aan te 
vullen. De auditor kan bijvoorbeeld vaststellen dat de met governance belaste personen hetzelfde 
inzicht als de auditor hebben in de feiten en omstandigheden die betrekking hebben op specifieke 
transacties en gebeurtenissen. 
 
A18. Als ISA 701 van toepassing is, zijn zowel de communicatie met de met governance belaste 
personen zoals vereist op basis van paragraaf 16, als de communicatie over de significante 
risico’s die door de auditor zijn geïdentificeerd zoals vereist op basis van paragraaf 15, in het 
bijzonder van belang voor de bepaling door de auditor van aangelegenheden die significante 
aandacht van de auditor vereisten en die derhalve kernpunten van de controle kunnen zijn11.  
 
Significante kwalitatieve aspecten van praktijken inzake administratieve verwerking (Zie Par 16(a)) 
 
A19. Stelsels inzake financiële verslaggeving bieden de entiteit gewoonlijk de mogelijkheid om 
schattingen te maken, alsmede oordeelsvormingen te maken met betrekking tot de grondslagen 
voor financiële verslaggeving en de in de financiële overzichten opgenomen toelichtingen, 
bijvoorbeeld met betrekking tot het gebruik van veronderstellingen bij het ontwikkelen van 
schattingen. Bovendien kunnen wet- en regelgeving of stelsels inzake financiële verslaggeving 
de toelichting van een samenvatting van significante grondslagen voor de financiële 
 
11  ISA 701, paragrafen 9-10.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
14/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
verslaggeving vereisen of verwijzen naar ”kritieke schattingen” of “kritieke grondslagen voor de 
financiële verslaggeving en praktijken inzake administratieve verwerking” om aanvullende 
informatie te identificeren en deze aan gebruikers te verschaffen inzake de moeilijkste, de meest 
subjectieve of de meest complexe oordeelsvormingen die door het management zijn gemaakt bij 
het opstellen van de financiële overzichten.  
 
A20. Als gevolg daarvan kunnen de opvattingen van de auditor over de subjectieve aspecten van de 
financiële overzichten in het bijzonder relevant zijn voor de met governance belaste personen bij 
het vervullen van hun verantwoordelijkheden voor het toezicht op het proces van financiële 
verslaggeving. Met betrekking tot aangelegenheden die bijvoorbeeld in paragraaf A19 worden 
beschreven kunnen de met governance belaste personen interesse hebben in de visie van de 
auditor over de mate waarin complexiteit, subjectiviteit of andere inherente risicofactoren van 
invloed zijn op de keuze of toepassing van de methoden, veronderstellingen en gegevens die 
worden gebruikt bij het maken van een significante schatting, evenals de evaluatie door de auditor 
of de puntschatting van het management en toelichtingen daarop in de financiële overzichten 
redelijk zijn in de context van het van toepassing zijnde stelsel inzake financiële verslaggeving. 
Open en constructieve communicatie over significante kwalitatieve aspecten van de praktijken 
inzake administratieve verwerking en de kwaliteit van de toelichtingen. Dit kan omvatten, indien 
van toepassing, of een significante praktijk van de entiteit inzake administratieve verwerking met 
betrekking tot schattingen door de auditor als niet de meest geschikte wordt beschouwd voor de 
specifieke omstandigheden van de entiteit. Bijvoorbeeld wanneer een alternatieve aanvaardbare 
methode voor het maken van een schatting naar het oordeel van de auditor meer geschikt zou 
zijn. Bijlage 2 identificeert aangelegenheden die in deze communicatie kunnen worden 
opgenomen. 
 
Significante problemen die zich gedurende de controle voordoen (Zie par. 16(b)). 
 
A21. Significante problemen die zich gedurende de controle voordoen, kunnen aangelegenheden 
inhouden zoals:  
 
• 
Significante vertraging door het management, het niet beschikbaar zijn van het personeel 
van de entiteit, of het niet bereid zijn van het management om informatie te verstrekken die 
de auditor nodig heeft om de controlewerkzaamheden uit te voeren; 
• 
Een onnodig korte tijd waarin de controle moet worden voltooid; 
• 
Onverwacht veel benodigde moeite om voldoende en geschikte controle -informatie te 
verkrijgen; 
• 
Het niet beschikbaar zijn van verwachte informatie; 
• 
Beperkingen die door het management aan de auditor worden opgelegd; 
• 
Het niet bereid zijn van het management, wanner daarom wordt gevraagd, tot het maken 
of uitbreiden van zijn inschatting van de mogelijkheid van de entiteit om haar continuïteit te 
waarborgen.  
 
In sommige situaties kunnen dergelijke problemen een beperking van de reikwijdte van de 
controle vormen die leidt tot een aanpassing van het oordeel van de auditor leidt12. 
 
Significante aangelegenheden die met het management zijn besproken onderwerp van correspondentie 
zijn geweest (Zie par. 16(c)(i)). 
 
A22. Significante aangelegenheden die met het management zijn besproken of onderwerp van 
correspondentie zijn geweest, kunnen onder meer zijn:  
 
• 
Significante gebeurtenissen of transacties die zich tijdens het jaar hebben voorgedaan; 
 
12  ISA 705 (herzien), Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
15/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
• 
Zakelijke omstandigheden die de activiteiten van de entiteit beïnvloeden, alsmede 
bedrijfsplannen en strategieën die van invloed kunnen zijn op de risico’s op een afwijking 
van materieel belang; 
• 
Punten van zorg over het raadplegen door het management van andere auditors inzake 
aangelegenheden op het gebied van financiële verslaggeving en controle; 
• 
Besprekingen of correspondentie in samenhang met het verstrekken van de eerste of 
doorlopende opdracht aan de auditor die betrekking hebben op praktijken inzake 
administratieve verwerking, het toepassen van controlestandaarden dan wel vergoedingen 
in verband met control- en andere verleende diensten; 
• 
Significante aangelegenheden waarover met het management een meningsverschil 
bestond, behalve voor aanvankelijke verschillen van mening als gevolg van onvolledigheid 
van de feiten of de voorlopige informatie die later zijn opgelost doordat de auditor 
aanvullende relevante feiten of informatie verkreeg. 
 
Omstandigheden die de vorm en inhoud van de controleverklaring beïnvloeden (Zie Par 16(d)) 
 
A23. ISA 210 vereist van de auditor het overeenkomen van de voorwaarden van de controleopdracht, 
met het management of de met governance belaste personen, naar gelang passend13. Het is 
vereist dat de overeengekomen voorwaarden van de controleopdracht worden opgenomen in een 
opdrachtbevestiging of andere geschikte vorm van een schriftelijke overeenkomst en omvat 
onder meer een verwijzing naar de verwachte vorm en inhoud van de controleverklaring14. Zoals 
is uitgelegd in paragraaf A9, kan de auditor de met governance belaste personen een kopie van 
de opdrachtbevestiging overhandigen om te kunnen communiceren over aangelegenheden die 
voor de controle relevant zijn, indien de voorwaarden van de opdracht niet met de met 
governance belaste personen overeen zijn gekomen. De communicatie die op grond van 
paragraaf 16(d) is vereist, is bedoeld om de met governance belaste personen te informeren over 
omstandigheden waarin de controleverklaring kan afwijken van zijn verwachte vorm en inhoud of 
wanneer deze aanvullende informatie bevat over de controle die was uitgevoerd. 
 
A24. Omstandigheden waarin van de auditor vereist is of dat hij het anderszins noodzakelijk kan achten 
om in de controleverklaring aanvullende informatie op te nemen overeenkomstig de ISA’s, en 
waarvoor communicatie met de met governance belaste personen vereist is, omvatten 
omstandigheden waarin:  
 
• 
De auditor verwacht zijn oordeel in de controleverklaring aan te passen overeenkomstig 
ISA 705 (herzien)15; 
• 
Een materiële onzekerheid die verband houdt met continuïteit is gerapporteerd 
overeenkomstig ISA 570 (herzien)16; 
• 
Kernpunten van de controle worden gecommuniceerd overeenkomstig ISA 70117; 
• 
De auditor het noodzakelijk acht om overeenkomstig ISA 706 (herzien)18 een paragraaf ter 
benadrukking van bepaalde aangelegenheden of een paragraaf inzake overige 
aangelegenheden in de controleverklaring op te nemen, of hij op grond van andere ISA’s 
vereist is dit te doen; 
• 
De auditor heeft geconcludeerd dat er een ongecorrigeerde afwijking van materieel belang 
is in de andere informatie in overeenstemming met ISA 720 (herzien)19. 
 
 
13  ISA 210, paragraaf 9. 
14  ISA 210, paragraaf 10. 
15  ISA 705 (herzien), paragraaf 30. 
16  ISA 570, (herzien), Continuïteit, paragraaf 25(d). 
17  ISA 701, paragraaf 17. 
18  ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor, paragraaf 12. 
19  ISA 720 (herzien), De verantwoordelijkheden van de accountant met betrekking tot andere informatie, paragraaf 18(a).

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
16/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
In dergelijke omstandigheden kan de auditor het nuttig achten om aan de met governance belaste 
personen een concept van de controleverklaring te verstrekken als hulpmiddel bij de bespreking 
van de wijze waarop er op dergelijke aangelegenheden in de controleverklaring wordt ingespeeld. 
 
A25. In de zeldzame omstandigheden dat de auditor voornemens is om de naam van de 
opdrachtpartner niet op te nemen in de controleverklaring overeenkomstig ISA 700 (herzien), is 
van de auditor vereist om deze intentie te bespreken met de met governance belaste personen 
om de inschatting door de auditor van de waarschijnlijkheid en ernst van een significante 
persoonlijke bedreiging van de veiligheid te vormen.20 De auditor kan tevens met de met 
governance belaste personen communiceren in het geval dat de auditor ervoor kiest geen 
beschrijving van de verantwoordelijkheden van de auditor op te nemen in de tekst van de 
controleverklaring zoals op grond van ISA 700 (herzien) is toegestaan21.  
 
Andere significante aangelegenheden die relevant zijn voor het financiële verslaggevingsproces (Zie 
par. 16(e)) 
 
A26. ISA 30022 geeft aan dat, als gevolg van onverwachte gebeurtenissen, wijzigingen in voorwaarden 
of de controle-informatie die is verkregen uit resultaten van controlewerkzaamheden, het nodig 
kan zijn dat de auditor de algehele controleaanpak en het controleprogramma aanpast en 
derhalve de resulterende aard, timing en omvang van verdere controlewerkzaamheden, op basis 
van de herziene overweging van ingeschatte risico’s. De auditor kan dergelijke aangelegenheden 
met de governance belaste personen communiceren, bijvoorbeeld als een actualisering van 
aanvankelijke besprekingen over de geplande reikwijdte en timing van de controle. 
 
A27. Andere significante aangelegenheden die tijdens de controle aan de orde komen en die direct 
relevant zijn voor de met governance belaste personen bij hun toezicht op het proces van 
financiële verslaggeving kunnen aangelegenheden zoals afwijkingen van materieel belang in de 
andere informatie die gecorrigeerd zijn, omvatten. 
 
A28. Voor de mate waarin dit niet reeds door de vereisten in paragrafen 16(a)-(d) en gerelateerde 
toepassingsgerichte teksten is behandeld, kan de auditor overwegen te communiceren over 
andere aangelegenheden die met de opdrachtgerichte kwaliteitsbeoordelaar, indien er een is 
aangesteld, zijn besproken of door deze onder de aandacht zijn gebracht. 
 
Onafhankelijkheid van de auditor (Zie par. 17) 
 
A29. Van de auditor wordt vereist dat hij voldoet aan relevante ethische voorschriften, voor opdrachten 
inzake de controle van financiële overzichten, met inbegrip van die betreffende 
onafhankelijkheid23.  
 
A30. De relaties en andere aangelegenheden, alsmede de maatregelen die moeten worden 
meegedeeld, zijn afhankelijk van de omstandigheden van de opdracht, maar hebben in het 
algemeen betrekking op: 
 
(a) 
Bedreigingen voor de onafhankelijkheid die kunnen worden onderverdeeld in: bedreigingen 
als gevolg van eigenbelang, bedreigingen als gevolg van zelftoetsing, bedreigingen als 
gevolg van belangenbehartiging, bedreiging als gevolg van vertrouwdheid en bedreiging 
als gevolg van intimidatie; en 
(b) 
Maatregelen die door het beroep, de wet- of regelgeving tot stand zijn gebracht, 
maatregelen binnen de entiteit en maatregelen binnen de systemen en procedures van het 
kantoor zelf.  
 
20  ISA 700 (herzien), paragrafen 46 en A63. 
21  ISA 700 (herzien), paragraaf 41. 
22  ISA 300, Planning van een controle van financiële overzichten, paragraaf A15. 
23  ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de 
International Standards on Auditing, paragraaf 14.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
17/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
A31. Relevante ethische voorschriften of wet- of regelgeving kunnen ook bepaalde mededelingen aan 
de met governance belaste personen specificeren in omstandigheden waar overtredingen van 
onafhankelijkheidsvereisten zijn geïdentificeerd. De International Federation of Accountants’ 
Code of Ethics for Professional Accountants (de IESBA Code) bijvoorbeeld, vereist van de auditor 
om met de met governance belaste personen schriftelijk overtredingen en de maatregelen die het 
kantoor heeft genomen en voornemens is te nemen, mee te delen24. 
 
A32. De communicatievereisten met betrekking tot de onafhankelijkheid van de auditor die van 
toepassing zijn op beursgenoteerde entiteiten, kunnen ook geschikt zijn voor bepaalde andere 
entiteiten, inclusief die entiteiten die van significant openbaar belang kunnen zijn, bijvoorbeeld 
omdat zij  een groot aantal en een breed scala aan belanghebbenden hebben en gezien de aard 
en omvang van het bedrijf. Voorbeelden van dergelijke entiteiten kunnen financiële instellingen 
omvatten (zoals banken, verzekeringsmaatschappijen en pensioenfondsen), en andere entiteiten 
zoals charitatieve instellingen. Er kunnen echter ook situaties bestaan waarin communicatie over 
onafhankelijkheid mogelijk niet relevant is, bijvoorbeeld wanneer alle met governance belaste 
personen op grond van hun leidinggevende activiteiten zijn geïnformeerd over de betrokken 
feiten. Dit is bijzonder waarschijnlijk wanneer de entiteit wordt geleid door de eigenaar, alsmede 
wanneer het kantoor van de auditor en de kantoren die tot het netwerk behoren, naast de controle 
van de financiële overzichten weinig bij de entiteit betrokken zijn.  
 
Aanvullende aangelegenheden (Zie par. 3) 
 
A33. Het door de met governance belaste personen uitgeoefende toezicht op het management houdt 
onder meer in dat erop wordt toegezien dat de entiteit een interne beheersing opzet, 
implementeert en onderhoudt met betrekking tot de betrouwbaarheid van de financiële 
verslaggeving, de effectiviteit en doelmatigheid van haar activiteiten alsmede het naleven van de 
toepassing zijnde wet- en regelgeving. 
 
A34. De auditor kan zich bewust worden van aanvullende aangelegenheden die niet 
noodzakelijkerwijze verband houden met het toezicht op het proces van financiële verslaggeving 
maar die niettemin naar alle waarschijnlijkheid significant zijn voor de verantwoordelijkheden van 
de met governance belaste personen bij het toezicht houden op de strategische richting of de 
verantwoordingsplicht van de entiteit. Dergelijke aangelegenheden zijn bijvoorbeeld kwesties 
inzake governance-structuren en -processen, alsmede significante beslissingen of acties van het 
senior management waarvoor de passende autorisatie ontbreekt. 
 
A35. Bij het bepalen of aanvullende aangelegenheden moeten worden meegedeeld aan de met 
governance belaste personen, kan de auditor dit soort aangelegenheden die hem ter kennis zijn 
gekomen, bespreken met het management op het passende verantwoordelijkheidsniveau, tenzij 
het in de gegeven omstandigheden niet passend is om dit te doen. 
 
A36. Indien een aanvullende aangelegenheid wordt meegedeeld, kan het passend zijn dat de auditor 
de met governance belaste personen ervan op de hoogte stelt dat: 
 
(a) 
het identificeren en meedelen van dergelijke aangelegenheden ondergeschikt is aan het 
doel van de controle, namelijk het tot uitdrukking brengen van een oordeel over de 
financiële overzichten; 
(b) 
er geen andere werkzaamheden zijn uitgevoerd met betrekking tot deze aangelegenheid 
dan die welke noodzakelijk waren om een oordeel over de financiële overzichten te 
vormen; en 
(c) 
er geen werkzaamheden zijn uitgevoerd om vast te stellen of vergelijkbare 
aangelegenheden bestaan. 
 
 
24  Zie Secties R400.80-R400.82 en R400.81 van de IESBA Code, die het overtreden van de onafhankelijkheidsvereisten 
behandelen.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
18/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Het communicatieproces 
 
Het tot stand brengen van het communicatieproces (Zie par. 18) 
 
A37. Het duidelijk meedelen van de verantwoordelijkheden van de auditor, de geplande reikwijdte en 
timing van de controle, alsmede van de verwachte algemene inhoud van de communicatie helpt 
een basis te leggen voor een effectieve wederzijdse communicatie. 
 
A38. Aangelegenheden waarvan de bespreking eveneens kan bijdragen aan een effectieve 
wederzijdse communicatie, zijn onder meer: 
 
• 
het doel van de communicatie. Wanneer het doel duidelijk is, zijn de auditor en de met 
governance belaste personen in een betere positie om hetzelfde begrip te hebben van 
relevante kwesties en van te verwachten acties die uit het communicatieproces 
voortkomen; 
• 
de vorm waarin de communicatie zal plaatsvinden; 
• 
het lid (de leden) van het opdrachtteam en de met governance belaste persoon (personen) 
die over specifieke aangelegenheden zullen communiceren; 
• 
de verwachting van de auditor dat de communicatie wederzijds zal zijn en dat de met 
governance belaste personen aangelegenheden die zij voor de controle als relevant 
beschouwen, aan de auditor zullen meedelen, bijvoorbeeld de strategische beslissingen 
die een significante invloed kunnen hebben op de aard, timing en omvang van 
controlewerkzaamheden, het vermoeden of detecteren van fraude, en punten van zorg 
over de integriteit of competenties van het senior management; 
• 
het te volgen proces van actie ondernemen en terug rapporteren inzake aangelegenheden 
die de auditor heeft meegedeeld; 
• 
het te volgen proces van action ondernemen en terug rapporteren inzake 
aangelegenheden door de met governance belaste personen. 
 
A39. Het communicatieproces zal afhangen van de omstandigheden, met inbegrip van de omvang en 
de governance-structuur van de entiteit, van de wijze waarop de met governance belaste 
personen te werk gaan, alsmede van de visie van de auditor op de significantie van mee te delen 
aangelegenheden. Problemen bij het opzetten van een effectieve wederzijdse communicatie 
kunnen erop wijzen dat de communicatie tussen de auditor en de met governance belaste 
personen niet adequaat is voor het doel van de controle. (Zie par. A52) 
 
Overwegingen die specifiek voor de kleine entiteiten gelden  
 
A40. Bij controles van kleinere entiteiten kan de auditor op een minder gestructureerde wijze 
communiceren met de met governance belaste personen dan indien het beursgenoteerde of 
grotere entiteiten betreft. 
 
Communicatie met het management 
 
A41. Veel aangelegenheden kunnen tijdens het normale verloop van de controle met het management 
worden besproken, met inbegrip van aangelegenheden die deze ISA vereist aan de met 
governance belaste personen mee te delen. Bij dergelijke besprekingen wordt rekening 
gehouden met de met het dagelijks bestuur verband houdende verantwoordelijkheid van het 
management voor de uitoefening van de activiteiten van de entiteit en met name met de 
verantwoordelijkheid van het management voor het opstellen van de financiële overzichten. 
 
A42. Alvorens aangelegenheden mee te delen aan de met governance belaste personen, kan de 
auditor deze met het management bespreken, tenzij dit niet passend is. Zo is het mogelijk niet 
passend vragen over de competenties en de integriteit van het management met het 
management zelf te bespreken. Deze voorafgaande besprekingen houden niet alleen een 
erkenning in van de met het dagelijks bestuur verband houdende verantwoordelijkheid van het

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
19/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
management, maar kunnen ook duidelijkheid brengen over bepaalde feiten en kwesties en het 
management de gelegenheid bieden verdere informatie en uitleg te verschaffen. Op gelijksoortige 
wijze kan de auditor, wanneer de entiteit beschikt over een interne auditfunctie, aangelegenheden 
met de interne auditor bespreken alvorens deze aan de met governance belaste personen mee 
te delen. 
 
Communicatie met derden  
 
A43. Het is mogelijk dat de met governance belaste personen verplicht zijn door wet- of regelgeving of 
dat zij wensen om kopieën van een schriftelijke mededeling van de auditor te verstrekken aan 
derden, bijvoorbeeld aan bankiers of aan bepaalde regelgevende of toezichthoudende instanties. 
In sommige gevallen kan het verstrekken van deze informatie aan derden onwettig of anderszins 
ongepast zijn. Wanneer een schriftelijke mededeling die is opgesteld ten behoeve van de met 
governance belaste personen, aan derden wordt verstrekt, kan het in de gegeven 
omstandigheden belangrijk zijn dat deze derden ervan op de hoogte worden gesteld dat deze 
mededeling niet ten behoeve van hen werd opgesteld door bijvoorbeeld in de schriftelijke, aan de 
met governance belaste personen gerichte mededelingen te vermelden: 
 
(a) 
dat de mededeling is opgesteld om alleen door de met governance belaste personen te 
worden gebruikt en, indien van toepassing, door het management op groepsniveau en door 
de auditor van de groep, alsmede dat daarop niet moet worden gesteund door derden; 
(b) 
dat door de auditor geen verantwoordelijkheid wordt erkend ten opzichte van derden; en 
(c) 
alle beperkingen inzake het bekendmaken of beschikbaar stellen van informatie aan 
derden. 
 
A44. In sommige rechtsgebieden kan van de auditor, op grond van wet- of regelgeving, worden vereist 
dat hij bijvoorbeeld: 
 
• 
een toezichthoudende of handhavingsinstantie op de hoogte stelt van bepaalde 
aangelegenheden die hij aan de met governance belaste personen heeft meegedeeld.In 
sommige landen heeft de auditor bijvoorbeeld de plicht om afwijkingen te rapporteren aan 
bepaalde instanties wanneer het management en de met governance belaste personen 
geen acties ondernemen om deze te corrigeren; 
• 
kopieën van bepaalde ten behoeve van de met governance belaste personen opgestelde 
rapporten overlegt aan relevante toezichthoudende of financierende instanties, dan wel 
aan andere instanties zoals een centrale instantie voor bepaalde entiteiten in de publieke 
sector;  
• 
ten behoeve van de met governance belaste personen opgesteld rapporten openbaar 
beschikbaar stelt.  
 
A45. Tenzij het op grond van wet- of regelgeving is vereist aan derden een kopie te verstrekken van 
de ten behoeve van de met governance belaste personen opgestelde schriftelijke mededeling 
van de auditor, kan de auditor een voorafgaande toestemming nodig hebben van de met 
governance belaste personen alvorens dit te doen. 
 
Vormen van communicatie (Zie par. 19)  
 
A46. Effectieve communicatie kan bestaan uit gestructureerde presentaties en schriftelijke rapporten, 
alsook uit minder gestructureerde communicatie, zoals besprekingen. De auditor kan andere dan 
in de paragrafen 19-20 genoemde aangelegenheden op mondelinge dan wel op schriftelijke wijze 
meedelen. Een voorbeeld van een schriftelijke mededeling is een opdrachtbrief die aan de met 
governance belaste personen wordt verstrekt. 
 
A47. Naast de significantie van een specifieke aangelegenheid kunnen ook andere factoren van 
invloed zijn op de communicatievorm (bijv. de vraag of op mondelinge dan wel op schriftelijke 
wijze moet worden gecommuniceerd, de mate waarin details en samenvattingen in de

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
20/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
mededeling worden opgenomen, alsmede de vraag of op een gestructureerde dan wel op een 
ongestructureerde wijze moet worden gecommuniceerd), bijvoorbeeld: 
 
• 
de vraag of een uiteenzetting van de aangelegenheid in de controleverklaring zal worden 
opgenomen. Bijvoorbeeld wanneer kernpunten van de controle worden gecommuniceerd 
in de controleverklaring, kan de auditor het noodzakelijk achten om schriftelijk te 
communiceren over de aangelegenheden die als kernpunten van de controle worden 
bepaald; 
• 
de vraag of de aangelegenheid naar tevredenheid is opgelost; 
• 
de vraag of het management de aangelegenheid al eerder heeft meegedeeld; 
• 
de omvang, operationele structuur, interne beheersomgeving en juridische vorm van de 
entiteit; 
• 
bij een controle van financiële overzichten voor specifieke doeleinden, de vraag of de 
auditor ook de financiële overzichten voor algemene doeleinden controleert; 
• 
de door de wetgeving gestelde vereisten. In bepaalde rechtsgebieden moet 
overeenkomstig de lokale wetgeving een schriftelijke mededeling in een voorgeschreven 
vorm aan de met governance belaste personen worden gericht; 
• 
de verwachtingen van de met governance belaste personen, met inbegrip van de 
afspraken die zijn gemaakt over periodieke vergaderingen of te voeren communicatie met 
de auditor; 
• 
het aantal doorlopende contacten en gesprekken die de auditor met de met governance 
belaste personen heeft; 
• 
de vraag of er significante wijzigingen zijn geweest in de leden van de groep van met 
governance belaste personen.  
 
A48. Wanneer een significante aangelegenheid wordt besproken met één individueel lid van de met 
governance belaste personen, bijvoorbeeld met de voorzitter van het auditcomité, kan het 
passend zijn dat de auditor deze aangelegenheid in latere mededelingen samenvat zodat alle 
met governance belaste personen over volledige en afgewogen informatie beschikken. 
 
Timing van de communicatie 
 
A49. Tijdige communicatie gedurende de controle draagt bij aan het bewerkstelligen van een krachtige 
wederzijdse dialoog tussen de met governance belaste personen en de auditor. De geschikte 
timing voor communicatie zal echter afhankelijk zijn van de omstandigheden van de opdracht. 
Relevante omstandigheden zijn onder meer de significantie en de aard van de aangelegenheid, 
alsmede de acties die van de met governance belaste personen worden verwacht. Bijvoorbeeld: 
 
• 
vindt communicatie met betrekking tot aangelegenheden inzake de planning vaak in een 
vroegtijdig stadium van de controleopdracht plaats en kan deze bij een initiële opdracht 
deel uitmaken van het bereiken van overeenstemming voer de opdrachtvoorwaarden; 
• 
kan het passend zijn een significante moeilijkheid die zich tijdens de controle voordoet, zo 
spoedig als praktisch uitvoerbaar mee te delen indien de met governance belaste personen 
in staat zijn de auditor bij te staan bij het oplossen van de moeilijkheid, of indien dit naar 
alle waarschijnlijkheid leidt tot een aanpassing van het oordeel in de controleverklaring. 
Tevens kan de auditor zo spoedig als praktisch uitvoerbaar significante tekortkomingen in 
de interne beheersing die hij heeft geïdentificeerd, mondeling aan de met governance 
belaste personen meedelen, alvorens deze schriftelijk mee te delen, zoals vereist door ISA 
26525; 
• 
als ISA 701 van toepassing is kan de auditor een voorlopige zienswijze over de kernpunten 
communiceren bij het bespreken van de geplande reikwijdte en timing van de controle (zie 
paragraaf A13) en de auditor kan ook vaker communiceren om dergelijke 
aangelegenheden verder te bespreken bij het communiceren over significante 
controlebevindingen; 
 
25  ISA 265, paragrafen 9 en A14.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
21/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
• 
communicatie met betrekking tot onafhankelijkheid kan passend zijn in alle gevallen waarin 
significante 
oordeelsvormingen 
worden 
gemaakt 
inzake 
bedreigingen 
van 
de 
onafhankelijkheid en inzake de daarmee samenhangende maatregelen, bijvoorbeeld bij 
het aanvaarden van een opdracht tot het verlenen van niet op controle gerichte diensten, 
alsmede bij een slotbespreking; 
• 
communicatie over bevindingen van de controle, inclusief de zienswijze van de auditor over 
de kwalitatieve aspecten van de prakijken van administratieve verwerking van de entiteit, 
kan ook onderdeel van de slotbespreking zijn; 
• 
bij het controleren van zowel financiële overzichten voor algemene doeleinden als 
financiële overzichten voor specifieke doeleinden kan het passend zijn om de timing van 
de communicatie wederzijds af te stemmen. 
 
A50. Andere factoren die relevant kunnen zijn voor de timing van de communicatie zijn onder meer: 
 
• 
de omvang, operationele structuur, interne beheersomgeving en juridische vorm van de 
gecontroleerde entiteit; 
• 
elke wettelijke verplichting tot het binnen een voorgeschreven tijdsbestek meedelen van 
bepaalde aangelegenheden; 
• 
de verwachtingen van de met governance belaste personen, met inbegrip van afspraken 
die zijn gemaakt over periodieke vergaderingen of periodieke communicatie met de auditor; 
• 
het tijdstip waarop de auditor bepaalde aangelegenheden identificeert. Zo is het mogelijk 
dat het identificeren van een specifieke aangelegenheid (zoals het niet naleven van een 
wettelijke bepaling) door de auditor niet tijdig genoeg is voor het nemen van preventieve 
maatregelen, maar dat de auditor door het meedelen van de aangelegenheid ervoor zorgt 
dat corrigerende maatregelen kunnen worden genomen. 
 
De adequaatheid van het communicatieproces (Zie par. 22) 
 
A51. De auditor hoeft geen specifieke werkzaamheden op te zetten ter ondersteuning van de evaluatie 
van de wederzijdse communicatie tussen de auditor en de met governance belaste personen; 
deze evaluatie kan worden gebaseerd op waarnemingen die voortkomen uit voor andere 
doeleinden uitgevoerde controlewerkzaamheden. Dergelijke waarnemingen kunnen de volgende 
aangelegenheden betreffen: 
 
• 
de geschiktheid en tijdigheid van acties die door de met governance belaste personen 
worden genomen teneinde in te spelen op aangelegenheden die door de auditor aan de 
orde zijn gesteld. Wanneer in eerdere mededelingen aan de orde gestelde significante 
aangelegenheden niet op doeltreffende wijze zijn afgehandeld, kan het passend zijn dat 
de auditor inlichtingen inwint over de vraag waarom geen passende actie is ondernomen, 
en dat hij overweegt dit punt opnieuw aan de orde te stellen. Dit voorkomt het risico dat de 
indruk wordt gewekt dat de auditor ervan overtuigd is dat de aangelegenheid naar behoren 
is afgehandeld of niet langer significant is; 
• 
de klaarblijkelijke openheid van de met governance belaste personen in hun communicatie 
met de auditor; 
• 
de bereidheid en de mogelijkheid van de met governance belaste personen om met de 
auditor te vergaderen zonder de aanwezigheid van het management; 
• 
de klaarblijkelijke mogelijkheid van de met governance belaste personen om de door de 
auditor aan de orde gestelde aangelegenheden volledig te begrijpen, bijvoorbeeld de mate 
waarin de met governance belaste personen kwesties onderzoeken alsmede de aan hen 
gedane aanbevelingen ter discussie stellen; 
• 
problemen om met de met governance belaste personen tot hetzelfde begrip te komen van 
de vorm, de timing en de verwachte algemene inhoud van de communicatie; 
• 
wanneer alle of sommige van de met governance belaste personen betrokken zijn bij het 
leiden van de entiteit, hun klaarblijkelijke kennis van de wijze waarop met de auditor 
besproken aangelegenheden van invloed zijn op zowel hun verantwoordelijkheden inzake

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
22/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
governance in de brede betekenis van het woord als op hun leidinggevende 
verantwoordelijkheden; 
• 
de vraag of de wederzijdse communicatie tussen de auditor en de met governance belaste 
personen voldoet aan de van toepassing zijnde, op grond van wet- en regelgeving gestelde 
vereisten. 
 
A52. Zoals vermeld in paragraaf 4 is wederzijdse communicatie een hulpmiddel voor zowel de auditor 
als de met governance belaste personen. Verder wordt in ISA 315 (herzien 2019) de 
betrokkenheid van de met governance belaste personen, met inbegrip van de interactie met de 
(eventuele) interne auditfunctie en met de externe auditors genoemd als een element van de 
interne beheersomgeving van de entiteit26. Niet-adequate wederzijdse communicatie kan wijzen 
op een onbevredigende interne beheersomgeving en kan van invloed zijn op de inschatting door 
de auditor van de risico’s op een afwijking van materieel belang. Tevens bestaat het risico dat de 
auditor geen voldoende en geschikte controle-informatie heeft verkregen om een oordeel te 
vormen over de financiële overzichten. 
 
A53. Indien wederzijdse communicatie tussen de auditor en de met governance belaste personen niet 
adequaat is en deze situatie niet kan worden opgelost, kan de auditor acties ondernemen als: 
 
• 
het aanpassen van het oordeel in de controleverklaring op basis van een beperking in de 
reikwijdte van de controle; 
• 
het verzoeken om juridisch advies over de gevolgen van verschillende handelwijzen; 
• 
het communiceren met derden (bijv. een toezichthouder) of met een ten aanzien van de 
entiteit externe instantie met een hoger niveau van verantwoordelijkheid binnen de 
governance-structuur, zoals de eigenaren van een onderneming (bijv. aandeelhouders 
tijdens een algemene vergadering) of in de publieke sector de verantwoordelijke minister 
in de regering dan wel het parlement; 
• 
het teruggeven van de opdracht wanneer dat op grond van de van toepassing zijnde wet- 
of regelgeving mogelijk is. 
 
Documentatie (Zie par. 23) 
 
A54. Documentatie van mondelinge communicatie kan onder meer bestaan uit een kopie van de 
notulen die zijn opgesteld door de entiteit en die als onderdeel van de controledocumentatie wordt 
bewaard indien deze notulen een passende vastlegging van de communicatie vormen. 
 
 
 
 
26  ISA 315 (herzien 2019), bijlage 3.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
23/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Bijlage 1  
(Zie par. 3) 
 
Specifieke vereisten in ISQM 1 en andere ISA’s met betrekking tot de 
communicatie met de met governance belaste personen 
 
In deze bijlage wordt vermeld welke paragrafen in ISQM 127 en in andere ISA’s  die het meedelen van 
specifieke aangelegenheden aan de met governance belaste personen vereisen. Deze opsomming is 
geen substituut voor het in aanmerking nemen van de in de ISA’s voorkomende vereisten en daarmee 
verband houdende toepassingsgerichte en overige verklarende teksten. 
 
• 
ISQM 1, Kwaliteitsmanagement voor kantoren die controles of beoordelingen van financiële 
overzichten, of andere assurance opdrachten of opdrachten voor aan assurance verwante 
diensten uitvoeren, paragraaf 34(e); 
• 
ISA 240, Verantwoordelijkheden van de auditor met betrekking tot fraude in het kader van een 
controle van financiële overzichten, paragraaf 21, 398(c)(i) en 41-43; 
• 
ISA 250 (herzien), Het in aanmerking nemen van wet- en regelgeving bij een controle van 
financiële overzichten, paragraaf 15, 20 en 23-25; 
• 
ISA 265, Meedelen van tekortkomingen in de interne beheersing aan de met governance 
belaste personen en het management, paragraaf 9; 
• 
ISA 450, Evaluatie van tijdens de controle geïdentificeerde afwijkingen, paragraaf 12-13; 
• 
ISA 505, Externe bevestigingen, paragraaf 9;  
• 
ISA 510, Initiële controleopdrachten – Beginsaldi, paragraaf 7; 
• 
ISA 540 (herzien), De controle van schattingen en toelichtingen daarop, paragraaf 38; 
• 
ISA 550, Verbonden partijen, paragraaf 27; 
• 
ISA 560, Gebeurtenissen na de einddatum van de verslagperiode, paragraaf 7(b)-(c), 10(a), 
13(b), 14(a) en 17; 
• 
ISA 570 (herzien), Continuïteit, paragraaf 25; 
• 
ISA 600, Bijzondere overwegingen – Controles van financiële overzichten van een groep 
(inclusief de werkzaamheden van auditors van groepsonderdelen), paragraaf 49; 
• 
ISA 610 (herzien 2013), Gebruikmaken van de werkzaamheden van interne auditors - 
paragrafen 20 en 31; 
• 
ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten, 
paragraaf 46; 
• 
ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de 
onafhankelijke auditor, paragraaf 17; 
• 
ISA 705 (herzien), Aanpassingen van het oordeel in de controleverklaring van de 
onafhankelijke auditor, paragrafen 12, 14, 23 en 30; 
• 
ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en 
paragrafen inzake overige aangelegenheden, toegevoegd in de controleverklaring van de 
onafhankelijk auditor, paragraaf 12; 
• 
ISA 710, Ter vergelijking opgenomen informatie – Overeenkomstige cijfers en vergelijkende 
financiële overzichten, paragraaf 18; 
• 
ISA 720 (herzien), De verantwoordelijkheden van de auditor met betrekking tot andere 
informatie, paragrafen 17-19. 
 
 
 
 
 
27  Internationale Standaard inzake kwaliteitsmanagement (ISQM) 1, “Kwaliteitsmanagement voor kantoren die controles of 
beoordelingen van financiële overzichten, of andere assurance opdrachten of opdrachten voor aan assurance verwante 
diensten uitvoeren”.

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
24/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Bijlage 2  
(Zie par. 16(a), A19–A20) 
 
Kwalitatieve aspecten van praktijken inzake administratieve verwerking 
 
De communicatie die op grond van paragraaf 16(a) is vereist en die in paragraaf A19–A20 behandeld 
is, kan aangelegenheden betreffen als: 
 
Grondslagen voor financiële verslaggeving 
 
• 
de geschiktheid van de grondslagen voor financiële verslaggeving in de specifieke 
omstandigheden van de entiteit, rekening houdend met de noodzaak om de kosten van het 
verschaffen van informatie af te wegen ten opzichte van de waarschijnlijke baten voor de 
gebruikers van financiële overzichten van de entiteit. Wanneer er aanvaardbare alternatieve 
grondslagen voor financiële verslaggeving bestaan, kan de communicatie onder meer 
betrekking hebben op het aanwijzen van elementen in de financiële overzichten die worden 
beïnvloed door de keuze van significante grondslagen voor financiële verslaggeving, alsook 
op informatie over de grondslagen voor financiële verslaggeving die door soortgelijke 
entiteiten worden gehanteerd; 
• 
de initiële keuze inzake significante grondslagen voor financiële verslaggeving, en de latere 
wijzigingen daarin, met inbegrip van het toepassen van nieuwe standaarden inzake financiële 
verslaggeving. De communicatie kan onder meer betrekking hebben op het effect van de 
timing en van de methode van het aanbrengen van een wijziging in de grondslagen voor 
financiële verslaggeving op de huidige en toekomstige winst van de entiteit, alsmede op de 
timing van een wijziging in de grondslagen voor financiële verslaggeving in relatie tot 
verwachte nieuwe standaarden inzake financiële verslaggeving; 
• 
het effect van significante grondslagen voor financiële verslaggeving op omstreden of 
opkomende gebieden (of op gebieden die uniek zijn voor een bedrijfstak, met name wanneer 
er een gebrek is aan gezaghebbende richtlijnen of eensgezindheid); 
• 
het effect van het moment waarop transacties worden uitgevoerd op de verslagperiode waarin 
zij worden geboekt. 
 
Schattingen en toelichtingen daarop 
 
Bijlage 2 van ISA 540 (herzien) omvat aangelegenheden die de auditor kan overwegen om te 
communiceren met betrekking tot significante kwalitatieve aspecten van de administratieve praktijken 
van de entiteit met betrekking tot schattingen en toelichtingen daarop. 
 
In de financiële overzichten opgenomen toelichtingen 
 
• 
de kwesties, alsmede de daarop betrekking hebbende oordeelsvormingen, die verband 
houden met het formuleren van bijzonder gevoelige, in de financiële overzichten opgenomen 
toelichtingen (bijv. toelichtingen over het verantwoorden van opbrengsten, beloningen, 
continuïteit, gebeurtenissen na de einddatum van de verslagperiode en kwesties inzake 
voorwaardelijke gebeurtenissen); 
• 
de algehele neutraliteit, consistentie en duidelijkheid van de in de financiële overzichten 
opgenomen toelichtingen. 
 
Verwante aangelegenheden 
 
• 
het mogelijke effect op de financiële overzichten van significante risico’s, de onderhevigheid 
aan risico’s en onzekerheden, zoals lopende rechtszaken, waarover in de financiële 
overzichten een toelichting wordt opgenomen;

COMMUNICATIE MET DE MET GOVERNANCE BELASTE PERSONEN 
 
ISA 260 (herzien) 
NBA-IBR 2023 
 
25/25 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
• 
de mate waarin de financiële overzichten worden beïnvloed door significante transacties die 
zich buiten het kader van de normale bedrijfsvoering van de entiteit bevinden, of die 
anderszins ongebruikelijk lijken. Deze communicatie kan het volgende benadrukken: 
 
o 
de eenmalige bedragen die tijdens de periode zijn verwerkt. 
o 
de mate waarin dergelijke transacties afzonderlijk in de financiële overzichten zijn 
toegelicht. 
o 
of dergelijke transacties lijken te zijn opgezet om een bepaalde administratieve of fiscale 
verwerking te bewerkstelligen, dan wel een doelstelling op grond van wet-of 
regelgeving. 
o 
of de vorm van dergelijke transacties overdreven complex lijkt of waar uitgebreid advies 
met betrekking tot het structureren van de transactie is ondernomen. 
o 
waar het management meer nadruk legt op de noodzaak van een specifieke wijze van 
administratieve verwerking dan op de onderliggende economische beweegreden van 
de transactie.  
 
• 
de factoren die van invloed zijn op de boekwaarden van de activa en passiva, met inbegrip 
van de grondslagen voor het bepalen van de aan de materiële en immateriële activa 
toegekende economische levensduur. In de communicatie kan uitleg worden gegeven over 
de wijze waarop factoren die van invloed zijn op de boekwaarden worden gekozen en over de 
wijze waarop alternatieve keuzes de financiële overzichten zouden hebben beïnvloed; 
• 
het selectief corrigeren van afwijkingen, bijvoorbeeld het corrigeren van afwijkingen die een 
verhoging van de gerapporteerde winsten tot gevolg hebben, maar niet van afwijkingen die 
een verlaging van deze winsten tot gevolg hebben.