---
title: IAS-26 — Administratieve verwerking en verslaggeving door pensioenregelingen
tags:
- '1.5'
- ifrs
- ias
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IAS
standaard_nummer: '26'
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
    pages: 176-183
  tooling:
    pipeline: tools/etl/split_ifrs_verordening.py
    pipeline_version: '1.0'
    model: null
    prompt_version: null
  generated_at: '2026-05-16T19:10:04Z'
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

## International Accounting Standard 26

Administratieve verwerking en verslaggeving door pensioenregelingen

## Toepassingsgebied

1 Deze standaard moet worden toegepast in de jaarrekening van pensioenregelingen indien dergelijke jaar rekeningen worden opgesteld. 2 Naar pensioenregelingen wordt soms verwezen met verschillende andere namen, zoals “stelsels van ouderdoms verzekering”, “pensioenplannen ” of “pensioenstelsels ”. In deze standaard wordt een pensioenregeling beschouwd als een afzonderlijke verslaggevende entiteit, los van de werkgevers van de deelnemers aan de regeling. Alle andere International Accounting Standards zijn van toepassing op de jaarrekening van pensioenregelingen in zoverre ze niet door deze standaard worden vervangen. 3 Deze standaard behandelt de administratieve verwerking en verslaggeving door de regeling aan alle deelnemers als een groep. Verslagen aan individuele deelnemers over hun pensioenrechten worden niet behandeld. 4 IAS 19 Personeelsbeloningen behandelt de bepaling van de kosten van pensioenrechten in de jaarrekening van werk gevers die over regelingen beschikken. Deze standaard vormt dan ook een aanvulling op IAS 19. 5 Pensioenregelingen kunnen toegezegdebijdrageregelingen of toegezegdpensioenregelingen zijn. Voor vele regelingen kan de oprichting van aparte regelingen vereist zijn, die al dan niet een afzonderlijke juridische identiteit kunnen hebben en die al dan niet over beheerders kunnen beschikken, waaraan bijdragen worden gestort en waaruit pensioenrechten worden betaald. Deze standaard is van toepassing ongeacht het feit of een dergelijke regeling is opgericht en onafhankelijk van het al dan niet bestaan van beheerders. 6 Op pensioenregelingen met activa die bij verzekeringsmaatschappijen worden belegd, zijn dezelfde vereisten inzake administratieve verwerking en financiering van toepassing als op regelingen die door de entiteit zelf worden gefinancierd. Bijgevolg vallen ze binnen het toepassingsgebied van deze standaard, tenzij het contract bij de ver zekeringsmaatschappij is opgesteld in de naam van een bepaalde deelnemer of groep van deelnemers en de pensioenverplichting uitsluitend de verantwoordelijkheid is van de verzekeringsmaatschappij. 7 Deze standaard behandelt geen andere vormen van personeelsbeloningen, zoals ontslagvergoedingen, regelingen in verband met uitgestelde vergoedingen, verlof voor lange dienstprestatie, bijzondere regelingen voor vervroegde pensionering of afvloeiingsregelingen, regelingen inzake medische vergoedingen, bijstandsregelingen of bonusrege lingen. Regelingen van de overheid inzake socialezekerheidsvergoedingen vallen eveneens buiten het toepassings gebied van deze standaard.

## Definities

8 De volgende begrippen worden in deze standaard gebruikt met de hierna omschreven betekenis: Pensioenregelingen zijn regelingen waarbij een entiteit beloningen verschaft aan haar werknemers op het moment van de beëindiging van het dienstverband of daarna (ofwel in de vorm van jaarlijkse inkomsten ofwel als een vast bedrag), indien dergelijke beloningen, of de bijdragen ten behoeve van deze beloningen, vóór het pensioen kunnen worden bepaald of geschat op basis van de bepalingen van een document of uit de bestendig toegepaste gedrags lijnen van de entiteit. Toegezegdebijdrageregelingen zijn pensioenregelingen waarvoor de bedragen die als pensioenrechten moeten worden betaald, worden bepaald op basis van de bijdragen aan een fonds, samen met de beleggingsopbrengsten daarop. Toegezegdpensioenregelingen zijn pensioenregelingen waarvoor de bedragen die als pensioenrechten moeten worden betaald, worden bepaald op basis van een formule die gewoonlijk gebaseerd is op de inkomsten en/of het aantal dienstjaren van werknemers.

