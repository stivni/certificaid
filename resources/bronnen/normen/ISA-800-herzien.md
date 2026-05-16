---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ISA 800 (herzien) — Bijzondere overwegingen — Controles van financiële overzichten
  die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs:
  - id: https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/isa-800-herzien-def.pdf
    sha256: 0fd732a628d76f3b2436363d4cbf4c9351f019c1003ca630dc1efc06ff56ab4f
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
title: ISA 800 (herzien) — Bijzondere overwegingen — Controles van financiële overzichten
  die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden
uitgever: IAASB / IBR-IRE (NL-vertaling)
---

# ISA 800 (herzien) — Bijzondere overwegingen — Controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden

> Bron: [IBR-IRE PDF](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/isa-800-herzien-def.pdf) — gedownload 2026-05-16.  
> SHA-256: `0fd732a628d76f3b2436363d4cbf4c9351f019c1003ca630dc1efc06ff56ab4f`  
> Trust-status: `unreviewed` — automatisch geconverteerd uit PDF; nog te valideren door QA-pass.

---

Internationale controlestandaard (herzien) 
ISA 800 (herzien)  
bijzondere overwegingen - controles 
van financiële overzichten die zijn 
opgesteld in overeenstemming met 
stelsels voor bijzondere doeleinden

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
toestemming van IFAC. Het proces voor het vertalen van de Internationale controlestandaard (ISA) 800 
(herzien) is onderzocht door IFAC en de vertaling werd uitgevoerd in overeenstemming met de Policy 
Statement de l’IFAC – Policy for Translating and Reproducing Standards published by IFAC. De 
goedgekeurde Internationale controlestandaard (ISA) 800 (herzien) is gepubliceerd door IFAC in de 
Engelse taal. IFAC aanvaardt geen verantwoordelijkheid voor de juistheid en volledigheid van de 
vertaling, noch voor handelingen die daaruit kunnen voortvloeien. 
Tekst in de Engelse taal van de Internationale controlestandaard (ISA) 800 (herzien) Bijzondere 
overwegingen - controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels 
voor bijzondere doeleinden © 2022 van de International Federation of Accountants (IFAC). Alle rechten 
voorbehouden. 
Tekst in de Nederlandse taal van de Internationale controlestandaard (ISA) 800 (herzien) Bijzondere 
overwegingen - controles van financiële overzichten die zijn opgesteld in overeenstemming met stelsels 
voor bijzondere doeleinden © 2025 van de International Federation of Accountants (IFAC). Alle rechten 
voorbehouden. 
Originele titel: International Standard on Auditing (ISA) 800 (Revised), Special Considerations—Audits 
of Financial Statements Prepared in Accordance with Special Purpose Frameworks. 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and 
Related Services Pronouncements, 2022 Edition Volume I - ISBN number: 978-1-60815-546-0. 
 
Neem contact op met permissions@ifac.org voor toestemming om dit document te reproduceren, op te 
slaan of door te geven, of voor ander soortgelijk gebruik van dit document.

INTERNATIONALE CONTROLESTANDAARD 800 (HERZIEN) 
 
BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE 
OVERZICHTEN DIE ZIJN OPGESTELD IN OVEREENSTEMMING 
MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
(Van toepassing op controles van financiële overzichten over verslagperioden die op of na 15 
december 2016 worden afgesloten)) (*) 
(*) De wijzigingen in de huidige Nederlandse versie van de ISA 800 ten opzichte van de vorige 
versie van 2009 hebben voornamelijk betrekking op de inhoud van het rapport dat op basis van de 
ISA 700 (herzien) is opgesteld, evenals bepaalde bepalingen uit de normen ISA 260 (herzien), 570 
(herzien), 705 (herzien) en 706 (herzien). 
 
 
 
INHOUDSOPGAVE 
Paragraaf 
Inleiding 
Toepassingsgebied van deze ISA ........................................................................................................... 1-3 
Ingangsdatum ........................................................................................................................................ 4 
Doelstelling ................................................................................................................................................ 5 
Definities ............................................................................................................................................ 6-7 
Vereisten 
Overwegingen bij het aanvaarden van de opdracht ............................................................................... 8 
Overwegingen bij het plannen en uitvoeren van de controle ............................................................ 9-10 
Het vormen van een oordeel en overwegingen bij het rapporteren ................................................ 11-14 
Toepassingsgerichte en overige verklarende teksten 
Definitie van een stelsel voor bijzondere doeleinden ............. Error! Reference source not found.-A4 
Overwegingen bij het aanvaarden van de opdracht .......................................................................... A5-A8 
Overwegingen bij het plannen en uitvoeren van de controle Error! Reference source not found.-A12 
Het vormen van een oordeel en overwegingen bij het rapporterenError! Reference source not found.-
A21 
Bijlage :  
Voorbeelden van controleverklaringen van de onafhankelijke auditor betreffende financiële 
overzichten voor bijzondere doeleinden 
 
International Standard on Auditing (ISA) 800 (herzien), Bijzondere overwegingen – Controles van 
financiële overzichten die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden, 
moet worden gelezen in samenhang met ISA 200, Algehele doelstellingen van de onafhankelijke 
auditor, alsmede het uitvoeren van een controle overeenkomstig de International Standards on 
Auditing.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD 
IN OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
ISA 800 (herzien)  
NBA – IBR 2025 
4/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Versie 2025 
 
Inleiding 
Toepassingsgebied van deze ISA 
 
1. 
De International Standards on Auditing (ISA’s) in de reeksen 100 tot en met 700 zijn van 
toepassing op een controle van financiële overzichten. Deze ISA behandelt speciale 
overwegingen bij de toepassing van die  ISA’s bij een controle van financiële overzichten die zijn 
opgesteld in overeenstemming met een stelsel voor bijzondere doeleinden. 
2. 
Deze ISA is geschreven in de context van een volledige set van financiële overzichten die zijn 
opgesteld in overeenstemming met stelsels voor bijzondere doeleinden. ISA 805 (herzien)1 
behandelt speciale overwegingen die relevant zijn voor een controle van een enkel financieel 
overzicht of een specifiek(e) element, rekening of item van een financieel overzicht. 
3. 
Deze ISA doet geen afbreuk aan de vereisten van de andere ISAs; noch behandelt deze ISA alle 
speciale overwegingen die relevant kunnen zijn in de omstandigheden van de opdracht. 
Ingangsdatum 
4. 
Deze ISA is van toepassing op controles van financiële overzichten over verslagperioden die op 
of na 15 december 2016 worden afgesloten. 
Doelstelling 
5. 
De doelstelling van de auditor bij het toepassen van de ISA’s bij een controle van financiële 
overzichten die zijn opgesteld in overeenstemming met stelsels voor bijzondere doeleinden is het 
op passende wijze behandelen van de speciale overwegingen die relevant zijn voor: 
a) 
de aanvaarding van de opdracht; 
b) 
het plannen en uitvoeren van die opdracht; en 
c) 
het vormen van een oordeel en het rapporteren over de financiële overzichten. 
Definities 
6. 
In het kader van de ISA’s hebben de volgende termen de hieronder weergegeven betekenissen: 
a) 
Financiële overzichten voor bijzondere doeleinden – Financiële overzichten die zijn 
opgesteld in overeenstemming met een stelsel voor bijzondere doeleinden. (Zie Par. A4) 
b) 
Stelsel voor bijzondere doeleinden – Een stelsel inzake financiële verslaggeving dat is 
opgezet om te voldoen aan de informatiebehoeften van specifieke gebruikers. Het stelsel 
inzake financiële verslaggeving kan een getrouw-beeld-stelsel of een compliance-stelsel 
zijn.2 (Zie Par. A1, tot en met A4) 
7. 
Met de term ‘financiële overzichten’ wordt in deze ISA aangeduid ‘een volledige set van financiële 
overzichten voor bijzondere doeleinden. De vereisten van het van toepassing zijnde stelsel inzake 
financiële verslaggeving bepalen de presentatie, structuur en inhoud van de financiële 
overzichten, alsmede waaruit een volledige set van financiële overzichten bestaat. Verwijzing 
naar ‘financiële overzichten voor bijzondere doeleinden’ omvat de daarop betrekking hebbende 
toelichtingen.
 
