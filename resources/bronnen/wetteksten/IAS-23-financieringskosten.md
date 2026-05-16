---
title: IAS-23 — Financieringskosten
tags:
- '1.5'
- ifrs
- ias
itaa-lex-sectie: ''
wet: Verordening (EU) 2023/1803 — geconsolideerde IFRS
bron_rol: normatief
bron_categorie: ifrs
standaard_type: IAS
standaard_nummer: '23'
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
    pages: 163-167
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

## International Accounting Standard 23

Financieringskosten

## Kernbeginsel

1 Financieringskosten die rechtstreeks zijn toe te rekenen aan de verwerving, bouw of productie van een in aanmerking komend actief vormen een onderdeel van de kostprijs van dat actief. Andere financierings kosten worden als last opgenomen.

## Toepassingsgebied

2 Een entiteit moet deze standaard toepassen bij de administratieve verwerking van financieringskosten. 3 Deze standaard behandelt niet de eigenlijke of toegerekende kosten van eigen vermogen, met inbegrip van preferent aandelenkapitaal dat niet als een verplichting is geclassificeerd. 4 Een entiteit is niet verplicht deze standaard toe te passen op financieringskosten die rechtstreeks zijn toe te rekenen aan de verwerving, bouw of productie van:
(a) een in aanmerking komend actief dat tegen reële waarde wordt gewaardeerd, bijvoorbeeld een biologisch actief dat binnen het toepassingsgebied van IAS 41 Landbouw valt; of
(b) voorraden die in grote hoeveelheden en op repetitieve basis worden geproduceerd als onderdeel van het gewoonlijke productieproces of anderszins.

## Definities

5 De volgende begrippen worden in deze standaard gebruikt met de hierna omschreven betekenis: Financieringskosten zijn rente en andere kosten die een entiteit maakt in verband met het lenen van middelen. Een in aanmerking komend actief is een actief dat noodzakelijkerwijs pas na een aanzienlijke tijdsperiode klaar is voor het beoogde gebruik of voor verkoop. 6 Financieringskosten kunnen het volgende omvatten:
(a) rentelasten die volgens de in IFRS 9 beschreven effectieverentemethode zijn berekend;
(b) [verwijderd]
(c) [verwijderd]
(d) rente in verband met in overeenstemming met IFRS 16 Leaseovereenkomsten opgenomen leaseverplichtingen; en
(e) valutakoersverschillen die voortvloeien uit leningen in vreemde valuta, in zoverre zij als een aanpassing van de rentekosten worden beschouwd. 7 Afhankelijk van de omstandigheden kunnen de volgende items in aanmerking komende activa zijn:
(a) voorraden;
(b) fabrieken;

(c) elektriciteitscentrales;
(d) immateriële activa;
(e) vastgoedbeleggingen;
(f) vruchtdragende planten. Financiële activa en voorraden die in een korte tijdsperiode worden geproduceerd als onderdeel van het gewoon lijke productieproces of anderszins, zijn geen in aanmerking komende activa. Activa die op het moment van hun verwerving klaar zijn voor het beoogde gebruik of voor verkoop zijn evenmin in aanmerking komende activa.

## Opname

