---
title: IAS-16 — Materiële vaste activa
tags:
- '1.5'
- ifrs
- ias
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IAS
standaard_nummer: '16'
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
    pages: 94-108
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

## International Accounting Standard 16

Materiële vaste activa

## Doel

1 Het doel van deze standaard is het voorschrijven van de administratieve verwerkingswijze voor materiële vaste activa, zodat de gebruikers van jaarrekeningen inzicht krijgen in de geïnvesteerde bedragen van een entiteit in materiële vaste activa en de mutaties daarin. De voornaamste kwesties die zich voordoen bij de administratieve verwerking van materiële vaste activa betreffen de opname van activa, de bepaling van hun boekwaarde en de afschrijvingskosten en bijzondere waardeverminderingsverliezen die in verband met de activa moeten worden opgenomen.

## Toepassingsgebied

2 Deze standaard moet worden toegepast bij de administratieve verwerking van materiële vaste activa, tenzij een andere International Accounting Standard een andere verwerkingswijze vereist of toestaat. 3 Deze standaard is niet van toepassing op:
(a) materiële vaste activa die zijn geclassificeerd als aangehouden voor verkoop overeenkomstig IFRS 5 Vaste activa aangehouden voor verkoop en beëindigde bedrijfsactiviteiten ;
(b) biologische activa die met agrarische activiteiten verband houden en die geen vruchtdragende planten zijn (zie IAS 41 Landbouw). Deze standaard is van toepassing op vruchtdragende planten maar niet op de producten die door vruchtdragende planten worden voortgebracht;
(c) de opname en waardering van exploratie- en evaluatieactiva (zie IFRS 6 Exploratie en evaluatie van minerale hulpbronnen);
(d) rechten om mineralen te winnen en minerale reserves zoals olie, aardgas en vergelijkbare uitputbare hulp bronnen. Deze standaard is echter van toepassing op materiële vaste activa die worden gebruikt om de in de punten (b) tot en met (d) vermelde activa te ontwikkelen of in stand te houden. 4 [Verwijderd] 5 Een entiteit die overeenkomstig IAS 40 Vastgoedbeleggingen het kostprijsmodel voor vastgoedbeleggingen hanteert, moet voor vastgoedbeleggingen in eigendom het kostprijsmodel in deze standaard gebruiken.

## Definities

6 De volgende begrippen worden in deze standaard gebruikt met de hierna omschreven betekenis: Een vruchtdragende plant is een levende plant:
(a) die wordt gebruikt bij de productie of levering van agrarische producten;
(b) waarvan wordt verwacht dat zij in meer dan één periode producten voortbrengt; en
(c) waarvoor er een zeer kleine kans bestaat dat zij als agrarisch product wordt verkocht, met uit zondering van incidentele verkopen als afval. (In de alinea’s 5A tot en met 5B van IAS 41 wordt nader ingegaan op deze definitie van een vrucht dragende plant.) De boekwaarde is het bedrag waarvoor een actief opgenomen wordt, na aftrek van eventuele geaccumuleerde afschrijvingen en geaccumuleerde bijzondere waardeverminderingsverliezen.

De kostprijs is het bedrag van de geldmiddelen of kasequivalenten die worden betaald of de reële waarde van de andere vergoeding die wordt gegeven om een actief te verwerven op het ogenblik dat het wordt verworven of gebouwd, of, indien van toepassing, het bedrag dat bij eerste opname wordt toegerekend aan dat actief in overeenstemming met de specifieke vereisten van andere IFRSs, bijvoorbeeld IFRS 2 Op aandelen gebaseerde betalingen. Het af te schrijven bedrag is de kostprijs van een actief of een ander kostprijsvervangend bedrag verminderd met zijn restwaarde. Afschrijving is de systematische allocatie van het af te schrijven bedrag van een actief over zijn gebruiksduur. De entiteitsgebonden waarde is de contante waarde van de kasstromen die naar verwachting van een entiteit zullen voortvloeien uit het voortgezette gebruik van een actief en uit zijn vervreemding aan het eind van zijn gebruiks duur of waarvan een entiteit verwacht dat deze zal plaatsvinden bij de afwikkeling van een verplichting. Reële waarde is de prijs die zou worden ontvangen om een actief te verkopen of die zou worden betaald om een verplichting over te dragen in een regelmatige transactie tussen marktdeelnemers op de waarderingsdatum. (Zie IFRS 13 Waardering tegen reële waarde.) Een bijzonder waardeverminderingsverlies is het bedrag waarmee de boekwaarde van een actief zijn realiseerbare waarde overschrijdt. Materiële vaste activa zijn materiële posten die:
(a) worden aangehouden voor gebruik in de productie of levering van goederen of diensten, voor verhuur aan derden of voor bestuurlijke doeleinden; en
(b) waarvan men verwacht dat ze langer dan één periode zullen worden gebruikt. De realiseerbare waarde is de hoogste waarde van de reële waarde minus verkoopkosten van een actief en de bedrijfswaarde van een actief. De restwaarde van een actief is het bedrag dat een entiteit naar verwachting momenteel voor het actief zou ontvangen bij vervreemding, na aftrek van de verwachte kosten van de vervreemding, indien het actief reeds de verwachte ouderdom zou hebben en in de staat zou verkeren die aan het eind van zijn gebruiksduur wordt verwacht. De gebruiksduur is:
(a) de periode gedurende welke een actief naar verwachting voor een entiteit beschikbaar is voor gebruik; dan wel
(b) het aantal productie- of vergelijkbare eenheden dat de entiteit van het actief verwacht te verkrijgen.

## Opname

7 De kostprijs van een materieel vast actief moet als actief worden opgenomen alleen en alleen als:
(a) het waarschijnlijk is dat de toekomstige economische voordelen met betrekking tot het actief naar de entiteit zullen vloeien; en
(b) de kostprijs van het actief betrouwbaar kan worden bepaald. 8 Posten zoals reserveonderdelen, reserveapparatuur en onderhoudsbenodigdheden worden opgenomen in over eenstemming met deze IFRS wanneer zij aan de definitie van materiële vaste activa voldoen. Anders worden dergelijke posten als voorraden geclassificeerd. 9 Deze standaard schrijft niet voor wat een voor opname in aanmerking komend materieel vast actief vormt. Bijgevolg vereist de toepassing van de opnamecriteria een beoordeling van de omstandigheden die voor de entiteit gelden. Het kan geëigend zijn om posten die individueel onbeduidend zijn, zoals mallen, gereedschap en matrijzen, samen te voegen en de criteria toe te passen op de totale waarde.

