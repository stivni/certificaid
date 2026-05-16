---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 610 (herzien) — Gebruikmaken van de werkzaamheden van interne auditors
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-610-(herzien)_nl_2023.pdf
    sha256: a3e5b2a69645b729b2f3b833e7d4f94a74d2f2236bcd9fdcb2ad3dffe089f05b
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
title: ISA 610 (herzien) — Gebruikmaken van de werkzaamheden van interne auditors
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 610 (herzien) — Gebruikmaken van de werkzaamheden van interne auditors

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-610-(herzien)_nl_2023.pdf) — gedownload 2026-05-16.  
> SHA-256: `a3e5b2a69645b729b2f3b833e7d4f94a74d2f2236bcd9fdcb2ad3dffe089f05b`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard 610 (herzien 2013) 
ISA 610 (herzien 2013) 
 
Gebruikmaken van de 
werkzaamheden van interne 
auditors

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
2/20 
 
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
de Internationale controlestandaard (ISA) 610 (herzien 2013) is onderzocht door IFAC en de vertaling werd 
uitgevoerd in overeenstemming met de Policy Statement de l’IFAC – Policy for Translating and 
Reproducing Standards published by IFAC. De goedgekeurde Internationale controlestandaard (ISA) 610 
(herzien 2013) is gepubliceerd door IFAC in de Engelse taal. 
 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 610 (herzien 2013) © 2022 van de 
International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 610 (herzien 2013) © 2022 van 
de International Federation of Accountants (IFAC). Alle rechten voorbehouden. 
 
Originele titel: International Standard on Auditing 610 (Revised 2013), Using the Work of Internal Auditors. 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and 
Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
3/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
INTERNATIONALE CONTROLESTANDAARD 610 (herzien 2013) 
GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE 
AUDITORS 
 
 (Van toepassing op controles van financiële overzichten over verslagperioden die op of 
na 15 december 2014 aanvangen) (*) 
 
(*) Deze ISA bevat overeenstemmingswijzigingen die voortvloeien uit de herziene ISA’s 220, 250, 315 en 
540 en de normen ISQM 1 en 2. De inwerkingtreding van deze wijzigingen valt samen met deze normen 
(voor de verslagperiode die op of na 15 december aanvangen). 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ............................................................................................................ 1 -5 
Relatie tussen ISA 315 (herzien 2019) en ISA 610 (herzien 2013) ..................................................... 6-10 
De verantwoordelijkheid van de externe auditor voor de controle .......................................................... 11  
Ingangsdatum ....................................................................................................................................................  12 
Doelstellingen .....................................................................................................................................  13 
Definities ...................................................................................................................................................... 14 
Vereisten 
Het bepalen of, in welke gebieden, en in welke mate, er van de werkzaamheden  
van een interne auditfunctie gebruik kan worden gemaakt ............................................................... 15-20 
Gebruikmaken van de werkzaamheden van de interne auditfunctie ................................................. 21-25 
Bepalen of, in welke gebieden, en in welke mate er gebruik kan worden  
gemaakt van interne auditors om directe ondersteuning te verschaffen ........................................... 26-32 
Gebruikmaken van interne auditors om directe ondersteuning te verschaffen  ................................ 33-35 
Documentatie ...................................................................................................................................  36-37 
Toepassingsgerichte en overige verklarende teksten 
Definitie van de interne auditfunctie ................................................................................................. A1-A4 
Het bepalen of, in welke gebieden, en in welke mate, er van de werkzaamheden 
van de interne auditfunctie gebruik kan worden gemaakt .............................................................. A5-A23 
Gebruikmaken van de werkzaamheden van de interne auditfunctie ............................................ A24-A30 
Bepalen of, in welke gebieden, en in welke mate er gebruik kan worden  
gemaakt van interne auditors om directe ondersteuning te verschaffen  ..................................... A31-A39 
Gebruikmaken van interne auditors om directe ondersteuning te verschaffen  ........................... A40-A41 
 
International Standard on Auditing (ISA) 610 (herzien 2013), “Gebruikmaken van de werkzaamheden 
van interne auditors”, moet worden gelezen in samenhang met ISA 200, “Algehele doelstellingen van 
de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig de International 
Standards on Auditing”.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
4/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
 
Inleiding 
 
Reikwijdte van deze ISA 
 
1. 
Deze ISA behandelt de verantwoordelijkheden van de externe auditor indien hij gebruikmaakt van 
de werkzaamheden van interne auditors. Dit omvat (a) het gebruikmaken van de werkzaamheden 
van de interne auditfunctie bij het verkrijgen van controle-informatie en (b) het gebruikmaken van 
interne auditors om directe ondersteuning te verschaffen onder de aansturing, het toezicht en de 
beoordeling van de externe auditor. 
 
2. 
Deze ISA is niet van toepassing als de entiteit niet over een interne auditfunctie beschikt. (Zie par. 
A2) 
 
3. 
Indien de entiteit over een interne auditfunctie beschikt, zijn de vereisten in deze ISA die betrekking 
hebben op het gebruikmaken van de werkzaamheden van die functie niet van toepassing als: 
 
(a) 
De verantwoordelijkheden en activiteiten van de interne auditfunctie niet relevant zijn voor de 
externe controle; of  
(b) 
Op basis van het voorlopige inzicht van de auditor in de interne auditfunctie dat is verworven 
als gevolg van werkzaamheden die onder ISA 315 (herzien)1 zijn uitgevoerd, de externe 
auditor niet verwacht van de werkzaamheden van de interne auditfunctie bij het verkrijgen van 
controle-informatie gebruik te zullen maken. 
 
Niets in deze ISA vereist van de externe auditor dat hij van de werkzaamheden van de interne 
auditfunctie gebruik maakt om de aard of timing van controlewerkzaamheden door de externe auditor 
zelf uit te voeren aan te passen, of de mate ervan te verminderen; dit blijft een beslissing van de 
externe auditor bij het vaststellen van de algehele controleaanpak. 
 
4. 
Verder zijn de vereisten in deze ISA die betrekking hebben op directe ondersteuning niet van 
toepassing als de externe auditor niet gepland heeft om gebruik te maken van interne auditors om 
directe ondersteuning te verschaffen. 
 
5. 
In sommige rechtsgebieden kan het de externe auditor door wet- of regelgeving worden verboden, 
of tot op zekere hoogte worden beperkt, om gebruik te maken van de werkzaamheden van de interne 
auditfunctie of om  gebruik te maken van interne auditors om directe ondersteuning te verschaffen. 
De ISAs doen geen afbreuk aan wet- of regelgeving die een controle van de financiële overzichten 
regelt.2 Dergelijke verboden of beperkingen zullen derhalve het naleven van de ISAs door de externe 
auditor niet in de weg staan. (Zie par. A31)   
 
Relatie tussen ISA 315 (herzien 2019) en ISA 610 (herzien 2013) 
 
6. 
Veel entiteiten richten een interne auditfunctie in als onderdeel van hun interne beheersings- en  
governancestructuren. De doelstellingen en reikwijdte van een interne auditfunctie, de aard van haar 
verantwoordelijkheden 
en 
haar 
organisatorische 
positie, 
inclusief 
de 
bevoegdheid 
en 
verantwoordingsplicht van de interne auditfunctie, variëren in hoge mate en zijn afhankelijk van de 
omvang en structuur van de entiteit, alsmede van de vereisten van het management en, voor zover 
van toepassing, de met governance belaste personen.  
 
7. 
ISA 315 (herzien 2019) behandelt de wijze waarop de kennis van en ervaring met de interne 
auditfunctie de externe auditor inzicht kan verschaffen in de entiteit en haar omgeving, het van 
toepassing zijnde stelsel inzake financiële verslaggevingen het systeem van interne beheersing van 
de entiteit en in het onderkennen en inschatten van risico's van een afwijking van materieel belang. 
 
1  
ISA 315 (herzien 2019), Het identificeren en inschatten van de risico’s van een afwijking van materieel belang. 
2  
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, en het uitvoeren van een controle volgens ISAs, paragraaf A60.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
5/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
ISA 315 (herzien 2019)3 behandelt tevens op welke wijze doeltreffende communicatie tussen de 
interne en externe auditors een omgeving creëert waarin de externe auditor kan worden 
geïnformeerd over significante aangelegenheden die de werkzaamheden van de externe auditor 
kunnen beïnvloeden.  
 
