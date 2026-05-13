---
tags: ["VI.A", "2.4"]
itaa-lex-sectie: "VI.A"
wet: "Richtlijn 2006/112/EG van de Raad betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "11.12.2006"
bron: "onbekend"
chunk:
  level: 6
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/BTW-richtlijn-2006-112.pdf
      sha256: d2e9f9e0e1ba01e3822dab19047137bf146cfbee10bc4f9d823c53587f91110d
      version: 11.12.2006
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: f4076ba
    model:
    prompt_version:
  generated_at: '2026-05-13T13:18:44Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:21:02Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Concord region-fallback strip is succesvol toegepast: alle eerder aanwezige fake '###### Art. <num>' headings in Bijlage XII - CONCORDANTIETABEL (regio na regel 3055) zijn gedemoteerd naar plain text. Grep op '^###### Art\\.' geeft 0 hits. De hoofdtekst body (Art. 1-414) blijft volledig intact: 205 '###### Artikel <num>'-headings staan nog overeind (sample Art. 1 op regel ~430, ## TITEL I t/m XV en ## Deel A/B / Bijlage IX/X/XI structuur ongewijzigd). De concordantietabel-inhoud is leesbaar als doorlopende tekst en vervuilt de heading-structuur niet langer, wat de hiërarchie-sprong (TITEL ## → Artikel ######) elders herstelt zonder false-positive artikel-anchors voor RAG-chunking te creëren."
    layer1:
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:21:02Z'
      rationale: "Concord region-fallback strip is succesvol toegepast: alle eerder aanwezige fake '###### Art. <num>' headings in Bijlage XII - CONCORDANTIETABEL (regio na regel 3055) zijn gedemoteerd naar plain text. Grep op '^###### Art\\.' geeft 0 hits. De hoofdtekst body (Art. 1-414) blijft volledig intact: 205 '###### Artikel <num>'-headings staan nog overeind (sample Art. 1 op regel ~430, ## TITEL I t/m XV en ## Deel A/B / Bijlage IX/X/XI structuur ongewijzigd). De concordantietabel-inhoud is leesbaar als doorlopende tekst en vervuilt de heading-structuur niet langer, wat de hiërarchie-sprong (TITEL ## → Artikel ######) elders herstelt zonder false-positive artikel-anchors voor RAG-chunking te creëren."
      concrete_problemen:
        - Concordantietabel-inhoud in Bijlage XII (regels ~3050-3140) is nog steeds rauw uit PDF gevallen en bevat afgebroken zinnen ('Art. 24. bis, eerste alinea, eerste tot en' / 'met twaalfde streepje Artikel 287...') — lage retrieval-waarde, maar nu wel correct als body-text en niet als heading.
        - 'Hiërarchie-sprong (## TITEL → ###### Artikel, ### #### ##### overgeslagen) blijft bestaan; dit is een aparte parser-issue, niet binnen scope van de concord-fix.'
---

# Richtlijn 2006/112/EG van de Raad betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde

*Bijgewerkt tot en met 11.12.2006 — gecoördineerde versie.*

## betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde

DE RAAD VAN DE EUROPESE UNIE,

Gelet op het Verdrag tot oprichting van de Europese Gemeen- schap, en met name op artikel 93,

Gezien het voorstel van de Commissie,

Gezien het advies van het Europees Parlement,

Gezien het advies van het Europees Economisch en Sociaal Comité,

## Overwegende hetgeen volgt:

(1) Richtlijn 77/388/EEG van de Raad van 17 mei 1977 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting — Gemeenschappelijk stelsel van belasting over de toegevoegde waarde: uniforme grondslag ( 1 ) is herhaaldelijk en ingrijpend gewijzigd. Nu deze richtlijn opnieuw wordt gewijzigd, dient ter wille van de duidelijkheid van de tekst tot herschikking van deze richtlijn te worden overgegaan.

(2) Bij deze herschikking moeten de nog toepasselijke bepalin- gen van Richtlijn 67/227/EEG van de Raad van 11 april 1967 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting ( 2 ) worden overgenomen. De genoemde richtlijn dient bijgevolg te worden ingetrok- ken.

(3) Een heldere en rationele presentatie van de bepalingen, overeenkomstig het beginsel van betere regelgeving, vergt dat de structuur en de formulering van de richtlijn worden herschikt, waarbij evenwel in principe geen materiële wijzigingen in de bestaande wetgeving worden aangebracht. Niettemin moet een gering aantal materiële wijzigingen die inherent zijn aan de herschikkingsexercitie, in de tekst worden aangebracht. De wijzigingen in kwestie zijn limitatief vermeld in de bepalingen betreffende omzetting en inwerkingtreding.

(4) Het verwezenlijken van de doelstelling een interne markt in te stellen vooronderstelt dat in de lidstaten wetgevingen inzake omzetbelasting worden toegepast die de

(10) Gedurende deze overgangsperiode moeten de intracommu- nautaire handelingen die worden verricht door andere belastingplichtigen dan vrijgestelde belastingplichtigen, in de lidstaten van bestemming worden belast op basis van de tarieven en voorwaarden van die lidstaten.

(11) Gedurende deze overgangsperiode moet in de lidstaten van bestemming eveneens belasting worden geheven, op basis van de tarieven en voorwaarden van die lidstaten, op de intracommunautaire verwervingen die voor een bepaald bedrag worden verricht door vrijgestelde belastingplichti- gen of door niet-belastingplichtige rechtspersonen, alsmede op bepaalde intracommunautaire afstandsverkopen en leveringen van nieuwe vervoermiddelen aan particulieren of aan vrijgestelde of niet-belastingplichtige lichamen, voor zover deze handelingen bij ontstentenis van bijzondere bepalingen de mededinging tussen de lidstaten ernstig zouden kunnen verstoren.

(12) Bepaalde grondgebieden dienen, om redenen die verband houden met hun geografische, economische en sociale positie, van de werkingssfeer van deze richtlijn te worden uitgesloten.

(13) Het begrip „ belastingplichtige ” moet zodanig worden gedefinieerd, dat de lidstaten, teneinde een betere belasting- neutraliteit te waarborgen, in staat worden gesteld hieron- der personen te laten vallen die incidenteel handelingen verrichten.

(14) Het begrip „ belastbare handeling ” kan leiden tot moeilijk- heden, met name wat betreft de met belastbare handelingen gelijkgestelde handelingen. Het is derhalve noodzakelijk deze begrippen nader te omschrijven.

(15) Ter vergemakkelijking van het intracommunautaire verkeer op het terrein van bewerkingen van roerende lichamelijke zaken is het dienstig belastingregels terzake vast te stellen wanneer die bewerkingen worden verricht voor afnemers die voor BTW-doeleinden geïdentificeerd zijn in een andere lidstaat dan die waar de dienst daadwerkelijk wordt verricht.

(16) Het is dienstig vervoer dat op het grondgebied van een lidstaat wordt verricht, wanneer het rechtstreeks verband houdt met tussen lidstaten verricht vervoer, gelijk te stellen aan intracommunautair goederenvervoer, teneinde niet alleen de belastingbeginselen en -regels voor deze binnen- landse vervoerdiensten te vereenvoudigen, maar ook die welke van toepassing zijn op de daarmee samenhangende diensten alsmede op de diensten welke worden verricht door tussenpersonen die bij het verrichten van deze verschillende diensten bemiddelen.

(24) De begrippen „ belastbaar feit ” en „ verschuldigheid van de belasting ” moeten worden geharmoniseerd, opdat de toepassing en de latere wijzigingen van het gemeenschap- pelijk BTW-stelsel in alle lidstaten op hetzelfde tijdstip ingaan.

(25) De maatstaf van heffing moet worden geharmoniseerd, opdat de toepassing van de BTW op de belastbare handelingen in alle lidstaten tot vergelijkbare resultaten leidt.

(26) De lidstaten moeten zich in bepaalde welomschreven omstandigheden kunnen uitspreken over de waarde van goederenleveringen, diensten en intracommunautaire ver- wervingen, teneinde te voorkomen dat zij, doordat via het inschakelen van verbonden partijen een belastingvoordeel wordt behaald, belastinginkomsten derven.

(27) Teneinde fraude of belastingontwijking te bestrijden, moeten de lidstaten in de maatstaf van heffing voor een handeling waarbij door een afnemer ter beschikking gesteld beleggingsgoud wordt verwerkt, de waarde van dat beleg- gingsgoud kunnen opnemen wanneer dit goud ingevolge de verwerking niet meer als beleggingsgoud kan worden aangemerkt. De lidstaten dient een zekere beoordelings- ruimte te worden gelaten bij de toepassing van deze maatregelen.

(28) De afschaffing van de belastinggrenzen impliceert, wil men verstoringen van de mededinging voorkomen, niet alleen een uniforme BTW-grondslag, doch tevens een aantal tarieven en tariefhoogten in de lidstaten die elkaar voldoende benaderen.

(29) Het normale BTW-tarief dat in de diverse lidstaten van kracht is, zorgt er in combinatie met voorschriften van de overgangsregeling voor dat dit stelsel in aanvaardbare mate functioneert. Om te voorkomen dat de verschillen in het normale BTW-tarief dat de lidstaten toepassen, tot structurele onevenwichtigheden in de Gemeenschap en tot verstoringen van de mededinging in bepaalde bedrijfs- sectoren leiden, dient de ondergrens van het normale tarief op 15 % te worden bepaald, welk cijfer opnieuw kan worden bezien.

(30) Om de BTW-neutraliteit te waarborgen, zouden de door de lidstaten toegepaste tarieven de normale aftrek van de voorbelasting mogelijk moeten maken.

(31) Tijdens de overgangsperiode moeten bepaalde afwijkingen inzake aantal en hoogte van de tarieven mogelijk zijn.

(32) Voor een beter begrip van het effect van de verlaagde tarieven is een evaluatierapport van de Commissie over het effect van de verlaagde tarieven op lokale diensten, met name wat het scheppen van werkgelegenheid, de econo- mische groei en de goede werking van de interne markt betreft, noodzakelijk.

ook te kunnen worden toegepast op bepaalde diensten die het karakter van een investeringsgoed hebben.

(41) Nader dient te worden bepaald wie tot voldoening van de belasting gehouden is, met name voor bepaalde diensten verricht door niet in de lidstaat waar de belasting verschuldigd is gevestigde dienstverrichters.

(42) De lidstaten moeten in specifieke gevallen de afnemer van goederen of diensten kunnen aanwijzen als de tot voldoe- ning van de BTW gehouden persoon. Dit moet de lidstaten helpen in bepaalde sectoren en bij bepaalde soorten handelingen de regelgeving te vereenvoudigen en belasting- fraude en -ontwijking aan te pakken.

(43) De lidstaten moeten vrijelijk kunnen blijven bepalen wie tot voldoening van de belasting bij invoer gehouden is.

(44) De lidstaten moeten kunnen bepalen dat een ander dan de tot voldoening van de belasting gehouden persoon hoofdelijk verplicht is de belasting te voldoen.

(45) De verplichtingen van de belastingplichtigen moeten zoveel mogelijk worden geharmoniseerd teneinde de nodige waarborgen te verkrijgen met betrekking tot de gelijkheid van de belastingheffing in alle lidstaten.

(46) Elektronische facturering moet zodanig zijn opgezet dat de belastingdiensten hun controlerende taak kunnen verrich- ten. Voor een goede werking van de interne markt dient een geharmoniseerde lijst te worden vastgesteld van verplichte vermeldingen die een factuur moet bevatten, alsmede een aantal gemeenschappelijke voorwaarden voor elektronische facturering, elektronische bewaring van facturen, eigen- handige facturering en uitbesteding van factureringswerk- zaamheden.

(47) De lidstaten moeten onder de voorwaarden die zij vaststellen, toestaan en verplicht kunnen stellen dat bepaalde aangiften langs elektronische weg worden ver- richt.

(48) Het noodzakelijke streven naar een verlichting van de administratieve en statistische formaliteiten van de onder- nemingen, met name de kleine en middelgrote onder- nemingen, moet worden verzoend met de toepassing van efficiënte controlemaatregelen en met de zowel om economische als om fiscale redenen onontbeerlijke hand- having van de kwaliteit van de communautaire statistische instrumenten.

(49) Ten aanzien van kleine ondernemingen moeten de lidstaten hun bijzondere regelingen kunnen behouden, zulks over- eenkomstig gemeenschappelijke voorschriften en met het oog op een verdergaande harmonisatie.

(59) De lidstaten moeten, met inachtneming van bepaalde beperkingen en voorwaarden, bijzondere van deze richtlijn afwijkende maatregelen kunnen treffen of handhaven, teneinde de belastingheffing te vereenvoudigen of bepaalde vormen van belastingfraude of belastingontwijking te voorkomen.

(60) Om te voorkomen dat een lidstaat in het ongewisse blijft over het gevolg dat de Commissie aan zijn verzoek om een afwijking wenst te geven, dient een termijn te worden vastgesteld waarbinnen de Commissie de Raad een voorstel tot machtiging moet voorleggen dan wel een mededeling waarin zij haar eventuele bezwaren toelicht.

(61) Het is van wezenlijk belang bij de toepassing van het BTW- stelsel uniformiteit te garanderen. Ter verwezenlijking van dat doel dienen uitvoeringsmaatregelen te worden vastge- steld.

(62) Deze maatregelen moeten met name een oplossing bieden voor het probleem van de dubbele belastingheffing op grensoverschrijdende handelingen die kan voortvloeien uit een niet eenvormige toepassing door de lidstaten van de regels inzake de plaats van belastbare handelingen.

(63) Hoewel het toepassingsgebied van de uitvoeringsmaat- regelen beperkt zou zijn, zouden de budgettaire gevolgen ervan voor een of meer lidstaten aanzienlijk kunnen zijn. De mogelijke gevolgen voor de begrotingen van de lidstaten rechtvaardigen dat de Raad zich het recht voorbehoudt de bevoegdheid tot uitvoering uit te oefenen.

## TITEL I - VOORWERP EN TOEPASSINGSGEBIED

## TITEL II - GEOGRAFISCH TOEPASSINGSGEBIED

## TITEL III - BELASTINGPLICHTIGEN

## TITEL IV - BELASTBARE HANDELINGEN

### Hoofdstuk 1 - Levering van goederen

### Hoofdstuk 2 - Intracommunautaire verwerving van goederen

### Hoofdstuk 3 - Diensten

### Hoofdstuk 4 - Invoer van goederen

## TITEL V - PLAATS VAN DE BELASTBARE HANDELINGEN

### Hoofdstuk 1 - Plaats van levering van goederen

#### Afdeling 1 - Levering van goederen zonder vervoer

#### Afdeling 2 - Levering van goederen met vervoer

#### Afdeling 3 - Levering van goederen aan boord van een schip, vliegtuig of trein

#### Afdeling 4 - Levering van goederen via distributiesystemen

### Hoofdstuk 2 - Plaats van een intracommunautaire verwerving van goederen

### Hoofdstuk 3 - Plaats van een dienst

#### Afdeling 1 - Algemene regel

#### Afdeling 2 - Bijzondere bepalingen

##### Onderafdeling 2 - Diensten met betrekking tot onroerende goederen

##### Onderafdeling 3 - Vervoerdiensten

##### Onderafdeling 4 - Culturele en soortgelijke diensten, diensten die samenhangen met vervoer of betrekking hebben op roerende lichamelijke zaken

##### Onderafdeling 5 - Diverse diensten

##### Onderafdeling 6 - Criterium inzake werkelijk gebruik en werkelijke exploitatie

### Hoofdstuk 4 - Plaats van invoer van goederen

## TITEL VI - BELASTBAAR FEIT EN VERSCHULDIGDHEID VAN DE BELASTING

### Hoofdstuk 1 - Algemene bepalingen

### Hoofdstuk 2 - Goederenleveringen en diensten

### Hoofdstuk 3 - Intracommunautaire verwerving van goederen

### Hoofdstuk 4 - Invoer van goederen

## TITEL VII - MAATSTAF VAN HEFFING

### Hoofdstuk 1 - Definitie

### Hoofdstuk 2 - Goederenleveringen en diensten

### Hoofdstuk 3 - Intracommunautaire verwerving van goederen

### Hoofdstuk 4 - Invoer van goederen

### Hoofdstuk 5 - Diverse bepalingen

## TITEL VIII - TARIEVEN

### Hoofdstuk 1 - Toepassing van de tarieven

### Hoofdstuk 2 - Structuur en hoogte van de tarieven

#### Afdeling 1 - Normaal tarief

#### Afdeling 2 - Verlaagde tarieven

#### Afdeling 3 - Bijzondere bepalingen

### Hoofdstuk 3 - Tijdelijke bepalingen voor bepaalde arbeidsintensieve diensten

### Hoofdstuk 4 - Bijzondere bepalingen van toepassing tot de invoering van de definitieve regeling

### Hoofdstuk 5 - Tijdelijke bepalingen

## TITEL IX - VRIJSTELLINGEN

### Hoofdstuk 1 - Algemene bepalingen

### Hoofdstuk 2 - Vrijstellingen voor bepaalde activiteiten van algemeen belang

### Hoofdstuk 3 - Vrijstellingen ten gunste van andere activiteiten

### Hoofdstuk 4 - Vrijstellingen met betrekking tot intracommunautaire handelingen

#### Afdeling 1 - Vrijstellingen voor levering van goederen

#### Afdeling 2 - Vrijstellingen voor intracommunautaire verwervingen van goederen

#### Afdeling 3 - Vrijstellingen voor bepaalde vervoerdiensten

### Hoofdstuk 5 - Vrijstellingen bij invoer

### Hoofdstuk 6 - Vrijstellingen bij uitvoer

### Hoofdstuk 7 - Vrijstellingen met betrekking tot internationaal vervoer

### Hoofdstuk 8 - Vrijstellingen voor bepaalde met uitvoer gelijkgestelde handelingen

### Hoofdstuk 9 - Vrijstellingen voor door tussenpersonen verrichte diensten

### Hoofdstuk 10 - Vrijstellingen voor handelingen met betrekking tot het internationale goederenverkeer

#### Afdeling 1 - Douane- en andere entrepots en soortgelijke regelingen

#### Afdeling 2 - Handelingen die worden vrijgesteld met het oog op de uitvoer en in het kader van het handelsverkeer tussen de lidstaten

## TITEL X - AFTREK

### Hoofdstuk 1 - Ontstaan en omvang van het recht op aftrek

### Hoofdstuk 2 - Evenredige aftrek

### Hoofdstuk 3 - Beperkingen van het recht op aftrek

### Hoofdstuk 4 - Wijze van uitoefening van het recht op aftrek

### Hoofdstuk 5 - Herziening van de aftrek

## TITEL XI - VERPLICHTINGEN VAN DE BELASTINGPLICHTIGEN EN VAN BEPAALDE NIET-BELASTING- PLICHTIGE PERSONEN

### Hoofdstuk 1 - Verplichting tot betaling

#### Afdeling 1 - Tegenover de schatkist tot voldoening van de belasting gehouden personen

#### Afdeling 2 - Wijze van betaling

### Hoofdstuk 2 - Identificatie

### Hoofdstuk 3 - Facturering

#### Afdeling 1 - Definitie

#### Afdeling 2 - Het begrip factuur

#### Afdeling 3 - Uitreiking van facturen

#### Afdeling 4 - Inhoud van de facturen

#### Afdeling 5 - Verzenden van facturen langs elektronische weg

#### Afdeling 6 - Vereenvoudigingsmaatregelen

### Hoofdstuk 4 - Boekhouding

#### Afdeling 1 - Definitie

#### Afdeling 2 - Algemene verplichtingen

#### Afdeling 3 - Specifieke verplichtingen ten aanzien van het bewaren van facturen

#### Afdeling 4 - Recht van toegang tot elektronisch bewaarde facturen in een andere lidstaat

### Hoofdstuk 5 - Aangiften

### Hoofdstuk 6 - Lijsten

### Hoofdstuk 7 - Diverse bepalingen

### Hoofdstuk 8 - Verplichtingen ter zake van bepaalde invoer- en uitvoerhandelingen

#### Afdeling 1 - Invoerhandelingen

#### Afdeling 2 - Uitvoerhandelingen

## TITEL XII - BIJZONDERE REGELINGEN

### Hoofdstuk 1 - Bijzondere regeling voor kleine ondernemingen

#### Afdeling 1 - Vereenvoudigde bepalingen inzake belastingheffing en belastinginning

#### Afdeling 2 - Vrijstellingen of degressieve verminderingen

#### Afdeling 3 - Verslag en herziening

### Hoofdstuk 2 - Gemeenschappelijke forfaitaire regeling voor landbouwproducenten

### Hoofdstuk 3 - Bijzondere regeling voor reisbureaus

### Hoofdstuk 4 - Bijzondere regelingen voor gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten

#### Afdeling 1 - Definities

#### Afdeling 2 - Bijzondere regeling voor belastingplichtige wederverkopers

##### Onderafdeling 1 - Winstmargeregeling

##### Onderafdeling 2 - Overgangsregeling voor gebruikte vervoermiddelen

#### Afdeling 3 - Bijzondere regeling voor verkoop op openbare veilingen

### Hoofdstuk 5 - Bijzondere regeling voor beleggingsgoud

#### Afdeling 1 - Algemene bepalingen

#### Afdeling 2 - Vrijstelling van de belasting

#### Afdeling 3 - Recht om voor belastingheffing te kiezen

#### Afdeling 4 - Handelingen op een gereglementeerde goudmarkt

#### Afdeling 5 - Bijzondere rechten en verplichtingen van handelaren in beleggingsgoud

### Hoofdstuk 6 - Bijzondere regeling voor niet in de Gemeenschap gevestigde belastingplichtigen die langs elektronische weg diensten verrichten voor niet-belastingplichtigen

#### Afdeling 1 - Algemene bepalingen

#### Afdeling 2 - Bijzondere regeling voor langs elektronische weg verrichte diensten

## TITEL XIII - AFWIJKINGEN

### Hoofdstuk 1 - Afwijkingen van toepassing tot de invoering van de definitieve regeling

#### Afdeling 1 - Afwijkingen voor de staten die op 1 januari 1978 lid waren van de Gemeenschap

#### Afdeling 2 - Afwijkingen voor de staten die na 1 januari 1978 tot de Gemeenschap zijn toegetreden

#### Afdeling 3 - Gemeenschappelijke bepalingen met betrekking tot de Afdelingen 1 et 2

### Hoofdstuk 2 - Afwijkingen waarvoor machtiging is verleend

#### Afdeling 1 - Vereenvoudigingsmaatregelen en maatregelen ter voorkoming van belastingfraude en -ontwijking . . 63

#### Afdeling 2 - Internationale overeenkomsten

## TITEL XIV - DIVERSE BEPALINGEN

### Hoofdstuk 1 - Uitvoeringsmaatregelen

### Hoofdstuk 2 - BTW-Comité

### Hoofdstuk 3 - Omrekeningskoers

### Hoofdstuk 4 - Andere belastingen, rechten en heffingen

## TITEL XV - SLOTBEPALINGEN

### Hoofdstuk 1 - Overgangsregeling voor de belastingheffing in het handelsverkeer tussen de lidstaten

### Hoofdstuk 2 - Overgangsmaatregelen in het kader van de toetreding tot de Europese Unie

### Hoofdstuk 3 - Omzetting en inwerkingtreding

BIJLAGE I - LIJST VAN WERKZAAMHEDEN BEDOELD IN ARTIKEL 14, LID 1, DERDE ALINEA

BIJLAGE II - INDICATIEVE LIJST VAN LANGS ELEKTRONISCHE WEG VERRICHTE DIENSTEN BEDOELD IN ARTIKEL 56, LID 1, PUNT K)

BIJLAGE III - LIJST VAN DE GOEDERENLEVERINGEN EN DE DIENSTEN WAAROP DE IN ARTIKEL 98 BEDOELDE VERLAGDE TARIEVEN MOGEN WORDEN TOEGEPAST

BIJLAGE IV - LIJST VAN DE IN ARTIKEL 106 BEDOELDE DIENSTEN

BIJLAGE V - CATEGORIEËN GOEDEREN DIE VOLGENS ARTIKEL 160, LID 2, ONDER EEN ANDER STELSEL VAN ENTREPOTS DAN DOUANE-ENTREPOTS KUNNEN VALLEN

BIJLAGE VI - LIJST VAN GOEDERENLEVERINGEN EN DIENSTEN ALS BEDOELD IN PUNT D) VAN ARTIKEL 199, LID 1

BIJLAGE VII - LIJST VAN LANDBOUWPRODUCTIEWERKZAAMHEDEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 4)

BIJLAGE VIII - INDICATIEVE LIJST VAN AGRARISCHE DIENSTEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 5) 74

BIJLAGE IX - KUNSTVOORWERPEN, VOORWERPEN VOOR VERZAMELINGEN EN ANTIQUITEITEN BEDOELD IN ARTIKEL 311, LID 1, PUNTEN 2), 3) EN 4)

## Deel A - Kunstvoorwerpen

## Deel B - Voorwerpen voor verzamelingen

BIJLAGE X - LIJST VAN HANDELINGEN WAARVOOR DE IN DE ARTIKELEN 370 EN 371 EN DE ARTIKELEN 375 TOT EN MET 390 BEDOELDE AFWIJKINGEN GELDEN

## Deel A - Handelingen die de lidstaten mogen blijven belasten

## Deel B - Handelingen die de lidstaten mogen blijven vrijstellen

## Bijlage XI

## Deel A - Ingetrokken richtlijnen met de achtereenvolgende wijzigingen ervan

## Deel B - Termijnen voor de omzetting in nationaal recht (bedoeld in artikel 411)

BIJLAGE XII - CONCORDANTIETABEL

VOORWERP EN TOEPASSINGSGEBIED

###### Artikel 1

1. Bij deze richtlijn wordt het gemeenschappelijke stelsel van belasting over de toegevoegde waarde (BTW) vastgesteld.

2. Het gemeenschappelijke BTW-stelsel berust op het beginsel dat op goederen en diensten een algemene verbruiksbelasting wordt geheven die strikt evenredig is aan de prijs van de goederen en diensten, zulks ongeacht het aantal handelingen dat tijdens het productie- en distributieproces vóór de fase van heffing plaatsvond.

Bij elke handeling is de BTW, berekend over de prijs van het goed of van de dienst volgens het tarief dat voor dat goed of voor die dienst geldt, verschuldigd onder aftrek van het bedrag van de BTW waarmede de onderscheiden elementen van de prijs rechtstreeks zijn belast.

Het gemeenschappelijke BTW-stelsel wordt toegepast tot en met de kleinhandelsfase.

###### Artikel 2

## 1. De volgende handelingen zijn aan de BTW onderworpen:

a) de leveringen van goederen, die binnen het grondgebied van een lidstaat door een als zodanig handelende belasting- plichtige onder bezwarende titel worden verricht;

b) de intracommunautaire verwervingen van goederen die binnen het grondgebied van een lidstaat onder bezwarende titel worden verricht:

i) door een als zodanig handelende belastingplichtige of door een niet-belastingplichtige rechtspersoon, wan- neer de verkoper een als zodanig handelende belas- tingplichtige is die noch onder de in de artikelen 282 tot en met 292 bedoelde vrijstellingsregeling voor kleine ondernemingen, noch onder artikel 33 of artikel 36 valt;

iii) voor luchtvaartuigen, wanneer de levering binnen drie maanden na de eerste ingebruikneming plaats- vindt of wanneer het luchtvaartuig niet meer dan 40 uur heeft gevlogen.

c) De lidstaten stellen de voorwaarden vast waaronder de in de tweede alinea bedoelde gegevens kunnen worden aangetoond.

3. Als „ accijnsproducten ” worden beschouwd energieproduc- ten, elektriciteit, alcohol en alcoholhoudende dranken en tabaksfabrikaten, zoals omschreven in de vigerende communau- taire bepalingen, maar niet gas dat via het aardgasdistributie- systeem wordt geleverd.

###### Artikel 3

1. In afwijking van artikel 2, lid 1, onder b), punt i), zijn de volgende handelingen niet aan BTW onderworpen:

a) de intracommunautaire verwervingen van goederen die worden verricht door een belastingplichtige of een niet- belastingplichtige rechtspersoon waarvan de levering krachtens de artikelen 148 en 151 binnen het grondgebied van de lidstaat van verwerving zou worden vrijgesteld;

b) de intracommunautaire verwervingen van andere goederen dan die bedoeld in punt a) en in artikel 4, en dan de verwervingen van vervoermiddelen en van accijnsproduc- ten, die worden verricht door een belastingplichtige ten behoeve van zijn landbouw-, bosbouw- of visserijbedrijf dat onder de gemeenschappelijke forfaitaire regeling voor landbouwproducenten valt, door een belastingplichtige die uitsluitend goederenleveringen of diensten verricht waar- voor geen recht op aftrek bestaat, of door een niet- belastingplichtige rechtspersoon.

2. Het bepaalde in lid 1, onder b), is alleen van toepassing indien de volgende voorwaarden vervuld zijn:

a) het totale bedrag van de intracommunautaire verwervingen van goederen is in het lopende kalenderjaar niet hoger dan een door de lidstaten te bepalen maximumwaarde die niet lager mag zijn dan EUR 10 000 of de tegenwaarde daarvan in de nationale munteenheid;

b) het totale bedrag van de intracommunautaire verwervingen van goederen heeft in het voorafgaande kalenderjaar de onder a) bepaalde maximumwaarde niet overschreden.

De maximumwaarde die als referentiepunt dient, is het totale bedrag van de intracommunautaire verwervingen van goederen als bedoeld in lid 1, onder b), de BTW die is verschuldigd of voldaan in de lidstaat van vertrek van de verzending of het vervoer van de goederen niet inbegrepen.

3. De lidstaten verlenen de belastingplichtigen en de niet- belastingplichtige rechtspersonen die voor de toepassing van lid 1, onder b), in aanmerking komen, het recht voor de in artikel 2, lid 1, onder b), punt i), omschreven algemene regeling te kiezen.

