---
tags: ["4.0"]
itaa-lex-sectie: ""
wet: "Handleiding interne procedures — Model voor de beroepsbeoefenaar (in toepassing van de AWW 2017)"
bron_rol: "praktijkgids"
status: "beschikbaar"
bijgewerkt: "07.11.2019"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/ITAA-Handleiding-interne-procedures-AWW-2019.pdf
      sha256: ba44c8b7c54ed0ae09e507130ba917975c3718e054ed19eb1a30a2fcd96e7a9b
      version: 07.11.2019
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T15:41:56Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T15:49:09Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Alle drie primaire ETL-fixes zijn bevestigd: 0 running page-headers ('Interne procedure'), 0 TOC dotted-leaders, 0 '•'-bullets. Resterende aandachtspunten (➢-bullets, invul-velden, inline-URLs) zijn source-conform artefacten van het modelformulier die transformers niet kunnen of mogen wegnemen, en vallen buiten de needs-rework-drempel. Layer 1 toont nog 'warn' in frontmatter, maar dat reflecteert de toestand vóór de rerun — de inhoudelijke oorzaak (page-headers) is opgelost."
    caveat:
    layer1:
      status: warn
      run_id: 20260519-154646
      run_at: '2026-05-19T15:46:46Z'
      heading_count: 20
      max_section_chars: 40984
      file_size_chars: 144079
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ##-niveau: 40984 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T15:49:09Z'
      rationale: "Alle drie primaire ETL-fixes zijn bevestigd: 0 running page-headers ('Interne procedure'), 0 TOC dotted-leaders, 0 '•'-bullets. Resterende aandachtspunten (➢-bullets, invul-velden, inline-URLs) zijn source-conform artefacten van het modelformulier die transformers niet kunnen of mogen wegnemen, en vallen buiten de needs-rework-drempel. Layer 1 toont nog 'warn' in frontmatter, maar dat reflecteert de toestand vóór de rerun — de inhoudelijke oorzaak (page-headers) is opgelost."
      concrete_problemen:
        - regel: 216
          categorie: (source)
          type: niet-standaard bullet ➢ in modelformulier-blokken (100 exemplaren)
          voorbeeld: '➢ Optioneel: indien betrokkene onbeschikbaar is kan men contact nemen met:'
        - regel: 202
          categorie: (invul-field)
          type: invul-velden van modelformulier als plain tekst in body
          voorbeeld: de heer/mevrouw ………………………., die de beroepshoedanigheid heeft van ……………..
        - regel: 80
          categorie: (source)
          type: plaintext URL in body-tekst (source-conform)
          voorbeeld: http://www.ctif-cfi.be/website/images/NL/meld/toelichting2017-ndls.pdf
---

# Handleiding interne procedures — Model voor de beroepsbeoefenaar (in toepassing van de AWW 2017)

*Bijgewerkt tot en met 07.11.2019 — gecoördineerde versie.*

Handleiding interne procedures – Model voor de beroepsbeoefenaar

In toepassing van de AWW van 18 september 2017 tot voorkoming van het witwassen  van geld en de financiering van terrorisme en tot beperking van het gebruik van  contanten

Referenties van het kantoor/de beroepsbeoefenaar

- Naam en, indien van toepassing, rechtsvorm :  • Adres van het hoofdkantoor :  • Zetel :  • inschrijvingsnummer:

1. INHOUDSTAFEL

2. BEGELEIDENDE NOTA

Huidig document is bestemd om de AMLCO van de kantoren van beroepsbeoefenaars bij  te staan bij het opstellen en het inwerkingstellen van doeltreffende gedragslijnen,  procedures en interne controlemaatregelen, evenredig met hun aard en omvang, zoals  opgelegd door artikel 8, §1 van de AWW van 18 september 2017 tot voorkoming van het  witwassen van geld en de financiering van terrorisme en tot beperking van het gebruik van  contanten (hierna de AWW ).

Dit voorbeeld van handleiding voor het opstellen van doeltreffende gedragslijnen,  procedures en interne controlemaatregelen heeft geen verplicht of normatief karakter.  Het komt de kantoren toe zich hierop in voorkomend geval te inspireren in functie van hun  noden en/of in functie van hun eigen bestaande gedragslijnen, procedures en interne  controlemaatregelen of met deze die ze wensen toe te passen. Het document kan op zich  worden gebruikt, maar wij raden aan om het desgevallend te integreren in de eigen  bestaande documenten betreffende procedures en/of kwaliteitsbeheersing.

Huidig document strekt ertoe de beroepsbeoefenaars en hun medewerkers toe te laten de  antiwitwaswet- en regelgeving beter te begrijpen en in werking te stellen, op een wijze die  aangepast is aan de eigen structuur en omvang van het kantoor teneinde de  geïdentificeerde risico’s op witwassen van geld en/of de financiering van terrorisme te  beperken en efficiënt te beheren.

Aanpassingen, weglatingen en toevoegingen kunnen worden aangebracht in functie van  de omvang, de activiteiten en de diensten van het kantoor en de kenmerken van het  cliënteel.

Daarbij zullen de kantoren in alle omstandigheden rekening houden met:

-  De deontologische regels van het beroep

-  De antiwitwaswetgeving (Wet 18 september 2017 – hierna AWW genoemd),

-  De eigen handleiding kwaliteitsbeheer

Verder kan steeds www.ctif-cfi.be geraadpleegd worden. Daar zal men onder  http://www.ctif-cfi.be/website/images/NL/meld/toelichting2017-ndls.pdf  Richtsnoeren  voor de entiteiten en beroepsbeoefenaars onderworpen aan de wet van 18 september 2017  kunnen vinden, met o.a. in de hoofdstukken 1, 2 en 3 “ Wie moet melden ”, “ Wat verstaat  men onder “witwassen van geld” en “ Financiering van terrorisme ”, in welke gevallen men  moet melden, alsook wie de personen zijn die gemachtigd zijn om een melding aan de CFI  te doen.

De beroepsbeoefenaars die deel uitmaken van een netwerk moeten de op dit niveau  geldende gedragslijnen en procedures ter voorkoming van WG/FT toepassen, daaronder  met name inbegrepen de gedragslijnen inzake gegevensbescherming en de gedragslijnen  en procedures voor het delen van informatie binnen het netwerk ten behoeve van de strijd  tegen WG/FT. Dergelijke situaties worden in dit basismodel niet behandeld. Elk netwerk  dient dit zelf in functie van de eigen situatie uit te werken.

3. TERMINOLOGIE EN DEFINITIES

1° “de AWW “ : de wet van 18 september 2017 tot voorkoming van het witwassen van geld  en de financiering van terrorisme en tot beperking van het gebruik van contanten;  2° “witwassen van geld “: zoals bedoeld in artikel 2 van de AWW;  3° “ financiering van terrorisme”: zoals bedoeld in artikel 3 van de AWW;  4° “WG/FT”: het witwassen van geld en de financiering van terrorisme;  5° “criminele activiteit”: zoals bedoeld in artikel 4,23° van de AWW;  6° “uiteindelijke begunstigde”: een natuurlijke persoon zoals bedoeld in artikel 4,27° van de  AWW;  7°”politiek prominente personen”: een persoon zoals bedoeld in artikel 4,28° tot 30°van de  AWW;  8° “zakelijke relatie”: een zakelijke relatie zoals bedoeld in artikel 4, 33°, van de AWW;  9° « beroepsbeoefenaar”:  a) de natuurlijke personen of rechtspersonen die in België activiteiten uitoefenen en die  geregistreerd of ingeschreven zijn in het openbaar register van het Instituut van de  bedrijfsrevisoren overeenkomstig artikel 10 van de wet van 7 december 2016 tot  organisatie van het beroep van en het publiek toezicht op de bedrijfsrevisoren, de  natuurlijke personen stagiairs bedrijfsrevisoren van externe ondernemingen bedoeld in  artikel 11, § 3, van voormelde wet, alsook de auditkantoren en éénieder die het beroep van  wettelijk auditor uitoefent; of  b) de natuurlijke personen of rechtspersonen ingeschreven op de lijst van de externe  accountants en op de lijst van de externe belastingconsulenten bedoeld in artikel 5, § 1, van  de wet van 22 april 1999 betreffende boekhoudkundige en fiscale beroepen, alsook de  natuurlijke personen ingeschreven op de lijst van de stagiairs accountants en op de lijst van  de stagiairs belastingconsulenten bedoeld in artikel 4 van voormelde wet; of  c) de natuurlijke personen of rechtspersonen ingeschreven op de lijst van de externe  erkende boekhouders en op de lijst van de externe erkende boekhouders-fiscalisten  bedoeld in artikel 44, vijfde lid, van de voormelde wet van 22 april 1999, alsook de stagiairs  ingeschreven op de lijst van de externe erkende stagiairs boekhouders en op de lijst van de  externe erkende stagiairs boekhouders-fiscalisten bedoeld in hetzelfde artikel van de  voormelde wet van 22 april 1999;  10° “onafhankelijke auditfunctie “: de functie bedoeld in artikel 8 §2, 2° a) van de AWW om  de gedragslijnen, procedures en internecontrolemaatregelen te testen;  11° “verantwoordelijke persoon op het hoogste niveau “: zijnde een lid van het wettelijk  bestuursorgaan of, in voorkomend geval, van de effectieve leiding van de onderworpen  entiteiten die rechtspersonen zijn of indien de onderworpen entiteit een natuurlijke  persoon is, die persoon zelf, die belast is met de opdrachten zoals bedoeld in artikel 9, §1  van de AWW;  12° “AMLCO” (Anti-money laundering compliance officer): een persoon die belast is met de  opdrachten zoals bedoeld in artikel 9, §2, van de AWW;

13° “occasionele verrichting “: een verrichting zoals bedoeld in artikel 21, § 1, 2°, a) of b) van  de AWW ;  14° “atypische verrichting “: een verrichting die niet strookt met de kenmerken van de  cliënt, met het doel en de aard van de zakelijke relatie of van de betrokken verrichting, of  met het risicoprofiel van de cliënt, en die hierdoor verband zou kunnen houden met het  witwassen van geld of de financiering van terrorisme;  15° “lasthebber “: de persoon die de cliënt vertegenwoordigt in het kader van de zakelijke  relatie of de occasionele verrichting, onder andere de persoon of personen die de  opdrachtbrief ondertekent(en) of enige andere persoon die de bevoegdheid heeft om de  cliënt te verbinden  16° “medewerker”: de personeelsleden en de zelfstandige medewerkers, met inbegrip van  de beroepsbeoefenaars, die op regelmatige en voortdurende wijze werkzaamheden  uitvoeren in opdracht van de beroepsbeoefenaar;  17° “toezichtautoriteit”: autoriteit zoals bedoeld in artikel 85 van de AWW , namelijk:

a)  voor de leden van het het Instituut van de bedrijfsrevisoren: het College van  toezicht op de bedrijfsrevisoren;  b)  voor de leden van het Instituut van de accountants en de belastingconsulenten: het  Instituut van de accountants en de belastingconsulenten;  c)  voor de leden van het Beroepsinstituut van erkende boekhouders en fiscalisten: het  Beroepsinstituut van erkende boekhouders en fiscalisten.

18° “kantoor”:

a) voor de leden van het Instituut van de bedrijfsrevisoren: een rechtspersoon of een

andere entiteit met om het even welke rechtsvorm, andere dan een natuurlijk  persoon, ingeschreven in het openbaar register van de bedrijfsrevisoren;  b) voor de leden van het Instituut van de accountants en de belastingconsulenten: de

organisatorische eenheid

1) waarbinnen één of meer beroepsbeoefenaars voor een cliënt

beroepsactiviteiten uitoefenen, zoals bedoeld in artikelen 34 en 38 van de  wet van 22 april 1999 betreffende de boekhoudkundige en fiscale  beroepen;  2) en die bestaat uit ofwel uitsluitend één vestiging ofwel meerdere

vestigingen waarbinnen dezelfde werkmethodes van toepassing zijn.  c) voor de leden van het Beroepsinstituut van erkende boekhouders en fiscalisten:

de organisatorische eenheid  1) waarbinnen één of meer beroepsbeoefenaars voor een cliënt

beroepsactiviteiten uitoefenen, als bedoeld in artikelen 49 en 38 van de wet  van 22 april 1999 betreffende de boekhoudkundige en fiscale beroepen;  2) en die bestaat uit, ofwel uitsluitend één vestiging, ofwel meerdere vestigingen

waarbinnen dezelfde werkmethodes van toepassing zijn.

19° “netwerk”: de grotere structuur waartoe een beroepsbeoefenaar of kantoor behoort:

a) die op samenwerking is gericht en  b) die duidelijk is gericht op winst- of kostendeling, of het delen van

gemeenschappelijke  eigendom,  zeggenschap  of  bestuur,  een

gemeenschappelijk beleid en procedures inzake kwaliteitsbeheersing,  een gemeenschappelijke bedrijfsstrategie, het gebruik van een  gemeenschappelijke merknaam of een aanzienlijk deel van de  bedrijfsmiddelen; en    20° “derde zaakaanbrenger”: zoals bedoeld in artikel 43 van de AWW

21° “CFI”: De Cel voor Financiële Informatieverwerking, zoals bedoeld in artikel 76 van de  AWW ;

4. ALGEMENE INLEIDING

Wettelijk kader

## Art. 7

AWW :  Behoudens andersluidende bepalingen gaan de bevoegde autoriteiten en de

onderworpen entiteiten, overeenkomstig de bepalingen van deze wet, over tot de  tenuitvoerlegging op gedifferentieerde wijze van de preventieve maatregelen bedoeld in  boek II, in functie van hun evaluatie van de WG/FT-risico's .

## Art. 8

AWW :  § 1. De onderworpen entiteiten ontwikkelen en passen doeltreffende

gedragslijnen, procedures en interne controlemaatregelen toe die evenredig zijn met hun aard  en omvang.

In ons kantoor

Deze handleiding is in ons kantoor in voege sinds …/…../2019 en werd goedgekeurd door  de verantwoordelijke op het hoogste niveau van het kantoor].

In deze handleiding wordt een risicogebaseerde benadering toegepast in functie van de  evaluatie van de WG/FT-risico’s en dit zowel op het niveau van ons kantoor [naam] als op  het niveau van de cliënten, alsook van de diensten en van de verrichtingen.

Deze handleiding heeft tot doel om de in ons kantoor toe te passen doeltreffende  gedragslijnen, procedures en interne controlemaatregelen vast te leggen inzake de strijd  tegen het witwassen van geld en de financiering van terrorisme, met inbegrip van de te  gebruiken  werkdocumenten.  Deze  gedragslijnen,  procedures  en  interne  controlemaatregelen dienen te worden geïntegreerd in de gebruikelijke controles van de  dossiers en de opdrachten, met als opzet enerzijds, de verplichtingen van de  beroepsbeoefenaars en alle medewerkers betreffende de preventieve AWW na te komen,  en anderzijds om door middel van de formalisering van de uitgevoerde taken te kunnen  aantonen dat het door de AWW vereiste klantenonderzoek werd uitgevoerd en het geheel  van de wettelijke en normatieve verplichtingen werd nagekomen.

Elke beroepsbeoefenaar en medewerker van ons kantoor wordt geacht zich in te zetten  voor de toepassing, van de huidige interne procedures, teneinde enerzijds risico’s op een  misbruik van ons kantoor voor witwasdoeleinden of de financiering van terrorisme  maximaal te beperken, en anderzijds het risico te beperken dat onze tuchtrechtelijke,  burgerrechtelijke of strafrechtelijke aansprakelijkheid in het gedrang zou komen in geval  een dergelijke verrichting zich zou voordoen bij een van onze klanten.

Teneinde te vermijden in de meest algemene zin dat ons kantoor een zakelijke relatie zou  aangaan met dubieuze personen, in de zin van de betreffende wetgeving zal bij het  klantenacceptatiebeleid en de aanvaarding van opdrachten de nodige voorzorg worden  genomen en de gepaste waakzaamheid aan de dag gelegd.

De punten 7 tot 10 en 13 tot 18 van deze handleiding zijn bijzonder relevant voor alle  medewerkers, met dien verstande dat medewerkers niet vrijgesteld worden om kennis te  nemen van de andere punten.

De punten 1 tot 6, 11 en 12 zijn eerder bestemd ter attentie van de AMLCO et de  verantwoordelijke persoon op het hoogste niveau.

In geval een medewerker zich vragen stelt bij een verrichting, bij een cliënt of meer  algemeen bij de toepassing van de AWW of over een vermoeden van witwassen, zal deze  contact opnemen met één van de personen vermeld in het volgende punt.

5. DE KANTOORORGANISATIE EN DE AWW

Wettelijk kader

## Art. 8

§ 2 van de AWW  voorziet in “[...]b)  procedures om bij de aanwerving en de

aanstelling van personeelsleden of de aanwijzing van agenten of distributeurs na te gaan of  deze personen blijk geven van passende betrouwbaarheid, rekening houdend met de risico's  die verbonden zijn aan de uit te voeren opdrachten en functies ; [...] en dat de  personeelsleden van ons kantoor opleiding krijgen en gesensibiliseerd worden met  betrekking tot het voorkomen van het witwassen van geld en de financiering van  terrorisme. Dit geldt voor alle personeelsleden die door de taken die zij verrichten, of door  de verrichtingen die zij uitvoeren, het risico lopen te worden geconfronteerd met pogingen  tot witwassen van geld of met financiering van terrorisme.

## Art. 9

AWW  voorziet dat er in elk kantoor twee functies moeten voorzien worden: een

verantwoordelijke op het hoogste niveau en een AMLCO.

In elke kantoor waarin minstens 10 beroepsbeoefenaars een activiteit uitoefenen en/of een  deelname hebben in het kantoor en/of lid zijn van het bestuursorgaan moet de AMLCO een  onderscheiden persoon zijn van de verantwoordelijke persoon op het hoogste niveau.

In geval voor bovenstaande functies geen twee onderscheiden personen werden  aangesteld, vervult de persoon die werd aangesteld om beide functies uit te oefenen zelf  de opdrachten van beide functies, zoals infra omschreven.

De verantwoordelijke op het hoogste niveau

## Art. 9

van de AWW stelt dat elke beroepsbeoefenaar die een rechtspersoon is een

verantwoordelijke persoon op het hoogste niveau moet aanstellen. In geval de  beroepsbeoefenaar een natuurlijke persoon is, wordt de voornoemde functie door die  natuurlijke persoon zelf uitgeoefend.

De rol van de verantwoordelijke persoon op het hoogste niveau, is om te waken over de  toepassing en de naleving van de bepalingen van de AWW en de besluiten en reglementen  genomen ter uitvoering ervan en, in voorkomend geval, van de bestuursrechtelijke  beslissingen genomen op grond van deze bepalingen.

De AMLCO

Bovendien moet elke beroepsbeoefenaar in toepassing van de art. 9, §2 van de AWW een  AMLCO aanduiden. Deze persoon moet voldoen aan de in artikel 9 AWW vermelde  voorwaarden.