1  
ISA 805 (herzien), Bijzondere overwegingen – controles van een enkel financieel overzicht en controles van specifieke 
elementen, rekeningen of posten van een financieel overzicht 
2  
ISA 200, Algehele doelstellingen van de onafhankelijke auditor, alsmede het uitvoeren van een controle overeenkomstig 
de international standard on auditing, paragraaf 13(a)

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD 
IN OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
ISA 800 (herzien)  
NBA – IBR 2025 
5/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
Versie 2025 
 
 
Vereisten 
Overwegingen bij het aanvaarden van de opdracht 
Aanvaardbaarheid van het stelsel inzake financiële verslaggeving 
 
8. 
ISA 210 vereist van de auditor om de aanvaardbaarheid te bepalen van het stelsel inzake 
financiële verslaggeving dat is toegepast bij het opstellen van de financiële overzichten.3 Bij een 
controle van financiële overzichten voor bijzondere doeleinden dient de auditor inzicht te 
verwerven in: (Zie Par. A5, A6, A7 en A8) 
a)       het doel waarvoor de financiële overzichten worden opgesteld; 
b) 
de beoogde gebruikers; en 
c) 
de door het management ondernomen stappen om te bepalen dat het van toepassing 
zijnde stelsel inzake financiële verslaggeving aanvaardbaar is in de gegeven 
omstandigheden. 
Overwegingen bij het plannen en uitvoeren van de controle 
 
9. 
ISA 200 vereist van de auditor om alle ISA’s die relevant zijn voor de controle na te leven.4 Bij het 
plannen en uitvoeren van een controle van financiële overzichten voor bijzondere doeleinden 
dient de auditor te bepalen of het toepassen van de ISA’s speciale overweging vereist in de 
omstandigheden van de opdracht. (Zie Par. A9, A10, A11 en A12) 
10. 
ISA 315 (herzien in 2019) vereist van de auditor om inzicht te verwerven in de keuze en de 
toepassing van de grondslagen voor financiële verslaggeving door de entiteit.5 Indien de 
financiële overzichten zijn opgesteld in overeenstemming met de bepalingen van een contract, 
dient de auditor inzicht te verwerven in alle significante interpretaties van het contract die het 
management heeft gemaakt bij het opstellen van die financiële overzichten. Een interpretatie is 
significant als het aannemen van een andere redelijke interpretatie een van materieel belang 
zijnde verschil zou opleveren in de informatie zoals deze is weergegeven in de financiële 
overzichten. 
Het vormen van een oordeel en overwegingen bij het rapporteren 
 
11. 
Bij het vormen van een oordeel en het rapporteren over financiële overzichten voor bijzondere 
doeleinden dient de auditor de vereisten zoals omschreven in ISA 700 (herzien) 6 toe te 
passen. (Zie Par. A13, A14, A15, A16, A17, A18 en A19) 
Beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving 
 
12. 
ISA 700 (herzien) vereist van de auditor om te evalueren of de financiële overzichten op adequate 
wijze naar het van toepassing zijnde stelsel voor financiële verslaggeving verwijzen danwel dit 
beschrijven. 7 Indien de financiële overzichten zijn opgesteld in overeenstemming met de 
bepalingen in een contract dient de auditor te evalueren of de financiële overzichten alle 
significante interpretaties van het contract waarop de financiële overzichten zijn gebaseerd op 
adequate wijze beschrijven. 
13. 
ISA 700 (herzien) behandelt de vorm en inhoud van de controleverklaring inclusief de specifieke 
volgorde voor bepaalde elementen. In het geval van een controleverklaring betreffende financiële 
overzichten voor bijzondere doeleinden: 
a) dient de controleverklaring tevens het doel te beschrijven waarvoor de financiële overzichten 
zijn opgesteld en, indien noodzakelijk, de beoogde gebruikers, dan wel te verwijzen naar een 
toelichting in de financiële overzichten voor bijzondere doeleinden die deze informatie bevat; 
en 
 
3  
ISA 210, Overeenkomen van de voorwaarden van controleopdrachten, lid  6 a). 
4  
ISA 200, paragraaf 18 
5  
ISA 315 (herzien in 2019), Risico’s op een afwijking van materieel belang identificeren en inschatten, lid 19 b). 
6  
ISA 700 (herzien), Het vormen van een oordeel en het rapporteren over financiële overzichten. 
7  
ISA 700 (herzien), paragraaf 15.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
b) indien het management de keuze heeft uit verschillende stelsels inzake financiële verslaggeving 
bij het opstellen van de betreffende financiële overzichten, dient de uiteenzetting van de 
verantwoordelijkheid van het management 8 voor de financiële overzichten tevens te verwijzen 
naar de verantwoordelijkheid van het management om te bepalen of het van toepassing zijnde 
stelsel inzake financiële verslaggeving aanvaardbaar is in de gegeven omstandigheden. 
De lezers er op attenderen dat de financiële overzichten zijn opgesteld in overeenstemming met een 
stelsel voor bijzondere doeleinden 
 
14. 
De controleverklaring betreffende financiële overzichten voor bijzondere doeleinden dient een 
paragraaf ter benadrukking van bepaalde aangelegenheden te bevatten die de lezers van de 
controleverklaring 
erop 
attendeert dat 
de financiële 
overzichten zijn opgesteld in 
overeenstemming met een stelsel voor bijzondere doeleinden en dat de financiële overzichten 
derhalve ongeschikt kunnen zijn voor een ander doel. (Zie Par. A20 en A21) 
 
*** 
Toepassingsgerichte en overige verklarende teksten 
Definitie van een stelsel voor bijzondere doeleinden (Zie Par. 6) 
 
A1. 
Voorbeelden van stelsels voor bijzondere doeleinden zijn: 
• 
fiscale verslaggevingsgrondslagen voor een set van financiële overzichten die wordt 
toegevoegd aan de belastingaangifte van de entiteit; 
• 
een verslaggeving op kasbasis voor kasstroominformatie die een entiteit gevraagd wordt 
op te stellen ten behoeve van crediteuren; 
• 
de door een regelgever of toezichthouder vastgestelde bepalingen inzake financiële 
verslaggeving om te voldoen aan de vereisten van die regelgever of toezichthouder; of 
• 
de bepalingen inzake financiële verslaggeving van een contract, van bijvoorbeeld een 
obligatie emissie-overeenkomst, een leningsovereenkomst, of een projectsubsidie. 
A2.   Er kunnen zich omstandigheden voordoen waarbij een stelsel voor bijzondere doeleinden is 
gebaseerd op een stelsel inzake financiële verslaggeving dat is vastgesteld door een 
geautoriseerde of erkende instantie die standaarden vaststelt (standards setting organization) 
dan wel gebaseerd is op wet- of regelgeving, maar dat niet voldoet aan alle vereisten van dat 
stelsel. Een voorbeeld is een contract dat van financiële overzichten vereist om te worden 
opgesteld overeenkomstig de meeste, maar niet alle, vereisten van de standaarden voor 
financiële verslaggeving van rechtsgebied X. Wanneer het bovenstaande in de omstandigheden 
van de opdracht aanvaardbaar is, is het niet passend om in de omschrijving van het van 
toepassing zijnde stelsel inzake financiële verslaggeving die in de financiële overzichten voor 
bijzondere doeleinden is opgenomen, te laten uitschijnen dat deze volledig voldoen aan alle 
vereisten van het stelsel inzake financiële verslaggeving dat door de geautoriseerde of erkende 
instantie die standaarden vaststelt (standards setting organization) dan wel op grond van wet- of 
regelgeving is vastgesteld. In bovenstaand voorbeeld van het contract is het aangewezen dat de 
beschrijving van het van toepassing zijnde stelsel inzake financiële verslaggeving verwijst naar 
de bepalingen inzake financiële verslaggeving van het contract, en niet naar de standaarden voor 
financiële verslaggeving van rechtsgebied X. 
A3.  In de omstandigheden zoals beschreven in paragraaf A2 hoeft het voor bijzondere doeleinden 
niet noodzakelijkerwijs een getrouw-beeld-stelsel te zijn, zelfs indien het stelsel inzake financiële 
verslaggeving waarop het gebaseerd is wel een getrouw-beeld-stelsel is. De reden daarvoor is 
dat het stelsel voor bijzondere doeleinden mogelijk niet voldoet aan alle vereisten van het stelsel 
inzake financiële verslaggeving dat de geautoriseerde of erkende instantie die standaarden 
vaststelt (standards setting organization) heeft uitgevaardigd, dan wel op grond van wet- of 
regelgeving, is vastgesteld om te komen tot een getrouw beeld van de financiële overzichten. 
A4.  Het is mogelijk dat financiële overzichten die zijn opgesteld volgens een stelsel voor bijzondere 
doeleinden, de enige financiële overzichten zijn die een entiteit opstelt. In dergelijke 
omstandigheden kunnen die financiële overzichten gebruikt worden door anderen dan degenen 
 
