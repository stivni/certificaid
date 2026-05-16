---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 700 (herzien) — Het vormen van een oordeel en het rapporteren over financiële
  overzichten
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-700-(herzien)_nl_2023.pdf
    sha256: c79da260d3cc504f8979cbfe85db06b6532ecb16064a416f8d8e92e6867a4862
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
title: ISA 700 (herzien) — Het vormen van een oordeel en het rapporteren over financiële
  overzichten
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 700 (herzien) — Het vormen van een oordeel en het rapporteren over financiële overzichten

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-700-(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `c79da260d3cc504f8979cbfe85db06b6532ecb16064a416f8d8e92e6867a4862`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard 700 (herzien) 
ISA 700 (herzien)  
 
Het vormen van een oordeel en 
het rapporteren over financiële 
overzichten

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 2/50 
 
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
de Internationale controlestandaard (ISA) 700 (herzien) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 
700 (herzien) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 700 (herzien) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 700 (herzien) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 700 (Revised), Forming an Opinion and Reporting on 
Financial Statements. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, 
and Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 3/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
INTERNATIONALE CONTROLESTANDAARD 700 (HERZIEN) 
HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN  
OVER FINANCIËLE OVERZICHTEN 
(Van toepassing op controles van financiële overzichten over verslagperioden die op of na 15 
december 2016 worden afgesloten)(*) 
 
(*) Deze ISA bevat overeenstemmingswijzigingen die voortvloeien uit de herziene ISA’s 220, 250, 315 
en 540 en de normen ISQM 1 en 2. De inwerkingtreding van deze wijzigingen valt samen met deze 
normen (voor de verslagperiode die op of na 15 december 2016 aanvangen). 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ........................................................................................................ 1-4 
Ingangsdatum ...........................................................................................................................................5 
Doelstellingen  ........................................................................................................................................6 
Definities ............................................................................................................................................. 7-9 
Vereisten  
Het vormen van een oordeel over de financiële overzichten  .......................................................... 10-15 
Vorm van het oordeel  ...................................................................................................................... 16-19 
Controleverklaring  ........................................................................................................................... 20-52 
Aanvullende informatie gepresenteerd bij de financiële overzichten  .............................................. 53-54 
Toepassingsgerichte en overige verklarende teksten 
Kwalitatieve aspecten van de praktijken van de entiteit inzake administratieve dienstverlening .... A1-A3 
Grondslagen voor financiële verslaggeving op passende wijze toegelicht in de financiële  
overzichten  ........................................................................................................................................... A4 
Informatie die gepresenteerd is in de financiële overzichten is relevant, betrouwbaar,  
vergelijkbaar en begrijpelijk ................................................................................................................... A5 
Toelichting van het effect van transacties en gebeurtenissen van materieel belang op de  
informatie op de in financiële overzichten bekendgemaakte informatie ............................................... A6 
Evalueren of de financiële overzichten een getrouwe weergave vormen  ...................................... A7-A9 
Beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving  ................. A10-A15 
Vorm van het oordeel  ................................................................................................................. A16-A17 
Controleverklaring  ...................................................................................................................... A18-A77 
Aanvullende informatie gepresenteerd bij de financiële overzichten  ......................................... A78-A84 
 
Bijlage: Voorbeelden van controleverklaringen van de onafhankelijke auditor over financiële overzichten

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 4/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
International Standard on Auditing (ISA) 700 (herzien), Het vormen van een oordeel en het rapporteren 
over financiële overzichten, moet worden gelezen in samenhang met ISA 200, Algehele doelstellingen 
van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de International 
Standards on Auditing.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 5/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Inleiding 
 
Toepassingsgebied van deze ISA 
 
1. 
Deze International Standards on Auditing (ISA) behandelt de verantwoordelijkheid van de auditor 
voor het vormen van een oordeel over financiële overzichten. Deze ISA behandelt tevens de vorm 
en inhoud van de controleverklaring die wordt uitgebracht als resultaat van een controle van 
financiële overzichten. 
  
2. 
ISA 7011 behandelt de verantwoordelijkheid van de auditor om de kernpunten van de controle in 
de controleverklaring te communiceren. ISA 705 (herzien)2 en ISA 706 (herzien)3 behandelen de 
wijze waarop de vorm en inhoud van de controleverklaring worden beïnvloed indien de auditor 
een aangepast oordeel tot uitdrukking brengt of indien hij een paragraaf ter benadrukking van 
bepaalde aangelegenheden dan wel een paragraaf inzake overige aangelegenheden in de 
controleverklaring opneemt. Ook andere ISA’s bevatten rapporteringsvereisten die van 
toepassing zijn bij het uitbrengen van een controleverklaring. 
 
3. 
Deze ISA is van toepassing op een controle van een volledige set financiële overzichten voor 
algemene doeleinden en is in die context geschreven. ISA 800 (herzien)4 behandelt bijzondere 
overwegingen wanneer de financiële overzichten in overeenstemming met een stelsel voor 
bijzondere doeleinden zijn opgesteld. ISA 805 (herzien)5 behandelt bijzondere overwegingen die 
relevant zijn voor een controle van een enkel financieel overzicht of een controle van een specifiek 
element, een specifieke rekening of een specifieke post van een financieel overzicht. Deze ISA 
is ook van toepassing op controles waarop ISA 800 en of 805 van toepassing zijn. 
 
4. 
De vereisten van deze ISA zijn gericht op vinden van een passende balans tussen de behoefte 
aan consistentie en vergelijkbaarheid wereldwijd van controleverklaringen en de behoefte aan 
het verhogen van de waarde van de controleverklaring door de beschikbaar gestelde informatie 
in de controleverklaring voor gebruikers relevanter te maken. Deze ISA bevordert de consistentie 
in de controleverklaring, maar erkent de behoefte aan flexibiliteit om aan bepaalde 
omstandigheden van individuele rechtsgebieden tegemoet te komen. Consistentie in de 
controleverklaring, wanneer de controle is uitgevoerd overeenkomstig met de ISA’s, bevordert de 
geloofwaardigheid in de wereldwijde markt door die controles die overeenkomstig wereldwijd 
erkende standaarden zijn uitgevoerd, makkelijker herkenbaar te maken. Consistentie in de 
controleverklaring is tevens bevorderlijk voor het begrip van de gebruiker, alsmede voor het 
identificeren van ongebruikelijke omstandigheden wanneer deze zich voordoen. 
 
Ingangsdatum 
 
5. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten. 
 
Doelstellingen 
 
6. 
De doelstellingen van de auditor zijn: 
 
(a) 
Een oordeel te vormen over de financiële overzichten op basis van een evaluatie van de 
conclusies die uit de verkregen controle-informatie zijn getrokken; en 
 
1  
ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijke auditor. 
2  
ISA 705 (herzien), Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor. 
3  
ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor. 
4  
ISA 800, Bijzondere overwegingen - Controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels 
voor bijzondere doeleinden. 
5  
ISA 805, Bijzondere overwegingen - Controles van een enkel financieel overzicht en controles van specifieke elementen, 
rekeningen of posten van een financieel overzicht.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 6/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
(b) 
Dat oordeel op duidelijke wijze tot uitdrukking te brengen door middel van een schriftelijke 
verklaring. 
 
Definities 
 
7. 
Voor de toepassing van de ISA’s hebben de volgende termen de hierna weergegeven betekenis: 
 
(a) 
Financiële overzichten voor algemene doeleinden – Financiële overzichten die zijn 
opgesteld in overeenstemming met een stelsel voor algemene doeleinden. 
(b) 
Stelsel voor algemene doeleinden – Een stelsel inzake financiële verslaggeving dat is 
opgezet om te voorzien in de gemeenschappelijke informatiebehoefte van een breed scala 
aan gebruikers. Het stelsel inzake financiële verslaggeving kan een getrouw-beeld-stelsel 
zijn, dan wel een compliance-stelsel. 
 
De term ‘getrouw-beeld-stelsel’ wordt gebruikt om te verwijzen naar een stelsel inzake 
financiële verslaggeving dat de naleving van de door het stelsel gestelde vereisten 
voorschrijft, en dat: 
 
(i) 
Expliciet of impliciet erkent dat, opdat de financiële overzichten een getrouwe 
weergave vormen, het nodig kan zijn dat het management toelichtingen verstrekt die 
verder gaan dan de toelichtingen die specifiek door het stelsel vereist zijn; of 
(ii) 
Expliciet erkent dat het noodzakelijk kan zijn dat het management van een door het 
stelsel gesteld vereiste afwijkt opdat de financiële overzichten een getrouwe 
weergave vormen. Dergelijke afwijkingen worden uitsluitend in buitengewoon 
zeldzame omstandigheden noodzakelijke geacht. 
 
De term ‘compliance-stelsel’ wordt gebruikt om te verwijzen naar een stelsel inzake 
financiële verslaggeving dat de naleving van de door het stelsel gestelde vereisten 
voorschrijft, maar de hierboven onder (i) of (ii) genoemde erkenningen niet bevat.6 
  
(c) 
Goedkeurend oordeel – Het door de auditor tot uitdrukking gebrachte oordeel indien de 
auditor tot de conclusie komt dat de financiële overzichten in alle van materieel belang 
zijnde opzichten zijn opgesteld in overeenstemming met het van toepassing zijnde stelsel 
inzake financiële verslaggeving.7 
 
8. 
In deze ISA wordt met ‘financiële overzichten’ een volledige set financiële overzichten voor 
algemene doeleinden.8 De door het van toepassing zijnde stelsel inzake financiële verslaggeving 
gestelde vereisten bepalen de presentatie, structuur en inhoud van de financiële overzichten, 
alsmede waaruit een volledige set financiële overzichten bestaat. 
 
9. 
In deze ISA wordt met ‘International Financial Reporting Standards’ de International Financial 
Reporting Standards (IFRS) uitgebracht door de International Accounting Standards Board 
bedoeld, en wordt met ‘International Public Sector Accounting Standards’ (IPSAS) de 
International Public Sector Accounting Standards uitgebracht door de International Public Sector 
Accounting Standards Board (IPSASB) bedoeld. 
 
Vereisten 
 
Het vormen van een oordeel over de financiële overzichten 
 
 
6  
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de 
International Standards on Auditing, paragraaf 13(a). 
7  
De paragrafen 25-26 behandelen de gebruikte formuleringen om dit oordeel tot uitdrukking te brengen in het geval van 
respectievelijk een getrouw-beeld-stelsel en een compliance-stelsel. 
8  
ISA 200, paragraaf 13(f), zet de inhoud van de financiële overzichten uiteen.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 7/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
10. 
De auditor dient een oordeel te vormen over de vraag of de financiële overzichten in alle van 
materieel belang zijnde opzichten zijn opgesteld in overeenstemming met het van toepassing 
zijnde stelsel inzake financiële verslaggeving.9,10 
 
11. 
Teneinde dit oordeel te vormen, dient de auditor te concluderen of hij een redelijke mate van 
zekerheid heeft verkregen over de vraag of de financiële overzichten als geheel geen afwijkingen 
van materieel belang bevatten die het gevolg zijn van fraude of van fouten. Deze conclusie dient 
rekening te houden met: 
 
(a) 
De conclusie van de auditor, overeenkomstig ISA 330, of voldoende en geschikte controle-
informatie is verkregen;11  
(b) 
De conclusie van de auditor, overeenkomstig ISA 450, of de niet-gecorrigeerde afwijkingen 
afzonderlijk of gezamenlijk van materieel belang zijn;12 en 
(c) 
De evaluaties die op grond van de paragrafen 12-15 zijn vereist. 
 
12. 
De auditor dient te evalueren of de financiële overzichten in alle van materieel belang zijnde 
opzichten zijn opgesteld in overeenstemming met de vereisten gesteld door het van toepassing 
zijnde stelsel inzake financiële verslaggeving. Deze evaluatie dient onder meer in te houden dat 
de kwalitatieve aspecten van de praktijken van de entiteit inzake administratieve verwerking 
worden overwogen, met inbegrip van indicaties van een mogelijke tendentie in de 
oordeelsvormingen van het management. (Zie par. A1-A3) 
 
13. 
In het bijzonder dient de auditor te evalueren of, in het licht van de vereisten gesteld door het van 
toepassing zijnde stelsel inzake financiële verslaggeving: 
 
(a) 
De financiële overzichten op passende wijze informatie verschaffen over de belangrijke 
geselecteerde en toegepaste grondslagen voor financiële verslaggeving. Bij het maken van 
deze evaluatie dient de accountant de relevantie van de grondslagen voor financiële 
verslaggeving van de entiteit in aanmerking te nemen, en of ze zijn gepresenteerd op een 
begrijpelijke manier; (Zie par. A4) 
(b) 
De geselecteerde en toegepaste grondslagen voor financiële verslaggeving consistent zijn 
met het van toepassing zijnde stelsel inzake financiële verslaggeving, en passend zijn; 
(c) 
De door het management gemaakte schattingen en toelichtingen daarop redelijk zijn; 
(d) 
De in de financiële overzichten gepresenteerde informatie relevant, betrouwbaar, 
vergelijkbaar en begrijpelijk is. Bij het maken van deze evaluatie zal de accountant 
overwegen of: 
 
• 
De informatie die had moeten worden opgenomen is opgenomen en of deze 
informatie op de juiste wijze is geclassificeerd, samengevoegd of uitgesplitst, en 
gekenmerkt; 
• 
De algehele presentatie van de financiële overzichten is ondermijnd door het 
opnemen van informatie die niet relevant is of die een goed begrip van de toegelichte 
aangelegenheden verhult. (Zie par. A5) 
 
(e) De financiële overzichten adequate toelichtingen verschaffen om de beoogde gebruikers in 
staat te stellen het effect van transacties en gebeurtenissen van materieel belang op de in 
de financiële overzichten bekendgemaakte informatie te begrijpen; en (Zie par. A6) 
(f) 
De in de financiële overzichten gebruikte terminologie, met inbegrip van de titel van elk 
financieel overzicht, passend is. 
 
14. 
Indien de financiële overzichten zijn opgesteld in overeenstemming met een getrouw-beeld-
stelsel, zal de evaluatie die op grond van de paragrafen 1 2 -13 is vereist, mede de vraag 
 
9  
ISA 200, paragraaf 11. 
10  De paragrafen 25-26 behandelen de gebruikte formuleringen om dit oordeel tot uitdrukking te brengen in het geval van 
respectievelijk een getrouw-beeld-stelsel en een compliance-stelsel. 
11  ISA 330, Inspelen door de auditor op ingeschatte risico's, paragraaf 26. 
12  ISA 450, Evaluatie van tijdens de controle geïdentificeerde afwijkingen, paragraaf 11.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 8/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
omvatten of de financiële overzichten een getrouwe weergave vormen. De evaluatie door de 
accountant van de vraag of de financiële overzichten een getrouwe weergave vormen dient in te 
houden dat het volgende wordt overwogen (Zie par. A7-A9): 
 
(a) 
De algehele presentatie, structuur en inhoud van de financiële overzichten; en 
(b) 
De vraag of de financiële overzichten de onderliggende transacties en gebeurtenissen 
weergeven op een wijze die een getrouwe weergave vormt. 
 
15. 
De auditort dient te evalueren of de financiële overzichten op adequate wijze verwijzen naar het 
van toepassing zijnde stelsel inzake financiële verslaggeving, dan wel op adequate wijze hiervan 
een beschrijving geven. (Zie par. A10-A15) 
 
Vorm van het oordeel 
  
16. 
De auditor dient een goedkeurend oordeel tot uitdrukking te brengen in het geval hij tot de 
conclusie komt dat de financiële overzichten in alle van materieel belang zijnde opzichten zijn 
opgesteld in overeenstemming met het van toepassing zijnde stelsel inzake financiële 
verslaggeving. 
  
17. 
Indien de auditor: 
 
(a) 
Tot de conclusie komt dat, op basis van de verkregen controle-informatie, de financiële 
overzichten als geheel niet vrij zijn van een afwijking van materieel belang; of 
(b) 
Niet in staat is voldoende en geschikte controle-informatie te verkrijgen om te concluderen 
dat de financiële overzichten als geheel vrij zijn van een afwijking van materieel belang, 
dient hij het oordeel in de controleverklaring aan te passen overeenkomstig ISA 705 
(herzien). 
 
18. 
Indien de financiële overzichten, opgesteld in overeenstemming met de vereisten gesteld door 
een getrouw-beeld-stelsel, geen getrouwe weergave vormen, dient de auditor deze 
aangelegenheid met het management te bespreken en, afhankelijk van de vereisten gesteld door 
het van toepassing zijnde stelsel inzake financiële verslaggeving alsmede van de wijze waarop 
deze aangelegenheid wordt opgelost, dient hij te bepalen of het noodzakelijk is het oordeel in de 
controleverklaring aan te passen overeenkomstig ISA 705 (herzien). (Zie par. A16) 
 
19. 
Als de financiële overzichten zijn opgesteld in overeenstemming met een compliance-stelsel, 
wordt niet van de auditor vereist om te evalueren of de financiële overzichten een getrouwe 
weergave vormen. Indien de auditor evenwel, in uiterst zeldzame omstandigheden, tot de 
conclusie komt dat dergelijke financiële overzichten misleidend zijn, dient hij deze 
aangelegenheid met het management te bespreken, en afhankelijk van de wijze waarop deze 
aangelegenheid wordt opgelost, dient hij te bepalen of, en op welke wijze, hij hierover 
communiceert in de controleverklaring. (Zie par. A17) 
 
Controleverklaring 
 
20. 
De controleverklaring dient op schrift te worden gesteld. (Zie par. A18-A19) 
 
Controleverklaring voor controles uitgevoerd overeenkomstig de International Standards on Auditing 
 
Titel 
 
21. 
De controleverklaring dient een titel te hebben die duidelijk aangeeft dat het een verklaring van 
een onafhankelijke auditor betreft. (Zie par. A20) 
 
Geadresseerde

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 9/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
22. 
De controleverklaring dient te worden geadresseerd, naar gelang passend, op basis van, de 
omstandigheden van de opdracht. (Zie par. A21) 
 
Oordeel van de auditor 
  
23. 
De eerste sectie van de controleverklaring dient het oordeel van de auditor te bevatten en dient 
de titel “Oordeel” te dragen. 
 
24. 
De sectie “Oordeel” in de controleverklaring dient tevens:  
 
(a) 
De entiteit te identificeren waarvan de financiële overzichten zijn gecontroleerd; 
(b) 
Te vermelden dat de financiële overzichten zijn gecontroleerd; 
(c) 
De titel van elk in de financiële overzichten opgenomen overzicht te vermelden; 
(d) 
Te verwijzen naar de toelichtingen bij de financiële overzichten, inclusief het overzicht van 
belangrijke gehanteerde grondslagen voor financiële verslaggeving; en 
(e) 
De datum of periode te specificeren waarop elk financieel overzicht dat tot de financiële 
overzichten behoort, betrekking heeft. (Zie par. A22-A23) 
  
25. 
Indien een goedkeurend oordeel tot uitdrukking wordt gebracht over financiële overzichten die in 
overeenstemming met een getrouw-beeld-stelsel zijn opgesteld, dient het oordeel van de auditor, 
tenzij anderszins door de wet- of regelgeving vereist, een van de volgende formuleringen te 
gebruiken, die beschouwd worden als zijnde equivalent: 
 
(a) 
Naar ons oordeel vormen de bijgevoegde financiële overzichten in alle van materieel 
belang zijnde opzichten een getrouwe weergave, […] in overeenstemming met [het van 
toepassing zijnde stelsel inzake financiële verslaggeving]; of  
(b) 
Naar ons oordeel geven de bijgevoegde financiële overzichten een getrouw beeld van […] 
in overeenstemming met [het van toepassing zijnde stelsel inzake financiële 
verslaggeving]. (Zie par. A24-A31) 
 
26. 
Bij het tot uitdrukking brengen van een goedkeurend oordeel over financiële overzichten die in 
overeenstemming met een compliance-stelsel zijn opgesteld, dient het oordeel van de auditor te 
vermelden dat de bijgevoegde financiële overzichten in alle van materieel belang zijnde opzichten 
zijn opgesteld in overeenstemming met [het van toepassing zijnde stelsel inzake financiële 
verslaggeving]. (Zie par. A26-A31) 
 
27. 
Indien de in de controleverklaring opgenomen verwijzing naar het van toepassing zijnde stelsel 
inzake financiële verslaggeving geen referentie is aan de IFRS die door de International 
Accounting Standards Board (IASB) zijn uitgebracht, noch aan de International Public Sector 
Accounting Standards IPSAS die door de International Public Sector Accounting Standards Board 
zijn uitgebracht, noch aan Titel 9 Boek 2 BW dient het oordeel van de auditor het rechtsgebied 
van oorsprong van het stelsel te vermelden. 
 
Basis voor het oordeel  
 
28. 
De controleverklaring dient een sectie te bevatten, die direct de sectie “Oordeel” opvolgt, met de 
titel “Basis voor ons oordeel”, die: (Zie par. A32) 
 
(a) 
Vermeldt dat de controle overeenkomstig de International Standards on Auditing is 
uitgevoerd; (Zie par. A33) 
(b) 
Verwijst naar de sectie van de controleverklaring die de verantwoordelijkheden van de 
auditor onder de ISA’s beschrijft; 
(c) 
Een vermelding bevat dat de auditor onafhankelijk is van de entiteit in overeenstemming 
met de ethische voorschriften die relevant zijn voor de controle van de financiële 
overzichten en de overige ethische verantwoordelijkheden nageleefd in overeenstemming 
met deze vereisten heeft nageleefd. Deze vermelding zal het oorspronkelijk rechtsgebied 
van deze relevante ethische voorschriften aangeven of verwijzen naar de Code of Ethics

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 10/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
for Professional Accountants van de International Ethics Standards Board for Accountants 
(IFAC Code); en (Zie par. A34-A39) 
(d) 
Vermeldt of de auditor van mening is dat de controle-informatie die de auditor heeft 
verkregen voldoende en geschikt is om een basis te verschaffen voor het oordeel van de 
auditor. 
 
Continuïteit 
 
29. 
Waar van toepassing dient de auditor te rapporten overeenkomstig ISA 570 (herzien).13 
 
Kernpunten van de controle 
 
30. 
Voor controles van volledige sets financiële overzichten voor algemene doeleinden van 
beursgenoteerde entiteiten dient de auditor kernpunten van de controle overeenkomstig ISA 701 
in de controleverklaring te communiceren. 
 
31. 
Wanneer van de auditor anderszins op grond van wet- of regelgeving is vereist om kernpunten 
van de controle in de controleverklaring te communiceren, of wanneer hij hiertoe besluit, dient hij 
dit overeenkomstig ISA 701 te doen. (Zie par. A40-A42) 
 
Andere informatie 
 
32. 
Waar van toepassing, zal de auditor rapporteren in overeenstemming met ISA 720 (herzien).14 
 
Verantwoordelijkheden voor de financiële overzichten. 
 
33. 
De controleverklaring dient een sectie te bevatten met de titel “Verantwoordelijkheden van het 
management voor de financiële overzichten”. De controleverklaring dient de term te gebruiken die 
gepast is in de context van het wettelijke kader in het desbetreffende rechtsgebied en hoeft niet 
specifiek te verwijzen naar “het management”. In sommige rechtsgebieden kan de gepaste 
verwijzing naar de met governance belaste personen zijn. (Zie par. A44) 
 
34. 
Deze sectie van de controleverklaring dient de verantwoordelijkheid van het management te 
beschrijven voor: (Zie par. A45-A48) 
 
(a) 
Het opstellen van de financiële overzichten in overeenstemming met het van toepassing 
zijnde stelsel inzake financiële verslaggeving en voor dergelijke interne beheersing 
waarvan het management bepaalt dat deze noodzakelijk is voor het opstellen van de 
financiële overzichten die vrij zijn van afwijkingen van materieel belang als gevolg van 
fraude of fouten; en 
(b) 
Het inschatten van de mogelijkheid van de entiteit om haar continuïteit te handhaven15 en 
de vraag of het hanteren van de continuïteitsveronderstelling gepast is en dat deze, indien 
van toepassing, aangelegenheden met betrekking tot continuïteit toelicht. De uitleg van de 
verantwoordelijkheid van het management voor deze inschatting dient een beschrijving te 
omvatten van wanneer het gebruik van de continuïteitsveronderstelling gepast is. (Zie par. 
A48) 
 
35. 
Deze sectie van de controleverklaring dient tevens degenen die verantwoordelijk zijn voor het 
toezicht op het proces van financiële verslaggeving te identificeren, wanneer degenen die 
verantwoordelijk zijn voor dit toezicht anderen zijn dan degenen die deze verantwoordelijkheden 
vervullen zoals in paragraaf 33 hierboven is beschreven. In dit geval dient de titel van deze sectie 
tevens te verwijzen naar “De met governance belaste personen” of een dergelijke term die binnen 
het wettelijke kader in het desbetreffende rechtsgebied gepast is.(Zie par. A49) 
 
 
13  ISA 570 (herzien), Continuïteit, par. 21-23 
14  ISA 720 (herzien), De verantwoordelijkheden van de auditor met betrekking tot andere informatie. 
15  ISA 570 (herzien), paragraaf 2

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 11/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
36. 
Wanneer de financiële overzichten in overeenstemming met een getrouw-beeld-stelsel zijn 
opgesteld dient de beschrijving van de verantwoordelijkheden voor de financiële overzichten in 
de controleverklaring te verwijzen naar “het opstellen en getrouw weergeven van deze financiële 
overzichten” of “het opstellen van de financiële overzichten die een getrouw beeld geven”, naar 
gelang wat in de omstandigheden gepast is. 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten. 
  
37. 
De controleverklaring dient een sectie te bevatten met de titel “Verantwoordelijkheden van de 
auditor voor de controle van de financiële overzichten.” 
 
38. 
Deze sectie van de controleverklaring dient: (Zie par. A50) 
  
(a) 
Te vermelden dat de doelstellingen van de auditor zijn om: 
(i) 
Een redelijke mate van zekerheid te verkrijgen over de vraag of de financiële 
overzichten als geheel geen afwijking van materieel belang bevatten als gevolg van 
fraude of van fouten; en 
(ii) 
Een controleverklaring uit te brengen waarin het oordeel van de auditor is 
opgenomen. (Zie par. A51) 
 
(b) 
Te vermelden dat een redelijke mate van zekerheid een hoog niveau van zekerheid is, 
maar geen garantie dat een controle die overeenkomstig de ISA en is uitgevoerd altijd een 
afwijking van materieel belang ontdekt wanneer hier sprake van is; en  
(c) 
Te vermelden dat afwijkingen zich kunnen voordoen als gevolg van fraude of van fouten 
en: 
 
(i) 
Beschrijven dat zij als van materieel belang worden beschouwd indien hiervan, 
individueel of afzonderlijk, redelijkerwijs kan worden verwacht dat zij de 
economische beslissingen, die gebruikers op basis van deze financiële overzichten 
nemen, beïnvloeden16; of 
(ii) 
Een definitie of beschrijving van materialiteit verschaffen in overeenstemming met 
het van toepassing zijnde stelsel inzake financiële verslaggeving.(Zie par. A53) 
 
39. 
De sectie “Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten” 
in de controleverklaring dient verder: (Zie. Par. A50) 
 
(a) 
Te vermelden dat, als onderdeel van een controle overeenkomstig de ISA’s, de auditor 
gedurende de controle professionele oordeelsvorming toepast en een professioneel-
kritische houding handhaaft; en  
(b) 
Een controle te beschrijven door te vermelden dat de verantwoordelijkheden van de auditor 
bestaan uit: 
 
(i) 
Het identificeren en inschatten van de risico’s op een afwijking van materieel belang 
in de financiële overzichten als gevolg van fraude of van fouten; het opzetten en 
uitvoeren van controlewerkzaamheden die op die risico’s inspelen; en het verkrijgen 
van controle-informatie die voldoende en geschikt is om een basis voor het oordeel 
van de auditor te verschaffen. Het risico van het niet-ontdekken van een afwijking 
van materieel belang die het gevolg is van fraude is hoger dan een die het gevolg is 
van fouten, aangezien fraude gepaard kan gaan met samenspanning, valsheid in 
geschrifte, opzettelijke weglatingen, een verkeerde voorstelling van zaken of het 
doorbreken van de interne beheersing; 
(ii) 
Het verwerven van inzicht in de interne beheersing die voor de controle relevant is 
om controlewerkzaamheden op te zetten die in de omstandigheden gepast zijn, 
maar die niet bedoeld zijn om een oordeel tot uitdrukking te brengen over de 
effectiviteit van de interne beheersing van de entiteit. In omstandigheden waarin de 
auditor tevens de verantwoordelijkheid heeft om een oordeel tot uitdrukking te 
 
16  ISA 320, Materialiteit bij planning en uitvoering van een controle, paragraaf 2.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 12/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
brengen over de effectiviteit van de interne beheersing in samenhang met de 
controle van de financiële overzichten, dient de auditor de formulering weg te laten 
dat het door de auditor overwegen van de interne beheersing niet bedoeld is om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing; 
(iii) 
Het evalueren van de geschiktheid van de grondslagen van de financiële 
verslaggeving die worden gebruikt en de redelijkheid van schattingen en daarmee 
verband houdende toelichtingen die door het management worden gemaakt; 
(iv) 
Het 
concluderen 
over 
de 
geschiktheid 
van 
het 
hanteren 
van 
de 
continuïteitsveronderstelling door het management en, gebaseerd op de verkregen 
controle-informatie, de vraag of er een onzekerheid van materieel belang bestaat 
met betrekking tot gebeurtenissen of omstandigheden die gerede twijfel kunnen 
doen ontstaan over de mogelijkheid van de entiteit om haar continuïteit te 
handhaven. Indien de auditor concludeert dat er sprake is van een onzekerheid van 
materieel belang, is van de auditor vereist om in de controleverklaring de aandacht 
te vestigen op de daarmee verband houdende toelichtingen in de financiële 
overzichten of, indien dergelijke toelichtingen inadequaat zijn, het oordeel daarover 
aan te passen. De conclusies van de auditor zijn gebaseerd op de controle-
informatie die verkregen is tot op de datum van de controleverklaring. Toekomstige 
gebeurtenissen of omstandigheden kunnen er echter voor zorgen dat de entiteit niet 
langer in staat is haar continuïteit te handhaven; 
(v) 
Wanneer de financiële overzichten in overeenstemming met een getrouw-beeld-
stelsel zijn opgesteld, het evalueren van de algehele weergave, structuur en inhoud 
van de financiële overzichten, inclusief de toelichtingen en de vraag of de financiële 
overzichten de onderliggende transacties en gebeurtenissen weergeven op een 
manier die een getrouwe weergave vormt; 
 
(c) 
Als ISA 60017 van toepassing is, het verder beschrijven van de verantwoordelijkheden van 
de auditor in een controleopdracht op groepsniveau door te vermelden dat: 
  
(i) 
De verantwoordelijkheden van de auditor bestaan uit het verkrijgen van voldoende 
geschikte controle-informatie met betrekking tot de financiële informatie van de 
entiteiten of bedrijfsactiviteiten binnen de groep om een oordeel tot uitdrukking te 
brengen over de financiële overzichten van een groep; 
(ii) 
De auditor verantwoordelijk is voor de aansturing van, het toezicht op en de 
uitvoering van de groepscontrole; en  
(iii) 
De auditor ongedeeld verantwoordelijk blijft voor zijn oordeel. 
 
40. 
De sectie “Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten” 
dient tevens: (Zie par. A50) 
 
(a) 
Te vermelden dat de auditor aan de met governance belaste personen aangelegenheden 
communiceert zoals de geplande reikwijdte en timing van de controle en significante 
controlebevindingen, inclusief significante tekortkomingen in de interne beheersing die de 
auditor tijdens de controle identificeert; 
(b) 
Voor controles van financiële overzichten van beursgenoteerde entiteiten te vermelden dat 
de auditor aan [de met governance belaste personen]heeft gemeld dat alle relevante 
ethische voorschriften zijn nageleefd met betrekking tot onafhankelijkheid en dat hij aan 
hen alle relaties en overige aangelegenheden heeft gecommuniceerd waarvan 
redelijkerwijs kan worden verwacht dat deze consequenties kunnen hebben voor de 
onafhankelijkheid van de auditor, en waar van toepassing, daarmee verband houdende 
maatregelen; en  
(c) 
Voor controles van financiële overzichten van beursgenoteerde entiteiten en andere 
entiteiten waarvoor kernpunten van de controle overeenkomstig ISA 701 worden 
gecommuniceerd, te vermelden dat, van de aangelegenheden die gecommuniceerd zijn 
met [de met governance belaste personen], de auditor die aangelegenheden bepaalt die 
 
17  ISA 600, Bijzondere overwegingen – Controles van financiële overzichten van de groep (Inclusief de werkzaamheden van 
auditor van groepsonderdelen).

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 13/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
het meest significant waren bij de controle van de financiële overzichten van de huidige 
periode en derhalve kernpunten van de controle zijn. De auditor beschrijft deze 
aangelegenheden in de controleverklaring tenzij wet- of regelgeving openbaarmaking van 
de aangelegenheid verhindert of wanneer, in uiterst zeldzame omstandigheden, de auditor 
bepaalt dat een aangelegenheid niet in de controleverklaring zou moeten worden 
gecommuniceerd omdat redelijkerwijs verwacht wordt dat de nadelige gevolgen van 
dergelijke communicatie groter zijn dan de voordelen voor het maatschappelijk verkeer. 
(Zie par. A53) 
 
Plaats van de beschrijving van de verantwoordelijkheden van de auditor voor de controle van de 
financiële overzichten 
 
41. 
De beschrijving van de verantwoordelijkheden van de auditor voor de controle van de financiële 
overzichten zoals vereist op grond van paragrafen 39-40, dient te worden opgenomen: (Zie par. 
A54) 
 
(a) 
In de tekst van de controleverklaring; 
(b) 
In een bijlage bij de controleverklaring, in welk geval de controleverklaring een verwijzing 
dient te bevatten naar de plaats van de bijlage; of (Zie par. A54-A57) 
(c) 
Door een specifieke verwijzing in de controleverklaring naar de plaats van een dergelijke 
beschrijving op een website van een bevoegde instantie, waar wet- en regelgeving of 
nationale controlestandaarden de auditor uitdrukkelijk toestaan dit te doen. (Zie par. A54, 
A56-A57) 
 
42. 
Wanneer de auditor verwijst naar een beschrijving van de verantwoordelijkheden van de auditor 
op een website van een bevoegde instantie dient de auditor te bepalen of een dergelijke 
beschrijving de vereisten in paragrafen 39-40 behandelt en hiermee niet strijdig is. (Zie par. A56) 
 
Andere rapporteringsverplichtingen 
  
43. 
Indien de auditor in de controleverklaring over de financiële overzichten andere 
rapporteringsverplichtingen behandelt naast zijn verantwoordelijkheid overeenkomstig de ISA’s, 
dienen deze overige rapporteringsverplichtingen te worden behandeld in een aparte sectie in de 
controleverklaring met als titel Verklaring betreffende overige door wet- of regelgeving gestelde 
vereisten, of anderszins naargelang passend ten aanzien van de inhoud van de sectie, tenzij 
deze andere rapporteringsverplichtingen dezelfde onderwerpen behandelen als degenen die zijn 
gepresenteerd onder de rapporteringsverplichtingen die op grond van de ISA’s zijn vereist, in 
welk geval de andere rapporteringsverplichtingen in dezelfde sectie kunnen worden 
gepresenteerd als de daarmee verband houdende rapporteringselementen die op grond van de 
ISA’s zijn vereist. (Zie par. A58-A60) 
 
44. 
Indien andere rapporteringsverplichtingen in dezelfde sectie worden gepresenteerd als de 
daarmee verband houdende rapporteringselementen die op grond van de ISA’s zijn vereist, dient 
de controleverklaring duidelijk de andere rapporteringsverplichtingen te onderscheiden van de 
rapportering die op grond van de ISA’s is vereist.(Zie par. A60) 
 
45. 
Indien 
de 
controleverklaring 
een 
aparte 
sectie 
bevat 
die 
overige 
rapporteringsverantwoordelijkheden behandelt, dienen de vereisten uit paragrafen 21-40 te 
worden opgenomen in een sectie met de titel “Verklaring betreffende de controle van de financiële 
overzichten”. De “Verklaring betreffende overige door wet- of regelgeving gestelde vereisten” 
dient te volgen op de “Verklaring betreffende de controle van de financiële overzichten”. (Zie par. 
A60) 
 
Naam van de opdrachtpartner  
 
46. 
De naam van de opdrachtpartner dient in de controleverklaring te worden opgenomen voor 
controles van volledige sets van financiële overzichten voor algemene doeleinden van

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 14/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
beursgenoteerde entiteiten, tenzij in zeldzame omstandigheden, van een dergelijke toelichting 
redelijkerwijs verwacht wordt dat deze leidt tot een significante bedreiging voor de persoonlijke 
veiligheid. In de zeldzame omstandigheden dat de auditor van plan is om de naam van de 
opdrachtpartner niet op te nemen in de controleverklaring, dient de auditor deze intentie met de 
met governance belaste personen te bespreken om de inschatting door de auditor van de 
waarschijnlijkheid en ernst van een significante bedreiging voor de persoonlijke veiligheid te 
onderbouwen. (Zie par. A61-A63) 
 
Handtekening van de auditor 
  
47. 
De controleverklaring dient te worden ondertekend. (Zie par. A64-A65) 
 
Adres van de auditor 
 
48. 
De controleverklaring dient de naam te vermelden van de locatie in het rechtsgebied waar de 
auditor kantoor houdt. 
 
 
Datum van de controleverklaring 
 
49. 
De controleverklaring dient niet vroeger te worden gedateerd dan de datum waarop de auditor 
voldoende en geschikte controle-informatie heeft verkregen waarop hij zijn oordeel over de 
financiële overzichten baseert, met inbegrip van informatie die aantoont dat: (Zie par. A66-A69) 
 
(a) 
Alle overzichten en toelichtingen die de financiële overzichten vormen zijn opgesteld; en 
(b) 
De personen met de erkende bevoegdheid hebben beweerd dat zij verantwoordelijkheid 
hebben genomen voor die financiële overzichten. 
 
Controleverklaring voorgeschreven door wet- of regelgeving 
 
50. 
Indien op grond van de wet- of regelgeving van een specifiek rechtsgebied van de auditor wordt 
vereist dat hij zich houdt aan een specifieke opmaak of formulering in de controleverklaring, mag 
de controleverklaring slechts naar de International Standards on Auditing verwijzen als ze ten 
minste elk van de volgende elementen bevat (Zie par. A70-A71) 
 
(a) 
Een titel ; 
(b) 
Een geadresseerde, zoals door de omstandigheden van de opdracht vereist; 
(c) 
Een oordeelsectie waarin een oordeel over de financiële overzichten tot uitdrukking wordt 
gebracht en een verwijzing naar het van toepassing zijnde stelsel inzake financiële 
verslaggeving dat bij het opstellen van de financiële overzichten is gebruikt (met inbegrip 
van de vermelding van het rechtsgebied van oorsprong van het stelsel inzake financiële 
verslaggeving dat noch de International Financial Reporting Standards, noch de 
International Public Sector Accounting Standards is, Zie par. 27); 
(d) 
Een identificatie van de financiële overzichten van de entiteit die gecontroleerd zijn; 
(e) 
Een vermelding dat de auditor onafhankelijk is van de entiteit in overeenstemming met de 
voor de controle relevante ethische voorschriften en dat de auditor heeft voldaan aan de 
andere ethische voorschriften in overeenstemming met deze voorschriften. De vermelding 
zal het oorspronkelijk rechtsgebied van deze relevante ethische voorschriften aangeven of 
verwijzen naar de IFAC Code; 
(f) 
Waar van toepassing, een sectie die de rapportagevereisten in paragraaf 22 van ISA 570 
(herzien) behandelt en hiermee niet in strijd is; 
(g) 
Waar van toepassing, een sectie Onderbouwing van ons oordeel met beperking (of 
afkeurend oordeel) die de rapporteringsvereisten in paragraaf 23 van ISA 570 behandelt 
en hiermee niet in strijd is; 
(h) 
Waar van toepassing, een sectie die de informatie bevat die op grond van ISA 701 is 
vereist, of aanvullende informatie over de controle die op grond van wet- of regelgeving is

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 15/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
voorgeschreven en de rapporteringsvereisten in die ISA behandelt en hiermee niet in strijd 
is;18 (Zie par. A72-A75) 
(i) 
Waar van toepassing, een sectie, die de rapportagevereisten in paragraaf 24 van ISA 720 
(herzien) behandelt; 
(j) 
Een beschrijving van de verantwoordelijkheden van het management voor het opstellen 
van de financiële overzichten en een identificatie van degenen die verantwoordelijk zijn 
voor het toezicht op het proces van financiële verslaggeving die de vereisten in paragrafen 
33-36 behandelt en hiermee niet strijdig is; 
(k) 
Een verwijzing naar de ISA’s en de wet- of regelgeving alsmede een verwijzing naar de 
verantwoordelijkheden van de auditor voor een controle van de financiële overzichten die 
de vereisten in paragrafen 36-39 behandelt en hiermee niet strijdig is; (Zie par. A50-A53) 
(l) 
Voor controles van volledige sets financiële overzichten voor algemene doeleinden van 
beursgenoteerde entiteiten, de naam van de opdrachtpartner, tenzij, in zeldzame 
omstandigheden, van een dergelijke toelichting redelijkerwijs kan worden verwacht dat 
deze tot een significante bedreiging voor de persoonlijke veiligheid leidt ; 
(m) 
De handtekening van de auditor; 
(n) 
Het adres van de auditor; en 
(o) 
De datum van de controleverklaring. 
  
Controleverklaring voor controles uitgevoerd overeenkomstig zowel controlestandaarden van een 
specifiek rechtsgebied als de International Standards on Auditing 
 
51. 
Van een auditor kan vereist worden een controle uit te voeren overeenkomstig andere 
controlestandaarden van een specifiek rechtsgebied (de “nationale controlestandaarden”) en hij 
heeft bovendien de International Standards on Auditing nageleefd bij de uitvoering van de 
controle. Indien dit het geval is, mag de auditor in zijn controleverklaring verwijzen naar 
International Standards on Auditing in aanvulling op de andere controlestandaarden, maar de 
auditor dient dit alleen te doen als: (Zie par. A76-A77) 
 
(a) 
er geen conflict is tussen de vereisten van de andere controlestandaarden en die van de 
International Standards on Auditing dat ertoe zou leiden dat de auditor (i) een ander oordeel 
vormt, of (ii) geen paragraaf ter benadrukking van bepaalde aangelegenheden of een 
paragraaf inzake overige aangelegenheden opneemt die in de bijzondere omstandigheden 
op grond van de International Standards on Auditing vereist is; en 
(b) 
de controleverklaring ten minste elk van de in paragraaf 50(a)–(0) uiteengezette elementen 
bevat indien de auditor gebruikmaakt van de door de andere controlestandaarden 
gespecificeerde opmaak of formulering. Verwijzingen wet- of regelgeving in paragraaf 50(k) 
dienen echter te worden gelezen als verwijzingen naar de andere controlestandaarden. De 
controleverklaring dient daarbij deze andere controlestandaarden te vermelden. 
 
52. 
In het geval de controleverklaring verwijst naar zowel de andere controlestandaarden als de 
International Standards on Auditing, dient de controleverklaring het rechtsgebied van oorsprong 
van de nationale controlestandaarden te vermelden. 
 
Aanvullende informatie gepresenteerd bij de financiële overzichten (Zie par. A78-A84) 
 
53. 
Indien aanvullende informatie die niet wordt vereist door het van toepassing zijnde stelsel inzake 
financiële verslaggeving wordt gepresenteerd met de gecontroleerde financiële overzichten, dient 
de auditor te evalueren of, naar de professionele oordeelsvorming van de auditor, aanvullende 
informatie niettemin een integrerend onderdeel is van de financiële overzichten vanwege de aard 
hiervan en hoe deze wordt gepresenteerd. Wanneer het een integrerend onderdeel is van het 
financieel overzicht, dient de aanvullende informatie door het oordeel van de auditor te worden 
omvat. 
 
 
18  ISA 701, paragrafen 11-16.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 16/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
54. 
Indien aanvullende informatie die niet wordt vereist door het van toepassing zijnde stelsel inzake 
financiële verslaggeving niet wordt beschouwd als een integrerend onderdeel van het 
gecontroleerde financieel overzicht dient de auditor te evalueren of dergelijke aanvullende 
informatie op een manier wordt weergegeven die voldoende is en duidelijk onderscheid maakt 
tussen de gecontroleerde financiële overzichten. Indien dit niet het geval is, dient de auditor het 
management te verzoeken de wijze waarop niet-gecontroleerde aanvullende informatie wordt 
gepresenteerd, te wijzigen. Als het management dat weigert, dient de auditor de niet-
gecontroleerde aanvullende informatie te identificeren en in de controleverklaring uiteen te zetten 
dat die aanvullende informatie niet is gecontroleerd. 
 
 
**** 
Toepassingsgerichte en overige verklarende teksten 
 
Kwalitatieve aspecten van de praktijken van de entiteit inzake administratieve verwerking (Zie 
par. 12) 
 
A1. 
Het management maakt een aantal oordeelsvormingen met betrekking tot de in de financiële 
overzichten opgenomen bedragen en toelichtingen. 
 
A2. 
ISA 260 (herzien) omvat een uiteenzetting van de kwalitatieve aspecten van praktijken inzake 
administratieve verwerking19. Bij het in aanmerking nemen van de kwalitatieve aspecten van de 
praktijken van de entiteit inzake administratieve verwerking, is het mogelijk dat de auditor zich 
bewust wordt van mogelijke tendentie in de oordeelsvormingen van het management. De auditor 
kan tot de conclusie komen dat het cumulatieve effect van het gebrek aan neutraliteit, samen met 
het effect van niet-gecorrigeerde afwijkingen, ertoe leidt dat de financiële overzichten als geheel 
een afwijking van materieel belang bevatten. Indicaties voor een gebrek aan neutraliteit dat een 
effect kan hebben op de evaluatie door de auditor van de vraag of de financiële overzichten als 
geheel een afwijking van materieel belang bevatten, zijn onder meer: 
 
• 
De selectieve correctie van afwijkingen die tijdens de controle onder de aandacht van het 
management zijn gebracht (bijv. het corrigeren van afwijkingen die het effect hebben dat 
ze de gerapporteerde winsten verhogen, maar het niet corrigeren van afwijkingen die het 
effect hebben dat ze de gerapporteerde resultaten verlagen); 
• 
Mogelijke tendentie bij het management bij het maken van schattingen. 
 
A3. 
ISA 540 (herzien) behandelt mogelijke tendentie bij het management bij het maken van 
schattingen.20 Indicaties voor mogelijke tendentie bij het management vormen geen afwijkingen 
bij het trekken van conclusies over de redelijkheid van individuele schattingen. Zij kunnen echter 
wel van invloed zijn op de evaluatie door de auditor van de vraag of de financiële overzichten 
als geheel vrij zijn van een afwijking van materieel belang. 
 
Grondslagen voor financiële verslaggeving op passende wijze toegelicht in de financiële 
overzichten (Zie par. 13(a)) 
 
A4. 
Bij de evaluatie of de financiële overzichten op de juiste wijze de belangrijke geselecteerd en 
toegepaste grondslagen toelichten, omvat de overweging van de accountant aangelegenheden 
als: 
 
 
19  ISA 260 (herzien), Communicatie met de met governance belaste personen, Bijlage 2. 
20  ISA 540 (herzien), De controle van schattingen en de toelichtingen daarop, paragraaf 21.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 17/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
• 
Of alle toelichtingen met betrekking tot de belangrijke grondslagen voor financiële 
verslaggeving die vereist zijn om te worden opgenomen op grond van het van toepassing 
zijnde stelsel inzake financiële verslaggeving zijn toegelicht; 
• 
Of de informatie over de belangrijke grondslagen voor financiële verslaggeving die zijn 
toegelicht relevant is en derhalve reflecteert hoe de verantwoording, waardering en 
presentatie criteria in het van toepassing zijnde stelsel inzake financiële verslaggeving zijn 
toegepast op transactiestromen, rekeningsaldi en toelichtingen in de financiële overzichten 
in de specifieke omstandigheden van de activiteiten van de entiteit en haar omgeving; en 
• 
De duidelijkheid waarmee de belangrijke grondslagen voor financiële verslaggeving zijn 
gepresenteerd. 
 
Informatie die gepresenteerd is in de financiële overzichten is relevant, betrouwbaar, 
vergelijkbaar en begrijpelijk (Zie par. 13(d)) 
 
A5. 
Evalueren van de begrijpelijkheid van de financiële overzichten omvat overweging van dergelijke 
aangelegenheden zoals de vraag of : 
 
• 
De informatie in de financiële overzichten gepresenteerd wordt op een duidelijke en 
beknopte wijze; 
• 
De plaatsing van significante toelichtingen gepaste aandacht hieraan geeft (bijvoorbeeld 
wanneer er gepercipieerde waarde is van entiteit specifieke informatie voor gebruikers) en 
of de toelichtingen passende kruisverwijzingen bevatten op een manier die geen 
significante uitdagingen aan gebruikers zou geven bij het identificeren van noodzakelijke 
informatie. 
 
Toelichting van het effect van transacties en gebeurtenissen van materieel belang op de in de 
financiële overzichten bekendgemaakte informatie (Zie par. 13(e)) 
 
A6. 
Het is gebruikelijk dat financiële overzichten die in overeenstemming met een stelsel voor 
algemene doeleinden zijn opgesteld de financiële positie, de financiële prestaties en de 
kasstromen van een entiteit presenteren. Evalueren of, in het licht van het van toepassing zijnde 
stelsel 
inzake financiële verslaggeving, de financiële overzichten adequate toelichtingen 
verschaffen om de beoogde gebruikers in staat te stellen het effect van de van materieel belang 
zijnde transacties en gebeurtenissen op de financiële positie, de financiële prestaties en de 
kasstromen van de entiteit te begrijpen omvat overwegen van aangelegenheden als: 
 
• 
De mate waarin de informatie in de financiële overzichten relevant en specifiek is voor de 
omstandigheden van de entiteit; en 
• 
Of de toelichtingen adequaat zijn om de beoogde gebruikers te helpen om te begrijpen: 
 
o 
De aard en omvang van de potentiële activa en verplichtingen van de entiteit die 
voortvloeien uit transacties of gebeurtenissen die niet voldoen aan de criteria voor 
opname (of de criteria voor van de balans halen), vastgesteld door het van 
toepassing zijnde stelsel inzake financiële verslaggeving; 
o 
De aard en omvang van de risico's van een afwijking van materieel belang die 
voortvloeien uit transacties en gebeurtenissen; 
o 
De gebruikte methoden en de gemaakte veronderstellingen en oordeelsvormingen 
en veranderingen daarin, die van invloed zijn op de gepresenteerde of anderszins 
toegelichte bedragen inclusief relevante gevoeligheidsanalyses.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 18/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Evalueren of de financiële overzichten een getrouwe weergave vormen (Zie par. 14) 
 
A7. 
Sommige stelsels inzake financiële verslaggeving erkennen expliciet of impliciet het concept van 
getrouwe weergave21. Zoals vermeld in paragraaf 7(b) van deze ISA, vereist een getrouw beeld 
stelsel22 inzake financiële verslaggeving niet alleen voldoen aan de eisen van het stelsel, maar 
erkent het ook expliciet of impliciet dat het nodig kan zijn voor het management om toelichtingen 
te verstrekken die verder gaan dan degene die specifiek vereist zijn op grond van het stelsel23. 
 
A8. 
De evaluatie van de auditor over de vraag of de financiële overzichten een getrouwe weergave 
vormen, zowel ten aanzien van presentatie als toelichting, is een kwestie van professionele 
oordeelsvorming. Deze evaluatie houdt rekening met aangelegenheden als de feiten en 
omstandigheden van de entiteit, inclusief de wijzigingen daarin, gebaseerd op inzicht van de 
auditor in de entiteit en de controle controle-informatie verkregen tijdens de controle. De evaluatie 
omvat ook overweging van bijvoorbeeld de toelichtingen die nodig zijn om een getrouw beeld te 
vormen als gevolg van aangelegenheden die van materieel belang zouden kunnen zijn (dat wil 
zeggen, in het algemeen worden afwijkingen beschouwd als van materieel belang als 
redelijkerwijs kan worden verwacht dat zij de economische beslissingen die gebruikers nemen op 
basis van de financiële overzichten als geheel beïnvloeden), zoals het effect van de veranderende 
financiële rapportagevereisten of de veranderende economische omgeving. 
 
A9. 
Evalueren of de financiële overzichten een getrouwe weergave vormen kan 
bijvoorbeeld 
gesprekken met het management en de personen belast met governance over hun opvattingen 
over waarom een bepaalde presentatie werd gekozen omvatten, evenals alternatieven die 
mogelijk zijn overwogen. De besprekingen kunnen bijvoorbeeld omvatten: 
 
• 
De mate waarin de bedragen in de financiële overzichten zijn samengevoegd of opgesplitst, 
en of de presentatie van de bedragen of toelichtingen nuttige informatie verhult of resulteert 
in misleidende informatie; 
• 
Consistentie met geschikte sector specifieke praktijken, of dat eventuele afwijkingen 
relevant zijn voor de omstandigheden van de entiteit en daarom gerechtvaardigd zijn. 
 
Beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving (Zie par. 15) 
 
A10. Zoals in ISA 200 uiteengezet, vereist het opstellen van de financiële overzichten door het 
management en, in voorkomend geval, de met governance belaste personen, dat in de financiële 
overzichten een adequate beschrijving van het van toepassing zijnde stelsel inzake financiële 
verslaggeving wordt opgenomen.24 Deze beschrijving informeert de gebruikers van de financiële 
overzichten over het stelsel waarop de financiële overzichten zijn gebaseerd. 
 
A11. Een beschrijving dat de financiële overzichten zijn opgesteld in overeenstemming met een 
bepaald van toepassing zijnd stelsel inzake financiële verslaggeving is alleen passend als de 
financiële overzichten in overeenstemming zijn met alle door dat stelsel gestelde vereisten die 
van toepassing zijn gedurende de periode waarop de financiële overzichten betrekking hebben. 
 
A12. Een beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving die 
onnauwkeurige kwalificerende of beperkende formuleringen omvat (bv. “de financiële overzichten 
zijn grotendeels in overeenstemming met de International Financial Reporting Standards”) is 
 
21  Bijvoorbeeld, de International Financial Reporting Standards (IFRS) geven aan dat een getrouwe weergave de getrouwe 
weergave vereist van de gevolgen van transacties, andere gebeurtenissen en omstandigheden in overeenstemming met de 
definities en opnamecriteria voor activa, passiva, baten en lasten. 
22  Zie ISA 200, paragraaf 13(a). 
23  Bijvoorbeeld IFRS vereist van een entiteit om aanvullende informatie te vertrekken, wanneer de naleving van de specifieke 
vereisten in de IFRS ontoereikend is om gebruikers in staat te stellen om de impact van bepaalde transacties, andere 
gebeurtenissen en omstandigheden op financiële prestaties van de entiteit te begrijpen (International Accounting Standard 1 
Presentatie van de financiële overzichten paragraaf 17 (c)). 
24  ISA 200, paragraaf A4-A5.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 19/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
geen adequate beschrijving van dat stelsel, aangezien het gebruikers van de financiële 
overzichten kan misleiden. 
 
Verwijzing naar meer dan één stelsel inzake financiële verslaggeving 
 
A13. Soms wordt in financiële overzichten gesteld dat zij zijn opgesteld in overeenstemming met twee 
stelsels inzake financiële verslaggeving (bv. het nationale stelsel en de IFRS). Dit kan zijn omdat 
het management verplicht is of ervoor heeft gekozen de financiële overzichten op te stellen in 
overeenstemming met beide stelsels, in welk geval beide stelsels van toepassing zijnde stelsels 
inzake financiële verslaggeving zijn. Een dergelijke beschrijving is alleen passend indien de 
financiële overzichten in overeenstemming zijn met elk van de stelsels afzonderlijk. Om te worden 
beschouwd als zijnde opgesteld in overeenstemming met beide stelsels, is het nodig dat de 
financiële overzichten tegelijkertijd met beide stelsels in overeenstemming zijn zonder dat 
aansluitingsoverzichten nodig zijn. In de praktijk is gelijktijdige overeenstemming onwaarschijnlijk, 
tenzij het rechtsgebied het andere stelsel (bv. de IFRS) als zijn eigen nationale stelsel heeft 
aangenomen of alle belemmeringen voor het daarmee in overeenstemming zijn heeft 
weggenomen. 
 
A14. Financiële overzichten die zijn opgesteld in overeenstemming met een bepaald stelsel inzake 
financiële verslaggeving en die een toelichting of aanvullend overzicht bevatten met een 
aansluiting van de resultaten met die welke onder een ander stelsel zouden worden 
weergegeven, zijn niet opgesteld in overeenstemming met dat andere stelsel. Dit is omdat de 
financiële overzichten niet alle informatie omvatten op de wijze die door dat andere stelsel wordt 
vereist. 
 
A15. De financiële overzichten kunnen evenwel zijn opgesteld in overeenstemming met één van 
toepassing zijnd stelsel inzake financiële verslaggeving en daarnaast in de toelichting beschrijven 
in welke mate ze in overeenstemming zijn met een ander stelsel (bijv. financiële overzichten 
opgesteld in overeenstemming met het nationale stelsel die tevens beschrijven in welke mate zij 
in overeenstemming zijn met de IFRS). Een dergelijke beschrijving kan aanvullende financiële 
informatie vormen– zoals in paragraaf 54 uiteen wordt gezet en wordt bijgevolg door het oordeel 
van de auditor omvat indien het niet duidelijk van de financiële overzichten kan worden 
onderscheiden. 
 
Vorm van het oordeel 
 
A16. Er kunnen zich gevallen voordoen waarin financiële overzichten die zijn opgesteld in 
overeenstemming met de door een getrouw-beeld-stelsel gestelde vereisten geen getrouwe 
weergave vormen. Als dit het geval is, kan het management in de financiële overzichten 
aanvullende toelichtingen opnemen naast die welke het stelsel specifiek vereist of, in uiterst 
zeldzame omstandigheden, afwijken van een door het stelsel gesteld vereiste opdat de financiële 
overzichten een getrouwe weergave vormen. (Zie par. 18) 
 
A17. Het zal uiterst zelden voorkomen dat de auditor financiële overzichten die zijn opgesteld in 
overeenstemming met een compliance-stelsel als misleidend beschouwt indien, overeenkomstig 
ISA 210, de auditor heeft vastgesteld dat het stelsel aanvaardbaar is.25 (Zie par. 19) 
 
Controleverklaring (Zie par. 20) 
 
A18. Een schriftelijke verklaring omvat zowel verklaringen in papieren vorm als in elektronische vorm. 
 
A19. De bijlage van deze ISA bevat voorbeelden van controleverklaringen over financiële overzichten 
waarin de in de paragrafen 20-49 uiteengezette elementen zijn opgenomen. Met uitzondering van 
de secties Oordeel en Basis voor het oordeel, stelt deze ISA geen vereisten vast voor de volgorde 
van de elementen van de controleverklaring. Deze ISA vereist echter wel het gebruik van 
 
25  ISA 210, “Overeenkomen van de voorwaarden van controleopdrachten”, paragraaf 6(a).

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 20/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
specifieke titels, die bedoeld zijn om te helpen om controleverklaringen die verwijzen naar 
controles die zijn uitgevoerd overeenkomstig ISA en, herkenbaarder te maken, in het bijzonder in 
situaties waar de elementen van de controleverklaring zijn weergegeven in een volgorde die 
afwijkt van de voorbeelden van controleverklaringen in de bijlage van deze ISA. 
 
Controleverklaring voor controles uitgevoerd overeenkomstig de International Standards on Auditing 
 
Titel (Zie par. 21) 
 
A20. Een titel die aangeeft dat de verklaring een verklaring van een onafhankelijke auditor is, 
bijvoorbeeld Controleverklaring van de onafhankelijke auditor, onderscheidt bijgevolg de 
controleverklaring van de onafhankelijke auditor van verklaringen die door anderen zijn 
uitgebracht. 
 
Geadresseerde (Zie par. 22) 
 
A21. Wet- of regelgeving of de voorwaarden van de opdracht specificeren vaak aan wie de 
controleverklaring 
in 
dat 
specifieke 
rechtsgebied 
moet 
worden 
geadresseerd. 
De 
controleverklaring wordt gewoonlijk geadresseerd aan de personen voor wie de verklaring wordt 
opgesteld, vaak ofwel aan de aandeelhouders, ofwel aan de met governance belaste personen 
van de entiteit waarvan de financiële overzichten worden gecontroleerd. 
 
Oordeel van de auditor (Zie Par 24-26) 
 
Verwijzing naar de financiële overzichten die zijn gecontroleerd 
 
A22. De controleverklaring vermeldt bijvoorbeeld dat de auditor de financiële overzichten van de 
entiteit heeft gecontroleerd, die bestaan uit [vermelding van de titel van elk financieel overzicht 
dat bestaat uit de volledige set financiële overzichten die door het van toepassing zijnde stelsel 
inzake financiële verslaggeving zijn vereist, met vermelding van de datum of periode waarop elk 
financieel overzicht betrekking heeft] en toelichtingen op de financiële overzichten, inclusief een 
samenvatting van significante grondslagen voor de financiële verslaggeving. 
 
A23. Indien de auditor op de hoogte is van het feit dat de gecontroleerde financiële overzichten zullen 
worden opgenomen in een document dat andere informatie bevat, zoals een jaarrapport, kan de 
auditor overwegen, indien de vorm van de presentatie dit toelaat, de nummers te vermelden van 
de pagina’s waarop de gecontroleerde financiële overzichten zijn gepresenteerd. Dit helpt de 
gebruikers te bepalen op welke financiële overzichten de controleverklaring betrekking heeft. 
 
 ‘Vormt een getrouwe weergave, in alle van materieel belang zijnde opzichten’ of ‘geeft een getrouw 
beeld’ 
 
A24. De zinnen “Vormt een getrouwe weergave, in alle van materieel belang zijnde opzichten’ of ‘geeft 
een getrouw beeld” worden als gelijkwaardig beschouwd. Of de formulering ‘vormt een getrouwe 
weergave, in alle van materieel belang zijnde opzichten’, dan wel de formulering ‘geeft een 
getrouw beeld’ in een bepaald rechtsgebied wordt gebruikt, wordt bepaald door de wet- of 
regelgeving die de controle van financiële overzichten in dat rechtsgebied regelt, of door de 
algemeen aanvaarde praktijk in dat rechtsgebied. Indien de wet- of regelgeving vereist dat andere 
formuleringen worden gebruikt, heeft dit geen invloed op de in paragraaf 14 van deze ISA 
beschreven vereiste dat de auditor de getrouwe weergave van financiële overzichten die zijn 
opgesteld in overeenstemming met een getrouw-beeld-stelsel evalueert. 
 
A25. Als de auditor een goedkeurend oordeel tot uitdrukking brengt, is het niet passend om 
formuleringen te gebruiken zoals “met de voorgaande uitleg” of “behoudens” in de relatie tot het 
oordeel aangezien deze een voorwaardelijk oordeel of een verzwakking of een aanpassing van 
het oordeel suggereren.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 21/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Beschrijving van de financiële overzichten en de aangelegenheden zij weergeven 
   
A26. Het oordeel van de auditor omvat de volledige set financiële overzichten zoals gedefinieerd door 
het van toepassing zijnde stelsel inzake financiële verslaggeving. Bijvoorbeeld in het geval van 
vele stelsels voor algemene doeleinden omvatten de financiële overzichten: een overzicht van de 
financiële positie en een overzicht van gerealiseerde en niet-gerealiseerde resultaten; een 
mutatieoverzicht van het eigen vermogen, een kasstroomoverzicht, en daarop betrekking 
hebbende toelichtingen die gewoonlijk bestaan uit een overzicht van de belangrijke gehanteerde 
grondslagen voor financiële verslaggeving en andere toelichtingen. In bepaalde rechtsgebieden 
kan aanvullende informatie eveneens worden beschouwd als een integrerend onderdeel van de 
financiële overzichten. 
 
A27. In het geval van financiële overzichten die in overeenstemming met een getrouw-beeld stelsel 
zijn opgesteld, wordt in het oordeel van de auditor vermeld dat de financiële overzichten een 
getrouwe weergave vormen, in alle van materieel belang zijnde opzichten, dan wel een getrouw 
beeld geven van de aangelegenheden waarvoor is voorzien dat deze in de financiële overzichten 
worden gepresenteerd. In het geval van financiële overzichten die bijvoorbeeld zijn opgesteld in 
overeenstemming met IFRS, zijn deze aangelegenheden de financiële positie van de entiteit 
zoals op het einde van de verslagperiode en de financiële prestatie van de entiteit en de 
kasstromen voor de verslagperiode die net is geëindigd. Derhalve is […] in paragraaf 25 en elders 
in deze ISA bedoeld om te worden vervangen door de schuingedrukte woorden in de voorgaande 
zin wanneer het van toepassing zijnde stelsel inzake financiële verslaggeving IFRS is of, in het 
geval van andere van toepassing zijnde stelsels inzake financiële verslaggeving, te worden 
vervangen door bewoordingen die de aangelegenheden beschrijven waarvoor is voorzien dat 
deze in de financiële overzichten worden gepresenteerd. 
 
Beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving en de wijze waarop 
dit het oordeel van de auditor kan beïnvloeden 
 
A28. De vermelding van het van toepassing zijnde stelsel inzake financiële verslaggeving in het 
oordeel van de auditor is bedoeld om de gebruikers van de controleverklaring de nodige 
informatie te verschaffen over de context waarbinnen het oordeel van de auditor tot uitdrukking 
wordt gebracht; dit is niet bedoeld om de op grond van paragraaf 14 vereiste evaluatie te 
beperken. Het van toepassing zijnde stelsel inzake financiële verslaggeving wordt als volgt 
vermeld: 
 
‘… in overeenstemming met de International Financial Reporting Standards’ of 
‘… in overeenstemming met de in rechtsgebied X algemeen aanvaarde verslaggevingsprincipes’ 
 
A29. Indien het van toepassing zijnde stelsel inzake financiële verslaggeving standaarden voor 
financiële verslaggeving alsmede voorschriften van wet- of regelgeving omvat, wordt het stelsel 
als volgt vermeld: ‘… in overeenstemming met de International Financial Reporting Standards en 
de door de vennootschapswet van rechtsgebied X gestelde vereisten’. ISA 210 behandelt 
omstandigheden waarin er conflicten optreden tussen de standaarden voor financiële 
verslaggeving en de door de wet- of regelgever gestelde vereisten.26 
 
A30. Zoals in paragraaf A13 aangegeven, is het mogelijk dat financiële overzichten zijn opgesteld in 
overeenstemming met twee stelsels inzake financiële verslaggeving, die derhalve beide van 
toepassing zijnde stelsels inzake financiële verslaggeving zijn. Bijgevolg neemt de auditor elk 
stelsel apart in overweging bij het vormen van zijn oordeel over de financiële overzichten, en 
verwijst hij in zijn oordeel in overeenstemming met de paragrafen 25-27 naar de beide stelsels 
als volgt: 
 
(a) 
Indien de financiële overzichten in overeenstemming zijn met elk van de beide stelsels, 
individueel genomen, worden twee oordelen tot uitdrukking gebracht: dat de financiële 
overzichten zijn opgesteld in overeenstemming met één van de van toepassing zijnde 
 
26  ISA 210, paragraaf 18.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 22/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
stelsels inzake financiële verslaggeving (bijv. het nationale stelsel) en dat de financiële 
overzichten zijn opgesteld in overeenstemming met het andere van toepassing zijnde 
stelsel inzake financiële verslaggeving (bijv. de IFRS). Deze oordelen kunnen afzonderlijk 
of in een enkele zin tot uitdrukking worden gebracht (bijv. de financiële overzichten vormen 
een getrouwe weergave, in alle van materieel belang zijnde opzichten, in overeenstemming 
met de in rechtsgebied X algemeen aanvaarde verslaggevingsprincipes en met de IFRS); 
(b) 
Indien de financiële overzichten in overeenstemming zijn met één van de stelsels maar niet 
met het andere stelsel, kan een goedkeurend oordeel worden gegeven dat de financiële 
overzichten zijn opgesteld in overeenstemming met het ene stelsel (bijv. het nationale 
stelsel), maar een aangepast oordeel met betrekking tot het andere stelsel (bijv. de IFRS) 
overeenkomstig ISA 705 (herzien). 
 
A31. Zoals in paragraaf A15 aangegeven, is het mogelijk dat in financiële overzichten wordt vermeld 
dat ze in overeenstemming zijn met het van toepassing zijnde stelsel inzake financiële 
verslaggeving en dat daarnaast de mate van overeenstemming met een ander stelsel inzake 
financiële verslaggeving wordt toegelicht. Dergelijke aanvullende informatie wordt omvat door het 
oordeel van de auditor aangezien ze niet duidelijk kan worden onderscheiden van de financiële 
overzichten (Zie par. 53-54 en gerelateerde toepassingsgerichte teksten in Par. A78-A84). 
Derhalve, 
 
(a) 
Indien de toelichting met betrekking tot het in overeenstemming zijn met het andere stelsel 
misleidend is, wordt een aangepast oordeel tot uitdrukking gebracht overeenkomstig ISA 
705 (herzien); 
(b) 
Indien de toelichting niet misleidend is, maar de auditor van oordeel is dat ze van een 
dusdanig belang is dat ze fundamenteel is voor het begrip van de gebruikers van de 
financiële 
overzichten, 
wordt 
een 
paragraaf 
ter 
benadrukking 
van 
bepaalde 
aangelegenheden toegevoegd overeenkomstig ISA 706 (herzien), waarbij de aandacht 
wordt gevestigd op de toelichting. 
 
Basis voor het oordeel (Zie par. 28) 
 
A32. De sectie “Basis voor het oordeel” verschaft belangrijke context over het oordeel van de auditor. 
Derhalve is op grond van deze ISA vereist dat de sectie “Basis voor ons oordeel” direct de sectie 
“Oordeel” opvolgt in de controleverklaring. 
 
A33. De verwijzing naar de Standaarden die worden gebruikt maakt de gebruikers van de 
controleverklaring duidelijk dat de controle is uitgevoerd in overeenstemming met vastgestelde 
Standaarden. 
 
Relevante ethische voorschriften (Zie par. 28(c)) 
 
A34. De identificatie van het oorspronkelijke rechtsgebied van relevante ethische voorschriften 
vergroot de transparantie over die vereisten die betrekking hebben op de desbetreffende 
controleopdracht. In ISA 200 wordt uitgelegd dat relevante ethische vereisten gewoonlijk bestaan 
uit de delen A en B van de IFAC Code met betrekking tot een controle van financiële overzichten 
samen met nationale vereisten die stringenter zijn.27 Indien de relevante ethische voorschriften 
deze van de IFAC Code bevatten, kan de vermelding ook verwijzen naar de IFAC Code. Indien 
de IFAC Code alle relevante ethische vereisten met betrekking tot een controle van financiële 
overzichten vormt, moet de vermelding niet het oorspronkelijke rechtsgebied identificeren. 
  
A35. In sommige rechtsgebieden kunnen er relevante ethische voorschriften aan een aantal 
verschillende bronnen worden ontleend zoals de ethische code(s) en aanvullende regels en 
vereisten binnen wet- en regelgeving. Wanneer de onafhankelijkheid en andere relevante 
ethische voorschriften binnen een beperkt aantal bronnen is gevat, kan de auditor ervoor kiezen 
om de relevante bron(nen) te noemen, (bijv. de naam van de code, wet- of regelgeving die in het 
 
27. ISA 200, paragraaf A17.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 23/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
rechtsgebied van toepassing is) of hij kan naar een voorwaarde verwijzen die doorgaans 
algemeen wordt begrepen en die op gepaste wijze die bronnen samenvat (bijv. 
onafhankelijkheidsvereisten voor controle van niet-beursgenoteerde entiteiten in rechtsgebied X). 
  
A36. Wet- of regelgeving, nationale controlestandaarden of de voorwaarden van een controleopdracht 
kunnen van de auditor vereisen om in de controleverklaring meer specifieke informatie over de 
bronnen van de relevante ethische voorschriften te verschaffen, met inbegrip van die betreffende 
onafhankelijkheid, die zijn toegepast op de controle van de financiële overzichten. 
 
A37. Bij het bepalen wat de gepaste hoeveelheid informatie is die in de controleverklaring moet worden 
opgenomen wanneer er sprake is van meerdere bronnen van relevante ethische voorschriften 
met betrekking tot de controle van de financiële overzichten, is een belangrijke overweging de 
balans tussen transparantie en het risico van het verhullen van overige nuttige informatie in de 
controleverklaring. 
 
Overwegingen specifiek voor groepscontroles 
 
A38. Wanneer er bij groepscontroles sprake is van meerdere bronnen van relevante ethische 
voorschriften, inclusief degenen die betrekking hebben op onafhankelijkheid, heeft de verwijzing 
in de controleverklaring naar het rechtsgebied doorgaans betrekking op de relevante ethische 
voorschriften die van toepassing zijn op het opdrachtteam op groepsniveau. Dit is het geval omdat 
in een groepscontrole auditor van groepsonderdelen ook onderworpen zijn aan ethische 
voorschriften die relevant zijn voor de groepscontrole.28 
 
A39. De ISA’s stellen geen specifieke onafhankelijkheids- of ethische voorschriften vast voor auditor, 
onder wie ook auditor van groepsonderdelen, en breiden deze dus niet uit, of doorbreken deze 
anderszins, de onafhankelijkheidsvereisten van de IFAC Code of overige ethische voorschriften 
waaraan het opdrachtteam op groepsniveau onderhevig is, noch vereisen zij dat de auditor van 
groepsonderdelen in alle gevallen onderhevig is aan dezelfde onafhankelijkheidsvereisten die 
van toepassing zijn op de opdracht op groepsniveau. Als gevolg daarvan kunnen de relevante 
ethische voorschriften, inclusief degenen die betrekking hebben op onafhankelijkheid in het geval 
van een groepscontrole complex zijn. ISA 60029 verschaft leidraden voor auditor bij het uitvoeren 
van werkzaamheden inzake de financiële informatie van een onderdeel voor een groepscontrole, 
inclusief die situaties waar de auditor van groepsonderdelen niet voldoet aan de 
onafhankelijkheidsvereisten die voor de groepscontrole relevant zijn. 
 
Kernpunten van de controle (Zie par. 31) 
 
A40. Wet- of regelgeving kan communicatie van kernpunten van de controle vereisen voor andere 
entiteiten dan beursgenoteerde entiteiten, zoals entiteiten die in deze wet- of regelgeving 
gedefinieerd worden als organisaties van openbaar belang. 
  
A41. De auditor kan er tevens voor kiezen om kernpunten van de controle te communiceren voor 
andere entiteiten dan beursgenoteerde entiteiten, inclusief degenen die van significant openbaar 
belang kunnen zijn, bijvoorbeeld omdat zij een groot aantal en breed scala aan aandeelhouders 
hebben en gezien de aard en omvang van de activiteiten. Voorbeelden van dergelijke entiteiten 
kunnen financiële instellingen zijn (zoals pensioenfondsen) en andere entiteiten zoals charitatieve 
instellingen. 
 
A42. Op grond van ISA 210 is van de auditor vereist om de voorwaarden van de controleopdracht met 
het management en, in voorkomend geval, de met governance belaste personen overeen te 
komen en hier wordt ook uitgelegd dat de rollen van het management en de met governance 
belaste personen voor de entiteit afhankelijk zijn van de governance-regelingen van de entiteit en 
relevante wet- of regelgeving.30 Op grond van ISA 210 wordt tevens vereist dat de 
 
28  ISA 600, paragraaf A37. 
29  ISA 600, paragrafen 19-20. 
30  ISA 210, paragrafen 9 en A22.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 24/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
opdrachtbevestiging of een andere geschikte vorm van schriftelijke overeenkomst een verwijzing 
bevat naar de verwachte vorm en inhoud van de rapportages die door de auditor worden 
uitgebracht.31 Wanneer van de auditor niet anderszins is vereist om kernpunten van de controle 
te communiceren wordt er in ISA 21032 uitgelegd dat het voor de auditor nuttig kan zijn om in de 
voorwaarden van de controleopdracht te verwijzen naar de mogelijkheid van het communiceren 
van kernpunten van de controle in de controleverklaring en kan het in sommige rechtsgebieden 
voor de auditor noodzakelijk zijn om een verwijzing naar een dergelijke mogelijkheid op te nemen 
om de mogelijkheid om dit te doen te handhaven. 
 
Overwegingen specifiek voor entiteiten in de publieke sector 
 
A43. Beursgenoteerde entiteiten zijn niet gebruikelijk in de publieke sector. Entiteiten in de publieke 
sector kunnen significant zijn door hun grootte, complexiteit of aspecten van openbaar belang. In 
dergelijke gevallen kan van een auditor van een entiteit in de publieke sector op grond van wet- 
of regelgeving vereist zijn of kan hij anderszins beslissen om de kernpunten van de controle in 
de controleverklaring te communiceren. 
 
Verantwoordelijkheden van het management voor de financiële overzichten (Zie par. 33-35) 
 
A44. In ISA 200 wordt het uitgangspunt met betrekking tot de verantwoordelijkheden van het 
management en, in voorkomend geval, van de met governance belaste personen, op basis 
waarvan een controle overeenkomstig de ISA’s wordt uitgevoerd33. Het management en, waar 
van toepassing, de met governance belaste personen aanvaarden de verantwoordelijkheid voor 
het opstellen van de financiële overzichten in overeenkomst met het financiële stelsel inzake 
financiële verslaggeving, met inbegrip van, waar relevant, de getrouwe weergave hiervan. Het 
management aanvaardt tevens de verantwoordelijkheid voor dergelijke interne beheersing die 
het noodzakelijk acht om het opstellen van de financiële overzichten die geen afwijking van 
materieel belang bevatten als gevolg van fraude of van fouten mogelijk te maken. De beschrijving 
van de verantwoordelijkheden van het management in de controleverklaring omvat een verwijzing 
naar beide verantwoordelijkheden aangezien dit helpt om de gebruikers het uitgangspunt uit te 
leggen op basis waarvan een controle wordt uitgevoerd. ISA 260 (herzien) hanteert de term de 
met governance belaste personen om de persoon/personen of organisatie(s) te beschrijven met 
de verantwoordelijkheid voor het toezicht op de entiteit en verschaft een bespreking over de 
diversiteit van governance-structuren tussen rechtsgebieden en per entiteit. 
 
A45. Er kunnen zich omstandigheden voordoen waarin het voor de auditor passend is om de 
beschrijving van de verantwoordelijkheden van het management en de met governance belaste 
personen in paragraaf 34-35 uit te breiden teneinde de aanvullende verantwoordelijkheden weer 
te geven die relevant zijn voor het opstellen van de financiële overzichten in de context van het 
specifieke rechtsgebied of gegeven de aard van de entiteit. 
  
A46. Op grond van ISA 210 wordt van de auditor vereist om in een opdrachtbevestiging of andere 
geschikte vorm van schriftelijke overeenkomst in te stemmen met de verantwoordelijkheden van 
het management34. ISA 210 voorziet in enige flexibiliteit hoe dat te doen door uit te leggen dat, 
indien wet- of regelgeving de verantwoordelijkheden van het management en, waar van 
toepassing, de met governance belaste personen voorschrijft met betrekking tot de financiële 
verslaggeving kan de auditor bepalen dat de wet- of regelgeving verantwoordelijkheden bevat 
die, naar het oordeel van de auditor, equivalent zijn aan die welke in ISA 210 uiteen zijn gezet. 
Voor dergelijke verantwoordelijkheden die equivalent zijn kan de auditor de bewoordingen 
gebruiken van de wet- of regelgeving om dezen in een opdrachtbevestiging of andere geschikte 
vorm van schriftelijke overeenkomst te beschrijven. In dergelijke gevallen kunnen deze 
bewoordingen ook worden gebruikt in de controleverklaring om de verantwoordelijkheden te 
beschrijven zoals op grond van paragraaf 34(a) van deze ISA is vereist. Ter aanvulling op het 
 
31  ISA 210, paragraaf 10. 
32  ISA 210, paragraaf A25. 
33  ISA 200, paragraaf 13(j). 
34  ISA 210, paragraaf 6(b)(i)-(ii).

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 25/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
opnemen van de beschrijving van de verantwoordelijkheden van het management in de 
controleverklaring zoals vereist op grond van paragraaf 34, kan de auditor verwijzen naar een 
gedetailleerdere beschrijving van deze verantwoordelijkheden door een verwijzing op te nemen 
naar waar dergelijke informatie verkregen kan worden (bijv. in het jaarrapport van de entiteit of 
een website van een bevoegde instantie). 
 
A47. In sommige rechtsgebieden is het mogelijk dat wet- of regelgeving die de verantwoordelijkheden 
van het management voorschrijft specifiek verwijst naar een verantwoordelijkheid voor de 
adequaatheid van de administratie en vastleggingen, of van het systeem van de administratieve 
verwerking. Aangezien boeken, vastleggingen en systemen een integrerend onderdeel van de 
interne beheersing (zoals gedefinieerd in ISA 315 (herzien 2019)35) zijn, verwijzen de 
beschrijvingen in ISA 210 en in paragraaf 34 niet specifiek daarnaar. 
 
A48. De bijlage van deze ISA verschaft voorbeelden van hoe de vereiste in paragraaf 34(b) zou worden 
toegepast wanneer IFRS het van toepassing zijnde stelsel inzake financiële verslaggeving is. 
Indien een van toepassing zijnd stelsel inzake financiële verslaggeving anders dan IFRS gebruikt 
wordt, kan het zijn dat de voorbeelden van vermeldingen die in de bijlage staan moeten worden 
aangepast om de toepassing van een ander stelsel inzake financiële verslaggeving in de 
omstandigheden weer te geven. 
 
Toezicht op het proces van financiële verslaggeving (Zie par. 35) 
 
A49. Wanneer bepaalde, maar niet alle, personen die betrokken zijn bij het toezìcht op het proces van 
financiële verslaggeving tevens betrokken zijn bij het opstellen van de financiële overzichten, kan 
het nodig zijn dat de beschrijving zoals vereist op grond van paragraaf 35 van deze ISA aangepast 
moet worden om op juiste wijze de specifieke omstandigheden van de entiteit weer te geven. 
Wanneer personen die verantwoordelijk zijn voor het toezicht op het proces van financiële 
verslaggeving dezelfde zijn als diegenen die verantwoordelijk zijn voor het opstellen van de 
financiële overzichten, is er geen verwijzing naar toezichtverantwoordelijkheden vereist. 
 
De verantwoordelijkheden van de auditor voor de controle van de financiële overzichten (Zie par. 37-
40) 
 
A50. De beschrijving van de verantwoordelijkheden van de auditor zoals op grond van paragrafen 37-
40 van deze ISA is vereist, kunnen specifiek zijn gemaakt om de specifieke aard van de entiteit 
weer te geven, bijvoorbeeld wanneer de controleverklaring de geconsolideerde financiële 
overzichten behandelt. Voorbeeld 2 in de bijlage van deze ISA omvat een voorbeeld van hoe dat 
kan worden gedaan. 
 
Doelstellingen van de auditor (Zie Par 38(a)) 
 
A51. In de controleverklaring wordt uitgelegd dat de doelstellingen van de auditor bestaan uit het 
verkrijgen van een redelijke mate van zekerheid over de vraag of de financiële overzichten als 
geheel geen afwijking van materieel belang bevatten als gevolg van fraude of van fouten, en om 
een controleverklaring uit te brengen die het oordeel van de auditor omvat. Deze zijn in contrast 
met de verantwoordelijkheden van het management voor het opstellen van de financiële 
overzichten. 
 
Beschrijving van materialiteit (Zie par. 38(c)) 
  
A52. De bijlage van deze ISA verschaft voorbeelden van de wijze waarop de vereisten in paragraaf 
38(c), om een beschrijving van materialiteit te verschaffen, zouden worden toegepast wanneer 
IFRS het van toepassing zijnde stelsel inzake financiële verslaggeving is. Indien een van 
toepassing zijnd stelsel inzake financiële verslaggeving anders dan IFRS wordt gehanteerd, kan 
het nodig zijn dat de voorbeelden van vermeldingen die in de bijlage van deze ISA worden 
 
35  ISA 315 (herzien 2019), Risico's op een afwijking van materieel belang identificeren en inschatten, paragraaf 4(c).

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 26/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
weergegeven worden aangepast om de toepassing van het andere van toepassing zijnde stelsel 
inzake financiële verslaggeving in de omstandigheden weer te geven. 
 
Verantwoordelijkheden van de auditor met betrekking tot ISA 701 (Zie par. 40(c)) 
 
A53. De auditor kan het tevens nuttig achten om aanvullende informatie in de beschrijving van de 
verantwoordelijkheden van de auditor te verschaffen naast die welke op grond van paragraaf 
40(c) vereist is. De auditor kan bijvoorbeeld verwijzen naar: het vereiste in paragraaf 9 van ISA 
701 om de aangelegenheden die de significante aandacht van de auditor vereisten bij het 
uitvoeren van de controle vast te stellen, daarbij de gebieden met een hoger ingeschat risico op 
een afwijking van materieel belang of significante risico’s die overeenkomstig ISA 315 (herzien) 
zijn geïdentificeerd in overweging nemend; significante oordelen van de auditor met betrekking 
tot gebieden in de financiële overzichten die te maken hadden met significante oordeelsvorming 
van het management, inclusief schattingen met een hoge schattingsonzekerheid; en de effecten 
op de controle van significante gebeurtenissen of transacties die zich gedurende de periode 
voordeden. 
 
Plaats van de beschrijving van de verantwoordelijkheden van de auditor voor de controle van de 
financiële overzichten (Zie par. 41, 50(j)) 
 
A54. Het opnemen van de informatie die op grond van paragrafen 39-40 van deze ISA is 
vereist in een bijlage van de controleverklaring of, wanneer wet- of regelgeving of andere 
controlestandaarden dit uitdrukkelijk toestaan, het verwijzen naar een website van een 
bevoegde instantie die dergelijke informatie bevat kan een nuttige manier zijn om de 
inhoud van de controleverklaring te stroomlijnen. Omdat de beschrijving van de 
verantwoordelijkheden van de auditor echter informatie bevat die noodzakelijk is om de 
verwachtingen van gebruikers van een controle die overeenkomstig de ISA’s is 
uitgevoerd te ondersteunen, is het vereist dat er in de controleverklaring een verwijzing 
wordt opgenomen die aangeeft waar er tot dergelijke informatie toegang kan worden 
verkregen. 
 
Plaats in een bijlage (Zie par. 41(b), 50(j)) 
 
A55. Op grond van paragraaf 41 is het de auditor toegestaan om vermeldingen op te nemen die op 
grond van paragraaf 39-40 vereist zijn die de verantwoordelijkheden van de auditor voor de 
controle van de financiële overzichten in een bijlage van de controleverklaring beschrijven, onder 
de voorwaarde dat er een gepaste wijziging wordt opgenomen in de kern van de 
controleverklaring naar de plaats van de bijlage. Het volgende is een voorbeeld van de wijze 
waarop er een verwijzing in de controleverklaring kan worden gemaakt: 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten  
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijkingen van materieel belang bevatten als gevolg van 
fraude of fouten en om een controleverklaring uit te brengen die ons oordeel bevat. Een redelijke 
mate van zekerheid is een hoge mate van zekerheid, maar is geen garantie dat een controle die 
overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang detecteert 
wanneer hier sprake van is. Afwijkingen kunnen zich voordoen als gevolg van fraude of van fouten 
en worden geacht van materieel belang te zijn indien hiervan, individueel of afzonderlijk, 
redelijkerwijs zou kunnen worden verwacht dat zij de economische beslissingen die gebruikers 
op basis van de financiële overzichten nemen, beïnvloeden.  
Een verdere beschrijving van onze verantwoordelijkheden voor de controle van de financiële 
overzichten is opgenomen in bijlage X van deze controleverklaring. Deze beschrijving, die is te 
vinden op [geef het paginanummer of andere specifieke referentie naar de plaats van de 
beschrijving ], vormt onderdeel van onze controleverklaring. 
 
Referentie naar een website van een bevoegde instantie (Zie par. 41(c), 42)

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 27/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A56. In paragraaf 41 wordt uitgelegd dat de auditor kan verwijzen naar een beschrijving van de 
verantwoordelijkheden van de auditor die te vinden is op een website van een bevoegde instantie, 
mits dit uitdrukkelijk wordt toegestaan door wet- of regelgeving of nationale controlestandaarden. 
De informatie op de website die in de controleverklaring is verwerkt door middel van een 
specifieke verwijzing naar de plaats van de website waar dergelijke informatie kan worden 
gevonden kan uitvoeriger de werkzaamheden van de auditor beschrijven, of de controle 
overeenkomstig de ISA’s, maar deze kan niet strijdig zijn met de beschrijving zoals die op grond 
van paragrafen 39-40 van deze ISA is vereist. Dit houdt in dat de bewoordingen van de 
beschrijving van de verantwoordelijkheden van de auditor op de website gedetailleerder mogen 
zijn, of overige aangelegenheden kunnen behandelen die betrekking hebben op een controle van 
financiële overzichten, onder de voorwaarde dat dergelijke bewoordingen de aangelegenheden 
die worden behandeld in paragrafen 39-40 weergeeft en niet tegenspreekt. 
 
A57. Een bevoegde instantie kan een nationale organisatie zijn die controlestandaarden vaststelt, een 
regelgever of toezichthouder, of een orgaan dat toezicht houdt op de controle. Dergelijke 
organisaties zijn goed gepositioneerd om te zorgen voor de nauwkeurigheid, de volledigheid en 
blijvende beschikbaarheid van de gestandaardiseerde informatie. Het zou voor de auditor niet 
gepast zijn om een dergelijke website te onderhouden. Het volgende is een voorbeeld van de 
wijze waarop een dergelijke verwijzing naar een website zou kunnen worden gemaakt in de 
controleverklaring: 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten  
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijkingen van materieel belang bevatten als gevolg van 
fraude of fouten en om een controleverklaring uit te brengen die ons oordeel bevat. Een redelijke 
mate van zekerheid is een hoge mate van zekerheid, maar is geen garantie dat een controle die 
overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang detecteert 
wanneer hier sprake van is. Afwijkingen kunnen zich voordoen als gevolg van fraude of van fouten 
en worden geacht van materieel belang te zijn indien hiervan, individueel of afzonderlijk, 
redelijkerwijs zou kunnen worden verwacht dat zij de economische beslissingen die gebruikers 
op basis van de financiële overzichten nemen, beïnvloeden.  
Een verdere beschrijving van onze verantwoordelijkheden voor de controle van de financiële 
overzichten is te vinden op de website van [organisatie] op: [website]. Deze beschrijving is 
onderdeel van de controleverklaring. 
 
Andere rapporteringsverantwoordelijkheden (Zie. Par 43-45) 
 
A58. Bepaalde rechtsgebieden kan de auditor naast zijn verantwoordelijkheid op grond van de ISA’s 
ook aanvullende verantwoordelijkheden hebben om over overige aangelegenheden te 
rapporteren. Zo is het mogelijk dat de auditor wordt gevraagd te rapporteren over bepaalde 
aangelegenheden indien zij in de loop van de controle van de financiële overzichten onder zijn 
aandacht komen. Ook is het mogelijk dat de auditor wordt gevraagd te rapporteren over 
aanvullende specifieke werkzaamheden, of om een oordeel tot uitdrukking te brengen over 
specifieke aangelegenheden, zoals de adequaatheid van de administratie, vastleggingen en 
interne beheersing over financiële verslaggeving of andere informatie. Controlestandaarden in 
het specifieke rechtsgebied verschaffen vaak leidraden over de verantwoordelijkheden van de 
auditor met betrekking tot specifieke aanvullende rapporteringsverantwoordelijkheden in dat 
rechtsgebied. 
 
A59. In sommige gevallen is het mogelijk dat de relevante wet- of regelgeving vereist of toestaat dat 
de auditor over deze overige verantwoordelijkheden rapporteert als onderdeel van de 
controleverklaring over de financiële overzichten. In andere gevallen kan het vereist of toegestaan 
zijn dat de auditor daarover rapporteert in een afzonderlijke verklaring. 
 
A60. Paragrafen 43-45 van deze ISA staan een gecombineerde presentatie van overige 
rapporteringsverantwoordelijkheden en de verantwoordelijkheden van de auditor onder de ISA’s

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 28/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
en toe wanneer deze dezelfde onderwerpen behandelen en de bewoordingen van de 
controleverklaring 
duidelijk 
onderscheid 
maken 
tussen 
de 
overige 
rapporteringsverantwoordelijkheden en die onder de ISA’s. Dergelijk duidelijk onderscheid kan 
ervoor zorgen dat het noodzakelijk is dat de controleverklaring verwijst naar de bron van de 
overige rapporteringsverantwoordelijkheden en vermeldt dat dergelijke verantwoordelijkheden 
verder gaan dan degenen die onder de ISA’s vereist zijn. Anders is het vereist dat de overige 
rapporteringsverantwoordelijkheden worden geadresseerd in een aparte sectie in de 
controleverklaring met de titel “Verklaring betreffende overige door de wet- of regelgeving 
gestelde vereisten” of naar gelang passend in de context van de sectie. In dergelijke gevallen is 
op grond van paragraaf 45 van de auditor vereist dat rapporteringsverantwoordelijkheden onder 
de ISA’s worden opgenomen onder een kopje met de titel “Verklaring betreffende de controle van 
de financiële overzichten”. 
 
Naam van de opdrachtpartner (Zie par. 46) 
 
A61.  De doelstelling van het kantoor bepaald in ISQM 136 is het opzetten, implementeren en in werking 
stellen van een kwaliteitsmanagementsysteem dat aan het kantoor een redelijke mate van 
zekerheid verschaft dat:  
 
• 
het kantoor en zijn personeel hun verantwoordelijkheden vervullen in overeenstemming 
met professionele standaarden en met van toepassing zijnde vereisten uit wet- en 
regelgeving, en opdrachten uitvoeren in overeenstemming met deze standaarden en 
vereisten; en  
• 
de door het kantoor of de opdrachtpartners uitgebrachte opdrachtrapporten in de gegeven 
omstandigheden passend zijn. 
 
 Niettegenstaande de doelstelling van ISQM 1, is het benoemen van de opdrachtpartner in de 
controleverklaring bedoeld om meer transparantie te verschaffen aan de gebruikers van de 
controleverklaring van een complete serie van financiële overzichten voor algemene doeleinden 
van een beursgenoteerde entiteit. 
 
A62. Op grond van wet- of regelgeving of nationale controlestandaarden kan zijn vereist dat de 
controleverklaring de naam van de opdrachtpartner bevat die verantwoordelijk is voor controles 
anders dan die van volledige sets financiële overzichten voor algemene doeleinden van 
beursgenoteerde entiteiten. Van de auditor kan tevens zijn vereist op grond van wet- of 
regelgeving of nationale controle-standaarden, of kan hij besluiten om in de controleverklaring 
aanvullende informatie op te nemen naast de naam van de opdrachtpartner om de 
opdrachtpartner beter te identificeren, bijvoorbeeld het nummer van zijn vergunning die relevant 
is voor het rechtsgebied waar de auditor werkzaam is. 
 
A63. In zeldzame omstandigheden kan de auditor informatie identificeren of kan hij onderhevig zijn 
aan ervaringen die een indicatie zijn voor de waarschijnlijkheid van een bedreiging voor de 
persoonlijke veiligheid die, indien de identiteit van de opdrachtpartner openbaar wordt gemaakt, 
kan resulteren in fysieke schade aan de opdrachtpartner, overige leden van het opdrachtteam of 
andere nauw betrokken personen. Een dergelijke bedreiging omvat echter bijvoorbeeld geen 
bedreigingen van juridische aansprakelijkheid of juridische, regelgevende of professionele 
sancties. Besprekingen met de met governance belaste personen over omstandigheden die 
kunnen resulteren in fysieke schade kunnen aanvullende informatie verschaffen over de 
waarschijnlijkheid of ernst van de significante bedreiging voor de persoonlijke veiligheid. Wet- of 
regelgeving of nationale controlestandaarden kunnen verdere vereisten vaststellen die relevant 
zijn voor het bepalen van wanneer de openbaarmaking van de naam van de opdrachtpartner kan 
worden weggelaten. 
 
Handtekening van de auditor (Zie par. 47) 
 
 
36  ISQM 1, Kwaliteitsmanagement voor kantoren die controles of beoordelingen van financiële overzichten, of andere assurance 
opdrachten of opdrachten voor aan assurance verwante diensten uitvoeren, paragraaf 14.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 29/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
A64. De handtekening van de auditor wordt geplaatst hetzij in naam van het auditkantoor, in 
persoonlijke naam van de auditor, hetzij beide, naargelang passend voor het specifieke 
rechtsgebied. Naast de handtekening van de auditor, kan in bepaalde rechtsgebieden van de 
auditor worden vereist om in de controleverklaring zijn professionele accountancy-titel te 
vermelden dan wel het feit te vermelden dat de auditor of het kantoor, naargelang passend, 
erkend is door de passende instantie die in dat rechtsgebied de vergunningen verstrekt. 
 
A65. In sommige gevallen staat wet- of regelgeving het gebruik van een elektronische handtekening 
in de controleverklaring toe. 
 
Datum van de controleverklaring (Zie par. 49) 
 
A66. De datum van de controleverklaring informeert de gebruikers van de controleverklaring dat de 
auditor rekening heeft gehouden met de effecten van gebeurtenissen en transacties waarvan hij 
kennis heeft gekregen en die tot op die datum hebben plaatsgevonden. De verantwoordelijkheid 
van de auditor voor gebeurtenissen en transacties na de datum van de controleverklaring wordt 
behandeld in ISA 560.37 
 
A67. Omdat het oordeel van de accountant betrekking heeft op de financiële overzichten en de 
financiële overzichten onder de verantwoordelijkheid van het management vallen, is de 
accountant niet in een positie om te concluderen dat voldoende en geschikte controle-informatie 
is verkregen totdat informatie is verkregen die aantoont dat alle overzichten en toelichtingen die 
samen de financiële overzichten vormen de daarmee verband houdende toelichtingen, zijn 
opgesteld en het management de verantwoordelijkheid daarvoor heeft aanvaard. 
 
A68. In sommige rechtsgebieden wijst wet- of regelgeving de personen of 
instanties (bijv. de 
bestuurders) aan die verantwoordelijk zijn voor het concluderen dat alle overzichten en 
toelichtingen die samen de financiële overzichten vormen, zijn opgesteld, en specificeert de wet- 
of regelgeving het noodzakelijke goedkeuringsproces. In dergelijke gevallen wordt informatie 
verkregen die deze goedkeuring vόόr het dateren van de verklaring over de financiële overzichten 
aantoont. In andere rechtsgebieden wordt het goedkeuringsproces evenwel niet voorgeschreven 
in wet- of regelgeving. In dergelijke gevallen wordt overwogen welke procedures de entiteit volgt 
bij het opstellen en finaliseren van haar financiële overzichten in het licht van haar management- 
en governancestructuren, om te bepalen welke personen of welke instantie bevoegd is om te 
concluderen dat alle overzichten die samen de financiële overzichten vormen, met inbegrip van 
de daarmee verband houdende toelichtingen, zijn opgesteld. In sommige gevallen specificeert de 
wet- of regelgeving op welk moment in het proces 
van verslaggeving over de financiële 
overzichten de controle geacht wordt te zijn afgerond. 
 
A69. In sommige rechtsgebieden is de finale goedkeuring van de financiële overzichten door de 
aandeelhouders vereist alvorens de financiële overzichten op publieke wijze bekend worden 
gemaakt. In deze rechtsgebieden is de finale goedkeuring door aandeelhouders niet noodzakelijk 
voor de accountant om te concluderen dat voldoende en geschikte controle-informatie is 
verkregen. De goedkeuringsdatum van de financiële overzichten in het kader van ISA’s is de 
eerdere datum waarop de personen met de erkende bevoegdheid bepalen dat alle overzichten en 
toelichtingen waaruit de financiële overzichten bestaan, zijn opgesteld en dat de personen met de 
erkende bevoegdheid hebben verklaard dat zij daarvoor verantwoordelijk zijn. 
 
Controleverklaring voorgeschreven door wet- of regelgeving (Zie par. 50) 
 
A70. In ISA 200 wordt uiteengezet dat van de auditor mogelijk vereist wordt dat hij naast de ISA’s ook 
de door wet- of regelgever gestelde vereisten naleeft.38 Indien de verschillen tussen de door de 
wet- of regelgever gestelde vereisten en de ISA’s alleen betrekking hebben op de opmaak en 
formulering van de controleverklaring zetten de vereisten in paragraaf 50(a)-(o) het minimale 
aantal elementen uiteen die in de controleverklaring zijn opgenomen om een verwijzing mogelijk 
 
37  ISA 560, Gebeurtenissen na de einddatum van de verslagperiode, paragrafen 10-17. 
38  ISA 200, paragraaf A60.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 30/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
te maken naar de International Standards on Auditing In dergelijke omstandigheden hoeven de 
vereisten uit paragrafen 21-49 die niet zijn opgenomen in paragraaf 50(a)-(o) niet te worden 
toegepast, inclusief bijvoorbeeld de vereiste volgorde van de secties Oordeel en Basis voor het 
oordeel. 
 
A71. Indien specifieke vereisten gesteld in een bepaald rechtsgebied niet in strijd zijn met de ISA’s, 
draagt de in deze ISA gebruikte opmaak en formulering die vereist is op grond van paragraaf 21-
49 ertoe bij dat de gebruikers van de controleverklaring de controleverklaring gemakkelijker 
herkennen als een verklaring over een controle die overeenkomstig de ISA’s is uitgevoerd. 
  
Informatie die op grond van ISA 701 vereist is (Zie par. 50(h)) 
 
A72. Op grond van wet- of regelgeving kan van de auditor zijn vereist om aanvullende informatie te 
verschaffen over de controle die is uitgevoerd, welke informatie kan bevatten die consistent is 
met de doelstellingen van ISA 701 of die de aard en omvang van communicatie over dergelijke 
aangelegenheden kan voorschrijven. 
 
A73. De ISA’s doen geen afbreuk aan wet- of regelgeving die een controle van de financiële 
overzichten regelt. Als ISA 701 van toepassing is, kan er in de controleverklaring alleen een 
verwijzing worden gemaakt naar de ISA’s wanneer, bij het toepassen van wet- of regelgeving, de 
sectie die op grond van paragraaf 50(h) van deze ISA vereist is, niet strijdig is met de 
rapporteringsvereisten van ISA 701. In dergelijke omstandigheden kan het nodig zijn dat de 
auditor bepaalde aspecten van de communicatie over kernpunten van de controle in de 
controleverklaring zoals vereist op grond van ISA 701 specifiek maakt door bijvoorbeeld: 
 
• 
De titel “Kernpunten van de controle” aan te passen indien wet- of regelgeving een 
specifieke titel voorschrijft; 
• 
Uit te leggen waarom de informatie die op grond van wet- of regelgeving is vereist in de 
controleverklaring wordt verschaft, bijvoorbeeld door een verwijzing te maken naar de 
relevante wet- of regelgeving en te beschrijven hoe die informatie verband houdt met de 
kernpunten van de controle; 
• 
Waar wet- of regelgeving de aard en omvang van de beschrijving voorschrijft, de 
voorgeschreven informatie aan te vullen om een algehele beschrijving van elk kernpunt 
van de controle te bewerkstelligen die consistent is met het vereiste uit paragraaf 13 van 
ISA 701. 
 
A74. In ISA 210 behandelt omstandigheden waar wet- of regelgeving van het desbetreffende 
rechtsgebied in bepaalde gevallen de opmaak of formuleringen van de controleverklaring  
voorschrijft gebruikmakend van termen die op significante wijze verschillen van de vereisten van 
de ISA’s, die in het bijzonder het oordeel van de auditor omvat. In dat geval is op grond van ISA 
210 vereist dat de auditor evalueert: 
 
(a) 
Of de gebruikers de mate van zekerheid die uit de controle van de financiële overzichten 
wordt verkregen, verkeerd zouden kunnen interpreteren en, indien dit het geval is; 
(b) 
Of aanvullende uitleg in de controleverklaring de kans op een verkeerd begrip kan 
verkleinen. 
 
Indien de auditor tot de conclusie komt dat aanvullende uitleg in de controleverklaring de kans op 
een verkeerd begrip niet kan verkleinen, is op grond van ISA 210 vereist dat de auditor de 
controleopdracht niet aanvaardt, tenzij hij hiertoe op grond van wet- of regelgeving verplicht is. 
Overeenkomstig ISA 210 voldoet een overeenkomstig dergelijke wet- of regelgeving uitgevoerde 
controle niet aan de ISA’s. Bijgevolg neemt de auditor in de controleverklaring geen enkele 
verwijzing op naar het feit dat de controle overeenkomstig de International Standards on Auditing 
is uitgevoerd.39 
 
 
39  ISA 210, paragraaf 21.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 31/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Overwegingen specifiek voor entiteiten in de publieke sector 
 
A75. 
Auditor van entiteiten in de publieke sector kunnen tevens over de mogelijkheid beschikken om 
op grond van wet- of regelgeving publiekelijk te rapporteren over bepaalde aangelegenheden, 
hetzij in de controleverklaring of in een aanvullend rapport, welke informatie kan bevatten die 
consistent is met de doelstellingen van ISA 701. In dergelijke omstandigheden kan het nodig 
zijn dat de auditor bepaalde aspecten van de communicatie over kernpunten van de controle in 
de controleverklaring die is vereist op grond van ISA 701 specifiek maakt of een verwijzing in 
de controleverklaring opneemt naar een beschrijving van de aangelegenheid in het aanvullende 
rapport. 
 
Controleverklaring voor controles uitgevoerd overeenkomstig zowel controlestandaarden van een 
specifiek rechtsgebied als de International Standards on Auditing (Zie par. 51) 
 
A76. De auditor kan in de controleverklaring verwijzen naar het feit dat de controle is uitgevoerd 
overeenkomstig zowel de International Standards on Auditing als de andere controlestandaarden 
indien de auditor naast de relevante nationale controlestandaarden ook elk van de voor de 
controle relevante ISA’s naleeft.40 
 
A77. Een verwijzing naar zowel de International Standards on Auditing als de andere 
controlestandaarden is niet passend als er een conflict is tussen de vereisten in de ISA’s en die 
in de andere controlestandaarden dat de auditor ertoe zou brengen een ander oordeel te vormen 
of een paragraaf ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden niet op te nemen die in de gegeven omstandigheden door de ISA’s vereist is. 
In een dergelijk geval verwijst de controleverklaring alleen naar de controlestandaarden (hetzij de 
International Standards on Auditing, hetzij de andere controlestandaarden) overeenkomstig 
welke de controleverklaring is opgesteld. 
 
Aanvullende informatie gepresenteerd bij de financiële overzichten (Zie par. 53-54) 
 
A78. In bepaalde omstandigheden is het mogelijk dat de entiteit op grond van wet- of regelgeving of 
standaarden verplicht is of vrijwillig kan kiezen om samen met de financiële overzichten 
aanvullende informatie te presenteren die niet door het van toepassing zijnde stelsel inzake 
financiële verslaggeving is vereist. Zo is het mogelijk dat aanvullende informatie wordt 
gepresenteerd om de gebruikers meer inzicht te verschaffen in het van toepassing zijnde stelsel 
inzake financiële verslaggeving of om nadere uitleg te geven over specifieke elementen van de 
financiële overzichten. Dergelijke informatie wordt gewoonlijk gepresenteerd in aanvullende 
bijlagen of als aanvullende toelichtingen. 
 
A79. In paragraaf 53 van deze ISA wordt uitgelegd dat het oordeel van de auditor aanvullende 
informatie die een integrerend onderdeel is van de financiële overzichten bevat vanwege diens 
aard of de manier waarop dit is weergegeven. Deze evaluatie is een kwestie van professionele 
oordeelsvorming. Als voorbeeld: 
 
• 
Als de toelichtingen op de financiële overzichten een uitleg of de aansluiting bevatten van 
de mate waarin de financiële overzichten in overeenstemming zijn met een ander stelsel 
inzake financiële verslaggeving, kan de auditor dit als aanvullende informatie beschouwen 
die niet duidelijk onderscheiden kan worden van de financiële overzichten. Het oordeel van 
de auditor zou tevens toelichtingen of aanvullende bijlagen omvatten waarnaar in de 
financiële overzichten wordt verwezen; 
• 
Wanneer een aanvullende winst- en verliesrekening die specifieke uitgavenposten toelicht, 
wordt toegelicht als een aparte bijlage die in een bijlage voor de financiële overzichten is 
opgenomen, kan de auditor het noodzakelijk achten om dit als aanvullende informatie te 
beschouwen die duidelijk onderscheiden kan worden van de financiële overzichten. 
 
 
40  ISA 200, paragraaf A61.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 32/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
A80. In de controleverklaring hoeft niet specifiek te worden verwezen naar de aanvullende informatie 
die door het oordeel van de auditor is omvat indien de in de inleidende paragraaf opgenomen 
verwijzing naar de toelichtingen in de beschrijving van de overzichten die samen de financiële 
overzichten vormen, volstaat het rapport van de auditor. 
 
A81. Het is mogelijk dat wet- of regelgeving niet vereist dat de aanvullende informatie wordt 
gecontroleerd, en het management kan besluiten de auditor niet te vragen de aanvullende 
informatie op te nemen in de reikwijdte van de controle van de financiële overzichten. 
 
A82. De evaluatie door de auditor van de vraag of niet-gecontroleerde aanvullende informatie is 
gepresenteerd op een wijze die zou kunnen worden opgevat als zijnde omvat door het oordeel 
van de auditor omvat bijvoorbeeld de vraag waar die informatie is gepresenteerd in relatie tot de 
financiële overzichten en eventuele gecontroleerde aanvullende informatie en of ze op duidelijke 
wijze als “niet-gecontroleerd” is aangeduid. 
 
A83. Het management zou de presentatie van niet-gecontroleerde aanvullende informatie die zou 
kunnen worden opgevat als zijnde omvat door het oordeel van de auditor, kunnen wijzigen, 
bijvoorbeeld door: 
 
• 
Eventuele verwijzingen vanuit de financiële overzichten naar niet-gecontroleerde 
aanvullende bijlagen of niet-gecontroleerde toelichtingen te verwijderen, zodat de 
scheiding tussen de gecontroleerde en de niet-gecontroleerde informatie voldoende 
duidelijk is; 
• 
De niet-gecontroleerde aanvullende informatie buiten de financiële overzichten te plaatsen 
of, indien dat in de gegeven omstandigheden niet mogelijk is, ten minste de niet-
gecontroleerde toelichtingen aan het einde van de vereiste toelichtingen op de financiële 
overzichten te plaatsen en duidelijk aan te geven dat zij niet gecontroleerd zijn. Niet-
gecontroleerde toelichtingen die tussen de gecontroleerde toelichtingen worden gevoegd, 
kunnen verkeerd worden geïnterpreteerd als zijnde gecontroleerd. 
 
A84. Het feit dat aanvullende informatie niet gecontroleerd is, ontheft de auditor niet van zijn 
verantwoordelijkheden die in ISA 720 (herzien) zijn beschreven.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 33/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Bijlage 
(Zie par. A19) 
Voorbeelden 
van 
onafhankelijke 
controleverklaringen 
over 
financiële 
overzichten (*) 
 
• 
Voorbeeld 1:  
Een controleverklaring over financiële overzichten van een beursgenoteerde 
entiteit opgesteld in overeenstemming met een getrouw-beeld-stelsel.  
• 
Voorbeeld 2:  
Een controleverklaring over geconsolideerde financiële overzichten van een 
beursgenoteerde entiteit opgesteld in overeenstemming met een getrouw-beeld-stelsel. 
• 
Voorbeeld 3:  
Een controleverklaring over financiële overzichten van een entiteit anders dan 
een beursgenoteerde entiteit opgesteld in overeenstemming met een getrouw-beeld-stelsel (waar 
referentie werd gemaakt aan zaken die op een website te vinden zijn of aan een bevoegde 
instantie). 
• 
Voorbeeld 4:  
Een controleverklaring over financiële overzichten van een entiteit, anders dan 
a beursgenoteerde entiteit, opgesteld in overeenstemming met een compliance-stelsel voor 
algemene doeleinden. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(*) Gezien het groot aantal wijzigingen aan de voorbeelden van controleverklaringen, werden deze niet 
aangeduid in het grijs in de hiernavolgende teksten.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 34/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 1 – Controleverklaring over financiële overzichten van een beursgenoteerde 
entiteit opgesteld in overeenstemming met een getrouw-beeld-stelsel 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen:  
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit 
waarbij gebruik wordt gemaakt van a getrouw-beeld-stelsel. De controle is geen groepscontrole 
(i.e., ISA 600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in 
ISA 210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is 
op basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle omvatten de Code of 
Ethics for Professional Accountants van de International Ethics Standards Board for 
Accountants samen met de ethische vereisten die verband houden met de controle in het 
rechtsgebied, en de auditor verwijst naar beide; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit 
om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en 
heeft geen afwijking van materieel belang in de andere informatie vastgesteld; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de 
met het opstellen van de financiële overzichten belaste personen; 
• 
Naast 
de 
controle 
van 
de 
financiële 
overzichten 
heeft 
de 
auditor 
overige 
rapporteringsverplichtingen op grond van lokale wetgeving.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 35/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de financiële overzichten41 
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
onze verklaring.Wij zijn onafhankelijk van de Vennootschap in overeensteming met de Code of Ethics 
for Professional Accountants van de International Ethics Standards Board for Accountants (IESBA 
Code) en met de ethische vereisten die relevant zijn voor de controle van de financiële overzichten in 
[rechtsgebied], en we hebben onze overige ethische verantwoordelijkheden nageleefd in 
overeenstemming met deze vereisten en de IESBA Code. Wij zijn van mening dat de door ons verkregen 
controle-informatie voldoende en geschikt is als basis voor ons oordeel. 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701.] 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 1 in bijlage 2 van ISA 720 (herzien)] 
 