8. 
Afhankelijk van de vraag of de organisatorische positie en relevante beleidslijnen en procedures van 
de interne auditfunctie op adequate wijze de objectiviteit van de interne auditors ondersteunen en 
het competentieniveau van de interne auditfunctie, en van de vraag of de interne auditfunctie een 
systematische en gedisciplineerde benadering hanteert, kan de externe auditor tevens in staat zijn 
om op een constructieve en complementaire wijze gebruik te maken van de werkzaamheden van de 
interne auditfunctie. Deze ISA behandelt de verantwoordelijkheden van de externe auditor wanneer, 
op basis van het voorlopige inzicht van de externe auditor in de interne auditfunctie dat is verworven 
als gevolg van de werkzaamheden die overeenkomstig ISA 315 (herzien 2019) zijn uitgevoerd, de 
externe auditor verwacht de werkzaamheden van de interne auditfunctie te gebruiken als onderdeel 
van de verkregen controle-informatie.4 Dergelijk gebruik van die werkzaamheden leidt tot 
aanpassing van de aard of timing, of vermindert de omvang, van de controlewerkzaamheden uit te 
voeren  door de externe auditor zelf.  
 
9. 
Bovendien gaat deze ISA tevens in op de verantwoordelijkheden van de externe auditor bij de  
overweging om gebruik te maken van interne auditors om directe ondersteuning te verschaffen onder 
de aansturing, het toezicht en de beoordeling van de externe auditor. 
 
10. 
Er kunnen personen binnen een entiteit zijn die werkzaamheden uitvoeren die vergelijkbaar zijn met 
werkzaamheden die door een interne auditfunctie worden uitgevoerd. Tenzij deze door een 
objectieve en competente interne auditfunctie die een systematische en gedisciplineerde benadering 
hanteert, worden uitgevoerd, inclusief kwaliteitsbeheersing, worden dergelijke werkzaamheden 
evenwel als interne beheersingsmaatregelen beschouwd en kan het verkrijgen van controle-
informatie met betrekking tot de effectiviteit van dergelijke interne beheersingsmaatregelen 
onderdeel zijn van de wijzen van inspelen door de auditor op ingeschatte risico's overeenkomstig 
ISA 330.5 
 
De verantwoordelijkheid van de externe auditor voor de controle  
 
11. 
De externe auditor heeft de ongedeelde verantwoordelijkheid voor het controleoordeel dat tot 
uitdrukking wordt gebracht en die verantwoordelijkheid wordt niet verminderd doordat de externe 
auditor voor de opdracht gebruik maakt van de werkzaamheden van de interne auditfunctie of van 
interne auditors om directe ondersteuning te verschaffen bij de opdracht. Hoewel zij 
controlewerkzaamheden kunnen uitvoeren, die vergelijkbaar zijn met de werkzaamheden die door 
de externe auditor worden uitgevoerd, zijn de interne auditfunctie noch de interne auditors 
onafhankelijk van de entiteit zoals van de externe auditor vereist is bij een controle van financiële 
overzichten overeenkomstig ISA 200.6 Deze ISA definieert dan ook de voorwaarden die voor de 
externe auditor noodzakelijk  zijn om gebruik te kunnen maken van de werkzaamheden van interne 
auditors. Deze definieert tevens de noodzakelijke werkinspanning om voldoende en geschikte 
onderbouwende informatie te verkrijgen dat de werkzaamheden van de interne auditfunctie of van 
interne auditors om directe ondersteuning te verschaffen  adequaat zijn voor de doeleinden van de 
controle . De vereisten zijn ontworpen om voor de oordeelsvorming van de externe auditor met 
betrekking tot het gebruikmaken van de werkzaamheden van interne auditors een raamwerk te 
verschaffen om bovenmatig of ongepast gebruik van dergelijke werkzaamheden te voorkomen.  
 
Ingangsdatum 
 
12. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden eindigend 
op of na 15 december 2014. 
 
 
3  
ISA 315 (herzien 2019), paragraaf 24(a)(ii) et Bijlage 4. 
4  
Zie par. 15-25. 
5  
ISA 330, De wijze van inspelen door de auditor op ingeschatte risico’s. 
6  
ISA 200, paragraaf 14.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
6/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Doelstellingen 
 
13. 
De doelstellingen van de externe auditor, in het geval de entiteit een interne auditfunctie heeft en de 
externe auditor verwacht van de werkzaamheden van die functie gebruik te zullen maken of om de 
aard of de timing van de controlewerkzaamheden uit te voeren door de externe auditor zelf aan te 
passen of de omvang van de werkzaamheden  te verminderen, of om gebruik te maken van interne 
auditors om directe ondersteuning te verschaffen, zijn  : 
 
(a) 
Bepalen of van de werkzaamheden van de interne auditfunctie of directe ondersteuning van 
interne auditors gebruik kan worden gemaakt, en, zo ja, op welke terreinen en in welke mate;  
 
en na dit te hebben bepaald:   
 
(b) 
Indien van de werkzaamheden van de interne auditfunctie gebruik wordt gemaakt, bepalen of 
die werkzaamheden adequaat zijn voor de doeleinden van de controle; en  
(c) 
Indien van interne auditors gebruikt wordt gemaakt om directe ondersteuning te verschaffen 
op gepaste wijze hun werkzaamheden aansturen, hierop toezien en deze beoordelen. 
 
Definitie 
 
14. 
In het kader van de ISA’s  hebben de volgende termen de hierna weergegeven betekenis:  
 
(a) 
Interne auditfunctie – Een functie van een entiteit die assurance- en advies activiteiten uitvoert 
die zijn opgezet om de effectiviteit van de governance-, risicobeheersings- en interne 
beheersingsprocessen van de entiteit te evalueren en te verbeteren. (Zie par. A1-A4) 
(b) 
Directe ondersteuning - Het gebruikmaken van interne auditors om controlewerkzaamheden 
uit te voeren onder de aansturing, het toezicht en de beoordeling van de externe auditor.   
 
Vereisten 
 
Het bepalen of, op welke gebieden, en in welke mate, er van de werkzaamheden van de interne 
auditfunctie gebruik kan worden gemaakt 
 
Het evalueren van de interne auditfunctie 
 
15. 
De externe auditor dient te bepalen of van de werkzaamheden van de interne auditfunctie voor de 
doeleinden van de controle gebruik kan worden gemaakt door het volgende te evalueren: 
 
(a) 
De mate waarin de organisatorische positie en relevante beleidslijnen en procedures van de 
interne auditfunctie de objectiviteit van de interne auditors ondersteunen; (Zie par. A5-A9) 
(b) 
Het competentieniveau van de interne auditfunctie; en (Zie par. A5-A9) 
(c) 
Of de interne auditfunctie een systematische en gedisciplineerde benadering hanteert, 
inclusief kwaliteitsbeheersing. (Zie par. A10-A11) 
 
16. 
De externe auditor dient geen gebruik te maken van de werkzaamheden van de interne auditfunctie 
indien de externe auditor vaststelt dat: 
 
(a) 
De organisatorische positie en relevante beleidslijnen en procedures van de interne 
auditfunctie niet op adequate wijze de objectiviteit van de interne auditors ondersteunen; 
(b) 
Het de interne auditfunctie aan voldoende competentie ontbreekt; of 
(c) 
De interne auditfunctie geen systematische en gedisciplineerde benadering hanteert, inclusief 
kwaliteitsbeheersing. (Zie par. A12-A14) 
 
Het bepalen van de aard en de mate van de werkzaamheden van de interne auditfunctie waarvan gebruik 
kan worden gemaakt 
 
17. 
Als basis voor het bepalen van de gebieden waarop en de mate waarin van de werkzaamheden van

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
7/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
de interne auditfunctie gebruik kan worden gemaakt, dient de externe auditor de aard en reikwijdte 
van de werkzaamheden die door de interne auditfunctie zijn uitgevoerd of die zijn gepland om te 
worden uitgevoerd, en de relevantie daarvan voor de algehele controleaanpak en voor het 
controleprogramma van de externe auditor in overweging te nemen. (Zie par. A15-A17) 
 
18. 
De externe auditor dient alle significante oordelen bij de uitvoering van de controleopdracht te 
vormen en dient, om overmatig gebruik van de werkzaamheden van de interne auditfunctie te 
voorkomen, te plannen om minder gebruik te maken van de werkzaamheden van de interne 
auditfunctie, en meer werkzaamheden zelf uit te voeren: (Zie par. A15-A17) 
 
(a) 
Naar mate er meer sprake is van oordeelsvorming bij: 
 
(i) 
Het plannen en uitvoeren van relevante controlewerkzaamheden; en  
(ii) 
Het evalueren van de verzamelde controle-informatie; (Zie par. A18-A19) 
 
(b) 
Naarmate de ingeschatte risico’s van een afwijking van materieel belang op het niveau van 
beweringen hoger is, waarbij speciale aandacht dient te worden besteed aan significante 
risico's; (Zie par. A20-A22) 
(c) 
Naarmate de organisatorische positie en relevante beleidslijnen en procedures van de interne 
auditfunctie op minder adequate wijze de objectiviteit van de interne auditors ondersteunen; 
en 
(d) 
Naarmate het competentieniveau van de interne auditfunctie lager is. 
 
19. 
De externe auditor dient tevens te evalueren of, in zijn totaliteit, het gebruikmaken van de 
werkzaamheden van de interne auditfunctie in de geplande mate er nog steeds in zou resulteren dat 
de externe auditor voldoende bij de controle betrokken is, gezien de ongedeelde 
verantwoordelijkheid van de externe auditor voor het controleoordeel dat tot uitdrukking wordt 
gebracht. (Zie par. A15-A22) 
 
