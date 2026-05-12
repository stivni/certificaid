---
tags: ["2.2", "2.3", "2.5"]
itaa-lex-sectie: ""
wet: "Belastinggids 2025 — ACLVB"
bron_rol: "praktijkgids"
status: "beschikbaar"
bijgewerkt: "05.2025"
bron: "ejustice.just.fgov.be (gecoördineerde versie)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/belastinggids-aclvb-2025.pdf
      sha256: 6fc36df9c407289d6ef85297bdd13a9aca1a5ca13f492a7ffbe364ba796b1010
      version: '05.2025'
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 6655d4b-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T20:05:33Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-12T20:58:28Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "L1 flags terecht: 126 dotted-leader TOC-regels door het document (A2). Paginanummer 'Belastinggids 2025 • 3' op regel 107 is een pagina-voettekst in de body (A1). Cover-pagina-ruis bovenaan (regels 57-67): 'Belastinggids\\n2025\\n Belastinggids\\n2025\\n 2V.U.:\\n• Gert\\nBrochure\\nTruyens,\\nA5 Koning Albertlaan 95...'. Heading-count van 5 is correct voor de 5 hoofdstukken, maar sectie-groottes zijn enorm."
    layer1:
      status: warn
      run_id: 20260512-203610
      run_at: '2026-05-12T20:36:15Z'
      heading_count: 5
      max_section_chars: 89710
      file_size_chars: 154793
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ##-niveau: 89710 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
        - name: no_toc_dots
          status: warn
          detail: 126 TOC-stippen-regel(s) gevonden
          samples:
            - '................................................................................'
            - '................................................................................'
            - '................................................................................'
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T20:58:28Z'
      rationale: "L1 flags terecht: 126 dotted-leader TOC-regels door het document (A2). Paginanummer 'Belastinggids 2025 • 3' op regel 107 is een pagina-voettekst in de body (A1). Cover-pagina-ruis bovenaan (regels 57-67): 'Belastinggids\\n2025\\n Belastinggids\\n2025\\n 2V.U.:\\n• Gert\\nBrochure\\nTruyens,\\nA5 Koning Albertlaan 95...'. Heading-count van 5 is correct voor de 5 hoofdstukken, maar sectie-groottes zijn enorm."
      concrete_problemen:
        - regel: 70
          categorie: A2
          type: dotted-leader
          voorbeeld: I Woord vooraf.................................................................................................................  9
        - regel: 107
          categorie: A1
          type: form-feed
          voorbeeld: Belastinggids 2025 • 3
        - regel: 57
          categorie: A6
          type: scrambled-words
          voorbeeld: Belastinggids\n2025\n Belastinggids\n2025\n 2V.U.:\n• Gert\nBrochure\nTruyens,\nA5 Koning Albertlaan 95, 9000 Gent
---

# Belastinggids 2025 — ACLVB

*Bijgewerkt tot en met 05.2025 — gecoördineerde versie.*

Belastinggids
2025

 Belastinggids
2025

 2V.U.:
• Gert
Brochure
Truyens,
A5 Koning Albertlaan 95, 9000 Gent. 05/2025

 inhoudsopgave
I Woord vooraf.................................................................................................................................................................................. 9
II Belasting en het gezin.......................................................................................................................................................... 11
1. Gehuwd, wettelijk samenwonend of alleenstaand?................................................................................... 11
a. Echtgenoten of gehuwden. ..................................................................................................................................... 11
b. Alleenstaanden. ................................................................................................................................................................. 12
2. Hoe worden gehuwden en wettelijk samenwonenden belast?....................................................... 12
a. Beroepsinkomsten.......................................................................................................................................................... 12
b. Onroerende inkomsten en intresten. ............................................................................................................. 13
c. Diverse inkomsten. ......................................................................................................................................................... 13
d. Aftrekbare bestedingen.............................................................................................................................................. 13
e. Uitgaven die recht geven op een belastingvermindering. ........................................................ 13
3. Kinderen en andere personen ten laste.................................................................................................................. 14
a. Wie kan fiscaal ten laste zijn?. ............................................................................................................................. 14
b. Welke voorwaarden moeten vervuld zijn?............................................................................................... 14
4. Inkomsten van kinderen........................................................................................................................................................ 16
III Belastbare inkomsten......................................................................................................................................................... 19
1. De onroerende inkomsten. .................................................................................................................................................. 19
a. Principe van belasting................................................................................................................................................. 19
b. Uitzonderingen................................................................................................................................................................... 19
c. Absolute vrijstelling KI ‘eigen woning’........................................................................................................ 20
d. Aangifte KI buitenlandse woning. .................................................................................................................... 20
2. De beroepsinkomsten.............................................................................................................................................................. 20
a. Bezoldigingen. .................................................................................................................................................................... 21
b. Beroepskosten. ................................................................................................................................................................... 24
b.1 Forfaitaire aftrek beroepskosten werknemers.............................................................................. 24
b.2 Werkelijke beroepskosten................................................................................................................................ 25
b.2.1 Kosten voor auto en motorvoertuigen..................................................................................... 25
b.2.2 Andere vervoermiddelen woon-werkverkeer. ................................................................... 26
b.2.3 Diverse kosten................................................................................................................................................. 27
c. Vervangingsinkomsten............................................................................................................................................... 27
3. De diverse inkomsten............................................................................................................................................................... 27
4. Roerende inkomsten. ................................................................................................................................................................ 28
5. Verenigingswerk en deeleconomie.............................................................................................................................. 28
IV Berekening van de belasting........................................................................................................................................ 31
1. Financiering, autonomiefactor en opcentiemen............................................................................................. 31
2. Berekeningsgrondslag............................................................................................................................................................ 32
3. Roerende inkomsten. ................................................................................................................................................................ 33
Belastinggids 2025 • 3

 4. Fiscale woonplaats. .................................................................................................................................................................... 34
5. De belasting....................................................................................................................................................................................... 34
6. Belastingvrije som....................................................................................................................................................................... 35
7. Uitsluitende bevoegdheden van de federale staat. ...................................................................................... 36
8. Uitsluitende bevoegdheden van de gewesten.................................................................................................. 38
9. Overzicht fiscale voordelen.................................................................................................................................................. 38
9.1 Aftrekbare bestedingen.............................................................................................................................................. 39
9.2 Belastingverminderingen. ....................................................................................................................................... 39
a. Federale belastingverminderingen. ....................................................................................................... 40
a.1 Niet-eigen woning. ..................................................................................................................................... 40
a.2 Giften........................................................................................................................................................................ 40
a.3 Kosten voor uitgaven voor kinderoppas. ............................................................................... 40
a.4 Bezoldigingen van een huisbediende...................................................................................... 41
a.5 Langetermijnsparen.................................................................................................................................. 41
a.6 Intresten van groene leningen........................................................................................................ 42
a.7 Elektrische twee-, drie- of vierwieler. ........................................................................................ 42
a.8 Bezoldiging voor overwerk................................................................................................................. 43
a.9 Aandelen van erkende ontwikkelingsfondsen................................................................. 43
a.10 Nieuwe aandelen/tax shelter voor startende vennootschappen.................... 44
a.11 Nieuwe aandelen/tax shelter van groeibedrijven......................................................... 44
a.12 Adoptiekosten. ................................................................................................................................................ 44
a.13 Rechtsbijstandsverzekering............................................................................................................... 44
a.14 Pensioenen en vervangingsinkomsten ................................................................................. 44
a.15 Inkomsten uit het buitenland........................................................................................................... 44
a.16 Dividenden......................................................................................................................................................... 44
a.17 Installatie thuislaadpaal........................................................................................................................ 45
b. Gewestelijke belastingverminderingen.............................................................................................. 45
b.1 Eigen woning................................................................................................................................................... 45
b.2 Restauratie monumenten.................................................................................................................... 45
b.3 Dakisolatie.......................................................................................................................................................... 46
b.4 PWA-cheques, wijk-werkcheques en dienstencheques . ....................................... 46
b.5 Vernieuwing sociaal verhuurde woning. ............................................................................... 47
c. Belastingverminderingen voor vervangingsinkomsten. .................................................... 47
9.3 Belastingkredieten . ....................................................................................................................................................... 48

4 • Belastinggids 2025

 a. Belastingkrediet voor kinderen ten laste........................................................................................... 48
b. Belastingkrediet voor werknemers met lage lonen (fiscale werkbonus)........... 49
c. Belastingkrediet voor dienstencheques............................................................................................. 49
d. Omzetting gewestelijk woonbonus in belastingkrediet...................................................... 49
e. Belastingkrediet Win-winlening, Coup de Pouce-lening en Proxi-lening. ........ 50
f. Belastingkrediet voor vriendenaandelen.......................................................................................... 52
10. Woonfiscaliteit na de zesde staatshervorming. ............................................................................................... 52
10.1 Gewestelijke inwoner. .................................................................................................................................................. 52
10.2 Begrip ‘eigen woning’. ................................................................................................................................................ 52
a. Fiscale uitgaven......................................................................................................................................................... 52
b. Begrip ‘eigen woning’. ........................................................................................................................................ 52
c. Tijdstip beoordeling ‘eigen woning’...................................................................................................... 52
d. Absolute vrijstelling ‘eigen woning’....................................................................................................... 53
10.3 Aangifte van de onroerende inkomsten. .................................................................................................... 54
10.4 Fiscale voordelen woningkredieten. .............................................................................................................. 54
a. Leningen vanaf 1 januari 2020. ................................................................................................................ 56
a.1 Vlaams gewest............................................................................................................................................... 56
a.2 Waals gewest................................................................................................................................................... 56
a.3 Brussels gewest............................................................................................................................................. 56
b. Leningen vanaf 1 januari 2017. ................................................................................................................ 56
b.1 Vlaams gewest............................................................................................................................................... 56
b.2 Waals gewest................................................................................................................................................... 57
b.3 Brussels gewest............................................................................................................................................. 57
c. Hypothecaire leningen vanaf 1 januari 2016 voor de ‘eigen’ woning
   en de ‘niet-eigen’ woning................................................................................................................................. 59
c.1 Vlaams gewest............................................................................................................................................... 59
c.2 Waals gewest................................................................................................................................................... 59
c.3 Brussels gewest (opgelet! Leningen t.e.m. 31.12.2016). .................................. 60
d. Hypothecaire leningen gesloten in 2015 voor de ‘eigen’ woning. .......................... 60
d.1 Vlaams gewest............................................................................................................................................... 60
d.2 Waals gewest................................................................................................................................................... 61
d.3 Brussels gewest............................................................................................................................................. 61
e. Hypothecaire leningen gesloten tussen 1 januari 2005 en 31 december
   2014 voor de ‘eigen’ woning. ...................................................................................................................... 62
e.1 Vlaams gewest............................................................................................................................................... 62
e.2 Waals gewest................................................................................................................................................... 63
e.3 Brussels gewest............................................................................................................................................. 63

Belastinggids 2025 • 5

 f. Hypothecaire leningen gesloten vóór 31 december 2004 voor
   de ‘eigen’ woning voor het Vlaams, Waals en Brussels gewest................................. 64
g. Kapitaalaflossingen en intresten die op het tijdstip van de betaling
   betrekking hebben op een andere dan de ‘eigen’ woning: steeds
   federale voordelen. ................................................................................................................................................. 65
g.1 Lening afgesloten tot 2023............................................................................................................... 65
g.2 Lening afgesloten tussen 1 januari 2005 en 31 december 2013............... 65
g.3 Lening afgesloten tussen 1 januari 1993 en 31 december 2014
  
(voor kapitaalaflossingen) en tussen 01.05.1986 en 31.12.2014
  
(voor intresten).............................................................................................................................................. 66
11. Afzonderlijke aanslagen......................................................................................................................................................... 67
a. Taxatieregels individuele levensverzekeringen en pensioensparen. .............................. 67
b. Taxatieregels aanvullende pensioenen. ..................................................................................................... 68
1. Voor het kapitaal opgebouwd uit de werknemersbijdragen ............................. 69
2. Voor het kapitaal opgebouwd uit de werkgeversbijdragen................................. 69
c. Worden eveneens belast tegen 33%............................................................................................................ 70
d. Worden belast tegen de gemiddelde aanslagvoet. ......................................................................... 70
e. Omzetting in een lijfrente van sommige kapitalen, vergoedingen en
  afkoopwaarden................................................................................................................................................................... 71
12. Voorheffingen en voorafbetalingen............................................................................................................................. 72
a. Bedrijfsvoorheffing. ........................................................................................................................................................ 72
b. Mogelijkheden tot voorafbetaling. ................................................................................................................... 72
13. Bijzondere bijdrage voor de sociale zekerheid................................................................................................. 73
14. Gemeente­belasting. ................................................................................................................................................................... 74
V Niet akkoord met de fiscus?Verweer u!..........................................................................................................77
Bijlage: Cijfers in een notendop...................................................................................................................................... 79

6 • Belastinggids 2025

 Belastinggids 2025 • 7

 8 • Brochure A5

## I Woord vooraf
De nieuwe belastingaangifte telt iets meer codes dan vorig jaar. Dat is in de 3 gewesten het
geval. Er zijn nieuwe fiscale maatregelen op het vlak van overuren, flexi-jobinkomsten en belastingkredieten. Belangrijke nieuwigheden vallen eveneens te noteren bij de fietsvergoedingen
die worden deels aan banden gelegd. Verder heeft u minder voordeel met uw hypotheeklening
voor een tweede woning.
Voor aanslagjaar 2025 zijn de indieningstermijnen – net als de twee vorige aanslagjaren –
gebaseerd op de aard van de inkomsten en de complexiteit van de aangifte. Sinds aanslagjaar
2024 zijn de indieningstermijnen in de wet verankerd. Doet u de aangifte nog op papier dan
is de uiterste datum 30 juni 2025. Bij een aangifte via MyMinfin heeft u tot 15 juli 2025 de tijd
(zowel burgers als mandatarissen). Een langere aangiftetermijn wordt toegekend als ze één of
meerdere inkomsten bevat en daardoor als ‘complex’ wordt beschouwd d.w.z. bij:
• winsten en/of baten
• bezoldigingen van bedrijfsleiders
• bezoldigingen aan meewerkende echtgenoten (wettelijk samenwonenden)
• buitenlandse beroepsinkomsten.
Op papier zal de ‘complexe’ aangifte nog steeds ingediend moeten worden tegen 30 juni
2025. Maar via MyMinfin (tax-on-web) heeft u tijd tot 16 oktober 2025 (voor zowel burgers als
mandatarissen).
Wenst u het voorstel van vereenvoudigde aangifte te wijzigen, dan doet u dit binnen de
normale termijnen d.w.z. 30 juni 2025 (papieren aangifte) of 15 juli 2025 (MyMinfin). Als de
vereenvoudigde aangifte een complexe aangifte wordt dan zal u ten laatste op 15 juli 2025
een verlenging moeten aanvragen. Dit doet u door te bellen naar 02/572 57 57 waarbij u de
code 17001 gebruikt.
Hou er rekening mee dat de aangifte sinds twee aanslagjaren genderneutraal is geworden.
Voortaan staat in de linkerkolom de oudste en in de rechtse kolom de jongste partner (bij een
gemeenschappelijke aangifte).
Voor specifieke situaties of bij problemen kan u als lid uiteraard steeds een beroep doen op
onze diensten. Op de website www.aclvb.be/nl/secretariaten vindt u de adressen terug van de
verschillende zones van de ACLVB die u graag verder helpen.
Studiedienst ACLVB
april 2025

Belastinggids 2025 • 9

 10 • Brochure A5

## II Belasting en het gezin
1. Gehuwd, wettelijk samenwonend of alleenstaand?

Er zijn 2 soorten belastingplichtigen: gehuwd of alleenstaand, waarbij:
• gehuwd = gehuwden en wettelijk samenwonenden (homo- of heterokoppels)
• alleenstaanden = alleenstaanden en feitelijk samenwonenden
Als u gehuwd bent of wettelijk samenwoont, moet u een gemeenschappelijke aangifte
invullen vanaf de inkomsten van het jaar volgend op het huwelijk of op de verklaring
van wettelijk samenwonen. Als u in 2024 huwde (en in 2023 nog niet wettelijk samenwoonde) of als u in 2024 een verklaring van wettelijk samenwonen heeft afgelegd,
wordt u nog beschouwd als alleenstaande. Alleenstaanden vullen steeds een eigen
aangifte in en worden afzonderlijk belast.

Wie is wat?
a. Echtgenoten of gehuwden

Zij die:
• gehuwd zijn vóór 1 januari 2024 en in 2024 niet wettelijk gescheiden zijn;
• wettelijk samenwonen vóór 1 januari 2024 en deze samenwoning niet
hebben beëindigd;
• in de loop van 2024 feitelijk gescheiden zijn.
Wat zijn wettelijk samenwonenden?
Het Belgisch Burgerlijk Wetboek definieert wettelijk samenwonen als volgt:
“Onder wettelijke samenwoning wordt de toestand van samenleven verstaan van twee
personen die een verklaring van wettelijke samenwoning hebben afgelegd door middel
van een geschrift dat tegen ontvangstbewijs wordt overhandigd aan de ambtenaar van
de burgerlijke stand van de gemeenschappelijke woonplaats”.
Verder wordt er bepaald dat de wettelijke samenwoning ophoudt wanneer één van de
partijen in het huwelijk treedt of overlijdt, of wanneer er een einde aan wordt gemaakt
hetzij in onderlinge overeenstemming, hetzij eenzijdig door één van de samenwonenden. Dit laatste kan door middel van een schriftelijke verklaring die tegen ontvangst­
bewijs wordt overhandigd aan de ambtenaar van de burgerlijke stand. De ambtenaar
van de burgerlijke stand zal opnieuw melding maken van de beëindiging van de wettelijke samenwoning in het Rijksregister.
Belastinggids 2025 • 11

 b. Alleenstaanden

Zij die niet gehuwd zijn. Het gaat hier om personen die niet of niet meer gehuwd zijn of
­personen die niet of niet meer wettelijk samenwonen.
In de praktijk gaat het om:
• alleenstaanden;
• feitelijk samenwonenden;
• wettelijk gescheiden, ook bij echtscheiding in 2024;
• ex-wettelijk samenwonenden, ook bij herroeping van contract in 2024;
• weduwnaars en weduwen, ook bij overlijden van de partner in 2024;
• na overlijden van een wettelijk samenwonende partner, ook bij overlijden in 2024;
• bij huwelijk of samenlevingscontract in 2024;
• bij feitelijke scheiding van vóór 2024.

2. Hoe worden gehuwden en wettelijk samenwonenden belast?

Sinds aanslagjaar 2005 worden alle inkomsten, aftrekbare bestedingen en uitgaven die
recht geven op een belastingvermindering gedecumuleerd.

a. Beroepsinkomsten
Twee beroepsinkomsten: de ‘decumul’
De beroepsinkomsten worden afzonderlijk belast en beide bedragen worden daarna
samen­geteld. Wanneer echter één van beiden minder verdient dan 13 050 euro of nog
geen 30% van de totale beroepsinkomsten, wordt de regel van het ‘huwelijksquotiënt’
toegepast.
Eén beroepsinkomen: eerst ‘het huwelijksquotiënt’ en dan decumul
De partner zonder beroepsinkomsten krijgt fictief 30% van de beroepsinkomsten van
de ander toebedeeld met een maximum van 13 050 euro. Na deze opdeling worden zij
apart belast en worden beide bedragen samengeteld.

!  Opgelet! Het fiscaal voordeel wordt van het huwelijksquotiënt ­ingeval van emigratie of immigratie nog slechts ‘pro rata temporis’ toegekend (= X/12den).

12 • Belastinggids 2025

 b. Onroerende inkomsten en intresten
Vraag: Gehuwd met welk huwelijksstelsel?
Gemeenschap van goederen of wettelijk stelsel:
Bij ieder voor 50% (ook indien woning slechts eigendom is van één van beiden want de
opbrengst van het goed – zijnde het KI – is gemeenschappelijk);
Scheiding van goederen en wettelijk samenwonenden:
Vraag: wie is eigenaar en volgens welke verhouding? Volgens deze verhouding moet de
­opsplitsing worden gemaakt en wordt het onroerend inkomen belast bij elke partner.

c. Diverse inkomsten

Ontvangen onderhoudsuitkeringen worden belast in hoofde van de partner aan wie
ze zijn toegekend. De andere diverse inkomsten: afhankelijk van het huwelijksstelsel
(zie b. hierboven).

