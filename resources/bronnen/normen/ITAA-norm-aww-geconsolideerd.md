---
tags:
  - norm
  - itaa
naam: Geconsolideerde AWW-norm — IAB-norm + BIBF-richtlijn gecombineerd
datum: 2022-04-26
type: norm
itaa-lex-sectie: XVII
toepassingsgebied: Alle ITAA-leden (gecertificeerde accountants + belastingadviseurs)
themas:
  - antiwitwas
  - cliëntenonderzoek
  - UBO
  - AMLCO
  - risicoanalyse
  - meldingsplicht
  - geconsolideerd
bron: beexcellentnl.itaa.be
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: beexcellentnl.itaa.be
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 15302c50
    model:
    prompt_version:
  generated_at: '2026-05-14T20:17:52Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-16T20:34:11Z'
    confirmed_by: human
    rationale: "Spot-check 2026-05-16: slechts 5 ## headings terwijl de norm 10 hoofdsecties (+ 4 bijlagen) heeft. De two-column PDF-extractie via pdftotext (geen -layout) fragmenteert sectie-koppen 2-4 en 6-10 in body-text zonder ze als heading te promoveren. Voorbeeld: '2.1. Elke beroepsbeoefenaar...' verschijnt zonder voorafgaande '## 2. Organisatie en interne controle'-heading. Dit is een patroon dat de huidige inject_norm_headings.py niet pakt voor dit specifieke document; vereist refactoring in tools/etl/inject_norm_headings.py (patroon A guard te zwak voor two-column glitches)."
    caveat:
    layer1:
    layer2:
---
Geconsolideerde tekst door het Instituut van de Belastingadviseurs en de Accountants (ITAA) van de norm van het IAB en de richtlijn van het BIBF inzake de toepassing van de wet van 18 september 2017 tot

voorkoming van het witwassen van geld en de financiering van terrorisme en tot beperking van het gebruik van contanten

Op 31 maart 2020 hebben de Nationale Raad van het Beroepsinstituut van Boekhouders-Fiscalisten
respectievelijk een richtlijn en een norm goedgekeurd inzake de toepassing van de wet van 18
september 2017 tot voorkoming van het witwassen van geld en de financiering van terrorisme en de beperking van het gebruik van contanten.

De BIBF-richtlijn en de IAB-norm hebben exact dezelfde inhoud en blijven aldus van toepassing na de
fusie tussen beide Instituten en de daaruit volgende oprichting van het ITAA op 30 september 2020.

om een nieuwe norm, maar een samensmelting van beide documenten als gevolg van de oprichting
van het ITAA. Deze samensmelting ligt volledig in lijn met het optreden in rechten en plichten van de
vroegere IAB en BIBF, als toezichthoudend orgaan inzake antiwitwas (overeenkomstig artikel 85,7° van de wet van 18 september 2017).

## 1. Algemene bepalingen

Definities 1.1. Voor de toepassing van de geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF wordt verstaan onder:

1° “de Wet”: de wet van 18 september 2017 tot voorkoming van het witwassen van geld en de financiering van terrorisme en tot beperking van het gebruik van contanten;

2° “witwassen van geld”: zoals bedoeld in artikel 2 van de Wet;

3° “financiering van terrorisme”: zoals bedoeld in artikel 3 van de Wet;

4° “WG/FT": het witwassen van geld en/of de financiering van terrorisme;

5° “criminele activiteit”: zoals bedoeld in artikel 4,23° van de Wet;

6° “uiteindelijke begunstigde”: een natuurlijke persoon zoals bedoeld in artikel 4,27° van de Wet;

7° “politiek prominente personen”: een persoon zoals bedoeld in artikel 4, 28° tot
30° van de Wet;

8° “zakelijke relatie”: een zakelijke relatie zoals bedoeld in artikel 4, 33° van de Wet;

9° “beroepsbeoefenaar”:

a) voor de norm van het Instituut van de Bedrijfsrevisoren: een natuurlijke persoon, een rechtspersoon of een andere entiteit met om het even welke rechtsvorm die ressorteert onder één van de categorieën opgesomd in artikel 5, §1,
23°, van de Wet;