De opdracht van een AMLCO omvat het toezicht op de tenuitvoerlegging van de  gedragslijnen, procedures en internecontrolemaatregelen inzake AWW in ons kantoor,  inclusief de analyse van de atypische verrichtingen evenals de opstelling van de

desbetreffende schriftelijke verslagen overeenkomstig de artikelen 45 en 46 van de AWW  teneinde er zo nodig het passend gevolg aan te geven krachtens artikel 47 van de AWW,  inclusief de mededeling van de informatie bedoeld in artikel 54 van de AWW aan de CFI.  Hij zorgt bovendien voor de sensibilisering en de opleiding van het personeel.    AMLCO, beroepsbeoefenaar of niet ?

De AMLCO is in principe een beroepsbeoefenaar. In functie van de structuur, de organisatie  en de grootte van de onderworpen entiteit kan de functie van de AMLCO worden  toevertrouwd aan een andere persoon dan een beroepsbeoefenaar, op voorwaarde dat  deze persoon voldoende is gekwalificeerd (zoals omschreven in artikel 9, §2 AWW) om  deze functie uit te oefenen. In het geval dat de AMLCO en de verantwoordelijke persoon  op het hoogste niveau dezelfde persoon zijn, dient deze een beroepsbeoefenaar, natuurlijk  persoon, te zijn

De aanstelling van de verantwoordelijke op het hoogste niveau en/of van de AMLCO  in ons kantoor:

OPMERKING VOORAF: Elk kantoor dient te kijken welke van de onderstaande punten van  toepassing zijn en de overige te schrappen.

5.4.1. Minder dan 10 beroepsbeoefenaars: de AMLCO en de verantwoordelijke persoon op  het hoogste niveau zijn dezelfde persoon

Gezien er in ons kantoor minder dan 10 beroepsbeoefenaars zijn in voornoemde zin,  worden beide voornoemde functies uitgeoefend door één en dezelfde persoon, met name  door de heer/mevrouw ………………………., die de beroepshoedanigheid heeft van  …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

➢ Optioneel: indien betrokkene onbeschikbaar is kan men contact nemen met:

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

5.4.2. Minder dan 10 beroepsbeoefenaars – de AMLCO en de verantwoordelijke zijn  onderscheiden personen

Hoewel er in ons kantoor minder dan 10 beroepsbeoefenaars zijn in voornoemde zin wordt  vanaf …………. beslist dat voor beide voornoemde functies twee onderscheiden  personen worden aangeduid, te weten :

➢ Voor de functie van verantwoordelijke persoon op het hoogste niveau wordt

aangeduid de heer/mevrouw … die de beroepshoedanigheid heeft van  …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

➢ Voor de functie van AMLCO ………………………….. wordt aangeduid de

heer/mevrouw … die de beroepshoedanigheid heeft van …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

Optioneel : indien betrokkene onbeschikbaar is kan men contact nemen met:

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

5.4.3. Minstens 10 beroepsbeoefenaars

Gezien er in ons kantoor meer dan 10 beroepsbeoefenaars zijn in voornoemde zin worden  beide voornoemde functies door twee onderscheiden personen waargenomen

➢ Voor de functie van verantwoordelijke persoon op het hoogste niveau wordt

aangeduid de heer/mevrouw … die de beroepshoedanigheid heeft van  …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

➢ Voor de functie van AMLCO ………………………….. wordt aangeduid de

heer/mevrouw … die de beroepshoedanigheid heeft van …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

Optioneel : indien betrokkene onbeschikbaar is kan men contact nemen met:

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

De onafhankelijke auditfunctie

Alle kantoren en netwerken dienen zelf te beslissen al dan niet een onafhankelijke  auditfunctie  te  installeren.  Deze  auditfunctie  is  te  onderscheiden  van  de  commissarisfunctie.

Bij deze beslissing dient men niet alleen rekening te houden met het aantal medewerkers  (criterium van 100 beroepsbeoefenaars )doch ook met het AML-risico waaraan het  kantoor of netwerk is blootgesteld.    In ons kantoor is er wel/niet (schrappen wat niet past) voorzien in een onafhankelijke  audit.

De vermelding van de identiteit van de persoon belast met de auditfunctie is facultatief

-  Deze functie wordt uitgeoefend door de heer/mevrouw … die de  beroepshoedanigheid heeft van …………….

Naam + voornaam

Adres

Tel/ GSM

E-mail

Aangesteld door

Op …./…./2….. en dit voor een periode van … of onbepaalde duur

De kantoren en netwerken die vandaag reeds beschikken over een onafhankelijke interne  of externe auditfunctie (onderscheiden van de commissarisfunctie) dienen het testen van  gedragslijnen, procedures en internecontrolemaatregelen inzake AWW toe te voegen  aan de opdracht van de auditfunctie.    De twee volgende punten handelen over personeel en medewerkers. Indien het kantoor  geen personeel of medewerkers heeft mogen deze twee punten worden geschrapt of

hier gewoon worden gemeld : geen personeel of medewerkers. Indien later het kantoor  personeel zou aanwerven of een beroep doen op medewerkers moeten deze punten wel  worden geïntegreerd in onze handleiding.

Aanwerving & aanstelling van personeel en medewerkers

Bij de aanwerving of promotie van personeel of medewerkers zal het kantoor steeds  nazien of betrokkenen over de nodige bekwaamheid en moraliteit beschikken voor de  uitoefening van hun taak en niet alleen in het algemeen doch in het bijzonder op het vlak  van de AWW en dit in functie van het risico dat verbonden is aan de uit te voeren taak en  functie.    In uitvoering van artikel 8 van de AWW voert ons kantoor volgende procedure in bij de  aanwerving of promotie van medewerkers en bij de aanwijzing van onze  vertegenwoordigers:    Voorbeeld : (het kantoor vult hier haar eigen aanwervingsprocedure in)

-  In het voorafgaand gesprek wordt gepeild naar de kennis van de kandidaat inzake  de AWW. Hierbij wordt rekening gehouden met het ervaringsniveau en de  toekomstige functie. Hierbij kunnen volgende vragen worden gesteld:

o Weet u of ons beroep onderworpen is aan bepaalde verplichtingen inzake

de AWW?  o Heeft u een vorming en/of onderwijs genoten inzake de AWW?  o Weet u wat een witwasmelding is  -  Peilen naar de technische competenties inzake het herkennen van verdachte  transacties, in het kader van de AWW, alsook de deontologische ingesteldheid  daartegenover  -  Voorafgaand wordt aan de betreffende persoon gevraagd een 'uittreksel uit het  strafregister' voor te leggen, afgeleverd door de gemeente van de woonplaats.  De opgevraagde uittreksels mogen niet bewaard worden en worden na nazicht  vernietigd.    In elk geval wordt elke nieuwe medewerker door de verantwoordelijke voor de  toepassing van de AWW, door het bestuur of door de dossierverantwoordelijke  minstens steeds in kennis gesteld van de in ons kantoor toepasselijke procedures en  documenten (met inbegrip van deze handleiding). In functie van de vaardigheden en de  vereisten van de functie zal eventueel in een aanvullende opleiding worden voorzien.

Opleiding en sensibilisering van het personeel en medewerkers

5.7.1. Inleiding

De organisatie van deze vorming gebeurt door de AMLCO. Het volgen van deze  opleidingen is verplicht voor alle betrokkenen en uitzonderingen worden niet toegestaan.

5.7.2. Inhoud van de opleiding.

De concrete inhoud van de opleidingsprogramma’s is erop gericht om alle medewerkers:

➢  De interne procedures inzake identificatie en identiteitsverificatie van de klanten,  hun lasthebbers en uiteindelijke begunstigden, alsook het klantenonderzoek met  betrekking tot het voorwerp en de aard van de zakenrelatie of verrichting aan te  leren;

➢  De binnen het kantoor geldende risicogeoriënteerde aanpak aan te leren;

➢  De verrichtingen en feiten die met witwassen verband kunnen houden te leren  onderkennen;

➢  Te helpen de vereiste kennis te verwerven en de nodige kritische reflex te  ontwikkelen om atypische verrichtingen of feiten vast te stellen;

➢  Te helpen de nodige kennis van de interne procedures te verwerven om op  passende wijze te reageren wanneer zij met dergelijke verrichtingen of feiten  worden geconfronteerd;

➢  Op de hoogte te houden van de evoluties, zowel op wettelijk als op reglementair  vlak en van de gevolgen van deze wijzingen voor de interne procedures;

De concrete inhoud wordt ingevuld in functie van taken die zij verrichten, of naargelang ze  door de verrichtingen die zij uitvoeren, het risico lopen te worden geconfronteerd met  pogingen tot witwassen van geld of met financiering van terrorisme.

5.7.3. Vorm en frequentie

Voor de bestaande medewerkers wordt minstens éénmaal per 3 jaar een opleiding  voorzien. Deze opleiding kan intern of extern gebeuren en is verplicht. De medewerkers  worden tijdig in kennis gesteld van de datum. Indien de omstandigheden dit vereisen  kunnen er steeds bijkomende opleidingen voorzien worden en/of zal de informatie via een  interne nota worden verspreid.

Ook de AMLCO en alle beroepsbeoefenaars van het kantoor moeten ter zake de nodige  opleidingen volgen. De beroepsbeoefenaars kunnen deze vormingen kaderen in hun  deontologische verplichtingen inzake permanente vorming. Zij dienen ter zake rekening te  houden met eventuele bijzondere richtlijnen van hun Instituut wat betreft de verhouding  tussen de verschillende opleidingsvormen.

5.7.4. Documentatie - informatie

De toepassing van de AWW en deze handleiding vereisen onze permanente aandacht.    Het kantoor stelt daarom haar medewerkers volgende informatie ter beschikking op …….  (verwijzen naar plaats in bibliotheek of intranet of andere plaats waar alles ter beschikking  is):

-  Huidige handleiding  •  De AWW  •  Publicaties (bv artikelen …..)  •  Syllabi van de basisvorming en de gevolgde opleidingen  •  De interne nota’s  •  E-learning-modules  •  ……..    Elk kantoor kan deze lijst zelf bepalen en/of aanvullen.

6. ALGEMENE RISICOBEOORDELING VAN HET KANTOOR

Wettelijk kader

De artikelen 16 tot 18 van de AWW leggen op dat elke beroepsbeoefenaar een algemene  risicobeoordeling van het kantoor dientuit te voeren.

Inleiding

Ons kantoor dient uit te zoeken aan welke WG/FT-risico’s wij zijn, of zouden kunnen  worden, blootgesteld als gevolg van het aangaan van een zakelijke relatie of het verrichten  van een occasionele transactie en in functie hiervan dient het kantoor passende  maatregelen te voorzien om die risico’s te kunnen beheren.

Bij deze beoordeling houden wij tevens rekening met de kenmerken van de cliënten,  diensten of verrichtingen die we aanbieden, de betrokken landen of geografische  gebieden .

Bij deze algemene risicobeoordeling houden wij ook rekening met de variabelen vermeld  in de bijlagen bij de AWW (zie punt 21):

In het bijzonder dient rekening gehouden te worden met volgende variabelen (bijlage I)

1° het doel van een rekening of een relatie;

2° de omvang van de activa die door een cliënt worden gedeponeerd of de omvang van de  gesloten verrichtingen;

3° de regelmaat of de duur van de zakelijke relatie.

Tevens wordt rekening gehouden met de in de AWW opgenomen risicoverlagende  factoren (bijlage II) en de risicoverhogende factoren (bijlage III).

Deze bedrijfsbrede beoordeling staat los van de individuele risicobeoordeling die we bij  elke cliënt dienen toe te passen (zie punt 8.).

Bronnen van informatie:

In ons kantoor nemen wij de volgende bronnen van informatie in overweging: Hierna een  voorbeeld

➢ De supranationale risicobeoordeling door de Europese Commissie;  ➢ Informatie van de overheid, zoals de nationale risicobeoordeling, voor zover

beschikbaar,  ➢ De sectorale risicobeoordeling, voor zover beschikbaar  ➢ Memories van toelichting bij relevante wetgeving;  ➢ De informatie vanwege de instituten van de boekhoudkundige en fiscale

beroepen  ➢ Andere informatie zoals dreigingsrapporten, waarschuwingen en typologieën

gepubliceerd door de CFI

➢ Informatie verkregen in het kader van de toepassing van ons klantenacceptatie

en opvolgingsbeleid  ➢ Informatie van geloofwaardige en betrouwbare openbare bronnen  ➢ Media  Cursief: Wettelijke verplichting om hier rekening mee te houden

De beoordeling

Er bestaat geen unieke methodologie om de blootstelling van een kantoor aan het WG/FT- risico in concreto uit te voeren. Er zijn verschillende manieren mogelijk om de  aandachtspunten van de wetgever in concreto toe te passen.    Daarom stellen wij twee methodes voor. Beide methodes behandelen alle  aandachtspunten van de wetgever doch op een verschillende manier.    Model 1: dit is gewoon een document waarin aan de hand van een aantal vragen een  algemeen beeld kan gevormd worden van de al dan niet aanwezigheid van risicofactoren.  De vragen zijn gemaakt op basis van de nationale risicoanalyse van de CFI, alsook van  risicofactoren uitgewerkt door de Financiële actiegroep (FAG) Dit model kan u afzonderlijk  bewaren of gewoon in dit punt 6.4. toevoegen -    Model 2. Dit is een Excel tabel zoals die werd uitgewerkt door de FSMA ten aanzien van de  onderworpen entiteiten die onder haar toezicht vallen. Deze tabel werd bijgewerkt in  functie van de economische beroepen en laat ook toe van de blootstelling te visualiseren.  De tabel kan u downloaden via de website van het Instituut. Als u dit model gebruikt kan u  hier dan gewoon een link leggen naar de plaats waar u de ingevulde tabel in uw systeem  bewaard heeft.    U kan beide modellen achteraan (respectievelijk punt 20 en punt 21) vinden.

Deze modellen vormen een hulpmiddel waarvan het gebruik geen verplicht karakter heeft.  Indien u er gebruik van maakt, moet deze, indien nodig, worden aangepast, rekening  houdend met de specifieke kenmerken van uw activiteit. U kan er ook voor opteren om uw  algemene risicobeoordeling uit te voeren volgens een andere methode maar welke  methode u ook kiest, u zal steeds in staat moeten zijn om, op basis van documenten, aan  de bevoegde toezichtautoriteit aan te tonen dat de gevolgde methode toelaat om te  voldoen aan de verplichtingen van de AWW.

Actualisatie

In ons kantoor zorgen wij er op volgende wijze voor dat onze bedrijfsbrede  risicobeoordeling actueel blijft:

➢  Indien wij ervan op de hoogte zijn dat een nieuw risico is opgekomen, of een  bestaand risico is toegenomen, wordt dit zo snel mogelijk weerspiegeld in de  algemene alsook in individuele risicobeoordelingen.

➢  De AMLCO zal regelmatig [bv éénmaal per jaar) bekijken of huidige  risicobeoordeling nog overeenstemt met de activiteiten van het kantoor en dit  toelichten in het jaarverslag.

Besluit

Op basis van het bovenstaande zijn wij van oordeel dat in het algemeen de blootstelling  aan WG/FT-risico’s laag is en wel hierom:    Voorbeeld: In het algemeen is het risico laag. Het kantoor verleent hoofdzakelijk diensten  inzake boekhouding, opmaak en neerlegging van jaarrekeningen, fiscale aangiftes (PB,  VennB en btw) en beperkt fiscaal advies voor een cliënteel met wie zij een langdurige  zakelijke relatie heeft. Het cliënteel is, op een beperkt aantal uitzonderingen na, in  hoofdorde actief in sectoren die geen hoger risico vertonen. Het cliënteel is zonder  uitzondering gevestigd in België en hun activiteiten vinden plaats in België en landen van  de EU. Het kantoor neemt enkel cliënten aan na een face-to-face contact en in belangrijke  mate wanneer zij werden aangebracht door andere cliënten of confraters die gekend zijn.    Maar:  Voorbeeld: Het kantoor verleent hoofdzakelijk diensten inzake boekhouding, opmaak en  neerlegging van jaarrekeningen, fiscale aangiftes (PB, VennB en btw) en beperkt fiscaal  advies voor een cliënteel met wie zij een langdurige zakelijke relatie heeft en is het risico  op blootstelling aan WG/FT laag. Evenwel heeft het kantoor ook te maken met een aantal  factoren die een indicator zijn van hoog risico. Er is cliënteel actief in een aantal sectoren  die een hoger risico vertonen. Er is cliënteel dat actief is buiten de EU en ook in een aantal  landen met hoog risico. Bij die cliënten zal identificatie op afstand de regel zijn. Het kantoor  heeft dan ook voorzien in bijkomende maatregelen om in casu een verscherpt  cliëntenonderzoek te voeren.

7. WG/FT-RISICO: BEOORDELING – CATEGORISERING – MAATREGELEN - OPVOLGING

Algemene Inleiding

Het kantoor kijkt naar het totaal van de WG/FT-risicofactoren die voor de cliënt werden  geïdentificeerd en die, tezamen, het niveau van het aan een zakelijke relatie of occasionele  transactie verbonden WG/FT-risico bepalen.

➢  De risicobeoordeling mag niet wordt beïnvloed door economische of  winstoverwegingen;

➢  De risicobeoordeling mag niet leiden tot een situatie waarin het onmogelijk is om  een zakelijke relatie in te delen als een relatie met een hoog risico.

De risicobeoordeling kan leiden tot een beslissing van niet-aanvaarding van zakelijke  relaties of weigeren van een occasionele verrichting. Deze beslissingen worden steeds  gedocumenteerd en bewaard.

Categorisering van zakelijke relaties en occasionele verrichtingen

Na de beoordeling categoriseert ons kantoor zijn zakelijke relaties en occasionele  verrichtingen in categorieën volgens het waargenomen niveau van het WG/FT-risico.

Ons kantoor hanteert ter zake volgende categorieën: standaard, laag of hoog. [Mits  aanpassing van de hiernavolgende interne gedragslijnen kan een kantoor ook andere  indelingen uitwerken, op voorwaarde dat er minstens steeds één categorie hoog risico en  één laag risico is.]

De passende maatregelen in functie van het risico

Hier worden de maatregelen omschreven die in functie van voormelde risicocategorieën  worden genomen door het kantoor.

7.3.1. Vereenvoudigd cliëntenonderzoek

In situaties waarin het aan een zakelijke relatie verbonden WG/FT-risico als laag is  beoordeeld, past ons kantoor een vereenvoudigd klantenonderzoek toe.

De maatregelen die in ons kantoor dan worden toegepast zijn:    Dit is louter een voorbeeld. Elk kantoor dient dit individueel te beoordelen en uit te  werken:

➢  Aanpassing van het tijdstip van verificatie: de identiteit van de cliënt of de UBO  te verifiëren na het aangaan van de zakelijke relatie en mits aan de andere  voorwaarden vermeld in punt 10;

➢  Aanpassing van de hoeveelheid informatie die wordt ingewonnen voor  identificatie-, om met voldoende zekerheid de ene persoon van de andere  persoon te kunnen onderscheiden;

