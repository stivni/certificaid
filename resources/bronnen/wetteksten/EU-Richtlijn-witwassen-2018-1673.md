---
bijgewerkt: 12.11.2018
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: normatief
chunk:
  level: 2
  sub_strategy:
  type: Art.
itaa-lex-sectie: ''
provenance:
  inputs:
    - id: resources/raw/wetteksten/EU-Richtlijn-witwassen-2018-1673.pdf
      sha256: 5ddc01ecaee55f528a3a359f734cbab5c30d0077178d052830d13bcba2a0db8a
      version: 12.11.2018
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:56:15Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:56:58Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A7/B5: de heading-structuur is ernstig verward door 2-kolom extractie. Artikel-titels staan ACHTER de artikelinhoud in plaats van ervoor: zo staat de body-tekst van Art. 4 t/m Art. 10 op regels 227-311, terwijl de bijbehorende ###### headings ('Artikel 4. Medeplichtigheid...', 'Artikel 5. Sancties...') pas op regels 249-325 verschijnen — de opmaak-kolom rechts met de korte artikel-titels is later in de body ingevoerd dan de inhoud-kolom links. Dit maakt de structuur onleesbaar voor RAG."
    layer1:
      file_size_chars: 39811
      flags: []
      heading_count: 16
      max_section_chars: 20441
      run_at: '2026-05-11T16:52:50Z'
      run_id: 20260511-165250
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:56:58Z'
      rationale: "A7/B5: de heading-structuur is ernstig verward door 2-kolom extractie. Artikel-titels staan ACHTER de artikelinhoud in plaats van ervoor: zo staat de body-tekst van Art. 4 t/m Art. 10 op regels 227-311, terwijl de bijbehorende ###### headings ('Artikel 4. Medeplichtigheid...', 'Artikel 5. Sancties...') pas op regels 249-325 verschijnen — de opmaak-kolom rechts met de korte artikel-titels is later in de body ingevoerd dan de inhoud-kolom links. Dit maakt de structuur onleesbaar voor RAG."
      concrete_problemen:
        - regel: 227
          categorie: A7
          type: scrambled-words
          voorbeeld: 1. De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de hierna genoemde omstandigheden... [dit is Art. 6 inhoud, maar Art. 6 heading staat pas op r.257]
        - regel: 233
          categorie: A7
          type: scrambled-words
          voorbeeld: 1. De lidstaten nemen de nodige maatregelen... [Art. 7 inhoud voor heading Art. 7 op r.261]
        - regel: 245
          categorie: A7
          type: scrambled-words
          voorbeeld: 1. De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat rechtspersonen aansprakelijk kunnen worden gesteld... [Art. 7 body voor heading]
        - regel: 249
          categorie: B5
          type: other
          voorbeeld: '###### Artikel 4 Medeplichtigheid, uitlokking en poging [heading na content van Art.4]'
        - regel: 273
          categorie: A7
          type: scrambled-words
          voorbeeld: De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat een rechtspersoon... [Art. 8 body voor heading op r.315]
        - regel: 327
          categorie: A7
          type: scrambled-words
          voorbeeld: 1. Elke lidstaat neemt de nodige maatregelen om zijn rechtsmacht te vestigen... [Art. 10 body voor heading op r.323]
        - regel: 349
          categorie: B5
          type: other
          voorbeeld: '###### Artikel 11 Onderzoeksmiddelen [heading na body-tekst van Art.11 op r.327]'
status: beschikbaar
tags:
  - '1.2'
  - '4.0'
wet: Richtlijn (EU) 2018/1673 van het Europees Parlement en de Raad van 23 oktober 2018 inzake de strafrechtelijke bestrijding van het witwassen van geld
---

# Richtlijn (EU) 2018/1673 van het Europees Parlement en de Raad van 23 oktober 2018 inzake de strafrechtelijke bestrijding van het witwassen van geld

*Bijgewerkt tot en met 12.11.2018 — gecoördineerde versie.*

RICHTLIJNEN

RICHTLIJN (EU) 2018/1673 VAN HET EUROPEES PARLEMENT EN DE RAAD

van 23 oktober 2018

inzake de strafrechtelijke bestrijding van het witwassen van geld

HET EUROPEES PARLEMENT EN DE RAAD VAN DE EUROPESE UNIE,

Gezien het Verdrag betreffende de werking van de Europese Unie, en met name artikel 83, lid 1,

Gezien het voorstel van de Europese Commissie,

Na toezending van het ontwerp van wetgevingshandeling aan de nationale parlementen,

Handelend volgens de gewone wetgevingsprocedure ( 1 ),

Overwegende hetgeen volgt:

(1)  Het witwassen van geld en de daarmee verband houdende financiering van terrorisme en georganiseerde misdaad  blijven aanzienlijke problemen op het niveau van de Unie, waardoor afbreuk wordt gedaan aan de integriteit, de  stabiliteit en de reputatie van de financiële sector, en de interne markt en de interne veiligheid van de Unie worden  bedreigd. Om deze problemen aan te pakken en om Richtlijn (EU) 2015/849 van het Europees Parlement en de  Raad ( 2 ) aan te vullen en de toepassing ervan kracht bij te zetten, beoogt deze richtlijn het witwassen van geld  strafrechtelijk te bestrijden, zodat een doeltreffendere en snellere grensoverschrijdende samenwerking tussen de  bevoegde autoriteiten mogelijk wordt.

(2)  Maatregelen die uitsluitend op nationaal niveau of zelfs op Unieniveau worden getroffen zonder internationale  coördinatie en samenwerking, zouden een zeer beperkte uitwerking hebben. De door de Unie ter bestrijding van  het witwassen van geld vastgestelde maatregelen dienen derhalve verenigbaar te zijn met en minstens even streng  te zijn als andere in internationale fora ondernomen acties.

