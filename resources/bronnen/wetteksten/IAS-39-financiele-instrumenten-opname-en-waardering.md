---
title: 'IAS-39 — Financiële instrumenten: opname en waardering'
tags:
- '1.5'
- ifrs
- ias
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IAS
standaard_nummer: '39'
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
    pages: 329-353
  tooling:
    pipeline: tools/etl/split_ifrs_verordening.py
    pipeline_version: '1.0'
    model: null
    prompt_version: null
  generated_at: '2026-05-16T19:10:05Z'
  stale: false
  stale_reason: null
  trust:
    status: unreviewed
    confirmed_at: null
    confirmed_by: null
    rationale: 'ETL-output: pymupdf-extractie + heading-detectie (DOEL/TOEPASSINGSGEBIED/DEFINITIES
      etc.) + paragraph-merge. QA-pass nodig om heading-correctheid en incidentele
      woord-splits (zoals ''op brengstwaarde'', erfgenaam van PDF-kolom-wrap) te valideren.
      EU-publicatieblad CELEX 32023R1803 = primary law.'
---

## International Accounting Standard 39

Financiële instrumenten: opname en waardering

## Toepassingsgebied

2 Deze standaard moet door alle entiteiten worden toegepast op alle financiële instrumenten die binnen het toepassingsgebied van IFRS 9 Financiële instrumenten vallen, mits en voor zover:
(a) IFRS 9 toestaat dat de vereisten inzake hedge accounting van deze standaard worden toegepast; en
(b) het financiële instrument deel uitmaakt van een hedgerelatie die in overeenstemming met deze standaard voor hedge accounting in aanmerking komt.

## 2A–7

[Verwijderd]

## Definities

8 De begrippen die in IFRS 13, IFRS 9 en IAS 32 worden gedefinieerd, worden in deze standaard gebruikt met de in bijlage A bij IFRS 13, bijlage A bij IFRS 9 en alinea 11 van IAS 32 vermelde betekenis. IFRS 13, IFRS 9 en IAS 32 bevatten een definitie van de volgende begrippen: — geamortiseerde kostprijs van een financieel actief of een financiële verplichting — niet langer opnemen — derivaat — effectieverentemethode — effectieve rentevoet — eigenvermogensinstrument — reële waarde — financieel actief — financieel instrument — financiële verplichting en verschaffen een leidraad voor de toepassing van die definities. 9 De volgende begrippen worden in deze standaard gebruikt met de hierna omschreven betekenis: Definities in verband met hedge accounting Een vaststaande toezegging is een bindende overeenkomst voor de ruil van een bepaalde hoeveelheid eco nomische middelen tegen een bepaalde prijs op een bepaalde datum of op bepaalde data in de toekomst. Een verwachte toekomstige transactie is een toekomstige transactie waarvoor nog geen verplichting is aange gaan maar die waarschijnlijk is. Een hedge-instrument is een aangemerkt derivaat of (uitsluitend voor een hedge van het risico van ver anderingen in valutakoersen) een aangemerkt niet-afgeleid financieel actief of niet-afgeleide financiële ver plichting waarvan de reële waarde of kasstromen naar verwachting veranderingen in de reële waarde van of kasstromen uit een aangemerkte gehedgede positie (in de alinea’s 72 tot en met 77 en bijlage A, de alinea’s TL94 tot en met TL97 wordt de definitie van een hedge-instrument verder uitgewerkt) zullen compenseren.

Een gehedgede positie is een actief, verplichting, vaststaande toezegging, zeer waarschijnlijke verwachte toekomstige transactie of een netto-investering in een buitenlandse entiteit dat, respectievelijk die, a) de entiteit blootstelt aan het risico van veranderingen in de reële waarde of toekomstige kasstromen en b) wordt aangemerkt als zijnde gehedged (in de alinea’s 78 tot en met 84 en bijlage A, alinea’s TL98 tot en met TL101 wordt de definitie van gehedgede positie verder uitgewerkt). Hedge-effectiviteit is de mate waarin veranderingen in de reële waarde van of kasstromen uit het hedge- instrument compensatie bieden voor veranderingen in de reële waarde van of kasstromen uit de gehedgede positie die zijn toe te rekenen aan een gehedged risico (zie bijlage A, alinea’s TL105 tot en met TL 113A). 10-70 [Verwijderd]

## Hedging

71 Indien een entiteit IFRS 9 toepast en er niet voor heeft gekozen om de vereisten van deze standaard inzake hedge accounting als grondslag voor financiële verslaggeving te blijven toepassen (zie alinea 7.2.21 van IFRS 9), past zij de in hoofdstuk 6 van IFRS 9 vervatte vereisten inzake hedge accounting toe. Bij een reële-waardehedge van het renterisico van een deel van een porte feuille van financiële activa of financiële verplichtingen mag een entiteit in overeenstemming met alinea 6.1.3 van IFRS 9 echter de vereisten van deze standaard inzake hedge accounting in plaats van die van IFRS 9 toepassen. In dat geval moet de entiteit ook de specifieke vereisten inzake reële-waarde-hedge-accounting ten behoeve van een portefeuillehedge van het renterisico toepas sen (zie de alinea’s 81A, 89A en TL114 tot en met TL132). Hedge-instrumenten In aanmerking komende instrumenten 72 Deze standaard stelt geen beperkingen aan de omstandigheden waarin een derivaat als een hedge-instru ment kan worden aangemerkt, mits wordt voldaan aan de voorwaarden in alinea 88, uitgezonderd be paalde geschreven opties (zie bijlage A, alinea TL94). Een financieel actief of financiële verplichting, niet zijnde een derivaat, kan echter alleen als een hedge-instrument worden aangemerkt voor een hedge van valutarisico. 73 Ten behoeve van hedge accounting kunnen alleen instrumenten als hedge-instrument worden aangemerkt waarbij een partij buiten de verslaggevende entiteit (d.w.z. buiten de groep of de individuele entiteit waarover wordt gerapporteerd) is betrokken. Hoewel individuele entiteiten binnen een geconsolideerde groep, of divisies binnen een entiteit, individueel hedges kunnen sluiten met andere entiteiten binnen de groep, of andere divisies binnen de entiteit, worden eventuele winsten en verliezen op dergelijke transacties binnen een groep bij consolidatie geëlimineerd. Dergelijke hedges komen derhalve niet in aanmerking voor hedge accounting in de geconsolideerde jaarrekening van de groep. Zij kunnen echter wel voor hedge accounting in aanmerking komen in de individuele of enkelvoudige jaarrekening van individuele entiteiten binnen de groep, mits deze transacties partijen betreffen buiten de individuele entiteit waarover wordt gerapporteerd. Aanwijzing van hedge-instrumenten 74 Normaliter wordt de reële waarde van een hedge-instrument in zijn geheel bepaald en zijn de factoren die de veranderingen in reële waarde veroorzaken onderling afhankelijk. Bijgevolg wordt door een entiteit een hedge-instrument als geheel aangemerkt voor een hedgerelatie. De enige toegestane uitzonderingen zijn:
(a) splitsing van de intrinsieke waarde en de tijdswaarde van een optiecontract, waarbij alleen de ver andering in de intrinsieke waarde van een optie als hedge-instrument wordt aangemerkt, en de ver andering in de tijdswaarde wordt uitgesloten; en
(b) splitsing van het rentedeel en de contante prijs bij een termijncontract. Deze uitzonderingen zijn toegestaan omdat de intrinsieke waarde van de optie en de premie op het termijncontract over het algemeen afzonderlijk te bepalen zijn. Een dynamische hedgingstrategie waarbij zowel de intrinsieke waarde als de tijdswaarde van een optiecontract worden beoordeeld, kan voldoen aan de voorwaarden voor hedge accounting.

75 Een gedeelte van het gehele hedge-instrument, zoals 50 procent van het nominale bedrag, mag worden aangewezen als hedge-instrument in een hedgerelatie. Een hedgerelatie mag echter niet worden aangemerkt voor slechts een deel van de tijd dat een hedge-instrument uitstaat. 76 Een individueel hedge-instrument kan worden aangemerkt als hedge van meer dan één soort risico mits a) de gehedgede risico’s duidelijk identificeerbaar zijn; b) de effectiviteit van de hedge aantoonbaar is, en c) gegarandeerd kan worden dat het hedge-instrument en de verschillende risicoposities specifiek worden aangemerkt. 77 Twee of meer derivaten, of gedeelten daarvan (of, in geval van een hedge van valutarisico, twee of meer niet-derivaten of gedeelten daarvan, of een combinatie van derivaten en niet-derivaten of gedeelten daar van), mogen in combinatie worden beschouwd en gezamenlijk als hedge-instrument worden aangemerkt, ook wanneer het risico dat uit sommige derivaten voortvloeit, of de risico’s die uit sommige derivaten voortvloeien, de risico’s die uit andere derivaten voortvloeien, compenseert, respectievelijk compenseren. Een “interest rate collar” of ander afgeleid instrument waarin een geschreven optie en een gekochte optie worden gecombineerd, komt echter niet in aanmerking als hedge-instrument, indien dit afgeleide instru ment in feite een op nettobasis geschreven optie is (waarvoor een nettopremie wordt ontvangen). Evenzo kunnen twee of meer instrumenten (of gedeelten daarvan) alleen als hedge-instrument worden aangemerkt indien geen van de instrumenten een (netto) geschreven optie is. Gehedgede posities In aanmerking komende posities 78 Een gehedgede positie kan zijn een actief of verplichting, een niet-opgenomen vaststaande toezegging, een zeer waarschijnlijke verwachte toekomstige transactie of een netto-investering in een buitenlandse entiteit. De gehedgede positie kan zijn: a) één actief, verplichting, vaststaande toezegging, zeer waarschijnlijke verwachte toekomstige transactie of één netto-investering in een buitenlandse entiteit; b) een groep activa, verplichtingen, vaststaande toezeggingen, zeer waarschijnlijke verwachte toekomstige transacties of netto- investeringen in een buitenlandse entiteit met een vergelijkbaar risico, of c) uitsluitend in geval van een portefeuillehedge van et renterisico, een gedeelte van de portefeuille van financiële activa of financiële verplichtingen die blootgesteld zijn aan hetzelfde, gehedgede risico. 79 [Verwijderd] 80 Ten behoeve van hedge accounting kunnen alleen activa, verplichtingen, vaststaande toezeggingen en zeer waarschijnlijke verwachte toekomstige transacties als gehedgede positie worden aangewezen, indien daarbij een partij buiten de entiteit is betrokken. Dit houdt in dat de toepassing van hedge accounting op transacties tussen entiteiten in dezelfde groep alleen is toegestaan in de individuele of enkelvoudige jaar rekening van die entiteiten en niet in de geconsolideerde jaarrekening van de groep, behalve wat de geconsolideerde jaarrekening van een beleggingsentiteit (zoals gedefinieerd in IFRS 10) betreft, waarin transacties tussen een beleggingsentiteit en haar dochterondernemingen die worden gewaardeerd tegen reële waarde met verwerking van waardeveranderingen in winst of verlies, niet in de geconsolideerde jaarrekening worden geëlimineerd. Een uitzondering hierop wordt gevormd door het valutarisico van een monetaire intragroepspost (bv. een vordering-schuldverhouding tussen twee dochterondernemingen), die als gehedgede positie in aanmerking kan komen indien deze resulteert in een risicopositie waarbij valutawinsten en -verliezen kunnen optreden die overeenkomstig IAS 21 De gevolgen van wisselkoerswijzi gingen bij consolidatie niet volledig worden geëlimineerd. Overeenkomstig IAS 21 worden winsten en verliezen uit wisselkoersverschillen op monetaire intragroepsposten bij consolidatie niet volledig geëlimi neerd indien de monetaire intragroepspost een transactie betreft tussen twee groepsentiteiten met een verschillende functionele valuta. Daarnaast kan het valutarisico van een zeer waarschijnlijke verwachte toekomstige intragroepstransactie in de geconsolideerde jaarrekening als gehedgede positie in aanmerking komen, mits de transactie luidt in een valuta die verschilt van de functionele valuta van de entiteit die die transactie aangaat, en het valutarisico de geconsolideerde winst of het geconsolideerde verlies beïnvloedt.

Aanwijzing van financiële posities als gehedgede positie 81 Is de gehedgede positie een financieel actief of een financiële verplichting, dan kan het zijn dat slechts de risico’s die verbonden zijn aan een deel van de kasstromen of reële waarde (zoals een of meer bepaalde contractuele kasstromen of delen daarvan, of een percentage van de reële waarde) zijn gehedged, mits de effectiviteit van de hedge te bepalen valt. Een identificeerbaar en afzonderlijk te bepalen gedeelte van het renterisico van een rentedragend actief of rentedragende verplichting kan bijvoorbeeld als het gehedgede risico worden aangemerkt (zoals de component van de risicovrije rentevoet of referentierente in de totale renterisicopositie van een gehedged financieel instrument).

## 81A

