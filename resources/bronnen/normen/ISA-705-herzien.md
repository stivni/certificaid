---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 705 (herzien) — Aanpassingen van het oordeel in de controleverklaring van
  de onafhankelijke auditor
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-705-(herzien)_nl_2023.pdf
    sha256: 1383ba94823f9d9bddfaaa82b92037132344843d979eb5094f554b8453c243f7
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
title: ISA 705 (herzien) — Aanpassingen van het oordeel in de controleverklaring van
  de onafhankelijke auditor
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 705 (herzien) — Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-705-(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `1383ba94823f9d9bddfaaa82b92037132344843d979eb5094f554b8453c243f7`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard 705 (herzien) 
ISA 705 (herzien)  
 
Aanpassingen van het oordeel in 
de controleverklaring van de 
onafhankelijke auditor

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
 
ISA 705 (herzien) 
NBA-IBR 2022 
2/31 
 
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
de Internationale controlestandaard (ISA) 705 (herzien) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 
705 (herzien) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 705 (herzien) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 705 (herzien) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 705 (Revised), Modifications to the Opinion in the 
Independent Auditor’s Report. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, 
and Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
 
ISA 705 (herzien) 
NBA-IBR 2022 
3/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
INTERNATIONALE CONTROLESTANDAARD 705 (HERZIEN) 
AANPASSINGEN VAN HET OORDEEL IN DE 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
(Van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten) (*) 
 
(*) Deze ISA bevat overeenstemmingswijzigingen die voortvloeien uit de herziene ISA’s 220, 250, 315 
en 540 en de normen ISQM 1 en 2. De inwerkingtreding van deze wijzigingen valt samen met deze 
normen (voor de verslagperiode die op of na 15 december aanvangen) 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ...........................................................................................................  1 
Soorten aangepaste oordelen .............................................................................................................. 2 
Ingangsdatum .................................................................................................................................................. 3 
Doelstelling........................................................................................................................................  4 
Definities ................................................................................................................................................... 5 
Vereisten 
Omstandigheden waarbij een aanpassing van het oordeel van de auditor vereist is .......................... 6 
Het bepalen van het soort aanpassing van het oordeel van de auditor ......................................... 7-15 
Vorm en inhoud van de controleverklaring indien het oordeel wordt aangepast ......................... 16-29 
Communicatie met de met governance belaste personen ................................................................  30 
Toepassingsgerichte en overige verklarende teksten 
Soorten aangepaste oordelen ........................................................................................................... A1 
Aard van afwijkingen van materieel belang ............................................................................... A2-A12 
Het bepalen van het soort aanpassing van het oordeel van de auditor .................................. A13-A16 
Vorm en inhoud van de controleverklaring indien het oordeel wordt aangepast .................... A17-A26 
Communicatie met de met governance belaste personen .............................................................. A27 
 
Bijlage 1: Voorbeelden van controleverklaringen met aanpassingen van het oordeel 
 
International Standard on Auditing (ISA) 705 (herzien), Communicatie met de met governance belaste 
personen, moet worden gelezen in samenhang met ISA 200, Algehele doelstellingen van de 
onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de International 
Standards on Auditing.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
4/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Inleiding 
 
Toepassingsgebied van deze ISA 
  
1. 
Deze ISA behandelt de verantwoordelijkheid van de auditor om een passende verklaring af te 
geven in omstandigheden waarin de auditor, bij het vormen van een oordeel overeenkomstig ISA 
700 (herzien)1, tot de conclusie komt dat een aanpassing van het oordeel van de auditor over de 
financiële overzichten noodzakelijk is. Deze ISA behandelt ook hoe de vorm en inhoud van de 
controleverklaring wordt beïnvloed als de auditor een aangepast oordeel tot uitdrukking brengt. 
In alle gevallen zijn de rapportagevereisten van ISA 700 (herzien) van toepassing en worden deze 
niet herhaald in deze ISA, tenzij ze expliciet worden behandeld of aangepast door de vereisten 
van deze ISA. 
 
Soorten aangepaste oordelen  
 
2. 
Deze ISA stelt drie soorten aangepaste oordelen vast: een oordeel met beperking, een afkeurend 
oordeel en een oordeelonthouding. De beslissing welke soort aangepast oordeel passend is, 
hangt af van: 
  
(a) 
De aard van de aangelegenheid die tot de aanpassing leidt, dat wil zeggen de vraag of de 
financiële overzichten een afwijking van materieel belang bevatten of, in het geval van een 
onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen, mogelijk een 
afwijking van materieel belang bevatten; en 
(b) 
De oordeelsvorming van de auditor over de diepgaande invloed van de gevolgen of 
mogelijke gevolgen van de aangelegenheid op de financiële overzichten. (Zie par. A1) 
 
Ingangsdatum 
 
3. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten.  
 
Doelstelling 
 
4. 
De doelstelling van de auditor is het duidelijk tot uitdrukking brengen van een op passende wijze 
aangepast oordeel over de financiële overzichten dat noodzakelijk is als: 
 
(a) 
De auditor op basis van de verkregen controle-informatie tot de conclusie komt dat de 
financiële overzichten als geheel een afwijking van materieel belang bevatten; of 
(b) 
De auditor niet in staat is voldoende en geschikte controle-informatie te verkrijgen om te 
concluderen dat de financiële overzichten als geheel geen afwijking van materieel belang 
bevatten. 
 
Definities 
 
5. 
Voor de toepassing van de ISA en hebben de volgende termen de hierna weergegeven betekenis:  
 
(a) 
Met een diepgaande invloed – Een term die binnen de context van afwijkingen wordt 
gebruikt voor het beschrijven van de gevolgen voor de financiële overzichten van 
afwijkingen of van de mogelijke gevolgen voor de financiële overzichten van eventuele 
afwijkingen die niet zijn gedetecteerd als gevolg van de onmogelijkheid om voldoende en 
geschikte controle-informatie te verkrijgen. Gevolgen met een diepgaande invloed op de 
financiële overzichten zijn die welke, op grond van de oordeelsvorming van de auditor: 
 
1  
ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
5/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
 
(i) 
Niet beperkt zijn tot specifieke elementen, rekeningen of posten van de financiële 
overzichten;  
(ii) 
Indien ze wel daartoe beperkt zijn, een substantieel deel van de financiële 
overzichten vertegenwoordigen of zouden kunnen vertegenwoordigen; of  
(iii) 
Met betrekking tot toelichtingen, van fundamenteel belang zijn voor het begrip van 
gebruikers van de financiële overzichten. 
 
(b) 
Aangepast oordeel – Een oordeel met beperking, een afkeurend oordeel of een 
oordeelonthouding bij de financiële overzichten. 
 
Vereisten 
 
Omstandigheden waarin een aanpassing van het oordeel van de auditor vereist is 
 
6. 
De auditor dient het oordeel in de controleverklaring aan te passen wanneer: 
 
(a) 
Hij op basis van de verkregen controle-informatie tot de conclusie komt dat de financiële 
overzichten als geheel een afwijking van materieel belang bevatten; of (Zie par. A2-A7) 
(b) 
De auditor niet in staat is voldoende en geschikte controle-informatie te verkrijgen om te 
concluderen dat de financiële overzichten als geheel geen afwijking van materieel belang 
bevatten. (Zie par. A8-A12) 
 
Het bepalen van het soort aanpassing van het oordeel van de auditor 
  
Oordeel met beperking 
 
7. 
De auditor dient een oordeel met beperking tot uitdrukking te brengen wanneer: 
 
(a) 
Hij, nadat hij voldoende en geschikte controle-informatie heeft verkregen, tot de conclusie 
komt dat afwijkingen afzonderlijk of gezamenlijk van materieel belang zijn voor, maar geen 
diepgaande invloed hebben op, de financiële overzichten; of  
(b) 
Hij niet in staat is voldoende en geschikte controle-informatie te verkrijgen om daarop zijn 
oordeel te baseren maar tot de conclusie komt dat de mogelijke gevolgen van eventuele 
niet-gedetecteerde afwijkingen voor de financiële overzichten van materieel belang kunnen 
zijn maar geen diepgaande invloed kunnen hebben. 
 
Afkeurend oordeel  
 
8. 
De auditor dient een afkeurend oordeel tot uitdrukking te brengen als hij, nadat hij voldoende en 
geschikte controle-informatie heeft verkregen, tot de conclusie komt dat afwijkingen afzonderlijk 
of gezamenlijk zowel van materieel belang zijn voor, als een diepgaande invloed hebben op, de 
financiële overzichten.  
 
Oordeelonthouding 
 
9. 
De auditor dient een oordeelonthouding te formuleren als hij niet in staat is voldoende en 
geschikte controle-informatie te verkrijgen om daarop zijn oordeel te baseren en de auditor tot de 
conclusie komt dat de mogelijke gevolgen van eventuele niet-gedetecteerde afwijkingen voor de 
financiële overzichten zowel van materieel belang kunnen zijn als een diepgaande invloed 
zouden kunnen hebben. 
 
10. 
De auditor dient een oordeelonthouding te formuleren als, in uiterst zeldzame omstandigheden 
waarin meerdere onzekerheden meespelen, hij tot de conclusie komt dat, ondanks het feit dat hij

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
6/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
voldoende en geschikte controle-informatie heeft verkregen met betrekking tot elk van de 
afzonderlijke onzekerheden, het niet mogelijk is een oordeel over de financiële overzichten te 
vormen vanwege de mogelijke interactie tussen de onzekerheden en het mogelijke cumulatieve 
effect ervan op de financiële overzichten.  
 
Gevolgen van de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen vanwege 
een door het management opgelegde beperking nadat de auditor de opdracht heeft aanvaard 
 
11. 
Als de auditor na het aanvaarden van de opdracht zich ervan bewust wordt dat het management 
een beperking in de reikwijdte van de controle heeft opgelegd die volgens de auditor waarschijnlijk 
zal leiden tot de noodzaak om een oordeel met beperking tot uitdrukking te brengen of om een 
oordeelonthouding over de financiële overzichten te formuleren, dient de auditor het management 
te verzoeken de beperking op te heffen. 
 
12. 
Indien het management de in paragraaf 11 van deze ISA genoemde beperking weigert op te heffen, 
dient de auditor deze aangelegenheid mee te delen aan de met governance belaste personen, 
tenzij alle met governance belaste personen betrokken zijn bij het leiden van de entiteit2, en dient 
hij na te gaan of het mogelijk is alternatieve werkzaamheden uit te voeren teneinde voldoende en 
geschikte controle-informatie te verkrijgen. 
 
13. 
Indien de auditor niet in staat is voldoende en geschikte controle-informatie te verkrijgen, dient hij 
de implicaties hiervan als volgt te bepalen: 
 
(a) 
Indien de auditor tot de conclusie komt dat de mogelijke gevolgen van eventuele niet-
gedetecteerde afwijkingen voor de financiële overzichten van materieel belang zouden 
kunnen zijn maar geen diepgaande invloed zouden kunnen hebben, dient hij een oordeel 
met beperking tot uitdrukking te brengen; of 
(b) 
Indien de auditor tot de conclusie komt dat de mogelijke gevolgen van eventuele niet-
gedetecteerde afwijkingen voor de financiële overzichten zowel van materieel belang 
zouden kunnen zijn als een diepgaande invloed zouden kunnen hebben zodat een oordeel 
met beperking niet adequaat zou zijn om de ernst van de situatie over te brengen, dient hij: 
  
(i) 
De controleopdracht terug te geven, indien dit overeenkomstig de van toepassing 
zijnde wet- of regelgeving praktisch uitvoerbaar en mogelijk is; of (Zie par. A13) 
(ii) 
Indien het teruggeven van de controleopdracht vóór het uitbrengen van de 
controleverklaring niet praktisch uitvoerbaar of mogelijk is, een oordeelonthouding 
over de financiële overzichten te formuleren. (Zie par. A14) 
 
14. 
Indien de auditor de controleopdracht teruggeeft zoals beschreven in paragraaf 13(b)(i), dient hij, 
alvorens hij de opdracht teruggeeft, alle aangelegenheden met betrekking tot tijdens de controle 
geïdentificeerde afwijkingen die tot een aanpassing van het oordeel zouden hebben geleid aan 
de met governance belaste personen mee te delen. (Zie par. A15) 
 
Andere overwegingen met betrekking tot een afkeurend oordeel of oordeelonthouding 
 
15. 
Als de auditor het noodzakelijk acht een afkeurend oordeel of een oordeelonthouding over de 
financiële overzichten als geheel tot uitdrukking te brengen, dient de controleverklaring niet 
tevens een goedkeurend oordeel met betrekking tot hetzelfde stelsel inzake financiële 
verslaggeving over een enkel financieel overzicht of over een of meer specifieke elementen, 
rekeningen of posten van een financieel overzicht te bevatten. In deze omstandigheden zou het 
 
2  
ISA 260 (herzien), Communicatie met de met governance belaste personen, paragraaf 13

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
7/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
opnemen van een dergelijk goedkeurend oordeel in dezelfde verklaring3 in tegenspraak zijn met 
het afkeurend oordeel of de oordeelonthouding van de auditor over de financiële overzichten als 
geheel. (Zie par. A16). 
 
Vorm en inhoud van de controleverklaring indien het oordeel wordt aangepast 
 
Oordeel van de auditor  
 
16. 
Als de auditor het controleoordeel aanpast, dient hij voor de oordeelsectie de titel Ons oordeel 
met beperking, Ons afkeurend oordeel of Onze oordeelonthouding, naargelang passend, te 
hanteren. (Zie par. A17-A19) 
 
Oordeel met beperking 
 
17. 
Als de auditor vanwege een afwijking van materieel belang in de financiële overzichten een 
oordeel met beperking tot uitdrukking brengt, dient hij te vermelden dat naar zijn oordeel, 
uitgezonderd de gevolgen van de aangelegenheid (aangelegenheden) beschreven in de sectie  
 
Onderbouwing van ons oordeel met beperking: 
 
(a) 
Als de verslaggeving in overeenstemming is met een getrouw-beeld-stelsel, de 
bijgevoegde financiële overzichten, in alle van materieel belang zijnde opzichten, een 
getrouwe weergave vormen (of een getrouw beeld geven) in overeenstemming met het 
van toepassing zijnde stelsel inzake financiële verslaggeving; of 
(b) 
Als de verslaggeving in overeenstemming is met een compliance-stelsel, de bijgevoegde 
financiële overzichten in alle van materieel belang zijnde opzichten zijn opgesteld in 
overeenstemming met het van toepassing zijnde stelsel inzake financiële verslaggeving.  
 
Als de aanpassing het gevolg is van de onmogelijkheid om voldoende en geschikte controle-
informatie te verkrijgen, dient de auditor de overeenkomstige formulering ‘uitgezonderd de 
mogelijke gevolgen van de aangelegenheid (aangelegenheden) ...‘ te gebruiken voor het 
aangepaste oordeel. (Zie par. A20) 
 
Afkeurend oordeel 
 
18. 
Als de auditor een afkeurend oordeel tot uitdrukking brengt, dient hij te vermelden dat, naar zijn 
oordeel, vanwege het belang van de aangelegenheid (aangelegenheden) beschreven in de sectie  
 
Onderbouwing van ons afkeurend oordeel: 
 
(a) 
Als de verslaggeving in overeenstemming is met een getrouw-beeld-stelsel, de 
bijgevoegde financiële overzichten geen getrouwe weergave vormen (of geen getrouw 
beeld geven) in overeenstemming met het van toepassing zijnde stelsel inzake financiële 
verslaggeving; of  
(b) 
Als de verslaggeving in overeenstemming is met een compliance-stelsel, de bijgevoegde 
financiële overzichten niet in alle van materieel belang zijnde opzichten zijn opgesteld in 
overeenstemming met [het van toepassing zijnde stelsel inzake financiële verslaggeving].  
 
Oordeelonthouding 
 
 
3  
ISA 805, Bijzondere overwegingen - Controles van een enkel financieel overzicht en controles van specifieke elementen, 
rekeningen of posten van een financieel overzicht, behandelt omstandigheden waarin de auditor de opdracht krijgt een 
afzonderlijk oordeel over een of meer elementen, rekeningen of posten van een financieel overzicht tot uitdrukking te brengen.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
8/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
19. 
Als de auditor een oordeelonthouding formuleert vanwege de onmogelijkheid om voldoende en 
geschikte controle-informatie te verkrijgen, dient hij:  
 
(a) 
te vermelden dat hij geen oordeel over de bijgevoegde financiële overzichten tot 
uitdrukking brengt; 
(b) 
te vermelden dat hij, vanwege het belang van de aangelegenheid (aangelegenheden) 
beschreven in de sectie Onderbouwing van onze oordeelonthouding, niet in staat was 
voldoende en geschikte controle-informatie te verkrijgen om daarop zijn controleoordeel bij 
de financiële overzichten te baseren; en  
(c) 
de zin vereist in paragraaf 24(b) van ISA 700 (herzien), die aangeeft dat de financiële 
overzichten gecontroleerd zijn, aan te passen om te vermelden dat hij de opdracht heeft 
gekregen om de financiële overzichten te controleren. 
 
Basis voor het oordeel 
 
20. 
Wanneer de auditor het oordeel over de financiële overzichten aanpast, dient hij, naast de 
specifieke elementen die op grond van ISA 700 (herzien) vereist zijn, tevens (Zie par. A21)  
 
(a) 
De titel Basis voor ons oordeel vereist in paragraaf 28 van ISA 700 (herzien) aan te passen 
in Basis voor ons oordeel met beperking, Basis voor ons afkeurend oordeel of Basis voor 
onze oordeelonthouding naar gelang passend; en  
(b) 
Binnen deze sectie een beschrijving te geven van de aangelegenheid die leidt tot de 
aanpassing.  
 
21. 
Indien de financiële overzichten een afwijking van materieel belang bevatten die verband houdt 
met specifieke bedragen in de financiële overzichten (met inbegrip van kwantitatieve 
toelichtingen), dient de auditor in de sectie Basis voor ons oordeel een beschrijving en 
kwantificering van de financiële gevolgen van de afwijking op te nemen, tenzij dit praktisch 
onuitvoerbaar is. Indien het niet praktisch uitvoerbaar is de financiële gevolgen te kwantificeren, 
dient de auditor dit in deze sectie te vermelden. (Zie par. A22) 
 
22. 
Indien de financiële overzichten een afwijking van materieel belang bevatten die verband houdt 
met kwalitatieve toelichtingen, dient de auditor in de sectie Basis voor ons oordeel een uitleg op 
te nemen over de wijze waarop de toelichtingen een afwijking van materieel belang bevatten. 
 
23. 
Indien de financiële overzichten een afwijking van materieel belang bevatten die verband houdt 
met het niet toelichten van informatie die moet worden toegelicht, dient de auditor:  
 
(a) 
De niet-toelichting te bespreken met de met governance belaste personen;  
(b) 
In de sectie Basis voor ons oordeel de aard van de weggelaten informatie te beschrijven; 
en  
(c) 
Tenzij dit op grond van wet- of regelgeving verboden is, de weggelaten informatie op te 
nemen, mits dit praktisch uitvoerbaar is en de auditor voldoende en geschikte controle-
informatie over de weggelaten informatie heeft verkregen. (Zie par. A23) 
 
24. 
Indien de aanpassing het resultaat is van de onmogelijkheid om voldoende en geschikte controle-
informatie te verkrijgen, dient de auditor de redenen voor deze onmogelijkheid in de sectie Ons 
oordeel op te nemen. 
 
25. 
Als de auditor een oordeel met beperking of afkeurend oordeel tot uitdrukking brengt, dient de 
auditor de vermelding dat de controle-informatie voldoende en geschikt is om een basis te vormen 
voor zijn oordeel zoals vereist in paragraaf 28(d) van ISA 700 (herzien) aan te passen en, al naar 
gelang passend, te wijzigen in “oordeel met beperking” of “afkeurend oordeel”.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
9/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
26. 
Als de auditor een oordeelonthouding formuleert, dient de controleverklaring niet de elementen 
die vereist zijn in paragrafen 28(b) en 28(d) van ISA 700 (herzien) te bevatten. Die elementen 
zijn:  
 
(a) 
Een verwijzing naar de sectie van de controleverklaring waar de verantwoordelijkheden 
van de auditor zijn beschreven; en 
(b) 
Een vermelding dat de verkregen controle-informatie voldoende en geschikt is om een 
basis te verschaffen voor het oordeel van de auditor. 
 
27. 
Zelfs indien de auditor een afkeurend oordeel over de financiële overzichten tot uitdrukking heeft 
gebracht of een oordeelonthouding heeft geformuleerd, dient hij in de sectie Basis voor ons 
oordeel de redenen te beschrijven voor alle andere aangelegenheden waarvan de auditor kennis 
heeft en die een aanpassing van het oordeel zouden hebben vereist, alsmede de gevolgen 
daarvan. (Zie par. A24) 
 
Beschrijving van de verantwoordelijkheden van de auditor voor de controle van financiële overzichten 
als hij een oordeelonthouding formuleert 
 
28. 
Als de auditor een oordeelonthouding bij de financiële overzichten formuleert vanwege de 
onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen, dient hij de auditor 
beschrijving van zijn verantwoordelijkheid zoals vereist in paragrafen 39-40 van ISA 700 (herzien) 
aan te passen zodat deze alleen het volgende bevat: (Zie par. A25): 
 
(a) 
Een vermelding dat het de verantwoordelijkheid is van de auditor om een controle van de 
financiële overzichten van de entiteit uit te voeren overeenkomstig de ISA’s en om een 
controleverklaring te verstrekken; 
(b) 
Een vermelding dat echter vanwege de aangelegenheid (aangelegenheden) beschreven 
in de sectie Basis van onze oordeelonthouding de auditor niet in staat was om voldoende 
en geschikte controle-informatie te verkrijgen om daarop een controleoordeel bij de 
financiële overzichten te baseren; en  
(c) 
De vermelding van de onafhankelijkheid van de auditor en andere ethische 
verantwoordelijkheden zoals vereist op grond van paragraaf 28(c) van ISA 700 (herzien). 
 
Overwegingen wanneer de auditor een oordeelonthouding bij de financiële overzichten formuleert 
 
29. 
Tenzij vereist door wet- of regelgeving, dient de controleverklaring van de auditor geen sectie 
Kernpunten van de controle te bevatten als hij een oordeelonthouding bij de financiële overzichten 
formuleert overeenkomstig ISA 7014 of een sectie “Andere informatie” overeenkomstig ISA 720 
(herzien)5. (Zie par. A26) 
 
Communicatie met de met governance belaste personen 
 
30. 
Als de auditor verwacht het oordeel in de controleverklaring aan te passen, dient hij de 
omstandigheden die tot de verwachte aanpassing hebben geleid alsmede de voorgestelde 
formulering van de aanpassing aan de met governance belaste personen mee te delen. (Zie par. 
A27) 
 
 
**** 
 
 
 
4  
ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijke auditor, 
paragrafen 11-13. 
5  
ISA 720, De verantwoordelijkheden van de auditor met betrekking tot andere informatie.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
10/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Toepassingsgerichte en overige verklarende teksten 
 
Soorten aangepaste oordelen (Zie par. 2) 
 
A1. 
De onderstaande tabel laat zien op welke wijze de door de auditor toegepaste oordeelsvorming 
over de aard van de aangelegenheid die tot de aanpassing leidt, alsmede de mate waarin de 
gevolgen of mogelijke gevolgen voor de financiële overzichten een diepgaande invloed hebben, 
van invloed zijn op het soort oordeel dat tot uitdrukking wordt gebracht. 
 
 
 
Aard van de aangelegenheid 
die tot de aanpassing leidt 
 
De oordeelsvorming van de auditor over de diepgaande invloed 
van de gevolgen of mogelijke gevolgen voor de financiële 
overzichten 
 
Van materieel belang maar 
zonder diepgaande invloed 
 
Van materieel belang en met 
diepgaande invloed 
Financiële overzichten 
bevatten een afwijking van 
materieel belang 
 
Oordeel met beperking 
 
Afkeurend oordeel 
Onmogelijkheid om voldoende 
en geschikte controle-
informatie te verkrijgen 
 
Oordeel met beperking 
 
Oordeelonthouding 
 
Omstandigheden waarin een aanpassing van het oordeel van de auditor vereist is 
 
Aard van afwijkingen van materieel belang (Zie par. 6(a)) 
 
A2. 
ISA 700 (herzien) vereist van de auditor dat hij, teneinde een oordeel over de financiële 
overzichten te vormen, concludeert of al dan niet een redelijke mate van zekerheid is verkregen 
over de vraag of de financiële overzichten als geheel geen afwijking van materieel belang 
bevatten6. Deze conclusie houdt rekening met de evaluatie door de auditor van eventuele niet-
gecorrigeerde afwijkingen in de financiële overzichten overeenkomstig ISA 4507. 
 
A3. 
ISA 450 definieert een afwijking als een verschil tussen het gerapporteerde bedrag, de 
classificatie, de presentatie of de toelichting van een in een element financieel overzicht en het 
bedrag, de classificatie, de presentatie of de toelichting dat/die vereist is opdat het element in 
overeenstemming is met het van toepassing zijnde stelsel inzake financiële verslaggeving. 
Bijgevolg kan een afwijking van materieel belang in de financiële overzichten ontstaan met 
betrekking tot: 
 
(a) 
De geschiktheid van de geselecteerde grondslagen voor financiële verslaggeving; 
(b) 
De toepassing van de geselecteerde grondslagen voor financiële verslaggeving; of 
(c) 
De geschiktheid of adequaatheid van de in de financiële overzichten opgenomen 
toelichtingen. 
 
Geschiktheid van de geselecteerde grondslagen voor financiële verslaggeving 
 
 
6  
ISA 700 (herzien), paragraaf 11 
7  
ISA 450, Evaluatie van tijdens de controle geïdentificeerde afwijkingen, paragraaf 11.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
11/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
A4. 
Met betrekking tot de geschiktheid van de door het management geselecteerde grondslagen voor 
financiële verslaggeving kan een afwijking van materieel belang in de financiële overzichten 
bijvoorbeeld ontstaan als: 
 
(a) 
De geselecteerde grondslagen voor financiële verslaggeving niet consistent zijn met het 
van toepassing zijnde stelsel inzake financiële verslaggeving; of  
(b) 
De financiële overzichten een grondslag inzake financiële verslaggeving die betrekking 
heeft op een significant element in het overzicht van de financiële positie, het overzicht van 
gerealiseerde en niet-gerealiseerde 
resultaten, het mutatieoverzicht van het eigen 
vermogen of het kasstroomoverzicht, niet juist beschrijven; of 
(c) 
De financiële overzichten, de onderliggende transacties en gebeurtenissen niet zodanig 
weergeven of toelichten dat zij een getrouwe weergave vormen. 
 
A5. 
Stelsels inzake financiële verslaggeving bevatten vaak vereisten voor de administratieve 
verwerking en toelichting van wijzigingen in de grondslagen voor financiële verslaggeving. Als de 
entiteit haar selectie van belangrijke grondslagen voor financiële verslaggeving heeft gewijzigd, 
kan in de financiële overzichten een afwijking van materieel belang ontstaan als de entiteit niet 
aan deze vereisten heeft voldaan. 
 
Toepassing van de geselecteerde grondslagen voor financiële verslaggeving 
 
A6. 
Met betrekking tot de toepassing van de geselecteerde grondslagen voor financiële verslaggeving 
kan een afwijking van materieel belang in de financiële overzichten ontstaan: 
 
(a) 
Als het management de geselecteerde grondslagen voor financiële verslaggeving niet in 
overeenstemming met het stelsel inzake financiële verslaggeving heeft toegepast, met 
inbegrip van de situatie waarin het management de geselecteerde grondslagen voor 
financiële verslaggeving niet consistent heeft toegepast in opeenvolgende verslagperioden 
of op soortgelijke transacties en gebeurtenissen (consistentie in toepassing); of  
(b) 
Als gevolg van de methode voor de toepassing van de geselecteerde grondslagen voor 
financiële verslaggeving (bijvoorbeeld een onopzettelijke fout in de toepassing). 
 
Geschiktheid of adequaatheid van toelichtingen in de financiële overzichten 
 
A7. 
Met betrekking tot de geschiktheid of adequaatheid van toelichtingen in de financiële overzichten 
kan een afwijking van materieel belang in de financiële overzichten ontstaan als: 
 
(a) 
De financiële overzichten niet alle toelichtingen bevatten die op grond van het van 
toepassing zijnde stelsel inzake financiële verslaggeving vereist zijn; 
(b) 
De toelichtingen in de financiële overzichten niet in overeenstemming met het van 
toepassing zijnde stelsel inzake financiële verslaggeving worden gepresenteerd; of 
(c) 
De financiële overzichten niet de nodige additionele toelichtingen verschaffen om een 
getrouwe weergave te vormen die verder gaat dan de toelichtingen die specifiek vereist zijn 
op grond van het van toepassing zijnde stelsel inzake financiële verslaggeving. 
 
Paragraaf A17 van ISA 450 geeft verdere voorbeelden van afwijkingen van materieel belang in 
kwalitatieve toelichtingen die kunnen ontstaan. 
 
Aard van de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen (Zie par. 6(b)) 
 
A8. 
De onmogelijkheid van de auditor om voldoende en geschikte controle-informatie te verkrijgen 
(hetgeen ook een beperking in de reikwijdte van de controle wordt genoemd) kan voortkomen uit: 
 
(a) 
Omstandigheden waarover de entiteit geen controle heeft;

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
12/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
(b) 
Omstandigheden die verband houden met de aard of timing van de werkzaamheden van 
de auditor; of 
(c) 
Beperkingen die door het management zijn opgelegd. 
 
A9. 
De onmogelijkheid om specifieke controlewerkzaamheden uit te voeren, vormt geen beperking in 
de reikwijdte van de controle als de auditor door middel van het uitvoeren van alternatieve 
werkzaamheden voldoende en geschikte controle-informatie kan verkrijgen. Indien dat niet 
mogelijk is, zijn de vereisten van paragraaf 7(b) en 9-10 van toepassing. Door het management 
opgelegde beperkingen kunnen andere implicaties voor de controle hebben, bijvoorbeeld voor 
het inschatten door de auditor van frauderisico’s en voor het overwegen van de continuering van 
de controleopdracht. 
 
A10. Omstandigheden waarover de entiteit geen controle heeft, zijn bijvoorbeeld situaties waarin:  
 
• 
De administratieve vastleggingen van de entiteit vernietigd zijn;  
• 
De administratieve vastleggingen van een significant groepsonderdeel voor onbepaalde 
tijd door overheidsinstanties in beslag is genomen. 
 
A11. Omstandigheden die verband houden met de aard of timing van de werkzaamheden van de 
auditor, zijn bijvoorbeeld situaties waarin:  
 
• 
De entiteit verplicht is de equity-methode te gebruiken voor een geassocieerde entiteit, en 
de auditor niet in staat is voldoende en geschikte controle-informatie over de financiële 
informatie van die geassocieerde entiteit te verkrijgen om te evalueren of de equity-
methode op passende wijze is toegepast;  
• 
De timing van de aanstelling van de auditor hem verhindert om de voorraadopname bij te 
wonen; 
• 
De auditor vaststelt dat de uitvoering van alleen gegevensgerichte controles niet volstaat, 
maar de interne beheersingsmaatregelen van de entiteit niet effectief zijn. 
 
A12. Voorbeelden van de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen 
als gevolg van een door het management opgelegde beperking in de reikwijdte van de controle 
zijn situaties waarin: 
 
• 
Het management de auditor belet om de voorraadopname bij te wonen; 
• 
Het management de auditor belet om externe bevestiging van specifieke rekeningsaldi te 
verzoeken. 
 
Het bepalen van het soort aanpassing van het oordeel van de auditor 
 
Gevolg van de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen vanwege 
een door het management opgelegde beperking nadat de auditor de opdracht heeft aanvaard (Zie par. 
13(b)(i)-14) 
A13. De praktische uitvoerbaarheid van het teruggeven van een controleopdracht kan afhankelijk zijn 
van het stadium van voltooiing van de opdracht op het moment dat het management de beperking 
in de reikwijdte van de controle oplegt. Als de auditor de controle grotendeels heeft voltooid, kan 
hij besluiten om de controle voor zover als mogelijk is te voltooien, een oordeelonthouding te 
formuleren en de beperking in de reikwijdte toe te lichten in de sectie Basis voor onze 
oordeelonthouding alvorens de opdracht terug te geven. 
 
A14. In bepaalde omstandigheden is het wellicht niet mogelijk om de controleopdracht terug te geven 
als de auditor op grond van wet- of regelgeving verplicht is de controleopdracht voort te zetten. 
Dit kan het geval zijn voor een auditor die is aangesteld om de financiële overzichten van 
entiteiten in de publieke sector te controleren. Ook kan dit het geval zijn in rechtsgebieden waar

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
13/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
de auditor is aangesteld om financiële overzichten te controleren die op een specifieke periode 
betrekking hebben of waar de auditor voor een specifieke periode is aangesteld en het verboden 
is de controleopdracht terug te geven vóór de controle van die financiële overzichten is voltooid, 
respectievelijk vóór het einde van die verslagperiode. De auditor kan het ook noodzakelijk achten 
om in de controleverklaring een paragraaf inzake overige aangelegenheden op te nemen.8 
 
A15. Als de auditor tot de conclusie komt dat het noodzakelijk is de controleopdracht terug te geven 
vanwege een beperking in de reikwijdte van de controle, kan hij op grond van beroepsvereisten 
of wet- of regelgeving verplicht zijn om aangelegenheden die betrekking hebben op het 
teruggeven van de opdracht mee te delen aan regelgevers of toezichthouders of aan de 
eigenaren van de entiteit. 
 
Andere overwegingen met betrekking tot een afkeurend oordeel of oordeelonthouding (Zie par. 15) 
 
A16. Hierna volgen voorbeelden van rapporteringsomstandigheden die niet in tegenspraak zouden zijn 
met een afkeurend oordeel of oordeelonthouding van de auditor: 
 
• 
Het tot uitdrukking brengen van een goedkeurend oordeel over financiële overzichten die 
zijn opgesteld overeenkomstig een bepaald stelsel inzake financiële verslaggeving en, 
binnen dezelfde verklaring, het tot uitdrukking brengen van een afkeurend oordeel over 
dezelfde financiële overzichten overeenkomstig een ander stelsel inzake financiële 
verslaggeving9; 
• 
Het tot uitdrukking brengen van een oordeelonthouding met betrekking tot de operationele 
resultaten en kasstromen, indien relevant, en een goedkeurend oordeel met betrekking tot 
de financiële positie (zie ISA 51010). In dit geval heeft de auditor geen oordeelonthouding 
tot uitdrukking gebracht over de financiële overzichten als geheel. 
 
Vorm en inhoud van de controleverklaring indien het oordeel wordt aangepast 
 
Voorbeelden van controleverklaringen (Zie par. 16) 
 
A17. De voorbeelden 1 en 2 in de bijlage bevatten controleverklaringen met respectievelijk een oordeel 
met beperking en een afkeurend oordeel vanwege het feit dat de financiële overzichten een 
afwijking van materieel belang bevatten. 
 
A18. Voorbeeld 3 in de bijlage bevat een controleverklaring met een oordeel met beperking vanwege 
het feit dat de auditor niet in staat was voldoende en geschikte controle-informatie te verkrijgen. 
Voorbeeld 4 bevat een oordeelonthouding vanwege de onmogelijkheid om over een enkel 
element van de financiële overzichten voldoende en geschikte controle-informatie te verkrijgen. 
Voorbeeld 5 bevat een oordeelonthouding vanwege de onmogelijkheid om over meerdere 
elementen van de financiële overzichten voldoende en geschikte controle-informatie te verkrijgen. 
In elk van de twee laatstgenoemde gevallen zijn de mogelijke gevolgen van deze onmogelijkheid 
voor de financiële overzichten zowel van materieel belang als van diepgaande invloed. De 
bijlagen bij andere ISA’s die rapportagevereisten bevatten inclusief ISA 570 (herzien)11, bevatten 
ook voorbeelden van controleverklaringen met aangepaste oordelen. 
 
Oordeel van de auditor (Zie par. 16) 
 
 
8  
ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor, paragraaf A10. 
9 
Zie paragraaf A31 van ISA 700 (herzien) voor een beschrijving van deze omstandigheid. 
10 ISA 510, Initiële controleopdrachten – Beginsaldi, paragraaf 10. 
11 ISA 570 (herzien), Continuïteit.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
14/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
A19. Het aanpassen van deze titel maakt het voor de gebruiker duidelijk dat het oordeel van de auditor 
aangepast is en geeft het soort aanpassing aan. 
 
Oordeel met beperking (Zie par. 17) 
 
A20. Als de auditor een oordeel met beperking tot uitdrukking brengt, zou het niet passend zijn om in 
de sectie Ons oordeel formuleringen te gebruiken zoals ‘met de voorgaande uitleg’ of 
‘behoudens’, aangezien deze niet duidelijk of krachtig genoeg zijn. 
 
Basis voor ons oordeel (Zie par. 20-23 en 27) 
 
A21. Consistentie in de controleverklaring bevordert het begrip van gebruikers en het identificeren van 
ongewone omstandigheden wanneer deze zich voordoen. Hoewel uniformiteit in de formulering 
van een aangepast oordeel en in de beschrijving van de redenen voor de aanpassing misschien 
niet mogelijk is, is consistentie in zowel de vorm als inhoud van de controleverklaring gewenst. 
 
A22. Een voorbeeld van de financiële gevolgen van afwijkingen van materieel belang die de auditor 
kan beschrijven in de sectie Basis voor ons oordeel in de controleverklaring, is de kwantificering 
van de gevolgen voor de winstbelasting, de winst vóór belastingen, het nettoresultaat en het eigen 
vermogen indien voorraden te hoog worden opgenomen 
 
A23. Het toelichten van de weggelaten informatie in de sectie Basis voor ons oordeel is niet praktisch 
uitvoerbaar indien: 
 
(a) 
De toelichtingen niet door het management zijn opgesteld of om een andere reden niet 
meteen beschikbaar zijn voor de auditor; of 
(b) 
Op grond van de oordeelsvorming van de auditor de toelichtingen veel te omvangrijk 
zouden zijn in verhouding tot de controleverklaring. 
 
A24. Een afkeurend oordeel of een oordeelonthouding die verband houdt met een specifieke 
aangelegenheid die in de sectie Basis voor ons oordeel is beschreven, is geen rechtvaardiging 
voor het weglaten van een beschrijving van andere vastgestelde aangelegenheden die 
anderszins een aanpassing van het oordeel van de auditor zouden hebben vereist. In dergelijke 
gevallen kan de toelichting van dergelijke andere aangelegenheden waarvan de auditor kennis 
heeft, relevant zijn voor gebruikers van de financiële overzichten. 
 
Beschrijving van de verantwoordelijkheden van de auditor voor de controle van financiële overzichten 
als hij een oordeelonthouding bij de financiële overzichten formuleert (Zie par. 28) 
 
A25. Als de auditor een oordeelonthouding formuleert bij de financiële overzichten, kunnen de 
volgende vermeldingen beter gepositioneerd worden in de sectie Verantwoordelijkheden van de 
auditor voor de controle van de financiële overzichten van de controleverklaring, zoals 
geïllustreerd in voorbeelden 4-5 in de bijlage bij deze ISA: 
 
• 
De vermelding vereist in paragraaf 28(a) van ISA 700 (herzien) om aan te geven dat het 
de verantwoordelijkheid van de auditor is om een controle van de financiële overzichten 
van de entiteit uit te voeren overeenkomstig de ISA’s; en 
• 
De vermelding vereist in paragraaf 28(c) van ISA 700 (herzien) over onafhankelijkheid en 
andere ethische verantwoordelijkheden. 
 
Overwegingen wanneer de auditor een oordeelonthouding bij de financiële overzichten formuleert (Zie 
par. 29) 
A26. Het verschaffen van de redenen voor de onmogelijkheid van de auditor om voldoende en 
geschikte controle-informatie in de sectie Basis voor onze oordeelonthouding in de

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
15/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
controleverklaring verschaft nuttige informatie voor gebruikers bij het begrijpen waarom de auditor 
een oordeelonthouding bij de financiële overzichten heeft geformuleerd en kan hun verder 
behoeden voor ongepast vertrouwen hierop. Echter communicatie van andere kernpunten van 
de controle dan degene(n) die aanleiding geeft (geven) voor de oordeelonthouding, kan 
suggereren dat de financiële overzichten als geheel meer geloofwaardig zijn in relatie tot die 
aangelegenheden dan gepast zou zijn in de omstandigheden, en zou inconsistent zijn met de 
oordeelonthouding bij de financiële overzichten als geheel. Derhalve verbiedt paragraaf 29 van 
deze ISA een sectie Kernpunten van de controle op te nemen in de controleverklaring als de 
auditor een oordeelonthouding bij de financiële overzichten formuleert, tenzij wet- of regelgeving 
van de auditor vereist om kernpunten van de controle te communiceren. 
 
Communicatie met de met governance belaste personen (Zie par. 30) 
 
A27. Het bespreken met de met governance belaste personen van de omstandigheden die leiden tot 
een verwachte aanpassing van het oordeel van de auditor en van de formulering van de 
aanpassing:  
 
(a) 
Maakt het voor de auditor mogelijk om de met governance belaste personen in te lichten 
over de voorgenomen aanpassing(en) en de redenen voor (of omstandigheden van) de 
aanpassing(en);  
(b) 
Maakt het voor de auditor mogelijk om te trachten overeenstemming te bereiken met de 
met 
governance 
belaste 
personen 
over 
de 
feiten 
van 
de 
aangelegenheid 
(aangelegenheden) die aanleiding geeft (geven) tot de verwachte aanpassing(en), of om 
aangelegenheden waarover een verschil van mening met het management bestaat te 
bevestigen; en  
(c) 
Geeft de met governance belaste personen de gelegenheid, in voorkomend geval, om aan 
de auditor verdere informatie en uitleg te verschaffen over de aangelegenheid 
(aangelegenheden) die aanleiding geeft (geven) tot de verwachte aanpassing(en).

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
16/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Bijlage 
(Zie par. A17–A18, A25) 
Voorbeelden van controleverklaringen over financiële overzichten (*) 
• 
Voorbeeld 1: Een controleverklaring die een oordeel met beperking omvat als gevolg van het feit 
dat de financiële overzichten een van materieel belang zijnde afwijking bevatten. 
• 
Voorbeeld 2: Een controleverklaring die een afkeurend oordeel omvat als gevolg van het feit dat 
de geconsolideerde financiële overzichten een van materieel belang zijnde afwijking bevatten. 
• 
Voorbeeld 3: Een controleverklaring die een oordeel met beperking omvat als gevolg van de 
onmogelijkheid van de auditor om voldoende en geschikte controle-informatie te verkrijgen met 
betrekking tot een in het buitenland verworven geassocieerde deelneming. 
• 
Voorbeeld 4: Een controleverklaring die een oordeelonthouding omvat als gevolg van de 
onmogelijkheid van de auditor om voldoende en geschikte controle-informatie te verkrijgen met 
betrekking tot één enkel element van de geconsolideerde financiële overzichten. 
• 
Voorbeeld 5: Een controleverklaring die oordeelonthouding omvat als gevolg van de 
onmogelijkheid van de auditor om voldoende en geschikte controle-informatie te verkrijgen 
betreffende meerdere elementen van de financiële overzichten.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
17/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Voorbeeld 1 – Oordeel met beperking als gevolg van het feit dat de financiële overzichten 
een van materieel belang zijnde afwijking bevatten  
 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
 
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde entiteit 
waarbij gebruik wordt gemaakt van een getrouw-beeld-stelsel. De controle is geen 
groepscontrole (i.e., ISA 600 12 is niet van toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in 
ISA 21013; 
• 
Er is een afwijking in de voorraden. De afwijking wordt beschouwd als zijnde van materieel 
belang maar zonder diepgaande invloed op de financiële overzichten (i.e. een oordeel met 
beperking is passend); 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied; 
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
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van 
de met het opstellen van de financiële overzichten belaste personen; 
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
 
 
 
 
 
 
 
12  ISA 600, Bijzondere overwegingen – Controles van financiële overzichten van een groep (Inclusief de werkzaamheden van 
auditors van groepsonderdelen). 
13  ISA 210, Overeenkomen van de voorwaarden van controleopdrachten.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
18/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
Aan de aandeelhouders van Vennootschap ABC [of andere passende geaddresseerde]  
Verklaring over de controle van de financiële overzichten14 
Oordeel met beperking 
Wij hebben de financiële overzichten van vennootschap ABC (de Vennootschap) gecontroleerd, die 
bestaan uit het overzicht van de financiële positie op 31 december 20X1, het overzicht van gerealiseerde 
en niet-gerealiseerde resultaten, het mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving. 
Uitgezonderd de effecten van de aangelegenheid beschreven in de sectie ‘Basis voor ons oordeel met 
beperking’ van onze verklaring, vormen de bijhorende financiële overzichten, naar ons oordeel, in alle 
van materieel belang zijnde opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) 
van de financiële positie van de vennootschap per 31 december 20X1, en van haar financiële prestaties 
en kasstromen voor het op die datum afgesloten boekjaar, in overeenstemming met International 
Financial Reporting Standards (IFRS). 
Basis voor ons oordeel met beperking 
De voorraden van de vennootschap zijn in het overzicht van de financiële positie opgenomen tegen een 
waarde xxx. Het management heeft de voorraden niet gewaardeerd tegen de laagste waarde van 
kostprijs enerzijds en opbrengstwaarde anderzijds, maar heeft deze gewaardeerd tegen kostprijs, 
hetgeen een afwijking vormt van de International Financial Reporting Standards. De vastleggingen van 
de vennootschap geven aan dat, indien het management de voorraden zou hebben gewaardeerd tegen 
de laagste waarde van kostprijs enerzijds en opbrengstwaarde anderzijds, een bedrag van xxx zou 
vereist zijn om de voorraden af te schrijven tot hun opbrengstwaarde. Dienovereenkomstig zou de 
kostprijs van de omzet gestegen zijn met xxx, en de belastingen over de winst, de nettowinst en het 
eigen vermogen zouden gedaald zijn met respectievelijk xxx, xxx en xxx.  
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie 'Verantwoordelijkheden voor de controle van de financiële overzichten' van 
onze verklaring. Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische 
vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben 
onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. Wij 
zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is als basis voor 
ons oordeel met beperking. 
Andere informatie [of andere gepaste titel, zoals “Informatie andere dan de financiële 
overzichten en de controleverklaring over deze overzichten”]  
 
14  De subtitel “Verklaring over de controle van de financiële overzichten” is niet nodig in de omstandigheden dat de tweede 
subtitel “Verklaring betreffende overige door wet- of regelgeving gestelde eisen” niet van toepassing is.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
19/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 6 in bijlage 2 van ISA 720 (herzien). 
De laatste paragraaf van de sectie “Andere informatie” in voorbeeld 6 zal aangepast worden om het 
specifiek punt te beschrijven dat aan de basis ligt van het oordeel met beperking en dat tevens een 
impact heeft op de andere informatie.] 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. In aanvulling tot de aangelegenheid beschreven in de sectie “Basis voor ons 
oordeel met beperking”, hebben wij de hierna beschreven aangelegenheden als de in onze verklaring 
te communiceren kernpunten van onze controle vastgesteld. 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701] 
Verantwoordelijkheden van het management en de met governance van de financiële 
overzichten belaste personen15 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum] 
 
 
15  In deze voorbeelden van controleverklaringen kunnen de termen ‘management’ en ‘de met governance belaste personen’ 
worden vervangen door andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke 
rechtsgebied.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
20/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Voorbeeld 2 – Afkeurend oordeel als gevolg van het feit dat de geconsolideerde financiële 
overzichten een afwijking van materieel belang bevatten 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen:  
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een 
beursgenoteerde entiteit waarbij gebruik wordt gemaakt van een getrouw-beeld-stelsel. De 
controle is groepscontrole van een entiteit met dochtermaatschappijen (i.e., ISA 600 is van 
toepassing); 
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de 
entiteit in overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten 
zoals opgenomen in ISA 210; 
• 
De geconsolideerde financiële overzichten bevatten een afwijking van materieel belang die 
het gevolg is van het niet in de consolidatie opnemen van een dochtervennootschap. De van 
materieel belang zijnde afwijking wordt beschouwd als zijn van diepgaande invloed op de 
geconsolideerde financiële overzichten. De effecten van de afwijking op de geconsolideerde 
financiële overzichten zijn niet bepaald omdat het niet praktisch uitvoerbaar was dit te doen 
(i.e. een afkeurend oordeel is passend); 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen 
van materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de 
entiteit om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
ISA 701 is van toepassing. De auditor heeft evenwel bepaald dat er geen kernpunten van de 
controle bestaan anders dan de aangelegenheid beschreven in de sectie ‘Basis voor 
afkeurend oordeel’; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring 
en de aangelegenheid die aan de basis lag van het afkeurend oordeel over de 
geconsolideerde financiële overzichten heeft tevens een impact op de andere informatie. 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen. 
• 
Naast de controle van de geconsolideerde financiële overzichten heeft de auditor overige 
rapporteringsverplichtingen op grond van lokale wetgeving.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
21/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de geconsolideerde financiële overzichten16 
Afkeurend oordeel 
Wij hebben de geconsolideerde financiële overzichten van vennootschap ABC en haar 
dochtermaatschappijen (de Groep) gecontroleerd, die bestaan uit het geconsolideerd overzicht van de 
financiële positie op 31 december 20X1, het geconsolideerde overzicht van gerealiseerde en niet-
gerealiseerde resultaten, het geconsolideerde mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving.  
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
 