(3)  Bij het optreden van de Unie moet in het bijzonder rekening worden gehouden met de aanbevelingen van de  Financiëleactiegroep (Financial Action Task Force — FATF) en met de instrumenten van andere internationale  organisaties en organen voor de bestrijding van het witwassen van geld en terrorismefinanciering. De relevante  Unierechtshandelingen moeten in voorkomend geval verder in overeenstemming worden gebracht met de inter nationale normen voor de bestrijding van het witwassen van geld en de financiering van terrorisme en proliferatie,  die in februari 2012 zijn aangenomen door de FATF (de „herziene FATF-aanbevelingen”). Als ondertekenaar van  het Verdrag van de Raad van Europa inzake het witwassen, de opsporing, de inbeslagneming en de confiscatie van  opbrengsten van misdrijven en de financiering van terrorisme dient de Unie de voorschriften van dat verdrag in  haar rechtsorde om te zetten.

(4)  Kaderbesluit 2001/500/JBZ van de Raad ( 3 ) bevat voorschriften inzake de strafbaarstelling van het witwassen van  geld. Dat kaderbesluit is echter te beperkt en de huidige strafbaarstelling van het witwassen van geld is niet  coherent genoeg om witwassen in de hele Unie te bestrijden, wat zorgt voor handhavingslacunes en belemme ringen voor de samenwerking tussen de bevoegde autoriteiten in de verschillende lidstaten.

( 1 ) Standpunt van het Europees Parlement van 12 september 2018 (nog niet bekendgemaakt in het Publicatieblad) en besluit van de  Raad van 11 oktober 2018.  ( 2 ) Richtlijn (EU) 2015/849 van het Europees Parlement en de Raad van 20 mei 2015 inzake de voorkoming van het gebruik van het  financiële stelsel voor het witwassen van geld of terrorismefinanciering, tot wijziging van Verordening (EU) nr. 648/2012 van het  Europees Parlement en de Raad en tot intrekking van Richtlijn 2005/60/EG van het Europees Parlement en de Raad en Richtlijn  2006/70/EG van de Commissie (PB L 141 van 5.6.2015, blz. 73).  ( 3 ) Kaderbesluit 2001/500/JBZ van de Raad van 26 juni 2001 inzake het witwassen van geld, de identificatie, opsporing, bevriezing,  inbeslagneming en confiscatie van hulpmiddelen en van opbrengsten van misdrijven (PB L 182 van 5.7.2001, blz. 1).

(5)  De definitie van criminele activiteiten die basisdelicten voor het witwassen van geld vormen, moet voldoende  uniform zijn in alle lidstaten. De lidstaten moeten ervoor zorgen dat alle strafbare feiten waarop een gevangenis straf van een bij deze richtlijn bepaalde duur staat als basisdelicten voor het witwassen van geld worden be schouwd. Voorts moeten de lidstaten, voor zover de toepassing van die strafdrempels hierin nog niet voorziet, een  reeks strafbare feiten opnemen in elk van de in deze richtlijn vermelde categorieën van strafbare feiten. In dat geval  moeten de lidstaten kunnen bepalen hoe zij de reeks strafbare feiten binnen elke categorie afbakenen. Wanneer een  categorie van strafbare feiten zoals terrorisme of milieudelicten, strafbare feiten omvat die in de Unierechtshan delingen zijn opgenomen, moet deze richtlijn naar die rechtshandelingen verwijzen. De lidstaten moeten evenwel  elk in die Unierechtshandelingen opgenomen strafbaar feit als basisdelict voor het witwassen van geld beschouwen.  Elke vorm van strafbare betrokkenheid bij het plegen van een basisdelict, als strafbaar gesteld conform het  nationale recht, moet voor de toepassing van deze richtlijn eveneens als een criminele activiteit worden beschouwd.  In gevallen waarin de lidstaten op grond van het Unierecht in andere sancties dan strafrechtelijke sancties kunnen  voorzien, mag deze richtlijn de lidstaten er niet toe verplichten om de strafbare feiten in die gevallen voor de  toepassing van deze richtlijn als basisdelicten aan te merken.

(6)  Het gebruik van virtuele valuta brengt, vanuit het oogpunt van de bestrijding van het witwassen van geld, nieuwe  risico’s en uitdagingen met zich mee. De lidstaten moeten ervoor zorgen dat die risico’s op passende wijze worden  aangepakt.

(7)  In verband met de gevolgen die door bekleders van openbare ambten gepleegde witwasdelicten kunnen hebben  voor de publieke ruimte en voor de integriteit van openbare instellingen, moeten de lidstaten kunnen overwegen  om in hun nationale kaders en in overeenstemming met hun nationale rechtstradities voor bekleders van openbare  ambten strengere sancties in te voeren.

(8)  In overeenstemming met de herziene FATF-aanbevelingen moeten fiscale misdrijven in verband met directe en  indirecte belastingen ook onder de definitie van criminele activiteit vallen. Aangezien verschillende fiscale mis drijven in elke lidstaat een criminele activiteit kunnen vormen die kan worden bestraft met de in deze richtlijn  bedoelde sancties, kunnen de definities van fiscale misdrijven in het nationaal recht verschillen. Deze richtlijn  beoogt echter niet de definities van fiscale misdrijven in het nationale recht te harmoniseren.

(9)  De lidstaten moeten elkaar in het kader van strafrechtelijke procedures met betrekking tot het witwassen van geld  zo veel mogelijk ondersteunen en ervoor zorgen dat er tijdig en op doeltreffende wijze informatie wordt uit gewisseld, een en ander in overeenstemming met het nationale recht en het bestaande rechtskader van de Unie.  Onderlinge verschillen tussen de lidstaten wat betreft de nationaalrechtelijke definities van basisdelicten mogen  geen belemmering vormen voor internationale samenwerking in strafzaken met betrekking tot het witwassen van  geld. De samenwerking met derde landen moet worden geïntensiveerd, met name door de vaststelling van  doeltreffende maatregelen en mechanismen ter bestrijding van het witwassen van geld te stimuleren en te onder steunen en door betere internationale samenwerking op dit gebied te waarborgen.