10 Overeenkomstig dit opnameprincipe evalueert een entiteit al haar kosten in verband met materiële vaste activa op het moment dat deze worden gemaakt. Deze kosten omvatten de eerste kosten die voor het verwerven of bouwen van een materieel vast actief zijn gemaakt en de kosten die daarna worden gemaakt om aan dit actief nieuwe bestanddelen toe te voegen, bestanddelen te vervangen of het actief te onderhouden. De kosten in verband met een materieel vast actief kunnen kosten omvatten die worden gemaakt in verband met leaseover eenkomsten voor activa die worden gebruikt om een materieel vast actief te bouwen, aan dit actief nieuwe bestanddelen toe te voegen, bestanddelen ervan te vervangen of het actief te onderhouden, zoals afschrijving van met een gebruiksrecht overeenstemmende activa. Eerste kosten 11 Materiële vaste activa kunnen worden verworven om veiligheids- of milieuredenen. Hoewel de verwerving van dergelijke materiële vaste activa de toekomstige economische voordelen van een bepaald bestaand materieel vast actief niet rechtstreeks verhoogt, kan de verwerving voor een entiteit nodig zijn om toekomstige economische voordelen van haar andere activa te verkrijgen. Dergelijke materiële vaste activa komen in aanmerking voor opname als activa, omdat ze de entiteit de mogelijkheid geven om aan de activa die er verband mee houden meer toekomstige economische voordelen te onttrekken dan wanneer deze activa niet waren verworven. Zo kan bijvoorbeeld een fabrikant van chemische producten nieuwe chemische behandelingsprocessen invoeren om te voldoen aan de milieunormen voor de productie en opslag van gevaarlijke chemische stoffen. De daaraan gerelateerde verbeteringen van de fabriek worden opgenomen als activa, omdat de entiteit zonder deze ver beteringen geen chemische producten kan produceren of verkopen. De resulterende boekwaarde van een der gelijk actief en de daaraan gerelateerde activa wordt getoetst op bijzondere waardevermindering in overeen stemming met IAS 36 Bijzondere waardevermindering van activa. Kosten na eerste opname 12 Op basis van het principe van opname in alinea 7 neemt een entiteit de dagelijkse onderhoudskosten van een materieel vast actief niet op in de boekwaarde van het actief. Deze kosten worden daarentegen in winst of verlies opgenomen wanneer zij worden gemaakt. De dagelijkse onderhoudskosten zijn voornamelijk de kosten van arbeid en hulpgoederen, waartoe ook de kosten van kleine onderdelen mogen worden gerekend. Het oogmerk van deze uitgaven wordt vaak omschreven als zijnde “de reparatie en het onderhoud” van het materieel vast actief. 13 Het is mogelijk dat onderdelen van bepaalde materiële vaste activa met regelmatige tussenpozen moeten worden vervangen. Zo is het mogelijk dat een oven na een gegeven aantal gebruiksuren opnieuw moet worden bekleed, of dat onderdelen van het interieur van een vliegtuig (bv. stoelen en pantry’s) meermaals moeten worden vervangen gedurende de gebruiksduur van het casco. Er kunnen ook materiële vaste activa worden verworven in het kader van minder vaak terugkerende vervangingen, bijvoorbeeld voor het vervangen van de binnenmuren van een gebouw of voor het uitvoeren van een eenmalige vervanging. Op basis van het opnameprincipe in alinea 7 neemt een entiteit de kostprijs van een vervangingsonderdeel op in de boekwaarde van een materieel vast actief wanneer de kosten worden gemaakt en indien aan de opnamecriteria wordt voldaan. De boekwaarde van deze vervangen onderdelen wordt niet langer opgenomen, overeenkomstig de in deze standaard beschreven bepalingen inzake het niet langer opnemen (zie de alinea’s 67 tot en met 72). 14 Een voorwaarde voor het blijven gebruiken van een materieel vast actief (bv. een vliegtuig) kan bestaan uit het regelmatig uitvoeren van grondige inspecties om gebreken op te sporen, ongeacht of onderdelen van het actief worden vervangen. De kosten van grondige inspecties worden als vervangingsinvestering opgenomen in de boekwaarde van het materieel vast actief indien aan de opnamecriteria wordt voldaan. De eventuele resterende boekwaarde van de kosten van de vorige inspectie (niet zijnde materiële onderdelen) wordt niet langer opge nomen. Dit vindt plaats ongeacht of de kosten van de vorige inspectie bepaald werden in de transactie waarin het actief verworven of vervaardigd werd. Indien noodzakelijk kan de verwachte kostprijs van een soortgelijke toekomstige inspectiebeurt worden gebruikt als een indicatie voor de bepaling van de kosten van de reeds uitgevoerde inspectie op het moment dat de post werd verworven of vervaardigd.

## Waardering Bij Eerste Opname

15 Een materieel vast actief dat in aanmerking komt voor opname als actief moet worden gewaardeerd tegen de kostprijs. Samenstelling van de kostprijs 16 De kostprijs van een materieel vast actief omvat:
(a) de aankoopprijs, met inbegrip van invoerrechten en niet-restitueerbare omzetbelasting, na aftrek van handels- en andere kortingen;
(b) alle rechtstreeks toerekenbare kosten om het actief op de locatie en in de staat te krijgen die noodzakelijk is om te functioneren op de door het management beoogde wijze;

(c) de eerste schatting van de kosten van ontmanteling en verwijdering van het actief, en van het herstel van het terrein waar het actief zich bevindt; de verplichting hiervoor wordt door de entiteit aangegaan wanneer het actief wordt verkregen, of ontstaat als gevolg van het gebruik gedurende een bepaalde periode voor andere doeleinden dan de productie van voorraden tijdens die periode. 17 Voorbeelden van rechtstreeks toerekenbare kosten zijn:
(a) kosten van personeelsbeloningen (zoals gedefinieerd in IAS 19 Personeelsbeloningen ) die rechtstreeks voort komen uit de vervaardiging of verwerving van een materieel vast actief;
(b) kosten voor het geschikt maken van het terrein;
(c) initiële leverings- en afhandelingskosten;
(d) installatie- en montagekosten;
(e) kosten om te onderzoeken of het actief naar behoren functioneert (d.w.z. onderzoeken of het actief technisch en fysiek zodanig presteert dat het kan worden gebruikt in de productie of levering van goederen of diensten, voor verhuur aan derden, of voor bestuurlijke doeleinden); en
(f) honoraria van adviseurs. 18 Een entiteit past IAS 2 Voorraden toe op de kosten die samenhangen met de verplichtingen inzake de ont manteling en verwijdering van het actief, en het herstel van het terrein waar het actief zich bevindt, die gedurende een bepaalde periode worden gemaakt als gevolg van het gebruik van het actief tijdens die periode voor de productie van voorraden. De verplichtingen betreffende kosten die worden verwerkt in overeenstemming met IAS 2 of IAS 16 worden opgenomen en gewaardeerd overeenkomstig IAS 37 Voorzieningen, voorwaardelijke verplichtingen en voorwaardelijke activa. 19 Voorbeelden van kosten die geen kosten van een materieel vast actief zijn:
(a) openingskosten van een nieuwe vestiging;
(b) kosten om een nieuw product of een nieuwe dienst te lanceren (met inbegrip van advertentie- en promo tiekosten);
(c) kosten voor bedrijfsvoering op een nieuwe locatie of met een nieuwe cliëntencategorie (met inbegrip van opleidingskosten voor het personeel); en
(d) administratie- en andere algemene overheadkosten. 20 De opname van kosten in de boekwaarde van een materieel vast actief wordt beëindigd wanneer het actief op de locatie is en zich in de staat bevindt die noodzakelijk is om te kunnen functioneren op de door het management beoogde wijze. Derhalve worden kosten die worden gemaakt voor het gebruik of het anders inzetten van een materieel vast actief niet opgenomen in de boekwaarde van dat actief. De volgende kosten worden bijvoorbeeld niet in de boekwaarde van een materieel vast actief opgenomen:
(a) kosten die worden gemaakt voor een actief dat, hoewel het in staat is om te functioneren op de door het management beoogde wijze, nog gebruiksklaar moet worden gemaakt of dat functioneert beneden zijn optimale productiecapaciteit;
(b) initiële exploitatieverliezen, zoals de verliezen die optreden wanneer de vraag naar de producten die met het actief worden vervaardigd zich in een opbouwfase bevindt; en
(c) kosten van verplaatsing of reorganisatie van een deel van of alle bedrijfsactiviteiten van de entiteit.