d. Aftrekbare bestedingen

Deze bedragen worden met uitzondering van de door één partner betaalde onderhouds­
uitkeringen, evenredig afgetrokken van het netto-inkomen van iedere partner.

e. Uitgaven die recht geven op een belastingvermindering

Een uitgave enkel door één partner gedaan (vb. pensioensparen) geeft enkel een vermindering op de belasting van die partner.
De algemene regel is dat voor alle belastingverminderingen de omdeling van de
belastingvermindering tussen echtgenoten (en wettelijk samenwonenden) bij wie dus
een gemeenschappelijke aanslag wordt gevestigd, evenredig gebeurt in functie van het
belastbaar inkomen van elk van de partners ten opzichte van de som van de inkomsten
van de beide partners. Bijvoorbeeld: giften, uitgaven voor kinderopvang, dienstencheques, enz.
Toch wordt niet elke belastingvermindering bij een gemeenschappelijke aanslag
onderling in de belastingberekening verdeeld volgens ieders aandeel in het belastbaar
inkomen. Bij de vermindering voor intresten bijvoorbeeld gebeurt dit enkel voor de
gewestelijke vermindering van intresten en niet voor de federale vermindering waar
de automatische overdracht van het saldo van de intresten van de ene partner naar de
andere partner behouden blijft.

Belastinggids 2025 • 13

 3. Kinderen en andere personen ten laste

Het is van groot belang te weten welke personen u fiscaal ten laste kunt nemen
­aangezien dit voor u voordelen biedt wat betreft de berekening van de belasting,
de onroerende voorheffing, … Kinderen en andere personen ten laste geven recht
op een verhoging van de belastingvrije som.

a. Wie kan fiscaal ten laste zijn?

a. uw afstammelingen: kinderen, kleinkinderen, pleegkinderen, …;
b. uw ascendenten: ouders, grootouders, …;
c. uw broers en/of zussen;
d. personen van wie u ten laste bent geweest toen u kind was (mensen die u in hun
gezin hebben opgenomen);
e. een kind dat financieel volledig of hoofdzakelijk aan uw zorgen is toevertrouwd (vb. het
kind van uw feitelijk samenwonende partner kan ten laste van u genomen worden).

!  Een echtgeno(o)t(e) of samenwonende partner (wettelijk of feitelijk)
kan nooit ten laste zijn.

b. Welke voorwaarden moeten vervuld zijn?
Deze personen moeten op 1 januari 2025 deel uitmaken van uw gezin.
Wanneer ouders gescheiden leven, is hun kind ten laste van de ouder bij wie het kind
hoofd­zakelijk verblijft (ouder met hoederecht).
Co-ouderschap
Onder bepaalde voorwaarden wordt bij co-ouderschap het voordeel van de bijkomende
belasting­vrije sommen automatisch tussen de beide (niet samenwonende) ouders
verdeeld. Het co-ouderschap dient aan de volgende voorwaarden te voldoen:
• er moet ten laatste op 1 januari 2025 een geregistreerde of een door een rechter
gehomologeerde overeenkomst bestaan waarin uitdrukkelijk vermeld wordt dat de
huisvesting van die kinderen gelijkmatig verdeeld is over de beide belastingplichtigen
en dat zij bereid zijn de bijkomende belastingvrije sommen te verdelen;
of
• er moet ten laatste op 1 januari 2025 een rechterlijke beslissing genomen zijn waarin
uitdrukkelijk bepaald wordt dat de huisvesting van die kinderen gelijkmatig is verdeeld
over beide belastingplichtigen.
Deze verdeling van fiscaal co-ouderschap zal niet gebeuren indien één van de ouders
onderhoudsuitkeringen aftrekt die hij/zij heeft betaald voor de kinderen.

14 • Belastinggids 2025

 De verdeelbare belastingvrije sommen betreffen ‘alle’ bijkomende belastingvrije sommen inclusief ‘alleenstaande ouder’ conform de individuele situatie van elke ouder.
Fiscaal co-ouderschap uitgebreid tot meerderjarige kinderen
Volgens het Burgerlijk Wetboek zijn enkel minderjarige kinderen onderworpen aan het
ouderlijk gezag. Aangezien het ‘gezamenlijk uitoefenen van het ouderlijk gezag’ een cruciale voorwaarde is om co-ouderschap te kunnen toepassen en meerderjarige kinderen
niet aan het ouderlijk gezag zijn onderworpen, was tot voor kort het fiscaal co-ouderschap over meerderjarige kinderen uitgesloten.
De fiscale wetgeving heeft de verwijzing naar ‘gezamenlijke uitoefening van het ouderlijk gezag’ geschrapt en verwijst nu naar de onderhoudsplicht tegenover hun kinderen
(art. 203 BW). De onderhoudsplicht stopt niet bij meerderjarigheid van het kind maar
loopt dus verder tot na de meerderjarigheid indien het kind zijn/haar opleiding nog niet
voltooid heeft.
Bij een feitelijk samenwonend ongehuwd koppel kunnen de gemeenschappelijke
kinderen niet tegelijkertijd als ten laste van de vader en de moeder aangemerkt worden.
Deze kinderen zijn ten laste van de ouder die ‘in feite’ aan het hoofd staat van dat gezin.
Wie van beiden dit is, moet worden uitgemaakt aan de hand van de feitelijke gegevens.
Sommige personen worden geacht toch deel te blijven uitmaken van het gezin hoewel
ze er niet dagelijks aanwezig zijn (vb. student op kot). Een kind of persoon, op 1 januari
2024 ten laste maar in de loop van 2024 overleden, wordt beschouwd als deel uitmakend van het gezin op 1 januari 2025. Een doodgeboren kindje kan als ten laste worden
beschouwd.
nieuw ! Kinderen die nog ten laste zijn mogen in 2024 niet meer dan respectievelijk
7 290 euro netto bestaansmiddelen hebben genoten (dit geldt enkel voor aanslagjaren
2024 en 2025).
‘Bestaansmiddelen’ omvatten inkomsten van de persoon ten laste zoals eigen bezoldigingen. Er wordt geen rekening gehouden met o.a. studiebeurzen, kinderbijslag en
achterstallig onderhoudsgeld. Gewone onderhoudsuitkeringen van kinderen worden tot
een bedrag van 3 980 euro per jaar voortaan niet meer aangemerkt als bestaansmiddel.

!  Opgelet! Bij emigratie of immigratie worden de toegelaten bestaansmiddelen voor
personen ten laste nog slechts ‘pro rata temporis’
toegepast (= X/12den).

Belastinggids 2025 • 15

 De eerste 3 310 euro verdiend in het kader van een arbeidsovereenkomst voor studenten, ­worden evenmin beschouwd als bestaansmiddelen. Het vrijgestelde bedrag geldt
eveneens voor de baten van een student-zelfstandige en voor bezoldigingen in het
kader van alternerend leren.
Voor inwonende ouders of broers of zussen boven de 65 jaar wordt het pensioen­
inkomen tot 32 040 euro evenmin aanzien als bestaansmiddelen.

4. Inkomsten van kinderen

Onderhoudsgeld voor kinderen, de alimentatie dus, vormt een inkomen voor een kind
dus het is niet voor de ouder die de gelden ontvangt. Kinderen vanaf 16 jaar moeten
een aangifte indienen als er onderhoudsuitkeringen voor hen worden betaald. Ook als
het bedrag onder de belastingvrije som ligt (10 570 euro).
Kinderen jonger dan 16 jaar zijn alleen verplicht een aangifte in te dienen als het bedrag
van de onderhoudsgelden meer bedraagt dan de belastingvrije som. Het gaat hier wel om
netto-bestaansmiddelen (d.w.z. het brutobedrag verminderd met 20% forfaitaire kosten).
Ook jobstudenten moeten een belastingaangifte indienen. Dat kan eenvoudig en snel
via MyMinfin.be. Wilt u toch liever de aangifte op papier indienen, en u heeft vóór 1 juni
nog geen aangifteformulier ontvangen, dan zal u zelf een formulier moeten aanvragen
bij uw belastingkantoor. In de aangifte vermeldt u alle belastbare inkomsten, d.w.z. ook
het deel van de (eventuele) onderhoudsuitkeringen en de bezoldigingen dat niet als
bestaans­middelen wordt beschouwd en waarmee dus geen rekening wordt gehouden
om te bepalen of u nog ten laste van uw ouders bent.

16 • Belastinggids 2025

 Belastinggids 2025 • 17

 18 • Brochure A5

## III Belastbare inkomsten
1. De onroerende inkomsten

Inkomsten van in België of in het buitenland gelegen onroerende goederen zijn de
eerste categorie van aan te geven belaste inkomsten.

a. Principe van belasting

Het belastbaar inkomen is het kadastraal inkomen (KI) van het onroerend goed
­wanneer u er zelf in woont.
Dit KI stelt de normale huurwaarde voor van 1 jaar. Dit bedrag wordt voor alle onroerende goederen vastgelegd voor een langere periode (algemene perequatie). De thans
gebruikte KI’s zijn de weergave van de huurwaarden van 1975.
Het kan ook gebeuren dat u uw huis verbouwt waardoor het een meerwaarde krijgt.
In dit geval wordt een bijzondere perequatie – een herziening van het KI – doorgevoerd.
U moet spontaan de Algemene Administratie van de Patrimoniumdocumentatie (AAPD)
op de hoogte brengen van de verbouwingen binnen de 30 dagen na de voltooiing
van de werken. Werken door energiebesparende uitgaven kunnen enkel leiden tot een
verhoging van het KI indien aan de woning een beduidend nieuw comfortelement is
toegevoegd, vb. de installatie van een centrale verwarming. Indien het enkel gaat over
werken bedoeld om louter energie te besparen (vb. isolatiewerken) zonder impact op de
huurwaarde van het onroerend goed, dan is er geen reden om het KI te herschatten.
De KI’s worden jaarlijks geïndexeerd. Voor het aanslagjaar 2025 wordt het KI vermenigvuldigd met 2,1763 (vb.: KI: 1 500 euro → aanslagjaar 2025 KI = 3 264,45 afgerond
3 264 euro). In de aangifte vermeldt u het niet geïndexeerde bedrag.

b. Uitzonderingen

1. Als u uw huis gebruikt voor beroepsdoeleinden, behoort dit tot uw beroepsinkomsten.
2. Voor uw tweede woning wordt het KI vermenigvuldigd met 1,40.
3. Als u uw huis verhuurt aan een derde voor privédoeleinden,
wordt het KI vermenigvuldigd met 1,40.
4. Als u uw huis verhuurt aan een natuurlijk persoon voor professionele doeleinden of
aan een rechtspersoon, bestaat het belastbaar inkomen uit de netto-huurprijs en de
huurlasten, met minimum het KI.

Belastinggids 2025 • 19

 c. Absolute vrijstelling KI ‘eigen woning’

Sinds aanslagjaar 2006 is het KI van de eigen woning een vrijgesteld onroerend inkomen
indien u:
• geen intresten meer inbrengt van een lening aangegaan vóór 01.01.2005;
• intresten inbrengt van een lening aangegaan vanaf 01.01.2005.
Sinds aanslagjaar 2015 heeft de wetgever de absolute vrijstelling ingevoerd voor het
inkomen van de eigen woning. Dit betekent concreet dat u niet langer het KI van de
eigen woning moet aangeven in uw belastingaangifte zelfs wanneer u nog oude
fiscale voordelen aanvraagt. Door deze absolute vrijstelling verdwijnt ook de vroegere
woningaftrek en de verrekening van de onroerende voorheffing. Dit laatste werd om­­
gevormd tot een gewestelijke belastingvermindering.

d. Aangifte KI buitenlandse woning

Als u eigenaar bent van een woning in het buitenland, dan zal u eveneens het kadastraal
inkomen moeten aangeven op dezelfde manier als een tweede woning in België. Uw
vakantiewoning of terrein in het buitenland zal ondertussen door de Administratie
Opmetingen en Waarderingen een KI hebben gekregen. Er wordt geen onderscheid
meer gemaakt tussen een in België gelegen onroerend goed of een in het buitenland
gelegen onroerend goed. Maar een uniforme bepaling van de belastbare grondslag (op
basis van het KI) betekent echter niet dat de buitenlandse onroerende inkomsten ook op
dezelfde wijze worden belast als de Belgische. De dubbelbelastingverdragen die België
met de meeste landen sloot, wijzen de heffingsbevoegdheid doorgaans toe aan het
land waar het onroerend goed gelegen is. België, het land waar de belastingplichtige
eigenaar van het buitenlands goed woont, moet dan het inkomen uit dat goed vrijstellen, maar er wel rekening mee houden voor de bepaling van het belastingtarief op de
andere Belgische inkomsten. De toepassing van deze ‘vrijstelling met progressievoorbehoud’ moet door u als eigenaar dan wel expliciet aangevraagd worden in de aangifte
(‘Inkomsten van buitenlandse oorsprong’ in vak III).

2. De beroepsinkomsten

Deze categorie bestaat uit volgende 7 soorten inkomsten:
1. bezoldigingen van werknemers;
2. bezoldigingen van bedrijfsleiders;
3. landbouw-, nijverheids- en handelswinsten;
4. baten van vrije beroepen;
5. winsten en baten in verband met een voorheen uitgeoefende beroepswerkzaamheid;
6. vervangingsinkomsten: pensioenen, brugpensioenen, werkloosheidsuitkeringen,
ziekte- en invaliditeitsvergoedingen, enz.;
7. auteursrechten.
20 • Belastinggids 2025

 In deze brochure beperken we ons tot de bespreking van de bezoldigingen van de werknemers en daarmee gepaard gaand de beroepskosten en de vervangingsinkomsten.

a. Bezoldigingen

De aan te geven inkomsten vindt u terug op de fiscale fiche 281.10 die de werkgever u
overhandigt om uw aangifte correct te kunnen invullen. De belangrijkste componenten
van deze bezoldiging zijn:
Het loon
Het belastbaar loon is uw brutoloon verminderd met de RSZ-bijdragen.
Als u geen fiscale fiche ontvangt, moet u toch uw beroepsinkomsten aangeven (vb. aan
de hand van uw loonfiches). Voor arbeiders uit de bouwsector bevat het bedrag van de
lonen (op de fiscale fiche) automatisch de getrouwheidszegels van 9%. De 2% weerverletzegels, worden aangegeven bij de vervangingsinkomsten (rubriek andere).
Het vakantiegeld
Voor arbeiders wordt dit nog steeds apart uitbetaald door een vakantiekas, voor bedienden zit dit bedrag begrepen in het geheel van de belastbare bezoldigingen.
Achterstallige lonen en opzegvergoedingen
Deze inkomsten worden afzonderlijk op de fiscale fiche meegegeven omdat zij afzonderlijk zullen belast worden (zie later).
Voordelen van alle aard
De aan te geven waarde van de voordelen van alle aard zijn meestal vervat in het geheel
van de belastbare bezoldigingen. Hieronder zijn begrepen o.a. kosteloze beschikking
over onroerende goederen, gebruik van een firmawagen, leningen tegen verminderde
rentevoet, enz.
Terugbetaling door de werkgever van het woon-werkverkeer
Wanneer uw werkgever tussenkomt in de verplaatsingskosten van uw woon-werkverkeer, is dit bedrag volledig of gedeeltelijk vrijgesteld van belasting.
Trekt u uw werkelijke beroepskosten af dan hebt u in geen geval recht op belastingvrijstelling van de tussenkomst.

Belastinggids 2025 • 21

 Indien u opteert voor de toepassing van de forfaitaire beroepskosten, is de terugbetaling
door de werkgever van de reiskosten voor het woon-werkverkeer als volgt vrijgesteld
van belasting:
a. U gebruikt het openbaar vervoer: de vergoeding van uw werkgever voor het gebruik
van het openbaar vervoer is volledig vrijgesteld.
b. U maakt gebruik van het gemeenschappelijk georganiseerd vervoer: de vergoeding
voor dergelijk georganiseerd vervoer is vrijgesteld van belastingen, en wel tot aan de
prijs van een treinabonnement 1ste klasse voor eenzelfde afstand.
c. U gebruikt de eigen auto of motor: u hebt recht op een belastingvrijstelling
van 490 euro.
d. U gebruikt een bedrijfswagen: ook als uw werkgever u kosteloos een bedrijfswagen
of -motor ter beschikking stelt, hebt u recht op een belastingvrijstelling van
maximaal 490 euro.
e. U gebruikt de fiets: er geldt een vrijstelling ten belope van € 0,35/km voor de werkelijk gedane verplaatsingen tussen uw woonplaats en de plaats van tewerkstelling.
Sinds inkomstenjaar 2024 bestaat er wel een drempel van 3 500 euro op jaarbasis.
Boven dit bedrag zijn er wél belastingen verschuldigd op het surplus. Daarnaast mag
u sinds 1 januari 2024 uw werkelijke beroepskosten niet bewijzen als u de fiscale
vrijstelling van de fietsvergoeding wil blijven genieten.
Het Grondwettelijk Hof vernietigde begin 2020 de mobiliteitsvergoeding, ook wel cash
for car geheten. Sinds aanslagjaar 2020 verscheen als alternatief het mobiliteitsbudget
(inwisseling van een bedrijfswagen in een mobiliteitsbudget). Bij een mobiliteitsbudget
zijn er 3 pijlers van mogelijke bestedingsopties (pijler 1 een milieuvriendelijke wagen,
pijler 2 alternatieve en duurzame transportmiddelen en pijler 3 het resterend deel mobiliteitsbudget). Ondertussen zijn er op dit vlak ook wel wat aanpassingen gebeurd. Merk
op dat het mobiliteitsbudget maximaal mag overeenstemmen met de jaarlijkse totale
brutokosten van de firmawagen.
Bij een combinatie mag u de verschillende vrijstellingen voor ieder vervoermiddel combineren. De specifieke bedragen telt u samen. Als uw werkgever geen aparte vergoeding
voor ieder vervoermiddel betaalt, maar wel een alles omvattende vergoeding, wordt
eerst de vrijstelling van 490 euro toegepast. Vervolgens komt de vrijstelling voor het
openbaar vervoer en ten slotte die voor het georganiseerd gemeenschappelijk vervoer.
Syndicale premie
Indien u een syndicale premie van de ACLVB hebt ontvangen dan moet u deze aangeven als inkomsten. In principe wordt een vakbondspremie tot de eigenlijke bezoldigingen van een werk­nemer gerekend. Deze worden aangeven in Vak IV – Rubriek 1.

22 • Belastinggids 2025

 Wedden, lonen enz. – b) die niet op de fiche zijn vermeld. Dit bedrag moet u dan
optellen met de andere bedragen van rubriek 1.

!  Opgelet! Indien u de syndicale premie ontvangen hebt in een periode dat u niet

werkte, wordt de premie anders belast. De vakbondspremie ontvangen tijdens een
periode van werkloosheid is bijvoorbeeld belastbaar als werkloosheidsuitkering
(vak IV – code 260); vakbondspremies ontvangen tijdens een periode van SWT
zijn als SWT belastbaar (code 281).