Bij een reële-waardehedge van het renterisico van een portefeuille van financiële activa of financiële ver plichtingen (en uitsluitend bij een dergelijke hedge) mag het gehedgede gedeelte worden aangemerkt in de vorm van een bedrag in een bepaalde valuta (bv. een bedrag in dollar, euro, pond of rand) in plaats van als individuele activa (of verplichtingen). Hoewel de portefeuille, voor risicobeheerdoeleinden, activa en ver plichtingen kan omvatten, is het aangemerkte bedrag een activabedrag of een verplichtingenbedrag. Aan wijzing van een nettobedrag bestaande uit activa en verplichtingen is niet toegestaan. De entiteit mag een gedeelte van het met dit aangemerkte bedrag verbonden renterisico hedgen. In geval van bijvoorbeeld een hedge van een portefeuille die vervroegd aflosbare activa bevat, mag de entiteit de verandering in de reële waarde hedgen die is toe te schrijven aan een verandering in de gehedgede rentevoet op basis van de verwachte, in plaats van de contractuele, renteherzieningsdata. […]. Aanwijzing van niet-financiële posities als gehedgede positie 82 Is de gehedgede positie een niet-financieel actief of niet-financiële verplichting, dan moet deze worden aangemerkt als gehedgede positie a) voor valutarisico’s, of b) als geheel voor alle risico’s omdat het moeilijk is het juiste deel van de kasstromen of wijzigingen in reële waarde die aan andere specifieke risico’s dan valutarisico’s zijn toe te rekenen, af te zonderen en te bepalen. Aanwijzing van groepen van posities als gehedgede positie 83 Vergelijkbare activa en vergelijkbare verplichtingen moeten alleen samengevoegd en als groep gehedged worden indien de afzonderlijke activa of verplichtingen in de groep het risico delen dat als gehedged risico wordt aangemerkt. Verder wordt voor elke afzonderlijke positie in de groep de verandering in de reële waarde die is toe te rekenen aan het gehedgede risico geacht ongeveer evenredig te zijn aan de totale verandering in de reële waarde die is toe te rekenen aan het gehedgede risico van de groep van posities. 84 Aangezien een entiteit de hedge-effectiviteit beoordeelt door vergelijking van de verandering in de reële waarde van of de kasstroom uit een hedge-instrument (of groep van vergelijkbare hedge-instrumenten) met die van een gehedgede positie (of groep van vergelijkbare gehedgede posities) voldoet vergelijking van een hedge-instrument met een totale nettopositie, in plaats van met een specifieke gehedgede positie, niet aan de voorwaarden voor hedge accounting (bv. het nettosaldo van alle vastrentende activa en vastrentende verplichtingen met een vergelijkbare looptijd). Hedge accounting 85 Bij hedge accounting wordt rekening gehouden met de tegengestelde effecten op de winst of het verlies van veranderingen in de reële waarde van het hedge-instrument en van de gehedgede positie. 86 Er zijn drie soorten hedge-relaties:
(a) reële-waardehedge : een hedge van het risico van veranderingen in de reële waarde van een opgenomen actief of verplichting, of een niet-opgenomen vaststaande toezegging, of een vastgesteld deel van een dergelijk actief, een dergelijke verplichting, of vaststaande toezegging, die verband houden met een bepaald risico en invloed zouden kunnen hebben op de winst of het verlies;

(b) kasstroomhedge: een hedge van de mogelijke variabiliteit van kasstromen die i) is toe te rekenen aan een bepaald risico dat is verbonden met een opgenomen actief of verplichting (zoals een aantal of alle toekomstige rentebetalingen op een schuld met een variabele rente) of een zeer waarschijnlijke ver wachte toekomstige transactie en ii) invloed zou kunnen hebben op de winst of het verlies;
(c) hedge van een netto-investering in een buitenlandse activiteit zoals gedefinieerd in IAS 21. 87 Een hedge van het valutarisico van een vaststaande toezegging mag administratief worden verwerkt als een reële-waardehedge of als een kasstroomhedge. 88 Een hedgerelatie komt voor hedge accounting overeenkomstig de alinea’s 89 tot en met 102 in aanmerking als en alleen als aan alle onderstaande voorwaarden is voldaan:
(a) Bij het afsluiten van de hedge wordt de hedgerelatie formeel aangemerkt en gedocumenteerd, evenals de doelstelling van de entiteit ten aanzien van risicobeheer en haar strategie bij het aangaan van de hedge. In die documentatie moet het volgende worden opgenomen: een aan duiding van het hedge-instrument, de gehedgede positie of transactie, de aard van het te hedgen risico en hoe de entiteit zal beoordelen in hoeverre het hedge-instrument effectief is bij het compenseren van het risico van veranderingen in de reële waarde van de gehedgede positie of aan het gehedgede risico toe te rekenen kasstromen.
(b) De hedge is naar verwachting zeer effectief (zie bijlage A, alinea’s TL105 tot en met TL113A) in het bereiken van compensatie van aan het gehedgede risico toe te rekenen veranderingen in reële waarde of kasstromen, en wel in overeenstemming met de oorspronkelijk gedocumen teerde strategie voor risicobeheer voor die bepaalde hedgerelatie.
(c) Bij kasstroomhedges moet de verwachte toekomstige transactie die het voorwerp van de hedge is, zeer waarschijnlijk zijn en een risicopositie opleveren wat betreft veranderingen in kas stromen die uiteindelijk van invloed kunnen zijn op de winst of het verlies.
(d) De effectiviteit van de hedge kan betrouwbaar worden bepaald, d.w.z. dat de reële waarde of de kasstromen van de gehedgede positie die toerekenbaar is/zijn aan het gehedgede risico en de reële waarde van het hedge-instrument betrouwbaar kunnen worden bepaald.
(e) De hedge wordt voortdurend beoordeeld, waarbij wordt vastgesteld dat de hedge gedurende de verslagperioden waarvoor de hedge was bedoeld, feitelijk zeer effectief is geweest. Reële-waardehedges 89 Indien een reële-waardehedge gedurende de periode voldoet aan de voorwaarden in alinea 88, moet die administratief als volgt worden verwerkt:
(a) de winst of het verlies uit herwaardering van het hedge-instrument op reële waarde (bij een afgeleid hedge-instrument) of de vreemdevalutacomponent in de overeenkomstig IAS 21 be paalde boekwaarde (bij een niet-afgeleid hedge-instrument) moet onmiddellijk in winst of verlies worden opgenomen; en
(b) de winst of het verlies op de gehedgede positie die, respectievelijk dat, aan het gehedgede risico is toe te rekenen, moet leiden tot aanpassing van de boekwaarde van de gehedgede positie en moet in winst of verlies worden opgenomen. Dit geldt eveneens indien de gehed gede positie anders tegen kostprijs wordt gewaardeerd. De winst die of het verlies dat aan het gehedgede risico is toe te rekenen, wordt in winst of verlies opgenomen indien de gehedgede positie een financieel actief is dat overeenkomstig alinea 4.1.2A van IFRS 9 tegen reële waarde met verwerking van waardeveranderingen in de overige onderdelen van het totaalresultaat wordt gewaardeerd.

## 89A

In geval van een reële-waardehedge van het renterisico van een gedeelte van een portefeuille van financiële activa of financiële verplichtingen (en uitsluitend bij een dergelijke hedge) kan aan de vereiste in alinea 89
(b) worden voldaan door de aan de gehedgede positie toe te schrijven winst of het aan de gehedgede positie toe te schrijven verlies te presenteren hetzij:

(a) als een afzonderlijke post onder de activa, gedurende renteherzieningsperioden waarin de gehedgede positie een actief is; dan wel
(b) als een afzonderlijke post onder de verplichtingen, gedurende de renteherzieningsperioden waarin de gehedgede positie een verplichting is. De afzonderlijke post waarnaar bij (a) en (b) hierboven wordt verwezen, moet direct na de financiële activa of financiële verplichtingen worden gepresenteerd. In deze posten opgenomen bedragen moeten uit het overzicht van de financiële positie worden verwijderd wanneer de activa of verplichtingen waarop zij betrekking hebben, niet langer worden opgenomen. 90 Indien er alleen bepaalde aan een gehedgede positie toe te rekenen risico’s worden gehedged, worden niet aan het gehedgede risico gerelateerde, opgenomen veranderingen in de reële waarde van de gehedgede positie opgenomen zoals uiteengezet in alinea 5.7.1 van IFRS 9. 91 Een entiteit moet de in alinea 89 vermelde hedge accounting voor de toekomst staken indien:
(a) het hedge-instrument afloopt of wordt verkocht, beëindigd of uitgeoefend. Voor de toepassing van dit punt wordt vervanging of telkens vernieuwen (“roll-over”) van een hedge-instrument in een ander hedge-instrument niet beschouwd als expiratie of beëindiging indien deze vervanging of vernieuwing deel uitmaakt van de gedocumenteerde hedgingstrategie van de entiteit. Daarnaast is er voor de toepassing van deze alinea geen sprake van aflopen of beëindigen van het hedge-instrument indien:
(i) de partijen bij het hedge-instrument als gevolg van wet- of regelgeving of de invoering van wet- of regelgeving overeenkomen dat een of meer clearingtegenpartijen in de plaats komen van hun oorspronkelijke tegenpartij en de nieuwe tegenpartij van elk van de partijen worden. Voor de toepassing van dit punt is een clearingtegenpartij een centrale tegenpartij (soms een “clearing organisatie” of “clearinginstituut ” genoemd), dan wel een entiteit of entiteiten, zoals een clearing member van een clearingorganisatie of een cliënt van een clearing member van een clearingorga nisatie, die als tegenpartij optreden om tot clearing door een centrale tegenpartij over te gaan. Als de bij het hedge-instrument betrokken partijen hun oorspronkelijke tegenpartijen echter door andere tegenpartijen vervangen, is deze alinea enkel van toepassing indien elk van deze partijen met dezelfde centrale tegenpartij tot clearing overgaan;
(ii) eventuele andere wijzigingen in het hedge-instrument beperkt blijven tot de wijzigingen die noodzakelijk zijn om tot een dergelijke vervanging van de tegenpartij over te gaan. Deze wijzigingen blijven beperkt tot wijzigingen die in overeenstemming zijn met de te verwachten voorwaarden indien het hedge-instrument oorspronkelijk met de clearingtegen partij zou zijn gecleard. Deze wijzigingen omvatten wijzigingen in de zekerheidsvereisten, in de rechten om handelsvorderingen en -schulden te salderen, en in geheven lasten.
(b) de hedge niet langer voldoet aan de criteria voor hedge accounting in alinea 88; dan wel
(c) de entiteit de aanwijzing intrekt. 92 Aanpassingen naar aanleiding van alinea 89(b) van de boekwaarde van een gehedged financieel instrument waarvoor de effectieverentemethode wordt gehanteerd (of, in het geval van een hedge van het renterisico van een portefeuille, van de afzonderlijke post in het overzicht van de finan ciële positie die in alinea 89A wordt beschreven) moeten in winst of verlies worden geamorti seerd. De amortisatie kan beginnen zodra een aanpassing zich voordoet en moet uiterlijk aan vangen wanneer de gehedgede positie niet meer wordt aangepast voor veranderingen in de reële waarde die aan het te hedgen risico zijn toe te rekenen. De aanpassing wordt gebaseerd op een herberekende effectieve rentevoet op de datum waarop met amortisatie wordt begonnen. Indien echter, in geval van een reële-waardehedge van het renterisico van een portefeuille van financiële activa of financiële verplichtingen (en uitsluitend bij een dergelijke hedge) amortisatie via een herberekende effectieve rentevoet niet uitvoerbaar is, moet de aanpassing volgens een lineaire methode worden geamortiseerd. De aanpassing moet aan het eind van de looptijd van het finan ciële instrument of, in het geval van een hedge van het renterisico van een portefeuille, aan het eind van de relevante renteherzieningsperiode, volledig geamortiseerd zijn.

93 Bij aanwijzing van een niet-opgenomen vaststaande toezegging als gehedgede positie wordt de daarna optredende cumulatieve verandering in de reële waarde van de aan het te hedgen risico toe te rekenen vaststaande toezegging als een actief of een verplichting opgenomen, waarbij een overeenkomstige winst of overeenkomstig verlies in winst of verlies wordt opgenomen (zie alinea 89(b)). De veranderingen in de reële waarde van het hedge-instrument worden ook in winst of verlies opgenomen. 94 Wanneer een entiteit een vaststaande toezegging doet om een actief te verwerven of een verplichting aan te gaan dat, respectievelijk die, een gehedgede positie is in een reële-waardehedge, wordt de eerste boek waarde van het actief of de verplichting die voortvloeit uit het door de entiteit nakomen van de vast staande toezegging, aangepast voor de cumulatieve verandering in de reële waarde van de vaststaande toezegging, die is toe te rekenen aan de gehedgede positie die in het overzicht van de financiële positie is opgenomen. Kasstroomhedges 95 Indien een kasstroomhedge gedurende de periode voldoet aan de voorwaarden in alinea 88, moet ze administratief als volgt worden verwerkt:
(a) het deel van de winst of het verlies op het hedge-instrument waarvan is vastgesteld dat het een effectieve hedge is (zie alinea 88), moet in de overige onderdelen van het totaalresultaat worden opgenomen; en
(b) het niet-effectieve deel van de winst of het verlies op het hedge-instrument moet in winst of verlies worden opgenomen. 96 Meer specifiek wordt een kasstroomhedge administratief als volgt verwerkt:
(a) de afzonderlijke, met de gehedgede positie samenhangende eigenvermogenscomponent wordt aange past naar de laagste van de volgende waarden (in absolute bedragen):
(i) de cumulatieve winst of het cumulatieve verlies op het hedge-instrument vanaf afsluiting van de hedge; en
(ii) de cumulatieve verandering in de reële waarde (contante waarde) van de verwachte toekomstige kasstromen uit de gehedgede positie vanaf afsluiting van de hedge;
(b) een eventueel resterende winst of resterend verlies op het hedge-instrument of een aangemerkt deel daarvan (dat geen effectieve hedge vormt) wordt in winst of verlies opgenomen; en
(c) indien volgens de gedocumenteerde risicobeheerstrategie van een entiteit ten aanzien van een bepaalde hedgerelatie een bepaald onderdeel van de winst of het verlies of de daaraan gerelateerde kasstromen van het hedge-instrument van beoordeling van de hedge-effectiviteit wordt uitgesloten (zie de ali nea’s 74, 75 en 88(a)), wordt dat uitgesloten onderdeel van de winst of het verlies opgenomen in overeenstemming met alinea 5.7.1 van IFRS 9. 97 Leidt een hedge van een verwachte toekomstige transactie tot de opname van een financieel actief of een financiële verplichting, dan moeten de daarmee verbonden winsten of verliezen die over eenkomstig alinea 95 in de overige onderdelen van het totaalresultaat zijn opgenomen, van het eigen vermogen naar de winst of het verlies worden overgeboekt als een herclassificatieaanpassing (zie IAS 1 (herziene versie van 2007)) in dezelfde periode of perioden waarin de gehedgede verwachte toekomstige kasstromen van invloed zijn op de winst of het verlies (zoals in de perioden waarin rentebaten en -lasten worden opgenomen). Verwacht een entiteit echter dat een (deel van een) verlies dat in de overige onderdelen van het totaalresultaat is verwerkt in een of meer toekomstige perioden niet realiseerbaar zal zijn, dan moet zij het naar verwachting niet-realiseerbare bedrag overboeken naar de winst of het verlies als een herclassificatieaanpassing. 98 Indien een hedge van een verwachte toekomstige transactie tot de opname van een niet-financieel actief of een niet-financiële verplichting leidt, of indien een verwachte toekomstige transactie betreffende een niet-financieel actief of niet-financiële verplichting een vaststaande toezegging wordt waarvoor reële-waarde-hedge-accounting wordt toegepast, dan moet de entiteit op de bij
(a) en (b) beschreven wijze handelen:

(a) De entiteit boekt de hiermee samenhangende winsten en verliezen die overeenkomstig ali nea 95 in de overige onderdelen van het totaalresultaat zijn opgenomen over naar de winst of het verlies als een herclassificatieaanpassing (zie IAS 1 (herziene versie van 2007)) in dezelfde periode of perioden waarin het verworven actief of de aangegane verplichting de winst of het verlies beïnvloedt (zoals de perioden waarin afschrijvingskosten of de kostprijs van de omzet wordt opgenomen). Verwacht een entiteit echter dat een (deel van een) verlies dat in de overige onderdelen van het totaalresultaat is verwerkt in een of meer toekomstige perioden niet recupereerbaar zal zijn, dan moet zij het naar verwachting niet-recupereerbare bedrag overboeken van het eigen vermogen naar de winst of het verlies als een herclassificatieaan passing.
(b) De entiteit boekt de hiermee samenhangende winsten en verliezen die in overeenstemming met alinea 95 in de overige onderdelen van het totaalresultaat zijn verwerkt over om deze op te nemen in de eerste kostprijs of andere boekwaarde van het actief of de verplichting. 99 Een entiteit moet één van de twee mogelijkheden (a) en (b) in alinea 98 kiezen als grondslag voor financiële verslaggeving en deze consistent toepassen op alle hedges waarop alinea 98 betrekking heeft. 100 Voor andere kasstroomhedges dan die welke in de alinea’s 97 en 98 worden besproken, moeten bedragen die in de overige onderdelen van het totaalresultaat waren opgenomen, overgeboekt worden van het eigen vermogen naar de winst of het verlies als een herclassificatieaanpassing (zie IAS 1 (herziene versie van 2007)) in dezelfde periode(n) waarin de gehedgede verwachte toekom stige kasstromen de winst of het verlies beïnvloeden (bijvoorbeeld wanneer een verwachte ver koop werkelijk plaatsvindt). 101 In elk van de volgende omstandigheden moet een entiteit de in de alinea’s 95 tot en met 100 uiteengezette hedge accounting voor de toekomst staken:
(a) Het hedge-instrument loopt af of wordt verkocht, beëindigd of uitgeoefend. In dit geval moet de cumulatieve winst of het cumulatieve verlies op het hedge-instrument die, respectievelijk dat, eerst in de overige onderdelen van het totaalresultaat werd verwerkt toen er sprake was van een effectieve hedge (zie alinea 95(a)), afzonderlijk in het eigen vermogen blijven tot de verwachte toekomstige transactie plaatsvindt. Wanneer de transactie plaatsvindt, is alinea 97, 98 of 100 van toepassing. Voor de toepassing van dit punt wordt vervanging of telkens vernieuwen (“roll-over”) van een hed ge-instrument in een ander hedge-instrument niet beschouwd als expiratie of beëindiging indien deze vervanging of vernieuwing deel uitmaakt van de gedocumenteerde hedgingstrategie van de entiteit. Daarnaast is er voor de toepassing van dit punt geen sprake van expiratie of beëindiging van het hedge-instrument indien:
(i) de partijen bij het hedge-instrument als gevolg van wet- of regelgeving of de invoering van wet- of regelgeving overeenkomen dat een of meer clearingtegenpartijen in de plaats komen van hun oorspronkelijke tegenpartij en de nieuwe tegenpartij van elk van de partijen worden. Voor de toepassing van dit punt is een clearingtegenpartij een centrale tegenpartij (soms een “clearing organisatie” of “clearinginstituut ” genoemd), dan wel een entiteit of entiteiten, zoals een clearinglid van een clearingorganisatie of een cliënt van een clearinglid van een clearingorganisatie, die als tegenpartij optreden om tot clearing door een centrale tegenpartij over te gaan. Als de bij het hedge-instrument betrokken partijen hun oorspronkelijke tegenpartijen echter door andere tegen partijen vervangen, is deze alinea enkel van toepassing indien elk van deze partijen met dezelfde centrale tegenpartij tot clearing overgaan;
(ii) eventuele andere wijzigingen in het hedge-instrument beperkt blijven tot de wijzigingen die noodzakelijk zijn om tot een dergelijke vervanging van de tegenpartij over te gaan. Deze wijzigingen blijven beperkt tot wijzigingen die in overeenstemming zijn met de te verwachten voorwaarden indien het hedge-instrument oorspronkelijk met de clearingtegen partij zou zijn gecleard. Deze wijzigingen omvatten wijzigingen in de zekerheidsvereisten, in de rechten om handelsvorderingen en -schulden te salderen, en in geheven lasten.

(b) De hedge voldoet niet langer aan de criteria voor hedge accounting in alinea 88. In dit geval moet de cumulatieve winst of het cumulatieve verlies op het hedge-instrument die, respectie velijk dat, eerst in de overige onderdelen van het totaalresultaat werd verwerkt toen er sprake was van een effectieve hedge (zie alinea 95(a)), afzonderlijk in het eigen vermogen blijven tot de verwachte toekomstige transactie plaatsvindt. Wanneer de transactie plaatsvindt, is ali nea 97, 98 of 100 van toepassing.
(c) De verwachte toekomstige transactie zal naar verwachting niet meer plaatsvinden, in welk geval een hiermee samenhangend(e) cumulatieve winst of cumulatief verlies op het hedge- instrument die, respectievelijk dat, vanaf de periode waarin de hedge effectief was, rechtstreeks in het eigen vermogen opgenomen blijft (zie alinea 95(a)), als een herclassificatieaanpassing van het eigen vermogen naar de winst of het verlies worden overgeboekt. Een verwachte toe komstige transactie die niet meer zeer waarschijnlijk zal plaatsvinden (zie alinea 88(c)), kan nog wel naar verwachting plaatsvinden.
(d) De entiteit trekt de aanwijzing in. Bij hedges van een verwachte toekomstige transactie moet de cumulatieve winst of het cumulatieve verlies op het hedge-instrument die, respectievelijk dat, eerst in de overige onderdelen van het totaalresultaat werd verwerkt toen er sprake was van een effectieve hedge (zie alinea 95(a)), afzonderlijk in het eigen vermogen blijven tot de verwachte toekomstige transactie plaatsvindt of naar verwachting niet meer zal plaatsvinden. Wanneer de transactie plaats vindt, is alinea 97, 98 of 100 van toepassing. Indien de transactie naar verwachting niet meer zal plaatsvinden, moet de cumulatieve winst die, of het cumulatieve verlies dat, rechtstreeks in de overige onderdelen van het totaalresultaat was opgenomen, overgeboekt worden van het eigen vermogen naar de winst of het verlies als een herclassificatieaanpassing. Hedges van een netto-investering in een buitenlandse entiteit 102 Hedges van een netto-investering in een buitenlandse activiteit, met inbegrip van een monetaire post die als deel van de netto-investering wordt verwerkt (zie IAS 21), moeten op vergelijkbare wijze worden verwerkt als kasstroomhedges:
(a) het deel van de winst of het verlies op het hedge-instrument waarvan is vastgesteld dat het een effectieve hedge is (zie alinea 88) moet in de overige onderdelen van het totaalresultaat wor den opgenomen; en
(b) het niet-effectieve deel moet in winst of verlies worden opgenomen. De winst of het verlies op het hedge-instrument met betrekking tot het effectieve deel van de hedge dat in de overige onderdelen van het totaalresultaat is opgenomen, moet bij afstoting of gedeeltelijke afstoting van de buitenlandse entiteit worden overgeboekt van het eigen vermogen naar de winst of het verlies als een herclassificatieaanpassing (zie IAS 1 (herziene versie van 2007)) in overeenstemming met de alinea’s 48 en 49 van IAS 21. Tijdelijke uitzonderingen van de toepassing van specifieke vereisten inzake hedge accounting

## 102A

Entiteiten moeten de alinea’s 102D tot en met 102N en alinea 108G toepassen op alle hedgerelaties waarop de rentebenchmarkhervorming rechtstreeks van invloed is. Deze alinea’s zijn enkel op dergelijke hedgerelaties van toepassing. De rentebenchmarkhervorming is enkel rechtstreeks op een hedgerelatie van invloed als de hervorming aanleiding geeft tot onzekerheden in verband met:
(a) de (al dan niet contractueel gespecificeerde) rentebenchmark die als een gehedged risico is aangemerkt; en/of
(b) het tijdstip of het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit de gehedgede positie of het hedge-instrument voortvloeien.

## 102B

Voor de toepassing van de alinea’s 102D tot en met 102N verwijst de term “rentebenchmarkhervorming ” naar de marktbrede hervorming van een rentebenchmark, met inbegrip van de vervanging van een rentebenchmark door een alternatieve referentierente, zoals die welke voortvloeit uit de aanbevelingen in het verslag van de Financial Stability Board van juli 2014 met als titel “Reforming Major Interest Rate Benchmarks” ( 26 ). ( 26 ) Het verslag “Reforming Major Interest Rate Benchmarks” is te vinden op http://www.fsb.org/wp-content/uploads/r_140722.pdf

## 102C

De alinea’s 102D tot en met 102N voorzien enkel in uitzonderingen op de in de genoemde alinea’s ge specificeerde vereisten. Een entiteit moet alle andere vereisten inzake hedge accounting blijven toepassen op hedgerelaties waarop de rentebenchmarkhervorming rechtstreeks van invloed is. Voor kasstroomhedges geldend vereiste dat een verwachte toekomstige transactie zeer waarschijnlijk moet zijn

## 102D

Voor de toepassing van het vereiste van alinea 88(c) dat een verwachte toekomstige transactie zeer waarschijnlijk moet zijn, moet een entiteit aannemen dat de rentebenchmark waarop de (al dan niet contractueel gespecificeerde) gehedgede kasstromen zijn gebaseerd, niet wordt gewijzigd als gevolg van de rentebenchmarkhervorming. Herclassificatie van de cumulatieve winst die of het cumulatieve verlies dat in de overige onderdelen van het totaalresultaat is opgenomen

## 102E

Voor de toepassing van het vereiste van alinea 101(c) voor het bepalen of de verwachte toekomstige transactie naar verwachting niet meer zal plaatsvinden, moet een entiteit aannemen dat de rentebenchmark waarop de (al dan niet contractueel gespecificeerde) gehedgede kasstromen zijn gebaseerd, niet wordt gewijzigd als gevolg van de rentebenchmarkhervorming. Beoordeling van de effectiviteit

## 102F

Voor de toepassing van de vereisten van de alinea’s 88(b) en TL105(a) moet een entiteit aannemen dat de rentebenchmark waarop de (al dan niet contractueel gespecificeerde) gehedgede kasstromen en/of het (al dan niet contractueel gespecificeerde) gehedgede risico zijn gebaseerd, dan wel de rentebenchmark waarop de kasstromen uit het hedge-instrument zijn gebaseerd, niet wordt gewijzigd als gevolg van de rente benchmarkhervorming.

## 102G

Voor de toepassing van het vereiste van alinea 88(e) is een entiteit niet verplicht een hedgerelatie te beëindigen omdat de feitelijke resultaten van de hedge niet aan de vereisten van alinea TL105(b) voldoen. Om alle twijfel weg te nemen, moet een entiteit de andere in alinea 88 gestelde voorwaarden, waaronder de in alinea 88(b) bedoelde prospectieve beoordeling, toepassen om te beoordelen of de hedgerelatie moet worden beëindigd. Aanwijzing van financiële posities als gehedgede positie

## 102H

Tenzij alinea 102I van toepassing is, moet een entiteit enkel bij de aanvang van de hedgerelatie voor de hedge van een niet contractueel gespecificeerde benchmarkgedeelte van een renterisico overgaan tot de toepassing van het vereiste van de alinea’s 81 en TL99F (dat het aangewezen gedeelte afzonderlijk iden tificeerbaar moet zijn).

## 102I

Wanneer een entiteit in overeenstemming met haar documentatie van de hedge een hedgerelatie vaak opnieuw vaststelt (d.w.z. beëindigt en vernieuwt) omdat zowel het hedge-instrument als de gehedgede positie vaak veranderen (m.a.w. de entiteit maakt gebruik van een dynamisch proces waarin zowel de gehedgede posities als de hedge-instrumenten die worden gebruikt om die blootstelling te beheren, niet lang hetzelfde blijven), moet de entiteit pas tot de toepassing van het vereiste van de alinea’s 81 en TL99F (dat het aangewezen gedeelte afzonderlijk identificeerbaar moet zijn) overgaan wanneer zij voor het eerst een gehedgede positie in die hedgerelatie aanwijst. Een gehedgede positie die is beoordeeld ten tijde van haar eerste aanwijzing in de hedgerelatie, ongeacht of deze aanwijzing ten tijde van de aanvang van de hedge of later heeft plaatsgevonden, wordt niet herbeoordeeld bij een eventuele latere heraanwijzing in dezelfde hedgerelatie. Einde van de toepassing

## 102J