## 20A

Items kunnen worden geproduceerd door een materieel vast actief naar de locatie en in de staat te brengen die nodig is opdat het actief zou kunnen functioneren op de door het management beoogde wijze (zoals geprodu ceerde monsters wanneer wordt getest of het actief naar behoren functioneert). Een entiteit neemt de opbreng sten van de verkoop van die items, en de kosten van die items, in winst of verlies op in overeenstemming met de toepasselijke standaarden. De entiteit waardeert de kostprijs van die items volgens de waarderingsvereisten van IAS 2. 21 Sommige bedrijfsactiviteiten houden verband met de vervaardiging of ontwikkeling van een materieel vast actief, maar zijn niet noodzakelijk om het actief naar de locatie of in de staat te brengen die nodig is opdat het actief zou kunnen functioneren op de door het management beoogde wijze. Deze incidentele bedrijfsactiviteiten kunnen vóór of tijdens de vervaardiging of ontwikkelingsactiviteiten plaatsgrijpen. Er kunnen bijvoorbeeld baten worden gegenereerd door een bouwterrein als parkeerterrein te gebruiken tot de bouw van start gaat. Omdat incidentele bedrijfsactiviteiten niet noodzakelijk zijn om het actief naar de locatie en in de staat te brengen die nodig is om te kunnen functioneren op de door het management beoogde wijze, worden de baten en daaraan gerelateerde lasten van incidentele bedrijfsactiviteiten in winst of verlies opgenomen als onderdeel van de baten- en lastencategorieën waartoe zij behoren. 22 De kostprijs van een zelf vervaardigd actief wordt bepaald volgens dezelfde principes als bij een verworven actief. Indien een entiteit soortgelijke activa maakt voor verkoop in het kader van de normale bedrijfsuitoefening, is de kostprijs van het actief meestal gelijk aan de kostprijs van een actief dat wordt vervaardigd voor verkoop (zie IAS 2). Eventuele interne winsten worden derhalve geëlimineerd bij het bepalen van dergelijke kostprijzen. Evenzo maken abnormale kosten in verband met verspilde materialen, arbeid en andere middelen die zijn aangewend voor de vervaardiging van een actief geen deel uit van de kostprijs van het actief. In IAS 23 Financieringskosten zijn de criteria vastgelegd voor de opname van rente als een onderdeel van de boekwaarde van een zelf vervaardigd materieel vast actief.

## 22A

Vruchtdragende planten worden op dezelfde wijze administratief verwerkt als zelf vervaardigde materiële activa voordat deze op de locatie zijn en zich in de staat bevinden die noodzakelijk is om te kunnen functioneren op de door het management beoogde wijze. De in deze standaard voorkomende verwijzingen naar “vervaardiging” moeten bijgevolg worden gelezen als betrekking hebbend op de activiteiten die noodzakelijk zijn om de vrucht dragende planten te telen voordat deze op de locatie zijn en zich in de staat bevinden die noodzakelijk is om te kunnen functioneren op de door het management beoogde wijze. Bepaling van de kostprijs 23 De kostprijs van een materieel vast actief is het equivalent van de contante prijs op het moment van opname. Indien de betaling wordt uitgesteld tot na de gebruikelijke betalingstermijn, wordt het verschil tussen het equivalent van de contante prijs en het totaal betaalde bedrag opgenomen als rente gedurende de periode van uitgestelde betaling, tenzij die rente wordt geactiveerd in overeenstemming met IAS 23. 24 Een of meer materiële vaste activa kunnen worden verworven in ruil voor een niet-monetair actief of niet- monetaire activa, of een combinatie van monetaire en niet-monetaire activa. De volgende beschouwing verwijst eenvoudigweg naar een ruil van een niet-monetair actief voor een ander niet-monetair actief, maar is ook van toepassing op alle ruiltransacties die in de voorgaande zin beschreven zijn. De kostprijs van een dergelijk materieel vast actief wordt bepaald op basis van de reële waarde tenzij a) de ruiltransactie geen economische betekenis heeft, of b) als de reële waarde van het ontvangen actief en het opgegeven actief niet betrouwbaar kunnen worden bepaald. Het verworven actief wordt op deze wijze gewaardeerd, zelfs indien een entiteit het opgegeven actief niet onmiddellijk kan verwijderen. Indien het verworven actief niet tegen reële waarde wordt gewaardeerd, is de kostprijs gelijk aan de boekwaarde van het opgegeven actief. 25 Een entiteit bepaalt of een ruiltransactie economische betekenis heeft door te beoordelen in welke mate zij verwacht dat toekomstige kasstromen zullen wijzigen als gevolg van de transactie. Een ruiltransactie heeft economische betekenis indien:
(a) de samenstelling (risico, tijdstip en bedrag) van de kasstromen van het ontvangen actief verschilt van de samenstelling van de kasstromen van het overgedragen actief; of
(b) de entiteitsgebonden waarde van het gedeelte van de bedrijfsactiviteiten van de entiteit dat door de transactie wordt beïnvloed, verandert als gevolg van de ruil; en
(c) het verschil onder (a) of (b) significant is ten opzichte van de reële waarde van de geruilde activa.

Om te bepalen of een ruiltransactie economische betekenis heeft, moet de entiteitsgebonden waarde van het gedeelte van de bedrijfsactiviteiten van de entiteit dat door de transactie is beïnvloed, de kasstromen na aftrek van belastingen weergeven. Het resultaat van deze analyses kan duidelijk zijn zonder dat een entiteit gedetailleerde berekeningen hoeft uit te voeren. 26 De reële waarde van een actief kan betrouwbaar worden bepaald als (a) de variabiliteit in de bandbreedte van redelijke waarderingen van dat actief tegen reële waarde niet aanzienlijk is, of als (b) de waarschijnlijkheid van de verschillende schattingen binnen de bandbreedte redelijk goed kan worden ingeschat en voor het bepalen van de reële waarde kan worden gebruikt. Als een entiteit de reële waarde van het ontvangen of opgegeven actief betrouwbaar kan bepalen, wordt de reële waarde van het opgegeven actief gebruikt om de kostprijs van het ontvangen actief te bepalen, tenzij de reële waarde van het ontvangen actief duidelijker blijkt. 27 [Verwijderd] 28 De boekwaarde van een materieel vast actief kan worden verminderd met overheidssubsidies in overeenstemming met IAS 20 Administratieve verwerking van overheidssubsidies en informatieverschaffing over overheidssteun.

## Waardering Na Eerste Opname

29 Een entiteit moet ofwel het kostprijsmodel in alinea 30 ofwel het herwaarderingsmodel in alinea 31 als grondslag voor haar financiële verslaggeving kiezen en deze grondslag op een volledige categorie van materiële vaste activa toepassen.

## 29A