Daartegenover staat wel dat u uw lidgeld mag inbrengen als u de werkelijke beroepskost bewijst (zie hieronder b.2 Werkelijke beroepskosten). Bewijst u de werkelijke
beroepskosten niet, dan is het syndicale lidgeld begrepen in het kostenforfait en kan u
de bijdrage niet inbrengen bovenop het forfait.
Niet belastbare bezoldigingen, vergoedingen of voordelen
Er zijn een heleboel niet belastbare vergoedingen, voordelen of uitkeringen zoals maaltijd-, sport- en cultuurcheques, bezoldiging flexi-jobs, overuren horeca, sociale vergoedingen, morele schadevergoedingen enz.
Slechts enkele worden hieronder toegelicht.
Niet-recurrente resultaatsgebonden voordelen (de loonbonus)
Werkgevers kunnen aan al hun werknemers of een omschreven groep van werkne- mers
op een sociaal en fiscaal gunstige manier een bonus toekennen. De uitkering van de
loonbonus is afhankelijk van het bereiken van objectief meetbare en collectieve doelstellingen. De maximumbedragen worden elk jaar geïndexeerd. Voor het inkomsten­­­­­jaar
2024 (aj. 2025 kon aan de werknemers een belastingvrije loonbonus worden uitgekeerd
van bruto 4 020 euro (sociaal plafond). Dit bedrag is onderworpen aan 13,07% solidariteitsbijdrage zodat het maximaal bruto vrijgestelde bedrag 3 496 euro is.
Het ontvangen bedrag staat vermeld op de fiscale fiche en moet u overnemen in uw
aangifte. Is er meer ontvangen dan wordt u belast op het overschreden gedeelte.
Werkgeverstussenkomst m.b.t. PC-privé
De werkgeverstussenkomst in de aankoop van een PC-configuratie door een werknemer
met een bruto belastbare bezoldiging van maximaal 42 090 euro, is tot 1 070 euro
vrijgesteld van belasting. De ontvangen som moet op de aangifte vermeld worden, die
u vervolgens zelf opnieuw moet vrijstellen zodat u niet belast zou worden. Ook hier zal u
bij emigratie of immigratie het fiscale voordeel slechts genieten ‘pro rata temporis’
(= X/12den).

Belastinggids 2025 • 23

 Gewestelijke opleidingspremies
Sinds aanslagjaar 2020 geldt een nieuwe belastingvrijstelling ten voordele van bepaalde
opleidingspremies die de gewesten of de Duitstalige gemeenschap toekennen aan uitkeringsgerechtigde werklozen die een opleiding volgen met het oog op een tewerkstelling in een
knelpuntberoep. De vrijstelling is voor aanslagjaar 2025 beperkt tot 820 euro

b. Beroepskosten

Iedereen heeft recht op een vermindering van zijn beroepsinkomsten voor gemaakte
kosten. Eén van de maatregelen van de taxshift om het netto-inkomen van de werknemers te verhogen, is het optrekken van het wettelijk kostenforfait. U kunt uw werkelijk
gemaakte kosten in mindering brengen. Doet u dit niet, dan hebt u automatisch recht
op een forfaitaire aftrek. Deze forfaitaire aftrek zal ook door de fiscus worden toegepast
indien het voor u voordeliger is dan de inbreng van werkelijke kosten.

b.1 Forfaitaire aftrek beroepskosten werknemers
Voor inkomstenjaar 2024 (aj. 2025) wordt het kostenforfait berekend tegen een uniform tarief van 30% en het maximale bedrag stijgt naar 5 750 euro. De forfaitaire aftrek
van de beroepskosten wordt dus niet langer progressief berekend.

!  Opgelet! De forfaitaire beroepskosten worden ‘pro rata temporis’ toegepast bij
emigratie of immigratie.

Als de afstand tussen uw woonplaats en uw werk op 1 januari 2025 75 km of meer
bedroeg en u niet kiest voor aangifte van uw ‘werkelijke beroepskosten’, kunt u in uw
aangifte het bijkomende forfait vermelden dat voor u geldt. U moet wel een bijlage
toevoegen waarop u de plaats van uw werk op 1 januari 2025 vermeldt en de afstand
uitgedrukt in kilometer tussen die plaats en uw woonplaats.
Afstand tussen uw woonplaats en uw werk

Bijkomende forfait

van 75 km tot 100 km

75 euro

van 101 km tot 125 km

125 euro

meer dan 125 km

175 euro

24 • Belastinggids 2025

 b.2 Werkelijke beroepskosten
b.2.1 Kosten voor auto en motorvoertuigen
a. Woon-werkverkeer
In geval van vaste werkplaats
Wanneer u het woon-werkverkeer aflegt met uw eigen wagen, worden de kosten forfaitair bepaald. Financierings- en mobilofoonkosten zijn niet in dit forfait begrepen.
De kosten zelf moet u niet bewijzen, wel het effectief gebruik van de wagen en de afgelegde kilometers.
De totale kostprijs voor uw woon-werkverkeer berekent u volgens de formule:
0,15 euro × aantal kilometer per enkel traject × aantal trajecten per dag × aantal
gewerkte dagen. Let wel, vanaf 2026 zal dit beperkt worden voor bedrijfswagens met
een CO2-uitstoot.
Dit forfait is niet van toepassing wanneer u het woon-werkverkeer aflegt met een
motorfiets of met de wagen wanneer u geen vaste werkplaats heeft. Hiervoor geldt de
regeling omschreven in punt b hierna.
De fiscus begrijpt onder de vaste werkplaats doorgaans de plaats waar de aanwezigheid
van een werknemer tijdens het belastbaar tijdperk 40 dagen of meer bedraagt. Deze
40 dagen moeten niet noodzakelijk op elkaar volgen.
b. Andere beroepsverplaatsingen
De ‘vaste’ autokosten zijn in de personenbelasting aftrekbaar volgens het percentage
dat ook wordt toegepast in de vennootschapsbelasting en dus afhankelijk van de CO2uitstoot (uitgezonderd wagens die zijn aangekocht vóór 1 januari 2018 en die dus nog
steeds recht geven op de aftrek van minimum 75%).
De formule om het aftrekpercentage te bepalen is de volgende: 120% - (0,5% x coëfficiënt x aantal gram CO2 per kilometer) waarbij de coëfficiënt verschillend is naargelang
het gaat om een elektrische wagen, een wagen op diesel, benzine, aardgas, etc. Het
aldus berekende aftrekpercentage mag minimum 50% en maximum 100% bedragen
(volledig elektrische wagens zullen op vandaag de facto op een volledige (100%)
aftrekbaarheid uitkomen). Let wel, voor wagens op fossiele brandstof gekocht, gehuurd
of geleased vanaf 1 juli 2023 geldt reeds een degressief stelsel (uitdoofregeling) waarbij de ondergrens van 50% zal verdwijnen en de bovengrens van 100% zal afnemen
vanaf aanslagjaar 2026.
Kosten van financiering zijn 100% aftrekbaar. De aftrekbaarheid van de brandstofkosten
volgt het regime voor de ‘vaste’ autokosten. Voor oplaadbare hybride bedrijfswagens
Belastinggids 2025 • 25

 wordt de fiscale aftrekbaarheid van de benzine- of dieselkosten echter al sneller beperkt.
Voor een vanaf 1 januari 2023 aangekocht, geleased of gehuurd oplaadbaar hybride
voertuig, speelt hier meteen een bovengrens van 50%. Dit was althans wat voorzien
was in de Vivaldi-regering.
De Arizona-regering heeft andere plannen met de plug-in hybride. Voor deze wagens
zou het maximale aftrekpercentage van 75% behouden blijven tot eind 2027. Voor
plug-in hybrides met een uitstoot van maximaal 50 g/km waarvan het aftrekpercentage
volgens de gramformule hoger ligt dan 75%, zal dat hogere aftrekpercentage zelfs
tot eind 2027 toegepast mogen worden. In 2028 zou het maximale aftrekpercentage
dan dalen naar 65% en in 2029 naar 57,5% (gelijktijdig met de daling van elektrische
auto’s). In het regeerakkoord kan u lezen dat deze aftrekpercentages van toepassing
zijn voor de hele gebruiksduur van de wagen door dezelfde huurder/eigenaar. Concreet
betekent dit dat de autokosten van bijna alle plug-in hybrides nog tot eind 2027 voor
100% aftrekbaar zouden blijven.
Van deze kosten, die u moet bewijzen, moet u het beroepsgedeelte in aanmerking
nemen. M.a.w. u vermenigvuldigt deze kosten met de verhouding tussen enerzijds de
jaarlijks afgelegde kilometers voor het beroep (met uitzondering van de afgelegde kilometers tussen woonst en plaats van tewerkstelling) en anderzijds de in dat jaar totaal
afgelegde kilometers.
b.2.2 Andere vervoermiddelen woon-werkverkeer
De mogelijkheid om werkelijke kosten gemaakt voor woon-werkverkeer in te brengen, werd uitgebreid naar het gebruik van andere vervoermiddelen. Legt u het traject af anders dan met de
eigen wagen, bijvoorbeeld met het openbaar vervoer, mag u eveneens 0,15 euro per afgelegde
kilometer aanrekenen, maar slechts voor maximum 100 km per enkel traject.
Om het gebruik van de fiets (rijwiel of speed pedelec) naar het werk te stimuleren is er een
hogere belastingvrije kilometer­vergoeding voor woon-werkverplaatsing per fiets gelijk aan
0,35 euro per werkelijk afgelegde kilometer (aj. 2025). Vanaf 2024 is er ook een plafond op
jaarbasis per werknemer en per werkgever van maximaal 3 500 euro (inkomsten 2024).
Met andere vervoermiddelen wordt bedoeld alle andere mogelijkheden dan de wagen: te voet,
per fiets, trein, bus, brommer of motorfiets. Dit forfait van 0,15 euro per km met een maximum
van 100 km enkele reis geldt bij gebrek aan bewijs van eventuele hogere kosten. Als u m.a.w.
kan bewijzen dat de werkelijke kosten verbonden aan andere vervoermiddelen dan de auto
hoger liggen, kunnen deze hogere kosten worden ingebracht. Zo kunnen kosten i.v.m. de
motor­fiets of een treinbiljet 1ste klasse hiervoor in aanmerking komen. Voor de eigen wagen is
dit echter uitgesloten: hier is het maximum 0,15 euro per km voor heel het traject.

26 • Belastinggids 2025

 Ook carpoolers mogen van deze regeling gebruik maken. Rijdt u mee met een vriend of een
collega naar het werk, dan mag u de werkelijk betaalde vergoeding of een forfait van 0,15 euro
per kilometer (met een maximum van 100 km per traject) fiscaal inbrengen. Dat forfait kan u
eveneens inbrengen als u helemaal niets betaalt voor het carpoolen.
b.2.3 Diverse kosten
• huurprijs of intresten van de lening, onderhouds- en energiekosten voor het onroerend
goed dat voor uw beroep werd aangewend;
• kledij: alleen kosten van specifieke werkkledij;
• restaurantkosten ten belope van 69%;
• telefoonkosten, kantoorbenodigdheden, vakliteratuur, …;
• kosten vakbondswerk voor afgevaardigden.
Wist u dat uw jaarlijkse lidmaatschapsbijdrage voor de ACLVB eveneens aftrekbaar is
als beroepskost?
Als u werkloos bent mag u het bedrag dat u betaalde rechtstreeks aftrekken van de
werkloosheidsuitkeringen, bent u met SWT dan mag u het betaalde lidgeld rechtstreeks
aftrekken van uw SWT. Dit bedrag staat ook vermeld op de fiscale fiche die u van uw
vakbond ontvangt.
Loontrekkenden kunnen hun werkelijke beroepskosten (waaronder hun jaarlijks lidgeld
aan de vakbond) aangeven in hun belastingaangifte.
Kiest u voor het wettelijk kostenforfait, dan is de vakbondsbijdrage begrepen in dat
kostenforfait en kan u die bijdrage niet inbrengen bovenop het kostenforfait.

c. Vervangingsinkomsten

Dit zijn o.a.:
• ouderdoms-, rust- en overlevingspensioenen;
• werkloosheidsvergoedingen;
• ziekte- en invaliditeitsvergoedingen;
• stelsel van werkloosheid met bedrijfstoeslag (SWT).
Voor deze vervangingsinkomsten wordt een belastingvermindering toegekend.
Er worden wel geen beroepskosten in mindering gebracht.
De uitbetalingsinstelling zal een fiscale fiche bezorgen met de aan te geven inkomsten
erop vermeld. Werklozen en SWT’ers mogen van het aan te geven bedrag aan werkloosheidsuitkeringen de betaalde vakbondsbijdragen in mindering brengen.

Belastinggids 2025 • 27

 3. De diverse inkomsten

Deze omvatten een aantal componenten die niet onder de drie vorige inkomstencategorieën kunnen worden ondergebracht, o.a.:
• inkomsten uit onderverhuring of overdracht van huur van onroerende goederen;
• ontvangen bedragen uit de verhuring van jacht-, vis- en vogelvangstrechten;
• winsten of baten betaald uit toevallige prestaties, speculaties of diensten (m.a.w. deze
die behaald zijn buiten de beroepswerkzaamheid);
• ontvangen onderhoudsuitkeringen;
•…

4. Roerende inkomsten

Het algemene tarief van de roerende voorheffing (RV) is 30%.
Daarop worden nog enkele uitzonderingen gemaakt zoals:
• inkomsten uit ‘gewone spaardeposito’s’: 15% (de eerste schijf van 1 020 euro is
vrijgesteld);
• dividenden VVPR: 20% of 15%;
• inkomsten uit auteursrechten: 15% tot aan de eerste schijf van 73 070 euro
(Opgelet! Met ingang van 1 januari 2023 – voor inkomsten uit auteursrechten die
vanaf die datum toegekend of betaald worden – werd een nieuwe regeling ingevoerd.
Aangezien de nieuwe regeling veel strikter is, werd er voorzien in een overgangsmaatregel die ondertussen ook is verstreken).
Naast de 30% en 15%, bestaat er ook nog een RV van 5%. Het 17% tarief voor roerende inkomsten is vorig aanslagjaar afgeschaft.
In de mate waarin de RV op regelmatige wijze is ingehouden, moeten de normale
inkomsten niet meer worden aangegeven in de personenbelasting. Een belangrijke
uitzondering zijn de auteursrechten: zelfs als er RV wordt ingehouden moeten de inkomsten nog vermeld worden in de aangifte.

5. Verenigingswerk en deeleconomie

Wie in zijn vrije tijd tegen betaling bijkluste, kon tot eind 2020 onder bepaalde voorwaarden tot een bepaald bedrag per jaar verdienen zonder dat men daarop belastingen
of sociale bijdragen moest betalen. Door een uitspraak van het Grondwettelijk Hof is dit
niet langer mogelijk.
Voor occasionele diensten van burger aan burger zal u sinds1 januari 2021 niet langer
kunnen genieten van deze vrijstelling want deze activiteiten worden voortaan belast als
diverse inkomsten, aan 33% dus.

28 • Belastinggids 2025

 Ook het verenigingswerk valt niet langer onder de vrijstelling maar kent nu een
aangepaste regeling, en dan nog voor een beperkte lijst van activiteiten uit de
sport- en culturele sector.
Deze activiteiten zullen belast worden aan 20% na aftrek van 50% forfaitaire
kosten m.a.w. belast aan 10%. U dient wel rekening te houden met een jaarlijks
plafond van van 7 460 euro.
De inkomsten uit de deeleconomie door tussenkomst van een erkend platform,
die sinds 1 januari 2021 worden betaald of toegekend, zijn opnieuw belastbaar tegen het tarief van 20% na aftrek van 50% forfaitaire kosten (ook hier
dus 10%). Het vroegere belastingvrij stelsel werd ook hier omgevormd tot een
stelsel van afzonderlijke belastingheffing. Ook hier geldt een maximumbedrag
per jaar van 7 460 euro (incl. inkomsten uit verenigingswerk).

Belastinggids 2025 • 29

 30 • Brochure A5

## IV Berekening van de belasting
De zesde staatshervorming heeft de belastingberekening grondig door elkaar geschud
en dit sinds enkele aanslagjaren. Een overzicht.

1. Financiering, autonomiefactor en opcentiemen

Vóór de zesde staatshervorming kregen de gewesten een jaarlijkse dotatie van de
federale overheid. Sinds aanslagjaar 2015 is deze dotatie omgezet in een gewestelijke
personenbelasting. De gewesten heffen opcentiemen op de personenbelasting.
Schematisch: gewesten vóór en na de zesde staatshervorming
Vóór de zesde staatshervorming
• Dotaties vanuit de PB (= ± 26% PB)
• Successie- en registratierechten
• Onroerende voorheffing
• Verkeersbelasting, BIV, eurovignet
• Eigen niet-fiscale ontvangsten
(legaten, schenkingen)

Na de zesde staatshervorming
• Opcentiemen op ‘gereduceerde personen­
belasting staat’ (van ± 26% PB voor de
aanslagjaren 2015, 2016 en 2017 naar
24,957% sinds aanslagjaar 2018)
• Dotaties i.v.m. nieuwe bevoegdheden
• Successie- en registratierechten
• Onroerende voorheffing
• Verkeersbelasting, BIV, eurovignet
• Eigen niet-fiscale ontvangsten
(legaten, schenkingen)

Ook voor aanslagjaar 2025 blijft men de personenbelasting berekenen aan de hand van
de federale inkomensschaal met belastingtarieven die naargelang het inkomen oplopen
van 25% tot 50%, d.i. de ‘personenbelasting staat’ (zie verder). De gewesten hebben
dus geen eigen inkomensschaal met eigen tarieven.
De ‘personenbelasting staat’ wordt nadien gereduceerd met de zogenaamde ‘autonomiefactor’, ook voor aanslagjaar 2025 vastgelegd op 24,957%. De autonomiefactor
bepaalt het toegekende aandeel in de personenbelasting aan de gewesten.
Op die gereduceerde basis heffen de gewesten opcentiemen. De Bijzondere
Financieringswet bepaalde het % van de opcentiemen op 35,117% (tot en met
aanslagjaar 2017). Sinds aanslagjaar 2018 bedraagt dit voor Vlaanderen en Wallonië
33,257% en voor Brussel 32,591%.

Belastinggids 2025 • 31

 2. Berekeningsgrondslag

Zoals hoger vermeld is de grondslag van de berekening van de opcentiemen de ‘gereduceerde belasting staat’ (= belasting staat − autonomiefactor).
De federale basisbelasting is de belasting, na toepassing van de federale belastingtarieven op de inkomsten (zie verder) maar vóór toepassing van:
• de belastingvermindering voor gezinslasten (= toekenning belastingvrije sommen en
toe­slagen personen ten laste);
• de belastingvermindering voor pensioenen en vervangingsinkomsten;
• de belastingvermindering voor buitenlandse inkomsten.
Bovenstaande belastingverminderingen worden toegekend vóór de bepaling ‘belasting
staat’. De federale overheid blijft bevoegd voor deze belastingverminderingen.
Alle andere belastingverminderingen worden nadien aangerekend: de federale
belastingverminderingen op de ‘gereduceerde belasting staat’ en de (oude en nieuwe)
gewestelijke belastingverminderingen op de gewestelijke opcentiemen.
Algemeen schema – Federale en gewestelijke personenbelasting1
Samenstelling van het belastbaar inkomen
+ netto onroerend inkomen
+ netto inkomen uit roerende goederen en kapitalen
+ netto beroepsinkomen
+ netto divers inkomen
− aftrek van het netto inkomen: onderhoudsgelden
= belastbaar inkomen (gezamenlijk BI + afzonderlijk BI)
Berekening van de belasting
belasting op de afzonderlijk
belaste inkomsten

− basisbelasting volgens
tariefschaal op GBI
− belasting op de belastingvrije som
= om te slane belasting
− vermindering voor pensioenen en vervangings­
inkomsten
− vermindering voor inkomsten uit het buitenland
= hoofdsom

1 Dit schema is opgenomen in bijlage 1 van de circulaire AAFisc 29/2014 (Ci.RH.331/633.424) van 7 juli 2014 die de invoering van de
gewestelijke aanvullende belasting op de personenbelasting toelicht.

32 • Belastinggids 2025

 samenvoeging van de belasting op de afzonderlijk belaste inkomsten en de hoofdsom op de gezamenlijk belaste inkomsten
belasting op intresten, dividenden, royalty’s, loten van effecten
van leningen en als diverse
inkomsten belaste meerwaarden op effecten en waarden

= belasting op de andere
inkomsten
= belasting Staat
− (belasting Staat ×
autonomiefactor)
= gereduceerde belasting
Staat

− andere federale belastingverminderingen

+ gewestelijke opcentiemen op ­gereduceerde
belasting Staat
+ gewestelijke
belastingvermeer­
deringen
− gewestelijke kortingen
− gewestelijke belastingverminderingen

saldo
indien = 0 eventueel nog te verminderen met het niet verrekende deel van federale belastingverminderingen dat kan worden
aangerekend op het positieve saldo van het gewest.

saldo
indien = 0 eventueel nog
te vermin­deren met het
niet verrekende deel van
gewestelijke kortingen en
belastingverminderingen
dat kan worden aangerekend op het positieve
saldo van federaal.

= federale personenbelasting (kan negatief zijn)

= gewestelijke personenbelasting
(kan negatief zijn)

= totale belasting (kan nooit negatief zijn)
+ federale belastingvermeerderingen
− federale verrekenbare niet terugbetaalbare bestanddelen
− federale en gewestelijke terugbetaalbare belastingkredieten
− federale verrekenbare en terugbetaalbare bestanddelen
+ opcentiemen gemeente en agglomeratie op de ‘totale belasting’
= verschuldigde of terug te storten belasting

3. Roerende inkomsten

De Bijzondere Financieringswet maakt een uitzondering voor de meeste roerende
inkomsten. De belasting erop wordt niet gereduceerd met de autonomiefactor van
24,957%. Ook de gewesten kunnen geen opcentiemen heffen op de belasting op die

Belastinggids 2025 • 33

 roerende inkomsten zoals dividenden, intresten enzovoort. Deze belasting blijft dus
federaal (via de roerende voorheffing).

4. Fiscale woonplaats

Welk gewest is bevoegd of anders gezegd waar betaalt u de gewestelijke opcentiemen
en kan u genieten van gewestelijke fiscale voordelen en belastingverminderingen.
Bevoegd is het gewest waar u uw fiscale woonplaats heeft op 1 januari van het
aanslagjaar.
De fiscale woonplaats is de plaats waar de belastingplichtige feitelijk woont, en die valt
niet altijd samen met het adres waar u gedomicilieerd bent. Bij gehuwden en wettelijk
samenwonenden is dat de plaats waar het gezin is gevestigd. Bij een feitelijke scheiding, én geen verblijf meer in hetzelfde gewest, neemt men als criterium de laatste
gezamenlijke verblijfplaats.

5. De belasting

De belasting wordt berekend zowel op het belastbaar netto-inkomen als op de belastingvrije sommen. Voor gehuwden zal deze berekening voor elk afzonderlijk gebeuren.
Achteraf worden beide bedragen samengeteld zodat men de uiteindelijke gezinsbelasting verkrijgt. Personen ten laste komen bij de echtgenoot met het hoogste beroepsinkomen. De belasting wordt berekend op een progressieve wijze.
Dit betekent dat het percentage aan verschuldigde belasting stijgt naargelang uw
inkomen stijgt. De schijf van 30% is al enkele jaren geleden afgeschaft, zodat een
groter deel van het inkomen belast wordt aan een lager tarief, en de schijf van 40% is
verbreed. De laatste uitrol van de taxshift-wet resulteerde in een verdere verbreding van
de belastingschijven.
Voor het aanslagjaar 2025 bedragen de tarieven:
Belastbaar inkomen (schijven)

Belasting

van

tot

0 euro

15 820 euro

25%

15 820 euro

27 920 euro

40%

27 920 euro

48 320 euro

45%

boven

48 320 euro

50%

34 • Belastinggids 2025

 6. Belastingvrije som

Nadat eerst de brutobelasting werd berekend op het nettobelastbaar inkomen, wordt
vervolgens een eerste (laagste belaste) schijf van het nettobelastbaar inkomen opnieuw
vrijgesteld van belasting d.i. de belastingvrije som.

!  Opgelet! Iedere belastingplichtige heeft ongeacht de hoogte van het inkomen,

recht op eenzelfde belastingvrije som. Voor aanslag- jaar 2025 is dit 10 570 euro.

Ook hier zal de belastingvrije som ‘pro rata temporis’ worden toegepast ingeval van emigratie of immigratie. Dit belastingvrij inkomen wordt verhoogd naargelang het aantal
personen ten laste.
Kinderen ten laste

Verhoging belastingvrij inkomen

1 kind

1 920 euro

2 kinderen

4 950 euro

3 kinderen

11 090 euro

4 kinderen

17 940 euro

supplement per kind boven het vierde

6 850 euro

Bovendien worden deze bedragen met 720 euro verhoogd voor elk kind van minder
dan 3 jaar voor wie geen kosten voor kinderoppas zijn aangegeven. Gehandicapte
kinderen worden voor twee kinderen ten laste geteld. Bij co-ouderschap na feitelijke
scheiding of echtscheiding kan de verhoging van het belastingvrij inkomen verdeeld
worden over beide ouders.
Andere personen ten laste

Verhoging
belastingvrij inkomen

iedere andere persoon ten laste

1 920 euro

alleenstaande ouder met één of meer kinderen ten laste
of in co-ouderschap

1 920 euro

gehandicapte belastingplichtige

1 920 euro

Inkomstenjaar huwelijk én echtgenoot geen netto inkomsten
van meer dan 3 980 euro het jaar van het huwelijk

1 920 euro

(groot)ouder, broer of zus ouder dan 65 jaar

3 850 euro

zorgbehoevende (groot)ouder, broer of zus ouder dan 65 jaar

5 770 euro

Belastinggids 2025 • 35

 nieuw! De toeslag van 3 850 euro voor (groot)ouder, broer of zus ouder dan 65 jaar
geldt enkel nog voor de aanslagjaren 2022 t.e.m. 2025 indien deze persoon ten laste
reeds voor het aanslagjaar 2021 voor deze toeslag in aanmerking kwam. Is dat niet het
geval dan zal hij of zij (sinds aanslagjaar 2022) slechts in aanmerking komen voor de
lagere toeslag voor andere personen ten laste (1 920 euro) tenzij betrokkene ‘hulpbehoevend’ is. Zorgbehoevend betekent een verminderde zelfredzaamheid van minstens
9 punten. Dit wil bijvoorbeeld zeggen dat de persoon niet voor zichzelf kan zorgen, niet
zonder hulp kan eten of koken of dat hij of zij zich niet zonder hulp van anderen kan
verplaatsen. Het fiscaal voordeel is flink verhoogd. Voor aanslagjaar 2025 betekent dit
een toeslag op de belastingvrije som van 5 770 euro. Anderzijds wordt de zorgbe- hoevende persoon die gehandicapt is, niet langer voor 2 gerekend (zoals wel het geval is bij
kinderen of ‘andere personen’ ten laste).
Sinds aanslagjaar 2018 heeft een alleenstaande ouder met een laag inkomen en met
een kind of kinderen ten laste, bovenop de reeds bestaande bijkomende belastingvrije
som voor alleenstaande ouder (1 920 euro), recht op een ‘extra’ bijkomende belastingvrije som van maximaal 1 250 euro (aanslagjaar 2025).
Om de volledige som te kunnen genieten mag het belastbaar inkomen in dit aanslagjaar
niet hoger zijn dan 18 660 euro. Is het inkomen hoger dan wordt de ‘extra’ bijkomende
belastingvrije som afgebouwd tot 0 euro bij een inkomen van 23 650 euro. Er moet wel
sprake zijn van een netto-belastbaar beroepsinkomen van minimaal 3 980 (aanslagjaar 2025) om in aanmerking te komen voor deze ‘extra’ bijkomende belastingvrije som.
Noteer eveneens dat de bijkomende belastingvrije sommen normaliter bij de echtgenoot met het hoogste inkomen worden aangerekend. Indien het hoogste inkomen een
buitenlands inkomen was, gaf dit in het verleden problemen. Als gevolg van rechtspraak
van het Europees Hof en het Belgisch Grondwettelijk Hof moeten de bijkomende belastingvrije sommen toegekend worden aan de ouder met het Belgisch inkomen, zo niet
is er sprake van belemmering van het vrij verkeer van werknemers en discriminatie met
feitelijk samenwonenden.

7. Uitsluitende bevoegdheden van de federale staat

Enkel de federale staat is bevoegd voor de bepaling van het netto belastbaar inkomen.
De vaststelling en de berekening van het netto belastbaar onroerend inkomen, het
roerend inkomen, het beroepsinkomen, diverse inkomsten blijft na de zesde staats­
hervorming een federale bevoegdheid. Van het ‘globaal belastbaar inkomen’ kunnen in
tegenstelling tot vroeger nog enkel de onderhoudsuitkeringen worden afgetrokken (zie
verder IV, 9.1). Verder is de federale overheid bevoegd voor:
• het tarief van de personenbelasting (zie IV, 5);
36 • Belastinggids 2025

 • het opstellen van de belastingaangifte;
• de inning en invordering van de personenbelasting;
• de fiscale procedure (bezwaar, ontheffing van ambtswege, …);
• de roerende voorheffing en bedrijfsvoorheffing.
Voor de inkomstenjaren 2020 – 2023 (aanslagjaren 2021 – 2024) werd de indexering
van een aantal federale fiscale uitgaven bevroren op het niveau van 2019 (aj. 2020).
Dit gaat o.a. over de vrijgestelde eerste schijf van dividenden, de fiscale korf lange­
termijnsparen, de belastingvermindering voor giften, adoptiekosten en rechtsbijstandsverzekeringen. De grensbedragen m.b.t. pensioensparen zijn pas sinds aanslagjaar
2022 bevroren. De grensbedragen in het kader van de belastingvermindering voor
pensioenen en vervangingsinkomsten worden niet bevroren. Vanaf dit aanslagjaar
worden de federale fiscale uitgaven opnieuw geïndexeerd.
Voor volgende uitgaven is de federale overheid bevoegd en kent zij de belasting­vermin­
deringen en belastingkredieten toe (voor een verdere bespreking zie IV, 9.2):
• Belastingvermindering langetermijnsparen (indien levensverzekering, niet gekoppeld
aan krediet ‘eigen woning’, kapitaalaflossingen krediet niet-eigen woning, pensioensparen en werkgeversaandelen, werknemersbijdrage groepsverzekering);
• Belastingvermindering voor giften;
• Belastingvermindering uitgaven kinderoppas;
• Belastingvermindering intresten ‘groene’ lening;
• Belastingvermindering voor huisbediende;
• Belastingvermindering voor uitgaven voor een ontwikkelingsfonds;
• Belastingvermindering voor elektrische voertuigen;
• Belastingvermindering voor adoptiekosten;
• Belastingvermindering voor overwerk dat recht geeft op overwerktoeslag;
• Belastingvermindering verwerving aandelen van een startende KMO;
• Belastingvermindering van aandelen van een groeibedrijf;
• Belastingvermindering voor premies rechtsbijstandsverzekering;
• Belastingvermindering voor de opbouw van het extra pensioenkapitaal
voor werknemers (VAPW);
• Belastingvermindering op pensioenen en vervangingsinkomsten;
• Belastingvermindering op inkomsten uit het buitenland;
• Belastingvermindering op dividenden;
• Belastingvermindering voor laadstations;
• Belastingkrediet lage activiteitsinkomsten en belastingkrediet lage lonen
(‘pro rata temporis’ bij emigratie of immigratie);
• Belastingkrediet werkbonus (‘pro rata temporis’ bij emigratie of immigratie);
• Belastingkrediet kinderen ten laste;
Belastinggids 2025 • 37

 8. Uitsluitende bevoegdheden van de gewesten

Er zijn ook specifieke belastingverminderingen en -kredieten die gewestelijk zijn (voor
een verdere bespreking zie IV, 9.2). In Vlaanderen is er momenteel nog een belastingkrediet win-winlening en de Vlaamse renovatieovereenkomst (‘mama-papa­lening’).
De Waalse Regering kent de ‘Coup de Pouce’, de Waalse tegenhanger van de Vlaamse
win-winlening. En dan is er nog het belastingkrediet Brusselse Proxi-lening.
Hieronder vindt u een overzicht van de gewestelijke belastingverminderingen:
• Krediet en levensverzekering ‘eigen woning’
• Onderhoud en restauratie van beschermde monumenten en landschappen
(in Brussel afgeschaft);
• PWA-cheques, wijk-werkcheques en dienstencheques;
• Energiebesparende uitgaven (dakisolatie; nog enkel in Wallonië);
• Vernieuwing woning verhuurd via een sociaal verhuurkantoor
(voor uitgaven vanaf 2018, nog enkel van toepassing in Wallonië);
• Win-winlening (Vlaanderen);
• Coup de Pouce-lening (Wallonië);
• Proxi-lening (Brussel);
• De Vlaamse renovatieovereenkomst;
• Vernieuwing van woningen gelegen in een zone voor positief grootstedelijk beleid.

9. Overzicht fiscale voordelen

Er bestaan drie soorten fiscale voordelen:
• aftrekbare bestedingen
• belastingverminderingen
• belastingkredieten
Sinds aanslagjaar 2018 zal bij emigratie of immigratie volgende fiscale voordelen nog
slechts ‘pro rata temporis’ worden aangerekend. De beperking heeft o.a. betrekking op:
• het plafond van het huwelijkquotiënt (zie II, 2, a);
• de belastingvrije sommen (zie IV, 6);
• toegelaten bestaansmiddelen voor personen ten laste (zie II, 3);
• schijven en plafond m.b.t. de forfaitaire beroepskosten (zie III, 2, b);
• werkgeverstussenkomst in PC-privé (zie hierna);
• vrijgestelde overuren in de horeca (zie hierna);
• fiscale vrijstelling intresten spaarrekening (zie III, 4);
• bedragen die recht geven op de federale belastingvermindering langetermijn- en
pensioen­sparen en werkgeversaandelen (zie hierna);
•…

38 • Belastinggids 2025

 De proratering zal gebeuren op maandbasis, met inbegrip van de maand waarvan de
vijftiende dag tot het belastbaar tijdperk behoort. Voorbeeld: belastbaar tijdperk van
1 januari t.e.m. 20 september (datum van vertrek) geeft 9/12de als beperkingsbreuk.

9.1 Aftrekbare bestedingen

Vroeger kon u van het totaal netto belastbaar inkomen allerlei soorten van bestedingen
aftrekken. U moest deze telkens wel zelf in uw aangifte opnemen. De fiscus paste deze
niet automatisch toe. Sinds het aanslagjaar 2015 kunnen van het totaal netto inkomen
enkel nog maar onderhoudsgelden worden afgetrokken. Dit heeft ook tot gevolg dat de
vroegere aftrekbare bestedingen (bijvoorbeeld aftrek enige woning en de bijkomende
intrestaftrek) omgevormd worden tot belastingverminderingen (zie verder, IV, 10).
Onderhoudsuitkeringen
Onderhoudsuitkeringen die u in 2024 betaalde, zijn aftrekbaar indien aan volgende
voorwaarden is voldaan:
• Het onderhoudsgeld wordt betaald op grond van een wettelijke onderhoudsplicht
(volgens het Burgerlijk en het Gerechtelijk Wetboek bestaat er een onderhoudsplicht
tussen ouders/kinderen en tussen echtgenoten onderling; tussen broers en zussen
bestaat de plicht niet);
• De begunstigde maakt geen deel uit van uw gezin;
• Men moet kunnen bewijzen dat de uitkering regelmatig betaald wordt.
Het aftrekbaar bedrag is beperkt tot 80% van de betaalde onderhoudsuitkeringen
(u geeft in uw belastingaangifte wél het totale bedrag aan).

9.2 Belastingverminderingen

De zesde staatshervorming droeg de bevoegdheid voor de belastingvermindering voor
bepaalde uitgaven over aan de gewesten, andere uitgaven bleven federaal.
Het komt er op neer dat een aantal bestaande federale belastingverminderingen
werden overgeheveld naar de gewesten. Dat houdt bijgevolg in dat de gewesten zelf
instaan voor de financiering van deze nieuwe gewestverminderingen.
Ondertussen zijn er al een aantal federale en gewestelijke belastingverminderingen
bijgekomen maar ook enkele werden geschrapt.
De federale belastingverminderingen worden aangerekend op de gereduceerde
belasting staat verhoogd met de belasting op de intresten, dividenden, royalty’s, loten
van effecten van leningen en meerwaarden op roerende waarden en titels. De gewestelijke belastingverminderingen en kortingen worden aangerekend op de gewestelijke
opcentiemen en belastingvermeerderingen. In tegenstelling tot de federale belastingverminderingen, zullen de gewestelijke verminderingen ook worden aangerekend op de
Belastinggids 2025 • 39

 opcentiemen met betrekking tot de afzonderlijk belaste inkomsten (zie model uitgebreide opcentiemen, IV, 2).
Het totaal van de gewestelijke belastingverminderingen, kan hoger zijn dan de som
van de gewestelijke opcentiemen en belastingenvermeerderingen verminderd met de
gewestelijke kortingen.
Het gewest kan in dit geval beslissen het overschot te verrekenen met de federale
personenbelasting. De Vlaamse regering heeft reeds beslist dit mechanisme toe te passen, behalve dan voor de PWA- en dienstencheques. Omgekeerd kan ook de federale
overheid voor elke belastingvermindering beslissen dat een overschot van een federale belastingvermindering kan verrekend worden met het saldo van de gewestelijke
personenbelasting.
Hierna volgt een bespreking van de voornaamste gewestelijke en federale belastingverminderingen. Gezien het belang van de woonfiscaliteit, zullen deze belastingverminderingen in een apart onderdeel worden besproken (zie verder IV, 10).
a. Federale belastingverminderingen
a.1 Niet-eigen woning
Zie apart onderdeel woonfiscaliteit (IV, 10).
De ‘niet-eigen woning’ is in principe de woning die u als belastingplichtige niet zelf
betrekt.
a.2 Giften
Giften van minstens 40 euro aan erkende instellingen worden met een belastingvoordeel gestimuleerd. Er wordt een belastingvermindering toegekend ten belope van 45%
van het werkelijk betaalde bedrag. Sinds 2019 zijn ook onlinegiften aftrekbaar. Het
totale bedrag van de giften waarvoor de belastingvermindering verleend wordt, mag
niet meer bedragen dan 10% van het totale netto gezamenlijk belastbaar inkomen, met
een absoluut maximum van 408 130 euro (aanslagjaar 2025). Giften die aan buitenlandse instellingen worden gedaan moeten niet langer voldoen aan de attest-verplichting. De afschaffing van het attest- dat overigens niet geldt voor giften aan binnenlandse
instellingen - wordt vervangen door een bewijs dat door de schenker ter beschikking
gehouden wordt van de administratie dat de gift effectief werd betaald.
a.3 Kosten voor uitgaven voor kinderoppas
De uitgaven moeten betaald zijn aan een instelling die erkend is door of onder toezicht
staat van ‘Kind & Gezin’, ‘l’Office de la Naissance et de l’enfance’ en de Executieve van
de Duitstalige Gemeenschap, die u een fiscaal attest aflevert (ook kosten voor voor- en
40 • Belastinggids 2025

 naschoolse opvang). Voor de uitgaven voor kinderopvang heeft u recht op een belastingvermindering. U mag voor 2024 (aanslagjaar 2025) maximaal 16,40 euro per
opvangdag en per kind jonger dan 14 jaar (of jonger dan 21 jaar bij een zware handicap) inbrengen als uitgaven.
Het tarief van de belastingvermindering bedraagt 45%. Voor alleenstaande ouders
(werkelijk alleenstaanden, minimum netto-beroepsinkomen en maximum gezamenlijk
belastbaar beroepsinkomen) kan de belastingvermindering verhoogd worden van 45%
naar 75% en wordt enkel toegepast als u een netto belastbaar inkomen heeft van minimaal 3 980 euro en maximaal 23 650 euro (aanslagjaar 2025).
De belastingvermindering ‘uitgaven voor kinderoppas’ is niet te combineren met het
fiscale voordeel van de bijkomende belastingvrije som van 720 euro (aanslagjaar
2025) voor kinderen jonger dan 3 jaar. De onverenigbaarheid geldt per kind en niet
per gezin. De keuze voor de ene of andere maatregel (belastingvermindering kinderoppas of verhoging van de belastingvrije som voor kinderen jonger dan 3 jaar) komt
toe aan de belastingplichtige. De keuze gebeurt m.a.w. per kind in de aangifte en is niet
onherroepelijk.
a.4 Bezoldigingen van een huisbediende
Hoewel u het volledige bedrag moet aangeven, geeft slecht 50% van de uitgave, met
voor 2024 bovendien een maximum van 8 160 euro, recht op een belastingvermindering van 30%. De bezoldiging (met inbegrip van de sociale bijdragen) die u in 2024 aan
een huisbediende hebt betaald, moet minimaal 4 770 euro bedragen.
a.5 Langetermijnsparen
Deze belastingvermindering wordt berekend tegen een vast percentage van 30%.
Tot de belastingverminderingen voor het langetermijnsparen behoren:
• de bijdragen voor aanvullend pensioen. Dit bedrag moet u vermelden in de aangifte.
De werkgever houdt wel reeds maandelijks rekening met een belastingvermindering
van 30% van de premie die hij verrekent met de bedrijfsvoorheffing op het loon.
De correcte vermindering gebeurt dan in uw belastingaangifte.
• de individuele levensverzekeringspremies (wanneer de levensverzekering niet dient
tot het waarborgen of weder samenstellen van een lening met betrekking tot een
woning). Het bedrag van de premie dat in aanmerking komt voor de berekening van
de vermindering is:
→ 15% van de eerste schijf van de netto beroepsinkomsten van 2 040 euro
(= 306 euro) + 6% van de rest van de netto beroepsinkomsten.
Belastinggids 2025 • 41

 Per echtgenoot of wettelijk samenwonende partner is dat bedrag maximaal 2 450 euro
voor premies individuele levensverzekeringen en kapitaalaflossingen samen.
• verwerving van werkgeversaandelen
Het maximaal aftrekbaar bedrag van aandelen die u van uw werkgever koopt, is
vastgesteld op 820 euro per belastbaar tijdperk en per belastingplichtige. Het fiscaal
voordeel is niet cumuleerbaar met het fiscaal voordeel verbonden aan het pensioensparen. Om het fiscaal voordeel definitief te verwerven moeten de aandelen 5 jaar in
uw bezit zijn (de overdracht binnen de 5 jaar na het ­verwerven van de aandelen wordt
gesanctioneerd met een terugname van de belastingvermindering onder de vorm van
een federale belastingvermeerdering).
De belastingvermindering bedraagt 30% van het in aanmerking te nemen bedrag.
• betalingen voor het pensioensparen, inclusief premiebetalingen voor een pensioenspaarverzekeringscontract dat dient voor het waarborgen of weder samenstellen van
een lening voor het verwerven of behouden van een woning die de eigen woning is
van de belastingplichtige.
Voor het pensioensparen mag per belastingplichtige per jaar maximaal 1 020 euro
worden gestort met een belastingvermindering van 30% of 1 310 euro met 25%
belastingvermindering. Zoals eerder vermeld, kan de vermindering niet samengaan
met de vermindering van aankoop van aandelen van de eigen werkgever.
• vrij aanvullend pensioen voor werknemers (VAPW). De werknemer kan een contract
VAPW afsluiten bij een verzekeraar of instelling voor bedrijfspensioenen naar eigen
keuze. Binnen bepaalde grenzen kiest u als werknemer zelf vrij hoeveel u voor uw aanvullend pensioen wil storten. De maximale bijdrage is gelijk aan 3% van het referentieloon, met een minimum van 1 910 euro.
a.6 Intresten van groene leningen
Groene leningen kunnen niet meer afgesloten worden, doch de intrestbepalingen van
de eerder afgesloten leningen geven bij voortduren aanleiding tot een intrestbonifi­catie
(een korting van 1,5%) en een belastingvermindering. Net zoals de uitdovende vermindering voor energiebesparende uitgaven, is deze vermindering federaal. De belastingvermindering bedraagt 30%.
a.7 Elektrische twee-, drie- of vierwieler
Als u in 2024 een elektrisch voertuig hebt gekocht, kunt u op een belastingvermindering rekenen. Het moet gaan om een elektrisch voertuig in nieuwe staat: d.i. een motorfiets, driewieler of vierwieler die uitsluitend elektrisch aangedreven wordt. De aankoop
van een elektrische personenwagen, een elektrische auto voor dubbel gebruik of een
42 • Belastinggids 2025

 elektrische minibus levert geen belastingvermindering meer op. De vermindering geldt
per aangekocht voertuig en bedraagt 15% van de aankoopprijs met met een maximum
van 5 350 euro voor een vierwieler en 3 270 euro voor de andere vervoermiddelen
(motorfiets of driewieler). Wanneer deze aankoop zich echter situeert binnen pijler 2
van het federale mobiliteitsbudget, heeft u geen recht op deze belastingvermindering.
Dit cumulverbod geldt sinds 1 januari 2022.
a.8 Bezoldiging voor overwerk
Er bestaat een fiscaal gunstregime voor overuren met overurentoeslag dat normaal
gezien beperkt is tot 130 overuren per jaar en per werknemer. Het maximum van
130 uren wordt verhoogd voor overwerk in de horeca (tot 360 uren) en bij werkgevers die werken in onroerende staat verrichten en gebruik maken van een elektronisch
aanwezigheidsregister (tot 180 uren). Als tegenhanger geniet de werkgever van een
vrijstelling van doorstorten van bedrijfsvoorheffing.
De belastingvermindering wordt dus in principe toegekend voor de eerste 130 overuren. Voor de periode van 1 juli 2021 tot en met 30 juni 2025 wordt het maximum
verhoogd tot 180 uren overwerk. Sinds 1 juni 2024 wordt het maximale aantal uren
dat recht geeft op de belastingvermindering verhoogd van 180 naar 280 uren voor
werknemers die tewerkgesteld worden door werkgevers die hoofdzakelijk wegenwerken
uitvoeren (met uitsluiting van het aanleggen van ondergrondse leidingen en kabels of
spoorwegwerken) en voor werknemers die door de overheid worden opgelegd om in
het weekend, op feestdagen of ‘s nachts te werken en die deze werken hebben uitgevoerd tijdens de overuren die voor deze werkgevers zijn gepresteerd.
Als werknemer geniet je van een fiscaal gunstregime voor overuren dat bestaat uit een
vermindering van de bedrijfsvoorheffing ten belope van:
• 66,81% op de bedrijfsvoorheffing op het brutoloon aan 100% dat als grondslag dient
voor de berekening van het overloon, voor wat overuren betreft waarop een wettelijke
overurentoeslag van 20% verschuldigd is;
• 57,75% op de bedrijfsvoorheffing op het brutoloon aan 100% dat als grondslag dient
voor de berekening van het overloon, voor wat overuren betreft waarop een wettelijke
overurentoeslag van 50% of 100% verschuldigd is.
a.9 Aandelen van erkende ontwikkelingsfondsen
Microfinancieringsinstellingen verstrekken kredieten aan kleine ondernemingen in ontwikkelingslanden. België heeft, om deze financieringsinstellingen de nodige middelen
te verschaffen, ‘ontwikkelingsfondsen’ opgericht. De belastingvermindering bedraagt
5% van de tijdens het belastbaar tijdperk werkelijk gedane betalingen. De belastingvermindering wordt wel geplafonneerd: de vermindering wordt beperkt tot 340 euro.
Belastinggids 2025 • 43

 a.10 Nieuwe aandelen/tax shelter voor startende vennootschappen
U kan van een belastingvermindering genieten van 30% of zelfs 45% indien het gaat
om nieuwe aandelen van een micro-vennootschap. De belastingvermindering wordt
verleend op jaarbasis op een maximaal gestort bedrag van 100 000 euro.
a.11 Nieuwe aandelen/tax shelter van groeibedrijven
Particulieren kunnen rechtstreeks of via een erkend crowdfundingsplatform investeren
in nieuwe aandelen van groeibedrijven en genieten van een belastingvermindering
van 25% op het geïnvesteerde bedrag. Particulieren kunnen via de tax shelter voor
starters (zie a.10) en voor groeibedrijven samen jaarlijks voor een maximaal bedrag van
100 000 euro investeren.
a.12 Adoptiekosten
De belastingvermindering voor adoptiekosten is gelijk aan 20% van de gemaakte kosten en zal minimum 6 530 euro bedragen per adoptieprocedure.
In het belastbaar tijdperk waarin de procedure wordt beëindigd, kan eenmalig een
belasting­vermindering worden aangevraagd. Alle kosten van dat jaar en de vijf voorafgaande jaren kunnen dan in één keer ingebracht worden.
a.13 Rechtsbijstandsverzekering
U kan een globale verzekering rechtsbijstand afsluiten die de kosten van bepaalde
juridische geschillen dekt. De premies rechtsbijstandsverzekering geven recht op een
belastingvermindering. De vermindering bedraagt 40% van de betaalde premies, waarvan het bedrag beperkt is tot 320 euro.
a.14 Pensioenen en vervangingsinkomsten
Er bestaat een belastingvermindering voor natuurlijke personen die pensioenen, vervangingsinkomsten, werkloosheidsuitkeringen, wettelijke ziekte- en invaliditeitsuitkeringen
en andere vervangingsinkomsten ontvangen (zie verder).
a.15 Inkomsten uit het buitenland
Als Belgisch rijksinwoner moet u steeds uw wereldwijd inkomen in België aangeven
in uw aangifte personenbelasting. Is er een dubbelbelastingverdrag, dan kunnen de
buitenlandse inkomsten, onder bepaalde voorwaarden in België vrijgesteld worden met
progressievoorbehoud. Als er geen dubbelbelastingverdrag afgesloten is tussen België
en de bronstaat, wordt de dubbele belasting op een andere manier vermeden.
a.16 Dividenden
Dividenden zijn in principe belastbaar als roerend inkomen. De eerste schijf van
833 euro (aj. 2025) aan dividenden is vrijgesteld van belastingen.
44 • Belastinggids 2025

 a.17 Installatie thuislaadpaal
Voor de aankoop (in nieuwe staat) en de installatie van een laadstation op het adres van
de belastingplichtige (op 01.01.aj.) kan u als particulier een belastingvermindering krijgen. Het moet gaan om de eigen woning waar u uiterlijk op 1 januari van het aanslagjaar ingeschreven bent. Dat kan zowel om uw eigen woning gaan waarvan u eigenaar
bent, alsook de woning waar u gebruiksrechten over heeft als huurder, vruchtgebruiker,
erfpachter of opstalhouder.
Het tarief bedroeg 45% voor uitgaven betaald in de periode 01.09.2021 tot
31.12.2022. Het percentage zakte naar 30% in 2023 en naar 15% in 2024.
Het grensbedrag van de uitgaven dat per laadstation en per belastingplichtige als basis
dient voor de belastingvermindering wordt opgetrokken (aanvankelijk 1 500 euro) naar
1 750 euro. Sinds 1 januari 2023 geldt een hoger grensbedrag voor bidirectionele laadpalen die, in tegenstelling tot standaard laadstations, elektriciteit in 2 richtingen kunnen
laden. Hiervoor voorziet de fiscus een hoger grensbedrag van 8 000 euro.
b. Gewestelijke belastingverminderingen
b.1 Eigen woning
Zie apart onderdeel woonfiscaliteit (IV, 10).
De ‘eigen woning’ is in principe de woning die u als belastingplichtige zelf betrekt.
De vermindering bedraagt tussen 30% en 50% van de uitgave.
b.2 Restauratie monumenten
De belastingvermindering voor de uitgaven voor het onderhoud of de restauratie van
gebouwde onroerende goederen of landschappen die beschermd zijn, worden enkel in
het Vlaams en Waals gewest verleend.
Voor de restauratie en het onderhoud van beschermde monumenten en gebouwen
bedraagt de gewestelijke belastingvermindering in het Waals gewest 30%. Het bedrag
waarvoor de belastingvermindering wordt verleend, is gelijk aan 50% van de werkelijk
betaalde uitgaven in het belastbaar tijdperk. Het maximaal bedrag van de uitgaven dat
recht geeft op de belastingvermindering is 48 710 euro.
In het Vlaams gewest wordt een belastingvermindering toegestaan van 40% voor uitgaven die verband houden met het behoud of herwaardering van onroerend erfgoed. Het
bedrag waarvoor de belastingvermindering wordt verleend, is gelijk aan de tijdens het
belastbaar tijdperk werkelijk betaalde uitgaven. Het bedrag mag per belastbaar tijdperk
niet meer bedragen dan 25 000 euro; dit bedrag wordt niet geïndexeerd.

Belastinggids 2025 • 45

 b.3 Dakisolatie
De energiebesparende uitgaven zijn nog uitsluitend te herleiden tot één enkele uitgave
namelijk die voor dakisolatie. Het maximumbedrag van de gewestelijke belastingvermindering voor dakisolatie bedraagt 3 900 euro. De belastingvermindering van 30%
van de uitgave wordt per woning en per belastbaar tijdperk en niet per belastingplichtige bepaald. Deze belastingvermindering bestaat enkel nog in het Waals gewest.
Overschrijden de berekende belastingverminderingen het toegelaten maximum, wordt
niet voorzien in een overdracht van het saldo naar een volgend belastbaar tijdperk. Een
eventueel belastingkrediet is evenmin aan de orde indien het belastbaar inkomen onvoldoende hoog is om de belastingvermindering integraal toe te passen.
b.4 PWA-cheques, wijk-werkcheques en dienstencheques
PWA-cheques en wijkwerken
Voor de in 2024 gekochte PWA- en wijk-werkcheques kan er per belastingplichtige
(alleenstaande of echtgenoot) vermindering worden bekomen op een bedrag van
maximaal 1 790 euro, voor de beide cheques samen (samen met dienstencheques).
In het Vlaams Gewest zijn de PWA-cheques vervangen door de wijk-werkcheques (de
voorwaarden en grenzen blijven dezelfde als bij het PWA-stelsel). In het Waals en het
Brussels Hoofdstedelijk gewest blijft het systeem van de PWA-cheques geldig.
In het Vlaamse gewest bedraagt de belastingvermindering 20% van het in aanmerking
te nemen bedrag. In het Waals gewest en Brussels Hoofdstedelijk gewest bedraagt de
belastingvermindering respectievelijk 30% en 15% van het in aanmerking te nemen
bedrag.
Dienstencheques
In het Vlaams en Brussels gewest is het bedrag dat in aanmerking komt voor de belastingvermindering, de nominale waarde of aanschafwaarde van de dienstencheques die
tijdens het belastbaar tijdperk zijn aangekocht verminderd met de nominale waarde
van de cheques die tijdens hetzelfde belastbaar tijdperk teruggestuurd zijn. Het bedrag
wordt ook hier beperkt tot maximaal 1 790 euro.

! Noot: het maximumbedrag geldt zowel voor de PWA- of wijkwerkcheques als dienstencheques samen.

In het Vlaams gewest bedraagt de vermindering 20% en in het Brussels gewest is er
een belastingvermindering van 15% van het in aanmerking te nemen bedrag.
In het Waals gewest worden de uitgaven die in aanmerking komen voor de belastingvermindering berekend in 3 stappen. Hiervoor kan verwezen worden naar de circulaire
Ci.700.168. van 17 december 2015. Het bedrag is beperkt tot maximaal 1 790 euro per
46 • Belastinggids 2025

 belastingplichtige. De belastingvermindering bedraagt 30% van het in aanmerking te
nemen bedrag.
De vermindering voor dienstencheques blijft omzetbaar in een (gewestelijk) belastingkrediet voor zover de vermindering niet kan worden verrekend met de gewestelijke
opcentiemen en gewestelijke belastingvermeerderingen.
b.5 Vernieuwing sociaal verhuurde woning
Vernieuwingswerken aan een woning van minstens 15 jaar oud, voor een bedrag van
minimaal 14 610 euro en die worden verhuurd via een sociaal verhuurkantoor, geven
recht op een belastingvermindering. Dit is een vermindering gedurende 9 jaar telkens
aan 5% van het bedrag van de uitgevoerde werken (of in totaal 45%) met een maximum van 1 460 euro per jaar. Deze regeling is geschrapt in het Brussels gewest (sinds
aanslagjaar 2017) en in het Vlaams Gewest (voor de uitgaven vanaf 1 januari 2019)
maar blijft in het kader van een overgangsregeling van toepassing. In het Waals gewest
is deze belastingvermindering nog steeds van toepassing.
c. Belastingverminderingen voor vervangingsinkomsten
De berekening van de belastingvermindering voor pensioenen, vervangingsinkomsten,
werkloosheidsuitkeringen, wettelijke ziekte- en invaliditeitsvergoedingen en werkloosheidsuitkeringen met bedrijfstoeslag is een van de moeilijkste onderdelen van de
personenbelasting.
De belastingvermindering voor pensioenen en andere vervangingsinkomsten wordt per
­echtgenoot/wettelijk samenwonende partner toegekend.
Met de Jobsdealswet (2019) is de berekeningswijze van de belastingvermindering voor
pensioenen en vervangingsinkomsten helemaal herwerkt zodat de ‘activiteitsval’ en de
‘pensioenval’ kan vermeden of toch minstens verzacht worden.
Basisbedrag van de belastingvermindering aanslagjaar 2025
:
• Wettelijk ziekte en invaliditeit: 2 887,28 euro;
• Pensioenen, andere vervangingsinkomsten, …:
• basisvermindering: 2 151,72 euro;
• aanvullende vermindering: 448,78 euro;
• Werkloosheidsuitkeringen: ;
• basisvermindering: 2151,72 euro
• aanvullende vermindering: 444,78 euro
• afbouwpercentage bijkomende vermindering: 60%

Belastinggids 2025 • 47

 De berekening van de vermindering is genuanceerder dan hierboven vermeld als
het inkomen binnen bepaalde grenzen valt of niet uitsluitend bestaat uit eenzelfde
vervangingsinkomen.

9.3 Belastingkredieten

Een belastingkrediet gaat verder dan een belastingvermindering. Een belastingvermindering kan tot gevolg hebben dat er geen belastingen meer moeten worden betaald.
Een belastingkrediet daarentegen kan onder 0 gaan en is zelfs terugbetaalbaar als het
voordeel groter is dan de belasting waarop het voordeel kan worden aangerekend.

a. Belastingkrediet voor kinderen ten laste
Wat?
Heel wat kinderrijke gezinnen kunnen niet of niet ten volle genieten van de belastingvoordelen wegens kinderlast. De verhoging van de belastingvrije som biedt hen vaak
geen voordeel omdat het inkomen lager is dan de belastingvrije som zelf.
De belastingvrije toeslagen voor kinderen ten laste, en dus ook het belastingkrediet
voor die kinderen, blijven een federale bevoegdheid.
Berekening van het belastingkrediet
Het niet gebruikte deel van de belastingvrije som wegens kinderlast wordt omgezet in
een terug betaalbaar belastingkrediet met een maximum van 550 euro per kind ten
laste (gehandicapte kinderen tellen dubbel).
Berekening van dit belastingkrediet wegens kinderlast (BKKL):
BKKL = het niet verrekende gedeelte van de belastingvrije som × het tarief van de
corresponderende inkomensschijf.
Het belastingkrediet wordt volledig verrekend met de personenbelasting zodat het
eventueel saldo wordt (terug)betaald.
Sinds aanslagjaar 2013 wordt het belastingkrediet bij gehuwden berekend tegen het
corresponderende tarief dat geldt bij de partner met het hoogste inkomen en niet meer
het tarief dat geldt bij de partner met het laagste inkomen. Bedoeling van deze maatregel is om gehuwden niet te discrimineren t.o.v. alleenstaanden.
Tevens kunnen internationale ambtenaren sinds aanslagjaar 2013 niet langer gebruik
maken van dit belastingkrediet. Zij genieten vaak een royaal inkomen maar worden
omwille van hun statuut vrijgesteld van belastingen in België. Omdat zij in de praktijk
geen belastingen moesten betalen genoten zij dus toch ook van dit belastingkrediet.
48 • Belastinggids 2025

 Dit belastingkrediet werd voor deze categorie nu expliciet uitgesloten in het Wetboek
van Inkomstenbelastingen.
b. Belastingkrediet voor werknemers met lage lonen (fiscale werkbonus)
Het gaat hier om een belastingkrediet, toegekend aan werknemers met een laag
inkomen, die genieten van de werkbonus. De sociale werkbonus is een systeem dat een
vermindering van de werknemersbijdrage voor de sociale zekerheid toekent aan werknemers met een laag loon. Op die manier houden ze een hoger nettoloon over, zonder
hiervoor het brutoloon te moeten verhogen.
Bedrag van 1 januari 2024 tot en met 31 maart 2024
De fiscale werkbonus, zonder dat dit hoger mag zijn dan 1 380 euro, is gelijk aan
33,14 % van de sociale werkbonus.
Bedrag sinds 1 april 2024
De fiscale werkbonus, zonder dat dit hoger kan zijn dan 1 380 euro, is gelijk aan een
bepaald percentage van de sociale werkbonus met een luik A voor de lage lonen (minder of gelijk aan 3 144,45 euro) en luik B voor de zeer lage lonen (loon minder of gelijk
aan 2 669,96 euro):
• 33,14 % van het bedrag van luik A
• 52,54 % van het bedrag van luik B.
Het gaat hier om een verrekenbaar en terugbetaalbaar belastingkrediet.
c. Belastingkrediet voor dienstencheques
Het deel van de belastingvermindering voor dienstencheques dat niet verrekend is
kunnen worden, is terugbetaalbaar. In tegenstelling tot bijvoorbeeld de belastingvrije
toeslagen voor kinderen ten laste, zijn dienstencheques een gewestelijke bevoegdheid
geworden. Deze gewestelijke belastingvermindering wordt dan ook omgezet in een
gewestelijk belastingkrediet.
In het Vlaams gewest kan het belastingkrediet enkel toegepast worden wanneer het
gezamenlijk belastbaar inkomen niet meer bedraagt dan 55 730 euro. In het Brussels
en Waals gewest geldt er geen beperking in functie van het gezamenlijk belastbaar
inkomen. Internationale ambtenaren (die in België wonen) die hun internationaal
­inkomen niet moeten aangeven in België, zijn uitgesloten.
d. Omzetting gewestelijk woonbonus in belastingkrediet
De omzetting van een aftrek naar een belastingvermindering (laatste staatshervorming)
heeft zo zijn gevolgen, ook op het vlak van het fiscaal voordeel van de woonbonus.

Belastinggids 2025 • 49

 Tot het aanslagjaar 2014 gebeurde het belastingvoordeel voor de enige woning onder
de vorm van een aftrekbare besteding waardoor het mogelijk was dat het gezamenlijk
belastbaar inkomen onder het bedrag van de belastingvrije som daalde. In dit geval
werd het niet aangerekende gedeelte van de belastingvrije som automatisch overgeheveld naar de andere echtgenoot (het moest gaan om gehuwden of wettelijk samenwonenden die gemeenschappelijk worden belast). Op die manier kon aan de partner met
een laag belastbaar inkomen steeds het volledige voordeel van de woonbonus worden
verleend.
Aangezien de aftrek nu omgevormd werd tot een belastingvermindering, zal de overheveling van het onbenutte saldo van de belastingvrije som niet altijd meer gebeuren.
Als compensatie wordt dit verlies opgevangen door het niet-aangerekend gedeelte van
de gewestelijke belastingvermindering om te zetten in een terugbetaalbaar belasting­
krediet. Dit zal enkel mogelijk zijn voor leningen die vóór 1 januari 2015 zijn afgesloten
en enkel voor de gewestelijke woonbonus.
e. Belastingkrediet Win-winlening, Coup de Pouce-lening en Proxi-lening
Het Vlaamse en Waalse gewest kenden reeds het stelsel van leningen aan bedrijven door
particulieren maar Brussel heeft nu ook al enkele jaren zijn eigen Proxi-lening. Ook een
inwoner van Brussel kan nu geld lenen aan een kmo en een deel via de belastingaangifte
recupereren.
Verder is er in Vlaanderen sinds enkele jaren een extra belastingvoordeel bijgekomen:
het zogenaamde vriendenaandeel. Familieleden en vrienden die aandelen verwerven
in kmo’s worden fiscaal beloond. Er is een belastingvoordeel wanneer u intekent op
een kapitaalverhoging met nieuwe aandelen op naam. De grens van 75 000 euro per
inbrenger en maximaal 300 000 euro per kredietnemer geldt voor de win-winlening en
vriendenaandeel samen.

50 • Belastinggids 2025

 Een overzicht van de 3 stelsels:
Proxi-lening:
sinds 15.10.2020*

Win-winlening

Coup de pouce

Geen werknemer,
aandeelhouder,
vennoot, bestuurder, zaakvoerder of
bedrijfsleider van
de kredietnemer

Dit wordt beoordeeld
bij het sluiten van de
lening

De uitsluiting geldt
de volledige looptijd

Dit wordt beoordeeld
bij het sluiten van de
lening

Looptijd

5 tot 10 jaar; de
hoofdsom moet in
1 keer of op basis
van een aflossings­
tabel terugbetaald
worden; vervroegde
terugbetaling is
mogelijk

4, 6, 8 of 10 jaar;
vervroegde terugbetaling is eerder
uitzonderlijk mogelijk

5 of 8 jaar maar
vervroegde terug­
betaling is mogelijk

Maximumbedrag
kredietgever
per jaar

max. € 75 000

max. € 125 000

max. € 50 000

Totaalbedrag
krediet­gever aan
één of meerdere
kredietnemers

max. € 75 000

max. € 125 000

max. € 50 000

Totaalbedrag dat
1 kredietnemer
kan ontlenen

€ 300 000

€ 250 000

€ 250 000

Belastingkrediet

2,5%

De 1ste 4 jaar 4%,
daarna 2,5%

De 1ste 3 jaar 4%,
daarna 2,5%

Wanneer de onderneming niet kan
terugbetalen: belastingkrediet 30%

Wanneer de onderneming niet kan
terugbetalen: belastingkrediet 30%

Wanneer de onderneming niet kan
terugbetalen: belastingkrediet 30%; kan
verhoogd worden tot
50 % indien geleend
aan een ‘voorbeeldige’ kredietnemer/
kmo (2de semester
vanaf 1 juli 2024)

Er is een versoepeling van 5 tot 10 jaar
mogelijk

* Wijzigingen in Ordonnantie van het Brussels Gewest van 17 maart 2023.

Belastinggids 2025 • 51

 f. Belastingkrediet voor vriendenaandelen
Particulieren, inwoners van het Vlaams gewest, kunnen aandelen verwerven van een
KMO-vennootschap, gevestigd in het Vlaams gewest. Het doel van deze regeling is om
het ondernemerschap in Vlaanderen te stimuleren. Het maximum bedrag per investeerder is 75 000 euro; het maximum bedrag per vennootschap is 300 000 euro.
Het belastingkrediet bedraagt 2,5% van het geïnvesteerde bedrag met een maximum
van 1 875 euro per belastingplichtige per jaar.

10. Woonfiscaliteit na de zesde staatshervorming

In dit hoofdstuk zal u een overzicht vinden van de woonfiscaliteit na de zesde staats­
hervorming voor aanslagjaar 2025.

10.1 Gewestelijke inwoner

Fiscaal bevoegd is steeds het gewest waar u op 1 januari van het aanslagjaar uw ‘fiscale
woonplaats’ hebt gevestigd. Woont u op 1 januari 2025 in het Brussels Hoofdstedelijk
gewest, dan betaalt u Brusselse opcentiemen op de federale belasting met betrekking
tot de inkomsten van heel 2024 en kent dit gewest de belastingverminderingen en
-kredieten toe voor het volledig jaar.

10.2 Begrip ‘eigen woning’
a. Fiscale uitgaven
De fiscale uitgaven met betrekking tot de ‘eigen woning’ maken het leeuwendeel uit
van de uitgaven die overgeheveld zijn naar de gewesten. De gewesten zijn namelijk
bevoegd voor de leningsuitgaven (kapitaalaflossingen en intrestbetalingen, premiebetalingen individuele levensverzekering) voor de ‘eigen woning’. De federale overheid
blijft bevoegd voor de ‘niet-eigen woning’, dat is de 2de of de 3de woning waarvan u
eigenaar bent.
b. Begrip ‘eigen woning’
De ‘eigen woning’ is de woning waarin u zelf woont (de gezinswoning), maar ook de
woning die u niet zelf betrekt, kan fiscaal een eigen woning zijn. Bijvoorbeeld wanneer
u uw woning niet betrekt omwille van verbouwingswerken of beroepsredenen (u woont
te ver van uw werk en huurt daarom een studio) ofwel wegens contractuele belemme­
ringen (het pand is verhuurd aan derden).
c. Tijdstip beoordeling ‘eigen woning’
De voorwaarden die voldaan moeten zijn om te kwalificeren als ‘eigen woning’, worden
beoordeeld tijdens het belastbaar tijdperk. In geval de situatie wijzigt in de loop van het
belastbaar tijdperk wordt het eigen karakter op dagbasis beoordeeld.
52 • Belastinggids 2025

 Ter illustratie twee voorbeelden.
Voorbeeld 1
U bent gehuwd en u heeft op 1 januari 2025 uw fiscale woonplaats in het Waalse gewest.
U hebt in de loop van het jaar 2024 samen met uw partner een andere woning (B)
gekocht om daar te gaan wonen. De 1ste woning (A) wordt verkocht in datzelfde jaar.
07.04.2024

15.07.2024

26.09.2024

aankoop woning B

verhuis naar woning B

verkoop woning A

Periode

Beoordeling ‘eigen woning’

01.01.2024 – 06.04.2024

Het echtpaar is eigenaar van één woning (A) die het zelf
betrekt; woning A is de eigen woning van het echtpaar.

07.04.2024 – 14.07.2024

Het echtpaar is nu eigenaar geworden van 2 woningen. De
eigen woning is de door het echtpaar zelf betrokken woning (A).

15.07.2024 – 25.09.2024

Het echtpaar is eigenaar van 2 woningen. De eigen woning is
de door het echtpaar zelf betrokken woning (B).

26.09.2024 – 31.12.2024

Het echtpaar is nu eigenaar van 1 woning (B) die het zelf
betrekt. Woning B is de eigen woning van het echtpaar.

Voorbeeld 2
Een wettelijk samenwonend koppel huurt een woning en kocht in 2019 een woning (A) die
ze zelf door verbouwingswerkzaamheden pas vanaf 10 december 2020 konden betrekken.
Periode

Beoordeling ‘eigen woning’

01.01.2020 – 09.12.2020

Het echtpaar is eigenaar van 1 woning (A) die zij zelf niet
betrekken omwille van de stand van de verbouwingswerkzaamheden. Woning A is de eigen woning van het echtpaar.

10.12.2020 – 31.12.2020

Het echtpaar is eigenaar van 1 woning (A) die zij zelf betrekken. Woning A is de eigen woning.

d. Absolute vrijstelling ‘eigen woning’
Reeds sinds aanslagjaar 2006 is het KI van de eigen woning een vrijgesteld onroerend
inkomen (zie III, 1.e).

Belastinggids 2025 • 53

 Sinds het aanslagjaar 2015 heeft de wetgever een absolute vrijstelling ingevoerd
voor het inkomen van de eigen woning. Dit heeft concreet tot gevolg dat geen enkele
belastingplichtige het KI van zijn eigen woning nog moet vermelden, zelfs niet wanneer
u nog fiscale voordelen aanvraagt van een oude lening die u voor deze woning heeft
afgesloten (althans voor vak III van de aangifte). Door deze vrijstelling verdwijnt dan
ook definitief de woningaftrek en de verrekening van de onroerende voorheffing uit het
fiscaal wetboek.
Door het wegvallen van de verrekening van de onroerende voorheffing, bestaat er nu een
gelijkaardig voordeel onder de vorm van een nieuwe gewestelijke belastingvermindering
(zie verder 10.4).

10.3 Aangifte van de onroerende inkomsten

Het KI is sinds het aanslagjaar 2015 niet langer opgedeeld in maanden, zoals van toepassing tot aanslagjaar 2014, maar wel in dagen. Ook bij nieuwbouw en vernieuwbouw zal
het KI vastgesteld worden vanaf de dag van de eerste ingebruikname van de nieuwbouwwoning of vanaf de dag waarop de werken zijn beëindigd.

10.4 Fiscale voordelen woningkredieten

Woonfiscaliteit was vroeger een federale materie maar na de zesde staatshervorming
werd deze bevoegdheid (deels) overgeheveld naar de gewesten. Sinds juli 2014 zien
we dat de gewesten gaandeweg verschillende accenten hebben gelegd. Voor lopende
kredieten wijzigt er voorlopig niet veel.
Ondertussen heeft de Vlaamse regering de geïntegreerde woonbonus afgeschaft voor
nieuwe hypothecaire leningen vanaf 1 januari 2020 en vervangen door een verlaging
van de registratierechten.
Het Vlaams gewest heeft voor de leningen afgesloten in 2015 de woonbonus, of de
belastingvermindering voor de ‘eigen’ woning, reeds gevoelig verlaagd. Het basisbedrag werd verlaagd naar 1 520 euro (in plaats van 2 280 euro). Ook werd de belastingvermindering beperkt tot 40% (i.p.v. de marginale aanslagvoet voor de ‘oude’ leningen). Noteer eveneens dat het basisbedrag (samen met de toeslagen van 760 euro en
80 euro) niet langer wordt geïndexeerd.
Nadien heeft het Vlaams gewest een nieuwe geïntegreerde woonbonus gelanceerd en dit
voor hypothecaire leningen vanaf 2016 tot en met 2019 voor het kopen of (ver)bouwen
van uw ‘eigen’ woning. Het tarief van het belastingvoordeel wijzigt niet en blijft 40%.
Maar de belastingvermindering voor het langetermijnsparen en de belastingvermindering voor de ‘gewone’ intresten wordt afgeschaft en in de nieuwe woonbonus
54 • Belastinggids 2025

 (3de generatie) ondergebracht. De ‘nieuwe’ woonbonus is van toepassing op hypothecaire leningen afgesloten vanaf januari 2016 tot en met 2019 met betrekking tot
de ‘eigen’ woning, ongeacht of dat de 1ste, 2de of 3de woning is. De voorwaarde
van ‘enige’ woning die noodzakelijk was om te kunnen genieten van een woonbonus,
vervalt hier.
In het Waals gewest heeft men de woonbonus reeds afgeschaft voor leningen afgesloten vanaf 1 januari 2016. De woonbonus wordt vervangen door de chèque habitat, een
soort van wooncheque. Noteer dat voor de bestaande leningen (dus afgesloten vóór
1 januari 2016) de bestaande fiscale grensbedragen niet meer worden geïndexeerd.
De chèque habitat is van toepassing op nieuwe leningen afgesloten voor het verwerven
van de volle eigendom van een woning. Ook dit is een uitdovend verhaal aangezien de
chèque habitat niet langer van toepassing zal zijn voor hypothecaire leningen afgesloten
vanaf 1 januari 2025 (aj. 2026).
Bovendien moet het ook gaan om de ‘enige’ woning van de belastingplichtige op
31 december van het leningsjaar (de voorwaarden zijn strenger dan voor de woon­
bonus). Het is een voordeel dat toegekend wordt vanaf het jaar volgend op het jaar van
het afsluiten van de lening en geldt per belastingplichtige en niet per woning.
Het voordeel geldt 20 jaar én op voorwaarde dat het netto belastbaar inkomen niet
hoger is dan 101 805 euro (aj. 2025).
De belastingplichtige die woont in het Waals gewest kan dan rekenen op twee voordelen:
• een forfaitair bedrag van 125 euro per kind ten laste vrij te verdelen over beide ouders
en
• een variabel bedrag per kredietnemer-eigenaar dat wordt berekend in functie van het
netto belastbaar inkomen.
Na tien jaar wordt het voordeel gehalveerd. De chèque habitat is niet gekoppeld aan een
bepaalde woning. De belastingplichtige kan in zijn leven gedurende maximum 20 jaar
beroep doen op de wooncheque. In het Brussels gewest werd de bestaande regeling
afgevoerd voor leningen afgesloten vanaf 1 januari 2017 en vervangen door een
­korting op de registratierechten (abattement) bij de aankoop van een ‘eigen’ woning.
Het gaat om een vrijstelling van registratierecht op een eerste schijf van 200 000 euro
bij de aankoop van een in het Brussels gewest gelegen ‘eigen/enige’ woning met een
waarde van maximaal 600 000 euro. Een hypothecaire lening is dus niet langer nodig.
Aangezien de woonfiscaliteit nu stilaan onoverzichtelijk wordt (leningen vóór 2004,
leningen vanaf 2005, leningen gesloten in 2015, leningen gesloten in 2016, leningen
gesloten in 2017, 2018, etc.) en er eveneens rekening moet gehouden worden met het
Belastinggids 2025 • 55

 soort woning (eigen of niet-eigen woning), zullen de hierna volgende info en tabellen u
hopelijk verder helpen. We focussen hier (voornamelijk) op de hypothecaire leningen.
a. Leningen vanaf 1 januari 2020
a.1 Vlaams gewest
De Vlaamse regering heeft de woonbonus in 2020 laten uitdoven. Voor bestaande
leningen verandert er niets maar heeft u in de loop van 2024 met een hypothecaire
lening een woning of appartement gekocht dan kan u niet langer genieten van een
fiscaal voordeel. Als compensatie krijgt u een gedeeltelijke verlaging van de registratierechten. Sinds 1 januari 2022 kan u in Vlaanderen een gezinswoning kopen tegen een
tarief van 3%. Het gaat dan om de woning waarvan u de volle eigendom verwerft met
de bedoeling om er uw hoofdverblijfplaats te vestigen. Bij een ingrijpende energetische
renovatie of sloop of herbouw van deze woning betaalt u nog maar 1%.
a.2 Waals gewest
Sinds 1 januari 2016 kent het Waals gewest de chèque habitat (zie verder b.2) dus ook
voor de leningen vanaf 1 januari 2020 tot en met 2024.

! Opgelet! De chèque habitat zal verdwijnen voor hypothecaire kredieten afgesloten
vanaf 1 januari 2025 (aj. 2026).

a.3 Brussels gewest
Het systeem van de woonbonus is ook in het Brussels gewest reeds afgevoerd sinds
1 januari 2017. De vroegere woonbonus is vervangen door een systeem van abattement (zie verder b.3).
b. Leningen vanaf 1 januari 2017
b.1 Vlaams gewest
Voor hypothecaire leningen afgesloten vanaf 1 januari 2017, dus ook voor leningen
vanaf 1 januari 2018 en in 2019 (niet voor leningen vanaf 2020), wijzigt er niets t.o.v.
de leningen afgesloten vanaf 1 januari 2016. Het bedrag van de Vlaamse geïntegreerde
woonbonus is dezelfde alsook de verhogingen (de bedragen worden niet meer geïndexeerd). Zie voor de bedragen de tabel in punt c.1. Vlaams gewest. Gaat het over een
niet-eigen woning , dan blijft de federale overheid bevoegd (langetermijn­sparen).
De bedragen kan u eveneens terugvinden in de tabel onder punt c.1 Vlaams gewest.

56 • Belastinggids 2025

 b.2 Waals gewest
In het Waals gewest geldt voor hypothecaire leningen vanaf 1 januari 2016 de chèque
habitat. Het betreft hier nog steeds een inkomensafhankelijk (uitkeerbaar) belasting­
krediet (geen belastingvermindering) berekend op een bepaald bedrag aan kapitaalaflossingen en/of intresten. Voor de voorwaarden kan verwezen worden naar punt c.2
Waals gewest. De chèque habitat bedraagt 1 520 euro (wordt niet meer geïndexeerd)
bij een nettobelastbaar inkomen van minder of gelijk aan 26 394 euro (aj. 2025) (geïndexeerd). Bij een hoger inkomen wordt van de 1 520 euro een bepaald bedrag afgetrokken. Per kind ten laste wordt het bedrag (voor de beide ouders samen) verhoogd met
125 euro (niet geïndexeerd).

! Opgelet! Wie een nettobelastbaar inkomen heeft hoger dan 101 805 euro

(aj. 2025 (geïndexeerd) heeft geen recht meer op de chèque habitat. Voor hypo­
thecaire leningen ‘eigen/enige’ woning aangegaan vanaf 1 januari 2025, zal de
chèque habitat worden afgeschaft. Ter compensatie vermindert dan wel het
registratie­recht naar 3 % bij de aankoop van een ‘eigen/enige’ woning vanaf
1 januari 2025.

b.3 Brussels gewest
Zoals reeds hierboven vermeld, is sinds 1 januari 2017 het systeem van de woonbonus
afgeschaft in Brussel. In de plaats krijgen kopers (natuurlijke personen) van een ‘eigen’
woning in het Brussels Hoofdstedelijk gewest een hogere korting van 25 000 euro
op de registratierechten (ook wel abattement genoemd). Tot en met een aankoop van
200 000 euro moeten er geen registratierechten betaald worden.

Belastinggids 2025 • 57

 Wat zijn de voorwaarden bij de aankoop van een huis of appartement?
• Het abattement wordt geplafonneerd tot aankopen van 600 000 euro.
Boven dit bedrag gelden de gebruikelijke registratierechten van 12,5%.
• De woning moet gelegen zijn in het Brussels Hoofdstedelijk gewest
(19 gemeenten).
• De aankoop moet gaan om ‘een tot bewoning aangewend of bestemd
onroerend goed’ en betreft een geheelheid in volle eigendom.
• De kopers mogen geen andere woning voor de geheelheid in volle eigendom bezitten op datum van de overeenkomst tot verkrijging (ook niet in het
buitenland).
• De woning zal door alle kopers worden bestemd als hoofdverblijfplaats binnen
de 2 jaar na datum van de registratie van het document waarop de evenredige
rechten werden geheven; bij een aankoop van een appartement op plan of in
aanbouw wordt deze termijn op 3 jaar gebracht.
• De verkrijger moet gedurende een ononderbroken periode van 5 jaar zijn
hoofdverblijfplaats behouden in de aangekochte woning te rekenen vanaf het
vestigen van de hoofdverblijfplaats in het onroerend goed.
Verminderde registratierechten voor bouwgronden
Eveneens sinds 1 januari 2018 krijgt u een korting op de registratierechten als u
een bouwgrond koopt. Op de eerste 100 000 euro moet u geen registratie­rechten
van 12,5% betalen (besparing van 12 500 euro). Het bedrag van de bouwgrond
moet lager zijn dan 300 000 euro en u vestigt uw hoofdverblijfplaats op het adres
van de bouwgrond binnen de 3 jaar na de aankoop. Het nieuw ­abattement voor
de aankoop van bouwgronden geldt enkel wanneer de grond wordt aangekocht
met de bedoeling er zelf een woning te bouwen.
Opgelet! Het abattement voor de aankoop van een bouwgrond is niet geldig voor
de aankoop van een onroerend goed in aanbouw of een huis op plan, dat eigenlijk
in aanmerking kan komen van het abattement van 200 000 euro. Het abattement
van 100 000 euro is alleen van toepassing op de verwerving van onbebouwd
terrein, zonder een overeenkomst met de verkoper om op het terrein te bouwen.
Bijkomend abattement bij een energetische renovatie
Dit abattement is bijkomend aan het algemeen abattement en enkel van toepassing op voorwaarde dat het algemeen abattement wordt toegepast. Het bedraagt
25 000 per sprong van energieklasse, mits een verbetering van minstens 2
sprongen.

58 • Belastinggids 2025

 c. Hypothecaire leningen vanaf 1 januari 2016 voor de ‘eigen’ woning en
de ‘niet-eigen’ woning
c.1 Vlaams gewest
Eigen woning
• Vlaamse geïntegreerde woonbonus indien het de eigen woning betreft
• Basiskorf: 1 520 euro (tarief 40%)
• Vraag: is de woning op 31.12 van het leningsjaar de ‘enige’ woning2?
Indien ja: recht op toeslagen3: 760 euro (1ste 10 jaar) en 80 euro (3 kinderen)
Niet-eigen woning
• Kapitaal: federaal langetermijnsparen (tarief 30%) met grens
(zie tabel achteraan brochure)
• Intrest: federale intrestaftrek (marginaal tarief)
• Schuldsaldoverzekering: federaal langetermijnsparen (tarief 30%)

!  Opgelet! de Vlaamse geïntegreerde woonbonus is niet combineerbaar met de

ouder Vlaamse voordelen van leningen gesloten vóór 1 januari 2016 (keuze).

c.2 Waals gewest
Eigen woning
• Chèque-habitat indien de toekenningsvoorwaarden4 zijn vervuld.
• Indien de voorwaarden niet zijn voldaan: geen voordelen voor intresten,
kapitaal en levensverzekering
Niet-eigen woning
• Kapitaal: federaal langetermijnsparen (tarief 30%) met grens
(zie tabel achteraan brochure)
• Intrest: federale intrestaftrek (marginaal tarief)
• Schuldsaldoverzekering: federaal langetermijnsparen (tarief 30%)

2 ‘Enige’ woning op 31.12 van het leningsjaar d.w.z. geen volle (mede)eigenaar, vruchtgebruiker, erfpachter, opstalhouder, bezitter of naakte
eigenaar van een andere woning. Uitzonderingen: a) door erfenis mede-eigenaar, naakte eigenaar of vruchtgebruiker worden van de andere
woning of b) de woning te koop aangeboden op 31.12 van het leningsjaar en verkocht uiterlijk op 31.12 van het jaar van de lening + 1.
3 De toeslagen kunnen verloren gaan: a) sowieso vanaf het 11de leningsjaar en b) als de kredietnemer volle (mede)eigenaar , vruchtgebruiker,
erfpachter, opstalhouder of bezitter is geworden op 31.12 van een andere woning.
4 Toekenningsvoorwaarden chèque-habitat: de woning zelf betrekken én het moet de ‘enige’ woning zijn op 31.12 van het leningsjaar (uitzonderingen: sociale of beroepsredenen, wettelijke of contractuele belemmeringen, stand van de bouwwerkzaamheden die niet mogelijk maken dat de woning kan betrokken worden (bij de laatste 2 uitzonderingen moet de woning betrokken worden op 31.12 van het leningsjaar + 2). Bij de voorwaarde
van ‘enige’ woning kan verwezen worden naar voetnoot 1 maar met bijkomende uitzondering de ‘verhuring via een sociaal verhuurkantoor’.

Belastinggids 2025 • 59

 c.3 Brussels gewest (opgelet! Leningen t.e.m. 31.12.2016)
Eigen woning
1. Gewestelijke woonbonus indien eigen woning (uitzonderingen)
én enige woning op 31.12 van het leningsjaar 5 (tarief 45%)
• Basiskorf: 2 810 euro
• Recht op toeslagen: 940 euro (1ste 10 jaar) en 90 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn voldaan
(maar wel nog steeds ‘eigen’ woning):
• Kapitaal: gewestelijke belastingvermindering langetermijnsparen (tarief 30%)
• Intresten: geen voordelen
• Schuldsaldoverzekering: gewestelijke belastingvermindering langetermijn­sparen
(tarief 30%)
Niet-eigen woning
• Kapitaal: federaal langetermijnsparen (tarief 30%) met grens
(zie tabel achteraan brochure)
• Intrest: federale intrestaftrek (marginaal tarief)
• Schuldsaldoverzekering: federaal langetermijnsparen (tarief 30%)

d. Hypothecaire leningen gesloten in 2015 voor de ‘eigen’ woning
d.1 Vlaams gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 40%)
• Basiskorf: 1 520 euro
• Vraag: is de woning nog steeds de ‘enige’ woning?
Indien ja: toeslag 760 euro (1ste 10 jaar) en 80 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)

