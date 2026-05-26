---
tags: ["2.8"]
itaa-lex-sectie: ""
wet: "Synthesetekst van het Belgisch-Fins dubbelbelastingverdrag zoals gewijzigd door het MLI — illustratie van MLI-toepassing op een bestaand DBV"
bron_rol: "interpretatief"
status: "beschikbaar"
bijgewerkt: "2017"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/DBV-Finland-Synthesetekst-MLI.md
      sha256: 1832498b9fe46525b34528a6ee285aee02b2c67033e15bee2fa5c8282fdf2e12
      version: '2017'
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T18:46:04Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T18:51:56Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Synthesetekst van 812 regels met 9 headings — de platte structuur (9 headings voor een document van 103K chars) is inherent aan het synthesetekst-format en niet een extractie-tekortkoming. De Layer 1 WARN (langste sectie 61K chars) is verwacht; de chunker doet paragraph-split. Verdragsartikelen 1 t/m 32 plus Protocol volledig aanwezig, MLI-vakken correct als inline-tekstblokken gemarkeerd.
    caveat:
    layer1:
      status: warn
      run_id: 20260519-184604
      run_at: '2026-05-19T18:46:04Z'
      heading_count: 7
      max_section_chars: 61043
      file_size_chars: 102954
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ####-niveau: 61043 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T18:51:56Z'
      rationale: Synthesetekst van 812 regels met 9 headings — de platte structuur (9 headings voor een document van 103K chars) is inherent aan het synthesetekst-format en niet een extractie-tekortkoming. De Layer 1 WARN (langste sectie 61K chars) is verwacht; de chunker doet paragraph-split. Verdragsartikelen 1 t/m 32 plus Protocol volledig aanwezig, MLI-vakken correct als inline-tekstblokken gemarkeerd.
      concrete_problemen:
        - "Lijn 52: '# \uFEFF\\n' (lege heading met BOM-karakter U+FEFF) — zelfde patroon als Wet Pijler 2; fisconet+-export-artefact. De '\uFEFF'-tekens (BOM/ZWNBSP) verschijnen ook op lijn 56 als standalone alinea — extractie-residu."
        - "Regels 82-92: URL-verwijzingen ('De link naar de versie in de Finse taal') zonder de eigenlijke URL — de hyperlink-tekst is correct geëxtraheerd maar de target-URL ontbreekt. Dit is een beperking van de MCP-browser-extractie voor hyperlinks, niet een structuurprobleem. Voor RAG-doeleinden neutraal."
        - 'Lijn 121: volledige verdragstitel herhaald als plain-tekst-alinea midden in het document (na de disclaimer-sectie) — dit is correct: de synthesetekst begint formeel na de disclaimer, en de herhaalde titel markeert dat begin. Geen probleem.'
        - "Lijn 248: 'andere onderneming' in plaats van 'andere onderneming' (extra spatie ontbreekt in 'bewerking of verwerking door een ander onderneming') — source-typo in verdragstekst."
---

# Synthesetekst van het Belgisch-Fins dubbelbelastingverdrag zoals gewijzigd door het MLI — illustratie van MLI-toepassing op een bestaand DBV

*Bijgewerkt tot en met 2017 — gecoördineerde versie.*

# ﻿

> Officiële bron: FOD Financiën via fisconet+.

﻿
SYNTHESETEKST VAN HET MLI EN DE OVEREENKOMST TUSSEN HET KONINKRIJK BELGIË EN DE REPUBLIEK FINLAND TOT HET VERMIJDEN VAN DUBBELE BELASTING EN TOT HET VOORKOMEN VAN HET ONTGAAN VAN BELASTING INZAKE BELASTINGEN NAAR HET INKOMEN EN NAAR HET VERMOGEN, ONDERTEKEND TE BRUSSEL OP 18 MEI 1976, ZOALS GEWIJZIGD DOOR HET AANVULLEND AKKOORD ONDERTEKEND TE BRUSSEL OP 13 MAART 1991 EN DOOR HET PROTOCOL ONDERTEKEND TE BRUSSEL OP 15 SEPTEMBER 2009

Dit document werd opgemaakt in overleg met de bevoegde autoriteit van Finland en is een weergave van de gedeelde visie op de wijzigingen die door het MLI werden aangebracht aan de Overeenkomst*.

* De Engelse tekst van dit. document werd afgestemd met de bevoegde autoriteiten van Finland. Voor de Nederlandse vertaling ervan is er geen afstemming geweest.

Algemene disclaimer inzake het document synthesetekst

Dit document geeft de synthesetekst weer voor de toepassing van de op 18 mei 1976 ondertekende Overeenkomst tussen het Koninkrijk België en de Republiek Finland tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting inzake belastingen naar het inkomen en naar het vermogen, het op 13 maart 1991 ondertekende aanvullend akkoord en het op 15 september 2009 ondertekende Protocol (samen de "Overeenkomst"), zoals gewijzigd door de multilaterale Overeenkomst ter implementatie van aan belastingverdragen gerelateerde maatregelen ter voorkoming van grondslaguitholling en winstverschuiving, ondertekend door België en Finland op 7 juni 2017 (het "MLI").

Het document werd opgemaakt op basis van het MLI-standpunt van België dat aan de depositaris werd overgemaakt bij de bekrachtiging op 26 juni 2019 en van het MLI-standpunt van Finland dat aan de depositaris werd overgemaakt bij de aanvaarding op 25 februari 2019. Deze MLI-standpunten kunnen gewijzigd worden zoals bepaald in het MLI. Wijzigingen die aan MLI-standpunten worden aangebracht, zouden het effect van het MLI op deze Overeenkomst kunnen wijzigen. De Republiek Finland heeft haar MLI-standpunt gewijzigd door haar voorbehoud bij artikel 9 in te trekken en door aanvullende kennisgevingen te doen (geconsolideerd MLI-standpunt van de Republiek Finland op 27 juni 2023). Deze wijzigingen hebben het effect van het MLI op de Overeenkomst niet veranderd.

De authentieke wettelijke teksten van de Overeenkomst en van het MLI hebben voorrang en blijven de toepasselijke wettelijke teksten.

De bepalingen van het MLI die van toepassing zijn met betrekking tot de bepalingen van de Overeenkomst, zijn opgenomen in vakken doorheen de tekst van dit document in de context van de desbetreffende bepalingen van de Overeenkomst. De vakken die de bepalingen van het MLI bevatten, zijn over het algemeen ingevoegd overeenkomstig de volgorde van de bepalingen van het OESO-modelverdrag inzake belasting.

De tekst van de bepalingen van het MLI werd gewijzigd om de in het MLI gebruikte terminologie in overeenstemming te brengen met de in de Overeenkomst gebruikte terminologie (zoals "gedekt belastingverdrag" en "Overeenkomst", "verdragsluitende rechtsgebieden" en "overeenkomstsluitende Staten"), teneinde de bepalingen van het MLI gemakkelijker te begrijpen. De wijzigingen van de terminologie zijn bedoeld om de leesbaarheid van het document te vergroten, niet om de inhoud van de bepalingen van het MLI te wijzigen. Zo werden ook onderdelen van bepalingen van het MLI gewijzigd die bestaande bepalingen van de Overeenkomst beschrijven; beschrijvende taal werd vervangen door verwijzingen naar de bestaande bepalingen (van de Overeenkomst) teneinde de leesbaarheid te vergemakkelijken.

In alle gevallen moeten verwijzingen naar de bepalingen van de Overeenkomst of naar de Overeenkomst verstaan worden als zijnde verwijzingen naar de Overeenkomst zoals gewijzigd door de bepalingen van het MLI, op voorwaarde dat die bepalingen van het MLI van toepassing zijn geworden.

Verwijzingen

De authentieke wettelijke tekst van het MLI en van de Overeenkomst is terug te vinden op de onderstaande links:

Het MLI:

In België:

In Finland:

De op 18 mei 1976 ondertekende Overeenkomst tussen het Koninkrijk België en de Republiek Finland tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting inzake belastingen naar het inkomen en naar het vermogen, is gepubliceerd in de "Treaty Series" van het "Statue Book" van Finland SopS 66/1978. De link naar de versie in de Finse taal

Het op 13 maart 1991 ondertekende aanvullend akkoord tot wijziging van de Overeenkomst tussen het Koninkrijk België en de Republiek Finland tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting inzake belastingen naar het inkomen en naar het vermogen, is gepubliceerd in de "Treaty Series" van het "Statue Book" van Finland SopS 54/1997. De link naar de versie in de Finse taal

Het op 15 september 2009 ondertekende Protocol tot wijziging van de op 18 mei 1976 ondertekende Overeenkomst tussen het Koninkrijk België en de Republiek Finland tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting inzake belastingen naar het inkomen en naar het vermogen, zoals gewijzigd door het op 13 maart 1991 ondertekende aanvullend akkoord, is gepubliceerd in de "Treaty Series" van het "Statue Book" van Finland SopS 13/2014. De link naar de versie in de Finse taal

Het MLI-standpunt van België dat aan de depositaris werd overgemaakt bij de bekrachtiging op 26 juni 2019, het MLI-standpunt van Finland dat aan de depositaris werd overgemaakt bij de aaanvaarding op 25 februari 2019 en het geconsolideerde MLI-standpunt van de Republiek Finland ingediend bij de depositaris op 27 juni 2023, vindt u op de webpagina MLI Depositaris (OESO).

Disclaimer betreffende de toepassing van de bepalingen van het MLI

Toepassing van de MLI-bepalingen:

De op deze Overeenkomst toepasselijke bepalingen van het MLI, worden niet van toepassing op dezelfde data als de oorspronkelijke bepalingen van de Overeenkomst. Elke bepaling van het MLI zou op een verschillende datum van toepassing kunnen worden, naargelang van de soort belasting waarover het gaat (aan de bron ingehouden belastingen of andere geheven belastingen) en van de keuzes die door België en Finland werden gemaakt in hun MLI-standpunten.

Data van de neerlegging van de akte van bekrachtiging, aanvaarding of goedkeuring: 26 juni 2019 voor België en 25 februari 2019 voor Finland.

Inwerkingtreding van het MLI: 1 oktober 2019 voor België en 1 juni 2019 voor Finland.

Toepassing:

a) Ingevolge paragraaf 1 van artikel 35 van het MLI zijn de bepalingen van het MLI, niet zijnde de bepalingen van artikel 36, van toepassing met betrekking tot de Overeenkomst:

- met betrekking tot belastingen geheven aan de bron, op bedragen die zijn betaald of toegekend aan niet-inwoners, wanneer het feit dat aanleiding geeft tot die belastingen zich voordoet op of na 1 januari 2020;

-met betrekking tot alle andere door België geheven belastingen, op belastingen die worden geheven ter zake van belastbare tijdperken die aanvangen op of na 01/04/2020; en

-met betrekking tot alle andere door Finland geheven belastingen, op belastingen die worden geheven ter zake van belastbare tijdperken die aanvangen op of na 01/01/2021.

b) Ingevolge paragraaf 1 van artikel 36 van het MLI zijn de bepalingen van deel VI (Arbitrage) van het MLI van toepassing op deze Overeenkomst

- met betrekking tot zaken die aan de bevoegde autoriteit van een overeenkomstsluitende Staat worden voorgelegd op of na 1 oktober 2019; en

- met betrekking tot zaken die aan de bevoegde autoriteit van een overeenkomstsluitende Staat worden voorgelegd vóór 1 oktober 2019, op de datum waarop beide overeenkomstsluitende Staten de Secretaris-Generaal van de OESO kennis gegeven hebben van het feit dat zij onderling overeenstemming hebben bereikt overeenkomstig paragraaf 10 van artikel 19 (Verplichte en bindende arbitrage) van het MLI en met die kennisgeving ook inlichtingen verstrekt hebben over de datum of data waarop die zaken volgens de bereikte onderlinge overeenstemming beschouwd worden als zijnde voorgelegd aan de bevoegde autoriteit van een overeenkomstsluitende Staat (zoals omschreven in alinea a) van paragraaf 1 van artikel 19 (Verplichte en bindende arbitrage) van het MLI).

SYNTHESETEKST VAN HET MLI EN DE OVEREENKOMST TUSSEN HET KONINKRIJK BELGIË EN DE REPUBLIEK FINLAND TOT HET VERMIJDEN VAN DUBBELE BELASTING EN TOT HET VOORKOMEN VAN HET ONTGAAN VAN BELASTING INZAKE BELASTINGEN NAAR HET INKOMEN EN NAAR HET VERMOGEN, ONDERTEKEND TE BRUSSEL OP 18 MEI 1976, ZOALS GEWIJZIGD DOOR HET AANVULLEND AKKOORD ONDERTEKEND TE BRUSSEL OP 13 MAART 1991 EN DOOR HET PROTOCOL ONDERTEKEND TE BRUSSEL OP 15 SEPTEMBER 2009

De Regering van het Koninkrijk België en de Regering van de Republiek Finland,

[VERVANGEN door paragraaf 1 van artikel 6 van het MLI][WENSENDE een nieuwe Overeenkomst te sluiten tot het vermijden van dubbele belasting en het voorkomen van het ontgaan van belasting inzake belastingen naar het inkomen en naar het vermogen;]

De volgende paragraaf 1 van artikel 6 van het MLI vervangt de tekst die verwijst naar een voornemen om dubbele belasting te vermijden in de preambule van deze Overeenkomst

ARTIKEL 6 VAN HET MLI ─ DOEL VAN EEN GEDEKT BELASTINGVERDRAG

Voornemens dubbele belasting te vermijden met betrekking tot de onder [de Overeenkomst] vallende belastingen, zonder daarbij mogelijkheden te scheppen tot niet-heffing of verminderde heffing van belasting door middel van het ontduiken of het ontwijken van belasting (daaronder begrepen het gebruik van treaty-shopping-structuren die als doel hebben in [de Overeenkomst] voorziene tegemoetkomingen te verkrijgen in het indirecte voordeel van inwoners van derde rechtsgebieden),

Zijn als volgt overeengekomen :

Artikel 1
PERSONEN OP WIE DE OVEREENKOMST VAN TOEPASSING IS