➢  Aanpassing van de bronnen die worden geraadpleegd om de informatie te  verifiëren;

➢  Aanpassing van de frequentie van actualiseringen van het klantenonderzoek en  evaluaties van de zakelijke relatie, bijvoorbeeld door deze alleen uit te voeren  wanneer zich triggergebeurtenissen voordoen, zoals wanneer de cliënt een  nieuwe dienst wil afnemen.

In geval van twijfel of de verkregen informatie waarheidsgetrouw is, moet het  vereenvoudigd klantenonderzoek worden stopgezet en moet de risicobeoordeling  hernomen worden.

7.3.2. Verscherpt cliëntenonderzoek

In situaties met een hoger risico past ons kantoor verscherpt cliëntenonderzoek toe om de  betreffende risico’s op passende wijze te beheersen en te beperken.

Dit zijn voorbeelden van situaties waarin de wetgever in elk geval een verscherpt  cliëntenonderzoek vereist.

➢ Indien de cliënt, diens lasthebber, of de UBO van de cliënt, een PPP (Politiek

Prominent Persoon) is;

➢ Alle complexe en ongebruikelijk grote transacties, of ongebruikelijke

transactiepatronen, die geen duidelijk economisch of rechtmatig doel hebben.

➢ indien een onderneming zaken doet met natuurlijke personen of juridische

entiteiten welke zich bevinden in derde landen met een hoog risico.

Elk kantoor kan hier dus op basis van de eigen beoordeling situaties toevoegen waarin  een verscherpt onderzoek wordt toegepast en/of bijkomende maatregelen invoeren.  Een voorbeeld kan men vinden in punt 7.3.4..

7.3.2.1. Politiek prominente personen

Om te bepalen of een persoon al dan niet een PPP is zal het kantoor o.a. gebruik maken  van Google en www.openthebox.be . Als het kantoor heeft vastgesteld dat een cliënt of  UBO een politiek prominente persoon is, moet men altijd:

➢  Passende maatregelen nemen om de bron van het vermogen en de bron van de  geldmiddelen die in de zakelijke relatie worden gebruikt, vast te stellen, zodat de  beroepsbeoefenaar zich ervan kan vergewissen dat hij niet de opbrengsten van  corruptie of andere criminele activiteiten moet verwerken. De maatregelen die  ons kantoor dient te nemen om de bron van het vermogen en de bron van de  geldmiddelen van de PPP vast te stellen, zullen afhangen van de hoogte van het  risico dat is verbonden aan de zakelijke relatie. Indien het aan de relatie met een  PPP verbonden risico bijzonder hoog is, verifieert de beroepsbeoefenaar de bron  van het vermogen en de bron van de middelen op basis van betrouwbare en  onafhankelijke gegevens, documenten of informatie.

➢  Van de verantwoordelijke persoon op het hoogste niveau goedkeuring verkrijgen  voor het aangaan, of voortzetten, van een zakelijke relatie met een PPP.

➢  Bij het maken van de afweging of een relatie met een PPP kan worden  goedgekeurd, baseert de V ERANTWOORDELIJKE OP HET HOOGSTE NIVEAU 1 in ons kantoor  zijn beslissing op het niveau van het WG/FT-risico waaraan ons kantoor wordt  blootgesteld als het de betreffende zakelijke relatie aangaat, en op de mate  waarin ons kantoor is toegerust om dat risico doeltreffend te beheersen.

➢  Zowel verrichtingen als het aan de zakelijke relatie verbonden risico doorlopend  verscherpt monitoren. Ons kantoor identificeert ongebruikelijke transacties en  evalueert regelmatig de informatie waarover we beschikken om ervoor te zorgen  dat alle nieuwe of naar boven komende informatie die de risicobeoordeling zou  kunnen beïnvloeden, tijdig wordt geïdentificeerd.

Ons kantoor moet al deze maatregelen toepassen op PPP’s, hun familieleden en personen  bekend als hun naaste geassocieerden, en past de omvang van deze maatregelen aan op  basis van risicogevoeligheid.

7.3.3. Ongebruikelijke transacties

Ons kantoor past maatregelen van verhoogde waakzaamheid toe in volgende gevallen:

➢ Ze groter zijn dan wat ons kantoor op grond van de kennis van de cliënt, de zakelijke

relatie of de categorie waartoe de cliënt behoort, normaal zou verwachten;

➢ Ze een ongebruikelijk of onverwacht patroon vertonen vergeleken met de normale

activiteiten van de cliënt of met de transactiepatronen die verband houden met

vergelijkbare  cliënten,  transacties  of  diensten;

➢  Ze zeer complex zijn vergeleken met andere, vergelijkbare transacties die verband  houden met soortgelijke typen cliënten, of diensten.

en ons kantoor zich niet bewust is van een economisch of rechtmatig doel of  twijfelt aan waarheidsgetrouwheid van de ontvangen verstrekte informatie,  passen wij verhoogde waakzaamheid toe.

De volgende maatregelen dienen voldoende te zijn om ons kantoor te helpen vaststellen  of deze transacties aanleiding geven tot verdenking, en moeten ten minste het volgende  omvatten:

➢  Het nemen van redelijke en toereikende maatregelen om de achtergrond en het  doel van deze transacties te begrijpen, bijvoorbeeld door de bron en de  bestemming van de geldmiddelen vast te stellen of door meer informatie over de  zakelijke activiteit van de cliënt te vergaren om duidelijkheid te verkrijgen over de  waarschijnlijkheid dat de cliënt dergelijke transacties verricht; en

➢  Het frequenter en met meer aandacht voor details monitoren van de zakelijke  relatie en erop volgende transacties.

7.3.4. Derde landen met een hoog risico en andere situaties met een hoog risico

In geval van zakelijke relaties met natuurlijke personen of rechtspersonen die gevestigd  zijn of verblijven in een land met een hoog risico en in alle andere situaties met een hoog  risico, dienen passende maatregelen van verhoogde waakzaamheid toegepast te worden  die voor elke situatie met een hoog risico passend zijn. Het passende type maatregelen,  met inbegrip van de omvang van de aanvullende informatie die wordt ingewonnen en het  passende type intensievere monitoring dat wordt uitgevoerd, zal afhangen van de reden  waarom een occasionele verrichting of een zakelijke relatie werd ingedeeld als een  verrichting of relatie met een hoog risico.

In situaties met een hoog risico zal ons kantoor steeds de hoeveelheid informatie die voor  klantenonderzoeksdoeleinden wordt ingewonnen aanvullen met:

i.  Het inwinnen en beoordelen van informatie over de reputatie van de cliënt of de UBO  door:

a)  Informatie over de vroegere en huidige zakelijke activiteiten van de cliënt of  de uiteindelijke begunstigde via [bv Google/ Companyweb ......]

b)   Zoekacties naar ongunstige berichtgeving in de media.

c)  Verbetering  van  de  kwaliteit  van  de  informatie  die  voor  klantenonderzoeksdoeleinden wordt ingewonnen om de identiteit van de  cliënt of de UBO op een onbetwistbare wijze te bevestigen.

In sommige gevallen, indien het risico dat aan de relatie is verbonden bijzonder hoog is,  kan het verifiëren van de bron van het vermogen en de bron van de geldmiddelen de enige  geschikte manier zijn om het risico te beperken. De bron van de geldmiddelen of van het  vermogen kan onder andere worden geverifieerd door de aangiften btw en  inkomstenbelasting,  kopieën  van  door  een  externe  accountant/bedrijfsrevisor  gecontroleerde rekeningen, loonstrookjes, openbare akten of berichtgeving in  onafhankelijke media te raadplegen.

ii . verhoging van de frequentie van evaluaties om zekerheid te verkrijgen dat ons kantoor  ook in de toekomst in staat blijft het aan de afzonderlijke zakelijke relatie verbonden risico  te beheersen of te concluderen dat de relatie niet langer aansluit bij de risicobereidheid  van ons kantoor, en transacties te helpen identificeren die nader moeten worden bekeken,  onder andere door:

a. de frequentie van evaluaties van de zakelijke relatie te verhogen om zekerheid te  verkrijgen of het risicoprofiel van de cliënt is gewijzigd en of het risico beheersbaar blijft;

b. de goedkeuring van de verantwoordelijke op het hoogste niveau te verkrijgen om de  zakelijke relatie aan te gaan of voort te zetten om te waarborgen dat de  verantwoordelijke persoon op het hoogste niveau zich bewust is van het risico waaraan  ons kantoor wordt blootgesteld, en een onderbouwde beslissing kan worden genomen  over de mate waarin ons kantoor dit risico kan beheersen;

c. de zakelijke relatie regelmatiger evalueren om ervoor te zorgen dat alle wijzigingen in  het risicoprofiel van de cliënt worden geïdentificeerd en beoordeeld en er, indien nodig,  actie wordt ondernomen;

of transacties frequenter of diepgaander monitoren om eventuele ongebruikelijke of  onverwachte transacties te identificeren die aanleiding tot een vermoeden van WG/FT  zouden kunnen geven. Dit kan inhouden dat de bestemming van geldmiddelen wordt  vastgesteld of dat zekerheid wordt verkregen over de reden van bepaalde transacties,  onder andere door vast te stellen dat het vermogen en de geldmiddelen van de cliënt  die in de zakelijke relatie worden gebruikt, niet de opbrengsten van criminele  activiteiten zijn en dat de bron van het vermogen en de bron van de geldmiddelen in  overeenstemming zijn met de kennis die ons kantoor heeft over de cliënt en de aard van  de zakelijke relatie.

Hieronder een voorbeeld van een aanvulling: het kantoor is van oordeel dat  identificatie op afstand een hoger risico met zich meebrengt en beschrijft de  bijkomende maatregelen die het in dit geval zal toepassen.

7.3.5. Bij identificatie op afstand

Als de cliënt niet fysiek aanwezig is, dit wil zeggen in het licht van de identiteitsverificatie  op afstand , zal het kantoor volgende passende maatregelen toepassen. De verificatie kan  gebeuren:

a) Hetzij aan de hand van een latere face-to-face-identificatie binnen de kortst

mogelijke termijn;

b) Hetzij aan de hand van een (Belgische of buitenlandse) elektronische

identiteitskaart;

c) Hetzij aan de hand van een gekwalificeerd certificaat 2 .

Het is belangrijk dat we ons de vraag stellen of de cliënt niet zijn toevlucht tot deze  procedure van identificatie op afstand neemt teneinde zijn echte identiteit te verhullen. Dit  risico zou weleens nog groter kunnen blijken te zijn als de aangegane relatie eenmalig van  opzet is. In dit geval helpt de identiteitsverificatie aan de hand van de elektronische  identiteitskaart of certificaat om het risico op een fout te verkleinen.

In alle gevallen, ongeacht de vraag of het gaat om de verificatie van de face-to-face- identificatie of de identificatie op afstand, kan de verificatie geldig worden gedaan aan de  hand van een kopie van elk bewijsstuk dat voortvloeit uit bijkomend onderzoek onder  andere via analyse- en zoekprogramma’s (‘search engines’) die ter beschikking worden  gesteld door onafhankelijke of officiële bronnen, of aan de hand van statuten, publicaties  en lijsten van internationale mandaten, voor zover:

a) De cliënt een laag risico WG/ FT inhoudt;

b) Die identificatie gedaan wordt met het oog op het aangaan van de zakenrelatie;

c) Het bewijsstuk pertinent en geloofwaardig is.

De keuze van het document ter staving en verificatie van de identificatiegegevens is  afhankelijk van de risicogevoeligheid van de cliënt: aldus is het gebruik van elk ander  hierboven vermeld bewijsstuk slechts geldig voor zover de identificatie erop gericht is een  zakenrelatie aan te gaan en de beroepsbeoefenaar van mening is dat noch de cliënt noch

2 : certificaten klasse III zoals bv Verisign, Globalsign, Isabel of gelijkwaardig

de zakenrelatie specifieke risico’s op witwassen inhoudt, rekening houdend met de  risicovariabelen die vastgesteld zijn in punt 8.

Indien risicobepaling niet mogelijk is

Ons kantoor gaat geen zakelijke relatie aan indien we niet kunnen voldoen aan de  voorschriften inzake klantenonderzoek, indien we er niet van overtuigd zijn dat het doel  en de aard van de zakelijke relatie rechtmatig zijn, of indien wij er niet van overtuigd zijn  dat wij het risico dat ons kantoor voor WG/FT-doeleinden wordt gebruikt, doeltreffend  kunnen beheersen.

Indien een dergelijke zakelijke relatie al bestaat, beëindigen wij deze of schorten wij elke  dienstprestatie op totdat de relatie kan worden beëindigd.

In dergelijk geval dient hiervan steeds melding gemaakt te worden aan de AMLCO. Men  kan hiervoor gebruik maken van het formulier in de modellenbundel.

De AMLCO zal ter zake een verslag (zie modellenbundel) opmaken en indien er redelijke  gronden zijn om te vermoeden dat er sprake is van een poging tot WG/FT, zal dit door de  AMLCO worden gemeld aan de CFI.

Actualisatie

In ons kantoor zorgen wij er op volgende wijze voor dat onze individuele  risicobeoordelingen actueel blijven:

➢  Voor cliënten en UBO’s met standaardrisico of met laag risico dient minstens om  de drie jaar het risico op WG/FT en de identificatiestukken te worden geverifieerd  en desgevallend geactualiseerd, in casu uiterlijk op 31 december van het derde  jaar volgend op de aanvaarding van de cliënt

➢  Voor cliënten met hoog risico moet de actualisering van de risicobeoordeling  plaatsvinden uiterlijk op 31 december van elk jaar volgend op het jaar van  aanvaarding van de cliënt.

➢  Indien wij ervan op de hoogte zijn dat een nieuw risico is opgekomen, of een  bestaand risico is toegenomen, wordt dit zo snel mogelijk weerspiegeld in de  risicobeoordelingen.

Net als de oorspronkelijke risicobeoordelingen is elke actualisering van een  risicobeoordeling en elke aanpassing van de bijbehorende klantenonderzoeksmaatregelen  maatregelen evenredig met en in verhouding tot het vastgestelde WG/FT-risico.

Bijhouden van gegevens risicobeoordeling

Ons kantoor registreert en documenteert zijn individuele risicobeoordelingen (model  formulier in modellenbundel) van zakelijke relaties, alsook alle wijzigingen die worden  aangebracht in risicobeoordelingen in het kader van de evaluatie en monitoring ervan, om  ervoor te zorgen dat wij tegenover de bevoegde autoriteiten kunnen aantonen dat ons  risicobeoordelingen en de daaraan verbonden risicobeheermaatregelen adequaat zijn !

8. RISICOBEOORDELING CLIENTEN – DIENST – VERRICHTINGEN

Wettelijk kader

## Art. 19

§ 2. AWW  voorziet in de toepassing van waakzaamheidsmaatregelen gebaseerd op

een individuele beoordeling van de WG/FT-risico’s verbonden aan een cliënt, dienst of  verrichting.

Algemene principes/ in de praktijk

Er bestaat geen unieke methodologie om aan een cliënt, dienst of verrichting een  welbepaalde witwasrisicogevoeligheid toe te kennen. Het hiernavolgende interne systeem  is gericht op de inschatting en het beheer van witwasrisico’s, alsook op het bepalen van  het  risicoprofiel  van  elke  cliënt,  dienst  of  verrichting.    Elke cliënt, dienst of verrichting wordt ingeschaald op een standaard, laag of hoog  risicoprofiel. De inschaling gebeurt in principe op het niveau standaard, tenzij er  omstandigheden, behoorlijk geïdentificeerd en onderbouwd, zijn waardoor een inschaling  op een hoger of lager risiconiveau dient gedaan te worden. Ter zake wordt verwezen naar  de  hierna  toegelichte  criteria.    Cliënten, diensten of verrichtingen die een hoog WG/FT risico inhouden of met zich mee  kunnen brengen, vereisen een voorafgaand grondig onderzoek en elke beslissing dient ter  zake genomen te worden overeenkomstig punt 9 (acceptatiebeleid) van dit document.

De risicobeoordeling van de cliënt betreft niet alleen de identiteit doch ook het voorwerp  en de verwachte aard van de zakenrelatie. Met het oog hierop wordt kennisgenomen van  het type diensten waarvoor de cliënt een beroep op ons kantoor doet, alsook van alle  relevante informatie die inzicht kan verschaffen in de doelstelling die de cliënt met het  aangaan van de zakenrelatie nastreeft.

OPMERKING Dit punt dient het kantoor (met inbegrip van personeel en medewerkers) toe  te laten om bij elke (potentiële) cliënt een risicobeoordeling uit te voeren.

8.2.1. Wanneer een risicobeoordeling uitvoeren?

Dit proces van risicobepaling is doorlopend en wordt minstens uitgevoerd op de volgende  tijdstippen:

a)  Op het moment van de cliëntacceptatie bij een nieuwe cliënt;

b)  Telkens als een gebeurtenis een onderzoek verantwoordt, bijvoorbeeld: wijziging  van het aandelenbezit, activiteitenwijziging, verplaatsing van de maatschappelijke  zetel, enz.;

c)  Wijziging in de aard van de zakelijke relatie: bv cliënt vraagt een nieuwe dienst (die  niet voorzien was in de initiële opdrachtbrief) of verderzetting van een  samenwerking

d)  Op regelmatige basis zoals voorzien in punt 7.5. van deze procedure.

De risicofactoren

Er bestaat geen unieke methodologie om een dergelijke risicobeoordeling in concreto uit  te voeren.    Verschillende benaderingen zijn dus mogelijk. Zo werd door de Financiële Actiegroep  (FAG) een richtsnoer uitgschreven voor economische beroepen. De volledige tekst  bestaat echter enkel in het Engels: klik hier )    Uit voornoemde richtsnoeren van de FAG werden de meest relevante passages  opgenomen in deze handleiding onder punt 22.

Dit model vormt een hulpmiddel waarvan het gebruik geen verplicht karakter heeft. Indien  u er gebruik van maakt, moet deze, indien nodig, worden aangepast, rekening houdend  met de specifieke kenmerken van uw kantoor. U kan er ook voor opteren om deze  risicobeoordeling uit te voeren volgens een andere methode, maar welke methode u ook  kiest, u zal steeds in staat moeten zijn om, op basis van documenten, aan de bevoegde  toezichtautoriteit aan te tonen dat de gevolgde methode toelaat om te voldoen aan de  verplichtingen van de AWW .

9. LEIDRAAD VOOR ACCEPTATIE EN IDENTIFICATIE VAN DE CLIËNTEN

Wettelijk kader

De hieronder behandelde onderwerpen vinden we terug in Boek II,Titel 3 van de AWW .

Beslissingsbevoegdheid in ons kantoor

De aanvaarding van een cliënt of van een opdracht behoort in ons kantoor tot de  verantwoordelijkheid van volgende perso(o)n(-en) XXX….. . [Elk kantoor kan dit zelf verder  in detail te omschrijven en te bepalen.]

Algemene factoren bij aanvaarding of weigering van klanten in ons kantoor

