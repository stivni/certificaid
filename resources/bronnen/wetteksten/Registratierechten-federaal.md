---
bijgewerkt: 01.04.2026
bron: Fisconetplus.be (officieuze gecoördineerde versie)
chunk:
  level: 6
  sub_strategy:
  type: Art.
itaa-lex-sectie: VIII
provenance:
  inputs:
    - id: resources/raw/wetteksten/Registratierechten-federaal.pdf
      sha256: 768b62551dcd235cd7e3859626df172408bca181bdd6aceb8c7f153ced5d65c2
      version: 01.04.2026
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:21:47Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:30:31Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A8: doorheen het volledige bestand staat kolom-bleed: elke artikeltekst bevat twee kolommen (NL links, FR rechts) die op dezelfde regel gemengd zijn — bv. regel 71: 'KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie- (A hypotheek-...' of regel 81: 'Registratie is een formaliteit bestaande in het afschrijven... L'e vermelden van een akte...'. Dit is een systematisch A8-kolom-bleed-artefact door tweetalig PDF-extract. B4: regel 67 '## EN GRIFFIERECHTEN' is een losstaand heading-fragment (titelrest). F1: de `bron_rol`-veld ontbreekt in de frontmatter (wel `bron` aanwezig, maar `bron_rol` is leeg)."
    layer1:
      file_size_chars: 1123028
      flags:
        - detail: 'langste sectie op ######-niveau: 128584 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          name: max_section_size
          samples: []
          status: warn
        - detail: 3 kolom-bleed-patroon/-en gevonden buiten tabellen (twee-kolom PDF-extractie?)
          name: no_column_bleed
          samples:
            - 'regel 171: Wordt, voor de toepassing van dit wetboek, met een aan een                        Pour l’application du présent code, es'
            - 'regel 240: De exequaturs der scheidsrechterlijke uitspraken en die der                            Les exequatur des sentences arbit'
            - 'regel 1985: Wanneer er niet anderszins bij deze titel over beschikt is, mag het                    Lorsqu’il n’en est pas disposé au'
          status: warn
      heading_count: 525
      max_section_chars: 128584
      run_at: '2026-05-11T13:40:46Z'
      run_id: 20260511-134044
      status: warn
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:30:31Z'
      rationale: "A8: doorheen het volledige bestand staat kolom-bleed: elke artikeltekst bevat twee kolommen (NL links, FR rechts) die op dezelfde regel gemengd zijn — bv. regel 71: 'KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie- (A hypotheek-...' of regel 81: 'Registratie is een formaliteit bestaande in het afschrijven... L'e vermelden van een akte...'. Dit is een systematisch A8-kolom-bleed-artefact door tweetalig PDF-extract. B4: regel 67 '## EN GRIFFIERECHTEN' is een losstaand heading-fragment (titelrest). F1: de `bron_rol`-veld ontbreekt in de frontmatter (wel `bron` aanwezig, maar `bron_rol` is leeg)."
      concrete_problemen:
        - regel: 67
          categorie: B4
          type: other
          voorbeeld: '## EN GRIFFIERECHTEN'
        - regel: 71
          categorie: A8
          type: column-bleed
          voorbeeld: KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie-              (A hypotheek-
        - regel: 81
          categorie: A8
          type: column-bleed
          voorbeeld: Registratie is een formaliteit bestaande in het afschrijven...        L'e vermelden van een akte
        - regel: 171
          categorie: A8
          type: column-bleed
          voorbeeld: Wordt, voor de toepassing van dit wetboek, met een aan een                        Pour l'application du présent code, es
        - regel: 240
          categorie: A8
          type: column-bleed
          voorbeeld: De exequaturs der scheidsrechterlijke uitspraken en die der                            Les exequatur des sentences arbit
status: beschikbaar
tags:
  - VIII
  - '2.5'
  - '2.6'
wet: Wetboek der Registratie-, Hypotheek- en Griffierechten — federaal
---

# Registratierechten — federaal

*Bijgewerkt tot en met 01.04.2026 — gecoördineerde versie.*

## EN GRIFFIERECHTEN

(officieuze coördinatie)

(KB nr. 64 van 30.11.1939, bevattende het Wetboek der registratie-              (A hypotheek- en griffierechten (B.S. 01.12.1939) err. (B.S., 03.12.1939 en B.S.   d’e 13.12.1939). Dit KB werd bekrachtigd bij art. 2 van de wet van 16.06.1947       03 (B.S. 14.08.1947) err. (B.S., 26.10.1947))                                      16

## TITEL I - REGISTRATIERECHT

### HOOFDSTUK I - Formaliteit der registratie en vestiging van de belasting

###### Art. 1

(gewijzigd bij art. 79 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).    (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                 ap

Registratie is een formaliteit bestaande in het afschrijven, ontleden of        L’e vermelden van een akte of van een geschrift, in een hiertoe bestemd             l’a register     van       de     Algemene         Administratie     van      de    de Patrimoniumdocumentatie of op elke andere informatiedrager                      pa bepaald door de Koning.

Deze formaliteit geeft aanleiding tot heffing van een belasting                 Ce genaamd registratierecht.                                                       d’

###### Art. 2

(gewijzigd bij art. 111 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).   (m Tekst van toepassing vanaf 17.08.2020 (art. -))                                 ap

De akten worden op de minuten, brevetten of originelen                          Le geregistreerd.

Evenwel worden de buitenlands verleden authentieke akten in                    To minuut op de uitgiften, afschriften of uittreksels geregistreerd.              ac

De Koning kan voor de door Hem aangewezen categorieën van akten,               Le geschriften en verklaringen die aan de formaliteit van de registratie          dé onderworpen worden, bepalen dat zij onder de vorm van de minuut,               dé een afschrift of een kopie en al dan niet op gedematerialiseerde wijze,        l’e ter registratie kunnen of moeten worden aangeboden. Voor de aldus              dé aangewezen categorieën van akten, geschriften en verklaringen                  d’ bepaalt Hij de modaliteiten van de aanbieding ter formaliteit en van           pr de uitvoering van de formaliteit alsook de voorschriften die voor de           les juiste heffing van de verschuldigde rechten nodig zijn. Hij kan daarbij        ef afwijken van de bepalingen van de artikelen 6, tweede lid, 8, 9, 26, 39,       39 40, 168, 171 en 172 van dit Wetboek. Hij kan echter geen geldboete             d’ opleggen met een bedrag hoger dan 25 euro in geval van overtreding             17 van de door hem in afwijking van de artikelen 171 en 172 vastgestelde regels.

De Koning kan bepalen dat wanneer de aanbieding ter registratie van            Le akten of van bepaalde categorieën van akten op gedematerialiseerde             ac wijze geschiedt, de aanbieding vergezeld moet gaan van                         do gestructureerde metagegevens betreffende de akte, waaronder in                 do het bijzonder, voor elke partij bij de akte, haar identificatienummer in       d' het Rijksregister of het haar in uitvoering van artikel 4, § 2, van de wet     d' van 15 januari 1990 houdende oprichting en organisatie van een                 4, Kruispuntbank       van     de      sociale     zekerheid     toegekende       l'o identificatienummer in het bisregister of, voor een rechtspersoon, zijn        en ondernemingsnummer bedoeld in artikel III. 17 van het Wetboek van              l’a economisch recht.

Onverminderd het derde en het vierde lid, worden de vonnissen en               Sa arresten geregistreerd op een door de griffier eensluidend verklaard           en afschrift dat op elektronische wijze wordt aangeboden, behoudens               pa overmacht of technische storing in welk geval de aanbieding gebeurt            dy op papier. De vermelding van de registratie wordt aan de griffier              pa verzonden samen met het geregistreerde vonnis of arrest, op                    ju dezelfde wijze als dat laatste werd aangeboden.                                ét

Onverminderd het derde en het vierde lid, worden de onderhandse                Sa akten geregistreerd op een origineel of op een kopie, met uitzondering         en van de akten bedoeld in artikel 19, eerste lid, 3° die op een kopie            àl worden geregistreerd.

###### Art. 2bis

(ingevoegd bij art. 43 van de wet van 21.12.2013 (B.S., 31.12.2013 – ed. 2).   (in Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))                           ap

De registratie van de notariële akten vereist de vermelding van het                L’e identificatienummer of het ondernemingsnummer bedoeld in artikel                   nu 2, vierde lid, voor elke partij bij de akte, wanneer dit nummer                    ali beschikbaar is.                                                                    di

Deze vermelding geschiedt in de akte of, ten laatste bij de aanbieding             Ce ervan ter registratie, in een aanvullende verklaring onderaan de akte,             pr getekend door de betrokken partij of door de instrumenterende                      pi notaris, in haar naam.                                                             no

###### Art. 2ter

(ingevoegd bij art. 44 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).       (in Tekst van toepassing vanaf: a) wat de akten bedoeld in art. 19, 1e lid, 3°, a),    ap e àp b), van hetzelfde Wetboek betreft, vanaf 01.06.2014 (art. 87, 4°, a en b))         ae

De vermeldingsplicht bedoeld in artikel 2bis, eerste lid, geldt ook voor           L'o de registratie van de akten bedoeld in artikel 19, eerste lid, 3°, wat             po betreft rechtspersonen.                                                            ce

Indien aan een partij bij een dergelijke akte nog geen                             Lo ondernemingsnummer is toegekend, bevestigt die partij dit in de akte               nu of in een ondertekende aanvullende verklaring onderaan de akte.                    dé

###### Art. 2quater

(lid 3, vervangen bij art. 58 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.    (al 2). Tekst van toepassing vanaf 09.06.2024 (art. -))                                Te

De registratie van een akte bedoeld in artikel 19, eerste lid, 3°, al dan          L'e niet samen met bijlagen, of van een plaatsbeschrijving die niet samen              sa met de hiervoor bedoelde akte wordt aangeboden, is, in geval van                   vis aanbieding op een papierendrager, afhankelijk van de aanbieding                    pa samen met de te registreren documenten van een volledig en                         en leesbaar ingevuld formulier waarvan het model wordt bepaald door                   do de Koning.

Het formulier kan de verplichte vermelding bevatten van het                        Le identificatienummer of het ondernemingsnummer, bedoeld in artikel                  d' 2, vierde lid, van de partijen bij de akte, wanneer dit nummer                     de beschikbaar is.

De aanbieding ter registratie van de in het eerste lid bedoelde                La documenten wordt gedaan door ze via een aanbieder van                          a postdiensten te sturen naar het adres dat door de Koning wordt                 dé bepaald.

In geval de uitvoering van de formaliteit van de registratie wordt             En geweigerd wegens niet naleving van de voorgaande bepalingen,                   du wordt de verzoeker daarvan in kennis gesteld.                                  in

Dit artikel is niet van toepassing in het geval bepaald in artikel 25.         Le

###### Art. 3

(gewijzigd bij art. 80 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).   (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                ap

Wordt een in een andere taal dan de landstalen gestelde akte of                S’ geschrift ter registratie aangeboden, zo kan het bevoegde kantoor              lan van de Algemene Administratie van de Patrimoniumdocumentatie                   l’A eisen dat, op de kosten van de persoon die de formaliteit vordert, een         ex door een beëdigde vertaler voor echt verklaarde vertaling daaraan              fo worde toegevoegd.

###### Art. 4

De registratie is ondeelbaar: zij wordt toegepast op de gehele akte of         L’e het geheel geschrift welke tot de formaliteit wordt aangeboden.                de

###### Art. 5

(opgeheven bij art. 3 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1).    (ab Tekst van toepassing vanaf 29.06.2020 (art. -))                                ap

(…)                                                                            (…

###### Art. 5bis

(vervangen bij art. 93 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed.       (re 1). Tekst van toepassing vanaf 07.02.2022 (art. -))                            ap

Een akte die wordt aangeboden ter registratie en ter hypothecaire              Un overschrijving, wordt tezelfdertijd tot de beide formaliteiten                 l’e aangeboden, behalve indien de termijnen voor de aanbieding ervan               di verschillen.

Bij gelijktijdige aanbieding tot de formaliteiten, wordt de registratie        En van de akte geweigerd zolang op dit kantoor de overschrijving wordt            de geweigerd.                                                                     bu

Het eerste en tweede lid zijn niet van toepassing op een akte die enkel        Le de niet-vatbaarheid voor beslag vaststelt van de woning van een                ex zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse              pa bepalingen (IV).

###### Art. 6

(gewijzigd bij art. 82 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).   (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                ap

Het bevoegde kantoor van de Algemene Administratie van de                      Le Patrimoniumdocumentatie is gehouden tot het registreren van de                 Do akten of geschriften op de datum waarop ze onder de wettelijke                 à voorwaarden tot de formaliteit worden aangeboden.                              lég

Een buiten de openingsuren van de kantoren aangeboden akte of                  Un geschrift, wordt geacht aangeboden te zijn bij de eerstvolgende                bu opening van de kantoren.                                                       bu

Het kantoor mag ze niet langer houden dan nodig is.                            Le

###### Art. 7

(gewijzigd bij art. 83 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).   (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                ap

Zo een akte of geschrift, waarvan er geen minuut bestaat, inlichtingen         Si vervat die kunnen dienen om aan 's Rijks schatkist verschuldigde               re sommen te ontdekken, heeft het bevoegde kantoor van de Algemene                le Administratie van de Patrimoniumdocumentatie het recht er een                  Do afschrift van te maken en dit eensluidend met het origineel te doen            ce waarmerken door de werkende openbare officier of, zo het gaat om               s’a een onderhandse of buitenlands verleden akte, door de betrokken                in persoon die de formaliteit heeft gevorderd. Bij weigering, waarmerkt           co het bevoegde kantoor zelf de eensluidendheid van het afschrift, met            de vermelding van die weigering. Het aldus gewaarmerkt afschrift                  pr

wordt, behoudens bewijs van het tegendeel, als eensluidend aangezien.

###### Art. 8

(gewijzigd bij art. 4 van de wet van 11.06.2020 (B.S., 19.06.2020 - ed. 1). Tekst   (m van toepassing vanaf 29.06.2020 (art. -))                                           ap

Vermelding van de registratie wordt op de akte of het geschrift                     La gesteld naar een door de minister van Financiën bepaalde tekst.                     lib

Voor akten en geschriften als bedoeld in artikel 2quater, wordt de                  Po vermelding van de registratie gesteld volgens door de Koning te                     l'e bepalen nadere regels.                                                              Ro

Indien er toepassing gemaakt wordt van de vrijstelling voorzien in                  Lo artikel 8bis, wordt de vermelding van de registratie vervangen door de              re vermelding van de betaling die verricht moet worden volgens de                      pa modaliteiten voorzien in uitvoering van dit artikel. Deze vermelding                ar geschiedt naar een door de Minister van Financiën vastgestelde tekst.               de

###### Art. 8bis

(ingevoegd bij art. 135 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst         (in van toepassing vanaf 01.01.1990 (art. 244))                                         ap

De Koning kan bepaalde categorieën van de in de artikelen 19, 1° en                 Le
6°, 26 en 29 bedoelde akten van de registratieformaliteit vrijstellen               ca zonder dat deze vrijstelling de ontheffing van de op deze akten                     ce toepasselijke rechten meebrengt, alsook de betalingsmodaliteiten                    et voor genoemde rechten, binnen de termijnen die Hij bepaalt, regelen,                qu in voorkomend geval afwijkend van de bepalingen van hoofdstuk III                   ch en IX van deze titel. Indien er toepassing gemaakt wordt van deze                   di bepaling kan de Koning het neerleggen van een afschrift van de akten                de voorschrijven en aanvullende regels vaststellen om de juiste heffing                de van de belasting te verzekeren.

###### Art. 9

(gewijzigd bij art. 12 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van      (m toepassing vanaf 01.03.2021 (art. -))                                               ap

Valt de laatste dag van de termijn, die door onderhavig Wetboek                     Lo vastgesteld is voor de uitvoering van een formaliteit, op een                       l’e

sluitingsdag van de kantoren, dan wordt deze termijn verlengd tot de          dé eerste openingsdag der kantoren die volgt op het verstrijken van de           su termijn.

### HOOFDSTUK II - Indeling van de rechten en algemene                           CH heffingsregels

###### Art. 10

(gewijzigd bij art. 136 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (m van toepassing vanaf 01.01.1990 (art. 244))                                   ap

Er zijn evenredige en vaste registratierechten.                               Le

Vaste rechten zijn verdeeld in algemeen vast recht en specifieke vaste        Le rechten.                                                                      sp

###### Art. 11

(gewijzigd bij art. 11 van de Programmawet van 28.06.2013 (B.S.,              (m 01.07.2013 - ed. 2). Tekst van toepassing op alle akten en geschriften die    éd vanaf 01.07.2013 tot de formaliteit worden aangeboden (art. 13))              du

De evenredige en de specifieke vaste rechten worden geheven                   Le volgens het in dit Wetboek vastgestelde tarief.                               ta

Het algemeen vast recht is van toepassing op al de in dat tarief niet         Le voorziene akten en geschriften.                                               da

Het algemeen vast recht bedraagt 50 EUR.                                      Le

###### Art. 12

Het evenredig of specifiek vast recht wordt slechts eenmaal op een            Le rechtshandeling geheven, wat ook het getal zij van de geschriften die         su daarvan laten blijken.                                                        co

###### Art. 13

Geven slechts aanleiding tot heffing van het algemeen vast recht,               Ne tenzij daarin een toevoeging of wijziging voorkomt welke van die aard           un is dat ze de heffing van een nieuw of aanvullend recht ten gevolge              d’ heeft:

1° Alle nieuw geschrift opgemaakt om te laten blijken van een                   1 rechtshandeling waarop reeds het evenredig of specifiek vast recht              dé werd geheven;

2° Alle geschrift houdende bekrachtiging, bevestiging, uitvoering, aan          2 vulling of voltrekking van geregistreerde vroegere akten, indien het            co niet laat blijken van nieuwe rechtshandelingen welke als dusdanig aan           ne een evenredig of specifiek vast recht onderhevig zijn.                          àu

Geven insgelijks slechts aanleiding tot heffing van het algemeen vast           Ne recht, die rechtshandelingen welke ter oorzake van nietigheid,                  ju ontbinding of om andere reden opnieuw werden verricht zonder enige              au verandering     welke     iets   toevoegt     aan   het    voorwerp      der    va overeenkomsten of aan derzelver waarde, ten ware het op de eerste               n’ handeling geheven evenredig recht teruggegeven werd of voor teruggaaf vatbaar zij.

###### Art. 14

(vervangen bij art. 2 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (re toepassing vanaf 17.01.1959 (art. -))                                           ap

Wanneer een akte verscheidene onder dezelfde contractanten tot                  Lo stand gekomen beschikkingen vervat, welke de ene van de andere                  dé afhankelijk zijn of de ene uit de andere noodzakelijk voortvloeien, is          en slechts één recht voor deze gezamenlijke beschikkingen verschuldigd.            de

Het recht wordt geheven met inachtneming van diegene van                        Le bedoelde beschikkingen welke tot het hoogste recht aanleiding geeft.            dr

###### Art. 15

Wanneer, in een akte, verscheidene onafhankelijke of niet                       Lo noodzakelijk uit elkaar voortvloeiende beschikkingen voorkomen, is              ne voor elk dier beschikkingen en wel naar eigen aard een bijzonder recht          ch verschuldigd.

Deze regel is niet van toepassing op het algemeen vast recht.                   Ce

###### Art. 16

De rechtshandeling waarop het evenredig recht verschuldigd is, doch               L’a welke aan een schorsende voorwaarde onderworpen is, geeft alleen                  co tot heffing van het algemeen vast recht aanleiding zolang de                      lo voorwaarde niet is vervuld.

Wordt de voorwaarde vervuld, zo is het recht verschuldigd dat bij het             Lo tarief voor de handeling is vastgesteld, behoudens toerekening van                sa het reeds geheven recht. Het wordt berekend naar het tarief dat van               vig kracht was op de datum waarop het recht aan de Staat zou verworven                et geweest zijn indien de handeling een onvoorwaardelijke was                        co geweest, en op de bij dit wetboek vastgelegde en op de datum van de vervulling der voorwaarde beschouwde belastbare grondslag.

###### Art. 17

Wordt, voor de toepassing van dit wetboek, met een aan een                        Po schorsende voorwaarde onderworpen handeling gelijkgesteld, de                     co rechtshandeling door een rechtspersoon verricht en aan machtiging,                su goedkeuring of bekrachtiging van overheidswege onderworpen.                       su

###### Art. 18

(§ 2, vervangen bij art. 168 van de programmawet van 29.03.2012 (B.S.,            (§ 06.04.2012 - ed. 3). Tekst van toepassing te weten op de rechtshandelingen        06 of het geheel van rechtshandelingen die éénzelfde verrichting tot stand brengt,   jur die zijn gesteld vanaf 01.06.2012 (art. 169))                                     01

§ 1. De datum van de onderhandse akten over 't algemeen of van de                 §1 overeenkomsten die door het feit alleen van haar bestaan verplicht                as aan de formaliteit van registratie onderworpen zijn, kan niet tegen het           ex bestuur worden ingeroepen dan voor zover hij tegen derden kan                     el worden ingeroepen. Registratie sluit geen erkenning door het bestuur              re in van de datum der akte of der overeenkomst.                                     co

§ 2. Aan de administratie kan niet worden tegengeworpen, de                       § rechtshandeling noch het geheel van rechtshandelingen dat een                     l’e zelfde verrichting tot stand brengt, wanneer de administratie door                l’a vermoedens of door andere in artikel 185 bedoelde bewijsmiddelen                  de en aan de hand van objectieve omstandigheden aantoont dat er                      ob sprake is van fiscaal misbruik.

Er is sprake van fiscaal misbruik wanneer de belastingschuldige door              Il middel van de door hem gestelde rechtshandeling of het geheel van                 l’e su

rechtshandelingen één van de volgende verrichtingen tot stand brengt:

1. een verrichting waarbij hij zichzelf in strijd met de doelstellingen van       1. een bepaling van dit Wetboek of de ter uitvoering daarvan genomen                 di besluiten buiten het toepassingsgebied van die bepaling plaatst; of               ci,

2. een verrichting waarbij aanspraak wordt gemaakt op een                         2. belastingvoordeel voorzien door een bepaling van dit Wetboek of de                un ter uitvoering daarvan genomen besluiten en de toekenning van dit                 ce voordeel in strijd zou zijn met de doelstellingen van die bepaling en die         et in wezen het verkrijgen van dit voordeel tot doel heeft.

Het komt aan de belastingschuldige toe te bewijzen dat de keuze voor              Il a zijn rechtshandeling of het geheel van rechtshandelingen door andere              ou motieven verantwoord is dan het ontwijken van registratierechten.                 qu

Indien de belastingschuldige het tegenbewijs niet levert, dan wordt de            Lo verrichting aan een belastingheffing overeenkomstig het doel van de               so wet onderworpen alsof het misbruik niet heeft plaatsgevonden.                     l’a

### HOOFDSTUK III - Registratieverplichting

Eerste afdeling - Akten en verklaringen aan de formaliteit onderworpen

###### Art. 19

(lid 1, 5°, gewijzigd bij art. 20 van de wet van 10.02.2026 (B.S., 27.02.2026).   (al Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))                           Te

Moeten binnen de bij artikel 32 gestelde termijnen geregistreerd                  Do worden:

1° De akten van notarissen; de exploten en processen-verbaal van                  1 gerechtsdeurwaarders, met uitzondering van de protesten zoals                     de bedoeld in de protestwet van 3 juni 1997; de arresten en vonnissen                les der hoven en rechtbanken die bepalingen bevatten welke door deze                  co titel aan een evenredig recht onderworpen worden;                                 pr

2° De akten waarbij de eigendom of het vruchtgebruik van in België                2 gelegen onroerende goederen overgedragen of aangewezen wordt;                     d’

3° a) De akten houdende verhuring, onderverhuring of overdracht van             3 huur van in België gelegen onroerende goederen of gedeelten van                 ou onroerende goederen, die uitsluitend bestemd zijn tot huisvesting van           au een gezin of van één persoon;

b) De andere dan onder a) bedoelde akten houdende verhuring,                    b) onderverhuring of overdracht van huur van in België gelegen                     ce onroerende goederen of gedeelten van onroerende goederen.                       Be

4° De processen-verbaal van openbare verkoping van lichamelijke                 4 roerende voorwerpen;                                                            co

5° De akten houdende inbreng van goederen in vennootschappen                    5° met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke                pe leiding in België, hetzij de statutaire zetel in België en de zetel der         en werkelijke leiding buiten het grondgebied van de lidstaten van de               di Europese Unie, is gevestigd;                                                    eu

6° de in het buitenland verleden notariële akten die titel vormen voor          6° een schenking onder de levenden van roerende goederen door een                  do rijksinwoner.

Onverminderd de bepaling onder 6° van het eerste lid en behoudens               Sa wat de bepalingen onder 2°, 3° en 5° van hetzelfde lid betreft,                 3° worden in dit artikel alleen de in België verleden akten bedoeld.               pa

###### Art. 20

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van   (ab toepassing vanaf 01.01.1961 (art. 39))                                          àp

(…)                                                                             (…

###### Art. 211

(vervangen bij art. 59 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).    (re Tekst van toepassing vanaf 09.06.2024 (art. -))                                 ap

De bevoegde dienst van de Algemene administratie van de                         Le patrimoniumdocumentatie neemt een kopie bij de aanbieding ter                   do registratie op een papieren drager van de volgende akten, haar                  à bijlagen en alle andere tegelijk aan te bieden stukken, geschriften en          to verklaringen:                                                                   dé

1° de plaatsbeschrijving bedoeld in artikel 2quater, eerste lid;                1°

2° de onderhandse of in het buitenland verleden akten bedoeld in                2° artikel 19, eerste lid, 2°, behalve wanneer het gaat om een akte welke          àl onder de minuten van een notaris in België berust of bij zijn minuten           m is gevoegd;

3° de onderhandse of in het buitenland verleden akten bedoeld in                3° artikel 19, eerste lid, 3°, 5° en 6°, behalve wanneer het gaat om een           à akte welke onder de minuten van een notaris in België berust of bij             au zijn minuten is gevoegd;                                                        m

4° de verklaringen bedoeld in artikel 31.                                       4°

De Koning kan de categorie van akten, geschriften en verklaringen               Le bedoeld in het eerste lid vervolledigen of wijzigen.                            dé

De kopie bedoeld in het eerste lid wordt minstens gedurende tien jaar           La bewaard door de bevoegde dienst van de Algemene administratie van               pa de patrimoniumdocumentatie, voor zover deze niet wordt                          do overgedragen aan het Rijksarchief of vernietigd in uitvoering van de            Ar artikelen 1 en 5 van de archiefwet Wet van 24 juni 1955.                        du

###### Art. 212

(gewijzigd bij art. 1 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van   (m toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van       ap 19.12.1969 (B.S., 20.12.1969))                                                  19

Als onroerende goederen worden niet beschouwd:                                  Ne

1° Voor de toepassing van de artikelen 19, 3° en 83, brandkasten, in            1° huur gegeven door personen, verenigingen, gemeenschappen of                     en vennootschappen die gewoonlijk brandkasten verhuren;                            so

2° Voor de toepassing van dit Wetboek, lichamelijk roerende                     2° voorwerpen aangewend tot de dienst en de exploitatie van                        af onroerende goederen.

###### Art. 22

(opgeheven bij art. 3 van de wet van 10.06.1997 (B.S., 19.07.1997). Tekst van   (ab toepassing voor de effecten die ter betaling worden aangeboden vanaf            po 23.09.1997 (art. 10, KB van 15.09.1997 (B.S., 23.09.1997))                      23

(…)                                                                             (…

###### Art. 23

De exequaturs der scheidsrechterlijke uitspraken en die der                            Le buitenslands gewezen rechterlijke beslissingen                   moeten,         bij   ju aanbieding ter registratie, vergezeld zijn van de desbetreffende                       l’e uitspraken of beslissingen.                                                            au

###### Art. 24

(opgeheven bij art. 2 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst van          (ab toepassing vanaf 01.01.1961 (art. 39))                                                 àp

(…)                                                                                    (…

###### Art. 25

(gewijzigd bij art. 3 van de wet van 03.12.2020 (B.S., 11.12.2020 - ed. 1). Tekst      (m van toepassing vanaf 15.12.2020 (art. 5))                                              ap

Wanneer een onderhandse of in het buitenland verleden akte bedoeld                     Lo in artikel 19, eerste lid, 2°, 3°, 5° of 6°, terzelfdertijd van een niet               l'a verplicht in België te registreren overeenkomst doet blijken, kunnen                   co de betrokkenen een door hen gewaarmerkt beknopt uittreksel                 (1) uit   in de akte doen registreren waarin alleen melding wordt gemaakt van                       an de overeenkomsten die verplicht in België te registreren zijn.                         ob

Het uittreksel wordt in dubbel opgemaakt. Wanneer beide                                L’e exemplaren ter registratie worden aangeboden, moeten ze vergezeld                      l’e zijn van de oorspronkelijke akte of, zo het een buitenslands verleden                  ou authentieke akte in minuut geldt, van een uitgifte daarvan. De heffing                 ex wordt beperkt tot die goederen welke het voorwerp van het uittreksel                   fo uitmaken. Een exemplaar van dit uittreksel blijft op het bevoegde                      bu kantoor         van       de    Algemene       Administratie        van          de    pa Patrimoniumdocumentatie berusten.
(1) ‘uittrek-sel’ in het B.S.

###### Art. 26

(laatste lid vervangen bij art. 47 van de wet van 21.12.2013 (B.S., 31.12.2013         (de - ed. 2). Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))                         éd

Geen akte of geschrift mag aan een van de krachtens artikel 19, 1°,            Au verplichtend te registreren akten, andere dan een vonnis of arrest,            ob worden gehecht, of onder de minuten van een notaris worden                     ju neergelegd zonder te voren geregistreerd te zijn.                              êt

Evenwel staat het de notarissen en de gerechtsdeurwaarders vrij de             To aangehechte of neergelegde akte tegelijk met de desbetreffende akte            pr ter registratie aan te bieden.                                                 te

De in het eerste lid bedoelde verplichting is niet van toepassing:             L'o

1° in geval van aanhechting of van neerlegging, onder de vorm van              1° minuut, uitgifte, afschrift of uittreksel, van in België verleden              civ gerechtelijke akten of akten van de burgerlijke stand;

2° in geval van aanhechting of van neerlegging van een plan dat is             2° opgenomen in de databank van plannen van afbakening van de                     de Algemene Administratie van de Patrimoniumdocumentatie, op                      la voorwaarde dat de akte, of een door de partijen of de                          dé instrumenterende ambtenaar, in hun naam, ondertekende verklaring               le onderaan de akte, verwijst naar deze opname met vermelding van het             m refertenummer van het plan en bevestigt dat het plan nadien niet is            pa gewijzigd.

###### Art. 27

(opgeheven bij art. 19 van de wet van 01.07.1983 (B.S., 08.07.1983). Tekst     (ab van toepassing vanaf 18.07.1983 (art. -))                                      ap

(…)                                                                            (…

###### Art. 28

(opgeheven bij art. 2/art. 28 van de wet van 10.10.1967 (B.S., 31.10.1967).    (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,       ap 13.11.1968))                                                                   13

(…)                                                                            (…

###### Art. 29

(gewijzigd bij art. 87 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).   (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                ap

Behoudens het bij artikel 173, 1°, voorziene geval, mag geen                     Ho overschrijving, inschrijving, doorhaling of randvermelding in de                 in registers van de hypothecaire openbaarmaking plaats hebben                       pu krachtens niet vooraf geregistreerde akten.                                      n’

###### Art. 30

(gewijzigd bij art. 88 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).     (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                  ap

Op vorig artikel wordt uitzondering gemaakt voor de overschrijvingen,            Il inschrijvingen, doorhalingen of randvermeldingen gedaan krachtens                tra akten in verband met scheepskredietverrichtingen gedaan onder het                ef voordeel der wet van 23 augustus 1948 of met kredietverrichtingen                m gedaan onder het voordeel der wet tot bevordering van de                         op financiering van de voorraden van de steenkoolmijnen.                            fin

Op vorig artikel wordt eveneens uitzondering gemaakt voor de in                  Il België verleden gerechtelijke akten van de burgerlijke stand, in                 ac minuut, uitgifte, afschrift of uittreksel.                                       m

###### Art. 31

(lid 1, 1°bis, gewijzigd bij art. 21 van de wet van 10.02.2026 (B.S.,            (al 27.02.2026). Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))             Te

Er bestaat verplichting tot ondertekening en tot aanbieding ter                  Il registratie, binnen de bij artikel 33 gestelde termijnen, van een                l’e verklaring in onderstaande gevallen:                                             da

1° Wanneer een overeenkomst, waarbij eigendom of vruchtgebruik                   1 van in België gelegen onroerende goederen overgedragen of                        d’ aangewezen wordt, niet bij een akte is vastgesteld;                              ac

1°bis Wanneer een inbreng van goederen in een vennootschap met                   1° rechtspersoonlijkheid, waarvan hetzij de zetel der werkelijke leiding in         pe België, hetzij de statutaire zetel in België en de zetel der werkelijke          Be leiding buiten het grondgebied van de lidstaten van de Europese Unie,            di is gevestigd, niet bij een akte is vastgesteld;                                  eu

1°ter (…)                                                                        1°

2° Wanneer de voorwaarde die de heffing van een recht heeft                      2 geschorst, vervuld wordt;                                                        vie

3° In de in artikelen 74 en 75 bedoelde gevallen.                                3

Deze door de contracterende partijen of door een van hen                         Ce ondertekende verklaring vermeldt: de aard en het doel van de                     d' overeenkomst, de datum ervan of de datum van het nieuwe feit dat                 ce de verschuldigdheid van het recht heeft doen ontstaan, de aanwijzing             dé van de partijen, de omvang van de goederen, de belastbare grondslag              et en alle voor de vereffening van de belasting nodige gegevens. Een                es kopie wordt bewaard door de bevoegde dienst van de Algemene                      de administratie van de patrimoniumdocumentatie.

Vanaf het verstrijken van vorenstaande termijnen wordt de door een               A der partijen ondertekende verklaring als van al de partijen uitgaande            de aangezien.

#### Afdeling II - Termijnen voor de aanbieding ter registratie

###### Art. 32

(7°, gewijzigd bij art. 22 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst   (7 van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                ap

De termijnen voor de aanbieding ter registratie van verplicht te                 Le registreren akten zijn:                                                          ob

1° voor akten van notarissen, vijftien dagen;                                    1°

De termijn is evenwel:                                                           Le

a) twee maanden, voor de in het kader van een openbare verkoop van               a) een onroerende goed opgemaakte processen-verbaal van:                            ve

i. het ontbreken van hoger bod;                                                  i. l

ii. definitieve toewijs;                                                         ii.

iii. het al dan niet uitoefenen van een voorkooprecht;                           iii.

iv. het vaststellen van het bekomen van een financiering;                        iv.

b) vier maanden, te rekenen van het overlijden van de erflaters of               b) schenkers voor:

i. de testamenten;                                                               i. l

ii. de schenkingen van toekomstige goederen gedaan tussen                        ii. echtgenoten       gedurende       het     huwelijk     andere      dan     bij   m huwelijkscontract;

iii. de akten van herroeping van de onder i en ii bedoelde akten;             iii.

iv. de verklaringen betreffende testamenten in de internationale              iv. vorm;

v. de akten van bewaargeving van een testament door de erflater.              v.

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten         Po van de registratie en van de hypothecaire overschrijving die bij de           l’e aanbieding ter registratie binnen de in het eerste lid gestelde termijn       pr niet werden geregistreerd wegens de weigering van de                          pa overschrijving, bedraagt de termijn zeven dagen te rekenen van de             de datum van de kennisgeving aan de notaris van deze weigering. Deze             re termijn verstrijkt niet voor het einde van de termijn bepaald,                l’a naargelang het geval, in het eerste lid of in het tweede lid, a);

2° Voor akten van gerechtsdeurwaarders, vier dagen;                           2°

3° voor arresten en vonnissen der hoven en rechtbanken, tien dagen;           3°

3°bis voor akten van bestuursoverheden en ambtenaren van de                   3° Staat, gefedereerde entiteiten, provincies, gemeenten en openbare             de instellingen die verplicht onderworpen zijn aan de formaliteit van de         co registratie en aan die van de hypothecaire overschrijving, vijftien           la dagen;                                                                        hy

De termijn is evenwel twee maanden voor de in het kader van een               Le openbare verkoop van een onroerende goed opgemaakte processen-                da verbaal van:

a) het ontbreken van hoger bod;                                               a)

b) definitieve toewijs;                                                       b)

c) het al dan niet uitoefenen van een voorkooprecht;                          c)

d) het vaststellen van het bekomen van een financiering.                      d)

Voor de akten die gelijktijdig worden aangeboden tot de formaliteiten         Po van de registratie en van de hypothecaire overschrijving, die bij de          l’e aanbieding ter registratie binnen de in het eerste lid gestelde termijn       pr niet werden geregistreerd wegens de weigering van de                          pa overschrijving, bedraagt de termijn zeven dagen te rekenen van de             de datum van de kennisgeving van deze weigering aan de                           au bestuursoverheden of ambtenaren van de Staat, gefedereerde                    de entiteiten, provincies, gemeenten en openbare instellingen. Deze              n’ termijn verstrijkt niet voor het einde van de termijn bepaald,                l’a naargelang het geval, in het eerste lid of in het tweede lid;

4° Voor akten waarbij de eigendom of het vruchtgebruik van in België             4° gelegen onroerende goederen overgedragen of aangewezen wordt,                    pr vier maanden;

5° Voor akten van verhuring, onderverhuring of overdracht van huur               5° bedoeld in artikel 19, 3°, a), twee maanden en voor akten van                    ba verhuring, onderverhuring of overdracht van huur bedoeld in artikel              ba 19, 3°, b), vier maanden;

6° Voor processen-verbaal van openbare verkoping van lichamelijke                6° roerende goederen opgemaakt door bestuursoverheden en                            m ambtenaren van de Staat, gefedereerde entiteiten, provincies,                    ag gemeenten en openbare instellingen, één maand;                                   et

7° Voor akten houdende inbreng van goederen in vennootschappen                   7° met rechtspersoonlijkheid waarvan hetzij de zetel der werkelijke                 so leiding in België, hetzij de statutaire zetel in België en de zetel der          de werkelijke leiding buiten het grondgebied van de lidstaten van de                Be Europese Unie is gevestigd, vier maanden;                                        m

8° voor de in artikel 19, eerste lid, 6°, bedoelde akten, vier maanden.          8°

###### Art. 33

(gewijzigd bij art. 60 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (m toepassing vanaf 01.04.1999 (art. 80, § 31))                                     àp

De termijn, binnen welke de in artikel 31 voorziene verklaringen ter             Le registratie moeten aangeboden worden, is vier maand ingaande met                 es de datum van de overeenkomst of, in voorkomend geval, van de                     éc vervulling van de voorwaarde welke de heffing van het recht heeft                la geschorst.

###### Art. 34

(opgeheven bij art. 77 van de wet van 18.12.2015 (B.S., 28.12.2015 - ed. 2).     (ab Tekst van toepassing vanaf 07.01.2016 (art. -))                                  ap

(…)                                                                              (…

Vierde lid: gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van       Al 16.01.1989 betreffende de financiering van de gemeenschappen en de               16 gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

#### Afdeling III - Personen verplicht tot aanbieding ter registratie

###### Art. 35

(lid 5, vervangen bij art. 61 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De verplichting tot aanbieding ter registratie van akten of verklaringen              L’o en tot betaling van de des betreffende rechten en gebeurlijk de                       les geldboeten, waarvan de vorderbaarheid uit bewuste akten of                            ré verklaringen blijkt, berust ondeelbaar:                                               sa

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de                       1 akten van hun ambt;                                                                   m

2° (…)                                                                                2

3° (…)                                                                                3

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de                          4 akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in                   an handen neergelegd, zonder voorafgaande registratie;                                   pr

5° Op de bestuursoverheden en ambtenaren van de Staat,                                5 gefedereerde entiteiten, provincies, gemeenten en openbare                            fé instellingen, ten aanzien van de door hen opgemaakte akten;                           pu

6° Op de contracterende partijen, ten aanzien van de onderhandse of                   6 buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b)                 pa en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;                    dé

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands                     7 verleden akten waarvan sprake in artikel 19, 3°, a);                                  vis

8° op de contracterende partijen ten aanzien van de in artikel 19,                    8° eerste lid, 6°, bedoelde akten.                                                       1e

De verplichting tot aanbieding ter registratie van de arresten en                     L’o vonnissen van hoven en rechtbanken berust op de griffiers. In                         et afwijking van artikel 169ter worden deze arresten en vonnissen in                     ce debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten                      L'o waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van                     de

hoven en rechtbanken, berust op de verweerders, elkeen in de mate              dé waarin de veroordelingen, vereffeningen of rangregelingen te zijnen            ou laste werden uitgesproken of vastgesteld, en op de verweerders                 so hoofdelijk in geval van hoofdelijke veroordeling.

Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een        Si overeenkomst waarbij de eigendom of het vruchtgebruik van in België            un gelegen onroerende goederen overgedragen of aangewezen wordt, zijn             d’ die rechten en boeten ondeelbaar verschuldigd door de personen die             in partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald               Le binnen de termijn van één maand, te rekenen vanaf de dag van de                m verzending van de aangetekende zending van het belastingbericht                l'a door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van             Lo de boeten geen gekende woonplaats in België of in het buitenland               pa heeft, wordt het bericht aan de procureur des Konings te Brussel               es verzonden.

#### Afdeling III - Personen verplicht tot aanbieding ter registratie

###### Art. 35

(gewijzigd bij art. 95 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).   (m Tekst van toepassing vanaf 07.02.2022 (art. -))                                ap

De verplichting tot aanbieding ter registratie van akten of verklaringen       L’o en tot betaling van de des betreffende rechten en gebeurlijk de                les geldboeten, waarvan de vorderbaarheid uit bewuste akten of                     ré verklaringen blijkt, berust ondeelbaar:                                        sa

1° Op de notarissen en gerechtsdeurwaarders, ten aanzien van de                1 akten van hun ambt;                                                            m

2° (…)                                                                         2

3° (…)                                                                         3

4° De notarissen en gerechtsdeurwaarders, ten aanzien van de                   4 akten, overeenkomstig artikel 26 aan hun akten gehecht of in hun in            an handen neergelegd, zonder voorafgaande registratie;                            pr

5° Op de bestuursoverheden en ambtenaren van de Staat,                         5 gefedereerde entiteiten, provincies, gemeenten en openbare                     fé instellingen, ten aanzien van de door hen opgemaakte akten;                    pu

6° Op de contracterende partijen, ten aanzien van de onderhandse of            6 buitenslands verleden akten, waarvan sprake in artikel 19, 2°, 3°, b)          pa en 5°, en ten aanzien van de in artikel 31 voorziene verklaringen;             dé

7° Op de verhuurder ten aanzien van de onderhandse of buitenlands              7 verleden akten waarvan sprake in artikel 19, 3°, a);                           vis

8° op de contracterende partijen ten aanzien van de in artikel 19,             8° eerste lid, 6°, bedoelde akten.                                                1e

De verplichting tot aanbieding ter registratie van de arresten en              L’o vonnissen van hoven en rechtbanken berust op de griffiers. In                  et afwijking van artikel 169ter worden deze arresten en vonnissen in              ce debet geregistreerd.

De verplichting tot betaling van de rechten en van de geldboeten               L'o waarvan de vorderbaarheid blijkt uit de arresten en vonnissen van              de hoven en rechtbanken, berust op de verweerders, elkeen in de mate              dé waarin de veroordelingen, vereffeningen of rangregelingen te zijnen            ou laste werden uitgesproken of vastgesteld, en op de verweerders                 so hoofdelijk in geval van hoofdelijke veroordeling.

Zo op een vonnis of arrest verschuldigde rechten en boeten slaan op een        Si overeenkomst waarbij de eigendom of het vruchtgebruik van in België            un gelegen onroerende goederen overgedragen of aangewezen wordt, zijn             d’ die rechten en boeten ondeelbaar verschuldigd door de personen die             in partijen bij de overeenkomst zijn geweest.

De rechten en, in voorkomend geval, de geldboeten worden betaald               Le binnen de termijn van één maand, te rekenen vanaf de dag van de                d’ verzending van het belastingbericht bij ter post aangetekende brief            po door de ontvanger.

Wanneer de schuldenaar van de rechten en, in voorkomend geval, van             Lo de boeten geen gekende woonplaats in België of in het buitenland               pa heeft, wordt het bericht aan de procureur des Konings te Brussel               es verzonden.

###### Art. 36

(gewijzigd bij art. 96 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).   (m Tekst van toepassing vanaf 07.02.2022 (art. -))                                ap

Artikel 35, eerste lid, vindt geen toepassing op de voor notaris               L’a opgemaakte testamenten en andere akten als bedoeld in artikel 32,              ac
1°, tweede lid, b), wanneer de betrokkenen het bedrag van de rechten           lo en eventueel van de boeten uiterlijk daags vóór het verstrijken van de         pl voor de registratie gestelde termijn in handen der notarissen niet             l’e hebben geconsigneerd.                                                          am

###### Art. 37

(gewijzigd bij art. 97 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).   (m Tekst van toepassing vanaf 07.02.2022 (art. -))                                ap

Wanneer de rechten betreffende testamenten en andere in artikel 32,            Lo
1°, tweede lid, b), bedoelde akten niet in handen der notarissen               à werden geconsigneerd, zijn ze ondeelbaar door de erfgenamen,                   no legatarissen of begiftigden zomede door de testamentuitvoerders                do verschuldigd.

###### Art. 38

(opgeheven bij art. 140 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst    (ab van toepassing vanaf 01.01.1990 (art. 244))                                    ap

(…)                                                                            (…

#### Afdeling IV - Plaats der registratie

###### Art. 39

(1° en 4°, vervangen bij art. 98 van de wet van 21.01.2022 (B.S., 28.01.2022   (1 - ed. 1). Tekst van toepassing vanaf 07.02.2022 (art. -))                      éd

De akten en verklaringen worden geregistreerd:                                 Le

1° de akten van notarissen en gerechtsdeurwaarders, op het kantoor             1° bevoegd voor hun standplaats;                                                  co

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde            To onroerende goed wordt evenwel geregistreerd een akte die                       pr cumulatief:

a) onder de toepassing valt van het koninklijk besluit van 14 maart            a) 2014 houdende regeling van de aanbieding van akten van bepaalde                du

instrumenterende ambtenaren tot de registratieformaliteit en tot de       fo hypothecaire openbaarmaking;                                              ce

b) onroerende goederen betreft die alle gelegen zijn buiten het           b) ambtsgebied van het kantoor bevoegd voor de standplaats;                  bu

c) gelijktijdig ter overschrijving wordt aangeboden.                      c)

Het tweede lid is niet van toepassing op een akte die enkel de van        L’a niet-vatbaarheid voor beslag vaststelt van de woning van een              l’in zelfstandige bedoeld in de wet van 25 april 2007 houdende diverse         du bepalingen (IV);

1°bis (…)                                                                 1°

2° De arresten en vonnissen der hoven en rechtbanken, ten kantore         2° in welks gebied de zetel van het hof of de rechtbank gelegen is;          re

3° De akten die overeenkomstig artikel 26 zonder voorafgaande             3° registratie worden aangehecht of neergelegd, ten kantore waar de          l'a akte van de notaris of de gerechtsdeurwaarder moet worden                 do geregistreerd;

4° De akten van bestuursoverheden en ambtenaren van de Staat,             4° gefedereerde entiteiten, provincies, gemeenten en openbare                en instellingen, op het kantoor bevoegd voor hun zetel of standplaats;       ét ré

Op het kantoor bevoegd voor de ligging van het eerste erin vermelde       To onroerende goed wordt evenwel geregistreerd een akte die                  pr cumulatief:

a) onder de toepassing valt van het koninklijk besluit van 14 maart       a) 2014 houdende regeling van de aanbieding van akten van bepaalde           du instrumenterende ambtenaren tot de registratieformaliteit en tot de       fo hypothecaire openbaarmaking;                                              ce

b) onroerende goederen betreft die alle gelegen zijn buiten het           b) ambtsgebied van het kantoor bevoegd voor de zetel of de                   bu standplaats;

c) gelijktijdig ter overschrijving wordt aangeboden;                      c)

5° De onderhandse of buitenslands verleden akten en de                    5° verklaringen betreffende in België gelegen onroerende goederen en         dé welke in artikel 19, 2° en 3° en in artikel 31, 1° en 3°, zijn bedoeld,   vis ten kantore in welks gebied de goederen gelegen zijn. Zijn die            le goederen gelegen in het gebied van verscheidene kantoren, dan             re mogen de akten en verklaringen onverschillig in een van deze              en kantoren worden geregistreerd;

6° De verklaringen van vervulling van een in artikel 31, 2°, voorziene           6° schorsende voorwaarde, ten kantore waar de akte werd                             à geregistreerd welke van de overeenkomst laat blijken, of, bij gebreke            co aan geregistreerde akte, ten kantore in het 5° hiervoren aangeduid;              av

7° De andere akten dan voornoemde, onverschillig in alle kantoren.               7° in

###### Art. 40

(opgeheven bij art. 27 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).     (ab Tekst van toepassing vanaf 08.01.2018 (art. -))                                  ap

(…)                                                                              (…

#### Afdeling V - Sancties

###### Art. 41

(gewijzigd bij art. 4 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van    (m toepassing vanaf 01.01.2015 (art. 8))                                            àp

Verbeuren ondeelbaar een geldboete gelijk aan het bedrag der                     En rechten, zonder dat ze lager dan 25 EUR mag zijn:                                sa

1° de personen die binnen de voorgeschreven termijnen, de akten of               1° verklaringen niet hebben doen registreren welke zij gehouden zijn aan            les de formaliteit te onderwerpen of de in artikel 169ter, tweede lid,               fo bedoelde betaling niet hebben gedaan;                                            ali

2° De in artikel 37 aangewezen personen die, binnen den hun daartoe              2 gestelden termijn, de bij artikel 36 voorziene consignatie niet hebben           dé gedaan.                                                                          l’a

3° De in artikel 35, derde en vierde lid aangewezen personen die de              3° betaling bedoeld in het vijfde lid van genoemde artikel niet hebben              n’ gedaan binnen de voorgeschreven termijn.                                         du

###### Art. 41bis

(gewijzigd bij art. 54 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (m toepassing vanaf 16.05.2016 (art. -))                                            ap

De personen die de rechten, verschuldigd op de akten die van de                        Le formaliteit der registratie zijn vrijgesteld niet betaald hebben op de                 pr voorgeschreven wijze en binnen de voorgeschreven termijn, die geen                     l’e afschrift van deze akten neergelegd hebben of die zich niet gehouden                   qu hebben aan de door de Koning bepaalde aanvullende regels in                            le uitvoering van artikel 8bis, verbeuren ondeelbaar een boete van 25                     am EUR tot 250 EUR per overtreding.

Het bedrag van de boete wordt, binnen deze grenzen, vastgesteld                        Le door de bevoegde adviseur-generaal van de Algemene Administratie                       gé van de Patrimoniumdocumentatie.                                                        pa

De in het eerste lid bedoelde personen verbeuren ondeelbaar een                        Le boete gelijk aan de ontdoken rechten voor elke akte waarop zij ten                     am onrechte de vrijstelling van de formaliteit bedoeld in artikel 8bis,                   àt toegepast hebben.

###### Art. 42

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Voor elke overtreding van artikel 26 verbeurt de notaris of de                         Il e gerechtsdeurwaarder een boete van 25 EUR.                                              ju

###### Art. 43

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

De griffiers die binnen de voorgeschreven termijn de arresten en                       En vonnissen niet hebben doen registreren welke zij gehouden zijn aan                     n’ de formaliteit te onderwerpen, verbeuren voor elke overtreding een                     qu boete van 25 EUR.

###### Art. 44

tot 50 W.Reg. federaal

Het registratierecht op de inbreng door een natuurlijke persoon van                    Le een woning in een buitenlandse vennootschap (art. 44 tot 50 W.Reg.)                    pe is een federale belasting (art. 3, eerste lid, 6°, wet 16.01.1989

betreffende de financiering van de gemeenschappen en de                              es gewesten).                                                                           au

### HOOFDSTUK IV - Vaststelling van de rechten

#### Afdeling I - Overdrachten onder bezwarende titel van onroerende goederen

§ 1. Algemene bepalingen

###### Art. 44

(gewijzigd bij art. 40 van de wet van 30.03.1994 (BS., 31.03.1994 - ed. 2).          (m Tekst van toepassing vanaf 10.04.1994 (art. - ))                                     ap

Het recht wordt gesteld op 12,50 t.h. voor de verkopingen, ruilingen                 Le en alle overeenkomsten onder bezwarende titel, waarbij eigendom of                   co vruchtgebruik van onroerende goederen wordt overgedragen.                            bi

Eerste lid, streepje 1,2 en 4: gewestelijke bepalingen (art. 3, eerste lid, 6° van   Al de wet van 16.01.1989 betreffende de financiering van de gemeenschappen              sp en de gewesten)                                                                      Ré

###### Art. 45

(aangevuld bij art. 41 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).         (co Tekst van toepassing vanaf 10.04.1994 (art. -))                                      ap

Het recht wordt vereffend:                                                           Le

- ten aanzien van verkopingen, op het bedrag van bedongen prijs en                   -e lasten;                                                                              st

- ten aanzien van de ruilingen, op de overeengekomen waarde van de                   -e in een der prestatiën begrepen goederen, met inachtneming van die                    bi welke aanleiding tot het hoogste recht zou geven zoo beide waren                     do toegestaan tegen een naar die waarde vastgestelde geldprijs;                         m

- ten aanzien van inbrengen van onroerende goederen in                               -e vennootschappen, andere dan inbrengen als vermeld in artikel 115bis,                 qu op de waarde van de als vergoeding van de inbreng toegekende                         at su

maatschappelijke rechten verhoogd met de lasten die door de vennootschap gedragen worden;

- ten aanzien van de overige overdragende overeenkomsten, op de                 - overeengekomen waarde van de ten laste van de verkrijger van het                co onroerend goed bedongen tegenprestatie.                                         de

###### Art. 46

Evenwel mag de belastbare grondslag in geen geval lager zijn dan de             To verkoopwaarde van de overgedragen onroerende goederen.                          la

###### Art. 47

(gewijzigd bij art. 3 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (m toepassing vanaf 17.01.1959 (art. -))                                           àp

Wanneer de overeenkomst op het vruchtgebruik van een onroerend                  Lo goed slaat, wordt de in artikel 46 bedoelde verkoopwaarde                       vé vertegenwoordigd door de som verkregen door vermenigvuldiging                   m van de jaarlijkse opbrengst of, bij ontstentenis daarvan, van de                lo huurwaarde van het goed, met het getal dat in de onderstaande tabel             l’â is opgegeven en afhankelijk is van de leeftijd, welke degene op wiens           es hoofd het vruchtgebruik is gevestigd, op de dag van de akte heeft:

Getal        Leeftijd
18            20 jaar of minder
17           meer dan 20 jaar en niet meer dan 30 jaar;
16           meer dan 30 jaar en niet meer dan 40 jaar;
14           meer dan 40 jaar en niet meer dan 50 jaar;
13           meer dan 50 jaar en niet meer dan 55 jaar;
11           meer dan 55 jaar en niet meer dan 60 jaar;
9,5          meer dan 60 jaar en niet meer dan 65 jaar;
8            meer dan 65 jaar en niet meer dan 70 jaar;
6            meer dan 70 jaar en niet meer dan 75 jaar;
4            meer dan 75 jaar en niet meer dan 80 jaar;
2            meer dan 80 jaar;

Is het vruchtgebruik voor een beperkte tijd gevestigd, zo is de                 Si verkoopwaarde vertegenwoordigd door de som verkregen door het                   re kapitaliseren ad 4 pct. van de jaarlijkse opbrengst, rekening gehouden          re met de bij de overeenkomst gestelde duur van het vruchtgebruik,                 co maar zonder te mogen overschrijden hetzij de naar voorgaande alinea             l’a bepaalde waarde, zo het gaat om een ten bate van een natuurlijke                pe persoon gevestigd vruchtgebruik, hetzij het bedrag van twintigmaal              es

de opbrengst, zo het vruchtgebruik ten bate van een rechtspersoon is gevestigd.

In geen geval mag aan het vruchtgebruik een hogere waarde dan de              En vier vijfden van de verkoopwaarde van de volle eigendom worden                su toegewezen.                                                                   pr

###### Art. 48

Gaat de overeenkomst over de blote eigendom van een onroerend                 Lo goed waarvan het vruchtgebruik door de vervreemder is                         do voorbehouden, zo mag de belastbare grondslag niet lager zijn dan de           êt verkoopwaarde van de volle eigendom.

###### Art. 49

Gaat de overeenkomst over de blote eigendom van een onroerend                 Lo goed, zonder dat het vruchtgebruik door de vervreemder is                     sa voorbehouden, zoo mag de belastbare grondslag niet lager zijn dan de          pe verkoopwaarde van de volle eigendom, na aftrekking van de                     fa overeenkomstig artikel 47 berekende waarde van het vruchtgebruik.

###### Art. 50

Wordt of werd het vruchtgebruik op het hoofd van twee of meer                 Si personen gevestigd, met recht van aanwas of van terugvalling, zo is           pe de voor de toepassing van artikelen 47 en 49 in aanmerking te nemen           en leeftijd die van de jongste persoon.                                          pe

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)             re

§ 2. Verkopingen aan bouwmaatschappijen tot nut van het algemeen

###### Art. 51

(aangevuld bij art. 145 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (co van toepassing vanaf 01.01.1990 (art. 244))                                   ap

Het bij artikel 44 vastgelegd recht wordt tot 6 t.h. verlaagd voor de         Le verkopingen gedaan met het oog op de verwezenlijking van haar                 vu maatschappelijk doel:

aan maatschappijen erkend hetzij door de Nationale Maatschappij               1 voor de Huisvesting, hetzij door de Nationale Landmaatschappij,               pa hetzij door de Gewestelijke Maatschappijen opgericht in uitvoering            cr van de wet van 28 december 1984 tot afschaffing of herstructurering           su van sommige instellingen van openbaar nut.                                    pu

aan de samenwerkende maatschappij «Woningsfonds van de Bond                   2° der Kroostrijke Gezinnen in België», aan de coöperatieve                      fa vennootschappen Vlaams Woningfonds van de Grote Gezinnen,                     fla Woningfonds van de Kroostrijke Gezinnen van Wallonië en                       de Woningfonds van de gezinnen van het Brusselse Gewest.                         fa

Wat betreft de onder 1° hierboven bedoelde maatschappijen, wordt              En de verlaging slechts toegestaan mits het bewijs geleverd wordt van            ré de erkenning der verkrijgende maatschappij.                                   so

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)             re

§ 3. Verkopingen aan de met regeringspremie begunstigde kopers               §

###### Art. 52

(gewijzigd bij art. 146 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (m van toepassing vanaf 01.01.1990 (art. 244))                                   ap

Het recht wordt tot 1,50 t.h. verlaagd voor de verkopingen van                Le woningen toegestaan door de Nationale Maatschappij voor de                    pa Huisvesting, de Nationale Landmaatschappij, de door hen of door de            so Gewestelijke Maatschappijen opgericht in uitvoering van de wet van            ex 28 december 1984 tot afschaffing of herstructurering van sommige              re instellingen van openbaar nut erkende maatschappijen, de openbare             ad besturen of de openbare instellingen, aan personen wie de door de             bé Staat verleende aankooppremie ten goede komt.

Het gebeurlijk intrekken van die premie brengt voor de verkrijger der         Le verplichting mede het verschuldigde recht tot het bij artikel 44              l'a vastgesteld percentage aan te zuiveren.                                       fix

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)             re

§ 4. Verkopingen van kleine landeigendommen en bescheiden woningen

###### Art. 53

(gewijzigd bij art. 35 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst van   (m toepassing vanaf 01.01.1980 (art. 45))                                           ap

Het bij artikel 44 vastgesteld recht wordt tot 6 t.h. verlaagd voor de           Le verkopingen van de eigendom:                                                     pr

1° Van onroerende landgoederen waarvan het kadastraal inkomen                    1 een bij koninklijk besluit vast te stellen maximum niet te boven gaat.           m

Wordt als landgoed aangezien, het onroerend goed dat hetzij uit voor             Es landbouwbedrijf aangewende of bestemde gebouwen en gronden,                      bâ hetzij uit dergelijke gronden alleen bestaat;                                    ag

2° Van woningen waarvan het gebouwd of ongebouwd kadastraal                      2 inkomen een bij koninklijk besluit vast te stellen maximum niet                  pa overschrijdt.

Als woning wordt aangemerkt het huis of het geheel of het gedeelte               Es van een verdieping van een gebouw, dat dient of zal dienen tot                   d’ huisvesting van een gezin of één persoon, met in voorkomend geval                fa de aanhorigheden die tegelijk met het huis, het geheel of het gedeelte           dé van een verdieping worden verkregen. De Koning stelt regels vast                 pa voor het bepalen van de aanhorigheden waarop deze bepalingen van                 dé toepassing is.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 54

(gewijzigd bij art. 36 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst van   (m toepassing vanaf 01.01.1980 (art. 45))                                           ap

De in voorgaand artikel voorziene verlaging is niet toepasselijk op de           La verkoop van een onverdeeld deel, tenzij dit deel verbonden is aan een            d' verdieping of aan een gedeelte van verdieping van een gebouw.                    ou

Zij is evenmin van toepassing, zo de verkrijger of zijn echtgenoot de          El algeheelheid of een onverdeeld deel, in volle of blote eigendom, bezit         po van één of meer onroerende goederen, waarvan het kadastraal                    in inkomen voor de geheelheid of voor het onverdeeld deel, met dit van            la het verkregen onroerend goed, meer bedraagt dan het krachtens het              ac vorig artikel vast te stellen maximum. In afwijking van deze bepaling          pr wordt evenwel geen rekening gehouden met hetgeen door de                       te verkrijger of door zijn echtgenoot werd verkregen uit de nalatenschap          da van hun bloedverwanten in de opgaande lijn, mits het desbetreffende            ca kadastraal inkomen 25 % van evenbedoeld maximum niet overschrijdt.

De onder 2° van het voorgaande artikel bepaalde vermindering is                La eveneens niet toepasselijk indien de verkrijger of zijn echtgenoot             ap reeds, voor het geheel in volle of in blote eigendom, een onroerend            to goed bezitten dat geheel of gedeeltelijk tot bewoning is bestemd en            en dat door hen of door een van hen anders dan uit de nalatenschap van            au hun bloedverwanten in de opgaande lijn is verkregen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989      Di betreffende de financiering van de gemeenschappen en de gewesten)              re

###### Art. 55

(gewijzigd bij art. 79 van de wet van 22.12.2009 (B.S., 31.12.2009 - ed. 2).   (m Tekst van toepassing vanaf 10.01.2010 (art. -))                                ap

De in artikel 53 voorziene verlaging is bovendien aan volgende                 La voorwaarden verbonden:                                                         co

1° (…)                                                                         1

2° De akte, of een door de verkrijger gewaarmerkte en ondertekende             2 verklaring onderaan op de akte, moet uitdrukkelijk vermelden:                  l’a

a) dat de verkrijger en zijn echtgenoot geen andere onroerende                 a) goederen bezitten of dat zij, voor het geheel of in onverdeeldheid niet        im één of meer onroerende goederen bezitten waarvan het kadastraal                ou inkomen, voor het geheel of voor het onverdeelde deel, samen met               po dat van het verkregen onroerend goed, meer dan het krachtens artikel           su 53 vastgestelde maximum bedraagt, afgezien van hetgeen zij uit de              de nalatenschap van hun bloedverwanten in de opgaande lijn hebben                 lo verkregen wanneer het desbetreffende kadastraal inkomen 25 pct.                m van evenbedoeld maximum niet overschrijdt.

b) in geval van toepassing van artikel 53, 1°, dat de landeigendom          b) uitgebaat zal worden door de verkrijger, zijn echtgenoot of zijn            ex afstammelingen;

c) in geval van toepassing van artikel 53, 2°, dat de verkrijger of zijn    c) echtgenoot, voor het geheel in volle of in blote eigendom geen              co onroerend goed bezitten dat geheel of gedeeltelijk tot bewoning is          nu bestemd en door hen of door één van hen anders dan uit de                   ac nalatenschap van hun bloedverwanten in de opgaande lijn werd                le verkregen.

d) in geval van toepassing van artikel 53, 2°, dat de verkrijger of zijn    d) echtgenoot zijn inschrijving in het bevolkingsregister of in het            co vreemdelingenregister op het adres van het verkregen onroerend              da goed zal bekomen.

In geval van niet-nakoming van een van bovenstaande voorwaarden             A uiterlijk wanneer de akte ter formaliteit wordt aangeboden, wordt           lo deze akte tegen het gewoon recht geregistreerd; hetgeen boven het           au verlaagd recht geheven werd is vatbaat voor teruggaaf, tot beloop           re van de acht tienden, mits overlegging van een uittreksel uit de             de kadastrale legger en een verklaring ondertekend door de verkrijger,         l’a waarin de door voorgaand 2° beoogde vermeldingen voorkomen.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 56

Wanneer het kadastraal inkomen van het verkregen onroerend goed             Lo nog niet is vastgesteld, wordt het sub 1° van vorenstaand artikel           fix bedoeld uittreksel uit den kadastrale legger vervangen door een             es attest van de controleur van het kadaster houdende dat het                  qu kadastraal inkomen van bewust onroerend goed nog moet vastgesteld worden.

In dit geval, wordt de akte, behoudens de in artikel 58 voorziene           En teruggaaf, tegen het gewoon recht geregistreerd.                            pr

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 57

(gewijzigd bij art. 2 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van    (m toepassing vanaf 31.07.1960 (art. -))                                            àp

Onder voorbehoud der door artikel 54 voorziene beperkingen, wordt                So het bij artikel 44 vastgesteld recht verlaagd tot 6 pct. voor de                 es verkopingen van de eigendom van een grond welke tot bouwplaats                   se van een woning moet dienen, op voorwaarde:

1° Dat het verkregen goed en het gebouwd onroerend goed aan de                   1 bij artikel 53, 2°, gestelde voorwaarden beantwoorden;                           co

2° Dat de akte van verkrijging de bij artikel 55, 2°, geëiste                    2 vermeldingen vervat.                                                             l’a

In dit geval, wordt de akte tegen het gewoon recht geregistreerd,                En behoudens de bij artikel 58 voorziene teruggaaf, na voltooiing van het           pr gebouw.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 58

(aangevuld bij art. 26 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (co toepassing vanaf 17.01.1959 (art. -))                                            ap

In de bij artikelen 56 en 57 voorziene gevallen, wordt hetgeen boven             Da het verlaagd recht werd geheven, teruggegeven op overlegging van                 dr een na de vaststelling van het kadastraal inkomen afgeleverd                     ca uittreksel uit den kadastrale legger.

Het ter uitvoering van artikel 53, 2°, toepasselijk maximum is datgene           Le dat van kracht was op de datum van de akte van verkrijging.                      qu

Zo, tussen de datum van de akte en de 2de januari die volgt op het               Si betrekken der gebouwde woning, nieuwe kadastrale inkomens,                       gé vastgesteld     ingevolge     een       algemene    perekwatie      of   een     la buitengewone herziening, voor de heffing der grondbelasting in                   jan toepassing worden gebracht, dan moet het voor de gebouwde                        ca woning in acht te nemen kadastraal inkomen bepaald worden                        dé volgens de regeling die op de datum van de akte van toepassing was.              Le Het aldus bepaalde kadastraal inkomen wordt de verkrijger ter kennis             ré gebracht; deze kan bezwaar indienen volgens de procedure                         re betreffende de vaststelling van de nieuwe kadastrale inkomens.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 59

(gewijzigd bij art. 148 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (m van toepassing vanaf 01.01.1990 (art. 244))                                     ap

In geval van onjuistheid in de vermeldingen waarvan sprake in artikel           En 55, eerste lid, 2°, a en c, verbeurt de verkrijger een aan het ontdoken         ali recht gelijke geldboete.                                                        él

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 60

(gewijzigd bij art. 3 van de wet van 19.05.1998 (B.S., 14.07.1998). Tekst van   (m toepassing vanaf 24.07.1998 (art. -))                                           àp

Het voordeel van de in artikel 53, 1°, bedoelde vermindering blijft             Le alleen dan behouden zo de verkrijger, zijn echtgenoot of zijn                   si afstammelingen zelf de landeigendom uitbaten. Die uitbating dient               m aangevangen binnen een termijn van vijf jaar ingaande op de datum               da van de akte van verkrijging en tenminste drie jaar zonder                       et onderbreking voortgezet.                                                        au

Het voordeel van de in artikel 53, 2° bedoelde vermindering blijft              Le alleen dan behouden zo de verkrijger of zijn echtgenoot ingeschreven            si is in het bevolkingsregister of in het vreemdelingenregister op het             ac adres van het verkregen onroerend goed. Deze inschrijving moet                  ét geschieden binnen een termijn van drie jaar te rekenen van de datum             pr van de authentieke akte van verkrijging en ten minste drie jaar zonder          m onderbreking behouden blijven.

Evenwel blijft de verlaging verkregen zo niet-nakoming van die                  To voorwaarden het gevolg is van overmacht.                                        co

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 611

(vervangen bij art. 4 van de wet van 19.05.1998 (B.S., 14.07.1998). Tekst van   (re toepassing vanaf 24.07.1998 (art. -))                                           ap

Indien de vermindering vervalt bij gebreke van exploitatie binnen de            En termijn en gedurende de tijd bepaald in artikel 60, eerste lid, is de           et verkrijger, naast het aan vullend recht, een daaraan gelijke                    l’a vermeerdering verschuldigd.                                                     m

Indien de vermindering vervalt bij gebreke van inschrijving binnen de           En termijn en gedurende de tijd bepaald in artikel 60, tweede lid, is de           et verkrijger, naast het aanvullend recht, een daaraan gelijke                     l’a vermeerdering verschuldigd.                                                     m

De Minister van Financiën kan evenwel van die vermeerdering geheel              Le of gedeeltelijk afzien.                                                         pa

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 612

(gewijzigd bij art. 5 van de wet van 19.05.1998 (B.S., 14.07.1998). Tekst van   (m toepassing vanaf 24.07.1998 (art. -))                                           àp

Wanneer een ongebouwd landeigendom, verkregen met de in deze                    Lo paragraaf bedoelde verlaging, naderhand in een ruiling betrokken                ré wordt volgens artikel 72, treedt het in ruil verkregen goed, voor de            d’ toepassing van de artikelen 60, eerste lid en 61 , eerste lid, in de ac plaats van het oorspronkelijk verkregen goed.                                   61

Hetzelfde     heeft       plaats    ingeval      van   ruilverkaveling   van    La landeigendommen in der minne of uit kracht van de wet. In geval van             ou gebruiksruil bij toepassing van titel I van de wet houdende bijzondere          ap maatregelen inzake ruilverkaveling van landeigendommen uit kracht               m van de wet bij de uitvoering van grote infrastructuurwerken, treedt,            gr voor de toepassing van de artikelen 60, eerste lid en 61 , eerste lid, l’a het bij de akte van ruiling voor gebruik toebedeeld goed in de plaats           61 van het verkregen goed.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

§ 5. Verkopingen aan personen die hun beroep maken van den                 § aankoop van onroerende goederen met het oog op wederverkoop

###### Art. 62

(vervangen bij art. 1 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van   (re toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978 (B.S. 30.11.1978)))          ap

Het in artikel 44 bepaalde recht wordt tot 5 pct. verminderd voor de            Le verkopingen die uit de hand en bij authentieke akte gedaan worden               gr aan personen die hun beroep maken van het kopen en verkopen van                 pr onroerende goederen.

Deze vermindering is echter niet van toepassing op de verkopen van              Ce landeigendommen waarvan de verkoopswaarde het bedrag niet te                    ru boven gaat dat verkregen wordt bij vermenigvuldiging van het                    m kadastraal inkomen met een door de Koning vastgestelde coëfficiënt.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 631

(lid 1, 1°, vervangen bij art. 62 van de wet van 12.05.2024 (B.S., 30.05.2024   (al – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders    éd van een ondernemingsnummer, evenals voor natuurlijke personen, op een           nu datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028   da (art. 222))

Om de in vorenstaand artikel voorziene vermindering te genieten,                Po moet de beroepspersoon:                                                         pr

1° in de vorm en aan het bij koninklijk besluit te bepalen kantoor, een         1° beroepsverklaring ondertekenen en verzenden;                                    fo

2° op eigen kosten, zekerheid stellen voor de invordering van de                2 sommen welke bij toepassing van artikel 64 en volgende artikelen van            so deze paragraaf vorderbaar kunnen worden;                                        de

3° de erkenning verkregen hebben van een in België gevestigd                    3 vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem                as instaat voor de nakoming van zijn fiscale verplichtingen indien hij:            s’i

a) een natuurlijke persoon is en zijn wettelijke verblijfplaats buitend de       a) Europese Economische Ruimte heeft;                                               éc

b) een rechtspersoon is zonder vestiging in België en wiens                      b) maatschappelijke zetel gevestigd is buiten de Europese Economische               siè Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte             L’a van verkrijging, hetzij in een onderaan de akte gestelde verklaring of           d’ in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie,           un door de verkrijger of, in zijn naam, door de werkende notaris                    pa ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet               Lo een uittreksel uit de kadastrale legger betreffende de verkregen                 la goederen aan de akte gehecht zijn wanneer zij ter registratie wordt              lo aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en,          L’a in voorkomend geval, het uittreksel uit de kadastrale legger, zoals              dé bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het             au gewoon recht geregistreerd en geen vordering tot teruggaaf is                    de ontvankelijk.

Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan            Le de    erkenning     verkrijgen     van      een   in   België    gevestigde      re vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem                 so instaat voor de nakoming van zijn fiscale verplichtingen.                        fis

###### Art. 631

(gewijzigd bij art. 62 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst van   (m toepassing vanaf 16.05.2011 (art. -))                                            ap

Om de in vorenstaand artikel voorziene vermindering te genieten,                 Po moet de beroepspersoon:                                                          pr

1° in de vorm en op het bij koninklijk besluit te bepalen kantoor, een           1 beroepsverklaring ondertekenen en indienen;                                      et

2° op eigen kosten, zekerheid stellen voor de invordering van de                 2 sommen welke bij toepassing van artikel 64 en volgende artikelen van             so deze paragraaf vorderbaar kunnen worden;                                         de

3° de erkenning verkregen hebben van een in België gevestigd                     3 vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem                 as instaat voor de nakoming van zijn fiscale verplichtingen indien hij:             s’i

a) een natuurlijke persoon is en zijn wettelijke verblijfplaats buitend de      a) Europese Economische Ruimte heeft;                                              éc

b) een rechtspersoon is zonder vestiging in België en wiens                     b) maatschappelijke zetel gevestigd is buiten de Europese Economische              siè Ruimte.

De vervulling van deze voorwaarden dient bevestigd hetzij in de akte            L’a van verkrijging, hetzij in een onderaan de akte gestelde verklaring of          d’ in een bijgevoegd schrijven. De verklaring wordt, vóór de registratie,          un door de verkrijger of, in zijn naam, door de werkende notaris                   pa ondertekend;

Zo de verkrijging onroerende landgoederen tot voorwerp heeft, moet              Lo een uittreksel uit de kadastrale legger betreffende de verkregen                la goederen aan de akte gehecht zijn wanneer zij ter registratie wordt             lo aangeboden.

De akte welke die bevestiging niet inhoudt of waarbij de verklaring en,         L’a in voorkomend geval, het uittreksel uit de kadastrale legger, zoals             dé bedoeld in vorenstaande alinea's, niet gehecht zijn, wordt tegen het            au gewoon recht geregistreerd en geen vordering tot teruggaaf is                   de ontvankelijk.

Een beroepspersoon, andere dan die bedoeld in het eerste lid, 3°, kan           Le de    erkenning     verkrijgen     van   een     in   België    gevestigde      re vertegenwoordiger die medeaansprakelijk is en hoofdelijk met hem                so instaat voor de nakoming van zijn fiscale verplichtingen.                       fis

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 632

(ingevoegd bij art. 3 van de wet van 03.02.1959 (B.S., 14.02.1959). Tekst van   (in toepassing vanaf 24.02.1959 (art. -))                                           àp

Wanneer door een schatting volgens artikelen 190 en 199 bevonden                Lo wordt dat de verkoopwaarde van landgoederen, welke met                          19 toepassing van het bij artikel 62 voorzien verminderd recht verkregen           ap werden, op de datum van de verkrijging de door laatstbedoeld artikel            de vastgestelde grens niet overtrof, is de verkrijger gehouden tot het             du betalen van het bijkomend recht berekend op de grondslag die voor               pe de heffing van het verminderd recht gediend heeft, van een zelfde               fra som als boete en van de kosten der procedure.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 64

Het bij artikel 44 bepaald recht wordt vorderbaar ten laste van de          Le verkrijger van het onroerend goed die het voordeel van artikel 62           de heeft genoten, bijaldien bedoelde verkrijger of zijn rechthebbenden dit     ay onroerend goed niet hebben vervreemd door wederverkoop of alle              tra andere overdracht onder bezwarende titel, andere dan den inbreng in         pa vennootschap, vastgesteld bij authentieke akte uiterlijk verleden op        an 31 december van het tiende jaar na de datum van de koopakte.

De wederverkoop aan een beroepspersoon met toepassing van                   Ne artikel 62 staat deze vorderbaarheid niet in de weg.                        pr

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 65

De verkrijger mag de betaling aanbieden van het gewoon recht vóór           L’a het verstrijken van de in eerste alinea van vorig artikel voorziene         dé termijn.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 66

Het recht dat voor de verkrijging van het goed betaald werd, mag niet       Le op de krachtens artikelen 64 en 65 verschuldigde rechten worden             su aangerekend.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989   Di betreffende de financiering van de gemeenschappen en de gewesten)           re

###### Art. 67

De overeenkomstig artikelen 64 en 65 vorderbare rechten worden                    Le berekend op de waarde die tot grondslag heeft gediend aan het voor                su de verkrijging betaald recht en naar het op de datum dezer verkrijging            le van kracht zijnde tarief.

Bijaldien slechts een deel van tegen een enige prijs aangekochte                  Si onroerende goederen wordt vervreemd, wordt de belastbare waarde                   ali van het niet vervreemde gedeelte bepaald naar verhouding van de                   dé grootte.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989         Di betreffende de financiering van de gemeenschappen en de gewesten)                 re

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 68

(lid 3, vervangen bij art. 63 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed.   (al 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van        Te een ondernemingsnummer, evenals voor natuurlijke personen, op een datum           d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art.     fix 222))

In het geval van artikel 64 worden de gewone rechten vereffend op                 Da een verklaring die, binnen de eerste vier maanden na het verstrijken              dé van het tiende jaar en op straf van boete gelijk aan de rechten, tot              pr registratie dient aangeboden ten kantore in welks gebied de goederen              d’ gelegen zijn.                                                                     bi

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter            Da registratie een verklaring aanbieden waarin samenstelling en waarde               l’e zijn bepaald van de goederen waarvoor hij de rechten wenst te                     co betalen.                                                                          dr

De bij dit artikel voorgeschreven verklaringen worden door de                     Le belanghebbende         of    zijn      aangenomen       vertegenwoordiger         l'in ondertekend en vermelden de akte of de akten van verkrijging, het                 ac nieuwe feit waaruit de verschuldigdheid van het recht volgt en al de              et tot de vereffening van de belasting nodige gegevens. Een kopie wordt              co bewaard door de bevoegde dienst van de Algemene administratie van                 do de patrimoniumdocumentatie.

###### Art. 68

(gewijzigd bij art. 152 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (m van toepassing vanaf 01.01.1990 (art. 244))                                     ap

In het geval van artikel 64 worden de gewone rechten vereffend op               Da een verklaring die, binnen de eerste vier maanden na het verstrijken            dé van het tiende jaar en op straf van boete gelijk aan de rechten, tot            pr registratie dient aangeboden ten kantore in welks gebied de goederen            d’ gelegen zijn.                                                                   bi

In het geval van artikel 65, moet de verkrijger op bedoeld kantoor ter          Da registratie een verklaring aanbieden waarin samenstelling en waarde             l’e zijn bepaald van de goederen waarvoor hij de rechten wenst te                   co betalen.                                                                        dr

De bij dit artikel voorgeschreven verklaringen, welke door                      Le belanghebbende of zijn aangenomen vertegenwoordiger worden                      l’in ondertekend, worden in dubbel gesteld, en een exemplaar blijft op het           ex kantoor der registratie. Deze verklaringen houden vermelding van de             El akte of de akten van verkrijging, van het nieuwe feit waaruit de                dé verschuldigdheid van het recht volgt en al de tot de vereffening van            liq de belasting nodige gegevens.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 69

(gewijzigd bij artikel 63 van de wet van 14.04.2011 (B.S., 06.05.2011). Tekst   (m van toepassing vanaf 16.05.2011 (art. -))                                       ap

Bij overlijden van den vertegenwoordiger van een beroepspersoon                 En bedoeld in artikel 631, eerste lid, 3°, bij de intrekking van zijn erkenning    ali of in geval hij onbekwaam wordt verklaard om als vertegenwoordiger              so op te treden, dient binnen zes maand in zijn vervanging voorzien.               re

Wanneer de door den verkrijger gestelde zekerheid ontoereikend                  Lo wordt, dient hij, binnen de door het bestuur vastgestelde termijn, een          do aanvullende zekerheid te verstrekken.                                           l’a

Wordt aan vorenstaande voorschriften niet voldaan, zo wordt het                 S’ volgens artikelen 66 en 67 berekend gewoon recht op de niet                     or wederverkochte goederen vorderbaar.                                             no

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 70

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

De Minister van Financiën of zijn afgevaardigde bepaalt aard en                        Le bedrag der ter voldoening van artikelen 63 , 2°, en 69 te stellen de zekerheid of aanvullende zekerheid. Deze zekerheid dient gesteld                       de onder de door de Minister of zijn afgevaardigde bepaalde                               co voorwaarden en mag niet minder dan 5.000 EUR bedragen.                                 in

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

###### Art. 71

Indien hij die een beroepsverklaring heeft ondertekend bij het                         Si verstrijken van een termijn van vijf jaar na die verklaring, niet bij                  àl machte is om door een reeks wederverkoper te laten blijken dat hij                     pa het aangegeven beroep werkelijk uitoefent, wordt hij schuldenaar van                   pr de gewone rechten op zijn aankopen, onder aftrek van de reeds                          ac geheven rechten, en daarenboven van een som gelijk aan de                              so aanvullende rechten als boete.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

§ 6. Ruiling van ongebouwde landgoederen

###### Art. 72

(gewijzigd en aangevuld bij art. 2 van de wet van 27.04.1978 (B.S.,                    (m 30.11.1978). Tekst van toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978              Te (B.S., 30.11.1978)))                                                                   30

Zijn vrijgesteld van het evenredig recht en onderworpen aan het                        So algemeen        vast     recht,      de     ruilingen       van    ongebouwde          les landeigendommen waarvan de verkoopwaarde voor elk der kavels

het bedrag niet te boven gaat dat verkregen wordt bij                           ch vermenigvuldiging van het kadastraal inkomen met een door de                    re Koning vastgestelde coëfficiënt.

Evenwel wordt bij ongelijkheid van de kavels het bij artikel 44                 To bepaalde recht geheven op het waardeverschil of de opleg, indien                lo deze groter is dan dat verschil. Dit recht wordt verlaagd tot 6 t.h.            à indien het waardeverschil of de opleg een vierde van de                         ou verkoopwaarde van de minste kavel niet te boven gaat.

De toepassing van dit artikel is ondergeschikt aan een drievoudige              L’a voorwaarde:

1° dat de verkoopwaarde van elke kavel door partijen wordt                      1° aangegeven, hetzij in de akte, hetzij onderaan de akte, vóór de                 so registratie;

2° dat een uittreksel uit de kadastrale legger aan de akte wordt                2° gehecht bij de registratie;                                                     m

3° dat de partijen vóór de registratie, in een verklaring gedaan in de          3° akte of onderaan op de akte, aanduiden of de geruilde onroerende                av goederen door henzelf of door derden worden geëxploiteerd en dat,               éc in deze laatste onderstelling, de akte of een daaraan vóór de                   ce registratie gehecht schrijven de instemming inhoudt van alle                    l’e exploitanten van de in de ruiling begrepen goederen.                            co

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 731

(vervangen bij art. 3 van de wet van 26.07.1952 (B.S., 30.08.1952). Tekst van   (re toepassing vanaf 09.09.1952 (art. -))                                           ap

Voor elke te laag bevonden opleg of waardeverschil is, behalve het              To ontdoken recht, een geldboete van hetzelfde bedrag als dit recht                so vorderbaar.

Hetzelfde geldt voor elke overschatting van de kavels die een                   Il e vermindering van het recht tot gevolg heeft.                                    de

De geldboete is evenwel niet verschuldigd, indien het verschil tussen           To de verkoopwaarde van de kavels en de aangegeven schatting minder                lo dan een achtste hiervan bedraagt.                                               ce

Het bepaalde in de artikelen 189 tot 201 geldt mede voor de controle           Le op de in dit artikel omschreven schattingen.                                   de

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989      Di betreffende de financiering van de gemeenschappen en de gewesten)              re

###### Art. 732

(hersteld bij art. 3 van de wet van 27.04.1978 (B.S., 30.11.1978). Tekst van   (ré toepassing vanaf 30.11.1978 (art. 2, KB 13.11.1978 (B.S., 30.11.1978)))        àp

In geval van onjuistheid van de verklaring betreffende de uitbating van        En de geruilde onroerende goederen, zijn de partijen ondeelbaar                   im gehouden tot de betaling van het verschil tussen het gewoon recht en           pa het geheven recht, alsook van een boete gelijk aan dat verschil.               qu

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989      Di betreffende de financiering van de gemeenschappen en de gewesten)              re

§ 7. Afzonderlijke verkrijgingen van de grond en van de opstal of van de tot de dienst van het onroerend goed aangewende voorwerpen

###### Art. 74

(gewijzigd bij art. 42 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).   (m Tekst van toepassing vanaf 10.04.1994 (art. -))                                ap

Wie bij een overdragende overeenkomst onder bezwarende titel,                  Ce andere dan een inbreng in vennootschap vermeld in artikel 115bis, de           au eigendom heeft verkregen, hetzij van hout op stam onder beding van             de het te vellen, hetzij van gebouwen onder beding van ze te slopen, en           av nadien onder de levenden de eigendom verkrijgt van de grond                    pr vooraleer het hout gans geveld is of de gebouwen volomen gesloopt              qu zijn, moet uit hoofde van de eerste verkrijging en op de grondslag             en aangewezen in artikel 45 en volgende, het voor de verkoop van                  45 onroerende goederen vastgesteld recht kwijten met aftrek van het               fa evenredig registratierecht eventueel op deze verkrijging werd                  ac geheven.

Deze bepaling is evenwel niet van toepassing, zo er bewezen wordt              Ce dat de belasting over de toegevoegde waarde werd gekweten voor de              ta levering van het hout op stam of van de te slopen gebouwen.                    pi

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

###### Art. 75

(gewijzigd bij art. 43 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).    (m Tekst van toepassing vanaf 10.04.1994 (art. -))                                 ap

Wordt als overdracht van een onroerend goed aangezien, die welke                Es voortvloeit uit een overeenkomst onder de levenden te bezwarende                ré titel, andere dan een inbreng in vennootschap vermeld in artikel                ap 115bis, en welke over de eigendom gaat hetzij van hout op stam,                 bo hetzij van gebouwen, zo bewuste overdracht ten bate van de eigenaar             co van de grond wordt toegestaan.

Deze bepaling is niet van toepassing zo de belasting over de                    Ce toegevoegde waarde verschuldigd is voor de levering van de                      es goederen die in de overeenkomst begrepen zijn. De heffing van het               pe vast recht is echter ondergeschikt aan de vermelding, in de akte of in          l’a een erbij gevoegd geschrift, vóór de registratie, van het kantoor, waar         au de verkoper periodiek de aangiften indient die voor de heffing van de           po belasting over de toegevoegde waarde zijn vereist.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989       Di betreffende de financiering van de gemeenschappen en de gewesten)               re

§ 8. (…)

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van   (ab toepassing vanaf 31.07.1960 (art. -))                                           àp

###### Art. 76

(opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst van   (ab toepassing vanaf 31.07.1960 (art. -))                                           àp

(…)                                                                             (…

###### Art. 77

tot 82 W.Reg. federaal

Het registratierecht op de openbare verkopingen van lichamelijke                      Le roerende goederen is een federale belasting (art. 3, a contrario, wet                 co 16 januari 1989 betreffende de financiering van de gemeenschappen                     19 en de gewesten).

#### Afdeling II - Openbare verkopingen van lichamelijke

roerende goederen

(opschrift vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959).         (in Tekst van toepassing vanaf 17.01.1959 (art. -))                                       ap

###### Art. 77

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van         (re toepassing vanaf 17.01.1959 (art. -))                                                 ap

Het recht wordt vastgesteld op 5 t.h. voor de openbare verkopingen                    Le van lichamelijke roerende goederen.                                                   co

###### Art. 78

(opgeheven bij art. 5 van de wet van 10.07.1969 (B.S., 25.07.1969). Tekst van         (ab toepassing vanaf 01.01.1971 (art. 10, gewijzigd bij art. 3 van de wet van             à 19.12.1969 (B.S., 20.12.1969)))                                                       (M

(…)                                                                                   (…

###### Art. 79

(vervangen bij art. 4 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van         (re toepassing vanaf 17.01.1959 (art. -))                                                 ap

De heffingsgrondslag wordt bepaald zoals gezegd in de artikelen 45                    La en 231.                                                                               et

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 80

(lid 2, gewijzigd bij art. 64 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Vrijgesteld van het recht van 5 pct. en onderworpen aan het algemeen              So vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als                  1° belastingplichtige in de zin van de wetgeving op de belasting over de             qu toegevoegde waarde;                                                               va

2° de openbare verkopingen van goederen bedoeld in de artikelen 2                 2 en 3 van titel I van het Wetboek der met het zegel gelijkgestelde                 Co taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.                   3°

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven                Da mits in het proces-verbaal of in een geschrift dat bij het proces-                su verbaal vóór de registratie is gevoegd, vermeld wordt naar welk                   an kantoor de verkoper de periodieke aangiften voor de belasting over de             de toegevoegde waarde moet verzenden.                                                ajo

###### Art. 80

(vervangen bij art. 42 van de wet van 27.12.1977 (B.S., 30.12.1977) err. (B.S.,   (re 10.05.1978). Tekst van toepassing vanaf 01.01.1978 (art. 43))                     10

Vrijgesteld van het recht van 5 pct. en onderworpen aan het algemeen              So vast recht zijn:

1° de openbare verkopingen op verzoek van iemand die handelt als                  1° belastingplichtige in de zin van de wetgeving op de belasting over de             qu toegevoegde waarde;                                                               va

2° de openbare verkopingen van goederen bedoeld in de artikelen 2                 2 en 3 van titel I van het Wetboek der met het zegel gelijkgestelde                 Co taksen;

3° de openbare verkopingen van inlands hout, op stam of gekapt.                   3°

Voor de onder 1° bedoelde verkopingen wordt het vast recht geheven                Da mits in het proces-verbaal of in een geschrift dat bij het proces-                su verbaal vóór de registratie is gevoegd, vermeld wordt bij welk kantoor            an de verkoper de periodieke aangiften voor de belasting over de                     de toegevoegde waarde moet indienen.                                                 ajo

#### Afdeling III - (…)

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

###### Art. 81

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

(…)                                                                              (…

###### Art. 82

(opgeheven bij art. 5 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

(…)                                                                              (…

###### Art. 83

tot 86 W.Reg. federaal

Het registratierecht op de huurcontracten is een federale belasting              Le (art. 3, a contrario, wet 16.01.1989 betreffende de financiering van de          co gemeenschappen en de gewesten).                                                  co

#### Afdeling IV - Huurcontracten

###### Art. 83

(lid 1, 3°, gewijzigd bij art. 5 van de wet van 22.12.2023 (B.S., 29.12.2023 –   (al ed. 1). Tekst van toepassing vanaf 01.01.2024 (art. 6))                          1)

Het recht wordt vastgesteld op:                                                  Le

1° 0,20 pct. voor contracten van verhuring, onderverhuring en                    1° overdracht van huur van onroerende goederen;                                     im

2° 1,50 pct. voor jacht- en vispacht;                                            2°

3° 5 pct. voor contracten tot vestiging van een erfpacht- of                     3° opstalrecht en tot overdracht daarvan, behalve wanneer daardoor                  su een vereniging zonder winstoogmerk, een internationale vereniging                du zonder winstoogmerk of een gelijkaardige rechtspersoon die                       as

opgericht is volgens en onderworpen is aan de wetgeving van een              an lidstaat van de Europese Economische Ruimte en die bovendien zijn            Ét statutaire zetel, zijn hoofdbestuur of zijn hoofdvestiging binnen de         siè Europese Economische Ruimte heeft, titularis van het erfpacht- of            ét opstalrecht wordt, in welk geval het recht wordt vastgesteld op 0,50         au pct.

Een rechtspersoon is gelijkaardig aan een VZW wanneer de volgende            Pa voorwaarden cumulatief zijn vervuld:                                         pe

1° het doel van de rechtspersoon is belangeloos, zonder                      1° winstoogmerk;

2° de activiteit van de rechtspersoon mag niet leiden tot de materiële       2° verrijking van:

a) de stichters, de leden of de bestuurders ervan;                           a)

b) de echtgenoot, de wettelijk samenwonende, een bloedverwant in             b) de rechte lijn, een bloedverwant in de zijlijn die tot een stichter in een   pa erfgerechtigde graad staat, of een andere rechtsopvolger van een             lég stichter ervan;                                                              fo

c) de echtgenoot of een wettelijk samenwonende van een persoon               c) bedoeld in a) en b);                                                         et

3° in geval van ontbinding of vereffening van de rechtspersoon               3° mogen de goederen ervan niet toekomen aan personen vermeld                   ca onder 2°, maar moeten ze worden overgedragen aan:                            êt

a) hetzij een gelijkaardige rechtspersoon die zelf is opgericht volgens      a) en onderworpen aan de wetgeving van een lidstaat van de Europese             co Economische Ruimte en bovendien zijn statutaire zetel, zijn                  de hoofdbestuur      of   zijn   hoofdvestiging   binnen     de   Europese      st Economische Ruimte heeft;                                                    su

b) hetzij een lidstaat is van de Europese Economische Ruimte of een          b) territoriaal gedecentraliseerde overheid van een EER-lidstaat is of          su nog, een dienstgewijze gedecentraliseerde overheid is van een                ét dergelijke publiekrechtelijke rechtspersoon.                                 pu

Contracten tot vestiging van erfpacht- of opstalrecht en overdrachten        Le daarvan worden, voor het overige, met huurcontracten en -                    le overdrachten gelijkgesteld, voor de toepassing van dit wetboek,              ce behalve voor de toepassing van de artikelen 2quater en 161, 12°.             l’a

Dit recht is evenwel niet verschuldigd in geval van toepassing van           Ce artikel 140bis.

###### Art. 84

(gewijzigd bij art. 22 van de wet van 13.08.1947 (B.S., 17.09.1947). Tekst van   (se toepassing vanaf 27.09.1947 (art. -))                                            (M

De belastbare grondslag wordt als volgt vastgelegd:                              La

Voor huur van bepaalde duur, geldt als grondslag van het voor de duur            Si van het contract of, ter zake overdracht, voor het nog te lopen tijdperk         ch samengevoegd bedrag van huursommen en aan huurder opgelegde                      d’ lasten;

Is zij levenslang of van onbepaalde duur, zo geldt als grondslag het             S’ tienvoudig bedrag van de jaarlijkse huurprijs en lasten, zonder dat de           lo belastbare som minder moge zijn dan het samengevoegd bedrag van                  in huurprijzen en aan huurder opgelegde lasten voor de bij de huurakte              pr voorziene minimumduur.

Bij overdracht van huur, wordt het bedrag of de waarde van de                    En gebeurlijk ten bate van de overdrager bedongen prestatiën gevoegd                év bij de heffingsgrondslag zoals hij hiervoor is bepaald.                          pe

#### Afdeling V - (…)

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

###### Art. 85

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

(…)                                                                              (…

###### Art. 86

(opgeheven bij art. 7 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                            àp

(…)                                                                              (…

###### Art. 87

tot 102 W.Reg. federaal

Het registratierecht op:                                                         Le - de vestiging van een hypotheek op een schip dat niet naar zijn aard            la voor zeevervoer bestemd is;                                                      pa - de inpandgeving van een handelszaak;                                           la - de vestiging van een landbouwvoorrecht;                                        la - de overdracht van een hypotheek op een onroerend goed;                         la zijn federale belastingen (art. 3, eerste lid, 7° a) a contrario wet             so 16.01.1989 betreffende de financiering van de gemeenschappen en                  16 de gewesten).                                                                    ré

Alleen het registratierecht op de vestiging van een hypotheek op een in          Se België gelegen onroerend goed is een gewestelijke belasting (art. 3,             su eerste lid, 7°, a) wet 16.01.1989 betreffende de financiering van de             al. gemeenschappen en de gewesten). Zie ook ontwerp van bijzondere                   co wet tot herfinanciering van de gemeenschappen en uitbreiding van de              po fiscale bevoegdheden van de gewesten, Parl.St. Kamer 2000-01, nr.                co 50 1183/001, 74.                                                                 n°

Gewestelijke bepalingen (art. 3, eerste lid, 7°, a) van de wet van 16.01.1989    Di betreffende de financiering van de gemeenschappen en de gewesten)                re

#### Afdeling VI - Hypotheekvestigingen

(gewijzigd bij art. 55 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (m toepassing vanaf 01.01.2018 (art. 70))                                           ap

###### Art. 87

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (re toepassing vanaf 17.01.1959 (art. -))                                            ap

Worden aan een recht van 1 t.h. onderworpen, de vestigingen van een              So hypotheek op een in België gelegen onroerend goed.                               un

###### Art. 88

(vervangen bij art. 56 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (re toepassing vanaf 01.01.2018 (art. 70))   (1) ap

De vestigingen van een hypotheek op een schip dat niet naar zijn aard            Le voor het zeevervoer bestemd is, worden aan een recht van 0,50 pct.               na onderworpen.

----------                                                                       -- Nota (1) – Overgangsbepaling:                                                    No Het recht van 0,50 pct., geheven overeenkomstig art. 88 W.Reg. vóór de           Le inwerkingtreding van deze wet, wordt in mindering gebracht op het krachtens      vig art. 87 W.Reg. verschuldigde recht, wanneer later een hypotheek wordt            lor gevestigd tot zekerheid van dezelfde schuld (art. 69).                           de

###### Art. 89

(gewijzigd bij art. 57 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (m toepassing vanaf 01.01.2018 (art. 70))                                           ap

De bij artikelen 87 en 88 bepaalde rechten zijn van toepassing zelfs             Le wanneer de hypotheek gevestigd is tot zekerheid van een                          lo toekomstige schuld, van een voorwaardelijke of eventuele schuld of               d’ van een verbintenis om iets te doen.

###### Art. 90

(vervangen bij art. 8 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van    (re toepassing vanaf 17.01.1959 (art. -))                                            ap

De bij artikelen 87 en 88 bepaalde rechten zijn niet verschuldigd zo de          Le gewaarborgde verbintenis voortkomt uit een contract waarop een                   l’o evenredig recht van minstens 1 pct. werd geheven.                                dr

Gewestelijke bepalingen (art. 3, eerste lid, 7°, a) van de wet van 16.01.1989    Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 91

(vervangen bij art. 58 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (m toepassing vanaf 01.01.2018 (art. 70))                                           ap

De vestiging van een hypotheek op een in België gelegen onroerend                La goed tot zekerheid van een schuld die gewaarborgd is door een                    po hypotheek op een schip dat niet naar zijn aard voor het zeevervoer               n’ bestemd is, (…) wordt aan het recht van 1 pct. onderworpen onder                 dr aftrek, in voorkomend geval, van het krachtens artikel 88 geheven                pe recht van 0,50 pct.

###### Art. 921

(vervangen bij art. 82 van de wet van 11.02.2019 (B.S., 22.03.2019). Tekst van   (re toepassing vanaf 01.01.2019 (art. 83))                                           ap

Het in artikel 88 en het in artikel 3, eerste lid, 7°, a), van de bijzondere     Le wet van 16 januari 1989 betreffende de financiering van de                       sp Gemeenschappen en de Gewesten bedoeld recht dekt elke latere                     Co vestiging van hypotheek op een schip tot zekerheid van dezelfde                  d‘ schuldvordering en van hetzelfde gewaarborgd bedrag.                             m

###### Art. 922

(gewijzigd bij art. 60 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (m toepassing vanaf 01.01.2018 (art. 70))                                           ap

De overdracht van een hypotheek op een in België gelegen onroerend               La goed met inbegrip van de voorrechten bedoeld bij artikel 27 van de               Be wet van 16 december 1851 of van een hypotheek op een schip dat                   dé niet naar zijn aard voor het zeevervoer bestemd is, ingevolge de                 de overdracht onder bezwarende titel van de schuldvordering, de                     tit contractuele indeplaatsstelling of elke andere verrichting onder                 to bezwarende titel, wordt onderworpen aan een recht van 1 pct. of van              p.
0,50 pct., al naar gelang de overdracht al dan niet een hypotheek op             hy een onroerend goed betreft.

###### Art. 93

(gewijzigd bij art. 61 van de wet van 25.12.2016 (B.S., 30.12.2016). Tekst van   (m toepassing vanaf 01.01.2018 (art. 70))                                           ap

Het recht van 1 pct. of van 0,50 pct. wordt vereffend op het bedrag              Le van de sommen die door de hypotheek gewaarborgd zijn, met                        ga uitsluiting van de interesten of rentetermijnen van drie jaren, die              tro gewaarborgd zijn door artikel 87 van de wet van 16 december 1851.

###### Art. 94

(gewijzigd bij art. 12 van de wet van 03.07.2018 (B.S., 19.07.2018). Tekst van   (m toepassing vanaf het aanslagjaar 2019 (art. 13))                                 ap

Schepen worden niet onderworpen aan het in artikel 88 bepaalde                   Le recht op voorwaarde dat:                                                         qu

1° een getuigschrift, afgeleverd door het Belgisch Scheepsregister,             1° ter bevestiging dat het schip is geregistreerd in het Belgisch register         at der zeeschepen of dat voor het schip een aangifte voor registratie in           na het Belgisch register der zeeschepen werd ingediend, aan de akte                de wordt gehecht;

2° de akte, of een door de hypotheeksteller gewaarmerkte en                     2° ondertekende verklaring onderaan op de akte, uitdrukkelijk vermeldt:            l’h

a) dat het schip naar zijn aard voor het zeevervoer bestemd is;                 a)

b) dat de hypotheeksteller de verbintenis aangaat om de                         b) voorwaarden inzake het behoud of de uitbreiding van de tonnage en               un inzake de bewijslevering van naleving van de tonnage-eis en van het             l’a voldoen van elk schip van de vloot aan de betreffende internationale            to en communautaire normen, zoals die voorwaarden nader zijn                       de omschreven in punt 3.1, leden 8 en 9 van de Mededeling C(2004) van              in de Europese Commissie, na te leven gedurende vijf jaar te rekenen               co van de datum van de registratie van de akte.                                    9

Als de in het eerste lid, 2°, a) bedoelde verklaring onjuist blijkt of als      Lo de in het eerste lid, 2°, b) bedoelde verbintenis niet wordt nageleefd,         in is de hypotheeksteller gehouden tot betaling van het evenredig recht,           re vermeerderd met de interesten.                                                  dr

De hypotheeksteller kan aanbieden het evenredig recht vermeerderd               Le met de interesten te betalen alvorens de in het eerste lid, 2°, b)              pr voorziene termijn is verstreken.                                                àl

#### Afdeling VII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

###### Art. 95

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 96

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959).Tekst van    (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 97

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 98

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

#### Afdeling VIII - (…)

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

###### Art. 99

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 100

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 101

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(...)                                                                           (…

###### Art. 102

(opgeheven bij art. 9 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (ab toepassing vanaf 17.01.1959 (art. -))                                           àp

(…)                                                                             (…

###### Art. 103

tot 108 W.Reg. federaal

Het specifiek vast recht op de handlichting van een hypothecaire                Le inschrijving is een federale belasting (art. 3, a contrario, wet                es 16.01.1989 betreffende de financiering van de gemeenschappen en                 au de gewesten).

#### Afdeling IX - Opheffingen

###### Art. 103

(gewijzigd bij art. 92 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).    (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                 ap

§ 1. Elke gehele of gedeeltelijke handlichting van een in België                § genomen hypothecaire inschrijving, gedaan bij een akte bedoeld in               hy artikel 19, 1°, is onderworpen aan een specifiek vast recht van 75              1° euro.

§ 2. In afwijking van paragraaf 1 geven slechts aanleiding tot éénmaal          § de heffing van het recht bedoeld in paragraaf 1, de handlichtingen              fo vastgesteld in één akte:                                                        co

1° van inschrijvingen genomen lastens éénzelfde schuldenaar-                    1° hypotheeksteller;

2° van inschrijvingen genomen lastens een schuldenaar-                          2° hypotheeksteller en een persoon-hypotheeksteller als waarborg voor              af de eerstgenoemde;

3° van inschrijvingen van wettelijke hypotheken lastens éénzelfde               3° schuldenaar;

4° van door een hypotheekbewaarder of de Algemene Administratie              4° van     de    Patrimoniumdocumentatie          ambtshalve      genomen       l’A inschrijvingen;

5° die geschieden in het kader van een openbare verkoping na beslag          5° of van een verkoop uit de hand bedoeld in artikel 1580bis van het            ve Gerechtelijk Wetboek.

###### Art. 104

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst   (ab van toepassing vanaf 17.01.1959 (art. -))                                    ap

(...)                                                                        (…

###### Art. 105

(opgeheven bij art. 153, 1° van de wet van 22.12.1989 (B.S., 29.12.1989).    (ab Tekst van toepassing vanaf 01.01.1990 (art. 244))                            ap

(...)                                                                        (…

###### Art. 106

(opgeheven bij art. 153, 2°, van de wet van 22.12.1989 (B.S., 29.12.1989).   (ab Tekst van toepassing vanaf 01.01.1990 (art. 244))                            ap

(…)                                                                          (…

###### Art. 107

(opgeheven bij art. 10 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst   (ab van toepassing vanaf 17.01.1959 (art. -))                                    ap

(...)                                                                        (…

###### Art. 108

(opgeheven bij art. 153, 3°, van de wet van 22.12.1989 (B.S., 29.12.1989).   (ab Tekst van toepassing vanaf 01.01.1990 (art. 244))                            ap

(...)                                                                            (…

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)                re

#### Afdeling X - Verdelingen

###### Art. 109

(aangevuld bij art. 33 van de wet van 14.05.1981 (B.S., 27.05.1981). Tekst van   (co toepassing vanaf 06.06.1981 (art. -))                                            ap

Het recht wordt op 1 t.h. vastgesteld voor:                                      Le

1° de gedeeltelijke of gehele verdelingen van onroerende goederen;               1

2°de afstanden onder bezwarende titel, onder medeëigenaars, van                  2 onverdeelde delen in onroerende goederen.                                        in

3° de omzetting bedoeld in de artikelen 745quater en 745quinquies                3° van het Burgerlijk Wetboek, zelfs indien er geen onverdeeldheid is.              Co

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 110

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (re toepassing vanaf 17.01.1959 (art. -))                                            ap

Voor de goederen waarvan de akte de onverdeeldheid doet ophouden                 En onder al de medeëigenaars, wordt het recht vereffend op de waarde                en van die goederen.                                                                bi

Voor de goederen waarvan de akte de onverdeeldheid niet doet                     En ophouden onder al de medeëigenaars, wordt het recht vereffend op                 l’in de waarde der afgestane delen.                                                   va

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 111

(vervangen bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (re toepassing vanaf 17.01.1959 (art. -))                                            ap

De heffingsgrondslag is bepaald door de overeengekomen waarde                    La der goederen, zoals ze blijkt uit de bepalingen van de akte, zonder dat          bi hij lager dan de verkoopwaarde mag zijn.                                         pu

Wanneer de bepalingen van de akte het niet mogelijk maken de                     Lo overeengekomen         waarde      vast     te   stellen,   wordt     daarin     va overeenkomstig artikel 168 voorzien.

In voorkomend geval wordt de verkoopwaarde van het vruchtgebruik                 Le of van de blote eigendom overeenkomstig artikelen 47 tot 50                      es vastgesteld.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 112

(opgeheven bij art. 16 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst       (ab van toepassing vanaf 17.01.1959 (art. -))                                        ap

(...)                                                                            (…

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 113

(vervangen bij art. 17 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (re toepassing vanaf 17.01.1959 (art. -))                                            ap

In geval van toebedeling bij verdeling of van afstand van onverdeelde            En delen aan een derde die bij overeenkomst een onverdeeld deel heeft               tie verkregen van goederen toebehorende aan één of meer personen,                    ap wordt het recht, met afwijking van artikel 109, geheven tegen het                dé voor de overdrachten onder bezwarende titel vastgesteld tarief, op de            on delen waarvan de derde ten gevolge van de overeenkomst eigenaar                  la wordt, en zulks volgens de in artikelen 45 tot 50 voorziene regels.

Deze bepaling is van toepassing wanneer de toebedeling van                           Ce goederen of de afstand van onverdeelde delen gedaan wordt aan de                     ou erfgenamen of legatarissen van de overleden derde verkrijger. Zij is                 lég niet van toepassing wanneer de derde, aan wie de toebedeling of de                   ca afstand gedaan wordt, met anderen het geheel van één of meer                         to goederen heeft verkregen.

Gewestelijke bepalingen (art. 3, eerste lid, 7° b) van de wet van 16.01.1989         Di betreffende de financiering van de gemeenschappen en de gewesten)                    re

###### Art. 114

De bepalingen van deze afdeling zijn niet van toepassing op de                       Le uitvoering van een beding van terugvalling of van aanwas.                            ré

###### Art. 115

tot 130 W.Reg. federaal

Het registratierecht op de inbreng in een vennootschap is een                        Le de financiering van de gemeenschappen en de gewesten).                               fin

#### Afdeling XI - Vennootschappen

###### Art. 115

(lid 1, gewijzigd en lid 3, opgeheven bij art. 22 van de wet van 30.10.2025 (B.S.,   (al 24.11.2025). Tekst van toepassing vanaf 25.11.2025 (art. 28))                        24

Aan een recht van 0 pct. wordt onderworpen de inbreng van roerende                   So goederen in vennootschappen waarvan hetzij de zetel der werkelijke                   so leiding in België, hetzij de statutaire zetel in België en de zetel der              le werkelijke leiding buiten het grondgebied van de lidstaten van de                    ho Europese Unie, is gevestigd, onverschillig of de inbreng bij de                      ap oprichting van de vennootschap of naderhand plaats heeft.                            ul

Het recht wordt vereffend op het totaal bedrag van de inbrengen.                     Le

###### Art. 115bis

(lid 1, gewijzigd bij art. 23 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst    (al van toepassing vanaf 25.11.2025 (art. 28))                                           ap

De inbrengen van onroerende goederen, andere dan die welke                       So gedeeltelijk of geheel tot bewoning aangewend worden of bestemd                  le zijn en door een natuurlijke persoon ingebracht worden, in                       en vennootschappen waarvan de zetel der werkelijke leiding in België                Et gevestigd is, of de statutaire zetel in België en de zetel van werkelijke        qu leiding buiten het grondgebied van de lidstaten van de Europese Unie             l’h gevestigd is, worden aan het recht van 0 pct. onderworpen.

In geval van onjuiste verklaring betreffende de aanwending of de                 En bestemming van het onroerend goed, zijn de aanvullende rechten                   de opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.             et

###### Art. 116

(gewijzigd bij art. 24 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van   (m toepassing vanaf 25.11.2025 (art. 28))                                           ap

Aan een recht van 0 pct. wordt onderworpen de vermeerdering van                  Es het kapitaal, zonder nieuwe inbreng, van een vennootschap waarvan                ap hetzij de zetel der werkelijke leiding in België, hetzij de statutaire zetel     ef in België en de zetel der werkelijke leiding buiten het grondgebied van          siè de lidstaten van de Europese Unie, is gevestigd.                                 l'U

Het recht wordt vereffend op het bedrag van de vermeerdering.                    Le

Het recht is niet verschuldigd in de mate waarin het kapitaal                    Le vermeerderd wordt door inlijving van reserves of provisies, die                  in gevestigd werden, bij gelegenheid van inbrengen gedaan in de                     d’ vennootschap, ter vertegenwoordiging van het geheel of een                       du gedeelte van het bedrag van die inbrengen dat onderworpen werd                   ar aan het bij de artikelen 115 en 115bis bedoeld recht.

###### Art. 117

(gewijzigd bij art. 25 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst van   (m toepassing vanaf 25.11.2025 (art. 28))                                           ap

§ 1. Het bij de artikelen 115 en 115bis bepaalde recht is niet                   § verschuldigd in geval van inbreng van de universaliteit der goederen             d’ van een vennootschap, bij wijze van fusie, splitsing of anderszins, in           fu een of meer nieuwe of bestaande vennootschappen.                                 ou

Deze bepaling is evenwel slechts toepasselijk op voorwaarde:                     Ce

1° dat de vennootschap die de inbreng doet de zetel van haar               1° werkelijke leiding of haar statutaire zetel heeft op het grondgebied       ef van een lidstaat van de Europese Unie;                                     l'U

2° a) dat de rechtshandeling door artikel 12:7 van het Wetboek van         2° vennootschappen en verenigingen wordt gelijkgesteld met fusie door         so overneming, of

b) dat, eventueel na aftrek van de op het tijdstip van de inbreng door     b) de inbrengende vennootschap verschuldigde sommen, de inbreng               de uitsluitend vergoed wordt hetzij door toekenning van aandelen, hetzij      ré door toekenning van aandelen samen met een storting in contanten           d'a die het tiende van de nominale waarde of, bij gebrek aan een nominale      le waarde, van de fractiewaarde van de toegekende aandelen niet               pa overschrijdt. Indien het Belgisch of buitenlands recht dat de              ré verkrijgende vennootschap beheerst niet in een begrip gelijkaardig         du aan dat van het kapitaal van een naamloze vennootschap voorziet,           va wordt met de fractiewaarde gelijkgesteld, de inbrengwaarde, zoals          ap die blijkt uit de jaarrekening, van alle door de aandeelhouders of         co vennoten toegezegde inbrengen in geld of in natura, met uitzondering       de van de inbrengen in nijverheid, in voorkomend geval verhoogd met de        êt reserves die op grond van een statutaire bepaling slechts aan de           m aandeelhouders of vennoten kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen.

§ 2. Het in de artikelen 115 en 115bis bedoelde recht is eveneens niet     §2 verschuldigd voor de inbrengen gedaan door een vennootschap                les waarvan de zetel der werkelijke leiding of de statutaire zetel             ef gevestigd is op het grondgebied van een lidstaat van de Europese           l'U Unie, van goederen die één of meer van haar bedrijfstakken uitmaken        br onder de volgende voorwaarden:

1° dat de inbreng het geheel omvat van de goederen die door de             1° inbrengende vennootschap worden aangewend tot één of meer                  pa afdelingen van haar onderneming welke, op technisch en                     en organisatorisch gebied, elk een autonome activiteit uitoefenen en op       l'o eigen kracht kunnen werken; en                                             su

2° dat, eventueel na aftrek van de bij de inbreng door de inbrengende      2° vennootschap verschuldigde sommen die betrekking hebben op de              l'a ingebrachte bedrijfstakken, de inbreng uitsluitend vergoed wordt           d'a hetzij door toekenning van aandelen, hetzij door toekenning van            l'a aandelen samen met een storting in contanten die het tiende van de         d' nominale waarde of, bij gebrek aan een nominale waarde, van de             no fractiewaarde van de toegekende aandelen niet overschrijdt. Indien         ac het Belgisch of buitenlands recht dat de verkrijgende vennootschap         bé beheerst niet in een begrip gelijkaardig aan dat van het kapitaal van      so een naamloze vennootschap voorziet, wordt met de fractiewaarde             te gelijkgesteld, de inbrengwaarde, zoals die blijkt uit de jaarrekening,     nu van alle door de aandeelhouders of vennoten toegezegde inbrengen           pa

in geld of in natura, met uitzondering van de inbrengen in nijverheid,    ré in voorkomend geval verhoogd met de reserves die op grond van een         di statutaire bepaling slechts aan de aandeelhouders of vennoten             m kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen.

De bepaling onder 2° is niet van toepassing op de door artikel 12:8,      Le
2°, van het Wetboek van vennootschappen en verenigingen met               sc splitsing gelijkgestelde rechtshandelingen.                               as

Wordt niet beschouwd als een afdeling van de onderneming het              N' beheer van de participaties en de waarden in portefeuille. De             de participaties en waarden in portefeuille worden slechts beschouwd         va als behorende tot een bedrijfstak wanneer zij normaal in de exploitatie   br van deze tak van de bedrijvigheid zijn geïntegreerd.                      l'e

Onverminderd het recht tot controle, moet de vervulling van de            So voorwaarden bevestigd worden, hetzij in de akte van inbreng, hetzij in    êt een onderaan deze akte gestelde verklaring, die vóór de registratie       pi door de partijen of, in hun naam, door de werkende notaris zal            le ondertekend worden. Bij gebrek aan deze bevestiging zal de akte           af geregistreerd worden mits betaling van het recht bepaald zonder           sa rekening te houden met de vrijstelling van het evenredig recht of de      l'e uitzondering, naar gelang van het geval, behoudens latere teruggave.

§ 3. Het in de artikelen 115 en 115bis bedoelde recht is eveneens niet    §3 verschuldigd    in   geval    van    inbreng    van    aandelen     of    les aandelencertificaten, die tot gevolg heeft dat de vennootschap bij wie    so de inbreng gebeurt, ten minste 75 pct. van het kapitaal of van het        ca eigen vermogen verwerft van de vennootschap waarvan de aandelen           so of aandelencertificaten zijn ingebracht.

Wanneer dat percentage ten gevolge van verscheidene inbrengen is          Lo bereikt, is deze paragraaf alleen toepasselijk op de inbrengen die het    d’ bereiken van het percentage mogelijk hebben gemaakt, alsmede op           ain de daaropvolgende inbrengen.                                              pr

Bovendien vindt deze paragraaf alleen toepassing wanneer voldaan          L’a is aan de volgende voorwaarden:                                           co

1° de vennootschap die verkrijgt en de vennootschap waarvan de            1° aandelen of deelbewijzen zijn ingebracht, moeten beide hun zetel der      ap werkelijke leiding of hun statutaire zetel hebben op het grondgebied      le van een lidstaat van de Europese Unie;                                    eu

2° de inbreng moet uitsluitend door uitgifte van aandelen van de          2° verkrijgende vennootschap vergoed worden, samen met een storting          de in contanten die het tiende van de nominale waarde of, bij gebrek aan     dé een nominale waarde, van de fractiewaarde van de toegekende               no aandelen niet overschrijdt. Indien het Belgisch of buitenlands recht      ou

dat de verkrijgende vennootschap beheerst niet in een begrip                    an gelijkaardig aan dat van het kapitaal van een naamloze vennootschap             pa voorziet,    wordt     met     de    fractiewaarde      gelijkgesteld,    de    to inbrengwaarde, zoals die blijkt uit de jaarrekening, van alle door de           in aandeelhouders of vennoten toegezegde inbrengen in geld of in                   au natura, met uitzondering van de inbrengen in nijverheid, in                     pe voorkomend geval verhoogd met de reserves die op grond van een                  un statutaire bepaling slechts aan de aandeelhouders of vennoten kunnen worden uitgekeerd mits een statutenwijziging, dit alles gedeeld door het aantal aandelen;

3° de akte van inbreng moet vermelden dat bij de inbreng ten minste             3° 75 pct. van het kapitaal of van het eigen vermogen van de                       ob vennootschap waarvan de aandelen zijn ingebracht, door de                       ca verwervende vennootschap wordt verkregen;

4° een attest van een bedrijfsrevisor dat het vermelde feit                     4° overeenkomstig het 3° van dit lid bevestigt, moet aan de akte worden            én aangehecht.                                                                     l’a

In geval van niet-nakoming van een van de toepassingsvoorwaarden                A van deze paragraaf uiterlijk wanneer de akte ter formaliteit wordt              pa aangeboden, wordt deze akte tegen het gewoon tarief geregistreerd.              ce

###### Art. 118

(vervangen bij art. 7 van de wet van 03.07.1972 (B.S., 01.08.1972). Tekst van   (re toepassing vanaf 01.01.1972 (art. 11))                                          ap

Voor de toepassing van dit Wetboek worden beschouwd als                         Po oprichtingen van nieuwe vennootschap:                                           co

1° de overbrenging naar België van de zetel der werkelijke leiding van          1° een vennootschap waarvan de statutaire zetel in het buitenland is;              so

2° de overbrenging naar België van de statutaire zetel van een                  2° vennootschap waarvan de zetel der werkelijke leiding in het                     siè buitenland is;

3° de overbrenging van het buitenland naar België, van de statutaire            3° zetel en van de zetel der werkelijke leiding van een vennootschap.              siè

In deze gevallen omvat de inbreng de goederen van elke aard die aan             Da de vennootschap toebehoren op het tijdstip van de overbrenging.                 ap

###### Art. 119

(gewijzigd bij art. 46 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).   (m Tekst van toepassing vanaf 10.04.1994 (art. -))                                ap

In de gevallen bedoeld in de artikelen 115, 115bis en 118 wordt de             Da belastbare grondslag vastgesteld met inachtneming van de waarde                es der als vergelding van de inbrengen toegekende maatschappelijke                at rechten, zonder dat hij nochtans minder mag bedragen dan de                    êt verkoopwaarde van de goederen onder aftrek van de lasten die de                ch vennootschap op zich neemt boven de toekenning van de                          so maatschappelijke rechten.

De inbrengen die bestaan uit andere zaken dan geldspecie of                    Le goederen in natura worden geraamd bij vergelijking met de inbrengen            qu van geldspecie of goederen in natura, gelet op de onderscheidene               ap aandelen van de inbrengers in de winst.                                        re

De verkoopwaarde van het vruchtgebruik of van de blote eigendom                La van in België gelegen onroerende goederen wordt bepaald                        sit overeenkomstig de artikelen 47 tot 50.                                         50

###### Art. 120

(gewijzigd bij art. 47 van de wet van 30.03.1994 (B.S., 31.03.1994 - ed. 2).   (m Tekst van toepassing vanaf 10.04.1994 (art. -))                                ap

Wanneer een inbreng in vennootschap gedeeltelijk vergolden wordt               Lo anders dan bij toekenning van maatschappelijke rechten, wordt de               pa overeenkomst, naarmate van deze vergelding onderworpen aan de                  de rechten zoals ze in dit hoofdstuk vastgesteld zijn voor de                     ch overeenkomsten onder bezwarende titel die goederen van dezelfde                bi aard tot voorwerp hebben.

Zo een inbreng meteen onroerende goederen vermeld in artikel                   Si 115bis en goederen van een andere aard begrijpt, worden,                       et niettegenstaande elke strijdig beding, de maatschappelijke rechten en          ch de andere lasten, die de vergeldingen van bedoelde inbreng uitmaken            no geacht evenredig verdeeld te zijn tussen de waarde die aan de                  en onroerende goederen is toegekend en die welke aan de andere                    bi goederen is toegekend bij overeenkomst. De te vervallen huurprijzen            so van de huurcontracten waarvan de rechten worden ingebracht,                    ce worden evenwel geacht enkel op laatstbedoelde rechten betrekking te hebben.

Deze bepalingen zijn evenwel niet toepasselijk bij inbreng van de              Ce universaliteit van de goederen of van een bedrijfstak overeenkomstig           d’ artikel 117.                                                                   l’a

###### Art. 121

(lid 1, 3°, gewijzigd bij art. 26 van de wet van 30.10.2025 (B.S., 24.11.2025).     (al Tekst van toepassing vanaf 25.11.2025 (art. 28))                                    Te

Met afwijking van de artikelen 115, 115bis, 118 en 120 worden van                   Pa het evenredig recht vrijgesteld:                                                    du

1° de omvorming van een vennootschap met rechtspersoonlijkheid                      1° in een vennootschap van een verschillende soort en de omzetting van                 ju een vereniging zonder winstoogmerk in een sociale onderneming.                      d’ Deze bepaling is toepasselijk zelfs wanneer de omvorming plaats                     di heeft bij wege van liquidatie gevolgd door de oprichting van een                    ré nieuwe vennootschap, voor zover deze wederoprichting in de akte                     no van in-liquidatie-stellen in het vooruitzicht wordt gesteld en binnen               de vijftien dagen na de akte plaats heeft;                                             ac

2° de wijziging van het voorwerp van een vennootschap;                              2°

3° de overbrenging van de zetel der werkelijke leiding of van de                    3° statutaire zetel van een vennootschap, wanneer deze overbrenging                    d’ geschiedt uit het grondgebied van een lidstaat van de Europese Unie                 Et of wanneer het een overbrenging naar België betreft van de zetel der                Be werkelijke leiding van een vennootschap waarvan de statutaire zetel                 st zich reeds op het grondgebied van de Europese Unie bevindt. Deze                    di bepaling is slechts toepasselijk in de mate waarin het vaststaat dat de             so vennootschap behoort tot de soort van die welke onderworpen zijn                    im aan een belasting op het bijeenbrengen van kapitaal in het land dat in              pr aanmerking komt voor het voordeel van de vrijstelling.

In alle gevallen wordt het recht geheven op de vermeerdering van het                Da kapitaal van de vennootschap, zonder nieuwe inbreng, of op de                       la inbrengen van nieuwe goederen, die gedaan worden ter gelegenheid                    ef van de omvorming, de wijziging van het voorwerp of de overbrenging                  du van de zetel.

###### Art. 122

(lid 1, 1° en 3°, vervangen, lid 1, 4° en lid 2, gewijzigd bij art. 28 van de wet   (al van 10.02.2026 (B.S., 27.02.2026). Tekst van toepassing vanaf 09.03.2026            10 (art. 33, lid 1))                                                                   33

Onder voorbehoud van de bepalingen van artikel 120, wordt van het                   So evenredig recht vrijgesteld de inbreng gedaan:                                      pr

1° aan de maatschappijen die erkend zijn door de Société wallonne                1° du logement, de Brusselse Gewestelijke Huisvestingsmaatschappij of               So Wonen in Vlaanderen;                                                             Vl

2° aan maatschappijen die uitsluitend ten doel hebben leningen te                2° doen met het oog op het bouwen, het aankopen of het inrichten van                la volkswoningen, kleine landeigendommen of daarmede gelijkgestelde                 so woningen, alsmede de uitrusting ervan met geschikt mobilair;                     ain

3° aan de besloten vennootschap Vlaams Woning-fonds, de                          3° coöperatieve vennootschap Fonds du logement des familles                         so nombreuses de Wallonie en de coöperatieve vennootschap                           W Woningfonds van het Brussels Hoofdstedelijk Gewest;                              Br

4° aan de beleggingsvennootschappen bedoeld in artikel 6 van de                  4° wet van 3 augustus 2012 betreffende de instellingen voor collectieve             20 belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG                au en de instellingen voor belegging in schuldvorderingen.                          pl

Het evenredig recht, zonder aftrek van het reeds geïnde algemeen                 To vast recht, wordt echter opeisbaar wanneer de in het eerste lid, 4°,             dé bedoelde beleggingsvennootschap de erkenning overeenkomstig de                   à wet van 3 augustus 2012 betreffende de instellingen voor collectieve             co belegging die voldoen aan de voorwaarden van Richtlijn 2009/65/EG                pl en de instellingen voor belegging in schuldvorderingen niet verkrijgt            20 of verliest, al naar het geval, zulks vanaf de datum van de beslissing           co tot weigering of tot intrekking van de erkenning.

###### Art. 1222

(opgeheven bij art. 14, 1°, van de wet van 14.04.1965 (B.S., 24.04.1965).        (ab Tekst van toepassing vanaf 04.05.1965 (art. -))                                  ap

(…)                                                                              (…

###### Art. 123

(gewijzigd bij art. 93 van de wet van 17.03.2019 (B.S., 10.05.2019). Tekst van   (m toepassing vanaf 01.05.2019 (art. 119, § 1))   (1) ap

Onder voorbehoud van de bepalingen van de artikelen 44 en 120                    So wordt van het evenredig recht vrijgesteld, de vermeerdering van het              dr kapitaal of het eigen vermogen, met nieuwe inbreng, door een                     av vennootschap bedoeld in artikel 201, eerste lid, 1°, van het Wetboek             du van de inkomstenbelastingen 1992, mits aandelen of andere met                    de

aandelen gelijk te stellen waardepapieren van die vennootschap ter               ac notering op een Belgische effectenbeurs zijn toegelaten.                         m

Deze vrijstelling is alleen toepasselijk indien in de akte of in een vóór        Ce de registratie bij de akte te voegen geschrift wordt bevestigd dat de            da toepassingsvoorwaarden ervan zijn vervuld.                                       les

In geval van onjuistheid van die vermelding verbeurt de vennootschap             En een boete gelijk aan het ontdoken recht.                                         ég
----------                                                                       -- Nota (1) – Overgangsbepalingen:                                                  No Zolang het Wetboek van vennootschappen en verenigingen, overeenkomstig           Au hoofdstuk IV, afdeling II, van de wet van 23 maart 2019, niet van toepassing     23 is op een vennootschap, vereniging of stichting, moet elke verwijzing naar een   so bepaling van het Wetboek van vennootschappen en verenigingen die                 de voorkomt in een bepaling van het Wetboek van de inkomstenbelastingen             un 1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het            d'e Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het       du Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering           la ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze        ex belastingen, worden gelezen, voor wat deze vennootschap, vereniging of           fo stichting betreft, als een verwijzing naar de bepaling van het Wetboek van       ar vennootschappen of andere bijzondere wetgeving die in zulke fiscale              dis wetgeving voorkwam voor de inwerkingtreding van deze wet (art. 119, § 2);
Zolang, overeenkomstig hoofdstuk IV, afdeling II van de wet van 23 maart         Au 2019, een vennootschap, vereniging of stichting, die door het Belgisch recht     23 wordt beheerst, een rechtsvorm heeft die het Wetboek van vennootschappen         co en verenigingen niet erkent, worden de bepalingen van het Wetboek van de         re inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en           Co Griffierechten, het Wetboek van Successierechten, het Wetboek diverse            de rechten en taksen en het Wetboek van de Belasting over de Toegevoegde            va Waarde, de ter uitvoering ervan genomen besluiten en de bijzondere               pr wetgeving van toepassing op deze belastingen, die voor de inwerkingtreding       vig van deze wet deze rechtsvorm vermeldden, geacht deze rechtsvorm te blijven       av vermelden voor wat deze vennootschap, vereniging of stichting betreft, zoals     as voor de inwerkingtreding van deze wet. (art. 119, § 3).

###### Art. 124

(hersteld bij art. 31 van de wet van 22.05.2001 (B.S., 09.06.2001). Tekst van    (ré toepassing vanaf 01.01.2002 (art. 4, KB 19.12.2001 (B.S., 29.12.2001- ed. 2)))   àp

Onder voorbehoud van de voorschriften van de artikelen 44 en 120,                So worden van het evenredig recht vrijgesteld:                                      du

1° de statutaire kapitaalsverhoging, uitgevoerd bij toepassing van               1° een participatieplan bedoeld in artikel 2, 7°, van de wet van 22 mei             pl 2001 betreffende de werknemersparticipatie in het kapitaal en in de              re

winst van de vennootschappen, en ten belope van de                               bé kapitaalsparticipaties bedoeld in artikel 2, 17°, van dezelfde wet;              vis

2° de inbreng in een coöperatieve participatievennootschap                       2° uitgevoerd volgens artikel 12, § 2, van dezelfde wet.                            co

Deze vrijstelling is slechts toepasbaar voor zover er vermeld is in de           Ce akte of in een vóór de registratie bij de akte gevoegd geschrift dat de          da toepassingsvoorwaarden zijn vervuld.                                             les

Ingeval deze vermelding ontbreekt of onjuist is, loopt de                        En vennootschap een boete op gelijk aan het ontdoken recht.                         en

###### Art. 125

(opgeheven bij art. 14, 3°, van de wet van 14.04.1965 (B.S.,24.04.1965).         (ab Tekst van toepassing vanaf 04.05.1965 (art. -))                                  ap

(…)                                                                              (…

###### Art. 126

(opgeheven bij art. 14, 4°, van de wet van 14.04.1965 (B.S.,24.04.1965).         (ab Tekst van toepassing vanaf 04.05.1965 (art. -))                                  ap

( …)                                                                             (…

###### Art. 127

(opgeheven bij art. 14, 5°, van de wet van 14.04.1965 (B.S., 24.04.1965).        (ab Tekst van toepassing vanaf 04.05.1965 (art. -))                                  ap

( ...)                                                                           (…

###### Art. 128

(gewijzigd bij art. 15 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van   (m toepassing vanaf 04.05.1965 (art. -))                                            ap

Met afwijking van artikel 2, mogen de onderhandse akten welke de in              Pa artikelen 115 tot 122 bedoelde overeenkomsten tot voorwerp                       les hebben, op de originelen of op afschriften of uittreksels worden                 en

geregistreerd. Wanneer de afschriften of uittreksels ter registratie             pr worden aangeboden, moeten ze vergezeld zijn van de oorspronkelijke               ac akte.

###### Art. 211

wordt toepasselijk gemaakt op de onderhandse of                      L’a buitenslands verleden akten die de zelfde overeenkomsten tot                     en voorwerp hebben, al hadden deze geen betrekking op in België                     qu gelegen onroerende goederen.                                                     Be

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 129

(gewijzigd bij art. 31 van de wet van 23.03.2019 (B.S., 04.04.2019). Tekst van   (m toepassing vanaf 01.05.2019 (art. 38))                                           ap

Het verkrijgen, anderszins dan bij inbreng in vennootschap, door één             L’a of meer vennoten, van in België gelegen onroerende goederen,                     d’ voortkomende van een vennootschap onder gemeenschappelijke                       so naam of bij wijze van eenvoudige geldschieting, van een besloten                 re vennootschap of van een landbouwvennootschap, geeft, welke ook                   m de wijze zij waarop het geschiedt, aanleiding tot het heffen van het voor verkopingen gesteld recht.

In geval van afgifte van de maatschappelijke goederen door de                    En vereffenaar van de in vereffening gestelde vennootschap aan al de                liq vennoten, is voorgaand lid van toepassing op de latere toebedeling               l’a van de goederen aan één of meer vennoten.

Lid l is niet toepasselijk zo het gaat om:                                       L’a

1° onroerende goederen welke in de vennootschappen werden                        1° ingebracht, wanneer ze verkregen worden door de persoon, die de                  pe inbreng gedaan heeft;

2° onroerende goederen welke door de vennootschap met betaling                   2° van het voor de verkopingen bepaald registratierecht verkregen                   d’ werden, wanneer het vaststaat dat de vennoot die eigenaar van die                qu onroerende goederen wordt deel uitmaakte van de vennootschap                     au toen laatstgenoemde de goederen verkreeg.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 130

(gewijzigd bij art. 2, 4°, van de wet van 14.03.1962 (B.S., 17.03.1962). Tekst        (m van toepassing vanaf 17.03.1962 (art. 3))                                             ap

Het verkrijgen anderszins dan bij inbreng in vennootschap door één of                 L’a meer vennoten van in België gelegen onroerende goederen,                              d’ voortkomende         van    een     vennootschap        op     aandelen,      een     so samenwerkende vennootschap (…), geeft, welke ook de wijze zij                         m waarop het geschiedt, aanleiding tot het heffen van het voor verkopingen gesteld recht.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989             Di betreffende de financiering van de gemeenschappen en de gewesten)                     re

#### Afdeling XII - Schenkingen

##### Onderafdeling I - Algemene bepalingen

###### Art. 131

(gewijzigd bij art. 3, § 1 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1).      (m Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 5°   ap van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing            de vanaf 01.01.2002 (art. 45, § 1))                                                      01

Voor de schenkingen onder de levenden van roerende of onroerende                      Po goederen wordt over het bruto-aandeel van elk der begiftigden een                     pe evenredig recht geheven volgens het tarief in onderstaande tabellen                   do aangeduid.

Hierin wordt vermeld:                                                                 Ce

onder a: het percentage dat toepasselijk is op het overeenstemmend                    so gedeelte;                                                                             co

onder b: het totale bedrag van de belasting over de voorgaande                        so gedeelten.                                                                            pr

TABEL I                                                                               TA

Gedeelte van de schenking                 Rechte lijn tussen
Tranche de la donation                    echtgenoten
Ligne directe entre époux

Van                 tot inbegrepen a                                b
De                  à … inclus

EUR                 EUR                   t.h. / p.c.               EUR 0,01                - 12.500              3 12.500              - 25.000              4                         375 25.000              - 50.000              5                         875 50.000              - 100.000             7                         2.125 100.000             - 150.000             10                        5.625 150.000             - 200.000             14                        10.625 200.000             - 250.000             18                        17.625 250.000             - 500.000             24                        26.625 boven de / au-                            30                        86.625 delà de 500.000

TABEL II                                                                             TA

Gedeelte van de           Tussen              Tussen            Tussen alle schenking                 broeders en         ooms of           andere Tranche de la             zusters             tantes en         personen donation                  Entre frères        neven of          Entre toutes et sœurs            nichten           autres Entre oncles      personnes ou tantes et neveux ou nièces Van        tot            a       b           a         b       a         b de         inbegrepen à … inclus EUR        EUR            t.h.    EUR         t.h.      EUR     t.h.      EUR /                   /                 / p.c.                p.c.              p.c.
0,01       - 12.500       20      -           25        -       30        - 12.500 - 25.000           25      2.500       30        3.125   35        3.750 25.000 - 75.000           35      5.625       40        6.875   50        8.125 75.000 - 175.000 50               23.125 55             26.875 65         33.125 boven de / au-delà        65      73.125 70             81.875 80         98.125 de 175.000

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989            Di betreffende de financiering van de gemeenschappen en de gewesten)                    re

###### Art. 1321

(opgeheven bij art. 156 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (ab van toepassing vanaf 01.01.1990 (art. 244))                                      ap

(…)                                                                              (…

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 1322

(vervangen bij art. 157 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (re van toepassing vanaf 01.01.1990 (art. 244))                                      ap

Voor de toepassing van deze afdeling wordt er geen rekening                      Po gehouden met de verwantschapsband voortspruitende uit de                         lie gewone adoptie.

Evenwel wordt, mits bewijs te verstrekken door de belanghebbende,                To met deze adoptieve afstamming rekening gehouden:                                 te

1° wanneer het adoptief kind een kind is van de echtgenoot van de                1° adoptant;

2° wanneer, op het ogenblik van de adoptie, het adoptief kind onder              2° de voogdij was van de openbare onderstand of van een openbaar                    tu centrum voor maatschappelijk welzijn, of wees van een voor België                or gestorven vader of moeder;

3° wanneer het adoptief kind, vóór de leeftijd van eenentwintig jaar             3° bereikt te hebben en gedurende zes onafgebroken jaren, uitsluitend               an van de adoptant of eventueel van hem en zijn echtgenoot te samen,                l’a de hulp en de verzorging heeft gekregen welke kinderen normaal van               en hun ouders krijgen.                                                              no

4° wanneer de adoptie gedaan werd door een persoon van wie al de                 4° afstammelingen voor België gestorven zijn.                                       de

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 133

(gewijzigd bij art. 11 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van   (m toepassing vanaf 17.01.1959 (art. -))                                            ap

Het recht wordt vereffend op de verkoopwaarde van de geschonken                        Le goederen, zonder aftrek van lasten.                                                    di

Gaat de schenking evenwel over ter beurs genoteerde publieke                           To effecten, zo wordt de belastbare grondslag vastgesteld naar de                         bo waarde van de jongste prijscourant gepubliceerd bij order van de                       de regering vóór de datum waarop het recht aan de Staat verworven is.                     où

Gaat de schenking over het vruchtgebruik of de blote eigendom van                      Si een onroerend goed, dan wordt de belastbare grondslag bepaald                          im zoals in artikelen 47 tot 50 is aangeduid.                                             au

Gaat de schenking over een lijfrente of een levenslang pensioen dan                    Si wordt het recht vereffend op het jaarlijks bedrag van de uitkering                     es vermenigvuldigd met het getal dat, gelet op de leeftijd van de                         co beneficiant, in artikel 47 is aangeduid.

Gaat de schenking over een altijddurende rente, dan wordt het recht                    Si vereffend op het twintigvoudig jaarlijks bedrag der rente.                             su

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

###### Art. 134

Voor de toepassing van artikelen 131 tot 133, wordt de last,                           Po bestaande uit een som, een rente of een pensioen onder kastelozen                      so titel bedongen ten bate van een derde die aanneemt, in hoofde van                      tie deze derde als schenking belast en van het aandeel van de                              tie hoofdbegiftigde afgetrokken.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

###### Art. 135

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Het bedrag van het recht vereffend ten laste van de begiftigde, die op        Le het tijdstip waarop het recht aan de Staat verworven is minstens drie         en kinderen in leven heeft die de leeftijd van eenentwintig jaar niet            l’im hadden bereikt, wordt verminderd met 2 t.h. voor elk van deze                 en kinderen, zonder dat de vermindering 62 EUR per kind mag overschrijden.

Deze vermindering wordt ten gunste van de begiftigde echtgenoot               Ce gebracht op 4 t.h. per kind dat de leeftijd van eenentwintig jaar niet        en had bereikt kind, zonder dat de vermindering 124 EUR per kind mag             ré overschrijden.

Voor de toepassing van dit artikel wordt het ontvangen kind voor              Po zover het levensvatbaar geboren wordt, gelijkgesteld met het                  qu geboren kind.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)             re

###### Art. 136

(gewijzigd bij art. 159 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (m van toepassing vanaf 01.01.1990 (art. 244))                                   ap

Het voordeel van de in vorig artikel voorziene verminderingen wordt           Le afhankelijk gesteld van de vermelding in de akte van schenking van            su naam, voornamen, woonplaats, plaats en datum van geboorte van de              pr kinderen van de begiftigde beoogd bij artikel 135.                            vis

Deze vermelding mag gedaan worden onderaan op de akte in een                  Ce verklaring vóór de registratie ondertekend en echt bevestigd door de          sig begiftigde of, in zijn naam, door de werkende notaris.                        in

Ingeval een kind, ontvangen vóór de eischbaarheid van de belasting,           En geboren wordt na de registratie, wordt hetgeen te veel werd geheven           l’e terugbetaald op aanvraag van den betrokkene, te doen binnen twee              de jaar vanaf de geboorte van het kind.                                          l’e

De begiftigde die in verband met het aantal van zijn wettige (1)              Le afstammelingen een onjuiste verklaring heeft afgelegd, verbeurt een           no boete gelijk aan het ontdoken recht.                                          au
----------                                                                    -- Nota:                                                                         No
(1) Bij vergetelheid werd het woord “wettige” niet geschrapt.                 (1

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

###### Art. 137

Ter bepaling van het op een schenking toepasselijk tarief, wordt de                    Po desbetreffende belastbare grondslag gevoegd bij de som die heeft                       ce gediend tot grondslag van heffing op de schenkingen welke reeds                        les tussen dezelfde partijen zijn voorgekomen en vastgesteld werden                        pa door akten die dagtekenen van minder dan drie jaar vóór de datum                       do der nieuwe schenking en vóór laatstbedoelde datum geregistreerd                        de werden of verplicht registreerbaar geworden zijn.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989              Di betreffende de financiering van de gemeenschappen en de gewesten)                      re

###### Art. 1381

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Ongeacht of zij verplicht registreerbaar zijn dan wel vrijwillig tot de                Le formaliteit worden aangeboden, moeten de akten van schenking                           pr vermelding houden of er reeds tussen dezelfde partijen één of meer                     in schenkingen zijn voorgekomen welke vastgesteld werden door akten                       pa die dagtekenen van minder dan drie jaar vóór de datum der nieuwe                       do schenking en vóór dezelfde datum geregistreerd werden of verplicht                     de registreerbaar geworden zijn.

Zo ja, moeten zij den datum der akten vermelden, zomede den                            Da grondslag waarop de belasting werd of dient geheven.                                   qu

De in dit artikel voorziene opgaven en vermeldingen mogen gedaan                       Le worden onderaan de akte in een verklaring vóór de registratie                          fa ondertekend en echt bevestigd door de begiftigde of, in zijn naam,                     do door de werkende notaris.                                                              l’e

Indien bewuste opgaven en vermeldingen ontbreken of indien zij                         Si onjuist of onvolledig zijn, verbeuren de partijen ondeelbaar een                       in geldboete ten bedrage van het ontdoken recht, zonder dat ze lager                      am dan 25 EUR mag zijn.                                                                   EU

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989          Di betreffende de financiering van de gemeenschappen en de gewesten)                  re

###### Art. 1382

(ingevoegd bij art. 7 van de wet van 14.08.1947 (B.S., 17.09.1947). Tekst van      (in toepassing vanaf 27.09.1947 (art.. -))                                             àp

Voor de toepassing van artikelen 137 en 1381 op de aan een                         Po schorsende voorwaarde onderworpen schenkingen, wordt de datum                      un van de vervulling der voorwaarden in de plaats gesteld van de datum                co van de akte.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989          Di betreffende de financiering van de gemeenschappen en de gewesten)                  re

###### Art. 139

Bij onjuist opgeven van den graad van verwantschap tussen schenker                 En en begiftigde, is door deze laatsten, benevens het ontdoken recht,                 et ondeelbaar een boete verschuldigd gelijk aan het bedrag van dat                    él recht.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989          Di betreffende de financiering van de gemeenschappen en de gewesten)                  re

###### Art. 140

(gewijzigd bij art. 43 van de wet van 02.05.2002 (B.S., 18.10.2002 - ed. 2) err.   (m (B.S., 19.10.2002 - ed. 2) heruitgave (B.S., 11.12.2002). Tekst van toepassing     (M vanaf 01.07.2003 (art. 66))                                                        pa

De bij artikel 131 vastgestelde rechten worden verlaagd tot:                       Le

1° 6,60 t.h. voor de schenkingen aan provinciën, gemeenten,                        1 provinciale en gemeentelijke openbare instellingen, instellingen van               au openbaar nut; de Nationale Maatschappij voor de Huisvesting en de                  ét Nationale Landmaatschappij alsmede de door hen erkende                             et maatschappijen,        aan      de       samenwerkende         vennootschap        el «Woningfonds van den bond der Groote Gezinnen», aan de C.V.                        Fa Vlaams Woningfonds van de Grote Gezinnen, aan de C.V.                              no Woningfonds van de Kroostrijke Gezinnen van Wallonië, aan de C.V.                  W

Woningfonds van de gezinnen van het Brusselse Gewest, aan de                     br naamloze of samenwerkende maatschappijen die uitsluitend ten doel                ob hebben leningen te doen met het oog op het bouwen, het aankopen                  ou of het inrichten van volkswoningen, kleine landeigendommen of                    te daarmede gelijkgestelde woningen, alsmede de uitrusting ervan met                m geschikt mobilair, aan de door de wet van 26 Augustus 1913                       in opgerichte Nationale Maatschappij der Waterleidingen, aan de                     les verenigingen gesticht volgens hetgeen voorzien is bij de wetten van              So 18 Augustus 1907 en 1 Maart 1922 en de Nationale Maatschappij der Belgische spoorwegen;

2° 8,80 t.h. voor de schenkingen, met inbegrip van de inbrengsten om             2 niet,   gedaan     aan     vereenigingen      zonder     winstoogmerken,         fa aangenomen mutualiteitsvereenigingen, beroepsvereenigingen en                    re internationale vereenigingen met wetenschappelijk doel.                          in

3° 1,10 t.h. voor de schenkingen, gedaan aan instellingen van                    3° openbaar nut of aan rechtspersonen die in het 2° bedoeld zijn, zo de             pu schenker of de inbrenger zelf een instelling van openbaar nut of een             ou dezer rechtspersonen is.                                                         l’u

3°bis het algemeen vast recht voor de inbrengen om niet aan private              3° stichtingen en stichtingen van openbaar nut of aan rechtspersonen                fo als bedoeld onder 2°, indien de inbrenger zelf een stichting van                 vis openbare nut of een dezer rechtspersonen is.                                     pu

4° 1,10 t.h. voor de schenkingen met inbegrip van de inbrengsten om              4° niet gedaan door de gemeenten aan de pensioenfondsen die zij onder               fa de vorm van een vereniging zonder winstoogmerk hebben opgericht                  fo in uitvoering van een door de voogdijoverheid goedgekeurd                        d’ saneringsplan.

Die verlagingen zijn enkel op de Belgische rechtspersonen                        Ce toepasselijk.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

##### Onderafdeling II - Bijzondere bepalingen voor schenkingen van                 S ondernemingen

###### Art. 140bis

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Het bij artikel 131 vastgestelde recht wordt verlaagd tot 3 pct. voor:           Le

1° de bij authentieke akte vastgestelde overeenkomsten die de                    1° overdracht ten kosteloze titel vaststellen van de volle eigendom van             la een universaliteit van goederen of van een bedrijfstak, waarmee een              de nijverheids-, handels-, ambachts- of landbouwactiviteit, een vrij                un beroep of een ambt of post wordt uitgeoefend.                                    pr

Het bij artikel 131 vastgestelde recht blijft niettemin toepasselijk op          Le de overdrachten van onroerende goederen die gedeeltelijk of geheel               tra tot bewoning worden aangewend of zijn bestemd;                                   ou

2° de bij authentieke akte vastgestelde overeenkomsten die de                    2° overdracht ten kosteloze titel vaststellen van de volle eigendom van             la aandelen of deelbewijzen van een vennootschap waarvan de zetel                   d’ van haar werkelijke leiding is gevestigd in een lidstaat van de                  m Europese Unie en die de uitoefening van een nijverheids-, handels-,              ac ambachts- of landbouwactiviteit, een vrij beroep, of een ambt of post            pr tot doel heeft.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 140ter

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Het bij artikel 140bis vastgestelde verlaagde recht is onderworpen               La aan de volgende voorwaarden:                                                     co

1° de schenker en de begiftigde moeten natuurlijke personen zijn;                1°

2° in geval van toepassing van artikel 140bis, 1°:                               2°

- moet in de akte of in een door de schenker en de begiftigde                    -l gewaarmerkte en ondertekende verklaring onderaan op de akte                      do uitdrukkelijk worden vermeld:

a) dat de schenking betrekking heeft op de volle eigendom van een                a) universaliteit van goederen of van een bedrijfstak, waarmee een                  bi nijverheids-, handels-, ambachts- of landbouwactiviteit, een vrij                ac beroep of een ambt of post wordt uitgeoefend;                                    pr

b) in geval de schenking onroerende goederen bevat, of deze al dan               b) niet gedeeltelijk of geheel tot bewoning worden aangewend of zijn                ci bestemd;                                                                         l’h

- moet in de akte of in een door de begiftigde gewaarmerkte en           -l ondertekende verklaring onderaan op de akte bovendien uitdrukkelijk      do worden vermeld:

a) dat de begiftigde zich ertoe verbindt de activiteit zonder            a) onderbreking voort te zetten gedurende vijf jaar te rekenen van de       in datum van de authentieke akte van schenking;                             de

b) dat de begiftigde zich ertoe verbindt aan de ontvanger der            b) registratie van het kantoor waar de akte werd geregistreerd jaarlijks    l’e het bewijs te leveren van het behoud van de activiteit;                  m

c) dat de begiftigde zich ertoe verbindt de onroerende goederen die      c) met toepassing van het verlaagde recht werden overgedragen, niet         to gedeeltelijk of geheel tot bewoning aan te wenden gedurende een          an ononderbroken periode van vijf jaar te rekenen van de datum van de       bi authentieke akte van schenking;

3° in geval van toepassing van artikel 140bis, 2°:                       3°

- moet de begiftigde een door een notaris, een bedrijfsrevisor of een    -l accountant ondertekend attest afleveren dat bevestigt dat de             ré schenking betrekking heeft op een geheel van aandelen of                 do deelbewijzen, dat minstens 10 pct. van de stemrechten in de              p. algemene vergadering vertegenwoordigt;

- in geval het geheel van de geschonken aandelen of deelbewijzen         -d minder dan 50 pct. van de stemrechten in de algemene vergadering         do vertegenwoordigt,      moet       de    begiftigde        tevens   een   gé aandeelhouderschapsovereenkomst voorleggen, die betrekking               po heeft op ten minste 50 pct. van de stemrechten in de algemene            et vergadering en waarvan de modaliteiten door de' Koning worden vastgesteld.

De hogervermelde documenten worden aan de authentieke akte               Le gehecht;

- moet in de akte of in een door de begiftigde gewaarmerkte en           -l ondertekende verklaring onderaan op de akte bovendien uitdrukkelijk      do worden vermeld:

a) dat de begiftigde zich ertoe verbindt de volle eigendom van de        a) aandelen of deelbewijzen die het voorwerp van de schenking               ou uitmaken gedurende een ononderbroken periode van vijf jaar te            in rekenen van de datum van de authentieke akte van schenking te            de behouden;

b) dat de begiftigde zich ertoe verbindt aan de ontvanger der            b) registratie van het kantoor waar de akte werd geregistreerd jaarlijks    l’e

het bewijs te leveren dat hij de volle eigendom van de geschonken                m aandelen of deelbewijzen heeft behouden.                                         do

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 140quater

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Indien een van de onder de artikelen 140bis en 140ter gestelde                   A voorwaarden uiterlijk bij de aanbieding van de akte ter registratie niet         14 is vervuld, wordt de akte geregistreerd tegen betaling van het bij de            de artikelen 131 tot 140 vastgestelde recht. Geen enkele vordering tot              de teruggaaf is ontvankelijk.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 140quinquies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Behalve in geval van overmacht, wordt het overeenkomstig de                      Sa artikelen 131 tot 140 verschuldigde recht, vermeerderd met de                    à1 wettelijke interest tegen de rentevoet bepaald in burgerlijke zaken te           de rekenen van de datum van registratie van de schenking, opeisbaar ten             du laste van de begiftigde, indien deze laatste:

a) de overeenkomstig artikel 140ter, 2° of 3° aangegane                          a) verbintenissen niet nakomt;                                                      3°

b) in geval van een door artikel 140bis, 1°, bedoelde schenking, de              b) goederen, die dienen voor de uitoefening van een nijverheids-,                   les handels-, ambachts- of landbouwactiviteit, een vrij beroep, of een               au ambt of post, geheel of gedeeltelijk heeft overgedragen binnen de in             ar artikel 140ter bepaalde termijn van vijf jaar; deze bepaling is echter           ce niet van toepassing indien de overdracht gerechtvaardigd is door de              ju uitoefening van de activiteit, van het vrij beroep of van het ambt of de         ch post;

c) in geval van een door artikel 140bis, 2°, bedoelde schenking, binnen          c) de in artikel 140ter bepaalde termijn van vijf jaar de aandelen of               les deelbewijzen geheel of gedeeltelijk heeft overgedragen of de zetel               ac van werkelijke leiding van de vennootschap heeft overgebracht naar               so een staat die geen lid is van de Europese Unie.

Dit artikel is niet van toepassing op de overdrachten van goederen               Le bepaald onder hogervermeld punt b), indien ze plaats hebben door                 po erfopvolging of schenking en de rechthebbenden of de begiftigden de              et door de overledene of de schenker aangegane verbintenissen                       so overnemen.

Dit artikel is evenmin van toepassing op de overdrachten van                     Il n aandelen of deelbewijzen als bepaald onder hogervermeld punt c),                 au indien ze plaats hebben door erfopvolging, door schenking of door                ou overdracht ten bezwarende titel aan een ander lid van de                         d’ aandeelhouderschapsovereenkomst, en dat de rechthebbenden, de                    re begiftigden of de verwerver de door de overledene, de schenker of de             cé overdrager aangegane verbintenissen overnemen.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 140sexies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

De begiftigde die de toepassing van het verlaagd recht heeft genoten             Le kan aanbieden om het overeenkomstig de artikelen 131 tot 140                     pa verschuldigde recht, vermeerderd met de wettelijke interest tegen de             l’in rentevoet bepaald in burgerlijke zaken, opeisbaar te rekenen van de              da datum van registratie van de schenking, te betalen alvorens de                   cin termijn van vijf jaar is verstreken gedurende dewelke de activiteit              pr moet worden voortgezet of de volle eigendom van de aandelen of deelbewijzen behouden moet blijven.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 140septies

(ingevoegd bij art. 68 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Het overeenkomstig artikel 140quinquies opeisbare recht is evenwel                    Le niet opeisbaar indien de volle eigendom van de goederen waarop het                    pa verlaagd recht werd toegepast, het voorwerp uitmaakt van een                          bé overdracht ten kosteloze titel ten voordele van de oorspronkelijke                    en schenker alvorens de termijn van vijf jaar is verstreken gedurende                    pe dewelke de activiteit moet worden voortgezet of de volle eigendom                     ac van de aandelen of deelbewijzen moet behouden blijven.

Gewestelijke bepalingen (art. 3, eerste lid, 8° van de wet van 16.01.1989             Di betreffende de financiering van de gemeenschappen en de gewesten)                     re

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 140octies

(lid 3, vervangen bij art. 65 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   res

Indien artikel 140quinquies van toepassing is worden het recht                        En verschuldigd bij toepassing van de artikelen 131 tot 140 en de                        co interesten vereffend op een verklaring die ter registratie wordt                      un aangeboden op het kantoor waar het verlaagd recht werd                                le vastgesteld, binnen de eerste vier maanden na het verstrijken van het                 l’a jaar tijdens hetwelk de oorzaak van de opeisbaarheid van het recht                    so zich heeft voorgedaan en dit op straffe van een boete gelijk aan dit recht.

Indien artikel 140sexies van toepassing is, biedt de opvolger die het                 En verlaagd recht heeft genoten op het voormelde kantoor een                             du verklaring ter registratie aan waarin de samenstelling en de waarde                   dé van de goederen waarvoor hij het overeenkomstig de artikelen 131                      les tot 140 verschuldigde recht wenst te betalen wordt aangegeven.                        à1

Deze verklaring wordt door de opvolger die het verlaagd recht heeft                   Ce genoten ondertekend en vermeldt de akte, de oorzaak van de                            ré opeisbaarheid van het verschuldigde recht en al de voor de                            élé vereffening van het recht vereiste gegevens. Een kopie wordt                          co bewaard door de bevoegde dienst van de Algemene administratie van                     do de patrimoniumdocumentatie.

###### Art. 140octies

(vervangen bij art. 99 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed. 1).   (re Tekst van toepassing vanaf 07.02.2022 (art. -))                                ap

Indien artikel 140quinquies van toepassing is worden het recht                 En verschuldigd bij toepassing van de artikelen 131 tot 140 en de                 co interesten vereffend op een verklaring die ter registratie wordt               un aangeboden op het kantoor waar het verlaagd recht werd                         le vastgesteld, binnen de eerste vier maanden na het verstrijken van het          l’a jaar tijdens hetwelk de oorzaak van de opeisbaarheid van het recht             so zich heeft voorgedaan en dit op straffe van een boete gelijk aan dit recht.

Indien artikel 140sexies van toepassing is, biedt de opvolger die het          En verlaagd recht heeft genoten op het voormelde kantoor een                      du verklaring ter registratie aan waarin de samenstelling en de waarde            dé van de goederen waarvoor hij het overeenkomstig de artikelen 131               les tot 140 verschuldigde recht wenst te betalen wordt aangegeven.                 à1

Deze verklaring wordt in dubbel gesteld en door de opvolger die het            Ce verlaagd recht heeft genoten ondertekend; één exemplaar ervan blijft           ré berusten op het voormelde kantoor. Ze vermeldt de akte, de oorzaak             pr van de opeisbaarheid van het verschuldigde recht en al de voor de              les vereffening van het recht vereiste gegevens.

#### Afdeling XIII - Huwelijkscontracten en testamenten

###### Art. 141

(opgeheven bij art. 162 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst    (ab van toepassing vanaf 01.01.1990 (art. 244))                                    ap

(…)                                                                            (…

###### Art. 142

tot 157 W.Reg. federaal

De volgende belastingen zijn federaal:                                         Le - het veroordelingsrecht en                                                    - - het titelrecht voor zover het betrekking heeft op de inbreng door een        - natuurlijke persoon van een woning in een buitenlandse                         pe vennootschap (art. 3, eerste lid, 6° wet 16.01.1989 betreffende de             3, financiering van de gemeenschappen en de gewesten).                            co

#### Afdeling XIV- Vonnissen en arresten

###### Art. 142

(gewijzigd bij art. 4 van de wet van 24.12.1993 (B.S., 31.12.1993 - ed. 2). Tekst      (m van toepassing vanaf 01.01.1994 (art. 26))                                             ap

Het recht wordt vastgesteld op 3 pct. voor de in alle zaken gewezen                    Le arresten en vonnissen der hoven en rechtbanken, houdende                               tri definitieve, voorlopige, voornaamste, subsidiaire of voorwaardelijke                   liq veroordeling of vereffening gaande over sommen en roerende                             co waarden, met inbegrip van de beslissingen van de rechterlijke                          dé overheid houdende rangregeling van dezelfde sommen en waarden.                         so

Het recht wordt vereffend, in geval van veroordeling of vereffening                    Le van sommen en roerende waarden, op het samengevoegd bedrag, in                         et hoofdsom, van de uitgesproken veroordelingen of van de gedane                          co vereffeningen ten laste van een zelfde persoon, afgezien van de                        d’ interesten waarvan het bedrag niet door de rechter is becijferd en                     n’ kosten, en, in geval van rangregeling, op het totaal bedrag der aan de                 su schuldeisers uitgedeelde sommen.

###### Art. 143

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

De bepaling van artikel 142 is niet toepasselijk:                                      La

1° op de bevelen in kortgeding en op de arresten gewezen op beroep                     1° daarvan;                                                                               ci

2° op vonnissen en arresten voor zover zij strafboeten, burgerlijke                    2° boeten of tuchtboeten uitspreken;                                                      pé

3° op vonnissen en arresten voor zover zij een veroordeling inhouden                   3° tot het betalen van een uitkering tot onderhoud.                                       pa

Zij is niet toepasselijk wanneer het samengevoegd bedrag van de                        El uitgesproken veroordelingen en van de gedane vereffeningen ten                         co laste van een zelfde persoon, of van de aan de schuldeisers van een                    d’ zelfde persoon uitgedeelde sommen, 12.500 EUR niet overtreft.                          d’

###### Art. 144

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Werd het bij artikel 142 vastgestelde recht op een later veranderd                     Lo vonnis of arrest geheven, dan wordt voor de nieuwe beslissing het                      ar recht van 3 t.h. alleen geheven op de aanvullende veroordeling,                        dé vereffening of rangregeling van sommen of waarden uitgesproken of                      co vastgesteld ten laste van een zelfde persoon en voor zover deze                        pr 12.500 EUR te boven gaat.                                                              au

Wanneer een vonnis of arrest een hoofdelijke veroordeling uitspreekt                   Lo en de op dat vonnis of arrest verschuldigde rechten volledig of                        co gedeeltelijk betaald werden door één van de veroordeelden, maakt de                    pa beslissing, waardoor diegene die betaald heeft, buiten zaak wordt                      ef gesteld, de rechten die deze betaald heeft opeisbaar in hoofde van de                  so andere hoofdelijke veroordeelden, dit alles onverminderd de                            l’a toepassing van de voorschriften genomen in het eerste lid.

###### Art. 145

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Werd het bij artikel 142 vastgestelde recht op een vonnis of arrest                    Lo geheven, dan wordt op elke andere veroordeling ten laste van                           ar dezelfde persoon of van een derde, welke steunt hetzij op dezelfde                     d’ oorzaak hetzij op een verplichting tot waarborg en meer in het                         ob algemeen op elke door de in eerste orde veroordeelde persoon                           ex uitgeoefende verhaalsvordering, het recht van 3 t.h. alleen geheven                    dr op de aanvullende veroordeling tot sommen of waarden, en voor                          va zover deze 12.500 EUR te boven gaat.

###### Art. 146

(gewijzigd bij art. 167 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst            (m van toepassing vanaf 01.01.1990 (art. 244))                                            ap

De vonnissen en arresten die tot bewijs strekken van een                               Le overeenkomst waarbij eigendom of vruchtgebruik van in België                           dé gelegen onroerende goederen overgedragen of aangewezen wordt                           qu en welke aan de desbetreffende belasting niet onderworpen werd                         dr

geven aanleiding, onverminderd het door artikel 142 vastgesteld                    au recht, tot het recht en eventueel tot de boete waaraan de                          ac overeenkomst zou onderworpen zijn indien zij in een minnelijke akte vastgesteld ware geweest.

Dit geldt eveneens, zelfs indien de rechterlijke beslissing die tot bewijs         Il van de overeenkomst strekt, de ontbinding of herroeping ervan voor                 co om 't even welke reden uitspreekt, tenzij uit de beslissing blijkt dat ten         qu hoogste één jaar na de overeenkomst een eis tot ontbinding of                      la herroeping, zelfs bij een onbevoegd rechter, werd ingesteld.                       ré ju

###### Art. 147

(vervangen bij art. 10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst   (re van toepassing vanaf 01.01.1961 (art. 39))                                         ap

De vonnissen en arresten houdende vernietiging, ontbinding of                      Le herroeping van een overeenkomst waarbij eigendom of vruchtgebruik                  d’ van in België gelegen onroerende goederen overgedragen of                          d’ aangewezen wordt, geven geen aanleiding tot heffing van het                        pr evenredig recht uit hoofde van dat te niet doen, tenzij die                        pr uitgesproken zij ten voordele van een ander persoon dan een van de                 co partijen bij de overeenkomst, haar erfgenamen of legatarissen. In                  les laatstbedoeld geval worden de rechten geheven die verschuldigd                     ré waren geweest indien de vernietiging, de ontbinding of de herroeping het voorwerp van een minnelijke akte had uitgemaakt.

###### Art. 148

(vervangen bij art.10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst    (re van toepassing vanaf 01.01.1961 (art. 39))                                         ap

Exequaturs van scheidsrechterlijke uitspraken en van buitenlands                   Le gewezen rechterlijke beslissingen worden, voor de toepassing van dit               ju Wetboek, als een geheel met de desbetreffende akte aangezien, en                   l’a zijn aan dezelfde rechten als de in België gewezen vonnissen en                    au arresten onderworpen.                                                              ju

Deze rechten zijn eveneens van toepassing in geval van aanbieding                  Ce ter registratie van een buitenlands gewezen rechterlijke beslissing                l’e indien zij van rechtswege in België uitvoerbaar is.                                ce

###### Art. 149

(vervangen bij art. 10, § 2, van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst   (re van toepassing vanaf 01.01.1961 (art. 39))                                         ap

Behoudens in de gevallen beoogd door de artikelen 146 tot 148                      Sa maken de vonnissen en arresten geen evenredig recht eisbaar uit                    ne hoofde van de overeenkomsten waarvan zij het bestaan vaststellen.                  co

###### Art. 150

(hersteld bij art. 12 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst van      (ré toepassing vanaf 01.11.1986 (art. 15))                                             ap

Om de invordering van de rechten en, in voorkomend geval, van de                   Il e boeten eisbaar uit hoofde van deze afdeling te waarborgen, wordt,                  et ten bate van de Staat, een voorrecht ingesteld op de sommen en                     se waarden die het voorwerp uitmaken van de veroordeling, vereffening                 co of rangregeling.

De rechten en boeten bedoeld in het eerste lid gaan boven alle                     Le schuldvorderingen van de begunstigden van de veroordelingen,                       de vereffeningen of rangregelingen.

###### Art. 151

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960).         (ab Tekst van toepassing vanaf 01.01.1961 (art. 39))                                   ap

(…)                                                                                (…

###### Art. 152

(opgeheven bij art. 10, § 3, van de wet van 12.07.1960 (B.S., 09.11.1960).         (ab Tekst van toepassing vanaf 01.01.1961 (art. 39))                                   ap

(…)                                                                                (…

#### Afdeling XV - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).        (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van                 ap 04.11.1968 (B.S., 13.11.1968))                                                     13

###### Art. 153

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).   (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van            ap 04.11.1968 (B.S., 13.11.1968))                                                13

( …)                                                                          (…

#### Afdeling XVI - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).   (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, van het KB van            ap 04.11.1968 (B.S., 13.11.1968))                                                13

###### Art. 154

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).   (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,      ap 13.11.1968)))                                                                 13

(…)                                                                           (…

#### Afdeling XVII - (…)

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).   (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,      ap 13.11.1968)))                                                                 13

###### Art. 155

(opgeheven bij art. 2/art. 29 van de wet van 10.10.1967 (B.S., 31.10.1967).   (ab Tekst van toepassing vanaf 01.01.1969 (art. 3, 28°, KB 04.11.1968 (B.S.,      ap 13.11.1968)))                                                                 13

(…)                                                                           (…

#### Afdeling XVIII - (…)

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst    (ab van toepassing vanaf 01.01.1961 (art. 39))                                    ap

###### Art. 156

(opgeheven bij art. 11 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst          (ab van toepassing vanaf 01.01.1961 (art. 39))                                          ap

(…)                                                                                 (…

#### Afdeling XIX - Protesten

###### Art. 157

(opgeheven bij art. 73 van de wet van 14.01.2013 (B.S., 01.03.2013). Tekst          (ab van toepassing vanaf 01.01.2013 (art. 85))                                          ap

(…)                                                                                 (…

###### Art. 158

W.Reg. federaal

Het specifiek vast recht voor bijlagen is een federale belasting (art. 3,           Le a contrario, wet 16.01.1989 betreffende de financiering van de                      a gemeenschappen en de gewesten).                                                     co

#### Afdeling XIXbis - Aangehechte akten en geschriften

(ingevoegd bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).        (in Tekst van toepassing vanaf 01.04.2014 (art. 87, 3°))                                ap

###### Art. 158

(hersteld bij art. 51 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2). Tekst   (ré van toepassing vanaf 01.04.2014 (art. 87, 3°))                                      ap

De aangehechte akten of geschriften bedoeld in artikel 26, tweede lid,              Le worden geregistreerd tegen betaling van één specifiek vast recht van                en 100 euro voor al die documenten samen, behalve indien sommige                       eu ervan een of meer andere in dit hoofdstuk bepaalde rechten                          re verschuldigd maken, in welk geval, naast de rechten verschuldigd                    ch voor de registratie van laatstbedoelde documenten, het specifiek vast               de recht van 100 euro eenmaal verschuldigd is voor de registratie van de               fo overige documenten.

1°, 12°: gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van               1° 16.01.1989 betreffende de financiering van de gemeenschappen en de                    16 gewesten)

TOEKOMSTIG RECHT (vanaf 01.01.2028)

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en Se

onderhevig aan het algemeen vast recht                                                as

###### Art. 159

(lid 1, 8°, b), gewijzigd bij art. 66 van de wet van 12.05.2024 (B.S., 30.05.2024 –   (al ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders van een    éd ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   nu respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   da

Worden van het evenredig recht vrijgesteld en aan het algemeen vast                   So recht onderworpen:

1° de aanwijzing van lastgever, op voorwaarde:                                        1

a) dat het vermogen om een lastgever aan te wijzen in de akte van                     a) toewijzing of koop voorbehouden is;                                                   d’a

b) dat de aanwijzing bij authentieke akte geschied is;                                b)

c) dat zij bij exploot van gerechtsdeurwaarder aan de ontvanger der                   c) registratie betekend wordt of dat de akte ter formaliteit aangeboden                  l’e wordt uiterlijk op de eerste werkdag na de dag van de toewijzing of                   pr van het contract.

Bij niet-voldoening aan deze voorwaarden wordt de aanwijzing van                      A lastgever voor de toepassing van dit Wetboek als wederverkoop                         co beschouwd.

Met afwijking van het vorenstaande:                                                   Pa

a) moet de aanwijzing van lastgever, bij toewijzingen die wettelijk                   a) gedaan zijn onder de schorsende voorwaarde van ontstentenis van                       lég opbod, om van het evenredig recht vrijgesteld te zijn, gedaan worden                  po vóór de notaris die de toewijzing gedaan heeft of hem betekend                        ap worden uiterlijk op de eerste werkdag na die waarop de wettelijke                     qu termijn voor opbod verstrijkt;

b) moet de aanwijzing van lastgever, in geval van toewijzing ten                      b) gevolge van hoger bod op vrijwillige vervreemding van onroerende                      su goederen, om van het evenredig recht vrijgesteld te zijn, gedaan                      ex worden vóór de notaris die de toewijzing heeft gedaan of hem

betekend worden uiterlijk op de eerste werkdag na de dag van de           à toewijzing.                                                               qu

In die gevallen wordt de aanwijzing ingeschreven of vermeld               Da onderaan op het proces-verbaal van toewijzing, zonder dat zij aan de      ve ontvanger der registratie behoeft te worden betekend;                     l’e

2° de toewijzingen naar aanleiding van rouwkoop, van roerende of          2 onroerende goederen, wanneer zij geen aanleiding geven tot de             im heffing van een hoger evenredig recht dan datgene geheven op de           su vorige toewijzing. In het tegenovergesteld geval wordt laatstbedoeld      le recht afgerekend van het bedrag van de belasting waartoe de               au daaropvolgende toewijzing aanleiding geeft.

Hetzelfde regime is van toepassing op de toewijzingen naar                Le aanleiding van prijsverhoging in de gevallen waarin het voorbehoud        su van prijsverhoging geen schorsende voorwaarde uitmaakt.                   un

3° De overeenkomsten die strekken tot de overdracht van het               3 vruchtgebruik op de blote eigenaar, wanneer het evenredig                 nu registratierecht of het successierecht door de blote eigenaar of door     dr een vorigen blote eigenaar, zijn rechtsvoorganger, op de waarde van       pr de volle eigendom werd voldaan;                                           pl

4° (…)                                                                    4

5° (…)                                                                    5

6° (…)                                                                    6

7° de overdragende of aanwijzende overeenkomsten, andere dan de           7 inbrengen onderworpen aan het in artikel 115bis bepaalde recht die        so buitenslands gelegen onroerende goederen tot voorwerp hebben,             im zomede de huurcontracten van dergelijke goederen;                         im

8° de overdragende of aanwijzende vervreemdingen onder                    8 bezwarende titel, andere dan die welke aan het in artikel 115bis          qu bepaalde recht onderworpen zijn van op te richten, in oprichting zijnde   ér of nieuwe opgerichte gebouwen, op voorwaarde dat de belasting over        co de toegevoegde waarde opeisbaar is voor de levering van de                de vervreemde     gebouwen;      de    vestigingen,   overdrachten     of    de wederoverdrachten van de zakelijke rechten bedoeld in artikel 9,          la tweede lid, 2°, van het Wetboek van de belasting over de                  co toegevoegde waarde met betrekking tot op te richten, in oprichting,       la zijnde of nieuw opgerichte gebouwen, op voorwaarde dat de                 dr belasting over de toegevoegde waarde opeisbaar is op de vestiging of de overdracht van deze rechten.

De vrijstelling geldt niet voor de grond begrepen in de overeenkomst.     L’e l’a

Wanneer de gebouwen samen met de grond waarop ze staan voor                  Lo een enige prijs worden vervreemd, wordt het evenredig recht wegens           leq de vervreemding van de grond berekend over de verkoopwaarde van              re de grond, geraamd op het tijdstip van de vervreemding, doch met              à inachtneming van de staat van de grond vóór de aanvang van het               co werk. Wanneer de vestiging of de overdracht van de in het eerste lid         1e bedoelde zakelijke rechten tevens betrekking heeft op de grond               les waarop de gebouwen staan en voor een enige prijs gebeurt, wordt het          pr evenredig recht wegens de vestiging of de overdracht van die rechten         le op de grond berekend over de waarde van die rechten, geraamd op              co het tijdstip van de vestiging of de overdracht, doch met inachtneming        co van de staat van de grond vóór de aanvang van het werk. In die               co gevallen worden de gegevens nodig voor de berekening van de                  liq rechten opgeheven in een verklaring als omschreven in artikel 168.

Indien de overeenkomst betrekking heeft op het vruchtgebruik of de           Si blote eigendom van de grond, wordt de belastbare grondslag bepaald           ba op de wijze vermeld in de artikelen 47 tot 50.                               à5

De bepalingen van dit 8° zijn alleen toepasselijk, indien in de akte of in   L’a een vóór de registratie bij de akte te voegen geschrift worden               l’in vermeld:                                                                     l’e

a) het jaar waarin, in voorkomend geval, de onroerende voorheffing           a) van het gebouw waarop de overeenkomst betrekking heeft voor het              en eerst ten kohiere is gebracht;                                               co

b) het kantoor waarnaar de belastingplichtige de aangifte moet               b) verzenden voor de heffing van de belasting over de toegevoegde               pe waarde;

c) wanneer de overeenkomst het werk is van een andere dan in artikel         c) 12, § 2, van het Wetboek van de belasting over de toegevoegde waard          à bedoelde belastingplichtige, de datum waarop hij kennis heeft                laq gegeven van zijn bedoeling de verrichting te doen met betaling van de        ap belasting over de toegevoegde waarde.

In geval van onjuistheid van die vermeldingen, verbeurt de cedent een        En boete gelijk aan het ontdoken recht;                                         ég

9° (…)                                                                       9

10° de contracten van onroerende financieringshuur bedoeld in                10 artikel 44, § 3, 2°, b, van het Wetboek van de belasting over de             l’a toegevoegde waarde;

11° de inbreng van goederen in Europese economische                          11 samenwerkingsverbanden;                                                      éc

12° de teruggave van de onroerende goederen aan de leden van                      12 Europese economische samenwerkingsverbanden die deze goederen                     éc hebben ingebracht, wanneer de teruggave gebeurt tengevolge van de                 int uittreding    van    deze     leden     of   de     ontbinding     van    het     gr samenwerkingsverband.

Indien onroerende goederen verkregen worden in andere                             Si omstandigheden dan deze voorzien in het vorige lid, is voor deze                  à verkrijging, hoe zij ook gebeurt, het voor verkopingen bepaalde recht             qu verschuldigd.

13° (…)                                                                           13

14° de inbrengen van onroerende goederen, andere dan die welke                    14 gedeeltelijk of geheel tot bewoning aangewend worden of bestemd                   ef zijn en door een natuurlijke persoon ingebracht worden, in                        siè vennootschappen met zetel van werkelijke leiding en statutaire zetel              te buiten België, of met statutaire zetel in België doch met zetel van               bi werkelijke leiding op het grondgebied van één van de lidstaten van de             ou Europese Unie. Deze vrijstelling geldt voor zover de inbreng met                  da maatschappelijke rechten wordt vergolden. Indien de inbreng zowel                 de in België gelegen onroerende goederen als andere goederen omvat                   im wordt, niettegenstaande elk strijdig beding, de vergelding die anders             fa dan door toekenning van maatschappelijke rechten geschiedt, geacht                ré evenredig verdeeld te zijn tussen de waarde die aan de onroerende                 en goederen is toegekend en die welke aan de andere goederen is                      bi toegekend. In de mate dat de inbreng betrekking heeft op in België                el gelegen onroerende goederen wordt hij onderworpen aan het recht voorgeschreven voor verkopingen.

In geval van onjuiste verklaring betreffende de aanwending of de                  En bestemming van het onroerend goed, worden de bijvoeglijke rechten                 de opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.              et

#### Afdeling XX - Akten vrijgesteld van het evenredig recht en onderhevig aan het algemeen vast recht

###### Art. 159

(14°, gewijzigd bij art. 23 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst   (1 van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                 ap

Worden van het evenredig recht vrijgesteld en aan het algemeen vast               So recht onderworpen:

1° de aanwijzing van lastgever, op voorwaarde:                                    1

a) dat het vermogen om een lastgever aan te wijzen in de akte van       a) toewijzing of koop voorbehouden is;                                     d’a

b) dat de aanwijzing bij authentieke akte geschied is;                  b)

c) dat zij bij exploot van gerechtsdeurwaarder aan de ontvanger der     c) registratie betekend wordt of dat de akte ter formaliteit aangeboden    l’e wordt uiterlijk op de eerste werkdag na de dag van de toewijzing of     pr van het contract.

Bij niet-voldoening aan deze voorwaarden wordt de aanwijzing van        A lastgever voor de toepassing van dit Wetboek als wederverkoop           co beschouwd.

Met afwijking van het vorenstaande:                                     Pa

a) moet de aanwijzing van lastgever, bij toewijzingen die wettelijk     a) gedaan zijn onder de schorsende voorwaarde van ontstentenis van         lég opbod, om van het evenredig recht vrijgesteld te zijn, gedaan worden    po vóór de notaris die de toewijzing gedaan heeft of hem betekend          ap worden uiterlijk op de eerste werkdag na die waarop de wettelijke       qu termijn voor opbod verstrijkt;

b) moet de aanwijzing van lastgever, in geval van toewijzing ten        b) gevolge van hoger bod op vrijwillige vervreemding van onroerende        su goederen, om van het evenredig recht vrijgesteld te zijn, gedaan        ex worden vóór de notaris die de toewijzing heeft gedaan of hem            à betekend worden uiterlijk op de eerste werkdag na de dag van de         qu toewijzing.

In die gevallen wordt de aanwijzing ingeschreven of vermeld             Da onderaan op het proces-verbaal van toewijzing, zonder dat zij aan de    ve ontvanger der registratie behoeft te worden betekend;                   l’e

2° de toewijzingen naar aanleiding van rouwkoop, van roerende of        2 onroerende goederen, wanneer zij geen aanleiding geven tot de           im heffing van een hoger evenredig recht dan datgene geheven op de         su vorige toewijzing. In het tegenovergesteld geval wordt laatstbedoeld    le recht afgerekend van het bedrag van de belasting waartoe de             au daaropvolgende toewijzing aanleiding geeft.

Hetzelfde regime is van toepassing op de toewijzingen naar              Le aanleiding van prijsverhoging in de gevallen waarin het voorbehoud      su van prijsverhoging geen schorsende voorwaarde uitmaakt.                 un

3° De overeenkomsten die strekken tot de overdracht van het             3 vruchtgebruik op de blote eigenaar, wanneer het evenredig               nu registratierecht of het successierecht door de blote eigenaar of door   dr

een vorigen blote eigenaar, zijn rechtsvoorganger, op de waarde van       pr de volle eigendom werd voldaan;                                           pl

4° (…)                                                                    4

5° (…)                                                                    5

6° (…)                                                                    6

7° de overdragende of aanwijzende overeenkomsten, andere dan de           7 inbrengen onderworpen aan het in artikel 115bis bepaalde recht die        so buitenslands gelegen onroerende goederen tot voorwerp hebben,             im zomede de huurcontracten van dergelijke goederen;                         im

8° de overdragende of aanwijzende vervreemdingen onder                    8 bezwarende titel, andere dan die welke aan het in artikel 115bis          qu bepaalde recht onderworpen zijn van op te richten, in oprichting zijnde   ér of nieuwe opgerichte gebouwen, op voorwaarde dat de belasting over        co de toegevoegde waarde opeisbaar is voor de levering van de                de vervreemde     gebouwen;      de    vestigingen,   overdrachten     of    de wederoverdrachten van de zakelijke rechten bedoeld in artikel 9,          la tweede lid, 2°, van het Wetboek van de belasting over de                  co toegevoegde waarde met betrekking tot op te richten, in oprichting,       la zijnde of nieuw opgerichte gebouwen, op voorwaarde dat de                 dr belasting over de toegevoegde waarde opeisbaar is op de vestiging of de overdracht van deze rechten.

De vrijstelling geldt niet voor de grond begrepen in de overeenkomst.     L’e l’a

Wanneer de gebouwen samen met de grond waarop ze staan voor               Lo een enige prijs worden vervreemd, wordt het evenredig recht wegens        leq de vervreemding van de grond berekend over de verkoopwaarde van           re de grond, geraamd op het tijdstip van de vervreemding, doch met           à inachtneming van de staat van de grond vóór de aanvang van het            co werk. Wanneer de vestiging of de overdracht van de in het eerste lid      1e bedoelde zakelijke rechten tevens betrekking heeft op de grond            les waarop de gebouwen staan en voor een enige prijs gebeurt, wordt het       pr evenredig recht wegens de vestiging of de overdracht van die rechten      le op de grond berekend over de waarde van die rechten, geraamd op           co het tijdstip van de vestiging of de overdracht, doch met inachtneming     co van de staat van de grond vóór de aanvang van het werk. In die            co gevallen worden de gegevens nodig voor de berekening van de               liq rechten opgeheven in een verklaring als omschreven in artikel 168.

Indien de overeenkomst betrekking heeft op het vruchtgebruik of de        Si blote eigendom van de grond, wordt de belastbare grondslag bepaald        ba op de wijze vermeld in de artikelen 47 tot 50.                            à5

De bepalingen van dit 8° zijn alleen toepasselijk, indien in de akte of in   L’a een vóór de registratie bij de akte te voegen geschrift worden               l’in vermeld:                                                                     l’e

a) het jaar waarin, in voorkomend geval, de onroerende voorheffing           a) van het gebouw waarop de overeenkomst betrekking heeft voor het              en eerst ten kohiere is gebracht;                                               co

b) het kantoor waar de belastingplichtige de aangifte moet indienen          b) voor de heffing van de belasting over de toegevoegde waarde;                 pe

c) wanneer de overeenkomst het werk is van een andere dan in artikel         c) 12, § 2, van het Wetboek van de belasting over de toegevoegde waard          à bedoelde belastingplichtige, de datum waarop hij kennis heeft                laq gegeven van zijn bedoeling de verrichting te doen met betaling van de        ap belasting over de toegevoegde waarde.

In geval van onjuistheid van die vermeldingen, verbeurt de cedent een        En boete gelijk aan het ontdoken recht;                                         ég

9° (…)                                                                       9

10° de contracten van onroerende financieringshuur bedoeld in                10 artikel 44, § 3, 2°, b, van het Wetboek van de belasting over de             l’a toegevoegde waarde;

11° de inbreng van goederen in Europese economische                          11 samenwerkingsverbanden;                                                      éc

12° de teruggave van de onroerende goederen aan de leden van                 12 Europese economische samenwerkingsverbanden die deze goederen                éc hebben ingebracht, wanneer de teruggave gebeurt tengevolge van de            int uittreding   van    deze    leden    of   de    ontbinding     van    het    gr samenwerkingsverband.

Indien onroerende goederen verkregen worden in andere                        Si omstandigheden dan deze voorzien in het vorige lid, is voor deze             à verkrijging, hoe zij ook gebeurt, het voor verkopingen bepaalde recht        qu verschuldigd.

13° (…)                                                                      13

14° de inbrengen van onroerende goederen, andere dan die welke               14 gedeeltelijk of geheel tot bewoning aangewend worden of bestemd              ef zijn en door een natuurlijke persoon ingebracht worden, in                   siè vennootschappen met zetel van werkelijke leiding en statutaire zetel         te buiten België, of met statutaire zetel in België doch met zetel van          bi werkelijke leiding op het grondgebied van één van de lidstaten van de        ou Europese Unie. Deze vrijstelling geldt voor zover de inbreng met             da maatschappelijke rechten wordt vergolden. Indien de inbreng zowel            de

in België gelegen onroerende goederen als andere goederen omvat                 im wordt, niettegenstaande elk strijdig beding, de vergelding die anders           fa dan door toekenning van maatschappelijke rechten geschiedt, geacht              ré evenredig verdeeld te zijn tussen de waarde die aan de onroerende               en goederen is toegekend en die welke aan de andere goederen is                    bi toegekend. In de mate dat de inbreng betrekking heeft op in België              el gelegen onroerende goederen wordt hij onderworpen aan het recht voorgeschreven voor verkopingen.

In geval van onjuiste verklaring betreffende de aanwending of de                En bestemming van het onroerend goed, worden de bijvoeglijke rechten               de opeisbaar en verbeurt iedere partij een boete gelijk aan de rechten.            et

### HOOFDSTUK V - Registratie in debet

###### Art. 160

(gewijzigd bij art. 5 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van   (m toepassing vanaf 01.01.2015 (art. 8))                                           àp

In afwijking van artikel 169ter, worden in debet geregistreerd:                 Pa

1° de akten opgemaakt ten verzoek van de persoon die                            1 rechtsbijstand heeft verkregen voor de rechtspleging waarop                     ju bedoelde akten betrekking hebben, met inbegrip van de akten tot ten             co uitvoerlegging van het vonnis of arrest.

Het gaat evenzo met de rechterlijke beslissingen wanneer                        Il e rechtsbijstand aan de eiser werd toegestaan. Wanneer bijstand aan               au de verweerder werd toegestaan en de eiser in gebreke blijft de op het           de vonnis of arrest verschuldigde rechten te consigneren, kan de                   ou verweerder registratie in debet ervan bekomen.

Verlening van bijstand dient te worden vermeld in al de akten die               Il ervan genieten. Deze vermelding moet de datum der beslissing                    ac alsmede het gerecht of het bureau voor rechtsbijstand, dat ze heeft             dé getroffen, aanduiden.

De rechten alsmede de andere kosten worden ingevorderd                          Le overeenkomstig de bepalingen van het Gerechtelijk Wetboek;                      au

2° de akten en vonnissen betreffende procedures bij faillissement,              2 wanneer de kosteloosheid door de rechtbank werd bevolen.                        fa

De kosteloosheid van de rechtspleging moet vermeld worden in alle               Il akten die ze genieten.                                                          ac

De rechten alsmede de andere kosten worden ingevorderd                            Le overeenkomstig de bepalingen van het Gerechtelijk Wetboek;                        au

3° de akten betreffende de vorderingen tot interpretatie of tot                   3 verbetering van een vonnis of arrest.                                             re

De rechten worden ingevorderd overeenkomstig de bepalingen van                    Le het Gerechtelijk Wetboek;                                                         ju

4° de akten opgemaakt ten verzoek en ter verdediging van de                       4 beklaagden of betichten in lijfstraffelijke, boetstraffelijke of                  ac politiezaken er weze al dan niet een burgerlijke partij in het geding met         ou inbegrip van de akten waartoe de borg, welke dient gesteld om de                  le voorlopige invrijheidstelling van een voorlopig gedetineerd betichte te           d’ bekomen, aanleiding geeft.

De rechten worden in de gerechtskosten begrepen en als zodanig                    Le ingevorderd ten laste van de tot betaling er van veroordeelde partij.             su

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989         Di betreffende de financiering van de gemeenschappen en de gewesten)                 re

### HOOFDSTUK VI - Kosteloze registratie

###### Art. 161

(1° en 12°, gewijzigd bij art. 29 van de wet van 10.02.2026 (B.S., 27.02.2026).   (1 Tekst van toepassing vanaf 09.03.2026 (art. 33, lid 1))   (2) Te

Worden kosteloos geregistreerd:                                                   So

1° Akten in der minne verleden ten name of ten bate van de Staat,                 1 gefedereerde entiteiten en de openbare instellingen ervan.                        en

De akten in der minne, die betrekking hebben op onroerende                        Le goederen die uitsluitend bestemd zijn voor onderwijs, verleden ten                af name of ten bate van de inrichtende machten van het                               or gemeenschapsonderwijs of het gesubsidieerd onderwijs, alsook ten                  l'e name of ten bate van verenigingen zonder winstoogmerk voor                        as patrimoniaal beheer die tot uitsluitend doel hebben onroerende                    ob goederen ter beschikking te stellen voor onderwijs dat door de                    di voornoemde inrichtende machten wordt versterkt.

De akten in der minne verleden ten name of ten bate van de naamloze               Le vennootschappen van publiek recht ASTRID, BIO, Infrabel, HR Rail en               an NMBS.

Deze beschikkingen zijn echter slechts van toepassing op de akten       Ce waarvan de kosten wettelijk ten laste van bedoelde organismen           fra vallen.

1°bis De vonnissen en arresten houdende veroordeling van de Staat,      1° de Gemeenschappen en de Gewesten, van de openbare instellingen          Co die zijn opgericht door de Staat, en van de inrichtingen van de         de Gemeenschappen en de Gewesten.

2° Overdrachten in der minne van onroerende goederen ten                2 algemenen nutte, aan Staat, provinciën, gemeenten, openbare             l’E instellingen en aan alle andere tot onteigening gerechtigde             to organismen of personen: akten betreffen de wederafstand na              ac onteigening ten algemenen nutte in de gevallen waarin hij bij de wet    pu toegelaten is; akten tot vaststelling van een ruilverkaveling of een    ac herverkaveling verricht met inachtneming van de bepalingen van          ex
Hoofdstuk VI van Titel I van de wet houdende organisatie van de         l’a ruimtelijke ordening en van de stedebouw. De akten houdende             la overdracht van een afgedankte bedrijfsruimte aan de Staat of een        au andere publiekrechtelijke rechtspersoon.

3° De akten houdende oprichting, wijziging, verlenging of ontbinding    3 van de Nationale Maatschappij der Waterleidingen, van de                di verenigingen overeenkomstig de bepalingen der wetten van 18             as augustus 1907 en van 1 maart 1922 gevormd, van de Maatschappij          du voor het Intercommunaal Vervoer te Brussel, van de maatschappij         Br voor tussengemeentelijk vervoer beheerst door de wet betreffen de       lo oprichting van maatschappijen voor stedelijk gemeenschappelijk          de vervoer, van de Federale Investeringsmaatschappij, de gewestelijke      d’ investeringsmaatschappijen en van de Belgische Naamloze                 la Vennootschap tot Exploitatie van het Luchtverkeer (Sabena).

4° Akten die, bij toepassing van de organieke wet betreffen de          4 openbare centra voor maatschappelijk welzijn, de overgave               d’ vaststellen van goederen aan of de inbreng in openbare centra voor      pu maatschappelijk welzijn ofwel de overgave van goederen aan of de        pr inbreng in op grond van voornoemde wet opgerichte verenigingen,         as evenals akten houdende verdeling, na ontbinding of splitsing van een bovenbedoelde vereniging.

5° Waarmerkingen en akten van bekendheid, in de gevallen bedoeld        5 in artikel 139 van de hypotheekwet van 16 december 1851;                l’a

6° Akten houdende verkrijging door vreemde Staten van onroerende        6° goederen die bestemd zijn tot vestiging van hun diplomatieke of         de consulaire vertegenwoordiging in België, of voor de woning van het      co hoofd der standplaats.

De kosteloosheid is echter ondergeschikt aan de voorwaarde dat           La wederkerigheid aan de Belgische Staat toegekend wordt.                   so

7° De akten, vonnissen en arresten betreffen de uitvoering van de        7° wet houdende bijzondere maatregelen inzake ruilverkaveling van           de landeigendommen in der minne;                                            de

8° (…)                                                                   8°

9° Akten, vonnissen en arresten betreffen de uitvoering der wet op       9° de ruilverkaveling van landeigendommen uit kracht van de wet en de       re wet houdende bijzondere maatregelen inzake ruilverkaveling van           pa landeigendommen uit kracht van de wet bij de uitvoering van grote        de infrastructuurwerken.

10°      Akten   tot    vaststelling   van   een    vereniging    van    10 kolenmijnconcessies, een afstand, een uitwisseling of een                ho verpachting van een gedeelte van deze concessies.                        ce

De kosteloosheid is ondergeschikt aan de voorwaarde dat een              La eensluidend verklaard afschrift van het koninklijk besluit, waarbij de   l’e verrichting toegelaten of bevolen wordt, aan de akte gehecht is op het   au ogenblik der registratie.

Het eerste lid is mede van toepassing wanneer bedoelde akten             Le terzelfder tijd de afstand vaststellen van goederen die voor de          co exploitatie van de afgestane concessie of het afgestane                  l’e concessiegedeelte worden gebruikt.

11° De akten en attesten die gevoegd moeten worden bij de akten          11 van schenking van ondernemingen.                                         d'

12°                                                                      12
a) de akten houdende verhuring, onderverhuring of overdracht van         a) huur van in België gelegen onroerende goederen of gedeelten van          de onroerende goederen, die uitsluitend bestemd zijn tot huisvesting van    au een gezin of van één persoon;

b) (…)                                                                   b)

c) de plaatsbeschrijvingen opgemaakt naar aanleiding van een onder       c)
a) bedoelde akte;

d) de documenten die krachtens wettelijke, decretale of ordonnantiële    d) bepalingen gevoegd zijn bij een onder a) bedoelde akte op het ogenblik   or dat zij ter registratie wordt aangeboden.                                pr

13° De overeenkomsten bedoeld in artikel 132bis van het Wetboek          13 van de inkomstenbelastingen 1992.                                        les

14° een authentieke volmacht die uitsluitend bestemd is om een of                    14 meer partijen te laten vertegenwoordigen bij het verlijden van een                   re authentieke akte, op voorwaarde dat de instrumenterende                              au ambtenaar voor het verlijden van de volmacht geen ereloon, vacaties                  ré of kosten vraagt en voor zover de volmacht uitsluitend effect sorteert               la binnen de zes maanden na de ondertekening ervan.                                     se

15° De verklaring van verwerping ten overstaan van een notaris                       15 bedoeld in artikel 4.44, eerste lid, van het Burgerlijk Wetboek, onder               4. de voorwaarden bedoeld in het derde lid van hetzelfde artikel.           (1) m

De bijlagen bij een dergelijke verklaring worden ook kosteloos                       Le geregistreerd, behalve wanneer ze een in Titel I, Hoofdstuk IV van het               au Wetboek bepaald recht, ander dan het in artikel 158 bepaalde recht,                  Ch opeisbaar maken.

16° de akten van erfopvolging bedoeld in artikel 3.30, § 1, 7°, van het              16 Burgerlijk Wetboek, op voorwaarde dat de instrumenterende                            co ambtenaar voor het opstellen van de akte geen vacaties of kosten                     va vraagt en de akte opgesteld wordt binnen de 6 maanden na het                         ét overlijden.
----------                                                                           -- Nota:                                                                                No
(1) Vanaf 03.08.2017 tot 02.08.2020 mag het netto actief van de                      (1 nalatenschap niet meer bedragen dan 5.000 EUR. Vanaf 03.08.2020 tot                  dé 31.07.2023 bedraagt het geïndexeerde bedrag 5.219,21 euro. Vanaf                     de 01.08.2023 tot 31.07.2026 bedraagt het geïndexeerde bedrag 6.093,20                  6.0 euro (EE/107.394).
(2) Wat betreft art. 161, 1°, W.Reg.: De federale wetgever treedt hier uitsluitend   (2 op in het kader van niet-geregionaliseerde belastingen, terwijl de tarifering van    ex gewestelijke registratierechten onder de bevoegdheid van de gewesten valt.           ta Door de tekst te wijzigen, rationaliseert de federale wetgever de bepalingen die     de van toepassing zijn op zijn eigen belastingen, zonder de regionale versies te        dis beïnvloeden, die afzonderlijk blijven en niet door deze wijzigingen worden           ve geraakt (Parl.St., Kamer: 56-1127 001, blz. 8).                                      m

###### Art. 161/1

(gewijzigd bij art. 1 van het KB van 03.10.2019 (B.S., 30.10.2019). Tekst van        (m toepassing vanaf 09.11.2019 (art. -))                                                ap

Onverminderd artikel 162, 51°, worden de akten, vonnissen en                         Sa arresten, betreffende een overeenkomstig Boek XX, Titel V van het                    d' Wetboek van economisch recht ingestelde procedure van                                19 gerechtelijke reorganisatie vrijgesteld van de registratierechten die                ac niet worden bedoeld in artikel 3 van de bijzondere wet van 16 januari                ju 1989 betreffende de financiering van de Gemeenschappen en de                         dr Gewesten.

### HOOFDSTUK VII - Vrijstelling van de formaliteit der registratie

###### Art. 162

(10°, opgeheven bij art. 4 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst   (1 van toepassing vanaf 02.09.2023 (art. -))                                        ap

Zijn onder het in artikel 163 aangewezen voorbehoud, van de                      So formaliteit der registratie vrijgesteld.                                         de

1° Akten, vonnissen en arresten in kieszaken;                                    1

2° Akten, vonnissen en arresten betreffende de uitvoering van                    2 wetten en reglementen op de militie, de vergoeding inzake militie en             rè de militaire opeishingen;                                                        ré

3° Akten, vonnissen en arresten betreffende de uitvoering der wetten             3 en reglementen inzake 's lands mobilisatie en de bescherming der                 rè bevolking in geval van oorlog, de burgerlijke opeischingen en vrijwillige        de dienstnemingen, alsmede de in vredestijd aangegane uitgestelde                   vo contracten;

4° Akten, vonnissen en arresten betreffende de uitvoering van                    4 wetten en reglementen inzake belastingen ten bate van de Staat,                  rè gefedereerde entiteiten, provincies, gemeenten, polders en                       fé wateringen;

5° Exploten en andere akten, in strafzaken opgemaakt ten verzoek                 5 van ambtenaren van het openbaar ministerie en van andere                         re ambtenaren of besturen waaraan de wet de vordering voor de                       ou toepassing der straffen opdraagt; bovenaan op bedoelde akten                     pe worden de woorden Pro Justitia aangebracht;

5°bis De akten waartoe de rechtsplegingen in burgerlijke zaken of                5° tuchtzaken aanleiding geven, wanneer het openbaar ministerie of de               ou vrederechter van ambtswege optreedt;                                             d’

6° (…)                                                                           6

6°bis Akten, vonnissen en arresten betreffende de uitvoering der wet             6° op eerherstel in strafzaken en deze betreffende de uitvoering der wet            la tot bescherming der maatschappij tegen de abnormalen en de                       lo gewoontemisdadigers;                                                             d’

7° Akten, vonnissen en arresten inzake onteigeningen ten algemenen            7 nutte en die welke betrekking hebben op de uitvoering van Titel I van         ca de wet houdende organisatie van de ruimtelijke ordening en van de             or stedenbouw, met uitzondering van de in artikel 161, 2°, bedoelde              l’e akten;

8° Akten, vonnissen en arresten betreffende ingebruikneming van               8 gronden door den Staat met het oog op de inrichting van 's Lands              pa verdediging;

9° Akten en vonnissen betreffende procedures vóór den                         9 onderzoeksraad voor de zeevaart;                                              d’

10° (…)                                                                       10

11° De akten, vonnissen en arresten inzake onttrekking van de zaak            11 aan de rechter, zoals bedoeld in het Gerechtelijk Wetboek, deel III, titel    de IV, hoofdstuk III;                                                            tit

12° De akten, vonnissen en arresten inzake wraking, zoals bedoeld in          12 het Gerechtelijk Wetboek, deel IV, boek II, titel III, hoofdstuk V;           ré ch

13° Akten en vonnissen betreffende procedures vóór vrederechters,             13 wanneer het bedrag van den hoofdeisch het maximum van den                     de laatsten aanleg niet te boven gaat, of wanneer het gaat om een                ta procedure      inzake    uitkering   tot    onderhoud      of     ingesteld   de overeenkomstig artikel 221 van het Burgerlijk Wetboek; Akten en               Co vonnissen            betreffende       procedures          vóór         de    tri ondernemingsrechtbanken, wanneer het geschillen geldt die gegrond             les zijn op de bepalingen van het Wetboek van bepaalde voorrechten op             di zeeschepen en diverse bepalingen of van de wet van 5 mei 1936 op              flu de rivierbevrachting, indien het bedrag van de hoofdeis het bedrag            de van de laatste aanleg vóór het vredegerecht niet te boven gaat;

13°bis De exploten van gerechtsdeurwaarders opgesteld ter                     13 vervanging van een gerechtsbrief in het geval bepaald in artikel 46, §        pl 3, van het Gerechtelijk Wetboek;

Bovenaan het exploot dient te worden vermeld dat het is opgesteld             L’e ter vervanging van een gerechtsbrief en zulks met vermelding van het          d’ artikel van het Gerechtelijk Wetboek op grond waarvan de betekening           la wordt gedaan;

14° Akten, vonnissen en arresten betreffende procedures ingesteld             14 bij de wetten van 10 Maart 1900 op de arbeidsovereenkomst, van 7              pa Augustus 1922 op de bediendenarbeidsovereenkomst en van 5 Juni                su 1928 houdende regeling van het arbeidscontract wegens                         co scheepsdienst, met betrekking tot de bekwaamheid van de                       d’

minderjarige om zijn arbeid te verhuren en zijn loon of bezoldiging te ontvangen;

15° Akten opgemaakt ten verzoeke van de ambtenaren van het               15 openbaar ministerie betreffende de uitvoering van rogatoire              re opdrachten die uitgaan van buitenlandse rechters;                        ét

16° (...)                                                                16

17° De akten, vonnissen en arresten betrekking hebbende op de            17 uitvoering van de wet betreffende het herstel van zekere schade          re veroorzaakt aan private goederen door natuurrampen;                      pr

18° De akten, vonnissen en arresten betreffende procedures               18 ingesteld bij de wet van 26 juni 1990 betreffende de bescherming van     pa de persoon van de geesteszieke en bij de artikelen de bepalingen van     m het vierde deel, boek IV, hoofdstuk X van het Gerechtelijk Wetboek.      IV

19° de akten, vonnissen en arresten betreffende procedures tot           19 machtiging ingesteld overeenkomstig artikel 4.40, § 3 van het            d'a Burgerlijk Wetboek;

20° (...)                                                                20

21° Voorzieningen in verbreking van het openbaar ministerie en           21 derzelver betekeningen;                                                  sig

22° (...)                                                                22

23° Akten opgemaakt alsmede vonnissen of arresten gewezen voor           23 de toepassing van de wetten op het gebruik van de talen in de            l’a gerechtszaken en in bestuurszaken;                                       ju

24° Akten betreffende de uitvoering van de bepalingen van het            24 Gerechtelijk Wetboek inzake de inruststelling der magistraten;           co

25° (...)                                                                25

26° (...)                                                                26

26°bis (...)                                                             26

27° (...)                                                                27

28° (...)                                                                28

29°     Getuigschriften,   akten   van   bekendheid,     volmachten,     29 machtigingen met inbegrip van de verzoekschriften die er zouden          au verband mede houden, wanneer die stukken opgemaakt of uitgereikt         ce worden om te worden overgelegd aan de diensten van het Grootboek         du

van de Rijksschuld aan de Deposito- en Consignatiekas, zomede aan       m de mutualiteitsverenigingen, spaar-, lijfrente-, voorzorgs- en          se onderstandskassen erkend door de regering, ingesteld met                l’a goedkeuring van de bestuursoverheid of aan dezer controle               ce onderworpen;

30° (...)                                                               30

31° (...)                                                               31

32° (...)                                                               32

33° Akten opgemaakt voor den dienst van de openbare kassen van          33 lening, met inbegrip van processen-verbaal van openbaren verkoop        y van in pand gegeven roerende voorwerpen;                                m

33°bis Akten, vonnissen en arresten betreffende betwistingen inzake     33 arbeidsovereenkomsten, leerovereenkomsten en overeenkomsten             m voor versnelde beroepsopleiding, betreffende betwistingen tussen        et werknemers naar aanleiding van het werk alsmede tussen personen         co die samen een beroep uitoefenen waarbij hoofdzakelijk handenarbeid      en wordt verricht en inzonderheid tussen een schipper ter visserij en de   ca schepelingen met wie hij geassocieerd is, betreffende betwistingen      pê van burgerlijke aard die het gevolg zijn van een overtreding van de     co wetten en verordeningen betreffende de arbeidsreglementering en         re de aangelegenheden onder de bevoegdheid van de arbeidsrechtbank;        la

34° Akten, vonnissen en arresten betrekkelijk de uitvoering van de      34 wetten en reglementen op de kinderbijslagen;                            rè

35° Akten, vonnissen en arresten betrekkelijk de uitvoering van de      35 wetten en reglementen op de verzekering tegen de geldelijke             rè gevolgen van ouderdom en vroegtijdige dood, op de verzekering           pr tegen de geldelijke gevolgen van ouderdom en vroegtijdige dood van      pr bedienden en op het pensioenstelsel der mijnwerkers;                    m

35°bis De akten, vonnissen en arresten in verband met de uitvoering     35 van de wetten en verordeningen betreffende het sociaal statuut der      rè zelfstandigen;

35°ter De akten, vonnissen en arresten betreffende de uitvoering van    35 de wetten en verordeningen betreffende de rust-, invaliditeits-, en     rè overlevingspensioenen ten laste van de Staat, de provincies, de         ch gemeenten, de openbare instellingen, de Nationale Maatschappij der      pu Belgische Spoorwegen of alle andere organismen of openbare              au diensten waarvan het personeel onderworpen is aan een bijzondere        un pensioenregeling getroffen bij of krachtens een wet;

35°quater De akten, vonnissen en arresten betreffende de uitvoering       35 van de wetten, decreten en verordeningen betreffende de rust-,            dé invaliditeits- en overlevingspensioenen van de leden van het              su beroepspersoneel der kaders in Afrika en der personeelsleden die zijn     du bedoeld in artikel 31, van het koninklijk besluit van 21 mei 1964 tot     po coördinatie van de wetten betreffende het personeel in Afrika;

36° Akten, vonnissen en arresten betreffende de uitvoering der            36 wetten en reglementen op het herstel van schade ten gevolge van           rè arbeidsongevallen, van ongevallen overkomen op weg naar of van            du den arbeid, of van beroepsziekten;                                        m

36°bis Akten, vonnissen en arresten betreffende betwistingen in           36 verband met de rechten en verplichtingen voortvloeiend uit de wet op      co de sociale reclassering van de minder-validen;                            re

36°ter Akten, vonnissen en arresten betreffende betwistingen in           36 verband      met   de   oprichting    en   de    inrichting   van    de   co ondernemingsraden, alsmede van de diensten en comités tot                 d’ veiligheid, hygiëne en verfraaiing der werkplaatsen, daarin begrepen      d’ de diensten en comités opgericht in mijnen, groeven en graverijen;        se

37° Akten, vonnissen en arresten betreffende de uitvoering der            37 wetten en reglementen op de onvrijwillige werkloosheid;                   rè

37°bis Akten, vonnissen en arresten betreffende de uitvoering der         37 wetten en reglementen in verband met de maatschappelijke                  rè zekerheid;

38° Akten en beslissingen betreffende het verzoek om rechtsbijstand       38 of de betwisting ervan; akten van schikking inzake uitkering tot          ou onderhoud verleden op het bureel van bijstand;                            ali

39° Akten, vonnissen en arresten betreffende de invordering van de        39 voorschotten van Rijkswege gedaan in uitvoering van de bepalingen         av van het Gerechtelijk Wetboek betreffende de gerechtelijke bijstand;       ju

40° Akten, vonnissen en arresten betreffende de uitvoering van de         40 wet van 27 juni 1969 betreffende het toekennen van                        ju tegemoetkomingen aan de minder-validen;

41° Akten nodig voor het huwelijk van personen wier onvermogen            41 blijkt uit een getuigschrift van den burgemeester van hun                 es verblijfplaats of van dezes gelastigde;                                   de

42° Akten, vonnissen en arresten betreffende procedures inzake de         42 voogdij van minderjarigen;                                                de

43° Akten betreffende de vrijwillige erkenning van een natuurlijk kind          43 of de ontvoogding, wanneer het onvermogen der kinderen en van hun               na ouders vastgesteld is overeenkomstig bovenstaand nr. 41°;                       pè

44° Akten, vonnissen en arresten betreffende de verklaringen van                44 nationaliteit of van keuze van vaderland, wanneer het onvermogen                na der belanghebbenden vastgesteld is overeenkomstig bovenstaand                   es nr. 41°;

45° De akten, vonnissen en arresten betreffende betwistingen in                 45 verband met een maatregel van sociale bescherming;                              co

46° De akten, vonnissen en arresten, betreffende de procedure van               46 collectieve schuldenregeling ingesteld overeenkomstig de artikelen              rè 1675/2 tot en met 1675/19 van het Gerechtelijk Wetboek;                         Co

46° (47°) (1) De overdrachten tussen de componenten van een                     46 politieke partij zoals die zijn bepaald bij artikel 1, 1°, tweede lid, van de   te wet van 4 juli 1989 betreffende de beperking en de controle van de              re verkiezingsuitgaven voor de verkiezingen van de federale Kamers, de             en financiering en de open boekhouding van de politieke partijen;                  fin

47° (48°) (2) De akten, vonnissen en arresten betreffende de                    47 tegemoetkomingen bedoeld in de wet van 21 februari 2003 tot                     pr oprichting van een Dienst voor alimentatievorderingen bij de FOD                ali Financiën;

47° (49°) (3) De akten, de vonnissen en arresten, betreffende het               47 toestaan van betalingsfaciliteiten inzake consumentenkrediet,                   fa ingesteld overeenkomstig de artikelen 1337bis tot en met 1337octies             co van het Gerechtelijk Wetboek;                                                   ju

48° (50°) De akten en vonnissen betreffende de procedures voor de               48 rechters voor de bescherming van de maatschappij en de                          ju strafuitvoeringsrechtbanken, alsook de arresten gewezen als gevolg              ain van een cassatieberoep tegen een beslissing van de rechter voor de              dé bescherming van de maatschappij of de kamer voor de bescherming                 so van de maatschappij;

51°    De    akten,    vonnissen      en   arresten     betreffende     een     51 overeenkomstig Boek XX, Titel V van het Wetboek van economisch                  ré recht ingestelde procedure van gerechtelijke organisatie, behalve:              du

a) de akten die tot bewijs strekken van een overeenkomst                        a) onderworpen aan een registratierecht bedoeld in artikel 3 van de                d' bijzondere wet van 16 januari 1989 betreffende de financiering van              re de Gemeenschappen en de Gewesten;

b) de in artikelen 146 en 147 bedoelde vonnissen en arresten;                   b)

52° De exploten en processen-verbaal van de gerechtsdeurwaarders                 52 in verband met de invordering van onbetwiste geldschulden bedoeld                re in de artikelen 1394/20 tot 1394/27 van het Gerechtelijk Wetboek.                13
----------                                                                       -- Nota:                                                                            No
(1) Aangezien door de wet van 05.07.1998 (B.S., 31.07.1998), eveneens een        (1 “46°” werd ingevoegd, zou het “46°” dat werd ingevoegd door de wet van           ins 19.11.1998 (B.S., 10.12.1998), in feite “47°” moeten zijn.
(2) Het “47°” ingevoegd bij art. 28, § 1 van de wet van 21.02.2003 zou het       (2 “48°” moeten zijn.
(3) Het “47°” ingevoegd bij art. 82 van de wet van 24.03.2003 zou het “49°”      (3 moeten zijn.

###### Art. 163

(gewijzigd bij art. 16 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van   (m toepassing vanaf 04.05.1965 (art. -))                                            ap

De bij voorgaand artikel ingevoerde vrijstelling is niet toepasselijk op         L’e de in dit artikel opgesomde akten, vonnissen en arresten, in zover zij           ac tot bewijs van een overeenkomst strekken voorzien in artikel 19, 2°.             où

Zij is niet van toepassing op andere dan gerechtelijke akten, in zover           El zij tot bewijs van een in artikel 19, 3° of 5°, bedoelde overeenkomst            da strekken.                                                                        ou

Tenzij er anders over beschikt wordt, is ze niet van toepassing op:              A

a) processen-verbaal van verkoop van in beslag genomen roerende of               a) onroerende goederen en alle nakomende handelingen welke derde                    to verkrijgers aanbelangen;

b) processen-verbaal van rangregeling en van verdeling bij aandelen.             b)

###### Art. 164

Zijn mede van de formaliteit der registratie vrijgesteld, de uitgiften,          So afschriften van en uittreksels uit akten welke geregistreerd werden of           ex die krachtens artikel 162 van de formaliteit zijn vrijgesteld.                   so

###### Art. 165

Indien een bij artikelen 162 en 164 van de formaliteit der registratie                 Si vrijgestelde akte of geschrift toch ter registratie wordt aangeboden,                  ar geeft zij aanleiding tot het heffen van het algemeen vast recht.                       do

### HOOFDSTUK VIII - Diverse bepalingen betreffende de vereffening van de rechten en de betaling van het verschuldigde bedrag

(vervangen bij art. 6 van de wet van 26.05.2016 (B.S., 09.06.2016). Tekst van          (re toepassing vanaf 01.01.2015 (art. 8))                                                  ap

###### Art. 166

(gewijzigd bij art. 5, § 7, 1° van het KB van 20.07.2000 (B.S., 30.08.2000 - ed. 1).   (m Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42, 3°    Te van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1) err. (B.S., 21.12.2001).          42 Tekst van toepassing vanaf 01.01.2002 (art. 45, § 1))                                  Te

In geval van openbare verkoping van roerende of onroerende                             En goederen of van openbare verhuring, in verschillende loten, wordt het                  pu recht vereffend op het samengevoegd bedrag der aan hetzelfde tarief                    de onderworpen loten.

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de                       Le hogere eurocent afgerond.                                                              su

###### Art. 167

Wanneer er niet anderszins bij deze titel over beschikt is, mag het                    Lo bedrag van het op een akte of een verklaring te heffen evenredig recht                 m niet minder dan in het algemeen vast recht bedragen.                                   dé

###### Art. 168

(gewijzigd bij art. 17 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van         (m toepassing vanaf 04.05.1965 (art. -))                                                  ap

Wanneer de sommen en waarden of andere ter vereffening van de                          Lo belasting noodzakelijke gegevens niet voldoende uitgedrukt zijn in                     liq een ter formaliteit aangeboden akte, zijn de partijen of de werkende                   ac openbare officier, in hun naam, er toe gehouden daarin, vóór de                        in un

registratie, te voorzien door een aanvullende verklaring, gewaarmerkt en ondertekend onderaan de akte.

Wanneer een zelfde overeenkomst meteen op in België gelegen                      Lo onroerende goederen en op andere goederen slaat, moet de                         en overeengekomen         waarde      of,   in    voorkomend       geval,    de     éc verkoopwaarde van de goederen van elkeen der categorieën, zelfs                  m indien het tarief van de belasting niet verschilt naar gelang van de aard        in van de goederen, afzonderlijk aangeduid worden, hetzij in de akte,               ce hetzij in een door de partijen of, in hun naam, door de werkende                 pa notaris vóór de registratie gewaarmerkte en ondertekende verklaring onderaan op de akte.

Indien de bepaling van den belastbaren grondslag geheel of                       Si gedeeltelijk van de schatting van een levenslang recht afhangt, moet             de de verklaring naam, voornamen, woonplaats, plaats en datum van                   no geboorte van de beneficianten van dit levenslang recht vervatten.                bé

###### Art. 169

Ar

De rechten verschuldigd op akten waarbij eigendom of vruchtgebruik               Le van een handelszaak overgedragen of aangewezen worden, worden                    d’ geheven volgens de aard van elk der goederen die er deel van                     ch uitmaken en op de bij dit wetboek vastgestelde grondslagen.                      pr

De schulden die al dan niet met de handelszaak in verband staan en               Le die door den nieuwe eigenaar of vruchtgebruiker ten laste genomen                en worden, moeten als lasten van de overeenkomst beschouwd worden.                  co

###### Art. 169bis

(ingevoegd bij art. 70 van de wet van 22.12.1998 (B.S., 15.01.1999). Tekst van   (in toepassing vanaf 25.01.1999 (art. -))                                            àp

Voor de toepassing van de artikelen 115bis en 140bis, moet de                    Po aanwending of de bestemming van een onroerend goed worden                        de nagegaan per kadastraal perceel of per gedeelte van kadastraal                   pa perceel wanneer dat gedeelte is ofwel een afzonderlijke huisvesting,             lo ofwel een afdeling van de productie of van de werkzaamheden die, of              ou een onderdeel daarvan dat, afzonderlijk kan werken, ofwel een                    di eenheid die van de andere goederen of delen die het perceel vormen kan worden afgezonderd.

###### Art. 169ter

(gewijzigd bij art. 2 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van          (m toepassing vanaf 01.12.2021 (art. 7))                                                  àp

De rechten en, in voorkomend geval, de boeten en de interesten, zoals                  Le zij door het in artikel 39 bedoelde kantoor zijn vastgesteld, worden                   so voorafgaandelijk aan de registratie betaald.                                           pr

Behalve wanneer ze verschuldigd zijn in het kader van de                               Sa registratierechten die, krachtens artikel 3, eerste lid, 6° tot 8°, van de             ve bijzondere wet van 16 januari 1989 betreffende de financiering van                     19 de gemeenschappen en de gewesten, worden aangemerkt als                                co gewestelijke belastingen, kan de Koning, bij een besluit vastgesteld na                ar overleg in de Ministerraad, in afwijking van het eerste lid bepalen dat                1e de rechten, boeten en interesten die verschuldigd zijn op de door Hem                  d’ aangewezen categorieën van akten, kunnen of moeten worden                              l’e betaald na de registratie. In voorkomend geval bepaalt hij de termijn                  pa en de nadere regels van de betaling.

Niemand kan, onder voorwendsel van betwisting van het                                  Nu verschuldigde bedrag of om enige andere reden, die betaling                            co verminderen of uitstellen, behoudens het recht om teruggave te                         po vorderen, indien daartoe grond bestaat.

### HOOFDSTUK IX - Verplichtingen met het oog op het                                     Ch verzekeren van het heffen van de rechten

#### Afdeling I - Vermeldingen op te nemen in bepaalde akten

###### Art. 170

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Wanneer, in een ander dan een vonnis of arrest aan de formaliteit                      Lo onderworpen authentieke akte, melding wordt gemaakt van een                            ét onderhandsche akte of van een buitenslands verleden akte vallende                      ac in de termen van artikel 19, 2° of 3°, moet die authentieke akte                       fo afschrift van de vermelding der registratie van bedoelde akte                          l’e bevatten.

Indien die akte niet geregistreerd werd, dan wordt daarvan in de                       Si authentieke akte melding gemaakt.                                                      au

Alle overtreding van dit artikel wordt gestraft met een boete van 25                   To EUR ten laste van den werkenden ambtenaar of openbaren officier.                       EU

###### Art. 170bis

(ingevoegd bij art. 6 van de wet van 07.03.2002 (B.S., 19.03.2002). Tekst van          (in toepassing vanaf 01.01.2002 (art. 7))                                                  àp

In geval van een schenking moet de notaris in de akte een verklaring                   En van de schenker opnemen die vermelding inhoudt van het adres en                        dé de datum en duur van de vestiging van de verschillende fiscale                         d' woonplaatsen die de schenker gehad heeft in de periode van vijf jaar                   fis voorafgaand van de datum van de schenking.                                             la

In geval van weigering de verklaring te doen of bij onjuiste of                        En onvolledige verklaring verbeurt de schenker een boete ten bijdrage                     le van tweemaal de aanvullende rechten.                                                   co

De notaris die nagelaten heeft de schenker te vragen de verklaring te                  Le doen, verbeurt een boete van 25 EUR.                                                   en

###### Art. 171

(aangevuld bij art. 112 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).          (co Tekst van toepassing vanaf 17.08.2020 (art. -))                                        Te

Alle expedities, afschriften van of uittreksels uit een burgerlijke of                 To gerechtelijke authentieke akte die aan de formaliteit onderworpen is                   ju of die in artikel 8bis bedoeld is, moeten, op straf van een boete van 25               l'a EUR, een afschrift van de vermelding van de registratie of van de                      co vermelding voorzien in het tweede lid van artikel 8 bevatten.                          de

Het eerste lid is niet van toepassing op een afschrift gemaakt met het                 L'a oog op de aanbieding ervan ter formaliteit van de registratie.                         pr

#### Afdeling II - Voorschriften betreffende het uitreiken van uitgiften

###### Art. 172

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te

5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing   42 vanaf 01.01.2002 (art. 45, § 1))                                                pa

Notarissen,      gerechtsdeurwaarders,           griffiers   der   hoven   en   No rechtbanken en bestuurlijke overheden mogen; vóór het nakomen                   au van de formaliteit der registratie, de akten welke zij verplicht zijn te        fo doen registreren of waarvan de rechten in hun handen moeten                     ex worden geconsigneerd, niet in brevet, uitgifte, afschrift of uittreksel         dr uitreiken, zelfs zo de voor de registratie gestelde termijn niet                l'e verstreken is.

Alle overtreding van dit verbod wordt met een geldboete van 25 EUR              To gestraft.                                                                       EU

###### Art. 173

(7°bis, ingevoegd bij art. 113 van de wet van 31.07.2020 (B.S., 07.08.2020 -    (7 ed. 1). Tekst van toepassing vanaf 17.08.2020 (art. -))                         Te

Van voorgaand artikel wordt afgeweken ten aanzien van:                          Il e

1° De uitgiften van akten, verleden voor notarissen of bestuurlijke             1 overheden, die aanleiding geven tot een hypothecaire formaliteit                ad waarbij de bedoelde uitgiften eerst aan de betrokken partijen mogen             ex worden afgegeven nadat zij, overeenkomstig artikel 171 zijn                     av aangevuld, met een afschrift van de vermelding van de registratie of            la met de in artikel 8, tweede lid, voorgeschreven vermelding;                     ali

1°bis De uitgiften en uittreksel van akten, verleden voor notarissen,           1° die aanleiding geven tot neerlegging ter griffie van de                         qu ondernemingsrechtbank overeenkomstig artikel 2:12 van het                       co Wetboek van vennootschappen en verenigingen;                                    as

1°ter de uitgiften en uittreksels van akten, verleden voor notarissen,          1° die worden uitgereikt met als enig doel de inschrijving van een                 so onderneming bij een ondernemingsloket, op voorwaarde dat dit                    au uitdrukkelijk vermeld wordt op de uitgifte of het uittreksel;                   ex

2° Afschriften welke vereist zijn voor de betekening van exploten en            2 van andere soortgelijke akten;                                                  de

3° Niet ondertekende afschriften van vonnissen en arresten;                     3

4° Vonnissen en arresten die, met het oog op de dringende                       4 noodzakelijkheid, op de minuut en vóór de registratie uitvoerbaar               su verklaard worden;

5° Voor eensluidend verklaarde afschriften van vonnissen en                       5 arresten slechts afgeleverd ten einde de verhaalstermijnen te doen                à lopen. Die afschriften moeten vermelding van hun bijzondere                       po bestemming dragen en mogen tot geen andere doeleinden worden                      d’ gebruikt;

6° Uitgiften van vonnissen en arresten die worden uitgereikt aan het              6 openbaar ministerie, alsmede uitgiften, afschriften of uittreksels die            pu in strafzaken worden uitgereikt aan de Rijksagenten welke belast zijn             dé met de tenuitvoerlegging van vonnissen en arresten;                               ar

7° Afschriften waarvan de aflevering wegens hoogdringendheid                      7° werd bevolen door de voorzitter van de rechtbank van eerste aanleg;               tri

7°bis de afschriften van de vonnissen en arresten gemaakt met het                 7° oog op de aanbieding ervan ter formaliteit van de registratie;                    pr

8° de gedematerialiseerde afschriften van notariële akten, die                    8° worden neergelegd in de Notariële Aktebank overeenkomstig artikel                 Ba 18 van de wet van 25 ventôse jaar XI op het notarisambt.                          ve

###### Art. 174

(opgeheven bij art. 13 van de wet van 19.06.1986 (B.S., 24.07.1986). Tekst        (ab van toepassing vanaf 01.11.1986 (art. 15))                                        ap

(…)                                                                               (…

###### Art. 175

(opgeheven bij art. 17 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst        (ab van toepassing vanaf 01.01.1961 (art. 39))                                        ap

(…)                                                                               (…

#### Afdeling III - Repertorium van de akten

###### Art. 176

(gewijzigd bij art. 48, § 4 van de wet van 05.07.1963 (B.S., 17.07.1963). Tekst   (m van toepassing vanaf 28.09.1963 (art. 52))                                        ap

Notarissen en gerechtsdeurwaarders moeten een kolomsgewijze                            Le ingedeeld repertorium houden, waarin zij dagelijks zonder openlaten                    co van tussenruimte, noch tussenregel, noch vervalsing en in de                           in volgorde der nummers, alle akten van hun ambt inschrijven.                             m

###### Art. 177

(gewijzigd bij art. 53 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).           (m Tekst van toepassing vanaf 10.01.2014 (art. 87, 1°))                                   ap

In elk artikel van het repertorium dienen vermeld:                                     Ch

1° volgnummer;                                                                         1

2° datum en aard van de akte;                                                          2

3° naam, voornamen, woonplaats en identificatienummer of                               3 ondernemingsnummer bedoeld in artikel 2, vierde lid, van de partijen;                  d'

4° bondige aanduiding der onroerende goederen;                                         4

5° vermelding van de registratie;                                                      5

6° wat aangaat de gerechtsdeurwaarders, de kosten van hun akten                        6 en exploten na aftrek van hun verschotten.                                             ex

De Koning kan aanvullende vermeldingen voorschrijven of                                Le afwijkingen toestaan.                                                                  dé

###### Art. 178

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Een boete van 25 EUR wordt verbeurd voor elke weggelaten of te laat                    Il e in het repertorium ingeschreven akte, voor elke akte ingeschreven                      ta met tussenregel of met vervalsing, alsmede voor elke akte van                          ou vroegere datum dan die van het proces-verbaal van nummering en                         pr waarmerk van het repertorium.

###### Art. 179

(vervangen bij art. 82 van de wet van 22.12.2009 (B.S., 31.12.2009 - ed. 2).        (re Tekst van toepassing vanaf 10.01.2010 (art. -))                                     ap

De in artikel 176 bedoelde repertoria die moeten worden gehouden                    Le door de notarissen, mogen overeenkomstig artikel 29 van de wet van                  pe 16 maart 1803 tot regeling van het notarisambt hetzij op papier, hetzij             po op een gedematerialiseerde wijze die is vastgesteld door de Nationale               m Kamer van notarissen in een door de Koning goedgekeurd reglement,                   de worden gehouden.

De Koning kan bepalen dat de repertoria die door de                                 Le gerechtsdeurwaarders moeten worden gehouden, mogen worden                           do gehouden op een gedematerialiseerde wijze die vastgesteld is door                   dé de Nationale Kamer van gerechtsdeurwaarders in een door de Koning                   rè goedgekeurd reglement.

###### Art. 180

(gewijzigd bij art. 54 van de wet van 21.12.2013 (B.S., 31.12.2013 - ed. 2).        (m Tekst van toepassing vanaf 01.04.2014 (art. 87, 3°))                                ap

De in artikel 176 aangeduide personen zijn er toe gehouden, om de                   Le drie maand, hun repertorium voor te leggen aan de ontvanger van het                 to kantoor aangeduid in artikel 39, 1°, eerste lid, die het viseert en in zijn         l’a visum het aantal ingeschreven akten vermeldt.                                       d’

Deze voorlegging geschiedt binnen de eerste tien dagen van de                       Ce maanden januari, april, juli en oktober van elk jaar.                               jan

De Koning kan voor de op gedematerialiseerde wijze gehouden                         Po repertoria bijzondere regels vaststellen wat de modaliteiten van de                 ét voorlegging en het visum van het repertorium betreft.                               pr

Bij laattijdige voorlegging van het repertorium wordt een boete                     Un verbeurd van 25 euro per week vertraging.                                           de

###### Art. 180bis

(lid 1, gewijzigd bij art. 24 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst   (al van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                   (M

Een kopie van de geregistreerde uitgifte en van de geregistreerde                   Le bijlagen wordt, samen met de vermelding van de registratie,                         re gedurende twintig jaar bewaard door de instrumenterende notaris.                    de

Indien de akte op gedematerialiseerde wijze ter registratie                      Si aangeboden werd, gebeurt deze bewaring door de Koninklijke                       ce Federatie van het Belgisch Notariaat of haar gedelegeerde, voor                  Fé rekening van de notaris.

Die bewaring geschiedt:                                                          Ce

1° voor de akten die zijn opgenomen in de Notariële Aktebank,                    1° bedoeld in artikel 18 van de wet van 25 ventôse jaar XI op het                   no notarisambt, door die Notariële Aktebank;                                        or

2° voor de andere akten, door de Koninklijke Federatie van het                   2° Belgisch Notariaat of haar gedelegeerde, op elektronische wijze, voor            so rekening van de notaris.

De bewaring moet de onveranderlijkheid en de integriteit van de                  La inhoud van deze stukken waarborgen.                                              pi

###### Art. 180ter

(ingevoegd bij art. 114 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).    (in Tekst van toepassing vanaf 17.08.2020 (art. -))                                  ap

De griffier bewaart, samen met de minuut van het vonnis of arrest:               Le

1° de vermelding van de registratie van dat vonnis of arrest;                    1°

2° een kopie van het geregistreerde afschrift van dat vonnis of arrest.          2°

#### Afdeling IV - Verplichting van inzageverlening

###### Art. 1811

(gewijzigd bij art. 55 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (se toepassing vanaf 16.05.2016 (art. -))                                            (M

Notarissen,      gerechtsdeurwaarders,            bestuursoverheden       en     Le ambtenaren van de Staat, provincies, gemeenten en openbare                       les instellingen zijn ertoe gehouden, op verbeurte van een boete van 25              ét EUR per overtreding, op elk verzoek van de ambtenaren van de                     EU Algemene Administratie van de Patrimoniumdocumentatie, van hun                   ré repertoriums en de akten waarvan zij bewaarders zijn, evenals van de             do uitgiften en relazen bedoeld in artikel 180bis, zonder verplaatsing              so inzage te verlenen en deze ambtenaren de inlichtingen, af schriften en           l'a et

uittreksels te laten nemen die zij nodig hebben met het oog op 's Rijks belangen.

Deze verplichting is echter, bij 't leven van de erflaters, niet                 To toepasselijk op de bij notarissen berustende testamenten.                        au

###### Art. 1812

(gewijzigd bij art. 115 van de wet van 31.07.2020 (B.S., 07.08.2020 - ed. 1).    (m Tekst van toepassing vanaf 17.08.2020 (art. -))                                  ap

De griffiers van de hoven en rechtbanken zijn er toe gehouden op straf           Le van een boete van vijfentwintig euro per overtreding, aan de                     am ambtenaren       van     de     Algemene          Administratie   van     de     ag Patrimoniumdocumentatie inzage te verlenen van:                                  pa

1° de door hen of vóór hen verleden akten;                                       1°

2° de minuten van de vonnissen, arresten, bevelschriften en alle                 2° andere akten waarvan zij bewaarders zijn;                                        ac

3° de afschriften en vermeldingen bedoeld in artikel 180ter.                     3°

De modaliteiten waaronder deze inzage moet verleend worden en de                 Le termijn waarbinnen dit moet geschieden, worden bij koninklijk besluit            av bepaald. Inbreuken op de voorschriften van dit koninklijk besluit                du kunnen beteugeld worden met boeten waarvan het bedrag 25 EUR                     ta per inbreuk niet zal te boven gaan.

###### Art. 182

(gewijzigd bij art. 57 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (m toepassing vanaf 16.05.2016 (art. -))                                            ap

De personen die de in artikel 631 bedoelde beroepsaangifte                       Le ondertekenen zijn ertoe gehouden van hun registers, repertoria,                  l’a boeken, akten en alle andere bescheiden betreffende hun handels-,                ré beroeps- of statutaire bedrijvigheid, bij iedere vordering van de                do ambtenaren       van     de     Algemene          Administratie    van     de    et Patrimoniumdocumentatie, zonder verplaatsing inzage te verlenen,                 pr ten einde bedoelde ambtenaren te laten nagaan of de door hen of                  de door derden verschuldigde registratierechten wel richting werden                 de geheven.

Elke weigering van inzageverlening wordt bij proces-verbaal                      To vastgesteld en gestraft met een geldboete van 250 tot 2.500 EUR,                 d’

waarvan het bedrag door de bevoegde adviseur-generaal van de                          co Algemene Administratie van de Patrimoniumdocumentatie wordt                           do bepaald.

###### Art. 182bis

(gewijzigd bij art. 66 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van        (m toepassing vanaf 16.05.2014 (art. 99))                                                ap

De personen die de toepassing van artikel 140bis vragen, zijn er toe                  Le gehouden, zonder verplaatsing, van alle boeken en bescheiden                          te betreffende hun activiteit bij iedere vordering van de ambtenaren van                 ag de Algemene Administratie van de Patrimoniumdocumentatie inzage                       to te verlenen teneinde bedoelde ambtenaren toe te laten zich te                         ag vergewissen van de juiste heffing van de door de verzoekers of                        du derden verschuldigde rechten.

Elke weigering van inzageverlening wordt bij proces-verbaal                           To vastgesteld en wordt gestraft met een geldboete van 1.250 EUR.                        pu

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 183

(gewijzigd bij art. 67 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (al van toepassing voor alle of bepaalde categorieën van houders van een                  Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Openbare instellingen, stichtingen van openbaar nut en private                        Le stichtingen, alle verenigingen en vennootschappen die in België hun                   fo hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben,             le bankiers,       wisselagenten          en        wisselagentcorrespondenten,          d’ zaakwaarnemers en aannemers, openbare of ministeriële officieren                      co zijn ertoe gehouden aan de ambtenaren van de Algemene                                 pu Administratie        van       de      Patrimoniumdocumentatie,               met     l’A desvoorkomend inzageverlening van de stukken tot staving, al de                       co inlichtingen te verstrekken welke deze nodig achten om de correcte                    re heffing van de te hunnen laste of ten laste van derden invorderbare                   ju rechten te verzekeren.                                                                tie

Deze inlichtingen kunnen slechts gevraagd worden krachtens                            Ce bijzondere machtiging van de administrateur-generaal van de                           au Algemene       Administratie        van     de    Patrimoniumdocumentatie,            gé houdende nauwkeurige aanduiding van het rechtsfeit omtrent                            pr hetwelk navorsing dient gedaan.                                                       po

De inlichtingen moeten worden verschaft binnen drie maanden na de                Le datum waarop ze werden gevraagd. Die termijn kan worden verlengd                 co door de ambtenaar aangewezen in de machtiging bedoeld in het                     fo tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500                 Il EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de                2.
Algemene Administratie van de Patrimoniumdocumentatie wordt                      co vastgesteld.                                                                     pa

###### Art. 183

(gewijzigd bij art. 58 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (m toepassing vanaf 16.05.2016 (art. -))                                            ap

Openbare instellingen, stichtingen van openbaar nut en private                   Le stichtingen, alle verenigingen en vennootschappen die in België hun              fo hoofdinrichting, een filiale of enigerlei zetel van verrichtingen hebben,        le bankiers,      wisselagenten         en        wisselagentcorrespondenten,       d’ zaakwaarnemers en aannemers, openbare of ministeriële officieren                 co zijn ertoe gehouden aan de ambtenaren van de Algemene                            pu Administratie       van      de      Patrimoniumdocumentatie,            met     l’A desvoorkomend inzageverlening van de stukken tot staving, al de                  co inlichtingen te verstrekken welke deze van node achten om de                     re richtige heffing van de te hunnen laste of ten laste van derden                  ju invorderbare rechten te verzekeren.                                              tie

Deze inlichtingen kunnen slechts gevraagd worden krachtens                       Ce bijzondere machtiging van den administrateur-generaal van de                     au Algemene       Administratie      van     de    Patrimoniumdocumentatie,         gé houdende nauwkeurige aanduiding van het rechtsfeit omtrent                       pr hetwelk navorsing dient gedaan.                                                  po

De inlichtingen moeten worden verschaft binnen drie maanden na de                Le datum waarop ze werden gevraagd. Die termijn kan worden verlengd                 co door de ambtenaar aangewezen in de machtiging bedoeld in het                     fo tweede lid.

Voor elke overtreding wordt een boete verbeurd van 250 tot 2.500                 Il EUR, waarvan het bedrag door de bevoegde adviseur-generaal van de                2.
Algemene Administratie van de Patrimoniumdocumentatie wordt                      co vastgesteld.                                                                     pa -- No (1

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 184

(lid 2, vervangen bij art. 68 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Wanneer de som te betalen door de eigenaar van een muur om deze                       Lo gemeen te maken, door tussenkomst van een deskundige,                                 ce bouwkundige, aannemer, landmeter of landmeetkundige werd                              en bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25                    d’ EUR, de bevoegde ambtenaar van de Algemene Administratie van de                       l’a Patrimoniumdocumentatie daarvan bericht te geven binnen de drie                       l’A maanden na de voltooiing van zijn werk.

De Koning bepaalt de modaliteiten van deze communicatie en duidt                      Le de ambtenaar aan ertoe bevoegd hetzelve te ontvangen.                                 fo

###### Art. 184

(gewijzigd bij art. 68 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van        (m toepassing vanaf 16.05.2014 (art. 99))                                                ap

Wanneer de som te betalen door de eigenaar van een muur om deze                       Lo gemeen te maken, door tussenkomst van een deskundige,                                 ce bouwkundige, aannemer, landmeter of landmeetkundige werd                              en bepaald, is deze ertoe gehouden, op verbeurte van een boete van 25                    d’ EUR, de bevoegde ambtenaar van de Algemene Administratie van de                       l’a Patrimoniumdocumentatie daarvan bericht te geven binnen de drie                       l’A maanden na de voltooiing van zijn werk.

Een koninklijk besluit bepaalt de wijze waarop dit bericht dient                      Un gegeven en duidt de ambtenaar aan ertoe bevoegd hetzelve te                           do ontvangen.                                                                            re

#### Afdeling V - Verplichtingen opgelegd aan openbare

ambtenaren ter verzekering van de invordering der registratierechten

###### Art. 184bis

(gewijzigd bij art. 93 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).          (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                       ap

De notarissen, gerechtsdeurwaarders en griffiers, de vereffenaars en                  Le curatoren alsook de ambtenaren van de Deposito- en Consignatiekas                     les mogen slechts de betaling, overschrijving of teruggave van sommen                     co of waarden die voortkomen van een veroordeling, van een                               re vereffening of van een rangregeling, verrichten na de aflevering, door                liq de ontvanger, van een getuigschrift houdende verklaring dat geen                      ce enkele som eisbaar blijft als registratierecht of als boete uit hoofde                dr van die veroordeling, vereffening of rangregeling.                                    liq

Het eerste lid is slechts van toepassing op de vereffenaars en de                     L'a curators in het geval dat de veroordeling, de vereffening of                          da rangregeling die de betaling, overschrijving, of teruggave tot gevolg                 ré heeft, hen ter kennis wordt gebracht.                                                 va

Indien de personen bepaald in het eerste lid de voorschriften van dit                 Da artikel niet zijn nagekomen, zijn zij persoonlijk aansprakelijk voor de               re betaling van de sommen die opeisbaar blijven.                                         pe ex

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Art. 185

(lid 2, vervangen bij art. 69 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze                    In titel, wordt het bestuur er toe gemachtigd volgens de regelen en door                 sp alle middelen van gemeen recht, met inbegrip van getuigen en                          au vermoedens, maar met uitzondering van de eed, en, bovendien door                      co de processen-verbaal van zijn ambtenaren, elke overtreding van de                     se beschikkingen van deze titel vast te stellen en om het even welk feit                 co te bewijzen dat de opvorderbaarheid van een recht of een boete laat                   qu blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.                   am

De processen-verbaal gelden als bewijs tot het tegendeel bewezen is.             Le Zij zullen aan belanghebbenden betekend worden binnen de maand                   no van de vaststelling van de overtreding. Deze betekening gebeurt met              co een aangetekende zending.

### HOOFDSTUK X - Bewijsmiddelen

#### Afdeling I - Algemene bepalingen

###### Art. 185

(gewijzigd bij art. 59 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (m toepassing vanaf 16.05.2016 (art. -))                                            06

Behoudens de bewijs- en controlemiddelen speciaal voorzien in deze               In titel, wordt het bestuur er toe gemachtigd volgens de regelen en door            sp alle middelen van gemeen recht, met inbegrip van getuigen en                     au vermoedens, maar met uitzondering van de eed, en, bovendien door                 co de processen-verbaal van zijn ambtenaren, elke overtreding van de                se beschikkingen van deze titel vast te stellen en om het even welk feit            co te bewijzen dat de opvorderbaarheid van een recht of een boete laat              qu blijken of er toe bijdraagt deze opvorderbaarheid te laten blijken.              am

De processen-verbaal gelden als bewijs tot het tegendeel bewezen is.             Le Zij zullen aan belanghebbenden betekend worden binnen de maand                   no van de vaststelling van de overtreding. Deze betekening mag                      co gebeuren bij een ter post aangetekend schrijven. De afgifte van het              re stuk ter post geldt als betekening van de volgende dag af.                       co

###### Art. 186

(opnieuw opgeheven bij art. 11 van de wet van 13.08.1947 (B.S., 17.09.1947).     (à Tekst van toepassing vanaf 27.09.1947 (art. -))                                  Te

(…)                                                                              (…

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989        Di betreffende de financiering van de gemeenschappen en de gewesten)                re

###### Art. 187

Verandering in eigendom of vruchtgebruik van een in België gelegen             Le onroerend goed, ten gevolge van een overdragende of aanwijzende                Be overeenkomst, wordt, ter vordering van het recht tegen de nieuwe               su eigenaar of vruchtgebruiker, in voldoende mate bewezen door daden              pr van beschikking of van bestuur of door andere handelingen of akten             d’ waarbij, in zijnen hoofde, de eigendom of het vruchtgebruik                    ch vastgesteld of ondersteld wordt.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989      Di betreffende de financiering van de gemeenschappen en de gewesten)              re

###### Art. 188

Wordt als koper voor eigen rekening beschouwd en mag zich op de                Es hoedanigheid van lasthebber of van commissionair van de verkoper               pe niet beroepen, ieder persoon die de verkoop van een onroerend goed             ve bewerkt, wanneer vaststaat dat hij, reeds vóór het tot stand brengen           es van deze verkoop, aan de eigenaar den prijs of elke van den verkoop            s’e voort te komen som betaald heeft of er zich toe verbonden heeft te             pr betalen.

De tussenpersoon wordt geacht het onroerend goed te hebben                     L’i verkregen op de dag van de betaling of van de verbintenis tot betaling.        pa

#### Afdeling II - Controleschatting

###### Art. 189

(gewijzigd bij art. 94 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).   (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                ap

Onverminderd de toepassing van de bepalingen betreffende het                   Sa bewimpelen van prijs, heeft de ontvanger de bevoegdheid om                     di schatting te vorderen van de goederen die het voorwerp van de                  de overeenkomst uitmaken, ten einde van de ontoereikendheid van de                l’in uitgedrukte prijs of van de aangegeven waarde te doen blijken,                 la wanneer het gaat om eigendom of vruchtgebruik van in België gelegen onroerende goederen.

###### Art. 190

(lid 3, opgeheven bij art. 3 van de wet van 22.06.1960 (B.S., 21.07.1960). Tekst   (al van toepassing vanaf 31.07.1960 (art. -))                                          ap

De schatting dient gevorderd bij een aanvraag genotificeerd door den               L’e ontvanger aan de verkrijgende partij binnen twee jaar te rekenen van               àl de dag van de registratie van de akte of verklaring.                               l’e

In de gevallen bedoeld in artikelen 16 en 17 gaat de termijn slechts in            Da den dag der registratie van de in artikel 31, 2°, voorziene verklaring.            du

De vordering tot schatting houdt aanwijzing van de goederen                        La waarover de schatting gaat, zomede van de som waarop zij door het                  et bestuur geschat werden en van het vermoedelijk wegens recht en                     pr boete verschuldigd bedrag.

###### Art. 191

Binnen vijftien dagen na de in artikel 190 voorziene notificatie, kunnen           Da ontvanger en partij overeenkomen dat de waardering door één of                     re door drie door hen gekozen deskundigen zal worden gedaan.                          pa

In dit geval wordt het akkoord vastgesteld bij een proces-verbaal dat              Da het voorwerp der schatting vermeldt en den of de verkozen                          l’o deskundigen aanwijst.

Dit proces-verbaal is gedagtekend; het wordt door de ontvanger en                  Ce door de partij ondertekend; indien de partij niet mag of niet kan                  si ondertekenen, dient dit in het proces-verbaal vermeld.                             ve

###### Art. 192

Bij gemis van het onder artikel 191 voorzien akkoord richt de                      A ontvanger, aan den vrederechter in wiens ambtsgebied de                            de onroerende goederen gelegen zijn, een verzoekschrift waarin de                     ex feiten worden uiteengezet en dat de vordering tot schatting inhoudt.               im Wanneer de onroerende goederen in het ambtsgebied van                              ju verschillende vredegerechten gelegen zijn, is de bevoegde rechter hij              bi in wiens ambtsgebied zich het gedeelte der goederen bevindt met het grootste kadastraal inkomen.

Het verzoekschrift wordt aan de partij betekend.                                   La

De rechter beslist binnen vijftien dagen na het verzoek; hij beveelt de            Le schatting en stelt, naar vereiste van omstandigheden, een of drie                  l’e deskundigen aan.                                                                   ex

###### Art. 193

(gewijzigd bij art. 69 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van   (m toepassing vanaf 16.05.2014 (art. 99))                                           ap

Kunnen niet tot deskundigen gekozen of benoemd worden:                           Ne

1° ambtenaren         van    de    Algemene      Administratie     van    de     1 Patrimoniumdocumentatie;                                                         do

2° openbare of ministeriële officieren opstellers van de akten of                2 verklaringen;                                                                    dé

3° beambten van bedoelde ambtenaren en openbare of ministeriële                  3 officieren.                                                                      m

###### Art. 194

(gewijzigd bij art. 3/art. 119 van de wet van 10.10.1967 (B.S., 31.10.1967).     (m Tekst van toepassing vanaf 01.01.1969 (art. 1, KB 04.11.1968 (B.S.,              ap 13.11.1968)))

Het vonnis waarbij de schatting wordt bevolen, wordt ten verzoeke                Le van de ontvanger aan de partij betekend.                                         du

De ontvanger of de partij, indien zij gegronde redenen hebben om de              Le bevoegdheid, onafhankelijkheid of onpartijdigheid van de benoemde                la deskundigen in twijfel te trekken, mogen, binnen acht dagen na                   pe bedoelde betekening, deszelfs of derzelver wraking bij de rechter                ré vorderen. Deze wraking mag altijd worden gevorderd in de gevallen                vis beoogd door artikel 966 van het Gerechtelijk Wetboek.

De vordering tot wraking geschiedt per rekest waarin de oorzaken der             La wraking nader worden bepaald. De rechter beslist na de                           de belanghebbenden te hebben gehoord. Bij hetzelfde vonnis vervangt                 le hij de gewraakte deskundigen.

Deze nieuwe beslissing wordt aan de partij betekend.                             Ce

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 195

(gewijzigd bij art. 70 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (m van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De ontvanger notificeert aan de deskundigen de opdracht die hun                       Le toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de                              Au deskundigen, zowel aan de ontvanger als aan de partij, een                            ta briefwisseling waarbij zij hen verwittigen van dag en uur waarop zij de               pr nodig geachte bezoeken ter plaatse zullen doen en hen in hun                          de gezegden en opmerkingen zullen aanhoren.                                              ob

Ieder aan de deskundigen door een der partijen ter inzage verleend                    To bescheid moet tezelfdertijd in afschrift aan de andere partij bij                     m aangetekende zending worden gezonden.                                                 en

###### Art. 195

De ontvanger notificeert aan de deskundigen de opdracht die hun                       Le toevertrouwd wordt.

Onmiddellijk na ontvangst van deze notificatie sturen de                              Au deskundigen, zowel aan de ontvanger als aan de partij, een schrijven                  ta waarbij zij hen verwittigen van dag en uur waarop zij de nodig geachte                pr bezoeken ter plaatse zullen doen en hen in hun gezegden en                            de opmerkingen zullen aanhoren.                                                          ob

Ieder aan de deskundigen door een der partijen ter inzage verleend                    To bescheid moet tezelfdertijd in afschrift aan de andere partij bij                     m aangetekende brief worden gezonden.                                                   pl

###### Art. 196

(lid 3 vervangen bij art. 7 van de wet van 27.05.1974 (B.S., 06.07.1974) err. (B.S.   (al 12.07.1974 en 21.12.1974). Tekst van toepassing vanaf 16.07.1973 (art. -))            12

De deskundige of, desvoorkomend, de drie gezamenlijke optredende                      L’e deskundigen vorsen den staat en de verkoopwaarde der in de                            re vordering tot schatting aangewezen goederen, op het er vermeld                        de tijdstip.

Zij maken, uiterlijk binnen drie maanden te rekenen van bij eerste                    Ils alinea van artikel 195 voorziene notificatie, één enkel verslag op, dat               no gedagtekend en ondertekend wordt, en waarin zij op beredeneerde                       qu wijze en met bewijsgronden tot staving, zonder enige beperking noch                   et voorbehoud, hun advies over bedoelde waarde uitbrengen.                               av

De handtekening van de deskundige wordt voorafgaan door de eed:                       La

"Ik zweer dat ik in eer en geweten, nauwgezet en eerlijk mijn opdracht                « heb vervuld".                                                                         ex

of:                                                                                   ou

"Je jure que j'ai rempli ma mission en honneur et conscience, avec                    “Ik exactitude et probité".                                                               he

of:                                                                                   ou

"Ich schwöre, dass ich den mir erteilten Auftrag auf Ehre und                         “Ic Gewissen, genau und ehrlich erfüllt habe".                                            Ge

De minuut van het verslag wordt ter griffie van het onder artikel 192                 La aangeduid vredegerecht neergelegd.                                                    dé

###### Art. 197

Het verslag wordt door de meest gerede partij gelicht en aan de                       Le andere partij betekend.                                                               ad

Naar de door de deskundigen gegeven waardering en, in geval van                       L’é niet-overeenstemming, naar de waardering van de meerderheid of,                       l’é bij gemis van meerderheid, naar de tussenwaardering, wordt de                         in verkoopwaarde van het goed ten opzichte van de heffing der                            la belasting bepaald.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 198

(vervangen bij art. 71 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (re van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De krachtens voorgaande artikelen van deze afdeling te verrichten                Le betekeningen en notificaties geschieden bij aangetekende zending.                pr re

###### Art. 198

De krachtens vorenstaande artikelen van deze afdeling te verrichten              Le betekeningen en notificaties mogen bij aangetekend schrijven                     pr geschieden. De afgifte van het stuk ter post geldt als notificatie vanaf         re de daaropvolgende dag.                                                           du

###### Art. 199

(vervangen bij art. 33 door de programmawet van 09.07.2004 (B.S.,                (re 15.07.2004 - ed. 2). Tekst van toepassing vanaf 25.07.2004 (art. -))             -é

Zowel de ontvanger als de partij kunnen de schatting betwisten door              Ta inleiding van een rechtsvordering. Deze rechtsvordering dient ingeleid           in te worden, op straffe van verval, binnen de termijn van één maand te             pe rekenen van de betekening van het verslag.                                       sig

###### Art. 200

(gewijzigd bij art. 181 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (m van toepassing vanaf 01.01.1990 (art. 244))                                      ap

Indien de opgegeven prijs of de aangegeven waarde lager is dan de                Si door de schatting opgeleverde begroting, moet de verkrijger het                  ré bijkomend recht betalen, met de moratoire intresten naar de in                   su burgerlijke zaken vastgestelde voet, te rekenen van de bij artikel 100           m voorziene notificatie en, desvoorkomend, met de bij artikel 201                  ca opgelegde boete.

Hem worden desvoorkomend ook de kosten van de procedure                          Il opgelegd, indien het vastgestelde tekort het achtste van de                      co uitgedrukte prijs of van de aangegeven waarde bereikt of overtreft.              va

Deze kosten blijven evenwel ten laste van 's Rijks Schatkist zo de               To belanghebbende, vóór de in artikel 190 voorziene notificatie, heeft              pr aangeboden het bijkomend recht, verhoogd met de boete bepaald in                 su artikel 201 te betalen, op een som welke het bij de schatting                    un uitgewezen tekort bereikt of overtreft.                                          l’e

De invordering geschiedt bij dwangschrift, zoals aangewezen in                         Le artikel 220.                                                                           in

### HOOFDSTUK XI - Tekort in de waardering, bewimpeling                                     C en veinzing. Sanctiën

###### Art. 201

(gewijzigd bij art. 182 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst            (m van toepassing vanaf 01.01.1990 (art. 244))                                            ap

Wanneer bevonden wordt dat de opgegeven prijs of de aangegeven                         Lo waarde van aan de onder artikel 189 voorziene schatting                                su onderworpen goederen te laag is, en dat het vastgestelde tekort gelijk                 l’in is aan of hoger dan het achtste van de opgegeven prijs of van de                       ou aangegeven waarde, verbeurt de verkrijgende partij een geldboete                       ég ten bedrage van het ontdoken recht.

###### Art. 202

(gewijzigd bij art. 15 van de wet van 23.12.1958 (B.S., 07.01.1959). Tekst van         (m toepassing vanaf 17.01.1959 (art. -))                                                  ap

Wanneer er geen aanleiding tot schatting bestaat en een waardering,                    Lo gedaan om de vereffening van de rechten mogelijk te maken,                             pe ontoereikend wordt erkend, is het ontdoken recht ondeelbaar                            él verschuldigd door hen die de waardering hebben gedaan; zij zijn                        en daarenboven ondeelbaar een boete verschuldigd gelijk aan het                           su aanvullend recht, zoo het tekort gelijk is aan of hoger is dan het                     lad achtste van bewuste waardering.

Alle andere onjuistheid, bevonden in de elementen van een verklaring                   To in of onderaan de akte gesteld tot vereffening van de belasting, wordt                 dé gestraft met een boete gelijk aan het ontdoken recht, benevens                         la betaling van dat recht, het al ondeelbaar ten laste van hen die de                     ou verklaring gedaan hebben.                                                              au

###### Art. 203

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

In geval van bewimpeling aangaande prijs en lasten overeengekomen                En waarde, is elke der contracterende partijen een boete verschuldigd               co gelijk aan het ontdoken recht. Dit recht ondeelbaar door alle partijen           co verschuldigd.                                                                    in

Het aanvullend recht dat ingevolge een bij schatting vastgesteld                 Le tekort of anderszins betaald geworden is, wordt aangerekend op het               co aanvullend recht, vereffend uit hoofde van de bewimpeling waarvan                su sprake in vorenstaande alinea.                                                   pr

In alle gevallen waarin de heffing op den prijs en de lasten op de               Da overeengekomen waarde geschiedt, moet de werkende notaris den                    ou verschijnende partijen de eerste alinea van dit artikel voorlezen.               do

Op straf van een boete van 25 EUR moet uitdrukkelijke melding van                M die voorlezing in de akte gemaakt worden.                                        pe

###### Art. 204

(gewijzigd bij art. 18 van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst van   (m toepassing vanaf 04.05.1965 (art. -))                                            ap

Wanneer de in een akte vastgestelde overeenkomst niet die is welke               Lo door de partijen werd gesloten, of wanneer de akte betreffende een               co in artikel 19, 2° of 5°, bedoelde overeenkomst onvolledig of onjuist             l’a is, met dien verstande dat ze al de bestanddelen van de                          ne overeenkomst niet doet kennen, is elke der contracterende partijen               in een geldboete verschuldigd gelijk aan het ontdoken recht. Dit recht is           ég ondeelbaar door alle partijen verschuldigd.                                      pa

###### Art. 205

(opgeheven bij art. 64 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst       (ab van toepassing vanaf 06.04.1999 (art. -))                                        ap

(…)                                                                              (…

### HOOFDSTUK XII - Correctionele straffen

###### Art. 206

(gewijzigd bij art. 22 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van   (m toepassing vanaf 01.11.2012 (art. -))                                            ap

Onverminderd de fiscale boeten, wordt hij die met bedrieglijk opzet of           Sa met het oogmerk om te schaden, de bepalingen van dit Wetboek of                  de de ter uitvoering ervan genomen besluiten overtreedt, gestraft met               l’u gevangenisstraf van acht dagen tot twee jaar en met geldboete van                fra 250 EUR tot 12.500 EUR of met één van die straffen alleen.                       pr

Wanneer de overtreding werd begaan in het kader van een                          Lo registratierecht dat geen gewestelijke belasting is volgens het                  d’ bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van          de 16 januari 1989 betreffende de financiering van de gemeenschappen                re en de gewesten, wordt het bedrag van het in het eerste lid bepaalde              du maximum van de boete gebracht op 500.000 euro.

###### Art. 206bis

(gewijzigd bij art. 23 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van   (m toepassing vanaf 01.11.2012 (art. -))                                            ap

Met gevangenisstraf van een maand tot vijf jaar en met geldboete van             Se 250 tot 12.500 EUR of met één van die straffen alleen frank wordt                de gestraft, hij die, met het oogmerk om een van de in artikel 206                  in bedoelde misdrijven te plegen, in openbare geschriften, in                       pu handelsgeschriften of in private geschriften valsheid pleegt, of die van         fa een zodanig vals geschrift gebruik maakt.

Hij die wetens en willens een vals getuigschrift opstelt dat de                  Ce belangen van de Schatkist kan schaden of die van een dergelijk                   co getuigschrift gebruik maakt, wordt gestraft met gevangenisstraf van              se acht dagen tot twee jaar en met geldboete van 250 tot 12.500 EUR.                am of met één van die straffen alleen.

Wanneer het misdrijf werd begaan in het kader van een                            Lo registratierecht dat geen gewestelijke belasting is volgens het                  d’ bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van          de 16 januari 1989 betreffende de financiering van de gemeenschappen                re en de gewesten, wordt het bedrag van het in het eerste en het tweede             du lid bepaalde maximum van de boete gebracht op 500.000 euro.                      eu

###### Art. 206bis/1

(ingevoegd bij art. 109 van de wet van 05.05.2019 (B.S., 24.05.2019 - ed. 1).    (in Tekst van toepassing op de datum bepaald door de Koning en ten laatste op        ap 01.01.2020 (art. 200))

Wanneer de overtreding werd begaan in het kader van een                          Lo registratierecht dat geen gewestelijke belasting is volgens het                  d' bepaalde in artikel 3, eerste lid, 6° tot 8° van de bijzondere wet van           de 16 januari 1989 betreffende de financiering van de gemeenschappen                re en de gewesten en teneinde te vermijden dat een veroordeelde aan                 d' een onredelijk zware straf zou worden onderworpen, houdt de                      lo rechter bij de straftoemeting rekening met de verschuldigde fiscale              fis boeten.

Artikel 42, 3°, van het Strafwetboek vindt geen toepassing op de                 L'a vermogensvoordelen die rechtstreeks uit de fiscale misdrijven zijn               pa verkregen, op de goederen en waarden die in de plaats ervan zijn                 va gesteld en op de inkomsten uit de belegde voordelen in geval de                  in vordering van de fiscale administratie gegrond wordt verklaard en tot            do een effectieve betaling van deze volledige vordering heeft geleid.

###### Art. 207

(vervangen bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van   (re toepassing vanaf 14.02.1981 (art. 22))                                           ap

§ 1. Wanneer de beoefenaar van een van de volgende beroepen:                     §1

1° belastingadviseur;                                                            1°

2° zaakbezorger;                                                                 2°

3° deskundige in belastingzaken of in boekhouden;                                3°

4° of enig ander beroep dat tot doel heeft voor een of meer                      4° belastingplichtigen boek te houden of te helpen houden, ofwel voor               les eigen rekening ofwel als hoofd, lid of bediende van enigerlei                    po vennootschap, vereniging, groepering of onderneming;                             em qu

5° of, meer in het algemeen, het beroep dat erin bestaat een of meer             5° belastingsplichtigen raad te geven of bij te staan bij het vervullen van         aid de verplichtingen opgelegd bij dit Wetboek of bij de ter uitvoering              dé ervan vastgestelde besluiten, wordt veroordeeld wegens een van de                du misdrijven bedoeld in de artikelen 206 en 206bis, kan het vonnis hem             ju verbod opleggen om gedurende drie maanden tot vijf jaar,                         d’ rechtstreeks of onrechtstreeks, de hiervoren bedoelde beroepen op                les welke wijze ook uit te oefenen.

De rechter kan bovendien, mits hij zijn beslissing op dat stuk                   Le motiveert, voor een duur van drie maanden tot vijf jaar de sluiting              or

bevelen van de inrichtingen van de vennootschap, vereniging,                      ét groepering of onderneming waarvan de veroordeelde hoofd, lid of                   do bediende is.

§ 2. Het verbod en de sluiting bedoeld in § 1 treden in werking vanaf             §2 de dag waarop de veroordeling in kracht van gewijsde is gegaan.                   àc

###### Art. 207bis

(gewijzigd bij art. 24 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van    (m toepassing vanaf 01.11.2012 (art. -))                                             ap

Hij die, rechtstreeks of onrechtstreeks, het verbod of de sluiting                Ce uitgesproken krachtens artikel 207 overtreedt, wordt gestraft met                 fe gevangenisstraf van acht dagen tot twee jaar en geldboete van 250                 em EUR tot 12.500 EUR of met één van die straffen alleen.                            12

Wanneer het verbod werd opgelegd in het kader van een                             Lo registratierecht dat geen gewestelijke belasting is volgens het                   d’ bepaalde in artikel 3, eerste lid, 6° tot 8°, van de bijzondere wet van           de 16 januari 1989 betreffende de financiering van de gemeenschappen                 re en de gewesten, wordt het bedrag van het in het eerste lid bepaalde               du maximum van de boete gebracht op 500.000 euro.

###### Art. 207ter

(gewijzigd bij art. 25 van de wet van 20.09.2012 (B.S., 22.10.2012). Tekst van    (m toepassing vanaf 01.11.2012 (art. -))                                             ap

§ 1. Alle bepalingen van het Eerste Boek van het Strafwetboek, met                § inbegrip van artikel 85, zijn van toepassing op de misdrijven bedoeld             co in de artikelen 206, 206bis en 207bis.                                            ar

§ 2. (…)                                                                          §2

§ 3. De wet van 5 maart 1952, gewijzigd bij de wetten van 22                      §3 december 1969 en 25 juni 1975, betreffende de opdecimes op de                     et strafrechtelijke geldboeten, is van toepassing op de misdrijven                   pé bedoeld in artikel 206, 206bis en 207bis.                                         20

###### Art. 207quater

(lid 2, 2°, gewijzigd bij art. 51 van de wet van 09.04.2024 (B.S., 18.04.2024).   (al Tekst van toepassing vanaf 28.04.2024 (art. -))                                   ap

Personen die als daders of als medeplichtigen van misdrijven bedoeld             Le in de artikelen 206 en 206bis werden veroordeeld, zijn hoofdelijk                co gehouden tot betaling van de ontdoken belasting en de interesten                 te verschuldigd door de oorspronkelijke belastingschuldige.                         pa

De personen beschuldigd als daders of als medeplichtigen van                     Le misdrijven bedoeld in de artikelen 206 en 206bis zijn eveneens                   vis gehouden tot betaling van de ontdoken rechten en de interesten zoals             pa bedoeld in het eerste lid, wanneer de bestanddelen van de misdrijven             lo bewezen verklaard zijn, wanneer ze genieten van:                                 lo

1° een opschorting van de uitspraak van de veroordeling of een uitstel           1° van de tenuitvoerlegging van de straffen voorzien in de wet van 29               à juni 1964 betreffende de opschorting, het uitstel en de probatie;                la

2° een veroordeling bij eenvoudige schuldigverklaring voorzien in                2° artikel 27 van de Voorafgaande titel van het Wetboek van                         l'a Strafvordering;

3° de procedure van voorafgaande erkenning van schuld bedoeld in                 3° artikel 216 van het Wetboek van Strafvordering;                                  l'a

4° de verjaring van de strafvordering.                                           4°

De natuurlijke personen of de rechtspersonen zijn burgerlijk en                  Le hoofdelijk aansprakelijk voor de geldboeten en kosten die het gevolg             so zijn van de veroordelingen welke krachtens de artikelen 206 tot                  co 207bis tegen hun aangestelden of hun bestuurders, zaakvoerders of                le vereffenaars, in het kader van de uitoefening van hun functie, in                le rechte of in feite zijn uitgesproken.

###### Art. 207quinquies

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van   (in toepassing vanaf 14.02.1981 (art. 22))                                           àp

De rechter kan bevelen dat ieder vonnis of arrest houdende                       Le veroordeling tot een gevangenisstraf, uitgesproken krachtens de                  co artikelen 206, 206bis en 207bis, wordt aangeplakt in de plaatsen die             de hij bepaalt en eventueel bij uittreksel, wordt bekendgemaakt op de               dé wijze die hij bepaalt, een en ander op kosten van de veroordeelde.               qu

Hetzelfde kan gelden voor iedere krachtens artikel 207 uitgesproken              Il beslissing     tot    verbod     van     het     uitoefenen      van     een     l'a beroepswerkzaamheid in België of tot sluiting van de in het land                 pr geëxploiteerde inrichtingen.                                                     d'

###### Art. 207sexies

(ingevoegd bij art. 13 van de wet van 10.02.1981 (B.S., 14.02.1981). Tekst van   (in toepassing vanaf 14.02.1981 (art. 22))                                           ap

De schending van het bij artikel 236bis bepaalde beroepsgeheim                   La wordt gestraft overeenkomstig de artikelen 66, 67 en 458 van het                 se Strafwetboek.

###### Art. 207septies

(gewijzigd bij art. 110 van de wet van 05.05.2019 (B.S., 24.05.2019 - ed. 1).    (m Tekst van toepassing op de datum bepaald door de Koning en ten laatste op        ap 01.01.2020 (art. 200))

§ 1. De strafvordering wordt uitgeoefend door het openbaar                       §1 ministerie.

§ 2. Het openbaar ministerie kan geen vervolging instellen indien het            § kennis heeft gekregen van de feiten ten gevolge van een klacht of een            co aangifte van een ambtenaar die niet de machtiging had waarvan                    d' sprake is in artikel 29, § 2, van het Wetboek van strafvordering.                l'a

Het openbaar ministerie beslist om al dan niet de strafvervolging in te          Le stellen van de feiten waarvan het kennis heeft genomen gedurende                 de het overleg bedoeld in artikel 29, § 3, tweede lid, van het Wetboek van          àl strafvordering binnen de 3 maanden na de initiële aangifte bedoeld in            m artikel 29, § 3, eerste lid, van hetzelfde Wetboek.                              m

§ 3. Onverminderd het in artikel 29, § 3, tweede lid, van het Wetboek            § van strafvordering bedoelde overleg, kan de procureur des Konings,               du indien hij een vervolging instelt wegens feiten die strafrechtelijk              de strafbaar zijn ingevolge de bepalingen van dit Wetboek of van de ter             pr uitvoering ervan genomen besluiten, het advies vragen van de                     du bevoegde adviseur-generaal. De procureur des Konings voegt het                   de feitenmateriaal waarover hij beschikt bij zijn verzoek om advies. De             gé adviseur-generaal antwoordt op dit verzoek binnen vier maanden na                sa de ontvangst ervan.

In geen geval schorst het verzoek om advies de strafvordering.                   En

###### Art. 207octies

(gewijzigd bij art. 70 van de wet van 25.04.2014 (B.S., 16.05.2014). Tekst van   (m toepassing vanaf 16.05.2014 (art. 99))                                           ap

De ambtenaren van de Algemene Administratie van de                               So Patrimoniumdocumentatie en de Algemene Administratie van de                      l’A Bijzondere Belastinginspectie mogen, op straffe van nietigheid van de            l'A akte van rechtspleging, slechts als getuige worden gehoord.                      pe

Het eerste lid is niet van toepassing op de krachtens artikel 71 van de          L'a wet van 28 december 1992 bij het parket gedetacheerde ambtenaren                 ad van die administraties.                                                          de

Het eerste lid is evenmin van toepassing op de ambtenaren van die                L'a administraties die, krachtens artikel 31 van de wet van 30 maart                 ad 1994 tot uitvoering van het globaal plan op het stuk van de fiscaliteit,         po ter beschikking zijn gesteld van de federale politie.                            di

Het eerste lid is niet van toepassing op de ambtenaren die deelnemen             L'a aan het in artikel 29, derde lid van het Wetboek van strafvordering              la bedoelde overleg.                                                                cr

### HOOFDSTUK XIII - Teruggaaf

###### Art. 208

De regelmatig geheven rechten kunnen niet worden teruggegeven,                   Le welke ook de latere gebeurtenissen zijn, behoudens in de bij deze titel          so voorziene gevallen.                                                              tit

###### Art. 209

(gewijzigd bij art. 96 van de wet van 17.03.2019 (B.S., 10.05.2019). Tekst van   (m toepassing vanaf 01.05.2019 (art. 119, § 1))   (1) ap

Zijn vatbaar voor teruggaaf:                                                     So

1° De rechten, geheven omdat de partijen in gebreke gebleven zijn in             1 de akte of verklaring te vermelden:                                              l’a

a) dat de overeenkomst reeds belast werd;                                        a)

b) dat de voorwaarden tot bekomen van vrijstelling of vermindering               b) vervuld zijn, tenzij het bestaan van deze vermelding bij de wet als een          un uitdrukkelijke voorwaarde ter verkrijging van de fiscale gunst is                l’e gesteld;                                                                         fa

2° De evenredige rechten geheven hetzij wegens een akte die vals                 2 verklaard werd, hetzij wegens een overeenkomst die uit hoofde van                dé nietigheid ongedaan gemaakt werd door een in kracht van gewijsde                 de gegaan vonnis of arrest.

3° het evenredig recht geheven wegens een overeenkomst waarvan                   3° een in kracht van gewijsde gegaan vonnis of arrest in ontbinding of de           ré herroeping uitspreekt, mits uit de beslissing blijkt dat ten hoogste één         ar jaar na de overeenkomst een eis tot ontbinding of herroeping, zelfs bij          dé een onbevoegd rechter, is ingesteld.                                             de de

4° de evenredige rechten geheven op een door een rechtspersoon                   4° gestelde rechtshandeling die door de hogere overheid nietig verklaard            un werd.

5° de bij toepassing van de artikelen 115, 115bis, 116 en 120 aan het            5° tarief van 0,5% geheven rechten naar aanleiding van een                          11 vermeerdering van het kapitaal of het eigen vermogen, met nieuwe                 ca inbreng, door een vennootschap bedoeld in artikel 201, eerste lid, 1°,           20 van het Wetboek van de inkomstenbelastingen 1992, mits die                       au vermeerdering van het kapitaal of het eigen vermogen is geschied                 lie binnen het jaar vóór de datum van de toelating tot de notering op een            au Belgische effectenbeurs van aandelen of met aandelen gelijk te                   so stellen waardepapieren van de vennootschap.

De teruggaaf geschiedt desvoorkomend onder aftrekking van het                    La algemeen vast recht.                                                             gé
----------                                                                       -- Nota (1) – Overgangsbepalingen:                                                  No Zolang het Wetboek van vennootschappen en verenigingen, overeenkomstig           Au hoofdstuk IV, afdeling II, van de wet van 23 maart 2019, niet van toepassing     23 is op een vennootschap, vereniging of stichting, moet elke verwijzing naar een   so bepaling van het Wetboek van vennootschappen en verenigingen die                 de voorkomt in een bepaling van het Wetboek van de inkomstenbelastingen             un 1992, het Wetboek van Registratie-, Hypotheek- en Griffierechten, het            d'e Wetboek van Successierechten, het Wetboek diverse rechten en taksen en het       du Wetboek van de Belasting over de Toegevoegde Waarde, de ter uitvoering           la ervan genomen besluiten en de bijzondere wetgeving van toepassing op deze        ex belastingen, worden gelezen, voor wat deze vennootschap, vereniging of           fo stichting betreft, als een verwijzing naar de bepaling van het Wetboek van       ar vennootschappen of andere bijzondere wetgeving die in zulke fiscale              dis wetgeving voorkwam voor de inwerkingtreding van deze wet (art. 119, § 2);
Zolang, overeenkomstig hoofdstuk IV, afdeling II van de wet van 23 maart         Au 2019, een vennootschap, vereniging of stichting, die door het Belgisch recht     23 wordt beheerst, een rechtsvorm heeft die het Wetboek van vennootschappen         co en verenigingen niet erkent, worden de bepalingen van het Wetboek van de         re inkomstenbelastingen 1992, het Wetboek van Registratie-, Hypotheek- en           Co Griffierechten, het Wetboek van Successierechten, het Wetboek diverse            de rechten en taksen en het Wetboek van de Belasting over de Toegevoegde            va

Waarde, de ter uitvoering ervan genomen besluiten en de bijzondere                  pr wetgeving van toepassing op deze belastingen, die voor de inwerkingtreding          vig van deze wet deze rechtsvorm vermeldden, geacht deze rechtsvorm te blijven          av vermelden voor wat deze vennootschap, vereniging of stichting betreft, zoals        as voor de inwerkingtreding van deze wet. (art. 119, § 3).

###### Art. 210

(gewijzigd bij art. 26 van de wet van 28.04.2019 (B.S., 06.05.2019). Tekst van      (m toepassing vanaf 16.05.2019 (art. -))                                               ap

In geval van gehele of gedeeltelijke vernietiging van een vonnis of                 En arrest door een andere in kracht van gewijsde gegane rechterlijke                   au beslissing zijn de op de vernietigde beslissing geheven evenredige                  pr rechten voor gehele of gedeeltelijke teruggaaf vatbaar.                             re

Het op een voorwaardelijke veroordeling geheven evenredig recht                     Le wordt teruggegeven in de mate dat er wordt aangetoond door alle                     la middelen van gemeen recht, met inbegrip van getuigen en                             et vermoedens, met uitzondering van de eed, dat de voorwaarde niet in                  ne vervulling is gegaan en het niet in vervulling gaan van de voorwaarde               ré leidt tot een resultaat dat gelijk is aan het afwijzen van de vordering.            la

Het recht wordt volledig teruggegeven indien het samengevoegd                       Le bedrag van de veroordelingen, vereffeningen of rangregelingen,                      l'o waarop de heffing werd gedaan, herleid wordt tot een som die bij                    les artikel 143, laatste lid, vastgestelde bedrag niet overschrijdt.                    qu

###### Art. 211

(opgeheven bij art. 23 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst          (ab van toepassing vanaf 01.01.1961 (art. 39))                                          ap

(…)                                                                                 (…

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989           Di betreffende de financiering van de gemeenschappen en de gewesten)                   re

###### Art. 212

(lid 5, gewijzigd bij art. 25 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst   (m van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                   27

In geval van wederverkoop van een onroerend goed, door de verkoper            En of zijn rechtsvoorgangers verkregen bij een akte waarop het bij artikel       ac 44 vastgestelde recht is voldaan, wordt drie vijfde van dat recht aan         re de wederverkoper teruggegeven indien de wederverkoop bij                      es authentieke akte vastgesteld is binnen twee jaar na de datum van de           da authentieke akte van verkrijging.

Wanneer de verkrijging of de wederverkoop heeft plaatsgehad onder             Lo een opschortende voorwaarde, wordt de termijn van wederverkoop                su berekend op basis van de datum waarop deze voorwaarde is vervuld.             ré

Niet teruggegeven wordt het recht dat betrekking heeft op het                 La gedeelte van de prijs en de lasten van de verkrijging, dat hoger is dan       du het bedrag dat tot grondslag heeft gediend voor de heffing van de             de belasting op de akte van wederverkoop.

In geval van gedeeltelijke wederverkoop wordt in het verzoek tot              Si teruggave het deel van de aanschaffingsprijs dat betrekking heeft op          pa het wederverkochte gedeelte nader aangegeven onder controle van               d’ het bestuur.

Een door de wederverkoper en de instrumenterende notaris                      Un ondertekend verzoek tot teruggave, onderaan op de akte gesteld voor           re de registratie, heeft dezelfde gevolgen als het met redenen omkleed           les verzoek ingevolge artikel 217 . Dit verzoek moet een afschrift van de Ce vermelding van de registratie van de authentieke akte van verkrijging         l’e bevatten, alsook de naam van de begunstigde van de teruggave en, in           du voorkomend geval, het rekeningnummer waarop het bedrag van de                 co terug te geven rechten moet worden gestort.

Gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet van 16.01.1989     Di betreffende de financiering van de gemeenschappen en de gewesten)             re

###### Art. 213

(gewijzigd bij art. 24 van het KB nr. 12 van 18.04.1967 (B.S., 20.04.1967).   (m Tekst van toepassing vanaf 30.04.1967 (art. -))                               ap

Wordt, onder aftrekking van het algemeen vast recht, aan de                   Es betrokken maatschappij teruggegeven het overeenkomstig artikel 51             gé geheven recht van 6 t.h. wanneer het aangekochte goed wordt                   l’im wederverkocht bij authentieke akte verleden binnen tien jaar na den           di datum van de akte van verkrijging.

Zijn toepasselijk op deze teruggaaf, de bepalingen van artikel 212,           So tweede en derde lid.                                                          ali

Eerste lid, 3° tot 5°: gewestelijke bepalingen (art. 3, eerste lid, 6° van de wet   Al van 16.01.1989 betreffende de financiering van de gemeenschappen en de              du gewesten)

### HOOFDSTUK XIV - Verjaring

###### Art. 214

(gewijzigd bij art. 63 van de wet van 28.12.1992 (B.S., 31.12.1992 - ed. 3) err.    (m (B.S., 18.02.1993). Tekst van toepassing vanaf 10.01.1993 (art. -))                 (M

Er is verjaring voor de invordering:                                                Il y

1° Van rechten en boeten verschuldigd op een akte of een                            1 overeenkomst, na twee jaar, enkel te rekenen van den dag van de                     de registratie van een akte of geschrift welke de oorzaak van de                       ou vorderbaarheid van de rechten en boeten aan het bestuur                             et genoegzaam doet kennen om de noodzakelijkheid van alle verdere                      to opzoeking uit te sluiten.

Worden, voor de toepassing van deze bepaling met registratie                        So gelijkgesteld: het visum van de repertoria van de notarissen, waarvan               di sprake in artikel 180; de ontvangst van de bij artikel 184                          18 voorgeschreven mededeling, zoomede de regelmatige inlevering van                    le een aangifte van nalatenschap;

2° Van rechten en boeten verschuldigd in geval van ontoereikende                    2 waardering, na twee jaar, te rekenen van den dag van de registratie                 ap van de akte of van de verklaring, dit alles onder voorbehoud van                    la hetgeen in artikel 190 is voorzien;

3° van rechten verschuldigd in geval van niet-vervulling van de in artikel          3 60 gestelde voorwaarden, na tien jaar, te rekenen van de datum van de               60 akte;

4° Van rechten verschuldigd in het in de tweede alinea van artikel 52               4 voorzien geval, na twee jaar, te rekenen van de intrekking van de premie;           ap

5° Van rechten en boeten verschuldigd in geval van onjuistheid in de in             5 artikelen 55, 2°, voorziene vermeldingen of attesten, na twee jaar, te              ou rekenen van den dag van de registratie van de akte;                                 jou

6° Van boeten verschuldigd in de in artikelen 1811 tot 183 voorziene                6 gevallen, na twee jaar, te rekenen van den dag waarop de overtreding                ap werd vastgesteld;

7° Van rechten en boeten verschuldigd buiten de in voorgaande                 7 nummers voorziene gevallen, met inbegrip van die welke betrekking             pr hebben op veinzing, bewimpeling van prijs of al ander feit niet of            di onjuist vastgesteld in een geregistreerde akte, na vijftien jaar, te          in rekenen van den dag waarop de rechtsvordering van de Staat                    co ontstaan is.

Is van toepassing, ten aanzien van de verjaring, artikel 18 van dit           Es wetboek.                                                                      pr

###### Art. 215

Er is verjaring voor de vordering tot teruggaaf van rechten, interesten       Il y en boeten, na twee jaar, te rekenen van den dag waarop de                     et rechtsvordering is ontstaan.

###### Art. 216

De verjaring van de bij artikel 189 ingestelde rechtsvordering tot            La schatting en die van de rechtsvordering tot inning van de rechten en          ce boeten verschuldigd wegens de ongenoegzaamheid blijkende uit die              de schatting, worden gestuit door de in artikel 190 bedoelde notificatie.        no

De stuiting heeft haar uitwerking tot den dag der nederlegging ter            Ce griffie van het verslag van schatting.                                        du

De invordering van rechten, interesten en gebeurlijk van boeten en            Le kosten, vorderbaar uit hoofde van de bij bedoeld verslag erkende              am ongenoegzaamheid, dient vervolgd binnen de twee jaar na de                    led nederlegging van dit verslag.                                                 ci.

###### Art. 2171

(gewijzigd en art. 2171 geworden door art. 36 van de wet van 23.12.1958       (m (B.S., 07.01.1959). Tekst van toepassing van 17.01.1959 (art. -))             07

De verjaringen voor de invordering van rechten, interesten en boeten,         Le worden gestuit op de wijze en onder de voorwaarden voorzien door              am artikel 2244 en volgende van het Burgerlijk Wetboek. In dit geval is er       pr een nieuwe verjaring, die op dezelfde wijze kan worden gestuit,               no verworven twee jaar na de laatste akte of handeling waardoor de               m vorige verjaring werd gestuit, indien er geen geding aanhangig is vóór        pr het gerecht.

De afstand van de verlopen tijd van de verjaring wordt, wat zijn                      La uitwerking betreft, gelijkgesteld met de stuitingshandelingen bedoeld                 às in vorige alinea.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 2172

(gewijzigd bij art. 72 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (m van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De verjaringen voor de teruggaaf van rechten, interesten en boeten                    Le worden gestuit door een met redenen omklede aanvraag                                  so genotificeerd bij aangetekende zending aan het kantoor dat de schuld                  re heeft vastgesteld of aan de bevoegde adviseur-generaal van de                         co Algemene Administratie van de Patrimoniumdocumentatie; ze                             pa worden eveneens gestuit op de wijze en onder de voorwaarden                           co voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-                     Lo generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee                 bu jaar, die slechts op de wijze en onder de voorwaarden voorzien bij                    an artikelen 2244 en volgende van het Burgerlijk Wetboek kan worden                      les gestuit, verworven twee jaar na de datum waarop de beslissing,                        es waarbij de aanvraag werd verworpen, aan belanghebbende met een                        de aangetekende zending genotificeerd werd.

###### Art. 2172

(gewijzigd bij art. 3 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van         (m toepassing vanaf 01.12.2021 (art. 7))                                                 àp

De verjaringen voor de teruggaaf van rechten, interesten en boeten                    Le worden gestuit door een met redenen omklede aanvraag                                  so genotificeerd bij aangetekende zending aan het kantoor dat de schuld                  re heeft vastgesteld of aan de bevoegde adviseur-generaal van de                         co Algemene Administratie van de Patrimoniumdocumentatie; ze                             pa worden eveneens gestuit op de wijze en onder de voorwaarden                           co voorzien door artikelen 2244 en volgende van het Burgerlijk Wetboek.

Zo de verjaring gestuit werd door de aan het kantoor of adviseur-                     Lo generaal genotificeerde aanvraag, is er een nieuwe verjaring van twee                 bu

jaar, die slechts op de wijze en onder de voorwaarden voorzien bij                    an artikelen 2244 en volgende van het Burgerlijk Wetboek kan worden                      les gestuit, verworven twee jaar na de datum waarop de beslissing,                        es waarbij de aanvraag werd verworpen, aan belanghebbende bij ter                        de post aangetekend schrijven genotificeerd werd.                                        po

De afgifte van de brieven ter post geldt als notificatie van de volgende              Le dag af.                                                                               len

###### Art. 218

(vervangen bij art. 96 van de wet van 26.03.2018 (B.S., 30.03.2018 - ed. 2).          (re Tekst van toepassing vanaf 09.04.2018 (art. -))                                       ap

Elke daad van onderzoek of van vervolging als bedoeld in artikel 22                   To van de Voorafgaande Titel van het Wetboek van Strafvordering                          pr betreffende de misdrijven bedoeld in artikel 206 en 206bis schorst de                 vis verjaring van de vordering tot voldoening van de rechten, de                          de interesten en de fiscale geldboeten die erop betrekking hebben.                       fis

De schorsing vangt aan met het op gang brengen van de                                 La strafvordering, en eindigt met het staken van de strafrechtelijke                     m vervolging, het verval van de strafvordering of wanneer het vonnis of                 l'e arrest in kracht van gewijsde is gegaan voor de misdrijven bedoeld in                 co het eerste lid.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Art. 219

(lid 2, gewijzigd bij art. 73 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).   (al Tekst van toepassing voor alle of bepaalde categorieën van houders van een            Te ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De moeilijkheden die in verband met de heffing of de invordering van                  La de registratierechten vóór het inleiden der gedingen kunnen oprijzen,                 pe worden door de minister van Financiën of de door hem gemachtigde                      l'in ambtenaar opgelost.                                                                   au

Indien, na onderhandelingen, met de minister of met de door hem                       Si gemachtigde ambtenaar geen akkoord wordt bereikt over een                             fo moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een             1e

aanvraag tot bemiddeling verzenden bij de fiscale bemiddelingsdienst               au bedoeld bij artikel 116 van de wet van 25 april 2007 houdende diverse              25 bepalingen (IV).

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat                  Da aan de in artikel 189 bedoelde schatting is onderworpen, kan de                    so bemiddeling van de fiscale bemiddelingsdienst daarover niet meer                   co gevraagd       of   worden     voortgezet      zodra    de    vordering     tot    su controleschatting is ingesteld. De Koning kan bepalen voor welke                   Ro moeilijkheden in verband met de heffing en invordering van de                      re registratierechten bemiddeling door de fiscale bemiddelingsdienst is               co uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar                    Le gaat dadingen met de belastingplichtigen aan, voor zover zij geen                  co vrijstelling of vermindering van belasting in zich sluiten.                        n'

Binnen de door de wet gestelde grenzen, wordt het bedrag van de                    Da proportionele fiscale boeten en de vermeerderingen vastgesteld in dit              pr Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald                   pa volgens een schaal waarvan de trappen door de Koning worden                        les vastgesteld. Deze bepaling geldt niet voor het bedrag van de                       to proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en           pr 204, behalve wanneer de overtreder hetzij uit eigen beweging en                    co voordat het bestuur iets gevorderd heeft, de overtreding aan het                   àc bestuur bekent, hetzij overleden is.

### HOOFDSTUK XV - Vervolgingen en gedingen

###### Art. 219

(gewijzigd bij art. 124 van de wet van 25.04.2007 (B.S., 08.05.2007 - ed. 3). In   (m werking vanaf 01.05.2007 (in afwijking hiervan kan de aanvraag tot                 ap bemiddeling slechts worden ingediend met ingang van 01.11.2007 (art. 14,           la KB 09.05.2007 (B.S., 24.05.2007)))                                                 (ar

De moeilijkheden die in verband met de heffing of de invordering van               La de registratierechten vóór het inleiden der gedingen kunnen oprijzen,              pe worden door de minister van Financiën of de door hem gemachtigde                   l'in ambtenaar opgelost.                                                                au

Indien, na onderhandelingen, met de minister of met de door hem                    Si gemachtigde ambtenaar geen akkoord wordt bereikt over een                          fo moeilijkheid als bedoeld in het eerste lid, kan de belastingplichtige een          1e aanvraag tot bemiddeling indienen bij de fiscale bemiddelingsdienst                au

bedoeld bij artikel 116 van de wet van 25 april 2007 houdende diverse bepalingen (IV).

Ingeval de moeilijkheid de verkoopwaarde betreft van een goed dat                Da aan de in artikel 189 bedoelde schatting is onderworpen, kan de                  so bemiddeling van de fiscale bemiddelingsdienst daarover niet meer                 co gevraagd       of   worden    voortgezet      zodra    de     vordering   tot    su controleschatting is ingesteld. De Koning kan bepalen voor welke                 Ro moeilijkheden in verband met de heffing en invordering van de                    re registratierechten bemiddeling door de fiscale bemiddelingsdienst is             co uitgesloten.

De minister van Financiën of de door hem gedelegeerde ambtenaar                  Le gaat dadingen met de belastingplichtigen aan, voor zover zij geen                co vrijstelling of vermindering van belasting in zich sluiten.                      n'

Binnen de door de wet gestelde grenzen, wordt het bedrag van de                  Da proportionele fiscale boeten en de vermeerderingen vastgesteld in dit            pr Wetboek of in de ter uitvoering ervan genomen besluiten, bepaald                 pa volgens een schaal waarvan de trappen door de Koning worden                      les vastgesteld. Deze bepaling geldt niet voor het bedrag van de                     to proportionele fiscale boeten bepaald in de artikelen 203, eerste lid, en         pr 204, behalve wanneer de overtreder hetzij uit eigen beweging en                  co voordat het bestuur iets gevorderd heeft, de overtreding aan het                 àc bestuur bekent, hetzij overleden is.

###### Art. 220

(gewijzigd bij art. 62 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van   (m toepassing vanaf 16.05.2016 (art. -))                                            ap

De eerste akte van vervolging ter invordering van fiscale rechten of             Le boeten en bijkomende sommen is een dwangschrift.                                 am

Het wordt door den met de invordering belasten ontvanger                         El uitgevaardigd; het wordt door den bevoegde adviseur-generaal van                 vis de Algemene Administratie van de Patrimoniumdocumentatie                         l’A geviseerd      en    uitvoerbaar      verklaard   en    bij    exploot    van    sig gerechtsdeurwaarder betekend.

###### Art. 221

(vervangen bij art. 67 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van   (re toepassing van 06.04.1999 (art. -))                                              ap

De tenuitvoerlegging van het dwangbevel kan slechts worden gestuit              L'e door een vordering in rechte.                                                   ac

###### Art. 222

(gewijzigd bij art. 4 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van   (m toepassing vanaf 01.12.2021 (art. 7))                                           àp

In geval van niet-betaling van een schuld voortvloeiende uit de                 En toepassing van dit Wetboek, kan de ambtenaar die belast is met de               pr invordering van die schuld, bij het Centraal Aanspreekpunt van de               pe Nationale Bank bedoeld in artikel 322, § 3, eerste lid, van het Wetboek         Na van de inkomstenbelastingen 1992 de gegevens opvragen die ten                   re aanzien van die schuldenaar beschikbaar zijn zonder de beperkingen              lim van artikel 322, §§ 2 tot 4, van hetzelfde Wetboek. De machtiging               vis hiertoe wordt verleend door een ambtenaar met minimum de graad                  co van adviseur–generaal.

###### Art. 223

De moratoire interesten op de in te vorderen of terug te geven                  Le sommen zijn verschuldigd naar den voet en de regelen in burgerlijke             so zaken vastgesteld.

###### Art. 224

(opgeheven bij art. 69 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst      (ab van toepassing vanaf 06.04.1999 (art. -))                                       ap

(…)                                                                             (…

###### Art. 225

De openbare ambtenaren die, krachtens de bepalingen van deze titel,             Le voor de partijen, de rechten en, bij voorkomend geval, de boeten                fa voorgeschoten hebben, kunnen, met het oog op de terugbetaling                   am ervan, uitvoerbaar bevel vragen aan de vrederechter van hun kanton.             po

De bepalingen van dit hoofdstuk zijn toepasselijk op het tegen dit              Le bevel aangetekend verzet.                                                       fo

###### Art. 225bis

(ingevoegd bij art. 70 van de wet van 15.03.1999 (B.S., 27.03.1999). Tekst van     (in toepassing vanaf 06.04.1999 (art. -))                                              àp

De termijnen van verzet, hoger beroep en cassatie, alsmede het                     Le verzet, het hoger beroep en de voorziening in cassatie schorsen de                 l'a tenuitvoerlegging van de gerechtelijke beslissing.                                 dé

###### Art. 225ter

(vervangen bij art. 382 van de programmawet van 27.12.2004 (B.S.,                  (re 31.12.2004 - ed. 2). Tekst van toepassing vanaf 10.01.2005 (art. -))               31

Het verzoekschrift houdende voorziening in cassatie en het antwoord                La op de voorziening mag door een advocaat worden ondertekend en                      po neergelegd.

###### Art. 225quater

(ingevoegd bij art. 97 van de wet van 26.03.2018 (B.S., 30.03.2018 - ed. 2).       (in Tekst van toepassing vanaf 09.04.2018 (art. -))                                    ap

De bepalingen van dit Wetboek doen geen afbreuk aan het recht van                  Le de Staat om het herstel van de schade te vorderen die kan bestaan uit              l'E de niet-betaling van de rechten, interesten, fiscale geldboeten en                 le bijbehoren door een burgerlijke partijstelling of door een                         ac aansprakelijkheidsvordering.                                                       re

### HOOFDSTUK XVI - Bijzondere bepalingen betreffende                                 C de openbare verkopingen van roerende goederen

###### Art. 226

(gewijzigd bij art. 48, § 4, van de wet van 05.07.1963 (M.B., 17.07.1963). Tekst   (m van toepassing vanaf 28.09.1963 (art. 52))                                         ap

Meubelen, koopwaren, hout, vruchten, oogsten en alle andere                        Le lichamelijke roerende voorwerpen mogen bij openbare toewijzing                     m slechts ten overstaan en door het ambt van een notaris of een                      qu gerechtsdeurwaarder verkocht worden.                                               ju

Nochtans kunnen Staat, provinciën, gemeenten en openbare                       To instellingen de hun toebehorende roerende voorwerpen openbaar                  pu door hun ambtenaren doen verkopen.                                             de

###### Art. 227

(vervangen bij art. 27 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2).   (re Tekst van toepassing vanaf 01.01.2024 (art. 29))                               ap

Iedere openbare officier die belast is met de openbare verkoop van             To roerende voorwerpen moet daarvan vooraf kennis geven aan het                   m bevoegde kantoor, behalve wanneer het gaat om voorwerpen die aan               sa de Staat, de gefedereerde entiteiten, de provincies, de gemeenten of           pr de openbare instellingen toebehoren.

De Koning kan bepalen:                                                         Le

1° de nadere regels van deze kennisgeving en de vermelding, als de             1° verkopende partij er een heeft, van haar identificatienummer in het            ve Rijksregister van de natuurlijke personen of in de registers van de            na Kruispuntbank van de sociale zekerheid of in de Kruispuntbank van              ca Ondernemingen;                                                                 En

2° dat de kennisgeving vergezeld moet gaan van metagegevens.                   2°

###### Art. 228

De werkende openbare officier of ambtenaar vermeldt, in zijn proces-           L’o verbaal, naam, voornamen, hoedanigheid en woonplaats van den                   pr verzoeker, van de personen wier mobilair te koop wordt gesteld en,             de indien het gaat om een verkoop na overlijden, van den overleden                ve eigenaar, zomede, desvorkomend, den datum van de overhandiging                 da of de verzending van de in artikel 227 voorziene kennisgeving.

###### Art. 229

(vervangen bij art. 28 van de wet van 28.12.2023 (B.S., 29.12.2023 – ed. 2).   (re Tekst van toepassing vanaf 01.01.2024 (art. 29))                               ap

De instrumenterende openbare officier of ambtenaar verbeurt voor               Il elke overtreding van de artikelen 227 en 228 een geldboete van 25              un euro.                                                                          et

###### Art. 230

De werkende openbare officier of ambtenaar moet van den                                Il e openbaren verkoop een proces-verbaal opmaken.                                          le

Ieder toegewezen voorwerp wordt onmiddellijk in dat proces-verbaal                     Ch opgetekend; de prijs wordt voluit in letterschrift en buiten de linie nog              pr eens in cijfers aangeduid.

Na elke zitting wordt het proces-verbaal afgesloten en ondertekend.                    Ap

###### Art. 231

(gewijzigd bij art. 190 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst            (m van toepassing vanaf 01.01.1990 (art. 244))                                            ap

Wordt voor de toepassing van dit hoofdstuk als toegewezen                              Es beschouwd en is aan het door de artikel 77 vastgesteld evenredig                       et recht onderworpen, ieder roerend voorwerp waarvan het openbaar                         m tekoopstelling van een openbaar aanbod of een openbaar gemaakt                         pu aanbod is gevolgd, ongeacht wie het aanbod heeft gedaan en welke                       of de modaliteiten van den verkoop zijn en ongeacht of al dan niet toewijzing plaats heeft.

Het recht is evenwel niet verschuldigd indien de werkende openbare                     To officier of ambtenaar onmiddellijk na ontvangst en bekendmaking van                    in de aanbiedingen verkondigt, en zulks in het proces-verbaal                             ré aantekent, dat het te koop gesteld voorwerp «ingehouden» wordt.                        re

Het recht wordt geheven op den toewijzingsprijs en, bij gebreke                        Le daaraan, op het hoogste aanbod.                                                        éle

Wanneer het een verkoop geldt, gedaan op verzoek van een                               Lo rechtspersoon, wordt nochtans niet afgeweken van artikelen 16 en                       il 17 voor zover zij beschikken voor het geval van voorbehoud van                         di machtiging, goedkeuring of bekrachtiging van de overheid.                              d’

###### Art. 232

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Worden door den werkenden openbaren officier of ambtenaar                              Il e verbeurd:

1° Een geldboete, gelijk aan twintigmaal het ontdoken recht, zonder                    1 dat ze minder dan 25 EUR mag bedragen:                                                 êt

a) voor elk toegewezen of bij artikel 231 als dusdanig beschouwd lot,                  a) welk niet onmiddellijk in het proces-verbaal wordt opgetekend;                         no

b) voor elk lot welk in het proces-verbaal als aan den verkoop                         b) onttrokken wordt opgegeven, wanneer de verklaring van inhouding                        dé niet werd gedaan in den bij artikel 231, 2 alinea, voorziene vorm; de l’a

c) voor elk lot waarvan de belastbare grondslag in het proces-verbaal                  c) vervalst of onvolkomen opgetekend werd; dit alles onverminderd het                     in ontdoken recht;                                                                        du

2° Een boete van 12,50 EUR voor elk toegewezen lot waarvan de prijs                    2 in het proces-verbaal niet voluit in letters of niet in cijfers buiten de              pa linie is aangeduid.                                                                    en

###### Art. 233

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

Iedere persoon die, buiten de aanwezigheid van een openbaar officier,                  Il roerende voorwerpen openbaar te koop heeft gesteld of doen stellen,                    ve loopt een geldboete gelijk aan twintigmaal het ontdoken recht, zonder                  pu dat deze boete, voor elk toegewezen of als dusdanig beschouwd lot,                     êt minder dan 25 EUR mag bedragen.                                                        te

De overtreders zijn daarbij hoofdelijk gehouden tot de betaling van het                Le ontdoken recht.                                                                        du

###### Art. 234

(gewijzigd bij art. 63 van de wet van 27.04.2016 (B.S., 06.05.2016). Tekst van         (se toepassing vanaf 16.05.2016 (art. -))                                                  (M

Ambtenaren         van     de      Algemene           Administratie     van     de     Le Patrimoniumdocumentatie hebben steeds toegang tot alle plaatsen                        pa waar roerende voorwerpen openbaar worden verkocht. Zij hebben                          d’ het recht zich de processen-verbaal van verkoop te doen overleggen

en van hun bevindingen proces-verbaal op te maken. Dit proces-                   ve verbaal geldt als bewijs tot het tegenbewijs.                                    Ce

###### Art. 235

(vervangen door het enig art. van de wet van 03.07.1962 (B.S., 17.07.1962).      (re Tekst van toepassing vanaf 27.07.1962 (art. -))                                  ap

De bepalingen van dit hoofdstuk zijn niet van toepassing op de                   Ne openbare verkopingen:                                                            pu

1° van alle landbouwproducten, in instellingen waar de koopwaren                 1° uitsluitend openbaar bij opbod of bij afbod verkocht worden op                   m bepaalde dagen en uren, die op bestendige wijze in de lokalen                    au aangeplakt zijn;                                                                 pe

2° van eetwaren en van afgesneden bloemen in de voornoemde                       2° instellingen of op de markten;                                                   pr

3° van voorwerpen welke in de openbare kassen van lening in pand                 3° werden gegeven;

4° van zee- en binnenschepen.                                                    4°

### HOOFDSTUK XVII - Inlichtingen te verstrekken door de Algemene Administratie van de Patrimoniumdocumentatie

###### Art. 236

Ar

(vervangen bij art. 10 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van   (re toepassing vanaf 01.11.2023 (art. 14, lid 1), met uitzondering van lid 3, van    ap toepassing vanaf 01.01.2024 (art. 14, lid 1, 7°). De Koning kan evenwel een      ap datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))                 un

De    ambtenaren      van    de    Algemene       administratie    van    de     Le patrimoniumdocumentatie leveren, hetzij op verzoek van een partij of             pa een rechtverkrijgende ervan, hetzij, ingevolge een beschikking van de            ay vrederechter, op verzoek van een derde die een rechtmatig belang                 d' inroept, afschriften of uittreksels af van hun registratieregisters en           le van geregistreerde akten en verklaringen, alles onverminderd de                  en bepalingen van bijzondere wetten.                                                pa

Deze afschriften of uittreksels kunnen aan de lasthebbers van de                 Ce belanghebbenden worden afgeleverd, indien zij van de lastgeving                  in laten blijken.

De aflevering van deze stukken geeft recht op een door de Koning te              La bepalen retributie.                                                              pa

###### Art. 236/1

(ingevoegd bij art. 11 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van   (in toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een          à datum van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))                 d’e

§ 1. De ambtenaren van de Algemene administratie van de                          § patrimoniumdocumentatie kunnen kosteloos inlichtingen afleveren                  do aan:                                                                             re

1° de administratieve diensten van de federale overheid, de                      1° gefedereerde entiteiten, de provincies, de agglomeraties, de                     fé federaties van gemeenten, de intercommunales, de gemeenten en de                 co openbare centra voor maatschappelijk welzijn;                                    pu

2° de parketten en de griffies van de hoven en van alle rechtscolleges;          2°

3° de openbare instellingen of inrichtingen, namelijk de instellingen,           3° maatschappijen, verenigingen, inrichtingen en diensten die de                    so mede beheert, waaraan zo een overheid een waarborg verstrekt,                    un waarop zo een overheid toezicht uitoefent op de werkzaamheden                    su ervan, of waarvan zo een overheid het leidinggevend personeel                    au aanwijst, voordraagt of hun aanstelling goedkeurt.

§ 2. Deze aflevering wordt beperkt tot de inlichtingen die noodzakelijk          § zijn voor de uitvoering van wettelijke bepalingen.                               l'e

De verstrekte inlichtingen mogen niet langer worden bewaard dan                  Le noodzakelijk is voor de verwezenlijking van met de verwerking van de             lo persoonsgegevens nagestreefde doelstelling.                                      tra

###### Art. 236/2

(aangevuld bij art. 79 van de wet van 12.05.2024 (B.S., 29.05.2024). Tekst van   (co toepassing vanaf 08.06.2024 (art. -))                                            ap

De Koning kan ter uitvoering van dit hoofdstuk:                                  Po

1° de nadere regels van de aanvraag bepalen, waaronder de                           1° vermelding,      als   de     aanvrager       er    een      heeft,   van    zijn   de identificatienummer in het Rijksregister van de natuurlijke personen                na of in de registers van de Kruispuntbank van de sociale zekerheid of in              Ca de Kruispuntbank van de ondernemingen;                                              en

2° de nadere regels van de aflevering bepalen;                                      2°

3° onder voorbehoud van de bepalingen van de Archiefwet van 24                      3° juni 1955, de bewaartermijnen en de wijze van bewaring bepalen van                  ar de vragen om inlichtingen en van de verstrekte antwoorden.                          re

###### Art. 236bis

(gewijzigd bij art. 13 van de wet van 31.07.2023 (B.S., 24.08.2023). Tekst van      (m toepassing vanaf 01.11.2023 (art. 14, lid 1). De Koning kan evenwel een datum       à van inwerkingtreding voorafgaand bepalen (art. 14, lid 2))                          d’e

Hij die, uit welken hoofde ook, optreedt bij de toepassing van de                   Ce belastingwetten of die toegang heeft tot de ambtsvertrekken van de                  lo Algemene Administratie van de Patrimoniumdocumentatie, is buiten                    gé het uitoefenen van zijn ambt, verplicht tot de meest volstrekte                     de geheimhouding aangaande alle zaken waarvan hij wegens de                            de uitvoering van zijn opdracht kennis heeft.                                          m

Personen die deel uitmaken van diensten of openbare instellingen of                 Le inrichtingen    waaraan       inlichtingen,    afschriften      of    uittreksels   pu afgeleverd werden overeenkomstig de bepalingen van dit hoofdstuk,                   dé zijn tot dezelfde geheimhouding verplicht en mogen ze niet gebruiken                te buiten het kader van de wettelijke bepalingen voor de uitvoering                    du waarvan zij zijn afgeleverd.                                                        ét

De    ambtenaren       van     de    Algemene       administratie      van    de    Le patrimoniumdocumentatie, oefenen hun ambt uit wanneer zij                           pa overeenkomstig de bepalingen van dit hoofdstuk inlichtingen,                        dé afschriften of uittreksels afleveren.                                               di

### HOOFDSTUK XVIII - Speciaal recht op de nationaliteit, de adelbrieven en de verzoeken tot verandering van naam

###### Art. 237

(opgeheven bij art. 30 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst          (ab van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                   ap

(…)                                                                              (…

#### Afdeling I - Nationaliteit

###### Art. 238

(gewijzigd bij art. 31 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van   (m toepassing vanaf 29.07.2025 (art. 33, lid 2))                                    ap

Er wordt een recht geheven op de procedures tot verkrijging van de               Il e Belgische nationaliteit, die worden bepaald bij hoofdstuk III van het            be Wetboek van de Belgische nationaliteit met uitzondering van de                   l’e procedures tot verkrijging van de Belgische nationaliteit op grond van           fo artikel 17 van het Wetboek van de Belgische nationaliteit.

Het recht bedraagt 1000 euro.                                                    Le

Dit recht wordt tot 150 euro verminderd voor de vreemdeling die de               Ce hoedanigheid heeft van staatloze in België krachtens de er vigerende             d'a internationale overeenkomsten en die zijn aanvraag indient op basis              so van artikel 19, § 2, van het Wetboek van de Belgische nationaliteit.             §2

Het recht moet gekweten worden vóór de indiening van het verzoek                 Le of vóór de aflegging van de verklaring.                                          le

Het recht wordt jaarlijks op 1 januari geïndexeerd volgens de volgende           Le formule: basisrecht vermenigvuldigd met de nieuwe index en gedeeld               su door de beginindex. Het resultaat verkregen ingevolge de indexering              l'in wordt afgerond op het hogere tiental euro.                                       la

De beginindex is de index van de consumptieprijzen van de maand                  L'i september 2024 en de nieuwe index is die van de consumptieprijzen                se van de maand september die elke indexatie voorafgaat.                            co

Uiterlijk in de loop van de maand december van elk jaar wordt het                Au bedrag toepasselijk tijdens het volgende kalenderjaar in het Belgisch            le Staatsblad gepubliceerd. De Federale Overheidsdienst Financiën                   M vermeldt die inlichting eveneens op zijn webstek.                                ce
----------                                                                       -- Nota:                                                                            No Procedures tot verkrijging van de Belgische nationaliteit - Publicatie           Pr voorgeschreven bij art. 238, laatste lid, W.Reg.:                                23 - geïndexeerde bedragen vanaf 01.01.2026: bericht van B.S., 29.12.2025:          -m 1030 euro (z. art. 238, 2 lid) ; aangevuld bij bericht van B.S., 16.03.2026 de – ed. 2: 160 euro (z. art. 238, 3 lid). de

###### Art. 239

(opgeheven bij art. 9 van de wet van 06.08.1993 (B.S., 23.09.1993). Tekst van     (ab toepassing vanaf 03.10.1993 (art. -))                                             àp

(…)                                                                               (…

###### Art. 240

(opgeheven bij art. 7, 2° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).   (ab Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor     ap deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke       av bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))             ap

(…)                                                                               (…

###### Art. 240bis

(opgeheven bij art. 7, 3° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).   (ab Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor     ap deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke       av bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))             ap

(…)                                                                               (…

###### Art. 241

(opgeheven bij art. 7, 4° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).   (ab Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor     ap deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke       av bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))             ap

(…)                                                                               (…

###### Art. 242

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S. 12.07.1984). Tekst     (ab van toepassing vanaf 01.01.1985 (art. 19))                                        ap

(…)                                                                               (...

###### Art. 243

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst    (ab van toepassing vanaf 01.01.1985 (art. 19))                                        ap

(…)                                                                               (...

###### Art. 244

(opgeheven bij art. 7, 5° van de wet van 24.12.1999 (B.S., 31.12.1999 – ed. 2).   (ab Tekst van toepassing vanaf 01.02.2000. De verzoeken om naturalisatie die voor     ap deze datum zijn ingediend, blijven onderworpen aan de vroeger toepasselijke       av bepalingen van de art. 238, 240, 240bis, 241 en 244 W.Reg. (art. 12))             ap

( …)                                                                              (...

###### Art. 245

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst    (ab van toepassing vanaf 01.01.1985 (art. 19))                                        ap

(…)                                                                               (...

###### Art. 246

(opgeheven bij art. 21, 5° van de wet van 28.06.1984 (B.S., 12.07.1984). Tekst    (ab van toepassing vanaf 01.01.1985 (art. 19))                                        ap

( …)                                                                              (...

###### Art. 247

(opgeheven bij art. 195 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst       (ab van toepassing vanaf 01.01.1990 (art. 244))                                       ap

(…)                                                                               (...

#### Afdeling II - Open brieven van adeldom en verzoeken tot verandering van naam

(gewijzigd bij art. 7 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van    (m toepassing vanaf 01.03.2021 (art. -))                                            àp

###### Art. 248

(gewijzigd bij art. 26 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst van   (m toepassing vanaf 09.03.2026 (art. 33, lid 1))                                    ap

Op open brieven van verlening van adeldom of van een hogere                      Il adeldomsrang of van opneming onder 's Rijks adel met of zonder titel,            co wordt er een recht van 740 euro geheven.                                         d’

De Koning kan bij een met redenen omkleed besluit dat recht                      Le verminderen, met dien verstande dat het aldus verminderde recht                  ré niet minder dan 490 euro mag bedragen voor de gezamenlijke                       de personen in de open brief bedoeld.

De vermindering kan slechts worden verleend wanneer de                           La begunstigde of een van de begunstigden, of een van hun                           bé bloedverwanten in de opgaande of nederdalende lijn, aan het Land                 Na buitengewone diensten heeft bewezen van vaderlandslievende,                      cu wetenschappelijke, culturele, economische, sociale of humanitaire aard.

###### Art. 249

(aangevuld bij art. 8 van de wet van 07.01.2024 (B.S., 19.01.2024). Tekst van    (co toepassing vanaf 01.07.2024 (art. 9))                                            ap

Een recht is verschuldigd wegens de indiening van het verzoek tot                Un verandering van naam bedoeld in artikel 370/3 van het Burgerlijk                 ch Wetboek.

Het recht bedraagt 140 euro.                                                     Le

Het recht is niet verschuldigd in geval van een verandering van naam             Le als bedoeld in de artikelen 11bis, 15 en 21 van het Wetboek van de               11 Belgische nationaliteit.

Het recht is niet verschuldigd bij een naamswijziging als bedoeld in             Le artikel 370/4, tweede lid, van het oud Burgerlijk Wetboek.                       37

###### Art. 250

(gewijzigd bij art. 130 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst     (m van toepassing vanaf 01.08.2018 (art. 136))                                     ap

In de gevallen bedoeld in artikel 248, eerste lid, en in artikel 249, is elke   Da begunstigde een recht verschuldigd.                                             dû

De door de kinderen of afstammelingen verschuldigde rechten                     To worden evenwel met de twee vijfden verminderd wanneer aan                       de hetzelfde recht onderworpen vergunningen bij eenzelfde beslissing               dr verleend worden aan een persoon en aan zijn kinderen of                         en afstammelingen waarvan het aantal drie overschrijdt.

###### Art. 251

(vervangen bij art. 131 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst     (re van toepassing vanaf 01.08.2018 (art. 136))                                     ap

Wanneer de vergunning tot verandering van naam wordt ingetrokken                Lo of vernietigd terwijl de registratierechten reeds geïnd zijn, betaalt de        alo verzoeker, behalve als hij te kwader trouw was, geen rechten meer               sa wanneer het verzoek beoogt rechtstreeks te verhelpen aan deze                   qu intrekking of vernietiging.

###### Art. 252

(gewijzigd bij art. 132 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst     (m van toepassing vanaf 01.08.2018 (art. 136))                                     ap

Het recht wordt berekend volgens het tarief van kracht op de datum              Le van het besluit tot verheffing in de adelstand, dat aan de                      d'o ondertekening van de adelbrieven voorafgaat, of op de datum van de              ce indiening van het verzoek tot verandering van naam.

###### Art. 253

(gewijzigd bij art. 133 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst     (m van toepassing vanaf 01.08.2018 (art. 136))                                     ap

De in artikel 248 bedoelde open brieven worden geregistreerd, tegen             Le betaling van het recht door de begunstigden, binnen zes maanden na              pa hun datum ten kantore Brussel.                                                  au

Wordt de registratie gevorderd na het verstrijken van hierboven                 Lo gestelde termijnen, zoo geeft deze formaliteit aanleiding tot het               de heffen van en geldboete gelijk aan het recht, onverminderd ditzelve.            ég

###### Art. 254

(gewijzigd bij art. 134 van de wet van 18.06.2018 (B.S., 02.07.2018). Tekst     (m van toepassing van 01.08.2018 (art. 136))                                       ap

Na betaling van het recht en, gebeurlijk, van de geldboete, wordt               Ap vermelding van registratie gesteld op den open brief van adeldom.               de

Zolang aan de formaliteit van registratie niet is voldaan, mag de open          La brief van adeldom niet aan begunstigden worden uitgereikt.                      ta

#### Afdeling III - Bepaling gemeen aan afdelingen I en II

(gewijzigd bij art. 9 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van   (m toepassing vanaf 01.03.2021 (art. -))                                           àp

###### Art. 255

De algemene bepalingen van deze titel betreffende de formaliteit van            Le de registratie, de verplichting van inzageverlening, bewijsmiddelen,            l’e verjaring, rechtsvervolgingen en gedingen, moratoire interesten zijn            la van toepassing in de mate waarin daarvan bij dit hoofdstuk niet wordt           so afgeweken.                                                                      ch

### HOOFDSTUK XIX - Speciale geldboete wegens late                            C

neerlegging van aan bekendmaking onderworpen akten van vennootschap

###### Art. 256

(opgeheven bij art. 28 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).    (ab Tekst van toepassing vanaf 08.01.2018 (art. -))                                 ap

(…)                                                                             (…

###### Art. 257

(opgeheven bij art. 29 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).    (ab Tekst van toepassing vanaf 08.01.2018 (art. -))                                 ap

(…)                                                                             (…

###### Art. 258

(opgeheven bij art. 30 van de wet van 25.12.2017 (B.S., 29.12.2017 - ed. 1).    (ab Tekst van toepassing vanaf 08.01.2018 (art. -))                                 ap

(…)                                                                             (…

###### Art. 259

tot 267 W.Reg. federaal                                                Ar

Het hypotheekrecht is een federale belasting (art. 3, a contrario, wet          Le 16.01.1989 betreffende de financiering van de gemeenschappen en                 du de gewesten).                                                                   ré

## TITEL II - HYPOTHEEKRECHT

###### Art. 259

(gewijzigd bij art. 5 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van   (m toepassing vanaf 01.12.2021 (art. 7))                                           àp

Onder de benaming hypotheekrecht wordt een belasting gevestigd                  Il op de inschrijvingen van hypotheken en voorrechten op onroerende                in goederen.

###### Art. 260

(gewijzigd bij art. 99 van de wet van 11.07.2018 (B.S., 20.07.2018 - ed. 2).    (m Tekst van toepassing vanaf 30.07.2018 (art. -))                                 ap

Inschrijving van hypotheek wordt slechts verleend, tegen                        La voorafbetaling door de verzoeker, van de uit dien hoofde                        m verschuldigde retributies en recht.                                             ré

Het detail en het totaal van de voor recht en retributies ontvangen              Le sommen worden op het inschrijvingsborderel vermeld                               ré

De Koning kan deze wijze van vermelding geven aanvullen of wijzigen              Le voor het geval het inschrijvingsborderel op gedematerialiseerde wijze            lo wordt aangeboden.                                                                dé

###### Art. 261

(vervangen bij art. 6 van de wet van 26.11.2021 (B.S., 02.12.2021). Tekst van    (re toepassing vanaf 01.12.2021 (art. 7))                                            ap

Wanneer een inschrijving op verschillende kantoren wordt gevraagd                Lo tot zekerheid van één en hetzelfde bedrag, wordt het over dat bedrag             sû verschuldigde recht vastgesteld door het kantoor waar de inschrijving            re het eerst is gevorderd. Het over dat bedrag geïnde recht dekt de                 pe inschrijvingen op de overige kantoren.                                           bu

Wanneer tot zekerheid van één en hetzelfde bedrag op                             Lo gedematerialiseerde wijze gelijktijdig een inschrijving wordt gevraagd           re op verschillende kantoren, wordt het over dat bedrag verschuldigde               bu recht vastgesteld door het kantoor dat bevoegd is voor het goed dat              bo als eerste in het inschrijvingsborderel is vermeld. Het over dat bedrag          dr geïnde recht dekt de inschrijvingen op de overige kantoren.                      bu

###### Art. 262

(gewijzigd bij art. 196 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (m van toepassing vanaf 01.01.1990 (art. 244))                                      ap

Het hypotheekrecht is op 0,30 t.h. gesteld.                                      Le

###### Art. 263

Het recht is vereffend op het bedrag in hoofd- en bijkomende                     Le sommen waarvoor de inschrijving genomen of hernieuwd wordt.                      so

###### Art. 264

(gewijzigd bij art. 2, nr. 11 en 5, § 7, 2° van het KB van 20.07.2000 (B.S.,     (m 30.08.2000 - ed. 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf   30 gewijzigd bij art. 42, 3° en 5° van het KB van 13.07.2001 (B.S., 11.08.2001 -    m

ed. 1) err. (B.S., 21.12.2001). Tekst van toepassing vanaf 01.01.2002 (art. 45,    11
§ 1))                                                                              01

Het bedrag van het vereffende recht wordt, desvoorkomend, tot de                   Le hogere cent afgerond.                                                              su

Het in te vorderen recht mag niet minder dan 5 EUR bedragen.                       Le

###### Art. 265

(3°, gewijzigd bij art. 103 van de wet van 21.01.2022 (B.S., 28.01.2022 - ed.      (3 1). Tekst van toepassing vanaf 07.02.2022 (art. -))                                Te

Zijn vrijgesteld van hypotheekrecht:                                               So

1° Inschrijvingen van wettelijke hypotheken en hun vernieuwingen;                  1

2° Inschrijvingen ambtshalve door den Algemene Administratie van                   2 de Patrimoniumdocumentatie genomen;                                                Do

3° Inschrijvingen tot zekerheid van de invordering van belastingen,                3 verschuldigd aan de Staat, gefedereerde entiteiten, provincies,                    du gemeenten, polders en wateringen, en vernieuwingen van die                         po inschrijvingen;

4° Inschrijvingen genomen ten laste van den Staat, van openbare                    4 instellingen van den Staat en andere in artikel 161, 1°, aangewezen                pu rechtspersonen, en hun vernieuwingen;                                              16

5° De inschrijvingen van de voorrechten en hypotheken opgesteld bij                5° de wet betreffende het herstel van zekere schade veroorzaakt aan                   re private goederen door natuurrampen.                                                pr

###### Art. 266

(laatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S., 07.01.1959).   (de Tekst van toepassing vanaf 17.01.1959 (art. -))                                    Te

Er is verjaring:                                                                   Il y

1° Voor de invordering van hypotheekrechten die op het tijdstip van                1 de inschrijving niet zouden geheven zijn geweest, na twee jaar, te                 ét rekenen van den dag der inschrijving;                                              jo

2° Voor de vordering tot teruggaaf van ten onrechte geheven rechten,            2 na twee jaar, te rekenen van den dag der betaling.                              de

Die verjaringen worden gestuit overeenkomstig artikel 2171 en 2172.             Le et

###### Art. 267

Zijn toepasselijk op het hypotheekrecht, de bepalingen van titel I,             So betreffende de rechtsvervolgingen en gedingen en de moratoire                   re interesten.

###### Art. 268

tot 288 W.Reg. federaal

Het griffierecht is een federale belasting (art. 3, a contrario, wet            Le 16.01.1989 betreffende de financiering van de gemeenschappen en                 16 de gewesten).                                                                   ré

## TITEL III - GRIFFIERECHT

### HOOFDSTUK I - VESTIGING VAN DE BELASTING EN                                   C

## VASTSTELLING VAN DE RECHTEN

###### Art. 268

(gewijzigd bij art. 2 van de wet van 28.04.2015 (B.S., 26.05.2015). Tekst van   (m toepassing vanaf 01.06.2015 (art. 2, 1°, KB 12.05.2015 (B.S, 26.05.2015)))      àp

Onder de benaming van griffierecht wordt een belasting gevestigd op             Il e de hiernavolgende in de hoven en rechtbanken gedane verrichtingen:              ci-

1° de inschrijving van zaken op de algemene rol, op de rol van de               1 verzoekschriften of op de rol van de vorderingen in kort geding;                rô

2° het opstellen van akten van de griffiers, van vóór hen verleden              2 akten, van zekere akten van de rechters en van de ambtenaren van                ac het openbaar ministerie;

3° het afleveren van uitgiften, kopieën of uittreksels uit akten,               3° vonnissen en arresten en van kopieën van andere stukken die op de               ju griffie worden bewaard;

#### Afdeling I - Rolrecht

###### Art. 2691

(gewijzigd bij art. 130 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst       (m van toepassing vanaf 29.06.2019 (art. -))                                         ap

Voor elke zaak die op de algemene rol, in het register van de                     Il verzoekschriften of in het register van de vorderingen in kort geding             re wordt ingeschreven of terug ingeschreven, is er verschuldigd:

1° in de vredegerechten en de politierechtbanken, een recht van 50                1° euro;                                                                             eu

2°      in   de    rechtbanken        van     eerste     aanleg      en    de     2° ondernemingsrechtbanken, een recht van 165 euro;                                  l'e

3° in de hoven van beroep een recht van 400 euro;                                 3°

4° in het Hof van Cassatie een recht van 650 euro.                                4°

Geen enkel recht wordt geïnd bij de rechtsgedingen voor de                        Au beslagrechter of de vrederechter in het kader van de toepassing van               de artikel 1409, § 1, vierde lid, en 1409, § 1bis, vierde lid, van het               14 Gerechtelijk Wetboek.

De zaken die worden geacht spoedeisend te zijn zoals bedoeld in                   Le artikel 1253ter/7 van het Gerechtelijk Wetboek zijn onderworpen aan               ju een eenmalig recht wanneer de nieuwe aanhangigmaking bij de                       no familierechtbank het wijzigen van een vordering waarover deze zich                su al heeft uitgesproken, tot doel heeft. Dit stelsel wordt uitgebreid tot           re de maatregelen betreffende de uitoefening van het ouderlijk gezag                 de uitgesproken door de jeugdrechtbank, waarvan de wijziging wordt                   de gevraagd voor de familierechtbank.
----------                                                                        -- Nota:                                                                             No De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het     La Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de        de rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019        jus en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de   31 rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om          m juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld   sit krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van       lig het gerechtelijk wetboek teneinde de toegang tot de juridische                    31 tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake          jur geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die             pla van toepassing waren vóór de inwerkingtreding van die bepalingen.                 qu

###### Art. 2692

(gewijzigd bij art. 131 van de wet van 05.05.2019 (B.S., 19.06.2019). Tekst       (m van toepassing vanaf 29.06.2019 (art. -))                                         ap

§ 1. De rechter veroordeelt in zijn eindbeslissing de partij of de partijen       § die het recht verschuldigd zijn tot de betaling ervan of tot betaling van         pa hun deel erin. Tegen de beslissing van de rechter kan geen                        pa rechtsmiddel worden aangewend.                                                    su

Het recht is volledig verschuldigd door de partij die de zaak op de rol           La heeft doen stellen, behalve indien:                                               dr

1° de verweerder in het ongelijk wordt gesteld, in welk geval het recht           1° volledig verschuldigd is door de verweerder;                                      le

2° de partijen onderscheidenlijk omtrent enig geschilpunt in het                  2° ongelijk zijn gesteld, in welk geval het recht ten dele door de eiser en          ca ten dele door de verweerder verschuldigd is, volgens de beslissing van            dé de rechter.

Het recht wordt opeisbaar op de datum van de veroordeling.                        Le

§ 2. In geval de zaak op de rol wordt doorgehaald of van de rol wordt             §2 weggelaten bij toepassing van artikel 730, § 1 en § 2, a), van het                l’a Gerechtelijk Wetboek, is het recht vanaf de datum van de doorhaling               pa of van de weglating opeisbaar ten laste van de partij die de zaak op de           qu rol heeft doen stellen.
----------                                                                        -- Nota:                                                                             No De wijziging van de wet van is vernietigd door het arrest nr. 84/2021 van het     La Grondwettelijk Hof van 10.06.2021 in zoverre zij van toepassing zijn op de        de rechtzoekenden van wie de zaak op de rol is ingeschreven tussen 01.02.2019        jus en 31.08.2020, die uiterlijk op 31.08.2020 zijn veroordeeld tot betaling van de   31 rolrechten, en van wie de bestaansmiddelen lager zijn dan de plafonds om          m juridische tweedelijnsbijstand en rechtsbijstand te genieten, zoals vastgesteld   sit krachtens de artikelen 3 en 4 van de wet van 31.07.2020 « tot wijziging van       lig het gerechtelijk wetboek teneinde de toegang tot de juridische                    31 tweedelijnsbijstand en de rechtsbijstand te verbeteren, door de ter zake          jur geldende inkomensmaxima te verhogen », maar hoger dan de plafonds die             pla van toepassing waren vóór de inwerkingtreding van die bepalingen.                 qu

###### Art. 2693

(opgeheven bij art. 4 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).       (ab Tekst van toepassing vanaf 01.02.2019 (art. 29))   (1) ap

(…)                                                                                   (…
----------                                                                            -- Nota (1) – Overgangsbepaling:                                                         No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in              Le vanaf hun datums van inwerkingtreding (art. 28).                                      da

###### Art. 2694

(opgeheven bij art. 5 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).           (ab Tekst van toepassing vanaf 01.02.2019 (art. 29))     (1) ap

(…)                                                                                   (…
----------                                                                            -- Nota (1) – Overgangsbepaling:                                                         No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in              Le art. 269 , 1 lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht 1   ste ré vanaf hun datums van inwerkingtreding (art. 28).                                      da

###### Art. 270

(opgeheven bij art. 26 van de wet van 12.07.1960 (B.S., 09.11.1960); de art.          (ab 269 en 270 zijn door art. 269 vervangen. Tekst van toepassing vanaf                   27 01.01.1961 (art. 39))                                                                 39

(…)                                                                                   (...

#### Afdeling Ibis - Opstelrecht

###### Art. 2701

(gewijzigd bij art. 98 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst van        (m toepassing vanaf 08.07.2012 (art. -))                                                 ap

Op akten van griffiers van hoven en rechtbanken, op akten die buiten                  Il e bemoeiing van rechters vóór hen zijn verleden, wordt een opstelrecht                  de geheven van 35 euro.                                                                  ju

Met akten van griffiers van hoven en rechtbanken worden                               So gelijkgesteld, overschrijvingen gedaan door griffiers in hun registers,               tra van de verklaringen van beroep of van voorziening in verbreking                       dé strafzaken, door gedetineerden of geïnterneerden afgelegd.                            ré

###### Art. 2702

(gewijzigd bij art. 99 van de programmawet van 22.06.2012 (B.S.,                (m 28.06.2012). Tekst van toepassing vanaf 08.07.2012 (art. -))                    ap

De akten van bekendheid, de akten van aanneming en de akten                     Le waarbij een minderjarige machtiging wordt verleend om handel te                 un drijven, die verleden worden ten overstaan van de vrederechters, zijn           de onderhevig aan een opstelrecht waarvan het bedrag op 35 euro wordt              à3 bepaald.

###### Art. 2703

(gewijzigd bij art. 100 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst     (m van toepassing vanaf 08.07.2012 (art. -))                                       ap

De verklaringen van keus van vaderland zijn onderhevig aan een                  Le opstelrecht, waarvan het bedrag op 35 euro wordt bepaald.                       ré

Dit recht is vatbaar voor teruggaaf ingeval de inwilliging bij een              Ce eindbeslissing van het bevoegd gerecht wordt geweigerd.                         dé

#### Afdeling II - Expeditierecht

###### Art. 271

(2°, gewijzigd bij art. 252 van de wet van 15.04.2018 (B.S., 27.04.2018 - ed.   (2 2). Tekst van toepassing vanaf 01.11.2018 (art. 260). De Koning kan een         Te voorafgaande datum van inwerkingtreding bepalen (art. 260, lid 2))              d'e

Op de uitgiften, kopieën of uittreksels die in de griffies worden               Il afgeleverd, wordt een expeditierecht geheven van:                               da

1°    1,75     euro   per    bladzijde      in   de   vredegerechten      en    1 politierechtbanken;                                                             po

2° 3 euro per bladzijde in de hoven van beroep, de hoven van assisen,           2 het militair gerechtshof, de arrondissementsrechtbanken, de                     co rechtbanken van eerste aanleg, de ondernemingsrechtbanken en de                 pr krijgsraden;                                                                    gu

3° 5,55 euro per bladzijde in het Hof van Cassatie.                             3

###### Art. 272

(gewijzigd bij art. 102 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst    (m van toepassing vanaf 08.07.2012 (art. -))                                      ap

Ongeacht op welke griffie en ongeacht op welke informatiedrager de             Qu aflevering geschiedt, wordt het recht op 0,85 euro per bladzijde               so bepaald, zonder dat het verschuldigd bedrag aan rechten lager mag              pa zijn dan 1,75 euro per afgifte op papier en 5,75 euro op een andere            à drager:                                                                        su

1° voor de niet ondertekende kopieën. Indien echter bij één en                 1° hetzelfde verzoek en voor één en dezelfde zaak meer dan twee                   po kopieën worden aangevraagd, wordt het tarief vanaf de derde kopie              pa bepaald op 0,30 euro per bladzijde, zonder dat het globaal bedrag aan          m verschuldigde expeditierechten alsdan meer dan 1.450 euro kan                  êt bedragen;

2° voor uitgiften, kopieën of uittreksels uit de registers van de              2° burgerlijke stand of uit de registers welke de akten betreffende het           civ verkrijgen, het herkrijgen, het behoud en het verlies van nationaliteit        re bevatten;

3° voor uitgiften, kopieën of uittreksels uit akten, vonnissen en              3° arresten die krachtens artikel 162, 33°bis tot 37°bis, vrijstelling            ar genieten van de formaliteit der registratie;                                   de

4° voor de uitgiften, kopieën of uittreksels van akten en stukken              4° betreffende rechtspersonen ingeschreven in de Kruispuntbank van                co Ondernemingen.                                                                 Ca

Hetzelfde recht is verschuldigd voor uitgiften, kopieën en uittreksels         Le uit akten, vonnissen en arresten afgeleverd in kieszaken of                    ac militiezaken. Deze stukken dragen bovenaan de vermelding van hun               Ce bestemming; zij mogen tot geen andere doeleinden dienen.                       pe

Hetzelfde recht is eveneens verschuldigd voor de kopie van een                 Le elektronisch bestand. Het recht is verschuldigd voor elke gekopieerde          éle elektronische bladzijde van het brondocument. De parameters van                do het brondocument, die de elektronische bladzijde bepalen, mogen bij            do het maken van de kopie niet gewijzigd worden.                                  êt

###### Art. 273

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006 - ed. 3).   (m Tekst van toepassing vanaf 07.01.2007 (art. -))                                (M

Het recht wordt berekend per bladzijde van het arrest, het vonnis of             Le de akte, welke in de uitgifte, de kopie of het uittreksel wordt                  re weergegeven.

Het recht wordt evenwel éénvormig berekend alsof er slechts één                  To bladzijde was, voor de uittreksels die worden afgeleverd ter uitvoering          les van artikel 121 van het Algemeen Reglement op de gerechtskosten in               gé strafzaken.

###### Art. 274

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S. 28.12.2006). Tekst van   (m toepassing vanaf 07.01.2007 (art. -))                                            (M

Wanneer in een uitgifte, kopie of uittreksel meerdere arresten,                  Lo vonnissen of akten worden weergegeven, wordt het recht berekend                  un per bladzijde van elk dezer documenten, zonder dat er, voor ieder van            ch deze documenten, minder mag geheven worden dan het recht                         d' verschuldigd voor één bladzijde.

###### Art. 274bis

(gewijzigd bij art. 103 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst      (m van toepassing vanaf 08.07.2012 (art. -))                                        ap

Voor kopieën van audiovisueel materiaal is, ongeacht op welke                    Po informatiedrager de kopie wordt afgeleverd, per gekopieerde minuut               leq 1,15 euro verschuldigd, zonder dat de verschuldigde rechten minder               qu mogen bedragen dan 5,75 euro Een begonnen minuut telt voor een                   en volle minuut.

###### Art. 274ter

(gewijzigd bij art. 104 van de wet van 22.06.2012 (B.S., 28.06.2012). Tekst      (m van toepassing vanaf 08.07.2012 (art. -))                                        ap

De expeditierechten die verschuldigd zijn op één en hetzelfde verzoek            Le voor één en dezelfde zaak, mogen 1 450 euro niet overschrijden.                  pe

#### Afdeling III - Legalisatie- en opzoekingsrechten

###### Art. 275

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst        (ab van toepassing vanaf 01.01.1990 (art. 244))                                        ap

(…)                                                                                (...

###### Art. 276

(opgeheven bij art. 205 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst        (ab van toepassing vanaf 01.01.1990 (art. 244))                                        ap

(…)                                                                                (...

#### Afdeling IV - Recht van inschrijving in het handelsregister, in                     S het ambachtsregister en in de registers van de economische samenwerkingsverbanden

###### Art. 277

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003 - ed. 3).   (ab Tekst van toepassing vanaf 01.07.2003 (art. 6))                                    ap

(…)                                                                                (…

###### Art. 278

(opgeheven bij art. 5, § 1 van het KB van 28.05.2003 (B.S., 20.06.2003). Tekst     (ab van toepassing van 01.07.2003 (art. 6))                                            ap

(…)                                                                                (...

### HOOFDSTUK II - Vrijstellingen

###### Art. 2791

(aangevuld bij art. 6 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).        (co Tekst van toepassing vanaf 01.02.2019 (art. 29))   ((1) ap

Zijn vrijgesteld van het rolrecht:                                                 So

1° De inschrijving van zaken waarvan de vonnissen en arresten,                     1 krachtens artikelen 161 en 162, vrijstelling genieten van het recht of             de van de formaliteit der registratie.                                                de

Het recht is echter verschuldigd voor de onder artikel 162, 13°,                   To bedoelde procedures;                                                               13

2° De inschrijving van een zaak door de griffier van het gerecht                   2 waarnaar de zaak verwezen werd overeenkomstig de wet op het                        ce gebruik der talen in gerechtszaken of ingevolge een rechterlijke                   lan beslissing van onttrekking.                                                        de

3° de inschrijving van zaken die worden gebracht voor de                           3° arbeidsgerechten;                                                                  tra

4° de inschrijving van zaken die ingeleid worden in het kader van het              4° boek XX van het Wetboek van economisch recht.                                      XX
----------                                                                         -- Nota (1) – Overgangsbepaling:                                                      No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in           Le art. 269 , 1 lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht 1   ste ré vanaf hun datums van inwerkingtreding (art. 28).                                   da

###### Art. 2792

(5°, opgeheven bij art. 32 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst     (5 van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                  ap

Zijn vrijgesteld van het opstelrecht:                                              So

1° de akten verleden in de gevallen voorzien door artikelen 161 en                 1° 162;

2° de akten of ontvangstbewijzen ten blijke van het neerleggen of                  2° mededelen van stukken, sommen of voorwerpen ter griffie van de                     de hoven en rechtbanken;

3° de faillissementsbekentenissen, alsmede de afsluitingen of                      3° vermeldingen dier worden aangebracht op de registers, titels en                    les stukken tot staving daarvan;

4° (…)                                                                             4°

5° (…)                                                                             5°

###### Art. 280

(6°, gewijzigd bij art. 27 van de wet van 10.02.2026 (B.S., 27.02.2026). Tekst   (6 van toepassing vanaf 09.03.2026 (art. 33, lid 1))                                ap

Zijn van expeditierecht vrijgesteld:                                             So

1° uitgiften, kopieën of uittreksels van of uit akten, vonnissen en              1° arresten, die krachtens de artikelen 161 en 162 van het recht of van             so de formaliteit der registratie zijn vrijgesteld.                                 de

Deze bepaling is echter niet van toepassing a) op de in artikel 272,             To laatste alinea, bedoelde uitgiften, kopieën of uittreksels; b) op de             co uitgiften, afschriften of uittreksels van of uit de in artikel 162, 5°, 13°,     ex
27° en 33°bis tot 37°bis bedoelde akten en vonnissen;                            16

2° de uitgiften, kopieën of uittreksels van of uit vonnissen, arresten,          2° beschikkingen of andere akten van rechtspleging, die de griffier                 or ambtshalve of op verzoek van een der partijen toezendt aan de                    gr partijen, aan hun advokaten of aan derden, in uitvoering van het                 ré Gerechtelijk Wetboek of van andere wettelijke of reglementaire                   d’ bepalingen.

3° de kopieën van verklaringen met het oog op de inschrijving of tot             3° wijziging van een inschrijving in het rechtspersonenregister van de              in Kruispuntbank van Ondernemingen ambtshalve afgegeven of                          Ba toegezonden aan de personen die de inschrijving of de wijziging                  pe aanvragen; de oorzaak van de vrijstelling moet op het kopie vermeld              do worden;

4° Uitgiften, kopieën of uittreksels uit de registers van de burgerlijke         4 stand of uit de registers welke de akten betreffende het verkrijgen,             ou het herkrijgen, het behoud en het verlies van nationaliteit bevatten.            re

5° de kopieën of uittreksels van vonnissen en arresten die afgeleverd            5° worden aan juridische tijdschriften, aangewezen door de Minister van             pu Financiën;

6° de uitgiften, kopieën of uittreksels afgegeven door de griffie van            6° het Hof van beroep te Brussel, met het oog op de tenuitvoerlegging in            d’ België van de arresten en beschikkingen die een uitvoerbare titel                de uitmaken en gewezen zijn op grond van de Verdragen betreffende de                l'U Europese Unie, betreffende de werking van de Europese unie en tot                ce oprichting van de Europese Gemeenschap voor Atoomenergie, en                     qu welke luidens de bewoordingen van die Verdragen vatbaar zijn voor gedwongen tenuitvoerlegging.

7° de grossen of kopieën, afgeleverd door de griffie van het Hof van               7° beroep te Brussel, met het oog op de erkenning en de                               de tenuitvoerlegging in België van de scheidsrechterlijke beslissingen                Be geveld krachtens het Verdrag inzake de beslechting van geschillen                  po met betrekking tot investeringen tussen Staten en onderdanen van                   Et andere Staten, opgemaakt te Washington op 18 maart 1965.                           19

8° de kopieën in strafzaken, afgeleverd aan de vader of de moeder,                 8° aan een adoptant of aan de voogd in hun hoedanigheid van burgerlijke               ad partij of van persoon die zich op grond van het dossier zou kunnen                 su beroepen op een nadeel, wanneer de zaak betrekking heeft op een                    l'a misdrijf gepleegd tegen een minderjarige en dat naar de wetten                     lo strafbaar is gesteld met een criminele of correctionele straf.

9° de uitvoerbare uitgiften van vonnissen en arresten die aan de                   9° partijen worden verstrekt anders dan krachtens een beschikking van                 dé de voorzitter van de rechtbank als bedoeld in artikel 1379 van het                 pr Gerechtelijk Wetboek.

10° uitgiften, kopieën of uittreksels van een proces-verbaal van                   10 minnelijke schikking bedoeld in artikel 733 van het Gerechtelijk                   co Wetboek en dat plaats heeft gevonden:

a) bij gelegenheid van verrichtingen binnen het kader van de wet van               a) 12 juli 1976 betreffende het herstel van zekere schade veroorzaakt                 12 aan private goederen door natuurrampen of van de overeenkomstige                   à gewestelijke bepalingen;                                                           ré

b) naar aanleiding van schadelijke gebeurtenissen die als een                      b) openbare of landbouwramp worden erkend en waarin het herstel of                    pu de schadeloosstelling wordt geregeld door bijzondere wetten of door                or internationale overeenkomsten.                                                     in

###### Art. 281

(opgeheven bij art. 8 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).        (ab Tekst van toepassing vanaf 01.02.2019 (art. 29))   (1) ap

(…)                                                                                (…
----------                                                                         -- Nota (1) – Overgangsbepaling:                                                      No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in           Le art. 269 , 1 lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht 1   ste ré vanaf hun datums van inwerkingtreding (art. 28).                                   da

###### Art. 282

(opgeheven bij art. 211 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

### HOOFDSTUK III - Diverse bepalingen

###### Art. 283

In de in artikel 160 voorziene gevallen, worden de griffierechten in          Da debet vereffend en ingevorderd volgens de regelen die van                     dé toepassing zijn op de onder dezelfde voorwaarden vereffende                   d’ registratierechten.

###### Art. 284

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst   (m van toepassing vanaf 07.01.2007 (art. -))                                     (M

Worden eveneens in debet vereffend, de griffierechten verschuldigd            So op uitgiften, kopieën van en uittreksels uit akten, vonnissen en              ex arresten, wanneer die stukken in strafzaken worden afgeleverd aan             ce het openbaar ministerie of aan de Rijksagenten belast met de                  au tenuitvoerlegging van vonnissen en arresten.

De rechten worden onder de gerechtskosten begrepen en als                     Le dusdanig ingevorderd ten laste van de partij die er toe veroordeeld           su werd.

###### Art. 284bis

(gewijzigd bij art. 312 van de wet van 27.12.2006 (B.S., 28.12.2006). Tekst   (m van toepassing vanaf 07.01.2007 (art. -))                                     (M

In debet worden eveneens vereffend, de griffierechten verschuldigd            So op de kopieën in strafzaken die worden afgegeven met toepassing               co van de artikelen 674bis en volgende van het Gerechtelijk Wetboek. De          67 rechten    alsmede      de    andere    kosten    worden     ingevorderd      re overeenkomstig de bepalingen van hetzelfde Wetboek.

###### Art. 285

(gewijzigd bij art. 2, nr. 11 van het KB van 20.07.2000 (B.S., 30.08.2000 - ed.        (m 1). Tekst van toepassing vanaf 01.01.2002 (art. 7, § 2), zelf gewijzigd bij art. 42,   Te
5° van het KB van 13.07.2001 (B.S., 11.08.2001 - ed. 1). Tekst van toepassing          42 vanaf 01.01.2002 (art. 45, § 1))                                                       pa

De wijze van heffing der griffierechten en het houden der registers in                 Un de griffies van de hoven en rechtbanken worden bij koninklijk besluit                  la geregeld.

Daarbij kan de medewerking van de griffies bij de heffing van de                       Il p griffierechten worden voorzien, zonder dat zij daardoor de                             gr hoedanigheid van Staatsrekenplichtige verkrijgen.

Inbreuken op de voorschriften van evenbedoeld koninklijk besluit                       Le kunnen worden bestraft met boeten waarvan het bedrag per inbreuk                       ré 250 EUR niet mag te boven gaan.                                                        po

###### Art. 286

(voorlaatste lid vervangen bij art. 37 van de wet van 23.12.1958 (B.S.,                (av 07.01.1959). Tekst van toepassing vanaf 17.01.1959 (art. -))                           07

Er is verjaring:                                                                       Il y

1° Voor het invorderen der griffierechten en -boeten, na twee jaar, te                 1 rekenen van den dag waarop zij aan den Staat verworven zijn;                           de

2° Voor de vordering tot teruggaaf van ten onrechte geheven rechten                    2 en boeten, na twee jaar, te rekenen van den dag der betaling.                          pe

Die verjaringen worden gestuit overeenkomstig artikel 2171 en 2172.                    Ce et

Verjaring voor het invorderen der in debet vereffende rechten                          To ontstaat echter zoals die voor de onder dezelfde voorwaarden                           dé vereffende registratierechten.                                                         m

###### Art. 287

De bepalingen van titel I betreffende de vervolgingen en gedingen en                   So de moratoire interesten, zijn toepasselijk op de griffierechten.                       re

###### Art. 288

(hersteld bij art. 9 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2). Tekst   (ré van toepassing vanaf 01.02.2019 (art. 29))   (1) ap

De Koning kan wat de rolrechten betreft bij een in Ministerraad                    En overlegd besluit de regels bepalen inzake de inning, de                            ét verjaringstermijnen, de wijzen waarop de verjaring wordt gestuit of                rè geschorst, de vervolgingen en gedingen en de moratoire interesten en               d’ daarbij afwijken van de in artikelen 286 en 287 bepaalde regels. De                in besluiten die genomen worden in toepassing van dit artikel, worden                 au bekrachtigd door de wet binnen de 12 maanden volgend op de datum                   ar van hun bekendmaking in het Belgisch Staatsblad.                                   le
----------                                                                         -- Nota (1) – Overgangsbepaling:                                                      No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in           Le art. 269 , 1 lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht 1   ste ré vanaf hun datums van inwerkingtreding (art. 28).                                   da

###### Art. 288bis

(ingevoegd bij art. 10 van de wet van 14.10.2018 (B.S., 20.12.2018 - ed. 2).       (in Tekst van toepassing vanaf 01.02.2019 (art. 29))   (1) ap

De Koning kan bepalen dat wegens de laattijdige betaling van een                   Le rolrecht een administratieve boete zal verschuldigd zijn waarvan het               m bedrag niet minder kan bedragen dan 25 euro en niet hoger mag zijn                 po dan de helft van het recht bepaald in artikel 269 .      1 l’a
----------                                                                         -- Nota (1) – Overgangsbepaling:                                                      No De bepalingen van deze wet zijn van toepassing op de zaken waarvan de in           Le art. 269 , 1 lid, W.Reg. bedoelde inschrijving of herinschrijving wordt verzocht 1   ste ré vanaf hun datums van inwerkingtreding (art. 28).                                   da

TOEKOMSTIG RECHT (vanaf 01.01.2028)

## TITEL IV - DIGITALISATIE VAN DE RELATIES

## TUSSEN DE FEDERALE OVERHEIDSDIENST                                          E

FINANCIËN, DE BURGERS EN BEPAALDE DERDEN

(ingevoegd bij art. 74 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2).       (in Tekst van toepassing voor alle of bepaalde categorieën van houders van een         ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art.      fix 222))

###### Art. 288ter

(ingevoegd bij art. 75 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Voor de toepassing van de bepalingen van dit Wetboek, van de                          Po bijzondere wetsbepalingen met betrekking tot de registratie-,                         lég hypotheek- en griffierechten of van de ter uitvoering ervan genomen                   d'h besluiten, wordt verstaan onder:                                                      en

1° aangetekende zending: hetzij de briefwisseling, al dan niet                        1° vergezeld van een ontvangstbevestiging, neergelegd bij de aanbieder                   ac van de universele postdienst, een aanbieder van postdiensten of een                   un gekwalificeerde verlener van vertrouwensdiensten die voldoet aan de                   se vereisten van artikel 44 van Verordening (EU) nr. 910 /2014 van het                   du Europees Parlement en de Raad van 23 juli 2014 betreffende                            Co elektronische       identificatie      en      vertrouwensdiensten            voor    se elektronische transacties binnen de interne markt en tot intrekking                   m van Richtlijn 1999/93/CE, en al dan niet elektronisch verzonden door                  éle een van hen naar een vooraf aangewezen ontvanger, die toelaat om                      pr de datum van verzending en ontvangst van de briefwisseling door de                    tra bestemmeling aan te tonen, hetzij het bericht dat door de FOD                         m Financiën is verzonden in het kader van de uitoefening van haar taak                  de van openbare dienst door middel van de dienst voor het versturen en                   d' ontvangen        van      elektronische       berichten       door      bepaalde      se vertegenwoordigers door de Federale Overheidsdienst belast met de                     d'A Digitale Agenda en aan houders van een ondernemingsnummer zoals                       qu gedefinieerd in artikel III.16 van het Wetboek van economisch recht of                re aan hun vertegenwoordigers door de Rijksdienst voor Sociale Zekerheid;

2° beveiligd elektronisch platform: elke computertoepassing ter                       2° beschikking gesteld door de Federale Overheidsdienst Financiën of                     fo door een andere openbare instelling in samenwerking met de                            in burgers, bedrijven, rechtspersonen en bepaalde derden elektronische                   de diensten aanbiedt om elektronische berichten uit te wisselen met de                   se authenticatie en identificatie worden uitgevoerd in toepassing van                    l'a hoofdstuk 4 van de wet van 18 juli 2017 inzake elektronische                          ch identificatie door middel van een stelsel voor elektronische                          éle identificatie zoals bedoeld in art. 8., 2., van Verordening (EU) nr.                  à 910/2014 van het Europees Parlement en de Raad van 23 juli 2014                       eu betreffende elektronische identificatie en vertrouwensdiensten voor                   éle elektronische transacties in de interne markt en tot intrekking van                   éle

Richtlijn (EG) 1999/93, dat ten minste een substantieel                               (C veiligheidsniveau in de zin van artikel 8., 2., b) van bovengenoemde                  sé Verordening inzake de integriteit van de inhoud, de tijdsaanduiding, en               l'in zo ook de bewaring van het verzonden bericht garandeert.                              m

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288quater

(ingevoegd bij art. 76 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen                       § anders bepalen, wordt elk bericht aan de Federale Overheidsdienst                     au Financiën dat uitgaat van een natuurlijke persoon die geen houder is                  ém van een ondernemingsnummer, verzonden door middel van een                             d' beveiligd elektronisch platform voor zover hij er expliciet voor gekozen              sé heeft om met de Federale Overheidsdienst Financiën langs                              co elektronische weg te communiceren.                                                    éle

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig                    En het eerste lid, wordt elk bericht onder gesloten omslag verzonden.                    ch

Wanneer het bericht aan de Federale Overheidsdienst Financiën dat                     Lo uitgaat van een burger, natuurlijke persoon, die geen houder is van                   cit een ondernemingsnummer, betrekking heeft op meerdere burgers en                       co niet al deze burgers expliciet gekozen hebben om langs elektronische                  ex weg met de Federale Overheidsdienst Financiën te communiceren,                        Fi wordt het bericht altijd onder gesloten omslag verzonden naar al deze                 so burgers.

De     Koning      bepaalt     de     toepassingsmodaliteiten           van     de    Le uitwisselingsprocedure van berichten via elektronische weg.                           d'

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen                       § anders bepalen, wordt elk bericht van de Federale Overheidsdienst                     au Financiën aan een natuurlijke persoon die geen houder is van een                      tra ondernemingsnummer, verzonden door middel van een beveiligd                           d' elektronisch platform voor zover die er expliciet voor gekozen heeft                  au om met de Federale Overheidsdienst Financiën langs elektronische                      pu weg te communiceren.

Bij het ontbreken van een uitdrukkelijke verklaring overeenkomstig                    En het eerste lid, wordt elk bericht onder gesloten omslag verzonden.                    ch

Wanneer het bericht van de Federale Overheidsdienst Financiën aan                      Lo een burger, natuurlijk persoon, betrekking heeft op meerdere burgers                   pe en niet al deze burgers expliciet gekozen hebben om langs                              pl elektronische weg met de Federale Overheidsdienst Financiën te                         ex communiceren, wordt het bericht altijd onder gesloten omslag                           Fi verzonden naar al deze burgers.                                                        so

§ 3. De keuze van een natuurlijke persoon die geen houder is van een                   § ondernemingsnummer om met de Federale Overheidsdienst                                  nu Financiën langs elektronische weg te communiceren gebeurt door de                      Fi uitdrukkelijke en voorafgaande aanvaarding van het elektronische                       pr communicatieproces met de Federale Overheidsdienst Financiën                           Se door middel van een beveiligd elektronisch platform. Deze                              éle voorafgaande        en      uitdrukkelijke      toestemming            moet    vrij,   êt weloverwogen en ondubbelzinnig zijn. De natuurlijk persoon die geen                    tit houder is van een ondernemingsnummer kan zijn instemming op elk                        to moment intrekken. Het bericht zal dan voor de toekomst onder                           et gesloten omslag worden verstuurd en deze intrekking van toestemming zal onmiddellijk van kracht worden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288quinquies

(ingevoegd bij art. 77 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst     (in van toepassing voor alle of bepaalde categorieën van houders van een                   ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                    d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))    fix

Behoudens indien de wettelijke of reglementaire bepalingen anders                      Sa bepalen, wordt elk bericht aan de Federale Overheidsdienst Financiën                   au dat    uitgaat    van     een     persoon      die    houder      is    van    een     ém ondernemingsnummer, verzonden door middel van een beveiligd                            tra elektronisch platform.

Behoudens indien de wettelijke of reglementaire bepalingen anders                      Sa bepalen, wordt elk bericht van de Federale Overheidsdienst Financiën                   au aan een persoon die houder is van een ondernemingsnummer,                              tra verzonden door middel van een beveiligd elektronisch platform.                         m

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288sexies

(ingevoegd bij art. 78 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst     (in van toepassing voor alle of bepaalde categorieën van houders van een                   ap

ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Behoudens indien de wettelijke of reglementaire bepalingen anders                     Sa bepalen, zal een bericht wanneer dat bericht niet verzonden kan                       au worden door middel van een beveiligd elektronisch platform                            d' ingevolge overmacht, worden verzonden onder gesloten omslag.                          ce

Wanneer een persoon zich niet heeft kunnen identificeren bij een                      Lo beveiligd elektronisch platform omdat het beveiligd elektronisch                      éle platform technisch niet geconfigureerd is om deze persoon toe te                      te staan er verbinding mee te maken, wordt het bericht eveneens onder                    s'y gesloten omslag verzonden.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288septies

(ingevoegd bij art. 79 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

§ 1. Behoudens indien de wettelijke of reglementaire bepalingen                       § anders bepalen, wordt elk bericht door een persoon verzonden door                     au middel van een beveiligd elektronisch platform, onmiddellijk ter                      d' beschikking gesteld op het beveiligd elektronisch platform van de                     di terbeschikkingstelling geldt als datum van de ontvangst van het                       du bericht door de Federale Overheidsdienst Financiën.

Elk bericht door de Federale Overheidsdienst Financiën verzonden                      Ch door middel van een beveiligd elektronisch platform bevat in het                      m opschrift van het bericht op het beveiligd elektronisch platform van de               l'in terbeschikkingstelling van het bericht.                                               m

Behoudens indien de wettelijke of reglementaire bepalingen anders                     Sa bepalen is het, voor elk bericht verzonden of ontvangen door middel                   au van een beveiligd elektronisch platform, de derde werkdag die volgt                   pl op de datum van terbeschikkingstelling in het opschrift van het                       su bericht op het beveiligd elektronisch platform van de Federale                        fig termijnen die van toepassing zijn voor het vervullen van de rechten en                d'a plichten in dit Wetboek, in de bijzondere wetsbepalingen met                          da betrekking tot de registratie-, hypotheek- en griffierechten of van de                re tot uitvoering ervan genomen besluiten.                                               da

Wanneer een bericht wordt verzonden door de Federale                                  Lo platform en wanneer de datum van terbeschikkingstelling van het                       de bericht in het opschrift van het bericht op het beveiligd elektronisch                m platform van de Federale Overheidsdienst Financiën en de datum van                    pu verzending van het bericht verzonden door middel van een beveiligd                    tra elektronisch platform verschillend zijn, zal de datum die het                         di voordeligst is voor de betrokken persoon het vertrekpunt van de                       se termijn zijn.

§ 2. Behoudens indien de wettelijke of reglementaire bepalingen                       § anders bepalen, is het de derde werkdag die volgt op de datum van                     au verzending van het bericht verzonden of ontvangen onder gesloten                      m omslag, die het vertrekpunt zal zijn van de termijnen die van                         de toepassing zijn voor het vervullen van de rechten en plichten in dit                  d'o Wetboek, in de bijzondere wetsbepalingen met betrekking tot de                        lég registratie-, hypotheek- en griffierechten of in de tot uitvoering ervan              d'h genomen besluiten.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288octies

(ingevoegd bij art. 80 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

De rechtsgevolgen van een bericht verzonden door middel van een                       Le beveiligd elektronisch platform of onder gesloten omslag zijn                         pl dezelfde.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288nonies

(ingevoegd bij art. 81 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Wanneer een document elektronisch wordt ondertekend door de                           Lo opsteller of opstellers, gebeurt die ondertekening minstens door                      au middel van een geavanceerde elektronische handtekening in de zin                      m van artikel 3.11. van Verordening (EU) nr. 910/2014 van het Europees                  du

Parlement en de Raad van 23 juli 2014 betreffende elektronische                       Co identificatie en vertrouwensdiensten voor elektronische transacties                   se in de interne markt en tot intrekking van Richtlijn 1999/93/EG.                       m

Wanneer een document elektronisch wordt ondertekend door middel                       Lo van het stelsel voor elektronische identificatie aangemeld door België                éle overeenkomstig artikel 9.1. van de Verordening (EU) nr. 910/2014,                     Rè wordt die ondertekening beschouwd als gekwalificeerd in de zin van                    qu artikel 3.12. van die Verordening.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 288decies

(ingevoegd bij art. 82 van de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst    (in van toepassing voor alle of bepaalde categorieën van houders van een                  ap ondernemingsnummer, evenals voor natuurlijke personen, op een datum                   d’e respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028 (art. 222))   fix

Voor de toepassing van artikelen 288quater tot en met 288nonies,                      Po wordt verstaan onder "bericht": alle schriftelijke mededelingen                       "m betreffende de rechten en plichten opgenomen in dit Wetboek, in de                    et bijzondere wetsbepalingen met betrekking tot de registratie-,                         lég hypotheek- en griffierechten of in de ter uitvoering ervan genomen                    d'h besluiten, inclusief briefwisseling, formulieren en verzendingen van                  ce gegevens, ongeacht de gebruikte drager.                                               in

## GEMEENSCHAPPELIJKE BEPALINGEN VOOR ALLE

## BELASTINGEN

(gewijzigd bij art. 5 van de wet van 17.08.2013 (B.S., 05.09.2013). Tekst van         (m toepassing vanaf 01.01.2013 (art. 21))                                                àp

###### Art. 289

(gewijzigd bij art. 3 van de wet van 14.01.2013 (B.S., 31.01.2013 - ed. 2). Tekst     (m van toepassing vanaf 10.02.2013 (art. -))                                             ap

§ 1. De bestuursdiensten van de Staat, met inbegrip van de parketten                  § en de griffies der hoven en rechtbanken, de besturen van de                           les provinciën en van de gemeenten, zomede de openbare organismen                         et en instellingen, zijn gehouden, wanneer zij daartoe aangezocht zijn                   so door een ambtenaar van een der Rijksbesturen belast met de aanslag                    Ad

in, of de invordering van de belastingen, hem alle in hun bezit zijnde    re inlichtingen te verstrekken, hem, zonder verplaatsing van alle in hun     po bezit zijnde akten, stukken, registers en om 't even welke bescheiden     pi inzage te verlenen en hem alle inlichtingen, afschriften of uittreksels   lai te laten nemen, welke bedoelde ambtenaar ter verzekering van de           fo aanslag in, of de heffing van de door de Staat geheven belastingen        pe nodig acht.

Onder openbare organismen dienen verstaan, naar de geest van deze         Pa wet, de instellingen, maatschappijen, verenigingen, inrichtingen en       in diensten welke de Staat mede beheert, waaraan de Staat een                l’a waarborg verstrekt, op welker bedrijvigheid de Staat toezicht             ga uitoefent of waarvan het bestuurspersoneel aangewezen wordt door          le de regering, op haar voordracht of mits haar goedkeuring.                 pr

Van de akten, stukken, registers, bescheiden of inlichtingen in           To verband met gerechtelijke procedures mag evenwel geen inzage of           re afschrift worden verleend zonder uitdrukkelijke toelating van het         co openbaar ministerie.

Alinea 1 is niet van toepassing op het Bestuur der postchecks, het        L’a Nationaal Instituut voor de statistiek, noch op de kredietinstellingen.   l’In Andere afwijkingen van deze bepaling kunnen worden ingevoerd bij          D’ door de Minister van Financiën medeondertekende koninklijke               de besluiten.

§ 2. Elke inlichting, stuk, proces-verbaal of akte ontdekt of bekomen     § in het uitoefenen van zijn functie, door een ambtenaar van de             ob tussenkomst van een der hierboven aangeduide diensten, kan door           se de Staat ingeroepen worden voor het opsporen van elke krachtens de        re belastingwetten verschuldigde som.

Desondanks kan het aanbieden tot registratie van de processen-            Né verbaal en van de verslagen over expertises betreffende gerechtelijke     de procedures, het bestuur dan alleen toelaten die akten in te roepen        pe mits het daartoe de in alinea 3 van § 1 bepaalde toelating heeft          l’a bekomen.

§ 3. Alle administraties die ressorteren onder de Federale                § toereikende, ter zake dienende en niet overmatige inlichtingen ter        ag beschikking te stellen aan alle ambtenaren van deze Overheidsdienst,      ou voorzover die ambtenaren regelmatig belast zijn met de vestiging of       pe de invordering van de belastingen, en voorzover die gegevens              po bijdragen tot de vervulling van de opdracht van die ambtenaren tot de     re vestiging of de invordering van eender welke door de Staat geheven belasting.

Elke ambtenaar van de Federale Overheidsdienst Financiën, die                     To wettelijk werd belast met een controle- of onderzoeksopdracht, is                 d’ van rechtswege gemachtigd alle toereikende, ter zake dienende en                  pr niet overmatige inlichtingen te vragen, op te zoeken of in te zamelen             pe die bijdragen tot de vestiging of de invordering van eender welke,                ou andere, door de Staat geheven belasting.

TOEKOMSTIG RECHT (vanaf 01.01.2028)

###### Art. 289bis

(§ 12, lid 3, gewijzigd bij art. 83 van de wet van 12.05.2024 (B.S., 30.05.2024   (§ – ed. 2). Tekst van toepassing voor alle of bepaalde categorieën van houders      12 van een ondernemingsnummer, evenals voor natuurlijke personen, op een             ce datum respectievelijk te bepalen door de Koning, en ten laatste op 01.01.2028     pe (art. 222))                                                                       au

§ 1. Dit artikel legt de voorschriften en procedures vast voor de                 § samenwerking tussen België en de andere lidstaten van de Europese                 les Unie met het oog op de uitwisseling van inlichtingen die naar                     eu verwachting van belang zijn voor de administratie en de handhaving                vr van de nationale wetgeving van alle lidstaten met betrekking tot de               de registratie-, hypotheek- en griffierechten.                                       d’

Dit artikel legt tevens de bepalingen vast voor de elektronische                  Le uitwisseling van de in het eerste lid bedoelde inlichtingen.                      l’é éle

Dit artikel laat de toepassing van de regels inzake wederzijdse                   Le rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de                  l’e verplichtingen van de lidstaten inzake ruimere administratieve                    pl samenwerking, welke voortvloeien uit andere rechtsinstrumenten,                   co waaronder bilaterale en multilaterale overeenkomsten.                             in m

§ 2. Voor de toepassing van dit artikel wordt verstaan onder:                     §2

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari               1° 2011 betreffende de administratieve samenwerking op het gebied                    20 van de belastingen en tot intrekking van richtlijn 77/799/EEG;                    et

2° "lidstaat": een lidstaat van de Europese Unie;                                 2°

3° "centraal verbindingsbureau": het bureau dat als zodanig is                    3° aangewezen door de bevoegde autoriteit en belast is met de primaire               te zorg voor de contacten met de andere lidstaten op het gebied van de               co administratieve samenwerking;                                                     co

4° "verbindingsdienst": elk ander bureau dan het centraal                  4° verbindingsbureau dat als zodanig is aangewezen door de bevoegde           lia autoriteit om op grond van dit artikel rechtstreeks inlichtingen uit te    éc wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel       5° gemachtigd is door de bevoegde autoriteit om rechtstreeks                  pa inlichtingen uit te wisselen;                                              en

6° "Belgische bevoegde autoriteit": de door België als zodanig             6° aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de         te Belgische    verbindingsdiensten     en   de    Belgische    bevoegde      lia ambtenaren worden eveneens als Belgische bevoegde autoriteit bij           ég delegatie beschouwd;                                                       dé

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere         7° dan België, als zodanig aangewezen autoriteit. Het centraal                te verbindingsbureau, de verbindingsdiensten en de bevoegde                   lia ambtenaren van deze lidstaat worden eveneens als buitenlandse              Et bevoegde autoriteit bij delegatie beschouwd;                               co

8° "verzoekende autoriteit": het centraal verbindingsbureau, een           8° verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die         lia namens de Belgische of een buitenlandse bevoegde autoriteit om             fo bijstand verzoekt;                                                         be

9° "aangezochte autoriteit": het centraal verbindingsbureau, een           9° verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die          lia namens de Belgische of een buitenlandse bevoegde autoriteit om             un bijstand wordt verzocht;                                                   d’

10° "administratief onderzoek": alle door de lidstaten bij het vervullen   10 van hun taken verrichte controles, onderzoeken en acties ter               vé waarborging van de juiste toepassing van de belastingwetgeving;            de lég

11° "automatische uitwisseling":                                           11

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de        a) systematische mededeling met regelmatige, vooraf vastgestelde              co tussenpozen zonder voorafgaand verzoek van vooraf bepaalde                 de inlichtingen aan een andere lidstaat;                                      pr

b) voor de toepassing van alle andere bepalingen van dit artikel,          b) andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3,        au de systematische mededeling van vooraf bepaalde inlichtingen               co verstrekt overeenkomstig de punten a) en b)                                co

12° "spontane uitwisseling": het niet-systematisch, te eniger tijd en    12 ongevraagd verstrekken van inlichtingen aan een andere lidstaat;         m m

13° "persoon":                                                           13

a. een natuurlijk persoon;                                               a.

b. een rechtspersoon;                                                    b.

c. indien de geldende wetgeving in die mogelijkheid voorziet, een        c. vereniging van personen die bevoegd is rechtshandelingen te              pe verrichten, maar niet de status van rechtspersoon bezit; of              ju

d. een andere juridische constructie, ongeacht de aard of de vorm, met   d. of zonder rechtspersoonlijkheid, die activa, met inbegrip van de         fo daardoor gegenereerde inkomsten, bezit of beheert welke aan              de belastingen in de zin van de richtlijn zijn onderworpen;                 im

14° "langs elektronische weg": door middel van elektronische             14 apparatuur voor gegevensverwerking - met inbegrip van digitale           éle compressie - en gegevensopslag, met gebruikmaking van kabels,            et radio, optische technologie of andere elektromagnetische middelen;       op

15°     "CCN-netwerk":       het    op    het     gemeenschappelijke     15 communicatienetwerk gebaseerde gemeenschappelijke platform dat           co de Europese Unie heeft ontwikkeld voor het elektronische                 po berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied      au van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk          16 akkoord, elke mededeling of enig ander instrument of handeling met       ac soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of           ay hernieuwd, in het kader van een belastingcontrole, en die aan de         re volgende cumulatieve voorwaarden voldoen:                                co

a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht     a) of deze beslissingen effectief gebruikt worden;                          dé

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon       b) of een groep van personen, en voor zover deze persoon of deze groep      gr van personen er zich kan op beroepen;                                    de

c) betreft de interpretatie of toepassing van een wettelijke of          c) administratieve bepaling betreffende de handhaving of de toepassing      lég van dit Wetboek en de met de registratie-, hypotheek- en                 l’a griffierechten verband houdende autonome bepalingen;                     d’

d) heeft betrekking op een grensoverschrijdende verrichting en           d)

e) is tot stand gekomen voorafgaand aan de indiening van een               e) belastingaangifte voor het tijdvak waarin de verrichting of reeks          co verrichtingen of de activiteiten hebben plaatsgevonden.                    d’

17° "grensoverschrijdende verrichting" als vermeld in de bepaling          17 onder 16°: een verrichting of reeks van verrichtingen die voldoen aan      op een of meer van de volgende voorwaarden:                                   co

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van    a) verrichtingen   fiscaal    inwoners    van     België   zijn   dat   de    d’ grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt,      ay gewijzigd of hernieuwd                                                     m

b) waarbij een van de partijen bij de verrichting of reeks van             b) verrichtingen haar fiscale woonplaats tegelijkertijd in meer dan een       d’ rechtsgebied heeft;                                                        sim

c)   de    verrichtingen    of    reeks      van   verrichtingen     een   c) grensoverschrijdend effect hebben.                                         tra

18° "verbonden onderneming", voor de toepassing van paragraaf              18 6/3: een persoon die gelieerd is met een andere persoon op ten             pe minste één van de volgende wijzen:                                         fa

a) een persoon neemt deel aan de leiding van een andere persoon            a) waarbij hij invloed van betekenis kan uitoefenen op die andere             es persoon;

b) een persoon neemt deel aan de zeggenschap over een andere               b) persoon door middel van een deelneming van meer dan 25 % van de            d' stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon           c) door middel van een eigendomsrecht van, rechtstreeks of middellijk,        d' meer dan 25 % van het kapitaal;                                            %

d) een persoon heeft recht op 25 % of meer van de winsten van een          d) andere persoon.                                                            pe

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en         Si met d), aan de leiding van, aan de zeggenschap over of in het kapitaal     au of de winsten van dezelfde persoon, worden alle betrokken personen         les als verbonden ondernemingen beschouwd.                                     as

Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met        Si d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de   la winsten van meer dan één persoon, worden alle betrokken personen           pe als verbonden ondernemingen beschouwd.                                     en

Voor de toepassing van dit punt wordt een persoon die met                    Au betrekking tot de stemrechten of het kapitaalbezit van een entiteit          un samen met een andere persoon optreedt, beschouwd als houder van              dé een deelneming in alle stemrechten of het volledige kapitaalbezit dat        dé die andere persoon in de genoemde entiteit heeft.                            pa

Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c)        En is voldaan door vermenigvuldiging van de deelnemingspercentages              vis door de opeenvolgende niveaus heen. Een persoon die meer dan 50              su % van de stemrechten houdt, wordt geacht 100 % te houden.                    de

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in         Un de rechte lijn worden behandeld als één persoon.                             de pe

19° "gezamenlijke audit": een administratief onderzoek dat                   19 gezamenlijk door de bevoegde autoriteiten van twee of meer                   co lidstaten wordt uitgevoerd, en verband houdt met een of meer                 ou personen van gezamenlijk of complementair belang voor de                     co bevoegde autoriteiten van die lidstaten;                                     Et

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot           20 vernietiging, verlies, wijziging of elk voorval van ongepaste of             en ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen,            oc met inbegrip van, maar niet beperkt tot, persoonsgegevens die                l'u worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg            do van opzettelijke onwettige handelingen, nalatigheid of ongevallen.           au Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid,           d'a de beschikbaarheid en de integriteit van gegevens.                           co

§ 3. De Belgische bevoegde autoriteit wisselt met de buitenlandse            § bevoegde autoriteiten inlichtingen uit.                                      au

§ 4. Met betrekking tot een specifiek geval kan de Belgische bevoegde        § autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de         de eerste § vermelde inlichtingen die deze in haar bezit heeft of naar          to aanleiding van een administratief onderzoek verkregen heeft, te              ao verstrekken. Het verzoek kan een met redenen omkleed verzoek om              co een bepaald administratief onderzoek in te stellen, omvatten.                ad

De Belgische bevoegde autoriteit kan de aangezochte autoriteit               L’a verzoeken haar de originele stukken over te maken.                           de

§ 5. De Belgische bevoegde autoriteit verstrekt op verzoek van een           § buitenlandse bevoegde autoriteit met betrekking tot een specifiek            co geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft   to of naar aanleiding van een administratief onderzoek verkregen heeft,         ob dat werd ingesteld om die inlichtingen te verkrijgen.                        àl

In voorkomend geval deelt de Belgische bevoegde autoriteit de               Le verzoekende autoriteit mee op welke gronden zij een administratief          re onderzoek niet noodzakelijk acht.                                           ad

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten         Po van het gevraagde administratief onderzoek gaat de Belgische                l’e bevoegde autoriteit te werk volgens dezelfde procedures als                 les handelde zij uit eigen beweging of op verzoek van een andere                d’ Belgische instantie.

Op specifiek verzoek van de verzoekende autoriteit verstrekt de             En Belgische bevoegde autoriteit de originele stukken, tenzij de               co Belgische voorschriften zich hiertegen verzetten.                           di

De inlichtingen worden door de Belgische bevoegde autoriteit zo             Le spoedig mogelijk, doch uiterlijk drie maanden na de datum van               le ontvangst van het verzoek verstrekt. Indien de Belgische bevoegde           da autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij    co deze binnen twee maanden. In bijzondere gevallen kunnen de                  co Belgische bevoegde autoriteit en de verzoekende autoriteit een              de andere termijn overeenkomen.                                                co co

De ontvangst van het verzoek wordt door de Belgische bevoegde               L’a autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval      im uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs               éle elektronische weg, bevestigd.                                               ap

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk        L’a een maand na ontvangst van het verzoek, aan de verzoekende                  év autoriteit weten welke tekortkomingen het verzoek vertoont en               éc preciseert welke aanvullende achtergrondinformatie zij verlangt. In         gé dit geval gaan de in het vijfde lid gestelde termijnen in op de datum       Da waarop de Belgische bevoegde autoriteit de aanvullende informatie           l’a ontvangt.                                                                   co

Indien de Belgische bevoegde autoriteit niet binnen de gestelde             Lo termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor          à onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van       im het verzoek, aan de verzoekende autoriteit mee, met vermelding van          la de datum waarop zij meent aan het verzoek te kunnen voldoen. Deze           de termijn mag niet langer zijn dan zes maanden te rekenen vanaf de            ré datum van ontvangst van het verzoek.                                        ré

Indien de Belgische bevoegde autoriteit niet over de gevraagde              Lo inlichtingen beschikt en niet aan het verzoek om inlichtingen kan           de voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt        d’ zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand   el na ontvangst van het verzoek, aan de verzoekende autoriteit mee.            en la

§ 5/1. Wat betreft een in paragraaf 4 en in paragraaf 5 bedoeld           § verzoek worden de verzochte inlichtingen geacht van verwacht              pa belang te zijn indien op het ogenblik van het verzoek de verzoekende      vr autoriteit van oordeel is dat er overeenkomstig haar nationale            de wetgeving een redelijke mogelijkheid bestaat dat de verzochte             lég inlichtingen van belang zullen zijn voor de belastingaangelegenheden      in van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of   d' anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van      au het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen,        Da verstrekt de verzoekende autoriteit ten minste de volgende                in inlichtingen aan de aangezochte autoriteit:                               au

a) het fiscale doel waarvoor de informatie wordt opgevraagd;              a)

b) een specificering van de inlichtingen die nodig zijn voor de           b) uitvoering of handhaving van haar nationale recht.                        àl

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op      § een groep belastingplichtigen die niet individueel kunnen worden          pa geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op          pe basis van een gemeenschappelijke reeks kenmerken.                         dé ca

In dergelijke gevallen, verstrekt de verzoekende autoriteit de            En volgende informatie aan de aangezochte autoriteit:                        in

a) een gedetailleerde beschrijving van de groep;                          a)

b) een toelichting bij de toepasselijke wetgeving en bij de feiten op     b) basis waarvan redelijkerwijze vermoed kan worden dat de                   il e belastingplichtigen in de groep de toepasselijke wetgeving niet           pa hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen         c) zouden bijdragen tot het bepalen van de mate waarin de                    co belastingplichtigen in de groep aan hun verplichtingen voldoen;           gr

d) in voorkomend geval, feiten en omstandigheden die verband              d) houden met de tussenkomst van een derde die actief heeft                  tie bijgedragen tot de mogelijke niet-naleving van de toepasselijke           ap wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse           § bevoegde autoriteit automatisch alle inlichtingen waarover zij ten        co aanzien van ingezetenen van die andere lidstaat beschikt inzake de        to volgende specifieke inkomsten- en vermogenscategorieën, op te             ré vatten in de zin van de Belgische wetgeving:

su be

a) inkomen uit een dienstbetrekking;                                     a)

b) tantièmes en presentiegelden;                                         b)

c) levensverzekeringsproducten die niet vallen onder andere              c) Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch      ju onder soortgelijke voorschriften;                                        m

d) pensioenen;                                                           d)

e) eigendom van en inkomsten uit onroerend goed;                         e)

f) royalty's;                                                            f)

g) inkomsten uit dividenden zonder bewaarneming, met uitzondering        g) van    inkomsten    uit   dividenden    die   zijn   vrijgesteld   van   "n vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn    ex 2011/96/EU van de Raad.                                                  la

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de    Po verstrekking van de in de eerste alinea genoemde inlichtingen het        ce door de lidstaat van verblijf afgegeven fiscaal identificatienummer      pr (TIN) van ingezetenen.                                                   ré

België stelt de Commissie jaarlijks in kennis van ten minste twee        La inkomsten- en vermogenscategorieën die zijn opgenomen in de              de eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over      ali ingezetenen van een andere lidstaat.                                     ré

België stelt de Commissie vóór 1 januari 2026 in kennis van ten          Av minste vijf categorieën die zijn opgenomen in het eerste lid, ten        m aanzien waarvan de bevoegde autoriteit van elke andere lidstaat          co automatisch inlichtingen verstrekt over ingezetenen van die andere       to lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken   au die ingaan op of na 1 januari 2026.                                      im

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen     La zes maanden na het verstrijken van het kalenderjaar in de loop           pa waarvan de inlichtingen beschikbaar zijn geworden.                       de

"Beschikbare inlichtingen" betekent inlichtingen die zich in de          Le belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden     da en die opvraagbaar zijn overeenkomstig de procedures voor het            in verzamelen en verwerken van inlichtingen in die lidstaat.                pr da

§ 6/1. In het kader van de verplichte automatische uitwisseling van          § inlichtingen      over    grensoverschrijdende     voorafgaande    fiscale   d’ beslissingen, zijn de voorwaarden de volgende:                               tra

1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van           1° deze paragraaf, verstrekt de Belgische bevoegde autoriteit                   au automatisch inlichtingen aan de bevoegde autoriteiten van alle               les andere lidstaten en de Europese Commissie, overeenkomstig de                 ex volgens § 24 vastgestelde van toepassing zijnde praktische                   co modaliteiten wanneer een grensoverschrijdende voorafgaande                   ve beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december             tra
2016.                                                                        dé

2°    de      Belgische    bevoegde   autoriteit   verstrekt   eveneens,     2° overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde            co praktische modaliteiten, aan de bevoegde autoriteiten van alle andere        ve lidstaten, evenals aan de Europese Commissie, de inlichtingen over           les grensoverschrijdende voorafgaande fiscale beslissingen die zijn              ex verstrekt, gewijzigd of hernieuwd binnen de periode beginnend vijf           dé jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in        m de bepaling onder 6° van deze paragraaf.                                     an

Indien de grensoverschrijdende voorafgaande fiscale beslissingen             Si werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en            ém 31 december 2013, worden deze inlichtingen verstrekt op                      dé voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.          ce

Als grensoverschrijdende voorafgaande fiscale beslissingen werden            Si verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31                ém december 2016, worden die inlichtingen verstrekt ongeacht of die             dé grensoverschrijdende voorafgaande beslissingen al dan niet nog               dé geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin        3° een voorafgaande grensoverschrijdende ruling betrekking heeft op             an belastingaangelegenheden van een of meer natuurlijke personen,               ex tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1          ph januari 2026 is afgegeven, gewijzigd of hernieuwd, en:                       re

a) het bedrag van de transactie of reeks transacties van de                  a) voorafgaande grensoverschrijdende ruling groter is dan 1.500.000             po euro (of het equivalent daarvan in een andere valuta), indien dat            1. bedrag wordt vermeld in de voorafgaande grensoverschrijdende                 un ruling, of;                                                                  tra

b) de voorafgaande grensoverschrijdende ruling bepaalt of een                b) persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de        un ruling afgeeft.                                                              la

Voor de toepassing van punt a), en onverminderd het in de                 Au voorafgaande grensoverschrijdende ruling bedoelde bedrag, omvat           fis het bedrag van de voorafgaande grensoverschrijdende ruling bij een        d'o reeks transacties met betrekking tot verschillende goederen,              m diensten of activa, de totale onderliggende waarde. De bedragen           la worden niet geaggregeerd indien dezelfde goederen, diensten of            m activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande             No grensoverschrijdende rulings inzake bronbelasting op inkomsten uit        fis arbeid, tantièmes en presentiegelden of pensioenen van niet-              pe ingezetenen niet onder de uitwisseling van inlichtingen over              l'im voorafgaande grensoverschrijdende rulings met betrekking tot              ta natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:                  4°

a) voor de op grond van 1° uitgewisselde inlichtingen: onverwijld         a) zodra de voorafgaande grensoverschrijdende rulings of voorafgaande        ap verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of            fis hernieuwd en uiterlijk binnen drie maanden na het einde van het           pr semester     van   het   kalenderjaar    waarin    de      voorafgaande   ap grensoverschrijdende           rulings        of           voorafgaande   fis verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of            en hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde             b) inlichtingen: vóór 1 januari 2018.                                        le

5° De door de Belgische bevoegde autoriteit uit hoofde van de             5° bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen     co omvatten de volgende gegevens:                                            élé

a) de identificatie van de rechtspersoon, tenzij de voorafgaande          a) grensoverschrijdende ruling betrekking heeft op een natuurlijke           fis persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt,         ph en in voorkomend geval de groep personen waartoe die persoon              éc behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende              b) ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen          ou een omschrijving van de relevante zakelijke activiteiten of transacties   de of reeks van transacties, alsook alle andere inlichtingen die voor de     d'o bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een           l'a mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking       lie van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een         pr fabrieks- of handelswerkwijze, of van inlichtingen waarvan het            di verstrekken in strijd zou zijn met de openbare orde.

c) de data van de aflevering, wijziging of hernieuwing van de                 c) grensoverschrijdende voorafgaande fiscale beslissing;                         la

d) de aanvangsdatum van de geldigheidsperiode van de                          d) grensoverschrijdende    voorafgaande       fiscale    beslissing,    indien   an vermeld;

e)   de    einddatum     van     de     geldigheidsperiode      van      de   e) grensoverschrijdende    voorafgaande       fiscale    beslissing,    indien   an vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;             f)

g) het bedrag van de verrichting of reeks van verrichtingen van de            g) grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld          po in de grensoverschrijdende voorafgaande fiscale beslissing;                   m tra

h) in voorkomend geval, de identificatie van de andere lidstaten die          h) mogelijks betrokken zijn bij de grensoverschrijdende voorafgaande             se fiscale beslissing;                                                           en

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling          i) betrekking heeft op een natuurlijke persoon en overeenkomstig de              to bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die       m er zijn, waarop de voorafgaande grensoverschrijdende ruling of de             co voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van           co invloed zal zijn waarbij vermeld dient te worden met welke lidstaten          ou de getroffen personen verbonden zijn, en                                      qu

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a), b), en i) van       6° deze paragraaf worden niet medegedeeld aan de Europese                        ne Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de             7° inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel         po en in elk geval niet later dan zeven werkdagen na ontvangst, aan de           lu verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing           se totdat het in § 24, 3    de en 4de lid, bedoelde gegevensbestand          ré operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met               8° inachtneming van de bepalingen van § 24, 2 lid, om aanvullende de ég inlichtingen verzoeken, daaronder begrepen de volledige tekst van             co een grensoverschrijdende voorafgaande fiscale beslissing.                     an

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen,          Po bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van           ce

het eerste lid het fiscaal identificatienummer van de rijksinwoner dat       et werd afgeleverd door rechtsgebied van verblijf.                              ré

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan        §6 de commissie mee de statistieken over het volume van de                      un automatische uitwisseling in toepassing van de paragrafen 6 en 6/1,          au alsook de inlichtingen over de kosten en baten, administratief en            in andere, verbonden aan de uitwisseling die plaats heeft gevonden, en          au aan de eventuele wijzigingen, zowel voor de belastingadministraties          les als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle             L'a relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie   in van de administratieve samenwerking voorzien door dit artikel in het         la licht van de strijd tegen de fiscale fraude en ontduiking.                   de

De Belgische bevoegde autoriteit controleert en evalueert de                 L'a efficiëntie van de administratieve samenwerking voorzien door dit            co artikel, met name wat betreft de strijd tegen de belastingontduiking         po en deelt de Commissie de resultaten van zijn evaluatie een maal per          Co jaar mee via een formulier en volgens de modaliteiten voorzien door          du de Commissie.

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde         § lid bedoelde termijn de in tweede lid bedoelde gegevens inzake               l'a grensoverschrijdende constructies, waarvan zij ingelicht is door de          tra intermediair of de relevante belastingplichtige overeenkomstig de            co artikelen 289bis/1 tot en met 289bis/8, via automatische uitwisseling        28 mee aan de bevoegde autoriteiten van alle andere lidstaten.                  co

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid       Le mee te delen gegevens zijn de volgende, voor zover van toepassing:           co

1° de identificatiegegevens van intermediairs, en relevante                  1° belastingplichtigen, bedoeld in artikel 289bis/1, 4° en 5°, met              vis uitzondering van intermediairs die op grond van het juridisch                di beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig          so artikel 289bis/7, met inbegrip van hun naam, geboortedatum en -              le plaats (in het geval van een natuurlijk persoon), fiscale woonplaats,        ré fiscaal identificatienummer, en, in voorkomend geval, van de                 les personen die overeenkomstig paragraaf 2, 21° een verbonden                   en onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in                  2° artikel 289bis/2 op grond waarvan de grensoverschrijdende                    28 constructie gemeld moet worden;                                              d'

3° een samenvatting van de inhoud van de meldingsplichtige                   3° grensoverschrijdende constructie, met onder meer de benaming                 l'o waaronder zij algemeen bekend staat, indien voorhanden, en een               pa

beschrijving van de relevante constructies, alsook alle andere             de inlichtingen die voor de bevoegde autoriteit van belang kunnen zijn bij    su het beoordelen van een mogelijk belastingrisico, die niet mag leiden       po tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of         in beroepsgeheim of een fabrieks- of handelswerkwijze, of van                 d' inlichtingen waarvan de onthulling in strijd zou zijn met de openbare orde;

4° de datum waarop de eerste stap voor de implementatie van de             4° meldingsplichtige grensoverschrijdende constructie is of zal worden        di ondernomen;                                                                ac

5° nadere bijzonderheden van de nationale bepalingen die aan de            5° meldingsplichtige grensoverschrijdende constructie ten grondslag           les liggen;                                                                    d'

6° de waarde van de meldingsplichtige grensoverschrijdende                 6° constructie;                                                               dé

7° de lidstaat van de relevante belastingbetaler(s) en eventuele           7° andere lidstaten waarop de meldingsplichtige grensoverschrijdende          co constructie naar alle waarschijnlijkheid van invloed zal zijn;             co dé

8° de identificatiegegevens van andere personen in een lidstaat, op        8° wie de meldingsplichtige grensoverschrijdende constructie naar alle        su waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met         fa welke lidstaten deze personen verbonden zijn.                              ce

De automatische uitwisseling geschiedt binnen één maand te                 L'é rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn       co verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020      ét meegedeeld.                                                                31

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze           Le paragraaf, worden niet medegedeeld aan de Europese Commissie.              pa

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028,       Po bevat     de   mededeling    van    de   gegevens      betreffende    de   ce grensoverschrijdende regelingen het fiscaal identificatienummer van        tra de personen bepaald in het tweede lid, 8°.                                 pe

§ 7. De Belgische bevoegde autoriteit verstrekt spontaan, in elk van       § de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de       sp buitenlandse bevoegde autoriteit:                                          vis

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen          1° dat in de andere lidstaat een derving van belasting kan bestaan;           ex

2° een belastingplichtige verkrijgt in België een vrijstelling of        2° vermindering van belasting die voor hem een belastingplicht of een       ex hogere belasting in de andere lidstaat zou moeten meebrengen;            au ou

3° transacties tussen een belastingplichtige in België en een            3° belastingplichtige in een andere lidstaat worden over één of meer        d’ andere landen geleid, op zodanige wijze dat daardoor in één van beide    m of in beide lidstaten een belastingbesparing kan ontstaan;               l’u

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen        4° dat er belastingbesparing kan ontstaan door een kunstmatige              ex verschuiving van winsten binnen een groep van ondernemingen;             fic

5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen       5° door een buitenlandse bevoegde autoriteit, hebben informatie             co opgeleverd die voor de vaststelling van de belastingschuld in die        in andere lidstaat toereikend, ter zake dienend en niet overmatig is.       l’é

De Belgische bevoegde autoriteit kan een buitenlandse bevoegde           L’a autoriteit spontaan alle inlichtingen meedelen waarvan zij kennis        au heeft en die voor deze buitenlandse bevoegde autoriteit toereikend,      co ter zake dienend en niet overmatig zijn.                                 ce

De in het eerste lid bedoelde inlichtingen worden door de Belgische      L’a bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand      l’a nadat deze beschikbaar worden, aan de buitenlandse bevoegde              Et autoriteit van elke betrokken lidstaat verstrekt.                        m

§ 8. De ontvangst van de in § 7 bedoelde inlichtingen wordt door de      §8 Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen        § zeven werkdagen na ontvangst, indien mogelijk langs elektronische        éle weg, aan de verstrekkende buitenlandse bevoegde autoriteit               co bevestigd.                                                               se

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in   §
§ 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde      co autoriteit verzoeken dat door eerstgenoemde gemachtigde                  ét ambtenaren onder de voorwaarden die zijn vastgesteld door de             co buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren     1° waar de administratieve autoriteiten van de lidstaat taken vervullen;    où tâ

2° aanwezig zijn bij administratieve onderzoeken die worden              2° uitgevoerd op het grondgebied van de buitenlandse bevoegde               l'a autoriteit;

3° deelnemen aan de administratieve onderzoeken die worden               3° uitgevoerd op het grondgebied van de andere lidstaat, met                de gebruikmaking     van      elektronische   communicatiemiddelen,    in   éle voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren              Da aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen      au door middel van elektronische communicatiemiddelen, kunnen zij           m personen      ondervragen     en   bescheiden   onderzoeken,     onder   pe voorbehoud van de door de buitenlandse bevoegde autoriteit               de gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde              § inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische    co bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde         co ambtenaren onder de voorwaarden die zijn vastgesteld door de             so Belgische bevoegde autoriteit mogen:

1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn   1° taken vervult;                                                           ex

2° aanwezig zijn bij administratieve onderzoeken die worden              2° uitgevoerd op Belgisch grondgebied;                                      be

3° deelnemen aan de administratieve onderzoeken die worden               3° uitgevoerd op Belgisch grondgebied, met gebruikmaking van                be elektronische communicatiemiddelen, in voorkomend geval.                 éc

De Belgische bevoegde autoriteit antwoordt op het overeenkomstig         L'a de eerste alinea ingediende verzoek binnen een termijn van 60 dagen      co na ontvangst van het verzoek, om haar instemming te bevestigen of        ré haar gemotiveerde weigering aan de buitenlandse bevoegde                 àl autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden             Lo waartoe de ambtenaren van de Belgische bevoegde autoriteit               au toegang hebben, ontvangen de ambtenaren van de verzoekende               les autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn            Da tijdens een administratief onderzoek of daaraan deelnemen met            au gebruikmaking van elektronische communicatiemiddelen, mogen zij          m personen ondervragen en bescheiden onderzoeken, onder de                 pe voorwaarden die zijn vastgesteld door de Belgische bevoegde              de autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking          To heeft, om de controlemaatregelen van de ambtenaren van de                co verzoekende autoriteit na te leven, wordt door de Belgische bevoegde     re re

autoriteit beschouwd als een weigering tegenover haar eigen ambtenaren.

De door de verzoekende lidstaat gemachtigde ambtenaren die              Le overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds    Be een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en     de hun officiële hoedanigheid worden vermeld.                              of

§ 11. In de gevallen waarin België met één of meer lidstaten            § overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of   m meer personen te wier aanzien zij een gezamenlijk of complementair      co belang hebben, controles te verrichten en de aldus verkregen            pr inlichtingen uit te wisselen, is deze § van toepassing.                 d’

De Belgische bevoegde autoriteit bepaalt autonoom welke personen        L’a zij voor een gelijktijdige controle wil voorstellen. Zij deelt de       pe buitenlandse bevoegde autoriteit van de betrokken lidstaten met         sim opgave van redenen mee welke dossiers zij voor een gelijktijdige        m controle voorstelt. Zij bepaalt binnen welke termijn de controle moet   un plaatsvinden.                                                           leq

Wanneer aan de Belgische bevoegde autoriteit een gelijktijdige          Lo controle wordt voorgesteld, beslist zij of ze aan de gelijktijdige      be controle wenst deel te nemen. Zij doet de buitenlandse bevoegde         El autoriteit die de controle voorstelt een bevestiging van deelname of    pr een gemotiveerde weigering toekomen binnen een termijn van 60           dé dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan        L’a die wordt belast met de leiding en de coördinatie van de controle.      su

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de         § Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit      pe te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het    co verzoek om een gezamenlijke audit binnen een termijn van 60 dagen,      de te rekenen vanaf de ontvangst van het verzoek en motiveert haar         ré beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en                  Le gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd       pr door de bevoegde autoriteit van de verzoekende lidstaat, door de        lin Belgische bevoegde autoriteit, en in voorkomend geval, door de          pa bevoegde autoriteiten van de andere aangezochte lidstaten en in         co overeenstemming met de Belgische wetgeving en procedurele               la voorschriften. De Belgische bevoegde autoriteit wijst een               co vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en   de de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die              Le deelnemen aan de gezamenlijke audit op Belgisch grondgebied,            pa

worden vastgesteld overeenkomstig de Belgische wetgeving. Tegelijk        co met het naleven van die wetgeving, oefenen de ambtenaren van een          lég andere lidstaat geen bevoegdheden uit die verder zouden gaan dan          au de bevoegdheden die hun krachtens de wetgeving van hun lidstaat           la zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de         Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op           vis Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die         d'a deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd       co om personen te ondervragen en bescheiden te onderzoeken in                do samenspraak met de ambtenaren van de Belgische bevoegde                   co autoriteit, met inachtneming van de in België bepaalde procedurele        en regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de         Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op           vis Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de              pr activiteiten van de gezamenlijke audit is verzameld, worden               év beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde              m juridische voorwaarden als in het geval van een klassieke audit,          ca uitgevoerd in België door Belgische ambtenaren, onder meer in de          fo loop van een bezwaar-, herzienings- of beroepsprocedures.                 ré

Onverminderd het tweede en derde lid en voor de toepassing van de         Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op           vis Belgisch grondgebied, genieten personen die aan een gezamenlijke          fa audit worden onderworpen of erdoor worden geraakt, dezelfde               de rechten en hebben ze dezelfde plichten als in het geval van een           s'a klassieke audit waaraan alleen Belgische ambtenaren deelnemen,            av onder meer in de loop van een bezwaar-, herzienings- of                   co beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van     Lo een of meer lidstaten een gezamenlijke audit verrichten, trachten zij     de het eens te worden over de feiten en omstandigheden die relevant          s'e zijn voor de gezamenlijke audit, en streven zij naar overeenstemming      le over de fiscale positie van de geaudite persoon of personen op basis      fis van de resultaten van de gezamenlijke audit. De bevindingen van de        de gezamenlijke audit worden neergelegd in een eindverslag. Punten           in waarover de bevoegde autoriteiten het eens zijn, worden in de             au conclusies van het eindverslag opgenomen en worden in aanmerking          ra genomen in de relevante instrumenten die de bevoegde autoriteiten         ap van de deelnemende lidstaten naar aanleiding van die gezamenlijke         pa audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het       La resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het   ré eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.        da

§ 11/2. De Belgische bevoegde autoriteit kan de bevoegde autoriteit      § van een andere of meerdere lidstaten verzoeken een gezamenlijke          co audit uit te voeren.                                                     co

Gezamenlijke audits worden op vooraf overeengekomen en                   Le gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd        pr door de betrokken bevoegde autoriteiten, en in overeenstemming           lin met de wetgeving en de procedurele voorschriften van de lidstaat         co waar de activiteiten van de gezamenlijke audit plaatsvinden.             m

De rechten en plichten van de Belgische ambtenaren die deelnemen         Le aan de gezamenlijke audit op het grondgebied van een andere              co lidstaat, worden vastgesteld overeenkomstig de wetgeving van die         dé lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de        en Belgische ambtenaren geen bevoegdheden uit die verder zouden             au gaan dan de bevoegdheden die hun krachtens de Belgische                  la wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de        Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het      vis grondgebied van een andere lidstaat, kan het bewijsmateriaal dat         élé tijdens de activiteiten van de gezamenlijke audit is verzameld, worden   co beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde             da juridische voorwaarden als in het geval van een klassieke audit          da uitgevoerd in België door Belgische ambtenaren.                          fo

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van    Lo een of meerdere andere lidstaten een gezamenlijke audit verrichten,      de trachten zij het eens te worden over de feiten en omstandigheden die     s'e relevant zijn voor de gezamenlijke audit, en streven zij naar            le overeenstemming over de fiscale positie van de geaudite persoon of       fis personen op basis van de resultaten van de gezamenlijke audit. De        de bevindingen van de gezamenlijke audit worden neergelegd in een           in eindverslag. De punten waarover de bevoegde autoriteiten het eens        au zijn, worden in de conclusies van het eindverslag opgenomen en           ra worden in aanmerking genomen in de relevante instrumenten die de         ap bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding       pa van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het         La resultaat van de gezamenlijke audit en krijgen een kopie van het         ré eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.       da

§ 12. De Belgische bevoegde autoriteit kan een verzoek aan een           § buitenlandse bevoegde autoriteit richten tot kennisgeving aan de         co geadresseerde, overeenkomstig de in de aangezochte lidstaat              ré geldende voorschriften voor de kennisgeving van soortgelijke akten,      m van alle door de Belgische administratieve overheden afgegeven           ém akten en besluiten die betrekking hebben op de toepassing in België      l’a van wetgeving betreffende registratie-, hypotheek- en griffierechten.    d’

Het verzoek tot kennisgeving vermeldt de naam en het adres van de         La geadresseerde, evenals alle overige informatie ter identificatie van de   ain geadresseerde, en het onderwerp van de akte of het besluit waarvan        id de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde             L’a autoriteit slechts gedaan indien de kennisgeving van de akten niet        qu volgens de Belgische regels kan geschieden, of buitensporige              rè problemen zou veroorzaken. De Belgische bevoegde autoriteit kan           di een document, met een aangetekende zending of langs elektronische         no weg, rechtstreeks ter kennis brengen aan een persoon op het               éle grondgebied van een andere lidstaat.                                      au

§ 13. Op verzoek van een buitenlandse bevoegde autoriteit gaat de         § Belgische bevoegde autoriteit, overeenkomstig de Belgische                co voorschriften voor de kennisgeving van soortgelijke akten, over tot       be kennisgeving aan de geadresseerde van alle door de administratieve        de overheden van de verzoekende lidstaat afgegeven akten en besluiten        m die betrekking hebben op de toepassing op haar grondgebied van            lég wetgeving betreffende registratie-, hypotheek- en griffierechten.         gr

De Belgische bevoegde autoriteit stelt de verzoekende autoriteit          L’a onverwijld in kennis van het aan het verzoek gegeven gevolg en, in het    re bijzonder, van de datum waarop de akte of het besluit aan de              de geadresseerde ter kennis is gebracht.

§ 14. Indien een buitenlandse bevoegde autoriteit inlichtingen            § overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding                  in betreffende   de    ontvangen     inlichtingen   verzoekt,   doet   de    d’ ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen         les aan de Belgische voorschriften inzake beroepsgeheim en                    pr gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie             à maanden nadat het resultaat van het gebruik van de verlangde              ra inlichtingen bekend is, een terugmelding aan de buitenlandse              de bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar,                   L’a overeenkomstig bilateraal overeengekomen praktische afspraken,            m een terugmelding over de automatische inlichtingenuitwisseling naar       au de betrokken lidstaten.                                                   bi

§ 15. De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7       § inlichtingen heeft verstrekt, kan de ontvangende buitenlandse             in bevoegde autoriteit om terugmelding betreffende de ontvangen              co inlichtingen verzoeken.                                                   re

§ 16. De Belgische verbindingsdienst of de Belgische bevoegde             § ambtenaar die een verzoek om samenwerking ontvangt dat een                co optreden vereist buiten de hem krachtens de Belgische wetgeving of        pa

het Belgische beleid verleende bevoegdheid, geeft het verzoek                lég onmiddellijk door aan het Belgisch centraal verbindingsbureau en             bu stelt de verzoekende buitenlandse bevoegde autoriteit hiervan in             ét kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat      co het verzoek aan het Belgisch centraal verbindingsbureau is                   bu doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in                 §1 enigerlei     vorm    of   volgens    dit   artikel,   vallen   onder   de   qu geheimhoudingsplicht en genieten de bescherming waarin het                   co nationale recht van de ontvangende lidstaat met betrekking tot               à soortgelijke inlichtingen voorziet.                                          m

Deze inlichtingen mogen worden gebruikt:                                     Ce

1° voor de vaststelling, de toepassing en de handhaving van het              1° nationale recht met betrekking tot de in artikel 2 van de richtlijn          lég bedoelde belastingen, alsmede de btw, andere indirecte belastingen,          vis douanerechten, de bestrijding van het witwassen van geld en van de           in financiering van terrorisme;                                                 ca

2° voor de vestiging en de invordering van de andere belastingen en          2° rechten met betrekking tot artikel 3 van de wet van 9 januari 2012           re houdende omzetting van Richtlijn 2010/24/EU van de Raad van 16               di maart 2010 betreffende de wederzijdse bijstand inzake de                     l'a invordering van schuldvorderingen die voortvloeien uit belastingen,          re rechten en andere maatregelen, en voor het vestigen en invorderen            et van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures           3° die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op         en de fiscale wetgeving, onverminderd algemene regels en wettelijke             lég bepalingen die de rechten van beklaagden en getuigen in het kader            de van dergelijke procedures beheersen.                                         té

Met de toestemming van de buitenlandse bevoegde autoriteit die de            Av inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor            co zover dat toegelaten is door de Belgische wetgeving, kunnen de               au ontvangen inlichtingen en documenten ontvangen van deze autoriteit           et worden gebruikt voor andere doeleinden dan deze bedoeld in het               au tweede lid.

De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en            L'a documenten zonder de in de derde lid van deze paragraaf bedoelde             re toestemming ook gebruiken voor elk doel dat onder een op artikel 215         pr van het Verdrag betreffende de werking van de Europese Unie                  l'a gebaseerde handeling valt en deze daartoe delen met de bevoegde              les autoriteit die verantwoordelijk is voor beperkende maatregelen in de         m betrokken lidstaat.

De Belgische bevoegde autoriteit die van oordeel is dat de van de             Lo bevoegde autoriteit van een andere lidstaat verkregen inlichtingen de         qu bevoegde autoriteit van een derde lidstaat van nut kunnen zijn voor           su de in het tweede lid beoogde doelen, mag de inlichtingen aan deze             m autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit            ce van de inlichtingen verstrekkende lidstaat in kennis stelt van haar           l'E voornemen om die inlichtingen met een derde lidstaat te delen en op           co voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel           co vastgelegde regels en procedures. De inlichtingen verstrekkende               ar lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na        da de datum van ontvangst van de kennisgeving van de lidstaat die de             de inlichtingen wenst te delen.

§ 18. De Belgische bevoegde autoriteit kan het gebruik toestaan van           § de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in        l’E de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid,             co bedoelde doeleinden. De Belgische bevoegde autoriteit verleent                § toestemming indien de inlichtingen in België voor soortgelijke                co doeleinden kunnen worden gebruikt.                                            sim

De Belgische bevoegde autoriteit deelt aan de bevoegde autoriteiten           L'a van alle andere lidstaten een lijst mee van andere dan in paragraaf 1         de bedoelde doeleinden waarvoor overeenkomstig haar nationale recht,             ce de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde             dr autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen          L'a inlichtingen en bescheiden zonder de in het eerste lid bedoelde               pe toestemming gebruiken voor alle doeleinden die de Belgische                   l'a bevoegde autoriteit heeft opgenoemd.                                          l'a

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de            L’a in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit           in België die door een buitenlandse bevoegde autoriteit aan een                  un buitenlandse bevoegde autoriteit van een derde lidstaat werden                pr doorgegeven, in die derde lidstaat toestaan.                                  fin

§ 19. Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht        § de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit      l’a alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan           ha aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te          ob komen.                                                                        ré

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde             L’a autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op             ét voorwaarde dat de buitenlandse bevoegde autoriteit eerst de                   co inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in   d’ de gegeven omstandigheden kon aanspreken zonder dat het                       in beoogde resultaat in het gedrang dreigt te komen.                             re

§ 20. Het is de Belgische bevoegde autoriteit niet toegelaten                 § onderzoek in te stellen of inlichtingen te verstrekken wanneer de             de

Belgische wetgeving haar niet toestaat voor eigen doeleinden het          ré onderzoek in te stellen of de gevraagde inlichtingen te verzamelen.       qu lég

De Belgische bevoegde autoriteit kan weigeren inlichtingen te             L’a verstrekken indien:                                                       in

1° de verzoekende lidstaat, op juridische gronden, soortgelijke           1° inlichtingen niet kan verstrekken;                                        ju

2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-,      2° nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze,       pr of indien het inlichtingen betreft waarvan de onthulling in strijd zou    di zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee      L’a op welke gronden zij het verzoek om inlichtingen afwijst.                 du

§ 21. De Belgische bevoegde autoriteit wendt de middelen aan              § waarover zij beschikt om de gevraagde inlichtingen te verzamelen,         co zelfs indien zij de inlichtingen niet voor eigen belastingdoeleinden      de nodig heeft. Deze verplichting geldt onverminderd § 20, eerste en         se tweede lid, die, wanneer er een beroep op wordt gedaan, in geen geval     du zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te        ca verstrekken uitsluitend omdat België geen binnenlands belang bij          fo deze inlichtingen heeft.                                                  pr

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat   Le de Belgische bevoegde autoriteit kan weigeren inlichtingen te             in verstrekken, uitsluitend op grond dat deze berusten bij een bank, een     fo andere financiële instelling, een gevolmachtigde of een persoon die       dé als vertegenwoordiger of trustee optreedt, of dat zij betrekking          m hebben op eigendomsbelangen in een persoon.                               ou pe

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit          No weigeren de gevraagde inlichtingen toe te zenden indien deze              tra betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de      su toezending van de inlichtingen geweigerd had kunnen worden op             tra grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom     l’a was verzocht vóór 11 maart 2011.                                          de

§ 22. Indien de Belgische overheid voorziet in een samenwerking met       § een derde land welke verder reikt dan de bij de richtlijn geregelde       pl samenwerking, kan de Belgische overheid de verderreikende                 ce samenwerking niet weigeren aan een andere lidstaat die met haar           pr deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken         § die zijn ingediend op grond van § 4, alsook de antwoorden op grond        in

van § 5, de ontvangstbevestigingen, de verzoeken om inlichtingen van     ac algemene aard en de verklaringen van ongeschiktheid of weigering         gé krachtens § 5 worden, voor zover mogelijk, overgemaakt door middel       da van een door de Commissie goedgekeurd standaardformulier. Er             ad mogen rapporten, certificaten en andere bescheiden, of andere voor       ac eensluidend verklaarde afschriften of uittreksels daarvan bij de         do standaardformulieren gevoegd worden.                                     de

De in het eerste lid bedoelde standaardformulieren bevatten ten          Le minste de volgende gegevens, die de verzoekende autoriteit moet          in verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle    a) is ingesteld en, in het geval van vragen betreffende een groep zoals     en bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;          §5

b) het fiscale doel van de gevraagde informatie.                         b)

De Belgische bevoegde autoriteit kan, voor zover bekend en in            L'a overeenstemming met de ontwikkeling van de internationale situatie,      et de namen en adressen verstrekken van alle personen van wie er            les redenen zijn om aan te nemen dat ze in het bezit zijn van de gevraagde   qu informatie, alsook alle elementen die het verzamelen van informatie      to door de aangezochte autoriteit kunnen vergemakkelijken.                  l'a

De    spontane     gegevensuitwisseling    en      de   desbetreffende   Le ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8,          les verzoeken tot administratieve kennisgeving op grond van §§ 12 en         de 13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op          d' grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden       §§ overgemaakt door middel van de door de Commissie goedgekeurde            fo standaardformulieren.

De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1     Le wordt verricht in een geautomatiseerd standaardformaat dat               so ontworpen is om die automatische uitwisseling te vergemakkelijken        fa en dat is goedgekeurd door de Commissie.

§ 24. De krachtens dit artikel verstrekte inlichtingen worden voor       §2 zover mogelijk verzonden langs elektronische weg, via het CCN-           da netwerk.                                                                 du

Het verzoek om samenwerking, waaronder het verzoek tot                   Le kennisgeving en de bijgevoegde bescheiden kunnen in elke door de         no aangezochte en de verzoekende autoriteit overeengekomen taal zijn        lan gesteld. Slechts in bijzondere gevallen en mits het verzoek met          re redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken       tra het verzoek vergezeld te laten gaan van een vertaling in één van de      de officiële talen van België.                                              m

Om te voldoen aan de automatische uitwisseling als bedoeld in § 6/1,      Af
1° en 2°, te verstrekken inlichtingen, worden de gegevens die             le moeten worden meegedeeld opgeslagen in een beveiligd centraal             co gegevensbestand betreffende de administratieve samenwerking op            de belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter             da beschikking gesteld door de Commissie uiterlijk op 31 december            dé
2017. De Belgische bevoegde autoriteiten hebben toegang tot de in         be dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand                  Av operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde             l’é automatische uitwisseling van gegevens, volgens lid 1 van deze            co paragraaf en de toepasselijke praktische modaliteiten.                    m

§ 25. De Belgische bevoegde autoriteit die van een derde land             § inlichtingen ontvangt welke naar verwachting van belang zijn voor         l’a haar administratie en de handhaving van de Belgische wetgeving            dr betreffende registratie-, hypotheek- en griffierechten, kan deze          co inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten        de van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan    l’a elke buitenlandse bevoegde autoriteit die erom verzoekt, mits dat         de krachtens een overeenkomst met dat derde land is toegestaan.              et

De Belgische bevoegde autoriteit kan, met inachtneming van de wet         L’a van 8 december 1992 tot bescherming van de persoonlijke                   dé levenssfeer ten opzichte van de verwerking van persoonsgegevens           tra en de wet van 3 augustus 2012 houdende bepalingen betreffende de          20 verwerking van persoonsgegevens door de Federale Overheidsdienst          ca Financiën in het kader van zijn opdrachten, de overeenkomstig dit         da artikel ontvangen inlichtingen doorgeven aan een derde land, op           in voorwaarde dat aan elk van de volgende voorwaarden is voldaan:            qu

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de         a) inlichtingen afkomstig zijn, heeft daarin toegestemd;                     les

b) het derde land heeft zich ertoe verbonden de medewerking te            b) verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent        élé het ongeoorloofde of onwettige karakter van verrichtingen die blijken     pa in strijd te zijn met of een misbruik te vormen van de                    fis belastingwetgeving.

§   26.   Rapporterende     financiële   instellingen,   intermediairs,   § rapporterende platformexploitanten en de Belgische bevoegde               op autoriteit worden als verwerkingsverantwoordelijken beschouwd             so wanneer zij, alleen of gezamenlijk, de doelen en middelen van de          ag verwerking van persoonsgegevens bepalen in de zin van Verordening         m (EU) 2016/679 van het Europees Parlement en de Raad van 27 april          rè 2016 betreffende de bescherming van natuurlijke personen in               av verband met de verwerking van persoonsgegevens en betreffende             tra de

het vrije verkeer van die gegevens en tot intrekking van Richtlijn
95/46/EG.

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in                         L'a kennis van elke gegevensinbreuk                           en alle daaropvolgende          vio corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen                     L'a met de lidstaat of de lidstaten waar de gegevensinbreuk heeft                             d' plaatsgevonden, schorsen door de Commissie en de betrokken                                ou lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een                      Co dergelijke schorsing wordt onmiddellijk van kracht.                                       su

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de                          En Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de                      àu Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van                    m de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn,                     l'a indien de gegevensinbreuk niet onmiddellijk en op passende wijze                          de onder controle kan worden gebracht. Op een dergelijk verzoek schorst                      ap de Commissie de toegang van die lidstaat of lidstaten tot het CCN-                        l'a netwerk voor de toepassing van de richtlijn.                                              au

De Belgische bevoegde autoriteit stelt, in geval van een                                  L'a gegevensinbreuk, de Commissie op de hoogte wanneer zij deze                               la inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie                        pl verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is                           eu verholpen, geeft de Commissie pas na die verificatie de betrokken                         Co lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de                         m toepassing van de richtlijn.                                                              ef

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in                       Da het centrale gegevensbestand of het CCN-netwerk plaatsvindt die                           ce nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen                        lo door de lidstaten via het CCN-netwerk, stelt de Commissie de                              ré lidstaten       zonder       onnodige         vertraging      in    kennis     van   de   sa gegevensinbreuk en van eventuele corrigerende maatregelen die zijn                        de genomen. Zulke corrigerende maatregelen kunnen inhouden dat de                            co toegang tot het centrale gegevensbestand of het CCN-netwerk voor                          ré de toepassing van de richtlijn wordt geschorst totdat de                                  vio gegevensinbreuk is verholpen.
----------                                                                                -- Nota:                                                                                     No - in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.                         -d - in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.                               -d - in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.              -d - in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.

###### Art. 289bis

(§§ 6, 6/1, 6/2, 6/3, gewijzigd en § 17, vervangen bij art. 28 van de wet van    (§§ 16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))   16

§ 1. Dit artikel legt de voorschriften en procedures vast voor de                § samenwerking tussen België en de andere lidstaten van de Europese                les Unie met het oog op de uitwisseling van inlichtingen die naar                    eu verwachting van belang zijn voor de administratie en de handhaving               vr van de nationale wetgeving van alle lidstaten met betrekking tot de              de registratie-, hypotheek- en griffierechten.                                      d’

Dit artikel legt tevens de bepalingen vast voor de elektronische                 Le uitwisseling van de in het eerste lid bedoelde inlichtingen.                     l’é éle

Dit artikel laat de toepassing van de regels inzake wederzijdse                  Le rechtshulp in strafzaken onverlet. Zij laat eveneens onverlet de                 l’e verplichtingen van de lidstaten inzake ruimere administratieve                   pl samenwerking, welke voortvloeien uit andere rechtsinstrumenten,                  co waaronder bilaterale en multilaterale overeenkomsten.                            in m

§ 2. Voor de toepassing van dit artikel wordt verstaan onder:                    §2

1° "richtlijn": de richtlijn 2011/16/EU van de Raad van 15 februari              1° 2011 betreffende de administratieve samenwerking op het gebied                   20 van de belastingen en tot intrekking van richtlijn 77/799/EEG;                   et

2° "lidstaat": een lidstaat van de Europese Unie;                                2°

3° "centraal verbindingsbureau": het bureau dat als zodanig is                   3° aangewezen door de bevoegde autoriteit en belast is met de primaire              te zorg voor de contacten met de andere lidstaten op het gebied van de              co administratieve samenwerking;                                                    co

4° "verbindingsdienst": elk ander bureau dan het centraal                        4° verbindingsbureau dat als zodanig is aangewezen door de bevoegde                 lia autoriteit om op grond van dit artikel rechtstreeks inlichtingen uit te          éc wisselen;

5° "bevoegde ambtenaar": elke ambtenaar die op grond van dit artikel             5° gemachtigd is door de bevoegde autoriteit om rechtstreeks                        pa inlichtingen uit te wisselen;                                                    en

6° "Belgische bevoegde autoriteit": de door België als zodanig                   6° aangewezen autoriteit. Het Belgisch centraal verbindingsbureau, de               te Belgische     verbindingsdiensten       en    de     Belgische     bevoegde      lia

ambtenaren worden eveneens als Belgische bevoegde autoriteit bij           ég delegatie beschouwd;                                                       dé

7° "buitenlandse bevoegde autoriteit": de door een lidstaat andere         7° dan België, als zodanig aangewezen autoriteit. Het centraal                te verbindingsbureau, de verbindingsdiensten en de bevoegde                   lia ambtenaren van deze lidstaat worden eveneens als buitenlandse              Et bevoegde autoriteit bij delegatie beschouwd;                               co

8° "verzoekende autoriteit": het centraal verbindingsbureau, een           8° verbindingsdienst, of elke bevoegde ambtenaar van een lidstaat die         lia namens de Belgische of een buitenlandse bevoegde autoriteit om             fo bijstand verzoekt;                                                         be

9° "aangezochte autoriteit": het centraal verbindingsbureau, een           9° verbindingsdienst of elke bevoegde ambtenaar van een lidstaat die          lia namens de Belgische of een buitenlandse bevoegde autoriteit om             un bijstand wordt verzocht;                                                   d’

10° "administratief onderzoek": alle door de lidstaten bij het vervullen   10 van hun taken verrichte controles, onderzoeken en acties ter               vé waarborging van de juiste toepassing van de belastingwetgeving;            de lég

11° "automatische uitwisseling":                                           11

a) voor de toepassing van paragrafen 6, eerste lid, 6/1, en 6/3, de        a) systematische mededeling met regelmatige, vooraf vastgestelde              co tussenpozen zonder voorafgaand verzoek van vooraf bepaalde                 de inlichtingen aan een andere lidstaat;                                      pr

b) voor de toepassing van alle andere bepalingen van dit artikel,          b) andere dan deze van voormelde paragrafen 6, eerste lid, 6/1 en 6/3,        au de systematische mededeling van vooraf bepaalde inlichtingen               co verstrekt overeenkomstig de punten a) en b)                                co

12° "spontane uitwisseling": het niet-systematisch, te eniger tijd en      12 ongevraagd verstrekken van inlichtingen aan een andere lidstaat;           m m

13° "persoon":                                                             13

a. een natuurlijk persoon;                                                 a.

b. een rechtspersoon;                                                      b.

c. indien de geldende wetgeving in die mogelijkheid voorziet, een          c. vereniging van personen die bevoegd is rechtshandelingen te                pe verrichten, maar niet de status van rechtspersoon bezit; of                ju

d. een andere juridische constructie, ongeacht de aard of de vorm, met    d. of zonder rechtspersoonlijkheid, die activa, met inbegrip van de          fo daardoor gegenereerde inkomsten, bezit of beheert welke aan               de belastingen in de zin van de richtlijn zijn onderworpen;                  im

14° "langs elektronische weg": door middel van elektronische              14 apparatuur voor gegevensverwerking - met inbegrip van digitale            éle compressie - en gegevensopslag, met gebruikmaking van kabels,             et radio, optische technologie of andere elektromagnetische middelen;        op

15°     "CCN-netwerk":       het    op     het    gemeenschappelijke      15 communicatienetwerk gebaseerde gemeenschappelijke platform dat            co de Europese Unie heeft ontwikkeld voor het elektronische                  po berichtenverkeer tussen autoriteiten die bevoegd zijn op het gebied       au van douane en belastingen.

16° "grensoverschrijdende voorafgaande fiscale beslissing": elk           16 akkoord, elke mededeling of enig ander instrument of handeling met        ac soortgelijke effecten, inbegrepen deze verstrekt, gewijzigd of            ay hernieuwd, in het kader van een belastingcontrole, en die aan de          re volgende cumulatieve voorwaarden voldoen:                                 co

a) verstrekt, gewijzigd of hernieuwd door de FOD Financiën, ongeacht      a) of deze beslissingen effectief gebruikt worden;                           dé

b) verstrekt, gewijzigd of hernieuwd, voor een welbepaalde persoon        b) of een groep van personen, en voor zover deze persoon of deze groep       gr van personen er zich kan op beroepen;                                     de

c) betreft de interpretatie of toepassing van een wettelijke of           c) administratieve bepaling betreffende de handhaving of de toepassing       lég van dit Wetboek en de met de registratie-, hypotheek- en                  l’a griffierechten verband houdende autonome bepalingen;                      d’

d) heeft betrekking op een grensoverschrijdende verrichting en            d)

e) is tot stand gekomen voorafgaand aan de indiening van een              e) belastingaangifte voor het tijdvak waarin de verrichting of reeks         co verrichtingen of de activiteiten hebben plaatsgevonden.                   d’

17° "grensoverschrijdende verrichting" als vermeld in de bepaling         17 onder 16°: een verrichting of reeks van verrichtingen die voldoen aan     op een of meer van de volgende voorwaarden:                                  co

a) waarbij niet alle partijen betrokken bij de verrichting of reeks van   a) verrichtingen   fiscaal   inwoners       van   België   zijn   dat   de   d’ grensoverschrijdende voorafgaande fiscale beslissing heeft verstrekt,     ay gewijzigd of hernieuwd                                                    m

b) waarbij een van de partijen bij de verrichting of reeks van             b) verrichtingen haar fiscale woonplaats tegelijkertijd in meer dan een       d’ rechtsgebied heeft;                                                        sim

c)   de    verrichtingen    of    reeks    van    verrichtingen     een    c) grensoverschrijdend effect hebben.                                         tra

18° "verbonden onderneming", voor de toepassing van paragraaf              18 6/3: een persoon die gelieerd is met een andere persoon op ten             pe minste één van de volgende wijzen:                                         fa

a) een persoon neemt deel aan de leiding van een andere persoon            a) waarbij hij invloed van betekenis kan uitoefenen op die andere             es persoon;

b) een persoon neemt deel aan de zeggenschap over een andere               b) persoon door middel van een deelneming van meer dan 25 % van de            d' stemrechten;

c) een persoon neemt deel in het kapitaal van een andere persoon           c) door middel van een eigendomsrecht van, rechtstreeks of middellijk,        d' meer dan 25 % van het kapitaal;                                            %

d) een persoon heeft recht op 25 % of meer van de winsten van een          d) andere persoon.                                                            pe

Indien meer dan één persoon deelneemt, als bedoeld onder a) tot en         Si met d), aan de leiding van, aan de zeggenschap over of in het kapitaal     au of de winsten van dezelfde persoon, worden alle betrokken personen         les als verbonden ondernemingen beschouwd.                                     as

Indien dezelfde personen deelnemen, als bedoeld onder a) tot en met        Si d), aan de leiding van, aan de zeggenschap over of in het kapitaal of de   la winsten van meer dan één persoon, worden alle betrokken personen           pe als verbonden ondernemingen beschouwd.                                     en

Voor de toepassing van dit punt wordt een persoon die met                  Au betrekking tot de stemrechten of het kapitaalbezit van een entiteit        un samen met een andere persoon optreedt, beschouwd als houder van            dé een deelneming in alle stemrechten of het volledige kapitaalbezit dat      dé die andere persoon in de genoemde entiteit heeft.                          pa

Bij middellijke deelneming wordt vastgesteld of aan de eisen onder c)      En is voldaan door vermenigvuldiging van de deelnemingspercentages            vis door de opeenvolgende niveaus heen. Een persoon die meer dan 50            su % van de stemrechten houdt, wordt geacht 100 % te houden.                  de

Een natuurlijk persoon, zijn of haar echtgenoot en bloedverwanten in       Un de rechte lijn worden behandeld als één persoon.                           de pe

19° "gezamenlijke audit": een administratief onderzoek dat                   19 gezamenlijk door de bevoegde autoriteiten van twee of meer                   co lidstaten wordt uitgevoerd, en verband houdt met een of meer                 ou personen van gezamenlijk of complementair belang voor de                     co bevoegde autoriteiten van die lidstaten;                                     Et

20° "gegevensinbreuk": een inbreuk op de beveiliging die leidt tot           20 vernietiging, verlies, wijziging of elk voorval van ongepaste of             en ongeoorloofde inzage, openbaarmaking of gebruik van inlichtingen,            oc met inbegrip van, maar niet beperkt tot, persoonsgegevens die                l'u worden doorgegeven, opgeslagen of anderszins verwerkt, als gevolg            do van opzettelijke onwettige handelingen, nalatigheid of ongevallen.           au Een gegevensinbreuk kan betrekking hebben op de vertrouwelijkheid,           d'a de beschikbaarheid en de integriteit van gegevens.                           co

§ 3. De Belgische bevoegde autoriteit wisselt met de buitenlandse            § bevoegde autoriteiten inlichtingen uit.                                      au

§ 4. Met betrekking tot een specifiek geval kan de Belgische bevoegde        § autoriteit een buitenlandse bevoegde autoriteit verzoeken alle in de         de eerste § vermelde inlichtingen die deze in haar bezit heeft of naar          to aanleiding van een administratief onderzoek verkregen heeft, te              ao verstrekken. Het verzoek kan een met redenen omkleed verzoek om              co een bepaald administratief onderzoek in te stellen, omvatten.                ad

De Belgische bevoegde autoriteit kan de aangezochte autoriteit               L’a verzoeken haar de originele stukken over te maken.                           de

§ 5. De Belgische bevoegde autoriteit verstrekt op verzoek van een           § buitenlandse bevoegde autoriteit met betrekking tot een specifiek            co geval alle in de eerste § vermelde inlichtingen die ze in haar bezit heeft   to of naar aanleiding van een administratief onderzoek verkregen heeft,         ob dat werd ingesteld om die inlichtingen te verkrijgen.                        àl

In voorkomend geval deelt de Belgische bevoegde autoriteit de                Le verzoekende autoriteit mee op welke gronden zij een administratief           re onderzoek niet noodzakelijk acht.                                            ad

Voor het verkrijgen van de gevraagde inlichtingen of het verrichten          Po van het gevraagde administratief onderzoek gaat de Belgische                 l’e bevoegde autoriteit te werk volgens dezelfde procedures als                  les handelde zij uit eigen beweging of op verzoek van een andere                 d’ Belgische instantie.

Op specifiek verzoek van de verzoekende autoriteit verstrekt de              En Belgische bevoegde autoriteit de originele stukken, tenzij de                co Belgische voorschriften zich hiertegen verzetten.                            di

De inlichtingen worden door de Belgische bevoegde autoriteit zo             Le spoedig mogelijk, doch uiterlijk drie maanden na de datum van               le ontvangst van het verzoek verstrekt. Indien de Belgische bevoegde           da autoriteit evenwel de inlichtingen al in haar bezit heeft, verstrekt zij    co deze binnen twee maanden. In bijzondere gevallen kunnen de                  co Belgische bevoegde autoriteit en de verzoekende autoriteit een              de andere termijn overeenkomen.                                                co co

De ontvangst van het verzoek wordt door de Belgische bevoegde               L’a autoriteit aan de verzoekende autoriteit onmiddellijk, en in elk geval      im uiterlijk zeven werkdagen na ontvangst, indien mogelijk langs               éle elektronische weg, bevestigd.                                               ap

De Belgische bevoegde autoriteit laat in voorkomend geval, uiterlijk        L’a een maand na ontvangst van het verzoek, aan de verzoekende                  év autoriteit weten welke tekortkomingen het verzoek vertoont en               éc preciseert welke aanvullende achtergrondinformatie zij verlangt. In         gé dit geval gaan de in het vijfde lid gestelde termijnen in op de datum       Da waarop de Belgische bevoegde autoriteit de aanvullende informatie           l’a ontvangt.                                                                   co

Indien de Belgische bevoegde autoriteit niet binnen de gestelde             Lo termijn aan het verzoek kan voldoen, deelt zij de redenen hiervoor          à onmiddellijk, en in elk geval uiterlijk drie maanden na ontvangst van       im het verzoek, aan de verzoekende autoriteit mee, met vermelding van          la de datum waarop zij meent aan het verzoek te kunnen voldoen. Deze           de termijn mag niet langer zijn dan zes maanden te rekenen vanaf de            ré datum van ontvangst van het verzoek.                                        ré

Indien de Belgische bevoegde autoriteit niet over de gevraagde              Lo inlichtingen beschikt en niet aan het verzoek om inlichtingen kan           de voldoen of het verzoek om de in § 20 genoemde redenen afwijst, deelt        d’ zij de redenen hiervoor onmiddellijk, en in elk geval uiterlijk een maand   el na ontvangst van het verzoek, aan de verzoekende autoriteit mee.            en la

§ 5/1. Wat betreft een in paragraaf 4 en in paragraaf 5 bedoeld             § verzoek worden de verzochte inlichtingen geacht van verwacht                pa belang te zijn indien op het ogenblik van het verzoek de verzoekende        vr autoriteit van oordeel is dat er overeenkomstig haar nationale              de wetgeving een redelijke mogelijkheid bestaat dat de verzochte               lég inlichtingen van belang zullen zijn voor de belastingaangelegenheden        in van één of meer belastingplichtigen, hetzij bij naam geïdentificeerd of     d' anderszins, en het verzoek gerechtvaardigd is voor de doeleinden van        au het onderzoek.

Om het verwacht belang van de verzochte inlichtingen aan te tonen,          Da verstrekt de verzoekende autoriteit ten minste de volgende                  in inlichtingen aan de aangezochte autoriteit:                                 au

a) het fiscale doel waarvoor de informatie wordt opgevraagd;            a)

b) een specificering van de inlichtingen die nodig zijn voor de         b) uitvoering of handhaving van haar nationale recht.                      àl

§ 5/2. Een in § 4 en in § 5 bedoeld verzoek kan betrekking hebben op    § een groep belastingplichtigen die niet individueel kunnen worden        pa geïdentificeerd, maar die uitsluitend kunnen worden aangeduid op        pe basis van een gemeenschappelijke reeks kenmerken.                       dé ca

In dergelijke gevallen, verstrekt de verzoekende autoriteit de          En volgende informatie aan de aangezochte autoriteit:                      in

a) een gedetailleerde beschrijving van de groep;                        a)

b) een toelichting bij de toepasselijke wetgeving en bij de feiten op   b) basis waarvan redelijkerwijze vermoed kan worden dat de                 il e belastingplichtigen in de groep de toepasselijke wetgeving niet         pa hebben nageleefd;

c) een toelichting bij de manier waarop de gevraagde inlichtingen       c) zouden bijdragen tot het bepalen van de mate waarin de                  co belastingplichtigen in de groep aan hun verplichtingen voldoen;         gr

d) in voorkomend geval, feiten en omstandigheden die verband            d) houden met de tussenkomst van een derde die actief heeft                tie bijgedragen tot de mogelijke niet-naleving van de toepasselijke         ap wetgeving door de belastingplichtigen in de groep.

§ 6. De Belgische bevoegde autoriteit verstrekt de buitenlandse         § bevoegde autoriteit automatisch alle inlichtingen waarover zij ten      co aanzien van ingezetenen van die andere lidstaat beschikt inzake de      to volgende specifieke inkomsten- en vermogenscategorieën, op te           ré vatten in de zin van de Belgische wetgeving:                            su be

a) inkomen uit een dienstbetrekking;                                    a)

b) tantièmes en presentiegelden;                                        b)

c) levensverzekeringsproducten die niet vallen onder andere             c) Unierechtsinstrumenten inzake de uitwisseling van inlichtingen noch     ju onder soortgelijke voorschriften;                                       m

d) pensioenen;                                                          d)

e) eigendom van en inkomsten uit onroerend goed;                        e)

f) royalty's;                                                                     f)

g) inkomsten uit dividenden zonder bewaarneming, met uitzondering                 g) van     inkomsten       uit   dividenden   die     zijn   vrijgesteld     van     "n vennootschapsbelasting overeenkomstig artikel 4, 5 of 6 van Richtlijn             ex 2011/96/EU van de Raad.                                                           la

Voor belastingtijdvakken die ingaan op of na 1 januari 2024, omvat de             Po verstrekking van de in de eerste alinea genoemde inlichtingen het                 ce door de lidstaat van verblijf afgegeven fiscaal identificatienummer               pr (TIN) van ingezetenen.                                                            ré

België stelt de Commissie jaarlijks in kennis van ten minste twee                 La inkomsten- en vermogenscategorieën die zijn opgenomen in de                       de eerste alinea ten aanzien waarvan zij inlichtingen verstrekken over               ali ingezetenen van een andere lidstaat.                                              ré

België stelt de Commissie vóór 1 januari 2026 in kennis van ten                   Av minste vijf categorieën die zijn opgenomen in het eerste lid, ten                 m aanzien waarvan de bevoegde autoriteit van elke andere lidstaat                   co automatisch inlichtingen verstrekt over ingezetenen van die andere                to lidstaat. Deze inlichtingen hebben betrekking op belastbare tijdperken            au die ingaan op of na 1 januari 2026.                                               im

De inlichtingen worden ten minste eenmaal per jaar verstrekt, binnen              La zes maanden na het verstrijken van het kalenderjaar in de loop                    pa waarvan de inlichtingen beschikbaar zijn geworden.                                de

"Beschikbare inlichtingen" betekent inlichtingen die zich in de                   Le belastingdossiers van de inlichtingenverstrekkende lidstaat bevinden              da en die opvraagbaar zijn overeenkomstig de procedures voor het                     in verzamelen en verwerken van inlichtingen in die lidstaat.                         pr da

§ 6/1. In het kader van de verplichte automatische uitwisseling van               § inlichtingen    over     grensoverschrijdende      voorafgaande         fiscale   d’ beslissingen, zijn de voorwaarden de volgende:                                    tra

1° uitgezonderd in de gevallen bedoeld in de bepaling onder 6° van                1° deze paragraaf, verstrekt de Belgische bevoegde autoriteit                        au automatisch inlichtingen aan de bevoegde autoriteiten van alle                    les andere lidstaten en de Europese Commissie, overeenkomstig de                      ex volgens § 24 vastgestelde van toepassing zijnde praktische                        co modaliteiten wanneer een grensoverschrijdende voorafgaande                        ve beslissing werd verstrekt, gewijzigd of hernieuwd na 31 december                  tra
2016.                                                                             dé

2°    de    Belgische     bevoegde    autoriteit    verstrekt    eveneens,        2° overeenkomstig de volgens § 24 vastgestelde van toepassing zijnde                 co praktische modaliteiten, aan de bevoegde autoriteiten van alle andere             ve

lidstaten, evenals aan de Europese Commissie, de inlichtingen over      les grensoverschrijdende voorafgaande fiscale beslissingen die zijn         ex verstrekt, gewijzigd of hernieuwd binnen de periode beginnend vijf      dé jaar vóór 1 januari 2017, met uitzondering van de gevallen bedoeld in   m de bepaling onder 6° van deze paragraaf.                                an

Indien de grensoverschrijdende voorafgaande fiscale beslissingen        Si werden verstrekt, gewijzigd of hernieuwd tussen 1 januari 2012 en       ém 31 december 2013, worden deze inlichtingen verstrekt op                 dé voorwaarde dat die beslissingen nog geldig waren op 1 januari 2014.     ce

Als grensoverschrijdende voorafgaande fiscale beslissingen werden       Si verstrekt, gewijzigd of hernieuwd tussen 1 januari 2014 en 31           ém december 2016, worden die inlichtingen verstrekt ongeacht of die        dé grensoverschrijdende voorafgaande beslissingen al dan niet nog          dé geldig zijn.

3° De bepalingen 1° en 2° zijn niet van toepassing in gevallen waarin   3° een voorafgaande grensoverschrijdende ruling betrekking heeft op        an belastingaangelegenheden van een of meer natuurlijke personen,          ex tenzij een dergelijke voorafgaande grensoverschrijdende ruling na 1     ph januari 2026 is afgegeven, gewijzigd of hernieuwd, en:                  re

a) het bedrag van de transactie of reeks transacties van de             a) voorafgaande grensoverschrijdende ruling groter is dan 1.500.000        po euro (of het equivalent daarvan in een andere valuta), indien dat       1. bedrag wordt vermeld in de voorafgaande grensoverschrijdende            un ruling, of;                                                             tra

b) de voorafgaande grensoverschrijdende ruling bepaalt of een           b) persoon al dan niet fiscaal ingezetene is van het rechtsgebied dat de   un ruling afgeeft.                                                         la

Voor de toepassing van punt a), en onverminderd het in de               Au voorafgaande grensoverschrijdende ruling bedoelde bedrag, omvat         fis het bedrag van de voorafgaande grensoverschrijdende ruling bij een      d'o reeks transacties met betrekking tot verschillende goederen,            m diensten of activa, de totale onderliggende waarde. De bedragen         la worden niet geaggregeerd indien dezelfde goederen, diensten of          m activa meerdere malen worden verhandeld.

Niettegenstaande het bepaalde in punt b), vallen voorafgaande           No grensoverschrijdende rulings inzake bronbelasting op inkomsten uit      fis arbeid, tantièmes en presentiegelden of pensioenen van niet-            pe ingezetenen niet onder de uitwisseling van inlichtingen over            l'im voorafgaande grensoverschrijdende rulings met betrekking tot            ta natuurlijke personen.

4° De uitwisseling van inlichtingen geschiedt als volgt:                4°

a) voor de op grond van 1° uitgewisselde inlichtingen: onverwijld             a) zodra de voorafgaande grensoverschrijdende rulings of voorafgaande            ap verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of                fis hernieuwd en uiterlijk binnen drie maanden na het einde van het               pr semester     van   het   kalenderjaar      waarin     de   voorafgaande       ap grensoverschrijdende           rulings          of         voorafgaande       fis verrekenprijsafspraken zijn afgegeven of gemaakt, gewijzigd of                en hernieuwd.

b) voor de overeenkomstig de bepaling onder 2°, uitgewisselde                 b) inlichtingen: vóór 1 januari 2018.                                            le

5° De door de Belgische bevoegde autoriteit uit hoofde van de                 5° bepalingen onder 1° en 2° van dit artikel te verstrekken inlichtingen         co omvatten de volgende gegevens:                                                élé

a) de identificatie van de rechtspersoon, tenzij de voorafgaande              a) grensoverschrijdende ruling betrekking heeft op een natuurlijke               fis persoon en overeenkomstig de bepalingen 1° en 4° wordt verstrekt,             ph en in voorkomend geval de groep personen waartoe die persoon                  éc behoort;

b) een samenvatting van de voorafgaande grensoverschrijdende                  b) ruling of voorafgaande verrekenprijsafspraak, daaronder begrepen              ou een omschrijving van de relevante zakelijke activiteiten of transacties       de of reeks van transacties, alsook alle andere inlichtingen die voor de         d'o bevoegde autoriteit nuttig kunnen zijn bij de evaluatie van een               l'a mogelijk belastingrisico, die niet mag leiden tot de openbaarmaking           lie van een handels-, bedrijfs-, nijverheids- of beroepsgeheim of een             pr fabrieks- of handelswerkwijze, of van inlichtingen waarvan het                di verstrekken in strijd zou zijn met de openbare orde.

c) de data van de aflevering, wijziging of hernieuwing van de                 c) grensoverschrijdende voorafgaande fiscale beslissing;                         la

d) de aanvangsdatum van de geldigheidsperiode van de                          d) grensoverschrijdende     voorafgaande       fiscale   beslissing,    indien   an vermeld;

e)   de    einddatum     van    de       geldigheidsperiode     van      de   e) grensoverschrijdende     voorafgaande       fiscale   beslissing,    indien   an vermeld;

f) het type grensoverschrijdende voorafgaande fiscale beslissing;             f)

g) het bedrag van de verrichting of reeks van verrichtingen van de            g) grensoverschrijdende voorafgaande fiscale beslissing, indien vermeld          po in de grensoverschrijdende voorafgaande fiscale beslissing;                   m tra

h) in voorkomend geval, de identificatie van de andere lidstaten die         h) mogelijks betrokken zijn bij de grensoverschrijdende voorafgaande            se fiscale beslissing;                                                          en

i) rechtpersonen, tenzij de voorafgaande grensoverschrijdende ruling         i) betrekking heeft op een natuurlijke persoon en overeenkomstig de             to bepalingen 1° en 4° wordt verstrekt, in de andere lidstaten, indien die      m er zijn, waarop de voorafgaande grensoverschrijdende ruling of de            co voorafgaande verrekenprijsafspraak naar alle waarschijnlijkheid van          co invloed zal zijn waarbij vermeld dient te worden met welke lidstaten         ou de getroffen personen verbonden zijn, en                                     qu

6° Inlichtingen gedefinieerd in de bepaling onder 5°, a), b), en i) van      6° deze paragraaf worden niet medegedeeld aan de Europese                       ne Commissie.

7° De Belgische bevoegde autoriteit bevestigt de ontvangst van de            7° inlichtingen, indien mogelijk langs elektronische weg, zonder uitstel        po en in elk geval niet later dan zeven werkdagen na ontvangst, aan de          lu verstrekkende bevoegde autoriteit. Deze maatregel is van toepassing          se totdat het in § 24, 3     de en 4de lid, bedoelde gegevensbestand        ré operationeel wordt.

8° De Belgische bevoegde overheid kan overeenkomstig § 4 en met              8° inachtneming van de bepalingen van § 24, 2de lid, om aanvullende             ég inlichtingen verzoeken, daaronder begrepen de volledige tekst van            co een grensoverschrijdende voorafgaande fiscale beslissing.                    an

Voor de belastbare tijdperken die op of na 1 januari 2028 aanvangen,         Po bevat de mededeling van de inlichtingen vermeld in 6°, a) en k) van          ce het eerste lid het fiscaal identificatienummer van de rijksinwoner dat       et werd afgeleverd door rechtsgebied van verblijf.                              ré

§ 6/2. De Belgische bevoegde autoriteit deelt op jaarlijkse basis aan        §6 de commissie mee de statistieken over het volume van de                      un automatische uitwisseling in toepassing van de paragrafen 6 en 6/1,          au alsook de inlichtingen over de kosten en baten, administratief en            in andere, verbonden aan de uitwisseling die plaats heeft gevonden, en          au aan de eventuele wijzigingen, zowel voor de belastingadministraties          les als voor derden.

De Belgische bevoegde autoriteit deelt aan de Commissie mee alle             L'a relevante inlichtingen die nodig zijn voor de evaluatie van de efficiëntie   in van de administratieve samenwerking voorzien door dit artikel in het         la licht van de strijd tegen de fiscale fraude en ontduiking.                   de

De Belgische bevoegde autoriteit controleert en evalueert de                 L'a efficiëntie van de administratieve samenwerking voorzien door dit            co artikel, met name wat betreft de strijd tegen de belastingontduiking         po

en deelt de Commissie de resultaten van zijn evaluatie een maal per       Co jaar mee via een formulier en volgens de modaliteiten voorzien door       du de Commissie.

§ 6/3. De Belgische bevoegde autoriteit deelt binnen de in het derde      § lid bedoelde termijn de in tweede lid bedoelde gegevens inzake            l'a grensoverschrijdende constructies, waarvan zij ingelicht is door de       tra intermediair of de relevante belastingplichtige overeenkomstig de         co artikelen 289bis/1 tot en met 289bis/8, via automatische uitwisseling     28 mee aan de bevoegde autoriteiten van alle andere lidstaten.               co

De door de Belgische bevoegde autoriteit uit hoofde van het eerste lid    Le mee te delen gegevens zijn de volgende, voor zover van toepassing:        co

1° de identificatiegegevens van intermediairs, en relevante               1° belastingplichtigen, bedoeld in artikel 289bis/1, 4° en 5°, met           vis uitzondering van intermediairs die op grond van het juridisch             di beroepsgeheim van de meldingsplicht vrijgesteld zijn overeenkomstig       so artikel 289bis/7, met inbegrip van hun naam, geboortedatum en -           le plaats (in het geval van een natuurlijk persoon), fiscale woonplaats,     ré fiscaal identificatienummer, en, in voorkomend geval, van de              les personen die overeenkomstig paragraaf 2, 21° een verbonden                en onderneming vormen met de relevante belastingplichtige;

2° nadere bijzonderheden over de wezenskenmerken bedoeld in               2° artikel 289bis/2 op grond waarvan de grensoverschrijdende                 28 constructie gemeld moet worden;                                           d'

3° een samenvatting van de inhoud van de meldingsplichtige                3° grensoverschrijdende constructie, met onder meer de benaming              l'o waaronder zij algemeen bekend staat, indien voorhanden, en een            pa beschrijving van de relevante constructies, alsook alle andere            de inlichtingen die voor de bevoegde autoriteit van belang kunnen zijn bij   su het beoordelen van een mogelijk belastingrisico, die niet mag leiden      po tot de openbaarmaking van een handels-, bedrijfs-, nijverheids- of        in beroepsgeheim of een fabrieks- of handelswerkwijze, of van                d' inlichtingen waarvan de onthulling in strijd zou zijn met de openbare orde;

4° de datum waarop de eerste stap voor de implementatie van de            4° meldingsplichtige grensoverschrijdende constructie is of zal worden       di ondernomen;                                                               ac

5° nadere bijzonderheden van de nationale bepalingen die aan de           5° meldingsplichtige grensoverschrijdende constructie ten grondslag          les liggen;                                                                   d'

6° de waarde van de meldingsplichtige grensoverschrijdende                6° constructie;                                                              dé

7° de lidstaat van de relevante belastingbetaler(s) en eventuele           7° andere lidstaten waarop de meldingsplichtige grensoverschrijdende          co constructie naar alle waarschijnlijkheid van invloed zal zijn;             co dé

8° de identificatiegegevens van andere personen in een lidstaat, op        8° wie de meldingsplichtige grensoverschrijdende constructie naar alle        su waarschijnlijkheid van invloed zal zijn, waarbij wordt vermeld met         fa welke lidstaten deze personen verbonden zijn.                              ce

De automatische uitwisseling geschiedt binnen één maand te                 L'é rekenen vanaf het einde van het kwartaal waarin de inlichtingen zijn       co verstrekt. De eerste inlichtingen worden uiterlijk op 31 oktober 2020      ét meegedeeld.                                                                31

De inlichtingen bedoeld in het tweede lid, 1°, 3° en 8° van deze           Le paragraaf, worden niet medegedeeld aan de Europese Commissie.              pa

Voor de belastbare tijdperken die aanvangen op of na 1 januari 2028,       Po bevat   de    mededeling     van    de   gegevens      betreffende    de   ce grensoverschrijdende regelingen het fiscaal identificatienummer van        tra de personen bepaald in het tweede lid, 8°.                                 pe

§ 7. De Belgische bevoegde autoriteit verstrekt spontaan, in elk van       § de volgende gevallen, de in de eerste § bedoelde inlichtingen aan de       sp buitenlandse bevoegde autoriteit:                                          vis

1° de Belgische bevoegde autoriteit heeft redenen om aan te nemen          1° dat in de andere lidstaat een derving van belasting kan bestaan;           ex

2° een belastingplichtige verkrijgt in België een vrijstelling of          2° vermindering van belasting die voor hem een belastingplicht of een         ex hogere belasting in de andere lidstaat zou moeten meebrengen;              au ou

3° transacties tussen een belastingplichtige in België en een              3° belastingplichtige in een andere lidstaat worden over één of meer          d’ andere landen geleid, op zodanige wijze dat daardoor in één van beide      m of in beide lidstaten een belastingbesparing kan ontstaan;                 l’u

4° de Belgische bevoegde autoriteit heeft redenen om aan te nemen          4° dat er belastingbesparing kan ontstaan door een kunstmatige                ex verschuiving van winsten binnen een groep van ondernemingen;               fic

5° de aan de Belgische bevoegde autoriteit verstrekte inlichtingen         5° door een buitenlandse bevoegde autoriteit, hebben informatie               co opgeleverd die voor de vaststelling van de belastingschuld in die          in andere lidstaat toereikend, ter zake dienend en niet overmatig is.         l’é

De Belgische bevoegde autoriteit kan een buitenlandse bevoegde           L’a autoriteit spontaan alle inlichtingen meedelen waarvan zij kennis        au heeft en die voor deze buitenlandse bevoegde autoriteit toereikend,      co ter zake dienend en niet overmatig zijn.                                 ce

De in het eerste lid bedoelde inlichtingen worden door de Belgische      L’a bevoegde autoriteit zo snel mogelijk, en uiterlijk binnen een maand      l’a nadat deze beschikbaar worden, aan de buitenlandse bevoegde              Et autoriteit van elke betrokken lidstaat verstrekt.                        m

§ 8. De ontvangst van de in § 7 bedoelde inlichtingen wordt door de      §8 Belgische bevoegde autoriteit onmiddellijk en in elk geval binnen        § zeven werkdagen na ontvangst, indien mogelijk langs elektronische        éle weg, aan de verstrekkende buitenlandse bevoegde autoriteit               co bevestigd.                                                               se

§ 9. Met het oog op de uitwisseling van de inlichtingen als bedoeld in   §
§ 1, kan de Belgische bevoegde autoriteit een buitenlandse bevoegde      co autoriteit verzoeken dat door eerstgenoemde gemachtigde                  ét ambtenaren onder de voorwaarden die zijn vastgesteld door de             co buitenlandse bevoegde autoriteit mogen:

1° aanwezig zijn, op het grondgebied van de lidstaat, in de kantoren     1° waar de administratieve autoriteiten van de lidstaat taken vervullen;    où tâ

2° aanwezig zijn bij administratieve onderzoeken die worden              2° uitgevoerd op het grondgebied van de buitenlandse bevoegde               l'a autoriteit;

3° deelnemen aan de administratieve onderzoeken die worden               3° uitgevoerd op het grondgebied van de andere lidstaat, met                de gebruikmaking     van    elektronische     communicatiemiddelen,    in   éle voorkomend geval.

In de gevallen waarin de door België gemachtigde ambtenaren              Da aanwezig zijn bij de administratieve onderzoeken of eraan deelnemen      au door middel van elektronische communicatiemiddelen, kunnen zij           m personen      ondervragen   en    bescheiden    onderzoeken,     onder   pe voorbehoud van de door de buitenlandse bevoegde autoriteit               de gedefinieerde proceduremodaliteiten.

§ 10. Met het oog op de uitwisseling van de in § 1 bedoelde              § inlichtingen kan de bevoegde autoriteit van een lidstaat de Belgische    co bevoegde autoriteit verzoeken dat door eerstgenoemde gemachtigde         co ambtenaren onder de voorwaarden die zijn vastgesteld door de             so Belgische bevoegde autoriteit mogen:

1° aanwezig zijn, in België, in de kantoren waar de FOD Financiën zijn   1° taken vervult;                                                           ex

2° aanwezig zijn bij administratieve onderzoeken die worden             2° uitgevoerd op Belgisch grondgebied;                                     be

3° deelnemen aan de administratieve onderzoeken die worden              3° uitgevoerd op Belgisch grondgebied, met gebruikmaking van               be elektronische communicatiemiddelen, in voorkomend geval.                éc

De Belgische bevoegde autoriteit antwoordt op het overeenkomstig        L'a de eerste alinea ingediende verzoek binnen een termijn van 60 dagen     co na ontvangst van het verzoek, om haar instemming te bevestigen of       ré haar gemotiveerde weigering aan de buitenlandse bevoegde                àl autoriteit mee te delen.

Indien de gevraagde inlichtingen vermeld staan in bescheiden            Lo waartoe de ambtenaren van de Belgische bevoegde autoriteit              au toegang hebben, ontvangen de ambtenaren van de verzoekende              les autoriteit een afschrift van die bescheiden.

Indien ambtenaren van de verzoekende autoriteit aanwezig zijn           Da tijdens een administratief onderzoek of daaraan deelnemen met           au gebruikmaking van elektronische communicatiemiddelen, mogen zij         m personen ondervragen en bescheiden onderzoeken, onder de                pe voorwaarden die zijn vastgesteld door de Belgische bevoegde             de autoriteit.

Elke weigering door een persoon op wie een onderzoek betrekking         To heeft, om de controlemaatregelen van de ambtenaren van de               co verzoekende autoriteit na te leven, wordt door de Belgische bevoegde    re autoriteit beschouwd als een weigering tegenover haar eigen             re ambtenaren.

De door de verzoekende lidstaat gemachtigde ambtenaren die              Le overeenkomstig het eerste lid in België aanwezig zijn, moeten steeds    Be een schriftelijk mandaat kunnen voorleggen waarin hun identiteit en     de hun officiële hoedanigheid worden vermeld.                              of

§ 11. In de gevallen waarin België met één of meer lidstaten            § overeenkomt om gelijktijdig, elk op het eigen grondgebied, bij een of   m meer personen te wier aanzien zij een gezamenlijk of complementair      co belang hebben, controles te verrichten en de aldus verkregen            pr inlichtingen uit te wisselen, is deze § van toepassing.                 d’

De Belgische bevoegde autoriteit bepaalt autonoom welke personen        L’a zij voor een gelijktijdige controle wil voorstellen. Zij deelt de       pe buitenlandse bevoegde autoriteit van de betrokken lidstaten met         sim opgave van redenen mee welke dossiers zij voor een gelijktijdige        m controle voorstelt. Zij bepaalt binnen welke termijn de controle moet   un plaatsvinden.                                                           leq

Wanneer aan de Belgische bevoegde autoriteit een gelijktijdige          Lo controle wordt voorgesteld, beslist zij of ze aan de gelijktijdige      be controle wenst deel te nemen. Zij doet de buitenlandse bevoegde         El autoriteit die de controle voorstelt een bevestiging van deelname of    pr een gemotiveerde weigering toekomen binnen een termijn van 60           dé dagen, te rekenen vanaf de ontvangst van het voorstel.

De Belgische bevoegde autoriteit wijst een vertegenwoordiger aan        L’a die wordt belast met de leiding en de coördinatie van de controle.      su

§ 11/1. De bevoegde autoriteit van een of meer lidstaten kan de         § Belgische bevoegde autoriteit verzoeken een gezamenlijke audit uit      pe te voeren. De Belgische bevoegde autoriteit aanvaardt of weigert het    co verzoek om een gezamenlijke audit binnen een termijn van 60 dagen,      de te rekenen vanaf de ontvangst van het verzoek en motiveert haar         ré beslissing ingeval ze het verzoek verwerpt.

Gezamenlijke audits worden op vooraf overeengekomen en                  Le gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd       pr door de bevoegde autoriteit van de verzoekende lidstaat, door de        lin Belgische bevoegde autoriteit, en in voorkomend geval, door de          pa bevoegde autoriteiten van de andere aangezochte lidstaten en in         co overeenstemming met de Belgische wetgeving en procedurele               la voorschriften. De Belgische bevoegde autoriteit wijst een               co vertegenwoordiger aan die verantwoordelijk is voor het toezicht op en   de de coördinatie van de gezamenlijke audit op Belgisch grondgebied.

De rechten en plichten van de ambtenaren van lidstaten die              Le deelnemen aan de gezamenlijke audit op Belgisch grondgebied,            pa worden vastgesteld overeenkomstig de Belgische wetgeving. Tegelijk      co met het naleven van die wetgeving, oefenen de ambtenaren van een        lég andere lidstaat geen bevoegdheden uit die verder zouden gaan dan        au de bevoegdheden die hun krachtens de wetgeving van hun lidstaat         la zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de       Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op         vis Belgisch grondgebied, zijn de ambtenaren van andere lidstaten die       d'a deelnemen aan de activiteiten van de gezamenlijke audit, gemachtigd     co om personen te ondervragen en bescheiden te onderzoeken in              do samenspraak met de ambtenaren van de Belgische bevoegde                 co autoriteit, met inachtneming van de in België bepaalde procedurele      en regelingen.

Onverminderd het tweede en derde lid en voor de toepassing van de       Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op         vis Belgisch grondgebied, kan het bewijsmateriaal dat tijdens de            pr activiteiten van de gezamenlijke audit is verzameld, worden             év beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde            m juridische voorwaarden als in het geval van een klassieke audit,        ca

uitgevoerd in België door Belgische ambtenaren, onder meer in de          fo loop van een bezwaar-, herzienings- of beroepsprocedures.                 ré

Onverminderd het tweede en derde lid en voor de toepassing van de         Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op           vis Belgisch grondgebied, genieten personen die aan een gezamenlijke          fa audit worden onderworpen of erdoor worden geraakt, dezelfde               de rechten en hebben ze dezelfde plichten als in het geval van een           s'a klassieke audit waaraan alleen Belgische ambtenaren deelnemen,            av onder meer in de loop van een bezwaar-, herzienings- of                   co beroepsprocedures.

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van     Lo een of meer lidstaten een gezamenlijke audit verrichten, trachten zij     de het eens te worden over de feiten en omstandigheden die relevant          s'e zijn voor de gezamenlijke audit, en streven zij naar overeenstemming      le over de fiscale positie van de geaudite persoon of personen op basis      fis van de resultaten van de gezamenlijke audit. De bevindingen van de        de gezamenlijke audit worden neergelegd in een eindverslag. Punten           in waarover de bevoegde autoriteiten het eens zijn, worden in de             au conclusies van het eindverslag opgenomen en worden in aanmerking          ra genomen in de relevante instrumenten die de bevoegde autoriteiten         ap van de deelnemende lidstaten naar aanleiding van die gezamenlijke         pa audit uitvaardigen.

De geaudite persoon of personen word(t)en in kennis gesteld van het       La resultaat van de gezamenlijke audit en krijgt/krijgen een kopie van het   ré eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.        da

§ 11/2. De Belgische bevoegde autoriteit kan de bevoegde autoriteit       § van een andere of meerdere lidstaten verzoeken een gezamenlijke           co audit uit te voeren.                                                      co

Gezamenlijke audits worden op vooraf overeengekomen en                    Le gecoördineerde wijze, met inbegrip van taalregelingen, uitgevoerd         pr door de betrokken bevoegde autoriteiten, en in overeenstemming            lin met de wetgeving en de procedurele voorschriften van de lidstaat          co waar de activiteiten van de gezamenlijke audit plaatsvinden.              m

De rechten en plichten van de Belgische ambtenaren die deelnemen          Le aan de gezamenlijke audit op het grondgebied van een andere               co lidstaat, worden vastgesteld overeenkomstig de wetgeving van die          dé lidstaat. Tegelijk met het naleven van deze wetgeving, oefenen de         en Belgische ambtenaren geen bevoegdheden uit die verder zouden              au gaan dan de bevoegdheden die hun krachtens de Belgische                   la wetgeving zijn verleend.

Onverminderd het tweede en derde lid en voor de toepassing van de         Sa in het eerste lid bedoelde gezamenlijke audits, gerealiseerd op het       vis grondgebied van een andere lidstaat, kan het bewijsmateriaal dat          élé

tijdens de activiteiten van de gezamenlijke audit is verzameld, worden    co beoordeeld, ook op de ontvankelijkheid ervan, onder dezelfde              da juridische voorwaarden als in het geval van een klassieke audit           da uitgevoerd in België door Belgische ambtenaren.                           fo

Indien de Belgische bevoegde autoriteit en de bevoegde autoriteit van     Lo een of meerdere andere lidstaten een gezamenlijke audit verrichten,       de trachten zij het eens te worden over de feiten en omstandigheden die      s'e relevant zijn voor de gezamenlijke audit, en streven zij naar             le overeenstemming over de fiscale positie van de geaudite persoon of        fis personen op basis van de resultaten van de gezamenlijke audit. De         de bevindingen van de gezamenlijke audit worden neergelegd in een            in eindverslag. De punten waarover de bevoegde autoriteiten het eens         au zijn, worden in de conclusies van het eindverslag opgenomen en            ra worden in aanmerking genomen in de relevante instrumenten die de          ap bevoegde autoriteiten van de deelnemende lidstaten naar aanleiding        pa van die gezamenlijke audit uitvaardigen.

De geaudite persoon of personen worden in kennis gesteld van het          La resultaat van de gezamenlijke audit en krijgen een kopie van het          ré eindverslag binnen 60 dagen na het uitbrengen van het eindverslag.        da

§ 12. De Belgische bevoegde autoriteit kan een verzoek aan een            § buitenlandse bevoegde autoriteit richten tot kennisgeving aan de          co geadresseerde, overeenkomstig de in de aangezochte lidstaat               ré geldende voorschriften voor de kennisgeving van soortgelijke akten,       m van alle door de Belgische administratieve overheden afgegeven            ém akten en besluiten die betrekking hebben op de toepassing in België       l’a van wetgeving betreffende registratie-, hypotheek- en griffierechten.     d’

Het verzoek tot kennisgeving vermeldt de naam en het adres van de         La geadresseerde, evenals alle overige informatie ter identificatie van de   ain geadresseerde, en het onderwerp van de akte of het besluit waarvan        id de geadresseerde kennis moet worden gegeven.

Het verzoek tot kennisgeving wordt door de Belgische bevoegde             L’a autoriteit slechts gedaan indien de kennisgeving van de akten niet        qu volgens de Belgische regels kan geschieden, of buitensporige              rè problemen zou veroorzaken. De Belgische bevoegde autoriteit kan           di een document, per aangetekende brief of langs elektronische weg,          no rechtstreeks ter kennis brengen aan een persoon op het grondgebied        éle van een andere lidstaat.                                                  au

§ 13. Op verzoek van een buitenlandse bevoegde autoriteit gaat de         § Belgische bevoegde autoriteit, overeenkomstig de Belgische                co voorschriften voor de kennisgeving van soortgelijke akten, over tot       be kennisgeving aan de geadresseerde van alle door de administratieve        de overheden van de verzoekende lidstaat afgegeven akten en besluiten        m die betrekking hebben op de toepassing op haar grondgebied van            lég wetgeving betreffende registratie-, hypotheek- en griffierechten.         gr

De Belgische bevoegde autoriteit stelt de verzoekende autoriteit                 L’a onverwijld in kennis van het aan het verzoek gegeven gevolg en, in het           re bijzonder, van de datum waarop de akte of het besluit aan de                     de geadresseerde ter kennis is gebracht.

§ 14. Indien een buitenlandse bevoegde autoriteit inlichtingen                   § overeenkomstig §§ 4 of 8 heeft verstrekt en terugmelding                         in betreffende    de   ontvangen         inlichtingen      verzoekt,    doet   de   d’ ontvangende Belgische bevoegde autoriteit, zonder afbreuk te doen                les aan de Belgische voorschriften inzake beroepsgeheim en                           pr gegevensbescherming, zo spoedig mogelijk, doch uiterlijk drie                    à maanden nadat het resultaat van het gebruik van de verlangde                     ra inlichtingen bekend is, een terugmelding aan de buitenlandse                     de bevoegde autoriteit die de inlichtingen heeft verzonden.

De Belgische bevoegde autoriteit doet eenmaal per jaar,                          L’a overeenkomstig bilateraal overeengekomen praktische afspraken,                   m een terugmelding over de automatische inlichtingenuitwisseling naar              au de betrokken lidstaten.                                                          bi

§ 15. De Belgische bevoegde autoriteit die overeenkomstig §§ 5 of 7              § inlichtingen heeft verstrekt, kan de ontvangende buitenlandse                    in bevoegde autoriteit om terugmelding betreffende de ontvangen                     co inlichtingen verzoeken.                                                          re

§ 16. De Belgische verbindingsdienst of de Belgische bevoegde                    § ambtenaar die een verzoek om samenwerking ontvangt dat een                       co optreden vereist buiten de hem krachtens de Belgische wetgeving of               pa het Belgische beleid verleende bevoegdheid, geeft het verzoek                    lég onmiddellijk door aan het Belgisch centraal verbindingsbureau en                 bu stelt de verzoekende buitenlandse bevoegde autoriteit hiervan in                 ét kennis. In dat geval gaat de in § 5 vermelde termijn in op de dag nadat          co het verzoek aan het Belgisch centraal verbindingsbureau is                       bu doorgezonden.

§ 17. De inlichtingen meegedeeld en ontvangen door België in                     §1 enigerlei   vorm    of    volgens      dit   artikel,    vallen     onder   de   qu geheimhoudingsplicht en genieten de bescherming waarin het                       co nationale recht van de ontvangende lidstaat met betrekking tot                   à soortgelijke inlichtingen voorziet.                                              m

Deze inlichtingen mogen worden gebruikt:                                         Ce

1° voor de vaststelling, de toepassing en de handhaving van het                  1° nationale recht met betrekking tot de in artikel 2 van de richtlijn              lég bedoelde belastingen, alsmede de btw, andere indirecte belastingen,              vis douanerechten, de bestrijding van het witwassen van geld en van de               in financiering van terrorisme;                                                     ca

2° voor de vestiging en de invordering van de andere belastingen en      2° rechten met betrekking tot artikel 3 van de wet van 9 januari 2012       re houdende omzetting van Richtlijn 2010/24/EU van de Raad van 16           di maart 2010 betreffende de wederzijdse bijstand inzake de                 l'a invordering van schuldvorderingen die voortvloeien uit belastingen,      re rechten en andere maatregelen, en voor het vestigen en invorderen        et van de verplichte sociale bijdragen;

3° ter gelegenheid van gerechtelijke en administratieve procedures       3° die kunnen leiden tot sancties, geheven ten gevolge van inbreuken op     en de fiscale wetgeving, onverminderd algemene regels en wettelijke         lég bepalingen die de rechten van beklaagden en getuigen in het kader        de van dergelijke procedures beheersen.                                     té

Met de toestemming van de buitenlandse bevoegde autoriteit die de        Av inlichtingen overeenkomstig de Richtlijn heeft meegedeeld en voor        co zover dat toegelaten is door de Belgische wetgeving, kunnen de           au ontvangen inlichtingen en documenten ontvangen van deze autoriteit       et worden gebruikt voor andere doeleinden dan deze bedoeld in het           au tweede lid.

De Belgische bevoegde autoriteit kan de ontvangen inlichtingen en        L'a documenten zonder de in de derde lid van deze paragraaf bedoelde         re toestemming ook gebruiken voor elk doel dat onder een op artikel 215     pr van het Verdrag betreffende de werking van de Europese Unie              l'a gebaseerde handeling valt en deze daartoe delen met de bevoegde          les autoriteit die verantwoordelijk is voor beperkende maatregelen in de     m betrokken lidstaat.

De Belgische bevoegde autoriteit die van oordeel is dat de van de        Lo bevoegde autoriteit van een andere lidstaat verkregen inlichtingen de    qu bevoegde autoriteit van een derde lidstaat van nut kunnen zijn voor      su de in het tweede lid beoogde doelen, mag de inlichtingen aan deze        m autoriteit doorgeven, op voorwaarde dat zij de bevoegde autoriteit       ce van de inlichtingen verstrekkende lidstaat in kennis stelt van haar      l'E voornemen om die inlichtingen met een derde lidstaat te delen en op      co voorwaarde dat dat gebeurt in overeenstemming met de in dit artikel      co vastgelegde regels en procedures. De inlichtingen verstrekkende          ar lidstaat kan zich hiertegen verzetten binnen vijftien kalenderdagen na   da de datum van ontvangst van de kennisgeving van de lidstaat die de        de inlichtingen wenst te delen.

§ 18. De Belgische bevoegde autoriteit kan het gebruik toestaan van      § de overeenkomstig dit artikel verstrekte inlichtingen en bescheiden in   l’E de lidstaat die ze ontvangt, voor andere dan in § 17, tweede lid,        co bedoelde doeleinden. De Belgische bevoegde autoriteit verleent           § toestemming indien de inlichtingen in België voor soortgelijke           co doeleinden kunnen worden gebruikt.                                       sim

De Belgische bevoegde autoriteit deelt aan de bevoegde autoriteiten           L'a van alle andere lidstaten een lijst mee van andere dan in paragraaf 1         de bedoelde doeleinden waarvoor overeenkomstig haar nationale recht,             ce de inlichtingen en bescheiden kunnen worden gebruikt. De bevoegde             dr autoriteit die inlichtingen en bescheiden ontvangt, kan de ontvangen          L'a inlichtingen en bescheiden zonder de in het eerste lid bedoelde               pe toestemming gebruiken voor alle doeleinden die de Belgische                   l'a bevoegde autoriteit heeft opgenoemd.                                          l'a

De Belgische bevoegde autoriteit kan het gebruik overeenkomstig de            L’a in § 17, derde lid beoogde doelen van de inlichtingen afkomstig uit           in België die door een buitenlandse bevoegde autoriteit aan een                  un buitenlandse bevoegde autoriteit van een derde lidstaat werden                pr doorgegeven, in die derde lidstaat toestaan.                                  fin

§ 19. Alvorens om de in § 4 bedoelde inlichtingen te verzoeken, tracht        § de Belgische bevoegde autoriteit eerst de inlichtingen te verkrijgen uit      l’a alle gebruikelijke bronnen die zij in de gegeven omstandigheden kan           ha aanspreken zonder dat het beoogde resultaat in het gedrang dreigt te          ob komen.                                                                        ré

De in § 5 bedoelde inlichtingen worden door de Belgische bevoegde             L’a autoriteit aan een buitenlandse bevoegde autoriteit verstrekt, op             ét voorwaarde dat de buitenlandse bevoegde autoriteit eerst de                   co inlichtingen tracht te verkrijgen uit alle gebruikelijke bronnen die zij in   d’ de gegeven omstandigheden kon aanspreken zonder dat het                       in beoogde resultaat in het gedrang dreigt te komen.                             re

§ 20. Het is de Belgische bevoegde autoriteit niet toegelaten                 § onderzoek in te stellen of inlichtingen te verstrekken wanneer de             de Belgische wetgeving haar niet toestaat voor eigen doeleinden het              ré onderzoek in te stellen of de gevraagde inlichtingen te verzamelen.           qu lég

De Belgische bevoegde autoriteit kan weigeren inlichtingen te                 L’a verstrekken indien:                                                           in

1° de verzoekende lidstaat, op juridische gronden, soortgelijke               1° inlichtingen niet kan verstrekken;                                            ju

2° dit zou leiden tot de openbaarmaking van een handels-, bedrijfs-,          2° nijverheids- of beroepsgeheim of een fabrieks- of handelswerkwijze,           pr of indien het inlichtingen betreft waarvan de onthulling in strijd zou        di zijn met de openbare orde.

De Belgische bevoegde autoriteit deelt de verzoekende autoriteit mee          L’a op welke gronden zij het verzoek om inlichtingen afwijst.                     du

§ 21. De Belgische bevoegde autoriteit wendt de middelen aan                  § waarover zij beschikt om de gevraagde inlichtingen te verzamelen,             co

zelfs indien zij de inlichtingen niet voor eigen belastingdoeleinden      de nodig heeft. Deze verplichting geldt onverminderd § 20, eerste en         se tweede lid, die, wanneer er een beroep op wordt gedaan, in geen geval     du zo kunnen worden uitgelegd dat België kan weigeren inlichtingen te        ca verstrekken uitsluitend omdat België geen binnenlands belang bij          fo deze inlichtingen heeft.                                                  pr

In geen geval wordt § 20, eerste lid en tweede lid, 2° zo uitgelegd dat   Le de Belgische bevoegde autoriteit kan weigeren inlichtingen te             in verstrekken, uitsluitend op grond dat deze berusten bij een bank, een     fo andere financiële instelling, een gevolmachtigde of een persoon die       dé als vertegenwoordiger of trustee optreedt, of dat zij betrekking          m hebben op eigendomsbelangen in een persoon.                               ou pe

Onverminderd het tweede lid kan de Belgische bevoegde autoriteit          No weigeren de gevraagde inlichtingen toe te zenden indien deze              tra betrekking hebben op belastbare tijdperken vóór 1 januari 2011 en de      su toezending van de inlichtingen geweigerd had kunnen worden op             tra grond van artikel 8, punt 1, van de richtlijn 77/799/EG indien daarom     l’a was verzocht vóór 11 maart 2011.                                          de

§ 22. Indien de Belgische overheid voorziet in een samenwerking met       § een derde land welke verder reikt dan de bij de richtlijn geregelde       pl samenwerking, kan de Belgische overheid de verderreikende                 ce samenwerking niet weigeren aan een andere lidstaat die met haar           pr deze verderreikende, wederzijdse samenwerking wenst aan te gaan.

§ 23. Verzoeken om inlichtingen en de administratieve onderzoeken         § die zijn ingediend op grond van § 4, alsook de antwoorden op grond        in van § 5, de ontvangstbevestigingen, de verzoeken om inlichtingen van      ac algemene aard en de verklaringen van ongeschiktheid of weigering          gé krachtens § 5 worden, voor zover mogelijk, overgemaakt door middel        da van een door de Commissie goedgekeurd standaardformulier. Er              ad mogen rapporten, certificaten en andere bescheiden, of andere voor        ac eensluidend verklaarde afschriften of uittreksels daarvan bij de          do standaardformulieren gevoegd worden.                                      de

De in het eerste lid bedoelde standaardformulieren bevatten ten           Le minste de volgende gegevens, die de verzoekende autoriteit moet           in verstrekken:

a) de identiteit van de persoon naar wie het onderzoek of de controle     a) is ingesteld en, in het geval van vragen betreffende een groep zoals      en bedoeld in § 5/2, een gedetailleerde beschrijving van de groep;           §5

b) het fiscale doel van de gevraagde informatie.                          b)

De Belgische bevoegde autoriteit kan, voor zover bekend en in             L'a overeenstemming met de ontwikkeling van de internationale situatie,       et

de namen en adressen verstrekken van alle personen van wie er            les redenen zijn om aan te nemen dat ze in het bezit zijn van de gevraagde   qu informatie, alsook alle elementen die het verzamelen van informatie      to door de aangezochte autoriteit kunnen vergemakkelijken.                  l'a

De    spontane     gegevensuitwisseling    en   de    desbetreffende     Le ontvangstbevestiging respectievelijk op grond van de §§ 7 en 8,          les verzoeken tot administratieve kennisgeving op grond van §§ 12 en         de 13, terugmeldingen op grond van §§ 14 en 15, de inlichtingen op          d' grond van §§ 17, tweede lid en 18, en van § 25, tweede lid, worden       §§ overgemaakt door middel van de door de Commissie goedgekeurde            fo standaardformulieren.

De automatische inlichtingenuitwisseling op grond van de §§ 6 en 6/1     Le wordt verricht in een geautomatiseerd standaardformaat dat               so ontworpen is om die automatische uitwisseling te vergemakkelijken        fa en dat is goedgekeurd door de Commissie.

§ 24. De krachtens dit artikel verstrekte inlichtingen worden voor       §2 zover mogelijk verzonden langs elektronische weg, via het CCN-           da netwerk.                                                                 du

Het verzoek om samenwerking, waaronder het verzoek tot                   Le kennisgeving en de bijgevoegde bescheiden kunnen in elke door de         no aangezochte en de verzoekende autoriteit overeengekomen taal zijn        lan gesteld. Slechts in bijzondere gevallen en mits het verzoek met          re redenen omkleed is, kan de Belgische bevoegde autoriteit verzoeken       tra het verzoek vergezeld te laten gaan van een vertaling in één van de      de officiële talen van België.                                              m

Om te voldoen aan de automatische uitwisseling als bedoeld in § 6/1,     Af
1° en 2°, te verstrekken inlichtingen, worden de gegevens die            le moeten worden meegedeeld opgeslagen in een beveiligd centraal            co gegevensbestand betreffende de administratieve samenwerking op           de belastinggebied, bestemd voor de lidstaten, ontwikkeld en ter            da beschikking gesteld door de Commissie uiterlijk op 31 december           dé
2017. De Belgische bevoegde autoriteiten hebben toegang tot de in        be dit gegevensbestand opgeslagen inlichtingen.

In afwachting dat dat beveiligd centraal gegevensbestand                 Av operationeel wordt, geschiedt de in § 6/1, 1° en 2°, bedoelde            l’é automatische uitwisseling van gegevens, volgens lid 1 van deze           co paragraaf en de toepasselijke praktische modaliteiten.                   m

§ 25. De Belgische bevoegde autoriteit die van een derde land            § inlichtingen ontvangt welke naar verwachting van belang zijn voor        l’a haar administratie en de handhaving van de Belgische wetgeving           dr betreffende registratie-, hypotheek- en griffierechten, kan deze         co inlichtingen verstrekken aan de buitenlandse bevoegde autoriteiten       de van de lidstaten voor wie die inlichtingen van nut kunnen zijn, en aan   l’a

elke buitenlandse bevoegde autoriteit die erom verzoekt, mits dat         de krachtens een overeenkomst met dat derde land is toegestaan.              et

De Belgische bevoegde autoriteit kan, met inachtneming van de wet         L’a van 8 december 1992 tot bescherming van de persoonlijke                   dé levenssfeer ten opzichte van de verwerking van persoonsgegevens           tra en de wet van 3 augustus 2012 houdende bepalingen betreffende de          20 verwerking van persoonsgegevens door de Federale Overheidsdienst          ca Financiën in het kader van zijn opdrachten, de overeenkomstig dit         da artikel ontvangen inlichtingen doorgeven aan een derde land, op           in voorwaarde dat aan elk van de volgende voorwaarden is voldaan:            qu

a) de buitenlandse bevoegde autoriteit van de lidstaat waaruit de         a) inlichtingen afkomstig zijn, heeft daarin toegestemd;                     les

b) het derde land heeft zich ertoe verbonden de medewerking te            b) verlenen die nodig is om bewijsmateriaal bijeen te brengen omtrent        élé het ongeoorloofde of onwettige karakter van verrichtingen die blijken     pa in strijd te zijn met of een misbruik te vormen van de                    fis belastingwetgeving.

§   26.   Rapporterende     financiële   instellingen,   intermediairs,   § rapporterende platformexploitanten en de Belgische bevoegde               op autoriteit worden als verwerkingsverantwoordelijken beschouwd             so wanneer zij, alleen of gezamenlijk, de doelen en middelen van de          ag verwerking van persoonsgegevens bepalen in de zin van Verordening         m (EU) 2016/679 van het Europees Parlement en de Raad van 27 april          rè 2016 betreffende de bescherming van natuurlijke personen in               av verband met de verwerking van persoonsgegevens en betreffende             tra het vrije verkeer van die gegevens en tot intrekking van Richtlijn        de 95/46/EG.

De Belgische bevoegde autoriteit stelt de Commissie onverwijld in         L'a kennis van elke gegevensinbreuk           en alle daaropvolgende          vio corrigerende maatregelen.

De Belgische bevoegde autoriteit kan de uitwisseling van inlichtingen     L'a met de lidstaat of de lidstaten waar de gegevensinbreuk heeft             d' plaatsgevonden, schorsen door de Commissie en de betrokken                ou lidstaat of lidstaten daarvan schriftelijk in kennis te stellen. Een      Co dergelijke schorsing wordt onmiddellijk van kracht.                       su

In geval van gegevensinbreuk, onderzoekt, beperkt en verhelpt de          En Belgische bevoegde autoriteit de gegevensinbreuk, en verzoekt zij de      àu Commissie, daarvan schriftelijk in kennis gesteld, om de schorsing van    m de toegang tot het CCN-netwerk voor de toepassing van deze richtlijn,     l'a indien de gegevensinbreuk niet onmiddellijk en op passende wijze          de onder controle kan worden gebracht. Op een dergelijk verzoek schorst      ap de Commissie de toegang van die lidstaat of lidstaten tot het CCN-        l'a netwerk voor de toepassing van de richtlijn.                              au

De Belgische bevoegde autoriteit stelt, in geval van een                                  L'a gegevensinbreuk, de Commissie op de hoogte wanneer zij deze                               la inbreuk heeft verholpen. Indien een of meer lidstaten de Commissie                        pl verzoeken om gezamenlijk te verifiëren of de gegevensinbreuk is                           eu verholpen, geeft de Commissie pas na die verificatie de betrokken                         Co lidstaat of lidstaten opnieuw toegang tot het CCN-netwerk voor de                         m toepassing van de richtlijn.                                                              ef

Indien voor de toepassing van deze richtlijn een gegevensinbreuk in                       Da het centrale gegevensbestand of het CCN-netwerk plaatsvindt die                           ce nadelige gevolgen kan hebben voor de uitwisseling van inlichtingen                        lo door de lidstaten via het CCN-netwerk, stelt de Commissie de                              ré lidstaten       zonder       onnodige         vertraging      in    kennis     van   de   sa gegevensinbreuk en van eventuele corrigerende maatregelen die zijn                        de genomen. Zulke corrigerende maatregelen kunnen inhouden dat de                            co toegang tot het centrale gegevensbestand of het CCN-netwerk voor                          ré de toepassing van de richtlijn wordt geschorst totdat de                                  vio gegevensinbreuk is verholpen.
----------                                                                                -- Nota:                                                                                     No - in § 6/1, lid 1, 5°, a) en i): lees ‘1° en 3°’ ipv. ‘1° en 4°’.                         -d - in § 6/1, lid 2: lees ‘5°, a) en i)’ ipv. ‘6°, a) en k)’.                               -d - in § 6/3, lid 2, 1°: lees ‘’ paragraaf 2, 18° ‘ ipv. ‘’ paragraaf 2, 21°’.              -d - in § 6/1, lid 1, 5°, i): lees ‘rechtspersonen’ ipv. ‘rechtpersonen’.

###### Art. 289bis/1

(8°, ingevoegd bij art. 29 van de wet van 16.03.2026 (B.S., 01.04.2026). Tekst            (8 van toepassing vanaf 11.04.2026 (art. -))                                                 ap

Voor de toepassing van de artikelen 289bis, § 6/3 en 289bis/2 tot en                      Po met 289bis/9, wordt verstaan onder:                                                       en

1° "grensoverschrijdende constructie": een constructie die ofwel                          1° meer dan één lidstaat ofwel een lidstaat en een derde land betreft,                       Et waarbij ten minste een van de volgende voorwaarden is vervuld:                            de

a) niet alle deelnemers aan de constructie hebben hun fiscale                             a) woonplaats in hetzelfde rechtsgebied;                                                     fis

b) een of meer van de deelnemers aan de constructie heeft zijn fiscale                    b) woonplaats tegelijkertijd in meer dan één rechtsgebied;                                   fin

c) een of meer van de deelnemers aan de constructie oefent een                            c) bedrijf uit in een ander rechtsgebied via een in dat rechtsgebied                         da gelegen vaste inrichting en de constructie behelst een deel of het                        st geheel van het bedrijf van die vaste inrichting;                                          ou

d) een of meer van de deelnemers aan de constructie oefent een                d) activiteit uit in een ander rechtsgebied zonder in dat rechtsgebied zijn      da fiscale woonplaats te hebben of zonder in dat rechtsgebied een vaste          cr inrichting te creëren;

e) een dergelijke constructie heeft mogelijk gevolgen voor de                 e) automatische uitwisseling van inlichtingen of de vaststelling van het         au uiteindelijk belang.                                                          ef

Een constructie betekent ook een reeks constructies. Een constructie          Un kan uit verscheidene stappen of onderdelen bestaan.                           pe

2° "meldingsplichtige grensoverschrijdende constructie": iedere               2° grensoverschrijdende constructie die ten minste één van de in artikel         to 289bis/2 bedoelde wezenskenmerken bezit;                                      m

3° "wezenskenmerk": een in artikel 289bis/2 bedoelde eigenschap of            3° kenmerk van een grensoverschrijdende constructie die geldt als een            28 indicatie van een mogelijk risico op belastingontwijking;                     d'

4°   "intermediair": een      persoon       die   een   meldingsplichtige     4° grensoverschrijdende      constructie       bedenkt,    aanbiedt,    opzet,   or beschikbaar maakt voor implementatie of de implementatie ervan                dé beheert.                                                                      sa

Een intermediair is ook een persoon die, gelet op de betrokken feiten         Un en omstandigheden en op basis van de beschikbare informatie en de             cir deskundigheid die en het begrip dat nodig is om die diensten te               ain verstrekken, weet of redelijkerwijs kon weten dat hij rechtstreeks of         né via andere personen, heeft toegezegd hulp, bijstand of advies te              ra verstrekken met betrekking tot het bedenken, aanbieden, opzetten,             di beschikbaar maken voor implementatie of beheren van de                        as implementatie van een meldingsplichtige grensoverschrijdende                  co constructie. Elke persoon heeft het recht bewijs te leveren van het feit      de dat hij niet wist en redelijkerwijs niet kon weten dat hij bij een            di meldingsplichtige grensoverschrijdende constructie betrokken was.             œ Daartoe kan die persoon alle relevante feiten en omstandigheden,              qu beschikbare informatie en zijn relevante deskundigheid en begrip              sa ervan vermelden.                                                              l'o to di

Om een intermediair te zijn, dient een persoon ten minste één van de          Po volgende aanvullende voorwaarden te vervullen:                                co

a) fiscaal inwoner van een lidstaat zijn;                                     a)

b) beschikken over een vaste inrichting in een lidstaat via welke de          b) diensten in verband met de constructie worden verleend;                       du

c) opgericht zijn in of onder de toepassing van de wetten vallen van                  c) een lidstaat;                                                                         m

d) ingeschreven zijn bij een beroepsorganisatie in verband met de                     d) verstrekking van juridische, fiscale of adviesdiensten in een lidstaat.               ra Et

5° "relevante belastingplichtige": elke persoon voor wie een                          5° meldingsplichtige grensoverschrijdende constructie beschikbaar                        tra wordt gemaakt voor implementatie, of die gereed is om een                             di meldingsplichtige          grensoverschrijdende             constructie         te    en implementeren of die de eerste stap van een dergelijke constructie                    dé heeft geïmplementeerd;                                                                di

6° "marktklare constructie": een grensoverschrijdende constructie                     6° die is bedacht of aangeboden, implementeerbaar is of beschikbaar is                   co gemaakt voor implementatie zonder dat er wezenlijke aanpassingen                      au nodig zijn;                                                                           im

7° "constructie op maat": een grensoverschrijdende constructie die                    7° geen marktklare constructie is.                                                       pa

8° "cliënt": elke intermediair of relevante belastingplichtige die                    8° diensten, met inbegrip van bijstand, advies, raad of begeleiding,                     se ontvangt van een tot het juridisch beroepsgeheim gehouden                             or intermediair      met       betrekking       tot    een      meldingsplichtige        pr grensoverschrijdende constructie.                                                     fa

###### Art. 289bis/2

(ingevoegd bij art. 21 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

De in artikel 289bis/1, 3°, bedoelde wezenskenmerken van een                          Le grensoverschrijdende constructie kunnen worden onderverdeeld in                       3° vijf categorieën, categorie A zijnde de algemene wezenskenmerken                      m die aan de in het tweede lid bedoelde "main benefit test" zijn                        vis gekoppeld, categorie B zijnde de specifieke wezenskenmerken die                       so aan de hiervoor vermelde "main benefit test" zijn gekoppeld,                          ét categorie C zijnde specifieke wezenskenmerken in verband met                          la grensoverschrijdende transacties, categorie D zijnde specifieke                       au wezenskenmerken in verband met de automatische uitwisseling van                       la inlichtingen en uiteindelijk belang en categorie E zijnde specifieke                  tra wezenskenmerken in verband met verrekenprijzen.

De algemene wezenskenmerken in categorie A bedoeld in het vierde                      Le lid en de specifieke wezenskenmerken in categorie B bedoeld in het                    m

vijfde lid en de specifieke wezenskenmerken in categorie C bedoeld in     m het zesde lid, 1°, b), eerste streepje, c) en d) mogen uitsluitend in     pr aanmerking worden genomen indien kan worden aangetoond dat het            ét belangrijkste voordeel of één van de belangrijkste voordelen die, gelet   pe op alle relevante feiten en omstandigheden, redelijkerwijs te             co verwachten valt van de constructie het verkrijgen van een                 l'o belastingvoordeel is. Dit is de zogenaamde "main benefit test             l'a

In het kader van het specifieke wezenskenmerk van categorie C,            Da bedoeld in het zesde lid, 1° is de aanwezigheid van één van de            6, voorwaarden bedoeld in hetzelfde zesde lid, 1°, b), eerste streepje, c)   b) en d) niet voldoende om te besluiten dat een constructie voldoet aan      sa de in het tweede lid bedoelde "main benefit test

Wordt beschouwd als een algemeen wezenskenmerk van categorie              Es A:

1° een constructie waarbij de relevante belastingplichtige of een         1° deelnemer aan de constructie zich tot geheimhouding verbindt en op        di grond    hiervan     niet    aan   andere     intermediairs   of    de    laq belastingautoriteiten mag onthullen hoe de constructie een                in belastingvoordeel kan opleveren;                                          po

2° een constructie waarbij de intermediair aanspraak maakt op een         2° vergoeding (of rente, betaling van financieringskosten en andere          ho uitgaven) voor de constructie en die vergoeding wordt vastgelegd op       et basis van:                                                                ré

a) het bedrag van het belastingvoordeel dat de constructie oplevert;      a) of

b) de vraag of de constructie daadwerkelijk een belastingvoordeel         b) heeft opgeleverd. De intermediair moet daarbij de vergoeding              Ce gedeeltelijk of volledig terugbetalen wanneer het met de constructie      pa beoogde belastingvoordeel niet gedeeltelijk of volledig werd              es verwezenlijkt;                                                            pa

3° een       constructie    waarbij gebruik   wordt gemaakt van           3° gestandaardiseerde documenten en/of een gestandaardiseerde                gr structuur en die beschikbaar is voor meer dan een relevante               co belastingplichtige zonder dat er voor implementatie wezenlijke            im aanpassingen nodig zijn.

Wordt beschouwd als een specifiek wezenskenmerk van categorie B:          Es

1° een constructie waarbij een deelnemer aan de constructie een           1° reeks geplande stappen onderneemt die erin bestaan een                    ar verlieslijdende onderneming te verwerven, de hoofdactiviteit van die      ré onderneming stop te zetten en de verliezen ervan te gebruiken om de       et door hem verschuldigde belastingen te verminderen, onder meer

door overdracht van die verliezen naar een ander rechtsgebied of door    co een versneld gebruik van die verliezen;                                  l'a

2° een constructie die tot gevolg heeft dat inkomsten worden             2° omgezet in vermogen, schenkingen of andere inkomstencategorieën          do die lager worden belast of van belasting worden vrijgesteld;             in

3° een constructie die circulaire transacties omvat met als resultaat    3° dat middelen worden rondgepompt ("round-tripping"), meer bepaald         ré met behulp van tussengeschoven entiteiten zonder ander primair           in handelsdoel of van transacties die elkaar compenseren of tenietdoen      se of andere soortgelijke kenmerken hebben.                                 ca

Wordt beschouwd als een specifiek wezenskenmerk van categorie C:         Es

1° een constructie met aftrekbare grensoverschrijdende betalingen        1° tussen twee of meer verbonden ondernemingen waarbij ten minste           tra een van de volgende voorwaarden is vervuld:                              as re

a) de ontvanger is in geen van de fiscale rechtsgebieden fiscaal         a) inwoner;                                                                 fis

b) de ontvanger is fiscaal inwoner in een rechtsgebied, maar dat         b) rechtsgebied:                                                            ju

- heft geen vennootschapsbelasting, of heft vennootschapsbelasting       -n tegen een nultarief of bijna-nultarief; of                               àt

- is opgenomen in een lijst van rechtsgebieden van derde landen die      -f door de lidstaten gezamenlijk of in het kader van de OESO als niet-      pa coöperatief zijn beoordeeld;                                             co

c) de betaling geniet een volledige belastingvrijstelling in het         c) rechtsgebied waar de ontvanger fiscaal inwoner is;                       ju

d) de betaling geniet een fiscaal gunstregime in het rechtsgebied waar   d) de ontvanger fiscaal inwoner is;                                         ju

2° in meer dan één rechtsgebied wordt aanspraak gemaakt op               2° aftrekken voor dezelfde afschrijving;                                    de

3° in meer dan één rechtsgebied wordt aanspraak gemaakt op               3° voorkoming van dubbele belasting voor hetzelfde inkomens- of             élé vermogensbestanddeel;                                                    ju

4° een constructie met overdrachten van activa waarbij er een            4° wezenlijk verschil bestaat tussen het bedrag dat in de betrokken         di rechtsgebieden wordt aangemerkt als de voor die activa te betalen        pa vergoeding.

Wordt beschouwd als een specifiek wezenskenmerk van categorie D:           Es

1° een constructie die kan leiden tot het ondermijnen van de               1° rapportageverplichting uit hoofde van de wetgeving ter omzetting           l'o van Uniewetgeving of evenwaardige overeenkomsten inzake de                 lég automatische     uitwisseling     van   inlichtingen   over   financiële   au rekeningen, waaronder overeenkomsten met derde landen, of die              ac profiteert van het gebrek aan die wetgeving of overeenkomsten.             di Dergelijke constructies omvatten ten minste het volgende:                  ce

a) het gebruik van een rekening, product of belegging die geen             a) financiële rekening is of niet als zodanig te boek staat, maar die over    n' eigenschappen beschikt die in wezen vergelijkbaar zijn met die van         m een financiële rekening;                                                   ce

b) de overdracht van financiële rekeningen of activa aan, of het           b) gebruik van rechtsgebieden die niet gebonden zijn aan de                   qu automatische uitwisseling van inlichtingen over financiële rekeningen      co met de staat van verblijf van de relevante belastingplichtige;             ou

c) de herkwalificatie van inkomsten en vermogen in producten of            c) betalingen die niet onder de automatische uitwisseling van                 pa inlichtingen vallen;                                                       d'

d) de overdracht of omzetting van een financiële instelling of een         d) financiële rekening of de activa daarvan in een financiële instelling of   co een financiële rekening of activa die niet onder de rapportage in het      fin kader van de automatische uitwisseling van inlichtingen vallen;            en fin

e) het gebruik van rechtspersonen, juridische constructies of              e) structuren die de rapportage over één of meer rekeninghouders of           su uiteindelijk begunstigden in het kader van de automatische                 tit uitwisseling van inlichtingen over financiële rekeningen stopzetten of     de daartoe strekken;

f) constructies die due-diligenceprocedures die door financiële            f) instellingen worden gebruikt om te voldoen aan hun verplichtingen          ra tot het rapporteren van inlichtingen over financiële rekeningen,           co ondermijnen of zwakke punten ervan benutten, onder meer via het            co gebruik van rechtsgebieden met ontoereikende of zwakke regelingen          pr voor de handhaving van antiwitwaswetgeving of met zwakke                   m transparantievereisten     voor     rechtspersonen      of    juridische   co constructies;                                                              in pe

2° een constructie waarbij de juridische of feitelijke eigendom niet-      2° transparant is door het gebruik van personen, juridische constructies      ef of structuren:                                                             co

a) die geen wezenlijke economische, door voldoende personeel,              a) uitrusting, activa en gebouwen ondersteunde activiteit uitoefenen; en      s'a lo

b) die zijn opgericht in, worden beheerd in, inwoner zijn van, onder       b) zeggenschap staan in, of gevestigd zijn in een ander rechtsgebied dan      to het rechtsgebied van verblijf van een of meer van de uiteindelijk          pl begunstigden van de activa die door die personen, juridische               pe constructies of structuren worden aangehouden; en

c) indien de uiteindelijk begunstigden van die personen, juridische        c) constructies of structuren, zoals bedoeld in artikel 4, 27°, van de wet    ju van 18 september 2017 tot voorkoming van het witwassen van geld            se en de financiering van terrorisme en tot beperking van het gebruik van     et contanten, niet-identificeerbaar zijn gemaakt.                             es

Wordt beschouwd als een specifiek wezenskenmerk van categorie E:           Es

1° een constructie met gebruik van unilaterale veiligehavenregels;         1° un

2° een constructie met overdracht van moeilijk te waarderen                2° immateriële activa. De term "moeilijk te waarderen immateriële             év activa" omvat immateriële activa of rechten op immateriële activa          de waarvoor, op het tijdstip van de overdracht ervan tussen verbonden         les ondernemingen:                                                             as

a) geen betrouwbare vergelijkbare activa bestaan; en                       a)

b) de prognoses van de toekomstige kasstromen of inkomsten die             b) naar verwachting uit de overgedragen activa voortvloeien, of de            les aannames die worden gebruikt voor het waarderen van de                     tra immateriële activa, bijzonder onzeker zijn, waardoor het moeilijk is te    so voorspellen hoe succesvol de immateriële activa op het moment van          qu de overdracht uiteindelijk zullen zijn;                                    au

3° een constructie met een grensoverschrijdende overdracht binnen          3° de groep van functies, en/of risico's en/of activa, indien de geraamde     fo jaarlijkse winst vóór interest en belastingen (ebit) van de overdrager     bé of overdragers, tijdens de periode van drie jaar na de overdracht,         an minder dan 50 % bedraagt van de geraamde jaarlijkse ebit van die           an overdrager of overdragers indien de overdracht niet had                    ét plaatsgevonden.
----------                                                                 -- Nota:                                                                      No
(1) Moeten eveneens de inlichtingen verstrekt worden over de in deze wet   (1 bedoelde meldingsplichtige grensoverschrijdende constructies waarvan de    tra eerste stap is geïmplementeerd tussen 25 juni 2018 en 01.07.2020. Deze     la

inlichtingen over die meldingsplichtige grensoverschrijdende constructies worden      Ce uiterlijk op 31 augustus 2020 meegedeeld (art. 61, lid 2).                            dé

###### Art. 289bis/3

(ingevoegd bij art. 22 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

§ 1. Elke intermediair moet de in artikel 289bis, § 6/3 bedoelde                      § inlichtingen,      over       meldingsplichtige         grensoverschrijdende          co constructies waarvan zij kennis, bezit of controle hebben verstrekken                 l'a aan de in artikel 289bis, § 2, 6°, bedoelde Belgische bevoegde                        co autoriteit binnen 30 dagen te rekenen vanaf het hierna vermelde                       d' geval dat het eerst plaatsvindt:                                                      m

- de dag nadat de meldingsplichtige grensoverschrijdende constructie                  -l voor implementatie beschikbaar is gesteld; of                                         di

- de dag nadat de meldingsplichtige grensoverschrijdende constructie                  - gereed is voor implementatie; of                                                      l'o

- het ogenblik dat de eerste stap in de implementatie van de                          - meldingsplichtige grensoverschrijdende constructie is ondernomen.                     tra

Onverminderd het eerste lid moeten de intermediairs bedoeld in                        No artikel 289bis/1, 4°, tweede lid, eveneens inlichtingen verstrekken                   4° met betrekking tot een meldingsplichtige grensoverschrijdende                         in constructie binnen 30 dagen te rekenen vanaf de dag nadat zij,                        l'o rechtstreeks of via andere personen, hulp, bijstand of advies hebben                  len verstrekt.                                                                            d'a

§ 2. Wanneer de intermediair inlichtingen over meldingsplichtige                      §2 grensoverschrijdende constructies moet verstrekken aan de                             pl bevoegde autoriteiten van meer dan één lidstaat dan verstrekt hij                     fa deze inlichtingen enkel aan de Belgische bevoegde autoriteit indien                   l'a België als eerste op de onderstaande lijst voorkomt:                                  pl

1° de lidstaat waar de intermediair fiscaal inwoner is;                               1° fis

2° de lidstaat waar de intermediair een vaste inrichting heeft via                    2° welke de diensten met betrekking tot de constructie worden                            ét verstrekt;                                                                            co

3° de lidstaat waar de intermediair is opgericht of onder toepassing                  3° van de wetten valt;                                                                   dr

4° de lidstaat waar de intermediair is ingeschreven bij een                           4° beroepsorganisatie in verband met de verstrekking van juridische,                     d' fiscale of adviesdiensten.                                                            ju

Wanneer er op grond van het eerste lid een meervoudige                                Lo meldingsplicht bestaat, wordt de intermediair ontheven van het                        dé verstrekken van de inlichtingen als hij een schriftelijk bewijs voorlegt              de dat dezelfde inlichtingen in een andere lidstaat zijn verstrekt.                      in

###### Art. 289bis/4

(ingevoegd bij art. 23 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

Indien het gaat om een marktklare constructie moet de intermediair                    Da om de drie maanden een periodiek verslag opstellen met een                            ét overzicht van nieuwe meldingsplichtige inlichtingen zoals bedoeld in                  co artikel 289bis, § 6/3, 1°, 4°, 7° en 8°, die sinds het laatste ingediende             dé verslag beschikbaar zijn geworden.                                                    de

De intermediair die het uniek referentienummer van de bevoegde                        L'i instanties ontvangt, dient dit, samen met de samenvatting                             co betreffende de gemelde constructie, onverwijld aan de andere                          ré betrokken intermediairs en aan de relevante belastingplichtige door                   im te geven.

###### Art. 289bis/5

(ingevoegd bij art. 24 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

Naar aanleiding van de melding van een grensoverschrijdende                           A constructie die ten minste één van de in artikel 289bis /2 vermelde                   m wezenskenmerken bezit, wordt een uniek referentienummer                               nu toegekend, dat naar aanleiding van elke volgende melding                              dé betreffende diezelfde grensoverschrijdende constructie moet                           co worden meegedeeld, zowel voor meldingen door elke betrokken                           in intermediair als voor meldingen door de relevante belastingplichtige.

De intermediair die het uniek referentienummer van de bevoegde                        L'i instanties ontvangt, dient dit, samen met de samenvatting                             co betreffende de gemelde constructie, onverwijld aan de andere                          ré betrokken intermediairs en aan de relevante belastingplichtige door                   im te geven.

###### Art. 289bis/6

(ingevoegd bij art. 25 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

Wanneer meerdere intermediairs betrokken zijn bij dezelfde                            Si meldingsplichtige grensoverschrijdende constructie, moeten alle                       tra betrokken intermediairs de inlichtingen verstrekken over de                           in meldingsplichtige grensoverschrijdende constructie.                                   di

Een intermediair wordt ontheven van de verplichting tot het                           Un verstrekken van inlichtingen indien hij een schriftelijk bewijs voorlegt              fo dat een andere intermediair de inlichtingen bedoeld in artikel 289bis,                in
§ 6/3, tweede lid, reeds heeft verstrekt.

###### Art. 289bis/7

(§ 1, lid 1, 1°, vernietigd door het arrest 1/2024 van 11.01.2024 van het             (§ Grondwettelijk Hof, wordt hersteld, en § 4, ingevoegd bij art. 30 van de wet van      Co 16.03.2026 (B.S., 01.04.2026). Tekst van toepassing vanaf 11.04.2026 (art. -))        (M

§ 1. Wanneer een intermediair gebonden is door een beroepsgeheim,                     §1 is hij gehouden:

1° de betrokken intermediair of intermediairs schriftelijk en                         1° gemotiveerd op de hoogte te brengen dat hij niet aan de                               m meldingsplicht      kan     voldoen,     waardoor       deze     meldingsplicht       su automatisch rust op de andere intermediair of intermediairs;                          au in

2° bij gebreke aan een andere intermediair, de relevante                              2° belastingplichtige of belastingplichtigen schriftelijk en gemotiveerd                 fa op de hoogte te brengen van zijn of hun meldingsplicht.                               ob

De ontheffing van de meldingsplicht krijgt slechts uitwerking op het                  La tijdstip dat een intermediair voldaan heeft aan de in het eerste lid                  m bedoelde verplichting.

§ 2. De relevante belastingplichtige kan de intermediair door                         § schriftelijke instemming toelaten alsnog te voldoen aan de in artikel                 à 289bis/3 bedoelde meldingsplicht.                                                     l'a

Indien de relevante belastingplichtige geen instemming verleent blijft                Si de meldingsplicht bij de belastingplichtige en bezorgt de intermediair                dé de nodige gegevens voor het vervullen van de in artikel 289bis/3                      fo bedoelde meldingsplicht aan de relevante belastingplichtige.                          dé

§ 3. Geen beroepsgeheim overeenkomstig paragraaf 1 of ontheffing                      § van    rechtswege        kan     worden      ingeroepen        aangaande       de     di meldingsplicht van marktklare constructies die aanleiding geven tot                   dé een periodiek verslag overeenkomstig artikel 289bis/4.                                ra

§ 4. In afwijking van paragraaf 1, eerste lid, 1°, is de intermediair die             §4 een advocaat is, niet gehouden een betrokken intermediair die niet de                 es cliënt is op de hoogte te brengen dat hij niet aan de meldingsplicht kan              n' voldoen.                                                                              dé

###### Art. 289bis/8

(ingevoegd bij art. 27 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

§ 1. In de volgende gevallen ligt de meldingsplicht bij de relevante                  § belastingplichtige:                                                                   co

1° wanneer er geen intermediair betrokken was bij het bedenken,                       1° aanbieden, opzetten, beschikbaar maken voor implementatie of het                      co beheren        voor    implementatie         van      de      meldingsplichtige       m grensoverschrijdende constructie; of                                                  tra

2° wanneer de intermediair ontheven is van de verplichting om                         2° inlichtingen te verstrekken overeenkomstig artikel 289bis/7, § 1, en                  in hij de relevante belastingplichtige of belastingplichtigen op de hoogte               le heeft gesteld van zijn of hun meldingsplicht, overeenkomstig artikel                  dé 289bis/7, § 1, 2°.

3° wanneer deze niet de in artikel 289bis/7, § 2, eerste lid bedoelde                 3° toestemming heeft verleend.                                                           28

§ 2. Ingeval de meldingsplicht overeenkomstig paragraaf 1 bij de                      § relevante belastingplichtige ligt, verstrekt deze de inlichtingen binnen              dé dertig dagen, te rekenen vanaf het hierna vermelde geval dat eerst                    in plaatsvindt:                                                                          m

- de dag nadat de meldingsplichtige grensoverschrijdende constructie                  - voor     implementatie         ter    beschikking       van     de     relevante      l'o belastingplichtige is gesteld of;                                                     co

- de dag nadat de meldingsplichtige grensoverschrijdende constructie                  - gereed is voor implementatie door de relevante belastingplichtige of;                 l'o co

- vanaf het ogenblik dat de eerste stap voor de implementatie ervan                   -à met betrekking tot de relevante belastingplichtige is ondernomen.                     ac

§ 3. Wanneer de relevante belastingplichtige inlichtingen over de                     § meldingsplichtige          grensoverschrijdende          constructie        moet      de verstrekken aan de bevoegde autoriteiten van meer dan één lidstaat,                   l'o dan moet hij deze inlichtingen enkel verstrekken aan de Belgische                     m bevoegde autoriteit indien België als eerste op de onderstaande, lijst                à voorkomt:                                                                             pr

1° de lidstaat waar de relevante belastingplichtige fiscaal inwoner is;               1° de

2° de lidstaat waar de relevante belastingplichtige een vaste                         2° inrichting heeft die begunstigde van de constructie is;                               ét

3° de lidstaat waar de relevante belastingplichtige inkomsten                         3° ontvangt      of     winsten       genereert,      hoewel       de     relevante      re belastingplichtige geen fiscaal inwoner van een lidstaat is noch een                  fin vaste inrichting in een lidstaat heeft;                                               da

4° de lidstaat waar de relevante belastingplichtige een activiteit                    4° uitoefent, hoewel de relevante belastingplichtige geen fiscaal                        ac inwoner van een lidstaat is noch een vaste inrichting in een lidstaat                 m heeft.                                                                                m

Wanneer er op grond van het eerste lid een meervoudige                                Lo meldingsplicht bestaat, wordt de relevante belastingplichtige                         dé ontheven van het verstrekken van de inlichtingen als hij een                          tra schriftelijk bewijs voorlegt dat dezelfde inlichtingen in een andere                  m lidstaat zijn verstrekt.
----------                                                                            -- Nota:                                                                                 No
(1) Moeten eveneens de inlichtingen verstrekt worden over de in deze wet              (1 bedoelde meldingsplichtige grensoverschrijdende constructies waarvan de               tra eerste stap is geïmplementeerd tussen 25 juni 2018 en 01.07.2020. Deze                la inlichtingen over die meldingsplichtige grensoverschrijdende constructies worden      Ce uiterlijk op 31 augustus 2020 meegedeeld (art. 61, lid 2).                            dé

###### Art. 289bis/9

(ingevoegd bij art. 28 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

Wanneer de meldingsplicht bij de relevante belastingplichtige ligt en                 Lo er meer dan één relevante belastingplichtige is, worden de                            et inlichtingen overeenkomstig artikel 289bis/8 verstrekt door de                        tra relevante belastingplichtige die als eerste op de onderstaande lijst                  qu voorkomt:

1° de relevante belastingplichtige die de meldingsplichtige                           1° constructie is overeengekomen met de intermediair;                                    di

2° de relevante belastingplichtige die de implementatie van de                        2° constructie beheert.

Een relevante belastingplichtige wordt ontheven van de verplichting                   Un tot het verstrekken van de inlichtingen indien hij een schriftelijk bewijs            tra voorlegt dat een andere relevante belastingplichtige de inlichtingen                  pr bedoeld in artikel 289bis, § 6/3, reeds heeft verstrekt.                              6/

###### Art. 289bis/10

(ingevoegd bij art. 29 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

Voor de toepassing van de artikelen 289bis, § 6/3 en 289bis/1 tot en                  Po met 289bis/9 en de daaruit voortvloeiende uitvoeringsbesluiten dient                  de de melding van de inlichtingen, voor de onderdelen die de Koning                      in nader bepaalt, naast het gebruik van één van de officiële landstalen,                 d' ook in het Engels te gebeuren.                                                        an
----------                                                                            -- Nota:                                                                                 No Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën       L’A of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens,            dir naast het gebruik van één van de officiële landstalen, ook in het Engels moeten       de worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of      1e de relevante belastingplichtige moet worden gebruikt (art. 2). De leidinggevende      co ambtenaar bedoeld in het bovenvermelde KB is de leidinggevende ambtenaar van          l'a de algemene administratie          bevoegd     voor    de vestiging      van de       rev inkomstenbelastingen (art. 1, MB 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289bis/11

(ingevoegd bij art. 30 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

De Koning bepaalt het formulier waarop de intermediair of de                          Le relevante belastingplichtige de verplichtingen opgenomen in de                        co artikelen 289bis/1 tot en met 289bis/9 moeten naleven.                                au
----------                                                                            -- Nota:                                                                                 No Het KB van 03.07.2020 (B.S., 14.07.2020) voorziet dat de Minister van Financiën       L’A of de door hem aangewezen leidinggevende ambtenaar bepaalt welke gegevens,            dir naast het gebruik van één van de officiële landstalen, ook in het Engels moeten       de worden meegedeeld (art. 1) en eveneens het formulier dat door de intermediair of      1e

de relevante belastingplichtige moet worden gebruikt (art. 2). De leidinggevende      co ambtenaar bedoeld in het bovenvermelde KB is de leidinggevende ambtenaar van          l'a de algemene administratie          bevoegd     voor    de vestiging      van de       rev inkomstenbelastingen (art. 1, MB 07.07.2020 (B.S., 14.07.2020)).

###### Art. 289bis/12

(gewijzigd bij art. 18 van de wet van 20.12.2024 (B.S., 31.12.2024). Tekst van        (m toepassing vanaf 31.12.2024 (art. 19))                                                ap

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan                       Le voor de overtreding van de bepalingen van de artikelen 289bis/1 tot                   in en met 289bis/9, evenals van de ter uitvoering ervan genomen                          28 besluiten, die bestaat uit het onvolledig verstrekken van de                          en inlichtingen bedoeld in artikel 289bis, § 6/3, een boete opleggen van 1               § 250 euro tot 12 500 euro. Voor dergelijke overtredingen gedaan met                    in bedrieglijk opzet of het oogmerk te schaden wordt een boete van 2                     nu 500 euro tot 25 000 euro opgelegd.

De door de bevoegde adviseur-generaal gemachtigde ambtenaar kan                       Le voor de overtreding van de bepalingen van de artikelen 289bis/1 tot                   in en met 289bis/9, evenals van de ter uitvoering ervan genomen                          28 besluiten, die bestaat uit het niet of laattijdig verstrekken van de                  ne inlichtingen bedoeld in artikel 289bis, § 6/3, een boete opleggen van 5               28 000 euro tot 50 000 euro. Voor dergelijke overtredingen gedaan met                    te bedrieglijk opzet of het oogmerk te schaden wordt een boete van 12                    de 500 euro tot 100 000 euro opgelegd.

De Koning legt de progressieve schaal van de administratieve                          Le geldboetes vast en regelt hun toepassingsmodaliteiten.                                les

De Koning kan voor de geldboeten die Hij bepaalt, voorzien in de                      Le toepassingsmodaliteiten van de maatregelen tot individualisering van                  d'a de sanctie door de bevoegde rechter.                                                  co

###### Art. 289bis/13

(ingevoegd bij art. 32 van de wet van 20.12.2019 (B.S., 30.12.2019). Tekst van        (in toepassing vanaf 01.07.2020 (art. 61, lid 1) en overgangsbepaling (art. 61, lid 2))   àp

(Bij arrest van 15.09.2022 (nr. 103/2022), heeft het Grondwettelijk Hof art.          (P 289bis/13 W.Reg. vernietigd)                                                          an

De fiscale administratie, mag binnen de door haar bepaalde termijn,                   L'a welke wegens wettige redenen kan worden verlengd, voor zover zij                      co die informatie nodig acht om de correcte naleving van de artikelen                    ra

289bis/1 tot en met 289bis/11 te verzekeren, van de betrokken                    so intermediair(s) alle informatie vorderen die in toepassing van artikel           28 289bis/1 tot en met 289bis/11 diende te worden gemeld aan de                     28 Belgische bevoegde autoriteit.                                                   co

###### Art. 289ter

(ingevoegd bij art. 11 van de wet van 07.02.2021 (B.S., 19.02.2021). Tekst van   (in toepassing vanaf 01.03.2021 (art. -))                                            àp

De Koning bepaalt de wijze van betaling van alle bedragen die                    Le krachtens de bepalingen van dit Wetboek en de uitvoeringsbesluiten               ve ervan verschuldigd zijn, andere dan de strafrechtelijke boetes.                  ce

###### Art. 289quater

(tekst niet in werking getreden)

(ingevoegd bij art. 81 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289quinquies

(tekst niet in werking getreden)

(ingevoegd bij art. 82 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289sexies

(ingevoegd bij art. 83 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van    (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                  àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum              vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))       dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van        (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf      12 09.06.2024 (art. -))                                                              09

(…)                                                                               (…

###### Art. 289septies

(§ 1, opgeheven bij art. 216 van de wet van 12.05.2024 (B.S., 30.05.2024 –        (§ ed. 2). Tekst van toepassing vanaf 09.06.2024 (art. -))                           Te

(…) (1)                                                                           (…
----------                                                                        -- Nota:                                                                             No
(1) § 2, ingevoegd bij art. 84 van de wet van 26.01.2021 (B.S., 10.02.2021) die   (1 nooit in werking is getreden wordt opgeheven bij art. 213 van de wet van          n’e 12.05.2024 (B.S., 30.05.2024 – ed. 2).                                            (M

###### Art. 289octies

(tekst niet in werking getreden)

(ingevoegd bij art. 85 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van    (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                  àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum              vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))       dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van        (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf      12 09.06.2024 (art. -))                                                              09

(…)                                                                               (…

###### Art. 289nonies

(tekst niet in werking getreden)

(ingevoegd bij art. 86 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van    (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                  àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum              vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))       dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289decies

(tekst niet in werking getreden)

(ingevoegd bij art. 87 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289undecies

(tekst niet in werking getreden)

(ingevoegd bij art. 88 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289duodecies

(tekst niet in werking getreden)

(ingevoegd bij art. 89 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

###### Art. 289terdecies

(tekst niet in werking getreden)

(ingevoegd bij art. 90 van de wet van 26.01.2021 (B.S., 10.02.2021). Tekst van   (in toepassing vanaf 01.01.2025 (art. 219, lid 1). De Koning kan een                 àp inwerkingtreding voorafgaand aan de in het eerste lid vermelde datum             vig vastleggen voor de verschillende bepalingen van deze wet (art. 219, lid 2))      dis

(de wet van 26.01.2021 (B.S., 10.02.2021) wordt opgeheven bij art. 213 van       (la de wet van 12.05.2024 (B.S., 30.05.2024 – ed. 2). Tekst van toepassing vanaf     12 09.06.2024 (art. -))                                                             09

(…)                                                                              (…

## INTREKKINGSBEPALING

###### Art. 290

Onder voorbehoud van de bijzondere fiscale bepalingen voortvloeiend              So hetzij uit door den Staat gesloten en bij een wet goedgekeurde                   co contracten, hetzij uit internationale overeenkomsten, worden alle                co vroegere wetsbepalingen betreffende registratie-, hypotheek- of                  lég griffierechten ingetrokken.                                                      d’

## TIJDELIJKE BEPALINGEN

#### Afdeling I - Maatregelen waarbij de oprichting van nieuwe                       S gebouwen begunstigd wordt door een vermindering der registratierechten

§ 1 - Aankoop van een bouwgrond

###### Art. 291

(zonder voorwerp geworden)

(…)                                                                              (…

###### Art. 292

(niet meer van toepassing)

(…)                                                            (…

###### Art. 293

(zonder voorwerp geworden)

(…)                                                            (…

###### Art. 294

(niet meer van toepassing)

(…)                                                            (…

###### Art. 295

(niet meer van toepassing)

(…)                                                            (…

###### Art. 296

(zonder voorwerp geworden)

(…)                                                            (…

§ 2 - Verkoop van een gebouwd onroerend goed

###### Art. 297

(niet meer van toepassing)

(…)                                                            (…

###### Art. 298

(zonder voorwerp geworden)

(…)                                                            (…

###### Art. 299

(niet meer van toepassing)

(…)                                                            (…

#### Afdeling II - Diverse bepalingen

###### Art. 300

(opgeheven bij art. 32 van de wet van 12.07.1960 (B.S., 09.11.1960). Tekst      (ab van toepassing vanaf 01.01.1961 (art. 39))                                      ap

(…)                                                                             (…

###### Art. 301

(1°, gewijzigd bij art. 5 van de wet van 31.07.2023 (B.S., 23.08.2023). Tekst   (1 van toepassing vanaf 02.09.2023 (art. -))                                       ap

Zijn van de formaliteit van registratie vrijgesteld:                            So

1° Akten in der minne betreffende de leningen toegestaan door de                1 Centrale Dienst voor sociale en culturele actie van het Ministerie van          d'a Landsverdediging.

2° Akten, vonnissen en arresten betreffende de uitvoering van de                2 wetten op het herstel van oorlogsschade; minnelijke akten                       ré betreffende leningen en kredietopeningen toegekend aan de                       pr geteisterden om hun toe te laten de schade te herstellen die zijn               pe geleden hebben ingevolge oorlogsfeiten, wanneer deze leningen en                gu kredietopeningen worden toegestaan volgens de voorzieningen van                 se de ter zake geldende wettelijke beschikkingen, door een in deze                 or beschikkingen bedoelde kredietinstelling.

3° Akten van overdracht en inpandgeving van vorderingen tot herstel             3 van oorlogsschade;                                                              po

4° (…)                                                                          4

5° (…)                                                                          5

6° Akten van procedure voor de gemengde scheidsgerechten                        6 ingesteld bij de vredesverdragen, waaronder de beslissingen en de               in betekening ervan.                                                               sig

7° Akten, vonnissen en arresten betreffende de rechtsplegingen tot              7° wettiging van de kinderen wier ouders, ten gevolge van den oorlog,              lég zich in de onmogelijkheid hebben bevonden een huwelijk aan te gaan.             la

8° (…)                                                                          8°

8°bis (…)                                                                        8°

9° De akten, vonnissen en arresten die betrekking hebben op de                   9° tenuitvoerlegging van de wet betreffende de verklaringen van                     re overlijden en van vermoedelijk overlijden, alsmede betreffende de                tra overschrijving en de verbetering van sommige akten van de burgerlijke stand.

10° De akten en vonnissen betreffende de rechtsplegingen vóór de                 10 vrederechters bedoeld bij de wet houdende uitzonderingsbepalingen                de in zake huishuur, wanneer het jaarlijks bedrag van de huurprijs,                 m eisbaar op het ogenblik van de indiening van de eis, niet hoger is dan           m 300 EUR.

###### Art. 301bis

(opgeheven bij art. 72, 1° van de wet van 29.03.1962 (B.S., 12.04.1962). Tekst   (ab van toepassing vanaf 202.04.1962 (art. 77))                                      ap

(…)                                                                              (…

###### Art. 301ter

(impliciet opgeheven bij art. 2 van de wet van 24.01.1958 (B.S., 14.02.1958).    (ab Tekst van toepassing vanaf 24.02.1958 (art. -))                                  Te

(…)                                                                              (…

###### Art. 301quater

(ingevoegd bij art. 3 van de wet van 25.05.1951 (B.S., 31.05.1951). Tekst van    (in toepassing vanaf 10.06.1951 (art. -))                                            àp

Kosteloos worden geregistreerd de akten, waarbij aan de                          So gerechtigden van de wet van 1 oktober 1947 betreffende de                        de herstelling van de oorlogsschade aan private goederen, uit de hand               de woonhuizen worden verkocht die op initiatief van de Staat met het                l'in oog op de huisvesting van de geteisterden door oorlogsfeit werden                de gebouwd.

###### Art. 302

Akten betreffende de ambtshalve tenuitvoerlegging van de                       So beslissingen van de bij de vredesverdragen ingestelde gemengde                 dé scheidsgerechten worden in debet geregistreerd.                                pa

###### Art. 302bis

(aangevuld bij art. 9 van de wet van 04.08.1978 (B.S. 17.08.1978). Tekst van   (co toepassing vanaf 27.08.1978 (art. -))                                          ap

§ 1. Wordt van het evenredig recht vrijgesteld, de inbreng in                  § vennootschappen die de rechtspersoonlijkheid bezitten en die de                po verwezenlijking nastreven van verrichtingen als bedoeld bij artikel 10         op van de wet betreffende de economische expansie.

Te dien einde, zal de Minister die Economische zaken,                          A Streekeconomie of Middenstand in zijn bevoegdheid heeft, vóór het              ré verlijden van de akte een bewijsstuk afgeven, waarvan de                       pr afgiftemodaliteiten door de Koning worden bepaald. Dit stuk moet               m aan de akte worden gehecht op het ogenblik van de registratie.                 êt

§     2.       Wordt,    overeenkomstig         de     voorwaarden       en    § toepassingsmodaliteiten als bepaald in § 1, van het evenredig recht            m vrijgesteld,     de     inbreng      in   vennootschappen        die     de    po rechtspersoonlijkheid bezitten en die in titel I, artikel 2, van de wet tot    la economische heroriëntering zijn bedoeld.

###### Art. 302ter

(opgeheven bij art. 27 van de wet van 30.10.2025 (B.S., 24.11.2025). Tekst     (ab van toepassing vanaf 25.11.2025 (art. 28))                                     ap

(…)                                                                            (…

###### Art. 302quater

(opgeheven bij art. 15, 1° van de wet van 24.12.1993 (B.S., 31.12.1993 - ed.   (ab 2). Tekst van toepassing vanaf 01.01.1994 (art. 26))                           Te

(…)                                                                            (…

###### Art. 303

(gewijzigd bij art. 23 van het Besl. Secr. Gen. van 30.06.1941 (B.S., 13.07.1941).   (m Tekst van toepassing vanaf 23.07.1941 (art. -))                                      Te

Worden van hypotheekrecht vrijgesteld:                                               So

1° hypothecaire inschrijvingen genomen tot waarborg van de in                        1° artikel 301, 1° en 2°, bedoelde leningen en kredietopeningen;                        cr

2° Inschrijvingen genomen ter uitvoering van de wet van 27 maart                     2 1924, betreffende de Nationale Vereniging van nijveraars en                          co handelaars voor het herstel der oorlogsschade.                                       po

###### Art. 304

(aangevuld     bij    art.   39      samengeordende        wetten      houdende      (co uitzonderingsbepalingen inzake huishuur gecoördineerd door Besluit Regent van        ex 31.01.1949 (B.S., 23.02.1949). Tekst van toepassing vanaf 05.03.1949 (art. -))       31

Is vrij van rolrecht, de inschrijving van de zaken waarvan vonnissen en              Es arresten krachtens artikel 301 vrijstelling van de registratieformaliteit            les genieten.                                                                            l’e

De vonnissen en arresten zijn vrij van expeditierecht.                               Le d’

Die vrijstellingen zijn evenwel niet toepasselijk in het geval bedoeld bij           To artikel 301, 10°.                                                                    àl

###### Art. 304bis

(opgeheven bij art. 15, 2° van de wet van 24.12.1993 (B.S., 31.12.1993 - ed.         (ab 2). Tekst van toepassing vanaf 01.01.1994 (art. 26))                                 Te

(…)                                                                                  (…

###### Art. 305

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst          (ab van toepassing vanaf 01.01.1990 (art. 244))                                          ap

(…)                                                                                  (…

###### Art. 305bis

(opgeheven bij art. 5, 2° van de wet van 06.08.1967 (B.S., 20.09.1967). Tekst   (ab van toepassing vanaf 30.09.1967 (art. -))                                       ap

(…)                                                                             (…

## OVERGANGSBEPALINGEN

#### Afdeling I - Algemene maatregelen

###### Art. 306

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (ab van toepassing vanaf 01.01.1990 (art. 244))                                     ap

(…)                                                                             (…

###### Art. 307

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (ab van toepassing vanaf 01.01.1990 (art. 244))                                     ap

(…)                                                                             (…

###### Art. 308

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (ab van toepassing vanaf 01.01.1990 (art. 244))                                     ap

(…)                                                                             (…

###### Art. 309

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst     (ab van toepassing vanaf 01.01.1990 (art. 244))                                     ap

(…)                                                                             (…

###### Art. 310

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

###### Art. 311

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

###### Art. 312

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

###### Art. 313

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

###### Art. 314

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst   (ab van toepassing vanaf 01.01.1990 (art. 244))                                   ap

(…)                                                                           (…

#### Afdeling II - Bijzondere maatregelen

§ 1. Overdrachten onder bezwarende titel van onroerende goederen

###### Art. 315

(opgeheven bij art. 42 van de wet van 19.07.1979 (B.S., 22.08.1979). Tekst       (ab van toepassing vanaf 01.01.1980 (art. 45, § 1, 4°))                              ap

(…)                                                                              (…

###### Art. 316

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (ab van toepassing vanaf 01.01.1990 (art. 244))                                      ap

(…)                                                                              (…

§ 2. Burgerlijke en handelsvennootschappen

###### Art. 317

(opgeheven bij art. 213 van de wet van 22.12.1989 (B.S., 29.12.1989). Tekst      (ab van toepassing vanaf 01.01.1990 (art. 244))                                      ap

(…)                                                                              (…

###### Art. 318

(opgeheven bij art. 19, 2° van de wet van 14.04.1965 (B.S., 24.04.1965). Tekst   (ab van toepassing vanaf 04.05.1965 (art. -))                                        ap

(…)                                                                              (…

## BIJBEPALINGEN BETREFFENDE DE MET HET ZEGEL

## GELIJKGESTELDE TAKSEN

###### Art. 319

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969).   (ab Tekst van toepassing vanaf 01.01.1971 (art. 98))                                 Te

(…)                                                                              (…

###### Art. 320

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969).   (ab Tekst van toepassing vanaf 01.01.1971 (art. 98))                                 Te

(…)                                                                              (…

###### Art. 321

(impliciet opgeheven bij art. 94 van de wet van 03.07.1969 (B.S., 17.07.1969).   (ab Tekst van toepassing vanaf 01.01.1971 (art. 98))                                 Te

(…)                                                                              (…

## INWERKINGTREDING

###### Art. 322

Dit besluit treedt in werking op 1 Februari 1940.                                Le