Sommige entiteiten hebben intern of extern een beleggingsfonds dat beleggers voordelen biedt die worden bepaald door de rechten van deelneming in het fonds. Evenzo geven sommige entiteiten groepen verzekerings contracten met directe winstdelingselementen uit en houden zij de onderliggende posten aan. Sommige van deze fondsen of onderliggende posten omvatten vastgoed voor eigen gebruik. De entiteit past IAS 16 toe op vastgoed voor eigen gebruik dat deel uitmaakt van een dergelijk fonds of dat een onderliggende post is. Ondanks alinea 29 kan de entiteit ervoor kiezen dergelijk vastgoed te waarderen op basis van het reëlewaardemodel overeenkomstig IAS 40. Voor de toepassing van deze keuze omvatten verzekeringscontracten beleggingscontracten met discre tionaire winstdelingselementen. (Zie IFRS 17 Verzekeringscontracten voor in deze alinea gebruikte termen die in die standaard zijn gedefinieerd.)

## 29B

Een entiteit moet vastgoed voor eigen gebruik dat wordt gewaardeerd met behulp van het reëlewaardemodel voor vastgoedbeleggingen met toepassing van alinea 29A behandelen als een afzonderlijke categorie materiële vaste activa. Kostprijsmodel 30 Na de opname als een actief, moet een materieel vast actief worden geboekt tegen zijn kostprijs, ver minderd met eventuele geaccumuleerde afschrijvingen en eventuele geaccumuleerde bijzondere waarde verminderingsverliezen. Herwaarderingsmodel 31 Na de opname als een actief moet een materieel vast actief waarvan de reële waarde betrouwbaar kan worden bepaald, worden geboekt tegen de geherwaardeerde waarde, zijnde de reële waarde op het moment van de herwaardering, verminderd met eventuele latere geaccumuleerde afschrijvingen en latere geaccumuleerde bijzondere waardeverminderingsverliezen. De herwaardering moet voldoende regelmatig worden uitgevoerd om ervoor te zorgen dat de boekwaarde niet beduidend verschilt van de boekwaarde die zou worden bepaald aan de hand van de reële waarde op het einde van de ver slagperiode. 32 [Verwijderd] 33 [Verwijderd] 34 De frequentie van de herwaarderingen hangt af van de wijzigingen in de reële waarde van de materiële vaste activa die worden geherwaardeerd. Indien de reële waarde van een geherwaardeerd actief beduidend verschilt van de boekwaarde, is een verdere herwaardering vereist. Sommige materiële vaste activa zijn onderworpen aan aanzienlijke en volatiele wijzigingen in de reële waarde, waardoor een jaarlijkse herwaardering noodzakelijk is. Dergelijke frequente herwaarderingen zijn niet nodig voor materiële vaste activa waarvan de reële waarde niet aanzienlijk schommelt. In dit geval kan een herwaardering om de drie of vijf jaar volstaan.

35 Wanneer een materieel vast actief wordt geherwaardeerd, wordt de boekwaarde van dat actief aan de geher waardeerde waarde aangepast. Op de datum van de herwaardering wordt het actief op een van de volgende wijzen verwerkt:
(a) de brutoboekwaarde wordt aangepast op een wijze die overeenstemt met de herwaardering van de boek waarde van het actief. Zo kan de brutoboekwaarde op basis van waarneembare marktgegevens, dan wel evenredig aan de wijziging van de boekwaarde worden aangepast. De geaccumuleerde afschrijving op de datum van de herwaardering wordt zodanig aangepast dat zij gelijk is aan het verschil tussen de brutoboek waarde en de boekwaarde van het actief na inaanmerkingneming van geaccumuleerde bijzondere waarde verminderingsverliezen; of
(b) de geaccumuleerde afschrijving wordt geëlimineerd tegen de brutoboekwaarde van het actief. Het bedrag van de aanpassing van de geaccumuleerde afschrijving maakt deel uit van de verhoging of verlaging van de boekwaarde die administratief wordt verwerkt in overeenstemming met de alinea’s 39 en 40. 36 Indien een materieel vast actief wordt geherwaardeerd, moet de volledige categorie van materiële vaste activa waartoe dat actief behoort, worden geherwaardeerd. 37 Een categorie van materiële vaste activa is een groepering van activa met een gelijksoortige aard en een gelijksoortig gebruik in de bedrijfsactiviteiten van de entiteit. Voorbeelden van afzonderlijke categorieën zijn:
(a) grond;
(b) terreinen en gebouwen;
(c) machines;
(d) schepen;
(e) vliegtuigen;
(f) motorvoertuigen;
(g) meubilair en inrichting;
(h) kantoorinrichting; en
(i) vruchtdragende planten. 38 De posten binnen een categorie van materiële vaste activa worden gelijktijdig geherwaardeerd om te voorkomen dat activa selectief worden geherwaardeerd en dat de jaarrekening bedragen weergeeft die een mengeling zijn van kosten en waarden op verschillende data. Een categorie van activa mag echter op voortschrijdende basis worden geherwaardeerd, op voorwaarde dat de herwaardering van de categorie van activa binnen een korte periode wordt voltooid en dat de herwaarderingen actueel blijven. 39 Indien de boekwaarde van een actief stijgt als gevolg van een herwaardering, moet de stijging in overige onderdelen van het totaalresultaat worden opgenomen en in het eigen vermogen worden verwerkt als herwaarderingsreserve. De stijging moet echter in winst of verlies worden opgenomen in zoverre zij een herwaarderingsafname van hetzelfde actief terugdraait die voorheen in winst of verlies was opge nomen. 40 Indien de boekwaarde van een actief afneemt als gevolg van een herwaardering, moet de afname in winst of verlies worden opgenomen. De afname moet echter in overige onderdelen van het totaalre sultaat worden opgenomen in zoverre de herwaarderingsreserve die op dat actief betrekking heeft over een creditsaldo beschikt. De in overige onderdelen van het totaalresultaat opgenomen afname reduceert het bedrag dat als herwaarderingsreserve in het eigen vermogen is opgenomen.

