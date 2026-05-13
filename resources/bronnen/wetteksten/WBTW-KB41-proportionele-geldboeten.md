---
tags: ["VI.B", "2.4"]
itaa-lex-sectie: "VI.B"
wet: "K.B. nr. 41 van 30 januari 1987, tot vaststelling van het bedrag van de proportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "30.01.1987"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 3
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
      sha256: 5f1bad7278d1f8e1f5c00efb5d792f61342d3f7a14a7950caca2937924bfa91c
      version: 06.03.2020
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: d4b4775
    model:
    prompt_version:
  generated_at: '2026-05-13T10:58:06Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T10:59:42Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Zware kolom-bleed door de hele bijlage (Tabellen A-J). Originele PDF heeft een 2-koloms structuur: links de overtredingsbeschrijving, rechts het percentage/boete. De extractie heeft kolomstrooien afwisselend gemerged, met als resultaat scrambled zinnen zoals 'A) belasting en voorschotten waarvan de per maand vertraging (1), een opeisbaarheid blijkt uit de maand- of percentage gelijk aan dat van kwartaalaangiften en belasting waarvan de de nalatigheidsinterest dat is opeisbaarheid blijkt uit de jaaraangiften bepaald in artikel 91, § 1, van het...' (regel 143). Dat is onbruikbaar voor retrieval en evident niet-mens-geschreven. Dit is veruit het zwaarste geval van de batch."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T10:59:42Z'
      rationale: "Zware kolom-bleed door de hele bijlage (Tabellen A-J). Originele PDF heeft een 2-koloms structuur: links de overtredingsbeschrijving, rechts het percentage/boete. De extractie heeft kolomstrooien afwisselend gemerged, met als resultaat scrambled zinnen zoals 'A) belasting en voorschotten waarvan de per maand vertraging (1), een opeisbaarheid blijkt uit de maand- of percentage gelijk aan dat van kwartaalaangiften en belasting waarvan de de nalatigheidsinterest dat is opeisbaarheid blijkt uit de jaaraangiften bepaald in artikel 91, § 1, van het...' (regel 143). Dat is onbruikbaar voor retrieval en evident niet-mens-geschreven. Dit is veruit het zwaarste geval van de batch."
      concrete_problemen:
        - 'Kolom-bleed in heel TABEL A (regels 137-408): elke rij heeft beschrijving + tarief door elkaar gehusseld zonder pipe-syntax'
        - "Voorbeeld scrambled regel 143-145: 'A) belasting en voorschotten waarvan de per maand vertraging (1), een opeisbaarheid blijkt uit de maand- of percentage gelijk aan dat van...'"
        - 'Idem TABEL G (regels 487-700) en alle andere tabellen: zelfde 2-koloms scramble'
        - TOC bovenaan (regels 95-127) lijst alle tabellen op met sub-afdelingen die later opnieuw verschijnen als '## Afdeling 1', '## Afdeling 2' - misleidende heading-hiërarchie
        - "## Afdeling 1 verschijnt zonder body (regel 97) net na 'TABEL A:' titel - geen pipe-tabel maar enkel een rij met de tarief-cellen die als plain text doorlopen"
        - Volledig ontbreken van pipe-tabel markdown; PDF-bullets zoals '- minder dan of gelijk aan 10.000 F nihil' (regel 168) zien er uit als list maar zijn eigenlijk tabel-rijen
        - Vraagteken bij Art. 2 (regel 67) - alleen amendment-blok, geen body (oorspronkelijk opgeheven, OK)
---

# K.B. nr. 41 van 30 januari 1987, tot vaststelling van het bedrag van de proportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 30.01.1987 — gecoördineerde versie.*

Koninklijk besluit nr. 41, van 30 januari 1987, tot vaststelling van het bedrag van de proportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde.
(Uitvoering van de artikelen 70, 71 en 84 van het Wetboek. Officieuze coördinatie)

Laatstelijk gewijzigd, met ingang van 01.04.2019 bij:
- 17 MAART 2019 - Koninklijk besluit tot wijziging van de koninklijke besluiten nrs. 4, 15, 24, 31, 41 en 56 met betrekking tot de belasting over de toegevoegde waarde, met het oog op de automatisering van de uitvoerbare titel inzake de belasting over de toegevoegde waarde (B.S. 08.04.2019, pg. 35699)

### Art. 1
(De tekst van KB nr. 41, artikel 1 is van toepassing met ingang van 01.11.1993 (Art.1, KB 21.10.1993))

De schaal voor de vermindering van de proportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde is bepaald :
1° voor overtredingen begaan vóór 1 november 1993 in tabel A, en voor overtredingen begaan na 31 oktober 1993 in tabel G van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 70, § 1, van het Wetboek van de belasting over de toegevoegde waarde ;
2° voor overtredingen begaan vóór 1 november 1993 in tabel B, en voor overtredingen begaan na 31 oktober 1993 in tabel H van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 70, § 1bis, van hetzelfde Wetboek ;
3° in tabel C van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 70,
§ 2, van hetzelfde Wetboek ;
4° voor overtredingen begaan vóór 1 november 1993 in tabel D, en voor overtredingen begaan na 31 oktober 1993 in tabel I van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 70, § 3, van hetzelfde Wetboek ;
5° in tabel E van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 70,
§ 5, van hetzelfde Wetboek ;
6° voor overtredingen begaan vóór 1 november 1993 in tabel F, en voor overtredingen begaan na 31 oktober 1993 in tabel J van de bijlage bij dit besluit, ten aanzien van overtredingen beoogd in artikel 71 van hetzelfde Wetboek.
De in de tabellen A tot J van de bijlage bij dit besluit opgenomen schaal is echter niet van toepassing ten aanzien van overtredingen begaan met het oogmerk de belasting te ontduiken of de ontduiking ervan mogelijk te maken.

### Art. 2
(De tekst van KB nr. 41, artikel 2, werd opgeheven met ingang van 01.04.2019 (Art. 17, KB 17.03.2019, pg. 35699). Dit besluit (KB 17.03.2019) is niet van toepassing op het dwangbevel dat werd kennisgegeven of betekend vóór de datum van zijn inwerkingtreding – 01.04.2019 (Art. 23, KB 17.03.2019))

### Art. 3
(De tekst van KB nr. 41, artikel 3, is van toepassing met ingang van 01.02.1987 (KB 30.01.1987))

Volledige kwijtschelding van de geldboeten wordt verleend wanneer een schuldenaar zijn toestand spontaan rechtzet vóór enige tussenkomst van een fiscale administratie.