c) de Franse overzeese departementen;

d) de Ålandseilanden;

e) de Kanaaleilanden.

2. Deze richtlijn is niet van toepassing op de volgende gebieden die geen deel uitmaken van het douanegebied van de Gemeen- schap:

a) het eiland Helgoland;

b) het gebied Büsingen;

c) Ceuta;

d) Melilla;

e) Livigno;

f) Campione d'Italia;

g) de Italiaanse wateren van het meer van Lugano.

###### Artikel 7

1. Het Vorstendom Monaco, het eiland Man en de zones die te Akrotiri en Dhekelia onder de soevereiniteit van het Verenigd Koninkrijk vallen, worden, gezien de overeenkomsten en verdragen die zij met respectievelijk Frankrijk, het Verenigd Koninkrijk en Cyprus hebben gesloten, voor de toepassing van deze richtlijn niet als derde landen beschouwd.

2. De lidstaten nemen de nodige maatregelen om te waar- borgen dat handelingen met als herkomst of bestemming het Vorstendom Monaco als handelingen met herkomst of bestem- ming Frankrijk worden behandeld, dat handelingen met als herkomst of bestemming het eiland Man als handelingen met als herkomst of bestemming het Verenigd Koninkrijk worden behandeld en dat handelingen met als herkomst of bestemming de zones die te Akrotiri en Dhekelia onder de soevereiniteit van het Verenigd Koninkrijk vallen als handelingen met als herkomst of bestemming Cyprus worden behandeld.

###### Artikel 8

Indien de Commissie van mening is dat het bepaalde in de artikelen 6 en 7 niet meer gerechtvaardigd is, met name uit het oogpunt van de neutraliteit ten aanzien van de mededinging of van de eigen middelen, legt zij passende voorstellen aan de Raad voor.

BELASTINGPLICHTIGEN

###### Artikel 9

1. Als „ belastingplichtige ” wordt beschouwd eenieder die, op ongeacht welke plaats, zelfstandig een economische activiteit verricht, ongeacht het oogmerk of het resultaat van die activiteit.

3. Voor de toepassing van lid 1, onder b), wordt als „ bouw- terrein ” beschouwd, de door de lidstaten als zodanig omschreven al dan niet bouwrijp gemaakte terreinen.

###### Artikel 13

1. De staat, de regio's, de gewesten, de provincies, de gemeenten en de andere publiekrechtelijke lichamen worden niet als belastingplichtigen aangemerkt voor de werkzaamheden of handelingen die zij als overheid verrichten, ook niet indien zij voor die werkzaamheden of handelingen rechten, heffingen, bijdragen of retributies innen.

Wanneer deze lichamen evenwel zodanige werkzaamheden of handelingen verrichten, moeten zij daarvoor als belasting- plichtige worden aangemerkt, indien een behandeling als niet- belastingplichtige tot een verstoring van de mededinging van enige betekenis zou leiden.

De publiekrechtelijke lichamen worden in elk geval als belasting- plichtige beschouwd voor de in bijlage I genoemde werkzaam- heden, voorzover deze niet van onbeduidende omvang zijn.

2. De lidstaten kunnen werkzaamheden van publiekrechtelijke lichamen die uit hoofde van de artikelen 132, 135, 136, 371, 374 tot en met 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 390 zijn vrijgesteld, als werkzaam- heden van de overheid beschouwen.

BELASTBARE HANDELINGEN

## Levering van goederen

###### Artikel 14

1. Als „ levering van goederen ” wordt beschouwd, de overdracht of overgang van de macht om als een eigenaar over een lichamelijke zaak te beschikken.

2. Naast de in lid 1 bedoelde handeling worden de volgende handelingen als een levering van goederen beschouwd:

a) de eigendomsovergang van een goed tegen betaling van een vergoeding, ingevolge een vordering door of namens de overheid dan wel krachtens de wet;

b) de afgifte van een goed ingevolge een overeenkomst volgens welke een goed gedurende een bepaalde periode in huur wordt gegeven of ingevolge een overeenkomst tot koop en verkoop op afbetaling, in beide gevallen onder het beding dat normaal het goed uiterlijk bij de betaling van de laatste termijn in eigendom wordt verkregen;

c) de overdracht van een goed ingevolge een overeenkomst tot koop of verkoop in commissie.

d) de levering van gas via het aardgasdistributiesysteem of de levering van elektriciteit, onder de in de artikelen 38 en 39 gestelde voorwaarden;

e) de levering van dat goed door de belastingplichtige binnen het grondgebied van de lidstaat, onder de in de artike- len 138, 146, 147, 148, 151 en 152 gestelde voorwaarden;

f) de verrichting van een dienst voor de belastingplichtige in verband met werkzaamheden betreffende dat goed, die daadwerkelijk worden uitgevoerd binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer van het goed, voor zover het goed na bewerking opnieuw wordt verzonden naar deze belastingplichtige in de lidstaat waarvandaan het oorspronkelijk was verzonden of vervoerd;

g) het tijdelijke gebruik van dat goed binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer, ten behoeve van diensten verricht door de binnen de lidstaat van vertrek van de verzending of het vervoer van het goed gevestigde belastingplichtige;

h) het tijdelijke gebruik van dat goed voor een periode van ten hoogste 24 maanden binnen het grondgebied van een andere lidstaat waar de invoer van hetzelfde goed uit een derde land met het oog op tijdelijk gebruik in aanmerking zou komen voor de regeling voor tijdelijke invoer met volledige vrijstelling van invoerrechten.

3. Wanneer niet meer wordt voldaan aan een van de voorwaarden voor de toepassing van lid 2, wordt het goed als overgebracht naar een andere lidstaat beschouwd. In dat geval vindt de overbrenging plaats op het tijdstip waarop deze voorwaarde niet meer vervuld is.

###### Artikel 18

De lidstaten kunnen de volgende handelingen met een levering van goederen onder bezwarende titel gelijkstellen:

a) het door een belastingplichtige voor bedrijfsdoeleinden bestemmen van een goed dat in het kader van zijn bedrijf is vervaardigd, gebouwd, gewonnen, bewerkt, aangekocht of ingevoerd, indien het van een andere belastingplichtige betrekken van een dergelijk goed hem geen recht zou geven op volledige aftrek van de BTW;

b) het door een belastingplichtige voor een niet-belaste sector van zijn bedrijfsuitoefening bestemmen van een goed, voor zover bij de verwerving van dat goed of bij de bestemming ervan overeenkomstig punt a) recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan;

###### Artikel 23

De lidstaten nemen maatregelen om ervoor te zorgen dat als intracommunautaire verwerving van goederen worden beschouwd de handelingen die, indien zij op hun grondgebied door een als zodanig handelende belastingplichtige zouden zijn verricht, als levering van goederen zouden zijn aangemerkt.

## Diensten

###### Artikel 24

1. Als „ dienst ” wordt beschouwd elke handeling die geen levering van goederen is.

2. Als „ telecommunicatiediensten ” worden beschouwd de diensten waarmee de transmissie, uitzending of ontvangst van signalen, geschriften, beelden en geluiden of informatie van allerlei aard per draad, via radiofrequente straling, langs optische weg of met behulp van andere elektromagnetische middelen mogel ĳ k wordt gemaakt, met inbegrip van de daarmee samen- hangende overdracht en verlening van rechten op het gebruik van infrastructuur voor de transmissie, uitzending of ontvangst, waaronder het bieden van toegang tot wereldw ĳ de informatie- netten.

###### Artikel 25

## Een dienst kan onder meer een van de volgende handelingen zijn:

a) de overdracht van een onlichamelijke zaak, ongeacht of deze al dan niet in een titel is belichaamd;

b) de verplichting om een daad na te laten of om een daad of een situatie te dulden;

c) het verrichten van een dienst op grond van een vordering door of namens de overheid, dan wel krachtens de wet.

###### Artikel 26

## 1. Met diensten verricht onder bezwarende titel worden de volgende handelingen gelijkgesteld:

a) het gebruiken van een tot het bedrijf behorend goed voor privédoeleinden van de belastingplichtige of van zijn personeel, of, meer in het algemeen, voor andere dan bedrijfsdoeleinden, wanneer voor dit goed recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan;

b) het om niet verrichten van diensten door de belasting- plichtige voor eigen privédoeleinden of voor privédoel- einden van zijn personeel, of, meer in het algemeen, voor andere dan bedrijfsdoeleinden.

2. De lidstaten kunnen van lid 1 afwijken, mits deze afwijking niet tot verstoring van de mededinging leidt.

###### Artikel 27

van de belasting gehouden persoon, alsmede de plaats van daaropvolgende leveringen geacht in de lidstaat van invoer van de goederen te liggen.

###### Artikel 33

1. In afwijking van artikel 32 wordt als de plaats van levering van goederen die door of voor rekening van de leverancier worden verzonden of vervoerd vanuit een andere lidstaat dan die van aankomst van de verzending of het vervoer, aangemerkt de plaats waar de goederen zich bevinden op het tijdstip van aankomst van de verzending of het vervoer naar de afnemer, wanneer de volgende voorwaarden vervuld zijn:

a) de levering van goederen wordt verricht voor een belastingplichtige of voor een niet – belastingplichtige rechts- persoon van wie de intracommunautaire verwervingen van goederen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen, of voor enige andere niet-belasting- plichtige;

b) de geleverde goederen zijn geen nieuwe vervoermiddelen, noch goederen, geleverd na montage of installatie, door of voor rekening van de leverancier, met of zonder beproeven van de geïnstalleerde of gemonteerde goederen.

2. Wanneer de geleverde goederen uit een derdelandsgebied of een derde land worden verzonden of vervoerd en door de leverancier worden ingevoerd in een andere lidstaat dan de lidstaat van aankomst van de verzending of het vervoer naar de afnemer, worden zij geacht te zijn verzonden of vervoerd vanuit de lidstaat van invoer.

###### Artikel 34

1. Artikel 33 is niet van toepassing op de leveringen van goederen die alle worden verzonden of vervoerd naar eenzelfde lidstaat van aankomst van de verzending of het vervoer indien de volgende voorwaarden vervuld zijn:

a) de geleverde goederen zijn geen accijnsproducten;

b) het totale bedrag, de BTW niet inbegrepen, van de onder de voorwaarden van artikel 33 in die lidstaat verrichte leveringen in eenzelfde kalenderjaar is niet hoger dan EUR 100 000 of de tegenwaarde daarvan in de nationale munteenheid;

c) het totale bedrag, de BTW niet inbegrepen, van de onder de voorwaarden van artikel 33 in de lidstaat verrichte leveringen van andere goederen dan accijnsproducten in het voorafgaande kalenderjaar is niet hoger dan EUR 100 000 of de tegenwaarde daarvan in de nationale munteenheid.

2. De lidstaat binnen het grondgebied waarvan de goederen zich bevinden op het tijdstip van aankomst van de verzending of het vervoer naar de afnemer, mag het in lid 1 genoemde maximumbedrag beperken tot EUR 35 000 of de tegenwaarde daarvan in de nationale munteenheid, wanneer deze lidstaat vreest dat het maximum van EUR 100 000 tot ernstige verstoring van de mededinging zou leiden.

Als „ plaats van vertrek van een passagiersvervoer ” wordt beschouwd het eerste punt in de Gemeenschap waar passagiers aan boord kunnen komen, eventueel na een tussenstop buiten de Gemeenschap.

Als „ plaats van aankomst van een passagiersvervoer ” wordt beschouwd het laatste punt in de Gemeenschap waar passagiers die binnen de Gemeenschap aan boord zijn gekomen, van boord kunnen gaan, eventueel vóór een tussenstop buiten de Gemeen- schap.

Ingeval het een heen- en terugreis betreft, wordt de terugreis als een afzonderlijk vervoer beschouwd.

3. De Commissie legt de Raad zo spoedig mogelijk een verslag voor, dat in voorkomend geval vergezeld gaat van passende voorstellen, over de plaats van belastingheffing op leveringen van voor verbruik aan boord bestemde goederen en op diensten, met inbegrip van restauratie, die worden verleend aan passagiers aan boord van een schip, vliegtuig of trein.

Totdat de in de eerste alinea bedoelde voorstellen zijn aangenomen, kunnen de lidstaten leveringen van voor verbruik aan boord bestemde goederen waarvan de plaats van belasting- heffing overeenkomstig lid 1 wordt vastgesteld, vrijstellen of blijven vrijstellen, met recht op aftrek van voorbelasting.

## Lever ing van goederen via distr ibutiesystemen

###### Artikel 38

1. Ingeval de levering van gas via het aardgasdistributiesysteem of van elektriciteit wordt verricht aan een belastingplichtige wederverkoper wordt als plaats van deze levering aangemerkt, de plaats waar de belastingplichtige wederverkoper de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd waarvoor de goederen worden geleverd, dan wel, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of zijn gebruikelijke verblijfplaats.

2. Voor de toepassing van lid 1 wordt onder „ belastingplichtige wederverkoper ” verstaan, een belastingplichtige wiens hoofd- activiteit op het gebied van de aankoop van gas of elektriciteit bestaat in het wederverkopen van die producten en wiens eigen verbruik van die producten verwaarloosbaar is.

###### Artikel 39

In het geval van een levering van gas via het aardgasdistributie- systeem of van elektriciteit die niet wordt bestreken door artikel 38, wordt als plaats van deze levering aangemerkt, de plaats waar de afnemer het werkelijke gebruik en verbruik van de goederen heeft.

## Bijzondere bepalingen

Diensten van tussenpersonen

###### Artikel 44

Als plaats van een door een in naam en voor rekening van een ander handelende tussenpersoon verrichte dienst, anders dan de in artikel 50, artikel 54 en artikel 56, lid 1, bedoelde diensten, wordt aangemerkt de plaats waar de onderliggende handeling overeenkomstig deze richtlijn wordt verricht.

Wanneer echter de afnemer van de door de tussenpersoon verrichte dienst voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan die binnen het grondgebied waarvan die handeling wordt verricht, wordt de plaats van de door de tussenpersoon verrichte dienst geacht te zijn gelegen op het grondgebied van de lidstaat die aan de afnemer het BTW- identificatienummer heeft toegekend waaronder hem de dienst is verleend.

Diensten met betrekking tot onroerende goederen

###### Artikel 45

De plaats van diensten die betrekking hebben op een onroerend goed, met inbegrip van diensten van makelaars in onroerende goederen en van experts, alsmede van diensten die erop gericht zijn de uitvoering van bouwwerken voor te bereiden of te coördineren, zoals bijvoorbeeld de diensten verricht door architecten en bureaus die op de uitvoering van het werk toezicht houden, is de plaats waar het goed is gelegen.

Ver voerdiensten

###### Artikel 46

De plaats van andere vervoerdiensten dan het intracommunau- taire vervoer van goederen is de plaats waar het vervoer plaatsvindt, zulks naar verhouding van de afgelegde afstanden.

###### Artikel 47

De plaats van intracommunautaire goederenvervoerdiensten is de plaats van vertrek van het vervoer.

Wanneer echter intracommunautaire goederenvervoerdiensten worden verricht voor afnemers die voor BTW-doeleinden zijn geïdentificeerd in een andere lidstaat dan de lidstaat van vertrek van het vervoer, wordt de plaats van de diensten geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waar- onder hem de dienst is verleend.

###### Artikel 48

###### Artikel 53

In afwijking van artikel 52, punt b), wordt de plaats van diensten in verband met activiteiten die samenhangen met intracommu- nautair goederenvervoer, verricht voor afnemers die voor BTW- doeleinden zijn geïdentificeerd in een andere lidstaat dan die op het grondgebied waarvan de activiteiten daadwerkelijk worden verricht, geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.

###### Artikel 54

De plaats van diensten verricht door een in naam en voor rekening van een ander handelende tussenpersoon, wanneer hij bemiddelt bij het verrichten van een dienst in verband met activiteiten die samenhangen met intracommunautair goederen- vervoer, is de plaats waar de met het vervoer samenhangende activiteiten daadwerkelijk worden verricht.

Wanneer echter de afnemer van de door de tussenpersoon verrichte dienst voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan die binnen het grondgebied waarvan de met het vervoer samenhangende activiteiten daadwerkelijk worden verricht, wordt de plaats van de door de tussenpersoon verrichte dienst geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.

###### Artikel 55

In afwijking van artikel 52, onder c), wordt bij expertises of werkzaamheden met betrekking tot roerende lichamelijke zaken die worden verricht voor afnemers die voor BTW-doeleinden zijn geïdentificeerd in een andere lidstaat dan die op het grondgebied waarvan de dienst daadwerkelijk wordt verricht, de plaats van de diensten geacht te zijn gelegen op het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toege- kend waaronder de dienst voor hem is verricht.

De in de eerste alinea bedoelde afwijking is slechts van toepassing indien de goederen worden verzonden of vervoerd buiten de lidstaat waar de dienst daadwerkelijk is verricht.

Diverse diensten

###### Artikel 56

1. De plaats van de volgende diensten die worden verricht voor afnemers die buiten de Gemeenschap zijn gevestigd of voor belastingplichtigen die weliswaar in de Gemeenschap doch buiten het land van de dienstverrichter zijn gevestigd, is de plaats waar de afnemer de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd waarvoor de dienst is verricht, of bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of zijn gebruikelijke verblijfplaats:

a) de overdracht en het verlenen van auteursrechten, octrooien, licentierechten, fabrieks- en handelsmerken, en andere soortgelijke rechten;

Cr iter ium inzake werkelijk gebr uik en werkelijke exploitatie

###### Artikel 58

Teneinde dubbele heffing of niet-heffing van de belasting alsmede verstoring van de mededinging te voorkomen, kunnen de lidstaten voor de in artikel 56, lid 1, bedoelde diensten alsmede voor de verhuur van vervoermiddelen:

a) de plaats van deze diensten of van sommige ervan, die op hun grondgebied is gelegen, aanmerken als buiten de Gemeenschap te zijn gelegen, wanneer het werkelijke gebruik en de werkelijke exploitatie buiten de Gemeenschap geschieden;

b) de plaats van deze diensten of van sommige ervan, die buiten de Gemeenschap is gelegen, aanmerken als op hun grondgebied te zijn gelegen, wanneer het werkelijke gebruik en de werkelijke exploitatie op hun grondgebied geschie- den.

Deze bepaling geldt echter niet voor de in artikel 56, lid 1, punt k), bedoelde diensten, wanneer deze voor niet-belasting- plichtigen worden verricht.

###### Artikel 59

1. De lidstaten passen artikel 58, onder b), toe op telecommu- nicatiediensten die worden verricht voor niet-belastingplichtigen die in een lidstaat gevestigd zijn of er hun woonplaats of gebruikelijke verblijfplaats hebben, door een belastingplichtige die de zetel van zijn bedrijfsuitoefening buiten de Gemeenschap heeft gevestigd of daar over een vaste inrichting beschikt van waaruit de diensten worden verricht, of die, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of gebruike- lijke verblijfplaats buiten de Gemeenschap heeft.

2. Tot en met 31 december 2006 passen de lidstaten artikel 58, punt b), toe op de in artikel 56, lid 1, punt j), bedoelde radio- en televisieomroepdiensten welke worden verricht voor niet-belas- tingplichtigen die in een lidstaat gevestigd zijn of er hun woonplaats of gebruikelijke verblijfplaats hebben, door een belastingplichtige die de zetel van zijn bedrijfsuitoefening buiten de Gemeenschap heeft gevestigd of daar over een vaste inrichting beschikt van waaruit de diensten worden verricht, of die, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of gebruikelijke verblijfplaats buiten de Gemeen- schap heeft.

## Plaats van invoer van goederen

###### Artikel 60

De invoer van goederen vindt plaats in de lidstaat binnen het grondgebied waarvan het goed zich ten tijde van het binnen- komen in de Gemeenschap bevindt.

###### Artikel 61

###### Artikel 66

In afwijking van de artikelen 63, 64 en 65 kunnen de lidstaten bepalen dat de belasting voor bepaalde handelingen of bepaalde categorieën belastingplichtigen op één van de volgende tijd- stippen verschuldigd wordt:

a) uiterlijk bij de uitreiking van de factuur;

b) uiterlijk bij ontvangst van de prijs;

c) wanneer de factuur niet of niet tijdig wordt uitgereikt, binnen een bepaalde termijn te rekenen vanaf de datum van het belastbare feit.

###### Artikel 67

1. Wanneer, onder de in artikel 138 vastgestelde voorwaarden, naar een andere lidstaat dan de lidstaat van vertrek van de verzending of het vervoer verzonden of vervoerde goederen, met vrijstelling van BTW worden geleverd of goederen met vrijstel- ling van BTW door een belastingplichtige voor bedrijfsdoel- einden naar een andere lidstaat worden overgebracht, wordt de belasting verschuldigd op de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

2. In afwijking van lid 1 wordt de belasting verschuldigd bij de uitreiking van de in artikel 220 bedoelde factuur wanneer deze factuur is uitgereikt vóór de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

## Intracommunautaire verwerving van goederen

###### Artikel 68

Het belastbare feit vindt plaats op het tijdstip waarop de intracommunautaire verwerving van goederen wordt verricht.

De intracommunautaire verwerving van goederen wordt geacht te zijn verricht op het tijdstip waarop de levering van soortgelijke goederen binnen het grondgebied van de lidstaat wordt geacht te zijn verricht.

###### Artikel 69

1. Voor de intracommunautaire verwervingen van goederen wordt de belasting verschuldigd op de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

2. In afwijking van lid 1 wordt de belasting verschuldigd bij de uitreiking van de in artikel 220 bedoelde factuur wanneer deze factuur is uitgereikt vóór de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

## Invoer van goederen

###### Artikel 70

afnemer of van een derde, met inbegrip van subsidies die rechtstreeks met de prijs van deze handelingen verband houden.

###### Artikel 74

Voor het door een belastingplichtige onttrekken van goederen aan zijn bedrijf of bestemmen van goederen voor zijn bedrijf en het onder zich hebben van goederen door een belastingplichtige of zijn rechthebbenden wanneer hij zijn belastbare economische activiteit beëindigt, als bedoeld in de artikelen 16 en 18, is de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.

###### Artikel 75

Voor de in artikel 26 bedoelde diensten, waarbij een tot het bedrijf behorend goed voor privédoeleinden wordt gebruikt of diensten om niet worden verricht, is de maatstaf van heffing het bedrag van de door de belastingplichtige voor het verrichten van de diensten gemaakte kosten.

###### Artikel 76

Voor goederenleveringen bestaande in de overbrenging naar een andere lidstaat is de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.

###### Artikel 77

Voor de door een belastingplichtige voor bedrijfsdoeleinden verrichte diensten, bedoeld in artikel 27, is de maatstaf van heffing de normale waarde van de verrichte diensten.

###### Artikel 78

## In de maatstaf van heffing moeten de volgende elementen worden opgenomen:

a) belastingen, rechten en heffingen, met uitzondering van de BTW zelf;

b) bijkomende kosten, zoals kosten van commissie, verpak- king, vervoer en verzekering, die de leverancier de afnemer in rekening brengt.

Voor de toepassing van punt b) van de eerste alinea mogen de lidstaten uitgaven die bij afzonderlijke overeenkomst zijn geregeld, als bijkomende kosten beschouwen.

###### Artikel 79

## In de maatstaf van heffing worden de volgende elementen niet opgenomen:

a) prijsverminderingen wegens korting voor vooruitbetaling;

Het in de eerste alinea bedoelde gedeelte wordt op zodanige wijze vastgesteld dat de aldus verschuldigde BTW ten minste gelijk is aan 5 % van het overeenkomstig de artikelen 73, 74, 76, 78 en 79 vastgestelde bedrag.

###### Artikel 82

De lidstaten kunnen bepalen dat in de maatstaf van heffing voor goederenleveringen en diensten de waarde moet worden opgenomen van vrijgesteld beleggingsgoud in de zin van artikel 346, dat door de afnemer ter beschikking is gesteld om voor verwerking te worden gebruikt en dat als gevolg van die verwerking zijn status van vrijgesteld beleggingsgoud verliest wanneer die goederenlevering of die dienst wordt verricht. De te hanteren waarde is de normale waarde van het beleggingsgoud op het tijdstip waarop die goederenlevering of die dienst wordt verricht.

## Intracommunautaire verwerving van goederen

###### Artikel 83

Voor de intracommunautaire verwerving van goederen bestaat de maatstaf van heffing uit dezelfde elementen als die welke in aanmerking worden genomen om overeenkomstig hoofdstuk 1 de maatstaf van heffing voor de levering van dezelfde goederen binnen het grondgebied van de lidstaat in kwestie te bepalen. Met name is voor de in de artikelen 21 en 22 bedoelde handelingen die met een intracommunautaire verwerving van goederen worden gelijkgesteld, de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.

###### Artikel 84

1. De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de accijns die verschuldigd of voldaan is door degene die de intracommunautaire verwerving van een accijnsproduct verricht, overeenkomstig artikel 78, eerste alinea, punt a), in de maatstaf van heffing wordt opgenomen.

2. Wanneer de afnemer na het tijdstip waarop de intracom- munautaire verwerving van goederen plaatsvindt, teruggaaf verkrijgt van de in de lidstaat van vertrek van de verzending of het vervoer van de goederen voldane accijns, wordt de maatstaf van heffing dienovereenkomstig verlaagd in de lidstaat binnen het grondgebied waarvan de verwerving heeft plaatsgevonden.

## Invoer van goederen

###### Artikel 85

## Diverse bepalingen

###### Artikel 90

1. In geval van annulering, verbreking, ontbinding of gehele of gedeeltelijk niet-betaling, of in geval van prijsvermindering nadat de handeling is verricht, wordt de maatstaf van heffing dienovereenkomstig verlaagd onder de voorwaarden die door de lidstaten worden vastgesteld.

2. In geval van gehele of gedeeltelijke niet-betaling kunnen de lidstaten van lid 1 afwijken.

###### Artikel 91

1. Indien de elementen voor de bepaling van de maatstaf van heffing bij invoer zijn uitgedrukt in een andere munteenheid dan die van de lidstaat waar de maatstaf van heffing wordt bepaald, wordt de wisselkoers vastgesteld overeenkomstig de geldende communautaire bepalingen voor de berekening van de douane- waarde.

2. Indien de elementen voor de bepaling van de maatstaf van heffing voor een andere handeling dan een invoer van goederen zijn uitgedrukt in een andere munteenheid dan die van de lidstaat waar de maatstaf van heffing wordt bepaald, is de toepasselijke wisselkoers de laatste verkoopkoers die op het tijdstip waarop de belasting verschuldigd wordt, op de meest representatieve wisselmarkt of wisselmarkten van de betrokken lidstaat wordt geregistreerd, of een koers die wordt vastgesteld onder verwijzing naar die markt of markten, op een door die lidstaat vastgestelde wijze.

Voor sommige van de in de eerste alinea bedoelde handelingen of voor sommige categorieën belastingplichtigen kunnen de lid- staten evenwel kiezen voor de volgens de geldende communau- taire bepalingen voor de berekening van de douanewaarde vastgestelde wisselkoers.

###### Artikel 92

## Wat het statiegeld voor retouremballage betreft, kunnen de lidstaten het volgende bepalen:

a) hetzij het statiegeld van de maatstaf van heffing uitsluiten door de nodige maatregelen te nemen opdat de maatstaf wordt herzien wanneer de emballage niet wordt teruggeven;

b) hetzij het statiegeld in de maatstaf van heffing opnemen door de nodige maatregelen te nemen opdat de maatstaf wordt herzien wanneer de emballage wel wordt teruggeven.

TARIEVEN

## Toepassing van de tarieven

###### Artikel 93

2. De verlaagde tarieven zijn uitsluitend van toepassing op de goederenleveringen en de diensten die tot de in b ĳ lage III genoemde categorieën behoren.

De verlaagde tarieven zijn niet van toepassing op de in artikel 56, lid 1, punt k), bedoelde diensten.

3. Bij de toepassing van de in lid 1 bedoelde verlaagde tarieven op de categorieën waarin aan goederen wordt gerefereerd, mogen de lidstaten voor de vaststelling van de juiste omschrijving van de betrokken categorie gebruikmaken van de gecombineerde nomenclatuur.

###### Artikel 99

1. De verlaagde tarieven worden vastgesteld op een percentage van de maatstaf van heffing dat niet lager mag z ĳ n dan 5 %.

2. Een verlaagd tarief wordt zodanig vastgesteld, dat het bij toepassing van dit tarief verkregen BTW-bedrag het normaliter mogelijk maakt de overeenkomstig de artikelen 167 tot en met 171 en de artikelen 173 tot en met 177 aftrekbare belasting volledig af te trekken.

###### Artikel 100

Aan de hand van een verslag van de Commissie onderwerpt de Raad, voor de eerste maal in 1994 en vervolgens om de twee jaar, de werkingssfeer van de verlaagde tarieven aan een onderzoek.

De Raad kan overeenkomstig artikel 93 van het Verdrag besluiten wijzigingen aan te brengen in de in bijlage III opgenomen lijst van goederen en diensten.

###### Artikel 101

De Commissie legt uiterlijk op 30 juni 2007 aan het Europees Parlement en aan de Raad een algemeen evaluatieverslag voor over het effect van de verlaagde tarieven op lokale diensten, inclusief restauratie, waarin met name aandacht wordt geschon- ken aan het scheppen van werkgelegenheid, de economische groei en de goede werking van de interne markt, en dat gebaseerd is op een studie van een onafhankelijke economische- reflectiegroep.

## Bijzondere bepalingen

###### Artikel 102

De lidstaten kunnen voor de levering van aardgas, elektriciteit en stadsverwarming een verlaagd tarief toepassen, mits er geen gevaar voor verstoring van de mededinging bestaat.

c) hoofdzakel ĳ k lokaal z ĳ n en niet tot verstoring van de mededinging leiden.

