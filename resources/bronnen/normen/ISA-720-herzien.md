---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 720 (herzien) — De verantwoordelijkheden van de auditor met betrekking tot
  andere informatie
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-720-(herzien)_nl_2023.pdf
    sha256: a6e4e798a8c86aaf934f3e31eaf0a36444a7e836e9f8211c973358f0228191b6
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
title: ISA 720 (herzien) — De verantwoordelijkheden van de auditor met betrekking
  tot andere informatie
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 720 (herzien) — De verantwoordelijkheden van de auditor met betrekking tot andere informatie

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-720-(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `a6e4e798a8c86aaf934f3e31eaf0a36444a7e836e9f8211c973358f0228191b6`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard 720 (herzien) 
ISA 720 (herzien)  
 
De verantwoordelijkheden van de 
auditor met betrekking tot andere 
informatie

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
2/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Over de IAASB 
 
Copyright IFAC 
 
Deze Internationale controlestandaard (ISA) werd in 2022 in de Engelse taal gepubliceerd door de 
International Auditing and Assurance Standards Board (IAASB) van de International Federation of 
Accountants (IFAC). Deze ISA werd in 2022 vertaald naar het Nederlands door de Nederlandse 
Beroepsorganisatie van Accountants (NBA), met medewerking van het Belgisch Instituut van de 
Bedrijfsrevisoren (IBR), en werd verspreid met toestemming van IFAC. Het proces voor het vertalen van 
de Internationale controlestandaard (ISA) 720 (herzien) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 
720 (herzien) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 720 (herzien) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 720 (herzien) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 720 (Revised), Comparative Information–
Corresponding Figures and Comparative Financial Statements. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, 
and Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
3/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
INTERNATIONALE CONTROLESTANDAARD 720 (HERZIEN) 
 
DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET 
BETREKKING TOT ANDERE INFORMATIE 
 
(Van toepassing op controles van financiële overzichten over verslagperioden  
die op of na 15 december 2016 worden afgesloten) (*) 
 
(*) Deze ISA bevat overeenstemmingswijzigingen die voortvloeien uit de herziene ISA’s 220, 250, 315 
en 540 en de normen ISQM 1 en 2. De inwerkingtreding van deze wijzigingen valt samen met deze 
normen (voor de verslagperiode die op of na 15 december aanvangen). 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ......................................................................................................... 1-9 
Ingangsdatum................................................................................................................................................  10 
Doelstellingen .................................................................................................................................  11 
Definities ................................................................................................................................................. 12 
Vereisten 
Verkrijgen van andere informatie ....................................................................................................... 13 
Lezen en overwegen van de andere informatie  ......................................................................... 14-15 
Reageren wanneer een inconsistentie van materieel belang lijkt te bestaan of de andere 
informatie afwijkingen van materieel belang lijkt te bevatten ............................................................  16 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de 
andere informatie bestaat ............................................................................................................. 17-19 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de 
financiële overzichten bestaat of het inzicht van de auditor in de entiteit en haar omgeving moet 
worden geactualiseerd ....................................................................................................................... 20 
Rapportage ................................................................................................................................... 21-24 
Documentatie ..................................................................................................................................... 25 
Toepassingsgerichte en overige verklarende teksten 
Definities  ................................................................................................................................... A1-A10 
Verkrijgen van andere informatie ............................................................................................. A11-A22 
Lezen en overwegen van de andere informatie ....................................................................... A23-A38 
Reageren wanneer een inconsistentie van materieel belang lijkt te bestaan of andere 
informatie een afwijking van materieel belang lijkt te bevatten ................................................ A39-A43 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de 
andere informatie bestaat ........................................................................................................ A44-A50 
Reageren wanneer er een afwijking van materieel belang in de financiële overzichten bestaat

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
4/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
of het inzicht van de auditor in de entiteit en haar omgeving moet worden geactualiseerd ........... A51 
Rapportage ............................................................................................................................. A52-A59 
 
Bijlage 1:  Voorbeelden van bedragen of andere elementen die kunnen worden opgenomen in de 
andere informatie  
Bijlage 2: 
Voorbeelden van controleverklaringen met betrekking tot andere informatie 
 
International Standard on Auditing (ISA) 720 (herzien), De verantwoordelijkheden van de auditor met 
betrekking tot andere informatie, moet worden gelezen in samenhang met ISA 200, Algehele 
doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig 
de International Standards on Auditing.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
5/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Inleiding 
 
Toepassingsgebied van deze ISA 
 
1. 
Deze ISA behandelt de verantwoordelijkheden van de auditor met betrekking tot andere 
informatie, hetzij financiële informatie of niet- financiële informatie (anders dan financiële 
overzichten en de daarbij horende controleverklaring), opgenomen in het jaarrapport van een 
entiteit. Een jaarrapport van een entiteit kan één enkel document of een combinatie van 
documenten zijn die hetzelfde doel dienen. 
  
2. 
Deze ISA is geschreven in de context van een controle van financiële overzichten door een 
onafhankelijke auditor. De doelstellingen van de auditor in deze ISA moeten daarom begrepen 
worden in de context van de algehele doelstellingen van de auditor zoals weergegeven in 
paragraaf 11 van ISA 2001. De vereisten zijn opgezet om de auditor in staat te stellen de 
doelstellingen die gespecificeerd zijn in de ISA’s en daarmee de algehele doelstellingen van de 
auditor te bereiken. Het oordeel van de auditor over de financiële overzichten omvat niet de andere 
informatie, noch vereist deze ISA van de auditor controle- informatie te verkrijgen die verder gaat 
dan vereist om een oordeel over de financiële overzichten te vormen. 
 
3. 
Deze ISA vereist van de auditor om de andere informatie te lezen en te overwegen omdat andere 
informatie die materieel inconsistent is met de financiële overzichten of met de kennis die de 
auditor heeft verkregen tijdens de controle, erop kan wijzen dat er een afwijking van materieel 
belang in de financiële overzichten is of dat er een afwijking van materieel belang in de andere 
informatie bestaat, welke beide de geloofwaardigheid van de financiële overzichten en de daarbij 
horende controleverklaring kunnen ondermijnen. Dergelijke afwijkingen van materieel belang 
kunnen ook op onjuiste wijze de economische beslissingen van gebruikers waarvoor de 
controleverklaring is opgesteld, beïnvloeden. 
 
4. 
Deze ISA kan de auditor ook helpen om de relevante ethische voorschriften2 na te leven die van 
de auditor vereisen te vermijden om bewust geassocieerd te worden met informatie waarvan de 
auditor van mening is dat deze een materieel onjuiste of misleidende vermelding bevat, 
onzorgvuldig verschafte vermeldingen of informatie bevat, of informatie weglaat of verhult 
waarvan is vereist dat die informatie is toegevoegd waar een dergelijke weglating of verhulling 
misleidend zou kunnen zijn. 
 
5. 
Andere informatie kan bedragen of andere elementen omvatten die bedoeld zijn om hetzelfde te 
zijn, om samen te vatten, of om een grotere detaillering te verschaffen over bedragen of andere 
elementen in de financiële overzichten en andere bedragen of andere elementen waarover de 
auditor kennis heeft verkregen tijdens de controle. Andere informatie kan ook andere 
aangelegenheden omvatten. 
 
6. 
De verantwoordelijkheden van de auditor met betrekking tot andere informatie (anders dan van 
toepassing zijnde rapporteringsverantwoordelijkheden) zijn van toepassing ongeacht of de 
andere informatie is verkregen door de auditor voor of na de datum van de controleverklaring.  
 
7. 
Deze ISA is niet van toepassing op: 
 
(a) 
Voorlopige aankondigingen van financiële informatie: of  
(b) 
Documenten inzake aanbiedingen van effecten, inclusief prospectussen 
 
8. 
De verantwoordelijkheden van de auditor onder deze ISA vormen geen assurance-opdracht 
betreffende andere informatie en leggen de auditor geen verplichting op om assurance te 
verkrijgen over de andere informatie. 
 
1  
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de 
International Standards on Auditing. 
2  
International Ethics Standards Board for Auditors Code of Ethics for Professional Accountants (IFAC Code), paragraph R111.2.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
6/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
9. 
Wet- of regelgeving kan additionele verplichtingen aan de auditor opleggen met betrekking tot 
andere informatie die verder gaan dan de reikwijdte van deze ISA. 
  
Ingangsdatum 
 
10. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten.  
 
Doelstellingen 
 
11. 
De doelstellingen van de auditor zijn, nadat hij de andere informatie heeft gelezen: 
 
(a) 
Om te overwegen of er een inconsistentie van materieel belang is tussen de andere 
informatie en de financiële overzichten; 
(b) 
Om te overwegen of er een inconsistentie van materieel belang is tussen de andere 
informatie en de kennis van de auditor verkregen in de controle; 
(c) 
Om op passende wijze te reageren wanneer de auditor constateert dat dergelijke 
inconsistenties van materieel belang lijken te bestaan of wanneer de auditor zich er 
anderszins van bewust wordt dat andere informatie een afwijking van materieel belang lijkt 
te bevatten; en 
(d) 
Om overeenkomstig deze ISA te rapporteren. 
 
Definities 
 
12. 
Voor de toepassing van de ISA’s en hebben de volgende termen de hierna weergegeven 
betekenis: 
 
(a) 
Jaarrapport – Een document of combinatie van documenten, meestal opgesteld op 
jaarbasis door het management of de personen belast met governance in 
overeenstemming met wet- of regelgeving of gebruik, waarvan het doel is om eigenaren 
(of vergelijkbare belanghebbenden) van informatie te voorzien over de activiteiten van de 
entiteit en de financiële resultaten en financiële positie van de entiteit zoals uiteengezet in 
de financiële overzichten. Een jaarrapport bevat of gaat samen met de financiële 
overzichten en de daarbij horende controleverklaring en bevat gewoonlijk informatie over 
de ontwikkelingen van de entiteit, haar vooruitzichten en risico’s en onzekerheden, een 
statement door de groep met governance belaste personen van de entiteit en rapporten 
die governance aangelegenheden bevatten. (Zie par. A1-A5) 
(b) 
Afwijking van de andere informatie – Een afwijking van de andere informatie bestaat 
wanneer de andere informatie onjuist is vermeld of anderszins misleidend is (inclusief 
omdat het informatie weglaat of verhult die nodig is voor een goed begrip van een 
aangelegenheid die is toegelicht in de andere informatie). (Zie par. A6-A7) 
(c) 
Andere informatie – Financiële of niet-financiële informatie (anders dan de financiële 
overzichten en de daarbij horende controleverklaring ) opgenomen in het jaarrapport van 
een entiteit. (Zie par. A8-A10) 
 
Vereisten 
 
Verkrijgen van de andere informatie 
 
13. 
De auditor dient: (Zie par. A11-A22) 
 
(a) 
Te bepalen, door bespreking met het management, welke documenten het jaarrapport 
vormen en de geplande wijze en timing van de publicatie van (een) dergelijk(e) 
document(en) door de entiteit; 
(b) 
Passende afspraken te maken met het management om tijdig en, indien mogelijk, vóór de 
datum van de controleverklaring, de definitieve versie van het(de) document(en) waaruit 
het jaarrapport bestaat te verkrijgen; en

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
7/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
(c) 
Wanneer sommige of alle documenten bepaald in (a) niet beschikbaar zijn tot na de datum 
van de controleverklaring, het management te verzoeken om een schriftelijke bevestiging 
te verschaffen dat de definitieve versie van het(de) document(en) aan de auditor verschaft 
zal worden wanneer dit (deze) beschikbaar is (zijn) en voorafgaand aan de publicatie door 
de entiteit, zodat de auditor de werkzaamheden die door deze ISA vereist zijn, kan 
voltooien. (Zie par. A22) 
 
Lezen en overwegen van de andere informatie 
 
14. 
De auditor dient de andere informatie te lezen en daarbij dient hij: (Zie par. A23-A24) 
 
(a) 
Te overwegen of er een inconsistentie van materieel belang is tussen de andere 
informatie en de financiële overzichten. Als basis voor deze overweging dient de auditor, 
om de consistentie daarvan te evalueren, geselecteerde bedragen of andere elementen 
in de andere informatie (die bedoeld zijn om hetzelfde te zijn, om samen te vatten, of om 
een grotere detaillering te verschaffen over de bedragen of andere elementen in de 
financiële overzichten) te vergelijken met dergelijke bedragen of andere elementen in de 
financiële overzichten; en (Zie par. A25-A29) 
(b) 
Te overwegen of er een inconsistentie van materieel belang is tussen de andere 
informatie en de kennis van de auditor verkregen in de controle, in de context van de 
verkregen controle-informatie en de conclusies getrokken in de controle. (Zie par. A30-
A36) 
 
15. 
Tijdens het lezen van de andere informatie in overeenstemming met paragraaf 14, dient de 
auditor alert te blijven voor aanwijzingen dat de andere informatie die niet is gerelateerd aan de 
financiële overzichten of aan de kennis van de auditor verkregen in de controle, afwijkingen van 
materieel belang lijkt te bevatten. (Zie par. A24, A37-A38) 
 
Reageren wanneer een inconsistentie van materieel belang lijkt te bestaan of de andere 
informatie afwijkingen van materieel belang lijkt te bevatten 
 
16. 
Als de auditor identificeert dat er een onzekerheid van materieel belang lijkt te bestaan (of zich 
ervan bewust wordt dat de andere informatie afwijkingen van materieel belang lijkt te bevatten), 
dient de auditor de aangelegenheid te bespreken met het management en, indien noodzakelijk, 
andere werkzaamheden uit te voeren om te concluderen of:  (Zie par. A39-A43) 
 
(a) 
Er een afwijking van materieel belang van de andere informatie bestaat; 
(b) 
Er een afwijking van materieel belang van de financiële overzichten bestaat;  
(c) 
Het inzicht van de auditor in de entiteit en haar omgeving moet worden bijgewerkt. 
 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de andere 
informatie bestaat 
 
17. 
Als de auditor concludeert dat er een afwijking van materieel belang in de andere informatie 
bestaat, dient de auditor het management te verzoeken om de andere informatie te corrigeren. 
Indien het  management: 
 
(a) 
Instemt met de correctie, dient de auditor te bepalen dat de correctie gemaakt is; of 
(b) 
Weigert om de correctie te maken, dient de auditor de aangelegenheid te communiceren 
met de personen belast met governance en te verzoeken dat de correctie gemaakt wordt. 
 
18. 
Indien de auditor concludeert dat er een afwijking van materieel belang in de andere informatie 
bestaat die verkregen is vóór de datum van de controleverklaring en de andere informatie niet 
gecorrigeerd is na communicatie met de personen belast met governance, dient de auditor 
passende maatregelen te nemen, inclusief: (Zie par. A44) 
 
(a) 
De implicaties voor de controleverklaring te overwegen en te communiceren met de

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
8/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
personen belast met governance over hoe de auditor plant om de afwijking van materieel 
belang in de controleverklaring te behandelen (zie paragraaf 22(e)(ii)); of (Zie par. A45) 
(b) 
De opdracht terug te geven wanneer dat overeenkomstig de van toepassing zijnde wet- 
of regelgeving mogelijk is. (Zie par. A46-A47) 
 
19. 
Indien de auditor concludeert dat er een afwijking van materieel belang bestaat in de andere 
informatie die verkregen is na de datum van de controleverklaring, dient de auditor: 
 
(a) 
Indien de andere informatie is gecorrigeerd, de werkzaamheden uit te voeren die 
noodzakelijk zijn in de omstandigheden; of (Zie par. A48) 
(b) 
Indien de andere informatie niet gecorrigeerd is na communicatie met de personen belast 
met governance, passende maatregelen te nemen rekening houdend met de wettelijke 
rechten en verplichtingen van de auditor en te streven naar het op passende wijze onder 
de aandacht brengen van de ongecorrigeerde afwijking van materieel belang bij de 
gebruikers voor wie de controleverklaring is opgesteld. (Zie par. A49–A50) 
 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de 
financiële overzichten bestaat of het inzicht van de auditor in de entiteit en haar omgeving moet 
worden geactualiseerd 
 
20. 
Indien de auditor, als gevolg van het uitvoeren van de werkzaamheden in paragraaf 14-15, 
concludeert dat er een afwijking van materieel belang in de financiële overzichten bestaat of dat 
het inzicht van de auditor in de entiteit en haar omgeving moet worden geactualiseerd, dient de 
auditor op gepaste wijze hierop in te spelen  in overeenstemming met de andere ISA’s. (Zie par. 
A51) 
 
Rapportage 
 
21. 
De controleverklaring dient een aparte sectie te bevatten met een titel “Andere informatie” of 
andere geschikte titel wanneer op de datum van de controleverklaring: 
 
(a) 
Voor een controle van financiële overzichten van een genoteerde entiteit de auditor de 
andere informatie heeft verkregen of verwacht deze te verkrijgen; of 
(b) 
Voor een controle van financiële overzichten van een niet-genoteerde entiteit, de auditor 
bepaalde of alle andere informatie heeft verkregen. (Zie par. A52) 
 
22. 
Wanneer het verplicht is om in de controleverklaring een sectie "Andere informatie” op te nemen 
in overeenstemming met paragraaf 21, dient deze sectie te omvatten: (Zie par. A53) 
 
(a) 
Een vermelding dat het management verantwoordelijk is voor de andere informatie; 
(b) 
Een identificatie van: 
 
(i) 
Eventuele andere informatie verkregen door de auditor vóór de datum van de 
controleverklaring; en 
(ii) 
Voor een controle van financiële overzichten van een beursgenoteerde entiteit, 
eventuele andere informatie die naar verwachting na de datum van de 
controleverklaring zal worden verkregen; 
 
(c) 
Een vermelding dat het oordeel van de auditor de andere informatie niet omvat en dat, 
dienovereenkomstig, de auditor over de andere informatie geen controleoordeel tot 
uitdrukking brengt (of zal brengen) en geen enkele vorm van assurance-conclusie 
formuleert (of zal formuleren); 
(d) 
Een beschrijving van de verantwoordelijkheden van de auditor met betrekking tot het 
lezen, het overwegen van, en het rapporteren over, andere informatie zoals vereist door 
deze ISA; en 
(e) 
Wanneer andere informatie is verkregen vóór de datum van de controleverklaring: 
 
(i) 
Een vermelding dat de auditor niets heeft te rapporteren; of

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
9/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
(ii) 
Als de auditor heeft geconcludeerd dat er een ongecorrigeerde afwijking van 
materieel belang in de andere informatie is, een vermelding die de ongecorrigeerde 
afwijking van materieel belang in de andere informatie beschrijft. 
 
23. 
Wanneer de auditor een oordeel met beperking of een afkeurend oordeel tot uitdrukking brengt 
in overeenstemming met ISA 705 (herzien)3, dient de auditor de implicaties te overwegen van 
de aangelegenheid die aanleiding geeft voor de aanpassing van het oordeel voor de vermelding 
vereist in paragraaf 22(e)). (Zie par. A54-A58) 
 
