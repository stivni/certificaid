---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 810 (herzien) — Opdrachten om te rapporteren betreffende samengevatte financiële
  overzichten
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/isa-810-herzien-def.pdf
    sha256: 04c49faf609000c8dc1b1e3630822c2fcda17bc6b452f4b726038ee46575ac17
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
title: ISA 810 (herzien) — Opdrachten om te rapporteren betreffende samengevatte financiële
  overzichten
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 810 (herzien) — Opdrachten om te rapporteren betreffende samengevatte financiële overzichten

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/isa-810-herzien-def.pdf) — gedownload 2026-05-16.  
> SHA-256: `04c49faf609000c8dc1b1e3630822c2fcda17bc6b452f4b726038ee46575ac17`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationaal controlestandaard  (ISA) 
ISA 810 (herzien) 
Opdrachten om te rapporteren 
betreffende samengevatte 
financiële overzichten

Over de IAASB 
Dit document werd ontwikkeld en goedgekeurd door de International Auditing and Assurance Standards 
Board (IAASB). 
Deze IAASB ontwikkelt controle- en assurance-standaarden en leidraden voor gebruik door alle auditors 
onder een gedeeld proces voor het vaststellen van standaarden waarbij de Public Interest Oversight 
Board en de IAASB Consultative Advisory Group betrokken zijn. De Public Interest Oversight Board 
houdt toezicht op de activiteiten van de IAASB. De IAASB Consultative Advisory Group geeft inbreng 
op de ontwikkeling van standaarden en leidraden vanuit het openbaar belang. 
De doelstelling van de IAASB is om het openbaar belang te dienen door het vaststellen van controle- 
en overige standaarden van hoge kwaliteit en door het faciliteren van de convergentie van internationale 
en nationale controle- en assurance-standaarden. Daarmee verhoogt zij de kwaliteit en consistentie van 
de praktijk in de hele wereld en versterkt zij het publieke vertrouwen in het wereldwijde 
accountantsberoep. 
Copyright IFAC 
Deze Internationale controlestandaard (ISA) 800 (herzien) Bijzondere overwegingen - controles van 
financiële overzichten die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden, 
werd in 2022 in de Engelse taal gepubliceerd door de International Auditing and Assurance Standards 
Board (IAASB) van de International Federation of Accountants (IFAC). Deze ISA 800 (herzien) werd in 
2023 vertaald naar het Nederlands door de Nederlandse Beroepsorganisatie van Accountants (NBA), 
met medewerking van het Belgisch Instituut van de Bedrijfsrevisoren (IBR), en werd verspreid met 
toestemming van IFAC. Het proces voor het vertalen van de Internationale controlestandaard (ISA) 810 
(herzien) is onderzocht door IFAC en de vertaling werd uitgevoerd in overeenstemming met de Policy 
Statement de l’IFAC – Policy for Translating and Reproducing Standards published by IFAC. De 
goedgekeurde Internationale controlestandaard (ISA) 800 (herzien) is gepubliceerd door IFAC in de 
Engelse taal. IFAC aanvaardt geen verantwoordelijkheid voor de juistheid en volledigheid van de 
vertaling, noch voor handelingen die daaruit kunnen voortvloeien. 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 810 (herzien) Bijzondere 
overwegingen - controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels 
voor bijzondere doeleinden © 2022 van de International Federation of Accountants (IFAC). Alle rechten 
voorbehouden. 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 810 (herzien) Bijzondere 
overwegingen - controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels 
voor bijzondere doeleinden © 2025 van de International Federation of Accountants (IFAC). Alle rechten 
voorbehouden. 
Originele titel: International Standard on Auditing (ISA) 810 (Revised), Special Considerations—Audits 
of Financial Statements Prepared in Accordance with Special Purpose Frameworks. 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and 
Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

INTERNATIONALE CONTROLESTANDAARD 810 (HERZIEN) 
 
OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE 
SAMENGEVATTE FINANCIELE OVERZICHTEN 
 
(Van toepassing op opdrachten met betrekking tot samengevatte jaarrekeningen voor perioden die 
op of na 15 december 2016 worden afgesloten)(*) 
 
(*) De wijzigingen in de huidige Nederlandse versie van de ISA 810 ten opzichte van de vorige 
versie van 2009 hebben voornamelijk betrekking op de inhoud van het rapport dat op basis van de 
ISA 700 (herzien) is opgesteld, evenals bepaalde bepalingen uit de normen ISA 260 (herzien), 570 
(herzien), 705 (herzien) en 706 (herzien). 
 
 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA .............................................................................................................. 1 
Ingangsdatum ........................................................................................................................................ 2 
Doelstelling ................................................................................................................................................ 3 
Definities ............................................................................................................................................... 4 
Vereisten 
Aanvaarding van de opdracht ............................................................................................................. 5-7 
Aard van de werkzaamheden ................................................................................................................ 8 
Vorm van het oordeel ........................................................................................................................ 9-11 
Timing van de werkzaamheden en gebeurtenissen die plaatsvinden na de datum van de 
controleverklaring betreffende de gecontroleerde financiële overzichten ....................................... 12-13 
Informatie in documenten die samengevatte financiële overzichten bevatten  .............................. 14-15 
De controleverklaring betreffende samengevatte financiële overzichten ....................................... 16-21 
Beperking 
van 
verspreiding 
of 
gebruik 
dan 
wel 
het 
attenderen 
van 
lezers 
op 
de 
verslaggevingsgrondslagen ................................................................................................................. 22 
Vergelijke cijfers .............................................................................................................................. 23-24 
Niet gecontroleerde aanvullende informatie die wordt gepresenteerd samen met samengevatte financiële 
overzichten........................................................................................................................................... 25 
Associëren van de auditor .............................................................................................................. 26-27 
Toepassingsgerichte en overige verklarende teksten 
Aanvaarding van de opdracht ........................................................................................................ A1-A7 
Het evalueren van de beschikbaarheid van de gecontroleerde financiële overzichten ........................A8 
Vorm van het oordeel ................................................................................................................................ A9 
Timing van werkzaamheden en gebeurtenissen na de datum van de controleverklaring bij de 
gecontroleerde financiële overzichten ............................................................................................... A10 
Informatie in documenten die samengevatte financiële overzichten bevatten ........................... A11-A16 
De controleverklaring betreffende samengevatte financiële overzichten .................................... A17-A23 
Vergelijke cijfers ......................................................................................................................... A24-A25 
Niet gecontroleerde aanvullende informatie die wordt gepresenteerd samen met samengevatte financiële 
overzichten......................................................................................................................................... A26 
Associëren van de auditor ................................................................................................................. A27 
Bijlage :  
Voorbeelden van verklaringen betreffende samengevatte financiële overzichten 
 
International Standard on Auditing (ISA) 810 (herzien), Opdrachten om te rapporteren betreffende 
samengevatte financiële overzichten, moet worden gelezen in samenhang met ISA 200, Algehele 
doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig 
de International Standards on Auditing.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
4/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Inleiding 
Toepassingsgebied van deze ISA 
1. 
Deze Standaard behandelt de verantwoordelijkheden van de auditor die verband houden met 
een opdracht om te rapporteren betreffende samengevatte financiële overzichten die zijn 
afgeleid van de door diezelfde auditor overeenkomstig de ISA’s gecontroleerde financiële 
overzichten. 
Ingangsdatum 
2. 
Deze ISA is van toepassing op opdrachten met betrekking tot de samengevatte jaarekeningen 
van afgesloten perioden vanaf 15 december 2016.  
Doelstelling 
3. 
De doelstellingen van de auditor zijn: 
 
a) te bepalen of het passend is de opdracht om te rapporteren betreffende samengevatte 
financiële overzichten te aanvaarden; en 
b) indien hij de opdracht heeft om te rapporteren over samengevatte financiële overzichten: 
i) 
een oordeel te formuleren over de samengevatte financiële overzichten op basis 
van een evaluatie van de conclusies die zijn getrokken uit de verworven controle-
informatie; en 
ii) dit oordeel helder tot uitdrukking te brengen door middel van een schriftelijke 
rapportering die ook de onderbouwing voor dat oordeel beschrijft. 
Definities 
4. 
In het kader van deze ISA hebben de volgende termen de hierna weergegeven betekenissen: 
a) toegepaste criteria – De criteria die door het management worden toegepast bij het 
opstellen van samengevatte financiële overzichten. 
b) gecontroleerde financiële overzichten1 – Financiële overzichten die gecontroleerd zijn door 
de auditor overeenkomstig de ISA’s en waarvan de samengevatte financiële overzichten 
zijn afgeleid. 
c) samengevatte financiële overzichten – Historische financiële informatie die is afgeleid van 
financiële overzichten, maar die minder details bevat dan de financiële overzichten, terwijl 
zij nog steeds in een gestructureerde weergave voorziet die consistent is met de weergave 
van de economische middelen of verplichtingen die verschaft worden door de financiële 
overzichten van de entiteit op een bepaald tijdstip dan wel van de veranderingen daarin 
over een bepaalde periode.2 Verschillende rechtsgebieden kunnen verschillende 
terminologie gebruiken om dergelijke historische financiële informatie te beschrijven. 
Vereisten 
Aanvaarding van de opdracht 
5. 
De auditor dient een opdracht om te rapporteren betreffende samengevatte financiële 
overzichten overeenkomstig deze ISA alleen te aanvaarden wanneer de auditor de opdracht 
 