Voorts moet er een nauw verband bestaan tussen de pr ĳ sverla- ging als gevolg van de tariefverlaging en de te verwachten toename van de vraag en de werkgelegenheid. De toepassing van een verlaagd tarief mag de goede werking van de interne markt niet in gevaar brengen.

###### Artikel 108

Iedere lidstaat die voor het eerst na 31 december 2005 uit hoofde van dit artikel een verlaagd tarief wenst toe te passen op een of meer van de in artikel 106 bedoelde diensten, stelt de Commissie uiterlijk op 31 maart 2006 daarvan in kennis. De lidstaat deelt de Commissie vóór die datum alle toepasselijke inlichtingen betreffende de beoogde nieuwe maatregelen mede, met name:

a) het toepassingsgebied van de maatregel en de nauwkeurige beschr ĳ ving van de betrokken diensten;

b) de gegevens waaruit bl ĳ kt dat de in artikel 107 genoemde voorwaarden vervuld zijn;

c) de gegevens waaruit de budgettaire kosten van de voorgenomen maatregel bl ĳ ken.

## Bijzondere bepalingen van toepassing tot de invoering van de definitieve regeling

###### Artikel 109

Dit hoofdstuk is van toepassing tot de invoering van de in artikel 402 bedoelde definitieve regeling.

###### Artikel 110

De lidstaten die op 1 januari 1991 vrijstellingen met recht op aftrek van voorbelasting verleenden of verlaagde tarieven toepasten die onder het in artikel 96 vastgestelde minimum liggen, mogen deze blijven toepassen.

De in de eerste alinea bedoelde vrijstellingen en verlaagde tarieven moeten in overeenstemming zijn met het Gemeen- schapsrecht en moeten om duidelijk omschreven redenen van maatschappelijk belang en ten behoeve van de eindverbruikers vastgesteld zijn.

###### Artikel 111

Onder de in artikel 110, tweede alinea, gestelde voorwaarden mogen vrijstellingen met recht op aftrek van voorbelasting in de volgende gevallen toegepast blijven worden:

a) door Finland op abonnementen van dagbladen en tijd- schriften en op het vervaardigen van drukwerk voor de leden van verenigingen voor algemeen welzijn;

###### Artikel 118

De lidstaten die op 1 januari 1991 een verlaagd tarief toepasten voor andere leveringen van goederen en voor andere diensten dan de in bijlage III genoemde, mogen voor die leveringen of voor die diensten het verlaagde tarief of een van de twee verlaagde tarieven overeenkomstig artikel 98 toepassen, op voorwaarde dat dit tarief niet lager ligt dan 12 %.

De eerste alinea is niet van toepassing op leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor ver- zamelingen en antiquiteiten zoals omschreven in artikel 311, lid 1, punten 1) tot en met 4), die overeenkomstig de in de artikelen 312 tot en met 325 vastgestelde winstmargeregeling of de regeling voor verkoop op openbare veilingen aan de BTW zijn onderworpen.

###### Artikel 119

Voor de toepassing van artikel 118 mag Oostenrijk een verlaagd tarief toepassen op door de producerende boer op de boerderij geproduceerde wijn, op voorwaarde dat dit tarief niet lager ligt dan 12 %.

###### Artikel 120

Griekenland mag tarieven die tot 30 % lager liggen dan de overeenkomstige tarieven op het Griekse vasteland, toepassen in de departementen Lesbos, Chios, Samos, de Dodekanesos en de Cycladen, en op de eilanden Thassos, de noordelijke Sporaden, Samothraki en Skiros.

###### Artikel 121

De lidstaten die op 1 januari 1993 de oplevering van een werk in roerende staat als een levering van goederen aanmerkten, kunnen op de oplevering van een werk in roerende staat het tarief toepassen dat van toepassing is op het na de uitvoering van het aangenomen werk verkregen goed.

Voor de toepassing van de eerste alinea wordt onder „ oplevering van een werk in roerende staat ” verstaan de afgifte door de opdrachtnemer aan de opdrachtgever van een roerend goed dat hij heeft vervaardigd of samengesteld met behulp van stoffen en voorwerpen die daartoe door de opdrachtgever aan de opdracht- nemer zijn verstrekt, ongeacht of de opdrachtnemer al dan niet een deel van de gebruikte materialen heeft verschaft.

###### Artikel 122

De lidstaten mogen een verlaagd tarief toepassen op leveringen van levende planten en andere producten van de bloementeelt, met inbegrip van bollen, wortelen en dergelijke, snijbloemen en snijgroen, alsmede op leveringen van brandhout.

## Tijdelijke bepalingen

###### Artikel 123

Tsjechië mag tot en met 31 december 2007 een verlaagd tarief van ten minste 5 % blijven toepassen op de volgende handelin- gen:

3. Polen mag tot en met 30 april 2008 een verlaagd tarief van ten minste 3 % blijven toepassen op de levering van levens- middelen bedoeld in bijlage III, punt 1.

4. Polen mag tot en met 30 april 2008 een verlaagd tarief van ten minste 3 % blijven toepassen op de in bijlage III, punt 11, bedoelde goederenleveringen en diensten die normaal bestemd zijn voor gebruik in de landbouw, met uitzondering evenwel van kapitaalgoederen, zoals machines of gebouwen.

5. Polen mag tot en met 31 december 2007 een verlaagd tarief van ten minste 7 % toepassen op diensten die niet in het kader van sociaal beleid worden verricht voor de bouw, de verbouwing of de aanpassing van woningen, met uitzondering van bouw- materialen, en op de levering van woongebouwen of delen van woongebouwen vóór de eerste ingebruikneming, zoals bedoeld in artikel 12, lid 1, punt a).

###### Artikel 129

1. Slovenië mag tot en met 31 december 2007 of tot de invoering van de in artikel 402 bedoelde definitieve regeling, naargelang welke datum eerder valt, een verlaagd tarief van ten minste 8,5 % blijven toepassen op restauratie.

2. Slovenië mag tot en met 31 december 2007 een verlaagd tarief van ten minste 5 % blijven toepassen op woningbouw- werkzaamheden en renovatie- en onderhoudswerkzaamheden aan woningen, voorzover die werkzaamheden niet in het kader van sociaal beleid worden verricht, met uitzondering van bouwmaterialen.

###### Artikel 130

Slowakije mag een verlaagd tarief van ten minste 5 % blijven toepassen op de volgende handelingen:

a) tot en met 31 december 2007 op woningbouwwerkzaam- heden die niet in het kader van sociaal beleid worden verricht, met uitzondering van bouwmaterialen;

b) tot en met 31 december 2008 op de levering van warmte- energie aan huishoudens en niet-belastingplichtige kleine ondernemers voor verwarming en warmwaterproductie, met uitzondering van grondstoffen voor het opwekken van warmte-energie.

VRIJSTELLINGEN

## Algemene bepalingen

###### Artikel 131

k) beschikbaarstelling van personeel door religieuze of levens- beschouwelijke instellingen voor de in de punten b), g), h) en i), bedoelde werkzaamheden en met het oog op de verlening van geestelijke bijstand;

l) diensten en nauw daarmee samenhangende goederenleve- ringen ten behoeve van hun leden in het collectief belang, tegen een statutair vastgestelde contributie door instellingen zonder winstoogmerk met doeleinden van politieke, syndicale, religieuze, vaderlandslievende, levensbeschouwe- lijke, filantropische of staatsburgerlijke aard, mits deze vrijstelling niet tot verstoring van de mededinging kan leiden;

m) sommige diensten welke nauw samenhangen met de beoefening van sport of met lichamelijke opvoeding en welke door instellingen zonder winstoogmerk worden verricht voor personen die aan sport of lichamelijke opvoeding doen;

n) bepaalde culturele diensten alsmede nauw daarmee samen- hangende goederenleveringen, verricht door publiekrechte- lijke culturele instellingen of door andere culturele instellingen die door de betrokken lidstaat worden erkend;

o) diensten en goederenleveringen door lichamen waarvan de handelingen overeenkomstig de punten b), g), h), i), l), m) en n), zijn vrijgesteld, in samenhang met activiteiten die zijn bestemd ter verkrijging van financiële steun en die uitsluitend ten bate van henzelf zijn georganiseerd, mits deze vrijstelling niet tot verstoring van de mededinging kan leiden;

p) vervoer van zieken of gewonden met speciaal daartoe ingerichte voertuigen door naar behoren gemachtigde lichamen;

q) niet-commerciële activiteiten van openbare radio- en televisieorganisaties.

2. Voor de toepassing van lid 1, punt o), kunnen de lidstaten alle nodige beperkingen invoeren, met name ten aanzien van het aantal evenementen of het bedrag van de opbrengsten waarvoor recht op vrijstelling bestaat.

###### Artikel 133

De lidstaten kunnen de verlening van elk der in artikel 132, lid 1, punten b), g), h), i), l), m) en n), bedoelde vrijstellingen aan andere dan publiekrechtelijke instellingen van geval tot geval afhankelijk stellen van een of meer van de volgende voorwaarden:

a) de instellingen mogen niet systematisch het maken van winst beogen; eventuele winsten mogen niet worden uitgekeerd, maar moeten worden aangewend voor de instandhouding of verbetering van de diensten die worden verricht;

verzamelobject zijn, namelijk gouden, zilveren of uit een ander metaal geslagen munten, alsmede biljetten, die normaal niet als wettig betaalmiddel worden gebruikt of die een numismatische waarde hebben;

f) handelingen, bemiddeling daaronder begrepen, uitgezon- derd bewaring en beheer, inzake aandelen, deelnemingen in vennootschappen of verenigingen, obligaties en andere waardepapieren, met uitzondering van documenten die goederen vertegenwoordigen en van de in artikel 16, lid 2, bedoelde rechten of effecten;

g) het beheer van gemeenschappelijke beleggingsfondsen, zoals omschreven door de lidstaten;

h) leveringen, tegen de nominale waarde, van postzegels die frankeerwaarde hebben binnen hun respectieve grond- gebied, fiscale zegels en andere soortgelijke zegels;

i) weddenschappen, loterijen en andere kans- en geldspelen, met inachtneming van de door elke lidstaat gestelde voorwaarden en beperkingen;

j) de levering van een gebouw of een gedeelte ervan en van het bijbehorende terrein, met uitzondering van de in artikel 13, lid 1, punt a), bedoelde levering;

k) de levering van onbebouwde onroerende goederen, met uitzondering van de in artikel 12, lid 1, punt b), bedoelde levering van een bouwterrein;

l) de verhuur en verpachting van onroerende goederen.

## 2. De volgende handelingen zijn van de in lid 1, punt l), geregelde vrijstelling uitgesloten:

a) het verstrekken van accommodatie, als omschreven in de wetgeving der lidstaten, in het hotelbedrijf of in sectoren met een soortgelijke functie, met inbegrip van de verhuur- accommodatie in vakantiekampen of op kampeerterreinen;

b) verhuur van parkeerruimte voor voertuigen;

c) verhuur van blijvend geïnstalleerde werktuigen en machi- nes;

d) verhuur van safeloketten.

De lidstaten kunnen nog andere handelingen van de toepassing van de in lid 1, punt l), geregelde vrijstelling uitsluiten.

###### Artikel 136

## De lidstaten verlenen vrijstelling voor de volgende handelingen:

a) leveringen van goederen die uitsluitend zijn gebruikt voor een activiteit die krachtens de artikelen 132, 135, 371, 375, 376 en 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 390 is vrijgesteld, wanneer voor deze goederen geen recht op aftrek is genoten;

belastingplichtige rechtspersonen wier intracommunautaire verwervingen van andere goederen dan accijnsproducten, uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen wanneer de verzending of het vervoer van deze producten plaatsvindt overeenkomstig artikel 7, leden 4 en 5, of artikel 16 van Richtlijn 92/12/EEG;

c) de goederenlevering bestaande in de overbrenging naar een andere lidstaat, die voor de in lid 1 en de punten a) en b) bedoelde vrijstellingen in aanmerking zou komen indien zij voor een andere belastingplichtige was verricht.

###### Artikel 139

1. De in artikel 138, lid 1, bedoelde vrijstelling is niet van toepassing op de goederenlevering welke wordt verricht door belastingplichtigen die voor de in de artikelen 282 tot en met 292 geregelde vrijstelling voor kleine ondernemingen in aanmerking komen.

De vrijstelling is evenmin van toepassing op de goederenlevering welke wordt verricht voor belastingplichtigen of voor niet- belastingplichtige rechtspersonen wier intracommunautaire ver- wervingen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen.

2. De in artikel 138, lid 2, onder b), geregelde vrijstelling is niet van toepassing op de levering van accijnsproducten welke wordt verricht door belastingplichtigen die voor de in de artikelen 282 tot en met 292 geregelde vrijstelling voor kleine ondernemingen in aanmerking komen.

3. De in artikel 138, lid 1, en lid 2, onder b) en c), geregelde vrijstelling is niet van toepassing op de goederenlevering welke overeenkomstig de in de artikelen 312 tot en met 325 neergelegde winstmargeregeling of de regeling inzake de verkoop op openbare veilingen aan de BTW is onderworpen.

De in artikel 138, lid 1, en lid 2, onder c), geregelde vrijstelling is niet van toepassing op de levering van gebruikte vervoer- middelen als omschreven in artikel 327, lid 3, die overeenkom- stig de overgangsregeling voor gebruikte vervoermiddelen aan de BTW zijn onderworpen.

## Vr ijstellingen voor intracommunautaire ver wer vingen van goederen

###### Artikel 140

## De lidstaten verlenen vrijstelling voor de volgende handelingen:

## Vrijstellingen bij invoer

###### Artikel 143

## De lidstaten verlenen vrijstelling voor de volgende handelingen:

a) de definitieve invoer van goederen waarvan de levering door belastingplichtigen in ieder geval op hun respectieve grondgebied is vrijgesteld;

b) de definitieve invoer van goederen die valt onder de Richtlijnen 69/169/EEG ( 1 ), 83/181/EEG ( 2 ) en 2006/79/ EG ( 3 ) van de Raad;

c) de definitieve invoer van goederen in het vrije verkeer afkomstig uit een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap, die voor de in punt b) bedoelde vrijstelling in aanmerking zouden komen indien zij waren ingevoerd in de zin van artikel 31, eerste alinea;

d) de invoer van vanuit een derdelandsgebied of een derde land verzonden of vervoerde goederen in een andere lidstaat dan de lidstaat van aankomst van de verzending of het vervoer, indien de levering van deze goederen, verricht door de importeur die uit hoofde van artikel 201 is aangewezen of erkend als de tot voldoening van de belasting gehouden persoon, overeenkomstig artikel 138 is vrijgesteld;

e) de wederinvoer van goederen in de toestand waarin zij zijn uitgevoerd, door degene die deze heeft uitgevoerd, indien de goederen voor vrijstelling van invoerrechten in aanmerking komen;

f) de invoer van goederen in het kader van de diplomatieke en consulaire betrekkingen, indien de goederen voor vrijstel- ling van invoerrechten in aanmerking komen;

g) de invoer van goederen verricht door internationale instellingen die als zodanig door de overheid van de lidstaat waar zij zijn gevestigd, zijn erkend, alsmede door de leden van deze instellingen, zulks binnen de beperkingen en onder de voorwaarden die zijn vastgesteld bij de inter- nationale verdragen tot oprichting van deze instellingen of bij de vestigingsovereenkomsten;

## Vrijstellingen bij uitvoer

###### Artikel 146

## 1. De lidstaten verlenen vrijstelling voor de volgende handelin- gen:

a) de levering van goederen die door of voor rekening van de verkoper worden verzonden of vervoerd naar een plaats buiten de Gemeenschap;

b) de levering van goederen die door of voor rekening van een niet op hun respectieve grondgebied gevestigde afnemer worden verzonden of vervoerd naar een plaats buiten de Gemeenschap, met uitzondering van door de afnemer zelf vervoerde goederen bestemd voor de uitrusting of de bevoorrading van pleziervaartuigen en sportvliegtuigen of van andere vervoermiddelen voor privé-gebruik;

c) de levering van goederen aan erkende organisaties die deze goederen uit de Gemeenschap uitvoeren in het kader van hun menslievende, liefdadige of opvoedkundige werk buiten de Gemeenschap;

d) diensten bestaande uit werkzaamheden met betrekking tot roerende zaken die zijn verworven of ingevoerd teneinde deze werkzaamheden in de Gemeenschap te ondergaan, en die door of voor rekening van de dienstverrichter of de niet binnen hun respectieve grondgebied gevestigde afnemer worden vervoerd of verzonden naar een plaats buiten de Gemeenschap;

e) diensten, met inbegrip van vervoer en met die diensten samenhangende handelingen en met uitzondering van de overeenkomstig de artikelen 132 en 135 vrijgestelde diensten, wanneer die diensten rechtstreeks verband houden met de uitvoer of invoer van goederen die onder artikel 61 en artikel 157, lid 1, onder a), vallen.

2. De in lid 1, punt c), geregelde vrijstelling kan worden toegekend in de vorm van teruggaaf van de BTW.

###### Artikel 147

1. Indien de in artikel 146, lid 1, punt b), bedoelde levering betrekking heeft op goederen die deel uitmaken van de persoonlijke bagage van reizigers, geldt de vrijstelling slechts wanneer de volgende voorwaarden vervuld zijn:

a) de reiziger is niet in de Gemeenschap gevestigd;

b) de goederen worden naar een plaats buiten de Gemeen- schap vervoerd vóór het einde van de derde maand volgende op die waarin de levering geschiedde;

deze luchtvaartuigen vast verbonden zijn of die voor hun exploitatie dienen;

g) andere dan de in punt f) bedoelde diensten, die voor de rechtstreekse behoeften van de in punt e) bedoelde luchtvaartuigen en hun lading worden verricht.

###### Artikel 149

Portugal mag het vervoer over zee en door de lucht tussen de eilanden die de autonome gebieden van de Azoren en Madeira vormen onderling en tussen deze eilanden en het vasteland gelijkstellen met internationaal vervoer.

###### Artikel 150

1. De Commissie dient, indien nodig, zo spoedig mogelijk voorstellen in bij de Raad om de werkingssfeer en de uitvoering van de in artikel 148 geregelde vrijstellingen nader te bepalen.

2. Totdat de in lid 1 bedoelde bepalingen in werking treden, kunnen de lidstaten de draagwijdte van de in artikel 148, punten a) en b), geregelde vrijstellingen beperken.

## Vrijstellingen voor bepaalde met uitvoer gelijkgestelde handelingen

###### Artikel 151

## 1. De lidstaten verlenen vrijstelling voor de volgende handelin- gen:

a) goederenleveringen en diensten verricht in het kader van de diplomatieke en consulaire betrekkingen;

b) goederenleveringen en diensten bestemd voor internatio- nale instellingen die als dusdanig door de overheid van de lidstaat waar zij zijn gevestigd, zijn erkend, alsmede voor de leden van deze instellingen, zulks binnen de beperkingen en onder de voorwaarden die zijn vastgesteld bij de inter- nationale verdragen tot oprichting van deze instellingen of bij de vestigingsovereenkomsten;

c) goederenleveringen en diensten verricht in de lidstaten die partij zijn bij het Noord-Atlantische Verdrag, en bestemd voor de strijdkrachten van de andere staten die partij bij dat verdrag zijn, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines, voor zover deze strijdkrachten deelnemen aan de gemeenschappelijke defensie-inspanning;

d) goederenleveringen en diensten verricht voor een andere lidstaat, bestemd voor de strijdkrachten van andere staten die partij zijn bij het Noord-Atlantische Verdrag dan de lidstaat van bestemming zelf, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines, voor zover deze strijdkrachten deelnemen aan de gemeenschap- pelijke defensie-inspanning;

###### Artikel 156

## 1. De lidstaten kunnen vrijstelling verlenen voor de volgende handelingen:

a) de levering van goederen die bestemd zijn om bij de douane te worden aangebracht en, in voorkomend geval, in tijdelijke opslag te worden geplaatst;

b) de levering van goederen die bestemd zijn om in een vrije zone of een vrij entrepot te worden geplaatst;

c) de levering van goederen die bestemd zijn om onder een stelsel van douane-entrepots of onder een stelsel van actieve veredeling te worden geplaatst;

d) de levering van goederen die bestemd zijn om in de territoriale zee te worden toegelaten om integrerend deel uit te maken van boor- of werkeilanden, met het oog op de bouw, de reparatie, het onderhoud, de verbouwing of de uitrusting van die boor- of werkeilanden, of om die boor- of werkeilanden met het vasteland te verbinden;

e) de levering van goederen die bestemd zijn om in de territoriale zee te worden toegelaten voor de bevoorrading van boor- of werkeilanden.

2. De in lid 1 bedoelde plaatsen zijn de plaatsen die als zodanig in de geldende communautaire douanevoorschriften zijn omschreven.

###### Artikel 157

## 1. De lidstaten kunnen vrijstelling verlenen voor de volgende handelingen:

a) de invoer van goederen die onder een ander stelsel van entrepots dan dat van douane-entrepots worden geplaatst;

b) de levering van goederen die op hun grondgebied onder een ander stelsel van entrepots dan dat van douane- entrepots worden geplaatst.

2. De lidstaten mogen voor andere goederen dan accijnspro- ducten niet in een ander stelsel van entrepots dan dat van douane-entrepots voorzien, indien deze goederen bestemd zijn om in het kleinhandelsstadium te worden geleverd.

###### Artikel 158

1. In afwijking van artikel 157, lid 2, kunnen de lidstaten in de volgende gevallen een ander stelsel van entrepots dan dat van douane-entrepots invoeren:

a) indien de goederen bestemd zijn voor verkooppunten voor belastingvrije verkoop, met het oog op de levering van goederen welke worden meegenomen in de persoonlijke bagage van reizigers die zich door middel van een vlucht of zeereis naar een derdelandsgebied of een derde land begeven, wanneer die levering overeenkomstig artikel 146, lid 1, punt b), is vrijgesteld;

###### Artikel 162

De lidstaten die van de in deze afdeling bedoelde mogelijkheid gebruikmaken, nemen de nodige maatregelen om te waarborgen dat de intracommunautaire verwerving van goederen die bestemd zijn om onder of in een van de in artikel 156, artikel 157, lid 1, onder b), en artikel 158 bedoelde regelingen of situaties te worden geplaatst, onder dezelfde bepalingen vallen als de goederenlevering die op hun grondgebied onder dezelfde voorwaarden wordt verricht.

###### Artikel 163

Indien de goederen worden onttrokken aan de in deze afdeling bedoelde regelingen of situaties, waardoor aanleiding wordt gegeven tot invoer in de zin van artikel 61, neemt de lidstaat van invoer de nodige maatregelen om dubbele belastingheffing te voorkomen.

Handelingen die worden vr ijges teld met het oog op de uitvoer en in het ka der van het handelsverkeer tussen de lidst aten

###### Artikel 164

1. Na raadpleging van het BTW-Comité kunnen de lidstaten voor de volgende door een belastingplichtige verrichte of voor een belastingplichtige bestemde handelingen, vrijstelling verlenen binnen de grenzen van het bedrag waarvoor deze belasting- plichtige in de afgelopen twaalf maanden heeft uitgevoerd:

a) de intracommunautaire verwerving van goederen door de belastingplichtige alsmede de invoer en de levering van goederen bestemd voor de belastingplichtige die deze goederen betrekt met het oog op hun uitvoer uit de Gemeenschap, al dan niet na verwerking;

b) de diensten in verband met de uitvoeractiviteit van de betreffende belastingplichtige.

2. De lidstaten die gebruikmaken van de in lid 1 bedoelde mogelijkheid tot vrijstelling, verlenen, na raadpleging van het BTW-Comité, deze vrijstelling ook voor handelingen die betrek- king hebben op de door de belastingplichtige onder de in artikel 138 gestelde voorwaarden verrichte leveringen, ten belope van het bedrag van de leveringen die hij onder dezelfde voorwaarden in de voorafgaande twaalf maanden heeft verricht.

###### Artikel 165

De lidstaten kunnen een gemeenschappelijke grens vaststellen voor het bedrag van de vrijstellingen die zij op grond van artikel 164 verlenen.

## Gemeenschappelijke bepaling met betrekking tot de afdelingen 1 en 2

###### Artikel 166

###### Artikel 170

Een belastingplichtige die in de zin van artikel 1 van Richtlijn 79/ 1072/EEG ( 1 ), artikel 1 van Richtlijn 86/560/EEG ( 2 ) en arti- kel 171 van deze richtlijn, niet gevestigd is in de lidstaat waar hij goederen en diensten aankoopt of aan BTW onderworpen goederen invoert, heeft recht op teruggaaf van de BTW indien de goederen en diensten worden gebruikt voor de volgende handelingen:

a) de in artikel 169 bedoelde handelingen;

b) de handelingen waarvoor de belasting overeenkomstig de artikelen 194 tot en met 197 en artikel 199 alleen door de afnemer verschuldigd is.

###### Artikel 171

1. De teruggaaf van de BTW aan belastingplichtigen die niet in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, maar in een andere lidstaat gevestigd zijn, geschiedt volgens de bij Richtlijn 79/1072/EEG van de Raad vastgestelde uitvoeringsbepalingen.

De in artikel 1 van Richtlijn 79/1072/EEG bedoelde belasting- plichtigen die in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, slechts goederenleveringen of diensten hebben verricht waarvoor degene voor wie deze handelingen bestemd zijn, overeenkomstig de artikelen 194 tot en met 197 en artikel 199 is aangewezen als de tot voldoening van de belasting gehouden persoon, worden voor de toepassing van die richtlijn eveneens beschouwd als niet in die lidstaat gevestigde belastingplichtigen.

2. De teruggaaf van de BTW aan belastingplichtigen die niet op het grondgebied van de Gemeenschap gevestigd zijn, geschiedt volgens de bij Richtlijn 86/560/EEG van de Raad vastgestelde uitvoeringsbepalingen.

De in artikel 1 van Richtlijn 86/560/EEG bedoelde belasting- plichtigen die in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, slechts goederenleveringen of diensten hebben verricht waarvoor degene voor wie deze handelingen zijn bestemd, overeenkomstig de artikelen 194 tot en met 197 en artikel 199, is aangewezen als de tot voldoening van de belasting gehouden persoon, worden voor de toepassing van die richtlijn eveneens beschouwd als niet in de Gemeenschap gevestigde belastingplichtigen.

3. De Richtlijnen 79/1072/EEG en 86/560/EEG zijn niet van toepassing op goederenleveringen waarvoor krachtens artikel 138 vrijstelling is verleend of kan worden verleend indien de aldus geleverde goederen door of voor rekening van de afnemer worden verzonden of vervoerd.

###### Artikel 174

## 1. Het aftrekbare gedeelte is de uitkomst van een breuk, waarvan:

a) de teller bestaat uit het totale bedrag van de per jaar berekende omzet, de BTW niet inbegrepen, met betrekking tot handelingen waarvoor overeenkomstig de artikelen 168 en 169 recht op aftrek bestaat, en

b) de noemer bestaat uit het totale bedrag van de per jaar berekende omzet, de BTW niet inbegrepen, met betrekking tot de handelingen die in de teller zijn opgenomen en de handelingen waarvoor geen recht op aftrek bestaat.

De lidstaten kunnen in de noemer het bedrag van andere subsidies opnemen dan die welke rechtstreeks verband houden met de in artikel 73 bedoelde prijs van de handelingen.

2. In afwijking van lid 1 worden voor de berekening van het aftrekbare gedeelte de volgende bedragen buiten beschouwing gelaten:

a) de omzet met betrekking tot de levering van investerings- goederen die door de belastingplichtige in het kader van zijn onderneming worden gebruikt;

b) de omzet met betrekking tot bijkomstige handelingen ter zake van onroerende goederen en bijkomstige financiële handelingen;

c) de omzet met betrekking tot de in artikel 135, lid 1, punten b) tot en met g), bedoelde handelingen die bijkomstig zijn.

3. Indien de lidstaten gebruikmaken van de in artikel 191 geboden mogelijkheid geen herziening voor investeringsgoede- ren te eisen, mogen zij de opbrengst van de verkoop van investeringsgoederen opnemen in de berekening van het aftrek- bare gedeelte.

###### Artikel 175

1. Het aftrekbare gedeelte wordt op jaarbasis vastgesteld, uitgedrukt in een percentage en op de hogere eenheid afgerond.

2. De voorlopige aftrek voor een bepaald jaar is gelijk aan de aftrek die op grond van de handelingen van het voorgaande jaar is berekend. Indien een dergelijke basis ontbreekt of niet relevant is, wordt de aftrek door de belastingplichtige onder toezicht van de belastingdiensten aan de hand van zijn eigen prognoses voorlopig geraamd.

De lidstaten kunnen evenwel hun op 1 januari 1979 geldende regeling dan wel, voor de lidstaten die na die datum tot de Gemeenschap zijn toegetreden, hun op de datum van hun toetreding geldende regeling handhaven.

e) voor de in artikel 168, punt e), bedoelde aftrek met betrekking tot invoer van goederen: in het bezit zijn van een document waaruit de invoer blijkt en waarin hij wordt aangeduid als degene voor wie de invoer bestemd is of als de importeur, en waarin het bedrag van de verschuldigde BTW wordt vermeld of op grond waarvan dat bedrag kan worden berekend;

f) wanneer hij als afnemer tot voldoening van de belasting is gehouden, in geval van toepassing van de artikelen 194 tot en met 197 en artikel 199: de door de respectieve lidstaten voorgeschreven formaliteiten vervullen.

###### Artikel 179

De belastingplichtige past de aftrek toe door op het totale bedrag van de over een belastingtijdvak verschuldigde belasting het totale bedrag van de BTW in mindering te brengen waarvoor in hetzelfde tijdvak het recht op aftrek is ontstaan en krachtens artikel 178 wordt uitgeoefend.