5 Voorwaarden woonbonus: zelf de woning betrekken én de ‘enige’ woning op 31.12 van het leningsjaar. De uitzonderingen op de zelfbetrekkingsverplichting: sociale of beroepsredenen, wettelijke of contractuele belemmeringen, stand van de bouwwerkzaamheden die niet
mogelijk maken dat de woning kan betrokken worden (bij de laatste 2 uitzonderingen moet de woning betrokken worden op 31.12 van het
leningsjaar + 2). Voor de ‘enige’ woning gelden dezelfde uitzonderingen als in voetnoot 1.

60 • Belastinggids 2025

 Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 40%)
• Basiskorf: 1 520 euro
• Vraag: is de woning nog steeds de ‘enige’ woning?
Indien ja: toeslag 760 euro (1ste 10 jaar) en 80 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering gewone intresten (tarief 40%)

d.2 Waals gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 40%)
• Basiskorf: 2 290 euro
• Vraag: is de woning nog steeds de ‘enige’ woning?
Indien ja: toeslag 760 euro (1ste 10 jaar) en 80 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)
Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 40%)
• Basiskorf: 2 290 euro
• Vraag: is de woning nog steeds de ‘enige’ woning?
Indien ja: toeslag 760 euro (1ste 10 jaar) en 80 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• GEEN gewestelijke belastingvermindering meer

