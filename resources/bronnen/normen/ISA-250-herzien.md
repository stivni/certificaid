---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 250 (herzien) — Het in aanmerking nemen van wet- en regelgeving bij een
  controle van financiële overzichten
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-250_(herzien)_nl_2023.pdf
    sha256: 004c0a10d36a2eb336f1eb7ad1bb939287dc4a394d06d40ca1a6820eae8ff318
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
title: ISA 250 (herzien) — Het in aanmerking nemen van wet- en regelgeving bij een
  controle van financiële overzichten
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 250 (herzien) — Het in aanmerking nemen van wet- en regelgeving bij een controle van financiële overzichten

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-250_(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `004c0a10d36a2eb336f1eb7ad1bb939287dc4a394d06d40ca1a6820eae8ff318`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Definitieve uitspraak 
Oktober 2016 
Internationale controlestandaard 250 (herzien) 
ISA 250 (herzien)  
 
Het in aanmerking nemen van 
wet- en regelgeving bij een 
controle van financiële overzichten

ISA 250 (herzien) 
NBA-IBR 2023 
 
2/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
Over de IAASB 
 
Copyright IFAC 
 
Deze Internationale controlestandaard (ISA) werd in 2022 in de Engelse taal gepubliceerd door de 
International Auditing and Assurance Standards Board (IAASB) van de International Federation of 
Accountants (IFAC). Deze ISA werd in 2022 vertaald naar het Nederlands door de Nederlandse 
Beroepsorganisatie van Accountants (NBA), met medewerking van het Belgisch Instituut van de 
Bedrijfsrevisoren (IBR), en werd verspreid met toestemming van IFAC. Het proces voor het vertalen van 
de Internationale controlestandaard (ISA) 250 (herzien) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 
250 (herzien) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 250 (herzien) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 250 (herzien) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 250 (Revised), Consideration of Laws and Regulations 
in an Audit of Financial Statements. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, 
and Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

ISA 250 (herzien) 
NBA-IBR 2023 
 
3/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
 
 
INTERNATIONALE CONTROLESTANDAARD 250 (HERZIEN) 
 
HET IN AANMERKING NEMEN VAN WET EN REGELGEVING BIJ 
EEN CONTROLE VAN FINANCIËLE OVERZICHTEN 
(van toepassing voor controles van financiële overzichten voor perioden eindigend 
op of na 15 december 2017) 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA  ........................................................................................................... 1 
Invloed van wet- en regelgeving............................................................................................................... 2 
Verantwoordelijkheid voor het naleven van wet- en regelgeving ......................................................... 3-9 
Ingangsdatum ......................................................................................................................................... 10 
Doelstellingen  ...................................................................................................................................... 11 
Definities  .............................................................................................................................................. 12 
Vereisten 
Het overwegen door de auditor van het naleven van wet- en regelgeving  ..................................... 13-18 
Controlewerkzaamheden wanneer niet naleving werd geïdentificeerd of vermoed  ....................... 19-22 
Het communiceren en rapporteren van geïdentificeerde of vermoede niet-naleving  ..................... 23-29 
Documentatie  ........................................................................................................................................ 30 
Toepassingsgerichte en overige verklarende teksten 
Verantwoordelijkheid voor het naleven van wet- en regelgeving  .................................................... A1-A8 
Definities ......................................................................................................................................... A9-A10 
Het overwegen door de auditor van het naleven van wet- en regelgeving  ................................. A11-A16 
Controlewerkzaamheden wanneer niet-naleving werd geïdentificeerd of vermoed  ................... A17-A25 
Het communiceren en rapporteren van geïdentificeerde of vermoede niet-naleving  ................. A26-A34 
Documentatie  .............................................................................................................................. A35-A36 
 
 
 
 
Internationale Controlestandaard (ISA) 250 (herzien), Het in aanmerking nemen van wet- en 
regelgeving bij een controle van financiële overzichten dient te worden gelezen in samenhang met 
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een 
controle overeenkomstig de Internationale Controlestandaarden. 
ISA 250 (herzien) heeft de goedkeuring gekregen van de Public Interest Oversight Board (PIOB) 
die tot de conclusie is gekomen dat het due process werd gevolgd in de totstandkoming van de 
standaard en dat juiste aandacht werd besteed aan het openbaar belang.

ISA 250 (herzien) 
NBA-IBR 2023 
 
4/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
Inleiding 
 
Toepassingsgebied van deze Standaard 
 
1. 
Deze Internationale Controlestandaard (ISA) behandelt de verantwoordelijkheid van de auditor 
om wet- en regelgeving in aanmerking te nemen bij een controle van financiële overzichten. Deze 
ISA is niet van toepassing op andere assurance opdrachten waarbij de auditor specifiek de 
opdracht heeft gekregen om afzonderlijk het naleven van specifieke wet- of regelgeving te toetsen 
en daarover te rapporteren. 
 
Invloed van wet- en regelgeving 
 
2. 
De invloed van wet- en regelgeving op de financiële overzichten loopt aanzienlijk uiteen. De wet- 
en regelgeving waaraan een entiteit is onderworpen, vormt het wet- en regelgevingskader. 
Sommige bepalingen van wet- en regelgeving zijn van directe invloed op de financiële overzichten 
omdat zij de gerapporteerde bedragen en toelichtingen in de financiële overzichten van een 
entiteit bepalen. Overige wet- en regelgeving dient door het management te worden nageleefd of 
stelt de bepalingen vast waaronder het de entiteit wordt toegestaan haar activiteiten uit te 
oefenen, maar heeft geen directe invloed op de financiële overzichten van een entiteit. Sommige 
entiteiten zijn actief in streng gereguleerde sectoren (zoals banken en bedrijven in de chemie). 
Andere zijn slechts onderworpen aan veel wet- en regelgeving die in het algemeen betrekking 
hebben op de operationele aspecten van de activiteiten (zoals bepalingen inzake 
arbeidsveiligheid en -gezondheid en gelijke kansen op werk). Het niet naleven van wet- en 
regelgeving kan leiden tot boetes, rechtszaken of andere gevolgen voor de entiteit die een van 
materieel belang zijnde invloed kunnen hebben op de financiële overzichten. 
 
Verantwoordelijkheid voor het naleven van wet- en regelgeving (Zie par. A1-A8) 
 
3. 
Het is de verantwoordelijkheid van het management, onder het toezicht van de met governance 
belaste personen, om ervoor te zorgen dat de activiteiten van de entiteit worden uitgevoerd in 
overeenstemming met de bepalingen van wet- en regelgeving, met inbegrip van de bepalingen 
van wet- en regelgeving die de gerapporteerde bedragen en toelichtingen in de financiële 
overzichten van een entiteit vaststellen. 
 
Verantwoordelijkheid van de auditor 
 
4. 
De vereisten van deze ISA zijn erop gericht de auditor te helpen afwijkingen van materieel belang 
in de financiële overzichten als gevolg van niet-naleving van wet- en regelgeving te identificeren. 
De auditor is evenwel niet verantwoordelijk voor het voorkómen van niet-naleving, en evenmin 
kan er van hem worden verwacht dat hij niet-naleving van alle wet- en regelgeving detecteert. 
 
5. 
De auditor is verantwoordelijk voor het verkrijgen van een redelijke mate van zekerheid dat de 
financiële overzichten als geheel geen afwijkingen van materieel belang bevatten die het gevolg 
zijn van fraude of van fouten. 1 Bij het uitvoeren van een controle van financiële overzichten houdt 
de auditor rekening met het van toepassing zijnde wet- en regelgevingskader. Door de inherente 
beperkingen van een controle bestaat er een onvermijdbaar risico dat bepaalde afwijkingen van 
materieel belang niet worden gedetecteerd, ook al wordt de controle naar behoren gepland en 
overeenkomstig de ISAs uitgevoerd2. In de context van wet- en regelgeving zijn de potentiële 
invloeden van inherente beperkingen op  de mogelijkheid van de auditor om afwijkingen van 
materieel belang te detecteren, groter door factoren zoals de volgende: 
 
 
1  
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de 
Internationale Controlestandaarden, paragraaf 5. 
2  
ISA 200, paragrafen A51-A52.

ISA 250 (herzien) 
NBA-IBR 2023 
 
5/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
• 
Er bestaan veel wets- en regelgevingsvoorschriften, in hoofdzaak met betrekking tot de 
bedrijfsvoeringsaspecten van een entiteit, die door de aard ervan geen invloed hebben op 
de financiële overzichten en die niet zijn vastgelegd in de informatiesystemen van de 
entiteit inzake financiële verslaggeving. 
• 
niet-naleving kan gepaard gaan met handelingen die erop gericht zijn deze te verhullen, 
zoals samenspanning, valsheid in geschrifte, het opzettelijk nalaten transacties vast te 
leggen, het door het management doorbreken van interne beheersingsmaatregelen of het 
opzettelijk aan de auditor verkeerd voorstellen van zaken; 
• 
de vraag of een handeling niet-naleving vormt, is uiteindelijk een zaak die door een 
rechtbank of andere bevoegde gerechtelijke instantie moet worden vastgesteld. 
 
Doorgaans geldt dat hoe verder de niet-naleving afstaat van de gebeurtenissen en transacties 
die in de financiële overzichten zijn weerspiegeld, des te onwaarschijnlijker het is dat de auditor 
zich hiervan bewust wordt of dat hij de niet-naleving zal herkennen. 
 
6. 
In deze ISA wordt het volgende onderscheid gemaakt in de verantwoordelijkheden van de auditor 
met betrekking tot het naleven van twee verschillende categorieën van wet- en regelgeving: (Zie 
par. A6, A12-A13) 
 
(a) 
de bepalingen van die wet- en regelgeving die in het algemeen geacht worden van directe 
invloed te zijn op de vaststelling van bedragen en in de financiële overzichten opgenomen 
toelichtingen die van materieel belang zijn, zoals wet- en regelgeving op het gebied van 
belastingen en pensioenen (Zie par. 14) (Zie par. A12); en 
(b) 
overige wet- en regelgeving die geen directe invloed heeft op de vaststelling van de 
bedragen en toelichtingen in de financiële overzichten, maar waarvan het naleven van 
fundamenteel belang kan zijn voor de operationele aspecten van het bedrijf, voor de 
mogelijkheid van een entiteit om haar activiteiten voort te zetten, dan wel voor het 
voorkomen van sancties van materieel belang (bijv. het naleven van de voorwaarden van 
een vergunning voor het uitvoeren van een activiteit, het naleven van door een 
regelgevende of toezichthoudende instantie gestelde solvabiliteitseisen, of het naleven van 
regelgeving betreffende het milieu); niet-naleving van dergelijke wet- en regelgeving kan 
daarom van materieel belang zijnde invloed hebben op de financiële overzichten. (Zie 
par. 15) (Zie par. A13) 
 
7. 
In deze ISA zijn verschillende vereisten gespecificeerd voor elk van de beide hierboven 
genoemde categorieën van wet- en regelgeving. Voor de categorie waarnaar in paragraaf 6(a) 
wordt verwezen, is het de verantwoordelijkheid van de auditor om voldoende en geschikte 
controle-informatie te verkrijgen omtrent het naleven van de bepalingen van die wet- en 
regelgeving. Voor de categorie waarnaar in paragraaf 6(b) wordt verwezen, is de 
verantwoordelijkheid van de auditor beperkt tot het uitvoeren van gespecificeerde 
controlewerkzaamheden ter bevordering van het identificeren van niet-naleving van wet- en 
regelgeving die een invloed van materieel belang kan hebben op de financiële overzichten. 
 
8. 
Deze ISA vereist dat de auditor alert blijft op de mogelijkheid dat andere controlewerkzaamheden, 
uitgevoerd met als doel een oordeel over de financiële overzichten te vormen, gevallen niet-
naleving van wet- en regelgeving onder de aandacht van de auditor kunnen brengen. Het 
handhaven van een professioneel-kritische instelling gedurende de gehele controle, zoals is 
voorgeschreven door ISA 200 3, is in deze context belangrijk, gezien de omvang van de wet- en 
regelgeving die van invloed is op de entiteit. 
 
9. 
De auditor kan additionele verantwoordelijkheden hebben onder wet- of regelgeving of relevante 
ethische voorschriften met betrekking tot niet-naleving van wet- en regelgeving van een entiteit, 
die kunnen verschillen van of verder gaan dan deze ISA, zoals: (Zie par. A8) 
 
 
3  
ISA 200, paragraaf 15.

ISA 250 (herzien) 
NBA-IBR 2023 
 
6/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
(a) 
inspelen op geïdentificeerde of vermoede niet-naleving van wet- en regelgeving, inclusief 
vereisten met betrekking tot specifieke communicatie met het management en de personen 
belast met governance, inschatten van de geschiktheid van hun reactie op niet-naleving 
en overwegen of verdere actie noodzakelijk is; 
(b) 
communiceren van geïdentificeerde of vermoede niet-naleving van wet- en regelgeving 
aan andere auditors (b.v. in een controle van financiële overzichten van een groep); en 
(c) 
documentatievereisten met betrekking tot geïdentificeerde of vermoede niet-naleving van 
wet- en regelgeving. 
 
Naleven van additionele verantwoordelijkheden kan verdere informatie verschaffen die relevant is voor 
het werk van de auditor in overeenstemming met deze en andere ISAs (b.v. met betrekking tot de 
integriteit van het management of, in voorkomend geval, de personen belast met governance). 
 
Ingangsdatum 
 
10. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperiodes die op 
of na 15 december 2017 aanvangen. 
 
Doelstellingen 
 
11. 
De doelstellingen van de auditor zijn: 
  
(a) 
het verkrijgen van voldoende en geschikte controle-informatie omtrent het naleven van de 
bepalingen van die wet- en regelgeving die gewoonlijk wordt geacht van directe invloed te 
zijn op de vaststelling van bedragen en in de financiële overzichten opgenomen 
toelichtingen die van materieel belang zijn; 
(b) 
het uitvoeren van gespecificeerde controlewerkzaamheden teneinde bij te dragen tot het 
identificeren van gevallen van niet-naleving van overige wet- en regelgeving die een 
invloed van materieel belang kan hebben op de financiële overzichten; en 
(c) 
het op passende wijze inspelen op tijdens de controle geïdentificeerde of vermoede niet-
naleving van wet- en regelgeving. 
 
Definities 
 
12. 
Voor de toepassing van de ISAs heeft de volgende term de hierna weergegeven betekenis: 
  
Niet-naleving – Het , opzettelijk of niet opzettelijk, in strijd met de geldende wet- of regelgeving 
uitvoeren of niet uitvoeren van handelingen begaan door de entiteit, of door de personen belast 
met governance, door het management of door andere individuen die werken voor of onder 
leiding van de entiteit. Persoonlijke misdragingen (die geen verband houden met de zakelijke 
activiteiten van de entiteit) door de met governance belaste personen, het management of 
werknemers van de entiteit vallen niet onder niet-naleving. (Zie par. A9-A10) 
 
Vereisten 
 
Het overwegen door de auditor van het naleven van wet- en regelgeving 
 
13. 
In het kader van het verwerven van inzicht in de entiteit en haar omgeving overeenkomstig ISA 
315 (herzien 2019),4 dient de auditor een algemeen inzicht te verwerven in: 
 
(a) 
het wet- en regelgevingskader dat van toepassing is op de entiteit en de branche of sector 
waarbinnen de entiteit actief is; en 
 
4  
ISA 315 (herzien 2019), Risico’s op een afwijking van materieel belang identificeren en inschatten, paragraaf 11.

ISA 250 (herzien) 
NBA-IBR 2023 
 
7/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
(b) 
de manier waarop de entiteit dat kader naleeft. (Zie par. A11) 
 
14. 
De auditor dient voldoende en geschikte controle-informatie te verkrijgen omtrent het naleven van 
de bepalingen van die wet- en regelgeving die gewoonlijk wordt geacht van directe invloed te zijn 
op de vaststelling van bedragen en in de financiële overzichten opgenomen toelichtingen die van 
materieel belang zijn. (Zie par. A12) 
 
15. 
Ter bevordering van het identificeren van gevallen van niet-naleving van overige wet- en 
regelgeving die een invloed van materieel belang kan hebben op de financiële overzichten, dient 
de auditor de volgende controlewerkzaamheden uit te voeren: (Zie par. A13-A14) 
 
(a) 
Het management en, in voorkomend geval, de met governance belaste personen vragen 
of de entiteit dergelijke wet- en regelgeving naleeft; en 
(b) 
De eventuele correspondentie met de desbetreffende vergunningverlenende of 
regelgevende of toezichthoudende instanties inspecteren.  
 
16. 
De auditor dient gedurende de controle alert te blijven op de mogelijkheid dat andere 
controlewerkzaamheden die worden uitgevoerd, de niet-naleving of vermoedens van niet-
naleving van wet- en regelgeving onder de aandacht van de auditor kunnen brengen. (Zie par. 
A15) 
 
17. 
De auditor dient het management en in voorkomend geval, de met governance belaste personen, 
te verzoeken schriftelijke bevestigingen te verstrekken dat alle bekende gevallen van niet-
naleving of vermoede niet-naleving van wet- en regelgeving waarmee bij het opstellen van de 
financiële overzichten rekening moet worden gehouden, de auditor ter kennis zijn gebracht. (Zie 
par. A16) 
 
18. 
Indien er geen sprake is van geïdentificeerde of vermoede niet-naleving van wet- en regelgeving 
wordt niet van de auditor vereist dat hij andere controlewerkzaamheden uitvoert met betrekking 
tot het naleven van wet- en regelgeving door de entiteit, dan die werkzaamheden die zijn 
uiteengezet in de paragrafen 13–17. 
 
Controlewerkzaamheden wanneer niet-naleving werd geïdentificeerd of vermoed 
 
19. 
Indien de auditor zich bewust wordt van informatie omtrent een geval of vermoeden van niet-
naleving van wet- en regelgeving, dient de auditor het volgende te verkrijgen: (Zie par. A17-A18) 
 
(a) 
inzicht in de aard van de handeling en de omstandigheden waaronder deze heeft 
plaatsgevonden; en 
(b) 
verdere informatie om de mogelijke invloed op de financiële overzichten te evalueren. (Zie 
par. A19) 
 
20. 
Indien de auditor vermoedt dat er sprake kan zijn van niet-naleving, dient de auditor de 
aangelegenheid, tenzij dit op grond van wet- of regelgeving verboden is, met het management 
op het passende verantwoordelijkheidsniveau en, in voorkomend geval, met de met governance 
belaste personen te bespreken. Indien het management of, in voorkomend geval, de met 
governance belaste personen niet voldoende informatie verstrekt (verstrekken) waaruit blijkt dat 
de entiteit de wet- en regelgeving naleeft, en indien op grond van de oordeelsvorming van de 
auditor het effect van vermoedens van niet-naleving voor de financiële overzichten van materieel 
belang kan zijn, dient de auditor de noodzaak te overwegen om juridisch advies in te winnen. (Zie 
par. A20-A22) 
 
21. 
Indien niet voldoende informatie omtrent vermoedens van niet-naleving kan worden verkregen, 
dient de auditor de invloed van het gebrek aan voldoende en geschikte controle-informatie op zijn 
oordeel te evalueren.

ISA 250 (herzien) 
NBA-IBR 2023 
 
8/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
22. 
De auditor dient de gevolgen van geïdentificeerde of vermoede niet-naleving met betrekking tot 
de andere aspecten van de controle te evalueren, met inbegrip van de risico-inschatting van de 
auditor en de betrouwbaarheid van schriftelijke bevestigingen, alsmede passende actie te 
ondernemen. (Zie par. A23-A25) 
 
Het communiceren en rapporteren van geïdentificeerde over vermoede niet-naleving 
 
Het communiceren van geïdentificeerde of vermoede niet-naleving met de met governance belaste 
personen 
 
23. 
Tenzij alle met governance belaste personen betrokken zijn bij het leiden van de entiteit en 
daardoor kennis hebben van aangelegenheden omtrent geïdentificeerde of vermoede niet-
naleving die door de auditor reeds zijn meegedeeld,5 dient de auditor, tenzij dit op grond van wet- 
of regelgeving verboden is, aan de met governance belaste personen aangelegenheden mee te 
delen omtrent niet-naleving van wet- en regelgeving die in de loop van de controle onder zijn 
aandacht zijn gekomen, behalve wanneer de aangelegenheden duidelijk onbetekenend zijn. 
 
24. 
Indien, op grond van de oordeelsvorming van de auditor, niet-naleving waarnaar in paragraaf 22 
wordt verwezen, als opzettelijk en van materieel belang wordt beschouwd, dient de auditor de 
aangelegenheid zo spoedig als praktisch uitvoerbaar is aan de met governance belaste personen 
mee te delen. 
 
25. 
Indien de auditor vermoedt dat het management of de met governance belaste personen 
betrokken is (zijn) bij niet-naleving dient de auditor de aangelegenheid te rapporteren aan het 
volgende hogere gezagsniveau binnen de entiteit, indien dit bestaat, zoals een auditcomité of een 
toezichthoudend orgaan. In het geval een dergelijk hoger gezagsniveau niet bestaat of indien de 
auditor van mening is dat naar aanleiding van zijn mededeling geen actie zal worden ondernomen 
of indien hij niet zeker is aan wie hij moet rapporteren, dient de auditor de noodzaak te overwegen 
juridisch advies in te winnen. 
 
Mogelijke implicaties van geïdentificeerde of vermoede niet-naleving in voor de controleverklaring (Zie 
par. A26-A27) 
 
26. 
Indien de auditor tot de conclusie komt dat de geïdentificeerde of vermoede niet-naleving een 
invloed van materieel belang heeft op de financiële overzichten en niet op adequate wijze in de 
financiële overzichten is weerspiegeld, dient de auditor overeenkomstig ISA 705 een oordeel met 
beperking dan wel een afkeurend oordeel over de financiële overzichten tot uitdrukking te 
brengen.6 
 
27. 
Indien de auditor door het management of de met governance belaste personen wordt verhinderd 
om voldoende en geschikte controle-informatie te verkrijgen om te evalueren of er sprake is 
geweest dan wel waarschijnlijk sprake is geweest van niet-naleving die een invloed van materieel 
belang kan hebben op de financiële overzichten, dient de auditor over de financiële overzichten 
een oordeel met beperking tot uitdrukking te brengen dan wel een oordeelonthouding te 
formuleren op basis van een beperking in de reikwijdte van de controle, overeenkomstig ISA 705.7 
 
28. 
Indien de auditor vanwege beperkingen die door de omstandigheden zijn veroorzaakt en niet door 
het management of door de met governance belaste personen zijn opgelegd, niet in staat is te 
bepalen of er sprake is geweest van niet-naleving, dient de auditor overeenkomstig ISA 705 de 
invloed daarvan op het oordeel van de auditor te evalueren. 
 
Het rapporteren van niet-naleving aan bevoegde instantie buiten de entiteit 
 
5  
ISA 260 (herzien), Communicatie met de met governance belaste personen, paragraaf 13 
6  
ISA 705 (herzien), Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor, paragraaf 7-8. 
7  
ISA 705 (herzien), paragrafen 7 en 9.

ISA 250 (herzien) 
NBA-IBR 2023 
 
9/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
29. 
Indien de auditor gevallen van niet-naleving van wet- en regelgeving heeft geïdentificeerd of 
indien hij deze vermoedt, dient de auditor te bepalen of wet-of regelgeving of relevante ethische 
voorschriften: (Zie par. A28-A34) 
 
(a) 
van de auditor vereisen om te rapporteren aan een bevoegde instantie buiten de entiteit. 
(b) 
verantwoordelijkheden vaststellen waaronder het rapporteren aan een bevoegde instantie 
buiten de entiteit passend kan zijn in de omstandigheden. 
 
Documentatie 
 
30. 
De auditor dient in de controledocumentatie8 geïdentificeerde of vermoede niet-naleving van wet- 
en regelgeving op te nemen, alsmede: (Zie par. A35-A36) 
 
(a) 
de uitgevoerde controlewerkzaamheden, de significante gemaakte oordeelsvormingen en 
de conclusies die daarover zijn getrokken; en 
(b) 
de besprekingen van significante aangelegenheden met betrekking tot de niet-naleving met 
het management, de personen belast met governance en anderen, inclusief hoe het 
management en, waar van toepassing, de personen belast met governance hebben 
gereageerd op de aangelegenheid. 
 
*** 
 
Toepassingsgerichte en overige verklarende teksten 
 
Verantwoordelijkheden voor het naleven van wet- en regelgeving (Zie par. 3-9) 
  
A1. 
Het is de verantwoordelijkheid van het management, onder het toezicht van de met governance 
belaste personen, om ervoor te zorgen dat de activiteiten van de entiteit in overeenstemming met 
de wet- en regelgeving worden uitgevoerd. Wet- en regelgeving kan de financiële overzichten 
van een entiteit op verschillende manieren beïnvloeden: op de meest directe manier kan zij 
bijvoorbeeld van invloed zijn op specifieke van de entiteit vereiste toelichtingen in de financiële 
overzichten, of kan zij het van toepassing zijnde stelsel inzake financiële verslaggeving 
voorschrijven. Zij kan tevens bepaalde juridische rechten en verplichtingen van de entiteit 
vaststellen, waarvan sommige in de financiële overzichten van de entiteit zullen worden 
opgenomen. Bovendien kunnen bij wet- en regelgeving sancties worden opgelegd in geval van 
niet-naleving. 
 
A2. 
Ter bevordering van het voorkómen en het detecteren van niet-naleving van wet- en regelgeving 
kan een entiteit bijvoorbeeld de volgende soorten beleidslijnen en procedures implementeren: 
 
• 
het monitoren van de door de wet gestelde vereisten en ervoor zorgen dat operationele 
maatregelen erop gericht zijn hieraan te voldoen; 
• 
het invoeren en toepassen van passende interne beheersingssystemen; 
• 
het ontwikkelen, openbaar maken en naleven van een gedragscode; 
• 
ervoor zorgen dat werknemers naar behoren zijn opgeleid en dat zij de gedragscode 
begrijpen; 
• 
het monitoren van het naleven van de gedragscode en het treffen van disciplinaire 
maatregelen jegens werknemers die de code niet naleven; 
• 
het inschakelen van juridisch adviseurs om het monitoren van de juridische vereisten te 
ondersteunen; 
• 
het bijhouden van een registratie van significante wet- en regelgeving die door de entiteit 
dient te worden nageleefd in de specifieke branche waarin ze actief is, alsmede een 
vastlegging van klachten.  
 
8  
ISA 230, Controledocumentatie, paragrafen 8-11 en A6.

ISA 250 (herzien) 
NBA-IBR 2023 
 
10/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
  
Bij grotere entiteiten kunnen deze beleidslijnen en procedures worden aangevuld met het toewijzen van 
passende verantwoordelijkheden aan: 
 
• 
een interne auditfunctie; 
• 
een auditcomité; 
• 
een compliancefunctie. 
 
Verantwoordelijkheid van de auditor  
 
A3. 
Niet-naleving van wet- en regelgeving door de entiteit kan resulteren in een afwijking van 
materieel belang in de financiële overzichten. Het detecteren van niet-naleving, ongeacht de 
materialiteit, kan andere aspecten van de controle beïnvloeden, zoals het overwegen door de 
auditor van de integriteit van het management, de personen belast met governance of van 
werknemers. 
 
A4. 
Of een handeling als een geval van niet-naleving van wet- en regelgeving moet worden 
aangemerkt, is een aangelegenheid die bepaald wordt door een rechtbank of andere bevoegde 
gerechtelijke instantie. In het algemeen beschikt de auditor niet over de vakbekwaamheid om 
hierover te oordelen. Niettemin kan de auditor op basis van zijn training, ervaring en inzicht in de 
entiteit en in de branche of sector inzien dat bepaalde handelingen die onder zijn aandacht 
komen, niet-naleving van wet- en regelgeving kunnen vormen. 
 
A5. 
Het is mogelijk dat de auditor overeenkomstig specifieke wettelijke vereisten, in het kader van de 
controle van de financiële overzichten moet rapporteren omtrent de vraag of de entiteit specifieke 
bepalingen van wet- en regelgeving naleeft. In deze gevallen behandelen ISA 7009 of ISA 80010 
de wijze waarop in de controleverklaring met deze controleverantwoordelijkheden wordt 
omgegaan. In het geval van specifiek door de wet gestelde vereisten inzake rapporteren, is het 
mogelijk dat het controleprogramma passende toetsingen moet bevatten betreffende het naleven 
van deze bepalingen van wet- en regelgeving. 
 
Categorieën van wet- en regelgeving (Zie par. 6) 
 
A6. 
De aard en omstandigheden van de entiteit kunnen van invloed zijn op de vraag of relevante wet- 
en regelgeving binnen de categorieën van wet- en regelgeving vallen zoals beschreven in 
paragrafen 6(a) of 6(b). Voorbeelden van wet- en regelgeving die kunnen zijn inbegrepen in de 
categorieën beschreven in paragraaf 6 omvatten degenen die betrekking hebben op: 
 
• 
fraude, corruptie en omkoping. 
• 
witwassen, financiering van terrorisme en opbrengsten van misdrijven. 
• 
effecten markten en handel. 
• 
bankdiensten en andere financiële producten en diensten. 
• 
databescherming. 
• 
belasting- en pensioenverplichtingen en –betalingen. 
• 
milieubescherming. 
• 
volksgezondheid en veiligheid. 
 
Overwegingen die specifiek voor entiteiten in de publieke sector gelden 
 
A7. 
In de publieke sector kan er sprake zijn van aanvullende controleverantwoordelijkheden met 
betrekking tot het in aanmerking nemen van wet- en regelgeving die verband houden met de 
 
9  
ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten, paragraaf 38. 
10  ISA 800 (herzien), Bijzondere overwegingen: controles van financiële overzichten die zijn opgesteld in overeenstemming met 
stelsels voor bijzondere doeleinden, paragraaf 11.

ISA 250 (herzien) 
NBA-IBR 2023 
 
11/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
controle van financiële overzichten of die ook andere aspecten van de activiteiten van de entiteit 
kunnen omvatten. 
 
Additionele verantwoordelijkheden vastgesteld door wet- en regelgeving of relevante ethische 
voorschriften (Zie par.9) 
 
A8. 
Wet- of regelgeving of relevante ethische voorschriften kunnen van de auditor vereisen om 
additionele werkzaamheden te verrichten en verdere actie te ondernemen. Bijvoorbeeld de Code 
of Ethics voor professionele accountants uitgegeven door de International Ethics Standards 
Board for Accountants (IESBA Code) vereist van de auditor om stappen te ondernemen om in te 
spelen op geïdentificeerde of vermoede niet-naleving van wet- en regelgeving en te bepalen of 
verdere actie nodig is. Zulke stappen kunnen de communicatie van geïdentificeerde of vermoede 
niet-naleving van wet- en regelgeving aan andere auditors binnen een groep omvatten, inclusief 
een opdrachtpartner op groepsniveau, auditors van groepsonderdelen of andere auditors die 
werk uitvoeren bij groepsonderdelen voor andere doeleinden dan de controle van de financiële 
overzichten van de groep.11 
 
Definitie (Zie par. 12) 
 
A9. 
Handelingen van niet-naleving van wet- en regelgeving omvatten transacties die zijn aangegaan 
door, of in naam van of  voor rekening van, de entiteit, door de personen belast met governance, 
door het management of door andere individuen die werken voor of onder de leiding van de 
entiteit. 
 
A10. Niet-naleving omvat ook persoonlijke misdragingen die verband houden met de zakelijke 
activiteiten van de entiteit, bijvoorbeeld in omstandigheden waarin een individu in een 
sleutelpositie binnen het management op persoonlijke titel steekpenningen heeft aangenomen 
van een leverancier van de entiteit en in ruil daarvoor de aanstelling van de leverancier om 
diensten of contracten aan de entiteit te verlenen, zeker stelt. 
 
Het overwegen door de auditor van het naleven van wet- en regelgeving  
 
Het verwerven van inzicht in het wet- en regelgevingskader (Zie par. 13) 
 
A11. Voor het verwerven van een algemeen inzicht in het wet- en regelgevingskader, en in de wijze 
waarop de entiteit dat kader naleeft, kan de auditor bijvoorbeeld:  
 
• 
gebruikmaken van zijn inzicht in de sectorgebonden, regelgevings- en andere externe 
factoren van de entiteit; 
• 
zijn inzicht actualiseren in de wet- en regelgeving welke de gerapporteerde bedragen en 
toelichtingen in de financiële overzichten direct bepaalt; 
• 
bij het management inlichtingen inwinnen over overige wet- of regelgeving waarvan kan 
worden verwacht dat deze een fundamentele invloed heeft op de uitoefening van de 
activiteiten van de entiteit; 
• 
bij het management inlichtingen inwinnen over de beleidslijnen en procedures van de 
entiteit inzake het naleven van wet- en regelgeving; en 
• 
bij het management inlichtingen inwinnen over de beleidslijnen en procedures die zijn 
vastgesteld ten aanzien van het identificeren, evalueren en administratief verwerken van 
claims die voortvloeien uit rechtszaken. 
 
Wet- en regelgeving waarvan in het algemeen wordt aangenomen dat zij een directe invloed heeft op 
het bepalen van bedragen en toelichtingen in de financiële overzichten die van materieel belang zijn 
(Zie Par. 6, 14) 
 
 
11  Zie secties 225.21–225.22 van de IESBA Code.

ISA 250 (herzien) 
NBA-IBR 2023 
 
12/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
A12. Bepaalde wet- en regelgeving is goed ontwikkeld, bekend bij de entiteit en binnen haar branche 
of sector en relevant voor de financiële overzichten (zoals beschreven in paragraaf 6(a)). 
Dergelijke wet- en regelgeving kan onder meer betrekking hebben op: 
 
• 
de vorm en inhoud van de financiële overzichten; 
• 
sectorspecifieke kwesties met betrekking tot financiële verslaggeving; 
• 
de administratieve verwerking van transacties voortvloeiend uit contracten met de 
overheid; of 
• 
het toerekenen of opnemen van lasten inzake winstbelastingen of van pensioenkosten. 
 
Sommige bepalingen in deze wet- en regelgeving kunnen op directe wijze relevant zijn voor 
specifieke beweringen in de financiële overzichten (bijv. de volledigheid van voorzieningen voor 
winstbelastingen), terwijl andere op directe wijze relevant kunnen zijn voor de financiële 
overzichten als geheel (bijv. de vereiste overzichten die een volledige set financiële overzichten 
vormen). Het oogmerk van het in paragraaf 14 bepaalde vereiste is dat de auditor voldoende en 
geschikte controle-informatie verkrijgt omtrent het bepalen van bedragen en toelichtingen in de 
financiële overzichten overeenkomstig de relevante bepalingen van die wet- en regelgeving. Niet-
naleving van andere bepalingen van dergelijke en overige wet- en regelgeving kan leiden tot 
boetes, rechtszaken of andere gevolgen voor de entiteit, waarvan de kosten mogelijk in de 
financiële overzichten moeten worden opgenomen, maar die niet worden geacht een directe 
invloed op de financiële overzichten te hebben zoals beschreven in paragraaf 6(a). 
 
Procedures gericht op het identificeren van gevallen van niet-naleving – overige wet- en regelgeving 
(Zie par. 6, 15) 
 
A13. Bepaalde overige wet- en regelgeving vergt mogelijk bijzondere aandacht van de auditor omdat 
zij een fundamentele invloed heeft op de activiteiten van de entiteit (zoals beschreven in paragraaf 
6(b)). Niet-naleving van wet- en regelgeving die een fundamentele invloed heeft op de activiteiten 
van de entiteit kan ertoe leiden dat de entiteit haar activiteiten moet beëindigen of dat het 
handhaven van de continuïteit van de entiteit in het geding komt.12 Zo kan niet-naleving van de 
vereisten op grond van de vergunning of een andere machtiging van de entiteit om haar 
activiteiten uit te oefenen, een dergelijk gevolg hebben (bijv. voor een bank: niet-naleving van de 
kapitaal- of beleggingsvereisten). Er is ook veel wet- en regelgeving, in hoofdzaak met betrekking 
op de operationele aspecten van de entiteit, die door de aard daarvan geen invloed heeft op de 
financiële overzichten en die niet in de voor de financiële verslaggeving relevante 
informatiesystemen van de entiteit is vastgelegd. 
 
A14. Omdat overige wet- en regelgeving verschillende gevolgen kan hebben voor de financiële 
verslaggeving naar gelang van de activiteiten van de entiteit, zijn de op grond van paragraaf 15 
vereiste controlewerkzaamheden gericht op het onder de aandacht van de auditor brengen van 
gevallen van niet-naleving van wet- en regelgeving die een invloed van materieel belang kan 
hebben op de financiële overzichten. 
 
Gevallen van niet-naleving die als gevolg van andere controlewerkzaamheden onder de aandacht van 
de auditor zijn gebracht (Zie par. 16) 
 
A15. 
Controlewerkzaamheden die worden uitgevoerd om een oordeel over de financiële overzichten te 
vormen, kunnen gevallen van gedetecteerde of vermoede niet-naleving van wet- en regelgeving 
onder de aandacht van de auditor brengen. Dergelijke controlewerkzaamheden zijn bijvoorbeeld: 
 
• 
het lezen van notulen; 
• 
het vragen aan het management en de interne of externe juridisch adviseur van de entiteit 
naar rechtszaken, claims en inschattingen; en 
 
12  Zie ISA 570 (herzien), Continuïteit.

ISA 250 (herzien) 
NBA-IBR 2023 
 
13/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
• 
het uitvoeren van gegevensgerichte detailcontroles op categorieën van transactiestromen, 
rekeningsaldi of in de financiële overzichten opgenomen toelichtingen. 
 
Schriftelijke bevestigingen (Zie par. 17) 
 
A16. Omdat de invloed van wet- en regelgeving op financiële overzichten aanzienlijk kan verschillen, 
verschaffen schriftelijke bevestigingen noodzakelijke controle-informatie over de kennis van het 
management over geïdentificeerde of vermoede niet-naleving van wet- en regelgeving, waarvan 
de gevolgen van materieel belang zijnde invloed kunnen hebben op de financiële overzichten. 
Schriftelijke bevestigingen op zichzelf voorzien evenwel niet in voldoende en geschikte controle-
informatie en hebben bijgevolg geen invloed op de aard en omvang van andere controle-
informatie die door de auditor moet worden verkregen.13 
 
Controlewerkzaamheden wanneer niet-naleving werd geïdentificeerd of vermoed 
 
Aanwijzingen voor niet-naleving van wet- en regelgeving (Zie par. 19) 
 
A17. De auditor kan zich bewust worden van informatie met betrekking tot een geval van niet-naleving 
van wet- en regelgeving anders dan als gevolg van het uitvoeren van de werkzaamheden in 
paragrafen 13-17 (bijv. wanneer de auditor wordt geattendeerd op niet-naleving door een 
klokkenluider). 
 
A18. De volgende aangelegenheden, kunnen een aanwijzing zijn voor niet-naleving van wet- en 
regelgeving: 
 
• 
onderzoeken door regelgevende of toezichthoudende instanties en overheidsinstanties, 
dan wel betaling van boetes of sancties; 
• 
betalingen voor niet gespecificeerde diensten of leningen aan consultants, verbonden 
partijen of overheidsfunctionarissen; 
• 
commissies op verkopen of vergoedingen van agenten die buitensporig hoog lijken in 
verhouding tot hetgeen gewoonlijk wordt betaald door de entiteit of in de branche, dan wel 
tot de daadwerkelijk ontvangen diensten; 
• 
inkopen tegen prijzen die beduidend boven of beneden marktprijzen liggen; 
• 
ongebruikelijke contante betalingen, aankopen tegen cheques aan toonder of 
overboekingen naar nummerrekeningen bij banken; 
• 
ongebruikelijke 
transacties 
met 
vennootschappen 
statutair 
gevestigd 
in 
belastingparadijzen; 
• 
betalingen voor goederen of verleende diensten in een ander land dan het land van 
herkomst van de goederen of diensten; 
• 
betalingen 
zonder 
behoorlijke 
documentatie 
(met 
betrekking 
tot 
interne 
beheersingsmaatregelen) voor vreemde valutatransacties; 
• 
het bestaan van een informatiesysteem dat door zijn opzet of toevallig niet in staat is een 
adequaat controlespoor dan wel voldoende informatie te verschaffen; 
• 
niet-geautoriseerde transacties of niet naar behoren vastgelegde transacties; 
• 
negatieve publiciteit in de media. 
 
Aangelegenheden die relevant zijn voor de evaluatie door de auditor (Zie par. 19(b)) 
 
A19. Aangelegenheden die relevant zijn voor het evalueren door de auditor van de mogelijke invloed 
op de financiële overzichten zijn onder meer:  
 
• 
de mogelijke financiële gevolgen van geïdentificeerde of vermoede niet-naleving van wet- 
en regelgeving voor de financiële overzichten, waaronder het opleggen van boetes, 
 
13  ISA 580, Schriftelijke bevestigingen, paragraaf 4.

ISA 250 (herzien) 
NBA-IBR 2023 
 
14/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
strafvorderingen, schadevergoedingen, de dreiging van inbeslagneming van activa, de 
gedwongen beëindiging van de activiteiten, alsmede rechtszaken; 
• 
de vraag of de potentiële financiële gevolgen toelichting vereisen; 
• 
de vraag of de potentiële financiële gevolgen zo ernstig zijn dat de getrouwe weergave van 
de financiële overzichten ter discussie komt te staan, of dat de financiële overzichten 
anderszins een misleidend karakter krijgen. 
 
Controlewerkzaamheden en het communiceren van geïdentificeerde of vermoede niet-naleving aan het 
management en de met governance belaste personen (Zie par. 20) 
 
A20. Van de auditor is vereist om de vermoede niet-naleving te bespreken met het management op 
het passende verantwoordelijkheidsniveau en, waar van toepassing, met de met governance 
belaste personen, zodat zij in staat kunnen zijn aanvullende controle-informatie te geven. De 
auditor kan bijvoorbeeld bevestigen dat het management, en waar van toepassing, de met 
governance belaste personen hetzelfde begrip hebben van de feiten en omstandigheden die 
relevant zijn voor transacties of gebeurtenissen die hebben geleid tot de vermoede niet-naleving 
van wet- en regelgeving. 
 
A21. Echter, in bepaalde rechtsgebieden, kan wet- of regelgeving de communicatie van de auditor van 
bepaalde aangelegenheden met het management en de personen belast met governance 
beperken. Wet- of regelgeving kan specifiek communicatie, of andere actie, verbieden die een 
onderzoek door een bevoegde instantie naar een actuele of vermoede illegale handeling zou 
kunnen schaden, inclusief het hierop attenderen van de entiteit. Bijvoorbeeld wanneer van de 
auditor is vereist om de geïdentificeerde of vermoede niet-naleving te rapporteren aan een 
bevoegde instantie krachtens anti-witwas wetgeving. In deze omstandigheden kunnen de 
kwesties die worden overwogen door de auditor complex zijn en de auditor kan het geschikt 
achten juridisch advies in te winnen. 
 
A22. Indien het management of, in voorkomend geval, de met governance belaste personen, aan de 
auditor geen voldoende informatie verstrekt (verstrekken) waaruit blijkt dat de entiteit wel degelijk 
wet- en regelgeving naleeft, kan de auditor het passend achten om de interne of externe juridisch 
adviseur van de entiteit te raadplegen omtrent het toepassen van de wet- en regelgeving op de 
omstandigheden, met inbegrip van de mogelijkheid van fraude, alsmede omtrent de mogelijke 
gevolgen voor de financiële overzichten. Indien het niet passend wordt geacht de juridisch 
adviseur van de entiteit te raadplegen of indien de auditor niet tevreden is met het advies dat is 
verstrekt door de juridisch adviseur, kan de auditor het passend achten op een vertrouwelijke 
basis anderen binnen het kantoor, een kantoor die deel uitmaakt van het netwerk, een 
beroepsorganisatie of de juridisch adviseur van de auditor te raadplegen over de vraag of er 
sprake is van schending van een wet of regel, met inbegrip van de mogelijkheid van fraude, wat 
de mogelijke juridische gevolgen daarvan kunnen zijn, en welke verdere actie de auditor 
eventueel zou moeten ondernemen. 
 
Het evalueren van de gevolgen van geïdentificeerde over vermoede niet-naleving (Zie par. 22) 
 
A23. Zoals in paragraaf 22 is voorgeschreven, evalueert de auditor de gevolgen van geïdentificeerde 
of vermoede niet-naleving met betrekking tot andere aspecten van de controle, met inbegrip van 
de risico-inschatting door de auditor en de betrouwbaarheid van schriftelijke bevestigingen. De 
gevolgen van bepaalde geïdentificeerde of vermoede niet-naleving, zullen afhangen van de 
verhouding tussen het plegen van de handeling en het eventueel verhullen ervan voor de 
specifieke interne beheersingsmaatregelen en het niveau van het management of individuen die 
werken voor of onder de leiding van de entiteit dat (die) daarbij betrokken is (zijn), in het bijzonder 
de gevolgen die voortvloeien uit de betrokkenheid van het hoogste gezag binnen de entiteit. Zoals 
vermeld in paragraaf 9, kan naleving van wet- en regelgeving of relevante ethische voorschriften 
door de auditor verdere informatie verstrekken die relevant is voor de verantwoordelijkheden van 
de auditor in overeenstemming met paragraaf 22.

ISA 250 (herzien) 
NBA-IBR 2023 
 
15/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
A24. Er zijn omstandigheden die ertoe kunnen leiden dat de auditor de implicaties van geïdentificeerde 
of vermoede niet-naleving voor de betrouwbaarheid van schriftelijke bevestigingen ontvangen 
van het management en, waar van toepassing, de personen belast met governance evalueert. 
Voorbeelden zijn  omstandigheden wanneer: 
 
• 
de auditor vermoedt of informatie heeft over de betrokkenheid of vermeende betrokkenheid 
van het management en, waar van toepassing, de personen belast met governance in elke 
geïdentificeerde of vermoede niet-naleving. 
• 
de auditor zich ervan bewust is dat het management en, waar van toepassing, de personen 
belast met governance kennis hebben van een dergelijke niet-naleving en, in tegenstelling 
tot door wet- of regelgeving gestelde vereisten, de aangelegenheid niet hebben 
gerapporteerd of rapportage hiervan hebben geautoriseerd aan een bevoegde instantie 
binnen een redelijke periode. 
 
A25. In bepaalde omstandigheden kan de auditor het teruggeven van de opdracht overwegen, indien 
de wet- of regelgeving dit toestaat bijvoorbeeld wanneer het management of de met governance 
belaste personen niet de corrigerende actie onderneemt (ondernemen) die de auditor in de 
gegeven omstandigheden passend acht, of de geïdentificeerde of vermoede niet-naleving vragen 
oproept met betrekking tot de integriteit van het management of de personen belast met 
governance, zelfs wanneer niet-naleving niet van materieel belang is voor de financiële 
overzichten. De auditor kan overwegen of het gepast is juridisch advies in te winnen om te 
bepalen of teruggeven van de opdracht gepast is. Wanneer de auditor bepaalt dat het teruggeven 
van de opdracht passend is, ontslaat dit hem niet van het naleven van andere 
verantwoordelijkheden onder wet- of regelgeving of relevante ethische voorschriften om in te 
spelen op geïdentificeerde of vermoede niet-naleving. Verder geeft paragraaf A55 van ISA 220 
(herzien)14 aan dat sommige ethische voorschriften van de voorgaande auditor, op verzoek van 
de voorgestelde opvolgende auditor, kunnen vereisen om informatie te verschaffen met 
betrekking tot niet-naleving van wet- en regelgeving aan de opvolgende auditor. 
 
Het communiceren en rapporteren van geïdentificeerde of vermoede niet-naleving 
 
Potentiële implicaties van geïdentificeerde of vermoede niet-naleving voor de controleverklaring (Zie 
par. 26-28) 
 
A26. Geïdentificeerde of vermoede niet-naleving van wet- en regelgeving wordt gecommuniceerd in 
de controleverklaring wanneer de auditor het oordeel aanpast in overeenstemming met 
paragrafen 26-28. In bepaalde andere omstandigheden, kan de auditor geïdentificeerde of 
vermoede niet-naleving van wet- en regelgeving communiceren in de controleverklaring, 
bijvoorbeeld: 
 
• 
wanneer 
de 
auditor 
andere 
rapporteringsverplichtingen 
heeft, 
naast 
zijn 
verantwoordelijkheid overeenkomstig de Internationale Controlestandaarden, zoals 
beschouwd in paragraaf 43 van ISA 700.  
• 
wanneer de auditor bepaalt dat de geïdentificeerde of vermoede niet-naleving van wet- en 
regelgeving een kernpunt van de controle is en bijgevolg de aangelegenheid in 
overeenstemming met ISA 70115 communiceert, tenzij paragraaf 14 van die ISA van 
toepassing is; of 
• 
In uitzonderlijke gevallen wanneer het management of de personen belast met governance 
niet de corrigerende maatregelen nemen die de auditor gepast acht in de omstandigheden 
en teruggeven van de opdracht niet mogelijk is (zie paragraaf A25), kan de auditor 
overwegen om de geïdentificeerde of vermoede niet-naleving van wet- en regelgeving te 
 
14  ISA 220 (herzien), Kwaliteitsmanagement voor een controle van financiële overzichten. 
15  ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijke auditor.

ISA 250 (herzien) 
NBA-IBR 2023 
 
16/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
beschrijven in een paragraaf inzake overige aangelegenheden in overeenstemming met 
ISA 706.16 
 
A27. Wet- of regelgeving kan openbaarmaking door hetzij management, de personen belast met 
governance of de auditor van een specifieke aangelegenheid beletten. Wet- of regelgeving kan 
specifiek een communicatie of andere actie verbieden, die een onderzoek van een bevoegde 
instantie naar een daadwerkelijke of vermoede illegale handeling zou kunnen schaden, inclusief 
een verbod om de entiteit hierop te attenderen. Wanneer de auditor van plan is om 
geïdentificeerde of vermoede niet-naleving in de controleverklaring te communiceren onder de 
omstandigheden uiteengezet in paragraaf A26 of anderszins, kan dergelijke wet-of regelgeving 
implicaties hebben voor de mogelijkheid van de auditor om de aangelegenheid in de 
controleverklaring te beschrijven, of in bepaalde omstandigheden om de controleverklaring uit te 
brengen, In dergelijke gevallen kan de auditor overwegen om juridisch advies in te winnen om de 
passende te ondernemen actie te bepalen. 
 
Het rapporteren van geïdentificeerde of vermoede niet-naleving aan een bevoegde instantie buiten de 
entiteit (Zie par. 29) 
 
A28. Het rapporteren van geïdentificeerde of vermoede niet-naleving aan een bevoegde instantie 
buiten de entiteit kan vereist worden of geschikt zijn in de omstandigheden omdat: 
 
(a) 
wet- of regelgeving of relevante ethische voorschriften van de auditor vereisen om te 
rapporteren (Zie par. A29): 
(b) 
de auditor bepaald heeft dat rapporteren een passende actie is om in te spelen op 
geïdentificeerde of vermoede niet-naleving in overeenstemming met relevante ethische 
voorschriften (Zie par. A30): of 
(c) 
wet- of regelgeving of relevante ethische voorschriften de auditor het recht verschaffen om 
dit te doen (Zie par. A31). 
 
A29. In bepaalde rechtsgebieden, kan van de auditor vereist zijn door wet- of regelgeving of relevante 
ethische voorschriften om geïdentificeerde of vermoede niet-naleving aan een bevoegde instantie 
buiten de entiteit te rapporteren. In bepaalde rechtsgebieden bestaan bijvoorbeeld vereisten op 
grond van wetgeving voor de auditor van een financiële instelling om gevallen, of vermoede 
gevallen van niet-naleving van wet- en regelgeving aan een toezichthoudende instantie te 
rapporteren.  Afwijkingen kunnen ook ontstaan door niet-naleving van wet-of regelgeving en in 
sommige rechtsgebieden kan van de auditor vereist zijn om afwijkingen aan een bevoegde 
instantie te rapporteren in gevallen waar het management of de personen belast met governance 
falen om correctieve actie te ondernemen. 
 
A30. In andere gevallen kunnen de relevante ethische voorschriften van de auditor vereisen om te 
bepalen of het rapporteren van geïdentificeerde of vermoede niet-naleving van wet- en 
regelgeving aan een bevoegde instantie buiten de entiteit een passende actie is in de 
omstandigheden. De IESBA Code vereist bijvoorbeeld van de auditor om stappen te ondernemen 
om in te spelen op geïdentificeerde of vermoede niet-naleving van wet- en regelgeving en om te 
bepalen of verdere actie nodig is, hetgeen rapportage aan een bevoegde instantie buiten de 
entiteit kan omvatten.17 De IESBA Code legt uit dat een dergelijke rapportage niet zou worden 
beschouwd als een schending van de geheimhoudingsplicht onder de IESBA Code.18 
 
A31. Zelfs als wet- of regelgeving of relevante ethische voorschriften geen vereisten omvatten die het 
rapporteren van geïdentificeerde of vermoede niet-naleving adresseren, kunnen zij de auditor het 
recht verschaffen om geïdentificeerde of vermoede niet-naleving aan een bevoegde instantie 
buiten de entiteit te rapporteren. De auditor kan bijvoorbeeld wanneer hij de financiële overzichten 
 
16  ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen over overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor. 
17  Zie bijvoorbeeld Sectie 225.29 en Secties 225.33–225.36 van de IESBA Code. 
18  Zie bijvoorbeeld Sectie 140.7 en Sectie 225.35 van de IESBA Code.

ISA 250 (herzien) 
NBA-IBR 2023 
 
17/17 
Originele bron: Handbook of International Quality Control, Review, Other Assurance, and Related Services 
Pronouncements, 2021 Edition Volume  
 
Versie 2023 
 
van financiële instellingen controleert, het recht hebben onder wet-of regelgeving om 
aangelegenheden zoals geïdentificeerde of vermoede niet-naleving van wet- en regelgeving met 
een toezichthoudende instantie te bespreken. 
 
A32. In andere omstandigheden kan het rapporteren van geïdentificeerde of vermoede niet-naleving 
van wet- en regelgeving aan een bevoegde instantie buiten de entiteit verhinderd worden door 
de geheimhoudingsplicht van de auditor op grond van wet- of regelgeving of relevante ethische 
voorschriften. 
 
A33. De bepaling vereist door paragraaf 29 kan complexe overwegingen en professionele 
oordeelsvormingen omvatten. Bijgevolg kan de auditor overwegen om intern te consulteren (bijv. 
binnen het kantoor of een kantoor die deel uitmaakt van het netwerk) of op een vertrouwelijke 
basis met een regelgever of toezichthouder of beroepsorganisatie (tenzij dit op grond van wet- of 
regelgeving verboden is of de geheimhoudingsplicht zou schenden). De auditor kan ook 
overwegen om juridisch advies in te winnen om de opties van de auditor en de professionele of 
juridische implicaties van het ondernemen van een bepaalde actie te begrijpen.  
 
Overwegingen die specifiek voor entiteiten in de publieke sector gelden 
 
A34. Een auditor van de publieke sector kan de verplichting hebben om geïdentificeerde of vermoede 
niet-naleving te rapporteren aan de wetgever of een andere bevoegde instantie dan wel om deze 
gevallen in de controleverklaring te rapporteren. 
 
Documentatie (Zie par. 30) 
 
A35. De documentatie van de auditor van de bevindingen omtrent geïdentificeerde of vermoede niet-
naleving van wet- en regelgeving kan bijvoorbeeld omvatten: 
 
• 
kopieën van vastleggingen of documenten; 
• 
notulen van besprekingen met het management, met de met governance belaste personen 
of met partijen buiten de entiteit. 
 
A36. Wet- 
of 
regelgeving 
of 
relevante 
ethische 
voorschriften 
kunnen 
ook 
additionele 
documentatievereisten met betrekking tot geïdentificeerde of vermoede niet-naleving van wet- en 
regelgeving uiteenzetten.19 
 
 
 
19  Zie bijvoorbeeld sectie 225.37 van de IESBA Code.