(10)  Deze richtlijn is niet van toepassing op het witwassen van geld waarbij voorwerpen betrokken zijn die afkomstig  zijn uit strafbare feiten waardoor de financiële belangen van de Unie worden geschaad, waarvoor de specifieke  bepalingen van Richtlijn (EU) 2017/1371 van het Europees Parlement en de Raad ( 1 ) gelden. Hiermee wordt geen  afbreuk gedaan aan de mogelijkheid van de lidstaten om deze richtlijn en Richtlijn (EU) 2017/1371 om te zetten  in één overkoepelend kader op nationaal niveau. Overeenkomstig artikel 325, lid 2, van het Verdrag betreffende de  werking van de Europese Unie (VWEU), moeten de lidstaten ter bestrijding van fraude waardoor de financiële  belangen van de Unie worden geschaad, dezelfde maatregelen nemen als die welke zij treffen ter bestrijding van  fraude waardoor hun eigen financiële belangen worden geschaad.

(11)  De lidstaten moeten ervoor zorgen dat bepaalde soorten witwasactiviteiten ook strafbaar zijn wanneer zij worden  verricht door de pleger van de criminele activiteit waarmee het voorwerp is verkregen („self-laundering”). In zulke  gevallen, waarin de witwasactiviteiten niet slechts neerkomen op enkel bezit of gebruik, maar ook de overdracht,  de omzetting, het verhelen of verhullen van voorwerpen betreffen, en resulteren in verdere schade dan die welke  reeds door de criminele activiteit is veroorzaakt, bijvoorbeeld door het door criminele activiteiten verkregen  voorwerp in het verkeer te brengen en aldus de onrechtmatige herkomst ervan te verhelen, moet die witwas activiteit strafbaar worden gesteld.

( 1 ) Richtlijn (EU) 2017/1371 van het Europees Parlement en de Raad van 5 juli 2017 betreffende de strafrechtelijke bestrijding van  fraude die de financiële belangen van de Unie schaadt (PB L 198 van 28.7.2017, blz. 29).

(12)  Om ervoor te zorgen dat strafrechtelijke maatregelen tegen het witwassen van geld doeltreffend zijn, moet,  rekening houdend met alle relevante omstandigheden en bewijzen, een veroordeling mogelijk zijn zonder dat  daarvoor exact dient te worden vastgesteld met welke criminele activiteit het voorwerp is verkregen, of zonder dat  er sprake dient te zijn van een eerdere of gelijktijdige veroordeling voor die criminele activiteit. Overeenkomstig  hun nationale rechtsstelsel moeten de lidstaten hiervoor kunnen zorgen met andere middelen dan wetgeving.  Vervolging wegens het witwassen van geld mag ook niet worden belemmerd door het feit dat de criminele  activiteit werd gepleegd in een andere lidstaat of in een derde land, onder de voorwaarden van deze richtlijn.

(13)  Deze richtlijn beoogt het witwassen van geld strafbaar te stellen wanneer het opzettelijk heeft plaatsgevonden en in  de wetenschap dat het voorwerp uit criminele activiteiten werd verkregen. In die context mag deze richtlijn geen  onderscheid maken tussen situaties waarin een voorwerp rechtstreeks uit criminele activiteiten is verkregen en  situaties waarin het indirect uit criminele activiteiten is verkregen, in overeenstemming met de ruime definitie van  „opbrengsten” in Richtlijn 2014/42/EU van het Europees Parlement en de Raad ( 1 ). In ieder geval moet bij het  beoordelen of het voorwerp uit criminele activiteit is verkregen en of de betrokkene dit wist, rekening worden  gehouden met de specifieke omstandigheden van de zaak, zoals het feit dat de waarde van het voorwerp niet in  verhouding staat tot het legale inkomen van de beklaagde of het feit dat de criminele activiteit en de verwerving  van het voorwerp hebben plaatsgevonden binnen hetzelfde tijdsbestek. Opzet en wetenschap kunnen worden  afgeleid uit objectieve, feitelijke omstandigheden. Aangezien deze richtlijn voorziet in minimumvoorschriften  inzake de definitie van strafbare feiten en in sancties op het gebied van het witwassen van geld, staat het de  lidstaten vrij om strengere strafrechtelijke bepalingen op dat gebied vast te stellen of te handhaven. lidstaten  moeten bijvoorbeeld kunnen bepalen dat het roekeloos of als gevolg van ernstige nalatigheid witwassen van  geld een strafbaar feit vormt. Verwijzingen in deze richtlijn naar het witwassen van geld als gevolg van nalatigheid  moeten als zodanig worden opgevat voor de lidstaten die dergelijk gedrag strafbaar stellen.

(14)  Teneinde het witwassen van geld in de hele Unie tegen te gaan, moeten de lidstaten ervoor zorgen dat dit strafbaar  wordt gesteld met een maximumgevangenisstraf van ten minste vier jaar. Die verplichting doet geen afbreuk aan de  individualisering en de toepassing van sancties en de uitvoering van veroordelingen op grond van de concrete  omstandigheden van elk afzonderlijk geval. De lidstaten moeten ook voorzien in bijkomende sancties of maat regelen, zoals boeten, tijdelijke of permanente uitsluiting van toegang tot overheidsfinanciering, waaronder aan bestedingsprocedures, subsidies en concessies, een tijdelijk verbod op het uitoefenen van commerciële activiteiten  of een tijdelijk verbod op kandidaatstelling voor een verkozen of openbaar ambt. Die verplichting doet geen  afbreuk aan de vrijheid van de rechter of de rechtbank om te bepalen of er, rekening houdend met alle om standigheden van het concrete geval, al dan niet bijkomende sancties of maatregelen moeten worden opgelegd.