20. 
De externe auditor dient bij het communiceren met de met governance belaste personen van een 
overzicht van de geplande reikwijdte en timing van de controle overeenkomstig ISA 260 (herzien)7 
aan te geven hoe de externe auditor gepland heeft gebruik te maken van de werkzaamheden van 
de interne auditfunctie. (Zie par. A23) 
 
Het gebruikmaken van de werkzaamheden van de interne auditfunctie 
 
21. 
Indien de externe auditor van plan is gebruik te maken van de werkzaamheden van de interne 
auditfunctie dient de externe auditor het geplande gebruik van zijn werkzaamheden met de interne 
auditfunctie te bespreken als basis voor de coördinatie van hun respectievelijke activiteiten. (Zie par. 
A24-A26) 
 
22. 
De externe auditor dient de rapportages van de interne auditfunctie te lezen, die verband houden 
met de werkzaamheden van de interne auditfunctie waarvan de auditor van plan is gebruik te maken, 
om inzicht te verwerven in de aard en omvang van controlewerkzaamheden die deze heeft 
uitgevoerd en de daaruit voortvloeiende bevindingen.   
 
23. 
De externe auditor dient voldoende controlewerkzaamheden uit te voeren op het geheel van de 
werkzaamheden van de interne auditfunctie als geheel waarvan de externe auditor van plan is 
gebruik te maken, om het adequaat zijn van laatstgenoemde werkzaamheden te bepalen voor de 
doeleinden van de controle, inclusief het evalueren of: 
 
(a) 
De werkzaamheden van de interne auditfunctie op behoorlijke wijze zijn gepland, uitgevoerd, 
hierop toezicht is gehouden, beoordeeld en gedocumenteerd; 
(b) 
Voldoende en geschikte informatie is verkregen om de interne auditfunctie in staat te stellen 
redelijke conclusies te trekken; en  
(c) 
De getrokken conclusies onder de gegeven omstandigheden passend zijn en de rapportages 
 
7  
ISA 260 (herzien), Communicatie met de met governance belaste personen, paragraaf 15.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
8/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
die door de interne auditfunctie zijn opgesteld consistent zijn met de uitkomsten van de 
uitgevoerde werkzaamheden. (Zie par. A27-A30) 
 
24. 
De aard en  reikwijdte van de controlewerkzaamheden van de externe auditor dienen in te spelen op 
de evaluatie door de externe auditor van: 
 
(a) 
De mate van hierbij betrokken oordeelsvorming; 
(b) 
Het ingeschatte risico van een afwijking van materieel belang; 
(c) 
De mate waarin de organisatorische positie en relevante beleidslijnen en procedures van de 
interne auditfunctie de objectiviteit van de interne auditors ondersteunen; en 
(d) 
Het competentieniveau  van de interne auditfunctie8; (Zie par. A27-A29) 
 
en dienen het opnieuw uitvoeren van bepaalde werkzaamheden te omvatten. (Zie par. A30) 
 
25. 
De externe auditor dient tevens te evalueren of zijn conclusies met betrekking tot de interne 
auditfunctie in paragraaf 15 van deze ISA en de bepaling van de aard en mate van het gebruikmaken 
van de werkzaamheden van de interne auditfunctie voor de doeleinden van de controle in paragrafen 
18-19 van deze ISA nog passend blijven. 
 
Bepalen of, in welke gebieden, en in welke mate er gebruik kan worden gemaakt van interne auditors 
om directe ondersteuning te verschaffen 
 
Het bepalen of er gebruik kan worden gemaakt van interne auditors om directe ondersteuning te 
verschaffen voor de doeleinden van de controle 
 
26. 
De externe auditor kan door wet- of regelgeving worden verboden om directe ondersteuning te 
verkrijgen van interne auditors. Zo ja, dan zijn de paragrafen 27–35 en 37 niet van toepassing. (Zie 
par. A31)   
 
27. 
Indien het gebruikmaken van interne auditors om directe ondersteuning te verschaffen niet door wet- 
of regelgeving wordt verboden, . en de externe auditor van plan is gebruik te maken van interne 
auditors om voor de controle directe ondersteuning te verschaffen, dient de externe auditor het 
bestaan en de significantie van bedreigingen voor de objectiviteit en het competentieniveau van de 
interne auditors die dergelijke ondersteuning zullen verschaffen, te evalueren. De evaluatie van de 
externe auditor van het bestaan en de significantie van bedreigingen voor de objectiviteit van de 
interne auditors dient een verzoek om inlichtingen aan de interne auditors te omvatten met betrekking 
tot belangen en relaties die een bedreiging kunnen vormen voor hun objectiviteit. (Zie par. A32-A34)   
 
28. 
De externe auditor dient geen gebruik te maken van een interne auditor om directe ondersteuning te 
verschaffen indien: 
 
(a) 
Er significante bedreigingen bestaan voor de objectiviteit van de interne auditor; of  
(b) 
Het de interne auditor ontbreekt aan voldoende competentie om de voorgestelde 
werkzaamheden uit te voeren.  (Zie par. A32-A34)  
 
Het bepalen van de aard en omvang van het werk dat kan worden toegewezen aan interne auditors die 
directe ondersteuning verschaffen 
 
29. 
Bij het bepalen van de aard en de omvang van het werk dat aan interne auditors kan worden 
toegewezen en de aard, timing en de omvang van de aansturing, het toezicht en de beoordeling die 
in de omstandigheden passend is, dient de externe auditor het volgende in overweging te nemen: 
 
(a) 
De hoeveelheid van de oordeelsvorming die hoort bij: 
 
(i) 
Het plannen en uitvoeren van de relevante controlewerkzaamheden; en 
(ii) 
Het evalueren van de verzamelde controle-informatie; 
 
8  
Zie par. 18.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
9/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
(b) 
Het ingeschatte risico van een afwijking van materieel belang; en  
(c) 
De evaluatie van de externe auditor van het bestaan en de significantie van bedreigingen voor 
zowel de objectiviteit als het competentieniveau van de interne auditors die dergelijke 
ondersteuning zullen verschaffen. (Zie par. A35-A39)   
 
30. 
De externe auditor dient geen gebruik te maken van interne auditors om directe ondersteuning te 
verschaffen om werkzaamheden uit te voeren die: 
 
(a) 
Betrekking hebben op het vormen van significante oordelen in de controle; (Zie par. A19)  
(b) 
Betrekking hebben op hoger ingeschatte risico's op een afwijking van materieel belang waar 
het oordeel dat vereist is bij het uitvoeren van de relevante controlewerkzaamheden of bij het 
evalueren van de verzamelde controle-informatie meer dan beperkt is.  (Zie par. A38)  
(c) 
Betrekking hebben op het werk waarbij de interne auditors betrokken zijn geweest en 
waarover aan het management of de met governance belaste personen door de interne 
auditfunctie reeds is gerapporteerd, of waarover nog zal worden gerapporteerd; of 
(d) 
Betrekking hebben op beslissingen die de externe auditor maakt overeenkomstig deze ISA 
met betrekking tot de interne auditfunctie en het gebruikmaken van de werkzaamheden of de 
directe ondersteuning hiervan. (Zie par. A35-A39)  
  
31. 
Nadat op passende wijze is geëvalueerd of en, zo ja, in welke mate er gebruik kan worden gemaakt 
van interne auditors om voor de controle directe ondersteuning te verschaffen, dient de externe 
auditor bij het communiceren met de met governance belaste personen van een overzicht van de 
geplande reikwijdte en timing van de controle overeenkomstig ISA 260 (herzien)9, de aard en 
reikwijdte te communiceren van het geplande gebruik van interne auditors om directe ondersteuning 
te verschaffen, om tot wederzijds begrip te komen dat dergelijk gebruik niet overmatig is in de 
omstandigheden van de opdracht.  (Zie par. A39)   
 
32. 
De externe auditor dient te evalueren, of in zijn totaliteit, het gebruikmaken van interne auditors om 
directe ondersteuning te verschaffen, samen met het geplande gebruikmaken van de 
werkzaamheden van de interne auditfunctie er nog steeds toe zou leiden dat de externe auditor 
voldoende bij de controle betrokken is gelet op de ongedeelde verantwoordelijkheid van de externe 
auditor voor het controleoordeel dat tot uitdrukking wordt gebracht.  
 
Gebruikmaken van interne auditors om directe ondersteuning te verschaffen 
 
33. 
Voorafgaand aan het gebruikmaken van interne auditors om directe ondersteuning te verschaffen 
voor het doel van de controle, dient de externe auditor: 
 