41  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. )

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 36/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen42 
Het management is verantwoordelijk voor het opstellen en getrouw weergeven van de financiële 
overzichten 
in 
overeenstemming 
met 
IFRS43 
en 
voor 
de 
interne 
beheersing 
die 
het 
management noodzakelijk acht om het opstellen mogelijk te maken van financiële overzichten die geen 
afwijking van materieel belang bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de Vennootschap om haar continuïteit te handhaven, het toelichten, indien van 
toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de Vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
proces van financiële verslaggeving van de Vennootschap. 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijking van materieel belang bevatten die het gevolg is van 
fraude of van fouten; en het uitbrengen van een controleverklaring waarin ons oordeel is opgenomen. 
Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie dat een 
controle die overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang ontdekt 
wanneer die bestaat. Afwijkingen kunnen zich voordoen als gevolg van fraude of fouten en worden als 
van materieel belang beschouwd indien redelijkerwijs kan worden verwacht dat zij, individueel of 
gezamenlijk, de economische beslissingen genomen door gebruikers op basis van deze financiële 
overzichten, beïnvloeden.  
Paragraaf 41(b) van deze ISA legt uit dat de in schaduw hieronder voorgestelde tekst kan worden opgenomen in een Bijlage tot 
de controleverklaring. Paragraaf 41(c) legt uit dat wanneer wet- of regelgeving of nationale controlestandaarden op expliciete 
wijze dit toelaten, referentie kan worden gemaakt aan een website van een bevoegde autoriteit die de beschrijving van de 
verantwoordelijkheden van de auditor bevat, eerder dan deze tekst in de controleverklaring op te nemen, op voorwaarde dat de 
beschrijving op de website de beschrijving van de verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en 
hiermee niet inconsistent is.  
 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. We 