Rapportage voorgeschreven door wet-of regelgeving 
 
24. 
Indien op grond van de wet- of regelgeving van een specifiek rechtsgebied van de auditor wordt 
vereist dat hij middels een specifieke opmaak of formulering in de controleverklaring refereert aan 
de andere informatie, mag de controleverklaring slechts naar de International Standards on 
Auditing verwijzen als ze ten minste elk van de volgende elementen bevat: (Zie par. A59) 
 
(a) 
Identificatie van de andere informatie verkregen door de auditor voor de datum van de 
controleverklaring; 
(b) 
Een beschrijving van de verantwoordelijkheden van de auditor met betrekking tot de 
andere informatie; en 
(c) 
Een expliciete vermelding die de uitkomsten van het werk van de auditor voor dit doel 
behandelt. 
 
Documentatie 
 
25. 
Bij het inspelen op de vereisten van ISA 2304 zoals dit van toepassing is op deze ISA, dient de 
auditor in de controledocumentatie op te nemen: 
 
(a) 
Documentatie van de onder deze ISA uitgevoerde werkzaamheden; en 
(b) 
De definitieve versie van de andere informatie waarop de auditor het onder deze ISA 
vereiste werk heeft uitgevoerd. 
 
 
**** 
 
Toepassingsgerichte en overige verklarende teksten 
 
Definities 
 
Jaarrapport (Zie par. 12(a)) 
 
A1. 
Wet- of regelgeving of gebruik kan voor entiteiten in een specifiek rechtsgebied de inhoud van 
een jaarrapport en de naam waarnaar moet worden verwezen, definiëren; de inhoud en de naam 
kunnen echter verschillen binnen een rechtsgebied en van het ene rechtsgebied naar het andere. 
 
A2. 
Een jaarrapport wordt meestal opgesteld op jaarbasis. Echter, wanneer de gecontroleerde 
financiële overzichten opgesteld zijn voor een periode van minder dan of meer dan een jaar, kan 
een jaarrapport ook worden opgesteld dat dezelfde periode als de financiële overzichten omvat. 
 
A3. 
In sommige gevallen kan het jaarrapport van een entiteit één enkel document zijn en kan ernaar 
verwezen worden door de titel “jaarrapport” of een andere titel. In andere gevallen is het mogelijk 
dat wet- of regelgeving of gebruik, van de entiteit vereist om aan eigenaren (of soortgelijke 
belanghebbenden) informatie te rapporteren over de activiteiten van de entiteit en over de 
financiële resultaten en financiële positie van de entiteit zoals uiteengezet in de financiële 
overzichten (b.v. een jaarrapport) bij wijze van één enkel document of twee of meer aparte 
 
3  
ISA 705 (herzien), Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor. 
4  
ISA 230, Controledocumentatie, paragrafen 8-11.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
10/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
documenten die in combinatie hetzelfde doel dienen. Bijvoorbeeld, afhankelijk van wet- of 
regelgeving of gebruik in een bepaald rechtsgebied, kunnen één of meer van de volgende 
documenten deel uitmaken van het jaarrapport: 
 
• 
Management rapport, management commentaar, of operationele en financiële beoordeling 
of soortgelijke rapportages door de personen belast met governance (bijvoorbeeld een 
verslag van de raad van commissarissen); 
• 
Mededeling van de voorzitter; 
• 
Mededeling inzake corporate governance; 
• 
Interne beheersings- en risico-inschattingsrapportages. 
 
 
A4. 
Een jaarrapport kan beschikbaar worden gesteld aan gebruikers in geprinte vorm of elektronisch, 
inclusief op de website van de entiteit. Een document (of combinatie van documenten) kan 
voldoen aan de definitie van een jaarrapport, ongeacht de wijze waarop het beschikbaar is gesteld 
aan gebruikers. 
 
A5. 
Een jaarrapport verschilt in aard, doel en inhoud van andere rapporten, zoals een rapport dat is 
opgesteld om te voldoen aan de informatiebehoeften van een specifieke groep belanghebbenden 
of een rapport dat is opgesteld om te voldoen aan een specifiek rapporteringsdoel op grond van 
regelgeving (zelfs wanneer zo’n rapport vereist wordt om openbaar beschikbaar te zijn). 
Voorbeelden van rapporten die, wanneer ze worden gepubliceerd als zelfstandige documenten, 
niet typisch onderdeel zijn van de combinatie van documenten die een jaarrapport vormen 
(onderworpen aan wet- of regelgeving of gebruik) en die daarom geen andere informatie zijn 
binnen de reikwijdte van deze ISA omvatten: 
 