41 De in het eigen vermogen opgenomen herwaarderingsreserve met betrekking tot een materieel vast actief mag direct naar de ingehouden winsten worden overgeboekt wanneer het actief niet langer wordt opgenomen. Dit kan inhouden dat de desbetreffende reserve in zijn geheel wordt overgeboekt wanneer het actief buiten gebruik wordt gesteld of wordt vervreemd. Een gedeelte van de reserve kan echter worden overgedragen wanneer het actief door een entiteit wordt gebruikt. In een dergelijk geval komt het bedrag van de overgeboekte reserve overeen met het verschil tussen de afschrijving gebaseerd op de geherwaardeerde boekwaarde van het actief en de afschrijving die gebaseerd is op de oorspronkelijke kostprijs van het actief. Overboekingen van de herwaarde ringsreserve naar ingehouden winsten vinden niet in winst of verlies plaats. 42 De eventuele gevolgen van winstbelastingen die voortvloeien uit de herwaardering van materiële vaste activa worden opgenomen en vermeld overeenkomstig IAS 12 Winstbelastingen . Afschrijving 43 Ieder bestanddeel van een materieel vast actief met een substantiële kostprijs in relatie tot de totale kostprijs van het actief moet afzonderlijk worden afgeschreven. 44 Een entiteit rekent het bedrag dat aanvankelijk voor een materieel vast actief is opgenomen toe aan de belang rijke onderdelen ervan en schrijft elk dergelijk onderdeel afzonderlijk af. Het kan bijvoorbeeld geëigend zijn om het casco en de motoren van een vliegtuig afzonderlijk af te schrijven. Zo ook kan het geëigend zijn, als een entiteit materiële vaste activa verwerft die het voorwerp uitmaken van een operationele lease waarbij ze de lessor is, om bedragen weerspiegeld in de kostprijs van die activa die aan gunstige of ongunstige leasevoorwaarden in vergelijking met de marktvoorwaarden kunnen worden toegerekend, afzonderlijk af te schrijven. 45 Indien een belangrijk bestanddeel van een materieel vast actief dezelfde gebruiksduur en afschrijvingsmethode heeft als een ander belangrijk bestanddeel van hetzelfde actief, kunnen zulke bestanddelen worden samengevoegd bij de bepaling van de afschrijvingskosten. 46 Voor zover een entiteit sommige bestanddelen van een materieel vast actief afzonderlijk afschrijft, moet zij ook de overige bestanddelen van het actief afzonderlijk afschrijven. De overige bestanddelen bestaan uit bestanddelen van het actief die op zich niet van betekenis zijn. Indien een entiteit voor deze bestanddelen verschillende verwachtingen heeft, kan het gebruik van benaderingstechnieken noodzakelijk zijn om de overige bestanddelen af te schrijven op zodanige wijze dat de afschrijving een getrouw beeld geeft van het gebruikspatroon en/of de gebruiksduur van de bestanddelen. 47 Een entiteit mag de bestanddelen van een actief die geen substantieel deel uitmaken van de totale kostprijs van het actief, afzonderlijk afschrijven. 48 De afschrijvingskosten over elke periode moeten worden opgenomen in winst of verlies, tenzij ze worden opgenomen in de boekwaarde van een ander actief. 49 De afschrijvingskosten over een periode worden gewoonlijk in winst of verlies opgenomen. Soms worden de toekomstige economische voordelen die een actief in zich bergt echter gebruikt bij de productie van andere activa. In dit geval vormen de afschrijvingskosten een gedeelte van de kosten van het andere actief en worden ze opgenomen in de boekwaarde van dat actief. Zo wordt de afschrijving van fabrieksinstallaties opgenomen in de conversiekosten van voorraden (zie IAS 2). Evenzo kan de afschrijving van materiële vaste activa die worden gebruikt voor ontwikkelingsactiviteiten worden opgenomen in de kostprijs van immateriële activa die worden opgenomen in overeenstemming met IAS 38 Immateriële activa. Het af te schrijven bedrag en de afschrijvingsperiode 50 Het af te schrijven bedrag van een actief moet stelselmatig worden toegerekend over de gebruiksduur van het actief. 51 De restwaarde en de gebruiksduur van een actief moeten ten minste aan het eind van elk boekjaar worden herzien, en indien de verwachtingen verschillen van de vorige schattingen, moet(en) de wijziging(en) admini stratief worden verwerkt als een schattingswijziging in overeenstemming met IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten. 52 Er wordt afgeschreven, zelfs indien de reële waarde van het actief groter is dan zijn boekwaarde, tot de rest waarde is bereikt. Reparaties en onderhoud van een actief doen niets af aan de noodzaak tot afschrijving.

53 Het af te schrijven bedrag van een actief wordt bepaald na aftrek van zijn restwaarde. In de praktijk is de restwaarde van een actief vaak onbeduidend en speelt ze dus geen belangrijke rol in de berekening van het af te schrijven bedrag. 54 De restwaarde van een actief kan stijgen tot een bedrag dat gelijk is aan of groter is dan de boekwaarde van het actief. Indien dit het geval is, zijn de afschrijvingskosten van het actief nihil, tenzij en totdat de restwaarde van het actief daarna afneemt tot een bedrag dat kleiner is dan de boekwaarde van het actief. 55 De afschrijving van een actief vangt aan wanneer het gereed is voor gebruik, d.w.z. wanneer het actief op de locatie en in de staat is die noodzakelijk is om te functioneren op de door het management beoogde wijze. Afschrijvingen van een actief moeten worden beëindigd op de datum waarop het actief wordt geclassificeerd als aangehouden voor verkoop (of wanneer het wordt opgenomen in een groep activa die wordt afgestoten en die geclassificeerd is als aangehouden voor verkoop) overeenkomstig IFRS 5, of op de datum waarop het actief niet langer wordt opgenomen als deze datum voorafgaat aan de eerste. Derhalve worden afschrijvingen niet beëindigd wanneer het actief niet langer wordt gebruikt of buiten gebruik wordt gesteld, tenzij het actief volledig is afgeschreven. In geval van afschrijving op basis van verbruikte werkeenheden kunnen de afschrijvingskosten echter nihil zijn zolang er geen productie plaatsvindt. 56 De toekomstige economische voordelen die een actief in zich bergt, worden door een entiteit hoofdzakelijk verbruikt door het actief te gebruiken. Vaak leiden echter andere factoren, zoals technische of economische veroudering en slijtage terwijl een actief niet wordt gebruikt, tot een vermindering van de economische voordelen die met het actief hadden kunnen worden gegenereerd. Bijgevolg worden alle volgende factoren in aanmerking genomen bij de bepaling van de gebruiksduur van een actief:
(a) het verwachte gebruik van het actief. Het gebruik wordt geschat op basis van de verwachte capaciteit of fysieke productie van het actief;
(b) de verwachte fysieke slijtage, die afhangt van operationele factoren zoals het aantal werkperioden waarin het actief zal worden gebruikt, het reparatie- en onderhoudsprogramma, en het onderhoud van het actief wanneer het niet in gebruik is;
(c) de technische of economische veroudering als gevolg van wijzigingen of verbeteringen in de productie of als gevolg van een wijziging in de vraag van de markt naar het product dat of de dienst die met het actief wordt geleverd. Verwachte toekomstige verminderingen van de verkoopprijs van een post die met een actief is geproduceerd, kunnen wijzen op een verwachte technische of economische veroudering van het actief, die op haar beurt mogelijkerwijs een vermindering kan weerspiegelen van de toekomstige economische voordelen die het actief in zich bergt;
(d) juridische of soortgelijke beperkingen op het gebruik van het actief, zoals de vervaldata van gerelateerde leaseovereenkomsten. 57 De gebruiksduur van een actief wordt gedefinieerd in termen van het verwachte nut van het actief voor de entiteit. Het beleid van een entiteit ten aanzien van het activabeheer kan inhouden dat een actief na een bepaalde tijd wordt vervreemd of nadat een bepaald gedeelte van de toekomstige economische voordelen die het actief in zich bergt, is verbruikt. De gebruiksduur van een actief kan dus korter zijn dan zijn economische levensduur. De schatting van de gebruiksduur van het actief is een kwestie van beoordeling, gebaseerd op de ervaring van de entiteit met soortgelijke activa. 58 Terreinen en gebouwen zijn afscheidbare activa en worden administratief afzonderlijk verwerkt, zelfs indien ze samen zijn verworven. Behoudens enkele uitzonderingen, zoals steengroeven en locaties die gebruikt worden voor het storten van afval, hebben terreinen een onbeperkte gebruiksduur en worden ze daarom niet afgeschre ven. Gebouwen hebben een beperkte gebruiksduur en zijn dus af te schrijven activa. Een waardestijging van de grond waarop een gebouw staat, heeft geen invloed op de bepaling van het af te schrijven bedrag van het gebouw. 59 Indien in de kostprijs van de grond de kosten van ontmanteling, verwijdering en herstel inbegrepen zijn, is de afschrijvingstermijn van dat gedeelte van de geactiveerde grond gelijk aan de periode waarin de voordelen verkregen worden die voortvloeien uit het maken van deze kosten. In sommige gevallen kan de grond zelf een beperkte gebruiksduur hebben. In dit geval wordt de grond afgeschreven op een wijze die een afspiegeling is van de voordelen die eraan worden ontleend. Afschrijvingsmethode 60 De gebruikte afschrijvingsmethode moet een afspiegeling zijn van het patroon volgens welk de toe komstige economische voordelen van het actief naar verwachting zullen worden verbruikt door de entiteit. 61 De op een actief toegepaste afschrijvingsmethode moet ten minste aan het eind van elk boekjaar worden herzien. Indien het verwachte verbruikspatroon van de toekomstige economische voordelen die het actief in zich bergt beduidend is gewijzigd, moet de methode worden gewijzigd om rekening te houden met het gewijzigde patroon. Een dergelijke wijziging moet administratief worden verwerkt als een schattingswijziging, in overeenstemming met IAS 8.