voeren tevens de volgende werkzaamheden uit: 
• 
het identificeren en inschatten van de risico’s dat de financiële overzichten een afwijking van 
materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en uitvoeren van 
controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van controle-informatie 
die voldoende en geschikt is als basis voor ons oordeel. Het risico van het niet detecteren van 
een van materieel belang zijnde afwijking is groter indien die afwijking het gevolg is van fraude 
dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn van samenspanning, 
valsheid in geschrifte, het opzettelijk nalaten om transacties vast te leggen, het opzettelijk 
verkeerd voorstellen van zaken of het doorbreken van de interne beheersing; 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle, met als doel 
controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn maar die 
 
42  In deze voorbeelden van controleverklaringen kunnen de termen ‘management’ en ‘de met governance belaste personen’ 
worden vervangen door andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke 
rechtsgebied.  
43  Waar het de verantwoordelijkheid is van het management om financiële overzichten op te stellen die een getrouw beeld 
geven, kan dit als volgt luiden: “Management is verantwoordelijk voor het opstellen van de financiële overzichten die een 
getrouw beeld geven in overeenstemming met International Financial Reporting Standards, en voor een (…)”.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 37/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne beheersing van 
de entiteit44; 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen; 
• 
het concluderen of de door de management gehanteerde continuïteitsveronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, of er een 
onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of omstandigheden 
die significante twijfel kunnen doen ontstaan over de mogelijkheid van de Vennootschap om haar 
continuïteit te handhaven. Indien wij concluderen dat er een onzekerheid van materieel belang 
bestaat, zijn wij ertoe gehouden om de aandacht in onze controleverklaring te vestigen op de 
daarop betrekking hebbende toelichtingen in de financiële overzichten, of, indien deze 
toelichtingen inadequaat zijn, om ons oordeel aan te passen. Onze conclusies zijn gebaseerd op 
de controle-informatie die verkregen is tot de datum van onze controleverklaring. Toekomstige 
gebeurtenissen of omstandigheden kunnen er echter toe leiden dat de Vennootschap haar 
continuïteit niet langer kan handhaven; 
• 
het evalueren van de algehele presentatie, structuur en inhoud van de financiële overzichten, met 
inbegrip van de daarin opgenomen toelichtingen, en van de vraag of de financiële overzichten de 
onderliggende transacties en gebeurtenissen weergeven op een wijze die leidt tot een getrouw 
beeld. 
 