### Art. 4
(Vanaf 01.01.2002 wordt het in KB nr. 41, artikel 4, opgenomen bedrag uitgedrukt in euro. (Art.3, 20 en Art.6, § 14, KB 20.07.2000 en Art.9, KB 13.07.2001))

§ 1. Het totale bedrag van de geldboeten wordt afgerond naar de lagere euro of het tiental euro naargelang het kleiner of groter is dan 250 EUR.

§ 2. Wanneer de geldboete wordt verhoogd overeenkomstig de bepalingen van artikel 2 van dit besluit, wordt het resultaat niet opnieuw afgerond.

### Art. 5

(De tekst van KB nr. 41, artikel 5, is van toepassing met ingang van 01.02.1987 (KB 30.01.1987))

Dit besluit treedt in werking op 1 februari 1987.

### Art. 6

(De tekst van KB nr. 41, artikel 6, is van toepassing met ingang van 01.02.1987 (KB 30.01.1987))

Onze Minister van Financiën is belast met de uitvoering van dit besluit.

Bijlage

TABEL A: Geldboeten voor overtredingen beoogd in artikel 70, § 1, van het wetboek

## Afdeling 1. - Binnenlandse verrichtingen

## Afdeling 2. - Invoer.

## Afdeling 3. - Uitvoer.

TABEL B: Geldboeten voor overtredingen beoogd in artikel 70, § 1bis, van het wetboek

TABEL C: Geldboeten voor overtredingen beoogd in artikel 70, § 2, van het wetboek

TABEL D: Geldboeten voor overtredingen beoogd in artikel 70, § 3, van het wetboek

TABEL E: Geldboeten voor overtredingen beoogd in artikel 70, § 5, van het wetboek

TABEL F: Geldboeten voor overtredingen beoogd in artikel 71 van het wetboek

TABEL G: Geldboeten voor overtredingen beoogd in artikel 70, § 1, van het wetboek

## Afdeling 1.- Binnenlandse en intracommunautaire verrichtingen.

## Afdeling 2.- Invoer.

## Afdeling 3.- Uitvoer.

## Afdeling 4.- Andere regeling van entrepot dan douane-entrepot.

TABEL H: Geldboeten voor overtredingen beoogd in artikel 70, § 1bis, van het wetboek

TABEL I: Geldboeten voor overtredingen beoogd in artikel 70, § 3, van het wetboek

TABEL J: Geldboeten voor overtredingen beoogd in artikel 71 van het wetboek

BIJLAGE

TABEL A

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 1, VAN HET WETBOEK

Eerste afdeling. - Binnenlandse verrichtingen.
(KB nr. 41, Tabel A, afdeling 1, I, 1. A) en 2. B), werden gewijzigd met ingang van 01.04.2019 (KB 17.03.2019, B.S. 08.04.2019, pg. 35699))

I. Niet-betaling en niet-tijdige betaling van de belasting of van de voorschotten waarvan de opeisbaarheid blijkt uit de ingediende periodieke btw-aangiften of uit het opstellen van de bijzondere rekening.

1. Overtreding vastgesteld door het C.I.V. (computer) betreffende :

A) belasting en voorschotten waarvan de per maand vertraging (1), een opeisbaarheid blijkt uit de maand- of percentage gelijk aan dat van kwartaalaangiften en belasting waarvan de de nalatigheidsinterest dat is opeisbaarheid blijkt uit de jaaraangiften bepaald in artikel 91, § 1, van het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

B) voorschotten waarvan de opeisbaarheid blijkt 500 F per voorschot uit de jaaraangiften

2. Overtreding waarvoor de btw-hoofdcontroleur eenbericht stuurt betreffende :

A) belasting waarvan de opeisbaarheid blijkt uit de 10 pct. van de verschuldigde ingediende periodieke aangiften of uit het belasting opstellen van de bijzondere rekening

B) voorschotten verschuldigd door belasting- per maand vertraging (1), een plichtigen gehouden tot het indienen van percentage gelijk aan dat van maand- of kwartaalaangiften de nalatigheidsinterest dat is bepaald in artikel 91, § 1, van het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

C) voorschotten verschuldigd door belasting- 500 F per voorschot plichtigen gehouden tot het indienen van jaaraangiften

II. Onjuistheden vastgesteld bij het nazicht van de boekhouding met betrekking tot de wiskundige juistheid ervan en de juiste toepassing van de btw ;

niet-betaling of niet-tijdige betaling van de belasting wanneer de betaling moet worden verricht door de medecontractant gehouden tot het indienen van periodieke aangiften ;

niet-betaling of niet-tijdige betaling van de belasting wanneer deze moet worden voldaan op grond van een bijzondere aangifte ;

niet-toepassing van artikel 17bis van het koninklijk besluit nr.
1 van 23 juli 1969 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde.

(1) Ieder begonnen tijdvak van een maand wordt voor een gehele maand gerekend.

Het bedrag van de verschuldigde belasting voor een controleperiode van één jaar (2) is :

- minder dan of gelijk aan 10.000 F nihil

- van 10.001 F tot 50.000 F 5 pct. van de verschuldigde belasting

- meer dan 50.000 F 10 pct. van de verschuldigde belasting

III. Ten onrechte toepassen van artikel 17bis van het in rubriek II 20 pct. van de verschuldigde hierboven genoemd koninklijk besluit nr. 1 belasting

IV. Onjuistheden vastgesteld bij het nazicht van de boekhouding met betrekking tot de inhoud ervan ;

niet-betaling van de belasting vastgesteld naar aanleiding van een controle bij belastingplichtigen die hun periodieke btwaangiften niet indienen.

Het bedrag van de verschuldigde belasting voor een controleperiode van één jaar (2) is :

- minder dan of gelijk aan 50.000 F 10 pct. van de verschuldigde belasting

- meer dan 50.000 F 20 pct. van de verschuldigde belasting

V. Terug te storten belasting wegens het niet overleggen van 10 pct. van de terug te storten het teruggaafregister of het niet inschrijven in dat register belasting van een verbeterend stuk

VI. Vrijstellingen beoogd door artikel 42, §§ 1, 2 en 3, 1° tot 6°, van het Wetboek.

1. Vrijstelling ten onrechte toegepast of erop aanspraak gemaakt.

A. Zonder normaal de juistheid ervan te kunnen nihil nagaan, heeft de belastingplichtige de vrijstelling toegepast op grond van onjuiste inlichtingen verstrekt door zijn medecontractant