Deze Overeenkomst is van toepassing op personen die inwoner zijn van een overeenkomstsluitende Staat of van beide overeenkomstsluitende Staten.

Artikel 2
BELASTINGEN WAAROP DE OVEREENKOMST VAN TOEPASSING IS

(1) Deze Overeenkomst is van toepassing op belastingen naar het inkomen en naar het vermogen die, ongeacht de wijze van heffing, worden geheven ten behoeve van elk van de overeenkomstsluitende Staten of van de openbare verenigingen of plaatselijke gemeenschappen daarvan.

(2) Als belastingen naar het inkomen en naar het vermogen worden beschouwd alle belastingen die worden geheven naar het gehele inkomen, naar het gehele vermogen of naar bestanddelen van het inkomen of van het vermogen, daaronder begrepen belastingen naar voordelen verkregen uit de vervreemding van roerende of onroerende goederen alsmede belastingen naar waardevermeerdering.

(3) De bestaande belastingen waarop de Overeenkomst van toepassing is, zijn met name :

(a) voor Finland :

(i) de Rijksbelasting op het inkomen en op het vermogen (tulo-ja varallisuusvero - inkomst - och förmögenhetsskatten) ;

(ii) de gemeentebelasting (kunnallisvero - kommunalskatten) ;

(iii) de kerkelijke belasting (kirkollisvero - kyrkoskatten) ;

(iv) de belasting op de zeelieden (merimiesvero - sjömanskatten) ; (hierna te noemen "Finse belasting").

(b) voor België :

(i) de personenbelasting ;

(ii) de vennootschapsbelasting ;

(iii) de rechtspersonenbelasting ;

(iv) de belasting der niet- verblijfhouders ;

    met inbegrip van de voorheffingen, de opdeciemen en opcentiemen op die belastingen en voorheffingen, alsmede de aanvullende gemeentebelasting op de personenbelasting ; (hierna te noemen "Belgische belasting").

(4) De Overeenkomst is ook van toepassing op alle gelijke of in wezen gelijksoortige belastingen die na de datum van de ondertekening van deze Overeenkomst naast of in de plaats van de bestaande belastingen worden geheven. De bevoegde autoriteiten van de overeenkomstsluitende Staten delen elkaar alle wezenlijke wijzigingen die in hun onderscheiden belastingwetten zijn aangebracht, mede.

Artikel 3
ALGEMENE BEPALINGEN

(1) In deze Overeenkomst, tenzij het zinsverband anders vereist :

(a) betekent de uitdrukking "Finland" de Republiek Finland en, in aardrijkskundig verband gebruikt, betekent zij het grondgebied van de Republiek Finland en elk gebied dat aan de territoriale wateren van de Republiek Finland grenst waarin volgens de wetgeving van Finland en in overeenstemming met het internationaal recht, de rechten van Finland met betrekking tot het opsporen en het winnen van de natuurlijke rijkdommen van de zeebodem en de ondergrond daarvan, kunnen worden uitgeoefend ; wat de gemeentebelasting betreft omvat de uitdrukking niet het Graafschap Aland ;

(b) betekent de uitdrukking "België" het Koninkrijk België ; in aardrijkskundig verband gebruikt, omvat zij elk gebied buiten de Belgische nationale soevereiniteit dat volgens de Belgische wetgeving betreffende het continentaal plat en in overeenstemming met het internationale recht, is aangeduid of later zal worden aangeduid, als een gebied waarin de rechten van België met betrekking tot de zeebodem en de ondergrond en de natuurlijke rijkdommen daarvan kunnen worden uitgeoefend ;

(c) omvat de uitdrukking "persoon" elke natuurlijke persoon, elke vennootschap, en elke andere vereniging van personen ;

(d) betekent de uitdrukking "vennootschap" elke rechtspersoon of elk lichaam dat in de overeenkomstsluitende Staat waarvan het een inwoner is, voor de belastingheffing als een rechtspersoon wordt behandeld ;

(e) betekenen de uitdrukkingen "onderneming van een overeenkomstsluitende Staat" en "onderneming van de andere overeenkomstsluitende Staat" onderscheidenlijk een onderneming gedreven door een inwoner van een overeenkomstsluitende Staat en een onderneming gedreven door een inwoner van de andere overeenkomstsluitende Staat ;

(f) betekent de uitdrukking "onderdaan" ;

(i) alle natuurlijke personen die de nationaliteit van een overeenkomstsluitende Staat bezitten ;

(ii) alle rechtspersonen, personenvennootschappen en verenigingen die hun rechtspositie als zodanig ontlenen aan de wetgeving die in een overeenkomstsluitende Staat van kracht is ;

(g) betekent de uitdrukking "internationaal verkeer" elk vervoer door middel van een schip of luchtvaartuig dat door een onderneming die haar plaats van werkelijke leiding in een overeenkomstsluitende Staat heeft, wordt geëxploiteerd, behalve indien het schip of het luchtvaartuig slechts tussen in de andere overeenkomstsluitende Staat gelegen plaatsen wordt geëxploiteerd ;

(h) betekent de uitdrukking "bevoegde autoriteit" :

(i) in Finland, de Minister van Financiën of zijn bevoegde vertegenwoordiger, en

(ii) in België, de Minister van Financiën of zijn bevoegde vertegenwoordiger.

(2) Voor de toepassing van de Overeenkomst door een overeenkomstsluitende Staat heeft, tenzij het zinsverband anders vereist, elke niet anders omschreven uitdrukking de betekenis welke die uitdrukking heeft volgens de wetgeving van die overeenkomstsluitende Staat met betrekking tot de belastingen die het onderwerp van de Overeenkomst uitmaken.

Artikel 4
FISCALE WOONPLAATS

(1) Voor de toepassing van deze Overeenkomst betekent de uitdrukking "inwoner van een overeenkomstsluitende Staat" iedere persoon wiens inkomen of vermogen ingevolge de wetgeving van die Staat aldaar aan belasting is onderworpen op grond van zijn woonplaats, verblijf, plaats van leiding of enige andere soortgelijke omstandigheid. Deze uitdrukking omvat echter niet personen die in die overeenkomstsluitende Staat enkel aan belasting zijn onderworpen ter zake van inkomsten uit aldaar gelegen bronnen of ter zake van in die Staat gelegen vermogen. Een onverdeelde nalatenschap wordt geacht inwoner te zijn van de overeenkomstsluitende Staat waarvan de overledene op het ogenblik van zijn overlijden, overeenkomstig de bepalingen van deze paragraaf of de bepalingen van paragraaf 2, een inwoner was.

(2) Indien een natuurlijke persoon ingevolge de bepalingen van paragraaf 1 inwoner van beide overeenkomstsluitende Staten is, wordt zijn toestand op de volgende wijze geregeld :

(a) hij wordt geacht inwoner te zijn van de overeenkomstsluitende Staat waar hij een duurzaam tehuis tot zijn beschikking heeft. Indien hij in beide overeenkomstsluitende Staten een duurzaam tehuis tot zijn beschikking heeft, wordt hij geacht inwoner te zijn van de overeenkomstsluitende Staat waarmede zijn persoonlijke en economische betrekkingen het nauwst zijn (middelpunt van de levensbelangen) ;

(b) indien niet kan worden bepaald in welke overeenkomstsluitende Staat hij het middelpunt van zijn levensbelangen heeft, of indien hij in geen van de overeenkomstsluitende Staten een duurzaam tehuis tot zijn beschikking heeft, wordt hij geacht inwoner te zijn van de overeenkomstsluitende Staat waar hij gewoonlijk verblijft ;

(c) indien hij in beide overeenkomstsluitende Staten of in geen van beide gewoonlijk verblijft, wordt hij geacht inwoner te zijn van de overeenkomstsluitende Staat waarvan hij onderdaan is ;

(d) indien hij onderdaan is van beide overeenkomstsluitende Staten of van geen van beide, regelen de bevoegde autoriteiten van de overeenkomstsluitende Staten de aangelegenheid in onderlinge overeenstemming.

(3) Indien een andere dan een natuurlijke persoon ingevolge de bepalingen van paragraaf 1 inwoner is van beide overeenkomstsluitende Staten, wordt hij geacht inwoner te zijn van de overeenkomstsluitende Staat waar de plaats van zijn werkelijke leiding is gelegen.

Artikel 5
VASTE INRICHTING

(1) Voor de toepassing van deze Overeenkomst betekent de uitdrukking "vaste inrichting" een vaste bedrijfsinrichting waarin de onderneming haar werkzaamheden geheel of gedeeltelijk uitoefent.

(2) De uitdrukking "vaste inrichting" omvat in het bijzonder :

(a) een plaats waar leiding wordt gegeven ;

(b) een filiaal ;

(c) een kantoor ;

(d) een fabriek ;

(e) een werkplaats ;

(f) een mijn, een steengroeve of enige andere plaats waar natuurlijke rijkdommen worden gewonnen ;

(g) de plaats van uitvoering van een bouwwerk of van constructiewerkzaamheden waarvan de duur twaalf maanden overschrijdt.

(3) Een vaste inrichting wordt niet aanwezig geacht indien :

(a) gebruik wordt gemaakt van inrichtingen, uitsluitend voor de opslag, uitstalling of aflevering van aan de onderneming toebehorende goederen ;

(b) een voorraad van aan de onderneming toebehorende goederen wordt aangehouden, uitsluitend voor de opslag, uitstalling of aflevering ;

(c) een voorraad van aan de onderneming toebehorende goederen wordt aangehouden, uitsluitend voor de bewerking of verwerking door een ander onderneming ;

(d) een vaste bedrijfsinrichting wordt aangehouden, uitsluitend om voor de onderneming goederen aan te kopen of inlichtingen in te winnen ;

(e) een vaste bedrijfsinrichting wordt aangehouden, uitsluitend voor reclamedoeleinden, voor het geven van inlichtingen, voor wetenschappelijk onderzoek of voor soortgelijke werkzaamheden ten behoeve van de onderneming die van voorbereidende aard zijn of het karakter van hulpwerkzaamheden hebben.

(4) Een persoon - niet zijnde een onafhankelijke vertegenwoordiger in de zin van paragraaf 5 - die in een overeenkomstsluitende Staat voor een onderneming van de andere overeenkomstsluitende Staat werkzaam is, wordt als een in de eerstbedoelde Staat aanwezige vaste inrichting beschouwd, indien hij een machtiging bezit om namens de onderneming overeenkomsten af te sluiten en dit recht in die Staat gewoonlijk uitoefent, tenzij zijn werkzaamheden beperkt blijven tot de aankoop van goederen voor de onderneming.

(5) Een onderneming van een overeenkomstsluitende Staat wordt niet geacht een vaste inrichting in de andere overeenkomstsluitende Staat te bezitten op grond van de enkele omstandigheid dat zij aldaar zaken doet door middel van een makelaar, een algemeen commissionair of enig andere onafhankelijke vertegenwoordiger, op voorwaarde dat deze personen in de normale uitoefening van hun bedrijf handelen.

(6) Niettegenstaande de bepalingen van de paragrafen 4 en 5 wordt een verzekeringsonderneming van een overeenkomstsluitende Staat beschouwd in de andere Staat een vaste inrichting te hebben indien zij in die andere Staat premies int of aldaar gelegen risico's verzekert door bemiddeling van een in paragraaf 4 bedoelde persoon of van een onafhankelijke vertegenwoordiger die een machtiging bezit om namens de onderneming overeenkomsten af te sluiten en dit recht gewoonlijk uitoefent.

(7) De enkele omstandigheid dat een vennootschap die inwoner is van een overeenkomstsluitende Staat, een vennootschap beheerst of door een vennootschap wordt beheerst, die inwoner is van de andere overeenkomstsluitende Staat of die in die andere Staat zaken doet (hetzij met behulp van een vaste inrichting hetzij op andere wijze), stempelt een van beide vennootschappen niet tot een vaste inrichting van de andere.

Artikel 6
INKOMSTEN UIT ONROERENDE GOEDEREN

(1) Inkomsten uit onroerende goederen, inkomsten uit landbouw- en bosbedrijven daaronder begrepen, mogen worden belast in de overeenkomstsluitende Staat waar deze goederen zijn gelegen.

(2) De uitdrukking "onroerende goederen" heeft de betekenis die daaraan wordt toegekend door de wetgeving van de overeenkomstsluitende Staat waar de desbetreffende goederen zijn gelegen. De uitdrukking omvat in ieder geval de goederen die bij de onroerende goederen behoren, de levende en dode have van landbouw- en bosbedrijven, de rechten waarop de bepalingen van het privaatrecht betreffende de grondeigendom van toepassing zijn, het vruchtgebruik van onroerende goederen en de rechten op veranderlijke of vaste vergoedingen ter zake van de exploitatie, of het recht tot exploitatie, van minerale aardlagen, bronnen en andere bodemrijkdommen ; schepen en luchtvaartuigen worden niet als onroerende goederen beschouwd.

(3) De bepalingen van paragraaf 1 zijn van toepassing op inkomsten verkregen uit de rechtstreekse exploitatie of het rechtstreekse genot, uit het verhuren of verpachten, of uit elke andere vorm van exploitatie van onroerende goederen.

(4) Indien de eigendom van aandelen of andere maatschappelijke rechten in een vennootschap die inwoner is van Finland de eigenaar van die aandelen of maatschappelijke rechten, recht geeft op het genot van onroerende goederen die aan de vennootschap toebehoren, mag het inkomen uit de rechtstreekse exploitatie of het rechtstreekse genot, uit het verhuren of verpachten, of-uit elke andere vorm van exploitatie van dat recht op genot, worden belast in de overeenkomstsluitende Staat waar de onroerende goederen zijn gelegen.

(5) De bepalingen van de paragrafen 1, 3 en 4 zijn ook van toepassing op inkomsten uit onroerende goederen van een onderneming en op inkomsten uit onroerende goederen gebezigd voor de uitoefening van een vrij beroep.

Artikel 7
ONDERNEMINGSWINST

(1) Winsten van een onderneming van een overeenkomstsluitende Staat zijn slechts in die Staat belastbaar, tenzij de onderneming in de andere overeenkomstsluitende Staat haar bedrijf uitoefent met behulp van een aldaar gevestigde vaste inrichting. Indien de onderneming aldus haar bedrijf uitoefent, mogen de winsten van de onderneming in de andere Staat worden belast, maar slechts in zoverre als zij aan die vaste inrichting kunnen worden toegerekend.