(15)  Hoewel er geen verplichting bestaat om hogere straffen op te leggen, moeten de lidstaten ervoor zorgen dat de  rechter of de rechtbank de in deze richtlijn omschreven verzwarende omstandigheden kan laten meewegen bij de  veroordeling van daders. Het behoort tot de beoordelingsvrijheid van de rechter of de rechtbank om te bepalen of  de specifieke verzwarende omstandigheden worden meegewogen, rekening houdend met alle feiten van het con crete geval. De lidstaten mogen niet verplicht zijn in verzwarende omstandigheden te voorzien wanneer in het  nationale recht is bepaald dat de strafbare feiten als vermeld in Kaderbesluit 2008/841/JBZ van de Raad ( 2 ) of  strafbare feiten die door als meldingsplichtige optredende natuurlijke personen zijn gepleegd in het kader van de  uitoefening van hun beroepsactiviteiten, strafbaar moeten worden gesteld als afzonderlijke strafbare feiten en dit  strengere sancties tot gevolg kan hebben.

(16)  De bevriezing en de confiscatie van hulpmiddelen en opbrengsten van misdrijven doen de financiële prikkels voor  criminaliteit teniet. Richtlijn 2014/42/EU voorziet in minimumregels voor de bevriezing en confiscatie van hulp middelen en opbrengsten van misdrijven in strafzaken. Die richtlijn verlangt ook dat de Commissie verslag  uitbrengt aan het Europees Parlement en de Raad over de uitvoering ervan en, indien nodig, dat zij passende  voorstellen indient. De lidstaten moeten ten minste de bevriezing en confiscatie van hulpmiddelen en opbrengsten  van misdrijven waarborgen in alle in Richtlijn 2014/42/EU bedoelde gevallen. Daarnaast moeten de lidstaten  serieus nadenken over het mogelijk maken van confiscatie in alle gevallen waarin er geen strafrechtelijke procedure  kan worden ingeleid of afgerond, waaronder gevallen waarin de dader overleden is. De Commissie zal, in een  verklaring bij Richtlijn 2014/42/EU, overeenkomstig het verzoek van het Europees Parlement en de Raad, een  verslag indienen met een analyse van de haalbaarheid en mogelijke voordelen van invoering van nadere gemeen schappelijke regels voor de confiscatie van voorwerpen die afkomstig zijn van activiteiten van criminele aard, ook  bij ontstentenis van een veroordeling van een specifieke persoon of specifieke personen voor die activiteiten. Bij die  analyse zal rekening worden gehouden met de verschillen tussen de rechtstradities en rechtsstelsels van de lidstaten.

( 1 ) Richtlijn 2014/42/EU van het Europees Parlement en de Raad van 3 april 2014 betreffende de bevriezing en confiscatie van  hulpmiddelen en opbrengsten van misdrijven in de Europese Unie (PB L 127 van 29.4.2014, blz. 39).  ( 2 ) Kaderbesluit 2008/841/JBZ van de Raad van 24 oktober 2008 ter bestrijding van georganiseerde criminaliteit (PB L 300 van  11.11.2008, blz. 42).

(17)  Gelet op de mobiliteit van de plegers en de opbrengsten van criminele activiteiten, alsmede op de complexe  grensoverschrijdende onderzoeken die nodig zijn om het witwassen van geld te bestrijden, moeten alle lidstaten  hun rechtsmacht zodanig vaststellen dat de bevoegde autoriteiten dergelijke activiteiten kunnen onderzoeken en  vervolgen. De lidstaten moeten er daarbij voor zorgen dat hun rechtsmacht zich uitstrekt tot situaties waarin een  strafbaar feit met behulp van informatie- en communicatietechnologie vanaf hun grondgebied is gepleegd, on geacht of die technologie zich al dan niet op hun grondgebied bevindt.

(18)  Krachtens Kaderbesluit 2009/948/JBZ ( 1 ) en Besluit 2002/187/JBZ van de Raad ( 2 ) moeten de bevoegde autoriteiten  van twee of meer lidstaten waar parallelle strafprocedures worden gevoerd wegens dezelfde feiten en ten aanzien  van dezelfde personen met de bijstand van Eurojust overgaan tot rechtstreeks onderling overleg, met name om te  waarborgen dat alle onder deze richtlijn vallende strafbare feiten worden vervolgd.

(19)  Om witwaszaken naar behoren te kunnen onderzoeken en vervolgen, moeten degenen die verantwoordelijk zijn  voor het onderzoek naar of de vervolging van zulke strafbare feiten, gebruik kunnen maken van doeltreffende  onderzoeksmiddelen, zoals die welke worden gebruikt bij de bestrijding van georganiseerde criminaliteit of andere  ernstige misdrijven. Daarbij moet worden gewaarborgd dat er voldoende personeel en gerichte scholing, middelen  en actuele technologische capaciteit beschikbaar zijn. Bij het gebruik van die middelen overeenkomstig het na tionale recht moet gericht worden gewerkt en moet rekening worden gehouden met het evenredigheidsbeginsel en  met de aard en de ernst van de strafbare feiten waarop het onderzoek betrekking heeft, en moet het recht op  bescherming van persoonsgegevens worden nageleefd.

(20)  Deze richtlijn vervangt een aantal bepalingen van Kaderbesluit 2001/500/JBZ voor de lidstaten die door deze  richtlijn gebonden zijn.