b) Voor de geconsolideerde tekst door het Instituut van de Belastingadviseurs en het IAB en de richtlijn van het BIBF : een natuurlijke persoon, een rechtspersoon of een andere entiteit met om het even welke rechtsvorm die ressorteert onder één van de categorieën opgesomd in artikel 5, §1, 24° of 25°, van de Wet

10° “onafhankelijke auditfunctie”: de functie bedoeld in artikel 8, §2, 2°, a) van de Wet om de gedragslijnen, procedures en interne controlemaatregelen te testen;

een andere entiteit met om het even welke rechtsvorm, andere dan een natuurlijk persoon, ingeschreven in het openbaar register van de bedrijfsrevisoren;

b) voor de geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF: de organisatorische eenheid

1) waarbinnen één of meer beroepsbeoefenaars voor een cliënt beroepsactiviteiten uitoefenen, als bedoeld in artikelen 3 en 6 van de wet van 17 maart 2019 betreffende de beroepen van accountant en belastingadviseur;

2) en die bestaat uit ofwel uitsluitend één vestiging ofwel meerdere vestigingen waarbinnen dezelfde werkmethodes van toepassing zijn.

19° “ netwerk”: de grotere structuur waartoe een beroepsbeoefenaar of kantoor behoort:

a) die op samenwerking is gericht; en b) die duidelijk is gericht op winst- of kostendeling, of het delen van gemeenschappelijke eigendom, zeggenschap of bestuur, een gemeenschappelijk beleid en procedures inzake kwaliteitsbeheersing, een gemeenschappelijke bedrijfsstrategie, het gebruik van een gemeenschappelijke merknaam of een aanzienlijk deel van de bedrijfsmiddelen.

20° “CFI”: de Cel voor financiële informatieverwerking bedoeld in artikel 76 van de Wet.

1.2. Voor het overige hebben de in deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF gebruikte termen dezelfde betekenis als in de Wet.

Toepassingsgebied ratione personae 1.3. De bepalingen van deze geconsolideerde van het BIBF zijn van toepassing op de beroepsbeoefenaars zoals bedoeld in artikel 5,
§1, 24° en 25° van de Wet,  handelend in het kader van hun beroepsactiviteiten:

bedoelde functie door die persoon zelf uitgeoefend.

2.2. Elke beroepsbeoefenaar moet in toepassing van artikel 9, §2 van de Wet, een AMLCO aanduiden.

Van zodra het kantoor minstens tien beroepsbeoefenaars telt, in de zin van punt 1.1, 9°, a) of b) van deze geconsolideerde van het BIBF, die een activiteit uitoefenen en/of een deelname hebben en/of lid zijn van het wettelijk bestuursorgaan, moet de AMLCO een van de in punt 2.1 van deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF onderscheiden persoon zijn.

In alle andere gevallen, kan de verantwoordelijke op het hoogste niveau zelf ook de functie van AMLCO vervullen.

De kantoren die deel uitmaken van een netwerk, dienen elk een AMLCO aan te duiden, onverminderd de mogelijkheid om tevens een AMLCO te benoemen op het niveau van het netwerk. De benoeming van een AMLCO op het niveau van het netwerk mag op geen enkele manier de bevoegdheden kantoor wijzigen.

2.3. Onverminderd hetgeen bepaald is in punten 2.1 en 2.2 van deze geconsolideerde van het BIBF, zal een stagiair in geen geval aangeduid kunnen worden als verantwoordelijke op het hoogste niveau noch als AMLCO.

2.4. Bij voorkeur voorafgaandelijk, of ten beëindiging van de opdracht van de in punten 2.1 en 2.2 bedoelde personen stelt de beroepsbeoefenaar de Toezichtautoriteit hiervan schriftelijk of via een elektronisch bericht in kennis.

2.5. In het geval dat de AMLCO en de verantwoordelijke op het hoogste niveau onderscheiden personen zijn dient:

risico's waaraan de beroepsbeoefenaar is blootgesteld, en om het passend karakter te waarborgen van de gedragslijnen, procedures en interne controlemaatregelen die ten uitvoer zijn gelegd in toepassing van artikel 8 van de Wet

