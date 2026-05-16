---
title: IFRS-12 — Informatieverschaffing over belangen in andere entiteiten
tags:
- '1.5'
- ifrs
- ifrs
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IFRS
standaard_nummer: '12'
status: beschikbaar
bijgewerkt: 13.08.2023
bron: EUR-Lex CELEX 32023R1803
chunk:
  level: 2
  type: Sectie
  sub_strategy: null
provenance:
  inputs:
  - id: resources/raw/wetteksten/EU-Verordening-2023-1803-IFRS-Geconsolideerd.pdf
    sha256: 20512af4119d8dc42de857d3ccca87d9e0dac728b0c79f0eb047ca16e9694132
    version: 13.08.2023
    pages: 723-740
  tooling:
    pipeline: tools/etl/split_ifrs_verordening.py
    pipeline_version: '1.0'
    model: null
    prompt_version: null
  generated_at: '2026-05-16T19:10:06Z'
  stale: false
  stale_reason: null
  trust:
    status: trusted
    confirmed_at: '2026-05-16T20:31:37Z'
    confirmed_by: subagent-qa-2026-05-16
    rationale: >-
      QA-pass 2026-05-16: gestructureerde body met heading-detectie op
      DOEL/TOEPASSINGSGEBIED/DEFINITIES + paragraph-numbers; inhoud is volledig en
      RAG-bruikbaar. Kolomwrap-splits ('instru menten', 'voorwaar den') zijn inherent aan de
      bron-PDF (EUR-Lex CELEX 32023R1803 kolommen), niet aan de ETL — analoog aan
      EU-IFRS-verordening-1606-2002.md die trusted is.
    caveat: >-
      pymupdf-heading-detector promoot incidenteel paragraph-nummers en korte regels (zoals '##
      38A', '## B12', '## (X)', '## Ifrs 9;') tot ## — over-segmentation maar geen
      content-verlies; chunker handelt dit af. Tweetalig is geen issue (NL-only
      EUR-Lex-extractie).
    layer1: null
    layer2: null
---

## International Financial Reporting Standard 12

Informatieverschaffing over belangen in andere entiteiten

## Doel

1 Deze IFRS heeft ten doel een entiteit te verplichten informatie te verschaffen die gebruikers van haar jaarrekening in staat stellen het volgende te beoordelen:
(a) de aard van en de risico’s die verband houden met haar belangen in andere entiteiten; en
(b) de gevolgen van die belangen voor haar financiële positie, financiële prestaties en kasstromen. Verwezenlijking van het doel 2 Om het in alinea 1 beschreven doel te verwezenlijken, moet een entiteit de volgende informatie verschaffen:
(a) de belangrijke oordelen en veronderstellingen waarvan zij is uitgegaan bij de bepaling:
(i) van de aard van haar belang in een andere entiteit of overeenkomst;
(ii) van het type gezamenlijke overeenkomst waarin zij een belang heeft (alinea’s 7 tot en met 9);
(iii) indien toepasselijk, of zij aan de definitie van een beleggingsentiteit voldoet (alinea 9A); en
(b) informatie over haar belangen in:
(i) dochterondernemingen (alinea’s 10 tot en met 19);
(ii) gezamenlijke overeenkomsten en geassocieerde deelnemingen (alinea’s 20 tot en met 23); en
(iii) gestructureerde entiteiten waarover geen zeggenschap wordt uitgeoefend door de entiteit (niet-geconsoli deerde gestructureerde entiteiten) (alinea’s 24 tot en met 31). 3 Indien de informatie die op grond van deze IFRS en andere IFRSs moet worden verstrekt, niet volstaat om het in alinea 1 beschreven doel te verwezenlijken, moet een entiteit alle aanvullende informatie verschaffen die nood zakelijk is om dat doel te realiseren. 4 Een entiteit moet beoordelen hoever in detail moet worden gegaan om aan de informatiedoelstelling te voldoen en hoeveel nadruk op elk van de eisen van deze IFRS moet worden gelegd. Zij moet de informatie zodanig samen voegen of opsplitsen dat nuttige informatie niet wordt versluierd doordat deze is opgenomen te midden van een grote hoeveelheid onbeduidende details, dan wel doordat posten zijn samengevoegd die verschillende kenmerken hebben (zie de alinea’s B2 tot en met B6).

## Toepassingsgebied

5 Deze IFRS moet worden toegepast door een entiteit die een belang heeft in:
(a) dochterondernemingen;
(b) gezamenlijke overeenkomsten (d.w.z. gezamenlijke bedrijfsactiviteiten of joint ventures);
(c) geassocieerde deelnemingen;
(d) niet-geconsolideerde gestructureerde entiteiten.

5A Behoudens het bepaalde in alinea B17 zijn de vereisten in deze IFRS van toepassing op de in lid 5 bedoelde belangen van een entiteit die zijn geclassificeerd (of opgenomen in een groep activa die wordt afgestoten) als aangehouden voor verkoop of als beëindigde bedrijfsactiviteiten in overeenstemming met IFRS 5 Vaste activa aangehouden voor verkoop en beëindigde bedrijfsactiviteiten . 6 Deze IFRS is niet van toepassing op:
(a) regelingen inzake vergoedingen na uitdiensttreding of andere regelingen inzake langetermijnpersoneelsbelonin gen waarop IAS 19 Personeelsbeloningen van toepassing is;
(b) de enkelvoudige jaarrekening van een entiteit, waarop IAS 27 Enkelvoudige jaarrekening van toepassing is. In afwijking hiervan:
(i) moet een entiteit, indien zij belangen heeft in niet-geconsolideerde gestructureerde entiteiten en alleen een enkelvoudige jaarrekening opstelt, bij de opstelling van deze enkelvoudige jaarrekening de eisen van de alinea’s 24 tot en met 31 toepassen;
(ii) moet een beleggingsentiteit die een jaarrekening opstelt waarin al haar dochterondernemingen overeen komstig alinea 31 van IFRS 10 zijn gewaardeerd tegen reële waarde met verwerking van waardeverande ringen in de winst- en verliesrekening, de door deze IFRS vereiste informatie over beleggingsentiteiten presenteren;
(c) een door een entiteit aangehouden belang dat deelneemt in maar geen gezamenlijke zeggenschap heeft over een gezamenlijke overeenkomst, tenzij het belang resulteert in invloed van betekenis in de overeenkomst of een belang in een gestructureerde entiteit is;
(d) een belang in een andere entiteit dat administratief is verwerkt in overeenstemming met IFRS 9 Financiële instrumenten. Een entiteit moet deze IFRS echter toepassen:
(i) wanneer het gaat om een belang in een geassocieerde deelneming of een joint venture dat in overeen stemming met IAS 28 Investeringen in geassocieerde deelnemingen en joint ventures tegen reële waarde wordt gewaardeerd met verwerking van waardeveranderingen in winst of verlies; of
(ii) wanneer het gaat om een belang in een niet-geconsolideerde gestructureerde entiteit.

## Belangrijke Oordelen En Veronderstellingen

7 Een entiteit moet informatie verschaffen over belangrijke oordelen en veronderstellingen (en wijzigingen in deze oordelen en veronderstellingen) waarvan zij is uitgegaan bij de bepaling van het volgende:
(a) dat zij zeggenschap uitoefent over een andere entiteit, d.w.z. een deelneming zoals beschreven in de alinea’s 5 en 6 van IFRS 10 Geconsolideerde jaarrekening;
(b) dat zij gezamenlijke zeggenschap uitoefent over of invloed van betekenis heeft in een andere entiteit; en
(c) het type gezamenlijke overeenkomst (d.w.z. gezamenlijke bedrijfsactiviteit of joint venture) wanneer de overeenkomst via een afzonderlijk vehikel is gestructureerd. 8 De in overeenstemming met alinea 7 vermelde belangrijke oordelen en veronderstellingen omvatten ook die waarvan door de entiteit wordt uitgegaan wanneer er zich zodanige veranderingen in feiten en omstandigheden hebben voorgedaan dat dit tijdens de verslagperiode leidt tot een wijziging van de conclusie met betrekking tot de vraag of de entiteit zeggenschap, gezamenlijke zeggenschap of invloed van betekenis heeft.

9 Om aan alinea 7 te voldoen, moet een entiteit bijvoorbeeld de belangrijke oordelen en veronderstellingen ver melden waarvan zij is uitgegaan om te bepalen dat:
(a) zij geen zeggenschap heeft over een andere entiteit, ook al houdt zij meer dan de helft van de stemrechten in de andere entiteit;
(b) zij zeggenschap heeft over een andere entiteit, ook al houdt zij minder dan de helft van de stemrechten in de andere entiteit;
(c) zij een agent of principaal is (zie de alinea’s B58 tot en met B72 van IFRS 10);
(d) zij geen invloed van betekenis heeft, ook al houdt zij 20 procent of meer van de stemrechten in een andere entiteit;
(e) zij invloed van betekenis heeft, ook al houdt zij minder dan 20 procent van de stemrechten in een andere entiteit. Status van beleggingsentiteit 9A Wanneer een moedermaatschappij overeenkomstig alinea 27 van IFRS 10 bepaalt dat zij een beleggings entiteit is, dan moet de beleggingsentiteit informatie verschaffen over de belangrijke oordelen en ver onderstellingen waarvan zij is uitgegaan bij de bepaling dat zij een beleggingsentiteit is. Als de beleggings entiteit een of meer van de typische kenmerken van een beleggingsentiteit (zie alinea 28 van IFRS 10) ontbeert, dan moet zij de redenen opgeven waarom zij concludeert dat zij toch een beleggingsentiteit is. 9B Wanneer een entiteit een beleggingsentiteit wordt of geen beleggingsentiteit meer is, dan moet zij de wijziging van haar status als beleggingsentiteit en de redenen voor deze statuswijziging vermelden. Daarnaast moet een entiteit die een beleggingsentiteit wordt, het effect van de statuswijziging op de jaarrekening voor de gepresenteerde periode toelichten, onder vermelding van:
(a) de totale reële waarde op de datum van de statuswijziging van de dochterondernemingen die niet langer worden geconsolideerd;
(b) de eventuele totale winst of het eventuele totale verlies, berekend overeenkomstig alinea B101 van IFRS 10; en
(c) de post(en) in de winst-en-verliesrekening waarin de winst of het verlies is opgenomen (indien niet afzonderlijk gepresenteerd).

## Belangen In Dochterondernemingen

10 Een entiteit moet informatie verstrekken die gebruikers van haar geconsolideerde jaarrekening:
(a) inzicht verschaft in:
(i) de samenstelling van de groep; en
(ii) het belang dat belangen zonder zeggenschap hebben in de activiteiten en kasstromen van de groep (alinea 12); en
(b) in staat stelt het volgende te beoordelen:
(i) de aard en omvang van belangrijke beperkingen op haar vermogen om toegang te krijgen tot of gebruik te maken van activa en om over te gaan tot afwikkeling van verplichtingen van de groep (alinea 13);
(ii) de aard van en wijzigingen in de risico’s die verband houden met haar belangen in geconsoli deerde gestructureerde entiteiten (alinea’s 14 tot en met 17);

(iii) de gevolgen van wijzigingen in haar eigendomsbelang in een dochteronderneming die niet tot een verlies van zeggenschap leiden (alinea 18); en
(iv) de gevolgen van verlies van zeggenschap over een dochteronderneming tijdens de verslagperiode (alinea 19). 11 Indien de datum of periode van de bij de opstelling van de geconsolideerde jaarrekening gebruikte jaarrekening van een dochteronderneming niet samenvalt met die van de geconsolideerde jaarrekening (zie de alinea’s B92 en B93 van IFRS 10), moet een entiteit het volgende vermelden:
(a) de datum van het einde van de verslagperiode van de jaarrekening van de betrokken dochteronderneming; en
(b) de reden waarom niet dezelfde datum of periode wordt gebruikt. Het belang dat belangen zonder zeggenschap hebben in de activiteiten en kasstromen van de groep 12 Voor al haar dochterondernemingen die belangen zonder zeggenschap hebben die van materieel belang zijn voor de verslaggevende entiteit, moet een entiteit het volgende vermelden:
(a) de naam van de dochteronderneming;
(b) de hoofdvestiging (en het land van oprichting, indien verschillend van het land van de hoofdvestiging) van de dochteronderneming;
(c) de omvang van eigendomsbelangen die door belangen zonder zeggenschap worden gehouden;
(d) de omvang van stemrechten die door belangen zonder zeggenschap worden gehouden, indien verschillend van de omvang van de gehouden eigendomsbelangen;
(e) het resultaat dat tijdens de verslagperiode aan belangen zonder zeggenschap van de dochteronderneming is toegerekend;
(f) geaccumuleerde belangen zonder zeggenschap van de dochteronderneming aan het einde van de verslagperi ode;
(g) samengevatte financiële informatie over de dochteronderneming (zie alinea B10). Aard en omvang van belangrijke beperkingen 13 Een entiteit moet het volgende vermelden:
(a) belangrijke beperkingen (bv. wettelijke, contractuele en door regelgevende instanties opgelegde beperkingen) op haar vermogen om toegang te krijgen tot of gebruik te maken van activa en om over te gaan tot afwikkeling van verplichtingen van de groep, zoals:
(i) die welke het vermogen van een moedermaatschappij of haar dochterondernemingen beperken om geld middelen of andere activa over te dragen aan (of te ontvangen van) andere entiteiten binnen de groep;
(ii) garanties of andere vereisten die beperkingen kunnen inhouden voor de uitbetaling van dividenden en andere kapitaaluitkeringen, dan wel voor de verstrekking of terugbetaling van leningen en voorschotten aan (of door) andere entiteiten binnen de groep;
(b) de wijze waarop en mate waarin beschermingsrechten van belangen zonder zeggenschap het vermogen van de entiteit om toegang te krijgen tot of gebruik te maken van activa en om over te gaan tot afwikkeling van verplichtingen van de groep aanzienlijk kunnen beperken (bijvoorbeeld wanneer een moedermaatschappij verplichtingen van een dochteronderneming moet afwikkelen voordat zij haar eigen verplichtingen afwikkelt, of wanneer de goedkeuring van belangen zonder zeggenschap is vereist om toegang te krijgen tot de activa of over te gaan tot de afwikkeling van de verplichtingen van een dochteronderneming);

(c) de boekwaarde in de geconsolideerde jaarrekening van de activa en verplichtingen ten aanzien waarvan deze beperkingen gelden. Aard van de risico’s die verband houden met de belangen van een entiteit in geconsolideerde gestructu reerde entiteiten 14 Een entiteit moet de voorwaarden vermelden van alle contractuele overeenkomsten op grond waarvan de moe dermaatschappij of haar dochterondernemingen verplicht kunnen zijn financiële steun aan een geconsolideerde gestructureerde entiteit te verlenen, met inbegrip van gebeurtenissen of omstandigheden die de verslaggevende entiteit aan een verlies kunnen blootstellen (bv. liquiditeitsovereenkomsten of credit rating triggers die gerelateerd zijn aan verplichtingen om activa van de gestructureerde entiteit te kopen of financiële steun te verlenen). 15 Indien een moedermaatschappij of een van haar dochterondernemingen, zonder daartoe contractueel verplicht te zijn, tijdens de verslagperiode financiële of andere steun aan een geconsolideerde gestructureerde entiteit heeft verleend (bijvoorbeeld kopen van activa van of van instrumenten uitgegeven door de gestructureerde entiteit), moet de entiteit het volgende vermelden:
(a) het type en de omvang van de verleende steun, met inbegrip van de situaties waarin de moedermaatschappij of haar dochterondernemingen de gestructureerde entiteit hebben bijgestaan bij het verkrijgen van financiële steun; en
(b) de redenen voor het verlenen van de steun. 16 Indien een moedermaatschappij of een van haar dochterondernemingen, zonder daartoe contractueel verplicht te zijn, tijdens de verslagperiode financiële of andere steun aan een voordien niet-geconsolideerde gestructureerde entiteit heeft verleend en die steunverlening resulteerde in zeggenschap van de entiteit over de gestructureerde entiteit, moet de entiteit een verklaring vermelden van de relevante factoren die tot deze beslissing hebben geleid. 17 Een entiteit moet informatie verschaffen over alle bestaande voornemens om financiële of andere steun aan een geconsolideerde gestructureerde entiteit te verlenen, met inbegrip van voornemens om de gestructureerde entiteit bij te staan bij het verkrijgen van financiële steun. Gevolgen van wijzigingen in een eigendomsbelang van een moedermaatschappij in een dochteronder neming die niet tot een verlies van zeggenschap leiden 18 Een entiteit moet een schema presenteren dat toont wat de gevolgen voor het aan eigenaars van de moedermaat schappij toerekenbaar eigen vermogen zijn van eventuele wijzigingen in het eigendomsbelang van de moedermaat schappij in een dochteronderneming die niet tot een verlies van zeggenschap leiden. Gevolgen van verlies van zeggenschap over een dochteronderneming tijdens de verslagperiode 19 Een entiteit moet de eventuele winst of het eventuele verlies, berekend overeenkomstig alinea 25 van IFRS 10, vermelden, alsook:
(a) het deel van die winst of dat verlies dat is toe te rekenen aan de waardering van elke in de voormalige dochteronderneming aangehouden investering tegen haar reële waarde op de datum waarop de zeggenschap wordt verloren; en
(b) de post(en) in de winst-en-verliesrekening waarin de winst of het verlies is opgenomen (indien niet afzonderlijk gepresenteerd). BELANGEN IN NIET-GECONSOLIDEERDE DOCHTERONDERNEMINGEN (BELEGGINGSENTITEITEN) 19A Een beleggingsentiteit die overeenkomstig IFRS 10 verplicht is de uitzondering op de consolidatie toe te passen en haar belegging in een dochteronderneming administratief moet verwerken tegen reële waarde met verwerking van waardeveranderingen in winst of verlies, moet dit feit vermelden.

19B Voor elke niet-geconsolideerde dochteronderneming moet een beleggingsentiteit het volgende vermelden:
(a) de naam van de dochteronderneming;
(b) de hoofdvestiging (en het land van oprichting, indien verschillend van het land van de hoofdvestiging) van de dochteronderneming; en
(c) de omvang van het eigendomsbelang van de beleggingsentiteit en, indien verschillend, de omvang van de gehouden stemrechten. 19C Indien een beleggingsentiteit de moedermaatschappij van een andere beleggingsentiteit is, moet de moedermaat schappij ook de op grond van de alinea’s 19B(a)-(c) vereiste informatie verstrekken voor beleggingen waarover zeggenschap wordt uitgeoefend door de beleggingsentiteit die haar dochteronderneming is. Deze informatie mag worden verschaft door in de jaarrekening van de moedermaatschappij de financiële overzichten van de dochter onderneming (of dochterondernemingen) op te nemen die de bovenbedoelde informatie bevatten. 19D Een beleggingsentiteit moet de volgende informatie verschaffen:
(a) de aard en omvang van eventuele belangrijke beperkingen (die bijvoorbeeld voortvloeien uit financieringsover eenkomsten, voorschriften van regelgevende instanties of contractuele overeenkomsten) op het vermogen van een niet-geconsolideerde dochteronderneming om middelen aan de beleggingsentiteit over te dragen in de vorm van dividenden in contanten, of om leningen of voorschotten van de beleggingsentiteit aan de niet- geconsolideerde dochteronderneming terug te betalen; en
(b) alle bestaande verbintenissen of voornemens om financiële of andere steun aan een niet-geconsolideerde dochteronderneming te verlenen, met inbegrip van verbintenissen of voornemens om de dochteronderneming bij te staan bij het verkrijgen van financiële steun. 19E Indien een beleggingsentiteit of een van haar dochterondernemingen, zonder daartoe contractueel verplicht te zijn, tijdens de verslagperiode financiële of andere steun aan een niet-geconsolideerde dochteronderneming heeft ver leend (bijvoorbeeld kopen van activa van of van instrumenten uitgegeven door de dochteronderneming of bijstaan van de dochteronderneming bij het verkrijgen van financiële steun), moet de entiteit het volgende vermelden:
(a) het type en de omvang van de steun die aan elke niet-geconsolideerde dochteronderneming is verleend; en
(b) de redenen voor het verlenen van de steun. 19F Een beleggingsentiteit moet de voorwaarden vermelden van alle contractuele overeenkomsten op grond waarvan de entiteit of haar niet-geconsolideerde dochterondernemingen verplicht kunnen zijn financiële steun te verlenen aan een niet-geconsolideerde, gestructureerde entiteit waarover zij de zeggenschap heeft, met inbegrip van gebeur tenissen of omstandigheden die de verslaggevende entiteit aan een verlies kunnen blootstellen (bv. liquiditeitsover eenkomsten of credit rating triggers die gerelateerd zijn aan verplichtingen om activa van de gestructureerde entiteit te kopen of financiële steun te verlenen). 19G Indien een beleggingsentiteit of een van haar niet-geconsolideerde dochterondernemingen, zonder daartoe con tractueel verplicht te zijn, tijdens de verslagperiode financiële of andere steun heeft verleend aan een niet-geconsoli deerde gestructureerde entiteit waarover de beleggingsentiteit geen zeggenschap had, en indien die steunverlening resulteerde in zeggenschap van de beleggingsentiteit over de gestructureerde entiteit, dan moet de beleggingsentiteit een verklaring vermelden van de relevante factoren die hebben geleid tot de beslissing om deze steun te verlenen.

## Belangen In Gezamenlijke Overeenkomsten En Geassocieerde Deelnemingen

20 Een entiteit moet informatie verschaffen die gebruikers van haar jaarrekening in staat stelt het volgende te beoordelen:
(a) de aard, omvang en financiële gevolgen van haar belangen in gezamenlijke overeenkomsten en ge associeerde deelnemingen, met inbegrip van de aard en gevolgen van haar contractuele relatie met de andere investeerders die gezamenlijk de zeggenschap uitoefenen over, of invloed van betekenis heb ben in gezamenlijke overeenkomsten en geassocieerde deelnemingen (alinea’s 21 en 22); en

(b) de aard van en wijzigingen in de risico’s die verband houden met haar belangen in joint ventures en geassocieerde deelnemingen (alinea 23). Aard, omvang en financiële gevolgen van belangen van een entiteit in gezamenlijke overeenkomsten en geassocieerde deelnemingen 21 Een entiteit moet het volgende vermelden:
(a) voor elke gezamenlijke overeenkomst en geassocieerde deelneming die van materieel belang is voor de ver slaggevende entiteit:
(i) de naam van de gezamenlijke overeenkomst of geassocieerde deelneming;
(ii) de aard van de relatie van de entiteit met de gezamenlijke overeenkomst of geassocieerde deelneming (door, bijvoorbeeld, een beschrijving te geven van de aard van de activiteiten van de gezamenlijke over eenkomst of geassocieerde deelneming en aan te geven of deze van strategisch belang zijn voor de activiteiten van de entiteit);
(iii) de hoofdvestiging (en, in voorkomend geval, het land van oprichting, indien verschillend van het land van de hoofdvestiging) van de gezamenlijke overeenkomst of geassocieerde deelneming;
(iv) de omvang van het eigendomsbelang of de deelneming gehouden door de entiteit en, indien verschillend, de omvang van de gehouden stemrechten (indien van toepassing);
(b) voor elke joint venture en geassocieerde deelneming die van materieel belang is voor de verslaggevende entiteit:
(i) of de investering in de joint venture of geassocieerde deelneming volgens de vermogensmutatiemethode of tegen reële waarde is gewaardeerd;
(ii) samengevatte financiële informatie over de joint venture of geassocieerde deelneming zoals bepaald in de alinea’s B12 en B13;
(iii) indien de joint venture of geassocieerde deelneming administratief wordt verwerkt volgens de vermogens mutatiemethode, de reële waarde van haar investering in de joint venture of geassocieerde deelneming indien er een genoteerde marktprijs voor de investering voorhanden is;
(c) financiële informatie zoals bepaald in alinea B16 over de investeringen van de entiteit in joint ventures en geassocieerde deelnemingen die afzonderlijk niet van materieel belang zijn:
(i) geaggregeerd voor alle joint ventures die afzonderlijk niet van materieel belang zijn, en, apart,
(ii) geaggregeerd voor alle geassocieerde deelnemingen die afzonderlijk niet van materieel belang zijn. 21A Een beleggingsentiteit hoeft de overeenkomstig de alinea’s 21(b) en (c) vereiste informatie niet te verstrekken. 22 De entiteit moet tevens het volgende vermelden:
(a) de aard en omvang van eventuele belangrijke beperkingen (die bijvoorbeeld voortvloeien uit financieringsover eenkomsten, voorschriften van regelgevende instanties of contractuele overeenkomsten tussen investeerders die gezamenlijk de zeggenschap uitoefenen over, of invloed van betekenis hebben in een joint venture of geas socieerde deelneming) op het vermogen van joint ventures of geassocieerde deelnemingen om middelen aan de entiteit over te dragen in de vorm van dividenden in contanten, of om leningen of voorschotten van de entiteit terug te betalen;
(b) indien de datum of periode van de bij de toepassing van de vermogensmutatiemethode gebruikte jaarrekening van een joint venture of geassocieerde deelneming niet samenvalt met die van de jaarrekening van de entiteit:
(i) de datum van het einde van de verslagperiode van de jaarrekening van de betrokken joint venture of geassocieerde deelneming; en
(ii) de reden waarom niet dezelfde datum of periode wordt gebruikt.

(c) het niet-opgenomen aandeel in de verliezen van een joint venture of geassocieerde deelneming, zowel over de verslagperiode als cumulatief, indien de entiteit haar aandeel in de verliezen van de joint venture of geasso cieerde deelneming niet langer opneemt bij de toepassing van de vermogensmutatiemethode. Risico’s verbonden aan belangen van een entiteit in joint ventures en geassocieerde deelnemingen 23 Een entiteit moet het volgende vermelden:
(a) haar verbintenissen die met haar joint ventures verband houden; deze verbintenissen moeten afzonderlijk van het bedrag van andere verbintenissen worden vermeld zoals gespecificeerd in de alinea’s B18 tot en met B20;
(b) overeenkomstig IAS 37 Voorzieningen, voorwaardelijke verplichtingen en voorwaardelijke activa, tenzij verlies zeer onwaarschijnlijk is, voorwaardelijke verplichtingen die de entiteit is aangegaan in verband met haar belangen in joint ventures of geassocieerde deelnemingen (met inbegrip van haar aandeel in de voorwaardelijke verplich tingen die gezamenlijk zijn aangegaan met andere investeerders die gezamenlijk de zeggenschap uitoefenen over, of invloed van betekenis hebben in de betrokken joint ventures of geassocieerde deelnemingen); deze verplichtingen moeten afzonderlijk van het bedrag van andere voorwaardelijke verplichtingen worden vermeld. BELANGEN IN NIET-GECONSOLIDEERDE GESTRUCTUREERDE ENTITEITEN 24 Een entiteit moet informatie verstrekken die gebruikers van haar jaarrekening:
(a) inzicht verschaft in de aard en omvang van haar belangen in niet-geconsolideerde gestructureerde entiteiten (alinea’s 26 tot en met 28); en
(b) in staat stelt zich een oordeel te vormen over de aard van en wijzigingen in de risico’s die verband houden met haar belangen in niet-geconsolideerde gestructureerde entiteiten (alinea’s 29 tot en met
31). 25 De informatie die op grond van alinea 24(b) moet worden verstrekt, omvat informatie over de blootstelling van een entiteit aan risico’s als gevolg van haar betrokkenheid bij niet-geconsolideerde gestructureerde entiteiten in voorgaande perioden (bv. als sponsor van de gestructureerde entiteit), ook al is er op de verslagdatum geen sprake meer van een contractuele betrokkenheid van de entiteit bij de gestructureerde entiteit. 25A Een beleggingsentiteit hoeft de overeenkomstig alinea 24 vereiste informatie niet te verstrekken voor een niet- geconsolideerde gestructureerde entiteit waarover zij de zeggenschap heeft en waarvoor zij de overeenkomstig de alinea’s 19A tot en met 19G vereiste informatie presenteert. Aard van de belangen 26 Een entiteit moet kwalitatieve en kwantitatieve informatie verschaffen over haar belangen in niet-geconsolideerde gestructureerde entiteiten, met inbegrip van maar niet beperkt tot de aard, het doel, de omvang en de activiteiten van de gestructureerde entiteit en de wijze waarop de gestructureerde entiteit is gefinancierd. 27 Indien een entiteit is opgetreden als sponsor van een niet-geconsolideerde gestructureerde entiteit waarvoor zij niet de op grond van alinea 29 te verstrekken informatie verschaft (bijvoorbeeld omdat zij op de verslagdatum geen belang in de entiteit heeft), moet zij het volgende vermelden:
(a) hoe zij heeft bepaald voor welke gestructureerde entiteiten zij als sponsor is opgetreden;
(b) baten uit hoofde van deze gestructureerde entiteiten tijdens de verslagperiode, met inbegrip van een beschrijving van de gepresenteerde soorten baten; en
(c) de boekwaarde (op het moment van overdracht) van alle activa die tijdens de verslagperiode aan deze gestructureerde entiteiten zijn overgedragen.

28 Een entiteit moet de in alinea 27(b) en (c) bedoelde informatie in tabelvorm presenteren, tenzij een andere opmaak meer geëigend is, en haar activiteiten als sponsor in relevante categorieën classificeren (zie de alinea’s B2 tot en met B6). Aard van de risico’s 29 Een entiteit moet in tabelvorm, tenzij een andere opmaak meer geëigend is, een samenvatting presenteren van:
(a) de boekwaarde van de in haar jaarrekening opgenomen activa en verplichtingen die met haar belangen in niet- geconsolideerde gestructureerde entiteiten verband houden;
(b) de posten in het overzicht van de financiële positie waarin deze activa en verplichtingen zijn opgenomen;
(c) het bedrag dat het best de maximale blootstelling van de entiteit aan verlies uit hoofde van haar belangen in niet-geconsolideerde gestructureerde entiteiten weergeeft, met vermelding van de wijze waarop de maximale blootstelling aan verlies is bepaald. Indien een entiteit haar maximale blootstelling aan verlies uit hoofde van haar belangen in niet-geconsolideerde gestructureerde entiteiten niet kan kwantificeren, moet zij dit feit en de redenen waarom vermelden;
(d) een vergelijking van de boekwaarde van de activa en verplichtingen van de entiteit die met haar belangen in niet-geconsolideerde gestructureerde entiteiten verband houden, met de maximale blootstelling van de entiteit aan verlies uit hoofde van deze entiteiten. 30 Indien een entiteit, zonder daartoe contractueel verplicht te zijn, tijdens de verslagperiode financiële of andere steun heeft verleend aan een niet-geconsolideerde gestructureerde entiteit waarin zij voordien een belang had of op het moment een belang heeft (bijvoorbeeld kopen van activa van of instrumenten uitgegeven door de gestructu reerde entiteit), moet de entiteit het volgende vermelden:
(a) het type en de omvang van de verleende steun, met inbegrip van de situaties waarin de entiteit de gestruc tureerde entiteit heeft bijgestaan bij het verkrijgen van financiële steun; en
(b) de redenen voor het verlenen van de steun. 31 Een entiteit moet informatie verschaffen over alle bestaande voornemens om financiële of andere steun aan een niet-geconsolideerde gestructureerde entiteit te verlenen, met inbegrip van voornemens om de gestructureerde entiteit bij te staan bij het verkrijgen van financiële steun.

Bijlage A

## Definities

Deze bijlage is een integraal onderdeel van de IFRS. baten uit hoofde van een gestructureerde entiteit In het kader van deze IFRS omvatten baten uit hoofde van een gestructureerde entiteit, maar zijn zij niet beperkt tot, terugkerende en niet-terugkerende ver goedingen, rente, dividenden, winsten of verliezen als gevolg van de herwaardering of het niet langer opnemen van belangen in gestructureerde entiteiten, en winsten of verliezen voortvloeiend uit de overdracht van activa en verplichtingen aan de gestructureerde entiteit. belang in een andere entiteit In het kader van deze IFRS is een belang in een andere entiteit een contractuele of niet-contractuele betrokkenheid die een entiteit blootstelt aan veranderlijkheid van opbrengsten uit de prestaties van de andere entiteit. Een belang in een andere entiteit kan blijken uit, maar is niet beperkt tot het houden van eigenvermogens instrumenten of schuldbewijzen, alsook andere vormen van betrokkenheid zoals de verstrekking van financiering, liquiditeitssteun, kredietbescherming en garanties. Het omvat de wijze waarop een entiteit zeggenschap of gezamenlijke zeggenschap uitoefent over, of invloed van betekenis heeft in een andere entiteit. Een entiteit heeft niet noodzakelijkerwijze een belang in een andere entiteit enkel en alleen omdat er een typische klanten-leveranciersrelatie bestaat. In de alinea’s B7 tot en met B9 wordt nadere informatie over belangen in andere entiteiten verstrekt. In de alinea’s B55 tot en met B57 van IFRS 10 wordt de veranderlijkheid van opbrengsten toegelicht. gestructureerde entiteit Een entiteit die zodanig is opgezet dat stemrechten of vergelijkbare rechten niet de dominante factor zijn bij het uitmaken wie zeggenschap over de entiteit uitoefent, zoals wanneer eventuele stemrechten uitsluitend met administratieve taken ver band houden en de relevante activiteiten door middel van contactuele overeen komsten worden aangestuurd. In de alinea’s B22 tot en met B24 wordt nadere informatie over gestructureerde entiteiten verstrekt. De volgende begrippen worden gedefinieerd in IAS 27 (herziene versie van 2011), IAS 28 (herziene versie van 2011), IFRS 10 en IFRS 11 Gezamenlijke overeenkomsten en worden in deze IFRS gebruikt met de betekenis die in de genoemde IFRSs wordt omschreven: — geassocieerde deelneming — geconsolideerde jaarrekening — zeggenschap over een entiteit — vermogensmutatiemethode — groep — beleggingsentiteit — gezamenlijke overeenkomst — gezamenlijke zeggenschap

— gezamenlijke bedrijfsactiviteit — joint venture — belang zonder zeggenschap — moedermaatschappij — beschermingsrechten — relevante activiteiten — enkelvoudige jaarrekening — afzonderlijk vehikel — invloed van betekenis — dochteronderneming.

Bijlage B Toepassingsleidraad Deze bijlage is een integraal onderdeel van de IFRS. Ze beschrijft de toepassing van de alinea’s 1 tot en met 31 en heeft dezelfde status als de andere delen van de IFRS. B1 De voorbeelden in deze bijlage hebben betrekking op hypothetische situaties. Sommige aspecten van de voor beelden kunnen weliswaar in feitelijke situaties voorkomen, maar dat neemt niet weg dat bij de toepassing van IFRS 12 alle relevante feiten en omstandigheden van een bepaalde feitelijke situatie moeten worden beoordeeld.

## Samenvoeging (Alinea 4)

B2 Een entiteit moet, in het licht van haar omstandigheden, uitmaken hoe ver zij in detail gaat om aan de informatiebehoeften van gebruikers te voldoen, hoeveel nadruk zij legt op verschillende aspecten van de eisen en hoe zij de informatie samenvoegt. Het is noodzakelijk om een juist evenwicht te vinden tussen het overladen van jaarrekeningen met te veel details waar gebruikers van jaarrekeningen mogelijk niet veel aan hebben en het versluieren van informatie door een te hoge mate van aggregatie. B3 Een entiteit kan de op grond van deze IFRS te verschaffen informatie samenvoegen voor belangen in soortgelijke entiteiten indien een dergelijke samenvoeging consistent is met de informatiedoelstelling en de eis in alinea B4, en de verstrekte informatie niet versluiert. Een entiteit moet vermelden hoe zij haar belangen in soortgelijke entiteiten heeft samengevoegd. B4 Een entiteit moet afzonderlijke informatie presenteren voor belangen in:
(a) dochterondernemingen;
(b) joint ventures;
(c) gezamenlijke bedrijfsactiviteiten;
(d) geassocieerde deelnemingen; en
(e) niet-geconsolideerde gestructureerde entiteiten. B5 Bij de bepaling of informatie wordt samengevoegd, moet een entiteit rekening houden met de kwantitatieve en kwalitatieve informatie over de verschillende kenmerken van de risico’s en opbrengsten van elke entiteit die zij overweegt samen te voegen, alsook met de betekenis van elke betrokken entiteit voor de verslaggevende entiteit. De entiteit moet de informatie op zodanige wijze presenteren dat gebruikers van jaarrekeningen een duidelijk inzicht wordt verschaft in de aard en omvang van haar belangen in deze andere entiteiten. B6 Voorbeelden van eventueel passende aggregatieniveaus binnen de in alinea B4 genoemde klassen van entiteiten zijn:
(a) aard van de activiteiten (bv. een onderzoeks- en ontwikkelingsentiteit, een entiteit voor de securitisatie van revolverende vorderingen uit hoofde van kredietkaarten);
(b) bedrijfstakkenclassificatie;
(c) geografie (bv. land of regio).

## Belangen In Andere Entiteiten

B7 Een belang in een andere entiteit is een contractuele of niet-contractuele betrokkenheid die de verslaggevende entiteit blootstelt aan veranderlijkheid van opbrengsten uit de prestaties van de andere entiteit. Inaanmerking neming van het doel en de opzet van de andere entiteit kan de verslaggevende entiteit helpen bij het beoordelen of zij een belang in deze entiteit heeft, en of zij bijgevolg verplicht is de op grond van deze IFRS te verschaffen informatie te verstrekken. Bij deze beoordeling moet ook rekening worden gehouden met de risico’s waartoe de andere entiteit geacht werd aanleiding te geven en met de risico’s die de andere entiteit aan de verslaggevende entiteit en andere partijen geacht werd over te dragen.

B8 Een verslaggevende entiteit is gewoonlijk aan veranderlijkheid van opbrengsten uit de prestaties van een andere entiteit blootgesteld doordat zij instrumenten (zoals eigenvermogensinstrumenten of schuldbewijzen uitgegeven door de andere entiteit) aanhoudt of een andere vorm van betrokkenheid heeft die veranderlijkheid absorbeert. Stel bijvoorbeeld dat een gestructureerde entiteit een leningportefeuille heeft. De gestructureerde entiteit gaat een credit default swap met een andere entiteit (de verslaggevende entiteit) aan om zich tegen wanbetaling met betrekking tot de rentebetalingen op en aflossingen van de leningen te beschermen. De verslaggevende entiteit heeft een betrokkenheid die haar aan veranderlijkheid van opbrengsten uit de prestaties van de gestructureerde entiteit blootstelt omdat de credit default swap veranderlijkheid van opbrengsten van de gestructureerde entiteit absorbeert. B9 Sommige instrumenten zijn bedoeld om risico van een verslaggevende entiteit aan een andere entiteit over te dragen. Dergelijke instrumenten geven aanleiding tot veranderlijkheid van opbrengsten voor de andere entiteit, maar stellen de verslaggevende entiteit doorgaans niet bloot aan veranderlijkheid van opbrengsten uit de pres taties van de andere entiteit. Stel bijvoorbeeld dat een gestructureerde entiteit wordt opgericht om investerings mogelijkheden te bieden aan investeerders die wensen te worden blootgesteld aan het kredietrisico van entiteit Z (entiteit Z is met geen enkele bij de overeenkomst betrokken partij gelieerd). De gestructureerde entiteit financiert zich door ten behoeve van deze investeerders aan het kredietrisico van entiteit Z gekoppeld waardepapier (”credit-linked notes”) uit te geven en gebruikt de opbrengsten om te investeren in een portefeuille van risicoloze activa. De gestructureerde entiteit stelt zich bloot aan kredietrisico van entiteit Z door met een swaptegenpartij een credit default swap (CDS) aan te gaan. De CDS draagt kredietrisico van entiteit Z over aan de gestructureerde entiteit in ruil voor een door de swaptegenpartij betaalde vergoeding. De investeerders in de gestructureerde entiteit ontvangen een hogere opbrengst die zowel het door de gestructureerde entiteit op haar activaportefeuille behaalde rendement als de CDS-vergoeding weerspiegelt. Er is geen sprake van een betrokkenheid van de swaptegenpartij bij de gestructureerde entiteit welke de swaptegenpartij aan veranderlijkheid van opbrengsten uit de prestaties van de gestructureerde entiteit blootstelt omdat de CDS veranderlijkheid aan de gestructureerde entiteit overdraagt in plaats van veranderlijkheid van de opbrengsten van de gestructureerde entiteit te absor beren. SAMENGEVATTE FINANCIËLE INFORMATIE OVER DOCHTERONDERNEMINGEN, JOINT VENTURES EN GEASSOCIEERDE DEEL

## Nemingen (Alinea’S 12 En 21)

## B10

Voor al haar dochterondernemingen die belangen zonder zeggenschap hebben die van materieel belang zijn voor de verslaggevende entiteit, moet een entiteit het volgende vermelden:
(a) aan belangen zonder zeggenschap betaalde dividenden;
(b) samengevatte financiële informatie over de activa, verplichtingen, resultaten en kasstromen van de dochter onderneming die gebruikers inzicht verschaft in het belang dat belangen zonder zeggenschap hebben in de activiteiten en kasstromen van de groep. Deze informatie omvat eventueel maar is niet beperkt tot bijvoor beeld vlottende activa, vaste activa, kortlopende verplichtingen, langlopende verplichtingen, opbrengsten, winst of verlies, en het totaalresultaat.

## B11

De op grond van alinea B10(b) te verschaffen samengevatte financiële informatie moet bestaan uit de bedragen vóór intragroepseliminaties.

## B12

Voor elke joint venture en geassocieerde deelneming die van materieel belang is voor de verslaggevende entiteit, moet een entiteit het volgende vermelden:
(a) van de joint venture of geassocieerde deelneming ontvangen dividenden;
(b) samengevatte financiële informatie over de joint venture of geassocieerde deelneming (zie de alinea’s B14 en B15), met inbegrip van maar niet noodzakelijkerwijze beperkt tot:
(i) vlottende activa;
(ii) vaste activa;
(iii) kortlopende verplichtingen;
(iv) langlopende verplichtingen;
(v) opbrengsten;

(vi) de winst of het verlies uit voortgezette bedrijfsactiviteiten;
(vii) de winst of het verlies na belastingen uit beëindigde bedrijfsactiviteiten;
(viii) overige onderdelen van het totaalresultaat;
(ix) het totaalresultaat.

## B13

Naast de op grond van alinea B12 te verschaffen samengevatte financiële informatie moet een entiteit voor elke joint venture die van materieel belang is voor de verslaggevende entiteit de volgende bedragen vermelden:
(a) de geldmiddelen en kasequivalenten vervat in de in alinea B12(b)(i) bedoelde informatie;
(b) de kortlopende financiële verplichtingen (exclusief handelsschulden en overige schulden en voorzieningen) vervat in de in alinea B12(b)(iii) bedoelde informatie;
(c) de langlopende financiële verplichtingen (exclusief handelsschulden en overige schulden en voorzieningen) vervat in de in alinea B12(b)(iv) bedoelde informatie;
(d) afschrijvingen;
(e) rentebaten;
(f) rentelasten;
(g) lasten of baten uit hoofde van winstbelastingen.

## B14

De samengevatte financiële informatie die overeenkomstig de alinea’s B12 en B13 wordt gepresenteerd, moet bestaan uit de bedragen die in de IFRS-jaarrekening van de joint venture of geassocieerde deelneming zijn opgenomen (en niet uit het aandeel van de entiteit in deze bedragen). Indien de entiteit haar belang in de joint venture of geassocieerde deelneming volgens de vermogensmutatiemethode verwerkt:
(a) moeten de in de IFRS-jaarrekening van de joint venture of geassocieerde deelneming opgenomen bedragen worden aangepast om de aanpassingen weer te geven die de entiteit bij de toepassing van de vermogens mutatiemethode heeft aangebracht, zoals aanpassingen naar reële waarde op het moment van de overname en aanpassingen in verband met verschillen in grondslagen voor financiële verslaggeving;
(b) moet de entiteit een aansluiting tussen de gepresenteerde samengevatte financiële informatie en de boek waarde van haar belang in de joint venture of geassocieerde deelneming vermelden.

## B15

Een entiteit kan de op grond van de alinea’s B12 en B13 te verschaffen samengevatte financiële informatie op basis van de jaarrekening van de joint venture of geassocieerde deelneming presenteren indien:
(a) de entiteit haar belang in de joint venture of geassocieerde deelneming tegen reële waarde waardeert over eenkomstig IAS 28 (herziene versie van 2011); en
(b) de joint venture of geassocieerde deelneming geen IFRS-jaarrekening opstelt en de opstelling van een dergelijke jaarrekening praktisch niet haalbaar is of ongerechtvaardigde kosten met zich meebrengt. In dat geval moet de entiteit de grondslag vermelden waarop de samengevatte financiële informatie is opgesteld.

## B16

Een entiteit moet de geaggregeerde boekwaarde vermelden van haar belangen in alle afzonderlijk niet van materieel belang zijnde joint ventures of geassocieerde deelnemingen die volgens de vermogensmutatiemethode zijn verwerkt. Een entiteit moet ook apart het geaggregeerde bedrag vermelden van haar aandeel in de volgende bedragen van die joint ventures of geassocieerde deelnemingen:

(a) de winst of het verlies uit voortgezette bedrijfsactiviteiten;
(b) de winst of het verlies na belastingen uit beëindigde bedrijfsactiviteiten;
(c) overige onderdelen van het totaalresultaat;
(d) het totaalresultaat. Een entiteit verstrekt de informatie afzonderlijk voor joint ventures en geassocieerde deelnemingen.

## B17

Wanneer het belang van een entiteit in een dochteronderneming, joint venture of geassocieerde deelneming (of een deel van haar belang in een joint venture of geassocieerde deelneming) is geclassificeerd (of is opgenomen in een groep activa die wordt afgestoten en die is geclassificeerd) als aangehouden voor verkoop in overeenstem ming met IFRS 5, is de entiteit niet verplicht voor de betrokken dochteronderneming, joint venture of geasso cieerde deelneming samengevatte financiële informatie in overeenstemming met de alinea’s B10 tot en met B16 te verschaffen. VERBINTENISSEN IN VERBAND MET JOINT VENTURES (ALINEA 23(a))

## B18

Een entiteit moet het totale bedrag van de op de verslagdatum aangegane maar niet opgenomen verbintenissen (met inbegrip van haar aandeel in verbintenissen die gezamenlijk zijn aangegaan met andere investeerders die gezamenlijk de zeggenschap over een joint venture uitoefenen) vermelden die met haar belangen in joint ventures verband houden. Verbintenissen zijn toezeggingen die aanleiding kunnen geven tot een toekomstige uitstroom van geldmiddelen of andere middelen.

## B19

Niet-opgenomen verbintenissen die tot een toekomstige uitstroom van geldmiddelen of andere middelen aan leiding kunnen geven, omvatten:
(a) niet-opgenomen verbintenissen om financiering of middelen in te brengen als gevolg van bijvoorbeeld:
(i) de oprichtings- of overnameovereenkomst van een joint venture (op grond waarvan een entiteit bijvoor beeld verplicht is over een specifieke periode middelen in te brengen);
(ii) door een joint venture opgezette kapitaalintensieve projecten;
(iii) onvoorwaardelijke aankoopverplichtingen, die bestaan in de aankoop van bedrijfsinstallaties, voorraden of diensten die een entiteit heeft toegezegd van of namens een joint venture te zullen kopen;
(iv) niet-opgenomen verbintenissen om leningen of andere financiële steun aan een joint venture te ver strekken;
(v) niet-opgenomen verbintenissen om middelen, zoals activa of diensten, in een joint venture in te brengen;
(vi) andere niet-opzegbare niet-opgenomen verbintenissen die met een joint venture verband houden;
(b) niet-opgenomen verbintenissen om het eigendomsbelang van een andere partij (of een deel van dat eigen domsbelang) in een joint venture over te nemen indien er in de toekomst een bepaalde gebeurtenis plaats vindt of niet plaatsvindt.

## B20

De eisen en voorbeelden in de alinea’s B18 en B19 illustreren sommige typen van informatie die op grond van alinea 18 van IAS 24 Informatieverschaffing over verbonden partijen moet worden verstrekt: BELANGEN IN NIET-GECONSOLIDEERDE GESTRUCTUREERDE ENTITEITEN (ALINEA’S 24 TOT EN MET 31) Gestructureerde entiteiten

## B21

Een gestructureerde entiteit is een entiteit die zodanig is opgezet dat stemrechten of vergelijkbare rechten niet de dominante factor zijn bij het uitmaken wie zeggenschap over de entiteit uitoefent, zoals wanneer eventuele stemrechten uitsluitend met administratieve taken verband houden en de relevante activiteiten door middel van contactuele overeenkomsten worden aangestuurd.

## B22

Een gestructureerde entiteit heeft veelal sommige of alle volgende kenmerken of eigenschappen:
(a) beperkte activiteiten;
(b) een beperkte en duidelijk omlijnde doelstelling, zoals het uitvoeren van een fiscaal interessante lease, het verrichten van onderzoeks- en ontwikkelingsactiviteiten, het verstrekken aan een entiteit van een bron van kapitaal of financiering, of het bieden van investeringsmogelijkheden aan investeerders door aan de activa van de gestructureerde entiteit verbonden risico’s en voordelen aan investeerders over te dragen;
(c) ontoereikend eigen vermogen om de gestructureerde entiteit in staat te stellen haar activiteiten te financieren zonder achtergestelde financiële steun;
(d) financiering in de vorm van diverse contractueel verbonden instrumenten ten behoeve van investeerders welke tot kredietconcentraties of andere risico’s aanleiding geven (tranches).

## B23

Voorbeelden van entiteiten die als gestructureerde entiteiten worden beschouwd, zijn:
(a) securitisatievehikels;
(b) door activa gedekte financieringen;
(c) sommige beleggingsfondsen.

## B24

Een entiteit waarover via stemrechten zeggenschap wordt uitgeoefend, is geen gestructureerde entiteit enkel en alleen omdat zij bijvoorbeeld na een reorganisatie financiering van derden ontvangt. Aard van de risico’s van belangen in niet-geconsolideerde gestructureerde entiteiten (alinea’s 29 tot en met 31)

## B25

Naast de op grond van de alinea’s 29 tot en met 31 te verschaffen informatie moet een entiteit alle aanvullende informatie verstrekken die noodzakelijk is om aan de informatiedoelstelling van alinea 24(b) te voldoen.

## B26

Voorbeelden van aanvullende informatie die, afhankelijk van de omstandigheden, eventueel relevant kan zijn voor een beoordeling van de risico’s waaraan een entiteit is blootgesteld wanneer zij een belang in een niet- geconsolideerde gestructureerde entiteit heeft, zijn:
(a) de voorwaarden van een overeenkomst op grond waarvan de entiteit verplicht kan zijn financiële steun aan een niet-geconsolideerde gestructureerde entiteit te verlenen (bv. liquiditeitsovereenkomsten of credit rating triggers die gerelateerd zijn aan verplichtingen om activa van de gestructureerde entiteit te kopen of finan ciële steun te verlenen), met inbegrip van:
(i) een beschrijving van gebeurtenissen of omstandigheden die de verslaggevende entiteit aan een verlies kunnen blootstellen;
(ii) of er voorwaarden zijn die de verplichting beperken;
(iii) of er andere partijen zijn die financiële steun verlenen en, indien dit het geval is, welke rangorde de verplichting van de verslaggevende entiteit heeft ten opzichte van de verplichtingen van andere partijen;
(b) door de entiteit tijdens de verslagperiode geleden verliezen die met haar belangen in niet-geconsolideerde gestructureerde entiteiten verband houden;
(c) de door de entiteit tijdens de verslagperiode ontvangen soorten baten uit hoofde van haar belangen in niet- geconsolideerde gestructureerde entiteiten;

(d) of de entiteit verplicht is vóór andere partijen verliezen van een niet-geconsolideerde gestructureerde entiteit te absorberen, de maximumlimiet van dergelijke verliezen voor de entiteit, en (indien relevant) de rangorde en bedragen van de potentiële verliezen die worden gedragen door partijen met belangen die van een lagere rangorde zijn dan het belang van de entiteit in de niet-geconsolideerde gestructureerde entiteit;
(e) informatie over liquiditeitsovereenkomsten, garanties of andere verbintenissen met derden welke van invloed kunnen zijn op de reële waarde of het risico van belangen van de entiteit in niet-geconsolideerde gestruc tureerde entiteiten;
(f) eventuele moeilijkheden die een niet-geconsolideerde gestructureerde entiteit tijdens de verslagperiode heeft ondervonden bij de financiering van haar activiteiten;
(g) in verband met de financiering van een niet-geconsolideerde gestructureerde entiteit, de financieringsvormen (bv. commercial paper of medium-term notes) en de gewogen gemiddelde looptijd ervan. Deze informatie kan eventueel vervaldaganalyses van de activa en de financiering van een niet-geconsolideerde gestructureerde entiteit omvatten indien de gestructureerde entiteit langerlopende activa heeft die met behulp van korterlo pende financiering worden gefinancierd.

Bijlage C

## Ingangsdatum En Overgang

Deze bijlage is een integraal onderdeel van de IFRS en heeft hetzelfde gezag als de andere delen van de IFRS.

## Ingangsdatum En Overgang

C1 Entiteiten moeten deze IFRS toepassen op jaarperioden die op of na 1 januari 2013 aanvangen. Eerdere toepassing is toegestaan. C1A De alinea’s C2A en C2B zijn toegevoegd door de in juni 2012 uitgegeven Geconsolideerde jaarrekening, gezamenlijke overeenkomsten en informatieverschaffing over belangen in andere entiteiten: overgangsleidraden (wijzigingen in IFRS 10, IFRS 11 en IFRS 12). Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2013 aanvangen. Als een entiteit IFRS 12 op een eerdere periode toepast, moet zij ook deze wijzigingen op die eerdere periode toepassen. C1B Alinea 2 en bijlage A zijn gewijzigd en de alinea’s 9A-9B, 19A-19G, 21A en 25A zijn toegevoegd door Beleggings entiteiten (wijzigingen in IFRS 10, IFRS 12 en IAS 27), uitgegeven in oktober 2012. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2014 aanvangen. Eerdere toepassing is toegestaan. Indien een entiteit deze wijzigingen eerder toepast, moet zij dit feit vermelden en tegelijkertijd alle in Beleggings entiteiten vervatte wijzigingen toepassen. C1C Alinea 6 is gewijzigd door Beleggingsentiteiten: toepassing van de uitzondering op de consolidatie (wijzigingen in IFRS 10, IFRS 12 en IAS 28), uitgegeven in december 2014. Entiteiten moeten die wijziging toepassen op jaar perioden die op of na 1 januari 2016 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijziging op een eerdere periode toepast, moet zij dit feit vermelden. C1D Alinea 5A is toegevoegd en alinea B17 is gewijzigd door jaarlijkse verbeteringen aan IFRS (cyclus 2014-2016), uitgegeven in december 2016. Entiteiten moeten deze wijzigingen retroactief toepassen in overeenstemming met IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten op jaarperioden die op of na 1 januari 2017 aanvangen. C2 Een entiteit wordt aangemoedigd om op grond van deze IFRS te verschaffen informatie eerder te verstrekken dan voor jaarperioden die op of na 1 januari 2013 aanvangen. Het verstrekken van sommige op grond van deze IFRS te verschaffen informatie verplicht de entiteit niet om aan alle eisen van deze IFRS te voldoen of IFRS 10, IFRS 11, IAS 27 (herziene versie van 2011) en IAS 28 (herziene versie van 2011) eerder toe te passen. C2A De vereisten inzake informatieverschaffing van deze IFRS hoeven niet te worden toegepast op een gepresenteerde periode die aanvangt vóór de jaarperiode die onmiddellijk voorafgaat aan de eerste jaarperiode waarop IFRS 12 wordt toegepast. C2B De vereisten inzake informatieverschaffing van de alinea’s 24 tot en met 31 en de overeenkomstige leidraden in de alinea’s B21 tot en met B26 van deze IFRS hoeven niet te worden toegepast op een gepresenteerde periode die aanvangt vóór de eerste jaarperiode waarop IFRS 12 wordt toegepast.

## Verwijzingen Naar Ifrs 9

C3 Als een entiteit wel deze IFRS maar nog niet IFRS 9 toepast, moeten alle verwijzingen naar IFRS 9 worden gelezen als verwijzingen naar IAS 39 Financiële instrumenten: opname en waardering.