(a) 
Van een bevoegd vertegenwoordiger van de entiteit schriftelijke instemming te verkrijgen dat 
het de interne auditors is toegestaan om de instructies van de externe auditor op te volgen en 
dat de entiteit niet zal ingrijpen in de werkzaamheden die de interne auditor voor de externe 
auditor uitvoert; en  
(b) 
Van de interne auditors schriftelijke instemming te verkrijgen dat zij specifieke 
aangelegenheden geheim zullen houden zoals door de externe auditor is opgedragen en dat 
zij de externe auditor inlichten over eventuele bedreigingen voor hun objectiviteit. 
 
34. 
De externe auditor zal de werkzaamheden die door de interne auditors voor de opdracht zijn 
uitgevoerd aansturen, hierop toezien en beoordelen overeenkomstig ISA 220 (herzien)10. Hierbij:  
 
(a) 
Dienen uit de aard, timing en omvang van de aansturing, het toezicht en beoordeling te blijken  
dat de interne auditors niet onafhankelijk zijn van de entiteit en dienen in te spelen op de 
uitkomst van de evaluatie van de factoren in paragraaf 29 van deze ISA; en  
(b) 
Dienen de beoordelingswerkzaamheden te omvatten dat de externe auditor bepaalde 
werkzaamheden die door de interne auditors zijn uitgevoerd afstemt met de onderliggende 
controle-informatie.  
 
9  
ISA 260 (herzien), Communicatie met de met governance belaste personen, paragraaf 15. 
10  ISA 220 (herzien), Kwaliteitsmanagement voor een controle van financiële overzichten.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
10/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
De aansturing, het toezicht en de beoordeling door de externe auditor van de werkzaamheden die 
door de interne auditors zijn uitgevoerd dienen voor de externe auditor voldoende te zijn om vast 
te stellen dat de interne auditors voldoende geschikte controle-informatie hebben verkregen om de 
conclusies die op die werkzaamheden zijn gebaseerd te onderbouwen.  (Zie par. A40-A41)   
 
35. 
Bij het aansturen, toezien op en beoordelen van de werkzaamheden die door interne auditors zijn 
uitgevoerd dient de externe auditor alert te blijven op aanwijzingen dat de evaluaties van de externe 
auditors in paragraaf 27 niet langer geschikt zijn.  
 
Documentatie 
 
36. 
Indien de externe auditor gebruik maakt van de werkzaamheden van de interne auditfunctie dient hij 
in de controledocumentatie op te nemen:  
 
(a) 
De evaluatie van: 
 
(i) 
De vraag of de organisatorische positie en relevante beleidslijnen en procedures van 
de interne auditfunctie op adequate wijze de objectiviteit van de interne auditors 
ondersteunen;  
(ii) 
Het competentieniveau van de functie; en  
(iii) 
De vraag of de interne auditfunctie een systematische en gedisciplineerde benadering 
hanteert, inclusief kwaliteitsbeheersing. 
 
(b) 
De aard en reikwijdte van de werkzaamheden waarvan gebruik wordt gemaakt en de 
onderbouwing voor die beslissing; en  
(c) 
De controlewerkzaamheden die door de externe auditor zijn uitgevoerd om het adequaat zijn 
van de werkzaamheden waarvan gebruik wordt gemaakt te evalueren. 
 
37. 
Indien de externe auditor gebruik maakt van interne auditors om directe ondersteuning te verschaffen 
dient de externe auditor het volgende in de controledocumentatie op te nemen: 
 
(a) 
De evaluatie van het bestaan en de significantie van bedreigingen voor de objectiviteit van de 
interne auditors en het competentieniveau van de interne auditors waarvan wordt gebruik 
wordt gemaakt om directe ondersteuning te verschaffen; 
(b) 
De basis voor de beslissing met betrekking tot de aard en omvang van de werkzaamheden 
die door de interne auditors worden uitgevoerd; 
(c) 
Wie de werkzaamheden heeft beoordeeld, alsmede de datum en omvang van die beoordeling 
overeenkomstig ISA 23011; 
(d) 
De schriftelijke instemmingen die van een bevoegde vertegenwoordiger van de entiteit en van 
de interne auditors zijn verkregen onder paragraaf 33 van deze ISA; en  
(e) 
De werkdocumenten die door de interne auditors zijn opgesteld die bij de controleopdracht 
directe ondersteuning hebben verschaft. 
 
**** 
 
Toepassingsgerichte en overige verklarende teksten 
 
Definitie van de interne auditfunctie (Zie par. 2, 14(a)) 
 
A1. 
De doelstellingen en reikwijdte van interne auditfuncties omvatten doorgaans assurance- en 
adviserende activiteiten die zijn opgezet om de effectiviteit van de governanceprocessen, van de 
risicobeheersing en van de interne beheersing van de entiteit te evalueren en te verbeteren, zoals: 
 
Activiteiten die betrekking hebben op governance 
 
 
11  ISA 230, Controledocumentatie.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
11/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
• 
De interne auditfunctie kan het governance-proces beoordelen op het realiseren van 
doelstellingen  voor normen en waarden, prestatiemanagement en verantwoording, met het 
communiceren van risico- en beheersingsinformatie aan de juiste organisatieonderdelen, 
alsmede met de effectiviteit van de communicatie tussen de met governance belaste 
personen, externe en interne auditors en het management. 
 
Activiteiten die betrekking hebben op risicobeheersing 
 
• 
De interne auditfunctie kan de entiteit ondersteunen bij het identificeren en evalueren van 
significante blootstellingen aan risico’s en bij het bijdragen aan de verbetering van 
risicobeheersing en interne beheersing (inclusief de effectiviteit van het financiële 
verslaggevingsproces). 
• 
De interne auditfunctie kan werkzaamheden uitvoeren om de entiteit te ondersteunen bij het 
ontdekken van fraude.  
 
Activiteiten die betrekking hebben op interne beheersing 
 
• 
Het 
evalueren 
van 
interne 
beheersing. 
De 
interne 
auditfunctie 
kan 
specifieke 
verantwoordelijkheid toegewezen hebben gekregen voor het beoordelen van interne 
beheersingsmaatregelen, het evalueren van de werking daarvan en het aanbevelen van 
verbeteringen daarin. Hierdoor verschaft de interne auditfunctie een bepaalde mate van 
zekerheid over de interne beheersingsmaatregel. De interne auditfunctie kan bijvoorbeeld 
toetsingen of  andere werkzaamheden plannen en uitvoeren om aan het management en de 
met governance belaste personen een bepaalde mate van zekerheid te verschaffen met 
betrekking tot de opzet, het bestaan  en de werking van de interne beheersing, inclusief die 
toetsingen of werkzaamheden die voor de controle relevant zijn.  
• 
Het onderzoeken van financiële en operationele informatie.  De interne auditfunctie kan 
opdracht hebben gekregen om de middelen te beoordelen die zijn gebruikt bij het identificeren, 
erkennen, waarderen rubriceren en rapporteren van financiële en operationele informatie, en 
om specifiek onderzoek te doen naar afzonderlijke items, inclusief het in detail toetsen van 
transacties, saldi en procedures. 
• 
 Het beoordelen van operationele activiteiten. De interne auditfunctie kan opdracht hebben 
gekregen om de kostenefficiëntie, doelmatigheid en doeltreffendheid van de operationele 
activiteiten te beoordelen, inclusief niet-financiële activiteiten van een entiteit. 
• 
Het beoordelen van het naleven van wet- en regelgeving. De interne auditfunctie kan opdracht 
hebben gekregen om het naleven van wet- en regelgeving en overige externe voorschriften, 
en van de beleidslijnen en instructies van het management en van andere interne vereisten, 
te beoordelen. 
 
A2. 
Activiteiten die vergelijkbaar zijn met die van een interne auditfunctie, kunnen door functies onder 
een andere naam binnen een entiteit worden  uitgevoerd. Enkele of alle activiteiten van een interne 
auditfunctie kunnen tevens worden uitbesteed aan een externe dienstverlener. Noch de naam van 
de functie, noch de vraag of deze door de entiteit of door een externe dienstverlener worden 
uitgevoerd, is afzonderlijk bepalend voor de vraag of de externe auditor al dan niet gebruik kan 
maken van de werkzaamheden van de interne auditfunctie. Meer relevant zijn de aard van de 
activiteiten, de mate waarin de organisatorische positie en relevante beleidslijnen en procedures van 
de interne auditfunctie de objectiviteit van de interne auditors ondersteunen, de  competentie, en de 
systematische en gedisciplineerde benadering van de interne auditfunctie. Verwijzingen in deze ISA 
naar de werkzaamheden van de interne auditfunctie omvatten relevante activiteiten van andere 
functies of externe dienstverleners die deze kenmerken hebben.  
 
A3. 
Daarnaast zouden degenen die binnen de entiteit met operationele en bestuurlijke taken en 
verantwoordelijkheden buiten de interne auditfunctie belast zijn,   doorgaans  met bedreigingen in 
hun objectiviteit geconfronteerd worden die in het kader van deze ISA zouden verhinderen dat ze 
worden 
behandeld 
als 
onderdeel 
van 
een 
interne 
auditfunctie, 
hoewel 
zij 
interne 
beheersingsmaatregelen kunnen uitvoeren die overeenkomstig ISA 330 kunnen worden getoetst.12 
 