8        Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
voor wie het stelsel inzake financiële verslaggeving is opgezet. Ondanks de ruime verspreiding 
van de financiële overzichten in die omstandigheden worden de financiële overzichten in het 
kader van de ISA’s nog altijd beschouwd als financiële overzichten voor bijzondere doeleinden. 
De in paragraaf 13 en 14 gestelde vereisten zijn bedoeld om misverstanden te voorkomen over 
het doel waarvoor de financiële overzichten worden opgesteld. Toelichtingen bestaan uit 
verklarende of beschrijvende informatie, uiteengezet zoals vereist, die uitdrukkelijk toegelaten of 
anderszins toegestaan zijn door het van toepassing zijnde stelsel inzake financiële verslaggeving, 
in de individuele financiële overzichten zelf of in de toelichtingen of zijn daarin opgenomen door 
kruisverwijzingen.9 
Overwegingen bij het aanvaarden van de opdracht 
Aanvaardbaarheid van het stelsel inzake financiële verslaggeving (Zie Par. 8) 
 
A5.  Bij financiële overzichten voor bijzondere doeleinden zijn de financiële informatiebehoeften van 
de beoogde gebruikers de belangrijkste factoren bij het bepalen van de aanvaardbaarheid van 
het bij het opstellen van de financiële overzichten toegepaste stelsel inzake financiële 
verslaggeving. 
A6.  Het van toepassing zijnde stelsel inzake financiële verslaggeving kan de standaarden voor 
financiële verslaggeving bevatten die zijn vastgesteld door een organisatie die bevoegd is of 
erkend wordt om standaarden voor financiële overzichten voor bijzondere doeleinden uit te 
vaardigen. In dat geval worden die standaarden als aanvaardbaar beschouwd voor dat doel indien 
de organisatie een vastgesteld en transparant proces volgt waarin de zienswijzen van relevante 
belanghebbenden overwogen en beschouwd worden. In sommige rechtsgebieden kan wet- of 
regelgeving het stelsel inzake financiële verslaggeving voorschrijven dat door het management 
gebruikt dient te worden bij het opstellen van financiële overzichten voor bijzondere doeleinden 
voor een bepaalde soort entiteit. Een regelgever of toezichthouder kan bijvoorbeeld bepalingen 
inzake financiële verslaggeving vaststellen om te voldoen aan de vereisten van die regelgever of 
toezichthouder. Indien er geen aanleiding is om het tegendeel aan te nemen, wordt een dergelijk 
stelsel inzake financiële verslaggeving aanvaardbaar geacht voor financiële overzichten voor 
bijzondere doeleinden die door een dergelijke entiteit worden opgesteld. 
A7.  Wanneer de standaarden voor financiële verslaggeving waarnaar in paragraaf A6 wordt 
verwezen, worden aangevuld met vereisten op grond van wet- of regelgeving, vereist ISA 210 
van de auditor om te bepalen of er tegenstrijdigheden bestaan tussen de standaarden inzake 
financiële verslaggeving en de aanvullende vereisten en schrijft ISA 210 de acties voor die de 
auditor moet ondernemen indien dergelijke tegenstrijdigheden bestaan.10 
A8.  In het van toepassing zijnde stelsel inzake financiële verslaggeving kunnen de bepalingen inzake 
financiële verslaggeving opgenomen zijn van een contract, dan wel andere bronnen dan de in 
paragraaf A6 en A7 genoemde. In dat geval wordt de aanvaardbaarheid van het stelsel inzake 
financiële verslaggeving in de omstandigheden van de opdracht bepaald door na te gaan of het 
stelsel blijk geeft van kenmerken die gewoonlijk aanwezig zijn in aanvaardbare stelsels inzake 
financiële verslaggeving zoals omschreven in bijlage 2 van ISA 210. In geval van een stelsel voor 
bijzondere doeleinden is voor een bepaalde opdracht het relatieve belang van elk van de 
kenmerken zoals die gewoonlijk in aanvaardbare stelsels inzake financiële verslaggeving 
aanwezig zijn een zaak van professionele oordeelsvorming. De verkoper en de koper kunnen ten 
behoeve van het vaststellen van de intrinsieke waarde van een entiteit op de datum van de 
verkoop van die entiteit bijvoorbeeld overeen zijn gekomen dat zeer voorzichtige schattingen van 
voorzieningen voor oninbare vorderingen in hun geval passend zijn, ook al is dergelijke financiële 
informatie niet neutraal in vergelijking met informatie die is opgesteld in overeenstemming met 
een stelsel inzake financiële verslaggeving voor algemene doeleinden. 
Overwegingen bij het plannen en uitvoeren van de controle (Zie Par. 9) 
A9.  ISA 200 vereist van de auditor om te voldoen aan (a) relevante ethische voorschriften, waaronder 
de voorschriften met betrekking tot onafhankelijkheid, verband houdend met controleopdrachten 
van financiële overzichten, en (b) alle ISA’s die relevant zijn voor de controle. ISA 200 vereist 
eveneens van de auditor om zich te houden aan elk van de vereisten van een ISA, tenzij in het 
geval van de controle de gehele ISA niet relevant is of een vereiste niet relevant is omdat die 
 
9  
ISA 200, lid 13 f). 
10  
ISA 210, paragraaf 18.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
voorwaardelijk is en aan de voorwaarde niet wordt voldaan. In uitzonderlijke gevallen kan de 
auditor het noodzakelijk achten om af te wijken van een relevante vereiste in een ISA door 
alternatieve controlewerkzaamheden uit te voeren om het doel van de betreffende vereiste te 
bereiken.11 
A10. Het toepassen van sommige van de vereisten van de ISA’s bij de controle van financiële 
overzichten voor bijzondere doeleinden kan speciale overwegingen van de auditor vereisen. In 
ISA 320 zijn bijvoorbeeld oordeelsvormingen over aangelegenheden die van materieel belang zijn 
voor gebruikers van de financiële overzichten gebaseerd op de gemeenschappelijke financiële 
informatiebehoeften van de gebruikers als groep.12 In het geval van een controle van financiële 
overzichten voor bijzondere doeleinden zijn die oordeelsvormingen gebaseerd op een 
beoordeling van de financiële informatiebehoeften van de beoogde gebruikers. 
A11. Bij financiële overzichten voor bijzondere doeleinden, zoals overzichten die zijn opgesteld in 
overeenstemming met de vereisten van een contract, kan het management met de beoogde 
gebruikers een grenswaarde overeenkomen waar beneden tijdens de controle geïdentificeerde 
afwijkingen niet zullen worden gecorrigeerd of anderszins worden aangepast. Het bestaan van 
een dergelijke grenswaarde ontslaat de auditor echter niet van de verplichting om overeenkomstig 
ISA 320 de materialiteit te bepalen in overeenstemming met ISA 320 ten behoeve van het plannen 
en uitvoeren van de controle van de financiële overzichten voor bijzondere doeleinden. 
A12. ISA 260 (herzien) vereist van de auditor om te bepalen wie de geschikte personen zijn binnen de 
governance structuur van de entiteit om mee te communiceren.13 ISA 260 (herzien) merkt op dat 
in sommige gevallen alle met governance belaste personen betrokken zijn bij het leiden van de 
entiteit en de toepassing van de communicatievereisten aangepast is om deze positie te 
erkennen.14 Wanneer ook een volledige set van financiële overzichten voor algemene doeleinden 
wordt opgesteld door de entiteit, is het mogelijk dat de perso(o)n(en) verantwoordelijk voor het 
toezicht op het opstellen van de financiële overzichten voor bijzondere doeleinden niet dezelfde 
is (zijn) als de met governance belaste personen die verantwoordelijk zijn voor het toezicht op het 
opstellen van de financiële overzichten voor algemene doeleinden. 
Het vormen van een oordeel en overwegingen bij het rapporteren (Zie Par. 11) 
A13. De bijlage van deze ISA bevat voorbeelden van controleverklaringen van de onafhankelijke auditor 
betreffende financiële overzichten voor bijzondere doeleinden. Andere voorbeelden van 
controleverklaringen kunnen relevant zijn voor het rapporteren over financiële overzichten voor 
bijzondere doeleinden (zie bijvoorbeeld de bijlagen van ISA 700 (herzien), ISA 705 (herzien)15 
ISA 570 (herzien)16, ISA 720 (herzien)17 et ISA 706 (herzien)18).). 
Toepassing van ISA 700 (herzien) wanneer er wordt gerapporteerd over financiële overzichten voor 
bijzondere doeleinden 
A14. Paragraaf 11 van deze ISA legt uit dat van de auditor wordt vereist om ISA 700 (herzien) toe te 
passen bij het vormen van een oordeel en het rapporteren over financiële overzichten voor 
bijzondere doeleinden. Hierbij is van de auditor ook vereist om de rapporteringsvereisten in 
andere ISA’s toe te passen en kan hij de bijzondere overwegingen die worden behandeld in 
paragrafen A15, A16, A17, A18 en A19 hieronder nuttig achten. 
Continuïteit 
A15. Financiële overzichten voor bijzondere doeleinden kunnen al dan niet zijn opgesteld in 
overeenstemming 
met 
een 
stelsel 
inzake 
financiële 
verslaggeving 
waarvoor 
de 
continuïteitsveronderstelling relevant is (bijvoorbeeld in sommige rechtsgebieden is de 
continuïteitsveronderstelling niet van belang voor bepaalde financiële overzichten die zijn 
opgesteld op basis van een fiscale grondslag).19 Afhankelijk van de vraag of de 
 