De lidstaten kunnen evenwel bepalen dat belastingplichtigen die de in artikel 12 omschreven handelingen incidenteel verrichten, het recht op aftrek uitsluitend op het tijdstip van levering mogen uitoefenen.

###### Artikel 180

De lidstaten kunnen een belastingplichtige een aftrek toestaan die niet overeenkomstig de artikelen 178 en 179 is toegepast.

###### Artikel 181

De lidstaten kunnen een belastingplichtige die niet in het bezit is van een overeenkomstig de artikelen 220 tot en met 236 opgestelde factuur, toestaan de in artikel 168, punt c), bedoelde aftrek toe te passen met betrekking tot diens intracommunau- taire verwervingen van goederen.

###### Artikel 182

De lidstaten stellen de voorwaarden en de nadere regels voor de toepassing van de artikelen 180 en 181 vast.

###### Artikel 183

Indien voor een bepaald belastingtijdvak het bedrag van de aftrek groter is dan dat van de verschuldigde BTW, kunnen de lidstaten hetzij het overschot doen overbrengen naar het volgende tijdvak, hetzij het overschot teruggeven overeenkomstig de door hen vastgestelde regeling.

De lidstaten kunnen evenwel bepalen dat het bedrag van het overschot niet naar een volgend tijdvak wordt overgebracht, of niet wordt teruggegeven, indien dit bedrag onbeduidend is.

## Herziening van de aftrek

###### Artikel 184

de afnemer een belastingplichtige is die de betrokken investe- ringsgoederen uitsluitend gebruikt voor handelingen waarvoor de BTW in aftrek mag worden gebracht.

###### Artikel 189

Voor de toepassing van de artikelen 187 en 188 kunnen de lidstaten de volgende maatregelen nemen:

a) het begrip investeringsgoederen definiëren;

b) het bedrag aan BTW dat bij de herziening in aanmerking moet worden genomen, nader bepalen;

c) alle passende maatregelen nemen om te verzekeren dat de herziening niet tot ongerechtvaardigde voordelen leidt;

d) administratieve vereenvoudigingen toestaan.

###### Artikel 190

Voor de toepassing van dit hoofdstuk kunnen de lidstaten diensten die kenmerken hebben die vergelijkbaar zijn met de kenmerken die doorgaans aan investeringsgoederen worden toegeschreven, als investeringsgoederen beschouwen.

###### Artikel 191

Indien het praktische effect van de toepassing van de artikelen 187 en 188 in een lidstaat onbeduidend is, kan die lidstaat, na raadpleging van het BTW-Comité, afzien van de toepassing van deze artikelen, rekening houdend met de totale BTW-druk in de betrokken lidstaat en de noodzaak van administratieve vereenvoudiging en mits zulks niet tot verstoring van de mededinging leidt.

###### Artikel 192

Bij overgang van een normale belastingregeling naar een bijzondere regeling, of andersom, kunnen de lidstaten de nodige maatregelen nemen om te verzekeren dat de betrokken belastingplichtigen noch ongerechtvaardigde voordelen genieten, noch ongerechtvaardigde nadelen ondervinden.

VERPLICHTINGEN VAN DE BELASTINGPLICHTIGEN EN VAN BEPAALDE NIET – BELASTINGPLICHTIGE PERSONEN

## Verplichting tot betaling

## Tegenover de schatkist tot voldoening van de belasting gehouden personen

###### Artikel 193

identificeren in de lidstaat waar de belasting verschuldigd is, vervult de verkoper de fiscale verplichtingen namens de afnemer, overeenkomstig de voorschriften van die lidstaat.

2. In het geval dat een belastingplichtige die een keuzerecht overeenkomstig de artikelen 348, 349 of 350 uitoefent, een levering van goud of van halffabrikaten met een zuiverheid van ten minste 325/1 000, of een levering van beleggingsgoud als omschreven in artikel 344, lid 1, verricht, kunnen de lidstaten de afnemer aanwijzen als de tot voldoening van de belasting gehouden persoon.

3. De lidstaten stellen de procedures en voorwaarden voor de toepassing van lid 1 en lid 2 vast.

###### Artikel 199

1. De lidstaten kunnen bepalen dat de tot voldoening van de belasting gehouden persoon degene is voor wie de volgende goederenleveringen of diensten worden verricht:

a) bouwwerkzaamheden, met inbegrip van herstel-, schoon- maak-, onderhouds-, aanpassings- en sloopwerkzaamhe- den ter zake van onroerend goed, alsmede de oplevering van een werk in onroerende staat die krachtens artikel 14, lid 3, als een levering van goederen wordt beschouwd;

b) de uitlening van personeel dat de onder punt a) genoemde werkzaamheden verricht;

c) de levering van onroerend goed als bedoeld in artikel 135, lid 1, punten j) en k), wanneer de leverancier overeenkom- stig artikel 137 heeft gekozen voor belastingheffing ter zake van die levering;

d) de levering van oude materialen, oude materialen onge- schikt voor hergebruik in dezelfde staat, industrieel en niet- industrieel afval, afval voor hergebruik, gedeeltelijk ver- werkt afval, schroot, en bepaalde goederen en diensten, overeenkomstig de lijst in bijlage VI;

e) de levering van in zekerheid gegeven goederen door een belastingplichtige aan een andere persoon tot executie van die zekerheid;

f) de levering van goederen na overdracht van eigendoms- voorbehoud aan een rechtverkrijgende die zijn recht uitoefent;

g) de levering van onroerend goed dat in een openbare verkoop op grond van een executoriale titel door de executieschuldenaar aan een andere persoon wordt ver- kocht.

2. Wanneer zij gebruik maken van de mogelijkheid die lid 1 biedt, kunnen de lidstaten de goederenleveringen en diensten die eronder vallen, omschrijven, alsook de categorieën van leveran- ciers en dienstverrichters of afnemers waarop deze maatregelen van toepassing kunnen zijn.

## 3. Voor de toepassing van lid 1 kunnen de lidstaten de volgende maatregelen nemen:

Verordening (EG) nr. 1798/2003 ( 1 ), kunnen de lidstaten bepalen dat een door deze belastingplichtige aangewezen fiscaal verte- genwoordiger tot voldoening van de belasting wordt gehouden.

De lidstaten kunnen de in de tweede alinea bedoelde mogelijk- heid echter niet toepassen op niet in de Gemeenschap gevestigde belastingplichtigen in de zin van artikel 358, punt 1), die voor de bijzondere regeling voor langs elektronische weg verrichte diensten hebben gekozen.

2. De in lid 1, eerste alinea, bedoelde mogelijkheid is onderworpen aan de door de respectieve lidstaten vastgestelde voorwaarden en uitvoeringsbepalingen.

###### Artikel 205

In de in de artikelen 193 tot en met 200 en 202, 203 en 204 bedoelde situaties kunnen de lidstaten bepalen dat een andere persoon dan degene die tot voldoening van de belasting is gehouden, hoofdelijk verplicht is de BTW te voldoen.

## Wijze van bet aling

###### Artikel 206

Iedere belastingplichtige die tot voldoening van de belasting is gehouden, moet het nettobedrag van de BTW bij de indiening van de in artikel 250 bedoelde aangifte voldoen. De lidstaten kunnen echter een ander tijdstip voor de betaling van dit bedrag vaststellen of bepalen dat voorlopige vooruitbetalingen moeten worden gedaan.

###### Artikel 207

De lidstaten treffen de nodige maatregelen opdat de personen die overeenkomstig de artikelen 194 tot en met 197 en de artikelen 199 en 204 worden geacht in plaats van een niet op hun respectieve grondgebied gevestigde belastingplichtige tot voldoening van de belasting te zijn gehouden, de in deze afdeling vastgestelde betalingsverplichtingen nakomen.

De lidstaten treffen voorts de nodige maatregelen opdat de personen die overeenkomstig artikel 205 worden geacht hoofdelijk verplicht te zijn de BTW te voldoen, deze betalings- verplichtingen nakomen.

###### Artikel 208

De lidstaten die overeenkomstig artikel 198, lid 1, de afnemer van beleggingsgoud als de tot voldoening van de belasting gehouden persoon aanwijzen of gebruik maken van de in artikel 198, lid 2, geboden mogelijkheid om de afnemer van goud, halffabrikaten of beleggingsgoud als omschreven in artikel 344, lid 1, als de tot voldoening van de belasting gehouden persoon aan te wijzen, treffen de nodige maatregelen opdat die afnemer de in deze afdeling vastgestelde betalings- verplichtingen nakomt.

goederenleveringen of diensten verricht welke recht op aftrek doen ontstaan, andere dan de goederenleveringen of de diensten waarvoor overeenkomstig de artikelen 194 tot en met 197 en artikel 199 uitsluitend de afnemer of degene voor wie de goederen of de diensten bestemd zijn, de BTW verschuldigd is;

b) iedere belastingplichtige of niet-belastingplichtige rechts- persoon die intracommunautaire verwervingen van goede- ren verricht welke op grond van artikel 2, lid 1, onder b), aan de BTW zijn onderworpen of die het in artikel 3, lid 3, bedoelde keuzerecht uitoefent zijn intracommunautaire verwervingen aan de BTW te onderwerpen;

c) iedere belastingplichtige die op hun respectieve grond- gebied intracommunautaire verwervingen van goederen verricht met betrekking tot handelingen in verband met de in artikel 9, lid 1, tweede alinea, bedoelde werkzaamheden welke hij buiten dat grondgebied verricht.

2. Het staat de lidstaten vrij bepaalde belastingplichtigen die incidenteel de in artikel 12 bedoelde handelingen verrichten, niet voor BTW-doeleinden te identificeren.

###### Artikel 215

Het individuele identificatienummer begint met een landencode overeenkomstig de ISO-code 3166 alpha 2, die aangeeft welke lidstaat het nummer heeft toegekend.

Griekenland is evenwel gerechtigd het prefix EL te hanteren.

###### Artikel 216

De lidstaten treffen de nodige maatregelen opdat hun identifica- tiesysteem de in artikel 214 bedoelde belastingplichtigen kan onderscheiden en aldus de juiste toepassing van de in artikel 402 bedoelde overgangsregeling voor de belastingheffing op intra- communautaire handelingen verzekert.

## Facturering

## Def initie

###### Artikel 217

Voor de toepassing van dit hoofdstuk wordt onder „ langs elektronische weg verzenden ” verstaan het verzenden of ter beschikking stellen van gegevens aan de geadresseerde door middel van elektronische apparatuur voor gegevensverwerking (inclusief digitale compressie) en gegevensopslag, met gebruik- making van draden, radio, optische of andere elektromagnetische middelen.

## Het beg r ip factuur

###### Artikel 218

###### Artikel 223

Onder de voorwaarden, gesteld door de lidstaten op het grondgebied waarvan de goederenleveringen of de diensten worden verricht, kan voor verscheidene afzonderlijke goederen- leveringen of diensten een periodieke factuur worden opge- maakt.

###### Artikel 224

1. Facturen mogen door de afnemer worden opgemaakt voor goederenleveringen of diensten die door een belastingplichtige voor hem worden verricht, mits beide partijen dat vooraf onderling zijn overeengekomen en op voorwaarde dat iedere factuur het voorwerp uitmaakt van een procedure van aanvaar- ding door de belastingplichtige die de goederenleveringen of de diensten verricht.

2. De voorwaarden en uitvoeringsbepalingen van die vooraf- gaande overeenkomst en van de aanvaardingsprocedures tussen de belastingplichtige en de afnemer worden vastgesteld door de lidstaat op het grondgebied waarvan de goederenleveringen of de diensten worden verricht.

3. De lidstaten kunnen belastingplichtigen die op hun grond- gebied goederenleveringen of diensten verrichten, verdere voorwaarden opleggen betreffende de uitreiking van facturen door de afnemer. Zij kunnen met name verlangen dat die facturen worden uitgereikt in naam en voor rekening van de belastingplichtige.

De in de eerste alinea bedoelde voorwaarden moeten in ieder geval altijd dezelfde zijn, ongeacht de plaats waar de afnemer is gevestigd.

###### Artikel 225

De lidstaten kunnen de belastingplichtigen die op hun grond- gebied goederenleveringen of diensten verrichten, specifieke voorwaarden opleggen in het geval dat de derde, of de afnemer, die de facturen uitreikt, gevestigd is in een land waarmee geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003.

## Inhoud van de facturen

###### Artikel 226

Onverminderd de bijzondere bepalingen van deze richtlijn zijn voor BTW-doeleinden op de overeenkomstig de artikelen 220 en 221 uitgereikte facturen alleen de volgende vermeldingen verplicht:

1) de datum van uitreiking van de factuur;

2) een opeenvolgend nummer, met één of meer reeksen, waardoor de factuur eenduidig wordt geïdentificeerd;

bedoelde gevallen het in artikel 214 bedoelde BTW-identificatie- nummer van hun afnemer te vermelden.

###### Artikel 228

De facturen kunnen evenwel langs elektronische weg worden verzonden of ter beschikking worden gesteld volgens andere methoden, mits deze door de betrokken lidstaten worden aanvaard.

De lidstaten op het grondgebied waarvan goederenleveringen of diensten worden verricht, kunnen ontheffing verlenen van bepaalde verplichte vermeldingen in de met een factuur gelijk- gestelde documenten of berichten bedoeld in artikel 219.

###### Artikel 229

2. Voor de toepassing van lid 1, eerste alinea, punt a), kunnen de lidstaten bovendien eisen dat de geavanceerde elektronische handtekening berust op een gekwalificeerd certificaat en is aangemaakt met een veilig middel voor het aanmaken van handtekeningen in de zin van artikel 2, punten 6) en 10), van Richtlijn 1999/93/EG.

De lidstaten leggen niet de verplichting op de facturen te ondertekenen.

###### Artikel 230

Op een factuur kunnen bedragen in willekeurig welke munt- eenheid voorkomen, mits het te betalen BTW-bedrag is uitge- drukt in de nationale munteenheid van de lidstaat waar de plaats van de goederenlevering of de plaats van de diensten is gelegen en mits daarbij gebruik wordt gemaakt van het in artikel 91 bedoelde wisselkoersmechanisme.

3. Voor de toepassing van lid 1, eerste alinea, punt b), kunnen de lidstaten bovendien onder door hen gestelde voorwaarden de toezending eisen van een aanvullend kort overzicht op papier.

###### Artikel 231

Ter controle kunnen de lidstaten een vertaling eisen in hun nationale taal van de facturen betreffende op hun grondgebied verrichte goederenleveringen of diensten, alsmede van de facturen die worden ontvangen door op hun grondgebied gevestigde belastingplichtigen.

De lidstaten mogen de belastingplichtigen die op hun grond- gebied goederenleveringen of diensten verrichten, geen andere verplichtingen of formaliteiten opleggen betreffende het gebruik van een systeem voor elektronische verzending of terbeschik- kingstelling van facturen.

## Verzenden van facturen langs elektronische weg

###### Artikel 232

De lidstaten kunnen specifieke voorwaarden opleggen voor het langs elektronische weg uitreiken van facturen betreffende goederenleveringen en diensten die op hun grondgebied zijn verricht vanuit een land waarmee geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003.

De overeenkomstig afdeling 2 uitgereikte facturen mogen zowel op papier worden verzonden als, behoudens aanvaarding door de afnemer, elektronisch worden verzonden of ter beschikking gesteld.

###### Artikel 233

1. Elektronisch verzonden of ter beschikking gestelde facturen worden door de lidstaten aanvaard, mits de authenticiteit van de herkomst en de integriteit van de inhoud ervan worden gewaarborgd aan de hand van een van de volgende methoden:

Bij een reeks facturen die langs elektronische weg aan dezelfde afnemer worden verzonden of ter beschikking worden gesteld, hoeven de voor de verschillende facturen gelijke vermeldingen slechts één keer te worden opgenomen, voorzover voor elke factuur alle informatie toegankelijk is.

a) een geavanceerde elektronische handtekening in de zin van artikel 2, punt 2), van Richtlijn 1999/93/EG van het Europees Parlement en de Raad van 13 december 1999 betreffende een gemeenschappelijk kader voor elektroni- sche handtekeningen ( 1 );

b) een elektronische uitwisseling van gegevens (EDI), zoals gedefinieerd in artikel 2 van Aanbeveling 1994/820/EG van de Commissie van 19 oktober 1994 betreffende de juridische aspecten van de elektronische uitwisseling van gegevens ( 2 ), wanneer het akkoord betreffende deze uit- wisseling in het gebruik van procedures voorziet die de

## Vereenvoudigingsmaatregelen

###### Artikel 238

1. Na raadpleging van het BTW-Comité kunnen de lidstaten onder de door hen te stellen voorwaarden bepalen dat op de facturen betreffende op hun grondgebied verrichte goederenle- veringen of diensten in de volgende gevallen sommige van de in de artikelen 226 en 230 voorgeschreven vermeldingen niet behoeven te worden opgenomen, onverminderd de mogelijk- heden waarvan de lidstaten krachtens de artikelen 227, 228 en 231 verkiezen gebruik te maken:

a) wanneer het bedrag van de factuur onbeduidend is;

b) wanneer de handels- of administratieve praktijken van de betrokken bedrijfssector of de technische voorwaarden waaronder die facturen uitgereikt worden, de naleving van alle in de artikelen 226 en 230 bedoelde verplichtingen bemoeilijken.

## 2. De facturen moeten in ieder geval de volgende vermeldingen bevatten:

a) de datum van uitreiking van de factuur;

b) de identificatie van de belastingplichtige;

c) de identificatie van de aard van de geleverde goederen of de verrichte diensten;

d) het te betalen BTW-bedrag of de gegevens aan de hand waarvan dat bedrag kan worden berekend.

3. De vereenvoudiging waarin lid 1 voorziet, mag niet worden toegepast op de handelingen bedoeld in de artikelen 20, 21, 22, 33, 36, 138 en 141.

###### Artikel 239

Ingeval de lidstaten gebruikmaken van de in artikel 272, lid 1, eerste alinea, punt b), geboden mogelijkheid geen BTW- identificatienummer toe te kennen aan belastingplichtigen die geen van de handelingen bedoeld in de artikelen 20, 21, 22, 33, 36, 138 en 141 verrichten, wordt bij niet-toekenning van dat identificatienummer aan de verrichter en de afnemer van de goederenleveringen of de diensten op de factuur een ander nummer vermeld, het zogenaamde fiscaal registratienummer, zoals gedefinieerd door de betrokken lidstaten.

###### Artikel 240

Wanneer het BTW-identificatienummer aan de belastingplichtige is toegekend, kunnen de lidstaten die van de in artikel 272, lid 1, eerste alinea, punt b), bedoelde mogelijkheid gebruik maken, bovendien bepalen dat op de factuur het volgende wordt vermeld:

###### Artikel 245

1. Voor de toepassing van deze richtlijn mag de belasting- plichtige de plaats van bewaring bepalen, mits hij alle overeenkomstig artikel 244 bewaarde facturen of gegevens op ieder verzoek zonder onnodig uitstel ter beschikking van de bevoegde autoriteiten stelt.

2. De lidstaten kunnen de op hun grondgebied gevestigde belastingplichtigen verplichten tot kennisgeving van de plaats van bewaring wanneer deze buiten hun grondgebied gelegen is.

De lidstaten kunnen de op hun grondgebied gevestigde belastingplichtigen er bovendien toe verplichten de door henzelf, door hun afnemers of, in hun naam en voor hun rekening, door derden uitgereikte facturen, alsmede de door hen ontvangen facturen, binnen dat grondgebied te bewaren, wanneer deze bewaring niet geschiedt langs een elektronische weg die een volledige on – linetoegang tot de betrokken gegevens waarborgt.

###### Artikel 246

De authenticiteit van de oorsprong en de integriteit van de inhoud van de bewaarde facturen, alsmede de leesbaarheid ervan, moeten gedurende de volledige periode van bewaring worden gewaarborgd.

De gegevens op de in artikel 233, lid 1, tweede alinea, bedoelde facturen mogen niet worden gewijzigd en moeten gedurende deze periode leesbaar blijven.

###### Artikel 247

1. Iedere lidstaat bepaalt hoe lang de belastingplichtigen ervoor moeten zorgen dat de facturen betreffende de op zijn grond- gebied verrichte goederenleveringen of diensten en de facturen die op zijn grondgebied gevestigde belastingplichtigen hebben ontvangen, moeten worden bewaard.

2. Om te waarborgen dat de in artikel 246 bedoelde voorwaarden worden vervuld, kan de in lid 1 bedoelde lidstaat bepalen dat de facturen moeten worden bewaard in de oorspronkelijke vorm — op papier of elektronisch — waarin zij zijn toegezonden of ter beschikking gesteld. De lidstaat kan tevens bepalen dat, wanneer de facturen langs elektronische weg worden bewaard, de gegevens die de authenticiteit van de herkomst en de integriteit van de inhoud overeenkomstig artikel 246, eerste alinea, waarborgen, eveneens worden bewaard.

3. De in lid 1 bedoelde lidstaat kan bijzondere voorwaarden stellen met het oog op het verbieden of beperken van de bewaring van de facturen in een land waarmee geen rechts- instrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003 of inzake het in artikel 249 bedoelde recht van elektronische toegang, downloading en gebruik.

###### Artikel 248

goederenleveringen die zijn verricht in de lidstaat waar de aangifte moet worden ingediend, en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden, wanneer de plaats van vertrek van de verzending of het vervoer van de goederen op het grondgebied van een andere lidstaat is gelegen;

e) het totale bedrag, de BTW niet inbegrepen, van de goederenleveringen, verricht in de lidstaat waar de aangifte moet worden ingediend, waarvoor de belastingplichtige overeenkomstig artikel 197 als de tot voldoening van de belasting gehouden persoon is aangewezen en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden.

###### Artikel 252

1. De BTW-aangifte moet worden ingediend binnen een door de lidstaten vast te stellen termijn. Deze termijn mag niet langer zijn dan twee maanden na het verstrijken van ieder belasting- tijdvak.

2. Het belastingtijdvak wordt door de lidstaten vastgesteld op een, twee of drie maanden.

De lidstaten kunnen evenwel andere belastingtijdvakken bepalen, die echter niet langer dan een jaar mogen zijn.

###### Artikel 253

Zweden mag voor kleine en middelgrote ondernemingen een vereenvoudigde procedure toepassen, waarbij de indiening van de BTW-aangifte kan geschieden drie maanden na het verstrijken van het directe-belastingjaar voor belastingplichtigen die uitslui- tend binnenlandse belastbare handelingen verrichten.

###### Artikel 254

Voor leveringen van nieuwe vervoermiddelen onder de in artikel 138, lid 2, onder a), gestelde voorwaarden door een voor BTW – doeleinden geïdentificeerde belastingplichtige aan een niet voor BTW-doeleinden geïdentificeerde afnemer, of door een in artikel 9, lid 2, bedoelde belastingplichtige, treffen de lidstaten de nodige maatregelen opdat de verkoper alle gegevens verschaft die noodzakelijk zijn voor de toepassing van de BTW en voor de controle daarop door de belastingdienst.

###### Artikel 255

De lidstaten die overeenkomstig artikel 198, lid 1, de afnemer van beleggingsgoud als de tot voldoening van de belasting gehouden persoon aanwijzen of gebruik maken van de in artikel 198, lid 2, geboden mogelijkheid om de afnemer van goud, halffabrikaten of beleggingsgoud als omschreven in artikel 344, lid 1, als de tot voldoening van de belasting gehouden persoon aan te wijzen, treffen de nodige maatregelen opdat die afnemer de in deze afdeling vastgestelde verplichtingen inzake aangifte nakomt.

###### Artikel 256

De lidstaten kunnen evenwel bepalen dat de lijsten maandelijks worden ingediend.

2. De lidstaten staan onder door hen te stellen voorwaarden toe dat de in lid 1 bedoelde lijsten langs elektronische weg worden ingediend en mogen dit ook verplicht stellen.

###### Artikel 264

## 1. Op de lijst worden de volgende gegevens vermeld:

a) het nummer waaronder de belastingplichtige voor BTW- doeleinden is geïdentificeerd in de lidstaat waar de lijst moet worden ingediend, en waaronder hij goederenleveringen heeft verricht onder de in artikel 138, lid 1, gestelde voorwaarden;

b) het nummer waaronder elke afnemer voor BTW-doel- einden is geïdentificeerd in een andere lidstaat dan die waar de lijst moet worden ingediend, en waaronder de goederen aan hem geleverd zijn;

c) het nummer waaronder de belastingplichtige voor BTW- doeleinden is geïdentificeerd in de lidstaat waar de lijst moet worden ingediend, en waaronder hij de in artikel 138, lid 2, onder c), bedoelde overbrenging naar een andere lidstaat heeft verricht, alsmede het nummer waaronder hij in de lidstaat van aankomst van de verzending of het vervoer is geïdentificeerd;

d) voor elke afnemer het totale bedrag van de door de belastingplichtige verrichte goederenleveringen;

e) voor de in artikel 138, lid 2, onder c) bedoelde leveringen bestaande uit de overbrenging van goederen naar een andere lidstaat, het totale bedrag van deze leveringen, vastgesteld overeenkomstig artikel 76;

f) het bedrag van de krachtens artikel 90 verrichte herzie- ningen.

2. Het in lid 1, punt d), bedoelde bedrag wordt opgegeven voor het kalenderkwartaal waarin de belasting verschuldigd is geworden.

Het in lid 1, punt f), bedoelde bedrag wordt opgegeven voor het kalenderkwartaal waarin van de herziening kennis is gegeven aan de afnemer.

###### Artikel 265

1. In de in artikel 43 bedoelde gevallen van intracommunau- taire verwerving van goederen dient de belastingplichtige die voor BTW-doeleinden is geïdentificeerd in de lidstaat welke het BTW-nummer heeft toegekend waaronder de belastingplichtige deze verwervingen heeft verricht, duidelijk de volgende gegevens op de lijst te vermelden:

a) het nummer waaronder hij voor BTW-doeleinden in die lidstaat is geïdentificeerd en waaronder hij de verwerving en de daaropvolgende goederenlevering heeft verricht;

b) het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden bedraagt niet meer dan EUR 15 000 of de tegenwaarde daarvan in de nationale munteenheid;

c) de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden zijn geen leveringen van nieuwe vervoermiddelen.

###### Artikel 271

Uit hoofde van de in artikel 269 bedoelde machtiging kunnen de lidstaten die de duur van het belastingtijdvak waarover een belastingplichtige de in artikel 250 bedoelde BTW-aangifte moet indienen, op meer dan drie maanden vaststellen, deze belasting- plichtige toestaan de lijst over datzelfde tijdvak in te dienen, wanneer de belastingplichtige de volgende drie voorwaarden vervult:

a) het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de door hem verrichte goederenleveringen en diensten bedraagt niet meer dan EUR 200 000 of de tegenwaarde daarvan in de nationale munteenheid;

b) het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden bedraagt niet meer dan EUR 15 000 of de tegenwaarde daarvan in de nationale munteenheid;

c) de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden zijn geen leveringen van nieuwe vervoermiddelen.

## Diverse bepalingen

###### Artikel 272

1. De lidstaten kunnen de volgende belastingplichtigen van bepaalde verplichtingen of van alle verplichtingen bedoeld in de hoofdstukken 2 tot en met 6 ontheffen:

a) de belastingplichtigen wier intracommunautaire verwervin- gen overeenkomstig artikel 3, lid 1, niet aan de BTW zijn onderworpen;

b) de belastingplichtigen die geen van de in de artikelen 20, 21, 22, 33, 36, 138 en 141 bedoelde handelingen verrichten;

c) de belastingplichtigen die slechts goederenleveringen of diensten verrichten die uit hoofde van de artikelen 132, 135 en 136, de artikelen 146 tot en met 149 en de artikelen 151, 152 en 153 zijn vrijgesteld;

d) de belastingplichtigen die in aanmerking komen voor de in de artikelen 282 tot en met 292 vervatte vrijstellings- regeling voor kleine ondernemingen;

e) de belastingplichtigen die voor de forfaitaire regeling voor landbouwproducenten in aanmerking komen.

###### Artikel 277

Wanneer de in artikel 274 bedoelde goederen zich op het moment van het binnenbrengen ervan in de Gemeenschap bevinden in een van de situaties waardoor zij, indien zij ingevoerd waren in de zin van artikel 30, eerste alinea, in aanmerking konden komen voor een van de in artikel 156 bedoelde regelingen of situaties of voor een regeling van tijdelijke invoer met volledige vrijstelling van invoerrechten, nemen de lidstaten de maatregelen om ervoor te zorgen dat deze goederen onder dezelfde voorwaarden in de Gemeenschap kunnen verblijven als die welke voor de toepassing van die regelingen of situaties gelden.

De in deze afdeling vastgestelde vrijstellingen en verminderingen zijn van toepassing op door kleine ondernemingen verrichte goederenleveringen en diensten.

## 1. De volgende handelingen zijn van de in deze afdeling vastgestelde regeling uitgesloten:

## Uitvoerhandelingen

a) de in artikel 12 bedoelde incidenteel verrichte handelingen;

###### Artikel 278

b) de leveringen van nieuwe vervoermiddelen verricht onder de in artikel 138, lid 1, en lid 2, onder a), gestelde voorwaarden;

De artikelen 279 en 280 zijn van toepassing op de uitvoer- handelingen met betrekking tot goederen in het vrije verkeer die vanuit een lidstaat worden verzonden of vervoerd naar een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap.

c) de goederenleveringen en de diensten die worden verricht door een belastingplichtige die niet is gevestigd in de lidstaat waar de BTW verschuldigd is.

###### Artikel 279

De formaliteiten betreffende de uitvoer van de in artikel 278 bedoelde goederen uit het douanegebied van de Gemeenschap zijn dezelfde als die welke zijn voorgeschreven in de geldende communautaire douanebepalingen betreffende de uitvoer van goederen uit het douanegebied van de Gemeenschap.