(2) Onverminderd het bepaalde in paragraaf 3 worden, indien een onderneming van een overeenkomstsluitende Staat in de andere overeenkomstsluitende Staat haar bedrijf uitoefent met behulp van een aldaar gevestigde vaste inrichting, in elke overeenkomstsluitende Staat aan die vaste inrichting de winsten toegerekend die zij geacht zou kunnen worden te behalen indien zij een onafhankelijke en zelfstandige onderneming zou zijn, die dezelfde of soortgelijke werkzaamheden zou uitoefenen onder dezelfde of soortgelijke omstandigheden en die geheel onafhankelijk met de onderneming waarvan zij een vaste inrichting is zou handelen.

(3) Bij het bepalen van de winsten van een vaste inrichting worden in aftrek toegelaten de kosten, daaronder begrepen kosten van de leiding en algemene beheerskosten, die ten behoeve van de vaste inrichting zijn gemaakt, hetzij in de Staat waar de vaste inrichting is gevestigd, hetzij elders.

(4) Voor zover het in een overeenkomstsluitende Staat gebruikelijk is de aan een vaste inrichting toe te rekenen winsten te bepalen op basis van een verdeling van de totale winst van de onderneming, over haar verschillende delen, belet paragraaf 2 die overeenkomstsluitende Staat niet de belastbare winsten te bepalen volgens de gebruikelijke verdeling ; de gevolgde methode van verdeling moet echter zodanig zijn dat het bekomen resultaat in overeenstemming is met de beginselen van dit artikel.

(5) Geen winsten worden aan een vaste inrichting toegerekend enkel op grond van aankoop door die vaste inrichting van goederen voor de onderneming.

(6) Voor de toepassing van de voorgaande paragrafen worden de aan de vaste inrichting toe te rekenen winsten van jaar tot jaar volgens dezelfde methode bepaald, tenzij er een goede en genoegzame reden bestaat om hiervan af te wijken.

(7) Indien in de winsten bestanddelen van het inkomen zijn begrepen die afzonderlijk in andere artikelen van deze Overeenkomst worden behandeld, worden de bepalingen van die artikelen niet aangetast door de bepalingen van dit artikel.

Artikel 8
ZEEVAART EN LUCHTVAART

(1) Winsten uit de exploitatie van schepen of luchtvaartuigen in internationaal verkeer zijn slechts belastbaar in de overeenkomstsluitende Staat waar de plaats van de werkelijke leiding van de onderneming is gelegen.

(2) Indien de plaats van de werkelijke leiding van een scheepvaartonderneming zich aan boord van een schip bevindt, wordt deze plaats geacht te zijn gelegen in de overeenkomstsluitende Staat waar het schip zijn thuishaven heeft, of, indien er geen thuishaven is, in de overeenkomstsluitende Staat waarvan de exploitant van het schip inwoner is.

(3) De bepaling van paragraaf 1 is ook van toepassing op winsten verkregen uit de deelneming aan een pool, een gemeenschappelijke organisatie of een internationaal geëxploiteerd agentschap.

Artikel 9
AFHANKELIJKE ONDERNEMINGEN

(1) Indien :

(a) een onderneming van een overeenkomstsluitende Staat onmiddellijk of middellijk deelneemt aan de leiding van, aan het toezicht op, dan wel in het kapitaal van een onderneming van de andere overeenkomstsluitende Staat, of

(b) dezelfde personen onmiddellijk of middellijk deelnemen aan de leiding van, aan het toezicht op, dan wel in het kapitaal van een onderneming van een overeenkomstsluitende Staat en van een onderneming van de andere overeenkomstsluitende Staat,

    en in het ene of in het andere geval tussen beide ondernemingen in hun handelsbetrekkingen of financiële betrekkingen, voorwaarden worden aanvaard of opgelegd die afwijken van die welke zouden worden overeengekomen tussen onafhankelijke ondernemingen, mogen de winsten welke zonder deze voorwaarden door een van de ondernemingen zouden zijn behaald maar ten gevolge van die voorwaarden niet zijn behaald, worden begrepen in de winsten van die onderneming en dienovereenkomstig worden belast.

(2) Indien winsten, ter zake waarvan een onderneming van een overeenkomstsluitende Staat in die Staat werden belast, op grond van paragraaf 1 eveneens in de winsten van een onderneming van de andere overeenkomstsluitende Staat zijn begrepen en dienovereenkomstig zijn belast, en deze winsten bestaan uit winsten waarvan had mogen worden verwacht dat zij door de onderneming van de andere Staat zouden zijn behaald, indien tussen de ondernemingen zodanige voorwaarden hadden gegolden als hadden mogen worden verwacht te gelden tussen onafhankelijke ondernemingen die volledig onafhankelijk met elkaar zaken doen, herziet de eerstbedoelde Staat op de hem geschikt voorkomende wijze het bedrag aan belasting dat in die Staat over die winsten is geheven. Bij deze herziening wordt rekening gehouden met de overige bepalingen van deze Overeenkomst en te dien einde plegen de bevoegde autoriteiten van de overeenkomstsluitende Staten zo nodig met elkaar overleg.

Artikel 10
DIVIDENDEN

 (1) Dividenden betaald door een vennootschap die inwoner is van een overeenkomstsluitende Staat aan een inwoner van de andere overeenkomstsluitende Staat, mogen in die andere Staat worden belast.

(2) Deze dividenden mogen echter in de overeenkomstsluitende Staat waarvan de vennootschap die de dividenden betaalt inwoner is, overeenkomstig de wetgeving van die Staat worden belast, maar indien de persoon die de dividenden ontvangt de werkelijke genieter ervan is, mag de aldus geheven belasting niet hoger zijn dan :

a) 5 percent van het brutobedrag van de dividenden indien die persoon een vennootschap is die onmiddellijk ten minste 25 percent bezit van het kapitaal van de vennootschap die de dividenden betaalt ;

b) 15 percent van het brutobedrag van de dividenden in alle andere gevallen.

Deze paragraaf laat onverlet de belastingheffing van de vennootschap ter zake van de winst waaruit de dividenden worden betaald.

(3) De uitdrukking "dividenden", zoals gebezigd in dit artikel, betekent inkomsten uit aandelen of andere rechten op een aandeel in de winst, met uitzondering van schuldvorderingen, alsmede inkomsten uit andere rechten in vennootschappen die ingevolge de belastingwetgeving van de Staat waarvan de uitkerende vennootschap inwoner is, op dezelfde wijze als inkomsten uit aandelen in de belastingheffing worden betrokken. Die uitdrukking betekent ook inkomsten, zelfs indien zij worden toegekend in de vorm van interest, die belastbaar zijn als inkomsten van belegde kapitalen van vennoten in vennootschappen, niet zijnde vennootschappen op aandelen, die inwoner zijn van België.

(4) De bepalingen van de paragrafen 1 en 2 zijn niet van toepassing indien de genieter van de dividenden, die inwoner is van een overeenkomstsluitende Staat, in de andere overeenkomstsluitende Staat waarvan de vennootschap die de dividenden betaalt inwoner is, een bedrijf met behulp van een aldaar gevestigde vaste inrichting of een vrij beroep door middel van een aldaar gevestigde vaste basis uitoefent en het aandelenbezit uit hoofde waarvan de dividenden worden betaald, met die vaste inrichting op vaste basis wezenlijk is verbonden. In dat geval zijn de bepalingen van artikel 7 of van artikel 14, naar het geval, van toepassing.

(5) Indien een vennootschap die inwoner is van een overeenkomstsluitende Staat winsten of inkomsten verkrijgt uit de andere overeenkomstsluitende Staat, mag die andere Staat geen belasting heffen op dividenden die door de vennootschap aan een inwoner van de eerstbedoelde Staat worden betaald, noch de niet-uitgedeelde winst van de vennootschap onderwerpen aan een belasting op de niet-uitgedeelde winst van de vennootschap, zelfs indien de betaalde dividenden of de niet-uitgedeelde winst geheel of gedeeltelijk bestaan uit winsten of inkomsten die uit die andere Staat afkomstig zijn ; deze bepaling belet die andere Staat niet belasting te heffen op dividenden verkregen uit hoofde van een aandelenbezit dat wezenlijk verbonden is met een in die andere Staat gelegen vaste inrichting of vaste basis.

Artikel 11
INTEREST

(1) Interest afkomstig uit een overeenkomstsluitende Staat en betaald aan een inwoner van de andere overeenkomstsluitende Staat, mag in die andere Staat worden belast.

(2) Deze interest mag echter in de overeenkomstsluitende Staat waaruit hij afkomstig is, overeenkomstig de wetgeving van die Staat worden belast, maar indien de persoon die de interest ontvangt de werkelijke genieter van de interest is, mag de aldus geheven belasting niet hoger zijn dan 10 pct. van het bedrag van de interest.

(3) De uitdrukking "interest" zoals gebezigd in dit artikel, betekent inkomsten uit schuldvorderingen van welke aard ook, al dan niet gewaarborgd door hypotheek en al dan niet aanspraak gevend op een aandeel in de winst van de schuldenaar, en in het bijzonder inkomsten uit overheidsleningen en obligaties, daaronder begrepen premies en loten op die effecten.

    Die uitdrukking omvat niet :

(a) interest die volgens de Belgische wetgeving belastbaar is als inkomen van belegde kapitalen van vennoten in andere vennootschappen dan op aandelen die inwoner van België zijn ; die interest wordt in paragraaf 3 van artikel 10 met dividenden gelijkgesteld ;

(b) boeten voor laattijdige betaling ;

(c) interest van handelsschuldvorderingen - daaronder begrepen vorderingen vertegenwoordigd door handelspapier wegens termijnbetaling van koopwaar, goederen of diensten geleverd door een onderneming ;

(d) interest van rekeningen-courant of van voorschotten tussen bankondernemingen van de overeenkomstsluitende Staten ;

(e) interest van niet door effecten aan toonder vertegenwoordigde gelddeposito's of geldsommen bij bankondernemingen daaronder begrepen openbare kredietinstellingen.

    De in (c) en (d) van het vorige lid vermelde interest is onderworpen aan de bepalingen van artikel 7 en de in (b) en (e) vermelde interest is onderworpen aan de bepalingen van artikel 7 of van artikel 21, naar het geval.

(4) De bepalingen van de paragrafen 1 en 2 zijn niet van toepassing, indien de genieter van de interest die inwoner is van een overeenkomstsluitende Staat, in de andere overeenkomstsluitende Staat waaruit de interest afkomstig is, een bedrijf met behulp van een aldaar gevestigde vaste inrichting of een vrij beroep door middel van een aldaar gevestigde vaste basis uitoefent en de schuldvordering uit hoofde waarvan de interest is verschuldigd, met die vaste inrichting of vaste basis wezenlijk is verbonden. In dat geval zijn de bepalingen van artikel 7 of van artikel 14, naar het geval, van toepassing.

(5) Interest wordt geacht uit een overeenkomstsluitende Staat afkomstig te zijn indien de schuldenaar die Staat zelf is, een openbare vereniging of een plaatselijke gemeenschap daarvan of een inwoner van die Staat. Indien evenwel de schuldenaar van de interest, ongeacht of hij inwoner van een overeenkomstsluitende Staat is of niet, in een overeenkomstsluitende Staat een vaste inrichting heeft waarvoor de lening uit hoofde waarvan de interest is verschuldigd werd aangegaan en de interest ten laste valt van die vaste inrichting, wordt die interest geacht afkomstig te zijn uit de overeenkomstsluitende Staat waar de vaste inrichting is gevestigd.

(6) Indien, ten gevolge van een bijzondere verhouding tussen de schuldenaar en de schuldeiser of tussen hen beiden en een derde, het bedrag van de interest, gelet op de schuldvordering waarvoor hij wordt betaald, hoger is dan het bedrag dat zonder zulk een verhouding door de schuldenaar en de schuldeiser zou zijn overeengekomen, zijn de bepalingen van dit artikel slechts op het laatstbedoelde bedrag van toepassing. In dat geval mag het daarboven uitgaande deel van de interest in de overeenkomstsluitende Staat waaruit hij afkomstig is worden belast overeenkomstig de wetgeving van die Staat.

Artikel 12
ROYALTY'S

(1) Royalty's afkomstig uit een overeenkomstsluitende Staat en betaald aan een inwoner van de andere overeenkomstsluitende Staat mogen in die andere Staat worden belast.

(2) De in lid (b) van paragraaf 3 bedoelde royalty's mogen echter in de overeenkomstsluitende Staat waaruit zij afkomstig zijn, overeenkomstig de wetgeving van die Staat worden belast, maar indien de persoon die de royalty's ontvangt de werkelijke genieter van de royalty's is, mag de aldus geheven belasting niet hoger zijn dan 5 pct. van het brutobedrag van de royalty's.

(3) De uitdrukking "royalty's", zoals gebezigd in dit artikel, betekent betalingen van elke aard als vergoeding voor het gebruik van, of voor het recht van gebruik van :

(a) een auteursrecht op een werk op het gebied van letterkunde, kunst of wetenschap, daaronder begrepen bioscoopfilms en films of banden voor televisie- of radio-uitzendingen ;

(b) een octrooi, een fabrieks- of handelsmerk, een tekening, een model, een plan, een geheim recept of een geheime werkwijze, alsmede en nijverheids- of handelsuitrusting of wetenschappelijke uitrusting, of voor inlichtingen omtrent ervaringen op het gebied van nijverheid, handel of wetenschap.

(4) De bepalingen van de paragrafen 1 en 2 zijn niet van toepassing indien de genieter van de royalty's die inwoner is van een overeenkomstsluitende Staat, in de andere overeenkomstsluitende Staat waaruit de royalty's afkomstig zijn, een bedrijf met behulp van een aldaar gevestigde vaste inrichting of een vrij beroep door middel van een aldaar gevestigde vaste basis uitoefent en het recht of het goed uit hoofde waarvan de royalty's verschuldigd zijn, met die vaste inrichting of vaste basis wezenlijk is verbonden. In dat geval zijn de bepalingen van artikel 7 of van artikel 14, naar het geval, van toepassing.