Hoewel het klantenacceptatiebeleid in toepassing van de AWW voorziet in specifieke  maatregelen op het vlak van identificatie en waakzaamheid maakt het evenwel integraal  deel uit van het binnen ons kantoor strikt toepasselijke algemene kwaliteitsreglement.    De « antiwitwasregels » zijn een aanvulling op de « algemene regels » en brengen de  toepassing van specifieke verplichtingen en procedures met zich mee.    Dit betekent dat, vooraleer de antiwitwasregels kunnen toegepast worden, in eerste  instantie volgende criteria (in te vullen door elk kantoor) moeten in overweging worden  genomen:

Dit is louter een voorbeeld. Elk kantoor dient dit individueel uit te werken

FACTOREN  IN CONCRETO  Activiteitensector:  volgende sectoren worden in ons kantoor  niet aanvaard : ………..  Geografische ligging  Ons kantoor neemt enkel cliënten aan  gevestigd …….  Solvabiliteit  Is er een risico op discontinuïteit ?  Onafhankelijkheid  Risico op belangconflicten ?  Ereloon  Is de potentiële cliënt bereid ons ereloon te  aanvaarden?  Werklastmeting  Hoe  zwaar  weegt  het  dossier  in  verhouding tot andere cliënten?  Varia  Waarom gekozen voor ons kantoor?  Confrater  Reden van overstap naar ons kantoor?  Enz………

WG/FT -factoren bij aanvaarding of weigering van klanten in ons kantoor

Het kantoor houdt, in deze context, rekening met de volgende factoren bij het bepalen van  de aanvaardbaarheid van klanten:

➢  De identiteit, zakelijke reputatie, integriteit van de cliënt, de belangrijkste  bestuursleden en de lasthebbers van de cliënt en de uiteindelijke begunstigden  van de cliënt;

o  bv. agressieve interpretatie van de boekhoudkundige wetgeving en de  interne controleomgeving in de context van wettelijke opdrachten;    o  het publieke profiel van de potentiële cliënt dat twijfels doet rijzen over zijn  integriteit;    o  een aan de entiteit niet aangepaste operationele en controleomgeving.

➢  Aanwijzingen dat de cliënt, hetzij zelf, hetzij door de aard van zijn werkzaamheden  betrokken kan zijn bij het witwassen van geld of andere criminele activiteiten (zie  de punten 10 en 11 van deze handleiding);    ➢  Aanwijzingen dat de cliënt door zijn houding of door het verstrekken van  onvolledige informatie of het niet mededelen ervan de correcte uitvoering van de  opdracht wil bemoeilijken en dit op een manier die twijfel doet ontstaan over de  integriteit van de cliënt;    ➢  De financiële toestand en zijn vermogen om erelonen te betalen;

o  de cliënt biedt aan abnormaal hoge erelonen te betalen en/of biedt aan om  belangrijke erelonen in contanten te betalen.

➢  Huidige of vroegere relaties met andere beroepsbeoefenaars (bv. vroegere of  momenteel lopende contracten) en in het bijzonder informatie die wijst op het  bestaan van een mogelijk WG/FT-risico.

Weigering van cliënten: wie verwittigen?

Indien de toepassing van één of meerdere van de hierboven vermelde criteria aanleiding  geeft tot de weigering van de potentiële cliënt dan dient dit in alle gevallen  gedocumenteerd te worden.    Elk kantoor moet hier verder zelf aangeven in welke gevallen een weigering op grond van  reden opgesomd in 9.3. moet gerapporteerd worden aan de AMLCO of leiding van het  kantoor.

In het geval van een weigering om redenen opgesomd in 9.4. dient dit evenwel altijd  gerapporteerd te worden aan de AMLCO en zal de AMLCO een verslag maken.

Mogelijke bronnen van informatie

Enkele van de mogelijke informatiebronnen [bij te werken door elk kantoor]  voor de beoordeling van de aanvaardbaarheid van klanten zijn:    Voorbeeld :

➢  Vorige professionele adviseurs/beroepsbeoefenaars,.;

➢  Onderzoeksbureaus of informatieverstrekkende bedrijven (vb.Companyweb,  Dun& Bradstreet, Graydon, Infobase, Vadis, openthebox.be …);

➢  Rapporten van kredietratingbureaus;

➢  Ministeries, toezichthoudende instanties en handelsorganisaties;

➢  Zakelijke contacten en bestaande klanten in vergelijkbare bedrijven;

➢  Publiek beschikbare informatie, zoals jaar-/tussentijdse verslagen, informatieve  circulaires en een lijst van sancties;

➢  Van de VS of de OESO uitgaande sancties tegen landen of personen;

➢  Persdiensten of -commentaar en andere via het internet beschikbare informatie;

➢  Dow Jones of Worldcheck en gelijkaardige websites.

Modaliteiten betreffende de identificatie

9.7.1. Formulieren

Bij de aanvaarding van cliënten en opdrachten zullen volgende documenten worden  gebruikt:

➢  De beslissingsbomen  ➢  De identificatieschema’s  ➢  De identificatieformulieren  ➢  Het formulier risicobepaling

De identificatieformulieren en het formulier risicobepaling, volgens de modellen die ons  kantoor gebruikt, moeten met aandacht worden ingevuld en dit in principe voorafgaand  aan elke acceptatie (zie verder in deze handleiding voor eventuele uitzonderingen).    Deze formulieren worden ook gebruikt in geval van actualisering van gegevens.

9.7.2. Stappenplan

➢  Verzamelen van de identificatiedocumenten (zie bundel modelformulieren)  ➢  Deze documenten worden gekopieerd  ➢  Analyse van deze documenten met het oog op het bekomen van redelijke  zekerheid dat het om pertinente en geloofwaardige documenten gaat en niet om  valse stukken  ➢  voornoemde documenten en de bijlagen ter staving (zoals identiteitskaart,  paspoort, enz…) dienen te worden bewaard gedurende ten minste tien jaar te  rekenen vanaf het einde van de zakelijke relatie met de cliënt 3 .    Bij dit alles wordt niet uit het oog verloren dat de cliënt zelf de verklaring betreffende de  uiteindelijke begunstigde moet ondertekenen en zelf de nodige gegevens moet  verstrekken (zie formulier).

De risicobepaling:

Alvorens een cliënt te aanvaarden dient het risiconiveau bepaald te worden.  In ons kantoor worden drie risiconiveaus toegepast (zie punt 7): standaard, laag en hoog.  [Indien andere niveaus van of indelingen van toepassing zijn dienen de details hiervan hier  ook opgenomen te worden]

Ons kantoor hanteert voor de beoordeling en indeling van de klanten op basis van hun  risicogevoeligheid volgende criteria:

a) de elementen uit de algemene risicobeoordeling;

b) de risicocriteria verbonden aan de cliënt;

c) de risicocriteria verbonden aan de door de cliënt gevraagde of gebruikte dienst

of verrichtingen;

d) de geografische risicofactoren.

In de praktijk kunnen deze risico’s behoren tot verschillende categorieën en dienen ze  derhalve te worden beschouwd als onderling afhankelijke risico’s in plaats van  afzonderlijke en onderscheiden risico’s.

De risicobeoordeling wordt uitgevoerd in twee fasen:

FASE 1 : als één van de risicocriteria is vastgesteld, wordt de (potentiële) cliënt ingedeeld in  de categorie van klanten met een hoog risico. Dit zal desgevallend voor verder onderzoek  worden meegedeeld aan de AMLCO via het formulier risicobepaling;

FASE 2: in een tweede fase kan, aansluitend op de bijkomende ingewonnen informatie, de  oorspronkelijk vastgestelde risico-indeling worden bevestigd als zijnde een hoog risico of

worden aangeduid als een laag/standaard risico in functie van het eventuele advies van de  AMLCO.

Als één van deze criteria aanwezig is, beschouwen wij de cliënt als zijnde met een hoog  risico, tenzij de bijkomende informatie de beoordeling wijzigt.

In alle andere gevallen is het in principe een cliënt met een standaard risico.

Wanneer, wat en hoe – identificatie & verificatie bij nieuwe zakelijke relatie?

9.9.1. Inleiding

Het verrichten van een cliëntenonderzoek omvat minimaal en in ieder geval - via de binnen  het kantoor gebruikte formulieren of IT-toepassingen - het documenteren op basis van  gegevens afkomstig van betrouwbare en onafhankelijke bron(-nen):

➢  Identificatie van de cliënt en verificatie van diens identiteit;

➢  Identificatie en verificatie van de identiteit van de lasthebber van de cliënt die de  opdrachtbrief tekent;

➢  Indien van toepassing, de identificatie van de natuurlijke persoon (of personen)  die uiteindelijk begunstigde is/zijn (d.i. de persoon die meer dan 25% van  stemrechten/aandelen bezit of die de controle uitoefent over 25% of meer van het  vermogen) van de cliënt en/of de persoon namens wie een opdracht wordt  uitgevoerd ("de uiteindelijke begunstigde") en dit te controleren, door middel van  risicogeoriënteerde en adequate maatregelen;

➢  Het doel van de zakelijke relatie in het licht van de activiteiten van de cliënt, met  inbegrip van zijn bedrijfsvoering, omschrijven. Ter zake kan men bv de offerte of  het ontwerp van opdrachtbrief raadplegen;

➢  Bepalen van een risicoprofiel voor elke cliënt (zie punt 8 van deze handleiding).    De dossierverantwoordelijken moeten kunnen aantonen dat de genomen maatregelen in  verhouding staan tot het risico zoals bepaald. Met andere woorden, van  de dossierverantwoordelijken wordt ter zake verwacht dat zij een redelijk oordeel  toepassen.

9.9.2. Wanneer dient de identificatie & verificatie te gebeuren?

In principe dienen klantenonderzoeksmaatregelen verricht te worden VOORAFGAAND aan  de aanvang van de opdracht.    Hier dient het kantoor te bepalen of zij al dan niet toestaat een afwijkingsregel te  gebruiken  … [zelf in te vullen door elk kantoor]  Vb. In de in 10.2.1. omschreven omstandigheden kan de verificatie gebeuren nadat de  zakelijke relatie aangevangen is.

9.9.3. Wat en hoe bij standaardrisico?

Hieronder een uitgewerkt voorbeeld. Elk kantoor dient dit echter voor zichzelf uit te  werken.

Identificatie  natuurlijke persoon

Minstens:

Minstens:

Zie  formulier in  bundel

-  naam en voornaam

-  naam en voornaam

-  in de mate van het  mogelijke :

-  in de mate van het  mogelijke :

o geboortedatum

o geboortedatum

en -plaats

en -plaats

o adres

o adres

-  statutaire zetel

-  statutaire zetel

Identificatie rechts- persoon

Zie  formulier in  bundel

-  benaming

-  benaming

-  lijst bestuurders

-  lijst bestuurders

-  vertegenwoordigings- bevoegdheid

-  vertegenwoordigings- bevoegdheid

-  identiteitskaart (fiche e- id of recto/verso kopie)

-  identiteitskaart (fiche e- id of recto/verso kopie)

Verificatie  natuurlijke persoon

Zie  formulier in  bundel

-  of paspoort

-  of paspoort

-  of gelijkwaardige  documenten/stukken die  dezelfde informatie  geven (bv rijbewijs,  attest sociale kas,  aanslagbiljet  personenbelasting.....)

-  of gelijkwaardige  documenten/stukken die  dezelfde informatie  geven (bv rijbewijs,  attest sociale kas,  aanslagbiljet  personenbelasting.....)

-  KBO

-  KBO

Verificatie rechts- persoon

Zie  formulier in  bundel

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk

-  gecoördineerde statuten

-  gecoördineerde statuten

-   publicatie benoeming

-  publicatie benoeming

9.9.4. Wat en hoe bij laag risico?

Hieronder een uitgewerkt voorbeeld. Elk kantoor dient dit echter voor zichzelf uit te  werken.

Identificatie  natuurlijke persoon

Minstens: naam en  voornaam

Minstens: naam en  voornaam

Zie  formulier in  bundel

Indien verwarring met een  andere persoon mogelijk is  moet ook minstens:

Indien verwarring met een  andere persoon mogelijk is  moet ook minstens:

geboortedatum en -plaats

geboortedatum en -plaats

-  statutaire zetel

-  statutaire zetel

Identificatie rechts- persoon

Zie  formulier in  bundel

-  benaming

-  benaming

-  lijst bestuurders

-  lijst bestuurders

-  vertegenwoordigings- bevoegdheid

-  vertegenwoordigings- bevoegdheid

-  identiteitskaart (fiche e- id of recto/verso kopie)

-  identiteitskaart (fiche e- id of recto/verso kopie)

Verificatie  natuurlijke persoon

Zie  formulier in  bundel

-  of paspoort

-  of paspoort

-  of gelijkwaardige  documenten/stukken die  dezelfde informatie  geven (bv rijbewijs,  attest sociale kas, EGW- factuur, Linkedin,  aanslagbiljet  personenbelasting.....)

-  of gelijkwaardige  documenten/stukken die  dezelfde informatie  geven. (bv rijbewijs,  attest sociale kas, EGW- factuur, Linkedin,  aanslagbiljet  personenbelasting.....)

-  KBO

-  KBO

Zie  formulier in  bundel

Verificatie rechts- persoon

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk

-  gecoördineerde statuten

-  gecoördineerde statuten

-  publicatie benoeming

-  publicatie benoeming

9.9.5. Wat en hoe bij hoog risico?

Hieronder een uitgewerkt voorbeeld. Elk kantoor dient dit echter voor zichzelf uit te  werken.

-  naam en voornaam  -  geboortedatum en – plaats  -  adres

-  naam en voornaam  -  geboortedatum en – plaats  -  adres

Identificatie  natuurlijke persoon

Zie  formulier in  bundel

-   statutaire zetel

-  statutaire zetel

Identificatie rechts- persoon

Zie  formulier in  bundel

-  benaming

-  benaming

-  lijst bestuurders

-  lijst bestuurders

-  vertegenwoordigings- bevoegdheid

-  vertegenwoordigings- bevoegdheid

-  identiteitskaart (fiche e- id of recto/verso kopie)

-  identiteitskaart (fiche e- id of recto/verso kopie)

Verificatie  natuurlijke persoon

Zie  formulier in  bundel

-  of paspoort

-  of paspoort

-  document waaruit  lastgeving blijkt

-  KBO

-  KBO

Verificatie rechts- persoon

Zie  formulier in  bundel

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk)

-  of gelijkwaardig in het  buitenland (bv Infogreffe  in Frankrijk)

-  gecoördineerde statuten

-  gecoördineerde statuten

-  publicatie benoeming

-  publicatie benoeming

*UBO : In dit geval moet de drempel van 25% verlaagd worden naar 10% en dienen alle  personen die minstens 10% aandelen of stemrechten hebben geïdentificeerd te worden  (voornaam, naam en adres).  Alternatief identificatie - voornaam, naam, geboortedatum en -plaats en adres- van de  natuurlijke personen die de bestuurders-rechtspersonen vertegenwoordigen.

Derde zaakaanbrenger

Indien het kantoor en/of de dossierverantwoordelijke hiervoor opteert, kan de procedure  van de derde zaakaanbrenger toegepast worden om de klantenonderzoeksmaatregelen  te voldoen. Echter, in dergelijk geval blijft het kantoor nog steeds verantwoordelijk voor  het voldoen van de klantenonderzoeksmaatregelen.    … [zelf in te vullen door elk kantoor]    Onder deze voorwaarden kan de dossierverantwoordelijke zich beraden over de te nemen  klantenonderzoeksmaatregelen voor een potentiele cliënt op basis van de gegevens  aangereikt door een derde zaakaanbrenger (bijvoorbeeld een advocaat, een bankier of  andere beroepsbeoefenaar) die kan bevestigen dat hij onlangs de nodige controles  afgerond heeft en de nodige klantenonderzoeksdocumentatie bekomen heeft.

Prestaties binnen ons netwerk

Het is mogelijk dat leden van ons netwerk op ons kantoor een beroep doen met het oog  op het uitvoeren van bepaalde prestaties (zoals opdrachten die betrekking hebben op  technische adviezen) zonder dat wij door het lid van het netwerk wordt ingelicht over de  identiteit van de uiteindelijke begunstigde(n) van deze prestaties.

In dit geval dient de uiteindelijke begunstigde(n) niet te worden geïdentificeerd als aan de  volgende voorwaarden voldaan is:

a)  er is geen enkele contractuele relatie, noch enig contact tussen de  beroepsbeoefenaar en de uiteindelijke begunstigde;

b)  het resultaat van de prestaties (verslagen, adviezen, enz.) wordt uitsluitend aan het  lid van het netwerk meegedeeld;

c)  de beroepsbeoefenaar factureert de prestaties aan het lid van zijn netwerk.

In alle andere gevallen dient de gewone procedure te worden toegepast.

Vrijstellingen van de identificatieverplichting - UBO

De AWW voorziet in een vrijstelling van de identificatieverplichting van de UBO van de  cliënt of lasthebber als de cliënt of de lasthebber een beursgenoteerde vennootschap is  waarvan de effecten in een EER-land zijn toegelaten tot verhandeling op een  gereglementeerde markt of een vennootschap genoteerd op de beurs in een gelijkwaardig  derde  land.    Vandaag worden door de Europese Unie volgende landen beschouwd als gelijkwaardige  derde landen: Australië, Hongkong, Zwitserland en de Verenigde Staten van Amerika.    Voor lijst van de EER- gereglementeerde markten:  https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_upreg#    Voor eventuele updates over de gelijkwaardige derde landen:  https://ec.europa.eu/info/business-economy-euro/banking-and-finance/international- relations/recognition-non-eu-financial-frameworks-equivalence-decisions_en#recognition-of-non- eu-regulatory-frameworks    Deze vrijstelling van de identificatieverplichting heeft enkel betrekking op de UBO van de  cliënt of de lasthebber.    De beroepsbeoefenaar wordt aanbevolen om schriftelijk vast te leggen op welk(e)  document(en) hij zich heeft gebaseerd bij zijn beslissing om van de vrijstelling van de  identificatieverplichting gebruik te maken, en deze bij te houden.    Bovendien kan men in geen geval een beroep doen op een vrijstelling van de  identificatieverplichting zodra de omstandigheden vermoedens van witwassen van geld  meebrengen op het moment dat de zakenrelatie aangegaan wordt of daarna. In dit geval  dient men over te gaan tot de identificatie, overeenkomstig wat hierboven ter zake is  bepaald. In dit geval dient de AMLCO hiervan in kennis gesteld te worden per e-mail of via  een andere daartoe voorziene methode.

10. VERHOOGDE EN DOORLOPENDE WAAKZAAMHEID

Wettelijk kader

De artikelen 19, 35, 37 tot 39 en 41 van de AWW voorzien dat het kantoor naast de algemene  waakzaamheid (punt 9) ook steeds een doorlopende waakzaamheid en in sommige  gevallen een verhoogde waakzaamheid aan de dag moet leggen.

Verhoogde waakzaamheid

In volgende omstandigheden wordt in toepassing van de AWW (artikelen 37 tot 39 en 41)  door ons kantoor een verhoogde waakzaamheid toegepast.