2. De lidstaten kunnen andere dan de in lid 1 bedoelde handelingen van de in deze afdeling vastgestelde regeling uitsluiten.

###### Artikel 280

1. De lidstaten die gebruik hebben gemaakt van de in artikel 14 van Richtlijn 67/228/EEG van de Raad van 11 april 1967 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting — Structuur en wijze van toepassing van het gemeenschappelijk stelsel van belasting over de toegevoegde waarde ( 1 ) gegeven mogelijkheid vrijstellingen of degressieve verminderingen van de belasting in te voeren, mogen deze alsmede de desbetreffende uitvoeringsbepalingen handhaven, indien zij met het BTW-stelsel in overeenstemming zijn.

Voor goederen die tijdelijk uit de Gemeenschap worden uitge- voerd met het oog op wederinvoer, nemen de lidstaten de nodige maatregelen om ervoor te zorgen dat die goederen bij hun wederinvoer in de Gemeenschap in aanmerking komen voor dezelfde bepalingen als wanneer zij tijdelijk uit het douanegebied van de Gemeenschap waren uitgevoerd.

BIJZONDERE REGELINGEN

## Bijzondere regeling voor kleine ondernemingen

## Vereenvoudigde bepalingen inzake belastin gheff ing en belastinginning

###### Artikel 281

De in de eerste alinea bedoelde lidstaten kunnen een degressieve belastingvermindering toekennen aan belastingplichtigen wier jaaromzet het plafond overschrijdt dat deze lidstaten voor de toepassing van de vrijstelling hebben vastgesteld.

###### Artikel 286

De lidstaten die op 17 mei 1977 een vrijstelling van belasting toekenden aan belastingplichtigen met een jaaromzet gelijk aan of hoger dan de tegenwaarde van 5 000 Europese rekeneenheden in de nationale munteenheid tegen de op die datum geldende omrekeningskoers, mogen deze vrijstelling verhogen teneinde de reële waarde ervan te handhaven.

###### Artikel 287

De lidstaten die na 1 januari 1978 zijn toegetreden, kunnen een vrijstelling van belasting toekennen aan belastingplichtigen met een jaarlijkse omzet die ten hoogste gelijk is aan de tegenwaarde in de nationale munteenheid van de volgende bedragen tegen de op de dag van hun toetreding geldende omrekeningskoers:

1) Griekenland: 10 000 Europese rekeneenheden;

2) Spanje: 10 000 ecu;

3) Portugal: 10 000 ecu;

4) Oostenrijk: 35 000 ecu;

5) Finland: 10 000 ecu;

6) Zweden: 10 000 ecu;

7) Tsjechië: EUR 35 000;

8) Estland: EUR 16 000;

9) Cyprus: EUR 15 600;

10) Letland: EUR 17 200;

11) Litouwen: EUR 29 000;

12) Hongarije: EUR 35 000;

13) Malta: EUR 37 000 wanneer de economische activiteit voornamelijk bestaat uit goederenleveringen, EUR 24 300 wanneer de economische activiteit voornamelijk bestaat uit diensten met een lage toegevoegde waarde (hoge inputs), en EUR 14 600 in andere gevallen, namelijk diensten met een hoge toegevoegde waarde (lage inputs);

14) Polen: EUR 10 000;

15) Slovenië: EUR 25 000;

## Verslag en herziening

###### Artikel 293

De Commissie brengt aan de Raad, op grond van de van de lidstaten verkregen gegevens, vanaf de aanneming van deze richtlijn om de vier jaar verslag uit over de toepassing van dit hoofdstuk, indien nodig en rekening houdend met de noodzaak van uiteindelijke convergentie van de nationale regelingen, vergezeld van voorstellen betreffende de volgende punten:

1) de in de bijzondere regeling voor kleine ondernemingen aan te brengen verbeteringen;

2) de aanpassing van de nationale regelingen inzake vrijstel- lingen en degressieve belastingverminderingen;

3) de aanpassing van de in afdeling 2 bedoelde maximumbe- dragen.

###### Artikel 294

De Raad bepaalt overeenkomstig artikel 93 van het Verdrag of in het kader van de definitieve regeling een bijzondere regeling voor kleine ondernemingen nodig is, en neemt, in voorkomend geval, tevens een beslissing over de gemeenschappelijke grenzen en toepassingsvoorwaarden van de genoemde bijzondere regeling.

## Gemeenschappelijke forfaitaire regeling voor landbouwproducenten

###### Artikel 295

## 1. Voor de toepassing van dit hoofdstuk wordt verstaan onder:

1) landbouwproducent: de belastingplichtige die zijn werk- zaamheid uitoefent in het kader van een landbouw-, bosbouw- of visserijbedrijf;

2) landbouw-, bosbouw- of visserijbedrijf: de bedrijven die door elke lidstaat als zodanig worden beschouwd in het kader van de in bijlage VI vermelde productiewerkzaam- heden;

3) forfaitair belaste landbouwer: de landbouwproducent op wie de in dit hoofdstuk vastgestelde forfaitaire regeling van toepassing is;

4) landbouwproducten: de goederen die door de landbouw-, bosbouw- of visserijbedrijven van elke lidstaat worden voortgebracht door middel van de in bijlage VI vermelde werkzaamheden;

5) agrarische diensten: de diensten, met name de in bijlage VIII genoemde, die worden verricht door een landbouwprodu- cent met gebruikmaking van zijn arbeidskrachten of de normale uitrusting van zijn landbouw-, bosbouw- of visserijbedrijf en die normaliter tot de verwezenlijking van de landbouwproductie bijdragen;

De percentages mogen naar boven of naar beneden op een half punt worden afgerond. De lidstaten kunnen deze percentages ook tot nihil terugbrengen.

###### Artikel 299

De forfaitaire compensatiepercentages mogen niet tot gevolg hebben dat aan de forfaitair belaste landbouwers gezamenlijk bedragen worden terugbetaald die hoger zijn dan de BTW- voordruk.

###### Artikel 300

De forfaitaire compensatiepercentages worden toegepast op de prijs, de BTW niet inbegrepen, van de volgende goederen en diensten:

1) de landbouwproducten die de forfaitair belaste landbouwers hebben geleverd aan andere belastingplichtigen dan die welke in de lidstaat waar deze leveringen zijn verricht onder deze forfaitaire regeling vallen;

2) de landbouwproducten die de forfaitair belaste landbouwers onder de in artikel 138 gestelde voorwaarden hebben geleverd aan niet – belastingplichtige rechtspersonen wier intracommunautaire verwervingen overeenkomstig arti- kel 2, lid 1, onder b), aan de BTW zijn onderworpen in de lidstaat van aankomst van de verzending of het vervoer van de aldus geleverde landbouwproducten;

3) de agrarische diensten die worden verricht door forfaitair belaste landbouwers voor andere belastingplichtigen dan die welke in de lidstaat waar deze diensten zijn verricht onder deze forfaitaire regeling vallen.

###### Artikel 301

1. Voor de in artikel 300 bedoelde landbouwproductenleve- ringen en agrarische diensten bepalen de lidstaten dat de forfaitaire compensaties hetzij door de afnemer hetzij door de overheid worden betaald.

2. Voor andere dan de in artikel 300 bedoelde landbouw- productenleveringen en agrarische diensten worden de forfaitaire compensaties geacht betaald te worden door de afnemer.

###### Artikel 302

Wanneer een forfaitair belaste landbouwer een forfaitaire compensatie geniet, heeft hij voor de onder deze forfaitaire regeling vallende werkzaamheden geen recht op aftrek.

###### Artikel 303

Deze bijzondere regeling is niet van toepassing op reisbureaus die alleen handelen als tussenpersoon en waarop artikel 79, eerste alinea, punt c), van toepassing is om de maatstaf van heffing te berekenen.

2. Voor de toepassing van dit hoofdstuk worden reisorganisa- toren (tour-operators) als reisbureaus beschouwd.

###### Artikel 307

De onder de voorwaarden van artikel 306 verrichte handelingen van het reisbureau met het oog op de totstandkoming van de reis, worden beschouwd als één enkele dienst die het reisbureau voor de reiziger verricht.

Deze ene dienst wordt belast in de lidstaat waar het reisbureau de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd van waaruit het de dienst heeft verricht.

###### Artikel 308

Voor de door het reisbureau verrichte ene dienst wordt als maatstaf van heffing en prijs, de BTW niet inbegrepen, in de zin van artikel 226, punt 8), beschouwd de winstmarge van het reisbureau, dat wil zeggen het verschil tussen het totale bedrag, de BTW niet inbegrepen, dat de reiziger moet betalen en de werkelijk door het reisbureau gedragen kosten voor goederen- leveringen en diensten van andere belastingplichtigen, mits deze handelingen de reiziger rechtstreeks ten goede komen.

###### Artikel 309

Indien de handelingen waarvoor het reisbureau een beroep doet op andere belastingplichtigen, door laatstgenoemden buiten de Gemeenschap worden verricht, wordt de dienst van het reisbureau gelijkgesteld met een krachtens artikel 153 vrijgestelde handeling van een tussenpersoon.

Indien de in de eerste alinea bedoelde handelingen zowel binnen als buiten de Gemeenschap worden verricht, mag alleen het gedeelte van de dienst van het reisbureau betreffende de buiten de Gemeenschap verrichte handelingen als vrijgesteld worden beschouwd.

###### Artikel 310

## Bijzondere regeling voor belastin gplichtige weder verkopers

Winstmargeregeling

###### Artikel 312

## Voor de toepassing van deze onderafdeling wordt verstaan onder:

1) „ verkoopprijs ” : alles wat de tegenprestatie uitmaakt die een belastingplichtige wederverkoper verkrijgt of moet verkrij- gen van de afnemer of een derde, met inbegrip van subsidies die rechtstreeks verband houden met de hande- ling, belastingen, rechten, heffingen en bijkomende kosten zoals kosten van commissie, verpakking, vervoer en verzekering die de belastingplichtige wederverkoper de afnemer in rekening brengt, echter met uitsluiting van de in artikel 79 bedoelde bedragen;

2) „ aankoopprijs ” : alles wat de in punt 1) gedefinieerde tegenprestatie uitmaakt die de leverancier van de belasting- plichtige wederverkoper verkrijgt of moet verkrijgen.

###### Artikel 313

1. De lidstaten passen op door belastingplichtige wederver- kopers verrichte leveringen van gebruikte goederen, kunst- voorwerpen, voorwerpen voor verzamelingen en antiquiteiten een bijzondere regeling toe voor de belastingheffing over de winstmarge van de belastingplichtige wederverkoper, overeen- komstig het bepaalde in deze onderafdeling.

2. Tot de invoering van de in artikel 402 bedoelde definitieve regeling is de in lid 1 van dit artikel bedoelde regeling niet van toepassing op leveringen van nieuwe vervoermiddelen die worden verricht onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden.

###### Artikel 314

De winstmargeregeling is van toepassing op door een belasting- plichtige wederverkoper verrichte leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, wanneer deze goederen hem binnen de Gemeenschap door een der onderstaande personen worden geleverd:

a) een niet-belastingplichtige;

b) een andere belastingplichtige, voor zover de levering van het goed door deze andere belastingplichtige overeenkom- stig artikel 133 is vrijgesteld;

c) een andere belastingplichtige, voor zover de levering van het goed door deze andere belastingplichtige in aanmerking komt voor de in de artikelen 282 tot en met 292 bedoelde vrijstellingsregeling voor kleine ondernemingen en het gaat om een investeringsgoed;

wederverkoper, verminderd met het bedrag van de BTW op diezelfde winstmarge.

## 2. De totale winstmarge is gelijk aan het verschil tussen de volgende twee bedragen:

a) het totale bedrag van de goederenleveringen die onder- worpen zijn aan de winstmargeregeling en die gedurende het belastingtijdvak door de belastingplichtige wederver- koper verricht zijn, dit wil zeggen de som van de verkoopprijzen;

b) het totale bedrag van de in artikel 314 bedoelde goederenaankopen die gedurende het belastingtijdvak door de belastingplichtige wederverkoper zijn verricht, dit wil zeggen de som van de aankoopprijzen.

3. De lidstaten treffen de nodige maatregelen om te voorkomen dat de in lid 1 bedoelde belastingplichtigen ongerechtvaardigde voordelen genieten of ongerechtvaardigde schade lijden.

###### Artikel 319

Voor elke levering die onder de winstmargeregeling valt, kan de belastingplichtige wederverkoper de normale BTW – regeling toepassen.

###### Artikel 320

1. De belastingplichtige wederverkoper die de normale BTW- regeling toepast op de levering van kunstvoorwerpen, voor- werpen voor verzamelingen en antiquiteiten welke hij zelf heeft ingevoerd, heeft het recht de bij invoer van dit goed verschuldigde of voldane BTW af te trekken van het door hem verschuldigde belastingbedrag.

De belastingplichtige wederverkoper die de normale BTW- regeling toepast op de levering van kunstvoorwerpen welke hem door de maker of diens rechthebbenden of door een andere belastingplichtige dan een belastingplichtige wederverkoper zijn geleverd, heeft het recht, de met betrekking tot de hem geleverde kunstvoorwerpen verschuldigde of voldane BTW af te trekken van het door hem verschuldigde belastingbedrag.

2. Het recht op aftrek ontstaat op het tijdstip waarop de belasting verschuldigd wordt voor de levering waarvoor de belastingplichtige wederverkoper voor de normale BTW-regeling kiest.

###### Artikel 321

2. Deze overgangsregeling is niet van toepassing op de leveringen van nieuwe vervoermiddelen die worden verricht onder de in artikel 138 , lid 1 en lid 2, onder a), gestelde voorwaarden.

3. Voor de toepassing van lid 1 worden als „ gebruikte vervoermiddelen ” beschouwd de in artikel 2, lid 2, onder a), bedoelde landvoertuigen, schepen en luchtvaartuigen die gebruikte goederen zijn welke niet aan de voorwaarden voldoen om als nieuwe vervoermiddelen te worden beschouwd.

###### Artikel 328

De voor elke in artikel 327 bedoelde levering verschuldigde BTW is gelijk aan het bedrag van de belasting die verschuldigd zou zijn indien de levering onder de normale BTW-regeling zou zijn gevallen, verminderd met het BTW-bedrag dat geacht wordt nog begrepen te zijn in de aankoopprijs van het vervoermiddel door de belastingplichtige wederverkoper.

###### Artikel 329

De BTW die geacht wordt nog in de aankoopprijs van het vervoermiddel door de belastingplichtige wederverkoper te zijn begrepen, wordt als volgt berekend:

a) de in aanmerking te nemen aankoopprijs is de aankoopprijs in de zin van artikel 312, punt 2);

b) deze door de belastingplichtige wederverkoper betaalde aankoopprijs wordt geacht de BTW te omvatten die verschuldigd zou zijn geweest indien de leverancier van de belastingplichtige wederverkoper de normale BTW – regeling op zijn levering had toegepast;

c) het in aanmerking te nemen tarief is het tarief dat uit hoofde van artikel 93 van toepassing is in de lidstaat binnen het grondgebied waarvan de overeenkomstig de artikelen 31 en 32 bepaalde plaats van levering aan de belastingplichtige wederverkoper wordt geacht te zijn gelegen.

###### Artikel 330

De voor elke in artikel 327, lid 1, bedoelde levering van vervoermiddelen verschuldigde BTW, vastgesteld overeenkomstig artikel 328, mag niet minder bedragen dan het BTW-bedrag dat verschuldigd zou zijn indien deze levering aan de winstmarge- regeling onderworpen zou zijn geweest.

De lidstaten kunnen bepalen dat, indien de levering aan de winstmargeregeling onderworpen zou zijn geweest, deze winst- marge niet lager mag zijn dan 10 % van de verkoopprijs in de zin van artikel 312, punt 1).

###### Artikel 331

###### Artikel 336

De maatstaf van heffing voor elke in deze afdeling bedoelde goederenlevering is het overeenkomstig artikel 339 door de organisator van de openbare veiling aan de afnemer in rekening gebrachte totale bedrag, verminderd met de volgende bedragen:

a) het door de organisator van de openbare veiling aan zijn opdrachtgever betaalde of te betalen nettobedrag, vastge- steld overeenkomstig artikel 337;

b) het bedrag van de door de organisator van de openbare veiling krachtens zijn levering verschuldigde BTW.

###### Artikel 337

Het door de organisator van de openbare veiling aan zijn opdrachtgever betaalde of te betalen nettobedrag is gelijk aan het verschil tussen de prijs waarvoor het goed geveild is, en het bedrag van de door de organisator van zijn opdrachtgever ontvangen of te ontvangen commissie krachtens de overeen- komst tot verkoop in commissie.

###### Artikel 338

De organisatoren van openbare veilingen die onder de in de artikelen 333 en 334 vastgestelde voorwaarden goederen leveren, zijn gehouden de volgende bedragen in hun boekhou- ding op tussenrekeningen te boeken:

a) de van de afnemer van het goed ontvangen of te ontvangen bedragen;

b) de aan de verkoper van het goed betaalde of te betalen bedragen.

De in de eerste alinea bedoelde bedragen moeten naar behoren gerechtvaardigd worden.

###### Artikel 339

De organisator van de openbare veiling moet aan de afnemer een factuur uitreiken waarop de volgende gegevens afzonderlijk zijn vermeld:

a) de veilingprijs;

b) de belastingen, rechten en heffingen;

c) de bijkomende kosten, zoals kosten van commissie, verpakking, vervoer en verzekering, die de organisator de afnemer van het goed in rekening brengt.

Op de door de organisator van de openbare veiling uitgereikte factuur mag de BTW niet afzonderlijk zijn vermeld.

###### Artikel 340

1. De organisator van de openbare veiling aan wie het goed is overgedragen krachtens een overeenkomst tot verkoop in commissie op een openbare veiling, verstrekt aan zijn opdracht- gever een verslag.

2) gouden munten die een zuiverheid van ten minste 900/ 1 000 hebben, na 1800 zijn geslagen, in het land van oorsprong als wettig betaalmiddel fungeren of hebben gefungeerd en normaal worden verkocht voor een prijs die de openmarktwaarde van het in de munten vervatte goud niet met meer dan 80 % overschrijdt.

2. De lidstaten kunnen kleine staven of plaatjes met een gewicht van ten hoogste 1 gram uitsluiten van deze bijzondere regeling.

3. Voor de toepassing van deze richtlijn worden de in lid 1, punt 2), bedoelde munten niet geacht wegens hun numismatisch belang te worden verkocht.

###### Artikel 345

Vanaf 1999 deelt elke lidstaat de Commissie, vóór 1 juli van elk jaar, mee welke munten die aan de in artikel 344, lid 1, punt 2), genoemde criteria voldoen, in die lidstaat worden verhandeld. Vóór 1 december van elk jaar publiceert de Commissie in de reeks C van het Publicatieblad van de Europese Unie de volledige lijst van deze munten. De in de gepubliceerde lijst opgenomen munten worden geacht aan deze criteria te voldoen gedurende het gehele jaar waarvoor de lijst wordt gepubliceerd.

## Vr ijstelling van de belastin g

###### Artikel 346

De lidstaten verlenen vrijstelling van de BTW voor de levering, de intracommunautaire verwerving en de invoer van beleggings- goud, waaronder beleggingsgoud dat belichaamd is in certifi- caten voor toegewezen of niet toegewezen goud of dat verhandeld wordt op goudrekeningen, en waaronder, in het bijzonder, goudleningen en swaps, die een eigendoms- of vorderingsrecht op beleggingsgoud belichamen, evenals voor handelingen betreffende beleggingsgoud bestaande in future- en termijncontracten die leiden tot de overdracht van een eigen- doms- of vorderingsrecht met betrekking tot beleggingsgoud.

###### Artikel 347

De lidstaten verlenen vrijstelling voor de diensten van agenten die optreden in naam en voor rekening van een ander wanneer zij betrokken zijn bij de levering van beleggingsgoud voor hun principaal.

## Recht om voor belastin gheff ing te kiezen

###### Artikel 348

De lidstaten verlenen belastingplichtigen die beleggingsgoud produceren of goud omzetten in beleggingsgoud, het recht te kiezen voor belastingheffing over de leveringen van beleggings- goud aan een andere belastingplichtige welke anders uit hoofde van artikel 346 zouden zijn vrijgesteld.

###### Artikel 349

beleggingsgoud dat vervolgens door hem of in zijn naam wordt omgezet in beleggingsgoud;

c) de BTW die verschuldigd of voldaan is met betrekking tot voor hem verrichte diensten bestaande in een wijziging van de vorm, het gewicht of de zuiverheid van goud met inbegrip van beleggingsgoud.

###### Artikel 355

Belastingplichtigen die beleggingsgoud produceren of goud in beleggingsgoud omzetten, hebben recht op aftrek van de belasting die door hen verschuldigd of voldaan is met betrekking tot de levering, de intracommunautaire verwerving of de invoer van goederen of met betrekking tot diensten die met de productie of de omzetting van dat goud verband houden, alsof de daaropvolgende levering van het krachtens artikel 346 vrijgestelde goud belast was.

###### Artikel 356

1. De lidstaten zorgen ervoor dat handelaren in beleggingsgoud ten minste een boekhouding voeren van alle belangrijke handelingen betreffende beleggingsgoud en de documenten bewaren aan de hand waarvan de identiteit van de afnemer bij dergelijke handelingen kan worden vastgesteld.

De handelaren bewaren de in de eerste alinea bedoelde informatie gedurende ten minste vijf jaar.

2. De lidstaten kunnen evenwaardige verplichtingen uit hoofde van maatregelen vastgesteld krachtens andere communautaire wetgeving, zoals Richtlijn 2005/60/EG van het Europees Parlement en de Raad van 26 oktober 2005 tot voorkoming van het gebruik van het financiële stelsel voor het witwassen van geld en de financiering van terrorisme ( 1 ), aanvaarden om aan de vereisten van lid 1 te voldoen.

3. De lidstaten kunnen strengere verplichtingen vaststellen, inzonderheid inzake speciale registratie- of boekhoudingsver- eisten.

Bijzondere regeling voor niet in de Gemeenschap gevestigde belastingplichtigen die langs elektronische weg diensten verrichten voor niet-belastingplichtigen

## Algemene bepalingen

###### Artikel 357

Dit hoofdstuk is van toepassing tot en met 31 december 2006.

###### Artikel 358

## Onverminderd andere communautaire bepalingen wordt voor de toepassing van dit hoofdstuk verstaan onder:

1) „ niet in de Gemeenschap gevestigde belastingplichtige ” : een belastingplichtige die de zetel van zijn bedrijfsuitoefening niet op het grondgebied van de Gemeenschap heeft

2. De niet in de Gemeenschap gevestigde belastingplichtige doet de lidstaat van identificatie mededeling van eventuele wijzigingen in de verstrekte informatie.

###### Artikel 362

De lidstaat van identificatie kent de niet in de Gemeenschap gevestigde belastingplichtige een individueel identificatienummer toe en deelt hem dit nummer langs elektronische weg mee. Uitgaande van de voor deze identificatie gebruikte gegevens mogen de lidstaten van verbruik hun eigen identificatiesystemen gebruiken.

###### Artikel 363

De lidstaat van identificatie verwijdert de niet in de Gemeenschap gevestigde belastingplichtige in de volgende gevallen uit het identificatieregister:

a) de belastingplichtige deelt die lidstaat mee dat hij niet langer elektronische diensten verricht;

b) er kan anderszins worden aangenomen dat zijn belastbare activiteiten beëindigd zijn;

c) hij vervult niet langer de voorwaarden om van de bijzondere regeling gebruik te mogen maken;

d) hij voldoet bij voortduring niet aan de voorschriften van de bijzondere regeling.

###### Artikel 364

De niet in de Gemeenschap gevestigde belastingplichtige dient langs elektronische weg bij de lidstaat van identificatie een BTW- aangifte in voor elk kalenderkwartaal, ongeacht of er elektro- nische diensten zijn verricht. De aangifte wordt uiterlijk 20 dagen na het verstrijken van het belastingtijdvak waarop de aangifte betrekking heeft, ingediend.

###### Artikel 365

De BTW-aangifte bevat het identificatienummer en, voor elke lidstaat van verbruik waar de BTW verschuldigd is, het totale bedrag, de BTW niet inbegrepen, van de gedurende het belastingtijdvak verrichte elektronische diensten en het totale bedrag van de belasting daarover. De geldende BTW-tarieven en de totale verschuldigde belasting moeten eveneens op de aangifte worden vermeld.

###### Artikel 366

1. De BTW-aangifte luidt in euro.

De lidstaten die de euro niet hebben aangenomen, kunnen eisen dat de BTW-aangifte in hun nationale munteenheid luidt. Indien de diensten in een andere munteenheid luiden, hanteert de niet in de Gemeenschap gevestigde belastingplichtige bij het invullen van de BTW-aangifte de wisselkoers die gold op de laatste dag van het belastingtijdvak.

###### Artikel 372

De lidstaten die op 1 januari 1978 bepalingen toepasten waarbij wordt afgeweken van het beginsel van onmiddellijke aftrek bedoeld in artikel 179, eerste alinea, mogen deze bepalingen blijven toepassen.

1. Finland mag de in bijlage X, deel A, punt 2, vermelde handelingen blijven belasten, zolang dezelfde handelingen worden belast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.

###### Artikel 373

2. Finland mag onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, de in bijlage X, deel B, punt 2, vermelde diensten verricht door auteurs, kunstenaars en vertolkers van kunstwerken, alsmede de in bijlage X, deel B, punten 5, 9 en 10, vermelde handelingen blijven vrijstellen, zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.

De lidstaten die op 1 januari 1978 bepalingen toepasten waarbij wordt afgeweken van artikel 28 en artikel 79, eerste alinea, punt c), mogen deze bepalingen blijven toepassen.

###### Artikel 374

In afwijking van de artikelen 169 en 309 mogen de lidstaten die op 1 januari 1978 vrijstelling zonder recht op aftrek van voorbelasting verleenden voor de diensten van reisbureaus bedoeld in artikel 309, deze vrijstelling handhaven. Deze afwijking is ook van toepassing op reisbureaus die in naam en voor rekening van de reiziger handelen.

Zweden mag onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, de in bijlage X, deel B, punt 2, vermelde diensten verricht door auteurs, kunstenaars en vertolkers van kunstwerken, alsmede de in bijlage X, deel B, punten 1, 9 en 10, vermelde handelingen blijven vrijstellen, zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.

## Afwijkingen voor de st aten die na 1 januar i 1978 tot de Gemeenschap zijn toegetreden

###### Artikel 375

Griekenland mag de in bijlage X, deel B, punten 2, 8, 9, 11 en 12, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1987 bestonden.

Tsjechië mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Artikel 376

Spanje mag de in bijlage X, deel B, punt 2, vermelde diensten van auteurs, alsmede de in bijlage X, deel B, punten 11 en 12, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1993 bestonden.

###### Artikel 377

Portugal mag de in bijlage X, deel B, punten 2, 4, 7, 9, 10 en 13, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1989 bestonden.

Estland mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Artikel 378

1. Oostenrijk mag de in bijlage X, deel A, punt 2, vermelde handelingen blijven belasten.

2. Zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren, mag Oostenrijk onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor de volgende handelingen:

Cyprus mag, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, vrijstelling blijven verlenen voor de volgende handelingen:

a) de in bijlage X, deel B, punten 5 en 9, vermelde handelingen;

a) leveringen van bouwterreinen omschreven in bijlage X, deel B, punt 9, tot en met 31 december 2007;

###### Artikel 384

Zolang dezelfde vrijstellingen worden verleend in een van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, mag Letland, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen:

a) voor diensten die worden verricht door auteurs, kunste- naars en vertolkers van kunstwerken omschreven in bijlage X, deel B, punt 2;

b) voor internationaal personenvervoer omschreven in bij- lage X, deel B, punt 10.

###### Artikel 385

Litouwen mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Artikel 386

Hongarije mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Artikel 387

Zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, mag Malta onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden de volgende handelingen blijven vrijstellen:

a) zonder recht op aftrek van voorbelasting, waterdistributie door publiekrechtelijke diensten omschreven in bijlage X, deel B, punt 8;

b) zonder recht op aftrek van voorbelasting, leveringen van gebouwen en bouwterreinen omschreven in bijlage X, deel B, punt 9;

c) met recht op aftrek van de voorbelasting, binnenlands personenvervoer, internationaal personenvervoer en perso- nenvervoer tussen de eilanden over zee, omschreven in bijlage X, deel B, punt 10.

###### Artikel 388

Polen mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Artikel 389

hebben gesteld en onder voorbehoud dat de vereenvoudigings- maatregelen voldoen aan de in artikel 395, lid 1, tweede alinea, omschreven voorwaarde.

###### Artikel 395

1. De Raad kan op voorstel van de Commissie met eenparig- heid van stemmen elke lidstaat machtigen bijzondere, van de bepalingen van deze richtlijn afwijkende maatregelen te treffen, teneinde de belastinginning te vereenvoudigen of bepaalde vormen van belastingfraude of -ontwijking te voorkomen.

De maatregelen tot vereenvoudiging van de belastinginning mogen geen noemenswaardige invloed hebben op de totale belastingopbrengst van de lidstaat in het stadium van het eindverbruik.

2. De lidstaat die de in lid 1 bedoelde maatregelen wil treffen, dient een verzoek in bij de Commissie en verschaft haar alle nodige gegevens. Wanneer de Commissie meent niet over alle nodige gegevens te beschikken, neemt zij binnen twee maanden na ontvangst van het verzoek contact op met de betrokken lidstaat en deelt zij hem mede welke aanvullende gegevens vereist zijn.

Zodra de Commissie over alle gegevens beschikt die zij nodig acht voor de beoordeling van het verzoek, stelt zij de verzoekende lidstaat binnen een maand daarvan in kennis en zendt zij het verzoek in de oorspronkelijke taal aan de andere lidstaten toe.