Een entiteit moet tot de prospectieve stopzetting van de toepassing van alinea 102D op een gehedgede positie overgaan op het vroegste van de volgende twee momenten:
(a) wanneer er geen uit de rentebenchmarkhervorming voortvloeiende onzekerheid meer bestaat ten aan zien van het tijdstip en het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit de gehedgede positie voortvloeien; en
(b) wanneer de hedgerelatie waarvan de gehedgede positie deel uitmaakt, wordt beëindigd.

## 102K

Een entiteit moet tot de prospectieve stopzetting van de toepassing van alinea 102E overgaan op het vroegste van de volgende twee momenten:
(a) wanneer er geen uit de rentebenchmarkhervorming voortvloeiende onzekerheid meer bestaat ten aan zien van het tijdstip en het bedrag van de op een rentebenchmark gebaseerde toekomstige kasstromen die uit de gehedgede positie voortvloeien; en
(b) wanneer de volledige cumulatieve winst die, of het volledige cumulatieve verlies dat, met betrekking tot die beëindigde hedgerelatie in de overige onderdelen van het totaalresultaat is opgenomen, naar de winst of het verlies is overgeboekt.

## 102L

Een entiteit moet overgaan tot de prospectieve stopzetting van de toepassing van alinea 102F:
(a) op een gehedgede positie, wanneer er geen uit de rentebenchmarkhervorming voortvloeiende onze kerheid meer bestaat ten aanzien van het gehedgede risico of het tijdstip en het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit de gehedgede positie voortvloeien; en
(b) op een hedge-instrument, wanneer er geen uit de rentebenchmarkhervorming voortvloeiende onzeker heid meer bestaat ten aanzien van het tijdstip en het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit het hedge-instrument voortvloeien. Indien de hedgerelatie waarvan de gehedgede positie en het hedge-instrument deel uitmaken, vóór de in alinea 102L(a) of de in alinea 102L(b) gespecificeerde datum wordt beëindigd, moet de entiteit op de datum waarop de hedgerelatie werd beëindigd, tot de prospectieve stopzetting van de toepassing van alinea 102F op die hedgerelatie overgaan.

## 102M

Een entiteit moet de toepassing van alinea 102G op een hedgerelatie prospectief beëindigen op het vroegste van de volgende twee momenten:
(a) wanneer er geen onzekerheid ten gevolge van de rentebenchmarkhervorming meer bestaat ten aanzien van het gehedgede risico en het tijdstip en het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit de gehedgede positie en uit het hedge-instrument voortvloeien, en
(b) wanneer de hedgerelatie waarop de uitzondering wordt toegepast, wordt beëindigd.

## 102N

Bij de aanwijzing van een groep van posities als de gehedgede positie of van een combinatie van financiële instrumenten als het hedge-instrument, moet een entiteit in overeenstemming met de alinea’s 102J, 102K, 102L of 102M, al naargelang het geval, overgaan tot de prospectieve stopzetting van de toepassing van de alinea’s 102D tot en met 102G op een individuele positie of een individueel financieel instrument wanneer er geen uit de rentebenchmarkhervorming voortvloeiende onzekerheid meer bestaat ten aanzien van het gehedgede risico en/of het tijdstip en het bedrag van de op een rentebenchmark gebaseerde kasstromen die uit die positie of dat financiële instrument voortvloeien.

## 102O

Een entiteit moet de toepassing van de alinea’s 102H en 102I prospectief beëindigen op het vroegste van de volgende twee momenten:
(a) wanneer er in het niet contractueel gespecificeerde risicogedeelte veranderingen worden aangebracht die vereist zijn door de rentebenchmarkhervorming, met toepassing van alinea 102P; of
(b) wanneer de hedgerelatie waarin het niet contractueel gespecificeerde risicogedeelte is aangewezen, wordt beëindigd. Bijkomende tijdelijke uitzonderingen ten gevolge van de rentebenchmarkhervorming Hedge accounting

## 102P

Wanneer de vereisten in de alinea’s 102D tot en met 102I niet langer worden toegepast op een hedge relatie (zie de alinea’s 102J tot en met 102O), moet een entiteit de formele aanwijzing van die hedgerelatie zoals eerder gedocumenteerd wijzigen om rekening te houden met de veranderingen die vereist zijn ten gevolge van de rentebenchmarkhervorming, d.w.z. de veranderingen moeten consistent zijn met de ver eisten in de alinea’s 5.4.6 tot en met 5.4.8 van IFRS 9. In dit verband moet de aanwijzing van de hedge alleen worden gewijzigd om een of meer van deze veranderingen aan te brengen:

(a) de (al dan niet contractueel gespecificeerde) alternatieve referentierente aanmerken als een gehedged risico;
(b) de beschrijving wijzigen van de gehedgede positie, waaronder de beschrijving van het aangewezen gedeelte van de te hedgen kasstromen of reële waarde;
(c) de beschrijving van het hedge-instrument wijzigen; of
(d) de beschrijving wijzigen van de wijze waarop de entiteit de hedge-effectiviteit zal beoordelen.

## 102Q

Een entiteit moet ook het vereiste in alinea 102P(c), toepassen indien aan deze drie voorwaarden is voldaan:
(a) de entiteit zorgt voor een verandering die vereist is door de rentebenchmarkhervorming en maakt daarbij gebruik van een andere aanpak dan een verandering van de grondslag voor de vaststelling van de contractuele kasstromen van het hedge-instrument (zoals beschreven in alinea 5.4.6 van IFRS 9);
(b) het oorspronkelijke hedge-instrument wordt niet langer opgenomen; en
(c) de gekozen aanpak is economisch gelijkwaardig met een verandering van de grondslag voor de vast stelling van de contractuele kasstromen van het oorspronkelijke hedge-instrument (zoals beschreven in de alinea’s 5.4.7 en 5.4.8 van IFRS 9).

## 102R

Het is mogelijk dat de vereisten van de alinea’s 102D tot en met 102I op een verschillend tijdstip niet langer van toepassing zijn. Bij toepassing van alinea 102P is het dus mogelijk dat een entiteit ertoe verplicht wordt de formele aanwijzing van haar hedgerelaties op verschillende tijdstippen te wijzigen of dat zij de formele aanwijzing van een hedgerelatie meer dan eens moet wijzigen. Alleen wanneer een dergelijke wijziging in de aanwijzing van de hedge wordt aangebracht, moet een entiteit, voor zover van toepassing, de alinea’s 102V tot en met 102Z2 toepassen. Een entiteit moet ook alinea 89 (voor een reële- waardehedge) of alinea 96 (voor een kasstroomhedge) toepassen om rekening te houden met veranderin gen in de reële waarde van de gehedgede positie of het hedge-instrument.

## 102S

Een entiteit moet een hedgerelatie zoals vereist in alinea 102P wijzigen tegen het einde van de verslagpe riode waarin een door de rentebenchmarkhervorming vereiste wijziging wordt aangebracht in het gehed gede risico, de gehedgede positie of het hedge-instrument. Om twijfel te voorkomen betekent een derge lijke wijziging in de formele aanwijzing van een hedgerelatie noch de beëindiging van de hedgerelatie noch de aanwijzing van een nieuwe hedgerelatie.

## 102T

Indien naast de veranderingen die door de rentebenchmarkhervorming zijn vereist, veranderingen worden aangebracht aan het financieel actief of de financiële verplichting die in een hedgerelatie (zoals beschreven in de alinea’s 5.4.6 tot en met 5.4.8 van IFRS 9) is aangewezen, of aan de aanwijzing van de hedgerelatie (zoals vereist door alinea 102P), moet een entiteit eerst de toepasselijke vereisten van deze standaard toepassen om te bepalen of deze bijkomende veranderingen aanleiding geven tot de beëindiging van hedge accounting. Indien de bijkomende veranderingen geen aanleiding geven tot de beëindiging van hedge accounting, moet een entiteit de formele aanwijzing van de in alinea 102P omschreven hedgerelatie wijzigen.

## 102U

De alinea’s 102V tot en met 102Z3 voorzien alleen in uitzonderingen op de vereisten die in de genoemde alinea’s zijn beschreven. Een entiteit moet alle andere verplichtingen inzake hedge accounting in deze standaard, met inbegrip van de criteria in alinea 88 waaraan moet worden voldaan om in aanmerking te komen, toepassen op de hedgerelaties waarop de rentebenchmarkhervorming rechtstreeks van invloed is.

Administratieve verwerking van in aanmerking komende hedgerelaties R e t r o a c t i e v e b e o o r d e l i n g v a n d e e f f e c t i v i t e i t

## 102V

Voor de beoordeling van de retroactieve effectiviteit van een hedgerelatie op cumulatieve basis met toepassing van alinea 88(e) en alleen met dit doel kan een entiteit ervoor kiezen de cumulatieve ver anderingen in de reële waarde van de gehedgede positie en het hedge-instrument opnieuw op nul te stellen wanneer, zoals vereist bij alinea 102M, de toepassing van alinea 102G wordt beëindigd. Deze keuze wordt afzonderlijk gemaakt voor elke hedgerelatie (d.w.z. op basis van een individuele hedgerelatie). K a s s t r o o m h e d g e s

## 102W

Voor de toepassing van alinea 97 wordt, op het tijdstip dat een entiteit de beschrijving van een gehedgede positie als vereist in alinea 102P(b) wijzigt, de cumulatieve winst of het cumulatieve verlies in de overige onderdelen van het totaalresultaat is opgenomen, geacht te zijn gebaseerd op de alternatieve referentierente waarop de gehedgede toekomstige kasstromen worden bepaald.

## 102X

Voor een beëindigde hedgerelatie wordt, wanneer de rentebenchmark waarop de gehedgede toekomstige kasstromen waren gebaseerd, wordt veranderd zoals vereist door de rentebenchmarkhervorming, het in de overige onderdelen van het totaalresultaat geaccumuleerde bedrag voor die hedgerelatie, voor de toepassing van alinea 101(c) voor het bepalen of de gehedgede toekomstige kasstromen naar verwachting zullen plaatsvinden, geacht te zijn gebaseerd op de alternatieve referentierente waarop de gehedgede toekomstige kasstromen zullen zijn gebaseerd. Groepen posities

## 102Y

Wanneer een entiteit alinea 102P toepast op groepen posities die als gehedgede posities in een reëlewaar de- of een kasstroomhedge zijn aangewezen, moet zij de gehedgede posities toewijzen aan subgroepen gebaseerd op de te hedgen rentebenchmark en de rentebenchmark aanwijzen als het gehedgede risico voor elke subgroep. In een hedgerelatie waarbij een groep posities wordt gehedged voor veranderingen in een onder de rentebenchmarkhervorming vallende rentebenchmark, kunnen bijvoorbeeld de gehedgede kas stromen of reële waarde van bepaalde posities in de groep worden veranderd om te refereren aan een alternatieve referentierente voordat andere posities in de groep worden veranderd. In dit voorbeeld zou de entiteit bij de toepassing van alinea 102P de alternatieve referentierente aanwijzen als het gehedgede risico voor die relevante subgroep van gehedgede posities. De entiteit zou de bestaande rentebenchmark blijven aanwijzen als het gehedgede risico voor de andere subgroep van gehedgede posities totdat de gehedgede kasstromen of reële waarde van die posities worden veranderd om te refereren aan de alternatieve refe rentierente, of totdat de posities vervallen en worden vervangen door gehedgede posities die refereren aan de alternatieve referentierente.

## 102Z

Een entiteit moet afzonderlijk onderzoeken of elke subgroep voldoet aan de vereisten in de alinea’s 78 en 83 om in aanmerking te komen als gehedgede positie. Indien een subgroep niet aan de vereisten van de alinea’s 78 en 83 voldoet, moet de entiteit hedge accounting prospectief beëindigen voor de hedgerelatie in haar geheel. Een entiteit moet ook de vereisten in alinea 89 of 96 toepassen om rekening te houden met de ineffectiviteit met betrekking tot de hedgerelatie in haar geheel. Aanwijzing van financiële posities als gehedgede positie

## 102Z1

Een alternatieve referentierente aangewezen als een niet contractueel gespecificeerd risicogedeelte dat op de datum waarop zij wordt aangewezen niet afzonderlijk identificeerbaar is (zie alinea 81 en TL99F), wordt geacht op die datum aan dat vereiste te hebben voldaan indien de entiteit redelijkerwijs verwacht dat de alternatieve referentierente binnen 24 maanden afzonderlijk identificeerbaar zal zijn. De periode van 24 maanden geldt voor elke alternatieve referentierente afzonderlijk en gaat in op de datum waarop de entiteit de alternatieve referentierente voor de eerste maal aanwijst als een niet contractueel gespecificeerde risico component (d.w.z. dat de periode van 24 maanden op elke rente afzonderlijk (“rate-by-rate”) van toepas sing is).

## 102Z2

Indien een entiteit vervolgens redelijkerwijs verwacht dat de alternatieve referentierente niet afzonderlijk identificeerbaar zal zijn binnen 24 maanden na de datum waarop zij deze als een niet contractueel gespecificeerd risicogedeelte heeft aangewezen, moet zij het vereiste in alinea 102Z1 niet langer op die alternatieve referentierente toepassen en vanaf de datum van die herbeoordeling hedge accounting pro spectief beëindigen voor alle hedgerelaties waarbij de alternatieve referentierente als een niet contractueel gespecificeerd risicogedeelte was aangewezen.

## 102Z3

Naast die in alinea 102P vermelde hedgerelaties moet een entiteit de vereisten van de alinea’s 102Z1 en 102Z2 toepassen op nieuwe hedgerelaties waarin een alternatieve referentierente als een niet-contractueel gespecificeerd risicogedeelte wordt aangewezen (zie de alinea’s 81 en TL99F) wanneer dat risicogedeelte vanwege de rentebenchmarkhervorming niet afzonderlijk identificeerbaar is op de datum waarop dit wordt aangewezen.

## Ingangsdatum En Overgang