1 ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de 
International Standards on Auditing, paragraaf 13(f), definieert de term ‘financiële overzichten’ 
2 ISA 200, paragraaf 13(f)

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
5/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
heeft gekregen tot het uitvoeren van een controle overeenkomstig de ISA’s van de financiële 
overzichten waarvan de samengevatte financiële overzichten zijn afgeleid. (Zie Par. A1) 
6. 
Voordat de auditor een opdracht aanvaardt om te rapporteren betreffende samengevatte 
financiële overzichten, dient hij: (Zie Par. A2) 
a) te bepalen of de toegepaste criteria aanvaardbaar zijn; (Zie Par. A3, A4, A5, A6 en A7) 
b) de instemming van het management te verkrijgen dat deze zijn verantwoordelijkheid erkent 
en begrijpt: 
i) 
bij het opstellen van de samengevatte financiële overzichten in overeenstemming met 
de toegepaste criteria; 
ii) om de gecontroleerde financiële overzichten zonder onnodige problemen beschikbaar 
te stellen voor de beoogde gebruikers van de samengevatte financiële overzichten (of, 
indien wet- of regelgeving bepaalt dat de gecontroleerde financiële overzichten niet 
beschikbaar hoeven te worden gesteld voor de beoogde gebruikers van de 
samengevatte financiële overzichten en de criteria vaststelt voor het opstellen van de 
samengevatte financiële overzichten, om die wet- of regelgeving in de samengevatte 
financiële overzichten te beschrijven); alsmede 
iii) om de controleverklaring bij de samengevatte financiële overzichten op te nemen in elk 
document dat de samengevatte financiële overzichten bevat en dat aangeeft dat de 
auditor daarover heeft gerapporteerd. 
c) overeenstemming te bereiken met het management over de vorm van het oordeel dat tot 
uitdrukking moet worden gebracht bij de samengevatte financiële overzichten (Zie 
Par. 9, 10 en 11). 
7. 
Indien de auditor concludeert dat de toegepaste criteria niet aanvaardbaar zijn of indien hij niet 
in staat is om het akkoord van het management te verkrijgen zoals beschreven in paragraaf 
6(b), dient de auditor de opdracht om te rapporteren betreffende de samengevatte financiële 
overzichten niet te aanvaarden, tenzij wet- of regelgeving vereisen dit wel te doen. Een opdracht 
die wordt uitgevoerd in overeenstemming met dergelijke wet- of regelgeving voldoet niet aan 
deze ISA. Daarom dient de controleverklaring bij de samengevatte financiële overzichten niet 
te vermelden dat de opdracht is uitgevoerd in overeenstemming met deze ISA. De auditor dient 
een passende verwijzing naar dit feit op te nemen in de opdrachtvoorwaarden. De auditor dient 
eveneens het effect te bepalen dat dit mogelijk heeft op de opdracht om de financiële 
overzichten te controleren waarvan de samengevatte financiële overzichten zijn afgeleid. 
Aard van de werkzaamheden 
8. 
De auditor dient de volgende werkzaamheden uit te voeren, alsmede alle overige 
werkzaamheden die de auditor noodzakelijk acht, ter onderbouwing van zijn oordeel over de 
samengevatte financiële overzichten: 
a) evalueren of de samengevatte financiële overzichten op adequate wijze het samengevatte 
karakter daarvan uiteenzetten en de gecontroleerde financiële overzichten identificeren; 
b) wanneer samengevatte financiële overzichten niet vergezeld gaan van de gecontroleerde 
financiële overzichten, evalueren of zij duidelijk beschrijven: 
i) 
bij wie of waar de gecontroleerde financiële overzichten beschikbaar zijn; of 
ii) 
de wet- of regelgeving die specificeert dat de gecontroleerde financiële overzichten 
niet beschikbaar hoeven te worden gesteld voor de beoogde gebruikers van de 
samengevatte financiële overzichten en die de criteria vaststelt voor het opstellen 
van de samengevatte financiële overzichten. 
c) evalueren of de samengevatte financiële overzichten op adequate wijze de toegepaste 
criteria uiteenzetten;

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
6/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
d) de samengevatte financiële overzichten vergelijken met de gerelateerde informatie in de 
gecontroleerde financiële overzichten, teneinde te bepalen of de samengevatte financiële 
overzichten overeenkomen met of herberekend kunnen worden vanuit de gerelateerde 
informatie in de gecontroleerde financiële overzichten; 
e) evalueren of de samengevatte financiële overzichten zijn opgesteld in overeenstemming 
met de toegepaste criteria; 
f) 
evalueren, in het licht van het doel van de samengevatte financiële overzichten, of de 
samengevatte financiële overzichten de noodzakelijke informatie bevatten, alsmede of deze 
zich op een geschikt aggregatieniveau bevinden zodat zij onder de omstandigheden niet 
misleidend zijn; 
g) evalueren of de gecontroleerde financiële overzichten zonder onnodige problemen 
beschikbaar zijn voor de beoogde gebruikers van de samengevatte financiële overzichten, 
tenzij wet- of regelgeving bepaalt dat deze niet beschikbaar hoeven te worden gesteld en 
de criteria vaststelt voor het opstellen van de samengevatte financiële overzichten. (Zie 
Par. A8) 
Vorm van het oordeel 
9. 
Wanneer de auditor heeft geconcludeerd dan een goedkeurend oordeel over de samengevatte 
financiële overzichten passend is, dient het oordeel van de auditor, tenzij wet- of regelgeving 
anders vereist, gebruik te maken van één van de volgende bewoordingen: (Zie Par. A9) 
a) de bijgevoegde samengevatte financiële overzichten zijn in alle van materieel belang zijnde 
opzichten consistent met de gecontroleerde financiële overzichten, in overeenstemming 
met [de toegepaste criteria]; of 
b) de bijgevoegde samengevatte financiële overzichten zijn een getrouwe samenvatting van 
de gecontroleerde financiële overzichten, in overeenstemming met [de toegepaste criteria]. 
10. 
Indien wet- of regelgeving de bewoording van het oordeel over de samengevatte financiële 
overzichten voorschrijft in termen die anders zijn dan die welke beschreven zijn in paragraaf 9, 
dient de auditor: 
a) de werkzaamheden die beschreven zijn in paragraaf 8 en alle verdere werkzaamheden toe 
te passen die noodzakelijk zijn om de auditor in staat te stellen om het voorgeschreven 
oordeel tot uitdrukking te brengen; alsmede 
b) te evalueren of de gebruikers van de samengevatte financiële overzichten het oordeel van 
de auditor over de samengevatte financiële overzichten verkeerd zouden kunnen begrijpen 
en, indien dat zo is, of aanvullende toelichting in de controleverklaring betreffende de 
samengevatte financiële overzichten mogelijke misverstanden kan wegnemen. 
11. 
Indien, in het geval van paragraaf 10(b), de auditor concludeert dat aanvullende uitleg in de 
controleverklaring 
betreffende 
de 
samengevatte 
financiële 
overzichten 
mogelijke 
misverstanden niet kan wegnemen, dient de auditor de opdracht niet te aanvaarden, tenzij wet- 
of regelgeving vereist dat hij dit wel doet. Een opdracht die wordt uitgevoerd in 
overeenstemming met dergelijke wet- of regelgeving voldoet niet aan deze ISA. Daarom dient 
de controleverklaring bij de samengevatte financiële overzichten niet te vermelden dat de 
opdracht is uitgevoerd overeenkomstig deze ISA. 
 
Timing van de werkzaamheden en gebeurtenissen die plaatsvinden na de datum van de 
controleverklaring betreffende de gecontroleerde financiële overzichten 
12. 
De controleverklaring betreffende de samengevatte financiële overzichten kan van een latere 
datum zijn dan de datum van de controleverklaring bij de gecontroleerde financiële overzichten. 
In dergelijke gevallen dient de controleverklaring bij de samengevatte financiële overzichten te 
vermelden dat de samengevatte financiële overzichten en de gecontroleerde financiële

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
7/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
overzichten geen weergave zijn van de invloed van gebeurtenissen die plaatsvonden na de 
datum van de controleverklaring bij de gecontroleerde financiële overzichten. (Zie Par. A10) 
13. 
De auditor kan bewust worden van feiten die al bestonden op de datum van de 
controleverklaring betreffende de gecontroleerde financiële overzichten, maar waarvan de 
auditor voordien niet bewust was. In dergelijke gevallen dient de auditor de controleverklaring 
bij de samengevatte financiële overzichten niet uit brengen voordat de overwegingen van de 
auditor omtrent dergelijke feiten met betrekking tot de gecontroleerde financiële overzichten, 
overeenkomstig ISA 5603 is afgerond. 
Informatie in documenten die samengevatte financiële overzichten bevatten 
14. 
De auditor dient de informatie te lezen die is opgenomen in een document dat de samengevatte 
financiële overzichten en de daarbij horende controleverklaring bevat ter overweging of er alle 
van materieel belang zijnde inconsistenties zijn tussen die informatie en de samengevatte 
financiële overzichten. 
15. 
Indien de auditor een van materieel belang zijnde inconsistentie identificeert, dient de auditor 
de aangelegenheid met het management te bespreken en te bepalen of de samengevatte 
financiële overzichten of de informatie opgenomen in het document dat de samengevatte 
financiële overzichten bevat en de daarbij horende controleverklaring moeten worden herzien. 
Indien de auditor bepaalt dat de informatie moet worden herzien en het management weigert 
om de informatie te herzien zoals noodzakelijk, dient de auditor passende actie te ondernemen 
in de gegeven omstandigheden inclusief het overwegen van de implicaties voor de 
controleverklaring 
over 
de 
samengevatte 
financiële 
overzichten. 
(Zie 
Par. A11, A12, A13, A14, A15 en A16) 
De controleverklaring betreffende samengevatte financiële overzichten 
Elementen van de controleverklaring 
16. 
De controleverklaring betreffende samengevatte financiële overzichten dient de volgende 
elementen te bevatten:4 (Zie Par. A23) 
a) een titel die duidelijk aangeeft dat het de verklaring van een onafhankelijke auditor is; (Zie 
Par. A17) 
b) een geadresseerde; (Zie Par. A18) 
c) identificatie van de samengevatte financiële overzichten waarover de auditor rapporteert, 
met inbegrip van de titel van elk overzicht dat is opgenomen in de samengevatte financiële 
overzichten; (Zie Par. A19) 
d) identificatie van de gecontroleerde financiële overzichten; 
e) met toepassing van paragraaf 20, een paragraaf waarin op duidelijke wijze een oordeel tot 
uitdrukking wordt gebracht; (Zie Par. 9, 10 en 11) 
f) 
een vermelding die aangeeft dat de samengevatte financiële overzichten niet alle 
toelichtingen bevatten die vereist zijn op grond van het stelsel inzake financiële 
verslaggeving dat is toegepast bij het opstellen van de gecontroleerde financiële 
overzichten, alsmede dat het lezen van de samengevatte financiële overzichten en de 
daarbij horende controleverklaring het lezen van de gecontroleerde financiële overzichten 
en de daarbij behorende controleverklaring niet kan vervangen; 
g) waar van toepassing, de vermelding zoals vereist op grond van paragraaf 12; 
h) verwijzing naar de controleverklaring bij de gecontroleerde financiële overzichten, de datum 
van die verklaring alsmede, met toepassing van paragraaf 19 en 20, het feit dat een 
 