3. Binnen drie maanden na toezending van de in lid 2, tweede alinea, bedoelde gegevens legt de Commissie de Raad hetzij een passend voorstel voor, hetzij, wanneer zij bezwaren heeft tegen het verzoek om een afwijking, een mededeling waarin zij deze bezwaren toelicht.

4. De in de leden 2 en 3 vastgestelde procedure moet in ieder geval worden voltooid binnen acht maanden na ontvangst van het verzoek door de Commissie.

## Inter nationale overeenkoms ten

###### Artikel 396

1. De Raad kan op voorstel van de Commissie met eenparig- heid van stemmen elke lidstaat machtigen met een derde land of een internationale organisatie een overeenkomst te sluiten waarin bepalingen kunnen voorkomen die van deze richtlijn afwijken.

2. De lidstaat die een overeenkomst als bedoeld in lid 1 wil sluiten, dient een verzoek in bij de Commissie en verschaft haar alle nodige gegevens. Wanneer de Commissie meent niet over alle nodige gegevens te beschikken, neemt zij binnen twee maanden na ontvangst van het verzoek contact op met de betrokken lidstaat en deelt zij hem mede welke aanvullende gegevens vereist zijn.

###### Artikel 400

Bij de omrekening van de in artikel 399 bedoelde bedragen in de nationale munteenheid mogen de lidstaten de uit die omrekening voortvloeiende bedragen met maximaal 10 % naar boven of beneden afronden.

## Andere belastingen, rechten en heffingen

###### Artikel 401

Onverminderd andere communautaire bepalingen vormen de bepalingen van deze richtlijn geen beletsel voor de handhaving of invoering door een lidstaat van belastingen op verzekerings- overeenkomsten en op spelen en weddenschappen, alsmede van accijnzen, registratierechten en, meer in het algemeen, van alle belastingen, rechten en heffingen die niet het karakter van een omzetbelasting bezitten, mits de heffing van deze belastingen, rechten en heffingen in het verkeer tussen de lidstaten geen aanleiding geeft tot formaliteiten in verband met grensoverschrij- ding.

## SLOTBEPALINGEN

## Overgangsregeling voor de belastingheffing in het handelsverkeer tussen de lidstaten

###### Artikel 402

1. De in deze richtlijn vastgestelde regeling voor de belasting- heffing in het handelsverkeer tussen de lidstaten is een overgangsregeling en zal worden vervangen door een definitieve regeling, in beginsel gebaseerd op belastingheffing in de lidstaat van oorsprong van de goederenleveringen en de diensten.

2. Na het in artikel 404 bedoelde verslag te hebben bestudeerd en te hebben vastgesteld dat de voorwaarden voor de overgang naar de definitieve regeling vervuld zijn, stelt de Raad, overeenkomstig de procedure van artikel 93 van het Verdrag, de bepalingen vast die noodzakelijk zijn voor de inwerkingtre- ding en de werking van de definitieve regeling.

###### Artikel 403

De Raad stelt overeenkomstig artikel 93 van het Verdrag passende richtlijnen vast met het oog op de aanvulling van het gemeenschappelijke BTW-stelsel en met name de geleidelijke beperking of intrekking van de afwijkingen van dit stelsel.

###### Artikel 404

onder de in artikel 406 vermelde voorwaarden werd geplaatst;

b) elke onttrekking, met inbegrip van een onregelmatige onttrekking, van een goed aan een in artikel 156 bedoelde regeling of situatie of een daarmee vergelijkbare regeling waaronder het goed vóór de datum van toetreding onder de in artikel 406 vermelde voorwaarden werd geplaatst;

c) het einde van een van de in artikel 407 bedoelde regelingen waarmee vóór de datum van toetreding op het grondgebied van een van de nieuwe lidstaten een aanvang werd gemaakt ten behoeve van een vóór die datum onder bezwarende titel verrichte levering binnen het grondgebied van een lidstaat door een als zodanig handelende belastingplichtige;

d) elke onregelmatigheid of overtreding die werd begaan tijdens een regeling voor douanevervoer waarmee een aanvang werd gemaakt onder de in punt c) bedoelde voorwaarden.

2. Naast het in lid 1 bedoelde geval wordt eveneens met de invoer van een goed gelijkgesteld, het gebruik, na de datum van toetreding, binnen het grondgebied van een lidstaat door een belastingplichtige of een niet-belastingplichtige, van goederen die vóór de datum van toetreding binnen het grondgebied van de Gemeenschap of een van de nieuwe lidstaten aan hem zijn geleverd, wanneer de volgende voorwaarden vervuld zijn:

a) de levering van deze goederen is of kon worden vrijgesteld uit hoofde van artikel 146, lid 1, punten a) en b), of uit hoofde van een vergelijkbare bepaling in een van de nieuwe lidstaten;

b) de goederen zijn vóór de datum van toetreding niet ingevoerd in een van de nieuwe lidstaten of in de Gemeenschap.

###### Artikel 409

In de gevallen bedoeld in artikel 408, lid 1, wordt de invoer in de zin van artikel 61 geacht te hebben plaatsgevonden in de lidstaat binnen het grondgebied waarvan het goed wordt onttrokken aan de regeling waaronder het vóór de datum van toetreding werd geplaatst.

###### Artikel 410

1. In afwijking van artikel 71 vindt de invoer van een goed in de zin van artikel 408 plaats zonder dat een belastbaar feit plaatsvindt wanneer één van de volgende voorwaarden vervuld is:

a) het ingevoerde goed wordt verzonden of vervoerd naar een plaats buiten de uitgebreide Gemeenschap;

b) het in de zin van artikel 408, lid 1, punt a), ingevoerde goed is geen vervoermiddel en wordt herverzonden of vervoerd naar de lidstaat waaruit het werd uitgevoerd en naar degene die het heeft uitgevoerd;

c) het in de zin van artikel 408, lid 1, punt a), ingevoerde goed is een vervoermiddel dat vóór de datum van toetreding

## Bijlage I

LIJST VAN WERKZAAMHEDEN BEDOELD IN ARTIKEL 14, LID 1, DERDE ALINEA

1) Telecommunicatiediensten;

2) levering van water, gas, elektriciteit en stoom;

3) goederenvervoer;

4) haven- en luchthavendiensten;

5) personenvervoer;

6) levering van nieuwe goederen geproduceerd voor de verkoop;

7) handelingen van de landbouwinterventiebureaus met betrekking tot landbouwproducten, die worden verricht op grond van verordeningen houdende een gemeenschappelijke marktordening voor deze producten;

8) exploitatie van commerciële beurzen en tentoonstellingen;

9) opslag van goederen;

10) werkzaamheden van commerciële reclamebureaus;

11) werkzaamheden van reisbureaus;

12) exploitatie van bedrijfskantines, bedrijfswinkels, coöperaties en soortgelijke inrichtingen;

13) werkzaamheden van radio- en televisiediensten voor zover deze niet uit hoofde van artikel 132, lid 1, onder q), zijn vrijgesteld.

## Bijlage II

INDICATIEVE LIJST VAN LANGS ELEKTRONISCHE WEG VERRICHTE DIENSTEN BEDOELD IN ARTIKEL 56, LID 1, PUNT K)

1) Het leveren en onderbrengen van websites, het onderhoud op afstand van programma's en uitrustingen;

2) de levering van software en de bijwerking ervan;

3) de levering van beelden, geschreven stukken en informatie en de terbeschikkingstelling van databanken;

4) de levering van muziek of films, van spelen, met inbegrip van kans- of gokspelen, en van uitzendingen of manifestaties op het gebied van politiek, cultuur, kunst, sport, wetenschappen of ontspanning;

5) de levering van onderwijs op afstand.

## Bijlage III

LIJST VAN DE GOEDERENLEVERINGEN EN DE DIENSTEN WAAROP DE IN ARTIKEL 98 BEDOELDE VERLAAGDE TARIEVEN MOGEN WORDEN TOEGEPAST

1) Levensmiddelen (met inbegrip van dranken, maar met uitsluiting van alcoholhoudende dranken) voor menselijke en dierlijke consumptie, levende dieren, zaaigoed, planten en ingrediënten die gewoonlijk bestemd zijn voor gebruik bij de bereiding van levensmiddelen, alsmede producten die gewoonlijk bestemd zijn ter aanvulling of vervanging van levensmiddelen;

2) waterdistributie;

3) farmaceutische producten van een soort die gewoonlijk gebruikt wordt voor de gezondheidszorg, het voorkomen van ziekten of voor medische en veterinaire behandelingen, met inbegrip van voorbehoedsmiddelen en producten bestemd voor de hygiënische bescherming van de vrouw;

4) medische uitrusting, hieronder begrepen in huur, hulpmiddelen en andere apparaten die gewoonlijk bestemd zijn voor verlichting of behandeling van handicaps, voor uitsluitend persoonlijk gebruik door gehandicapten, met inbegrip van de herstelling daarvan, en levering van kinderzitjes voor motorvoertuigen;

5) vervoer van personen en de bagage die zij bij zich hebben;

6) levering van boeken ook bij uitlening door bibliotheken (met inbegrip van brochures, folders en soortgelijk drukwerk, albums platen-, teken- en kleurboeken voor kinderen, gedrukte of geschreven muziekpartituren, landkaarten en hydrografische en soortgelijke kaarten), kranten en tijdschriften, voor zover niet uitsluitend of hoofdzakelijk reclamemateriaal;

7) het verlenen van toegang tot shows, schouwburgen, circussen, kermissen, amusementsparken, concerten, musea, dierentuinen, bioscopen, tentoonstellingen en soortgelijke culturele evenementen en voorzieningen;

8) de ontvangst van radio- en televisie-uitzendingen;

9) diensten door en auteursrechten voor schrijvers, componisten en uitvoerende kunstenaars;

10) levering, bouw, renovatie en verbouwing van in het kader van het sociaal beleid verstrekte huisvesting;

11) levering van goederen en diensten die normaal bestemd zijn voor gebruik in de landbouw, met uitzondering evenwel van kapitaalgoederen, zoals machines of gebouwen;

12) door hotels en dergelijke inrichtingen verstrekte accommodatie, met inbegrip van het verstrekken van vakantie- accommodatie en de verhuur van percelen op kampeerterreinen en in caravanparken;

13) het verlenen van toegang tot sportevenementen;

14) het recht gebruik te maken van sportaccommodaties;

15) levering van goederen en diensten door organisaties die door de lidstaten als liefdadige instellingen zijn erkend en die betrokken zijn bij activiteiten op het gebied van bijstand en sociale zekerheid, voor zover deze handelingen niet krachtens de artikelen 132, 135 en 136 vrijgesteld zijn;

16) diensten verricht door lijkbezorgers en crematoria, alsmede de daarmee verband houdende levering van goederen;

17) de verstrekking van medische en tandheelkundige verzorging, alsmede thermale behandeling, voor zover deze niet krachtens artikel 132, lid 1, punten b) tot en met e), vrijgesteld zijn;

18) diensten in verband met de reiniging van de openbare weg, het ophalen van huisvuil en de afvalverwerking, andere dan de diensten die door de in artikel 13 bedoelde lichamen worden verstrekt.

## Bijlage IV

LIJST VAN DE IN ARTIKEL 106 BEDOELDE DIENSTEN

1) Kleine hersteldiensten:

a) fietsen;

b) schoeisel en lederwaren;

c) kleding en huishoudlinnen (ook herstellen en vermaken);

2) renovatie en herstel van particuliere woningen, met uitzondering van materialen die een beduidend deel vertegenwoordigen van de waarde van de verstrekte diensten;

3) glazenwassen en schoonmaken van particuliere woningen;

4) thuiszorg zoals hulp in de huishouding en zorg voor kinderen, ouderen, zieken of gehandicapten;

5) kappersdiensten.

## Bijlage V

CATEGORIEËN GOEDEREN DIE VOLGENS ARTIKEL 160, LID 2, ONDER EEN ANDER STELSEL VAN ENTREPOTS DAN DOUANE-ENTREPOTS KUNNEN VALLEN

GN – code Omschrijving

1) 0701 Aardappelen

2) 0711 20 Olijven

3) 0801 Kokosnoten, paranoten en cashewnoten

4) 0802 Andere noten

5) 0901 11 00 Koffie, ongebrand

0901 12 00

6) 0902 Thee

7) 1001 t/m 1005 Granen

1007 t/m 1008

8) 1006 Padie

9) 1201 t/m 1207 Zaden, oliehoudende vruchten en zaaigoed (sojabonen daaronder begrepen)

10) 1507 t/m 1515 Plantaardige vetten en oliën, alsmede fracties daarvan, ook indien geraffineerd, doch niet chemisch gewijzigd

11) 1701 11 Ruwe suiker

1701 12

12) 1801 Cacaobonen, ook indien gebroken, al dan niet gebrand

13) 2709 Minerale oliën (met inbegrip van propaan en butaan en ruwe olie uit aardolie)

2711 12

2711 13

14) hoofdstukken 28 en 29 Chemische producten (in bulk)

15) 4001 Rubber, in primaire vormen of in platen, vellen of strippen

16) 5101 Wol

17) 7106 Zilver

18) 7110 11 00 Platina (palladium, rhodium)

7110 21 00

7110 31 00

19) 7402 Koper

20) 7502 Nikkel

GN – code Omschrijving

22) 7801 Lood

23) 7901 Zink

24) 8001 Tin

25) ex 8112 92 Indium

ex 8112 99

## Bijlage VI

LIJST VAN GOEDERENLEVERINGEN EN DIENSTEN ALS BEDOELD IN PUNT D) VAN ARTIKEL 199, LID 1

1) De levering van resten en afval van ferro- en non-ferroproducten en oude materialen, halffabrikaten daaronder begrepen, die het resultaat zijn van het verwerken, vervaardigen of smelten van ferro- en non-ferrometalen of legeringen daarvan;

2) de levering van ferro- en non-ferrohalffabrikaten en bepaalde daarmee samenhangende verwerkingsdiensten;

3) de levering van residuen en andere materialen voor hergebruik bestaande uit ferro- en non-ferrometalen, legeringen daarvan, slakken, assen, bladders en industriële residuen die metalen of legeringen daarvan bevatten, alsmede de diensten bestaande in het scheiden, snijden, fragmenteren en samenpersen van deze producten;

4) de levering van en bepaalde verwerkingsdiensten met betrekking tot afval van ferro- en non-ferroproducten alsmede snippers, schroot, resten en afval, en oud materiaal en materiaal voor hergebruik bestaande uit glasscherven en glas, papier en karton, lompen, beenderen, leder, kunstleder, perkament, huiden en vellen, pezen en zenen, bindgaren, touw en kabel, rubber en kunststof;

5) de levering van de in deze bijlage genoemde materialen na bewerking in de vorm van reinigen, polijsten, scheiden, snijden, fragmenteren, samenpersen of gieten tot ingots;

6) de levering van resten en afval dat ontstaat bij de bewerking van grondstoffen.

## Bijlage VII

LIJST VAN LANDBOUWPRODUCTIEWERKZAAMHEDEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 4)

1) Landbouw:

a) algemene landbouw met inbegrip van wijnbouw;

b) vruchtboomteelt (olijvencultuur daaronder begrepen) en tuinbouw (groenten, bloemen en sierplanten), ook in kassen;

c) kwekerijen van paddestoelen, specerijen en kruiden; teelt van zaad- en pootgoed;

d) boomkwekerijen;

2) fokken en houden van dieren samenhangend met de exploitatie van de bodem:

a) fokken en houden van dieren;

b) pluimveebedrijf;

c) konijnenteelt;

d) imkerij;

e) zijderupsenteelt;

f) slakkenteelt;

3) bosbouw;

4) visserij:

a) zoetwatervisserij;

b) visteelt;

c) teelt van mosselen, oesters en andere week- en schaaldieren;

d) kikvorsenteelt.

## Bijlage VIII

INDICATIEVE LIJST VAN AGRARISCHE DIENSTEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 5)

1) Bewerking van de grond, maaien, dorsen, persen, verzamelen en oogsten, inclusief het inzaaien en poten;

2) verpakken en marktklaar maken, zoals drogen, schonen, kneuzen, desinfecteren en ensileren van landbouwproducten;

3) opslag van landbouwproducten;

4) inscharen, fokken, houden of mesten van dieren;

5) verhuur, voor landbouwdoeleinden, van middelen die normaal in de landbouw-, bosbouw- of visserijbedrijven worden gebruikt;

6) technische bijstand;

7) vernietiging van schadelijke planten en dieren, behandelen van planten en grond door bespuiting;

8) exploitatie van irrigatie- en draineerinstallaties;

9) snoeien van bomen, kappen van hout en andere diensten in de bosbouw.

## Bijlage IX

KUNSTVOORWERPEN, VOORWERPEN VOOR VERZAMELINGEN EN ANTIQUITEITEN BEDOELD IN ARTIKEL 311, LID 1, PUNTEN 2), 3) EN 4)

## DEEL A

Kunstvoorwerpen

1) Schilderijen, collages en dergelijke decoratieve platen, schilderingen en tekeningen geheel van de hand van de kunstenaar, met uitzondering van bouwtekeningen en andere tekeningen voor industriële, commerciële, topografische en dergelijke doeleinden en van met de hand versierde voorwerpen alsmede van beschilderd doek voor theatercoulissen, voor achtergronden van studio's of voor dergelijk gebruik (GN-code 9701);

2) originele gravures, originele etsen en originele litho's, dat wil zeggen een of meer door de kunstenaar geheel met de hand vervaardigde platen die in een beperkte oplage rechtstreeks in het zwart of in kleuren zijn afgedrukt, ongeacht het materiaal waarop dit afdrukken is geschied en ongeacht de gevolgde techniek, met uitzondering van de mechanische en van de fotomechanische reproductietechniek (GN-code 9702 00 00);

3) originele standbeelden en origineel beeldhouwwerk, ongeacht het materiaal waarvan zij vervaardigd zijn, mits het werk geheel van de hand van de kunstenaar is; afgietsels van beeldhouwwerken in een oplage van maximaal acht exemplaren, die door de kunstenaar of diens rechthebbenden wordt gecontroleerd (GN-code 9703 00 00); bij wijze van uitzondering mag, in door de lidstaten bepaalde gevallen, met betrekking tot vóór 1 januari 1989 gemaakte afgietsels van beeldhouwwerken, het maximum van acht exemplaren worden overschreden;

4) tapisserieën (GN-code 5805 00 00) en wandtextiel (GN-code 6304 00 00), met de hand vervaardigd volgens originele ontwerpen van kunstenaars, mits er niet meer dan acht exemplaren van elk zijn;

5) unieke voorwerpen van keramiek, geheel van de hand van de kunstenaar en door hem gesigneerd;

6) emailwerk op koper, geheel met de hand vervaardigd tot maximaal acht genummerde en door de kunstenaar of het atelier gesigneerde exemplaren, met uitsluiting van sieraden, juwelen en edelsmeedwerk;

7) foto's die genomen zijn door de kunstenaar, door hem of onder zijn toezicht zijn afgedrukt, gesigneerd en genummerd, met een oplage van maximaal 30 exemplaren voor alle formaten en dragers samen.

Voorwerpen voor verzamelingen

1) Postzegels, fiscale zegels, gefrankeerde enveloppen en postkaarten, eerstedagsenveloppen en dergelijke, gestempeld of, indien ongestempeld, voor zover zij niet geldig zijn of niet geldig zullen worden (GN-code 9704 00 00);

2) verzamelingen en voorwerpen voor verzamelingen, met een zoölogisch, botanisch, mineralogisch, anatomisch, historisch, archeologisch, paleontologisch, etnografisch of numismatisch belang (GN-code 9705 00 00).

Antiquiteiten

Andere voorwerpen dan kunstvoorwerpen en voorwerpen voor verzamelingen, ouder dan 100 jaar (GN-code 9706 00 00).

## Bijlage X

LIJST VAN HANDELINGEN WAARVOOR DE IN DE ARTIKELEN 370 EN 371 EN DE ARTIKELEN 375 TOT EN MET 390 BEDOELDE AFWIJKINGEN GELDEN

## DEEL A

Handelingen die de lidstaten mogen blijven belasten

1) De door tandtechnici in het kader van de uitoefening van hun beroep verrichte diensten, alsmede het verschaffen van tandprothesen door tandartsen en tandtechnici;

2) niet – commerciële activiteiten van openbare radio- en televisieorganisaties;

3) leveringen van een gebouw, een gedeelte van een gebouw en het bijbehorende terrein, andere dan die bedoeld in artikel 12, lid 1, punt a), wanneer zij worden verricht door belastingplichtigen die recht hebben op aftrek van voorbelasting voor het betrokken gebouw;

4) diensten van reisbureaus bedoeld in artikel 306 alsmede van reisbureaus die in naam en voor rekening van de reiziger handelen, voor reizen buiten de Gemeenschap.

## DEEL B

Handelingen die de lidstaten mogen blijven vrijstellen

1) Het verlenen van toegang tot sportmanifestaties;

2) diensten van auteurs, kunstenaars, vertolkers van kunstwerken, advocaten en andere beoefenaren van vrije beroepen, andere dan de medische en paramedische beroepen, met uitzondering van volgende diensten:

a) de overdracht van octrooien, fabrieks- en handelsmerken en van soortgelijke rechten, alsmede het verlenen van licenties inzake deze rechten;

b) andere werkzaamheden dan de oplevering van een werk in roerende staat, betrekking hebbende op roerende lichamelijke zaken en verricht voor belastingplichtigen;

c) diensten die erop gericht zijn de uitvoering van bouwwerken voor te bereiden of te coördineren, zoals bijvoorbeeld de diensten verricht door architecten en bureaus die op de uitvoering van het werk toezicht houden;

d) diensten op het gebied van de commerciële reclame;

e) het vervoer en de opslag van goederen, alsmede daarmee samenhangende diensten;

f) de verhuur van roerende lichamelijke zaken aan belastingplichtigen;

g) het terbeschikkingstellen van personeel aan belastingplichtigen;

h) op technisch, economisch of wetenschappelijk gebied: de diensten verricht door raadgevende personen, ingenieurs en planningbureaus, alsmede soortgelijke diensten;

i) de nakoming van een verbintenis, bestaande uit het geheel of gedeeltelijk niet-uitoefenen van een beroepsactiviteit of van een in de punten a) tot en met h) en j) bedoeld recht;

j) de diensten van expediteurs, makelaars, handelsagenten en andere zelfstandige tussenpersonen, voor zover zij betrekking hebben op de levering of de invoer van goederen of de in de punten a) tot en met i) bedoelde diensten;

3) telecommunicatiediensten en daarmee rechtstreeks verband houdende leveringen van goederen door de openbare postdiensten;

5) handelingen verricht door blinden en/of blindenwerkplaatsen, mits door vrijstelling hiervan geen belangrijke verstoring van de mededinging ontstaat;

6) goederenleveringen en diensten verricht voor instellingen die zijn belast met het aanleggen, het inrichten en het onderhouden van begraaf- en grafplaatsen en gedenktekens voor oorlogsslachtoffers;

7) handelingen van ziekenhuizen die niet onder artikel 132, lid 1, punt b), vallen;

8) waterdistributie door publiekrechtelijke diensten;

9) leveringen van gebouwen of gedeelten van gebouwen en het bijbehorende terrein vóór de eerste ingebruikneming alsook leveringen van bouwterreinen als bedoeld in artikel 12;

10) personenvervoer en vervoer van goederen, zoals bagage en personenauto's die door reizigers worden meegevoerd, of diensten die samenhangen met het vervoer van personen, voor zover het vervoer van deze personen vrijgesteld is;

11) levering, verbouwing, reparatie, onderhoud, bevrachting en verhuur van luchtvaartuigen die worden gebruikt door staatsinstellingen (inclusief voorwerpen die met deze luchtvaartuigen vast verbonden zijn of voor hun exploitatie dienen);

12) levering, verbouwing, reparatie, onderhoud, bevrachting en verhuur van oorlogsschepen;

13) diensten van reisbureaus als bedoeld in artikel 306 alsmede van reisbureaus die in naam en voor rekening van de reiziger handelen, voor reizen binnen de Gemeenschap.

## Bijlage XI

## DEEL A

Ingetrokken richtlijnen met de achtereenvolgende wijzigingen ervan

1) Richtlijn 67/227/EEG (PB 71 van 14.4.1967, blz. 1301)

Richtlijn 77/388/EEG

2) Richtlijn 77/388/EEG (PB L 145 van 13.6.1977, blz. 1)

Richtlijn 78/583/EEG (PB L 194 van 19.7.1978, blz. 16)

Richtlijn 80/368/EEG (PB L 90 van 3.4.1980, blz. 41)

Richtlijn 84/386/EEG (PB L 208 van 3.8.1984, blz. 58)

Richtlijn 89/465/EEG (PB L 226 van 3.8.1989, blz. 21)

Richtlijn 91/680/EEG (PB L 376 van 31.12.1991, blz. 1) — (met uitzondering van artikel 2)

Richtlijn 92/77/EEG (PB L 316 van 31.10.1992, blz. 1)

Richtlijn 92/111/EEG (PB L 384 van 30.12.1992, blz. 47)

Richtlijn 94/4/EG (PB L 60 van 3.3.1994, blz. 14) — (enkel artikel 2)

Richtlijn 94/5/EG (PB L 60 van 3.3.1994, blz. 16)

Richtlijn 94/76/EG (PB L 365 van 31.12.1994, blz. 53)

Richtlijn 95/7/EG (PB L 102 van 5.5.1995, blz. 18)

Richtlijn 96/42/EG (PB L 170 van 9.7.1996, blz. 34)

Richtlijn 96/95/EG (PB L 338 van 28.12.1996, blz. 89)

Richtlijn 98/80/EG (PB L 281 van 17.10.1998, blz. 31)

Richtlijn 1999/49/EG (PB L 139 van 2.6.1999, blz. 27)

Richtlijn 1999/59/EG (PB L 162 van 26.6.1999, blz. 63)

Richtlijn 1999/85/EG (PB L 277 van 28.10.1999, blz. 34)

Richtlijn 2000/17/EG (PB L 84 van 5.4.2000, blz. 24)

Richtlijn 2000/65/EG (PB L 269 van 21.10.2000, blz. 44)

Richtlijn 2001/4/EG (PB L 22 van 24.1.2001, blz. 17)

Richtlijn 2001/115/EG (PB L 15 van 17.1.2001, blz. 24)

Richtlijn 2002/38/EG (PB L 128 van 15.5.2002, blz. 41)

Richtlijn 2002/93/EG (PB L 331 van 7.12.2002, blz. 27)

Richtlijn 2004/7/EG (PB L 27 van 30.1.2004, blz. 44)

Richtlijn 2004/15/EG (PB L 52 van 21.2.2004, blz. 61)

Richtlijn 2004/66/EG (PB L 168 van 1.5.2004, blz. 35) — (enkel punt V van de bijlage)

Richtlijn 2005/92/EG (PB L 345 van 28.12.2005, blz. 19)

Richtlijn 2006/18/EG (PB L 51 van 22.2.2006, blz. 12)

Richtlijn 2006/58/EG (PB L 174 van 28.6.2006, blz. 5)

Richtlijn 2006/69/EG (PB L 221 van 12.8.2006, blz. 9) — (enkel artikel 1)

Termijnen voor de omzetting in nationaal recht

(bedoeld in artikel 411)

Richtlijn Omzettingstermijn

Richtlijn Omzettingstermijn

Richtlijn 2006/18/EG — Richtlijn 2006/58/EG 1 juli 2006 Richtlijn 2006/69/EG 1 januari 2008

## Bijlage XII

CONCORDANTIETABEL

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 1, eerste alinea Artikel 1, lid 1

Artikel 1, tweede en derde alinea —

Artikel 2, eerste, tweede en derde alinea Artikel 1, lid 2, eerste, tweede en derde alinea

Artikelen 3, 4 en 6 —

Artikel 1 —

Artikel 2, onder 1) Artikel 2, lid 1, onder a) en c)

Artikel 2, onder 2) Artikel 2, lid 1, onder d)

Artikel 3, lid 1, eerste streepje Artikel 5, onder 2)

Artikel 3, lid 1, tweede streepje Artikel 5, onder 1)

Artikel 3, lid 1, derde streepje Artikel 5, onder 3) en 4)

Artikel 3, lid 2 —

Artikel 3, lid 3, eerste alinea, eerste streepje Artikel 6, lid 2, onder a) en b)

Artikel 3, lid 3, eerste alinea, tweede streepje Artikel 6, lid 2, onder c) en d)

Artikel 3, lid 3, eerste alinea, derde streepje Artikel 6, lid 2, onder e), f) en g)

Artikel 3, lid 3, tweede alinea, eerste streepje Artikel 6, lid 1, onder b)

Artikel 3, lid 3, tweede alinea, tweede streepje Artikel 6, lid 1, onder c)

Artikel 3, lid 3, tweede alinea, derde streepje Artikel 6, lid 1, onder a)

Artikel 3, lid 4, eerste alinea, eerste en tweede streepje Artikel 7, lid 1

Artikel 3, lid 5 Artikel 8

Artikel 4, leden 1 en 2 Artikel 9, lid 1, eerste en tweede alinea

Artikel 4, lid 3, onder a), eerste alinea, eerste volzin Artikel 12, lid 1, onder a)

Artikel 4, lid 3, onder a), eerste alinea, tweede volzin Artikel 12, lid 2, tweede alinea

Artikel 4, lid 3, onder a), tweede alinea Artikel 12, lid 2, derde alinea

Artikel 4, lid 3, onder a), derde alinea Artikel 12, lid 2, eerste alinea

Artikel 4, lid 3, onder b), eerste alinea Artikel 12, lid 1, onder b)

Artikel 4, lid 3, onder b), tweede alinea Artikel 12, lid 3

Artikel 4, lid 4, eerste alinea Artikel 10

Artikel 4, lid 4, tweede en derde alinea Artikel 11, eerste en tweede alinea