16  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
22/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie voorbeeld 7 in bijlage 2 van ISA 720 (herzien). 
De laatste paragraaf van de sectie “Andere informatie” in voorbeeld 7 zal aangepast worden om het 
specifiek punt te beschrijven dat aan de basis ligt van het oordeel met beperking en dat tevens een 
impact heeft op de andere informatie.] 
Kernpunten van onze controle 
Uitgezonderd de aangelegenheid beschreven in de sectie ‘Basis voor ons afkeurend oordeel’ hebben 
we bepaald dat er geen overige kernpunten van onze controle bestaan om te communiceren in onze 
verklaring. 
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen17 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien).] 
 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum] 
 
 
 
 
 
 
 
17  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
23/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
 
Voorbeeld 3 – Oordeel met beperking als gevolg van de onmogelijkheid van de auditor om 
voldoende en geschikte controle-informatie te verkrijgen met betrekking tot een in het 
buitenland verworven geassocieerde deelneming 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen: 
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een 
beursgenoteerde entiteit waarbij gebruik wordt gemaakt van een getrouw-beeld-stelsel. De 
controle is groepscontrole van een entiteit met dochtermaatschappijen (i.e., ISA 600 is van 
toepassing);  
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten zoals 
opgenomen in ISA 210; 
• 
De auditor was in de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen 
met betrekking tot een in het buitenland verworven geassocieerde deelneming. De mogelijke 
effecten van de onmogelijkheid tot het verkrijgen van voldoende en geschikte controle-informatie 
worden geacht van materieel belang te zijn voor, maar niet van diepgaande invloed op, de 
geconsolideerde financiële overzichten (i.e. een oordeel met beperking is passend); 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied; 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen van 
materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de entiteit 
om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien); 
• 
Kernpunten van de controle werden gecommuniceerd overeenkomstig ISA 701; 
• 
De auditor heeft alle andere informatie verkregen voor de datum van de controleverklaring en de 
aangelegenheid die aan de basis lag van het oordeel met beperking over de geconsolideerde 
financiële overzichten heeft tevens een impact op de andere informatie; 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen; 
• 
Naast de controle van de geconsolideerde financiële overzichten heeft de auditor overige 
rapporteringsverplichtingen op grond van lokale wetgeving.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
24/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
Aan: de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de geconsolideerde financiële overzichten18 
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
 