(21)  Deze richtlijn eerbiedigt de in artikel 2 van het Verdrag betreffende de Europese Unie (VEU) erkende beginselen,  eerbiedigt de grondrechten en de fundamentele vrijheden en neemt de met name in het Handvest van de grond rechten van de Europese Unie erkende beginselen in acht, waaronder die welke zijn neergelegd in de titels II, III, V  en VI daarvan, die onder meer betrekking hebben op het recht op eerbiediging van het privéleven en van het  familie- en gezinsleven, het recht op bescherming van persoonsgegevens, de beginselen inzake legaliteit en even redigheid van strafbare feiten en sancties, die ook het vereiste van nauwkeurigheid, duidelijkheid en voorzienbaar heid in het strafrecht omvatten, het vermoeden van onschuld alsmede het recht van verdachten en beklaagden op  toegang tot een advocaat, het recht om zichzelf niet te belasten en het recht op een eerlijk proces. Deze richtlijn  dient overeenkomstig die rechten en beginselen te worden toegepast, waarbij tevens rekening wordt gehouden met  het Europees Verdrag tot bescherming van de rechten van de mens en de fundamentele vrijheden, het Inter nationaal Verdrag inzake burgerrechten en politieke rechten en andere mensenrechtenverplichtingen uit hoofde van  het internationaal recht.

(22)  Daar de doelstelling van deze richtlijn, met name het stellen van doeltreffende, evenredige en afschrikkende  strafrechtelijke sancties in alle lidstaten op het witwassen van geld, niet voldoende door de lidstaten kan worden  verwezenlijkt, maar vanwege de omvang en de gevolgen van deze richtlijn beter door de Unie kan worden  verwezenlijkt, kan de Unie, overeenkomstig het in artikel 5 VEU neergelegde subsidiariteitsbeginsel, maatregelen  nemen. Overeenkomstig het in hetzelfde artikel neergelegde evenredigheidsbeginsel gaat deze richtlijn niet verder  dan nodig is om deze doelstelling te verwezenlijken.

(23)  Overeenkomstig de artikelen 1 en 2 van Protocol nr. 21 betreffende de positie van het Verenigd Koninkrijk en  Ierland ten aanzien van de ruimte van vrijheid, veiligheid en recht, gehecht aan het VEU en aan het VWEU, en  onverminderd artikel 4 van dat protocol, nemen het Verenigd Koninkrijk en Ierland niet deel aan de vaststelling  van deze richtlijn, die derhalve niet bindend is voor, noch van toepassing is in die lidstaten.

(24)  Overeenkomstig de artikelen 1 en 2 van Protocol nr. 22 betreffende de positie van Denemarken, gehecht aan het  VEU en het VWEU, neemt Denemarken niet deel aan de vaststelling van deze richtlijn, die derhalve niet bindend is  voor, noch van toepassing is in deze lidstaat. Kaderbesluit 2001/500/JBZ blijft bindend voor en van toepassing in  Denemarken,

HEBBEN DE VOLGENDE RICHTLIJN VASTGESTELD:

###### Artikel 1

Onderwerp en toepassingsgebied

1.  Deze richtlijn stelt minimumvoorschriften vast voor de definitie van strafbare feiten en sancties op het gebied van  het witwassen van geld.

( 1 ) Kaderbesluit 2009/948/JBZ van de Raad van 30 november 2009 over het voorkomen en beslechten van geschillen over de uit oefening van rechtsmacht bij strafprocedures (PB L 328 van 15.12.2009, blz. 42).  ( 2 ) Besluit 2002/187/JBZ van de Raad van 28 februari 2002 betreffende de oprichting van Eurojust teneinde de strijd tegen ernstige  vormen van criminaliteit te versterken (PB L 63 van 6.3.2002, blz. 1).

2.  Deze richtlijn is niet van toepassing op het witwassen van geld waarbij voorwerpen betrokken zijn die afkomstig  zijn uit strafbare feiten waardoor de financiële belangen van de Unie worden geschaad, waarvoor de specifieke bepalingen  van Richtlijn (EU) 2017/1371 gelden.

###### Artikel 2

Definities

Voor de toepassing van deze richtlijn wordt verstaan onder:

1. „criminele activiteit”: iedere vorm van criminele betrokkenheid bij het plegen van een strafbaar feit dat overeenkom stig het nationale recht strafbaar is gesteld met een maximale vrijheidsstraf of detentiemaatregel van meer dan een jaar  of, voor lidstaten die in hun rechtsstelsel een strafminimum voor strafbare feiten kennen, een strafbaar feit dat  strafbaar is gesteld met een minimale vrijheidsstraf of detentiemaatregel van meer dan zes maanden. In elk geval  worden strafbare feiten in de volgende categorieën als criminele activiteit aangemerkt:

a) deelname aan een georganiseerde criminele groep en racketeering, met inbegrip van elk strafbaar feit vermeld in  Kaderbesluit 2008/841/JBZ;

b) terrorisme, met inbegrip van elk strafbaar feit vermeld in Richtlijn (EU) 2017/541 van het Europees Parlement en  de Raad ( 1 );

c) mensenhandel en migrantensmokkel, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2011/36/EU van het  Europees Parlement en de Raad ( 2 ) en Kaderbesluit 2002/946/JBZ van de Raad ( 3 );

d) seksuele uitbuiting, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2011/93/EU van het Europees Parle ment en de Raad ( 4 );

e) illegale handel in verdovende middelen en psychotrope stoffen, met inbegrip van elk strafbaar feit vermeld in  Kaderbesluit 2004/757/JBZ van de Raad ( 5 );

f)  illegale wapenhandel;

g) illegale handel in gestolen goederen en andere goederen;

h) corruptie, met inbegrip van elk strafbaar feit vermeld in de Overeenkomst ter bestrijding van corruptie waarbij  ambtenaren van de Europese Gemeenschappen of van de lidstaten van de Europese Unie betrokken zijn ( 6 ) en in  Kaderbesluit 2003/568/JBZ van de Raad ( 7 );

i)  fraude, met inbegrip van elk strafbaar feit vermeld in Kaderbesluit 2001/413/JBZ van de Raad ( 8 );

