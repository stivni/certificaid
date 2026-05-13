---
tags: ["VIII", "2.5", "2.6"]
itaa-lex-sectie: "VIII"
wet: "Wetboek der Registratie-, Hypotheek- en Griffierechten — federaal"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "01.04.2026"
bron: "onbekend"
chunk:
  level: 6
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/Registratierechten-federaal.pdf
      sha256: 768b62551dcd235cd7e3859626df172408bca181bdd6aceb8c7f153ced5d65c2
      version: 01.04.2026
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 2ab0aa1
    model:
    prompt_version:
  generated_at: '2026-05-12T21:23:24Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T10:38:29Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A2+A8+A1 bevestigd. A2: TOC met dotted-leaders (regels 67-251). A8: NL+FR tekst op één regel door bilingue bron-PDF (bv. regel 544: 'Het kantoor mag ze niet langer houden dan nodig is.  Le bureau ne peut les retenir au-delà du temps nécessaire.'). A1: titels gecombineerd als 'INWERKINGTREDING  ENTREE EN VIGUEUR' (regel 17027). Structureel probleem van bilingue PDF-bron — ETL kan NL-alleen-versie extraheren als die beschikbaar is."
    layer1:
      status: warn
      run_id: 20260513-104838
      run_at: '2026-05-13T10:48:41Z'
      heading_count: 625
      max_section_chars: 55446
      file_size_chars: 498657
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ######-niveau: 55446 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
        - name: no_toc_dots
          status: warn
          detail: 86 TOC-stippen-regel(s) gevonden
          samples:
            - '................................................................................'
            - '................................................................................'
            - '................................................................................'
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T10:38:29Z'
      rationale: "A2+A8+A1 bevestigd. A2: TOC met dotted-leaders (regels 67-251). A8: NL+FR tekst op één regel door bilingue bron-PDF (bv. regel 544: 'Het kantoor mag ze niet langer houden dan nodig is.  Le bureau ne peut les retenir au-delà du temps nécessaire.'). A1: titels gecombineerd als 'INWERKINGTREDING  ENTREE EN VIGUEUR' (regel 17027). Structureel probleem van bilingue PDF-bron — ETL kan NL-alleen-versie extraheren als die beschikbaar is."
      concrete_problemen:
        - regel: 67
          categorie: A2
          type: dotted-leader
          voorbeeld: '## TITEL I - REGISTRATIERECHT.............'
        - regel: 544
          categorie: A8
          type: column-bleed
          voorbeeld: Het kantoor mag ze niet langer houden dan nodig is.  Le bureau ne peut les retenir au-delà du temps nécessaire.
        - regel: 17027
          categorie: A1
          type: other
          voorbeeld: INWERKINGTREDING  ENTREE EN VIGUEUR
---

# Registratierechten — federaal

*Bijgewerkt tot en met 01.04.2026 — gecoördineerde versie.*

#### WETBOEK DER REGISTRATIE-, HYPOTHEEK- EN GRIFFIERECHTEN

CODE DES DROITS D’ENREGISTREMENT, D’HYPOTHEQUE ET DE GREFFE

##### Federale wetgeving

##### Législation Fédérale

(officieuze coördinatie)

(coordination officieuse)

(KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie- hypotheek- en griffierechten (B.S. 01.12.1939) err. (B.S.,

03.12.1939 en B.S. 13.12.1939). Dit KB werd bekrachtigd door art. 2 van de wet van 16 jun. 1947 (B.S. 14.08.1947) err. (B.S.,

26.10.1947))

(Arrêté royal n  64 du 30.11.1939, contenant le Code des droits d’enregistrement, d’hypothèque et de greffe (M.B., 01.12.1939)

err. (M.B., 03.12.1939 et M.B., 13.12.1939). Cet AR a été confirmé par l’art. 2 de la loi du 16 juin 1947 (M.B., 14.08.1947) err. (M.B.,

26.10.1947))

INHOUDSTAFEL:

TABLE DES MATIÈRES :

## TITEL I - REGISTRATIERECHT................................................................................................................................................ 8

### HOOFDSTUK I - Formaliteit der registratie en vestiging van de belasting .................................................................................... 8

### HOOFDSTUK II - Indeling van de rechten en algemene heffingsregels ....................................................................................... 14

### HOOFDSTUK III - Registratieverplichting .................................................................................................................................................. 17

Eerste afdeling - Akten en verklaringen aan de formaliteit onderworpen .......................................................................... 17

#### Afdeling II - Termijnen voor de aanbieding ter registratie .......................................................................................................... 23

#### Afdeling III - Personen verplicht tot aanbieding ter registratie ................................................................................................. 26

#### Afdeling IV - Plaats der registratie ........................................................................................................................................................ 29

#### Afdeling V - Sancties ................................................................................................................................................................................... 31

### HOOFDSTUK IV - Vaststelling van de rechten ........................................................................................................................................ 33

#### Afdeling I - Overdrachten onder bezwarende titel van onroerende goederen .................................................................. 33

#### Afdeling II - Openbare verkopingen van lichamelijke roerende goederen ........................................................................... 53

#### Afdeling III - (…) .............................................................................................................................................................................................. 55

#### Afdeling IV - Huurcontracten ................................................................................................................................................................... 55

#### Afdeling V - (…) ............................................................................................................................................................................................... 57

#### Afdeling VI - Hypotheekvestigingen ..................................................................................................................................................... 58

#### Afdeling VII - (…) ............................................................................................................................................................................................ 61

#### Afdeling VIII - (…) ........................................................................................................................................................................................... 62

#### Afdeling IX - Opheffingen .......................................................................................................................................................................... 63

#### Afdeling X - Verdelingen ............................................................................................................................................................................ 65

#### Afdeling XI - Vennootschappen .............................................................................................................................................................. 67

#### Afdeling XII - Schenkingen ........................................................................................................................................................................ 78

#### Afdeling XIII - Huwelijkscontracten en testamenten .................................................................................................................... 91

#### Afdeling XIV- Vonnissen en arresten ................................................................................................................................................... 91

#### Afdeling XV - (…) ............................................................................................................................................................................................ 95

#### Afdeling XVI - (…) ........................................................................................................................................................................................... 96

#### Afdeling XVII - (…) ......................................................................................................................................................................................... 96

#### Afdeling XVIII - (…) ........................................................................................................................................................................................ 96

#### Afdeling XIX - Protesten ............................................................................................................................................................................ 97

##### Afdeling XIX bis - Aangehechte akten en geschriften .................................................................................................................... 97

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en onderhevig aan het algemeen vast recht ............... 101

### HOOFDSTUK V - Registratie in debet ...................................................................................................................................................... 105

### HOOFDSTUK VI - Kosteloze registratie ................................................................................................................................................... 106

### HOOFDSTUK VII - Vrijstelling van de formaliteit der registratie ................................................................................................... 110

### HOOFDSTUK VIII - Diverse bepalingen betreffende de vereffening van de rechten en de betaling van het

verschuldigde bedrag ...................................................................................................................................................................................... 117

### HOOFDSTUK IX - Verplichtingen met het oog op het verzekeren van het heffen van de rechten ................................ 119

#### Afdeling I - Vermeldingen op te nemen in bepaalde akten ..................................................................................................... 119

#### Afdeling II - Voorschriften betreffende het uitreiken van uitgiften ...................................................................................... 120

#### Afdeling III - Repertorium van de akten ........................................................................................................................................... 122

#### Afdeling IV - Verplichting van inzageverlening ............................................................................................................................. 125

#### Afdeling V - Verplichtingen opgelegd aan openbare ambtenaren ter verzekering van de invordering der

registratierechten ...................................................................................................................................................................................... 129

d’enregistrement ....................................................................................................................................................................................... 129

### HOOFDSTUK X - Bewijsmiddelen .............................................................................................................................................................. 130

#### Afdeling I - Algemene bepalingen ...................................................................................................................................................... 130

#### Afdeling II - Controleschatting ............................................................................................................................................................. 132

### HOOFDSTUK XI - Tekort in de waardering, bewimpeling en veinzing. Sanctiën ................................................................... 138

### HOOFDSTUK XII - Correctionele straffen ............................................................................................................................................... 139

### HOOFDSTUK XIII - Teruggaaf ...................................................................................................................................................................... 145

### HOOFDSTUK XIV - Verjaring ........................................................................................................................................................................ 149

### HOOFDSTUK XV - Vervolgingen en gedingen ...................................................................................................................................... 152

### HOOFDSTUK XVI - Bijzondere bepalingen betreffende de openbare verkopingen van roerende goederen............ 156

### HOOFDSTUK XVII - Inlichtingen te verstrekken door de Algemene Administratie van de

Patrimoniumdocumentatie .......................................................................................................................................................................... 160

### HOOFDSTUK XVIII - Speciaal recht op de nationaliteit, de adelbrieven en de verzoeken tot verandering van naam

de nom ................................................................................................................................................................................................................... 162

#### Afdeling I - Nationaliteit .......................................................................................................................................................................... 163

#### Afdeling II - Open brieven van adeldom en verzoeken tot verandering van naam ....................................................... 166

#### Afdeling III - Bepaling gemeen aan afdelingen I en II ................................................................................................................. 168

### HOOFDSTUK XIX - Speciale geldboete wegens late neerlegging van aan bekendmaking onderworpen akten van

vennootschap ..................................................................................................................................................................................................... 168

## TITEL II - HYPOTHEEKRECHT ........................................................................................................................................... 169

## TITEL III - GRIFFIERECHT .................................................................................................................................................. 172

### HOOFDSTUK I - VESTIGING VAN DE BELASTING EN VASTSTELLING VAN DE RECHTEN ............................................... 172

#### Afdeling I - Rolrecht .................................................................................................................................................................................. 173

##### Afdeling I bis - Opstelrecht ...................................................................................................................................................................... 175

#### Afdeling II - Expeditierecht .................................................................................................................................................................... 176

#### Afdeling III - Legalisatie- en opzoekingsrechten .......................................................................................................................... 178

#### Afdeling IV - Recht van inschrijving in het handelsregister, in het ambachtsregister en in de registers van de

economische samenwerkingsverbanden ....................................................................................................................................... 179

groupements d'intérêt économique .................................................................................................................................................. 179

### HOOFDSTUK II - Vrijstellingen ..................................................................................................................................................................... 179

### HOOFDSTUK III - Diverse bepalingen ....................................................................................................................................................... 183

## Titel IV - Digitalisatie van de relaties tussen de Federale Overheidsdienst Financiën, de burgers en bepaalde derden .... 185

GEMEENSCHAPPELIJKE BEPALINGEN VOOR ALLE BELASTINGEN .......................................................................................... 191

DISPOSITIONS COMMUNES A TOUS LES IMPOTS ............................................................................................................................ 191

INTREKKINGSBEPALING ............................................................................................................................................................................... 259

DISPOSITION ABROGATOIRE ...................................................................................................................................................................... 259

TIJDELIJKE BEPALINGEN ................................................................................................................................................................................ 259

DISPOSITIONS TEMPORAIRES ................................................................................................................................................................... 259

#### Afdeling I - Maatregelen waarbij de oprichting van nieuwe gebouwen begunstigd wordt door een

vermindering der registratierechten ................................................................................................................................................. 259

nouveaux bâtiments ................................................................................................................................................................................ 259

#### Afdeling II - Diverse bepalingen ........................................................................................................................................................... 261

OVERGANGSBEPALINGEN ........................................................................................................................................................................... 265

DISPOSITIONS TRANSITOIRES ................................................................................................................................................................... 265

#### Afdeling I - Algemene maatregelen ................................................................................................................................................... 265

#### Afdeling II - Bijzondere maatregelen................................................................................................................................................. 266

BIJBEPALINGEN BETREFFENDE DE MET HET ZEGEL GELIJKGESTELDE TAKSEN .............................................................. 267

DISPOSITIONS ADDITIONNELLES RELATIVES AUX TAXES ASSIMILEES AU TIMBRE ....................................................... 267

INWERKINGTREDING ...................................................................................................................................................................................... 268

ENTREE EN VIGUEUR ..................................................................................................................................................................................... 268

### EN GRIFFIERECHTEN

Federale wetgeving  Législation Fédérale

(officieuze coördinatie)  (coordination officieuse)

(KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie-

hypotheek- en griffierechten (B.S. 01.12.1939) err. (B.S., 03.12.1939 en B.S.

13.12.1939). Dit KB werd bekrachtigd bij art. 2 van de wet van 16.06.1947

(B.S. 14.08.1947) err. (B.S., 26.10.1947))

## TITEL I - REGISTRATIERECHT

### HOOFDSTUK I - Formaliteit der registratie en vestiging

##### van de belasting

###### Artikel 1

(gewijzigd bij art. 79 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Registratie is een formaliteit bestaande in het afschrijven, ontleden of

vermelden van een akte of van een geschrift, in een hiertoe bestemd

register  van  de  Algemene  Administratie  van  de

Patrimoniumdocumentatie of op elke andere informatiedrager

bepaald door de Koning.

Deze formaliteit geeft aanleiding tot heffing van een belasting

genaamd registratierecht.

###### Artikel 2

(gewijzigd bij art. 111 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).

Tekst van toepassing vanaf 17.08.2020 (art. -))

De akten worden op de minuten, brevetten of originelen

geregistreerd.

De Koning kan voor de door Hem aangewezen categorieën van akten,

geschriften en verklaringen die aan de formaliteit van de registratie

onderworpen worden, bepalen dat zij onder de vorm van de minuut,

een afschrift of een kopie en al dan niet op gedematerialiseerde wijze,

ter registratie kunnen of moeten worden aangeboden. Voor de aldus

aangewezen categorieën van akten, geschriften en verklaringen

bepaalt Hij de modaliteiten van de aanbieding ter formaliteit en van

de uitvoering van de formaliteit alsook de voorschriften die voor de

juiste heffing van de verschuldigde rechten nodig zijn. Hij kan daarbij

afwijken van de bepalingen van de artikelen 6, tweede lid, 8, 9, 26, 39,

40, 168, 171 en 172 van dit Wetboek. Hij kan echter geen geldboete

opleggen met een bedrag hoger dan 25 euro in geval van overtreding

van de door hem in afwijking van de artikelen 171 en 172

vastgestelde regels.

De Koning kan bepalen dat wanneer de aanbieding ter registratie van

akten of van bepaalde categorieën van akten op gedematerialiseerde

wijze geschiedt, de aanbieding vergezeld moet gaan van

gestructureerde metagegevens betreffende de akte, waaronder in

het bijzonder, voor elke partij bij de akte, haar identificatienummer in

het Rijksregister of het haar in uitvoering van artikel 4, § 2, van de wet

van 15 januari 1990 houdende oprichting en organisatie van een

Kruispuntbank  van  de  sociale  zekerheid  toegekende

identificatienummer in het bisregister of, voor een rechtspersoon, zijn

ondernemingsnummer bedoeld in artikel III. 17 van het Wetboek van

economisch recht.

Onverminderd het derde en het vierde lid, worden de vonnissen en

arresten geregistreerd op een door de griffier eensluidend verklaard

afschrift dat op elektronische wijze wordt aangeboden, behoudens

overmacht of technische storing in welk geval de aanbieding gebeurt

op papier. De vermelding van de registratie wordt aan de griffier

verzonden samen met het geregistreerde vonnis of arrest, op

dezelfde wijze als dat laatste werd aangeboden.

Onverminderd het derde en het vierde lid, worden de onderhandse

akten geregistreerd op een origineel of op een kopie, met uitzondering

van de akten bedoeld in artikel 19, eerste lid, 3° die op een kopie

worden geregistreerd.

###### Art. 2. bis

(ingevoegd bij art. 43 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2).

Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))

2, vierde lid, voor elke partij bij de akte, wanneer dit nummer

beschikbaar is.

Deze vermelding geschiedt in de akte of, ten laatste bij de aanbieding

ervan ter registratie, in een aanvullende verklaring onderaan de akte,

getekend door de betrokken partij of door de instrumenterende

notaris, in haar naam.

###### Art. 2. ter

(ingevoegd bij art. 44 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).

Tekst van toepassing vanaf: a) wat de akten bedoeld in art. 19, 1 e lid, 3°, a),

W.Reg. betreft: vanaf 01.04.2014; b) wat de akten bedoeld in art. 19, 1 e lid, 3°,

b), van hetzelfde Wetboek betreft, vanaf 01.06.2014 (art. 87, 4°, a en b))

De vermeldingsplicht bedoeld in artikel 2 bis , eerste lid, geldt ook voor

de registratie van de akten bedoeld in artikel 19, eerste lid, 3°, wat

betreft rechtspersonen.

Indien aan een partij bij een dergelijke akte nog geen

ondernemingsnummer is toegekend, bevestigt die partij dit in de akte

of in een ondertekende aanvullende verklaring onderaan de akte.

###### Art. 2. quater

(lid 3, vervangen bij art. 58 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.

2). Tekst van toepassing vanaf 09.06.2024 (art. -))

De registratie van een akte bedoeld in artikel 19, eerste lid, 3°, al dan

niet samen met bijlagen, of van een plaatsbeschrijving die niet samen

met de hiervoor bedoelde akte wordt aangeboden, is, in geval van

aanbieding op een papierendrager, afhankelijk van de aanbieding

samen met de te registreren documenten van een volledig en

leesbaar ingevuld formulier waarvan het model wordt bepaald door

de Koning.

Het formulier kan de verplichte vermelding bevatten van het

identificatienummer of het ondernemingsnummer, bedoeld in artikel

2, vierde lid, van de partijen bij de akte, wanneer dit nummer

beschikbaar is.

bepaald.

In geval de uitvoering van de formaliteit van de registratie wordt

geweigerd wegens niet naleving van de voorgaande bepalingen,

wordt de verzoeker daarvan in kennis gesteld.

Dit artikel is niet van toepassing in het geval bepaald in artikel 25.

###### Artikel 3

(gewijzigd bij art. 80 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Wordt een in een andere taal dan de landstalen gestelde akte of

geschrift ter registratie aangeboden, zo kan het bevoegde kantoor

van de Algemene Administratie van de Patrimoniumdocumentatie

eisen dat, op de kosten van de persoon die de formaliteit vordert, een

door een beëdigde vertaler voor echt verklaarde vertaling daaraan

worde toegevoegd.

###### Artikel 4

De registratie is ondeelbaar: zij wordt toegepast op de gehele akte of

het geheel geschrift welke tot de formaliteit wordt aangeboden.

###### Artikel 5

(opgeheven bij art. 3 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1).

Tekst van toepassing vanaf 29.06.2020 (art. -))

(…)

###### Art. 5. bis

(vervangen bij art. 93 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed.

1). Tekst van toepassing vanaf 07.02.2022 (art. -))

verschillen.

Bij gelijktijdige aanbieding tot de formaliteiten, wordt de registratie

van de akte geweigerd zolang op dit kantoor de overschrijving wordt

geweigerd.

Het eerste en tweede lid zijn niet van toepassing op een akte die enkel

de niet-vatbaarheid voor beslag vaststelt van de woning van een

zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse

bepalingen (IV).

###### Artikel 6

(gewijzigd bij art. 82 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Het bevoegde kantoor van de Algemene Administratie van de

Patrimoniumdocumentatie is gehouden tot het registreren van de

akten of geschriften op de datum waarop ze onder de wettelijke

voorwaarden tot de formaliteit worden aangeboden.

Een buiten de openingsuren van de kantoren aangeboden akte of

geschrift, wordt geacht aangeboden te zijn bij de eerstvolgende

opening van de kantoren.

Het kantoor mag ze niet langer houden dan nodig is.  Le bureau ne peut les retenir au-delà du temps nécessaire.

###### Artikel 7

(gewijzigd bij art. 83 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Zo een akte of geschrift, waarvan er geen minuut bestaat, inlichtingen

vervat die kunnen dienen om aan 's Rijks schatkist verschuldigde

sommen te ontdekken, heeft het bevoegde kantoor van de Algemene

Administratie van de Patrimoniumdocumentatie het recht er een

afschrift van te maken en dit eensluidend met het origineel te doen

waarmerken door de werkende openbare officier of, zo het gaat om

een onderhandse of buitenlands verleden akte, door de betrokken

persoon die de formaliteit heeft gevorderd. Bij weigering, waarmerkt

het bevoegde kantoor zelf de eensluidendheid van het afschrift, met

vermelding van die weigering. Het aldus gewaarmerkt afschrift

###### Artikel 8

(gewijzigd bij art. 4 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1). Tekst

van toepassing vanaf 29.06.2020 (art. -))

Vermelding van de registratie wordt op de akte of het geschrift

gesteld naar een door de minister van Financiën bepaalde tekst.

Voor akten en geschriften als bedoeld in artikel 2 quater , wordt de

vermelding van de registratie gesteld volgens door de Koning te

bepalen nadere regels.

Indien er toepassing gemaakt wordt van de vrijstelling voorzien in

###### Art. 8. bis , wordt de vermelding van de registratie vervangen door de

vermelding van de betaling die verricht moet worden volgens de

modaliteiten voorzien in uitvoering van dit artikel. Deze vermelding

geschiedt naar een door de Minister van Financiën vastgestelde tekst.

###### Art. 8. bis

(ingevoegd bij art. 135 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

De Koning kan bepaalde categorieën van de in de artikelen 19, 1° en

6°, 26 en 29 bedoelde akten van de registratieformaliteit vrijstellen

zonder dat deze vrijstelling de ontheffing van de op deze akten

toepasselijke rechten meebrengt, alsook de betalingsmodaliteiten

voor genoemde rechten, binnen de termijnen die Hij bepaalt, regelen,

in voorkomend geval afwijkend van de bepalingen van hoofdstuk III

en IX van deze titel. Indien er toepassing gemaakt wordt van deze

bepaling kan de Koning het neerleggen van een afschrift van de akten

voorschrijven en aanvullende regels vaststellen om de juiste heffing

van de belasting te verzekeren.

###### Artikel 9

(gewijzigd bij art. 12 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van

toepassing vanaf 01.03.2021 (art. -))

Valt de laatste dag van de termijn, die door onderhavig Wetboek

vastgesteld is voor de uitvoering van een formaliteit, op een

### HOOFDSTUK II - Indeling van de rechten en algemene

##### heffingsregels

###### Artikel 10

(gewijzigd bij art. 136 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Er zijn evenredige en vaste registratierechten.  Les droits d’enregistrement sont proportionnels ou fixes.

Vaste rechten zijn verdeeld in algemeen vast recht en specifieke vaste

rechten.

###### Artikel 11

(gewijzigd bij art. 11 van de Programmawet van 28.06.2013 (B.S.,

01.07.2013 - ed. 2). Tekst van toepassing op alle akten en geschriften die

vanaf 01.07.2013 tot de formaliteit worden aangeboden (art. 13))

De evenredige en de specifieke vaste rechten worden geheven

volgens het in dit Wetboek vastgestelde tarief.

Het algemeen vast recht is van toepassing op al de in dat tarief niet

voorziene akten en geschriften.

Het algemeen vast recht bedraagt 50 EUR.  Le montant du droit fixe général est de 50 EUR.

###### Artikel 12

Het evenredig of specifiek vast recht wordt slechts eenmaal op een

rechtshandeling geheven, wat ook het getal zij van de geschriften die

daarvan laten blijken.

###### Artikel 13

heeft:

1° Alle nieuw geschrift opgemaakt om te laten blijken van een

rechtshandeling waarop reeds het evenredig of specifiek vast recht

werd geheven;

2° Alle geschrift houdende bekrachtiging, bevestiging, uitvoering, aan

vulling of voltrekking van geregistreerde vroegere akten, indien het

niet laat blijken van nieuwe rechtshandelingen welke als dusdanig aan

een evenredig of specifiek vast recht onderhevig zijn.

Geven insgelijks slechts aanleiding tot heffing van het algemeen vast

recht, die rechtshandelingen welke ter oorzake van nietigheid,

ontbinding of om andere reden opnieuw werden verricht zonder enige

verandering  welke  iets  toevoegt  aan  het  voorwerp  der

overeenkomsten of aan derzelver waarde, ten ware het op de eerste

handeling geheven evenredig recht teruggegeven werd of voor

teruggaaf vatbaar zij.

###### Artikel 14

(vervangen bij art. 2 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Wanneer een akte verscheidene onder dezelfde contractanten tot

stand gekomen beschikkingen vervat, welke de ene van de andere

afhankelijk zijn of de ene uit de andere noodzakelijk voortvloeien, is

slechts één recht voor deze gezamenlijke beschikkingen verschuldigd.

Het recht wordt geheven met inachtneming van diegene van

bedoelde beschikkingen welke tot het hoogste recht aanleiding geeft.

###### Artikel 15

Wanneer, in een akte, verscheidene onafhankelijke of niet

noodzakelijk uit elkaar voortvloeiende beschikkingen voorkomen, is

voor elk dier beschikkingen en wel naar eigen aard een bijzonder recht

verschuldigd.

Deze regel is niet van toepassing op het algemeen vast recht.  Cette règle n’est pas applicable au droit fixe général.

###### Artikel 16

welke aan een schorsende voorwaarde onderworpen is, geeft alleen

tot heffing van het algemeen vast recht aanleiding zolang de

voorwaarde niet is vervuld.

Wordt de voorwaarde vervuld, zo is het recht verschuldigd dat bij het

tarief voor de handeling is vastgesteld, behoudens toerekening van

het reeds geheven recht. Het wordt berekend naar het tarief dat van

kracht was op de datum waarop het recht aan de Staat zou verworven

geweest zijn indien de handeling een onvoorwaardelijke was

geweest, en op de bij dit wetboek vastgelegde en op de datum van de

vervulling der voorwaarde beschouwde belastbare grondslag.

###### Artikel 17

Wordt, voor de toepassing van dit wetboek, met een aan een

schorsende voorwaarde onderworpen handeling gelijkgesteld, de

rechtshandeling door een rechtspersoon verricht en aan machtiging,

goedkeuring of bekrachtiging van overheidswege onderworpen.

###### Artikel 18

(§ 2, vervangen bij art. 168 van de programmawet van 29.03.2012 (B.S.,

06.04.2012 - ed. 3). Tekst van toepassing te weten op de rechtshandelingen

of het geheel van rechtshandelingen die éénzelfde verrichting tot stand brengt,

die zijn gesteld vanaf 01.06.2012 (art. 169))

§ 1. De datum van de onderhandse akten over 't algemeen of van de

overeenkomsten die door het feit alleen van haar bestaan verplicht

aan de formaliteit van registratie onderworpen zijn, kan niet tegen het

bestuur worden ingeroepen dan voor zover hij tegen derden kan

worden ingeroepen. Registratie sluit geen erkenning door het bestuur

in van de datum der akte of der overeenkomst.

§ 2. Aan de administratie kan niet worden tegengeworpen, de

rechtshandeling noch het geheel van rechtshandelingen dat een

zelfde verrichting tot stand brengt, wanneer de administratie door

vermoedens of door andere in artikel 185 bedoelde bewijsmiddelen

en aan de hand van objectieve omstandigheden aantoont dat er

sprake is van fiscaal misbruik.

Er is sprake van fiscaal misbruik wanneer de belastingschuldige door

middel van de door hem gestelde rechtshandeling of het geheel van

1. een verrichting waarbij hij zichzelf in strijd met de doelstellingen van

een bepaling van dit Wetboek of de ter uitvoering daarvan genomen

besluiten buiten het toepassingsgebied van die bepaling plaatst; of

2. een verrichting waarbij aanspraak wordt gemaakt op een

belastingvoordeel voorzien door een bepaling van dit Wetboek of de

ter uitvoering daarvan genomen besluiten en de toekenning van dit

voordeel in strijd zou zijn met de doelstellingen van die bepaling en die

in wezen het verkrijgen van dit voordeel tot doel heeft.

Het komt aan de belastingschuldige toe te bewijzen dat de keuze voor

zijn rechtshandeling of het geheel van rechtshandelingen door andere

motieven verantwoord is dan het ontwijken van registratierechten.

Indien de belastingschuldige het tegenbewijs niet levert, dan wordt de

verrichting aan een belastingheffing overeenkomstig het doel van de

wet onderworpen alsof het misbruik niet heeft plaatsgevonden.

### HOOFDSTUK III - Registratieverplichting

Eerste afdeling - Akten en verklaringen aan de formaliteit

onderworpen

###### Artikel 19

(lid 1, 5°, gewijzigd bij art. 20 van de wet van 10.02.2026 (B.S., 27.02.2026).

Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Moeten binnen de bij artikel 32 gestelde termijnen geregistreerd

worden:

1° De akten van notarissen; de exploten en processen-verbaal van

gerechtsdeurwaarders, met uitzondering van de protesten zoals

bedoeld in de protestwet van 3 juni 1997; de arresten en vonnissen

der hoven en rechtbanken die bepalingen bevatten welke door deze

### titel aan een evenredig recht onderworpen worden;

2° De akten waarbij de eigendom of het vruchtgebruik van in België

gelegen onroerende goederen overgedragen of aangewezen wordt;

een gezin of van één persoon;

b) De andere dan onder a) bedoelde akten houdende verhuring,

onderverhuring of overdracht van huur van in België gelegen

onroerende goederen of gedeelten van onroerende goederen.

4° De processen-verbaal van openbare verkoping van lichamelijke

roerende voorwerpen;

5° De akten houdende inbreng van goederen in vennootschappen

met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke

leiding in België, hetzij de statutaire zetel in België en de zetel der

werkelijke leiding buiten het grondgebied van de lidstaten van de

Europese Unie, is gevestigd;

6° de in het buitenland verleden notariële akten die titel vormen voor

een schenking onder de levenden van roerende goederen door een

rijksinwoner.

Onverminderd de bepaling onder 6° van het eerste lid en behoudens

wat de bepalingen onder 2°, 3° en 5° van hetzelfde lid betreft,

worden in dit artikel alleen de in België verleden akten bedoeld.

###### Artikel 20

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van

toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Art. 21. 1

(vervangen bij art. 59 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing vanaf 09.06.2024 (art. -))

De bevoegde dienst van de Algemene administratie van de

patrimoniumdocumentatie neemt een kopie bij de aanbieding ter

registratie op een papieren drager van de volgende akten, haar

bijlagen en alle andere tegelijk aan te bieden stukken, geschriften en

verklaringen:

1° de plaatsbeschrijving bedoeld in artikel 2 quater , eerste lid;

is gevoegd;

3° de onderhandse of in het buitenland verleden akten bedoeld in

artikel 19, eerste lid, 3°, 5° en 6°, behalve wanneer het gaat om een

akte welke onder de minuten van een notaris in België berust of bij

zijn minuten is gevoegd;

4° de verklaringen bedoeld in artikel 31.

De Koning kan de categorie van akten, geschriften en verklaringen

bedoeld in het eerste lid vervolledigen of wijzigen.

De kopie bedoeld in het eerste lid wordt minstens gedurende tien jaar

bewaard door de bevoegde dienst van de Algemene administratie van

de patrimoniumdocumentatie, voor zover deze niet wordt

overgedragen aan het Rijksarchief of vernietigd in uitvoering van de

artikelen 1 en 5 van de archiefwet Wet van 24 juni 1955.

###### Art. 21. 2

(gewijzigd bij art. 1 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van

toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van

19.12.1969 (B.S., 20.12.1969))

Als onroerende goederen worden niet beschouwd:  Ne sont pas considérés comme immeubles :

1° Voor de toepassing van de artikelen 19, 3° en 83, brandkasten, in

huur gegeven door personen, verenigingen, gemeenschappen of

vennootschappen die gewoonlijk brandkasten verhuren;

2° Voor de toepassing van dit Wetboek, lichamelijk roerende

voorwerpen aangewend tot de dienst en de exploitatie van

onroerende goederen.

###### Artikel 22

(opgeheven bij art. 3 van de wet van 10.06.1997 (B.S., 19.07.1997). Tekst van

toepassing voor de effecten die ter betaling worden aangeboden vanaf

23.09.1997 (art. 10, KB van 15.09.1997 (B.S., 23.09.1997))

(…)

De exequaturs der scheidsrechterlijke uitspraken en die der

buitenslands gewezen rechterlijke beslissingen  moeten,  bij

aanbieding ter registratie, vergezeld zijn van de desbetreffende

uitspraken of beslissingen.

###### Artikel 24

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van

toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Artikel 25

(gewijzigd bij art. 3 van de wet van 03.12.2020 (B.S., 11.12.2020 - ed. 1). Tekst

van toepassing vanaf 15.12.2020 (art. 5))

Wanneer een onderhandse of in het buitenland verleden akte bedoeld

in artikel 19, eerste lid, 2°, 3°, 5° of 6°, terzelfdertijd van een niet

verplicht in België te registreren overeenkomst doet blijken, kunnen

de betrokkenen een door hen gewaarmerkt beknopt uittreksel (1) uit

de akte doen registreren waarin alleen melding wordt gemaakt van

de overeenkomsten die verplicht in België te registreren zijn.

Het uittreksel wordt in dubbel opgemaakt. Wanneer beide

exemplaren ter registratie worden aangeboden, moeten ze vergezeld

zijn van de oorspronkelijke akte of, zo het een buitenslands verleden

authentieke akte in minuut geldt, van een uitgifte daarvan. De heffing

wordt beperkt tot die goederen welke het voorwerp van het uittreksel

uitmaken. Een exemplaar van dit uittreksel blijft op het bevoegde

kantoor  van  de  Algemene  Administratie  van  de

Patrimoniumdocumentatie berusten.

-----------

Nota:

(1) ‘uittrek-sel’ in het B.S.

###### Artikel 26

(laatste lid vervangen bij art. 47 van de wet van 21.12.2013 (B.S., 31.12.2013

- ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))

neergelegd zonder te voren geregistreerd te zijn.

Evenwel staat het de notarissen en de gerechtsdeurwaarders vrij de

aangehechte of neergelegde akte tegelijk met de desbetreffende akte

ter registratie aan te bieden.

De in het eerste lid bedoelde verplichting is niet van toepassing:

1° in geval van aanhechting of van neerlegging, onder de vorm van

minuut, uitgifte, afschrift of uittreksel, van in België verleden

gerechtelijke akten of akten van de burgerlijke stand;

2° in geval van aanhechting of van neerlegging van een plan dat is

opgenomen in de databank van plannen van afbakening van de

Algemene Administratie van de Patrimoniumdocumentatie, op

voorwaarde dat de akte, of een door de partijen of de

instrumenterende ambtenaar, in hun naam, ondertekende verklaring

onderaan de akte, verwijst naar deze opname met vermelding van het

refertenummer van het plan en bevestigt dat het plan nadien niet is

gewijzigd.

###### Artikel 27

(opgeheven bij art. 19 van de wet van 01.07.1983 (B.S., 08.07.1983). Tekst

van toepassing vanaf 18.07.1983 (art. -))

(…)

###### Artikel 28

(opgeheven bij art. 2/art. 28 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,

13.11.1968))

(…)

###### Artikel 29

(gewijzigd bij art. 87 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

krachtens niet vooraf geregistreerde akten.

###### Artikel 30

(gewijzigd bij art. 88 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Op vorig artikel wordt uitzondering gemaakt voor de overschrijvingen,

inschrijvingen, doorhalingen of randvermeldingen gedaan krachtens

akten in verband met scheepskredietverrichtingen gedaan onder het

voordeel der wet van 23 augustus 1948 of met kredietverrichtingen

gedaan onder het voordeel der wet tot bevordering van de

financiering van de voorraden van de steenkoolmijnen.

Op vorig artikel wordt eveneens uitzondering gemaakt voor de in

België verleden gerechtelijke akten van de burgerlijke stand, in

minuut, uitgifte, afschrift of uittreksel.

###### Artikel 31

(lid 1, 1°bis, gewijzigd bij art. 21 van de wet van 10.02.2026 (B.S.,

27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Er bestaat verplichting tot ondertekening en tot aanbieding ter

registratie, binnen de bij artikel 33 gestelde termijnen, van een

verklaring in onderstaande gevallen:

1° Wanneer een overeenkomst, waarbij eigendom of vruchtgebruik

van in België gelegen onroerende goederen overgedragen of

aangewezen wordt, niet bij een akte is vastgesteld;

1° bis Wanneer een inbreng van goederen in een vennootschap met

rechtspersoonlijkheid, waarvan hetzij de zetel der werkelijke leiding in

België, hetzij de statutaire zetel in België en de zetel der werkelijke

leiding buiten het grondgebied van de lidstaten van de Europese Unie,

is gevestigd, niet bij een akte is vastgesteld;

1° ter (…)

2° Wanneer de voorwaarde die de heffing van een recht heeft

geschorst, vervuld wordt;

3° In de in artikelen 74 en 75 bedoelde gevallen.  3  Dans les cas visés aux articles 74 et 75.

overeenkomst, de datum ervan of de datum van het nieuwe feit dat

de verschuldigdheid van het recht heeft doen ontstaan, de aanwijzing

van de partijen, de omvang van de goederen, de belastbare grondslag

en alle voor de vereffening van de belasting nodige gegevens. Een

kopie wordt bewaard door de bevoegde dienst van de Algemene

administratie van de patrimoniumdocumentatie.

Vanaf het verstrijken van vorenstaande termijnen wordt de door een

der partijen ondertekende verklaring als van al de partijen uitgaande

aangezien.

#### Afdeling II - Termijnen voor de aanbieding ter registratie

###### Artikel 32

(7°, gewijzigd bij art. 22 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

De termijnen voor de aanbieding ter registratie van verplicht te

registreren akten zijn:

1° voor akten van notarissen, vijftien dagen;  1° de quinze jours pour les actes des notaires ;

De termijn is evenwel:  Le délai est toutefois :

a) twee maanden, voor de in het kader van een openbare verkoop van

een onroerende goed opgemaakte processen-verbaal van:

i.   het ontbreken van hoger bod;  i.   l’absence de surenchère ;

ii. definitieve toewijs;  ii. l’adjudication définitive ;

iii. het al dan niet uitoefenen van een voorkooprecht;  iii. l’exercice ou non d’un droit de préemption ;

iv. het vaststellen van het bekomen van een financiering;  iv. la constatation de l’obtention d’un financement ;

b) vier maanden, te rekenen van het overlijden van de erflaters of

schenkers voor:

i.   de testamenten;  i.   les testaments ;

ii. de schenkingen van toekomstige goederen gedaan tussen

echtgenoten  gedurende  het  huwelijk  andere  dan  bij

huwelijkscontract;

iv. de verklaringen betreffende testamenten in de internationale

vorm;

v.   de akten van bewaargeving van een testament door de erflater.  v.   les actes constatant le dépôt d’un testament par le testateur.

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten

van de registratie en van de hypothecaire overschrijving die bij de

aanbieding ter registratie binnen de in het eerste lid gestelde termijn

niet werden geregistreerd wegens de weigering van de

overschrijving, bedraagt de termijn zeven dagen te rekenen van de

datum van de kennisgeving aan de notaris van deze weigering. Deze

termijn verstrijkt niet voor het einde van de termijn bepaald,

naargelang het geval, in het eerste lid of in het tweede lid, a);

2° Voor akten van gerechtsdeurwaarders, vier dagen;  2° De quatre jours, pour les actes des huissiers de justice ;

3° voor arresten en vonnissen der hoven en rechtbanken, tien dagen;  3° De dix jours, pour les arrêts et jugements des cours et tribunaux ;

3° bis voor akten van bestuursoverheden en ambtenaren van de

Staat, gefedereerde entiteiten, provincies, gemeenten en openbare

instellingen die verplicht onderworpen zijn aan de formaliteit van de

registratie en aan die van de hypothecaire overschrijving, vijftien

dagen;

De termijn is evenwel twee maanden voor de in het kader van een

openbare verkoop van een onroerende goed opgemaakte processen-

verbaal van:

a) het ontbreken van hoger bod;  a) l’absence de surenchère ;

b) definitieve toewijs;  b) l’adjudication définitive ;

c) het al dan niet uitoefenen van een voorkooprecht;  c) l’exercice ou non d’un droit de préemption ;

d) het vaststellen van het bekomen van een financiering.  d) la constatation de l’obtention d’un financement.

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten

van de registratie en van de hypothecaire overschrijving, die bij de

aanbieding ter registratie binnen de in het eerste lid gestelde termijn

niet werden geregistreerd wegens de weigering van de

overschrijving, bedraagt de termijn zeven dagen te rekenen van de

datum van de kennisgeving van deze weigering aan de

bestuursoverheden of ambtenaren van de Staat, gefedereerde

entiteiten, provincies, gemeenten en openbare instellingen. Deze

termijn verstrijkt niet voor het einde van de termijn bepaald,

naargelang het geval, in het eerste lid of in het tweede lid;

5° Voor akten van verhuring, onderverhuring of overdracht van huur

bedoeld in artikel 19, 3°, a), twee maanden en voor akten van

verhuring, onderverhuring of overdracht van huur bedoeld in artikel

19, 3°, b), vier maanden;

6° Voor processen-verbaal van openbare verkoping van lichamelijke

roerende goederen opgemaakt door bestuursoverheden en

ambtenaren van de Staat, gefedereerde entiteiten, provincies,

gemeenten en openbare instellingen, één maand;

7° Voor akten houdende inbreng van goederen in vennootschappen

met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke

leiding in België, hetzij de statutaire zetel in België en de zetel der

werkelijke leiding buiten het grondgebied van de lidstaten van de

Europese Unie is gevestigd, vier maanden;

8° voor de in artikel 19, eerste lid, 6°, bedoelde akten, vier maanden.

###### Artikel 33

(gewijzigd bij art. 60 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 01.04.1999 (art. 80, § 31))

De termijn, binnen welke de in artikel 31 voorziene verklaringen ter

registratie moeten aangeboden worden, is vier maand ingaande met

de datum van de overeenkomst of, in voorkomend geval, van de

vervulling van de voorwaarde welke de heffing van het recht heeft

geschorst.

###### Artikel 34

(opgeheven bij art. 77 van de wet van 18.12.2015 (B.S., 28.12.2015 - ed. 2).

Tekst van toepassing vanaf 07.01.2016 (art. -))

(…)

Vierde lid: gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van

16.01.1989 betreffende de financiering van de gemeenschappen en de

gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 35

(lid 5, vervangen bij art. 61 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De verplichting tot aanbieding ter registratie van akten of verklaringen

en tot betaling van de des betreffende rechten en gebeurlijk de

geldboeten, waarvan de vorderbaarheid uit bewuste akten of

verklaringen blijkt, berust ondeelbaar:

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de

akten van hun ambt;

2° (…)  2  (…)

3° (…)  3  (…)

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de

akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in

handen neergelegd, zonder voorafgaande registratie;

5° Op de bestuursoverheden en ambtenaren van de Staat,

gefedereerde entiteiten, provincies, gemeenten en openbare

instellingen, ten aanzien van de door hen opgemaakte akten;

6° Op de contracterende partijen, ten aanzien van de onderhandse of

buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b)

en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands

verleden akten waarvan sprake in artikel 19, 3°, a);

8° op de contracterende partijen ten aanzien van de in artikel 19,

eerste lid, 6°, bedoelde akten.

De verplichting tot aanbieding ter registratie van de arresten en

vonnissen van hoven en rechtbanken berust op de griffiers. In

afwijking van artikel 169 ter worden deze arresten en vonnissen in

debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten

waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van

hoofdelijk in geval van hoofdelijke veroordeling.

Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een

overeenkomst waarbij de eigendom of het vruchtgebruik van in België

gelegen onroerende goederen overgedragen of aangewezen wordt, zijn

die rechten en boeten ondeelbaar verschuldigd door de personen die

partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald

binnen de termijn van één maand, te rekenen vanaf de dag van de

verzending van de aangetekende zending van het belastingbericht

door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van

de boeten geen gekende woonplaats in België of in het buitenland

heeft, wordt het bericht aan de procureur des Konings te Brussel

verzonden.

-----

#### Afdeling III - Personen verplicht tot aanbieding ter

registratie

###### Artikel 35

(gewijzigd bij art. 95 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).

Tekst van toepassing vanaf 07.02.2022 (art. -))

De verplichting tot aanbieding ter registratie van akten of verklaringen

en tot betaling van de des betreffende rechten en gebeurlijk de

geldboeten, waarvan de vorderbaarheid uit bewuste akten of

verklaringen blijkt, berust ondeelbaar:

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de

akten van hun ambt;

2° (…)  2  (…)

3° (…)  3  (…)

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de

akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in

handen neergelegd, zonder voorafgaande registratie;

6° Op de contracterende partijen, ten aanzien van de onderhandse of

buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b)

en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands

verleden akten waarvan sprake in artikel 19, 3°, a);

8° op de contracterende partijen ten aanzien van de in artikel 19,

eerste lid, 6°, bedoelde akten.

De verplichting tot aanbieding ter registratie van de arresten en

vonnissen van hoven en rechtbanken berust op de griffiers. In

afwijking van artikel 169 ter worden deze arresten en vonnissen in

debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten

waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van

hoven en rechtbanken, berust op de verweerders, elkeen in de mate

waarin de veroordelingen, vereffeningen of rangregelingen te zijnen

laste werden uitgesproken of vastgesteld, en op de verweerders

hoofdelijk in geval van hoofdelijke veroordeling.

Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een

overeenkomst waarbij de eigendom of het vruchtgebruik van in België

gelegen onroerende goederen overgedragen of aangewezen wordt, zijn

die rechten en boeten ondeelbaar verschuldigd door de personen die

partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald

binnen de termijn van één maand, te rekenen vanaf de dag van de

verzending van het belastingbericht bij ter post aangetekende brief

door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van

de boeten geen gekende woonplaats in België of in het buitenland

heeft, wordt het bericht aan de procureur des Konings te Brussel

verzonden.

###### Artikel 36

(gewijzigd bij art. 96 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).

Tekst van toepassing vanaf 07.02.2022 (art. -))

en eventueel van de boeten uiterlijk daags vóór het verstrijken van de

voor de registratie gestelde termijn in handen der notarissen niet

hebben geconsigneerd.

###### Artikel 37

(gewijzigd bij art. 97 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).

Tekst van toepassing vanaf 07.02.2022 (art. -))

Wanneer de rechten betreffende testamenten en andere in artikel 32,

1°, tweede lid, b), bedoelde akten niet in handen der notarissen

werden geconsigneerd, zijn ze ondeelbaar door de erfgenamen,

legatarissen of begiftigden zomede door de testamentuitvoerders

verschuldigd.

###### Artikel 38

(opgeheven bij art. 140 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling IV - Plaats der registratie

###### Artikel 39

(1° en 4°, vervangen bij art. 98 van de wet van 21.01.2022 (B.S., 28.01.2022

- ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))

De akten en verklaringen worden geregistreerd:  Les actes et déclarations sont enregistrés, savoir :

1° de akten van notarissen en gerechtsdeurwaarders, op het kantoor

bevoegd voor hun standplaats;

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde

onroerende goed wordt evenwel geregistreerd een akte die

cumulatief:

a) onder de toepassing valt van het koninklijk besluit van 14 maart

2014 houdende regeling van de aanbieding van akten van bepaalde

b) onroerende goederen betreft die alle gelegen zijn buiten het

ambtsgebied van het kantoor bevoegd voor de standplaats;

c) gelijktijdig ter overschrijving wordt aangeboden.  c) est présenté simultanément à la transcription.

Het tweede lid is niet van toepassing op een akte die enkel de van

niet-vatbaarheid voor beslag vaststelt van de woning van een

zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse

bepalingen (IV);

1° bis (…)

2° De arresten en vonnissen der hoven en rechtbanken, ten kantore

in welks gebied de zetel van het hof of de rechtbank gelegen is;

3° De akten die overeenkomstig artikel 26 zonder voorafgaande

registratie worden aangehecht of neergelegd, ten kantore waar de

akte van de notaris of de gerechtsdeurwaarder moet worden

geregistreerd;

4° De akten van bestuursoverheden en ambtenaren van de Staat,

gefedereerde entiteiten, provincies, gemeenten en openbare

instellingen, op het kantoor bevoegd voor hun zetel of standplaats;

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde

onroerende goed wordt evenwel geregistreerd een akte die

cumulatief:

a) onder de toepassing valt van het koninklijk besluit van 14 maart

2014 houdende regeling van de aanbieding van akten van bepaalde

instrumenterende ambtenaren tot de registratieformaliteit en tot de

hypothecaire openbaarmaking;

b) onroerende goederen betreft die alle gelegen zijn buiten het

ambtsgebied van het kantoor bevoegd voor de zetel of de

standplaats;

c) gelijktijdig ter overschrijving wordt aangeboden;  c) est présenté simultanément à la transcription ;

5° De onderhandse of buitenslands verleden akten en de

verklaringen betreffende in België gelegen onroerende goederen en

welke in artikel 19, 2° en 3° en in artikel 31, 1° en 3°, zijn bedoeld,

ten kantore in welks gebied de goederen gelegen zijn. Zijn die

goederen gelegen in het gebied van verscheidene kantoren, dan

mogen de akten en verklaringen onverschillig in een van deze

kantoren worden geregistreerd;

geregistreerd welke van de overeenkomst laat blijken, of, bij gebreke

aan geregistreerde akte, ten kantore in het 5° hiervoren aangeduid;

7° De andere akten dan voornoemde, onverschillig in alle kantoren.  7° Les actes autres que ceux qui précèdent, dans tous les bureaux

###### Artikel 40

(opgeheven bij art. 27 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).

Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

#### Afdeling V - Sancties

###### Artikel 41

(gewijzigd bij art. 4 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van

toepassing vanaf 01.01.2015 (art. 8))

Verbeuren ondeelbaar een geldboete gelijk aan het bedrag der

rechten, zonder dat ze lager dan 25 EUR mag zijn:

1° de personen die binnen de voorgeschreven termijnen, de akten of

verklaringen niet hebben doen registreren welke zij gehouden zijn aan

de formaliteit te onderwerpen of de in artikel 169 ter , tweede lid,

bedoelde betaling niet hebben gedaan;

2° De in artikel 37 aangewezen personen die, binnen den hun daartoe

gestelden termijn, de bij artikel 36 voorziene consignatie niet hebben

gedaan.

3° De in artikel 35, derde en vierde lid aangewezen personen die de

betaling bedoeld in het vijfde lid van genoemde artikel niet hebben

gedaan binnen de voorgeschreven termijn.

###### Art. 41. bis

(gewijzigd bij art. 54 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

voorgeschreven wijze en binnen de voorgeschreven termijn, die geen

afschrift van deze akten neergelegd hebben of die zich niet gehouden

hebben aan de door de Koning bepaalde aanvullende regels in

uitvoering van artikel 8 bis , verbeuren ondeelbaar een boete van 25

EUR tot 250 EUR per overtreding.

Het bedrag van de boete wordt, binnen deze grenzen, vastgesteld

door de bevoegde adviseur-generaal van de Algemene Administratie

van de Patrimoniumdocumentatie.

De in het eerste lid bedoelde personen verbeuren ondeelbaar een

boete gelijk aan de ontdoken rechten voor elke akte waarop zij ten

onrechte de vrijstelling van de formaliteit bedoeld in artikel 8 bis ,

toegepast hebben.

###### Artikel 42

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Voor elke overtreding van artikel 26 verbeurt de notaris of de

gerechtsdeurwaarder een boete van 25 EUR.

###### Artikel 43

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

De griffiers die binnen de voorgeschreven termijn de arresten en

vonnissen niet hebben doen registreren welke zij gehouden zijn aan

de formaliteit te onderwerpen, verbeuren voor elke overtreding een

boete van 25 EUR.

###### Art. 44. tot 50 W.Reg. federaal

###### Art. 44 à 50 C. enr. fédéral

Het registratierecht op de inbreng door een natuurlijke persoon van

een woning in een buitenlandse vennootschap (art. 44 tot 50 W.Reg.)

is een federale belasting (art. 3, eerste lid, 6°, wet 16.01.1989

#### Afdeling I - Overdrachten onder bezwarende titel van

onroerende goederen

§ 1. Algemene bepalingen

###### Artikel 44

(gewijzigd bij art. 40 van de wet van 30.03.1994 (BS., 31.03.1994 - ed. 2).

Tekst van toepassing vanaf 10.04.1994 (art. - ))

Het recht wordt gesteld op 12,50 t.h. voor de verkopingen, ruilingen

en alle overeenkomsten onder bezwarende titel, waarbij eigendom of

vruchtgebruik van onroerende goederen wordt overgedragen.

Eerste lid, streepje 1,2 en 4: gewestelijke bepalingen (art. 3, eerste lid, 6° van

de wet van 16.01.1989 betreffende de financiering van de gemeenschappen

en de gewesten)

###### Artikel 45

(aangevuld bij art. 41 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).

Tekst van toepassing vanaf 10.04.1994 (art. -))

Het recht wordt vereffend:  Le droit est liquidé, savoir :

- ten aanzien van verkopingen, op het bedrag van bedongen prijs en

lasten;

- ten aanzien van de ruilingen, op de overeengekomen waarde van de

in een der prestatiën begrepen goederen, met inachtneming van die

welke aanleiding tot het hoogste recht zou geven zoo beide waren

toegestaan tegen een naar die waarde vastgestelde geldprijs;

- ten aanzien van inbrengen van onroerende goederen in

vennootschappen, andere dan inbrengen als vermeld in artikel 115 bis ,

op de waarde van de als vergoeding van de inbreng toegekende

- ten aanzien van de overige overdragende overeenkomsten, op de

overeengekomen waarde van de ten laste van de verkrijger van het

onroerend goed bedongen tegenprestatie.

###### Artikel 46

Evenwel mag de belastbare grondslag in geen geval lager zijn dan de

verkoopwaarde van de overgedragen onroerende goederen.

###### Artikel 47

(gewijzigd bij art. 3 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Wanneer de overeenkomst op het vruchtgebruik van een onroerend

goed slaat, wordt de in artikel 46 bedoelde verkoopwaarde

vertegenwoordigd door de som verkregen door vermenigvuldiging

van de jaarlijkse opbrengst of, bij ontstentenis daarvan, van de

huurwaarde van het goed, met het getal dat in de onderstaande tabel

is opgegeven en afhankelijk is van de leeftijd, welke degene op wiens

hoofd het vruchtgebruik is gevestigd, op de dag van de akte heeft:

Getal  Leeftijd

18   20 jaar of minder

17  meer dan 20 jaar en niet meer dan 30 jaar;

16  meer dan 30 jaar en niet meer dan 40 jaar;

14  meer dan 40 jaar en niet meer dan 50 jaar;

13  meer dan 50 jaar en niet meer dan 55 jaar;

11  meer dan 55 jaar en niet meer dan 60 jaar;

9,5  meer dan 60 jaar en niet meer dan 65 jaar;

8  meer dan 65 jaar en niet meer dan 70 jaar;

6  meer dan 70 jaar en niet meer dan 75 jaar;

4  meer dan 75 jaar en niet meer dan 80 jaar;

2  meer dan 80 jaar;

Is het vruchtgebruik voor een beperkte tijd gevestigd, zo is de

verkoopwaarde vertegenwoordigd door de som verkregen door het

kapitaliseren ad 4 pct. van de jaarlijkse opbrengst, rekening gehouden

met de bij de overeenkomst gestelde duur van het vruchtgebruik,

maar zonder te mogen overschrijden hetzij de naar voorgaande alinea

bepaalde waarde, zo het gaat om een ten bate van een natuurlijke

persoon gevestigd vruchtgebruik, hetzij het bedrag van twintigmaal

In geen geval mag aan het vruchtgebruik een hogere waarde dan de

vier vijfden van de verkoopwaarde van de volle eigendom worden

toegewezen.

###### Artikel 48

Gaat de overeenkomst over de blote eigendom van een onroerend

goed waarvan het vruchtgebruik door de vervreemder is

voorbehouden, zo mag de belastbare grondslag niet lager zijn dan de

verkoopwaarde van de volle eigendom.

###### Artikel 49

Gaat de overeenkomst over de blote eigendom van een onroerend

goed, zonder dat het vruchtgebruik door de vervreemder is

voorbehouden, zoo mag de belastbare grondslag niet lager zijn dan de

verkoopwaarde van de volle eigendom, na aftrekking van de

overeenkomstig artikel 47 berekende waarde van het vruchtgebruik.

###### Artikel 50

Wordt of werd het vruchtgebruik op het hoofd van twee of meer

personen gevestigd, met recht van aanwas of van terugvalling, zo is

de voor de toepassing van artikelen 47 en 49 in aanmerking te nemen

leeftijd die van de jongste persoon.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

§ 2. Verkopingen aan bouwmaatschappijen tot nut van het algemeen  § 2. Ventes aux sociétés immobilières de service public

###### Artikel 51

(aangevuld bij art. 145 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

aan maatschappijen erkend hetzij door de Nationale Maatschappij

voor de Huisvesting, hetzij door de Nationale Landmaatschappij,

hetzij door de Gewestelijke Maatschappijen opgericht in uitvoering

van de wet van 28 december 1984 tot afschaffing of herstructurering

van sommige instellingen van openbaar nut.

aan de samenwerkende maatschappij «Woningsfonds van de Bond

der Kroostrijke Gezinnen in België», aan de coöperatieve

vennootschappen Vlaams Woningfonds van de Grote Gezinnen,

Woningfonds van de Kroostrijke Gezinnen van Wallonië en

Woningfonds van de gezinnen van het Brusselse Gewest.

Wat betreft de onder 1° hierboven bedoelde maatschappijen, wordt

de verlaging slechts toegestaan mits het bewijs geleverd wordt van

de erkenning der verkrijgende maatschappij.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

§ 3. Verkopingen aan de met regeringspremie begunstigde kopers  § 3. Ventes aux acheteurs bénéficiaires de la prime gouvernementale

###### Artikel 52

(gewijzigd bij art. 146 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Het recht wordt tot 1,50 t.h. verlaagd voor de verkopingen van

woningen toegestaan door de Nationale Maatschappij voor de

Huisvesting, de Nationale Landmaatschappij, de door hen of door de

Gewestelijke Maatschappijen opgericht in uitvoering van de wet van

28 december 1984 tot afschaffing of herstructurering van sommige

instellingen van openbaar nut erkende maatschappijen, de openbare

besturen of de openbare instellingen, aan personen wie de door de

Staat verleende aankooppremie ten goede komt.

Het gebeurlijk intrekken van die premie brengt voor de verkrijger der

verplichting mede het verschuldigde recht tot het bij artikel 44

vastgesteld percentage aan te zuiveren.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

woningen

###### Artikel 53

(gewijzigd bij art. 35 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst van

toepassing vanaf 01.01.1980 (art. 45))

Het bij artikel 44 vastgesteld recht wordt tot 6 t.h. verlaagd voor de

verkopingen van de eigendom:

1° Van onroerende landgoederen waarvan het kadastraal inkomen

een bij koninklijk besluit vast te stellen maximum niet te boven gaat.

Wordt als landgoed aangezien, het onroerend goed dat hetzij uit voor

landbouwbedrijf aangewende of bestemde gebouwen en gronden,

hetzij uit dergelijke gronden alleen bestaat;

2° Van woningen waarvan het gebouwd of ongebouwd kadastraal

inkomen een bij koninklijk besluit vast te stellen maximum niet

overschrijdt.

Als woning wordt aangemerkt het huis of het geheel of het gedeelte

van een verdieping van een gebouw, dat dient of zal dienen tot

huisvesting van een gezin of één persoon, met in voorkomend geval

de aanhorigheden die tegelijk met het huis, het geheel of het gedeelte

van een verdieping worden verkregen. De Koning stelt regels vast

voor het bepalen van de aanhorigheden waarop deze bepalingen van

toepassing is.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 54

(gewijzigd bij art. 36 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst van

toepassing vanaf 01.01.1980 (art. 45))

De in voorgaand artikel voorziene verlaging is niet toepasselijk op de

verkoop van een onverdeeld deel, tenzij dit deel verbonden is aan een

verdieping of aan een gedeelte van verdieping van een gebouw.

inkomen voor de geheelheid of voor het onverdeeld deel, met dit van

het verkregen onroerend goed, meer bedraagt dan het krachtens het

vorig artikel vast te stellen maximum. In afwijking van deze bepaling

wordt evenwel geen rekening gehouden met hetgeen door de

verkrijger of door zijn echtgenoot werd verkregen uit de nalatenschap

van hun bloedverwanten in de opgaande lijn, mits het desbetreffende

kadastraal inkomen 25 % van evenbedoeld maximum niet

overschrijdt.

De onder 2° van het voorgaande artikel bepaalde vermindering is

eveneens niet toepasselijk indien de verkrijger of zijn echtgenoot

reeds, voor het geheel in volle of in blote eigendom, een onroerend

goed bezitten dat geheel of gedeeltelijk tot bewoning is bestemd en

dat door hen of door een van hen anders dan uit de nalatenschap van

hun bloedverwanten in de opgaande lijn is verkregen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 55

(gewijzigd bij art. 79 van de wet van 22.12.2009 (B.S., 31.12.2009 - ed. 2).

Tekst van toepassing vanaf 10.01.2010 (art. -))

De in artikel 53 voorziene verlaging is bovendien aan volgende

voorwaarden verbonden:

1° (…)  1  (…)

2° De akte, of een door de verkrijger gewaarmerkte en ondertekende

verklaring onderaan op de akte, moet uitdrukkelijk vermelden:

a) dat de verkrijger en zijn echtgenoot geen andere onroerende

goederen bezitten of dat zij, voor het geheel of in onverdeeldheid niet

één of meer onroerende goederen bezitten waarvan het kadastraal

inkomen, voor het geheel of voor het onverdeelde deel, samen met

dat van het verkregen onroerend goed, meer dan het krachtens artikel

53 vastgestelde maximum bedraagt, afgezien van hetgeen zij uit de

nalatenschap van hun bloedverwanten in de opgaande lijn hebben

verkregen wanneer het desbetreffende kadastraal inkomen 25 pct.

van evenbedoeld maximum niet overschrijdt.

c) in geval van toepassing van artikel 53, 2°, dat de verkrijger of zijn

echtgenoot, voor het geheel in volle of in blote eigendom geen

onroerend goed bezitten dat geheel of gedeeltelijk tot bewoning is

bestemd en door hen of door één van hen anders dan uit de

nalatenschap van hun bloedverwanten in de opgaande lijn werd

verkregen.

d) in geval van toepassing van artikel 53, 2°, dat de verkrijger of zijn

echtgenoot zijn inschrijving in het bevolkingsregister of in het

vreemdelingenregister op het adres van het verkregen onroerend

goed zal bekomen.

In geval van niet-nakoming van een van bovenstaande voorwaarden

uiterlijk wanneer de akte ter formaliteit wordt aangeboden, wordt

deze akte tegen het gewoon recht geregistreerd; hetgeen boven het

verlaagd recht geheven werd is vatbaat voor teruggaaf, tot beloop

van de acht tienden, mits overlegging van een uittreksel uit de

kadastrale legger en een verklaring ondertekend door de verkrijger,

waarin de door voorgaand 2° beoogde vermeldingen voorkomen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 56

Wanneer het kadastraal inkomen van het verkregen onroerend goed

nog niet is vastgesteld, wordt het sub 1° van vorenstaand artikel

bedoeld uittreksel uit den kadastrale legger vervangen door een

attest van de controleur van het kadaster houdende dat het

kadastraal inkomen van bewust onroerend goed nog moet

vastgesteld worden.

In dit geval, wordt de akte, behoudens de in artikel 58 voorziene

teruggaaf, tegen het gewoon recht geregistreerd.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 57

Onder voorbehoud der door artikel 54 voorziene beperkingen, wordt

het bij artikel 44 vastgesteld recht verlaagd tot 6 pct. voor de

verkopingen van de eigendom van een grond welke tot bouwplaats

van een woning moet dienen, op voorwaarde:

1° Dat het verkregen goed en het gebouwd onroerend goed aan de

bij artikel 53, 2°, gestelde voorwaarden beantwoorden;

2° Dat de akte van verkrijging de bij artikel 55, 2°, geëiste

vermeldingen vervat.

In dit geval, wordt de akte tegen het gewoon recht geregistreerd,

behoudens de bij artikel 58 voorziene teruggaaf, na voltooiing van het

gebouw.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 58

(aangevuld bij art. 26 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

In de bij artikelen 56 en 57 voorziene gevallen, wordt hetgeen boven

het verlaagd recht werd geheven, teruggegeven op overlegging van

een na de vaststelling van het kadastraal inkomen afgeleverd

uittreksel uit den kadastrale legger.

Het ter uitvoering van artikel 53, 2°, toepasselijk maximum is datgene

dat van kracht was op de datum van de akte van verkrijging.

Zo, tussen de datum van de akte en de 2 de januari die volgt op het

betrekken der gebouwde woning, nieuwe kadastrale inkomens,

vastgesteld  ingevolge  een  algemene  perekwatie  of  een

buitengewone herziening, voor de heffing der grondbelasting in

toepassing worden gebracht, dan moet het voor de gebouwde

woning in acht te nemen kadastraal inkomen bepaald worden

volgens de regeling die op de datum van de akte van toepassing was.

Het aldus bepaalde kadastraal inkomen wordt de verkrijger ter kennis

gebracht; deze kan bezwaar indienen volgens de procedure

betreffende de vaststelling van de nieuwe kadastrale inkomens.

###### Artikel 59

(gewijzigd bij art. 148 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

In geval van onjuistheid in de vermeldingen waarvan sprake in artikel

55, eerste lid, 2°, a en c, verbeurt de verkrijger een aan het ontdoken

recht gelijke geldboete.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 60

(gewijzigd bij art. 3 van de wet van 19.05.1998 (B.S., 14.07.1998). Tekst van

toepassing vanaf 24.07.1998 (art. -))

Het voordeel van de in artikel 53, 1°, bedoelde vermindering blijft

alleen dan behouden zo de verkrijger, zijn echtgenoot of zijn

afstammelingen zelf de landeigendom uitbaten. Die uitbating dient

aangevangen binnen een termijn van vijf jaar ingaande op de datum

van de akte van verkrijging en tenminste drie jaar zonder

onderbreking voortgezet.

Het voordeel van de in artikel 53, 2° bedoelde vermindering blijft

alleen dan behouden zo de verkrijger of zijn echtgenoot ingeschreven

is in het bevolkingsregister of in het vreemdelingenregister op het

adres van het verkregen onroerend goed. Deze inschrijving moet

geschieden binnen een termijn van drie jaar te rekenen van de datum

van de authentieke akte van verkrijging en ten minste drie jaar zonder

onderbreking behouden blijven.

Evenwel blijft de verlaging verkregen zo niet-nakoming van die

voorwaarden het gevolg is van overmacht.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 61. 1

Indien de vermindering vervalt bij gebreke van exploitatie binnen de

termijn en gedurende de tijd bepaald in artikel 60, eerste lid, is de

verkrijger, naast het aan vullend recht, een daaraan gelijke

vermeerdering verschuldigd.

Indien de vermindering vervalt bij gebreke van inschrijving binnen de

termijn en gedurende de tijd bepaald in artikel 60, tweede lid, is de

verkrijger, naast het aanvullend recht, een daaraan gelijke

vermeerdering verschuldigd.

De Minister van Financiën kan evenwel van die vermeerdering geheel

of gedeeltelijk afzien.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 61. 2

(gewijzigd bij art. 5 van de wet van 19.05.1998 (B.S., 14.07.1998). Tekst van

toepassing vanaf 24.07.1998 (art. -))

Wanneer een ongebouwd landeigendom, verkregen met de in deze

paragraaf bedoelde verlaging, naderhand in een ruiling betrokken

wordt volgens artikel 72, treedt het in ruil verkregen goed, voor de

toepassing van de artikelen 60, eerste lid en 61 1 , eerste lid, in de

plaats van het oorspronkelijk verkregen goed.

Hetzelfde  heeft  plaats  ingeval  van  ruilverkaveling  van

landeigendommen in der minne of uit kracht van de wet. In geval van

gebruiksruil bij toepassing van titel I van de wet houdende bijzondere

maatregelen inzake ruilverkaveling van landeigendommen uit kracht

van de wet bij de uitvoering van grote infrastructuurwerken, treedt,

voor de toepassing van de artikelen 60, eerste lid en 61 1 , eerste lid,

het bij de akte van ruiling voor gebruik toebedeeld goed in de plaats

van het verkregen goed.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 62

(vervangen bij art. 1 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van

toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978 (B.S. 30.11.1978)))

Het in artikel 44 bepaalde recht wordt tot 5 pct. verminderd voor de

verkopingen die uit de hand en bij authentieke akte gedaan worden

aan personen die hun beroep maken van het kopen en verkopen van

onroerende goederen.

Deze vermindering is echter niet van toepassing op de verkopen van

landeigendommen waarvan de verkoopswaarde het bedrag niet te

boven gaat dat verkregen wordt bij vermenigvuldiging van het

kadastraal inkomen met een door de Koning vastgestelde coëfficiënt.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 63. 1

(lid 1, 1°, vervangen bij art. 62 van de wet van 12.05.2024 (B.S., 30.05.2024

– ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders

van een ondernemingsnummer, evenals voor natuurlijke personen, op een

datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028

(art. 222))

Om de in vorenstaand artikel voorziene vermindering te genieten,

moet de beroepspersoon:

1° in de vorm en aan het bij koninklijk besluit te bepalen kantoor, een

beroepsverklaring ondertekenen en verzenden;

2° op eigen kosten, zekerheid stellen voor de invordering van de

sommen welke bij toepassing van artikel 64 en volgende artikelen van

deze paragraaf vorderbaar kunnen worden;

3° de erkenning verkregen hebben van een in België gevestigd

vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem

instaat voor de nakoming van zijn fiscale verplichtingen indien hij:

b) een rechtspersoon is zonder vestiging in België en wiens

maatschappelijke zetel gevestigd is buiten de Europese Economische

Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte

van verkrijging, hetzij in een onderaan de akte gestelde verklaring of

in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie,

door de verkrijger of, in zijn naam, door de werkende notaris

ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet

een uittreksel uit de kadastrale legger betreffende de verkregen

goederen aan de akte gehecht zijn wanneer zij ter registratie wordt

aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en,

in voorkomend geval, het uittreksel uit de kadastrale legger, zoals

bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het

gewoon recht geregistreerd en geen vordering tot teruggaaf is

ontvankelijk.

Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan

de  erkenning  verkrijgen  van  een  in  België  gevestigde

vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem

instaat voor de nakoming van zijn fiscale verplichtingen.

-----

###### Art. 63. 1

(gewijzigd bij art. 62 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst van

toepassing vanaf 16.05.2011 (art. -))

Om de in vorenstaand artikel voorziene vermindering te genieten,

moet de beroepspersoon:

1° in de vorm en op het bij koninklijk besluit te bepalen kantoor, een

beroepsverklaring ondertekenen en indienen;

2° op eigen kosten, zekerheid stellen voor de invordering van de

sommen welke bij toepassing van artikel 64 en volgende artikelen van

deze paragraaf vorderbaar kunnen worden;

3° de erkenning verkregen hebben van een in België gevestigd

vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem

instaat voor de nakoming van zijn fiscale verplichtingen indien hij:

b) een rechtspersoon is zonder vestiging in België en wiens

maatschappelijke zetel gevestigd is buiten de Europese Economische

Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte

van verkrijging, hetzij in een onderaan de akte gestelde verklaring of

in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie,

door de verkrijger of, in zijn naam, door de werkende notaris

ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet

een uittreksel uit de kadastrale legger betreffende de verkregen

goederen aan de akte gehecht zijn wanneer zij ter registratie wordt

aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en,

in voorkomend geval, het uittreksel uit de kadastrale legger, zoals

bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het

gewoon recht geregistreerd en geen vordering tot teruggaaf is

ontvankelijk.

Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan

de  erkenning  verkrijgen  van  een  in  België  gevestigde

vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem

instaat voor de nakoming van zijn fiscale verplichtingen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 63. 2

(ingevoegd bij art. 3 van de wet van 03.02.1959 (B.S., 14.02.1959). Tekst van

toepassing vanaf 24.02.1959 (art. -))

Wanneer door een schatting volgens artikelen 190 en 199 bevonden

wordt dat de verkoopwaarde van landgoederen, welke met

toepassing van het bij artikel 62 voorzien verminderd recht verkregen

werden, op de datum van de verkrijging de door laatstbedoeld artikel

vastgestelde grens niet overtrof, is de verkrijger gehouden tot het

betalen van het bijkomend recht berekend op de grondslag die voor

de heffing van het verminderd recht gediend heeft, van een zelfde

som als boete en van de kosten der procedure.

###### Artikel 64

Het bij artikel 44 bepaald recht wordt vorderbaar ten laste van de

verkrijger van het onroerend goed die het voordeel van artikel 62

heeft genoten, bijaldien bedoelde verkrijger of zijn rechthebbenden dit

onroerend goed niet hebben vervreemd door wederverkoop of alle

andere overdracht onder bezwarende titel, andere dan den inbreng in

vennootschap, vastgesteld bij authentieke akte uiterlijk verleden op

31 december van het tiende jaar na de datum van de koopakte.

De wederverkoop aan een beroepspersoon met toepassing van

###### Art. 62

staat deze vorderbaarheid niet in de weg.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 65

De verkrijger mag de betaling aanbieden van het gewoon recht vóór

het verstrijken van de in eerste alinea van vorig artikel voorziene

termijn.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 66

Het recht dat voor de verkrijging van het goed betaald werd, mag niet

op de krachtens artikelen 64 en 65 verschuldigde rechten worden

aangerekend.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 67

de verkrijging betaald recht en naar het op de datum dezer verkrijging

van kracht zijnde tarief.

Bijaldien slechts een deel van tegen een enige prijs aangekochte

onroerende goederen wordt vervreemd, wordt de belastbare waarde

van het niet vervreemde gedeelte bepaald naar verhouding van de

grootte.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 68

(lid 3, vervangen bij art. 63 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.

2). Tekst van toepassing voor alle of bepaalde categorieën van houders van

een ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art.

222))

In het geval van artikel 64 worden de gewone rechten vereffend op

een verklaring die, binnen de eerste vier maanden na het verstrijken

van het tiende jaar en op straf van boete gelijk aan de rechten, tot

registratie dient aangeboden ten kantore in welks gebied de goederen

gelegen zijn.

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter

registratie een verklaring aanbieden waarin samenstelling en waarde

zijn bepaald van de goederen waarvoor hij de rechten wenst te

betalen.

De bij dit artikel voorgeschreven verklaringen worden door de

belanghebbende  of  zijn  aangenomen  vertegenwoordiger

ondertekend en vermelden de akte of de akten van verkrijging, het

nieuwe feit waaruit de verschuldigdheid van het recht volgt en al de

tot de vereffening van de belasting nodige gegevens. Een kopie wordt

bewaard door de bevoegde dienst van de Algemene administratie van

de patrimoniumdocumentatie.

-----

###### Artikel 68

In het geval van artikel 64 worden de gewone rechten vereffend op

een verklaring die, binnen de eerste vier maanden na het verstrijken

van het tiende jaar en op straf van boete gelijk aan de rechten, tot

registratie dient aangeboden ten kantore in welks gebied de goederen

gelegen zijn.

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter

registratie een verklaring aanbieden waarin samenstelling en waarde

zijn bepaald van de goederen waarvoor hij de rechten wenst te

betalen.

De bij dit artikel voorgeschreven verklaringen, welke door

belanghebbende of zijn aangenomen vertegenwoordiger worden

ondertekend, worden in dubbel gesteld, en een exemplaar blijft op het

kantoor der registratie. Deze verklaringen houden vermelding van de

akte of de akten van verkrijging, van het nieuwe feit waaruit de

verschuldigdheid van het recht volgt en al de tot de vereffening van

de belasting nodige gegevens.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 69

(gewijzigd bij artikel 63 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst

van toepassing vanaf 16.05.2011 (art. -))

Bij overlijden van den vertegenwoordiger van een beroepspersoon

bedoeld in artikel 63 1 , eerste lid, 3°, bij de intrekking van zijn erkenning

of in geval hij onbekwaam wordt verklaard om als vertegenwoordiger

op te treden, dient binnen zes maand in zijn vervanging voorzien.

Wanneer de door den verkrijger gestelde zekerheid ontoereikend

wordt, dient hij, binnen de door het bestuur vastgestelde termijn, een

aanvullende zekerheid te verstrekken.

Wordt aan vorenstaande voorschriften niet voldaan, zo wordt het

volgens artikelen 66 en 67 berekend gewoon recht op de niet

wederverkochte goederen vorderbaar.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

De Minister van Financiën of zijn afgevaardigde bepaalt aard en

bedrag der ter voldoening van artikelen 63 1 , 2°, en 69 te stellen

zekerheid of aanvullende zekerheid. Deze zekerheid dient gesteld

onder de door de Minister of zijn afgevaardigde bepaalde

voorwaarden en mag niet minder dan 5.000 EUR bedragen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 71

Indien hij die een beroepsverklaring heeft ondertekend bij het

verstrijken van een termijn van vijf jaar na die verklaring, niet bij

machte is om door een reeks wederverkoper te laten blijken dat hij

het aangegeven beroep werkelijk uitoefent, wordt hij schuldenaar van

de gewone rechten op zijn aankopen, onder aftrek van de reeds

geheven rechten, en daarenboven van een som gelijk aan de

aanvullende rechten als boete.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

§ 6. Ruiling van ongebouwde landgoederen  § 6. Echanges d’immeubles ruraux non bâtis

###### Artikel 72

(gewijzigd en aangevuld bij art. 2 van de wet van 27.04.1978 (B.S.,

30.11.1978). Tekst van toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978

(B.S., 30.11.1978)))

Zijn vrijgesteld van het evenredig recht en onderworpen aan het

algemeen  vast  recht,  de  ruilingen  van  ongebouwde

landeigendommen waarvan de verkoopwaarde voor elk der kavels

Evenwel wordt bij ongelijkheid van de kavels het bij artikel 44

bepaalde recht geheven op het waardeverschil of de opleg, indien

deze groter is dan dat verschil. Dit recht wordt verlaagd tot 6 t.h.

indien het waardeverschil of de opleg een vierde van de

verkoopwaarde van de minste kavel niet te boven gaat.

De toepassing van dit artikel is ondergeschikt aan een drievoudige

voorwaarde:

1° dat de verkoopwaarde van elke kavel door partijen wordt

aangegeven, hetzij in de akte, hetzij onderaan de akte, vóór de

registratie;

2° dat een uittreksel uit de kadastrale legger aan de akte wordt

gehecht bij de registratie;

3° dat de partijen vóór de registratie, in een verklaring gedaan in de

akte of onderaan op de akte, aanduiden of de geruilde onroerende

goederen door henzelf of door derden worden geëxploiteerd en dat,

in deze laatste onderstelling, de akte of een daaraan vóór de

registratie gehecht schrijven de instemming inhoudt van alle

exploitanten van de in de ruiling begrepen goederen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 73. 1

(vervangen bij art. 3 van de wet van 26.07.1952 (B.S., 30.08.1952). Tekst van

toepassing vanaf 09.09.1952 (art. -))

Voor elke te laag bevonden opleg of waardeverschil is, behalve het

ontdoken recht, een geldboete van hetzelfde bedrag als dit recht

vorderbaar.

Hetzelfde geldt voor elke overschatting van de kavels die een

vermindering van het recht tot gevolg heeft.

De geldboete is evenwel niet verschuldigd, indien het verschil tussen

de verkoopwaarde van de kavels en de aangegeven schatting minder

dan een achtste hiervan bedraagt.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 73. 2

(hersteld bij art. 3 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van

toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978 (B.S., 30.11.1978)))

In geval van onjuistheid van de verklaring betreffende de uitbating van

de geruilde onroerende goederen, zijn de partijen ondeelbaar

gehouden tot de betaling van het verschil tussen het gewoon recht en

het geheven recht, alsook van een boete gelijk aan dat verschil.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

§ 7. Afzonderlijke verkrijgingen van de grond en van de opstal of van de

tot de dienst van het onroerend goed aangewende voorwerpen

###### Artikel 74

(gewijzigd bij art. 42 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).

Tekst van toepassing vanaf 10.04.1994 (art. -))

Wie bij een overdragende overeenkomst onder bezwarende titel,

andere dan een inbreng in vennootschap vermeld in artikel 115 bis , de

eigendom heeft verkregen, hetzij van hout op stam onder beding van

het te vellen, hetzij van gebouwen onder beding van ze te slopen, en

nadien onder de levenden de eigendom verkrijgt van de grond

vooraleer het hout gans geveld is of de gebouwen volomen gesloopt

zijn, moet uit hoofde van de eerste verkrijging en op de grondslag

aangewezen in artikel 45 en volgende, het voor de verkoop van

onroerende goederen vastgesteld recht kwijten met aftrek van het

evenredig registratierecht eventueel op deze verkrijging werd

geheven.

Deze bepaling is evenwel niet van toepassing, zo er bewezen wordt

dat de belasting over de toegevoegde waarde werd gekweten voor de

levering van het hout op stam of van de te slopen gebouwen.

###### Artikel 75

(gewijzigd bij art. 43 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).

Tekst van toepassing vanaf 10.04.1994 (art. -))

Wordt als overdracht van een onroerend goed aangezien, die welke

voortvloeit uit een overeenkomst onder de levenden te bezwarende

### titel, andere dan een inbreng in vennootschap vermeld in artikel

115 bis , en welke over de eigendom gaat hetzij van hout op stam,

hetzij van gebouwen, zo bewuste overdracht ten bate van de eigenaar

van de grond wordt toegestaan.

Deze bepaling is niet van toepassing zo de belasting over de

toegevoegde waarde verschuldigd is voor de levering van de

goederen die in de overeenkomst begrepen zijn. De heffing van het

vast recht is echter ondergeschikt aan de vermelding, in de akte of in

een erbij gevoegd geschrift, vóór de registratie, van het kantoor, waar

de verkoper periodiek de aangiften indient die voor de heffing van de

belasting over de toegevoegde waarde zijn vereist.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

§ 8. (…)

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van

toepassing vanaf 31.07.1960 (art. -))

###### Artikel 76

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van

toepassing vanaf 31.07.1960 (art. -))

(…)

###### Art. 77. tot 82 W.Reg. federaal

###### Art. 77 à 82 C. enr. fédéral

en de gewesten).

#### Afdeling II - Openbare verkopingen van lichamelijke

roerende goederen

(opschrift vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959).

Tekst van toepassing vanaf 17.01.1959 (art. -))

###### Artikel 77

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Het recht wordt vastgesteld op 5 t.h. voor de openbare verkopingen

van lichamelijke roerende goederen.

###### Artikel 78

(opgeheven bij art. 5 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van

toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van

19.12.1969 (B.S., 20.12.1969)))

(…)

###### Artikel 79

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

De heffingsgrondslag wordt bepaald zoals gezegd in de artikelen 45

en 231.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 80

(lid 2, gewijzigd bij art. 64 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als

belastingplichtige in de zin van de wetgeving op de belasting over de

toegevoegde waarde;

2° de openbare verkopingen van goederen bedoeld in de artikelen 2

en 3 van titel I van het Wetboek der met het zegel gelijkgestelde

taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.  3° les ventes publiques des bois indigènes livrés sur pied ou abattus.

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven

mits in het proces-verbaal of in een geschrift dat bij het proces-

verbaal vóór de registratie is gevoegd, vermeld wordt naar welk

kantoor de verkoper de periodieke aangiften voor de belasting over de

toegevoegde waarde moet verzenden.

-----

###### Artikel 80

(vervangen bij art. 42 van de wet van 27.12.1977 (B.S., 30.12.1977) err. (B.S.,

10.05.1978). Tekst van toepassing vanaf 01.01.1978 (art. 43))

Vrijgesteld van het recht van 5 pct. en onderworpen aan het algemeen

vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als

belastingplichtige in de zin van de wetgeving op de belasting over de

toegevoegde waarde;

2° de openbare verkopingen van goederen bedoeld in de artikelen 2

en 3 van titel I van het Wetboek der met het zegel gelijkgestelde

taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.  3° les ventes publiques des bois indigènes livrés sur pied ou abattus.

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven

mits in het proces-verbaal of in een geschrift dat bij het proces-

verbaal vóór de registratie is gevoegd, vermeld wordt bij welk kantoor

de verkoper de periodieke aangiften voor de belasting over de

toegevoegde waarde moet indienen.

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 81

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 82

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 83. tot 86 W.Reg. federaal

###### Art. 83 à 86 C. enr. fédéral

Het registratierecht op de huurcontracten is een federale belasting

(art. 3, a contrario , wet 16.01.1989 betreffende de financiering van de

gemeenschappen en de gewesten).

#### Afdeling IV - Huurcontracten

###### Artikel 83

(lid 1, 3°, gewijzigd bij art. 5 van de wet van 22.12.2023 (B.S., 29.12.2023 –

ed. 1). Tekst van toepassing vanaf 01.01.2024 (art. 6))

Het recht wordt vastgesteld op:  Le droit est fixé à :

1° 0,20 pct. voor contracten van verhuring, onderverhuring en

overdracht van huur van onroerende goederen;

2° 1,50 pct. voor jacht- en vispacht;  2° 1,50 p.c. pour les baux de chasse et de pêche ;

3° 5 pct. voor contracten tot vestiging van een erfpacht- of

opstalrecht en tot overdracht daarvan, behalve wanneer daardoor

een vereniging zonder winstoogmerk, een internationale vereniging

zonder winstoogmerk of een gelijkaardige rechtspersoon die

Europese Economische Ruimte heeft, titularis van het erfpacht- of

opstalrecht wordt, in welk geval het recht wordt vastgesteld op 0,50

pct.

Een rechtspersoon is gelijkaardig aan een VZW wanneer de volgende

voorwaarden cumulatief zijn vervuld:

1° het doel van de rechtspersoon is belangeloos, zonder

winstoogmerk;

2° de activiteit van de rechtspersoon mag niet leiden tot de materiële

verrijking van:

a) de stichters, de leden of de bestuurders ervan;  a) ni ses fondateurs, ses membres ou ses administrateurs ;

b) de echtgenoot, de wettelijk samenwonende, een bloedverwant in

de rechte lijn, een bloedverwant in de zijlijn die tot een stichter in een

erfgerechtigde graad staat, of een andere rechtsopvolger van een

stichter ervan;

c) de echtgenoot of een wettelijk samenwonende van een persoon

bedoeld in a) en b);

3° in geval van ontbinding of vereffening van de rechtspersoon

mogen de goederen ervan niet toekomen aan personen vermeld

onder 2°, maar moeten ze worden overgedragen aan:

a) hetzij een gelijkaardige rechtspersoon die zelf is opgericht volgens

en onderworpen aan de wetgeving van een lidstaat van de Europese

Economische Ruimte en bovendien zijn statutaire zetel, zijn

hoofdbestuur  of  zijn  hoofdvestiging  binnen  de  Europese

Economische Ruimte heeft;

b) hetzij een lidstaat is van de Europese Economische Ruimte of een

territoriaal gedecentraliseerde overheid van een EER-lidstaat is of

nog, een dienstgewijze gedecentraliseerde overheid is van een

dergelijke publiekrechtelijke rechtspersoon.

Contracten tot vestiging van erfpacht- of opstalrecht en overdrachten

daarvan worden, voor het overige, met huurcontracten en -

overdrachten gelijkgesteld, voor de toepassing van dit wetboek,

behalve voor de toepassing van de artikelen 2 quater en 161, 12°.

Dit recht is evenwel niet verschuldigd in geval van toepassing van

###### Art. 140

bis .

toepassing vanaf 27.09.1947 (art. -))

De belastbare grondslag wordt als volgt vastgelegd:  La base imposable est déterminée, savoir :

Voor huur van bepaalde duur, geldt als grondslag van het voor de duur

van het contract of, ter zake overdracht, voor het nog te lopen tijdperk

samengevoegd bedrag van huursommen en aan huurder opgelegde

lasten;

Is zij levenslang of van onbepaalde duur, zo geldt als grondslag het

tienvoudig bedrag van de jaarlijkse huurprijs en lasten, zonder dat de

belastbare som minder moge zijn dan het samengevoegd bedrag van

huurprijzen en aan huurder opgelegde lasten voor de bij de huurakte

voorziene minimumduur.

Bij overdracht van huur, wordt het bedrag of de waarde van de

gebeurlijk ten bate van de overdrager bedongen prestatiën gevoegd

bij de heffingsgrondslag zoals hij hiervoor is bepaald.

#### Afdeling V - (…)

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 85

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 86

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 87. tot 102 W.Reg. federaal

voor zeevervoer bestemd is;

- de inpandgeving van een handelszaak;

- de vestiging van een landbouwvoorrecht;

- de overdracht van een hypotheek op een onroerend goed;

zijn federale belastingen (art. 3, eerste lid, 7° a) a contrario wet

16.01.1989 betreffende de financiering van de gemeenschappen en

de gewesten).

Alleen het registratierecht op de vestiging van een hypotheek op een in

België gelegen onroerend goed is een gewestelijke belasting (art. 3,

eerste lid, 7°, a) wet 16.01.1989 betreffende de financiering van de

gemeenschappen en de gewesten). Zie ook ontwerp van bijzondere

wet tot herfinanciering van de gemeenschappen en uitbreiding van de

fiscale bevoegdheden van de gewesten, Parl.St. Kamer 2000-01, nr.

50 1183/001, 74.

Gewestelijke bepalingen (art. 3, eerste lid, 7°, a) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

#### Afdeling VI - Hypotheekvestigingen

(gewijzigd bij art. 55 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70))

###### Artikel 87

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Worden aan een recht van 1 t.h. onderworpen, de vestigingen van een

hypotheek op een in België gelegen onroerend goed.

###### Artikel 88

(vervangen bij art. 56 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70)) (1)

De vestigingen van een hypotheek op een schip dat niet naar zijn aard

voor het zeevervoer bestemd is, worden aan een recht van 0,50 pct.

onderworpen.

inwerkingtreding van deze wet, wordt in mindering gebracht op het krachtens

###### Art. 87. W.Reg. verschuldigde recht, wanneer later een hypotheek wordt

gevestigd tot zekerheid van dezelfde schuld (art. 69).

###### Artikel 89

(gewijzigd bij art. 57 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70))

De bij artikelen 87 en 88 bepaalde rechten zijn van toepassing zelfs

wanneer de hypotheek gevestigd is tot zekerheid van een

toekomstige schuld, van een voorwaardelijke of eventuele schuld of

van een verbintenis om iets te doen.

###### Artikel 90

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

De bij artikelen 87 en 88 bepaalde rechten zijn niet verschuldigd zo de

gewaarborgde verbintenis voortkomt uit een contract waarop een

evenredig recht van minstens 1 pct. werd geheven.

Gewestelijke bepalingen (art. 3, eerste lid, 7°, a) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 91

(vervangen bij art. 58 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70))

De vestiging van een hypotheek op een in België gelegen onroerend

goed tot zekerheid van een schuld die gewaarborgd is door een

hypotheek op een schip dat niet naar zijn aard voor het zeevervoer

bestemd is, (…) wordt aan het recht van 1 pct. onderworpen onder

aftrek, in voorkomend geval, van het krachtens artikel 88 geheven

recht van 0,50 pct.

###### Art. 92. 1

Het in artikel 88 en het in artikel 3, eerste lid, 7°, a) , van de bijzondere

wet van 16 januari 1989 betreffende de financiering van de

Gemeenschappen en de Gewesten bedoeld recht dekt elke latere

vestiging van hypotheek op een schip tot zekerheid van dezelfde

schuldvordering en van hetzelfde gewaarborgd bedrag.

###### Art. 92. 2

(gewijzigd bij art. 60 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70))

De overdracht van een hypotheek op een in België gelegen onroerend

goed met inbegrip van de voorrechten bedoeld bij artikel 27 van de

wet van 16 december 1851 of van een hypotheek op een schip dat

niet naar zijn aard voor het zeevervoer bestemd is, ingevolge de

overdracht onder bezwarende titel van de schuldvordering, de

contractuele indeplaatsstelling of elke andere verrichting onder

bezwarende titel, wordt onderworpen aan een recht van 1 pct. of van

0,50 pct., al naar gelang de overdracht al dan niet een hypotheek op

een onroerend goed betreft.

###### Artikel 93

(gewijzigd bij art. 61 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van

toepassing vanaf 01.01.2018 (art. 70))

Het recht van 1 pct. of van 0,50 pct. wordt vereffend op het bedrag

van de sommen die door de hypotheek gewaarborgd zijn, met

uitsluiting van de interesten of rentetermijnen van drie jaren, die

gewaarborgd zijn door artikel 87 van de wet van 16 december 1851.

###### Artikel 94

(gewijzigd bij art. 12 van de wet van 03.07.2018 (B.S., 19.07.2018). Tekst van

toepassing vanaf het aanslagjaar 2019 (art. 13))

Schepen worden niet onderworpen aan het in artikel 88 bepaalde

recht op voorwaarde dat:

het Belgisch register der zeeschepen werd ingediend, aan de akte

wordt gehecht;

2° de akte, of een door de hypotheeksteller gewaarmerkte en

ondertekende verklaring onderaan op de akte, uitdrukkelijk vermeldt:

a) dat het schip naar zijn aard voor het zeevervoer bestemd is;  a) que le navire est destiné par nature au transport maritime ;

b) dat de hypotheeksteller de verbintenis aangaat om de

voorwaarden inzake het behoud of de uitbreiding van de tonnage en

inzake de bewijslevering van naleving van de tonnage-eis en van het

voldoen van elk schip van de vloot aan de betreffende internationale

en communautaire normen, zoals die voorwaarden nader zijn

omschreven in punt 3.1, leden 8 en 9 van de Mededeling C(2004) van

de Europese Commissie, na te leven gedurende vijf jaar te rekenen

van de datum van de registratie van de akte.

Als de in het eerste lid, 2°, a) bedoelde verklaring onjuist blijkt of als

de in het eerste lid, 2°, b) bedoelde verbintenis niet wordt nageleefd,

is de hypotheeksteller gehouden tot betaling van het evenredig recht,

vermeerderd met de interesten.

De hypotheeksteller kan aanbieden het evenredig recht vermeerderd

met de interesten te betalen alvorens de in het eerste lid, 2°, b)

voorziene termijn is verstreken.

#### Afdeling VII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 95

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 96

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959).Tekst van

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 97

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 98

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

#### Afdeling VIII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 99

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 100

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Artikel 101

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

###### Artikel 102

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

(…)

###### Art. 103. tot 108 W.Reg. federaal

Het specifiek vast recht op de handlichting van een hypothecaire

inschrijving is een federale belasting (art. 3, a contrario , wet

16.01.1989 betreffende de financiering van de gemeenschappen en

de gewesten).

#### Afdeling IX - Opheffingen

###### Artikel 103

(gewijzigd bij art. 92 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

§ 1. Elke gehele of gedeeltelijke handlichting van een in België

genomen hypothecaire inschrijving, gedaan bij een akte bedoeld in

artikel 19, 1°, is onderworpen aan een specifiek vast recht van 75

euro.

§ 2. In afwijking van paragraaf 1 geven slechts aanleiding tot éénmaal

de heffing van het recht bedoeld in paragraaf 1, de handlichtingen

vastgesteld in één akte:

1° van inschrijvingen genomen lastens éénzelfde schuldenaar-

hypotheeksteller;

2° van inschrijvingen genomen lastens een schuldenaar-

hypotheeksteller en een persoon-hypotheeksteller als waarborg voor

de eerstgenoemde;

3° van inschrijvingen van wettelijke hypotheken lastens éénzelfde

schuldenaar;

5° die geschieden in het kader van een openbare verkoping na beslag

of van een verkoop uit de hand bedoeld in artikel 1580 bis van het

Gerechtelijk Wetboek.

###### Artikel 104

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst

van toepassing vanaf 17.01.1959 (art. -))

(...)  (…)

###### Artikel 105

(opgeheven bij art. 153, 1° van de wet van 22.12.1989 (B.S., 29.12.1989).

Tekst van toepassing vanaf 01.01.1990 (art. 244))

(...)  (…)

###### Artikel 106

(opgeheven bij art. 153, 2°, van de wet van 22.12.1989 (B.S., 29.12.1989).

Tekst van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 107

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst

van toepassing vanaf 17.01.1959 (art. -))

(...)  (…)

###### Artikel 108

(opgeheven bij art. 153, 3°, van de wet van 22.12.1989 (B.S., 29.12.1989).

Tekst van toepassing vanaf 01.01.1990 (art. 244))

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

#### Afdeling X - Verdelingen

###### Artikel 109

(aangevuld bij art. 33 van de wet van 14.05.1981 (B.S., 27.05.1981). Tekst van

toepassing vanaf 06.06.1981 (art. -))

Het recht wordt op 1 t.h. vastgesteld voor:  Le droit est fixé à 1 p. c. pour :

1° de gedeeltelijke of gehele verdelingen van onroerende goederen;  1  les partages, partiels ou totaux, de biens immeubles ;

2° de afstanden onder bezwarende titel, onder medeëigenaars, van

onverdeelde delen in onroerende goederen.

3° de omzetting bedoeld in de artikelen 745 quater en 745 quinquies

van het Burgerlijk Wetboek, zelfs indien er geen onverdeeldheid is.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 110

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Voor de goederen waarvan de akte de onverdeeldheid doet ophouden

onder al de medeëigenaars, wordt het recht vereffend op de waarde

van die goederen.

Voor de goederen waarvan de akte de onverdeeldheid niet doet

ophouden onder al de medeëigenaars, wordt het recht vereffend op

de waarde der afgestane delen.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

De heffingsgrondslag is bepaald door de overeengekomen waarde

der goederen, zoals ze blijkt uit de bepalingen van de akte, zonder dat

hij lager dan de verkoopwaarde mag zijn.

Wanneer de bepalingen van de akte het niet mogelijk maken de

overeengekomen  waarde  vast  te  stellen,  wordt  daarin

overeenkomstig artikel 168 voorzien.

In voorkomend geval wordt de verkoopwaarde van het vruchtgebruik

of van de blote eigendom overeenkomstig artikelen 47 tot 50

vastgesteld.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 112

(opgeheven bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst

van toepassing vanaf 17.01.1959 (art. -))

(...)  (…)

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 113

(vervangen bij art. 17 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

In geval van toebedeling bij verdeling of van afstand van onverdeelde

delen aan een derde die bij overeenkomst een onverdeeld deel heeft

verkregen van goederen toebehorende aan één of meer personen,

wordt het recht, met afwijking van artikel 109, geheven tegen het

voor de overdrachten onder bezwarende titel vastgesteld tarief, op de

delen waarvan de derde ten gevolge van de overeenkomst eigenaar

wordt, en zulks volgens de in artikelen 45 tot 50 voorziene regels.

erfgenamen of legatarissen van de overleden derde verkrijger. Zij is

niet van toepassing wanneer de derde, aan wie de toebedeling of de

afstand gedaan wordt, met anderen het geheel van één of meer

goederen heeft verkregen.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 114

De bepalingen van deze afdeling zijn niet van toepassing op de

uitvoering van een beding van terugvalling of van aanwas.

###### Art. 115. tot 130 W.Reg. federaal

Het registratierecht op de inbreng in een vennootschap is een

federale belasting (art. 3, eerste lid, 6°, wet 16.01.1989 betreffende

de financiering van de gemeenschappen en de gewesten).

#### Afdeling XI - Vennootschappen

###### Artikel 115

(lid 1, gewijzigd en lid 3, opgeheven bij art. 22 van de wet van 30.10.2025 (B.S.,

24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))

Aan een recht van 0 pct. wordt onderworpen de inbreng van roerende

goederen in vennootschappen waarvan hetzij de zetel der werkelijke

leiding in België, hetzij de statutaire zetel in België en de zetel der

werkelijke leiding buiten het grondgebied van de lidstaten van de

Europese Unie, is gevestigd, onverschillig of de inbreng bij de

oprichting van de vennootschap of naderhand plaats heeft.

Het recht wordt vereffend op het totaal bedrag van de inbrengen.  Le droit est liquidé sur le montant total des apports.

###### Art. 115. bis

(lid 1, gewijzigd bij art. 23 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst

van toepassing vanaf 25.11.2025 (art. 28))

gedeeltelijk of geheel tot bewoning aangewend worden of bestemd

zijn en door een natuurlijke persoon ingebracht worden, in

vennootschappen waarvan de zetel der werkelijke leiding in België

gevestigd is, of de statutaire zetel in België en de zetel van werkelijke

leiding buiten het grondgebied van de lidstaten van de Europese Unie

gevestigd is, worden aan het recht van 0 pct. onderworpen.

In geval van onjuiste verklaring betreffende de aanwending of de

bestemming van het onroerend goed, zijn de aanvullende rechten

opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.

###### Artikel 116

(gewijzigd bij art. 24 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van

toepassing vanaf 25.11.2025 (art. 28))

Aan een recht van 0 pct. wordt onderworpen de vermeerdering van

het kapitaal, zonder nieuwe inbreng, van een vennootschap waarvan

hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel

in België en de zetel der werkelijke leiding buiten het grondgebied van

de lidstaten van de Europese Unie, is gevestigd.

Het recht wordt vereffend op het bedrag van de vermeerdering.  Le droit est liquidé sur le montant de l’augmentation.

Het recht is niet verschuldigd in de mate waarin het kapitaal

vermeerderd wordt door inlijving van reserves of provisies, die

gevestigd werden, bij gelegenheid van inbrengen gedaan in de

vennootschap, ter vertegenwoordiging van het geheel of een

gedeelte van het bedrag van die inbrengen dat onderworpen werd

aan het bij de artikelen 115 en 115 bis bedoeld recht.

###### Artikel 117

(gewijzigd bij art. 25 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van

toepassing vanaf 25.11.2025 (art. 28))

§ 1 . Het bij de artikelen 115 en 115 bis bepaalde recht is niet

verschuldigd in geval van inbreng van de universaliteit der goederen

van een vennootschap, bij wijze van fusie, splitsing of anderszins, in

een of meer nieuwe of bestaande vennootschappen.

Deze bepaling is evenwel slechts toepasselijk op voorwaarde:  Cette disposition n’est toutefois applicable qu’à condition :

2° a) dat de rechtshandeling door artikel 12:7 van het Wetboek van

vennootschappen en verenigingen wordt gelijkgesteld met fusie door

overneming, of

b) dat, eventueel na aftrek van de op het tijdstip van de inbreng door

de inbrengende vennootschap verschuldigde sommen, de inbreng

uitsluitend vergoed wordt hetzij door toekenning van aandelen, hetzij

door toekenning van aandelen samen met een storting in contanten

die het tiende van de nominale waarde of, bij gebrek aan een nominale

waarde, van de fractiewaarde van de toegekende aandelen niet

overschrijdt. Indien het Belgisch of buitenlands recht dat de

verkrijgende vennootschap beheerst niet in een begrip gelijkaardig

aan dat van het kapitaal van een naamloze vennootschap voorziet,

wordt met de fractiewaarde gelijkgesteld, de inbrengwaarde, zoals

die blijkt uit de jaarrekening, van alle door de aandeelhouders of

vennoten toegezegde inbrengen in geld of in natura, met uitzondering

van de inbrengen in nijverheid, in voorkomend geval verhoogd met de

reserves die op grond van een statutaire bepaling slechts aan de

aandeelhouders of vennoten kunnen worden uitgekeerd mits een

statutenwijziging, dit alles gedeeld door het aantal aandelen.

§ 2. Het in de artikelen 115 en 115 bis bedoelde recht is eveneens niet

verschuldigd voor de inbrengen gedaan door een vennootschap

waarvan de zetel der werkelijke leiding of de statutaire zetel

gevestigd is op het grondgebied van een lidstaat van de Europese

Unie, van goederen die één of meer van haar bedrijfstakken uitmaken

onder de volgende voorwaarden:

1° dat de inbreng het geheel omvat van de goederen die door de

inbrengende vennootschap worden aangewend tot één of meer

afdelingen van haar onderneming welke, op technisch en

organisatorisch gebied, elk een autonome activiteit uitoefenen en op

eigen kracht kunnen werken; en

2° dat, eventueel na aftrek van de bij de inbreng door de inbrengende

vennootschap verschuldigde sommen die betrekking hebben op de

ingebrachte bedrijfstakken, de inbreng uitsluitend vergoed wordt

hetzij door toekenning van aandelen, hetzij door toekenning van

aandelen samen met een storting in contanten die het tiende van de

nominale waarde of, bij gebrek aan een nominale waarde, van de

fractiewaarde van de toegekende aandelen niet overschrijdt. Indien

het Belgisch of buitenlands recht dat de verkrijgende vennootschap

beheerst niet in een begrip gelijkaardig aan dat van het kapitaal van

een naamloze vennootschap voorziet, wordt met de fractiewaarde

gelijkgesteld, de inbrengwaarde, zoals die blijkt uit de jaarrekening,

van alle door de aandeelhouders of vennoten toegezegde inbrengen

kunnen worden uitgekeerd mits een statutenwijziging, dit alles

gedeeld door het aantal aandelen.

De bepaling onder 2° is niet van toepassing op de door artikel 12:8,

2°, van het Wetboek van vennootschappen en verenigingen met

splitsing gelijkgestelde rechtshandelingen.

Wordt niet beschouwd als een afdeling van de onderneming het

beheer van de participaties en de waarden in portefeuille. De

participaties en waarden in portefeuille worden slechts beschouwd

als behorende tot een bedrijfstak wanneer zij normaal in de exploitatie

van deze tak van de bedrijvigheid zijn geïntegreerd.

Onverminderd het recht tot controle, moet de vervulling van de

voorwaarden bevestigd worden, hetzij in de akte van inbreng, hetzij in

een onderaan deze akte gestelde verklaring, die vóór de registratie

door de partijen of, in hun naam, door de werkende notaris zal

ondertekend worden. Bij gebrek aan deze bevestiging zal de akte

geregistreerd worden mits betaling van het recht bepaald zonder

rekening te houden met de vrijstelling van het evenredig recht of de

uitzondering, naar gelang van het geval, behoudens latere teruggave.

§ 3. Het in de artikelen 115 en 115 bis bedoelde recht is eveneens niet

verschuldigd  in  geval  van  inbreng  van  aandelen  of

aandelencertificaten, die tot gevolg heeft dat de vennootschap bij wie

de inbreng gebeurt, ten minste 75 pct. van het kapitaal of van het

eigen vermogen verwerft van de vennootschap waarvan de aandelen

of aandelencertificaten zijn ingebracht.

Wanneer dat percentage ten gevolge van verscheidene inbrengen is

bereikt, is deze paragraaf alleen toepasselijk op de inbrengen die het

bereiken van het percentage mogelijk hebben gemaakt, alsmede op

de daaropvolgende inbrengen.

Bovendien vindt deze paragraaf alleen toepassing wanneer voldaan

is aan de volgende voorwaarden:

1° de vennootschap die verkrijgt en de vennootschap waarvan de

aandelen of deelbewijzen zijn ingebracht, moeten beide hun zetel der

werkelijke leiding of hun statutaire zetel hebben op het grondgebied

van een lidstaat van de Europese Unie;

2° de inbreng moet uitsluitend door uitgifte van aandelen van de

verkrijgende vennootschap vergoed worden, samen met een storting

in contanten die het tiende van de nominale waarde of, bij gebrek aan

een nominale waarde, van de fractiewaarde van de toegekende

aandelen niet overschrijdt. Indien het Belgisch of buitenlands recht

inbrengwaarde, zoals die blijkt uit de jaarrekening, van alle door de

aandeelhouders of vennoten toegezegde inbrengen in geld of in

natura, met uitzondering van de inbrengen in nijverheid, in

voorkomend geval verhoogd met de reserves die op grond van een

statutaire bepaling slechts aan de aandeelhouders of vennoten

kunnen worden uitgekeerd mits een statutenwijziging, dit alles

gedeeld door het aantal aandelen;

3° de akte van inbreng moet vermelden dat bij de inbreng ten minste

75 pct. van het kapitaal of van het eigen vermogen van de

vennootschap waarvan de aandelen zijn ingebracht, door de

verwervende vennootschap wordt verkregen;

4° een attest van een bedrijfsrevisor dat het vermelde feit

overeenkomstig het 3° van dit lid bevestigt, moet aan de akte worden

aangehecht.

In geval van niet-nakoming van een van de toepassingsvoorwaarden

van deze paragraaf uiterlijk wanneer de akte ter formaliteit wordt

aangeboden, wordt deze akte tegen het gewoon tarief geregistreerd.

###### Artikel 118

(vervangen bij art. 7 van de wet van 03.07.1972 (B.S., 01.08.1972). Tekst van

toepassing vanaf 01.01.1972 (art. 11))

Voor de toepassing van dit Wetboek worden beschouwd als

oprichtingen van nieuwe vennootschap:

1° de overbrenging naar België van de zetel der werkelijke leiding van

een vennootschap waarvan de statutaire zetel in het buitenland is;

2° de overbrenging naar België van de statutaire zetel van een

vennootschap waarvan de zetel der werkelijke leiding in het

buitenland is;

3° de overbrenging van het buitenland naar België, van de statutaire

zetel en van de zetel der werkelijke leiding van een vennootschap.

In deze gevallen omvat de inbreng de goederen van elke aard die aan

de vennootschap toebehoren op het tijdstip van de overbrenging.

###### Artikel 119

In de gevallen bedoeld in de artikelen 115, 115 bis en 118 wordt de

belastbare grondslag vastgesteld met inachtneming van de waarde

der als vergelding van de inbrengen toegekende maatschappelijke

rechten, zonder dat hij nochtans minder mag bedragen dan de

verkoopwaarde van de goederen onder aftrek van de lasten die de

vennootschap op zich neemt boven de toekenning van de

maatschappelijke rechten.

De inbrengen die bestaan uit andere zaken dan geldspecie of

goederen in natura worden geraamd bij vergelijking met de inbrengen

van geldspecie of goederen in natura, gelet op de onderscheidene

aandelen van de inbrengers in de winst.

De verkoopwaarde van het vruchtgebruik of van de blote eigendom

van in België gelegen onroerende goederen wordt bepaald

overeenkomstig de artikelen 47 tot 50.

###### Artikel 120

(gewijzigd bij art. 47 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).

Tekst van toepassing vanaf 10.04.1994 (art. -))

Wanneer een inbreng in vennootschap gedeeltelijk vergolden wordt

anders dan bij toekenning van maatschappelijke rechten, wordt de

overeenkomst, naarmate van deze vergelding onderworpen aan de

rechten zoals ze in dit hoofdstuk vastgesteld zijn voor de

overeenkomsten onder bezwarende titel die goederen van dezelfde

aard tot voorwerp hebben.

Zo een inbreng meteen onroerende goederen vermeld in artikel

115 bis en goederen van een andere aard begrijpt, worden,

niettegenstaande elke strijdig beding, de maatschappelijke rechten en

de andere lasten, die de vergeldingen van bedoelde inbreng uitmaken

geacht evenredig verdeeld te zijn tussen de waarde die aan de

onroerende goederen is toegekend en die welke aan de andere

goederen is toegekend bij overeenkomst. De te vervallen huurprijzen

van de huurcontracten waarvan de rechten worden ingebracht,

worden evenwel geacht enkel op laatstbedoelde rechten betrekking

te hebben.

Deze bepalingen zijn evenwel niet toepasselijk bij inbreng van de

universaliteit van de goederen of van een bedrijfstak overeenkomstig

###### artikel 117.

(lid 1, 3°, gewijzigd bij art. 26 van de wet van 30.10.2025 (B.S., 24.11.2025).

Tekst van toepassing vanaf 25.11.2025 (art. 28))

Met afwijking van de artikelen 115, 115 bis , 118 en 120 worden van

het evenredig recht vrijgesteld:

1° de omvorming van een vennootschap met rechtspersoonlijkheid

in een vennootschap van een verschillende soort en de omzetting van

een vereniging zonder winstoogmerk in een sociale onderneming.

Deze bepaling is toepasselijk zelfs wanneer de omvorming plaats

heeft bij wege van liquidatie gevolgd door de oprichting van een

nieuwe vennootschap, voor zover deze wederoprichting in de akte

van in-liquidatie-stellen in het vooruitzicht wordt gesteld en binnen

vijftien dagen na de akte plaats heeft;

2° de wijziging van het voorwerp van een vennootschap;  2° le changement de l’objet d’une société ;

3° de overbrenging van de zetel der werkelijke leiding of van de

statutaire zetel van een vennootschap, wanneer deze overbrenging

geschiedt uit het grondgebied van een lidstaat van de Europese Unie

of wanneer het een overbrenging naar België betreft van de zetel der

werkelijke leiding van een vennootschap waarvan de statutaire zetel

zich reeds op het grondgebied van de Europese Unie bevindt. Deze

bepaling is slechts toepasselijk in de mate waarin het vaststaat dat de

vennootschap behoort tot de soort van die welke onderworpen zijn

aan een belasting op het bijeenbrengen van kapitaal in het land dat in

aanmerking komt voor het voordeel van de vrijstelling.

In alle gevallen wordt het recht geheven op de vermeerdering van het

kapitaal van de vennootschap, zonder nieuwe inbreng, of op de

inbrengen van nieuwe goederen, die gedaan worden ter gelegenheid

van de omvorming, de wijziging van het voorwerp of de overbrenging

van de zetel.

###### Artikel 122

(lid 1, 1° en 3°, vervangen, lid 1, 4° en lid 2, gewijzigd bij art. 28 van de wet

van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026

(art. 33, lid 1))

Onder voorbehoud van de bepalingen van artikel 120, wordt van het

evenredig recht vrijgesteld de inbreng gedaan:

2° aan maatschappijen die uitsluitend ten doel hebben leningen te

doen met het oog op het bouwen, het aankopen of het inrichten van

volkswoningen, kleine landeigendommen of daarmede gelijkgestelde

woningen, alsmede de uitrusting ervan met geschikt mobilair;

3° aan de besloten vennootschap Vlaams Woning-fonds, de

coöperatieve vennootschap Fonds du logement des familles

nombreuses de Wallonie en de coöperatieve vennootschap

Woningfonds van het Brussels Hoofdstedelijk Gewest;

4° aan de beleggingsvennootschappen bedoeld in artikel 6 van de

wet van 3 augustus 2012 betreffende de instellingen voor collectieve

belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG

en de instellingen voor belegging in schuldvorderingen.

Het evenredig recht, zonder aftrek van het reeds geïnde algemeen

vast recht, wordt echter opeisbaar wanneer de in het eerste lid, 4°,

bedoelde beleggingsvennootschap de erkenning overeenkomstig de

wet van 3 augustus 2012 betreffende de instellingen voor collectieve

belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG

en de instellingen voor belegging in schuldvorderingen niet verkrijgt

of verliest, al naar het geval, zulks vanaf de datum van de beslissing

tot weigering of tot intrekking van de erkenning.

###### Art. 122. 2

(opgeheven bij art. 14, 1°, van de wet van 14.04.1965 (B.S., 24.04.1965).

Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

###### Artikel 123

(gewijzigd bij art. 93 van de wet van 17.03.2019 (B.S., 10.05.2019). Tekst van

toepassing vanaf 01.05.2019 (art. 119, § 1)) (1)

Onder voorbehoud van de bepalingen van de artikelen 44 en 120

wordt van het evenredig recht vrijgesteld, de vermeerdering van het

kapitaal of het eigen vermogen, met nieuwe inbreng, door een

vennootschap bedoeld in artikel 201, eerste lid, 1°, van het Wetboek

van de inkomstenbelastingen 1992, mits aandelen of andere met

Deze vrijstelling is alleen toepasselijk indien in de akte of in een vóór

de registratie bij de akte te voegen geschrift wordt bevestigd dat de

toepassingsvoorwaarden ervan zijn vervuld.

In geval van onjuistheid van die vermelding verbeurt de vennootschap

een boete gelijk aan het ontdoken recht.

----------

Nota (1) – Overgangsbepalingen:

Zolang het Wetboek van vennootschappen en verenigingen, overeenkomstig

#### hoofdstuk IV, afdeling II, van de wet van 23 maart 2019, niet van toepassing

is op een vennootschap, vereniging of stichting, moet elke verwijzing naar een

bepaling van het Wetboek van vennootschappen en verenigingen die

voorkomt in een bepaling van het Wetboek van de inkomstenbelastingen

1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het

Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het

Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering

ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze

belastingen, worden gelezen, voor wat deze vennootschap, vereniging of

stichting betreft, als een verwijzing naar de bepaling van het Wetboek van

vennootschappen of andere bijzondere wetgeving die in zulke fiscale

wetgeving voorkwam voor de inwerkingtreding van deze wet (art. 119, § 2);

Zolang, overeenkomstig hoofdstuk IV, afdeling II van de wet van 23 maart

2019, een vennootschap, vereniging of stichting, die door het Belgisch recht

wordt beheerst, een rechtsvorm heeft die het Wetboek van vennootschappen

en verenigingen niet erkent, worden de bepalingen van het Wetboek van de

inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en

Griffierechten, het Wetboek van Successierechten, het Wetboek diverse

rechten en taksen en het Wetboek van de Belasting over de Toegevoegde

Waarde, de ter uitvoering ervan genomen besluiten en de bijzondere

wetgeving van toepassing op deze belastingen, die voor de inwerkingtreding

van deze wet deze rechtsvorm vermeldden, geacht deze rechtsvorm te blijven

vermelden voor wat deze vennootschap, vereniging of stichting betreft, zoals

voor de inwerkingtreding van deze wet. (art. 119, § 3).

###### Artikel 124

(hersteld bij art. 31 van de wet van 22.05.2001 (B.S., 09.06.2001). Tekst van

toepassing vanaf 01.01.2002 (art. 4, KB 19.12.2001 (B.S., 29.12.2001- ed. 2)))

Onder voorbehoud van de voorschriften van de artikelen 44 en 120,

worden van het evenredig recht vrijgesteld:

1° de statutaire kapitaalsverhoging, uitgevoerd bij toepassing van

een participatieplan bedoeld in artikel 2, 7°, van de wet van 22 mei

2001 betreffende de werknemersparticipatie in het kapitaal en in de

2° de inbreng in een coöperatieve participatievennootschap

uitgevoerd volgens artikel 12, § 2, van dezelfde wet.

Deze vrijstelling is slechts toepasbaar voor zover er vermeld is in de

akte of in een vóór de registratie bij de akte gevoegd geschrift dat de

toepassingsvoorwaarden zijn vervuld.

Ingeval deze vermelding ontbreekt of onjuist is, loopt de

vennootschap een boete op gelijk aan het ontdoken recht.

###### Artikel 125

(opgeheven bij art. 14, 3°, van de wet van 14.04.1965 (B.S.,24.04.1965).

Tekst van toepassing vanaf 04.05.1965 (art. -))

(…)

###### Artikel 126

(opgeheven bij art. 14, 4°, van de wet van 14.04.1965 (B.S.,24.04.1965).

Tekst van toepassing vanaf 04.05.1965 (art. -))

( …)  (…)

###### Artikel 127

(opgeheven bij art. 14, 5°, van de wet van 14.04.1965 (B.S., 24.04.1965).

Tekst van toepassing vanaf 04.05.1965 (art. -))

( ...)  (…)

###### Artikel 128

(gewijzigd bij art. 15 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van

toepassing vanaf 04.05.1965 (art. -))

Met afwijking van artikel 2, mogen de onderhandse akten welke de in

artikelen 115 tot 122 bedoelde overeenkomsten tot voorwerp

hebben, op de originelen of op afschriften of uittreksels worden

###### Art. 21. 1  wordt toepasselijk gemaakt op de onderhandse of

buitenslands verleden akten die de zelfde overeenkomsten tot

voorwerp hebben, al hadden deze geen betrekking op in België

gelegen onroerende goederen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 129

(gewijzigd bij art. 31 van de wet van 23.03.2019 (B.S., 04.04.2019). Tekst van

toepassing vanaf 01.05.2019 (art. 38))

Het verkrijgen, anderszins dan bij inbreng in vennootschap, door één

of meer vennoten, van in België gelegen onroerende goederen,

voortkomende van een vennootschap onder gemeenschappelijke

naam of bij wijze van eenvoudige geldschieting, van een besloten

vennootschap of van een landbouwvennootschap, geeft, welke ook

de wijze zij waarop het geschiedt, aanleiding tot het heffen van het

voor verkopingen gesteld recht.

In geval van afgifte van de maatschappelijke goederen door de

vereffenaar van de in vereffening gestelde vennootschap aan al de

vennoten, is voorgaand lid van toepassing op de latere toebedeling

van de goederen aan één of meer vennoten.

Lid l is niet toepasselijk zo het gaat om:  L’alinéa 1 er n’est pas applicable en ce qui concerne :

1° onroerende goederen welke in de vennootschappen werden

ingebracht, wanneer ze verkregen worden door de persoon, die de

inbreng gedaan heeft;

2° onroerende goederen welke door de vennootschap met betaling

van het voor de verkopingen bepaald registratierecht verkregen

werden, wanneer het vaststaat dat de vennoot die eigenaar van die

onroerende goederen wordt deel uitmaakte van de vennootschap

toen laatstgenoemde de goederen verkreeg.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

van toepassing vanaf 17.03.1962 (art. 3))

Het verkrijgen anderszins dan bij inbreng in vennootschap door één of

meer vennoten van in België gelegen onroerende goederen,

voortkomende  van  een  vennootschap  op  aandelen,  een

samenwerkende vennootschap (…), geeft, welke ook de wijze zij

waarop het geschiedt, aanleiding tot het heffen van het voor

verkopingen gesteld recht.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

#### Afdeling XII - Schenkingen

##### Onderafdeling I - Algemene bepalingen

###### Artikel 131

(gewijzigd bij art. 3, § 1 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1).

Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 5°

van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Voor de schenkingen onder de levenden van roerende of onroerende

goederen wordt over het bruto-aandeel van elk der begiftigden een

evenredig recht geheven volgens het tarief in onderstaande tabellen

aangeduid.

Hierin wordt vermeld:  Ce tarif mentionne :

onder a: het percentage dat toepasselijk is op het overeenstemmend

gedeelte;

onder b: het totale bedrag van de belasting over de voorgaande

gedeelten.

TABEL I

Gedeelte van de schenking

Tranche de la donation

0,01  - 12.500  3

12.500  - 25.000  4  375

25.000  - 50.000  5  875

50.000  - 100.000  7  2.125

100.000  - 150.000  10  5.625

150.000  - 200.000  14  10.625

200.000  - 250.000  18  17.625

250.000  - 500.000  24  26.625

boven de / au-

30  86.625

delà de

500.000

TABEL II

Gedeelte van de

Tussen

Tussen

Tussen alle

schenking

broeders en

ooms of

andere

Tranche de la

zusters

tantes en

personen

donation

Entre frères

neven of

Entre toutes

et sœurs

nichten

autres

Entre oncles

personnes

ou tantes et

neveux ou

nièces

Van

tot

a  b  a  b  a  b

de

inbegrepen

à … inclus

EUR  t.h.

EUR  t.h.

EUR  t.h.

EUR

/

/

/

p.c.

p.c.

p.c.

0,01  - 12.500  20  -  25  -  30  -

12.500 - 25.000  25  2.500  30  3.125  35  3.750

25.000 - 75.000  35  5.625  40  6.875  50  8.125

75.000 - 175.000 50  23.125 55  26.875 65  33.125

boven de

65  73.125 70  81.875 80  98.125

de 175.000

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

relative au financement des Communautés et des Régions)

###### Art. 132. 1

(…)

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 132. 2

(vervangen bij art. 157 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Voor de toepassing van deze afdeling wordt er geen rekening

gehouden met de verwantschapsband voortspruitende uit de

gewone adoptie.

Evenwel wordt, mits bewijs te verstrekken door de belanghebbende,

met deze adoptieve afstamming rekening gehouden:

1° wanneer het adoptief kind een kind is van de echtgenoot van de

adoptant;

2° wanneer, op het ogenblik van de adoptie, het adoptief kind onder

de voogdij was van de openbare onderstand of van een openbaar

centrum voor maatschappelijk welzijn, of wees van een voor België

gestorven vader of moeder;

3° wanneer het adoptief kind, vóór de leeftijd van eenentwintig jaar

bereikt te hebben en gedurende zes onafgebroken jaren, uitsluitend

van de adoptant of eventueel van hem en zijn echtgenoot te samen,

de hulp en de verzorging heeft gekregen welke kinderen normaal van

hun ouders krijgen.

4° wanneer de adoptie gedaan werd door een persoon van wie al de

afstammelingen voor België gestorven zijn.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 133

(gewijzigd bij art. 11 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

goederen, zonder aftrek van lasten.

Gaat de schenking evenwel over ter beurs genoteerde publieke

effecten, zo wordt de belastbare grondslag vastgesteld naar de

waarde van de jongste prijscourant gepubliceerd bij order van de

regering vóór de datum waarop het recht aan de Staat verworven is.

Gaat de schenking over het vruchtgebruik of de blote eigendom van

een onroerend goed, dan wordt de belastbare grondslag bepaald

zoals in artikelen 47 tot 50 is aangeduid.

Gaat de schenking over een lijfrente of een levenslang pensioen dan

wordt het recht vereffend op het jaarlijks bedrag van de uitkering

vermenigvuldigd met het getal dat, gelet op de leeftijd van de

beneficiant, in artikel 47 is aangeduid.

Gaat de schenking over een altijddurende rente, dan wordt het recht

vereffend op het twintigvoudig jaarlijks bedrag der rente.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 134

Voor de toepassing van artikelen 131 tot 133, wordt de last,

bestaande uit een som, een rente of een pensioen onder kastelozen

### titel bedongen ten bate van een derde die aanneemt, in hoofde van

deze derde als schenking belast en van het aandeel van de

hoofdbegiftigde afgetrokken.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 135

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

hadden bereikt, wordt verminderd met 2 t.h. voor elk van deze

kinderen, zonder dat de vermindering 62 EUR per kind mag

overschrijden.

Deze vermindering wordt ten gunste van de begiftigde echtgenoot

gebracht op 4 t.h. per kind dat de leeftijd van eenentwintig jaar niet

had bereikt kind, zonder dat de vermindering 124 EUR per kind mag

overschrijden.

Voor de toepassing van dit artikel wordt het ontvangen kind voor

zover het levensvatbaar geboren wordt, gelijkgesteld met het

geboren kind.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 136

(gewijzigd bij art. 159 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Het voordeel van de in vorig artikel voorziene verminderingen wordt

afhankelijk gesteld van de vermelding in de akte van schenking van

naam, voornamen, woonplaats, plaats en datum van geboorte van de

kinderen van de begiftigde beoogd bij artikel 135.

Deze vermelding mag gedaan worden onderaan op de akte in een

verklaring vóór de registratie ondertekend en echt bevestigd door de

begiftigde of, in zijn naam, door de werkende notaris.

Ingeval een kind, ontvangen vóór de eischbaarheid van de belasting,

geboren wordt na de registratie, wordt hetgeen te veel werd geheven

terugbetaald op aanvraag van den betrokkene, te doen binnen twee

jaar vanaf de geboorte van het kind.

De begiftigde die in verband met het aantal van zijn wettige (1)

afstammelingen een onjuiste verklaring heeft afgelegd, verbeurt een

boete gelijk aan het ontdoken recht.

----------

Nota:  Note :

(1) Bij vergetelheid werd het woord “wettige” niet geschrapt.  (1) Il a été omis de supprimer le mot « légitimes ».

###### Artikel 137

Ter bepaling van het op een schenking toepasselijk tarief, wordt de

desbetreffende belastbare grondslag gevoegd bij de som die heeft

gediend tot grondslag van heffing op de schenkingen welke reeds

tussen dezelfde partijen zijn voorgekomen en vastgesteld werden

door akten die dagtekenen van minder dan drie jaar vóór de datum

der nieuwe schenking en vóór laatstbedoelde datum geregistreerd

werden of verplicht registreerbaar geworden zijn.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 138. 1

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Ongeacht of zij verplicht registreerbaar zijn dan wel vrijwillig tot de

formaliteit worden aangeboden, moeten de akten van schenking

vermelding houden of er reeds tussen dezelfde partijen één of meer

schenkingen zijn voorgekomen welke vastgesteld werden door akten

die dagtekenen van minder dan drie jaar vóór de datum der nieuwe

schenking en vóór dezelfde datum geregistreerd werden of verplicht

registreerbaar geworden zijn.

Zo ja, moeten zij den datum der akten vermelden, zomede den

grondslag waarop de belasting werd of dient geheven.

De in dit artikel voorziene opgaven en vermeldingen mogen gedaan

worden onderaan de akte in een verklaring vóór de registratie

ondertekend en echt bevestigd door de begiftigde of, in zijn naam,

door de werkende notaris.

Indien bewuste opgaven en vermeldingen ontbreken of indien zij

onjuist of onvolledig zijn, verbeuren de partijen ondeelbaar een

geldboete ten bedrage van het ontdoken recht, zonder dat ze lager

dan 25 EUR mag zijn.

###### Art. 138. 2

(ingevoegd bij art. 7 van de wet van 14.08.1947 (B.S., 17.09.1947). Tekst van

toepassing vanaf 27.09.1947 (art.. -))

Voor de toepassing van artikelen 137 en 138 1 op de aan een

schorsende voorwaarde onderworpen schenkingen, wordt de datum

van de vervulling der voorwaarden in de plaats gesteld van de datum

van de akte.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 139

Bij onjuist opgeven van den graad van verwantschap tussen schenker

en begiftigde, is door deze laatsten, benevens het ontdoken recht,

ondeelbaar een boete verschuldigd gelijk aan het bedrag van dat

recht.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 140

(gewijzigd bij art. 43 van de wet van 02.05.2002 (B.S., 18.10.2002 - ed. 2) err.

(B.S., 19.10.2002 - ed. 2) heruitgave (B.S., 11.12.2002). Tekst van toepassing

vanaf 01.07.2003 (art. 66))

De bij artikel 131 vastgestelde rechten worden verlaagd tot:  Les droits fixés à l’article 131 sont réduits :

1° 6,60 t.h. voor de schenkingen aan provinciën, gemeenten,

provinciale en gemeentelijke openbare instellingen, instellingen van

openbaar nut; de Nationale Maatschappij voor de Huisvesting en de

Nationale Landmaatschappij alsmede de door hen erkende

maatschappijen,  aan  de  samenwerkende  vennootschap

«Woningfonds van den bond der Groote Gezinnen», aan de C.V.

Vlaams Woningfonds van de Grote Gezinnen, aan de C.V.

Woningfonds van de Kroostrijke Gezinnen van Wallonië, aan de C.V.

of het inrichten van volkswoningen, kleine landeigendommen of

daarmede gelijkgestelde woningen, alsmede de uitrusting ervan met

geschikt mobilair, aan de door de wet van 26 Augustus 1913

opgerichte Nationale Maatschappij der Waterleidingen, aan de

verenigingen gesticht volgens hetgeen voorzien is bij de wetten van

18 Augustus 1907 en 1 Maart 1922 en de Nationale Maatschappij der

Belgische spoorwegen;

2° 8,80 t.h. voor de schenkingen, met inbegrip van de inbrengsten om

niet,  gedaan  aan  vereenigingen  zonder  winstoogmerken,

aangenomen mutualiteitsvereenigingen, beroepsvereenigingen en

internationale vereenigingen met wetenschappelijk doel.

3° 1,10 t.h. voor de schenkingen, gedaan aan instellingen van

openbaar nut of aan rechtspersonen die in het 2° bedoeld zijn, zo de

schenker of de inbrenger zelf een instelling van openbaar nut of een

dezer rechtspersonen is.

3° bis het algemeen vast recht voor de inbrengen om niet aan private

stichtingen en stichtingen van openbaar nut of aan rechtspersonen

als bedoeld onder 2°, indien de inbrenger zelf een stichting van

openbare nut of een dezer rechtspersonen is.

4° 1,10 t.h. voor de schenkingen met inbegrip van de inbrengsten om

niet gedaan door de gemeenten aan de pensioenfondsen die zij onder

de vorm van een vereniging zonder winstoogmerk hebben opgericht

in uitvoering van een door de voogdijoverheid goedgekeurd

saneringsplan.

Die verlagingen zijn enkel op de Belgische rechtspersonen

toepasselijk.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

##### Onderafdeling II - Bijzondere bepalingen voor schenkingen van

ondernemingen

###### Art. 140. bis

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

overdracht ten kosteloze titel vaststellen van de volle eigendom van

een universaliteit van goederen of van een bedrijfstak, waarmee een

nijverheids-, handels-, ambachts- of landbouwactiviteit, een vrij

beroep of een ambt of post wordt uitgeoefend.

Het bij artikel 131 vastgestelde recht blijft niettemin toepasselijk op

de overdrachten van onroerende goederen die gedeeltelijk of geheel

tot bewoning worden aangewend of zijn bestemd;

2° de bij authentieke akte vastgestelde overeenkomsten die de

overdracht ten kosteloze titel vaststellen van de volle eigendom van

aandelen of deelbewijzen van een vennootschap waarvan de zetel

van haar werkelijke leiding is gevestigd in een lidstaat van de

Europese Unie en die de uitoefening van een nijverheids-, handels-,

ambachts- of landbouwactiviteit, een vrij beroep, of een ambt of post

tot doel heeft.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 140. ter

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

Het bij artikel 140 bis vastgestelde verlaagde recht is onderworpen

aan de volgende voorwaarden:

1° de schenker en de begiftigde moeten natuurlijke personen zijn;  1° le donateur et le donataire doivent être des personnes physiques ;

2° in geval van toepassing van artikel 140 bis , 1°:  2° en cas d’application de l’article 140 bis , 1° :

- moet in de akte of in een door de schenker en de begiftigde

gewaarmerkte en ondertekende verklaring onderaan op de akte

uitdrukkelijk worden vermeld:

a) dat de schenking betrekking heeft op de volle eigendom van een

universaliteit van goederen of van een bedrijfstak, waarmee een

nijverheids-, handels-, ambachts- of landbouwactiviteit, een vrij

beroep of een ambt of post wordt uitgeoefend;

b) in geval de schenking onroerende goederen bevat, of deze al dan

niet gedeeltelijk of geheel tot bewoning worden aangewend of zijn

bestemd;

worden vermeld:

a) dat de begiftigde zich ertoe verbindt de activiteit zonder

onderbreking voort te zetten gedurende vijf jaar te rekenen van de

datum van de authentieke akte van schenking;

b) dat de begiftigde zich ertoe verbindt aan de ontvanger der

registratie van het kantoor waar de akte werd geregistreerd jaarlijks

het bewijs te leveren van het behoud van de activiteit;

c) dat de begiftigde zich ertoe verbindt de onroerende goederen die

met toepassing van het verlaagde recht werden overgedragen, niet

gedeeltelijk of geheel tot bewoning aan te wenden gedurende een

ononderbroken periode van vijf jaar te rekenen van de datum van de

authentieke akte van schenking;

3° in geval van toepassing van artikel 140 bis , 2°:  3° en cas d’application de l’article 140 bis , 2° :

- moet de begiftigde een door een notaris, een bedrijfsrevisor of een

accountant ondertekend attest afleveren dat bevestigt dat de

schenking betrekking heeft op een geheel van aandelen of

deelbewijzen, dat minstens 10 pct. van de stemrechten in de

algemene vergadering vertegenwoordigt;

- in geval het geheel van de geschonken aandelen of deelbewijzen

minder dan 50 pct. van de stemrechten in de algemene vergadering

vertegenwoordigt,  moet  de  begiftigde  tevens  een

aandeelhouderschapsovereenkomst voorleggen, die betrekking

heeft op ten minste 50 pct. van de stemrechten in de algemene

vergadering en waarvan de modaliteiten door de' Koning worden

vastgesteld.

De hogervermelde documenten worden aan de authentieke akte

gehecht;

- moet in de akte of in een door de begiftigde gewaarmerkte en

ondertekende verklaring onderaan op de akte bovendien uitdrukkelijk

worden vermeld:

a) dat de begiftigde zich ertoe verbindt de volle eigendom van de

aandelen of deelbewijzen die het voorwerp van de schenking

uitmaken gedurende een ononderbroken periode van vijf jaar te

rekenen van de datum van de authentieke akte van schenking te

behouden;

b) dat de begiftigde zich ertoe verbindt aan de ontvanger der

registratie van het kantoor waar de akte werd geregistreerd jaarlijks

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 140. quater

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

Indien een van de onder de artikelen 140 bis en 140 ter gestelde

voorwaarden uiterlijk bij de aanbieding van de akte ter registratie niet

is vervuld, wordt de akte geregistreerd tegen betaling van het bij de

artikelen 131 tot 140 vastgestelde recht. Geen enkele vordering tot

teruggaaf is ontvankelijk.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 140. quinquies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

Behalve in geval van overmacht, wordt het overeenkomstig de

artikelen 131 tot 140 verschuldigde recht, vermeerderd met de

wettelijke interest tegen de rentevoet bepaald in burgerlijke zaken te

rekenen van de datum van registratie van de schenking, opeisbaar ten

laste van de begiftigde, indien deze laatste:

a) de overeenkomstig artikel 140 ter , 2° of 3° aangegane

verbintenissen niet nakomt;

b) in geval van een door artikel 140 bis , 1°, bedoelde schenking, de

goederen, die dienen voor de uitoefening van een nijverheids-,

handels-, ambachts- of landbouwactiviteit, een vrij beroep, of een

ambt of post, geheel of gedeeltelijk heeft overgedragen binnen de in

###### Art. 140. ter  bepaalde termijn van vijf jaar; deze bepaling is echter

niet van toepassing indien de overdracht gerechtvaardigd is door de

uitoefening van de activiteit, van het vrij beroep of van het ambt of de

post;

van werkelijke leiding van de vennootschap heeft overgebracht naar

een staat die geen lid is van de Europese Unie.

Dit artikel is niet van toepassing op de overdrachten van goederen

bepaald onder hogervermeld punt b), indien ze plaats hebben door

erfopvolging of schenking en de rechthebbenden of de begiftigden de

door de overledene of de schenker aangegane verbintenissen

overnemen.

Dit artikel is evenmin van toepassing op de overdrachten van

aandelen of deelbewijzen als bepaald onder hogervermeld punt c),

indien ze plaats hebben door erfopvolging, door schenking of door

overdracht ten bezwarende titel aan een ander lid van de

aandeelhouderschapsovereenkomst, en dat de rechthebbenden, de

begiftigden of de verwerver de door de overledene, de schenker of de

overdrager aangegane verbintenissen overnemen.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 140. sexies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

De begiftigde die de toepassing van het verlaagd recht heeft genoten

kan aanbieden om het overeenkomstig de artikelen 131 tot 140

verschuldigde recht, vermeerderd met de wettelijke interest tegen de

rentevoet bepaald in burgerlijke zaken, opeisbaar te rekenen van de

datum van registratie van de schenking, te betalen alvorens de

termijn van vijf jaar is verstreken gedurende dewelke de activiteit

moet worden voortgezet of de volle eigendom van de aandelen of

deelbewijzen behouden moet blijven.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Art. 140. septies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

verlaagd recht werd toegepast, het voorwerp uitmaakt van een

overdracht ten kosteloze titel ten voordele van de oorspronkelijke

schenker alvorens de termijn van vijf jaar is verstreken gedurende

dewelke de activiteit moet worden voortgezet of de volle eigendom

van de aandelen of deelbewijzen moet behouden blijven.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 140. octies

(lid 3, vervangen bij art. 65 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Indien artikel 140 quinquies van toepassing is worden het recht

verschuldigd bij toepassing van de artikelen 131 tot 140 en de

interesten vereffend op een verklaring die ter registratie wordt

aangeboden op het kantoor waar het verlaagd recht werd

vastgesteld, binnen de eerste vier maanden na het verstrijken van het

jaar tijdens hetwelk de oorzaak van de opeisbaarheid van het recht

zich heeft voorgedaan en dit op straffe van een boete gelijk aan dit

recht.

Indien artikel 140 sexies van toepassing is, biedt de opvolger die het

verlaagd recht heeft genoten op het voormelde kantoor een

verklaring ter registratie aan waarin de samenstelling en de waarde

van de goederen waarvoor hij het overeenkomstig de artikelen 131

tot 140 verschuldigde recht wenst te betalen wordt aangegeven.

Deze verklaring wordt door de opvolger die het verlaagd recht heeft

genoten ondertekend en vermeldt de akte, de oorzaak van de

opeisbaarheid van het verschuldigde recht en al de voor de

vereffening van het recht vereiste gegevens. Een kopie wordt

bewaard door de bevoegde dienst van de Algemene administratie van

de patrimoniumdocumentatie.

-----

###### Art. 140. octies

Indien artikel 140 quinquies van toepassing is worden het recht

verschuldigd bij toepassing van de artikelen 131 tot 140 en de

interesten vereffend op een verklaring die ter registratie wordt

aangeboden op het kantoor waar het verlaagd recht werd

vastgesteld, binnen de eerste vier maanden na het verstrijken van het

jaar tijdens hetwelk de oorzaak van de opeisbaarheid van het recht

zich heeft voorgedaan en dit op straffe van een boete gelijk aan dit

recht.

Indien artikel 140 sexies van toepassing is, biedt de opvolger die het

verlaagd recht heeft genoten op het voormelde kantoor een

verklaring ter registratie aan waarin de samenstelling en de waarde

van de goederen waarvoor hij het overeenkomstig de artikelen 131

tot 140 verschuldigde recht wenst te betalen wordt aangegeven.

Deze verklaring wordt in dubbel gesteld en door de opvolger die het

verlaagd recht heeft genoten ondertekend; één exemplaar ervan blijft

berusten op het voormelde kantoor. Ze vermeldt de akte, de oorzaak

van de opeisbaarheid van het verschuldigde recht en al de voor de

vereffening van het recht vereiste gegevens.

#### Afdeling XIII - Huwelijkscontracten en testamenten

###### Artikel 141

(opgeheven bij art. 162 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Art. 142. tot 157 W.Reg. federaal

De volgende belastingen zijn federaal:

- het veroordelingsrecht en

- het titelrecht voor zover het betrekking heeft op de inbreng door een

natuurlijke persoon van een woning in een buitenlandse

vennootschap (art. 3, eerste lid, 6° wet 16.01.1989 betreffende de

financiering van de gemeenschappen en de gewesten).

#### Afdeling XIV- Vonnissen en arresten

(gewijzigd bij art. 4 van de wet van 24.12.1993 (B.S., 31.12.1993 - ed. 2). Tekst

van toepassing vanaf 01.01.1994 (art. 26))

Het recht wordt vastgesteld op 3 pct. voor de in alle zaken gewezen

arresten en vonnissen der hoven en rechtbanken, houdende

definitieve, voorlopige, voornaamste, subsidiaire of voorwaardelijke

veroordeling of vereffening gaande over sommen en roerende

waarden, met inbegrip van de beslissingen van de rechterlijke

overheid houdende rangregeling van dezelfde sommen en waarden.

Het recht wordt vereffend, in geval van veroordeling of vereffening

van sommen en roerende waarden, op het samengevoegd bedrag, in

hoofdsom, van de uitgesproken veroordelingen of van de gedane

vereffeningen ten laste van een zelfde persoon, afgezien van de

interesten waarvan het bedrag niet door de rechter is becijferd en

kosten, en, in geval van rangregeling, op het totaal bedrag der aan de

schuldeisers uitgedeelde sommen.

###### Artikel 143

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

De bepaling van artikel 142 is niet toepasselijk:  La disposition de l’article 142 n’est pas applicable :

1° op de bevelen in kortgeding en op de arresten gewezen op beroep

daarvan;

2° op vonnissen en arresten voor zover zij strafboeten, burgerlijke

boeten of tuchtboeten uitspreken;

3° op vonnissen en arresten voor zover zij een veroordeling inhouden

tot het betalen van een uitkering tot onderhoud.

Zij is niet toepasselijk wanneer het samengevoegd bedrag van de

uitgesproken veroordelingen en van de gedane vereffeningen ten

laste van een zelfde persoon, of van de aan de schuldeisers van een

zelfde persoon uitgedeelde sommen, 12.500 EUR niet overtreft.

###### Artikel 144

vanaf 01.01.2002 (art. 45, § 1))

Werd het bij artikel 142 vastgestelde recht op een later veranderd

vonnis of arrest geheven, dan wordt voor de nieuwe beslissing het

recht van 3 t.h. alleen geheven op de aanvullende veroordeling,

vereffening of rangregeling van sommen of waarden uitgesproken of

vastgesteld ten laste van een zelfde persoon en voor zover deze

12.500 EUR te boven gaat.

Wanneer een vonnis of arrest een hoofdelijke veroordeling uitspreekt

en de op dat vonnis of arrest verschuldigde rechten volledig of

gedeeltelijk betaald werden door één van de veroordeelden, maakt de

beslissing, waardoor diegene die betaald heeft, buiten zaak wordt

gesteld, de rechten die deze betaald heeft opeisbaar in hoofde van de

andere hoofdelijke veroordeelden, dit alles onverminderd de

toepassing van de voorschriften genomen in het eerste lid.

###### Artikel 145

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Werd het bij artikel 142 vastgestelde recht op een vonnis of arrest

geheven, dan wordt op elke andere veroordeling ten laste van

dezelfde persoon of van een derde, welke steunt hetzij op dezelfde

oorzaak hetzij op een verplichting tot waarborg en meer in het

algemeen op elke door de in eerste orde veroordeelde persoon

uitgeoefende verhaalsvordering, het recht van 3 t.h. alleen geheven

op de aanvullende veroordeling tot sommen of waarden, en voor

zover deze 12.500 EUR te boven gaat.

###### Artikel 146

(gewijzigd bij art. 167 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

De vonnissen en arresten die tot bewijs strekken van een

overeenkomst waarbij eigendom of vruchtgebruik van in België

gelegen onroerende goederen overgedragen of aangewezen wordt

en welke aan de desbetreffende belasting niet onderworpen werd

vastgesteld ware geweest.

Dit geldt eveneens, zelfs indien de rechterlijke beslissing die tot bewijs

van de overeenkomst strekt, de ontbinding of herroeping ervan voor

om 't even welke reden uitspreekt, tenzij uit de beslissing blijkt dat ten

hoogste één jaar na de overeenkomst een eis tot ontbinding of

herroeping, zelfs bij een onbevoegd rechter, werd ingesteld.

###### Artikel 147

(vervangen bij art. 10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

De vonnissen en arresten houdende vernietiging, ontbinding of

herroeping van een overeenkomst waarbij eigendom of vruchtgebruik

van in België gelegen onroerende goederen overgedragen of

aangewezen wordt, geven geen aanleiding tot heffing van het

evenredig recht uit hoofde van dat te niet doen, tenzij die

uitgesproken zij ten voordele van een ander persoon dan een van de

partijen bij de overeenkomst, haar erfgenamen of legatarissen. In

laatstbedoeld geval worden de rechten geheven die verschuldigd

waren geweest indien de vernietiging, de ontbinding of de herroeping

het voorwerp van een minnelijke akte had uitgemaakt.

###### Artikel 148

(vervangen bij art.10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

Exequaturs van scheidsrechterlijke uitspraken en van buitenlands

gewezen rechterlijke beslissingen worden, voor de toepassing van dit

Wetboek, als een geheel met de desbetreffende akte aangezien, en

zijn aan dezelfde rechten als de in België gewezen vonnissen en

arresten onderworpen.

Deze rechten zijn eveneens van toepassing in geval van aanbieding

ter registratie van een buitenlands gewezen rechterlijke beslissing

indien zij van rechtswege in België uitvoerbaar is.

###### Artikel 149

Behoudens in de gevallen beoogd door de artikelen 146 tot 148

maken de vonnissen en arresten geen evenredig recht eisbaar uit

hoofde van de overeenkomsten waarvan zij het bestaan vaststellen.

###### Artikel 150

(hersteld bij art. 12 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst van

toepassing vanaf 01.11.1986 (art. 15))

Om de invordering van de rechten en, in voorkomend geval, van de

boeten eisbaar uit hoofde van deze afdeling te waarborgen, wordt,

ten bate van de Staat, een voorrecht ingesteld op de sommen en

waarden die het voorwerp uitmaken van de veroordeling, vereffening

of rangregeling.

De rechten en boeten bedoeld in het eerste lid gaan boven alle

schuldvorderingen van de begunstigden van de veroordelingen,

vereffeningen of rangregelingen.

###### Artikel 151

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960).

Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Artikel 152

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960).

Tekst van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling XV - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van

04.11.1968 (B.S., 13.11.1968))

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van

04.11.1968 (B.S., 13.11.1968))

( …)  (…)

#### Afdeling XVI - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van

04.11.1968 (B.S., 13.11.1968))

###### Artikel 154

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,

13.11.1968)))

(…)

#### Afdeling XVII - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,

13.11.1968)))

###### Artikel 155

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,

13.11.1968)))

(…)

#### Afdeling XVIII - (…)

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling XIX - Protesten

###### Artikel 157

(opgeheven bij art. 73 van de wet van 14.01.2013 (B.S., 01.03.2013). Tekst

van toepassing vanaf 01.01.2013 (art. 85))

(…)

###### Art. 158. W.Reg. federaal

###### Art. 158 C. enr. fédéral

Het specifiek vast recht voor bijlagen is een federale belasting (art. 3,

a contrario , wet 16.01.1989 betreffende de financiering van de

gemeenschappen en de gewesten).

##### Afdeling XIX bis - Aangehechte akten en geschriften

(ingevoegd bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).

Tekst van toepassing vanaf 01.04.2014 (art. 87, 3°))

###### Artikel 158

(hersteld bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2). Tekst

van toepassing vanaf 01.04.2014 (art. 87, 3°))

De aangehechte akten of geschriften bedoeld in artikel 26, tweede lid,

worden geregistreerd tegen betaling van één specifiek vast recht van

100 euro voor al die documenten samen, behalve indien sommige

ervan een of meer andere in dit hoofdstuk bepaalde rechten

verschuldigd maken, in welk geval, naast de rechten verschuldigd

voor de registratie van laatstbedoelde documenten, het specifiek vast

recht van 100 euro eenmaal verschuldigd is voor de registratie van de

overige documenten.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en

onderhevig aan het algemeen vast recht

###### Artikel 159

(lid 1, 8°, b), gewijzigd bij art. 66 van de wet van 12.05.2024 (B.S., 30.05.2024 –

ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Worden van het evenredig recht vrijgesteld en aan het algemeen vast

recht onderworpen:

1° de aanwijzing van lastgever, op voorwaarde:  1  les déclarations de command, à condition :

a) dat het vermogen om een lastgever aan te wijzen in de akte van

toewijzing of koop voorbehouden is;

b) dat de aanwijzing bij authentieke akte geschied is;  b) que la déclaration soit faite par acte authentique ;

c) dat zij bij exploot van gerechtsdeurwaarder aan de ontvanger der

registratie betekend wordt of dat de akte ter formaliteit aangeboden

wordt uiterlijk op de eerste werkdag na de dag van de toewijzing of

van het contract.

Bij niet-voldoening aan deze voorwaarden wordt de aanwijzing van

lastgever voor de toepassing van dit Wetboek als wederverkoop

beschouwd.

Met afwijking van het vorenstaande:

a) moet de aanwijzing van lastgever, bij toewijzingen die wettelijk

gedaan zijn onder de schorsende voorwaarde van ontstentenis van

opbod, om van het evenredig recht vrijgesteld te zijn, gedaan worden

vóór de notaris die de toewijzing gedaan heeft of hem betekend

worden uiterlijk op de eerste werkdag na die waarop de wettelijke

termijn voor opbod verstrijkt;

b) moet de aanwijzing van lastgever, in geval van toewijzing ten

gevolge van hoger bod op vrijwillige vervreemding van onroerende

goederen, om van het evenredig recht vrijgesteld te zijn, gedaan

worden vóór de notaris die de toewijzing heeft gedaan of hem

In die gevallen wordt de aanwijzing ingeschreven of vermeld

onderaan op het proces-verbaal van toewijzing, zonder dat zij aan de

ontvanger der registratie behoeft te worden betekend;

2° de toewijzingen naar aanleiding van rouwkoop, van roerende of

onroerende goederen, wanneer zij geen aanleiding geven tot de

heffing van een hoger evenredig recht dan datgene geheven op de

vorige toewijzing. In het tegenovergesteld geval wordt laatstbedoeld

recht afgerekend van het bedrag van de belasting waartoe de

daaropvolgende toewijzing aanleiding geeft.

Hetzelfde regime is van toepassing op de toewijzingen naar

aanleiding van prijsverhoging in de gevallen waarin het voorbehoud

van prijsverhoging geen schorsende voorwaarde uitmaakt.

3° De overeenkomsten die strekken tot de overdracht van het

vruchtgebruik op de blote eigenaar, wanneer het evenredig

registratierecht of het successierecht door de blote eigenaar of door

een vorigen blote eigenaar, zijn rechtsvoorganger, op de waarde van

de volle eigendom werd voldaan;

4° (…)  4  (…)

5° (…)  5  (…)

6° (…)  6  (…)

7° de overdragende of aanwijzende overeenkomsten, andere dan de

inbrengen onderworpen aan het in artikel 115 bis bepaalde recht die

buitenslands gelegen onroerende goederen tot voorwerp hebben,

zomede de huurcontracten van dergelijke goederen;

8° de overdragende of aanwijzende vervreemdingen onder

bezwarende titel, andere dan die welke aan het in artikel 115 bis

bepaalde recht onderworpen zijn van op te richten, in oprichting zijnde

of nieuwe opgerichte gebouwen, op voorwaarde dat de belasting over

de toegevoegde waarde opeisbaar is voor de levering van de

vervreemde  gebouwen;  de  vestigingen,  overdrachten  of

wederoverdrachten van de zakelijke rechten bedoeld in artikel 9,

tweede lid, 2°, van het Wetboek van de belasting over de

toegevoegde waarde met betrekking tot op te richten, in oprichting,

zijnde of nieuw opgerichte gebouwen, op voorwaarde dat de

belasting over de toegevoegde waarde opeisbaar is op de vestiging of

de overdracht van deze rechten.

De vrijstelling geldt niet voor de grond begrepen in de overeenkomst.  L’exemption ne s’applique pas pour le terrain compris dans

de vervreemding van de grond berekend over de verkoopwaarde van

de grond, geraamd op het tijdstip van de vervreemding, doch met

inachtneming van de staat van de grond vóór de aanvang van het

werk. Wanneer de vestiging of de overdracht van de in het eerste lid

bedoelde zakelijke rechten tevens betrekking heeft op de grond

waarop de gebouwen staan en voor een enige prijs gebeurt, wordt het

evenredig recht wegens de vestiging of de overdracht van die rechten

op de grond berekend over de waarde van die rechten, geraamd op

het tijdstip van de vestiging of de overdracht, doch met inachtneming

van de staat van de grond vóór de aanvang van het werk. In die

gevallen worden de gegevens nodig voor de berekening van de

rechten opgeheven in een verklaring als omschreven in artikel 168.

Indien de overeenkomst betrekking heeft op het vruchtgebruik of de

blote eigendom van de grond, wordt de belastbare grondslag bepaald

op de wijze vermeld in de artikelen 47 tot 50.

De bepalingen van dit 8° zijn alleen toepasselijk, indien in de akte of in

een vóór de registratie bij de akte te voegen geschrift worden

vermeld:

a) het jaar waarin, in voorkomend geval, de onroerende voorheffing

van het gebouw waarop de overeenkomst betrekking heeft voor het

eerst ten kohiere is gebracht;

b) het kantoor waarnaar de belastingplichtige de aangifte moet

verzenden voor de heffing van de belasting over de toegevoegde

waarde;

c) wanneer de overeenkomst het werk is van een andere dan in artikel

12, § 2, van het Wetboek van de belasting over de toegevoegde waard

bedoelde belastingplichtige, de datum waarop hij kennis heeft

gegeven van zijn bedoeling de verrichting te doen met betaling van de

belasting over de toegevoegde waarde.

In geval van onjuistheid van die vermeldingen, verbeurt de cedent een

boete gelijk aan het ontdoken recht;

9° (…)  9  (…)

10° de contracten van onroerende financieringshuur bedoeld in

artikel 44, § 3, 2°, b, van het Wetboek van de belasting over de

toegevoegde waarde;

11° de inbreng van goederen in Europese economische

samenwerkingsverbanden;

uittreding  van  deze  leden  of  de  ontbinding  van  het

samenwerkingsverband.

Indien onroerende goederen verkregen worden in andere

omstandigheden dan deze voorzien in het vorige lid, is voor deze

verkrijging, hoe zij ook gebeurt, het voor verkopingen bepaalde recht

verschuldigd.

13° (…)

14° de inbrengen van onroerende goederen, andere dan die welke

gedeeltelijk of geheel tot bewoning aangewend worden of bestemd

zijn en door een natuurlijke persoon ingebracht worden, in

vennootschappen met zetel van werkelijke leiding en statutaire zetel

buiten België, of met statutaire zetel in België doch met zetel van

werkelijke leiding op het grondgebied van één van de lidstaten van de

Europese Unie. Deze vrijstelling geldt voor zover de inbreng met

maatschappelijke rechten wordt vergolden. Indien de inbreng zowel

in België gelegen onroerende goederen als andere goederen omvat

wordt, niettegenstaande elk strijdig beding, de vergelding die anders

dan door toekenning van maatschappelijke rechten geschiedt, geacht

evenredig verdeeld te zijn tussen de waarde die aan de onroerende

goederen is toegekend en die welke aan de andere goederen is

toegekend. In de mate dat de inbreng betrekking heeft op in België

gelegen onroerende goederen wordt hij onderworpen aan het recht

voorgeschreven voor verkopingen.

In geval van onjuiste verklaring betreffende de aanwending of de

bestemming van het onroerend goed, worden de bijvoeglijke rechten

opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.

-----

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en

onderhevig aan het algemeen vast recht

###### Artikel 159

(14°, gewijzigd bij art. 23 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Worden van het evenredig recht vrijgesteld en aan het algemeen vast

recht onderworpen:

1° de aanwijzing van lastgever, op voorwaarde:  1  les déclarations de command, à condition :

b) dat de aanwijzing bij authentieke akte geschied is;  b) que la déclaration soit faite par acte authentique ;

c) dat zij bij exploot van gerechtsdeurwaarder aan de ontvanger der

registratie betekend wordt of dat de akte ter formaliteit aangeboden

wordt uiterlijk op de eerste werkdag na de dag van de toewijzing of

van het contract.

Bij niet-voldoening aan deze voorwaarden wordt de aanwijzing van

lastgever voor de toepassing van dit Wetboek als wederverkoop

beschouwd.

Met afwijking van het vorenstaande:

a) moet de aanwijzing van lastgever, bij toewijzingen die wettelijk

gedaan zijn onder de schorsende voorwaarde van ontstentenis van

opbod, om van het evenredig recht vrijgesteld te zijn, gedaan worden

vóór de notaris die de toewijzing gedaan heeft of hem betekend

worden uiterlijk op de eerste werkdag na die waarop de wettelijke

termijn voor opbod verstrijkt;

b) moet de aanwijzing van lastgever, in geval van toewijzing ten

gevolge van hoger bod op vrijwillige vervreemding van onroerende

goederen, om van het evenredig recht vrijgesteld te zijn, gedaan

worden vóór de notaris die de toewijzing heeft gedaan of hem

betekend worden uiterlijk op de eerste werkdag na de dag van de

toewijzing.

In die gevallen wordt de aanwijzing ingeschreven of vermeld

onderaan op het proces-verbaal van toewijzing, zonder dat zij aan de

ontvanger der registratie behoeft te worden betekend;

2° de toewijzingen naar aanleiding van rouwkoop, van roerende of

onroerende goederen, wanneer zij geen aanleiding geven tot de

heffing van een hoger evenredig recht dan datgene geheven op de

vorige toewijzing. In het tegenovergesteld geval wordt laatstbedoeld

recht afgerekend van het bedrag van de belasting waartoe de

daaropvolgende toewijzing aanleiding geeft.

Hetzelfde regime is van toepassing op de toewijzingen naar

aanleiding van prijsverhoging in de gevallen waarin het voorbehoud

van prijsverhoging geen schorsende voorwaarde uitmaakt.

3° De overeenkomsten die strekken tot de overdracht van het

vruchtgebruik op de blote eigenaar, wanneer het evenredig

registratierecht of het successierecht door de blote eigenaar of door

4° (…)  4  (…)

5° (…)  5  (…)

6° (…)  6  (…)

7° de overdragende of aanwijzende overeenkomsten, andere dan de

inbrengen onderworpen aan het in artikel 115 bis bepaalde recht die

buitenslands gelegen onroerende goederen tot voorwerp hebben,

zomede de huurcontracten van dergelijke goederen;

8° de overdragende of aanwijzende vervreemdingen onder

bezwarende titel, andere dan die welke aan het in artikel 115 bis

bepaalde recht onderworpen zijn van op te richten, in oprichting zijnde

of nieuwe opgerichte gebouwen, op voorwaarde dat de belasting over

de toegevoegde waarde opeisbaar is voor de levering van de

vervreemde  gebouwen;  de  vestigingen,  overdrachten  of

wederoverdrachten van de zakelijke rechten bedoeld in artikel 9,

tweede lid, 2°, van het Wetboek van de belasting over de

toegevoegde waarde met betrekking tot op te richten, in oprichting,

zijnde of nieuw opgerichte gebouwen, op voorwaarde dat de

belasting over de toegevoegde waarde opeisbaar is op de vestiging of

de overdracht van deze rechten.

De vrijstelling geldt niet voor de grond begrepen in de overeenkomst.  L’exemption ne s’applique pas pour le terrain compris dans

Wanneer de gebouwen samen met de grond waarop ze staan voor

een enige prijs worden vervreemd, wordt het evenredig recht wegens

de vervreemding van de grond berekend over de verkoopwaarde van

de grond, geraamd op het tijdstip van de vervreemding, doch met

inachtneming van de staat van de grond vóór de aanvang van het

werk. Wanneer de vestiging of de overdracht van de in het eerste lid

bedoelde zakelijke rechten tevens betrekking heeft op de grond

waarop de gebouwen staan en voor een enige prijs gebeurt, wordt het

evenredig recht wegens de vestiging of de overdracht van die rechten

op de grond berekend over de waarde van die rechten, geraamd op

het tijdstip van de vestiging of de overdracht, doch met inachtneming

van de staat van de grond vóór de aanvang van het werk. In die

gevallen worden de gegevens nodig voor de berekening van de

rechten opgeheven in een verklaring als omschreven in artikel 168.

Indien de overeenkomst betrekking heeft op het vruchtgebruik of de

blote eigendom van de grond, wordt de belastbare grondslag bepaald

op de wijze vermeld in de artikelen 47 tot 50.

a) het jaar waarin, in voorkomend geval, de onroerende voorheffing

van het gebouw waarop de overeenkomst betrekking heeft voor het

eerst ten kohiere is gebracht;

b) het kantoor waar de belastingplichtige de aangifte moet indienen

voor de heffing van de belasting over de toegevoegde waarde;

c) wanneer de overeenkomst het werk is van een andere dan in artikel

12, § 2, van het Wetboek van de belasting over de toegevoegde waard

bedoelde belastingplichtige, de datum waarop hij kennis heeft

gegeven van zijn bedoeling de verrichting te doen met betaling van de

belasting over de toegevoegde waarde.

In geval van onjuistheid van die vermeldingen, verbeurt de cedent een

boete gelijk aan het ontdoken recht;

9° (…)  9  (…)

10° de contracten van onroerende financieringshuur bedoeld in

artikel 44, § 3, 2°, b, van het Wetboek van de belasting over de

toegevoegde waarde;

11° de inbreng van goederen in Europese economische

samenwerkingsverbanden;

12° de teruggave van de onroerende goederen aan de leden van

Europese economische samenwerkingsverbanden die deze goederen

hebben ingebracht, wanneer de teruggave gebeurt tengevolge van de

uittreding  van  deze  leden  of  de  ontbinding  van  het

samenwerkingsverband.

Indien onroerende goederen verkregen worden in andere

omstandigheden dan deze voorzien in het vorige lid, is voor deze

verkrijging, hoe zij ook gebeurt, het voor verkopingen bepaalde recht

verschuldigd.

13° (…)

14° de inbrengen van onroerende goederen, andere dan die welke

gedeeltelijk of geheel tot bewoning aangewend worden of bestemd

zijn en door een natuurlijke persoon ingebracht worden, in

vennootschappen met zetel van werkelijke leiding en statutaire zetel

buiten België, of met statutaire zetel in België doch met zetel van

werkelijke leiding op het grondgebied van één van de lidstaten van de

Europese Unie. Deze vrijstelling geldt voor zover de inbreng met

maatschappelijke rechten wordt vergolden. Indien de inbreng zowel

evenredig verdeeld te zijn tussen de waarde die aan de onroerende

goederen is toegekend en die welke aan de andere goederen is

toegekend. In de mate dat de inbreng betrekking heeft op in België

gelegen onroerende goederen wordt hij onderworpen aan het recht

voorgeschreven voor verkopingen.

In geval van onjuiste verklaring betreffende de aanwending of de

bestemming van het onroerend goed, worden de bijvoeglijke rechten

opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.

### HOOFDSTUK V - Registratie in debet

###### Artikel 160

(gewijzigd bij art. 5 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van

toepassing vanaf 01.01.2015 (art. 8))

In afwijking van artikel 169 ter , worden in debet geregistreerd:

1° de akten opgemaakt ten verzoek van de persoon die

rechtsbijstand heeft verkregen voor de rechtspleging waarop

bedoelde akten betrekking hebben, met inbegrip van de akten tot ten

uitvoerlegging van het vonnis of arrest.

Het gaat evenzo met de rechterlijke beslissingen wanneer

rechtsbijstand aan de eiser werd toegestaan. Wanneer bijstand aan

de verweerder werd toegestaan en de eiser in gebreke blijft de op het

vonnis of arrest verschuldigde rechten te consigneren, kan de

verweerder registratie in debet ervan bekomen.

Verlening van bijstand dient te worden vermeld in al de akten die

ervan genieten. Deze vermelding moet de datum der beslissing

alsmede het gerecht of het bureau voor rechtsbijstand, dat ze heeft

getroffen, aanduiden.

De rechten alsmede de andere kosten worden ingevorderd

overeenkomstig de bepalingen van het Gerechtelijk Wetboek;

2° de akten en vonnissen betreffende procedures bij faillissement,

wanneer de kosteloosheid door de rechtbank werd bevolen.

De kosteloosheid van de rechtspleging moet vermeld worden in alle

akten die ze genieten.

3° de akten betreffende de vorderingen tot interpretatie of tot

verbetering van een vonnis of arrest.

De rechten worden ingevorderd overeenkomstig de bepalingen van

het Gerechtelijk Wetboek;

4° de akten opgemaakt ten verzoek en ter verdediging van de

beklaagden of betichten in lijfstraffelijke, boetstraffelijke of

politiezaken er weze al dan niet een burgerlijke partij in het geding met

inbegrip van de akten waartoe de borg, welke dient gesteld om de

voorlopige invrijheidstelling van een voorlopig gedetineerd betichte te

bekomen, aanleiding geeft.

De rechten worden in de gerechtskosten begrepen en als zodanig

ingevorderd ten laste van de tot betaling er van veroordeelde partij.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

### HOOFDSTUK VI - Kosteloze registratie

###### Artikel 161

(1° en 12°, gewijzigd bij art. 29 van de wet van 10.02.2026 (B.S., 27.02.2026).

Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1)) (2)

Worden kosteloos geregistreerd:  Sont enregistrés gratuitement :

1° Akten in der minne verleden ten name of ten bate van de Staat,

gefedereerde entiteiten en de openbare instellingen ervan.

De akten in der minne, die betrekking hebben op onroerende

goederen die uitsluitend bestemd zijn voor onderwijs, verleden ten

name of ten bate van de inrichtende machten van het

gemeenschapsonderwijs of het gesubsidieerd onderwijs, alsook ten

name of ten bate van verenigingen zonder winstoogmerk voor

patrimoniaal beheer die tot uitsluitend doel hebben onroerende

goederen ter beschikking te stellen voor onderwijs dat door de

voornoemde inrichtende machten wordt versterkt.

De akten in der minne verleden ten name of ten bate van de naamloze

vennootschappen van publiek recht ASTRID, BIO, Infrabel, HR Rail en

NMBS.

vallen.

1° bis De vonnissen en arresten houdende veroordeling van de Staat,

de Gemeenschappen en de Gewesten, van de openbare instellingen

die zijn opgericht door de Staat, en van de inrichtingen van de

Gemeenschappen en de Gewesten.

2° Overdrachten in der minne van onroerende goederen ten

algemenen nutte, aan Staat, provinciën, gemeenten, openbare

instellingen en aan alle andere tot onteigening gerechtigde

organismen of personen: akten betreffen de wederafstand na

onteigening ten algemenen nutte in de gevallen waarin hij bij de wet

toegelaten is; akten tot vaststelling van een ruilverkaveling of een

herverkaveling verricht met inachtneming van de bepalingen van

#### Hoofdstuk VI van Titel I van de wet houdende organisatie van de

ruimtelijke ordening en van de stedebouw. De akten houdende

overdracht van een afgedankte bedrijfsruimte aan de Staat of een

andere publiekrechtelijke rechtspersoon.

3° De akten houdende oprichting, wijziging, verlenging of ontbinding

van de Nationale Maatschappij der Waterleidingen, van de

verenigingen overeenkomstig de bepalingen der wetten van 18

augustus 1907 en van 1 maart 1922 gevormd, van de Maatschappij

voor het Intercommunaal Vervoer te Brussel, van de maatschappij

voor tussengemeentelijk vervoer beheerst door de wet betreffen de

oprichting van maatschappijen voor stedelijk gemeenschappelijk

vervoer, van de Federale Investeringsmaatschappij, de gewestelijke

investeringsmaatschappijen en van de Belgische Naamloze

Vennootschap tot Exploitatie van het Luchtverkeer (Sabena).

4° Akten die, bij toepassing van de organieke wet betreffen de

openbare centra voor maatschappelijk welzijn, de overgave

vaststellen van goederen aan of de inbreng in openbare centra voor

maatschappelijk welzijn ofwel de overgave van goederen aan of de

inbreng in op grond van voornoemde wet opgerichte verenigingen,

evenals akten houdende verdeling, na ontbinding of splitsing van een

bovenbedoelde vereniging.

5° Waarmerkingen en akten van bekendheid, in de gevallen bedoeld

in artikel 139 van de hypotheekwet van 16 december 1851;

6° Akten houdende verkrijging door vreemde Staten van onroerende

goederen die bestemd zijn tot vestiging van hun diplomatieke of

consulaire vertegenwoordiging in België, of voor de woning van het

hoofd der standplaats.

7° De akten, vonnissen en arresten betreffen de uitvoering van de

wet houdende bijzondere maatregelen inzake ruilverkaveling van

landeigendommen in der minne;

8° (…)

9° Akten, vonnissen en arresten betreffen de uitvoering der wet op

de ruilverkaveling van landeigendommen uit kracht van de wet en de

wet houdende bijzondere maatregelen inzake ruilverkaveling van

landeigendommen uit kracht van de wet bij de uitvoering van grote

infrastructuurwerken.

10°  Akten  tot  vaststelling  van  een  vereniging  van

kolenmijnconcessies, een afstand, een uitwisseling of een

verpachting van een gedeelte van deze concessies.

De kosteloosheid is ondergeschikt aan de voorwaarde dat een

eensluidend verklaard afschrift van het koninklijk besluit, waarbij de

verrichting toegelaten of bevolen wordt, aan de akte gehecht is op het

ogenblik der registratie.

Het eerste lid is mede van toepassing wanneer bedoelde akten

terzelfder tijd de afstand vaststellen van goederen die voor de

exploitatie van de afgestane concessie of het afgestane

concessiegedeelte worden gebruikt.

11° De akten en attesten die gevoegd moeten worden bij de akten

van schenking van ondernemingen.

12°

a) de akten houdende verhuring, onderverhuring of overdracht van

huur van in België gelegen onroerende goederen of gedeelten van

onroerende goederen, die uitsluitend bestemd zijn tot huisvesting van

een gezin of van één persoon;

b) (…)  b) (…)

c) de plaatsbeschrijvingen opgemaakt naar aanleiding van een onder

a) bedoelde akte;

d) de documenten die krachtens wettelijke, decretale of ordonnantiële

bepalingen gevoegd zijn bij een onder a) bedoelde akte op het ogenblik

dat zij ter registratie wordt aangeboden.

13° De overeenkomsten bedoeld in artikel 132 bis van het Wetboek

van de inkomstenbelastingen 1992.

ambtenaar voor het verlijden van de volmacht geen ereloon, vacaties

of kosten vraagt en voor zover de volmacht uitsluitend effect sorteert

binnen de zes maanden na de ondertekening ervan.

15° De verklaring van verwerping ten overstaan van een notaris

bedoeld in artikel 4.44, eerste lid, van het Burgerlijk Wetboek, onder

de voorwaarden bedoeld in het derde lid van hetzelfde artikel. (1)

De bijlagen bij een dergelijke verklaring worden ook kosteloos

geregistreerd, behalve wanneer ze een in Titel I, Hoofdstuk IV van het

Wetboek bepaald recht, ander dan het in artikel 158 bepaalde recht,

opeisbaar maken.

16° de akten van erfopvolging bedoeld in artikel 3.30, § 1, 7°, van het

Burgerlijk Wetboek, op voorwaarde dat de instrumenterende

ambtenaar voor het opstellen van de akte geen vacaties of kosten

vraagt en de akte opgesteld wordt binnen de 6 maanden na het

overlijden.

----------

Nota:  Note :

(1) Vanaf 03.08.2017 tot 02.08.2020 mag het netto actief van de

nalatenschap niet meer bedragen dan 5.000 EUR. Vanaf 03.08.2020 tot

31.07.2023 bedraagt het geïndexeerde bedrag 5.219,21 euro. Vanaf

01.08.2023 tot 31.07.2026 bedraagt het geïndexeerde bedrag 6.093,20

euro (EE/107.394).

(2) Wat betreft art. 161, 1°, W.Reg.: De federale wetgever treedt hier uitsluitend

op in het kader van niet-geregionaliseerde belastingen, terwijl de tarifering van

gewestelijke registratierechten onder de bevoegdheid van de gewesten valt.

Door de tekst te wijzigen, rationaliseert de federale wetgever de bepalingen die

van toepassing zijn op zijn eigen belastingen, zonder de regionale versies te

beïnvloeden, die afzonderlijk blijven en niet door deze wijzigingen worden

geraakt (Parl.St., Kamer: 56-1127 001, blz. 8).

###### Artikel 161/1

(gewijzigd bij art. 1 van het KB van 03.10.2019 (B.S., 30.10.2019). Tekst van

toepassing vanaf 09.11.2019 (art. -))

Onverminderd artikel 162, 51°, worden de akten, vonnissen en

arresten, betreffende een overeenkomstig Boek XX, Titel V van het

Wetboek van economisch recht ingestelde procedure van

gerechtelijke reorganisatie vrijgesteld van de registratierechten die

niet worden bedoeld in artikel 3 van de bijzondere wet van 16 januari

1989 betreffende de financiering van de Gemeenschappen en de

Gewesten.

##### registratie

###### Artikel 162

(10°, opgeheven bij art. 4 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst

van toepassing vanaf 02.09.2023 (art. -))

Zijn onder het in artikel 163 aangewezen voorbehoud, van de

formaliteit der registratie vrijgesteld.

1° Akten, vonnissen en arresten in kieszaken;  1  Les actes, jugements et arrêts en matière électorale ;

2° Akten, vonnissen en arresten betreffende de uitvoering van

wetten en reglementen op de militie, de vergoeding inzake militie en

de militaire opeishingen;

3° Akten, vonnissen en arresten betreffende de uitvoering der wetten

en reglementen inzake 's lands mobilisatie en de bescherming der

bevolking in geval van oorlog, de burgerlijke opeischingen en vrijwillige

dienstnemingen, alsmede de in vredestijd aangegane uitgestelde

contracten;

4 ° Akten, vonnissen en arresten betreffende de uitvoering van

wetten en reglementen inzake belastingen ten bate van de Staat,

gefedereerde entiteiten, provincies, gemeenten, polders en

wateringen;

5° Exploten en andere akten, in strafzaken opgemaakt ten verzoek

van ambtenaren van het openbaar ministerie en van andere

ambtenaren of besturen waaraan de wet de vordering voor de

toepassing der straffen opdraagt; bovenaan op bedoelde akten

worden de woorden Pro Justitia aangebracht;

5° bis De akten waartoe de rechtsplegingen in burgerlijke zaken of

tuchtzaken aanleiding geven, wanneer het openbaar ministerie of de

vrederechter van ambtswege optreedt;

6° (…)  6  (…)

6° bis Akten, vonnissen en arresten betreffende de uitvoering der wet

op eerherstel in strafzaken en deze betreffende de uitvoering der wet

tot bescherming der maatschappij tegen de abnormalen en de

gewoontemisdadigers;

stedenbouw, met uitzondering van de in artikel 161, 2°, bedoelde

akten;

8° Akten, vonnissen en arresten betreffende ingebruikneming van

gronden door den Staat met het oog op de inrichting van 's Lands

verdediging;

9° Akten en vonnissen betreffende procedures vóór den

onderzoeksraad voor de zeevaart;

10° (…)  10  (…)

11° De akten, vonnissen en arresten inzake onttrekking van de zaak

aan de rechter, zoals bedoeld in het Gerechtelijk Wetboek, deel III, titel

IV, hoofdstuk III;

12° De akten, vonnissen en arresten inzake wraking, zoals bedoeld in

het Gerechtelijk Wetboek, deel IV, boek II, titel III, hoofdstuk V;

13° Akten en vonnissen betreffende procedures vóór vrederechters,

wanneer het bedrag van den hoofdeisch het maximum van den

laatsten aanleg niet te boven gaat, of wanneer het gaat om een

procedure  inzake  uitkering  tot  onderhoud  of  ingesteld

overeenkomstig artikel 221 van het Burgerlijk Wetboek; Akten en

vonnissen  betreffende  procedures  vóór  de

ondernemingsrechtbanken, wanneer het geschillen geldt die gegrond

zijn op de bepalingen van het Wetboek van bepaalde voorrechten op

zeeschepen en diverse bepalingen of van de wet van 5 mei 1936 op

de rivierbevrachting, indien het bedrag van de hoofdeis het bedrag

van de laatste aanleg vóór het vredegerecht niet te boven gaat;

13° bis De exploten van gerechtsdeurwaarders opgesteld ter

vervanging van een gerechtsbrief in het geval bepaald in artikel 46, §

3, van het Gerechtelijk Wetboek;

Bovenaan het exploot dient te worden vermeld dat het is opgesteld

ter vervanging van een gerechtsbrief en zulks met vermelding van het

artikel van het Gerechtelijk Wetboek op grond waarvan de betekening

wordt gedaan;

14° Akten, vonnissen en arresten betreffende procedures ingesteld

bij de wetten van 10 Maart 1900 op de arbeidsovereenkomst, van 7

Augustus 1922 op de bediendenarbeidsovereenkomst en van 5 Juni

1928 houdende regeling van het arbeidscontract wegens

scheepsdienst, met betrekking tot de bekwaamheid van de

15° Akten opgemaakt ten verzoeke van de ambtenaren van het

openbaar ministerie betreffende de uitvoering van rogatoire

opdrachten die uitgaan van buitenlandse rechters;

16° (...)  16  (…)

17° De akten, vonnissen en arresten betrekking hebbende op de

uitvoering van de wet betreffende het herstel van zekere schade

veroorzaakt aan private goederen door natuurrampen;

18° De akten, vonnissen en arresten betreffende procedures

ingesteld bij de wet van 26 juni 1990 betreffende de bescherming van

de persoon van de geesteszieke en bij de artikelen de bepalingen van

het vierde deel, boek IV, hoofdstuk X van het Gerechtelijk Wetboek.

19° de akten, vonnissen en arresten betreffende procedures tot

machtiging ingesteld overeenkomstig artikel 4.40, § 3 van het

Burgerlijk Wetboek;

20° (...)  20  (…)

21° Voorzieningen in verbreking van het openbaar ministerie en

derzelver betekeningen;

22° (...)  22  (…)

23° Akten opgemaakt alsmede vonnissen of arresten gewezen voor

de toepassing van de wetten op het gebruik van de talen in de

gerechtszaken en in bestuurszaken;

24° Akten betreffende de uitvoering van de bepalingen van het

Gerechtelijk Wetboek inzake de inruststelling der magistraten;

25° (...)  25  (…)

26° (...)  26  (…)

26° bis (...)  26° bis (…)

27° (...)  27  (…)

28° (...)  28  (…)

29°  Getuigschriften,  akten  van  bekendheid,  volmachten,

machtigingen met inbegrip van de verzoekschriften die er zouden

verband mede houden, wanneer die stukken opgemaakt of uitgereikt

worden om te worden overgelegd aan de diensten van het Grootboek

goedkeuring van de bestuursoverheid of aan dezer controle

onderworpen;

30° (...)  30  (…)

31° (...)  31  (…)

32° (...)  32  (…)

33° Akten opgemaakt voor den dienst van de openbare kassen van

lening, met inbegrip van processen-verbaal van openbaren verkoop

van in pand gegeven roerende voorwerpen;

33° bis Akten, vonnissen en arresten betreffende betwistingen inzake

arbeidsovereenkomsten, leerovereenkomsten en overeenkomsten

voor versnelde beroepsopleiding, betreffende betwistingen tussen

werknemers naar aanleiding van het werk alsmede tussen personen

die samen een beroep uitoefenen waarbij hoofdzakelijk handenarbeid

wordt verricht en inzonderheid tussen een schipper ter visserij en de

schepelingen met wie hij geassocieerd is, betreffende betwistingen

van burgerlijke aard die het gevolg zijn van een overtreding van de

wetten en verordeningen betreffende de arbeidsreglementering en

de aangelegenheden onder de bevoegdheid van de arbeidsrechtbank;

34° Akten, vonnissen en arresten betrekkelijk de uitvoering van de

wetten en reglementen op de kinderbijslagen;

35° Akten, vonnissen en arresten betrekkelijk de uitvoering van de

wetten en reglementen op de verzekering tegen de geldelijke

gevolgen van ouderdom en vroegtijdige dood, op de verzekering

tegen de geldelijke gevolgen van ouderdom en vroegtijdige dood van

bedienden en op het pensioenstelsel der mijnwerkers;

35° bis De akten, vonnissen en arresten in verband met de uitvoering

van de wetten en verordeningen betreffende het sociaal statuut der

zelfstandigen;

35° ter De akten, vonnissen en arresten betreffende de uitvoering van

de wetten en verordeningen betreffende de rust-, invaliditeits-, en

overlevingspensioenen ten laste van de Staat, de provincies, de

gemeenten, de openbare instellingen, de Nationale Maatschappij der

Belgische Spoorwegen of alle andere organismen of openbare

diensten waarvan het personeel onderworpen is aan een bijzondere

pensioenregeling getroffen bij of krachtens een wet;

beroepspersoneel der kaders in Afrika en der personeelsleden die zijn

bedoeld in artikel 31, van het koninklijk besluit van 21 mei 1964 tot

coördinatie van de wetten betreffende het personeel in Afrika;

36° Akten, vonnissen en arresten betreffende de uitvoering der

wetten en reglementen op het herstel van schade ten gevolge van

arbeidsongevallen, van ongevallen overkomen op weg naar of van

den arbeid, of van beroepsziekten;

36° bis Akten, vonnissen en arresten betreffende betwistingen in

verband met de rechten en verplichtingen voortvloeiend uit de wet op

de sociale reclassering van de minder-validen;

36° ter Akten, vonnissen en arresten betreffende betwistingen in

verband  met  de  oprichting  en  de  inrichting  van  de

ondernemingsraden, alsmede van de diensten en comités tot

veiligheid, hygiëne en verfraaiing der werkplaatsen, daarin begrepen

de diensten en comités opgericht in mijnen, groeven en graverijen;

37° Akten, vonnissen en arresten betreffende de uitvoering der

wetten en reglementen op de onvrijwillige werkloosheid;

37° bis Akten, vonnissen en arresten betreffende de uitvoering der

wetten en reglementen in verband met de maatschappelijke

zekerheid;

38° Akten en beslissingen betreffende het verzoek om rechtsbijstand

of de betwisting ervan; akten van schikking inzake uitkering tot

onderhoud verleden op het bureel van bijstand;

39° Akten, vonnissen en arresten betreffende de invordering van de

voorschotten van Rijkswege gedaan in uitvoering van de bepalingen

van het Gerechtelijk Wetboek betreffende de gerechtelijke bijstand;

40° Akten, vonnissen en arresten betreffende de uitvoering van de

wet van 27 juni 1969 betreffende het toekennen van

tegemoetkomingen aan de minder-validen;

41° Akten nodig voor het huwelijk van personen wier onvermogen

blijkt uit een getuigschrift van den burgemeester van hun

verblijfplaats of van dezes gelastigde;

42° Akten, vonnissen en arresten betreffende procedures inzake de

voogdij van minderjarigen;

44° Akten, vonnissen en arresten betreffende de verklaringen van

nationaliteit of van keuze van vaderland, wanneer het onvermogen

der belanghebbenden vastgesteld is overeenkomstig bovenstaand

nr. 41°;

45° De akten, vonnissen en arresten betreffende betwistingen in

verband met een maatregel van sociale bescherming;

46° De akten, vonnissen en arresten, betreffende de procedure van

collectieve schuldenregeling ingesteld overeenkomstig de artikelen

1675/2 tot en met 1675/19 van het Gerechtelijk Wetboek;

46° (47°) (1) De overdrachten tussen de componenten van een

politieke partij zoals die zijn bepaald bij artikel 1, 1°, tweede lid, van de

wet van 4 juli 1989 betreffende de beperking en de controle van de

verkiezingsuitgaven voor de verkiezingen van de federale Kamers, de

financiering en de open boekhouding van de politieke partijen;

47° (48°) (2) De akten, vonnissen en arresten betreffende de

tegemoetkomingen bedoeld in de wet van 21 februari 2003 tot

oprichting van een Dienst voor alimentatievorderingen bij de FOD

Financiën;

47° (49°) (3) De akten, de vonnissen en arresten, betreffende het

toestaan van betalingsfaciliteiten inzake consumentenkrediet,

ingesteld overeenkomstig de artikelen 1337 bis tot en met 1337 octies

van het Gerechtelijk Wetboek;

48° (50°) De akten en vonnissen betreffende de procedures voor de

rechters voor de bescherming van de maatschappij en de

strafuitvoeringsrechtbanken, alsook de arresten gewezen als gevolg

van een cassatieberoep tegen een beslissing van de rechter voor de

bescherming van de maatschappij of de kamer voor de bescherming

van de maatschappij;

51°  De  akten,  vonnissen  en  arresten  betreffende  een

overeenkomstig Boek XX, Titel V van het Wetboek van economisch

recht ingestelde procedure van gerechtelijke organisatie, behalve:

a) de akten die tot bewijs strekken van een overeenkomst

onderworpen aan een registratierecht bedoeld in artikel 3 van de

bijzondere wet van 16 januari 1989 betreffende de financiering van

de Gemeenschappen en de Gewesten;

b) de in artikelen 146 en 147 bedoelde vonnissen en arresten;  b) les jugements et arrêts visés aux articles 146 et 147.

----------

Nota:  Note :

(1) Aangezien door de wet van 05.07.1998 (B.S., 31.07.1998), eveneens een

“46°” werd ingevoegd, zou het “46°” dat werd ingevoegd door de wet van

19.11.1998 (B.S., 10.12.1998), in feite “47°” moeten zijn.

(2) Het “47°” ingevoegd bij art. 28, § 1 van de wet van 21.02.2003 zou het

“48°” moeten zijn.

(3) Het “47°” ingevoegd bij art. 82 van de wet van 24.03.2003 zou het “49°”

moeten zijn.

###### Artikel 163

(gewijzigd bij art. 16 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van

toepassing vanaf 04.05.1965 (art. -))

De bij voorgaand artikel ingevoerde vrijstelling is niet toepasselijk op

de in dit artikel opgesomde akten, vonnissen en arresten, in zover zij

tot bewijs van een overeenkomst strekken voorzien in artikel 19, 2°.

Zij is niet van toepassing op andere dan gerechtelijke akten, in zover

zij tot bewijs van een in artikel 19, 3° of 5°, bedoelde overeenkomst

strekken.

Tenzij er anders over beschikt wordt, is ze niet van toepassing op:  A moins qu’il n’en soit autrement disposé, elle n’est pas applicable :

a) processen-verbaal van verkoop van in beslag genomen roerende of

onroerende goederen en alle nakomende handelingen welke derde

verkrijgers aanbelangen;

b) processen-verbaal van rangregeling en van verdeling bij aandelen.  b) aux procès-verbaux d’ordre et de distribution par contribution.

###### Artikel 164

Zijn mede van de formaliteit der registratie vrijgesteld, de uitgiften,

afschriften van en uittreksels uit akten welke geregistreerd werden of

die krachtens artikel 162 van de formaliteit zijn vrijgesteld.

###### Artikel 165

### HOOFDSTUK VIII - Diverse bepalingen betreffende de

##### vereffening van de rechten en de betaling van het

##### verschuldigde bedrag

(vervangen bij art. 6 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van

toepassing vanaf 01.01.2015 (art. 8))

###### Artikel 166

(gewijzigd bij art. 5, § 7, 1° van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1).

Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 3°

van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1) err. (B.S., 21.12.2001).

Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))

In geval van openbare verkoping van roerende of onroerende

goederen of van openbare verhuring, in verschillende loten, wordt het

recht vereffend op het samengevoegd bedrag der aan hetzelfde tarief

onderworpen loten.

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de

hogere eurocent afgerond.

###### Artikel 167

Wanneer er niet anderszins bij deze titel over beschikt is, mag het

bedrag van het op een akte of een verklaring te heffen evenredig recht

niet minder dan in het algemeen vast recht bedragen.

###### Artikel 168

(gewijzigd bij art. 17 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van

toepassing vanaf 04.05.1965 (art. -))

Wanneer de sommen en waarden of andere ter vereffening van de

belasting noodzakelijke gegevens niet voldoende uitgedrukt zijn in

een ter formaliteit aangeboden akte, zijn de partijen of de werkende

openbare officier, in hun naam, er toe gehouden daarin, vóór de

Wanneer een zelfde overeenkomst meteen op in België gelegen

onroerende goederen en op andere goederen slaat, moet de

overeengekomen  waarde  of,  in  voorkomend  geval,  de

verkoopwaarde van de goederen van elkeen der categorieën, zelfs

indien het tarief van de belasting niet verschilt naar gelang van de aard

van de goederen, afzonderlijk aangeduid worden, hetzij in de akte,

hetzij in een door de partijen of, in hun naam, door de werkende

notaris vóór de registratie gewaarmerkte en ondertekende verklaring

onderaan op de akte.

Indien de bepaling van den belastbaren grondslag geheel of

gedeeltelijk van de schatting van een levenslang recht afhangt, moet

de verklaring naam, voornamen, woonplaats, plaats en datum van

geboorte van de beneficianten van dit levenslang recht vervatten.

###### Artikel 169

De rechten verschuldigd op akten waarbij eigendom of vruchtgebruik

van een handelszaak overgedragen of aangewezen worden, worden

geheven volgens de aard van elk der goederen die er deel van

uitmaken en op de bij dit wetboek vastgestelde grondslagen.

De schulden die al dan niet met de handelszaak in verband staan en

die door den nieuwe eigenaar of vruchtgebruiker ten laste genomen

worden, moeten als lasten van de overeenkomst beschouwd worden.

###### Art. 169. bis

(ingevoegd bij art. 70 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van

toepassing vanaf 25.01.1999 (art. -))

Voor de toepassing van de artikelen 115 bis en 140 bis , moet de

aanwending of de bestemming van een onroerend goed worden

nagegaan per kadastraal perceel of per gedeelte van kadastraal

perceel wanneer dat gedeelte is ofwel een afzonderlijke huisvesting,

ofwel een afdeling van de productie of van de werkzaamheden die, of

een onderdeel daarvan dat, afzonderlijk kan werken, ofwel een

eenheid die van de andere goederen of delen die het perceel vormen

kan worden afgezonderd.

###### Art. 169. ter

De rechten en, in voorkomend geval, de boeten en de interesten, zoals

zij door het in artikel 39 bedoelde kantoor zijn vastgesteld, worden

voorafgaandelijk aan de registratie betaald.

Behalve wanneer ze verschuldigd zijn in het kader van de

registratierechten die, krachtens artikel 3, eerste lid, 6° tot 8°, van de

bijzondere wet van 16 januari 1989 betreffende de financiering van

de gemeenschappen en de gewesten, worden aangemerkt als

gewestelijke belastingen, kan de Koning, bij een besluit vastgesteld na

overleg in de Ministerraad, in afwijking van het eerste lid bepalen dat

de rechten, boeten en interesten die verschuldigd zijn op de door Hem

aangewezen categorieën van akten, kunnen of moeten worden

betaald na de registratie. In voorkomend geval bepaalt hij de termijn

en de nadere regels van de betaling.

Niemand kan, onder voorwendsel van betwisting van het

verschuldigde bedrag of om enige andere reden, die betaling

verminderen of uitstellen, behoudens het recht om teruggave te

vorderen, indien daartoe grond bestaat.

### HOOFDSTUK IX - Verplichtingen met het oog op het

##### verzekeren van het heffen van de rechten

#### Afdeling I - Vermeldingen op te nemen in bepaalde akten

###### Artikel 170

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Wanneer, in een ander dan een vonnis of arrest aan de formaliteit

onderworpen authentieke akte, melding wordt gemaakt van een

onderhandsche akte of van een buitenslands verleden akte vallende

in de termen van artikel 19, 2° of 3°, moet die authentieke akte

afschrift van de vermelding der registratie van bedoelde akte

bevatten.

Indien die akte niet geregistreerd werd, dan wordt daarvan in de

authentieke akte melding gemaakt.

###### Art. 170. bis

(ingevoegd bij art. 6 van de wet van 07.03.2002 (B.S., 19.03.2002). Tekst van

toepassing vanaf 01.01.2002 (art. 7))

In geval van een schenking moet de notaris in de akte een verklaring

van de schenker opnemen die vermelding inhoudt van het adres en

de datum en duur van de vestiging van de verschillende fiscale

woonplaatsen die de schenker gehad heeft in de periode van vijf jaar

voorafgaand van de datum van de schenking.

In geval van weigering de verklaring te doen of bij onjuiste of

onvolledige verklaring verbeurt de schenker een boete ten bijdrage

van tweemaal de aanvullende rechten.

De notaris die nagelaten heeft de schenker te vragen de verklaring te

doen, verbeurt een boete van 25 EUR.

###### Artikel 171

(aangevuld bij art. 112 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).

Tekst van toepassing vanaf 17.08.2020 (art. -))

Alle expedities, afschriften van of uittreksels uit een burgerlijke of

gerechtelijke authentieke akte die aan de formaliteit onderworpen is

of die in artikel 8 bis bedoeld is, moeten, op straf van een boete van 25

EUR, een afschrift van de vermelding van de registratie of van de

vermelding voorzien in het tweede lid van artikel 8 bevatten.

Het eerste lid is niet van toepassing op een afschrift gemaakt met het

oog op de aanbieding ervan ter formaliteit van de registratie.

#### Afdeling II - Voorschriften betreffende het uitreiken van

uitgiften

###### Artikel 172

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

Notarissen,  gerechtsdeurwaarders,  griffiers  der  hoven  en

rechtbanken en bestuurlijke overheden mogen; vóór het nakomen

van de formaliteit der registratie, de akten welke zij verplicht zijn te

doen registreren of waarvan de rechten in hun handen moeten

worden geconsigneerd, niet in brevet, uitgifte, afschrift of uittreksel

uitreiken, zelfs zo de voor de registratie gestelde termijn niet

verstreken is.

Alle overtreding van dit verbod wordt met een geldboete van 25 EUR

gestraft.

###### Artikel 173

(7°bis, ingevoegd bij art. 113 van de wet van 31.07.2020 (B.S., 07.08.2020 -

ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))

Van voorgaand artikel wordt afgeweken ten aanzien van:  Il est dérogé à l’article précédent en ce qui concerne :

1° De uitgiften van akten, verleden voor notarissen of bestuurlijke

overheden, die aanleiding geven tot een hypothecaire formaliteit

waarbij de bedoelde uitgiften eerst aan de betrokken partijen mogen

worden afgegeven nadat zij, overeenkomstig artikel 171 zijn

aangevuld, met een afschrift van de vermelding van de registratie of

met de in artikel 8, tweede lid, voorgeschreven vermelding;

1° bis De uitgiften en uittreksel van akten, verleden voor notarissen,

die aanleiding geven tot neerlegging ter griffie van de

ondernemingsrechtbank overeenkomstig artikel 2:12 van het

Wetboek van vennootschappen en verenigingen;

1° ter de uitgiften en uittreksels van akten, verleden voor notarissen,

die worden uitgereikt met als enig doel de inschrijving van een

onderneming bij een ondernemingsloket, op voorwaarde dat dit

uitdrukkelijk vermeld wordt op de uitgifte of het uittreksel;

2° Afschriften welke vereist zijn voor de betekening van exploten en

van andere soortgelijke akten;

3° Niet ondertekende afschriften van vonnissen en arresten;  3  Les copies non signées des jugements et arrêts ;

4° Vonnissen en arresten die, met het oog op de dringende

noodzakelijkheid, op de minuut en vóór de registratie uitvoerbaar

verklaard worden;

bestemming dragen en mogen tot geen andere doeleinden worden

gebruikt;

6° Uitgiften van vonnissen en arresten die worden uitgereikt aan het

openbaar ministerie, alsmede uitgiften, afschriften of uittreksels die

in strafzaken worden uitgereikt aan de Rijksagenten welke belast zijn

met de tenuitvoerlegging van vonnissen en arresten;

7° Afschriften waarvan de aflevering wegens hoogdringendheid

werd bevolen door de voorzitter van de rechtbank van eerste aanleg;

7° bis de afschriften van de vonnissen en arresten gemaakt met het

oog op de aanbieding ervan ter formaliteit van de registratie;

8° de gedematerialiseerde afschriften van notariële akten, die

worden neergelegd in de Notariële Aktebank overeenkomstig artikel

18 van de wet van 25 ventôse jaar XI op het notarisambt.

###### Artikel 174

(opgeheven bij art. 13 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst

van toepassing vanaf 01.11.1986 (art. 15))

(…)

###### Artikel 175

(opgeheven bij art. 17 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

(…)

#### Afdeling III - Repertorium van de akten

###### Artikel 176

(gewijzigd bij art. 48, § 4 van de wet van 05.07.1963 (B.S., 17.07.1963). Tekst

van toepassing vanaf 28.09.1963 (art. 52))

volgorde der nummers, alle akten van hun ambt inschrijven.

###### Artikel 177

(gewijzigd bij art. 53 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).

Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))

In elk artikel van het repertorium dienen vermeld:  Chaque article du répertoire mentionne :

1° volgnummer;  1  son numéro d’ordre ;

2° datum en aard van de akte;  2  la date et la nature de l’acte ;

3° naam, voornamen, woonplaats en identificatienummer of

ondernemingsnummer bedoeld in artikel 2, vierde lid, van de partijen;

4° bondige aanduiding der onroerende goederen;  4  la désignation sommaire des immeubles ;

5° vermelding van de registratie;  5  la relation de l’enregistrement ;

6° wat aangaat de gerechtsdeurwaarders, de kosten van hun akten

en exploten na aftrek van hun verschotten.

De Koning kan aanvullende vermeldingen voorschrijven of

afwijkingen toestaan.

###### Artikel 178

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Een boete van 25 EUR wordt verbeurd voor elke weggelaten of te laat

in het repertorium ingeschreven akte, voor elke akte ingeschreven

met tussenregel of met vervalsing, alsmede voor elke akte van

vroegere datum dan die van het proces-verbaal van nummering en

waarmerk van het repertorium.

###### Artikel 179

De in artikel 176 bedoelde repertoria die moeten worden gehouden

door de notarissen, mogen overeenkomstig artikel 29 van de wet van

16 maart 1803 tot regeling van het notarisambt hetzij op papier, hetzij

op een gedematerialiseerde wijze die is vastgesteld door de Nationale

Kamer van notarissen in een door de Koning goedgekeurd reglement,

worden gehouden.

De Koning kan bepalen dat de repertoria die door de

gerechtsdeurwaarders moeten worden gehouden, mogen worden

gehouden op een gedematerialiseerde wijze die vastgesteld is door

de Nationale Kamer van gerechtsdeurwaarders in een door de Koning

goedgekeurd reglement.

###### Artikel 180

(gewijzigd bij art. 54 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).

Tekst van toepassing vanaf 01.04.2014 (art. 87, 3°))

De in artikel 176 aangeduide personen zijn er toe gehouden, om de

drie maand, hun repertorium voor te leggen aan de ontvanger van het

kantoor aangeduid in artikel 39, 1°, eerste lid, die het viseert en in zijn

visum het aantal ingeschreven akten vermeldt.

Deze voorlegging geschiedt binnen de eerste tien dagen van de

maanden januari, april, juli en oktober van elk jaar.

De Koning kan voor de op gedematerialiseerde wijze gehouden

repertoria bijzondere regels vaststellen wat de modaliteiten van de

voorlegging en het visum van het repertorium betreft.

Bij laattijdige voorlegging van het repertorium wordt een boete

verbeurd van 25 euro per week vertraging.

###### Art. 180. bis

(lid 1, gewijzigd bij art. 24 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Een kopie van de geregistreerde uitgifte en van de geregistreerde

bijlagen wordt, samen met de vermelding van de registratie,

gedurende twintig jaar bewaard door de instrumenterende notaris.

rekening van de notaris.

Die bewaring geschiedt:  Cette conservation a lieu :

1° voor de akten die zijn opgenomen in de Notariële Aktebank,

bedoeld in artikel 18 van de wet van 25 ventôse jaar XI op het

notarisambt, door die Notariële Aktebank;

2° voor de andere akten, door de Koninklijke Federatie van het

Belgisch Notariaat of haar gedelegeerde, op elektronische wijze, voor

rekening van de notaris.

De bewaring moet de onveranderlijkheid en de integriteit van de

inhoud van deze stukken waarborgen.

###### Art. 180. ter

(ingevoegd bij art. 114 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).

Tekst van toepassing vanaf 17.08.2020 (art. -))

De griffier bewaart, samen met de minuut van het vonnis of arrest:  Le greffier conserve, avec la minute du jugement ou de l'arrêt :

1° de vermelding van de registratie van dat vonnis of arrest;  1° la relation de l'enregistrement de ce jugement ou de cet arrêt ;

2° een kopie van het geregistreerde afschrift van dat vonnis of arrest.  2° une copie de la copie enregistrée de ce jugement ou de cet arrêt.

#### Afdeling IV - Verplichting van inzageverlening

###### Art. 181. 1

(gewijzigd bij art. 55 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

Notarissen,  gerechtsdeurwaarders,  bestuursoverheden  en

ambtenaren van de Staat, provincies, gemeenten en openbare

instellingen zijn ertoe gehouden, op verbeurte van een boete van 25

EUR per overtreding, op elk verzoek van de ambtenaren van de

Algemene Administratie van de Patrimoniumdocumentatie, van hun

repertoriums en de akten waarvan zij bewaarders zijn, evenals van de

uitgiften en relazen bedoeld in artikel 180 bis , zonder verplaatsing

inzage te verlenen en deze ambtenaren de inlichtingen, af schriften en

Deze verplichting is echter, bij 't leven van de erflaters, niet

toepasselijk op de bij notarissen berustende testamenten.

###### Art. 181. 2

(gewijzigd bij art. 115 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).

Tekst van toepassing vanaf 17.08.2020 (art. -))

De griffiers van de hoven en rechtbanken zijn er toe gehouden op straf

van een boete van vijfentwintig euro per overtreding, aan de

ambtenaren  van  de  Algemene  Administratie  van  de

Patrimoniumdocumentatie inzage te verlenen van:

1° de door hen of vóór hen verleden akten;  1° les actes passés par eux ou devant eux ;

2° de minuten van de vonnissen, arresten, bevelschriften en alle

andere akten waarvan zij bewaarders zijn;

3° de afschriften en vermeldingen bedoeld in artikel 180 ter .

De modaliteiten waaronder deze inzage moet verleend worden en de

termijn waarbinnen dit moet geschieden, worden bij koninklijk besluit

bepaald. Inbreuken op de voorschriften van dit koninklijk besluit

kunnen beteugeld worden met boeten waarvan het bedrag 25 EUR

per inbreuk niet zal te boven gaan.

###### Artikel 182

(gewijzigd bij art. 57 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

De personen die de in artikel 63 1 bedoelde beroepsaangifte

ondertekenen zijn ertoe gehouden van hun registers, repertoria,

boeken, akten en alle andere bescheiden betreffende hun handels-,

beroeps- of statutaire bedrijvigheid, bij iedere vordering van de

ambtenaren  van  de  Algemene  Administratie  van  de

Patrimoniumdocumentatie, zonder verplaatsing inzage te verlenen,

ten einde bedoelde ambtenaren te laten nagaan of de door hen of

door derden verschuldigde registratierechten wel richting werden

geheven.

Elke weigering van inzageverlening wordt bij proces-verbaal

vastgesteld en gestraft met een geldboete van 250 tot 2.500 EUR,

###### Art. 182. bis

(gewijzigd bij art. 66 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van

toepassing vanaf 16.05.2014 (art. 99))

De personen die de toepassing van artikel 140 bis vragen, zijn er toe

gehouden, zonder verplaatsing, van alle boeken en bescheiden

betreffende hun activiteit bij iedere vordering van de ambtenaren van

de Algemene Administratie van de Patrimoniumdocumentatie inzage

te verlenen teneinde bedoelde ambtenaren toe te laten zich te

vergewissen van de juiste heffing van de door de verzoekers of

derden verschuldigde rechten.

Elke weigering van inzageverlening wordt bij proces-verbaal

vastgesteld en wordt gestraft met een geldboete van 1.250 EUR.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 183

(gewijzigd bij art. 67 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Openbare instellingen, stichtingen van openbaar nut en private

stichtingen, alle verenigingen en vennootschappen die in België hun

hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben,

bankiers,  wisselagenten  en  wisselagentcorrespondenten,

zaakwaarnemers en aannemers, openbare of ministeriële officieren

zijn ertoe gehouden aan de ambtenaren van de Algemene

Administratie  van  de  Patrimoniumdocumentatie,  met

desvoorkomend inzageverlening van de stukken tot staving, al de

inlichtingen te verstrekken welke deze nodig achten om de correcte

heffing van de te hunnen laste of ten laste van derden invorderbare

rechten te verzekeren.

Deze inlichtingen kunnen slechts gevraagd worden krachtens

bijzondere machtiging van de administrateur-generaal van de

Algemene  Administratie  van  de  Patrimoniumdocumentatie,

houdende nauwkeurige aanduiding van het rechtsfeit omtrent

hetwelk navorsing dient gedaan.

door de ambtenaar aangewezen in de machtiging bedoeld in het

tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500

EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de

Algemene Administratie van de Patrimoniumdocumentatie wordt

vastgesteld.

-----

###### Artikel 183

(gewijzigd bij art. 58 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

Openbare instellingen, stichtingen van openbaar nut en private

stichtingen, alle verenigingen en vennootschappen die in België hun

hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben,

bankiers,  wisselagenten  en  wisselagentcorrespondenten,

zaakwaarnemers en aannemers, openbare of ministeriële officieren

zijn ertoe gehouden aan de ambtenaren van de Algemene

Administratie  van  de  Patrimoniumdocumentatie,  met

desvoorkomend inzageverlening van de stukken tot staving, al de

inlichtingen te verstrekken welke deze van node achten om de

richtige heffing van de te hunnen laste of ten laste van derden

invorderbare rechten te verzekeren.

Deze inlichtingen kunnen slechts gevraagd worden krachtens

bijzondere machtiging van den administrateur-generaal van de

Algemene  Administratie  van  de  Patrimoniumdocumentatie,

houdende nauwkeurige aanduiding van het rechtsfeit omtrent

hetwelk navorsing dient gedaan.

De inlichtingen moeten worden verschaft binnen drie maanden na de

datum waarop ze werden gevraagd. Die termijn kan worden verlengd

door de ambtenaar aangewezen in de machtiging bedoeld in het

tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500

EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de

Algemene Administratie van de Patrimoniumdocumentatie wordt

vastgesteld.

----------

Note :

(1) Lire : « de l’ ».

###### Artikel 184

(lid 2, vervangen bij art. 68 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Wanneer de som te betalen door de eigenaar van een muur om deze

gemeen te maken, door tussenkomst van een deskundige,

bouwkundige, aannemer, landmeter of landmeetkundige werd

bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25

EUR, de bevoegde ambtenaar van de Algemene Administratie van de

Patrimoniumdocumentatie daarvan bericht te geven binnen de drie

maanden na de voltooiing van zijn werk.

De Koning bepaalt de modaliteiten van deze communicatie en duidt

de ambtenaar aan ertoe bevoegd hetzelve te ontvangen.

-----

###### Artikel 184

(gewijzigd bij art. 68 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van

toepassing vanaf 16.05.2014 (art. 99))

Wanneer de som te betalen door de eigenaar van een muur om deze

gemeen te maken, door tussenkomst van een deskundige,

bouwkundige, aannemer, landmeter of landmeetkundige werd

bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25

EUR, de bevoegde ambtenaar van de Algemene Administratie van de

Patrimoniumdocumentatie daarvan bericht te geven binnen de drie

maanden na de voltooiing van zijn werk.

Een koninklijk besluit bepaalt de wijze waarop dit bericht dient

gegeven en duidt de ambtenaar aan ertoe bevoegd hetzelve te

ontvangen.

#### Afdeling V - Verplichtingen opgelegd aan openbare

ambtenaren ter verzekering van de invordering der

registratierechten

###### Art. 184. bis

De notarissen, gerechtsdeurwaarders en griffiers, de vereffenaars en

curatoren alsook de ambtenaren van de Deposito- en Consignatiekas

mogen slechts de betaling, overschrijving of teruggave van sommen

of waarden die voortkomen van een veroordeling, van een

vereffening of van een rangregeling, verrichten na de aflevering, door

de ontvanger, van een getuigschrift houdende verklaring dat geen

enkele som eisbaar blijft als registratierecht of als boete uit hoofde

van die veroordeling, vereffening of rangregeling.

Het eerste lid is slechts van toepassing op de vereffenaars en de

curators in het geval dat de veroordeling, de vereffening of

rangregeling die de betaling, overschrijving, of teruggave tot gevolg

heeft, hen ter kennis wordt gebracht.

Indien de personen bepaald in het eerste lid de voorschriften van dit

artikel niet zijn nagekomen, zijn zij persoonlijk aansprakelijk voor de

betaling van de sommen die opeisbaar blijven.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Artikel 185

(lid 2, vervangen bij art. 69 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze

### titel, wordt het bestuur er toe gemachtigd volgens de regelen en door

alle middelen van gemeen recht, met inbegrip van getuigen en

vermoedens, maar met uitzondering van de eed, en, bovendien door

de processen-verbaal van zijn ambtenaren, elke overtreding van de

beschikkingen van deze titel vast te stellen en om het even welk feit

te bewijzen dat de opvorderbaarheid van een recht of een boete laat

blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.

een aangetekende zending.

-----

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Artikel 185

(gewijzigd bij art. 59 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze

### titel, wordt het bestuur er toe gemachtigd volgens de regelen en door

alle middelen van gemeen recht, met inbegrip van getuigen en

vermoedens, maar met uitzondering van de eed, en, bovendien door

de processen-verbaal van zijn ambtenaren, elke overtreding van de

beschikkingen van deze titel vast te stellen en om het even welk feit

te bewijzen dat de opvorderbaarheid van een recht of een boete laat

blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.

De processen-verbaal gelden als bewijs tot het tegendeel bewezen is.

Zij zullen aan belanghebbenden betekend worden binnen de maand

van de vaststelling van de overtreding. Deze betekening mag

gebeuren bij een ter post aangetekend schrijven. De afgifte van het

stuk ter post geldt als betekening van de volgende dag af.

###### Artikel 186

(opnieuw opgeheven bij art. 11 van de wet van 13.08.1947 (B.S., 17.09.1947).

Tekst van toepassing vanaf 27.09.1947 (art. -))

(…)

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 187

overeenkomst, wordt, ter vordering van het recht tegen de nieuwe

eigenaar of vruchtgebruiker, in voldoende mate bewezen door daden

van beschikking of van bestuur of door andere handelingen of akten

waarbij, in zijnen hoofde, de eigendom of het vruchtgebruik

vastgesteld of ondersteld wordt.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 188

Wordt als koper voor eigen rekening beschouwd en mag zich op de

hoedanigheid van lasthebber of van commissionair van de verkoper

niet beroepen, ieder persoon die de verkoop van een onroerend goed

bewerkt, wanneer vaststaat dat hij, reeds vóór het tot stand brengen

van deze verkoop, aan de eigenaar den prijs of elke van den verkoop

voort te komen som betaald heeft of er zich toe verbonden heeft te

betalen.

De tussenpersoon wordt geacht het onroerend goed te hebben

verkregen op de dag van de betaling of van de verbintenis tot betaling.

#### Afdeling II - Controleschatting

###### Artikel 189

(gewijzigd bij art. 94 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Onverminderd de toepassing van de bepalingen betreffende het

bewimpelen van prijs, heeft de ontvanger de bevoegdheid om

schatting te vorderen van de goederen die het voorwerp van de

overeenkomst uitmaken, ten einde van de ontoereikendheid van de

uitgedrukte prijs of van de aangegeven waarde te doen blijken,

wanneer het gaat om eigendom of vruchtgebruik van in België

gelegen onroerende goederen.

###### Artikel 190

De schatting dient gevorderd bij een aanvraag genotificeerd door den

ontvanger aan de verkrijgende partij binnen twee jaar te rekenen van

de dag van de registratie van de akte of verklaring.

In de gevallen bedoeld in artikelen 16 en 17 gaat de termijn slechts in

den dag der registratie van de in artikel 31, 2°, voorziene verklaring.

De vordering tot schatting houdt aanwijzing van de goederen

waarover de schatting gaat, zomede van de som waarop zij door het

bestuur geschat werden en van het vermoedelijk wegens recht en

boete verschuldigd bedrag.

###### Artikel 191

Binnen vijftien dagen na de in artikel 190 voorziene notificatie, kunnen

ontvanger en partij overeenkomen dat de waardering door één of

door drie door hen gekozen deskundigen zal worden gedaan.

In dit geval wordt het akkoord vastgesteld bij een proces-verbaal dat

het voorwerp der schatting vermeldt en den of de verkozen

deskundigen aanwijst.

Dit proces-verbaal is gedagtekend; het wordt door de ontvanger en

door de partij ondertekend; indien de partij niet mag of niet kan

ondertekenen, dient dit in het proces-verbaal vermeld.

###### Artikel 192

Bij gemis van het onder artikel 191 voorzien akkoord richt de

ontvanger, aan den vrederechter in wiens ambtsgebied de

onroerende goederen gelegen zijn, een verzoekschrift waarin de

feiten worden uiteengezet en dat de vordering tot schatting inhoudt.

Wanneer de onroerende goederen in het ambtsgebied van

verschillende vredegerechten gelegen zijn, is de bevoegde rechter hij

in wiens ambtsgebied zich het gedeelte der goederen bevindt met het

grootste kadastraal inkomen.

Het verzoekschrift wordt aan de partij betekend.  La requête est signifiée à la partie.

De rechter beslist binnen vijftien dagen na het verzoek; hij beveelt de

schatting en stelt, naar vereiste van omstandigheden, een of drie

deskundigen aan.

(gewijzigd bij art. 69 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van

toepassing vanaf 16.05.2014 (art. 99))

Kunnen niet tot deskundigen gekozen of benoemd worden:  Ne peuvent être choisis ou nommés comme experts :

1° ambtenaren van de Algemene Administratie van  de

Patrimoniumdocumentatie;

2° openbare of ministeriële officieren opstellers van de akten of

verklaringen;

3° beambten van bedoelde ambtenaren en openbare of ministeriële

officieren.

###### Artikel 194

(gewijzigd bij art. 3/art. 119 van de wet van 10.10.1967 (B.S., 31.10.1967).

Tekst van toepassing vanaf 01.01.1969 (art. 1, KB 04.11.1968 (B.S.,

13.11.1968)))

Het vonnis waarbij de schatting wordt bevolen, wordt ten verzoeke

van de ontvanger aan de partij betekend.

De ontvanger of de partij, indien zij gegronde redenen hebben om de

bevoegdheid, onafhankelijkheid of onpartijdigheid van de benoemde

deskundigen in twijfel te trekken, mogen, binnen acht dagen na

bedoelde betekening, deszelfs of derzelver wraking bij de rechter

vorderen. Deze wraking mag altijd worden gevorderd in de gevallen

beoogd door artikel 966 van het Gerechtelijk Wetboek.

De vordering tot wraking geschiedt per rekest waarin de oorzaken der

wraking nader worden bepaald. De rechter beslist na de

belanghebbenden te hebben gehoord. Bij hetzelfde vonnis vervangt

hij de gewraakte deskundigen.

Deze nieuwe beslissing wordt aan de partij betekend.  Cette nouvelle décision est signifiée à la partie.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 195

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De ontvanger notificeert aan de deskundigen de opdracht die hun

toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de

deskundigen, zowel aan de ontvanger als aan de partij, een

briefwisseling waarbij zij hen verwittigen van dag en uur waarop zij de

nodig geachte bezoeken ter plaatse zullen doen en hen in hun

gezegden en opmerkingen zullen aanhoren.

Ieder aan de deskundigen door een der partijen ter inzage verleend

bescheid moet tezelfdertijd in afschrift aan de andere partij bij

aangetekende zending worden gezonden.

-----

###### Artikel 195

De ontvanger notificeert aan de deskundigen de opdracht die hun

toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de

deskundigen, zowel aan de ontvanger als aan de partij, een schrijven

waarbij zij hen verwittigen van dag en uur waarop zij de nodig geachte

bezoeken ter plaatse zullen doen en hen in hun gezegden en

opmerkingen zullen aanhoren.

Ieder aan de deskundigen door een der partijen ter inzage verleend

bescheid moet tezelfdertijd in afschrift aan de andere partij bij

aangetekende brief worden gezonden.

###### Artikel 196

(lid 3 vervangen bij art. 7 van de wet van 27.05.1974 (B.S., 06.07.1974) err. (B.S.

12.07.1974 en 21.12.1974). Tekst van toepassing vanaf 16.07.1973 (art. -))

De deskundige of, desvoorkomend, de drie gezamenlijke optredende

deskundigen vorsen den staat en de verkoopwaarde der in de

vordering tot schatting aangewezen goederen, op het er vermeld

tijdstip.

wijze en met bewijsgronden tot staving, zonder enige beperking noch

voorbehoud, hun advies over bedoelde waarde uitbrengen.

De handtekening van de deskundige wordt voorafgaan door de eed:  La signature des experts est précédée du serment :

"Ik zweer dat ik in eer en geweten, nauwgezet en eerlijk mijn opdracht

heb vervuld".

of:  ou :

"Je jure que j'ai rempli ma mission en honneur et conscience, avec

exactitude et probité".

of:  ou :

"Ich schwöre, dass ich den mir erteilten Auftrag auf Ehre und

Gewissen, genau und ehrlich erfüllt habe".

De minuut van het verslag wordt ter griffie van het onder artikel 192

aangeduid vredegerecht neergelegd.

###### Artikel 197

Het verslag wordt door de meest gerede partij gelicht en aan de

andere partij betekend.

Naar de door de deskundigen gegeven waardering en, in geval van

niet-overeenstemming, naar de waardering van de meerderheid of,

bij gemis van meerderheid, naar de tussenwaardering, wordt de

verkoopwaarde van het goed ten opzichte van de heffing der

belasting bepaald.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Artikel 198

(vervangen bij art. 71 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

-----

###### Artikel 198

De krachtens vorenstaande artikelen van deze afdeling te verrichten

betekeningen en notificaties mogen bij aangetekend schrijven

geschieden. De afgifte van het stuk ter post geldt als notificatie vanaf

de daaropvolgende dag.

###### Artikel 199

(vervangen bij art. 33 door de programmawet van 09.07.2004 (B.S.,

15.07.2004 - ed. 2). Tekst van toepassing vanaf 25.07.2004 (art. -))

Zowel de ontvanger als de partij kunnen de schatting betwisten door

inleiding van een rechtsvordering. Deze rechtsvordering dient ingeleid

te worden, op straffe van verval, binnen de termijn van één maand te

rekenen van de betekening van het verslag.

###### Artikel 200

(gewijzigd bij art. 181 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Indien de opgegeven prijs of de aangegeven waarde lager is dan de

door de schatting opgeleverde begroting, moet de verkrijger het

bijkomend recht betalen, met de moratoire intresten naar de in

burgerlijke zaken vastgestelde voet, te rekenen van de bij artikel 100

voorziene notificatie en, desvoorkomend, met de bij artikel 201

opgelegde boete.

Hem worden desvoorkomend ook de kosten van de procedure

opgelegd, indien het vastgestelde tekort het achtste van de

uitgedrukte prijs of van de aangegeven waarde bereikt of overtreft.

Deze kosten blijven evenwel ten laste van 's Rijks Schatkist zo de

belanghebbende, vóór de in artikel 190 voorziene notificatie, heeft

aangeboden het bijkomend recht, verhoogd met de boete bepaald in

###### Art. 201. te betalen, op een som welke het bij de schatting

uitgewezen tekort bereikt of overtreft.

### HOOFDSTUK XI - Tekort in de waardering, bewimpeling

##### en veinzing. Sanctiën

###### Artikel 201

(gewijzigd bij art. 182 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Wanneer bevonden wordt dat de opgegeven prijs of de aangegeven

waarde van aan de onder artikel 189 voorziene schatting

onderworpen goederen te laag is, en dat het vastgestelde tekort gelijk

is aan of hoger dan het achtste van de opgegeven prijs of van de

aangegeven waarde, verbeurt de verkrijgende partij een geldboete

ten bedrage van het ontdoken recht.

###### Artikel 202

(gewijzigd bij art. 15 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van

toepassing vanaf 17.01.1959 (art. -))

Wanneer er geen aanleiding tot schatting bestaat en een waardering,

gedaan om de vereffening van de rechten mogelijk te maken,

ontoereikend wordt erkend, is het ontdoken recht ondeelbaar

verschuldigd door hen die de waardering hebben gedaan; zij zijn

daarenboven ondeelbaar een boete verschuldigd gelijk aan het

aanvullend recht, zoo het tekort gelijk is aan of hoger is dan het

achtste van bewuste waardering.

Alle andere onjuistheid, bevonden in de elementen van een verklaring

in of onderaan de akte gesteld tot vereffening van de belasting, wordt

gestraft met een boete gelijk aan het ontdoken recht, benevens

betaling van dat recht, het al ondeelbaar ten laste van hen die de

verklaring gedaan hebben.

###### Artikel 203

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

waarde, is elke der contracterende partijen een boete verschuldigd

gelijk aan het ontdoken recht. Dit recht ondeelbaar door alle partijen

verschuldigd.

Het aanvullend recht dat ingevolge een bij schatting vastgesteld

tekort of anderszins betaald geworden is, wordt aangerekend op het

aanvullend recht, vereffend uit hoofde van de bewimpeling waarvan

sprake in vorenstaande alinea.

In alle gevallen waarin de heffing op den prijs en de lasten op de

overeengekomen waarde geschiedt, moet de werkende notaris den

verschijnende partijen de eerste alinea van dit artikel voorlezen.

Op straf van een boete van 25 EUR moet uitdrukkelijke melding van

die voorlezing in de akte gemaakt worden.

###### Artikel 204

(gewijzigd bij art. 18 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van

toepassing vanaf 04.05.1965 (art. -))

Wanneer de in een akte vastgestelde overeenkomst niet die is welke

door de partijen werd gesloten, of wanneer de akte betreffende een

in artikel 19, 2° of 5°, bedoelde overeenkomst onvolledig of onjuist

is, met dien verstande dat ze al de bestanddelen van de

overeenkomst niet doet kennen, is elke der contracterende partijen

een geldboete verschuldigd gelijk aan het ontdoken recht. Dit recht is

ondeelbaar door alle partijen verschuldigd.

###### Artikel 205

(opgeheven bij art. 64 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst

van toepassing vanaf 06.04.1999 (art. -))

(…)

### HOOFDSTUK XII - Correctionele straffen

###### Artikel 206

Onverminderd de fiscale boeten, wordt hij die met bedrieglijk opzet of

met het oogmerk om te schaden, de bepalingen van dit Wetboek of

de ter uitvoering ervan genomen besluiten overtreedt, gestraft met

gevangenisstraf van acht dagen tot twee jaar en met geldboete van

250 EUR tot 12.500 EUR of met één van die straffen alleen.

Wanneer de overtreding werd begaan in het kader van een

registratierecht dat geen gewestelijke belasting is volgens het

bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van

16 januari 1989 betreffende de financiering van de gemeenschappen

en de gewesten, wordt het bedrag van het in het eerste lid bepaalde

maximum van de boete gebracht op 500.000 euro.

###### Art. 206. bis

(gewijzigd bij art. 23 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van

toepassing vanaf 01.11.2012 (art. -))

Met gevangenisstraf van een maand tot vijf jaar en met geldboete van

250 tot 12.500 EUR of met één van die straffen alleen frank wordt

gestraft, hij die, met het oogmerk om een van de in artikel 206

bedoelde misdrijven te plegen, in openbare geschriften, in

handelsgeschriften of in private geschriften valsheid pleegt, of die van

een zodanig vals geschrift gebruik maakt.

Hij die wetens en willens een vals getuigschrift opstelt dat de

belangen van de Schatkist kan schaden of die van een dergelijk

getuigschrift gebruik maakt, wordt gestraft met gevangenisstraf van

acht dagen tot twee jaar en met geldboete van 250 tot 12.500 EUR.

of met één van die straffen alleen.

Wanneer het misdrijf werd begaan in het kader van een

registratierecht dat geen gewestelijke belasting is volgens het

bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van

16 januari 1989 betreffende de financiering van de gemeenschappen

en de gewesten, wordt het bedrag van het in het eerste en het tweede

lid bepaalde maximum van de boete gebracht op 500.000 euro.

###### Art. 206. bis /1

(ingevoegd bij art. 109 van de wet van 05.05.2019 (B.S., 24.05.2019 - ed. 1).

Tekst van toepassing op de datum bepaald door de Koning en ten laatste op

01.01.2020 (art. 200))

registratierecht dat geen gewestelijke belasting is volgens het

bepaalde in artikel 3, eerste lid, 6° tot 8° van de bijzondere wet van

16 januari 1989 betreffende de financiering van de gemeenschappen

en de gewesten en teneinde te vermijden dat een veroordeelde aan

een onredelijk zware straf zou worden onderworpen, houdt de

rechter bij de straftoemeting rekening met de verschuldigde fiscale

boeten.

Artikel 42, 3°, van het Strafwetboek vindt geen toepassing op de

vermogensvoordelen die rechtstreeks uit de fiscale misdrijven zijn

verkregen, op de goederen en waarden die in de plaats ervan zijn

gesteld en op de inkomsten uit de belegde voordelen in geval de

vordering van de fiscale administratie gegrond wordt verklaard en tot

een effectieve betaling van deze volledige vordering heeft geleid.

###### Artikel 207

(vervangen bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van

toepassing vanaf 14.02.1981 (art. 22))

§ 1. Wanneer de beoefenaar van een van de volgende beroepen:  § 1 er . En condamnant le titulaire d’une des professions suivantes :

1° belastingadviseur;  1° conseiller fiscal ;

2° zaakbezorger;  2° agent d’affaires ;

3° deskundige in belastingzaken of in boekhouden;  3° expert en matière fiscale ou comptable ;

4° of enig ander beroep dat tot doel heeft voor een of meer

belastingplichtigen boek te houden of te helpen houden, ofwel voor

eigen rekening ofwel als hoofd, lid of bediende van enigerlei

vennootschap, vereniging, groepering of onderneming;

5° of, meer in het algemeen, het beroep dat erin bestaat een of meer

belastingsplichtigen raad te geven of bij te staan bij het vervullen van

de verplichtingen opgelegd bij dit Wetboek of bij de ter uitvoering

ervan vastgestelde besluiten, wordt veroordeeld wegens een van de

misdrijven bedoeld in de artikelen 206 en 206 bis , kan het vonnis hem

verbod opleggen om gedurende drie maanden tot vijf jaar,

rechtstreeks of onrechtstreeks, de hiervoren bedoelde beroepen op

welke wijze ook uit te oefenen.

De rechter kan bovendien, mits hij zijn beslissing op dat stuk

motiveert, voor een duur van drie maanden tot vijf jaar de sluiting

§ 2. Het verbod en de sluiting bedoeld in § 1 treden in werking vanaf

de dag waarop de veroordeling in kracht van gewijsde is gegaan.

###### Art. 207. bis

(gewijzigd bij art. 24 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van

toepassing vanaf 01.11.2012 (art. -))

Hij die, rechtstreeks of onrechtstreeks, het verbod of de sluiting

uitgesproken krachtens artikel 207 overtreedt, wordt gestraft met

gevangenisstraf van acht dagen tot twee jaar en geldboete van 250

EUR tot 12.500 EUR of met één van die straffen alleen.

Wanneer het verbod werd opgelegd in het kader van een

registratierecht dat geen gewestelijke belasting is volgens het

bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van

16 januari 1989 betreffende de financiering van de gemeenschappen

en de gewesten, wordt het bedrag van het in het eerste lid bepaalde

maximum van de boete gebracht op 500.000 euro.

###### Art. 207. ter

(gewijzigd bij art. 25 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van

toepassing vanaf 01.11.2012 (art. -))

§ 1. Alle bepalingen van het Eerste Boek van het Strafwetboek, met

inbegrip van artikel 85, zijn van toepassing op de misdrijven bedoeld

in de artikelen 206, 206 bis en 207 bis .

§ 2. (…)

§ 3. De wet van 5 maart 1952, gewijzigd bij de wetten van 22

december 1969 en 25 juni 1975, betreffende de opdecimes op de

strafrechtelijke geldboeten, is van toepassing op de misdrijven

bedoeld in artikel 206, 206 bis en 207 bis .

###### Art. 207. quater

(lid 2, 2°, gewijzigd bij art. 51 van de wet van 09.04.2024 (B.S., 18.04.2024).

Tekst van toepassing vanaf 28.04.2024 (art. -))

gehouden tot betaling van de ontdoken belasting en de interesten

verschuldigd door de oorspronkelijke belastingschuldige.

De personen beschuldigd als daders of als medeplichtigen van

misdrijven bedoeld in de artikelen 206 en 206 bis zijn eveneens

gehouden tot betaling van de ontdoken rechten en de interesten zoals

bedoeld in het eerste lid, wanneer de bestanddelen van de misdrijven

bewezen verklaard zijn, wanneer ze genieten van:

1° een opschorting van de uitspraak van de veroordeling of een uitstel

van de tenuitvoerlegging van de straffen voorzien in de wet van 29

juni 1964 betreffende de opschorting, het uitstel en de probatie;

2° een veroordeling bij eenvoudige schuldigverklaring voorzien in

###### Art. 27. van de Voorafgaande titel van het Wetboek van

Strafvordering;

3° de procedure van voorafgaande erkenning van schuld bedoeld in

###### Art. 216

van het Wetboek van Strafvordering;

4° de verjaring van de strafvordering.  4° de la prescription de l'action publique.

De natuurlijke personen of de rechtspersonen zijn burgerlijk en

hoofdelijk aansprakelijk voor de geldboeten en kosten die het gevolg

zijn van de veroordelingen welke krachtens de artikelen 206 tot

207 bis tegen hun aangestelden of hun bestuurders, zaakvoerders of

vereffenaars, in het kader van de uitoefening van hun functie, in

rechte of in feite zijn uitgesproken.

###### Art. 207. quinquies

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van

toepassing vanaf 14.02.1981 (art. 22))

De rechter kan bevelen dat ieder vonnis of arrest houdende

veroordeling tot een gevangenisstraf, uitgesproken krachtens de

artikelen 206, 206 bis en 207 bis , wordt aangeplakt in de plaatsen die

hij bepaalt en eventueel bij uittreksel, wordt bekendgemaakt op de

wijze die hij bepaalt, een en ander op kosten van de veroordeelde.

Hetzelfde kan gelden voor iedere krachtens artikel 207 uitgesproken

beslissing  tot  verbod  van  het  uitoefenen  van  een

beroepswerkzaamheid in België of tot sluiting van de in het land

geëxploiteerde inrichtingen.

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van

toepassing vanaf 14.02.1981 (art. 22))

De schending van het bij artikel 236 bis bepaalde beroepsgeheim

wordt gestraft overeenkomstig de artikelen 66, 67 en 458 van het

Strafwetboek.

###### Art. 207. septies

(gewijzigd bij art. 110 van de wet van 05.05.2019 (B.S., 24.05.2019 - ed. 1).

Tekst van toepassing op de datum bepaald door de Koning en ten laatste op

01.01.2020 (art. 200))

§ 1 . De strafvordering wordt uitgeoefend door het openbaar

ministerie.

§ 2 . Het openbaar ministerie kan geen vervolging instellen indien het

kennis heeft gekregen van de feiten ten gevolge van een klacht of een

aangifte van een ambtenaar die niet de machtiging had waarvan

sprake is in artikel 29, § 2, van het Wetboek van strafvordering.

Het openbaar ministerie beslist om al dan niet de strafvervolging in te

stellen van de feiten waarvan het kennis heeft genomen gedurende

het overleg bedoeld in artikel 29, § 3, tweede lid, van het Wetboek van

strafvordering binnen de 3 maanden na de initiële aangifte bedoeld in

artikel 29, § 3, eerste lid, van hetzelfde Wetboek.

§ 3 . Onverminderd het in artikel 29, § 3, tweede lid, van het Wetboek

van strafvordering bedoelde overleg, kan de procureur des Konings,

indien hij een vervolging instelt wegens feiten die strafrechtelijk

strafbaar zijn ingevolge de bepalingen van dit Wetboek of van de ter

uitvoering ervan genomen besluiten, het advies vragen van de

bevoegde adviseur-generaal. De procureur des Konings voegt het

feitenmateriaal waarover hij beschikt bij zijn verzoek om advies. De

adviseur-generaal antwoordt op dit verzoek binnen vier maanden na

de ontvangst ervan.

In geen geval schorst het verzoek om advies de strafvordering.  En aucun cas, la demande d'avis n'est suspensive de l'action publique.

###### Art. 207. octies

(gewijzigd bij art. 70 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van

toepassing vanaf 16.05.2014 (art. 99))

Patrimoniumdocumentatie en de Algemene Administratie van de

Bijzondere Belastinginspectie mogen, op straffe van nietigheid van de

akte van rechtspleging, slechts als getuige worden gehoord.

Het eerste lid is niet van toepassing op de krachtens artikel 71 van de

wet van 28 december 1992 bij het parket gedetacheerde ambtenaren

van die administraties.

Het eerste lid is evenmin van toepassing op de ambtenaren van die

administraties die, krachtens artikel 31 van de wet van 30 maart

1994 tot uitvoering van het globaal plan op het stuk van de fiscaliteit,

ter beschikking zijn gesteld van de federale politie.

Het eerste lid is niet van toepassing op de ambtenaren die deelnemen

aan het in artikel 29, derde lid van het Wetboek van strafvordering

bedoelde overleg.

### HOOFDSTUK XIII - Teruggaaf

###### Artikel 208

De regelmatig geheven rechten kunnen niet worden teruggegeven,

welke ook de latere gebeurtenissen zijn, behoudens in de bij deze titel

voorziene gevallen.

###### Artikel 209

(gewijzigd bij art. 96 van de wet van 17.03.2019 (B.S., 10.05.2019). Tekst van

toepassing vanaf 01.05.2019 (art. 119, § 1)) (1)

Zijn vatbaar voor teruggaaf:  Sont sujets à restitution :

1° De rechten, geheven omdat de partijen in gebreke gebleven zijn in

de akte of verklaring te vermelden:

a) dat de overeenkomst reeds belast werd;  a) que la convention avait déjà subi l’impôt ;

b) dat de voorwaarden tot bekomen van vrijstelling of vermindering

vervuld zijn, tenzij het bestaan van deze vermelding bij de wet als een

uitdrukkelijke voorwaarde ter verkrijging van de fiscale gunst is

gesteld;

gegaan vonnis of arrest.

3° het evenredig recht geheven wegens een overeenkomst waarvan

een in kracht van gewijsde gegaan vonnis of arrest in ontbinding of de

herroeping uitspreekt, mits uit de beslissing blijkt dat ten hoogste één

jaar na de overeenkomst een eis tot ontbinding of herroeping, zelfs bij

een onbevoegd rechter, is ingesteld.

4° de evenredige rechten geheven op een door een rechtspersoon

gestelde rechtshandeling die door de hogere overheid nietig verklaard

werd.

5° de bij toepassing van de artikelen 115, 115 bis , 116 en 120 aan het

tarief van 0,5% geheven rechten naar aanleiding van een

vermeerdering van het kapitaal of het eigen vermogen, met nieuwe

inbreng, door een vennootschap bedoeld in artikel 201, eerste lid, 1°,

van het Wetboek van de inkomstenbelastingen 1992, mits die

vermeerdering van het kapitaal of het eigen vermogen is geschied

binnen het jaar vóór de datum van de toelating tot de notering op een

Belgische effectenbeurs van aandelen of met aandelen gelijk te

stellen waardepapieren van de vennootschap.

De teruggaaf geschiedt desvoorkomend onder aftrekking van het

algemeen vast recht.

----------

Nota (1) – Overgangsbepalingen:

Zolang het Wetboek van vennootschappen en verenigingen, overeenkomstig

#### hoofdstuk IV, afdeling II, van de wet van 23 maart 2019, niet van toepassing

is op een vennootschap, vereniging of stichting, moet elke verwijzing naar een

bepaling van het Wetboek van vennootschappen en verenigingen die

voorkomt in een bepaling van het Wetboek van de inkomstenbelastingen

1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het

Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het

Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering

ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze

belastingen, worden gelezen, voor wat deze vennootschap, vereniging of

stichting betreft, als een verwijzing naar de bepaling van het Wetboek van

vennootschappen of andere bijzondere wetgeving die in zulke fiscale

wetgeving voorkwam voor de inwerkingtreding van deze wet (art. 119, § 2);

Zolang, overeenkomstig hoofdstuk IV, afdeling II van de wet van 23 maart

2019, een vennootschap, vereniging of stichting, die door het Belgisch recht

wordt beheerst, een rechtsvorm heeft die het Wetboek van vennootschappen

en verenigingen niet erkent, worden de bepalingen van het Wetboek van de

inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en

Griffierechten, het Wetboek van Successierechten, het Wetboek diverse

rechten en taksen en het Wetboek van de Belasting over de Toegevoegde

vermelden voor wat deze vennootschap, vereniging of stichting betreft, zoals

voor de inwerkingtreding van deze wet. (art. 119, § 3).

###### Artikel 210

(gewijzigd bij art. 26 van de wet van 28.04.2019 (B.S., 06.05.2019). Tekst van

toepassing vanaf 16.05.2019 (art. -))

In geval van gehele of gedeeltelijke vernietiging van een vonnis of

arrest door een andere in kracht van gewijsde gegane rechterlijke

beslissing zijn de op de vernietigde beslissing geheven evenredige

rechten voor gehele of gedeeltelijke teruggaaf vatbaar.

Het op een voorwaardelijke veroordeling geheven evenredig recht

wordt teruggegeven in de mate dat er wordt aangetoond door alle

middelen van gemeen recht, met inbegrip van getuigen en

vermoedens, met uitzondering van de eed, dat de voorwaarde niet in

vervulling is gegaan en het niet in vervulling gaan van de voorwaarde

leidt tot een resultaat dat gelijk is aan het afwijzen van de vordering.

Het recht wordt volledig teruggegeven indien het samengevoegd

bedrag van de veroordelingen, vereffeningen of rangregelingen,

waarop de heffing werd gedaan, herleid wordt tot een som die bij

artikel 143, laatste lid, vastgestelde bedrag niet overschrijdt.

###### Artikel 211

(opgeheven bij art. 23 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

(…)

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 212

(lid 5, gewijzigd bij art. 25 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

de wederverkoper teruggegeven indien de wederverkoop bij

authentieke akte vastgesteld is binnen twee jaar na de datum van de

authentieke akte van verkrijging.

Wanneer de verkrijging of de wederverkoop heeft plaatsgehad onder

een opschortende voorwaarde, wordt de termijn van wederverkoop

berekend op basis van de datum waarop deze voorwaarde is vervuld.

Niet teruggegeven wordt het recht dat betrekking heeft op het

gedeelte van de prijs en de lasten van de verkrijging, dat hoger is dan

het bedrag dat tot grondslag heeft gediend voor de heffing van de

belasting op de akte van wederverkoop.

In geval van gedeeltelijke wederverkoop wordt in het verzoek tot

teruggave het deel van de aanschaffingsprijs dat betrekking heeft op

het wederverkochte gedeelte nader aangegeven onder controle van

het bestuur.

Een door de wederverkoper en de instrumenterende notaris

ondertekend verzoek tot teruggave, onderaan op de akte gesteld voor

de registratie, heeft dezelfde gevolgen als het met redenen omkleed

verzoek ingevolge artikel 217 2 . Dit verzoek moet een afschrift van de

vermelding van de registratie van de authentieke akte van verkrijging

bevatten, alsook de naam van de begunstigde van de teruggave en, in

voorkomend geval, het rekeningnummer waarop het bedrag van de

terug te geven rechten moet worden gestort.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989

betreffende de financiering van de gemeenschappen en de gewesten)

###### Artikel 213

(gewijzigd bij art. 24 van het KB nr. 12 van 18.04.1967 (B.S., 20.04.1967).

Tekst van toepassing vanaf 30.04.1967 (art. -))

Wordt, onder aftrekking van het algemeen vast recht, aan de

betrokken maatschappij teruggegeven het overeenkomstig artikel 51

geheven recht van 6 t.h. wanneer het aangekochte goed wordt

wederverkocht bij authentieke akte verleden binnen tien jaar na den

datum van de akte van verkrijging.

Zijn toepasselijk op deze teruggaaf, de bepalingen van artikel 212,

tweede en derde lid.

gewesten)

### HOOFDSTUK XIV - Verjaring

###### Artikel 214

(gewijzigd bij art. 63 van de wet van 28.12.1992 (B.S., 31.12.1992 - ed. 3) err.

(B.S., 18.02.1993). Tekst van toepassing vanaf 10.01.1993 (art. -))

Er is verjaring voor de invordering:  Il y a prescription pour le recouvrement :

1° Van rechten en boeten verschuldigd op een akte of een

overeenkomst, na twee jaar, enkel te rekenen van den dag van de

registratie van een akte of geschrift welke de oorzaak van de

vorderbaarheid van de rechten en boeten aan het bestuur

genoegzaam doet kennen om de noodzakelijkheid van alle verdere

opzoeking uit te sluiten.

Worden, voor de toepassing van deze bepaling met registratie

gelijkgesteld: het visum van de repertoria van de notarissen, waarvan

sprake in artikel 180; de ontvangst van de bij artikel 184

voorgeschreven mededeling, zoomede de regelmatige inlevering van

een aangifte van nalatenschap;

2° Van rechten en boeten verschuldigd in geval van ontoereikende

waardering, na twee jaar, te rekenen van den dag van de registratie

van de akte of van de verklaring, dit alles onder voorbehoud van

hetgeen in artikel 190 is voorzien;

3° van rechten verschuldigd in geval van niet-vervulling van de in artikel

60 gestelde voorwaarden, na tien jaar, te rekenen van de datum van de

akte;

4° Van rechten verschuldigd in het in de tweede alinea van artikel 52

voorzien geval, na twee jaar, te rekenen van de intrekking van de premie;

5° Van rechten en boeten verschuldigd in geval van onjuistheid in de in

artikelen 55, 2°, voorziene vermeldingen of attesten, na twee jaar, te

rekenen van den dag van de registratie van de akte;

6° Van boeten verschuldigd in de in artikelen 181 1 tot 183 voorziene

gevallen, na twee jaar, te rekenen van den dag waarop de overtreding

werd vastgesteld;

onjuist vastgesteld in een geregistreerde akte, na vijftien jaar, te

rekenen van den dag waarop de rechtsvordering van de Staat

ontstaan is.

Is van toepassing, ten aanzien van de verjaring, artikel 18 van dit

wetboek.

###### Artikel 215

Er is verjaring voor de vordering tot teruggaaf van rechten, interesten

en boeten, na twee jaar, te rekenen van den dag waarop de

rechtsvordering is ontstaan.

###### Artikel 216

De verjaring van de bij artikel 189 ingestelde rechtsvordering tot

schatting en die van de rechtsvordering tot inning van de rechten en

boeten verschuldigd wegens de ongenoegzaamheid blijkende uit die

schatting, worden gestuit door de in artikel 190 bedoelde notificatie.

De stuiting heeft haar uitwerking tot den dag der nederlegging ter

griffie van het verslag van schatting.

De invordering van rechten, interesten en gebeurlijk van boeten en

kosten, vorderbaar uit hoofde van de bij bedoeld verslag erkende

ongenoegzaamheid, dient vervolgd binnen de twee jaar na de

nederlegging van dit verslag.

###### Art. 217. 1

(gewijzigd en art. 217 1 geworden door art. 36 van de wet van 23.12.1958

(B.S., 07.01.1959). Tekst van toepassing van 17.01.1959 (art. -))

De verjaringen voor de invordering van rechten, interesten en boeten,

worden gestuit op de wijze en onder de voorwaarden voorzien door

###### Art. 2244. en volgende van het Burgerlijk Wetboek. In dit geval is er

een nieuwe verjaring, die op dezelfde wijze kan worden gestuit,

verworven twee jaar na de laatste akte of handeling waardoor de

vorige verjaring werd gestuit, indien er geen geding aanhangig is vóór

het gerecht.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 217. 2

(gewijzigd bij art. 72 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De verjaringen voor de teruggaaf van rechten, interesten en boeten

worden gestuit door een met redenen omklede aanvraag

genotificeerd bij aangetekende zending aan het kantoor dat de schuld

heeft vastgesteld of aan de bevoegde adviseur-generaal van de

Algemene Administratie van de Patrimoniumdocumentatie; ze

worden eveneens gestuit op de wijze en onder de voorwaarden

voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-

generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee

jaar, die slechts op de wijze en onder de voorwaarden voorzien bij

artikelen 2244 en volgende van het Burgerlijk Wetboek kan worden

gestuit, verworven twee jaar na de datum waarop de beslissing,

waarbij de aanvraag werd verworpen, aan belanghebbende met een

aangetekende zending genotificeerd werd.

-----

###### Art. 217. 2

(gewijzigd bij art. 3 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van

toepassing vanaf 01.12.2021 (art. 7))

De verjaringen voor de teruggaaf van rechten, interesten en boeten

worden gestuit door een met redenen omklede aanvraag

genotificeerd bij aangetekende zending aan het kantoor dat de schuld

heeft vastgesteld of aan de bevoegde adviseur-generaal van de

Algemene Administratie van de Patrimoniumdocumentatie; ze

worden eveneens gestuit op de wijze en onder de voorwaarden

voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-

generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee

waarbij de aanvraag werd verworpen, aan belanghebbende bij ter

post aangetekend schrijven genotificeerd werd.

De afgifte van de brieven ter post geldt als notificatie van de volgende

dag af.

###### Artikel 218

(vervangen bij art. 96 van de wet van 26.03.2018 (B.S., 30.03.2018 - ed. 2).

Tekst van toepassing vanaf 09.04.2018 (art. -))

Elke daad van onderzoek of van vervolging als bedoeld in artikel 22

van de Voorafgaande Titel van het Wetboek van Strafvordering

betreffende de misdrijven bedoeld in artikel 206 en 206 bis schorst de

verjaring van de vordering tot voldoening van de rechten, de

interesten en de fiscale geldboeten die erop betrekking hebben.

De schorsing vangt aan met het op gang brengen van de

strafvordering, en eindigt met het staken van de strafrechtelijke

vervolging, het verval van de strafvordering of wanneer het vonnis of

arrest in kracht van gewijsde is gegaan voor de misdrijven bedoeld in

het eerste lid.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Artikel 219

(lid 2, gewijzigd bij art. 73 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De moeilijkheden die in verband met de heffing of de invordering van

de registratierechten vóór het inleiden der gedingen kunnen oprijzen,

worden door de minister van Financiën of de door hem gemachtigde

ambtenaar opgelost.

Indien, na onderhandelingen, met de minister of met de door hem

gemachtigde ambtenaar geen akkoord wordt bereikt over een

moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat

aan de in artikel 189 bedoelde schatting is onderworpen, kan de

bemiddeling van de fiscale bemiddelingsdienst daarover niet meer

gevraagd  of  worden  voortgezet  zodra  de  vordering  tot

controleschatting is ingesteld. De Koning kan bepalen voor welke

moeilijkheden in verband met de heffing en invordering van de

registratierechten bemiddeling door de fiscale bemiddelingsdienst is

uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar

gaat dadingen met de belastingplichtigen aan, voor zover zij geen

vrijstelling of vermindering van belasting in zich sluiten.

Binnen de door de wet gestelde grenzen, wordt het bedrag van de

proportionele fiscale boeten en de vermeerderingen vastgesteld in dit

Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald

volgens een schaal waarvan de trappen door de Koning worden

vastgesteld. Deze bepaling geldt niet voor het bedrag van de

proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en

204, behalve wanneer de overtreder hetzij uit eigen beweging en

voordat het bestuur iets gevorderd heeft, de overtreding aan het

bestuur bekent, hetzij overleden is.

-----

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Artikel 219

(gewijzigd bij art. 124 van de wet van 25.04.2007 (B.S., 08.05.2007 - ed. 3). In

werking vanaf 01.05.2007 (in afwijking hiervan kan de aanvraag tot

bemiddeling slechts worden ingediend met ingang van 01.11.2007 (art. 14,

KB 09.05.2007 (B.S., 24.05.2007)))

De moeilijkheden die in verband met de heffing of de invordering van

de registratierechten vóór het inleiden der gedingen kunnen oprijzen,

worden door de minister van Financiën of de door hem gemachtigde

ambtenaar opgelost.

Indien, na onderhandelingen, met de minister of met de door hem

gemachtigde ambtenaar geen akkoord wordt bereikt over een

moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een

aanvraag tot bemiddeling indienen bij de fiscale bemiddelingsdienst

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat

aan de in artikel 189 bedoelde schatting is onderworpen, kan de

bemiddeling van de fiscale bemiddelingsdienst daarover niet meer

gevraagd  of  worden  voortgezet  zodra  de  vordering  tot

controleschatting is ingesteld. De Koning kan bepalen voor welke

moeilijkheden in verband met de heffing en invordering van de

registratierechten bemiddeling door de fiscale bemiddelingsdienst is

uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar

gaat dadingen met de belastingplichtigen aan, voor zover zij geen

vrijstelling of vermindering van belasting in zich sluiten.

Binnen de door de wet gestelde grenzen, wordt het bedrag van de

proportionele fiscale boeten en de vermeerderingen vastgesteld in dit

Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald

volgens een schaal waarvan de trappen door de Koning worden

vastgesteld. Deze bepaling geldt niet voor het bedrag van de

proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en

204, behalve wanneer de overtreder hetzij uit eigen beweging en

voordat het bestuur iets gevorderd heeft, de overtreding aan het

bestuur bekent, hetzij overleden is.

###### Artikel 220

(gewijzigd bij art. 62 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

De eerste akte van vervolging ter invordering van fiscale rechten of

boeten en bijkomende sommen is een dwangschrift.

Het wordt door den met de invordering belasten ontvanger

uitgevaardigd; het wordt door den bevoegde adviseur-generaal van

de Algemene Administratie van de Patrimoniumdocumentatie

geviseerd  en  uitvoerbaar  verklaard  en  bij  exploot  van

gerechtsdeurwaarder betekend.

###### Artikel 221

(vervangen bij art. 67 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van

toepassing van 06.04.1999 (art. -))

###### Artikel 222

(gewijzigd bij art. 4 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van

toepassing vanaf 01.12.2021 (art. 7))

In geval van niet-betaling van een schuld voortvloeiende uit de

toepassing van dit Wetboek, kan de ambtenaar die belast is met de

invordering van die schuld, bij het Centraal Aanspreekpunt van de

Nationale Bank bedoeld in artikel 322, § 3, eerste lid, van het Wetboek

van de inkomstenbelastingen 1992 de gegevens opvragen die ten

aanzien van die schuldenaar beschikbaar zijn zonder de beperkingen

van artikel 322, §§ 2 tot 4, van hetzelfde Wetboek. De machtiging

hiertoe wordt verleend door een ambtenaar met minimum de graad

van adviseur–generaal.

###### Artikel 223

De moratoire interesten op de in te vorderen of terug te geven

sommen zijn verschuldigd naar den voet en de regelen in burgerlijke

zaken vastgesteld.

###### Artikel 224

(opgeheven bij art. 69 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst

van toepassing vanaf 06.04.1999 (art. -))

(…)

###### Artikel 225

De openbare ambtenaren die, krachtens de bepalingen van deze titel,

voor de partijen, de rechten en, bij voorkomend geval, de boeten

voorgeschoten hebben, kunnen, met het oog op de terugbetaling

ervan, uitvoerbaar bevel vragen aan de vrederechter van hun kanton.

De bepalingen van dit hoofdstuk zijn toepasselijk op het tegen dit

bevel aangetekend verzet.

toepassing vanaf 06.04.1999 (art. -))

De termijnen van verzet, hoger beroep en cassatie, alsmede het

verzet, het hoger beroep en de voorziening in cassatie schorsen de

tenuitvoerlegging van de gerechtelijke beslissing.

###### Art. 225. ter

(vervangen bij art. 382 van de programmawet van 27.12.2004 (B.S.,

31.12.2004 - ed. 2). Tekst van toepassing vanaf 10.01.2005 (art. -))

Het verzoekschrift houdende voorziening in cassatie en het antwoord

op de voorziening mag door een advocaat worden ondertekend en

neergelegd.

###### Art. 225. quater

(ingevoegd bij art. 97 van de wet van 26.03.2018 (B.S., 30.03.2018 - ed. 2).

Tekst van toepassing vanaf 09.04.2018 (art. -))

De bepalingen van dit Wetboek doen geen afbreuk aan het recht van

de Staat om het herstel van de schade te vorderen die kan bestaan uit

de niet-betaling van de rechten, interesten, fiscale geldboeten en

bijbehoren door een burgerlijke partijstelling of door een

aansprakelijkheidsvordering.

### HOOFDSTUK XVI - Bijzondere bepalingen betreffende

##### de openbare verkopingen van roerende goederen

###### Artikel 226

(gewijzigd bij art. 48, § 4, van de wet van 05.07.1963 (M.B., 17.07.1963). Tekst

van toepassing vanaf 28.09.1963 (art. 52))

Meubelen, koopwaren, hout, vruchten, oogsten en alle andere

lichamelijke roerende voorwerpen mogen bij openbare toewijzing

slechts ten overstaan en door het ambt van een notaris of een

gerechtsdeurwaarder verkocht worden.

door hun ambtenaren doen verkopen.

###### Artikel 227

(vervangen bij art. 27 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2).

Tekst van toepassing vanaf 01.01.2024 (art. 29))

Iedere openbare officier die belast is met de openbare verkoop van

roerende voorwerpen moet daarvan vooraf kennis geven aan het

bevoegde kantoor, behalve wanneer het gaat om voorwerpen die aan

de Staat, de gefedereerde entiteiten, de provincies, de gemeenten of

de openbare instellingen toebehoren.

De Koning kan bepalen:  Le Roi peut déterminer :

1° de nadere regels van deze kennisgeving en de vermelding, als de

verkopende partij er een heeft, van haar identificatienummer in het

Rijksregister van de natuurlijke personen of in de registers van de

Kruispuntbank van de sociale zekerheid of in de Kruispuntbank van

Ondernemingen;

2° dat de kennisgeving vergezeld moet gaan van metagegevens.  2° que l'information doit être accompagnée de métadonnées.

###### Artikel 228

De werkende openbare officier of ambtenaar vermeldt, in zijn proces-

verbaal, naam, voornamen, hoedanigheid en woonplaats van den

verzoeker, van de personen wier mobilair te koop wordt gesteld en,

indien het gaat om een verkoop na overlijden, van den overleden

eigenaar, zomede, desvorkomend, den datum van de overhandiging

of de verzending van de in artikel 227 voorziene kennisgeving.

###### Artikel 229

(vervangen bij art. 28 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2).

Tekst van toepassing vanaf 01.01.2024 (art. 29))

De instrumenterende openbare officier of ambtenaar verbeurt voor

elke overtreding van de artikelen 227 en 228 een geldboete van 25

euro.

De werkende openbare officier of ambtenaar moet van den

openbaren verkoop een proces-verbaal opmaken.

Ieder toegewezen voorwerp wordt onmiddellijk in dat proces-verbaal

opgetekend; de prijs wordt voluit in letterschrift en buiten de linie nog

eens in cijfers aangeduid.

Na elke zitting wordt het proces-verbaal afgesloten en ondertekend.  Après chaque séance, le procès-verbal est clôturé et signé.

###### Artikel 231

(gewijzigd bij art. 190 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Wordt voor de toepassing van dit hoofdstuk als toegewezen

beschouwd en is aan het door de artikel 77 vastgesteld evenredig

recht onderworpen, ieder roerend voorwerp waarvan het openbaar

tekoopstelling van een openbaar aanbod of een openbaar gemaakt

aanbod is gevolgd, ongeacht wie het aanbod heeft gedaan en welke

de modaliteiten van den verkoop zijn en ongeacht of al dan niet

toewijzing plaats heeft.

Het recht is evenwel niet verschuldigd indien de werkende openbare

officier of ambtenaar onmiddellijk na ontvangst en bekendmaking van

de aanbiedingen verkondigt, en zulks in het proces-verbaal

aantekent, dat het te koop gesteld voorwerp «ingehouden» wordt.

Het recht wordt geheven op den toewijzingsprijs en, bij gebreke

daaraan, op het hoogste aanbod.

Wanneer het een verkoop geldt, gedaan op verzoek van een

rechtspersoon, wordt nochtans niet afgeweken van artikelen 16 en

17 voor zover zij beschikken voor het geval van voorbehoud van

machtiging, goedkeuring of bekrachtiging van de overheid.

###### Artikel 232

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

1° Een geldboete, gelijk aan twintigmaal het ontdoken recht, zonder

dat ze minder dan 25 EUR mag bedragen:

a) voor elk toegewezen of bij artikel 231 als dusdanig beschouwd lot,

welk niet onmiddellijk in het proces-verbaal wordt opgetekend;

b) voor elk lot welk in het proces-verbaal als aan den verkoop

onttrokken wordt opgegeven, wanneer de verklaring van inhouding

niet werd gedaan in den bij artikel 231, 2 de alinea, voorziene vorm;

c) voor elk lot waarvan de belastbare grondslag in het proces-verbaal

vervalst of onvolkomen opgetekend werd; dit alles onverminderd het

ontdoken recht;

2° Een boete van 12,50 EUR voor elk toegewezen lot waarvan de prijs

in het proces-verbaal niet voluit in letters of niet in cijfers buiten de

linie is aangeduid.

###### Artikel 233

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.

1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

Iedere persoon die, buiten de aanwezigheid van een openbaar officier,

roerende voorwerpen openbaar te koop heeft gesteld of doen stellen,

loopt een geldboete gelijk aan twintigmaal het ontdoken recht, zonder

dat deze boete, voor elk toegewezen of als dusdanig beschouwd lot,

minder dan 25 EUR mag bedragen.

De overtreders zijn daarbij hoofdelijk gehouden tot de betaling van het

ontdoken recht.

###### Artikel 234

(gewijzigd bij art. 63 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van

toepassing vanaf 16.05.2016 (art. -))

Ambtenaren  van  de  Algemene  Administratie  van  de

Patrimoniumdocumentatie hebben steeds toegang tot alle plaatsen

waar roerende voorwerpen openbaar worden verkocht. Zij hebben

het recht zich de processen-verbaal van verkoop te doen overleggen

###### Artikel 235

(vervangen door het enig art. van de wet van 03.07.1962 (B.S., 17.07.1962).

Tekst van toepassing vanaf 27.07.1962 (art. -))

De bepalingen van dit hoofdstuk zijn niet van toepassing op de

openbare verkopingen:

1° van alle landbouwproducten, in instellingen waar de koopwaren

uitsluitend openbaar bij opbod of bij afbod verkocht worden op

bepaalde dagen en uren, die op bestendige wijze in de lokalen

aangeplakt zijn;

2° van eetwaren en van afgesneden bloemen in de voornoemde

instellingen of op de markten;

3° van voorwerpen welke in de openbare kassen van lening in pand

werden gegeven;

4° van zee- en binnenschepen.  4° de navires et de bateaux.

### HOOFDSTUK XVII - Inlichtingen te verstrekken door de

##### Algemene Administratie van de

##### Patrimoniumdocumentatie

###### Artikel 236

(vervangen bij art. 10 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van

toepassing vanaf 01.11.2023 (art. 14, lid 1), met uitzondering van lid 3, van

toepassing vanaf 01.01.2024 (art. 14, lid 1, 7°). De Koning kan evenwel een

datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

De ambtenaren van  de Algemene administratie  van de

patrimoniumdocumentatie leveren, hetzij op verzoek van een partij of

een rechtverkrijgende ervan, hetzij, ingevolge een beschikking van de

vrederechter, op verzoek van een derde die een rechtmatig belang

inroept, afschriften of uittreksels af van hun registratieregisters en

van geregistreerde akten en verklaringen, alles onverminderd de

bepalingen van bijzondere wetten.

De aflevering van deze stukken geeft recht op een door de Koning te

bepalen retributie.

###### Artikel 236/1

(ingevoegd bij art. 11 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van

toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een

datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

§ 1. De ambtenaren van de Algemene administratie van de

patrimoniumdocumentatie kunnen kosteloos inlichtingen afleveren

aan:

1° de administratieve diensten van de federale overheid, de

gefedereerde entiteiten, de provincies, de agglomeraties, de

federaties van gemeenten, de intercommunales, de gemeenten en de

openbare centra voor maatschappelijk welzijn;

2° de parketten en de griffies van de hoven en van alle rechtscolleges;  2° aux parquets et greffes des cours et de toutes les juridictions ;

3° de openbare instellingen of inrichtingen, namelijk de instellingen,

maatschappijen, verenigingen, inrichtingen en diensten die de

federale overheid, een gefedereerde overheid of een lokale overheid

mede beheert, waaraan zo een overheid een waarborg verstrekt,

waarop zo een overheid toezicht uitoefent op de werkzaamheden

ervan, of waarvan zo een overheid het leidinggevend personeel

aanwijst, voordraagt of hun aanstelling goedkeurt.

§ 2. Deze aflevering wordt beperkt tot de inlichtingen die noodzakelijk

zijn voor de uitvoering van wettelijke bepalingen.

De verstrekte inlichtingen mogen niet langer worden bewaard dan

noodzakelijk is voor de verwezenlijking van met de verwerking van de

persoonsgegevens nagestreefde doelstelling.

###### Artikel 236/2

(aangevuld bij art. 79 van de wet van 12.05.2024 (B.S., 29.05.2024). Tekst van

toepassing vanaf 08.06.2024 (art. -))

De Koning kan ter uitvoering van dit hoofdstuk:  Pour l'exécution du présent chapitre, le Roi peut déterminer :

of in de registers van de Kruispuntbank van de sociale zekerheid of in

de Kruispuntbank van de ondernemingen;

2° de nadere regels van de aflevering bepalen;  2° les modalités de la délivrance ;

3° onder voorbehoud van de bepalingen van de Archiefwet van 24

juni 1955, de bewaartermijnen en de wijze van bewaring bepalen van

de vragen om inlichtingen en van de verstrekte antwoorden.

###### Art. 236. bis

(gewijzigd bij art. 13 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van

toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een datum

van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))

Hij die, uit welken hoofde ook, optreedt bij de toepassing van de

belastingwetten of die toegang heeft tot de ambtsvertrekken van de

Algemene Administratie van de Patrimoniumdocumentatie, is buiten

het uitoefenen van zijn ambt, verplicht tot de meest volstrekte

geheimhouding aangaande alle zaken waarvan hij wegens de

uitvoering van zijn opdracht kennis heeft.

Personen die deel uitmaken van diensten of openbare instellingen of

inrichtingen  waaraan inlichtingen, afschriften of uittreksels

afgeleverd werden overeenkomstig de bepalingen van dit hoofdstuk,

zijn tot dezelfde geheimhouding verplicht en mogen ze niet gebruiken

buiten het kader van de wettelijke bepalingen voor de uitvoering

waarvan zij zijn afgeleverd.

De ambtenaren van  de Algemene administratie  van de

patrimoniumdocumentatie, oefenen hun ambt uit wanneer zij

overeenkomstig de bepalingen van dit hoofdstuk inlichtingen,

afschriften of uittreksels afleveren.

### HOOFDSTUK XVIII - Speciaal recht op de nationaliteit,

##### de adelbrieven en de verzoeken tot verandering van

##### naam

###### Artikel 237

(opgeheven bij art. 30 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

#### Afdeling I - Nationaliteit

###### Artikel 238

(gewijzigd bij art. 31 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van

toepassing vanaf 29.07.2025 (art. 33, lid 2))

Er wordt een recht geheven op de procedures tot verkrijging van de

Belgische nationaliteit, die worden bepaald bij hoofdstuk III van het

Wetboek van de Belgische nationaliteit met uitzondering van de

procedures tot verkrijging van de Belgische nationaliteit op grond van

###### Art. 17

van het Wetboek van de Belgische nationaliteit.

Het recht bedraagt 1000 euro.  Le droit s’élève à 1000 euros.

Dit recht wordt tot 150 euro verminderd voor de vreemdeling die de

hoedanigheid heeft van staatloze in België krachtens de er vigerende

internationale overeenkomsten en die zijn aanvraag indient op basis

van artikel 19, § 2, van het Wetboek van de Belgische nationaliteit.

Het recht moet gekweten worden vóór de indiening van het verzoek

of vóór de aflegging van de verklaring.

Het recht wordt jaarlijks op 1 januari geïndexeerd volgens de volgende

formule: basisrecht vermenigvuldigd met de nieuwe index en gedeeld

door de beginindex. Het resultaat verkregen ingevolge de indexering

wordt afgerond op het hogere tiental euro.

De beginindex is de index van de consumptieprijzen van de maand

september 2024 en de nieuwe index is die van de consumptieprijzen

van de maand september die elke indexatie voorafgaat.

Uiterlijk in de loop van de maand december van elk jaar wordt het

bedrag toepasselijk tijdens het volgende kalenderjaar in het Belgisch

Staatsblad gepubliceerd. De Federale Overheidsdienst Financiën

vermeldt die inlichting eveneens op zijn webstek.

----------

Nota:  Note :

Procedures tot verkrijging van de Belgische nationaliteit - Publicatie

voorgeschreven bij art. 238, laatste lid, W.Reg.:

- geïndexeerde bedragen vanaf 01.01.2026: bericht van B.S. , 29.12.2025:

1030 euro (z. art. 238, 2 de lid) ; aangevuld bij bericht van B.S. , 16.03.2026

– ed. 2: 160 euro (z. art. 238, 3 de lid).

(opgeheven bij art. 9 van de wet van 06.08.1993 (B.S., 23.09.1993). Tekst van

toepassing vanaf 03.10.1993 (art. -))

(…)

###### Artikel 240

(opgeheven bij art. 7, 2° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).

Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor

deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke

bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Art. 240. bis

(opgeheven bij art. 7, 3° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).

Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor

deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke

bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Artikel 241

(opgeheven bij art. 7, 4° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).

Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor

deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke

bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

(…)

###### Artikel 242

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S. 12.07.1984). Tekst

van toepassing vanaf 01.01.1985 (art. 19))

###### Artikel 243

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst

van toepassing vanaf 01.01.1985 (art. 19))

(…)  (...)

###### Artikel 244

(opgeheven bij art. 7, 5° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).

Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor

deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke

bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))

( …)  (...)

###### Artikel 245

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst

van toepassing vanaf 01.01.1985 (art. 19))

(…)  (...)

###### Artikel 246

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst

van toepassing vanaf 01.01.1985 (art. 19))

( …)  (...)

###### Artikel 247

(opgeheven bij art. 195 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)  (...)

(gewijzigd bij art. 7 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van

toepassing vanaf 01.03.2021 (art. -))

###### Artikel 248

(gewijzigd bij art. 26 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van

toepassing vanaf 09.03.2026 (art. 33, lid 1))

Op open brieven van verlening van adeldom of van een hogere

adeldomsrang of van opneming onder 's Rijks adel met of zonder titel,

wordt er een recht van 740 euro geheven.

De Koning kan bij een met redenen omkleed besluit dat recht

verminderen, met dien verstande dat het aldus verminderde recht

niet minder dan 490 euro mag bedragen voor de gezamenlijke

personen in de open brief bedoeld.

De vermindering kan slechts worden verleend wanneer de

begunstigde of een van de begunstigden, of een van hun

bloedverwanten in de opgaande of nederdalende lijn, aan het Land

buitengewone diensten heeft bewezen van vaderlandslievende,

wetenschappelijke, culturele, economische, sociale of humanitaire

aard.

###### Artikel 249

(aangevuld bij art. 8 van de wet van 07.01.2024 (B.S., 19.01.2024). Tekst van

toepassing vanaf 01.07.2024 (art. 9))

Een recht is verschuldigd wegens de indiening van het verzoek tot

verandering van naam bedoeld in artikel 370/3 van het Burgerlijk

Wetboek.

Het recht bedraagt 140 euro.  Le droit s’élève à 140 euros.

Het recht is niet verschuldigd in geval van een verandering van naam

als bedoeld in de artikelen 11 bis , 15 en 21 van het Wetboek van de

Belgische nationaliteit.

Het recht is niet verschuldigd bij een naamswijziging als bedoeld in

artikel 370/4, tweede lid, van het oud Burgerlijk Wetboek.

van toepassing vanaf 01.08.2018 (art. 136))

In de gevallen bedoeld in artikel 248, eerste lid, en in artikel 249, is elke

begunstigde een recht verschuldigd.

De door de kinderen of afstammelingen verschuldigde rechten

worden evenwel met de twee vijfden verminderd wanneer aan

hetzelfde recht onderworpen vergunningen bij eenzelfde beslissing

verleend worden aan een persoon en aan zijn kinderen of

afstammelingen waarvan het aantal drie overschrijdt.

###### Artikel 251

(vervangen bij art. 131 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst

van toepassing vanaf 01.08.2018 (art. 136))

Wanneer de vergunning tot verandering van naam wordt ingetrokken

of vernietigd terwijl de registratierechten reeds geïnd zijn, betaalt de

verzoeker, behalve als hij te kwader trouw was, geen rechten meer

wanneer het verzoek beoogt rechtstreeks te verhelpen aan deze

intrekking of vernietiging.

###### Artikel 252

(gewijzigd bij art. 132 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst

van toepassing vanaf 01.08.2018 (art. 136))

Het recht wordt berekend volgens het tarief van kracht op de datum

van het besluit tot verheffing in de adelstand, dat aan de

ondertekening van de adelbrieven voorafgaat, of op de datum van de

indiening van het verzoek tot verandering van naam.

###### Artikel 253

(gewijzigd bij art. 133 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst

van toepassing vanaf 01.08.2018 (art. 136))

De in artikel 248 bedoelde open brieven worden geregistreerd, tegen

betaling van het recht door de begunstigden, binnen zes maanden na

hun datum ten kantore Brussel.

heffen van en geldboete gelijk aan het recht, onverminderd ditzelve.

###### Artikel 254

(gewijzigd bij art. 134 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst

van toepassing van 01.08.2018 (art. 136))

Na betaling van het recht en, gebeurlijk, van de geldboete, wordt

vermelding van registratie gesteld op den open brief van adeldom.

Zolang aan de formaliteit van registratie niet is voldaan, mag de open

brief van adeldom niet aan begunstigden worden uitgereikt.

#### Afdeling III - Bepaling gemeen aan afdelingen I en II

(gewijzigd bij art. 9 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van

toepassing vanaf 01.03.2021 (art. -))

###### Artikel 255

De algemene bepalingen van deze titel betreffende de formaliteit van

de registratie, de verplichting van inzageverlening, bewijsmiddelen,

verjaring, rechtsvervolgingen en gedingen, moratoire interesten zijn

van toepassing in de mate waarin daarvan bij dit hoofdstuk niet wordt

afgeweken.

### HOOFDSTUK XIX - Speciale geldboete wegens late

##### neerlegging van aan bekendmaking onderworpen

##### akten van vennootschap

###### Artikel 256

(opgeheven bij art. 28 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).

Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

###### Artikel 258

(opgeheven bij art. 30 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).

Tekst van toepassing vanaf 08.01.2018 (art. -))

(…)

###### Art. 259. tot 267 W.Reg. federaal

###### Art. 259 à 267 C. enr. fédéral

Het hypotheekrecht is een federale belasting (art. 3, a contrario , wet

16.01.1989 betreffende de financiering van de gemeenschappen en

de gewesten).

## TITEL II - HYPOTHEEKRECHT

###### Artikel 259

(gewijzigd bij art. 5 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van

toepassing vanaf 01.12.2021 (art. 7))

Onder de benaming hypotheekrecht wordt een belasting gevestigd

op de inschrijvingen van hypotheken en voorrechten op onroerende

goederen.

###### Artikel 260

(gewijzigd bij art. 99 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).

Tekst van toepassing vanaf 30.07.2018 (art. -))

Inschrijving van hypotheek wordt slechts verleend, tegen

voorafbetaling door de verzoeker, van de uit dien hoofde

verschuldigde retributies en recht.

De Koning kan deze wijze van vermelding geven aanvullen of wijzigen

voor het geval het inschrijvingsborderel op gedematerialiseerde wijze

wordt aangeboden.

###### Artikel 261

(vervangen bij art. 6 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van

toepassing vanaf 01.12.2021 (art. 7))

Wanneer een inschrijving op verschillende kantoren wordt gevraagd

tot zekerheid van één en hetzelfde bedrag, wordt het over dat bedrag

verschuldigde recht vastgesteld door het kantoor waar de inschrijving

het eerst is gevorderd. Het over dat bedrag geïnde recht dekt de

inschrijvingen op de overige kantoren.

Wanneer tot zekerheid van één en hetzelfde bedrag op

gedematerialiseerde wijze gelijktijdig een inschrijving wordt gevraagd

op verschillende kantoren, wordt het over dat bedrag verschuldigde

recht vastgesteld door het kantoor dat bevoegd is voor het goed dat

als eerste in het inschrijvingsborderel is vermeld. Het over dat bedrag

geïnde recht dekt de inschrijvingen op de overige kantoren.

###### Artikel 262

(gewijzigd bij art. 196 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

Het hypotheekrecht is op 0,30 t.h. gesteld.  Le droit d’hypothèque est fixé à 0,30 p.c.

###### Artikel 263

Het recht is vereffend op het bedrag in hoofd- en bijkomende

sommen waarvoor de inschrijving genomen of hernieuwd wordt.

###### Artikel 264

(gewijzigd bij art. 2, nr. 11 en 5, § 7, 2° van het KB van 20.07.2000 (B.S.,

30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf

gewijzigd bij art. 42, 3° en 5° van het KB van 13.07.2001 (B.S., 11.08.2001 -

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de

hogere cent afgerond.

Het in te vorderen recht mag niet minder dan 5 EUR bedragen.  Le droit à percevoir ne peut être inférieur à 5 EUR.

###### Artikel 265

(3°, gewijzigd bij art. 103 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed.

1). Tekst van toepassing vanaf 07.02.2022 (art. -))

Zijn vrijgesteld van hypotheekrecht:  Sont exemptés du droit d’hypothèque :

1° Inschrijvingen van wettelijke hypotheken en hun vernieuwingen;  1  Les inscriptions d’hypothèques légales et leurs renouvellements ;

2° Inschrijvingen ambtshalve door den Algemene Administratie van

de Patrimoniumdocumentatie genomen;

3° Inschrijvingen tot zekerheid van de invordering van belastingen,

verschuldigd aan de Staat, gefedereerde entiteiten, provincies,

gemeenten, polders en wateringen, en vernieuwingen van die

inschrijvingen;

4° Inschrijvingen genomen ten laste van den Staat, van openbare

instellingen van den Staat en andere in artikel 161, 1°, aangewezen

rechtspersonen, en hun vernieuwingen;

5° De inschrijvingen van de voorrechten en hypotheken opgesteld bij

de wet betreffende het herstel van zekere schade veroorzaakt aan

private goederen door natuurrampen.

###### Artikel 266

(laatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S., 07.01.1959).

Tekst van toepassing vanaf 17.01.1959 (art. -))

Er is verjaring:  Il y a prescription :

1° Voor de invordering van hypotheekrechten die op het tijdstip van

de inschrijving niet zouden geheven zijn geweest, na twee jaar, te

rekenen van den dag der inschrijving;

Die verjaringen worden gestuit overeenkomstig artikel 217 1 en 217 2 .  Les prescriptions sont interrompues conformément aux articles 217 1

###### Artikel 267

Zijn toepasselijk op het hypotheekrecht, de bepalingen van titel I,

betreffende de rechtsvervolgingen en gedingen en de moratoire

interesten.

###### Art. 268. tot 288 W.Reg. federaal

###### Art. 268 à 288 C. enr. fédéral

Het griffierecht is een federale belasting (art. 3, a contrario , wet

16.01.1989 betreffende de financiering van de gemeenschappen en

de gewesten).

## TITEL III - GRIFFIERECHT

### HOOFDSTUK I - VESTIGING VAN DE BELASTING EN

##### VASTSTELLING VAN DE RECHTEN

###### Artikel 268

(gewijzigd bij art. 2 van de wet van 28.04.2015 (B.S., 26.05.2015). Tekst van

toepassing vanaf 01.06.2015 (art. 2, 1°, KB 12.05.2015 (B.S, 26.05.2015)))

Onder de benaming van griffierecht wordt een belasting gevestigd op

de hiernavolgende in de hoven en rechtbanken gedane verrichtingen:

1° de inschrijving van zaken op de algemene rol, op de rol van de

verzoekschriften of op de rol van de vorderingen in kort geding;

2° het opstellen van akten van de griffiers, van vóór hen verleden

akten, van zekere akten van de rechters en van de ambtenaren van

het openbaar ministerie;

3° het afleveren van uitgiften, kopieën of uittreksels uit akten,

vonnissen en arresten en van kopieën van andere stukken die op de

griffie worden bewaard;

###### Art. 269. 1

(gewijzigd bij art. 130 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst

van toepassing vanaf 29.06.2019 (art. -))

Voor elke zaak die op de algemene rol, in het register van de

verzoekschriften of in het register van de vorderingen in kort geding

wordt ingeschreven of terug ingeschreven, is er verschuldigd:

1° in de vredegerechten en de politierechtbanken, een recht van 50

euro;

2°  in  de  rechtbanken  van  eerste  aanleg  en  de

ondernemingsrechtbanken, een recht van 165 euro;

3° in de hoven van beroep een recht van 400 euro;  3° dans les cours d’appel, un droit de 400 euros ;

4° in het Hof van Cassatie een recht van 650 euro.  4° à la Cour de cassation, un droit de 650 euros.

Geen enkel recht wordt geïnd bij de rechtsgedingen voor de

beslagrechter of de vrederechter in het kader van de toepassing van

artikel 1409, § 1, vierde lid, en 1409, § 1 bis, vierde lid, van het

Gerechtelijk Wetboek.

De zaken die worden geacht spoedeisend te zijn zoals bedoeld in

###### Art. 1253. ter /7 van het Gerechtelijk Wetboek zijn onderworpen aan

een eenmalig recht wanneer de nieuwe aanhangigmaking bij de

familierechtbank het wijzigen van een vordering waarover deze zich

al heeft uitgesproken, tot doel heeft. Dit stelsel wordt uitgebreid tot

de maatregelen betreffende de uitoefening van het ouderlijk gezag

uitgesproken door de jeugdrechtbank, waarvan de wijziging wordt

gevraagd voor de familierechtbank.

----------

Nota:  Note :

De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het

Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de

rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019

en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de

rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om

juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld

krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van

het gerechtelijk wetboek teneinde de toegang tot de juridische

tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake

geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die

van toepassing waren vóór de inwerkingtreding van die bepalingen.

(gewijzigd bij art. 131 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst

van toepassing vanaf 29.06.2019 (art. -))

§ 1. De rechter veroordeelt in zijn eindbeslissing de partij of de partijen

die het recht verschuldigd zijn tot de betaling ervan of tot betaling van

hun deel erin. Tegen de beslissing van de rechter kan geen

rechtsmiddel worden aangewend.

Het recht is volledig verschuldigd door de partij die de zaak op de rol

heeft doen stellen, behalve indien:

1° de verweerder in het ongelijk wordt gesteld, in welk geval het recht

volledig verschuldigd is door de verweerder;

2° de partijen onderscheidenlijk omtrent enig geschilpunt in het

ongelijk zijn gesteld, in welk geval het recht ten dele door de eiser en

ten dele door de verweerder verschuldigd is, volgens de beslissing van

de rechter.

Het recht wordt opeisbaar op de datum van de veroordeling.  Le droit est exigible à la date de la condamnation.

§ 2. In geval de zaak op de rol wordt doorgehaald of van de rol wordt

weggelaten bij toepassing van artikel 730, § 1 en § 2, a), van het

Gerechtelijk Wetboek, is het recht vanaf de datum van de doorhaling

of van de weglating opeisbaar ten laste van de partij die de zaak op de

rol heeft doen stellen.

----------

Nota:  Note :

De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het

Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de

rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019

en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de

rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om

juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld

krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van

het gerechtelijk wetboek teneinde de toegang tot de juridische

tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake

geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die

van toepassing waren vóór de inwerkingtreding van die bepalingen.

###### Art. 269. 3

(opgeheven bij art. 4 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).

Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 269. 4

(opgeheven bij art. 5 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).

Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

(…)

----------

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

###### Artikel 270

(opgeheven bij art. 26 van de wet van 12.07.1960 (B.S., 09.11.1960); de art.

269 en 270 zijn door art. 269 vervangen. Tekst van toepassing vanaf

01.01.1961 (art. 39))

(…)  (...)

##### Afdeling I bis - Opstelrecht

###### Art. 270. 1

(gewijzigd bij art. 98 van de wet van 22.06.2012 (B.S. , 28.06.2012). Tekst van

toepassing vanaf 08.07.2012 (art. -))

Op akten van griffiers van hoven en rechtbanken, op akten die buiten

bemoeiing van rechters vóór hen zijn verleden, wordt een opstelrecht

geheven van 35 euro.

Met akten van griffiers van hoven en rechtbanken worden

gelijkgesteld, overschrijvingen gedaan door griffiers in hun registers,

van de verklaringen van beroep of van voorziening in verbreking

strafzaken, door gedetineerden of geïnterneerden afgelegd.

(gewijzigd bij art. 99 van de programmawet van 22.06.2012 (B.S. ,

28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))

De akten van bekendheid, de akten van aanneming en de akten

waarbij een minderjarige machtiging wordt verleend om handel te

drijven, die verleden worden ten overstaan van de vrederechters, zijn

onderhevig aan een opstelrecht waarvan het bedrag op 35 euro wordt

bepaald.

###### Art. 270. 3

(gewijzigd bij art. 100 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst

van toepassing vanaf 08.07.2012 (art. -))

De verklaringen van keus van vaderland zijn onderhevig aan een

opstelrecht, waarvan het bedrag op 35 euro wordt bepaald.

Dit recht is vatbaar voor teruggaaf ingeval de inwilliging bij een

eindbeslissing van het bevoegd gerecht wordt geweigerd.

#### Afdeling II - Expeditierecht

###### Artikel 271

(2°, gewijzigd bij art. 252 van de wet van 15.04.2018 (B.S., 27.04.2018 - ed.

2). Tekst van toepassing vanaf 01.11.2018 (art. 260). De Koning kan een

voorafgaande datum van inwerkingtreding bepalen (art. 260, lid 2))

Op de uitgiften, kopieën of uittreksels die in de griffies worden

afgeleverd, wordt een expeditierecht geheven van:

1°  1,75  euro  per  bladzijde  in  de  vredegerechten  en

politierechtbanken;

2° 3 euro per bladzijde in de hoven van beroep, de hoven van assisen,

het militair gerechtshof, de arrondissementsrechtbanken, de

rechtbanken van eerste aanleg, de ondernemingsrechtbanken en de

krijgsraden;

3° 5,55 euro per bladzijde in het Hof van Cassatie.  3  De 5,55 euros par page, à la Cour de cassation.

(gewijzigd bij art. 102 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst

van toepassing vanaf 08.07.2012 (art. -))

Ongeacht op welke griffie en ongeacht op welke informatiedrager de

aflevering geschiedt, wordt het recht op 0,85 euro per bladzijde

bepaald, zonder dat het verschuldigd bedrag aan rechten lager mag

zijn dan 1,75 euro per afgifte op papier en 5,75 euro op een andere

drager:

1° voor de niet ondertekende kopieën. Indien echter bij één en

hetzelfde verzoek en voor één en dezelfde zaak meer dan twee

kopieën worden aangevraagd, wordt het tarief vanaf de derde kopie

bepaald op 0,30 euro per bladzijde, zonder dat het globaal bedrag aan

verschuldigde expeditierechten alsdan meer dan 1.450 euro kan

bedragen;

2° voor uitgiften, kopieën of uittreksels uit de registers van de

burgerlijke stand of uit de registers welke de akten betreffende het

verkrijgen, het herkrijgen, het behoud en het verlies van nationaliteit

bevatten;

3° voor uitgiften, kopieën of uittreksels uit akten, vonnissen en

arresten die krachtens artikel 162, 33° bis tot 37° bis , vrijstelling

genieten van de formaliteit der registratie;

4° voor de uitgiften, kopieën of uittreksels van akten en stukken

betreffende rechtspersonen ingeschreven in de Kruispuntbank van

Ondernemingen.

Hetzelfde recht is verschuldigd voor uitgiften, kopieën en uittreksels

uit akten, vonnissen en arresten afgeleverd in kieszaken of

militiezaken. Deze stukken dragen bovenaan de vermelding van hun

bestemming; zij mogen tot geen andere doeleinden dienen.

Hetzelfde recht is eveneens verschuldigd voor de kopie van een

elektronisch bestand. Het recht is verschuldigd voor elke gekopieerde

elektronische bladzijde van het brondocument. De parameters van

het brondocument, die de elektronische bladzijde bepalen, mogen bij

het maken van de kopie niet gewijzigd worden.

###### Artikel 273

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006 - ed. 3).

Tekst van toepassing vanaf 07.01.2007 (art. -))

de akte, welke in de uitgifte, de kopie of het uittreksel wordt

weergegeven.

Het recht wordt evenwel éénvormig berekend alsof er slechts één

bladzijde was, voor de uittreksels die worden afgeleverd ter uitvoering

van artikel 121 van het Algemeen Reglement op de gerechtskosten in

strafzaken.

###### Artikel 274

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006). Tekst van

toepassing vanaf 07.01.2007 (art. -))

Wanneer in een uitgifte, kopie of uittreksel meerdere arresten,

vonnissen of akten worden weergegeven, wordt het recht berekend

per bladzijde van elk dezer documenten, zonder dat er, voor ieder van

deze documenten, minder mag geheven worden dan het recht

verschuldigd voor één bladzijde.

###### Art. 274. bis

(gewijzigd bij art. 103 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst

van toepassing vanaf 08.07.2012 (art. -))

Voor kopieën van audiovisueel materiaal is, ongeacht op welke

informatiedrager de kopie wordt afgeleverd, per gekopieerde minuut

1,15 euro verschuldigd, zonder dat de verschuldigde rechten minder

mogen bedragen dan 5,75 euro Een begonnen minuut telt voor een

volle minuut.

###### Art. 274. ter

(gewijzigd bij art. 104 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst

van toepassing vanaf 08.07.2012 (art. -))

De expeditierechten die verschuldigd zijn op één en hetzelfde verzoek

voor één en dezelfde zaak, mogen 1 450 euro niet overschrijden.

#### Afdeling III - Legalisatie- en opzoekingsrechten

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)  (...)

###### Artikel 276

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)  (...)

#### Afdeling IV - Recht van inschrijving in het handelsregister, in

het ambachtsregister en in de registers van de economische

samenwerkingsverbanden

###### Artikel 277

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003 - ed. 3).

Tekst van toepassing vanaf 01.07.2003 (art. 6))

(…)

###### Artikel 278

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003). Tekst

van toepassing van 01.07.2003 (art. 6))

(…)  (...)

### HOOFDSTUK II - Vrijstellingen

###### Art. 279. 1

(aangevuld bij art. 6 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).

Tekst van toepassing vanaf 01.02.2019 (art. 29)) ( (1)

1° De inschrijving van zaken waarvan de vonnissen en arresten,

krachtens artikelen 161 en 162, vrijstelling genieten van het recht of

van de formaliteit der registratie.

Het recht is echter verschuldigd voor de onder artikel 162, 13°,

bedoelde procedures;

2° De inschrijving van een zaak door de griffier van het gerecht

waarnaar de zaak verwezen werd overeenkomstig de wet op het

gebruik der talen in gerechtszaken of ingevolge een rechterlijke

beslissing van onttrekking.

3° de inschrijving van zaken die worden gebracht voor de

arbeidsgerechten;

4° de inschrijving van zaken die ingeleid worden in het kader van het

## boek XX van het Wetboek van economisch recht.

----------

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 279. 2

(5°, opgeheven bij art. 32 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Zijn vrijgesteld van het opstelrecht:  Sont exemptés du droit de rédaction :

1° de akten verleden in de gevallen voorzien door artikelen 161 en

162;

2° de akten of ontvangstbewijzen ten blijke van het neerleggen of

mededelen van stukken, sommen of voorwerpen ter griffie van de

hoven en rechtbanken;

3° de faillissementsbekentenissen, alsmede de afsluitingen of

vermeldingen dier worden aangebracht op de registers, titels en

stukken tot staving daarvan;

4° (…)

5° (…)

(6°, gewijzigd bij art. 27 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst

van toepassing vanaf 09.03.2026 (art. 33, lid 1))

Zijn van expeditierecht vrijgesteld:  Sont exemptés du droit d’expédition :

1° uitgiften, kopieën of uittreksels van of uit akten, vonnissen en

arresten, die krachtens de artikelen 161 en 162 van het recht of van

de formaliteit der registratie zijn vrijgesteld.

Deze bepaling is echter niet van toepassing a) op de in artikel 272,

laatste alinea, bedoelde uitgiften, kopieën of uittreksels; b) op de

uitgiften, afschriften of uittreksels van of uit de in artikel 162, 5°, 13°,

27° en 33° bis tot 37° bis bedoelde akten en vonnissen;

2° de uitgiften, kopieën of uittreksels van of uit vonnissen, arresten,

beschikkingen of andere akten van rechtspleging, die de griffier

ambtshalve of op verzoek van een der partijen toezendt aan de

partijen, aan hun advokaten of aan derden, in uitvoering van het

Gerechtelijk Wetboek of van andere wettelijke of reglementaire

bepalingen.

3° de kopieën van verklaringen met het oog op de inschrijving of tot

wijziging van een inschrijving in het rechtspersonenregister van de

Kruispuntbank van Ondernemingen ambtshalve afgegeven of

toegezonden aan de personen die de inschrijving of de wijziging

aanvragen; de oorzaak van de vrijstelling moet op het kopie vermeld

worden;

4° Uitgiften, kopieën of uittreksels uit de registers van de burgerlijke

stand of uit de registers welke de akten betreffende het verkrijgen,

het herkrijgen, het behoud en het verlies van nationaliteit bevatten.

5° de kopieën of uittreksels van vonnissen en arresten die afgeleverd

worden aan juridische tijdschriften, aangewezen door de Minister van

Financiën;

6° de uitgiften, kopieën of uittreksels afgegeven door de griffie van

het Hof van beroep te Brussel, met het oog op de tenuitvoerlegging in

België van de arresten en beschikkingen die een uitvoerbare titel

uitmaken en gewezen zijn op grond van de Verdragen betreffende de

Europese Unie, betreffende de werking van de Europese unie en tot

oprichting van de Europese Gemeenschap voor Atoomenergie, en

welke luidens de bewoordingen van die Verdragen vatbaar zijn voor

gedwongen tenuitvoerlegging.

geveld krachtens het Verdrag inzake de beslechting van geschillen

met betrekking tot investeringen tussen Staten en onderdanen van

andere Staten, opgemaakt te Washington op 18 maart 1965.

8° de kopieën in strafzaken, afgeleverd aan de vader of de moeder,

aan een adoptant of aan de voogd in hun hoedanigheid van burgerlijke

partij of van persoon die zich op grond van het dossier zou kunnen

beroepen op een nadeel, wanneer de zaak betrekking heeft op een

misdrijf gepleegd tegen een minderjarige en dat naar de wetten

strafbaar is gesteld met een criminele of correctionele straf.

9° de uitvoerbare uitgiften van vonnissen en arresten die aan de

partijen worden verstrekt anders dan krachtens een beschikking van

de voorzitter van de rechtbank als bedoeld in artikel 1379 van het

Gerechtelijk Wetboek.

10° uitgiften, kopieën of uittreksels van een proces-verbaal van

minnelijke schikking bedoeld in artikel 733 van het Gerechtelijk

Wetboek en dat plaats heeft gevonden:

a) bij gelegenheid van verrichtingen binnen het kader van de wet van

12 juli 1976 betreffende het herstel van zekere schade veroorzaakt

aan private goederen door natuurrampen of van de overeenkomstige

gewestelijke bepalingen;

b) naar aanleiding van schadelijke gebeurtenissen die als een

openbare of landbouwramp worden erkend en waarin het herstel of

de schadeloosstelling wordt geregeld door bijzondere wetten of door

internationale overeenkomsten.

###### Artikel 281

(opgeheven bij art. 8 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).

Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

(…)

----------

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

###### Artikel 282

(…)

### HOOFDSTUK III - Diverse bepalingen

###### Artikel 283

In de in artikel 160 voorziene gevallen, worden de griffierechten in

debet vereffend en ingevorderd volgens de regelen die van

toepassing zijn op de onder dezelfde voorwaarden vereffende

registratierechten.

###### Artikel 284

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst

van toepassing vanaf 07.01.2007 (art. -))

Worden eveneens in debet vereffend, de griffierechten verschuldigd

op uitgiften, kopieën van en uittreksels uit akten, vonnissen en

arresten, wanneer die stukken in strafzaken worden afgeleverd aan

het openbaar ministerie of aan de Rijksagenten belast met de

tenuitvoerlegging van vonnissen en arresten.

De rechten worden onder de gerechtskosten begrepen en als

dusdanig ingevorderd ten laste van de partij die er toe veroordeeld

werd.

###### Art. 284. bis

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst

van toepassing vanaf 07.01.2007 (art. -))

In debet worden eveneens vereffend, de griffierechten verschuldigd

op de kopieën in strafzaken die worden afgegeven met toepassing

van de artikelen 674 bis en volgende van het Gerechtelijk Wetboek. De

rechten  alsmede  de  andere  kosten  worden  ingevorderd

overeenkomstig de bepalingen van hetzelfde Wetboek.

###### Artikel 285

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing

vanaf 01.01.2002 (art. 45, § 1))

De wijze van heffing der griffierechten en het houden der registers in

de griffies van de hoven en rechtbanken worden bij koninklijk besluit

geregeld.

Daarbij kan de medewerking van de griffies bij de heffing van de

griffierechten worden voorzien, zonder dat zij daardoor de

hoedanigheid van Staatsrekenplichtige verkrijgen.

Inbreuken op de voorschriften van evenbedoeld koninklijk besluit

kunnen worden bestraft met boeten waarvan het bedrag per inbreuk

250 EUR niet mag te boven gaan.

###### Artikel 286

(voorlaatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S.,

07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))

Er is verjaring:  Il y a prescription :

1° Voor het invorderen der griffierechten en -boeten, na twee jaar, te

rekenen van den dag waarop zij aan den Staat verworven zijn;

2° Voor de vordering tot teruggaaf van ten onrechte geheven rechten

en boeten, na twee jaar, te rekenen van den dag der betaling.

Die verjaringen worden gestuit overeenkomstig artikel 217 1 en 217 2 .  Ces prescriptions sont interrompues conformément aux articles 217 1

Verjaring voor het invorderen der in debet vereffende rechten

ontstaat echter zoals die voor de onder dezelfde voorwaarden

vereffende registratierechten.

###### Artikel 287

De bepalingen van titel I betreffende de vervolgingen en gedingen en

de moratoire interesten, zijn toepasselijk op de griffierechten.

###### Artikel 288

De Koning kan wat de rolrechten betreft bij een in Ministerraad

overlegd besluit de regels bepalen inzake de inning, de

verjaringstermijnen, de wijzen waarop de verjaring wordt gestuit of

geschorst, de vervolgingen en gedingen en de moratoire interesten en

daarbij afwijken van de in artikelen 286 en 287 bepaalde regels. De

besluiten die genomen worden in toepassing van dit artikel, worden

bekrachtigd door de wet binnen de 12 maanden volgend op de datum

van hun bekendmaking in het Belgisch Staatsblad .

----------

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

###### Art. 288. bis

(ingevoegd bij art. 10 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).

Tekst van toepassing vanaf 01.02.2019 (art. 29)) (1)

De Koning kan bepalen dat wegens de laattijdige betaling van een

rolrecht een administratieve boete zal verschuldigd zijn waarvan het

bedrag niet minder kan bedragen dan 25 euro en niet hoger mag zijn

dan de helft van het recht bepaald in artikel 269 1 .

----------

Nota (1) – Overgangsbepaling:

De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in

###### Art. 269. 1 , 1 ste  lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht

vanaf hun datums van inwerkingtreding (art. 28).

TOEKOMSTIG RECHT (vanaf 01.01.2028)

## TITEL IV - DIGITALISATIE VAN DE RELATIES

### TUSSEN DE FEDERALE OVERHEIDSDIENST

### FINANCIËN, DE BURGERS EN BEPAALDE DERDEN

(ingevoegd bij art. 74 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).

Tekst van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art.

222))

(ingevoegd bij art. 75 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Voor de toepassing van de bepalingen van dit Wetboek, van de

bijzondere wetsbepalingen met betrekking tot de registratie-,

hypotheek- en griffierechten of van de ter uitvoering ervan genomen

besluiten, wordt verstaan onder:

1° aangetekende zending: hetzij de briefwisseling, al dan niet

vergezeld van een ontvangstbevestiging, neergelegd bij de aanbieder

van de universele postdienst, een aanbieder van postdiensten of een

gekwalificeerde verlener van vertrouwensdiensten die voldoet aan de

vereisten van artikel 44 van Verordening (EU) nr. 910 /2014 van het

Europees Parlement en de Raad van 23 juli 2014 betreffende

elektronische  identificatie  en  vertrouwensdiensten  voor

elektronische transacties binnen de interne markt en tot intrekking

van Richtlijn 1999/93/CE, en al dan niet elektronisch verzonden door

een van hen naar een vooraf aangewezen ontvanger, die toelaat om

de datum van verzending en ontvangst van de briefwisseling door de

bestemmeling aan te tonen, hetzij het bericht dat door de FOD

Financiën is verzonden in het kader van de uitoefening van haar taak

van openbare dienst door middel van de dienst voor het versturen en

ontvangen  van  elektronische  berichten  door  bepaalde

overheidsdiensten aangeboden aan de natuurlijke personen of hun

vertegenwoordigers door de Federale Overheidsdienst belast met de

Digitale Agenda en aan houders van een ondernemingsnummer zoals

gedefinieerd in artikel III.16 van het Wetboek van economisch recht of

aan hun vertegenwoordigers door de Rijksdienst voor Sociale

Zekerheid;

2° beveiligd elektronisch platform: elke computertoepassing ter

beschikking gesteld door de Federale Overheidsdienst Financiën of

door een andere openbare instelling in samenwerking met de

Federale Overheidsdienst Financiën of een andere instelling die aan

burgers, bedrijven, rechtspersonen en bepaalde derden elektronische

diensten aanbiedt om elektronische berichten uit te wisselen met de

Federale Overheidsdienst Financiën op voorwaarde dat de

authenticatie en identificatie worden uitgevoerd in toepassing van

#### hoofdstuk 4 van de wet van 18 juli 2017 inzake elektronische

identificatie door middel van een stelsel voor elektronische

identificatie zoals bedoeld in art. 8. , 2., van Verordening (EU) nr.

910/2014 van het Europees Parlement en de Raad van 23 juli 2014

betreffende elektronische identificatie en vertrouwensdiensten voor

elektronische transacties in de interne markt en tot intrekking van

zo ook de bewaring van het verzonden bericht garandeert.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. quater

(ingevoegd bij art. 76 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen

anders bepalen, wordt elk bericht aan de Federale Overheidsdienst

Financiën dat uitgaat van een natuurlijke persoon die geen houder is

van een ondernemingsnummer, verzonden door middel van een

beveiligd elektronisch platform voor zover hij er expliciet voor gekozen

heeft om met de Federale Overheidsdienst Financiën langs

elektronische weg te communiceren.

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig

het eerste lid, wordt elk bericht onder gesloten omslag verzonden.

Wanneer het bericht aan de Federale Overheidsdienst Financiën dat

uitgaat van een burger, natuurlijke persoon, die geen houder is van

een ondernemingsnummer, betrekking heeft op meerdere burgers en

niet al deze burgers expliciet gekozen hebben om langs elektronische

weg met de Federale Overheidsdienst Financiën te communiceren,

wordt het bericht altijd onder gesloten omslag verzonden naar al deze

burgers.

De  Koning  bepaalt  de  toepassingsmodaliteiten  van  de

uitwisselingsprocedure van berichten via elektronische weg.

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen

anders bepalen, wordt elk bericht van de Federale Overheidsdienst

Financiën aan een natuurlijke persoon die geen houder is van een

ondernemingsnummer, verzonden door middel van een beveiligd

elektronisch platform voor zover die er expliciet voor gekozen heeft

om met de Federale Overheidsdienst Financiën langs elektronische

weg te communiceren.

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig

het eerste lid, wordt elk bericht onder gesloten omslag verzonden.

elektronische weg met de Federale Overheidsdienst Financiën te

communiceren, wordt het bericht altijd onder gesloten omslag

verzonden naar al deze burgers.

§ 3. De keuze van een natuurlijke persoon die geen houder is van een

ondernemingsnummer om met de Federale Overheidsdienst

Financiën langs elektronische weg te communiceren gebeurt door de

uitdrukkelijke en voorafgaande aanvaarding van het elektronische

communicatieproces met de Federale Overheidsdienst Financiën

door middel van een beveiligd elektronisch platform. Deze

voorafgaande  en  uitdrukkelijke  toestemming  moet  vrij,

weloverwogen en ondubbelzinnig zijn. De natuurlijk persoon die geen

houder is van een ondernemingsnummer kan zijn instemming op elk

moment intrekken. Het bericht zal dan voor de toekomst onder

gesloten omslag worden verstuurd en deze intrekking van

toestemming zal onmiddellijk van kracht worden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. quinquies

(ingevoegd bij art. 77 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Behoudens indien de wettelijke of reglementaire bepalingen anders

bepalen, wordt elk bericht aan de Federale Overheidsdienst Financiën

dat  uitgaat  van  een  persoon  die  houder  is  van  een

ondernemingsnummer, verzonden door middel van een beveiligd

elektronisch platform.

Behoudens indien de wettelijke of reglementaire bepalingen anders

bepalen, wordt elk bericht van de Federale Overheidsdienst Financiën

aan een persoon die houder is van een ondernemingsnummer,

verzonden door middel van een beveiligd elektronisch platform.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. sexies

(ingevoegd bij art. 78 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

Behoudens indien de wettelijke of reglementaire bepalingen anders

bepalen, zal een bericht wanneer dat bericht niet verzonden kan

worden door middel van een beveiligd elektronisch platform

ingevolge overmacht, worden verzonden onder gesloten omslag.

Wanneer een persoon zich niet heeft kunnen identificeren bij een

beveiligd elektronisch platform omdat het beveiligd elektronisch

platform technisch niet geconfigureerd is om deze persoon toe te

staan er verbinding mee te maken, wordt het bericht eveneens onder

gesloten omslag verzonden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. septies

(ingevoegd bij art. 79 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen

anders bepalen, wordt elk bericht door een persoon verzonden door

middel van een beveiligd elektronisch platform, onmiddellijk ter

beschikking gesteld op het beveiligd elektronisch platform van de

Federale  Overheidsdienst  Financiën.  De  datum  van  de

terbeschikkingstelling geldt als datum van de ontvangst van het

bericht door de Federale Overheidsdienst Financiën.

Elk bericht door de Federale Overheidsdienst Financiën verzonden

door middel van een beveiligd elektronisch platform bevat in het

opschrift van het bericht op het beveiligd elektronisch platform van de

Federale  Overheidsdienst  Financiën,  een  datum  van

terbeschikkingstelling van het bericht.

Behoudens indien de wettelijke of reglementaire bepalingen anders

bepalen is het, voor elk bericht verzonden of ontvangen door middel

van een beveiligd elektronisch platform, de derde werkdag die volgt

op de datum van terbeschikkingstelling in het opschrift van het

bericht op het beveiligd elektronisch platform van de Federale

Overheidsdienst Financiën die het vertrekpunt zal zijn van de

termijnen die van toepassing zijn voor het vervullen van de rechten en

plichten in dit Wetboek, in de bijzondere wetsbepalingen met

betrekking tot de registratie-, hypotheek- en griffierechten of van de

tot uitvoering ervan genomen besluiten.

platform en wanneer de datum van terbeschikkingstelling van het

bericht in het opschrift van het bericht op het beveiligd elektronisch

platform van de Federale Overheidsdienst Financiën en de datum van

verzending van het bericht verzonden door middel van een beveiligd

elektronisch platform verschillend zijn, zal de datum die het

voordeligst is voor de betrokken persoon het vertrekpunt van de

termijn zijn.

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen

anders bepalen, is het de derde werkdag die volgt op de datum van

verzending van het bericht verzonden of ontvangen onder gesloten

omslag, die het vertrekpunt zal zijn van de termijnen die van

toepassing zijn voor het vervullen van de rechten en plichten in dit

Wetboek, in de bijzondere wetsbepalingen met betrekking tot de

registratie-, hypotheek- en griffierechten of in de tot uitvoering ervan

genomen besluiten.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. octies

(ingevoegd bij art. 80 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

De rechtsgevolgen van een bericht verzonden door middel van een

beveiligd elektronisch platform of onder gesloten omslag zijn

dezelfde.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. nonies

(ingevoegd bij art. 81 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Wanneer een document elektronisch wordt ondertekend door de

opsteller of opstellers, gebeurt die ondertekening minstens door

middel van een geavanceerde elektronische handtekening in de zin

van artikel 3.11. van Verordening (EU) nr. 910/2014 van het Europees

Wanneer een document elektronisch wordt ondertekend door middel

van het stelsel voor elektronische identificatie aangemeld door België

overeenkomstig artikel 9.1. van de Verordening (EU) nr. 910/2014,

wordt die ondertekening beschouwd als gekwalificeerd in de zin van

###### Art. 3.12

van die Verordening.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288. decies

(ingevoegd bij art. 82 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst

van toepassing voor alle of bepaalde categorieën van houders van een

ondernemingsnummer, evenals voor natuurlijke personen, op een datum

respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))

Voor de toepassing van artikelen 288 quater tot en met 288 nonies ,

wordt verstaan onder "bericht": alle schriftelijke mededelingen

betreffende de rechten en plichten opgenomen in dit Wetboek, in de

bijzondere wetsbepalingen met betrekking tot de registratie-,

hypotheek- en griffierechten of in de ter uitvoering ervan genomen

besluiten, inclusief briefwisseling, formulieren en verzendingen van

gegevens, ongeacht de gebruikte drager.

GEMEENSCHAPPELIJKE BEPALINGEN VOOR ALLE

##### BELASTINGEN

(gewijzigd bij art. 5 van de wet van 17.08.2013 (B.S., 05.09.2013). Tekst van

toepassing vanaf 01.01.2013 (art. 21))

###### Artikel 289

(gewijzigd bij art. 3 van de wet van 14.01.2013 (B.S., 31.01.2013 - ed. 2). Tekst

van toepassing vanaf 10.02.2013 (art. -))

§ 1. De bestuursdiensten van de Staat, met inbegrip van de parketten

en de griffies der hoven en rechtbanken, de besturen van de

provinciën en van de gemeenten, zomede de openbare organismen

en instellingen, zijn gehouden, wanneer zij daartoe aangezocht zijn

door een ambtenaar van een der Rijksbesturen belast met de aanslag

inzage te verlenen en hem alle inlichtingen, afschriften of uittreksels

te laten nemen, welke bedoelde ambtenaar ter verzekering van de

aanslag in, of de heffing van de door de Staat geheven belastingen

nodig acht.

Onder openbare organismen dienen verstaan, naar de geest van deze

wet, de instellingen, maatschappijen, verenigingen, inrichtingen en

diensten welke de Staat mede beheert, waaraan de Staat een

waarborg verstrekt, op welker bedrijvigheid de Staat toezicht

uitoefent of waarvan het bestuurspersoneel aangewezen wordt door

de regering, op haar voordracht of mits haar goedkeuring.

Van de akten, stukken, registers, bescheiden of inlichtingen in

verband met gerechtelijke procedures mag evenwel geen inzage of

afschrift worden verleend zonder uitdrukkelijke toelating van het

openbaar ministerie.

Nationaal Instituut voor de statistiek, noch op de kredietinstellingen.

Andere afwijkingen van deze bepaling kunnen worden ingevoerd bij

door de Minister van Financiën medeondertekende koninklijke

besluiten.

§ 2. Elke inlichting, stuk, proces-verbaal of akte ontdekt of bekomen

in het uitoefenen van zijn functie, door een ambtenaar van de

Federale Overheidsdienst Financiën, hetzij rechtstreeks, hetzij door

tussenkomst van een der hierboven aangeduide diensten, kan door

de Staat ingeroepen worden voor het opsporen van elke krachtens de

belastingwetten verschuldigde som.

Desondanks kan het aanbieden tot registratie van de processen-

verbaal en van de verslagen over expertises betreffende gerechtelijke

procedures, het bestuur dan alleen toelaten die akten in te roepen

mits het daartoe de in alinea 3 van § 1 bepaalde toelating heeft

bekomen.

§ 3. Alle administraties die ressorteren onder de Federale

Overheidsdienst Financiën zijn gehouden alle in hun bezit zijnde

toereikende, ter zake dienende en niet overmatige inlichtingen ter

beschikking te stellen aan alle ambtenaren van deze Overheidsdienst,

voorzover die ambtenaren regelmatig belast zijn met de vestiging of

de invordering van de belastingen, en voorzover die gegevens

bijdragen tot de vervulling van de opdracht van die ambtenaren tot de

vestiging of de invordering van eender welke door de Staat geheven

belasting.

niet overmatige inlichtingen te vragen, op te zoeken of in te zamelen

die bijdragen tot de vestiging of de invordering van eender welke,

andere, door de Staat geheven belasting.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 289. bis

(§   12, lid 3, gewijzigd bij art. 83 van de wet van 12.05.2024 (B.S., 30.05.2024

– ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders

van een ondernemingsnummer, evenals voor natuurlijke personen, op een

datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028

(art. 222))

§ 1 . Dit artikel legt de voorschriften en procedures vast voor de

samenwerking tussen België en de andere lidstaten van de Europese

Unie met het oog op de uitwisseling van inlichtingen die naar

verwachting van belang zijn voor de administratie en de handhaving

van de nationale wetgeving van alle lidstaten met betrekking tot de

registratie-, hypotheek- en griffierechten.

Dit artikel legt tevens de bepalingen vast voor de elektronische

uitwisseling van de in het eerste lid bedoelde inlichtingen.

Dit artikel laat de toepassing van de regels inzake wederzijdse

rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de

verplichtingen van de lidstaten inzake ruimere administratieve

samenwerking, welke voortvloeien uit andere rechtsinstrumenten,

waaronder bilaterale en multilaterale overeenkomsten.

§ 2 . Voor de toepassing van dit artikel wordt verstaan onder:  § 2. Aux fins du présent article, on entend par :

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari

2011 betreffende de administratieve samenwerking op het gebied

van de belastingen en tot intrekking van richtlijn 77/799/EEG;

2° "lidstaat": een lidstaat van de Europese Unie;  2° « Etat membre » : un Etat membre de l’Union Européenne ;

3° "centraal verbindingsbureau": het bureau dat als zodanig is

aangewezen door de bevoegde autoriteit en belast is met de primaire

zorg voor de contacten met de andere lidstaten op het gebied van de

administratieve samenwerking;

wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel

gemachtigd is door de bevoegde autoriteit om rechtstreeks

inlichtingen uit te wisselen;

6° "Belgische bevoegde autoriteit": de door België als zodanig

aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de

Belgische  verbindingsdiensten  en  de  Belgische  bevoegde

ambtenaren worden eveneens als Belgische bevoegde autoriteit bij

delegatie beschouwd;

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere

dan België, als zodanig aangewezen autoriteit. Het centraal

verbindingsbureau, de verbindingsdiensten en de bevoegde

ambtenaren van deze lidstaat worden eveneens als buitenlandse

bevoegde autoriteit bij delegatie beschouwd;

8° "verzoekende autoriteit": het centraal verbindingsbureau, een

verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die

namens de Belgische of een buitenlandse bevoegde autoriteit om

bijstand verzoekt;

9° "aangezochte autoriteit": het centraal verbindingsbureau, een

verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die

namens de Belgische of een buitenlandse bevoegde autoriteit om

bijstand wordt verzocht;

10° "administratief onderzoek": alle door de lidstaten bij het vervullen

van hun taken verrichte controles, onderzoeken en acties ter

waarborging van de juiste toepassing van de belastingwetgeving;

11° "automatische uitwisseling":  11° « échange automatique » :

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de

systematische mededeling met regelmatige, vooraf vastgestelde

tussenpozen zonder voorafgaand verzoek van vooraf bepaalde

inlichtingen aan een andere lidstaat;

b) voor de toepassing van alle andere bepalingen van dit artikel,

andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3,

de systematische mededeling van vooraf bepaalde inlichtingen

verstrekt overeenkomstig de punten a) en b)

13° "persoon":  13° « personne » :

a. een natuurlijk persoon;  a. une personne physique ;

b. een rechtspersoon;  b. une personne morale ;

c. indien de geldende wetgeving in die mogelijkheid voorziet, een

vereniging van personen die bevoegd is rechtshandelingen te

verrichten, maar niet de status van rechtspersoon bezit; of

d. een andere juridische constructie, ongeacht de aard of de vorm, met

of zonder rechtspersoonlijkheid, die activa, met inbegrip van de

daardoor gegenereerde inkomsten, bezit of beheert welke aan

belastingen in de zin van de richtlijn zijn onderworpen;

14° "langs elektronische weg": door middel van elektronische

apparatuur voor gegevensverwerking - met inbegrip van digitale

compressie - en gegevensopslag, met gebruikmaking van kabels,

radio, optische technologie of andere elektromagnetische middelen;

15°  "CCN-netwerk":  het  op  het  gemeenschappelijke

communicatienetwerk gebaseerde gemeenschappelijke platform dat

de Europese Unie heeft ontwikkeld voor het elektronische

berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied

van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk

akkoord, elke mededeling of enig ander instrument of handeling met

soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of

hernieuwd, in het kader van een belastingcontrole, en die aan de

volgende cumulatieve voorwaarden voldoen:

a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht

of deze beslissingen effectief gebruikt worden;

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon

of een groep van personen, en voor zover deze persoon of deze groep

van personen er zich kan op beroepen;

c) betreft de interpretatie of toepassing van een wettelijke of

administratieve bepaling betreffende de handhaving of de toepassing

van dit Wetboek en de met de registratie-, hypotheek- en

griffierechten verband houdende autonome bepalingen;

d) heeft betrekking op een grensoverschrijdende verrichting en  d) se rapporte à une opération transfrontière et

17° "grensoverschrijdende verrichting" als vermeld in de bepaling

onder 16°: een verrichting of reeks van verrichtingen die voldoen aan

een of meer van de volgende voorwaarden:

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van

verrichtingen  fiscaal  inwoners  van  België  zijn  dat  de

grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt,

gewijzigd of hernieuwd

b) waarbij een van de partijen bij de verrichting of reeks van

verrichtingen haar fiscale woonplaats tegelijkertijd in meer dan een

rechtsgebied heeft;

c)  de  verrichtingen  of  reeks  van  verrichtingen  een

grensoverschrijdend effect hebben.

18° "verbonden onderneming", voor de toepassing van paragraaf

6/3: een persoon die gelieerd is met een andere persoon op ten

minste één van de volgende wijzen:

a) een persoon neemt deel aan de leiding van een andere persoon

waarbij hij invloed van betekenis kan uitoefenen op die andere

persoon;

b) een persoon neemt deel aan de zeggenschap over een andere

persoon door middel van een deelneming van meer dan 25 % van de

stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon

door middel van een eigendomsrecht van, rechtstreeks of middellijk,

meer dan 25 % van het kapitaal;

d) een persoon heeft recht op 25 % of meer van de winsten van een

andere persoon.

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en

met d), aan de leiding van, aan de zeggenschap over of in het kapitaal

of de winsten van dezelfde persoon, worden alle betrokken personen

als verbonden ondernemingen beschouwd.

Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met

d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de

winsten van meer dan één persoon, worden alle betrokken personen

als verbonden ondernemingen beschouwd.

een deelneming in alle stemrechten of het volledige kapitaalbezit dat

die andere persoon in de genoemde entiteit heeft.

Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c)

is voldaan door vermenigvuldiging van de deelnemingspercentages

door de opeenvolgende niveaus heen. Een persoon die meer dan 50

% van de stemrechten houdt, wordt geacht 100 % te houden.

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in

de rechte lijn worden behandeld als één persoon.

19° "gezamenlijke audit": een administratief onderzoek dat

gezamenlijk door de bevoegde autoriteiten van twee of meer

lidstaten wordt uitgevoerd, en verband houdt met een of meer

personen van gezamenlijk of complementair belang voor de

bevoegde autoriteiten van die lidstaten;

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot

vernietiging, verlies, wijziging of elk voorval van ongepaste of

ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen,

met inbegrip van, maar niet beperkt tot, persoonsgegevens die

worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg

van opzettelijke onwettige handelingen, nalatigheid of ongevallen.

Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid,

de beschikbaarheid en de integriteit van gegevens.

§ 3 . De Belgische bevoegde autoriteit wisselt met de buitenlandse

bevoegde autoriteiten inlichtingen uit.

§ 4 . Met betrekking tot een specifiek geval kan de Belgische bevoegde

autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de

eerste § vermelde inlichtingen die deze in haar bezit heeft of naar

aanleiding van een administratief onderzoek verkregen heeft, te

verstrekken. Het verzoek kan een met redenen omkleed verzoek om

een bepaald administratief onderzoek in te stellen, omvatten.

De Belgische bevoegde autoriteit kan de aangezochte autoriteit

verzoeken haar de originele stukken over te maken.

§ 5 . De Belgische bevoegde autoriteit verstrekt op verzoek van een

buitenlandse bevoegde autoriteit met betrekking tot een specifiek

geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft

of naar aanleiding van een administratief onderzoek verkregen heeft,

dat werd ingesteld om die inlichtingen te verkrijgen.

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten

van het gevraagde administratief onderzoek gaat de Belgische

bevoegde autoriteit te werk volgens dezelfde procedures als

handelde zij uit eigen beweging of op verzoek van een andere

Belgische instantie.

Op specifiek verzoek van de verzoekende autoriteit verstrekt de

Belgische bevoegde autoriteit de originele stukken, tenzij de

Belgische voorschriften zich hiertegen verzetten.

De inlichtingen worden door de Belgische bevoegde autoriteit zo

spoedig mogelijk, doch uiterlijk drie maanden na de datum van

ontvangst van het verzoek verstrekt. Indien de Belgische bevoegde

autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij

deze binnen twee maanden. In bijzondere gevallen kunnen de

Belgische bevoegde autoriteit en de verzoekende autoriteit een

andere termijn overeenkomen.

De ontvangst van het verzoek wordt door de Belgische bevoegde

autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval

uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs

elektronische weg, bevestigd.

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk

een maand na ontvangst van het verzoek, aan de verzoekende

autoriteit weten welke tekortkomingen het verzoek vertoont en

preciseert welke aanvullende achtergrondinformatie zij verlangt. In

dit geval gaan de in het vijfde lid gestelde termijnen in op de datum

waarop de Belgische bevoegde autoriteit de aanvullende informatie

ontvangt.

Indien de Belgische bevoegde autoriteit niet binnen de gestelde

termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor

onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van

het verzoek, aan de verzoekende autoriteit mee, met vermelding van

de datum waarop zij meent aan het verzoek te kunnen voldoen. Deze

termijn mag niet langer zijn dan zes maanden te rekenen vanaf de

datum van ontvangst van het verzoek.

Indien de Belgische bevoegde autoriteit niet over de gevraagde

inlichtingen beschikt en niet aan het verzoek om inlichtingen kan

voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt

zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand

na ontvangst van het verzoek, aan de verzoekende autoriteit mee.

belang te zijn indien op het ogenblik van het verzoek de verzoekende

autoriteit van oordeel is dat er overeenkomstig haar nationale

wetgeving een redelijke mogelijkheid bestaat dat de verzochte

inlichtingen van belang zullen zijn voor de belastingaangelegenheden

van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of

anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van

het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen,

verstrekt de verzoekende autoriteit ten minste de volgende

inlichtingen aan de aangezochte autoriteit:

a) het fiscale doel waarvoor de informatie wordt opgevraagd;  a) la finalité fiscale des informations demandées ;

b) een specificering van de inlichtingen die nodig zijn voor de

uitvoering of handhaving van haar nationale recht.

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op

een groep belastingplichtigen die niet individueel kunnen worden

geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op

basis van een gemeenschappelijke reeks kenmerken.

In dergelijke gevallen, verstrekt de verzoekende autoriteit de

volgende informatie aan de aangezochte autoriteit:

a) een gedetailleerde beschrijving van de groep;  a) une description détaillée du groupe ;

b) een toelichting bij de toepasselijke wetgeving en bij de feiten op

basis waarvan redelijkerwijze vermoed kan worden dat de

belastingplichtigen in de groep de toepasselijke wetgeving niet

hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen

zouden bijdragen tot het bepalen van de mate waarin de

belastingplichtigen in de groep aan hun verplichtingen voldoen;

d) in voorkomend geval, feiten en omstandigheden die verband

houden met de tussenkomst van een derde die actief heeft

bijgedragen tot de mogelijke niet-naleving van de toepasselijke

wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse

bevoegde autoriteit automatisch alle inlichtingen waarover zij ten

aanzien van ingezetenen van die andere lidstaat beschikt inzake de

volgende specifieke inkomsten- en vermogenscategorieën, op te

vatten in de zin van de Belgische wetgeving:

a) inkomen uit een dienstbetrekking;  a) revenus d'emploi ;

b) tantièmes en presentiegelden;  b) tantièmes et jetons de présence ;

c) levensverzekeringsproducten die niet vallen onder andere

Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch

onder soortgelijke voorschriften;

d) pensioenen;  d) pensions ;

e) eigendom van en inkomsten uit onroerend goed;  e) propriété et revenus de biens immobiliers ;

f) royalty's;  f) redevances ;

g) inkomsten uit dividenden zonder bewaarneming, met uitzondering

van  inkomsten  uit  dividenden  die  zijn  vrijgesteld  van

vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn

2011/96/EU van de Raad.

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de

verstrekking van de in de eerste alinea genoemde inlichtingen het

door de lidstaat van verblijf afgegeven fiscaal identificatienummer

(TIN) van ingezetenen.

België stelt de Commissie jaarlijks in kennis van ten minste twee

inkomsten- en vermogenscategorieën die zijn opgenomen in de

eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over

ingezetenen van een andere lidstaat.

België stelt de Commissie vóór 1 januari 2026 in kennis van ten

minste vijf categorieën die zijn opgenomen in het eerste lid, ten

aanzien waarvan de bevoegde autoriteit van elke andere lidstaat

automatisch inlichtingen verstrekt over ingezetenen van die andere

lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken

die ingaan op of na 1 januari 2026.

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen

zes maanden na het verstrijken van het kalenderjaar in de loop

waarvan de inlichtingen beschikbaar zijn geworden.

"Beschikbare inlichtingen" betekent inlichtingen die zich in de

belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden

en die opvraagbaar zijn overeenkomstig de procedures voor het

verzamelen en verwerken van inlichtingen in die lidstaat.

1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van

deze paragraaf, verstrekt de Belgische bevoegde autoriteit

automatisch inlichtingen aan de bevoegde autoriteiten van alle

andere lidstaten en de Europese Commissie, overeenkomstig de

volgens § 24 vastgestelde van toepassing zijnde praktische

modaliteiten wanneer een grensoverschrijdende voorafgaande

beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december

2016.

2°  de  Belgische  bevoegde  autoriteit  verstrekt  eveneens,

overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde

praktische modaliteiten, aan de bevoegde autoriteiten van alle andere

lidstaten, evenals aan de Europese Commissie, de inlichtingen over

grensoverschrijdende voorafgaande fiscale beslissingen die zijn

verstrekt, gewijzigd of hernieuwd binnen de periode beginnend vijf

jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in

de bepaling onder 6° van deze paragraaf.

Indien de grensoverschrijdende voorafgaande fiscale beslissingen

werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en

31 december 2013, worden deze inlichtingen verstrekt op

voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.

Als grensoverschrijdende voorafgaande fiscale beslissingen werden

verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31

december 2016, worden die inlichtingen verstrekt ongeacht of die

grensoverschrijdende voorafgaande beslissingen al dan niet nog

geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin

een voorafgaande grensoverschrijdende ruling betrekking heeft op

belastingaangelegenheden van een of meer natuurlijke personen,

tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1

januari 2026 is afgegeven, gewijzigd of hernieuwd, en:

a) het bedrag van de transactie of reeks transacties van de

voorafgaande grensoverschrijdende ruling groter is dan 1.500.000

euro (of het equivalent daarvan in een andere valuta), indien dat

bedrag wordt vermeld in de voorafgaande grensoverschrijdende

ruling, of;

b) de voorafgaande grensoverschrijdende ruling bepaalt of een

persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de

ruling afgeeft.

reeks transacties met betrekking tot verschillende goederen,

diensten of activa, de totale onderliggende waarde. De bedragen

worden niet geaggregeerd indien dezelfde goederen, diensten of

activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande

grensoverschrijdende rulings inzake bronbelasting op inkomsten uit

arbeid, tantièmes en presentiegelden of pensioenen van niet-

ingezetenen niet onder de uitwisseling van inlichtingen over

voorafgaande grensoverschrijdende rulings met betrekking tot

natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:  4° L’échange d’informations est effectué comme suit :

a) voor de op grond van 1° uitgewisselde inlichtingen: onverwijld

zodra de voorafgaande grensoverschrijdende rulings of voorafgaande

verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of

hernieuwd en uiterlijk binnen drie maanden na het einde van het

semester  van  het  kalenderjaar  waarin  de  voorafgaande

grensoverschrijdende  rulings  of  voorafgaande

verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of

hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde

inlichtingen: vóór 1 januari 2018.

5° De door de Belgische bevoegde autoriteit uit hoofde van de

bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen

omvatten de volgende gegevens:

a) de identificatie van de rechtspersoon, tenzij de voorafgaande

grensoverschrijdende ruling betrekking heeft op een natuurlijke

persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt,

en in voorkomend geval de groep personen waartoe die persoon

behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende

ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen

een omschrijving van de relevante zakelijke activiteiten of transacties

of reeks van transacties, alsook alle andere inlichtingen die voor de

bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een

mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking

van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een

fabrieks- of handelswerkwijze, of van inlichtingen waarvan het

verstrekken in strijd zou zijn met de openbare orde.

d) de aanvangsdatum van de geldigheidsperiode van de

grensoverschrijdende  voorafgaande  fiscale  beslissing,  indien

vermeld;

e)  de  einddatum  van  de  geldigheidsperiode  van  de

grensoverschrijdende  voorafgaande  fiscale  beslissing,  indien

vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;  f) le type de décision fiscale anticipée en matière transfrontière ;

g) het bedrag van de verrichting of reeks van verrichtingen van de

grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld

in de grensoverschrijdende voorafgaande fiscale beslissing;

h) in voorkomend geval, de identificatie van de andere lidstaten die

mogelijks betrokken zijn bij de grensoverschrijdende voorafgaande

fiscale beslissing;

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling

betrekking heeft op een natuurlijke persoon en overeenkomstig de

bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die

er zijn, waarop de voorafgaande grensoverschrijdende ruling of de

voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van

invloed zal zijn waarbij vermeld dient te worden met welke lidstaten

de getroffen personen verbonden zijn, en

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a) , b) , en i) van

deze paragraaf worden niet medegedeeld aan de Europese

Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de

inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel

en in elk geval niet later dan zeven werkdagen na ontvangst, aan de

verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing

totdat het in § 24, 3 de en 4 de lid, bedoelde gegevensbestand

operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met

inachtneming van de bepalingen van § 24, 2 de lid, om aanvullende

inlichtingen verzoeken, daaronder begrepen de volledige tekst van

een grensoverschrijdende voorafgaande fiscale beslissing.

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen,

bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan

de commissie mee de statistieken over het volume van de

automatische uitwisseling in toepassing van de paragrafen 6 en 6/1,

alsook de inlichtingen over de kosten en baten, administratief en

andere, verbonden aan de uitwisseling die plaats heeft gevonden, en

aan de eventuele wijzigingen, zowel voor de belastingadministraties

als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle

relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie

van de administratieve samenwerking voorzien door dit artikel in het

licht van de strijd tegen de fiscale fraude en ontduiking.

De Belgische bevoegde autoriteit controleert en evalueert de

efficiëntie van de administratieve samenwerking voorzien door dit

artikel, met name wat betreft de strijd tegen de belastingontduiking

en deelt de Commissie de resultaten van zijn evaluatie een maal per

jaar mee via een formulier en volgens de modaliteiten voorzien door

de Commissie.

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde

lid bedoelde termijn de in tweede lid bedoelde gegevens inzake

grensoverschrijdende constructies, waarvan zij ingelicht is door de

intermediair of de relevante belastingplichtige overeenkomstig de

artikelen 289 bis /1 tot en met 289 bis /8, via automatische uitwisseling

mee aan de bevoegde autoriteiten van alle andere lidstaten.

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid

mee te delen gegevens zijn de volgende, voor zover van toepassing:

1° de identificatiegegevens van intermediairs, en relevante

belastingplichtigen, bedoeld in artikel 289 bis /1, 4° en 5°, met

uitzondering van intermediairs die op grond van het juridisch

beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig

###### Art. 289. bis /7, met inbegrip van hun naam, geboortedatum en -

plaats (in het geval van een natuurlijk persoon), fiscale woonplaats,

fiscaal identificatienummer, en, in voorkomend geval, van de

personen die overeenkomstig paragraaf 2, 21° een verbonden

onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in

###### Art. 289. bis /2 op grond waarvan de grensoverschrijdende

constructie gemeld moet worden;

3° een samenvatting van de inhoud van de meldingsplichtige

grensoverschrijdende constructie, met onder meer de benaming

waaronder zij algemeen bekend staat, indien voorhanden, en een

tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of

beroepsgeheim of een fabrieks- of handelswerkwijze, of van

inlichtingen waarvan de onthulling in strijd zou zijn met de openbare

orde;

4° de datum waarop de eerste stap voor de implementatie van de

meldingsplichtige grensoverschrijdende constructie is of zal worden

ondernomen;

5° nadere bijzonderheden van de nationale bepalingen die aan de

meldingsplichtige grensoverschrijdende constructie ten grondslag

liggen;

6° de waarde van de meldingsplichtige grensoverschrijdende

constructie;

7° de lidstaat van de relevante belastingbetaler(s) en eventuele

andere lidstaten waarop de meldingsplichtige grensoverschrijdende

constructie naar alle waarschijnlijkheid van invloed zal zijn;

8° de identificatiegegevens van andere personen in een lidstaat, op

wie de meldingsplichtige grensoverschrijdende constructie naar alle

waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met

welke lidstaten deze personen verbonden zijn.

De automatische uitwisseling geschiedt binnen één maand te

rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn

verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020

meegedeeld.

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze

paragraaf, worden niet medegedeeld aan de Europese Commissie.

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028,

bevat  de  mededeling  van  de  gegevens  betreffende  de

grensoverschrijdende regelingen het fiscaal identificatienummer van

de personen bepaald in het tweede lid, 8°.

§ 7 . De Belgische bevoegde autoriteit verstrekt spontaan, in elk van

de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de

buitenlandse bevoegde autoriteit:

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen

dat in de andere lidstaat een derving van belasting kan bestaan;

3° transacties tussen een belastingplichtige in België en een

belastingplichtige in een andere lidstaat worden over één of meer

andere landen geleid, op zodanige wijze dat daardoor in één van beide

of in beide lidstaten een belastingbesparing kan ontstaan;

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen

dat er belastingbesparing kan ontstaan door een kunstmatige

verschuiving van winsten binnen een groep van ondernemingen;

5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen

door een buitenlandse bevoegde autoriteit, hebben informatie

opgeleverd die voor de vaststelling van de belastingschuld in die

andere lidstaat toereikend, ter zake dienend en niet overmatig is.

De Belgische bevoegde autoriteit kan een buitenlandse bevoegde

autoriteit spontaan alle inlichtingen meedelen waarvan zij kennis

heeft en die voor deze buitenlandse bevoegde autoriteit toereikend,

ter zake dienend en niet overmatig zijn.

De in het eerste lid bedoelde inlichtingen worden door de Belgische

bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand

nadat deze beschikbaar worden, aan de buitenlandse bevoegde

autoriteit van elke betrokken lidstaat verstrekt.

§ 8 . De ontvangst van de in § 7 bedoelde inlichtingen wordt door de

Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen

zeven werkdagen na ontvangst, indien mogelijk langs elektronische

weg, aan de verstrekkende buitenlandse bevoegde autoriteit

bevestigd.

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in

§ 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde

autoriteit verzoeken dat door eerstgenoemde gemachtigde

ambtenaren onder de voorwaarden die zijn vastgesteld door de

buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren

waar de administratieve autoriteiten van de lidstaat taken vervullen;

2° aanwezig zijn bij administratieve onderzoeken die worden

uitgevoerd op het grondgebied van de buitenlandse bevoegde

autoriteit;

voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren

aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen

door middel van elektronische communicatiemiddelen, kunnen zij

personen  ondervragen  en  bescheiden  onderzoeken,  onder

voorbehoud van de door de buitenlandse bevoegde autoriteit

gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde

inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische

bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde

ambtenaren onder de voorwaarden die zijn vastgesteld door de

Belgische bevoegde autoriteit mogen:

1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn

taken vervult;

2° aanwezig zijn bij administratieve onderzoeken die worden

uitgevoerd op Belgisch grondgebied;

3° deelnemen aan de administratieve onderzoeken die worden

uitgevoerd op Belgisch grondgebied, met gebruikmaking van

elektronische communicatiemiddelen, in voorkomend geval.

De Belgische bevoegde autoriteit antwoordt op het overeenkomstig

de eerste alinea ingediende verzoek binnen een termijn van 60 dagen

na ontvangst van het verzoek, om haar instemming te bevestigen of

haar gemotiveerde weigering aan de buitenlandse bevoegde

autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden

waartoe de ambtenaren van de Belgische bevoegde autoriteit

toegang hebben, ontvangen de ambtenaren van de verzoekende

autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn

tijdens een administratief onderzoek of daaraan deelnemen met

gebruikmaking van elektronische communicatiemiddelen, mogen zij

personen ondervragen en bescheiden onderzoeken, onder de

voorwaarden die zijn vastgesteld door de Belgische bevoegde

autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking

heeft, om de controlemaatregelen van de ambtenaren van de

verzoekende autoriteit na te leven, wordt door de Belgische bevoegde

De door de verzoekende lidstaat gemachtigde ambtenaren die

overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds

een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en

hun officiële hoedanigheid worden vermeld.

§ 11 . In de gevallen waarin België met één of meer lidstaten

overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of

meer personen te wier aanzien zij een gezamenlijk of complementair

belang hebben, controles te verrichten en de aldus verkregen

inlichtingen uit te wisselen, is deze § van toepassing.

De Belgische bevoegde autoriteit bepaalt autonoom welke personen

zij voor een gelijktijdige controle wil voorstellen. Zij deelt de

buitenlandse bevoegde autoriteit van de betrokken lidstaten met

opgave van redenen mee welke dossiers zij voor een gelijktijdige

controle voorstelt. Zij bepaalt binnen welke termijn de controle moet

plaatsvinden.

Wanneer aan de Belgische bevoegde autoriteit een gelijktijdige

controle wordt voorgesteld, beslist zij of ze aan de gelijktijdige

controle wenst deel te nemen. Zij doet de buitenlandse bevoegde

autoriteit die de controle voorstelt een bevestiging van deelname of

een gemotiveerde weigering toekomen binnen een termijn van 60

dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan

die wordt belast met de leiding en de coördinatie van de controle.

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de

Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit

te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het

verzoek om een gezamenlijke audit binnen een termijn van 60 dagen,

te rekenen vanaf de ontvangst van het verzoek en motiveert haar

beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en

gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd

door de bevoegde autoriteit van de verzoekende lidstaat, door de

Belgische bevoegde autoriteit, en in voorkomend geval, door de

bevoegde autoriteiten van de andere aangezochte lidstaten en in

overeenstemming met de Belgische wetgeving en procedurele

voorschriften. De Belgische bevoegde autoriteit wijst een

vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en

de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die

deelnemen aan de gezamenlijke audit op Belgisch grondgebied,

de bevoegdheden die hun krachtens de wetgeving van hun lidstaat

zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die

deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd

om personen te ondervragen en bescheiden te onderzoeken in

samenspraak met de ambtenaren van de Belgische bevoegde

autoriteit, met inachtneming van de in België bepaalde procedurele

regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de

activiteiten van de gezamenlijke audit is verzameld, worden

beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde

juridische voorwaarden als in het geval van een klassieke audit,

uitgevoerd in België door Belgische ambtenaren, onder meer in de

loop van een bezwaar-, herzienings- of beroepsprocedures.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, genieten personen die aan een gezamenlijke

audit worden onderworpen of erdoor worden geraakt, dezelfde

rechten en hebben ze dezelfde plichten als in het geval van een

klassieke audit waaraan alleen Belgische ambtenaren deelnemen,

onder meer in de loop van een bezwaar-, herzienings- of

beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van

een of meer lidstaten een gezamenlijke audit verrichten, trachten zij

het eens te worden over de feiten en omstandigheden die relevant

zijn voor de gezamenlijke audit, en streven zij naar overeenstemming

over de fiscale positie van de geaudite persoon of personen op basis

van de resultaten van de gezamenlijke audit. De bevindingen van de

gezamenlijke audit worden neergelegd in een eindverslag. Punten

waarover de bevoegde autoriteiten het eens zijn, worden in de

conclusies van het eindverslag opgenomen en worden in aanmerking

genomen in de relevante instrumenten die de bevoegde autoriteiten

van de deelnemende lidstaten naar aanleiding van die gezamenlijke

audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het

resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het

eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

Gezamenlijke audits worden op vooraf overeengekomen en

gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd

door de betrokken bevoegde autoriteiten, en in overeenstemming

met de wetgeving en de procedurele voorschriften van de lidstaat

waar de activiteiten van de gezamenlijke audit plaatsvinden.

De rechten en plichten van de Belgische ambtenaren die deelnemen

aan de gezamenlijke audit op het grondgebied van een andere

lidstaat, worden vastgesteld overeenkomstig de wetgeving van die

lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de

Belgische ambtenaren geen bevoegdheden uit die verder zouden

gaan dan de bevoegdheden die hun krachtens de Belgische

wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het

grondgebied van een andere lidstaat, kan het bewijsmateriaal dat

tijdens de activiteiten van de gezamenlijke audit is verzameld, worden

beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde

juridische voorwaarden als in het geval van een klassieke audit

uitgevoerd in België door Belgische ambtenaren.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van

een of meerdere andere lidstaten een gezamenlijke audit verrichten,

trachten zij het eens te worden over de feiten en omstandigheden die

relevant zijn voor de gezamenlijke audit, en streven zij naar

overeenstemming over de fiscale positie van de geaudite persoon of

personen op basis van de resultaten van de gezamenlijke audit. De

bevindingen van de gezamenlijke audit worden neergelegd in een

eindverslag. De punten waarover de bevoegde autoriteiten het eens

zijn, worden in de conclusies van het eindverslag opgenomen en

worden in aanmerking genomen in de relevante instrumenten die de

bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding

van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het

resultaat van de gezamenlijke audit en krijgen een kopie van het

eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 12 . De Belgische bevoegde autoriteit kan een verzoek aan een

buitenlandse bevoegde autoriteit richten tot kennisgeving aan de

geadresseerde, overeenkomstig de in de aangezochte lidstaat

geldende voorschriften voor de kennisgeving van soortgelijke akten,

van alle door de Belgische administratieve overheden afgegeven

akten en besluiten die betrekking hebben op de toepassing in België

van wetgeving betreffende registratie-, hypotheek- en griffierechten.

geadresseerde, en het onderwerp van de akte of het besluit waarvan

de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde

autoriteit slechts gedaan indien de kennisgeving van de akten niet

volgens de Belgische regels kan geschieden, of buitensporige

problemen zou veroorzaken. De Belgische bevoegde autoriteit kan

een document, met een aangetekende zending of langs elektronische

weg, rechtstreeks ter kennis brengen aan een persoon op het

grondgebied van een andere lidstaat.

§ 13 . Op verzoek van een buitenlandse bevoegde autoriteit gaat de

Belgische bevoegde autoriteit, overeenkomstig de Belgische

voorschriften voor de kennisgeving van soortgelijke akten, over tot

kennisgeving aan de geadresseerde van alle door de administratieve

overheden van de verzoekende lidstaat afgegeven akten en besluiten

die betrekking hebben op de toepassing op haar grondgebied van

wetgeving betreffende registratie-, hypotheek- en griffierechten.

De Belgische bevoegde autoriteit stelt de verzoekende autoriteit

onverwijld in kennis van het aan het verzoek gegeven gevolg en, in het

bijzonder, van de datum waarop de akte of het besluit aan de

geadresseerde ter kennis is gebracht.

§ 14 . Indien een buitenlandse bevoegde autoriteit inlichtingen

overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding

betreffende  de  ontvangen  inlichtingen  verzoekt,  doet  de

ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen

aan de Belgische voorschriften inzake beroepsgeheim en

gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie

maanden nadat het resultaat van het gebruik van de verlangde

inlichtingen bekend is, een terugmelding aan de buitenlandse

bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar,

overeenkomstig bilateraal overeengekomen praktische afspraken,

een terugmelding over de automatische inlichtingenuitwisseling naar

de betrokken lidstaten.

§ 15 . De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7

inlichtingen heeft verstrekt, kan de ontvangende buitenlandse

bevoegde autoriteit om terugmelding betreffende de ontvangen

inlichtingen verzoeken.

§ 16 . De Belgische verbindingsdienst of de Belgische bevoegde

ambtenaar die een verzoek om samenwerking ontvangt dat een

optreden vereist buiten de hem krachtens de Belgische wetgeving of

kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat

het verzoek aan het Belgisch centraal verbindingsbureau is

doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in

enigerlei  vorm  of  volgens  dit  artikel,  vallen  onder  de

geheimhoudingsplicht en genieten de bescherming waarin het

nationale recht van de ontvangende lidstaat met betrekking tot

soortgelijke inlichtingen voorziet.

Deze inlichtingen mogen worden gebruikt:  Ces informations peuvent servir :

1° voor de vaststelling, de toepassing en de handhaving van het

nationale recht met betrekking tot de in artikel 2 van de richtlijn

bedoelde belastingen, alsmede de btw, andere indirecte belastingen,

douanerechten, de bestrijding van het witwassen van geld en van de

financiering van terrorisme;

2° voor de vestiging en de invordering van de andere belastingen en

rechten met betrekking tot artikel 3 van de wet van 9 januari 2012

houdende omzetting van Richtlijn 2010/24/EU van de Raad van 16

maart 2010 betreffende de wederzijdse bijstand inzake de

invordering van schuldvorderingen die voortvloeien uit belastingen,

rechten en andere maatregelen, en voor het vestigen en invorderen

van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures

die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op

de fiscale wetgeving, onverminderd algemene regels en wettelijke

bepalingen die de rechten van beklaagden en getuigen in het kader

van dergelijke procedures beheersen.

Met de toestemming van de buitenlandse bevoegde autoriteit die de

inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor

zover dat toegelaten is door de Belgische wetgeving, kunnen de

ontvangen inlichtingen en documenten ontvangen van deze autoriteit

worden gebruikt voor andere doeleinden dan deze bedoeld in het

tweede lid.

De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en

documenten zonder de in de derde lid van deze paragraaf bedoelde

toestemming ook gebruiken voor elk doel dat onder een op artikel 215

van het Verdrag betreffende de werking van de Europese Unie

gebaseerde handeling valt en deze daartoe delen met de bevoegde

autoriteit die verantwoordelijk is voor beperkende maatregelen in de

betrokken lidstaat.

de in het tweede lid beoogde doelen, mag de inlichtingen aan deze

autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit

van de inlichtingen verstrekkende lidstaat in kennis stelt van haar

voornemen om die inlichtingen met een derde lidstaat te delen en op

voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel

vastgelegde regels en procedures. De inlichtingen verstrekkende

lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na

de datum van ontvangst van de kennisgeving van de lidstaat die de

inlichtingen wenst te delen.

§ 18 . De Belgische bevoegde autoriteit kan het gebruik toestaan van

de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in

de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid,

bedoelde doeleinden. De Belgische bevoegde autoriteit verleent

toestemming indien de inlichtingen in België voor soortgelijke

doeleinden kunnen worden gebruikt.

De Belgische bevoegde autoriteit deelt aan de bevoegde autoriteiten

van alle andere lidstaten een lijst mee van andere dan in paragraaf 1

bedoelde doeleinden waarvoor overeenkomstig haar nationale recht,

de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde

autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen

inlichtingen en bescheiden zonder de in het eerste lid bedoelde

toestemming gebruiken voor alle doeleinden die de Belgische

bevoegde autoriteit heeft opgenoemd.

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de

in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit

België die door een buitenlandse bevoegde autoriteit aan een

buitenlandse bevoegde autoriteit van een derde lidstaat werden

doorgegeven, in die derde lidstaat toestaan.

§ 19 . Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht

de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit

alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan

aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te

komen.

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde

autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op

voorwaarde dat de buitenlandse bevoegde autoriteit eerst de

inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in

de gegeven omstandigheden kon aanspreken zonder dat het

beoogde resultaat in het gedrang dreigt te komen.

§ 20 . Het is de Belgische bevoegde autoriteit niet toegelaten

onderzoek in te stellen of inlichtingen te verstrekken wanneer de

De Belgische bevoegde autoriteit kan weigeren inlichtingen te

verstrekken indien:

1° de verzoekende lidstaat, op juridische gronden, soortgelijke

inlichtingen niet kan verstrekken;

2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-,

nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze,

of indien het inlichtingen betreft waarvan de onthulling in strijd zou

zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee

op welke gronden zij het verzoek om inlichtingen afwijst.

§ 21 . De Belgische bevoegde autoriteit wendt de middelen aan

waarover zij beschikt om de gevraagde inlichtingen te verzamelen,

zelfs indien zij de inlichtingen niet voor eigen belastingdoeleinden

nodig heeft. Deze verplichting geldt onverminderd § 20, eerste en

tweede lid, die, wanneer er een beroep op wordt gedaan, in geen geval

zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te

verstrekken uitsluitend omdat België geen binnenlands belang bij

deze inlichtingen heeft.

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat

de Belgische bevoegde autoriteit kan weigeren inlichtingen te

verstrekken, uitsluitend op grond dat deze berusten bij een bank, een

andere financiële instelling, een gevolmachtigde of een persoon die

als vertegenwoordiger of trustee optreedt, of dat zij betrekking

hebben op eigendomsbelangen in een persoon.

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit

weigeren de gevraagde inlichtingen toe te zenden indien deze

betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de

toezending van de inlichtingen geweigerd had kunnen worden op

grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom

was verzocht vóór 11 maart 2011.

§ 22. Indien de Belgische overheid voorziet in een samenwerking met

een derde land welke verder reikt dan de bij de richtlijn geregelde

samenwerking, kan de Belgische overheid de verderreikende

samenwerking niet weigeren aan een andere lidstaat die met haar

deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken

die zijn ingediend op grond van § 4, alsook de antwoorden op grond

van een door de Commissie goedgekeurd standaardformulier. Er

mogen rapporten, certificaten en andere bescheiden, of andere voor

eensluidend verklaarde afschriften of uittreksels daarvan bij de

standaardformulieren gevoegd worden.

De in het eerste lid bedoelde standaardformulieren bevatten ten

minste de volgende gegevens, die de verzoekende autoriteit moet

verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle

is ingesteld en, in het geval van vragen betreffende een groep zoals

bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;

b) het fiscale doel van de gevraagde informatie.  b) la finalité fiscale des informations demandées.

De Belgische bevoegde autoriteit kan, voor zover bekend en in

overeenstemming met de ontwikkeling van de internationale situatie,

de namen en adressen verstrekken van alle personen van wie er

redenen zijn om aan te nemen dat ze in het bezit zijn van de gevraagde

informatie, alsook alle elementen die het verzamelen van informatie

door de aangezochte autoriteit kunnen vergemakkelijken.

De  spontane  gegevensuitwisseling  en  de  desbetreffende

ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8,

verzoeken tot administratieve kennisgeving op grond van §§ 12 en

13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op

grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden

overgemaakt door middel van de door de Commissie goedgekeurde

standaardformulieren.

De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1

wordt verricht in een geautomatiseerd standaardformaat dat

ontworpen is om die automatische uitwisseling te vergemakkelijken

en dat is goedgekeurd door de Commissie.

§ 24 . De krachtens dit artikel verstrekte inlichtingen worden voor

zover mogelijk verzonden langs elektronische weg, via het CCN-

netwerk.

Het verzoek om samenwerking, waaronder het verzoek tot

kennisgeving en de bijgevoegde bescheiden kunnen in elke door de

aangezochte en de verzoekende autoriteit overeengekomen taal zijn

gesteld. Slechts in bijzondere gevallen en mits het verzoek met

redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken

het verzoek vergezeld te laten gaan van een vertaling in één van de

officiële talen van België.

gegevensbestand betreffende de administratieve samenwerking op

belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter

beschikking gesteld door de Commissie uiterlijk op 31 december

2017. De Belgische bevoegde autoriteiten hebben toegang tot de in

dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand

operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde

automatische uitwisseling van gegevens, volgens lid 1 van deze

paragraaf en de toepasselijke praktische modaliteiten.

§ 25 . De Belgische bevoegde autoriteit die van een derde land

inlichtingen ontvangt welke naar verwachting van belang zijn voor

haar administratie en de handhaving van de Belgische wetgeving

betreffende registratie-, hypotheek- en griffierechten, kan deze

inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten

van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan

elke buitenlandse bevoegde autoriteit die erom verzoekt, mits dat

krachtens een overeenkomst met dat derde land is toegestaan.

De Belgische bevoegde autoriteit kan, met inachtneming van de wet

van 8 december 1992 tot bescherming van de persoonlijke

levenssfeer ten opzichte van de verwerking van persoonsgegevens

en de wet van 3 augustus 2012 houdende bepalingen betreffende de

verwerking van persoonsgegevens door de Federale Overheidsdienst

Financiën in het kader van zijn opdrachten, de overeenkomstig dit

artikel ontvangen inlichtingen doorgeven aan een derde land, op

voorwaarde dat aan elk van de volgende voorwaarden is voldaan:

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de

inlichtingen afkomstig zijn, heeft daarin toegestemd;

b) het derde land heeft zich ertoe verbonden de medewerking te

verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent

het ongeoorloofde of onwettige karakter van verrichtingen die blijken

in strijd te zijn met of een misbruik te vormen van de

belastingwetgeving.

§  26.  Rapporterende  financiële  instellingen,  intermediairs,

rapporterende platformexploitanten en de Belgische bevoegde

autoriteit worden als verwerkingsverantwoordelijken beschouwd

wanneer zij, alleen of gezamenlijk, de doelen en middelen van de

verwerking van persoonsgegevens bepalen in de zin van Verordening

(EU) 2016/679 van het Europees Parlement en de Raad van 27 april

2016 betreffende de bescherming van natuurlijke personen in

verband met de verwerking van persoonsgegevens en betreffende

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in

kennis van elke gegevensinbreuk en alle daaropvolgende

corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen

met de lidstaat of de lidstaten waar de gegevensinbreuk heeft

plaatsgevonden, schorsen door de Commissie en de betrokken

lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een

dergelijke schorsing wordt onmiddellijk van kracht.

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de

Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de

Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van

de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn,

indien de gegevensinbreuk niet onmiddellijk en op passende wijze

onder controle kan worden gebracht. Op een dergelijk verzoek schorst

de Commissie de toegang van die lidstaat of lidstaten tot het CCN-

netwerk voor de toepassing van de richtlijn.

De Belgische bevoegde autoriteit stelt, in geval van een

gegevensinbreuk, de Commissie op de hoogte wanneer zij deze

inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie

verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is

verholpen, geeft de Commissie pas na die verificatie de betrokken

lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de

toepassing van de richtlijn.

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in

het centrale gegevensbestand of het CCN-netwerk plaatsvindt die

nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen

door de lidstaten via het CCN-netwerk, stelt de Commissie de

lidstaten  zonder  onnodige  vertraging  in  kennis  van  de

gegevensinbreuk en van eventuele corrigerende maatregelen die zijn

genomen. Zulke corrigerende maatregelen kunnen inhouden dat de

toegang tot het centrale gegevensbestand of het CCN-netwerk voor

de toepassing van de richtlijn wordt geschorst totdat de

gegevensinbreuk is verholpen.

----------

Nota:  Note :

- in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.  - dans le § 6/1, al. 1 er , 5°, a) et i) : lire « 1° et 3° » au lieu de « 1° et 4° ».

- in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.  - dans le § 6/1, al. 2 : lire « 5°, a) et i) » au lieu de « 6°, a) et k) ».

- in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.  - dans le § 6/3, al. 2, 1° : lire « paragraphe 2, 18° » au lieu de « paragraphe 2, 21° ».

- in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.

-----

16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))

§ 1 . Dit artikel legt de voorschriften en procedures vast voor de

samenwerking tussen België en de andere lidstaten van de Europese

Unie met het oog op de uitwisseling van inlichtingen die naar

verwachting van belang zijn voor de administratie en de handhaving

van de nationale wetgeving van alle lidstaten met betrekking tot de

registratie-, hypotheek- en griffierechten.

Dit artikel legt tevens de bepalingen vast voor de elektronische

uitwisseling van de in het eerste lid bedoelde inlichtingen.

Dit artikel laat de toepassing van de regels inzake wederzijdse

rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de

verplichtingen van de lidstaten inzake ruimere administratieve

samenwerking, welke voortvloeien uit andere rechtsinstrumenten,

waaronder bilaterale en multilaterale overeenkomsten.

§ 2 . Voor de toepassing van dit artikel wordt verstaan onder:  § 2. Aux fins du présent article, on entend par :

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari

2011 betreffende de administratieve samenwerking op het gebied

van de belastingen en tot intrekking van richtlijn 77/799/EEG;

2° "lidstaat": een lidstaat van de Europese Unie;  2° « Etat membre » : un Etat membre de l’Union Européenne ;

3° "centraal verbindingsbureau": het bureau dat als zodanig is

aangewezen door de bevoegde autoriteit en belast is met de primaire

zorg voor de contacten met de andere lidstaten op het gebied van de

administratieve samenwerking;

4° "verbindingsdienst": elk ander bureau dan het centraal

verbindingsbureau dat als zodanig is aangewezen door de bevoegde

autoriteit om op grond van dit artikel rechtstreeks inlichtingen uit te

wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel

gemachtigd is door de bevoegde autoriteit om rechtstreeks

inlichtingen uit te wisselen;

6° "Belgische bevoegde autoriteit": de door België als zodanig

aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de

Belgische  verbindingsdiensten  en  de  Belgische  bevoegde

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere

dan België, als zodanig aangewezen autoriteit. Het centraal

verbindingsbureau, de verbindingsdiensten en de bevoegde

ambtenaren van deze lidstaat worden eveneens als buitenlandse

bevoegde autoriteit bij delegatie beschouwd;

8° "verzoekende autoriteit": het centraal verbindingsbureau, een

verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die

namens de Belgische of een buitenlandse bevoegde autoriteit om

bijstand verzoekt;

9° "aangezochte autoriteit": het centraal verbindingsbureau, een

verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die

namens de Belgische of een buitenlandse bevoegde autoriteit om

bijstand wordt verzocht;

10° "administratief onderzoek": alle door de lidstaten bij het vervullen

van hun taken verrichte controles, onderzoeken en acties ter

waarborging van de juiste toepassing van de belastingwetgeving;

11° "automatische uitwisseling":  11° « échange automatique » :

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de

systematische mededeling met regelmatige, vooraf vastgestelde

tussenpozen zonder voorafgaand verzoek van vooraf bepaalde

inlichtingen aan een andere lidstaat;

b) voor de toepassing van alle andere bepalingen van dit artikel,

andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3,

de systematische mededeling van vooraf bepaalde inlichtingen

verstrekt overeenkomstig de punten a) en b)

12° "spontane uitwisseling": het niet-systematisch, te eniger tijd en

ongevraagd verstrekken van inlichtingen aan een andere lidstaat;

13° "persoon":  13° « personne » :

a. een natuurlijk persoon;  a. une personne physique ;

b. een rechtspersoon;  b. une personne morale ;

c. indien de geldende wetgeving in die mogelijkheid voorziet, een

vereniging van personen die bevoegd is rechtshandelingen te

verrichten, maar niet de status van rechtspersoon bezit; of

belastingen in de zin van de richtlijn zijn onderworpen;

14° "langs elektronische weg": door middel van elektronische

apparatuur voor gegevensverwerking - met inbegrip van digitale

compressie - en gegevensopslag, met gebruikmaking van kabels,

radio, optische technologie of andere elektromagnetische middelen;

15°  "CCN-netwerk":  het  op  het  gemeenschappelijke

communicatienetwerk gebaseerde gemeenschappelijke platform dat

de Europese Unie heeft ontwikkeld voor het elektronische

berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied

van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk

akkoord, elke mededeling of enig ander instrument of handeling met

soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of

hernieuwd, in het kader van een belastingcontrole, en die aan de

volgende cumulatieve voorwaarden voldoen:

a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht

of deze beslissingen effectief gebruikt worden;

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon

of een groep van personen, en voor zover deze persoon of deze groep

van personen er zich kan op beroepen;

c) betreft de interpretatie of toepassing van een wettelijke of

administratieve bepaling betreffende de handhaving of de toepassing

van dit Wetboek en de met de registratie-, hypotheek- en

griffierechten verband houdende autonome bepalingen;

d) heeft betrekking op een grensoverschrijdende verrichting en  d) se rapporte à une opération transfrontière et

e) is tot stand gekomen voorafgaand aan de indiening van een

belastingaangifte voor het tijdvak waarin de verrichting of reeks

verrichtingen of de activiteiten hebben plaatsgevonden.

17° "grensoverschrijdende verrichting" als vermeld in de bepaling

onder 16°: een verrichting of reeks van verrichtingen die voldoen aan

een of meer van de volgende voorwaarden:

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van

verrichtingen  fiscaal  inwoners  van  België  zijn  dat  de

grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt,

gewijzigd of hernieuwd

c)  de  verrichtingen  of  reeks  van  verrichtingen  een

grensoverschrijdend effect hebben.

18° "verbonden onderneming", voor de toepassing van paragraaf

6/3: een persoon die gelieerd is met een andere persoon op ten

minste één van de volgende wijzen:

a) een persoon neemt deel aan de leiding van een andere persoon

waarbij hij invloed van betekenis kan uitoefenen op die andere

persoon;

b) een persoon neemt deel aan de zeggenschap over een andere

persoon door middel van een deelneming van meer dan 25 % van de

stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon

door middel van een eigendomsrecht van, rechtstreeks of middellijk,

meer dan 25 % van het kapitaal;

d) een persoon heeft recht op 25 % of meer van de winsten van een

andere persoon.

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en

met d), aan de leiding van, aan de zeggenschap over of in het kapitaal

of de winsten van dezelfde persoon, worden alle betrokken personen

als verbonden ondernemingen beschouwd.

Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met

d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de

winsten van meer dan één persoon, worden alle betrokken personen

als verbonden ondernemingen beschouwd.

Voor de toepassing van dit punt wordt een persoon die met

betrekking tot de stemrechten of het kapitaalbezit van een entiteit

samen met een andere persoon optreedt, beschouwd als houder van

een deelneming in alle stemrechten of het volledige kapitaalbezit dat

die andere persoon in de genoemde entiteit heeft.

Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c)

is voldaan door vermenigvuldiging van de deelnemingspercentages

door de opeenvolgende niveaus heen. Een persoon die meer dan 50

% van de stemrechten houdt, wordt geacht 100 % te houden.

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in

de rechte lijn worden behandeld als één persoon.

lidstaten wordt uitgevoerd, en verband houdt met een of meer

personen van gezamenlijk of complementair belang voor de

bevoegde autoriteiten van die lidstaten;

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot

vernietiging, verlies, wijziging of elk voorval van ongepaste of

ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen,

met inbegrip van, maar niet beperkt tot, persoonsgegevens die

worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg

van opzettelijke onwettige handelingen, nalatigheid of ongevallen.

Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid,

de beschikbaarheid en de integriteit van gegevens.

§ 3 . De Belgische bevoegde autoriteit wisselt met de buitenlandse

bevoegde autoriteiten inlichtingen uit.

§ 4 . Met betrekking tot een specifiek geval kan de Belgische bevoegde

autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de

eerste § vermelde inlichtingen die deze in haar bezit heeft of naar

aanleiding van een administratief onderzoek verkregen heeft, te

verstrekken. Het verzoek kan een met redenen omkleed verzoek om

een bepaald administratief onderzoek in te stellen, omvatten.

De Belgische bevoegde autoriteit kan de aangezochte autoriteit

verzoeken haar de originele stukken over te maken.

§ 5 . De Belgische bevoegde autoriteit verstrekt op verzoek van een

buitenlandse bevoegde autoriteit met betrekking tot een specifiek

geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft

of naar aanleiding van een administratief onderzoek verkregen heeft,

dat werd ingesteld om die inlichtingen te verkrijgen.

In voorkomend geval deelt de Belgische bevoegde autoriteit de

verzoekende autoriteit mee op welke gronden zij een administratief

onderzoek niet noodzakelijk acht.

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten

van het gevraagde administratief onderzoek gaat de Belgische

bevoegde autoriteit te werk volgens dezelfde procedures als

handelde zij uit eigen beweging of op verzoek van een andere

Belgische instantie.

Op specifiek verzoek van de verzoekende autoriteit verstrekt de

Belgische bevoegde autoriteit de originele stukken, tenzij de

Belgische voorschriften zich hiertegen verzetten.

autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij

deze binnen twee maanden. In bijzondere gevallen kunnen de

Belgische bevoegde autoriteit en de verzoekende autoriteit een

andere termijn overeenkomen.

De ontvangst van het verzoek wordt door de Belgische bevoegde

autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval

uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs

elektronische weg, bevestigd.

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk

een maand na ontvangst van het verzoek, aan de verzoekende

autoriteit weten welke tekortkomingen het verzoek vertoont en

preciseert welke aanvullende achtergrondinformatie zij verlangt. In

dit geval gaan de in het vijfde lid gestelde termijnen in op de datum

waarop de Belgische bevoegde autoriteit de aanvullende informatie

ontvangt.

Indien de Belgische bevoegde autoriteit niet binnen de gestelde

termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor

onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van

het verzoek, aan de verzoekende autoriteit mee, met vermelding van

de datum waarop zij meent aan het verzoek te kunnen voldoen. Deze

termijn mag niet langer zijn dan zes maanden te rekenen vanaf de

datum van ontvangst van het verzoek.

Indien de Belgische bevoegde autoriteit niet over de gevraagde

inlichtingen beschikt en niet aan het verzoek om inlichtingen kan

voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt

zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand

na ontvangst van het verzoek, aan de verzoekende autoriteit mee.

§ 5/1. Wat betreft een in paragraaf 4 en in paragraaf 5 bedoeld

verzoek worden de verzochte inlichtingen geacht van verwacht

belang te zijn indien op het ogenblik van het verzoek de verzoekende

autoriteit van oordeel is dat er overeenkomstig haar nationale

wetgeving een redelijke mogelijkheid bestaat dat de verzochte

inlichtingen van belang zullen zijn voor de belastingaangelegenheden

van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of

anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van

het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen,

verstrekt de verzoekende autoriteit ten minste de volgende

inlichtingen aan de aangezochte autoriteit:

b) een specificering van de inlichtingen die nodig zijn voor de

uitvoering of handhaving van haar nationale recht.

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op

een groep belastingplichtigen die niet individueel kunnen worden

geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op

basis van een gemeenschappelijke reeks kenmerken.

In dergelijke gevallen, verstrekt de verzoekende autoriteit de

volgende informatie aan de aangezochte autoriteit:

a) een gedetailleerde beschrijving van de groep;  a) une description détaillée du groupe ;

b) een toelichting bij de toepasselijke wetgeving en bij de feiten op

basis waarvan redelijkerwijze vermoed kan worden dat de

belastingplichtigen in de groep de toepasselijke wetgeving niet

hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen

zouden bijdragen tot het bepalen van de mate waarin de

belastingplichtigen in de groep aan hun verplichtingen voldoen;

d) in voorkomend geval, feiten en omstandigheden die verband

houden met de tussenkomst van een derde die actief heeft

bijgedragen tot de mogelijke niet-naleving van de toepasselijke

wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse

bevoegde autoriteit automatisch alle inlichtingen waarover zij ten

aanzien van ingezetenen van die andere lidstaat beschikt inzake de

volgende specifieke inkomsten- en vermogenscategorieën, op te

vatten in de zin van de Belgische wetgeving:

a) inkomen uit een dienstbetrekking;  a) revenus d'emploi ;

b) tantièmes en presentiegelden;  b) tantièmes et jetons de présence ;

c) levensverzekeringsproducten die niet vallen onder andere

Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch

onder soortgelijke voorschriften;

d) pensioenen;  d) pensions ;

e) eigendom van en inkomsten uit onroerend goed;  e) propriété et revenus de biens immobiliers ;

van  inkomsten  uit  dividenden  die  zijn  vrijgesteld  van

vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn

2011/96/EU van de Raad.

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de

verstrekking van de in de eerste alinea genoemde inlichtingen het

door de lidstaat van verblijf afgegeven fiscaal identificatienummer

(TIN) van ingezetenen.

België stelt de Commissie jaarlijks in kennis van ten minste twee

inkomsten- en vermogenscategorieën die zijn opgenomen in de

eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over

ingezetenen van een andere lidstaat.

België stelt de Commissie vóór 1 januari 2026 in kennis van ten

minste vijf categorieën die zijn opgenomen in het eerste lid, ten

aanzien waarvan de bevoegde autoriteit van elke andere lidstaat

automatisch inlichtingen verstrekt over ingezetenen van die andere

lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken

die ingaan op of na 1 januari 2026.

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen

zes maanden na het verstrijken van het kalenderjaar in de loop

waarvan de inlichtingen beschikbaar zijn geworden.

"Beschikbare inlichtingen" betekent inlichtingen die zich in de

belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden

en die opvraagbaar zijn overeenkomstig de procedures voor het

verzamelen en verwerken van inlichtingen in die lidstaat.

§ 6/1 . In het kader van de verplichte automatische uitwisseling van

inlichtingen  over  grensoverschrijdende  voorafgaande  fiscale

beslissingen, zijn de voorwaarden de volgende:

1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van

deze paragraaf, verstrekt de Belgische bevoegde autoriteit

automatisch inlichtingen aan de bevoegde autoriteiten van alle

andere lidstaten en de Europese Commissie, overeenkomstig de

volgens § 24 vastgestelde van toepassing zijnde praktische

modaliteiten wanneer een grensoverschrijdende voorafgaande

beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december

2016.

2°  de  Belgische  bevoegde  autoriteit  verstrekt  eveneens,

overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde

praktische modaliteiten, aan de bevoegde autoriteiten van alle andere

jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in

de bepaling onder 6° van deze paragraaf.

Indien de grensoverschrijdende voorafgaande fiscale beslissingen

werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en

31 december 2013, worden deze inlichtingen verstrekt op

voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.

Als grensoverschrijdende voorafgaande fiscale beslissingen werden

verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31

december 2016, worden die inlichtingen verstrekt ongeacht of die

grensoverschrijdende voorafgaande beslissingen al dan niet nog

geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin

een voorafgaande grensoverschrijdende ruling betrekking heeft op

belastingaangelegenheden van een of meer natuurlijke personen,

tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1

januari 2026 is afgegeven, gewijzigd of hernieuwd, en:

a) het bedrag van de transactie of reeks transacties van de

voorafgaande grensoverschrijdende ruling groter is dan 1.500.000

euro (of het equivalent daarvan in een andere valuta), indien dat

bedrag wordt vermeld in de voorafgaande grensoverschrijdende

ruling, of;

b) de voorafgaande grensoverschrijdende ruling bepaalt of een

persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de

ruling afgeeft.

Voor de toepassing van punt a), en onverminderd het in de

voorafgaande grensoverschrijdende ruling bedoelde bedrag, omvat

het bedrag van de voorafgaande grensoverschrijdende ruling bij een

reeks transacties met betrekking tot verschillende goederen,

diensten of activa, de totale onderliggende waarde. De bedragen

worden niet geaggregeerd indien dezelfde goederen, diensten of

activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande

grensoverschrijdende rulings inzake bronbelasting op inkomsten uit

arbeid, tantièmes en presentiegelden of pensioenen van niet-

ingezetenen niet onder de uitwisseling van inlichtingen over

voorafgaande grensoverschrijdende rulings met betrekking tot

natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:  4° L’échange d’informations est effectué comme suit :

hernieuwd en uiterlijk binnen drie maanden na het einde van het

semester  van  het  kalenderjaar  waarin  de  voorafgaande

grensoverschrijdende  rulings  of  voorafgaande

verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of

hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde

inlichtingen: vóór 1 januari 2018.

5° De door de Belgische bevoegde autoriteit uit hoofde van de

bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen

omvatten de volgende gegevens:

a) de identificatie van de rechtspersoon, tenzij de voorafgaande

grensoverschrijdende ruling betrekking heeft op een natuurlijke

persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt,

en in voorkomend geval de groep personen waartoe die persoon

behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende

ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen

een omschrijving van de relevante zakelijke activiteiten of transacties

of reeks van transacties, alsook alle andere inlichtingen die voor de

bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een

mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking

van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een

fabrieks- of handelswerkwijze, of van inlichtingen waarvan het

verstrekken in strijd zou zijn met de openbare orde.

c) de data van de aflevering, wijziging of hernieuwing van de

grensoverschrijdende voorafgaande fiscale beslissing;

d) de aanvangsdatum van de geldigheidsperiode van de

grensoverschrijdende  voorafgaande  fiscale  beslissing,  indien

vermeld;

e)  de  einddatum  van  de  geldigheidsperiode  van  de

grensoverschrijdende  voorafgaande  fiscale  beslissing,  indien

vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;  f) le type de décision fiscale anticipée en matière transfrontière ;

g) het bedrag van de verrichting of reeks van verrichtingen van de

grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld

in de grensoverschrijdende voorafgaande fiscale beslissing;

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling

betrekking heeft op een natuurlijke persoon en overeenkomstig de

bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die

er zijn, waarop de voorafgaande grensoverschrijdende ruling of de

voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van

invloed zal zijn waarbij vermeld dient te worden met welke lidstaten

de getroffen personen verbonden zijn, en

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a) , b) , en i) van

deze paragraaf worden niet medegedeeld aan de Europese

Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de

inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel

en in elk geval niet later dan zeven werkdagen na ontvangst, aan de

verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing

totdat het in § 24, 3 de en 4 de lid, bedoelde gegevensbestand

operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met

inachtneming van de bepalingen van § 24, 2 de lid, om aanvullende

inlichtingen verzoeken, daaronder begrepen de volledige tekst van

een grensoverschrijdende voorafgaande fiscale beslissing.

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen,

bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van

het eerste lid het fiscaal identificatienummer van de rijksinwoner dat

werd afgeleverd door rechtsgebied van verblijf.

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan

de commissie mee de statistieken over het volume van de

automatische uitwisseling in toepassing van de paragrafen 6 en 6/1,

alsook de inlichtingen over de kosten en baten, administratief en

andere, verbonden aan de uitwisseling die plaats heeft gevonden, en

aan de eventuele wijzigingen, zowel voor de belastingadministraties

als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle

relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie

van de administratieve samenwerking voorzien door dit artikel in het

licht van de strijd tegen de fiscale fraude en ontduiking.

De Belgische bevoegde autoriteit controleert en evalueert de

efficiëntie van de administratieve samenwerking voorzien door dit

artikel, met name wat betreft de strijd tegen de belastingontduiking

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde

lid bedoelde termijn de in tweede lid bedoelde gegevens inzake

grensoverschrijdende constructies, waarvan zij ingelicht is door de

intermediair of de relevante belastingplichtige overeenkomstig de

artikelen 289 bis /1 tot en met 289 bis /8, via automatische uitwisseling

mee aan de bevoegde autoriteiten van alle andere lidstaten.

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid

mee te delen gegevens zijn de volgende, voor zover van toepassing:

1° de identificatiegegevens van intermediairs, en relevante

belastingplichtigen, bedoeld in artikel 289 bis /1, 4° en 5°, met

uitzondering van intermediairs die op grond van het juridisch

beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig

###### Art. 289. bis /7, met inbegrip van hun naam, geboortedatum en -

plaats (in het geval van een natuurlijk persoon), fiscale woonplaats,

fiscaal identificatienummer, en, in voorkomend geval, van de

personen die overeenkomstig paragraaf 2, 21° een verbonden

onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in

###### Art. 289. bis /2 op grond waarvan de grensoverschrijdende

constructie gemeld moet worden;

3° een samenvatting van de inhoud van de meldingsplichtige

grensoverschrijdende constructie, met onder meer de benaming

waaronder zij algemeen bekend staat, indien voorhanden, en een

beschrijving van de relevante constructies, alsook alle andere

inlichtingen die voor de bevoegde autoriteit van belang kunnen zijn bij

het beoordelen van een mogelijk belastingrisico, die niet mag leiden

tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of

beroepsgeheim of een fabrieks- of handelswerkwijze, of van

inlichtingen waarvan de onthulling in strijd zou zijn met de openbare

orde;

4° de datum waarop de eerste stap voor de implementatie van de

meldingsplichtige grensoverschrijdende constructie is of zal worden

ondernomen;

5° nadere bijzonderheden van de nationale bepalingen die aan de

meldingsplichtige grensoverschrijdende constructie ten grondslag

liggen;

6° de waarde van de meldingsplichtige grensoverschrijdende

constructie;

8° de identificatiegegevens van andere personen in een lidstaat, op

wie de meldingsplichtige grensoverschrijdende constructie naar alle

waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met

welke lidstaten deze personen verbonden zijn.

De automatische uitwisseling geschiedt binnen één maand te

rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn

verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020

meegedeeld.

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze

paragraaf, worden niet medegedeeld aan de Europese Commissie.

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028,

bevat  de  mededeling  van  de  gegevens  betreffende  de

grensoverschrijdende regelingen het fiscaal identificatienummer van

de personen bepaald in het tweede lid, 8°.

§ 7 . De Belgische bevoegde autoriteit verstrekt spontaan, in elk van

de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de

buitenlandse bevoegde autoriteit:

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen

dat in de andere lidstaat een derving van belasting kan bestaan;

2° een belastingplichtige verkrijgt in België een vrijstelling of

vermindering van belasting die voor hem een belastingplicht of een

hogere belasting in de andere lidstaat zou moeten meebrengen;

3° transacties tussen een belastingplichtige in België en een

belastingplichtige in een andere lidstaat worden over één of meer

andere landen geleid, op zodanige wijze dat daardoor in één van beide

of in beide lidstaten een belastingbesparing kan ontstaan;

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen

dat er belastingbesparing kan ontstaan door een kunstmatige

verschuiving van winsten binnen een groep van ondernemingen;

5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen

door een buitenlandse bevoegde autoriteit, hebben informatie

opgeleverd die voor de vaststelling van de belastingschuld in die

andere lidstaat toereikend, ter zake dienend en niet overmatig is.

ter zake dienend en niet overmatig zijn.

De in het eerste lid bedoelde inlichtingen worden door de Belgische

bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand

nadat deze beschikbaar worden, aan de buitenlandse bevoegde

autoriteit van elke betrokken lidstaat verstrekt.

§ 8 . De ontvangst van de in § 7 bedoelde inlichtingen wordt door de

Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen

zeven werkdagen na ontvangst, indien mogelijk langs elektronische

weg, aan de verstrekkende buitenlandse bevoegde autoriteit

bevestigd.

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in

§ 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde

autoriteit verzoeken dat door eerstgenoemde gemachtigde

ambtenaren onder de voorwaarden die zijn vastgesteld door de

buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren

waar de administratieve autoriteiten van de lidstaat taken vervullen;

2° aanwezig zijn bij administratieve onderzoeken die worden

uitgevoerd op het grondgebied van de buitenlandse bevoegde

autoriteit;

3° deelnemen aan de administratieve onderzoeken die worden

uitgevoerd op het grondgebied van de andere lidstaat, met

gebruikmaking  van  elektronische  communicatiemiddelen,  in

voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren

aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen

door middel van elektronische communicatiemiddelen, kunnen zij

personen  ondervragen  en  bescheiden  onderzoeken,  onder

voorbehoud van de door de buitenlandse bevoegde autoriteit

gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde

inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische

bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde

ambtenaren onder de voorwaarden die zijn vastgesteld door de

Belgische bevoegde autoriteit mogen:

1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn

taken vervult;

3° deelnemen aan de administratieve onderzoeken die worden

uitgevoerd op Belgisch grondgebied, met gebruikmaking van

elektronische communicatiemiddelen, in voorkomend geval.

De Belgische bevoegde autoriteit antwoordt op het overeenkomstig

de eerste alinea ingediende verzoek binnen een termijn van 60 dagen

na ontvangst van het verzoek, om haar instemming te bevestigen of

haar gemotiveerde weigering aan de buitenlandse bevoegde

autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden

waartoe de ambtenaren van de Belgische bevoegde autoriteit

toegang hebben, ontvangen de ambtenaren van de verzoekende

autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn

tijdens een administratief onderzoek of daaraan deelnemen met

gebruikmaking van elektronische communicatiemiddelen, mogen zij

personen ondervragen en bescheiden onderzoeken, onder de

voorwaarden die zijn vastgesteld door de Belgische bevoegde

autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking

heeft, om de controlemaatregelen van de ambtenaren van de

verzoekende autoriteit na te leven, wordt door de Belgische bevoegde

autoriteit beschouwd als een weigering tegenover haar eigen

ambtenaren.

De door de verzoekende lidstaat gemachtigde ambtenaren die

overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds

een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en

hun officiële hoedanigheid worden vermeld.

§ 11 . In de gevallen waarin België met één of meer lidstaten

overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of

meer personen te wier aanzien zij een gezamenlijk of complementair

belang hebben, controles te verrichten en de aldus verkregen

inlichtingen uit te wisselen, is deze § van toepassing.

De Belgische bevoegde autoriteit bepaalt autonoom welke personen

zij voor een gelijktijdige controle wil voorstellen. Zij deelt de

buitenlandse bevoegde autoriteit van de betrokken lidstaten met

opgave van redenen mee welke dossiers zij voor een gelijktijdige

controle voorstelt. Zij bepaalt binnen welke termijn de controle moet

plaatsvinden.

autoriteit die de controle voorstelt een bevestiging van deelname of

een gemotiveerde weigering toekomen binnen een termijn van 60

dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan

die wordt belast met de leiding en de coördinatie van de controle.

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de

Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit

te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het

verzoek om een gezamenlijke audit binnen een termijn van 60 dagen,

te rekenen vanaf de ontvangst van het verzoek en motiveert haar

beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en

gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd

door de bevoegde autoriteit van de verzoekende lidstaat, door de

Belgische bevoegde autoriteit, en in voorkomend geval, door de

bevoegde autoriteiten van de andere aangezochte lidstaten en in

overeenstemming met de Belgische wetgeving en procedurele

voorschriften. De Belgische bevoegde autoriteit wijst een

vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en

de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die

deelnemen aan de gezamenlijke audit op Belgisch grondgebied,

worden vastgesteld overeenkomstig de Belgische wetgeving. Tegelijk

met het naleven van die wetgeving, oefenen de ambtenaren van een

andere lidstaat geen bevoegdheden uit die verder zouden gaan dan

de bevoegdheden die hun krachtens de wetgeving van hun lidstaat

zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die

deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd

om personen te ondervragen en bescheiden te onderzoeken in

samenspraak met de ambtenaren van de Belgische bevoegde

autoriteit, met inachtneming van de in België bepaalde procedurele

regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de

activiteiten van de gezamenlijke audit is verzameld, worden

beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde

juridische voorwaarden als in het geval van een klassieke audit,

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op

Belgisch grondgebied, genieten personen die aan een gezamenlijke

audit worden onderworpen of erdoor worden geraakt, dezelfde

rechten en hebben ze dezelfde plichten als in het geval van een

klassieke audit waaraan alleen Belgische ambtenaren deelnemen,

onder meer in de loop van een bezwaar-, herzienings- of

beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van

een of meer lidstaten een gezamenlijke audit verrichten, trachten zij

het eens te worden over de feiten en omstandigheden die relevant

zijn voor de gezamenlijke audit, en streven zij naar overeenstemming

over de fiscale positie van de geaudite persoon of personen op basis

van de resultaten van de gezamenlijke audit. De bevindingen van de

gezamenlijke audit worden neergelegd in een eindverslag. Punten

waarover de bevoegde autoriteiten het eens zijn, worden in de

conclusies van het eindverslag opgenomen en worden in aanmerking

genomen in de relevante instrumenten die de bevoegde autoriteiten

van de deelnemende lidstaten naar aanleiding van die gezamenlijke

audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het

resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het

eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 11/2. De Belgische bevoegde autoriteit kan de bevoegde autoriteit

van een andere of meerdere lidstaten verzoeken een gezamenlijke

audit uit te voeren.

Gezamenlijke audits worden op vooraf overeengekomen en

gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd

door de betrokken bevoegde autoriteiten, en in overeenstemming

met de wetgeving en de procedurele voorschriften van de lidstaat

waar de activiteiten van de gezamenlijke audit plaatsvinden.

De rechten en plichten van de Belgische ambtenaren die deelnemen

aan de gezamenlijke audit op het grondgebied van een andere

lidstaat, worden vastgesteld overeenkomstig de wetgeving van die

lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de

Belgische ambtenaren geen bevoegdheden uit die verder zouden

gaan dan de bevoegdheden die hun krachtens de Belgische

wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de

in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het

grondgebied van een andere lidstaat, kan het bewijsmateriaal dat

uitgevoerd in België door Belgische ambtenaren.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van

een of meerdere andere lidstaten een gezamenlijke audit verrichten,

trachten zij het eens te worden over de feiten en omstandigheden die

relevant zijn voor de gezamenlijke audit, en streven zij naar

overeenstemming over de fiscale positie van de geaudite persoon of

personen op basis van de resultaten van de gezamenlijke audit. De

bevindingen van de gezamenlijke audit worden neergelegd in een

eindverslag. De punten waarover de bevoegde autoriteiten het eens

zijn, worden in de conclusies van het eindverslag opgenomen en

worden in aanmerking genomen in de relevante instrumenten die de

bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding

van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het

resultaat van de gezamenlijke audit en krijgen een kopie van het

eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.

§ 12 . De Belgische bevoegde autoriteit kan een verzoek aan een

buitenlandse bevoegde autoriteit richten tot kennisgeving aan de

geadresseerde, overeenkomstig de in de aangezochte lidstaat

geldende voorschriften voor de kennisgeving van soortgelijke akten,

van alle door de Belgische administratieve overheden afgegeven

akten en besluiten die betrekking hebben op de toepassing in België

van wetgeving betreffende registratie-, hypotheek- en griffierechten.

Het verzoek tot kennisgeving vermeldt de naam en het adres van de

geadresseerde, evenals alle overige informatie ter identificatie van de

geadresseerde, en het onderwerp van de akte of het besluit waarvan

de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde

autoriteit slechts gedaan indien de kennisgeving van de akten niet

volgens de Belgische regels kan geschieden, of buitensporige

problemen zou veroorzaken. De Belgische bevoegde autoriteit kan

een document, per aangetekende brief of langs elektronische weg,

rechtstreeks ter kennis brengen aan een persoon op het grondgebied

van een andere lidstaat.

§ 13 . Op verzoek van een buitenlandse bevoegde autoriteit gaat de

Belgische bevoegde autoriteit, overeenkomstig de Belgische

voorschriften voor de kennisgeving van soortgelijke akten, over tot

kennisgeving aan de geadresseerde van alle door de administratieve

overheden van de verzoekende lidstaat afgegeven akten en besluiten

die betrekking hebben op de toepassing op haar grondgebied van

wetgeving betreffende registratie-, hypotheek- en griffierechten.

bijzonder, van de datum waarop de akte of het besluit aan de

geadresseerde ter kennis is gebracht.

§ 14 . Indien een buitenlandse bevoegde autoriteit inlichtingen

overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding

betreffende  de  ontvangen  inlichtingen  verzoekt,  doet  de

ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen

aan de Belgische voorschriften inzake beroepsgeheim en

gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie

maanden nadat het resultaat van het gebruik van de verlangde

inlichtingen bekend is, een terugmelding aan de buitenlandse

bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar,

overeenkomstig bilateraal overeengekomen praktische afspraken,

een terugmelding over de automatische inlichtingenuitwisseling naar

de betrokken lidstaten.

§ 15 . De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7

inlichtingen heeft verstrekt, kan de ontvangende buitenlandse

bevoegde autoriteit om terugmelding betreffende de ontvangen

inlichtingen verzoeken.

§ 16 . De Belgische verbindingsdienst of de Belgische bevoegde

ambtenaar die een verzoek om samenwerking ontvangt dat een

optreden vereist buiten de hem krachtens de Belgische wetgeving of

het Belgische beleid verleende bevoegdheid, geeft het verzoek

onmiddellijk door aan het Belgisch centraal verbindingsbureau en

stelt de verzoekende buitenlandse bevoegde autoriteit hiervan in

kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat

het verzoek aan het Belgisch centraal verbindingsbureau is

doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in

enigerlei  vorm  of  volgens  dit  artikel,  vallen  onder  de

geheimhoudingsplicht en genieten de bescherming waarin het

nationale recht van de ontvangende lidstaat met betrekking tot

soortgelijke inlichtingen voorziet.

Deze inlichtingen mogen worden gebruikt:  Ces informations peuvent servir :

1° voor de vaststelling, de toepassing en de handhaving van het

nationale recht met betrekking tot de in artikel 2 van de richtlijn

bedoelde belastingen, alsmede de btw, andere indirecte belastingen,

douanerechten, de bestrijding van het witwassen van geld en van de

financiering van terrorisme;

maart 2010 betreffende de wederzijdse bijstand inzake de

invordering van schuldvorderingen die voortvloeien uit belastingen,

rechten en andere maatregelen, en voor het vestigen en invorderen

van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures

die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op

de fiscale wetgeving, onverminderd algemene regels en wettelijke

bepalingen die de rechten van beklaagden en getuigen in het kader

van dergelijke procedures beheersen.

Met de toestemming van de buitenlandse bevoegde autoriteit die de

inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor

zover dat toegelaten is door de Belgische wetgeving, kunnen de

ontvangen inlichtingen en documenten ontvangen van deze autoriteit

worden gebruikt voor andere doeleinden dan deze bedoeld in het

tweede lid.

De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en

documenten zonder de in de derde lid van deze paragraaf bedoelde

toestemming ook gebruiken voor elk doel dat onder een op artikel 215

van het Verdrag betreffende de werking van de Europese Unie

gebaseerde handeling valt en deze daartoe delen met de bevoegde

autoriteit die verantwoordelijk is voor beperkende maatregelen in de

betrokken lidstaat.

De Belgische bevoegde autoriteit die van oordeel is dat de van de

bevoegde autoriteit van een andere lidstaat verkregen inlichtingen de

bevoegde autoriteit van een derde lidstaat van nut kunnen zijn voor

de in het tweede lid beoogde doelen, mag de inlichtingen aan deze

autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit

van de inlichtingen verstrekkende lidstaat in kennis stelt van haar

voornemen om die inlichtingen met een derde lidstaat te delen en op

voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel

vastgelegde regels en procedures. De inlichtingen verstrekkende

lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na

de datum van ontvangst van de kennisgeving van de lidstaat die de

inlichtingen wenst te delen.

§ 18 . De Belgische bevoegde autoriteit kan het gebruik toestaan van

de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in

de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid,

bedoelde doeleinden. De Belgische bevoegde autoriteit verleent

toestemming indien de inlichtingen in België voor soortgelijke

doeleinden kunnen worden gebruikt.

de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde

autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen

inlichtingen en bescheiden zonder de in het eerste lid bedoelde

toestemming gebruiken voor alle doeleinden die de Belgische

bevoegde autoriteit heeft opgenoemd.

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de

in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit

België die door een buitenlandse bevoegde autoriteit aan een

buitenlandse bevoegde autoriteit van een derde lidstaat werden

doorgegeven, in die derde lidstaat toestaan.

§ 19 . Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht

de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit

alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan

aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te

komen.

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde

autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op

voorwaarde dat de buitenlandse bevoegde autoriteit eerst de

inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in

de gegeven omstandigheden kon aanspreken zonder dat het

beoogde resultaat in het gedrang dreigt te komen.

§ 20 . Het is de Belgische bevoegde autoriteit niet toegelaten

onderzoek in te stellen of inlichtingen te verstrekken wanneer de

Belgische wetgeving haar niet toestaat voor eigen doeleinden het

onderzoek in te stellen of de gevraagde inlichtingen te verzamelen.

De Belgische bevoegde autoriteit kan weigeren inlichtingen te

verstrekken indien:

1° de verzoekende lidstaat, op juridische gronden, soortgelijke

inlichtingen niet kan verstrekken;

2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-,

nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze,

of indien het inlichtingen betreft waarvan de onthulling in strijd zou

zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee

op welke gronden zij het verzoek om inlichtingen afwijst.

§ 21 . De Belgische bevoegde autoriteit wendt de middelen aan

waarover zij beschikt om de gevraagde inlichtingen te verzamelen,

zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te

verstrekken uitsluitend omdat België geen binnenlands belang bij

deze inlichtingen heeft.

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat

de Belgische bevoegde autoriteit kan weigeren inlichtingen te

verstrekken, uitsluitend op grond dat deze berusten bij een bank, een

andere financiële instelling, een gevolmachtigde of een persoon die

als vertegenwoordiger of trustee optreedt, of dat zij betrekking

hebben op eigendomsbelangen in een persoon.

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit

weigeren de gevraagde inlichtingen toe te zenden indien deze

betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de

toezending van de inlichtingen geweigerd had kunnen worden op

grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom

was verzocht vóór 11 maart 2011.

§ 22. Indien de Belgische overheid voorziet in een samenwerking met

een derde land welke verder reikt dan de bij de richtlijn geregelde

samenwerking, kan de Belgische overheid de verderreikende

samenwerking niet weigeren aan een andere lidstaat die met haar

deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken

die zijn ingediend op grond van § 4, alsook de antwoorden op grond

van § 5, de ontvangstbevestigingen, de verzoeken om inlichtingen van

algemene aard en de verklaringen van ongeschiktheid of weigering

krachtens § 5 worden, voor zover mogelijk, overgemaakt door middel

van een door de Commissie goedgekeurd standaardformulier. Er

mogen rapporten, certificaten en andere bescheiden, of andere voor

eensluidend verklaarde afschriften of uittreksels daarvan bij de

standaardformulieren gevoegd worden.

De in het eerste lid bedoelde standaardformulieren bevatten ten

minste de volgende gegevens, die de verzoekende autoriteit moet

verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle

is ingesteld en, in het geval van vragen betreffende een groep zoals

bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;

b) het fiscale doel van de gevraagde informatie.  b) la finalité fiscale des informations demandées.

De Belgische bevoegde autoriteit kan, voor zover bekend en in

overeenstemming met de ontwikkeling van de internationale situatie,

door de aangezochte autoriteit kunnen vergemakkelijken.

De  spontane  gegevensuitwisseling  en  de  desbetreffende

ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8,

verzoeken tot administratieve kennisgeving op grond van §§ 12 en

13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op

grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden

overgemaakt door middel van de door de Commissie goedgekeurde

standaardformulieren.

De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1

wordt verricht in een geautomatiseerd standaardformaat dat

ontworpen is om die automatische uitwisseling te vergemakkelijken

en dat is goedgekeurd door de Commissie.

§ 24 . De krachtens dit artikel verstrekte inlichtingen worden voor

zover mogelijk verzonden langs elektronische weg, via het CCN-

netwerk.

Het verzoek om samenwerking, waaronder het verzoek tot

kennisgeving en de bijgevoegde bescheiden kunnen in elke door de

aangezochte en de verzoekende autoriteit overeengekomen taal zijn

gesteld. Slechts in bijzondere gevallen en mits het verzoek met

redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken

het verzoek vergezeld te laten gaan van een vertaling in één van de

officiële talen van België.

Om te voldoen aan de automatische uitwisseling als bedoeld in § 6/1,

1° en 2°, te verstrekken inlichtingen, worden de gegevens die

moeten worden meegedeeld opgeslagen in een beveiligd centraal

gegevensbestand betreffende de administratieve samenwerking op

belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter

beschikking gesteld door de Commissie uiterlijk op 31 december

2017. De Belgische bevoegde autoriteiten hebben toegang tot de in

dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand

operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde

automatische uitwisseling van gegevens, volgens lid 1 van deze

paragraaf en de toepasselijke praktische modaliteiten.

§ 25 . De Belgische bevoegde autoriteit die van een derde land

inlichtingen ontvangt welke naar verwachting van belang zijn voor

haar administratie en de handhaving van de Belgische wetgeving

betreffende registratie-, hypotheek- en griffierechten, kan deze

inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten

van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan

De Belgische bevoegde autoriteit kan, met inachtneming van de wet

van 8 december 1992 tot bescherming van de persoonlijke

levenssfeer ten opzichte van de verwerking van persoonsgegevens

en de wet van 3 augustus 2012 houdende bepalingen betreffende de

verwerking van persoonsgegevens door de Federale Overheidsdienst

Financiën in het kader van zijn opdrachten, de overeenkomstig dit

artikel ontvangen inlichtingen doorgeven aan een derde land, op

voorwaarde dat aan elk van de volgende voorwaarden is voldaan:

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de

inlichtingen afkomstig zijn, heeft daarin toegestemd;

b) het derde land heeft zich ertoe verbonden de medewerking te

verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent

het ongeoorloofde of onwettige karakter van verrichtingen die blijken

in strijd te zijn met of een misbruik te vormen van de

belastingwetgeving.

§  26.  Rapporterende  financiële  instellingen,  intermediairs,

rapporterende platformexploitanten en de Belgische bevoegde

autoriteit worden als verwerkingsverantwoordelijken beschouwd

wanneer zij, alleen of gezamenlijk, de doelen en middelen van de

verwerking van persoonsgegevens bepalen in de zin van Verordening

(EU) 2016/679 van het Europees Parlement en de Raad van 27 april

2016 betreffende de bescherming van natuurlijke personen in

verband met de verwerking van persoonsgegevens en betreffende

het vrije verkeer van die gegevens en tot intrekking van Richtlijn

95/46/EG.

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in

kennis van elke gegevensinbreuk en alle daaropvolgende

corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen

met de lidstaat of de lidstaten waar de gegevensinbreuk heeft

plaatsgevonden, schorsen door de Commissie en de betrokken

lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een

dergelijke schorsing wordt onmiddellijk van kracht.

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de

Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de

Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van

de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn,

indien de gegevensinbreuk niet onmiddellijk en op passende wijze

onder controle kan worden gebracht. Op een dergelijk verzoek schorst

de Commissie de toegang van die lidstaat of lidstaten tot het CCN-

netwerk voor de toepassing van de richtlijn.

inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie

verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is

verholpen, geeft de Commissie pas na die verificatie de betrokken

lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de

toepassing van de richtlijn.

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in

het centrale gegevensbestand of het CCN-netwerk plaatsvindt die

nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen

door de lidstaten via het CCN-netwerk, stelt de Commissie de

lidstaten  zonder  onnodige  vertraging  in  kennis  van  de

gegevensinbreuk en van eventuele corrigerende maatregelen die zijn

genomen. Zulke corrigerende maatregelen kunnen inhouden dat de

toegang tot het centrale gegevensbestand of het CCN-netwerk voor

de toepassing van de richtlijn wordt geschorst totdat de

gegevensinbreuk is verholpen.

----------

Nota:  Note :

- in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.  - dans le § 6/1, al. 1 er , 5°, a) et i) : lire « 1° et 3° » au lieu de « 1° et 4° ».

- in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.  - dans le § 6/1, al. 2 : lire « 5°, a) et i) » au lieu de « 6°, a) et k) ».

- in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.  - dans le § 6/3, al. 2, 1° : lire « paragraphe 2, 18° » au lieu de « paragraphe 2, 21° ».

- in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.

###### Art. 289. bis /1

(8°, ingevoegd bij art. 29 van de wet van 16.03.2026 (B.S., 01.04.2026). Tekst

van toepassing vanaf 11.04.2026 (art. -))

Voor de toepassing van de artikelen 289 bis , § 6/3 en 289 bis /2 tot en

met 289 bis /9, wordt verstaan onder:

1° "grensoverschrijdende constructie": een constructie die ofwel

meer dan één lidstaat ofwel een lidstaat en een derde land betreft,

waarbij ten minste een van de volgende voorwaarden is vervuld:

a) niet alle deelnemers aan de constructie hebben hun fiscale

woonplaats in hetzelfde rechtsgebied;

b) een of meer van de deelnemers aan de constructie heeft zijn fiscale

woonplaats tegelijkertijd in meer dan één rechtsgebied;

c) een of meer van de deelnemers aan de constructie oefent een

bedrijf uit in een ander rechtsgebied via een in dat rechtsgebied

gelegen vaste inrichting en de constructie behelst een deel of het

geheel van het bedrijf van die vaste inrichting;

fiscale woonplaats te hebben of zonder in dat rechtsgebied een vaste

inrichting te creëren;

e) een dergelijke constructie heeft mogelijk gevolgen voor de

automatische uitwisseling van inlichtingen of de vaststelling van het

uiteindelijk belang.

Een constructie betekent ook een reeks constructies. Een constructie

kan uit verscheidene stappen of onderdelen bestaan.

2° "meldingsplichtige grensoverschrijdende constructie": iedere

grensoverschrijdende constructie die ten minste één van de in artikel

289 bis /2 bedoelde wezenskenmerken bezit;

3° "wezenskenmerk": een in artikel 289 bis /2 bedoelde eigenschap of

kenmerk van een grensoverschrijdende constructie die geldt als een

indicatie van een mogelijk risico op belastingontwijking;

4°  "intermediair":  een  persoon  die  een  meldingsplichtige

grensoverschrijdende  constructie  bedenkt,  aanbiedt,  opzet,

beschikbaar maakt voor implementatie of de implementatie ervan

beheert.

Een intermediair is ook een persoon die, gelet op de betrokken feiten

en omstandigheden en op basis van de beschikbare informatie en de

deskundigheid die en het begrip dat nodig is om die diensten te

verstrekken, weet of redelijkerwijs kon weten dat hij rechtstreeks of

via andere personen, heeft toegezegd hulp, bijstand of advies te

verstrekken met betrekking tot het bedenken, aanbieden, opzetten,

beschikbaar maken voor implementatie of beheren van de

implementatie van een meldingsplichtige grensoverschrijdende

constructie. Elke persoon heeft het recht bewijs te leveren van het feit

dat hij niet wist en redelijkerwijs niet kon weten dat hij bij een

meldingsplichtige grensoverschrijdende constructie betrokken was.

Daartoe kan die persoon alle relevante feiten en omstandigheden,

beschikbare informatie en zijn relevante deskundigheid en begrip

ervan vermelden.

Om een intermediair te zijn, dient een persoon ten minste één van de

volgende aanvullende voorwaarden te vervullen:

a) fiscaal inwoner van een lidstaat zijn;  a) être résidente dans un Etat membre à des fins fiscales ;

b) beschikken over een vaste inrichting in een lidstaat via welke de

diensten in verband met de constructie worden verleend;

d) ingeschreven zijn bij een beroepsorganisatie in verband met de

verstrekking van juridische, fiscale of adviesdiensten in een lidstaat.

5° "relevante belastingplichtige": elke persoon voor wie een

meldingsplichtige grensoverschrijdende constructie beschikbaar

wordt gemaakt voor implementatie, of die gereed is om een

meldingsplichtige  grensoverschrijdende  constructie  te

implementeren of die de eerste stap van een dergelijke constructie

heeft geïmplementeerd;

6° "marktklare constructie": een grensoverschrijdende constructie

die is bedacht of aangeboden, implementeerbaar is of beschikbaar is

gemaakt voor implementatie zonder dat er wezenlijke aanpassingen

nodig zijn;

7° "constructie op maat": een grensoverschrijdende constructie die

geen marktklare constructie is.

8° "cliënt": elke intermediair of relevante belastingplichtige die

diensten, met inbegrip van bijstand, advies, raad of begeleiding,

ontvangt van een tot het juridisch beroepsgeheim gehouden

intermediair  met  betrekking  tot  een  meldingsplichtige

grensoverschrijdende constructie.

###### Art. 289. bis /2

(ingevoegd bij art. 21 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

De in artikel 289 bis /1, 3°, bedoelde wezenskenmerken van een

grensoverschrijdende constructie kunnen worden onderverdeeld in

vijf categorieën, categorie A zijnde de algemene wezenskenmerken

die aan de in het tweede lid bedoelde "main benefit test" zijn

gekoppeld, categorie B zijnde de specifieke wezenskenmerken die

aan de hiervoor vermelde "main benefit test" zijn gekoppeld,

categorie C zijnde specifieke wezenskenmerken in verband met

grensoverschrijdende transacties, categorie D zijnde specifieke

wezenskenmerken in verband met de automatische uitwisseling van

inlichtingen en uiteindelijk belang en categorie E zijnde specifieke

wezenskenmerken in verband met verrekenprijzen.

De algemene wezenskenmerken in categorie A bedoeld in het vierde

lid en de specifieke wezenskenmerken in categorie B bedoeld in het

belangrijkste voordeel of één van de belangrijkste voordelen die, gelet

op alle relevante feiten en omstandigheden, redelijkerwijs te

verwachten valt van de constructie het verkrijgen van een

belastingvoordeel is. Dit is de zogenaamde "main benefit test

In het kader van het specifieke wezenskenmerk van categorie C,

bedoeld in het zesde lid, 1° is de aanwezigheid van één van de

voorwaarden bedoeld in hetzelfde zesde lid, 1°, b), eerste streepje, c)

en d) niet voldoende om te besluiten dat een constructie voldoet aan

de in het tweede lid bedoelde "main benefit test

Wordt beschouwd als een algemeen wezenskenmerk van categorie

A:

1° een constructie waarbij de relevante belastingplichtige of een

deelnemer aan de constructie zich tot geheimhouding verbindt en op

grond  hiervan  niet  aan  andere  intermediairs  of  de

belastingautoriteiten mag onthullen hoe de constructie een

belastingvoordeel kan opleveren;

2° een constructie waarbij de intermediair aanspraak maakt op een

vergoeding (of rente, betaling van financieringskosten en andere

uitgaven) voor de constructie en die vergoeding wordt vastgelegd op

basis van:

a) het bedrag van het belastingvoordeel dat de constructie oplevert;

of

b) de vraag of de constructie daadwerkelijk een belastingvoordeel

heeft opgeleverd. De intermediair moet daarbij de vergoeding

gedeeltelijk of volledig terugbetalen wanneer het met de constructie

beoogde belastingvoordeel niet gedeeltelijk of volledig werd

verwezenlijkt;

3° een  constructie waarbij gebruik  wordt gemaakt  van

gestandaardiseerde documenten en/of een gestandaardiseerde

structuur en die beschikbaar is voor meer dan een relevante

belastingplichtige zonder dat er voor implementatie wezenlijke

aanpassingen nodig zijn.

Wordt beschouwd als een specifiek wezenskenmerk van categorie B:  Est considéré comme un marqueur spécifique de catégorie B :

1° een constructie waarbij een deelnemer aan de constructie een

reeks geplande stappen onderneemt die erin bestaan een

verlieslijdende onderneming te verwerven, de hoofdactiviteit van die

onderneming stop te zetten en de verliezen ervan te gebruiken om de

door hem verschuldigde belastingen te verminderen, onder meer

2° een constructie die tot gevolg heeft dat inkomsten worden

omgezet in vermogen, schenkingen of andere inkomstencategorieën

die lager worden belast of van belasting worden vrijgesteld;

3° een constructie die circulaire transacties omvat met als resultaat

dat middelen worden rondgepompt ("round-tripping"), meer bepaald

met behulp van tussengeschoven entiteiten zonder ander primair

handelsdoel of van transacties die elkaar compenseren of tenietdoen

of andere soortgelijke kenmerken hebben.

Wordt beschouwd als een specifiek wezenskenmerk van categorie C:  Est considéré comme un marqueur spécifique de catégorie C :

1° een constructie met aftrekbare grensoverschrijdende betalingen

tussen twee of meer verbonden ondernemingen waarbij ten minste

een van de volgende voorwaarden is vervuld:

a) de ontvanger is in geen van de fiscale rechtsgebieden fiscaal

inwoner;

b) de ontvanger is fiscaal inwoner in een rechtsgebied, maar dat

rechtsgebied:

- heft geen vennootschapsbelasting, of heft vennootschapsbelasting

tegen een nultarief of bijna-nultarief; of

- is opgenomen in een lijst van rechtsgebieden van derde landen die

door de lidstaten gezamenlijk of in het kader van de OESO als niet-

coöperatief zijn beoordeeld;

c) de betaling geniet een volledige belastingvrijstelling in het

rechtsgebied waar de ontvanger fiscaal inwoner is;

d) de betaling geniet een fiscaal gunstregime in het rechtsgebied waar

de ontvanger fiscaal inwoner is;

2° in meer dan één rechtsgebied wordt aanspraak gemaakt op

aftrekken voor dezelfde afschrijving;

3° in meer dan één rechtsgebied wordt aanspraak gemaakt op

voorkoming van dubbele belasting voor hetzelfde inkomens- of

vermogensbestanddeel;

4° een constructie met overdrachten van activa waarbij er een

wezenlijk verschil bestaat tussen het bedrag dat in de betrokken

rechtsgebieden wordt aangemerkt als de voor die activa te betalen

vergoeding.

1° een constructie die kan leiden tot het ondermijnen van de

rapportageverplichting uit hoofde van de wetgeving ter omzetting

van Uniewetgeving of evenwaardige overeenkomsten inzake de

automatische  uitwisseling  van  inlichtingen  over  financiële

rekeningen, waaronder overeenkomsten met derde landen, of die

profiteert van het gebrek aan die wetgeving of overeenkomsten.

Dergelijke constructies omvatten ten minste het volgende:

a) het gebruik van een rekening, product of belegging die geen

financiële rekening is of niet als zodanig te boek staat, maar die over

eigenschappen beschikt die in wezen vergelijkbaar zijn met die van

een financiële rekening;

b) de overdracht van financiële rekeningen of activa aan, of het

gebruik van rechtsgebieden die niet gebonden zijn aan de

automatische uitwisseling van inlichtingen over financiële rekeningen

met de staat van verblijf van de relevante belastingplichtige;

c) de herkwalificatie van inkomsten en vermogen in producten of

betalingen die niet onder de automatische uitwisseling van

inlichtingen vallen;

d) de overdracht of omzetting van een financiële instelling of een

financiële rekening of de activa daarvan in een financiële instelling of

een financiële rekening of activa die niet onder de rapportage in het

kader van de automatische uitwisseling van inlichtingen vallen;

e) het gebruik van rechtspersonen, juridische constructies of

structuren die de rapportage over één of meer rekeninghouders of

uiteindelijk begunstigden in het kader van de automatische

uitwisseling van inlichtingen over financiële rekeningen stopzetten of

daartoe strekken;

f) constructies die due-diligenceprocedures die door financiële

instellingen worden gebruikt om te voldoen aan hun verplichtingen

tot het rapporteren van inlichtingen over financiële rekeningen,

ondermijnen of zwakke punten ervan benutten, onder meer via het

gebruik van rechtsgebieden met ontoereikende of zwakke regelingen

voor de handhaving van antiwitwaswetgeving of met zwakke

transparantievereisten  voor  rechtspersonen  of  juridische

constructies;

2° een constructie waarbij de juridische of feitelijke eigendom niet-

transparant is door het gebruik van personen, juridische constructies

of structuren:

b) die zijn opgericht in, worden beheerd in, inwoner zijn van, onder

zeggenschap staan in, of gevestigd zijn in een ander rechtsgebied dan

het rechtsgebied van verblijf van een of meer van de uiteindelijk

begunstigden van de activa die door die personen, juridische

constructies of structuren worden aangehouden; en

c) indien de uiteindelijk begunstigden van die personen, juridische

constructies of structuren, zoals bedoeld in artikel 4, 27°, van de wet

van 18 september 2017 tot voorkoming van het witwassen van geld

en de financiering van terrorisme en tot beperking van het gebruik van

contanten, niet-identificeerbaar zijn gemaakt.

Wordt beschouwd als een specifiek wezenskenmerk van categorie E:  Est considéré comme un marqueur spécifique de catégorie E :

1° een constructie met gebruik van unilaterale veiligehavenregels;  1° un dispositif qui prévoit l'utilisation de régimes de protection

2° een constructie met overdracht van moeilijk te waarderen

immateriële activa. De term "moeilijk te waarderen immateriële

activa" omvat immateriële activa of rechten op immateriële activa

waarvoor, op het tijdstip van de overdracht ervan tussen verbonden

ondernemingen:

a) geen betrouwbare vergelijkbare activa bestaan; en  a) il n'existe pas d'éléments de comparaison fiables ; et

b) de prognoses van de toekomstige kasstromen of inkomsten die

naar verwachting uit de overgedragen activa voortvloeien, of de

aannames die worden gebruikt voor het waarderen van de

immateriële activa, bijzonder onzeker zijn, waardoor het moeilijk is te

voorspellen hoe succesvol de immateriële activa op het moment van

de overdracht uiteindelijk zullen zijn;

3° een constructie met een grensoverschrijdende overdracht binnen

de groep van functies, en/of risico's en/of activa, indien de geraamde

jaarlijkse winst vóór interest en belastingen (ebit) van de overdrager

of overdragers, tijdens de periode van drie jaar na de overdracht,

minder dan 50 % bedraagt van de geraamde jaarlijkse ebit van die

overdrager of overdragers indien de overdracht niet had

plaatsgevonden.

----------

Nota:  Note :

(1) Moeten eveneens de inlichtingen verstrekt worden over de in deze wet

bedoelde meldingsplichtige grensoverschrijdende constructies waarvan de

eerste stap is geïmplementeerd tussen 25 juni 2018 en 01.07.2020. Deze

###### Art. 289. bis /3

(ingevoegd bij art. 22 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

§ 1. Elke intermediair moet de in artikel 289 bis , § 6/3 bedoelde

inlichtingen,  over  meldingsplichtige  grensoverschrijdende

constructies waarvan zij kennis, bezit of controle hebben verstrekken

aan de in artikel 289 bis , § 2, 6°, bedoelde Belgische bevoegde

autoriteit binnen 30 dagen te rekenen vanaf het hierna vermelde

geval dat het eerst plaatsvindt:

- de dag nadat de meldingsplichtige grensoverschrijdende constructie

voor implementatie beschikbaar is gesteld; of

- de dag nadat de meldingsplichtige grensoverschrijdende constructie

gereed is voor implementatie; of

- het ogenblik dat de eerste stap in de implementatie van de

meldingsplichtige grensoverschrijdende constructie is ondernomen.

Onverminderd het eerste lid moeten de intermediairs bedoeld in

###### Art. 289. bis /1, 4°, tweede lid, eveneens inlichtingen verstrekken

met betrekking tot een meldingsplichtige grensoverschrijdende

constructie binnen 30 dagen te rekenen vanaf de dag nadat zij,

rechtstreeks of via andere personen, hulp, bijstand of advies hebben

verstrekt.

§ 2. Wanneer de intermediair inlichtingen over meldingsplichtige

grensoverschrijdende constructies moet verstrekken aan de

bevoegde autoriteiten van meer dan één lidstaat dan verstrekt hij

deze inlichtingen enkel aan de Belgische bevoegde autoriteit indien

België als eerste op de onderstaande lijst voorkomt:

1° de lidstaat waar de intermediair fiscaal inwoner is;  1° l'Etat membre dans lequel l'intermédiaire est résident à des fins

2° de lidstaat waar de intermediair een vaste inrichting heeft via

welke de diensten met betrekking tot de constructie worden

verstrekt;

3° de lidstaat waar de intermediair is opgericht of onder toepassing

van de wetten valt;

Wanneer er op grond van het eerste lid een meervoudige

meldingsplicht bestaat, wordt de intermediair ontheven van het

verstrekken van de inlichtingen als hij een schriftelijk bewijs voorlegt

dat dezelfde inlichtingen in een andere lidstaat zijn verstrekt.

###### Art. 289. bis /4

(ingevoegd bij art. 23 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

Indien het gaat om een marktklare constructie moet de intermediair

om de drie maanden een periodiek verslag opstellen met een

overzicht van nieuwe meldingsplichtige inlichtingen zoals bedoeld in

###### Art. 289. bis , § 6/3, 1°, 4°, 7° en 8°, die sinds het laatste ingediende

verslag beschikbaar zijn geworden.

De intermediair die het uniek referentienummer van de bevoegde

instanties ontvangt, dient dit, samen met de samenvatting

betreffende de gemelde constructie, onverwijld aan de andere

betrokken intermediairs en aan de relevante belastingplichtige door

te geven.

###### Art. 289. bis /5

(ingevoegd bij art. 24 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

Naar aanleiding van de melding van een grensoverschrijdende

constructie die ten minste één van de in artikel 289 bis /2 vermelde

wezenskenmerken bezit, wordt een uniek referentienummer

toegekend, dat naar aanleiding van elke volgende melding

betreffende diezelfde grensoverschrijdende constructie moet

worden meegedeeld, zowel voor meldingen door elke betrokken

intermediair als voor meldingen door de relevante belastingplichtige.

De intermediair die het uniek referentienummer van de bevoegde

instanties ontvangt, dient dit, samen met de samenvatting

betreffende de gemelde constructie, onverwijld aan de andere

betrokken intermediairs en aan de relevante belastingplichtige door

te geven.

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

Wanneer meerdere intermediairs betrokken zijn bij dezelfde

meldingsplichtige grensoverschrijdende constructie, moeten alle

betrokken intermediairs de inlichtingen verstrekken over de

meldingsplichtige grensoverschrijdende constructie.

Een intermediair wordt ontheven van de verplichting tot het

verstrekken van inlichtingen indien hij een schriftelijk bewijs voorlegt

dat een andere intermediair de inlichtingen bedoeld in artikel 289 bis ,

§ 6/3, tweede lid, reeds heeft verstrekt.

###### Art. 289. bis /7

(§ 1, lid 1, 1°, vernietigd door het arrest 1/2024 van 11.01.2024 van het

Grondwettelijk Hof, wordt hersteld, en § 4, ingevoegd bij art. 30 van de wet van

16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))

§ 1. Wanneer een intermediair gebonden is door een beroepsgeheim,

is hij gehouden:

1° de betrokken intermediair of intermediairs schriftelijk en

gemotiveerd op de hoogte te brengen dat hij niet aan de

meldingsplicht  kan  voldoen,  waardoor  deze  meldingsplicht

automatisch rust op de andere intermediair of intermediairs;

2° bij gebreke aan een andere intermediair, de relevante

belastingplichtige of belastingplichtigen schriftelijk en gemotiveerd

op de hoogte te brengen van zijn of hun meldingsplicht.

De ontheffing van de meldingsplicht krijgt slechts uitwerking op het

tijdstip dat een intermediair voldaan heeft aan de in het eerste lid

bedoelde verplichting.

§ 2. De relevante belastingplichtige kan de intermediair door

schriftelijke instemming toelaten alsnog te voldoen aan de in artikel

289 bis /3 bedoelde meldingsplicht.

Indien de relevante belastingplichtige geen instemming verleent blijft

de meldingsplicht bij de belastingplichtige en bezorgt de intermediair

de nodige gegevens voor het vervullen van de in artikel 289 bis /3

bedoelde meldingsplicht aan de relevante belastingplichtige.

een periodiek verslag overeenkomstig artikel 289 bis /4.

§ 4. In afwijking van paragraaf 1, eerste lid, 1°, is de intermediair die

een advocaat is, niet gehouden een betrokken intermediair die niet de

cliënt is op de hoogte te brengen dat hij niet aan de meldingsplicht kan

voldoen.

###### Art. 289. bis /8

(ingevoegd bij art. 27 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

§ 1. In de volgende gevallen ligt de meldingsplicht bij de relevante

belastingplichtige:

1° wanneer er geen intermediair betrokken was bij het bedenken,

aanbieden, opzetten, beschikbaar maken voor implementatie of het

beheren  voor  implementatie  van  de  meldingsplichtige

grensoverschrijdende constructie; of

2° wanneer de intermediair ontheven is van de verplichting om

inlichtingen te verstrekken overeenkomstig artikel 289 bis /7, § 1, en

hij de relevante belastingplichtige of belastingplichtigen op de hoogte

heeft gesteld van zijn of hun meldingsplicht, overeenkomstig artikel

289 bis /7, § 1, 2°.

3° wanneer deze niet de in artikel 289 bis /7, § 2, eerste lid bedoelde

toestemming heeft verleend.

§ 2. Ingeval de meldingsplicht overeenkomstig paragraaf 1 bij de

relevante belastingplichtige ligt, verstrekt deze de inlichtingen binnen

dertig dagen, te rekenen vanaf het hierna vermelde geval dat eerst

plaatsvindt:

- de dag nadat de meldingsplichtige grensoverschrijdende constructie

voor  implementatie  ter  beschikking  van  de  relevante

belastingplichtige is gesteld of;

- de dag nadat de meldingsplichtige grensoverschrijdende constructie

gereed is voor implementatie door de relevante belastingplichtige of;

- vanaf het ogenblik dat de eerste stap voor de implementatie ervan

met betrekking tot de relevante belastingplichtige is ondernomen.

dan moet hij deze inlichtingen enkel verstrekken aan de Belgische

bevoegde autoriteit indien België als eerste op de onderstaande, lijst

voorkomt:

1° de lidstaat waar de relevante belastingplichtige fiscaal inwoner is;  1° l'Etat membre dans lequel le contribuable concerné est résident à

2° de lidstaat waar de relevante belastingplichtige een vaste

inrichting heeft die begunstigde van de constructie is;

3° de lidstaat waar de relevante belastingplichtige inkomsten

ontvangt  of  winsten  genereert,  hoewel  de  relevante

belastingplichtige geen fiscaal inwoner van een lidstaat is noch een

vaste inrichting in een lidstaat heeft;

4° de lidstaat waar de relevante belastingplichtige een activiteit

uitoefent, hoewel de relevante belastingplichtige geen fiscaal

inwoner van een lidstaat is noch een vaste inrichting in een lidstaat

heeft.

Wanneer er op grond van het eerste lid een meervoudige

meldingsplicht bestaat, wordt de relevante belastingplichtige

ontheven van het verstrekken van de inlichtingen als hij een

schriftelijk bewijs voorlegt dat dezelfde inlichtingen in een andere

lidstaat zijn verstrekt.

----------

Nota:  Note :

(1) Moeten eveneens de inlichtingen verstrekt worden over de in deze wet

bedoelde meldingsplichtige grensoverschrijdende constructies waarvan de

eerste stap is geïmplementeerd tussen 25 juni 2018 en 01.07.2020. Deze

inlichtingen over die meldingsplichtige grensoverschrijdende constructies worden

uiterlijk op 31 augustus 2020 meegedeeld (art. 61, lid 2).

###### Art. 289. bis /9

(ingevoegd bij art. 28 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

Wanneer de meldingsplicht bij de relevante belastingplichtige ligt en

er meer dan één relevante belastingplichtige is, worden de

inlichtingen overeenkomstig artikel 289 bis /8 verstrekt door de

relevante belastingplichtige die als eerste op de onderstaande lijst

voorkomt:

2° de relevante belastingplichtige die de implementatie van de

constructie beheert.

Een relevante belastingplichtige wordt ontheven van de verplichting

tot het verstrekken van de inlichtingen indien hij een schriftelijk bewijs

voorlegt dat een andere relevante belastingplichtige de inlichtingen

bedoeld in artikel 289 bis , § 6/3, reeds heeft verstrekt.

###### Art. 289. bis /10

(ingevoegd bij art. 29 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

Voor de toepassing van de artikelen 289 bis , § 6/3 en 289 bis /1 tot en

met 289 bis /9 en de daaruit voortvloeiende uitvoeringsbesluiten dient

de melding van de inlichtingen, voor de onderdelen die de Koning

nader bepaalt, naast het gebruik van één van de officiële landstalen,

ook in het Engels te gebeuren.

----------

Nota:  Note :

Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën

of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens,

naast het gebruik van één van de officiële landstalen, ook in het Engels moeten

worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of

de relevante belastingplichtige moet worden gebruikt (art. 2). De leidinggevende

ambtenaar bedoeld in het bovenvermelde KB is de leidinggevende ambtenaar van

de  algemene  administratie  bevoegd  voor  de  vestiging  van  de

inkomstenbelastingen (art. 1, MB 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289. bis /11

(ingevoegd bij art. 30 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

De Koning bepaalt het formulier waarop de intermediair of de

relevante belastingplichtige de verplichtingen opgenomen in de

artikelen 289 bis /1 tot en met 289 bis /9 moeten naleven.

----------

Nota:  Note :

Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën

of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens,

naast het gebruik van één van de officiële landstalen, ook in het Engels moeten

worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of

inkomstenbelastingen (art. 1, MB 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289. bis /12

(gewijzigd bij art. 18 van de wet van 20.12.2024 (B.S., 31.12.2024). Tekst van

toepassing vanaf 31.12.2024 (art. 19))

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan

voor de overtreding van de bepalingen van de artikelen 289 bis /1 tot

en met 289 bis /9, evenals van de ter uitvoering ervan genomen

besluiten, die bestaat uit het onvolledig verstrekken van de

inlichtingen bedoeld in artikel 289 bis , § 6/3, een boete opleggen van 1

250 euro tot 12 500 euro. Voor dergelijke overtredingen gedaan met

bedrieglijk opzet of het oogmerk te schaden wordt een boete van 2

500 euro tot 25 000 euro opgelegd.

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan

voor de overtreding van de bepalingen van de artikelen 289 bis /1 tot

en met 289 bis /9, evenals van de ter uitvoering ervan genomen

besluiten, die bestaat uit het niet of laattijdig verstrekken van de

inlichtingen bedoeld in artikel 289 bis , § 6/3, een boete opleggen van 5

000 euro tot 50 000 euro. Voor dergelijke overtredingen gedaan met

bedrieglijk opzet of het oogmerk te schaden wordt een boete van 12

500 euro tot 100 000 euro opgelegd.

De Koning legt de progressieve schaal van de administratieve

geldboetes vast en regelt hun toepassingsmodaliteiten.

De Koning kan voor de geldboeten die Hij bepaalt, voorzien in de

toepassingsmodaliteiten van de maatregelen tot individualisering van

de sanctie door de bevoegde rechter.

###### Art. 289. bis /13

(ingevoegd bij art. 32 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van

toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))

(Bij arrest van 15.09.2022 (nr. 103/2022), heeft het Grondwettelijk Hof art.

289bis/13 W.Reg. vernietigd)

De fiscale administratie, mag binnen de door haar bepaalde termijn,

welke wegens wettige redenen kan worden verlengd, voor zover zij

die informatie nodig acht om de correcte naleving van de artikelen

Belgische bevoegde autoriteit.

###### Art. 289. ter

(ingevoegd bij art. 11 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van

toepassing vanaf 01.03.2021 (art. -))

De Koning bepaalt de wijze van betaling van alle bedragen die

krachtens de bepalingen van dit Wetboek en de uitvoeringsbesluiten

ervan verschuldigd zijn, andere dan de strafrechtelijke boetes.

###### Art. 289. quater   (tekst niet in werking getreden)

(ingevoegd bij art. 81 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. quinquies   (tekst niet in werking getreden)

(ingevoegd bij art. 82 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. sexies

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. septies

(§ 1, opgeheven bij art. 216 van de wet van 12.05.2024 (B.S., 30.05.2024 –

ed. 2). Tekst van toepassing vanaf 09.06.2024 (art. -))

(…) (1)

----------

Nota:  Note :

(1) § 2, ingevoegd bij art. 84 van de wet van 26.01.2021 (B.S., 10.02.2021) die

nooit in werking is getreden wordt opgeheven bij art. 213 van de wet van

12.05.2024 (B.S., 30.05.2024 – ed. 2).

###### Art. 289. octies   (tekst niet in werking getreden)

(ingevoegd bij art. 85 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. nonies   (tekst niet in werking getreden)

(ingevoegd bij art. 86 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(…)

###### Art. 289. decies   (tekst niet in werking getreden)

(ingevoegd bij art. 87 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. undecies   (tekst niet in werking getreden)

(ingevoegd bij art. 88 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

###### Art. 289. duodecies   (tekst niet in werking getreden)

(ingevoegd bij art. 89 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

###### Art. 289. terdecies   (tekst niet in werking getreden)

(ingevoegd bij art. 90 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van

toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een

inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum

vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van

de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf

09.06.2024 (art. -))

(…)

INTREKKINGSBEPALING  DISPOSITION ABROGATOIRE

###### Artikel 290

Onder voorbehoud van de bijzondere fiscale bepalingen voortvloeiend

hetzij uit door den Staat gesloten en bij een wet goedgekeurde

contracten, hetzij uit internationale overeenkomsten, worden alle

vroegere wetsbepalingen betreffende registratie-, hypotheek- of

griffierechten ingetrokken.

TIJDELIJKE BEPALINGEN  DISPOSITIONS TEMPORAIRES

#### Afdeling I - Maatregelen waarbij de oprichting van nieuwe

gebouwen begunstigd wordt door een vermindering der

registratierechten

§ 1 - Aankoop van een bouwgrond  § 1 er . Achat d’un emplacement

###### Art. 291. (zonder voorwerp geworden)

(…)

###### Art. 292. (niet meer van toepassing)

###### Art. 293. (zonder voorwerp geworden)

(…)

###### Art. 294. (niet meer van toepassing)

(…)

###### Art. 295. (niet meer van toepassing)

(…)

###### Art. 296. (zonder voorwerp geworden)

(…)

§ 2 - Verkoop van een gebouwd onroerend goed  § 2. Vente d’un immeuble bâti

###### Art. 297. (niet meer van toepassing)

(…)

###### Art. 298. (zonder voorwerp geworden)

(…)

###### Art. 299. (niet meer van toepassing)

(…)

###### Artikel 300

(opgeheven bij art. 32 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst

van toepassing vanaf 01.01.1961 (art. 39))

(…)

###### Artikel 301

(1°, gewijzigd bij art. 5 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst

van toepassing vanaf 02.09.2023 (art. -))

Zijn van de formaliteit van registratie vrijgesteld:  Sont exemptés de la formalité de l’enregistrement :

1° Akten in der minne betreffende de leningen toegestaan door de

Centrale Dienst voor sociale en culturele actie van het Ministerie van

Landsverdediging.

2° Akten, vonnissen en arresten betreffende de uitvoering van de

wetten op het herstel van oorlogsschade; minnelijke akten

betreffende leningen en kredietopeningen toegekend aan de

geteisterden om hun toe te laten de schade te herstellen die zijn

geleden hebben ingevolge oorlogsfeiten, wanneer deze leningen en

kredietopeningen worden toegestaan volgens de voorzieningen van

de ter zake geldende wettelijke beschikkingen, door een in deze

beschikkingen bedoelde kredietinstelling.

3° Akten van overdracht en inpandgeving van vorderingen tot herstel

van oorlogsschade;

4° (…)  4  (…)

5° (…)  5  (…)

6° Akten van procedure voor de gemengde scheidsgerechten

ingesteld bij de vredesverdragen, waaronder de beslissingen en de

betekening ervan.

7° Akten, vonnissen en arresten betreffende de rechtsplegingen tot

wettiging van de kinderen wier ouders, ten gevolge van den oorlog,

zich in de onmogelijkheid hebben bevonden een huwelijk aan te gaan.

8° (…)

tenuitvoerlegging van de wet betreffende de verklaringen van

overlijden en van vermoedelijk overlijden, alsmede betreffende de

overschrijving en de verbetering van sommige akten van de

burgerlijke stand.

10° De akten en vonnissen betreffende de rechtsplegingen vóór de

vrederechters bedoeld bij de wet houdende uitzonderingsbepalingen

in zake huishuur, wanneer het jaarlijks bedrag van de huurprijs,

eisbaar op het ogenblik van de indiening van de eis, niet hoger is dan

300 EUR.

###### Art. 301. bis

(opgeheven bij art. 72, 1° van de wet van 29.03.1962 (B.S., 12.04.1962). Tekst

van toepassing vanaf 202.04.1962 (art. 77))

(…)

###### Art. 301. ter

(impliciet opgeheven bij art. 2 van de wet van 24.01.1958 (B.S., 14.02.1958).

Tekst van toepassing vanaf 24.02.1958 (art. -))

(…)

###### Art. 301. quater

(ingevoegd bij art. 3 van de wet van 25.05.1951 (B.S., 31.05.1951). Tekst van

toepassing vanaf 10.06.1951 (art. -))

Kosteloos worden geregistreerd de akten, waarbij aan de

gerechtigden van de wet van 1 oktober 1947 betreffende de

herstelling van de oorlogsschade aan private goederen, uit de hand

woonhuizen worden verkocht die op initiatief van de Staat met het

oog op de huisvesting van de geteisterden door oorlogsfeit werden

gebouwd.

###### Artikel 302

###### Art. 302. bis

(aangevuld bij art. 9 van de wet van 04.08.1978 (B.S. 17.08.1978). Tekst van

toepassing vanaf 27.08.1978 (art. -))

§ 1. Wordt van het evenredig recht vrijgesteld, de inbreng in

vennootschappen die de rechtspersoonlijkheid bezitten en die de

verwezenlijking nastreven van verrichtingen als bedoeld bij artikel 10

van de wet betreffende de economische expansie.

Te dien einde, zal de Minister die Economische zaken,

Streekeconomie of Middenstand in zijn bevoegdheid heeft, vóór het

verlijden van de akte een bewijsstuk afgeven, waarvan de

afgiftemodaliteiten door de Koning worden bepaald. Dit stuk moet

aan de akte worden gehecht op het ogenblik van de registratie.

§  2.  Wordt,  overeenkomstig  de  voorwaarden  en

toepassingsmodaliteiten als bepaald in § 1, van het evenredig recht

vrijgesteld,  de  inbreng  in  vennootschappen  die  de

rechtspersoonlijkheid bezitten en die in titel I, artikel 2, van de wet tot

economische heroriëntering zijn bedoeld.

###### Art. 302. ter

(opgeheven bij art. 27 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst

van toepassing vanaf 25.11.2025 (art. 28))

(…)

###### Art. 302. quater

(opgeheven bij art. 15, 1° van de wet van 24.12.1993 (B.S., 31.12.1993 - ed.

2). Tekst van toepassing vanaf 01.01.1994 (art. 26))

(…)

###### Artikel 303

Worden van hypotheekrecht vrijgesteld:  Sont exemptées du droit d’hypothèque :

1° hypothecaire inschrijvingen genomen tot waarborg van de in

artikel 301, 1° en 2°, bedoelde leningen en kredietopeningen;

2° Inschrijvingen genomen ter uitvoering van de wet van 27 maart

1924, betreffende de Nationale Vereniging van nijveraars en

handelaars voor het herstel der oorlogsschade.

###### Artikel 304

(aangevuld  bij  art.  39  samengeordende  wetten  houdende

uitzonderingsbepalingen inzake huishuur gecoördineerd door Besluit Regent van

31.01.1949 (B.S., 23.02.1949). Tekst van toepassing vanaf 05.03.1949 (art. -))

Is vrij van rolrecht, de inschrijving van de zaken waarvan vonnissen en

arresten krachtens artikel 301 vrijstelling van de registratieformaliteit

genieten.

De vonnissen en arresten zijn vrij van expeditierecht.  Les jugements et arrêts sont exemptés du droit de greffe

Die vrijstellingen zijn evenwel niet toepasselijk in het geval bedoeld bij

artikel 301, 10°.

###### Art. 304. bis

(opgeheven bij art. 15, 2° van de wet van 24.12.1993 (B.S., 31.12.1993 - ed.

2). Tekst van toepassing vanaf 01.01.1994 (art. 26))

(…)

###### Artikel 305

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

van toepassing vanaf 30.09.1967 (art. -))

(…)

OVERGANGSBEPALINGEN  DISPOSITIONS TRANSITOIRES

#### Afdeling I - Algemene maatregelen

###### Artikel 306

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 307

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 308

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 309

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 311

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 312

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 313

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 314

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

#### Afdeling II - Bijzondere maatregelen

###### Artikel 315

(opgeheven bij art. 42 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst

van toepassing vanaf 01.01.1980 (art. 45, § 1, 4°))

(…)

###### Artikel 316

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

§ 2. Burgerlijke en handelsvennootschappen  § 2. Sociétés civiles et commerciales

###### Artikel 317

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst

van toepassing vanaf 01.01.1990 (art. 244))

(…)

###### Artikel 318

(opgeheven bij art. 19, 2° van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst

van toepassing vanaf 04.05.1965 (art. -))

(…)

BIJBEPALINGEN BETREFFENDE DE MET HET ZEGEL

##### GELIJKGESTELDE TAKSEN

###### Artikel 319

(…)

###### Artikel 320

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969).

Tekst van toepassing vanaf 01.01.1971 (art. 98))

(…)

###### Artikel 321

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969).

Tekst van toepassing vanaf 01.01.1971 (art. 98))

(…)

INWERKINGTREDING  ENTREE EN VIGUEUR

###### Artikel 322

Dit besluit treedt in werking op 1 Februari 1940.  Le présent arrêté entrera en vigueur le 1 er février 1940.