8 Een entiteit moet financieringskosten die rechtstreeks zijn toe te rekenen aan de verwerving, bouw of productie van een in aanmerking komend actief activeren als onderdeel van de kostprijs van dat actief. Een entiteit moet andere financieringskosten als last opnemen in de periode waarin ze zijn gemaakt. 9 Financieringskosten die rechtstreeks zijn toe te rekenen aan de verwerving, bouw of productie van een in aan merking komend actief worden opgenomen in de kostprijs van dat actief. Dergelijke financieringskosten worden als deel van de kostprijs van het actief geactiveerd als het waarschijnlijk is dat zij zullen resulteren in toekomstige economische voordelen voor de entiteit en de kostprijs betrouwbaar kan worden bepaald. Wanneer een entiteit IAS 29 Financiële verslaggeving in economieën met hyperinflatie toepast, moet zij het deel van de financieringskosten dat de inflatie tijdens dezelfde periode compenseert als last opnemen in overeenstemming met alinea 21 van die standaard. Financieringskosten die in aanmerking komen voor activering 10 De financieringskosten die rechtstreeks zijn toe te rekenen aan de verwerving, bouw of productie van een in aanmerking komend actief zijn financieringskosten die zouden zijn vermeden indien de uitgaven voor het in aanmerking komende actief niet waren gedaan. Als een entiteit middelen leent met het specifieke doel een bepaald in aanmerking komend actief te verwerven, kunnen de financieringskosten die rechtstreeks verband houden met dat in aanmerking komende actief op eenvoudige wijze worden geïdentificeerd. 11 Het kan moeilijk zijn om een rechtstreeks verband te bepalen tussen bepaalde financieringen en een in aanmerking komend actief, en de financieringskosten te bepalen die anderszins hadden kunnen worden vermeden. Een dergelijke moeilijkheid doet zich bijvoorbeeld voor als de financieringsactiviteiten van een entiteit centraal worden gecoördineerd. Er doen zich eveneens moeilijkheden voor als een groep gebruik maakt van een reeks schuld instrumenten om middelen te lenen tegen variërende rentevoeten, en deze middelen onder verschillende voor waarden uitleent aan andere entiteiten binnen de groep. Andere complicaties ontstaan als leningen worden aange gaan die in vreemde valuta luiden of die aan vreemde valuta zijn gekoppeld indien de groep actief is in eco nomieën met een zeer hoge inflatie, en als gevolg van wisselkoersschommelingen. Bijgevolg is het moeilijk te bepalen welk bedrag van de financieringskosten rechtstreeks is toe te rekenen aan de verwerving van een in aanmerking komend actief en is er een zekere oordeelsvorming vereist. 12 In zoverre een entiteit middelen leent met het specifieke doel een in aanmerking komend actief te verwerven, moet de entiteit het bedrag van de financieringskosten dat in aanmerking komt voor active ring bepalen als de effectieve financieringskosten van die lening tijdens de periode, verminderd met enigerlei beleggingsinkomsten uit de tijdelijke belegging van die lening. 13 De financieringsregelingen voor een in aanmerking komend actief kunnen ertoe leiden dat een entiteit geleende middelen verwerft en daarmee verband houdende financieringskosten maakt vóór sommige of alle middelen worden gebruikt voor uitgaven in verband met het in aanmerking komende actief. In dergelijke gevallen worden de middelen vaak tijdelijk belegd tot ze kunnen worden uitgegeven voor het in aanmerking komende actief. Bij de bepaling van het bedrag van de financieringskosten dat tijdens een periode in aanmerking komt voor activering, worden eventuele beleggingsinkomsten die op dergelijke middelen zijn verkregen in mindering gebracht op de gemaakte financieringskosten.