B. Andere gevallen 10 pct. van de verschuldigde belasting

2. Ontbreken van het bewijs van het recht op vrijstelling 10 pct. van de verschuldigde belasting

## Afdeling 2. - Invoer.

VII. Overtredingen van de verplichting de goederen aan te geven bij het douanekantoor : invoer van goederen zonder aangifte of niet-aangifte van een gedeelte van de ingevoerde goederen.

1. De waarde van de niet aangegeven goederen bedraagt 50 pct. van de verschuldigde niet meer dan 30.000 F en de ontdoken btw bedraagt belasting niet meer dan 6.000 F

2. De waarde van de niet aangegeven goederen bedraagt 100 pct. van de verschuldigde niet meer dan 150.000 F en de ontdoken btw bedraagt belasting niet meer dan 30.000 F

(2) Om het bedrag van de voor de periode van één jaar verschuldigde belasting te berekenen, wordt het totaal van de verschuldigde belasting gedeeld door het aantal gecontroleerde jaren.

3. Andere gevallen 200 pct. van de verschuldigde belasting

VIII. Overtredingen van de verplichting de goederen aan te geven met naleving van de voorwaarden bepaald in artikel 51 van het Wetboek, andere dan deze beoogd in rubriek VII hierboven.

1. Overtredingen in verband met het bedrag van de belasting die voor de aangegeven goederen verschuldigd is.

A. Louter toevallige vergissingen ten aanzien van 10 pct. van de aanvullende de vermelding van de prijs of de bij de prijs te belasting met minimum van voegen kosten 500 F per document

B. Andere vergissingen ten aanzien van de zie tabel D, 2 vermelding van de prijs of de bij de prijs te voegen kosten

C. Andere vergissingen, inzonderheid betreffende :

- de omrekening in Belgische frank of in euro van de elementen die tot de maatstaf van heffing behoren ;

- het tarief van de btw en/of de egalisatiebelasting ;

- de maatstaf van heffing ;

- het bedrag van de verschuldigde belasting ;

- het vaststellen van de normale waarde ;

- de minimummaatstaf van heffing 10 pct. van de aanvullende belasting met minimum van 500 F per document

2. Louter toevallige overtredingen met betrekking tot het 10 pct. van de aanvullende aangeven van de aard of de hoeveelheid van de belasting met minimum van ingevoerde goederen 500 F per document

3. Andere overtredingen met betrekking tot het zie tabel D, 4 aangeven van de aard of de hoeveelheid van de ingevoerde goederen

4. Louter toevallige overtredingen met betrekking tot het 10 pct. van de ontdoken uitvoeren van de bij invoer te vervullen formaliteiten, belasting daaronder begrepen die ten aanzien van het vermelden van het registratienummer, de naam en het adres van degene op wiens naam de terzake van invoer verschuldigde belasting mag of moet worden voldaan

5. Andere overtredingen met betrekking tot het uitvoeren 200 pct. van de ontdoken van de bij invoer te vervullen formaliteiten, daaronder belasting begrepen die ten aanzien van het vermelden van het registratienummer, doch met uitzondering van deze ten aanzien van de vermelding van de naam en het adres van degene op wiens naam de ter zake van invoer verschuldigde belasting mag of moet worden voldaan

6. Andere overtredingen met betrekking tot het uitvoeren zie tabel D, 6 van de bij invoer te vervullen formaliteiten ten aanzien van het vermelden van de naam en het adres van degene op wiens naam de terzake van invoer verschuldigde belasting mag of moet worden voldaan

7. Overtredingen in verband met het weekkrediet 1 pct. van de verschuldigde belasting per maand vertraging
(3)

8. Misbruik van vrijstelling met betrekking tot goederen 50 pct. van de verschuldigde ingevoerd onder een regeling inzake doorvoer, belasting entrepot of tijdelijke opslag

9. Overtredingen ten aanzien van de regeling van de verlegging van de heffing beoogd in artikel 4, § 3, of in artikel 7 van het koninklijk besluit nr. 7 van 27 december 1977 met betrekking tot de invoer van goederen voor de toepassing van de belasting over de toegevoegde waarde.

A. Overtredingen in verband met het opnemen 10 pct. van de verschuldigde van de belasting verschuldigd voor de belasting aangegeven goederen in de periodieke btwaangifte

B. Niet-tijdige betaling van de vooruit te betalen belasting :

1° foute berekening van de vooruit te 2 pct. per maand vertraging (3) betalen belasting bij de aanvraag van de van de ontdoken vooruit te vergunning, wegens het verstrekken van betalen belasting onvolledige of onjuiste inlichtingen, of bij de jaarlijkse herziening

2° niet-betaling van de aanvullende, 1 pct. per maand vertraging (3) uiterlijk op 20 april vooruit te betalen van de aanvullende vooruit te belasting betalen belasting

IX. Overtredingen met betrekking tot de vrijstellingen beoogd 10 pct. van de verschuldigde door artikel 42, §§ 1, 2 en 3, 1° tot 6°, van het Wetboek belasting

X. Overtredingen op het stuk van de tijdelijke invoer van vervoermiddelen.

1. Vervoermiddel regelmatig ingevoerd met tijdelijke vrijstelling en uitzonderlijk ter beschikking gesteld van een persoon met normale verblijfplaats in België; misbruik van vrijstelling.

A. Eerste overtreding :

1° wegens het niet kennen van de nihil wetgeving

2° andere 10 pct. van de verschuldigde belasting

B. Tweede overtreding 20 pct. van de verschuldigde belasting

C. Volgende overtredingen 100 pct. van de verschuldigde belasting

2. Vervoermiddel dat niet kan worden ingevoerd met tijdelijke vrijstelling.

A. De invoerder heeft zonder enige twijfel zijn normale verblijfplaats in België en

1° doet spontaan aangifte nihil

2° heeft geen frauduleuze bedoelingen 10 pct. van de verschuldigde belasting

(3) Ieder begonnen tijdvak van een maand wordt voor een gehele maand gerekend.

3° de frauduleuze bedoeling is niet volledig 100 pct. van de verschuldigde uit te sluiten belasting

B. De invoerder heeft zijn normale verblijfplaats in nihil
België maar kan te goeder trouw oordelen dat deze zich in het buitenland bevindt

## Afdeling 3. – Uitvoer.

XI. Overtredingen inzake de toepassing van artikel 39 van het
Wetboek.

1. Het bewijs van het recht op vrijstelling wordt niet 10 pct. van de verschuldigde geleverd belasting

2. Overtredingen in verband met in entrepot opgeslagen goederen.