103 Entiteiten moeten deze standaard (met inbegrip van de wijzigingen die in maart 2004 zijn uitgegeven) toepassen op jaarperioden die op of na 1 januari 2005 aanvangen. Eerdere toepassing is toegestaan. Een entiteit mag deze standaard (met inbegrip van de wijzigingen die in maart 2004 zijn uitgegeven) niet toepassen op jaarperioden die vóór 1 januari 2005 aanvangen, tenzij de entiteit tevens IAS 32 (uitgegeven in december 2003) toepast. Als een entiteit deze standaard toepast op een periode die vóór 1 januari 2005 aanvangt, moet zij dit feit vermelden.

## 103A

[Verwijderd]

## 103B

[Verwijderd]

## 103C

IAS 1 (herziene versie van 2007) wijzigde de in de IFRSs gebruikte terminologie. Voorts werden de alinea’s 95(a), 97, 98, 100, 102, 108 en TL99B gewijzigd. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2009 aanvangen. Als een entiteit IAS 1 (herziene versie van 2007) toepast op een periode die vóór 1 januari 2009 aanvangt, moeten ook deze wijzigingen op die periode worden toegepast.

## 103D

[Verwijderd]

## 103E

IFRS 27 (als gewijzigd in 2008) heeft alinea 102 gewijzigd. Entiteiten moeten die wijziging toepassen op jaarperioden die op of na 1 juli 2009 aanvangen. Als een entiteit IAS 27 (herziene versie van 2008) op een eerdere periode toepast, moet zij ook deze wijziging op die eerdere periode toepassen.

## 103F

[Verwijderd]

## 103G

Entiteiten moeten de alinea’s TL99BA, TL99E, TL99F, TL110A en TL110B retroactief toepassen op jaar perioden die op of na 1 juli 2009 aanvangen, in overeenstemming met IAS 8 Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten. Eerdere toepassing is toegestaan. Als een entiteit Gehedgede items die in aanmerking komen (wijziging in IAS 39) toepast op verslagperioden die vóór 1 juli 2009 aanvangen, moet zij dit feit vermelden. 103H–103J [Verwijderd]

## 103K

De alinea’s 2(g), 97 en 100 zijn gewijzigd door de in april 2009 uitgegeven Verbeteringen in IFRSs. Entiteiten moeten de wijzigingen in deze alinea’s prospectief op alle niet-afgelopen contracten toepassen op jaarperioden die op of na 1 januari 2010 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit de wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden. 103L–103P [Verwijderd]

## 103Q

IFRS 13, uitgegeven in mei 2011, wijzigde de alinea’s 9, 13, 28, 47, 88, TL46, TL52, TL64, TL76, TL76A, TL80, TL81 en TL96, voegde alinea 43A toe en verwijderde de alinea’s 48-49, TL69-TL75, TL77-TL79 en TL82. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 13 toepast.

## 103R

De alinea’s 2 en 80 zijn gewijzigd door Beleggingsentiteiten (wijzigingen in IFRS 10, IFRS 12 en IAS 27), uitgegeven in oktober 2012. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2014 aanvangen. Eerdere toepassing van Beleggingsentiteiten is toegestaan. Indien een entiteit deze wijzigingen eerder toepast, moet zij tegelijkertijd ook alle in Beleggingsentiteiten vervatte wijzigingen toe passen.

## 103S

[Verwijderd]

## 103T

IFRS 15 Opbrengsten van contracten met klanten, uitgegeven in mei 2014, heeft de alinea’s 2, 9, 43, 47, 55, TL2, TL4 en TL48 gewijzigd en de alinea’s 2A, 44A, 55A en TL8A-TL8C toegevoegd. Een entiteit moet deze wijzigingen toepassen wanneer zij IFRS 15 toepast.

## 103U

De alinea’s 2, 8, 9, 71, 88-90, 96, TL95, TL114, TL118 en de kopjes boven TL133 zijn gewijzigd en de alinea’s 1, 4-7, 10-70, 103B, 103D, 103F, 103H-103J, 103L-103P, 103S, 105-107A, 108E-108F, TL1- TL93 en TL96 zijn verwijderd door IFRS 9, als uitgegeven in juli 2014. Een entiteit moet die wijzigingen toepassen wanneer zij IFRS 9 toepast.

## 103 V

[Deze alinea was toegevoegd voor een entiteit die IFRS 9 niet had toegepast.] 104 Deze standaard moet retroactief worden toegepast, behoudens het bepaalde in alinea 108. Het beginsaldo van ingehouden winsten voor de eerst gepresenteerde periode en alle andere vergelijkende bedragen moeten worden aangepast alsof deze standaard altijd was gebruikt, tenzij aanpassing van de informatie praktisch onhaalbaar zou zijn. Indien aanpassing praktisch onhaalbaar is, moet de entiteit dit feit ver melden, alsmede de mate waarin de informatie is aangepast.

## 105–107A

[Verwijderd] 108 Een entiteit mag de boekwaarde van niet-financiële activa en niet-financiële verplichtingen niet aanpassen om winsten en verliezen met betrekking tot kasstroomhedges uit te sluiten die deel uitmaakten van de boekwaarde vóór het begin van het boekjaar waarin de standaard voor het eerst wordt toegepast. Aan het begin van de verslagperiode waarin deze standaard voor het eerst wordt toegepast, moet elk bedrag dat buiten de winst of het verlies is opgenomen (hetzij in overige onderdelen van het totaalresultaat, hetzij direct in het eigen vermogen) in verband met een hedge van een vaststaande toezegging die op grond van deze standaard als een reële-waardehedge wordt verwerkt, als een actief of een verplichting worden geherclassificeerd, behalve een hedge van valutarisico die de entiteit als een kasstroomhedge blijft behan delen.

## 108A

Entiteiten moeten de laatste zin van alinea 80 en de alinea’s TL99A en TL99B toepassen op jaarperioden die op of na 1 januari 2006 aanvangen. Eerdere toepassing wordt aanbevolen. Indien een entiteit een externe verwachte toekomstige transactie die
(a) luidt in de functionele valuta van de entiteit die de transactie sluit;
(b) resulteert in een risicopositie die de geconsolideerde winst of het geconsolideerde verlies beïnvloedt (d. w.z. een risicopositie die luidt in een valuta die verschilt van de presentatievaluta van de groep); en
(c) voor de toepassing van hedge accounting in aanmerking zou zijn gekomen indien de transactie niet in de functionele valuta had geluid van de entiteit waardoor deze is gesloten, als gehedgede positie aanwijst, dan mag zij in de geconsolideerde jaarrekening hedge accounting toepassen in de periode(n) vóór de datum van toepassing van de laatste zin van alinea 80 en de alinea’s TL99A en TL99B.

## 108B

Een entiteit hoeft alinea TL99B niet toe te passen op vergelijkende informatie die betrekking heeft op perioden vóór de datum van toepassing van de laatste zin van alinea 80 en alinea TL99A.

## 108C

De alinea’s 73 en TL8 zijn gewijzigd door Verbeteringen in IFRSs, uitgegeven in mei 2008. Alinea 80 is gewijzigd door de in april 2009 uitgegeven Verbeteringen in IFRSs. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2009 aanvangen. Eerdere toepassing van alle wijzigingen is toegestaan. Als een entiteit de wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden.

## 108D

De alinea’s 91 en 101 zijn gewijzigd en alinea TL113A is toegevoegd door Novatie van derivaten en voort zetting van hedge accounting (wijzigingen in IAS 39), uitgegeven in juni 2013. Entiteiten moeten deze alinea’s toepassen op jaarperioden die op of na 1 januari 2014 aanvangen. Entiteiten moeten deze wijzi gingen retroactief toepassen in overeenstemming met IAS 8 Grondslagen voor financiële verslaggeving, schat tingswijzigingen en fouten. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden. 108E–108F [Verwijderd]

## 108G

De alinea’s 102A tot en met 102N zijn toegevoegd door Rentebenchmarkhervorming (wijzigingen in IFRS 9, IAS 39 en IFRS 7), uitgegeven in september 2019. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2020 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden. Een entiteit moet deze wijzigingen retroactief toepassen op de hedgerelaties die bestonden aan het begin van de verslagperiode waarin een entiteit deze wijzigingen voor het eerst toepast of die daarna zijn aangewezen, en op de in de overige onderdelen van het totaalresultaat opgenomen winst die, of het in de overige onderdelen van het totaalresultaat opgenomen verlies dat, bestond aan het begin van de verslagperiode waarin een entiteit deze wijzigingen voor het eerst toepast.

## 108H

De alinea’s 102O-102Z3 en 108I-108K zijn toegevoegd en alinea 102M is gewijzigd door Rentebenchmark hervorming – Fase 2 waarbij IFRS 9, IAS 39, IFRS 7, IFRS 4 en IFRS 16 zijn gewijzigd, uitgegeven in augustus 2020. Entiteiten moeten deze wijzigingen toepassen op jaarperioden die op of na 1 januari 2021 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen op een eerdere periode toepast, moet zij dit feit vermelden. Een entiteit moet deze wijzigingen retroactief toepassen in overeen stemming met IAS 8, tenzij anders vermeld in de alinea’s 108I tot en met 108K.

## 108I

Een entiteit moet een nieuwe hedgerelatie (bijvoorbeeld zoals omschreven in alinea 102Z3) alleen pro spectief toepassen (d.w.z. het is een entiteit verboden een nieuwe hedge-accountingrelatie aan te wijzen in voorgaande perioden). Een entiteit moet een beëindigde hedgerelatie echter opnieuw invoeren als en alleen als, aan de volgende voorwaarden is voldaan:
(a) de entiteit had die hedgerelatie alleen beëindigd wegens veranderingen die vereist waren door de rentebenchmarkhervorming, en de entiteit zou niet verplicht zijn geweest die hedgerelatie te beëindigen indien deze veranderingen op dat moment waren toegepast; en
(b) bij de aanvang van de verslagperiode waarin een entiteit deze wijzigingen voor het eerst toepast (datum van eerste toepassing van deze wijzigingen), voldoet die beëindigde hedgerelatie aan de criteria om voor hedge accounting in aanmerking te komen (rekening houdend met deze wijzigingen).

## 108J

Indien een entiteit bij de toepassing van alinea 108I een beëindigde hedgerelatie opnieuw invoert, moet zij alle verwijzingen in de alinea’s 102Z1 en 102Z2 naar de datum waarop de alternatieve referentierente voor het eerst als een niet-contractueel gespecificeerde risicocomponent wordt aangewezen, lezen als verwijzingen naar de datum van eerste toepassing van deze wijzigingen (d.w.z. de periode van 24 maanden voor die alternatieve referentierente aangewezen als een niet-contractueel gespecificeerde risicocomponent gaat in vanaf de datum van eerste toepassing van deze wijzigingen).

## 108K

Een entiteit is niet verplicht om voorgaande perioden aan te passen om rekening te houden met de toepassing van deze wijzigingen. De entiteit mag voorgaande perioden alleen aanpassen als en alleen als dit zonder gebruik van kennis achteraf mogelijk is. Indien een entiteit voorgaande perioden niet aanpast, moet zij een eventueel verschil tussen de vorige boekwaarde en de boekwaarde aan het begin van de jaarlijkse verslagperiode waarin de datum van eerste toepassing van deze wijzigingen valt, opnemen in het beginsaldo van ingehouden winsten (of in een andere eigenvermogenscomponent, al naargelang van het geval) voor de jaarlijkse verslagperiode waarin de datum van eerste toepassing van deze wijzigingen valt.

## Intrekking Van Andere Uitspraken

109 Deze standaard vervangt IAS 39 Financiële instrumenten: opname en waardering, herzien in oktober 2000. 110 Deze standaard en de bijbehorende implementatieleidraad vervangen de implementatieleidraad die is uitgegeven door het “IAS 39 Implementation Guidance Committee”, dat werd opgericht door de voor malige IASC.

Bijlage A Toepassingsleidraad Deze bijlage is een integraal onderdeel van de standaard.

## Tl1–Tl93

[Verwijderd] HEDGING (alinea’s 71 tot en met 102) Hedge-instrumenten (alinea’s 72 tot en met 77) Instrumenten die in aanmerking komen (alinea 72 en 73)

## Tl94

Het mogelijke verlies op een door een entiteit geschreven optie kan aanzienlijk groter zijn dan de mogelijke waardestijging van een daarmee samenhangende gehedgede positie. Een geschreven optie is met andere woorden niet effectief om het winst- of verliesrisico van een gehedgede balanspositie te reduceren. Een geschreven optie komt derhalve niet als een hedge-instrument in aanmerking, tenzij de optie wordt aange merkt als hedge van een gekochte optie, met inbegrip van een optie die in een ander financieel instrument is besloten (bijvoorbeeld een geschreven optie die wordt gebruikt om opeisbare schulden te hedgen). Daar entegen is de potentiële winst bij een gekochte optie gelijk aan of hoger dan het verlies; met een gekochte optie kan dus eventueel de winst of het verlies voortvloeiend uit veranderingen in de reële waarde of kas stromen worden gereduceerd. Een gekochte optie kan dan ook in aanmerking komen als hedge-instrument.

## Tl95

Een financieel actief dat tegen geamortiseerde kostprijs wordt gewaardeerd, kan als hedge-instrument worden aangewezen bij een hedge van valutarisico.

## Tl96

[Verwijderd]

## Tl97

Eigenvermogensinstrumenten van een entiteit zijn geen financiële activa of financiële verplichtingen van de entiteit en kunnen derhalve niet als hedge-instrument worden aangewezen. Gehedgede posities (alinea’s 78 tot en met 84) In aanmerking komende posities (alinea’s 78 tot en met 80)

## Tl98

Een vaststaande toezegging voor de overname van een bedrijf in een bedrijfscombinatie kan geen gehedgede positie zijn, behalve wat het valutarisico betreft, omdat de andere te hedgen risico’s niet specifiek kunnen worden vastgesteld en gemeten. Deze andere risico’s zijn algemene bedrijfsrisico’s.

## Tl99