Financiering is de overdracht van activa aan een entiteit (het fonds) die geen juridische banden heeft met de entiteit van de werkgever, om toekomstige verplichtingen voor de betaling van de pensioenrechten te vervullen. In het kader van deze standaard worden eveneens de volgende begrippen gehanteerd: Deelnemers zijn de participanten aan een pensioenregeling alsmede anderen die recht hebben op beloningen uit hoofde van de regeling. Nettoactiva beschikbaar voor uitkeringen zijn de activa van een fonds, verminderd met alle andere verplichtingen dan de actuariële contante waarde van toegezegde pensioenrechten. Actuariële contante waarde van toegezegde pensioenrechten is de contante waarde van de verwachte betalingen door een pensioenfonds aan bestaande en voormalige werknemers, welke betalingen zijn toe te rekenen aan de reeds verrichte arbeidsprestaties. Onvoorwaardelijk toegezegde beloningen zijn beloningen waarop de rechten ingevolge de bepalingen van een pensioen regeling, niet afhankelijk zijn van de voortzetting van het dienstverband. 9 Bepaalde pensioenregelingen hebben andere sponsors dan werkgevers. Deze standaard is eveneens van toepassing op de jaarrekening van dergelijke regelingen. 10 De meeste pensioenregelingen zijn gebaseerd op formele overeenkomsten. Bepaalde regelingen zijn informeel, maar hebben een bepaalde graad van verplichting verkregen ten gevolge van de bestendig toegepaste gedragslijnen van de werkgever. Hoewel het werkgevers ingevolge sommige regelingen is toegestaan om hun verplichtingen uit hoofde van de regelingen te beperken, is het voor een werkgever gewoonlijk moeilijk om een regeling te annuleren, wil hij zijn werknemers behouden. Op zowel informele als formele regelingen zijn dezelfde grondslagen voor financiële verwerking en verslaggeving van toepassing. 11 Vele pensioenregelingen voorzien in de oprichting van afzonderlijke fondsen waarin bijdragen worden gestort en waaruit uitkeringen worden betaald. Dergelijke fondsen kunnen worden beheerd door partijen die onafhankelijk handelen voor het beheer van fondsbeleggingen. In sommige landen worden deze partijen beheerders genoemd. Het begrip beheerder wordt in deze standaard gebruikt om naar dergelijke partijen te verwijzen, ongeacht of een trust is opgericht. 12 Pensioenregelingen kunnen normaliter worden ingedeeld als toegezegdebijdrageregelingen of toegezegdpensioen regelingen, die elk over hun eigen onderscheidende kenmerken beschikken. Incidenteel kunnen er tevens regelingen bestaan die kenmerken van beide soorten regelingen in zich bergen. Dergelijke hybridische regelingen worden in het kader van deze standaard beschouwd als toegezegdpensioenregelingen.

## Toegezegdebijdrageregelingen

13 De jaarrekening van een toegezegdebijdrageregeling moeten een overzicht bevatten van de nettoactiva beschikbaar voor uitkeringen en een omschrijving van het financieringsbeleid. 14 In een toegezegdebijdrageregeling wordt het bedrag van de toekomstige uitkeringen van een deelnemer bepaald door de bijdragen die door de werkgever, de deelnemer, of beiden worden betaald, alsmede door de beleggingsopbreng sten en de operationele efficiency van het fonds. Een werkgever voldoet gewoonlijk aan zijn verplichting door bijdragen te storten in het fonds. Normaliter is advies van een actuaris niet vereist, hoewel dergelijk advies soms wordt gebruikt om een raming te maken van de toekomstige uitkeringen die kunnen worden verkregen, op basis van de actuele bijdragen en de variërende niveaus van toekomstige bijdragen en beleggingsopbrengsten. 15 De deelnemers zijn geïnteresseerd in de activiteiten van de regeling, aangezien deze een directe invloed hebben op het bedrag van hun toekomstige uitkeringen. Deelnemers wensen op de hoogte te zijn van het feit of bijdragen zijn ontvangen en of deze op een geëigende wijze worden beheerd om de rechten van de begunstigden te beschermen. Een werkgever heeft belangstelling voor de efficiënte en billijke werking van de regeling.

16 Het doel van de verslaggeving door een toegezegdebijdrageregeling is periodiek informatie te verschaffen over de regeling en over de financiële prestaties van de beleggingen. Dit doel wordt gewoonlijk bereikt door in de financiële overzichten het volgende op te nemen:
(a) een beschrijving van de belangrijkste activiteiten over de periode en de gevolgen van eventuele wijzigingen ten aanzien van de regeling, en van de deelnemers en de algemene bepalingen;
(b) overzichten die verslag uitbrengen over de transacties en de beleggingsprestaties over de periode en de financiële positie van de regeling aan het eind van de periode; en
(c) een beschrijving van het beleggingsbeleid.