Wij communiceren met de met governance belaste personen, onder meer over de geplande reikwijdte 
en timing van de controle en over de significante controlebevindingen, waaronder eventuele significante 
tekortkomingen in de interne beheersing die wij identificeren gedurende onze controle.  
Wij verschaffen aan de met governane belaste personen een statement dat wij de relevante ethische 
voorschriften over onafhankelijkheid hebben nageleefd. Wij communiceren met deze personen 
tevens over alle relaties en andere zaken die redelijkerwijs onze onafhankelijkheid kunnen beïnvloeden 
en, waar van toepassing, over de daarmee verband houdende maatregelen om onze onafhankelijkheid 
te waarborgen. 
Uit de aangelegenheden die met de met governance belaste personen zijn gecommuniceerd bepalen 
wij die zaken die het meest significant waren bij de controle van de financiële overzichten van de huidige 
verslagperiode, en die derhalve de kernpunten van onze controle uitmaken. Wij beschrijven deze 
aangelegenheden in onze controleverklaring, tenzij het openbaar maken van deze aangelegenheden 
is verboden door wet- of regelgeving of, in buitengewoon zeldzame omstandigheden, tenzij wij bepalen 
dat een aangelegenheid niet in onze verklaring moet worden opgenomen omwille van het feit dat de 
negatieve gevolgen van dergelijke communicatie redelijkerwijs worden verwacht groter te zijn dan de 
voordelen voor het maatschappelijk verkeer. 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[De vorm en inhoud van deze sectie van de controleverklaring varieert in functie van de aard van de 
overige rapporteringsverplichtingen van de auditor zoals voorgeschreven door de lokale wet-of 
regelgeving, of door nationale controlestandaarden. De aangelegenheden behandeld door andere wet- 
or regelgeving of door nationale controlestandaarden (aangeduid met de term “overige 
rapporteringsverplichtingen”) dienen in deze sectie te worden behandeld, tenzij de overige 
rapporteringsverplichtingen dezelfde topics behandelen als diegene gepresenteerd onder de 
rapporteringsverplichtingen die door de ISA’s vereist zijn als onderdeel van de sectie “Verklaring over 
de controle van de financiële overzichten”. 
De verslaggeving betreffende de overige 
 
44  Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
financiële overzichten.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 38/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
rapporteringsverplichtingen die dezelfde topics behandelen als diegene die door de ISA’s zijn vereist, 
kan worden gecombineerd (i.e., ondergebracht in de sectie “Verklaring over de controle van de 
financiële overzichten” onder de passende subtitel), voorgenomen dat er in de bewoordingen van de 
controleverklaring 
een 
duidelijk 
onderscheid 
wordt 
gemaakt 
tussen 
de 
overige 
rapporteringsverplichtingen en de verslaggeving die door de ISA’s vereist is, indien een dergelijk 
verschil zich voordoet.] 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum]

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 39/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 2 – Een controleverklaring over geconsolideerde financiële overzichten van 
een beursgenoteerde entiteit opgesteld in overeenstemming met een getrouw-beeld-
stelsel 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen:  
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een 
beursgenoteerde entiteit waarbij gebruik wordt gemaakt van a getrouw-beeld-stelsel. De 
controle is groepscontrole van een entiteit met dochtermaatschappijen (i.e., ISA 600 is van 
toepassing);  
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de 
entiteit in overeenstemming met IFRS (een stelsel voor algemene doeleinden);  
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten 
zoals opgenomen in ISA 210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is 
op basis van de verkregen controle-informatie; 
• 
De Code of Ethics for Professional Accountants van de International Ethics Standards Board 
for Accountants omvat alle relevante ethische vereisten die van toepassing zijn op de 
controle; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen 
van materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de 
entiteit om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en 
heeft geen afwijking van materieel belang in de andere informatie vastgesteld; 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen; 
• 
Naast de controle van de geconsolideerde financiële overzichten heeft de auditor overige 
rapporteringsverplichtingen op grond van lokale wetgeving.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 40/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de geconsolideerde financiële overzichten45 
Oordeel 
Wij hebben de geconsolideerde financiële overzichten van vennootschap ABC en haar 
dochtermaatschappijen (de Groep) gecontroleerd, die bestaan uit het geconsolideerd overzicht van 
de financiële positie op 31 december 20X1, het geconsolideerde overzicht van gerealiseerde en niet-
gerealiseerde resultaten, het geconsolideerde mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip 
van een overzicht van de belangrijke grondslagen voor financiële verslaggeving.  
Naar ons oordeel vormen de bijhorende geconsolideerde financiële overzichten in alle van materieel 
belang zijnde opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de 
geconsolideerde financiële positie van de Groep per 31 december 20X1, en van haar geconsolideerde 
financiële prestaties en kasstromen voor het op die datum afgesloten boekjaar, in overeenstemming 
met International Financial Reporting Standards (IFRS). 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISAs). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de geconsolideerde financiële 
overzichten' van onze verklaring.Wij zijn onafhankelijk van de Vennootschap in overeensteming met de 
Code of Ethics for Professional Accountants van de International Ethics Standards Board for 
Accountants (IESBA Code), en we hebben onze overige ethische verantwoordelijkheden nageleefd in 
overeenstemming met de IESBA Code. Wij zijn van mening dat de door ons verkregen controle-
informatie voldoende en geschikt is als basis voor ons oordeel. 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de geconsolideerde financiële overzichten van de huidige 
verslagperiode. Deze aangelegenheden zijn behandeld in de context van onze controle van de 
geconsolideerde financiële overzichten als geheel en bij het vormen van ons oordeel hierover, en wij 
verschaffen geen afzonderlijk oordeel over deze aangelegenheden. 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701.] 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 1 in bijlage 2 van ISA 720 (herzien)] 
 