12  Zie par. 10.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
12/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
Om deze reden zou het monitoren van interne beheersingsmaatregelen dat door een eigenaar-
bestuurder wordt uitgevoerd niet als het equivalent worden beschouwd voor een interne auditfunctie.  
 
A4. 
Hoewel de doelstellingen van een interne auditfunctie en de externe auditor van een entiteit 
verschillen, kan de interne auditfunctie controlewerkzaamheden uitvoeren die vergelijkbaar zijn met 
de werkzaamheden die door de externe auditor worden uitgevoerd bij een controle van financiële 
overzichten. Indien dit het geval is, kan de externe auditor voor de doeleinden van de controle op 
één of meer van de volgende wijzen gebruikmaken van de interne auditfunctie: 
 
• 
Het verkrijgen van informatie die relevant is voor de inschatting door de externe auditor van 
de risico's van een afwijking van materieel belang die het gevolg is van fraude of van fouten. 
In dit opzicht vereist ISA 315 (herzien 2019)13 dat de externe auditor inzicht verwerft in de aard 
van de verantwoordelijkheden van de interne auditfunctie, haar positie binnen de organisatie 
en de activiteiten die zijn uitgevoerd, of zullen worden uitgevoerd, en het verzoeken om 
inlichtingen bij de juiste personen binnen de interne auditfunctie (als de entiteit over een 
dergelijke functie beschikt); of 
• 
Tenzij dit door wet- of regelgeving verboden of in enige mate beperkt is, kan de externe auditor 
na een adequate evaluatie besluiten om gebruik te maken van de werkzaamheden die door 
de interne auditfunctie zijn uitgevoerd gedurende de verslagperiode als gedeeltelijke 
vervanging voorcontrole-informatie die door de externe auditor14 zelf moet worden verkregen. 
 
Bovendien kan de externe auditor gebruikmaken van interne auditors om controlewerkzaamheden 
uit te voeren onder de aansturing, het toezicht en de beoordeling van de externe auditor (in deze ISA 
naar verwezen als "directe ondersteuning"), tenzij dit door wet- of regelgeving verboden of in enige 
mate beperkt is.15 
 
Het bepalen of, in welke gebieden, en in welke mate er van de werkzaamheden van de interne 
auditfunctie gebruik kan worden gemaakt. 
 
Het evalueren van de interne auditfunctie 
 
Objectiviteit en competentie (Zie par. 15(a)-(b)) 
 
A5. 
De externe auditor past professionele oordeelsvorming toe bij het bepalen of voor de doeleinden van 
de controle gebruik kan worden gemaakt van de werkzaamheden van de interne auditfunctie voor 
de doeleinden van de controle en bij het bepalen in welke mate en in welke omstandigheden daarvan 
gebruik kan worden gemaakt. 
 
A6. 
De mate waarin de organisatorische positie en de relevante beleidslijnen en procedures van de 
interne auditfunctie de objectiviteit van de interne auditors ondersteunen, alsmede het 
competentieniveau van de functie, zijn bijzonder belangrijk bij het bepalen of er van de 
werkzaamheden van de interne auditfunctie gebruik wordt gemaakt en, zo ja, bij het bepalen van de 
aard en omvang van het gebruik van de werkzaamheden van de functie dat passend is in de 
omstandigheden. 
 
A7. 
Objectiviteit verwijst naar het vermogen om die taken uit te voeren zonder toe te staan dat  tendentie, 
belangenconflict  of ongepaste invloed van anderen professionele oordeelsvorming te doorbreken. 
Factoren die van invloed kunnen zijn op de evaluatie van de externe auditor omvatten het volgende: 
 
• 
Of de organisatorische positie van de interne auditfunctie, inclusief de bevoegdheid en 
verantwoordingsplicht van de interne auditfunctie, het vermogen van de interne auditfunctie 
ondersteunt om  tendentie, belangenconflict of ongepaste invloed van anderen om  
professionele oordeelsvorming te doorbreken, te voorkomen. Bijvoorbeeld de vraag of de 
interne auditfunctie rapporteert aan de met governance belaste personen of aan een 
functionaris met de juiste bevoegdheid, of, indien de interne auditfunctie rapporteert aan het 
 
13  ISA 315 (herzien 2019), paragraaf 14(a). 
14  Zie par. 15-25. 
15  Zie par. 26-35.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
13/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
management, de vraag of de interne auditfunctie directe toegang heeft tot de met governance 
belaste personen;  
• 
Of de interne auditfunctie geen conflicterende verantwoordelijkheden heeft, zoals bestuurlijke 
of operationele verplichtingen of verantwoordelijkheden die buiten de interne auditfunctie 
vallen; 
• 
Of de met governance belaste personen toezicht houden op beslissingen over 
personeelsaangelegenheden die gerelateerd zijn aan de interne auditfunctie, zoals het 
bepalen van het gepaste beloningsbeleid; 
• 
Of de interne auditfunctie door het management of door de met governance belaste personen 
beperkingen wordt opgelegd bij, bijvoorbeeld, het communiceren van de bevindingen van de 
interne auditfunctie met de externe auditor; 
• 
Of de interne auditors lid zijn van relevante beroepsorganisaties en of hun lidmaatschap hen 
verplicht de relevante professionele standaarden na te leven die gerelateerd zijn aan 
objectiviteit, alsmede of met hun interne beleidslijnen dezelfde doelstellingen worden bereikt.  
 
A8. 
Competentie  van de interne auditfunctie verwijst naar het verkrijgen en onderhouden van kennis en 
vaardigheden van de interne auditfunctie als geheel op het vereiste niveau, om de toegewezen taken 
zorgvuldig en overeenkomstig de van toepassing zijnde professionele standaarden uit te voeren. 
Factoren die van invloed kunnen zijn op de vaststelling door de externe auditor omvatten de vraag: 
 
• 
Of de interne auditfunctie over adequate en gepaste middelen beschikt in verhouding tot de 
omvang van de entiteit en tot de aard van de uit te voeren werkzaamheden. 
• 
Of er vastgestelde beleidslijnen zijn voor het aannemen, trainen en toewijzen van interne 
auditors aan interne auditopdrachten. 
• 
Of de interne auditors adequate vaktechnische training en  vaardigheid in auditing hebben. 
Relevante criteria die door de externe auditor in overweging kunnen worden genomen bij de 
beoordeling kunnen bijvoorbeeld inhouden het aanhouden door de interne auditor van een 
relevante professionele titel en het hebben van relevante ervaring. 
• 
Of interne auditors beschikken over de vereiste kennis van de financiële verslaggeving van de 
entiteit en over het van toepassing zijnde stelsel inzake financiële verslaggeving, alsmede de 
vraag of de interne auditfunctie over de noodzakelijke vaardigheden beschikt (bijvoorbeeld 
sectorspecifieke kennis) om werkzaamheden uit te voeren met betrekking tot de financiële 
overzichten van de entiteit.  
• 
Of de interne auditors lid zijn van relevante beroepsorganisaties die hun verplichten om de 
relevante professionele standaarden na te leven, met inbegrip van vereisten inzake 
permanente educatie.  
 
A9. 
Objectiviteit en competentie kunnen worden gezien als een continuüm. Hoe meer de 
organisatorische positie en relevante beleidslijnen en procedures van de interne auditfunctie op 
adequate wijze de objectiviteit van de interne auditors ondersteunen en hoe hoger het 
competentieniveau  van de interne auditfunctie is, des te waarschijnlijker is het dat de externe auditor 
gebruik kan maken van de interne auditfunctie en dat op meerdere gebieden. Een organisatorische 
positie en relevante beleidslijnen en procedures die de objectiviteit van de interne auditors sterk 
ondersteunen, kunnen echter het gebrek aan voldoende competentie van de interne auditfunctie niet 
compenseren.. Evenmin kan een hoog competentieniveau van de interne auditfunctie een 
organisatorische positie en beleidslijnen en procedures die de objectiviteit van de interne auditors 
niet adequaat ondersteunen, compenseren.  
 
Het toepassen van een systematische en gedisciplineerde benadering. (Zie par. 15(c)) 
 
A10. Het toepassen van een systematische en gedisciplineerde benadering voor het plannen, uitvoeren, 
toezicht houden op, beoordelen en documenteren van haar activiteiten  onderscheidt de activiteiten 
van de interne auditfunctie van andere op monitoring gerichte activiteiten  interne 
beheersingmaatregelen die binnen de entiteit kunnen worden uitgevoerd.  
 