18  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
25/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
[Verslaggeving overeenkomstig ISA 720 (herzien) – zie Voorbeeld 6 in bijlage 2 van ISA 720 (herzien). 
De laatste paragraaf van de sectie “Andere informatie” in voorbeeld 6 zal aangepast worden om het 
specifiek punt te beschrijven dat aan de basis ligt van het oordeel met beperking en dat tevens een 
impact heeft op de andere informatie.] 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel over 
deze aangelegenheden. In aanvulling tot de aangelegenheid beschreven in de sectie ‘Basis voor ons 
oordeel met beperking’, hebben wij de hierna beschreven aangelegenheden als de in onze verklaring 
te communiceren kernpunten van onze controle vastgesteld. 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701] 
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen19 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum] 
 
 
 
19  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied eisen” niet 
van toepassing is.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
26/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Voorbeeld 4 – Oordeelonthouding als gevolg van de onmogelijkheid van de auditor om 
voldoende en geschikte controle-informatie te verkrijgen met betrekking tot één enkel 
element van de geconsolideerde financiële overzichten 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
• 
Controle van een volledige set van geconsolideerde financiële overzichten van een entiteit 
anders dan een beursgenoteerde entiteit waarbij gebruik wordt gemaakt van een getrouw-
beeld-stelsel. De controle is een groepscontrole van een entiteit met dochtermaatschappijen 
(i.e., ISA 600 is van toepassing); 
• 
De geconsolideerde financiële overzichten zijn opgesteld door het management van de 
entiteit in overeenstemming met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de geconsolideerde financiële overzichten 
zoals opgenomen in ISA 210; 
• 
De auditor was in de onmogelijkheid om voldoende en geschikte controle-informatie te 
verkrijgen met betrekking tot één enkel element van de geconsolideerde financiële 
overzichten. De auditor was namelijk niet in staat controle-informatie te verkrijgen over de 
financiële informatie van een investering in een joint venture die meer dan 90% 
vertegenwoordigt van de netto activa van de entiteit. De mogelijke effecten van de 
onmogelijkheid tot het verkrijgen van voldoende en geschikte controle-informatie worden 
geacht zowel van materieel belang te zijn voor, als van diepgaande invloed op, de 
geconsolideerde financiële overzichten (i.e. een oordeelonthouding is passend); 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van 
het rechtsgebied; 
• 
De met het toezicht over de geconsolideerde financiële overzichten belaste personen zijn 
verschillend van de met het opstellen van de geconsolideerde financiële overzichten belaste 
personen; 
• 
Een beperktere beschrijving van de sectie over de verantwoordelijkheden van de auditor is 
vereist; 
• 
Naast de controle van de geconsolideerde financiële overzichten heeft de auditor overige 
rapporteringsverplichtingen op grond van lokale wetgeving.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
27/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
 