2.7 Onverminderd de toepassing van artikel 8,
§2, 2°, a) van de Wet, moet een kantoor of netwerk waarbij minstens honderd beroepsbeoefenaars, zoals bedoeld in artikel 1, 9° a) of b) van deze geconsolideerde tekst BIBF, een activiteit uitoefenen en/of een deelname hebben in en/of lid zijn van het wettelijk bestuursorgaan, een onafhankelijke auditfunctie voorzien.

Interne procedures 2.8. Alle in de Wet vermelde gedragslijnen, procedures en interne controlemaatregelen worden goedgekeurd door de effectieve leiding die de eindverantwoordelijkheid draagt. Ze moeten worden gedocumenteerd, bijgewerkt en op papier of elektronisch ter beschikking worden gehouden van de Toezichtautoriteit van de beroepsoefenaar.

2.9. Overeenkomstig artikel 10 van de Wet, moet elke beroepsbeoefenaar die beroep doet op medewerkers voorzien in een specifiek, onafhankelijk en anoniem kanaal, zodat zij hun medewerkers in staat stellen om aan de AMLCO of aan de verantwoordelijke persoon op het hoogste niveau de inbreuken bij het vervullen van de verplichtingen bepaald in Boek II van de Wet, te melden.

2.10. De AMLCO voorziet in schriftelijke, op papier en/of digitaal, gedragslijnen, procedures en interne controlemaatregelen inzake sensibilisering en opleidingen van de medewerkers met betrekking tot de voorkoming van het WG/FT.

Om uit te maken welke personen geviseerd zijn en wat de inhoud en frequentie van voormelde sensibilisering en opleiding is, dient die de medewerkers verrichten voor de cliënten, de verrichtingen die deze uitvoeren,

3.3.
De algemene risicobeoordeling wordt bepaald en uitgevoerd onder de effectieve verantwoordelijkheid van de AMLCO en goedgekeurd op het hoogste niveau door het wettelijk bestuursorgaan of door de effectieve leiding.

3.4.
De beroepsbeoefenaar documenteert tevens op welke wijze de aldus vastgestelde WG/FT-risico's in aanmerking zijn genomen in de gedragslijnen, waaronder het cliëntacceptatiebeleid, in de procedures en in de interne controlemaatregelen.

Vaststellen van risicocategorieën 3.5 Elke beroepsbeoefenaar stelt verschillende risicocategorieën vast, waaraan geschikte waakzaamheidsmaatregelen worden gekoppeld.

Deze risicocategorieën worden vastgesteld op algemene risicobeoordeling en van objectieve risicocriteria die onderling coherent gecombineerd zijn.

De beroepsbeoefenaar ziet er voorts op toe dat deze risicocategorieën hem in staat stellen om rekening te houden met:

1° de gevallen van hoog risico die zijn geïdentificeerd in toepassing van artikel 19,
§ 2 van de Wet en, ten minste, met de gevallen bedoeld in de artikelen 37 tot 41 van de Wet;

2° in voorkomend geval, de gevallen van laag risico die zijn geïdentificeerd in toepassing van artikel 19, § 2, tweede lid van de Wet;

3° de Belgische risicoanalyse inzake WG/FT, alsook deze van de Europese Commissie.

Actualisering 3.6.
De algemene risicobeoordeling moet worden bijgewerkt telkens er zich een gebeurtenis voordoet die een significante invloed kan hebben op een of meerdere risico's.

3.7.
De AMLCO verifieert bovendien minstens jaarlijks of de algemene

- om maatregelen te nemen om de geïdentificeerde risico’s op te volgen en te beheersen.

3° de cliënten over de verschillende risicocategorieën als bedoeld in punt 3.5 van deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF, verdeelt.

Het cliëntacceptatiebeleid maakt het ook mogelijk om bindende bepalingen betreffende financiële embargo's zoals bedoeld in artikel 4,
6° van de Wet ten uitvoer te leggen.