11  
ISA 200, paragraaf 14, 18, 22 et 23. 
12  
ISA 320, Materialiteit bij de planning en uitvoering van een controle, paragraaf 2. 
13  
ISA 260 (herzien), Communicatie met de met governance belaste personen. 
14  
ISA 260 (herzien) 
15  
ISA 705 (herzien), Aanpassing van het oordeel in de controleverklaring van de onafhankelijke auditor.  
16  
ISA 570 (herzien), Continuiteit. 
17  
ISA 720 (herzien), De verantwoordelijkheden van de auditor met betrekking tot andere informatie. 
18  
ISA 706 (herzien), Paragrafen ter benadrukking van bepaalde aangelegenheden en paragrafen inzake overige 
aangelegenheden in de controleverklaring van de onafhankelijke auditor. 
19  
ISA 570 (herzien), paragraaf 2.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
continuïteitsveronderstelling relevant is voor het opstellen van de financiële overzichten voor 
bijzondere doeleinden, kan het noodzakelijk zijn om de vereiste beschrijving in de 
controleverklaring van de respectievelijke verantwoordelijkheden van het management20 en de 
auditor met betrekking tot continuïteit aan te passen. Het kan ook noodzakelijk zijn om de 
beschrijving in de controleverklaring van de verantwoordelijkheden van de auditor waar nodig aan 
te passen afhankelijk van hoe ISA 570 (herzien) van toepassing is in de omstandigheden van de 
opdracht.21 
Kernpunten van de controle 
A16. ISA 700 (herzien) vereist van de auditor om materialiteit, reikwijdte van de groepscontrole 
en kernpunten van de controle te communiceren in overeenstemming met 701 22 voor de 
controles van volledige sets van financiële overzichten voor algemene doeleinden 
beursgenoteerde ondernemingen. Voor controles van financiële overzichten voor bijzondere 
doeleinden is ISA 701 alleen van toepassing wanneer communicatie van de en kernpunten van 
de controle in de controleverklaring over de financiële overzichten voor bijzondere doeleinden 
vereist is op grond van wet- of regelgeving of de auditor anderszins besluit om de kernpunten van 
de controle te communiceren. Wanneer kernpunten van de controle worden gecommuniceerd in 
de controleverklaring over de financiële overzichten voor bijzondere doeleinden, is ISA 701 in zijn 
totaliteit van toepassing.23 
Andere informatie 
A17. ISA 720 (herzien) behandelt de verantwoordelijkheden van de auditor met betrekking tot andere 
informatie. In de context van deze ISA worden rapporten die de financiële overzichten voor 
bijzondere doeleinden bevatten of daarmee samengaan, waarvan het doel is om eigenaren (of 
soortgelijke 
belanghebbenden) 
informatie 
te 
verschaffen 
over 
aangelegenheden 
die 
gepresenteerd worden in de financiële overzichten voor bijzondere doeleinden, beschouwd als 
jaarverslagen voor de doelstelling van ISA 720 (herzien). In het geval van financiële overzichten 
die zijn opgesteld met gebruikmaking van een stelsel voor bijzondere doeleinden, omvat de term 
‘soortgelijke 
belanghebbenden’ 
de 
specifieke 
gebruikers 
waarvan 
in 
de 
financiële 
informatiebehoeften wordt voorzien door het stelsel voor bijzondere doeleinden dat wordt gebruikt 
om de financiële overzichten voor bijzondere doeleinden op te stellen. Wanneer de auditor 
vaststelt dat de entiteit van plan is om een dergelijk rapport uit te brengen, zijn de vereisten van 
ISA 720 (herzien) van toepassing op de controle van de financiële overzichten voor bijzondere 
doeleinden. 
Naam van de opdrachtpartner 
A18. Het vereiste in ISA 700 (herzien) voor de auditor om de naam van de opdrachtpartner op te nemen 
in de controleverklaring is ook van toepassing op controles van financiële overzichten voor 
bijzondere doeleinden beursgenoteerde ondernemingen.24 Van de auditor kan op grond van wet- 
of regelgeving vereist zijn om de naam van de opdrachtpartner op te nemen in de 
controleverklaring of hij kan anderszins besluiten om dit te doen als hij rapporteert over financiële 
overzichten voor bijzondere doeleinden voor andere 
entiteiten dan beursgenoteerde 
ondernemingen. 
Opnemen van een verwijzing naar de controleverklaring over de volledige set van financiële overzichten 
voor algemene doeleinden 
A19. De auditor kan het gepast achten om in een paragraaf inzake overige aangelegenheden in de 
controleverklaring over de financiële overzichten voor bijzondere doeleinden te verwijzen naar de 
controleverklaring over de volledige set van financiële overzichten voor algemene doeleinden of 
naar de aangelegenhe(i)d(en) die daarin is(zijn) gerapporteerd (zie ISA 706 (herzien)).25 De 
auditor kan het bijvoorbeeld gepast achten om in de controleverklaring over de financiële 
 
20  
ISA 700 (herzien), lid 34 b) et paragraaf A48. 
21  
ISA 700 (herzien), lid 39 b)iv). 
22  
ISA 701, Het communiceren van kernpunten van de controle in de controleverklaring van de onafhankelijk auditor.  
23  
ISA 700 (herzien), paragraaf 31.  
24  
ISA 700 (herzien), paragraaf 45 en A56 tot A58.  
25  
ISA 706 (herzien), paragraaf 10 et 11.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
overzichten voor bijzondere doeleinden te verwijzen naar een sectie Materiële onzekerheid 
omtrent de continuïteit die is opgenomen in de controleverklaring over de volledige set van 
financiële overzichten voor algemene doeleinden. 
De lezers er op attenderen dat de financiële overzichten zijn opgesteld in overeenstemming met een 
stelsel voor bijzondere doeleinden (Zie Par. 14) 
A20. De financiële overzichten voor bijzondere doeleinden kunnen gebruikt worden voor andere 
doeleinden dan die waarvoor zij waren bedoeld. Een regelgever of toezichthouder kan 
bijvoorbeeld van bepaalde entiteiten vereisen om de financiële overzichten voor bijzondere 
doeleinden openbaar te maken. Om misverstanden te voorkomen attendeert de auditor de 
gebruikers van de controleverklaring er op dat de financiële overzichten zijn opgesteld in 
overeenstemming met een stelsel voor bijzondere doeleinden en dat zij derhalve mogelijk niet 
geschikt zijn voor een ander doel door een paragraaf Benadrukking van bepaalde 
aangelegenheden op te nemen. ISA 706 (herzien) vereist dat deze paragraaf wordt opgenomen 
in een aparte sectie van de controleverklaring met een geschikte titel die de term ‘Benadrukking 
van een bepaalde aangelegenheid’ bevat.26 
Beperking van verspreiding of gebruik (Zie Par. 14) 
A21. Naast de waarschuwing zoals vereist op grond van paragraaf 14 kan de auditor het tevens passend 
achten om erop te wijzen dat de controleverklaring slechts is bedoeld voor de specifieke 
gebruikers. Afhankelijk van de wet- of regelgeving in het specifieke rechtsgebied kan dit worden 
bereikt door de beperking van verspreiding of gebruik van de controleverklaring. In deze 
omstandigheden kan de paragraaf waarnaar in paragraaf 14 wordt verwezen worden uitgebreid 
om daarin deze andere aangelegenheden op te nemen en kan de titel van de paragraaf 
dienovereenkomstig worden aangepast (zie de voorbeelden in de bijlage bij deze ISA). 
 
 
 
 
 
 
 
 
 
 
 