(5) Royalty's worden geacht uit een overeenkomstsluitende Staat afkomstig te zijn indien de schuldenaar die overeenkomstsluitende Staat zelf is, een openbare vereniging, een plaatselijke gemeenschap daarvan of een inwoner van die Staat. Indien evenwel de schuldenaar van de royalty's, ongeacht of hij inwoner van een overeenkomstsluitende Staat is of niet, in een overeenkomstsluitende Staat een vaste inrichting heeft waarvoor de overeenkomst uit hoofde waarvan de royalty's verschuldigd zijn werd aangegaan en de royalty's ten laste vallen van die vaste inrichting worden die royalty's geacht afkomstig te zijn uit de overeenkomstsluitende Staat waar de vaste inrichting is gevestigd.

(6) Indien, ten gevolge van een bijzondere verhouding tussen de schuldenaar en de schuldeiser of tussen hen beiden en een derde, het bedrag van de royalty's, gelet op het gebruik, het recht of de inlichtingen waarvoor zij worden betaald, hoger is dan het bedrag dat zonder zulk een verhouding door de schuldenaar en de schuldeiser zou zijn overeengekomen, zijn de bepalingen van dit artikel slechts op het laatstbedoelde bedrag van toepassing. In dat geval mag het daarboven uitgaande deel van de royalty's in de overeenkomstsluitende Staat waaruit de royalty's afkomstig zijn worden belast overeenkomstig de wetgeving van de Staat.

Artikel 13
VERMOGENSWINSTEN

(1) Voordelen verkregen uit de vervreemding van onroerende goederen, als omschreven in artikel 6, paragraaf 2, mogen worden belast in de overeenkomstsluitende Staat waar deze goederen zijn gelegen.

(2) Voordelen verkregen uit de vervreemding van roerende goederen die deel uitmaken van het bedrijfsvermogen van een vaste inrichting die een onderneming van een overeenkomstsluitende Staat in de andere overeenkomstsluitende Staat heeft, of van roerende goederen die behoren tot een vaste basis die een inwoner van een overeenkomstsluitende Staat in de andere overeenkomstsluitende Staat tot zijn beschikking heeft voor de uitoefening van een vrij beroep, daaronder begrepen voordelen verkregen uit de vervreemding van die vaste inrichting (alleen of te zamen met de gehele onderneming) of van die vaste basis, mogen in die andere Staat worden belast. Voordelen verkregen uit de vervreemding van roerende goederen zoals bedoeld in paragraaf 3 van artikel 23 zijn evenwel slechts belastbaar in de overeenkomstsluitende Staat waar die roerende goederen overeenkomstig gezegd artikel belastbaar zijn.

(3) Voordelen verkregen uit de vervreemding van maatschappelijke rechten waarvan sprake in artikel 6, paragraaf 4, mogen worden belast in de overeenkomstsluitende Staat waar de onroerende goederen die in het bezit zijn van de vennootschap, zijn gelegen.

(4) Voordelen verkregen uit de vervreemding van alle andere goederen dan die vermeld in de paragrafen 1, 2 en 3, zijn slechts belastbaar in de overeenkomstsluitende Staat waarvan de vervreemder inwoner is.

Artikel 14
VRIJE BEROEPEN

(1) Inkomsten verkregen door een inwoner van een overeenkomstsluitende Staat in de uitoefening van een vrij beroep of ter zake van andere zelfstandige werkzaamheden van soortgelijke aard zijn slechts in die Staat belastbaar, tenzij die inwoner in de andere overeenkomstsluitende Staat voor het verrichten van zijn werkzaamheden geregeld over een vaste basis beschikt. Indien hij over zulk een vaste basis beschikt, mogen de inkomsten in de andere overeenkomstsluitende Staat worden belast, maar slechts in zoverre als zij aan die vaste basis kunnen worden toegerekend.

(2) De uitdrukking "vrij beroep" omvat in het bijzonder zelfstandige werkzaamheden op het gebied van wetenschap, letterkunde, kunst, opvoeding of onderwijs, alsmede de zelfstandige werkzaamheden van artsen, advocaten, ingenieurs, architecten, tandartsen en accountant.

Artikel 15
NIET-ZELFSTANDIGE BEROEPEN

(1) Onder voorbehoud van de bepalingen van de artikelen 16, 18, 19 en 20, zijn lonen, salarissen en andere, soortgelijke beloningen verkregen door een inwoner van een overeenkomstsluitende Staat ter zake van een dienstbetrekking slechts in die Staat belastbaar, tenzij de dienstbetrekking in de andere overeenkomstsluitende Staat wordt uitgeoefend. Indien de dienstbetrekking aldaar wordt uitgeoefend, mogen de ter zake daarvan verkregen beloningen in die andere Staat worden belast.

(2) Niettegenstaande de bepalingen van paragraaf 1 zijn beloningen verkregen door een inwoner van een overeenkomstsluitende Staat ter zake van een in de andere overeenkomstsluitende Staat- uitgeoefende dienstbetrekking slechts in de eerstbedoelde Staat belastbaar, indien :

(a) de genieter in de andere Staat verblijft gedurende een tijdvak of tijdvakken die in het desbetreffende kalenderjaar een totaal van 183 dagen niet te boven gaan, en

(b) de beloningen worden betaald door of namens een werkgever die geen inwoner van de Staat is, en

(c) de beloningen niet ten laste vallen van een vaste inrichting of een vaste basis, die de werkgever in de andere Staat heeft.

(3) Niettegenstaande de voorgaande bepalingen van dit artikel, mogen beloningen ter zake van een dienstbetrekking uitgeoefend aan boord van een schip of luchtvaartuig in internationaal verkeer, worden belast in de overeenkomstsluitende Staat waar de zetel van de werkelijke leiding van de onderneming is gelegen.

Artikel 16
TANTIÈMES

(1) Tantièmes, presentiegelden en andere soortgelijke beloningen, door een inwoner van een overeenkomstsluitende Staat verkregen in zijn hoedanigheid van lid van de raad van bestuur of van toezicht of van een gelijkaardig orgaan van een vennootschap die inwoner is van de andere overeenkomstsluitende Staat, mogen in die andere Staat worden belast. Deze bepaling is ook van toepassing op beloningen verkregen ter zake van de uitoefening van werkzaamheden die volgens de wetgeving van de overeenkomstsluitende Staat waarvan de vennootschap inwoner is, worden behandeld als werkzaamheden van soortgelijke aard als die welke hiervoor worden bedoeld.

(2) Beloningen betaald door een vennootschap aan haar bestuurders ter zake van de uitoefening van dagelijkse werkzaamheden van leidinggevende of van technische aard en beloningen betaald door een vennootschap, niet zijnde een vennootschap op aandelen, aan haar vennoten ter zake van hun in die hoedanigheid uitgeoefend persoonlijke werkzaamheden, mogen overeenkomstig de bepalingen van artikel 15, paragraaf 1, worden belast alsof de beloningen zouden zijn betaald ter zake van een dienstbetrekking.

Artikel 17

ARTIESTEN EN SPORTBEOEFENAARS

(1) Niettegenstaande de bepalingen van de artikelen 14 en 15 mogen inkomsten die artiesten, zoals toneelspelers, film-, radio- of televisieartiesten en musici, alsmede sportbeoefenaars, als zodanig uit hun persoonlijke werkzaamheden verkrijgen, worden belast in de overeenkomstsluitende Staat waar deze werkzaamheden worden verricht.

(2) Indien inkomsten uit de persoonlijke werkzaamheden van artiesten of sportbeoefenaars als zodanig worden toegekend aan een andere persoon dan de artiest of de sportbeoefenaar zelf, mogen deze inkomsten, niettegenstaande de bepalingen van de artikelen 7, 14 en 15, worden belast in de overeenkomstsluitende Staat waar de werkzaamheden van de artiest of de sportbeoefenaar worden verricht.

Artikel 18
PENSIOENEN EN LIJFRENTEN

(1) Onder voorbehoud van de bepalingen van artikel 19, paragraaf 2, zijn pensioenen en andere soortgelijke beloningen betaald aan een inwoner van een overeenkomstsluitende Staat ter zake van een vroegere dienstbetrekking, slechts in die Staat belastbaar.

(2) Niettegenstaande de bepalingen van paragraaf 1, en onder voorbehoud van de bepalingen van artikel 19, paragraaf 2, mogen pensioenen en andere periodieke of niet periodieke uitkeringen betaald overeenkomstig de sociale zekerheidswetgeving van een overeenkomstsluitende Staat of overeenkomstig een algemene regeling ter bevordering van het maatschappelijk welzijn van een overeenkomstsluitende Staat en lijfrenten die uit die Staat afkomstig zijn, in die Staat worden belast.

(3) De uitdrukking "lijfrenten", zoals gebezigd in dit artikel, betekent een vaste som, periodiek betaalbaar op vaste tijdstippen, gedurende het leven of gedurende een vastgestelde of voor vaststelling vatbaar tijdvak, ingevolge een verbintenis tot het doen van betalingen, welke tegenover een voldoende en volledige tegenprestatie in geld of geldswaarde staat (niet zijnde bewezen diensten).

Artikel 19
OVERHEIDSFUNCTIES

(1) (a) Beloningen, niet zijnde pensioenen, door een overeenkomstsluitende Staat of een openbare vereniging of plaatselijke gemeenschap daarvan betaald aan een natuurlijke persoon ter zake van diensten bewezen aan die Staat of aan die openbare vereniging of die plaatselijke gemeenschap daarvan, zijn slechts in die Staat belastbaar.

(b) Die beloningen zijn evenwel slechts belastbaar in de overeenkomstsluitende Staat waarvan de genieter een inwoner is indien de diensten in die Staat worden bewezen en de genieter :

(i) onderdaan van die Staat is ; of

(ii) niet van die Staat inwoner is geworden uitsluitend om er de diensten uit te oefenen.

(2) (a) Pensioenen betaald door, of uit fondsen in het leven geroepen door een overeenkomstsluitende Staat of een openbare vereniging of plaatselijke gemeenschap daarvan, aan een natuurlijke persoon ter zake van diensten bewezen aan die Staat, aan die openbare vereniging of die plaatselijke gemeenschap daarvan, zijn slechts in die Staat belastbaar.

(b) Die pensioenen zijn evenwel slechts belastbaar in de overeenkomstsluitende Staat waarvan de genieter een inwoner is, indien hij een onderdaan van die Staat is.

(3) De bepalingen van de artikelen 15, 16 en 18 zijn van toepassing op beloningen en pensioenen ter zake van diensten bewezen in het kader van een op winst gericht bedrijf uitgeoefend door een overeenkomstsluitende Staat of een openbare vereniging of een plaatselijke gemeenschap daarvan.

Artikel 20
STUDENTEN

(1) Betalingen die een student of een voor een bedrijf of een technisch, landbouwkundig of bosbouwkundig beroep in opleiding zijnde persoon die uitsluitend voor zijn studie of opleiding in een overeenkomstsluitende Staat verblijft en die onmiddellijk voor zijn vertrek een inwoner van de andere overeenkomstsluitende Staat is of was, ontvangt ten behoeve van zijn onderhoud, studie of opleiding, worden in de eerstbedoelde overeenkomstsluitende Staat niet belast, op voorwaarde dat die betalingen hem uit bronnen buiten die Staat worden gedaan.

(2) Een student aan een universiteit of aan een andere instelling voor hogere studies in een overeenkomstsluitende Staat, of een voor een bedrijf, of een technisch, landbouwkundig of bosbouwkundig beroep in opleiding zijnde persoon die in de andere overeenkomstsluitende Staat verblijft voor een tijdvak of tijdvakken van in totaal niet meer dan 183 dagen in het desbetreffende kalenderjaar en die onmiddellijk voor zijn vertrek een inwoner van de eerstbedoelde Staat is zoals, wordt in de andere overeenkomstsluitende Staat niet belast ter zake van beloningen voor in die andere Staat bewezen diensten, op voorwaarde dat die diensten verband houden met zijn studies of opleiding en de beloningen inkomsten uitmaken die nodig zijn om in zijn onderhoud te voorzien.

Artikel 21
ANDERE INKOMSTEN

(1) Ongeacht de afkomst ervan zijn bestanddelen van het inkomen van een inwoner van een overeenkomstsluitende Staat die niet uitdrukkelijk in de voorgaande artikelen van deze Overeenkomst zijn vermeld slechts in die Staat belastbaar.

(2) De bepaling van paragraaf 1 is niet van toepassing indien de genieter van het inkomen die inwoner is van een overeenkomstsluitende Staat, in de andere overeenkomstsluitende Staat een bedrijf met behulp van een aldaar gevestigde vaste inrichting of een vrij beroep door middel van een aldaar gevestigde vaste basis uitoefen en het recht of het goed dat het inkomen oplevert met die vaste inrichting of vaste basis wezenlijk is verbonden. In dat geval zijn de bepalingen van artikel 7 of van artikel 14, naar het geval, van toepassing.

Artikel 22
ONVERDEELDE NALATENSCHAPPEN

Indien ingevolge de bepalingen van deze Overeenkomst een inwoner van België vrijgesteld is van, of gerechtigd is op vermindering van Finse belasting, is een soortgelijke vrijstelling of vermindering van toepassing op onverdeelde nalatenschappen in zo verre als één of meer van de genieters inwoner van België zijn.

Artikel 23
VERMOGEN

(1) Vermogen bestaande uit onroerende goederen als omschreven in artikel 6, paragraaf 2, mag worden belast in de overeenkomstsluitende Staat waar deze goederen zijn gelegen.

(2) Vermogen bestaande uit roerende goederen die deel uitmaken van het bedrijfsvermogen van een vaste inrichting van een onderneming, of uit roerende goederen die behoren tot een vaste basis gebezigd voor de uitoefening van een vrij beroep, mag worden belast in de overeenkomstsluitende Staat waar de vaste inrichting of de vaste basis is gelegen.