45  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 41/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen46 
Het management is verantwoordelijk voor het opstellen en getrouw weergeven van de geconsolideerde 
financiële overzichten in overeenstemming met IFRS47 en voor de interne beheersing die het 
management noodzakelijk acht om het opstellen mogelijk te maken van geconsolideerde financiële 
overzichten die geen afwijking van materieel belang bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de geconsolideerde financiële overzichten is het management verantwoordelijk 
voor het inschatten van de mogelijkheid van de Vennootschap om haar continuïteit te handhaven, het 
toelichten, indien van toepassing, van aangelegenheden die met continuïteit verband houden en het 
gebruiken van de continuïteitsveronderstelling, tenzij het management het voornemen heeft om de 
Vennootschap te liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief 
heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
proces van financiële verslaggeving van de Vennootschap. 
Verantwoordelijkheden van de auditor voor de controle van de geconsolideerde financiële 
overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
geconsolideerde financiële overzichten als geheel geen afwijking van materieel belang bevatten die het 
gevolg is van fraude of van fouten; en het uitbrengen van een controleverklaring waarin ons oordeel is 
opgenomen. Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie 
dat een controle die overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang 
ontdekt wanneer die bestaat. Afwijkingen kunnen zich voordoen als gevolg van fraude of fouten en 
worden als van materieel belang beschouwd indien redelijkerwijs kan worden verwacht dat zij, 
individueel of gezamenlijk, de economische beslissingen genomen door gebruikers op basis van deze 
geconsolideerde financiële overzichten, beïnvloeden. 
Paragraaf 41(b) van deze ISA legt uit dat hieronder voorgestelde gemarkeerde tekst kan worden opgenomen in een Bijlage tot 
de controleverklaring. Paragraaf 41(c) legt uit dat wanneer wet- of regelgeving of nationale controlestandaarden op expliciete 
wijze dit toelaten, referentie kan worden gemaakt aan een website van een bevoegde autoriteit die de beschrijving van de 
verantwoordelijkheden van de auditor bevat, eerder dan deze tekst in de controleverklaring op te nemen, op voorwaarde dat de 
beschrijving op de website de beschrijving van de verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en 
hiermee niet inconsistent is. 
 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. We 