10.2.1. Verificatie gebeurt na aanvang zakenrelatie

In beginsel gebeurt de verificatie vóór de cliënt aanvaard wordt (zie 8.9.2.) In volgende  bijzondere omstandigheden staan wij toe dat deze verificatie gebeurt nadat de  zakenrelatie aanving. [zelf in te vullen door elk kantoor. Indien dit niet wordt toegepast  mag dit geschrapt worden]    In elk geval kan dit enkel en alleen wanneer er sprake is van:

1) een laag risico EN  2) het noodzakelijk is dat de activiteit niet wordt onderbroken EN.  3) bovendien kan het enkel en alleen in volgende omstandigheden : zelf in te vullen

door elk kantoor.

10.2.2. Verhoogde waakzaamheid ten aanzien van fiscale paradijzen en het risico inzake  ernstige, al dan niet georganiseerde fiscale fraude

Ten aanzien van volgende landen dienen wij bijzonder waakzaam te zijn. Het gaat om  landen die gekend (zie Artikel 179 KB/WIB ) zijn als “fiscaal paradijs” en dus mogelijk een  risico inzake ernstige, al dan niet georganiseerde fiscale fraude bestaat.

Deze landen zijn vandaag: “Abu Dhabi; Ajman; Anguilla; Bahama's; Bahrein; Bermuda;  Britse Maagdeneilanden; Kaaimaneilanden; Dubai; Fujairah; Guernsey; Jersey; Eiland Man;  Marshalleilanden; Micronesië (Federatie van); Monaco; Montenegro; Nauru; Oezbekistan;  Palau; Pitcairneilanden; Ras al Khaimah; Saint-Barthelemy; Sharjah; Somalië; Turkmenistan;  Turks en Caicos Eilanden; Umm al Qaiwain; Vanuatu; Wallis-en-Futuna.".

De waakzaamheid heeft betrekking op diensten, verrichtingen van en door cliënten of  daarmee verbonden personen.

10.2.3. Verhoogde waakzaamheid: de politiek prominente personen (PPP)

Om na te gaan of een persoon kan beschouwd worden als een politiek prominent  persoon ( artikel 4, 28°-30 AWW ) zal de naam via bijvoorbeeld Google, Openthebox.be,  Linkedin [indien het kantoor ook nog andere toepassingen gebruikt kunnen deze hier  vermeld worden ] gecontroleerd worden

Zijn te beschouwen als "politiek prominente persoon”: een natuurlijk persoon die een  prominente publieke functie bekleedt of bekleed heeft, en met name:

a)  staatshoofden, regeringsleiders, ministers en staatssecretarissen;

b)  parlementsleden of leden van soortgelijke wetgevende organen;

c)  leden van bestuurslichamen van politieke partijen;

d)  leden van hooggerechtshoven, grondwettelijke hoven of van andere hoge  rechterlijke instanties, met inbegrip van administratieve rechterlijke instanties, die  arresten wijzen waartegen geen beroep openstaat, behalve in uitzonderlijke  omstandigheden;

e)  leden van rekenkamers of van raden van bestuur van centrale banken;

f)  ambassadeurs, consuls, zaakgelastigden en hoge officieren van de strijdkrachten;

g)  leden van het leidinggevend, toezichthoudend of bestuurslichaam van  overheidsbedrijven;

h)  bestuurders, plaatsvervangende bestuurders en leden van de raad van bestuur of  bekleders van een gelijkwaardige functie bij een internationale organisatie;

maar ook " familielid" van de PPP:

a)  de echtgenoot of een persoon die als gelijkwaardig met de echtgenoot wordt  aangemerkt;

b)  de kinderen en de echtgenoten van die kinderen of de personen die als  gelijkwaardig met de echtgenoot worden aangemerkt;

c)  de ouders;

en " personen bekend als naaste geassocieerden ”:

a)  natuurlijke personen die samen met een politiek prominente persoon de  uiteindelijke begunstigden zijn van rechtspersoon zoals een vennootschap, trust,  fiducie, vzw of stichting of waarvan bekend is dat zij met een politiek prominente  persoon andere nauwe zakelijke relaties hebben;

b)  natuurlijke personen die als enige de uiteindelijke begunstigden zijn van een  rechtspersoon zoals een vennootschap, trust, fiducie, vzw of stichting waarvan  bekend is dat deze in feite werd opgericht ten behoeve van een politiek  prominente persoon;

Deze personen kunnen hetzij cliënt of lasthebber of uiteindelijke begunstigde zijn.  Derhalve zal ons kantoor een verscherpte waakzaamheid aan de dag moeten leggen ten  aanzien van een cliënt-rechtspersoon of van elke andere juridische constructie waarvan de  uiteindelijke begunstigde een politiek prominente persoon zou zijn.

Onafhankelijk van het toepasselijke risiconiveau moet men in deze situatie steeds :

a)  toestemming verkrijgen van de AMLCO om zakelijke relaties met dergelijke  personen aan te gaan of voort te zetten;

b)  passende maatregelen nemen om de oorsprong vast te stellen van het vermogen  en van de geldmiddelen die bij zakelijke relaties of verrichtingen met dergelijke  personen worden gebruikt;

c)  een verscherpt toezicht uitoefenen op de zakelijke relatie.

Het kantoor zal de onder b en c gestelde maatregelen toepassen tot 12 maanden na de  stopzetting van het politiek mandaat van betrokkene.    Dergelijke situaties worden beschouwd als een verhoging van het witwasrisico en vragen  om toepassing van bijkomende maatregelen zoals omschreven in punt 8.3. van deze  handleiding.

Doorlopende waakzaamheid na de acceptatie en identificatie

De dossierverantwoordelijke of indien er geen is één van de beroepsbeoefenaars, moet  toezicht houden op de zakelijke relatie en bestendige waakzaamheid uitoefenen ter  bevestiging dat de opdrachten die worden uitgevoerd in overeenstemming zijn met de  kennis over de cliënt (KYC), omvattende diens zakelijk en risicoprofiel, en, waar nodig, de  bron van fondsen.    De documenten, gegevens of informaties die gediend hebben tot het bepalen van het  risicoprofiel van de cliënt dienen op basis van het risicoprofiel doorlopend te worden  geactualiseerd. Dit bij elke wijziging in het zakelijk en risicoprofiel van de cliënt en in elk  geval op regelmatige tijdstippen. Ter zake wordt verwezen naar punt 7.5 van dit document.

Wat indien geen identificatie of verificatie of doorlopende waakzaamheid mogelijk  is?