## Toegezegdpensioenregelingen

17 De jaarrekening van een toegezegdpensioenregeling moeten omvatten, hetzij:
(a) een overzicht van:
(i) de nettoactiva beschikbaar voor uitkeringen;
(ii) de actuariële contante waarde van toegezegde pensioenrechten, met een onderscheid tussen onvoorwaarde lijk toegezegde beloningen en niet onvoorwaardelijk toegezegde beloningen; en
(iii) het resulterende surplus of tekort; dan wel
(b) een overzicht van de nettoactiva beschikbaar voor uitkeringen, met inbegrip van hetzij:
(i) een toelichting waarin de actuariële contante waarde van toegezegde pensioenrechten wordt uiteengezet, met een onderscheid tussen onvoorwaardelijk toegezegde beloningen en niet onvoorwaardelijk toegezegde be loningen; dan wel
(ii) een verwijzing naar deze informatie in een begeleidend actuarieel verslag. Als op de datum van de financiële overzichten geen actuariële waardering is opgesteld, moet de recentste waardering als basis worden gebruikt en moet de datum van de waardering worden vermeld. 18 Ten behoeve van alinea 17 moet de actuariële contante waarde van toegezegde pensioenrechten worden gebaseerd op de uitkeringen die op grond van de bepalingen van de regeling zijn toegezegd voor tot dan toe verrichte arbeidsprestaties, door als basis hetzij het actuele loonniveau, hetzij het voorspelde loonni veau te gebruiken en te vermelden welke basis werd gehanteerd. Het gevolg van enigerlei wijzigingen in actuariële veronderstellingen die een wezenlijk effect hebben gehad op de actuariële contante waarde van toegezegde pensioenrechten moet eveneens worden vermeld. 19 In de financiële overzichten moet het verband worden verklaard tussen de actuariële contante waarde van toegezegde pensioenrechten en de nettoactiva beschikbaar voor uitkeringen, alsmede het beleid voor de financiering van de toegezegde uitkeringen. 20 In een toegezegdpensioenregeling is de betaling van de toegezegde pensioenrechten afhankelijk van de financiële positie van de regeling en het vermogen van bijdrageverschaffers om in de toekomst bijdragen te leveren aan de regeling, alsmede van de beleggingsprestaties en de operationele efficiency van de regeling.

21 Voor een toegezegdpensioenregeling is periodiek advies van een actuaris vereist om de financiële toestand van de regeling vast te stellen, de veronderstellingen te beoordelen en aanbevelingen te doen over het niveau van de toekomstige bijdragen. 22 Het doel van de verslaggeving door een toegezegdpensioenregeling is om periodiek informatie te verschaffen over de financiële middelen en activiteiten van de regeling, die nuttig is om de relaties te beoordelen tussen de opgebouwde middelen en de uitkeringen van de regeling in de loop der tijd. Dit doel wordt gewoonlijk bereikt door in de financiële overzichten het volgende op te nemen:
(a) een beschrijving van de belangrijkste activiteiten over de periode en de gevolgen van eventuele wijzigingen ten aanzien van de regeling, en van de deelnemers en de algemene bepalingen;
(b) overzichten die verslag uitbrengen over de transacties en de beleggingsprestaties over de periode en de financiële positie van de regeling aan het eind van de periode;
(c) actuariële informatie, hetzij als onderdeel van de overzichten of in een afzonderlijk verslag; en
(d) een beschrijving van het beleggingsbeleid. Actuariële contante waarde van toegezegde pensioenrechten 23 De contante waarde van de verwachte uitkeringen in het kader van een pensioenregeling kan worden berekend en in de verslaggeving worden opgenomen door gebruik te maken van het actuele loonniveau of het voorspelde loon niveau tot de datum waarop de deelnemers met pensioen gaan. 24 De redenen voor het gebruik van de benadering op basis van het actuele loon omvatten:
(a) de actuariële contante waarde van toegezegde pensioenrechten, zijnde de som van de bedragen die actueel aan elke deelnemer aan de regeling kunnen worden toegerekend, kan op een objectievere manier worden berekend dan voorspelde loonniveaus omdat er minder veronderstellingen zijn vereist;
(b) verhogingen van de vergoedingen die aan een loonsverhoging kunnen worden toegerekend, worden een ver plichting van de regeling op het moment van de loonsverhoging; en
(c) het bedrag van de actuariële contante waarde van toegezegde pensioenrechten op basis van het actuele loon niveau is doorgaans nauwer verbonden met het bedrag dat moet worden betaald in geval van beëindiging of stopzetting van de regeling. 25 De redenen voor het gebruik van de benadering op basis van het voorspelde loonniveau omvatten:
(a) financiële informatie moet worden opgesteld op basis van het continuïteitsbeginsel, onafhankelijk van de te maken veronderstellingen en schattingen;
(b) bij regelingen op basis van het eindsalaris worden de uitkeringen bepaald op basis van het loon op of omstreeks de pensioendatum; bijgevolg moeten er voorspellingen gebeuren omtrent lonen, bijdrageniveaus en rendemen ten; en
(c) als het grootste gedeelte van de financiering gebaseerd is op loonvoorspellingen en de loonvoorspellingen niet worden opgenomen, kan dit ertoe leiden dat uit de verslaggeving een overfinanciering blijkt terwijl de regeling niet overgefinancierd is, of dat uit de verslaggeving een voldoende financiering blijkt, terwijl het fonds onder gefinancierd is.