( 1 ) Richtlijn (EU) 2017/541 van het Europees Parlement en de Raad van 15 maart 2017 inzake terrorismebestrijding en ter vervanging  van Kaderbesluit 2002/475/JBZ van de Raad en tot wijziging van Besluit 2005/671/JBZ van de Raad (PB L 88 van 31.3.2017, blz. 6).  ( 2 ) Richtlijn 2011/36/EU van het Europees Parlement en de Raad van 5 april 2011 inzake de voorkoming en bestrijding van mensen handel en de bescherming van slachtoffers daarvan, en ter vervanging van Kaderbesluit 2002/629/JBZ van de Raad (PB L 101 van  15.4.2011, blz. 1).  ( 3 ) Kaderbesluit 2002/946/JBZ van de Raad van 28 november 2002 tot versterking van het strafrechtelijk kader voor de bestrijding van  hulpverlening bij illegale binnenkomst, illegale doortocht en illegaal verblijf (PB L 328 van 5.12.2002, blz. 1).  ( 4 ) Richtlijn 2011/93/EU van het Europees Parlement en de Raad van 13 december 2011 ter bestrijding van seksueel misbruik en  seksuele uitbuiting van kinderen en kinderpornografie, en ter vervanging van Kaderbesluit 2004/68/JBZ van de Raad (PB L 335  van 17.12.2011, blz. 1).  ( 5 ) Kaderbesluit 2004/757/JBZ van de Raad van 25 oktober 2004 betreffende de vaststelling van minimumvoorschriften met betrekking  tot de bestanddelen van strafbare feiten en met betrekking tot straffen op het gebied van de illegale drugshandel (PB L 335 van  11.11.2004, blz. 8).  ( 6 ) Akte van de Raad van 26 mei 1997 tot opstelling op basis van artikel K.3, lid 2, onder c), van het Verdrag betreffende de Europese  Unie van de Overeenkomst ter bestrijding van corruptie waarbij ambtenaren van de Europese Gemeenschappen of van de lidstaten  van de Europese Unie betrokken zijn (PB C 195 van 25.6.1997, blz. 1).  ( 7 ) Kaderbesluit 2003/568/JBZ van de Raad van 22 juli 2003 inzake de bestrijding van corruptie in de privésector (PB L 192 van  31.7.2003, blz. 54).  ( 8 ) Kaderbesluit 2001/413/JBZ van de Raad van 28 mei 2001 betreffende de bestrijding van fraude en vervalsing in verband met andere  betaalmiddelen dan contanten (PB L 149 van 2.6.2001, blz. 1).

j)  valsemunterij, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2014/62/EU van het Europees Parlement en  de Raad ( 1 );

k) namaak van producten en productpiraterij;

l)  milieucriminaliteit, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2008/99/EG van het Europees Parle ment en de Raad ( 2 ) of elk strafbaar feit vermeld in Richtlijn 2009/123/EG van het Europees Parlement en de  Raad ( 3 );

m) moord en doodslag, zware mishandeling;

n) ontvoering, wederrechtelijke vrijheidsberoving en gijzeling;

o) roof of diefstal;

p) smokkel;

q) fiscale misdrijven met betrekking tot directe en indirecte belastingen, zoals neergelegd in het nationale recht;

r) afpersing;

s) vervalsing;

t)  piraterij;

u) handel met voorkennis en marktmanipulatie, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2014/57/EU  van het Europees Parlement en de Raad ( 4 );

v) cybercriminaliteit, met inbegrip van elk strafbaar feit vermeld in Richtlijn 2013/40/EU van het Europees Parle ment en de Raad ( 5 );

2. „voorwerp”: goederen van eender welke soort, lichamelijk dan wel onlichamelijk, roerend dan wel onroerend,  materieel dan wel immaterieel, en rechtsbescheiden of instrumenten in eender welke vorm, ook elektronisch of  digitaal, waaruit de eigendom of andere rechten ten aanzien van deze goederen blijken;

3. „rechtspersoon”: elke entiteit met rechtspersoonlijkheid krachtens het toepasselijke recht, met uitzondering van staten  of overheidsinstanties bij de uitoefening van hun staatsgezag en van publiekrechtelijke internationale organisaties.

###### Artikel 3

Witwasdelicten

1.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de volgende gedragingen strafbaar worden  gesteld indien er sprake is van opzet:

a) de omzetting of overdracht van voorwerpen, wetende dat deze uit een criminele activiteit zijn verkregen, met het  oogmerk de illegale herkomst ervan te verhelen of te verhullen of met het oogmerk een bij een dergelijke activiteit  betrokken persoon te helpen aan de rechtsgevolgen van zijn daden te ontkomen;

b) het verhelen of verhullen van de werkelijke aard, oorsprong, vindplaats, vervreemding, verplaatsing, rechten op of de  eigendom van voorwerpen, wetende dat deze uit een criminele activiteit zijn verkregen;

c) de verwerving, het bezit of het gebruik van voorwerpen, wetende, op het tijdstip van ontvangst, dat deze uit een  criminele activiteit zijn verkregen.

2.  De lidstaten kunnen de nodige maatregelen nemen om ervoor te zorgen dat de in lid 1 bedoelde gedragingen  strafbaar worden gesteld als de dader vermoedde of had moeten weten dat het voorwerp uit criminele activiteiten was  verkregen.

( 1 ) Richtlijn 2014/62/EU van het Europees Parlement en de Raad van 15 mei 2014 betreffende de strafrechtelijke bescherming van de  euro en andere munten tegen valsemunterij en ter vervanging van Kaderbesluit 2000/383/JBZ van de Raad (PB L 151 van 21.5.2014,  blz. 1).  ( 2 ) Richtlijn 2008/99/EG van het Europees Parlement en de Raad van 19 november 2008 inzake de bescherming van het milieu door  middel van het strafrecht (PB L 328 van 6.12.2008, blz. 28).  ( 3 ) Richtlijn 2009/123/EG van het Europees Parlement en de Raad van 21 oktober 2009 tot wijziging van Richtlijn 2005/35/EG inzake  verontreiniging vanaf schepen en invoering van sancties voor inbreuken (PB L 280 van 27.10.2009, blz. 52).  ( 4 ) Richtlijn 2014/57/EU van het Europees Parlement en de Raad van 16 april 2014 betreffende strafrechtelijke sancties voor markt misbruik (richtlijn marktmisbruik) (PB L 173 van 12.6.2014, blz. 179).  ( 5 ) Richtlijn 2013/40/EU van het Europees Parlement en de Raad van 12 augustus 2013 over aanvallen op informatiesystemen en ter  vervanging van Kaderbesluit 2005/222/JBZ van de Raad (PB L 218 van 14.8.2013, blz. 8).