Indien niet kan voldaan worden aan de vereisten inzake identificatie & verificatie van de  cliënt, bepaling van de aard van de zakelijke relatie of doorlopende waakzaamheid mag  geen zakelijke relatie worden aangaan of verdergezet, noch een verrichting voor de  (potentiële) cliënt worden uitgevoerd.    Dit verbod tot het aangaan van de zakelijke relatie of de verplichting tot stopzetting is niet  van toepassing onder de strikte voorwaarde dat de beroepsbeoefenaar bezig is met het  bepalen van de rechtspositie van de cliënt of met het verdedigen van de cliënt of het  vertegenwoordigen ervan in of in verband met een rechtsgeding, met inbegrip van advies  over het instellen of vermijden van een dergelijk rechtsgeding (zie artikel 33, §2, 34, §4 en  35,§3 AWW en Toelichtingsnota CFI .

De AMLCO onderzoekt of de redenen waarom niet kan worden voldaan aan de bedoelde  verplichting een vermoeden van WG/FT doen rijzen en of er reden is tot melding aan de  CFI. (zie 14.5)

11. BEWARING VAN DOCUMENTEN - GEGEVENSBESCHERMING

Wettelijk kader

Artikelen 60 tot en met 65 AWW omschrijven op welke wijze de gegevens dienen  bewaard en beschermd te worden.

Algemeen

De dossierverantwoordelijke draagt er zorg voor de verzamelde klantenonderzoeks- documenten en de informatie te bewaren voor een periode van ten minste 10 jaar te  rekenen vanaf het einde van de zakelijke relatie met de cliënt.

Verder moeten volgende documenten ook gedurende 10 jaar worden bewaard:

➢  alle interne verslagen (zie modelbundel) met bijlagen zoals bv. in het geval van  vaststelling van atypische verrichtingen, de analyse hiervan en de beslissing  waartoe deze analyse heeft geleid op het vlak van de aan de CFI mee te delen  informatie;  ➢  het  jaarverslag  dat  desgevallend  werd  opgesteld  door  de  AMLCO    De bewijsstukken, de identificatiegegevens en de verslagen zullen op volgende wijze  worden bewaard: bv kopies inscannen of opslaan in het elektronisch dossier van de cliënt  of enkel kopies/uitprints in een afzonderlijke papieren dossier bewaren per cliënt. Elk  kantoor dient hier zelf te beschrijven hoe en waar deze stukken bewaard dienen te  worden. Indien het kantoor toegang heeft tot databanken die toelaten bepaalde of alle te  controleren identificatiegegevens via referentie (bv. ondernemingsnummer cliënt) te  raadplegen kan de beschrijving van de bewaringsprocedure vervangen worden door een  beschrijving van de referentie die dan voor elke cliënt moet bewaard worden in plaats van  de kopie van de stukken. Elk kantoor dient dit zelf in te vullen: men kan bv een link leggen  voor het dossier van de cliënt-rechtspersoon in Companyweb, Graydon voor alles wat  betreft de identificatie van de rechtspersoon.    Het kantoor zal de medewerkers wijzen op het feit dat het opslaan van de referentie niet  betekent dat de identificatiegegevens niet meer moeten worden nagekeken.

Privacy - GDPR

Alle in dit kader verwerkte persoonsgegevens vallen onder toepassing van de AVG- verordening (privacywetgeving) en dienen als vertrouwelijke gegevens te worden  beschouwd. Terzake verwijzen wij naar het privacyverklaring van het kantoor. Wij wijzen  onze medewerkers er bovendien op dat de in dit kader verzamelde persoonsgegevens een  bijzondere bescherming genieten zoals voorzien in artikel 65 van de AWW: alle verzoeken  tot toegang tot de in dit kader verwerkte persoonsgegevens dienen te worden  doorgegeven aan de AMLCO / DPO 4 die het nodige zullen doen.

12. PROCEDURE BIJ DE VASTSTELLING VAN ATYPISCHE VERRICHTINGEN

Wettelijk kader

De artikelen 35 en 45 tot 46 van de AWW voorzien dat elk kantoor aandacht moet hebben  voor de atypische verrichtingen.

Inleiding

De AWW vereist dat op een bijzonder aandachtige manier onderzocht worden: alle  verrichtingen of feiten die bijzonder vatbaar zijn voor witwassen van geld of financiering  van terrorisme:

➢  wegens hun aard of ongebruikelijk karakter gelet op de activiteiten van de cliënt;

➢  dan wel wegens de begeleidende omstandigheden;

➢  de hoedanigheid van de betrokken personen.

Over dit onderzoek moet een schriftelijk verslag opgesteld worden door de AMLCO.

Mogelijke aanwijzingen van het bestaan een atypische verrichting

De aanwijzingen of knipperlichten die kunnen leiden tot het onderzoek of een verrichting  of een feit al dan niet bijzonder vatbaar is voor witwassen van geld of voor de financiering  van terrorisme zijn de volgende (Hieronder een voorbeeld. Elk kantoor dient dit voor  zichzelf uit te werken):

➢  De cliënt lijkt boven zijn stand te leven rekening houdende met zijn  beroepsactiviteiten;

➢  de cliënt vraagt de beroepsbeoefenaar hem bij een kredietinstelling te  introduceren om rekeningen te openen hoewel de vennootschap  klaarblijkelijk geen activiteiten uitoefent in dit land en de cliënt  klaarblijkelijk geen duidelijk beeld heeft van haar toekomstige  activiteiten in dit land;

➢  de aankoopfacturen worden steeds betaald bij ontvangst terwijl dit niet  gebruikelijk is in die sector of voor die bedragen;

➢  de  aankoopfacturen  worden  onmiddellijk  gevolgd  door  verkoopfacturen voor bijna hetzelfde bedrag (verhoogd met een kleine  marge);

➢  het geld blijft nooit lang op de bankrekening van de vennootschap  (doorsluisrekening);

➢  beleggingen voor een buitengewoon bedrag gezien het profiel van de  cliënt;

➢  inbreng in contanten bij de oprichting of een kapitaalverhoging;

➢  inbreng in natura (materiaal / rekening courant) dat klaarblijkelijk  overgewaardeerd is;

➢  kapitaalverhoging door inbreng in natura van een rekening courant dat  zelf deels uit contanten bestaat;

➢  verdachte vereffening van een vennootschap kort na de oprichting;

➢  deelnemingen die de melder als verdacht beschouwt;

➢  verschillende wijzigingen van de statuten op korte tijd: wijziging van het  maatschappelijke doel, de maatschappelijke zetel, en regelmatig  wijziging van de zaakvoerders;

➢  de werkelijke activiteit stemt niet overeen met die in de statuten;

➢  voor sommige verkoopfacturen ontbreken de vervoerdocumenten,  stortingen in contanten – vermoeden van btw-fraude (verkoop in het  zwart).

➢  vermoedelijke  valse  facturen  (onregelmatigheden  bij  aankoopfacturen);

➢  omzetcijfer wordt slechts gedeeltelijk in de boekhouding opgenomen;

➢  talrijke aankoopfacturen zijn van een en dezelfde onderaannemer  afkomstig (valse facturen of btw-carrouselfraude)

➢  onregelmatigheden bij facturen binnen dezelfde groep;

➢  een groot aantal aankoopfacturen is afkomstig van een en dezelfde  groep;

➢  de  vennootschap  betaalt  diverse  consultancykosten  aan  offshorevennootschappen ;

➢  de jaarrekeningen worden niet of laattijdig neergelegd;

➢  de middelen die voortvloeien uit de beroepsactiviteit van de cliënt  staan niet in verhouding met de activiteitensector;

➢  de cliënt doet steeds een beroep op verschillende uitoefenaars van  boekhoudkundige beroepen;

➢  de  vennootschap  heeft  geen  werknemers,  wat  gezien  de  activiteitensector niet normaal is;

➢  de vennootschap doet verschillende aankopen (boten, luxevoertuigen,  enz.) zonder verband met de activiteit van de vennootschap.

Ten aanzien van klanten met een verhoogd risico moet bovendien bijzondere  aandacht besteed worden aan volgende verrichtingen:

➢  belangrijke bancaire verrichtingen met het buitenland die niet in  overeenstemming zijn met de kennis die men heeft betreffende  zakelijke activiteiten van de cliënt;

➢  rekeningen van klanten, leveranciers, bank of anderen die onbetaald  zijn of waar gedurende lange tijd geen beweging gebeurt.

Procedure bij vaststelling van één van de criteria:

12.4.1. De vaststelling

Als het kantoor met één van de onder 12.3. vermelde verrichtingen geconfronteerd wordt  dient de AMLCO hiervan steeds schriftelijk in kennis worden gesteld. [Elk kantoor dient hier  in functie van interne organisatie de persoon aan te duiden die in eerste instantie hiervan  moet in kennis worden gesteld, alsook de wijze waarop dit dient te gebeuren en  gedocumenteerd te worden]. Men moet hiervoor gebruik maken van het formulier  “Formulier interne melding atypische verrichting of gebeurtenis “dat men in de  formulierenbundel kan vinden.

12.4.2. Taak AMLCO

12.4.2.1. Samenstellen dossier

De AMLCO zal een dossier samenstellen en op basis van bijkomend onderzoek beoordelen  of van de gemelde verrichting vermoed kan worden dat ze verband houdt met WG/FT.

De aanvullende onderzoeken beogen o.a. na te gaan of het mogelijk is dat het kapitaal of  de goederen afkomstig zijn van één van de misdrijven opgesomd in artikel 5 van de AWW  (zie 11.1.1).

12.4.2.2. Er is geen verband met WG/FT

Indien uit dit onderzoek blijkt dat kan vastgesteld worden dat van deze verrichting(-en )  niet vermoed kan worden dat ze een verband houden met het witwassen van geld of  financiering van terrorisme zal een samenvatting met het resultaat van de aanvullende  analyse opgesteld en bewaard worden. Voor deze samenvatting zal in ons kantoor  gebruik gemaakt worden van het « intern verslag » [ voorbeeld in de modellenbundel].

Deze verslagen moeten gedurende 10 jaar na de kwestieuze verrichting worden bewaard.

12.4.2.3. Er is een verband met WG/FT

Indien uit het aanvullend onderzoek wel vermoed kan worden dat ze verband houdt met  het witwassen van geld of de financiering van terrorisme gaat de AMLCO over tot het  opstellen van een « intern verslag» [ voorbeeld in de modellenbundel] .

Het intern verslag wordt vervolledigd met de omschrijving van de uitgevoerde aanvullende  onderzoeken en getrokken besluiten. De verslagen dienen gedurende 10 jaar na de  kwestieuze verrichting te worden bewaard.

De AMLCO zal er op toezien dat wordt overgegaan tot een herevaluatie van het  toegekende risiconiveau.

Indien uit de onderzoeken kan besloten worden dat het feit of de verrichting verband  houdt met het witwassen van geld of de financiering van terrorisme of er een vermoeden  bestaat dat het feit of de verrichting verband houdt met het witwassen van geld of de  financiering van terrorisme zal de AMLCO, of desgevallend bij diens onbeschikbaarheid een  beroepsbeoefenaar, een melding opmaken en overmaken aan de CFI en dit conform punt  14.

13. DE VERSLAGEN VAN DE AMLCO

Wettelijk kader

De artikelen 9, 45 en 46 van de AWW voorzien dat de AMLCO in een aantal situaties een  verslag moet opmaken.

Toepassingsmodaliteiten:

De AMLCO moet een intern verslag maken in volgende gevallen:

-  vaststelling atypische verrichting, op basis van het formulier medegedeeld door de  medewerker die de verrichting heeft vastgesteld;

-  wanneer het kantoor niet kan voldoen aan haar verplichtingen inzake identificatie  en/of verificatie van de identiteit van de cliënt;

-  waneer het kantoor niet kan voldoen aan de verplichting tot beoordeling van het  risico verbonden aan de cliënt;

-  wanneer na het uitvoeren van de de risicobeoordeling het kantoor beslist om de  potentiële cliënt te weigeren wegens te hoog WG/FT risico.

De AMLCO maakt deze verslagen op basis van de modellen in de modellenbundel.

In geval van een vermoeden van WG/FT zal de AMLCO overgaan tot melding aan de CFI en  dit conform punt 14.

De AMLCO zal ook minstens eenmaal per jaar een activiteitenverslag opmaken.

14. DE MELDINGSPLICHT AAN DE CFI

Wettelijk kader

De artikelen 47 tot en met 59 AWW omschrijven de rechten en verplichtingen van de  beroepsbeoefenaar bij melding van vermoedens van WG/FT.

De meldingsplicht: principe

In het kader van hun beroepsactiviteiten, zijn de beroepsbeoefenaars gehouden tot het  beroepsgeheim en in geval zij deze verplichting niet respecteren kan deze wetsovertreding  strafrechtelijk worden bestraft.

De geheimhoudingsplicht van artikel 458 van het Strafwetboek is absoluut, buiten het  geval dat de beroepsbeoefenaar wordt opgeroepen om in rechte of voor een  parlementaire onderzoekscommissie een getuigenis af te leggen (spreekrecht) en buiten  het geval dat de wet, hen verplicht die geheimen bekend te maken. Voor onze beroepen is  de AWW één van die wettelijke uitzonderingen op het beroepsgeheim.

Immers volgens artikel 47 van de AWW 5 moeten (spreekplicht) de aan de AWW  onderworpen beroepsbeoefenaars :” .... aan de CFI melden, wanneer ze weten, vermoeden  of redelijke gronden hebben om te vermoeden :

1° dat geldmiddelen, ongeacht het bedrag, verband houden met het witwassen van geld of  de financiering van terrorisme;

2° dat verrichtingen of pogingen tot verrichtingen verband houden met het witwassen van  geld of de financiering van terrorisme. Deze verplichting tot melding is eveneens van  toepassing wanneer de cliënt beslist de voorgenomen verrichting niet uit te voeren;

3° buiten de gevallen bedoeld in 1° en 2°, dat een feit waarvan ze kennis hebben, verband  houdt met het witwassen van geld of de financiering van terrorisme.

De verplichting tot melding aan de CFI met toepassing van 1° tot en met 3°, houdt niet in dat  de onderworpen entiteit de onderliggende criminele activiteit van het witwassen van geld  dient te identificeren .”

Dit artikel 47 van de AWW vormt dus een belangrijke uitzondering op het hoger gestelde  principe van het beroepsgeheim. De genoemde verplichting tot melding aan de CFI,  wanneer een vermoeden of zekerheid van witwassen bestaat, staat centraal in de strijd  tegen het witwassen van geld en de financiering van terrorisme.

Witwassen van geld of financiering van terrorisme – wat is dit ?

De wetgever heeft de begrippen witwassen van geld of financiering van het terrorisme  duidelijk omschreven in artikel 2 en 3 van de AWW:

## Art. 2

Voor de toepassing van deze wet en de besluiten en reglementen genomen ter

uitvoering ervan, wordt beschouwd als " witwassen van geld" :

1° de omzetting of overdracht van geld of andere goederen, wetende dat deze zijn verworven  uit een criminele activiteit of uit deelneming aan een dergelijke activiteit, met het oogmerk de  illegale herkomst ervan te verhelen of te verhullen of een persoon die bij een dergelijke  activiteit is betrokken, te helpen aan de juridische gevolgen van zijn daden te ontkomen;

2° het verhelen of verhullen van de werkelijke aard, oorsprong, vindplaats, vervreemding,  verplaatsing, rechten op of de eigendom van geld of goederen, wetende dat deze verworven  zijn uit een criminele activiteit of uit deelneming aan een dergelijke activiteit;

3° de verwerving, het bezit of het gebruik van geld of goederen, wetende, op het tijdstip van  ontvangst, dat deze voorwerpen zijn verworven uit een criminele activiteit of uit deelneming  aan een dergelijke activiteit;

4° deelneming aan, medeplichtigheid aan, poging tot, hulp aan, aanzetten tot,  vergemakkelijken van, of het geven van raad met het oog op het begaan van één van de in de  bepalingen onder 1°, 2° en 3° bedoelde daden.

De onderliggende crimininele activiteiten waar het over gaat bij witwassen van geld zijn  opgesomd in artikel artikel 4,23° AWW . Het onderzoek van een link tussen het witwassen  en bepaalde criminele activiteit(-en) opgesomd in de AWW is de taak van de CFI. Het is niet  de opdracht van de beroepsbeoefenaar te bepalen of te onderzoeken welk crimineel feit  aan de oorsprong ligt van het witwassen. Het niet vinden van een criminele activiteit  betekent dus niet dat men vrijgesteld is om te melden.

## Art. 3

Voor de toepassing van deze wet en de besluiten en reglementen genomen ter

uitvoering ervan, wordt beschouwd als " financiering van terrorisme" : de verstrekking of  verzameling van geldmiddelen en andere vermogensbestanddelen, op welke wijze ook,  rechtstreeks of onrechtstreeks, met het oogmerk dat deze worden gebruikt of in de  wetenschap dat zij, geheel of gedeeltelijk, zullen worden gebruikt door een terroristische  organisatie, of door een terrorist die alleen handelt, zelfs zonder enige band met een bepaalde  terroristische daad.

De AMLCO dient ter zake in elk geval kennis te nemen van de Toelichtingsnota CFI .

Uitzondering op de meldingsplicht

De beroepsbeoefenaars dienen die informatie en inlichtingen echter niet mee te delen “ in  het geval zij deze van één van hun cliënten ontvangen of over één van hun cliënten verkrijgen  wanneer zij de rechtspositie van deze cliënt bepalen, dan wel die cliënt in of in verband met  een rechtsgeding verdedigen of vertegenwoordigen, met inbegrip van advies over het  instellen of vermijden van een rechtsgeding, ongeacht of dergelijke informatie vóór,  gedurende of na een dergelijk geding wordt ontvangen of verkregen ” (art 53 AWW).

In geval een beroepsbeoefenaar in het kader van zijn beroepsactiviteit bijgevolg juridisch  advies verstrekt in de hoger gegeven context blijft hij dus gehouden tot de – niet optionele  - wettelijke plicht van het beroepsgeheim. Bijgevolg dient een beroepsbeoefenaar die in  dit kader informatie ontvangt die een vermoeden van witwassen doet rijzen, niet over te  gaan tot het meedelen van de informatie aan de CFI.

Let wel, deze uitzondering op de meldingsplicht geldt echter niet wanneer de  beroepsbeoefenaar:

➢  hetzij zelf deelneemt aan de witwasactiviteiten of de activiteiten voor de  financiering van terrorisme;

➢  hetzij juridisch advies voor witwasdoeleinden of voor financiering van terrorisme  verstrekt; of

➢  weet dat de cliënt juridisch advies wenst voor deze doeleinden.

Het Grondwettelijk Hof definieert het bepalen van de rechtspositie, als het “ informeren van  de cliënt over de staat van de wetgeving die van toepassing is op zijn persoonlijke situatie of  op de verrichting die hij overweegt, of hem te adviseren over de wijze waarop die verrichting  binnen het wetttelijk kader kan worden uitgevoerd ”.

Specifieke gevallen

14.5.1. Melding ingevolge problemen bij identificatie – identiteitsverificatie – doorlopende  waakzaamheid - principe

Overeenkomstig de AWW mag ons kantoor met een cliënt geen zakelijke relatie aangaan  of in stand houden, noch verrichtingen voor hem uitvoeren indien geen klantenonderzoek  kan worden verricht over de cliënt of zijn lasthebber(s), overeenkomstig onze leidraad  voor acceptatie van klanten.

Dit betreft het klantenonderzoek in al zijn aspecten:

➢  identificatie & verificatie identiteit cliënt, lasthebbers en UBO;

➢  identificatie kenmerken cliënt, doel en aard zakelijke relatie / occasionele  verrichting;

➢  doorlopende waakzaamheid, desgevallend verhoogde.

Wanneer het klantenonderzoek niet kan worden uitgevoerd moet de AMLCO, na  onderzoek uitmaken of een melding aan de CFI zich opdringt indien de voorwaarden  vermeld in artikel 47 van de AWW (zie punt 13.1.1.) aanwezig zijn.

14.5.2. Melding ingevolge problemen bij identificatie – identiteitsverificatie – doorlopende  waakzaamheid - uitzondering

De beroepsbeoefenaars of AMLCO dienen die informatie en inlichtingen echter niet te  melden “ onder de strikte voorwaarde dat zij de rechtspositie van hun cliënt bepalen of deze  cliënt verdedigen of vertegenwoordigen in of in verband met een rechtsgeding, met inbegrip  van advies over het instellen of vermijden van een dergelijk rechtsgeding .(art 33 §2, art 34 §4  en 35 §3 AWW)”.

Wie op kantoor doet de melding en hoe? - gevolgen - persoon verantwoordelijk  voor de meldingen aan de CFI

14.6.1. Wie doet de meldingen ?

Het is uitsluitend de AMLCO die, binnen het kader van ons kantoor, eventueel een melding  mag doen aan de CFI.

Als deze niet beschikbaar is dient men contact te nemen met diens plaatsvervanger  waarvan men de naam kan terugvinden in punt 5 van deze handleiding.

In het uiterste geval kan de melding gebeuren door een medewerker die de hoedanigheid  heeft van een andere meldingsplichtige beroepsbeoefenaar van het kantoor..

Andere  medewerkers  zoals:  werknemers,  zelfstandige  medewerkers  (niet- beroepsbeoefenaars) hebben conform artikel 49 van de AWW in geen geval de  bevoegdheid om over te gaan tot het indienen van een melding bij de CFI.

Indien het kantoor van de CFI een verzoek (schriftelijk of telefonisch) ontvangt om  bijkomende inlichtingen te verstrekken, zal dit uitsluitend behandeld worden door de  AMLCO, diens plaatsvervanger of bij hun ontstententis een andere beroepsbeoefenaar.

14.6.2. Vorm van de melding

In ons kantoor wordt de melding in principe per e-mail gedaan op volgend adres: info@ctif- cfi.be

Een meldingsformulier bevindt zich in de modellenbundel of bij de CFI ( klik hier ). Voor de  rubrieken waarvoor men niet over de gevraagde inlichtingen beschikt, volstaat het de  vermelding “niet beschikbaar” te gebruiken.

14.6.3. Vertrouwelijk karakter van de melding: tipping off verbod.

Overeenkomstig artikel 55, § 1 van de AWW mogen de beroepsbeoefenaars van ons  kantoor, onze medewerkers en werknemers, in geen geval ter kennis brengen van de  betrokken cliënt of van derde personen dat er informatie werd meegedeeld aan de CFI of  dat een opsporingsonderzoek wegens witwassen van geld of financiering van terrorisme  aan de gang is of zou kunnen worden geopend. Dit is het zogenaamde “tipping off”  verbod.

Alle medewerkers, al dan niet beroepsbeoefenaars, die zijn tussengekomen in de opdracht  of in het dossier en die door de omstandigheden op de hoogte zouden zijn van een bij de  CFI neergelegde melding, moeten de confidentialiteitsverplichting, met inbegrip  tegenover de andere medewerkers, strikt respecteren.

Uitzonderingen: dit verbod tot mededeling geldt evenwel niet in volgende gevallen of  omstandigheden:

-  wanneer een beroepsbeoefenaar een cliënt tracht te ontraden deel te nemen aan  een illegale activiteit is er geen kennisgeving in voornoemde zin;

-  wanneer een beroepsbeoefenaar een kennisgeving doet aan het Instituut  waarvan hij/zij lid is (IAB, BIBF, IBR);

-  bij een kennisgeving voor repressieve doeleinden (aan parket, politie,  onderzoeksrechter); en

-  bij mededeling van de informatie aan andere beroepsbeoefenaars of advocaten of  notarissen, hetzij wanneer deze hun beroepsactiviteiten uitoefenen in dezelfde  entiteit of structuur waarin ons kantoor werkzaam is, hetzij wanneer zij  tussenkomen in verband met eenzelfde cliënt en in het kader van eenzelfde  verrichting. Voor verdere details zie artikel 56, §3, 3° van de AWW en de  Toelichtingsnota van de CFI van 26 oktober 2017

14.6.4. Immuniteit

De verstrekking te goeder trouw van informatie aan de CFI door de AMLCO, of bij zijn  afwezigheid, de betrokken beroepsbeoefenaar of de verantwoordelijke op het hoogste  niveau, vormt geen inbreuk op ongeacht welke op grond van een contract of van een  wettelijke, reglementaire of bestuursrechtelijke bepaling opgelegde beperking inzake de  openbaarmaking van informatie. De verstrekking te goeder trouw van informatie aan de  CFI leidt tot geen enkele vorm van aansprakelijkheid op burgerrechtelijk, strafrechtelijk en  tuchtrechtelijk vlak, noch tot nadelig of discriminatoir optreden van de werkgever, zelfs  indien deze niet precies op de hoogte waren van de onderliggende criminele activiteit, en  ongeacht of enige illegale activiteit daadwerkelijk heeft plaatsgevonden.

Behoud van de opdracht of van de cliënt nadat een melding werd gedaan.

De eventuele mogelijkheid tot verderzetting van de zakelijke relatie met de cliënt dient  gemotiveerd goedgekeurd te worden door de verantwoordelijke op het hoogste niveau .

15. BETALINGEN IN CONTANTEN

Wettelijk kader

## Art. 66

en 67 van de AWW  voorzien in specifieke bepalingen betreffende betaling in

contanten.

Hoe omgaan met vaststelling van inbreuken?

Het kantoor verwijst ter zake naar de gemeenschappelijke nota van de drie Instituten die  men hier kan vinden  http://www.bibf.be/uploads/documents/Communiqu%C3%A9_commun_sign%C3%A9_NL.p df

16. FINANCIELE EMBARGO’S

Wettelijk kader

## Art. 8

van de AWW  voorziet dat de kantoren rekening moeten houden met het bestaan

van fianciële embargo’s

Algemeen

De maatregelen inzake embargo’s en bevriezingen van tegoeden maken deel uit van het  stelsel van financiële sancties. Financiële sancties zijn beperkende maatregelen die worden  genomen tegenover regeringen van derde landen, personen of entiteiten (zoals  terroristische organisaties) met als doel een einde te maken aan bepaalde criminele  gedragspatronen.

Resolutie 1373 van 2001 van de Veiligheidsraad van de VN roept alle staten op om over te  gaan tot het bevriezen van de tegoeden en economische middelen van personen en  entiteiten die terroristische daden plegen of pogen te plegen, of aan het plegen van  dergelijke daden deelnemen of de uitvoering ervan vergemakkelijken. In aanvulling op  verordening 2580/2001, 881/2002 en het gemeenschappelijk standpunt 2001/931 heeft  België stappen ondernomen om een nationale lijst op te stellen.

De nationale lijst werd aangenomen en gewijzigd bij koninklijk besluit tot uitvoering van  het koninklijk besluit van 28 december 2006 inzake specifieke beperkende maatregelen  tegen bepaalde personen en entiteiten met het oog op de strijd tegen de financiering van  het terrorisme, bevestigd in artikel 155 van de wet van 25 april 2007 houdende diverse  bepalingen. Deze lijst wordt regelmatig geupdatet.

Toepassing

Rekening houdende met artikel 8 §1,3° van de AWW dient steeds nagegaan te worden of  een cliënt, een lasthebber of uiteindelijke begunstigde niet voorkomt op de nationale,

europese  of  internationale  lijst  die  men  kan  raadplegen  op  https://financien.belgium.be/nl/thesaurie/financiele-sancties .

Indien uit na een analyse van een knipperlicht de AMLCO dient te besluiten dat de cliënt,  een lasthebber, een UBO of de begunstigde van een verrichting beoogd wordt door een  financieel embargo of bevriezingmaatregelen wordt de volgende houding  aangenomen :

1. Verbod om een zakelijke relatie aan te gaan.

Het kantoor zal zich ervan onthouden een relatie aan te gaan met een persoon of  entiteit  die  voorkomt  in  een  lijst  van  de  financiële  embargo’s  of  bevriezingsmaatregelen.

2. Herbeoordeling van het risicoprofiel van de cliënt en daarmee verbonden personen en  desgevallend melding aan de CFI.

Het kantoor gaat over tot een herbeoordeling van het risicoprofiel van de cliënt, en de  ermee verbonden personen, die het voorwerp is van een financiële embargo of  bevriezingsmaatregel. Het kantoor zal een aangepaste waakzaamheid aan de dag leggen  ten aanzien van de cliënt en betrokken personen, alsook een grondig onderzoek  uitvoeren op eerdere verrichtingen of zakelijk relaties of die niet tot doel zouden kunnen  hebben om fondsen, financiële instrumenten of economische middelen ter beschikking te  stellen aan de op dergelijke lijst opgenomen persoon of entiteit of verbonden zijn met  witwassen  van  geld,  financiering  van  terrorisme  of  profilering  van  massavernietigingswapens.

Desgevallend zal de AMLCO overgaan tot de melding van een vermoeden.

17. WHISTLEBLOWING

Wettelijk kader:

## Art. 10

AWW bepaalt dat: De onderworpen entiteiten ontwikkelen en leggen passende procedures ten uitvoer die  evenredig zijn met hun aard en omvang, om hun personeelsleden of hun agenten of  distributeurs in staat te stellen om aan de personen die aangewezen zijn op grond van artikel  9 van de wet, via een specifiek, onafhankelijk en anoniem kanaal, de inbreuken bij het  vervullen van de verplichtingen bepaald bij dit boek , te melden .

## Art. 36

AWW bepaalt bovendien :

“ Elke onderworpen entiteit zorgt ervoor dat haar personeelsleden, alsook haar agenten en  distributeurs die een verrichting die ze als atypisch beschouwen in de zin van artikel 35, § 1, 1°,  of het feit dat ze niet kunnen voldoen aan de waakzaamheidsverplichtingen bedoeld in de  artikelen 33, § 1, 34, § 3, en 35, § 2, intern melden, worden beschermd tegen elke bedreiging  of daad van agressie, en in het bijzonder tegen nadelig of discriminerend optreden van de  werkgever .”

Artikel 90: AWW:

“De toezichtautoriteiten stellen effectieve en betrouwbare mechanismen in voor de melding  door de leidinggevenden, personeelsleden, agenten en distributeurs van de onderworpen  entiteiten of door derden, aan deze autoriteiten, van mogelijke of werkelijke inbreuken op  de bepalingen van deze wet, van de besluiten of reglementen genomen ter uitvoering ervan,  van de uitvoeringsmaatregelen van Richtlijn 2015/849, van de Europese verordening  betreffende geldovermakingen, en van de waakzaamheidsplichten bedoeld in de bindende  bepalingen betreffende financiële embargo's

Algemeen

De AWW vereist de invoering van twee meldingsprocedures voor whistleblowing:

De ene is een interne procedure en moet door het kantoor ingevoerd worden om de  personeelsleden en medewerkers in staat te stellen inbreuken op de verplichtingen  vermeld in Boek II van de AWW (d.w.z. artikel 8 tot en met artikel 65 van de AWW ) te  melden aan de AMLCO of aan de verantwoordelijke persoon op het hoogste niveau.

Anderzijds bepaalt de AWW ook dat elke toezichthoudende autoriteit, verplicht is om  mechanismen op te zetten die bestuurders, personeelsleden, agenten, distributeurs en  derden in staat stellen om vermoedelijke of bewezen inbreuken op de volledige AWW,  alsook op uitvoeringsbesluiten en –verordeningen, te melden.

Er is geen verplichting om bovengenoemde inbreuken te melden. In voorkomend geval  wordt de keuze tussen de interne meldingsprocedure of de procedure voor de melding aan  de Toezichtautoriteit volledig overgelaten aan de medewerker/personeelslid. Indien van  toepassing kan een inbreuk ook via de twee kanalen gemeld worden.

## VOORBEELDEN

Voorbeeld  1 :  een  medewerker  stelt  vast  dat  er  geen  identificatie-  en/of  identiteitsverificatieprocedure bestaat binnen het kantoor. Volgens artikel 10 van de AWW  kan de medewerker dit intern melden en/of aan de Toezichtsautoriteit, overeenkomstig  artikel 90 van de AWW.

Voorbeeld 2 : een medewerker stelt een atypische verrichting vast in een dossier. Hij moet  dit melden aan de AMLCO (punt 12 van deze handleiding). Een dergelijke melding valt dus  niet onder art. 10 of 90 van de AWW. Het is dus absoluut niet de bedoeling om atypische  verrichtingen aan de Toezichtsautoriteit te melden.

17.2.1. In ons kantoor: een specifiek, onafhankelijk en anoniem kanaal

Elk kantoor dient hier te omschrijven op welke wijze de medewerkers inbreuken bij het  vervullen van de verplichtingen bepaald bij Boek II van de AWW kunnen melden: bv via een  getypte brief te deponeren in een bepaalde brievenbus binnen het kantoor of via de

gegevens van de interne vertrouwenspersoon aan wie dergelijke meldingen kunnen  gebeuren. De meldingen moeten anoniem kunnen gebeuren.

De persoon belast met het behandelen van de meldingen maakt deze, naar gelang het  geval, over aan de AMLCO of aan de verantwoordelijke op het hoogste niveau, die de  gepaste maatregelen neemt.

17.2.2. Melding aan de toezichtautoriteiten

Deze specifieke meldingsmogelijkheid aan een toezichtautoriteit geldt voor alle  vermoedelijke of bewezen inbreuken op de AWW (met inbegrip van inbreuken met  betrekking tot de beperking van contanten) en is dus niet uitsluitend beperkt tot  inbreuken op boek II.

17.2.3. Wie kan een melding doen?

Elke persoon (vaste of tijdelijke, interne of externe werknemer, of zelfstandige  medewerker, statutair personeelslid, stagiair, enz.) die mogelijke of werkelijke inbreuken  op de AWW vaststelt, kan deze melden.

De AWW biedt bescherming aan personen die te goeder trouw een inbreuk op de AWW  melden bij een toezichtsautoriteit.

Zo kan een melding geen aanleiding geven tot burgerrechtelijke, strafrechtelijke of  tuchtrechtelijke vorderingen of tot professionele sancties. Deze personen worden niet  beschouwd als personen die contractueel of wettelijk opgelegde beperkingen op de  openbaarmaking of de verstrekking van informatie schenden en kunnen op geen enkele  wijze aansprakelijk worden gesteld voor de melding van deze informatie.

De melders worden beschermd tegen ongunstige of discriminatoire behandeling, zoals  vergelding, discriminatie en andere vormen van onbillijke behandelingen of nadelige  beslissingen (bv. ontslag, loonvermindering, wijziging van functie of van jobinhoud) door  hun werkgever in verband met of als gevolg van de melding van een inbreuk.

18. FORMULIEREN

Hieronder kan de AMLCO kort omschrijven welke documenten (formulieren,  modelverslagen) of software door het kantoor gebruikt worden om de verplichtingen  inzake de toepassing van de AWW na te komen en te registreren.

Deze modellen of een beschrijving van de gebruikte software kunnen afzonderlijk  gebundeld worden of toegevoegd worden aan de praktische handleiding voor de  medewerkers.

19. BIJLAGEN BIJ DE AWW

## Bijlage I

## Art. 1

De variabelen die de onderworpen entiteiten ten minste in overweging nemen

in hun integrale risicobeoordeling bedoeld in artikel 16, tweede lid, zijn de volgende :

1° het doel van een rekening of een relatie;

2° de omvang van de activa die door een cliënt worden gedeponeerd of de omvang van  de gesloten verrichtingen;

3° de regelmaat of de duur van de zakelijke relatie.

## Bijlage II

## Art. 1

De indicatieve factoren van een potentieel lager risico bedoeld in de artikelen 16, tweede lid, en 19, § 2, zijn de volgende :

1° cliëntgebonden risicofactoren :

a) beursgenoteerde vennootschappen die onderworpen zijn aan informatievereisten (op  grond van het beursreglement of krachtens wettelijke of afdwingbare middelen) welke  voorschriften omvatten om toereikende transparantie betreffende de uiteindelijke  begunstigden te garanderen;