voeren tevens de volgende werkzaamheden uit:  
 
• 
het identificeren en inschatten van de risico’s dat de geconsolideerde financiële overzichten een 
afwijking van materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en 
uitvoeren van controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van 
controle-informatie die voldoende en geschikt is als basis voor ons oordeel. Het risico van het 
niet detecteren van een van materieel belang zijnde afwijking is groter indien die afwijking het 
gevolg is van fraude dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn van 
samenspanning, valsheid in geschrifte, het opzettelijk nalaten om transacties vast te leggen, het 
opzettelijk verkeerd voorstellen van zaken of het doorbreken van de interne beheersing; 
 
46  Of andere wettelijke bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
47  Waar het de verantwoordelijkheid is van het management om geconsolideerde financiële overzichten op te stellen die een 
getrouw beeld geven, kan dit als volgt luiden: “Management is verantwoordelijk voor het opstellen van de geconsolideerde 
financiële overzichten die een getrouw beeld geven in overeenstemming met International Financial Reporting Standards, en 
voor een (...)”.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 42/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle met als doel 
controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn maar die 
niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne beheersing van 
de Groep48; 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen; 
• 
het concluderen dat de door de management gehanteerde continuïteitsveronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, dat er een 
onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of omstandigheden 
die significante twijfel kunnen doen ontstaan over de mogelijkheid van de Groep om zijn 
continuïteit te handhaven. Indien wij concluderen dat er een onzekerheid van materieel belang 
bestaat, zijn wij ertoe gehouden om de aandacht in onze controleverklaring te vestigen op de 
daarop betrekking hebbende toelichtingen in de geconsolideerde financiële overzichten, of, 
indien deze toelichtingen inadequaat zijn, om ons oordeel aan te passen. Onze conclusies zijn 
gebaseerd op de controle-informatie die verkregen is tot de datum van onze controleverklaring. 
Toekomstige gebeurtenissen of omstandigheden kunnen er echter toe leiden dat de Groep zijn 
continuïteit niet langer kan handhaven; 
• 
het evalueren van de algehele presentatie, structuur en inhoud van de geconsolideerde financiële 
overzichten, met inbegrip van de daarin opgenomen toelichtingen, en van de vraag of de 
geconsolideerde financiële overzichten de onderliggende transacties en gebeurtenissen 
weergeven op een wijze die leidt tot een getrouw beeld; 
• 
Het verkrijgen van voldoende en geschikte controle-informatie met betrekking tot de financiële 
informatie van de entiteiten of bedrijfsactiviteiten binnen de Groep gericht op het tot uitdrukking 
brengen van een oordeel over de geconsolideerde financiële overzichten. Wij zijn 
verantwoordelijk voor de aansturing van, het toezicht op en de uitvoering van de groepscontrole. 
Wij blijven ongedeeld verantwoordelijk voor ons oordeel. 
 