62 Er kunnen diverse afschrijvingsmethoden worden gehanteerd om het af te schrijven bedrag van een actief op systematische basis toe te rekenen over de gebruiksduur van het actief. Deze methoden omvatten de lineaire afschrijvingsmethode, de degressieve afschrijvingsmethode en de afschrijvingsmethode op basis van verbruikte werkeenheden. Lineaire afschrijving resulteert in een constante last gedurende de gebruiksduur indien de rest waarde van het actief niet verandert. De degressieve afschrijvingsmethode resulteert in een dalende last gedurende de gebruiksduur. De afschrijvingsmethode op basis van verbruikte werkeenheden leidt tot een last die gebaseerd is op het verwachte gebruik of de verwachte productie. De entiteit kiest de methode die het verwachte ver bruikspatroon van de toekomstige economische voordelen die het actief in zich bergt, het best weerspiegelt. Die afschrijvingsmethode wordt in elke periode consistent toegepast, tenzij het verwachte verbruikspatroon van deze toekomstige economische voordelen verandert.

## 62A

Een afschrijvingsmethode die is gebaseerd op de opbrengsten die worden gegenereerd door een activiteit die het gebruik van een actief omvat, is niet passend. De opbrengsten die worden gegenereerd door een activiteit die het gebruik van een actief omvat, weerspiegelen doorgaans immers andere factoren dan het verbruik van de eco nomische voordelen van het actief. Zo worden opbrengsten beïnvloed door andere inputs en processen, ver koopsactiviteiten en veranderingen in verkoopvolumes en prijzen. De prijscomponent van opbrengsten kan worden beïnvloed door inflatie, die geen invloed heeft op de wijze waarop een actief wordt verbruikt. Bijzondere waardevermindering 63 Om te bepalen of er sprake is van een bijzondere waardevermindering van een materieel vast actief, past een entiteit IAS 36 Bijzondere waardevermindering van activa toe. In deze standaard wordt verklaard hoe een entiteit de boekwaarde van haar activa herziet, hoe ze de realiseerbare waarde van een actief bepaalt en wanneer ze een bijzonder waardeverminderingsverlies opneemt of de opname ervan terugneemt. 64 [Verwijderd] Vergoeding voor bijzondere waardevermindering 65 Vergoedingen van derden voor materiële vaste activa die een bijzondere waardevermindering hebben ondergaan, verloren zijn gegaan of werden opgegeven, moeten in winst of verlies worden opgenomen op het moment dat de vergoeding invorderbaar wordt. 66 Bijzondere waardeverminderingen of het verloren gaan van materiële vaste activa, daarmee samenhangende vorderingen in verband met of betalingen van vergoedingen van derden en de eventuele latere aankoop of vervaardiging van vervangingsactiva zijn afzonderlijke economische gebeurtenissen en moeten administratief afzonderlijk worden verwerkt op de volgende wijze:
(a) bijzondere waardeverminderingen van materiële vaste activa worden overeenkomstig IAS 36 opgenomen;
(b) het niet langer opnemen van materiële vaste activa die buiten gebruik zijn gesteld of vervreemd zijn, wordt overeenkomstig deze standaard bepaald;
(c) vergoedingen van derden voor materiële vaste activa die een bijzondere waardevermindering hebben onder gaan, verloren zijn gegaan of zijn opgegeven, worden in winst of verlies opgenomen op het moment dat de vergoeding invorderbaar wordt; en
(d) de kostprijs van materiële vaste activa die ter vervanging worden hersteld, gekocht of vervaardigd, wordt overeenkomstig deze standaard bepaald.

## Niet Langer Opnemen

67 De boekwaarde van een materieel vast actief mag niet langer worden opgenomen:
(a) na vervreemding; dan wel
(b) indien er geen toekomstige economische voordelen meer te verwachten zijn van het gebruik of de vervreemding van het actief. 68 De winst die of het verlies dat voortvloeit uit het niet langer opnemen van een materieel vast actief moet in winst of verlies worden opgenomen wanneer het actief niet langer in het overzicht van de financiële positie wordt opgenomen (tenzij IFRS 16 Leaseovereenkomsten anderszins voorschrijft bij een sale-and-leasebacktransactie). Win sten mogen niet als opbrengsten worden geclassificeerd.

## 68A

Een entiteit die in het kader van haar normale bedrijfsactiviteiten stelselmatig overgaat tot de verkoop van materiële vaste activa die zij heeft aangehouden voor verhuur aan derden, moet dergelijke activa evenwel tegen hun boekwaarde naar voorraden overboeken wanneer deze activa niet meer worden verhuurd maar voor ver koop worden aangehouden. De opbrengsten van de verkoop van dergelijke activa moeten overeenkomstig IAS 15 Opbrengsten van contracten met klanten als opbrengsten worden opgenomen. IFRS 5 is niet van toepassing wanneer activa die in het kader van de normale bedrijfsactiviteiten voor verkoop worden aangehouden, naar voorraden worden overgeboekt. 69 De vervreemding van een materieel vast actief kan op verschillende wijzen plaatsvinden (bijvoorbeeld door verkoop, door het aangaan van een financiële lease of via schenking). De datum van vervreemding van een materieel vast actief is de datum waarop de ontvanger zeggenschap over dat actief verkrijgt in overeenstemming met de in IFRS 15 vervatte vereisten voor het bepalen wanneer een prestatieverplichting wordt vervuld. IFRS 16 is van toepassing op vervreemding via een sale-and-leasebacktransactie. 70 Indien een entiteit op grond van het opnameprincipe in alinea 7 de kostprijs van de vervanging van een bestanddeel van een materieel vast actief opneemt in de boekwaarde van het actief, dan neemt zij de boekwaarde van het vervangen bestanddeel niet langer op, ongeacht of dit vervangen bestanddeel afzonderlijk werd afge schreven. Indien het voor een entiteit praktisch niet haalbaar is om de boekwaarde van het vervangen gedeelte te bepalen, mag zij de kosten van de vervanging gebruiken als indicatie van de kostprijs van het vervangen gedeelte op het moment dat het verworven of gebouwd werd. 71 De winst die of het verlies dat voortvloeit uit het niet langer opnemen van een materieel vast actief zal worden bepaald als zijnde het verschil tussen de eventuele netto-opbrengst bij vervreemding en de boekwaarde van het actief. 72 De vergoeding die in winst of verlies moet worden opgenomen uit hoofde van het niet langer opnemen van een materieel vast actief, wordt bepaald in overeenstemming met de vereisten voor het bepalen van de transactieprijs in de alinea’s 47 tot en met 72 van IFRS 15. Verdere wijzigingen van het geschatte vergoedingsbedrag dat in winst of verlies is opgenomen, moeten administratief worden verwerkt in overeenstemming met de in IFRS 15 vervatte vereisten voor wijzigingen van de transactieprijs.