• 
Aparte sectorrapporten of rapporten op grond van regelgeving (bijvoorbeeld rapporten over 
kapitaaltoereikendheid), zoals die kunnen worden opgesteld in de banken-, verzekerings- 
en pensioensectoren; 
• 
Maatschappelijke verslagen; 
• 
Duurzaamheidsverslagen; 
• 
Rapporten over diversiteit -en gelijke behandeling; 
• 
Rapporten over productverantwoordelijkheid; 
• 
Rapporten over arbeidsomstandigheden en arbeidsvoorwaarden; 
• 
Rapporten over mensenrechten. 
 
Afwijkingen van de andere informatie (Zie par. 12(b)) 
 
 
A6. 
Wanneer een bepaalde aangelegenheid wordt toegelicht in de andere informatie, kan de andere 
informatie weglaten of verhullen die nodig is voor een goed begrip van die aangelegenheid. 
Bijvoorbeeld, als de andere informatie beweert de belangrijkste prestatie-indicatoren die worden 
gebruikt door het management te behandelen, dan zou het weglaten van een belangrijke door 
het management gebruikte prestatie-indicator erop kunnen wijzen dat de andere informatie 
misleidend is. 
 
A7. 
Het begrip “materialiteit” kan besproken worden in een stelsel dat van toepassing is op de andere 
informatie en, als dat zo is, kan zo’n stelsel een referentiekader bieden voor de auditor bij het 
vormen van oordelen over materialiteit onder deze ISA. Echter, in veel gevallen is er geen van 
toepassing zijnde stelsel dat een bespreking van het concept materialiteit omvat dat geldt voor de 
andere informatie. In dergelijke omstandigheden verschaffen de volgende kenmerken een 
referentiekader voor de auditor bij het bepalen of een afwijking in de andere informatie van 
materieel belang is: 
 
• 
Materialiteit wordt beschouwd in de context van de algemene informatiebehoeften van 
gebruikers als een groep. De gebruikers van de andere informatie worden verondersteld 
dezelfde te zijn als de gebruikers van de financiële overzichten aangezien dergelijke 
gebruikers worden verondersteld de andere informatie te lezen om de financiële 
overzichten van context te voorzien;

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
11/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
• 
Oordeelsvormingen over materialiteit houden rekening met de specifieke omstandigheden 
van de afwijking, overwegend of gebruikers beïnvloed zouden worden door het effect van 
de niet- gecorrigeerde afwijking. Niet alle afwijkingen zullen de economische beslissingen 
van gebruikers beïnvloeden; 
• 
Oordeelsvormingen over materialiteit omvatten zowel kwalitatieve als kwantitatieve 
overwegingen. Dienovereenkomstig kunnen dergelijke oordeelsvormingen rekening 
houden met de aard of omvang van de elementen die de andere informatie behandelt in 
de context van het jaarrapport van de entiteit. 
 
Andere informatie (Zie par. 12(c)) 
 
A8. 
Bijlage 1 bevat voorbeelden van bedragen of andere elementen die kunnen worden opgenomen 
in de andere informatie. 
 
A9. 
In sommige gevallen kan het van toepassing zijnde stelsel inzake financiële verslaggeving 
specifieke toelichtingen vereisen, maar toestaan om deze buiten de financiële overzichten weer 
te geven5. Aangezien dergelijke toelichtingen vereist zijn door het van toepassing zijnde stelsel 
maken zij deel uit van de financiële overzichten. Bijgevolg vertegenwoordigen zij geen andere 
informatie voor de doelstelling van deze ISA.  
 
A10. eXensible Business Reporting Language (XBRL) tags vertegenwoordigen geen andere informatie 
zoals gedefinieerd in deze ISA. 
 
Verkrijgen van de andere informatie (Zie par. 13) 
 
A11. Het bepalen van het (de) document(en) die het jaarrapport vormt (vormen) is vaak gebaseerd op 
wet-of regelgeving of gebruik. In veel gevallen kan het management of kunnen de personen belast 
met governance gewoonlijk een pakket van documenten hebben gepubliceerd die samen het 
jaarrapport vormen, of zich hebben gecommitteerd om dat te doen. Echter, in sommige gevallen, 
kan het niet duidelijk zijn welk(e) document(en) het jaarrapport vormt (vormen). In dergelijke 
gevallen zijn de timing en het doel van de documenten (en voor wie ze bedoeld zijn) 
aangelegenheden die relevant kunnen zijn voor de bepaling van de auditor welk(e) document(en) 
het jaarrapport vormt (vormen). 
 
A12. Wanneer het jaarrapport wordt vertaald in andere talen op grond van wet- of regelgeving (zoals 
kan gebeuren als een rechtsgebied meer dan een officiële taal heeft) of wanneer meerdere 
“jaarrapporten” worden opgesteld onder verschillende wetgeving (bijvoorbeeld wanneer een 
entiteit beursgenoteerd is in meer dan een rechtsgebied), kan het nodig zijn om te overwegen of 
een of meer dan een van de “jaarrapporten” deel uitmaken van de andere informatie. Lokale wet-
of regelgeving kan verdere leidraden verschaffen in dit opzicht. 
 
A13. Management of de personen belast met governance zijn verantwoordelijk voor het opstellen van 
het jaarrapport. De auditor kan met het management of de personen belast met governance 
communiceren over: 
 
• 
De verwachtingen van de auditor met betrekking tot het verkrijgen van de definitieve versie 
van het jaarrapport (inclusief een combinatie van documenten die samen het jaarrapport 
vormen) tijdig voor de datum van de controleverklaring zodat de auditor de 
werkzaamheden vereist door deze ISA kan afronden voor de datum van de 
controleverklaring, of als dat niet mogelijk is, zo spoedig als praktisch uitvoerbaar is en in 
elk geval voor de publicatie van dergelijke informatie door de entiteit; 
• 
De mogelijke implicaties wanneer de andere informatie is verkregen na de datum van de 
controleverklaring.  
 
5  
Bijvoorbeeld IFRS 7, “Financiële instrumenten: Toelichtingen” staat toe om bepaalde toelichtingen, vereist door de IFRS 
in de financiële overzichten te geven of met verwijzing vanuit de financiële overzichten op te nemen in een ander overzicht 
zoals het management commentaar of de risicorapportage, die beschikbaar is voor gebruikers van de financiële 
overzichten op dezelfde voorwaarden als de financiële overzichten en op dezelfde tijd.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
12/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A14. De communicatie waarnaar wordt verwezen in paragraaf A13 kan bijzonder geschikt zijn 
bijvoorbeeld: 
 
• 
Bij een eerste controleopdracht; 
• 
Wanneer er een verandering is geweest in het management of de personen belast met 
governance; 
• 
Wanneer andere informatie verwacht wordt om te worden verkregen na de datum van de 
controleverklaring. 
 
A15. Wanneer de personen belast met governance de andere informatie moeten goedkeuren voordat 
deze wordt gepubliceerd door de entiteit, is de definitieve versie van dergelijke andere informatie 
degene die is goedgekeurd voor publicatie door de personen belast met governance. 
 
A16. In sommige gevallen kan het jaarrapport van de entiteit één enkel document zijn dat in 
overeenstemming met wet- of regelgeving of de praktijk van rapportage door de entiteit, vlak na 
de periode van financiële rapportage dient te worden gepubliceerd, zodat het voor de datum van 
de controleverklaring beschikbaar is voor de auditor. In andere gevallen is het niet vereist om zo’n 
document te publiceren tot op een later tijdstip of tot op een tijdstip dat de entiteit uitkiest. Er 
kunnen ook omstandigheden zijn waarbij het jaarrapport van de entiteit een combinatie is van 
documenten, die met betrekking tot de timing van hun publicatie elk zijn onderworpen aan 
verschillende vereisten of een andere rapporteringspraktijk door de entiteit. 
 
A17. Er kunnen omstandigheden zijn waarbij de entiteit, op de datum van de controleverklaring, de 
ontwikkeling van een document dat onderdeel van het jaarrapport van de entiteit kan zijn, 
overweegt, maar dat het management niet in staat is om aan de auditor het doel of de timing van 
een dergelijk document te bevestigen. Als de auditor niet in staat is om het doel of timing van een 
dergelijk document vast te stellen, wordt het document niet beschouwd als andere informatie voor 
de doelstellingen van deze ISA. 
 
A18. Het tijdig vóór de datum van de controleverklaring verkrijgen van de andere informatie maakt het 
mogelijk om wijzigingen die nodig worden geacht aan te brengen in de financiële overzichten, de 
controleverklaring 
of 
de 
andere 
informatie 
voordat 
zij 
worden 
gepubliceerd. 
De 
opdrachtbevestiging6 kan refereren aan een overeenkomst met het management om de andere 
informatie tijdig ter beschikking te stellen aan de auditor en indien mogelijk vóór de datum van de 
controleverklaring.  
 
A19. Wanneer andere informatie alleen beschikbaar wordt gesteld aan gebruikers via de website van 
de entiteit, is de versie van de andere informatie verkregen van de entiteit, in plaats van de versie 
direct van de website van de entiteit, het desbetreffende document waarop de auditor 
werkzaamheden zou verrichten in overeenstemming met deze ISA. De auditor heeft onder deze 
ISA geen verantwoordelijkheid om te zoeken naar andere informatie, inclusief andere informatie 
die op de website kan staan, of om werkzaamheden uit te voeren die bevestigen dat andere 
informatie op passende wijze wordt weergegeven op de website van de entiteit of anderszins 
adequaat is doorgegeven of elektronisch weergegeven. 
 
A20. Het is de auditor niet verboden om de controleverklaring te dateren of uit te geven wanneer de 
auditor bepaalde of alle andere informatie niet heeft verkregen. 
 
A21. Wanneer de andere informatie wordt verkregen na de datum van controleverklaring, is de auditor 
niet verplicht om de werkzaamheden uitgevoerd in overeenstemming met paragrafen 6 en 7 van 
ISA 5607 bij te werken. 
 
 
6  
ISA 210, Overeenkomen van de voorwaarden van controleopdrachten, paragraaf A24. 
7  
ISA 560, Gebeurtenissen na de einddatum van de verslagperiode.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
13/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
A22. ISA 5808 stelt vereisten vast en geeft leidraden voor het gebruik van schriftelijke bevestigingen. 
De schriftelijke bevestiging vereist in paragraaf 13 (c) met betrekking tot andere informatie die 
beschikbaar zal zijn na de datum van de controleverklaring, is bedoeld ter ondersteuning van de 
mogelijkheid van de auditor om de werkzaamheden vereist in deze ISA met betrekking tot andere 
informatie te voltooien. Bovendien kan de auditor het nuttig achten om andere schriftelijke 
bevestigingen te verzoeken bijvoorbeeld dat: 
 
• 
Management de auditor heeft geïnformeerd over alle documenten die het verwacht te 
publiceren die mogelijk andere informatie vormen;  
• 
De financiële overzichten en alle andere informatie die door de auditor is verkregen vóór 
de datum van de controleverklaring consistent zijn met elkaar en dat de andere informatie 
geen afwijkingen van materieel belang bevat; en 
• 
Met betrekking tot andere informatie die niet voor de datum van de controleverklaring door 
de auditor is verkregen, het management van plan is deze andere informatie op te stellen 
en te publiceren en het verwachte tijdstip van de publicatie. 
 
Lezen en overwegen van de andere informatie (Zie par. 14-15) 
 
 
A23. ISA 2009 vereist van de auditor om de controle te plannen en uit te voeren met een professioneel-
kritische instelling. Handhaving van een professioneel-kritische instelling bij het lezen en 
overwegen van de andere informatie bevat bijvoorbeeld erkennen dat het management te 
optimistisch kan zijn over het succes van zijn plannen en alert zijn op informatie die inconsistent 
kan zijn met: 
 
(a) 
De financiële overzichten; of 
(b) 
Kennis van de auditor verkregen in de controle. 
 