Wij communiceren met de met governance belaste personen, onder meer over de geplande reikwijdte 
en timing van de controle en over de significante controlebevindingen, waaronder eventuele significante 
tekortkomingen in de interne beheersing die wij identificeren gedurende onze controle.  
 
Wij verschaffen aan de met governane belaste personen tevens een statement dat wij de relevante 
ethische voorschriften over onafhankelijkheid hebben nageleefd, en wij communiceren met deze 
personen over alle relaties en andere zaken die redelijkerwijs onze onafhankelijkheid kunnen 
beïnvloeden en, waar van toepassing, over de daarmee verband houdende maatregelen om onze 
onafhankelijkheid te waarborgen. 
 
Uit de aangelegenheden die met de met governance belaste personen zijn gecommuniceerd bepalen wij 
die zaken die het meest significant waren bij de controle van de financiële overzichten van de huidige 
verslagperiode, en die derhalve de kernpunten van onze controle uitmaken. Wij beschrijven deze 
aangelegenheden in onze controleverklaring, tenzij het openbaar  maken van deze aangelegenheden is 
verboden door wet- of regelgeving of, in buitengewoon zeldzame omstandigheden, tenzij wij bepalen dat 
een aangelegenheid niet in onze verklaring moet worden opgenomen omwille van het feit dat de 
negatieve gevolgen van dergelijke communicatie redelijkerwijs worden verwacht groter te zijn dan de 
voordelen voor het maatschappelijk verkeer. 
 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[De vorm en inhoud van deze sectie van de controleverklaring varieert in functie van de aard van de 
overige rapporteringsverplichtingen van de auditor zoals voorgeschreven door de lokale wet-of 
regelgeving, of door nationale controlestandaarden. De aangelegenheden behandeld door andere wet- 
or regelgeving of door nationale controlestandaarden (aangeduid met de term “overige 
 
48  Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
geconsolideerde financiële overzichten.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 43/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
rapporteringsverplichtingen”) dienen in deze sectie te worden behandeld, tenzij de overige 
rapporteringsverplichtingen dezelfde topics behandelen als diegene gepresenteerd onder de 
rapporteringsverplichtingen die door de ISA’s vereist zijn als onderdeel van de sectie “Verklaring over 
de controle van de geconsolideerde financiële overzichten”. De verslaggeving betreffende de overige 
rapporteringsverplichtingen die dezelfde topics behandelen als diegene die door de ISA’s zijn vereist, 
kan worden gecombineerd (i.e., ondergebracht in de sectie “Verklaring over de controle van de 
geconsolideerde financiële overzichten” onder de passende subtitel), voorgenomen dat er in de 
bewoordingen van de controleverklaring een duidelijk onderscheid wordt gemaakt tussen de overige 
rapporteringsverplichtingen en de verslaggeving die door de ISA’s vereist is, indien een dergelijk verschil 
zich voordoet. 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum]

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 44/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 3 – Een controleverklaring over financiële overzichten van een entiteit anders 
dan een beursgenoteerde entiteit opgesteld in overeenstemming met een getrouw-
beeld-stelsel 
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen: 
• 
Controle van een volledige set van financiële overzichten van een entiteit, anders dan een 
beursgenoteerde entiteit, waarbij gebruik wordt gemaakt van a getrouw-beeld-stelsel. De 
controle is geen groepscontrole (i.e., ISA 600 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in 
ISA 210; 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is 
op basis van de verkregen controle-informatie; 
• 
De relevante ethische vereisten die van toepassing zijn op de controle zijn diegene die verband 
houden met de controle in het rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit 
om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
De auditor heeft geen verplichting tot, en heeft beslist om niet over te gaan tot, het 
communiceren van kernpunten van de controle overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en 
heeft geen afwijking van materieel belang in de andere informatie vastgesteld; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de 
met het opstellen van de financiële overzichten belaste personen; 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wetgeving; 
• 
De auditor kiest ervoor om te refereren aan de beschrijving van de verantwoordelijkheid van 
de auditor zoals opgenomen op een website van een bevoegde instantie.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 45/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
Naar ons oordeel vormen de financiële overzichten in alle van materieel belang zijnde opzichten een 
getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie van de 
vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor het op die 
datum afgesloten boekjaar, in overeenstemming met International Financial Reporting Standards 
(IFRS).  
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
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 1 in bijlage 2 van ISA 720 (herzien)] 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen49 
Het management is verantwoordelijk voor het opstellen en getrouw weergeven van de financiële 
overzichten in overeenstemming met IFRS50 en voor de interne beheersing die het 
management noodzakelijk acht om het opstellen mogelijk te maken van financiële overzichten die geen 
afwijking van materieel belang bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de Vennootschap om haar continuïteit te handhaven, het toelichten, indien van 
toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de Vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
 