26 De actuariële contante waarde van toegezegde pensioenrechten op basis van het actuele loonniveau wordt in de jaarrekening van een regeling vermeld om de verplichting aan te geven voor uitkeringen die tot op de datum van de financiële overzichten zijn verdiend. De actuariële contante waarde van toegezegde pensioenrechten op basis van het voorspelde loonniveau wordt vermeld om op basis van het continuïteitsbeginsel de omvang van de potentiële verplichting aan te geven, die doorgaans tevens het uitgangspunt voor de financiering vormt. Naast de vermelding van de actuariële contante waarde van toegezegde pensioenrechten, moet mogelijk voldoende informatie worden verstrekt om duidelijk aan te geven in welke context de actuariële contante waarde van toegezegde pensioenrechten moet worden begrepen. Een dergelijke verklaring kan worden gegeven in de vorm van informatie over de geschikt heid van de geplande toekomstige financiering en het financieringsbeleid op basis van loonvoorspellingen. Dit kan worden opgenomen in de financiële overzichten of in het verslag van de actuaris. Frequentie van actuariële waarderingen 27 In vele landen worden actuariële waarderingen niet vaker dan elke drie jaar uitgevoerd. Als op de datum van de financiële overzichten geen actuariële waardering is opgesteld, wordt de recentste waardering als basis gebruikt en wordt de datum van de waardering vermeld. Inhoud van de financiële overzichten 28 Voor toegezegdpensioenregelingen wordt informatie gepresenteerd in een van de volgende indelingen, die verschil lende praktijken weerspiegelt voor de presentatie en toelichting van actuariële informatie:
(a) in de financiële overzichten wordt een overzicht opgenomen van de nettoactiva beschikbaar voor uitkeringen, de actuariële contante waarde van toegezegde pensioenrechten en het resulterende surplus of tekort. De jaarreke ning van de regeling omvat eveneens mutatieoverzichten van de nettoactiva beschikbaar voor uitkeringen en mutatieoverzichten van de actuariële contante waarde van toegezegde pensioenrechten. In de financiële over zichten kan een afzonderlijk verslag van de actuaris zijn vervat ter ondersteuning van de actuariële contante waarde van toegezegde pensioenrechten;
(b) financiële overzichten met een overzicht van de nettoactiva beschikbaar voor uitkeringen en een mutatieover zicht van de nettoactiva beschikbaar voor uitkeringen. De actuariële contante waarde van toegezegde pensioen rechten wordt vermeld in de toelichting bij de overzichten. In de financiële overzichten kan een afzonderlijk verslag van de actuaris zijn vervat ter ondersteuning van de actuariële contante waarde van toegezegde pensioen rechten; en
(c) financiële overzichten met een overzicht van de nettoactiva beschikbaar voor uitkeringen en een mutatieover zicht van de nettoactiva beschikbaar voor uitkeringen waarbij de actuariële contante waarde van toegezegde pensioenrechten is vermeld in een afzonderlijk actuarieel verslag. In elke indeling kan een verslag van de beheerders worden opgenomen in de vorm van een managementverslag of een directieverslag, en bij de financiële overzichten kan tevens een beleggingsverslag worden gevoegd. 29 Voorstanders van de indelingen die zijn beschreven in alinea 28(a) en (b) zijn van mening dat de kwantificering van toegezegde pensioenrechten en andere informatie die uit hoofde van deze benadering wordt verschaft, de gebruikers ervan als hulpmiddel dienen bij de beoordeling van de actuele status van het fonds en de waarschijnlijkheid dat het fonds zijn verplichtingen zal nakomen. Zij zijn tevens van mening dat de financiële overzichten op zich volledig moeten zijn, en niet door bijgevoegde overzichten moeten worden aangevuld. Sommigen zijn echter van mening dat de indeling die in alinea 28(a) wordt beschreven, de indruk geeft dat er een verplichting bestaat, terwijl de actuariële contante waarde van toegezegde pensioenrechten naar hun mening niet alle kenmerken van een verplichting in zich bergt.

