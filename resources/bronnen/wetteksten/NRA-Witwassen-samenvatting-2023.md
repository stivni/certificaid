---
tags: ["4.0"]
itaa-lex-sectie: ""
wet: "Samenvatting van de Nationale Risicoanalyse Witwassen van geld (update 09/2023, goedgekeurd 25-03-2024)"
bron_rol: "interpretatief"
status: "beschikbaar"
bijgewerkt: "25.03.2024"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/NRA-Witwassen-samenvatting-2023.pdf
      sha256: 14cee3706e3c53b096c8dc005938e0611de8cc2839c319a8f1eef7165789f751
      version: 25.03.2024
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T15:43:05Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T15:49:09Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Beide primaire ETL-fixes zijn bevestigd: de risicomatrix ASCII-grid is volledig weg (0 grid-regels, elke ## KWETSBAARHEID-sectie toont nu leesbare narratieve tekst per sectorgroep), en de inline voetnoot-blobs zijn volledig verwijderd (0 matches op '^[0-9]{1,2} [A-Z]'). Het resterende extractor-artefact (sector-beschrijvingen space-geconcateneerd op één lange regel, bv. 'Groep 1 – Financiële sector    De financiële sector heeft...') is een pymupdf-kolom-bleed die transformers niet kunnen herstellen zonder semantisch risico — dit is geen reden voor needs-rework."
    caveat:
    layer1:
      status: pass
      run_id: 20260519-154647
      run_at: '2026-05-19T15:46:47Z'
      heading_count: 15
      max_section_chars: 20821
      file_size_chars: 24837
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T15:49:09Z'
      rationale: "Beide primaire ETL-fixes zijn bevestigd: de risicomatrix ASCII-grid is volledig weg (0 grid-regels, elke ## KWETSBAARHEID-sectie toont nu leesbare narratieve tekst per sectorgroep), en de inline voetnoot-blobs zijn volledig verwijderd (0 matches op '^[0-9]{1,2} [A-Z]'). Het resterende extractor-artefact (sector-beschrijvingen space-geconcateneerd op één lange regel, bv. 'Groep 1 – Financiële sector    De financiële sector heeft...') is een pymupdf-kolom-bleed die transformers niet kunnen herstellen zonder semantisch risico — dit is geen reden voor needs-rework."
      concrete_problemen:
        - regel: 74
          categorie: (extractor)
          type: sector-label en bijhorende beschrijvingstekst space-geconcateneerd op één lange regel (pymupdf-kolom-bleed, 14 gevallen)
          voorbeeld: Bijlage    Groep 1 – Financiële sector    De financiële sector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als gematigd kan  worden beschouwd, gelet op het gematigde dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.
---

# Samenvatting van de Nationale Risicoanalyse Witwassen van geld (update 09/2023, goedgekeurd 25-03-2024)

*Bijgewerkt tot en met 25.03.2024 — gecoördineerde versie.*

## Samenvatting van de Nationale risicoanalyse

witwassen van geld (update 09/2023)

Goedgekeurd op 25/03/2024 door het ministeriele comité voor de coördinatie

van de bestrijding van witwassen    Inleiding    Deze risicoanalyse vloeit voort uit de nationale 1 , Europese 2 en internationale 3 (aanbeveling 1 van de  Financiële Actiegroep (FATF) verwachtingen en verplichtingen om de risico’s op het gebied van witwassen  van geld (WG) waaraan België wordt blootgesteld te identificeren en te beoordelen.    De risicoanalyse is gericht op sectoren, producten of diensten die een aanzienlijk en hoog risico op  witwassen kunnen vormen. Ze bestaat uit drie delen:    - een analyse van de dreiging WG die deze sectoren, producten of diensten beïnvloed;  - een analyse van de kwetsbaarheden WG van deze sectoren, producten of diensten;  - een analyse van de residuele risico’s WG.    Deze risicoanalyse is het resultaat van een nauwe samenwerking tussen de autoriteiten en diensten die deel  uitmaken van de partnerraad van het College voor de coördinatie van de strijd tegen het witwassen van geld  van illegale afkomst.    Deze risicoanalyse kwam tot stand met input van : de Federale Politie, de FOD Economie, de Administratie  van de Douane en Accijnzen, de Nationale Bank van België (NBB), de Autoriteit voor Financiële diensten  en Markten (FSMA) en de Cel voor Financiële Informatieverwerking (CFI).    De NBB, de FSMA, de FOD Economie, de FOD Financiën Administratie van de Thesaurie, de  Kansspelcommissie, de Nationale Kamer van Notarissen, de Administratie van de Douane en Accijnzen,  het College van Toezicht op de bedrijfsrevisoren, het Institute for Tax Advisors and Accountants en de  verschillende Ordes van Advocaten in België hebben daarentegen een aanzienlijke bijdrage aan de  kwetsbaarheidsanalyse geleverd.    Er werd ook rekening gehouden met de supranationale risicoanalyse op het gebied van witwassen van geld  en financiering van terrorisme die de Europese Commissie in juni 2022 goedkeurde 4 .    In september 2023 werden de WG-risico's geactualiseerd, waarbij de nadruk werd gelegd op belangrijke  veranderingen sinds de laatste beoordeling die van invloed zouden kunnen zijn op het AML/CFT-kader.    Ook al is het ingewikkeld om de precieze omvang van witwassen in de wereld en in België te beoordelen,  aangezien een groot deel van de witwasverrichtingen aan de controle van de autoriteiten ontsnappen, kan  het belang ervan niet worden ontkend.    1 Artikelen 68 en volgende van de wet van 18 september 2017 tot voorkoming van het witwassen van geld en de  financiering van terrorisme en tot beperking van het gebruik van contanten.  2 Artikel 7 van Richtlijn (EU) 2015/849 van het Europees parlement en de Raad van 20 mei 2015.  3 Aanbeveling 1 van de Financiële Actiegroep (FATF).  4 Report from the Commission to the European Parliament and the Council on the assessment of the risk of money  laundering and terrorist financing affecting the internal market and relating to cross-border activities.

Het Bureau van de Verenigde Naties voor drugs- en misdaadbestrijding (UNODC) schatte in 2009 dat het  witwassen 2,7% van het wereldwijde BBP bedraagt. Als we dit percentage van het UNODC overbrengen  op het BBP van België dan kan de omvang van witwassen in België in 2023 op ongeveer 15,7 miljard EUR  worden becijferd.    Misdaadfenomenen    België heeft te maken met verschillende vormen van criminaliteit waarvan de opbrengsten moeten worden  witgewassen. In volgorde van belangrijkheid zijn de belangrijkste : illegale drugshandel, diefstal en  gewelddaden, computerfraude, mensenhandel en terrorisme 5 .    Volgens Europol zijn er meer dan honderd grensoverschrijdende criminele netwerken actief in België. De  georganiseerde misdaad neemt vele vormen aan, waarbij drugshandel, migrantensmokkel, smokkel en  witwassen doorwegen. Mensenhandel en grijze huwelijken behoren ook tot de activiteiten van netwerken  die in België in kaart zijn gebracht. Criminele netwerken persen ook geld af en chanteren kleine bedrijven  en winkels, vooral die met contant geld, zoals restaurants en nachtclubs 6 .

Drugshandel, met name cocaïne, is een van de belangrijkste activiteiten van criminele netwerken, zoals  blijkt uit de recordvangsten van cocaïne in de haven van Antwerpen in de afgelopen drie jaar (meer dan  300 ton). België is ook een van de belangrijkste centra van amfetamineproductie in Europa.

Criminelen gebruiken legale bedrijven als dekmantel voor hun criminele activiteiten. Vooral de bouw-,  vastgoed-, hotel- en logistieke sectoren zijn een doelwit. Vastgoed is favoriet als middel om geld wit te  wassen. Het belangrijkste kenmerk van deze actieve criminele netwerken is hun multi-nationaliteit. Ze zijn  voornamelijk Belgisch en Nederlands, maar ook Albanees of gelieerd aan andere landen in de westelijke  Balkan, Turkije, Marokko, enz. 7 .

België kent ook een aantal maffia-achtige groepen, met name motorbendes, die zich bezighouden met  criminele activiteiten zoals wapen- en drugshandel en seksuele uitbuiting.    Methodologie    De geanalyseerde sectoren, producten en diensten worden uitsluitend beschouwd als actieve deelnemers  aan witwasschema’s. De profielen die werden bestudeerd voor de dreigingsanalyse beschrijven dus  natuurlijke personen of rechtspersonen die bepaalde handels- of financiële verrichtingen uitvoeren (of  dergelijke diensten leveren), ad hoc of stelselmatig, en voor de doeleinden bedoeld in artikel 505, eerste  lid, 2°, 3° en 4° van het Strafwetboek. De bedoelde personen kunnen deze handelingen al dan niet  beroepsmatig uitoefenen.    De blootstelling van deze sectoren, producten of diensten aan zwart geld en de mate waarin ze worden  misbruikt door witwassers is enkel het doel van de kwetsbaarheidsanalyse. Kwetsbaarheid kan worden  gedefinieerd als een risico dat natuurlijke personen of rechtspersonen mogelijk zonder hun medeweten en  voor hen onbedoeld door derden kunnen worden gebruikt om geld wit te wassen dat door derden werd  voortgebracht en waarvan ze weten dat dit geld een illegale oorsprong heeft.

Deze benadering heeft als voordeel dat er veel belang wordt gehecht aan het begrip “witwassen door  derden”, zonder dat het begrip witwassen van door eigen misdrijf verkregen opbrengsten bij deze  benadering wordt uitgesloten. Deze benadering slaat daarentegen niet op de deelname van de geanalyseerde  profielen aan het plegen van het onderliggende misdrijf zoals illegale handel in goederen en koopwaren,  illegale handel in tweedehandswagens, het vervoer van verdovende middelen door een import- of  exportbedrijf, enz.…    De mate van kwetsbaarheid voor witwaspraktijken in een sector hangt af van de (preventieve)  maatregelen die worden genomen. Deze maatregelen zullen het niveau van de dreiging van witwassen in  die sector verminderen. Bedreigingen en kwetsbaarheden zijn daarom nauw verwante begrippen.    De nationale analyse heeft niet tot doel bepaalde sectoren en actoren in het bijzonder te stigmatiseren en de  witwasdreiging die in bepaalde sectoren werd vastgesteld kan betrekking hebben op slechts een minderheid  van de ondernemingen die in deze sector actief zijn.    Resultaten van de risicoanalyse    België heeft een zeer goed inzicht in zijn risico's op witwassen.    Als lid van de FAG en de Europese Unie heeft België toegang tot nuttige informatie over risico's op  witwassen en financiering van terrorisme op internationaal en supranationaal niveau.    Het risico op witwassen is matig in de financiële sector en de verzekeringssector, twee belangrijke sectoren  van de Belgische economie. De andere geanalyseerde sectoren vertonen risiconiveaus gaande van  aanzienlijk tot groot (zie bijlage).    België bestrijdt al jaren het witwassen van geld en de financiering van terrorisme en beschikt over een  regelgevend kader dat aangepast is aan de witwasrisico's waarmee het geconfronteerd wordt.    Het past zich ook snel aan wanneer nieuwe risico's worden vastgesteld.    Voornaamste vaststellingen     Contanten nemen nog steeds een belangrijke plaats in    Het belang van contanten bij witwasverrichtingen mag niet worden onderschat. Contant geld heeft een  belangrijke invloed op de resultaten van de risicoanalyse op het gebied van witwassen van geld.    Vele sectoren, producten en diensten maken nog gebruik van contanten, wat de hoge scores van op het  gebied van de witwasdreiging verklaart. Dit is bijzonder het geval voor handelaars in edele stoffen, oude  metalen en koperkabels, de horecasector, handelaars in tweedehandsvoertuigen, de bouwsector, industriële  schoonmaak, carwashes, nachtwinkels, juweliers/horlogemakers, money mules , systemen voor  geldoverdracht van het type hawala , antiekhandelaars, prostitutie en de vrijetijdssector (sportclubs en  kansspelen).

 Rol van professionele witwassers    Het gebruik van contanten voor witwasdoeleinden is mogelijk door de tussenkomst van professionele  witwassers 8 . Onder andere de compensatietechniek 9 en de tussenkomst van deze professionele witwassers  maken het mogelijk dat sectoren als de bouwsector en de industriële schoonmaak over de nodige contanten  beschikken om arbeiders te betalen die illegaal op werven werken.    Deze professionele witwassers maken in tweede instantie het witwassen mogelijk van geld voortkomend  uit illegale handel in verdovende middelen, oplichting, en andere misdrijven die contanten voortbrengen en  illegale handel in goederen en koopwaren (met name afkomstig uit Azië) en Trade-Based Money  Laundering (TBML)-verrichtingen.    Vennootschappen in de bouw- en schoonmaaksector krijgen hiertoe de hulp van beroepsbeoefenaars in de  sector van dienstverlening aan vennootschappen (met name de cijferberoepen, de belastingadviseurs en  notarissen).     Bijstand en dienstverlening aan bedrijven    Sommige witwasverrichtingen worden mogelijk gemaakt dankzij de tussenkomst van cijferberoepen,  belastingadviseurs en notarissen. Het oprichten van vennootschapsstructuren en het verlenen van bijstand  op fiscaal en boekhoudkundig vlak zijn diensten die witwasverrichtingen vergemakkelijken.    De rol van sommige van deze beroepsbeoefenaars heeft een negatieve invloed op het dreigingsniveau van  deze sectoren. De strikte omkadering van bepaalde beroepen zoals de notarissen zorgt er echter voor dat  het uiteindelijke witwasrisico vermindert.     Fictieve juridische constructies, slapende vennootschappen    Het toenemende gebruik van fictieve juridische structuren, shell-bedrijven en slapende vennootschappen is  een zorg geworden voor de CFI, gerechtelijke autoriteiten, politie en belasting- en sociale overheden. Deze  bedrijven worden opgericht en gebruikt voor het witwassen van geld (vaak in combinatie met belasting- en  sociale fraude).    Ze worden gebruikt voor 6 maanden tot een jaar na hun oprichting, waarna ze worden verlaten door  criminelen. In de afgelopen 10 jaar is de oprichting van bedrijven veel gemakkelijker geworden, waardoor  criminelen honderden bedrijven in de keten kunnen creëren. Nieuwe technologieën maken het mogelijk om  snel een leger stromannen te werven in de functies van management, UBO,...    CFI observeert een toenemend aantal doormeldingen die worden gekenmerkt door de centrale rol die deze  bedrijven spelen als middel om wit te wassen. In zaken die verband houden met de zogenaamde  Braziliaansenetwerken, worden ondernemingen in serie opgericht als onderdeel van ernstige sociale en  fiscale fraude en worden zij gebruikt voor het witwassen van geld. Bovendien illustreren verschillende

gevallen waarin verbanden met de georganiseerde misdaad worden onthuld, de rol van bedrijven binnen  een netwerk in verband met het witwassen van polycrimineel geld. De betrokken bedragen zijn vaak in  miljoenen EUR per dossier. Verschillende nationale en internationale bronnen bevestigen deze trend 10 .    Deze bedrijven zijn ook vaak gevestigd binnen een business center 11 of op een postbusadres.    Als gevolg hiervan is het misbruik van deze structuren met het oog op het witwassen van geld de afgelopen  jaren aanzienlijk toegenomen.     Investeringen in onroerende goederen    Investeren in onroerende goederen (in België of in het buitenland) is een witwastechniek die witwassers  vaak gebruiken. Bij de dreigingsanalyse kon veel informatie worden verzameld die aangeeft dat geld van  illegale herkomst, al dan niet in contanten, vaak voor onroerende goederen wordt aangewend, zowel in  België als in het buitenland.    Contant geld van illegale herkomst wordt ook geïnvesteerd in renovatiewerken en panden die voor kleine  bedragen worden gekocht worden en die vervolgens met een aanzienlijke meerwaarde worden verkocht.    Een betere bewustmaking op het vlak van de opsporing van verdachte verrichtingen van de verschillende  spelers die bij vastgoedtransacties betrokken zijn, met name notarissen en vastgoedmakelaars, en die zonder  hun medeweten in witwasschema’s betrokken zouden kunnen zijn, zou het mogelijk kunnen maken  investeringen in onroerende goederen minder aantrekkelijk te maken voor criminelen.    Onroerend goed zijn ook verankerd in (vastgoed)bedrijven en kan gemakkelijk van eigendom veranderen  door een eenvoudige overdracht van aandelen zonder tussenkomst van een notaris. Het risico op het  witwassen van geld wordt dus niet alleen ontdekt bij notarissen of makelaars in onroerend goed.     Toevluchtswaarden    Net zoals investeringen in onroerende goederen brengen sommige van de bestudeerde 12 sectoren  zogenaamde toevluchtswaarden op de markt die interessant zijn voor criminelen. Diamanten, juwelen, edele  metalen en grote coupures zijn bijvoorbeeld toevluchtswaarden die criminelen op prijs stellen.     Voetbalclubs    De zaken die de voetbalwereld de afgelopen drie jaar treffen tonen zonder twijfel aan dat deze sector een  gevoelige sector is op het vlak van fraude en witwassen. Het risiconiveau van deze sector kan worden  verklaard door de surrealistische waarde van sommige spelers in eerste klasse, de tussenkomst van

tussenpersonen die worden vergoed met commissielonen die even surrealistisch zijn en transferprijzen die  met behulp van – vaak frauduleuze – constructies worden betaald.    Op de andere competitieniveaus wordt er enorm veel contant geld gebruikt in voetbalclubs en wordt ook  vastgesteld dat de bestuurders regelmatig wijzigen.    De witwasrisico’s in deze sector zijn bijzonder groot. De wetgever besliste dus om de professionele  topvoetbalclubs, de sportmakelaars in de voetbalsector en de VZW Koninklijke Belgische Voetbalbond aan  de anti-witwaswet te onderwerpen.     Virtuele valuta    In de afgelopen jaren hebben virtuele valuta’s aan populariteit gewonnen. Ongeveer 4 % van de 13 Belgische  bevolking zou cryptoactiva aanhouden en de wereldmarkt steeg in 2021 3,5 keer 14 .    Virtuele valuta kunnen tot op zekere hoogte worden beschouwd als een nieuw betaalmiddel. Op dit moment  zijn virtuele valuta echter geen wettig betaalmiddel of een vorm van elektronisch geld. Bovendien betekent  de hoge mate van anonimiteit van bepaalde virtuele valuta dat ze vaker worden gebruikt voor  witwasdoeleinden.    Sinds de wet van 20 juli 2020 zijn aanbieders van diensten voor het wisselen tussen virtuele valuta en  fiduciaire valuta die op Belgisch grondgebied zijn gevestigd en aanbieders van bewaarportemonnees die op  Belgisch grondgebied zijn gevestigd onderworpen aan de wet van 18 september 2017 15,16 .    Het koninklijk besluit van 8 februari 2022 bepaalt dat de in België gevestigde aanbieders, voordat zij op  Belgisch grondgebied virtuele valuta- en fiduciaire valutawisseldiensten of bewaarportemonnees  aanbieden, verplicht zijn registratie bij de FSMA te verkrijgen in het register van aanbieders van  uitwisselingsdiensten tussen virtuele valuta en fiduciaire valuta of in het register van aanbieders van  bewaarportemonnees 17 . Dit koninklijk besluit bepaalt dat aanbieders die elektronische infrastructuren  hebben geïnstalleerd die de uitwisseling tussen virtuele valuta en fiduciaire valuta mogelijk maken, en vice  versa, beter bekend als ATM’s, worden beschouwd als gevestigd in België.     Veilige bewaringsdiensten (leasers van kluizen buiten de financiële sector)    Tot voor kort werd de activiteit van het huren van kluizen vrijwel uitsluitend uitgevoerd door financiële  instellingen.    Omdat financiële instellingen deze activiteit hebben verlaten en sommige grote banken hebben besloten om  al hun kluiskamers helemaal te sluiten, zijn ongereglementeerde spelers op de markt gekomen. Deze    13 Study on the payment attitudes of consumers in the euro area (SPACE) – 2022 (europa.eu) ; “The 2022 SPACE  results are based on information collected directly from 50,000 euro area consumers by survey company Kantar Public  over two rounds of online and telephone interviews. The first round took place between October and December 2021  while the second was conducted between March and June 2022. “ ( Study on the payment attitudes of consumers in  the euro area (SPACE) (europa.eu) )  14 Assessment of Risks to Financial Stability from Crypto-assets - Financial Stability Board (fsb.org)  15 Zoals gewijzigd bij de wet van 1 februari 2022 tot wijziging van de wet van 18 september 2017 tot voorkoming van  witwassen en terrorismefinanciering en tot beperking van het gebruik van liquide middelen met het oog op de  invoering van bepalingen inzake de status van en de controle op aanbieders van wisseldiensten tussen virtuele valuta  en fiduciaire valuta en aanbieders van bewaarportemonnees.  16 Artikel 5, 14/1° en 14/2° van de wet van 18 september 2017.  17 Artikel 4 van het koninklijk besluit van 8 februari 2022.

activiteit, die nu ook wordt uitgevoerd door niet-financiële entiteiten, wordt momenteel niet gecontroleerd  op het niveau van de preventie van het witwassen van geld, wat niettemin een wettelijke verplichting is.  Deze huurovereenkomsten zijn niet geregistreerd bij het CAP van de Nationale Bank, zoals het geval is bij  kluizen die worden gehuurd van kredietinstellingen.    In februari 2024 heeft het parlement een wet diverse bepalingen gestemd en nu zijn de Safe Custody  Services providers onderworpen aan de anti-witwaswet.     Virtueel IBAN    Nieuwe betalingendiensten, gekoppeld met betaalrekeningen in verschillende valuta’s, worden aangeboden  door betalingsinstellingen. Dit is specifiek de uitgifte van virtuele betaalrekeningnummers (virtuele  IBAN’s), die uitsluitend bedoeld zijn om betalingen door te leiden naar een fysieke betaalrekening  gekoppeld aan een gewone IBAN. Een virtuele IBAN met “BE” vermelding kan perfect worden gebruikt  door personen of entiteiten die geen klant zijn van een Belgische, of zelfs van een EU, financiële instelling  . Deze praktijken verminderen de transparantie van het betalingssysteem, bemoeilijken de identificatie en  lokalisatie van de onderliggende rekeningen gekoppeld aan deze virtuele IBAN’s en kunnen het moeilijker  maken om transacties te identificeren door financiële inlichtingeenheden en vervolgingsautoriteiten  (parketten en politiediensten).    Hoewel virtuele IBAN’s oorspronkelijk waren ontworpen om de internationale handel te vergemakkelijken,  verhoogt hun misbruik het risico op witwassen. De aanwezigheid van vestigingen naar Belgisch recht die  zeer actief zijn in deze activiteiten vergroot het risico voor de Belgische markt.     De financiële sector en de verzekeringssector    De financiële sector en de verzekeringssector vertonen een gematigd witwasrisico.    De financiële sector is al lang onderworpen aan strenge regels en prudentieel toezicht door de NBB en de  FSMA, ook op het gebied van de voorkoming van witwassen van geld. Dit verklaart waarom het  witwasrisico slechts gematigd is. Daarenboven zijn de financiële instellingen ook onderworpen aan strenge  maatregelen bedoeld om de professionele betrouwbaarheid en passende deskundigheid van hun  aandeelhouders, bestuurders en verantwoordelijken voor essentiële functies te controleren.    Deze toezichtsbevoegdheid wordt rechtstreeks door de Europese Centrale Bank uitgeoefend ten aanzien  van de grootste kredietinstellingen (de “systeembanken”), in het kader van het “gemeenschappelijk  toezichtsmechanisme” en door de NBB, onder het toezicht van de Europese Centrale Bank, ten aanzien van  de minder grote kredietinstellingen.    Hoewel activiteiten zoals private banking, correspondentbankieren en geldtransfers, die door bepaalde  instellingen worden aangeboden, kwetsbaarder zijn, vertoont de financiële sector toch een matig  witwasrisico.

Bijlage    Groep 1 – Financiële sector    De financiële sector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als gematigd kan  worden beschouwd, gelet op het gematigde dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Financiële sector

## KWETSBAARHEID

Groep 2 – Verzekeringssector    De verzekeringssector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als gematigd kan  worden beschouwd, gelet op het gematigde dreigingsniveau en het gematigde kwetsbaarheidsniveau.

Verzekeringssector

## KWETSBAARHEID

Groep 3 – Vastgoedsector    De vastgoedsector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als aanzienlijk kan  worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Vastgoedsector

## KWETSBAARHEID

Groep 4 – Vrijetijdssector    De vrijetijdssector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als aanzienlijk kan  worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Vrijetijdssector

## KWETSBAARHEID

Groep 5 – Luxesector    De luxesector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als aanzienlijk kan  worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Luxesector

## KWETSBAARHEID

Groep 6 – Sector van de detailhandel    De sector van de detailhandel heeft gemiddeld een risiconiveau op het gebied van witwassen dat als  aanzienlijk kan worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het aanzienlijke  kwetsbaarheidsniveau.

Sector van de detailhandel

## KWETSBAARHEID

Groep 7 – Sector van de tweedehandsvoertuigen    De sector van de tweedehandsvoertuigen heeft een risiconiveau op het gebied van witwassen dat als  aanzienlijk kan worden beschouwd, gelet op het hoge dreigingsniveau en het aanzienlijke  kwetsbaarheidsniveau.

Sector van de tweedehandsvoertuigen

## KWETSBAARHEID

Groep 8 – Horecasector    De sector van de horecasector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als hoog  kan worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het hoge kwetsbaarheidsniveau.

Horecasector

## KWETSBAARHEID

Groep 9 – Financieringssector (particulieren)    De financieringssector (particulieren) heeft gemiddeld een risiconiveau op het gebied van witwassen dat  als beperkt kan worden beschouwd, gelet op het lage dreigingsniveau en het gematigde  kwetsbaarheidsniveau.

Financieringssector (particulieren)

## KWETSBAARHEID

Groep 10 – Sector van virtuele valuta    De sector van de virtuele valuta heeft gemiddeld een risiconiveau op het gebied van witwassen dat als hoog  kan worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het hoge kwetsbaarheidsniveau.

Sector van de virtuele valuta

## KWETSBAARHEID

Groep 11 – Sector van dienstverlening aan vennootschappen    De sector van dienstverlening aan vennootschappen heeft gemiddeld een risiconiveau op het gebied van  witwassen dat als gematigd kan worden beschouwd, gelet op het gematigde dreigingsniveau en het  gematigde kwetsbaarheidsniveau.

Sector van zakelijke dienstverlening

## KWETSBAARHEID

Groep 12 – Contanten, geldoverdracht en diensten    De groep contanten, geldoverdracht en diensten heeft gemiddeld een risiconiveau op het gebied van  witwassen dat als hoog kan worden beschouwd, gelet op het hoge dreigingsniveau en het hoge  kwetsbaarheidsniveau.

Contanten, geldoverdracht en diensten

## KWETSBAARHEID

Groep 13 – Transportsector    De transportsector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als aanzienlijk kan  worden beschouwd, gelet op het aanzienlijke dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Transportsector

## KWETSBAARHEID

Groep 14 – Schoonmaaksector    De schoonmaaksector heeft gemiddeld een risiconiveau op het gebied van witwassen dat als aanzienlijk  kan worden beschouwd, gelet op het hoge dreigingsniveau en het aanzienlijke kwetsbaarheidsniveau.

Schoonmaaksector

## KWETSBAARHEID