(3) Schepen en luchtvaartuigen die in internationaal verkeer worden geëxploiteerd, en roerende goederen die bij de exploitatie van deze schepen en luchtvaartuigen worden gebruikt, zijn slechts belastbaar in de overeenkomstsluitende Staat waar de plaats van de werkelijke leiding van de onderneming is gelegen.

(4) De maatschappelijke rechten vermeld in artikel 6, paragraaf 4, mogen worden belast in de overeenkomstsluitende Staat waar het onroerend goed dat aan de vennootschap toebehoort, is gelegen.

(5) Alle andere bestanddelen van het vermogen van een inwoner van een overeenkomstsluitende Staat zijn slechts in die Staat belastbaar.

Artikel 24
VERMIJDING VAN DUBBELE BELASTING

(1) In Finland wordt dubbele belasting op de volgende wijze vermeden :

(a) Indien een inwoner van Finland inkomsten verkrijgt of vermogensbestanddelen bezit die in overeenstemming met de bepalingen van deze Overeenkomst in België mogen worden belast, verleent Finland, onder voorbehoud van de bepalingen van subparagraaf b) :

(i) een vermindering op de belasting naar het inkomen van die persoon tot een bedrag dat gelijk is aan de in België betaalde belasting naar het inkomen ;

(ii) een vermindering op de belasting naar het vermogen van die persoon tot een bedrag dat gelijk is aan de in België betaalde belasting naar het vermogen.

    Deze vermindering overschrijdt echter in geen van beide gevallen dat deel van de belastingen naar het inkomen of naar het vermogen, zoals deze berekend zijn vóór het verlenen van de vermindering, dat kan worden toegerekend aan het inkomen of aan het vermogen, naar gelang van het geval, dat in België mag worden belast.

(b) Dividenden betaald door een vennootschap die inwoner is van België aan een vennootschap die inwoner is van Finland en die onmiddellijk ten minste 10 percent van het stemrecht bezit in de vennootschap die de dividenden betaalt, zijn vrijgesteld van de Finse belasting.

(c) Indien een inwoner van Finland inkomsten verkrijgt of vermogensbestanddelen bezit die ingevolge de bepalingen van de Overeenkomst in Finland van belasting zijn vrijgesteld, mag Finland evenwel, om het bedrag van de belasting op het overige inkomen of vermogen van die inwoner te berekenen, de vrijgestelde inkomsten of het vrijgestelde vermogen in aanmerking nemen.

(2) In België wordt dubbele belasting op de volgende wijze vermeden :

(a) Indien een inwoner van België inkomsten verkrijgt die, of vermogen bezit dat, ingevolge de bepalingen van deze Overeenkomst, niet zijnde de bepalingen van artikel 10, paragraaf 2, van artikel 11, paragrafen 2 en 6, en van artikel 12, paragrafen 2 en 6, in Finland mogen worden belast, stelt België die inkomsten of dat vermogen vrij van belasting, maar om het bedrag van de belasting op het overige inkomen of vermogen van die inwoner te berekenen, mag België het belastingtarief toepassen dat van toepassing zou zijn indien die inkomsten of dat vermogen niet waren vrijgesteld.

(b) Indien een inwoner van België inkomsten verkrijgt die deel uitmaken van zijn samengetelde inkomen dat aan de Belgische belasting is onderworpen, en die bestaan uit dividenden die belastbaar zijn ingevolge artikel 10, paragraaf 2, en niet van Belgische belasting zijn vrijgesteld ingevolge subparagraaf e) hierna, uit interest die belastbaar is ingevolge artikel 11, paragraaf 2 of 6, of uit royalty's die belastbaar zijn ingevolge artikel 12, paragraaf 2 of 6, wordt het forfaitaire gedeelte van de buitenlandse belasting waarin de Belgische wetgeving voorziet, op de voorwaarden en tegen het tarief van die wetgeving verrekend met de Belgische belasting op die inkomsten.

(c) Indien een inwoner van België inkomsten verkrijgt die overeenkomstig de bepalingen van artikel 13, paragraaf 3, in Finland werden belast, mag het bedrag van de Belgische belasting dat evenredig betrekking heeft op die inkomsten niet hoger zijn dan het bedrag dat volgens de Belgische wetgeving zou worden geheven indien die inkomsten als in het buitenland behaalde en belaste beroepsinkomsten belastbaar zouden zijn.

(d) Indien een inwoner van België inkomsten verkrijgt uit een onverdeelde nalatenschap die inwoner is van Finland, en die inkomsten op grond van de Overeenkomst in Finland mogen worden belast, zijn de bepalingen van subparagraaf a) of subparagraaf b), van toepassing naar gelang van de aard van de inkomsten.

(e) Indien een vennootschap die inwoner is van België, aandelen in eigendom bezit van een vennootschap die inwoner is van Finland, worden de dividenden die haar door de laatstbedoelde vennootschap worden betaald, in België vrijgesteld van de vennootschapsbelasting op de voorwaarden en binnen de grenzen bepaald in de Belgische wetgeving.

(f) Indien verliezen van een onderneming gedreven door een inwoner van België die aan een in Finland gelegen vaste inrichting kunnen worden toegerekend voor de belastingheffing van die onderneming in België volgens de Belgische wetgeving werkelijk in mindering van de winsten van die onderneming werden gebracht, is de vrijstelling ingevolge subparagraaf a) in België niet van toepassing op de winsten van andere belastbare tijdperken die aan die vaste inrichting kunnen worden toegerekend, voor zover deze winsten ook in Finland door de verrekening van die verliezen van belasting werden vrijgesteld.

Artikel 25
NON-DISCRIMINATIE

(1) Onderdanen van een overeenkomstsluitende Staat, ongeacht of zij al dan niet inwoner zijn van een overeenkomstsluitende Staat, worden in de andere overeenkomstsluitende Staat niet onderworpen aan enige belastingheffing of daarmede verband houdende verplichting, die anders of zwaarder is dan de belastingheffing en daarmede verband houdende verplichtingen waaraan onderdanen van die andere Staat onder gelijke omstandigheden worden of kunnen worden onderworpen.

(2) De belastingheffing van een vaste inrichting die een onderneming van een overeenkomstsluitende Staat in de andere overeenkomstsluitende Staat heeft, is in die andere Staat niet ongunstiger dan de belastingheffing van ondernemingen van die andere Staat die dezelfde werkzaamheden uitoefenen.

    Deze bepaling mag niet aldus worden uitgelegd dat zij een overeenkomstsluitende Staat verplicht aan inwoners van de andere overeenkomstsluitende Staat bij de belastingheffing de persoonlijke aftrekken, tegemoetkomingen en verminderingen uit hoofde van de samenstelling van het gezin of van gezinslasten te verlenen die de eerstbedoelde Staat aan zijn eigen inwoners verleent.

(3) Behoudens in geval van toepassing van artikel 9, paragraaf 1, van artikel 11, paragraaf 6, of van artikel 12, paragraaf 6, worden interest, royalty's en andere kosten, die door een onderneming van een overeenkomstsluitende Staat aan een inwoner van de andere overeenkomstsluitende Staat worden betaald, bij het bepalen van de belastbare winst van die onderneming op dezelfde voorwaarden in mindering gebracht, alsof zij aan een inwoner van de eerstbedoelde Staat zouden zijn betaald.

Schulden van een onderneming van een overeenkomstsluitende Staat tegenover een inwoner van de andere overeenkomstsluitende Staat worden bij het bepalen van het belastbare vermogen van die onderneming eveneens op dezelfde voorwaarden in mindering gebracht, alsof die schulden tegenover een inwoner van de eerstbedoelde Staat zouden zijn aangegaan.

(4) Ondernemingen van een overeenkomstsluitende Staat, waarvan het kapitaal geheel of ten dele, onmiddellijk of middellijk, in het bezit is van, of wordt beheerst door één of meer inwoners van de andere overeenkomstsluitende Staat, worden in de eerstbedoelde Staat niet aan enige belastingheffing of daarmede verband houdende verplichting onderworpen, die anders of zwaarder is dan de belastingheffing en daarmede verband houdende verplichtingen, waaraan andere, soortgelijke ondernemingen van de eerstbedoelde Staat zijn of kunnen worden onderworpen.

(5) Geen enkele bepaling van dit artikel mag aldus worden uitgelegd dat zij België belet de dividenden uit een aandelenbezit dat wezenlijk verbonden is met een in België gelegen vaste inrichting of vaste basis van een vennootschap die inwoner van Finland is of van een vereniging die haar plaats van werkelijke leiding in Finland heeft en als een rechtspersoon in België belastbaar is aan de roerende voorheffing te onderwerpen.

(6) In dit artikel betekent de uitdrukking "belastingheffing" belastingen van elke soort en benaming.

Artikel 26
REGELING VOOR ONDERLING OVERLEG

[De eerste zin van paragraaf 1 van artikel 26 van deze Overeenkomst wordt VERVANGEN door de eerste zin van paragraaf 1 van artikel 16 van het MLI][Indien een inwoner van een overeenkomstsluitende Staat van oordeel is dat de maatregelen van een overeenkomstsluitende Staat voor hem leiden of zullen leiden tot een belastingheffing die niet in overeenstemming is met deze Overeenkomst, kan hij, onverminderd de rechtsmiddelen waarin de nationale wetgeving van die Staten voorziet, zijn geval voorleggen aan de bevoegde autoriteit van de overeenkomstsluitende Staat waarvan hij inwoner is of, indien zijn geval onder artikel 25, paragraaf 1, valt, aan de overeenkomstsluitende Staat waarvan bij onderdaan is.] Het geval moet worden voorgelegd binnen drie jaren nadat de maatregel die aanleiding geeft tot een belastingheffing die niet in overeenstemming is met de Overeenkomst, voor het eerst te zijner kennis is gebracht.

De volgende eerste zin van paragraaf 1 van artikel 16 van het MLI vervangt de eerste zin van paragraaf 1 van artikel 26 van deze Overeenkomst:

ARTIKEL 16 VAN HET MLI – PROCEDURE VOOR ONDERLING OVERLEG

Indien een persoon van oordeel is dat de maatregelen van een [overeenkomstsluitende Staat] of van beide [overeenkomstsluitende Staten] voor die persoon leiden of zullen leiden tot een belastingheffing die niet in overeenstemming is met de bepalingen van [deze Overeenkomst], kan die persoon, ongeacht de rechtsmiddelen waarin het nationale recht van die [overeenkomstsluitende Staten] voorziet, de zaak voorleggen aan de bevoegde autoriteit van een van beide [overeenkomstsluitende Staten].

(2) De bevoegde autoriteit tracht, indien het bezwaar haar gegrond voorkomt en indien zij niet zelf in staat is tot een bevredigende oplossing te komen, de aangelegenheid in onderlinge overeenstemming met de bevoegde autoriteit van de andere overeenkomstsluitende Staat te regelen, ten einde eerst belastingheffing die niet in overeenstemming is met de Overeenkomst, te vermijden.

De volgende tweede zin van paragraaf 2 van artikel 16 van het MLI is van toepassing op deze Overeenkomst:

ARTIKEL 16 VAN MLI – PROCEDURE VOOR ONDERLING OVERLEG

Elke bereikte overeenstemming wordt uitgevoerd, niettegenstaande de termijnen waarin het nationale recht van de [overeenkomstsluitende Staten] voorziet.

(3) De bevoegde autoriteiten van de overeenkomstsluitende Staten trachten moeilijkheden of twijfelpunten die mochten rijzen met betrekking tot de toepassing van de Overeenkomst, in onderlinge overeenstemming op te lossen.

De volgende eerste zin van paragraaf 3 van artikel 16 van het MLI is van toepassing op deze Overeenkomst:

#### Artikel 16 van het MLI ─ Procedure voor onderling overleg

De bevoegde autoriteiten van de [overeenkomstsluitende Staten] trachten moeilijkheden of twijfelpunten die mochten rijzen met betrekking tot de interpretatie of de toepassing van [de Overeenkomst] in onderlinge overeenstemming op te lossen.

De volgende tweede zin van paragraaf 3 van artikel 16 van het MLI is van toepassing op deze Overeenkomst:

ARTIKEL 16 VAN HET MLI – PROCEDURE VOOR ONDERLING OVERLEG

Zij kunnen ook met elkaar overleg plegen teneinde dubbele belasting te vermijden in gevallen die niet in [de Overeenkomst] geregeld zijn.

(4) De bevoegde autoriteiten van de overeenkomstsluitende Staten plegen overleg omtrent de administratieve maatregelen die voor de uitvoering van de bepalingen van de Overeenkomst nodig zijn en, met name omtrent de bewijsstukken die de inwoners van elke overeenkomstsluitende Staat moeten overleggen om in de andere overeenkomstsluitende Staat de bij deze Overeenkomst vastgestelde belastingvrijstellingen of -verminderingen te genieten. Indien het voor het bereiken van een overeenkomst raadzaam voorkomt mondeling van gedachten te wisselen, van zulke gedachtenwisseling plaats vinden in de schoot van een Commissie die samengesteld is uit vertegenwoordigers van de bevoegde autoriteiten van de overeenkomstsluitende Staten.

Het volgende Deel VI van het MLI is van toepassing op deze Overeenkomst>[1]:

DEEL VI VAN HET MLI (ARBITRAGE)

#### Artikel 19 (Verplichte en bindende arbitrage) van het MLI

1. Wanneer:

a) op grond van [paragraaf 1 van artikel 26 van deze Overeenkomst] een persoon een zaak heeft voorgelegd aan de bevoegde autoriteit van een [overeenkomstsluitende Staat], omdat de maatregelen van een [overeenkomstsluitende Staat] of van beide [overeenkomstsluitende Staten] voor hem tot een belastingheffing geleid hebben die niet in overeenstemming is met de bepalingen van [deze Overeenkomst]; en

b) de bevoegde autoriteiten geen overeenstemming kunnen bereiken om die zaak op te lossen op grond van [paragraaf 2 van artikel 26 van deze Overeenkomst] binnen een termijn van twee jaar die begint te lopen op de aanvangsdatum die, naar gelang de zaak, bedoeld is in paragraaf 8 of 9 [van artikel 19 van het MLI] (tenzij de bevoegde autoriteiten van de [overeenkomstsluitende Staten] nog vóór het verstrijken van die termijn overeenstemming bereikt hebben over een andere termijn voor die zaak en de persoon die de zaak heeft voorgelegd daarvan op de hoogte hebben gebracht),