Een investering verwerkt volgens de vermogensmutatiemethodemethode kan geen gehedgede positie zijn bij een reële-waardehedge, omdat bij de vermogensmutatiemethodemethode het aandeel van de belegger in de winst of het verlies van de geassocieerde deelneming in winst of verlies wordt opgenomen, en niet de veranderingen in de reële waarde van de investering. Om dezelfde reden kan een investering in een geconsoli deerde dochteronderneming geen gehedgede positie zijn bij een reële-waardehedge omdat bij consolidatie het aandeel van de moedermaatschappij in de winst of het verlies van de dochteronderneming in winst of verlies wordt opgenomen, en niet de veranderingen in de reële waarde van de investering. Bij een hedge van een netto-investering in een buitenlandse activiteit ligt de situatie anders omdat het een hedge betreft van de blootstelling aan valutarisico en niet een reële-waardehedge van de waardeverandering van de investering.

## Tl99A

Alinea 80 bepaalt dat het valutarisico van een zeer waarschijnlijke verwachte toekomstige intragroepstrans actie in de geconsolideerde jaarrekening als gehedgede positie in aanmerking kan komen, mits de transactie in een valuta luidt die verschilt van de functionele valuta van de entiteit die de transactie sluit, en het valutarisico de geconsolideerde winst of het geconsolideerde verlies beïnvloedt. In dit verband kan een entiteit een moedermaatschappij, een dochteronderneming, een geassocieerde deelneming, een joint venture of een filiaal zijn. Indien het valutarisico van een verwachte toekomstige intragroepstransactie de geconsolideerde winst of het geconsolideerde verlies niet beïnvloedt, kan de intragroepstransactie niet als gehedgede positie in aan merking komen. Dit is gewoonlijk het geval voor royaltybetalingen, rentebetalingen en managementvergoe dingen tussen leden van dezelfde groep, tenzij deze betalingen en vergoedingen met een externe transactie verband houden. Wanneer het valutarisico van een verwachte toekomstige intragroepstransactie de geconsoli deerde winst of het geconsolideerde verlies echter wel beïnvloedt, kan de intragroepstransactie als gehedgede positie in aanmerking komen. Een voorbeeld hiervan is een verwachte toekomstige aankoop of verkoop van voorraden tussen leden van dezelfde groep indien de voorraden worden doorverkocht aan een partij buiten de groep. Ook een verwachte intragroepsverkoop van fabrieksinstallaties door de groepsentiteit die deze heeft vervaardigd, aan een groepsentiteit die de fabrieksinstallaties bij haar bedrijfsactiviteiten zal gebruiken, kan de geconsolideerde winst of het geconsolideerde verlies beïnvloeden. Dit kan bijvoorbeeld gebeuren omdat de fabrieksinstallaties door de aankopende entiteit zullen worden afgeschreven en het bedrag dat aanvankelijk voor de fabrieksinstallaties is opgenomen, kan veranderen indien de verwachte toekomstige intragroepstrans actie luidt in een valuta die verschilt van de functionele valuta van de aankopende entiteit.

## Tl99B

Komt een hedge van een verwachte toekomstige intragroepstransactie in aanmerking voor de toepassing van hedge accounting, dan moet de eventuele winst die of het eventuele verlies dat overeenkomstig alinea 95(a) in de overige onderdelen van het totaalresultaat is opgenomen, van het eigen vermogen naar de winst of het verlies worden overgeboekt als een herclassificatieaanpassing in dezelfde periode of perioden waarin het wisselkoersrisico van de gehedgede transactie de geconsolideerde winst of het geconsolideerde verlies beïn vloedt. TL99BA Een entiteit kan alle veranderingen in de kasstromen of reële waarde van een gehedgede positie in een hedge- relatie aanmerken. Een entiteit kan echter ook alleen veranderingen in de kasstromen of reële waarde van een gehedgede positie boven of onder een gespecificeerde prijs of andere variabele (een eenzijdig risico) aan merken. De intrinsieke waarde van een hedge-instrument in de vorm van een gekochte optie (uitgaande van de veronderstelling dat de belangrijkste voorwaarden ervan overeenstemmen met die van het aangewezen risico), maar niet zijn tijdswaarde, weerspiegelt een eenzijdig risico in een gehedgede positie. Een entiteit kan bijvoorbeeld de variabiliteit van toekomstige kasstroomresultaten die voortvloeien uit een prijsverhoging van een verwachte toekomstige commodityaankoop aanwijzen. In dat geval worden alleen kasstroomverliezen die voortvloeien uit een verhoging van de prijs boven het gespecificeerde niveau aangemerkt. Het gehedgede risico omvat niet de tijdswaarde van een gekochte optie, omdat de tijdswaarde geen component is van de verwachte toekomstige transactie die de winst of het verlies beïnvloedt (alinea 86 b)). Aanwijzing van financiële posities als gehedgede positie (alinea’s 81 en 81A)

## Tl99C

[…] De entiteit kan alle kasstromen van het gehele financieel actief of de gehele financiële verplichting aanwijzen als gehedgede positie, en deze uitsluitend tegen één bepaald risico hedgen (bijvoorbeeld uitsluitend in verband met veranderingen die zijn toe te schrijven aan wijzigingen in de LIBOR). Een entiteit kan bijvoorbeeld in het geval van een financiële verplichting waarvan de effectieve rente 100 basispunten onder de LIBOR ligt, de gehele verplichting (d.w.z. hoofdsom plus rente tegen de LIBOR minus 100 basispunten) aanwijzen als gehedgede positie en de verandering in de reële waarde of kasstromen van die gehele ver plichting hedgen, die is toe te schrijven aan wijzigingen in de LIBOR. De entiteit kan, om de effectiviteit van de hedge te verbeteren, ook kiezen voor een andere hedgeratio dan één op één, zoals beschreven in alinea TL100.

## Tl99D

Bovendien geldt dat, indien een vastrentend financieel instrument enige tijd na creatie wordt gehedged en de rente intussen is veranderd, de entiteit een deel kan aanwijzen gelijk aan een referentierente […]. Neem als voorbeeld een entiteit die een vastrentend financieel actief creëert van VE 100, met een effectieve rentevoet van zes procent terwijl de LIBOR vier procent bedraagt. De entiteit begint dat actief enige tijd later te hedgen, namelijk op het moment dat de LIBOR tot 8 procent is gestegen en de reële waarde van het actief tot VE 90 is gedaald. De entiteit berekent dat indien zij het actief had gekocht op het moment van de eerste aanwijzing van het actief als gehedgede positie, voor de reële waarde van dat moment (VE 90), het effectieve rendement 9,5 procent zou zijn geweest. […]. De entiteit kan een LIBOR-deel van 8 procent aanwijzen dat ten dele bestaat uit de contractuele rentekasstromen en ten dele uit het verschil tussen de actuele reële waarde (d.w.z. VE 90) en het aan het eind van de looptijd af te lossen bedrag (d.w.z. VE 100).

## Tl99E

Alinea 81 staat toe dat een entiteit iets anders dan de totale verandering in de reële waarde of variabiliteit van de kasstromen van een financieel instrument aanmerkt. Bijvoorbeeld:
(a) alle kasstromen van een financieel instrument mogen worden aangemerkt voor veranderingen in de kasstromen of reële waarde die toerekenbaar zijn aan bepaalde (maar niet alle) risico’s; of
(b) bepaalde (maar niet alle) kasstromen van een financieel instrument mogen worden aangemerkt voor veranderingen in de kasstromen of reële waarde die toerekenbaar zijn aan alle of slechts enkele risico’s (d.w.z. een “deel” van de kasstromen van het financieel instrument mag worden aangemerkt voor ver anderingen die toerekenbaar zijn aan alle of slechts enkele risico’s).

## Tl99F

Om in aanmerking te komen voor hedge accounting moeten de aangewezen risico’s en aangemerkte delen afzonderlijk identificeerbare componenten van het financieel instrument zijn, en moeten veranderingen in de kasstromen of reële waarde van het gehele financieel instrument die voortvloeien uit veranderingen in de aangewezen risico’s en aangemerkte delen betrouwbaar kunnen worden bepaald. Bijvoorbeeld:
(a) voor een vastrentend financieel instrument gehedged tegen veranderingen in de reële waarde die toere kenbaar zijn aan veranderingen in een risicovrije rentevoet of referentierente, wordt er normaliter van uitgegaan dat de risicovrije rentevoet of referentierente een afzonderlijk identificeerbare component van het financieel instrument is en betrouwbaar kan worden bepaald;
(b) inflatie is niet afzonderlijk identificeerbaar, kan niet betrouwbaar worden bepaald en kan niet worden aangemerkt als een risico of een deel van een financieel instrument, tenzij aan de vereisten in c) is voldaan;

(c) een contractueel gespecificeerd inflatiedeel van de kasstromen van een opgenomen aan de inflatie gekop pelde obligatie (in de veronderstelling dat er geen verplichting is om een in een contract besloten derivaat afzonderlijk te verwerken) is afzonderlijk identificeerbaar en kan betrouwbaar worden bepaald mits andere kasstromen van het instrument niet door het inflatiedeel worden beïnvloed. Aanwijzing van niet-financiële posities als gehedgede positie (alinea 82)

## Tl100

Veranderingen in de prijs van een bestanddeel of component van een niet-financieel actief of niet-financiële verplichting hebben over het algemeen geen voorspelbaar, afzonderlijk meetbaar effect op de prijs van de post dat vergelijkbaar is met het effect van bijvoorbeeld een verandering in de marktrente op de prijs van een obligatie. Een niet-financieel actief of een niet financiële verplichting vormt derhalve uitsluitend als geheel een gehedgede positie, of vormt een gehedgede positie in geval van valutarisico. Indien er sprake is van een verschil tussen de voorwaarden van het hedge-instrument en de gehedgede positie (zoals bij een hedge van de verwachte aankoop van Braziliaanse koffie door middel van een termijncontract voor de aankoop van Colombiaanse koffie onder overigens vergelijkbare voorwaarden) kan de hedgerelatie niettemin als een hed gerelatie worden aangemerkt, mits aan alle voorwaarden in alinea 88 wordt voldaan, met inbegrip van de verwachting dat de hedge zeer effectief zal zijn. In dit verband kan het bedrag van het hedge-instrument hoger of lager zijn dan dat van de gehedgede positie, indien hierdoor de effectiviteit van de hedgerelatie wordt bevorderd. Er zou bijvoorbeeld een regressieanalyse uitgevoerd kunnen worden om een statistische relatie vast te stellen tussen de gehedgede positie (bv. een transactie in Braziliaanse koffie) en het hedge-instrument (bv. een transactie in Colombiaanse koffie). In geval van een gegronde statistische relatie tussen beide variabelen (d. w.z. de prijzen per eenheid Braziliaanse en Colombiaanse koffie) kan de helling van de regressielijn worden gebruikt om de hedgeratio vast te stellen waarmee de maximale verwachte effectiviteit wordt bewerkstelligd. Indien bijvoorbeeld de helling van de regressielijn 1,02 bedraagt, wordt met een hedgeratio op basis van factor 0,98 van de hoeveelheid van de gehedgede positie tegenover factor 1,00 van de hoeveelheid van het hedge- instrument de maximale verwachte effectiviteit bereikt. De hedgerelatie kan echter leiden tot ineffectiviteit die gedurende de looptijd van de hedgerelatie in winst of verlies wordt opgenomen. Aanwijzing van groepen posities als gehedgede positie (alinea’s 83 en 84)

## Tl101

Een hedge van een netto totaalpositie (bv. het saldo van alle vastrentende activa en vastrentende verplichtingen met een vergelijkbare looptijd), in plaats van een specifieke gehedgede positie, voldoet niet aan de voor waarden voor hedge accounting. Vrijwel hetzelfde effect dat hedge accounting bij dit type hedgerelatie heeft op de winst of het verlies kan echter worden bereikt door een deel van de onderliggende posities aan te wijzen als de gehedgede positie. Bijvoorbeeld als een bank VE 100 aan activa en VE 90 aan verplichtingen heeft met een vergelijkbaar risico en vergelijkbare looptijd en de nettopositie van VE 10 hedget, kan de bank VE 10 van de activa aanwijzen als gehedgede positie. Van deze aanwijzing kan worden gebruikgemaakt indien bedoelde activa en verplichtingen vastrentende instrumenten zijn; in dat geval is er sprake van een reële- waardehedge. Indien beide instrumenten variabel rentend zijn, is er sprake van een kasstroomhedge. Zo kan een entiteit die een vaststaande toezegging heeft voor de aankoop in vreemde valuta van VE 100 en een vaststaande toezegging voor de verkoop in die vreemde valuta van VE 90, het saldo van VE 10 hedgen door een derivaat te kopen en dit aan te wijzen als hedge-instrument dat is verbonden aan VE 10 van de vast staande kooptoezegging van VE 100. Hedge accounting (alinea’s 85 tot en met 102)

## Tl102

Een voorbeeld van reële-waardehedge is een hedge van het risico dat de entiteit loopt ten aanzien van veranderingen in de reële waarde van een vastrentend schuldbewijs als gevolg van rentevoetwijzigingen. Een dergelijke hedge kan worden aangegaan door de emittent of door de houder van het schuldbewijs.

## Tl103

Een voorbeeld van een kasstroomhedge is het gebruik van een swap om een variabel rentende schuld te wijzigen in een vastrentende schuld (d.w.z. een hedge van een toekomstige transactie waarbij de toekomstige kasstromen die worden gehedged de toekomstige rentebetalingen zijn).

## Tl104

Een hedge van een vaststaande toezegging (bv. een hedge van de verandering van de brandstofprijs in relatie tot een niet-opgenomen contractuele verplichting door een elektriciteitsbedrijf om brandstof tegen een vaste prijs te kopen) is een hedge van het risico van een verandering in de reële waarde. Een dergelijke hedge is bijgevolg een reële-waardehedge. Volgens alinea 87 zou een hedge van het valutarisico van een vaststaande toezegging als alternatief administratief als een kasstroomhedge kunnen worden verwerkt.