26  
ISA 706 (herzien),lid 9 a).

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
11/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Bijlage 
(Zie Par. A14) 
Bijlage: Voorbeelden van controleverklaringen van de onafhankelijke auditor 
betreffende financiële overzichten voor bijzondere doeleinden 
• 
Voorbeeld 1: Een controleverklaring betreffende een volledige set van financiële overzichten van 
een entiteit die geen beursgenoteerde entiteit is, opgesteld volgens de in een contract 
vastgestelde bepalingen inzake financiële verslaggeving (in dit voorbeeld is een compliance-
stelsel gebruikt). 
• 
Voorbeeld 2: Een controleverklaring betreffende een volledige set van financiële overzichten van 
een 
entiteit 
die 
geen 
beursgenoteerde 
entiteit 
is, 
opgesteld 
volgens 
fiscale 
verslaggevingsgrondslagen in rechtsgebied X (in dit voorbeeld is een compliance-stelsel 
gebruikt). 
• 
Voorbeeld 3: Een controleverklaring betreffende een volledige set van financiële overzichten van 
een beursgenoteerde entiteit opgesteld volgens de door een regelgever of toezichthouder 
vastgestelde bepalingen inzake financiële verslaggeving (in dit voorbeeld is een getrouw-beeld-
stelsel gebruikt).

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
12/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Voorbeeld 1: Een controleverklaring betreffende een volledige set van financiële overzichten 
van een entiteit die geen beursgenoteerde entiteit is, opgesteld volgens de in een contract 
vastgestelde bepalingen inzake financiële verslaggeving (in dit voorbeeld is een compliance-
stelsel gebruikt). 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
• 
De financiële overzichten zijn opgesteld door het management van de entiteit in 
overeenstemming met de in een contract vastgestelde bepalingen inzake financiële 
verslaggeving (d.w.z. een stelsel voor bijzondere doeleinden). Het management heeft 
geen keuze uit stelsels inzake financiële verslaggeving. 
• 
Het van toepassing zijnde stelsel inzake financiële verslaggeving is een compliance-
stelsel. 
• 
Er is geen controleverklaring betreffende de volledige set van financiële overzichten 
voor algemene doeleinden uitgebracht. 
• 
De voorwaarden van de controleopdracht zijn een weergave van de beschrijving in 
ISA 210 van de verantwoordelijkheid van het management voor de financiële 
overzichten. 
• 
De auditor is op basis van de verkregen controle-informatie tot de conclusie gekomen 
dat een goedkeurend (d.i. “niet-aangepast”) oordeel passend is. 
• 
De relevante ethische vereisten die van toepassing zijn op de controle zijn diegene 
die verband houden met de controle in het rechtsgebied. 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er 
geen van materieel belang zijnde onzekerheid bestaat die verband houdt met 
gebeurtenissen of omstandigheden die significante twijfel kunnen doen rijzen over 
de mogelijkheid van de entiteit om haar continuïteit te handhaven overeenkomstig 
ISA 570 (herzien). 
• 
Verspreiding en gebruik van de controleverklaring zijn aan beperkingen onderhevig. 
• 
De auditor is er niet toe gehouden om, of heeft anderszins niet beslist om, kernpunten 
van de controle te communiceren overeenkomstig ISA 701. 
• 
De auditor heeft vastgesteld dat er geen andere informatie is (d.w.z. dat de vereisten 
van ISA 720 (herzien) niet van toepassing zijn).  
• 
De met het toezicht over het financiële verslaggevingsproces belaste personen zijn 
verschillend van de met het opstellen van de financiële overzichten belaste personen. 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wet- 
of regelgeving.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
13/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
[Passende geadresseerde] 
Oordeel  
Wij hebben de financiële overzichten van vennootschap ABC (de “vennootschap”) gecontroleerd, die 
bestaan uit de balans per 31 december 20X1, de winst- en verliesrekening, het mutatieoverzicht van 
het eigen vermogen en het kasstroomoverzicht voor het op die datum afgesloten boekjaar, evenals uit 
de toelichtingen bij de financiële overzichten, met inbegrip van een overzicht van de belangrijke 
gehanteerde grondslagen voor financiële verslaggeving. 
Naar ons oordeel zijn de bijhorende financiële overzichten van de vennootschap voor het boekjaar 
afgesloten op 31 december 20X1 in alle van materieel belang zijnde opzichten opgesteld in 
overeenstemming met de bepalingen inzake financiële verslaggeving van Sectie Z van het contract d.d. 
1 januari 20X1 tussen de vennootschap en vennootschap DEF (“het contract”). 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie “Verantwoordelijkheden van de auditor voor de controle van de financiële 
overzichten” van onze verklaring. Wij zijn onafhankelijk van de vennootschap in overeenstemming met 
de ethische vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], 
en wij hebben onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze 
vereisten. Wij zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is 
als basis voor ons oordeel. 
Benadrukking van een aangelegenheid – Bepalingen inzake financiële verslaggeving en 
beperking van verspreiding en gebruik 
Wij vestigen de aandacht op Toelichting X bij de financiële overzichten, die de bepalingen inzake 
financiële verslaggeving beschrijft. De financiële overzichten zijn opgesteld om een hulpmiddel te 
vormen voor de vennootschap om te voldoen aan de in het hierboven genoemde contract, vastgestelde 
bepalingen inzake financiële verslaggeving. Als gevolg daarvan zijn de financiële overzichten mogelijk 
niet geschikt voor andere doeleinden. Onze verklaring is uitsluitend gericht aan de vennootschap en 
vennootschap DEF en dient niet te worden verspreid voor, of gebruikt door andere partijen dan de 
vennootschap of vennootschap DEF. Ons oordeel is niet aangepast met betrekking tot deze 
aangelegenheid. 
Verantwoordelijkheden van het management en de met governance belaste personen voor de 
financiële overzichten1 
Het management is verantwoordelijk voor het opstellen en weergeven van de financiële overzichten in 
overeenstemming met de in Sectie Z van het contract vastgestelde bepalingen inzake financiële 
verslaggeving en voor de interne beheersing die het management noodzakelijk acht om het opstellen 
mogelijk te maken van financiële overzichten die geen afwijking van materieel belang bevatten die het 
gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de vennootschap om haar continuïteit te handhaven, het toelichten, indien van 
toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
financiële verslaggevingsproces van de vennootschap. 
 