A11. Factoren die van invloed kunnen zijn op de vaststelling door de externe auditor of de interne 
auditfunctie een systematische en gedisciplineerde benadering toepast, zijn onder meer de 
volgende:

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
14/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
• 
Het bestaan, adequaat zijn en gebruik van gedocumenteerde interne auditwerkzaamheden of 
van leidraden die gebieden beslaan zoals risico-inschattingen, werkprogramma's, 
documentatie en verslaggeving, waarvan de aard en omvang in verhouding staan tot de 
grootte en de omstandigheden van een entiteit; 
• 
Of de interne auditfunctie toereikende beleidslijnen en procedures voor kwaliteitsbeheersing 
heeft, bijvoorbeeld beleidslijnen en procedures die van toepassing zouden zijn  op een interne 
auditfunctie – zoals die welke in verband staan met leiding, human resources en 
opdrachtuitvoering - of vereisten inzake kwaliteitsbeheersing voortvloeiend uit standaarden 
die door de relevante beroepsorganisaties voor interne auditors zijn opgesteld. Dergelijke 
organisaties kunnen tevens andere passende eisen vaststellen, zoals het uitvoeren van 
periodieke externe kwaliteitsbeoordelingen.  
 
Omstandigheden waarin van de werkzaamheden van de interne auditfunctie geen gebruik kan worden 
gemaakt. (Zie par. 16) 
 
A12. De evaluatie van de externe auditor of de organisatorische positie en relevante beleidslijnen en 
procedures van de interne auditfunctie op adequate wijze de objectiviteit van de interne auditors 
ondersteunen, het competentieniveau van de interne auditfunctie, en of deze een systematische en 
gedisciplineerde benadering hanteert, kan erop wijzen dat de risico's ten aanzien van de kwaliteit 
van de werkzaamheden van de interne auditfunctie te significant zijn en dat het derhalve niet gepast 
is om de werkzaamheden van de interne auditfunctie te gebruiken als controle-informatie. 
 
A13. Het in overweging nemen van de factoren in paragrafen A7, A8 en A11 van deze ISA, afzonderlijk en 
in zijn totaliteit, is van belang omdat een individuele factor vaak niet voldoende is om te concluderen 
dat er voor de doeleinden van de controle geen gebruik kan worden gemaakt van de werkzaamheden 
van de interne auditfunctie. De organisatorische positie van de interne auditfunctie is bijvoorbeeld in 
het bijzonder van belang bij het evalueren van bedreigingen voor de objectiviteit van de interne 
auditors. Indien de interne auditfunctie aan het management  rapporteert zou dit als een significante 
bedreiging voor de objectiviteit van de interne auditfunctie worden beschouwd, tenzij andere factoren 
zoals die in paragraaf A7 van deze ISA zijn beschreven gezamenlijk voldoende waarborgen 
verschaffen om de bedreiging terug te brengen naar een aanvaardbaar niveau.  
 
A14. De IESBA Code (IFAC Code)16 stelt aanvullend dat een bedreiging als gevolg van zelftoetsing 
ontstaat wanneer de externe auditor een opdracht aanneemt om aan een controlecliënt interne 
auditdiensten te leveren en van de resultaten van die diensten bij het uitvoeren van de controle 
gebruik zal worden gemaakt. Deze situatie ontstaat doordat de externe auditor gebruik zal maken 
van de resultaten van de interne  auditdienst zonder op behoorlijke wijze die resultaten te evalueren 
of zonder dat eenzelfde professioneel-kritische instelling wordt gehanteerd die zou worden 
gehanteerd wanneer de interne auditwerkzaamheden worden uitgevoerd door personen die niet tot 
het kantoor behoren. De IFAC Code17 behandelt de verboden die in bepaalde omstandigheden van 
toepassing zijn, alsmede de bedreigingen en waarborgen die kunnen worden toegepast om de 
bedreigingen terug te brengen tot een aanvaardbaar niveau in andere omstandigheden.  
 
Het bepalen van de aard en omvang van de werkzaamheden van de interne auditfunctie waarvan gebruik 
kan worden gemaakt. 
 
Factoren van invloed op de bepaling van de aard en omvang van de werkzaamheden van de interne 
auditfunctie waarvan gebruik kan worden gemaakt. (Zie par. 17-19) 
 
A15. Zodra de externe auditor heeft bepaald dat er van de werkzaamheden van de interne auditfunctie 
voor de doeleinden van de controle gebruik kan worden gemaakt, is een eerste overweging of de 
geplande aard en reikwijdte van de werkzaamheden van de interne auditfunctie die zijn uitgevoerd, 
of gepland zijn om te worden uitgevoerd, relevant zijn voor de algehele controleaanpak die en het 
 
16  The International Ethics Standards Board for Accountants’ (IESBA) Code of Ethics for Professional Accountants (IFAC Code), 
Section 290.194. 
17  IFAC Code, Section 290.190–290.195.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
15/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
controleprogramma dat de externe auditor overeenkomstig ISA 30018 heeft opgesteld. 
  
A16. Voorbeelden van werkzaamheden van de interne auditfunctie waarvan door de externe auditor 
gebruik kan worden gemaakt zijn: 
 
• 
Het toetsen van de werking van interne beheersingsmaatregelen. 
• 
Gegevensgerichte werkzaamheden met een beperkte mate van oordeelsvorming. 
• 
Observaties van voorraadopnames. 
• 
Het volgen van transacties door het voor de financiële verslaggeving relevante 
informatiesysteem. 
• 
Het toetsen van het naleven van vereisten op grond van wet- of regelgeving. 
• 
In sommige omstandigheden, controles of beoordelingen van de financiële informatie van 
dochtermaatschappijen die geen significante groepsonderdelen van de groep zijn (waar dit 
niet strijdig is met de vereisten van ISA 600)19. 
 
A17. De vaststelling door de externe auditor van de geplande aard en mate van het gebruik van de 
werkzaamheden van de interne auditfunctie zal worden beïnvloed door de evaluatie van de externe 
auditor van de mate waarin de organisatorische positie en de relevante beleidslijnen en procedures 
van de interne auditfunctie op adequate wijze de objectiviteit van de interne auditors ondersteunen, 
alsmede door het competentieniveau van de interne auditfunctie in paragraaf 18 van deze ISA. 
Bovendien zijn zowel de mate van oordeelsvorming die noodzakelijk is bij het plannen, uitvoeren en 
evalueren van dergelijke werkzaamheden, als het ingeschatte risico van een afwijking van materieel 
belang op het niveau van beweringen inputs voor de vaststelling door de externe auditor. Verder zijn 
er omstandigheden waarin de externe auditor voor de doeleinden van de controle geen gebruik kan 
maken van de werkzaamheden van de interne auditfunctie, zoals in paragraaf 16 van deze ISA staat 
beschreven. 
 
Oordeelsvorming bij het plannen en uitvoeren van controlewerkzaamheden en het evalueren van 
resultaten. (Zie par. 18(a) en 30(a)) 
 
A18. Hoe groter het belang van de oordeelsvorming toe te passen bij het plannen en uitvoeren van de 
controlewerkzaamheden en bij het evalueren van de controle-informatie is, des te meer 
werkzaamheden zullen overeenkomstig paragraaf 18 van deze ISA door de externe auditor zelf uit 
te voeren, omdat gebruikmaken van de werkzaamheden van de interne auditfunctie alleen niet 
voldoende geschikte controle-informatie aan de externe auditor zal verschaffen.  
 
A19. Aangezien de externe auditor de ongedeelde verantwoordelijkheid heeft voor het controleoordeel dat 
tot uitdrukking wordt gebracht, is het noodzakelijk dat de externe auditor in de controleopdracht 
significante 
oordeelsvormingen 
uitvoert 
overeenkomstig 
paragraaf 
18. 
Significante 
oordeelsvormingen omvatten het volgende: 
 
• 
Het inschatten van de risico’s van een afwijking van materieel belang; 
• 
Het evalueren of de uitgevoerde toetsingen voldoende zijn; 
• 
Het evalueren van de geschiktheid van het hanteren door het management van de 
continuïteitsveronderstelling; 
• 
Het evalueren van significante schattingen; en  
• 
Het evalueren van de toereikendheid van de in de financiële overzichten opgenomen 
toelichtingen, en andere aangelegenheden die de controleverklaring beïnvloeden. 
 
Ingeschat risico van een afwijking van materieel belang. (Zie par. 18(b)) 
 
A20. Voor een bepaald rekeningsaldo en een bepaalde transactiestroom of  toelichting geldt dat hoe hoger 
een ingeschat risico op een afwijking van materieel belang op het niveau van beweringen is, des te 
meer oordeelsvorming er vaak betrokken is bij het plannen en uitvoeren van de 
 
18  ISA 300, Planning van een controle van financiële overzichten. 
19  ISA 600, Speciale overwegingen – Controles van financiële overzichten van de groep (inclusief de werkzaamheden van auditors 
van groepsonderdelen).

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
16/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
controlewerkzaamheden en het evalueren van de uitkomsten daarvan. In dergelijke omstandigheden 
zal het nodig zijn dat de externe auditor meer werkzaamheden overeenkomstig paragraaf 18 van 
deze ISA zelf uitvoert, en derhalve minder gebruikmaken van de werkzaamheden van de interne 
auditfunctie bij het verkrijgen van voldoende en geschikte controle-informatie. Verder geldt, zoals 
uitgelegd in ISA 20020, naarmate de risico's van een afwijking van materieel belang hoger zijn, des 
te overtuigender de controle-informatie moet zijn die door externe auditor wordt vereist, en het nodig 
is des te meer werkzaamheden de externe auditor dus zelf zal uitvoeren.  
 
