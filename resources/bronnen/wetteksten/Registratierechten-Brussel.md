---
tags: [VIII, '2.6']
itaa-lex-sectie: VIII
wet: Wetboek der Registratie-, Hypotheek- en Griffierechten — Brussels Hoofdstedelijk Gewest
status: beschikbaar
bijgewerkt: 16.03.2026
bron: Fisconetplus.be (officieuze gecoördineerde versie)
provenance:
  inputs:
    - id: resources/raw/wetteksten/Registratierechten-Brussel.pdf
      sha256: a5a42fdb62118bd14b1ff76a771cced7b25a5b4d9859eae758e7361286b4eb68
      version: 16.03.2026
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 732fcc0
    model:
    prompt_version:
  generated_at: '2026-05-07T13:37:30Z'
  stale: false
  stale_reason:
  trust:
    status: unreviewed
    confirmed_at:
    confirmed_by:
    rationale:
    layer1:
      status: warn
      run_id: 20260509-212552
      run_at:
      heading_count: 602
      max_section_chars: 58083
      file_size_chars: 543714
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ######-niveau: 58083 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
        - name: no_toc_dots
          status: warn
          detail: 72 TOC-stippen-regel(s) gevonden
          samples:
            - '................................................................................'
            - '...............................................................................6'
            - '................................................................................'
    layer2:
      status: needs-rework
      agent:
      run_at:
      rationale: 'Grote codex met 602 headings, maar Laag-1 meldt 72 TOC-stippen-regels (= TOC niet uit body verwijderd) en max_section_size 58k chars op niveau ######. RAG zal vervuilde TOC-chunks meekrijgen.'
      concrete_problemen:
        - 72 TOC-stippen-regels (TOC niet ontkoppeld)
        - max_section_size 58083 chars
chunk:
  level: 6
  type: Art.
  sub_strategy:
---

# Registratierechten — Brussels Hoofdstedelijk Gewest

*Bijgewerkt tot en met 16.03.2026 — officieuze gecoördineerde versie. Bron: Fisconetplus.be.*

HYPOTHEEK- EN GRIFFIERECHTEN

BRUSSELS HOOFDSTEDELIJK GEWEST

Wetgeving van toepassing in het BRUSSELSE HOOFDSTEDELIJK GEWEST

Wetgeving van toepassing in het BRUSSELSE HOOFDSTEDELIJK GEWEST

(officieuze coördinatie)

(KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie- hypotheek- en griffierechten (B.S. 01.12.1939) err. (B.S., 03.12.1939 en B.S. 13.12.1939). Dit KB werd bekrachtigd door art. 2 van de wet van 16.06.1947 (B.S. 14.08.1947) err. (B.S., 26.10.1947))

## TITEL I - REGISTRATIERECHT................................................................................................................................................ 6

### HOOFDSTUK I - Formaliteit der registratie en vestiging van de belasting ...............................................................................6

### HOOFDSTUK II - Indeling van de rechten en algemene heffingsregels ..................................................................................11

### HOOFDSTUK III - Registratieverplichting .............................................................................................................................................13

Eerste afdeling - Akten en verklaringen aan de formaliteit onderworpen .......................................................................13

#### Afdeling II - Termijnen voor de aanbieding ter registratie .......................................................................................................18

#### Afdeling III - Personen verplicht tot aanbieding ter registratie..............................................................................................22

#### Afdeling IV - Plaats der registratie .....................................................................................................................................................24

#### Afdeling V - Sanctiën................................................................................................................................................................................25

### HOOFDSTUK IV - Vaststelling van de rechten ...................................................................................................................................26

#### Afdeling I - Overdrachten onder bezwarende titel van onroerende goederen...............................................................27

#### Afdeling II - Openbare verkopingen van lichamelijke roerende goederen ........................................................................43

#### Afdeling III - (…) ...........................................................................................................................................................................................44

#### Afdeling IV - Huurcontracten................................................................................................................................................................45

#### Afdeling V - (…)............................................................................................................................................................................................46

#### Afdeling VI - Hypotheekvestigingen .................................................................................................................................................47

#### Afdeling VII - (…) .........................................................................................................................................................................................50

#### Afdeling VIII - (…) ........................................................................................................................................................................................50

#### Afdeling IX - Opheffingen.......................................................................................................................................................................51

#### Afdeling X - Verdelingen .........................................................................................................................................................................53

#### Afdeling XI - Vennootschappen...........................................................................................................................................................55

#### Afdeling XII - Schenkingen .....................................................................................................................................................................64

#### Afdeling XIII - Huwelijkscontracten en testamenten .................................................................................................................79

#### Afdeling XIV- Vonnissen en arresten ................................................................................................................................................79

#### Afdeling XV - (…).........................................................................................................................................................................................83

#### Afdeling XVI - (…)........................................................................................................................................................................................83

#### Afdeling XVII - (…) ......................................................................................................................................................................................83

#### Afdeling XVIII - (…) .....................................................................................................................................................................................84

#### Afdeling XIX - Protesten .........................................................................................................................................................................84

#### Afdeling XIXbis - Aangehechte akten en geschriften .................................................................................................................84

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en onderhevig aan het algemeen vast recht ...............84

#### Afdeling XXI - Akten vrijgesteld van het evenredig recht en onderhevig aan een bijzonder vast recht van 10

euro..................................................................................................................................................................................................................87

### HOOFDSTUK V - Registratie in debet ....................................................................................................................................................89

### HOOFDSTUK VI - Kosteloze registratie.................................................................................................................................................90

### HOOFDSTUK VII - Vrijstelling van de formaliteit der registratie.................................................................................................93

### HOOFDSTUK VIII - Diverse bepalingen betreffende de vereffening van de rechten en de betaling van het

verschuldigde bedrag ....................................................................................................................................................................................99

### HOOFDSTUK IX - Verplichtingen met het oog op het verzekeren van het heffen van de rechten........................... 101

#### Afdeling I - Vermeldingen op te nemen in bepaalde akten .................................................................................................. 101

#### Afdeling II - Voorschriften betreffende het uitreiken van uitgiften................................................................................... 102

#### Afdeling III - Repertorium van de akten ........................................................................................................................................ 104

#### Afdeling IV - Verplichting van inzageverlening .......................................................................................................................... 106

#### Afdeling V - Verplichtingen opgelegd aan openbare ambtenaren ter verzekering van de invordering der

registratierechten ................................................................................................................................................................................... 110

### HOOFDSTUK X - Bewijsmiddelen......................................................................................................................................................... 111

#### Afdeling I - Algemene bepalingen ................................................................................................................................................... 111

#### Afdeling II - Controleschatting .......................................................................................................................................................... 112

### HOOFDSTUK XI - Tekort in de waardering, bewimpeling en veinzing. Sanctiën .............................................................. 117

### HOOFDSTUK XII - Correctionele straffen .......................................................................................................................................... 118

### HOOFDSTUK XIII - Teruggaaf ................................................................................................................................................................. 123

### HOOFDSTUK XV - Vervolgingen en gedingen ................................................................................................................................. 134

### HOOFDSTUK XVI - Bijzondere bepalingen betreffende de openbare verkopingen van roerende goederen ...... 136

### HOOFDSTUK XVII - Inlichtingen te verstrekken door de Algemene Administratie van de

Patrimoniumdocumentatie ..................................................................................................................................................................... 140

### HOOFDSTUK XVIII - Speciaal recht op de nationaliteit, de adelbrieven en de verzoeken tot verandering van

naam.................................................................................................................................................................................................................. 141

#### Afdeling I - Nationaliteit ....................................................................................................................................................................... 142

#### Afdeling II - Open brieven van adeldom en verzoeken tot verandering van naam.................................................... 144

#### Afdeling III - Bepaling gemeen aan afdelingen I en II .............................................................................................................. 147

### HOOFDSTUK XIX - Speciale geldboete wegens late neerlegging van aan bekendmaking onderworpen akten van

vennootschap ................................................................................................................................................................................................ 147

## TITEL II - HYPOTHEEKRECHT........................................................................................................................................... 147

## TITEL III - GRIFFIERECHT .................................................................................................................................................. 150

### HOOFDSTUK I - VESTIGING VAN DE BELASTING EN VASTSTELLING VAN DE RECHTEN .......................................... 150

#### Afdeling I - Rolrecht ............................................................................................................................................................................... 150

#### Afdeling Ibis - Opstelrecht................................................................................................................................................................... 153

#### Afdeling II - Expeditierecht ................................................................................................................................................................. 154

#### Afdeling III - Legalisatie- en opzoekingsrechten....................................................................................................................... 156

#### Afdeling IV - Recht van inschrijving in het handelsregister .................................................................................................. 156

### HOOFDSTUK II - Vrijstellingen ............................................................................................................................................................... 156

### HOOFDSTUK III - Diverse bepalingen.................................................................................................................................................. 159

## TITEL IV - DIGITALISATIE VAN DE RELATIES TUSSEN DE FEDERALE OVERHEIDSDIENST FINANCIËN, DE

BURGERS EN BEPAALDE DERDEN ................................................................................................................................. 162 GEMEENSCHAPPELIJKE BEPALINGEN VOOR ALLE BELASTINGEN........................................................................... 166 INTREKKINGSBEPALING .......................................................................................................................................................................... 219 TIJDELIJKE BEPALINGEN .......................................................................................................................................................................... 219

#### Afdeling I - Maatregelen waarbij de oprichting van nieuwe gebouwen begunstigd wordt door een

vermindering der registratierechten .............................................................................................................................................. 219

#### Afdeling II - Diverse bepalingen........................................................................................................................................................ 221

OVERGANGSBEPALINGEN ...................................................................................................................................................................... 225

#### Afdeling II - Bijzondere maatregelen ............................................................................................................................................. 226

BIJBEPALINGEN BETREFFENDE DE MET HET ZEGEL GELIJKGESTELDE TAKSEN......................................................... 227

Wetgeving van toepassing in het BRUSSELSE HOOFDSTEDELIJK GEWEST

(officieuze coördinatie)

(KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie- hypotheek- en griffierechten (B.S. 01.12.1939) err. (B.S., 03.12.1939 en B.S. 13.12.1939). Dit KB werd bekrachtigd door art. 2 van de wet van 16.06.1947 (B.S. 14.08.1947) err. (B.S., 26.10.1947))

## TITEL I - REGISTRATIERECHT

### HOOFDSTUK I - Formaliteit der registratie en vestiging van de belasting

###### Art. 1

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 79 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Registratie is een formaliteit bestaande in het afschrijven, ontleden of vermelden van een akte of van een geschrift, in een hiertoe bestemd register van de Algemene Administratie van de Patrimoniumdocumentatie of op elke andere informatiedrager bepaald door de Koning.

Deze formaliteit geeft aanleiding tot heffing van een belasting genaamd registratierecht.

###### Art. 2

(van toepassing vanaf 17.08.2020)

(gewijzigd bij art. 111 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))

De akten worden op de minuten, brevetten of originelen geregistreerd.

Evenwel worden de buitenlands verleden authentieke akten in minuut op de uitgiften, afschriften of uittreksels geregistreerd.

De Koning kan voor de door Hem aangewezen categorieën van akten, geschriften en verklaringen die aan de formaliteit van de registratie onderworpen worden, bepalen dat zij onder de vorm van de minuut, een afschrift of een kopie en al dan niet op gedematerialiseerde wijze, ter registratie kunnen of moeten worden aangeboden. Voor de aldus aangewezen categorieën van akten, geschriften en verklaringen bepaalt Hij de modaliteiten van de aanbieding ter formaliteit en van de uitvoering van de formaliteit alsook de voorschriften die voor de juiste heffing van de verschuldigde rechten nodig zijn. Hij kan daarbij afwijken van de bepalingen van de artikelen 6, tweede lid, 8, 9, 26, 39, 40, 168, 171 en 172 van dit Wetboek. Hij kan echter geen geldboete opleggen met een bedrag hoger dan 25 euro in geval van overtreding van de door hem in afwijking van de artikelen 171 en 172 vastgestelde regels.

De Koning kan bepalen dat wanneer de aanbieding ter registratie van akten of van bepaalde categorieën van akten op gedematerialiseerde wijze geschiedt, de aanbieding vergezeld moet gaan van gestructureerde metagegevens betreffende de akte, waaronder in het bijzonder, voor elke partij bij de akte, haar identificatienummer in het Rijksregister of het haar in uitvoering van artikel 4, § 2, van de wet van 15 januari 1990 houdende oprichting en organisatie van een Kruispuntbank van de sociale zekerheid toegekende identificatienummer in het bisregister of, voor een rechtspersoon, zijn ondernemingsnummer bedoeld in artikel III. 17 van het Wetboek van economisch recht.

Onverminderd het derde en het vierde lid, worden de vonnissen en arresten geregistreerd op een door de griffier eensluidend verklaard afschrift dat op elektronische wijze wordt aangeboden, behoudens overmacht of technische storing in welk geval de aanbieding gebeurt op papier. De vermelding van de registratie wordt aan de griffier verzonden samen met het geregistreerde vonnis of arrest, op dezelfde wijze als dat laatste werd aangeboden.

Onverminderd het derde en het vierde lid, worden de onderhandse akten geregistreerd op een origineel of op een kopie, met uitzondering van de akten bedoeld in artikel 19, eerste lid, 3° die op een kopie worden geregistreerd.

###### Art. 2bis

(van toepassing vanaf 10.01.2014)

(ingevoegd bij art. 43 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87,
1°))

De registratie van de notariële akten vereist de vermelding van het identificatienummer of het ondernemingsnummer bedoeld in artikel 2, vierde lid, voor elke partij bij de akte, wanneer dit nummer beschikbaar is.

Deze vermelding geschiedt in de akte of, ten laatste bij de aanbieding ervan ter registratie, in een aanvullende verklaring onderaan de akte, getekend door de betrokken partij of door de instrumenterende notaris, in haar naam.

###### Art. 2ter

(van toepassing vanaf 01.04.2014 en 01.06.2014)

(ingevoegd bij art. 44 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf: a) wat de akten bedoeld in artikel 19, eerste lid, 3°, a), W.Reg. betreft: vanaf 01.04.2014; b) wat de akten bedoeld in artikel 19, eerste lid, 3°, b), van hetzelfde Wetboek betreft, vanaf 01.06.2014 (art. 87, 4°, a en b))

De vermeldingsplicht bedoeld in artikel 2bis, eerste lid, geldt ook voor de registratie van de akten bedoeld in artikel 19, eerste lid, 3°, wat betreft rechtspersonen.
Indien aan een partij bij een dergelijke akte nog geen ondernemingsnummer is toegekend, bevestigt die partij dit in de akte of in een ondertekende aanvullende verklaring onderaan de akte.

###### Art. 2quater

(van toepassing vanaf 09.06.2024)

(lid 3, vervangen bij art. 58 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf 09.06.2024 (art. -))

De registratie van een akte bedoeld in artikel 19, eerste lid, 3°, al dan niet samen met bijlagen, of van een plaatsbeschrijving die niet samen met de hiervoor bedoelde akte wordt aangeboden, is, in geval van aanbieding op een papierendrager, afhankelijk van de aanbieding samen met de te registreren documenten van een volledig en leesbaar ingevuld formulier waarvan het model wordt bepaald door de Koning.

Het formulier kan de verplichte vermelding bevatten van het identificatienummer of het ondernemingsnummer, bedoeld in artikel 2, vierde lid, van de partijen bij de akte, wanneer dit nummer beschikbaar is.

De aanbieding ter registratie van de in het eerste lid bedoelde documenten wordt gedaan door ze via een aanbieder van postdiensten te sturen naar het adres dat door de Koning wordt bepaald.

In geval de uitvoering van de formaliteit van de registratie wordt geweigerd wegens niet naleving van de voorgaande bepalingen, wordt de verzoeker daarvan in kennis gesteld.

Dit artikel is niet van toepassing in het geval bepaald in artikel 25.

###### Art. 3

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 80 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Wordt een in een andere taal dan de landstalen gestelde akte of geschrift ter registratie aangeboden, zo kan het bevoegde kantoor van de Algemene Administratie van de Patrimoniumdocumentatie eisen dat, op de kosten van de persoon die de formaliteit vordert, een door een beëdigde vertaler voor echt verklaarde vertaling daaraan worde toegevoegd.

###### Art. 4

(van toepassing vanaf 01.02.1940)

De registratie is ondeelbaar: zij wordt toegepast op de gehele akte of het geheel geschrift welke tot de formaliteit wordt aangeboden.

###### Art. 5

(van toepassing vanaf 29.06.2020)
(opgeheven bij art. 3 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1). Tekst van toepassing vanaf 29.06.2020 (art. -))

(…)

###### Art. 5bis

(van toepassing vanaf 07.02.2022))

(vervangen bij art. 93 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

Een akte die wordt aangeboden ter registratie en ter hypothecaire overschrijving, wordt tezelfdertijd tot de beide formaliteiten aangeboden, behalve indien de termijnen voor de aanbieding ervan verschillen.

Bij gelijktijdige aanbieding tot de formaliteiten, wordt de registratie van de akte geweigerd zolang op dit kantoor de overschrijving wordt geweigerd.

Het eerste en tweede lid zijn niet van toepassing op een akte die enkel de niet-vatbaarheid voor beslag vaststelt van de woning van een zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse bepalingen (IV).

###### Art. 6

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 82 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Het bevoegde kantoor van de Algemene Administratie van de Patrimoniumdocumentatie is gehouden tot het registreren van de akten of geschriften op de datum waarop ze onder de wettelijke voorwaarden tot de formaliteit worden aangeboden.

Een buiten de openingsuren van de kantoren aangeboden akte of geschrift, wordt geacht aangeboden te zijn bij de eerstvolgende opening van de kantoren.

Het kantoor mag ze niet langer houden dan nodig is.

###### Art. 7

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 83 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Zo een akte of geschrift, waarvan er geen minuut bestaat, inlichtingen vervat die kunnen dienen om aan 's Rijks schatkist verschuldigde sommen te ontdekken, heeft het bevoegde kantoor van de Algemene Administratie van de Patrimoniumdocumentatie het recht er een afschrift van te maken en dit eensluidend met het origineel te doen waarmerken door de werkende openbare officier of, zo het gaat om een onderhandse of buitenlands verleden akte, door de betrokken persoon die de formaliteit heeft gevorderd. Bij weigering, waarmerkt het bevoegde kantoor zelf de eensluidendheid van het afschrift, met vermelding van die weigering. Het aldus gewaarmerkt afschrift wordt, behoudens bewijs van het tegendeel, als eensluidend aangezien.

###### Art. 8

(van toepassing vanaf 29.06.2020)

(gewijzigd bij art. 4 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1). Tekst van toepassing vanaf 29.06.2020 (art. -))

Vermelding van de registratie wordt op de akte of het geschrift gesteld naar een door de minister van Financiën bepaalde tekst.

Voor akten en geschriften als bedoeld in artikel 2quater, wordt de vermelding van de registratie gesteld volgens door de Koning te bepalen nadere regels.

Indien er toepassing gemaakt wordt van de vrijstelling voorzien in artikel 8bis, wordt de vermelding van de registratie vervangen door de vermelding van de betaling die verricht moet worden volgens de modaliteiten voorzien in uitvoering van dit artikel. Deze vermelding geschiedt naar een door de Minister van Financiën vastgestelde tekst.

###### Art. 8bis

(van toepassing vanaf 01.01.1990)

(ingevoegd bij art. 135 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

De Koning kan bepaalde categorieën van de in de artikelen 19, 1° en 6°, 26 en 29 bedoelde akten van de registratieformaliteit vrijstellen zonder dat deze vrijstelling de ontheffing van de op deze akten toepasselijke rechten meebrengt, alsook de betalingsmodaliteiten voor genoemde rechten, binnen de termijnen die Hij bepaalt, regelen, in voorkomend geval afwijkend van de bepalingen van hoofdstuk III en IX van deze titel. Indien er toepassing gemaakt wordt van deze bepaling kan de Koning het neerleggen van een afschrift van de akten voorschrijven en aanvullende regels vaststellen om de juiste heffing van de belasting te verzekeren.

###### Art. 9

(van toepassing vanaf 01.03.2021)

(gewijzigd bij art. 12 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van toepassing vanaf 01.03.2021 (art. -))

Valt de laatste dag van de termijn, die door onderhavig Wetboek vastgesteld is voor de uitvoering van een formaliteit, op een sluitingsdag van de kantoren, dan wordt deze termijn verlengd tot de eerste openingsdag der kantoren die volgt op het verstrijken van de termijn.

### HOOFDSTUK II - Indeling van de rechten en algemene heffingsregels

###### Art. 10

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 136 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Er zijn evenredige en vaste registratierechten.

Vaste rechten zijn verdeeld in algemeen vast recht en specifieke vaste rechten.

###### Art. 11

(van toepassing vanaf 01.07.2013)

(gewijzigd bij art. 11 van de programmawet van 28.06.2013 (B.S., 01.07.2013 – ed. 2). Tekst van toepassing vanaf 01.07.2013 (art. 13))

De evenredige en de specifieke vaste rechten worden geheven volgens het in dit Wetboek vastgestelde tarief.

Het algemeen vast recht is van toepassing op al de in dat tarief niet voorziene akten en geschriften.

Het algemeen vast recht bedraagt 50 EUR.

###### Art. 12

(van toepassing vanaf 01.02.1940)

Het evenredig of specifiek vast recht wordt slechts eenmaal op een rechtshandeling geheven, wat ook het getal zij van de geschriften die daarvan laten blijken.

###### Art. 13

(van toepassing vanaf 01.02.1940)

Geven slechts aanleiding tot heffing van het algemeen vast recht, tenzij daarin een toevoeging of wijziging voorkomt welke van die aard is dat ze de heffing van een nieuw of aanvullend recht ten gevolge heeft:

1° Alle nieuw geschrift opgemaakt om te laten blijken van een rechtshandeling waarop reeds het evenredig of specifiek vast recht werd geheven;

2° Alle geschrift houdende bekrachtiging, bevestiging, uitvoering, aan vulling of voltrekking van geregistreerde vroegere akten, indien het niet laat blijken van nieuwe rechtshandelingen welke als dusdanig aan een evenredig of specifiek vast recht onderhevig zijn.
Geven insgelijks slechts aanleiding tot heffing van het algemeen vast recht, die rechtshandelingen welke ter oorzake van nietigheid, ontbinding of om andere reden opnieuw werden verricht zonder enige verandering welke iets toevoegt aan het voorwerp der overeenkomsten of aan derzelver waarde, ten ware het op de eerste handeling geheven evenredig recht teruggegeven werd of voor teruggaaf vatbaar zij.

###### Art. 14

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 2 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Wanneer een akte verscheidene onder dezelfde contractanten tot stand gekomen beschikkingen vervat, welke de ene van de andere afhankelijk zijn of de ene uit de andere noodzakelijk voortvloeien, is slechts één recht voor deze gezamenlijke beschikkingen verschuldigd.

Het recht wordt geheven met inachtneming van diegene van bedoelde beschikkingen welke tot het hoogste recht aanleiding geeft.

###### Art. 15

(van toepassing vanaf 01.02.1940)

Wanneer, in een akte, verscheidene onafhankelijke of niet noodzakelijk uit elkaar voortvloeiende beschikkingen voorkomen, is voor elk dier beschikkingen en wel naar eigen aard een bijzonder recht verschuldigd.

Deze regel is niet van toepassing op het algemeen vast recht.

###### Art. 16

(van toepassing vanaf 01.02.1940)

De rechtshandeling waarop het evenredig recht verschuldigd is, doch welke aan een schorsende voorwaarde onderworpen is, geeft alleen tot heffing van het algemeen vast recht aanleiding zolang de voorwaarde niet is vervuld.

Wordt de voorwaarde vervuld, zo is het recht verschuldigd dat bij het tarief voor de handeling is vastgesteld, behoudens toerekening van het reeds geheven recht. Het wordt berekend naar het tarief dat van kracht was op de datum waarop het recht aan de Staat zou verworven geweest zijn indien de handeling een onvoorwaardelijke was geweest, en op de bij dit wetboek vastgelegde en op de datum van de vervulling der voorwaarde beschouwde belastbare grondslag.

###### Art. 17

(van toepassing vanaf 01.02.1940)
Wordt, voor de toepassing van dit wetboek, met een aan een schorsende voorwaarde onderworpen handeling gelijkgesteld, de rechtshandeling door een rechtspersoon verricht en aan machtiging, goedkeuring of bekrachtiging van overheidswege onderworpen.

###### Art. 18

(van toepassing vanaf 01.06.2012)

(§ 2, vervangen bij art. 168 van de programmawet van 29.03.2012 (B.S., 06.04.2012 - ed. 3). Tekst van toepassing te weten op de rechtshandelingen of het geheel van rechtshandelingen die éénzelfde verrichting tot stand brengt, die zijn gesteld vanaf 01.06.2012 (art. 169))

§ 1. De datum van de onderhandse akten over 't algemeen of van de overeenkomsten die door het feit alleen van haar bestaan verplicht aan de formaliteit van registratie onderworpen zijn, kan niet tegen het bestuur worden ingeroepen dan voor zover hij tegen derden kan worden ingeroepen. Registratie sluit geen erkenning door het bestuur in van de datum der akte of der overeenkomst.

§ 2. Aan de administratie kan niet worden tegengeworpen, de rechtshandeling noch het geheel van rechtshandelingen dat een zelfde verrichting tot stand brengt, wanneer de administratie door vermoedens of door andere in artikel 185 bedoelde bewijsmiddelen en aan de hand van objectieve omstandigheden aantoont dat er sprake is van fiscaal misbruik.

Er is sprake van fiscaal misbruik wanneer de belastingschuldige door middel van de door hem gestelde rechtshandeling of het geheel van rechtshandelingen één van de volgende verrichtingen tot stand brengt:

1. een verrichting waarbij hij zichzelf in strijd met de doelstellingen van een bepaling van dit Wetboek of de ter uitvoering daarvan genomen besluiten buiten het toepassingsgebied van die bepaling plaatst; of

2. een verrichting waarbij aanspraak wordt gemaakt op een belastingvoordeel voorzien door een bepaling van dit Wetboek of de ter uitvoering daarvan genomen besluiten en de toekenning van dit voordeel in strijd zou zijn met de doelstellingen van die bepaling en die in wezen het verkrijgen van dit voordeel tot doel heeft.

Het komt aan de belastingschuldige toe te bewijzen dat de keuze voor zijn rechtshandeling of het geheel van rechtshandelingen door andere motieven verantwoord is dan het ontwijken van registratierechten.

Indien de belastingschuldige het tegenbewijs niet levert, dan wordt de verrichting aan een belastingheffing overeenkomstig het doel van de wet onderworpen alsof het misbruik niet heeft plaatsgevonden.

### HOOFDSTUK III - Registratieverplichting

Eerste afdeling - Akten en verklaringen aan de formaliteit onderworpen

###### Art. 19

(van toepassing vanaf 09.03.2026)

(lid 1, 5°, gewijzigd bij art. 20 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Moeten binnen de bij artikel 32 gestelde termijnen geregistreerd worden:

1° De akten van notarissen; de exploten en processen-verbaal van gerechtsdeurwaarders, met uitzondering van de protesten zoals bedoeld in de protestwet van 3 juni 1997; de arresten en vonnissen der hoven en rechtbanken die bepalingen bevatten welke door deze titel aan een evenredig recht onderworpen worden;

2° De akten waarbij de eigendom of het vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt;

3° a) De akten houdende verhuring, onderverhuring of overdracht van huur van in België gelegen onroerende goederen of gedeelten van onroerende goederen, die uitsluitend bestemd zijn tot huisvesting van een gezin of van één persoon;

b) De andere dan onder a) bedoelde akten houdende verhuring, onderverhuring of overdracht van huur van in België gelegen onroerende goederen of gedeelten van onroerende goederen.

4° De processen-verbaal van openbare verkoping van lichamelijke roerende voorwerpen;

5° De akten houdende inbreng van goederen in vennootschappen met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel in België en de zetel der werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie, is gevestigd;

6° de in het buitenland verleden notariële akten die titel vormen voor een schenking onder de levenden van roerende goederen door een rijksinwoner.

Onverminderd de bepaling onder 6° van het eerste lid en behoudens wat de bepalingen onder 2°, 3° en 5° van hetzelfde lid betreft, worden in dit artikel alleen de in België verleden akten bedoeld.

###### Art. 20

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 211

(van toepassing vanaf 09.06.2024)
(vervangen bij art. 59 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf 09.06.2024 (art. -))

De bevoegde dienst van de Algemene administratie van de patrimoniumdocumentatie neemt een kopie bij de aanbieding ter registratie op een papieren drager van de volgende akten, haar bijlagen en alle andere tegelijk aan te bieden stukken, geschriften en verklaringen:

1° de plaatsbeschrijving bedoeld in artikel 2quater, eerste lid;

2° de onderhandse of in het buitenland verleden akten bedoeld in artikel 19, eerste lid, 2°, behalve wanneer het gaat om een akte welke onder de minuten van een notaris in België berust of bij zijn minuten is gevoegd;

3° de onderhandse of in het buitenland verleden akten bedoeld in artikel 19, eerste lid, 3°, 5° en 6°, behalve wanneer het gaat om een akte welke onder de minuten van een notaris in België berust of bij zijn minuten is gevoegd;

4° de verklaringen bedoeld in artikel 31.

De Koning kan de categorie van akten, geschriften en verklaringen bedoeld in het eerste lid vervolledigen of wijzigen.

De kopie bedoeld in het eerste lid wordt minstens gedurende tien jaar bewaard door de bevoegde dienst van de Algemene administratie van de patrimoniumdocumentatie, voor zover deze niet wordt overgedragen aan het Rijksarchief of vernietigd in uitvoering van de artikelen 1 en 5 van de archiefwet Wet van 24 juni 1955.

###### Art. 212

(van toepassing vanaf 01.01.1971)

(gewijzigd bij art. 1 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van 19.12.1969 (B.S., 20.12.1969)))

Als onroerende goederen worden niet beschouwd:

1° Voor de toepassing van de artikelen 19, 3° en 83, brandkasten, in huur gegeven door personen, verenigingen, gemeenschappen of vennootschappen die gewoonlijk brandkasten verhuren;

2° Voor de toepassing van dit Wetboek, lichamelijk roerende voorwerpen aangewend tot de dienst en de exploitatie van onroerende goederen.

###### Art. 22

(van toepassing vanaf 23.09.1997)

(opgeheven bij art. 3 van de wet van 10.06.1997 (B.S., 19.07.1997). Tekst van toepassing voor de effecten die ter betaling worden aangeboden vanaf 23.09.1997 (art. 10, KB van 15.09.1997 (B.S., 23.09.1997))) (…)

###### Art. 23

(van toepassing vanaf 01.02.1940)

De exequaturs der scheidsrechterlijke uitspraken en die der buitenslands gewezen rechterlijke beslissingen moeten, bij aanbieding ter registratie, vergezeld zijn van de desbetreffende uitspraken of beslissingen

###### Art. 24

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 25

(van toepassing vanaf 15.12.2020)

(gewijzigd bij art. 3 van de wet van 03.12.2020 (B.S., 11.12.2020 – ed. 1). Tekst van toepassing vanaf 15.12.2020 (art. 5))

Wanneer een onderhandse of in het buitenland verleden akte bedoeld in artikel 19, eerste lid, 2°, 3°, 5° of 6°, terzelfdertijd van een niet verplicht in België te registreren overeenkomst doet blijken, kunnen de betrokkenen een door hen gewaarmerkt beknopt uittreksel uit de akte doen registreren waarin alleen melding wordt gemaakt van de overeenkomsten die verplicht in België te registreren zijn.

Het uittreksel wordt in dubbel opgemaakt. Wanneer beide exemplaren ter registratie worden aangeboden, moeten ze vergezeld zijn van de oorspronkelijke akte of, zo het een buitenslands verleden authentieke akte in minuut geldt, van een uitgifte daarvan. De heffing wordt beperkt tot die goederen welke het voorwerp van het uittreksel uitmaken. Een exemplaar van dit uittreksel blijft op het bevoegde kantoor van de Algemene Administratie van de Patrimoniumdocumentatie berusten.

###### Art. 26

(van toepassing vanaf 10.01.2014)

(laatste lid vervangen bij art. 47 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))

Geen akte of geschrift mag aan een van de krachtens artikel 19, 1°, verplichtend te registreren akten, andere dan een vonnis of arrest, worden gehecht, of onder de minuten van een notaris worden neergelegd zonder te voren geregistreerd te zijn.
Evenwel staat het de notarissen en de gerechtsdeurwaarders vrij de aangehechte of neergelegde akte tegelijk met de desbetreffende akte ter registratie aan te bieden.

De in het eerste lid bedoelde verplichting is niet van toepassing:

1° in geval van aanhechting of van neerlegging, onder de vorm van minuut, uitgifte, afschrift of uittreksel, van in België verleden gerechtelijke akten of akten van de burgerlijke stand;

2° in geval van aanhechting of van neerlegging van een plan dat is opgenomen in de databank van plannen van afbakening van de Algemene Administratie van de Patrimoniumdocumentatie, op voorwaarde dat de akte, of een door de partijen of de instrumenterende ambtenaar, in hun naam, ondertekende verklaring onderaan de akte, verwijst naar deze opname met vermelding van het refertenummer van het plan en bevestigt dat het plan nadien niet is gewijzigd.

###### Art. 27

(van toepassing vanaf 18.07.1983)

(opgeheven bij art. 19 van de wet van 01.07.1983 (B.S., 08.07.1983). Tekst van toepassing vanaf 18.07.1983 (art. -))

(…)

###### Art. 28

(van toepassing vanaf 01.01.1969)

(opgeheven bij art. 2/art. 28 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968)))

(…)

###### Art. 29

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 87 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Behoudens het bij artikel 173, 1°, voorziene geval, mag geen overschrijving, inschrijving, doorhaling of randvermelding in de registers van de hypothecaire openbaarmaking plaats hebben krachtens niet vooraf geregistreerde akten.

###### Art. 31

(van toepassing vanaf 09.03.2026)
(lid 1, 1°bis, gewijzigd bij art. 21 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art.
33, lid 1))

Er bestaat verplichting tot ondertekening en tot aanbieding ter registratie, binnen de bij artikel 33 gestelde termijnen, van een verklaring in onderstaande gevallen:

1° Wanneer een overeenkomst, waarbij eigendom of vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt, niet bij een akte is vastgesteld;

1°bis Wanneer een inbreng van goederen in een vennootschap met rechtspersoonlijkheid, waarvan hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel in België en de zetel der werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie, is gevestigd, niet bij een akte is vastgesteld;

1°ter (…)

2° Wanneer de voorwaarde die de heffing van een recht heeft geschorst, vervuld wordt;

3° In de in artikelen 74 en 75 bedoelde gevallen.

Deze door de contracterende partijen of door een van hen ondertekende verklaring vermeldt: de aard en het doel van de overeenkomst, de datum ervan of de datum van het nieuwe feit dat de verschuldigdheid van het recht heeft doen ontstaan, de aanwijzing van de partijen, de omvang van de goederen, de belastbare grondslag en alle voor de vereffening van de belasting nodige gegevens. Een kopie wordt bewaard door de bevoegde dienst van de Algemene administratie van de patrimoniumdocumentatie.

Vanaf het verstrijken van vorenstaande termijnen wordt de door een der partijen ondertekende verklaring als van al de partijen uitgaande aangezien.

#### Afdeling II - Termijnen voor de aanbieding ter registratie

###### Art. 32

(van toepassing vanaf 09.03.2026)

(7°, gewijzigd bij art. 22 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

De termijnen voor de aanbieding ter registratie van verplicht te registreren akten zijn:

1° voor akten van notarissen, vijftien dagen;

De termijn is evenwel:
a) twee maanden, voor de in het kader van een openbare verkoop van een onroerende goed opgemaakte processen-verbaal van:

i. het ontbreken van hoger bod;

ii. definitieve toewijs;

iii. het al dan niet uitoefenen van een voorkooprecht;

iv. het vaststellen van het bekomen van een financiering;

b) vier maanden, te rekenen van het overlijden van de erflaters of schenkers voor:

i. de testamenten;

ii. de schenkingen van toekomstige goederen gedaan tussen echtgenoten gedurende het huwelijk andere dan bij huwelijkscontract;

iii. de akten van herroeping van de onder i en ii bedoelde akten;

iv. de verklaringen betreffende testamenten in de internationale vorm;

v. de akten van bewaargeving van een testament door de erflater.

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten van de registratie en van de hypothecaire overschrijving die bij de aanbieding ter registratie binnen de in het eerste lid gestelde termijn niet werden geregistreerd wegens de weigering van de overschrijving, bedraagt de termijn zeven dagen te rekenen van de datum van de kennisgeving aan de notaris van deze weigering. Deze termijn verstrijkt niet voor het einde van de termijn bepaald, naargelang het geval, in het eerste lid of in het tweede lid, a);

2° Voor akten van gerechtsdeurwaarders, vier dagen;

3° voor arresten en vonnissen der hoven en rechtbanken, tien dagen;

3°bis voor akten van bestuursoverheden en ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen die verplicht onderworpen zijn aan de formaliteit van de registratie en aan die van de hypothecaire overschrijving, vijftien dagen;

De termijn is evenwel twee maanden voor de in het kader van een openbare verkoop van een onroerende goed opgemaakte processen-verbaal van:

a) het ontbreken van hoger bod;

b) definitieve toewijs;

c) het al dan niet uitoefenen van een voorkooprecht;
d) het vaststellen van het bekomen van een financiering.

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten van de registratie en van de hypothecaire overschrijving, die bij de aanbieding ter registratie binnen de in het eerste lid gestelde termijn niet werden geregistreerd wegens de weigering van de overschrijving, bedraagt de termijn zeven dagen te rekenen van de datum van de kennisgeving van deze weigering aan de bestuursoverheden of ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen. Deze termijn verstrijkt niet voor het einde van de termijn bepaald, naargelang het geval, in het eerste lid of in het tweede lid;

4° Voor akten waarbij de eigendom of het vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt, vier maanden;

5° Voor akten van verhuring, onderverhuring of overdracht van huur bedoeld in artikel 19, 3°, a), twee maanden en voor akten van verhuring, onderverhuring of overdracht van huur bedoeld in artikel 19, 3°, b), vier maanden;

6° Voor processen-verbaal van openbare verkoping van lichamelijke roerende goederen opgemaakt door bestuursoverheden en ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen, één maand;

7° Voor akten houdende inbreng van goederen in vennootschappen met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel in België en de zetel der werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie is gevestigd, vier maanden;

8° voor de in artikel 19, eerste lid, 6°, bedoelde akten, vier maanden.

9° (...).

###### Art. 33

(van toepassing vanaf 01.04.1999)

(gewijzigd bij art. 60 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van toepassing vanaf 01.04.1999 (art. 80, § 31))

De termijn, binnen welke de in artikel 31 voorziene verklaringen ter registratie moeten aangeboden worden, is vier maand ingaande met de datum van de overeenkomst of, in voorkomend geval, van de vervulling van de voorwaarde welke de heffing van het recht heeft geschorst.

###### Art. 34

(van toepassing vanaf 07.01.2016)

(opgeheven bij art. 77 van de wet van 18.12.2015 (B.S., 28.12.2015 – ed. 2). Tekst van toepassing vanaf 07.01.2016 (art. -))

(…)
TOEKOMSTIG RECHT (vanaf 01.01.2028)

#### Afdeling III - Personen verplicht tot aanbieding ter registratie

###### Art. 35

(van toepassing vanaf 01.01.2028)

(lid 5, vervangen bij art. 61 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De verplichting tot aanbieding ter registratie van akten of verklaringen en tot betaling van de des betreffende rechten en gebeurlijk de geldboeten, waarvan de vorderbaarheid uit bewuste akten of verklaringen blijkt, berust ondeelbaar:

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de akten van hun ambt;

2° (…)

3° (…)

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in handen neergelegd, zonder voorafgaande registratie;

5° Op de bestuursoverheden en ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen, ten aanzien van de door hen opgemaakte akten;

6° Op de contracterende partijen, ten aanzien van de onderhandse of buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b) en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands verleden akten waarvan sprake in artikel 19, 3°, a);

8° op de contracterende partijen ten aanzien van de in artikel 19, eerste lid, 6°, bedoelde akten.

De verplichting tot aanbieding ter registratie van de arresten en vonnissen van hoven en rechtbanken berust op de griffiers. In afwijking van artikel 169ter worden deze arresten en vonnissen in debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van hoven en rechtbanken, berust op de verweerders, elkeen in de mate waarin de veroordelingen, vereffeningen of rangregelingen te zijnen laste werden uitgesproken of vastgesteld, en op de verweerders hoofdelijk in geval van hoofdelijke veroordeling.
Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een overeenkomst waarbij de eigendom of het vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt, zijn die rechten en boeten ondeelbaar verschuldigd door de personen die partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald binnen de termijn van één maand, te rekenen vanaf de dag van de verzending van de aangetekende zending van het belastingbericht door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van de boeten geen gekende woonplaats in België of in het buitenland heeft, wordt het bericht aan de procureur des Konings te Brussel verzonden.

#### Afdeling III - Personen verplicht tot aanbieding ter registratie

###### Art. 35

(van toepassing vanaf 07.02.2022)

(gewijzigd bij art. 95 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

De verplichting tot aanbieding ter registratie van akten of verklaringen en tot betaling van de des betreffende rechten en gebeurlijk de geldboeten, waarvan de vorderbaarheid uit bewuste akten of verklaringen blijkt, berust ondeelbaar:

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de akten van hun ambt;

2° (…)

3° (…)

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in handen neergelegd, zonder voorafgaande registratie;

5° Op de bestuursoverheden en ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen, ten aanzien van de door hen opgemaakte akten;

6° Op de contracterende partijen, ten aanzien van de onderhandse of buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b) en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands verleden akten waarvan sprake in artikel 19, 3°, a);

8° op de contracterende partijen ten aanzien van de in artikel 19, eerste lid, 6°, bedoelde akten.
De verplichting tot aanbieding ter registratie van de arresten en vonnissen van hoven en rechtbanken berust op de griffiers. In afwijking van artikel 169ter worden deze arresten en vonnissen in debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van hoven en rechtbanken, berust op de verweerders, elkeen in de mate waarin de veroordelingen, vereffeningen of rangregelingen te zijnen laste werden uitgesproken of vastgesteld, en op de verweerders hoofdelijk in geval van hoofdelijke veroordeling.

Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een overeenkomst waarbij de eigendom of het vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt, zijn die rechten en boeten ondeelbaar verschuldigd door de personen die partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald binnen de termijn van één maand, te rekenen vanaf de dag van de verzending van het belastingbericht bij ter post aangetekende brief door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van de boeten geen gekende woonplaats in België of in het buitenland heeft, wordt het bericht aan de procureur des Konings te Brussel verzonden.

###### Art. 36

(van toepassing vanaf 07.02.2022)

(gewijzigd bij art. 96 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

Artikel 35, eerste lid, vindt geen toepassing op de voor notaris opgemaakte testamenten en andere akten als bedoeld in artikel 32, 1°, tweede lid, b), wanneer de betrokkenen het bedrag van de rechten en eventueel van de boeten uiterlijk daags vóór het verstrijken van de voor de registratie gestelde termijn in handen der notarissen niet hebben geconsigneerd.

###### Art. 37

(van toepassing vanaf 07.02.2022)

(gewijzigd bij art. 97 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

Wanneer de rechten betreffende testamenten en andere in artikel 32, 1°, tweede lid, b), bedoelde akten niet in handen der notarissen werden geconsigneerd, zijn ze ondeelbaar door de erfgenamen, legatarissen of begiftigden zomede door de testamentuitvoerders verschuldigd.

###### Art. 38

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 140 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling IV - Plaats der registratie

###### Art. 39

(van toepassing vanaf 07.02.2022)

(1° en 4°, vervangen bij art. 98 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

De akten en verklaringen worden geregistreerd:

1° de akten van notarissen en gerechtsdeurwaarders, op het kantoor bevoegd voor hun standplaats;

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde onroerende goed wordt evenwel geregistreerd een akte die cumulatief:

a) onder de toepassing valt van het koninklijk besluit van 14 maart 2014 houdende regeling van de aanbieding van akten van bepaalde instrumenterende ambtenaren tot de registratieformaliteit en tot de hypothecaire openbaarmaking;

b) onroerende goederen betreft die alle gelegen zijn buiten het ambtsgebied van het kantoor bevoegd voor de standplaats;

c) gelijktijdig ter overschrijving wordt aangeboden.

Het tweede lid is niet van toepassing op een akte die enkel de van niet-vatbaarheid voor beslag vaststelt van de woning van een zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse bepalingen (IV);

1°bis (…)

2° De arresten en vonnissen der hoven en rechtbanken, ten kantore in welks gebied de zetel van het hof of de rechtbank gelegen is;

3° De akten die overeenkomstig artikel 26 zonder voorafgaande registratie worden aangehecht of neergelegd, ten kantore waar de akte van de notaris of de gerechtsdeurwaarder moet worden geregistreerd;

4° De akten van bestuursoverheden en ambtenaren van de Staat, gefedereerde entiteiten, provincies, gemeenten en openbare instellingen, op het kantoor bevoegd voor hun zetel of standplaats;

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde onroerende goed wordt evenwel geregistreerd een akte die cumulatief:
a) onder de toepassing valt van het koninklijk besluit van 14 maart 2014 houdende regeling van de aanbieding van akten van bepaalde instrumenterende ambtenaren tot de registratieformaliteit en tot de hypothecaire openbaarmaking;

b) onroerende goederen betreft die alle gelegen zijn buiten het ambtsgebied van het kantoor bevoegd voor de zetel of de standplaats;

c) gelijktijdig ter overschrijving wordt aangeboden;

5° De onderhandse of buitenslands verleden akten en de verklaringen betreffende in België gelegen onroerende goederen en welke in artikel 19, 2° en 3° en in artikel 31, 1° en 3°, zijn bedoeld, ten kantore in welks gebied de goederen gelegen zijn. Zijn die goederen gelegen in het gebied van verscheidene kantoren, dan mogen de akten en verklaringen onverschillig in een van deze kantoren worden geregistreerd;

6° De verklaringen van vervulling van een in artikel 31, 2°, voorziene schorsende voorwaarde, ten kantore waar de akte werd geregistreerd welke van de overeenkomst laat blijken, of, bij gebreke aan geregistreerde akte, ten kantore in het 5° hiervoren aangeduid;

7° De andere akten dan voornoemde, onverschillig in alle kantoren.

###### Art. 40

(van toepassing vanaf 08.01.2018)

(opgeheven bij art. 27 van de wet van 25.12.2017 (B.S., 29.12.2017 – ed. 1). Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

#### Afdeling V - Sanctiën

###### Art. 41

(van toepassing vanaf 01.01.2015)

(gewijzigd bij art. 4 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van toepassing vanaf 01.01.2015 (art. 8))

Verbeuren ondeelbaar een geldboete gelijk aan het bedrag der rechten, zonder dat ze lager dan 25 EUR mag zijn:

1° de personen die binnen de voorgeschreven termijnen, de akten of verklaringen niet hebben doen registreren welke zij gehouden zijn aan de formaliteit te onderwerpen of de in artikel 169ter, tweede lid, bedoelde betaling niet hebben gedaan;

2° De in artikel 37 aangewezen personen die, binnen den hun daartoe gestelden termijn, de bij artikel 36 voorziene consignatie niet hebben gedaan.
3° De in artikel 35, derde en vierde lid aangewezen personen die de betaling bedoeld in het vijfde lid van genoemde artikel niet hebben gedaan binnen de voorgeschreven termijn.

###### Art. 41bis

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 54 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

De personen die de rechten, verschuldigd op de akten die van de formaliteit der registratie zijn vrijgesteld niet betaald hebben op de voorgeschreven wijze en binnen de voorgeschreven termijn, die geen afschrift van deze akten neergelegd hebben of die zich niet gehouden hebben aan de door de Koning bepaalde aanvullende regels in uitvoering van artikel 8bis, verbeuren ondeelbaar een boete van 25 EUR tot 250 EUR per overtreding.

Het bedrag van de boete wordt, binnen deze grenzen, vastgesteld door de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie.

De in het eerste lid bedoelde personen verbeuren ondeelbaar een boete gelijk aan de ontdoken rechten voor elke akte waarop zij ten onrechte de vrijstelling van de formaliteit bedoeld in artikel 8bis, toegepast hebben.

###### Art. 42

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Voor elke overtreding van artikel 26 verbeurt de notaris of de gerechtsdeurwaarder een boete van 25 EUR.

###### Art. 43

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

De griffiers die binnen de voorgeschreven termijn de arresten en vonnissen niet hebben doen registreren welke zij gehouden zijn aan de formaliteit te onderwerpen, verbeuren voor elke overtreding een boete van 25 EUR.

### HOOFDSTUK IV - Vaststelling van de rechten

#### Afdeling I - Overdrachten onder bezwarende titel van onroerende goederen

§ 1. Algemene bepalingen

###### Art. 44

(van toepassing vanaf 10.04.1994)

(gewijzigd bij art. 40 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

Het recht wordt gesteld op 12,50 t.h. voor de verkopingen, ruilingen en alle overeenkomsten onder bezwarende titel, waarbij eigendom of vruchtgebruik van onroerende goederen wordt overgedragen.

###### Art. 45

(van toepassing vanaf 10.04.1994)

(aangevuld bij art. 41 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

Het recht wordt vereffend:

- ten aanzien van verkopingen, op het bedrag van bedongen prijs en lasten;

- ten aanzien van de ruilingen, op de overeengekomen waarde van de in een der prestatiën begrepen goederen, met inachtneming van die welke aanleiding tot het hoogste recht zou geven zoo beide waren toegestaan tegen een naar die waarde vastgestelde geldprijs;

- ten aanzien van inbrengen van onroerende goederen in vennootschappen, andere dan inbrengen als vermeld in artikel 115bis, op de waarde van de als vergoeding van de inbreng toegekende maatschappelijke rechten verhoogd met de lasten die door de vennootschap gedragen worden;

- ten aanzien van de overige overdragende overeenkomsten, op de overeengekomen waarde van de ten laste van de verkrijger van het onroerend goed bedongen tegenprestatie.

###### Art. 46

(van toepassing vanaf 01.02.1940)

Evenwel mag de belastbare grondslag in geen geval lager zijn dan de verkoopwaarde van de overgedragen onroerende goederen.

###### Art. 46bis

(van toepassing vanaf 24.07.2025)
(lid 7, gewijzigd bij art. 6 van de ordonnantie van 17.07.2025 (B.S., 24.07.2025). Tekst van toepassing vanaf 24.07.2025 (art.
15))

Voor wat betreft de verkopingen, wordt de belastbare grondslag bepaald overeenkomstig de artikelen 45 en 46, verminderd met 200.000 euro in geval van verkrijging door een natuurlijke persoon van de geheelheid in volle eigendom van een geheel of gedeeltelijk tot bewoning aangewend of bestemd onroerend goed dat zal dienen tot hoofdverblijfplaats van de verkrijger. Dit abattement kan slechts worden toegepast indien het bedrag waarop het recht, overeenkomstig de voorgaande artikelen, moet worden vereffend 600.000 euro niet te boven gaat.

Hetzelfde abattement is van toepassing in geval van verkrijging door meerdere natuurlijke personen van de geheelheid in volle eigendom van een geheel of gedeeltelijk tot bewoning aangewend of bestemd onroerend goed dat zal dienen tot gemeenschappelijke hoofdverblijfplaats van de verkrijgers. Dit abattement kan slechts worden toegepast indien het bedrag waarop het recht, overeenkomstig de voorgaande artikelen, moet worden vereffend de 600.000 euro niet te boven gaat.

Voor de toepassing van dit artikel wordt, verstaan onder hoofdverblijfplaats, tenzij tegenbewijs, het adres waarop de verkrijgers zijn ingeschreven in het bevolkingsregister of vreemdelingenregister. Als datum van vestiging van de hoofdverblijfplaats geldt de datum van inschrijving in die registers.

In afwijking van het eerste en het tweede lid, is de vermindering van de belastbare grondslag bij de aankoop van een bouwgrond beperkt tot een bedrag van 100.000 euro wanneer het bedrag waarop het recht vereffend zou moeten worden overeenkomstig de artikelen 45 en 46 niet hoger is dan 300.000 euro. Voor de toepassing van dit lid, wordt de aankoop van een huis of een appartement in aanbouw of op plan niet beschouwd als de aankoop van een bouwgrond.

Aan de vermindering van de belastbare grondslag zijn de volgende voorwaarden verbonden:

1° de verkrijger mag op de datum van de overeenkomst tot verkrijging niet voor de geheelheid volle eigenaar zijn van een ander onroerend goed dat geheel of gedeeltelijk tot bewoning is bestemd; indien de verkrijging geschiedt door meer dan één persoon, moet elke verkrijger deze voorwaarde vervullen, en mogen de verkrijgers bovendien gezamenlijk niet voor de geheelheid volle eigenaar zijn van een ander onroerend goed dat geheel of gedeeltelijk tot bewoning is bestemd;

2° in of onderaan het document dat aanleiding geeft tot de heffing van het evenredig registratierecht of in een bij dat document gevoegd en ondertekend geschrift moeten de verkrijgers:

a) verklaren dat zij voldoen aan de voorwaarde vermeld in 1° van dit lid;

b) zich verbinden hun hoofdverblijfplaats te vestigen op de plaats van het aangekochte goed binnen drie jaar of, in geval van aanvraag om toepassing van artikel 46ter, binnen vijf jaar na :

- ofwel de datum van de registratie van het document dat tot de heffing van het evenredig registratierecht aanleiding geeft, wanneer dat document binnen de ervoor bepaalde termijn ter registratie wordt aangeboden;
- ofwel de uiterste datum voor tijdige aanbieding ter registratie, wanneer dat document ter registratie wordt aangeboden na het verstrijken van de ervoor bepaalde termijn.

c) zich ertoe verbinden hun hoofdverblijfplaats in het verkregen onroerend goed te behouden gedurende een ononderbroken periode van minstens vijf jaar vanaf het tijdstip waarop ze hun hoofdverblijfplaats gevestigd hebben in het onroerend goed waarvoor de vermindering is verkregen.

Ingeval de verklaring bedoeld in 2°, a), van het vijfde lid, onjuist wordt bevonden, zijn de verkrijgers ondeelbaar gehouden tot betaling van de aanvullende rechten op het bedrag waarmee de belastbare grondslag werd verminderd, en van een boete gelijk aan die aanvullende rechten.

Dezelfde aanvullende rechten en boete zijn ondeelbaar verschuldigd door de verkrijgers indien geen van hen de in
2°, b), van het vijfde lid, bedoelde verbintenis naleeft. Komen sommige verkrijgers de bedoelde verbintenis niet na, dan worden de aanvullende rechten en de boete waartoe zij ondeelbaar gehouden zijn, bepaald naar verhouding van hun wettelijk aandeel in het verkregen onroerend goed. Indien de niet-naleving van de verbintenis het gevolg is van overmacht is de boete evenwel niet verschuldigd; hetzelfde geldt ook, bij wege van teruggaaf overeenkomstig artikel 209, eerste lid, 7°, voor de aanvullende rechten, wanneer de termijn bedoeld in het vijfde lid, 2°, b), niet werd gerespecteerd als gevolg van een geval van overmacht, op voorwaarde dat de verkrijgers hun hoofdverblijfplaats vestigen op de plaats van het verkregen onroerend goed van zodra de overmacht ophoudt.
Wanneer de toepassing van artikel 46ter werd gevraagd, wordt om te beoordelen of de verbintenis bedoeld in het vijfde lid, 2°, b), werd nageleefd, rekening gehouden met een termijn van vijf jaar wanneer de in artikel 46ter, vierde lid, 1°, bedoelde voorwaarde niet werd nageleefd.

Behoudens overmacht, zijn aanvullende rechten op het bedrag waarmee de belastbare grondslag werd verminderd ondeelbaar verschuldigd door de verkrijgers indien geen van hen de in het vijfde lid, 2°, c), bedoelde verbintenis naleeft. Deze aanvullende rechten worden verminderd in verhouding tot het aantal volledige ononderbroken jaren tijdens welke de voornoemde verbintenis werd nageleefd.

###### Art. 46ter

(van toepassing vanaf 01.04.2024)

(lid 1, 1°, gewijzigd bij art. 77 van de ordonnantie van 07.03.2024 (B.S., 22.03.2024). Tekst van toepassing vanaf 01.04.2024 (art. -))

Voor de toepassing van dit artikel, wordt verstaan onder :

1° « energieklasse » : de energieklasse of energieklassen gegroepeerd onder dezelfde letter die het energieprestatieniveau uitdrukken in de zin van artikel 2.1.1, 1° van het Brussels Wetboek Lucht, Klimaat en Energiebeheer, zoals bepaald door de Brusselse Hoofdstedelijke Regering ter uitvoering van de artikelen 2.2.2, § 1, en 2.2.4/1, § 3, van hetzelfde Wetboek;

2° « EPB-certificaat » : het EPB-certificaat in de zin van artikel 2.1.1, 11° van het Brussels Wetboek Lucht, Klimaat en Energiebeheer.
De in artikel 46bis, eerste en tweede lid, bedoelde vermindering van de belastbare grondslag wordt verhoogd in geval van verbetering van de energieprestatie van het aangekochte goed, volgens de door dit artikel vastgestelde modaliteiten en voorwaarden.

Het bedrag van de in het tweede lid bedoelde verhoging van de vermindering van de belastbare grondslag is gelijk aan 25.000 euro voor elke uitgevoerde verbetering van de energieklasse. De verhoging van de vermindering van de belastbare grondslag wordt bepaald in functie van de verbetering van de energieprestatie vermeld in de in het vierde lid, 2°, b) bedoelde verbintenis.

De in het tweede lid bedoelde verhoging van de vermindering van de belastbare grondslag is, naast de in artikel 46bis, vijfde lid, bedoelde voorwaarden, onderworpen aan de naleving van de volgende voorwaarden:

1° de energieprestatie van het aangekochte goed wordt met ten minste twee energieklassen verbeterd binnen de vijf jaar vanaf:

- ofwel de datum van de registratie van het document dat tot de heffing van het evenredig registratierecht aanleiding geeft, wanneer dat document binnen de ervoor bepaalde termijn ter registratie wordt aangeboden;

- ofwel de uiterste datum voor de tijdige aanbieding ter registratie, wanneer dat document ter registratie wordt aangeboden na het verstrijken van de ervoor bepaalde termijn;

2° in of onderaan het document dat aanleiding geeft tot de heffing van het evenredig registratierecht of in een bij dat document gevoegd en ondertekend geschrift, moeten de verkrijgers:

a) de gegevens vermelden betreffende de energieprestatie van het aangekochte goed volgens het meest recente, geldige EPB-certificaat op de datum van de overeenkomst tot verkrijging, namelijk het nummer van het EPBcertificaat, de uitgiftedatum en de in het certificaat opgenomen energieklasse;

b) zich ertoe verbinden de in 1° bedoelde verbintenis na te leven, met vermelding van de verbetering van de energieklassen, met een minimum van twee, die in aanmerking te nemen zijn voor de vaststelling van het in het derde lid bedoelde bedrag van de verhoging van de vermindering van de belastbare grondslag;

3° het EPB-certificaat waarvan de gegevens zijn vermeld in 2°, a) wordt gevoegd bij het document dat aanleiding geeft tot de heffing van het evenredig registratierecht.

De controle op de naleving van de voorwaarde bedoeld in het vierde lid, 1° wordt uitgevoerd rekening houdend met de energieklasse opgenomen in het EPB-certificaat bedoeld in het vierde lid, 2°, a), en de energieklasse opgenomen in het meest recente geldige EPB-certificaat opgesteld voor het aangekochte goed op het einde van de termijn. De verkrijgers moeten dit EPB-certificaat meedelen aan de ontvanger van het bevoegde kantoor van de Algemene Administratie van de Patrimoniumdocumentatie binnen een termijn van zes maanden vanaf het verstrijken van de termijn bedoeld in het vierde lid, 1°.

Ingeval een van de in artikel 46bis, vijfde lid, bedoelde voorwaarden niet wordt nageleefd, zijn de verschuldigde aanvullende rechten en boetes, met toepassing van artikel 46bis, zesde, zevende of achtste lid, naargelang het geval, eveneens verschuldigd, rekening houdend met het bedrag van de verhoging van de vermindering van de belastbare grondslag bedoeld in het derde lid.
Ingeval de in het vierde lid, 2°, a) vermelde gegevens onjuist zijn, zijn de verkrijgers ondeelbaar gehouden tot betaling van de aanvullende rechten op het in het derde lid bedoelde bedrag van de verhoging van de vermindering van de belastbare grondslag, en van een boete gelijk aan de helft van deze aanvullende rechten, zonder dat die niet minder dan 625 euro kan bedragen.

Ingeval de verbintenis bedoeld in het vierde lid, 2°, b) niet wordt nagekomen, zijn de verkrijgers ondeelbaar gehouden tot betaling van de aanvullende rechten op het in het derde lid bedoelde bedrag van de verhoging van de vermindering van de belastbare grondslag en van een boete gelijk aan tien procent van deze rechten zonder dat die niet minder dan 625 euro kan bedragen, wanneer de niet nagekomen verbintenis bestaat uit het niet verbeteren van de energieklasse tot het minimum bedoeld in het vierde lid, 1°. De boete is evenwel niet verschuldigd wanneer door overmacht aan de verbintenis niet voldaan kon worden.

###### Art. 47

(van toepassing vanaf 17.01.1959)

(gewijzigd bij art. 3 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Wanneer de overeenkomst op het vruchtgebruik van een onroerend goed slaat, wordt de in artikel 46 bedoelde verkoopwaarde vertegenwoordigd door de som verkregen door vermenigvuldiging van de jaarlijkse opbrengst of, bij ontstentenis daarvan, van de huurwaarde van het goed, met het getal dat in de onderstaande tabel is opgegeven en afhankelijk is van de leeftijd, welke degene op wiens hoofd het vruchtgebruik is gevestigd, op de dag van de akte heeft:

Getal                               Leeftijd
18                 20 jaar of minder
17       meer dan 20 jaar en niet meer dan 30 jaar;
16       meer dan 30 jaar en niet meer dan 40 jaar;
14       meer dan 40 jaar en niet meer dan 50 jaar;
13       meer dan 50 jaar en niet meer dan 55 jaar;
11       meer dan 55 jaar en niet meer dan 60 jaar;
9,5       meer dan 60 jaar en niet meer dan 65 jaar;
8        meer dan 65 jaar en niet meer dan 70 jaar;
6        meer dan 70 jaar en niet meer dan 75 jaar;
4        meer dan 75 jaar en niet meer dan 80 jaar;
2        meer dan 80 jaar;

Is het vruchtgebruik voor een beperkte tijd gevestigd, zo is de verkoopwaarde vertegenwoordigd door de som verkregen door het kapitaliseren ad 4 pct. van de jaarlijkse opbrengst, rekening gehouden met de bij de overeenkomst gestelde duur van het vruchtgebruik, maar zonder te mogen overschrijden hetzij de naar voorgaande alinea bepaalde waarde, zo het gaat om een ten bate van een natuurlijke persoon gevestigd vruchtgebruik, hetzij het bedrag van twintigmaal de opbrengst, zo het vruchtgebruik ten bate van een rechtspersoon is gevestigd.
In geen geval mag aan het vruchtgebruik een hogere waarde dan de vier vijfden van de verkoopwaarde van de volle eigendom worden toegewezen.

###### Art. 48

(van toepassing vanaf 01.02.1940)

Gaat de overeenkomst over de blote eigendom van een onroerend goed waarvan het vruchtgebruik door de vervreemder is voorbehouden, zo mag de belastbare grondslag niet lager zijn dan de verkoopwaarde van de volle eigendom.

###### Art. 49

(van toepassing vanaf 01.02.1940)

Gaat de overeenkomst over de blote eigendom van een onroerend goed, zonder dat het vruchtgebruik door de vervreemder is voorbehouden, zoo mag de belastbare grondslag niet lager zijn dan de verkoopwaarde van de volle eigendom, na aftrekking van de overeenkomstig artikel 47 berekende waarde van het vruchtgebruik.

###### Art. 50

(van toepassing vanaf 01.02.1940)

Wordt of werd het vruchtgebruik op het hoofd van twee of meer personen gevestigd, met recht van aanwas of van terugvalling, zo is de voor de toepassing van artikelen 47 en 49 in aanmerking te nemen leeftijd die van de jongste persoon.

§ 2. Verkopingen aan bouwmaatschappijen tot nut van het algemeen

###### Art. 51

(van toepassing vanaf 01.01.1990)

(aangevuld bij art. 145 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Het bij artikel 44 vastgelegd recht wordt tot 6 t.h. verlaagd voor de verkopingen gedaan met het oog op de verwezenlijking van haar maatschappelijk doel:

1° aan maatschappijen erkend hetzij door de Nationale Maatschappij voor de Huisvesting, hetzij door de Nationale Landmaatschappij, hetzij door de Gewestelijke Maatschappijen opgericht in uitvoering van de wet van 28 december 1984 tot afschaffing of herstructurering van sommige instellingen van openbaar nut.

2° aan de samenwerkende maatschappij «Woningsfonds van de Bond der Kroostrijke Gezinnen in België», aan de coöperatieve vennootschappen Vlaams Woningfonds van de Grote Gezinnen, Woningfonds van de Kroostrijke Gezinnen van Wallonië en Woningfonds van de gezinnen van het Brusselse Gewest.
Wat betreft de onder 1° hierboven bedoelde maatschappijen, wordt de verlaging slechts toegestaan mits het bewijs geleverd wordt van de erkenning der verkrijgende maatschappij.

###### Art. 51bis

(van toepassing vanaf 19.09.2013)

(ingevoegd bij art. 2 van de ordonnantie van 26.07.2013 (B.S., 09.09.2013). Tekst van toepassing vanaf 19.09.2013 (art. -))

Het in artikel 44 vastgestelde recht wordt verlaagd tot 0% voor de verkoop, de ruiling en iedere overeenkomst tot overdracht onder bezwarende titel van eigendom of vruchtgebruik van onroerende goederen gesloten tussen erkende openbare vastgoedmaatschappijen.

§ 3. Verkopingen aan de met regeringspremie begunstigde kopers

###### Art. 52

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 146 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Het recht wordt tot 1,50 t.h. verlaagd voor de verkopingen van woningen toegestaan door de Nationale Maatschappij voor de Huisvesting, de Nationale Landmaatschappij, de door hen of door de Gewestelijke Maatschappijen opgericht in uitvoering van de wet van 28 december 1984 tot afschaffing of herstructurering van sommige instellingen van openbaar nut erkende maatschappijen, de openbare besturen of de openbare instellingen, aan personen wie de door de Staat verleende aankooppremie ten goede komt.

Het gebeurlijk intrekken van die premie brengt voor de verkrijger der verplichting mede het verschuldigde recht tot het bij artikel 44 vastgesteld percentage aan te zuiveren.

§ 4. Verkopingen van kleine landeigendommen en bescheiden woningen

###### Art. 53

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 54

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13)

(…)

###### Art. 55

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 56

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 57

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 58

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 59

(van toepassing vanaf 01.01.2003)
(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 60

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 611

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3) err. (B.S., 16.01.2003). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

###### Art. 612

(van toepassing vanaf 01.01.2003)

(opgeheven bij art. 11 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3) err. (B.S., 16.01.2003). Tekst van toepassing vanaf 01.01.2003 (art. 13))

(…)

§ 5. Verkopingen aan personen die hun beroep maken van de aankoop van onroerende goederen met het oog op wederverkoop

###### Art. 62

(van toepassing vanaf 01.01.2003)

(gewijzigd bij art. 3 van de ordonnantie van 20.12.2002 (B.S., 31.12.2002 - ed. 3). Tekst van toepassing vanaf 01.01.2003 (art. 13)) Het in artikel 44 bepaalde recht wordt tot 8 pct. verminderd voor de verkopingen die uit de hand en bij authentieke akte gedaan worden aan personen die hun beroep maken van het kopen en verkopen van onroerende goederen.

Deze vermindering is echter niet van toepassing op de verkopen van landeigendommen waarvan de verkoopswaarde het bedrag niet te boven gaat dat verkregen wordt bij vermenigvuldiging van het kadastraal inkomen met een door de Koning vastgestelde coëfficiënt.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 631

(van toepassing vanaf 01.01.2028)

(lid 1, 1°, vervangen bij art. 62 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Om de in vorenstaand artikel voorziene vermindering te genieten, moet de beroepspersoon:

1° in de vorm en aan het bij koninklijk besluit te bepalen kantoor, een beroepsverklaring ondertekenen en verzenden;

2° op eigen kosten, zekerheid stellen voor de invordering van de sommen welke bij toepassing van artikel 64 en volgende artikelen van deze paragraaf vorderbaar kunnen worden;

3° de erkenning verkregen hebben van een in België gevestigd vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem instaat voor de nakoming van zijn fiscale verplichtingen indien hij:

a) een natuurlijke persoon is en zijn wettelijke verblijfplaats buitend de Europese Economische Ruimte heeft;

b) een rechtspersoon is zonder vestiging in België en wiens maatschappelijke zetel gevestigd is buiten de Europese Economische Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte van verkrijging, hetzij in een onderaan de akte gestelde verklaring of in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie, door de verkrijger of, in zijn naam, door de werkende notaris ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet een uittreksel uit de kadastrale legger betreffende de verkregen goederen aan de akte gehecht zijn wanneer zij ter registratie wordt aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en, in voorkomend geval, het uittreksel uit de kadastrale legger, zoals bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het gewoon recht geregistreerd en geen vordering tot teruggaaf is ontvankelijk.
Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan de erkenning verkrijgen van een in België gevestigde vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem instaat voor de nakoming van zijn fiscale verplichtingen.

###### Art. 631

(van toepassing vanaf 16.05.2011)

(gewijzigd bij art. 62 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst van toepassing vanaf 16.05.2011 (art. -))

Om de in vorenstaand artikel voorziene vermindering te genieten, moet de beroepspersoon:

1° in de vorm en op het bij koninklijk besluit te bepalen kantoor, een beroepsverklaring ondertekenen en indienen;

2° op eigen kosten, zekerheid stellen voor de invordering van de sommen welke bij toepassing van artikel 64 en volgende artikelen van deze paragraaf vorderbaar kunnen worden;

3° de erkenning verkregen hebben van een in België gevestigd vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem instaat voor de nakoming van zijn fiscale verplichtingen indien hij:

a) een natuurlijke persoon is en zijn wettelijke verblijfplaats buitend de Europese Economische Ruimte heeft;

b) een rechtspersoon is zonder vestiging in België en wiens maatschappelijke zetel gevestigd is buiten de Europese Economische Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte van verkrijging, hetzij in een onderaan de akte gestelde verklaring of in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie, door de verkrijger of, in zijn naam, door de werkende notaris ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet een uittreksel uit de kadastrale legger betreffende de verkregen goederen aan de akte gehecht zijn wanneer zij ter registratie wordt aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en, in voorkomend geval, het uittreksel uit de kadastrale legger, zoals bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het gewoon recht geregistreerd en geen vordering tot teruggaaf is ontvankelijk.

Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan de erkenning verkrijgen van een in België gevestigde vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem instaat voor de nakoming van zijn fiscale verplichtingen.

###### Art. 632

(van toepassing vanaf 24.02.1959)

(ingevoegd bij art. 3 van de wet van 03.02.1959 (B.S., 14.02.1959). Tekst van toepassing vanaf 24.02.1959 (art. -)) Wanneer door een schatting volgens artikelen 190 en 199 bevonden wordt dat de verkoopwaarde van landgoederen, welke met toepassing van het bij artikel 62 voorzien verminderd recht verkregen werden, op de datum van de verkrijging de door laatstbedoeld artikel vastgestelde grens niet overtrof, is de verkrijger gehouden tot het betalen van het bijkomend recht berekend op de grondslag die voor de heffing van het verminderd recht gediend heeft, van een zelfde som als boete en van de kosten der procedure.

###### Art. 64

(van toepassing vanaf 01.02.1940)

Het bij artikel 44 bepaald recht wordt vorderbaar ten laste van de verkrijger van het onroerend goed die het voordeel van artikel 62 heeft genoten, bijaldien bedoelde verkrijger of zijn rechthebbenden dit onroerend goed niet hebben vervreemd door wederverkoop of alle andere overdracht onder bezwarende titel, andere dan den inbreng in vennootschap, vastgesteld bij authentieke akte uiterlijk verleden op 31 december van het tiende jaar na de datum van de koopakte.

De wederverkoop aan een beroepspersoon met toepassing van artikel 62 staat deze vorderbaarheid niet in de weg.

###### Art. 65

(van toepassing vanaf 01.02.1940)

De verkrijger mag de betaling aanbieden van het gewoon recht vóór het verstrijken van de in eerste alinea van vorig artikel voorziene termijn.

###### Art. 66

(van toepassing vanaf 01.02.1940)

Het recht dat voor de verkrijging van het goed betaald werd, mag niet op de krachtens artikelen 64 en 65 verschuldigde rechten worden aangerekend.

###### Art. 67

(van toepassing vanaf 01.02.1940)

De overeenkomstig artikelen 64 en 65 vorderbare rechten worden berekend op de waarde die tot grondslag heeft gediend aan het voor de verkrijging betaald recht en naar het op de datum dezer verkrijging van kracht zijnde tarief.

Bijaldien slechts een deel van tegen een enige prijs aangekochte onroerende goederen wordt vervreemd, wordt de belastbare waarde van het niet vervreemde gedeelte bepaald naar verhouding van de grootte.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 68

(van toepassing vanaf 01.01.2028)

(lid 3, vervangen bij art. 63 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

In het geval van artikel 64 worden de gewone rechten vereffend op een verklaring die, binnen de eerste vier maanden na het verstrijken van het tiende jaar en op straf van boete gelijk aan de rechten, tot registratie dient aangeboden ten kantore in welks gebied de goederen gelegen zijn.

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter registratie een verklaring aanbieden waarin samenstelling en waarde zijn bepaald van de goederen waarvoor hij de rechten wenst te betalen.

De bij dit artikel voorgeschreven verklaringen worden door de belanghebbende of zijn aangenomen vertegenwoordiger ondertekend en vermelden de akte of de akten van verkrijging, het nieuwe feit waaruit de verschuldigdheid van het recht volgt en al de tot de vereffening van de belasting nodige gegevens. Een kopie wordt bewaard door de bevoegde dienst van de Algemene administratie van de patrimoniumdocumentatie.

###### Art. 68

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 152 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

In het geval van artikel 64 worden de gewone rechten vereffend op een verklaring die, binnen de eerste vier maanden na het verstrijken van het tiende jaar en op straf van boete gelijk aan de rechten, tot registratie dient aangeboden ten kantore in welks gebied de goederen gelegen zijn.

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter registratie een verklaring aanbieden waarin samenstelling en waarde zijn bepaald van de goederen waarvoor hij de rechten wenst te betalen.

De bij dit artikel voorgeschreven verklaringen, welke door belanghebbende of zijn aangenomen vertegenwoordiger worden ondertekend, worden in dubbel gesteld, en een exemplaar blijft op het kantoor der registratie. Deze verklaringen houden vermelding van de akte of de akten van verkrijging, van het nieuwe feit waaruit de verschuldigdheid van het recht volgt en al de tot de vereffening van de belasting nodige gegevens.

###### Art. 69

(van toepassing vanaf 16.05.2011)

(gewijzigd bij artikel 63 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst van toepassing vanaf 16.05.2011 (art. -)) Bij overlijden van den vertegenwoordiger van een beroepspersoon bedoeld in artikel 631, eerste lid, 3°, bij de intrekking van zijn erkenning of in geval hij onbekwaam wordt verklaard om als vertegenwoordiger op te treden, dient binnen zes maand in zijn vervanging voorzien.

Wanneer de door den verkrijger gestelde zekerheid ontoereikend wordt, dient hij, binnen de door het bestuur vastgestelde termijn, een aanvullende zekerheid te verstrekken.

Wordt aan vorenstaande voorschriften niet voldaan, zo wordt het volgens artikelen 66 en 67 berekend gewoon recht op de niet wederverkochte goederen vorderbaar.

###### Art. 70

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

De Minister van Financiën of zijn afgevaardigde bepaalt aard en bedrag der ter voldoening van artikelen 631, 2°, en 69 te stellen zekerheid of aanvullende zekerheid. Deze zekerheid dient gesteld onder de door de Minister of zijn afgevaardigde bepaalde voorwaarden en mag niet minder dan 5.000 EUR bedragen.

###### Art. 71

(van toepassing vanaf 01.02.1940)

Indien hij die een beroepsverklaring heeft ondertekend bij het verstrijken van een termijn van vijf jaar na die verklaring, niet bij machte is om door een reeks wederverkoper te laten blijken dat hij het aangegeven beroep werkelijk uitoefent, wordt hij schuldenaar van de gewone rechten op zijn aankopen, onder aftrek van de reeds geheven rechten, en daarenboven van een som gelijk aan de aanvullende rechten als boete.

§ 6. Ruiling van ongebouwde landgoederen

###### Art. 72

(van toepassing vanaf 30.11.1978)

(gewijzigd en aangevuld bij art. 2 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van toepassing vanaf 30.11.1978 (art.
2, KB van 13.11.1978 (B.S., 30.11.1978)))

Zijn vrijgesteld van het evenredig recht en onderworpen aan het algemeen vast recht, de ruilingen van ongebouwde landeigendommen waarvan de verkoopwaarde voor elk der kavels het bedrag niet te boven gaat dat verkregen wordt bij vermenigvuldiging van het kadastraal inkomen met een door de Koning vastgestelde coëfficiënt.
Evenwel wordt bij ongelijkheid van de kavels het bij artikel 44 bepaalde recht geheven op het waardeverschil of de opleg, indien deze groter is dan dat verschil. Dit recht wordt verlaagd tot 6 t.h. indien het waardeverschil of de opleg een vierde van de verkoopwaarde van de minste kavel niet te boven gaat.

De toepassing van dit artikel is ondergeschikt aan een drievoudige voorwaarde:

1° dat de verkoopwaarde van elke kavel door partijen wordt aangegeven, hetzij in de akte, hetzij onderaan de akte, vóór de registratie;

2° dat een uittreksel uit de kadastrale legger aan de akte wordt gehecht bij de registratie;

3° dat de partijen vóór de registratie, in een verklaring gedaan in de akte of onderaan op de akte, aanduiden of de geruilde onroerende goederen door henzelf of door derden worden geëxploiteerd en dat, in deze laatste onderstelling, de akte of een daaraan vóór de registratie gehecht schrijven de instemming inhoudt van alle exploitanten van de in de ruiling begrepen goederen.

###### Art. 731

(van toepassing vanaf 09.09.1952)

(vervangen bij art. 3 van de wet van 26.07.1952 (B.S., 30.08.1952). Tekst van toepassing vanaf 09.09.1952 (art. -))

Voor elke te laag bevonden opleg of waardeverschil is, behalve het ontdoken recht, een geldboete van hetzelfde bedrag als dit recht vorderbaar.

Hetzelfde geldt voor elke overschatting van de kavels die een vermindering van het recht tot gevolg heeft.

De geldboete is evenwel niet verschuldigd, indien het verschil tussen de verkoopwaarde van de kavels en de aangegeven schatting minder dan een achtste hiervan bedraagt.

Het bepaalde in de artikelen 189 tot 201 geldt mede voor de controle op de in dit artikel omschreven schattingen.

###### Art. 732

(van toepassing vanaf 30.11.1978)

(hersteld bij art. 3 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van toepassing vanaf 30.11.1978 (art. 2, KB van 13.11.1978 (B.S., 30.11.1978)))

In geval van onjuistheid van de verklaring betreffende de uitbating van de geruilde onroerende goederen, zijn de partijen ondeelbaar gehouden tot de betaling van het verschil tussen het gewoon recht en het geheven recht, alsook van een boete gelijk aan dat verschil.

§ 7. Afzonderlijke verkrijgingen van de grond en van de opstal of van de tot de dienst van het onroerend goed aangewende voorwerpen

###### Art. 74

(van toepassing vanaf 10.04.1994)

(gewijzigd bij art. 42 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

Wie bij een overdragende overeenkomst onder bezwarende titel, andere dan een inbreng in vennootschap vermeld in artikel 115bis, de eigendom heeft verkregen, hetzij van hout op stam onder beding van het te vellen, hetzij van gebouwen onder beding van ze te slopen, en nadien onder de levenden de eigendom verkrijgt van de grond vooraleer het hout gans geveld is of de gebouwen volomen gesloopt zijn, moet uit hoofde van de eerste verkrijging en op de grondslag aangewezen in artikel 45 en volgende, het voor de verkoop van onroerende goederen vastgesteld recht kwijten met aftrek van het evenredig registratierecht eventueel op deze verkrijging werd geheven.

Deze bepaling is evenwel niet van toepassing, zo er bewezen wordt dat de belasting over de toegevoegde waarde werd gekweten voor de levering van het hout op stam of van de te slopen gebouwen.

###### Art. 75

(van toepassing vanaf 10.04.1994)

(gewijzigd bij art. 43 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

Wordt als overdracht van een onroerend goed aangezien, die welke voortvloeit uit een overeenkomst onder de levenden te bezwarende titel, andere dan een inbreng in vennootschap vermeld in artikel 115bis, en welke over de eigendom gaat hetzij van hout op stam, hetzij van gebouwen, zo bewuste overdracht ten bate van de eigenaar van de grond wordt toegestaan.

Deze bepaling is niet van toepassing zo de belasting over de toegevoegde waarde verschuldigd is voor de levering van de goederen die in de overeenkomst begrepen zijn. De heffing van het vast recht is echter ondergeschikt aan de vermelding, in de akte of in een erbij gevoegd geschrift, vóór de registratie, van het kantoor, waar de verkoper periodiek de aangiften indient die voor de heffing van de belasting over de toegevoegde waarde zijn vereist.

§ 8. (…)

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van toepassing vanaf 31.07.1960 (art. -))

###### Art. 76

(van toepassing vanaf 31.07.1960)

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van toepassing vanaf 31.07.1960 (art. -))

(…)

#### Afdeling II - Openbare verkopingen van lichamelijke roerende goederen

(opschrift vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Art. 77

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Het recht wordt vastgesteld op 5 t.h. voor de openbare verkopingen van lichamelijke roerende goederen.

###### Art. 78

(van toepassing vanaf 01.01.1971)

(opgeheven bij art. 5 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van 19.12.1969 (B.S., 20.12.1969)))

(…)

###### Art. 79

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

De heffingsgrondslag wordt bepaald zoals gezegd in de artikelen 45 en 231.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 80

(van toepassing vanaf 01.01.2028)

(lid 2, gewijzigd bij art. 64 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Vrijgesteld van het recht van 5 pct. en onderworpen aan het algemeen vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als belastingplichtige in de zin van de wetgeving op de belasting over de toegevoegde waarde;
2° de openbare verkopingen van goederen bedoeld in de artikelen 2 en 3 van titel I van het Wetboek der met het zegel gelijkgestelde taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven mits in het proces-verbaal of in een geschrift dat bij het proces-verbaal vóór de registratie is gevoegd, vermeld wordt naar welk kantoor de verkoper de periodieke aangiften voor de belasting over de toegevoegde waarde moet verzenden.

###### Art. 80

(van toepassing vanaf 01.01.1978)

(vervangen bij art. 42 van de wet van 27.12.1977 (B.S., 30.12.1977) err. (B.S., 10.05.1978). Tekst van toepassing vanaf 01.01.1978 (art. 43))

Vrijgesteld van het recht van 5 pct. en onderworpen aan het algemeen vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als belastingplichtige in de zin van de wetgeving op de belasting over de toegevoegde waarde;

2° de openbare verkopingen van goederen bedoeld in de artikelen 2 en 3 van titel I van het Wetboek der met het zegel gelijkgestelde taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven mits in het proces-verbaal of in een geschrift dat bij het proces-verbaal vóór de registratie is gevoegd, vermeld wordt bij welk kantoor de verkoper de periodieke aangiften voor de belasting over de toegevoegde waarde moet indienen.

#### Afdeling III - (…)

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Art. 81

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 82

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

#### Afdeling IV - Huurcontracten

###### Art. 83

(van toepassing vanaf 01.01.2024)

(lid 1, 3°, gewijzigd bij art. 5 van de wet van 22.12.2023 (B.S., 29.12.2023 – ed. 1). Tekst van toepassing vanaf 01.01.2024 (art. 6))

Het recht wordt vastgesteld op:

1° 0,20 pct. voor contracten van verhuring, onderverhuring en overdracht van huur van onroerende goederen;

2° 1,50 pct. voor jacht- en vispacht;

3° 5 pct. voor contracten tot vestiging van een erfpacht- of opstalrecht en tot overdracht daarvan, behalve wanneer daardoor een vereniging zonder winstoogmerk, een internationale vereniging zonder winstoogmerk of een gelijkaardige rechtspersoon die opgericht is volgens en onderworpen is aan de wetgeving van een lidstaat van de Europese Economische Ruimte en die bovendien zijn statutaire zetel, zijn hoofdbestuur of zijn hoofdvestiging binnen de Europese Economische Ruimte heeft, titularis van het erfpacht- of opstalrecht wordt, in welk geval het recht wordt vastgesteld op 0,50 pct.

Een rechtspersoon is gelijkaardig aan een VZW wanneer de volgende voorwaarden cumulatief zijn vervuld:

1° het doel van de rechtspersoon is belangeloos, zonder winstoogmerk;

2° de activiteit van de rechtspersoon mag niet leiden tot de materiële verrijking van:

a) de stichters, de leden of de bestuurders ervan;

b) de echtgenoot, de wettelijk samenwonende, een bloedverwant in de rechte lijn, een bloedverwant in de zijlijn die tot een stichter in een erfgerechtigde graad staat, of een andere rechtsopvolger van een stichter ervan;

c) de echtgenoot of een wettelijk samenwonende van een persoon bedoeld in a) en b);
3° in geval van ontbinding of vereffening van de rechtspersoon mogen de goederen ervan niet toekomen aan personen vermeld onder 2°, maar moeten ze worden overgedragen aan:

a) hetzij een gelijkaardige rechtspersoon die zelf is opgericht volgens en onderworpen aan de wetgeving van een lidstaat van de Europese Economische Ruimte en bovendien zijn statutaire zetel, zijn hoofdbestuur of zijn hoofdvestiging binnen de Europese Economische Ruimte heeft;

b) hetzij een lidstaat is van de Europese Economische Ruimte of een territoriaal gedecentraliseerde overheid van een EER-lidstaat is of nog, een dienstgewijze gedecentraliseerde overheid is van een dergelijke publiekrechtelijke rechtspersoon.

Contracten tot vestiging van erfpacht- of opstalrecht en overdrachten daarvan worden, voor het overige, met huurcontracten en -overdrachten gelijkgesteld, voor de toepassing van dit wetboek, behalve voor de toepassing van de artikelen 2quater en 161, 12°.

Dit recht is evenwel niet verschuldigd in geval van toepassing van artikel 140bis (1).
(1) Volgens art. 20, § 2, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 - ed. 3): « Elke vermelding van 140bis in het volgende ».

###### Art. 84

(van toepassing vanaf 27.09.1947)

(enkel de Nederlandse tekst werd gewijzigd bij art. 22 van de wet van 13.08.1947 (B.S., 17.09.1947). Tekst van toepassing vanaf 27.09.1947))

De belastbare grondslag wordt als volgt vastgelegd:

Voor huur van bepaalde duur, geldt als grondslag van het voor de duur van het contract of, ter zake overdracht, voor het nog te lopen tijdperk samengevoegd bedrag van huursommen en aan huurder opgelegde lasten;

Is zij levenslang of van onbepaalde duur, zo geldt als grondslag het tienvoudig bedrag van de jaarlijkse huurprijs en lasten, zonder dat de belastbare som minder moge zijn dan het samengevoegd bedrag van huurprijzen en aan huurder opgelegde lasten voor de bij de huurakte voorziene minimumduur.

Bij overdracht van huur, wordt het bedrag of de waarde van de gebeurlijk ten bate van de overdrager bedongen prestatiën gevoegd bij de heffingsgrondslag zoals hij hiervoor is bepaald.

#### Afdeling V - (…)

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Art. 85

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 86

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

#### Afdeling VI - Hypotheekvestigingen

(gewijzigd bij art. 55 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van toepassing vanaf 01.01.2018 (art. 70))

###### Art. 87

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Worden aan een recht van 1 t.h. onderworpen, de vestigingen van een hypotheek op een in België gelegen onroerend goed.

###### Art. 88

(van toepassing vanaf 01.01.2018)

(vervangen bij art. 56 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van toepassing vanaf 01.01.2018 (art. 70)) (1)

De vestigingen van een hypotheek op een schip dat niet naar zijn aard voor het zeevervoer bestemd is, worden aan een recht van 0,50 pct. onderworpen.
Het recht van 0,50 pct., geheven overeenkomstig art. 88 W.Reg. vóór de inwerkingtreding van deze wet, wordt in mindering gebracht op het krachtens art. 87 van hetzelfde Wetboek verschuldigde recht, wanneer later een hypotheek wordt gevestigd tot zekerheid van dezelfde schuld (art. 69).

###### Art. 89

(van toepassing vanaf 01.01.2018)

(gewijzigd bij art. 57 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van toepassing vanaf 01.01.2018 (art. 70))

De bij artikelen 87 en 88 bepaalde rechten zijn van toepassing zelfs wanneer de hypotheek gevestigd is tot zekerheid van een toekomstige schuld, van een voorwaardelijke of eventuele schuld of van een verbintenis om iets te doen.

###### Art. 90

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

De bij artikelen 87 en 88 bepaalde rechten zijn niet verschuldigd zo de gewaarborgde verbintenis voortkomt uit een contract waarop een evenredig recht van minstens 1 pct. werd geheven.

###### Art. 91

(van toepassing vanaf 01.01.2018)

(vervangen bij art. 58 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van toepassing vanaf 01.01.2018 (art. 70))

De vestiging van een hypotheek op een in België gelegen onroerend goed tot zekerheid van een schuld die gewaarborgd is door een hypotheek op een schip dat niet naar zijn aard voor het zeevervoer bestemd is, wordt aan het recht van 1 pct. onderworpen onder aftrek, in voorkomend geval, van het krachtens artikel 88 geheven recht van 0,50 pct.

###### Art. 921

(van toepassing vanaf 21.12.2018)

(vervangen bij art. 2 van de ordonnantie van 13.12.2018 (B.S., 21.12.2018). Tekst van toepassing vanaf 21.12.2018 (art. 6))

Onverminderd artikel 91, dekt het in artikel 88 en in artikel 3, eerste lid, 7°, a) van de bijzondere wet betreffende de financiering van de Gemeenschappen en de Gewesten bedoeld recht alle vestiging van hypotheek welke naderhand tot zekerheid van eenzelfde schuldvordering en van hetzelfde gewaarborgd bedrag mocht worden toegestaan.

###### Art. 922

(van toepassing vanaf 01.01.2018)

(gewijzigd bij art. 60 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van toepassing vanaf 01.01.2018 (art. 70)) De overdracht van een hypotheek op een in België gelegen onroerend goed met inbegrip van de voorrechten bedoeld bij artikel 27 van de wet van 16 december 1851 of van een hypotheek op een schip dat niet naar zijn aard voor het zeevervoer bestemd is, ingevolge de overdracht onder bezwarende titel van de schuldvordering, de contractuele indeplaatsstelling of elke andere verrichting onder bezwarende titel, wordt onderworpen aan een recht van 1 pct. of van 0,50 pct., al naar gelang de overdracht al dan niet een hypotheek op een onroerend goed betreft.

###### Art. 93

(van toepassing vanaf 01.01.2018)

(gewijzigd bij art. 61 van de wet van 25.12.2016 (B.S., 30.12.2017). Tekst van toepassing vanaf 01.01.2018 (art. 70))

Het recht van 1 pct. of van 0,50 pct. wordt vereffend op het bedrag van de sommen die door de hypotheek gewaarborgd zijn, met uitsluiting van de interesten of rentetermijnen van drie jaren, die gewaarborgd zijn door artikel 87 van de wet van 16 december 1851.

###### Art. 94

(van toepassing vanaf het aanslagjaar 2019)

(gewijzigd bij art. 12 van de wet van 03.07.2018 (B.S., 19.07.2018). Tekst van toepassing vanaf het aanslagjaar 2019 (art.
13))

Schepen worden niet onderworpen aan het in artikel 88 bepaalde recht op voorwaarde dat:

1° een getuigschrift, afgeleverd door het Belgisch Scheepsregister, ter bevestiging dat het schip is geregistreerd in het Belgisch register der zeeschepen of dat voor het schip een aangifte voor registratie in het Belgisch register der zeeschepen werd ingediend, aan de akte wordt gehecht;

2° de akte, of een door de hypotheeksteller gewaarmerkte en ondertekende verklaring onderaan op de akte, uitdrukkelijk vermeldt:

a) dat het schip naar zijn aard voor het zeevervoer bestemd is;

b) dat de hypotheeksteller de verbintenis aangaat om de voorwaarden inzake het behoud of de uitbreiding van de tonnage en inzake de bewijslevering van naleving van de tonnage-eis en van het voldoen van elk schip van de vloot aan de betreffende internationale en communautaire normen, zoals die voorwaarden nader zijn omschreven in punt 3.1, leden 8 en 9 van de Mededeling C(2004) van de Europese Commissie, na te leven gedurende vijf jaar te rekenen van de datum van de registratie van de akte.

Als de in het eerste lid, 2°, a) bedoelde verklaring onjuist blijkt of als de in het eerste lid, 2°, b) bedoelde verbintenis niet wordt nageleefd, is de hypotheeksteller gehouden tot betaling van het evenredig recht, vermeerderd met de interesten.
De hypotheeksteller kan aanbieden het evenredig recht vermeerderd met de interesten te betalen alvorens de in het eerste lid, 2°, b) voorziene termijn is verstreken.

#### Afdeling VII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Art. 95

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 96

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 97

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 98

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

#### Afdeling VIII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Art. 99

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 100

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 101

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(...)

###### Art. 102

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(…)

#### Afdeling IX - Opheffingen

###### Art. 103

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 92 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

§ 1. Elke gehele of gedeeltelijke handlichting van een in België genomen hypothecaire inschrijving, gedaan bij een akte bedoeld in artikel 19, 1°, is onderworpen aan een specifiek vast recht van 75 euro.
§ 2. In afwijking van paragraaf 1 geven slechts aanleiding tot éénmaal de heffing van het recht bedoeld in paragraaf 1, de handlichtingen vastgesteld in één akte:

1° van inschrijvingen genomen lastens éénzelfde schuldenaar-hypotheeksteller;

2° van inschrijvingen genomen lastens een schuldenaar-hypotheeksteller en een persoon-hypotheeksteller als waarborg voor de eerstgenoemde;

3° van inschrijvingen van wettelijke hypotheken lastens éénzelfde schuldenaar;

4° van door een hypotheekbewaarder of de Algemene Administratie van de Patrimoniumdocumentatie ambtshalve genomen inschrijvingen;

5° die geschieden in het kader van een openbare verkoping na beslag of van een verkoop uit de hand bedoeld in artikel 1580bis van het Gerechtelijk Wetboek.

###### Art. 104

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17 jan 1959 (art. -))

(...)

###### Art. 105

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 153, 1° van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(...)

###### Art. 106

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 153, 2°, van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 107

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -)) (...)

###### Art. 108

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 153, 3°, van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(...)

#### Afdeling X - Verdelingen

###### Art. 109

(van toepassing vanaf 01.07.2022)

(3°, gewijzigd bij art. 20 van de ordonnantie van 13.10.2022 (B.S., 19.10.2022). Tekst van toepassing vanaf 01.07.2022 (art.
24))

Het recht wordt op 1 t.h. vastgesteld voor:

1° de gedeeltelijke of gehele verdelingen van onroerende goederen;

2°de afstanden onder bezwarende titel, onder medeëigenaars, van onverdeelde delen in onroerende goederen.

3° de omzetting bedoeld in boek 4, titel 1, ondertitel 7 van het Burgerlijk Wetboek, zelfs indien er geen onverdeeldheid is.

###### Art. 110

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Voor de goederen waarvan de akte de onverdeeldheid doet ophouden onder al de medeëigenaars, wordt het recht vereffend op de waarde van die goederen.

Voor de goederen waarvan de akte de onverdeeldheid niet doet ophouden onder al de medeëigenaars, wordt het recht vereffend op de waarde der afgestane delen.

###### Art. 111

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -)) De heffingsgrondslag is bepaald door de overeengekomen waarde der goederen, zoals ze blijkt uit de bepalingen van de akte, zonder dat hij lager dan de verkoopwaarde mag zijn.

Wanneer de bepalingen van de akte het niet mogelijk maken de overeengekomen waarde vast te stellen, wordt daarin overeenkomstig artikel 168 voorzien.

In voorkomend geval wordt de verkoopwaarde van het vruchtgebruik of van de blote eigendom overeenkomstig artikelen 47 tot 50 vastgesteld.

###### Art. 112

(van toepassing vanaf 17.01.1959)

(opgeheven bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

(...)

###### Art. 113

(van toepassing vanaf 17.01.1959)

(vervangen bij art. 17 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

In geval van toebedeling bij verdeling of van afstand van onverdeelde delen aan een derde die bij overeenkomst een onverdeeld deel heeft verkregen van goederen toebehorende aan één of meer personen, wordt het recht, met afwijking van artikel 109, geheven tegen het voor de overdrachten onder bezwarende titel vastgesteld tarief, op de delen waarvan de derde ten gevolge van de overeenkomst eigenaar wordt, en zulks volgens de in artikelen 45 tot 50 voorziene regels.

Deze bepaling is van toepassing wanneer de toebedeling van goederen of de afstand van onverdeelde delen gedaan wordt aan de erfgenamen of legatarissen van de overleden derde verkrijger. Zij is niet van toepassing wanneer de derde, aan wie de toebedeling of de afstand gedaan wordt, met anderen het geheel van één of meer goederen heeft verkregen.

###### Art. 114

(van toepassing vanaf 01.02.1940)

De bepalingen van deze afdeling zijn niet van toepassing op de uitvoering van een beding van terugvalling of van aanwas.

#### Afdeling XI - Vennootschappen

###### Art. 115

(van toepassing vanaf 25.11.2025)

(lid 1, gewijzigd en lid 3, opgeheven bij art. 22 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

Aan een recht van 0 pct. wordt onderworpen de inbreng van roerende goederen in vennootschappen waarvan hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel in België en de zetel der werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie, is gevestigd, onverschillig of de inbreng bij de oprichting van de vennootschap of naderhand plaats heeft.

Het recht wordt vereffend op het totaal bedrag van de inbrengen.

###### Art. 115bis

(van toepassing vanaf 25.11.2025)

(lid 1, gewijzigd bij art. 23 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

De inbrengen van onroerende goederen, andere dan die welke gedeeltelijk of geheel tot bewoning aangewend worden of bestemd zijn en door een natuurlijke persoon ingebracht worden, in vennootschappen waarvan de zetel der werkelijke leiding in België gevestigd is, of de statutaire zetel in België en de zetel van werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie gevestigd is, worden aan het recht van 0 pct. onderworpen.

In geval van onjuiste verklaring betreffende de aanwending of de bestemming van het onroerend goed, zijn de aanvullende rechten opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.

###### Art. 116

(van toepassing vanaf 25.11.2025)

(gewijzigd bij art. 24 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

Aan een recht van 0 pct. wordt onderworpen de vermeerdering van het kapitaal, zonder nieuwe inbreng, van een vennootschap waarvan hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel in België en de zetel der werkelijke leiding buiten het grondgebied van de lidstaten van de Europese Unie, is gevestigd.

Het recht wordt vereffend op het bedrag van de vermeerdering.

Het recht is niet verschuldigd in de mate waarin het kapitaal vermeerderd wordt door inlijving van reserves of provisies, die gevestigd werden, bij gelegenheid van inbrengen gedaan in de vennootschap, ter vertegenwoordiging van het geheel of een gedeelte van het bedrag van die inbrengen dat onderworpen werd aan het bij de artikelen 115 en 115bis bedoeld recht.

###### Art. 117

(van toepassing vanaf 25.11.2025)

(gewijzigd bij art. 25 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

§ 1. Het bij de artikelen 115 en 115bis bepaalde recht is niet verschuldigd in geval van inbreng van de universaliteit der goederen van een vennootschap, bij wijze van fusie, splitsing of anderszins, in een of meer nieuwe of bestaande vennootschappen.

Deze bepaling is evenwel slechts toepasselijk op voorwaarde:

1° dat de vennootschap die de inbreng doet de zetel van haar werkelijke leiding of haar statutaire zetel heeft op het grondgebied van een lidstaat van de Europese Unie;

2° a) dat de rechtshandeling door artikel 12:7 van het Wetboek van vennootschappen en verenigingen wordt gelijkgesteld met fusie door overneming, of

b) dat, eventueel na aftrek van de op het tijdstip van de inbreng door de inbrengende vennootschap verschuldigde sommen, de inbreng uitsluitend vergoed wordt hetzij door toekenning van aandelen, hetzij door toekenning van aandelen samen met een storting in contanten die het tiende van de nominale waarde of, bij gebrek aan een nominale waarde, van de fractiewaarde van de toegekende aandelen niet overschrijdt. Indien het Belgisch of buitenlands recht dat de verkrijgende vennootschap beheerst niet in een begrip gelijkaardig aan dat van het kapitaal van een naamloze vennootschap voorziet, wordt met de fractiewaarde gelijkgesteld, de inbrengwaarde, zoals die blijkt uit de jaarrekening, van alle door de aandeelhouders of vennoten toegezegde inbrengen in geld of in natura, met uitzondering van de inbrengen in nijverheid, in voorkomend geval verhoogd met de reserves die op grond van een statutaire bepaling slechts aan de aandeelhouders of vennoten kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen.

§ 2. Het in de artikelen 115 en 115bis bedoelde recht is eveneens niet verschuldigd voor de inbrengen gedaan door een vennootschap waarvan de zetel der werkelijke leiding of de statutaire zetel gevestigd is op het grondgebied van een lidstaat van de Europese Unie, van goederen die één of meer van haar bedrijfstakken uitmaken onder de volgende voorwaarden:

1° dat de inbreng het geheel omvat van de goederen die door de inbrengende vennootschap worden aangewend tot één of meer afdelingen van haar onderneming welke, op technisch en organisatorisch gebied, elk een autonome activiteit uitoefenen en op eigen kracht kunnen werken; en

2° dat, eventueel na aftrek van de bij de inbreng door de inbrengende vennootschap verschuldigde sommen die betrekking hebben op de ingebrachte bedrijfstakken, de inbreng uitsluitend vergoed wordt hetzij door toekenning van aandelen, hetzij door toekenning van aandelen samen met een storting in contanten die het tiende van de nominale waarde of, bij gebrek aan een nominale waarde, van de fractiewaarde van de toegekende aandelen niet overschrijdt. Indien het Belgisch of buitenlands recht dat de verkrijgende vennootschap beheerst niet in een begrip gelijkaardig aan dat van het kapitaal van een naamloze vennootschap voorziet, wordt met de fractiewaarde gelijkgesteld, de inbrengwaarde, zoals die blijkt uit de jaarrekening, van alle door de aandeelhouders of vennoten toegezegde inbrengen in geld of in natura, met uitzondering van de inbrengen in nijverheid, in voorkomend geval verhoogd met de reserves die op grond van een statutaire bepaling slechts aan de aandeelhouders of vennoten kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen.

De bepaling onder 2° is niet van toepassing op de door artikel 12:8, 2°, van het Wetboek van vennootschappen en verenigingen met splitsing gelijkgestelde rechtshandelingen.

Wordt niet beschouwd als een afdeling van de onderneming het beheer van de participaties en de waarden in portefeuille. De participaties en waarden in portefeuille worden slechts beschouwd als behorende tot een bedrijfstak wanneer zij normaal in de exploitatie van deze tak van de bedrijvigheid zijn geïntegreerd.

Onverminderd het recht tot controle, moet de vervulling van de voorwaarden bevestigd worden, hetzij in de akte van inbreng, hetzij in een onderaan deze akte gestelde verklaring, die vóór de registratie door de partijen of, in hun naam, door de werkende notaris zal ondertekend worden. Bij gebrek aan deze bevestiging zal de akte geregistreerd worden mits betaling van het recht bepaald zonder rekening te houden met de vrijstelling van het evenredig recht of de uitzondering, naar gelang van het geval, behoudens latere teruggave.

§ 3. Het in de artikelen 115 en 115bis bedoelde recht is eveneens niet verschuldigd in geval van inbreng van aandelen of aandelencertificaten, die tot gevolg heeft dat de vennootschap bij wie de inbreng gebeurt, ten minste 75 pct. van het kapitaal of van het eigen vermogen verwerft van de vennootschap waarvan de aandelen of aandelencertificaten zijn ingebracht.

Wanneer dat percentage ten gevolge van verscheidene inbrengen is bereikt, is deze paragraaf alleen toepasselijk op de inbrengen die het bereiken van het percentage mogelijk hebben gemaakt, alsmede op de daaropvolgende inbrengen.

Bovendien vindt deze paragraaf alleen toepassing wanneer voldaan is aan de volgende voorwaarden:

1° de vennootschap die verkrijgt en de vennootschap waarvan de aandelen of deelbewijzen zijn ingebracht, moeten beide hun zetel der werkelijke leiding of hun statutaire zetel hebben op het grondgebied van een lidstaat van de Europese Unie;

2° de inbreng moet uitsluitend door uitgifte van aandelen van de verkrijgende vennootschap vergoed worden, samen met een storting in contanten die het tiende van de nominale waarde of, bij gebrek aan een nominale waarde, van de fractiewaarde van de toegekende aandelen niet overschrijdt. Indien het Belgisch of buitenlands recht dat de verkrijgende vennootschap beheerst niet in een begrip gelijkaardig aan dat van het kapitaal van een naamloze vennootschap voorziet, wordt met de fractiewaarde gelijkgesteld, de inbrengwaarde, zoals die blijkt uit de jaarrekening, van alle door de aandeelhouders of vennoten toegezegde inbrengen in geld of in natura, met uitzondering van de inbrengen in nijverheid, in voorkomend geval verhoogd met de reserves die op grond van een statutaire bepaling slechts aan de aandeelhouders of vennoten kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen;
3° de akte van inbreng moet vermelden dat bij de inbreng ten minste 75 pct. van het kapitaal of van het eigen vermogen van de vennootschap waarvan de aandelen zijn ingebracht, door de verwervende vennootschap wordt verkregen;

4° een attest van een bedrijfsrevisor dat het vermelde feit overeenkomstig het 3° van dit lid bevestigt, moet aan de akte worden aangehecht.

In geval van niet-nakoming van een van de toepassingsvoorwaarden van deze paragraaf uiterlijk wanneer de akte ter formaliteit wordt aangeboden, wordt deze akte tegen het gewoon tarief geregistreerd.

###### Art. 118

(van toepassing vanaf 01.01.1972)

(vervangen bij art. 7 van de wet van 03.07.1972 (B.S., 01.08.1972). Tekst van toepassing vanaf 01.01.1972 (art. 11))

Voor de toepassing van dit Wetboek worden beschouwd als oprichtingen van nieuwe vennootschap:

1° de overbrenging naar België van de zetel der werkelijke leiding van een vennootschap waarvan de statutaire zetel in het buitenland is;

2° de overbrenging naar België van de statutaire zetel van een vennootschap waarvan de zetel der werkelijke leiding in het buitenland is;

3° de overbrenging van het buitenland naar België, van de statutaire zetel en van de zetel der werkelijke leiding van een vennootschap.

In deze gevallen omvat de inbreng de goederen van elke aard die aan de vennootschap toebehoren op het tijdstip van de overbrenging.

###### Art. 119

(van toepassing vanaf 10.04.1994)

(gewijzigd bij art. 46 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

In de gevallen bedoeld in de artikelen 115, 115bis en 118 wordt de belastbare grondslag vastgesteld met inachtneming van de waarde der als vergelding van de inbrengen toegekende maatschappelijke rechten, zonder dat hij nochtans minder mag bedragen dan de verkoopwaarde van de goederen onder aftrek van de lasten die de vennootschap op zich neemt boven de toekenning van de maatschappelijke rechten.

De inbrengen die bestaan uit andere zaken dan geldspecie of goederen in natura worden geraamd bij vergelijking met de inbrengen van geldspecie of goederen in natura, gelet op de onderscheidene aandelen van de inbrengers in de winst.
De verkoopwaarde van het vruchtgebruik of van de blote eigendom van in België gelegen onroerende goederen wordt bepaald overeenkomstig de artikelen 47 tot 50.

###### Art. 120

(van toepassing vanaf 10.04.1994)

(gewijzigd bij art. 47 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2). Tekst van toepassing vanaf 10.04.1994 (art. -))

Wanneer een inbreng in vennootschap gedeeltelijk vergolden wordt anders dan bij toekenning van maatschappelijke rechten, wordt de overeenkomst, naarmate van deze vergelding onderworpen aan de rechten zoals ze in dit hoofdstuk vastgesteld zijn voor de overeenkomsten onder bezwarende titel die goederen van dezelfde aard tot voorwerp hebben.

Zo een inbreng meteen onroerende goederen vermeld in artikel 115bis en goederen van een andere aard begrijpt, worden, niettegenstaande elke strijdig beding, de maatschappelijke rechten en de andere lasten, die de vergeldingen van bedoelde inbreng uitmaken geacht evenredig verdeeld te zijn tussen de waarde die aan de onroerende goederen is toegekend en die welke aan de andere goederen is toegekend bij overeenkomst. De te vervallen huurprijzen van de huurcontracten waarvan de rechten worden ingebracht, worden evenwel geacht enkel op laatstbedoelde rechten betrekking te hebben.

Deze bepalingen zijn evenwel niet toepasselijk bij inbreng van de universaliteit van de goederen of van een bedrijfstak overeenkomstig artikel 117.

###### Art. 121

(van toepassing vanaf 25.11.2025)

(lid 1, 3°, gewijzigd bij art. 26 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art.
28))

Met afwijking van de artikelen 115, 115bis, 118 en 120 worden van het evenredig recht vrijgesteld:

1° de omvorming van een vennootschap met rechtspersoonlijkheid in een vennootschap van een verschillende soort en de omzetting van een vereniging zonder winstoogmerk in een sociale onderneming. Deze bepaling is toepasselijk zelfs wanneer de omvorming plaats heeft bij wege van liquidatie gevolgd door de oprichting van een nieuwe vennootschap, voor zover deze wederoprichting in de akte van in-liquidatie-stellen in het vooruitzicht wordt gesteld en binnen vijftien dagen na de akte plaats heeft;

2° de wijziging van het voorwerp van een vennootschap;

3° de overbrenging van de zetel der werkelijke leiding of van de statutaire zetel van een vennootschap, wanneer deze overbrenging geschiedt uit het grondgebied van een lidstaat van de Europese Unie of wanneer het een overbrenging naar België betreft van de zetel der werkelijke leiding van een vennootschap waarvan de statutaire zetel zich reeds op het grondgebied van de Europese Unie bevindt. Deze bepaling is slechts toepasselijk in de mate waarin het vaststaat dat de vennootschap behoort tot de soort van die welke onderworpen zijn aan een belasting op het bijeenbrengen van kapitaal in het land dat in aanmerking komt voor het voordeel van de vrijstelling.

In alle gevallen wordt het recht geheven op de vermeerdering van het kapitaal van de vennootschap, zonder nieuwe inbreng, of op de inbrengen van nieuwe goederen, die gedaan worden ter gelegenheid van de omvorming, de wijziging van het voorwerp of de overbrenging van de zetel.

###### Art. 122

(van toepassing vanaf 09.03.2026)

(lid 1, 1° en 3°, vervangen, lid 1, 4° en lid 2, gewijzigd bij art. 28 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Onder voorbehoud van de bepalingen van artikel 120, wordt van het evenredig recht vrijgesteld de inbreng gedaan:

1° aan de maatschappijen die erkend zijn door de Société wallonne du logement, de Brusselse Gewestelijke Huisvestingsmaatschappij of Wonen in Vlaanderen;

2° aan maatschappijen die uitsluitend ten doel hebben leningen te doen met het oog op het bouwen, het aankopen of het inrichten van volkswoningen, kleine landeigendommen of daarmede gelijkgestelde woningen, alsmede de uitrusting ervan met geschikt mobilair;

3° aan de besloten vennootschap Vlaams Woning-fonds, de coöperatieve vennootschap Fonds du logement des familles nombreuses de Wallonie en de coöperatieve vennootschap Woningfonds van het Brussels Hoofdstedelijk Gewest;

4° aan de beleggingsvennootschappen bedoeld in artikel 6 van de wet van 3 augustus 2012 betreffende de instellingen voor collectieve belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG en de instellingen voor belegging in schuldvorderingen.

Het evenredig recht, zonder aftrek van het reeds geïnde algemeen vast recht, wordt echter opeisbaar wanneer de in het eerste lid, 4°, bedoelde beleggingsvennootschap de erkenning overeenkomstig de wet van 3 augustus 2012 betreffende de instellingen voor collectieve belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG en de instellingen voor belegging in schuldvorderingen niet verkrijgt of verliest, al naar het geval, zulks vanaf de datum van de beslissing tot weigering of tot intrekking van de erkenning.

###### Art. 1222

(van toepassing vanaf 04.05.1965)

(opgeheven bij art. 14, 1°, van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

###### Art. 123

(van toepassing vanaf 01.05.2019)

(gewijzigd bij art. 93 van de wet van 17.03.2019 (B.S., 10.05.2019). Tekst van toepassing vanaf 01.05.2019 (art. 119, § 1)) (1)

Onder voorbehoud van de bepalingen van de artikelen 44 en 120 wordt van het evenredig recht vrijgesteld, de vermeerdering van het kapitaal of het eigen vermogen, met nieuwe inbreng, door een vennootschap bedoeld in artikel 201, eerste lid, 1°, van het Wetboek van de inkomstenbelastingen 1992, mits aandelen of andere met aandelen gelijk te stellen waardepapieren van die vennootschap ter notering op een Belgische effectenbeurs zijn toegelaten.

Deze vrijstelling is alleen toepasselijk indien in de akte of in een vóór de registratie bij de akte te voegen geschrift wordt bevestigd dat de toepassingsvoorwaarden ervan zijn vervuld.

In geval van onjuistheid van die vermelding verbeurt de vennootschap een boete gelijk aan het ontdoken recht.
Zolang het Wetboek van vennootschappen en verenigingen, overeenkomstig hoofdstuk IV, afdeling II, van de wet van 23 maart 2019, niet van toepassing is op een vennootschap, vereniging of stichting, moet elke verwijzing naar een bepaling van het Wetboek van vennootschappen en verenigingen die voorkomt in een bepaling van het Wetboek van de inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze belastingen, worden gelezen, voor wat deze vennootschap, vereniging of stichting betreft, als een verwijzing naar de bepaling van het Wetboek van vennootschappen of andere bijzondere wetgeving die in zulke fiscale wetgeving voorkwam voor de inwerkingtreding van deze wet (art. 119, § 2); Zolang, overeenkomstig hoofdstuk IV, afdeling II van de wet van 23 maart 2019, een vennootschap, vereniging of stichting, die door het Belgisch recht wordt beheerst, een rechtsvorm heeft die het Wetboek van vennootschappen en verenigingen niet erkent, worden de bepalingen van het Wetboek van de inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze belastingen, die voor de inwerkingtreding van deze wet deze rechtsvorm vermeldden, geacht deze rechtsvorm te blijven vermelden voor wat deze vennootschap, vereniging of stichting betreft, zoals voor de inwerkingtreding van deze wet. (art. 119, § 3).

###### Art. 124

(van toepassing vanaf 01.01.2002)

(hersteld bij art. 31 van de wet van 22.05.2001 (B.S., 09.06.2001). Tekst van toepassing vanaf 01.01.2002 (art. 4, KB van 19.12.2001 (B.S., 29.12.2001 – ed. 2)))

Onder voorbehoud van de voorschriften van de artikelen 44 en 120, worden van het evenredig recht vrijgesteld:

1° de statutaire kapitaalsverhoging, uitgevoerd bij toepassing van een participatieplan bedoeld in artikel 2, 7°, van de wet van 22 mei 2001 betreffende de werknemersparticipatie in het kapitaal en in de winst van de vennootschappen, en ten belope van de kapitaalsparticipaties bedoeld in artikel 2, 17°, van dezelfde wet;
2° de inbreng in een coöperatieve participatievennootschap uitgevoerd volgens artikel 12, § 2, van dezelfde wet.

Deze vrijstelling is slechts toepasbaar voor zover er vermeld is in de akte of in een vóór de registratie bij de akte gevoegd geschrift dat de toepassingsvoorwaarden zijn vervuld.

Ingeval deze vermelding ontbreekt of onjuist is, loopt de vennootschap een boete op gelijk aan het ontdoken recht.

###### Art. 125

(van toepassing vanaf 04.05.1965)

(opgeheven bij art. 14, 3°, van de wet van 14.04.1965 (B.S.,24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

###### Art. 126

(van toepassing vanaf 04.05.1965)

(opgeheven bij art. 14, 4°, van de wet van 14.04.1965 (B.S.,24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

###### Art. 127

(van toepassing vanaf 04.05.1965)

(opgeheven bij art. 14, 5°, van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

(...)

###### Art. 128

(van toepassing vanaf 04.05.1965)

(gewijzigd bij art. 15 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

Met afwijking van artikel 2, mogen de onderhandse akten welke de in artikelen 115 tot 122 bedoelde overeenkomsten tot voorwerp hebben, op de originelen of op afschriften of uittreksels worden geregistreerd.
Wanneer de afschriften of uittreksels ter registratie worden aangeboden, moeten ze vergezeld zijn van de oorspronkelijke akte.

###### Art. 211

wordt toepasselijk gemaakt op de onderhandse of buitenslands verleden akten die de zelfde overeenkomsten tot voorwerp hebben, al hadden deze geen betrekking op in België gelegen onroerende goederen.

###### Art. 129

(van toepassing vanaf 01.05.2019 en vanaf 12.07.2023 (voor wat betreft de coöperatieve vennootschap))

(lid 1, gewijzigd bij art. 2 van de ordonnantie van 01.06.2023 (B.S., 12.07.2023). Tekst van toepassing vanaf 01.05.2019 (art.
15, lid 1) en vanaf 12.07.2023 voor wat betreft de coöperatieve vennootschap (art. 15, lid 2)) (1)

Het verkrijgen, anderszins dan bij inbreng in vennootschap, door één of meer vennoten, van in België gelegen onroerende goederen, voortkomende van een vennootschap onder firma, een commanditaire vennootschap, een besloten vennootschap of een coöperatieve vennootschap, geeft, welke ook de wijze zij waarop het geschiedt, aanleiding tot het heffen van het voor verkopingen gesteld recht.

In geval van afgifte van de maatschappelijke goederen door de vereffenaar van de in vereffening gestelde vennootschap aan al de vennoten, is voorgaand lid van toepassing op de latere toebedeling van de goederen aan één of meer vennoten.

Lid 1 is niet toepasselijk zo het gaat om:

1° onroerende goederen welke in de vennootschappen werden ingebracht, wanneer ze verkregen worden door de persoon, die de inbreng gedaan heeft;

2° onroerende goederen welke door de vennootschap met betaling van het voor de verkopingen bepaald registratierecht verkregen werden, wanneer het vaststaat dat de vennoot die eigenaar van die onroerende goederen wordt deel uitmaakte van de vennootschap toen laatstgenoemde de goederen verkreeg.
In afwijking van art. 15, 1ste lid, voor de vennootschappen, met uitzondering van de landbouwvennootschappen, waarvan de oprichting voorafgaat aan de inwerkingtreding van het Wetboek van vennootschappen en verenigingen overeenkomstig art. 38, 1ste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, hebben art. 2 en 3 uitwerking met ingang van 01.01.2020. Voor de landbouwvennootschappen waarvan de oprichting voorafgaat aan de inwerkingtreding van het Wetboek van vennootschappen en verenigingen overeenkomstig art. 38, 1ste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen heeft artikel 2 uitwerking met ingang van 01.01.2024 (art. 16, lid 1).
In afwijking van het eerste lid, wanneer de vennootschap, met uitzondering van de landbouwvennootschap, opgericht vóór 01.05.2019, heeft besloten, overeenkomstig art. 39, § 1, 2de lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, om de bepalingen van voornoemd Wetboek toe te passen vóór 01.01.2020, zijn art. 2 en 3 van toepassing voor de verkrijgingen vastgesteld door authentieke akte vanaf de dag van publicatie van de wijziging van de statuten die deze beslissing bekrachtigt. Wanneer de vennootschap een landbouwvennootschap is opgericht vóór 01.05.2019 die zich vóór 01.01.2024 heeft omgezet overeenkomstig art. 41, § 4, 1ste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen is artikel 2 van toepassing voor de verkrijgingen vastgesteld door authentieke akte vanaf de dag van publicatie van de authentieke akte van omzetting (art. 16, lid 2).

###### Art. 130

(van toepassing vanaf 01.05.2019 en 12.07.2023 (voor wat betreft de coöperatieve vennootschap)) (gewijzigd bij art. 3 van de ordonnantie van 01.06.2023 (B.S., 12.07.2023). Tekst van toepassing vanaf 01.05.2019 (art. 15, lid 1) en vanaf 12.07.2023 voor wat betreft de coöperatieve vennootschap (art. 15, lid 2)) (1)

Het verkrijgen anderszins dan bij inbreng in vennootschap door één of meer vennoten van in België gelegen onroerende goederen, voortkomende van een naamloze vennootschap, van een Europese vennootschap of van een Europese coöperatieve vennootschap, geeft, welke ook de wijze zij waarop het geschiedt, aanleiding tot het heffen van het voor verkopingen gesteld recht.
In afwijking van art. 15, 1ste lid, voor de vennootschappen, met uitzondering van de landbouwvennootschappen, waarvan de oprichting voorafgaat aan de inwerkingtreding van het Wetboek van vennootschappen en verenigingen overeenkomstig art. 38, 1ste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, hebben art. 2 en 3 uitwerking met ingang van 01.01.2020. Voor de landbouwvennootschappen waarvan de oprichting voorafgaat aan de inwerkingtreding van het Wetboek van vennootschappen en verenigingen overeenkomstig art. 38, 1ste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen heeft art. 2 uitwerking met ingang van 01.01.2024 (art. 16, lid 1).
In afwijking van het eerste lid, wanneer de vennootschap, met uitzondering van de landbouwvennootschap, opgericht vóór 01.05.2019, heeft besloten, overeenkomstig art. 39, § 1, 2de lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, om de bepalingen van voornoemd Wetboek toe te passen vóór 01.01.2020, zijn art. 2 en 3 van toepassing voor de verkrijgingen vastgesteld door authentieke akte vanaf de dag van publicatie van de wijziging van de statuten die deze beslissing bekrachtigt. Wanneer de vennootschap een landbouwvennootschap is opgericht vóór 01.05.2019 die zich vóór 01.01.2024 heeft omgezet overeenkomstig artikel 41, § 4, eerste lid, van de wet van 23.03.2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen is art. 2 van toepassing voor de verkrijgingen vastgesteld door authentieke akte vanaf de dag van publicatie van de authentieke akte van omzetting (art. 16, lid 2).

#### Afdeling XII - Schenkingen

##### Onderafdeling I - Algemene bepalingen

###### Art. 131

(van toepassing vanaf 01.01.2024)

(gewijzigd bij art. 14 van de ordonnantie van 06.07.2023 (B.S., 27.09.2023). Tekst van toepassing vanaf 01.01.2024 en op de schenkingen die worden afgesloten vanaf deze datum (art. 19))

§ 1. Voor de schenkingen van onroerende goederen wordt over het bruto-aandeel van elk der begiftigden een evenredig recht geheven volgens het in de onderstaande tabellen vermelde tarief.

Hierin wordt onder « a » vermeld het percentage dat toepasselijk is op het overeenstemmende gedeelte.
Voor de toepassing van deze afdeling, wordt onder "`partner' verstaan:

a) de persoon die, op de dag van de schenking, met de schenker gehuwd is;

b) de persoon die zich, op de dag van de schenking, in de toestand van wettelijke samenwoning met de schenker bevindt in de zin van titel Vbis van boek III van het oud Burgerlijk Wetboek;

c) de persoon die, op de dag van de schenking, op ononderbroken wijze samenwoont met de schenker en met hem een gemeenschappelijke huishouding voert ten minste één jaar of, voor de toepassing van de artikelen 140/1 tot en met 140/3, drie jaar.

Voor de toepassing van het derde lid, c), houdt de inschrijving in het bevolkingsregister of in het vreemdelingenregister op hetzelfde adres van de schenker een weerlegbaar vermoeden in van het samenwonen en van het vormen van een gemeenschappelijke huishouding met de schenker. Deze voorwaarden worden geacht ook vervuld te zijn als het samenwonen en het vormen van een gemeenschappelijke huishouding met de schenker, aansluitend op de in het derde lid, c), bedoelde periode tot op de dag van de schenking onmogelijk is geworden, ingevolge overmacht.

Tabel I
Tarief in rechte lijn en tussen partners

Gedeelte van de schenking                   a van                        tot inbegrepen 0,01 EUR                           150.000 EUR       3% 150.000,01 EUR                     250.000 EUR       9% 250.000,01 EUR                     450.000 EUR      18% Boven de 450.000 EUR                                27%

Tabel II
Tarief tussen alle andere personen

Gedeelte van de schenking                   a van                        tot inbegrepen 0,01 EUR                           150.000 EUR      10% 150.000,01 EUR                     250.000 EUR      20% 250.000,01 EUR                     450.000 EUR      30% Boven de 450.000 EUR                                40%

§ 2. Voor de schenkingen van roerende goederen wordt over het bruto-aandeel van elk der begiftigden een recht geheven van:

1° 3% voor schenkingen in de rechte lijn en tussen partners;

2° 7% voor schenkingen aan andere personen.
Dit tarief is evenwel niet van toepassing op de schenkingen van roerende goederen gedaan onder een opschortende voorwaarde die vervuld wordt ingevolge het overlijden van de schenker, en die krachtens artikel 4,
3°, van het Wetboek van successierechten als legaten worden beschouwd voor de heffing van het recht van successie.

###### Art. 131bis

(van toepassing vanaf 01.07.2022)

(gewijzigd bij art. 22 van de ordonnantie van 13.10.2022 (B.S., 19.10.2022). Tekst van toepassing vanaf 01.07.2022 (art. 24))

In afwijking van artikel 131, § 2, wordt van het schenkingsrecht vrijgesteld de waarde van de schenkingen van roerende goederen die worden vermeld in een erfovereenkomst bedoeld in artikelen 4.242 tot 4.259 van het Burgerlijk Wetboek of in de overeenkomst bedoeld in artikel 4.84 van hetzelfde Wetboek.

De vrijstelling is alleen van toepassing als de partijen, in de akte of onderaan op de akte, verklaren dat de schenking heeft plaatsgevonden vóór de datum waarop de erfovereenkomst of de overeenkomst werd gesloten.

De vrijstelling is niet van toepassing indien de partijen uitdrukkelijk verklaren dat de vermelding van de eerdere schenking de bedoeling heeft om aan de begiftigde een titel van schenking te verschaffen.

###### Art. 1321

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 156 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 1322

(van toepassing vanaf 01.01.2024)

(1° en 3°, gewijzigd bij art. 15 van de ordonnantie van 06.07.2023 (B.S., 27.09.2023). Tekst van toepassing vanaf 01.01.2024 en op de schenkingen die worden afgesloten vanaf deze datum (art. 19))

Voor de toepassing van deze afdeling wordt er geen rekening gehouden met de verwantschapsband voortspruitende uit de gewone adoptie.

Evenwel wordt, mits bewijs te verstrekken door de belanghebbende, met deze adoptieve afstamming rekening gehouden:

1° wanneer het adoptief kind een kind is van de partner van de adoptant;
2° wanneer, op het ogenblik van de adoptie, het adoptief kind onder de voogdij was van de openbare onderstand of van een openbaar centrum voor maatschappelijk welzijn, of wees van een voor België gestorven vader of moeder;

3° wanneer het adoptief kind, vóór de leeftijd van eenentwintig jaar, gedurende één ononderbroken jaar van de adoptant of van de adoptant en diens partner samen de hulp en verzorging heeft gekregen die kinderen normaal van hun ouders krijgen;

4° wanneer de adoptie gedaan werd door een persoon van wie al de afstammelingen voor België gestorven zijn.

###### Art. 133

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 17 van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 2))

Het recht wordt vereffend op de verkoopwaarde van de geschonken goederen, zonder aftrek van lasten.

Evenwel, voor de schenking van financiële instrumenten die toegelaten zijn tot verhandeling op Belgische of buitenlandse gereglementeerde markten als vermeld in artikel 2, eerste lid, 5° en 6° van de wet van 2 augustus 2002 betreffende het toezicht op de financiële sector en de financiële diensten en voor Belgische of buitenlandse multilaterale handelsfaciliteiten als vermeld in artikel 2, eerste lid, 4° van de voormelde wet, wordt de belastbare grondslag bepaald volgens de beurswaarden ervan op datum van de laatste dag van de maand die voorafgaat aan de maand waarin de schenking plaatsvindt. Onder beurswaarde wordt verstaan, de slotkoers zoals vastgesteld op basis van de koersinformatie gepubliceerd door de betrokken beurs of, bij gebrek hieraan, door de gespecialiseerde media. Als er op die datum geen notering is, geldt de beurswaarde op de eerstvolgende dag waarop er opnieuw een notering wordt vastgesteld. Als er op de datum van de laatste dag van de maand die voorafgaat aan de maand waarin de schenking plaatsvindt voor bepaalde van de geschonken waarden wel en voor andere geen notering is, wordt de belastbare grondslag van die laatste waarden vastgesteld volgens de beurswaarden op de eerstvolgende dag waarop er wel een notering is.

Voor de schenking van het vruchtgebruik of de blote eigendom van een onroerend goed wordt de belastinggrondslag vastgesteld zoals in de artikelen 47 tot 50 is bepaald.

Voor de schenkingen van het op het leven van de schenker, een begiftigde of een derde gevestigde vruchtgebruik van roerende goederen geldt als heffingsgrondslag het bedrag verkregen door de vermenigvuldiging van de jaarlijkse opbrengst van de goederen, forfaitair vastgesteld op 4% van de volle eigendom van de goederen, met het getal dat in artikel 47, eerste lid, wordt aangegeven tegenover de leeftijdsklasse waartoe diegene op wiens leven het vruchtgebruik gevestigd is, behoort op de datum van de schenking.

Voor de schenkingen van het voor een bepaalde tijd gevestigde vruchtgebruik van roerende goederen geldt als heffingsgrondslag het bedrag verkregen door kapitalisatie van de jaarlijkse opbrengst tegen 4% over de duur van het vruchtgebruik bepaald in de schenkingsakte. De jaarlijkse opbrengst van de roerende goederen wordt forfaitair vastgesteld op 4% van de volle eigendom van die goederen. Het aldus verkregen bedrag van de heffingsgrondslag mag evenwel niet gaan boven de waarde berekend volgens het vierde lid indien het vruchtgebruik gevestigd is ten bate van een natuurlijk persoon.

Voor de schenkingen van de blote eigendom van roerende goederen waarvan het vruchtgebruik door de schenker is voorbehouden, is de heffingsgrondslag de verkoopwaarde van de volle eigendom van de goederen.

Voor de schenkingen van de blote eigendom van roerende goederen waarvan het vruchtgebruik door de schenker niet is voorbehouden, is de heffingsgrondslag de verkoopwaarde van de volle eigendom van de goederen, verminderd met de waarde van het vruchtgebruik, berekend volgens het vierde of vijfde lid.

Voor schenkingen van een lijfrente of een levenslang pensioen wordt het recht berekend over het jaarlijkse bedrag van de uitkering, vermenigvuldigd met de leeftijdscoëfficiënt die volgens de tabel in artikel 47 op de begiftigde moet worden toegepast.

Voor schenkingen van een altijddurende rente wordt het recht berekend over het jaarlijkse bedrag van de rente vermenigvuldigd met twintig.

###### Art. 134

(van toepassing vanaf 09.03.2005)

(gewijzigd bij art. 4 van de ordonnantie van 24.02.2005 (B.S., 09.03.2005) err. (B.S., 15.03.2005). Tekst van toepassing vanaf 09.03.2005 (art. 9))

Voor de toepassing van artikelen 131 tot 133, wordt de last, bestaande uit een som, een rente of een pensioen onder kosteloze titel bedongen ten bate van een derde die aanneemt, in hoofde van dezen derde als schenking belast en van het aandeel van den hoofdbegiftigde afgetrokken.

In de mate dat de schenking betrekking heeft op onroerende goederen, wordt de last in hoofde van de derde als schenking belast volgens de in artikel 131, § 1, geldende tarieven.

###### Art. 135

(van toepassing vanaf 01.01.2024)

(lid 2, gewijzigd bij art. 16 van de ordonnantie van 06.07.2023 (B.S., 27.09.2023). Tekst van toepassing vanaf 01.01.2024 en op de schenkingen die worden afgesloten vanaf deze datum (art. 19))

Het bedrag van het bij artikel 131, § 1, vastgestelde recht vereffend ten laste van de begiftigde, die op het tijdstip waarop het recht aan de Staat verworven is minstens drie kinderen in leven heeft die de leeftijd van eenentwintig jaar niet hadden bereikt, wordt verminderd met 2 t.h. voor elk van deze kinderen, zonder dat de vermindering 62 EUR per kind mag overschrijden.

Deze vermindering wordt ten gunste van de begiftigde partner gebracht op 4 t.h. per kind dat de leeftijd van eenentwintig jaar niet had bereikt kind, zonder dat de vermindering 124 EUR per kind mag overschrijden.
Voor de toepassing van dit artikel wordt het ontvangen kind voor zover het levensvatbaar geboren wordt, gelijkgesteld met het geboren kind.

###### Art. 136

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 159 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Het voordeel van de in vorig artikel voorziene verminderingen wordt afhankelijk gesteld van de vermelding in de akte van schenking van naam, voornamen, woonplaats, plaats en datum van geboorte van de kinderen van de begiftigde beoogd bij artikel 135.

Deze vermelding mag gedaan worden onderaan op de akte in een verklaring vóór de registratie ondertekend en echt bevestigd door de begiftigde of, in zijn naam, door de werkende notaris.

Ingeval een kind, ontvangen vóór de eischbaarheid van de belasting, geboren wordt na de registratie, wordt hetgeen te veel werd geheven terugbetaald op aanvraag van den betrokkene, te doen binnen twee jaar vanaf de geboorte van het kind.

De begiftigde die in verband met het aantal van zijn wettige (1) afstammelingen een onjuiste verklaring heeft afgelegd, verbeurt een boete gelijk aan het ontdoken recht.
(1) Bij vergetelheid werd het woord “wettige” niet geschrapt.

###### Art. 137

(van toepassing vanaf 09.03.2005)

(gewijzigd bij art. 6 van de ordonnantie van 24.02.2005 (B.S., 09.03.2005) err. (B.S., 15.03.2005). Tekst van toepassing vanaf 09.03.2005 (art. 9))

Ter bepaling van het op een schenking van onroerende goederen toepasselijk tarief, wordt de desbetreffende belastbare grondslag gevoegd bij de som die heeft gediend tot grondslag van heffing op de schenkingen van onroerende goederen welke reeds tussen dezelfde partijen zijn voorgekomen en vastgesteld werden door akten die dagtekenen van minder dan drie jaar vóór de datum der nieuwe schenking en vóór laatstbedoelde datum geregistreerd werden of verplicht registreerbaar geworden zijn.

###### Art. 1381

(van toepassing vanaf 09.03.2005)

(gewijzigd bij art. 7 van de ordonnantie van 24.02.2005 (B.S., 09.03.2005) err. (B.S., 15.03.2005). Tekst van toepassing vanaf 09.03.2005 (art. 9)) Ongeacht of zij verplicht registreerbaar zijn dan wel vrijwillig tot de formaliteit worden aangeboden, moeten de akten van schenking van onroerende goederen vermelding houden of er reeds tussen dezelfde partijen één of meer schenkingen van onroerende goederen zijn voorgekomen welke vastgesteld werden door akten die dagtekenen van minder dan drie jaar vóór den datum der nieuwe schenking en vóór dezelfde datum geregistreerd werden of verplicht registreerbaar geworden zijn.

Zo ja, moeten zij den datum dier akten vermelden, zomede de grondslag waarop de belasting werd of dient geheven.

De in dit artikel voorziene opgaven en vermeldingen mogen gedaan worden onderaan de akte in een verklaring vóór de registratie ondertekend en echt bevestigd door de begiftigde of, in zijn naam, door de werkende notaris.

Indien bewuste opgaven en vermeldingen ontbreken of indien zij onjuist of onvolledig zijn, verbeuren de partijen ondeelbaar een geldboete ten bedrage van het ontdoken recht, zonder dat ze lager dan 25 EUR mag zijn.

###### Art. 1382

(van toepassing vanaf 27.09.1947)

(ingevoegd bij art. 7 van de wet van 14.08.1947 (B.S., 17.09.1947). Tekst van toepassing vanaf 27.09.1947 (art. -))

Voor de toepassing van artikelen 137 en 1381 op de aan een schorsende voorwaarde onderworpen schenkingen, wordt de datum van de vervulling der voorwaarden in de plaats gesteld van de datum van de akte.

###### Art. 139

(van toepassing vanaf 01.02.1940)

Bij onjuist opgeven van den graad van verwantschap tussen schenker en begiftigde, is door deze laatsten, benevens het ontdoken recht, ondeelbaar een boete verschuldigd gelijk aan het bedrag van dat recht.

###### Art. 140

(van toepassing vanaf 12.02.2012)

(gewijzigd bij art. 3 van de ordonnantie van 16.12.2011 (B.S., 02.02.2012). Tekst van toepassing vanaf 12.02.2012 (art. -))

De bij artikel 131 vastgestelde rechten worden beperkt tot:

1° 6,60 t.h. voor schenkingen aan gemeenten gelegen in het Brussels Hoofdstedelijk Gewest en hun openbare instellingen, aan de door de Brusselse Gewestelijke Huisvestingsmaatschappij erkende maatschappijen, aan de coöperatieve vennootschap met beperkte aansprakelijkheid Woningfonds van het Brussels Hoofdstedelijk Gewest, aan de intercommunales van het Brussels Hoofdstedelijk Gewest en aan stichtingen van openbaar nut;
2° 7% voor de schenkingen, inclusief inbrengen om niet, van onroerende goederen aan verenigingen zonder winstoogmerk, aan ziekenfondsen en landsbonden van ziekenfondsen, aan beroepsverenigingen, aan internationale verenigingen zonder winstoogmerk en aan private stichtingen;

3° 100 EUR voor schenkingen, inclusief inbrengen om niet, gedaan aan stichtingen van openbaar nut of aan rechtspersonen bedoeld in 2°, zo de schenker zelf een dezer stichtingen of rechtspersonen is;

4° 1,10% voor de schenkingen met inbegrip van de inbrengen om niet, gedaan door de gemeenten aan de pensioenfondsen die zij onder de vorm van een vereniging zonder winstoogmerk hebben opgericht in uit voering van een door de voogdijoverheid goedgekeurd saneringsplan.

De verlagingen vermeld sub 1°, 2° en 3°, zijn ook toepasselijk op gelijkaardige rechtspersonen die opgericht zijn volgens en onderworpen zijn aan de wetgeving van een lidstaat van de Europese Economische Ruimte, en die bovendien hun statutaire zetel, hun hoofdbestuur of hun hoofdvestiging binnen de Europese Economische Ruimte hebben.

##### Onderafdeling II - Bijzondere bepalingen voor schenkingen van ondernemingen

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

###### Art. 140bis

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140ter

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140quater

(van toepassing vanaf 01.01.2017)
(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140quinquies

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140sexies

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140septies

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

###### Art. 140octies

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

##### Onderafdeling II van de afdeling XII van het hoofdstuk IV van de titel I van het Wetboek der Registratie-, Hypotheek-, en Griffierechten, met als opschrift « Bijzondere bepalingen voor schenkingen van ondernemingen » en bevattende de artikelen 140bis tot 140octies, wordt vervangen bij een onderafdeling II met hetzelfde opschrift, bevattende de artikelen 140/1 tot 140/6

##### Onderafdeling II - Bijzondere bepalingen voor schenkingen van ondernemingen

###### Art. 140/1

(van toepassing vanaf 01.01.2024)

(§ 2, 5°, opgeheven bij art. 17 van de ordonnantie van 06.07.2023 (B.S., 27.09.2023). Tekst van toepassing vanaf 01.01.2024 en op de schenkingen die worden afgesloten vanaf deze datum (art. 19))

§ 1. In afwijking van artikel 131, wordt van het schenkingsrecht vrijgesteld:

1° de schenking van de volle eigendom, de blote eigendom, het vruchtgebruik van de activa die door de schenker of zijn partner beroepsmatig zijn geïnvesteerd in een familiale onderneming. De vrijstelling is niet van toepassing op de verkrijging van onroerende goederen die hoofdzakelijk tot bewoning worden aangewend of zijn bestemd;

2° de schenking van de volle eigendom, de blote eigendom of het vruchtgebruik van aandelen van een familiale vennootschap met zetel van werkelijke leiding in een van de Staten van de Europese Economische Ruimte, op voorwaarde dat de aandelen van de vennootschap die, op het ogenblik van de schenking, in volle eigendom toebehoren aan de schenker en zijn familie ten minste 50% van de stemrechten in die vennootschap vertegenwoordigen.

In afwijking van het eerste lid, 2°, moeten de aandelen van de vennootschap, die op het ogenblik van de schenking in volle eigendom toebehoren aan de schenker en zijn familie, minstens 30% van de stemrechten in die vennootschap vertegenwoordigen, als hij en zijn familie aan één van de volgende voorwaarden voldoen:

1° hetzij samen met één andere aandeelhouder en zijn familie volle eigenaar zijn van de aandelen van de vennootschap die minstens 70% van de stemrechten in die vennootschap vertegenwoordigen;

2° hetzij samen met twee andere aandeelhouders en hun familie volle eigenaar zijn van de aandelen van de vennootschap die minstens 90% van de stemrechten in die vennootschap vertegenwoordigen.

Voor de toepassing van het tweede lid komen de aandelen die toebehoren aan rechtspersonen, niet in aanmerking om te worden samengeteld met de aandelen die toebehoren aan de schenker.

§ 2. Voor de toepassing van dit artikel, artikel 140/2 en artikel 140/3, wordt verstaan onder:

1° familiale onderneming: een nijverheids-, handels-, ambachts- of landbouwbedrijf of een vrij beroep dat door de schenker of zijn partner, al dan niet samen met anderen, persoonlijk wordt geëxploiteerd of uitgeoefend;

2° familiale vennootschap: een vennootschap die de uitoefening van een nijverheids-, handels-, ambachts- of landbouwactiviteit, of van een vrij beroep tot voorwerp heeft en deze activiteit of beroep uitoefent.
Als de vennootschap aan het voorgaande niet beantwoordt, maar aandelen van minstens één directe dochtervennootschap houdt die aan die voorwaarden beantwoordt en die haar zetel van werkelijke leiding heeft in één van de Staten van de Europese Economische Ruimte, en dat deze aandelen minstens 30% van de stemrechten in die dochtervennootschap vertegenwoordigen, wordt ze ook beschouwd als een familiale vennootschap.

Vennootschappen die geen reële economische activiteit hebben, worden uitgesloten van de vrijstelling, vermeld in paragraaf 1. Een vennootschap wordt geacht geen reële economische activiteit te hebben als blijkt uit de balansposten van ofwel de goedkeurde jaarrekening in geval van een vennootschap als vermeld in paragraaf 2, 2 °, eerste lid, ofwel de goedgekeurde geconsolideerde jaarrekening in geval van een vennootschap als vermeld in paragraaf 2, 2°, tweede lid, van minstens één van de drie boekjaren voorafgaand aan de datum van de schenking:

a. dat de bezoldigingen, sociale lasten en pensioenen een percentage gelijk of lager dan 1,50% uitmaken van de totale activa; en

b. dat de terreinen en gebouwen meer dan 50% uitmaken van het totale actief. De begiftigde kan het tegenbewijs daarvan leveren.

Voor de toepassing van de hiervoor vermelde omschrijving moet worden begrepen onder:

a. bezoldigingen, sociale lasten en pensioenen: de waarde, opgenomen onder de gelijknamige post van de resultatenrekening van de jaarrekening of onder een soortgelijke post van de geconsolideerde jaarrekening. Als een vennootschap geen jaarrekening volgens het standaardmodel naar Belgisch recht hoeft neer te leggen, wordt onder « waarde » verstaan die welke opgenomen is onder de post waaruit alle kosten blijken die naar hun aard als kosten kunnen worden beschouwd voor de tewerkstelling van personeel in dienstverband;

b. terreinen en gebouwen: de waarde, opgenomen onder de gelijknamige post van de resultatenrekening van de jaarrekening of onder een soortgelijke post van de geconsolideerde jaarrekening. Als een vennootschap geen jaarrekening volgens het standaardmodel naar Belgisch recht hoeft neer te leggen, wordt een soortgelijke post bedoeld die opgenomen is onder de post materiële vaste activa;

c. totaal actief: de waarde, opgenomen onder de balanspost totaal van de activa van de jaarrekening of onder een soortgelijke post van de jaarrekening of van de geconsolideerde jaarrekening;

3° aandelen:

a. elk aandeel met stemrecht dat, wanneer de familiale vennootschap een naamloze vennootschap, een Europese vennootschap of een Europese coöperatieve vennootschap is, dan wel een vennootschap met een andere rechtsvorm waarvoor het Belgische of buitenlandse recht dat haar beheerst voorziet in een gelijkaardig begrip met het begrip kapitaal, een deel van het kapitaal vertegenwoordigt;

b. de certificaten van aandelen, uitgereikt door rechtspersonen met een zetel in één van de Staten van de Europese Economische Ruimte, ter vertegenwoordiging van aandelen van familiale vennootschappen die aan de gestelde voorwaarden voldoen en waarvan de rechtspersoon de verplichting heeft om de dividenden en andere meerwaarden onmiddellijk en uiterlijk binnen één maand door te storten aan de certificaathouder;

4° familie van de schenker of de aandeelhouder als vermeld in paragraaf 1, eerste lid, 2°: a. de partner van de schenker of aandeelhouder, waarbij het begrip partner voor de aandeelhouder op een gelijkaardige wijze moet worden geïnterpreteerd als dat het geval is voor de schenker;

b. de verwanten in rechte lijn van de schenker of aandeelhouder, alsook hun partner, waarbij het begrip partner op een gelijkaardige wijze moet worden geïnterpreteerd als dat het geval is voor de schenker;

c. de zijverwanten van de schenker of aandeelhouder tot en met de tweede graad en hun partners, waarbij het begrip partner op een gelijkaardige wijze moet worden geïnterpreteerd als dat het geval is voor de schenker;

d. de kinderen van broers en zussen van de schenker of aandeelhouder.

5° (…).

§ 3. Als een vennootschap met toepassing van paragraaf 2, 2°, tweede lid, als een familiale vennootschap wordt beschouwd, wordt de toepassing van de vrijstelling beperkt tot de waarden van de aandelen van de vennootschap in de dochtervennootschapen die de uitoefening van een nijverheids-, handels-, ambachts- of landbouwactiviteit, of van een vrij beroep tot voorwerp hebben en die hun zetel van werkelijke leiding in één van de Staten van de Europese Economische Ruimte hebben.

§ 4. Voor de toepassing van de artikelen 140/1 tot 140/6, wordt de inbreng van activa in de familiale vennootschap en de beroepsmatige aanwending van activa in de familiale onderneming in het jaar dat de schenking voorafgaat, vermoed een niet aan de administratie tegenstelbare rechtshandeling te zijn, zoals bedoeld in artikel 18, paragraaf 2.

###### Art. 140/2

(van toepassing vanaf 01.05.2019 (art. 5, § 1, 2°) en 22.07.2023 (art. 5, § 1, 1° in de Franse tekst))

(§ 2, 1°, gewijzigd in de Franse versie bij art. 5, § 1, 1° en § 2, 3°, vervangen bij art. 5, § 1, 2° van de ordonnantie van 01.06.2023 (B.S., 12.07.2023). Tekst van toepassing vanaf 01.05.2019 (art. 15, lid 1), met uitzondering van art. 5, § 1, 1°, van toepassing vanaf 22.07.2023 (art. -)) (1)

§ 1. De vrijstelling, vermeld in artikel 140/1, § 1, eerste lid, 1°, wordt alleen behouden als de volgende voorwaarden cumulatief zijn vervuld:

1° de activiteit van de familiale onderneming wordt zonder onderbreking voortgezet gedurende drie jaar vanaf de datum van de authentieke akte van schenking;

2° de onroerende goederen die met toepassing van de vrijstelling zijn overgedragen, worden niet hoofdzakelijk tot bewoning aangewend of bestemd gedurende een periode van drie jaar van de datum van de authentieke akte van schenking.

§ 2. De vrijstelling, vermeld in artikel 140/1, § 1, eerste lid, 2°, wordt alleen behouden als de volgende voorwaarden cumulatief zijn vervuld:
1° de familiale vennootschap blijft gedurende drie jaar vanaf de datum van de authentieke akte van schenking voldoen aan de voorwaarden, vermeld in artikel 140/1, § 2, 2°;

2° de activiteit van de familiale vennootschap wordt zonder onderbreking voortgezet gedurende drie jaar vanaf de datum van de authentieke akte van schenking en voor elk van de drie jaar wordt een jaarrekening of geconsolideerde jaarrekening opgemaakt en in voorkomend geval gepubliceerd overeenkomstig de vigerende boekhoudwetgeving van de lidstaat waar de maatschappelijke zetel gevestigd is op het ogenblik van schenking, die ook aangewend is ter verantwoording van de aangifte in de inkomstenbelasting.

Ondernemingen of vennootschappen waarvan de maatschappelijke zetel buiten het Brussels Hoofdstedelijk Gewest, maar binnen België ligt, moeten een jaarrekening of geconsolideerd jaarrekening opmaken en in voorkomend geval publiceren overeenkomstig de vigerende boekhoudwetgeving in België op de datum van de authentieke akte van schenking;

3° naargelang het geval:

a. wanneer de familiale vennootschap een naamloze vennootschap, een Europese vennootschap of een Europese coöperatieve vennootschap is, dan wel een vennootschap met een andere rechtsvorm waarvoor het Belgische of buitenlandse recht dat haar beheerst voorziet in een gelijkaardig begrip: het kapitaal daalt niet gedurende drie jaar vanaf de datum van de authentieke akte van schenking door uitkeringen of terugbetalingen;

b. wanneer de familiale vennootschap een rechtsvorm heeft waarvoor het Belgische of buitenlandse recht dat de vennootschap beheerst niet voorziet in het begrip kapitaal of een gelijkaardig begrip: het eigen vermogen daalt niet gedurende drie jaar vanaf de datum van de authentieke akte van schenking door uitkeringen of terugbetalingen tot onder het bedrag van de tot op de datum van de authentieke akte van schenking verrichte inbrengen, zoals blijkt uit de jaarrekeningen.

4° de zetel van de werkelijke leiding van de vennootschap wordt niet overgebracht naar een Staat die geen deel uitmaakt van de Europese Economische Ruimte gedurende drie jaar vanaf de datum van de authentieke akte van schenking.
Artikelen 2, 3, 4, 1° tot en met 3°, 5, § 1, 2°, 7, 1°, b) en c), 2° en 3°, 8 en 11 tot en met 13 hebben uitwerking met ingang van 01.05.2019 (art. 15, lid 1).
In afwijking van artikel 15, eerste lid, voor de vennootschappen waarvan de oprichting voorafgaat aan de inwerkingtreding van het Wetboek van vennootschappen en verenigingen overeenkomstig artikel 38, eerste lid, van de wet van 23 maart 2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, hebben de artikelen 4,
1° en 2°, a), ii) en b), 5, § 1, 2°, 7, 1°, b) en c), 2°, a), ii), en b), en 8 uitwerking met ingang van 01.01.2020 (art. 17, lid 1).
In afwijking van het eerste lid, wanneer de vennootschap, opgericht vóór 01.05.2019, heeft besloten, overeenkomstig artikel 39, § 1, tweede lid, van de wet van 23 maart 2019 tot invoering van het Wetboek van vennootschappen en verenigingen en houdende diverse bepalingen, om de bepalingen van voornoemd Wetboek toe te passen vóór 01.01.2020, is artikel 4, 1° en
2°, a), ii) en b), van toepassing op de schenkingen vastgesteld door authentieke akte vanaf de dag van publicatie van de wijziging van de statuten die deze beslissing bekrachtigt. Artikel 5, § 1, 2°, is van toepassing vanaf de dag van publicatie van de wijziging van de statuten die deze beslissing bekrachtigt (art. 17, lid 2).

###### Art. 140/3

(van toepassing vanaf 22.07.2023)

(lid 1, 2°, b., 2., gewijzigd bij art. 5, § 2 van de ordonnantie van 01.06.2023 (B.S., 12.07.2023). Tekst van toepassing vanaf 22.07.2023 (art. -))

De vrijstelling vermeld in artikel 140/1 is alleen van toepassing als de volgende voorwaarden cumulatief zijn vervuld:

1° de schenking van de activa of aandelen van de familiale onderneming of vennootschap wordt vastgesteld bij authentieke akte;

2° de onderstaande formaliteiten zijn nageleefd:

a. de partijen verklaren in de akte of in een vermelding onderaan op de akte dat ze de toepassing vragen van artikel 140/1;

b. als de schenking ook andere goederen omvat dan de goederen, vermeld in artikel 140/1, § 1, geven ze nauwkeurig aan voor welke van de geschonken goederen die deel uitmaken van de familiale onderneming of van het aandelenpakket van de familiale vennootschap, de toepassing van de vrijstelling gevraagd wordt, en voor welke van de geschonken goederen geen toepassing van de vrijstelling gevraagd wordt. Daarnaast moet melding gemaakt worden van:

1. de benaming en het ondernemingsnummer van de familiale onderneming of familiale vennootschap waarvoor de vrijstelling gevraagd wordt;

2. hetzij de activa van de familiale onderneming met een duidelijke omschrijving en verwijzing naar de boekhouding en, als het onroerende goederen betreft, de vermelding of ze al dan niet hoofdzakelijk voor bewoning worden aangewend of zijn bestemd, hetzij het aantal aandelen en stemrechten en de precieze aard van alle aandelen van een familiale vennootschap met enerzijds de vermelding van het aantal aandelen en stemrechten dat in het bezit was van de schenker en van andere bij naam te noemen medeaandeelhouders, en anderzijds de aard van het zakelijk recht dat de schenker en andere bij naam te noemen personen bezitten.

Als de bescheiden, vermeld in het tweede lid, worden bezorgd met een aangetekende brief, geldt de datum van de poststempel op het verzendingsbewijs als datum van de indiening.

###### Art. 140/4

(van toepassing vanaf 01.01.2017)

(ingevoegd bij art. 20, § 1, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

Voor de toepassing van artikel 140/1 en artikel 140/5, § 1, 2°, moet de aanwending of de bestemming van een onroerend goed worden nagegaan per kadastraal perceel of per gedeelte van een kadastraal perceel als dat gedeelte ofwel een afzonderlijk huisvesting is, ofwel een productie- of activiteitenafdeling is die afzonderlijk kan werken, ofwel een eenheid is die van de andere goederen of delen die het perceel vormen, kan worden afgezonderd.

###### Art. 140/5

(van toepassing vanaf 01.01.2018)

(gewijzigd bij art. 5 van de ordonnantie van 01.03.2018 (B.S., 09.03.2018). Tekst van toepassing vanaf 01.01.2018 (art. 21))

§ 1. Na verloop van een termijn van drie jaar vanaf de datum van de authentieke akte van schenking controleert de door de Brusselse Hoofdstedelijke Regering aangeduide ambtenaar of de voorwaarden, gesteld voor het behoud van de vrijstelling, vervuld zijn. Deze laatste brengt de ontvanger van het bevoegde kantoor van de Algemene administratie van de Patrimoniumdocumentatie op de hoogte. De Brusselse Hoofdstedelijke Regering stelt de modaliteiten vast van deze op de hoogte stelling.

Bij niet-vervulling van de voorwaarden, vermeld in het eerste lid, wordt het schenkingsrecht geacht verschuldigd te zijn, berekend tegen het tarief, vermeld in artikel 131, zonder toepassing van de vrijstelling.

Bij niet-vervulling van de voorwaarde, vermeld in artikel 140/2, § 2, 3°, is het schenkingsrecht evenredig verschuldigd tegen het tarief vermeld in artikel 131, zonder toepassing van de vrijstelling.

§ 2. Als de voorwaarden, gesteld tot behoud van de vrijstelling, niet langer vervuld zijn, wordt het schenkingsrecht geacht verschuldigd te zijn, berekend tegen het tarief, vermeld in artikel 131, zonder toepassing van de vrijstelling.

Bij niet-vervulling van de voorwaarden, vermeld in artikel 140/2, § 2, 3°, is het schenkingsrecht evenredig verschuldigd tegen het tarief, vermeld in artikel 131, zonder toepassing van de vrijstelling.

###### Art. 140/6

(van toepassing vanaf 01.01.2018)

(gewijzigd bij art. 6 van de ordonnantie van 01.03.2018 (B.S., 09.03.2018). Tekst van toepassing vanaf 01.01.2018 (art. 21))

§ 1. Het attest uitgereikt door ambtenaar die is aangeduid door de Brusselse Hoofdstedelijke Regering en waarin bevestigd wordt dat voldaan is aan de gestelde voorwaarden wordt voorgelegd op het moment van de registratie van de schenkingsakte. De Brusselse Hoofdstedelijke Regering bepaalt de modaliteiten waaronder dit attest aangevraagd, gecontroleerd en verstrekt wordt.

Indien dit attest niet wordt ingediend voordat de rechten opeisbaar zijn, moeten deze rechten tegen het normale tarief worden berekend. In dat geval zijn de rechten geheven omdat partijen het attest waarvan sprake in deze paragraaf niet voorlegden, vatbaar voor teruggave op de wijze voorzien in artikel 209 wanneer dit attest neergelegd wordt bij de ontvanger van het bevoegde kantoor van de Algemene administratie van de Patrimoniumdocumentatie binnen het jaar na de betaling van de belasting.

§ 2. De begiftigden die de vrijstelling hebben genoten als bedoeld in de artikelen 140/1, 140/2 en 140/3 moeten daarenboven:
1° voor de vijfhonderdste dag die volgt op de datum van de authentieke akte van schenking een attest bezorgen aan de ontvanger van het bevoegde kantoor van de Algemene administratie van de Patrimoniumdocumentatie dat werd afgeleverd door de daartoe door de Brusselse Hoofdstedelijke Regering aangestelde ambtenaar en dat bevestigt dat de vereiste voorwaarden vervuld waren gedurende de eerste driehonderdvijfenzestig dagen die op de datum van de authentieke akte van schenking volgden;

2° voor de achthonderd vijfenzestigste dag die volgt op de datum van de authentieke akte van schenking een attest bezorgen aan de ontvanger van het bevoegde kantoor van de Algemene administratie van de Patrimoniumdocumentatie dat werd afgeleverd door de daartoe door de Brusselse Hoofdstedelijke Regering aangestelde ambtenaar en dat bevestigt dat de vereiste voorwaarden vervuld waren gedurende tussen de driehonderd zesenzestigste dag en de zevenhonderd dertigste dag die op de datum van de authentieke akte van schenking volgden.

De Brusselse Hoofdstedelijke Regering bepaalt de modaliteiten van de aanvraag, de controle en de aflevering van de voornoemde attesten.

In geval de begiftigden één van de voornoemde verplichtingen niet naleven, wordt het schenkingsrecht geacht verschuldigd te zijn, berekend tegen het tarief, vermeld in artikel 131, zonder toepassing van de vrijstelling.

#### Afdeling XIII - Huwelijkscontracten en testamenten

###### Art. 141

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 162 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling XIV- Vonnissen en arresten

###### Art. 142

(van toepassing vanaf 01.01.1994)

(gewijzigd bij art. 4 van de wet van 24.12.1993 (B.S., 31.12.1993 - ed. 2). Tekst van toepassing vanaf 01.01.1994 (art. 26))

Het recht wordt vastgesteld op 3 pct. voor de in alle zaken gewezen arresten en vonnissen der hoven en rechtbanken, houdende definitieve, voorlopige, voornaamste, subsidiaire of voorwaardelijke veroordeling of vereffening gaande over sommen en roerende waarden, met inbegrip van de beslissingen van de rechterlijke overheid houdende rangregeling van dezelfde sommen en waarden.
Het recht wordt vereffend, in geval van veroordeling of vereffening van sommen en roerende waarden, op het samengevoegd bedrag, in hoofdsom, van de uitgesproken veroordelingen of van de gedane vereffeningen ten laste van een zelfde persoon, afgezien van de interesten waarvan het bedrag niet door de rechter is becijferd en kosten, en, in geval van rangregeling, op het totaal bedrag der aan de schuldeisers uitgedeelde sommen

###### Art. 143

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

De bepaling van artikel 142 is niet toepasselijk:

1° op de bevelen in kortgeding en op de arresten gewezen op beroep daarvan;

2° op vonnissen en arresten voor zover zij strafboeten, burgerlijke boeten of tuchtboeten uitspreken;

3° op vonnissen en arresten voor zover zij een veroordeling inhouden tot het betalen van een uitkering tot onderhoud.

Zij is niet toepasselijk wanneer het samengevoegd bedrag van de uitgesproken veroordelingen en van de gedane vereffeningen ten laste van een zelfde persoon, of van de aan de schuldeisers van een zelfde persoon uitgedeelde sommen, 12.500 EUR niet overtreft.

###### Art. 144

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Werd het bij artikel 142 vastgestelde recht op een later veranderd vonnis of arrest geheven, dan wordt voor de nieuwe beslissing het recht van 3 t.h. alleen geheven op de aanvullende veroordeling, vereffening of rangregeling van sommen of waarden uitgesproken of vastgesteld ten laste van een zelfde persoon en voor zover deze 12.500 EUR te boven gaat.

Wanneer een vonnis of arrest een hoofdelijke veroordeling uitspreekt en de op dat vonnis of arrest verschuldigde rechten volledig of gedeeltelijk betaald werden door één van de veroordeelden, maakt de beslissing, waardoor diegene die betaald heeft, buiten zaak wordt gesteld, de rechten die deze betaald heeft opeisbaar in hoofde van de andere hoofdelijke veroordeelden, dit alles onverminderd de toepassing van de voorschriften genomen in het eerste lid.

###### Art. 145

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Werd het bij artikel 142 vastgestelde recht op een vonnis of arrest geheven, dan wordt op elke andere veroordeling ten laste van dezelfde persoon of van een derde, welke steunt hetzij op dezelfde oorzaak hetzij op een verplichting tot waarborg en meer in het algemeen op elke door de in eerste orde veroordeelde persoon uitgeoefende verhaalsvordering, het recht van 3 t.h. alleen geheven op de aanvullende veroordeling tot sommen of waarden, en voor zover deze 12.500 EUR te boven gaat.

###### Art. 146

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 167 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

De vonnissen en arresten die tot bewijs strekken van een overeenkomst waarbij eigendom of vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt en welke aan de desbetreffende belasting niet onderworpen werd geven aanleiding, onverminderd het door artikel 142 vastgesteld recht, tot het recht en eventueel tot de boete waaraan de overeenkomst zou onderworpen zijn indien zij in een minnelijke akte vastgesteld ware geweest.

Dit geldt eveneens, zelfs indien de rechterlijke beslissing die tot bewijs van de overeenkomst strekt, de ontbinding of herroeping ervan voor om 't even welke reden uitspreekt, tenzij uit de beslissing blijkt dat ten hoogste één jaar na de overeenkomst een eis tot ontbinding of herroeping, zelfs bij een onbevoegd rechter, werd ingesteld.

###### Art. 147

(van toepassing vanaf 01.01.1961)

(vervangen bij art. 10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

De vonnissen en arresten houdende vernietiging, ontbinding of herroeping van een overeenkomst waarbij eigendom of vruchtgebruik van in België gelegen onroerende goederen overgedragen of aangewezen wordt, geven geen aanleiding tot heffing van het evenredig recht uit hoofde van dat te niet doen, tenzij die uitgesproken zij ten voordele van een ander persoon dan een van de partijen bij de overeenkomst, haar erfgenamen of legatarissen. In laatstbedoeld geval worden de rechten geheven die verschuldigd waren geweest indien de vernietiging, de ontbinding of de herroeping het voorwerp van een minnelijke akte had uitgemaakt.

###### Art. 148

(van toepassing vanaf 01.01.1961)

(vervangen bij art.10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39)) Exequaturs van scheidsrechterlijke uitspraken en van buitenlands gewezen rechterlijke beslissingen worden, voor de toepassing van dit Wetboek, als een geheel met de desbetreffende akte aangezien, en zijn aan dezelfde rechten als de in België gewezen vonnissen en arresten onderworpen.

Deze rechten zijn eveneens van toepassing in geval van aanbieding ter registratie van een buitenlands gewezen rechterlijke beslissing indien zij van rechtswege in België uitvoerbaar is.

###### Art. 149

(van toepassing vanaf 01.01.1961)

(vervangen bij art. 10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

Behoudens in de gevallen beoogd door de artikelen 146 tot 148 maken de vonnissen en arresten geen evenredig recht eisbaar uit hoofde van de overeenkomsten waarvan zij het bestaan vaststellen.

###### Art. 150

(van toepassing vanaf 01.11.1986)

(hersteld bij art. 12 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst van toepassing vanaf 01.11.1986 (art. 15))

Om de invordering van de rechten en, in voorkomend geval, van de boeten eisbaar uit hoofde van deze afdeling te waarborgen, wordt, ten bate van de Staat, een voorrecht ingesteld op de sommen en waarden die het voorwerp uitmaken van de veroordeling, vereffening of rangregeling.

De rechten en boeten bedoeld in het eerste lid gaan boven alle schuldvorderingen van de begunstigden van de veroordelingen, vereffeningen of rangregelingen.

###### Art. 151

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 152

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling XV - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

###### Art. 153

(van toepassing vanaf 01.01.1969)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

(…)

#### Afdeling XVI - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

###### Art. 154

(van toepassing vanaf 01.01.1969)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

(…)

#### Afdeling XVII - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

###### Art. 155

(van toepassing vanaf 01.01.1969)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 3,
28°, KB van 04.11.1968 (B.S., 13.11.1968))

(…)

#### Afdeling XVIII - (…)

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

###### Art. 156

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling XIX - Protesten

###### Art. 157

(van toepassing vanaf 01.09.2013)

(opgeheven bij art. 73 van de wet van 14.01.2013 (B.S., 01.03.2013). Tekst van toepassing vanaf 01.01.2013 (art. 85))

(…)

#### Afdeling XIXbis - Aangehechte akten en geschriften

(ingevoegd bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87, 3°))

###### Art. 158

(van toepassing vanaf 01.04.2014)

(ingevoegd bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87, 3°))

De aangehechte akten of geschriften bedoeld in artikel 26, tweede lid, worden geregistreerd tegen betaling van één specifiek vast recht van 100 euro voor al die documenten samen, behalve indien sommige ervan een of meer andere in dit hoofdstuk bepaalde rechten verschuldigd maken, in welk geval, naast de rechten verschuldigd voor de registratie van laatstbedoelde documenten, het specifiek vast recht van 100 euro eenmaal verschuldigd is voor de registratie van de overige documenten.

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en onderhevig aan het algemeen vast recht

###### Art. 159

(van toepassing vanaf 09.03.2026)

(14°, gewijzigd bij art. 23 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Worden van het evenredig recht vrijgesteld en aan het algemeen vast recht onderworpen:

1° de aanwijzing van lastgever, op voorwaarde:

a) dat het vermogen om een lastgever aan te wijzen in de akte van toewijzing of koop voorbehouden is;

b) dat de aanwijzing bij authentieke akte geschied is uiterlijk op de vijfde werkdag na de dag van de toewijzing of van het contract;

c) (…).

Bij niet-voldoening aan deze voorwaarden wordt de aanwijzing van lastgever voor de toepassing van dit Wetboek als wederverkoop beschouwd.

Met afwijking van het vorenstaande:

a) moet de aanwijzing van lastgever, bij toewijzingen die wettelijk gedaan zijn onder de schorsende voorwaarde van ontstentenis van opbod, om van het evenredig recht vrijgesteld te zijn, gedaan worden vóór de notaris die de toewijzing gedaan heeft of hem betekend worden uiterlijk op de vijfde werkdag na die waarop de wettelijke termijn voor opbod verstrijkt;

b) moet de aanwijzing van lastgever, in geval van toewijzing ten gevolge van hoger bod op vrijwillige vervreemding van onroerende goederen, om van het evenredig recht vrijgesteld te zijn, gedaan worden vóór de notaris die de toewijzing heeft gedaan of hem betekend worden uiterlijk op de vijfde werkdag na de dag van de toewijzing.

In die gevallen wordt de aanwijzing ingeschreven of vermeld onderaan op het proces-verbaal van toewijzing, zonder dat zij aan de ontvanger der registratie behoeft te worden betekend;

2° de toewijzingen naar aanleiding van rouwkoop, van roerende of onroerende goederen, wanneer zij geen aanleiding geven tot de heffing van een hoger evenredig recht dan datgene geheven op de vorige toewijzing. In het tegenovergesteld geval wordt laatstbedoeld recht afgerekend van het bedrag van de belasting waartoe de daaropvolgende toewijzing aanleiding geeft.

Hetzelfde regime is van toepassing op de toewijzingen naar aanleiding van prijsverhoging in de gevallen waarin het voorbehoud van prijsverhoging geen schorsende voorwaarde uitmaakt.

3° De overeenkomsten die strekken tot de overdracht van het vruchtgebruik op de blote eigenaar, wanneer het evenredig registratierecht of het successierecht door de blote eigenaar of door een vorige blote eigenaar, zijn rechtsvoorganger, op de waarde van de volle eigendom werd voldaan;
4° (…)

5° (…)

6° (…)

7° de overdragende of aanwijzende overeenkomsten, andere dan de inbrengen onderworpen aan het in artikel 115bis bepaalde recht die buitenslands gelegen onroerende goederen tot voorwerp hebben, zomede de huurcontracten van dergelijke goederen;

8° de overdragende of aanwijzende vervreemdingen onder bezwarende titel, andere dan die welke aan het in artikel 115bis bepaalde recht onderworpen zijn, van gebouwen, gedeelten van gebouwen en het bijhorende terrein bedoeld in artikel 1, § 9, van het Wetboek van de belasting over de toegevoegde waarde, evenals de vestigingen, overdrachten of wederoverdrachten van de zakelijke rechten bedoeld in artikel 9, tweede lid, 2°, van het Wetboek van de belasting over de toegevoegde waarde met betrekking tot gebouwen, gedeelten van gebouwen en het bijhorende terrein bedoeld in artikel 1, § 9, van het Wetboek van de belasting over de toegevoegde waarde, op voorwaarde dat de belasting over de toegevoegde waarde opeisbaar is op de levering van deze goederen of de vestiging, de overdracht of wederoverdracht van deze rechten.

Deze vrijstelling is alleen toepasselijk indien in of onderaan de akte of in een vóór de registratie bij de akte te voegen geschrift worden vermeld:

a) de datum van de eerste ingebruikneming of eerste inbezitneming van het gebouw waarop de overeenkomst betrekking heeft;

b) in voorkomend geval, een verklaring van de overdrager, medeondertekend door de verkrijger, dat hij de bedoeling heeft de handeling met toepassing van de belasting over de toegevoegde waarde te verrichten.

c) (…)

In geval de vervreemding of de vestiging, overdracht of wederoverdracht van zakelijke rechten tevens goederen betreft waarop deze vrijstelling van het evenredig recht niet van toepassing is, moet de akte of het bijgevoegde geschrift dit nadrukkelijk vermelden en die goederen nauwkeurig aanduiden door middel van hun kadastrale beschrijving.

In geval van onjuistheid van die vermeldingen verbeurt de cedent een boete gelijk aan het ontdoken recht;

9° (…)

10° de contracten van onroerende financieringshuur bedoeld in artikel 44, § 3, 2°, b, van het Wetboek van de belasting over de toegevoegde waarde;

11° de inbreng van goederen in Europese economische samenwerkingsverbanden;
12°    de    teruggave     van    de    onroerende      goederen      aan     de   leden   van   Europese   economische samenwerkingsverbanden die deze goederen hebben ingebracht, wanneer de teruggave gebeurt tengevolge van de uittreding van deze leden of de ontbinding van het samenwerkingsverband.

Indien onroerende goederen verkregen worden in andere omstandigheden dan deze voorzien in het vorige lid, is voor deze verkrijging, hoe zij ook gebeurt, het voor verkopingen bepaalde recht verschuldigd.

13° (…)

14° de inbrengen van onroerende goederen, andere dan die welke gedeeltelijk of geheel tot bewoning aangewend worden of bestemd zijn en door een natuurlijke persoon ingebracht worden, in vennootschappen met zetel van werkelijke leiding en statutaire zetel buiten België, of met statutaire zetel in België doch met zetel van werkelijke leiding op het grondgebied van één van de lidstaten van de Europese Unie. Deze vrijstelling geldt voor zover de inbreng met maatschappelijke rechten wordt vergolden. Indien de inbreng zowel in België gelegen onroerende goederen als andere goederen omvat wordt, niettegenstaande elk strijdig beding, de vergelding die anders dan door toekenning van maatschappelijke rechten geschiedt, geacht evenredig verdeeld te zijn tussen de waarde die aan de onroerende goederen is toegekend en die welke aan de andere goederen is toegekend. In de mate dat de inbreng betrekking heeft op in België gelegen onroerende goederen wordt hij onderworpen aan het recht voorgeschreven voor verkopingen.

In geval van onjuiste verklaring betreffende de aanwending of de bestemming van het onroerend goed, worden de bijvoeglijke rechten opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.

#### Afdeling XXI - Akten vrijgesteld van het evenredig recht en onderhevig aan een bijzonder vast recht van 10 euro

(ingevoegd bij art. 18 van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 - ed. 3). Tekst van toepassing voor alle overeenkomsten onderworpen aan de evenredige rechten bedoeld in de art. 44 tot 71, 72, 2de lid, 74 en 75, 109 tot 114, 131 tot 140octies W.Reg. die niet vóór 29.12.2016 zijn gesloten (art. 40, § 3))

###### Art. 159bis

(van toepassing vanaf 29.12.2016)

(ingevoegd bij art. 18 van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 - ed. 3). Tekst van toepassing voor alle overeenkomsten onderworpen aan de evenredige rechten bedoeld in de art. 44 tot 71, 72, 2de lid, 74 en 75, 109 tot 114, 131 tot 140octies W.Reg. die niet vóór 29.12.2016 zijn gesloten (art. 40, § 3))

§ 1. Worden van het evenredig recht vrijgesteld en aan een bijzonder vast recht van 10 euro onderworpen:

1° de overeenkomsten bedoeld in de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies maar waarvan de nietigverklaring, de vernietiging, de annulering of de ontbinding minnelijk is overeengekomen tussen de partijen uiterlijk op het moment waarop de akte ter registratie wordt aangeboden op volgende voorwaarden:

a) de overeenkomst tot nietigverklaring, vernietiging, annulering of ontbinding ook ter registratie wordt aangeboden uiterlijk op hetzelfde moment als de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst, met toepassing op die overeenkomst van het in 2° van deze paragraaf bedoelde bijzonder vast recht;

b) de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst die nog niet vastgesteld is bij een authentieke akte;

c) de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst die niet meer dan één jaar vóór het sluiten van de overeenkomst tot nietigverklaring, vernietiging, annulering of ontbinding is gesloten;

2° de overeenkomsten tot nietigverklaring, vernietiging, annulering of ontbinding van overeenkomsten onderworpen aan de evenredige rechten bedoeld in de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies of van overeenkomsten onderworpen aan het vast recht van het 1° van deze paragraaf op volgende voorwaarden:

a) de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst is nog niet vastgesteld bij een authentieke akte;

b) de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst is niet meer dan één jaar vóór het sluiten van de overeenkomst tot nietigverklaring, vernietiging, annulering of ontbinding gesloten.

§ 2. Worden van het evenredig recht vrijgesteld en aan een bijzonder vast recht van 10 euro onderworpen:

1° de overeenkomsten bedoeld in de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies maar waarvan de annulering voortvloeit uit de toepassing van een ontbindende voorwaarde van rechtswege uitgevoerd uiterlijk op het moment waarop de akte ter registratie wordt aangeboden op volgende voorwaarden:

a) de vervulling van de ontbindende voorwaarde wordt vastgesteld in een akte getekend door alle partijen en ter registratie aangeboden, uiterlijk op hetzelfde ogenblik als de ontbonden overeenkomst, met toepassing, op die schriftelijke akte, van het bijzonder vast recht bedoeld in het 2° van deze paragraaf; wanneer de ontbonden overeenkomst vastgesteld is bij een authentieke akte, moet de vervulling van de ontbindende voorwaarde in een authentieke akte vastgesteld worden, die door alle partijen getekend wordt;

de ontbonden overeenkomst is niet meer dan één jaar voor de datum van vervulling van de ontbindende voorwaarde gesloten;

2° de akten die de vervulling van een ontbindende voorwaarde van rechtswege vaststellen, waarbij de ontbinding van de overeenkomsten onderworpen aan de evenredige rechten bedoeld in de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies of van overeenkomsten onderworpen aan het vast recht van het 1° van deze paragraaf als gevolg heeft, op volgende voorwaarden: a. wanneer de ontbonden overeenkomst bij een authentieke akte vastgesteld is, wordt de vervulling van de ontbindende voorwaarde ook bij een authentieke akte getekend door alle partijen vastgesteld;

b. de ontbonden overeenkomst is niet meer dan één jaar voor de datum van vervulling van de ontbindende voorwaarde gesloten.

### HOOFDSTUK V - Registratie in debet

###### Art. 160

(van toepassing vanaf 01.01.2015)

(gewijzigd bij art. 5 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van toepassing vanaf 01.01.2015 (art. 8))

In afwijking van artikel 169ter, worden in debet geregistreerd:

1° de akten opgemaakt ten verzoek van de persoon die rechtsbijstand heeft verkregen voor de rechtspleging waarop bedoelde akten betrekking hebben, met inbegrip van de akten tot ten uitvoerlegging van het vonnis of arrest.

Het gaat evenzo met de rechterlijke beslissingen wanneer rechtsbijstand aan de eiser werd toegestaan. Wanneer bijstand aan de verweerder werd toegestaan en de eiser in gebreke blijft de op het vonnis of arrest verschuldigde rechten te consigneren, kan de verweerder registratie in debet ervan bekomen.

Verlening van bijstand dient te worden vermeld in al de akten die ervan genieten. Deze vermelding moet de datum der beslissing alsmede het gerecht of het bureau voor rechtsbijstand, dat ze heeft getroffen, aanduiden.

De rechten alsmede de andere kosten worden ingevorderd overeenkomstig de bepalingen van het Gerechtelijk Wetboek;

2° de akten en vonnissen betreffende procedures bij faillissement, wanneer de kosteloosheid door de rechtbank werd bevolen.

De kosteloosheid van de rechtspleging moet vermeld worden in alle akten die ze genieten.

De rechten alsmede de andere kosten worden ingevorderd overeenkomstig de bepalingen van het Gerechtelijk Wetboek;

3° de akten betreffende de vorderingen tot interpretatie of tot verbetering van een vonnis of arrest.

De rechten worden ingevorderd overeenkomstig de bepalingen van het Gerechtelijk Wetboek;

4° de akten opgemaakt ten verzoek en ter verdediging van de beklaagden of betichten in lijfstraffelijke, boetstraffelijke of politiezaken er weze al dan niet een burgerlijke partij in het geding met inbegrip van de akten waartoe de borg, welke dient gesteld om de voorlopige invrijheidstelling van een voorlopig gedetineerd betichte te bekomen, aanleiding geeft.

De rechten worden in de gerechtskosten begrepen en als zodanig ingevorderd ten laste van de tot betaling er van veroordeelde partij.

### HOOFDSTUK VI - Kosteloze registratie

###### Art. 161

(van toepassing vanaf 09.03.2026)

(12°, gewijzigd bij art. 29 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Worden kosteloos geregistreerd:

1° Akten in der minne verleden ten name of ten bate van de Staat, gefedereerde entiteiten en de openbare instellingen ervan.

De akten in der minne, die betrekking hebben op onroerende goederen die uitsluitend bestemd zijn voor onderwijs, verleden ten name of ten bate van de inrichtende machten van het gemeenschapsonderwijs of het gesubsidieerd onderwijs, alsook ten name of ten bate van verenigingen zonder winstoogmerk voor patrimoniaal beheer die tot uitsluitend doel hebben onroerende goederen ter beschikking te stellen voor onderwijs dat door de voornoemde inrichtende machten wordt versterkt.

De akten in der minne verleden ten name of ten bate van de naamloze vennootschap van publiek recht HST-Fin.

De akten in der minne verleden ten name of ten bate van de naamloze vennootschap A.S.T.R.I.D.

De akten verleden ten name of ten bate van de naamloze vennootschap BIO.

De aktes met betrekking tot onroerende goederen gelegen op het grondgebied van het Brussels Hoofdstedelijk Gewest, die worden aangenomen in naam of ten voordele van de naamloze vennootschap van publiek recht Brusselse Maatschappij voor Waterbeheer, voor zover deze aktes de verschuldiging van een gewestelijke belasting meebrengen in de zin van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten.

De akten verleden ten name of ten bate van het " Brussels Agentschap voor het Ondernemerschap ", die betrekking hebben op onroerende goederen op het grondgebied van het Brussels Hoofdstedelijk Gewest.

De akten die betrekking hebben op onroerende goederen gelegen op het grondgebied van het Brussels Hoofdstedelijk Gewest en die worden verleden in naam of ten gunste van de Maatschappij voor Stedelijke Inrichting.
Hetzelfde geldt - met uitzondering van akten houden de schenking onder de levenden - voor akten verleden ten name of ten bate van de Nationale Maatschappij voor de Huisvesting, de Nationale Landmaatschappij en de Nationale Maatschappij van Belgische spoorwegen;

Deze beschikking is echter slechts van toepassing op de akten waarvan de kosten wettelijk ten laste van bedoelde organismen vallen.

De kosteloze registratie geldt niet voor akten houdende schenkingen onder de levenden aan andere onder deze rubriek bedoelde lichamen dan het Brussels Hoofdstedelijk Gewest, de Brusselse Agglomeratie, de Vlaamse Gemeenschapscommissie,        de     Franse     Gemeenschapscommissie         en     de     Gemeenschappelijke Gemeenschapscommissie en de openbare instellingen van deze publiekrechtelijke rechtspersonen en de naamloze vennootschap van publiek recht Brusselse Maatschappij voor Waterbeheer.

1°bis De vonnissen en arresten houdende veroordeling van de Staat, de Gemeenschappen en de Gewesten, van de openbare instellingen die zijn opgericht door de Staat, en van de inrichtingen van de Gemeenschappen en de Gewesten.

2° Overdrachten in der minne van onroerende goederen ten algemenen nutte, aan Staat, provinciën, gemeenten, openbare instellingen en aan alle andere tot onteigening gerechtigde organismen of personen; akten betreffende de wederafstand na onteigening ten algemenen nutte in de gevallen waarin hij bij de wet toegelaten is; akten tot vaststelling van een ruilverkaveling of een herverkaveling verricht met inachtneming van de bepalingen van
#### Hoofdstuk VI van Titel I van de wet houdende organisatie van de ruimtelijke ordening en van de stedebouw. De akten houdende overdracht van een afgedankte bedrijfsruimte aan de Staat of een andere publiekrechtelijke rechtspersoon.

3° De akten houdende oprichting, wijziging, verlenging of ontbinding van de Nationale Maatschappij der Waterleidingen, van de verenigingen overeenkomstig de bepalingen der wetten van 18 augustus 1907 en van 1 maart 1922 gevormd, van de Maatschappij voor het Intercommunaal Vervoer te Brussel, van de maatschappij voor tussengemeentelijk vervoer beheerst door de wet betreffende de oprichting van maatschappijen voor stedelijk gemeenschappelijk      vervoer,    van     de     Federale     Investeringsmaatschappij,     de     gewestelijke investeringsmaatschappijen en van de Belgische Naamloze Vennootschap tot Exploitatie van het Luchtverkeer (Sabena).

4° Akten die, bij toepassing van de organieke wet betreffende de openbare centra voor maatschappelijk welzijn, de overgave vaststellen van goederen aan of de inbreng in openbare centra voor maatschappelijk welzijn ofwel de overgave van goederen aan of de inbreng in op grond van voornoemde wet opgerichte verenigingen, evenals akten houdende verdeling, na ontbinding of splitsing van een bovenbedoelde vereniging.

5° Waarmerkingen en akten van bekendheid, in de gevallen bedoeld in artikel 139 van de hypotheekwet van 16 december 1851;

6° Akten houdende verkrijging door vreemde Staten van onroerende goederen die bestemd zijn tot vestiging van hun diplomatieke of consulaire vertegenwoordiging in België, of voor de woning van het hoofd der standplaats.
De kosteloosheid is echter ondergeschikt aan de voorwaarde dat wederkerigheid aan de Belgische Staat toegekend wordt.

7° De akten, vonnissen en arresten betreffende de uitvoering van de wet houdende bijzondere maatregelen inzake ruilverkaveling van landeigendommen in der minne;

8° (…)

9° Akten, vonnissen en arresten betreffende de uitvoering der wet op de ruilverkaveling van landeigendommen uit kracht van de wet en de wet houdende bijzondere maatregelen inzake ruilverkaveling van landeigendommen uit kracht van de wet bij de uitvoering van grote infrastructuurwerken.

10° Akten tot vaststelling van een vereniging van kolenmijnconcessies, een afstand, een uitwisseling of een verpachting van een gedeelte van deze concessies.

De kosteloosheid is ondergeschikt aan de voorwaarde dat een eensluidend verklaard afschrift van het koninklijk besluit, waarbij de verrichting toegelaten of bevolen wordt, aan de akte gehecht is op het ogenblik der registratie.

Het eerste lid is mede van toepassing wanneer bedoelde akten terzelfder tijd de afstand vaststellen van goederen die voor de exploitatie van de afgestane concessie of het afgestane concessiegedeelte worden gebruikt.

11° De akten en attesten die gevoegd moeten worden bij de akten van schenking van ondernemingen.

12°
a) de akten houdende verhuring, onderverhuring of overdracht van huur van in België gelegen onroerende goederen of gedeelten van onroerende goederen, die uitsluitend bestemd zijn tot huisvesting van een gezin of van één persoon;

b) (…);

c) de plaatsbeschrijvingen opgemaakt naar aanleiding van een onder a) bedoelde akte;

d) de documenten die krachtens wettelijke, decretale of ordonnantiële bepalingen gevoegd zijn bij een onder a) bedoelde akte op het ogenblik dat zij ter registratie wordt aangeboden.

13° De overeenkomsten bedoeld in artikel 132bis van het Wetboek van de inkomstenbelastingen 1992.

14° een authentieke volmacht die uitsluitend bestemd is om een of meer partijen te laten vertegenwoordigen bij het verlijden van een authentieke akte, op voorwaarde dat de instrumenterende ambtenaar voor het verlijden van de volmacht geen ereloon, vacaties of kosten vraagt en voor zover de volmacht uitsluitend effect sorteert binnen de zes maanden na de ondertekening ervan.

15° De verklaring van verwerping ten overstaan van een notaris bedoeld in artikel 4.44, eerste lid, van het Burgerlijk Wetboek, onder de voorwaarden bedoeld in het derde lid van hetzelfde artikel. (1) De bijlagen bij een dergelijke verklaring worden ook kosteloos geregistreerd, behalve wanneer ze een in Titel I,
#### Hoofdstuk IV van het Wetboek bepaald recht, ander dan het in artikel 158 bepaalde recht, opeisbaar maken.

16° de akten van erfopvolging bedoeld in artikel 3.30, § 1, 7°, van het Burgerlijk Wetboek, op voorwaarde dat de instrumenterende ambtenaar voor het opstellen van de akte geen vacaties of kosten vraagt en de akte opgesteld wordt binnen de 6 maanden na het overlijden.
(1) Vanaf 03.08.2017 tot 02.08.2020 mag het netto actief van de nalatenschap niet meer bedragen dan 5.000 EUR. Vanaf 03.08.2020 tot 31.07.2023 bedraagt het geïndexeerde bedrag 5.219,21 euro. Vanaf 01.08.2023 tot 31.07.2026 bedraagt het geïndexeerde bedrag 6.093,20 euro (EE/107.394).

###### Art. 161/1

(van toepassing vanaf 09.11.2019)

(gewijzigd bij art. 1 van het KB van 03.10.2019 (B.S., 30.10.2019). Tekst van toepassing vanaf 09.11.2019 (art. -))

Onverminderd artikel 162, 51°, worden de akten, vonnissen en arresten, betreffende een overeenkomstig Boek XX, Titel V van het Wetboek van economisch recht ingestelde procedure van gerechtelijke reorganisatie vrijgesteld van de registratierechten die niet worden bedoeld in artikel 3 van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten.

### HOOFDSTUK VII - Vrijstelling van de formaliteit der registratie

###### Art. 162

(van toepassing vanaf 02.09.2023)

(10°, opgeheven bij art. 4 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst van toepassing vanaf 02.09.2023 (art. -))

Zijn onder het in artikel 163 aangewezen voorbehoud, van de formaliteit der registratie vrijgesteld.

1° Akten, vonnissen en arresten in kieszaken;

2° Akten, vonnissen en arresten betreffende de uitvoering van wetten en reglementen op de militie, de vergoeding inzake militie en de militaire opeishingen;

3° Akten, vonnissen en arresten betreffende de uitvoering der wetten en reglementen inzake 's lands mobilisatie en de bescherming der bevolking in geval van oorlog, de burgerlijke opeischingen en vrijwillige dienstnemingen, alsmede de in vredestijd aangegane uitgestelde contracten;

4° Akten, vonnissen en arresten betreffende de uitvoering van wetten en reglementen inzake belastingen ten bate van de Staat, gefedereerde entiteiten, provincies, gemeenten, polders en wateringen;
5° Exploten en andere akten, in strafzaken opgemaakt ten verzoek van ambtenaren van het openbaar ministerie en van andere ambtenaren of besturen waaraan de wet de vordering voor de toepassing der straffen opdraagt; bovenaan op bedoelde akten worden de woorden Pro Justitia aangebracht;

5°bis De akten waartoe de rechtsplegingen in burgerlijke zaken of tuchtzaken aanleiding geven, wanneer het openbaar ministerie of de vrederechter van ambtswege optreedt;

6° (…)

6°bis Akten, vonnissen en arresten betreffende de uitvoering der wet op eerherstel in strafzaken en deze betreffende de uitvoering der wet tot bescherming der maatschappij tegen de abnormalen en de gewoontemisdadigers;

7° Akten, vonnissen en arresten inzake onteigeningen ten algemenen nutte en die welke betrekking hebben op de uitvoering van Titel I van de wet houdende organisatie van de ruimtelijke ordening en van de stedenbouw, met uitzondering van de in artikel 161, 2°, bedoelde akten;

8° Akten, vonnissen en arresten betreffende ingebruikneming van gronden door den Staat met het oog op de inrichting van 's Lands verdediging;

9° Akten en vonnissen betreffende procedures vóór den onderzoeksraad voor de zeevaart;

10° (…)

11° De akten, vonnissen en arresten inzake onttrekking van de zaak aan de rechter, zoals bedoeld in het Gerechtelijk Wetboek, deel III, titel IV, hoofdstuk III;

12° De akten, vonnissen en arresten inzake wraking, zoals bedoeld in het Gerechtelijk Wetboek, deel IV, boek II, titel III, hoofdstuk V;

13° Akten en vonnissen betreffende procedures vóór vrederechters, wanneer het bedrag van den hoofdeisch het maximum van den laatsten aanleg niet te boven gaat, of wanneer het gaat om een procedure inzake uitkering tot onderhoud of ingesteld overeenkomstig artikel 221 van het Burgerlijk Wetboek; Akten en vonnissen betreffende procedures vóór de ondernemingsrechtbanken, wanneer het geschillen geldt die gegrond zijn op de bepalingen van het Wetboek van bepaalde voorrechten op zeeschepen en diverse bepalingen of van de wet van 5 mei 1936 op de rivierbevrachting, indien het bedrag van de hoofdeis het bedrag van de laatste aanleg vóór het vredegerecht niet te boven gaat;

13°bis De exploten van gerechtsdeurwaarders opgesteld ter vervanging van een gerechtsbrief in het geval bepaald in artikel 46, § 3, van het Gerechtelijk Wetboek;

Bovenaan het exploot dient te worden vermeld dat het is opgesteld ter vervanging van een gerechtsbrief en zulks met vermelding van het artikel van het Gerechtelijk Wetboek op grond waarvan de betekening wordt gedaan;
14° Akten, vonnissen en arresten betreffende procedures ingesteld bij de wetten van 10 Maart 1900 op de arbeidsovereenkomst, van 7 Augustus 1922 op de bediendenarbeidsovereenkomst en van 5 Juni 1928 houdende regeling van het arbeidscontract wegens scheepsdienst, met betrekking tot de bekwaamheid van de minderjarige om zijn arbeid te verhuren en zijn loon of bezoldiging te ontvangen;

15° Akten opgemaakt ten verzoeke van de ambtenaren van het openbaar ministerie betreffende de uitvoering van rogatoire opdrachten die uitgaan van buitenlandse rechters;

16° (...)

17° De akten, vonnissen en arresten betrekking hebbende op de uitvoering van de wet betreffende het herstel van zekere schade veroorzaakt aan private goederen door natuurrampen;

18° De akten, vonnissen en arresten betreffende procedures ingesteld bij de wet van 26 juni 1990 betreffende de bescherming van de persoon van de geesteszieke en bij de artikelen de bepalingen van het vierde deel, boek IV, hoofdstuk X van het Gerechtelijk Wetboek.

19° de akten, vonnissen en arresten betreffende procedures tot machtiging ingesteld overeenkomstig artikel 4.40,
§ 3 van het Burgerlijk Wetboek;

20° (...)

21° Voorzieningen in verbreking van het openbaar ministerie en derzelver betekeningen;

22° (...)

23° Akten opgemaakt alsmede vonnissen of arresten gewezen voor de toepassing van de wetten op het gebruik van de talen in de gerechtszaken en in bestuurszaken;

24° Akten betreffende de uitvoering van de bepalingen van het Gerechtelijk Wetboek inzake de inruststelling der magistraten;

25° (...)

26° (...)

26°bis (...)

27° (...)

28° (...)

29° Getuigschriften, akten van bekendheid, volmachten, machtigingen met inbegrip van de verzoekschriften die er zouden verband mede houden, wanneer die stukken opgemaakt of uitgereikt worden om te worden overgelegd aan de diensten van het Grootboek van de Rijksschuld aan de Deposito- en Consignatiekas, zomede aan de mutualiteitsverenigingen, spaar-, lijfrente-, voorzorgs- en onderstandskassen erkend door de regering, ingesteld met goedkeuring van de bestuursoverheid of aan dezer controle onderworpen;

30° (...)

31° (...)

32° (...)

33° Akten opgemaakt voor den dienst van de openbare kassen van lening, met inbegrip van processen-verbaal van openbaren verkoop van in pand gegeven roerende voorwerpen;

33°bis      Akten,   vonnissen   en      arresten   betreffende   betwistingen   inzake   arbeidsovereenkomsten, leerovereenkomsten en overeenkomsten voor versnelde beroepsopleiding, betreffende betwistingen tussen werknemers naar aanleiding van het werk alsmede tussen personen die samen een beroep uitoefenen waarbij hoofdzakelijk handenarbeid wordt verricht en inzonderheid tussen een schipper ter visserij en de schepelingen met wie hij geassocieerd is, betreffende betwistingen van burgerlijke aard die het gevolg zijn van een overtreding van de wetten en verordeningen betreffende de arbeidsreglementering en de aangelegenheden onder de bevoegdheid van de arbeidsrechtbank;

34° Akten, vonnissen en arresten betrekkelijk de uitvoering van de wetten en reglementen op de kinderbijslagen;

35° Akten, vonnissen en arresten betrekkelijk de uitvoering van de wetten en reglementen op de verzekering tegen de geldelijke gevolgen van ouderdom en vroegtijdige dood, op de verzekering tegen de geldelijke gevolgen van ouderdom en vroegtijdige dood van bedienden en op het pensioenstelsel der mijnwerkers;

35°bis De akten, vonnissen en arresten in verband met de uitvoering van de wetten en verordeningen betreffende het sociaal statuut der zelfstandigen;

35°ter De akten, vonnissen en arresten betreffende de uitvoering van de wetten en verordeningen betreffende de rust-, invaliditeits-, en overlevingspensioenen ten laste van de Staat, de provincies, de gemeenten, de openbare instellingen, de Nationale Maatschappij der Belgische Spoorwegen of alle andere organismen of openbare diensten waarvan het personeel onderworpen is aan een bijzondere pensioenregeling getroffen bij of krachtens een wet;

35°quater De akten, vonnissen en arresten betreffende de uitvoering van de wetten, decreten en verordeningen betreffende de rust-, invaliditeits- en overlevingspensioenen van de leden van het beroepspersoneel der kaders in Afrika en der personeelsleden die zijn bedoeld in artikel 31, van het koninklijk besluit van 21 mei 1964 tot coördinatie van de wetten betreffende het personeel in Afrika;

36° Akten, vonnissen en arresten betreffende de uitvoering der wetten en reglementen op het herstel van schade ten gevolge van arbeidsongevallen, van ongevallen overkomen op weg naar of van den arbeid, of van beroepsziekten;

36°bis Akten, vonnissen en arresten betreffende betwistingen in verband met de rechten en verplichtingen voortvloeiend uit de wet op de sociale reclassering van de minder-validen;
36°ter Akten, vonnissen en arresten betreffende betwistingen in verband met de oprichting en de inrichting van de ondernemingsraden, alsmede van de diensten en comités tot veiligheid, hygiëne en verfraaiing der werkplaatsen, daarin begrepen de diensten en comités opgericht in mijnen, groeven en graverijen;

37° Akten, vonnissen en arresten betreffende de uitvoering der wetten en reglementen op de onvrijwillige werkloosheid;

37°bis Akten, vonnissen en arresten betreffende de uitvoering der wetten en reglementen in verband met de maatschappelijke zekerheid;

38° Akten en beslissingen betreffende het verzoek om rechtsbijstand of de betwisting ervan; akten van schikking inzake uitkering tot onderhoud verleden op het bureel van bijstand;

39° Akten, vonnissen en arresten betreffende de invordering van de voorschotten van Rijkswege gedaan in uitvoering van de bepalingen van het Gerechtelijk Wetboek betreffende de gerechtelijke bijstand;

40° Akten, vonnissen en arresten betreffende de uitvoering van de wet van 27 juni 1969 betreffende het toekennen van tegemoetkomingen aan de minder-validen;

41° Akten nodig voor het huwelijk van personen wier onvermogen blijkt uit een getuigschrift van den burgemeester van hun verblijfplaats of van dezes gelastigde;

42° Akten, vonnissen en arresten betreffende procedures inzake de voogdij van minderjarigen;

43° Akten betreffende de vrijwillige erkenning van een natuurlijk kind of de ontvoogding, wanneer het onvermogen der kinderen en van hun ouders vastgesteld is overeenkomstig bovenstaand nr. 41°;

44° Akten, vonnissen en arresten betreffende de verklaringen van nationaliteit of van keuze van vaderland, wanneer het onvermogen der belanghebbenden vastgesteld is overeenkomstig bovenstaand nr. 41°;

45° De akten, vonnissen en arresten betreffende betwistingen in verband met een maatregel van sociale bescherming;

46° De akten, vonnissen en arresten, betreffende de procedure van collectieve schuldenregeling ingesteld overeenkomstig de artikelen 1675/2 tot en met 1675/19 van het Gerechtelijk Wetboek;

46° (47°) (1) De overdrachten tussen de componenten van een politieke partij zoals die zijn bepaald bij artikel 1, 1°, tweede lid, van de wet van 4 juli 1989 betreffende de beperking en de controle van de verkiezingsuitgaven voor de verkiezingen van de federale Kamers, de financiering en de open boekhouding van de politieke partijen;

47° (48°) (2) De akten, vonnissen en arresten betreffende de tegemoetkomingen bedoeld in de wet van 21 februari 2003 tot oprichting van een Dienst voor alimentatievorderingen bij de FOD Financiën;

47° (49°) (3) De akten, de vonnissen en arresten, betreffende het toestaan van betalingsfaciliteiten inzake consumentenkrediet, ingesteld overeenkomstig de artikelen 1337bis tot en met 1337octies van het Gerechtelijk Wetboek;
48° (50°) De akten en vonnissen betreffende de procedures voor de rechters voor de bescherming van de maatschappij en de strafuitvoeringsrechtbanken, alsook de arresten gewezen als gevolg van een cassatieberoep tegen een beslissing van de rechter voor de bescherming van de maatschappij of de kamer voor de bescherming van de maatschappij;

51° De akten, vonnissen en arresten betreffende een overeenkomstig Boek XX, Titel V van het Wetboek van economisch recht ingestelde procedure van gerechtelijke organisatie, behalve:

a) de akten die tot bewijs strekken van een overeenkomst onderworpen aan een registratierecht bedoeld in artikel 3 van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten;

b) de in artikelen 146 en 147 bedoelde vonnissen en arresten;

52° De exploten en processen-verbaal van de gerechtsdeurwaarders in verband met de invordering van onbetwiste geldschulden bedoeld in de artikelen 1394/20 tot 1394/27 van het Gerechtelijk Wetboek.
(1) Aangezien door de wet van 05.07.1998 (B.S., 31.07.1998), eveneens een “46°” werd ingevoegd, zou het “46°” dat werd ingevoegd bij de wet van 19.11.1998 (B.S., 10.12.1998), in feite “47°” moeten zijn.
(2) Het “47°” ingevoegd bij art. 28, § 1 van de wet van 21.02.2003 zou het “48°” moeten zijn.
(3) Het “47°” ingevoegd bij art. 82 van de wet van 24.03.2003 zou het “49°” moeten zijn.

###### Art. 163

(van toepassing vanaf 04.05.1965)

(gewijzigd bij art. 16 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

De bij voorgaand artikel ingevoerde vrijstelling is niet toepasselijk op de in dit artikel opgesomde akten, vonnissen en arresten, in zover zij tot bewijs van een overeenkomst strekken voorzien in artikel 19, 2°.

Zij is niet van toepassing op andere dan gerechtelijke akten, in zover zij tot bewijs van een in artikel 19, 3° of 5°, bedoelde overeenkomst strekken.

Tenzij er anders over beschikt wordt, is ze niet van toepassing op:

a) processen-verbaal van verkoop van in beslag genomen roerende of onroerende goederen en alle nakomende handelingen welke derde verkrijgers aanbelangen;

b) processen-verbaal van rangregeling en van verdeling bij aandelen.

###### Art. 164

(van toepassing vanaf 01.02.1940)
Zijn mede van de formaliteit der registratie vrijgesteld, de uitgiften, afschriften van en uittreksels uit akten welke geregistreerd werden of die krachtens artikel 162 van de formaliteit zijn vrijgesteld.

###### Art. 165

(van toepassing vanaf 01.02.1940)

Indien een bij artikelen 162 en 164 van de formaliteit der registratie vrijgestelde akte of geschrift toch ter registratie wordt aangeboden, geeft zij aanleiding tot het heffen van het algemeen vast recht.

### HOOFDSTUK VIII - Diverse bepalingen betreffende de vereffening van de rechten en de betaling van het verschuldigde bedrag

(gewijzigd bij art. 6 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van toepassing vanaf 01.01.2015 (art. 8))

###### Art. 166

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 5, § 7, 1° van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 3° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1) err. (B.S., 21.12.2001). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

In geval van openbare verkoping van roerende of onroerende goederen of van openbare verhuring, in verschillende loten, wordt het recht vereffend op het samengevoegd bedrag der aan hetzelfde tarief onderworpen loten.

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de hogere eurocent afgerond.

###### Art. 167

(van toepassing vanaf 01.02.1940)

Wanneer er niet anderszins bij deze titel over beschikt is, mag het bedrag van het op een akte of een verklaring te heffen evenredig recht niet minder dan in het algemeen vast recht bedragen.

###### Art. 168

(van toepassing vanaf 04.05.1965)

(gewijzigd bij art. 17 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

Wanneer de sommen en waarden of andere ter vereffening van de belasting noodzakelijke gegevens niet voldoende uitgedrukt zijn in een ter formaliteit aangeboden akte, zijn de partijen of de werkende openbare officier, in hun naam, er toe gehouden daarin, vóór de registratie, te voorzien door een aanvullende verklaring, gewaarmerkt en ondertekend onderaan de akte.

Wanneer een zelfde overeenkomst meteen op in België gelegen onroerende goederen en op andere goederen slaat, moet de overeengekomen waarde of, in voorkomend geval, de verkoopwaarde van de goederen van elkeen der categorieën, zelfs indien het tarief van de belasting niet verschilt naar gelang van de aard van de goederen, afzonderlijk aangeduid worden, hetzij in de akte, hetzij in een door de partijen of, in hun naam, door de werkende notaris vóór de registratie gewaarmerkte en ondertekende verklaring onderaan op de akte.

Indien de bepaling van den belastbaren grondslag geheel of gedeeltelijk van de schatting van een levenslang recht afhangt, moet de verklaring naam, voornamen, woonplaats, plaats en datum van geboorte van de beneficianten van dit levenslang recht vervatten.

###### Art. 169

(van toepassing vanaf 01.02.1940)

De rechten verschuldigd op akten waarbij eigendom of vruchtgebruik van een handelszaak overgedragen of aangewezen worden, worden geheven volgens de aard van elk der goederen die er deel van uitmaken en op de bij dit wetboek vastgestelde grondslagen.

De schulden die al dan niet met de handelszaak in verband staan en die door den nieuwe eigenaar of vruchtgebruiker ten laste genomen worden, moeten als lasten van de overeenkomst beschouwd worden.

###### Art. 169bis

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 2, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

Voor de toepassing van de artikelen 115bis en 140bis (1), moet de aanwending of de bestemming van een onroerend goed worden nagegaan per kadastraal perceel of per gedeelte van kadastraal perceel wanneer dat gedeelte is ofwel een afzonderlijke huisvesting, ofwel een afdeling van de productie of van de werkzaamheden die, of een onderdeel daarvan dat, afzonderlijk kan werken, ofwel een eenheid die van de andere goederen of delen die het perceel vormen kan worden afgezonderd.
(1) Volgens art. 20, § 2, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 - ed. 3): « Elke vermelding van 140bis in het Wetboek der registratie-, hypotheek-, en griffierechten, dient te worden gelezen als vermelding van artikel 140/1 en volgende ».

###### Art. 169ter

(van toepassing vanaf 01.12.2021)

(gewijzigd bij art. 2 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van toepassing vanaf 01.12.2021 (art. 7)) De rechten en, in voorkomend geval, de boeten en de interesten, zoals zij door het in artikel 39 bedoelde kantoor zijn vastgesteld, worden voorafgaandelijk aan de registratie betaald.

Behalve wanneer ze verschuldigd zijn in het kader van de registratierechten die, krachtens artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de gemeenschappen en de gewesten, worden aangemerkt als gewestelijke belastingen, kan de Koning, bij een besluit vastgesteld na overleg in de Ministerraad, in afwijking van het eerste lid bepalen dat de rechten, boeten en interesten die verschuldigd zijn op de door Hem aangewezen categorieën van akten, kunnen of moeten worden betaald na de registratie. In voorkomend geval bepaalt hij de termijn en de nadere regels van de betaling.

Niemand kan, onder voorwendsel van betwisting van het verschuldigde bedrag of om enige andere reden, die betaling verminderen of uitstellen, behoudens het recht om teruggave te vorderen, indien daartoe grond bestaat.

### HOOFDSTUK IX - Verplichtingen met het oog op het verzekeren van het heffen van de rechten

#### Afdeling I - Vermeldingen op te nemen in bepaalde akten

###### Art. 170

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Wanneer, in een ander dan een vonnis of arrest aan de formaliteit onderworpen authentieke akte, melding wordt gemaakt van een onderhandsche akte of van een buitenslands verleden akte vallende in de termen van artikel 19,
2° of 3°, moet die authentieke akte afschrift van de vermelding der registratie van bedoelde akte bevatten.

Indien die akte niet geregistreerd werd, dan wordt daarvan in de authentieke akte melding gemaakt.

Alle overtreding van dit artikel wordt gestraft met een boete van 25 EUR ten laste van den werkenden ambtenaar of openbaren officier.

###### Art. 170bis

(van toepassing vanaf 01.01.2002)

(ingevoegd bij art. 6 van de wet van 07.03.2002 (B.S., 19.03.2002). Tekst van toepassing vanaf 01.01.2002 (art. 7)) In geval van een schenking moet de notaris in de akte een verklaring van de schenker opnemen die vermelding inhoudt van het adres en de datum en duur van de vestiging van de verschillende fiscale woonplaatsen die de schenker gehad heeft in de periode van vijf jaar voorafgaand van de datum van de schenking.

In geval van weigering de verklaring te doen of bij onjuiste of onvolledige verklaring verbeurt de schenker een boete ten bijdrage van tweemaal de aanvullende rechten.

De notaris die nagelaten heeft de schenker te vragen de verklaring te doen, verbeurt een boete van 25 EUR.

###### Art. 171

(van toepassing vanaf 17.08.2020)

(aangevuld bij art. 112 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))

Alle expedities, afschriften van of uittreksels uit een burgerlijke of gerechtelijke authentieke akte die aan de formaliteit onderworpen is of die in artikel 8bis bedoeld is, moeten, op straf van een boete van 25 EUR, een afschrift van de vermelding van de registratie of van de vermelding voorzien in het tweede lid van artikel 8 bevatten.

Het eerste lid is niet van toepassing op een afschrift gemaakt met het oog op de aanbieding ervan ter formaliteit van de registratie.

#### Afdeling II - Voorschriften betreffende het uitreiken van uitgiften

###### Art. 172

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Notarissen, gerechtsdeurwaarders, griffiers der hoven en rechtbanken en bestuurlijke overheden mogen; vóór het nakomen van de formaliteit der registratie, de akten welke zij verplicht zijn te doen registreren of waarvan de rechten in hun handen moeten worden geconsigneerd, niet in brevet, uitgifte, afschrift of uittreksel uitreiken, zelfs zo de voor de registratie gestelde termijn niet verstreken is.

Alle overtreding van dit verbod wordt met een geldboete van 25 EUR gestraft.

###### Art. 173

(van toepassing vanaf 17.08.2020)

(7°bis, ingevoegd bij art. 113 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -)) Van voorgaand artikel wordt afgeweken ten aanzien van:

1° De uitgiften van akten, verleden voor notarissen of bestuurlijke overheden, die aanleiding geven tot een hypothecaire formaliteit waarbij de bedoelde uitgiften eerst aan de betrokken partijen mogen worden afgegeven nadat zij, overeenkomstig artikel 171 zijn aangevuld, met een afschrift van de vermelding van de registratie of met de in artikel 8, tweede lid, voorgeschreven vermelding;

1°bis De uitgiften en uittreksel van akten, verleden voor notarissen, die aanleiding geven tot neerlegging ter griffie van de ondernemingsrechtbank overeenkomstig artikel 2:12 van het Wetboek van vennootschappen en verenigingen;

1°ter de uitgiften en uittreksels van akten, verleden voor notarissen, die worden uitgereikt met als enig doel de inschrijving van een onderneming bij een ondernemingsloket, op voorwaarde dat dit uitdrukkelijk vermeld wordt op de uitgifte of het uittreksel;

2° Afschriften welke vereist zijn voor de betekening van exploten en van andere soortgelijke akten;

3° Niet ondertekende afschriften van vonnissen en arresten;

4° Vonnissen en arresten die, met het oog op de dringende noodzakelijkheid, op de minuut en vóór de registratie uitvoerbaar verklaard worden;

5° Voor eensluidend verklaarde afschriften van vonnissen en arresten slechts afgeleverd ten einde de verhaalstermijnen te doen lopen. Die afschriften moeten vermelding van hun bijzondere bestemming dragen en mogen tot geen andere doeleinden worden gebruikt;

6° Uitgiften van vonnissen en arresten die worden uitgereikt aan het openbaar ministerie, alsmede uitgiften, afschriften of uittreksels die in strafzaken worden uitgereikt aan de Rijksagenten welke belast zijn met de tenuitvoerlegging van vonnissen en arresten;

7° Afschriften waarvan de aflevering wegens hoogdringendheid werd bevolen door de voorzitter van de rechtbank van eerste aanleg;

7°bis de afschriften van de vonnissen en arresten gemaakt met het oog op de aanbieding ervan ter formaliteit van de registratie;

8° de gedematerialiseerde afschriften van notariële akten, die worden neergelegd in de Notariële Aktebank overeenkomstig artikel 18 van de wet van 25 ventôse jaar XI op het notarisambt.

###### Art. 174

(van toepassing vanaf 01.11.1986)

(opgeheven bij art. 13 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst van toepassing vanaf 01.11.1986 (art. 15)) (…)

###### Art. 175

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 17 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling III - Repertorium van de akten

###### Art. 176

(van toepassing vanaf 28.09.1963)

(gewijzigd bij art. 48, § 4 van de wet van 05.07.1963 (B.S., 17.07.1963). Tekst van toepassing vanaf 28.09.1963 (art. 52))

Notarissen en gerechtsdeurwaarders moeten een kolomsgewijze ingedeeld repertorium houden, waarin zij dagelijks zonder openlaten van tussenruimte, noch tussenregel, noch vervalsing en in de volgorde der nummers, alle akten van hun ambt inschrijven.

###### Art. 177

(van toepassing vanaf 10.01.2014)

(gewijzigd bij art. 53 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87,
1°))

In elk artikel van het repertorium dienen vermeld:

1° volgnummer;

2° datum en aard van de akte;

3° naam, voornamen, woonplaats en identificatienummer of ondernemingsnummer bedoeld in artikel 2, vierde lid, van de partijen;

4° bondige aanduiding der onroerende goederen;

5° vermelding van de registratie;

6° wat aangaat de gerechtsdeurwaarders, de kosten van hun akten en exploten na aftrek van hun verschotten.
De Koning kan aanvullende vermeldingen voorschrijven of afwijkingen toestaan.

###### Art. 178

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Een boete van 25 EUR wordt verbeurd voor elke weggelaten of te laat in het repertorium ingeschreven akte, voor elke akte ingeschreven met tussenregel of met vervalsing, alsmede voor elke akte van vroegere datum dan die van het proces-verbaal van nummering en waarmerk van het repertorium.

###### Art. 179

(van toepassing vanaf 10.01.2010)

(vervangen bij art. 82 van de wet van 22.12.2009 (B.S., 31.12.2009 - ed. 2). Tekst van toepassing vanaf 10.01.2010 (art. -))

De in artikel 176 bedoelde repertoria die moeten worden gehouden door de notarissen, mogen overeenkomstig artikel 29 van de wet van 16 maart 1803 tot regeling van het notarisambt hetzij op papier, hetzij op een gedematerialiseerde wijze die is vastgesteld door de Nationale Kamer van notarissen in een door de Koning goedgekeurd reglement, worden gehouden.

De Koning kan bepalen dat de repertoria die door de gerechtsdeurwaarders moeten worden gehouden, mogen worden gehouden op een gedematerialiseerde wijze die vastgesteld is door de Nationale Kamer van gerechtsdeurwaarders in een door de Koning goedgekeurd reglement.

###### Art. 180

(van toepassing vanaf 01.04.2014)

(gewijzigd bij art. 54 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2). Tekst van toepassing vanaf 01.04.2014 (art. 87,
3°))

De in artikel 176 aangeduide personen zijn er toe gehouden, om de drie maand, hun repertorium voor te leggen aan de ontvanger van het kantoor aangeduid in artikel 39, 1°, eerste lid, die het viseert en in zijn visum het aantal ingeschreven akten vermeldt.

Deze voorlegging geschiedt binnen de eerste tien dagen van de maanden januari, april, juli en oktober van elk jaar.

De Koning kan voor de op gedematerialiseerde wijze gehouden repertoria bijzondere regels vaststellen wat de modaliteiten van de voorlegging en het visum van het repertorium betreft.
Bij laattijdige voorlegging van het repertorium wordt een boete verbeurd van 25 euro per week vertraging.

###### Art. 180bis

(van toepassing vanaf 09.03.2026)

(lid 1, gewijzigd bij art. 24 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Een kopie van de geregistreerde uitgifte en van de geregistreerde bijlagen wordt, samen met de vermelding van de registratie, gedurende twintig jaar bewaard door de instrumenterende notaris.

Indien de akte op gedematerialiseerde wijze ter registratie aangeboden werd, gebeurt deze bewaring door de Koninklijke Federatie van het Belgisch Notariaat of haar gedelegeerde, voor rekening van de notaris.

Die bewaring geschiedt:

1° voor de akten die zijn opgenomen in de Notariële Aktebank, bedoeld in artikel 18 van de wet van 25 ventôse jaar XI op het notarisambt, door die Notariële Aktebank;

2° voor de andere akten, door de Koninklijke Federatie van het Belgisch Notariaat of haar gedelegeerde, op elektronische wijze, voor rekening van de notaris.

De bewaring moet de onveranderlijkheid en de integriteit van de inhoud van deze stukken waarborgen.

###### Art. 180ter

(van toepassing vanaf 17.08.2020)

(ingevoegd bij art. 114 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))

De griffier bewaart, samen met de minuut van het vonnis of arrest:

1° de vermelding van de registratie van dat vonnis of arrest;

2° een kopie van het geregistreerde afschrift van dat vonnis of arrest.

#### Afdeling IV - Verplichting van inzageverlening

###### Art. 1811

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 55 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -)) Notarissen, gerechtsdeurwaarders, bestuursoverheden en ambtenaren van de Staat, provincies, gemeenten en openbare instellingen zijn ertoe gehouden, op verbeurte van een boete van 25 EUR per overtreding, op elk verzoek van de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie, van hun repertoriums en de akten waarvan zij bewaarders zijn, evenals van de uitgiften en relazen bedoeld in artikel 180bis, zonder verplaatsing inzage te verlenen en deze ambtenaren de inlichtingen, af schriften en uittreksels te laten nemen die zij nodig hebben met het oog op 's Rijks belangen.

Deze verplichting is echter, bij 't leven van de erflaters, niet toepasselijk op de bij notarissen berustende testamenten.

###### Art. 1812

(van toepassing vanaf 17.08.2020)

(gewijzigd bij art. 115 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))

De griffiers van de hoven en rechtbanken zijn er toe gehouden op straf van een boete van vijfentwintig euro per overtreding, aan de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie inzage te verlenen van:

1° de door hen of vóór hen verleden akten;

2° de minuten van de vonnissen, arresten, bevelschriften en alle andere akten waarvan zij bewaarders zijn;

3° de afschriften en vermeldingen bedoeld in artikel 180ter.

De modaliteiten waaronder deze inzage moet verleend worden en de termijn waarbinnen dit moet geschieden, worden bij koninklijk besluit bepaald. Inbreuken op de voorschriften van dit koninklijk besluit kunnen beteugeld worden met boeten waarvan het bedrag 25 EUR per inbreuk niet zal te boven gaan.

###### Art. 182

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 57 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

De personen die de in artikel 631 bedoelde beroepsaangifte ondertekenen zijn ertoe gehouden van hun registers, repertoria, boeken, akten en alle andere bescheiden betreffende hun handels-, beroeps- of statutaire bedrijvigheid, bij iedere vordering van de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie, zonder verplaatsing inzage te verlenen, ten einde bedoelde ambtenaren te laten nagaan of de door hen of door derden verschuldigde registratierechten wel richting werden geheven.

Elke weigering van inzageverlening wordt bij proces-verbaal vastgesteld en gestraft met een geldboete van 250 tot 2.500 EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie wordt bepaald.

###### Art. 182bis

(van toepassing vanaf 01.01.2017)

(gewijzigd bij art. 20, § 2, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 – ed. 3). Tekst van toepassing vanaf 01.01.2017 (art. 40, § 4))

De personen die de toepassing van artikel 140bis (1) vragen, zijn er toe gehouden, zonder verplaatsing, van alle boeken en bescheiden betreffende hun activiteit bij iedere vordering van de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie inzage te verlenen teneinde bedoelde ambtenaren toe te laten zich te vergewissen van de juiste heffing van de door de verzoekers of derden verschuldigde rechten.

Elke weigering van inzageverlening wordt bij proces-verbaal vastgesteld en wordt gestraft met een geldboete van 1250 EUR.
(1) Volgens art. 20, § 2, van de ordonnantie van 12.12.2016 (B.S., 29.12.2016 - ed. 3): « Elke vermelding van 140bis in het

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 183

(van toepassing vanaf 01.01.2028)

(gewijzigd bij art. 67 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Openbare instellingen, stichtingen van openbaar nut en private stichtingen, alle verenigingen en vennootschappen die in België hun hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben, bankiers, wisselagenten en wisselagentcorrespondenten, zaakwaarnemers en aannemers, openbare of ministeriële officieren zijn ertoe gehouden aan de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie, met desvoorkomend inzageverlening van de stukken tot staving, al de inlichtingen te verstrekken welke deze nodig achten om de correcte heffing van de te hunnen laste of ten laste van derden invorderbare rechten te verzekeren.

Deze inlichtingen kunnen slechts gevraagd worden krachtens bijzondere machtiging van de administrateurgeneraal van de Algemene Administratie van de Patrimoniumdocumentatie, houdende nauwkeurige aanduiding van het rechtsfeit omtrent hetwelk navorsing dient gedaan.

De inlichtingen moeten worden verschaft binnen drie maanden na de datum waarop ze werden gevraagd. Die termijn kan worden verlengd door de ambtenaar aangewezen in de machtiging bedoeld in het tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500 EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie wordt vastgesteld.

###### Art. 183

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 58 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

Openbare instellingen, stichtingen van openbaar nut en private stichtingen, alle verenigingen en vennootschappen die in België hun hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben, bankiers, wisselagenten en wisselagentcorrespondenten, zaakwaarnemers en aannemers, openbare of ministeriële officieren zijn ertoe gehouden aan de ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie, met desvoorkomend inzageverlening van de stukken tot staving, al de inlichtingen te verstrekken welke deze van node achten om de richtige heffing van de te hunnen laste of ten laste van derden invorderbare rechten te verzekeren.

Deze inlichtingen kunnen slechts gevraagd worden krachtens bijzondere machtiging van den administrateurgeneraal van de Algemene Administratie van de Patrimoniumdocumentatie, houdende nauwkeurige aanduiding van het rechtsfeit omtrent hetwelk navorsing dient gedaan.

De inlichtingen moeten worden verschaft binnen drie maanden na de datum waarop ze werden gevraagd. Die termijn kan worden verlengd door de ambtenaar aangewezen in de machtiging bedoeld in het tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500 EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie wordt vastgesteld.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 184

(van toepassing vanaf 01.01.2028)

(lid 2, vervangen bij art. 68 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Wanneer de som te betalen door de eigenaar van een muur om deze gemeen te maken, door tussenkomst van een deskundige, bouwkundige, aannemer, landmeter of landmeetkundige werd bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25 EUR, de bevoegde ambtenaar van de Algemene Administratie van de Patrimoniumdocumentatie daarvan bericht te geven binnen de drie maanden na de voltooiing van zijn werk.

De Koning bepaalt de modaliteiten van deze communicatie en duidt de ambtenaar aan ertoe bevoegd hetzelve te ontvangen.

###### Art. 184

(van toepassing vanaf 16.05.2014)

(gewijzigd bij art. 68 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van toepassing vanaf 16.05.2014 (art. 99))

Wanneer de som te betalen door de eigenaar van een muur om deze gemeen te maken, door tussenkomst van een deskundige, bouwkundige, aannemer, landmeter of landmeetkundige werd bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25 EUR, de bevoegde ambtenaar van de Algemene Administratie van de Patrimoniumdocumentatie daarvan bericht te geven binnen de drie maanden na de voltooiing van zijn werk.

Een koninklijk besluit bepaalt de wijze waarop dit bericht dient gegeven en duidt de ambtenaar aan ertoe bevoegd hetzelve te ontvangen.

#### Afdeling V - Verplichtingen opgelegd aan openbare ambtenaren ter verzekering van de invordering der registratierechten

###### Art. 184bis

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 93 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

De notarissen, gerechtsdeurwaarders en griffiers, de vereffenaars en curatoren alsook de ambtenaren van de Deposito- en Consignatiekas mogen slechts de betaling, overschrijving of teruggave van sommen of waarden die voortkomen van een veroordeling, van een vereffening of van een rangregeling, verrichten na de aflevering, door de ontvanger, van een getuigschrift houdende verklaring dat geen enkele som eisbaar blijft als registratierecht of als boete uit hoofde van die veroordeling, vereffening of rangregeling.

Het eerste lid is slechts van toepassing op de vereffenaars en de curators in het geval dat de veroordeling, de vereffening of rangregeling die de betaling, overschrijving, of teruggave tot gevolg heeft, hen ter kennis wordt gebracht.

Indien de personen bepaald in het eerste lid de voorschriften van dit artikel niet zijn nagekomen, zijn zij persoonlijk aansprakelijk voor de betaling van de sommen die opeisbaar blijven.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Art. 185

(van toepassing vanaf 01.01.2028)

(lid 2, vervangen bij art. 69 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze titel, wordt het bestuur er toe gemachtigd volgens de regelen en door alle middelen van gemeen recht, met inbegrip van getuigen en vermoedens, maar met uitzondering van de eed, en, bovendien door de processen-verbaal van zijn ambtenaren, elke overtreding van de beschikkingen van deze titel vast te stellen en om het even welk feit te bewijzen dat de opvorderbaarheid van een recht of een boete laat blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.

De processen-verbaal gelden als bewijs tot het tegendeel bewezen is. Zij zullen aan belanghebbenden betekend worden binnen de maand van de vaststelling van de overtreding. Deze betekening gebeurt met een aangetekende zending.

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Art. 185

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 59 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze titel, wordt het bestuur er toe gemachtigd volgens de regelen en door alle middelen van gemeen recht, met inbegrip van getuigen en vermoedens, maar met uitzondering van de eed, en, bovendien door de processen-verbaal van zijn ambtenaren, elke overtreding van de beschikkingen van deze titel vast te stellen en om het even welk feit te bewijzen dat de opvorderbaarheid van een recht of een boete laat blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.

De processen-verbaal gelden als bewijs tot het tegendeel bewezen is. Zij zullen aan belanghebbenden betekend worden binnen de maand van de vaststelling van de overtreding. Deze betekening mag gebeuren bij een ter post aangetekend schrijven. De afgifte van het stuk ter post geldt als betekening van de volgende dag af.

###### Art. 186

(van toepassing vanaf 27.09.1947)

(opgeheven bij art. 11 van de wet van 13.08.1947 (B.S., 17.09.1947). Tekst van toepassing vanaf 27.09.1947 (art. -)) (…)

###### Art. 187

(van toepassing vanaf 01.02.1940)

Verandering in eigendom of vruchtgebruik van een in België gelegen onroerend goed, ten gevolge van een overdragende of aanwijzende overeenkomst, wordt, ter vordering van het recht tegen de nieuwe eigenaar of vruchtgebruiker, in voldoende mate bewezen door daden van beschikking of van bestuur of door andere handelingen of akten waarbij, in zijnen hoofde, de eigendom of het vruchtgebruik vastgesteld of ondersteld wordt.

###### Art. 188

(van toepassing vanaf 01.02.1940)

Wordt als koper voor eigen rekening beschouwd en mag zich op de hoedanigheid van lasthebber of van commissionair van de verkoper niet beroepen, ieder persoon die de verkoop van een onroerend goed bewerkt, wanneer vaststaat dat hij, reeds vóór het tot stand brengen van deze verkoop, aan de eigenaar den prijs of elke van den verkoop voort te komen som betaald heeft of er zich toe verbonden heeft te betalen.

De tussenpersoon wordt geacht het onroerend goed te hebben verkregen op de dag van de betaling of van de verbintenis tot betaling.

#### Afdeling II - Controleschatting

###### Art. 189

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 94 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Onverminderd de toepassing van de bepalingen betreffende het bewimpelen van prijs, heeft de ontvanger de bevoegdheid om schatting te vorderen van de goederen die het voorwerp van de overeenkomst uitmaken, ten einde van de ontoereikendheid van de uitgedrukte prijs of van de aangegeven waarde te doen blijken, wanneer het gaat om eigendom of vruchtgebruik van in België gelegen onroerende goederen.

###### Art. 190

(van toepassing vanaf 31.07.1960)

(lid 3 opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van toepassing vanaf 31.07.1960 (art. -)) De schatting dient gevorderd bij een aanvraag genotificeerd door den ontvanger aan de verkrijgende partij binnen twee jaar te rekenen van de dag van de registratie van de akte of verklaring.

In de gevallen bedoeld in artikelen 16 en 17 gaat de termijn slechts in den dag der registratie van de in artikel 31,
2°, voorziene verklaring.

De vordering tot schatting houdt aanwijzing van de goederen waarover de schatting gaat, zomede van de som waarop zij door het bestuur geschat werden en van het vermoedelijk wegens recht en boete verschuldigd bedrag.

###### Art. 191

(van toepassing vanaf 01.02.1940)

Binnen vijftien dagen na de in artikel 190 voorziene notificatie, kunnen ontvanger en partij overeenkomen dat de waardering door één of door drie door hen gekozen deskundigen zal worden gedaan.

In dit geval wordt het akkoord vastgesteld bij een proces-verbaal dat het voorwerp der schatting vermeldt en den of de verkozen deskundigen aanwijst.

Dit proces-verbaal is gedagtekend; het wordt door de ontvanger en door de partij ondertekend; indien de partij niet mag of niet kan ondertekenen, dient dit in het proces-verbaal vermeld.

###### Art. 192

(van toepassing vanaf 01.02.1940)

Bij gemis van het onder artikel 191 voorzien akkoord richt de ontvanger, aan den vrederechter in wiens ambtsgebied de onroerende goederen gelegen zijn, een verzoekschrift waarin de feiten worden uiteengezet en dat de vordering tot schatting inhoudt. Wanneer de onroerende goederen in het ambtsgebied van verschillende vredegerechten gelegen zijn, is de bevoegde rechter hij in wiens ambtsgebied zich het gedeelte der goederen bevindt met het grootste kadastraal inkomen.

Het verzoekschrift wordt aan de partij betekend.

De rechter beslist binnen vijftien dagen na het verzoek; hij beveelt de schatting en stelt, naar vereiste van omstandigheden, een of drie deskundigen aan.

###### Art. 193

(van toepassing vanaf 16.05.2014)

(gewijzigd bij art. 69 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van toepassing vanaf 16.05.2014 (art. 99))

Kunnen niet tot deskundigen gekozen of benoemd worden:
1° ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie;

2° openbare of ministeriële officieren opstellers van de akten of verklaringen;

3° beambten van bedoelde ambtenaren en openbare of ministeriële officieren.

###### Art. 194

(van toepassing vanaf 01.01.1969)

(gewijzigd bij art. 3/art. 119 van de wet van 10.10.1967 (B.S., 31.10.1967). Tekst van toepassing vanaf 01.01.1969 (art. 1, KB van 04.11.1968 (B.S., 13.11.1968)))

Het vonnis waarbij de schatting wordt bevolen, wordt ten verzoeke van de ontvanger aan de partij betekend.

De ontvanger of de partij, indien zij gegronde redenen hebben om de bevoegdheid, onafhankelijkheid of onpartijdigheid van de benoemde deskundigen in twijfel te trekken, mogen, binnen acht dagen na bedoelde betekening, deszelfs of derzelver wraking bij de rechter vorderen. Deze wraking mag altijd worden gevorderd in de gevallen beoogd door artikel 966 van het Gerechtelijk Wetboek.

De vordering tot wraking geschiedt per rekest waarin de oorzaken der wraking nader worden bepaald. De rechter beslist na de belanghebbenden te hebben gehoord. Bij hetzelfde vonnis vervangt hij de gewraakte deskundigen.

Deze nieuwe beslissing wordt aan de partij betekend.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 195

(van toepassing vanaf 01.01.2028)

(gewijzigd bij art. 70 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De ontvanger notificeert aan de deskundigen de opdracht die hun toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de deskundigen, zowel aan de ontvanger als aan de partij, een briefwisseling waarbij zij hen verwittigen van dag en uur waarop zij de nodig geachte bezoeken ter plaatse zullen doen en hen in hun gezegden en opmerkingen zullen aanhoren.

Ieder aan de deskundigen door een der partijen ter inzage verleend bescheid moet tezelfdertijd in afschrift aan de andere partij bij aangetekende zending worden gezonden.

###### Art. 195

(van toepassing vanaf 01.02.1940)

De ontvanger notificeert aan de deskundigen de opdracht die hun toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de deskundigen, zowel aan de ontvanger als aan de partij, een schrijven waarbij zij hen verwittigen van dag en uur waarop zij de nodig geachte bezoeken ter plaatse zullen doen en hen in hun gezegden en opmerkingen zullen aanhoren.

Ieder aan de deskundigen door een der partijen ter inzage verleend bescheid moet tezelfdertijd in afschrift aan de andere partij bij aangetekende brief worden gezonden.

###### Art. 196

(van toepassing vanaf 16.07.1973)

(lid 3 vervangen bij art. 7 van de wet van 27.05.1974 (B.S., 06.07.1974) err. (B.S. 12.07.1974 en 21.12.1974). Tekst van toepassing vanaf 16.07.1973 (art. -))

De deskundige of, desvoorkomend, de drie gezamenlijke optredende deskundigen vorsen den staat en de verkoopwaarde der in de vordering tot schatting aangewezen goederen, op het er vermeld tijdstip.

Zij maken, uiterlijk binnen drie maanden te rekenen van bij eerste alinea van artikel 195 voorziene notificatie, één enkel verslag op, dat gedagtekend en ondertekend wordt, en waarin zij op beredeneerde wijze en met bewijsgronden tot staving, zonder enige beperking noch voorbehoud, hun advies over bedoelde waarde uitbrengen.

De handtekening van de deskundige wordt voorafgaan door de eed:

"Ik zweer dat ik in eer en geweten, nauwgezet en eerlijk mijn opdracht heb vervuld".

of:

"Je jure que j'ai rempli ma mission en honneur et conscience, avec exactitude et probité".

of:

"Ich schwöre, dass ich den mir erteilten Auftrag auf Ehre und Gewissen, genau und ehrlich erfüllt habe".

De minuut van het verslag wordt ter griffie van het onder artikel 192 aangeduid vredegerecht neergelegd.

###### Art. 197

(van toepassing vanaf 01.02.1940)

Het verslag wordt door de meest gerede partij gelicht en aan de andere partij betekend.
Naar de door de deskundigen gegeven waardering en, in geval van niet-overeenstemming, naar de waardering van de meerderheid of, bij gemis van meerderheid, naar de tussenwaardering, wordt de verkoopwaarde van het goed ten opzichte van de heffing der belasting bepaald.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 198

(van toepassing vanaf 01.01.2028)

(vervangen bij art. 71 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De krachtens voorgaande artikelen van deze afdeling te verrichten betekeningen en notificaties geschieden bij aangetekende zending.

###### Art. 198

(van toepassing vanaf 01.02.1940 tot 31.12.2024)

De krachtens vorenstaande artikelen van deze afdeling te verrichten betekeningen en notificaties mogen bij aangetekend schrijven geschieden. De afgifte van het stuk ter post geldt als notificatie vanaf de daaropvolgende dag.

###### Art. 199

(van toepassing vanaf 25.07.2004)

(vervangen bij art. 33 door de programmawet van 09.07.2004 (B.S., 15.07.2004 - ed. 2). Tekst van toepassing vanaf 25.07.2004 (art. -))

Zowel de ontvanger als de partij kunnen de schatting betwisten door inleiding van een rechtsvordering. Deze rechtsvordering dient ingeleid te worden, op straffe van verval, binnen de termijn van één maand te rekenen van de betekening van het verslag.

###### Art. 200

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 181 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Indien de opgegeven prijs of de aangegeven waarde lager is dan de door de schatting opgeleverde begroting, moet de verkrijger het bijkomend recht betalen, met de moratoire intresten naar de in burgerlijke zaken vastgestelde voet, te rekenen van de bij artikel 190 voorziene notificatie en, desvoorkomend, met de bij artikel 201 opgelegde boete.

Hem worden desvoorkomend ook de kosten van de procedure opgelegd, indien het vastgestelde tekort het achtste van de uitgedrukte prijs of van de aangegeven waarde bereikt of overtreft.

Deze kosten blijven evenwel ten laste van 's Rijks Schatkist zo de belanghebbende, vóór de in artikel 190 voorziene notificatie, heeft aangeboden het bijkomend recht, verhoogd met de boete bepaald in artikel 201 te betalen, op een som welke het bij de schatting uitgewezen tekort bereikt of overtreft.

De invordering geschiedt bij dwangschrift, zoals aangewezen in artikel 220.

### HOOFDSTUK XI - Tekort in de waardering, bewimpeling en veinzing. Sanctiën

###### Art. 201

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 182 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Wanneer bevonden wordt dat de opgegeven prijs of de aangegeven waarde van aan de onder artikel 189 voorziene schatting onderworpen goederen te laag is, en dat het vastgestelde tekort gelijk is aan of hoger dan het achtste van de opgegeven prijs of van de aangegeven waarde, verbeurt de verkrijgende partij een geldboete ten bedrage van het ontdoken recht.

###### Art. 202

(van toepassing vanaf 17.01.1959)

(gewijzigd bij art. 15 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Wanneer er geen aanleiding tot schatting bestaat en een waardering, gedaan om de vereffening van de rechten mogelijk te maken, ontoereikend wordt erkend, is het ontdoken recht ondeelbaar verschuldigd door hen die de waardering hebben gedaan; zij zijn daarenboven ondeelbaar een boete verschuldigd gelijk aan het aanvullend recht, zoo het tekort gelijk is aan of hoger is dan het achtste van bewuste waardering.

Alle andere onjuistheid, bevonden in de elementen van een verklaring in of onderaan de akte gesteld tot vereffening van de belasting, wordt gestraft met een boete gelijk aan het ontdoken recht, benevens betaling van dat recht, het al ondeelbaar ten laste van hen die de verklaring gedaan hebben.

###### Art. 203

(van toepassing vanaf 24.07.2025)
(lid 1, gewijzigd bij art. 8 van de ordonnantie van 17.07.2025 (B.S., 24.07.2025). Tekst van toepassing de dag waarop het in het B.S. bekendgemaakt wordt, zijnde 24.07.2025 (art. 15))

In geval van bewimpeling aangaande prijs en lasten overeengekomen waarde, is elke der contracterende partijen die aan de overtreding heeft deelgenomen een boete verschuldigd gelijk aan het ontdoken recht. Dit recht ondeelbaar verschuldigd door alle partijen die aan de overtreding hebben deelgenomen.

Het aanvullend recht dat ingevolge een bij schatting vastgesteld tekort of anderszins betaald geworden is, wordt aangerekend op het aanvullend recht, vereffend uit hoofde van de bewimpeling waarvan sprake in vorenstaande alinea.

In alle gevallen waarin de heffing op den prijs en de lasten op de overeengekomen waarde geschiedt, moet de werkende notaris den verschijnende partijen de eerste alinea van dit artikel voorlezen.

Op straf van een boete van 25 EUR moet uitdrukkelijke melding van die voorlezing in de akte gemaakt worden.

###### Art. 204

(van toepassing vanaf 04.05.1965)

(gewijzigd bij art. 18 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

Wanneer de in een akte vastgestelde overeenkomst niet die is welke door de partijen werd gesloten, of wanneer de akte betreffende een in artikel 19, 2° of 5°, bedoelde overeenkomst onvolledig of onjuist is, met dien verstande dat ze al de bestanddelen van de overeenkomst niet doet kennen, is elke der contracterende partijen een geldboete verschuldigd gelijk aan het ontdoken recht. Dit recht is ondeelbaar door alle partijen verschuldigd.

###### Art. 205

(van toepassing vanaf 06.04.1999)

(opgeheven bij art. 64 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van toepassing vanaf 06.04.1999 (art. -))

(…)

### HOOFDSTUK XII - Correctionele straffen

###### Art. 206

(van toepassing vanaf 01.07.2017)

(aangevuld bij art. 10 van de ordonnantie van 13.07.2017 (B.S., 18.07.2017). Tekst van toepassing vanaf 01.07.2017 (art. 17)) Onverminderd de fiscale boeten, wordt hij die met bedrieglijk opzet of met het oogmerk om te schaden, de bepalingen van dit Wetboek of de ter uitvoering ervan genomen besluiten overtreedt, gestraft met gevangenisstraf van acht dagen tot twee jaar en met geldboete van 250 EUR tot 12.500 EUR of met één van die straffen alleen.

Wanneer de overtreding werd begaan in het kader van een registratierecht dat geen gewestelijke belasting is volgens het bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de gemeenschappen en de gewesten, wordt het bedrag van het in het eerste lid bepaalde maximum van de boete gebracht op 500.000 euro.

Wanneer de overtreding werd begaan in het kader van een registratierecht dat een gewestelijke belasting is in de zin van artikel 3, eerste lid, 6° tot 8° van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten, wordt het bedrag van het in het eerste lid bepaalde maximum van de boete gebracht op 500.000 euro in geval van overtreding van de regels voor deze belastingen met uitzondering van die met betrekking tot de procedureregels.

###### Art. 206bis

(van toepassing vanaf 01.07.2017)

(aangevuld bij art. 11 van de ordonnantie van 13.07.2017 (B.S., 18.07.2017). Tekst van toepassing vanaf 01.07.2017 (art. 17))

Met gevangenisstraf van een maand tot vijf jaar en met geldboete van 250 tot 12.500 EUR of met één van die straffen alleen frank wordt gestraft, hij die, met het oogmerk om een van de in artikel 206 bedoelde misdrijven te plegen, in openbare geschriften, in handelsgeschriften of in private geschriften valsheid pleegt, of die van een zodanig vals geschrift gebruik maakt.

Hij die wetens en willens een vals getuigschrift opstelt dat de belangen van de Schatkist kan schaden of die van een dergelijk getuigschrift gebruik maakt, wordt gestraft met gevangenisstraf van acht dagen tot twee jaar en met geldboete van 250 tot 12.500 EUR of met één van die straffen alleen.

Wanneer het misdrijf werd begaan in het kader van een registratierecht dat geen gewestelijke belasting is volgens het bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de gemeenschappen en de gewesten, wordt het bedrag van het in het eerste en het tweede lid bepaalde maximum van de boete gebracht op 500.000 euro.

Wanneer de overtreding werd begaan in het kader van een registratierecht dat een gewestelijke belasting is in de zin van artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten, wordt het bedrag van het in het eerste en het tweede lid bepaalde maximum van de boete gebracht op 500.000 euro in geval van overtreding van de regels voor deze belastingen met uitzondering van die met betrekking tot de procedureregels.

###### Art. 206bis/1

(van toepassing vanaf 01.01.2020)

(ingevoegd bij art. 109 van de wet van 05.05.2019 (B.S., 24.05.2019 – ed. 1). Tekst van toepassing op de datum bepaald door de Koning en ten laatste op 01.01.2020 (art. 200)) Wanneer de overtreding werd begaan in het kader van een registratierecht dat geen gewestelijke belasting is volgens het bepaalde in artikel 3, eerste lid, 6° tot 8° van de bijzondere wet van 16 januari 1989 betreffende de financiering van de gemeenschappen en de gewesten en teneinde te vermijden dat een veroordeelde aan een onredelijk zware straf zou worden onderworpen, houdt de rechter bij de straftoemeting rekening met de verschuldigde fiscale boeten.

Artikel 42, 3°, van het Strafwetboek vindt geen toepassing op de vermogensvoordelen die rechtstreeks uit de fiscale misdrijven zijn verkregen, op de goederen en waarden die in de plaats ervan zijn gesteld en op de inkomsten uit de belegde voordelen in geval de vordering van de fiscale administratie gegrond wordt verklaard en tot een effectieve betaling van deze volledige vordering heeft geleid.

###### Art. 207

(van toepassing vanaf 14.02.1981)

(vervangen bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van toepassing vanaf 14.02.1981 (art. 22))

§ 1. Wanneer de beoefenaar van een van de volgende beroepen:

1° belastingadviseur;

2° zaakbezorger;

3° deskundige in belastingzaken of in boekhouden;

4° of enig ander beroep dat tot doel heeft voor een of meer belastingplichtigen boek te houden of te helpen houden, ofwel voor eigen rekening ofwel als hoofd, lid of bediende van enigerlei vennootschap, vereniging, groepering of onderneming;

5° of, meer in het algemeen, het beroep dat erin bestaat een of meer belastingsplichtigen raad te geven of bij te staan bij het vervullen van de verplichtingen opgelegd bij dit Wetboek of bij de ter uitvoering ervan vastgestelde besluiten, wordt veroordeeld wegens een van de misdrijven bedoeld in de artikelen 206 en 206bis, kan het vonnis hem verbod opleggen om gedurende drie maanden tot vijf jaar, rechtstreeks of onrechtstreeks, de hiervoren bedoelde beroepen op welke wijze ook uit te oefenen.

De rechter kan bovendien, mits hij zijn beslissing op dat stuk motiveert, voor een duur van drie maanden tot vijf jaar de sluiting bevelen van de inrichtingen van de vennootschap, vereniging, groepering of onderneming waarvan de veroordeelde hoofd, lid of bediende is.

§ 2. Het verbod en de sluiting bedoeld in § 1 treden in werking vanaf de dag waarop de veroordeling in kracht van gewijsde is gegaan.

###### Art. 207bis

(van toepassing vanaf 01.07.2017)
(aangevuld bij art. 12 van de ordonnantie van 13.07.2017 (B.S., 18.07.2017). Tekst van toepassing vanaf 01.07.2017 (art. 17))

Hij die, rechtstreeks of onrechtstreeks, het verbod of de sluiting uitgesproken krachtens artikel 207 overtreedt, wordt gestraft met gevangenisstraf van acht dagen tot twee jaar en geldboete van 250 EUR tot 12.500 EUR of met één van die straffen alleen.

Wanneer het verbod werd opgelegd in het kader van een registratierecht dat geen gewestelijke belasting is volgens het bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de gemeenschappen en de gewesten, wordt het bedrag van het in het eerste lid bepaalde maximum van de boete gebracht op 500.000 euro.

Wanneer het verbod werd geschonden in het kader van een registratierecht dat een gewestelijke belasting is in de zin van artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van 16 januari 1989 betreffende de financiering van de Gemeenschappen en de Gewesten, wordt het bedrag van het in het eerste lid bepaalde maximum van de boete gebracht op 500.000 euro in geval van overtreding van de verboden in het kader van deze belastingen met uitzondering van die met betrekking tot de procedureregels.

###### Art. 207ter

(van toepassing vanaf 01.11.2012)

(gewijzigd bij art. 25 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van toepassing vanaf 01.11.2012 (art. -))

§ 1. Alle bepalingen van het Eerste Boek van het Strafwetboek, met inbegrip van artikel 85, zijn van toepassing op de misdrijven bedoeld in de artikelen 206, 206bis en 207bis.

§ 2. (…)

§ 3. De wet van 5 maart 1952, gewijzigd bij de wetten van 22 december 1969 en 25 juni 1975, betreffende de opdecimes op de strafrechtelijke geldboeten, is van toepassing op de misdrijven bedoeld in artikel 206, 206bis en 207bis.

###### Art. 207quater

(van toepassing vanaf 28.04.2024)

(lid 2, 2°, gewijzigd bij art. 51 van de wet van 09.04.2024 (B.S., 18.04.2024). Tekst van toepassing vanaf 28.04.2024 (art. -))

Personen die als daders of als medeplichtigen van misdrijven bedoeld in de artikelen 206 en 206bis werden veroordeeld, zijn hoofdelijk gehouden tot betaling van de ontdoken belasting en de interesten verschuldigd door de oorspronkelijke belastingschuldige.
De personen beschuldigd als daders of als medeplichtigen van misdrijven bedoeld in de artikelen 206 en 206bis zijn eveneens gehouden tot betaling van de ontdoken rechten en de interesten zoals bedoeld in het eerste lid, wanneer de bestanddelen van de misdrijven bewezen verklaard zijn, wanneer ze genieten van:

1° een opschorting van de uitspraak van de veroordeling of een uitstel van de tenuitvoerlegging van de straffen voorzien in de wet van 29 juni 1964 betreffende de opschorting, het uitstel en de probatie;

2° een veroordeling bij eenvoudige schuldigverklaring voorzien in artikel 27 van de Voorafgaande titel van het Wetboek van Strafvordering;

3° de procedure van voorafgaande erkenning van schuld bedoeld in artikel 216 van het Wetboek van Strafvordering;

4° de verjaring van de strafvordering.

De natuurlijke personen of de rechtspersonen zijn burgerlijk en hoofdelijk aansprakelijk voor de geldboeten en kosten die het gevolg zijn van de veroordelingen welke krachtens de artikelen 206 tot 207bis tegen hun aangestelden of hun bestuurders, zaakvoerders of vereffenaars, in het kader van de uitoefening van hun functie, in rechte of in feite zijn uitgesproken.

###### Art. 207quinquies

(van toepassing vanaf 14.02.1981)

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van toepassing vanaf 14.02.1981 (art. 22))

De rechter kan bevelen dat ieder vonnis of arrest houdende veroordeling tot een gevangenisstraf, uitgesproken krachtens de artikelen 206, 206bis en 207bis, wordt aangeplakt in de plaatsen die hij bepaalt en eventueel bij uittreksel, wordt bekendgemaakt op de wijze die hij bepaalt, een en ander op kosten van de veroordeelde.

Hetzelfde kan gelden voor iedere krachtens artikel 207 uitgesproken beslissing tot verbod van het uitoefenen van een beroepswerkzaamheid in België of tot sluiting van de in het land geëxploiteerde inrichtingen.

###### Art. 207sexies

(van toepassing vanaf 14.02.1981)

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van toepassing vanaf 14.02.1981 (art. 22))

De schending van het bij artikel 236bis bepaalde beroepsgeheim wordt gestraft overeenkomstig de artikelen 66, 67 en 458 van het Strafwetboek.

###### Art. 207septies

(van toepassing vanaf 01.01.2020)
(gewijzigd bij art. 110 van de wet van 05.05.2019 (B.S., 24.05.2019 – ed. 1). Tekst van toepassing op de datum bepaald door de Koning en ten laatste op 01.01.2020 (art. 200))

§ 1. De strafvordering wordt uitgeoefend door het openbaar ministerie.

§ 2. Het openbaar ministerie kan geen vervolging instellen indien het kennis heeft gekregen van de feiten ten gevolge van een klacht of een aangifte van een ambtenaar die niet de machtiging had waarvan sprake is in artikel 29, § 2, van het Wetboek van strafvordering.

Het openbaar ministerie beslist om al dan niet de strafvervolging in te stellen van de feiten waarvan het kennis heeft genomen gedurende het overleg bedoeld in artikel 29, § 3, tweede lid, van het Wetboek van strafvordering binnen de 3 maanden na de initiële aangifte bedoeld in artikel 29, § 3, eerste lid, van hetzelfde Wetboek.

§ 3. Onverminderd het in artikel 29, § 3, tweede lid, van het Wetboek van strafvordering bedoelde overleg, kan de procureur des Konings, indien hij een vervolging instelt wegens feiten die strafrechtelijk strafbaar zijn ingevolge de bepalingen van dit Wetboek of van de ter uitvoering ervan genomen besluiten, het advies vragen van de bevoegde adviseur-generaal. De procureur des Konings voegt het feitenmateriaal waarover hij beschikt bij zijn verzoek om advies. De adviseur-generaal antwoordt op dit verzoek binnen vier maanden na de ontvangst ervan.

In geen geval schorst het verzoek om advies de strafvordering.

###### Art. 207octies

(van toepassing vanaf 16.05.2014)

(gewijzigd bij art. 70 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van toepassing vanaf 16.05.2014 (art. 99))

De ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie en de Algemene Administratie van de Bijzondere Belastinginspectie mogen, op straffe van nietigheid van de akte van rechtspleging, slechts als getuige worden gehoord.

Het eerste lid is niet van toepassing op de krachtens artikel 71 van de wet van 28 december 1992 bij het parket gedetacheerde ambtenaren van die administraties.

Het eerste lid is evenmin van toepassing op de ambtenaren van die administraties die, krachtens artikel 31 van de wet van 30 maart 1994 tot uitvoering van het globaal plan op het stuk van de fiscaliteit, ter beschikking zijn gesteld van de federale politie.

Het eerste lid is niet van toepassing op de ambtenaren die deelnemen aan het in artikel 29, derde lid van het Wetboek van strafvordering bedoelde overleg.

### HOOFDSTUK XIII - Teruggaaf

###### Art. 208

(van toepassing vanaf 01.02.1940)

De regelmatig geheven rechten kunnen niet worden teruggegeven, welke ook de latere gebeurtenissen zijn, behoudens in de bij deze titel voorziene gevallen.

###### Art. 209

(van toepassing vanaf 24.07.2025)

(lid 1, 7°, ingevoegd bij art. 9 van de ordonnantie van 17.07.2025 (B.S., 24.07.2025). Tekst van toepassing vanaf 24.07.2025 (art. 15))

Zijn vatbaar voor teruggaaf:

1° De rechten, geheven omdat de partijen in gebreke gebleven zijn in de akte of verklaring te vermelden: a) dat de overeenkomst reeds belast werd; b) dat de voorwaarden tot bekomen van vrijstelling of vermindering vervuld zijn, tenzij het bestaan van deze vermelding bij de wet als een uitdrukkelijke voorwaarde ter verkrijging van de fiscale gunst is gesteld;

2° De evenredige rechten geheven hetzij wegens een akte die vals verklaard werd, hetzij wegens een overeenkomst waarvan de nietigheid of de vernietiging verklaard of vastgesteld wordt door een in kracht van gewijsde gegaan vonnis of arrest.

3° de evenredige rechten geheven wegens een overeenkomst waarvan een in kracht van gewijsde gegaan vonnis of arrest de ontbinding of de herroeping uitspreekt of vaststelt, mits uit de beslissing blijkt dat ten hoogste één jaar na de overeenkomst een eis tot ontbinding of herroeping of tot vaststelling van ontbinding of herroeping, zelfs bij een onbevoegd rechter, is ingesteld;

3°/1 de evenredige rechten geheven overeenkomstig de artikelen 44 tot 71, 72, tweede lid, 74 en 75 wegens een overeenkomst die het voorwerp heeft uitgemaakt van een vermindering van de verkoopprijs uitgesproken bij een in kracht van gewijsde gegaan vonnis of arrest met het oog op de waarborg van de verkoper overeenkomstig de artikelen 1637 en 1644 van het Burgerlijk Wetboek, mits uit de beslissing blijkt dat de overeenkomst dateert van niet meer dan een jaar vóór een eis die hoofdzakelijk of subsidiair is gegrond op die bepalingen, zelfs als is die bij een onbevoegd rechter ingesteld: de teruggave is gelijk aan het bedrag van de evenredige rechten betaald op het gedeelte van de aankoopprijs dat terugbetaald is door de verkoper of zijn rechthebbenden zonder dat die teruggave evenwel als gevolg kan hebben dat het evenredige recht betreffende de overdracht onder bezwarende titel van dat onroerend goed geheven wordt op een totale belastbare grondslag kleiner dan de verkoopwaarde van het onroerend goed rekening houdende met zijn werkelijke staat op het moment van de aankoop;

3°/2 de evenredige rechten geheven overeenkomstig de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies wegens een overeenkomst waarvan de nietigverklaring, de vernietiging, de annulering of de ontbinding minnelijk is overeengekomen tussen de partijen op volgende voorwaarden: a. de overeenkomst tot nietigverklaring, vernietiging, annulering of ontbinding is ter registratie aangeboden uiterlijk op hetzelfde ogenblik als de aanvraag tot teruggave;

b. de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst is nog niet vastgesteld bij een authentieke akte;

c. de nietig verklaarde, vernietigde, geannuleerde of ontbonden overeenkomst is niet meer dan één jaar vóór het sluiten van de overeenkomst tot nietigverklaring, vernietiging, annulering of ontbinding gesloten;

3°/3 de evenredige rechten geheven overeenkomstig de artikelen 44 tot 71, 72, tweede lid, 74 en 75, 109 tot 114, 131 tot 140octies wegens een overeenkomst waarvan de ontbinding voortvloeit uit de toepassing van een ontbindende voorwaarde van rechtswege op volgende voorwaarden:

a. de vervulling van de ontbindende voorwaarde is vastgesteld in een akte getekend door alle partijen en ter registratie aangeboden uiterlijk op het ogenblik van de aanvraag tot teruggave; wanneer de ontbonden overeenkomst bij een authentieke akte vastgesteld is, moet de vervulling van de ontbindende voorwaarde ook bij een authentieke akte getekend door alle partijen vastgesteld worden;

b. de ontbonden overeenkomst is niet meer dan één jaar vóór de datum van vervulling van de ontbindende voorwaarde gesloten;

4° de evenredige rechten geheven op een door een rechtspersoon gestelde rechtshandeling die door de hogere overheid nietig verklaard werd.

5° de bij toepassing van de artikelen 115, 115bis, 116 en 120 aan het tarief van 0,5% geheven rechten naar aanleiding van een vermeerdering van het kapitaal of het eigen vermogen, met nieuwe inbreng, door een vennootschap bedoeld in artikel 201, eerste lid, 1°, van het Wetboek van de inkomstenbelastingen 1992, mits die vermeerdering van het kapitaal of het eigen vermogen is geschied binnen het jaar vóór de datum van de toelating tot de notering op een Belgische effectenbeurs van aandelen of met aandelen gelijk te stellen waardepapieren van de vennootschap.

6° de geheven evenredige rechten indien op de verrichting van overdracht onder bezwarende titel van een onroerend goed of van de vestiging, overdracht en wederoverdracht van een zakelijk recht op een onroerend goed, de belasting over de toegevoegde waarde opeisbaar wordt ingevolge de toepassing van artikel 1, § 10, van het Wetboek van de belasting over de toegevoegde waarde.

7° de aanvullende rechten bedoeld in artikel 46bis, zevende lid, in voorkomend geval verhoogd met de aanvullende rechten bedoeld in artikel 46ter, zesde lid, of in artikel 212bis, vierde lid, wanneer de verkrijgers hun hoofdverblijfplaats hebben gevestigd op de plaats van het verkregen onroerend goed zodra de overmacht die hen belette de termijn te respecteren heeft opgehouden, naargelang het geval, in artikel 46bis, vijfde lid, 2°, b), of in artikel 212bis, tweede lid, 2°, a).

Behalve in het geval van het eerste lid, 3°/1, geschiedt de teruggaaf, in voorkomend geval, onder aftrekking van het algemeen vast recht. In de gevallen van de teruggaven bedoeld onder het eerste lid, 2°, 3°, 3°/2 en 3°/3 geschiedt de teruggaaf evenwel onder de enige aftrekking, in voorkomend geval, van het bijzonder vast recht van 10 euro bedoeld in artikel 159bis.

###### Art. 210

(van toepassing vanaf 16.05.2019)

(gewijzigd bij art. 26 van de wet van 28.04.2019 (B.S., 06.05.2019). Tekst van toepassing vanaf 106.05.2019 (art. -))

In geval van gehele of gedeeltelijke vernietiging van een vonnis of arrest door een andere in kracht van gewijsde gegane rechterlijke beslissing zijn de op de vernietigde beslissing geheven evenredige rechten voor gehele of gedeeltelijke teruggaaf vatbaar.

Het op een voorwaardelijke veroordeling geheven evenredig recht wordt teruggegeven in de mate dat er wordt aangetoond door alle middelen van gemeen recht, met inbegrip van getuigen en vermoedens, met uitzondering van de eed, dat de voorwaarde niet in vervulling is gegaan en het niet in vervulling gaan van de voorwaarde leidt tot een resultaat dat gelijk is aan het afwijzen van de vordering.

Het recht wordt volledig teruggegeven indien het samengevoegd bedrag van de veroordelingen, vereffeningen of rangregelingen, waarop de heffing werd gedaan, herleid wordt tot een som die bij artikel 143, laatste lid, vastgestelde bedrag niet overschrijdt.

###### Art. 211

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 23 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 212

(van toepassing vanaf 09.03.2026)

(lid 5, gewijzigd bij art. 25 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

In geval van wederverkoop van een onroerend goed, door de verkoper of zijn rechtsvoorgangers verkregen bij een akte waarop het bij artikel 44 voor de verkopingen vastgestelde recht is voldaan, wordt 36 pct. van dat recht aan de wederverkoper teruggegeven indien de wederverkoop bij authentieke akte vastgesteld is binnen twee jaar na de datum van de authentieke akte van verkrijging.

Wanneer de verkrijging of de wederverkoop heeft plaatsgehad onder een opschortende voorwaarde, wordt de termijn van wederverkoop berekend op basis van de datum waarop deze voorwaarde is vervuld.
Niet teruggegeven wordt het recht dat betrekking heeft op het gedeelte van de prijs en de lasten van de verkrijging, dat hoger is dan de grondslag van het recht dat van toepassing is op de akte van wederverkoop, berekend zonder de vermindering voorgeschreven bij artikel 46bis.

In geval van gedeeltelijke wederverkoop wordt in het verzoek tot teruggave het deel van de aanschaffingsprijs dat betrekking heeft op het wederverkochte gedeelte nader aangegeven onder controle van het bestuur.

Een door de wederverkoper en de instrumenterende notaris ondertekend verzoek tot teruggave, onderaan op de akte gesteld voor de registratie, heeft dezelfde gevolgen als het met redenen omkleed verzoek ingevolge artikel
2172. Dit verzoek moet een afschrift van de vermelding van de registratie van de authentieke akte van verkrijging bevatten, alsook de naam van de begunstigde van de teruggave en, in voorkomend geval, het rekeningnummer waarop het bedrag van de terug te geven rechten moet worden gestort.

###### Art. 212bis

(van toepassing vanaf 24.07.2025)

(lid 4, aangevuld bij art. 11 van de ordonnantie van 17.07.2025 (B.S., 24.07.2025). Tekst van toepassing vanaf 24.07.2025 (art. 15))

Wanneer het voordeel van de vermindering van de belastbare grondslag als bepaald in artikel 46bis en, in voorkomend geval, de verhoging van de vermindering van de belastbare grondslag als bedoeld in artikel 46ter niet kon worden bekomen omdat niet voldaan was aan de voorwaarde daartoe gesteld in artikel 46bis, vijfde lid, 1°, worden de rechten die geheven werden boven het bedrag dat zou verschuldigd geweest zijn met toepassing van artikel 46bis en, in voorkomend geval, van artikel 46ter, teruggegeven, mits alle onroerende goederen die de vermindering van de heffingsgrondslag verhinderden, zijn vervreemd bij overeenkomsten, andere dan ruil, die vaste datum hebben gekregen uiterlijk twee jaar na de datum van de registratie van het document dat aanleiding heeft gegeven tot de heffing van het evenredig recht op de verkrijging waarvoor de teruggave wordt gevraagd. Werd bedoeld document evenwel te laat ter registratie aangeboden, dan wordt die termijn gerekend vanaf de uiterste datum voor de tijdige aanbieding ervan.

Aan de teruggave zijn de volgen de voorwaarden verbonden:

1° het gemotiveerd verzoek bevat:

a) een afschrift van het registratierelaas dat werd aangebracht op het document dat aanleiding heeft gegeven tot de heffing van het evenredig recht op de verkrijging waarvoor de teruggave wordt gevraagd;

b) de kadastrale beschrijving van alle onroerende goederen die de toepassing van artikel 46bis hebben verhinderd, evenals de data waarop de vervreemdingen van die goederen vaste datum hebben gekregen;

2° in het gemotiveerd verzoek moeten de betrokken verkrijgers:

a) verklaren dat zij hun hoofdverblijfplaats hebben gevestigd of zullen vestigen op het adres van het verkregen onroerend goed binnen drie jaar of, in geval van aanvraag om toepassing van artikel 46ter, binnen vijf jaar te rekenen van hetzij de datum van de registratie van het document dat aanleiding heeft gegeven tot de heffing van het evenredig recht op die verkrijging, hetzij, wanneer dat document te laat ter registratie werd aangeboden, de uiterste datum voor de tijdige aanbieding ervan;

b) zich ertoe verbinden hun hoofdverblijfplaats in het verkregen onroerend goed te behouden gedurende een ononderbroken periode van minstens vijf jaar vanaf het tijdstip waarop ze hun hoofdverblijfplaats gevestigd hebben in het onroerend goed waarvoor de teruggave werd gevraagd.

c) in voorkomend geval, de informatie bedoeld in artikel 46ter, vierde lid, 2°, a) vermelden en aan het gemotiveerd verzoek het document bedoeld in artikel 46ter, vierde lid, 3° bijvoegen;

d) in voorkomend geval, zich ertoe verbinden de in artikel 46ter, vierde lid, 1°, bedoelde verbintenis na te leven, volgens dezelfde modaliteiten als diegene die in het vierde lid, 2°, b), van hetzelfde artikel bepaald zijn.

Een door de betrokken verkrijgers en de instrumenterende notaris ondertekend verzoek tot teruggave, onderaan op de akte gesteld voor de registratie, heeft dezelfde gevolgen als het met redenen omkleed verzoek ingevolge artikel 2172.

Ingeval de verklaring van de verkrijgers bedoeld in 2°, a), van het tweede lid onjuist wordt bevonden, zijn zij ondeelbaar gehouden tot terugbetaling van het teruggegeven bedrag en verbeuren zij ondeelbaar een boete gelijk aan dat bedrag. Voldoen sommige verkrijgers wel en andere niet aan de bedoelde voorwaarden, dan wordt het terug te geven bedrag en de boete, waartoe de verkrijgers die niet aan de voorwaarden voldoen ondeelbaar gehouden zijn, bepaald naar verhouding van hun wettelijk aandeel in het onroerend goed waarvoor de teruggave werd gevraagd. De boete is evenwel niet verschuldigd wanneer door overmacht aan de voorwaarden niet voldaan kon worden; hetzelfde geldt ook, bij wege van teruggaaf overeenkomstig artikel 209, eerste lid, 7°, voor de aanvullende rechten, wanneer de termijn bedoeld in het tweede lid, 2°, a), niet werd gerespecteerd als gevolg van een geval van overmacht, op voorwaarde dat de verkrijgers hun hoofdverblijfplaats vestigen op de plaats van het verkregen onroerend goed van zodra de overmacht ophoudt.

Ingeval de in het tweede lid, 2°, c) vermelde gegevens onjuist zijn, zijn de verkrijgers ondeelbaar gehouden tot terugbetaling van het teruggegeven bedrag en verbeuren zij ondeelbaar een boete gelijk aan de helft van dit bedrag.

Behoudens overmacht, zijn aanvullende rechten op het bedrag waarmee de belastbare grondslag werd verminderd als bedoeld in artikel 46bis en, in voorkomend geval, op het bedrag van de verhoging van de vermindering van de belastbare grondslag als bedoeld in artikel 46ter, ondeelbaar verschuldigd door de verkrijgers indien geen van hen de in het tweede lid, 2°, b), bedoelde verbintenis naleeft. De verschuldigde aanvullende rechten op het bedrag waarmee de belastbare grondslag werd verminderd als bedoeld in artikel 46bis, worden verminderd in verhouding tot het aantal ononderbroken jaren tijdens welke de voornoemde verbintenis werd nagekomen.

Ingeval de in het tweede lid, 2°, d), bedoelde verbintenis niet wordt nagekomen, zijn de verkrijgers ondeelbaar gehouden tot betaling van de aanvullende rechten op het bedrag van de verhoging van de vermindering van de belastbare grondslag als bedoeld in artikel 46ter, derde lid, en van een boete gelijk aan tien procent van die aanvullende rechten. De boete is evenwel niet verschuldigd wanneer door overmacht aan de verbintenis niet voldaan kon worden.

###### Art. 212ter

(van toepassing vanaf 01.04.2023)
(gewijzigd bij art. 5 van de ordonnantie van 17.11.2022 (B.S., 05.12.2022). Tekst van toepassing vanaf 01.04.2023 (art. 8))

Ingeval de in de artikelen 46bis of 46ter bepaalde verminderingen van de heffingsgrondslag niet werden gevraagd of niet werden bekomen naar aanleiding van de registratie van het document dat aanleiding heeft gegeven tot de heffing van het evenredig recht, kunnen de teveel geheven rechten worden teruggegeven op verzoek in te dienen overeenkomstig de bepalingen van artikel 2172 binnen zes maanden te rekenen van de datum van registratie van dat document.

Het verzoek tot teruggave bedoeld in het eerste lid bevat de vermeldingen en verklaringen vereist bij artikel 46bis, vijfde lid, 2°, a, b en c, en, in voorkomend geval, de vermeldingen, verklaringen en documenten vereist bij artikel 46ter, vierde lid, 2° en 3°. Het verzoek vermeldt in voorkomend geval ook het rekeningnummer waarop het bedrag van de terug te geven rechten kan worden gestort.

###### Art. 212quater

(van toepassing vanaf 01.04.2023)

(ingevoegd bij art. 6 van de ordonnantie van 17.11.2022 (B.S., 05.12.2022). Tekst van toepassing vanaf 01.04.2023 (art. 8))

Voor de toepassing van dit artikel zijn de definities opgenomen in artikel 46ter, eerste lid, van toepassing.

Wanneer de verbetering van de energieprestatie bereikt bij het verstrijken van de termijn bedoeld in artikel 46ter, vierde lid, 1° groter is dan deze vermeld in het vierde lid, 2°, b) van hetzelfde artikel bedoelde verbintenis, worden de geheven rechten teruggeven boven het bedrag dat zou verschuldigd geweest zijn indien rekening zou zijn gehouden met de verbetering van de energieklassen waarmee geen rekening werd gehouden voor de vaststelling van het bedrag van de verhoging van de vermindering van de belastbare grondslag overeenkomstig het derde lid van hetzelfde artikel.

De teruggaaf is onderworpen aan het indienen van een gemotiveerd verzoek bevattende :

1° een kopie van de vermelding van de registratie die werd aangebracht op het document dat aanleiding heeft gegeven tot de heffing van het evenredig registratierecht op de verkrijging waarvoor de teruggaaf wordt gevraagd ;

2° een kopie van het meest recente, geldige EPB-certificaat opgesteld voor het verkregen goed uiterlijk op het einde van de termijn bedoeld in het vierde lid, 1° van hetzelfde artikel.

De aanvraag tot teruggaaf moet worden ingediend overeenkomstig de bepalingen van artikel 2172 binnen zes maanden vanaf het verstrijken van de termijn bedoeld in artikel 46ter, vierde lid, 1°. De aanvraag vermeldt, in voorkomend geval, het bankrekeningnummer waarop het bedrag van de terug te betalen rechten kan worden betaald.

###### Art. 213

(van toepassing vanaf 30.04.1967)
(gewijzigd bij art. 24 van het KB nr. 12 van 18.04.1967 (B.S., 20.04.1967). Tekst van toepassing vanaf 30.04.1967 (art. -))

Wordt, onder aftrekking van het algemeen vast recht, aan de betrokken maatschappij teruggegeven het overeenkomstig artikel 51 geheven recht van 6 t.h. wanneer het aangekochte goed wordt wederverkocht bij authentieke akte verleden binnen tien jaar na den datum van de akte van verkrijging.

Zijn toepasselijk op deze teruggaaf, de bepalingen van artikel 212, tweede en derde lid.

### HOOFDSTUK XIV - Verjaring

###### Art. 214

(van toepassing vanaf 10.01.1993)

(gewijzigd bij art. 63 van de wet van 28.12.1992 (B.S., 31.12.1992 – ed. 3) err. (B.S., 18.02.1993). Tekst van toepassing vanaf 10.01.1993 (art. -))

Er is verjaring voor de invordering:

1° Van rechten en boeten verschuldigd op een akte of een overeenkomst, na twee jaar, enkel te rekenen van den dag van de registratie van een akte of geschrift welke de oorzaak van de vorderbaarheid van de rechten en boeten aan het bestuur genoegzaam doet kennen om de noodzakelijkheid van alle verdere opzoeking uit te sluiten.

Worden, voor de toepassing van deze bepaling met registratie gelijkgesteld: het visum van de repertoria van de notarissen, waarvan sprake in artikel 180; de ontvangst van de bij artikel 184 voorgeschreven mededeling, zoomede de regelmatige inlevering van een aangifte van nalatenschap;

2° Van rechten en boeten verschuldigd in geval van ontoereikende waardering, na twee jaar, te rekenen van den dag van de registratie van de akte of van de verklaring, dit alles onder voorbehoud van hetgeen in artikel 190 is voorzien;

3° van rechten verschuldigd in geval van niet-vervulling van de in artikel 60 gestelde voorwaarden, na tien jaar, te rekenen van de datum van de akte;

4° Van rechten verschuldigd in het in de tweede alinea van artikel 52 voorzien geval, na twee jaar, te rekenen van de intrekking van de premie;

5° Van rechten en boeten verschuldigd in geval van onjuistheid in de in artikelen 55, 2°, voorziene vermeldingen of attesten, na twee jaar, te rekenen van den dag van de registratie van de akte;

6° Van boeten verschuldigd in de in artikelen 1811 tot 183 voorziene gevallen, na twee jaar, te rekenen van den dag waarop de overtreding werd vastgesteld;
7° Van rechten en boeten verschuldigd buiten de in voorgaande nummers voorziene gevallen, met inbegrip van die welke betrekking hebben op veinzing, bewimpeling van prijs of al ander feit niet of onjuist vastgesteld in een geregistreerde akte, na vijftien jaar, te rekenen van den dag waarop de rechtsvordering van de Staat ontstaan is.

Is van toepassing, ten aanzien van de verjaring, artikel 18 van dit wetboek.

###### Art. 215

(van toepassing vanaf 01.02.1940)

Er is verjaring voor de vordering tot teruggaaf van rechten, interesten en boeten, na twee jaar, te rekenen van den dag waarop de rechtsvordering is ontstaan.

###### Art. 216

(van toepassing vanaf 01.02.1940)

De verjaring van de bij artikel 189 ingestelde rechtsvordering tot schatting en die van de rechtsvordering tot inning van de rechten en boeten verschuldigd wegens de ongenoegzaamheid blijkende uit die schatting, worden gestuit door de in artikel 190 bedoelde notificatie.

De stuiting heeft haar uitwerking tot den dag der nederlegging ter griffie van het verslag van schatting.

De invordering van rechten, interesten en gebeurlijk van boeten en kosten, vorderbaar uit hoofde van de bij bedoeld verslag erkende ongenoegzaamheid, dient vervolgd binnen de twee jaar na de nederlegging van dit verslag.

###### Art. 2171

(van toepassing vanaf 17.01.1959)

(gewijzigd en art. 2171 geworden bij art. 36 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing van 17.01.1959 (art. -))

De verjaringen voor de invordering van rechten, interesten en boeten, worden gestuit op de wijze en onder de voorwaarden voorzien door artikel 2244 en volgende van het Burgerlijk Wetboek. In dit geval is er een nieuwe verjaring, die op dezelfde wijze kan worden gestuit, verworven twee jaar na de laatste akte of handeling waardoor de vorige verjaring werd gestuit, indien er geen geding aanhangig is vóór het gerecht.

De afstand van de verlopen tijd van de verjaring wordt, wat zijn uitwerking betreft, gelijkgesteld met de stuitingshandelingen bedoeld in vorige alinea.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 2172

(van toepassing vanaf 01.01.2028)
(gewijzigd bij art. 72 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De verjaringen voor de teruggaaf van rechten, interesten en boeten worden gestuit door een met redenen omklede aanvraag genotificeerd bij aangetekende zending aan het kantoor dat de schuld heeft vastgesteld of aan de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie; ze worden eveneens gestuit op de wijze en onder de voorwaarden voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee jaar, die slechts op de wijze en onder de voorwaarden voorzien bij artikelen 2244 en volgende van het Burgerlijk Wetboek kan worden gestuit, verworven twee jaar na de datum waarop de beslissing, waarbij de aanvraag werd verworpen, aan belanghebbende met een aangetekende zending genotificeerd werd.

###### Art. 2172

(van toepassing vanaf 01.12.2021)

(gewijzigd bij art. 3 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van toepassing vanaf 01.12.2021 (art. 7))

De verjaringen voor de teruggaaf van rechten, interesten en boeten worden gestuit door een met redenen omklede aanvraag genotificeerd bij aangetekende zending aan het kantoor dat de schuld heeft vastgesteld of aan de bevoegde adviseur-generaal van de Algemene Administratie van de Patrimoniumdocumentatie; ze worden eveneens gestuit op de wijze en onder de voorwaarden voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee jaar, die slechts op de wijze en onder de voorwaarden voorzien bij artikelen 2244 en volgende van het Burgerlijk Wetboek kan worden gestuit, verworven twee jaar na de datum waarop de beslissing, waarbij de aanvraag werd verworpen, aan belanghebbende bij ter post aangetekend schrijven genotificeerd werd.

De afgifte van de brieven ter post geldt als notificatie van de volgende dag af.

###### Art. 218

(van toepassing vanaf 09.04.2018)

(vervangen bij art. 96 van de wet van 26.03.2018 (B.S., 30.03.2018 – ed. 2). Tekst van toepassing vanaf 09.04.2018 (art. -))

Elke daad van onderzoek of van vervolging als bedoeld in artikel 22 van de Voorafgaande Titel van het Wetboek van Strafvordering betreffende de misdrijven bedoeld in artikel 206 en 206bis schorst de verjaring van de vordering tot voldoening van de rechten, de interesten en de fiscale geldboeten die erop betrekking hebben.
De schorsing vangt aan met het op gang brengen van de strafvordering, en eindigt met het staken van de strafrechtelijke vervolging, het verval van de strafvordering of wanneer het vonnis of arrest in kracht van gewijsde is gegaan voor de misdrijven bedoeld in het eerste lid.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Art. 219

(van toepassing vanaf 01.01.2028)

(lid 2, gewijzigd bij art. 73 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De moeilijkheden die in verband met de heffing of de invordering van de registratierechten vóór het inleiden der gedingen kunnen oprijzen, worden door de minister van Financiën of de door hem gemachtigde ambtenaar opgelost.

Indien, na onderhandelingen, met de minister of met de door hem gemachtigde ambtenaar geen akkoord wordt bereikt over een moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een aanvraag tot bemiddeling verzenden bij de fiscale bemiddelingsdienst bedoeld bij artikel 116 van de wet van 25 april 2007 houdende diverse bepalingen (IV).

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat aan de in artikel 189 bedoelde schatting is onderworpen, kan de bemiddeling van de fiscale bemiddelingsdienst daarover niet meer gevraagd of worden voortgezet zodra de vordering tot controleschatting is ingesteld. De Koning kan bepalen voor welke moeilijkheden in verband met de heffing en invordering van de registratierechten bemiddeling door de fiscale bemiddelingsdienst is uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar gaat dadingen met de belastingplichtigen aan, voor zover zij geen vrijstelling of vermindering van belasting in zich sluiten.

Binnen de door de wet gestelde grenzen, wordt het bedrag van de proportionele fiscale boeten en de vermeerderingen vastgesteld in dit Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald volgens een schaal waarvan de trappen door de Koning worden vastgesteld. Deze bepaling geldt niet voor het bedrag van de proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en 204, behalve wanneer de overtreder hetzij uit eigen beweging en voordat het bestuur iets gevorderd heeft, de overtreding aan het bestuur bekent, hetzij overleden is.

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Art. 219

(van toepassing vanaf 01.05.2007)

(gewijzigd bij art. 124 van de wet van 25.04.2007 (B.S., 08.05.2007 – ed. 3). Tekst van toepassing vanaf 01.05.2007 (in afwijking hiervan kan de aanvraag tot bemiddeling slechts worden ingediend met ingang van 01.11.2007 (art. 14, KB van 09.05.2007 (B.S., 24.05.2007)))

De moeilijkheden die in verband met de heffing of de invordering van de registratierechten vóór het inleiden der gedingen kunnen oprijzen, worden door de minister van Financiën of de door hem gemachtigde ambtenaar opgelost.

Indien, na onderhandelingen, met de minister of met de door hem gemachtigde ambtenaar geen akkoord wordt bereikt over een moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een aanvraag tot bemiddeling indienen bij de fiscale bemiddelingsdienst bedoeld bij artikel 116 van de wet van 25 april 2007 houdende diverse bepalingen (IV).

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat aan de in artikel 189 bedoelde schatting is onderworpen, kan de bemiddeling van de fiscale bemiddelingsdienst daarover niet meer gevraagd of worden voortgezet zodra de vordering tot controleschatting is ingesteld. De Koning kan bepalen voor welke moeilijkheden in verband met de heffing en invordering van de registratierechten bemiddeling door de fiscale bemiddelingsdienst is uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar gaat dadingen met de belastingplichtigen aan, voor zover zij geen vrijstelling of vermindering van belasting in zich sluiten.

Binnen de door de wet gestelde grenzen, wordt het bedrag van de proportionele fiscale boeten en de vermeerderingen vastgesteld in dit Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald volgens een schaal waarvan de trappen door de Koning worden vastgesteld. Deze bepaling geldt niet voor het bedrag van de proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en 204, behalve wanneer de overtreder hetzij uit eigen beweging en voordat het bestuur iets gevorderd heeft, de overtreding aan het bestuur bekent, hetzij overleden is.

###### Art. 220

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 62 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

De eerste akte van vervolging ter invordering van fiscale rechten of boeten en bijkomende sommen is een dwangschrift.
Het wordt door den met de invordering belasten ontvanger uitgevaardigd; het wordt door den bevoegde adviseurgeneraal van de Algemene Administratie van de Patrimoniumdocumentatie geviseerd en uitvoerbaar verklaard en bij deurwaardersexploot van gerechtsdeurwaarder betekend.

###### Art. 221

(van toepassing vanaf 06.04.1999)

(vervangen bij art. 67 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van toepassing van 06.04.1999 (art. -))

De tenuitvoerlegging van het dwangbevel kan slechts worden gestuit door een vordering in rechte.

###### Art. 222

(van toepassing vanaf 01.12.2021)

(gewijzigd bij art. 4 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van toepassing vanaf 01.12.2021 (art. 7))

In geval van niet-betaling van een schuld voortvloeiende uit de toepassing van dit Wetboek, kan de ambtenaar die belast is met de invordering van die schuld, bij het Centraal Aanspreekpunt van de Nationale Bank bedoeld in artikel 322, § 3, eerste lid, van het Wetboek van de inkomstenbelastingen 1992 de gegevens opvragen die ten aanzien van die schuldenaar beschikbaar zijn zonder de beperkingen van artikel 322, §§ 2 tot 4, van hetzelfde Wetboek. De machtiging hiertoe wordt verleend door een ambtenaar met minimum de graad van adviseur–generaal.

###### Art. 223

(van toepassing vanaf 01.02.1940)

De moratoire interesten op de in te vorderen of terug te geven sommen zijn verschuldigd naar den voet en de regelen in burgerlijke zaken vastgesteld.

###### Art. 224

(van toepassing vanaf 06.04.1999)

(opgeheven bij art. 69 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van toepassing vanaf 06.04.1999 (art. -))

(…)

###### Art. 225

(van toepassing vanaf 01.02.1940)

De openbare ambtenaren die, krachtens de bepalingen van deze titel, voor de partijen, de rechten en, bij voorkomend geval, de boeten voorgeschoten hebben, kunnen, met het oog op de terugbetaling ervan, uitvoerbaar bevel vragen aan de vrederechter van hun kanton.
De bepalingen van dit hoofdstuk zijn toepasselijk op het tegen dit bevel aangetekend verzet.

###### Art. 225bis

(van toepassing vanaf 06.04.1999)

(ingevoegd bij art. 70 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van toepassing vanaf 06.04.1999 (art. -))

De termijnen van verzet, hoger beroep en cassatie, alsmede het verzet, het hoger beroep en de voorziening in cassatie schorsen de tenuitvoerlegging van de gerechtelijke beslissing.

###### Art. 225ter

(van toepassing vanaf 10.01.2005)

(vervangen bij art. 382 van de programmawet van 27.12.2004 (B.S., 31.12.2004 – ed. 2). Tekst van toepassing vanaf 10.01.2005 (art. -))

Het verzoekschrift houdende voorziening in cassatie en het antwoord op de voorziening mag door een advocaat worden ondertekend en neergelegd.

###### Art. 225quater

(van toepassing vanaf 09.04.2018)

(ingevoegd bij art. 97 van de wet van 26.03.2018 (B.S., 30.03.2018 – ed. 2). Tekst van toepassing vanaf 09.04.2018 (art. -))

De bepalingen van dit Wetboek doen geen afbreuk aan het recht van de Staat om het herstel van de schade te vorderen die kan bestaan uit de niet-betaling van de rechten, interesten, fiscale geldboeten en bijbehoren door een burgerlijke partijstelling of door een aansprakelijkheidsvordering.

### HOOFDSTUK XVI - Bijzondere bepalingen betreffende de openbare verkopingen van roerende goederen

###### Art. 226

(van toepassing vanaf 28.09.1963)

(gewijzigd bij art. 48, § 4, van de wet van 05.07.1963 (M.B., 17.07.1963). Tekst van toepassing vanaf 28.09.1963 (art. 52))

Meubelen, koopwaren, hout, vruchten, oogsten en alle andere lichamelijke roerende voorwerpen mogen bij openbare toewijzing slechts ten overstaan en door het ambt van een notaris of een gerechtsdeurwaarder verkocht worden.
Nochtans kunnen Staat, provinciën, gemeenten en openbare instellingen de hun toebehorende roerende voorwerpen openbaar door hun ambtenaren doen verkopen.

###### Art. 227

(van toepassing vanaf 01.01.2024)

(vervangen bij art. 27 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2). Tekst van toepassing vanaf 01.01.2024 (art. 29))

Iedere openbare officier die belast is met de openbare verkoop van roerende voorwerpen moet daarvan vooraf kennis geven aan het bevoegde kantoor, behalve wanneer het gaat om voorwerpen die aan de Staat, de gefedereerde entiteiten, de provincies, de gemeenten of de openbare instellingen toebehoren.

De Koning kan bepalen:

1° de nadere regels van deze kennisgeving en de vermelding, als de verkopende partij er een heeft, van haar identificatienummer in het Rijksregister van de natuurlijke personen of in de registers van de Kruispuntbank van de sociale zekerheid of in de Kruispuntbank van Ondernemingen;

2° dat de kennisgeving vergezeld moet gaan van metagegevens.

###### Art. 228

(van toepassing vanaf 01.02.1940)

De werkende openbare officier of ambtenaar vermeldt, in zijn proces-verbaal, naam, voornamen, hoedanigheid en woonplaats van den verzoeker, van de personen wier mobilair te koop wordt gesteld en, indien het gaat om een verkoop na overlijden, van den overleden eigenaar, zomede, desvorkomend, den datum van de overhandiging of de verzending van de in artikel 227 voorziene kennisgeving.

###### Art. 229

(van toepassing vanaf 01.01.2024)

(vervangen bij art. 28 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2). Tekst van toepassing vanaf 01.01.2024 (art. 29))

De instrumenterende openbare officier of ambtenaar verbeurt voor elke overtreding van de artikelen 227 en 228 een geldboete van 25 euro.

###### Art. 230

(van toepassing vanaf 01.02.1940)

De werkende openbare officier of ambtenaar moet van den openbaren verkoop een proces-verbaal opmaken.
Ieder toegewezen voorwerp wordt onmiddellijk in dat proces-verbaal opgetekend; de prijs wordt voluit in letterschrift en buiten de linie nog eens in cijfers aangeduid.

Na elke zitting wordt het proces-verbaal afgesloten en ondertekend.

###### Art. 231

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 190 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Wordt voor de toepassing van dit hoofdstuk als toegewezen beschouwd en is aan het door de artikel 77 vastgesteld evenredig recht onderworpen, ieder roerend voorwerp waarvan het openbaar tekoopstelling van een openbaar aanbod of een openbaar gemaakt aanbod is gevolgd, ongeacht wie het aanbod heeft gedaan en welke de modaliteiten van den verkoop zijn en ongeacht of al dan niet toewijzing plaats heeft.

Het recht is evenwel niet verschuldigd indien de werkende openbare officier of ambtenaar onmiddellijk na ontvangst en bekendmaking van de aanbiedingen verkondigt, en zulks in het proces-verbaal aantekent, dat het te koop gesteld voorwerp «ingehouden» wordt.

Het recht wordt geheven op den toewijzingsprijs en, bij gebreke daaraan, op het hoogste aanbod.

Wanneer het een verkoop geldt, gedaan op verzoek van een rechtspersoon, wordt nochtans niet afgeweken van artikelen 16 en 17 voor zover zij beschikken voor het geval van voorbehoud van machtiging, goedkeuring of bekrachtiging van de overheid.

###### Art. 232

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Worden door den werkenden openbaren officier of ambtenaar verbeurd:

1° Een geldboete, gelijk aan twintigmaal het ontdoken recht, zonder dat ze minder dan 25 EUR mag bedragen:

a) voor elk toegewezen of bij artikel 231 als dusdanig beschouwd lot, welk niet onmiddellijk in het proces-verbaal wordt opgetekend;

b) voor elk lot welk in het proces-verbaal als aan den verkoop onttrokken wordt opgegeven, wanneer de verklaring van inhouding niet werd gedaan in den bij artikel 231, 2de alinea, voorziene vorm;

c) voor elk lot waarvan de belastbare grondslag in het proces-verbaal vervalst of onvolkomen opgetekend werd; dit alles onverminderd het ontdoken recht;
2° Een boete van 12,50 EUR voor elk toegewezen lot waarvan de prijs in het proces-verbaal niet voluit in letters of niet in cijfers buiten de linie is aangeduid.

###### Art. 233

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Iedere persoon die, buiten de aanwezigheid van een openbaar officier, roerende voorwerpen openbaar te koop heeft gesteld of doen stellen, loopt een geldboete gelijk aan twintigmaal het ontdoken recht, zonder dat deze boete, voor elk toegewezen of als dusdanig beschouwd lot, minder dan 25 EUR mag bedragen.

De overtreders zijn daarbij hoofdelijk gehouden tot de betaling van het ontdoken recht.

###### Art. 234

(van toepassing vanaf 16.05.2016)

(gewijzigd bij art. 63 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van toepassing vanaf 16.05.2016 (art. -))

Ambtenaren van de Algemene Administratie van de Patrimoniumdocumentatie hebben steeds toegang tot alle plaatsen waar roerende voorwerpen openbaar worden verkocht. Zij hebben het recht zich de processen-verbaal van verkoop te doen overleggen en van hun bevindingen proces-verbaal op te maken. Dit proces-verbaal geldt als bewijs tot het tegenbewijs.

###### Art. 235

(van toepassing vanaf 27.07.1962)

(vervangen bij het enig art. van de wet van 03.07.1962 (B.S., 17.07.1962). Tekst van toepassing vanaf 27.07.1962 (art. -))

De bepalingen van dit hoofdstuk zijn niet van toepassing op de openbare verkopingen:

1° van alle landbouwproducten, in instellingen waar de koopwaren uitsluitend openbaar bij opbod of bij afbod verkocht worden op bepaalde dagen en uren, die op bestendige wijze in de lokalen aangeplakt zijn;

2° van eetwaren en van afgesneden bloemen in de voornoemde instellingen of op de markten;

3° van voorwerpen welke in de openbare kassen van lening in pand werden gegeven;

4° van zee- en binnenschepen.

### HOOFDSTUK XVII - Inlichtingen te verstrekken door de Algemene Administratie van de Patrimoniumdocumentatie

###### Art. 236

(van toepassing vanaf 01.11.2023 en 01.01.2024 (lid 3))

(vervangen bij art. 10 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van toepassing vanaf 01.11.2023 (art. 14, lid 1), met uitzondering van lid 3, van toepassing vanaf 01.01.2024 (art. 14, lid 1, 7°). De Koning kan evenwel een datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

De ambtenaren van de Algemene administratie van de patrimoniumdocumentatie leveren, hetzij op verzoek van een partij of een rechtverkrijgende ervan, hetzij, ingevolge een beschikking van de vrederechter, op verzoek van een derde die een rechtmatig belang inroept, afschriften of uittreksels af van hun registratieregisters en van geregistreerde akten en verklaringen, alles onverminderd de bepalingen van bijzondere wetten.

Deze afschriften of uittreksels kunnen aan de lasthebbers van de belanghebbenden worden afgeleverd, indien zij van de lastgeving laten blijken.

De aflevering van deze stukken geeft recht op een door de Koning te bepalen retributie.

###### Art. 236/1

(van toepassing vanaf 01.11.2023)

(ingevoegd bij art. 11 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

§ 1. De ambtenaren van de Algemene administratie van de patrimoniumdocumentatie kunnen kosteloos inlichtingen afleveren aan:

1° de administratieve diensten van de federale overheid, de gefedereerde entiteiten, de provincies, de agglomeraties, de federaties van gemeenten, de intercommunales, de gemeenten en de openbare centra voor maatschappelijk welzijn;

2° de parketten en de griffies van de hoven en van alle rechtscolleges;

3° de openbare instellingen of inrichtingen, namelijk de instellingen, maatschappijen, verenigingen, inrichtingen en diensten die de federale overheid, een gefedereerde overheid of een lokale overheid mede beheert, waaraan zo een overheid een waarborg verstrekt, waarop zo een overheid toezicht uitoefent op de werkzaamheden ervan, of waarvan zo een overheid het leidinggevend personeel aanwijst, voordraagt of hun aanstelling goedkeurt.

§ 2. Deze aflevering wordt beperkt tot de inlichtingen die noodzakelijk zijn voor de uitvoering van wettelijke bepalingen.
De verstrekte inlichtingen mogen niet langer worden bewaard dan noodzakelijk is voor de verwezenlijking van met de verwerking van de persoonsgegevens nagestreefde doelstelling.

###### Art. 236/2

(van toepassing vanaf 08.06.2024)

(aangevuld bij art. 79 van de wet van 12.05.2024 (B.S., 29.05.2024). Tekst van toepassing vanaf 08.06.2024 (art. -))

De Koning kan ter uitvoering van dit hoofdstuk:

1° de nadere regels van de aanvraag bepalen, waaronder de vermelding, als de aanvrager er een heeft, van zijn identificatienummer in het Rijksregister van de natuurlijke personen of in de registers van de Kruispuntbank van de sociale zekerheid of in de Kruispuntbank van de ondernemingen;

2° de nadere regels van de aflevering bepalen;

3° onder voorbehoud van de bepalingen van de Archiefwet van 24 juni 1955, de bewaartermijnen en de wijze van bewaring bepalen van de vragen om inlichtingen en van de verstrekte antwoorden.

###### Art. 236bis

(van toepassing vanaf 01.11.2023)

(gewijzigd bij art. 13 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

Hij die, uit welken hoofde ook, optreedt bij de toepassing van de belastingwetten of die toegang heeft tot de ambtsvertrekken van de Algemene Administratie van de Patrimoniumdocumentatie, is buiten het uitoefenen van zijn ambt, verplicht tot de meest volstrekte geheimhouding aangaande alle zaken waarvan hij wegens de uitvoering van zijn opdracht kennis heeft.

Personen die deel uitmaken van diensten of openbare instellingen of inrichtingen waaraan inlichtingen, afschriften of uittreksels afgeleverd werden overeenkomstig de bepalingen van dit hoofdstuk, zijn tot dezelfde geheimhouding verplicht en mogen ze niet gebruiken buiten het kader van de wettelijke bepalingen voor de uitvoering waarvan zij zijn afgeleverd.

De ambtenaren van de Algemene administratie van de patrimoniumdocumentatie, oefenen hun ambt uit wanneer zij overeenkomstig de bepalingen van dit hoofdstuk inlichtingen, afschriften of uittreksels afleveren.

### HOOFDSTUK XVIII - Speciaal recht op de nationaliteit, de adelbrieven en de verzoeken tot verandering van naam

###### Art. 237

(van toepassing vanaf 09.03.2026)

(opgeheven bij art. 30 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

(…)

#### Afdeling I - Nationaliteit

###### Art. 238

(van toepassing vanaf 29.07.2025)

(gewijzigd bij art. 31 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 29.07.2025 (art. 33, lid 2))

Er wordt een recht geheven op de procedures tot verkrijging van de Belgische nationaliteit, die worden bepaald bij hoofdstuk III van het Wetboek van de Belgische nationaliteit met uitzondering van de procedures tot verkrijging van de Belgische nationaliteit op grond van artikel 17 van het Wetboek van de Belgische nationaliteit.

Het recht bedraagt 1000 euro.

Dit recht wordt tot 150 euro verminderd voor de vreemdeling die de hoedanigheid heeft van staatloze in België krachtens de er vigerende internationale overeenkomsten en die zijn aanvraag indient op basis van artikel 19, § 2, van het Wetboek van de Belgische nationaliteit.

Het recht moet gekweten worden vóór de indiening van het verzoek of vóór de aflegging van de verklaring.

Het recht wordt jaarlijks op 1 januari geïndexeerd volgens de volgende formule: basisrecht vermenigvuldigd met de nieuwe index en gedeeld door de beginindex. Het resultaat verkregen ingevolge de indexering wordt afgerond op het hogere tiental euro.

De beginindex is de index van de consumptieprijzen van de maand september 2024 en de nieuwe index is die van de consumptieprijzen van de maand september die elke indexatie voorafgaat.

Uiterlijk in de loop van de maand december van elk jaar wordt het bedrag toepasselijk tijdens het volgende kalenderjaar in het Belgisch Staatsblad gepubliceerd. De Federale Overheidsdienst Financiën vermeldt die inlichting eveneens op zijn webstek.
Procedures tot verkrijging van de Belgische nationaliteit - Publicatie voorgeschreven bij art. 238, laatste lid, W.Reg.: - geïndexeerde bedragen vanaf 01.01.2026: bericht van B.S., 29.12.2025: 1030 euro (z. art. 238, 2de lid) ; aangevuld bij bericht van B.S., 16.03.2026 – ed. 2: 160 euro (z. art. 238, 3de lid).

###### Art. 239

(van toepassing vanaf 03.10.1993)

(opgeheven bij art. 9 van de wet van 06.08.1993 (B.S., 23.09.1993). Tekst van toepassing vanaf 03.10.1993 (art. -))

(…)

###### Art. 240

(van toepassing vanaf 01.02.2000)

(opgeheven bij art. 7, 2° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2). Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Art. 240bis

(van toepassing vanaf 01.02.2000)

(opgeheven bij art. 7, 3° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2). Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Art. 241

(van toepassing vanaf 01.02.2000)

(opgeheven bij art. 7, 4° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2). Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Art. 242

(van toepassing vanaf 01.01.1985)

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S. 12.07.1984). Tekst van toepassing vanaf 01.01.1985 (art. 19))

(…)

###### Art. 243

(van toepassing vanaf 01.01.1985)

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst van toepassing vanaf 01.01.1985 (art. 19))

(…)

###### Art. 244

(van toepassing vanaf 01.02.2000)

(opgeheven bij art. 7, 5° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2). Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Art. 245

(van toepassing vanaf 01.01.1985)

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst van toepassing vanaf 01.01.1985 (art. 19))

(…)

###### Art. 246

(van toepassing vanaf 01.01.1985)

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst van toepassing vanaf 01.01.1985 (art. 19))

(…)

###### Art. 247

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 195 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling II - Open brieven van adeldom en verzoeken tot verandering van naam

###### Art. 248

(van toepassing vanaf 09.03.2026)

(gewijzigd bij art. 26 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Op open brieven van verlening van adeldom of van een hogere adeldomsrang of van opneming onder 's Rijks adel met of zonder titel, wordt er een recht van 740 euro geheven.

De Koning kan bij een met redenen omkleed besluit dat recht verminderen, met dien verstande dat het aldus verminderde recht niet minder dan 490 euro mag bedragen voor de gezamenlijke personen in de open brief bedoeld.

De vermindering kan slechts worden verleend wanneer de begunstigde of een van de begunstigden, of een van hun bloedverwanten in de opgaande of nederdalende lijn, aan het Land buitengewone diensten heeft bewezen van vaderlandslievende, wetenschappelijke, culturele, economische, sociale of humanitaire aard.

###### Art. 249

(van toepassing vanaf 01.07.2024)

(aangevuld bij art. 8 van de wet van 07.01.2024 (B.S., 19.01.2024). Tekst van toepassing vanaf 01.07.2024 (art. 9))

Een recht is verschuldigd wegens de indiening van het verzoek tot verandering van naam bedoeld in artikel 370/3 van het Burgerlijk Wetboek.

Het recht bedraagt 140 euro.

Het recht is niet verschuldigd in geval van een verandering van naam als bedoeld in de artikelen 11bis, 15 en 21 van het Wetboek van de Belgische nationaliteit.

Het recht is niet verschuldigd bij een naamswijziging als bedoeld in artikel 370/4, tweede lid, van het oud Burgerlijk Wetboek.

###### Art. 250

(van toepassing vanaf 01.08.2018)

(gewijzigd bij art. 130 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst van toepassing vanaf 01.08.2018 (art. 136))

In de gevallen bedoeld in artikel 248, eerste lid, en in artikel 249, is elke begunstigde een recht verschuldigd.

De door de kinderen of afstammelingen verschuldigde rechten worden evenwel met de twee vijfden verminderd wanneer aan hetzelfde recht onderworpen vergunningen bij eenzelfde beslissing verleend worden aan een persoon en aan zijn kinderen of afstammelingen waarvan het aantal drie overschrijdt.

###### Art. 251

(van toepassing vanaf 01.08.2018)

(vervangen bij art. 131 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst van toepassing vanaf 01.08.2018 (art. 136))

Wanneer de vergunning tot verandering van naam wordt ingetrokken of vernietigd terwijl de registratierechten reeds geïnd zijn, betaalt de verzoeker, behalve als hij te kwader trouw was, geen rechten meer wanneer het verzoek beoogt rechtstreeks te verhelpen aan deze intrekking of vernietiging.

###### Art. 252

(van toepassing vanaf 01.08.2018)

(gewijzigd bij art. 132 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst van toepassing vanaf 01.08.2018 (art. 136))

Het recht wordt berekend volgens het tarief van kracht op de datum van het besluit tot verheffing in de adelstand, dat aan de ondertekening van de adelbrieven voorafgaat, of op de datum van de indiening van het verzoek tot verandering van naam.

###### Art. 253

(van toepassing vanaf 01.08.2018)

(gewijzigd bij art. 133 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst van toepassing vanaf 01.08.2018 (art. 136))

De in artikel 248 bedoelde open brieven worden geregistreerd, tegen betaling van het recht door de begunstigden, binnen zes maanden na hun datum ten kantore Brussel.

Wordt de registratie gevorderd na het verstrijken van hierboven gestelde termijnen, zoo geeft deze formaliteit aanleiding tot het heffen van en geldboete gelijk aan het recht, onverminderd ditzelve.

###### Art. 254

(van toepassing vanaf 01.08.2018)

(gewijzigd bij art. 134 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst van toepassing van 01.08.2018 (art. 136))

Na betaling van het recht en, gebeurlijk, van de geldboete, wordt vermelding van registratie gesteld op den open brief van adeldom.

Zolang aan de formaliteit van registratie niet is voldaan, mag de open brief van adeldom niet aan begunstigden worden uitgereikt.

#### Afdeling III - Bepaling gemeen aan afdelingen I en II

(gewijzigd bij art. 9 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van toepassing vanaf 01.03.2021 (art. -))

###### Art. 255

(van toepassing vanaf 01.02.1940)

De algemene bepalingen van deze titel betreffende de formaliteit van de registratie, de verplichting van inzageverlening, bewijsmiddelen, verjaring, rechtsvervolgingen en gedingen, moratoire interesten zijn van toepassing in de mate waarin daarvan bij dit hoofdstuk niet wordt afgeweken.

### HOOFDSTUK XIX - Speciale geldboete wegens late neerlegging van aan bekendmaking onderworpen akten van vennootschap

###### Art. 256

(van toepassing vanaf 08.01.2018)

(opgeheven bij art. 28 van de wet van 25.12.2017 (B.S., 29.12.2017 – ed. 1). Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

###### Art. 257

(van toepassing vanaf 08.01.2018)

(opgeheven bij art. 29 van de wet van 25.12.2017 (B.S., 29.12.2017 – ed. 1). Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

###### Art. 258

(van toepassing vanaf 08.01.2018)

(opgeheven bij art. 30 van de wet van 25.12.2017 (B.S., 29.12.2017 – ed. 1). Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

## TITEL II - HYPOTHEEKRECHT

###### Art. 259

(van toepassing vanaf 01.12.2021)
(gewijzigd bij art. 5 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van toepassing vanaf 01.12.2021 (art. 7))

Onder de benaming hypotheekrecht wordt een belasting gevestigd op de inschrijvingen van hypotheken en voorrechten op onroerende goederen.

###### Art. 260

(van toepassing vanaf 30.07.2018)

(gewijzigd bij art. 99 van de wet van 11.07.2018 (B.S., 20.07.2018 – ed. 2). Tekst van toepassing vanaf 30.07.2018 (art. -))

Inschrijving van hypotheek wordt slechts verleend, tegen voorafbetaling door de verzoeker, van de uit dien hoofde verschuldigde retributies en recht.

Het detail en het totaal van de voor recht en retributies ontvangen sommen worden op het inschrijvingsborderel vermeld

De Koning kan deze wijze van vermelding geven aanvullen of wijzigen voor het geval het inschrijvingsborderel op gedematerialiseerde wijze wordt aangeboden.

###### Art. 261

(van toepassing vanaf 01.12.2021)

(vervangen bij art. 6 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van toepassing vanaf 01.12.2021 (art. 7))

Wanneer een inschrijving op verschillende kantoren wordt gevraagd tot zekerheid van één en hetzelfde bedrag, wordt het over dat bedrag verschuldigde recht vastgesteld door het kantoor waar de inschrijving het eerst is gevorderd. Het over dat bedrag geïnde recht dekt de inschrijvingen op de overige kantoren.

Wanneer tot zekerheid van één en hetzelfde bedrag op gedematerialiseerde wijze gelijktijdig een inschrijving wordt gevraagd op verschillende kantoren, wordt het over dat bedrag verschuldigde recht vastgesteld door het kantoor dat bevoegd is voor het goed dat als eerste in het inschrijvingsborderel is vermeld. Het over dat bedrag geïnde recht dekt de inschrijvingen op de overige kantoren.

###### Art. 262

(van toepassing vanaf 01.01.1990)

(gewijzigd bij art. 196 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

Het hypotheekrecht is op 0,30 t.h. gesteld.

###### Art. 263

(van toepassing vanaf 01.02.1940)

Het recht is vereffend op het bedrag in hoofd- en bijkomende sommen waarvoor de inschrijving genomen of hernieuwd wordt.

###### Art. 264

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 en 5, § 7, 2° van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 3° en 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1) err. (B.S., 21.12.2001). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de hogere cent afgerond.

Het in te vorderen recht mag niet minder dan 5 EUR bedragen.

###### Art. 265

(van toepassing vanaf 07.02.2022)

(3°, gewijzigd bij art. 103 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

Zijn vrijgesteld van hypotheekrecht:

1° Inschrijvingen van wettelijke hypotheken en hun vernieuwingen;

2° Inschrijvingen ambtshalve door den Algemene Administratie van de Patrimoniumdocumentatie genomen;

3° Inschrijvingen tot zekerheid van de invordering van belastingen, verschuldigd aan de Staat, gefedereerde entiteiten, provincies, gemeenten, polders en wateringen, en vernieuwingen van die inschrijvingen;

4° Inschrijvingen genomen ten laste van den Staat, van openbare instellingen van den Staat en andere in artikel 161, 1°, aangewezen rechtspersonen, en hun vernieuwingen.

5° De inschrijvingen van de voorrechten en hypotheken opgesteld bij de wet betreffende het herstel van zekere schade veroorzaakt aan private goederen door natuurrampen.

###### Art. 266

(van toepassing vanaf 17.01.1959)

(laatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -)) Er is verjaring:

1° Voor de invordering van hypotheekrechten die op het tijdstip van de inschrijving niet zouden geheven zijn geweest, na twee jaar, te rekenen van den dag der inschrijving;

2° Voor de vordering tot teruggaaf van ten onrechte geheven rechten, na twee jaar, te rekenen van den dag der betaling.

Verjaringen worden gestuit overeenkomstig artikel 2171 en 2172.

###### Art. 267

(van toepassing vanaf 01.02.1940)

Zijn toepasselijk op het hypotheekrecht, de bepalingen van titel I, betreffende de rechtsvervolgingen en gedingen en de moratoire interesten.

## TITEL III - GRIFFIERECHT

### HOOFDSTUK I - VESTIGING VAN DE BELASTING EN VASTSTELLING VAN DE RECHTEN

###### Art. 268

(van toepassing vanaf 01.06.2015)

(gewijzigd bij art. 2 van de wet van 28.04.2015 (B.S., 26.05.2015). Tekst van toepassing vanaf 01.06.2015 (art. 2, 1°, KB van 12.05.2015 (B.S, 26.05.2015))

Onder de benaming van griffierecht wordt een belasting gevestigd op de hiernavolgende in de hoven en rechtbanken gedane verrichtingen:

1° de inschrijving van zaken op de algemene rol, op de rol van de verzoekschriften of op de rol van de vorderingen in kort geding;

2° het opstellen van akten van de griffiers, van vóór hen verleden akten, van zekere akten van de rechters en van de ambtenaren van het openbaar ministerie;

3° het afleveren van uitgiften, kopieën of uittreksels uit akten, vonnissen en arresten en van kopieën van andere stukken die op de griffie worden bewaard.

#### Afdeling I - Rolrecht

###### Art. 2691

(van toepassing vanaf 29.06.2019 (1))

(gewijzigd bij art. 130 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst van toepassing vanaf 29.06.2019 (art. -))

Voor elke zaak die op de algemene rol, in het register van de verzoekschriften of in het register van de vorderingen in kort geding wordt ingeschreven of terug ingeschreven, is er verschuldigd:

1° in de vredegerechten en de politierechtbanken, een recht van 50 euro;

2° in de rechtbanken van eerste aanleg en de ondernemingsrechtbanken, een recht van 165 euro;

3° in de hoven van beroep een recht van 400 euro;

4° in het Hof van Cassatie een recht van 650 euro.

Geen enkel recht wordt geïnd bij de rechtsgedingen voor de beslagrechter of de vrederechter in het kader van de toepassing van artikel 1409, § 1, vierde lid, en 1409, § 1bis, vierde lid, van het Gerechtelijk Wetboek.

De zaken die worden geacht spoedeisend te zijn zoals bedoeld in artikel 1253ter/7 van het Gerechtelijk Wetboek zijn onderworpen aan een eenmalig recht wanneer de nieuwe aanhangigmaking bij de familierechtbank het wijzigen van een vordering waarover deze zich al heeft uitgesproken, tot doel heeft. Dit stelsel wordt uitgebreid tot de maatregelen betreffende de uitoefening van het ouderlijk gezag uitgesproken door de jeugdrechtbank, waarvan de wijziging wordt gevraagd voor de familierechtbank.
(1) Nota:
De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019 en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van het gerechtelijk wetboek teneinde de toegang tot de juridische tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die van toepassing waren vóór de inwerkingtreding van die bepalingen.

###### Art. 2692

(van toepassing vanaf 29.06.2019 (1))

(gewijzigd bij art. 131 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst van toepassing vanaf 29.06.2019 (art. -))

§ 1. De rechter veroordeelt in zijn eindbeslissing de partij of de partijen die het recht verschuldigd zijn tot de betaling ervan of tot betaling van hun deel erin. Tegen de beslissing van de rechter kan geen rechtsmiddel worden aangewend.

Het recht is volledig verschuldigd door de partij die de zaak op de rol heeft doen stellen, behalve indien:
1° de verweerder in het ongelijk wordt gesteld, in welk geval het recht volledig verschuldigd is door de verweerder;

2° de partijen onderscheidenlijk omtrent enig geschilpunt in het ongelijk zijn gesteld, in welk geval het recht ten dele door de eiser en ten dele door de verweerder verschuldigd is, volgens de beslissing van de rechter.

Het recht wordt opeisbaar op de datum van de veroordeling.

§ 2. In geval de zaak op de rol wordt doorgehaald of van de rol wordt weggelaten bij toepassing van artikel 730, § 1 en § 2, a), van het Gerechtelijk Wetboek, is het recht vanaf de datum van de doorhaling of van de weglating opeisbaar ten laste van de partij die de zaak op de rol heeft doen stellen.
(1) Nota:
De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019 en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van het gerechtelijk wetboek teneinde de toegang tot de juridische tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die van toepassing waren vóór de inwerkingtreding van die bepalingen

###### Art. 2693

(van toepassing vanaf 01.02.2019)

(opgeheven bij art. 4 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

(…)
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 2694

(van toepassing vanaf 01.02.2019)

(opgeheven bij art. 5 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

(…)
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 270

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 26 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling Ibis - Opstelrecht

###### Art. 2701

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 98 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

Op akten van griffiers van hoven en rechtbanken, op akten die buiten bemoeiing van rechters vóór hen zijn verleden, wordt een opstelrecht geheven van 35 euro.

Met akten van griffiers van hoven en rechtbanken worden gelijkgesteld, overschrijvingen gedaan door griffiers in hun registers, van de verklaringen van beroep of van voorziening in verbreking strafzaken, door gedetineerden of geïnterneerden afgelegd.

###### Art. 2702

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 99 van de programmawet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

De akten van bekendheid, de akten van aanneming en de akten waarbij een minderjarige machtiging wordt verleend om handel te drijven, die verleden worden ten overstaan van de vrederechters, zijn onderhevig aan een opstelrecht waarvan het bedrag op 35 euro wordt bepaald.

###### Art. 2703

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 100 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

De verklaringen van keus van vaderland zijn onderhevig aan een opstelrecht, waarvan het bedrag op 35 euro wordt bepaald.

Dit recht is vatbaar voor teruggaaf ingeval de inwilliging bij een eindbeslissing van het bevoegd gerecht wordt geweigerd.

#### Afdeling II - Expeditierecht

###### Art. 271

(van toepassing vanaf 01.11.2018)

(2°, gewijzigd bij art. 252 van de wet van 15.04.2018 (B.S., 27.04.2018 – ed. 2). Tekst van toepassing vanaf 01.11.2018 (art.
260). De Koning kan een voorafgaande datum van inwerkingtreding bepalen (art. 260, lid 2))

Op de uitgiften, kopieën of uittreksels die in de griffies worden afgeleverd, wordt een expeditierecht geheven van:

1° 1,75 euro per bladzijde in de vredegerechten en politierechtbanken;

2° 3 euro per bladzijde in de hoven van beroep, de hoven van assisen, het militair gerechtshof, de arrondissementsrechtbanken, de rechtbanken van eerste aanleg, de ondernemingsrechtbanken en de krijgsraden;

3° 5,55 euro per bladzijde in het Hof van Cassatie.

###### Art. 272

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 102 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

Ongeacht op welke griffie en ongeacht op welke informatiedrager de aflevering geschiedt, wordt het recht op 0,85 euro per bladzijde bepaald, zonder dat het verschuldigd bedrag aan rechten lager mag zijn dan 1,75 euro per afgifte op papier en 5,75 euro op een andere drager:

1° voor de niet ondertekende kopieën. Indien echter bij één en hetzelfde verzoek en voor één en dezelfde zaak meer dan twee kopieën worden aangevraagd, wordt het tarief vanaf de derde kopie bepaald op 0,30 euro per bladzijde, zonder dat het globaal bedrag aan verschuldigde expeditierechten alsdan meer dan 1.450 euro kan bedragen;

2° voor uitgiften, kopieën of uittreksels uit de registers van de burgerlijke stand of uit de registers welke de akten betreffende het verkrijgen, het herkrijgen, het behoud en het verlies van nationaliteit bevatten;

3° voor uitgiften, kopieën of uittreksels uit akten, vonnissen en arresten die krachtens artikel 162, 33°bis tot
37°bis, vrijstelling genieten van de formaliteit der registratie;

4° voor de uitgiften, kopieën of uittreksels van akten en stukken betreffende rechtspersonen ingeschreven in de Kruispuntbank van Ondernemingen.
Hetzelfde recht is verschuldigd voor uitgiften, kopieën en uittreksels uit akten, vonnissen en arresten afgeleverd in kieszaken of militiezaken. Deze stukken dragen bovenaan de vermelding van hun bestemming; zij mogen tot geen andere doeleinden dienen.

Hetzelfde recht is eveneens verschuldigd voor de kopie van een elektronisch bestand. Het recht is verschuldigd voor elke gekopieerde elektronische bladzijde van het brondocument. De parameters van het brondocument, die de elektronische bladzijde bepalen, mogen bij het maken van de kopie niet gewijzigd worden.

###### Art. 273

(van toepassing vanaf 07.01.2007)

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006 – ed. 3). Tekst van toepassing vanaf 07.01.2007 (art. -))

Het recht wordt berekend per bladzijde van het arrest, het vonnis of de akte, welke in de uitgifte, de kopie of het uittreksel wordt weergegeven.

Het recht wordt evenwel éénvormig berekend alsof er slechts één bladzijde was, voor de uittreksels die worden afgeleverd ter uitvoering van artikel 121 van het Algemeen Reglement op de gerechtskosten in strafzaken.

###### Art. 274

(van toepassing vanaf 07.01.2007)

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006). Tekst van toepassing vanaf 07.01.2007 (art. -))

Wanneer in een uitgifte, kopie of uittreksel meerdere arresten, vonnissen of akten worden weergegeven, wordt het recht berekend per bladzijde van elk dezer documenten, zonder dat er, voor ieder van deze documenten, minder mag geheven worden dan het recht verschuldigd voor één bladzijde.

###### Art. 274bis

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 103 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

Voor kopieën van audiovisueel materiaal is, ongeacht op welke informatiedrager de kopie wordt afgeleverd, per gekopieerde minuut 1,15 euro verschuldigd, zonder dat de verschuldigde rechten minder mogen bedragen dan 5,75 euro Een begonnen minuut telt voor een volle minuut.

###### Art. 274ter

(van toepassing vanaf 08.07.2012)

(gewijzigd bij art. 104 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -)) De expeditierechten die verschuldigd zijn op één en hetzelfde verzoek voor één en dezelfde zaak, mogen 1 450 euro niet overschrijden.

#### Afdeling III - Legalisatie- en opzoekingsrechten

###### Art. 275

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 276

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling IV - Recht van inschrijving in het handelsregister

###### Art. 277

(van toepassing vanaf 01.07.2003)

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003 – ed. 3). Tekst van toepassing vanaf 01.07.2003 (art. 6))

(…)

###### Art. 278

(van toepassing vanaf 01.07.2003)

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003 – ed. 3). Tekst van toepassing vanaf 01.07.2003 (art. 6))

(…)

### HOOFDSTUK II - Vrijstellingen

###### Art. 2791

(van toepassing vanaf 01.02.2019)

(aangevuld bij art. 6 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

Zijn vrijgesteld van het rolrecht:

1° De inschrijving van zaken waarvan de vonnissen en arresten, krachtens artikelen 161 en 162, vrijstelling genieten van het recht of van de formaliteit der registratie.

Het recht is echter verschuldigd voor de onder artikel 162, 13°, bedoelde procedures;

2° De inschrijving van een zaak door de griffier van het gerecht waarnaar de zaak verwezen werd overeenkomstig de wet op het gebruik der talen in gerechtszaken of ingevolge een rechterlijke beslissing van onttrekking.

3° de inschrijving van zaken die worden gebracht voor de arbeidsgerechten;

4° de inschrijving van zaken die ingeleid worden in het kader van het boek XX van het Wetboek van economisch recht.
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 2792

(van toepassing vanaf 09.03.2026)

(5°, opgeheven bij art. 32 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Zijn vrijgesteld van het opstelrecht:

1° de akten verleden in de gevallen voorzien door artikelen 161 en 162;

2° de akten of ontvangstbewijzen ten blijke van het neerleggen of mededelen van stukken, sommen of voorwerpen ter griffie van de hoven en rechtbanken;

3° de faillissementsbekentenissen, alsmede de afsluitingen of vermeldingen dier worden aangebracht op de registers, titels en stukken tot staving daarvan;

4° (…)

5° (…)

###### Art. 280

(van toepassing vanaf 09.03.2026)
(6°, gewijzigd bij art. 27 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Zijn van expeditierecht vrijgesteld:

1° uitgiften, kopieën of uittreksels van of uit akten, vonnissen en arresten, die krachtens de artikelen 161 en 162 van het recht of van de formaliteit der registratie zijn vrijgesteld.

Deze bepaling is echter niet van toepassing a) op de in artikel 272, laatste alinea, bedoelde uitgiften, kopieën of uittreksels; b) op de uitgiften, afschriften of uittreksels van of uit de in artikel 162, 5°, 13°, 27° en 33°bis tot 37°bis bedoelde akten en vonnissen;

2° de uitgiften, kopieën of uittreksels van of uit vonnissen, arresten, beschikkingen of andere akten van rechtspleging, die de griffier ambtshalve of op verzoek van een der partijen toezendt aan de partijen, aan hun advokaten of aan derden, in uitvoering van het Gerechtelijk Wetboek of van andere wettelijke of reglementaire bepalingen.

3° de kopieën van verklaringen met het oog op de inschrijving of tot wijziging van een inschrijving in het rechtspersonenregister van de Kruispuntbank van Ondernemingen ambtshalve afgegeven of toegezonden aan de personen die de inschrijving of de wijziging aanvragen; de oorzaak van de vrijstelling moet op het kopie vermeld worden;

4° Uitgiften, kopieën of uittreksels uit de registers van de burgerlijke stand of uit de registers welke de akten betreffende het verkrijgen, het herkrijgen, het behoud en het verlies van nationaliteit bevatten.

5° de kopieën of uittreksels van vonnissen en arresten die afgeleverd worden aan juridische tijdschriften, aangewezen door de Minister van Financiën;

6° de uitgiften, kopieën of uittreksels afgegeven door de griffie van het Hof van beroep te Brussel, met het oog op de tenuitvoerlegging in België van de arresten en beschikkingen die een uitvoerbare titel uitmaken en gewezen zijn op grond van de Verdragen betreffende de Europese Unie, betreffende de werking van de Europese unie en tot oprichting van de Europese Gemeenschap voor Atoomenergie, en welke luidens de bewoordingen van die Verdragen vatbaar zijn voor gedwongen tenuitvoerlegging.

7° de grossen of kopieën, afgeleverd door de griffie van het Hof van beroep te Brussel, met het oog op de erkenning en de tenuitvoerlegging in België van de scheidsrechterlijke beslissingen geveld krachtens het Verdrag inzake de beslechting van geschillen met betrekking tot investeringen tussen Staten en onderdanen van andere Staten, opgemaakt te Washington op 18 maart 1965.

8° de kopieën in strafzaken, afgeleverd aan de vader of de moeder, aan een adoptant of aan de voogd in hun hoedanigheid van burgerlijke partij of van persoon die zich op grond van het dossier zou kunnen beroepen op een nadeel, wanneer de zaak betrekking heeft op een misdrijf gepleegd tegen een minderjarige en dat naar de wetten strafbaar is gesteld met een criminele of correctionele straf.
9° de uitvoerbare uitgiften van vonnissen en arresten die aan de partijen worden verstrekt anders dan krachtens een beschikking van de voorzitter van de rechtbank als bedoeld in artikel 1379 van het Gerechtelijk Wetboek.

10° uitgiften, kopieën of uittreksels van een proces-verbaal van minnelijke schikking bedoeld in artikel 733 van het Gerechtelijk Wetboek en dat plaats heeft gevonden:

a) bij gelegenheid van verrichtingen binnen het kader van de wet van 12 juli 1976 betreffende het herstel van zekere schade veroorzaakt aan private goederen door natuurrampen of van de overeenkomstige gewestelijke bepalingen;

b) naar aanleiding van schadelijke gebeurtenissen die als een openbare of landbouwramp worden erkend en waarin het herstel of de schadeloosstelling wordt geregeld door bijzondere wetten of door internationale overeenkomsten.

###### Art. 281

(van toepassing vanaf 01.02.2019)

(opgeheven bij art. 8 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

(…)
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 282

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 211 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

### HOOFDSTUK III - Diverse bepalingen

###### Art. 283

(van toepassing vanaf 01.02.1940)

In de in artikel 160 voorziene gevallen, worden de griffierechten in debet vereffend en ingevorderd volgens de regelen die van toepassing zijn op de onder dezelfde voorwaarden vereffende registratierechten.

###### Art. 284

(van toepassing vanaf 07.01.2007)
(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst van toepassing vanaf 07.01.2007 (art. -))

Worden eveneens in debet vereffend, de griffierechten verschuldigd op uitgiften, kopieën van en uittreksels uit akten, vonnissen en arresten, wanneer die stukken in strafzaken worden afgeleverd aan het openbaar ministerie of aan de Rijksagenten belast met de tenuitvoerlegging van vonnissen en arresten.

De rechten worden onder de gerechtskosten begrepen en als dusdanig ingevorderd ten laste van de partij die er toe veroordeeld werd.

###### Art. 284bis

(van toepassing vanaf 07.01.2007)

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst van toepassing vanaf 07.01.2007 (art. -))

In debet worden eveneens vereffend, de griffierechten verschuldigd op de kopieën in strafzaken die worden afgegeven met toepassing van de artikelen 674bis en volgende van het Gerechtelijk Wetboek. De rechten alsmede de andere kosten worden ingevorderd overeenkomstig de bepalingen van hetzelfde Wetboek.

###### Art. 285

(van toepassing vanaf 01.01.2002)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7,
§ 2), zelf gewijzigd bij art. 42, 5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

De wijze van heffing der griffierechten en het houden der registers in de griffies van de hoven en rechtbanken worden bij koninklijk besluit geregeld.

Daarbij kan de medewerking van de griffies bij de heffing van de griffierechten worden voorzien, zonder dat zij daardoor de hoedanigheid van Staatsrekenplichtige verkrijgen.

Inbreuken op de voorschriften van evenbedoeld koninklijk besluit kunnen worden bestraft met boeten waarvan het bedrag per inbreuk 250 EUR niet mag te boven gaan.

###### Art. 286

(van toepassing vanaf 17.01.1959)

(voorlaatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Er is verjaring:
1° Voor het invorderen der griffierechten en -boeten, na twee jaar, te rekenen van den dag waarop zij aan den Staat verworven zijn;

2° Voor de vordering tot teruggaaf van ten onrechte geheven rechten en boeten, na twee jaar, te rekenen van den dag der betaling.

Die verjaringen worden gestuit overeenkomstig artikel 2171 en 2172.

Verjaring voor het invorderen der in debet vereffende rechten ontstaat echter zoals die voor de onder dezelfde voorwaarden vereffende registratierechten.

###### Art. 287

(van toepassing vanaf 01.02.1940)

De bepalingen van titel I betreffende de vervolgingen en gedingen en de moratoire interesten, zijn toepasselijk op de griffierechten.

###### Art. 288

(van toepassing vanaf 01.02.2019)

(hersteld bij art. 9 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

De Koning kan wat de rolrechten betreft bij een in Ministerraad overlegd besluit de regels bepalen inzake de inning, de verjaringstermijnen, de wijzen waarop de verjaring wordt gestuit of geschorst, de vervolgingen en gedingen en de moratoire interesten en daarbij afwijken van de in artikelen 286 en 287 bepaalde regels. De besluiten die genomen worden in toepassing van dit artikel, worden bekrachtigd door de wet binnen de 12 maanden volgend op de datum van hun bekendmaking in het Belgisch Staatsblad.
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 288bis

(van toepassing vanaf 01.02.2019)

(ingevoegd bij art. 10 van de wet van 14.10.2018 (B.S., 20.12.2018 – ed. 2). Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

De Koning kan bepalen dat wegens de laattijdige betaling van een rolrecht een administratieve boete zal verschuldigd zijn waarvan het bedrag niet minder kan bedragen dan 25 euro en niet hoger mag zijn dan de helft van het recht bepaald in artikel 2691.
De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in art. 2691, eerste lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht vanaf hun datums van inwerkingtreding (art. 28).

TOEKOMSTIG RECHT (vanaf 01.01.2028)

## TITEL       IV    -     DIGITALISATIE            VAN        DE      RELATIES          TUSSEN          DE      FEDERALE

(ingevoegd bij art. 74 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

###### Art. 288ter

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 75 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Voor de toepassing van de bepalingen van dit Wetboek, van de bijzondere wetsbepalingen met betrekking tot de registratie-, hypotheek- en griffierechten of van de ter uitvoering ervan genomen besluiten, wordt verstaan onder:

1° aangetekende zending: hetzij de briefwisseling, al dan niet vergezeld van een ontvangstbevestiging, neergelegd bij de aanbieder van de universele postdienst, een aanbieder van postdiensten of een gekwalificeerde verlener van vertrouwensdiensten die voldoet aan de vereisten van artikel 44 van Verordening (EU) nr. 910 /2014 van het Europees Parlement en de Raad van 23 juli 2014 betreffende elektronische identificatie en vertrouwensdiensten voor elektronische transacties binnen de interne markt en tot intrekking van Richtlijn 1999/93/CE, en al dan niet elektronisch verzonden door een van hen naar een vooraf aangewezen ontvanger, die toelaat om de datum van verzending en ontvangst van de briefwisseling door de bestemmeling aan te tonen, hetzij het bericht dat door de dienst voor het versturen en ontvangen van elektronische berichten door bepaalde overheidsdiensten aangeboden aan de natuurlijke personen of hun vertegenwoordigers door de Federale Overheidsdienst belast met de Digitale Agenda en aan houders van een ondernemingsnummer zoals gedefinieerd in artikel III.16 van het Wetboek van economisch recht of aan hun vertegenwoordigers door de Rijksdienst voor Sociale Zekerheid;

2° beveiligd elektronisch platform: elke computertoepassing ter beschikking gesteld door de Federale elektronische diensten aanbiedt om elektronische berichten uit te wisselen met de Federale Overheidsdienst Financiën op voorwaarde dat de authenticatie en identificatie worden uitgevoerd in toepassing van hoofdstuk 4 van de wet van 18 juli 2017 inzake elektronische identificatie door middel van een stelsel voor elektronische identificatie zoals bedoeld in art. 8., 2., van Verordening (EU) nr. 910/2014 van het Europees Parlement en de Raad van 23 juli 2014 betreffende elektronische identificatie en vertrouwensdiensten voor elektronische transacties in de interne markt en tot intrekking van Richtlijn (EG) 1999/93, dat ten minste een substantieel veiligheidsniveau in de zin van artikel 8., 2., b) van bovengenoemde Verordening inzake de integriteit van de inhoud, de tijdsaanduiding, en zo ook de bewaring van het verzonden bericht garandeert.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288quater

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 76 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, wordt elk bericht aan de Federale ondernemingsnummer, verzonden door middel van een beveiligd elektronisch platform voor zover hij er expliciet voor gekozen heeft om met de Federale Overheidsdienst Financiën langs elektronische weg te communiceren.

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig het eerste lid, wordt elk bericht onder gesloten omslag verzonden.

Wanneer het bericht aan de Federale Overheidsdienst Financiën dat uitgaat van een burger, natuurlijke persoon, die geen houder is van een ondernemingsnummer, betrekking heeft op meerdere burgers en niet al deze burgers expliciet gekozen hebben om langs elektronische weg met de Federale Overheidsdienst Financiën te communiceren, wordt het bericht altijd onder gesloten omslag verzonden naar al deze burgers.

De Koning bepaalt de toepassingsmodaliteiten van de uitwisselingsprocedure van berichten via elektronische weg.

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, wordt elk bericht van de Federale verzonden door middel van een beveiligd elektronisch platform voor zover die er expliciet voor gekozen heeft om met de Federale Overheidsdienst Financiën langs elektronische weg te communiceren.

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig het eerste lid, wordt elk bericht onder gesloten omslag verzonden.

Wanneer het bericht van de Federale Overheidsdienst Financiën aan een burger, natuurlijk persoon, betrekking heeft op meerdere burgers en niet al deze burgers expliciet gekozen hebben om langs elektronische weg met de naar al deze burgers.

§ 3. De keuze van een natuurlijke persoon die geen houder is van een ondernemingsnummer om met de Federale voorafgaande aanvaarding van het elektronische communicatieproces met de Federale Overheidsdienst Financiën door middel van een beveiligd elektronisch platform. Deze voorafgaande en uitdrukkelijke toestemming moet vrij, weloverwogen en ondubbelzinnig zijn. De natuurlijk persoon die geen houder is van een ondernemingsnummer kan zijn instemming op elk moment intrekken. Het bericht zal dan voor de toekomst onder gesloten omslag worden verstuurd en deze intrekking van toestemming zal onmiddellijk van kracht worden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288quinquies

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 77 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, wordt elk bericht aan de Federale door middel van een beveiligd elektronisch platform.

Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, wordt elk bericht van de Federale van een beveiligd elektronisch platform.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288sexies

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 78 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, zal een bericht wanneer dat bericht niet verzonden kan worden door middel van een beveiligd elektronisch platform ingevolge overmacht, worden verzonden onder gesloten omslag.

Wanneer een persoon zich niet heeft kunnen identificeren bij een beveiligd elektronisch platform omdat het beveiligd elektronisch platform technisch niet geconfigureerd is om deze persoon toe te staan er verbinding mee te maken, wordt het bericht eveneens onder gesloten omslag verzonden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288septies

(van toepassing vanaf 01.01.2028)
(ingevoegd bij art. 79 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, wordt elk bericht door een persoon verzonden door middel van een beveiligd elektronisch platform, onmiddellijk ter beschikking gesteld op het beveiligd elektronisch platform van de Federale Overheidsdienst Financiën. De datum van de terbeschikkingstelling geldt als datum van de ontvangst van het bericht door de Federale Overheidsdienst Financiën.

Elk bericht door de Federale Overheidsdienst Financiën verzonden door middel van een beveiligd elektronisch platform bevat in het opschrift van het bericht op het beveiligd elektronisch platform van de Federale

Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen is het, voor elk bericht verzonden of ontvangen door middel van een beveiligd elektronisch platform, de derde werkdag die volgt op de datum van terbeschikkingstelling in het opschrift van het bericht op het beveiligd elektronisch platform van de Federale van de rechten en plichten in dit Wetboek, in de bijzondere wetsbepalingen met betrekking tot de registratie-, hypotheek- en griffierechten of van de tot uitvoering ervan genomen besluiten.

Wanneer een bericht wordt verzonden door de Federale Overheidsdienst Financiën door middel van een beveiligd elektronisch platform en wanneer de datum van terbeschikkingstelling van het bericht in het opschrift van het bericht op het beveiligd elektronisch platform van de Federale Overheidsdienst Financiën en de datum van verzending van het bericht verzonden door middel van een beveiligd elektronisch platform verschillend zijn, zal de datum die het voordeligst is voor de betrokken persoon het vertrekpunt van de termijn zijn.

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen anders bepalen, is het de derde werkdag die volgt op de datum van verzending van het bericht verzonden of ontvangen onder gesloten omslag, die het vertrekpunt zal zijn van de termijnen die van toepassing zijn voor het vervullen van de rechten en plichten in dit Wetboek, in de bijzondere wetsbepalingen met betrekking tot de registratie-, hypotheek- en griffierechten of in de tot uitvoering ervan genomen besluiten.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288octies

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 80 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De rechtsgevolgen van een bericht verzonden door middel van een beveiligd elektronisch platform of onder gesloten omslag zijn dezelfde.
TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288nonies

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 81 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Wanneer een document elektronisch wordt ondertekend door de opsteller of opstellers, gebeurt die ondertekening minstens door middel van een geavanceerde elektronische handtekening in de zin van artikel 3.11. van Verordening (EU) nr. 910/2014 van het Europees Parlement en de Raad van 23 juli 2014 betreffende elektronische identificatie en vertrouwensdiensten voor elektronische transacties in de interne markt en tot intrekking van Richtlijn 1999/93/EG.

Wanneer een document elektronisch wordt ondertekend door middel van het stelsel voor elektronische identificatie aangemeld door België overeenkomstig artikel 9.1. van de Verordening (EU) nr. 910/2014, wordt die ondertekening beschouwd als gekwalificeerd in de zin van artikel 3.12. van die Verordening.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288decies

(van toepassing vanaf 01.01.2028)

(ingevoegd bij art. 82 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Voor de toepassing van artikelen 288quater tot en met 288nonies, wordt verstaan onder "bericht": alle schriftelijke mededelingen betreffende de rechten en plichten opgenomen in dit Wetboek, in de bijzondere wetsbepalingen met betrekking tot de registratie-, hypotheek- en griffierechten of in de ter uitvoering ervan genomen besluiten, inclusief briefwisseling, formulieren en verzendingen van gegevens, ongeacht de gebruikte drager.

GEMEENSCHAPPELIJKE BEPALINGEN VOOR ALLE BELASTINGEN

(gewijzigd bij art. 5 van de wet van 17.08.2013 (B.S., 05.09.2013). Tekst van toepassing vanaf 01.01.2013 (art. 21))

###### Art. 289

(van toepassing vanaf 10.02.2013)
(gewijzigd bij art. 3 van de wet van 14.01.2013 (B.S., 31.01.2013 – ed. 2). Tekst van toepassing vanaf 10.02.2013 (art. -))

§ 1. De bestuursdiensten van de Staat, met inbegrip van de parketten en de griffies der hoven en rechtbanken, de besturen van de provinciën en van de gemeenten, zomede de openbare organismen en instellingen, zijn gehouden, wanneer zij daartoe aangezocht zijn door een ambtenaar van een der Rijksbesturen belast met de aanslag in, of de invordering van de belastingen, hem alle in hun bezit zijnde inlichtingen te verstrekken, hem, zonder verplaatsing van alle in hun bezit zijnde akten, stukken, registers en om 't even welke bescheiden inzage te verlenen en hem alle inlichtingen, afschriften of uittreksels te laten nemen, welke bedoelde ambtenaar ter verzekering van de aanslag in, of de heffing van de door de Staat geheven belastingen nodig acht.

Onder openbare organismen dienen verstaan, naar de geest van deze wet, de instellingen, maatschappijen, verenigingen, inrichtingen en diensten welke de Staat mede beheert, waaraan de Staat een waarborg verstrekt, op welker bedrijvigheid de Staat toezicht uitoefent of waarvan het bestuurspersoneel aangewezen wordt door de regering, op haar voordracht of mits haar goedkeuring.

Van de akten, stukken, registers, bescheiden of inlichtingen in verband met gerechtelijke procedures mag evenwel geen inzage of afschrift worden verleend zonder uitdrukkelijke toelating van het openbaar ministerie.

Alinea 1 is niet van toepassing op het Bestuur der postchecks, het Nationaal Instituut voor de statistiek, noch op de kredietinstellingen. Andere afwijkingen van deze bepaling kunnen worden ingevoerd bij door de Minister van Financiën medeondertekende koninklijke besluiten.

§ 2. Elke inlichting, stuk, proces-verbaal of akte ontdekt of bekomen in het uitoefenen van zijn functie, door een ambtenaar van de Federale Overheidsdienst Financiën, hetzij rechtstreeks, hetzij door tussenkomst van een der hierboven aangeduide diensten, kan door de Staat ingeroepen worden voor het opsporen van elke krachtens de belastingwetten verschuldigde som.

Desondanks kan het aanbieden tot registratie van de processen-verbaal en van de verslagen over expertises betreffende gerechtelijke procedures, het bestuur dan alleen toelaten die akten in te roepen mits het daartoe de in alinea 3 van § 1 bepaalde toelating heeft bekomen.

§ 3. Alle administraties die ressorteren onder de Federale Overheidsdienst Financiën zijn gehouden alle in hun bezit zijnde toereikende, ter zake dienende en niet overmatige inlichtingen ter beschikking te stellen aan alle ambtenaren van deze Overheidsdienst, voorzover die ambtenaren regelmatig belast zijn met de vestiging of de invordering van de belastingen, en voorzover die gegevens bijdragen tot de vervulling van de opdracht van die ambtenaren tot de vestiging of de invordering van eender welke door de Staat geheven belasting.

Elke ambtenaar van de Federale Overheidsdienst Financiën, die wettelijk werd belast met een controle- of onderzoeksopdracht, is van rechtswege gemachtigd alle toereikende, ter zake dienende en niet overmatige inlichtingen te vragen, op te zoeken of in te zamelen die bijdragen tot de vestiging of de invordering van eender welke, andere, door de Staat geheven belasting.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 289bis

(van toepassing vanaf 01.01.2028)

(§ 12, lid 3, gewijzigd bij art. 83 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een ondernemingsnummer, evenals voor natuurlijke personen, op een datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

§ 1. Dit artikel legt de voorschriften en procedures vast voor de samenwerking tussen België en de andere lidstaten van de Europese Unie met het oog op de uitwisseling van inlichtingen die naar verwachting van belang zijn voor de administratie en de handhaving van de nationale wetgeving van alle lidstaten met betrekking tot de registratie-, hypotheek- en griffierechten.

Dit artikel legt tevens de bepalingen vast voor de elektronische uitwisseling van de in het eerste lid bedoelde inlichtingen.

Dit artikel laat de toepassing van de regels inzake wederzijdse rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de verplichtingen van de lidstaten inzake ruimere administratieve samenwerking, welke voortvloeien uit andere rechtsinstrumenten, waaronder bilaterale en multilaterale overeenkomsten.

§ 2. Voor de toepassing van dit artikel wordt verstaan onder:

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari 2011 betreffende de administratieve samenwerking op het gebied van de belastingen en tot intrekking van richtlijn 77/799/EEG;

2° "lidstaat": een lidstaat van de Europese Unie;

3° "centraal verbindingsbureau": het bureau dat als zodanig is aangewezen door de bevoegde autoriteit en belast is met de primaire zorg voor de contacten met de andere lidstaten op het gebied van de administratieve samenwerking;

4° "verbindingsdienst": elk ander bureau dan het centraal verbindingsbureau dat als zodanig is aangewezen door de bevoegde autoriteit om op grond van dit artikel rechtstreeks inlichtingen uit te wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel gemachtigd is door de bevoegde autoriteit om rechtstreeks inlichtingen uit te wisselen;

6° "Belgische bevoegde autoriteit": de door België als zodanig aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de Belgische verbindingsdiensten en de Belgische bevoegde ambtenaren worden eveneens als Belgische bevoegde autoriteit bij delegatie beschouwd;

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere dan België, als zodanig aangewezen autoriteit.
Het centraal verbindingsbureau, de verbindingsdiensten en de bevoegde ambtenaren van deze lidstaat worden eveneens als buitenlandse bevoegde autoriteit bij delegatie beschouwd;

8° "verzoekende autoriteit": het centraal verbindingsbureau, een verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die namens de Belgische of een buitenlandse bevoegde autoriteit om bijstand verzoekt;
9° "aangezochte autoriteit": het centraal verbindingsbureau, een verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die namens de Belgische of een buitenlandse bevoegde autoriteit om bijstand wordt verzocht;

10° "administratief onderzoek": alle door de lidstaten bij het vervullen van hun taken verrichte controles, onderzoeken en acties ter waarborging van de juiste toepassing van de belastingwetgeving;

11° "automatische uitwisseling":

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de systematische mededeling met regelmatige, vooraf vastgestelde tussenpozen zonder voorafgaand verzoek van vooraf bepaalde inlichtingen aan een andere lidstaat;

b) voor de toepassing van alle andere bepalingen van dit artikel, andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3, de systematische mededeling van vooraf bepaalde inlichtingen verstrekt overeenkomstig de punten a) en b)

12° "spontane uitwisseling": het niet-systematisch, te eniger tijd en ongevraagd verstrekken van inlichtingen aan een andere lidstaat;

13° "persoon":

a. een natuurlijk persoon;

b. een rechtspersoon;

c. indien de geldende wetgeving in die mogelijkheid voorziet, een vereniging van personen die bevoegd is rechtshandelingen te verrichten, maar niet de status van rechtspersoon bezit; of

d. een andere juridische constructie, ongeacht de aard of de vorm, met of zonder rechtspersoonlijkheid, die activa, met inbegrip van de daardoor gegenereerde inkomsten, bezit of beheert welke aan belastingen in de zin van de richtlijn zijn onderworpen;

14° "langs elektronische weg": door middel van elektronische apparatuur voor gegevensverwerking - met inbegrip van digitale compressie - en gegevensopslag, met gebruikmaking van kabels, radio, optische technologie of andere elektromagnetische middelen;

15° "CCN-netwerk": het op het gemeenschappelijke communicatienetwerk gebaseerde gemeenschappelijke platform dat de Europese Unie heeft ontwikkeld voor het elektronische berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk akkoord, elke mededeling of enig ander instrument of handeling met soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of hernieuwd, in het kader van een belastingcontrole, en die aan de volgende cumulatieve voorwaarden voldoen:
a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht of deze beslissingen effectief gebruikt worden;

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon of een groep van personen, en voor zover deze persoon of deze groep van personen er zich kan op beroepen;

c) betreft de interpretatie of toepassing van een wettelijke of administratieve bepaling betreffende de handhaving of de toepassing van dit Wetboek en de met de registratie-, hypotheek- en griffierechten verband houdende autonome bepalingen;

d) heeft betrekking op een grensoverschrijdende verrichting en

e) is tot stand gekomen voorafgaand aan de indiening van een belastingaangifte voor het tijdvak waarin de verrichting of reeks verrichtingen of de activiteiten hebben plaatsgevonden.

17° "grensoverschrijdende verrichting" als vermeld in de bepaling onder 16°: een verrichting of reeks van verrichtingen die voldoen aan een of meer van de volgende voorwaarden:

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van verrichtingen fiscaal inwoners van België zijn dat de grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt, gewijzigd of hernieuwd

b) waarbij een van de partijen bij de verrichting of reeks van verrichtingen haar fiscale woonplaats tegelijkertijd in meer dan een rechtsgebied heeft;

c) de verrichtingen of reeks van verrichtingen een grensoverschrijdend effect hebben.

18° "verbonden onderneming", voor de toepassing van paragraaf 6/3: een persoon die gelieerd is met een andere persoon op ten minste één van de volgende wijzen:

a) een persoon neemt deel aan de leiding van een andere persoon waarbij hij invloed van betekenis kan uitoefenen op die andere persoon;

b) een persoon neemt deel aan de zeggenschap over een andere persoon door middel van een deelneming van meer dan 25 % van de stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon door middel van een eigendomsrecht van, rechtstreeks of middellijk, meer dan 25 % van het kapitaal;

d) een persoon heeft recht op 25 % of meer van de winsten van een andere persoon.

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en met d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de winsten van dezelfde persoon, worden alle betrokken personen als verbonden ondernemingen beschouwd.
Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de winsten van meer dan één persoon, worden alle betrokken personen als verbonden ondernemingen beschouwd.

Voor de toepassing van dit punt wordt een persoon die met betrekking tot de stemrechten of het kapitaalbezit van een entiteit samen met een andere persoon optreedt, beschouwd als houder van een deelneming in alle stemrechten of het volledige kapitaalbezit dat die andere persoon in de genoemde entiteit heeft.

Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c) is voldaan door vermenigvuldiging van de deelnemingspercentages door de opeenvolgende niveaus heen. Een persoon die meer dan 50 % van de stemrechten houdt, wordt geacht 100 % te houden.

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in de rechte lijn worden behandeld als één persoon.

19° "gezamenlijke audit": een administratief onderzoek dat gezamenlijk door de bevoegde autoriteiten van twee of meer lidstaten wordt uitgevoerd, en verband houdt met een of meer personen van gezamenlijk of complementair belang voor de bevoegde autoriteiten van die lidstaten;

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot vernietiging, verlies, wijziging of elk voorval van ongepaste of ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen, met inbegrip van, maar niet beperkt tot, persoonsgegevens die worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg van opzettelijke onwettige handelingen, nalatigheid of ongevallen. Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid, de beschikbaarheid en de integriteit van gegevens.

§ 3. De Belgische bevoegde autoriteit wisselt met de buitenlandse bevoegde autoriteiten inlichtingen uit.

§ 4. Met betrekking tot een specifiek geval kan de Belgische bevoegde autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de eerste § vermelde inlichtingen die deze in haar bezit heeft of naar aanleiding van een administratief onderzoek verkregen heeft, te verstrekken. Het verzoek kan een met redenen omkleed verzoek om een bepaald administratief onderzoek in te stellen, omvatten.

De Belgische bevoegde autoriteit kan de aangezochte autoriteit verzoeken haar de originele stukken over te maken.

§ 5. De Belgische bevoegde autoriteit verstrekt op verzoek van een buitenlandse bevoegde autoriteit met betrekking tot een specifiek geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft of naar aanleiding van een administratief onderzoek verkregen heeft, dat werd ingesteld om die inlichtingen te verkrijgen.

In voorkomend geval deelt de Belgische bevoegde autoriteit de verzoekende autoriteit mee op welke gronden zij een administratief onderzoek niet noodzakelijk acht.

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten van het gevraagde administratief onderzoek gaat de Belgische bevoegde autoriteit te werk volgens dezelfde procedures als handelde zij uit eigen beweging of op verzoek van een andere Belgische instantie.
Op specifiek verzoek van de verzoekende autoriteit verstrekt de Belgische bevoegde autoriteit de originele stukken, tenzij de Belgische voorschriften zich hiertegen verzetten.

De inlichtingen worden door de Belgische bevoegde autoriteit zo spoedig mogelijk, doch uiterlijk drie maanden na de datum van ontvangst van het verzoek verstrekt. Indien de Belgische bevoegde autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij deze binnen twee maanden. In bijzondere gevallen kunnen de Belgische bevoegde autoriteit en de verzoekende autoriteit een andere termijn overeenkomen.

De ontvangst van het verzoek wordt door de Belgische bevoegde autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs elektronische weg, bevestigd.

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk een maand na ontvangst van het verzoek, aan de verzoekende autoriteit weten welke tekortkomingen het verzoek vertoont en preciseert welke aanvullende achtergrondinformatie zij verlangt. In dit geval gaan de in het vijfde lid gestelde termijnen in op de datum waarop de Belgische bevoegde autoriteit de aanvullende informatie ontvangt.

Indien de Belgische bevoegde autoriteit niet binnen de gestelde termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van het verzoek, aan de verzoekende autoriteit mee, met vermelding van de datum waarop zij meent aan het verzoek te kunnen voldoen.
Deze termijn mag niet langer zijn dan zes maanden te rekenen vanaf de datum van ontvangst van het verzoek.

Indien de Belgische bevoegde autoriteit niet over de gevraagde inlichtingen beschikt en niet aan het verzoek om inlichtingen kan voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand na ontvangst van het verzoek, aan de verzoekende autoriteit mee.

§ 5/1. Wat betreft een in paragraaf 4 en in paragraaf 5 bedoeld verzoek worden de verzochte inlichtingen geacht van verwacht belang te zijn indien op het ogenblik van het verzoek de verzoekende autoriteit van oordeel is dat er overeenkomstig haar nationale wetgeving een redelijke mogelijkheid bestaat dat de verzochte inlichtingen van belang zullen zijn voor de belastingaangelegenheden van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen, verstrekt de verzoekende autoriteit ten minste de volgende inlichtingen aan de aangezochte autoriteit:

a) het fiscale doel waarvoor de informatie wordt opgevraagd;

b) een specificering van de inlichtingen die nodig zijn voor de uitvoering of handhaving van haar nationale recht.

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op een groep belastingplichtigen die niet individueel kunnen worden geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op basis van een gemeenschappelijke reeks kenmerken.

In dergelijke gevallen, verstrekt de verzoekende autoriteit de volgende informatie aan de aangezochte autoriteit:

a) een gedetailleerde beschrijving van de groep;
b) een toelichting bij de toepasselijke wetgeving en bij de feiten op basis waarvan redelijkerwijze vermoed kan worden dat de belastingplichtigen in de groep de toepasselijke wetgeving niet hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen zouden bijdragen tot het bepalen van de mate waarin de belastingplichtigen in de groep aan hun verplichtingen voldoen;

d) in voorkomend geval, feiten en omstandigheden die verband houden met de tussenkomst van een derde die actief heeft bijgedragen tot de mogelijke niet-naleving van de toepasselijke wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse bevoegde autoriteit automatisch alle inlichtingen waarover zij ten aanzien van ingezetenen van die andere lidstaat beschikt inzake de volgende specifieke inkomsten- en vermogenscategorieën, op te vatten in de zin van de Belgische wetgeving:

a) inkomen uit een dienstbetrekking;

b) tantièmes en presentiegelden;

c) levensverzekeringsproducten die niet vallen onder andere Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch onder soortgelijke voorschriften;

d) pensioenen;

e) eigendom van en inkomsten uit onroerend goed;

f) royalty's;

g) inkomsten uit dividenden zonder bewaarneming, met uitzondering van inkomsten uit dividenden die zijn vrijgesteld van vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn 2011/96/EU van de Raad.

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de verstrekking van de in de eerste alinea genoemde inlichtingen het door de lidstaat van verblijf afgegeven fiscaal identificatienummer (TIN) van ingezetenen.

België stelt de Commissie jaarlijks in kennis van ten minste twee inkomsten- en vermogenscategorieën die zijn opgenomen in de eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over ingezetenen van een andere lidstaat.

België stelt de Commissie vóór 1 januari 2026 in kennis van ten minste vijf categorieën die zijn opgenomen in het eerste lid, ten aanzien waarvan de bevoegde autoriteit van elke andere lidstaat automatisch inlichtingen verstrekt over ingezetenen van die andere lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken die ingaan op of na 1 januari 2026.

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen zes maanden na het verstrijken van het kalenderjaar in de loop waarvan de inlichtingen beschikbaar zijn geworden.
"Beschikbare inlichtingen" betekent inlichtingen die zich in de belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden en die opvraagbaar zijn overeenkomstig de procedures voor het verzamelen en verwerken van inlichtingen in die lidstaat.

§ 6/1. In het kader van de verplichte automatische uitwisseling van inlichtingen over grensoverschrijdende voorafgaande fiscale beslissingen, zijn de voorwaarden de volgende:

1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van deze paragraaf, verstrekt de Belgische bevoegde autoriteit automatisch inlichtingen aan de bevoegde autoriteiten van alle andere lidstaten en de Europese Commissie, overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde praktische modaliteiten wanneer een grensoverschrijdende voorafgaande beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december 2016.

2° de Belgische bevoegde autoriteit verstrekt eveneens, overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde praktische modaliteiten, aan de bevoegde autoriteiten van alle andere lidstaten, evenals aan de Europese Commissie, de inlichtingen over grensoverschrijdende voorafgaande fiscale beslissingen die zijn verstrekt, gewijzigd of hernieuwd binnen de periode beginnend vijf jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in de bepaling onder 6° van deze paragraaf.

Indien de grensoverschrijdende voorafgaande fiscale beslissingen werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en 31 december 2013, worden deze inlichtingen verstrekt op voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.

Als grensoverschrijdende voorafgaande fiscale beslissingen werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31 december 2016, worden die inlichtingen verstrekt ongeacht of die grensoverschrijdende voorafgaande beslissingen al dan niet nog geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin een voorafgaande grensoverschrijdende ruling betrekking heeft op belastingaangelegenheden van een of meer natuurlijke personen, tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1 januari 2026 is afgegeven, gewijzigd of hernieuwd, en:

a) het bedrag van de transactie of reeks transacties van de voorafgaande grensoverschrijdende ruling groter is dan 1.500.000 euro (of het equivalent daarvan in een andere valuta), indien dat bedrag wordt vermeld in de voorafgaande grensoverschrijdende ruling, of;

b) de voorafgaande grensoverschrijdende ruling bepaalt of een persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de ruling afgeeft.

Voor de toepassing van punt a), en onverminderd het in de voorafgaande grensoverschrijdende ruling bedoelde bedrag, omvat het bedrag van de voorafgaande grensoverschrijdende ruling bij een reeks transacties met betrekking tot verschillende goederen, diensten of activa, de totale onderliggende waarde. De bedragen worden niet geaggregeerd indien dezelfde goederen, diensten of activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande grensoverschrijdende rulings inzake bronbelasting op inkomsten uit arbeid, tantièmes en presentiegelden of pensioenen van niet-ingezetenen niet onder de uitwisseling van inlichtingen over voorafgaande grensoverschrijdende rulings met betrekking tot natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:

a) voor de op grond van 1° uitgewisselde inlichtingen: onverwijld zodra de voorafgaande grensoverschrijdende rulings of voorafgaande verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of hernieuwd en uiterlijk binnen drie maanden na het einde van het semester van het kalenderjaar waarin de voorafgaande grensoverschrijdende rulings of voorafgaande verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde inlichtingen: vóór 1 januari 2018.

5° De door de Belgische bevoegde autoriteit uit hoofde van de bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen omvatten de volgende gegevens:

a) de identificatie van de rechtspersoon, tenzij de voorafgaande grensoverschrijdende ruling betrekking heeft op een natuurlijke persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt, en in voorkomend geval de groep personen waartoe die persoon behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen een omschrijving van de relevante zakelijke activiteiten of transacties of reeks van transacties, alsook alle andere inlichtingen die voor de bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of van inlichtingen waarvan het verstrekken in strijd zou zijn met de openbare orde.

c) de data van de aflevering, wijziging of hernieuwing van de grensoverschrijdende voorafgaande fiscale beslissing;

d) de aanvangsdatum van de geldigheidsperiode van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld;

e) de einddatum van de geldigheidsperiode van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;

g) het bedrag van de verrichting of reeks van verrichtingen van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld in de grensoverschrijdende voorafgaande fiscale beslissing;

h) in voorkomend geval, de identificatie van de andere lidstaten die mogelijks betrokken zijn bij de grensoverschrijdende voorafgaande fiscale beslissing;

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling betrekking heeft op een natuurlijke persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die er zijn, waarop de voorafgaande grensoverschrijdende ruling of de voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van invloed zal zijn waarbij vermeld dient te worden met welke lidstaten de getroffen personen verbonden zijn, en

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a), b), en i) van deze paragraaf worden niet medegedeeld aan de Europese Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel en in elk geval niet later dan zeven werkdagen na ontvangst, aan de verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing totdat het in § 24, 3de en 4de lid, bedoelde gegevensbestand operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met inachtneming van de bepalingen van § 24, 2de lid, om aanvullende inlichtingen verzoeken, daaronder begrepen de volledige tekst van een grensoverschrijdende voorafgaande fiscale beslissing.

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen, bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van het eerste lid het fiscaal identificatienummer van de rijksinwoner dat werd afgeleverd door rechtsgebied van verblijf.

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan de commissie mee de statistieken over het volume van de automatische uitwisseling in toepassing van de paragrafen 6 en 6/1, alsook de inlichtingen over de kosten en baten, administratief en andere, verbonden aan de uitwisseling die plaats heeft gevonden, en aan de eventuele wijzigingen, zowel voor de belastingadministraties als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie van de administratieve samenwerking voorzien door dit artikel in het licht van de strijd tegen de fiscale fraude en ontduiking.

De Belgische bevoegde autoriteit controleert en evalueert de efficiëntie van de administratieve samenwerking voorzien door dit artikel, met name wat betreft de strijd tegen de belastingontduiking en deelt de Commissie de resultaten van zijn evaluatie een maal per jaar mee via een formulier en volgens de modaliteiten voorzien door de Commissie.

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde lid bedoelde termijn de in tweede lid bedoelde gegevens inzake grensoverschrijdende constructies, waarvan zij ingelicht is door de intermediair of de relevante belastingplichtige overeenkomstig de artikelen 289bis/1 tot en met 289bis/8, via automatische uitwisseling mee aan de bevoegde autoriteiten van alle andere lidstaten.

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid mee te delen gegevens zijn de volgende, voor zover van toepassing:

1° de identificatiegegevens van intermediairs, en relevante belastingplichtigen, bedoeld in artikel 289bis/1, 4° en
5°, met uitzondering van intermediairs die op grond van het juridisch beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig artikel 289bis/7, met inbegrip van hun naam, geboortedatum en -plaats (in het geval van een natuurlijk persoon), fiscale woonplaats, fiscaal identificatienummer, en, in voorkomend geval, van de personen die overeenkomstig paragraaf 2, 21° een verbonden onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in artikel 289bis/2 op grond waarvan de grensoverschrijdende constructie gemeld moet worden;

3° een samenvatting van de inhoud van de meldingsplichtige grensoverschrijdende constructie, met onder meer de benaming waaronder zij algemeen bekend staat, indien voorhanden, en een beschrijving van de relevante constructies, alsook alle andere inlichtingen die voor de bevoegde autoriteit van belang kunnen zijn bij het beoordelen van een mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking van een handels-, bedrijfs- , nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of van inlichtingen waarvan de onthulling in strijd zou zijn met de openbare orde;

4° de datum waarop de eerste stap voor de implementatie van de meldingsplichtige grensoverschrijdende constructie is of zal worden ondernomen;

5° nadere bijzonderheden van de nationale bepalingen die aan de meldingsplichtige grensoverschrijdende constructie ten grondslag liggen;

6° de waarde van de meldingsplichtige grensoverschrijdende constructie;

7° de lidstaat van de relevante belastingbetaler(s) en eventuele andere lidstaten waarop de meldingsplichtige grensoverschrijdende constructie naar alle waarschijnlijkheid van invloed zal zijn;

8° de identificatiegegevens van andere personen in een lidstaat, op wie de meldingsplichtige grensoverschrijdende constructie naar alle waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met welke lidstaten deze personen verbonden zijn.

De automatische uitwisseling geschiedt binnen één maand te rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020 meegedeeld.

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze paragraaf, worden niet medegedeeld aan de Europese Commissie.

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028, bevat de mededeling van de gegevens betreffende de grensoverschrijdende regelingen het fiscaal identificatienummer van de personen bepaald in het tweede lid, 8°.

§ 7. De Belgische bevoegde autoriteit verstrekt spontaan, in elk van de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de buitenlandse bevoegde autoriteit:

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen dat in de andere lidstaat een derving van belasting kan bestaan;

2° een belastingplichtige verkrijgt in België een vrijstelling of vermindering van belasting die voor hem een belastingplicht of een hogere belasting in de andere lidstaat zou moeten meebrengen;
3° transacties tussen een belastingplichtige in België en een belastingplichtige in een andere lidstaat worden over één of meer andere landen geleid, op zodanige wijze dat daardoor in één van beide of in beide lidstaten een belastingbesparing kan ontstaan;

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen dat er belastingbesparing kan ontstaan door een kunstmatige verschuiving van winsten binnen een groep van ondernemingen;

5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen door een buitenlandse bevoegde autoriteit, hebben informatie opgeleverd die voor de vaststelling van de belastingschuld in die andere lidstaat toereikend, ter zake dienend en niet overmatig is.

De Belgische bevoegde autoriteit kan een buitenlandse bevoegde autoriteit spontaan alle inlichtingen meedelen waarvan zij kennis heeft en die voor deze buitenlandse bevoegde autoriteit toereikend, ter zake dienend en niet overmatig zijn.

De in het eerste lid bedoelde inlichtingen worden door de Belgische bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand nadat deze beschikbaar worden, aan de buitenlandse bevoegde autoriteit van elke betrokken lidstaat verstrekt.

§ 8. De ontvangst van de in § 7 bedoelde inlichtingen wordt door de Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen zeven werkdagen na ontvangst, indien mogelijk langs elektronische weg, aan de verstrekkende buitenlandse bevoegde autoriteit bevestigd.

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in § 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde ambtenaren onder de voorwaarden die zijn vastgesteld door de buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren waar de administratieve autoriteiten van de lidstaat taken vervullen;

2° aanwezig zijn bij administratieve onderzoeken die worden uitgevoerd op het grondgebied van de buitenlandse bevoegde autoriteit;

3° deelnemen aan de administratieve onderzoeken die worden uitgevoerd op het grondgebied van de andere lidstaat, met gebruikmaking van elektronische communicatiemiddelen, in voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen door middel van elektronische communicatiemiddelen, kunnen zij personen ondervragen en bescheiden onderzoeken, onder voorbehoud van de door de buitenlandse bevoegde autoriteit gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde ambtenaren onder de voorwaarden die zijn vastgesteld door de Belgische bevoegde autoriteit mogen:
1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn taken vervult;

2° aanwezig zijn bij administratieve onderzoeken die worden uitgevoerd op Belgisch grondgebied;

3° deelnemen aan de administratieve onderzoeken die worden uitgevoerd op Belgisch grondgebied, met gebruikmaking van elektronische communicatiemiddelen, in voorkomend geval.

De Belgische bevoegde autoriteit antwoordt op het overeenkomstig de eerste alinea ingediende verzoek binnen een termijn van 60 dagen na ontvangst van het verzoek, om haar instemming te bevestigen of haar gemotiveerde weigering aan de buitenlandse bevoegde autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden waartoe de ambtenaren van de Belgische bevoegde autoriteit toegang hebben, ontvangen de ambtenaren van de verzoekende autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn tijdens een administratief onderzoek of daaraan deelnemen met gebruikmaking van elektronische communicatiemiddelen, mogen zij personen ondervragen en bescheiden onderzoeken, onder de voorwaarden die zijn vastgesteld door de Belgische bevoegde autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking heeft, om de controlemaatregelen van de ambtenaren van de verzoekende autoriteit na te leven, wordt door de Belgische bevoegde autoriteit beschouwd als een weigering tegenover haar eigen ambtenaren.

De door de verzoekende lidstaat gemachtigde ambtenaren die overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en hun officiële hoedanigheid worden vermeld.

§ 11. In de gevallen waarin België met één of meer lidstaten overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of meer personen te wier aanzien zij een gezamenlijk of complementair belang hebben, controles te verrichten en de aldus verkregen inlichtingen uit te wisselen, is deze § van toepassing.

De Belgische bevoegde autoriteit bepaalt autonoom welke personen zij voor een gelijktijdige controle wil voorstellen. Zij deelt de buitenlandse bevoegde autoriteit van de betrokken lidstaten met opgave van redenen mee welke dossiers zij voor een gelijktijdige controle voorstelt. Zij bepaalt binnen welke termijn de controle moet plaatsvinden.

Wanneer aan de Belgische bevoegde autoriteit een gelijktijdige controle wordt voorgesteld, beslist zij of ze aan de gelijktijdige controle wenst deel te nemen. Zij doet de buitenlandse bevoegde autoriteit die de controle voorstelt een bevestiging van deelname of een gemotiveerde weigering toekomen binnen een termijn van 60 dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan die wordt belast met de leiding en de coördinatie van de controle.

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het verzoek om een gezamenlijke audit binnen een termijn van 60 dagen, te rekenen vanaf de ontvangst van het verzoek en motiveert haar beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd door de bevoegde autoriteit van de verzoekende lidstaat, door de Belgische bevoegde autoriteit, en in voorkomend geval, door de bevoegde autoriteiten van de andere aangezochte lidstaten en in overeenstemming met de Belgische wetgeving en procedurele voorschriften. De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die deelnemen aan de gezamenlijke audit op Belgisch grondgebied, worden vastgesteld overeenkomstig de Belgische wetgeving. Tegelijk met het naleven van die wetgeving, oefenen de ambtenaren van een andere lidstaat geen bevoegdheden uit die verder zouden gaan dan de bevoegdheden die hun krachtens de wetgeving van hun lidstaat zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd om personen te ondervragen en bescheiden te onderzoeken in samenspraak met de ambtenaren van de Belgische bevoegde autoriteit, met inachtneming van de in België bepaalde procedurele regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de activiteiten van de gezamenlijke audit is verzameld, worden beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde juridische voorwaarden als in het geval van een klassieke audit, uitgevoerd in België door Belgische ambtenaren, onder meer in de loop van een bezwaar-, herzienings- of beroepsprocedures.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, genieten personen die aan een gezamenlijke audit worden onderworpen of erdoor worden geraakt, dezelfde rechten en hebben ze dezelfde plichten als in het geval van een klassieke audit waaraan alleen Belgische ambtenaren deelnemen, onder meer in de loop van een bezwaar-, herzienings- of beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van een of meer lidstaten een gezamenlijke audit verrichten, trachten zij het eens te worden over de feiten en omstandigheden die relevant zijn voor de gezamenlijke audit, en streven zij naar overeenstemming over de fiscale positie van de geaudite persoon of personen op basis van de resultaten van de gezamenlijke audit. De bevindingen van de gezamenlijke audit worden neergelegd in een eindverslag. Punten waarover de bevoegde autoriteiten het eens zijn, worden in de conclusies van het eindverslag opgenomen en worden in aanmerking genomen in de relevante instrumenten die de bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 11/2. De Belgische bevoegde autoriteit kan de bevoegde autoriteit van een andere of meerdere lidstaten verzoeken een gezamenlijke audit uit te voeren.
Gezamenlijke audits worden op vooraf overeengekomen en gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd door de betrokken bevoegde autoriteiten, en in overeenstemming met de wetgeving en de procedurele voorschriften van de lidstaat waar de activiteiten van de gezamenlijke audit plaatsvinden.

De rechten en plichten van de Belgische ambtenaren die deelnemen aan de gezamenlijke audit op het grondgebied van een andere lidstaat, worden vastgesteld overeenkomstig de wetgeving van die lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de Belgische ambtenaren geen bevoegdheden uit die verder zouden gaan dan de bevoegdheden die hun krachtens de Belgische wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het grondgebied van een andere lidstaat, kan het bewijsmateriaal dat tijdens de activiteiten van de gezamenlijke audit is verzameld, worden beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde juridische voorwaarden als in het geval van een klassieke audit uitgevoerd in België door Belgische ambtenaren.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van een of meerdere andere lidstaten een gezamenlijke audit verrichten, trachten zij het eens te worden over de feiten en omstandigheden die relevant zijn voor de gezamenlijke audit, en streven zij naar overeenstemming over de fiscale positie van de geaudite persoon of personen op basis van de resultaten van de gezamenlijke audit. De bevindingen van de gezamenlijke audit worden neergelegd in een eindverslag. De punten waarover de bevoegde autoriteiten het eens zijn, worden in de conclusies van het eindverslag opgenomen en worden in aanmerking genomen in de relevante instrumenten die de bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het resultaat van de gezamenlijke audit en krijgen een kopie van het eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 12. De Belgische bevoegde autoriteit kan een verzoek aan een buitenlandse bevoegde autoriteit richten tot kennisgeving aan de geadresseerde, overeenkomstig de in de aangezochte lidstaat geldende voorschriften voor de kennisgeving van soortgelijke akten, van alle door de Belgische administratieve overheden afgegeven akten en besluiten die betrekking hebben op de toepassing in België van wetgeving betreffende registratie-, hypotheek- en griffierechten.

Het verzoek tot kennisgeving vermeldt de naam en het adres van de geadresseerde, evenals alle overige informatie ter identificatie van de geadresseerde, en het onderwerp van de akte of het besluit waarvan de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde autoriteit slechts gedaan indien de kennisgeving van de akten niet volgens de Belgische regels kan geschieden, of buitensporige problemen zou veroorzaken. De Belgische bevoegde autoriteit kan een document, met een aangetekende zending of langs elektronische weg, rechtstreeks ter kennis brengen aan een persoon op het grondgebied van een andere lidstaat.

§ 13. Op verzoek van een buitenlandse bevoegde autoriteit gaat de Belgische bevoegde autoriteit, overeenkomstig de Belgische voorschriften voor de kennisgeving van soortgelijke akten, over tot kennisgeving aan de geadresseerde van alle door de administratieve overheden van de verzoekende lidstaat afgegeven akten en besluiten die betrekking hebben op de toepassing op haar grondgebied van wetgeving betreffende registratie-, hypotheek- en griffierechten.
De Belgische bevoegde autoriteit stelt de verzoekende autoriteit onverwijld in kennis van het aan het verzoek gegeven gevolg en, in het bijzonder, van de datum waarop de akte of het besluit aan de geadresseerde ter kennis is gebracht.

§ 14. Indien een buitenlandse bevoegde autoriteit inlichtingen overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding betreffende de ontvangen inlichtingen verzoekt, doet de ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen aan de Belgische voorschriften inzake beroepsgeheim en gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie maanden nadat het resultaat van het gebruik van de verlangde inlichtingen bekend is, een terugmelding aan de buitenlandse bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar, overeenkomstig bilateraal overeengekomen praktische afspraken, een terugmelding over de automatische inlichtingenuitwisseling naar de betrokken lidstaten.

§ 15. De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7 inlichtingen heeft verstrekt, kan de ontvangende buitenlandse bevoegde autoriteit om terugmelding betreffende de ontvangen inlichtingen verzoeken.

§ 16. De Belgische verbindingsdienst of de Belgische bevoegde ambtenaar die een verzoek om samenwerking ontvangt dat een optreden vereist buiten de hem krachtens de Belgische wetgeving of het Belgische beleid verleende bevoegdheid, geeft het verzoek onmiddellijk door aan het Belgisch centraal verbindingsbureau en stelt de verzoekende buitenlandse bevoegde autoriteit hiervan in kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat het verzoek aan het Belgisch centraal verbindingsbureau is doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in enigerlei vorm of volgens dit artikel, vallen onder de geheimhoudingsplicht en genieten de bescherming waarin het nationale recht van de ontvangende lidstaat met betrekking tot soortgelijke inlichtingen voorziet.

Deze inlichtingen mogen worden gebruikt:

1° voor de vaststelling, de toepassing en de handhaving van het nationale recht met betrekking tot de in artikel 2 van de richtlijn bedoelde belastingen, alsmede de btw, andere indirecte belastingen, douanerechten, de bestrijding van het witwassen van geld en van de financiering van terrorisme;

2° voor de vestiging en de invordering van de andere belastingen en rechten met betrekking tot artikel 3 van de wet van 9 januari 2012 houdende omzetting van Richtlijn 2010/24/EU van de Raad van 16 maart 2010 betreffende de wederzijdse bijstand inzake de invordering van schuldvorderingen die voortvloeien uit belastingen, rechten en andere maatregelen, en voor het vestigen en invorderen van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op de fiscale wetgeving, onverminderd algemene regels en wettelijke bepalingen die de rechten van beklaagden en getuigen in het kader van dergelijke procedures beheersen.

Met de toestemming van de buitenlandse bevoegde autoriteit die de inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor zover dat toegelaten is door de Belgische wetgeving, kunnen de ontvangen inlichtingen en documenten ontvangen van deze autoriteit worden gebruikt voor andere doeleinden dan deze bedoeld in het tweede lid.
De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en documenten zonder de in de derde lid van deze paragraaf bedoelde toestemming ook gebruiken voor elk doel dat onder een op artikel 215 van het Verdrag betreffende de werking van de Europese Unie gebaseerde handeling valt en deze daartoe delen met de bevoegde autoriteit die verantwoordelijk is voor beperkende maatregelen in de betrokken lidstaat.

De Belgische bevoegde autoriteit die van oordeel is dat de van de bevoegde autoriteit van een andere lidstaat verkregen inlichtingen de bevoegde autoriteit van een derde lidstaat van nut kunnen zijn voor de in het tweede lid beoogde doelen, mag de inlichtingen aan deze autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit van de inlichtingen verstrekkende lidstaat in kennis stelt van haar voornemen om die inlichtingen met een derde lidstaat te delen en op voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel vastgelegde regels en procedures. De inlichtingen verstrekkende lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na de datum van ontvangst van de kennisgeving van de lidstaat die de inlichtingen wenst te delen.

§ 18. De Belgische bevoegde autoriteit kan het gebruik toestaan van de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid, bedoelde doeleinden.
De Belgische bevoegde autoriteit verleent toestemming indien de inlichtingen in België voor soortgelijke doeleinden kunnen worden gebruikt.

De Belgische bevoegde autoriteit deelt aan de bevoegde autoriteiten van alle andere lidstaten een lijst mee van andere dan in paragraaf 1 bedoelde doeleinden waarvoor overeenkomstig haar nationale recht, de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen inlichtingen en bescheiden zonder de in het eerste lid bedoelde toestemming gebruiken voor alle doeleinden die de Belgische bevoegde autoriteit heeft opgenoemd.

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit België die door een buitenlandse bevoegde autoriteit aan een buitenlandse bevoegde autoriteit van een derde lidstaat werden doorgegeven, in die derde lidstaat toestaan.

§ 19. Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te komen.

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op voorwaarde dat de buitenlandse bevoegde autoriteit eerst de inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in de gegeven omstandigheden kon aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te komen.

§ 20. Het is de Belgische bevoegde autoriteit niet toegelaten onderzoek in te stellen of inlichtingen te verstrekken wanneer de Belgische wetgeving haar niet toestaat voor eigen doeleinden het onderzoek in te stellen of de gevraagde inlichtingen te verzamelen.

De Belgische bevoegde autoriteit kan weigeren inlichtingen te verstrekken indien:

1° de verzoekende lidstaat, op juridische gronden, soortgelijke inlichtingen niet kan verstrekken;
2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of indien het inlichtingen betreft waarvan de onthulling in strijd zou zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee op welke gronden zij het verzoek om inlichtingen afwijst.

§ 21. De Belgische bevoegde autoriteit wendt de middelen aan waarover zij beschikt om de gevraagde inlichtingen te verzamelen, zelfs indien zij de inlichtingen niet voor eigen belastingdoeleinden nodig heeft. Deze verplichting geldt onverminderd § 20, eerste en tweede lid, die, wanneer er een beroep op wordt gedaan, in geen geval zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te verstrekken uitsluitend omdat België geen binnenlands belang bij deze inlichtingen heeft.

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat de Belgische bevoegde autoriteit kan weigeren inlichtingen te verstrekken, uitsluitend op grond dat deze berusten bij een bank, een andere financiële instelling, een gevolmachtigde of een persoon die als vertegenwoordiger of trustee optreedt, of dat zij betrekking hebben op eigendomsbelangen in een persoon.

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit weigeren de gevraagde inlichtingen toe te zenden indien deze betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de toezending van de inlichtingen geweigerd had kunnen worden op grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom was verzocht vóór 11 maart 2011.

§ 22. Indien de Belgische overheid voorziet in een samenwerking met een derde land welke verder reikt dan de bij de richtlijn geregelde samenwerking, kan de Belgische overheid de verderreikende samenwerking niet weigeren aan een andere lidstaat die met haar deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken die zijn ingediend op grond van § 4, alsook de antwoorden op grond van § 5, de ontvangstbevestigingen, de verzoeken om inlichtingen van algemene aard en de verklaringen van ongeschiktheid of weigering krachtens § 5 worden, voor zover mogelijk, overgemaakt door middel van een door de Commissie goedgekeurd standaardformulier. Er mogen rapporten, certificaten en andere bescheiden, of andere voor eensluidend verklaarde afschriften of uittreksels daarvan bij de standaardformulieren gevoegd worden.

De in het eerste lid bedoelde standaardformulieren bevatten ten minste de volgende gegevens, die de verzoekende autoriteit moet verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle is ingesteld en, in het geval van vragen betreffende een groep zoals bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;

b) het fiscale doel van de gevraagde informatie.

De Belgische bevoegde autoriteit kan, voor zover bekend en in overeenstemming met de ontwikkeling van de internationale situatie, de namen en adressen verstrekken van alle personen van wie er redenen zijn om aan te nemen dat ze in het bezit zijn van de gevraagde informatie, alsook alle elementen die het verzamelen van informatie door de aangezochte autoriteit kunnen vergemakkelijken.
De spontane gegevensuitwisseling en de desbetreffende ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8, verzoeken tot administratieve kennisgeving op grond van §§ 12 en 13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden overgemaakt door middel van de door de Commissie goedgekeurde standaardformulieren.

De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1 wordt verricht in een geautomatiseerd standaardformaat dat ontworpen is om die automatische uitwisseling te vergemakkelijken en dat is goedgekeurd door de Commissie.

§ 24. De krachtens dit artikel verstrekte inlichtingen worden voor zover mogelijk verzonden langs elektronische weg, via het CCN-netwerk.

Het verzoek om samenwerking, waaronder het verzoek tot kennisgeving en de bijgevoegde bescheiden kunnen in elke door de aangezochte en de verzoekende autoriteit overeengekomen taal zijn gesteld. Slechts in bijzondere gevallen en mits het verzoek met redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken het verzoek vergezeld te laten gaan van een vertaling in één van de officiële talen van België.

Om te voldoen aan de automatische uitwisseling als bedoeld in § 6/1, 1° en 2°, te verstrekken inlichtingen, worden de gegevens die moeten worden meegedeeld opgeslagen in een beveiligd centraal gegevensbestand betreffende de administratieve samenwerking op belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter beschikking gesteld door de Commissie uiterlijk op 31 december 2017. De Belgische bevoegde autoriteiten hebben toegang tot de in dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde automatische uitwisseling van gegevens, volgens lid 1 van deze paragraaf en de toepasselijke praktische modaliteiten.

§ 25. De Belgische bevoegde autoriteit die van een derde land inlichtingen ontvangt welke naar verwachting van belang zijn voor haar administratie en de handhaving van de Belgische wetgeving betreffende registratie-, hypotheek- en griffierechten, kan deze inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan elke buitenlandse bevoegde autoriteit die erom verzoekt, mits dat krachtens een overeenkomst met dat derde land is toegestaan.

De Belgische bevoegde autoriteit kan, met inachtneming van de wet van 8 december 1992 tot bescherming van de persoonlijke levenssfeer ten opzichte van de verwerking van persoonsgegevens en de wet van 3 augustus 2012 houdende bepalingen betreffende de verwerking van persoonsgegevens door de Federale Overheidsdienst Financiën in het kader van zijn opdrachten, de overeenkomstig dit artikel ontvangen inlichtingen doorgeven aan een derde land, op voorwaarde dat aan elk van de volgende voorwaarden is voldaan:

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de inlichtingen afkomstig zijn, heeft daarin toegestemd;

b) het derde land heeft zich ertoe verbonden de medewerking te verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent het ongeoorloofde of onwettige karakter van verrichtingen die blijken in strijd te zijn met of een misbruik te vormen van de belastingwetgeving.
§ 26. Rapporterende financiële instellingen, intermediairs, rapporterende platformexploitanten en de Belgische bevoegde autoriteit worden als verwerkingsverantwoordelijken beschouwd wanneer zij, alleen of gezamenlijk, de doelen en middelen van de verwerking van persoonsgegevens bepalen in de zin van Verordening (EU) 2016/679 van het Europees Parlement en de Raad van 27 april 2016 betreffende de bescherming van natuurlijke personen in verband met de verwerking van persoonsgegevens en betreffende het vrije verkeer van die gegevens en tot intrekking van Richtlijn 95/46/EG.

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in kennis van elke gegevensinbreuk en alle daaropvolgende corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen met de lidstaat of de lidstaten waar de gegevensinbreuk heeft plaatsgevonden, schorsen door de Commissie en de betrokken lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een dergelijke schorsing wordt onmiddellijk van kracht.

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn, indien de gegevensinbreuk niet onmiddellijk en op passende wijze onder controle kan worden gebracht. Op een dergelijk verzoek schorst de Commissie de toegang van die lidstaat of lidstaten tot het CCN-netwerk voor de toepassing van de richtlijn.

De Belgische bevoegde autoriteit stelt, in geval van een gegevensinbreuk, de Commissie op de hoogte wanneer zij deze inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is verholpen, geeft de Commissie pas na die verificatie de betrokken lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de toepassing van de richtlijn.

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in het centrale gegevensbestand of het CCNnetwerk plaatsvindt die nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen door de lidstaten via het CCN-netwerk, stelt de Commissie de lidstaten zonder onnodige vertraging in kennis van de gegevensinbreuk en van eventuele corrigerende maatregelen die zijn genomen. Zulke corrigerende maatregelen kunnen inhouden dat de toegang tot het centrale gegevensbestand of het CCN-netwerk voor de toepassing van de richtlijn wordt geschorst totdat de gegevensinbreuk is verholpen.
- in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.
- in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.
- in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.
- in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.

###### Art. 289bis

(van toepassing vanaf 11.04.2026)

(§§ 6, 6/1, 6/2, 6/3, gewijzigd en § 17, vervangen bij art. 28 van de wet van 16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))
§ 1. Dit artikel legt de voorschriften en procedures vast voor de samenwerking tussen België en de andere lidstaten van de Europese Unie met het oog op de uitwisseling van inlichtingen die naar verwachting van belang zijn voor de administratie en de handhaving van de nationale wetgeving van alle lidstaten met betrekking tot de registratie-, hypotheek- en griffierechten.

Dit artikel legt tevens de bepalingen vast voor de elektronische uitwisseling van de in het eerste lid bedoelde inlichtingen.

Dit artikel laat de toepassing van de regels inzake wederzijdse rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de verplichtingen van de lidstaten inzake ruimere administratieve samenwerking, welke voortvloeien uit andere rechtsinstrumenten, waaronder bilaterale en multilaterale overeenkomsten.

§ 2. Voor de toepassing van dit artikel wordt verstaan onder:

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari 2011 betreffende de administratieve samenwerking op het gebied van de belastingen en tot intrekking van richtlijn 77/799/EEG;

2° "lidstaat": een lidstaat van de Europese Unie;

3° "centraal verbindingsbureau": het bureau dat als zodanig is aangewezen door de bevoegde autoriteit en belast is met de primaire zorg voor de contacten met de andere lidstaten op het gebied van de administratieve samenwerking;

4° "verbindingsdienst": elk ander bureau dan het centraal verbindingsbureau dat als zodanig is aangewezen door de bevoegde autoriteit om op grond van dit artikel rechtstreeks inlichtingen uit te wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel gemachtigd is door de bevoegde autoriteit om rechtstreeks inlichtingen uit te wisselen;

6° "Belgische bevoegde autoriteit": de door België als zodanig aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de Belgische verbindingsdiensten en de Belgische bevoegde ambtenaren worden eveneens als Belgische bevoegde autoriteit bij delegatie beschouwd;

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere dan België, als zodanig aangewezen autoriteit.
Het centraal verbindingsbureau, de verbindingsdiensten en de bevoegde ambtenaren van deze lidstaat worden eveneens als buitenlandse bevoegde autoriteit bij delegatie beschouwd;

8° "verzoekende autoriteit": het centraal verbindingsbureau, een verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die namens de Belgische of een buitenlandse bevoegde autoriteit om bijstand verzoekt;

9° "aangezochte autoriteit": het centraal verbindingsbureau, een verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die namens de Belgische of een buitenlandse bevoegde autoriteit om bijstand wordt verzocht;

10° "administratief onderzoek": alle door de lidstaten bij het vervullen van hun taken verrichte controles, onderzoeken en acties ter waarborging van de juiste toepassing van de belastingwetgeving;
11° "automatische uitwisseling":

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de systematische mededeling met regelmatige, vooraf vastgestelde tussenpozen zonder voorafgaand verzoek van vooraf bepaalde inlichtingen aan een andere lidstaat;

b) voor de toepassing van alle andere bepalingen van dit artikel, andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3, de systematische mededeling van vooraf bepaalde inlichtingen verstrekt overeenkomstig de punten a) en b)

12° "spontane uitwisseling": het niet-systematisch, te eniger tijd en ongevraagd verstrekken van inlichtingen aan een andere lidstaat;

13° "persoon":

a. een natuurlijk persoon;

b. een rechtspersoon;

c. indien de geldende wetgeving in die mogelijkheid voorziet, een vereniging van personen die bevoegd is rechtshandelingen te verrichten, maar niet de status van rechtspersoon bezit; of

d. een andere juridische constructie, ongeacht de aard of de vorm, met of zonder rechtspersoonlijkheid, die activa, met inbegrip van de daardoor gegenereerde inkomsten, bezit of beheert welke aan belastingen in de zin van de richtlijn zijn onderworpen;

14° "langs elektronische weg": door middel van elektronische apparatuur voor gegevensverwerking - met inbegrip van digitale compressie - en gegevensopslag, met gebruikmaking van kabels, radio, optische technologie of andere elektromagnetische middelen;

15° "CCN-netwerk": het op het gemeenschappelijke communicatienetwerk gebaseerde gemeenschappelijke platform dat de Europese Unie heeft ontwikkeld voor het elektronische berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk akkoord, elke mededeling of enig ander instrument of handeling met soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of hernieuwd, in het kader van een belastingcontrole, en die aan de volgende cumulatieve voorwaarden voldoen:

a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht of deze beslissingen effectief gebruikt worden;

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon of een groep van personen, en voor zover deze persoon of deze groep van personen er zich kan op beroepen;
c) betreft de interpretatie of toepassing van een wettelijke of administratieve bepaling betreffende de handhaving of de toepassing van dit Wetboek en de met de registratie-, hypotheek- en griffierechten verband houdende autonome bepalingen;

d) heeft betrekking op een grensoverschrijdende verrichting en

e) is tot stand gekomen voorafgaand aan de indiening van een belastingaangifte voor het tijdvak waarin de verrichting of reeks verrichtingen of de activiteiten hebben plaatsgevonden.

17° "grensoverschrijdende verrichting" als vermeld in de bepaling onder 16°: een verrichting of reeks van verrichtingen die voldoen aan een of meer van de volgende voorwaarden:

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van verrichtingen fiscaal inwoners van België zijn dat de grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt, gewijzigd of hernieuwd

b) waarbij een van de partijen bij de verrichting of reeks van verrichtingen haar fiscale woonplaats tegelijkertijd in meer dan een rechtsgebied heeft;

c) de verrichtingen of reeks van verrichtingen een grensoverschrijdend effect hebben.

18° "verbonden onderneming", voor de toepassing van paragraaf 6/3: een persoon die gelieerd is met een andere persoon op ten minste één van de volgende wijzen:

a) een persoon neemt deel aan de leiding van een andere persoon waarbij hij invloed van betekenis kan uitoefenen op die andere persoon;

b) een persoon neemt deel aan de zeggenschap over een andere persoon door middel van een deelneming van meer dan 25 % van de stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon door middel van een eigendomsrecht van, rechtstreeks of middellijk, meer dan 25 % van het kapitaal;

d) een persoon heeft recht op 25 % of meer van de winsten van een andere persoon.

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en met d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de winsten van dezelfde persoon, worden alle betrokken personen als verbonden ondernemingen beschouwd.

Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de winsten van meer dan één persoon, worden alle betrokken personen als verbonden ondernemingen beschouwd.

Voor de toepassing van dit punt wordt een persoon die met betrekking tot de stemrechten of het kapitaalbezit van een entiteit samen met een andere persoon optreedt, beschouwd als houder van een deelneming in alle stemrechten of het volledige kapitaalbezit dat die andere persoon in de genoemde entiteit heeft.
Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c) is voldaan door vermenigvuldiging van de deelnemingspercentages door de opeenvolgende niveaus heen. Een persoon die meer dan 50 % van de stemrechten houdt, wordt geacht 100 % te houden.

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in de rechte lijn worden behandeld als één persoon.

19° "gezamenlijke audit": een administratief onderzoek dat gezamenlijk door de bevoegde autoriteiten van twee of meer lidstaten wordt uitgevoerd, en verband houdt met een of meer personen van gezamenlijk of complementair belang voor de bevoegde autoriteiten van die lidstaten;

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot vernietiging, verlies, wijziging of elk voorval van ongepaste of ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen, met inbegrip van, maar niet beperkt tot, persoonsgegevens die worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg van opzettelijke onwettige handelingen, nalatigheid of ongevallen. Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid, de beschikbaarheid en de integriteit van gegevens.

§ 3. De Belgische bevoegde autoriteit wisselt met de buitenlandse bevoegde autoriteiten inlichtingen uit.

§ 4. Met betrekking tot een specifiek geval kan de Belgische bevoegde autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de eerste § vermelde inlichtingen die deze in haar bezit heeft of naar aanleiding van een administratief onderzoek verkregen heeft, te verstrekken. Het verzoek kan een met redenen omkleed verzoek om een bepaald administratief onderzoek in te stellen, omvatten.

De Belgische bevoegde autoriteit kan de aangezochte autoriteit verzoeken haar de originele stukken over te maken.

§ 5. De Belgische bevoegde autoriteit verstrekt op verzoek van een buitenlandse bevoegde autoriteit met betrekking tot een specifiek geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft of naar aanleiding van een administratief onderzoek verkregen heeft, dat werd ingesteld om die inlichtingen te verkrijgen.

In voorkomend geval deelt de Belgische bevoegde autoriteit de verzoekende autoriteit mee op welke gronden zij een administratief onderzoek niet noodzakelijk acht.

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten van het gevraagde administratief onderzoek gaat de Belgische bevoegde autoriteit te werk volgens dezelfde procedures als handelde zij uit eigen beweging of op verzoek van een andere Belgische instantie.

Op specifiek verzoek van de verzoekende autoriteit verstrekt de Belgische bevoegde autoriteit de originele stukken, tenzij de Belgische voorschriften zich hiertegen verzetten.

De inlichtingen worden door de Belgische bevoegde autoriteit zo spoedig mogelijk, doch uiterlijk drie maanden na de datum van ontvangst van het verzoek verstrekt. Indien de Belgische bevoegde autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij deze binnen twee maanden. In bijzondere gevallen kunnen de Belgische bevoegde autoriteit en de verzoekende autoriteit een andere termijn overeenkomen.
De ontvangst van het verzoek wordt door de Belgische bevoegde autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs elektronische weg, bevestigd.

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk een maand na ontvangst van het verzoek, aan de verzoekende autoriteit weten welke tekortkomingen het verzoek vertoont en preciseert welke aanvullende achtergrondinformatie zij verlangt. In dit geval gaan de in het vijfde lid gestelde termijnen in op de datum waarop de Belgische bevoegde autoriteit de aanvullende informatie ontvangt.

Indien de Belgische bevoegde autoriteit niet binnen de gestelde termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van het verzoek, aan de verzoekende autoriteit mee, met vermelding van de datum waarop zij meent aan het verzoek te kunnen voldoen.
Deze termijn mag niet langer zijn dan zes maanden te rekenen vanaf de datum van ontvangst van het verzoek.

Indien de Belgische bevoegde autoriteit niet over de gevraagde inlichtingen beschikt en niet aan het verzoek om inlichtingen kan voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand na ontvangst van het verzoek, aan de verzoekende autoriteit mee.

§ 5/1. Wat betreft een in paragraaf 4 en in paragraaf 5 bedoeld verzoek worden de verzochte inlichtingen geacht van verwacht belang te zijn indien op het ogenblik van het verzoek de verzoekende autoriteit van oordeel is dat er overeenkomstig haar nationale wetgeving een redelijke mogelijkheid bestaat dat de verzochte inlichtingen van belang zullen zijn voor de belastingaangelegenheden van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen, verstrekt de verzoekende autoriteit ten minste de volgende inlichtingen aan de aangezochte autoriteit:

a) het fiscale doel waarvoor de informatie wordt opgevraagd;

b) een specificering van de inlichtingen die nodig zijn voor de uitvoering of handhaving van haar nationale recht.

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op een groep belastingplichtigen die niet individueel kunnen worden geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op basis van een gemeenschappelijke reeks kenmerken.

In dergelijke gevallen, verstrekt de verzoekende autoriteit de volgende informatie aan de aangezochte autoriteit:

a) een gedetailleerde beschrijving van de groep;

b) een toelichting bij de toepasselijke wetgeving en bij de feiten op basis waarvan redelijkerwijze vermoed kan worden dat de belastingplichtigen in de groep de toepasselijke wetgeving niet hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen zouden bijdragen tot het bepalen van de mate waarin de belastingplichtigen in de groep aan hun verplichtingen voldoen;
d) in voorkomend geval, feiten en omstandigheden die verband houden met de tussenkomst van een derde die actief heeft bijgedragen tot de mogelijke niet-naleving van de toepasselijke wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse bevoegde autoriteit automatisch alle inlichtingen waarover zij ten aanzien van ingezetenen van die andere lidstaat beschikt inzake de volgende specifieke inkomsten- en vermogenscategorieën, op te vatten in de zin van de Belgische wetgeving:

a) inkomen uit een dienstbetrekking;

b) tantièmes en presentiegelden;

c) levensverzekeringsproducten die niet vallen onder andere Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch onder soortgelijke voorschriften;

d) pensioenen;

e) eigendom van en inkomsten uit onroerend goed;

f) royalty's;

g) inkomsten uit dividenden zonder bewaarneming, met uitzondering van inkomsten uit dividenden die zijn vrijgesteld van vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn 2011/96/EU van de Raad.

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de verstrekking van de in de eerste alinea genoemde inlichtingen het door de lidstaat van verblijf afgegeven fiscaal identificatienummer (TIN) van ingezetenen.

België stelt de Commissie jaarlijks in kennis van ten minste twee inkomsten- en vermogenscategorieën die zijn opgenomen in de eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over ingezetenen van een andere lidstaat.

België stelt de Commissie vóór 1 januari 2026 in kennis van ten minste vijf categorieën die zijn opgenomen in het eerste lid, ten aanzien waarvan de bevoegde autoriteit van elke andere lidstaat automatisch inlichtingen verstrekt over ingezetenen van die andere lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken die ingaan op of na 1 januari 2026.

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen zes maanden na het verstrijken van het kalenderjaar in de loop waarvan de inlichtingen beschikbaar zijn geworden.

"Beschikbare inlichtingen" betekent inlichtingen die zich in de belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden en die opvraagbaar zijn overeenkomstig de procedures voor het verzamelen en verwerken van inlichtingen in die lidstaat.

§ 6/1. In het kader van de verplichte automatische uitwisseling van inlichtingen over grensoverschrijdende voorafgaande fiscale beslissingen, zijn de voorwaarden de volgende:
1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van deze paragraaf, verstrekt de Belgische bevoegde autoriteit automatisch inlichtingen aan de bevoegde autoriteiten van alle andere lidstaten en de Europese Commissie, overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde praktische modaliteiten wanneer een grensoverschrijdende voorafgaande beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december 2016.

2° de Belgische bevoegde autoriteit verstrekt eveneens, overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde praktische modaliteiten, aan de bevoegde autoriteiten van alle andere lidstaten, evenals aan de Europese Commissie, de inlichtingen over grensoverschrijdende voorafgaande fiscale beslissingen die zijn verstrekt, gewijzigd of hernieuwd binnen de periode beginnend vijf jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in de bepaling onder 6° van deze paragraaf.

Indien de grensoverschrijdende voorafgaande fiscale beslissingen werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en 31 december 2013, worden deze inlichtingen verstrekt op voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.

Als grensoverschrijdende voorafgaande fiscale beslissingen werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31 december 2016, worden die inlichtingen verstrekt ongeacht of die grensoverschrijdende voorafgaande beslissingen al dan niet nog geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin een voorafgaande grensoverschrijdende ruling betrekking heeft op belastingaangelegenheden van een of meer natuurlijke personen, tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1 januari 2026 is afgegeven, gewijzigd of hernieuwd, en:

a) het bedrag van de transactie of reeks transacties van de voorafgaande grensoverschrijdende ruling groter is dan 1.500.000 euro (of het equivalent daarvan in een andere valuta), indien dat bedrag wordt vermeld in de voorafgaande grensoverschrijdende ruling, of;

b) de voorafgaande grensoverschrijdende ruling bepaalt of een persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de ruling afgeeft.

Voor de toepassing van punt a), en onverminderd het in de voorafgaande grensoverschrijdende ruling bedoelde bedrag, omvat het bedrag van de voorafgaande grensoverschrijdende ruling bij een reeks transacties met betrekking tot verschillende goederen, diensten of activa, de totale onderliggende waarde. De bedragen worden niet geaggregeerd indien dezelfde goederen, diensten of activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande grensoverschrijdende rulings inzake bronbelasting op inkomsten uit arbeid, tantièmes en presentiegelden of pensioenen van niet-ingezetenen niet onder de uitwisseling van inlichtingen over voorafgaande grensoverschrijdende rulings met betrekking tot natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:

a) voor de op grond van 1° uitgewisselde inlichtingen: onverwijld zodra de voorafgaande grensoverschrijdende rulings of voorafgaande verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of hernieuwd en uiterlijk binnen drie maanden na het einde van het semester van het kalenderjaar waarin de voorafgaande grensoverschrijdende rulings of voorafgaande verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde inlichtingen: vóór 1 januari 2018.

5° De door de Belgische bevoegde autoriteit uit hoofde van de bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen omvatten de volgende gegevens:

a) de identificatie van de rechtspersoon, tenzij de voorafgaande grensoverschrijdende ruling betrekking heeft op een natuurlijke persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt, en in voorkomend geval de groep personen waartoe die persoon behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen een omschrijving van de relevante zakelijke activiteiten of transacties of reeks van transacties, alsook alle andere inlichtingen die voor de bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of van inlichtingen waarvan het verstrekken in strijd zou zijn met de openbare orde.

c) de data van de aflevering, wijziging of hernieuwing van de grensoverschrijdende voorafgaande fiscale beslissing;

d) de aanvangsdatum van de geldigheidsperiode van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld;

e) de einddatum van de geldigheidsperiode van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;

g) het bedrag van de verrichting of reeks van verrichtingen van de grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld in de grensoverschrijdende voorafgaande fiscale beslissing;

h) in voorkomend geval, de identificatie van de andere lidstaten die mogelijks betrokken zijn bij de grensoverschrijdende voorafgaande fiscale beslissing;

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling betrekking heeft op een natuurlijke persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die er zijn, waarop de voorafgaande grensoverschrijdende ruling of de voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van invloed zal zijn waarbij vermeld dient te worden met welke lidstaten de getroffen personen verbonden zijn, en

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a), b), en i) van deze paragraaf worden niet medegedeeld aan de Europese Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel en in elk geval niet later dan zeven werkdagen na ontvangst, aan de verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing totdat het in § 24, 3de en 4de lid, bedoelde gegevensbestand operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met inachtneming van de bepalingen van § 24, 2de lid, om aanvullende inlichtingen verzoeken, daaronder begrepen de volledige tekst van een grensoverschrijdende voorafgaande fiscale beslissing.

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen, bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van het eerste lid het fiscaal identificatienummer van de rijksinwoner dat werd afgeleverd door rechtsgebied van verblijf.

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan de commissie mee de statistieken over het volume van de automatische uitwisseling in toepassing van de paragrafen 6 en 6/1, alsook de inlichtingen over de kosten en baten, administratief en andere, verbonden aan de uitwisseling die plaats heeft gevonden, en aan de eventuele wijzigingen, zowel voor de belastingadministraties als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie van de administratieve samenwerking voorzien door dit artikel in het licht van de strijd tegen de fiscale fraude en ontduiking.

De Belgische bevoegde autoriteit controleert en evalueert de efficiëntie van de administratieve samenwerking voorzien door dit artikel, met name wat betreft de strijd tegen de belastingontduiking en deelt de Commissie de resultaten van zijn evaluatie een maal per jaar mee via een formulier en volgens de modaliteiten voorzien door de Commissie.

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde lid bedoelde termijn de in tweede lid bedoelde gegevens inzake grensoverschrijdende constructies, waarvan zij ingelicht is door de intermediair of de relevante belastingplichtige overeenkomstig de artikelen 289bis/1 tot en met 289bis/8, via automatische uitwisseling mee aan de bevoegde autoriteiten van alle andere lidstaten.

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid mee te delen gegevens zijn de volgende, voor zover van toepassing:

1° de identificatiegegevens van intermediairs, en relevante belastingplichtigen, bedoeld in artikel 289bis/1, 4° en
5°, met uitzondering van intermediairs die op grond van het juridisch beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig artikel 289bis/7, met inbegrip van hun naam, geboortedatum en -plaats (in het geval van een natuurlijk persoon), fiscale woonplaats, fiscaal identificatienummer, en, in voorkomend geval, van de personen die overeenkomstig paragraaf 2, 21° een verbonden onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in artikel 289bis/2 op grond waarvan de grensoverschrijdende constructie gemeld moet worden;

3° een samenvatting van de inhoud van de meldingsplichtige grensoverschrijdende constructie, met onder meer de benaming waaronder zij algemeen bekend staat, indien voorhanden, en een beschrijving van de relevante constructies, alsook alle andere inlichtingen die voor de bevoegde autoriteit van belang kunnen zijn bij het beoordelen van een mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking van een handels-, bedrijfs- , nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of van inlichtingen waarvan de onthulling in strijd zou zijn met de openbare orde;

4° de datum waarop de eerste stap voor de implementatie van de meldingsplichtige grensoverschrijdende constructie is of zal worden ondernomen;

5° nadere bijzonderheden van de nationale bepalingen die aan de meldingsplichtige grensoverschrijdende constructie ten grondslag liggen;

6° de waarde van de meldingsplichtige grensoverschrijdende constructie;

7° de lidstaat van de relevante belastingbetaler(s) en eventuele andere lidstaten waarop de meldingsplichtige grensoverschrijdende constructie naar alle waarschijnlijkheid van invloed zal zijn;

8° de identificatiegegevens van andere personen in een lidstaat, op wie de meldingsplichtige grensoverschrijdende constructie naar alle waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met welke lidstaten deze personen verbonden zijn.

De automatische uitwisseling geschiedt binnen één maand te rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020 meegedeeld.

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze paragraaf, worden niet medegedeeld aan de Europese Commissie.

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028, bevat de mededeling van de gegevens betreffende de grensoverschrijdende regelingen het fiscaal identificatienummer van de personen bepaald in het tweede lid, 8°.

§ 7. De Belgische bevoegde autoriteit verstrekt spontaan, in elk van de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de buitenlandse bevoegde autoriteit:

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen dat in de andere lidstaat een derving van belasting kan bestaan;

2° een belastingplichtige verkrijgt in België een vrijstelling of vermindering van belasting die voor hem een belastingplicht of een hogere belasting in de andere lidstaat zou moeten meebrengen;

3° transacties tussen een belastingplichtige in België en een belastingplichtige in een andere lidstaat worden over één of meer andere landen geleid, op zodanige wijze dat daardoor in één van beide of in beide lidstaten een belastingbesparing kan ontstaan;

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen dat er belastingbesparing kan ontstaan door een kunstmatige verschuiving van winsten binnen een groep van ondernemingen;
5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen door een buitenlandse bevoegde autoriteit, hebben informatie opgeleverd die voor de vaststelling van de belastingschuld in die andere lidstaat toereikend, ter zake dienend en niet overmatig is.

De Belgische bevoegde autoriteit kan een buitenlandse bevoegde autoriteit spontaan alle inlichtingen meedelen waarvan zij kennis heeft en die voor deze buitenlandse bevoegde autoriteit toereikend, ter zake dienend en niet overmatig zijn.

De in het eerste lid bedoelde inlichtingen worden door de Belgische bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand nadat deze beschikbaar worden, aan de buitenlandse bevoegde autoriteit van elke betrokken lidstaat verstrekt.

§ 8. De ontvangst van de in § 7 bedoelde inlichtingen wordt door de Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen zeven werkdagen na ontvangst, indien mogelijk langs elektronische weg, aan de verstrekkende buitenlandse bevoegde autoriteit bevestigd.

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in § 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde ambtenaren onder de voorwaarden die zijn vastgesteld door de buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren waar de administratieve autoriteiten van de lidstaat taken vervullen;

2° aanwezig zijn bij administratieve onderzoeken die worden uitgevoerd op het grondgebied van de buitenlandse bevoegde autoriteit;

3° deelnemen aan de administratieve onderzoeken die worden uitgevoerd op het grondgebied van de andere lidstaat, met gebruikmaking van elektronische communicatiemiddelen, in voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen door middel van elektronische communicatiemiddelen, kunnen zij personen ondervragen en bescheiden onderzoeken, onder voorbehoud van de door de buitenlandse bevoegde autoriteit gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde ambtenaren onder de voorwaarden die zijn vastgesteld door de Belgische bevoegde autoriteit mogen:

1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn taken vervult;

2° aanwezig zijn bij administratieve onderzoeken die worden uitgevoerd op Belgisch grondgebied;

3° deelnemen aan de administratieve onderzoeken die worden uitgevoerd op Belgisch grondgebied, met gebruikmaking van elektronische communicatiemiddelen, in voorkomend geval.
De Belgische bevoegde autoriteit antwoordt op het overeenkomstig de eerste alinea ingediende verzoek binnen een termijn van 60 dagen na ontvangst van het verzoek, om haar instemming te bevestigen of haar gemotiveerde weigering aan de buitenlandse bevoegde autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden waartoe de ambtenaren van de Belgische bevoegde autoriteit toegang hebben, ontvangen de ambtenaren van de verzoekende autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn tijdens een administratief onderzoek of daaraan deelnemen met gebruikmaking van elektronische communicatiemiddelen, mogen zij personen ondervragen en bescheiden onderzoeken, onder de voorwaarden die zijn vastgesteld door de Belgische bevoegde autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking heeft, om de controlemaatregelen van de ambtenaren van de verzoekende autoriteit na te leven, wordt door de Belgische bevoegde autoriteit beschouwd als een weigering tegenover haar eigen ambtenaren.

De door de verzoekende lidstaat gemachtigde ambtenaren die overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en hun officiële hoedanigheid worden vermeld.

§ 11. In de gevallen waarin België met één of meer lidstaten overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of meer personen te wier aanzien zij een gezamenlijk of complementair belang hebben, controles te verrichten en de aldus verkregen inlichtingen uit te wisselen, is deze § van toepassing.

De Belgische bevoegde autoriteit bepaalt autonoom welke personen zij voor een gelijktijdige controle wil voorstellen. Zij deelt de buitenlandse bevoegde autoriteit van de betrokken lidstaten met opgave van redenen mee welke dossiers zij voor een gelijktijdige controle voorstelt. Zij bepaalt binnen welke termijn de controle moet plaatsvinden.

Wanneer aan de Belgische bevoegde autoriteit een gelijktijdige controle wordt voorgesteld, beslist zij of ze aan de gelijktijdige controle wenst deel te nemen. Zij doet de buitenlandse bevoegde autoriteit die de controle voorstelt een bevestiging van deelname of een gemotiveerde weigering toekomen binnen een termijn van 60 dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan die wordt belast met de leiding en de coördinatie van de controle.

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het verzoek om een gezamenlijke audit binnen een termijn van 60 dagen, te rekenen vanaf de ontvangst van het verzoek en motiveert haar beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd door de bevoegde autoriteit van de verzoekende lidstaat, door de Belgische bevoegde autoriteit, en in voorkomend geval, door de bevoegde autoriteiten van de andere aangezochte lidstaten en in overeenstemming met de Belgische wetgeving en procedurele voorschriften. De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die deelnemen aan de gezamenlijke audit op Belgisch grondgebied, worden vastgesteld overeenkomstig de Belgische wetgeving. Tegelijk met het naleven van die wetgeving, oefenen de ambtenaren van een andere lidstaat geen bevoegdheden uit die verder zouden gaan dan de bevoegdheden die hun krachtens de wetgeving van hun lidstaat zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd om personen te ondervragen en bescheiden te onderzoeken in samenspraak met de ambtenaren van de Belgische bevoegde autoriteit, met inachtneming van de in België bepaalde procedurele regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de activiteiten van de gezamenlijke audit is verzameld, worden beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde juridische voorwaarden als in het geval van een klassieke audit, uitgevoerd in België door Belgische ambtenaren, onder meer in de loop van een bezwaar-, herzienings- of beroepsprocedures.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op Belgisch grondgebied, genieten personen die aan een gezamenlijke audit worden onderworpen of erdoor worden geraakt, dezelfde rechten en hebben ze dezelfde plichten als in het geval van een klassieke audit waaraan alleen Belgische ambtenaren deelnemen, onder meer in de loop van een bezwaar-, herzienings- of beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van een of meer lidstaten een gezamenlijke audit verrichten, trachten zij het eens te worden over de feiten en omstandigheden die relevant zijn voor de gezamenlijke audit, en streven zij naar overeenstemming over de fiscale positie van de geaudite persoon of personen op basis van de resultaten van de gezamenlijke audit. De bevindingen van de gezamenlijke audit worden neergelegd in een eindverslag. Punten waarover de bevoegde autoriteiten het eens zijn, worden in de conclusies van het eindverslag opgenomen en worden in aanmerking genomen in de relevante instrumenten die de bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 11/2. De Belgische bevoegde autoriteit kan de bevoegde autoriteit van een andere of meerdere lidstaten verzoeken een gezamenlijke audit uit te voeren.

Gezamenlijke audits worden op vooraf overeengekomen en gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd door de betrokken bevoegde autoriteiten, en in overeenstemming met de wetgeving en de procedurele voorschriften van de lidstaat waar de activiteiten van de gezamenlijke audit plaatsvinden.

De rechten en plichten van de Belgische ambtenaren die deelnemen aan de gezamenlijke audit op het grondgebied van een andere lidstaat, worden vastgesteld overeenkomstig de wetgeving van die lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de Belgische ambtenaren geen bevoegdheden uit die verder zouden gaan dan de bevoegdheden die hun krachtens de Belgische wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het grondgebied van een andere lidstaat, kan het bewijsmateriaal dat tijdens de activiteiten van de gezamenlijke audit is verzameld, worden beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde juridische voorwaarden als in het geval van een klassieke audit uitgevoerd in België door Belgische ambtenaren.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van een of meerdere andere lidstaten een gezamenlijke audit verrichten, trachten zij het eens te worden over de feiten en omstandigheden die relevant zijn voor de gezamenlijke audit, en streven zij naar overeenstemming over de fiscale positie van de geaudite persoon of personen op basis van de resultaten van de gezamenlijke audit. De bevindingen van de gezamenlijke audit worden neergelegd in een eindverslag. De punten waarover de bevoegde autoriteiten het eens zijn, worden in de conclusies van het eindverslag opgenomen en worden in aanmerking genomen in de relevante instrumenten die de bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het resultaat van de gezamenlijke audit en krijgen een kopie van het eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 12. De Belgische bevoegde autoriteit kan een verzoek aan een buitenlandse bevoegde autoriteit richten tot kennisgeving aan de geadresseerde, overeenkomstig de in de aangezochte lidstaat geldende voorschriften voor de kennisgeving van soortgelijke akten, van alle door de Belgische administratieve overheden afgegeven akten en besluiten die betrekking hebben op de toepassing in België van wetgeving betreffende registratie-, hypotheek- en griffierechten.

Het verzoek tot kennisgeving vermeldt de naam en het adres van de geadresseerde, evenals alle overige informatie ter identificatie van de geadresseerde, en het onderwerp van de akte of het besluit waarvan de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde autoriteit slechts gedaan indien de kennisgeving van de akten niet volgens de Belgische regels kan geschieden, of buitensporige problemen zou veroorzaken. De Belgische bevoegde autoriteit kan een document, per aangetekende brief of langs elektronische weg, rechtstreeks ter kennis brengen aan een persoon op het grondgebied van een andere lidstaat.

§ 13. Op verzoek van een buitenlandse bevoegde autoriteit gaat de Belgische bevoegde autoriteit, overeenkomstig de Belgische voorschriften voor de kennisgeving van soortgelijke akten, over tot kennisgeving aan de geadresseerde van alle door de administratieve overheden van de verzoekende lidstaat afgegeven akten en besluiten die betrekking hebben op de toepassing op haar grondgebied van wetgeving betreffende registratie-, hypotheek- en griffierechten.

De Belgische bevoegde autoriteit stelt de verzoekende autoriteit onverwijld in kennis van het aan het verzoek gegeven gevolg en, in het bijzonder, van de datum waarop de akte of het besluit aan de geadresseerde ter kennis is gebracht.

§ 14. Indien een buitenlandse bevoegde autoriteit inlichtingen overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding betreffende de ontvangen inlichtingen verzoekt, doet de ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen aan de Belgische voorschriften inzake beroepsgeheim en gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie maanden nadat het resultaat van het gebruik van de verlangde inlichtingen bekend is, een terugmelding aan de buitenlandse bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar, overeenkomstig bilateraal overeengekomen praktische afspraken, een terugmelding over de automatische inlichtingenuitwisseling naar de betrokken lidstaten.

§ 15. De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7 inlichtingen heeft verstrekt, kan de ontvangende buitenlandse bevoegde autoriteit om terugmelding betreffende de ontvangen inlichtingen verzoeken.

§ 16. De Belgische verbindingsdienst of de Belgische bevoegde ambtenaar die een verzoek om samenwerking ontvangt dat een optreden vereist buiten de hem krachtens de Belgische wetgeving of het Belgische beleid verleende bevoegdheid, geeft het verzoek onmiddellijk door aan het Belgisch centraal verbindingsbureau en stelt de verzoekende buitenlandse bevoegde autoriteit hiervan in kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat het verzoek aan het Belgisch centraal verbindingsbureau is doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in enigerlei vorm of volgens dit artikel, vallen onder de geheimhoudingsplicht en genieten de bescherming waarin het nationale recht van de ontvangende lidstaat met betrekking tot soortgelijke inlichtingen voorziet.

Deze inlichtingen mogen worden gebruikt:

1° voor de vaststelling, de toepassing en de handhaving van het nationale recht met betrekking tot de in artikel 2 van de richtlijn bedoelde belastingen, alsmede de btw, andere indirecte belastingen, douanerechten, de bestrijding van het witwassen van geld en van de financiering van terrorisme;

2° voor de vestiging en de invordering van de andere belastingen en rechten met betrekking tot artikel 3 van de wet van 9 januari 2012 houdende omzetting van Richtlijn 2010/24/EU van de Raad van 16 maart 2010 betreffende de wederzijdse bijstand inzake de invordering van schuldvorderingen die voortvloeien uit belastingen, rechten en andere maatregelen, en voor het vestigen en invorderen van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op de fiscale wetgeving, onverminderd algemene regels en wettelijke bepalingen die de rechten van beklaagden en getuigen in het kader van dergelijke procedures beheersen.

Met de toestemming van de buitenlandse bevoegde autoriteit die de inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor zover dat toegelaten is door de Belgische wetgeving, kunnen de ontvangen inlichtingen en documenten ontvangen van deze autoriteit worden gebruikt voor andere doeleinden dan deze bedoeld in het tweede lid.

De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en documenten zonder de in de derde lid van deze paragraaf bedoelde toestemming ook gebruiken voor elk doel dat onder een op artikel 215 van het Verdrag betreffende de werking van de Europese Unie gebaseerde handeling valt en deze daartoe delen met de bevoegde autoriteit die verantwoordelijk is voor beperkende maatregelen in de betrokken lidstaat.
De Belgische bevoegde autoriteit die van oordeel is dat de van de bevoegde autoriteit van een andere lidstaat verkregen inlichtingen de bevoegde autoriteit van een derde lidstaat van nut kunnen zijn voor de in het tweede lid beoogde doelen, mag de inlichtingen aan deze autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit van de inlichtingen verstrekkende lidstaat in kennis stelt van haar voornemen om die inlichtingen met een derde lidstaat te delen en op voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel vastgelegde regels en procedures. De inlichtingen verstrekkende lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na de datum van ontvangst van de kennisgeving van de lidstaat die de inlichtingen wenst te delen.

§ 18. De Belgische bevoegde autoriteit kan het gebruik toestaan van de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid, bedoelde doeleinden.
De Belgische bevoegde autoriteit verleent toestemming indien de inlichtingen in België voor soortgelijke doeleinden kunnen worden gebruikt.

De Belgische bevoegde autoriteit deelt aan de bevoegde autoriteiten van alle andere lidstaten een lijst mee van andere dan in paragraaf 1 bedoelde doeleinden waarvoor overeenkomstig haar nationale recht, de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen inlichtingen en bescheiden zonder de in het eerste lid bedoelde toestemming gebruiken voor alle doeleinden die de Belgische bevoegde autoriteit heeft opgenoemd.

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit België die door een buitenlandse bevoegde autoriteit aan een buitenlandse bevoegde autoriteit van een derde lidstaat werden doorgegeven, in die derde lidstaat toestaan.

§ 19. Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te komen.

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op voorwaarde dat de buitenlandse bevoegde autoriteit eerst de inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in de gegeven omstandigheden kon aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te komen.

§ 20. Het is de Belgische bevoegde autoriteit niet toegelaten onderzoek in te stellen of inlichtingen te verstrekken wanneer de Belgische wetgeving haar niet toestaat voor eigen doeleinden het onderzoek in te stellen of de gevraagde inlichtingen te verzamelen.

De Belgische bevoegde autoriteit kan weigeren inlichtingen te verstrekken indien:

1° de verzoekende lidstaat, op juridische gronden, soortgelijke inlichtingen niet kan verstrekken;

2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze, of indien het inlichtingen betreft waarvan de onthulling in strijd zou zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee op welke gronden zij het verzoek om inlichtingen afwijst.
§ 21. De Belgische bevoegde autoriteit wendt de middelen aan waarover zij beschikt om de gevraagde inlichtingen te verzamelen, zelfs indien zij de inlichtingen niet voor eigen belastingdoeleinden nodig heeft. Deze verplichting geldt onverminderd § 20, eerste en tweede lid, die, wanneer er een beroep op wordt gedaan, in geen geval zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te verstrekken uitsluitend omdat België geen binnenlands belang bij deze inlichtingen heeft.

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat de Belgische bevoegde autoriteit kan weigeren inlichtingen te verstrekken, uitsluitend op grond dat deze berusten bij een bank, een andere financiële instelling, een gevolmachtigde of een persoon die als vertegenwoordiger of trustee optreedt, of dat zij betrekking hebben op eigendomsbelangen in een persoon.

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit weigeren de gevraagde inlichtingen toe te zenden indien deze betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de toezending van de inlichtingen geweigerd had kunnen worden op grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom was verzocht vóór 11 maart 2011.

§ 22. Indien de Belgische overheid voorziet in een samenwerking met een derde land welke verder reikt dan de bij de richtlijn geregelde samenwerking, kan de Belgische overheid de verderreikende samenwerking niet weigeren aan een andere lidstaat die met haar deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken die zijn ingediend op grond van § 4, alsook de antwoorden op grond van § 5, de ontvangstbevestigingen, de verzoeken om inlichtingen van algemene aard en de verklaringen van ongeschiktheid of weigering krachtens § 5 worden, voor zover mogelijk, overgemaakt door middel van een door de Commissie goedgekeurd standaardformulier. Er mogen rapporten, certificaten en andere bescheiden, of andere voor eensluidend verklaarde afschriften of uittreksels daarvan bij de standaardformulieren gevoegd worden.

De in het eerste lid bedoelde standaardformulieren bevatten ten minste de volgende gegevens, die de verzoekende autoriteit moet verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle is ingesteld en, in het geval van vragen betreffende een groep zoals bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;

b) het fiscale doel van de gevraagde informatie.

De Belgische bevoegde autoriteit kan, voor zover bekend en in overeenstemming met de ontwikkeling van de internationale situatie, de namen en adressen verstrekken van alle personen van wie er redenen zijn om aan te nemen dat ze in het bezit zijn van de gevraagde informatie, alsook alle elementen die het verzamelen van informatie door de aangezochte autoriteit kunnen vergemakkelijken.

De spontane gegevensuitwisseling en de desbetreffende ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8, verzoeken tot administratieve kennisgeving op grond van §§ 12 en 13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden overgemaakt door middel van de door de Commissie goedgekeurde standaardformulieren.
De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1 wordt verricht in een geautomatiseerd standaardformaat dat ontworpen is om die automatische uitwisseling te vergemakkelijken en dat is goedgekeurd door de Commissie.

§ 24. De krachtens dit artikel verstrekte inlichtingen worden voor zover mogelijk verzonden langs elektronische weg, via het CCN-netwerk.

Het verzoek om samenwerking, waaronder het verzoek tot kennisgeving en de bijgevoegde bescheiden kunnen in elke door de aangezochte en de verzoekende autoriteit overeengekomen taal zijn gesteld. Slechts in bijzondere gevallen en mits het verzoek met redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken het verzoek vergezeld te laten gaan van een vertaling in één van de officiële talen van België.

Om te voldoen aan de automatische uitwisseling als bedoeld in § 6/1, 1° en 2°, te verstrekken inlichtingen, worden de gegevens die moeten worden meegedeeld opgeslagen in een beveiligd centraal gegevensbestand betreffende de administratieve samenwerking op belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter beschikking gesteld door de Commissie uiterlijk op 31 december 2017. De Belgische bevoegde autoriteiten hebben toegang tot de in dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde automatische uitwisseling van gegevens, volgens lid 1 van deze paragraaf en de toepasselijke praktische modaliteiten.

§ 25. De Belgische bevoegde autoriteit die van een derde land inlichtingen ontvangt welke naar verwachting van belang zijn voor haar administratie en de handhaving van de Belgische wetgeving betreffende registratie-, hypotheek- en griffierechten, kan deze inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan elke buitenlandse bevoegde autoriteit die erom verzoekt, mits dat krachtens een overeenkomst met dat derde land is toegestaan.

De Belgische bevoegde autoriteit kan, met inachtneming van de wet van 8 december 1992 tot bescherming van de persoonlijke levenssfeer ten opzichte van de verwerking van persoonsgegevens en de wet van 3 augustus 2012 houdende bepalingen betreffende de verwerking van persoonsgegevens door de Federale Overheidsdienst Financiën in het kader van zijn opdrachten, de overeenkomstig dit artikel ontvangen inlichtingen doorgeven aan een derde land, op voorwaarde dat aan elk van de volgende voorwaarden is voldaan:

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de inlichtingen afkomstig zijn, heeft daarin toegestemd;

b) het derde land heeft zich ertoe verbonden de medewerking te verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent het ongeoorloofde of onwettige karakter van verrichtingen die blijken in strijd te zijn met of een misbruik te vormen van de belastingwetgeving.

§ 26. Rapporterende financiële instellingen, intermediairs, rapporterende platformexploitanten en de Belgische bevoegde autoriteit worden als verwerkingsverantwoordelijken beschouwd wanneer zij, alleen of gezamenlijk, de doelen en middelen van de verwerking van persoonsgegevens bepalen in de zin van Verordening (EU) 2016/679 van het Europees Parlement en de Raad van 27 april 2016 betreffende de bescherming van natuurlijke personen in verband met de verwerking van persoonsgegevens en betreffende het vrije verkeer van die gegevens en tot intrekking van Richtlijn 95/46/EG.

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in kennis van elke gegevensinbreuk en alle daaropvolgende corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen met de lidstaat of de lidstaten waar de gegevensinbreuk heeft plaatsgevonden, schorsen door de Commissie en de betrokken lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een dergelijke schorsing wordt onmiddellijk van kracht.

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn, indien de gegevensinbreuk niet onmiddellijk en op passende wijze onder controle kan worden gebracht. Op een dergelijk verzoek schorst de Commissie de toegang van die lidstaat of lidstaten tot het CCN-netwerk voor de toepassing van de richtlijn.

De Belgische bevoegde autoriteit stelt, in geval van een gegevensinbreuk, de Commissie op de hoogte wanneer zij deze inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is verholpen, geeft de Commissie pas na die verificatie de betrokken lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de toepassing van de richtlijn.

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in het centrale gegevensbestand of het CCNnetwerk plaatsvindt die nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen door de lidstaten via het CCN-netwerk, stelt de Commissie de lidstaten zonder onnodige vertraging in kennis van de gegevensinbreuk en van eventuele corrigerende maatregelen die zijn genomen. Zulke corrigerende maatregelen kunnen inhouden dat de toegang tot het centrale gegevensbestand of het CCN-netwerk voor de toepassing van de richtlijn wordt geschorst totdat de gegevensinbreuk is verholpen.
- in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.
- in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.
- in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.
- in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.

###### Art. 289bis/1

(van toepassing vanaf 11.04.2026)

(8°, ingevoegd bij art. 29 van de wet van 16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))

Voor de toepassing van de artikelen 289bis, § 6/3 en 289bis/2 tot en met 289bis/9, wordt verstaan onder:

1° "grensoverschrijdende constructie": een constructie die ofwel meer dan één lidstaat ofwel een lidstaat en een derde land betreft, waarbij ten minste een van de volgende voorwaarden is vervuld:

a) niet alle deelnemers aan de constructie hebben hun fiscale woonplaats in hetzelfde rechtsgebied;
b) een of meer van de deelnemers aan de constructie heeft zijn fiscale woonplaats tegelijkertijd in meer dan één rechtsgebied;

c) een of meer van de deelnemers aan de constructie oefent een bedrijf uit in een ander rechtsgebied via een in dat rechtsgebied gelegen vaste inrichting en de constructie behelst een deel of het geheel van het bedrijf van die vaste inrichting;

d) een of meer van de deelnemers aan de constructie oefent een activiteit uit in een ander rechtsgebied zonder in dat rechtsgebied zijn fiscale woonplaats te hebben of zonder in dat rechtsgebied een vaste inrichting te creëren;

e) een dergelijke constructie heeft mogelijk gevolgen voor de automatische uitwisseling van inlichtingen of de vaststelling van het uiteindelijk belang.

Een constructie betekent ook een reeks constructies. Een constructie kan uit verscheidene stappen of onderdelen bestaan.

2° "meldingsplichtige grensoverschrijdende constructie": iedere grensoverschrijdende constructie die ten minste één van de in artikel 289bis/2 bedoelde wezenskenmerken bezit;

3° "wezenskenmerk": een in artikel 289bis/2 bedoelde eigenschap of kenmerk van een grensoverschrijdende constructie die geldt als een indicatie van een mogelijk risico op belastingontwijking;

4° "intermediair": een persoon die een meldingsplichtige grensoverschrijdende constructie bedenkt, aanbiedt, opzet, beschikbaar maakt voor implementatie of de implementatie ervan beheert.

Een intermediair is ook een persoon die, gelet op de betrokken feiten en omstandigheden en op basis van de beschikbare informatie en de deskundigheid die en het begrip dat nodig is om die diensten te verstrekken, weet of redelijkerwijs kon weten dat hij rechtstreeks of via andere personen, heeft toegezegd hulp, bijstand of advies te verstrekken met betrekking tot het bedenken, aanbieden, opzetten, beschikbaar maken voor implementatie of beheren van de implementatie van een meldingsplichtige grensoverschrijdende constructie. Elke persoon heeft het recht bewijs te leveren van het feit dat hij niet wist en redelijkerwijs niet kon weten dat hij bij een meldingsplichtige grensoverschrijdende constructie betrokken was. Daartoe kan die persoon alle relevante feiten en omstandigheden, beschikbare informatie en zijn relevante deskundigheid en begrip ervan vermelden.

Om een intermediair te zijn, dient een persoon ten minste één van de volgende aanvullende voorwaarden te vervullen:

a) fiscaal inwoner van een lidstaat zijn;

b) beschikken over een vaste inrichting in een lidstaat via welke de diensten in verband met de constructie worden verleend;

c) opgericht zijn in of onder de toepassing van de wetten vallen van een lidstaat;
d) ingeschreven zijn bij een beroepsorganisatie in verband met de verstrekking van juridische, fiscale of adviesdiensten in een lidstaat.

5° "relevante belastingplichtige": elke persoon voor wie een meldingsplichtige grensoverschrijdende constructie beschikbaar wordt gemaakt voor implementatie, of die gereed is om een meldingsplichtige grensoverschrijdende constructie te implementeren of die de eerste stap van een dergelijke constructie heeft geïmplementeerd;

6° "marktklare constructie": een grensoverschrijdende constructie die is bedacht of aangeboden, implementeerbaar is of beschikbaar is gemaakt voor implementatie zonder dat er wezenlijke aanpassingen nodig zijn;

7° "constructie op maat": een grensoverschrijdende constructie die geen marktklare constructie is;

8° "cliënt": elke intermediair of relevante belastingplichtige die diensten, met inbegrip van bijstand, advies, raad of begeleiding, ontvangt van een tot het juridisch beroepsgeheim gehouden intermediair met betrekking tot een meldingsplichtige grensoverschrijdende constructie.

###### Art. 289bis/2

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 21 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

De in artikel 289bis/1, 3°, bedoelde wezenskenmerken van een grensoverschrijdende constructie kunnen worden onderverdeeld in vijf categorieën, categorie A zijnde de algemene wezenskenmerken die aan de in het tweede lid bedoelde "main benefit test" zijn gekoppeld, categorie B zijnde de specifieke wezenskenmerken die aan de hiervoor vermelde "main benefit test" zijn gekoppeld, categorie C zijnde specifieke wezenskenmerken in verband met grensoverschrijdende transacties, categorie D zijnde specifieke wezenskenmerken in verband met de automatische uitwisseling van inlichtingen en uiteindelijk belang en categorie E zijnde specifieke wezenskenmerken in verband met verrekenprijzen.

De algemene wezenskenmerken in categorie A bedoeld in het vierde lid en de specifieke wezenskenmerken in categorie B bedoeld in het vijfde lid en de specifieke wezenskenmerken in categorie C bedoeld in het zesde lid, 1°, b), eerste streepje, c) en d) mogen uitsluitend in aanmerking worden genomen indien kan worden aangetoond dat het belangrijkste voordeel of één van de belangrijkste voordelen die, gelet op alle relevante feiten en omstandigheden, redelijkerwijs te verwachten valt van de constructie het verkrijgen van een belastingvoordeel is.
Dit is de zogenaamde "main benefit test

In het kader van het specifieke wezenskenmerk van categorie C, bedoeld in het zesde lid, 1° is de aanwezigheid van één van de voorwaarden bedoeld in hetzelfde zesde lid, 1°, b), eerste streepje, c) en d) niet voldoende om te besluiten dat een constructie voldoet aan de in het tweede lid bedoelde "main benefit test

Wordt beschouwd als een algemeen wezenskenmerk van categorie A:
1° een constructie waarbij de relevante belastingplichtige of een deelnemer aan de constructie zich tot geheimhouding verbindt en op grond hiervan niet aan andere intermediairs of de belastingautoriteiten mag onthullen hoe de constructie een belastingvoordeel kan opleveren;

2° een constructie waarbij de intermediair aanspraak maakt op een vergoeding (of rente, betaling van financieringskosten en andere uitgaven) voor de constructie en die vergoeding wordt vastgelegd op basis van:

a) het bedrag van het belastingvoordeel dat de constructie oplevert; of

b) de vraag of de constructie daadwerkelijk een belastingvoordeel heeft opgeleverd. De intermediair moet daarbij de vergoeding gedeeltelijk of volledig terugbetalen wanneer het met de constructie beoogde belastingvoordeel niet gedeeltelijk of volledig werd verwezenlijkt;

3° een constructie waarbij gebruik wordt gemaakt van gestandaardiseerde documenten en/of een gestandaardiseerde structuur en die beschikbaar is voor meer dan een relevante belastingplichtige zonder dat er voor implementatie wezenlijke aanpassingen nodig zijn.

Wordt beschouwd als een specifiek wezenskenmerk van categorie B:

1° een constructie waarbij een deelnemer aan de constructie een reeks geplande stappen onderneemt die erin bestaan een verlieslijdende onderneming te verwerven, de hoofdactiviteit van die onderneming stop te zetten en de verliezen ervan te gebruiken om de door hem verschuldigde belastingen te verminderen, onder meer door overdracht van die verliezen naar een ander rechtsgebied of door een versneld gebruik van die verliezen;

2° een constructie die tot gevolg heeft dat inkomsten worden omgezet in vermogen, schenkingen of andere inkomstencategorieën die lager worden belast of van belasting worden vrijgesteld;

3° een constructie die circulaire transacties omvat met als resultaat dat middelen worden rondgepompt ("roundtripping"), meer bepaald met behulp van tussengeschoven entiteiten zonder ander primair handelsdoel of van transacties die elkaar compenseren of tenietdoen of andere soortgelijke kenmerken hebben.

Wordt beschouwd als een specifiek wezenskenmerk van categorie C:

1° een constructie met aftrekbare grensoverschrijdende betalingen tussen twee of meer verbonden ondernemingen waarbij ten minste een van de volgende voorwaarden is vervuld:

a) de ontvanger is in geen van de fiscale rechtsgebieden fiscaal inwoner;

b) de ontvanger is fiscaal inwoner in een rechtsgebied, maar dat rechtsgebied:

- heft geen vennootschapsbelasting, of heft vennootschapsbelasting tegen een nultarief of bijna-nultarief; of

- is opgenomen in een lijst van rechtsgebieden van derde landen die door de lidstaten gezamenlijk of in het kader van de OESO als niet-coöperatief zijn beoordeeld;

c) de betaling geniet een volledige belastingvrijstelling in het rechtsgebied waar de ontvanger fiscaal inwoner is;
d) de betaling geniet een fiscaal gunstregime in het rechtsgebied waar de ontvanger fiscaal inwoner is;

2° in meer dan één rechtsgebied wordt aanspraak gemaakt op aftrekken voor dezelfde afschrijving;

3° in meer dan één rechtsgebied wordt aanspraak gemaakt op voorkoming van dubbele belasting voor hetzelfde inkomens- of vermogensbestanddeel;

4° een constructie met overdrachten van activa waarbij er een wezenlijk verschil bestaat tussen het bedrag dat in de betrokken rechtsgebieden wordt aangemerkt als de voor die activa te betalen vergoeding.

Wordt beschouwd als een specifiek wezenskenmerk van categorie D:

1° een constructie die kan leiden tot het ondermijnen van de rapportageverplichting uit hoofde van de wetgeving ter omzetting van Uniewetgeving of evenwaardige overeenkomsten inzake de automatische uitwisseling van inlichtingen over financiële rekeningen, waaronder overeenkomsten met derde landen, of die profiteert van het gebrek aan die wetgeving of overeenkomsten. Dergelijke constructies omvatten ten minste het volgende:

a) het gebruik van een rekening, product of belegging die geen financiële rekening is of niet als zodanig te boek staat, maar die over eigenschappen beschikt die in wezen vergelijkbaar zijn met die van een financiële rekening;

b) de overdracht van financiële rekeningen of activa aan, of het gebruik van rechtsgebieden die niet gebonden zijn aan de automatische uitwisseling van inlichtingen over financiële rekeningen met de staat van verblijf van de relevante belastingplichtige;

c) de herkwalificatie van inkomsten en vermogen in producten of betalingen die niet onder de automatische uitwisseling van inlichtingen vallen;

d) de overdracht of omzetting van een financiële instelling of een financiële rekening of de activa daarvan in een financiële instelling of een financiële rekening of activa die niet onder de rapportage in het kader van de automatische uitwisseling van inlichtingen vallen;

e) het gebruik van rechtspersonen, juridische constructies of structuren die de rapportage over één of meer rekeninghouders of uiteindelijk begunstigden in het kader van de automatische uitwisseling van inlichtingen over financiële rekeningen stopzetten of daartoe strekken;

f) constructies die due-diligenceprocedures die door financiële instellingen worden gebruikt om te voldoen aan hun verplichtingen tot het rapporteren van inlichtingen over financiële rekeningen, ondermijnen of zwakke punten ervan benutten, onder meer via het gebruik van rechtsgebieden met ontoereikende of zwakke regelingen voor de handhaving van antiwitwaswetgeving of met zwakke transparantievereisten voor rechtspersonen of juridische constructies;

2° een constructie waarbij de juridische of feitelijke eigendom niet-transparant is door het gebruik van personen, juridische constructies of structuren:
a) die geen wezenlijke economische, door voldoende personeel, uitrusting, activa en gebouwen ondersteunde activiteit uitoefenen; en

b) die zijn opgericht in, worden beheerd in, inwoner zijn van, onder zeggenschap staan in, of gevestigd zijn in een ander rechtsgebied dan het rechtsgebied van verblijf van een of meer van de uiteindelijk begunstigden van de activa die door die personen, juridische constructies of structuren worden aangehouden; en

c) indien de uiteindelijk begunstigden van die personen, juridische constructies of structuren, zoals bedoeld in artikel 4, 27°, van de wet van 18 september 2017 tot voorkoming van het witwassen van geld en de financiering van terrorisme en tot beperking van het gebruik van contanten, niet-identificeerbaar zijn gemaakt.

Wordt beschouwd als een specifiek wezenskenmerk van categorie E:

1° een constructie met gebruik van unilaterale veiligehavenregels;

2° een constructie met overdracht van moeilijk te waarderen immateriële activa. De term "moeilijk te waarderen immateriële activa" omvat immateriële activa of rechten op immateriële activa waarvoor, op het tijdstip van de overdracht ervan tussen verbonden ondernemingen:

a) geen betrouwbare vergelijkbare activa bestaan; en

b) de prognoses van de toekomstige kasstromen of inkomsten die naar verwachting uit de overgedragen activa voortvloeien, of de aannames die worden gebruikt voor het waarderen van de immateriële activa, bijzonder onzeker zijn, waardoor het moeilijk is te voorspellen hoe succesvol de immateriële activa op het moment van de overdracht uiteindelijk zullen zijn;

3° een constructie met een grensoverschrijdende overdracht binnen de groep van functies, en/of risico's en/of activa, indien de geraamde jaarlijkse winst vóór interest en belastingen (ebit) van de overdrager of overdragers, tijdens de periode van drie jaar na de overdracht, minder dan 50 % bedraagt van de geraamde jaarlijkse ebit van die overdrager of overdragers indien de overdracht niet had plaatsgevonden.

###### Art. 289bis/3

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 22 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

§ 1. Elke intermediair moet de in artikel 289bis, § 6/3 bedoelde inlichtingen, over meldingsplichtige grensoverschrijdende constructies waarvan zij kennis, bezit of controle hebben verstrekken aan de in artikel 289bis,
§ 2, 6°, bedoelde Belgische bevoegde autoriteit binnen 30 dagen te rekenen vanaf het hierna vermelde geval dat het eerst plaatsvindt:

- de dag nadat de meldingsplichtige grensoverschrijdende constructie voor implementatie beschikbaar is gesteld; of - de dag nadat de meldingsplichtige grensoverschrijdende constructie gereed is voor implementatie; of

- het ogenblik dat de eerste stap in de implementatie van de meldingsplichtige grensoverschrijdende constructie is ondernomen.

Onverminderd het eerste lid moeten de intermediairs bedoeld in artikel 289bis/1, 4°, tweede lid, eveneens inlichtingen verstrekken met betrekking tot een meldingsplichtige grensoverschrijdende constructie binnen 30 dagen te rekenen vanaf de dag nadat zij, rechtstreeks of via andere personen, hulp, bijstand of advies hebben verstrekt.

§ 2. Wanneer de intermediair inlichtingen over meldingsplichtige grensoverschrijdende constructies moet verstrekken aan de bevoegde autoriteiten van meer dan één lidstaat dan verstrekt hij deze inlichtingen enkel aan de Belgische bevoegde autoriteit indien België als eerste op de onderstaande lijst voorkomt:

1° de lidstaat waar de intermediair fiscaal inwoner is;

2° de lidstaat waar de intermediair een vaste inrichting heeft via welke de diensten met betrekking tot de constructie worden verstrekt;

3° de lidstaat waar de intermediair is opgericht of onder toepassing van de wetten valt;

4° de lidstaat waar de intermediair is ingeschreven bij een beroepsorganisatie in verband met de verstrekking van juridische, fiscale of adviesdiensten.

Wanneer er op grond van het eerste lid een meervoudige meldingsplicht bestaat, wordt de intermediair ontheven van het verstrekken van de inlichtingen als hij een schriftelijk bewijs voorlegt dat dezelfde inlichtingen in een andere lidstaat zijn verstrekt.

###### Art. 289bis/4

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 23 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

Indien het gaat om een marktklare constructie moet de intermediair om de drie maanden een periodiek verslag opstellen met een overzicht van nieuwe meldingsplichtige inlichtingen zoals bedoeld in artikel 289bis, § 6/3, 1°, 4°,
7° en 8°, die sinds het laatste ingediende verslag beschikbaar zijn geworden.

De intermediair die het uniek referentienummer van de bevoegde instanties ontvangt, dient dit, samen met de samenvatting betreffende de gemelde constructie, onverwijld aan de andere betrokken intermediairs en aan de relevante belastingplichtige door te geven.

###### Art. 289bis/5

(van toepassing vanaf 01.07.2020)
(ingevoegd bij art. 24 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

Naar aanleiding van de melding van een grensoverschrijdende constructie die ten minste één van de in artikel 289bis /2 vermelde wezenskenmerken bezit, wordt een uniek referentienummer toegekend, dat naar aanleiding van elke volgende melding betreffende diezelfde grensoverschrijdende constructie moet worden meegedeeld, zowel voor meldingen door elke betrokken intermediair als voor meldingen door de relevante belastingplichtige.

De intermediair die het uniek referentienummer van de bevoegde instanties ontvangt, dient dit, samen met de samenvatting betreffende de gemelde constructie, onverwijld aan de andere betrokken intermediairs en aan de relevante belastingplichtige door te geven.

###### Art. 289bis/6

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 25 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

Wanneer meerdere intermediairs betrokken zijn bij dezelfde meldingsplichtige grensoverschrijdende constructie, moeten alle betrokken intermediairs de inlichtingen verstrekken over de meldingsplichtige grensoverschrijdende constructie.

Een intermediair wordt ontheven van de verplichting tot het verstrekken van inlichtingen indien hij een schriftelijk bewijs voorlegt dat een andere intermediair de inlichtingen bedoeld in artikel 289bis, § 6/3, tweede lid, reeds heeft verstrekt.

###### Art. 289bis/7

(van toepassing vanaf 11.04.2026)

(§ 1, lid 1, 1°, vernietigd door het arrest 1/2024 van 11.01.2024 van het Grondwettelijk Hof, wordt hersteld, en § 4, ingevoegd bij art. 30 van de wet van 16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))

§ 1. Wanneer een intermediair gebonden is door een beroepsgeheim, is hij gehouden:

1° de betrokken intermediair of intermediairs schriftelijk en gemotiveerd op de hoogte te brengen dat hij niet aan de meldingsplicht kan voldoen, waardoor deze meldingsplicht automatisch rust op de andere intermediair of intermediairs;

2° bij gebreke aan een andere intermediair, de relevante belastingplichtige of belastingplichtigen schriftelijk en gemotiveerd op de hoogte te brengen van zijn of hun meldingsplicht.

De ontheffing van de meldingsplicht krijgt slechts uitwerking op het tijdstip dat een intermediair voldaan heeft aan de in het eerste lid bedoelde verplichting.
§ 2. De relevante belastingplichtige kan de intermediair door schriftelijke instemming toelaten alsnog te voldoen aan de in artikel 289bis/3 bedoelde meldingsplicht.

Indien de relevante belastingplichtige geen instemming verleent blijft de meldingsplicht bij de belastingplichtige en bezorgt de intermediair de nodige gegevens voor het vervullen van de in artikel 289bis/3 bedoelde meldingsplicht aan de relevante belastingplichtige.

§ 3. Geen beroepsgeheim overeenkomstig paragraaf 1 of ontheffing van rechtswege kan worden ingeroepen aangaande de meldingsplicht van marktklare constructies die aanleiding geven tot een periodiek verslag overeenkomstig artikel 289bis/4.

§ 4. In afwijking van paragraaf 1, eerste lid, 1°, is de intermediair die een advocaat is, niet gehouden een betrokken intermediair die niet de cliënt is op de hoogte te brengen dat hij niet aan de meldingsplicht kan voldoen.

###### Art. 289bis/8

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 27 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

§ 1. In de volgende gevallen ligt de meldingsplicht bij de relevante belastingplichtige:

1° wanneer er geen intermediair betrokken was bij het bedenken, aanbieden, opzetten, beschikbaar maken voor implementatie of het beheren voor implementatie van de meldingsplichtige grensoverschrijdende constructie; of

2° wanneer de intermediair ontheven is van de verplichting om inlichtingen te verstrekken overeenkomstig artikel 289bis/7, § 1, en hij de relevante belastingplichtige of belastingplichtigen op de hoogte heeft gesteld van zijn of hun meldingsplicht, overeenkomstig artikel 289bis/7, § 1, 2°.

3° wanneer deze niet de in artikel 289bis/7, § 2, eerste lid bedoelde toestemming heeft verleend.

§ 2. Ingeval de meldingsplicht overeenkomstig paragraaf 1 bij de relevante belastingplichtige ligt, verstrekt deze de inlichtingen binnen dertig dagen, te rekenen vanaf het hierna vermelde geval dat eerst plaatsvindt:

- de dag nadat de meldingsplichtige grensoverschrijdende constructie voor implementatie ter beschikking van de relevante belastingplichtige is gesteld of;

- de dag nadat de meldingsplichtige grensoverschrijdende constructie gereed is voor implementatie door de relevante belastingplichtige of;

- vanaf het ogenblik dat de eerste stap voor de implementatie ervan met betrekking tot de relevante belastingplichtige is ondernomen.
§ 3. Wanneer de relevante belastingplichtige inlichtingen over de meldingsplichtige grensoverschrijdende constructie moet verstrekken aan de bevoegde autoriteiten van meer dan één lidstaat, dan moet hij deze inlichtingen enkel verstrekken aan de Belgische bevoegde autoriteit indien België als eerste op de onderstaande, lijst voorkomt:

1° de lidstaat waar de relevante belastingplichtige fiscaal inwoner is;

2° de lidstaat waar de relevante belastingplichtige een vaste inrichting heeft die begunstigde van de constructie is;

3° de lidstaat waar de relevante belastingplichtige inkomsten ontvangt of winsten genereert, hoewel de relevante belastingplichtige geen fiscaal inwoner van een lidstaat is noch een vaste inrichting in een lidstaat heeft;

4° de lidstaat waar de relevante belastingplichtige een activiteit uitoefent, hoewel de relevante belastingplichtige geen fiscaal inwoner van een lidstaat is noch een vaste inrichting in een lidstaat heeft.

Wanneer er op grond van het eerste lid een meervoudige meldingsplicht bestaat, wordt de relevante belastingplichtige ontheven van het verstrekken van de inlichtingen als hij een schriftelijk bewijs voorlegt dat dezelfde inlichtingen in een andere lidstaat zijn verstrekt.

###### Art. 289bis/9

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 28 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

Wanneer de meldingsplicht bij de relevante belastingplichtige ligt en er meer dan één relevante belastingplichtige is, worden de inlichtingen overeenkomstig artikel 289bis/8 verstrekt door de relevante belastingplichtige die als eerste op de onderstaande lijst voorkomt:

1° de relevante belastingplichtige die de meldingsplichtige constructie is overeengekomen met de intermediair;

2° de relevante belastingplichtige die de implementatie van de constructie beheert.

Een relevante belastingplichtige wordt ontheven van de verplichting tot het verstrekken van de inlichtingen indien hij een schriftelijk bewijs voorlegt dat een andere relevante belastingplichtige de inlichtingen bedoeld in artikel 289bis, § 6/3, reeds heeft verstrekt.

###### Art. 289bis/10

(ingevoegd bij art. 29 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2)) Voor de toepassing van de artikelen 289bis, § 6/3 en 289bis/1 tot en met 289bis/9 en de daaruit voortvloeiende uitvoeringsbesluiten dient de melding van de inlichtingen, voor de onderdelen die de Koning nader bepaalt, naast het gebruik van één van de officiële landstalen, ook in het Engels te gebeuren.
Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens, naast het gebruik van één van de officiële landstalen, ook in het Engels moeten worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of de relevante belastingplichtige moet worden gebruikt (art. 2). De leidinggevende ambtenaar bedoeld in het bovenvermelde KB is de leidinggevende ambtenaar van de algemene administratie bevoegd voor de vestiging van de inkomstenbelastingen (art. 1, MB van 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289bis/11

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 30 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

De Koning bepaalt het formulier waarop de intermediair of de relevante belastingplichtige de verplichtingen opgenomen in de artikelen 289bis/1 tot en met 289bis/9 moeten naleven.
Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens, naast het gebruik van één van de officiële landstalen, ook in het Engels moeten worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of de relevante belastingplichtige moet worden gebruikt (art. 2). De leidinggevende ambtenaar bedoeld in het bovenvermelde KB is de leidinggevende ambtenaar van de algemene administratie bevoegd voor de vestiging van de inkomstenbelastingen (art. 1, MB van 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289bis/12

(van toepassing vanaf 31.12.2024)

(gewijzigd bij art. 18 van de wet van 20.12.2024 (B.S., 31.12.2024). Tekst van toepassing vanaf 31.12.2024 (art. 19))

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan voor de overtreding van de bepalingen van de artikelen 289bis/1 tot en met 289bis/9, evenals van de ter uitvoering ervan genomen besluiten, die bestaat uit het onvolledig verstrekken van de inlichtingen bedoeld in artikel 289bis, § 6/3, een boete opleggen van 1 250 euro tot 12 500 euro. Voor dergelijke overtredingen gedaan met bedrieglijk opzet of het oogmerk te schaden wordt een boete van 2 500 euro tot 25 000 euro opgelegd.

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan voor de overtreding van de bepalingen van de artikelen 289bis/1 tot en met 289bis/9, evenals van de ter uitvoering ervan genomen besluiten, die bestaat uit het niet of laattijdig verstrekken van de inlichtingen bedoeld in artikel 289bis, § 6/3, een boete opleggen van 5 000 euro tot 50 000 euro. Voor dergelijke overtredingen gedaan met bedrieglijk opzet of het oogmerk te schaden wordt een boete van 12 500 euro tot 100 000 euro opgelegd.
De Koning legt de progressieve schaal van de administratieve geldboetes vast en regelt hun toepassingsmodaliteiten.

De Koning kan voor de geldboeten die Hij bepaalt, voorzien in de toepassingsmodaliteiten van de maatregelen tot individualisering van de sanctie door de bevoegde rechter.

###### Art. 289bis/13

(van toepassing vanaf 01.07.2020)

(ingevoegd bij art. 32 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepalingen (art. 61, lid 2))

[Bij arrest van 15.09.2022 (nr. 103/2022), heeft het Grondwettelijk Hof art. 289bis/13 W.Reg. vernietigd]

De fiscale administratie, mag binnen de door haar bepaalde termijn, welke wegens wettige redenen kan worden verlengd, voor zover zij die informatie nodig acht om de correcte naleving van de artikelen 289bis/1 tot en met 289bis/11 te verzekeren, van de betrokken intermediair(s) alle informatie vorderen die in toepassing van artikel 289bis/1 tot en met 289bis/11 diende te worden gemeld aan de Belgische bevoegde autoriteit.

###### Art. 289ter

(van toepassing vanaf 01.03.2021)

(ingevoegd bij art. 11 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van toepassing vanaf 01.03.2021 (art. -))

De Koning bepaalt de wijze van betaling van alle bedragen die krachtens de bepalingen van dit Wetboek en de uitvoeringsbesluiten ervan verschuldigd zijn, andere dan de strafrechtelijke boetes.

###### Art. 289quater

(tekst niet in werking getreden)

(ingevoegd bij art. 81 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289quinquies

(tekst niet in werking getreden)
(ingevoegd bij art. 82 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289sexies

(tekst niet in werking getreden)

(ingevoegd bij art. 83 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289septies

(van toepassing vanaf 09.06.2024)

(§ 1, opgeheven bij art. 216 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…) (1)
(1) § 2, ingevoegd bij art. 84 van de wet van 26.01.2021 (B.S., 10.02.2021) die nooit in werking is getreden wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

###### Art. 289octies

(tekst niet in werking getreden)

(ingevoegd bij art. 85 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))
(…)

###### Art. 289nonies

(tekst niet in werking getreden)

(ingevoegd bij art. 86 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289decies

(tekst niet in werking getreden)

(ingevoegd bij art. 87 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289undecies

(tekst niet in werking getreden)

(ingevoegd bij art. 88 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289duodecies

(tekst niet in werking getreden)
(ingevoegd bij art. 89 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

###### Art. 289terdecies

(tekst niet in werking getreden)

(ingevoegd bij art. 90 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van toepassing vanaf 01.01.2025 (art. 219, lid 1).
De Koning kan een inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.
2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…)

INTREKKINGSBEPALING

###### Art. 290

(van toepassing vanaf 01.02.1940)

Onder voorbehoud van de bijzondere fiscale bepalingen voortvloeiend hetzij uit door den Staat gesloten en bij een wet goedgekeurde contracten, hetzij uit internationale overeenkomsten, worden alle vroegere wetsbepalingen betreffende registratie-, hypotheek- of griffierechten ingetrokken.

TIJDELIJKE BEPALINGEN

#### Afdeling I - Maatregelen waarbij de oprichting van nieuwe gebouwen begunstigd wordt door een vermindering der registratierechten

§ 1 - Aankoop van een bouwgrond

###### Art. 291

(zonder voorwerp geworden)

(…)

###### Art. 292

(niet meer van toepassing)

(…)

###### Art. 293

(zonder voorwerp geworden)

(…)

###### Art. 294

(niet meer van toepassing)

(…)

###### Art. 295

(niet meer van toepassing)

(…)

###### Art. 296

(zonder voorwerp geworden)

(…)

§ 2 - Verkoop van een gebouwd onroerend goed

###### Art. 297

(niet meer van toepassing)

(…)

###### Art. 298

(zonder voorwerp geworden)
(…)

###### Art. 299

(niet meer van toepassing)

(…)

#### Afdeling II - Diverse bepalingen

###### Art. 300

(van toepassing vanaf 01.01.1961)

(opgeheven bij art. 32 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 301

(van toepassing vanaf 02.09.2023)

(1°, gewijzigd bij art. 5 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst van toepassing vanaf 02.09.2023 (art. -))

Zijn van de formaliteit van registratie vrijgesteld:

1° Akten in der minne betreffende de leningen toegestaan door de Centrale Dienst voor sociale en culturele actie van het Ministerie van Landsverdediging.

2° Akten, vonnissen en arresten betreffende de uitvoering van de wetten op het herstel van oorlogsschade; minnelijke akten betreffende leningen en kredietopeningen toegekend aan de geteisterden om hun toe te laten de schade te herstellen die zijn geleden hebben ingevolge oorlogsfeiten, wanneer deze leningen en kredietopeningen worden toegestaan volgens de voorzieningen van de ter zake geldende wettelijke beschikkingen, door een in deze beschikkingen bedoelde kredietinstelling.

3° Akten van overdracht en inpandgeving van vorderingen tot herstel van oorlogsschade;

4° (…);

5° (…);
6° Akten van procedure voor de gemengde scheidsgerechten ingesteld bij de vredesverdragen, waaronder de beslissingen en de betekening ervan.

7° Akten, vonnissen en arresten betreffende de rechtsplegingen tot wettiging van de kinderen wier ouders, ten gevolge van den oorlog, zich in de onmogelijkheid hebben bevonden een huwelijk aan te gaan.

8° (…).

8°bis (…).

9° De akten, vonnissen en arresten die betrekking hebben op de tenuitvoerlegging van de wet betreffende de verklaringen van overlijden en van vermoedelijk overlijden, alsmede betreffende de overschrijving en de verbetering van sommige akten van de burgerlijke stand.

10° De akten en vonnissen betreffende de rechtsplegingen vóór de vrederechters bedoeld bij de wet houdende uitzonderingsbepalingen in zake huishuur, wanneer het jaarlijks bedrag van de huurprijs, eisbaar op het ogenblik van de indiening van de eis, niet hoger is dan 300 EUR.

###### Art. 301bis

(van toepassing vanaf 22.04.1962)

(opgeheven bij art. 72, 1° van de wet van 29.03.1962 (B.S., 12.04.1962). Tekst van toepassing vanaf 202.04.1962 (art. 77))

(…)

###### Art. 301quater

(van toepassing vanaf 10.06.1951)

(ingevoegd bij art. 3 van de wet van 25.05.1951 (B.S., 31.05.1951). Tekst van toepassing vanaf 10.06.1951 (art. -))

Kosteloos worden geregistreerd de akten, waarbij aan de gerechtigden van de wet van 1 oktober 1947 betreffende de herstelling van de oorlogsschade aan private goederen, uit de hand woonhuizen worden verkocht die op initiatief van de Staat met het oog op de huisvesting van de geteisterden door oorlogsfeit werden gebouwd.

###### Art. 301ter

(van toepassing vanaf 24.02.1958)

(impliciet opgeheven bij art. 2 van de wet van 24.01.1958 (B.S., 14.02.1958). Tekst van toepassing vanaf 24.02.1958 (art. -))

(…)

###### Art. 302

(van toepassing vanaf 01.02.1940)
Akten betreffende de ambtshalve tenuitvoerlegging van de beslissingen van de bij de vredesverdragen ingestelde gemengde scheidsgerechten worden in debet geregistreerd.

###### Art. 302bis

(van toepassing vanaf 27.08.1978)

(aangevuld bij art. 9 van de wet van 04.08.1978 (B.S. 17.08.1978). Tekst van toepassing vanaf 27.08.1978 (art. -))

§ 1. Wordt van het evenredig recht vrijgesteld, de inbreng in vennootschappen die de rechtspersoonlijkheid bezitten en die de verwezenlijking nastreven van verrichtingen als bedoeld bij artikel 10 van de wet betreffende de economische expansie.

Te dien einde, zal de Minister die Economische zaken, Streekeconomie of Middenstand in zijn bevoegdheid heeft, vóór het verlijden van de akte een bewijsstuk afgeven, waarvan de afgiftemodaliteiten door de Koning worden bepaald. Dit stuk moet aan de akte worden gehecht op het ogenblik van de registratie.

§ 2. Wordt, overeenkomstig de voorwaarden en toepassingsmodaliteiten als bepaald in § 1, van het evenredig recht vrijgesteld, de inbreng in vennootschappen die de rechtspersoonlijkheid bezitten en die in titel I, artikel 2, van de wet tot economische heroriëntering zijn bedoeld.

###### Art. 302quater

(van toepassing vanaf 01.01.1994)

(opgeheven bij art. 15, 1° van de wet van 24.12.1993 (B.S., 31.12.1993 – ed. 2). Tekst van toepassing vanaf 01.01.1994 (art.
26))

(…)

###### Art. 302ter

(van toepassing vanaf 25.11.2025)

(opgeheven bij art. 27 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

(…)

###### Art. 303

(van toepassing vanaf 23.07.1941)

(gewijzigd bij art. 23 van het Besl. Secr. Gen. van 30.06.1941 (B.S., 13.07.1941), bekrachtigd door art. 1 Besluitwet 30 nov.
1944 (B.S., 09.12.1944) en art. 68 van de wet van 1 okt. 1947 (B.S., 10.10.1947). Tekst van toepassing vanaf 23.07.1941 (art. -)) Worden van hypotheekrecht vrijgesteld:

1° hypothecaire inschrijvingen genomen tot waarborg van de in artikel 301, 1° en 2°, bedoelde leningen en kredietopeningen;

2° Inschrijvingen genomen ter uitvoering van de wet van 27 maart 1924, betreffende de Nationale Vereniging van nijveraars en handelaars voor het herstel der oorlogsschade.

###### Art. 304

(van toepassing vanaf 05.03.1949)

(aangevuld bij art. 39 samengeordende wetten houdende uitzonderingsbepalingen inzake huishuur gecoördineerd door Besluit Regent van 31.01.1949 (B.S., 23.02.1949). Tekst van toepassing vanaf 05.03.1949 (art. -))

Is vrij van rolrecht, de inschrijving van de zaken waarvan vonnissen en arresten krachtens artikel 301 vrijstelling van de registratieformaliteit genieten.

De vonnissen en arresten zijn vrij van expeditierecht.

Die vrijstellingen zijn evenwel niet toepasselijk in het geval bedoeld bij artikel 301, 10°.

###### Art. 304bis

(van toepassing vanaf 01.01.1994)

(opgeheven bij art. 15, 2° van de wet van 24.12.1993 (B.S., 31.12.1993 – ed. 2). Tekst van toepassing vanaf 01.01.1994 (art.
26))

(…)

###### Art. 305

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 305bis

(van toepassing vanaf 30.09.1967)

(opgeheven bij art. 5, 2° van de wet van 06.08.1967 (B.S., 20.09.1967). Tekst van toepassing vanaf 30.09.1967 (art. -)) (…)

OVERGANGSBEPALINGEN

#### Afdeling I - Algemene maatregelen

###### Art. 306

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 307

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 308

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 309

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 310

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244)) (…)

###### Art. 311

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 312

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 313

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 314

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling II - Bijzondere maatregelen

§ 1. Overdrachten onder bezwarende titel van onroerende goederen

###### Art. 315

(van toepassing vanaf 01.01.1980)
(opgeheven bij art. 42 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst van toepassing vanaf 01.01.1980 (art. 45, § 1,
4°))

(…)

###### Art. 316

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

§ 2. Burgerlijke en handelsvennootschappen

###### Art. 317

(van toepassing vanaf 01.01.1990)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 318

(van toepassing vanaf 04.05.1965)

(opgeheven bij art. 19, 2° van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

BIJBEPALINGEN BETREFFENDE DE MET HET ZEGEL GELIJKGESTELDE TAKSEN

###### Art. 319

(van toepassing vanaf 01.01.1971)

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969). Tekst van toepassing vanaf 01.01.1971 (art.
98))

(…)

###### Art. 320

(van toepassing vanaf 01.01.1971)

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969). Tekst van toepassing vanaf 01.01.1971 (art.
98))

(…)

###### Art. 321

(van toepassing vanaf 01.01.1971)

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969). Tekst van toepassing vanaf 01.01.1971 (art.
98))

(…)

INWERKINGTREDING

###### Art. 322

(van toepassing vanaf 01.02.1940)

Dit besluit treedt in werking op 1 Februari 1940.