A24. In overeenstemming met ISA 220 (herzien) is van 
de opdrachtpartner 
vereist om 
verantwoordelijkheid te nemen voor de aansturing van en het toezicht op de leden van het 
opdrachtteam, alsmede voor de beoordeling van hun werk,10 en te bepalen dat de aard, timing 
en omvang van de aansturing, het toezicht en de beoordeling wordt gepland en uitgevoerd in 
overeenstemming met de beleidslijnen of procedures van het kantoor, met professionele 
standaarden en met van toepassing zijnde vereisten uit wet- en regelgeving.11 In de context van 
deze ISA, omvatten factoren waarmee rekening kan worden gehouden bij het bepalen van de 
leden van het opdrachtteam die geschikt zijn om de vereisten van paragrafen 14-15 te 
behandelen: 
 
• 
De relatieve ervaring van de leden van het opdrachtteam; 
• 
De vraag of de leden van het opdrachtteam die worden toegewezen aan de taken de 
relevante kennis hebben verkregen om inconsistenties tussen de andere informatie en die 
kennis te identificeren;  
• 
De mate van oordeelsvorming die benodigd is bij het behandelen van de vereisten van 
paragrafen 14-15. Bijvoorbeeld werkzaamheden met als doel de consistentie te evalueren 
tussen bedragen in de andere informatie die bedoeld is om hetzelfde te zijn als de 
bedragen in de financiële overzichten, kunnen uitgevoerd worden door minder ervaren 
leden van het opdrachtteam; 
• 
De vraag of het, in het geval van een groepscontrole, noodzakelijk is om een auditor van 
een groepsonderdeel om inlichtingen te verzoeken bij het behandelen van de andere 
informatie die betrekking heeft op dat groepsonderdeel. 
 
 
8 
ISA 580, Schriftelijke bevestigingen. 
9  
ISA 200, paragraaf 15. 
10  ISA 220 (herzien), Kwaliteitsmanagement voor een controle van financiële overzichten, paragrafen 29-30. 
11  ISA 220 (herzien), paragraaf 30(a).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
14/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Beschouwen of er een inconsistentie van materieel belang is tussen de andere informatie en de 
financiële overzichten (Zie par. 14(a)) 
 
A25. Andere informatie kan bedragen of andere elementen bevatten die bedoeld zijn om hetzelfde te 
zijn, om samen te vatten of om een grotere detaillering te verschaffen over de bedragen of andere 
elementen in de financiële overzichten. Voorbeelden van zulke bedragen of andere elementen 
kunnen omvatten: 
 
• 
Tabellen of grafieken die uittreksels van de financiële overzichten bevatten. 
• 
Een toelichting die een grotere detaillering bevat over een saldo of rekening in de financiële 
overzichten zoals “Opbrengsten voor 20X1 bestaan uit XXX miljoen van product X en YYY 
miljoen van product Y.” 
• 
Beschrijvingen 
van 
de 
financiële 
resultaten 
zoals 
“Totale 
onderzoeks- 
en 
ontwikkelingsuitgaven waren XXX in 20X1.” 
 
 
A26. Bij het evalueren van de consistentie van geselecteerde bedragen of andere elementen in de 
andere informatie met de financiële overzichten,  is van de auditor niet vereist om alle bedragen 
of andere elementen in de andere informatie die bedoeld zijn om hetzelfde te zijn, om samen te 
vatten of om een grotere detaillering te verschaffen over bedragen of andere elementen in de 
financiële overzichten te vergelijken met dergelijke bedragen of andere elementen in de financiële 
overzichten. 
 
A27. Het selecteren van de bedragen of andere elementen om te vergelijken is een kwestie van 
professionele oordeelsvorming. Factoren die relevant zijn voor deze oordeelsvorming omvatten: 
 
• 
De significantie van het bedrag of ander element in de context waarin het wordt 
gepresenteerd, wat een impact kan hebben op het belang dat gebruikers aan het bedrag 
of andere element zouden kunnen hechten (bijvoorbeeld een kernverhoudingscijfer of 
bedrag);  
• 
Indien kwantitatief, de relatieve grootte van het bedrag vergeleken met rekeningen of 
elementen in de financiële overzichten of de andere informatie waarop zij betrekking 
hebben; 
• 
De gevoeligheid van het specifieke bedrag of andere element in de andere informatie, 
bijvoorbeeld op aandelen gebaseerde betalingen voor het senior management. 
 
A28. Het bepalen van de aard en omvang van de werkzaamheden benodigd om aan de vereiste in 
paragraaf 14(a) te voldoen is een kwestie van professionele oordeelsvorming, waarbij wordt 
onderkend dat de verantwoordelijkheden van de auditor onder deze ISA geen assurance-
opdracht ten aanzien van de andere informatie vormen en geen verplichting opleggen om 
assurance te verkrijgen over de andere informatie. Voorbeelden van dergelijke werkzaamheden 
omvatten: 
 
• 
Voor informatie die bedoeld is om hetzelfde te zijn als informatie in de financiële 
overzichten, vergelijken van de informatie met de financiële overzichten; 
• 
Voor informatie die bedoeld is om dezelfde betekenis als de toelichtingen in de financiële 
overzichten over te brengen, vergelijken van de gebruikte woorden en overwegen van de 
significantie van verschillen in de gebruikte woorden en of zulke verschillen verschillende 
betekenissen impliceren; 
• 
Van het management verkrijgen van een aansluiting tussen een bedrag in de andere 
informatie en de financiële overzichten en: 
 
o 
Vergelijken van elementen in de aansluiting met de financiële overzichten en de 
andere informatie; en 
o 
Controleren of de berekeningen in de aansluiting rekenkundig juist zijn.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
15/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
A29. Evalueren van de consistentie van geselecteerde bedragen of andere elementen in de andere 
informatie met de financiële overzichten omvat, wanneer dit relevant is gegeven de aard van de 
andere informatie, de wijze van hun presentatie vergeleken met de financiële overzichten. 
 
Beschouwen of er een inconsistentie van materieel belang is tussen de andere informatie en de kennis 
van de auditor verkregen in de controle (Zie par. 14(b)) 
 
A30. Andere informatie kan bedragen of elementen omvatten die betrekking hebben op de kennis van 
de auditor verkregen in de controle (anders dan die in paragraaf 14(a)). Voorbeelden van 
dergelijke bedragen of elementen omvatten: 
 
• 
Een toelichting van de geproduceerde eenheden, of een tabel die dergelijke productie 
samenvat per geografisch gebied; 
• 
Een vermelding dat “De vennootschap product X en product Y heeft geïntroduceerd 
gedurende het jaar”; 
• 
Een samenvatting van de locaties van de belangrijkste activiteiten van de entiteit, zoals 
“Het belangrijkste centrum van de activiteiten is in land X, en er zijn ook activiteiten in 
landen Y en Z.” 
 
A31. De kennis van de auditor verkregen in de controle omvat het inzicht van de auditor in de entiteit 
en haar omgeving, het van toepassing zijnde stelsel inzake financiële verslaggeving en, het 
systeem van interne beheersing van de entiteit, verkregen in overeenstemming met ISA 315 
(herzien 2019)12. ISA 315 (herzien 2019) zet het vereiste inzicht van de auditor uiteen, hetgeen 
aangelegenheden omvat zoals het verkrijgen van inzicht in: 
 
(a) 
de organisatiestructuur, eigendom en governance en bedrijfsmodel van de entiteit, 
inclusief de mate waarin het bedrijfsmodel het gebruik van IT integreert 
(b) 
 relevante sectorspecifieke factoren, regelgeving en andere externe factoren; 
(c) 
de relevante gebruikte interne en externe maatregelen om de financiële prestaties van 
de entiteit te beoordelen. 
 
A32. De kennis van de auditor verkregen in de controle kan ook aangelegenheden omvatten die van 
toekomstgerichte aard zijn. Dergelijke 
aangelegenheden kunnen bijvoorbeeld zakelijke 
vooruitzichten en toekomstige kasstromen omvatten die de auditor heeft overwogen bij het 
evalueren van de veronderstellingen die gebruikt zijn door het management bij het uitvoeren van 
toetsingen van bijzondere waardeverminderingen van immateriële activa zoals goodwill, of bij het 
evalueren van de inschatting van het management van de mogelijkheid van de entiteit om haar 
continuïteit te handhaven. 
 
A33. Bij het overwegen of er een inconsistentie van materieel belang is tussen de andere informatie en 
de kennis van de auditor verkregen in de controle, kan de auditor zich richten op de 
aangelegenheden in de andere informatie die van voldoende belang zijn zodat een afwijking van 
de andere informatie met betrekking tot die aangelegenheid van materieel belang zou kunnen zijn. 
 
A34. Met betrekking tot vele aangelegenheden in de andere informatie, kan de herinnering van de 
auditor aan de verkregen controle-informatie en aan de bereikte conclusies in de controle 
voldoende zijn om de auditor in staat te stellen te overwegen of er een inconsistentie van materieel 
belang is tussen de andere informatie en de kennis van de auditor verkregen in de controle. Hoe 
meer ervaren en meer  vertrouwd de auditor met de belangrijkste aspecten van de controle is, 
hoe waarschijnlijker het is dat de herinnering van de auditor aan relevante aangelegenheden 
voldoende zal zijn. De auditor kan bijvoorbeeld in het licht van zijn herinnering aan discussies 
gehouden met het management of de personen belast met governance of in het licht van 
bevindingen uit gedurende de controle uitgevoerde werkzaamheden,  zoals het lezen van notulen 
van bestuursvergaderingen, in staat zijn om te overwegen of er een inconsistentie van materieel 
belang bestaat tussen de andere informatie en de kennis van de auditor verkregen in de controle, 
zonder dat het noodzakelijk is om verdere actie te ondernemen. 
 
12  ISA 315 (herzien 2019), Risico’s op een afwijking van materieel belang identificeren en inschatten, paragraaf 19-27.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
16/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A35. De auditor kan bepalen dat het verwijzen naar relevante controledocumentatie of het bij relevante 
leden van het opdrachtteam of relevante auditors van groepsonderdelen verzoeken om 
inlichtingen geschikt is als basis voor de overweging van de auditor of een inconsistentie van 
materieel belang bestaat. Bijvoorbeeld: 
 
• 
Wanneer de andere informatie de geplande beëindiging van een belangrijke productlijn 
beschrijft kan de auditor, alhoewel hij zich bewust is van de geplande beëindiging, ter 
ondersteuning van zijn beschouwing of de beschrijving materieel inconsistent is met de 
kennis van de auditor verkregen tijdens de controle, om inlichtingen verzoeken bij het 
teamlid die de controlewerkzaamheden op dit gebied heeft uitgevoerd; 
• 
Wanneer de andere informatie belangrijke details beschrijft van een rechtszaak waarop 
was ingespeeld in de controle, maar de auditor zich deze details niet adequaat kan 
herinneren, kan het nodig zijn om te verwijzen naar de controledocumentatie waar 
dergelijke gegevens zijn samengevat om zo de herinnering van de auditor te ondersteunen. 
 
A36. Of, en zo ja in welke mate, de auditor verwijst naar relevante controledocumentatie, of om 
inlichtingen verzoekt bij betrokken leden van het opdrachtteam of relevante auditors van 
groepsonderdelen, is een kwestie van professionele oordeelsvorming. Het is echter voor de 
auditor niet nodig om te verwijzen naar relevante controledocumentatie, of om inlichtingen te 
verzoeken bij de betrokken 
leden van het opdrachtteam of auditors van relevante 
groepsonderdelen over elke aangelegenheid opgenomen in de andere informatie. 
 
Alert blijven op andere indicaties dat de andere informatie een afwijking van materieel belang lijkt te 
bevatten (Zie par. 15) 
 
A37. Andere informatie kan de bespreking van aangelegenheden omvatten die geen verband houden 
met de financiële overzichten en kan ook verder reiken dan de kennis van de auditor verkregen in 
de controle. De andere informatie kan bijvoorbeeld vermeldingen omvatten over de emissies van 
broeikasgassen van de entiteit. 
 