b) overheden of overheidsbedrijven;

c) cliënten die inwoner zijn van geografische gebieden met een lager risico als vermeld in  punt 3° ;

2° risicofactoren verbonden aan producten, diensten, verrichtingen of leveringskanalen :

a) levensverzekeringsovereenkomsten met een lage premie;

b) pensioenverzekeringsovereenkomsten die geen afkoopclausule bevatten en niet als  zekerheidstelling kunnen dienen;

c) een pensioenstelsel, een pensioenfonds of een soortgelijk stelsel dat pensioenen  uitkeert aan werknemers, waarbij de bijdragen worden ingehouden op het loon en de  regels van het stelsel de deelnemers niet toestaan hun rechten uit hoofde van het stelsel  over te dragen;

d) financiële producten of diensten die op passende wijze bepaalde en beperkte diensten  voor bepaalde soorten cliënten omvatten, om voor financiële inclusiedoeleinden de  toegang te vergroten;

e) producten waarbij het WG/FT-risico wordt beheerd door andere factoren zoals  bestedingslimieten of transparantie van eigendom (bv. bepaalde soorten elektronisch  geld);

3° geografische risicofactoren :

a) lidstaten;

b) derde landen met doeltreffende systemen ter bestrijding van WG/FT;

c) derde landen die volgens geloofwaardige bronnen een laag niveau van corruptie of  andere criminele activiteit hebben;

d) derde landen die volgens geloofwaardige bronnen zoals wederzijdse beoordelingen,  gedetailleerde evaluatierapporten, of gepubliceerde follow-uprapporten, voorschriften  inzake de bestrijding van WG/FT hebben die beantwoorden aan de herziene FAG- aanbevelingen en die voorschriften effectief ten uitvoer leggen.

## Bijlage III

## Art. 1

De indicatieve factoren van een potentieel hoger risico bedoeld in de artikelen 16, tweede lid, en 19, § 2, zijn de volgende :

1° cliëntgebonden risicofactoren :

a) de zakelijke relatie vindt plaats in ongebruikelijke omstandigheden;

b) de cliënten die inwoner zijn van geografische gebieden met een hoog risico bedoeld  onder 3° ;

c) rechtspersonen of juridische constructies die vehikels zijn voor het aanhouden van  persoonlijke activa;

d) vennootschappen met gevolmachtigde aandeelhouders ("shareholders") of met  aandelen aan toonder;

e) bedrijven waar veel geldverkeer in contanten plaatsvindt;

f) de eigendomsstructuur van de vennootschap lijkt ongebruikelijk of buitensporig  complex gezien de aard van de vennootschapsactiviteit;

2° risicofactoren verbonden aan producten, diensten, verrichtingen of leveringskanalen :

a) private banking;

b) producten of verrichtingen die anonimiteit bevorderen;

c) zakelijke relaties op afstand of verrichtingen op afstand, zonder sommige garanties,  zoals elektronische handtekeningen;

d) betalingen die worden ontvangen van onbekende of niet-verbonden derden;

e) nieuwe producten en nieuwe zakelijke praktijken, daaronder begrepen nieuwe  leveringsmechanismen, en het gebruik van nieuwe of in ontwikkeling zijnde  technologieën voor zowel nieuwe als reeds bestaande producten.

3° geografische risicofactoren :

a) onverminderd artikel 38, landen die op basis van geloofwaardige bronnen zoals  wederzijdse beoordelingen, gedetailleerde evaluatierapporten, of gepubliceerde follow- uprapporten, worden aangemerkt als een land zonder effectieve WG/FT-systemen;

b) landen die volgens geloofwaardige bronnen significante niveaus van corruptie of  andere criminele activiteit hebben;

c) landen waarvoor sancties, embargo's of soortgelijke maatregelen gelden die  bijvoorbeeld door de Europese Unie of de Verenigde Naties zijn uitgevaardigd;

d) landen die financiering of ondersteuning verschaffen voor terroristische activiteiten, of  op het grondgebied waarvan als terroristisch aangemerkte organisaties actief zijn.

20. ALGEMENE RISICOBEOORDELING – MODEL 1

De hieronder opgesomde risicofactoren worden, tenzij anders aangeduid, beschouwd als  risicoverhogende factoren. De aanwezigheid, de frequentie en/of omvang van de  betrokken bedragen van deze factoren verhoogt de blootstelling van het kantoor aan het  WG/FT-risico.

Risicofactoren in verband met het doel van de zakelijke relatie

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Krijgt het kantoor vragen tot fiscaal- financieel advies met als doel vermogen  te verbergen?

Krijgt het kantoor vragen tot het  opzetten van complexe  vennootschapsstructuren ?

Krijgt het kantoor opdrachten in verband  met koop verkoop van onroerende  goederen?

Krijgt het kantoor vragen om bijstand te  geven bij financiële verrichtingen zoals  verrichten van betalingen, aandelen te  kopen/verkopen, wisseloperaties uit te  voeren ?

Krijgt het kantoor vragen van cliënten  hen aan te brengen bij financiële  instellingen ?

Risicofactoren in verband met de omvang van de activa die door een cliënt worden  gedeponeerd of de omvang van de gesloten verrichtingen

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Krijgt het kantoor vragen om grote bedragen  in ontvangst te nemen, al dan niet op een  derdenrekening ?

Risicofactoren in verband met de regelmaat of duur van de zakelijke relatie.

De eenmaligheid of het hoogdringend karakter van een opdracht wordt in het algemeen  beschouwd als een risicoverhogende factor wegens mogelijks onvoldoende mogelijkheid  om onvoldoende inzicht te verwerven in de cliënt en/of verrichtingen.    Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Krijgt het kantoor veel te  maken met éénmalige  opdrachten ?

Krijgt het kantoor veel te  maken hoogdringende  opdrachten ?

Het gegeven dat een zakelijke relatie zich op lange termijn afspeelt wordt in het algemeen  beschouwd als een risicoverlagende factor daar er voldoende tijd is om inzicht te  verwerven  in  cliënt  en/of  verrichtingen  Relevantie  NEEN= komt in het geheel niet voor (= enkel opdrachten op korte termijn)  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt dat een zakelijke relatie zich op lange termijn afspeelt  hoe lager in dit geval het risico.: LAAG (in geval van JA) STANDAARD  (occassioneel/beperkte omvang), HOOG (regelmatig:)  Verantwoording: Dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Zijn de zakelijke relaties vooral op de  lange termijn gericht ?

Risicofactoren in verband met de sectoren waarin onze cliënten actief zijn

Ons kantoor heeft cliënten in volgende sectoren die mogelijk een hoger risico op WG/FT  inhouden. Onderstaande lijst werd opgemaakt op basis van gegevens uit de  jaarverslagen en nationale risicoanalyse van de CFI.

Handelaars in goud en edele metalen

Import-/Exportbedrijven

Juweliers en horlogemakers

Bedrijfsadviseurs en dienstverleners van beleggingsdiensten

Bouwbedrijven

Handelaars in tweedehandsvoertuigen

Diamantairs

Geldkoeriers (fysiek, grensoverschrijdend transport van  contanten)

Makelaars

Handelaars in alcohol en tabak

Dienstverleners horeca

Handelaars in telefoonkaarten en nachtwinkels

Wisselkantoren / betalingsinstellingen

Cliënten met banden met landen met een hoog risico

Cliëntgebonden risicofactoren

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Heeft het kantoor zakelijke relaties die  plaatsvinden in ongebruikelijke  omstandigheden ?

Heeft het kantoor als cliënt personen die  inwoner zijn van geografische gebieden  met een hoog risico of daar zaken mee  doen ?

Heeft het kantoor als cliënt  rechtspersonen of juridische constructies  die vehikels zijn voor het aanhouden van  persoonlijke activa?

Heeft het kantoor als cliënt  vennootschappen met gevolmachtigde  aandeelhouders ("shareholders") of met  aandelen aan toonder ?

Heeft het kantoor als cliënt bedrijven waar  veel geldverkeer in contanten plaatsvindt?

Heeft het kantoor als cliënt  ondernemingen met een complexe  eigendomsstructuur ?

Heeft het kantoor cliënten die actief zijn in  sectoren met een hoog risico (zie 20.3)

Risicofactoren in verband met de door het kantoor/netwerk aangeboden diensten

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Worden er door het kantoor producten of  verrichtingen die anonimiteit of verbergen  van de identiteit bevorderen geleverd of  gedaan?

Heeft het kantoor zakelijke relaties op  afstand of verrichtingen op afstand,  zonder sommige garanties, zoals  elektronische handtekeningen ?

Kan het kantoor betalingen ontvangen van  onbekende of niet-verbonden derden ?

Ontwikkelt het kantoor nieuwe producten  en nieuwe zakelijke praktijken, daaronder  begrepen nieuwe leveringsmechanismen,  en het gebruik van nieuwe of in  ontwikkeling zijnde technologieën voor  zowel nieuwe als reeds bestaande  producten?

Geografische risicofactoren met betrekking tot kantoor/netwerk

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Heeft het kantoor activiteiten in  landen, andere dan die bedoeld in  artikel 38 AWW , die op basis van  geloofwaardige bronnen zoals  wederzijdse beoordelingen,  gedetailleerde evaluatierapporten, of  gepubliceerde follow-uprapporten,  worden aangemerkt als een land  zonder effectieve WG/FT-systemen? :  zie :  https://financien.belgium.be/nl/landen- met-een-hoog-risico

Heeft het kantoor activiteiten in landen  die volgens geloofwaardige bronnen  significante niveaus van corruptie of  andere criminele activiteit hebben?

Heeft het kantoor activiteiten in landen  waarvoor sancties, embargo's of  soortgelijke maatregelen gelden die  bijvoorbeeld door de Europese Unie of  de Verenigde Naties zijn uitgevaardigd;?  Zie :  https://financien.belgium.be/nl/thesauri e/financiele-sancties

Heeft het kantoor activiteiten in landen  die financiering of ondersteuning  verschaffen voor terroristische  activiteiten, of op het grondgebied

waarvan als terroristisch aangemerkte  organisaties actief zijn?

Het kantoor maakt gebruik van  derdezaakaanbrengers die actief zijn in  een land met een hoger WG/FT risico

Risicofactoren in verband met de afstand bij het tot standkomen van de zakelijke  relatie

Bij het identificeren van het risico dat is verbonden aan de manier waarop de cliënt de  producten of diensten die hij verlangt verkrijgt, houden we rekening met het risico dat  verband houdt met de mate waarin de zakelijke relatie op afstand wordt onderhouden;

Het gegeven dat de identificatie op afstand gebeurt wordt beschouwd als een  risiciverhogende factor

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Maakt het kantoor gebruik van  identificatie op afstand ?

Risicofactoren in verband met de wijze waarop ons cliënteel in contact komt het  kantoor – rol van tussenpersonen

Bij het gebruik maken van een tussenpersoon, al dan niet derde zaakaanbrenger worden  volgende elementen als risicoverlagend beschouwd:

➢  De tussenpersoon is een aan de AWW onderworpen tussenpersoon zoals bedoeld  in artikel 5 van de AWW of geviseerd in de Richtlijn (EU) 2015/849

➢   Is de tussenpersoon onderworpen aan doeltreffend AWW-toezicht ?

Relevantie  NEEN= komt in het geheel niet voor  JA = komt wel voor  Risiconiveau: hoe meer het voorkomt hoe hoger het risico.: LAAG (in geval van neen),  STANDAARD (occassioneel/beperkte omvang), HOOG (regelmatig)  Verantwoording: dit is erg belangrijk, omdat de algemene risicobeoordeling moet worden  gedocumenteerd en moet worden gerechtvaardigd tegenover de toezichtautoriteit. Dit  zal het ook gemakkelijker maken om de periodieke herziening en actualisering van de risico  beoordeling uit te voeren.

Relevantie  Risiconiveau  Verantwoording

Zijn derde zaakaanbrengers  die het kantoor gebruikt aan  AWW-verplichtingen  onderworpen personen

Besluit

Zie 6.4. Het kantoor maakt op basis van deze vragen een algemeen besluit over het  risicioniveau

21. ALGEMENE RISICOBEOORDELING – MODEL 2

Toelichting

De algemene risicobeoordeling is een proces in drie stappen dat bestaat uit (i) het  identificeren van de WG/FT-risico's waaraan u wordt blootgesteld, (ii) deze evalueren en  (iii) om, op basis van uw beoordeling, risicocategorieën te definiëren.

De algemene risicobeoordeling moet worden afgestemd op de aard van uw activiteit en op  de omvang van uw kantoor.

De tabel « Mijn algemene risicobeoordeling » die u van de website kunt downloaden,  heeft als doel u te helpen om de risico’s eigen aan uw kantoor en uw activiteit te  identificeren en te evalueren, en om de risicocategorieën te definiëren, en bijgevolg om  uw algemene risicobeoordeling uit te voeren.

Deze tabel bevat onder het tabblad « definitie van termen » de definitie of verklaring van  bepaalde gebruikte termen zoals « uiteindelijk begunstigde», « derde land met een hoog  risico », « land onderworpen aan sancties of embargo's », « belastingparadijs » en « politiek  prominente persoon ».

Hoe de tabel « Mijn algemene risicobeoordeling » invullen?

21.2.1. Identificatie van de WG/FT-risico's

De algemene risicobeoordeling WG/FT wordt uitgevoerd op het niveau van uw kantoor en  bestaat, in een eerste fase, uit het identificeren van de risico's waaraan uw kantoor  objectief wordt blootgesteld, rekening houdend met de activiteit en de manier waarop  deze wordt uitgeoefend.

Bij uw algemene risicobeoordeling moet u, verplicht, rekening houden met:

✓ de kenmerken van uw klanten;  ✓ de kenmerken van de producten of transacties die u aanbiedt;  ✓ de betrokken landen of geografische gebieden;  ✓ de distributiekanalen die u gebruikt;  ✓ de variabelen die zijn opgenomen in bijlage I van de wet van 18 september 2017;  ✓ de indicatieve factoren die wijzen op een potentieel hoger risico als bedoeld in

bijlage III van de wet van 18 september 2017;

✓ de indicatieve factoren die wijzen op een potentieel lager risico als bedoeld in bijlage

II van de wet van 18 september 2017

✓ alle andere relevante risicofactoren.

Om uw risico’s te identificeren, moet u ook rekening houden met alle andere relevante  informatie waarover u beschikt 6 .

De tabel opgenomen in het tabblad « Mijn algemene risicobeoordeling » bevat een lijst met  risicofactoren die kunnen bijdragen aan het verhogen of verlagen van WG/FT-risico’s en die  mogelijk relevant zijn bij het uitvoeren van uw beroepsactiviteiten.