14 In zoverre een entiteit middelen leent voor algemene doeleinden en deze aanwendt met het oog op het verwerven van een in aanmerking komend actief, moet de entiteit het voor activering in aanmerking komende bedrag van de financieringskosten bepalen door een activeringspercentage toe te passen op de uitgaven voor dat actief. Het activeringspercentage moet gelijk zijn aan het gewogen gemiddelde van de financieringskosten die van toepassing zijn op alle leningen van de entiteit die uitstaan tijdens de periode. Bij deze berekening moet een entiteit echter de financieringskosten die van toepassing zijn op leningen die specifiek met het oog op de verwerving van een in aanmerking komend actief zijn aangegaan buiten beschouwing laten totdat vrijwel alle activiteiten die nodig zijn om dat actief op zijn beoogde gebruik of verkoop voor te bereiden, zijn voltooid. Het bedrag van de financieringskosten dat een entiteit tijdens een periode activeert, mag niet hoger liggen dan het bedrag van de financieringskosten dat zij tijdens die periode heeft uitgegeven. 15 In sommige gevallen is het geëigend om alle leningen van de moedermaatschappij en haar dochterondernemingen op te nemen in de berekening van een gewogen gemiddelde van de financieringskosten. In andere gevallen is het geëigend dat elke dochteronderneming een gewogen gemiddelde hanteert van de financieringskosten die op haar eigen leningen van toepassing zijn. De boekwaarde van het in aanmerking komende actief overschrijdt zijn realiseerbare waarde 16 Indien de boekwaarde of de verwachte uiteindelijke kostprijs van het in aanmerking komende actief hoger ligt dan zijn realiseerbare waarde of opbrengstwaarde, wordt de boekwaarde afgeschreven of afgewaardeerd in overeen stemming met de vereisten van andere International Accounting Standards. In bepaalde gevallen wordt het bedrag van de afschrijving of afwaardering teruggeboekt in overeenstemming met die andere International Accounting Standards. Begin van de activering 17 De activering van financieringskosten als onderdeel van de kostprijs van een in aanmerking komend actief moet aanvangen op de aanvangsdatum. De aanvangsdatum voor activering is de datum waarop de entiteit voor het eerst voldoet aan elk van de volgende voorwaarden:
(a) ze doet uitgaven voor het actief;
(b) ze maakt financieringskosten; en
(c) ze onderneemt activiteiten die nodig zijn om het actief voor te bereiden op zijn beoogde gebruik of verkoop. 18 Uitgaven voor een in aanmerking komend actief omvatten uitsluitend die uitgaven die hebben geleid tot betalingen in contanten, de overdracht van andere activa of het aangaan van rentedragende verplichtingen. Enigerlei ont vangen betalingen naar rato van de voortgang van het werk en steun die in verband met het actief werd verkregen (zie IAS 20 Administratieve verwerking van overheidssubsidies en informatieverschaffing over overheidssteun), worden in mindering gebracht op de uitgaven. De gemiddelde boekwaarde van het actief tijdens een periode, met inbegrip van reeds geactiveerde financieringskosten, is gewoonlijk een redelijke benadering van de uitgaven waarop het activeringspercentage in die periode wordt toegepast. 19 De activiteiten die nodig zijn om het actief voor te bereiden op zijn beoogde gebruik of verkoop, omvatten meer dan de fysieke bouw van het actief. Ze omvatten het technische en administratieve werk vóór de aanvang van de eigenlijke bouw, zoals activiteiten in verband met het verkrijgen van vergunningen vóór de aanvang van de eigenlijke bouw. Dergelijke activiteiten omvatten echter niet het houden van een actief als er geen productie of ontwikkeling plaatsvindt die de toestand van het actief verandert. Financieringskosten die bijvoorbeeld worden gemaakt terwijl terreinen gebruiksklaar worden gemaakt, worden geactiveerd tijdens de periode waarin de activi teiten in verband daarmee plaatsvinden. Anderzijds komen financieringskosten die worden gemaakt terwijl voor bouwdoeleinden verworven grond wordt gehouden zonder dat er enigerlei ontwikkelingsactiviteit plaatsvindt, niet in aanmerking voor activering.

Opschorting van de activering 20 Een entiteit moet de activering van financieringskosten opschorten tijdens lange perioden waarin ze de actieve ontwikkeling van een in aanmerking komend actief onderbreekt. 21 Een entiteit kan financieringskosten maken tijdens een lange periode waarin ze de activiteiten die nodig zijn om een actief voor te bereiden op zijn beoogde gebruik of verkoop onderbreekt. Dergelijke kosten zijn kosten voor het houden van gedeeltelijk voltooide activa en komen niet voor activering in aanmerking. Normaliter schort een entiteit de activering van financieringskosten echter niet op tijdens een periode waarin ze omvangrijke technische en administratieve werkzaamheden uitvoert. Een entiteit schort de activering van financieringskosten evenmin op als een tijdelijk uitstel een noodzakelijk onderdeel vormt van het proces om een actief klaar te maken voor zijn beoogde gebruik of verkoop. De activering wordt bijvoorbeeld voortgezet tijdens de lange periode waarin een hoog waterpeil leidt tot uitstel bij de bouw van een brug, indien een dergelijk hoog waterpeil tijdens de bouw periode normaal is in het betreffende geografische gebied. Beëindiging van de activering 22 Een entiteit moet de activering van financieringskosten beëindigen als vrijwel alle activiteiten die nodig zijn om het in aanmerking komende actief voor te bereiden op zijn beoogde gebruik of verkoop, zijn voltooid. 23 Een actief is gewoonlijk klaar voor zijn beoogde gebruik of verkoop als de eigenlijke bouw van het actief is voltooid, zelfs indien er nog administratieve routinewerkzaamheden moeten worden afgehandeld. Indien er slechts kleine wijzigingen overblijven, zoals de inrichting van een gebouw volgens de aanwijzingen van de koper of de gebruiker, vormt dit een aanwijzing dat vrijwel alle activiteiten zijn voltooid. 24 Als een entiteit de bouw van een in aanmerking komend actief in verschillende delen voltooit en elk deel afzonderlijk kan worden gebruikt terwijl de bouw van andere delen wordt voortgezet, moet de entiteit de activering van financieringskosten beëindigen wanneer vrijwel alle activiteiten die nodig zijn om dat deel voor te bereiden op zijn beoogde gebruik of verkoop zijn voltooid. 25 Een bedrijvenpark met verschillende gebouwen die elk afzonderlijk kunnen worden gebruikt, is een voorbeeld van een in aanmerking komend actief waarvan elk onderdeel kan worden gebruikt terwijl de bouw van de andere onderdelen wordt voortgezet. Een voorbeeld van een in aanmerking komend actief dat voltooid moet zijn vóór enig onderdeel kan worden gebruikt, is een fabriek waarin verschillende productieprocessen in een bepaalde volgorde moeten worden uitgevoerd in verschillende delen van de fabriek op hetzelfde terrein, zoals een staalfa briek.