A38. Alert blijven op andere indicaties dat de andere informatie, die geen betrekking heeft op de 
financiële overzichten of op de kennis van de auditor verkregen in de controle, een afwijking van 
materieel belang lijkt te bevatten, helpt de auditor bij het voldoen aan relevante ethische 
voorschriften die vereisen dat de auditor vermijdt om bewust te worden geassocieerd met andere 
informatie waarvan de auditor van mening is dat deze een materieel onjuiste of misleidende 
vermelding bevat, op onzorgvuldige wijze is verstrekt of de noodzakelijke informatie weglaat of 
verhult als gevolg waarvan de andere informatie als misleidend kan worden ervaren13. Alert blijven 
op andere indicaties dat de andere informatie een afwijking van materieel belang lijkt te bevatten, 
zou mogelijkerwijs erin kunnen resulteren dat de auditor dergelijke aangelegenheden identificeert 
als: 
 
• 
Verschillen tussen de andere informatie en de algemene kennis, afgezien van de kennis 
verkregen in de controle, van het opdrachtteamlid die de andere informatie leest die ertoe 
leidt dat de auditor van mening is dat de andere informatie een afwijking van materieel 
belang lijkt te bevatten; 
• 
Een interne inconsistentie in de andere informatie die ertoe leidt dat de auditor van mening 
is dat de andere informatie een afwijking van materieel belang lijkt te bevatten. 
 
Reageren wanneer een inconsistentie van materieel belang lijkt te bestaan of andere informatie 
een afwijking van materieel belang lijkt te bevatten (Zie par. 16) 
 
A39. Als onderdeel van de bespreking van de auditor met het management over een inconsistentie van 
materieel belang (of andere informatie die een afwijking van materieel belang lijkt te bevatten) kan 
het management worden verzocht onderbouwingen te verstrekken welke de vermeldingen van 
het management in de andere informatie ondersteunen. Verdere informatie of uitleg van het 
 
13  IESBA Code, paragraaf R111.2.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
17/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
management kan de auditor ervan overtuigen dat de andere informatie geen afwijking van 
materieel belang bevat. Uitleg van het management kan bijvoorbeeld redelijke en voldoende 
gronden voor geldige verschillen van oordeelsvorming aangeven. 
 
A40. Omgekeerd kan de discussie met het management verdere informatie opleveren die de conclusie 
van de auditor ondersteunt dat er een afwijking van materieel belang in de andere informatie 
bestaat. 
 
A41. Het kan moeilijker zijn voor de auditor om het management uit te dagen over kwesties van 
oordeelsvorming dan over die van een meer feitelijke aard. Toch kunnen er omstandigheden zijn 
waarin de auditor tot de conclusie komt dat de andere informatie een vermelding bevat die niet 
consistent is met de financiële overzichten of de kennis van de auditor verkregen in de controle. 
Deze omstandigheden kunnen twijfel doen ontstaan over de andere informatie, de financiële 
overzichten, of de kennis van de auditor verkregen in de controle. 
 
A42. Aangezien er een breed scala is van mogelijke afwijkingen van materieel belang van de andere 
informatie, zijn de aard en de omvang van andere werkzaamheden die de auditor kan uitvoeren 
om te concluderen of er een afwijking van materieel belang in de andere informatie bestaat, 
kwesties van de professionele oordeelsvorming van de auditor onder 
de gegeven 
omstandigheden. 
 
A43. Wanneer een aangelegenheid geen verband houdt met de financiële overzichten of de kennis van 
de auditor verkregen in de controle, kan het zijn dat de auditor niet in staat is om antwoorden van 
het management op vragen van de auditor volledig te kunnen beoordelen. Niettemin kan nadere 
informatie of uitleg van het management, of wijzigingen gemaakt door het management in de 
andere informatie, de auditor ervan overtuigen dat een inconsistentie van materieel belang niet 
meer lijkt te bestaan of dat de andere informatie niet langer afwijkingen van materieel belang lijkt 
te bevatten. Wanneer de auditor niet in staat is om te concluderen dat een inconsistentie van 
materieel belang niet meer lijkt te bestaan of dat de andere informatie niet langer een afwijking 
van materieel belang lijkt te bevatten, kan de auditor het management verzoeken een 
gekwalificeerde derde partij te consulteren (bijvoorbeeld een door het management ingeschakelde 
deskundige of een juridische adviseur). In bepaalde gevallen kan de auditor, na overweging van 
de uitkomsten van de consultaties van het management niet concluderen of er een afwijking van 
materieel belang in de andere informatie bestaat. Maatregelen die de auditor dan kan nemen, 
omvatten één of meer van de volgende: 
 
• 
Verkrijgen van advies van de juridische adviseur van de auditor; 
• 
Beschouwen van de implicatie voor de controleverklaring bijvoorbeeld het beschrijven van 
de omstandigheden als er een beperking is opgelegd door het management; of 
• 
Teruggeven van de opdracht (in het geval teruggeven mogelijk is overeenkomstig de van 
toepassing zijnde wet- of regelgeving). 
 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de andere 
informatie bestaat 
 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang bestaat in de andere 
informatie verkregen vóór de datum van de controleverklaring (Zie par. 18) 
 
A44. De maatregelen die de auditor neemt als de andere informatie niet wordt gecorrigeerd na het 
communiceren met de personen belast met governance zijn een kwestie van professionele 
oordeelsvorming van de auditor. De auditor kan rekening houden met de vraag of de 
beweegreden gegeven door het management en de personen belast met governance voor het 
niet maken van de correctie twijfel over de integriteit of eerlijkheid van het management of de 
personen belast met governance verhoogt, zoals wanneer de auditor een intentie om te misleiden 
vermoedt. De auditor kan ook het passend achten om juridisch advies in te winnen. In sommige 
gevallen kan van de auditor worden vereist door wet- of regelgeving of andere professionele

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
18/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
standaarden om de aangelegenheid te communiceren met een regelgever of toezichthouder of 
relevante beroepsorganisatie. 
 
Implicaties voor de verklaring (Zie par. 18(a)) 
 
A45. In zeldzame omstandigheden kan een oordeelonthouding over de financiële overzichten passend 
zijn wanneer de weigering om de afwijking van materieel belang in de andere informatie te 
corrigeren een zodanige twijfel over de integriteit van het management en de personen belast met 
governance opwerpt dat de betrouwbaarheid van de controle-informatie in het algemeen ter 
discussie wordt gesteld. 
 
Teruggeven van de opdracht (Zie par. 18(b)) 
 
A46. Teruggeven van de opdracht, in het geval teruggeven mogelijk is overeenkomstig de van 
toepassing zijnde wet- of regelgeving, kan geschikt zijn wanneer de omstandigheden rond de 
weigering om de afwijkingen van materieel belang in de andere informatie te corrigeren een 
zodanige twijfel over de integriteit van het management en de personen belast met governance 
oproept dat de betrouwbaarheid van de bevestigingen die van hen zijn verkregen tijdens de 
controle ter discussie wordt gesteld. 
  
Overwegingen die specifiek voor entiteiten in de publieke sector gelden (Zie par. 18(b)) 
 
A47. In de publieke sector kan het teruggeven van de opdracht niet mogelijk zijn. In dergelijke gevallen 
kan de auditor een rapportage voor de wetgever publiceren die details verschaft van de 
aangelegenheid of hij kan andere passende maatregelen nemen. 
 
Reageren wanneer de auditor concludeert dat er een afwijking van materieel belang in de andere 
informatie bestaat verkregen na de datum van de controleverklaring (Zie par. 19) 
 
A48. Als de auditor tot de conclusie komt dat er een afwijking van materieel belang bestaat in de andere 
informatie verkregen na de datum van de controleverklaring en een degelijke afwijking van 
materieel belang is gecorrigeerd, omvatten de werkzaamheden van de auditor die noodzakelijk 
zijn in de omstandigheden het bepalen dat de correctie is gemaakt (overeenkomstig paragraaf 17 
(a)) en kunnen deze het beoordelen van de stappen die zijn genomen door het management om 
te communiceren met degenen die de overige gegevens ontvangen, indien eerder gepubliceerd, 
om hen te informeren over de herziening, omvatten. 
 
A49. Als de personen belast met governance het niet eens zijn met het herzien van de andere 
informatie, vereist het nemen van passende maatregelen teneinde te trachten de ongecorrigeerde 
afwijking gepast onder de aandacht te brengen van de gebruikers voor wie de controleverklaring 
wordt opgesteld, de uitoefening van de professionele oordeelsvorming, en kan dit worden 
beïnvloed door relevante wet- of regelgeving in het rechtsgebied. Derhalve kan de auditor het 
passend achten om juridisch advies over de wettelijke rechten en verplichtingen van de auditor 
in te winnen. 
 
 
A50. Wanneer een afwijking van materieel belang in de andere informatie ongecorrigeerd blijft, 
omvatten passende maatregelen die de auditor wanneer dit is toegestaan door de wet of 
regelgeving kan nemen teneinde te trachten de ongecorrigeerde afwijking van materieel belang 
op passende wijze onder de aandacht van de gebruikers voor wie de controleverklaring wordt 
opgesteld te brengen, bijvoorbeeld: 
 
• 
Het verstrekken van een nieuwe of gewijzigde controleverklaring aan het management, 
inclusief een aangepaste sectie overeenkomstig paragraaf 22, en verzoeken aan het 
management om deze nieuwe of 
gewijzigde controleverklaring te verstrekken aan 
gebruikers voor wie de controleverklaring wordt opgesteld. Daarbij kan het nodig zijn dat 
de auditor het eventuele effect op de datum van de nieuwe of gewijzigde controleverklaring 
overweegt, met het oog op de vereisten van de ISA’s of toepasselijke wet- of regelgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
19/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
De auditor kan ook de stappen genomen door het management om de nieuwe of gewijzigde 
controleverklaring aan dergelijke gebruikers te verschaffen, beoordelen; 
• 
Het onder de aandacht brengen van de afwijking van materieel belang in de andere 
informatie van de gebruikers voor wie de controleverklaring is opgesteld (bijvoorbeeld door 
het behandelen van de aangelegenheid in een algemene vergadering van 
aandeelhouders); 
• 
Het communiceren met een regelgever of toezichthouder of relevante beroepsorganisatie 
over de ongecorrigeerde afwijking van materieel belang; of 
• 
Het overwegen van de implicaties voor het continueren van de opdracht (zie ook paragraaf 
A46). 
 
Reageren wanneer er een afwijking van materieel belang in de financiële overzichten bestaat of 
het inzicht van de auditor in de entiteit en haar omgeving moet worden geactualiseerd (Zie par. 
20) 
 
A51. Bij het lezen van de andere informatie, kan de auditor zich bewust worden van nieuwe informatie 
die implicaties heeft voor: 
 
• 
Het inzicht van de auditor in de entiteit en haar omgeving, het stelsel inzake financiële 
verslaggeving en het systeem van interne beheersing van de entiteit en kan daarom de 
noodzaak om de risicoanalyse van de auditor te herzien, aanduiden;14 
• 
De verantwoordelijkheid van de auditor om het effect van onderkende afwijkingen op de 
controle en van eventuele niet gecorrigeerde afwijkingen op de financiële overzichten te 
evalueren;15 
• 
De verantwoordelijkheden van de auditor met betrekking tot gebeurtenissen na de 
einddatum van de verslagperiode.16 
 
Rapportage (Zie par. 21-24) 
 
A52. Voor een controle van de financiële overzichten van een niet-beursgenoteerde entiteit, kan de 
auditor in overweging nemen dat de identificatie in de controleverklaring van de andere informatie 
die de auditor verwacht te krijgen na de datum van de controleverklaring geschikt zou zijn om 
extra 
transparantie over de andere informatie te verschaffen die valt onder de 
verantwoordelijkheid van de auditor in het kader van deze ISA. De auditor kan het nodig achten 
om dat te doen, bijvoorbeeld wanneer het management in staat is om aan de auditor te bevestigen 
dat dergelijke andere informatie zal worden gepubliceerd na de datum van de controleverklaring. 
 