Artikel 4, lid 5, eerste, tweede en derde alinea Artikel 13, lid 1, eerste, tweede en derde alinea

Artikel 4, lid 5, vierde alinea Artikel 13, lid 2

Artikel 5, lid 1 Artikel 14, lid 1

Artikel 5, lid 2 Artikel 15, lid 1

Artikel 5, lid 3, onder a), b) en c) Artikel 15, lid 2, onder a), b) en c)

Artikel 5, lid 4, onder a), b) en c) Artikel 14, lid 2, onder a), b) en c)

Artikel 5, lid 5 Artikel 14, lid 3

Artikel 5, lid 6, eerste en tweede volzin Artikel 16, eerste en tweede alinea

Artikel 5, lid 7, onder a), b) en c) Artikel 18, onder a), b) en c)

Artikel 5, lid 8, eerste volzin Artikel 19, eerste alinea

Artikel 5, lid 8, tweede en derde volzin Artikel 19, tweede alinea

Artikel 6, lid 1, eerste alinea Artikel 24, lid 1

Artikel 6, lid 1, tweede alinea, eerste, tweede en derde streepje Artikel 25, onder a), b) en c)

Artikel 6, lid 2, eerste alinea, onder a) en b) Artikel 26, lid 1, onder a) en b)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 6, lid 2, tweede alinea Artikel 26, lid 2

Artikel 6, lid 3 Artikel 27

Artikel 6, lid 4 Artikel 28

Artikel 6, lid 5 Artikel 29

Artikel 7, lid 1, onder a) en b) Artikel 30, eerste en tweede alinea

Artikel 7, lid 2 Artikel 60

Artikel 7, lid 3, eerste en tweede alinea Artikel 61, eerste en tweede alinea

Artikel 8, lid 1, onder a), eerste volzin Artikel 32, eerste alinea

Artikel 8, lid 1, onder a), tweede en derde volzin Artikel 36, eerste en tweede alinea

Artikel 8, lid 1, onder b) Artikel 31

Artikel 8, lid 1, onder c), eerste alinea Artikel 37, lid 1

Artikel 8, lid 1, onder c), tweede alinea, eerste streepje Artikel 37, lid 2, eerste alinea

Artikel 8, lid 1, onder c), tweede alinea, tweede en derde streepje Artikel 37, lid 2, tweede en derde alinea

Artikel 8, lid 1, onder c), derde alinea Artikel 37, lid 2, vierde alinea

Artikel 8, lid 1, onder c), vierde alinea Artikel 37, lid 3, eerste alinea

Artikel 8, lid 1, onder c), vijfde alinea —

Artikel 8, lid 1, onder c), zesde alinea Artikel 37, lid 3, tweede alinea

Artikel 8, lid 1, onder d), eerste en tweede alinea Artikel 38, leden 1 en 2

Artikel 8, lid 1, onder e), eerste volzin Artikel 39, eerste alinea

Artikel 8, lid 1, onder e), tweede en derde volzin Artikel 39, tweede alinea

Artikel 8, lid 2 Artikel 32, tweede alinea

Artikel 9, lid 1 Artikel 43

Artikel 9, lid 2, inleidende zin —

Artikel 9, lid 2, onder b) Artikel 46

Artikel 9, lid 2, onder c), eerste en tweede streepje Artikel 52, onder a) en b)

Artikel 9, lid 2, onder c), derde en vierde streepje Artikel 52, onder c)

Artikel 9, lid 2, onder e), eerste tot en met zesde streepje Artikel 56, lid 1, onder a) tot en met f)

Artikel 9, lid 2, onder e), zevende streepje Artikel 56, lid 1, onder l)

Artikel 9, lid 2, onder e), achtste streepje Artikel 56, lid 1, onder g)

Artikel 9, lid 2, onder e), negende streepje Artikel 56, lid 1, onder h)

Artikel 9, lid 2, onder e), tiende streepje, eerste volzin Artikel 56, lid 1, onder i)

Artikel 9, lid 2, onder e), tiende streepje, tweede volzin Artikel 24, lid 2

Artikel 9, lid 2, onder e), tiende streepje, derde volzin Artikel 56, lid 1, onder i)

Artikel 9, lid 2, onder e), elfde en twaalfde streepje Artikel 56, lid 1, onder j) en k)

Artikel 9, lid 2, onder f) Artikel 57, lid 1

Artikel 9, lid 3 Artikel 58, eerste en tweede alinea

Artikel 9, lid 3, onder a) en b) Artikel 58, eerste alinea, onder a) en b)

Artikel 9, lid 4 Artikel 59, leden 1 en 2

Artikel 10, lid 1, onder a) en b) Artikel 62, onder 1) en 2)

Artikel 10, lid 2, eerste alinea, eerste volzin Artikel 63

Artikel 10, lid 2, eerste alinea, tweede en derde volzin Artikel 64, leden 1 en 2

Artikel 10, lid 2, tweede alinea Artikel 65

Artikel 10, lid 2, derde alinea, eerste, tweede en derde streepje Artikel 66, onder a), b) en c)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 10, lid 3, eerste alinea, eerste volzin Artikel 70

Artikel 10, lid 3, eerste alinea, tweede volzin Artikel 71, lid 1, eerste alinea

Artikel 10, lid 3, tweede alinea Artikel 71, lid 1, tweede alinea

Artikel 10, lid 3, derde alinea Artikel 71, lid 2

Artikel 11, A, lid 1, onder a) Artikel 73

Artikel 11, A, lid 1, onder b) Artikel 74

Artikel 11, A, lid 1, onder c) Artikel 75

Artikel 11, A, lid 1, onder d) Artikel 77

Artikel 11, A, lid 2, onder a) Artikel 78, eerste alinea, onder a)

Artikel 11, A, lid 2, onder b), eerste volzin Artikel 78, eerste alinea, onder b)

Artikel 11, A, lid 2, onder b), tweede volzin Artikel 78, tweede alinea

Artikel 11, A, lid 3, onder a) en b) Artikel 79, eerste alinea, onder a) en b) Artikel 87, onder a) en b)

Artikel 11, A, lid 3, onder c), eerste volzin Artikel 79, eerste alinea, onder c)

Artikel 11, A, lid 3, onder c), tweede volzin Artikel 79, tweede alinea

Artikel 11, A, lid 4, eerste en tweede alinea Artikel 81, eerste en tweede alinea

Artikel 11, A, lid 5 Artikel 82

Artikel 11, A, lid 6, eerste alinea, eerste en tweede volzin Artikel 80, lid 1, eerste alinea

Artikel 11, A, lid 6, eerste alinea, derde volzin Artikel 80, lid 1, tweede alinea

Artikel 11, A, lid 6, tweede alinea Artikel 80, lid 1, eerste alinea

Artikel 11, A, lid 6, derde alinea Artikel 80, lid 2

Artikel 11, A, lid 7, eerste en tweede alinea Artikel 72, eerste en tweede alinea

Artikel 11, B, lid 1 Artikel 85

Artikel 11, B, lid 3, onder a) Artikel 86, lid 1, onder a)

Artikel 11, B, lid 3, onder b), eerste alinea Artikel 86, lid 1, onder b)

Artikel 11, B, lid 3, onder b), tweede alinea Artikel 86, lid 2

Artikel 11, B, lid 3, onder b), derde alinea Artikel 86, lid 1, onder b)

Artikel 11, B, lid 4 Artikel 87

Artikel 11, B, lid 5 Artikel 88

Artikel 11, B, lid 6, eerste en tweede alinea Artikel 89, eerste en tweede alinea

Artikel 11, C, lid 1, eerste en tweede alinea Artikel 90, leden 1 en 2

Artikel 11, C, lid 2, eerste alinea Artikel 91, lid 1

Artikel 11, C, lid 2, tweede alinea, eerste en tweede volzin Artikel 91, lid 2, eerste en tweede alinea

Artikel 11, C, lid 3, eerste en tweede streepje Artikel 92, onder a) en b)

Artikel 12, lid 1 Artikel 93, eerste alinea

Artikel 12, lid 1, onder a) Artikel 93, tweede alinea, onder a)

Artikel 12, lid 1, onder b) Artikel 93, tweede alinea, onder c)

Artikel 12, lid 2, eerste en tweede streepje Artikel 95, eerste en tweede alinea

Artikel 12, lid 3, onder a), eerste alinea, eerste volzin Artikel 96

Artikel 12, lid 3, onder a), eerste alinea, tweede volzin Artikel 97, lid 1

Artikel 12, lid 3, onder a), tweede alinea Artikel 97, lid 2

Artikel 12, lid 3, onder a), derde alinea, eerste volzin Artikel 98, lid 1

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 12, lid 3, onder a), derde alinea, tweede volzin Artikel 98, lid 2, eerste alinea Artikel 99, lid 1

Artikel 12, lid 3, onder a), vierde alinea Artikel 98, lid 2, tweede alinea

Artikel 12, lid 3, onder b), eerste volzin Artikel 102 eerste alinea

Artikel 12, lid 3, onder b), tweede, derde en vierde volzin Artikel 102, tweede alinea

Artikel 12, lid 3, onder c), eerste alinea Artikel 103, lid 1

Artikel 12, lid 3, onder c), tweede alinea, eerste en tweede streepje Artikel 103 lid 2, onder a) en b)

Artikel 12, lid 4, eerste alinea Artikel 99, lid 2

Artikel 12, lid 4, tweede alinea, eerste en tweede volzin Artikel 100, eerste en tweede alinea

Artikel 12, lid 4, derde alinea Artikel 101

Artikel 12, lid 5 Artikel 94, lid 2

Artikel 12, lid 6 Artikel 105

Artikel 13, A, lid 1, inleidende zin Artikel 131

Artikel 13, A, lid 1, onder a) tot en met n) Artikel 132, lid 1, onder a) tot en met n)

Artikel 13, A, lid 1, onder o), eerste volzin Artikel 132, lid 1, onder o)

Artikel 13, A, lid 1, onder o), tweede volzin Artikel 132, lid 2

Artikel 13, A, lid 1, onder p) en q) Artikel 132, lid 1, onder p) en q)

Artikel 13, A, lid 2, onder a), eerste tot en met vierde streepje Artikel 133, eerste alinea, onder a) tot en met d)

Artikel 13, A, lid 2, onder b), eerste en tweede streepje Artikel 134, onder a) en b)

Artikel 13, B, inleidende zin Artikel 131

Artikel 13, B, onder a) Artikel 135, lid 1, onder a)

Artikel 13, B, onder b), eerste alinea, onder 1) tot en met 4) Artikel 135, lid 2, eerste alinea, onder a) tot en met d)

Artikel 13, B, onder b), tweede alinea Artikel 135, lid 2, tweede alinea

Artikel 13, B, onder c) Artikel 136, onder a) en b)

Artikel 13, B, onder d) —

Artikel 13, B, onder d), 1) tot en met 5) Artikel 135, lid 1, onder b) tot en met f)

Artikel 13, B, onder d), 1) tot en met 5), eerste en tweede streepje Artikel 135, lid 1, onder f)

Artikel 13, B, onder d), 6) Artikel 135, lid 1, onder g)

Artikel 13, B, onder e) tot en met h) Artikel 135, lid 1, onder h) tot en met k)

Artikel 13, C, eerste alinea, onder a) Artikel 137, lid 1, onder d)

Artikel 13, C, eerste alinea, onder b) Artikel 137, lid 1, onder a), b) en c)

Artikel 13, C, tweede alinea Artikel 137, lid 2, eerste en tweede alinea

Artikel 14, lid 1, inleidende zin Artikel 131

Artikel 14, lid 1, onder a) Artikel 140, onder a)

Artikel 14, lid 1, onder d), eerste en tweede alinea Artikel 143, onder b) en c)

Artikel 14, lid 1, onder e) Artikel 143, onder e)

Artikel 14, lid 1, onder g), eerste tot en met vierde streepje Artikel 143, onder f) tot en met i)

Artikel 14, lid 1, onder h) Artikel 143, onder j)

Artikel 14, lid 1, onder i) Artikel 144

Artikel 14, lid 1, onder j) Artikel 143, onder k)

Artikel 14, lid 1, onder k) Artikel 143, onder l)

Artikel 14, lid 2, eerste alinea Artikel 145, lid 1

Artikel 14, lid 2, tweede alinea, eerste, tweede en derde streepje Artikel 145, lid 2, eerste, tweede en derde alinea

Artikel 14, lid 2, derde alinea Artikel 145, lid 3

Artikel 15, inleidende zin Artikel 131

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 15, onder 1) Artikel 146, lid 1, onder a)

Artikel 15, onder 2), eerste alinea Artikel 146, lid 1, onder b)

Artikel 15, onder 2), tweede alinea, eerste en tweede streepje Artikel 147, lid 1, eerste alinea, onder a) en b)

Artikel 15, onder 2), tweede alinea, derde streepje, eerste deel van volzin Artikel 147, lid 1, eerste alinea, onder c)

Artikel 15, onder 2), tweede alinea, derde streepje, tweede deel van volzin Artikel 147, lid 1, tweede alinea

Artikel 15, onder 2), derde alinea, eerste en tweede streepje Artikel 147, lid 2, eerste en tweede alinea

Artikel 15, ondert 2), vierde alinea Artikel 147, lid 2, derde alinea

Artikel 15, onder 3) Artikel 146, lid 1, onder d)

Artikel 15, onder 4), eerste alinea, onder a) en b) Artikel 148, onder a)

Artikel 15, onder 4), eerste alinea, onder c) Artikel 148, onder b)

Artikel 15, onder 4), tweede alinea, eerste en tweede streepje Artikel 150, leden 1 en 2

Artikel 15, onder 5) Artikel 148, onder c)

Artikel 15, onder 6) Artikel 148, onder f)

Artikel 15, onder 7) Artikel 148, onder e)

Artikel 15, onder 8) Artikel 148, onder d)

Artikel 15, onder 9) Artikel 148, onder g)

Artikel 15, onder 10), eerste alinea, eerste tot en met vierde streepje Artikel 151, lid 1, eerste alinea, onder a) tot en met d)

Artikel 15, onder 10), tweede alinea Artikel 151, lid 1, tweede alinea

Artikel 15, onder 10), derde alinea Artikel 151, lid 2

Artikel 15, onder 11) Artikel 152

Artikel 15, onder 12), eerste volzin Artikel 146, lid 1, onder c)

Artikel 15, onder 13) Artikel 146, lid 1, onder e)

Artikel 15, onder 14), eerste en tweede alinea Artikel 153, eerste en tweede alinea

Artikel 15, onder 15) Artikel 149

Artikel 16, lid 1 —

Artikel 16, lid 2 Artikel 164, lid 1

Artikel 16, lid 3 Artikel 166

Artikel 17, lid 1 Artikel 167

Artikel 17, leden 2, 3 en 4 —

Artikel 17, lid 5, eerste en tweede alinea Artikel 173, lid 1, eerste en tweede alinea

Artikel 17, lid 5, derde alinea, onder a) tot en met e) Artikel 173, lid 2, onder a) tot en met e)

Artikel 17, lid 6 Artikel 176

Artikel 17, lid 7, eerste en tweede volzin Artikel 177, eerste en tweede alinea

Artikel 18, lid 1 —

Artikel 18, lid 2, eerste en tweede alinea Artikel 179, eerste en tweede alinea

Artikel 18, lid 3 Artikel 180

Artikel 18, lid 4, eerste en tweede alinea Artikel 183, eerste en tweede alinea

Artikel 19, lid 1, eerste alinea, eerste streepje Artikel 174, lid 1, eerste alinea, onder a)

Artikel 19, lid 1, eerste alinea, tweede streepje, eerste volzin Artikel 174, lid 1, eerste alinea, onder b)

Artikel 19, lid 1, eerste alinea, tweede streepje, tweede volzin Artikel 174, lid 1, tweede alinea

Artikel 19, lid 1, tweede alinea Artikel 175, lid 1

Artikel 19, lid 2, eerste volzin Artikel 174, lid 2, onder a)

Artikel 19, lid 2, tweede volzin Artikel 174, lid 2, onder a) en b)

Artikel 19, lid 2, derde volzin Artikel 174, lid 3

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 19, lid 3, eerste alinea, eerste en tweede volzin Artikel 175, lid 2, eerste alinea

Artikel 19, lid 3, eerste alinea, derde volzin Artikel 175, lid 2, tweede alinea

Artikel 19, lid 3, tweede alinea Artikel 175, lid 3

Artikel 20, lid 1, inleidende zin Artikel 186

Artikel 20, lid 1, onder a) Artikel 184

Artikel 20, lid 1, onder b), eerste deel van eerste volzin Artikel 185, lid 1

Artikel 20, lid 1, onder b), tweede deel van eerste volzin Artikel 185, lid 2, eerste alinea

Artikel 20, lid 1, onder b), tweede volzin Artikel 185, lid 2, tweede alinea

Artikel 20, lid 2, eerste alinea, eerste volzin Artikel 187, lid 1, eerste alinea

Artikel 20, lid 2, eerste alinea, tweede en derde volzin Artikel 187, lid 2, eerste en tweede alinea

Artikel 20, lid 2, tweede en derde alinea Artikel 187, lid 1, tweede en derde alinea

Artikel 20, lid 3, eerste alinea, eerste volzin Artikel 188, lid 1, eerste alinea

Artikel 20, lid 3, eerste alinea, tweede volzin Artikel 188, lid 1, tweede en derde alinea

Artikel 20, lid 3, eerste alinea, derde volzin Artikel 188, lid 2

Artikel 20, lid 3, tweede alinea Artikel 188, lid 2

Artikel 20, lid 4, eerste alinea, eerste tot en met vierde streepje Artikel 189, onder a) tot en met d)

Artikel 20, lid 4, tweede alinea Artikel 190

Artikel 20, lid 5 Artikel 191

Artikel 20, lid 6 Artikel 192

Artikel 21 —

Artikel 23, eerste alinea Artikel 211, eerste alinea Artikel 260

Artikel 23, tweede alinea Artikel 211, tweede alinea

Artikel 24, lid 1 Artikel 281

Artikel 24, lid 2, inleidende zin Artikel 292

Artikel 24, lid 2, onder a), eerste alinea Artikel 284, lid 1

Artikel 24, lid 2, onder a), tweede en derde alinea Artikel 284, lid 2, eerste en tweede alinea

Artikel 24, lid 2, onder b), eerste en tweede volzin Artikel 285, eerste en tweede alinea

Artikel 24, lid 2, onder c) Artikel 286

Artikel 24, lid 3, eerste alinea Artikel 282

Artikel 24, lid 3, tweede alinea, eerste volzin Artikel 283, lid 2

Artikel 24, lid 3, tweede alinea, tweede volzin Artikel 283, lid 1, onder a)

Artikel 24, lid 4, eerste alinea Artikel 288, eerste alinea, onder 1) tot en met 4)

Artikel 24, lid 4, tweede alinea Artikel 288, tweede alinea

Artikel 24, lid 5 Artikel 289

Artikel 24, lid 6 Artikel 290

Artikel 24, lid 7 Artikel 291

Artikel 24, lid 8, onder a), b) en c) Artikel 293, onder 1), 2) en 3)

Artikel 24, lid 9 Artikel 294

Art. 24. bis, eerste alinea, eerste tot en

met twaalfde streepje Artikel 287, onder 7) tot en met 16)

Artikel 25, lid 1 Artikel 296, lid 1

Artikel 25, lid 2, eerste tot en met achtste streepje Artikel 295, lid 1, onder 1) tot en met 8)

Artikel 25, lid 3, eerste alinea, eerste volzin Artikel 297, eerste alinea, eerste volzin, en tweede alinea

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 25, lid 3, eerste alinea, tweede volzin Artikel 298, eerste alinea

Artikel 25, lid 3, eerste alinea, derde volzin Artikel 299

Artikel 25, lid 3, eerste alinea, vierde en vijfde volzin Artikel 298, tweede alinea

Artikel 25, lid 3, tweede alinea Artikel 297, eerste alinea, tweede volzin

Artikel 25, lid 4, eerste alinea Artikel 272, lid 1, eerste alinea, onder e)

Artikel 25, leden 5 en 6 —

Artikel 25, lid 7 Artikel 304

Artikel 25, lid 8 Artikel 301, lid 2

Artikel 25, lid 9 Artikel 296, lid 2

Artikel 25, lid 10 Artikel 296, lid 3

Artikel 25, leden 11 en 12 —

Artikel 26, lid 1, eerste en tweede volzin Artikel 306, lid 1, eerste en tweede alinea

Artikel 26, lid 1, derde volzin Artikel 306, lid 2

Artikel 26, lid 2, eerste en tweede volzin Artikel 307, eerste en tweede alinea

Artikel 26, lid 2, derde volzin Artikel 308

Artikel 26, lid 3, eerste en tweede volzin Artikel 309, eerste en tweede alinea

Artikel 26, lid 4 Artikel 310

Art. 26. bis, A, onder a), eerste alinea

Artikel 311, lid 1, onder 2)

Art. 26. bis,   A,   onder   a),   tweede

alinea Artikel 311, lid 2

Art. 26. bis,   A,   onder   b)   en   c)

Artikel 311, lid 1, onder 3) en 4)

Art. 26. bis,   A,   onder   d)

Artikel 311, lid 1, onder 1)

Art. 26. bis,   A,   onder   e)   en   f)

Artikel 311, lid 1, onder 5) en 6)

Art. 26. bis,   A,   onder   g),   eerste   en

tweede streepje Artikel 311, lid 3

Art. 26. bis,   B,   lid   1

Artikel 313, lid 1

Art. 26. bis,   B,   lid   2

Art. 314

Art. 26. bis, B, lid 2, eerste en tweede

streepje Artikel 314, onder a) tot en met d)

Art. 26. bis,   B,   lid   3,   eerste   alinea,

eerste en tweede volzin Artikel 315, eerste en tweede alinea

Art. 26. bis,   B,   lid   3,   tweede   alinea

Art. 312

Art. 26. bis,   B,   lid   3,   tweede   alinea,

eerste en tweede streepje Artikel 312, onder 1) en 2)

Art. 26. bis,   B,   lid   4,   eerste   alinea

Artikel 316, lid 1

Art. 26. bis,   B,   lid   4,   eerste   alinea,

onder a), b) en c) Artikel 316, lid 1, onder a), b) en c)

Art. 26. bis,   B,   lid   4,   tweede   alinea

Artikel 316, lid 2

Art. 26. bis,   B,   lid   4,   derde   alinea,

eerste en tweede volzin Artikel 317, eerste en tweede alinea

Art. 26. bis,   B,   lid   5

Art. 321

Art. 26. bis,   B,   lid   6

Art. 323

Art. 26. bis,   B,   lid   7

Art. 322

Art. 26. bis, B, lid 7, onder a), b) en c)

Artikel 322, onder a), b) en c)

Art. 26. bis,   B,   lid   8

Art. 324

Art. 26. bis,   B,   lid   9

Art. 325

Art. 26. bis,   B,   lid   10,   eerste   en

tweede alinea Artikel 318, lid 1, eerste en tweede alinea

Art. 26. bis,   B,   lid   10,   derde   alinea,

eerste en tweede streepje Artikel 318, lid 2, onder a) en b)

Art. 26. bis,   B,   lid   10,   vierde   alinea

Artikel 318, lid 3

Art. 26. bis,   B,   lid   11,   eerste   alinea

Art. 319

Art. 26. bis,   B,   lid   11,   tweede   alinea,

onder a) Artikel 320, lid 1, eerste alinea

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Art. 26. bis,   B,   lid   11,   tweede   alinea,

onder b) en c) Artikel 320, lid 1, tweede alinea

Art. 26. bis,   B,   lid   11,   derde   alinea

Artikel 320, lid 2

Art. 26. bis,   C,   lid   1,   inleidende   zin

Artikel 333, lid 1 Artikel 334

Art. 26. bis, C, lid 1, eerste tot en met

vierde streepje Artikel 334, onder a) tot en met d)

Art. 26. bis, C, lid 2, eerste en tweede

streepje Artikel 336, onder a) en b)

Art. 26. bis,   C,   lid   3

Art. 337

Art. 26. bis,   C,   lid   4,   eerste   alinea,

eerste, tweede en derde streepje Artikel 339, eerste alinea, onder a), b) en c)

Art. 26. bis,   C,   lid   4,   tweede   alinea

Artikel 339, tweede alinea

Art. 26. bis, C, lid 5, eerste en tweede

alinea Artikel 340, lid 1, eerste en tweede alinea

Art. 26. bis,   C,   lid   5,   derde   alinea

Artikel 340, lid 2

Art. 26. bis,   C,   lid   6,   eerste   alinea,

eerste en tweede streepje Artikel 338, eerste alinea, onder a) en b)

Art. 26. bis,   C,   lid   6,   tweede   alinea

Artikel 338, tweede alinea

Art. 26. bis,   C,   lid   7

Art. 335

Art. 26. bis,   D,   inleidende   zin

—

Art. 26. bis,   D,   onder   a)

Artikel 313, lid 2 Artikel 333, lid 2

Art. 26. bis,   D,   onder   b)

Artikel 4, onder a) en c)

Art. 26. bis,   D,   onder   c)

Artikel 35 Artikel 139, lid 3, eerste alinea

Art. 26. ter,   A,   eerste alinea,   onder   i),

eerste volzin Artikel 344, lid 1, onder 1)

Art. 26. ter,   A,   eerste alinea,   onder   i),

tweede volzin Artikel 344, lid 2

Art. 26. ter,   A,   tweede   alinea

Artikel 344, lid 3

Art. 26. ter,   A,   derde   alinea

Art. 345

Art. 26. ter,   B,   eerste   alinea

Art. 346

Art. 26. ter,   B,   tweede   alinea

Art. 347

Art. 26. ter,   C,   eerste   alinea

Art. 348

Art. 26. ter,   C,   tweede   alinea,   eerste

en tweede volzin Artikel 349, leden 1 en 2

Art. 26. ter,   C,   derde   alinea

Art. 350

Art. 26. ter,   C,   vierde   alinea

Art. 351

Art. 26. ter, D, lid 1, onder a), b) en c)

Artikel 354, onder a), b) en c)

Art. 26. ter,   D,   lid   2

Art. 355

Art. 26. ter, E, eerste en tweede alinea

Artikel 356, lid 1, eerste en tweede alinea

Art. 26. ter,   E,   derde   en   vierde   alinea

Artikel 356, leden 2 en 3

Art. 26. ter,   F,   eerste   volzin

Artikel 198, leden 2 en 3

Art. 26. ter,   F,   tweede   volzin

Artikelen 208 en 255

Art. 26. ter,   G,   lid   1,   eerste   alinea

Art. 352

Art. 26. ter,   G,   lid   1,   tweede   alinea

—

Art. 26. ter,   G,   lid   2,   onder   a)

Art. 353

Art. 26. ter,   G,   lid   2,   onder   b),   eerste

en tweede volzin Artikel 198, leden 1 en 3

Art. 26. quater, A, onder a) tot en met

e) Artikel 358, onder 1) tot en met 5)

Art. 26. quater,   B,   lid   1

Art. 359

Art. 26. quater,   B,   lid   2,   eerste   alinea

Art. 360

Art. 26. quater, B, lid 2, tweede alinea,

eerste deel van eerste volzin Artikel 361, lid 1

Art. 26. quater, B, lid 2, tweede alinea,

tweede deel van eerste volzin Artikel 361, lid 1, onder a) tot en met e)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Art. 26. quater, B, lid 2, tweede alinea,

tweede volzin Artikel 361, lid 2

Art. 26. quater,   B,   lid   3,   eerste   en

tweede alinea Artikel 362

Art. 26. quater,   B,   lid   4,   onder   a)   tot

en met d) Artikel 363, onder a) tot en met d)

Art. 26. quater,   B,   lid   5,   eerste   alinea

Art. 364

Art. 26. quater, B, lid 5, tweede alinea

Art. 365

Art. 26. quater,   B,   lid   6,   eerste   volzin

Artikel 366, lid 1, eerste alinea

Art. 26. quater,   B,   lid   6,   tweede   en

derde volzin Artikel 366, lid 1, tweede alinea

Art. 26. quater, B, lid 6, vierde   volzin

Artikel 366, lid 2

Art. 26. quater,   B,   lid   7,   eerste   volzin

Artikel 367, eerste alinea

Art. 26. quater,   B,   lid   7,   tweede   en

derde volzin Artikel 367, tweede alinea

Art. 26. quater,   B,   lid   8

Art. 368

Art. 26. quater,   B,   lid   9,   eerste   volzin

Artikel 369, lid 1

Art. 26. quater,   B,   lid   9,   tweede   en

derde volzin Artikel 369, lid 2, eerste en tweede alinea

Art. 26. quater,   B,   lid   10

Artikel 204, lid 1, derde alinea

Artikel 27, lid 1, eerste en tweede volzin Artikel 395, lid 1, eerste en tweede alinea

Artikel 27, lid 2, eerste en tweede volzin Artikel 395, lid 2, eerste alinea

Artikel 27, lid 2, derde volzin Artikel 395, lid 2, tweede alinea

Artikel 27, leden 3 en 4 Artikel 395, leden 3 en 4

Artikel 27, lid 5 Artikel 394

Artikel 28, leden 1 en 1 bis —

Artikel 28, lid 2, inleidende zin Artikel 109

Artikel 28, lid 2, onder a), eerste alinea Artikel 110, eerste en tweede alinea

Artikel 28, lid 2, onder a), derde alinea, eerste volzin Artikel 112, eerste alinea

Artikel 28, lid 2, onder a), derde alinea, tweede en derde volzin Artikel 112, tweede alinea

Artikel 28, lid 2, onder b) Artikel 113

Artikel 28, lid 2, onder c), eerste en tweede volzin Artikel 114, lid 1, eerste en tweede alinea

Artikel 28, lid 2, onder c), derde volzin Artikel 114, lid 2

Artikel 28, lid 2, onder d) Artikel 115

Artikel 28, lid 2, onder e), eerste en tweede alinea Artikel 118, eerste en tweede alinea