4.2.
Het cliëntacceptatiebeleid van de beroepsbeoefenaar bepaalt dat cliënten die mogelijk een specifiek risico vormen, pas als cliënt worden aanvaard na een passend onderzoek en er op een geschikt hiërarchisch niveau een beslissing is genomen.

Hieronder ressorteren onder meer cliënten en/of verrichtingen waarvan met toepassing van artikel 19, §2 van de Wet wordt vastgesteld dat ze een hoog risico inhouden, en ten minste de gevallen die worden bedoeld in de artikelen 37 tot 41 van de Wet.

4.3. Behoudens de uitzonderingen voorzien in weigert  de beroepsbeoefenaar de zakenrelatie verrichting uit te voeren, wanneer:

- hij zijn verplichtingen tot identificatie en verificatie van de identificatiegegevens van zijn cliënt, van diens lasthebbers of diens uiteindelijke begunstigden niet kan naleven; of

- er redenen bestaan om aan te nemen dat het gebrek aan relevantie of geloofwaardigheid van de door de cliënt meegedeelde informatie ertoe strekt zijn identiteit,  dat van zijn lasthebbers en/of van één of meer van zijn uiteindelijke begunstigden te verhullen; of

- hij zijn verplichting met betrekking tot het beoordelen van de kenmerken van aard van de zakelijke relatie of de

4.8. In functie van het risicoprofiel dienen de documenten, gegevens of informatie regelmatig te worden bijgewerkt.

Verhoogde waakzaamheid 4.9.
De beroepsbeoefenaar past, overeenkomstig de artikelen 37 tot en met 41 van de Wet, een verhoogde waakzaamheid toe ten aanzien van de zakelijke relatie of occasionele verrichting wanneer:

- het onmogelijk is om, conform artikel 31 van de Wet, over te gaan tot verificatie alvorens de zakelijke relatie aan te gaan;

- de cliënt, de lasthebber en/of uiteindelijke begunstigde gevestigd is in een derde land met een hoog risico;

- de cliënt, de lasthebber en/of uiteindelijke begunstigde gevestigd is in een Staat zonder of met een lage belasting, inzonderheid rekening houdend met het risico op het witwassen van geld afkomstig uit al dan niet georganiseerde ernstige fiscale fraude;

- de cliënt, de lasthebber en/of uiteindelijke begunstigde een politiek prominent persoon, familielid van een politiek prominent persoon of persoon bekend als naaste geassocieerde van een politiek prominent persoon is.

Nakoming van de waakzaamheidsverplichtingen door derde zaakaanbrengers 4.10. De beroepsbeoefenaar mag beroep doen op een derde zaakaanbrenger - die zelf een aan een gelijkwaardige antiwitwasregelgeving onderworpen entiteit is - voor de nakoming van zijn verplichtingen betreffende de identiteit van de  cliënt, van diens lasthebbers of diens uiteindelijke begunstigden en met betrekking tot en het doel en de beoogde aard van de zakelijke relatie  en de actualisering ervan.

De mogelijkheid om de bovenvermelde verplichtingen  te laten uitvoeren door een derde zaakaanbrenger is echter enkel mogelijk als deze laatste persoonlijk de identificatie heeft

## 5. Onderzoek van de verrichtingen

Onderkennen van atypische verrichtingen 5.1. De beroepsbeoefenaar brengt de volgende elementen schriftelijk ter kennis van de medewerkers bedoeld in punt 2.10, tweede lid van deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF:

1° de criteria die hen in staat moeten stellen atypische verrichtingen te onderkennen;

2° de te volgen procedure om deze verrichtingen te onderwerpen aan een specifieke analyse onder de verantwoordelijkheid van de AMLCO, overeenkomstig artikel 45, §1 van de Wet teneinde te bepalen of van deze verrichtingen vermoed kan worden dat ze verband houden met WG/FT.

Analyse van de atypische verrichtingen 5.2. Overeenkomstig artikel 9, §2 van de Wet stelt de beroepsbeoefenaar passende procedures vast om een analyse te verrichten van de atypische verrichtingen, teneinde overeenkomstig artikel 45, van de Wet te bepalen of er een vermoeden moet worden gemeld aan de CFI met toepassing van artikel 47 van de Wet.