Aan de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de geconsolideerde financiële overzichten20 
Oordeelonthouding 
Wij hebben opdracht gekregen om de geconsolideerde financiële overzichten van vennootschap ABC 
en haar dochtermaatschappijen (de Groep) te controleren, die bestaan uit het geconsolideerd overzicht 
van de financiële positie op 31 december 20X1, het geconsolideerde overzicht van gerealiseerde en 
niet-gerealiseerde resultaten, het geconsolideerde mutatieoverzicht van het eigen vermogen en het 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de toelichting met inbegrip van 
een overzicht van de belangrijke grondslagen voor financiële verslaggeving.  
We brengen geen oordeel over de bijgaande geconsolideerde financiële overzichten van de Groep tot 
uitdrukking. Vanwege de significantie van de aangelegenheid beschreven in de sectie ‘Basis van de 
oordeelonthouding’ van onze verklaring, zijn we niet in staat geweest om voldoende en geschikte 
controle-informatie te verkrijgen om een basis voor een controleoordeel over deze geconsolideerde 
financiële overzichten te verschaffen.  
Basis voor onze oordeelonthouding 
De investering van de Groep in zijn joint venture XYZ werd op het overzicht van de financiële positie 
van de Groep opgenomen tegen een waarde van xxx, hetgeen meer dan 90% vertegenwoordigt van de 
netto-activa van de Groep per 31 december 20X1. We werden de toegang ontzegd tot het management 
en de auditors van Vennootschap XYZ, waaronder de controledocumentatie van de auditors van 
Vennootschap XYZ. Als gevolg daarvan zijn we niet in staat geweest om te bepalen of enige 
aanpassingen noodzakelijk waren met betrekking tot het proportionele aandeel dat de Groep aanhoudt 
in de activa van Vennootschap XYZ waarover het gezamenlijke zeggenschap heeft, tot zijn 
proportioneel aandeel in de verplichtingen van Vennootschap XYZ waarvoor het gezamenlijke 
verantwoordelijkheid draagt, tot zijn proportioneel aandeel van de baten en de lasten van XYZ voor het 
boekjaar, en de elementen die het geconsolideerde mutatieoverzicht eigen vermogen en het 
geconsolideerde kasstroomoverzicht uitmaken.  
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen21 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Het is onze verantwoordelijkheid een controle van de geconsolideerde financiële overzichten van de 
Groep uit te voeren overeenkomstig de International Standards on Auditing en om een 
controleverklaring uit te brengen. Vanwege de significantie van de aangelegenheid beschreven in de 
sectie ‘Basis voor onze oordeelonthouding’ van onze verklaring, zijn we echter niet in staat geweest om 
 