De hier bedoelde overtredingen zijn de volgende :

A. uitslag uit entrepot voor de binnenlandse markt 5 pct. van de verschuldigde van goederen die voorheen van het binnenland belasting naar een entrepot werden vervoerd, zonder dat de regularisatie van de eventueel eisbare belasting heeft plaatsgehad

B. gebrek aan regularisatie opgelegd voor 5 pct. van de verschuldigde diensten met betrekking tot goederen in belasting entrepot die later werden uitgeslagen uit entrepot ter bestemming van de persoon voor wiens rekening deze diensten werden verricht

3. Overtredingen inzake het stelsel van entrepot ander dan douane-entrepot.

A. Een vergunning werd ten onrechte verleend, op 20 pct. van de belasting grond van door de aanvrager verstrekte waarvan de vrijstelling ten verkeerde inlichtingen onrechte is verkregen

B. Overtredingen in verband met de toepassing van de voorwaarden van de vergunning :

1° op de vergunning is aanspraak gemaakt 10 pct. van de belasting voor handelingen waarvoor ze niet van waarvan de vrijstelling ten toepassing is onrechte is verkregen

2° het vergelijkingsregister of de 20 pct. van de belasting boekhouding die ter controle van de waarvan de vrijstelling is vrijstelling wordt voorgeschreven is niet verkregen gehouden of is gehouden op zodanige wijze dat deze controle zeer moeilijk is.
De vergunninghouder voldoet niet aan het verzoek van de controlerende ambtenaar om het register of de boekhouding binnen een redelijke termijn aan te leggen of aan te passen

3° de uitvoer heeft niet plaats binnen de in de vergunning gestelde termijn of de goederen werden vóór het verstrijken van die termijn uit het entrepot ander dan douane-entrepot geslagen met een ander doel dan de uitvoer :

a) de houder van de vergunning 10 pct. van de te regulariseren heeft de regularisatie gedaan in belasting overeenstemming met de voorwaarden van de vergunning

b) de houder van de vergunning 20 pct. van de te regulariseren heeft op het tijdstip van de belasting controle de verplicht geworden regularisatie nog niet uitgevoerd

4. Overtredingen in verband met de toepassing van de vergunning beoogd in artikel 14 van het koninklijk besluit nr. 18 van 27 december 1977 met betrekking tot de vrijstellingen ten aanzien van de uitvoer van goederen en diensten, op het stuk van de belasting over de toegevoegde waarde, ter uitvoering van artikel 39, § 3, van het Wetboek.

A. Op de vergunning is aanspraak gemaakt voor 10 pct. van de belasting handelingen waarvoor ze niet van toepassing is waarvan de opschorting ten onrechte is verkregen

B. De goederen krijgen vóór het verstrijken van de voor de opschorting toegestane termijn een andere bestemming dan die toepasselijk inzake opschorting :

1. de vergunninghouder heeft de daarvoor nihil voorgeschreven regularisatie uitgevoerd in overeenstemming met de voorwaarden van de vergunning

2. de vergunninghouder heeft op het 10 pct. van de verschuldigde tijdstip van de controle de verplicht belasting geworden regularisatie nog niet uitgevoerd

C. De opgelegde formaliteiten om de verlenging te verkrijgen van de termijn van opschorting van de belasting zijn niet vervuld :

1° de vergunninghouder heeft de daarvoor 10 pct. van de verschuldigde voorgeschreven regularisatie uitgevoerd belasting met een maximum in overeenstemming met de voor- van 5.000 F per oorzaak van waarden van de vergunning verschuldigdheid van de belasting

2° de vergunninghouder heeft op het 10 pct. van de verschuldigde tijdstip van de controle de verplicht belasting met een maximum geworden regularisatie nog niet van 5.000 F per oorzaak van uitgevoerd verschuldigdheid van de belasting in geval de goederen zijn uitgevoerd

XII. Overtredingen inzake de toepassing van artikel 40, § 1, 3°, b, van het Wetboek.

1. Overtredingen in verband met de uitreiking van de vergunning.

A. De houder van een vergunning, die bovendien 10 pct. van de belasting geen recht meer had op de vrijstelling, heeft waarvan de vrijstelling ten zich verder beroepen op de vergunning zonder onrechte is verkregen daarvoor de vernieuwing te hebben aangevraagd

B. De vergunning is ten onrechte verleend op 10 pct. van de belasting grond van door de aanvrager verstrekte waarvan de vrijstelling ten verkeerde inlichtingen onrechte is verkregen

2. Overtredingen in verband met de toepassing van de voorwaarden van de vergunning.

A. Op de vergunning is aanspraak gemaakt voor handelingen waarvoor ze niet van toepassing is:

1° de belasting waarvan de vrijstelling ten 5 pct. van de belasting onrechte is verkregen, is aftrekbaar waarvan de vrijstelling ten onrechte is verkregen

2° de belasting waarvan de vrijstelling ten 10 pct. van de belasting onrechte is verkregen, is niet aftrekbaar waarvan de vrijstelling ten onrechte is verkregen

B. Het vergelijkingsregister of de boekhouding die 10 pct. van de belasting voor de controle van de vrijstelling wordt waarvan de vrijstelling is voorgeschreven, is niet gehouden of is verkregen gehouden op zodanige wijze dat deze controle zeer moeilijk is. De vergunninghouder voldoet niet aan het verzoek van de controlerende ambtenaar om het register of de boekhouding binnen een redelijke termijn aan te leggen of aan te passen

C. De goederen, die met vrijstelling van de belasting ingevoerd zijn om een loonbewerking te ondergaan, zijn niet uitgevoerd binnen de door de vergunning bepaalde termijn :

1° de houder van de vergunning is een belastingplichtige die gehouden is tot indiening van periodieke btw-aangiften en

a) heeft een regularisatie gedaan in 1 pct. van de belasting overeenstemming met de waarvan de vrijstelling bij voorwaarden van de vergunning invoer is verkregen

b) heeft op het tijdstip van de 3 pct. van de belasting controle nog niet de verplicht waarvan de vrijstelling bij geworden regularisatie uitgevoerd invoer is verkregen

2° de houder van de vergunning is een niet-belastingplichtige of een belastingplichtige die niet gehouden is tot indiening van periodieke btw-aangiften en

a) heeft een regularisatie gedaan in 10 pct. van de belasting overeenstemming met de waarvan de vrijstelling bij voorwaarden van de vergunning invoer is verkregen