worden alle onopgeloste kwesties die uit die zaak volgen op schriftelijk verzoek van de persoon aan arbitrage onderworpen op de in dit Deel uiteengezette manier, in overeenstemming met alle regels of procedures waarover de bevoegde autoriteiten van de [overeenkomstsluitende Staten] overeenstemming hebben bereikt overeenkomstig de bepalingen [van paragraaf 10 van artikel 19 van het MLI].

2. Wanneer een bevoegde autoriteit de in paragraaf 1 [van artikel 19 van het MLI] bedoelde procedure voor onderling overleg geschorst heeft, omdat een zaak nog aanhangig is voor een rechterlijke instantie of een administratieve rechtbank met betrekking tot een of meer soortgelijke kwesties, houdt de in alinea b) van paragraaf 1 [van artikel 19 van het MLI] vastgestelde termijn op te lopen, ofwel tot de rechterlijke instantie of de administratieve rechtbank een definitieve uitspraak heeft gedaan, ofwel tot de zaak geschorst of ingetrokken wordt. Ook wanneer een persoon die een zaak heeft voorgelegd en een bevoegde autoriteit overeengekomen zijn om de procedure voor onderling overleg te schorsen, houdt de in alinea b) van paragraaf 1 [van artikel 19 van het MLI] vastgestelde termijn op te lopen tot de schorsing opgeheven wordt.

3. Wanneer beide bevoegde autoriteiten het erover eens zijn dat een rechtsreeks bij de zaak betrokken persoon niet tijdig alle aanvullende materiële inlichtingen heeft verstrekt die door een van beide bevoegde autoriteiten gevraagd werden na aanvang van de in alinea b) van paragraaf 1 [van artikel 19 van het MLI] vastgestelde termijn, wordt de in alinea b) van paragraaf 1 [van artikel 19 van het MLI] vastgestelde termijn verlengd met een tijdsduur die gelijk is aan de termijn die aanvangt op de datum waarop om de inlichtingen werd verzocht en die afloopt op de datum waarop die inlichtingen verstrekt werden.

4) a) De arbitrale uitspraak die met betrekking tot de aan arbitrage onderworpen kwesties genomen wordt, wordt uitgevoerd via het in paragraaf 1 [van artikel 19 van het MLI] bedoelde onderling overleg met betrekking tot die zaak. De arbitrale uitspraak is definitief.

b) De arbitrale uitspraak is bindend voor beide [overeenkomstsluitende Staten], behalve in de volgende gevallen:

i) indien een rechtsreeks bij de zaak betrokken persoon de overeengekomen regeling waardoor de arbitrale uitspraak wordt uitgevoerd niet aanvaardt. In een dergelijk geval, komt de zaak niet in aanmerking voor verder beraad door de bevoegde autoriteiten. De overeengekomen regeling waardoor de arbitrale uitspraak met betrekking tot de zaak wordt uitgevoerd, wordt geacht niet aanvaard te zijn door een rechtsreeks bij de zaak betrokken persoon indien enig persoon die rechtstreeks bij de zaak betrokken is niet binnen 60 dagen na de datum waarop de kennisgeving met betrekking tot de overeengekomen regeling aan de persoon werd toegezonden, alle kwesties die in de overeengekomen regeling tot uitvoering van de arbitrale uitspraak opgelost werden uit het beraad door een rechterlijke instantie of een administratieve rechtbank terugtrekt of anderszins elke nog lopende gerechtelijke of administratieve procedure met betrekking tot dergelijke kwesties beëindigt op een manier die in overeenstemming is met die overeengekomen regeling.

ii) indien een definitieve uitspraak van de rechterlijke instanties van een van de [overeenkomstsluitende Staten] inhoudt dat de arbitrale uitspraak ongeldig is. In een dergelijk geval wordt het in paragraaf 1 [van artikel 19 van het MLI] bedoelde verzoek om arbitrage geacht niet te zijn ingediend en wordt de arbitrageprocedure geacht niet te hebben plaatsgevonden (behalve voor de toepassing van de artikelen 21 (Vertrouwelijkheid van de arbitrageprocedure) en 25 (Kosten van de arbitrageprocedure) [van het MLI]). In een dergelijk geval mag een nieuw verzoek om arbitrage worden ingediend tenzij de bevoegde autoriteiten het erover eens zijn dat een dergelijk nieuw verzoek niet mag worden toegestaan.

iii) indien een rechtstreeks bij de zaak betrokken persoon bij enigerlei rechterlijke instantie of administratieve rechtbank een rechtszaak aanspant met betrekking tot de kwesties die in de overeengekomen regeling tot uitvoering van de arbitrale uitspraak opgelost werden.

5. De bevoegde autoriteit die het aanvankelijke verzoek voor een procedure voor onderling overleg als omschreven in alinea a) van paragraaf 1 [van artikel 19 van het MLI] ontvangen heeft, moet binnen twee kalendermaanden na ontvangst van het verzoek:

a) aan de persoon die de zaak voorgelegd heeft een kennisgeving toezenden ter bevestiging van de ontvangst van het verzoek; en

b) de bevoegde autoriteit van [de] andere [overeenkomstsluitende Staat] een kennisgeving toezenden van dat verzoek, samen met een afschrift van het verzoek.

6. Binnen drie kalendermaanden nadat een bevoegde autoriteit het verzoek voor een procedure voor onderling overleg (of een afschrift daarvan afkomstig van de bevoegde autoriteit van [de] andere [overeenkomstsluitende Staat]) ontvangen heeft:

a) stelt zij de persoon die de zaak voorgelegd heeft en de andere bevoegde autoriteit ervan in kennis dat zij de inlichtingen heeft ontvangen die nodig zijn voor een grondig onderzoek van de zaak; of

b) vraagt zij om aanvullende inlichtingen daartoe aan die persoon.

7. Wanneer een van de bevoegde autoriteiten overeenkomstig alinea b) van paragraaf 6 [van artikel 19 van het MLI] aan de persoon die de zaak voorgelegd heeft aanvullende inlichtingen heeft gevraagd die nodig zijn voor een grondig onderzoek van de zaak, of wanneer beide bevoegde autoriteiten dat hebben gedaan, stelt de bevoegde autoriteit die de aanvullende inlichtingen heeft gevraagd binnen drie kalendermaanden nadat ze die aanvullende inlichtingen van die persoon ontvangen heeft die persoon en de andere bevoegde autoriteit in kennis:

a) ofwel van het feit dat ze de gevraagde inlichtingen ontvangen heeft;

b) ofwel van het feit dat sommige van de gevraagde inlichtingen nog steeds ontbreken.

8. Wanneer geen van beide bevoegde autoriteiten aanvullende inlichtingen heeft gevraagd overeenkomstig alinea b) van paragraaf 6 [van artikel 19 van het MLI], wordt de in paragraaf 1 [van artikel 19 van het MLI] bedoelde aanvangsdatum vastgesteld op de eerste van de volgende data:

a) de datum waarop beide bevoegde autoriteiten aan de persoon die de zaak voorgelegd heeft een kennisgeving hebben gedaan overeenkomstig alinea a) van paragraaf 6 [van artikel 19 van het MLI]; en

b) de datum die drie kalendermaanden later valt dan de datum waarop de kennisgeving overeenkomstig alinea b) van paragraaf 5 [van artikel 19 van het MLI], aan de bevoegde autoriteit van [de] andere [overeenkomstsluitende Staat] werd gedaan.

9. Wanneer er aanvullende inlichtingen werden gevraagd overeenkomstig alinea b) van paragraaf 6 [van artikel 19 van het MLI], wordt de in paragraaf 1 [van artikel 19 van het MLI] bedoelde aanvangsdatum vastgesteld op de eerste van de volgende data:

a) de laatste datum waarop de bevoegde autoriteiten die aanvullende inlichtingen hebben gevraagd aan de persoon die de zaak heeft voorgelegd en aan de andere bevoegde autoriteit een kennisgeving hebben gedaan overeenkomstig alinea a) van paragraaf 7 [van artikel 19 van het MLI]; en

b) de datum drie kalendermaanden nadat beide bevoegde autoriteiten van de persoon die de zaak heeft voorgelegd alle inlichtingen hebben gekregen die door een van beide bevoegde autoriteiten gevraagd werd.

Wanneer evenwel een van beide bevoegde autoriteiten de in alinea a) van paragraaf 7 [van artikel 19 van het MLI] bedoelde kennisgeving toezendt of beide bevoegde autoriteiten dat doen, wordt die kennisgeving behandeld als een verzoek om aanvullende inlichtingen als bedoeld in alinea b) van paragraaf 6 [van artikel 19 van het MLI].

10. De bevoegde autoriteiten van de [overeenkomstsluitende Staten] regelen de wijze van toepassing van de in dit Deel opgenomen bepalingen in onderling overleg overeenkomstig [artikel 26 van deze Overeenkomst], met inbegrip van het minimum aan inlichtingen dat voor elk van de bevoegde autoriteiten noodzakelijk is voor een grondig onderzoek van de zaak. Een dergelijke regeling wordt overeengekomen vóór de datum waarop onopgeloste kwesties van een zaak voor het eerst in aanmerking komen om aan arbitrage onderworpen te worden en kan daarna van tijd tot tijd gewijzigd worden.

12. a) Elke onopgeloste kwestie die voortkomt uit een zaak die via de procedure voor onderling overleg onderzocht werd en die anders onder de toepassing valt van de arbitrageprocedure waarin [het MLI] voorziet, wordt niet aan arbitrage onderworpen wanneer daaromtrent reeds een uitspraak werd gedaan door een rechterlijke instantie of een administratieve rechtbank van een van beide [overeenkomstsluitende Staten];

b) indien, op enig tijdstip nadat een verzoek om arbitrage werd ingediend en voordat het arbitragepanel zijn uitspraak heeft doen toekomen aan de bevoegde autoriteiten van de [overeenkomstsluitende Staten], een rechterlijke instantie of een administratieve rechtbank van een van de [overeenkomstsluitende Staten]een uitspraak ter zake van de kwestie gedaan heeft, wordt de arbitrageprocedure beëindigd.

#### Artikel 20 (Aanstelling van arbiters) van het MLI

1. Behalve voor zover de bevoegde autoriteiten van de [overeenkomstsluitende Staten] onderling andere regels overeenkomen, gelden de paragrafen 2 tot en met 4 [van artikel 20 van het MLI] voor de toepassing van dit Deel.

2. Het aanstellen van de leden van een arbitragepanel gebeurt volgens onderstaande regels:

a) Het arbitragepanel bestaat uit drie afzonderlijke leden met deskundigheid of ervaring op het gebied van internationale belastingaangelegenheden.

b) Binnen de 60 dagen, te rekenen vanaf de datum waarop het verzoek om arbitrage bedoeld in paragraaf 1 van artikel 19 [van het MLI] werd ingediend, stelt elk van de bevoegde autoriteiten één panellid aan. Binnen de 60 dagen na de laatste van deze aanstellingen stellen de twee aldus aangestelde panelleden een derde lid aan, dat optreedt als voorzitter van het arbitragepanel. De voorzitter mag geen onderdaan of inwoner zijn van een van de [overeenkomstsluitende Staten].

c) Elk lid dat aangesteld is voor het arbitragepanel moet, op het tijdstip waarop het zijn aanstelling aanvaardt, onpartijdig zijn en onafhankelijk van de bevoegde autoriteiten, belastingadministraties en ministeries van financiën van de [overeenkomstsluitende Staten] en van alle rechtsreeks bij de zaak betrokken personen (inclusief hun raadgevers), gedurende de hele procedure zijn onpartijdigheid en onafhankelijkheid bewaren en gedurende een redelijke periode volgend op die procedure elk gedrag vermijden dat afbreuk kan doen aan de schijn van onpartijdigheid en onafhankelijkheid van de arbiters met betrekking tot de procedure.

3. Indien de bevoegde autoriteit van een [overeenkomstsluitende Staat] nalaat om een lid van het arbitragepanel aan te stellen op de manier en binnen de termijnen zoals bepaald in paragraaf 2 [van artikel 20 van het MLI] of zoals overeengekomen door de bevoegde autoriteiten van de [overeenkomstsluitende Staten], wordt er voor die bevoegde autoriteit een lid aangesteld door de functionaris met de hoogste rang van het Centre for Tax Policy and Administration van de Organisatie voor Economische Samenwerking en Ontwikkeling (OESO) die van geen van de [overeenkomstsluitende Staten] onderdaan is.

4. Indien de twee oorspronkelijke leden van het arbitragepanel nalaten om de voorzitter aan te stellen op de manier en binnen de termijnen zoals bepaald in paragraaf 2 [van artikel 20 van het MLI] of zoals overeengekomen door de bevoegde autoriteiten van de [overeenkomstsluitende Staten], wordt de voorzitter aangesteld door de functionaris met de hoogste rang van het Centre for Tax Policy and Administration van de Organisatie voor Economische Samenwerking en Ontwikkeling (OESO) die van geen van de [overeenkomstsluitende Staten] onderdaan is.

#### Artikel 21 (Vertrouwelijkheid van de arbitrageprocedure) van het MLI

1. Uitsluitend voor de toepassing van de bepalingen van dit Deel, van de bepalingen van [deze Overeenkomst], en van de nationale wetgeving van de [overeenkomstsluitende Staten] die betrekking hebben op de uitwisseling van inlichtingen, vertrouwelijkheid en administratieve bijstand, worden leden van het arbitragepanel en maximaal drie medewerkers per lid (en aangezochte arbiters, evenwel uitsluitend voor zover nodig is om na te gaan of ze kunnen voldoen aan de vereisten die aan arbiters worden gesteld) beschouwd als personen of autoriteiten aan wie inlichtingen mogen worden kenbaar gemaakt. Inlichtingen die het arbitragepanel of aangezochte arbiters ontvangen en inlichtingen die de bevoegde autoriteiten ontvangen van het arbitragepanel, worden geacht inlichtingen te zijn die worden uitgewisseld overeenkomstig de bepalingen van [deze Overeenkomst] die betrekking hebben op de uitwisseling van inlichtingen en administratieve bijstand.