1  
In deze voorbeelden van controleverklaringen kunnen de termen “management” en “de met governance,belaste personen” 
worden vervangen door andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke 
rechtsgebied.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
14/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
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

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
15/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Paragraaf 41 (b) van ISA 700 (herzien) legt uit dat de in schaduw hieronder voorgestelde tekst kan worden opgenomen in een 
bijlage bij de controleverklaring. Paragraaf 41 (c) van ISA 700 (herzien) legt uit dat wanneer wet- en regelgeving of nationale 
controlestandaarden op expliciete wijze dit toelaten, een verwijzing  kan worden gemaakt naar een website van een bevoegde 
autoriteit die de beschrijving van de verantwoordelijkheden van de auditor bevat, veeleer dan deze tekst in de 
controleverklaring op te nemen, op voorwaarde dat de beschrijving op de website de beschrijving van de 
verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en hiermee niet inconsistent is. 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. 
Wij voeren tevens de volgende werkzaamheden uit: 
• 
het identificeren en inschatten van de risico’s dat de financiële overzichten een afwijking van  
materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en uitvoeren 
van controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van controle-
informatie die voldoende en geschikt is als basis voor ons oordeel. Het risico van het niet 
detecteren van een van materieel belang zijnde afwijking is groter indien die afwijking het 
gevolg is van fraude dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn 
van samenspanning, valsheid in geschrifte, opzettelijke weglatingen, het opzettelijk verkeerd 
voorstellen van zaken of het doorbreken van de interne beheersing; 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle, met als 
doel controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn 
maar die niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne 
beheersing van de vennootschap;2 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen; 
• 
het concluderen of de door het management gehanteerde continuïteitsveronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, of er 
een onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen ontstaan over de mogelijkheid van de 
vennootschap om haar continuïteit te handhaven. Indien wij concluderen dat er een 
onzekerheid van materieel belang bestaat, zijn wij ertoe gehouden om de aandacht in onze 
controleverklaring te vestigen op de daarop betrekking hebbende toelichtingen in de 
financiële overzichten, of, indien deze toelichtingen inadequaat zijn, om ons oordeel aan te 
passen. Onze conclusies zijn gebaseerd op de controle-informatie die verkregen is tot de 
datum van onze controleverklaring. Toekomstige gebeurtenissen of omstandigheden kunnen 
er echter toe leiden dat de vennootschap haar continuïteit niet langer kan handhaven. 
Wij communiceren met de met governance belaste personen, onder meer over de geplande reikwijdte 
en timing van de controle en over de significante controlebevindingen, waaronder eventuele 
significante tekortkomingen in de interne beheersing die wij identificeren gedurende onze controle. 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de auditor] 
[Datum] 
 
 
2  
Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om 
eenoordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
financiële overzichten.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
16/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Voorbeeld 2: Een controleverklaring betreffende een volledige set van financiële overzichten 
van een entiteit die geen beursgenoteerde entiteit is, opgesteld volgens fiscale 
verslaggevingsgrondslagen in rechtsgebied X (in dit voorbeeld is een compliance-stelsel 
gebruikt). 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
• 
Controle van een volledige set van financiële overzichten die zijn opgesteld door het 
management van een personenvennootschap in overeenstemming met fiscale 
verslaggevingsgrondslagen in rechtsgebied X (d.w.z. een stelsel voor bijzondere 
doeleinden) om een hulpmiddel te vormen voor de vennoten bij het opstellen van hun 
individuele belastingaangiften. Het management heeft geen keuze uit stelsels inzake 
financiële verslaggeving. 
• 
Het van toepassing zijnde stelsel inzake financiële verslaggeving is een compliance-stelsel. 
• 
De voorwaarden van de controleopdracht zijn een weergave van de beschrijving in ISA 210 
van de verantwoordelijkheid van het management voor de financiële overzichten. 
• 
De auditor is op basis van de verkregen controle-informatie tot de conclusie gekomen dat 
een goedkeurend (d.i. “niet-aangepast”) oordeel passend is. 
• 
De relevante ethische vereisten die van toepassing zijn op de controle zijn diegene van het 
rechtsgebied. 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er geen 
van materieel belang zijnde onzekerheid bestaat die verband houdt met gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen rijzen over de mogelijkheid van de 
entiteit om haar continuïteit te handhaven overeenkomstig ISA 570 (herzien). 
• 
Verspreiding van de controleverklaring is aan beperkingen onderhevig. 
• 
De auditor is er niet toe gehouden om, of heeft anderszins niet beslist om, kernpunten van 
de controle te communiceren overeenkomstig ISA 701. 
• 
De auditor heeft vastgesteld dat er geen andere informatie is (d.w.z. dat de vereisten van 
ISA 720 (herzien) niet van toepassing zijn). 
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend van 
de met het opstellen van de financiële overzichten belaste personen. 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wet- of 
regelgeving.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
17/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
[Passende geadresseerde] 
Oordeel 
Wij hebben de financiële overzichten van personenvennootschap ABC (de “vennootschap”) 
gecontroleerd, die bestaan uit de balans per 31 december 20X1 en de winst- en verliesrekening voor 
het op die datum afgesloten boekjaar, evenals uit de toelichtingen bij de financiële overzichten, met 
inbegrip van een overzicht van de belangrijke gehanteerde grondslagen voor financiële verslaggeving. 
Naar ons oordeel zijn de bijhorende financiële overzichten van de vennootschap voor het boekjaar 
afgesloten op 31 december 20X1 in alle van materieel belang zijnde opzichten opgesteld in 
overeenstemming met [beschrijf de van toepassing zijnde wetgeving inzake belasting op de winst] in 
rechtsgebied X. 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie “Verantwoordelijkheden van de auditor voor de controle van de financiële 
overzichten” van onze verklaring. Wij zijn onafhankelijk van de vennootschap in overeenstemming met 
de ethische vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], 
en wij hebben onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze 
vereisten. Wij zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is 
als basis voor ons oordeel. 
Benadrukking van een aangelegenheid – Bepalingen inzake financiële verslaggeving en 
beperking van verspreiding 
Wij vestigen de aandacht op Toelichting X bij de financiële overzichten, die de bepalingen inzake 
financiële verslaggeving beschrijft. De financiële overzichten zijn opgesteld om een hulpmiddel te 
vormen voor de vennoten van de vennootschap bij het opstellen van hun individuele 
belastingaangiften. Als gevolg daarvan zijn de financiële overzichten mogelijk niet geschikt voor andere 
doeleinden. Ons verslag is uitsluitend bestemd voor de vennootschap en haar vennoten en mag niet 
worden verspreid onder andere partijen dan de vennootschap of haar vennoten. Ons oordeel is niet 
aangepast met betrekking tot deze aangelegenheid. 
Verantwoordelijkheden van het management en de met governance belaste personen voor de 
financiële overzichten3 
Het management is verantwoordelijk voor het opstellen van de financiële overzichten in 
overeenstemming met de fiscale verslaggevingsgrondslagen in rechtsgebied X en voor de interne 
beheersing die het management noodzakelijk acht om het opstellen mogelijk te maken van financiële 
overzichten die geen afwijking van materieel belang bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de vennootschap om haar continuïteit te handhaven, het toelichten, indien 
van toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het toezicht op het financiële 
verslaggevingsproces van de vennootschap. 
 
3  
Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
18/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijking van materieel belang bevatten die het gevolg is van 
fraude of van fouten, en het uitbrengen van een controleverklaring waarin ons oordeel is opgenomen. 
Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie dat een 
controle die overeenkomstig de internationale controlestandaarden (ISA’s) is uitgevoerd altijd een 
afwijking van materieel belang ontdekt wanneer die bestaat. Afwijkingen kunnen zich voordoen als 
gevolg van fraude of fouten en worden als van materieel belang beschouwd indien redelijkerwijs kan 
worden verwacht dat zij, individueel of gezamenlijk, de economische beslissingen genomen door 
gebruikers op basis van deze financiële overzichten, beïnvloeden.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
19/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Paragraaf 41 (b) van ISA 700 (herzien) legt uit dat de in schaduw hieronder voorgestelde tekst kan worden opgenomen in een 
bijlage bij de controleverklaring. Paragraaf 41 (c) van ISA 700 (herzien) legt uit dat wanneer wet- en regelgeving of nationale 
controlestandaarden op expliciete wijze dit toelaten, een verwijzing kan worden gemaakt naar een website van een bevoegde 
autoriteit die de beschrijving van de verantwoordelijkheden van de auditor bevat, veeleer dan deze tekst in de 
controleverklaring op te nemen, op voorwaarde dat de beschrijving op de website de beschrijving van de 
verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en hiermee niet inconsistent is. 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. 
Wij voeren tevens de volgende werkzaamheden uit: 
• 
het identificeren en inschatten van de risico’s dat de financiële overzichten een afwijking van 
materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en uitvoeren van 
controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van controle-informatie 
die voldoende en geschikt is als basis voor ons oordeel. Het risico van het niet detecteren van 
een van materieel belang zijnde afwijking is groter indien die afwijking het gevolg is van fraude 
dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn van samenspanning, 
valsheid in geschrifte, het opzettelijke weglatingen, het opzettelijk verkeerd voorstellen van 
zaken of het doorbreken van de interne beheersing; 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle, met als doel 
controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn maar 
die niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne beheersing 
van de vennootschap;4 
• 
het concluderen of de door het management gehanteerde continuïteitsveronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, of er een 
onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen ontstaan over de mogelijkheid van de 
vennootschap om haar continuïteit te handhaven. Indien wij concluderen dat er een 
onzekerheid van materieel belang bestaat, zijn wij ertoe gehouden om de aandacht in onze 
controleverklaring te vestigen op de daarop betrekking hebbende toelichtingen in de financiële 
overzichten, of, indien deze toelichtingen inadequaat zijn, om ons oordeel aan te passen. Onze 
conclusies zijn gebaseerd op de controle-informatie die verkregen is tot de datum van onze 
controleverklaring. Toekomstige gebeurtenissen of omstandigheden kunnen er echter toe 
leiden dat de vennootschap haar continuïteit niet langer kan handhaven; 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen. 
Wij communiceren met de met governance belaste personen, onder meer over de geplande reikwijdte 
en timing van de controle en over de significante controlebevindingen, waaronder eventuele 
significante tekortkomingen in de interne beheersing die wij identificeren gedurende onze controle. 
 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de auditor] 