## Informatieverschaffing

73 De jaarrekening moet voor iedere categorie van materiële vaste activa de volgende informatie verschaf fen:
(a) de waarderingsgrondslagen die voor de bepaling van de brutoboekwaarde zijn gebruikt;
(b) de gebruikte afschrijvingsmethoden;
(c) de gebruiksduur of toegepaste afschrijvingspercentages;
(d) de brutoboekwaarde en de geaccumuleerde afschrijvingen (samengevoegd met de geaccumuleerde bijzondere waardeverminderingsverliezen) aan het begin en einde van de periode; en
(e) een aansluiting van de boekwaarde aan het begin en einde van de periode, met vermelding van:
(i) investeringen;
(ii) activa die zijn geclassificeerd als aangehouden voor verkoop of die zijn opgenomen in een groep activa die wordt afgestoten en die is geclassificeerd als aangehouden voor verkoop overeenkomstig IFRS 5, en andere vervreemdingen;
(iii) verwervingen via bedrijfscombinaties;
(iv) stijgingen of dalingen die voortvloeien uit herwaarderingen overeenkomstig de alinea’s 31, 39 en 40 en uit bijzondere waardeverminderingsverliezen die zijn opgenomen in of teruggeboekt uit overige onderdelen van het totaalresultaat in overeenstemming met IAS 36;
(v) bijzondere waardeverminderingsverliezen die in winst of verlies zijn opgenomen overeenkom stig IAS 36;
(vi) bijzondere waardeverminderingsverliezen die in winst of verlies zijn teruggenomen overeen komstig IAS 36;

(vii) afschrijvingen;
(viii) de nettowisselkoersverschillen die voortvloeien uit de omrekening van de functionele valuta in een presentatievaluta, met inbegrip van de omrekening van een buitenlandse activiteit in de presentatievaluta van de verslaggevende entiteit; en
(ix) overige veranderingen. 74 De jaarrekening moet ook de volgende informatie geven:
(a) het bestaan en de bedragen van beperkingen op eigendom en materiële vaste activa die als zekerheid voor verplichtingen zijn verstrekt;
(b) de uitgaven die zijn opgenomen in de boekwaarde van een materieel vast actief in aanbouw; en
(c) het bedrag van contractuele verbintenissen in verband met de verwerving van materiële vaste activa.

## 74A

Indien niet afzonderlijk in het overzicht van het totaalresultaat gepresenteerd, moet de jaarrekening ook de volgende informatie geven:
(a) het in winst of verlies opgenomen bedrag aan vergoedingen van derden voor materiële vaste activa die een bijzondere waardevermindering hebben ondergaan, verloren zijn gegaan of werden opge geven; en
(b) de bedragen van de in overeenstemming met alinea 20A in winst of verlies opgenomen opbrengsten en kosten die betrekking hebben op geproduceerde items niet zijnde output van de normale bedrijfs voering van de entiteit, en in welke post(en) in het overzicht van het totaalresultaat die verplich tingen opbrengsten en kosten zijn opgenomen. 75 De keuze van de afschrijvingsmethode en de schatting van de gebruiksduur van activa zijn een kwestie van beoordeling. Bijgevolg verschaft de vermelding van de toegepaste methoden en de geschatte gebruiksduur of afschrijvingspercentages de gebruikers van jaarrekeningen informatie die hen in staat stelt om het door het management gekozen beleid te beoordelen en vergelijkingen te maken met andere entiteiten. Om soortgelijke redenen is het nodig de volgende informatie te verschaffen:
(a) afschrijvingen gedurende de periode die in winst of verlies zijn opgenomen of die als onderdeel van de kostprijs van andere activa zijn opgenomen; en
(b) de geaccumuleerde afschrijvingen aan het eind van de periode. 76 In overeenstemming met IAS 8 vermeldt een entiteit de aard en het gevolg van een schattingswijziging die een effect heeft in de verslagperiode of die naar verwachting een effect zal hebben in toekomstige perioden. Voor materiële vaste activa kan dergelijke informatie voortvloeien uit schattingswijzigingen met betrekking tot:
(a) restwaarden;
(b) de geschatte kosten van de ontmanteling, de verwijdering of het herstel van materiële vaste activa;
(c) de gebruiksduur; en
(d) de afschrijvingsmethoden. 77 Als materiële vaste activa worden opgenomen tegen geherwaardeerde waarde, moet de volgende in formatie worden vermeld naast de informatie die op grond van IFRS 13 moet worden vermeld:
(a) de ingangsdatum van de herwaardering;

(b) de eventuele betrokkenheid van een onafhankelijke taxateur;
(c) [verwijderd]
(d) [verwijderd]
(e) voor elke geherwaardeerde categorie van materiële vaste activa: de boekwaarde die zou zijn opge nomen als de activa waren geboekt volgens het kostprijsmodel; en
(f) de herwaarderingsreserve, met vermelding van de mutatie daarin en eventuele beperkingen op de uitkering van het saldo aan de aandeelhouders. 78 In overeenstemming met IAS 36 verschaft een entiteit informatie over materiële vaste activa die bijzondere waardeverminderingen hebben ondergaan, naast de informatie die moet worden verstrekt op grond van ali nea 73(e)(iv)-(vi). 79 De volgende informatie kan eveneens relevant zijn voor gebruikers van de jaarrekening:
(a) de boekwaarde van tijdelijk ongebruikte materiële vaste activa;
(b) de brutoboekwaarde van eventuele volledig afgeschreven materiële vaste activa die nog worden gebruikt;
(c) de boekwaarde van materiële vaste activa die buiten dienst zijn gesteld en niet zijn geclassificeerd als aangehouden voor verkoop overeenkomstig IFRS 5; en
(d) indien het kostprijsmodel wordt toegepast, de reële waarde van materiële vaste activa indien deze beduidend verschilt van de boekwaarde. Entiteiten worden daarom aangemoedigd om deze bedragen te vermelden.

## Overgangsbepalingen

80 De vereisten van de alinea’s 24 tot en met 26 met betrekking tot de eerste waardering van een materieel vast actief dat via een ruiltransactie van activa is verworven moeten prospectief en uitsluitend op toekomstige transacties worden toegepast.

## 80A

Alinea 35 is gewijzigd door Jaarlijkse verbeteringen in IFRSs cyclus 2010–2012. Een entiteit moet deze wijziging toepassen op alle herwaarderingen die zijn opgenomen in jaarperioden die op of na de datum van eerste toepassing van deze wijziging aanvangen en in de jaarperiode die daar onmiddellijk aan voorafgaat. Een entiteit mag ook aangepaste vergelijkende informatie voor eerdere perioden presenteren, maar is daartoe niet verplicht. Indien een entiteit niet-aangepaste vergelijkende informatie voor eerdere perioden presenteert, moet zij duidelijk aangeven welke informatie niet is aangepast, vermelden dat deze op basis van een andere grondslag is gepre senteerd, en deze grondslag toelichten.

## 80B