b) heeft op het tijdstip van de 20 pct. van de belasting controle nog niet de verplicht waarvan de vrijstelling bij geworden regularisatie uitgevoerd invoer is verkregen

XIII. Overtredingen inzake de toepassing van artikel 42, § 3, 8°, van het Wetboek.

1. Een vergunning is verleend op grond van door de 20 pct. van de belasting aanvrager verstrekte verkeerde inlichtingen waarvan de vrijstelling is verkregen

2. Overtredingen in verband met de toepassing van de vergunning.

A. Op de vergunning is aanspraak gemaakt voor 10 pct. van de belasting handelingen waarvoor ze niet van toepassing is waarvan de vrijstelling ten onrechte is verkregen

B. Het vergelijkingsregister of de boekhouding die 20 pct. van de belasting ter controle van de vrijstelling wordt waarvan de vrijstelling is voorgeschreven is niet gehouden of is verkregen gehouden op zodanige wijze dat deze controle zeer moeilijk is. De vergunninghouder voldoet niet aan het verzoek van de controlerende ambtenaar om het register of de boekhouding binnen een redelijke termijn aan te leggen of

aan te passen

C. De goederen worden niet uitgevoerd binnen de in de vergunning bepaalde termijn en

1° de vergunninghouder heeft de daarvoor 10 pct. van de te regulariseren voorgeschreven regularisatie uitgevoerd belasting in overeenstemming met de voorwaarden van de vergunning

2° op het tijdstip van de controle heeft de 20 pct. van de te regulariseren vergunninghouder de verplicht geworden belasting regularisatie nog niet uitgevoerd

XIV. Overtredingen in verband met de toepassing van artikel 43 van het Wetboek.

1. Overtredingen in verband met de uitreiking van de vergunning.

A. De belastingplichtige heeft zich verder 10 pct. van de belasting beroepen op een vroeger verleende vergunning waarvan de vrijstelling ten waarvoor hij nagelaten heeft de vernieuwing onrechte is verkregen aan te vragen ; daarenboven had hij geen recht meer op vrijstelling of slechts recht op een lager percentage

B. Een vergunning is verleend op grond van door 10 pct. van de belasting de belastingplichtige verstrekte verkeerde waarvan de vrijstelling ten inlichtingen ; daarenboven is, ten gevolge van onrechte is verkregen deze onjuiste verklaring, de vergunning ten onrechte verleend of werd een percentage van vrijstelling vermeld dat hoger is dan dat waarop de belastingplichtige recht heeft

2. Overtredingen in verband met de toepassing van de voorwaarden van de uitgereikte vergunning.

A. Aanspraak op de vergunning is gemaakt voor handelingen die zijn uitgesloten van het voordeel van de vrijstelling en

1° de belasting waarvan de vrijstelling ten 5 pct. van de belasting onrechte is verkregen is aftrekbaar waarvan de vrijstelling ten onrechte is verkregen

2° de belasting waarvan de vrijstelling ten 10 pct. van de belasting onrechte is verkregen is niet aftrekbaar waarvan de vrijstelling ten onrechte is verkregen

B. De boekhouding die voor de controle van de 10 pct. van de belasting vrijstelling wordt voorgeschreven is niet waarvan de vrijstelling is gehouden of is gehouden op zodanige wijze dat verkregen deze controle zeer moeilijk is. De belastingplichtige voldoet niet aan het verzoek van de controlerende ambtenaar om de boekhouding binnen een redelijke termijn aan te leggen of aan te passen

C. De belastingplichtige heeft aanspraak gemaakt op de vrijstelling voor een groter bedrag dan dat waarop hij recht heeft en

1° heeft een regularisatie gedaan in 1 pct. van de te regulariseren overeenstemming met de voorwaarden belasting van de vergunning

1° heeft op het tijdstip van de controle de 3 pct. van de te regulariseren verplicht geworden regularisatie nog niet belasting uitgevoerd

TABEL B

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 1BIS, VAN HET WETBOEK

Ten onrechte afgetrokken belasting.

Het bedrag van de verkeerdelijk in aftrek gebrachte belasting voor een controleperiode van één jaar (4) is :

- minder dan of gelijk aan 10.000 F nihil

- van 10.001 F tot 50.000 F 5 pct. van de verkeerdelijk in aftrek gebrachte belasting

- meer dan 50.000 F 10 pct. van de verkeerdelijk in aftrek gebrachte belasting

TABEL C

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 2, VAN HET WETBOEK

I. Niet-uitreiken van facturen of van als zodanig geldende stukken :

1) dat geen verschuldigdheid van btw tot gevolg heeft 60 pct. van de op de handelingen verschuldigde belasting

2) dat verschuldigdheid van btw tot gevolg heeft 100 pct. van de op de handelingen verschuldigde belasting

II. Ontbreken van of onjuistheden in de vermeldingen aan te 100 pct. van de op de brengen op de facturen of op de als zodanig geldende handelingen verschuldigde bestukken lasting

TABEL D

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 3, VAN HET WETBOEK

Overtredingen van de verplichting de goederen aan te geven met naleving van de voorwaarden bepaald in artikel 51 van het Wetboek.

1. Louter toevallige vergissingen ten aanzien van de vermelding zie tabel A, VIII, 1, A van de prijs of de bij de prijs te voegen kosten

2. Andere vergissingen ten aanzien van de vermelding van de 200 pct. van de op de prijs of de bij de prijs te voegen kosten handeling verschuldigde belasting

3. Louter toevallige overtredingen met betrekking tot het zie tabel A, VIII, 2 aangeven van de aard of de hoeveelheid van de ingevoerde goederen

(4) Om het bedrag van de voor de periode van één jaar verkeerdelijk in aftrek gebrachte belasting te berekenen, wordt het totaal van de verkeerdelijk in aftrek gebrachte belasting gedeeld door het aantal gecontroleerde jaren.

4. Andere overtredingen met betrekking tot het aangeven van 200 pct. van de op de de aard of de hoeveelheid van de ingevoerde goederen handeling verschuldigde belasting

5. Louter toevallige overtredingen met betrekking tot het zie tabel A, VIII, 4 uitvoeren van de bij invoer te vervullen formaliteiten

6. Andere dan louter toevallige overtredingen met betrekking tot 200 pct. van de op de het uitvoeren van de bij invoer te vervullen formaliteiten ten handeling verschuldigde belasaanzien van de vermelding van de naam en het adres van ting degene op wiens naam de terzake van invoer verschuldigde belasting mag of moet worden voldaan