3 ISA 560, Gebeurtenissen na de einddatum van de verslagperiode 
4 Paragraaf 19–20, die betrekking hebben op situaties waarin het verslag van de auditor over de gecontroleerde financiële 
overzichten is aangepast, vereisen aanvullende elementen naast in deze paragraaf vermelde.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
8/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
goedkeurend oordeel tot uitdrukking is gebracht bij de gecontroleerde financiële 
overzichten; 
i) 
een beschrijving van de verantwoordelijkheid5 van het management voor de samengevatte 
financiële overzichten waarin wordt uitgelegd dat het management6 verantwoordelijk is voor 
het opstellen van de samengevatte financiële overzichten in overeenstemming met de 
toegepaste criteria; 
j) 
een vermelding dat de auditor verantwoordelijk is voor het tot uitdrukking brengen van een 
oordeel op basis van de werkzaamheden van de auditor uitgevoerd in overeenstemming 
met deze ISA, aangevend of de samengevatte financiële overzichten in alle van materieel 
belang zijnde opzichten consistent zijn met [of een getrouwe samenvatting zijn van] de 
gecontroleerde financiële overzichten; 
k) de ondertekening door de auditor; 
l) 
het adres van de auditor; 
m) de datum van de controleverklaring. (Zie Par. A20) 
17. 
Indien de geadresseerde van de samengevatte financiële overzichten niet dezelfde is als de 
geadresseerde van de controleverklaring betreffende de gecontroleerde financiële overzichten, 
dient de auditor de geschiktheid van het hanteren van een andere geadresseerde te evalueren. 
(Zie Par. A18) 
18. 
De auditor zal de controleverklaring betreffende de samengevatte financiële overzichten niet 
eerder te dateren dan: (Zie Par. A20) 
a) de datum waarop de auditor voldoende en geschikte controle-informatie heeft verworven 
om daarop het oordeel te baseren, met inbegrip van informatie waaruit blijkt dat de 
samengevatte financiële overzichten zijn opgesteld en dat degenen met de erkende 
bevoegdheid hebben verklaard dat zij de verantwoordelijkheid hiervoor op zich hebben 
genomen; alsmede 
b) de datum van de controleverklaring bij de gecontroleerde financiële overzichten. 
Verwijzing naar de controleverklaring betreffende de gecontroleerde financiële overzichten (Zie 
Par. A23) 
19. 
Wanneer de controleverklaring bij de gecontroleerde financiële overzichten het volgende 
omvat: 
a) een oordeel met beperking in overeenstemming met ISA 705 (Herzien);7 
b) een paragraaf ter benadrukking van bepaalde aangelegenheden of een paragraaf inzake 
overige aangelegenheden in overeenstemming met ISA 706 (Herzien);8 
c) een sectie Materiële onzekerheid omtrent de continuïteit in overeenstemming met ISA 570 
(Herzien);9 
d) communicatie van kernpunten van de controle in overeenstemming met ISA 700 
(Herzien) en 701;10 of 
 
5 Of een andere term die geschikt is in de context van het juridische kader in de betreffende juridictie. 
6 Of een andere term die geschikt is in de context van het juridische kader in de betreffende juridictie.  
7 ISA 705 (Herzien), Aanpassingen van het oordeel in de controleverklaring van de onafhankelijke auditor 
8 ISA 706 (Herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor 
9 ISA 570 (Herzien), Continuïteit,  paragraaf 22 
10 ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijke 
auditor

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
9/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
e) een vermelding die een niet gecorrigeerde afwijking van materieel belang betreffende de 
andere informatie in overeenstemming met ISA 720 (Herzien) beschrijft;11 
en de auditor ervan overtuigd is dat de samengevatte financiële overzichten, in alle van materieel 
belang zijnde opzichten, consistent zijn met of een getrouwe samenvatting zijn van de 
gecontroleerde financiële overzichten, in overeenstemming met de toegepaste criteria, dient de 
controleverklaring bij de samengevatte financiële overzichten, in bijkomend aan de elementen in 
paragraaf 16: 
i) 
te vermelden dat de controleverklaring bij de gecontroleerde financiële overzichten een 
oordeel met beperking omvat, een paragraaf ter benadrukking van bepaalde 
aangelegenheden, 
een 
paragraaf 
inzake 
overige 
aangelegenheden, 
een 
sectie Materiële onzekerheid omtrent de continuïteit, communicatie van materialiteit, 
reikwijdte van de groepscontrole en de kernpunten van de controle, of een vermelding 
die een niet gecorrigeerde afwijking van materieel belang betreffende de andere 
informatie beschrijft; en (Zie Par. A21) 
ii) 
te beschrijven: (Zie Par. A22) 
a. 
de basis voor het oordeel met beperking bij de gecontroleerde financiële 
overzichten en het eventuele effect daarvan op de samengevatte financiële 
overzichten; of 
b. 
de aangelegenheid waarnaar wordt verwezen in de paragraaf ter benadrukking 
van bepaalde aangelegenheden, de paragraaf inzake overige aangelegenheden 
of de Materiële onzekerheid omtrent de continuïteit in de controleverklaring 
betreffende de gecontroleerde financiële overzichten en het(de) eventuele 
effect(en) daarvan op de samengevatte financiële overzichten; of 
c. 
de niet gecorrigeerde afwijkingen van materieel belang betreffende de andere 
informatie en het(de) eventuele effect(en) daarvan op de informatie opgenomen 
in een document dat de samengevatte financiële overzichten bevat en de daarbij 
horende controleverklaring. (Zie Par. A15) 
20. 
Wanneer de controleverklaring betreffende de gecontroleerde financiële overzichten een 
afkeurend oordeel of een oordeelonthouding bevat, dient de controleverklaring bij de 
samengevatte financiële overzichten naast de in paragraaf 16 genoemde elementen: 
a) te vermelden dat de controleverklaring bij de gecontroleerde financiële overzichten een 
afkeurend oordeel of een oordeelonthouding bevat; 
b) de onderbouwing van dat afkeurende oordeel of die oordeelonthouding te beschrijven; 
alsmede 
c) te vermelden dat, als gevolg van het afkeurende oordeel of de oordeelonthouding, het niet 
passend is om een oordeel over de samengevatte financiële overzichten tot uitdrukking te 
brengen. (Zie Par. A23) 
Aangepast oordeel over de samengevatte financiële overzichten 
21. 
Indien de samengevatte financiële overzichten niet in alle van materieel belang zijnde opzichten 
consistent zijn met, dan wel geen getrouwe samenvatting zijn van de gecontroleerde financiële 
overzichten, in overeenstemming met de toegepaste criteria, en het management niet instemt 
met het maken van de noodzakelijke aanpassingen, dient de auditor een afkeurend oordeel tot 
uitdrukking te brengen over de samengevatte financiële overzichten. (Zie Par. A23) 
Beperking van verspreiding of gebruik dan wel het attenderen van lezers op de 
verslaggevingsgrondslagen 
22. 
Wanneer het verspreiden of het gebruik van de controleverklaring betreffende de 
 