Melding van vermoedens 5.3. Wanneer de AMLCO of, in voorkomend geval, één van de beroepsbeoefenaars zoals bedoeld in punt 1.1, 9°, a) of b) van deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF, in toepassing van artikel 47, van de Wet een vermoeden meldt, wordt een nieuwe individuele beoordeling van de WG/FT-risico's uitgevoerd waarbij rekening wordt gehouden met de omstandigheid dat er in verband met de betrokken cliënt een vermoeden werd gemeld.

Op basis van deze nieuwe beoordeling en van het in punt 4 van deze geconsolideerde tekst BIBF bedoelde cliëntacceptatiebeleid besluit de beroepsbeoefenaar de reeds aangegane zakelijke relatie ofwel voort te zetten, in welk geval deze de waakzaamheidsmaatregelen ten

- de bewijsstukken die nodig zijn voor het documenteren van het inzicht in de uitgevoerde verrichtingen rekening houdende met de finaliteit van de beoogde zakelijke relatie;

- het schriftelijk verslag, opgemaakt in het kader van de atypische verrichtingen, zoals bedoeld in artikelen 45 en 46 van de Wet;

- in toepassing van de artikelen 47 tot 54 van de Wet,  een melding te doen aan de CFI, rechtvaardigen;

- en, in het algemeen, alle informatie in geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF opgelegde verplichtingen.

6.3. De algemene risicobeoordeling wordt gedocumenteerd, bijgewerkt en ter beschikking gehouden van de Toezichtautoriteit en dit op papier of op elektronische drager.

6.4. Deze documenten moeten bewaard worden gedurende 10 jaar vanaf het einde van datum van een occasionele verrichting.

7. Beperkingen van het gebruik van contanten Wanneer de beroepsbeoefenaar weet, vermoedt of redelijke gronden heeft om te vermoeden dat feiten of verrichtingen die geleid hebben tot een gift of betaling in contanten verband houden met het WG/FT dient hij dit vermoeden onmiddellijk te melden aan de CFI.

Voor zover nodig, verwijzen de beroepsbeoefenaars naar de mededelingen van hun respectievelijke instituten.

8. Toezicht en controle Teneinde de Toezichtautoriteit toe te laten de

BIJLAGEN

financiering van terrorisme en tot beperking van het gebruik van contanten maken integraal deel uit van
de Wet. Ze zijn hieronder opgenomen en maken dus ook integraal deel uit van deze geconsolideerde verwezen wordt, wordt uitdrukkelijk vermeld dat het om artikelen van de betrokken bijlage gaat.

## Bijlage I. Variabelen ten minste in overweging te nemen in de integrale risicobeoordeling

risicobeoordeling bedoeld in punt 3.1 van deze geconsolideerde tekst van de norm van het IAB en de richtlijn van het BIBF, zijn de volgende:

1° het doel van een rekening of een relatie;

2° de omvang van de activa die door een cliënt worden gedeponeerd of de omvang van de gesloten verrichtingen;

3° de regelmaat of de duur van de zakelijke relatie.

## Bijlage II. De indicatieve factoren van een potentieel lager risico
Artikel 1. De indicatieve factoren van een potentieel lager risico bedoeld in punt 3.1 van deze

1° cliëntgebonden risicofactoren:

a) beursgenoteerde vennootschappen die onderworpen zijn aan informatievereisten (op grond
van het beursreglement of krachtens wettelijke of afdwingbare middelen) welke voorschriften
omvatten om toereikende transparantie betreffende de uiteindelijke begunstigden te garanderen;

b)  overheden of overheidsbedrijven;

c)  cliënten die inwoner zijn van geografische gebieden met een lager risico als vermeld in punt
3°;

2° risicofactoren verbonden aan producten, diensten, verrichtingen of leveringskanalen:

a) levensverzekeringsovereenkomsten met een lage premie;

b) pensioenverzekeringsovereenkomsten die geen afkoopclausule bevatten en niet als zekerheidstelling kunnen dienen;