[Datum] 
 
 
 
4  
Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
financiële overzichten.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
20/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Voorbeeld 3: Een controleverklaring betreffende een volledige set van financiële overzichten 
van een beursgenoteerde entiteit opgesteld volgens de door een regelgever of toezichthouder 
vastgestelde bepalingen inzake financiële verslaggeving (in dit voorbeeld is een getrouw-
beeld-stelsel gebruikt). 
Voor de doelstellingen van dit voorbeeld van controleverklaring worden de volgende 
omstandigheden als veronderstelling aangenomen: 
• 
Controle van een volledige set van financiële overzichten van een beursgenoteerde 
entiteit die zijn opgesteld door het management van de entiteit in overeenstemming 
met de door een regelgever of toezichthouder vastgestelde bepalingen inzake 
financiële verslaggeving (d.w.z. een stelsel voor bijzondere doeleinden) om te voldoen 
aan de vereisten van die regelgever of toezichthouder. Het management heeft geen 
keuze uit stelsels inzake financiële verslaggeving. 
• 
Het van toepassing zijnde stelsel inzake financiële verslaggeving is een getrouw-
beeld-stelsel. 
• 
De voorwaarden van de controleopdracht zijn een weergave van de beschrijving in ISA 
210 van de verantwoordelijkheid van het management voor de financiële overzichten. 
• 
De auditor is op basis van de verkregen controle-informatie tot de conclusie gekomen 
dat een goedkeurend (d.i. “niet-aangepast”) oordeel passend is. 
• 
De relevante ethische vereisten die van toepassing zijn op de controle zijn diegene die 
verband houden met de controle in het rechtsgebied. 
• 
Op basis van de verkregen controle-informatie heeft de auditor geconcludeerd dat er 
een van materieel belang zijnde onzekerheid bestaat die verband houdt met 
gebeurtenissen of omstandigheden die significante twijfel kunnen doen rijzen over de 
mogelijkheid van de entiteit om haar continuïteit te handhaven overeenkomstig ISA 
570 (herzien). De toelichting in de financiële overzichten van de van materieel belang 
zijnde onzekerheid is passend. 
• 
Verspreiding of gebruik van de controleverklaring zijn niet aan beperkingen 
onderhevig. 
• 
Van de auditor wordt door de regelgever of toezichthouder vereist dat hij kernpunten 
van de controle communiceert overeenkomstig ISA 701. 
• 
De Paragraaf inzake overige aangelegenheden refereert aan het feit dat de auditor 
tevens een controleverklaring heeft uitgebracht betreffende de financiële overzichten 
opgesteld door vennootschap ABC over dezelfde periode in overeenstemming met een 
stelsel voor algemene doeleinden. 
• 
De auditor heeft vastgesteld dat er geen andere informatie is (d.w.z. dat de vereisten 
van ISA 720 (herzien) niet van toepassing zijn).   
• 
De met het toezicht over de financiële overzichten belaste personen zijn verschillend 
van de met het opstellen van de financiële overzichten belaste personen. 
• 
De auditor heeft geen overige rapporteringsverplichtingen op grond van lokale wet- of 
regelgeving.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
21/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
CONTROLEVERKLARING VAN DE ONAFHANKELIJKE AUDITOR 
Aan de aandeelhouders van vennootschap ABC [of passende geadresseerde] 
Oordeel 
Wij hebben de financiële overzichten van vennootschap ABC (de “vennootschap”) gecontroleerd, die 
bestaan uit de balans per 31 december 20X1, de winst- en verliesrekening, het mutatieoverzicht van 
het eigen vermogen en het kasstroomoverzicht voor het op die datum afgesloten boekjaar, evenals uit 
de toelichtingen bij de financiële overzichten, met inbegrip van een overzicht van de belangrijke 
gehanteerde grondslagen voor financiële verslaggeving. 
Naar ons oordeel vormen de bijhorende financiële overzichten in alle van materieel belang zijnde 
opzichten een getrouwe weergave (dan wel geven zij een getrouw beeld) van de financiële positie van 
de vennootschap per 31 december 20X1, en van haar financiële prestaties en kasstromen voor het op 
die datum afgesloten boekjaar, in overeenstemming met de door Sectie Y van Reglement Z 
vastgestelde bepalingen inzake financiële verslaggeving. 
Basis voor ons oordeel 
Wij hebben onze controle uitgevoerd volgens de internationale controlestandaarden (International 
Standards on Auditing, ISA’s). Onze verantwoordelijkheden op grond van deze standaarden zijn verder 
beschreven in de sectie “Verantwoordelijkheden van de auditor voor de controle van de financiële 
overzichten” van onze verklaring. Wij zijn onafhankelijk van de vennootschap in overeenstemming met 
de ethische vereisten die relevant zijn voor de controle van de financiële overzichten in [rechtsgebied], 
en wij hebben onze overige ethische verantwoordelijkheden nageleefd in overeenstemming met deze 
vereisten. Wij zijn van mening dat de door ons verkregen controle-informatie voldoende en geschikt is 
als basis voor ons oordeel. 
Benadrukking van een aangelegenheid – Bepalingen inzake financiële verslaggeving 
Wij vestigen de aandacht op Toelichting X bij de financiële overzichten, die de bepalingen inzake 
financiële verslaggeving beschrijft. De financiële overzichten zijn opgesteld om een hulpmiddel te 
vormen voor de vennootschap bij het nakomen van de door regelgever of toezichthouder DEF gestelde 
eisen. Als gevolg daarvan zijn de financiële overzichten mogelijk niet geschikt voor andere doeleinden. 
Ons oordeel is niet aangepast met betrekking tot deze aangelegenheid. 
Van materieel belang zijnde onzekerheid met betrekking tot continuïteit 
Wij vestigen de aandacht op de in de financiële overzichten opgenomen Toelichting 6 die aangeeft dat 
de vennootschap een nettoverlies heeft geleden ten belope van ZZZ gedurende het boekjaar 
afgesloten op 31 december 20X1, en dat op die datum de kortlopende schulden de totale activa van 
de vennootschap overschreden met YYY. Zoals vermeld in Toelichting 6, vormen deze gebeurtenissen 
of omstandigheden, tezamen met overige aangelegenheden die in Toelichting 6 zijn uiteengezet, een 
aanwijzing dat een van materieel belang zijnde onzekerheid bestaat die significante twijfel kan doen 
rijzen over de mogelijkheid van de vennootschap om haar continuïteit te handhaven. Ons oordeel is 
niet aangepast met betrekking tot deze aangelegenheid. 
Kernpunten van onze controle 
Kernpunten van onze controle betreffen die aangelegenheden die naar ons professioneel oordeel het 
meest significant waren bij de controle van de financiële overzichten van de huidige verslagperiode. 
Deze aangelegenheden zijn behandeld in de context van onze controle van de financiële overzichten 
als geheel en bij het vormen van ons oordeel hierover, en wij verschaffen geen afzonderlijk oordeel 
over deze aangelegenheden. In aanvulling tot de aangelegenheid beschreven in de bovenstaande 
sectie “Van materieel belang zijnde onzekerheid met betrekking tot continuïteit”, hebben wij de hierna 
beschreven aangelegenheden als de in onze verklaring te communiceren kernpunten van onze 
controle vastgesteld.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
22/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
[Beschrijving van elk kernpunt van de controle in overeenstemming met ISA 701 zoals toegepast op 
deze controle.] 
Overige aangelegenheid 
De vennootschap heeft een separate set van financiële overzichten opgesteld voor het boekjaar 
afgesloten op 31 december 20X1, in overeenstemming met de internationale standaarden voor 
financiële verslaggeving (International Financial Reporting Standards, IFRS), waarover wij een 
separate controleverklaring hebben uitgebracht aan de aandeelhouders van de vennootschap d.d. 31 
maart 20X2. 
Verantwoordelijkheden van het management en de met governance belaste personen voor de 
financiële overzichten5 
Het management is verantwoordelijk voor het opstellen en getrouw weergeven van de financiële 
overzichten in overeenstemming met de door Sectie Y van Reglement Z6 vastgestelde bepalingen 
inzake financiële verslaggeving en voor de interne beheersing die het management noodzakelijk acht 
om het opstellen mogelijk te maken van financiële overzichten die geen afwijking van materieel belang 
bevatten die het gevolg is van fraude of van fouten. 
Bij het opstellen van de financiële overzichten is het management verantwoordelijk voor het inschatten 
van de mogelijkheid van de vennootschap om haar continuïteit te handhaven, het toelichten, indien 
van toepassing, van aangelegenheden die met continuïteit verband houden en het gebruiken van de 
continuïteitsveronderstelling, tenzij het management het voornemen heeft om de vennootschap te 
liquideren of om de bedrijfsactiviteiten te beëindigen of geen realistisch alternatief heeft dan dit te doen. 
De met governance belaste personen zijn verantwoordelijk voor het uitoefenen van toezicht op het 
financiële verslaggevingsproces van de vennootschap. 
Verantwoordelijkheden van de auditor voor de controle van de financiële overzichten 
Onze doelstellingen zijn het verkrijgen van een redelijke mate van zekerheid over de vraag of de 
financiële overzichten als geheel geen afwijking van materieel belang bevatten die het gevolg is van 
fraude of van fouten, en het uitbrengen van een controleverklaring waarin ons oordeel is opgenomen. 
Een redelijke mate van zekerheid is een hoog niveau van zekerheid, maar is geen garantie dat een 
controle die overeenkomstig de internationale controlestandaarden (ISA’s) is uitgevoerd altijd een 
afwijking van materieel belang ontdekt wanneer die bestaat. Afwijkingen kunnen zich voordoen als 
gevolg van fraude of fouten en worden als van materieel belang beschouwd indien redelijkerwijs kan 
worden verwacht dat zij, individueel of gezamenlijk, de economische beslissingen genomen door 
gebruikers op basis van deze financiële overzichten, beïnvloeden. 
 