d.3 Brussels gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 45%)
• Basiskorf: 2 920 euro
• Vraag: is de woning nog steeds de ‘enige’ woning? Indien ja: toeslag 970 euro
(1ste 10 jaar) en 100 euro (3 kinderen)
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)
Belastinggids 2025 • 61

 Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht
op de gewestelijke belastingvermindering van de woonbonus (tarief 45%)
• Basiskorf: 2 920 euro
• Vraag: is de woning nog steeds de ‘enige’ woning? Indien ja: toeslag 970 euro en
100 euro (3 kinderen)
2. Indien de cruciale woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• GEEN gewestelijke belastingvermindering meer

e. Hypothecaire leningen gesloten tussen 1 januari 2005 en 31 december 2014 voor
de ‘eigen’ woning
e.1 Vlaams gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min. 30%)
• Basiskorf: 2 280 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)
Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min 30%)
• Basiskorf: 2 280 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering gewone intresten (marginaal tarief, min 30%)

62 • Belastinggids 2025

 e.2 Waals gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min 30%)
• Basiskorf: 2 290 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)
Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min 30%)
• Basiskorf: 2 290 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering gewone intresten (marginaal tarief, min 30%)

e.3 Brussels gewest
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min 30%)
• Basiskorf: 2 920 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering langetermijnsparen (tarief 30%)