2. De bevoegde autoriteiten van de [overeenkomstsluitende Staten] garanderen dat leden van het arbitragepanel en hun medewerkers, alvorens op te treden in een arbitrageprocedure, er schriftelijk mee instemmen om alle inlichtingen in verband met die arbitrageprocedure te zullen behandelen in overeenstemming met de verplichtingen inzake vertrouwelijkheid en geheimhouding die zijn vastgelegd in de bepalingen van [deze Overeenkomst] die betrekking hebben op de uitwisseling van inlichtingen en administratieve bijstand en overeenkomstig de van toepassing zijnde wetten van de [overeenkomstsluitende Staten].

#### Artikel 22 (Oplossing van een zaak voordat de arbitrage afgesloten is) van het MLI

Voor de toepassing van dit Deel en van de bepalingen van [deze Overeenkomst] die betrekking hebben op het oplossen van zaken door onderling overleg, worden de procedure voor onderling overleg en de arbitrageprocedure met betrekking tot een zaak beëindigd, wanneer op enig tijdstip nadat een verzoek om arbitrage werd ingediend en voordat het arbitragepanel zijn uitspraak aan de bevoegde autoriteiten van de [overeenkomstsluitende Staten] heeft doen toekomen:

a) de bevoegde autoriteiten van de [overeenkomstsluitende Staten] onderling overeenstemming bereiken over een oplossing voor de zaak; of

b) de persoon die de zaak heeft voorgelegd het verzoek om arbitrage of het verzoek om een procedure voor onderling overleg intrekt.

#### Artikel 23 (Methode van arbitrage) van het MLI

1. Behalve voor zover de bevoegde autoriteiten van de [overeenkomstsluitende Staten] onderling andere regels overeenkomen, gelden de volgende regels voor een arbitrageprocedure overeenkomstig dit Deel:

a) nadat een zaak aan arbitrage is onderworpen, legt de bevoegde autoriteit van elk van de [overeenkomstsluitende Staten], uiterlijk op een in overleg vastgestelde datum, aan het arbitragepanel een voorgestelde oplossing voor, waarin alle onopgeloste kwesties van de zaak behandeld worden (rekening houdend met alle overeenkomsten die voordien rond die zaak werden bereikt tussen de bevoegde autoriteiten van de [overeenkomstsluitende Staten]). De voorgestelde oplossing blijft beperkt tot een vermelding van de specifieke geldbedragen uitgedrukt in munteenheden (bijvoorbeeld van inkomsten of uitgaven) of, waar gespecificeerd, van het maximale tarief van de belasting die overeenkomstig [deze Overeenkomst] werd geheven, voor elke aanpassing of soortgelijke kwestie bij de zaak. In een zaak waarin de bevoegde autoriteiten van de [overeenkomstsluitende Staten] er niet in geslaagd zijn om tot overeenstemming te komen over een kwestie met betrekking tot de toepassingsvoorwaarden van een bepaling van [deze Overeenkomst] (hierna "drempelkwestie" genoemd) ─ zoals de vraag of een natuurlijke persoon al dan niet een inwoner is, of de vraag of er al dan niet sprake is van een vaste inrichting ─ mogen de bevoegde autoriteiten andere voorgestelde oplossingen voorleggen met betrekking tot kwesties waarvan de beslissing afhangt van de oplossing van dergelijke drempelkwesties.

b) De bevoegde autoriteit van elk van de [overeenkomstsluitende Staten] mag het arbitragepanel ook een ondersteunende standpuntnota ter overweging voorleggen. Elke bevoegde autoriteit die een voorgestelde oplossing of een ondersteunende standpuntnota voorlegt, bezorgt de andere bevoegde autoriteit een afschrift daarvan uiterlijk op de datum waarop de voorgestelde oplossing en het ondersteunende standpuntnota moesten worden voorgelegd. Elke bevoegde autoriteit mag het arbitragepanel uiterlijk op een in overleg vastgestelde datum ook een memorie van antwoord voorleggen in antwoord op de voorgestelde oplossing en de ondersteunende standpuntennota die door de andere bevoegde autoriteit werd voorgelegd. Van elke memorie van antwoord wordt een afschrift toegezonden aan de andere bevoegde autoriteit uiterlijk op de datum waarop de memorie van antwoord voorgelegd moest worden.

c) Het arbitragepanel kiest als haar uitspraak een van de voorgestelde oplossingen voor de zaak, die door de bevoegde autoriteiten voor elke kwestie en voor alle drempelkwesties werden voorgelegd, zonder een redenering achter of andere uitleg van de uitspraak bij te voegen. De arbitrale uitspraak wordt aangenomen bij gewone meerderheid van de panelleden. Het arbitragepanel bezorgt haar uitspraak schriftelijk aan de bevoegde autoriteiten van de [overeenkomstsluitende Staten]. De arbitrale uitspraak heeft geen precedentwerking.

5. Alvorens met de arbitrageprocedure te beginnen, vergewissen de bevoegde autoriteiten van de [overeenkomstsluitende Staten] zich ervan dat elk van de personen die de zaak hebben voorgelegd, met inbegrip van hun raadgevers, zich schriftelijk akkoord verklaren om geen enkele inlichting die ze in de loop van de arbitrageprocedure hetzij van de bevoegde autoriteiten, hetzij van het arbitragepanel hebben ontvangen, kenbaar te maken aan elke andere persoon. De procedure voor onderling overleg waarin [deze Overeenkomst] voorziet en de arbitrageprocedure waarin dit Deel voorziet, worden met betrekking tot de zaak beëindigd wanneer een persoon die de zaak heeft voorgelegd, of een van diens raadgevers, dat akkoord materieel niet nakomt op enig tijdstip nadat een verzoek om arbitrage werd ingediend en voordat het arbitragepanel zijn uitspraak heeft doen toekomen aan de bevoegde autoriteiten van de [overeenkomstsluitende Staten].

#### Artikel 25 (Kosten van de arbitrageprocedure) van het MLI

In een arbitrageprocedure op grond van dit Deel, worden de vergoedingen en onkosten van de leden van het arbitragepanel, alsmede alle kosten die de [overeenkomstsluitende Staten] in verband met de arbitrageprocedure hebben gemaakt, gedragen door de [overeenkomstsluitende Staten] op een manier die de bevoegde autoriteiten van de [overeenkomstsluitende Staten] in onderlinge overeenstemming vaststellen. Indien een dergelijke overeenstemming ontbreekt, draagt [elke overeenkomstsluitende Staat] zijn eigen kosten en die van zijn aangesteld panellid. De kosten van de voorzitter van het arbitragepanel en de andere kosten in verband met het voeren van de arbitrageprocedure worden gelijkelijk door de [overeenkomstsluitende Staten] gedragen.

Paragrafen 2 en 3 van artikel 26 (Compatibiliteit) van het MLI

2. Geen enkele onopgeloste kwestie die volgt uit een zaak die door middel van de procedure voor onderling overleg onderzocht werd en die anders binnen de reikwijdte zou vallen van de arbitrageprocedure waarin dit Deel voorziet, wordt aan arbitrage onderworpen wanneer de kwestie binnen de reikwijdte valt van een zaak waarvoor er eerder al een arbitragepanel of een gelijksoortig orgaan opgericht werd in overeenstemming met een multilaterale of bilaterale overeenkomst die voorziet in verplichte en bindende arbitrage voor onopgeloste kwesties die volgen uit een zaak die door middel van de procedure voor onderling overleg onderzocht werd.

3. De bepalingen van dit Deel doen in geen enkel opzicht afbreuk aan het naleven van verdergaande verplichtingen inzake arbitrage met betrekking tot onopgeloste kwesties die ontstaan binnen de context van een procedure voor onderling overleg en die voortvloeien uit andere overeenkomsten waarbij de [overeenkomstsluitende Staten] partij zijn of zullen worden.

Alinea a) van paragraaf 2 van artikel 28 van het MLI

Ingevolge alinea a) van paragraaf 2 van artikel 28 van het MLI maakt Finland de volgende voorbehouden met betrekking tot de reikwijdte van gevallen die op grond van de bepalingen van Deel VI van het MLI in aanmerking komen voor arbitrage:

1. Finland behoudt zich het recht voor om van de reikwijdte van [Deel VI van het MLI] uit te sluiten, gevallen aangaande de toepassing van nationale anti-ontwijkingsregels van elke [overeenkomstsluitende Staat]. Te dien einde bevatten de nationale anti-ontwijkingsregels van Finland "Act on Assessment Procedure" ("verotusmenettelystä annettu laki" (1558/1995)) sectie 27 - 30, "Act on the Taxation of Business Profits and Income from Professional Activities" ("elinkeinotulon verottamisesta annettu laki" (360/1968)) sectie 6 a, subsectie 9 [2] en sectie 52 h en "Act on the Taxation of Shareholders in Controlled Foreign Companies" ("ulkomaisten väliyhteisöjen osakkaiden verotuksesta annetun laki" (1217/1994))". Alle latere bepalingen welke die anti-ontwijkingsregels vervangen, wijzigen of bijwerken worden ook begrepen onder dit voorbehoud te vallen. Finland stelt de depositaris in kennis van alle dergelijke latere bepalingen.

2. Finland behoudt zich het recht voor om van de reikwijdte van [Deel VI van het MLI] uit te sluiten, gevallen waarin sprake is van een handelwijze waarvoor de belastingplichtige of een persoon die voor de belastingplichtige optreedt, door een rechterlijke instantie schuldig werd bevonden aan belastingfraude of een andere strafrechtelijke belasting gerelateerde inbreuk in een van beide overeenkomstsluitende Staten. Voor de toepassing hiervan bevatten de nationale regels van Finland het Strafwetboek ("rikoslaki" (39/1889)), hoofdstuk 29 sectie 1-4. Alle latere bepalingen welke die regels vervangen, wijzigen of bijwerken worden ook begrepen onder dit voorbehoud te vallen. Finland stelt de depositaris in kennis van alle dergelijke latere bepalingen.

3. Finland behoudt zich het recht voor om van de reikwijdte van [Deel VI van het MLI] uit te sluiten, gevallen betreffende inkomsten- of vermogensbestanddelen waarbij er geen dubbele belasting is. Dubbele belasting betekent dat beide [overeenkomstsluitende Staten] belasting hebben geheven van hetzelfde belastbaar inkomen of vermogen, hetgeen aanleiding geeft tot een aanvullende fiscale last, een verhoging van belastingschulden of tot het opheffen of verminderen van verliezen, waarvan gebruik zou kunnen gemaakt worden voor het verrekenen met belastbare winst.

4. Finland behoudt zich het recht voor om van de reikwijdte van [Deel VI van het MLI] uit te sluiten:

met betrekking tot belastingen geheven aan de bron, op bedragen die zijn betaald of toegekend aan niet-inwoners, gevallen waarbij het belastbare feit dat aanleiding geeft tot die belastingen zich voordoen voor de referentiedatum;
-met betrekking tot alle andere belastingen, gevallen waarbij belastingen worden geheven ter zake van belastbare tijdperken die aanvangen voor de referentiedatum.

Voor de toepassing van dit voorbehoud is "de referentiedatum" de laatste van:

i) de datum van toepassing van [het MLI] in beide [overeenkomstsluitende Staten] met betrekking tot dergelijke belastingen;

ii) de eerste dag van januari van het kalenderjaar dat onmiddellijk volgt op het verstrijken van een termijn van zes kalendermaanden die aanvangt op de datum waarop de depositaris de laatste definitieve intrekking van het voorbehoud of de kennisgeving meedeelt waardoor [Deel VI van het MLI] (Arbitrage) tussen beide [overeenkomstsluitende Staten] van toepassing wordt;

iii) wanneer het gaat om een geval dat potentieel in aanmerking zou komen voor arbitrage ten gevolge van de intrekking, nadat [Deel VI van het MLI] tussen beide [overeenkomstsluitende Staten] van toepassing werd, van het voorbehoud van een [overeenkomstsluitende Staat] dat ingevolge artikel 28(2) of artikel 19(12) [van het MLI] werd gemaakt, de eerste dag van januari van het kalenderjaar dat onmiddellijk volgt op het verstrijken van een termijn van zes kalendermaanden die aanvangt op de datum waarop de depositaris de intrekking van het voorbehoud meedeelt.

5. Finland behoudt zich het recht voor om van de reikwijdte van [Deel VI van het MLI] uit te sluiten, alle gevallen waarbij een aanvraag werd ingediend ingevolge het Verdrag ter afschaffing van dubbele belasting in geval van winstcorrecties tussen verbonden ondernemingen (90/436/EEG) – zoals gewijzigd, of ingevolge andere instrumenten die door de lidstaten van de Europese Unie zijn overeengekomen of ingevolge nationale regels die dergelijke instrumenten implementeren.

Artikel 27
UITWISSELING VAN INLICHTINGEN

(1) De bevoegde autoriteiten van de overeenkomstsluitende Staten wisselen de inlichtingen uit die naar verwachting relevant zullen zijn voor de uitvoering van de bepalingen van deze Overeenkomst of voor de toepassing of de tenuitvoerlegging van de nationale wetgeving met betrekking tot belastingen van elke soort en benaming die worden geheven door of ten behoeve van de overeenkomstsluitende Staten of de plaatselijke gemeenschappen van Finland, voor zover de belastingheffing waarin die nationale wetgeving voorziet niet in strijd is met de Overeenkomst. De uitwisseling van inlichtingen wordt niet beerkt door de artikelen 1 en 2.