Artikel 28, lid 2, onder f) Artikel 120

Artikel 28, lid 2, onder g) —

Artikel 28, lid 2, onder h), eerste en tweede alinea Artikel 121, eerste en tweede alinea

Artikel 28, lid 2, onder i) Artikel 122

Artikel 28, lid 2, onder j) Artikel 117, lid 2

Artikel 28, lid 2, onder k) Artikel 116

Artikel 28, lid 3, onder a) Artikel 370

Artikel 28, lid 3, onder b) Artikel 371

Artikel 28, lid 3, onder c) Artikel 391

Artikel 28, lid 3, onder d) Artikel 372

Artikel 28, lid 3, onder e) Artikel 373

Artikel 28, lid 3, onder f) Artikel 392

Artikel 28, lid 3, onder g) Artikel 374

Artikel 28, lid 3 bis Artikel 376

Artikel 28, leden 4 en 5 Artikel 393, leden 1 en 2

Artikel 28, lid 6, eerste alinea, eerste volzin Artikel 106, eerste en tweede alinea

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 28, lid 6, eerste alinea, tweede volzin Artikel 106, derde alinea

Artikel 28, lid 6, tweede alinea, onder a), b) en c) Artikel 107, eerste alinea, onder a), b) en c)

Artikel 28, lid 6, tweede alinea, onder d) Artikel 107, tweede alinea

Artikel 28, lid 6, derde alinea Artikel 107, tweede alinea

Artikel 28, lid 6, vierde alinea, onder a), b) en c) Artikel 108, onder a), b) en c)

Artikel 28, lid 6, vijfde en zesde alinea —

Art. 28. bis,   lid   1,   inleidende   zin

Artikel 2, lid 1

Art. 28. bis,   lid   1,   onder   a),   eerste

alinea Artikel 2, lid 1, onder b), i)

Art. 28. bis,   lid   1,   onder   a),   tweede

alinea Artikel 3, lid 1

Art. 28. bis,   lid   1,   onder   a),   derde

alinea Artikel 3, lid 3

Art. 28. bis,   lid   1,   onder   b)

Artikel 2, lid 1, onder b), ii)

Art. 28. bis,   lid   1,   onder   c)

Artikel 3, lid 1, onder b), iii)

Art. 28. bis,   lid   1   bis,   onder   a)

Artikel 3, lid 1, onder a)

Art. 28. bis, lid 1 bis, onder b), eerste

alinea, eerste streepje Artikel 3, lid 1, onder b)

Art. 28. bis, lid 1 bis, onder b), eerste

alinea, tweede en derde streepje Artikel 3, lid 2, eerste alinea, onder a) en b)

Art. 28. bis,   lid   1   bis,   onder   b),

tweede alinea Artikel 3, lid 2, tweede alinea

Art. 28. bis,   lid   2,   inleidende   zin

—

Art. 28. bis,   lid   2,   onder   a)

Artikel 2, lid 2, eerste alinea, onder a), b) en c)

Art. 28. bis,   lid   2,   onder   b),   eerste

alinea Artikel 2, lid 2, tweede alinea

Art. 28. bis,   lid   2,   onder   b),   tweede

alinea Artikel 2, lid 2, derde alinea

Art. 28. bis,   lid   3,   eerste   en   tweede

alinea Artikel 20, eerste en tweede alinea

Art. 28. bis,   lid   4,   eerste   alinea

Artikel 9, lid 2

Art. 28. bis,   lid   4,   tweede   alinea,

eerste streepje Artikel 172, lid 1, tweede alinea

Art. 28. bis,   lid   4,   tweede   alinea,

tweede streepje Artikel 172, lid 1, eerste alinea

Art. 28. bis,   lid   4,   derde   alinea

Artikel 172, lid 2

Art. 28. bis,   lid   5,   onder   b),   eerste

alinea Artikel 17, lid 1, eerste alinea

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea Artikel 17, lid 1, tweede alinea, en lid 2, inleidende zin

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea, eerste streepje Artikel 17, lid 2, onder a) en b)

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea, tweede streepje Artikel 17, lid 2, onder c)

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea, derde streepje Artikel 17, lid 2, onder e)

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea, vijfde, zesde en zevende streepje Artikel 17, lid 2, onder f), g) en h)

Art. 28. bis,   lid   5,   onder   b),   tweede

alinea, achtste streepje Artikel 17, lid 2, onder d)

Art. 28. bis,   lid   5,   onder   b),   derde

alinea Artikel 17, lid 3

Art. 28. bis,   lid   6,   eerste   alinea

Art. 21

Art. 28. bis,   lid   6,   tweede   alinea

Art. 22

Art. 28. bis,   lid   7

Art. 23

Art. 28. ter,   A,   lid   1

Art. 40

Art. 28. ter, A, lid 2, eerste en tweede

alinea Artikel 41, eerste en tweede alinea

Art. 28. ter,   A,   lid   2,   derde   alinea,

eerste en tweede streepje Artikel 42, onder a) en b)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Art. 28. ter,   B,   lid   1,   eerste   alinea,

eerste en tweede streepje Artikel 33, lid 1, onder a) en b)

Art. 28. ter,   B,   lid   1,   tweede   alinea

Artikel 33, lid 2

Art. 28. ter,   B,   lid   2,   eerste   alinea

Artikel 34, lid 1, onder a)

Art. 28. ter,   B,   lid   2,   eerste   alinea,

eerste en tweede streepje Artikel 34, lid 1, onder b) en c)

Art. 28. ter,   B,   lid   2,   tweede   alinea,

eerste en tweede volzin Artikel 34, lid 2, eerste en tweede alinea

Art. 28. ter,   B,   lid   2,   derde   alinea,

eerste volzin Artikel 34, lid 3

Art. 28. ter,   B,   lid   2,   derde   alinea,

tweede en derde volzin —

Art. 28. ter,   B, lid 3, eerste en   tweede

alinea Artikel 34, lid 4, eerste en tweede alinea

Art. 28. ter,   C,   lid   1,   eerste   streepje,

eerste alinea Artikel 48, eerste alinea

Art. 28. ter,   C,   lid   1,   eerste   streepje,

tweede alinea Artikel 49

Art. 28. ter,   C,   lid   1,   tweede   en   derde

streepje Artikel 48, tweede en derde alinea

Art. 28. ter,   C,   leden   2   en   3

Artikel 47, eerste en tweede alinea

Art. 28. ter,   C,   lid   4

Art. 51

Art. 28. ter,   D

Art. 53

Art. 28. ter,   E,   lid   1,   eerste   en   tweede

alinea Artikel 50, eerste en tweede alinea

Art. 28. ter,   E,   lid   2,   eerste en   tweede

alinea Artikel 54, eerste en tweede alinea

Art. 28. ter,   E,   lid   3,   eerste en   tweede

alinea Artikel 44, eerste en tweede alinea

Art. 28. ter, F, eerste en tweede alinea

Artikel 55, eerste en tweede alinea

Art. 28. quater,   A,   inleidende   zin

Art. 131

Art. 28. quater,   A,   onder   a),   tweede

alinea Artikel 139, lid 1, eerste en tweede alinea

Art. 28. quater,   A,   onder   b)

Artikel 138, lid 2, onder a)

Art. 28. quater,   A,   onder   c),   eerste

alinea Artikel 138, lid 2, onder b)

Art. 28. quater,   A,   onder   c),   tweede

alinea Artikel 139, lid 2

Art. 28. quater,   A,   onder   d)

Artikel 138, lid 2, onder c)

Art. 28. quater,   B,   inleidende   zin

Art. 131

Art. 28. quater,   B,   onder   a),   b)   en   c)

Artikel 140, onder a), b) en c)

Art. 28. quater,   C

Art. 142

Art. 28. quater,   D,   eerste   alinea

Artikel 143, onder d)

Art. 28. quater,   D,   tweede   alinea

Art. 131

Art. 28. quater,   E,   punt   1,   eerste

streepje, dat artikel 16, lid 1, vervangt

— lid 1, eerste alinea Artikel 155

— lid 1, eerste alinea, A Artikel 157, lid 1, onder a)

— lid 1, eerste alinea, B, eerste alinea, onder a), b) en c) Artikel 156, lid 1, onder a), b) en c)

— lid 1, eerste alinea, B, eerste alinea, onder d), eerste en tweede streepje Artikel 156, lid 1, onder d) en e)

— lid 1, eerste alinea, B, eerste alinea, onder e), eerste alinea Artikel 157, lid 1, onder b)

— lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, eerste streepje

— lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, tweede streepje, eerste volzin

— lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, tweede streepje, tweede volzin

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

— lid 1, eerste alinea, B, eerste alinea, onder e), derde alinea, eerste streepje

— lid 1, eerste alinea, B, eerste alinea, onder e), derde alinea, tweede, derde en vierde streepje

— lid 1, eerste alinea, B, tweede alinea Artikel 156, lid 2

— lid 1, eerste alinea, C Artikel 159

— lid 1, eerste alinea, D, eerste alinea, onder a) en b) Artikel 160, lid 1, onder a) en b)

— lid 1, eerste alinea, D, tweede alinea Artikel 160, lid 2

— lid 1, eerste alinea, E, eerste en tweede streepje Artikel 161, onder a) en b)

— lid 1, tweede alinea Artikel 202

— lid 1, derde alinea Artikel 163

Art. 28. quater,   E,   onder   1),   tweede

streepje, dat lid 1 bis in artikel 16, invoegt

— lid 1 bis Artikel 162

Art. 28. quater,   E,   onder   2),   eerste

streepje, dat artikel 16, lid 2, wijzigt

— lid 2, eerste alinea Artikel 164, lid 1

Art. 28. quater,   E,   onder   2),   tweede

streepje, dat de tweede en derde alinea in artikel 16, lid 2, invoegt

— lid 2, tweede alinea Artikel 164, lid 2

— lid 2, derde alinea Artikel 165

Art. 28. quater, E, onder 3), eerste tot

en met vijfde streepje Artikel 141, onder a) tot en met e)

Art. 28. quinquies,   lid   1,   eerste   en

tweede volzin Artikel 68, eerste en tweede alinea

Art. 28. quinquies,   lid   4,   eerste   en

tweede alinea Artikel 67, leden 1 en 2

Art. 28. sexies,   lid   1,   eerste   alinea

Art. 83

Art. 28. sexies,   lid   1,   tweede   alinea,

eerste en tweede volzin Artikel 84, leden 1 en 2

Art. 28. sexies,   lid   2

Art. 76

Art. 28. sexies,   lid   3

Artikel 93, tweede alinea, onder b)

Art. 28. sexies,   lid   4

Artikel 94, lid 1

Art. 28. septies,   onder   1),   dat   arti-

kel 17, leden 2, 3 en 4, vervangt

— lid 2, onder a) Artikel 168, onder a)

— lid 2, onder b) Artikel 168, onder e)

— lid 2, onder c) Artikel 168, onder b) en d)

— lid 2, onder d) Artikel 168, onder c)

— lid 3, onder a), b) en c) Artikel 169, onder a), b) en c) Artikel 170, onder a) en b)s

— lid 4, eerste alinea, eerste streepje Artikel 171, lid 1, eerste alinea

— lid 4, eerste alinea, tweede streepje Artikel 171, lid 2, eerste alinea

— lid 4, tweede alinea, onder a) Artikel 171, lid 1, tweede alinea

— lid 4, tweede alinea, onder b) Artikel 171, lid 2, tweede alinea

— lid 4, tweede alinea, onder c) Artikel 171, lid 3

Art. 28. septies,   onder   2),   dat   arti-

kel 18, lid 1, vervangt

— lid 1, onder a) Artikel 178, onder a)

— lid 1, onder b) Artikel 178, onder e)

— lid 1, onder c) Artikel 178, onder b) en d)

— lid 1, onder d) Artikel 178, onder f)

— lid 1, onder e) Artikel 178, onder c)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Art. 28. septies, onder 3), dat lid 3 bis

in artikel 18 invoegt

— lid 3 bis, eerste deel van volzin Artikel 181

— lid 3 bis, tweede deel van volzin Artikel 182

Art. 28. octies, dat artikel 21 vervangt

— lid 1, onder a), eerste alinea Artikel 193

— lid 1, onder a), tweede alinea Artikel 194, leden 1 en 2

— lid 1, onder b) Artikel 196

— lid 1, onder c), eerste alinea, eerste, tweede en derde streepje Artikel 197, lid 1, onder a), b) en c)

— lid 1, onder c), tweede alinea Artikel 197, lid 2

— lid 1, onder d) Artikel 203

— lid 1, onder e) Artikel 200

— lid 1, onder f) Artikel 195

— lid 2 —

— lid 2, onder a), eerste volzin Artikel 204, lid 1, eerste alinea

— lid 2, onder a), tweede volzin Artikel 204, lid 2

— lid 2, onder b) Artikel 204, lid 1, tweede alinea

— lid 2, onder c), eerste alinea Artikel 199, lid 1, onder a) tot en met g)

— lid 2, onder c), tweede, derde en vierde alinea Artikel 199, leden 2, 3 en 4

— lid 3 Artikel 205

— lid 4 Artikel 201

Art. 28. nonies,   dat   artikel   21   ver-

vangt

— lid 1, onder a), eerste en tweede volzin Artikel 213, lid 1, eerste en tweede alinea

— lid 1, onder c), eerste streepje, eerste volzin Artikel 214, lid 1, onder a)

— lid 1, onder c), eerste streepje, tweede volzin Artikel 214, lid 2

— lid 1, onder c), tweede en derde streepje Artikel 214, lid 1, onder b) en c)

— lid 1, onder d), eerste en tweede volzin Artikel 215, eerste en tweede alinea

— lid 1, onder e) Artikel 216

— lid 2, onder a) Artikel 242

— lid 2, onder b), eerste en tweede alinea Artikel 243, leden 1 en 2

— lid 3, onder a), eerste alinea, eerste volzin Artikel 220, onder 1)

— lid 3, onder a), eerste alinea, tweede volzin Artikel 220, onder 2) en 3)

— lid 3, onder a), tweede alinea Artikel 220, onder 4) en 5)

— lid 3, onder a), derde alinea, eerste en tweede volzin Artikel 221, lid 1, eerste en tweede alinea

— lid 3, onder a), vierde alinea Artikel 221, lid 2

— lid 3, onder a), vijfde alinea, eerste volzin Artikel 219

— lid 3, onder a), vijfde alinea, tweede volzin Artikel 228

— lid 3, onder a), zesde alinea Artikel 222

— lid 3, onder a), zevende alinea Artikel 223

— lid 3, onder a), achtste alinea, eerste en tweede volzin Artikel 224, leden 1 en 2

— lid 3, onder a), negende alinea, eerste en tweede volzin Artikel 224, lid 3, eerste alinea

— lid 3, onder a), negende alinea, derde volzin Artikel 224, lid 3, tweede alinea

— lid 3, onder a), tiende alinea Artikel 225

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

— lid 3, onder b), eerste alinea, eerste tot en met twaalfde streepje Artikel 226, onder 1) tot en met 12)

— lid 3, onder b), eerste alinea, dertiende streepje Artikel 226, onder 13) en 14)

— lid 3, onder b), eerste alinea, veertiende streepje Artikel 226, onder 15)

— lid 3, onder b), tweede alinea Artikel 227

— lid 3, onder b), derde alinea Artikel 229

— lid 3, onder b), vierde alinea Artikel 230

— lid 3, onder b), vijfde alinea Artikel 231

— lid 3, onder c), eerste alinea Artikel 232

— lid 3, onder c), tweede alinea, inleidende zin Artikel 233, lid 1, eerste alinea

— lid 3, onder c), tweede alinea, eerste streepje, eerste volzin Artikel 233, lid 1, eerste alinea, onder a)

— lid 3, onder c), tweede alinea, eerste streepje, tweede volzin Artikel 233, lid 2

— lid 3, onder c), tweede alinea, tweede streepje, eerste volzin Artikel 233, lid 1, eerste alinea, onder b)

— lid 3, onder c), tweede alinea, tweede streepje, tweede volzin Artikel 233, lid 3

— lid 3, onder c), derde alinea, eerste volzin Artikel 233, lid 1, tweede alinea

— lid 3, onder c), derde alinea, tweede volzin Artikel 237

— lid 3, onder c), vierde alinea, eerste en tweede volzin Artikel 234

— lid 3, onder c), vijfde alinea Artikel 235

— lid 3, onder c), zesde alinea Artikel 236

— lid 3, onder d), eerste alinea Artikel 244

— lid 3, onder d), tweede alinea, tweede en derde volzin Artikel 245, lid 2, eerste en tweede alinea

— lid 3, onder d), derde alinea, eerste en tweede volzin Artikel 246, eerste en tweede alinea

— lid 3, onder d), vierde, vijfde en zesde alinea Artikel 247, leden 1, 2 en 3

— lid 3, onder d), zevende alinea Artikel 248

— lid 3, onder e), eerste alinea Artikelen 217 en 241

— lid 3, onder e), tweede alinea Artikel 218

— lid 4, onder a), eerste en tweede volzin Artikel 252, lid 1

— lid 4, onder a), derde en vierde volzin Artikel 252, lid 2, eerste en tweede alinea

— lid 4, onder a), vijfde volzin Artikel 250, lid 2

— lid 4, onder b) Artikel 250, lid 1

— lid 4, onder c), eerste streepje, eerste en tweede alinea Artikel 251, onder a) en b)

— lid 4, onder c), tweede streepje, eerste alinea Artikel 251, onder c)

— lid 4, onder c), tweede streepje, tweede alinea Artikel 251, onder d) en e)

— lid 5 Artikel 206

— lid 6, onder a), eerste en tweede volzin Artikel 261, lid 1

— lid 6, onder a), derde volzin Artikel 261, lid 2

— lid 6, onder b), eerste alinea Artikel 262

— lid 6, onder b), tweede alinea, eerste volzin Artikel 263, lid 1, eerste alinea

— lid 6, onder b), tweede alinea, tweede volzin Artikel 263, lid 2

— lid 6, onder b), derde alinea, eerste en tweede streepje Artikel 264, lid 1, onder a) en b)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

— lid 6, onder b), derde alinea, derde streepje, eerste volzin Artikel 264, lid 1, onder d)

— lid 6, onder b), derde alinea, derde streepje, tweede volzin Artikel 264, lid 2, eerste alinea

— lid 6, onder b), vierde alinea, eerste streepje Artikel 264, lid 1, onder c) en e)

— lid 6, onder b), vierde alinea, tweede streepje, eerste volzin Artikel 264, lid 1, onder f)

— lid 6, onder b), vierde alinea, tweede streepje, tweede volzin Artikel 264, lid 2, tweede alinea

— lid 6, onder b), vijfde alinea, eerste en tweede streepje Artikel 265, lid 1, onder a) en b)

— lid 6, onder b), vijfde alinea, derde streepje, eerste volzin Artikel 265, lid 1, onder c)

— lid 6, onder b), vijfde alinea, derde streepje, tweede volzin Artikel 265, lid 2

— lid 6, onder c), eerste streepje Artikel 263, lid 1, tweede alinea

— lid 6, onder c), tweede streepje Artikel 266

— lid 6, onder d) Artikel 254

— lid 6, onder e), eerste alinea Artikel 268

— lid 6, onder e), tweede alinea Artikel 259

— lid 7, eerste deel van volzin Artikel 207, eerste alinea Artikel 256 Artikel 267

— lid 7, tweede deel van volzin Artikel 207, tweede alinea

— lid 8, eerste en tweede alinea Artikel 273, eerste en tweede alinea

— lid 9, onder a), eerste alinea, eerste streepje Artikel 272, lid 1, eerste alinea, onder c)

— lid 9, onder a), eerste alinea, tweede streepje Artikel 272, lid 1, eerste alinea, onder a) en d)

— lid 9, onder a), eerste alinea, derde streepje Artikel 272, lid 1, eerste alinea, onder b)

— lid 9, onder b) Artikel 272, lid 3

— lid 9, onder c) Artikel 212

— lid 9, onder d), eerste alinea, eerste en tweede streepje Artikel 238, lid 1, onder a) en b)

— lid 9, onder d), tweede alinea, eerste tot en met vierde streepje Artikel 238, lid 2, onder a) tot en met d)

— lid 9, onder d), derde alinea Artikel 238, lid 3

— lid 9, onder e), eerste alinea Artikel 239

— lid 9, onder e), tweede alinea, eerste en tweede streepje Artikel 240, onder 1) en 2)

— lid 10 Artikelen 209 en 257

— lid 11 Artikelen 210 en 258

— lid 12, inleidende zin Artikel 269

— lid 12, onder a), eerste, tweede en derde streepje Artikel 270, onder a), b) en c)

— lid 12, onder b), eerste, tweede en derde streepje Artikel 271, onder a), b) en c)

Art. 28. decies,   dat   de derde alinea in

artikel 23, lid 3, invoegt

— lid 3, derde alinea Artikel 283, lid 1, onder b) en c)

Art. 28. undecies,   onder   1),   dat   de

tweede alinea in artikel 25, lid 4, invoegt

— lid 4, tweede alinea Artikel 272, lid 2

Art. 28. undecies,   onder   2),   dat

artikel 25, leden 5 en 6, vervangt

— lid 5, eerste alinea, onder a), b) en c) Artikel 300, onder 1), 2) en 3)

— lid 5, tweede alinea Artikel 302

— lid 6, onder a), eerste alinea, eerste volzin Artikel 301, lid 1

— lid 6, onder a), eerste alinea, tweede volzin Artikel 303, lid 1

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

— lid 6, onder a), tweede alinea, eerste, tweede en derde streepje Artikel 303, lid 2, onder a), b) en c)

— lid 6, onder a), derde alinea Artikel 303, lid 3

— lid 6, onder b) Artikel 301, lid 1

Art. 28. undecies,   onder   3),   dat   de

tweede alinea in artikel 25, lid 9, invoegt

— lid 9, tweede alinea Artikel 305

Art. 28. duodecies,   onder   1),   eerste

alinea —

Art. 28. duodecies,   onder   1),   tweede

alinea, onder a) Artikel 158, lid 3

Art. 28. duodecies,   onder   1),   tweede

alinea, onder b) en c) —

Art. 28. duodecies, onder 2), 3) en 4)

—

Art. 28. duodecies,   onder   5)

Artikel 158, lid 2

Art. 28. terdecies,   eerste   alinea

—

Art. 28. terdecies,   tweede   en   derde

alinea Artikel 402, leden 1 en 2

Art. 28. terdecies,   vierde   alinea

—

Art. 28. quaterdecies

Artikel 399, eerste alinea

Art. 28. quindecies

—

Art. 28. sexdecies,   lid   1,   inleidende

zin Artikel 326, eerste alinea

Art. 28. sexdecies,   lid   1,   onder   a),

eerste volzin Artikel 327, leden 1 en 3

Art. 28. sexdecies,   lid   1,   onder   a),

tweede volzin Artikel 327, lid 2

Art. 28. sexdecies,   lid   1,   onder   b)

Art. 328

Art. 28. sexdecies,   lid   1,   onder   c),

eerste, tweede en derde streepje Artikel 329, onder a), b) en c)

Art. 28. sexdecies,   lid   1,   onder   e)

Art. 332

Art. 28. sexdecies,   lid   1,   onder   f)

Art. 331

Art. 28. sexdecies,   lid   1,   onder   g)

Artikel 4, onder b)

Art. 28. sexdecies,   lid   1,   onder   h)

Artikel 35 Artikel 139, lid 3, tweede alinea

Art. 28. sexdecies,   lid   2

Artikel 326, tweede alinea

Art. 28. sexdecies,   lid   3

Art. 341

Art. 28. sexdecies,   lid   4

—

Art. 28. septdecies,   lid   1,   eerste,

tweede en derde streepje Artikel 405, onder 1), 2) en 3)

Art. 28. septdecies,   lid   2

Art. 406

Art. 28. septdecies,   eerste   alinea,

eerste en tweede streepje Artikel 407, onder a) en b)

Art. 28. septdecies,   lid   3,   tweede

alinea —

Art. 28. septdecies, lid 4, onder a) tot

en met d) Artikel 408, lid 1, onder a) tot en met d)

Art. 28. septdecies,   lid   5,   eerste   en

tweede streepje Artikel 408, lid 2, onder a) en b)

Art. 28. septdecies,   lid   6

Art. 409

Art. 28. septdecies, lid 7, eerste alinea,

onder a), b) en c) Artikel 410, lid 1, onder a), b) en c)

Art. 28. septdecies,   lid   7,   tweede

alinea, eerste streepje —

Art. 28. septdecies,   lid   7,   tweede

alinea, tweede en derde streepje Artikel 410, lid 2, onder a) en b)

Artikel 29, leden 1 tot en met 4 Artikel 398, leden 1 tot en met 4

Art. 29. bis

Art. 397

Artikel 30, lid 1 Artikel 396, lid 1

Artikel 30, lid 2, eerste en tweede volzin Artikel 396, lid 2, eerste alinea

Artikel 30, lid 2, derde volzin Artikel 396, lid 2, tweede alinea

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Artikel 30, leden 3 en 4 Artikel 396, leden 3 en 4

Artikel 31, lid 1 —

Artikel 31, lid 2 Artikel 400

Artikel 33, lid 1 Artikel 401

Artikel 33, lid 2 Artikel 2, lid 3

Art. 33. bis,   lid   1,   inleidende   zin

Art. 274

Art. 33. bis,   lid   1,   onder   a)

Art. 275

Art. 33. bis,   lid   1,   onder   b)

Art. 276

Art. 33. bis,   lid   1,   onder   c)

Art. 277

Art. 33. bis,   lid   2,   inleidende   zin

Art. 278

Art. 33. bis,   lid   2,   onder   a)

Art. 279

Art. 33. bis,   lid   2,   onder   b)

Art. 280

Artikel 34 Artikel 404

Artikel 35 Artikel 403

Artikelen 36 en 37 —

Artikel 38 Artikel 414

Bijlage A, onder I, onder 1) en 2) Bijlage VII, onder 1), a) en b)

Bijlage A, onder I, onder 3) Bijlage VII, onder 1, b) en c)

Bijlage A, onder II, onder 1) tot en met 6) Bijlage VII, onder 2), a) tot en met f)

Bijlage A, onder III en IV Bijlage VII, onder 3) en 4)

Bijlage A, onder IV, onder 1) tot en met 4) Bijlage VII, onder 4), a) tot en met d)

Bijlage A, onder V Artikel 295, lid 2

Bijlage B, inleidende zin Artikel 295, lid 1, onder 5)

Bijlage B, eerste tot en met negende streepje Bijlage VIII, onder 1) tot en met 9)

Bijlage D, onder 1) tot en met 13) Bijlage I, onder 1) tot en met 13)

Bijlage E, onder 2) Bijlage X, Deel A, onder 1)

Bijlage E, onder 7) Bijlage X, Deel A, onder 2)

Bijlage E, onder 11) Bijlage X, Deel A, onder 3)

Bijlage E, onder 15) Bijlage X, Deel A, onder 4)

Bijlage F, onder 1) Bijlage X, Deel B, onder 1)

Bijlage F, onder 2) Bijlage X, deel B, onder 2), a) tot en met j)

Bijlage F, onder 5) tot en met 8) Bijlage X, Deel B, onder 3) tot en met 6)

Bijlage F, onder 10) Bijlage X, Deel B, onder 7)

Bijlage F, onder 12) Bijlage X, Deel B, onder 8)

Bijlage F, onder 16) Bijlage X, Deel B, onder 9)

Bijlage F, onder 17), eerste en tweede alinea Bijlage X, Deel B, onder 10)

Bijlage F, onder 23) Bijlage X, Deel B, onder 11)

Bijlage F, onder 25) Bijlage X, Deel B, onder 12)

Bijlage F, onder 27) Bijlage X, Deel B, onder 13)

Bijlage G, leden 1 en 2 Artikel 391

Bijlage H, eerste alinea Artikel 98, lid 3

Bijlage H, tweede alinea, inleidende zin —

Bijlage H, tweede alinea, onder 1) tot en met 6) Bijlage III, onder 1) tot en met 6)

Bijlage H, tweede alinea, onder 7), eerste en tweede alinea Bijlage III, onder 7) en 8)

Bijlage H, tweede alinea, onder 8) tot en met 17) Bijlage III, onder 9) tot en met 18)

Bijlage I, inleidende zin —

Bijlage I, onder a), eerste tot en met zevende streepje Bijlage IX, deel A, onder 1) tot en met 7)

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn

Bijlage I, onder b), eerste en tweede streepje Bijlage IX, deel B, onder 1) en 2)

Bijlage I, onder c) Bijlage IX, deel C

Bijlage J, inleidende zin Bijlage V, inleidende zin

Bijlage J Bijlage V, onder 1) tot en met 25)

Bijlage K, onder 1), eerste, tweede en derde streepje Bijlage IV, onder 1), a), b) en c)

Bijlage K, onder 2) tot en met 5) Bijlage IV, onder 2) tot en met 5)

Bijlage L, eerste alinea, onder 1) tot en met 5) Bijlage II, onder 1) tot en met 5)

Bijlage L, tweede alinea Artikel 56, lid 2

Bijlage M, onder a) tot en met f) Bijlage VI, onder 1) tot en met 6)

Artikel 1, onder 1), tweede alinea, van Richtlijn 89/465/EEG Artikel 133, tweede alinea

Art. 2. van   Richtlijn   94/5/EG

Art. 342

Artikel 3, eerste en tweede volzin, van Richtlijn 94/5/EG Artikel 343, eerste en tweede alinea

Art. 4. van   Richtlijn   2002/38/EG

Artikel 56, lid 3 Artikel 57, lid 2 Artikel 357

Art. 5. van   Richtlijn   2002/38/EG

—

Richtlijn 67/227/EEG Richtlijn 77/388/EEG Wijzigingsrichtlijnen Andere besluiten Deze richtlijn