Belastinggids 2025 • 63

 Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar dan recht op
de gewestelijke belastingvermindering van de woonbonus (marginaal tarief, min 30%)
• Basiskorf: 2 920 euro
• De tienjarige toeslag-periode is voorbij
2. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• gewestelijke belastingvermindering gewone intresten (marginaal tarief, min 30%)

f. Hypothecaire leningen gesloten vóór 31 december 2004 voor de ‘eigen’ woning
voor het Vlaams, Waals en Brussels gewest
Kapitaalaflossingen (lening afgesloten tussen 1 januari 1993 en 31 december 2004)
1. Indien de ‘enige’ woning op de datum van het afsluiten van de lening dan gewestelijke
belastingvermindering bouwsparen (marginaal tarief, min 30%)
2. Indien niet de ‘enige’ woning dan gewestelijke belastingvermindering langetermijn­
sparen (tarief 30%)
Intresten (lening afgesloten tussen 1 mei 1986 en 31 december 2004)
1. Indien de voorwaarden van de bijkomende intrestaftrek6 zijn vervuld dan recht op de gewestelijke belastingvermindering voor bijkomende intresten (marginaal tarief, min 30%)
2. Indien de voorwaarden van de bijkomende intrestaftrek niet zijn vervuld dan gewestelijke belastingvermindering voor gewone intresten (marginaal tarief, min 30%) en
verrekening onroerende voorheffing (12,50%)