(2) De door een overeenkomstsluitende Staat ingevolge paragraaf 1 verkregen inlichtingen worden op dezelfde wijze geheim gehouden als inlichtingen die onder de nationale wetgeving van die Staat zijn verkregen en worden alleen ter kennis gebracht van personen of autoriteiten (daaronder begrepen rechterlijke instanties en administratieve lichamen) die betrokken zijn bij de vestiging of invordering van de in paragraaf 1 bedoelde belastingen, bij de tenuitvoerlegging of vervolging ter zake van die belastingen, bij de beslissing in beroepszaken die betrekking hebben op die belastingen, of bij het toezicht daarop. Deze personen of autoriteiten gebruiken die inlichtingen slechts voor die doeleinden. Zij mogen van deze inlichtingen melding maken tijdens openbare rechtszittingen of in rechterlijke beslissingen. Niettegenstaande het voorafgaande, mogen de inlichtingen die door een overeenkomstsluitende Staat zijn ontvangen voor andere doeleinden worden gebruikt indien ze overeenkomstig de wetgeving van beide Staten voor die andere doeleinden mogen worden gebruikt en indien de bevoegde autoriteit van de Staat die de inlichtingen verstrekt, de toestemming geeft voor dat gebruik.

(3) In geen geval mogen de bepalingen van de paragrafen 1 en 2 aldus worden uitgelegd dat zij een overeenkomstsluitende Staat de verplichting opleggen :

(a) administratieve maatregelen te nemen die afwijken van de wetgeving en de administratieve praktijk van die of van de andere overeenkomstsluitende Staat;

(b) inlichtingen te verstrekken die niet verkrijgbaar zijn volgens de wetgeving of in de normale gang van de administratieve werkzaamheden van die of van de andere overeenkomstsluitende Staat;

(c) inlichtingen te verstrekken die een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een handelswerkwijze zouden onthullen, dan wel inlichtingen waarvan het verstrekken in strijd zou zijn met de openbare orde.

(4) Wanneer op basis van de bepalingen van dit artikel door een overeenkomstsluitende Staat om inlichtingen is verzocht, gebruikt de andere overeenkomstsluitende Staat de middelen waarover hij beschikt om de gevraagde inlichtingen te verkrijgen, zelfs al heeft die andere Staat die inlichtingen niet nodig voor zijn eigen belastingdoeleinden. De verplichting die in de vorige zin is vervat, is onderworpen aan de beperkingen waarin paragraaf 3 van dit artikel voorziet, maar die beperkingen mogen in geen geval aldus worden uitgelegd dat ze een overeenkomstsluitende Staat toestaan het verstrekken van inlichtingen te weigeren enkel omdat die Staat geen binnenlands belang heeft bij die inlichtingen.

(5) In geen geval mogen de bepalingen van paragraaf 3 van dit artikel aldus worden uitgelegd dat ze een overeenkomstsluitende Staat toestaan om het verstrekken van inlichtingen te weigeren enkel en alleen omdat de inlichtingen in het bezit zijn van een bank, een andere financiële instelling, een trust, een stichting, een gevolmachtigde of een persoon die werkzaam is in de hoedanigheid van een vertegenwoordiger of een vertrouwenspersoon of omdat de inlichtingen betrekking hebben op eigendomsbelangen in een persoon. Teneinde zulke inlichtingen te verkrijgen heeft de belastingadministratie van de aangezochte overeenkomstsluitende Staat de bevoegdheid om te vragen inlichtingen bekend te maken en om een onderzoek en verhoren in te stellen, niettegenstaande andersluidende bepalingen in de binnenlandse belastingwetgeving van die Staat

Artikel 28
INVORDERINGSBIJSTAND

(1) De overeenkomstsluitende Staten verlenen elkaar hulp en bijstand voor de betekening en de invordering van de in artikel 2 vermelde belastingen, voorheffingen, verhogingen en opcentiemen op die belastingen, alsmede interest, kosten en boeten van niet-strafrechtelijke aard.

(2) Op verzoek van een overeenkomstsluitende Staat zorgt de andere overeenkomstsluitende Staat, overeenkomstig de wettelijke en reglementaire beschikkingen die voor de betekening en de invordering van zijn eigen belastingen van toepassing zijn, voor de betekening en de invordering van de in paragraaf 1 vermelde belastingvorderingen die in de verzoekende Staat eisbaar zijn. Die vorderingen genieten geen enkel voorrecht in de aangezochte Staat en die Staat is niet gehouden met het oog op de tenuitvoerlegging middelen aan te wenden die niet toegelaten zijn door de wettelijke en reglementaire beschikkingen van de verzoekende Staat.

(3) De overeenkomstsluitende Staat die volgens de bepalingen van paragraaf 2 een invordering doet, is tegenover de verzoekende Staat verantwoordelijk voor de aldus ingevorderde bedragen.

(4) Met betrekking tot de in paragraaf 1 vermelde belastingvorderingen waartegen beroep openstaat mag een overeenkomstsluitende Staat ter vrijwaring van zijn rechten, de andere overeenkomstsluitende Staat verzoeken conservatoire maatregelen te nemen waarin de wetgeving van die andere Staat voorziet. De bepalingen van paragraaf 2 zijn mutatis mutandis op die maatregelen van toepassing.

(5) De bepalingen van artikel 27, paragraaf 1, zijn mede van toepassing op elke inlichting die op grond van dit artikel ter kennis van de aangezochte Staat wordt gebracht.

(6) De bevoegde autoriteiten van de overeenkomstsluitende Staten bepalen in onderlinge overeenstemming de wijze van uitvoering van dit artikel.

Artikel 29
DIVERSE BEPALINGEN

(1) De bepalingen van deze Overeenkomst tasten in geen enkel opzicht de fiscale voorrechten aan die diplomatieke en consulaire ambtenaren en beambten ontlenen aan de algemene regelen van het volkenrecht of aan bepalingen van bijzondere overeenkomsten.

(2) Voor de toepassing van deze Overeenkomst worden de leden van een diplomatieke of consulaire vertegenwoordiging van een overeenkomstsluitende Staat, die in de andere overeenkomstsluitende Staat of in een derde Staat geaccrediteerd zijn en die de nationaliteit van de Zendstaat bezitten, geacht inwoner te zijn van de Zendstaat indien zij aldaar aan dezelfde verplichtingen inzake belastingen naar het inkomen en naar het vermogen zijn onderworpen als de inwoners van die Staat.

(3) Deze Overeenkomst is niet van toepassing op internationale organisaties, hun organen of hun ambtenaren, noch op personen die lid zijn van een diplomatieke of consulaire vertegenwoordiging van een derde Staat, indien deze in een overeenkomstsluitende Staat aanwezig zijn en in geen van de overeenkomstsluitende Staten, inzake belastingen naar het inkomen en naar het vermogen aan dezelfde verplichtingen zijn onderworpen als inwoners van die Staat.

(4) De bevoegde autoriteiten van de overeenkomstsluitende Staten stellen zich, met het oog op de toepassing van deze Overeenkomst, rechtstreeks met elkaar in verbinding.

De volgende paragraaf 1 van artikel 7 van het MLI is van toepassing en heeft voorrang op de bepalingen van deze Overeenkomst:

ARTIKEL 7 VAN HET MLI – VOORKOMEN VAN VERDRAGSMISBRUIK

(Bepaling van het criterium van de voornaamste doelen)

Niettegenstaande enige bepaling van [deze Overeenkomst], wordt een voordeel waarin [deze Overeenkomst] voorziet niet toegekend met betrekking tot een inkomens- of vermogensbestanddeel wanneer er, rekening houdend met alle relevante feiten en omstandigheden, redelijkerwijs kan worden geconcludeerd dat het verkrijgen van dat voordeel een van de voornaamste doelen was van een constructie of transactie die direct of indirect tot dat voordeel geleid heeft, tenzij vastgesteld wordt dat het toekennen van dat voordeel in die omstandigheden in overeenstemming zou zijn met het voorwerp en het doel van de desbetreffende bepalingen van [deze Overeenkomst].

Artikel 30
TERRITORIALE UITBREIDING

(1) Deze Overeenkomst kan in haar geheel of met alle noodzakelijke wijzigingen worden uitgebreid tot het Graafschap Aland met betrekking tot de gemeentebelasting. Zodanige uitbreiding treedt in werking met ingang van de datum, met de wijzigingen en op de voorwaarden, daaronder begrepen de voorwaarden met betrekking tot de beëindiging, welke tussen de overeenkomstsluitende Staten bij diplomatieke notawisseling worden vastgelegd.

(2) Tenzij door beide overeenkomstsluitende Staten anders is overeengekomen, zal de opzegging van de Overeenkomst door een van hen op grond van artikel 32, op de in dat artikel bepaalde voorwaarden een einde maken aan de toepassing van de Overeenkomst ten opzichte van het Graafschap Aland, ook mét betrekking tot de gemeentebelasting.

Artikel 31
INWERKINGTREDING

(1) De Regeringen van de overeenkomstsluitende Staten zullen elkaar mededelen dat aan alle grondwettelijke voorschriften met betrekking tot de inwerkingtreding van deze Overeenkomst is voldaan.

(2) De Overeenkomst zal in werking treden op de dertigste dag na de datum waarop de laatste van de in paragraaf 1 vermelde mededelingen is gedaan en haar bepalingen zullen toepassing vinden :

(a) met betrekking tot bij de bron verschuldigde belastingen, op inkomsten die zijn toegekend of betaalbaar gesteld op of na 1 januari van het kalenderjaar dat onmiddellijk volgt op het jaar waarin de Overeenkomst in werking treedt ;

(b) met betrekking tot andere belastingen geheven naar het inkomen en naar het vermogen, op belastingen verschuldigd voor elk aanslagjaar dat aanvangt op of na 1 januari van het kalenderjaar dat onmiddellijk volgt op het jaar waarin de Overeenkomst in werking treedt.

(3) De Overeenkomst tussen België en Finland tot voorkoming van dubbele belasting en tot regeling van zekere andere vraagstukken inzake belastingen op de inkomsten en op het vermogen, ondertekend te Helsinki op 11 februari 1954 en het slotprotocol, zoals gewijzigd bij het aanvullend akkoord ondertekend te Brussel op 21 mei 1970, zal ophouden uitwerking te hebben op het ogenblik dat de bepalingen van deze Overeenkomst in werking zullen zijn getreden.

(4) De Overeenkomst tussen België en Finland ter vermijding van de dubbele belasting van de inkomsten van scheepvaartondernemingen, ondertekend te Brussel op 19 februari 1929, zal geen uitwerking hebben voor de perioden waarvoor artikel 8 van deze Overeenkomst uitwerking heeft .

Artikel 32
BEËINDIGING

Deze Overeenkomst blijft in werking tot ze door één van de overeenkomstsluitende Staten wordt beëindigd. Elke overeenkomstsluitende Staat kan de Overeenkomst langs diplomatieke weg opzeggen door ten minste zes maanden vóór het einde van enig kalenderjaar na het vijfde jaar volgend op de datum van inwerkingtreding van de Overeenkomst een kennisgeving van beëindiging te zenden. In dat geval houdt de Overeenkomst op uitwerking te hebben :

(a) met betrekking tot bronbelastingen, op inkomsten die zijn toegekend of betaalbaar gesteld op of na 1 januari van het kalenderjaar dat onmiddellijk volgt op het jaar waarin de opzegging is gedaan ;

(b) met betrekking tot andere belastingen geheven naar het inkomen, en naar het vermogen, op belastingen verschuldigd voor elk aanslagjaar dat aanvangt op of na 1 januari van het kalenderjaar dat onmiddellijk volgt op het jaar waarin de opzegging is gedaan.

Ten blijke waarvan de ondergetekenden, daartoe behoorlijk gevolmachtigd door hun onderscheiden Regeringen, deze Overeenkomst hebben ondertekend.

Gedaan te Brussel, op 18 mei 1976, in tweevoud, in de Engelse taal.

Voor de Regering van het Koninkrijk België :

Renaat Van Elslande

Voor de Regering van de Republiek Finland :

Ake Wihtol

PROTOCOL

Artikel 10 van de Overeenkomst, zoals gewijzigd door het aanvullend akkoord, ondertekend te Brussel op 13 maart 1991, vloeit voort uit de belastingwetten welke op die datum in beide overeenkomstsluitende Staten van kracht zijn. Die wetten stellen de overeenkomstsluitende Staten niet in staat een regeling uit te werken die dividenden welke worden betaald door een vennootschap die inwoner is van een overeenkomstsluitende Staat aan een inwoner van de andere overeenkomstsluitende Staat op een meer geïntegreerde wijze behandelt.

Er is echter overeengekomen dat wanneer Finland in een dubbelbelastingverdrag gesloten tussen Finland en een derde Staat, zijnde een Europese Staat, akkoord gaat om, zonder wederkerigheids-voorwaarde de Finse compenserende belasting ("compensatory tax") terug te storten ter zake van dividenden die door een vennootschap die inwoner is van Finland aan inwoners van die derde Staat zijn betaald, de Regering van Finland onmiddellijk de Regering van België zal inlichten en met de Regering van België onderhandelingen zal aanvatten ten einde de inwoners van België op dezelfde wijze te behandelen als de voor inwoners van de derde Staat.

[1] Ingevolge paragraaf 1 van artikel 36 van het MLI zijn de bepalingen van deel VI (Arbitrage) van het MLI van toepassing op deze Overeenkomst

met betrekking tot zaken die aan de bevoegde autoriteit van een [overeenkomstsluitende Staat] worden voorgelegd op of na 1 oktober 2019, en met betrekking tot zaken die aan de bevoegde autoriteit van een overeenkomstsluitende Staat worden voorgelegd vóór 1 oktober 2019, op de datum waarop beide overeenkomstsluitende Staten de Secretaris-generaal van de OESO kennis gegeven hebben van het feit dat zij onderling overeenstemming hebben bereikt overeenkomstig paragraaf 10 van artikel 19 (Verplichte en bindende arbitrage) van het MLI en met die kennisgeving ook inlichtingen verstrekt hebben over de datum of data waarop die zaken volgens de bereikte onderlinge overeenstemming beschouwd worden als zijnde voorgelegd aan de bevoegde autoriteit van een overeenkomstsluitende Staat (zoals omschreven in alinea a) van paragraaf 1 van artikel 19 (Verplichte en bindende arbitrage) van het MLI).

[2] Verwijzing die werd gecorrigeerd : van sectie 6 a subsectie 8, waarnaar werd verwezen in het MLI-standpunt dat werd voorgelegd op 25 februari 2019, in sectie 6 subsectie 9. De depositaris werd op 25 februari 2019 in kennis gesteld van deze correctie.

NL