3.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat:

a) een voorafgaande of gelijktijdige veroordeling voor de criminele activiteit waarmee het voorwerp is verkregen, geen  voorwaarde is voor een veroordeling voor de strafbare feiten bedoeld in de leden 1 en 2;

b) een veroordeling voor de in de leden 1 en 2 bedoelde strafbare feiten mogelijk is indien is aangetoond dat het  voorwerp uit een criminele activiteit is verkregen, zonder dat alle feitelijke elementen of alle omstandigheden in  verband met die criminele activiteit, waaronder de identiteit van de dader, aangetoond hoeven te worden;

c) de in de leden 1 en 2 bedoelde strafbare feiten ook betrekking hebben op voorwerpen die zijn verkregen uit  gedragingen die plaatsvonden op het grondgebied van een andere lidstaat of van een derde land, indien die gedra gingen een criminele activiteit zouden hebben gevormd mochten zij binnenslands hebben plaatsgevonden.

4.  In het geval lid 3, onder c), van dit artikel kunnen de lidstaten daarnaast verlangen dat de betrokken gedragingen  een strafbaar feit vormen krachtens het nationale recht van de andere lidstaat of van het derde land waar die gedragingen  werden gesteld, behalve als die gedragingen moeten worden aangemerkt als een van de in artikel 2, lid 1, onder a) tot en  met e) en h), bedoelde strafbare feiten en als omschreven in het toepasselijke Unierecht.

5.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de in lid 1, onder a) en onder b), bedoelde  gedragingen strafbaar worden gesteld indien zij worden gepleegd door personen die de criminele activiteit waaruit het  voorwerp is verkregen, hebben gepleegd of hierbij waren betrokken.

De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat medeplichtigheid aan, uitlokking van en poging tot  het plegen van een in artikel 3, leden 1 en 5, bedoeld feit strafbaar worden gesteld.

1.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de in de artikelen 3 en 4 bedoelde strafbare  feiten kunnen worden bestraft met doeltreffende, evenredige en afschrikkende strafrechtelijke sancties.

2.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de in artikel 3, leden 1 en 5, bedoelde strafbare  feiten strafbaar worden gesteld met een maximumgevangenisstraf van ten minste vier jaar.

3.  Daarnaast nemen de lidstaten de nodige maatregelen om ervoor te zorgen dat natuurlijke personen die strafbare  feiten als bedoeld in de artikelen 3 en 4, hebben gepleegd, waar nodig, onderworpen worden aan aanvullende sancties of  maatregelen.

1.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de hierna genoemde omstandigheden met  betrekking tot de in artikel 3, leden 1 en 5, en artikel 4 bedoelde strafbare feiten als verzwarende omstandigheid worden  beschouwd wanneer:

a) het strafbare feit werd gepleegd in het kader van een criminele organisatie in de zin van Kaderbesluit 2008/841/JBZ, of

b) de dader een meldingsplichtige entiteit is in de zin van artikel 2 van Richtlijn (EU) 2015/849 en het strafbare feit heeft  gepleegd in het kader van de uitoefening van zijn beroepsactiviteiten.

2.  De lidstaten kunnen bepalen dat de hierna genoemde omstandigheden met betrekking tot de in artikel 3, leden 1  en 5, en artikel 4, bedoelde strafbare feiten als verzwarende omstandigheden worden beschouwd:

a) het witgewassen voorwerp heeft een aanzienlijke waarde, of

b) het witgewassen voorwerp is afkomstig van een van de in artikel 2, punt 1), onder a) tot en met e) en h), bedoelde  strafbare feiten.

1.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat rechtspersonen aansprakelijk kunnen worden  gesteld voor alle in artikel 3, leden 1 en 5, en artikel 4 genoemde strafbare feiten die in hun voordeel zijn gepleegd door  personen die individueel dan wel als lid van een orgaan van de rechtspersoon optreden en die in de rechtspersoon een  leidende functie bekleden op grond van:

a) een bevoegdheid om de rechtspersoon te vertegenwoordigen;

###### Artikel 4

Medeplichtigheid, uitlokking en poging

###### Artikel 5

Sancties voor natuurlijke personen

###### Artikel 6

Verzwarende omstandigheden

###### Artikel 7

Aansprakelijkheid van rechtspersonen

b) een bevoegdheid om namens de rechtspersoon beslissingen te nemen, of

c) een bevoegdheid om binnen de rechtspersoon controle uit te oefenen.

2.  De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat rechtspersonen aansprakelijk kunnen worden  gesteld indien als gevolg van een gebrek aan toezicht of controle door een in lid 1 van dit artikel bedoelde persoon, een  van de in artikel 3, leden 1 en 5, en artikel 4 genoemde strafbare feiten kon worden gepleegd ten voordele van die  rechtspersoon door een persoon die onder diens gezag staat.

3.  De aansprakelijkheid van rechtspersonen krachtens de leden 1 en 2 van dit artikel staat niet in de weg van straf rechtelijke vervolging van natuurlijke personen die een van de in artikel 3, leden 1 en 5, en artikel 4 bedoelde strafbare  feiten plegen, daartoe aanzetten of eraan medeplichtig zijn.

De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat een rechtspersoon die op grond van artikel 7  aansprakelijk is gesteld, kan worden gestraft met doeltreffende, evenredige en afschrikkende sancties, waaronder al dan  niet strafrechtelijke geldboeten en eventuele andere sancties, zoals:

a) uitsluiting van door de overheid verleende voordelen of steun;

b) tijdelijke of permanente uitsluiting van toegang tot overheidsfinanciering, waaronder aanbestedingsprocedures, subsi dies en concessies;

c) een tijdelijk of permanent verbod op het uitoefenen van commerciële activiteiten;

d) plaatsing onder toezicht van de rechter;

e) een rechterlijk bevel tot liquidatie;

f) tijdelijke of permanente sluiting van vestigingen die zijn gebruikt voor het plegen van het strafbare feit.

De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat hun bevoegde autoriteiten in overeenstemming met  Richtlijn 2014/42/EU in voorkomend geval de opbrengsten van en de hulpmiddelen die werden gebruikt of bestemd  waren om te worden gebruikt bij het plegen of het bijdragen aan het plegen van een van de in deze richtlijn genoemde  strafbare feiten, bevriezen of in beslag nemen.

1.  Elke lidstaat neemt de nodige maatregelen om zijn rechtsmacht te vestigen ten aanzien van de in de artikelen 3 en 4  bedoelde strafbare feiten, indien:

a) het strafbare feit geheel of gedeeltelijk op het grondgebied van die lidstaat is gepleegd;

b) het strafbare feit door een van zijn onderdanen is gepleegd.

2.  Een lidstaat stelt de Commissie in kennis van zijn besluit om zijn rechtsmacht uit te breiden naar in de artikelen 3  en 4 bedoelde strafbare feiten die buiten zijn grondgebied zijn gepleegd, indien:

a) de dader zijn gewone verblijfplaats op het grondgebied van die lidstaat heeft;

b) het strafbare feit is gepleegd ten voordele van een op het grondgebied van die lidstaat gevestigde rechtspersoon.

3.  Indien meer dan één lidstaat rechtsmacht heeft ten aanzien van een in de artikelen 3 en 4 bedoeld strafbaar feit en  elk van hen ten aanzien van dezelfde feiten op geldige wijze vervolging kan instellen, bepalen de betrokken lidstaten in  onderling overleg welk van hen de dader zal vervolgen, teneinde de procedure in één lidstaat te concentreren.

Daarbij wordt rekening gehouden met de volgende factoren:

a) het grondgebied van de lidstaat waar het strafbare feit is gepleegd;

b) de nationaliteit of verblijfplaats van de dader;

c) het land van oorsprong van het slachtoffer of de slachtoffers, en

d) het grondgebied waarop de dader werd aangetroffen.

In voorkomend geval wordt de zaak overeenkomstig artikel 12 van Kaderbesluit 2009/948/JBZ naar Eurojust verwezen.

###### Artikel 8

Sancties voor rechtspersonen

###### Artikel 9

Confiscatie

###### Artikel 10

Rechtsmacht

De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat doeltreffende onderzoeksmiddelen, zoals die welke  worden gebruikt bij de bestrijding van georganiseerde of andere zware criminaliteit, ter beschikking staan van personen,  eenheden of diensten die bevoegd zijn voor het onderzoeken of vervolgen van de in artikel 3, leden 1 en 5, en artikel 4  bedoelde strafbare feiten.

Vervanging van een aantal bepalingen van Kaderbesluit 2001/500/JBZ

Deze richtlijn komt in de plaats van artikel 1, onder b), en artikel 2 van Kaderbesluit 2001/500/JBZ ten aanzien van de  lidstaten die door deze richtlijn gebonden zijn, onverminderd de verplichtingen van die lidstaten met betrekking tot de  termijn voor de omzetting van dat kaderbesluit in nationaal recht.

Voor de lidstaten die gebonden zijn door deze richtlijn, gelden verwijzingen naar de bepalingen in het eerste lid van het  Kaderbesluit 2001/500/JBZ als verwijzingen naar deze richtlijn.

1.  De lidstaten doen de nodige wettelijke en bestuursrechtelijke bepalingen in werking treden om uiterlijk 3 december  2020 aan deze richtlijn te voldoen. Zij delen de Commissie de tekst van die bepalingen onverwijld mee.

Wanneer de lidstaten die bepalingen aannemen, wordt in die bepalingen zelf of bij de officiële bekendmaking daarvan  naar deze richtlijn verwezen. De regels voor de verwijzing worden vastgesteld door de lidstaten.

2.  De lidstaten delen de Commissie de tekst van de belangrijkste bepalingen van intern recht mede die zij op het onder  deze richtlijn vallende gebied vaststellen.

De Commissie dient uiterlijk 3 december 2022 een verslag in bij het Europees Parlement en de Raad waarin wordt  beoordeeld in hoeverre de lidstaten de nodige maatregelen hebben genomen om aan deze richtlijn te voldoen.

Voorts dient de Commissie uiterlijk 3 december 2023 een verslag in bij het Europees Parlement en de Raad waarin een  beoordeling wordt verricht van de toegevoegde waarde van deze richtlijn voor de bestrijding van het witwassen van geld  alsmede van de gevolgen van deze richtlijn voor de fundamentele rechten en vrijheden. Indien nodig dient de Commissie  op basis van dit verslag een wetgevingsvoorstel in tot wijziging van deze richtlijn. Daarbij houdt de Commissie rekening  met de door de lidstaten verstrekte informatie.

Deze richtlijn treedt in werking op de twintigste dag na die van de bekendmaking ervan in het Publicatieblad van de  Europese Unie .

Deze richtlijn is gericht tot de lidstaten overeenkomstig de Verdragen.

Gedaan te Straatsburg, 23 oktober 2018.

Voor het Europees Parlement

###### Artikel 11

Onderzoeksmiddelen

###### Artikel 12

###### Artikel 13

Omzetting

###### Artikel 14

Verslaglegging

###### Artikel 15

Inwerkingtreding

###### Artikel 16

Adressaten

Voor de Raad

De voorzitter

De voorzitter

A. TAJANI

K. EDTSTADLER