11 ISA 720 (Herzien), De verantwoordelijkheden van de auditor met betrekking tot andere informatie

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
10/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
gecontroleerde financiële overzichten beperkt wordt, of de controleverklaring bij de 
gecontroleerde financiële overzichten lezers erop attendeert dat de gecontroleerde financiële 
overzichten zijn opgesteld in overeenstemming met een stelsel voor bijzondere doeleinden, 
dient de auditor een vergelijkbare beperking of attentiepunt op te nemen in de controleverklaring 
bij de samengevatte financiële overzichten. 
Vergelijkende cijfers 
23. 
Indien de gecontroleerde financiële overzichten vergelijkende cijfers bevatten maar de 
samengevatte financiële overzichten dat niet doen, dient de auditor te bepalen of een dergelijke 
weglating redelijk is in de omstandigheden van de opdracht. De auditor dient de invloed te 
bepalen van een onredelijke weglating op de controleverklaring betreffende de samengevatte 
financiële overzichten. (Zie Par. A24) 
24. 
Indien de samengevatte financiële overzichten vergelijkende cijfers bevatten waarover 
gerapporteerd werd door een andere auditor, dient de controleverklaring betreffende de 
samengevatte financiële overzichten ook de aangelegenheden te bevatten die ISA 710 van de 
auditor vereist om op te nemen in de controleverklaring bij de gecontroleerde financiële 
overzichten.12 (Zie Par. A25) 
Niet gecontroleerde aanvullende informatie die wordt gepresenteerd samen met samengevatte 
financiële overzichten 
25. 
De auditor dient te evalueren of alle niet gecontroleerde aanvullende informatie die wordt 
gepresenteerd samen met de samengevatte financiële overzichten, duidelijk wordt 
onderscheiden ten opzichte van de samengevatte financiële overzichten. Indien de auditor 
concludeert dat de presentatie van de niet gecontroleerde aanvullende informatie, door de 
entiteit niet duidelijk wordt onderscheiden ten opzichte van de samengevatte financiële 
overzichten, dient de auditor het management te verzoeken om de presentatie van de niet 
gecontroleerde aanvullende informatie te wijzigen. Indien het management weigert dit te doen, 
dient de auditor in de controleverklaring betreffende de samengevatte financiële overzichten uit 
te leggen dat dergelijke informatie niet is opgenomen in die verklaring. (Zie Par. A26) 
 
Associëren van de auditor 
26. 
Indien de auditor zich ervan bewust wordt dat de entiteit van plan is te ver melden dat de auditor 
gerapporteerd heeft over samengevatte financiële overzichten in een document dat de 
samengevatte financiële overzichten bevat, maar niet van plan is om de daarop betrekking 
hebbende controleverklaring toe te voegen, dient de auditor het management te verzoeken de 
controleverklaring aan het document toe te voegen. Indien het management dat niet doet dient 
de auditor andere passende acties te bepalen en uit te voeren die zijn opgezet om te voorkomen 
dat het management de auditor op ongepaste wijze in verband brengt met de samengevatte 
financiële overzichten in dat document. (Zie Par. A27) 
27. 
Het is mogelijk dat de auditor de opdracht heeft te rapporteren betreffende de financiële 
overzichten van een entiteit, maar niet de opdracht heeft om te rapporteren over de 
samengevatte financiële overzichten. Indien in dit geval de auditor zich ervan bewust wordt dat 
de entiteit van plan is om een vermelding op te nemen in een document dat verwijst naar de 
auditor en naar het feit dat de samengevatte financiële overzichten zijn afgeleid van de door de 
auditor gecontroleerde financiële overzichten, dient de auditor zich ervan te vergewissen dat: 
a) de verwijzing naar de auditor wordt gemaakt in de context van de controleverklaring bij de 
gecontroleerde financiële overzichten; en 
b) de vermelding niet de indruk wekt dat de auditor heeft gerapporteerd over de samengevatte 
financiële overzichten. 
 
12 ISA 710, Ter vergelijking opgenomen informatie – Overeenkomstige cijfers en vergelijkende financiële overzichten

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
11/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
 
Indien noch aan (a) noch aan (b) wordt voldaan, dient de auditor het management te verzoeken 
de vermelding zodanig te wijzigen dat die daaraan wel voldoet, dan wel in het document niet 
naar de auditor te verwijzen. Anderzijds kan de entiteit de auditor de opdracht geven om te 
rapporteren over de samengevatte financiële overzichten en om de daarop betrekking 
hebbende controleverklaring aan het document toe te voegen. Indien het management de 
vermelding niet wijzigt, de verwijzing naar de auditor niet schrapt, dan wel een 
controleverklaring over de samengevatte financiële overzichten niet toevoegt aan het document 
dat de samengevatte financiële overzichten bevat, dient de auditor het management te 
informeren dat de auditor het niet eens is met de verwijzing naar de auditor en dient de auditor 
andere passende acties te bepalen en uit te voeren die zijn opgezet om te voorkomen dat het 
management op ongepaste wijze naar de auditor verwijst. (Zie Par. A27) 
*** 
Toepassingsgerichte en overige verklarende teksten 
Aanvaarding van de opdracht (Zie Par. 5 en 6) 
A1.  
De controle van de financiële overzichten waarvan de samengevatte financiële overzichten zijn 
afgeleid verschaft de auditor de noodzakelijke kennis om zich te kwijten van zijn 
verantwoordelijkheden met betrekking tot de samengevatte financiële overzichten in 
overeenstemming met deze ISA. Het toepassen van deze ISA zal geen voldoende en geschikte 
informatie verschaffen om daarop het oordeel over de samengevatte financiële overzichten te 
baseren indien de auditor niet ook de financiële overzichten heeft gecontroleerd waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
A2.  
De instemming van het management betreffende de aangelegenheden die beschreven zijn in 
paragraaf 6 kan blijken uit de schriftelijke aanvaarding van de opdrachtvoorwaarden door het 
management. 
 
Criteria (Zie Par. 6(a)) 
A3.  
Het opstellen van samengevatte financiële overzichten vereist van het management om de 
informatie vast te stellen die dient te worden weergegeven in de samengevatte financiële 
overzichten zodat deze in alle van materieel belang zijnde opzichten consistent zijn met dan 
wel een getrouwe samenvatting zijn van de gecontroleerde financiële overzichten. Omdat 
samengevatte financiële overzichten naar hun aard geaggregeerde informatie en beperkte 
toelichting bevatten, bestaat er een verhoogd risico dat zij niet de noodzakelijke informatie 
bevatten om onder de omstandigheden niet misleidend te zijn. Dit risico neemt toe wanneer er 
geen vastgestelde criteria bestaan voor het opstellen van samengevatte financiële overzichten. 
 
A4.  
Tot factoren die van invloed kunnen zijn op het bepalen door de auditor van de 
aanvaardbaarheid van de toegepaste criteria behoren: 
• 
de aard van de entiteit; 
• 
het doel van de samengevatte financiële overzichten; 
• 
de informatiebehoeften van de beoogde gebruikers van de samengevatte financiële 
overzichten; en 
• 
de vraag of de toegepaste criteria zullen resulteren in samengevatte financiële overzichten 
die onder de gegeven omstandigheden niet misleidend zullen zijn. 
A5.  
De criteria voor het opstellen van samengevatte financiële overzichten kunnen worden 
vastgesteld door een geautoriseerde of erkende instantie die ISA’s vaststelt (standards setting 
organization) of bij wet- of regelgeving. Zoals dit het geval is voor financiële overzichten, zoals

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
12/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
uiteengezet in ISA 210,13 kan de auditor in veel van dergelijke gevallen ervan uitgaan dat 
dergelijke criteria aanvaardbaar zijn. 
 
A6.  
Wanneer er geen vastgestelde criteria bestaan voor het opstellen van samengevatte financiële 
overzichten kunnen criteria door het management ontwikkeld worden, bijvoorbeeld op basis van 
gebruik in een bepaalde sector. Criteria die onder de omstandigheden aanvaardbaar zijn, zullen 
resulteren in samengevatte financiële overzichten die: 
a) op adequate wijze hun samengevatte karakter toelichten en de gecontroleerde financiële 
overzichten identificeren; 
b) op duidelijke wijze beschrijven bij wie of waar de gecontroleerde financiële overzichten 
beschikbaar zijn dan wel, indien wet- of regelgeving erin voorziet dat de gecontroleerde 
financiële overzichten niet beschikbaar gesteld hoeven te worden voor de beoogde 
gebruikers van de samengevatte financiële overzichten en de criteria vaststelt voor het 
opstellen van samengevatte financiële overzichten, die wet- of regelgeving beschrijven; 
c) de toegepaste criteria op adequate wijze uiteenzetten; 
d) overeenkomen met of kunnen worden herrekend vanuit de daaraan gerelateerde informatie 
in de gecontroleerde financiële overzichten; alsmede 
e) in het licht van het doel van de samengevatte financiële overzichten, de noodzakelijke 
informatie bevatten alsmede zich op een geschikt aggregatieniveau bevinden zodat zij 
onder de gegeven omstandigheden niet misleidend zijn. 
A7.  
Adequate uiteenzetting van het samengevatte karakter van de samengevatte financiële 
overzichten en de aanduiding van de gecontroleerde financiële overzichten, waarnaar wordt 
verwezen in paragraaf A6(a), kan worden verschaft door bijvoorbeeld een titel 
als Samengevatte financiële overzichten opgesteld vanuit de gecontroleerde financiële 
overzichten van het jaar geëindigd op 31 december 20XX. 
 
Het evalueren van de beschikbaarheid van de gecontroleerde financiële overzichten (Zie 
Par. 8(g)) 
A8. De evaluatie van de auditor of de gecontroleerde financiële overzichten zonder onnodige problemen 
beschikbaar zijn voor de beoogde gebruikers van de samengevatte financiële overzichten, 
wordt beïnvloed door factoren zoals: 
• 
de vraag of de samengevatte financiële overzichten op duidelijke wijze beschrijven bij wie 
of waar de gecontroleerde financiële overzichten beschikbaar zijn; 
• 
de vraag of de gecontroleerde financiële overzichten openbaar zijn gemaakt; of 
• 
de vraag of het management een proces heeft vastgesteld waardoor de beoogde 
gebruikers van de samengevatte financiële overzichten rechtstreekse toegang kunnen 
verkrijgen tot de gecontroleerde financiële overzichten. 
Vorm van het oordeel (Zie Par. 9) 
A9. 
 Een conclusie gebaseerd op een evaluatie van de controle-informatie die is verkregen door het 