A21. Zoals in ISA 315 (herzien 2019)21 wordt uitgelegd, zijn significante risico’s die aan de bovengrens 
van het spectrum van inherent risico worden ingeschat en zal de mogelijkheid van de auditor om 
gebruik te maken van de interne auditfunctie met betrekking tot significante risico's daardoor worden 
beperkt tot werkzaamheden die een beperkte oordeelsvorming vergen. Bovendien is het 
onwaarschijnlijk dat in die gevallen waar de risico's op een afwijking van materieel belang anders 
zijn dan laag, het gebruikmaken van de werkzaamheden van de interne auditfunctie op zichzelf, het 
controlerisico terugbrengt tot een aanvaardbaar niveau terug brengt. Het gebruikmaken van 
werkzaamheden van de interne auditfunctie elimineert niet de noodzaak van de auditor sommige 
toetsingen zelf uit te voeren. 
  
A22. Het uitvoeren van werkzaamheden overeenkomstig deze ISA kan voor de externe auditor aanleiding 
vormen om de inschatting door de externe auditor van de risico’s van een afwijking van materieel 
belang opnieuw te evalueren. Deze evaluatie kan ook de vaststelling door de externe auditor van de 
vraag of er van de werkzaamheden van interne auditfunctie gebruik kan worden gemaakt en of 
verdere toepassing van deze ISA noodzakelijk is, beïnvloeden.  
 
Communicatie met de met governance belaste personen. (Zie par. 20) 
 
A23. Overeenkomstig ISA 260 (herzien)22 wordt van de externe auditor vereist om de met governance 
belaste personen een overzicht van de geplande reikwijdte en timing van de controle te geven. Het 
geplande gebruik van de werkzaamheden van de interne auditfunctie Vormt een integrerend 
onderdeel van de algehele controleaanpak van de externe auditor en is derhalve relevant voor de 
met governance belaste personen met betrekking tot hun inzicht in de voorgestelde controleaanpak.  
 
Het gebruikmaken van de werkzaamheden van de interne auditfunctie 
 
Het bespreken en coördineren met de interne auditfunctie (Zie par. 21) 
 
A24. Bij het bespreken van het geplande gebruik van hun werkzaamheden met de interne auditfunctie als 
basis voor het coördineren van de respectievelijke activiteiten, kan het nuttig zijn om het volgende 
aan de orde te stellen: 
 
• 
De timing van dergelijke werkzaamheden; 
• 
De aard van de uitgevoerde werkzaamheden; 
• 
De mate waarin de risico’s door de audit worden afgedekt; 
• 
De materialiteit voor de financiële overzichten als geheel (en, indien van toepassing, het 
materialiteitsniveau 
of 
de 
materialiteitsniveaus 
voor 
bepaalde 
transactiestromen, 
rekeningsaldi en opgenomen toelichtingen) en de uitvoeringsmaterialiteit; 
• 
Voorgestelde methoden voor het selecteren van items en steekproefomvangen; 
• 
Documentatie van de uitgevoerde werkzaamheden; 
• 
Procedures voor beoordeling en rapporteren.  
 
A25. Coördinatie tussen de externe auditor en de interne auditfunctie is effectief wanneer bijvoorbeeld: 
 
• 
Besprekingen met passende intervallen plaatsvinden gedurende de verslagperiode. 
• 
De externe auditor de interne auditors informeert over significante aangelegenheden die de 
 
20  ISA 200, paragraaf A32. 
21  ISA 315 (herzien 2019), paragraaf 12(l). 
22  ISA 260 (herzien), paragraaf 15.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
17/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
interne auditfunctie zouden kunnen beïnvloeden. 
• 
De externe auditor op de hoogte wordt gebracht van of toegang heeft tot relevante rapportages 
van de interne auditfunctie en wordt geïnformeerd over significante aangelegenheden die 
onder de aandacht van de interne auditfunctie zijn gekomen wanneer dergelijke 
aangelegenheden de werkzaamheden van de externe auditor kunnen beïnvloeden, zodat de 
externe auditor in staat is de implicaties van dergelijke aangelegenheden voor de 
controleopdracht in overweging te nemen.  
 
A26. ISA 20023 behandelt het belang van planning en uitvoering van de controle met een professioneel-
kritische instelling door de externe auditor, inclusief het alert zijn op informatie die de 
betrouwbaarheid van documenten en reacties op verzoeken om inlichtingen die als controle-
informatie worden gebruikt, ter discussie stelt. Derhalve kan communicatie met de interne 
auditfunctie gedurende de uitvoering van de opdracht gelegenheid bieden aan interne auditors om 
aangelegenheden die de werkzaamheden van de externe auditor kunnen beïnvloeden onder de 
aandacht van de externe auditor te brengen.24 De externe auditor is dan in staat om met dergelijke 
informatie rekening houden bij het identificeren en inschatten van risico's van een afwijking van 
materieel belang.  
 
Bovendien, indien dergelijke informatie kan wijzen op een verhoogd risico van een afwijking van 
materieel belang in de financiële overzichten, of op gevallen van fraude die zich hebben voorgedaan, 
gevallen van vermoede fraude of aantijgingen van fraude, is de externe auditor in staat om hiermee 
rekening te houden bij het identificeren van een risico van een afwijking van materieel belang als 
gevolg van fraude overeenkomstig ISA 240.25 
 
Procedures om het adequaat zijn van de werkzaamheden van de interne auditfunctie te bepalen (Zie par. 
23-24) 
 
A27. De controlewerkzaamheden van de externe auditor betreffende het geheel van de werkzaamheden 
van de interne auditfunctie als geheel waarvan de externe auditor van plan is deze te gebruiken, 
bieden een basis voor het evalueren van de algehele kwaliteit van de werkzaamheden van de interne 
auditfunctie en de objectiviteit waarmee ze zijn uitgevoerd.  
 
A28. De werkzaamheden die de externe auditor kan uitvoeren om de kwaliteit van de uitgevoerde 
werkzaamheden en de conclusies die door de interne auditfunctie zijn getrokken te evalueren, ter 
aanvulling op het opnieuw uitvoeren overeenkomstig paragraaf 24, omvatten: 
 
• 
Het verzoeken om inlichtingen bij de juiste personen binnen de interne auditfunctie; 
• 
Het observeren van werkzaamheden die door de interne auditfunctie worden uitgevoerd; 
• 
Het beoordelen van het werkprogramma en de werkdocumenten van de interne auditfunctie.  
 
A29. Het is noodzakelijk dat de externe auditor meer werkzaamheden uitvoert op het geheel  van de 
werkzaamheden van de interne auditfunctie, om de beslissing te ondersteunen om gebruik te maken 
van de werkzaamheden van de interne auditfunctie bij het verkrijgen van voldoende en geschikte 
controle-informatie waarop het controleoordeel wordt gebaseerd. Dit geldt des te meer naarmate: 
 
• 
Meer oordeelsvorming nodig is; 
• 
Het ingeschatte risico van een afwijking van materieel belang hoger is; 
• 
De organisatorische positie en relevante beleidslijnen en procedures van de interne 
auditfunctie minder op adequate wijze de objectiviteit van de interne auditors ondersteunen; 
of 
• 
Het competentieniveau van de interne auditfunctie als lager wordt ingeschat.  
 
Het opnieuw uitvoeren (Zie par. 24) 
 
23  ISA 200, paragrafen 15 en A24. 
24  ISA 315 (herzien 2019), Bijlage 4. 
25  ISA 315 (herzien 2019), Bijlage 4 met betrekking tot ISA 240, De verantwoordelijkheid van de auditor met betrekking tot fraude in 
het kader van een controle van financiële overzichten.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
18/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
 