49  Of andere passende bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
50  Waar het de verantwoordelijkheid is van het management om financiële overzichten op te stellen die een getrouw beeld 
geven, kan dit als volgt luiden: “Management is verantwoordelijk voor het opstellen van de financiële overzichten die een 
getrouw beeld geven in overeenstemming met International Financial Reporting Standards, en voor een (...)” .

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 46/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
proces van financiële verslaggeving van de Vennootschap. 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijking van materieel belang bevatten die het gevolg is van 
fraude of van fouten; en het uitbrengen van een controleverklaring waarin ons oordeel is opgenomen. 
Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie dat een 
controle die overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang ontdekt 
wanneer die bestaat. Afwijkingen kunnen zich voordoen als gevolg van fraude of fouten en worden als 
van materieel belang beschouwd indien redelijkerwijs kan worden verwacht dat zij, individueel of 
gezamenlijk, de economische beslissingen genomen door gebruikers op basis van deze financiële 
overzichten, beïnvloeden.  
Een verdere beschrijving van de verantwoordelijkheden van de auditor voor de controle van de 
financiële overzichten bevindt zich op de website van [Organisatie]: [link tot website]. Deze 
beschrijving maakt deel uit van onze controleverklaring. 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied]  
[Adres van de Auditor]  
[Datum]

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 47/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Voorbeeld 4 – Een controleverklaring over financiële overzichten van een entiteit, anders 
dan een beursgenoteerde entiteit, opgesteld in overeenstemming met een compliance-
stelsel voor algemene doeleinden  
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
• 
Controle van een volledige set van financiële overzichten van een entiteit, anders dan een 
beursgenoteerde entiteit. De controle is geen groepscontrole (i.e., ISA 600 is niet van 
toepassing).  
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met het stelsel voor financiële verslaggeving (Wetgeving XYZ) van rechtsgebied X (d.i. een 
stelsel voor financiële verslaggeving, bestaande uit wet- of regelgeving, dat is opgezet om te 
voorzien in de gemeenschappelijke informatiebehoefte van een breed scala aan gebruikers, 
maar dat geen getrouw-beeld-stelsel is.). 
• 
De voorwaarden van de controleopdracht komen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in 
ISA 210. 
• 
De auditor heeft geconcludeerd dat een niet aangepast (i.e. een “zuiver”) oordeel passend is op 
basis van de verkregen controle-informatie. 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied. 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit 
om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien). 
• 
De auditor heeft geen verplichting tot, en heeft beslist om niet over te gaan tot, het 
communiceren van kernpunten van de controle overeenkomstig ISA 701. 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en 
heeft geen afwijking van materieel belang in de andere informatie vastgesteld. 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de 
met het opstellen van de financiële overzichten belaste personen. 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wetgeving.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 48/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
[Passende geadresseerde] 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
Naar ons oordeel zijn de financiële overzichten in alle van materieel belang zijnde opzichten opgesteld 
in overeenstemming met wetgeving XYZ van rechtsgebied X.  
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
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 1 in bijlage 2 van ISA 720 (herzien)] 
 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen51 
Het 
management is 
verantwoordelijk 
voor 
het opstellen 
van de 
financiële 
overzichten 
in 
overeenstemming met wetgeving XYZ van rechtsgebied X52 en voor de interne beheersing die het 
management noodzakelijk acht om het opstellen mogelijk te maken van financiële overzichten die geen 
afwijking van materieel belang bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de Vennootschap om haar continuïteit te handhaven, het toelichten, indien 
van toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de Vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
proces van financiële verslaggeving van de Vennootschap. 
 
51  Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
52  Waar het de verantwoordelijkheid is van het management om financiële overzichten op te stellen die een getrouw beeld 
geven, kan dit als volgt luiden: “Management is verantwoordelijk voor het opstellen van de financiële overzichten die een 
getrouw beeld geven in overeenstemming met International Financial Reporting Standards, en voor een (...)”.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 49/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijking van materieel belang bevatten die het gevolg is van 
fraude of van fouten, en het uitbrengen van een controleverklaring waarin ons oordeel is opgenomen. 
Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie dat een 
controle die overeenkomstig de ISA’s is uitgevoerd altijd een afwijking van materieel belang ontdekt 
wanneer die bestaat. Afwijkingen kunnen zich voordoen als gevolg van fraude of fouten en worden als 
van materieel belang beschouwd indien redelijkerwijs kan worden verwacht dat zij, individueel of 
gezamenlijk, de economische beslissingen genomen door gebruikers op basis van deze financiële 
overzichten, beïnvloeden. 
Paragraaf 41(b) van deze ISA legt uit dat de in schaduw hieronder voorgestelde tekst kan worden opgenomen in een Bijlage tot 
de controleverklaring. Paragraaf 41(c) legt uit dat wanneer wet- of regelgeving of nationale controlestandaarden op expliciete 
wijze dit toelaten, referentie kan worden gemaakt aan een website van een bevoegde autoriteit die de beschrijving van de 
verantwoordelijkheden van de auditor bevat, eerder dan deze tekst in de controleverklaring op te nemen, op voorwaarde dat de 
beschrijving op de website de beschrijving van de verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en 
hiermee niet inconsistent is. 
 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. We 
voeren tevens de volgende werkzaamheden uit: 
• 
het identificeren en inschatten van de risico’s dat de financiële overzichten een afwijking van 
materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en uitvoeren van 
controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van controle-informatie 
die voldoende en geschikt is als basis voor ons oordeel. Het risico van het niet detecteren van 
een van materieel belang zijnde afwijking is groter indien die afwijking het gevolg is van fraude 
dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn van samenspanning, 
valsheid in geschrifte, het opzettelijk nalaten om transacties vast te leggen, het opzettelijk 
verkeerd voorstellen van zaken of het doorbreken van de interne beheersing; 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle met als doel 
controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn maar die 
niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne beheersing van 
de entiteit53; 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen; 
• 
het concluderen dat de door de management gehanteerde continuïteits-veronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, dat er een 
onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of omstandigheden 
die significante twijfel kunnen doen ontstaan over de mogelijkheid van de Vennootschap om haar 
continuïteit te handhaven. Indien wij concluderen dat er een onzekerheid van materieel belang 
bestaat, zijn wij ertoe gehouden om de aandacht in onze controleverklaring te vestigen op de 
daarop betrekking hebbende toelichtingen in de financiële overzichten, of, indien deze 
toelichtingen inadequaat zijn, om ons oordeel aan te passen. Onze conclusies zijn gebaseerd op 
de controle-informatie die verkregen is tot de datum van onze controleverklaring. Toekomstige 
gebeurtenissen of omstandigheden kunnen er echter toe leiden dat de Vennootschap haar 
continuïteit niet langer kan handhaven. 
 
Wij communiceren met de met governance belaste personen, onder meer over de geplande reikwijdte 
en timing van de controle en over de significante controlebevindingen, waaronder eventuele significante 
tekortkomingen in de interne beheersing die wij identificeren gedurende onze controle. 
 
53  Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
financiële overzichten.

HET VORMEN VAN EEN OORDEEL EN HET RAPPORTEREN OVER FINANCIËLE OVERZICHTEN 
ISA 700 (herzien) 
NBA – IBR 2022 
 50/50 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied]  
[Adres van de Auditor]  
[Datum]