uitvoeren van de in paragraaf 8 genoemde werkzaamheden, dat een goedkeurend oordeel over 
de samengevatte financiële overzichten passend is, stelt de auditor in staat om een oordeel tot 
uitdrukking te brengen dat één van de bewoordingen uit paragraaf 9 bevat. De beslissing van 
de auditor over de vraag welke bewoordingen hij zal gebruiken, kan worden beïnvloed door 
 
13 ISA 210, Overeenkomen van de voorwaarden van controleopdrachten, paragraaf A3 en A8–A9

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
13/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
algemeen aanvaard gebruik in het desbetreffende rechtsgebied. 
 
Timing van werkzaamheden en gebeurtenissen na de datum van de controleverklaring bij de 
gecontroleerde financiële overzichten (Zie Par. 12) 
A10.  
De werkzaamheden die beschreven zijn in paragraaf 8 worden dikwijls uitgevoerd tijdens of 
direct na de controle van de financiële overzichten. Wanneer de auditor rapporteert betreffende 
de samengevatte financiële overzichten na het afronden van de controle van de financiële 
overzichten, wordt van de auditor niet vereist om aanvullende controle-informatie te verkrijgen 
over de gecontroleerde financiële overzichten, noch dat hij rapporteert betreffende de invloed 
van gebeurtenissen die plaatsvonden na de datum van de controleverklaring bij de 
gecontroleerde financiële overzichten, aangezien de samengevatte financiële overzichten zijn 
afgeleid van de gecontroleerde financiële overzichten en deze niet actualiseren. 
 
Informatie in documenten die samengevatte financiële overzichten bevatten (Zie Par. 14 en 15) 
A11.  
ISA 720 (Herzien) behandelt de verantwoordelijkheden van de auditor met betrekking tot andere 
informatie in een controle van financiële overzichten. In de context van ISA 720 (Herzien) is 
andere informatie financiële of niet financiële informatie (anders dan de financiële overzichten 
en de daarbij horende controleverklaring) opgenomen in het jaarverslag van een entiteit. Een 
jaarverslag bevat of gaat samen met de financiële overzichten en de daarbij horende 
controleverklaring. 
A12. 
Daarentegen behandelen paragrafen 14 en 15 de verantwoordelijkheid van de auditor met 
betrekking tot informatie opgenomen in een document dat ook de samengevatte financiële 
overzichten en de daarbij horende controleverklaring bevat. Deze informatie kan omvatten: 
• 
een deel van of alle aangelegenheden die ook behandeld zijn in de andere informatie die is 
opgenomen in het jaarverslag (bijv. wanneer de samengevatte financiële overzichten en de 
daarbij horende controleverklaring zijn opgenomen in een samengevat jaarverslag); of 
• 
aangelegenheden die niet behandeld zijn in de andere informatie opgenomen in het 
jaarverslag. 
A13.  
Bij het lezen van de informatie opgenomen in een document dat de samengevatte financiële 
overzichten en de daarbij horende controleverklaring bevat, kan de auditor zich ervan bewust 
worden dat dergelijke informatie misleidend is en kan het nodig zijn om passende actie te 
ondernemen. Relevante ethische voorschriften14 vereisen dat de auditor niet betrokken is bij of 
in verband gebracht wordt met informatie die materieel onjuist, onvolledig of misleidend is. 
 
Informatie in een document dat de samengevatte financiële overzichten omvat die een deel van of alle 
zelfde aangelegenheden als de andere informatie in het jaarverslag behandelt 
A14.  
Wanneer informatie opgenomen is in een document dat de samengevatte financiële overzichten 
en de daarbij horende controleverklaring omvat en die informatie behandelt een deel van of 
geheel dezelfde aangelegenheden als de andere informatie opgenomen in het jaarverslag, kan 
het werk dat is uitgevoerd op die andere informatie in overeenstemming met ISA 720 (Herzien) 
adequaat zijn voor de doelstellingen van paragrafen 14 en 15 van deze ISA. 
A15.  
Wanneer een niet gecorrigeerde afwijking van materieel belang van de andere informatie 
geïdentificeerd is in de controleverklaring bij de gecontroleerde financiële overzichten en die 
niet gecorrigeerde afwijking van materieel belang betrekking heeft op een aangelegenheid die 
behandeld is in de informatie in een document dat de samengevatte financiële overzichten en 
 
14 International Ethics Standards Board for Accountants’ International Code of Ethics for Professional Accountants  (IESBA Code), 
paragraaf R111.2

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
14/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
de daarbij horende controleverklaring omvat, kan er een materiële inconsistentie tussen de 
samengevatte financiële overzichten en die informatie bestaan of kan de informatie misleidend 
zijn. 
Informatie in een document dat de samengevatte financiële overzichten omvat die aangelegenheden 
behandelt die niet zijn behandeld in de andere informatie in het jaarverslag 
A16.  
ISA 720 (Herzien), aangepast waar nodig in de omstandigheden, kan nuttig zijn voor de auditor 
bij het bepalen van de passende actie om te reageren op de weigering van het management 
om de nodige wijzigingen aan te brengen in de informatie, inclusief het overwegen van de 
implicaties voor de controleverklaring betreffende de samengevatte financiële overzichten. 
 
De controleverklaring betreffende samengevatte financiële overzichten 
Elementen van de controleverklaring 
Titel (Zie Par. 16(a)) 
A17.  
Een titel die aangeeft dat de verklaring de verklaring is van een onafhankelijke auditor, 
bijvoorbeeld, Verklaring van de onafhankelijke auditor, bevestigt dat de auditor heeft voldaan 
aan alle relevante ethische voorschriften met betrekking tot onafhankelijkheid. Dit onderscheidt 
de verklaring van de onafhankelijke auditor van door anderen uitgebrachte rapportages. 
 
Geadresseerde (Zie: Par. 16(b), 17) 
A18.  
Tot factoren, die van invloed kunnen zijn op de evaluatie door de auditor van de juistheid van 
de 
geschiktheid 
van 
de 
samengevatte 
financiële 
overzichten, 
behoren 
de 
opdrachtvoorwaarden, de aard van de entiteit, alsmede het doel van de samengevatte 
financiële overzichten. 
 
Identificatie van de samengevatte financiële overzichten (Zie Par. 16(c)) 
A19.  
Wanneer de auditor zich ervan bewust is dat de samengevatte financiële overzichten zullen 
worden opgenomen in een document dat informatie anders dan de samengevatte financiële 
overzichten en de daarbij horende controleverklaring bevat, kan de auditor overwegen, indien 
de presentatievorm dit toelaat, om de paginanummers te identificeren waarop de samengevatte 
financiële overzichten worden weergegeven. Dit ondersteunt lezers bij het identificeren van de 
samengevatte financiële overzichten waarop de controleverklaring betrekking heeft. 
 
Datum van de controleverklaring (Zie Par. 16(m) en 18) 
A20.  
De persoon of personen met erkende bevoegdheid om te concluderen dat de samengevatte 
financiële overzichten zijn opgesteld en daarvoor verantwoordelijkheid te nemen, hangt/hangen 
af van de opdrachtvoorwaarden, de aard van de entiteit en het doel van de samengevatte 
financiële overzichten. 
 
Verwijzing naar de controleverklaring betreffende de financiële overzichten (Zie Par. 19) 
A21.  
Paragraaf 19(i) van deze ISA vereist van de auditor om een vermelding in de controleverklaring 
betreffende de samengevatte financiële overzichten op te nemen wanneer de controleverklaring 
betreffende de gecontroleerde financiële overzichten communicatie van kernpunten van de

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
15/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
controle in overeenstemming met ISA 701 bevat.15 Van de auditor is echter niet vereist om de 
individuele kernpunten van de controle te beschrijven in de controleverklaring betreffende de 
samengevatte financiële overzichten. 
A22.  
De vermelding(en) en beschrijving(en) zoals vereist op grond van paragraaf 19 zijn bedoeld om 
de aandacht te vestigen op die aangelegenheden en zijn geen vervanging voor het lezen van 
de controleverklaring betreffende de gecontroleerde financiële overzichten. De vereiste 
beschrijvingen zijn bedoeld om de aard van de aangelegenhe(i)d(en) duidelijk te maken en 
hoeven niet de overeenstemmende tekst in de controleverklaring betreffende de gecontroleerde 
financiële overzichten te herhalen. 
Voorbeelden (Zie Par. 16, 19, 20 en 21) 
A23.  
De bijlage bij deze ISA bevat gevarieerde voorbeelden van controleverklaringen betreffende 
samengevatte financiële overzichten die: 
a) goedkeurende oordelen bevatten; 
b) zijn afgeleid van gecontroleerde financiële overzichten waarbij de auditor aangepaste 
oordelen heeft uitgebracht; alsmede 
c) een aangepast oordeel bevatten. 
d) zijn afgeleid van gecontroleerde financiële overzichten waarbij de bijbehorende 
controleverklaring een vermelding bevat die een niet gecorrigeerde afwijking van materieel 
belang van de andere informatie in overeenstemming met ISA 720 (Herzien) beschrijft; en 
e) zijn afgeleid van gecontroleerde financiële overzichten waarbij de bijbehorende 
controleverklaring een sectie Onzekerheid van materieel belang omtrent de continuïteit en 
communicatie van andere kernpunten van de controle bevat. 
Vergelijkende cijfers (Zie Par. 23 en 24) 
A24.  
Indien de gecontroleerde financiële overzichten vergelijkende cijfers bevatten, wordt er 
verondersteld dat de samengevatte financiële overzichten eveneens vergelijkende cijfers 
zouden bevatten. Vergelijkende cijfers in de gecontroleerde financiële overzichten kunnen 
worden beschouwd als vergelijkende cijfers dan wel als ter vergelijking opgenomen financiële 
informatie. ISA 710 beschrijft hoe dit verschil van invloed is op de controleverklaring betreffende 
de financiële overzichten, met inbegrip van met name verwijzing naar andere auditors die de 
financiële overzichten over de voorgaande periode hebben gecontroleerd. 
A25.  
Omstandigheden die van invloed kunnen zijn op de bepaling van de auditor of een weglating 
van vergelijkende cijfers redelijk is, omvatten de aard en het doel van de samengevatte 
financiële overzichten, de toegepaste criteria, alsmede de informatiebehoeften van de beoogde 
gebruikers van de samengevatte financiële overzichten. 
 