c) een pensioenstelsel, een pensioenfonds of een soortgelijk stelsel dat pensioenen uitkeert
aan werknemers, waarbij de bijdragen worden ingehouden op het loon en de regels van het
stelsel de deelnemers niet toestaan hun rechten uit hoofde van het stelsel over te dragen;

d) financiële producten of diensten die op passende wijze bepaalde en beperkte diensten voor
bepaalde soorten cliënten omvatten, om voor financiële inclusiedoeleinden de toegang te vergroten;

e) producten waarbij het WG/FT-risico wordt beheerd door andere factoren zoals
bestedingslimieten of transparantie van eigendom (bv. bepaalde soorten elektronisch geld);

3° geografische risicofactoren:

a) lidstaten;

b) derde landen met doeltreffende systemen ter bestrijding van WG/FT;

c) derde landen die volgens geloofwaardige bronnen een laag niveau van corruptie of andere criminele activiteit hebben;

d) derde landen die volgens geloofwaardige bronnen zoals wederzijdse beoordelingen,
gedetailleerde evaluatierapporten, of gepubliceerde follow-uprapporten, voorschriften inzake de
bestrijding van WG/FT hebben die beantwoorden aan de herziene FAG-aanbevelingen en die voorschriften effectief ten uitvoer leggen.

## Bijlage III. De indicatieve factoren van een potentieel hoger risico
Artikel 1. De indicatieve factoren van een potentieel hoger risico bedoeld in punt 3.1 van deze

1° cliëntgebonden risicofactoren:

a) de zakelijke relatie vindt plaats in ongebruikelijke omstandigheden;

b) de cliënten die inwoner zijn van geografische gebieden met een hoog risico bedoeld onder
3°;

c) rechtspersonen of juridische constructies die vehikels zijn voor het aanhouden van persoonlijke activa;

d) vennootschappen met gevolmachtigde aandeelhouders ("shareholders") of met aandelen aan toonder;

e) bedrijven waar veel geldverkeer in contanten plaatsvindt;

2° risicofactoren verbonden aan producten, diensten, verrichtingen of leveringskanalen:

a) private banking;

b) producten of verrichtingen die anonimiteit bevorderen;

c) zakelijke relaties op afstand of verrichtingen op afstand, zonder sommige garanties, zoals elektronische handtekeningen;

d) betalingen die worden ontvangen van onbekende of niet-verbonden derden;

e) nieuwe producten en nieuwe zakelijke praktijken, daaronder begrepen nieuwe
leveringsmechanismen, en het gebruik van nieuwe of in ontwikkeling zijnde technologieën voor zowel nieuwe als reeds bestaande producten.

3° geografische risicofactoren:

a) onverminderd artikel 38, landen die op basis van geloofwaardige bronnen zoals wederzijdse
beoordelingen, gedetailleerde evaluatierapporten, of gepubliceerde follow-uprapporten, worden aangemerkt als een land zonder effectieve WG/FT-systemen;

b) landen die volgens geloofwaardige bronnen significante niveaus van corruptie of andere criminele activiteit hebben;

a) landen waarvoor sancties, embargo's of soortgelijke maatregelen gelden die b) landen die financiering of ondersteuning verschaffen voor terroristische activiteiten, of
op het grondgebied waarvan als terroristisch aangemerkte organisaties actief zijn.

BIJLAGE IV: Beslissingsbomen ter illustratie Elk kantoor is ertoe gehouden een methodologie vast te leggen teneinde de gedragslijnen, procedures
en interne controlemaatregelen te bepalen en toe te passen die evenredig zijn met de aard en omvang van het kantoor.

In dit opzicht, kunnen de hierna volgende beslissingsbomen door de kantoren als voorbeeld worden gebruikt. Ze hebben betrekking op:

- het aangaan van een zakenrelatie met een nieuwe cliënt ; en

- de identificatie van een uiteindelijke begunstigde.

Vermits het gebruik ervan niet verplicht is, worden ze enkel als voorbeeld aangehaald en dienen ze,
in voorkomend geval, aangepast te worden aan de specifieke activiteiten uitgeoefend door elk kantoor.