## Informatieverschaffing

26 Een entiteit moet het volgende vermelden:
(a) het bedrag van de financieringskosten dat tijdens de periode is geactiveerd; en
(b) het activeringspercentage dat is toegepast bij het bepalen van het bedrag van de financieringskosten dat voor activering in aanmerking komt.

## Overgangsbepalingen

27 Indien de toepassing van deze standaard leidt tot een wijziging in de grondslagen voor financiële ver slaggeving, moet een entiteit deze standaard toepassen op financieringskosten die verband houden met in aanmerking komende activa waarvoor de aanvangsdatum voor activering gelegen is op of na de ingangs datum.

28 Een entiteit mag echter een willekeurige datum vóór de ingangsdatum aanwijzen en de standaard toe passen op financieringskosten die verband houden met alle in aanmerking komende activa waarvoor de aanvangsdatum voor activering op of na die datum gelegen is. 28A Alinea 14 is gewijzigd door Jaarlijkse verbeteringen in IFRS-standaarden cyclus 2015-2017, uitgegeven in december 2017. Een entiteit moet deze wijzigingen toepassen op financieringskosten die zijn gemaakt bij of na het begin van de jaarlijkse verslagperiode waarin de entiteit deze wijzigingen voor het eerst toepast.

## Ingangsdatum

29 Entiteiten moeten deze standaard toepassen voor jaarperioden die op of na 1 januari 2009 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze standaard toepast vanaf een datum vóór 1 januari 2009, moet zij dit feit vermelden. 29A Alinea 6 is gewijzigd door Verbeteringen in IFRSs, uitgegeven in mei 2008. Entiteiten moeten die wijziging toepas sen op jaarperioden die op of na 1 januari 2009 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit de wijziging op een eerdere periode toepast, moet zij dit feit vermelden. 29B Alinea 6 is gewijzigd door IFRS 9, als uitgegeven in juli 2014. Een entiteit moet die wijziging toepassen wanneer zij IFRS 9 toepast. 29C Alinea 6 is gewijzigd door IFRS 16, uitgegeven in januari 2016. Een entiteit moet deze wijziging toepassen wanneer zij IFRS 16 toepast. 29D Alinea 14 is gewijzigd en alinea 28A is toegevoegd door Jaarlijkse verbeteringen in IFRS-standaarden cyclus 2015- 2017, uitgegeven in december 2017. Entiteiten moeten deze wijzigingen toepassen op jaarlijkse verslagperioden die op of na 1 januari 2019 aanvangen. Eerdere toepassing is toegestaan. Als een entiteit deze wijzigingen eerder toepast, moet zij dit feit vermelden.

## Intrekking Van Ias 23 (Herziene Versie Van 1993)

30 Deze standaard vervangt de in 1993 herziene versie van IAS 23 Financieringskosten .