Niet gecontroleerde aanvullende informatie die wordt gepresenteerd samen met samengevatte 
financiële overzichten (Zie Par. 25) 
A26.  
ISA 700 (Herzien)16 bevat vereisten en leidraden die moeten worden toegepast wanneer niet 
gecontroleerde aanvullende informatie wordt gepresenteerd samen met gecontroleerde 
financiële overzichten die, aangepast voor zover noodzakelijk in de gegeven omstandigheden, 
van dienst kunnen zijn bij het toepassen van de vereiste in paragraaf 25. 
 
 
15 ISA 701, paragraaf 13 
 
16 ISA 700 (Herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten, paragraaf 53–54

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (herzien)                                                          NBA-IBR 2025  
16/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Associëren van de auditor (Zie Par. 26 en 27) 
A27.  
Tot andere passende acties die de auditor kan ondernemen wanneer het management niet de 
actie onderneemt waartoe is verzocht, kunnen behoren het informeren van de beoogde 
gebruikers en overige bekende derde gebruikers over de ongepaste verwijzing naar de auditor. 
De handelwijze van de auditor hangt af van de wettelijke rechten en verplichtingen van de 
auditor. Derhalve kan de auditor het passend achten om juridisch advies in te winnen.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
17/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Bijlage 
(Zie Par. A23) 
Bijlage: Voorbeelden van verklaringen betreffende samengevatte financiële 
overzichten 
• 
 Voorbeeld 1: een controleverklaring over de samengevatte financiële overzichten die zijn 
opgesteld in overeenstemming met vastgestelde criteria. Over de gecontroleerde financiële 
overzichten werd een niet-aangepast oordeel tot uitdrukking gebracht. De controleverklaring over 
de samengevatte financiële overzichten is van een latere datum dan de datum van de 
controleverklaring over de financiële overzichten waarvan de samengevatte financiële 
overzichten zijn afgeleid. De controleverklaring over de gecontroleerde financiële overzichten 
bevat een sectie “Van materieel belang zijnde onzekerheid met betrekking tot continuïteit” en 
communicatie van andere kernpunten van de controle. 
• 
Voorbeeld 2: een controleverklaring over de samengevatte financiële overzichten die zijn 
opgesteld in overeenstemming met criteria die zijn ontwikkeld door het management en op 
adequate wijze in de samengevatte financiële overzichten zijn bekendgemaakt. De auditor heeft 
vastgesteld dat de toegepaste criteria aanvaardbaar zijn in de gegeven omstandigheden. Over 
de gecontroleerde financiële overzichten werd een niet-aangepast oordeel tot uitdrukking 
gebracht. De controleverklaring over de samengevatte financiële overzichten is van dezelfde 
datum als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. De controleverklaring over de gecontroleerde 
financiële overzichten bevat een vermelding die niet gecorrigeerde afwijking van materieel belang 
in de andere informatie beschrijft. De andere informatie waarop deze niet gecorrigeerde afwijking 
van materieel belang betrekking heeft, is ook informatie die is opgenomen in een document dat 
de samengevatte financiële overzichten en de controleverklaring daarover bevat. 
• 
Voorbeeld 3: een controleverklaring over de samengevatte financiële overzichten die zijn 
opgesteld in overeenstemming met criteria die zijn ontwikkeld door het management en op 
adequate wijze in de samengevatte financiële overzichten zijn bekendgemaakt. De auditor heeft 
vastgesteld dat de toegepaste criteria aanvaardbaar zijn in de gegeven omstandigheden. Over 
de gecontroleerde financiële overzichten werd een oordeel met beperking tot uitdrukking 
gebracht. De controleverklaring over de samengevatte financiële overzichten is van dezelfde 
datum als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
• 
Voorbeeld 4: een controleverklaring over de samengevatte financiële overzichten die zijn 
opgesteld in overeenstemming met criteria die zijn ontwikkeld door het management en op 
adequate wijze in de samengevatte financiële overzichten zijn bekendgemaakt. De auditor heeft 
vastgesteld dat de toegepaste criteria aanvaardbaar zijn in de gegeven omstandigheden. Over 
de gecontroleerde financiële overzichten werd een afkeurend oordeel tot uitdrukking gebracht. 
De controleverklaring over de samengevatte financiële overzichten is van dezelfde datum als de 
datum van de controleverklaring over de financiële overzichten waarvan de samengevatte 
financiële overzichten zijn afgeleid. 
• 
Voorbeeld 5: een controleverklaring over de samengevatte financiële overzichten die zijn 
opgesteld in overeenstemming met vastgestelde criteria. Over de gecontroleerde financiële 
overzichten werd een niet-aangepast oordeel tot uitdrukking gebracht. De auditor concludeert dat 
het niet mogelijk is om een niet-aangepast oordeel tot uitdrukking te brengen over de 
samengevatte financiële overzichten. De controleverklaring over de samengevatte financiële 
overzichten is van dezelfde datum als de datum van de controleverklaring over de financiële 
overzichten waarvan de samengevatte financiële overzichten zijn afgeleid.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
18/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Voorbeeld 1: 
De omstandigheden omvatten het volgende: 
• 
Een niet-aangepast oordeel over de gecontroleerde financiële overzichten van een 
beursgenoteerde entiteit werd tot uitdrukking gebracht. 
• 
Er bestaan vastgestelde criteria voor het opstellen van de samengevatte financiële 
overzichten. 
• 
De controleverklaring over de samengevatte financiële overzichten is van een latere 
datum dan de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
• 
De controleverklaring over de gecontroleerde financiële overzichten bevat een sectie 
“Van materieel belang zijnde onzekerheid met betrekking tot continuïteit”. 
• 
In de controleverklaring over de gecontroleerde financiële overzichten worden andere 
kernpunten van de controle gecommuniceerd.17 
 
 
VERKLARING VAN DE ONAFHANKELIJKE AUDITOR OVER DE SAMENGEVATTE FINANCIËLE 
OVERZICHTEN 
[Passende geadresseerde] 
Oordeel 
De samengevatte financiële overzichten, die bestaan uit de samengevatte balans per 31 december 
20X1, de samengevatte winst- en verliesrekening, het samengevatte mutatieoverzicht van het eigen 
vermogen en het samengevatte kasstroomoverzicht voor het boekjaar afgesloten op die datum, 
alsmede uit de daarop betrekking hebbende toelichtingen, zijn afgeleid van de gecontroleerde financiële 
overzichten van de vennootschap ABC voor het boekjaar afgesloten op 31 december 20X1. 
Naar ons oordeel zijn de bijhorende samengevatte financiële overzichten in alle van materieel belang 
zijnde opzichten consistent met (of een getrouwe samenvatting van) de gecontroleerde financiële 
overzichten, in overeenstemming met [omschrijf de vastgestelde criteria]. 
Samengevatte financiële overzichten 
De samengevatte financiële overzichten bevatten niet alle op grond van [omschrijf het stelsel inzake 
financiële verslaggeving dat wordt toegepast bij het opstellen van de gecontroleerde financiële 
overzichten van de vennootschap ABC] vereiste toelichtingen. Daarom kan het lezen van de 
samengevatte financiële overzichten en de controleverklaring daarover, het lezen van de 
gecontroleerde financiële overzichten en de controleverklaring daarover niet vervangen. In de 
samengevatte financiële overzichten en in de gecontroleerde financiële overzichten worden de effecten 
van gebeurtenissen die plaatsvonden na de datum van onze verklaring over de gecontroleerd financiële 
overzichten niet weergegeven. 
De gecontroleerde financiële overzichten en onze verklaring daarover 
Wij hebben een niet-aangepast controleoordeel over de gecontroleerde financiële overzichten tot 
uitdrukking gebracht in onze verklaring d.d. 15 februari 20X2. Die verklaring bevat ook: 
• 
Een sectie “Van materieel belang zijnde onzekerheid met betrekking tot continuïteit” die de aandacht 
vestigt op de in de gecontroleerde financiële overzichten opgenomen Toelichting 6.  Toelichting 6 
van de gecontroleerde financiële overzichten geeft aan dat de vennootschap ABC een nettoverlies 
heeft geleden ten belope van ZZZ gedurende het boekjaar afgesloten op 31 december 20X1, en 
 
17 Zoals uiteengezet in paragraaf 15 van ISA 701, is een van materieel belang zijnde onzekerheid met betrekking tot continuïteit, 
door haar aard, een kernpunt van de controle, maar dient deze te worden gerapporteerd in een aparte sectie van de 
controleverklaring overeenkomstig paragraaf 22 van ISA 570 (herzien).

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
19/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
dat op die datum de kortlopende schulden, de totale activa van de vennootschap ABC overschreden 
met YYY. Deze gebeurtenissen of omstandigheden, stamen met overige aangelegenheden die in 
Toelichting 6 bij de gecontroleerde financiële overzichten zijn uiteengezet, vormen een aanwijzing 
dat een van materieel belang zijnde onzekerheid bestaat die significante twijfel kan doen rijzen over 
de mogelijkheid van de vennootschap ABC om haar continuïteit te handhaven. Deze 
aangelegenheden worden behandeld in Toelichting 5 van de samengevatte financiële overzichten. 
• 
De communicatie van andere18 kernpunten van de controle. [Kernpunten van onze controle 
betreffen die aangelegenheden die naar ons professioneel oordeel het meest significant waren bij 
de controle van de financiële overzichten van de huidige verslagperiode.]19 
Verantwoordelijkheid van het management 20 voor de samengevatte financiële overzichten 
Het management is verantwoordelijk voor het opstellen van de samengevatte financiële overzichten in 
overeenstemming met [omschrijf de vastgestelde criteria]. 
Verantwoordelijkheid van de auditor 
Het is onze verantwoordelijkheid een oordeel tot uitdrukking te brengen over de vraag of de 
samengevatte financiële overzichten in alle van materieel belang zijnde opzichten consistent zijn met 
(of een getrouwe samenvatting zijn van) de gecontroleerde financiële overzichten op basis van onze 
werkzaamheden uitgevoerd overeenkomstig de Internationale controlestandaard (ISA) 810 (herzien), 
Opdrachten om te rapporteren betreffende samengevatte financiële overzichten. 
 
 
[Handtekening van de auditor] 
[Adres van de auditor] 
[Datum van de controleverklaring] 
 
 
 
 
 
 
 
 
 
 
 
 
18 In de gevallen waarin er geen van materieel belang zijnde onzekerheid met betrekking tot continuïteit bestaat, zou het niet nodig 
zijn om het woord "andere" op te nemen in de vermelding met betrekking tot de communicatie van kernpunten van de controle. 
19 De auditor kan aanvullende uitleg verstrekken over kernpunten van de controle die nuttig worden geacht voor gebruikers van 
de controleverklaring over de samengevatte financiële overzichten. 
20 Of een andere bewoording die passend is in de context van het wettelijke kader van het specifieke rechtsgebied.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
20/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
 
 
Voorbeeld 2: 
De omstandigheden omvatten het volgende: 
• 
Een niet-aangepast oordeel over de gecontroleerde financiële overzichten werd tot 
uitdrukking gebracht. 
• 
Criteria worden door het management ontwikkeld en op adequate wijze uiteengezet in 
Toelichting X. De auditor heeft vastgesteld dat de criteria in de gegeven omstandigheden 
aanvaardbaar zijn. 
• 
De controleverklaring over de samengevatte financiële overzichten is van dezelfde datum 
als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
• 
De controleverklaring over de gecontroleerde financiële overzichten bevat een vermelding 
die een niet gecorrigeerde afwijking van materieel belang in de andere informatie 
beschrijft. De andere informatie waarop deze niet gecorrigeerde afwijking van materieel 
belang betrekking heeft, is ook informatie die is opgenomen in een document dat de 
samengevatte financiële overzichten en de controleverklaring daarover bevat. 
 
VERKLARING VAN DE ONAFHANKELIJKE AUDITOR OVER DE SAMENGEVATTE FINANCIËLE 
OVERZICHTEN 
[Passende geadresseerde] 
Oordeel 
De samengevatte financiële overzichten, die bestaan uit de samengevatte balans per 31 december 
20X1, de samengevatte winst- en verliesrekening, het samengevatte mutatieoverzicht van het eigen 
vermogen en het samengevatte kasstroomoverzicht voor het boekjaar afgesloten op die datum, 
alsmede uit de daarop betrekking hebbende toelichtingen, zijn afgeleid van de gecontroleerde financiële 
overzichten van de vennootschap ABC voor het boekjaar afgesloten op 31 december 20X1. 
Naar ons oordeel zijn de bijhorende samengevatte financiële overzichten in alle van materieel belang 
zijnde opzichten consistent met (of een getrouwe samenvatting van) de gecontroleerde financiële 
overzichten, in overeenstemming met de in Toelichting X beschreven grondslag inzake financiële 
verslaggeving. 
Samengevatte financiële overzichten 
De samengevatte financiële overzichten bevatten niet alle op grond van [omschrijf het stelsel inzake 
financiële verslaggeving dat wordt toegepast bij het opstellen van de gecontroleerde financiële 
overzichten van de vennootschap ABC] vereiste toelichtingen. Daarom kan het lezen van de 
samengevatte financiële overzichten en de controleverklaring daarover het lezen van de gecontroleerde 
financiële overzichten en de controleverklaring daarover niet vervangen. 
De gecontroleerde financiële overzichten en onze verklaring daarover 
Wij hebben een niet-aangepast controleoordeel over de gecontroleerde financiële overzichten tot 
uitdrukking gebracht in onze verklaring d.d. 15 februari 20X2. [De gecontroleerde financiële overzichten 
zijn opgenomen in het jaarrapport over 20X1. De controleverklaring over de gecontroleerde financiële 
overzichten bevat een vermelding die een niet gecorrigeerde afwijking van materieel belang in de 
andere informatie beschrijft in het kader van de bespreking en analyse door het management 
opgenomen in het jaarrapport over 20X1. De bespreking en analyse door het management, en de daarin 
opgenomen niet gecorrigeerde afwijking van materieel belang in de andere informatie, zijn ook 
opgenomen in het samengevatte jaarrapport over 20X1.] [Omschrijf de niet gecorrigeerde afwijking van 
materieel belang in de andere informatie].

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
21/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Verantwoordelijkheid van het management21 voor de samengevatte financiële overzichten 
Het management is verantwoordelijk voor het opstellen van de samengevatte financiële overzichten in 
overeenstemming met de in Toelichting X beschreven grondslag inzake financiële verslaggeving. 
Verantwoordelijkheid van de auditor 
Het is onze verantwoordelijkheid een oordeel tot uitdrukking te brengen over de vraag of de 
samengevatte financiële overzichten in alle van materieel belang zijnde opzichten consistent zijn met 
(of een getrouwe samenvatting zijn van) de gecontroleerde financiële overzichten op basis van onze 
werkzaamheden uitgevoerd overeenkomstig de Internationale controlestandaard (ISA) 810 (herzien), 
Opdrachten om te rapporteren betreffende samengevatte financiële overzichten. 
[Handtekening van de auditor] 
[Adres van de auditor] 
[Datum van de controleverklaring] 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
21  Of een andere bewoording die passend is in de context van het wettelijke kader van het specifieke rechtsgebied.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
22/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Voorbeeld 3: 
De omstandigheden omvatten het volgende: 
• 
Er werd over de gecontroleerde financiële overzichten een oordeel met beperking tot 
uitdrukking gebracht. 
• 
Criteria worden door het management ontwikkeld en op adequate wijze uiteengezet in 
Toelichting X. De auditor heeft vastgesteld dat de criteria in de gegeven omstandigheden 
aanvaardbaar zijn. 
• 
De controleverklaring over de samengevatte financiële overzichten is van dezelfde datum 
als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
 
VERKLARING VAN DE ONAFHANKELIJKE AUDITOR OVER DE SAMENGEVATTE FINANCIËLE 
OVERZICHTEN 
[Passende geadresseerde] 
Oordeel 
De samengevatte financiële overzichten, die bestaan uit het samengevatte overzicht van de financiële 
positie per 31 december 20X1, het samengevatte overzicht van gerealiseerde en niet-gerealiseerde 
resultaten, het samengevatte mutatieoverzicht van het eigen vermogen en het samengevatte 
kasstroomoverzicht voor het boekjaar afgesloten op die datum, alsmede uit de daarop betrekking 
hebbende toelichtingen, zijn afgeleid van de gecontroleerde financiële overzichten van de vennootschap 
ABC (de “vennootschap”) voor het boekjaar afgesloten op 31 december 20X1. Wij hebben een 
controleoordeel met beperking over die financiële overzichten tot uitdrukking gebracht in onze verklaring 
d.d. 15 februari 20X2.22 
Naar ons oordeel zijn de bijhorende samengevatte financiële overzichten in alle van materieel belang 
zijnde opzichten consistent met (of een getrouwe samenvatting van) de gecontroleerde financiële 
overzichten, in overeenstemming met de in Toelichting X beschreven grondslag inzake financiële 
verslaggeving. De samengevatte financiële overzichten omvatten echter in dezelfde mate afwijkingen 
als de gecontroleerde financiële overzichten van de vennootschap ABC voor het boekjaar afgesloten 
op 31 december 20X1. 
 
Samengevatte financiële overzichten 
De samengevatte financiële overzichten bevatten niet alle op grond van [omschrijf het stelsel inzake 
financiële verslaggeving dat wordt toegepast bij het opstellen van de gecontroleerde financiële 
overzichten van de vennootschap ABC] vereiste toelichtingen. Daarom kan het lezen van de 
samengevatte financiële overzichten en de controleverklaring daarover het lezen van de gecontroleerde 
financiële overzichten en de controleverklaring daarover niet vervangen. 
De gecontroleerde financiële overzichten en onze verklaring daarover 
Wij hebben een controleoordeel met beperking over de gecontroleerde financiële overzichten tot 
uitdrukking gebracht in onze verklaring d.d. 15 februari 20X2. De basis voor ons controleoordeel met 
beperking was het feit [dat het management de voorraden niet heeft gewaardeerd tegen de laagste 
waarde van kostprijs enerzijds en opbrengstwaarde anderzijds, maar deze heeft gewaardeerd tegen 
kostprijs, hetgeen een afwijking vormt van de International Financial Reporting Standards.] De 
vastleggingen van de vennootschap geven aan dat, indien het management de voorraden zou hebben 
gewaardeerd tegen de laagste waarde van kostprijs enerzijds en nettoyerkoopwaarde anderzijds, een 
 
22 Het plaatsen van deze verwijzing naar het oordeel met beperking uitgedrukt in de controleverklaring over de gecontroleerde 
financiële overzichten in de sectie met betrekking tot het oordeel over de samengevatte financiële overzichten helpt gebruikers te 
begrijpen dat, hoewel de auditor een niet-aangepast oordeel tot uitdrukking heeft gebracht over de samengevatte financiële 
overzichten, deze laatste een weergave zijn van gecontroleerde financiële overzichten die een afwijking van materieel belang 
bevatten.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
23/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
bedrag van xxx zou vereist zijn om de voorraden af te schrijven tot hun nettoyerkoopwaarde. 
Dienovereenkomstig zou de kostprijs van de omzet gestegen zijn met xxx, en de belastingen over de 
winst, de nettowinst en het eigen vermogen zouden gedaald zijn met respectievelijk xxx, xxx en xxx.  
Verantwoordelijkheid van het management23 voor de samengevatte financiële overzichten 
Het management is verantwoordelijk voor het opstellen van de samengevatte financiële overzichten in 
overeenstemming met de in Toelichting X beschreven grondslag inzake financiële verslaggeving. 
Verantwoordelijkheid van de auditor 
Het is onze verantwoordelijkheid een oordeel tot uitdrukking te brengen over de vraag of de 
samengevatte financiële overzichten in alle van materieel belang zijnde opzichten consistent zijn met 
(of een getrouwe samenvatting zijn van) de gecontroleerde financiële overzichten op basis van onze 
werkzaamheden uitgevoerd overeenkomstig de Internationale controlestandaard (ISA) 810 (herzien), 
Opdrachten om te rapporteren betreffende samengevatte financiële overzichten. 
 
[Handtekening van de auditor] 
[Adres van de auditor] 
[Datum van de controleverklaring] 
 
 
 
 
 
 
 
 
 
 
 
 
23 Of een andere bewoording die passend is in de context van het wettelijke kader van het specifieke rechtsgebied.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
24/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Voorbeeld 4: 
De omstandigheden omvatten het volgende: 
• 
Een afkeurend oordeel werd tot uitdrukking gebracht over de gecontroleerde financiële 
overzichten. 
• 
Criteria worden door het management ontwikkeld en op adequate wijze uiteengezet in 
Toelichting X. De auditor heeft vastgesteld dat de criteria in de gegeven omstandigheden 
aanvaardbaar zijn. 
• 
De controleverklaring over de samengevatte financiële overzichten is van dezelfde datum 
als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
 
VERKLARING VAN DE ONAFHANKELIJKE AUDITOR OVER DE SAMENGEVATTE 
FINANCIËLE OVERZICHTEN 
[Passende geadresseerde] 
Weigering om een oordeel tot uitdrukking te brengen 
De samengevatte financiële overzichten, die bestaan uit de samengevatte balans per 31 december 
20X1, de samengevatte winst- en verliesrekening, het samengevatte mutatieoverzicht van het eigen 
vermogen en het samengevatte kasstroomoverzicht voor het boekjaar afgesloten op die datum, 
alsmede uit de daarop betrekking hebbende toelichtingen, zijn afgeleid van de gecontroleerde financiële 
overzichten van de vennootschap ABC voor het boekjaar afgesloten op 31 december 20X1. 
Als gevolg van het afkeurend oordeel over de gecontroleerde financiële overzichten opgenomen in de 
sectie van onze verklaring “De gecontroleerde financiële overzichten en onze verklaring daarover”, is 
het niet passend om een oordeel over de bijhorende samengevatte financiële overzichten tot uitdrukking 
te brengen. 
Samengevatte financiële overzichten 
De samengevatte financiële overzichten bevatten niet alle op grond van [omschrijf het stelsel inzake 
financiële verslaggeving dat wordt toegepast bij het opstellen van de gecontroleerde financiële 
overzichten van de vennootschap ABC] vereiste toelichtingen. Daarom kan het lezen van de 
samengevatte financiële overzichten en de controleverklaring daarover het lezen van de gecontroleerde 
financiële overzichten en de controleverklaring daarover niet vervangen. 
De gecontroleerde financiële overzichten en onze verklaring daarover 
In onze verklaring d.d. 15 februari 20X2 hebben wij een afkeurend controleoordeel tot uitdrukking 
gebracht over de gecontroleerde financiële overzichten van de vennootschap ABC voor het boekjaar 
afgesloten op 31 december 20X1. De basis voor ons afkeurend controleoordeel was [beschrijf de basis 
voor het afkeurend oordeel].  
Verantwoordelijkheid van het management24 voor de samengevatte financiële overzichten 
Het management is verantwoordelijk voor het opstellen van de samengevatte financiële overzichten in 
overeenstemming met de in Toelichting X beschreven grondslag inzake financiële verslaggeving. 
Verantwoordelijkheid van de auditor 
Het is onze verantwoordelijkheid een oordeel tot uitdrukking te brengen over de vraag of de 
samengevatte financiële overzichten in alle van materieel belang zijnde opzichten consistent zijn met 
 
24 Of een andere bewoording die passend is in de context van het wettelijke kader van het specifieke rechtsgebied.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
25/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
(of een getrouwe samenvatting zijn van) de gecontroleerde financiële overzichten op basis van onze 
werkzaamheden uitgevoerd overeenkomstig de Internationale controlestandaard (ISA) 810 (herzien), 
Opdrachten om te rapporteren betreffende samengevatte financiële overzichten. 
[Handtekening van de auditor] 
[Adres van de auditor] 
[Datum van de controleverklaring]

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
26/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Voorbeeld 5: 
De omstandigheden omvatten het volgende: 
• 
Er werd een niet-aangepast oordeel tot uitdrukking gebracht over de gecontroleerde 
financiële overzichten. 
• 
Er bestaan vastgestelde criteria voor het opstellen van de samengevatte financiële 
overzichten. 
• 
De auditor concludeert dat het niet mogelijk is om een niet-aangepast oordeel tot 
uitdrukking te brengen over de samengevatte financiële overzichten. 
• 
De controleverklaring over de samengevatte financiële overzichten is van dezelfde datum 
als de datum van de controleverklaring over de financiële overzichten waarvan de 
samengevatte financiële overzichten zijn afgeleid. 
 
VERKLARING VAN DE ONAFHANKELIJKE AUDITOR OVER DE SAMENGEVATTE FINANCIËLE 
OVERZICHTEN 
[Passende geadresseerde] 
Afkeurend oordeel 
De samengevatte financiële overzichten, die bestaan uit de samengevatte balans per 31 december 
20X1, de samengevatte winst- en verliesrekening, het samengevatte mutatieoverzicht van het eigen 
vermogen en het samengevatte kasstroomoverzicht voor het boekjaar afgesloten op die datum, 
alsmede uit de daarop betrekking hebbende toelichtingen, zijn afgeleid van de gecontroleerde financiële 
overzichten van de vennootschap ABC voor het boekjaar afgesloten op 31 december 20X1. 
Naar ons oordeel, gezien de significantie van de in de sectie “Basis voor ons afkeurend oordeel” 
beschreven aangelegenheid, zijn de bijhorende samengevatte financiële overzichten niet consistent met 
(of geen getrouwe samenvatting van) de gecontroleerde financiële overzichten van de vennootschap 
ABC voor het boekjaar afgesloten op 31 december 20X1, in overeenstemming met [beschrijf de 
vastgestelde criteria]. 
Basis voor ons afkeurend oordeel 
[Beschrijf de aangelegenheid die ervoor gezorgd heeft dat de samengevatte financiële overzichten in 
alle van materieel belang zijnde opzichten niet consistent zijn met (of geen getrouwe samenvatting zijn 
van) de gecontroleerde financiële overzichten, in overeenstemming met de toegepaste criteria.] 
Samengevatte financiële overzichten 
De samengevatte financiële overzichten bevatten niet alle op grond van [omschrijf het stelsel inzake 
financiële verslaggeving dat wordt toegepast bij het opstellen van de gecontroleerde financiële 
overzichten van de vennootschap ABC] vereiste toelichtingen. Daarom kan het lezen van de 
samengevatte financiële overzichten en de controleverklaring daarover het lezen van de gecontroleerde 
financiële overzichten en de controleverklaring daarover niet vervangen. 
De gecontroleerde financiële overzichten en onze verklaring daarover 
Wij hebben een niet-aangepast controleoordeel over de gecontroleerde financiële overzichten tot 
uitdrukking gebracht in onze verklaring d.d. 15 februari 20X2. 
Verantwoordelijkheid van het management25 voor de samengevatte financiële overzichten 
Het management is verantwoordelijk voor het opstellen van de samengevatte financiële overzichten in 
overeenstemming met [omschrijf de vastgestelde criteria]. 
 
25 Of een andere bewoording die passend is in de context van het wettelijke kader van het specifieke rechtsgebied.

OPDRACHTEN OM TE RAPPORTEREN BETREFFENDE SAMENGEVATTE FINANCIELE OVERZICHTEN 
ISA 810 (Herzien) - Bijlage 
NBA-IBR 2025  
27/27 
Originele bron : Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Version 2025 
Verantwoordelijkheid van de auditor 
Het is onze verantwoordelijkheid een oordeel tot uitdrukking te brengen over de vraag of de 
samengevatte financiële overzichten in alle van materieel belang zijnde opzichten consistent zijn met 
(of een getrouwe samenvatting zijn van) de gecontroleerde financiële overzichten op basis van onze 
werkzaamheden uitgevoerd overeenkomstig de Internationale controlestandaard (ISA) 810 (herzien), 
Opdrachten om te rapporteren betreffende samengevatte financiële overzichten. 
[Handtekening van de auditor] 
[Adres van de auditor] 
[Datum van de controleverklaring]