20  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. 
21  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
28/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
voldoende en geschikte controle-informatie te verkrijgen om een basis voor een controleoordeel over 
deze geconsolideerde financiële overzichten te verschaffen.  
Wij zijn onafhankelijk van de Groep in overeenstemming met de ethische vereisten die relevant zijn voor 
de controle van de financiële overzichten in [rechtsgebied], en we hebben onze overige ethische 
verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 2 in ISA 700 (herzien)] 
De partner verantwoordelijk voor de controle, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [Naam] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum]

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
29/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Voorbeeld 5 – Oordeelonthouding als gevolg van de onmogelijkheid van de auditor om 
voldoende en geschikte controle-informatie te verkrijgen met betrekking tot meerdere 
elementen van de financiële overzichten 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende omstandigheden 
als veronderstelling aangenomen: 
• 
Controle van een volledige set van overzichten van een entiteit anders dan een beursgenoteerde 
entiteit waarbij gebruik wordt gemaakt van een getrouw-beeld-stelsel. (i.e., ISA 600 is niet van 
toepassing); 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in overeenstemming 
met IFRS (een stelsel voor algemene doeleinden); 
• 
De voorwaarden van de controleopdracht stemmen overeen met de beschrijving van de 
verantwoordelijkheid van het management voor de financiële overzichten zoals opgenomen in 
ISA 210; 
• 
De auditor was in de onmogelijkheid om voldoende en geschikte controle-informatie te verkrijgen 
met betrekking tot meerdere elementen van de financiële overzichten. De auditor was namelijk 
niet in staat controle-informatie te verkrijgen over de voorraden en de vorderingen van de entiteit. 
De mogelijke effecten van de onmogelijkheid tot het verkrijgen van voldoende en geschikte 
controle-informatie worden geacht zowel van materieel belang te zijn voor, als van diepgaande 
invloed op, de financiële overzichten; 
• 
De op de controle van toepassing zijnde relevante ethische vereisten zijn de vereisten van het 
rechtsgebied; 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van de met 
het opstellen van de financiële overzichten belaste personen; 
• 
Een beperktere beschrijving van de sectie over de verantwoordelijkheden van de auditor is vereist; 
• 
Naast de controle van de financiële overzichten heeft de auditor overige rapporterings-
verplichtingen op grond van lokale wetgeving.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
30/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
Aan de aandeelhouders van Vennootschap ABC [of andere passende geadresseerde]  
Verklaring over de controle van de geconsolideerde financiële overzichten22 
Oordeelonthouding 
Wij hebben opdracht gekregen om de financiële overzichten van vennootschap ABC (de 
Vennootschap) te controleren, die bestaan uit het overzicht van de financiële positie op 31 december 
20X1, het overzicht van gerealiseerde en niet-gerealiseerde resultaten, het mutatieoverzicht van het 
eigen vermogen en het kasstroomoverzicht voor het boekjaar afgesloten op die datum, evenals de 
toelichting met inbegrip van een overzicht van de belangrijke grondslagen voor financiële 
verslaggeving. 
We brengen geen oordeel over de bijgaande financiële overzichten van de Vennootschap tot 
uitdrukking. Vanwege de significantie van de aangelegenheden beschreven in de sectie ‘Basis van de 
oordeelonthouding’ van onze verklaring, zijn we niet in staat geweest om voldoende en geschikte 
controle-informatie te verkrijgen om een basis voor een controleoordeel over deze financiële 
overzichten te verschaffen.  
Basis voor onze oordeelonthouding 
We zijn pas na 31 december 20X1 aangesteld als auditors van de vennootschap en hebben derhalve 
niet de opname van de fysieke voorraad waargenomen aan het begin en het einde van het boekjaar. 
We zijn niet in staat geweest om onszelf op een andere wijze te vergewissen van de 
voorraadhoeveelheden gehouden op 31 december 20X0 en 20X1 die opgenomen zijn in het overzicht 
van de financiële positie tegen respectievelijk xxx en xxx. Verder resulteerde de introductie in 
september 20X1 van een nieuw geautomatiseerd vorderingensysteem in talrijke fouten in de 
vorderingen. Op de datum van onze verklaring, was het management nog steeds bezig met het 
herstellen van tekortkomingen in het systeem en met het corrigeren van de fouten. We zijn niet in staat 
geweest om op een andere wijze de in het overzicht van de financiële positie opgenomen vorderingen 
te confirmeren of te verifiëren voor het totale bedrag van xxx per 31 december 20X1. Als gevolg van 
deze aangelegenheden zijn wij niet in staat geweest om te bepalen of enige aanpassingen 
noodzakelijk zouden worden geacht met betrekking tot vastgelegde of niet-vastgelegde voorraden en 
vorderingen, en de elementen die de winst- en verliesrekening, het mutatieoverzicht eigen vermogen 
en het kasstroomoverzicht uitmaken. 
Verantwoordelijkheden van het management en de met governance van de financiële overzichten 
belaste personen23 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Het is onze verantwoordelijkheid een controle van de financiële overzichten van de Vennootschap uit 
te voeren overeenkomstig de International Standards on Auditing en om een controleverklaring uit te 
 
22  De subtitel “Verklaring over de controle van de financiële overzichten” is niet noodzakelijk wanneer de tweede subtitel 
“Verklaring betreffende overige door de wet- of regelgeving gestelde eisen” niet van toepassing is. 
23  Of andere bewoordingen die passend zijn in de context van het juridisch kader van het betrokken rechtsgebied.

AANPASSINGEN VAN HET OORDEEL IN DE CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
ISA 705 (herzien) 
NBA-IBR 2022 
31/31 
 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
brengen. Vanwege de significantie van de aangelegenheid beschreven in de sectie ‘Basis voor onze 
oordeelonthouding’ van onze verklaring, zijn we echter niet in staat geweest om voldoende en 
geschikte controle-informatie te verkrijgen om een basis voor een controleoordeel over deze financiële 
overzichten te verschaffen.  
Wij zijn onafhankelijk van de Vennootschap in overeenstemming met de ethische vereisten die 
relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], en we hebben onze 
overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze vereisten. 
Verklaring betreffende overige door wet- of regelgeving gestelde vereisten 
[Verslaggeving overeenkomstig ISA 700 (herzien) – zie Voorbeeld 1 in ISA 700 (herzien)] 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de Auditor]  
[Datum]