Voorbeelden van verklaringen (Zie par. 21-22) 
 
A53. Voorbeelden van de sectie “Andere informatie” in de controleverklaring zijn opgenomen in Bijlage 
2. 
 
Implicaties voor de verklaring wanneer het oordeel van de auditor over de financiële overzichten een 
oordeel met beperking of een afkeurend oordeel is (Zie par. 23) 
 
A54. Een oordeel met beperking of afkeurend oordeel over de financiële overzichten hoeft geen impact 
te hebben op de verklaring vereist door paragraaf 22(e) als de aangelegenheid waardoor het 
oordeel van de auditor is gewijzigd, niet is opgenomen of op andere wijze is behandeld in de 
andere informatie en de aangelegenheid geen invloed heeft op een deel van de andere informatie. 
Een oordeel met beperking over de financiële overzichten als gevolg van niet-openbaarmaking 
van de beloning van bestuurders, zoals vereist door het van toepassing zijnde stelsel inzake 
financiële verslaggeving, zou bijvoorbeeld geen implicaties kunnen hebben voor de rapportage 
vereist onder deze ISA. In andere omstandigheden kunnen er implicaties voor deze rapportage 
zijn zoals beschreven in de paragrafen A55-A58.  
 
14  ISA 315 (herzien 2019), paragrafen 19-26 en 37. 
15 ISA 450, Evaluatie van tijdens de controle geïdentificeerde afwijkingen. 
16 ISA 560, paragrafen 10 en 14.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
20/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Oordeel met beperking vanwege een afwijking van materieel belang in de financiële overzichten 
 
A55. In omstandigheden waarin de auditor een oordeel met beperking tot uitdrukking brengt, kan 
worden overwogen of de andere informatie ook een afwijking van materieel belang bevat voor 
dezelfde aangelegenheid als, of een verwante aangelegenheid aan, de aangelegenheid die 
aanleiding geeft tot het oordeel met beperking over de financiële overzichten. 
 
Oordeel met beperking vanwege een beperking in de reikwijdte 
 
A56. Wanneer er sprake is van een beperking in de reikwijdte van de controle van een materieel 
element in de financiële overzichten, zal de auditor niet voldoende en geschikte controle-
informatie over die aangelegenheid hebben verkregen. In deze omstandigheden kan de auditor 
niet in staat zijn om te concluderen of de bedragen of andere elementen in de andere informatie 
met betrekking tot deze aangelegenheid resulteren in een afwijking van materieel belang in de 
andere informatie. Dienovereenkomstig, kan het nodig zijn dat de auditor de verklaring vereist 
door paragraaf 22 (e) aanpast door te verwijzen naar de onmogelijkheid van de auditor om de 
beschrijving van de aangelegenheid door het management in de andere informatie te overwegen 
waarover het oordeel van de auditor over de financiële overzichten beperkt is zoals uitgelegd in 
de paragraaf Basis voor ons oordeel met beperking. Van de auditor is niettemin vereist om 
eventuele andere niet-gecorrigeerde afwijkingen van materieel belang in de andere informatie die 
zijn geïdentificeerd, te rapporteren. 
 
Afkeurend oordeel 
 
A57. Een afkeurend oordeel over de financiële overzichten dat betrekking heeft op (een) bepaalde 
aangelegenhe(i)d(en) beschreven in de paragraaf Basis voor ons afkeurend oordeel rechtvaardigt 
niet het in de controleverklaring weglaten van het overeenkomstig paragraaf 22(e)(ii) rapporteren 
van afwijkingen van materieel belang die de auditor heeft geïdentificeerd in de andere informatie 
. Wanneer een afkeurend oordeel over de financiële overzichten tot uitdrukking is gebracht, kan 
het nodig zijn dat de auditor de verklaring vereist door paragraaf 22(e) op passende wijze aanpast, 
bijvoorbeeld om aan te geven dat de bedragen of elementen in de andere informatie een afwijking 
van materieel belang 
bevatten voor dezelfde aangelegenheid als, of een verwante 
aangelegenheid aan, de aangelegenheid die aanleiding geeft tot de afkeurende verklaring over 
de financiële overzichten. 
 
Oordeelonthouding 
 
A58. Wanneer de auditor een oordeelonthouding over de financiële overzichten formuleert, kan het 
verschaffen van nadere details over de controle, inclusief een sectie om de andere informatie te 
behandelen, de oordeelonthouding over de financiële overzichten als geheel overschaduwen. 
Dienovereenkomstig, omvat de controleverklaring in die omstandigheden, zoals vereist door ISA 
705 (herzien), geen sectie die de rapportagevereisten van deze ISA behandelt. 
 
Rapportage voorgeschreven door wet- of regelgeving (Zie par. 24) 
 
 
A59. ISA 20017 legt uit dat van de auditor kan worden vereist te voldoen aan de vereisten op grond van 
wet- of regelgeving in aanvulling op de ISA’s. Indien dit het geval is, kan de auditor worden 
verplicht een specifieke lay-out of formulering te gebruiken in de controleverklaring die verschilt 
van degene die in deze ISA is beschreven. Consistentie in de controleverklaring, wanneer de 
controle is uitgevoerd in overeenstemming met de ISA’s, bevordert de geloofwaardigheid in de 
wereldwijde markt door die controles die overeenkomstig wereldwijd erkende ISA’s zijn uitgevoerd, 
makkelijker herkenbaar te maken. Wanneer de verschillen tussen de vereisten op grond van wet- 
of regelgeving om te rapporteren met betrekking tot de andere informatie en deze ISA alleen 
betrekking hebben op de lay-out en de formulering in de controleverklaring en tenminste elk van 
de elementen die in paragraaf 24 zijn geïdentificeerd, is opgenomen in de controleverklaring, kan 
de controleverklaring verwijzen naar de International Standards on Auditing. Dienovereenkomstig, 
 
17 ISA 200, paragraaf A60.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
21/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
in dergelijke omstandigheden wordt de auditor geacht te hebben voldaan aan de vereisten van 
deze ISA, zelfs wanneer de lay-out en de formulering van de controleverklaring worden 
gespecificeerd door vereisten op grond van wet- of regelgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
22/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Bijlage 1 
(Zie par. 14, A8) 
 
Voorbeelden van bedragen of andere elementen die kunnen worden opgenomen in de andere 
informatie 
 
Hierna volgen voorbeelden van bedragen en andere elementen die kunnen worden opgenomen in de 
andere informatie. Deze lijst is niet bedoeld uitputtend te zijn. 
 
Bedragen 
• 
Elementen in een samenvatting van de belangrijkste financiële resultaten, zoals nettowinst, winst 
per aandeel, dividend, omzet en overige operationele bedrijfsopbrengsten, en aankopen en 
operationele kosten. 
• 
Geselecteerde bedrijfsgegevens, zoals inkomsten uit voortgezette bedrijfsactiviteiten per 
belangrijk operationeel gebied, of omzet per geografisch segment of productlijn. 
• 
Speciale elementen, zoals de verkoop van activa, voorzieningen voor rechtszaken, bijzondere 
waardeverminderingen, 
fiscale 
aanpassingen, 
voorzieningen 
voor 
milieusanering, 
en 
herstructurerings- en reorganisatiekosten. 
• 
Liquiditeit en kapitaalbronnen informatie, zoals geldmiddelen, kasequivalenten en verhandelbare 
effecten; 
dividenden; 
en 
schulden, 
financiële 
lease 
en 
rente 
verplichtingen 
van 
minderheidsbelangen. 
• 
De investeringen per segment of divisie. 
• 
Bedragen die betrokken zijn bij, en aanverwante financiële gevolgen van, niet in de balans 
opgenomen overeenkomsten. 
• 
Bedragen die betrokken zijn bij garanties, contractuele verplichtingen, juridische of milieuclaims, 
en andere voorwaardelijke gebeurtenissen. 
• 
Financiële maatregelen of ratio's, zoals bruto marge, rendement op het gemiddeld geïnvesteerd 
vermogen, rendement op het gemiddeld eigen vermogen, current ratio, interest coverage ratio en 
de debt ratio. Sommige van deze kunnen direct aan te sluiten zijn met de financiële overzichten. 
 
Andere elementen 
 
• 
Uitleg van belangrijke schattingen en gerelateerde veronderstellingen. 
• 
Identificatie van verbonden partijen en een beschrijving van transacties met hen. 
• 
Duidelijke uitdrukking van de beleidslijnen of de aanpak van de entiteit inzake het beheer van 
grondstoffen, vreemde valuta of renterisico’s, zoals door het gebruik van termijncontracten, 
renteswaps of andere financiële instrumenten. 
• 
Beschrijvingen van de aard van de off-balance sheet regelingen. 
• 
Beschrijvingen van garanties, vrijwaringen, contractuele verplichtingen, rechtszaken of 
milieuaansprakelijkheidsgevallen, 
en 
andere 
voorwaardelijke 
gebeurtenissen, 
inclusief 
kwalitatieve beoordelingen van het management van gerelateerde uitstaande bedragen van de 
entiteit.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
23/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
• 
Beschrijvingen van de wijzigingen in wet- en regelgeving, zoals nieuwe belastingen of 
milieuvoorschriften, die een materiële invloed hebben gehad op de activiteiten van de entiteit of 
de fiscale positie, of een materiële invloed zullen hebben op de toekomstige financiële 
vooruitzichten van de entiteit. 
• 
Kwalitatieve beoordelingen van het management van de invloed van nieuwe standaarden voor 
financiële verslaglegging die in de periode in werking zijn getreden, of in werking zullen treden in 
de volgende periode, op de financiële resultaten van de entiteit, de financiële positie en 
kasstromen. 
• 
Algemene beschrijvingen van de bedrijfsomgeving en vooruitzichten. 
• 
Overzicht van de strategie. 
• 
Beschrijvingen van trends in marktprijzen van belangrijke goederen of grondstoffen. 
• 
Contrasten van vraag, aanbod en regelgevende omstandigheden tussen geografische regio's. 
• 
Uitleg van specifieke factoren die de winstgevendheid van de entiteit in specifieke segmenten 
beïnvloeden.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
24/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Bijlage 2 
(Zie par. 21-22, A53) 
 
Voorbeelden van controleverklaringen betreffende andere informatie 
 