30 Voorstanders van de indeling beschreven in alinea 28(c) zijn van mening dat de actuariële contante waarde van toegezegde pensioenrechten niet in een overzicht van de nettoactiva beschikbaar voor uitkeringen moet worden opgenomen in de indeling die in alinea 28(a) wordt beschreven, of zelfs in de toelichting moet worden vermeld zoals beschreven in alinea 28(b), omdat zij direct met de fondsbeleggingen zal worden vergeleken en een dergelijke vergelijking mogelijk niet geldig is. Zij beweren dat actuarissen de actuariële contante waarde van toegezegde pensioenrechten niet noodzakelijk vergelijken met de marktwaarde van beleggingen, maar een beoordeling geven van de contante waarde van kasstromen die naar verwachting zullen voortvloeien uit de beleggingen. Voorstanders van deze indeling zijn bijgevolg van mening dat een dergelijke vergelijking de algemene beoordeling van de regeling door de actuaris wellicht niet weerspiegelt en dat deze verkeerd kan worden geïnterpreteerd. Ook zijn sommigen van mening dat de informatie over toegezegde pensioenrechten – al dan niet gekwantificeerd – alleen in een afzonderlijk actuarieel verslag moet worden opgenomen waarin een geëigende verklaring kan worden geboden. 31 Deze standaard accepteert de meningen die pleiten voor het toestaan van informatieverschaffing over toegezegde pensioenrechten in een afzonderlijk actuarieel verslag. Hij verwerpt argumenten tegen de kwantificering van de actuariële contante waarde van toegezegde pensioenrechten. Bijgevolg worden de indelingen die in alinea 28(a) en (b) zijn beschreven ingevolge deze standaard aanvaardbaar geacht, evenals de indeling die is beschreven in alinea 28(c) op voorwaarde dat de financiële overzichten een verwijzing bevatten naar een actuarieel verslag waarin de actuariële contante waarde van toegezegde pensioenrechten is opgenomen en dat bij de financiële overzichten is gevoegd.

## Alle Regelingen

Waardering van fondsbeleggingen 32 Beleggingen in het kader van pensioenregelingen moeten worden gewaardeerd tegen reële waarde. Voor verhandelbare effecten is de reële waarde de marktwaarde. Indien fondsbeleggingen worden gehouden waarvan de reële waarde niet kan worden geschat, moet worden vermeld waarom de reële waarde niet is gebruikt. 33 Voor verhandelbare effecten is de reële waarde gewoonlijk gelijk aan de marktwaarde, omdat deze wordt beschouwd als de meest nuttige maatstaf voor de effecten op het einde van de verslagperiode en voor de beleggingsprestaties over de periode. Effecten met een vaste inkoopwaarde en die zijn verworven om te worden toegerekend aan de verplichtingen van de regeling of bepaalde onderdelen daarvan, mogen worden geboekt tegen bedragen die geba seerd zijn op hun uiteindelijke inkoopwaarde, uitgaande van een constant rendement tot de vervaldatum. Indien fondsbeleggingen worden gehouden waarvan de reële waarde niet kan worden geschat, zoals het bezit van 100 % van een entiteit, moet worden vermeld waarom de reële waarde niet is gebruikt. In zoverre beleggingen worden geboekt tegen andere bedragen dan de marktwaarde of de reële waarde, wordt doorgaans ook de reële waarde vermeld. Activa die worden gebruikt in de activiteiten van het fonds worden administratief verwerkt in overeen stemming met de toepasselijke International Accounting Standards.

## Informatieverschaffing