7. Andere dan louter toevallige overtredingen met betrekking tot zie tabel A, VIII, 5 het uitvoeren van de bij invoer te vervullen formaliteiten, daaronder begrepen die ten aanzien van het vermelden van het registratienummer, doch met uitzondering van deze ten aanzien van de vermelding van de naam en het adres van degene op wiens naam de terzake van invoer verschuldigde belasting mag of moet worden voldaan

TABEL E

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 5, VAN HET WETBOEK

Ontoereikende maatstaf van heffing ten aanzien van vervreemdingen van gebouwen en van werk in onroerende staat.

Het bedrag van het tekort in de maatstaf van heffing, in verhouding tot het bedrag waarover de btw is voldaan, is :

- groter dan 1/8, zonder meer te bedragen dan 1/4 10 pct. van de verschuldigde belasting

- groter dan 1/4, zonder meer te bedragen dan 1/2 20 pct. van de verschuldigde belasting

- groter dan 1/2, zonder meer te bedragen dan 1/1 25 pct. van de verschuldigde belasting

- groter dan 1/1 35 pct. van de verschuldigde belasting

TABEL F

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 71 VAN HET WETBOEK

Vermelding op de bij uitvoer of tot staving ervan overgelegde 10 pct. van de overeenkomstig stukken, hetzij van een grotere hoeveelheid goederen dan de artikel 71 van het Wetboek werkelijk uitgevoerde hoeveelheid, hetzij van een hogere prijs of berekende belasting die waarde dan de werkelijke prijs of waarde van de uitgevoerde verschuldigd zou zijn geweest goederen, hetzij van de uitgevoerde goederen onder een valse benaming

TABEL G

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 1, VAN HET WETBOEK

Eerste afdeling.- Binnenlandse en intracommunautaire verrichtingen.
(KB nr. 41, Tabel G, afdeling 1, I, werd gewijzigd met ingang van 01.04.2019 (KB 17.03.2019, B.S. 08.04.2019, pg. 35699))

I. Niet-betaling en niet-tijdige betaling van de belasting of van per maand vertraging (5), een de voorschotten waarvan de opeisbaarheid blijkt uit de percentage gelijk aan dat van ingediende periodieke aangifte bedoeld in artikel 53, § 1, de nalatigheidsinterest dat is eerste lid, 2°, van het Wetboek, of uit het opstellen van de bepaald in artikel 91, § 1, van bijzondere rekening. het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

1. Overtreding vastgesteld door het C.I.V. betreffende belasting en voorschotten waarvan de opeisbaarheid blijkt uit de maand- of kwartaalaangiften bedoeld in artikel 53, § 1, eerste lid, 2°, van het Wetboek

2. Overtreding waarvoor de btw-hoofdcontroleur een bericht stuurt betreffende :

A) belasting waarvan de opeisbaarheid blijkt uit de 15 pct. van de verschuldigde ingediende periodieke aangiften bedoeld in belasting artikel 53, § 1, eerste lid, 2°, van het Wetboek, of uit het opstellen van de bijzondere rekening

B) voorschotten verschuldigd door belasting- per maand vertraging (5), een plichtigen gehouden tot het indienen van percentage gelijk aan dat van maand- of kwartaalaangiften bedoeld in artikel de nalatigheidsinterest dat is 53, § 1, eerste lid, 2°, van het Wetboek bepaald in artikel 91, § 1, van het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

(KB nr. 41, Tabel G, afdeling 1, Ibis, werd ingevoegd met ingang van 20.07.2015 (KB 05.07.2015, B.S. 10.07.2015, pg. 45614))

Ibis. Gehele of gedeeltelijke niet-betaling of niet-tijdige betaling 10 pct. van de verschuldigde van de belasting waarvan de opeisbaarheid blijkt uit de belasting ingediende aangifte met betrekking tot de Mini One Stop Shop bedoeld in de artikelen 58ter, § 5 en 58quater, § 5, van het Wetboek, die nog verschuldigd blijft de tiende van de tweede maand die volgt op het kalenderkwartaal waarvoor de voormelde aangifte werd ingediend.

II. Gehele of gedeeltelijke niet-betaling of niet-tijdige betaling 10 pct. van de verschuldigde van de belasting waarvan de opeisbaarheid blijkt uit de belasting ingediende bijzondere aangifte bedoeld in artikel 53ter, 1°, van het Wetboek, die nog verschuldigd blijft de 20ste van de tweede maand die volgt op het kalenderkwartaal waarvoor de voormelde aangifte werd ingediend

III. Gehele of gedeeltelijke niet-betaling of niet-tijdige betaling van de belasting verschuldigd ter zake van de intracommunautaire verwerving van :

- vervoermiddelen ten aanzien waarvan de bijzondere aangifte bedoeld in artikel 53nonies, § 1, van het Wetboek, werd ingediend ;

- accijnsproducten als bedoeld in artikel 58, § 1bis, van 10 pct. van de verschuldigde het Wetboek belasting

(5) Ieder begonnen tijdvak van een maand wordt voor een gehele maand gerekend.

IV. Gebrekkige toepassing van de btw-reglementering, andere dan die hierna aangeduid, vastgesteld bij het nazicht van de voorgelegde boeken en stukken.

Het bedrag van de verschuldigde belasting voor een controleperiode van één jaar (6) is :

- minder dan of gelijk aan 1.250 EUR 5 pct. van de verschuldigde belasting

- meer dan 1.250 EUR 10 pct. van de verschuldigde belasting

Ten onrechte toepassen van :

- artikel 51, § 2, van het Wetboek ;

- artikel 20 van het koninklijk besluit nr. 1 van 29 20 pct. van de verschuldigde december 1992 met betrekking tot de regeling voor de belasting voldoening van de belasting over de toegevoegde waarde

V. Onjuistheden vastgesteld bij het nazicht van de boekhouding met betrekking tot de inhoud ervan ;

belastbare handelingen zijn niet, slechts gedeeltelijk, of zijn laattijdig opgenomen in de daartoe bestemde aangifte ;

de persoon die niet gehouden is tot het indienen van een aangifte laat na de belasting binnen de vereiste termijn en op de voorgeschreven wijze te betalen.

Het bedrag van de verschuldigde belasting voor een controleperiode van één jaar (7) is :

- minder dan of gelijk aan 1.250 EUR 10 pct. van de verschuldigde belasting

- meer dan 1.250 EUR 20 pct. van de verschuldigde belasting

VI. Terug te storten belasting wegens het niet overleggen van 10 pct. van de terug te storten het teruggaafregister of het niet inschrijven in dat register belasting van een verbeterend stuk