• 
Voorbeeld 1 : Controleverklaring over financiële overzichten van een beursgenoteerde of van een 
niet-beursgenoteerde entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van de controleverklaring en heeft geen 
afwijking van materieel belang in de andere informatie vastgesteld 
• 
Voorbeeld 2 : Controleverklaring over financiële overzichten van een beursgenoteerde entiteit, 
die een niet-aangepast oordeel omvat, wanneer de auditor een deel van de andere informatie 
heeft verkregen voor de datum van zijn controleverklaring en verwacht de andere informatie te 
verkrijgen na de datum van zijn controleverklaring  
• 
Voorbeeld 3 : Controleverklaring over financiële overzichten van een niet-beursgenoteerde 
entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor een deel van de andere 
informatie heeft verkregen voor de datum van zijn controleverklaring, geen afwijking van materieel 
belang in de andere informatie heeft vastgesteld en andere informatie verwacht te verkrijgen na 
de datum van zijn controleverklaring 
• 
Voorbeeld 4 : Controleverklaring over financiële overzichten van een beursgenoteerde entiteit, 
die een niet-aangepast oordeel omvat, wanneer de auditor geen andere informatie heeft 
verkregen voor de datum van zijn controleverklaring, maar verwacht de andere informatie te 
verkrijgen na de datum van zijn controleverklaring 
• 
Voorbeeld 5 : Controleverklaring over financiële overzichten van een beursgenoteerde of van een 
niet-beursgenoteerde entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van zijn controleverklaring en geen afwijking 
van materieel belang in de andere informatie heeft vastgesteld  
• 
Voorbeeld 6 : Controleverklaring over financiële overzichten van een beursgenoteerde of van een 
niet-beursgenoteerde entiteit, die een oordeel met beperking omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van zijn controleverklaring en er een beperking 
bestaat in de reikwijdte van de werkzaamheden met betrekking tot een significant aspect in de 
geconsolideerde financiële overzichten die tevens een effect heeft op de andere informatie 
• 
Voorbeeld 7 : Controleverklaring over financiële overzichten van een beursgenoteerde of van een 
niet-beursgenoteerde entiteit, die een afkeurend oordeel omvat, wanneer de auditor alle andere 
informatie heeft verkregen voor de datum van zijn controleverklaring en zijn afkeurend oordeel 
over de geconsolideerde financiële overzichten tevens de andere informatie betreft

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
25/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 1 – Controleverklaring over financiële overzichten van een beursgenoteerde of van 
een niet-beursgenoteerde entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van de controleverklaring en heeft geen 
afwijking van materieel belang in de andere informatie vastgesteld 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit waarbij 
gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole (i.e., ISA 
600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in ISA 
210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien)18; 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en heeft 
geen afwijking van materieel belang in de andere informatie vastgesteld; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporteringsverplichtingen 
op grond van lokale wetgeving. 
 
 
 
 
 
 
18  ISA 570 (herzien), Continuïteit.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
26/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Verklaring over de controle van de financiële overzichten19 
 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie 
van de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor 
het op die datum afgesloten boekjaar, in overeenstemming met International Financial Reporting 
Standards (IFRS). 
 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel. 
 
[Kernpunten van onze controle20 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701]] 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.21 De andere informatie omvat [de 
informatie vervat in rapport X22, maar omvat niet de financiële overzichten en onze controleverklaring 
over deze financiële overzichten]. 
 
Ons oordeel over de financiële overzichten omvat niet de andere informatie en wij formuleren geen 
enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de financiële overzichten, zijn wij verantwoordelijk voor het 
lezen van de andere informatie en, tijdens het lezen, voor het overwegen of een inconsistentie van 
materieel belang bestaat tussen de andere informatie en de financiële overzichten of de kennis 
verkregen in de controle, dan wel of een afwijking van materieel belang in de andere informatie 
 
19  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. ) 
20  De sectie “Kernpunten van onze controle” is enkel vereist in het geval van beursgenoteerde entiteiten. 
21  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied 
22  Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, bijvoorbeeld “het 
management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
27/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
bestaat. Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat 
een afwijking van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. 
Wij hebben u hierover niets te rapporteren. 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen 23 
[Verslaggeving overeenkomstig ISA 700 (herzien)24 – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam]25 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
 
23  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
24  ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten. 
25  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
28/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 2 – Controleverklaring over financiële overzichten van een beursgenoteerde entiteit, 
die een niet-aangepast oordeel omvat, wanneer de auditor een deel van de andere informatie 
heeft verkregen voor de datum van zijn controleverklaring en verwacht de andere informatie te 
verkrijgen na de datum van zijn controleverklaring 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit waarbij 
gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole (i.e., ISA 
600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in ISA 
210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft een deel van de andere informatie verkregen voor de datum van de 
controleverklaring, heeft geen afwijking van materieel belang in de andere informatie vastgesteld 
en verwacht andere informatie te verkrijgen na de datum van zijn controleverklaring; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporteringsverplichtingen 
op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
29/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Verklaring over de controle van de financiële overzichten26 
 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie 
van de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor 
het op die datum afgesloten boekjaar, in overeenstemming met International Financial Reporting 
Standards (IFRS). 
 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel. 
 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701] 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.27 De andere informatie omvat de 
informatie vervat in rapport X28 (maar omvat niet de financiële overzichten en onze controleverklaring 
over deze financiële overzichten), die wij hebben verkregen op de datum van onze verklaring, alsook 
in rapport Y, dat wij geacht worden te ontvangen na deze datum. 
 
Ons oordeel over de financiële overzichten omvat niet de andere informatie en wij formuleren geen 
enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de financiële overzichten, zijn wij verantwoordelijk voor het 
lezen van de andere informatie en, tijdens het lezen, voor het overwegen of een inconsistentie van 
materieel belang bestaat tussen de andere informatie en de financiële overzichten of de kennis 
verkregen in de controle, dan wel of een afwijking van materieel belang in de andere informatie 
 
26  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. ) 
27  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied 
28  Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, bijvoorbeeld “het 
management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
30/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
bestaat.  
 
Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat een afwijking 
van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. Wij hebben 
u hierover niets te rapporteren. 
[Indien wij, bij het lezen van rapport Y, concluderen dat een afwijking van materieel belang in dit 
rapport bestaat, zijn wij ertoe gehouden om deze aangelegenheid te communiceren aan de met 
governance belaste personen en om [beschrijving van de maatregelen die van toepassing zijn in het 
rechtsgebied]29.] 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen30 
[Verslaggeving overeenkomstig ISA 700 (herzien)31 – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam]32 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
 
29  Deze bijkomende paragraaf kan nuttig blijken indien de auditor een ongecorrigeerde afwijking van materieel belang in de 
andere informatie die hij heeft verkregen na de datum van zijn controleverklaring identificeert en hij de juridische verplichting 
heeft om desbetreffend specifieke maatregelen te nemen.  
30  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
31  ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten. 
32  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
31/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 3 : Controleverklaring over financiële overzichten van een niet-beursgenoteerde 
entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor een deel van de andere 
informatie heeft verkregen voor de datum van zijn controleverklaring, geen afwijking van 
materieel belang in de andere informatie heeft vastgesteld en andere informatie verwacht te 
verkrijgen na de datum van zijn controleverklaring 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
 
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit waarbij 
gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole (i.e., ISA 
600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in ISA 
210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
De auditor heeft geen verplichting tot, en heeft beslist om niet over te gaan tot, het communiceren 
van kernpunten van de controle overeenkomstig ISA 701; 
• 
De auditor heeft een deel van de andere informatie verkregen voor de datum van de 
controleverklaring, heeft geen afwijking van materieel belang in de andere informatie vastgesteld 
en verwacht andere informatie te verkrijgen na de datum van zijn controleverklaring; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporteringsverplichtingen 
op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
32/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Verklaring over de controle van de financiële overzichten33 
 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie 
van de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor 
het op die datum afgesloten boekjaar, in overeenstemming met International Financial Reporting 
Standards (IFRS). 
 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel. 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.34 De andere informatie omvat [de 
informatie vervat in rapport X35, maar omvat niet de financiële overzichten en onze controleverklaring 
over deze financiële overzichten]. 
 
Ons oordeel over de financiële overzichten omvat niet de andere informatie en wij formuleren geen 
enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de financiële overzichten, zijn wij verantwoordelijk voor het 
lezen van de andere informatie en, tijdens het lezen, voor het overwegen of een inconsistentie van 
materieel belang bestaat tussen de andere informatie en de financiële overzichten of de kennis 
verkregen in de controle, dan wel of een afwijking van materieel belang in de andere informatie 
bestaat.  
 
Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat een afwijking 
van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. Wij hebben 
u hierover niets te rapporteren. 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen 36 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
33  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. ) 
34  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied 
35  Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, bijvoorbeeld “het 
management rapport of de mededeling van de voorzitter”.  
36  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
33/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum]

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
34/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 4 : Controleverklaring over financiële overzichten van een beursgenoteerde entiteit, 
die een niet-aangepast oordeel omvat, wanneer de auditor geen andere informatie heeft 
verkregen voor de datum van zijn controleverklaring, maar verwacht de andere informatie te 
verkrijgen na de datum van zijn controleverklaring 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
 
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit waarbij 
gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole (i.e., ISA 
600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in ISA 
210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft geen andere informatie verkregen voor de datum van de controleverklaring, maar 
verwacht de andere informatie nadien te verkrijgen; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporteringsverplichtingen 
op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
35/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Verklaring over de controle van de financiële overzichten37 
 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie 
van de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor 
het op die datum afgesloten boekjaar, in overeenstemming met International Financial Reporting 
Standards (IFRS). 
 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel. 
 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701] 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.38 De andere informatie omvat [de 
informatie vervat in rapport X39, maar omvat niet de financiële overzichten en onze controleverklaring 
over deze financiële overzichten]. Het rapport X worden wij geacht te ontvangen na deze 
controleverklaring. 
 
Ons oordeel over de financiële overzichten omvat niet de andere informatie en wij formuleren geen 
enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de financiële overzichten, zijn wij verantwoordelijk voor het 
lezen van de andere informatie en, tijdens het lezen, voor het overwegen of een inconsistentie van 
materieel belang bestaat tussen de andere informatie en de financiële overzichten of de kennis 
verkregen in de controle, dan wel of een afwijking van materieel belang in de andere informatie 
 
37  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. ) 
38  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied 
39  Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, bijvoorbeeld “het 
management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
36/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
bestaat.  
 
 [Indien wij, bij het lezen van rapport X, concluderen dat een afwijking van materieel belang in dit 
rapport bestaat, zijn wij ertoe gehouden om deze aangelegenheid te communiceren aan de met 
governance belaste personen en om [beschrijving van de maatregelen die van toepassing zijn in het 
rechtsgebied]40.] 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen 41 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam]42 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
 
40  Deze bijkomende paragraaf kan nuttig blijken indien de auditor een ongecorrigeerde afwijking van materieel belang in de 
andere informatie die hij heeft verkregen na de datum van zijn controleverklaring identificeert en hij de juridische verplichting 
heeft om desbetreffend specifieke maatregelen te nemen.  
41  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
42  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
37/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 5 : Controleverklaring over financiële overzichten van een beursgenoteerde of van 
een niet-beursgenoteerde entiteit, die een niet-aangepast oordeel omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van zijn controleverklaring en geen afwijking 
van materieel belang in de andere informatie heeft vastgesteld 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
 
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit waarbij 
gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole (i.e., ISA 
600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in ISA 
210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en heeft 
een afwijking van materieel belang in de andere informatie vastgesteld; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporteringsverplichtingen 
op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
38/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Verklaring over de controle van de financiële overzichten43 
 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie 
van de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor 
het op die datum afgesloten boekjaar, in overeenstemming met International Financial Reporting 
Standards (IFRS). 
 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel. 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.44 De andere informatie omvat [de 
informatie vervat in rapport X45, maar omvat niet de financiële overzichten en onze controleverklaring 
over deze financiële overzichten]. 
 
Ons oordeel over de financiële overzichten omvat niet de andere informatie en wij formuleren geen 
enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de financiële overzichten, zijn wij verantwoordelijk voor het 
lezen van de andere informatie en, tijdens het lezen, voor het overwegen of een inconsistentie van 
materieel belang bestaat tussen de andere informatie en de financiële overzichten of de kennis 
verkregen in de controle, dan wel of een afwijking van materieel belang in de andere informatie 
bestaat. Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat 
een afwijking van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. 
Zoals hierna beschreven, hebben wij geconcludeerd dat een afwijking van materieel belang in de 
andere informatie bestaat. 
 
[Beschrijving van de afwijking van materieel belang in de andere informatie] 
 
 
43  
De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de 
tweede subtitel “Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van 
toepassing is. ) 
44  
Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke 
rechtsgebied 
45  
Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, 
bijvoorbeeld “het management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
39/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
[Kernpunten van onze controle46 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701]] 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen 47 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam]48 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
 