5  
Of andere bewoordingen die passend zijn in de context van het wettelijke kader van het specifieke rechtsgebied. 
6  
In het geval het de verantwoordelijkheid is van het management om financiële overzichten op te stellen die een getrouw 
beeld geven, kan deze zin als volgt luiden: “Het management is verantwoordelijk voor het opstellen van financiële overzichten 
die een getrouw beeld geven in overeenstemming met de door Sectie Y van Reglement Z vastgestelde bepalingen inzake 
financiële verslaggeving en voor de interne beheersing …”.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
23/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
Paragraaf 41 (b) van ISA 700 (herzien) legt uit dat de in schaduw hieronder voorgestelde tekst kan worden opgenomen in 
een bijlage bij de controleverklaring. Paragraaf 41 (c) van ISA 700 (herzien) legt uit dat wanneer wet- en regelgeving of 
nationale controlestandaarden op expliciete wijze dit toelaten, een verwijzing kan worden gemaakt naar een website van een 
bevoegde autoriteit die de beschrijving van de verantwoordelijkheden van de auditor bevat, veeleer dan deze tekst in de 
controleverklaring op te nemen, op voorwaarde dat de beschrijving op de website de beschrijving van de 
verantwoordelijkheden van de auditor zoals hierna weergegeven behandelt, en hiermee niet inconsistent is. 
Als deel van een controle uitgevoerd overeenkomstig de ISA’s, passen wij professionele 
oordeelsvorming toe en handhaven wij een professioneel-kritische instelling gedurende de controle. 
Wij voeren tevens de volgende werkzaamheden uit: 
• 
het identificeren en inschatten van de risico’s dat de financiële overzichten een afwijking van 
materieel belang bevatten die het gevolg is van fraude of fouten, het bepalen en uitvoeren 
van controlewerkzaamheden die op deze risico’s inspelen en het verkrijgen van controle-
informatie die voldoende en geschikt is als basis voor ons oordeel. Het risico van het niet 
detecteren van een van materieel belang zijnde afwijking is groter indien die afwijking het 
gevolg is van fraude dan indien zij het gevolg is van fouten, omdat bij fraude sprake kan zijn 
van samenspanning, valsheid in geschrifte, het opzettelijk nalaten transacties vast te leggen, 
het opzettelijk verkeerd voorstellen van zaken of het doorbreken van de interne beheersing; 
• 
het verkrijgen van inzicht in de interne beheersing die relevant is voor de controle, met als 
doel controlewerkzaamheden op te zetten die in de gegeven omstandigheden geschikt zijn 
maar die niet zijn gericht op het geven van een oordeel over de effectiviteit van de interne 
beheersing van de vennootschap;7 
• 
het evalueren van de geschiktheid van de gehanteerde grondslagen voor financiële 
verslaggeving en het evalueren van de redelijkheid van de door het management gemaakte 
schattingen en van de daarop betrekking hebbende toelichtingen; 
• 
het concluderen of de door het management gehanteerde continuïteitsveronderstelling 
aanvaardbaar is, en het concluderen, op basis van de verkregen controle-informatie, of er 
een onzekerheid van materieel belang bestaat met betrekking tot gebeurtenissen of 
omstandigheden die significante twijfel kunnen doen ontstaan over de mogelijkheid van de 
vennootschap om haar continuïteit te handhaven. Indien wij concluderen dat er een 
onzekerheid van materieel belang bestaat, zijn wij ertoe gehouden om de aandacht in onze 
controleverklaring te vestigen op de daarop betrekking hebbende toelichtingen in de 
financiële overzichten, of, indien deze toelichtingen inadequaat zijn, om ons oordeel aan te 
passen. Onze conclusies zijn gebaseerd op de controle-informatie die verkregen is tot de 
datum van onze controleverklaring. Toekomstige gebeurtenissen of omstandigheden kunnen 
er echter toe leiden dat de vennootschap haar continuïteit niet langer kan handhaven; 
• 
het evalueren van de algehele presentatie, structuur en inhoud van de financiële overzichten, 
met inbegrip van de daarin opgenomen toelichtingen, en van de vraag of de financiële 
overzichten de onderliggende transacties en gebeurtenissen weergeven op een wijze die 
leidt tot een getrouw beeld. 
Wij communiceren met de met governance belaste personen, onder meer over de geplande 
reikwijdte en timing van de controle en over de significante controlebevindingen, waaronder 
eventuele significante tekortkomingen in de interne beheersing die wij identificeren gedurende onze 
controle. 
Wij verschaffen aan de met governance belaste personen tevens een verklaring dat wij de relevante 
ethische voorschriften over onafhankelijkheid hebben nageleefd, en wij communiceren met deze 
personen over alle relaties en andere zaken die redelijkerwijs onze onafhankelijkheid kunnen 
beïnvloeden en, waar van toepassing, over de daarmee verband houdende maatregelen om onze 
onafhankelijkheid te waarborgen. 
Uit de aangelegenheden die met de met governance belaste personen zijn gecommuniceerd 
bepalen wij die zaken die het meest significant waren bij de controle van de financiële overzichten 
van de huidige verslagperiode, en die derhalve de kernpunten van onze controle uitmaken. Wij 
beschrijven deze aangelegenheden in onze controleverklaring, tenzij het openbaar maken van deze 
aangelegenheden is verboden door wet- of regelgeving of, in buitengewoon zeldzame 
omstandigheden, tenzij wij bepalen dat een aangelegenheid niet in onze verklaring moet worden 
opgenomen omwille van het feit dat de negatieve gevolgen van dergelijke communicatie 
redelijkerwijs worden verwacht groter te zijn dan de voordelen voor het maatschappelijk verkeer.

BIJZONDERE OVERWEGINGEN – CONTROLES VAN FINANCIËLE OVERZICHTEN DIE ZIJN OPGESTELD IN 
OVEREENSTEMMING MET STELSELS VOOR BIJZONDERE DOELEINDEN 
 
 
 
ISA 800 (herzien) – Bijlage 
 
 NBA – IBR 2025 
24/24 
Originele bron: Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services 
Pronouncements, 2022 Edition Volume I 
 
Versie 2025 
 
De voor de controleopdracht verantwoordelijke vennoot, zoals tot uiting komt in deze verklaring van de 
onafhankelijke auditor, is [naam]. 
[Handtekening van het auditkantoor, de auditor, of beide, zoals van toepassing in het desbetreffende 
rechtsgebied] 
[Adres van de auditor] 
[Datum] 
 
 
 
 
7  
Deze zin wordt aangepast, waar nodig, in de omstandigheden dat de auditor tevens een verantwoordelijkheid heeft om een 
oordeel tot uitdrukking te brengen over de effectiviteit van de interne beheersing die relevant is voor de controle van de 
financiële overzichten.