VII. 1. Ten onrechte toepassen van artikel 25ter, § 1, tweede 10 pct. van de verschuldigde lid, 1°, van het Wetboek belasting

2. Overtredingen begaan bij de toepassing van artikel
39bis, 39ter en 42, §§ 1, 2 en 3, 1° tot 6°, van het
Wetboek.

A) Vrijstelling ten onrechte toegepast of 10 pct. van de verschuldigde ingeroepen belasting

B) Het bewijs van het recht op vrijstelling wordt 10 pct. van de verschuldigde niet geleverd belasting

(6) Indien de controleperiode korter of langer is dan één jaar wordt het bedrag van 1.250 EUR proportioneel verminderd of verhoogd.
(7) Indien de controleperiode korter of langer is dan één jaar wordt het bedrag van 1.250 EUR proportioneel verminderd of verhoogd.

## Afdeling 2.- Invoer.

(KB nr. 41, Tabel G, afdeling 2, VIII, 4. en 5. C), werden gewijzigd met ingang van 01.04.2019 (KB 17.03.2019, B.S. 08.04.2019, pg. 35699))

VIII. Overtredingen van de verplichting de goederen aan te geven en de belasting te voldoen met naleving van de voorwaarden bepaald in artikel 52 van het Wetboek.

1. Invoer van goederen zonder aangifte of niet-aangifte van een gedeelte van de ingevoerde goederen.

A) De niet aangegeven goederen zijn bedrijfs- 25 pct. van de verschuldigde middelen belasting

B) De niet-aangifte heeft betrekking op andere goederen.

Het bedrag van de verschuldigde belasting is :

- minder dan of gelijk aan 1.250 EUR 50 pct. van de verschuldigde belasting

- meer dan 1.250 EUR 100 pct. van de verschuldigde belasting

2. Overtredingen in verband met het bedrag van de belasting die voor de aangegeven goederen verschuldigd is ; worden hier inzonderheid bedoeld de vergissingen betreffende :

- de bepaling van de maatstaf van heffing ;

- de omrekening in Belgische frank of in euro van de elementen die tot de maatstaf van heffing behoren ;

- het tarief van de btw ;

- het bedrag van de verschuldigde belasting.

A) Louter toevallige overtredingen (8).

Het bedrag van de bijkomende belasting is :

- minder dan of gelijk aan 1.250 5 pct. van de bijkomende
EUR belasting

- meer dan 1.250 EUR 10 pct. van de bijkomende belasting

B) Andere overtredingen.

1° Vergissingen in verband met de zie tabel I, 2 vermelding van de prijs of het toebehoren ervan

2° Andere vergissingen 50 pct. van de bijkomende belasting

(8) Moet onder "louter toevallige overtredingen" worden verstaan, de onregelmatigheden die te wijten zijn aan onwetendheid, vergissingen of nalatigheid en waarbij aan de goede trouw van de overtreder niet kan worden getwijfeld.

3. Overtredingen inzake het aangeven van de aard of de hoeveelheid van de ingevoerde goederen.

A) Louter toevallige overtredingen (8).

Het bedrag van de bijkomende belasting is :

- minder dan of gelijk aan 1.250 EUR 5 pct. van de bijkomende belasting

- meer dan 1.250 EUR 10 pct. van de bijkomende belasting

B) Andere overtredingen zie tabel I, 1

4. Overtredingen in verband met het weekkrediet per maand vertraging (9), een percentage gelijk aan dat van de nalatigheidsinterest dat is bepaald in artikel 91, § 1, van het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

5. Overtredingen in verband met de regeling van de verlegging van de heffing bedoeld in artikel 5, § 3, van het koninklijk besluit nr. 7 van 29 december 1992 met betrekking tot de invoer van goederen voor de toepassing van de belasting over de toegevoegde waarde.

A) Overtredingen in verband met het ten onrechte 5 pct. van de belasting toepassen of inroepen van de verleggings- waarvoor de verleggingsregeling regeling onrechtmatig werd toegepast of ingeroepen

B) Overtredingen in verband met het opnemen van de belasting verschuldigd voor de aangegeven goederen in de periodieke btwaangifte.

1° De verschuldigde belasting is volledig 50 EUR voor het geheel van de aftrekbaar overtredingen vastgesteld tijdens eenzelfde controle

2° De verschuldigde belasting is niet of slechts gedeeltelijk aftrekbaar en het bedrag van de niet aftrekbare belasting voor een controleperiode van één jaar
(10) is :

- minder dan of gelijk aan 1.250 5 pct. van de niet aftrekbare
EUR verschuldigde belasting

- meer dan 1.250 EUR 10 pct. van de niet aftrekbare verschuldigde belasting

C) Niet-tijdige betaling van de vooruit te betalen per maand vertraging (11), een belasting percentage gelijk aan dat van de nalatigheidsinterest dat is bepaald in artikel 91, § 1, van het Wetboek, te berekenen over het verschuldigde of nog verschuldigde bedrag

(9) Ieder begonnen tijdvak van een maand wordt voor een gehele maand gerekend.
(10) Indien de controleperiode korter of langer is dan één jaar wordt het bedrag van 1.250 EUR proportioneel verminderd of verhoogd.
(11) Ieder begonnen tijdvak van een maand wordt voor een gehele maand gerekend.

6. Laattijdige voldoening van de belasting ingevolge 10 pct. van de verschuldigde overtredingen in verband met de opschortende belasting douaneregelingen bedoeld in artikel 23, §§ 4 en 5, van het Wetboek, en de opschortende fiscale regelingen bedoeld in § 5 van hetzelfde artikel

IX. Overtredingen met betrekking tot de vrijstellingen bedoeld in 10 pct. van de verschuldigde artikel 40, § 1, 1° en 2°, en § 4, van het Wetboek belasting

X. Onregelmatigheden met betrekking tot de vrijstellingen 10 pct. van de verschuldigde bedoeld in artikel 40, § 1, 1°, a, van het Wetboek, voor de belasting invoer van goederen bedoeld in artikel 42, §§ 1 en 2, van het Wetboek, en onregelmatigheden met betrekking tot de vrijstellingen bedoeld in artikel 42, § 3, 1° tot 6°, van het Wetboek

XI. Overtredingen op het stuk van de tijdelijke invoer van vervoermiddelen.

1. Vervoermiddel regelmatig ingevoerd met tijdelijke vrijstelling en uitzonderlijk ter beschikking gesteld van een persoon met normale verblijfplaats in België ;