Voor de verslagperiode waarin Landbouw: vruchtdragende planten (wijzigingen in IAS 16 en IAS 41) voor het eerst wordt toegepast, hoeft een entiteit de door alinea 28(f) van IAS 8 vereiste kwantitatieve informatie voor de lopende periode niet te verschaffen. Een entiteit moet de door alinea 28(f) van IAS 8 vereiste kwantitatieve informatie echter wel presenteren voor elke gepresenteerde voorgaande periode.

## 80C

Een entiteit kan ervoor kiezen om voor de verslagperiode waarin Landbouw: vruchtdragende planten (wijzigingen in IAS 16 en IAS 41) voor het eerst wordt toegepast, een post van vruchtdragende planten te waarderen tegen de reële waarde ervan aan het begin van de vroegste periode die in de jaarrekening wordt gepresenteerd, en deze reële waarde als de veronderstelde kostprijs op die datum te hanteren. Een eventueel verschil tussen de vorige boekwaarde en de reële waarde moet aan het begin van de vroegste periode die wordt gepresenteerd, in het beginsaldo van de ingehouden winsten worden opgenomen.

## 80D

De alinea’s 17 en 74 zijn gewijzigd en de alinea’s 20A en 74A zijn toegevoegd door Materiële vaste activa – Opbrengsten vóór beoogd gebruik, uitgegeven in mei 2020. Een entiteit moet deze wijzigingen retroactief toepassen, doch alleen op materiële vaste activa die naar de locatie en in de staat worden gebracht die nodig is om te kunnen functioneren op de door het management beoogde wijze bij of na het begin van de vroegste periode die wordt gepresenteerd in de eerste jaarrekening waarin een entiteit deze wijzigingen voor het eerst toepast. De entiteit moet het cumulatieve effect van de eerste toepassing van de wijziging opnemen als een aanpassing van het beginsaldo van ingehouden winsten (of een andere component van het eigen vermogen, al naargelang het geval) bij het begin van de vroegste periode die wordt gepresenteerd.

## Ingangsdatum

81 Entiteiten moeten deze standaard toepassen op jaarperioden die op of na 1 januari 2005 aanvangen. Eerdere toepassing wordt aanbevolen. Als een entiteit deze standaard toepast op een periode die vóór 1 januari 2005 aanvangt, moet zij dit feit vermelden.

## 81A

Entiteiten moeten de wijzigingen in alinea 3 toepassen op jaarperioden die op of na 1 januari 2006 aanvangen. Indien een entiteit IFRS 6 op een eerdere periode toepast, moeten deze wijzigingen voor die eerdere periode worden toegepast.

## 81B

IAS 1 Presentatie van de jaarrekening (herziene versie van 2007) wijzigde de in de IFRSs gebruikte terminologie. Voorts wijzigde IAS 1 (herziene versie van 2007) de alinea’s 39, 40 en 73(e)(iv). Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2009 aanvangen. Als een entiteit IAS 1 (herziene versie van 2007) toepast op een periode die vóór 1 januari 2009 aanvangt, moeten ook deze wijzigingen op die periode worden toegepast.

## 81C

IFRS 3 Bedrijfscombinaties (herziene versie van 2008) wijzigde alinea 44. Entiteiten moeten die wijziging toepassen op jaarperioden die op of na 1 juli 2009 aanvangen. Als een entiteit IFRS 3 (herziene versie van 2008) op een eerdere periode toepast, moet zij ook deze wijziging op die eerdere periode toepassen.

## 81D

De alinea’s 6 en 69 zijn gewijzigd en alinea 68A is toegevoegd bij Verbeteringen in IFRSs, uitgegeven in mei 2008. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2009 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit de wijzigingen op een eerdere periode toepast, moet zij dit feit ver melden en tegelijkertijd de gerelateerde wijzigingen in IAS 7 Het kasstroomoverzicht toepassen.

## 81E

Alinea 5 is gewijzigd door Verbeteringen in IFRSs, uitgegeven in mei 2008. Entiteiten moeten die wijziging prospectief toepassen op jaarperioden die op of na 1 januari 2009 aanvangen. Eerdere toepassing is toegestaan indien een entiteit tegelijkertijd ook de wijzigingen in de alinea’s 8, 9, 22, 48, 53, 53A, 53B, 54, 57 en 85B van IAS 40 toepast. Als een entiteit de wijziging op een eerdere periode toepast, moet zij dit feit vermelden.

## 81F

IFRS 13, uitgegeven in mei 2011, wijzigde de definitie van reële waarde en de definitie van realiseerbare waarde in alinea 6, wijzigde de alinea’s 26, 35 en 77 en verwijderde de alinea’s 32 en 33. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 13 toepast.

## 81G

Alinea 8 is gewijzigd door de in mei 2012 uitgegeven Verbeteringen cyclus 2009–2011. Entiteiten moeten deze wijziging retroactief toepassen overeenkomstig IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten op jaarperioden die op of na 1 januari 2013 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijziging op een eerdere periode toepast, moet zij dit feit vermelden.

## 81H

Alinea 35 is gewijzigd en alinea 80A is toegevoegd door de in december 2013 uitgegeven Jaarlijkse verbeteringen in IFRSs cyclus 2010–2012. Entiteiten moeten die wijziging toepassen op jaarperioden die op of na 1 juli 2014 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijziging op een eerdere periode toepast, moet zij dit feit vermelden.

## 81I

Alinea 56 is gewijzigd en alinea 62A is toegevoegd bij Verduidelijking van aanvaardbare afschrijvingsmethoden (wij zigingen in IAS 16 en IAS 38), uitgegeven in mei 2014. Entiteiten moeten deze wijzigingen prospectief toepassen op jaarperioden die op of na 1 januari 2016 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden.

## 81J

IFRS 15 Opbrengsten van contracten met klanten, uitgegeven in mei 2014, heeft de alinea’s 68A, 69 en 72 gewijzigd. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 15 toepast.

## 81K

De alinea’s 3, 6 en 37 zijn gewijzigd en de alinea’s 22A, 80B-80C zijn toegevoegd door Landbouw: vruchtdragende planten (wijzigingen in IAS 16 en IAS 41), uitgegeven in juni 2014. Entiteiten moeten deze wijzigingen toepassen op verslagperioden die op of na 1 januari 2016 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden. Entiteiten moeten deze wijzigingen retroactief toepassen in overeenstemming met IAS 8, tenzij anders vermeld in alinea 80C.

## 81L

De alinea’s 4 en 27 zijn verwijderd en de alinea’s 5, 10, 44, 68-69 zijn gewijzigd door IFRS 16, uitgegeven in januari 2016. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 16 toepast.

## 81M

IFRS 17, uitgegeven in mei 2017, heeft de alinea’s 29A en 29B toegevoegd. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 17 toepast.

## 81N

De alinea’s 17 en 74 zijn gewijzigd en de alinea’s 20A, 74A en 80D zijn toegevoegd door Materiële vaste activa – Opbrengsten vóór beoogd gebruik, uitgegeven in mei 2020. Entiteiten moeten deze wijzigingen toepassen op jaarlijkse verslagperioden die op of na 1 januari 2022 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden.

## Intrekking Van Andere Uitspraken

82 Deze standaard vervangt IAS 16 Materiële vaste activa (herziene versie van 1998). 83 Deze standaard vervangt de volgende interpretaties:
(a) SIC-6 Kosten van de aanpassing van bestaande software;
(b) SIC-14 Materiële vaste activa — Vergoeding voor de bijzondere waardevermindering of het verlies van posten; en
(c) SIC-23 Materiële vaste activa – Belangrijke inspectie- of revisiekosten.