A30. In het kader van deze ISA heeft het opnieuw uitvoeren betrekking op het onafhankelijk uitvoeren van 
werkzaamheden door de externe auditor om de conclusies die door de interne auditfunctie zijn 
getrokken, te valideren. Deze doelstelling kan worden bereikt door items te onderzoeken die reeds 
door de interne auditfunctie zijn onderzocht, of, waar het niet mogelijk is om dit te doen, kan dezelfde 
doelstelling tevens worden bereikt door voldoende andere vergelijkbare items te onderzoeken die 
niet daadwerkelijk door de interne auditfunctie zijn onderzocht. Het opnieuw uitvoeren verschaft meer 
overtuigende onderbouwing van de toereikendheid van de werkzaamheden van de interne 
auditfunctie in vergelijking met andere werkzaamheden die de externe auditor in paragraaf A28 kan 
uitvoeren. Het is voor de externe auditor niet noodzakelijk dat hij op elk gebied waarvoor hij gebruik 
maakt van de werkzaamheden van de interne auditfunctie deze werkzaamheden opnieuw uitvoert, 
echter het in bepaalde mate opnieuw uitvoeren inzake het geheel van de werkzaamheden van de 
interne auditfunctie waar de auditor van plan is gebruik te maken, is in overeenstemming met 
paragraaf 24. Het is waarschijnlijk dat de externe auditor bij het opnieuw uitvoeren focust op die 
gebieden waar er door de interne auditfunctie meer oordeelsvorming is toegepast bij het plannen, 
uitvoeren en evalueren van de uitkomsten van de controlewerkzaamheden en in gebieden met een 
hoger risico op een afwijking van materieel belang.  
 
Bepalen of, in welke gebieden, en in welke mate er gebruik kan worden gemaakt van interne auditors 
om directe ondersteuning te verschaffen 
 
Het bepalen of er gebruik kan worden gemaakt van interne auditors om directe ondersteuning te 
verschaffen voor de doeleinden van de controle  (Zie par. 5, 26-28)  
 
A31. Er zijn rechtsgebieden waar het de externe auditor door wet- of regelgeving wordt verboden om 
gebruik te maken van interne auditors om directe ondersteuning te verschaffen. Dan is het voor de 
auditors op groepsniveau relevant om te overwegen of dit verbod ook geldt voor auditors van een 
groepsonderdeel en, zo ja, om hierop in te spelen in de communicatie met de auditors van de 
groep.26 
 
A32. Zoals in paragraaf A7 van deze ISA staat vermeld, verwijst objectiviteit naar het vermogen om het 
voorgestelde werk uit te voeren zonder ruimte te bieden aan  tendentie, belangenconflicten of 
ongepaste invloed van anderen om professionele oordeelsvormingen te doorbreken. Bij het 
evalueren van het bestaan en de significantie van bedreigingen voor de objectiviteit van een interne 
auditor, kunnen de volgende factoren relevant zijn: 
 
• 
De mate waarin de organisatorische status en relevante beleidslijnen en procedures van de 
interne auditfunctie de objectiviteit van de interne auditors ondersteunen27; 
• 
Familie- en persoonlijke relaties met een individu die werkzaam is in het gebied van de entiteit 
waar de werkzaamheden betrekking op hebben, of die hier verantwoordelijk voor is.  
• 
Associatie met het onderdeel of de afdeling binnen de entiteit waar de werkzaamheden 
betrekking op hebben. 
• 
Significante financiële belangen binnen de entiteit anders dan beloning volgens voorwaarden 
die consistent zijn met degene die van toepassing zijn op andere werknemers op een 
soortgelijk niveau van senioriteit.   
 
Materiaal dat door relevante beroepsorganisaties voor interne auditors wordt uitgebracht kan 
aanvullende nuttige leidraden bevatten. 
 
A33. Er kunnen ook bepaalde omstandigheden zijn waarin de significantie van de bedreigingen voor de 
objectiviteit van een interne auditor zodanig is dat er geen waarborgen zijn die deze terug zouden 
kunnen brengen tot een aanvaardbaar niveau. Het adequaat zijn van waarborgen wordt bijvoorbeeld 
door de significantie van de werkzaamheden in de context van de controle beïnvloed. Daarom is het 
op grond van paragraaf 30 (a) en (b) verboden   gebruik te maken van interne auditors om directe 
ondersteuning te verschaffen met betrekking tot het uitvoeren van werkzaamheden die te maken 
 
26  ISA 600, paragraaf 40(b). 
27  Zie par. A7.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
19/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
hebben met het vormen van significante oordelen in de controle of die te maken hebben met hogere 
risico's op een afwijking van materieel belang waar het oordeel dat vereist is bij het uitvoeren van 
relevante controlewerkzaamheden of bij het evalueren van de verzamelde controle-informatie meer 
dan beperkt is. Dit zou tevens het geval zijn waar de betrokken werkzaamheden een bedreiging als 
gevolg van zelftoetsing vormen, wat de reden is dat het interne auditors verboden wordt om 
werkzaamheden uit te voeren in de omstandigheden beschreven in paragraaf 30 (c) en (d).  
 
A34. Bij het evalueren van het competentieniveau van een interne auditor kunnen vele factoren in 
paragraaf A8 van deze ISA ook relevant zijn, toegepast in de context van individuele interne auditors 
en de werkzaamheden die hun kunnen worden toegewezen. 
 
Het bepalen van de aard en omvang van het werk dat kan worden toegewezen aan interne auditors die 
directe ondersteuning verschaffen (Zie par. 29-31)  
 
A35. Paragrafen A15-A22 van deze ISA verschaffen relevante leidraden bij het bepalen van de aard en 
omvang van de werkzaamheden die aan interne auditors kunnen zijn toegewezen. 
 
A36. Bij het bepalen van de aard van de werkzaamheden die aan interne auditors kunnen worden 
toegewezen is de externe auditor behoedzaam om dergelijke werkzaamheden te beperken tot die 
gebieden die geschikt zijn om te worden toegewezen. Voorbeelden van activiteiten en taken die niet 
geschikt zouden zijn om gebruik te maken van interne auditors om directe ondersteuning te 
verschaffen omvatten de volgende: 
 
• 
Bespreking van frauderisico's. De externe auditors kunnen echter overeenkomstig ISA 315 
(herzien 2019)28 bij interne auditors verzoeken om inlichtingen over frauderisico's binnen de 
organisatie; 
• 
Het bepalen van niet-aangekondigde controlewerkzaamheden zoals in ISA 240 wordt 
behandeld. 
 
A37. Aangezien het van de externe auditor, overeenkomstig ISA 50529,  vereist is om externe 
confirmatieverzoeken te blijven beheersen en de resultaten van externe confirmatiewerkzaamheden 
te evalueren, zou het op soortgelijke wijze niet passend zijn om deze verantwoordelijkheden toe te 
wijzen aan interne auditors.  Interne auditors kunnen echter ondersteunen bij het samenstellen van 
informatie die voor de externe auditor noodzakelijk is om uitzonderingen in reacties op confirmaties 
af te handelen. 
 
A38. De mate van betrokken oordeelsvorming en het risico van een afwijking van materieel belang zijn 
tevens relevant bij het bepalen van de werkzaamheden die aan interne auditors die directe 
ondersteuning verschaffen kunnen worden toegewezen. In omstandigheden waar bijvoorbeeld de 
waardering van de vorderingen wordt ingeschat als een gebied met een hoger risico zou de externe 
auditor het checken van de juistheid van de ouderdom van deze vorderingen kunnen toewijzen aan 
een interne auditor die directe ondersteuning verschaft. Omdat de evaluatie van de toereikendheid 
van de voorziening op basis van de ouderdom echter meer dan beperkte oordeelsvorming zou 
inhouden, zou het niet passend zijn om de laatstgenoemde taak aan een interne auditor die directe 
ondersteuning verschaft toe te wijzen.  
 
A39. Ongeacht de aansturing, het toezicht en de beoordeling door de externe auditor kan het overmatig 
gebruik van interne auditors die directe ondersteuning verschaffen, percepties beïnvloeden met 
betrekking tot de onafhankelijkheid in het kader van de externe controleopdracht.  
 
Gebruikmaken van interne auditors om directe ondersteuning te verschaffen (Zie par. 34) 
 
A40. Individuen binnen de interne auditfunctie zijn niet onafhankelijk van de entiteit zoals van de externe 
auditor wordt vereist bij het tot uitdrukking brengen van een oordeel over de financiële overzichten. 
Daarom zal de betrokkenheid van de externe auditor bij het aansturen van, toezicht houden op, en 
 
28  ISA 315 (herzien 2019), paragraaf 14(a). 
29  ISA 505, Externe confirmaties, paragrafen 7 en 16.

GEBRUIKMAKEN VAN DE WERKZAAMHEDEN VAN INTERNE AUDITORS 
ISA 610 (herzien 2013) 
NBA-IBR 2022 
20/20 
 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2023 
beoordelen van de werkzaamheden die door interne auditors zijn uitgevoerd, over het algemeen van 
een andere aard en uitgebreider zijn dan wanneer leden van het opdrachtteam de werkzaamheden 
uitvoeren.  
 
A41. Bij het aansturen van interne auditors kan de externe auditor de interne auditors er bijvoorbeeld aan 
herinneren om issues op het gebied van financiële verslaggeving en controle die tijdens de controle 
zijn onderkend, onder de aandacht van de externe auditor te brengen.  Bij het beoordelen van de 
werkzaamheden die door de interne auditors zijn uitgevoerd, omvatten de overwegingen van de 
externe auditor de vraag of de verkregen onderbouwende informatie in de omstandigheden 
voldoende en geschikt is, alsmede dat deze informatie de getrokken conclusies ondersteunt.