misbruik van vrijstelling.

A) Eerste overtreding 10 pct. van de verschuldigde belasting

B) Tweede overtreding 20 pct. van de verschuldigde belasting

C) Volgende overtredingen 100 pct. van de verschuldigde belasting

2. Vervoermiddel dat niet kan worden ingevoerd met tijdelijke vrijstelling.

A) Louter toevallige overtredingen (12) 10 pct. van de verschuldigde belasting

B) Andere overtredingen 100 pct. van de verschuldigde belasting

## Afdeling 3.- Uitvoer.
XII. Overtredingen inzake de toepassing van artikel 39 van het
Wetboek.

1. A) Vrijstelling ten onrechte toegepast of 10 pct. van de verschuldigde ingeroepen belasting

B) Het bewijs van het recht op vrijstelling wordt 10 pct. van de verschuldigde niet geleverd belasting

2. Overtredingen in verband met de toepassing van de opschorting van de betaling van de belasting beoogd in artikel 15 van het koninklijk besluit nr. 18 van 29 december 1992 met betrekking tot de vrijstellingen ten aanzien van de uitvoer van goederen en diensten buiten de Gemeenschap, op het stuk van de belasting over de toegevoegde waarde, ter uitvoering van artikel 39, § 3, van het Wetboek.

A) De opschorting van de betaling van de belasting 10 pct. van de belasting werd ingeroepen voor handelingen waarvoor ze waarvan de opschorting ten niet van toepassing is en die de belasting onrechte werd ingeroepen opeisbaar maken

(12) Moet onder "louter toevallige overtredingen" worden verstaan, de onregelmatigheden die te wijten zijn aan onwetendheid, vergissingen of nalatigheid en waarbij aan de goede trouw van de overtreder niet kan worden getwijfeld.

B) De goederen krijgen een andere bestemming 10 pct. van de verschuldigde dan die voorzien onder het stelsel van belasting opschorting, waarvoor de belasting opeisbaar is, en de belastingplichtige die de opschorting heeft toegepast heeft de daarvoor voorziene regularisatie niet uitgevoerd op het tijdstip waarop de wijziging in bestemming plaatsvond

XIII. (opgeheven)

XIV. Overtredingen inzake de toepassing van artikel 42, § 3, 8°, en van artikel 40, § 1, 1°, a, van het Wetboek, voor wat betreft de invoer en de intracommunautaire verwervingen van goederen bedoeld in artikel 42, § 3, 8°, van het Wetboek.

1. Een vergunning is verleend op grond van verkeerde 20 pct. van de belasting inlichtingen verstrekt door de aanvrager waarvan de vrijstelling is verkregen

2. Overtredingen in verband met de toepassing van de vergunning.

A) Op de vergunning is aanspraak gemaakt voor 10 pct. van de belasting handelingen waarvoor ze niet van toepassing is waarvan de vrijstelling ten onrechte is verkregen

B) Het vergelijkingsregister of de boekhouding die 20 pct. van de belasting voor de controle van de vrijstelling wordt waarvan de vrijstelling is voorgeschreven is niet gehouden of is verkregen gehouden op zodanige wijze dat deze controle zeer moeilijk is. De vergunninghouder voldoet niet aan het verzoek van de controlerende ambtenaar om het register of de boekhouding binnen een redelijke termijn aan te leggen of aan te passen

C) De goederen worden niet uitgevoerd binnen de in de vergunning bepaalde termijn en :

1° de vergunninghouder heeft de daarvoor 10 pct. van de te regulariseren voorgeschreven regularisatie uitgevoerd belasting in overeenstemming met de voorwaarden van de vergunning

2° op het tijdstip van de controle heeft de 20 pct. van de te regulariseren vergunninghouder de verplicht geworden belasting regularisatie nog niet uitgevoerd

## Afdeling 4.- Andere regeling van entrepot dan douane-entrepot.

XV. Overtredingen begaan bij de toepassing van artikel 39quater 10 pct. van de verschuldigde van het Wetboek belasting.

TABEL H

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 1bis, VAN HET WETBOEK

Ten onrechte afgetrokken belasting.

Het bedrag van de verkeerdelijk in aftrek gebrachte belasting voor een controleperiode van één jaar (13) is :

- minder dan of gelijk aan 1.250 EUR 5 pct. van de verkeerdelijk in aftrek gebrachte belasting

- meer dan 1.250 EUR 10 pct. van de verkeerdelijk in aftrek gebrachte belasting

TABEL I

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 70, § 3, VAN HET WETBOEK

Het invoerdocument bevat onjuiste vermeldingen ten aanzien van :

1. de aard of de hoeveelheid van de ingevoerde goederen.

A) Louter toevallige overtredingen (14) zie tabel G, VIII, 3

B) Andere overtredingen 50 pct. van de op de handeling verschuldigde belasting zonder dat ze minder dan 50 EUR mag bedragen

2. de prijs of de bij de prijs te voegen kosten.

A) Louter toevallige overtredingen (14) zie tabel G, VIII, 2

B) Andere overtredingen 50 pct. van de op de handeling verschuldigde belasting zonder dat ze minder dan 50 EUR mag bedragen

3. de naam en het adres van degene op wiens naam de terzake van invoer verschuldigde belasting moet worden voldaan.

A) Louter toevallige overtredingen (14) nihil

B) Andere overtredingen 50 pct. van de op de handeling verschuldigde belasting zonder dat ze minder dan 50 EUR mag bedragen

(13) Indien de controleperiode korter of langer is dan één jaar wordt het bedrag van 1.250 EUR proportioneel verminderd of verhoogd.
(14) Moet onder "louter toevallige overtredingen" worden verstaan, de onregelmatigheden die te wijten zijn aan onwetendheid, vergissingen of nalatigheid en waarbij aan de goede trouw van de overtreder niet kan worden getwijfeld.

TABEL J

GELDBOETEN VAN TOEPASSING VOOR DE OVERTREDINGEN
BEOOGD IN ARTIKEL 71 VAN HET WETBOEK

Vermelding op de bij uitvoer of tot staving ervan overgelegde 10 pct. van de overeenkomstig stukken, hetzij van een grotere hoeveelheid goederen dan de artikel 71 van het Wetboek, werkelijk uitgevoerde hoeveelheid, hetzij van een hogere prijs of berekende belasting die verwaarde dan de werkelijke prijs of waarde van de uitgevoerde schuldigd zou zijn geweest, met goederen, hetzij van de uitgevoerde goederen onder een valse een minimum van 50 EUR benaming