34 In de jaarrekening van een pensioenregeling, ongeacht of het toegezegdpensioenregelingen of toegezegde bijdrageregelingen betreft, moet eveneens de volgende informatie worden vermeld:
(a) een mutatieoverzicht van de nettoactiva beschikbaar voor uitkeringen;
(b) informatie over de grondslagen voor financiële verslaggeving die van materieel belang is; en
(c) een beschrijving van de regeling en de gevolgen van enigerlei wijzigingen aan de regeling die tijdens de periode hebben plaatsgevonden.

35 In de financiële overzichten van pensioenregelingen moet, indien van toepassing, de volgende informatie worden verstrekt:
(a) een overzicht van de nettoactiva beschikbaar voor uitkeringen met vermelding van:
(i) de activa aan het eind van de periode, in een gepaste classificatie;
(ii) de grondslag voor de waardering van activa;
(iii) details over afzonderlijke beleggingen die meer dan 5 % uitmaken van de nettoactiva beschikbaar voor uitkeringen of 5 % van enigerlei klasse of soort van effecten;
(iv) details van enigerlei belegging in de werkgever; en
(v) alle andere verplichtingen dan de actuariële contante waarde van toegezegde pensioenrechten;
(b) een mutatieoverzicht van de nettoactiva beschikbaar voor uitkeringen met vermelding van het volgende:
(i) de werkgeversbijdragen;
(ii) de werknemersbijdragen;
(iii) beleggingsinkomsten, zoals rente en dividenden;
(iv) overige baten;
(v) betaalde of te betalen uitkeringen (bijvoorbeeld geanalyseerd als pensioen-, overlijdens- en invaliditeits uitkeringen en forfaitaire betalingen);
(vi) beheerskosten;
(vii) overige lasten;
(viii) winstbelastingen;
(ix) winsten en verliezen uit de vervreemding van beleggingen en wijzigingen in de waarde van beleggingen; en
(x) overdrachten vanuit en aan andere regelingen;
(c) een beschrijving van het financieringsbeleid;
(d) voor toegezegdpensioenregelingen: de actuariële contante waarde van toegezegde pensioenrechten (waarbij een onderscheid kan worden gemaakt tussen onvoorwaardelijk toegezegde beloningen en niet onvoorwaardelijk toegezegde beloningen) op basis van de uitkeringen die uit hoofde van de bepalingen van de regeling zijn toegezegd voor tot dan toe verrichte arbeidsprestaties, en die bepaald is op basis van het actuele of voorspelde loonniveau; deze informatie kan worden opgenomen in een bijgevoegd actuarieel verslag dat samen met de gerelateerde financiële overzichten moet worden gelezen; en

(e) voor toegezegdpensioenregelingen: een beschrijving van de belangrijke actuariële veronderstellingen die zijn gedaan en de methode die is gebruikt om de actuariële contante waarde van toegezegde pensioenrechten te berekenen. 36 Het verslag van een pensioenregeling omvat een beschrijving van de regeling, hetzij als onderdeel van de financiële overzichten, hetzij in een afzonderlijk verslag. Het kan het volgende omvatten:
(a) de namen van de werkgevers en de groepen van werknemers die zijn gedekt;
(b) het aantal deelnemers dat uitkeringen ontvangt en het aantal andere deelnemers, in een gepaste classificatie;
(c) het type regeling – toegezegdebijdrageregeling of toegezegdpensioenregeling;
(d) een toelichting waarin vermeld wordt of deelnemers bijdragen leveren aan de regeling;
(e) een beschrijving van de pensioenrechten die aan de deelnemers zijn toegezegd;
(f) een beschrijving van de eventuele beëindigingsvoorwaarden van de regeling; en
(g) wijzigingen in de items onder (a) tot (f) tijdens de verslagperiode. Het is niet ongebruikelijk om te verwijzen naar andere documenten die op eenvoudige wijze beschikbaar zijn voor gebruikers en waarin de regeling wordt beschreven, en alleen informatie op te nemen over daaropvolgende wijzi gingen.

## Ingangsdatum

37 Deze standaard wordt van kracht voor jaarrekeningen van pensioenregelingen die betrekking hebben op verslagpe rioden die op of na 1 januari 1988 aanvangen. 38 Informatieverschaffing over de grondslagen voor financiële verslaggeving, die IAS 1 Presentatie van de jaarrekeningen en IFRS Practice Statement 2 Making Materiality Judgements wijzigt, en in februari 2021 is uitgegeven, wijzigde alinea 34. Entiteiten moeten deze wijziging toepassen op jaarlijkse verslagperioden die op of na 1 januari 2023 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit de wijziging op een eerdere periode toepast, moet zij dit feit vermelden.