6 Voorwaarden bijkomende intrestaftrek: o.a. enige woning op 31.12 van het belastbaar tijdperk (dus geen andere woning(en) in volle (mede)
eigendom, vruchtgebruik, erfpacht, opstal of bezit. Telt niet mee als 2de woning: volle mede-eigendom of vruchtgebruik in onverdeeldheid
verworven door erfenis of schenking.

64 • Belastinggids 2025

 g. Kapitaalaflossingen en intresten die op het tijdstip van de betaling betrekking hebben
op een andere dan de ‘eigen’ woning: steeds federale voordelen
g.1 Lening afgesloten vanaf 1 januari 2014 maar vóór 2024
Kapitaalaflossingen:
• federale belastingvermindering langetermijnsparen (tarief 30%)
Intresten
• Indien het onroerend inkomen van de woning in de belastbare basis van het huidig
tijdperk zit dan de federale gewone intrestaftrek (marginaal tarief, min 30%)
• Indien niet het geval: geen aftrek
g.2 Lening afgesloten tussen 1 januari 2005 en 31 december 2013
Kapitaalaflossingen
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar en vóór
01.01.2016 ‘niet-eigen’ woning geworden (én vorig jaar de federale belastingvermindering woonbonus aangevraagd) dan federale belastingvermindering woonbonus
(marginaal tarief, min 30%):
• Basiskorf: 2 450 euro
• De tienjarige toeslag-periode is voorbij
• Optie voor de federale belastingvermindering langetermijnsparen (tarief 30%)
2. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar maar vóór
01.01.2016 niet de ‘niet-eigen’ woning geworden dan federale belastingvermindering
langetermijnsparen (tarief 30%)
3. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• federale belastingvermindering langetermijnsparen (tarief 30%)

Belastinggids 2025 • 65

 Intresten
1. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar en vóór
01.01.2016 ‘niet-eigen’ woning geworden (én vorig jaar de federale belastingvermindering woonbonus aangevraagd) dan de federale belastingvermindering woonbonus
(marginaal tarief, min 30%)
• Basiskorf: 2 450 euro
• De tienjarige toeslag-periode is voorbij
• Optie voor de federale gewone intrestaftrek
2. Indien de woonbonusvoorwaarden zijn vervuld op 31.12 van het leningsjaar maar vóór
01.01.2016 niet de ‘niet-eigen’ woning geworden dan 2 vragen:
• Zit het onroerend inkomen van die woning in de belastbare basis van huidig tijdperk?
Indien ja dan federale gewone intrestaftrek (marginaal tarief)
• Indien neen: geen aftrek
3. Indien de woonbonusvoorwaarden niet zijn vervuld op 31.12 van het leningsjaar
• Zit het onroerend inkomen van die woning in de belastbare basis van het huidig
tijdperk? Indien ja dan federale gewone intrestaftrek (marginaal tarief)
• Indien neen: geen aftrek

g.3 Lening afgesloten tussen 1 januari 1993 en 31 december 2014 (voor kapitaalaflossingen)
en tussen 01.05.1986 en 31.12.2014 (voor intresten)
Kapitaalaflossingen
1. Indien de ‘enige’ woning op de datum van het afsluiten van de lening en vóór
01.01.2016 de ‘niet-eigen’ woning geworden (en vorig jaar de federale belasting­
vermindering bouwsparen aangevraagd) dan federale belastingvermindering bouwsparen (marginaal tarief, min 30%)
2. Indien de ‘enige’ woning op de datum van het afsluiten van de lening en niet vóór
01.01.2016 de ‘niet-eigen’ woning geworden dan federale belastingvermindering
langetermijnsparen (tarief 30%)
3. Indien niet de ‘enige’ woning op de datum van het afsluiten van de lening dan federale
belastingvermindering langetermijnsparen (tarief 30%)

66 • Belastinggids 2025

 Intresten
1. Indien de voorwaarden voor de bijkomende intrestaftrek zijn vervuld en vóór
01.01.2016 de ‘niet-eigen’ woning geworden (én vorig aanslagjaar de federale
belastingvermindering bijkomende intresten aangevraagd) dan federale belastingvermindering voor bijkomende intresten (marginaal tarief)
2. Indien de voorwaarden voor de bijkomende intrestaftrek zijn vervuld en niet vóór
01.01.2016 de ‘niet-eigen’ woning geworden dan 2 vragen:
• Zit het onroerend inkomen van die woning in de belastbare basis van het huidig
tijdperk? Indien ja dan de federale gewone intrestaftrek (marginaal tarief)
• Indien neen: geen aftrek
3. Indien de voorwaarden voor de bijkomende intrestaftrek niet zijn vervuld dan 2 vragen:
• Zit het onroerend inkomen van die woning in de belastbare basis van het huidig
tijdperk? Indien ja dan de federale gewone intrestaftrek (marginaal tarief)
• Indien nee: geen aftrek

11. Afzonderlijke aanslagen

Hoewel uw netto belastbare inkomsten worden geglobaliseerd en onderworpen worden
aan een progressief tarief om de belastingen te berekenen, is er voor bepaalde inkomsten toch een uitzondering. Deze inkomsten worden uit de ‘korf’ inkomsten gelicht en
apart belast aan een bepaald percentage. Dit gebeurt enkel als het voor u voordeliger is.
Zo niet, worden de inkomsten toch mee betrokken in de globalisatie. In het overzicht dat
volgt worden de belangrijkste afzonderlijke aanslagen weergegeven.

a. Taxatieregels individuele levensverzekeringen en pensioensparen

Niettegenstaande de taxatie op het pensioensparen en de individuele levensverzekeringen grote gelijkenissen vertonen, is er toch wel een belangrijk verschil in de eind­
belasting waardoor het noodzakelijk wordt een opsplitsing te maken tussen beide in
de hiernavolgende tabellen.
Individuele levensverzekering
Soort verzekering

Tarief
Premies gestort
vóór 01.01.1993

Premies gestort
na 01.01.1993

10%

10%

1. Uitbetaling bij leven
Vanaf 60 jaar

Belastinggids 2025 • 67

 Individuele levensverzekering
Soort verzekering

Tarief
Premies gestort
vóór 01.01.1993

Premies gestort
na 01.01.1993

16,5%
Marginale aanslagvoet

10%
33%

16,5%

10%

1. Uitbetaling bij leven
Vóór 60 jaar
• op normale datum 1
• voor de normale datum 2
2. Overlijdensverzekering
Overlijden

Pensioensparen
Soort verzekering

Tarief
Premies gestort
vóór 01.01.1993

Premies gestort
na 01.01.1993

8% 3

8% 3

Vóór 60 jaar bij contract
10 j. en 5 stortingen en
elke storting 5 jaar belegd

16,5% 3/10%

8% 3

Andere omstandigheden

Marginale aanslagvoet

33%

16,5% 3

8% 3

1. Uitbetaling bij leven
Vanaf 60 jaar

2. Overlijdensverzekering
Overlijden

1 Dit is enkel voor vrouwen én een contract van vóór 01.01.2002 dat ten vroegste vanaf 55 jaar wordt afgekocht.
2 Alle andere gevallen dan onder (1).
3 Als gevolg van een budgettaire maatregel werd in 2012 op vele contracten een anticipatieve taks ingehouden. Bijgevolg worden sommige
gedeeltes in de eindafrekening nog op 16,5% belast terwijl andere op 10% belast worden. Dezelfde maatregel heeft eveneens als gevolg dat
voor uitkeringen vanaf 60 jaar of kapitaal gevormd door bijdragen na 01.01.1993 de taxatie op 8% wordt vastgelegd.

b. Taxatieregels aanvullende pensioenen

Aanvullende pensioenen worden zeer specifiek uitgewerkt in het kader van een arbeidsrelatie. Dit kan zowel op sector- als op bedrijfsvlak gebeuren.
De algemene regel is dat het bedrag van het aanvullend pensioen pas kan uitbetaald
worden op het ogenblik van de ‘pensionering’. Hiermee wordt het wettelijke pensioen
68 • Belastinggids 2025

 en het wettelijk vervroegd pensioen bedoelt. Er zijn evenwel een aantal overgangsmaat­
regelen voorzien volgens de specifieke situatie waarin de werknemer zich bevond in het
jaar 2016. Dit alles maakt dat sommige taxatieregels op uitbetaling van kapitalen in het
kader van een aanvullend pensioen op termijn zullen uitdoven en bijgevolg niet meer
zullen toegepast worden.
Het kapitaal kan opgebouwd worden uit werknemersbijdragen en/of werkgeversbijdragen.
De uitkering van het aanvullend pensioen kan – bij leven en bij het bereiken van de
pensioenleeftijd – via de volgende mogelijkheden:
• de uitbetaling onder de vorm van een éénmalig kapitaal;
• een rente;
• een kapitaal omgezet in een periodieke rente bij leven.
Het pensioenplan voorziet uitdrukkelijk één van deze mogelijkheden of kan aan de
betrokkene de keuze laten ervan.
De meest voorkomende vorm van uitbetaling van het aanvullend pensioen betreft de
betaling onder de vorm van een kapitaal, reden waarom verder enkel de belasting van
het kapitaal in deze rubriek wordt behandeld.
Het principe van de betaling op een ‘gunstig moment’ is hierbij van belang.
De uitbetaling kan verkregen worden op het ogenblik van de wettelijke pensionering.
Sommige pensioenplannen voorzien nog een uitbetaling vanaf 60 jaar en op voorwaarde dat dit uitdrukkelijk in het pensioenreglement werd opgenomen.
Elke uitbetaling van een aanvullend pensioen dat niet conform deze voorwaarden wordt
uitbetaald – op een zogenaamde ‘ongunstig moment’ – wordt fiscaal afgestraft.
De taxatieregels op aanvullende pensioenen kunnen als volgt samengevat worden:
1. Voor het kapitaal opgebouwd uit de werknemersbijdragen
Het kapitaal opgebouwd door persoonlijke stortingen vóór 01.01.1993 wordt belast
aan 16,5%. Het kapitaal opgebouwd door persoonlijke stortingen vanaf 01.01.1993
wordt belast aan 10%.
2. Voor het kapitaal opgebouwd uit de werkgeversbijdragen
De tarieven van de eenmalige taxatie wordt in de hiernavolgende tabel samengevat.
Leeftijd uitkering
kapitaal

Niet wettelijk gepensioneerd
(incl. ‘brugpensioen’/SWT)

(Vervroegd) wettelijk
met pensioen

(60 jaar)

(20%)1

(16,5%)

61 jaar

18% 1

16,5%
Belastinggids 2025 • 69

 Leeftijd uitkering
kapitaal

Niet wettelijk gepensioneerd
(incl. ‘brugpensioen’/SWT)

(Vervroegd) wettelijk
met pensioen

62 tot 64 jaar

16,5%

16,5%

65 jaar of bij vervroegd
pensioen met volledige
loopbaan (45 jaar)

10% 2

10% 2, 3

1 Deze percentages blijven behouden tot zolang de overgangsmaatregel van toepassing blijft.
2 Het tarief van 10% wordt toegekend zo men ononderbroken effectief actief was tot op het moment dat de wettelijke pensioenleeftijd bereikt
werd. Bepaalde periodes van inactiviteit of verminderde activiteit echter gelijkgesteld worden. Het 16,5%-tarief is van toepassing indien de
uitkering gebeurt naar aanleiding van de pensionering maar de bovenvermelde voorwaarde van effectief actief is niet voldaan of enkel ingeval
van pensionering zonder dat de leeftijd van 65 jaar werd bereikt.
3 Ook bij vervroegd pensioen met volledige loopbaan (45 jaar) geldt de voorwaarde van effectieve activiteit tot aan de vervroegde wettelijke
pensioenleeftijd om het gunsttarief van 10% te genieten. Indien niet geldt het tarief van 16,5%.

c. Worden eveneens belast tegen 33%

• de toevallige of occasioneel verkregen winsten;
• de kapitalen en afkoopwaarden in het kader van het pensioensparen, van individuele
levensverzekeringscontracten en van groepsverzekeringen wanneer deze voortijdig
worden uitbetaald. (Zie ook tabel taxatie individuele levensverzekeringen en pensioensparen onder punt a.);
• de belastbare bezoldigingen van gelegenheidswerkers in de horeca en van gepensioneerden in de zorgsector (gunstregeling verlengd tot minstens eind 2024).

d. Worden belast tegen de gemiddelde aanslagvoet
De gemiddelde aanslagvoet wordt toegepast bij o.a.:
• opzeggings- en inschakelingsvergoedingen;
• achterstallen;
• vervroegd vakantiegeld;
• achterstallige onderhoudsuitkeringen;
•…

De inkomsten zoals opzeggings- en inschakelingsvergoedingen en achterstallen worden
belast tegen het gemiddelde tarief van het laatste vorige jaar waarin de belastingplichtige 12 maanden belastbare beroepsinkomsten heeft gehad. De aard van de beroepsinkomsten is van geen belang meer. Het kan dus eveneens geheel of gedeeltelijk gaan om
vervangingsinkomsten of pensioenen. De nieuwe definitie van referentiejaar geldt sinds
aanslagjaar 2019 en zal meestal voordeliger zijn voor de belastingplichtige.

70 • Belastinggids 2025

 e. Omzetting in een lijfrente van sommige kapitalen, vergoedingen en
afkoopwaarden
Welke kapitalen, vergoedingen en afkoopwaarden?
Kapitalen die worden vereffend bij het normaal verstrijken van het contract of bij overlijden van de verzekerde en afkoopwaarden die worden vereffend in één der vijf jaren die
aan het normaal verstrijken van het contract voorafgaan, voorkomend van:
• aanvullende pensioenen;
• kapitalen als vergoeding voor het gehele of gedeeltelijk herstel van een bestendige
derving van beroepsinkomsten;
• individuele levensverzekeringscontracten:
a. kapitalen of afkoopwaarden voortkomend van een schuldsaldoverzekering;
b. kapitalen of afkoopwaarden van individuele levensverzekeringen in zover zij dienen
voor het waarborgen of de wedersamenstelling van een hypothecaire lening.
Welke taxatie?
De kapitalen worden, voor de vaststelling van de belastbare grondslag, slechts in
aanmerking genomen ten belope van de lijfrente die zou voortvloeien uit hun omzetting
volgens coëfficiënten die niet meer dan 5% mogen bedragen.
Leeftijd

Coëfficiënt

Leeftijd

Coëfficiënt

≤ 40

1

59 – 60

3,5

41 – 45

1,5

61 – 62

4

46 – 50

2

63 – 64

4,5

51 – 55

2,5

≤ 65

5

56 – 58

3

! Opmerking! Hetzelfde omzettingsstelsel is van toepassing op het kapitaal of van de

afkoopwaarde van levensverzekeringscontracten die het voorwerp hebben uitgemaakt van voorschotten op contracten of die als waarborg hebben gediend van een
hypothecaire lening, voor zover die voorschotten verleend of die leningen gesloten
werden voor het bouwen, het verwerven of het verbouwen van een in België gelegen
eerste woonhuis dat uitsluitend bestemd is voor het persoonlijk gebruik van de
leningnemer en van de personen die van zijn gezin deel uitmaken en indien, bij leven
van de verzekerde, de voorschotten op contracten of vestiging van de hypotheek ten
minste tien jaar vóór het verstrijken van het contract hebben plaatsgevonden.

Belastinggids 2025 • 71

 12. Voorheffingen en voorafbetalingen
a. Bedrijfsvoorheffing

De totale belasting wordt verminderd met de eventueel ingehouden bedrijfsvoorheffing.
Deze bedrijfsvoorheffing wordt maandelijks ingehouden op de bezoldiging of het
vervangings­inkomen en dit volgens regels en barema’s opgenomen in een KB. De regels
inzake de berekening van de bedrijfsvoorheffing zijn grondig gewijzigd sinds 1 januari 2023.
Vermits u door deze bedrijfsvoorheffing reeds een groot deel van de verschuldigde belasting vooraf betaalt, mag deze verminderd worden met de betaalde bedrijfsvoorheffing.

b. Mogelijkheden tot voorafbetaling

U kunt ook als niet-zelfstandige, vier keer per jaar een deel van uw belastingen vooraf betalen. Dit geeft recht op een bonificatie, hetgeen neerkomt op een belastingvermindering.
Een bonificatie wordt verleend aan elke natuurlijke persoon die nog effectief belasting
moet betalen op zijn inkomsten ondanks de aftrek van bedrijfsvoorheffing en andere
verrekenbare bestanddelen (belastingkredieten, roerende voorheffing, …).
Deze belastingvermindering wordt verleend aan de natuurlijke personen die de tot
106% verhoogde belasting, verminderd met de voorheffingen, de andere verrekenbare
bestanddelen en de voorafbetalingen die nodig zijn om de belastingvermeerdering te
vermijden, bij wijze van voorafbetaling voldoen.
Voor het aanslagjaar 2025 (inkomsten 2024) is het bedrag van de bonificatie gelijk aan
de som van de volgende producten:
• bedrag van het eerste kwartaal (VA 1) × 4,5%
• bedrag van het tweede kwartaal (VA 2) × 3,75%
• bedrag van het derde kwartaal (VA 3) × 3%
• bedrag van het vierde kwartaal (VA 4) × 2,25%
Hoe gaat u precies te werk indien u een voorafbetaling wenst te doen? Kies de eenvoudigste weg en doe het online via MyMinfin. Zo betaalt u automatisch op het juiste
rekeningnummer en met de juiste gestructureerde mededeling. U moet alleen nog het
bedrag invullen dat u wil storten en op ‘online betalen’ klikken.
Andere betaalmethodes zijn eveneens nog mogelijk:
1. U kan via een overschrijving betalen:
• Op het rekeningnummer BE61 6792 0022 9117 (BIC: PCHQ BEBB) van het
‘Inningscentrum – Dienst voorafbetalingen’ (Koning Albert II-laan, 1030 Brussel);
• Met een gestructureerde mededeling die u vindt in MyMinfin;
72 • Belastinggids 2025

 • Bij voorkeur via een bankrekening die op uw naam is geopend.
2. U kan een derde voor u laten betalen (zoals een bank). Uw bank zal dan wel de
gestructureerde mededeling moeten gebruiken die u terugvindt in MyMinfin.

13. Bijzondere bijdrage voor de sociale zekerheid

De bijzondere bijdrage voor de sociale zekerheid (BBSZ) is een ietwat vreemde bijdrage
die u als werknemer moet betalen. In tegenstelling tot de gewone socialezekerheidsbijdragen, wordt de bijzondere bijdrage niet berekend op het loon van de werknemer maar
berekend op basis van het belastbare inkomen van de werknemer, inclusief dat van uw
partner wanneer u een gemeenschappelijke aanslag in de personenbelasting heeft. In
afwachting van het definitief bedrag – dat berekend wordt met de eindafrekening van de
personenbelasting – zal u maandelijks een voorlopig bedrag afdragen (wordt afgehouden van uw maandelijks nettoloon).
De federale regering heeft beslist om de bijzondere bijdrage van de sociale zekerheid te
verlagen met de bedoeling dit op termijn volledig uit te faseren.
nieuw! Sinds 1 april 2022 is de bijdrage gewijzigd. Concreet zal dit voor de meeste
werknemers resulteren in een lagere maandelijkse inhouding. Er wordt bovendien een
nieuwe categorie ingevoerd: specifiek voor zij die een gemeenschappelijke aanslag
hebben in de personenbelasting (gehuwden of wettelijk samenwonenden) en waarvan
de partner geen beroepsinkomsten heeft.
Verder is de berekeningswijze voor de definitieve bijzondere bijdrage voor de sociale
zekerheid eveneens gewijzigd sinds 1 januari 2022. Deze wijziging is belangrijk omdat
dit zijn effect heeft op de eindafrekening van de personenbelasting.
Er wordt een onderscheid gemaakt tussen een ‘gemeenschappelijk aanslag’ en ‘andere’.
Gemeenschappelijke aanslag (fiscaal gehuwden en wettelijk samenwonenden)
Belastbaar netto-inkomen gezin/jaar

Definitief bedrag BBSZ

< € 18 592,02

€0

> € 18 592,01 – € 21 070,96

5% van het deel > € 18 592,02

> € 21 070,96 – € 60 181,95

€ 123,95 + 1,3% deel > € 21 070,96

> € 60 181,95 – € 74 688,00

€ 632,39

> € 74 688,00 – € 81 944,00

€ 632,39 + 1,3629% deel > € 74 688,00

> € 81 944,00

€ 731,28

Belastinggids 2025 • 73

 Andere (alleenstaanden, feitelijk samenwonenden)
Belastbaar netto-inkomen gezin/jaar

Definitief bedrag BBSZ

< € 18 592,02

€0

> € 18 592,01 – € 21 070,96

5% van het deel > € 18 592,02

> € 21 070,96 – € 37 344,00

€ 123,95 + 1,3% deel > € 21 070,96

> € 37 344,00 – € 40 977,26

€ 335,50 + 4,0090% deel > € 37 344,00

> € 40 977,26 – € 61 191,95

€ 481,96 + 1,2996% deel > € 40 977,26

> € 60 191,95

€ 731,28

14. Gemeente­belasting

Na de zesde staatshervorming kunnen de gemeenten nog steeds hun gemeentelijke
opcentiemen (aanvullende gemeentebelasting) heffen. Het tarief varieert per gemeente
van 0% tot 9%.
Omdat de gemeentelijke opcentiemen berekend worden op zowel het federale als het
gewestelijke deel van de personenbelasting, worden dat dus gedeeltelijk opcentiemen
op opcentiemen.

74 • Belastinggids 2025

 Belastinggids 2025 • 75

 76 • Brochure A5

## V Niet akkoord met de fiscus?
Verweer u!
Wanneer u meent dat de cijfers op uw ontvangen aanslagbiljet niet juist zijn, kan u
hiertegen reageren. U kan eerst proberen uw belastingcontroleur te benaderen en informeel een correctie te vragen. Lukt dit niet dan kan u een bezwaarschrift indienen.
Dit gemotiveerd bezwaarschrift dient u in bij de adviseur-generaal van de administratie
belast met de vestiging van de inkomstenbelastingen in wiens ambtsgebied de aanslag
gevestigd. U doet dit binnen een termijn van zes maanden te rekenen vanaf de datum
van verzending van het aanslagbiljet.
opgelet! Sinds 1 januari 2023 heeft u een jaar tijd in plaats van zes maanden om
in bezwaar te gaan tegen uw aanslagbiljet. De nieuwe bezwaartermijn geldt sinds
1 ­januari 2023 voor alle aanslagen waarvoor de termijn op die dag of later begint, maar
ook voor alle aanslagen waarvoor op 1 januari 2023 de vroegere termijn van zes maanden nog niet voorbij was. De totale termijn kan uiteraard nooit langer zijn dan een jaar.
En als de termijn van zes maanden op 1 januari 2023 reeds verstreken was, kan geen
nieuwe bezwaartermijn starten.
De wet zegt dat u een bezwaarschrift schriftelijk moet indienen maar nergens staat dat
dit aangetekend moet gebeuren. Toch is het raadzaam om dit nog steeds aangetekend
te doen zodat u over een bewijs beschikt. U kan een bezwaarschrift eveneens indienen
per fax of per mail maar de fiscus kan u nadien wel vragen om het origineel ondertekend
door te sturen. Ook kan u een bezwaar indienen via Myminfin (via de tab ‘een klacht
indienen en opvolgen’).
U kan eveneens bemiddeling proberen. Als u een bezwaarschrift heeft ingediend
(of een aanvraag voor ambtshalve ontheffing) kan u ook aankloppen bij de Fiscale
Bemiddelingsdienst. Deze dienst kan tussenkomen wanneer de adviseur-generaal nog geen beslissing heeft genomen. U doet uw aanvraag per post, telefonisch
(02 576 23 60) of via e-mail (fiscaal.bemiddelaars@minfin.fed.be) maar u kan ook ter
plaatse gaan.
Gaat u niet akkoord met de beslissing van de fiscus dan heeft u nog twee beroeps­
mogelijkheden.

Belastinggids 2025 • 77

 Eerste beroepsmogelijkheid
Sinds 1 mei 2018 heeft u de mogelijkheid om aan de adviseur-generaal te vragen om
zijn beslissing te herzien (u draagt dan argumenten aan waarbij u aantoont dat hij zich
heeft vergist). U doet dit binnen de drie maanden (volgend op de derde werkdag nadat
de beslissing werd verstuurd). De adviseur-generaal heeft een maand tijd om u te
antwoorden.
Tweede beroepsmogelijkheid
Komt u niet tot een akkoord dan zal u uw zaak aanhangig moeten maken bij de
rechtbank van eerste aanleg (steeds nadat u reeds een bezwaarschrift of verzoek tot
ambtshalve ontheffing heeft aangevraagd). U richt een officieel verzoek naar de betrokken griffie binnen de drie maanden (volgend op de datum waarop u van de beslissing
in kennis bent gesteld). U kan zich ook richten tot de rechtbank als u na zes maanden
nog geen nieuws heeft ontvangen over uw bezwaarschrift of uw verzoek tot ambtshalve
ontheffing.
Is de termijn van een bezwaarschrift verstreken, dan kan u bij te veel betaalde voorheffingen of voorafbetalingen of bij materiële vergissingen eventueel een ambtshalve
ontheffing vragen bij de adviseur-generaal van de administratie belast met de vestiging
van de inkomstenbelasting. Deze aanvraag moet u indienen binnen 5 jaar vanaf 1 januari van het jaar waarin de aanslag is gevestigd. Dit is ook mogelijk wanneer niet met alle
personen ten laste rekening werd gehouden of wanneer er nieuwe feiten of elementen
aan het licht gekomen zijn.

78 • Belastinggids 2025

 Bijlage: Cijfers in een notendop
Basisbedrag
in euro

Aanslagjaar
2025 in euro

Belastingvrije som
per belastingplichtige ongeacht de hoogte
van het inkomen

4 785

10 570

Verhoging belastingvrije som
1 920

1 kind

870

2 kinderen

2 240

4 950

3 kinderen

5 020

11 090

4 kinderen

8 120

17 940

meer dan 4 kinderen

8 120

17 940

supplement per kind boven vierde

3 100

6 850

kind jonger dan 3 (geen kosten opvang)

325

720

andere persoon ten laste

870

1 920

alleenstaande ouder met kind(eren) ten laste

870

1 920

alleenstaande ouder met laag inkomen, met
kind(eren) ten laste: maximale bijkomende
­belastingvrije som

565

1 250

gehandicapte belastingplichtige

870

1 920

(groot)ouder, broer of zus > 65 j.
(overgangsmaatregel)

1 740

3 850

zorgbehoevende (groot)ouder, broer of zus > 65j.

2 610

5 770

algemeen

1 800

3 980

kinderen ten laste (ongeacht van wie en ongeacht
al dan niet gehandicapt - regeling enkel voor de
aj. 2024 en 2025)

3 300

7 290

Maximum nettobestaansmiddelen

Belastinggids 2025 • 79

 Basisbedrag
in euro

Aanslagjaar
2025 in euro

niet meetellende onderhoudsgelden

1 800

3 980

niet meetellend pensioen

14 500

32 040

niet meetellende studentenarbeid, student-­
zelfstandige en leerling in alternerende opleiding

1 500

3 310

250

550

6 700

13 050

11,20/dag

16,40/dag

minimumbedrag giften

25

40

max. pensioensparen met 30% belastingvermindering
max. pensioensparen met 25% belastingvermindering

625

1 020
1 310

max. uitgaven PWA/dienstencheques
en wijk-werkcheques

920

1 790

adoptiekosten

4 000

6 530

energiebesparende uitgaven voor dakisolatie
(enkel voor Wallonië)

2 000

3 900

25%

0 – 8 120

0 – 15 820

40%

8 120 – 14 330

15 820 – 27 920

45%

14 330 – 24 800

27 920 – 48 320

50%

boven 24 800

boven 48 320

Maximumbedrag aan belastingkrediet voor kind ten laste
maximumbedrag aan belastingkrediet voor kind
ten laste
Huwelijksquotiënt
Huwelijksquotiënt
Belastingverminderingen
kosten kinderopvang

Belastingschijven

80 • Belastinggids 2025

 Basisbedrag
in euro

Aanslagjaar
2025 in euro

Maximumbedragen die recht geven op belastingvermindering voor enige woning
(Woonbonus – voorheen ‘aftrek enige woning’)
Federaal
basisbedrag

1 500

2 450

basisbedrag

1 500

2 280

verhoging basisbedrag tijdens 1ste 10 jaar

500

760

verhoging indien minimum 3 kinderen

50

80

basisbedrag

—

1 520

verhoging basisbedrag tijdens de 1ste 10 jaar

—

760

Verhoging indien minimum 3 kinderen

—

80

basisbedrag

1 500

2 920

verhoging basisbedrag tijdens 1ste 10 jaar

500

970

verhoging indien minimum 3 kinderen

50

100

basisbedrag

1 500

2 290

verhoging basisbedrag tijdens 1ste 10 jaar

500

760

verhoging indien minimum 3 kinderen

50

80

max. belastingvermindering of -krediet

1 520

1 520

extra belastingvermindering of -krediet
(per kind ten laste)

125

125

inkomstengrens: recht op max. chèque

21 000

26 394

max belastbaar inkomen met recht

81 000

101805

Vlaams gewest leningen t.e.m. 2014

Vlaams gewest leningen vanaf 2015 t.e.m. 2019

Brussels gewest leningen t.e.m. 2016

Waals gewest leningen t.e.m. 2015

Waals gewest chèque habitat leningen vanaf 2016

Belastinggids 2025 • 81

 Basisbedrag
in euro

Aanslagjaar
2025 in euro

Maximumbedrag kapitaalaflossingen en levensverzekeringspremies (samen)
Federaal

1 500

2 450

Vlaams gewest

2 021

2 280

Brussels gewest

1 500

2 920

Waals gewest

1 500

2 290

Maximum premies individuele levensverzekeringen en kapitaalaflossingen
(bouwsparen en langetermijnsparen)
Federaal
1ste schijf voor berekening belastingvermindering

1 250

2 040

absoluut maximum

1 500

2 450

1ste schijf voor berekening belastingvermindering

1 250

1 900

absoluut maximum

1 500

2 280

1ste schijf voor berekening belastingvermindering

1 250

1 910

absoluut maximum

1 500

2 290

1ste schijf voor berekening

1 250

2 440

absoluut maximum

1 500

2 920

verenigingswerk (sport en culturele sector)

3 830

7 460

deeleconomie

3 830

7 460

Vlaams gewest

Waals gewest

Brussels gewest

Deeleconomie en verenigingswerk

82 • Belastinggids 2025

 Vind een kantoor in jouw buurt:
www.aclvb.be/nl/secretariaten

Belastinggids 2025 • 83

 www.aclvb.be

 