De bovengenoemde risicofactoren zijn gegroepeerd in 3 verschillende tabellen, in functie  van de betreffende risicocategorieën: (i) klanten, (ii) producten of verrichtingen, (iii)  landen of geografische gebieden en distributiekanalen. Duid in elke tabel de risicofactoren  aan die relevant of niet-relevant zijn voor uw kantoor.

Houdt er rekening mee dat de lijst met risicofactoren niet exhaustief is. Het is daarom  noodzakelijk om de tabel te vervolledigen met de risicofactoren die relevant zijn voor uw  eigen activiteiten en die niet in de tabel zouden zijn opgenomen. Voor dit doel is in elk van  de drie tabellen een rubriek « andere risicofactoren (eigen aan uw kantoor) » toegevoegd.

21.2.2. Evaluatie van de geïdentificeerde WG/FT-risico’s

In een tweede stap is het noodzakelijk om de risico's WG/FT te evalueren die u hebt  geïdentificeerd als relevant voor uw activiteit.

Binnen elke categorie (dwz "klanten", "producten / verrichtingen", "land / geografische  gebieden"/"distributiekanalen") groepeert u verschillende risicofactoren waarvan de  combinatie overeenstemt met uw activiteit. In de categorie “klanten” kunt u bijvoorbeeld,  afhankelijk van uw activiteit, een combinatie maken met de naam “klanten met woonplaats  in België die PPP’s zijn” die u onderscheidt van de combinatie “klanten met woonplaats in  België die niet PPP’s zijn”.

Vervolgens associeert u met elk van de aldus vastgestelde combinaties een risiconiveau  (bijvoorbeeld: laag, standaard, hoog). Daarbij houdt u in ieder geval rekening met het doel  van de relatie, de omvang van de gesloten transacties en de regelmaat of duur van de  zakelijke relatie 7 .

Verantwoord vervolgens uw beoordeling van het risiconiveau van elke combinatie van  risicofactoren in de kolom "verantwoording". Deze verantwoording is erg belangrijk,  omdat uw algemene risicobeoordeling moet worden gedocumenteerd en moet worden  gerechtvaardigd tegenover de toezicht. Dit zal het ook gemakkelijker maken om de  periodieke herziening en actualisering van de risico beoordeling uit te voeren.

Zorg ervoor dat u het risiconiveau dat u met de gedefinieerde situaties associeert,  rechtvaardigt om uw evaluatie te documenteren!

Zorg er ook voor dat u uw tabel « Mijn algemene risicobeoordeling » dateert. Dit zal ervoor  zorgen dat u een historiek van de opeenvolgende updates kunt bijhouden.

21.2.3. Visualisering - dashboard

Nadat u het tabblad « Mijn algemene risicobeoordeling » hebt voltooid, vindt u op het  tabblad "dashboard" een visuele presentatie van de resultaten van uw algemene  risicobeoordeling. In dit dashboard wordt een visualisatie gegeven voor elk van de  risicocategorieën van a) het aantal risicofactoren, b) de verdeling van deze factoren op  basis van hun relevantie voor uw activiteit, en c) combinaties genomen op basis van hun  risiconiveau. Dit dashboard wordt automatisch ingevuld op basis van de informatie die u  hebt ingevoerd in het tabblad « Mijn algemene risicobeoordeling ».

Bijlage : tabel algemene risicobeoordeling

22. RISICOBEOORDELINGVAN CLIËNT – RICHTSNOEREN FAG 8

OPMERKING : hetgeen hieronder vermeld staat is een voorbeeld. Elk kantoor dient dit  individueel te beoordelen en desgevallend aan te passen. De voorbeelden steunen op  gegevens afkomstig uit jaarverslagen van de CFI alsook van nota’s van de FAG (Financiële  Actiegroep)  en  kunnen  beschouwd  worden  als  een  werkbasis.

Bij het identificeren van het aan onze cliënten verbonden risico, met inbegrip van de UBO’s  van de cliënten, houdt ons kantoor rekening met het risico dat verband houdt met:

➢ De geografische aspecten van de zakelijke relatie  ➢ De cliënt  ➢ De diensten en leveringskanalen

Risicofactoren verbonden aan bepaalde landen en geografische gebieden

Bij het identificeren van het aan landen en geografische gebieden verbonden risico houdt  ons kantoor rekening met het risico dat verband houdt met:

A. de landen waar de cliënt en/of de UBO is/zijn gevestigd;

B. de landen waar de cliënt en/of de UBO hun hoofdvestiging hebben of het meeste van

hen activiteiten doen;

### C. oorsprong/bewaarplaats van vermogen/fondsen.

Er bestaat geen universeel aanvaarde definitie die bepaalt of een specifiek land of  geografisch gebied een verhoogd risico inhoudt. Men kan evenwel aannemen dat klanten  een hoger risico inhouden als zij gevestigd zijn in of verbonden zijn met een land dat, of als  het land van herkomst of bestemming van de diensten een land is dat:

a)  onderworpen is aan sancties, embargo’s of gelijkaardige maatregelen  uitgevaardigd  door  bijvoorbeeld  de  Verenigde  Naties.  In  bepaalde  omstandigheden omvat dit landen die onderworpen zijn aan sancties of  gelijkaardige maatregelen als deze uitgevaardigd door instellingen zoals de  Verenigde Naties;

b)  door geloofwaardige bronnen werd geïdentificeerd als een land dat geen  wetgeving, regelgeving of andere maatregelen heeft aangenomen ter bestrijding  van witwassen van geld of financiering van terrorisme;

c)  door geloofwaardige bronnen werd geïdentificeerd als een land dat financiering  of bijstand verleent aan terroristische activiteiten door actieve contacten met  terroristische organisaties;

d)  door geloofwaardige bronnen werd geïdentificeerd als een land dat gekend is  voor zijn verregaande corruptie of andere criminele praktijken.

e)  een vestigingland is dat op de lijst van “Non Co-operative Countries and  Territories” (NCCT) van de FATF staat;

f)  door geloofwaardige bronnen geïdentificeerd is als niet-medewerkzaam in zake  het voorzien van UBO-informatie en/of het gebruik van aandelen aan toonder  toelaten en dus toelaten om de uiteindelijke begunstigde verborgen te houden

Actuele informatie over derde landen en het al dan niet hoog WG/FT-risico vinden we op:  https://financien.belgium.be/nl/landen-met-een-hoog-risico :

Indien ons kantoor zaken doet met natuurlijke of rechtspersonen die ingezetene zijn van  of gevestigd zijn in derde landen die werden geïdentificeerd als landen met een hoog  WG/FT-risico, past ons kantoor altijd maatregelen van verscherpte waakzaamheid toe.

Risicofactoren verbonden aan de cliënt

Dit zijn de belangrijkste risicofactoren waarmee we rekening moeten houden:

a)  de cliënten die PPP’s zijn of personen die nauwe banden hebben met of verwant zijn  met PPP’s, worden beschouwd als cliënten met een hoger risico;

b)  de cliënten die zaken doen of diensten vragen in ongewone of ongebruikelijke  omstandigheden

c)  de cliënten waarbij het door de structuur of de aard van de entiteit of van de relatie  moeilijk is om tijdig de echte UBO(‘s) of de meerderheidsaandeelhouder te  identificeren of cliënten die proberen om onduidelijkheid te scheppen over hun  activiteiten, de eigendom of de aard van hun transacties, zoals bijvoorbeeld:

i.  onverklaard  gebruik  van  fictieve  en  slapende  vennootschappen,  dekmantelbedrijven, juridische entiteiten met eigendomsrechten via fiducie of  partage of aandelen aan toonder, leiding door gevolmachtigden (stromannen) en  bedrijfsdirecteurs, rechtspersonen of rechtsregelingen, splitsing tussen de  statutaire zetel en de werkelijke bedrijfszetel (waar de middelen werkelijke beheerd  worden) over verschillende landen, dit alles zonder duidelijke juridische of  rechtmatige fiscale, zakelijke, economische of andere redenen;

ii.  onverklaard gebruik van informele regelingen zoals familieleden of nauwe partners  die optreden als gevolmachtigde aandeelhouders of bestuurders of cliënten die  lijken te handelen op instructies van anderen, zonder dat dit wordt bekendgemaakt;

iii.  ongebruikelijke complexiteit in de bestuurs- of eigendomsstructuren zonder  duidelijke verklaring.

d)  bedrijven van cliënten met een aanzienlijk deel van hun activiteiten of met  belangrijke dochterondernemingen in landen met een groter geografisch risico;

e)  cliënten met bedrijven waarin veel liquide middelen (en/of snel vrij te maken  middelen) omgaan. Dit is bv. het geval bij:

i. Money of Value Transfer Services (MVTS) bedrijven die geldtransferdiensten  aanbieden. Indien dergelijke cliënten (bv. MVTS-bedrijven) zelf onderworpen zijn  aan en gereglementeerd zijn conform de AWW of de EU-richtlijn, helpt dit om de  risico’s te beperken;

ii. operatoren, makelaars en anderen die diensten rond virtuele activa verlenen;

iii. casino’s, gokkantoren en andere gokgerelateerde instellingen en activiteiten.

f)  bedrijven die gewoonlijk niet veel liquide middelen hebben en toch lijken te  beschikken over grote hoeveelheden liquide middelen;

g)  bedrijven die sterk afhankelijk zijn van nieuwe technologieën (bv. online  handelsplatformen) die inherent kwetsbaar zijn voor misbruiken door criminelen,  vooral indien deze niet gereguleerd zijn voor AML/FT;

h)  cliënten die een beroep doen op financiële tussenpersonen, financiële instellingen  of niet-financiële beroepen en beroepsuitoefenaars (DNFBP’s) die niet  onderworpen zijn aan gepaste AML/FT-wetten en maatregelen en die niet naar  behoren onder toezicht staan van toezichtoverheden;

i)  cliënten die actief en zonder verklaring contacten face-to-face lijken te vermijden of  die af en toe zonder legitieme redenen instructies geven en voor het overige  ontwijkend optreden of moeilijk te bereiken zijn op momenten wanneer ze normaal  naar verwachting wel bereikbaar zouden moeten zijn;

j)  cliënten die vragen om transacties op ongewoon korte termijn of versneld af te  handelen zonder redelijke verklaring voor de versnelde transactie, waardoor het  voor de beroepsbeoefenaar moeilijk is om een gepaste risicobeoordeling uit te  voeren;

k)  cliënten die beschikken over fondsen 9 die duidelijk en zonder enige verklaring niet  in verhouding staan tot hun situatie (bv. hun leeftijd, inkomsten, beroep of  vermogen);

l)  cliënten die ongewoon hoge honoraria betalen voor diensten waarvoor zoiets  gewoonlijk niet gerechtvaardigd is. Bonafide en gepaste afspraken voor  resultaatafhankelijke honoraria, waarbij een beroepsbeoefenaar een aanzienlijke  premie krijgt voor een geslaagde dienstverlening, hoeven echter niet beschouwd te  worden als een risicofactor;

m)  ongebruikelijk grote activa of ongebruikelijk grote transacties in verhouding tot wat  billijkerwijze verwacht mag worden van cliënten met een gelijkaardig profiel,  kunnen erop wijzen dat een cliënt die anders niet als een cliënt met een groter risico  wordt beschouwd, toch als dusdanig moet worden behandeld. Omgekeerd kan een  beroepsbeoefenaar bij kleine activa of transacties van lage waarde bij een cliënt die  anders een hoger risiconiveau lijkt te hebben, deze cliënt behandelen als een cliënt  met een lager risico;

n)  cliënten waarvan wordt vermoed dat zij betrokken zijn bij vervalsingen door het  gebruik van valse leningen, valse facturen en misleidende benamingen;

o)  de overdracht van de zetel van een bedrijf naar een ander rechtsgebied zonder  authentieke economische activiteiten in het land waarnaar de zetel wordt verhuisd,  gaat gepaard met een risico op de oprichting van lege bedrijven die gebruikt kunnen  worden om de uiteindelijke begunstigde te verdoezelen;

p)  de verhouding tussen het personeelsaantal/de personeelsstructuur en de aard van  het bedrijf wijkt af van de norm voor de sector (bv. de omzet van een bedrijf is  onredelijk hoog in vergelijking met het personeelsaantal en de gebruikte activa in  vergelijkbare bedrijven);

q)  plotse activiteit van een voordien slapend bedrijf zonder duidelijke verklaring;

r)  indicatoren dat de cliënt geen moeite doet om de nodige erkenningen of  registraties door de overheid te verkrijgen, enz;

s)  de reden waarom de cliënt voor het kantoor kiest is onduidelijk, gezien de omvang,  de locatie of de specialisatie van het kantoor;

handelsinkomsten of betalingen door een trust), terwijl de bron van vermogen de activiteiten beschrijft die  de totale nettowaarde van een cliënt hebben gegenereerd (bv. eigendom van een bedrijf, erfenis of  beleggingen). Hoewel de bronnen van fondsen en van vermogen voor sommige cliënten identiek kunnen  zijn, kunnen ze geheel of gedeeltelijk verschillen voor andere cliënten. Voorbeeld: een PEP met een laag  officieel salaris die echter over veel fondsen beschikt, zonder duidelijke zakelijke belangen of erfenis, kan  vermoedens van omkoping, corruptie of misbruik van functie oproepen. In het kader van de RBA moeten  beroepsbeoefenaars ervoor zorgen dat ze beschikken over de gepaste informatie om na te gaan of de  bronnen van fondsen en van vermogen van een cliënt rechtmatig zijn, met een mate van zekerheid die  evenredig is met het risicoprofiel van de cliënt.

t)  frequente of onverklaarde wijzigingen bij de professionele adviseurs of de leden  van het management;

u)  de cliënt weigert om alle relevante gegevens te verstrekken of de  beroepsbeoefenaar heeft gegronde twijfels of de verstrekte informatie correct is  en volstaat.

Risico’s verbonden aan de dienstverlening-leveringskanalen

Volgende diensten die kunnen worden verstrekt door ons kantoor kunnen (in bepaalde  omstandigheden) het risico lopen om gebruikt te worden in het kader van het WG/FT:

a)  onverklaard (in gevallen waarin een verklaring gewettigd is) gebruik van  gemeenschappelijke cliëntenrekeningen of bewaarneming van activa of gelden van  cliënten;

b)  diensten waarbij beroepsbeoefenaars in de praktijk het prestige, de reputatie en de  geloofwaardigheid van de cliënt kunnen vertegenwoordigen of garanderen  tegenover derden, zonder een grondige kennis van de zaken van de cliënt;

c)  diensten die in grote mate steunen op nieuwe technologieën (bv. online  handelsplatformen) die inherent kwetsbaar kunnen zijn voor misbruik door  criminelen;

d)  overdracht van vastgoed of andere goederen of activa van grote waarde tussen  partijen binnen een termijn die ongebruikelijk kort is voor gelijkaardige transacties  zonder duidelijke juridische, fiscale, commerciële, economische of andere legitieme  redenen;

e)  gebruik van virtuele activa of andere anonieme betalingsmiddelen en middelen  voor vermogensoverdracht binnen de transactie zonder duidelijke juridische,  fiscale, commerciële, economische of andere legitieme redenen;

f)  Transacties waarbij ongebruikelijke betaalmiddelen worden gebruikt (bv. edele  metalen of edelstenen);

g)  inbrengen of overdrachten van goederen waarvan de waarde moeilijk te bepalen is  (bv. juwelen, edelstenen, kunstvoorwerpen of antiek, virtuele activa) indien dat niet  gebruikelijk is voor het type van cliënten, transacties of in de normale activiteiten  van  de  beroepsbeoefenaar  zoals  een  overdracht  naar  een  vennootschapsrechtelijke entiteit, of over het algemeen zonder een gepaste uitleg;

h)  opeenvolgende kapitaalinbrengen of andere inbrengen in hetzelfde bedrijf binnen  een korte termijn, zonder duidelijke juridische, fiscale, commerciële, economische  of andere legitieme redenen;

i)  overnames van bedrijven in liquidatie zonder duidelijke juridische, fiscale,  commerciële, economische of andere legitieme redenen;

j)  transacties waarbij nauw verbonden personen betrokken zijn en waarvoor de cliënt  en/of zijn financiële adviseurs inconsistente of irrationele redenen aangeven en  waarvoor zij vervolgens geen juridische, fiscale, commerciële, economische of  andere legitieme redenen kunnen of willen aanhalen;

k)  situaties waarin zonder juridische, fiscale, commerciële, economische of andere  legitieme redenen een gevolmachtigde wordt ingezet (bv. een vriend of familielid  wordt genoemd als eigenaar van eigendommen/activa terwijl het duidelijk is dat de  vriend of het familielid instructies krijgt van de uiteindelijke begunstigde);

l)  betalingen ontvangen van niet-verbonden of onbekende derden en betalingen voor  honoraria in contanten terwijl deze betalingswijze normaal niet zou worden  gebruikt;

m)  commerciële, onderhandse of vastgoedtransacties of diensten die door de cliënt  moeten worden uitgevoerd zonder duidelijke legitieme zakelijke, economische,  fiscale of juridische redenen of redenen van familiaal bestuur;

n)  bestaande vermoedens over frauduleuze transacties of transacties waarvoor op  ongepaste wijze verantwoording wordt afgelegd. Dit kan gaan om:

i.  over- of onderfacturatie van goederen/diensten

ii.  meervoudige facturatie van dezelfde goederen/diensten

iii.  foutief omschreven goederen/diensten – te grote en te kleine zendingen (bv.  foutieve vermeldingen op connossementen)

iv.  meervoudige verhandeling van dezelfde goederen/diensten.

Algemene risicofactoren

Bij het beoordelen of een welbepaalde transactie of een welbepaalde cliënt al dan niet een  bepaald risico inhoudt, dient het kantoor niet alleen rekening te houden met de hierboven  vermelde (verhogende) risicofactoren maar ook met volgende meer algemene factoren

22.4.1. Risicoverhogende algemene factoren

➢ Niet-verklaarbare hoogdringendheid.

➢ Ongebruikelijke complexiteit van de cliënt of verrichtingen

➢ Onregelmatige zeer korte duur van de zakelijke relatie (beperkte contacten bij

éénmalige opdrachten kan een hoger risico met zich meebrengen).

22.4.2. Risicoverlagende algemene factoren

➢ een tussenkomst of controle door toezichthoudende instanties;  ➢ een tussenkomst van adequaat gereguleerde financiële instellingen of niet-

financiële beroepen;  ➢ het regelmatige karakter of de duur van de zakenrelatie: langdurige zakenrelaties

met frequente klantencontacten tijdens de volledige duur van de relatie houden  mogelijk minder risico’s in;  ➢ cliënten met een integere reputatie;  ➢ vennootschappen die transparant zijn en die goed gekend zijn voor de

buitenwereld;  ➢ vertrouwdheid van ons kantoor met een land, met inbegrip van de kennis van de

plaatselijke wet- en regelgeving, alsook de structuur en het belang van de van  toezichthoudende instanties uitgaande controle.

➢ Bjjlage II AWW