46  
De sectie “Kernpunten van onze controle” is enkel vereist in het geval van beursgenoteerde entiteiten. 
47  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
48  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
40/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 6 : Controleverklaring over financiële overzichten van een beursgenoteerde of van 
een niet-beursgenoteerde entiteit, die een oordeel met beperking omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van zijn controleverklaring en er een beperking 
bestaat in de reikwijdte van de werkzaamheden met betrekking tot een significant aspect in de 
geconsolideerde financiële overzichten die tevens een effect heeft op de andere informatie 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen:  
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een 
beursgenoteerde entiteit waarbij gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is 
groepscontrole van een entiteit met dochtermaatschappijen (i.e., ISA 600 is van toepassing);  
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden);  
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten zoals 
opgenomen in ISA 210; 
• 
De auditor was in de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen 
met betrekking tot een in het buitenland verworven geassocieerde deelneming. De mogelijke 
effecten van de onmogelijkheid tot het verkrijgen van voldoende en geschikte controle-informatie 
worden geacht van materieel belang te zijn voor, maar niet van diepgaande invloed op, de 
geconsolideerde financiële overzichten (i.e. een oordeel met beperking is passend); 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de ethische 
vereisten die verband houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring, maar er 
bestaat een beperking in de reikwijdte van de controle met betrekking tot een significant onderdeel 
van de geconsolideerde financiële overzichten die tevens een effect heeft op de andere informatie; 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen; 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
41/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Oordeel met beperking 
Wij hebben de geconsolideerde financiële overzichten van vennootschap ABC en haar 
dochtermaatschappijen (de Groep) gecontroleerd, die bestaan uit het geconsolideerd overzicht van 
de financiële positie op 31 december 20X1, het geconsolideerde overzicht van gerealiseerde en niet-
gerealiseerde resultaten, het geconsolideerde mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip 
van een overzicht van de belangrijke grondslagen voor financiële verslaggeving.  
 
Uitgezonderd de mogelijke effecten van de aangelegenheid beschreven in de sectie ‘Basis voor ons 
oordeel met beperking’ van onze verklaring, vormen de bijhorende geconsolideerde financiële 
overzichten, naar ons oordeel, een getrouwe weergave (dan wel geven zij een getrouw beeld) van de 
geconsolideerde financiële positie van de Groep per 31 december 20X1, en van haar geconsolideerde 
financiële prestaties en kasstromen voor het op die datum afgesloten boekjaar, in overeenstemming 
met International Financial Reporting Standards (IFRS). 
 
Basis voor ons oordeel met beperking 
De investering van vennootschap ABC in vennootschap XYZ, een gedurende het boekjaar in het 
buitenland verworven geassocieerde deelneming, administratief verwerkt door middel van de equity-
methode, is opgenomen tegen een waarde van xxx op de balans per 31 december 20X1, en het aandeel 
van ABC in de nettowinst van XYZ van xxx is opgenomen in de winst van ABC voor het op die datum 
afgesloten boekjaar. We zijn niet in staat geweest om voldoende en geschikte controle-informatie te 
verkrijgen over de boekwaarde van de investering van ABC in XYZ per 31 december 20X1 en van het 
aandeel van ABC in het nettoresultaat van XYZ voor het boekjaar, omdat ons toegang tot de financiële 
informatie bij het management en bij de auditors van XYZ werd geweigerd. Bijgevolg zijn wij niet in staat 
geweest om te bepalen of eventuele aanpassingen aan deze bedragen noodzakelijk waren.  
 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de geconsolideerde financiële 
overzichten' van onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met 
de ethische vereisten die relevant zijn voor onze controle van de geconsolideerde financiële overzichten 
in [rechtsgebied], en we hebben onze overige ethische verantwoordelijkheden nageleefd in 
overeenstemming met deze vereisten. Wij zijn van mening dat de door ons verkregen controle-
informatie voldoende en geschikt is als basis voor ons oordeel met beperking. 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.49 De andere informatie omvat [de 
informatie vervat in rapport X50, maar omvat niet de geconsolideerde financiële overzichten en onze 
controleverklaring over deze geconsolideerde financiële overzichten].  
 
Ons oordeel over de geconsolideerde financiële overzichten omvat niet de andere informatie en wij 
formuleren geen enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de geconsolideerde financiële overzichten, zijn wij 
verantwoordelijk voor het lezen van de andere informatie en, tijdens het lezen, voor het overwegen of 
een inconsistentie van materieel belang bestaat tussen de andere informatie en de geconsolideerde 
financiële overzichten of de kennis verkregen in de controle, dan wel of een afwijking van materieel 
 
49  
Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke 
rechtsgebied 
50  
Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, 
bijvoorbeeld “het management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
42/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
belang in de andere informatie bestaat.  
 
Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat een afwijking 
van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. Zoals 
beschreven in de sectie “Basis voor ons oordeel met beperking”, zijn wij niet in staat geweest voldoende 
en geschikte controle-informatie te verkrijgen over de boekwaarde van de investering van ABC in XYZ 
per 31 december 20X1 en van het aandeel van ABC in het nettoresultaat van XYZ voor het boekjaar. 
Bijgevolg zijn wij niet in staat om een conclusie te trekken over de vraag of een afwijking van materieel 
belang in de andere informatie bestaat.  
 
[Kernpunten van onze controle51 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. In aanvulling tot de aangelegenheid beschreven in de sectie ‘Basis voor ons 
oordeel met beperking’, hebben wij de hierna beschreven aangelegenheden als de in onze verklaring 
te communiceren kernpunten van onze controle vastgesteld. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701]] 
 
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen52 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 53 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
 
 
51  De sectie “Kernpunten van onze controle” is enkel vereist in het geval van beursgenoteerde entiteiten. 
52  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied eisen” niet 
van toepassing is. 
53  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
43/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 7 : Controleverklaring over financiële overzichten van een beursgenoteerde of van 
een niet-beursgenoteerde entiteit, die een afkeurend oordeel omvat, wanneer de auditor alle 
andere informatie heeft verkregen voor de datum van zijn controleverklaring en zijn afkeurend 
oordeel over de geconsolideerde financiële overzichten tevens de andere informatie betreft 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen:  
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een beursgenoteerde entiteit 
waarbij gebruik wordt gemaakt van een getrouw-beeld-stelsel. Het gaar om de controle van een 
groep (i.e., ISA 600 is van toepassing); 
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten zoals 
opgenomen in ISA 210; 
• 
De geconsolideerde financiële overzichten bevatten een afwijking van materieel belang die het 
gevolg is van het niet in de consolidatie opnemen van een dochtervennootschap. De van materieel 
belang zijnde afwijking wordt beschouwd als zijn van diepgaande invloed op de geconsolideerde 
financiële overzichten. De effecten van de afwijking op de geconsolideerde financiële overzichten 
zijn niet bepaald omdat het niet praktisch uitvoerbaar was dit te doen (i.e. een afkeurend oordeel is 
passend); 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit om 
haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring, maar 
heeft een afkeurend oordeel over de geconsolideerde financiële overzichten tot uitdrukking gebracht 
en dit heeft tevens een effect op de andere informatie; 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen. 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wetgeving.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
44/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
 
Afkeurend oordeel 
Wij hebben de geconsolideerde financiële overzichten van vennootschap ABC en haar 
dochtermaatschappijen (de Groep) gecontroleerd, die bestaan uit het geconsolideerd overzicht van 
de financiële positie op 31 december 20X1, het geconsolideerde overzicht van gerealiseerde en niet-
gerealiseerde resultaten, het geconsolideerde mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip 
van een overzicht van de belangrijke grondslagen voor financiële verslaggeving.  
 
Omwille van de significantie van de aangelegenheid besproken in de sectie ‘Basis voor afkeurend 
oordeel’ in onze verklaring, vormen de bijhorende geconsolideerde financiële overzichten, naar ons 
oordeel, geen getrouwe weergave (dan wel geven zij geen getrouw beeld) van de geconsolideerde 
financiële positie van de Groep per 31 december 20X1, en van haar geconsolideerde financiële 
prestaties en kasstromen voor het op die datum afgesloten boekjaar, in overeenstemming met 
International Financial Reporting Standards (IFRS). 
 
Basis voor ons afkeurend oordeel 
Zoals uiteengezet in toelichting X, heeft de vennootschap de financiële overzichten van 
dochtervennootschap XYZ die zij in 20X1 heeft verworven, niet geconsolideerd omdat zij nog niet in 
staat geweest is om de reële waarden van bepaalde materiële activa en verplichtingen van de 
dochtervennootschap op de verwervingsdatum vast te stellen. Deze investering is daarom administratief 
verwerkt op kostenbasis. In toepassing van International Financial Reporting Standards, zou de 
dochtervennootschap moeten worden geconsolideerd en zou de verwerving administratief moeten 
worden verwerkt op basis van voorlopige bedragen. Indien XYZ in de consolidatie was opgenomen, 
zouden vele elementen in de bijgaande financiële overzichten op materiële wijze zijn beïnvloed. De 
effecten van het niet consolideren op de geconsolideerde financiële overzichten zijn niet bepaald.  
 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de geconsolideerde financiële 
overzichten' van onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met 
de ethische vereisten die relevant zijn voor onze controle van de geconsolideerde financiële overzichten 
in [rechtsgebied], en we hebben onze overige ethische verantwoordelijkheden nageleefd in 
overeenstemming met deze vereisten. Wij zijn van mening dat de door ons verkregen controle-
informatie voldoende en geschikt is als basis voor ons afkeurend oordeel. 
 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
Het management is verantwoordelijk voor de andere informatie.54 De andere informatie omvat [de 
informatie vervat in rapport X55, maar omvat niet de geconsolideerde financiële overzichten en onze 
controleverklaring over deze geconsolideerde financiële overzichten].  
 
Ons oordeel over de geconsolideerde financiële overzichten omvat niet de andere informatie en wij 
formuleren geen enkele vorm van assurance-conclusie omtrent deze informatie. 
 
In de context van de onze controle van de geconsolideerde financiële overzichten, zijn wij 
verantwoordelijk voor het lezen van de andere informatie en, tijdens het lezen, voor het overwegen of 
een inconsistentie van materieel belang bestaat tussen de andere informatie en de geconsolideerde 
financiële overzichten of de kennis verkregen in de controle, dan wel of een afwijking van materieel 
belang in de andere informatie bestaat.  
 
 
54  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied 
55  Een meer specifieke beschrijving voor het aanduiden van de andere informatie kan gehanteerd worden, bijvoorbeeld “het 
management rapport of de mededeling van de voorzitter”.

DE VERANTWOORDELIJKHEDEN VAN DE AUDITOR MET BETREKKING TOT ANDERE INFORMATIE 
ISA 720 (herzien) 
NBA-IBR 2022 
45/45 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Indien wij, in het licht van de werkzaamheden die wij hebben uitgevoerd, concluderen dat een afwijking 
van materieel belang in de andere informatie bestaat, dienen wij u dit te communiceren. Zoals 
beschreven in de sectie “Basis voor ons afkeurend oordeel”, zou de dochtervennootschap XYZ moeten 
worden geconsolideerd en zou de verwerving administratief moeten worden verwerkt op basis van 
voorlopige bedragen. Wij hebben hieruit geconcludeerd dat een afwijking van materieel belang in de 
andere informatie bestaat betreffende de bedragen of andere elementen die opgenomen zijn in rapport 
X en die zijn aangetast door het niet opnemen van XYZ  in de consolidatie. 
 
 [Kernpunten van onze controle56 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. In aanvulling tot de aangelegenheid beschreven in de sectie ‘Basis voor ons 
oordeel met beperking’, hebben wij de hierna beschreven aangelegenheden als de in onze verklaring 
te communiceren kernpunten van onze controle vastgesteld. 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701]] 
 
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen57 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 58 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
 
[Adres van de Auditor]  
 
[Datum] 
 
 
56  De sectie “Kernpunten van onze controle” is enkel vereist in het geval van beursgenoteerde entiteiten. 
57  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied. 
58  De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor controles van volledige sets van 
financiële overzichten voor algemene doeleinden van beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van 
een dergelijke toelichting redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. (ISA 700 (herzien), paragraaf 46).