Beoordeling van de hedge-effectiviteit

## Tl105

Een hedge wordt uitsluitend als zeer effectief aangemerkt indien beide onderstaande voorwaarden zijn vervuld.
(a) Bij het aangaan van de hedge en in daaropvolgende perioden wordt verwacht dat de hedge zeer effectief is wat betreft het compenseren van aan het gehedgede risico toe te schrijven veranderingen in de reële waarde of kasstromen gedurende de periode waarvoor de hedge wordt aangemerkt. Een dergelijke ver wachting kan op verschillende manieren worden aangetoond, onder meer door middel van een vergelij king van de aan het gehedgede risico toe te schrijven historische veranderingen in de reële waarde of kasstromen van de gehedgede positie met de historische veranderingen in de reële waarde of de kas stromen van het hedge-instrument, of door een hoge statistische correlatie aan te tonen tussen de reële waarde of de kasstromen van de gehedgede positie en die van het hedge-instrument. De entiteit kan, om de effectiviteit van de hedge te verbeteren, kiezen voor een andere hedgeratio dan één op één, zoals beschreven in alinea TL100.
(b) De werkelijke effectiviteit van de hedge valt binnen een bereik van 80-125 procent. Indien bijvoorbeeld de werkelijke uitkomsten zodanig zijn dat het verlies op het hedge-instrument VE 120 bedraagt en de winst op het kasinstrument VE 100 bedraagt, kan de effectiviteit worden gemeten als 120/100, oftewel 120 procent, of als 100/120, oftewel 83 procent. In dit voorbeeld zou de entiteit concluderen dat de hedge zeer effectief is geweest, ervan uitgaande dat de hedge voldoet aan voorwaarde (a).

## Tl106

De effectiviteit wordt in ieder geval beoordeeld bij het opstellen van de jaarrekening en tussentijdse financiële verslagen van de entiteit.

## Tl107

Deze standaard schrijft niet één bepaalde methode voor om de hedge-effectiviteit te beoordelen. Welke methode een entiteit hanteert voor het beoordelen van de hedge-effectiviteit hangt af van de strategie met betrekking tot risicobeheer. Indien de strategie van de entiteit met betrekking tot risicobeheer bijvoorbeeld is om het bedrag van het hedge-instrument periodiek aan te passen aan veranderingen in de gehedgede positie, dan moet de entiteit alleen aantonen dat de hedge naar verwachting zeer effectief zal zijn voor de periode tot de eerstvolgende aanpassing van het bedrag van het hedge-instrument. In sommige gevallen hanteert een entiteit verschillende methoden voor verschillende soorten hedges. In de documentatie van de hedgingstrategie van een entiteit zullen ook de procedures voor beoordeling van de effectiviteit worden opgenomen. Die procedures geven aan of de beoordeling betrekking heeft op de totale winst of het totale verlies op een hedge-instrument, of dat met de tijdswaarde van het instrument geen rekening wordt gehouden. TL107A […].

## Tl108

Zijn de belangrijkste voorwaarden van het hedge-instrument en van het gehedgede actief, de gehedgede verplichting, vaststaande toezegging of zeer waarschijnlijke verwachte toekomstige transactie hetzelfde, dan heffen de aan het gehedgede risico toe te rekenen veranderingen in de reële waarde en kasstromen elkaar waarschijnlijk volledig op, zowel bij het aangaan van de hedge als daarna. Een renteswap, bijvoorbeeld, zal als hedge waarschijnlijk effectief zijn indien het referentiebedrag en de hoofdsom, looptijd, renteherzieningsdata, data van ontvangst en betaling van rente en aflossingen, en de basis voor het bepalen van de rentevoet voor het hedge-instrument en de gehedgede positie gelijk zijn. Voorts is een hedge van een zeer waarschijnlijke verwachte toekomstige transactie van een commodity door middel van een termijncontract waarschijnlijk zeer effectief indien:
(a) het termijncontract de aankoop betreft van dezelfde hoeveelheid van dezelfde commodity, op hetzelfde tijdstip en op dezelfde plaats als de gehedgede verwachte toekomstige aankoop;
(b) de reële waarde van het termijncontract bij afsluiting nihil is; en
(c) de verandering in het disagio of agio op het termijncontract niet wordt betrokken in de beoordeling van de effectiviteit en in winst of verlies wordt opgenomen, of indien de verandering in de verwachte kas stromen van de zeer waarschijnlijke verwachte toekomstige transactie gebaseerd is op de termijnkoers van de commodity.

## Tl109

In sommige gevallen wordt met het hedge-instrument slechts een deel van het gehedgede risico gehedged. Een hedge zal bijvoorbeeld niet volledig effectief zijn als het hedge-instrument en de gehedgede positie in verschil lende valuta’s luiden die niet in hoge mate correleren. Ook een hedge van een renterisico door middel van een derivaat zal niet volledig effectief zijn, indien een deel van de verandering in de reële waarde van het derivaat is toe te rekenen aan het kredietrisico van de wederpartij.

## Tl110

Om voor hedge accounting in aanmerking te komen, moet de hedge betrekking hebben op een specifiek aangegeven en aangemerkt risico, en niet louter op de algemene bedrijfsrisico’s van de entiteit, en moet deze uiteindelijk van invloed zijn op het resultaat van de entiteit. Een hedge van het risico van economische veroudering van een materieel actief of het risico van onteigening van vastgoed door de overheid komt niet in aanmerking voor hedge accounting; de effectiviteit valt immers niet te bepalen, aangezien die risico’s niet betrouwbaar te bepalen zijn.

TL110A Alinea 74(a) staat toe dat een entiteit de intrinsieke waarde en tijdswaarde van een optiecontract scheidt en dat ze alleen de verandering in de intrinsieke waarde van het optiecontract aanmerkt als het hedge-instrument. Dergelijke aanmerking kan resulteren in een hedgerelatie die volledig effectief is in het tot stand brengen van compenserende veranderingen in kasstromen die toerekenbaar zijn aan een gehedged eenzijdig risico van een verwachte toekomstige transactie, indien de belangrijkste voorwaarden van de verwachte toekomstige trans actie overeenstemmen met die van het hedge-instrument. TL110B Als een entiteit een gekochte optie in haar geheel aanmerkt als het hedge-instrument van een eenzijdig risico dat voortvloeit uit een verwachte toekomstige transactie, zal de hedgerelatie niet volledig effectief zijn. Dit komt omdat de voor de optie betaalde premie tijdswaarde omvat en, zoals vermeld in alinea TL99BA, een aangemerkt eenzijdig risico niet de tijdswaarde van een optie omvat. Daarom zal er in dit geval geen sprake zijn van compensatie tussen de kasstromen die verband houden met de tijdswaarde van de betaalde optie premie en het aangemerkte gehedgede risico.

## Tl111

In het geval van renterisico kan de hedge-effectiviteit worden beoordeeld door een looptijdenoverzicht voor financiële activa en financiële verplichtingen op te stellen waaruit de netto-renterisicopositie voor iedere periode blijkt. Voorwaarde hierbij is dat de nettopositie in verband kan worden gebracht met een specifiek actief of een specifieke verplichting (of een specifieke groep activa of verplichtingen, of een specifiek deel daarvan) waaruit dat nettorisico voortvloeit, en dat de hedge-effectiviteit wordt afgemeten aan dat actief of die verplichting.

## Tl112

Bij het beoordelen van de effectiviteit van een hedge neemt een entiteit over het algemeen de tijdswaarde van geld in aanmerking. De vaste rente op een gehedgede positie hoeft niet precies overeen te komen met de vaste rente op een swap die is aangemerkt als reële-waardehedge. De variabele rente op een rentedragend actief of een rentedragende verplichting hoeft evenmin gelijk te zijn aan de variabele rente op een swap die is aange merkt als een kasstroomhedge. De reële waarde van een swap wordt bepaald door de nettoafwikkelingen. De vaste en variabele rentevoeten bij een swap kunnen worden gewijzigd zonder dat dit invloed heeft op de nettoafwikkeling, indien beide evenveel worden gewijzigd.

## Tl113

Indien een entiteit niet aan de criteria voor hedge accounting voldoet, beëindigt de entiteit de hedge accoun ting vanaf de laatste dag waarop de hedge-effectiviteit werd aangetoond. Indien de entiteit de gebeurtenis of verandering in omstandigheden waarneemt waardoor de hedgerelatie niet aan de effectiviteitscriteria voldoet, en aantoont dat de hedge effectief was voordat de gebeurtenis of verandering in omstandigheden plaatsvond, dan beëindigt de entiteit de hedge accounting vanaf de dag waarop de gebeurtenis of verandering in om standigheden plaatsvond. TL113A Om twijfel te vermijden, moeten de gevolgen van de vervanging van de oorspronkelijke tegenpartij door een clearingtegenpartij en van het doorvoeren van de daarmee verband houdende wijzigingen zoals beschreven in de alinea’s 91(a)(ii) en 101(a)(ii) worden weerspiegeld in de waardering van het hedge-instrument en dus in de beoordeling van de hedge-effectiviteit en de waardering van de hedge-effectiviteit. Reële-waarde-hedge-accounting voor een portefeuillehedge van renterisico

## Tl114

Voor een reële-waardehedge van het renterisico van een portefeuille van financiële activa of financiële ver plichtingen zou een entiteit aan de vereisten van deze standaard voldoen indien zij de onderstaande pro cedures in de punten (a) tot en met (i) en de alinea’s TL115 tot en met TL132 naleeft:
(a) De entiteit onderkent als onderdeel van het risicobeheerproces een portefeuille van posten waarvan zij het renterisico wil hedgen. De portefeuille kan bestaan uit alleen activa, alleen verplichtingen of een com binatie van activa en verplichtingen. De entiteit mag twee of meer portefeuilles onderscheiden. In dat geval worden de onderstaande leidraden op elke portefeuille afzonderlijk toegepast.
(b) De entiteit brengt een verdeling aan in de portefeuille op basis van de renteherzieningsperioden, waarbij wordt uitgegaan van de verwachte in plaats van de contractuele renteherzieningsdata. Deze verdeling naar renteherzieningsperioden kan op verschillende manieren worden uitgevoerd. Bijvoorbeeld door kasstro men in te delen op basis van de periode waarin deze naar verwachting zullen plaatsvinden, of door bij een renteswap onderliggende bedragen in te delen in alle perioden totdat de renteherziening naar verwachting zal plaatsvinden.
(c) Op basis van deze verdeling besluit de entiteit over het bedrag dat zij wil hedgen. De entiteit wijst als gehedgede positie een bedrag aan activa of verplichtingen (maar geen nettobedrag) uit de geïdentificeerde portefeuille aan, gelijk aan het bedrag dat zij als gehedged wenst wil wijzen. […].
(d) De entiteit wijst het renterisico aan dat zij aan het hedgen is. Dit risico zou een deel kunnen zijn van het renterisico in iedere post in de gehedgede positie, zoals een referentierente (bv. de LIBOR).
(e) De entiteit wijst voor iedere renteherzieningsperiode een of meer hedge-instrumenten aan.

(f) Op basis van de aanwijzingen die op grond van (c) tot en met (e) zijn gedaan, beoordeelt de entiteit bij het aangaan van de hedge en in daaropvolgende perioden of deze naar verwachting zeer effectief zal zijn gedurende de periode waarvoor de hedge is aangemerkt.
(g) De entiteit bepaalt periodiek de verandering in de reële waarde van de gehedgede positie (zoals aange merkt bij (c)) die is toe te schrijven aan het gehedgede risico (zoals aangemerkt bij (d)), […]. De entiteit neemt de verandering in de reële waarde van de gehedgede positie op als een baat of last in winst of verlies en in één of twee posten in het overzicht van de financiële positie zoals beschreven in alinea 89A op, mits met behulp van de door de entiteit gedocumenteerde methode voor bepaling van de effectiviteit wordt vastgesteld dat de hedge daadwerkelijk zeer effectief is geweest. De verandering in de reële waarde hoeft niet aan individuele activa of verplichtingen te worden toegerekend.
(h) De entiteit bepaalt de verandering in de reële waarde van het hedge-instrument of de hedge-instrumenten (zoals aangemerkt bij (e)) en neemt deze op als baat of last in winst of verlies. De reële waarde van het hedge-instrument of de hedge-instrumenten wordt als actief of verplichting in het overzicht van de financiële positie opgenomen.
(i) De eventuele ineffectiviteit ( 27 ) wordt in winst of verlies opgenomen als het verschil tussen de verandering in de reële waarde vermeld in (g) en die vermeld in (h).

## Tl115

Deze aanpak wordt hierna meer gedetailleerd beschreven. De aanpak moet alleen worden toegepast op een reële-waardehedge van het renterisico betreffende een portefeuille van financiële activa of financiële verplich tingen.

## Tl116

De portefeuille die op grond van TL114(a) wordt geïdentificeerd zou uit activa en verplichtingen kunnen bestaan. Een andere mogelijkheid is dat de portefeuille uitsluitend activa bevat, of alleen verplichtingen. De portefeuille wordt gebruikt om het bedrag van de activa of verplichtingen te bepalen dat de entiteit wil hedgen. De portefeuille wordt echter zelf niet als de gehedgede positie aangemerkt.

## Tl117

Bij de toepassing van alinea TL114(b) bepaalt de entiteit de verwachte renteherzieningsdatum van een post als de vroegste van de datum waarop de post naar verwachting afloopt en de datum waarop de renteherziening naar de marktrente naar verwachting zal plaatsvinden. De verwachte renteherzieningsdata worden geschat bij het aangaan van de hedge en gedurende de looptijd van de hedge, op basis van historische gegevens en andere beschikbare informatie, waaronder informatie en verwachtingen ten aanzien van het percentage vervroegde aflossingen, de rente en de wisselwerking hiertussen. Entiteiten die geen of onvoldoende eigen historie hebben, maken gebruik van gegevens van vergelijkbare entiteiten voor vergelijkbare financiële instrumenten. Deze schattingen worden periodiek beoordeeld en in het licht van de opgedane ervaring geactualiseerd. Indien een vastrentende post vervroegd aflosbaar is, is de verwachte renteherzieningsdatum gelijk aan de datum waarop de post naar verwachting vervroegd wordt afgelost, tenzij de renteherziening naar de marktrente eerder plaatsvindt. Bij een groep van vergelijkbare posten kan de uitsplitsing naar periode op basis van de verwachte renteherzieningsdata geschieden door een percentage van de groep aan iedere periode toe te wijzen, in plaats van de toewijzing van individuele posten. Een entiteit kan voor dergelijke toerekeningsdoeleinden andere methoden toepassen. De entiteit mag bijvoorbeeld een vermenigvuldigingsfactor inzake het percentage ver vroegde aflossingen gebruiken voor de verdeling van aflossingsleningen over perioden op basis van de ver wachte renteherzieningsdata. De methode voor een dergelijke verdeling moet echter in overeenstemming zijn met de procedures en doelstellingen van de entiteit inzake risicobeheer.

## Tl118

Ter illustratie van de aanwijzing die in alinea TL114(c) uiteengezet wordt, wijst een entiteit die voor een bepaalde renteherzieningsperiode schat dat zij vastrentende activa heeft van VE 100 en vastrentende ver plichtingen van VE 80, en besluit de totale nettopositie van VE 20 te hedgen, als gehedgede positie activa aan tot een bedrag van VE 20 (een gedeelte van de activa). De aanwijzing wordt uitgedrukt in een bedrag in een valuta (bv. een bedrag in dollar, euro, Britse pond of rand) in plaats van als individuele activa. Hieruit volgt dat alle activa (of verplichtingen) waaraan het gehedgede bedrag wordt ontleend – d.w.z. in het boven vermelde voorbeeld alle tot de VE 100 behorende activa – posten moeten zijn waarvan de reële waarde verandert als gevolg van veranderingen in de gehedgede rente […].

## Tl119

De entiteit neemt tevens de in alinea 88(a) uiteengezette overige vereisten inzake aanwijzing en documentatie in acht. Bij een portefeuillehedge van renterisico moet uit deze aanwijzing en documentatie blijken wat het beleid van de entiteit is ten aanzien van alle variabelen die worden gebruikt om het gehedgede bedrag te bepalen en op welke wijze de effectiviteit wordt bepaald, waaronder:
(a) de activa en verplichtingen die in de portefeuillehedge opgenomen gaan worden en de te hanteren grondslag voor verwijdering van activa en verplichtingen uit de portefeuille; ( 27 ) In dit verband gelden dezelfde materialiteitsoverwegingen als elders in de IFRSs.

(b) de wijze waarop de entiteit de renteherzieningsdata schat, met inbegrip van de veronderstellingen ten aanzien van de rente die ten grondslag liggen aan het percentage vervroegde aflossingen, en de grondslag voor wijziging van die schattingen. Dezelfde methode wordt gebruikt voor zowel de schattingen die worden gemaakt wanneer een actief of verplichting voor het eerst in de gehedgede portefeuille wordt opgenomen als voor latere herzieningen van deze schattingen;
(c) het aantal en de duur van de renteherzieningsperioden;
(d) de frequentie waarmee de entiteit de effectiviteit zal toetsen […];
(e) de methode die door de entiteit wordt gebruikt om het bedrag te bepalen van de activa of verplichtingen die als gehedgede positie worden aangemerkt […];
(f) […], of de entiteit de effectiviteit zal toetsen voor iedere individuele renteherzieningsperiode, voor alle perioden gezamenlijk of voor een of andere combinatie van beide. De grondslagen die zijn bepaald bij het aanwijzen en documenteren van de hedgerelatie moeten in overeenstemming zijn met de procedures en doelstellingen van de entiteit inzake risicobeheer. Grond slagwijzigingen mogen niet willekeurig worden doorgevoerd. Zij moeten gerechtvaardigd worden op basis van veranderingen in marktomstandigheden en andere factoren, en moeten onderbouwd zijn en in over eenstemming met de procedures en het beleid van de entiteit inzake risicobeheer.

## Tl120

Het hedge-instrument waarnaar in alinea TL114(e) wordt verwezen, kan één derivaat zijn of een portefeuille van derivaten die allemaal blootstaan aan het gehedgede renterisico dat in alinea TL114(d) is aangemerkt (bv. een portefeuille van renteswaps die allemaal blootstaan aan de ontwikkeling van de LIBOR). Een dergelijke portefeuille van derivaten kan elkaar compenserende risicoposities bevatten. Een dergelijke portefeuille kan echter geen (op nettobasis) geschreven opties bevatten, omdat de standaard ( 28 ) niet toestaat dat dergelijke opties als hedge-instrument worden aangemerkt (behalve wanneer een geschreven optie wordt aangemerkt ter compensatie van een gekochte optie). Indien met het hedge-instrument het op grond van alinea TL114(c) aangemerkte bedrag voor meer dan één renteherzieningsperiode wordt gehedged, dan wordt dit toegerekend aan alle gehedgede perioden. Het hedge-instrument moet echter in zijn geheel aan die renteherzieningsperi oden worden toegerekend omdat de standaard ( 29 ) niet toestaat dat een hedgerelatie wordt aangemerkt voor slechts een deel van een periode waarin een hedge-instrument blijft uitstaan.

## Tl121

Wanneer de entiteit de verandering in de reële waarde van een vervroegd aflosbare post in overeenstemming met alinea TL114(g) bepaalt, wordt de reële waarde van de vervroegd aflosbare post op twee manieren door een renteverandering beïnvloed: de renteverandering is van invloed op de reële waarde van de contractuele kasstromen en de reële waarde van de optie tot vervroegde aflossing die in de vervroegd aflosbare post is besloten. Een entiteit mag op grond van alinea 81 van de standaard een deel van een financieel actief of financiële verplichting, waarbij hetzelfde risico wordt gelopen, als de gehedgede positie aanwijzen, mits de effectiviteit kan worden bepaald. […].

## Tl122

In de standaard wordt niet bepaald welke technieken moeten worden gebruikt om het bedrag te bepalen dat in alinea TL114(g) wordt vermeld, namelijk de verandering in de reële waarde van de gehedgede positie die is toe te schrijven aan het gehedgede risico. […]. Het is niet juist te veronderstellen dat veranderingen in de reële waarde van de gehedgede positie gelijk zijn aan veranderingen in de waarde van het hedge-instrument.

## Tl123

Alinea 89A schrijft voor dat, indien de gehedgede positie voor een bepaalde renteherzieningsperiode een actief is, de verandering in de waarde daarvan wordt gepresenteerd als een aparte post binnen de activa. Indien de gehedgede positie voor een bepaalde renteherzieningsperiode een verplichting is, moet de verandering in de waarde daarvan worden gepresenteerd als een aparte post binnen de verplichtingen. Dit zijn de afzonderlijke posten waarnaar in alinea TL114(g) wordt verwezen. Specifieke toerekening aan individuele activa (of ver plichtingen) is niet vereist.

## Tl124

In alinea TL114(i) wordt opgemerkt dat ineffectiviteit ontstaat voor zover de verandering in de reële waarde van de gehedgede positie, die is toe te schrijven aan het gehedgede risico verschilt van de verandering in de reële waarde van het hedgingderivaat. Een dergelijk verschil kan een aantal oorzaken hebben, waaronder:
(a) […];
(b) posten in de gehedgede portefeuille zijn onderhevig aan een bijzondere waardevermindering of worden niet langer opgenomen; ( 28 ) Zie de alinea’s 77 en TL94. ( 29 ) Zie alinea 75.

(c) de betaaldata van het hedge-instrument en de gehedgede positie verschillen; en
(d) overige mutaties […]. De omvang van deze ineffectiviteit ( 30 ) moet worden bepaald en opgenomen in winst of verlies.

## Tl125

Over het algemeen zal de effectiviteit van de hedge verbeteren:
(a) indien de entiteit bij de indeling van posten met verschillende kenmerken wat betreft vervroegde aflossing rekening houdt met de verschillen in het gedrag inzake vervroegde aflossing;
(b) indien het aantal posten in de portefeuille groter is. Bij een relatief gering aantal posten in de portefeuille is het waarschijnlijk dat een relatief hoge mate van ineffectiviteit optreedt indien de vervroegde aflossing van een van de posten eerder of later dan verwacht plaatsvindt. Daarentegen kan bij een portefeuille met meer posten het gedrag inzake vervroegde aflossing nauwkeuriger worden voorspeld;
(c) indien de gehanteerde renteherzieningsperioden korter zijn (bv. renteherzieningsperioden van één maand in plaats van drie maanden). Kortere renteherzieningsperioden verminderen het effect van een mismatch tussen renteherzienings- en betaaldata (binnen de renteherzieningsperiode) van de gehedgede positie en die van het hedge-instrument;
(d) naarmate de frequentie waarmee het bedrag van het hedge-instrument wordt aangepast aan veranderingen in de gehedgede positie (bijvoorbeeld in verband met veranderingen in de verwachtingen ten aanzien van vervroegde aflossing), hoger ligt.

## Tl126

Een entiteit toetst de effectiviteit periodiek. […]

## Tl127

Bij het bepalen van de ineffectiviteit maakt de entiteit een onderscheid tussen herzieningen van de geschatte renteherzieningsdata van de bestaande activa (of verplichtingen) en de creatie van nieuwe activa (of ver plichtingen), waarbij alleen de eerstgenoemde aanleiding geven tot ineffectiviteit. […]. Zodra de ineffectiviteit is opgenomen zoals hiervoor uiteengezet, stelt de entiteit een nieuwe schatting vast van de totale activa (of verplichtingen) in iedere renteherzieningsperiode, met inbegrip van de nieuwe activa (of verplichtingen) die zijn gecreëerd sinds de entiteit voor het laatst de effectiviteit toetste, en wijst zij een nieuw bedrag aan als gehedgede positie en een nieuw percentage als het gehedgede percentage. […]

## Tl128

Posten die oorspronkelijk werden ingedeeld in een renteherzieningsperiode kunnen worden verwijderd omdat er eerder dan verwacht sprake is van vervroegde aflossing of van afwaardering als gevolg van bijzondere waardevermindering of verkoop. Wanneer dit zich voordoet, wordt het bedrag van de verandering in de reële waarde dat is opgenomen in de afzonderlijke post waaraan in alinea TL114(g) wordt gerefereerd, dat betrek king heeft op de niet langer opgenomen post verwijderd uit het overzicht van de financiële positie, en opgenomen in het resultaat dat bij het niet langer opnemen ontstaat. Hiertoe is het noodzakelijk om te weten in welke renteherzieningsperiode(n) de niet langer opgenomen post was ingedeeld, omdat dit bepalend is voor de renteherzieningsperiode(n) waaruit de post moet worden verwijderd, en derhalve voor het bedrag dat uit de afzonderlijke post moet worden verwijderd die in alinea TL114(g) wordt vermeld. Wanneer een post wordt verwijderd, en bepaald kan worden in welke periode deze was opgenomen, dan wordt de post uit deze periode verwijderd. Indien dit niet het geval is, wordt de post verwijderd uit de vroegste periode indien het niet langer opnemen van de post het gevolg was van meer dan verwachte vervroegde aflossingen, of op systematische en rationele basis toegerekend aan alle perioden waarin de niet langer opgenomen post was ingedeeld indien de post werd verkocht of een bijzondere waardevermindering heeft ondergaan.

## Tl129

Bovendien wordt elk bedrag dat betrekking heeft op een bepaalde periode dat bij afloop van de periode niet is verwijderd, op dat moment in winst of verlies opgenomen (zie alinea 89A). […]

## Tl130

[…].

## Tl131

Indien het gehedgede bedrag voor een renteherzieningsperiode wordt verlaagd zonder verwijdering van de desbetreffende activa (of verplichtingen), wordt het bedrag dat is opgenomen in de in alinea TL114(g) ver melde afzonderlijke post, dat betrekking heeft op de verlaging afgeschreven in overeenstemming met ali nea 92. ( 30 ) In dit verband gelden dezelfde materialiteitsoverwegingen als elders in de IFRSs.

## Tl132

Een entiteit zou de in alinea’s TL114 tot en met TL131 uiteengezette aanpak kunnen toepassen op een portefeuillehedge die voorheen administratief was verwerkt als een kasstroomhedge in overeenstemming met IAS 39. Een dergelijke entiteit zou de vorige aanwijzing als kasstroomhedge in overeenstemming met alinea 101(d) intrekken, en de in die alinea vermelde vereisten toepassen. De entiteit zou tevens de hedge nu aanwijzen als een reële-waardehedge en de aanpak in alinea’s TL114 tot en met TL131 prospectief toepassen op toekomstige verslagperioden. OVERGANG (alinea’s 103 tot en met 108c)

## Tl133

Een entiteit kan een verwachte toekomstige intragroepstransactie aan het begin van een jaarperiode die op of na 1 januari 2005 (of, met het oog op de aanpassing van vergelijkende informatie, het begin van een eerdere vergelijkende periode) aanvangt, als gehedgede positie hebben aangemerkt bij een hedge die overeenkomstig deze standaard (als gewijzigd bij de laatste zin van alinea 80) voor de toepassing van hedge accounting in aanmerking zou komen. De entiteit kan deze aanwijzing aangrijpen om vanaf het begin van de jaarperiode die op of na 1 januari 2005 (of het begin van de eerdere vergelijkende periode) aanvangt, in de geconsolideerde jaarrekening hedge accounting toe te passen. De entiteit moet ook de alinea’s TL99A en TL99B toepassen vanaf het begin van de jaarperiode die op of na 1 januari 2005 aanvangt. In overeenstemming met ali nea 108B hoeft zij alinea TL99B echter niet toe te passen op vergelijkende informatie voor eerdere perioden.
